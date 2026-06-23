from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session, selectinload

from models.gallery import GalleryCategory, GalleryItem, GalleryItemCategory
from schemas.gallery import GalleryCategorySummary, GalleryItemRead
from utils.orm_read import orm_read_with_nested


def gallery_item_query_with_categories(db: Session):
    return db.query(GalleryItem).options(
        selectinload(GalleryItem.category_links).selectinload(GalleryItemCategory.category),
    )


def sync_gallery_item_categories(
    db: Session,
    gallery_item: GalleryItem,
    category_ids: list[UUID],
) -> None:
    if not category_ids:
        gallery_item.category_links.clear()
        return

    categories = (
        db.query(GalleryCategory).filter(GalleryCategory.id.in_(category_ids)).all()
    )
    found_ids = {category.id for category in categories}
    missing = [str(category_id) for category_id in category_ids if category_id not in found_ids]
    if missing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unknown category_ids: {', '.join(missing)}",
        )

    gallery_item.category_links.clear()
    for category in categories:
        gallery_item.category_links.append(
            GalleryItemCategory(gallery_category_id=category.id)
        )


def gallery_item_to_read(gallery_item: GalleryItem) -> GalleryItemRead:
    categories = [
        GalleryCategorySummary(
            id=link.category.id,
            slug=link.category.slug,
            label=link.category.label,
        )
        for link in gallery_item.category_links
        if link.category is not None
    ]
    return orm_read_with_nested(
        GalleryItemRead,
        gallery_item,
        nested={"categories": categories},
    )
