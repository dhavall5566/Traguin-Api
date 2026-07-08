from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.admin_list_filters import AdminListFilters, apply_admin_list_filters, get_admin_list_filters
from dependencies.pagination import get_pagination
from models.destinations import Destination
from models.hotels import Hotel
from schemas.hotels import HotelCreate, HotelListRead, HotelRead, HotelUpdate
from schemas.pagination import PaginatedResponse
from services.hotels import (
    hotel_list_query,
    hotel_query_with_nested,
    hotel_to_list_read,
    hotel_to_read,
    sync_hotel_gallery,
    sync_hotel_nearby_attractions,
)
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[HotelListRead])
def list_hotels(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
    filters: AdminListFilters = Depends(get_admin_list_filters),
):
    limit, offset = pagination
    query = hotel_list_query(db)
    query = apply_admin_list_filters(
        query,
        Hotel,
        filters,
        search_fields=("name", "slug", "description"),
        destination_model=Destination,
    )
    query = query.order_by(Hotel.name)
    return paginate(query, limit, offset, transform=hotel_to_list_read)


@router.get("/{hotel_id}", response_model=HotelRead)
def get_hotel(hotel_id: UUID, db: Session = Depends(get_db)):
    hotel = hotel_query_with_nested(db).filter_by(id=hotel_id).one_or_none()
    if hotel is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hotel not found.")
    return hotel_to_read(hotel)


@router.post("", response_model=HotelRead, status_code=status.HTTP_201_CREATED)
def create_hotel(payload: HotelCreate, db: Session = Depends(get_db)):
    data = payload.model_dump()
    nearby_attractions = data.pop("nearby_attractions")
    gallery_media_ids = data.pop("gallery_media_ids")
    hotel = Hotel(**data)
    db.add(hotel)
    db.flush()
    sync_hotel_nearby_attractions(db, hotel, nearby_attractions)
    sync_hotel_gallery(db, hotel, gallery_media_ids)
    commit_or_raise(db)
    hotel = hotel_query_with_nested(db).filter_by(id=hotel.id).one()
    return hotel_to_read(hotel)


@router.patch("/{hotel_id}", response_model=HotelRead)
def update_hotel(
    hotel_id: UUID,
    payload: HotelUpdate,
    db: Session = Depends(get_db),
):
    hotel = hotel_query_with_nested(db).filter_by(id=hotel_id).one_or_none()
    if hotel is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hotel not found.")
    data = payload.model_dump(exclude_unset=True)
    nearby_attractions = data.pop("nearby_attractions", None)
    gallery_media_ids = data.pop("gallery_media_ids", None)
    apply_partial_update(hotel, data)
    if nearby_attractions is not None:
        sync_hotel_nearby_attractions(db, hotel, nearby_attractions)
    if gallery_media_ids is not None:
        sync_hotel_gallery(db, hotel, gallery_media_ids)
    commit_or_raise(db)
    hotel = hotel_query_with_nested(db).filter_by(id=hotel.id).one()
    return hotel_to_read(hotel)


@router.delete("/{hotel_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_hotel(hotel_id: UUID, db: Session = Depends(get_db)):
    hotel = db.get(Hotel, hotel_id)
    if hotel is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hotel not found.")
    db.delete(hotel)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
