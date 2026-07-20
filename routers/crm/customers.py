from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_agency_scope, require_crm_user
from dependencies.crm_tenancy import get_include_deleted
from dependencies.pagination import get_pagination
from models.crm.customer_flags import CustomerFlag
from models.crm.customers import Customer
from models.crm.tenancy import User
from schemas.crm.customer import CustomerCreate, CustomerRead, CustomerUpdate
from schemas.crm.customer_inquiry import (
    CustomerFlagCreate,
    CustomerFlagRead,
    CustomerInquiryHistoryRead,
)
from schemas.pagination import PaginatedResponse
from services.crm_audit import audit_create, audit_delete, audit_update, changed_fields_from_payload
from services.crm_scope import get_customer_for_agency
from services.customer_inquiry_history import (
    build_customer_inquiry_history,
    serialize_customer_flag,
)
from services.customers import customer_to_read
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

CUSTOMER_EMAIL_CONFLICT = "A customer with this email already exists in your agency."

router = APIRouter()


@router.get("", response_model=PaginatedResponse[CustomerRead])
def list_customers(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
    include_deleted: bool = Depends(get_include_deleted),
):
    limit, offset = pagination
    query = db.query(Customer).filter(Customer.agency_id == agency_id).order_by(Customer.last_name, Customer.first_name)
    if not include_deleted:
        query = query.filter(Customer.is_deleted.is_(False))
    return paginate(query, limit, offset, transform=customer_to_read)


@router.get("/{customer_id}", response_model=CustomerRead)
def get_customer(
    customer_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
    include_deleted: bool = Depends(get_include_deleted),
):
    customer = get_customer_for_agency(db, customer_id, agency_id, include_deleted=include_deleted)
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found.")
    return customer_to_read(customer)


@router.get("/{customer_id}/inquiry-history", response_model=CustomerInquiryHistoryRead)
def get_customer_inquiry_history(
    customer_id: UUID,
    include_interactions: bool = Query(default=True),
    include_details: bool = Query(default=True),
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    customer = get_customer_for_agency(db, customer_id, agency_id)
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found.")
    history = build_customer_inquiry_history(
        db,
        agency_id=agency_id,
        phone=customer.phone,
        email=customer.email,
        customer_id=customer.id,
        include_interactions=include_interactions,
        include_details=include_details,
    )
    return CustomerInquiryHistoryRead.model_validate(history.__dict__)


@router.get("/{customer_id}/flags", response_model=list[CustomerFlagRead])
def list_customer_flags(
    customer_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    customer = get_customer_for_agency(db, customer_id, agency_id)
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found.")
    from services.customer_inquiry_history import list_customer_flags as fetch_flags

    return [CustomerFlagRead.model_validate(serialize_customer_flag(db, flag)) for flag in fetch_flags(db, customer.id)]


@router.post("/{customer_id}/flags", response_model=CustomerFlagRead, status_code=status.HTTP_201_CREATED)
def create_customer_flag(
    customer_id: UUID,
    payload: CustomerFlagCreate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    customer = get_customer_for_agency(db, customer_id, agency_id)
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found.")
    remark = payload.remark.strip()
    flag = CustomerFlag(
        customer_id=customer.id,
        remark=remark,
        created_by_id=current_user.id,
    )
    db.add(flag)
    audit_create(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="CustomerFlag",
        entity_id=customer.id,
        details=f'Added customer flag on {customer.first_name} {customer.last_name}: "{remark}"',
    )
    commit_or_raise(db)
    db.refresh(flag)
    return CustomerFlagRead.model_validate(serialize_customer_flag(db, flag))


@router.delete("/{customer_id}/flags/{flag_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer_flag(
    customer_id: UUID,
    flag_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    customer = get_customer_for_agency(db, customer_id, agency_id)
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found.")
    flag = db.get(CustomerFlag, flag_id)
    if flag is None or flag.customer_id != customer.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Flag not found.")
    audit_delete(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="CustomerFlag",
        entity_id=customer.id,
        details=f'Removed customer flag on {customer.first_name} {customer.last_name}: "{flag.remark}"',
    )
    db.delete(flag)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("", response_model=CustomerRead, status_code=status.HTTP_201_CREATED)
def create_customer(
    payload: CustomerCreate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    data = payload.model_dump()
    data["email"] = str(payload.email).lower()
    customer = Customer(**data, agency_id=agency_id)
    db.add(customer)
    db.flush()
    audit_create(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Customer",
        entity_id=customer.id,
        details=f"Created customer {customer.first_name} {customer.last_name} ({customer.email})",
    )
    commit_or_raise(
        db,
        unique_fields=("email",),
        unique_field_messages={"email": CUSTOMER_EMAIL_CONFLICT},
    )
    db.refresh(customer)
    return customer_to_read(customer)


@router.patch("/{customer_id}", response_model=CustomerRead)
def update_customer(
    customer_id: UUID,
    payload: CustomerUpdate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    customer = get_customer_for_agency(db, customer_id, agency_id)
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found.")
    data = payload.model_dump(exclude_unset=True)
    if payload.email is not None:
        data["email"] = str(payload.email).lower()
    apply_partial_update(customer, data)
    audit_update(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Customer",
        entity_id=customer.id,
        details=f"Updated customer {customer.first_name} {customer.last_name} ({customer.email})",
        changed_fields=changed_fields_from_payload(payload),
    )
    commit_or_raise(
        db,
        unique_fields=("email",),
        unique_field_messages={"email": CUSTOMER_EMAIL_CONFLICT},
    )
    db.refresh(customer)
    return customer_to_read(customer)


@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(
    customer_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    customer = get_customer_for_agency(db, customer_id, agency_id)
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found.")
    audit_delete(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Customer",
        entity_id=customer.id,
        details=f"Soft-deleted customer {customer.first_name} {customer.last_name} ({customer.email})",
    )
    customer.is_deleted = True
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
