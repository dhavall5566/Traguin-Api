from __future__ import annotations

import sys

from sqlalchemy import select
from sqlalchemy.orm import Session

from database import SessionLocal
from models.destinations import Destination
from models.itineraries import Itinerary
from models.packages import Package
from schemas.itineraries import ItineraryCreate
from schemas.packages import PackageCreate
from services.itineraries import (
    itinerary_query_with_nested,
    sync_itinerary_days,
    sync_itinerary_highlights,
    sync_itinerary_hotels,
    sync_itinerary_inclusions,
    sync_itinerary_nested_content,
)
from services.media_from_pexels import apply_pexels_images_to_package
from services.packages import package_query_with_nested, sync_package_highlights, sync_package_moods
from services.travel_moods import travel_moods_for_package
from utils.db import commit_or_raise


def upsert_gujarat_package(
    db: Session,
    *,
    destination_id: str,
    package: PackageCreate,
    itinerary: ItineraryCreate,
    image_specs: list[dict[str, str | list[str]]],
    global_used_urls: set[str] | None = None,
) -> tuple[Package, Itinerary, list]:
    destination = db.get(Destination, destination_id)
    if destination is None:
        raise RuntimeError(f"Destination not found: {destination_id}")

    existing_pkg = db.scalar(select(Package).where(Package.slug == package.slug))
    moods = travel_moods_for_package(package.slug, package.moods)
    if existing_pkg:
        print(f"Package already exists: {package.slug} ({existing_pkg.id})")
        pkg_row = existing_pkg
        current_moods = [m.mood for m in pkg_row.moods]
        if current_moods != moods:
            sync_package_moods(db, pkg_row, moods)
            print(f"  Updated moods: {current_moods} -> {moods}")
    else:
        pkg_data = package.model_dump()
        highlights = pkg_data.pop("highlights")
        pkg_data.pop("moods", None)
        pkg_row = Package(**pkg_data)
        db.add(pkg_row)
        db.flush()
        sync_package_highlights(db, pkg_row, highlights)
        sync_package_moods(db, pkg_row, moods)
        print(f"Created package: {pkg_row.slug} ({pkg_row.id})")

    existing_itin = db.scalar(select(Itinerary).where(Itinerary.slug == itinerary.slug))
    if existing_itin:
        print(f"Itinerary already exists: {itinerary.slug} ({existing_itin.id})")
        itin_row = itinerary_query_with_nested(db).filter_by(id=existing_itin.id).one()
        if itin_row.package_id != pkg_row.id:
            itin_row.package_id = pkg_row.id
        sync_itinerary_nested_content(db, itin_row, itinerary)
        print(
            f"  Synced nested content: highlights={len(itinerary.highlights)} "
            f"days={len(itinerary.days)} hotels={len(itinerary.hotels)} "
            f"inclusions={len(itinerary.inclusions)}"
        )
    else:
        itin_data = itinerary.model_dump()
        itin_data["package_id"] = pkg_row.id
        highlights = itin_data.pop("highlights")
        days = itin_data.pop("days")
        hotels = itin_data.pop("hotels")
        inclusions = itin_data.pop("inclusions")
        itin_data.pop("gallery_media_ids", None)

        itin_row = Itinerary(**itin_data)
        db.add(itin_row)
        db.flush()
        sync_itinerary_highlights(db, itin_row, highlights)
        sync_itinerary_days(db, itin_row, days)
        sync_itinerary_hotels(db, itin_row, hotels)
        sync_itinerary_inclusions(db, itin_row, inclusions)
        print(f"Created itinerary: {itin_row.slug} ({itin_row.id})")

    assets = apply_pexels_images_to_package(
        db,
        package=pkg_row,
        itinerary=itin_row,
        image_specs=image_specs,
        global_used_urls=global_used_urls,
    )
    commit_or_raise(db)

    itin_row = itinerary_query_with_nested(db).filter_by(id=itin_row.id).one()
    pkg_row = package_query_with_nested(db).filter_by(id=pkg_row.id).one()
    print(f"Linked package {pkg_row.slug} -> itinerary {itin_row.slug}")
    print(
        f"Days: {len(itin_row.days)} | Hotels: {len(itin_row.hotels)} | "
        f"Inclusions: {len(itin_row.inclusions)}"
    )
    if assets:
        print(f"Pexels images attached: {len(assets)} (hero: {assets[0].slug})")
    else:
        print("Warning: no Pexels images were attached (check PEXELS_API_KEY).")
    return pkg_row, itin_row, assets


def run_gujarat_package_inserts(
    *,
    destination_id: str,
    packages: list[tuple[PackageCreate, ItineraryCreate, list[dict[str, str | list[str]]]]],
) -> None:
    global_used_urls: set[str] = set()
    with SessionLocal() as db:
        for package, itinerary, image_specs in packages:
            print(f"\n--- {package.slug} ---")
            try:
                upsert_gujarat_package(
                    db,
                    destination_id=destination_id,
                    package=package,
                    itinerary=itinerary,
                    image_specs=image_specs,
                    global_used_urls=global_used_urls,
                )
            except Exception as exc:
                print(f"Failed {package.slug}: {exc}", file=sys.stderr)
                raise


def upsert_package_without_images(
    db: Session,
    *,
    destination_id: str,
    package: PackageCreate,
    itinerary: ItineraryCreate,
) -> tuple[Package, Itinerary, list]:
    """Upsert package + itinerary without attaching Pexels images."""
    return upsert_gujarat_package(
        db,
        destination_id=destination_id,
        package=package,
        itinerary=itinerary,
        image_specs=[],
    )
