"""Fan-out lead-eligible website form submissions into CRM leads."""

from __future__ import annotations

from decimal import Decimal, InvalidOperation
from typing import Any
from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from config import settings
from models.crm.leads import Lead, LeadActivity, LeadNote
from models.crm.tenancy import User
from models.submissions import FormSubmission
from services.crm_audit import audit_create
from services.lead_customers import link_or_create_customer_for_lead
from utils.member_codes import inquiry_code_from_submission, member_code_from_phone

LEAD_ELIGIBLE_FORM_TYPES = frozenset(
    {
        "travel_planner",
        "itinerary_inquiry",
        "hotel_booking",
        "contact_consultation",
        "travel_expert_consultation",
        "plan_my_journey",
    }
)

_PAYLOAD_LABELS: dict[str, str] = {
    "destination": "Destination",
    "start_date": "Start date",
    "end_date": "End date",
    "travelers": "Travelers",
    "budget": "Budget (INR)",
    "style": "Travel style",
    "notes": "Notes",
    "email": "Email",
    "phone": "Phone",
    "country_code": "Country code",
    "name": "Name",
    "message": "Message",
    "service": "Service",
    "dates": "Preferred dates",
    "itinerary_slug": "Itinerary slug",
    "itinerary_title": "Itinerary",
    "rooms": "Rooms",
    "adults": "Adults",
    "children": "Children",
    "child_ages": "Children ages",
    "traveling_with_pets": "Traveling with pets",
    "member_code": "Member code",
    "inquiry_code": "Inquiry code",
    "hotel_id": "Hotel ID",
    "hotel_name": "Hotel",
    "rating": "Rating",
    "review": "Review",
}


def split_name(full_name: str) -> tuple[str, str]:
    trimmed = full_name.strip()
    if not trimmed:
        return "Unknown", "Visitor"
    parts = trimmed.split(None, 1)
    if len(parts) == 1:
        return parts[0], "Visitor"
    return parts[0], parts[1]


def _resolve_intake_actor(db: Session) -> tuple[UUID, UUID]:
    agency_id = settings.traguin_default_agency_id
    if agency_id is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Website lead intake is not configured (TRAGUIN_DEFAULT_AGENCY_ID).",
        )

    if settings.traguin_system_user_id is not None:
        return agency_id, settings.traguin_system_user_id

    user = db.scalar(
        select(User)
        .where(User.agency_id == agency_id)
        .order_by(User.created_at.asc())
        .limit(1)
    )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="No CRM user found for website lead intake.",
        )
    return agency_id, user.id


def _lead_title(submission: FormSubmission) -> str:
    form_type = submission.form_type
    payload = submission.payload or {}

    if form_type == "travel_planner":
        destination = (payload.get("destination") or "").strip()
        return f"{destination} trip inquiry" if destination else "Travel planner inquiry"

    if form_type == "itinerary_inquiry":
        itinerary_title = (payload.get("itinerary_title") or "").strip()
        if itinerary_title:
            return f"{itinerary_title} inquiry"
        slug = (payload.get("itinerary_slug") or "").strip()
        return f"{slug} inquiry" if slug else "Itinerary inquiry"

    if form_type == "hotel_booking":
        hotel_name = (payload.get("hotel_name") or "").strip()
        return f"{hotel_name} booking request" if hotel_name else "Hotel booking request"

    if form_type == "plan_my_journey":
        itinerary_title = (payload.get("itinerary_title") or "").strip()
        if itinerary_title:
            return f"Plan My Journey · {itinerary_title}"
        destination = (payload.get("destination") or "").strip()
        return f"Plan My Journey · {destination}" if destination else "Plan My Journey inquiry"

    if form_type == "travel_expert_consultation":
        service = (payload.get("service") or "").strip()
        return f"{service} consultation" if service else "Travel expert consultation"

    if form_type == "contact_consultation":
        return "Contact consultation request"

    return f"Website {form_type.replace('_', ' ')}"


def _lead_value(submission: FormSubmission) -> Decimal:
    if submission.form_type not in {"travel_planner", "plan_my_journey"}:
        return Decimal("0.00")
    budget = (submission.payload or {}).get("budget")
    if budget is None:
        return Decimal("0.00")
    try:
        return Decimal(str(budget))
    except (InvalidOperation, ValueError):
        return Decimal("0.00")


def _format_payload_value(value: Any) -> str:
    if value is None:
        return "—"
    if isinstance(value, list):
        return ", ".join(str(item) for item in value) if value else "—"
    if isinstance(value, dict):
        return str(value)
    return str(value).strip() or "—"


def _apply_tracking_codes(submission: FormSubmission) -> tuple[str, str]:
    payload = dict(submission.payload or {})
    phone = submission.phone or payload.get("phone")
    member_code = member_code_from_phone(str(phone) if phone else None)
    inquiry_code = inquiry_code_from_submission(
        submission.id,
        has_itinerary=bool(submission.related_itinerary_id or payload.get("itinerary_slug")),
    )
    payload["member_code"] = member_code
    payload["inquiry_code"] = inquiry_code
    submission.payload = payload
    return member_code, inquiry_code


