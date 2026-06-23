from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_agency_scope, require_crm_user
from dependencies.pagination import get_pagination
from models.crm.bookings import Booking
from models.crm.tenancy import User
from schemas.crm.booking import BookingCreate, BookingRead, BookingUpdate
from schemas.pagination import PaginatedResponse
from services.crm_audit import audit_create, audit_delete, audit_update, changed_fields_from_payload
from services.crm_scope import (
    get_booking_for_agency,
    get_customer_for_agency,
    get_itinerary_for_agency,
)
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


def _validate_booking_refs(
    db: Session,
    *,
    agency_id: UUID,
    customer_id: UUID | None = None,
    itinerary_id: UUID | None = None,
) -> None:
    if customer_id is not None and get_customer_for_agency(db, customer_id, agency_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found.")
    if itinerary_id is not None and get_itinerary_for_agency(db, itinerary_id, agency_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Itinerary not found.")


@router.get("", response_model=PaginatedResponse[BookingRead])
def list_bookings(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(Booking).filter(Booking.agency_id == agency_id).order_by(Booking.created_at.desc())
    return paginate(query, limit, offset, transform=BookingRead.model_validate)


@router.get("/{booking_id}", response_model=BookingRead)
def get_booking(
    booking_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    booking = get_booking_for_agency(db, booking_id, agency_id)
    if booking is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found.")
    return booking


@router.post("", response_model=BookingRead, status_code=status.HTTP_201_CREATED)
def create_booking(
    payload: BookingCreate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    _validate_booking_refs(db, agency_id=agency_id, customer_id=payload.customer_id, itinerary_id=payload.itinerary_id)
    booking = Booking(**payload.model_dump(), agency_id=agency_id)
    db.add(booking)
    db.flush()
    audit_create(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Booking",
        entity_id=booking.id,
        details=f"Created booking {booking.id} (status {booking.status})",
    )
    commit_or_raise(db)
    db.refresh(booking)
    return booking


@router.patch("/{booking_id}", response_model=BookingRead)
def update_booking(
    booking_id: UUID,
    payload: BookingUpdate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    booking = get_booking_for_agency(db, booking_id, agency_id)
    if booking is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found.")
    _validate_booking_refs(
        db,
        agency_id=agency_id,
        customer_id=payload.customer_id,
        itinerary_id=payload.itinerary_id,
    )
    apply_partial_update(booking, payload.model_dump(exclude_unset=True))
    audit_update(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Booking",
        entity_id=booking.id,
        details=f"Updated booking {booking.id}",
        changed_fields=changed_fields_from_payload(payload),
    )
    commit_or_raise(db)
    db.refresh(booking)
    return booking


@router.delete("/{booking_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_booking(
    booking_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    booking = get_booking_for_agency(db, booking_id, agency_id)
    if booking is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found.")
    audit_delete(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Booking",
        entity_id=booking.id,
        details=f"Deleted booking {booking.id}",
    )
    db.delete(booking)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
