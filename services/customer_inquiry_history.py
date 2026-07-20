"""Customer inquiry history and flag remarks — Lead Flow Guide v4.2."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from models.crm.bookings import Booking
from models.crm.customer_flags import CustomerFlag
from models.crm.customers import Customer
from models.crm.leads import Lead, LeadActivity, LeadFollowup, LeadNote
from models.crm.tenancy import User
from models.itineraries import Itinerary
from services.lead_customers import find_customer_by_contact
from utils.lead_codes import normalize_phone_digits
from utils.lead_pipeline import ACTIVE_PIPELINE_STATUSES, pipeline_status_label, resolve_pipeline_stage

NOT_CONVERTED_STATUSES = frozenset({"DUMP_LEAD", "LOST"})
TERMINAL_SUCCESS_STATUSES = frozenset({"BOOKED", "PAID", "READY", "CLOSED"})
MAX_INTERACTIONS = 300

ACTIVITY_TYPE_LABELS: dict[str, str] = {
    "NOTE": "System note",
    "PHONE": "Phone call",
    "STAGE_CHANGE": "Stage change",
    "MEET": "Meeting",
    "ENTERED_PROPOSAL_SENT": "Proposal sent",
    "ASSIGNMENT_ESCALATION": "Assignment escalated",
    "NO_ANSWER_ALERT": "No answer alert",
}


def _normalize_email(email: str | None) -> str | None:
    if not email or not email.strip():
        return None
    return email.strip().lower()


def _load_user_names(db: Session, user_ids: set[UUID]) -> dict[UUID, str]:
    if not user_ids:
        return {}
    rows = db.scalars(select(User).where(User.id.in_(user_ids))).all()
    return {row.id: row.name for row in rows}


def _lead_summary(lead: Lead, *, assignee_names: dict[UUID, str] | None = None) -> dict:
    stage = resolve_pipeline_stage(lead.status)
    assignee_name = None
    if assignee_names and lead.assigned_to_id is not None:
        assignee_name = assignee_names.get(lead.assigned_to_id)
    message = (lead.message or "").strip() or None
    return {
        "id": lead.id,
        "lead_code": lead.lead_code,
        "title": lead.title,
        "status": stage,
        "status_label": pipeline_status_label(stage),
        "source": lead.source,
        "travel_destination": lead.travel_destination,
        "message": message,
        "value": lead.value,
        "priority": lead.priority,
        "assigned_to_name": assignee_name,
        "created_at": lead.created_at,
        "updated_at": lead.updated_at,
    }


def _interaction_lead_context(lead: Lead) -> dict:
    return {
        "lead_id": lead.id,
        "lead_code": lead.lead_code,
        "lead_title": lead.title,
    }


def _normalize_dt(value: datetime | None) -> datetime:
    if value is None:
        return datetime.min.replace(tzinfo=timezone.utc)
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


def _activity_title(activity_type: str) -> str:
    return ACTIVITY_TYPE_LABELS.get(activity_type, activity_type.replace("_", " ").title())


def _count_customer_interactions(
    db: Session,
    *,
    lead_ids: list[UUID],
    booking_count: int,
    flag_count: int,
) -> int:
    """Fast interaction total without loading note/activity/followup rows."""
    inquiry_count = len(lead_ids)
    if not lead_ids:
        return inquiry_count + booking_count + flag_count

    note_count = db.scalar(
        select(func.count())
        .select_from(LeadNote)
        .where(LeadNote.lead_id.in_(lead_ids))
    ) or 0
    activity_count = db.scalar(
        select(func.count())
        .select_from(LeadActivity)
        .where(LeadActivity.lead_id.in_(lead_ids))
    ) or 0
    followup_count = db.scalar(
        select(func.count())
        .select_from(LeadFollowup)
        .where(LeadFollowup.lead_id.in_(lead_ids))
    ) or 0
    return inquiry_count + note_count + activity_count + followup_count + booking_count + flag_count


def _build_customer_interactions(
    db: Session,
    *,
    all_leads: list[Lead],
    bookings: list[dict],
    flags: list[dict],
) -> list[dict]:
    interactions: list[dict] = []
    lead_by_id = {lead.id: lead for lead in all_leads}
    user_ids: set[UUID] = set()

    for lead in all_leads:
        stage = resolve_pipeline_stage(lead.status)
        interactions.append(
            {
                "id": f"inquiry:{lead.id}",
                "type": "inquiry",
                "at": lead.created_at,
                **_interaction_lead_context(lead),
                "author_name": None,
                "title": "Inquiry received",
                "content": (lead.message or "").strip() or None,
                "activity_type": None,
                "status_label": pipeline_status_label(stage),
            }
        )

    lead_ids = [lead.id for lead in all_leads]
    if lead_ids:
        notes = db.scalars(
            select(LeadNote)
            .where(LeadNote.lead_id.in_(lead_ids))
            .order_by(LeadNote.created_at.desc())
            .limit(150)
        ).all()
        for note in notes:
            user_ids.add(note.created_by_id)
            lead = lead_by_id.get(note.lead_id)
            if lead is None:
                continue
            interactions.append(
                {
                    "id": f"note:{note.id}",
                    "type": "note",
                    "at": note.created_at,
                    **_interaction_lead_context(lead),
                    "author_id": note.created_by_id,
                    "author_name": None,
                    "title": "Note",
                    "content": note.content,
                    "activity_type": None,
                    "status_label": None,
                }
            )

        activities = db.scalars(
            select(LeadActivity)
            .where(LeadActivity.lead_id.in_(lead_ids))
            .order_by(LeadActivity.created_at.desc())
            .limit(150)
        ).all()
        for activity in activities:
            user_ids.add(activity.created_by_id)
            lead = lead_by_id.get(activity.lead_id)
            if lead is None:
                continue
            interactions.append(
                {
                    "id": f"activity:{activity.id}",
                    "type": "activity",
                    "at": activity.created_at,
                    **_interaction_lead_context(lead),
                    "author_id": activity.created_by_id,
                    "author_name": None,
                    "title": _activity_title(activity.type),
                    "content": activity.description,
                    "activity_type": activity.type,
                    "status_label": None,
                }
            )

        followups = db.scalars(
            select(LeadFollowup)
            .where(LeadFollowup.lead_id.in_(lead_ids))
            .order_by(LeadFollowup.created_at.desc())
            .limit(200)
        ).all()
        for followup in followups:
            user_ids.add(followup.created_by_id)
            lead = lead_by_id.get(followup.lead_id)
            if lead is None:
                continue
            interactions.append(
                {
                    "id": f"followup:{followup.id}",
                    "type": "followup",
                    "at": followup.scheduled_at,
                    **_interaction_lead_context(lead),
                    "author_id": followup.created_by_id,
                    "author_name": None,
                    "title": "Follow-up scheduled",
                    "content": (followup.notes or "").strip() or None,
                    "activity_type": followup.status,
                    "status_label": followup.status,
                }
            )

    for flag in flags:
        if flag.get("created_by_id"):
            user_ids.add(flag["created_by_id"])

    user_names = _load_user_names(db, user_ids)
    for row in interactions:
        author_id = row.pop("author_id", None)
        if author_id is not None:
            row["author_name"] = user_names.get(author_id)

    for booking in bookings:
        interactions.append(
            {
                "id": f"booking:{booking['id']}",
                "type": "booking",
                "at": booking["created_at"],
                "lead_id": None,
                "lead_code": None,
                "lead_title": booking.get("itinerary_title"),
                "author_name": None,
                "title": "Booking created",
                "content": booking.get("itinerary_title"),
                "activity_type": None,
                "status_label": booking.get("status"),
            }
        )

    for flag in flags:
        interactions.append(
            {
                "id": f"flag:{flag['id']}",
                "type": "flag",
                "at": flag["created_at"],
                "lead_id": None,
                "lead_code": None,
                "lead_title": None,
                "author_name": flag.get("created_by_name"),
                "title": "Customer flag",
                "content": flag["remark"],
                "activity_type": None,
                "status_label": None,
            }
        )

    for row in interactions:
        row["at"] = _normalize_dt(row["at"])
    interactions.sort(key=lambda row: row["at"], reverse=True)
    return interactions[:MAX_INTERACTIONS]


def _lead_matches_contact(
    lead: Lead,
    *,
    phone_key: str | None,
    email_key: str | None,
    customer_id: UUID | None,
) -> bool:
    if customer_id is not None and lead.customer_id == customer_id:
        return True
    if phone_key and normalize_phone_digits(lead.phone) == phone_key:
        return True
    if email_key and _normalize_email(lead.email) == email_key:
        return True
    return False


def gather_contact_leads(
    db: Session,
    *,
    agency_id: UUID,
    phone: str | None = None,
    email: str | None = None,
    customer_id: UUID | None = None,
) -> list[Lead]:
    phone_key = normalize_phone_digits(phone)
    email_key = _normalize_email(email)
    if customer_id is None and not phone_key and not email_key:
        return []

    filters = [Lead.agency_id == agency_id, Lead.is_deleted.is_(False)]
    contact_filters = []
    if customer_id is not None:
        contact_filters.append(Lead.customer_id == customer_id)
    if email_key:
        contact_filters.append(Lead.email.ilike(email_key))
    if phone_key:
        # Narrow candidates; exact digit match applied in Python below.
        contact_filters.append(Lead.phone.is_not(None))

    if not contact_filters:
        return []

    query = (
        select(Lead)
        .where(*filters, or_(*contact_filters))
        .order_by(Lead.created_at.asc())
        .limit(500)
    )
    candidates = db.scalars(query).all()

    matched: list[Lead] = []
    seen: set[UUID] = set()
    for lead in candidates:
        if lead.id in seen:
            continue
        if not _lead_matches_contact(
            lead,
            phone_key=phone_key,
            email_key=email_key,
            customer_id=customer_id,
        ):
            continue
        seen.add(lead.id)
        matched.append(lead)
    return matched


def _gather_leads_by_customer_id(
    db: Session,
    *,
    agency_id: UUID,
    customer_id: UUID,
) -> list[Lead]:
    return list(
        db.scalars(
            select(Lead)
            .where(
                Lead.agency_id == agency_id,
                Lead.is_deleted.is_(False),
                Lead.customer_id == customer_id,
            )
            .order_by(Lead.created_at.asc())
        ).all()
    )


def _count_leads_by_customer_id(
    db: Session,
    *,
    agency_id: UUID,
    customer_id: UUID,
) -> int:
    return int(
        db.scalar(
            select(func.count())
            .select_from(Lead)
            .where(
                Lead.agency_id == agency_id,
                Lead.is_deleted.is_(False),
                Lead.customer_id == customer_id,
            )
        )
        or 0
    )


def _lead_ids_by_customer_id(
    db: Session,
    *,
    agency_id: UUID,
    customer_id: UUID,
) -> list[UUID]:
    return list(
        db.scalars(
            select(Lead.id).where(
                Lead.agency_id == agency_id,
                Lead.is_deleted.is_(False),
                Lead.customer_id == customer_id,
            )
        ).all()
    )


def _count_bookings_by_customer_id(
    db: Session,
    *,
    agency_id: UUID,
    customer_id: UUID,
) -> int:
    return int(
        db.scalar(
            select(func.count())
            .select_from(Booking)
            .where(
                Booking.agency_id == agency_id,
                Booking.customer_id == customer_id,
            )
        )
        or 0
    )


def _count_flags_by_customer_id(db: Session, customer_id: UUID) -> int:
    return int(
        db.scalar(
            select(func.count())
            .select_from(CustomerFlag)
            .where(CustomerFlag.customer_id == customer_id)
        )
        or 0
    )


def _inquiry_number_for_lead(
    db: Session,
    *,
    agency_id: UUID,
    customer_id: UUID,
    current_lead_id: UUID,
) -> int | None:
    current = db.get(Lead, current_lead_id)
    if current is None:
        return None
    number = db.scalar(
        select(func.count())
        .select_from(Lead)
        .where(
            Lead.agency_id == agency_id,
            Lead.is_deleted.is_(False),
            Lead.customer_id == customer_id,
            Lead.created_at <= current.created_at,
        )
    )
    return int(number or 1)


def _is_active_lead(lead: Lead) -> bool:
    return resolve_pipeline_stage(lead.status) in ACTIVE_PIPELINE_STATUSES


def _is_not_converted(lead: Lead) -> bool:
    stage = resolve_pipeline_stage(lead.status)
    if stage in NOT_CONVERTED_STATUSES:
        return True
    if stage in TERMINAL_SUCCESS_STATUSES:
        return False
    return False


def list_customer_flags(db: Session, customer_id: UUID) -> list[CustomerFlag]:
    return list(
        db.scalars(
            select(CustomerFlag)
            .where(CustomerFlag.customer_id == customer_id)
            .order_by(CustomerFlag.created_at.desc())
        ).all()
    )


def serialize_customer_flag(db: Session, flag: CustomerFlag) -> dict:
    author = db.get(User, flag.created_by_id)
    return {
        "id": flag.id,
        "customer_id": flag.customer_id,
        "remark": flag.remark,
        "created_by_id": flag.created_by_id,
        "created_by_name": author.name if author else None,
        "created_at": flag.created_at,
    }


@dataclass(frozen=True)
class CustomerInquiryHistory:
    customer_id: UUID | None
    customer_code: str | None
    inquiry_number: int | None
    total_inquiry_count: int
    last_two_active_enquiries: list[dict]
    past_not_converted: list[dict]
    all_leads: list[dict]
    bookings: list[dict]
    flags: list[dict]
    interactions: list[dict]
    interaction_count: int
    booking_count: int = 0
    flag_count: int = 0


def build_customer_inquiry_history(
    db: Session,
    *,
    agency_id: UUID,
    phone: str | None = None,
    email: str | None = None,
    customer_id: UUID | None = None,
    current_lead_id: UUID | None = None,
    include_interactions: bool = True,
    include_details: bool = True,
) -> CustomerInquiryHistory:
    customer: Customer | None = None
    if customer_id is not None:
        customer = db.get(Customer, customer_id)
    if customer is None:
        customer = find_customer_by_contact(
            db,
            agency_id=agency_id,
            email=email,
            phone=phone,
        )

    resolved_customer_id = customer.id if customer is not None else customer_id

    if not include_details and resolved_customer_id is not None:
        total = _count_leads_by_customer_id(
            db,
            agency_id=agency_id,
            customer_id=resolved_customer_id,
        )
        inquiry_number: int | None = None
        if include_details:
            if current_lead_id is not None:
                inquiry_number = _inquiry_number_for_lead(
                    db,
                    agency_id=agency_id,
                    customer_id=resolved_customer_id,
                    current_lead_id=current_lead_id,
                )
            elif total > 0:
                inquiry_number = total

        booking_count = _count_bookings_by_customer_id(
            db,
            agency_id=agency_id,
            customer_id=resolved_customer_id,
        )
        flag_count = _count_flags_by_customer_id(db, resolved_customer_id)
        if include_interactions:
            lead_ids = _lead_ids_by_customer_id(
                db,
                agency_id=agency_id,
                customer_id=resolved_customer_id,
            )
            interaction_count = _count_customer_interactions(
                db,
                lead_ids=lead_ids,
                booking_count=booking_count,
                flag_count=flag_count,
            )
        else:
            interaction_count = 0
        return CustomerInquiryHistory(
            customer_id=resolved_customer_id,
            customer_code=customer.customer_code if customer is not None else None,
            inquiry_number=inquiry_number,
            total_inquiry_count=total,
            last_two_active_enquiries=[],
            past_not_converted=[],
            all_leads=[],
            bookings=[],
            flags=[],
            interactions=[],
            interaction_count=interaction_count,
            booking_count=booking_count,
            flag_count=flag_count,
        )

    if resolved_customer_id is not None:
        all_leads = _gather_leads_by_customer_id(
            db,
            agency_id=agency_id,
            customer_id=resolved_customer_id,
        )
    else:
        all_leads = gather_contact_leads(
            db,
            agency_id=agency_id,
            phone=phone,
            email=email,
            customer_id=resolved_customer_id,
        )

    total = len(all_leads)
    inquiry_number: int | None = None
    if current_lead_id is not None:
        for index, lead in enumerate(all_leads, start=1):
            if lead.id == current_lead_id:
                inquiry_number = index
                break
    elif total > 0:
        inquiry_number = total

    assignee_ids = {lead.assigned_to_id for lead in all_leads if lead.assigned_to_id is not None}
    assignee_names = _load_user_names(db, assignee_ids)

    active_sorted = sorted(
        [lead for lead in all_leads if _is_active_lead(lead)],
        key=lambda row: row.updated_at,
        reverse=True,
    )
    last_two_active = [_lead_summary(lead, assignee_names=assignee_names) for lead in active_sorted[:2]]

    not_converted_sorted = sorted(
        [lead for lead in all_leads if _is_not_converted(lead)],
        key=lambda row: row.updated_at,
        reverse=True,
    )
    past_not_converted = [_lead_summary(lead, assignee_names=assignee_names) for lead in not_converted_sorted[:10]]

    all_summaries = [_lead_summary(lead, assignee_names=assignee_names) for lead in reversed(all_leads)]

    bookings: list[dict] = []
    if resolved_customer_id is not None:
        booking_rows = db.scalars(
            select(Booking)
            .where(
                Booking.agency_id == agency_id,
                Booking.customer_id == resolved_customer_id,
            )
            .order_by(Booking.created_at.desc())
            .limit(20)
        ).all()
        itinerary_ids = {row.itinerary_id for row in booking_rows if row.itinerary_id is not None}
        itinerary_titles: dict[UUID, str] = {}
        if itinerary_ids:
            itinerary_rows = db.scalars(
                select(Itinerary).where(Itinerary.id.in_(itinerary_ids))
            ).all()
            itinerary_titles = {row.id: row.title for row in itinerary_rows}
        bookings = [
            {
                "id": row.id,
                "status": row.status,
                "created_at": row.created_at,
                "itinerary_title": itinerary_titles.get(row.itinerary_id) if row.itinerary_id else None,
            }
            for row in booking_rows
        ]

    flags: list[dict] = []
    if resolved_customer_id is not None:
        flags = [serialize_customer_flag(db, flag) for flag in list_customer_flags(db, resolved_customer_id)]

    lead_ids = [lead.id for lead in all_leads]
    interaction_count = _count_customer_interactions(
        db,
        lead_ids=lead_ids,
        booking_count=len(bookings),
        flag_count=len(flags),
    )
    if include_interactions:
        interactions = _build_customer_interactions(
            db,
            all_leads=all_leads,
            bookings=bookings,
            flags=flags,
        )
    else:
        interactions = []

    return CustomerInquiryHistory(
        customer_id=resolved_customer_id,
        customer_code=customer.customer_code if customer is not None else None,
        inquiry_number=inquiry_number,
        total_inquiry_count=total,
        last_two_active_enquiries=last_two_active,
        past_not_converted=past_not_converted,
        all_leads=all_summaries,
        bookings=bookings,
        flags=flags,
        interactions=interactions,
        interaction_count=interaction_count,
        booking_count=len(bookings),
        flag_count=len(flags),
    )


def format_inquiry_history_alert_lines(history: CustomerInquiryHistory) -> list[str]:
    lines: list[str] = []
    if history.total_inquiry_count > 0:
        number = history.inquiry_number or history.total_inquiry_count
        lines.append(f"Enquiry #{number} of {history.total_inquiry_count} from this mobile")
    if history.last_two_active_enquiries:
        lines.append("Last active enquiries:")
        for entry in history.last_two_active_enquiries[:2]:
            code = entry.get("lead_code") or str(entry["id"])[:8]
            lines.append(
                f"  · {code} — {entry['title']} ({entry['status_label']})"
            )
    if history.past_not_converted:
        lines.append(f"Past not converted: {len(history.past_not_converted)}")
    if history.flags:
        remarks = "; ".join(flag["remark"] for flag in history.flags[:5])
        lines.append(f"Flags: {remarks}")
    return lines


def format_inquiry_history_alert_extra(history: CustomerInquiryHistory) -> str:
    lines = format_inquiry_history_alert_lines(history)
    return " · ".join(line.replace("  · ", "") for line in lines) if lines else ""
