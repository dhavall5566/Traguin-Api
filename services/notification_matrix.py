"""Lead Flow Guide v4.2 — role-based notification routing."""

from __future__ import annotations

import logging
import time
from typing import Literal
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from config import settings
from models.crm.finance import Invoice
from models.crm.leads import Lead, LeadActivity
from models.crm.tenancy import Agency, User
from services.crm_escalation_targets import (
    dedupe_users,
    resolve_account_users,
    resolve_admin_users,
    resolve_ops_head_users,
    resolve_rm_user,
)
from services.customer_inquiry_history import (
    build_customer_inquiry_history,
    format_inquiry_history_alert_extra,
    format_inquiry_history_alert_lines,
)
from services.notification_templates.context import build_invoice_context, build_lead_context
from services.notification_templates.delivery import (
    matrix_customer_template,
    matrix_customer_whatsapp_template,
    matrix_staff_template,
    send_customer_lead_email,
    send_templated_email,
    send_templated_whatsapp,
    whatsapp_fields_for_template,
)
from services.notification_templates.renderer import render_email, render_plain, render_whatsapp
from services.whatsapp_notifications import (
    CrmAlertPayload,
    build_alert_fields,
    send_whatsapp_template,
)
from utils.lead_pipeline import pipeline_status_label, resolve_pipeline_stage

logger = logging.getLogger(__name__)

MatrixEvent = Literal[
    "new_lead",
    "assigned_to_rm",
    "itinerary_sent",
    "quote_approved",
    "booking_confirmed",
    "payment_overdue",
    "no_answer_calls",
    "booking_closed",
]

MatrixAudience = Literal["customer", "rm", "account", "ops_head", "admin"]

MATRIX_EVENT_AUDIENCES: dict[MatrixEvent, tuple[MatrixAudience, ...]] = {
    "new_lead": ("customer", "admin", "ops_head"),
    "assigned_to_rm": ("customer", "rm", "ops_head", "admin"),
    "itinerary_sent": ("customer", "rm"),
    "quote_approved": ("customer", "rm", "account", "ops_head"),
    "booking_confirmed": ("customer", "rm", "account", "ops_head"),
    "payment_overdue": ("customer", "rm", "account", "ops_head"),
    "no_answer_calls": ("rm", "ops_head"),
    "booking_closed": ("customer", "rm", "account", "ops_head"),
}

MATRIX_EVENT_LABELS: dict[MatrixEvent, str] = {
    "new_lead": "New lead",
    "assigned_to_rm": "Lead assigned to RM",
    "itinerary_sent": "Itinerary sent",
    "quote_approved": "Quote approved",
    "booking_confirmed": "Booking confirmed",
    "payment_overdue": "Payment overdue",
    "no_answer_calls": "No answer (3+ calls)",
    "booking_closed": "Booking closed",
}

STATUS_TO_MATRIX_EVENT: dict[str, MatrixEvent] = {
    "ITINERARY_SENT": "itinerary_sent",
    "PROPOSAL_SENT": "itinerary_sent",
    "APPROVED": "quote_approved",
    "BOOKED": "booking_confirmed",
    "CLOSED": "booking_closed",
}

_NO_ANSWER_THRESHOLD = 3
_recent_matrix_alerts: dict[tuple[str, ...], float] = {}
_MATRIX_DEDUPE_SECONDS = 45


def matrix_catalog() -> list[dict]:
    rows: list[dict] = []
    for event, audiences in MATRIX_EVENT_AUDIENCES.items():
        rows.append(
            {
                "event": event,
                "label": MATRIX_EVENT_LABELS[event],
                "customer": "customer" in audiences,
                "rm": "rm" in audiences,
                "account": "account" in audiences,
                "ops_head": "ops_head" in audiences,
                "admin": "admin" in audiences,
            }
        )
    return rows


def matrix_event_for_status(status: str | None) -> MatrixEvent | None:
    return STATUS_TO_MATRIX_EVENT.get(resolve_pipeline_stage(status))


