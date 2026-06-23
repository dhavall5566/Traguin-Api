from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session, selectinload

from models.destinations import (
    Destination,
    DestinationCategory,
    DestinationCategoryAssignment,
    DestinationMedia,
)
from models.media import MediaAsset
from schemas.destination import DestinationCategorySummary, DestinationRead
from schemas.media import MediaSummary
from utils.orm_read import orm_read_with_nested


def destination_query_with_categories(db: Session):
    return db.query(Destination).options(
        selectinload(Destination.category_assignments).selectinload(
            DestinationCategoryAssignment.category
        ),
        selectinload(Destination.gallery_media).selectinload(DestinationMedia.media),
    )


def sync_destination_categories(
    db: Session,
    destination: Destination,
    category_ids: list[UUID],
) -> None:
    if not category_ids:
        destination.category_assignments.clear()
        return

    categories = (
        db.query(DestinationCategory)
        .filter(DestinationCategory.id.in_(category_ids))
        .all()
    )
    found_ids = {category.id for category in categories}
    missing = [str(category_id) for category_id in category_ids if category_id not in found_ids]
    if missing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unknown category_ids: {', '.join(missing)}",
        )

    order_by_id = {category_id: index for index, category_id in enumerate(category_ids)}
    destination.category_assignments.clear()
    for category in categories:
        destination.category_assignments.append(
            DestinationCategoryAssignment(
                category_id=category.id,
                sort_order=order_by_id[category.id],
            )
        )


def sync_destination_gallery(
    db: Session,
    destination: Destination,
    media_ids: list[UUID],
) -> None:
    if not media_ids:
        destination.gallery_media.clear()
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
    destination.gallery_media.clear()
    for asset in assets:
        destination.gallery_media.append(
            DestinationMedia(media_id=asset.id, sort_order=order_by_id[asset.id])
        )


def destination_to_read(destination: Destination) -> DestinationRead:
    categories = [
        DestinationCategorySummary(
            id=assignment.category.id,
            slug=assignment.category.slug,
            title=assignment.category.title,
            sort_order=assignment.sort_order,
        )
        for assignment in sorted(
            destination.category_assignments,
            key=lambda item: (item.sort_order is None, item.sort_order or 0),
        )
        if assignment.category is not None
    ]
    gallery_media = [
        MediaSummary(
            id=link.media.id,
            url=link.media.url,
            alt_text=link.media.alt_text,
            sort_order=link.sort_order,
        )
        for link in sorted(destination.gallery_media, key=lambda item: item.sort_order)
        if link.media is not None
    ]
    return orm_read_with_nested(
        DestinationRead,
        destination,
        nested={"categories": categories, "gallery_media": gallery_media},
    )


INDIAN_ESCAPES_SLUG = "indian-escapes"


def get_or_create_destination_category(
    db: Session,
    *,
    slug: str,
    title: str,
    description: str,
    sort_order: int = 0,
) -> DestinationCategory:
    category = db.query(DestinationCategory).filter_by(slug=slug).one_or_none()
    if category is not None:
        return category

    category = DestinationCategory(
        slug=slug,
        title=title,
        description=description,
        sort_order=sort_order,
    )
    db.add(category)
    db.flush()
    return category


def resolve_import_category_ids(
    db: Session,
    *,
    region: str,
    category_ids: list[UUID],
) -> list[UUID]:
    if category_ids:
        return category_ids

    if region == "domestic":
        category = get_or_create_destination_category(
            db,
            slug=INDIAN_ESCAPES_SLUG,
            title="Indian Escapes",
            description="Diverse landscapes woven into singular luxury journeys.",
            sort_order=20,
        )
        return [category.id]

    return []
