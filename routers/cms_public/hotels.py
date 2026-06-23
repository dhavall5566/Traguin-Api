from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.hotels import Hotel
from schemas.hotels import HotelRead
from schemas.pagination import PaginatedResponse
from services.hotels import hotel_query_with_nested, hotel_to_read
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[HotelRead])
def list_hotels(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = (
        hotel_query_with_nested(db)
        .filter(Hotel.is_published.is_(True))
        .order_by(Hotel.name)
    )
    return paginate(query, limit, offset, transform=hotel_to_read)


@router.get("/slug/{slug}", response_model=HotelRead)
def get_hotel_by_slug(slug: str, db: Session = Depends(get_db)):
    hotel = (
        hotel_query_with_nested(db)
        .filter_by(slug=slug, is_published=True)
        .one_or_none()
    )
    if hotel is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hotel not found.")
    return hotel_to_read(hotel)