def _lead_name(lead: Lead) -> str:
    return f"{lead.first_name} {lead.last_name}".strip() or lead.title or "Lead"


def _crm_link(path: str = "/dashboard/crm") -> str:
    base = (settings.whatsapp_crm_base_url or "").rstrip("/")
    return f"{base}{path}" if base else "Open TRAGUIN CRM"


def _should_skip_matrix_alert(*parts: str, ttl: int = _MATRIX_DEDUPE_SECONDS) -> bool:
    key = tuple(parts)
    now = time.monotonic()
    sent_at = _recent_matrix_alerts.get(key)
    if sent_at is not None and now - sent_at < ttl:
        return True
    _recent_matrix_alerts[key] = now
    if len(_recent_matrix_alerts) > 512:
        cutoff = now - max(ttl, _MATRIX_DEDUPE_SECONDS)
        stale = [entry for entry, ts in _recent_matrix_alerts.items() if ts < cutoff]
        for entry in stale:
            _recent_matrix_alerts.pop(entry, None)
    return False


def resolve_audience_users(
    db: Session,
    *,
    agency_id: UUID,
    lead: Lead | None,
    audiences: tuple[MatrixAudience, ...],
) -> dict[MatrixAudience, list[User]]:
    resolved: dict[MatrixAudience, list[User]] = {
        "customer": [],
        "rm": [],
        "account": [],
        "ops_head": [],
        "admin": [],
    }
    if "rm" in audiences and lead is not None:
        rm = resolve_rm_user(db, lead)
        if rm is not None:
            resolved["rm"] = [rm]
    if "admin" in audiences:
        resolved["admin"] = resolve_admin_users(db, agency_id)
    if "ops_head" in audiences:
        resolved["ops_head"] = resolve_ops_head_users(db, agency_id)
    if "account" in audiences:
        resolved["account"] = resolve_account_users(db, agency_id)
    return resolved


def _staff_users_for_event(
    db: Session,
    *,
    agency_id: UUID,
    lead: Lead | None,
    audiences: tuple[MatrixAudience, ...],
    exclude_rm_email: bool = False,
) -> list[User]:
    buckets = resolve_audience_users(db, agency_id=agency_id, lead=lead, audiences=audiences)
    users: list[User] = []
    for audience in audiences:
        if audience == "customer":
            continue
        users.extend(buckets.get(audience, []))
    users = dedupe_users(users)
    if exclude_rm_email:
        rm = buckets.get("rm", [])
        rm_ids = {user.id for user in rm}
        users = [user for user in users if user.id not in rm_ids]
    return users


def _send_whatsapp_to_users(
    db: Session,
    *,
    agency_id: UUID,
    users: list[User],
    payload: CrmAlertPayload,
) -> int:
    if not settings.whatsapp_notifications_enabled:
        return 0
    fields = build_alert_fields(
        payload.event_title,
        payload.subject,
        payload.detail,
        payload.extra,
        payload.link,
    )
    sent = 0
    for user in users:
        if not user.phone:
            continue
        if send_whatsapp_template(
            user.phone,
            fields,
            db=db,
            agency_id=agency_id,
        ):
            sent += 1
    return sent


def _send_email_to_user_id(
    db: Session,
    *,
    agency_id: UUID,
    user_id: UUID,
    subject: str,
    body: str,
    html_body: str | None = None,
) -> bool:
    from services.email_notifications import _send_email_to_user

    return _send_email_to_user(
        db,
        agency_id=agency_id,
        to_user_id=user_id,
        subject=subject,
        body=body,
        html_body=html_body,
    )


def _send_customer_email(
    db: Session,
    *,
    lead: Lead,
    subject: str,
    body: str,
    html_body: str | None = None,
) -> bool:
    to_email = (lead.email or "").strip()
    if not to_email:
        return False
    from services.smtp_settings import get_agency_smtp_settings, send_agency_email

    smtp = get_agency_smtp_settings(db, lead.agency_id)
    if smtp is None or not smtp.enabled:
        return False
    agency = db.get(Agency, lead.agency_id)
    agency_name = agency.name if agency is not None else "TRAGUIN"
    send_agency_email(
        smtp,
        to_email=to_email,
        subject=subject,
        body=body,
        html_body=html_body,
        agency_name=agency_name,
    )
    return True


