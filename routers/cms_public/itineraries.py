from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.destinations import Destination
from models.itineraries import Itinerary
from schemas.itineraries import ItineraryRead
from schemas.pagination import PaginatedResponse
from services.itineraries import itinerary_query_with_nested, itinerary_to_read
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[ItineraryRead])
def list_itineraries(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = (
        itinerary_query_with_nested(db)
        .filter(Itinerary.is_published.is_(True))
        .order_by(Itinerary.title)
    )
    return paginate(query, limit, offset, transform=itinerary_to_read)


@router.get("/slug/{slug}", response_model=ItineraryRead)
def get_itinerary_by_slug(slug: str, db: Session = Depends(get_db)):
    itinerary = (
        itinerary_query_with_nested(db)
        .filter_by(slug=slug, is_published=True)
        .one_or_none()
    )
    if itinerary is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Itinerary not found.")
    return itinerary_to_read(itinerary)


@router.get("/by-destination/{destination_id}", response_model=ItineraryRead)
def get_itinerary_by_destination_id(destination_id: UUID, db: Session = Depends(get_db)):
    itinerary = (
        itinerary_query_with_nested(db)
        .filter_by(destination_id=destination_id, is_published=True)
        .order_by(Itinerary.updated_at.desc())
        .first()
    )
    if itinerary is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Itinerary not found.")
    return itinerary_to_read(itinerary)


@router.get("/by-destination/slug/{destination_slug}", response_model=ItineraryRead)
def get_itinerary_by_destination_slug(
    destination_slug: str,
    db: Session = Depends(get_db),
):
    destination = (
        db.query(Destination)
        .filter_by(slug=destination_slug, is_published=True)
        .one_or_none()
    )
    if destination is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Itinerary not found.")

    itinerary = (
        itinerary_query_with_nested(db)
        .filter_by(destination_id=destination.id, is_published=True)
        .order_by(Itinerary.updated_at.desc())
        .first()
    )
    if itinerary is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Itinerary not found.")
    return itinerary_to_read(itinerary)


@router.get("/by-destination/slug/{destination_slug}/all", response_model=list[ItineraryRead])
def list_itineraries_by_destination_slug(destination_slug: str, db: Session = Depends(get_db)):
    destination = (
        db.query(Destination)
        .filter_by(slug=destination_slug, is_published=True)
        .one_or_none()
    )
    if destination is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Itinerary not found.")

    itineraries = (
        itinerary_query_with_nested(db)
        .filter_by(destination_id=destination.id, is_published=True)
        .order_by(Itinerary.featured_sort_order.asc().nullslast(), Itinerary.title.asc())
        .all()
    )
    return [itinerary_to_read(itinerary) for itinerary in itineraries]
