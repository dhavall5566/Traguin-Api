from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.media import MediaAsset
from schemas.media import MediaAssetRead
from schemas.pagination import PaginatedResponse
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