def _customer_welcome_body(lead: Lead, agency_name: str) -> str:
    name = lead.first_name.strip() or "Traveller"
    ref = lead.lead_code or "—"
    return "\n".join(
        [
            f"Dear {name},",
            "",
            f"Thank you for contacting {agency_name}. We have received your travel inquiry.",
            "A dedicated travel expert will reach out to you shortly.",
            "",
            f"Your inquiry reference: {ref}",
            "",
            f"Warm regards,",
            f"{agency_name}",
        ]
    )


def _customer_status_body(
    lead: Lead,
    agency_name: str,
    *,
    headline: str,
    detail: str,
) -> str:
    name = lead.first_name.strip() or "Traveller"
    return "\n".join(
        [
            f"Dear {name},",
            "",
            headline,
            "",
            detail,
            "",
            f"Inquiry reference: {lead.lead_code or '—'}",
            "",
            f"Warm regards,",
            f"{agency_name}",
        ]
    )


def _history_extra(db: Session, lead: Lead) -> str:
    history = build_customer_inquiry_history(
        db,
        agency_id=lead.agency_id,
        phone=lead.phone,
        email=lead.email,
        customer_id=lead.customer_id,
        current_lead_id=lead.id,
    )
    return format_inquiry_history_alert_extra(history)


def _history_lines(db: Session, lead: Lead) -> list[str]:
    history = build_customer_inquiry_history(
        db,
        agency_id=lead.agency_id,
        phone=lead.phone,
        email=lead.email,
        customer_id=lead.customer_id,
        current_lead_id=lead.id,
    )
    return format_inquiry_history_alert_lines(history)


