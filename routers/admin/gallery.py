from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.gallery import ClientStory, GalleryCategory, GalleryItem
from schemas.gallery import (
    ClientStoryCreate,
    ClientStoryRead,
    ClientStoryUpdate,
    GalleryCategoryCreate,
    GalleryCategoryRead,
    GalleryCategoryUpdate,
    GalleryItemCreate,
    GalleryItemRead,
    GalleryItemUpdate,
)
from schemas.pagination import PaginatedResponse
from services.gallery import (
    client_story_query,
    client_story_to_read,
    gallery_item_query_with_categories,
    gallery_item_to_read,
    sync_gallery_item_categories,
    sync_gallery_item_media,
)
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

client_stories_router = APIRouter()
gallery_categories_router = APIRouter()
gallery_items_router = APIRouter()


@client_stories_router.get("", response_model=PaginatedResponse[ClientStoryRead])
def list_client_stories(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = client_story_query(db).order_by(
        ClientStory.home_sort_order.nulls_last(),
        ClientStory.gallery_sort_order.nulls_last(),
        ClientStory.client_name,
    )
    return paginate(query, limit, offset, transform=client_story_to_read)


@client_stories_router.get("/{story_id}", response_model=ClientStoryRead)
def get_client_story(story_id: UUID, db: Session = Depends(get_db)):
    item = client_story_query(db).filter_by(id=story_id).one_or_none()
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client story not found.")
    return client_story_to_read(item)


@client_stories_router.post("", response_model=ClientStoryRead, status_code=status.HTTP_201_CREATED)
def create_client_story(payload: ClientStoryCreate, db: Session = Depends(get_db)):
    item = ClientStory(**payload.model_dump())
    db.add(item)
    commit_or_raise(db)
    item = client_story_query(db).filter_by(id=item.id).one()
    return client_story_to_read(item)


@client_stories_router.patch("/{story_id}", response_model=ClientStoryRead)
def update_client_story(
    story_id: UUID,
    payload: ClientStoryUpdate,
    db: Session = Depends(get_db),
):
    item = db.get(ClientStory, story_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client story not found.")
    apply_partial_update(item, payload.model_dump(exclude_unset=True))
    commit_or_raise(db)
    item = client_story_query(db).filter_by(id=item.id).one()
    return client_story_to_read(item)


@client_stories_router.delete("/{story_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_client_story(story_id: UUID, db: Session = Depends(get_db)):
    item = db.get(ClientStory, story_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client story not found.")
    db.delete(item)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


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


@gallery_categories_router.post("", response_model=GalleryCategoryRead, status_code=status.HTTP_201_CREATED)
def create_gallery_category(payload: GalleryCategoryCreate, db: Session = Depends(get_db)):
    item = GalleryCategory(**payload.model_dump())
    db.add(item)
    commit_or_raise(db)
    db.refresh(item)
    return item


@gallery_categories_router.patch("/{category_id}", response_model=GalleryCategoryRead)
def update_gallery_category(
    category_id: UUID,
    payload: GalleryCategoryUpdate,
    db: Session = Depends(get_db),
):
    item = db.get(GalleryCategory, category_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gallery category not found.")
    apply_partial_update(item, payload.model_dump(exclude_unset=True))
    commit_or_raise(db)
    db.refresh(item)
    return item


@gallery_categories_router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_gallery_category(category_id: UUID, db: Session = Depends(get_db)):
    item = db.get(GalleryCategory, category_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gallery category not found.")
    db.delete(item)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@gallery_items_router.get("", response_model=PaginatedResponse[GalleryItemRead])
def list_gallery_items(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = gallery_item_query_with_categories(db).order_by(
        GalleryItem.sort_order.nulls_last(), GalleryItem.place
    )
    return paginate(query, limit, offset, transform=gallery_item_to_read)


@gallery_items_router.get("/{item_id}", response_model=GalleryItemRead)
def get_gallery_item(item_id: UUID, db: Session = Depends(get_db)):
    item = gallery_item_query_with_categories(db).filter_by(id=item_id).one_or_none()
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gallery item not found.")
    return gallery_item_to_read(item)


@gallery_items_router.post("", response_model=GalleryItemRead, status_code=status.HTTP_201_CREATED)
def create_gallery_item(payload: GalleryItemCreate, db: Session = Depends(get_db)):
    data = payload.model_dump()
    category_ids = data.pop("category_ids")
    media_ids = data.pop("media_ids")
    item = GalleryItem(**data)
    db.add(item)
    db.flush()
    sync_gallery_item_categories(db, item, category_ids)
    sync_gallery_item_media(db, item, media_ids)
    commit_or_raise(db)
    item = gallery_item_query_with_categories(db).filter_by(id=item.id).one()
    return gallery_item_to_read(item)


@gallery_items_router.patch("/{item_id}", response_model=GalleryItemRead)
def update_gallery_item(
    item_id: UUID,
    payload: GalleryItemUpdate,
    db: Session = Depends(get_db),
):
    item = gallery_item_query_with_categories(db).filter_by(id=item_id).one_or_none()
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gallery item not found.")
    data = payload.model_dump(exclude_unset=True)
    category_ids = data.pop("category_ids", None)
    media_ids = data.pop("media_ids", None)
    apply_partial_update(item, data)
    if category_ids is not None:
        sync_gallery_item_categories(db, item, category_ids)
    if media_ids is not None:
        sync_gallery_item_media(db, item, media_ids)
    commit_or_raise(db)
    item = gallery_item_query_with_categories(db).filter_by(id=item.id).one()
    return gallery_item_to_read(item)


@gallery_items_router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_gallery_item(item_id: UUID, db: Session = Depends(get_db)):
    item = db.get(GalleryItem, item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gallery item not found.")
    db.delete(item)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
