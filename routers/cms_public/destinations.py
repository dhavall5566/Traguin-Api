from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.destinations import Destination
from schemas.destination import DestinationRead
from schemas.pagination import PaginatedResponse
from services.destinations import destination_query_with_categories, destination_to_read
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[DestinationRead])
def list_destinations(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = (
        destination_query_with_categories(db)
        .filter(Destination.is_published.is_(True))
        .order_by(Destination.name)
    )
    return paginate(query, limit, offset, transform=destination_to_read)


@router.get("/slug/{slug}", response_model=DestinationRead)
def get_destination_by_slug(slug: str, db: Session = Depends(get_db)):
    destination = (
        destination_query_with_categories(db)
        .filter_by(slug=slug, is_published=True)
        .one_or_none()
    )
    if destination is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Destination not found.")
    return destination_to_read(destination)