def dispatch_lead_matrix_event(
    db: Session,
    event: MatrixEvent,
    lead: Lead,
    *,
    detail: str | None = None,
    extra: str | None = None,
    variables: dict[str, str] | None = None,
    dedupe_suffix: str = "",
    dedupe_ttl: int = _MATRIX_DEDUPE_SECONDS,
) -> dict[str, int]:
    if lead.is_deleted:
        return {"skipped": 1}

    if _should_skip_matrix_alert(str(lead.id), event, dedupe_suffix, ttl=dedupe_ttl):
        return {"deduped": 1}

    audiences = MATRIX_EVENT_AUDIENCES[event]
    agency = db.get(Agency, lead.agency_id)
    agency_name = agency.name if agency is not None else "TRAGUIN CRM"
    subject_name = _lead_name(lead)
    title = MATRIX_EVENT_LABELS[event]
    stage_label = pipeline_status_label(lead.status)

    history_extra = _history_extra(db, lead)
    payload_extra = extra or history_extra or f"Status: {stage_label}"
    payload_detail = detail or f"{lead.lead_code or '—'} · {lead.title or '—'}"

    payload = CrmAlertPayload(
        agency_id=lead.agency_id,
        event_title=title,
        subject=subject_name,
        detail=payload_detail,
        extra=payload_extra,
        link=_crm_link(f"/dashboard/crm?openLead={lead.id}"),
    )

    staff_users = _staff_users_for_event(
        db,
        agency_id=lead.agency_id,
        lead=lead,
        audiences=audiences,
        exclude_rm_email=(event == "assigned_to_rm"),
    )

    staff_template_id = matrix_staff_template(event)
    lead_context = build_lead_context(db, lead)
    if variables:
        lead_context.update(variables)
    if detail:
        lead_context["Detail"] = detail
    elif extra:
        lead_context["Detail"] = extra

    if staff_template_id:
        subject, html_body = render_email(staff_template_id, lead_context)
        email_body = render_plain(staff_template_id, lead_context)
        email_subject = subject
        wa_template_id = staff_template_id
        wa_fields = whatsapp_fields_for_template(staff_template_id, lead_context)
    else:
        email_subject = f"[{agency_name}] {title}: {subject_name}"
        email_lines = [
            title,
            "",
            f"Lead: {subject_name}",
            f"Code: {lead.lead_code or '—'}",
            payload_detail,
            payload_extra,
            "",
            _crm_link(f"/dashboard/crm?openLead={lead.id}"),
        ]
        history_lines = _history_lines(db, lead)
        if history_lines:
            email_lines.extend(["", "Inquiry history (internal):"])
            email_lines.extend(history_lines)
        email_body = "\n".join(email_lines)
        html_body = None
        wa_template_id = None
        wa_fields = build_alert_fields(
            payload.event_title,
            payload.subject,
            payload.detail,
            payload.extra,
            payload.link,
        )

    whatsapp_sent = 0
    if settings.whatsapp_notifications_enabled:
        for user in staff_users:
            if not user.phone:
                continue
            if wa_template_id and send_whatsapp_template(
                user.phone,
                wa_fields,
                db=db,
                agency_id=agency_id,
                notification_template_key=wa_template_id,
            ):
                whatsapp_sent += 1
            elif not wa_template_id and send_whatsapp_template(
                user.phone,
                wa_fields,
                db=db,
                agency_id=agency_id,
            ):
                whatsapp_sent += 1

    emails_sent = 0
    for user in staff_users:
        if event == "assigned_to_rm" and resolve_rm_user(db, lead) and user.id == lead.assigned_to_id:
            continue
        if staff_template_id:
            if (user.email or "").strip() and send_templated_email(
                db,
                agency_id=lead.agency_id,
                to_email=user.email or "",
                template_id=staff_template_id,
                variables=lead_context,
            ):
                emails_sent += 1
            continue
        if _send_email_to_user_id(
            db,
            agency_id=lead.agency_id,
            user_id=user.id,
            subject=email_subject,
            body=email_body,
            html_body=html_body,
        ):
            emails_sent += 1

    customer_emails = 0
    customer_whatsapp = 0
    if "customer" in audiences:
        customer_template_id = matrix_customer_template(event)
        customer_wa_template_id = matrix_customer_whatsapp_template(event)
        if customer_template_id or customer_wa_template_id:
            if customer_template_id and send_customer_lead_email(
                db, lead, customer_template_id, extra_variables=variables
            ):
                customer_emails = 1
            if (
                customer_wa_template_id
                and lead.phone
                and settings.whatsapp_notifications_enabled
                and send_templated_whatsapp(
                    lead.phone,
                    customer_wa_template_id,
                    lead_context,
                    db=db,
                    agency_id=lead.agency_id,
                )
            ):
                customer_whatsapp = 1
        else:
            customer_subject = f"{agency_name} — {title}"
            customer_body = _customer_status_body(
                lead,
                agency_name,
                headline=title,
                detail=payload_detail,
            )
            if _send_customer_email(db, lead=lead, subject=customer_subject, body=customer_body):
                customer_emails = 1

    return {
        "whatsapp": whatsapp_sent + customer_whatsapp,
        "staff_emails": emails_sent,
        "customer_emails": customer_emails,
    }


def dispatch_lead_matrix_event_by_id(
    lead_id: UUID,
    event: MatrixEvent,
    *,
    detail: str | None = None,
    extra: str | None = None,
    dedupe_suffix: str = "",
) -> None:
    from database import SessionLocal

    db = SessionLocal()
    try:
        lead = db.get(Lead, lead_id)
        if lead is None:
            return
        counts = dispatch_lead_matrix_event(
            db,
            event,
            lead,
            detail=detail,
            extra=extra,
            dedupe_suffix=dedupe_suffix,
        )
        logger.info("Matrix [%s] lead %s: %s", event, lead_id, counts)
    except Exception:
        logger.exception("Matrix notification failed for %s (%s)", lead_id, event)
    finally:
        db.close()


