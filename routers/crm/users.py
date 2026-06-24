from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_agency_scope, require_crm_user
from dependencies.crm_tenancy import get_include_deleted
from dependencies.pagination import get_pagination
from models.crm.tenancy import User
from schemas.crm.user import UserCreate, UserRead, UserUpdate
from schemas.pagination import PaginatedResponse
from services.crm_audit import audit_create, audit_delete, audit_update, changed_fields_from_payload
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate
from utils.passwords import hash_password

router = APIRouter()


def _user_query(db: Session, agency_id: UUID, *, include_deleted: bool):
    query = db.query(User).filter(User.agency_id == agency_id).order_by(User.name)
    if not include_deleted:
        query = query.filter(User.is_deleted.is_(False))
    return query


def _get_user_for_agency(
    db: Session,
    user_id: UUID,
    agency_id: UUID,
    *,
    include_deleted: bool = False,
) -> User | None:
    query = db.query(User).filter(User.id == user_id, User.agency_id == agency_id)
    if not include_deleted:
        query = query.filter(User.is_deleted.is_(False))
    return query.one_or_none()


@router.get("", response_model=PaginatedResponse[UserRead])
def list_users(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
    include_deleted: bool = Depends(get_include_deleted),
):
    limit, offset = pagination
    query = _user_query(db, agency_id, include_deleted=include_deleted)
    return paginate(query, limit, offset, transform=UserRead.model_validate)


@router.get("/{user_id}", response_model=UserRead)
def get_user(
    user_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
    include_deleted: bool = Depends(get_include_deleted),
):
    user = _get_user_for_agency(db, user_id, agency_id, include_deleted=include_deleted)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    return user


@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(
    payload: UserCreate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    target_agency_id = payload.agency_id or agency_id
    if target_agency_id != agency_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot create users outside your agency.",
        )

    data = payload.model_dump(exclude={"password", "agency_id", "email"})
    user = User(
        **data,
        email=str(payload.email).strip().lower(),
        agency_id=target_agency_id,
        password_hash=hash_password(payload.password),
    )
    db.add(user)
    db.flush()
    audit_create(
        db,
        agency_id=target_agency_id,
        user_id=current_user.id,
        entity_type="User",
        entity_id=user.id,
        details=f'Created user "{user.name}" ({user.email})',
    )
    commit_or_raise(db, unique_fields=("email",))
    db.refresh(user)
    return user


@router.patch("/{user_id}", response_model=UserRead)
def update_user(
    user_id: UUID,
    payload: UserUpdate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    user = _get_user_for_agency(db, user_id, agency_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")

    data = payload.model_dump(exclude_unset=True, exclude={"password"})
    if payload.email is not None:
        data["email"] = payload.email.lower()
    if payload.agency_id is not None and payload.agency_id != agency_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot move users outside your agency.",
        )
    apply_partial_update(user, data)
    if payload.password is not None:
        user.password_hash = hash_password(payload.password)

    changed = changed_fields_from_payload(payload, exclude={"password"})
    if payload.password is not None:
        changed.append("password")
    audit_update(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="User",
        entity_id=user.id,
        details=f'Updated user "{user.name}" ({user.email})',
        changed_fields=changed,
    )
    commit_or_raise(db, unique_fields=("email",))
    db.refresh(user)
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    user = _get_user_for_agency(db, user_id, agency_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    audit_delete(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="User",
        entity_id=user.id,
        details=f'Soft-deleted user "{user.name}" ({user.email})',
    )
    user.is_deleted = True
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
