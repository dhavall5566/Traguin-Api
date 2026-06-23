from __future__ import annotations

from uuid import UUID

from sqlalchemy.orm import Session

from models.destinations import Destination
from models.itineraries import Itinerary
from models.media import MediaAsset
from models.packages import Package
from schemas.destination import DestinationCreate
from schemas.itineraries import ItineraryCreate
from schemas.media import MediaAssetCreate
from schemas.package_import import PackageImportCommitRequest, PackageImportCommitResponse
from schemas.packages import PackageCreate
from services.destinations import (
    resolve_import_category_ids,
    sync_destination_categories,
    sync_destination_gallery,
)
from services.itineraries import (
    sync_itinerary_days,
    sync_itinerary_gallery,
    sync_itinerary_highlights,
    sync_itinerary_hotels,
    sync_itinerary_inclusions,
)
from services.packages import sync_package_highlights, sync_package_moods
from utils.db import commit_or_raise
from utils.slugify import slugify


def ensure_unique_slug(db: Session, model, base_slug: str) -> str:
    candidate = slugify(base_slug or "item", max_length=128)
    if not db.query(model).filter_by(slug=candidate).first():
        return candidate

    stem = candidate[:118].rstrip("-") or "item"
    suffix = 2
    while True:
        candidate = slugify(f"{stem}-{suffix}", max_length=128)
        if not db.query(model).filter_by(slug=candidate).first():
            return candidate
        suffix += 1


def _resolve_destination(
    db: Session,
    dest_data: dict,
    category_ids: list,
    gallery_media_ids: list,
) -> Destination:
    slug = dest_data.get("slug")
    existing = db.query(Destination).filter_by(slug=slug).one_or_none() if slug else None
    if existing:
        sync_destination_categories(db, existing, category_ids)
        sync_destination_gallery(db, existing, gallery_media_ids)
        return existing

    destination = Destination(**dest_data)
    db.add(destination)
    db.flush()
    sync_destination_categories(db, destination, category_ids)
    sync_destination_gallery(db, destination, gallery_media_ids)
    return destination


def create_media_asset(db: Session, payload: MediaAssetCreate) -> MediaAsset:
    item = MediaAsset(**payload.model_dump())
    db.add(item)
    db.flush()
    return item


def get_or_create_media_asset(db: Session, payload: MediaAssetCreate) -> MediaAsset:
    slug = payload.slug
    if slug:
        existing = db.query(MediaAsset).filter_by(slug=slug).one_or_none()
        if existing:
            return existing
    return create_media_asset(db, payload)


def commit_package_import(
    db: Session,
    payload: PackageImportCommitRequest,
) -> PackageImportCommitResponse:
    dest_data = payload.destination.model_dump()
    category_ids = resolve_import_category_ids(
        db,
        region=dest_data.get("region") or payload.destination.region,
        category_ids=dest_data.pop("category_ids"),
    )
    gallery_media_ids = dest_data.pop("gallery_media_ids")
    destination = _resolve_destination(db, dest_data, category_ids, gallery_media_ids)

    pkg_data = payload.package.model_dump()
    pkg_data["destination_id"] = destination.id
    pkg_data["slug"] = ensure_unique_slug(db, Package, pkg_data["slug"])
    highlights = pkg_data.pop("highlights")
    moods = pkg_data.pop("moods")
    package = Package(**pkg_data)
    db.add(package)
    db.flush()
    sync_package_highlights(db, package, highlights)
    sync_package_moods(db, package, moods)

    itin_data = payload.itinerary.model_dump()
    itin_data["destination_id"] = destination.id
    itin_data["package_id"] = package.id
    itin_data["slug"] = ensure_unique_slug(db, Itinerary, itin_data["slug"])
    itin_highlights = itin_data.pop("highlights")
    days = itin_data.pop("days")
    hotels = itin_data.pop("hotels")
    inclusions = itin_data.pop("inclusions")
    gallery_ids = itin_data.pop("gallery_media_ids")
    itinerary = Itinerary(**itin_data)
    db.add(itinerary)
    db.flush()
    sync_itinerary_highlights(db, itinerary, itin_highlights)
    sync_itinerary_days(db, itinerary, days)
    sync_itinerary_hotels(db, itinerary, hotels)
    sync_itinerary_inclusions(db, itinerary, inclusions)
    sync_itinerary_gallery(db, itinerary, gallery_ids)

    commit_or_raise(db)

    return PackageImportCommitResponse(
        destination_id=destination.id,
        package_id=package.id,
        itinerary_id=itinerary.id,
        destination_slug=destination.slug,
        package_slug=package.slug,
        itinerary_slug=itinerary.slug,
    )