def notify_lead_status_matrix_by_id(
    lead_id: UUID,
    *,
    old_status: str | None,
    new_status: str | None,
) -> None:
    event = matrix_event_for_status(new_status)
    if event is None:
        return
    if resolve_pipeline_stage(old_status) == resolve_pipeline_stage(new_status):
        return
    dispatch_lead_matrix_event_by_id(
        lead_id,
        event,
        dedupe_suffix=resolve_pipeline_stage(new_status) or "",
    )


def count_no_answer_phone_attempts(db: Session, lead_id: UUID) -> int:
    rows = db.scalars(
        select(LeadActivity)
        .where(
            LeadActivity.lead_id == lead_id,
            LeadActivity.type == "PHONE",
        )
        .order_by(LeadActivity.created_at.desc())
        .limit(20)
    ).all()
    total = 0
    for row in rows:
        text = (row.description or "").lower()
        if "no answer" in text or "unanswered" in text or "did not answer" in text:
            total += 1
    return total


def maybe_notify_no_answer_calls(db: Session, lead: Lead) -> bool:
    if count_no_answer_phone_attempts(db, lead.id) < _NO_ANSWER_THRESHOLD:
        return False
    already = db.scalar(
        select(LeadActivity.id)
        .where(
            LeadActivity.lead_id == lead.id,
            LeadActivity.type == "NO_ANSWER_ALERT",
        )
        .limit(1)
    )
    if already is not None:
        return False
    dispatch_lead_matrix_event(
        db,
        "no_answer_calls",
        lead,
        detail=f"{_NO_ANSWER_THRESHOLD}+ unanswered call attempts logged",
        extra=f"Phone: {lead.phone or '—'}",
        dedupe_suffix="no_answer",
    )
    from config import settings as app_settings

    actor_id = app_settings.traguin_system_user_id or lead.assigned_to_id or lead.assigned_by_id
    if actor_id is not None:
        db.add(
            LeadActivity(
                lead_id=lead.id,
                type="NO_ANSWER_ALERT",
                description="Notification matrix: 3+ unanswered call attempts escalated to RM and Ops",
                created_by_id=actor_id,
            )
        )
    return True


def maybe_notify_no_answer_calls_by_id(lead_id: UUID) -> None:
    from database import SessionLocal

    db = SessionLocal()
    try:
        lead = db.get(Lead, lead_id)
        if lead is None or lead.is_deleted:
            return
        if maybe_notify_no_answer_calls(db, lead):
            db.commit()
    except Exception:
        db.rollback()
        logger.exception("No-answer matrix notification failed for %s", lead_id)
    finally:
        db.close()


def notify_payment_overdue_for_invoice(db: Session, invoice: Invoice) -> bool:
    if (invoice.status or "").upper() != "UNPAID":
        return False
    booking = invoice.booking
    if booking is None:
        return False
    customer = booking.customer
    if customer is None:
        return False

    lead = db.scalar(
        select(Lead)
        .where(
            Lead.agency_id == invoice.agency_id,
            Lead.is_deleted.is_(False),
            Lead.customer_id == customer.id,
        )
        .order_by(Lead.updated_at.desc())
        .limit(1)
    )
    if lead is None:
        lead = db.scalar(
            select(Lead)
            .where(
                Lead.agency_id == invoice.agency_id,
                Lead.is_deleted.is_(False),
                Lead.email.is_not(None),
                Lead.email == customer.email,
            )
            .order_by(Lead.updated_at.desc())
            .limit(1)
        )
    if lead is None:
        return False

    invoice_context = build_invoice_context(db, invoice, lead=lead)
    dispatch_lead_matrix_event(
        db,
        "payment_overdue",
        lead,
        detail=f"Invoice {invoice.invoice_number} · ₹{invoice.amount}",
        extra=f"Due: {invoice.due_date}",
        variables=invoice_context,
        dedupe_suffix=str(invoice.id),
        dedupe_ttl=86_400,
    )
    return True
