from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.itineraries import Itinerary
from models.media import MediaAsset
from models.packages import Package
from services.itineraries import sync_itinerary_gallery
from services.media_upload import ingest_remote_image_url, is_local_media_url
from services.pexels_images import PexelsError, search_pexels_photo
from utils.slugify import slugify


def get_or_create_pexels_media(
    db: Session,
    *,
    slug_key: str,
    query: str,
    alt_text: str | None = None,
    usage: str = "package",
    tags: list[str] | None = None,
    exclude_urls: set[str] | None = None,
    exclude_pexels_ids: set[int] | None = None,
    request_base_url: str | None = None,
) -> MediaAsset | None:
    slug = slugify(f"pexels-{slug_key}")[:255]
    existing = db.scalar(select(MediaAsset).where(MediaAsset.slug == slug))
    if existing is not None and is_local_media_url(existing.url):
        blocked_urls = exclude_urls or set()
        if existing.url not in blocked_urls:
            return existing

    try:
        photo = search_pexels_photo(
            query,
            exclude_urls=exclude_urls,
            exclude_pexels_ids=exclude_pexels_ids,
        )
    except PexelsError:
        raise
    except Exception:
        return None

    if photo is None:
        return None

    _, mime_type, local_url = ingest_remote_image_url(photo["url"], request_base_url=request_base_url)
    merged_tags = list(tags or [])
    if "pexels" not in merged_tags:
        merged_tags.append("pexels")

    if existing is not None:
        existing.url = local_url
        existing.alt_text = alt_text or photo["alt_text"]
        existing.width = photo.get("width")
        existing.height = photo.get("height")
        existing.mime_type = mime_type
        existing.source = "upload"
        existing.tags = merged_tags
        db.flush()
        return existing

    asset = MediaAsset(
        slug=slug,
        url=local_url,
        alt_text=alt_text or photo["alt_text"],
        width=photo.get("width"),
        height=photo.get("height"),
        mime_type=mime_type,
        source="upload",
        usage=usage,
        tags=merged_tags,
    )
    db.add(asset)
    db.flush()
    return asset


def _dedupe_media_assets(assets: list[MediaAsset]) -> list[MediaAsset]:
    seen_urls: set[str] = set()
    unique: list[MediaAsset] = []
    for asset in assets:
        if asset.url in seen_urls:
            continue
        seen_urls.add(asset.url)
        unique.append(asset)
    return unique


def attach_pexels_images(
    db: Session,
    image_specs: list[dict[str, str | list[str]]],
    *,
    global_used_urls: set[str] | None = None,
    request_base_url: str | None = None,
) -> list[MediaAsset]:
    assets: list[MediaAsset] = []
    used_urls: set[str] = set(global_used_urls or ())
    used_pexels_ids: set[int] = set()

    for index, spec in enumerate(image_specs):
        slug_key = str(spec.get("slug") or f"image-{index + 1}")
        query = str(spec["query"])
        alt = spec.get("alt")
        alt_text = str(alt) if alt else None
        raw_tags = spec.get("tags")
        tags = list(raw_tags) if isinstance(raw_tags, list) else None
        asset = get_or_create_pexels_media(
            db,
            slug_key=slug_key,
            query=query,
            alt_text=alt_text,
            usage=str(spec.get("usage") or "package"),
            tags=tags,
            exclude_urls=used_urls,
            exclude_pexels_ids=used_pexels_ids,
            request_base_url=request_base_url,
        )
        if asset is None:
            continue

        if asset.url in used_urls:
            continue

        used_urls.add(asset.url)
        assets.append(asset)

    if global_used_urls is not None:
        global_used_urls.update(used_urls)

    return assets


def apply_pexels_images_to_package(
    db: Session,
    *,
    package: Package,
    itinerary: Itinerary | None,
    image_specs: list[dict[str, str | list[str]]],
    global_used_urls: set[str] | None = None,
    request_base_url: str | None = None,
) -> list[MediaAsset]:
    assets = _dedupe_media_assets(
        attach_pexels_images(
            db,
            image_specs,
            global_used_urls=global_used_urls,
            request_base_url=request_base_url,
        )
    )
    if not assets:
        return []

    hero = assets[0]
    package.hero_media_id = hero.id
    if itinerary is not None:
        itinerary.hero_media_id = hero.id
        sync_itinerary_gallery(db, itinerary, [asset.id for asset in assets])

    return assets
