from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_agency_scope, require_crm_user
from dependencies.pagination import get_pagination
from models.crm.itineraries import Itinerary
from models.crm.tenancy import User
from schemas.crm.itinerary import (
    ItineraryCreate,
    ItineraryFromCmsPackageCreate,
    ItineraryListRead,
    ItineraryRead,
    ItineraryUpdate,
)
from schemas.pagination import PaginatedResponse
from services.crm_audit import audit_create, audit_delete, audit_update, changed_fields_from_payload
from services.crm_itineraries import (
    get_itinerary_with_nested,
    itinerary_query_with_nested,
    itinerary_to_list_read,
    itinerary_to_read,
    sync_itinerary_days,
)
from services.crm_itinerary_from_cms_package import create_crm_itinerary_from_cms_package
from services.crm_scope import get_customer_for_agency, require_itinerary_for_agency
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


def _validate_customer(db: Session, customer_id: UUID | None, agency_id: UUID) -> None:
    if customer_id is None:
        return
    if get_customer_for_agency(db, customer_id, agency_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found.")


@router.get("", response_model=PaginatedResponse[ItineraryListRead])
def list_itineraries(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = (
        db.query(Itinerary)
        .filter(Itinerary.agency_id == agency_id)
        .order_by(Itinerary.created_at.desc())
    )
    return paginate(query, limit, offset, transform=itinerary_to_list_read)


@router.post("/from-cms-package", response_model=ItineraryRead, status_code=status.HTTP_201_CREATED)
def create_itinerary_from_cms_package(
    payload: ItineraryFromCmsPackageCreate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    _validate_customer(db, payload.customer_id, agency_id)
    itinerary = create_crm_itinerary_from_cms_package(
        db,
        agency_id=agency_id,
        cms_package_id=payload.cms_package_id,
        customer_id=payload.customer_id,
    )
    audit_create(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Itinerary",
        entity_id=itinerary.id,
        details=f'Created itinerary from CMS package "{itinerary.title}"',
    )
    commit_or_raise(db)
    itinerary = get_itinerary_with_nested(db, itinerary.id, agency_id)
    assert itinerary is not None
    return itinerary_to_read(itinerary)


@router.get("/{itinerary_id}", response_model=ItineraryRead)
def get_itinerary(
    itinerary_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    itinerary = get_itinerary_with_nested(db, itinerary_id, agency_id)
    if itinerary is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Itinerary not found.")
    return itinerary_to_read(itinerary)


@router.post("", response_model=ItineraryRead, status_code=status.HTTP_201_CREATED)
def create_itinerary(
    payload: ItineraryCreate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    _validate_customer(db, payload.customer_id, agency_id)
    data = payload.model_dump(exclude={"days"})
    itinerary = Itinerary(**data, agency_id=agency_id)
    db.add(itinerary)
    db.flush()
    sync_itinerary_days(db, itinerary, payload.days)
    audit_create(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Itinerary",
        entity_id=itinerary.id,
        details=f'Created itinerary "{itinerary.title}"',
    )
    commit_or_raise(db)
    itinerary = get_itinerary_with_nested(db, itinerary.id, agency_id)
    assert itinerary is not None
    return itinerary_to_read(itinerary)


@router.patch("/{itinerary_id}", response_model=ItineraryRead)
def update_itinerary(
    itinerary_id: UUID,
    payload: ItineraryUpdate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    itinerary = require_itinerary_for_agency(db, itinerary_id, agency_id)
    if payload.customer_id is not None:
        _validate_customer(db, payload.customer_id, agency_id)
    data = payload.model_dump(exclude_unset=True, exclude={"days"})
    apply_partial_update(itinerary, data)
    if payload.days is not None:
        sync_itinerary_days(db, itinerary, payload.days)
    changed = changed_fields_from_payload(payload, exclude={"days"})
    if payload.days is not None:
        changed.append("days")
    audit_update(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Itinerary",
        entity_id=itinerary.id,
        details=f'Updated itinerary "{itinerary.title}"',
        changed_fields=changed,
    )
    commit_or_raise(db)
    itinerary = get_itinerary_with_nested(db, itinerary.id, agency_id)
    assert itinerary is not None
    return itinerary_to_read(itinerary)


@router.delete("/{itinerary_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_itinerary(
    itinerary_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    itinerary = require_itinerary_for_agency(db, itinerary_id, agency_id)
    audit_delete(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Itinerary",
        entity_id=itinerary.id,
        details=f'Deleted itinerary "{itinerary.title}"',
    )
    db.delete(itinerary)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