def _build_intake_note(submission: FormSubmission) -> str:
    lines = [
        f"Website form submission ({submission.form_type})",
        f"Form submission ID: {submission.id}",
        "",
    ]

    if submission.name:
        lines.append(f"Name: {submission.name}")
    if submission.email:
        lines.append(f"Email: {submission.email}")
    if submission.phone:
        lines.append(f"Phone: {submission.phone}")
    if submission.related_itinerary_id:
        lines.append(f"Related itinerary ID: {submission.related_itinerary_id}")
    if submission.related_hotel_id:
        lines.append(f"Related hotel ID: {submission.related_hotel_id}")
    if submission.related_destination_id:
        lines.append(f"Related destination ID: {submission.related_destination_id}")

    payload = submission.payload or {}
    if payload:
        lines.append("")
        lines.append("Submission details:")
        for key in sorted(payload.keys()):
            label = _PAYLOAD_LABELS.get(key, key.replace("_", " ").title())
            lines.append(f"  • {label}: {_format_payload_value(payload[key])}")

    return "\n".join(lines)


def _contact_fields(submission: FormSubmission) -> tuple[str, str, str | None, str | None]:
    payload = submission.payload or {}

    if submission.form_type == "plan_my_journey":
        name = (submission.name or payload.get("name") or "").strip()
        first_name, last_name = split_name(name) if name else ("Unknown", "Visitor")
        email = submission.email or payload.get("email")
        if email:
            email = str(email).strip().lower() or None
        phone = submission.phone or payload.get("phone")
        if phone:
            phone = str(phone).strip() or None
        return first_name, last_name, email, phone

    name = (submission.name or payload.get("name") or "").strip()
    first_name, last_name = split_name(name) if name else ("Unknown", "Visitor")

    email = submission.email or payload.get("email")
    if email:
        email = str(email).strip().lower() or None

    phone = submission.phone or payload.get("phone")
    if phone:
        phone = str(phone).strip() or None

    return first_name, last_name, email, phone


def _lead_message(submission: FormSubmission) -> str | None:
    payload = submission.payload or {}
    for key in ("message", "notes", "review"):
        raw = payload.get(key)
        if raw is None:
            continue
        text = str(raw).strip()
        if text:
            return text
    return None


def process_form_submission_intake(db: Session, submission: FormSubmission) -> Lead | None:
    """Create CRM lead artifacts for lead-eligible submissions. Returns Lead or None."""
    if submission.form_type not in LEAD_ELIGIBLE_FORM_TYPES:
        return None

    member_code, inquiry_code = _apply_tracking_codes(submission)
    agency_id, actor_user_id = _resolve_intake_actor(db)
    first_name, last_name, email, phone = _contact_fields(submission)

    lead = Lead(
        agency_id=agency_id,
        title=_lead_title(submission),
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        status="NEW",
        value=_lead_value(submission),
        source=f"Website · {submission.form_type}",
        message=_lead_message(submission),
    )
    db.add(lead)
    db.flush()

    customer, _created = link_or_create_customer_for_lead(
        db,
        agency_id=agency_id,
        lead_id=lead.id,
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
    )
    lead.customer_id = customer.id

    tracking_meta = {
        "type": "website_intake",
        "member_code": member_code,
        "inquiry_code": inquiry_code,
        "form_submission_id": str(submission.id),
        "form_type": submission.form_type,
    }
    if submission.related_itinerary_id:
        tracking_meta["cms_itinerary_id"] = str(submission.related_itinerary_id)
    payload = submission.payload or {}
    if payload.get("itinerary_slug"):
        tracking_meta["itinerary_slug"] = payload.get("itinerary_slug")
    if payload.get("itinerary_title"):
        tracking_meta["itinerary_title"] = payload.get("itinerary_title")

    existing_history = customer.travel_history
    if isinstance(existing_history, list):
        customer.travel_history = [*existing_history, tracking_meta]
    elif isinstance(existing_history, dict):
        customer.travel_history = {**existing_history, **tracking_meta}
    else:
        customer.travel_history = tracking_meta

    note_body = _build_intake_note(submission)
    db.add(
        LeadNote(
            lead_id=lead.id,
            content=note_body,
            created_by_id=actor_user_id,
        )
    )
    db.add(
        LeadActivity(
            lead_id=lead.id,
            type="NOTE",
            description=(
                f"Website intake from {submission.form_type} "
                f"(form_submission_id={submission.id}) · Customer Directory profile linked"
            ),
            created_by_id=actor_user_id,
        )
    )

    audit_create(
        db,
        agency_id=agency_id,
        user_id=actor_user_id,
        entity_type="Lead",
        entity_id=lead.id,
        details=f"Website intake from {submission.form_type} (form_submission_id={submission.id})",
    )

    return lead
