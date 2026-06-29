from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session, joinedload, selectinload

from models.gallery import ClientStory, GalleryCategory, GalleryItem, GalleryItemCategory, GalleryItemMedia
from schemas.gallery import ClientStoryRead
from models.media import MediaAsset
from schemas.gallery import GalleryCategorySummary, GalleryItemRead
from schemas.media import MediaSummary
from utils.orm_read import orm_read_with_nested


def client_story_query(db: Session):
    return db.query(ClientStory).options(joinedload(ClientStory.destination))


def client_story_to_read(story: ClientStory) -> ClientStoryRead:
    destination_name = story.destination.name if story.destination else None
    return orm_read_with_nested(
        ClientStoryRead,
        story,
        nested={"destination_name": destination_name},
    )


def gallery_item_query_with_categories(db: Session):
    return db.query(GalleryItem).options(
        selectinload(GalleryItem.category_links).selectinload(GalleryItemCategory.category),
        selectinload(GalleryItem.gallery_media).selectinload(GalleryItemMedia.media),
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


def sync_gallery_item_media(
    db: Session,
    gallery_item: GalleryItem,
    media_ids: list[UUID],
) -> None:
    if not media_ids:
        gallery_item.gallery_media.clear()
        gallery_item.media_id = None
        return

    assets = db.query(MediaAsset).filter(MediaAsset.id.in_(media_ids)).all()
    found_ids = {asset.id for asset in assets}
    missing = [str(media_id) for media_id in media_ids if media_id not in found_ids]
    if missing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unknown media_ids: {', '.join(missing)}",
        )

    order_by_id = {media_id: index for index, media_id in enumerate(media_ids)}
    gallery_item.gallery_media.clear()
    for asset in sorted(assets, key=lambda row: order_by_id[row.id]):
        gallery_item.gallery_media.append(
            GalleryItemMedia(media_id=asset.id, sort_order=order_by_id[asset.id])
        )
    gallery_item.media_id = media_ids[0]


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
    media = [
        MediaSummary(
            id=link.media.id,
            url=link.media.url,
            alt_text=link.media.alt_text,
            sort_order=link.sort_order,
        )
        for link in sorted(gallery_item.gallery_media, key=lambda row: row.sort_order)
        if link.media is not None
    ]
    return orm_read_with_nested(
        GalleryItemRead,
        gallery_item,
        nested={"categories": categories, "media": media},
    )
