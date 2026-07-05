from uuid import UUID

from pathlib import Path

from fastapi import APIRouter, Depends, File, Form, HTTPException, Request, Response, UploadFile, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.media import MediaAsset
from schemas.media import MediaAssetCreate, MediaAssetRead, MediaAssetUpdate
from schemas.pagination import PaginatedResponse
from services.media_upload import (
    ingest_remote_image_url,
    is_local_media_url,
    public_upload_url,
    save_uploaded_image,
)
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


@router.post("/upload", response_model=MediaAssetRead, status_code=status.HTTP_201_CREATED)
async def upload_media_asset(
    request: Request,
    file: UploadFile = File(...),
    alt_text: str | None = Form(default=None),
    db: Session = Depends(get_db),
):
    stored_name, mime_type, slug = save_uploaded_image(file)
    url = public_upload_url(str(request.base_url), stored_name)
    if slug and db.query(MediaAsset).filter(MediaAsset.slug == slug).first() is not None:
        slug = None
    item = MediaAsset(
        slug=slug,
        url=url,
        alt_text=alt_text or (Path(file.filename or "").stem if file.filename else None),
        mime_type=mime_type,
        source="upload",
        usage="upload",
    )
    db.add(item)
    commit_or_raise(db)
    db.refresh(item)
    return item


@router.post("", response_model=MediaAssetRead, status_code=status.HTTP_201_CREATED)
def create_media_asset(
    payload: MediaAssetCreate,
    request: Request,
    db: Session = Depends(get_db),
):
    data = payload.model_dump()
    url = (data.get("url") or "").strip()
    if url and not is_local_media_url(url):
        _, mime_type, local_url = ingest_remote_image_url(url, request_base_url=str(request.base_url))
        data["url"] = local_url
        data["mime_type"] = mime_type or data.get("mime_type")
        data["source"] = "upload"
    item = MediaAsset(**data)
    db.add(item)
    commit_or_raise(db)
    db.refresh(item)
    return item


@router.patch("/{media_id}", response_model=MediaAssetRead)
def update_media_asset(
    media_id: UUID,
    payload: MediaAssetUpdate,
    request: Request,
    db: Session = Depends(get_db),
):
    item = db.get(MediaAsset, media_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Media asset not found.")
    updates = payload.model_dump(exclude_unset=True)
    url = updates.get("url")
    if isinstance(url, str) and url.strip() and not is_local_media_url(url.strip()):
        _, mime_type, local_url = ingest_remote_image_url(url.strip(), request_base_url=str(request.base_url))
        updates["url"] = local_url
        updates["mime_type"] = mime_type or updates.get("mime_type")
        updates["source"] = "upload"
    apply_partial_update(item, updates)
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
