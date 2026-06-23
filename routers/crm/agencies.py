from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_agency_scope, require_crm_user
from dependencies.crm_tenancy import get_include_deleted
from dependencies.pagination import get_pagination
from models.crm.tenancy import Agency, User
from schemas.crm.agency import AgencyCreate, AgencyRead, AgencyUpdate
from schemas.pagination import PaginatedResponse
from services.crm_audit import audit_create, audit_delete, audit_update, changed_fields_from_payload
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


def _get_agency_or_404(db: Session, agency_id: UUID, *, include_deleted: bool = False) -> Agency:
    query = db.query(Agency).filter(Agency.id == agency_id)
    if not include_deleted:
        query = query.filter(Agency.is_deleted.is_(False))
    agency = query.one_or_none()
    if agency is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agency not found.")
    return agency


@router.get("", response_model=PaginatedResponse[AgencyRead])
def list_agencies(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
    include_deleted: bool = Depends(get_include_deleted),
):
    limit, offset = pagination
    query = db.query(Agency).filter(Agency.id == agency_id).order_by(Agency.name)
    if not include_deleted:
        query = query.filter(Agency.is_deleted.is_(False))
    return paginate(query, limit, offset, transform=AgencyRead.model_validate)


@router.get("/{requested_agency_id}", response_model=AgencyRead)
def get_agency(
    requested_agency_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
    include_deleted: bool = Depends(get_include_deleted),
):
    if requested_agency_id != agency_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agency not found.")
    return _get_agency_or_404(db, agency_id, include_deleted=include_deleted)


@router.post("", response_model=AgencyRead, status_code=status.HTTP_201_CREATED)
def create_agency(
    payload: AgencyCreate,
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    if current_user.agency_id is not None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Agency staff cannot create new agencies.",
        )
    agency = Agency(**payload.model_dump())
    db.add(agency)
    db.flush()
    audit_create(
        db,
        agency_id=agency.id,
        user_id=current_user.id,
        entity_type="Agency",
        entity_id=agency.id,
        details=f'Created agency "{agency.name}" ({agency.subdomain})',
    )
    commit_or_raise(db, unique_fields=("subdomain",))
    db.refresh(agency)
    return agency


@router.patch("/{requested_agency_id}", response_model=AgencyRead)
def update_agency(
    requested_agency_id: UUID,
    payload: AgencyUpdate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    if requested_agency_id != agency_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agency not found.")
    agency = _get_agency_or_404(db, agency_id)
    apply_partial_update(agency, payload.model_dump(exclude_unset=True))
    audit_update(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Agency",
        entity_id=agency.id,
        details=f'Updated agency "{agency.name}"',
        changed_fields=changed_fields_from_payload(payload),
    )
    commit_or_raise(db, unique_fields=("subdomain",))
    db.refresh(agency)
    return agency


@router.delete("/{requested_agency_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_agency(
    requested_agency_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    if requested_agency_id != agency_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agency not found.")
    agency = _get_agency_or_404(db, agency_id)
    audit_delete(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Agency",
        entity_id=agency.id,
        details=f'Soft-deleted agency "{agency.name}"',
    )
    agency.is_deleted = True
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
