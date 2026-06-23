from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.gallery import ClientStory, GalleryCategory, GalleryItem
from schemas.gallery import ClientStoryRead, GalleryCategoryRead, GalleryItemRead
from schemas.pagination import PaginatedResponse
from services.gallery import gallery_item_query_with_categories, gallery_item_to_read
from utils.pagination import paginate

client_stories_router = APIRouter()
gallery_categories_router = APIRouter()
gallery_items_router = APIRouter()


@client_stories_router.get("", response_model=PaginatedResponse[ClientStoryRead])
def list_client_stories(
    show_on_home: bool | None = Query(default=None),
    show_in_gallery: bool | None = Query(default=None),
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(ClientStory).filter(ClientStory.is_published.is_(True))
    if show_on_home is not None:
        query = query.filter(ClientStory.show_on_home.is_(show_on_home))
    if show_in_gallery is not None:
        query = query.filter(ClientStory.show_in_gallery.is_(show_in_gallery))
    query = query.order_by(ClientStory.home_sort_order.nulls_last(), ClientStory.client_name)
    return paginate(query, limit, offset, transform=ClientStoryRead.model_validate)


@client_stories_router.get("/{story_id}", response_model=ClientStoryRead)
def get_client_story(story_id: UUID, db: Session = Depends(get_db)):
    item = db.get(ClientStory, story_id)
    if item is None or not item.is_published:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client story not found.")
    return item


@gallery_categories_router.get("", response_model=PaginatedResponse[GalleryCategoryRead])
def list_gallery_categories(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(GalleryCategory).order_by(GalleryCategory.sort_order, GalleryCategory.label)
    return paginate(query, limit, offset, transform=GalleryCategoryRead.model_validate)


@gallery_categories_router.get("/{category_id}", response_model=GalleryCategoryRead)
def get_gallery_category(category_id: UUID, db: Session = Depends(get_db)):
    item = db.get(GalleryCategory, category_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gallery category not found.")
    return item


@gallery_items_router.get("", response_model=PaginatedResponse[GalleryItemRead])
def list_gallery_items(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = (
        gallery_item_query_with_categories(db)
        .filter(GalleryItem.is_published.is_(True))
        .order_by(GalleryItem.sort_order.nulls_last(), GalleryItem.place)
    )
    return paginate(query, limit, offset, transform=gallery_item_to_read)


@gallery_items_router.get("/slug/{slug}", response_model=GalleryItemRead)
def get_gallery_item_by_slug(slug: str, db: Session = Depends(get_db)):
    item = (
        gallery_item_query_with_categories(db)
        .filter_by(slug=slug, is_published=True)
        .one_or_none()
    )
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gallery item not found.")
    return gallery_item_to_read(item)
