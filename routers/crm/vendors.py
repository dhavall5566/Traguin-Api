from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_agency_scope, require_crm_user
from dependencies.pagination import get_pagination
from models.crm.finance import VendorPayout
from models.crm.tenancy import User
from models.crm.vendors import Vendor
from schemas.crm.vendor import VendorCreate, VendorListRead, VendorRead, VendorUpdate
from schemas.pagination import PaginatedResponse
from services.crm_audit import audit_create, audit_delete, audit_update, changed_fields_from_payload
from services.crm_scope import require_vendor_for_agency
from services.crm_vendors import (
    sync_vendor_packages,
    sync_vendor_services,
    vendor_query_with_nested,
    vendor_to_list_read,
    vendor_to_read,
)
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[VendorListRead])
def list_vendors(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(Vendor).filter(Vendor.agency_id == agency_id).order_by(Vendor.name)
    return paginate(query, limit, offset, transform=vendor_to_list_read)


@router.get("/{vendor_id}", response_model=VendorRead)
def get_vendor(
    vendor_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    vendor = vendor_query_with_nested(db).filter(Vendor.id == vendor_id, Vendor.agency_id == agency_id).one_or_none()
    if vendor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vendor not found.")
    return vendor_to_read(vendor)


@router.post("", response_model=VendorRead, status_code=status.HTTP_201_CREATED)
def create_vendor(
    payload: VendorCreate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    data = payload.model_dump(exclude={"services", "packages"})
    vendor = Vendor(**data, agency_id=agency_id)
    db.add(vendor)
    db.flush()
    sync_vendor_services(db, vendor, payload.services)
    sync_vendor_packages(db, vendor, payload.packages)
    audit_create(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Vendor",
        entity_id=vendor.id,
        details=f'Created vendor "{vendor.name}" ({vendor.type})',
    )
    commit_or_raise(db)
    vendor = vendor_query_with_nested(db).filter(Vendor.id == vendor.id).one()
    return vendor_to_read(vendor)


@router.patch("/{vendor_id}", response_model=VendorRead)
def update_vendor(
    vendor_id: UUID,
    payload: VendorUpdate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    vendor = vendor_query_with_nested(db).filter(Vendor.id == vendor_id, Vendor.agency_id == agency_id).one_or_none()
    if vendor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vendor not found.")
    data = payload.model_dump(exclude_unset=True, exclude={"services", "packages"})
    apply_partial_update(vendor, data)
    if payload.services is not None:
        sync_vendor_services(db, vendor, payload.services)
    if payload.packages is not None:
        sync_vendor_packages(db, vendor, payload.packages)
    changed = changed_fields_from_payload(payload, exclude={"services", "packages"})
    if payload.services is not None:
        changed.append("services")
    if payload.packages is not None:
        changed.append("packages")
    audit_update(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Vendor",
        entity_id=vendor.id,
        details=f'Updated vendor "{vendor.name}"',
        changed_fields=changed,
    )
    commit_or_raise(db)
    db.refresh(vendor)
    vendor = vendor_query_with_nested(db).filter(Vendor.id == vendor.id).one()
    return vendor_to_read(vendor)


@router.delete("/{vendor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vendor(
    vendor_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    vendor = require_vendor_for_agency(db, vendor_id, agency_id)
    has_payouts = db.query(VendorPayout).filter(VendorPayout.vendor_id == vendor_id).count() > 0
    if has_payouts:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Cannot delete vendor: related vendor payouts exist.",
        )
    audit_delete(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Vendor",
        entity_id=vendor.id,
        details=f'Deleted vendor "{vendor.name}"',
    )
    db.delete(vendor)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
