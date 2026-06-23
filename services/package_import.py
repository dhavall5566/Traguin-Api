from __future__ import annotations

from sqlalchemy.orm import Session

from schemas.media import MediaAssetCreate
from schemas.package_import import (
    ExtractedPackageBundle,
    PackageImportExtractResponse,
    SourcedPlaceImage,
)
from services.groq_extract import extract_package_from_text
from services.package_import_commit import ensure_unique_slug, get_or_create_media_asset
from services.package_import_naming import apply_generated_names
from services.stock_images import place_media_slug, search_place_image
from utils.pdf_extract import extract_pdf_text
from utils.slugify import slugify

from models.destinations import Destination
from models.itineraries import Itinerary
from models.packages import Package


def _normalize_slugs(bundle: ExtractedPackageBundle) -> ExtractedPackageBundle:
    data = bundle.model_dump()
    dest = data["destination"]
    pkg = data["package"]
    itin = data["itinerary"]
    dest["slug"] = dest.get("slug") or slugify(dest["name"])
    pkg["slug"] = pkg.get("slug") or slugify(pkg["title"])
    itin["slug"] = itin.get("slug") or slugify(itin["title"])
    if dest.get("is_domestic") is True:
        dest["region"] = "domestic"
    return ExtractedPackageBundle.model_validate(data)


def _source_images(db: Session, places: list[str], warnings: list[str]) -> list[SourcedPlaceImage]:
    results: list[SourcedPlaceImage] = []
    seen: set[str] = set()
    for place in places:
        key = place.strip().lower()
        if not key or key in seen:
            continue
        seen.add(key)
        image = search_place_image(place.strip())
        if image.error:
            warnings.append(f"Image for '{place}': {image.error}")
            results.append(image)
            continue
        if not image.url:
            warnings.append(f"Image for '{place}': missing URL.")
            results.append(image)
            continue

        asset = get_or_create_media_asset(
            db,
            MediaAssetCreate(
                slug=place_media_slug(place),
                url=image.url,
                alt_text=place,
                mime_type="image/jpeg",
                width=image.width,
                height=image.height,
                source="pexels",
                usage="package_destination_photo",
                tags=["package_destination_photo", slugify(place, max_length=64)],
            ),
        )
        image.media_asset_id = asset.id
        results.append(image)
    return results


def _resolve_unique_catalog_slugs(db: Session, bundle: ExtractedPackageBundle) -> ExtractedPackageBundle:
    package_slug = ensure_unique_slug(db, Package, bundle.package.slug or slugify(bundle.package.title))
    itinerary_slug = ensure_unique_slug(
        db,
        Itinerary,
        bundle.itinerary.slug or slugify(f"{package_slug}-itinerary"),
    )
    return bundle.model_copy(
        update={
            "package": bundle.package.model_copy(update={"slug": package_slug}),
            "itinerary": bundle.itinerary.model_copy(update={"slug": itinerary_slug}),
        }
    )


def run_package_import_extract(
    db: Session,
    *,
    filename: str,
    file_bytes: bytes,
    fetch_images: bool = True,
) -> PackageImportExtractResponse:
    warnings: list[str] = []
    raw_text = extract_pdf_text(file_bytes)
    bundle, llm_raw = extract_package_from_text(raw_text)
    bundle = apply_generated_names(bundle)
    bundle = _normalize_slugs(bundle)
    bundle = _resolve_unique_catalog_slugs(db, bundle)

    images: list[SourcedPlaceImage] = []
    try:
        if fetch_images and bundle.places_mentioned:
            images = _source_images(db, bundle.places_mentioned, warnings)
            if not images and not warnings:
                warnings.append("No images sourced.")
        elif fetch_images:
            warnings.append("No places_mentioned extracted; skipped image search.")

        existing_destination = (
            db.query(Destination).filter_by(slug=bundle.destination.slug).one_or_none()
        )
        if existing_destination:
            warnings.append(
                f"Destination '{existing_destination.name}' already exists — Save will add a new package under it."
            )

        db.commit()
    except Exception:
        db.rollback()
        raise

    return PackageImportExtractResponse(
        filename=filename,
        raw_text=raw_text,
        raw_text_char_count=len(raw_text),
        extracted=bundle,
        llm_raw_json=llm_raw,
        images=images,
        warnings=warnings,
    )
