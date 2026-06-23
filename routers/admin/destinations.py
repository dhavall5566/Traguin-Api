from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.destinations import Destination
from schemas.destination import DestinationCreate, DestinationRead, DestinationUpdate
from schemas.pagination import PaginatedResponse
from services.destinations import (
    destination_query_with_categories,
    destination_to_read,
    sync_destination_categories,
    sync_destination_gallery,
)
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[DestinationRead])
def list_destinations(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = destination_query_with_categories(db).order_by(Destination.name)
    return paginate(query, limit, offset, transform=destination_to_read)


@router.get("/{destination_id}", response_model=DestinationRead)
def get_destination(destination_id: UUID, db: Session = Depends(get_db)):
    destination = destination_query_with_categories(db).filter_by(id=destination_id).one_or_none()
    if destination is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Destination not found.")
    return destination_to_read(destination)


@router.post("", response_model=DestinationRead, status_code=status.HTTP_201_CREATED)
def create_destination(payload: DestinationCreate, db: Session = Depends(get_db)):
    data = payload.model_dump()
    category_ids = data.pop("category_ids")
    gallery_media_ids = data.pop("gallery_media_ids")
    destination = Destination(**data)
    db.add(destination)
    db.flush()
    sync_destination_categories(db, destination, category_ids)
    sync_destination_gallery(db, destination, gallery_media_ids)
    commit_or_raise(db)
    destination = destination_query_with_categories(db).filter_by(id=destination.id).one()
    return destination_to_read(destination)


@router.patch("/{destination_id}", response_model=DestinationRead)
def update_destination(
    destination_id: UUID,
    payload: DestinationUpdate,
    db: Session = Depends(get_db),
):
    destination = destination_query_with_categories(db).filter_by(id=destination_id).one_or_none()
    if destination is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Destination not found.")

    data = payload.model_dump(exclude_unset=True)
    category_ids = data.pop("category_ids", None)
    gallery_media_ids = data.pop("gallery_media_ids", None)
    apply_partial_update(destination, data)
    if category_ids is not None:
        sync_destination_categories(db, destination, category_ids)
    if gallery_media_ids is not None:
        sync_destination_gallery(db, destination, gallery_media_ids)
    commit_or_raise(db)
    destination = destination_query_with_categories(db).filter_by(id=destination.id).one()
    return destination_to_read(destination)


@router.delete("/{destination_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_destination(destination_id: UUID, db: Session = Depends(get_db)):
    destination = db.get(Destination, destination_id)
    if destination is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Destination not found.")
    db.delete(destination)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
