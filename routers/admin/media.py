from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.media import MediaAsset
from schemas.media import MediaAssetCreate, MediaAssetRead, MediaAssetUpdate
from schemas.pagination import PaginatedResponse
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[MediaAssetRead])
def list_media_assets(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(MediaAsset).order_by(MediaAsset.created_at.desc())
    return paginate(query, limit, offset, transform=MediaAssetRead.model_validate)


@router.get("/{media_id}", response_model=MediaAssetRead)
def get_media_asset(media_id: UUID, db: Session = Depends(get_db)):
    item = db.get(MediaAsset, media_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Media asset not found.")
    return item


@router.post("", response_model=MediaAssetRead, status_code=status.HTTP_201_CREATED)
def create_media_asset(payload: MediaAssetCreate, db: Session = Depends(get_db)):
    item = MediaAsset(**payload.model_dump())
    db.add(item)
    commit_or_raise(db)
    db.refresh(item)
    return item


@router.patch("/{media_id}", response_model=MediaAssetRead)
def update_media_asset(
    media_id: UUID,
    payload: MediaAssetUpdate,
    db: Session = Depends(get_db),
):
    item = db.get(MediaAsset, media_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Media asset not found.")
    apply_partial_update(item, payload.model_dump(exclude_unset=True))
    commit_or_raise(db)
    db.refresh(item)
    return item


@router.delete("/{media_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_media_asset(media_id: UUID, db: Session = Depends(get_db)):
    item = db.get(MediaAsset, media_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Media asset not found.")
    db.delete(item)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
