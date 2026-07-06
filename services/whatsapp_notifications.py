"""WhatsApp team alerts via WhatsMarketing template API for CRM events."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import UUID

import httpx
from sqlalchemy import select
from sqlalchemy.orm import Session

from config import settings
from database import SessionLocal
from models.crm.bookings import Booking
from models.crm.finance import Invoice, Payment, Quotation
from models.crm.leads import Lead, LeadFollowup
from models.crm.tenancy import User
from schemas.crm.lead_mail_settings import LeadMailEventType

logger = logging.getLogger(__name__)

_PHONE_DIGITS = re.compile(r"\D+")

STATUS_LABELS: dict[str, str] = {
    "NEW": "New lead",
    "CONTACTED": "Contacted",
    "PROPOSAL_SENT": "Proposal sent",
    "NEGOTIATION": "Negotiation",
    "CONFIRMED": "Confirmed (won)",
    "LOST": "Lost",
}


@dataclass(frozen=True)
class CrmAlertPayload:
    agency_id: UUID
    event_title: str
    subject: str
    detail: str
    extra: str = ""
    link: str | None = None


def _whatsapp_credentials() -> str | None:
    """Full apiToken string for WhatsMarketing (format: user_id|token)."""
    raw = (settings.whatsapp_api_url or "").strip()
    return raw if raw and "|" in raw else None


def _recipient_phone(phone: str) -> str | None:
    """WhatsMarketing expects digits only with country code (no + sign)."""
    digits = _PHONE_DIGITS.sub("", phone.strip())
    if len(digits) < 10:
        return None
    if len(digits) == 10:
        return f"91{digits}"
    return digits


def _crm_dashboard_link(path: str = "/dashboard/crm") -> str:
    base = (settings.whatsapp_crm_base_url or "").rstrip("/")
    return f"{base}{path}" if base else "Open TRAGUIN CRM"


def _clip(value: str, limit: int = 200) -> str:
    text = (value or "—").strip()
    return text[:limit] if text else "—"


def list_team_notification_phones(db: Session, agency_id: UUID) -> list[str]:
    users = db.scalars(
        select(User)
        .where(
            User.agency_id == agency_id,
            User.is_deleted.is_(False),
            User.phone.is_not(None),
            User.phone != "",
        )
        .order_by(User.name)
    ).all()
    seen: set[str] = set()
    phones: list[str] = []
    for user in users:
        normalized = _recipient_phone(user.phone or "")
        if normalized:
            display = f"+{normalized}"
            if display not in seen:
                seen.add(display)
                phones.append(display)
    return phones


def build_alert_fields(
    event_title: str,
    subject: str,
    detail: str,
    extra: str = "",
    link: str | None = None,
) -> dict[str, str]:
    return {
        "field_1": _clip(event_title),
        "field_2": _clip(subject),
        "field_3": _clip(detail),
        "field_4": _clip(extra),
        "field_5": _clip(link or _crm_dashboard_link()),
    }


def _active_template_name() -> str:
    return (
        (settings.whatsapp_crm_template or settings.whatsapp_lead_template or "")
        .strip()
    )


def send_whatsapp_template(phone_number: str, fields: dict[str, str]) -> bool:
    api_token = _whatsapp_credentials()
    phone_number_id = (settings.whatsapp_phone_number_id or "").strip()
    template = _active_template_name()
    if api_token is None or not phone_number_id or not template:
        logger.warning(
            "WhatsApp notifications skipped: missing apiToken, phone_number_id, or template name"
        )
        return False

    recipient = _recipient_phone(phone_number)
    if recipient is None:
        logger.warning("WhatsApp send skipped: invalid phone %s", phone_number)
        return False

    base = settings.whatsapp_api_base_url.rstrip("/")
    url = f"{base}/api/v1/whatsapp/send/template"
    data = {
        "apiToken": api_token,
        "phone_number_id": phone_number_id,
        "phone_number": recipient,
        "template_name": template,
        "template_language": settings.whatsapp_lead_template_language,
        **fields,
    }

    try:
        response = httpx.post(
            url,
            data=data,
            headers={"Accept": "application/json"},
            timeout=20.0,
        )
        if response.status_code >= 400:
            logger.warning(
                "WhatsApp send failed (%s) for %s: HTTP %s %s",
                fields.get("field_1", "alert"),
                phone_number,
                response.status_code,
                response.text[:500],
            )
            return False
        body = response.json()
        if str(body.get("status")) != "1":
            logger.warning(
                "WhatsApp send rejected (%s) for %s: %s",
                fields.get("field_1", "alert"),
                phone_number,
                response.text[:500],
            )
            return False
        return True
    except httpx.HTTPError as exc:
        logger.warning("WhatsApp send error for %s: %s", phone_number, exc)
        return False


def notify_team(db: Session, agency_id: UUID, fields: dict[str, str]) -> int:
    if not settings.whatsapp_notifications_enabled:
        return 0

    phones = list_team_notification_phones(db, agency_id)
    if not phones:
        logger.info("WhatsApp alert skipped: no team phones for agency %s", agency_id)
        return 0

    sent = sum(1 for phone in phones if send_whatsapp_template(phone, fields))
    logger.info(
        "WhatsApp [%s] agency %s: sent %s/%s",
        fields.get("field_1", "alert"),
        agency_id,
        sent,
        len(phones),
    )
    return sent


def send_crm_alert(db: Session, payload: CrmAlertPayload) -> int:
    fields = build_alert_fields(
        payload.event_title,
        payload.subject,
        payload.detail,
        payload.extra,
        payload.link,
    )
    return notify_team(db, payload.agency_id, fields)


def dispatch_crm_alert(payload: CrmAlertPayload) -> None:
    db = SessionLocal()
    try:
        send_crm_alert(db, payload)
    except Exception:
        logger.exception("WhatsApp alert failed: %s", payload.event_title)
    finally:
        db.close()


def _lead_display_name(lead: Lead) -> str:
    return f"{lead.first_name} {lead.last_name}".strip()


def _user_name(db: Session, user_id: UUID | None) -> str:
    if user_id is None:
        return "Unassigned"
    user = db.get(User, user_id)
    return user.name if user else "Team member"


# --- Lead events ---


def notify_team_new_lead(db: Session, lead: Lead) -> int:
    return send_crm_alert(
        db,
        CrmAlertPayload(
            agency_id=lead.agency_id,
            event_title="New lead",
            subject=_lead_display_name(lead),
            detail=f"Source: {lead.source or 'Unknown'} · {lead.lead_code or '—'}",
            extra=f"Phone: {lead.phone or '—'} · Status: {lead.status}",
        ),
    )


def notify_team_new_lead_by_id(lead_id: UUID, *, event_type: LeadMailEventType = "crm_lead") -> None:
    db = SessionLocal()
    try:
        lead = db.get(Lead, lead_id)
        if lead is None or lead.is_deleted:
            return
        notify_team_new_lead(db, lead)
    except Exception:
        logger.exception("WhatsApp new-lead notification failed for %s", lead_id)
    finally:
        db.close()

    from services.email_notifications import notify_team_new_lead_email_by_id

    notify_team_new_lead_email_by_id(lead_id, event_type=event_type)


@dataclass
class LeadUpdateNotice:
    assigned_changed: bool = False
    assignee_name: str | None = None
    status_changed: bool = False
    old_status: str | None = None
    new_status: str | None = None
    followups_added: int = 0
    note_on_unassigned: bool = False


def notify_lead_update_by_id(lead_id: UUID, notice: LeadUpdateNotice) -> None:
    db = SessionLocal()
    try:
        lead = db.get(Lead, lead_id)
        if lead is None or lead.is_deleted:
            return

        name = _lead_display_name(lead)
        if notice.assigned_changed:
            send_crm_alert(
                db,
                CrmAlertPayload(
                    agency_id=lead.agency_id,
                    event_title="Lead assigned",
                    subject=name,
                    detail=f"Assigned to: {notice.assignee_name or 'Unassigned'}",
                    extra=f"Title: {lead.title}",
                ),
            )

        if notice.status_changed and notice.new_status:
            label = STATUS_LABELS.get(notice.new_status.upper(), notice.new_status)
            send_crm_alert(
                db,
                CrmAlertPayload(
                    agency_id=lead.agency_id,
                    event_title=f"Lead status · {label}",
                    subject=name,
                    detail=f"{notice.old_status or '—'} → {notice.new_status}",
                    extra=f"Source: {lead.source or '—'}",
                ),
            )
            from services.email_notifications import notify_lead_status_change_email_by_id

            notify_lead_status_change_email_by_id(
                lead.id,
                old_status=notice.old_status,
                new_status=notice.new_status,
            )

        if notice.followups_added > 0:
            send_crm_alert(
                db,
                CrmAlertPayload(
                    agency_id=lead.agency_id,
                    event_title="Follow-up scheduled",
                    subject=name,
                    detail=f"{notice.followups_added} follow-up(s) added",
                    extra=f"Status: {lead.status}",
                ),
            )

        if notice.note_on_unassigned:
            send_crm_alert(
                db,
                CrmAlertPayload(
                    agency_id=lead.agency_id,
                    event_title="Note on unassigned lead",
                    subject=name,
                    detail="New note added — no assignee yet",
                    extra=f"Phone: {lead.phone or '—'}",
                ),
            )
    except Exception:
        logger.exception("WhatsApp lead-update notification failed for %s", lead_id)
    finally:
        db.close()


# --- Booking / finance events ---


def notify_booking_created_by_id(booking_id: UUID) -> None:
    db = SessionLocal()
    try:
        booking = db.get(Booking, booking_id)
        if booking is None:
            return
        customer_name = booking.customer.name if booking.customer else "Customer"
        send_crm_alert(
            db,
            CrmAlertPayload(
                agency_id=booking.agency_id,
                event_title="New booking",
                subject=customer_name,
                detail=f"Status: {booking.status}",
                extra=f"Booking ID: {str(booking.id)[:8]}",
                link=_crm_dashboard_link("/dashboard/operations"),
            ),
        )
    except Exception:
        logger.exception("WhatsApp booking notification failed for %s", booking_id)
    finally:
        db.close()


def notify_quotation_created_by_id(quotation_id: UUID) -> None:
    db = SessionLocal()
    try:
        quotation = db.get(Quotation, quotation_id)
        if quotation is None:
            return
        send_crm_alert(
            db,
            CrmAlertPayload(
                agency_id=quotation.agency_id,
                event_title="Quotation created",
                subject=f"₹{quotation.amount}",
                detail=f"Status: {quotation.status}",
                extra=f"Quotation ID: {str(quotation.id)[:8]}",
                link=_crm_dashboard_link("/dashboard/finance"),
            ),
        )
    except Exception:
        logger.exception("WhatsApp quotation notification failed for %s", quotation_id)
    finally:
        db.close()


def notify_invoice_created_by_id(invoice_id: UUID) -> None:
    db = SessionLocal()
    try:
        invoice = db.get(Invoice, invoice_id)
        if invoice is None:
            return
        send_crm_alert(
            db,
            CrmAlertPayload(
                agency_id=invoice.agency_id,
                event_title="Invoice created",
                subject=invoice.invoice_number,
                detail=f"Amount: ₹{invoice.amount}",
                extra=f"Status: {invoice.status}",
                link=_crm_dashboard_link("/dashboard/finance"),
            ),
        )
    except Exception:
        logger.exception("WhatsApp invoice notification failed for %s", invoice_id)
    finally:
        db.close()


def notify_payment_received_by_id(payment_id: UUID) -> None:
    db = SessionLocal()
    try:
        payment = db.get(Payment, payment_id)
        if payment is None:
            return
        invoice = payment.invoice
        invoice_no = invoice.invoice_number if invoice else "—"
        send_crm_alert(
            db,
            CrmAlertPayload(
                agency_id=payment.agency_id,
                event_title="Payment received",
                subject=f"₹{payment.amount}",
                detail=f"Invoice: {invoice_no}",
                extra=f"Method: {payment.payment_method}",
                link=_crm_dashboard_link("/dashboard/finance"),
            ),
        )
    except Exception:
        logger.exception("WhatsApp payment notification failed for %s", payment_id)
    finally:
        db.close()


# --- Scheduled reminders (run via scripts/run_crm_whatsapp_reminders.py) ---


def _format_dt(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).strftime("%d %b %Y %H:%M UTC")


def run_scheduled_reminders(db: Session) -> dict[str, int]:
    """Send due-today, overdue follow-up, and stuck-proposal alerts. Run once daily."""
    if not settings.whatsapp_notifications_enabled:
        return {"skipped": 1}

    now = datetime.now(timezone.utc)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    today_end = today_start.replace(hour=23, minute=59, second=59, microsecond=999999)

    counts = {"followup_due_today": 0, "followup_overdue": 0, "proposal_stuck": 0}

    due_today = db.scalars(
        select(LeadFollowup)
        .join(Lead, LeadFollowup.lead_id == Lead.id)
        .where(
            Lead.is_deleted.is_(False),
            LeadFollowup.status == "PENDING",
            LeadFollowup.scheduled_at >= today_start,
            LeadFollowup.scheduled_at <= today_end,
        )
    ).all()
    for followup in due_today:
        lead = followup.lead
        if lead is None:
            continue
        send_crm_alert(
            db,
            CrmAlertPayload(
                agency_id=lead.agency_id,
                event_title="Follow-up due today",
                subject=_lead_display_name(lead),
                detail=f"Scheduled: {_format_dt(followup.scheduled_at)}",
                extra=f"Status: {lead.status}",
            ),
        )
        counts["followup_due_today"] += 1

    overdue = db.scalars(
        select(LeadFollowup)
        .join(Lead, LeadFollowup.lead_id == Lead.id)
        .where(
            Lead.is_deleted.is_(False),
            LeadFollowup.status == "PENDING",
            LeadFollowup.scheduled_at < today_start,
        )
    ).all()
    for followup in overdue:
        lead = followup.lead
        if lead is None:
            continue
        send_crm_alert(
            db,
            CrmAlertPayload(
                agency_id=lead.agency_id,
                event_title="Follow-up overdue",
                subject=_lead_display_name(lead),
                detail=f"Was due: {_format_dt(followup.scheduled_at)}",
                extra=f"Status: {lead.status}",
            ),
        )
        counts["followup_overdue"] += 1

    stuck_cutoff = now.timestamp() - (7 * 24 * 3600)
    stuck_leads = db.scalars(
        select(Lead).where(
            Lead.is_deleted.is_(False),
            Lead.status == "PROPOSAL_SENT",
            Lead.proposal_sent_at.is_not(None),
        )
    ).all()
    for lead in stuck_leads:
        if lead.proposal_sent_at is None:
            continue
        sent_at = lead.proposal_sent_at
        if sent_at.tzinfo is None:
            sent_at = sent_at.replace(tzinfo=timezone.utc)
        if sent_at.timestamp() > stuck_cutoff:
            continue
        send_crm_alert(
            db,
            CrmAlertPayload(
                agency_id=lead.agency_id,
                event_title="Proposal stuck 7+ days",
                subject=_lead_display_name(lead),
                detail=f"In PROPOSAL_SENT since {_format_dt(sent_at)}",
                extra=f"Value: ₹{lead.value}",
            ),
        )
        counts["proposal_stuck"] += 1

    return counts


def run_scheduled_reminders_job() -> None:
    db = SessionLocal()
    try:
        counts = run_scheduled_reminders(db)
        logger.info("WhatsApp scheduled reminders complete: %s", counts)
    except Exception:
        logger.exception("WhatsApp scheduled reminders failed")
    finally:
        db.close()
