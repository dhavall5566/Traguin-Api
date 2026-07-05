"""Link leads to Customer Directory profiles on creation (agency-scoped)."""

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.crm.customers import Customer


def _normalize_email(email: str | None) -> str | None:
    if not email or not email.strip():
        return None
    return email.strip().lower()


from utils.lead_codes import normalize_phone_digits


def link_or_create_customer_for_lead(
    db: Session,
    *,
    agency_id: UUID,
    lead_id: UUID,
    first_name: str,
    last_name: str,
    email: str | None,
    phone: str | None,
) -> tuple[Customer, bool]:
    """
    Find an active customer by email within the agency, or create one.

    Returns (customer, created) where created is True when a new row was inserted.
    Reuses by email first, then by normalized phone (last 10 digits), or creates with
    a placeholder email when none is provided.
    """
    normalized = _normalize_email(email)

    if normalized:
        existing = db.scalar(
            select(Customer).where(
                Customer.agency_id == agency_id,
                Customer.email == normalized,
                Customer.is_deleted.is_(False),
            )
        )
        if existing is not None:
            return existing, False

    phone_key = normalize_phone_digits(phone)
    if phone_key:
        candidates = db.scalars(
            select(Customer).where(
                Customer.agency_id == agency_id,
                Customer.phone.isnot(None),
                Customer.is_deleted.is_(False),
            ).limit(200)
        ).all()
        for candidate in candidates:
            if normalize_phone_digits(candidate.phone) == phone_key:
                return candidate, False

    if not (last_name or "").strip():
        last_name = "Visitor"

    profile_email = normalized or f"noreply.profile.{lead_id}@crm.directory"
    customer = Customer(
        agency_id=agency_id,
        first_name=first_name,
        last_name=last_name,
        email=profile_email,
        phone=phone,
        travel_history=[],
        documents=[],
    )
    db.add(customer)
    db.flush()
    return customer, True
