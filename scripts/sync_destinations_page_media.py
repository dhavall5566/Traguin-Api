#!/usr/bin/env python3
"""
Mirror traguin.in/destinations gallery images into CMS media and link records.

Downloads curated gallery URLs (same sources as the public website), stores them
locally via media_assets, and attaches hero + gallery to destinations, packages,
and itineraries.

Run from api/:
  python scripts/sync_destinations_page_media.py --dry-run
  python scripts/sync_destinations_page_media.py
  python scripts/sync_destinations_page_media.py --force
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from uuid import UUID

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import select
from sqlalchemy.orm import selectinload

import services.package_image_specs as package_image_specs
from config import settings
from database import SessionLocal
from models.destinations import Destination, DestinationMedia
from models.itineraries import Itinerary
from models.media import MediaAsset
from models.packages import Package
from services.destination_page_galleries import gallery_urls_for_destination_slug
from services.destinations import sync_destination_gallery
from services.itineraries import sync_itinerary_gallery
from services.media_from_pexels import apply_pexels_images_to_package
from services.media_upload import ingest_remote_image_url, is_local_media_url
from utils.db import commit_or_raise
from utils.slugify import slugify


def package_spec_key(slug: str) -> str | None:
    parts = slug.split("-")
    if len(parts) < 2:
        return None
    return f"{parts[0]}_{parts[1]}".upper()


def load_package_image_specs() -> dict[str, list[dict]]:
    mapping: dict[str, list[dict]] = {}
    for name in dir(package_image_specs):
        if not name.endswith("_PEXELS_IMAGES"):
            continue
        key = name.replace("_PEXELS_IMAGES", "")
        mapping[key] = getattr(package_image_specs, name)
    return mapping


def normalize_url(url: str) -> str:
    return (url or "").strip().split("?", 1)[0]


def get_or_create_media_from_url(
    db,
    *,
    url: str,
    slug: str,
    alt_text: str,
    usage: str,
    tags: list[str],
    request_base_url: str,
    dry_run: bool,
) -> MediaAsset | None:
    asset = db.scalar(select(MediaAsset).where(MediaAsset.slug == slug))
    if asset is not None and is_local_media_url(asset.url):
        return asset

    if dry_run:
        print(f"    [dry-run] would ingest {slug} <- {url[:90]}")
        return asset

    try:
        _, mime_type, local_url = ingest_remote_image_url(url, request_base_url=request_base_url)
    except Exception as exc:
        print(f"    skipped {slug}: {exc}")
        return None
    if asset is None:
        asset = MediaAsset(
            slug=slug,
            url=local_url,
            alt_text=alt_text,
            mime_type=mime_type,
            source="upload",
            usage=usage,
            tags=tags,
        )
        db.add(asset)
    else:
        asset.url = local_url
        asset.alt_text = alt_text
        asset.mime_type = mime_type
        asset.source = "upload"
        asset.tags = tags
    db.flush()
    return asset


def ingest_gallery_assets(
    db,
    *,
    slug_prefix: str,
    name: str,
    urls: list[str],
    usage: str,
    request_base_url: str,
    dry_run: bool,
) -> list[MediaAsset]:
    assets: list[MediaAsset] = []
    seen: set[str] = set()
    for index, url in enumerate(urls[:5]):
        normalized = normalize_url(url)
        if normalized in seen:
            continue
        seen.add(normalized)
        asset = get_or_create_media_from_url(
            db,
            url=url,
            slug=slugify(f"{slug_prefix}-gallery-{index + 1}")[:255],
            alt_text=f"{name} — photo {index + 1}",
            usage=usage,
            tags=[slug_prefix, usage, "destinations-page"],
            request_base_url=request_base_url,
            dry_run=dry_run,
        )
        if asset is not None:
            assets.append(asset)
    if not assets:
        print(f"    warning: no assets ingested for {slug_prefix}")
    return assets


def attach_destination_media(
    db,
    destination: Destination,
    *,
    request_base_url: str,
    dry_run: bool,
    force: bool,
) -> list[MediaAsset]:
    if destination.hero_media_id and not force:
        loaded = db.scalar(
            select(Destination)
            .where(Destination.id == destination.id)
            .options(selectinload(Destination.gallery_media).selectinload(DestinationMedia.media))
        )
        if loaded:
            assets = [
                link.media
                for link in sorted(loaded.gallery_media, key=lambda item: item.sort_order)
                if link.media is not None
            ]
            if assets:
                return assets
        hero = db.get(MediaAsset, destination.hero_media_id)
        return [hero] if hero else []

    urls = gallery_urls_for_destination_slug(
        destination.slug,
        region=destination.region,
        india_region=destination.india_region,
    )
    assets = ingest_gallery_assets(
        db,
        slug_prefix=destination.slug,
        name=destination.name,
        urls=urls,
        usage="destination",
        request_base_url=request_base_url,
        dry_run=dry_run,
    )
    if dry_run or not assets:
        print(f"  destination {destination.slug}: {len(urls)} url(s)")
        return assets

    destination.hero_media_id = assets[0].id
    sync_destination_gallery(db, destination, [asset.id for asset in assets])
    print(f"  destination {destination.slug}: hero + {len(assets)} gallery")
    return assets


def attach_package_and_itinerary(
    db,
    package: Package,
    itinerary: Itinerary | None,
    destination_assets: list[MediaAsset],
    package_specs: dict[str, list[dict]],
    *,
    package_index: int,
    request_base_url: str,
    dry_run: bool,
    force: bool,
) -> None:
    if package.hero_media_id and not force:
        return

    spec_key = package_spec_key(package.slug)
    specs = package_specs.get(spec_key or "")

    if specs and not dry_run:
        try:
            apply_pexels_images_to_package(
                db,
                package=package,
                itinerary=itinerary,
                image_specs=specs,
                request_base_url=request_base_url,
            )
            print(f"  package {package.slug}: pexels specs ({len(specs)} images)")
        except Exception as exc:
            print(f"  package {package.slug}: pexels failed ({exc}); using destination gallery")
            specs = None
        else:
            return

    if specs and dry_run:
        print(f"  package {package.slug}: would apply pexels specs ({len(specs)} images)")
        return

    if not destination_assets:
        print(f"  package {package.slug}: skipped (no destination gallery)")
        return

    if dry_run:
        hero = destination_assets[package_index % len(destination_assets)]
        print(f"  package {package.slug}: would use destination gallery hero {hero.slug}")
        return

    hero = destination_assets[package_index % len(destination_assets)]
    package.hero_media_id = hero.id
    gallery_ids = [asset.id for asset in destination_assets]
    if itinerary is not None:
        itinerary.hero_media_id = hero.id
        sync_itinerary_gallery(db, itinerary, gallery_ids)
    print(f"  package {package.slug}: linked destination gallery ({len(gallery_ids)} images)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync /destinations page images into CMS media.")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without writing.")
    parser.add_argument("--force", action="store_true", help="Replace existing hero/gallery links.")
    parser.add_argument(
        "--base",
        default=settings.api_public_base_url or "https://api.traguin.in",
        help="Public API base for uploaded media URLs.",
    )
    args = parser.parse_args()
    base = args.base.rstrip("/")
    package_specs = load_package_image_specs()

    db = SessionLocal()
    try:
        destinations = db.scalars(
            select(Destination)
            .where(Destination.is_published.is_(True))
            .order_by(Destination.slug)
        ).all()

        dest_assets_by_id: dict[UUID, list[MediaAsset]] = {}
        print(f"Destinations ({len(destinations)})")
        for destination in destinations:
            assets = attach_destination_media(
                db,
                destination,
                request_base_url=base,
                dry_run=args.dry_run,
                force=args.force,
            )
            if assets:
                dest_assets_by_id[destination.id] = assets

        packages = db.scalars(
            select(Package)
            .where(Package.is_published.is_(True))
            .order_by(Package.slug)
        ).all()
        itineraries = db.scalars(select(Itinerary)).all()
        itinerary_by_package = {it.package_id: it for it in itineraries if it.package_id}

        packages_by_destination: dict[UUID, list[Package]] = {}
        for package in packages:
            packages_by_destination.setdefault(package.destination_id, []).append(package)

        print(f"\nPackages ({len(packages)})")
        for destination_id, dest_packages in packages_by_destination.items():
            cached_assets = dest_assets_by_id.get(destination_id)
            if cached_assets is None and not args.dry_run:
                destination = db.get(Destination, destination_id)
                if destination is None:
                    continue
                cached_assets = ingest_gallery_assets(
                    db,
                    slug_prefix=destination.slug,
                    name=destination.name,
                    urls=gallery_urls_for_destination_slug(
                        destination.slug,
                        region=destination.region,
                        india_region=destination.india_region,
                    ),
                    usage="destination",
                    request_base_url=base,
                    dry_run=False,
                )
                dest_assets_by_id[destination_id] = cached_assets

            for index, package in enumerate(sorted(dest_packages, key=lambda item: item.slug)):
                itinerary = itinerary_by_package.get(package.id)
                attach_package_and_itinerary(
                    db,
                    package,
                    itinerary,
                    cached_assets or [],
                    package_specs,
                    package_index=index,
                    request_base_url=base,
                    dry_run=args.dry_run,
                    force=args.force,
                )

        if args.dry_run:
            print("\nDry run complete — no database changes.")
            return

        commit_or_raise(db)
        print("\nDone — media linked in database.")
        print(f"Upload files are in: {settings.media_upload_dir}")
        print("Sync uploads to production: rsync -avz api/uploads/media/ user@195.35.7.208:/www/wwwroot/api/uploads/media/")
    finally:
        db.close()


if __name__ == "__main__":
    main()
