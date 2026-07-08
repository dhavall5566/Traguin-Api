from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session, selectinload

from models.destinations import Destination
from models.itineraries import (
    Itinerary,
    ItineraryDay,
    ItineraryHighlight,
    ItineraryHotel,
    ItineraryInclusion,
    ItineraryMedia,
)
from models.media import MediaAsset
from models.packages import Package
from schemas.itineraries import (
    ItineraryCreate,
    ItineraryDayRead,
    ItineraryHighlightRead,
    ItineraryHotelRead,
    ItineraryInclusionRead,
    ItineraryListRead,
    ItineraryRead,
)
from schemas.media import MediaSummary
from utils.orm_read import orm_read_with_nested
from utils.package_codes import serial_code_from_slug
from utils.package_title import clean_package_title


def itinerary_query_with_nested(db: Session):
    return db.query(Itinerary).options(
        selectinload(Itinerary.package),
        selectinload(Itinerary.highlights),
        selectinload(Itinerary.days),
        selectinload(Itinerary.hotels),
        selectinload(Itinerary.inclusions),
        selectinload(Itinerary.gallery_media).selectinload(ItineraryMedia.media),
    )


def itinerary_list_query(db: Session):
    return (
        db.query(
            Itinerary,
            Destination.name.label("destination_name"),
            Package.title.label("package_title"),
            Package.serial_code.label("package_serial_code"),
        )
        .join(Destination, Itinerary.destination_id == Destination.id)
        .outerjoin(Package, Itinerary.package_id == Package.id)
    )


def itinerary_to_list_read(row: tuple[Itinerary, str, str | None, str | None]) -> ItineraryListRead:
    itinerary, destination_name, package_title, package_serial_code = row
    serial_code = package_serial_code or serial_code_from_slug(itinerary.slug)
    return ItineraryListRead(
        id=itinerary.id,
        created_at=itinerary.created_at,
        updated_at=itinerary.updated_at,
        slug=itinerary.slug,
        serial_code=serial_code,
        package_id=itinerary.package_id,
        package_title=clean_package_title(package_title) if package_title else package_title,
        destination_id=itinerary.destination_id,
        destination_name=destination_name,
        title=clean_package_title(itinerary.title) or itinerary.title,
        duration_label=itinerary.duration_label,
        duration_days=itinerary.duration_days,
        starting_price=itinerary.starting_price,
        price_note=itinerary.price_note,
        is_featured=itinerary.is_featured,
        featured_sort_order=itinerary.featured_sort_order,
        is_published=itinerary.is_published,
    )


def sync_itinerary_highlights(db: Session, itinerary: Itinerary, highlights: list) -> None:
    itinerary.highlights.clear()
    for item in highlights:
        data = item.model_dump() if hasattr(item, "model_dump") else item
        itinerary.highlights.append(ItineraryHighlight(**data))


def sync_itinerary_days(db: Session, itinerary: Itinerary, days: list) -> None:
    itinerary.days.clear()
    db.flush()
    for item in days:
        data = item.model_dump() if hasattr(item, "model_dump") else item
        itinerary.days.append(ItineraryDay(**data))


def sync_itinerary_hotels(db: Session, itinerary: Itinerary, hotels: list) -> None:
    itinerary.hotels.clear()
    for item in hotels:
        data = item.model_dump() if hasattr(item, "model_dump") else item
        itinerary.hotels.append(ItineraryHotel(**data))


def sync_itinerary_inclusions(db: Session, itinerary: Itinerary, inclusions: list) -> None:
    itinerary.inclusions.clear()
    for item in inclusions:
        data = item.model_dump() if hasattr(item, "model_dump") else item
        itinerary.inclusions.append(ItineraryInclusion(**data))


def sync_itinerary_nested_content(db: Session, itinerary: Itinerary, source: ItineraryCreate) -> None:
    """Replace highlights, days, hotels, and inclusions on an existing itinerary."""
    sync_itinerary_highlights(db, itinerary, source.highlights)
    sync_itinerary_days(db, itinerary, source.days)
    sync_itinerary_hotels(db, itinerary, source.hotels)
    sync_itinerary_inclusions(db, itinerary, source.inclusions)


def sync_itinerary_gallery(
    db: Session,
    itinerary: Itinerary,
    media_ids: list[UUID],
) -> None:
    if not media_ids:
        itinerary.gallery_media.clear()
        return

    assets = db.query(MediaAsset).filter(MediaAsset.id.in_(media_ids)).all()
    found_ids = {asset.id for asset in assets}
    missing = [str(media_id) for media_id in media_ids if media_id not in found_ids]
    if missing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unknown gallery_media_ids: {', '.join(missing)}",
        )

    order_by_id = {media_id: index for index, media_id in enumerate(media_ids)}
    itinerary.gallery_media.clear()
    for asset in assets:
        itinerary.gallery_media.append(
            ItineraryMedia(media_id=asset.id, sort_order=order_by_id[asset.id])
        )


def itinerary_to_read(itinerary: Itinerary) -> ItineraryRead:
    highlights = [
        ItineraryHighlightRead.model_validate(h)
        for h in sorted(itinerary.highlights, key=lambda x: x.sort_order)
    ]
    days = [
        ItineraryDayRead.model_validate(d)
        for d in sorted(itinerary.days, key=lambda x: (x.sort_order, x.day_number))
    ]
    hotels = [
        ItineraryHotelRead.model_validate(h)
        for h in sorted(itinerary.hotels, key=lambda x: x.sort_order)
    ]
    inclusions = [
        ItineraryInclusionRead.model_validate(i)
        for i in sorted(itinerary.inclusions, key=lambda x: x.sort_order)
    ]
    gallery_media = [
        MediaSummary(
            id=link.media.id,
            url=link.media.url,
            alt_text=link.media.alt_text,
            sort_order=link.sort_order,
        )
        for link in sorted(itinerary.gallery_media, key=lambda x: x.sort_order)
        if link.media is not None
    ]
    read = orm_read_with_nested(
        ItineraryRead,
        itinerary,
        nested={
            "highlights": highlights,
            "days": days,
            "hotels": hotels,
            "inclusions": inclusions,
            "gallery_media": gallery_media,
        },
    )
    if read.title:
        read.title = clean_package_title(read.title) or read.title
    linked_package = getattr(itinerary, "package", None)
    if linked_package is not None and linked_package.hero_media_id is not None:
        read.package_hero_media_id = linked_package.hero_media_id
    return read
