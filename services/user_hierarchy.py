"""Reporting manager validation for CRM users."""

from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.crm.org_units import OrgUnit
from models.crm.tenancy import User


def _get_active_user(db: Session, user_id: UUID, agency_id: UUID) -> User | None:
    return (
        db.query(User)
        .filter(
            User.id == user_id,
            User.agency_id == agency_id,
            User.is_deleted.is_(False),
        )
        .one_or_none()
    )


def validate_org_unit_for_agency(db: Session, agency_id: UUID, org_unit_id: UUID | None) -> None:
    if org_unit_id is None:
        return
    unit = (
        db.query(OrgUnit)
        .filter(
            OrgUnit.id == org_unit_id,
            OrgUnit.agency_id == agency_id,
            OrgUnit.is_deleted.is_(False),
        )
        .one_or_none()
    )
    if unit is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Org unit not found in this agency.",
        )


def validate_manager_for_user(
    db: Session,
    *,
    agency_id: UUID,
    user_id: UUID | None,
    manager_id: UUID | None,
) -> None:
    if manager_id is None:
        return
    if user_id is not None and manager_id == user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user cannot be their own reporting manager.",
        )

    manager = _get_active_user(db, manager_id, agency_id)
    if manager is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Reporting manager not found in this agency.",
        )

    if user_id is None:
        return

    seen: set[UUID] = {user_id}
    current: User | None = manager
    while current is not None:
        if current.id in seen:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Circular reporting hierarchy is not allowed.",
            )
        seen.add(current.id)
        if current.manager_id is None:
            break
        current = _get_active_user(db, current.manager_id, agency_id)
