from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.itineraries import Itinerary
from schemas.itineraries import ItineraryCreate, ItineraryListRead, ItineraryRead, ItineraryUpdate
from schemas.pagination import PaginatedResponse
from services.itineraries import (
    itinerary_list_query,
    itinerary_query_with_nested,
    itinerary_to_list_read,
    itinerary_to_read,
    sync_itinerary_days,
    sync_itinerary_gallery,
    sync_itinerary_highlights,
    sync_itinerary_hotels,
    sync_itinerary_inclusions,
)
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[ItineraryListRead])
def list_itineraries(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = itinerary_list_query(db).order_by(Itinerary.title)
    return paginate(query, limit, offset, transform=itinerary_to_list_read)


@router.get("/{itinerary_id}", response_model=ItineraryRead)
def get_itinerary(itinerary_id: UUID, db: Session = Depends(get_db)):
    itinerary = itinerary_query_with_nested(db).filter_by(id=itinerary_id).one_or_none()
    if itinerary is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Itinerary not found.")
    return itinerary_to_read(itinerary)


@router.post("", response_model=ItineraryRead, status_code=status.HTTP_201_CREATED)
def create_itinerary(payload: ItineraryCreate, db: Session = Depends(get_db)):
    data = payload.model_dump()
    highlights = data.pop("highlights")
    days = data.pop("days")
    hotels = data.pop("hotels")
    inclusions = data.pop("inclusions")
    gallery_media_ids = data.pop("gallery_media_ids")
    itinerary = Itinerary(**data)
    db.add(itinerary)
    db.flush()
    sync_itinerary_highlights(db, itinerary, highlights)
    sync_itinerary_days(db, itinerary, days)
    sync_itinerary_hotels(db, itinerary, hotels)
    sync_itinerary_inclusions(db, itinerary, inclusions)
    sync_itinerary_gallery(db, itinerary, gallery_media_ids)
    commit_or_raise(db)
    itinerary = itinerary_query_with_nested(db).filter_by(id=itinerary.id).one()
    return itinerary_to_read(itinerary)


@router.patch("/{itinerary_id}", response_model=ItineraryRead)
def update_itinerary(
    itinerary_id: UUID,
    payload: ItineraryUpdate,
    db: Session = Depends(get_db),
):
    itinerary = itinerary_query_with_nested(db).filter_by(id=itinerary_id).one_or_none()
    if itinerary is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Itinerary not found.")
    data = payload.model_dump(exclude_unset=True)
    highlights = data.pop("highlights", None)
    days = data.pop("days", None)
    hotels = data.pop("hotels", None)
    inclusions = data.pop("inclusions", None)
    gallery_media_ids = data.pop("gallery_media_ids", None)
    apply_partial_update(itinerary, data)
    if highlights is not None:
        sync_itinerary_highlights(db, itinerary, highlights)
    if days is not None:
        sync_itinerary_days(db, itinerary, days)
    if hotels is not None:
        sync_itinerary_hotels(db, itinerary, hotels)
    if inclusions is not None:
        sync_itinerary_inclusions(db, itinerary, inclusions)
    if gallery_media_ids is not None:
        sync_itinerary_gallery(db, itinerary, gallery_media_ids)
    commit_or_raise(db)
    itinerary = itinerary_query_with_nested(db).filter_by(id=itinerary.id).one()
    return itinerary_to_read(itinerary)


@router.delete("/{itinerary_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_itinerary(itinerary_id: UUID, db: Session = Depends(get_db)):
    itinerary = db.get(Itinerary, itinerary_id)
    if itinerary is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Itinerary not found.")
    db.delete(itinerary)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
