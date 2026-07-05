"""Auto-assign returning customers to their original handler when still active."""

from __future__ import annotations

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.crm.leads import Lead
from utils.lead_codes import normalize_phone_digits


def _normalize_email(email: str | None) -> str | None:
    if not email or not email.strip():
        return None
    return email.strip().lower()


def user_is_active_staff(db: Session, user_id: UUID, agency_id: UUID) -> bool:
    from models.crm.tenancy import User

    user = db.get(User, user_id)
    return (
        user is not None
        and user.agency_id == agency_id
        and not user.is_deleted
    )


def _lead_matches_customer(
    lead: Lead,
    *,
    customer_id: UUID | None,
    phone_key: str | None,
    email_key: str | None,
) -> bool:
    if customer_id is not None and lead.customer_id == customer_id:
        return True
    if phone_key and normalize_phone_digits(lead.phone) == phone_key:
        return True
    if email_key and _normalize_email(lead.email) == email_key:
        return True
    return False


def find_original_assignee_id(
    db: Session,
    *,
    agency_id: UUID,
    customer_id: UUID | None = None,
    phone: str | None = None,
    email: str | None = None,
) -> UUID | None:
    """
    Return the assignee from the earliest matching lead if that person is still
    an active agency user. If the first handler has left, returns None.
    """
    phone_key = normalize_phone_digits(phone)
    email_key = _normalize_email(email)

    if customer_id is None and not phone_key and not email_key:
        return None

    candidates = db.scalars(
        select(Lead)
        .where(
            Lead.agency_id == agency_id,
            Lead.is_deleted.is_(False),
        )
        .order_by(Lead.created_at.asc())
        .limit(500)
    ).all()

    for lead in candidates:
        if not _lead_matches_customer(
            lead,
            customer_id=customer_id,
            phone_key=phone_key,
            email_key=email_key,
        ):
            continue
        if not lead.assigned_to_id:
            continue
        if user_is_active_staff(db, lead.assigned_to_id, agency_id):
            return lead.assigned_to_id
        return None

    return None


def apply_returning_customer_assignee(
    db: Session,
    lead: Lead,
    *,
    agency_id: UUID,
    customer_id: UUID | None = None,
    requested_assignee_id: UUID | None = None,
    prefer_original_handler: bool = True,
) -> bool:
    """
    Assign the lead to the original handler when appropriate.

    Explicit requested_assignee_id always wins when that user is still active.
    When prefer_original_handler is True (returning customer), reassign to the
    first handler if they are still active. Otherwise only fill in when unassigned.
    """
    if requested_assignee_id is not None:
        if user_is_active_staff(db, requested_assignee_id, agency_id):
            changed = lead.assigned_to_id != requested_assignee_id
            lead.assigned_to_id = requested_assignee_id
            return changed
        return False

    if (
        not prefer_original_handler
        and lead.assigned_to_id
        and user_is_active_staff(db, lead.assigned_to_id, agency_id)
    ):
        return False

    if lead.assigned_to_id and not user_is_active_staff(db, lead.assigned_to_id, agency_id):
        lead.assigned_to_id = None

    original = find_original_assignee_id(
        db,
        agency_id=agency_id,
        customer_id=customer_id or lead.customer_id,
        phone=lead.phone,
        email=lead.email,
    )
    if original is None:
        return False

    changed = lead.assigned_to_id != original
    lead.assigned_to_id = original
    return changed
