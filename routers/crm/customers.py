from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_agency_scope, require_crm_user
from dependencies.crm_tenancy import get_include_deleted
from dependencies.pagination import get_pagination
from models.crm.customers import Customer
from models.crm.tenancy import User
from schemas.crm.customer import CustomerCreate, CustomerRead, CustomerUpdate
from schemas.pagination import PaginatedResponse
from services.crm_audit import audit_create, audit_delete, audit_update, changed_fields_from_payload
from services.crm_scope import get_customer_for_agency
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
