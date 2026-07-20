"""WhatsApp team alerts via WhatsMarketing template API for CRM events."""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import UUID

import httpx
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from config import settings
from database import SessionLocal
from models.crm.bookings import Booking
from models.crm.finance import Invoice, Payment, Quotation
from models.crm.leads import Lead, LeadFollowup
from models.crm.tenancy import User
from schemas.crm.lead_mail_settings import LeadMailEventType

from utils.lead_pipeline import PIPELINE_STATUS_LABELS

logger = logging.getLogger(__name__)

_PHONE_DIGITS = re.compile(r"\D+")

STATUS_LABELS: dict[str, str] = PIPELINE_STATUS_LABELS


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


def _meta_template_text(value: str) -> str:
    text = re.sub(r"[\r\n\t]+", " ", (value or "—").strip())
    text = re.sub(r" {2,}", " ", text)
    return text[:1024] or "—"


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


def _active_template_id() -> str:
    return (settings.whatsapp_template_id or "").strip()


_meta_access_token_cache: str | None = None
_sender_display_phone_cache: str | None = None


def get_whatsapp_sender_phone() -> str:
    global _sender_display_phone_cache
    if _sender_display_phone_cache:
        return _sender_display_phone_cache

    phone_number_id = (settings.whatsapp_phone_number_id or "").strip()
    access_token = _fetch_meta_access_token()
    if not access_token or not phone_number_id:
        return ""

    try:
        response = httpx.get(
            f"https://graph.facebook.com/v21.0/{phone_number_id}",
            params={"fields": "display_phone_number,verified_name"},
            headers={"Authorization": f"Bearer {access_token}"},
            timeout=20.0,
        )
        response.raise_for_status()
        display = str(response.json().get("display_phone_number") or "").strip()
        if display:
            _sender_display_phone_cache = display
            return display
    except httpx.HTTPError as exc:
        logger.warning("WhatsApp sender phone lookup failed: %s", exc)
    return ""


def _fetch_meta_access_token() -> str | None:
    """Reuse Meta token embedded in any synced WhatsMarketing template row."""
    global _meta_access_token_cache
    if _meta_access_token_cache:
        return _meta_access_token_cache

    api_token = _whatsapp_credentials()
    phone_number_id = (settings.whatsapp_phone_number_id or "").strip()
    if api_token is None or not phone_number_id:
        return None

    try:
        response = httpx.post(
            f"{settings.whatsapp_api_base_url.rstrip('/')}/api/v1/whatsapp/template/list",
            data={"apiToken": api_token, "phone_number_id": phone_number_id},
            timeout=20.0,
        )
        response.raise_for_status()
        for row in response.json().get("message") or []:
            raw = row.get("template_json")
            if not raw:
                continue
            token = json.loads(raw).get("access_token")
            if token:
                _meta_access_token_cache = token
                return token
    except (httpx.HTTPError, json.JSONDecodeError, TypeError) as exc:
        logger.warning("Meta access token lookup failed: %s", exc)
    return None


def _meta_body_params(fields: dict[str, str]) -> list[dict[str, str]]:
    params: list[dict[str, str]] = []
    index = 1
    while True:
        value = fields.get(f"field_{index}")
        if value is None:
            break
        params.append({"type": "text", "text": _meta_template_text(value)})
        index += 1
    if not params:
        params.append({"type": "text", "text": "—"})
    return params


def _send_via_meta_template(
    recipient: str,
    phone_number_id: str,
    template_name: str,
    template_language: str,
    fields: dict[str, str],
) -> tuple[bool, str]:
    access_token = _fetch_meta_access_token()
    if not access_token:
        return False, ""

    body_params = _meta_body_params(fields)
    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": recipient,
        "type": "template",
        "template": {
            "name": template_name,
            "language": {"code": template_language, "policy": "deterministic"},
            "components": [{"type": "body", "parameters": body_params}],
        },
    }

    try:
        response = httpx.post(
            f"https://graph.facebook.com/v21.0/{phone_number_id}/messages",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=20.0,
        )
        if response.status_code >= 400:
            logger.warning(
                "Meta WhatsApp send failed (%s): HTTP %s %s",
                template_name,
                response.status_code,
                response.text[:500],
            )
            return False, ""
        payload = response.json()
        messages = payload.get("messages") or []
        if messages:
            message_id = messages[0].get("id") or ""
            logger.info(
                "WhatsApp sent via Meta API (%s) to %s message_id=%s",
                template_name,
                recipient,
                message_id,
            )
            return True, message_id
        logger.warning("Meta WhatsApp send unexpected response: %s", response.text[:500])
        return False, ""
    except httpx.HTTPError as exc:
        logger.warning("Meta WhatsApp send error: %s", exc)
        return False, ""


def _should_retry_via_meta(body: dict) -> bool:
    message = str(body.get("message", "")).lower()
    return "template not found" in message or "template does not exist" in message


def send_whatsapp_template(
    phone_number: str,
    fields: dict[str, str],
    *,
    db: Session | None = None,
    agency_id: UUID | None = None,
    notification_template_key: str | None = None,
    force_template_id: str | None = None,
    force_template_name: str | None = None,
    force_template_language: str | None = None,
) -> bool:
    return send_whatsapp_template_with_result(
        phone_number,
        fields,
        db=db,
        agency_id=agency_id,
        notification_template_key=notification_template_key,
        force_template_id=force_template_id,
        force_template_name=force_template_name,
        force_template_language=force_template_language,
    ).ok


def send_whatsapp_template_with_result(
    phone_number: str,
    fields: dict[str, str],
    *,
    db: Session | None = None,
    agency_id: UUID | None = None,
    notification_template_key: str | None = None,
    force_template_id: str | None = None,
    force_template_name: str | None = None,
    force_template_language: str | None = None,
) -> "WhatsAppSendResult":
    from services.whatsapp_template_settings import WhatsAppSendResult, resolve_whatsapp_template

    api_token = _whatsapp_credentials()
    phone_number_id = (settings.whatsapp_phone_number_id or "").strip()
    if force_template_id or force_template_name:
        template_id = (force_template_id or "").strip()
        template_name = (force_template_name or "").strip()
        template_language = (force_template_language or settings.whatsapp_lead_template_language).strip()
    else:
        resolved = resolve_whatsapp_template(db, agency_id, notification_template_key)
        template_id = resolved.template_id or _active_template_id()
        template_name = resolved.template_name or _active_template_name()
        template_language = resolved.template_language or settings.whatsapp_lead_template_language
    if api_token is None or not phone_number_id or not (template_id or template_name):
        logger.warning(
            "WhatsApp notifications skipped: missing apiToken, phone_number_id, or template"
        )
        return WhatsAppSendResult(ok=False, error="Missing WhatsApp API credentials or template.")

    recipient = _recipient_phone(phone_number)
    if recipient is None:
        logger.warning("WhatsApp send skipped: invalid phone %s", phone_number)
        return WhatsAppSendResult(ok=False, error=f"Invalid phone number: {phone_number}")

    base = settings.whatsapp_api_base_url.rstrip("/")
    url = f"{base}/api/v1/whatsapp/send/template"
    data: dict[str, str] = {
        "apiToken": api_token,
        "phone_number_id": phone_number_id,
        "phone_number": recipient,
        **fields,
    }
    if template_id:
        data["template_id"] = template_id
        data["template_language"] = template_language
    else:
        data["template_name"] = template_name
        data["template_language"] = template_language

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
        else:
            body = response.json()
            if str(body.get("status")) == "1":
                message_id = str(body.get("wa_message_id") or "")
                logger.info(
                    "WhatsApp sent via WhatsMarketing (%s) to %s message_id=%s",
                    template_id or template_name,
                    recipient,
                    message_id,
                )
                return WhatsAppSendResult(
                    ok=True,
                    recipient=f"+{recipient}",
                    template_id=template_id,
                    template_name=template_name,
                    message_id=message_id,
                )
            if not _should_retry_via_meta(body):
                logger.warning(
                    "WhatsApp send rejected (%s) for %s: %s",
                    fields.get("field_1", "alert"),
                    phone_number,
                    response.text[:500],
                )
    except httpx.HTTPError as exc:
        logger.warning("WhatsApp send error for %s: %s", phone_number, exc)

    if settings.whatsapp_use_meta_api and template_name and _fetch_meta_access_token():
        meta_ok, message_id = _send_via_meta_template(
            recipient,
            phone_number_id,
            template_name,
            template_language,
            fields,
        )
        if meta_ok:
            return WhatsAppSendResult(
                ok=True,
                recipient=f"+{recipient}",
                template_id=template_id,
                template_name=template_name,
                message_id=message_id,
            )

    return WhatsAppSendResult(
        ok=False,
        recipient=f"+{recipient}",
        template_id=template_id,
        template_name=template_name,
        error="WhatsApp provider rejected the message. Check template sync and phone number.",
    )


def notify_team(db: Session, agency_id: UUID, fields: dict[str, str]) -> int:
    if not settings.whatsapp_notifications_enabled:
        return 0

    phones = list_team_notification_phones(db, agency_id)
    if not phones:
        logger.info("WhatsApp alert skipped: no team phones for agency %s", agency_id)
        return 0

    sent = sum(
        1
        for phone in phones
        if send_whatsapp_template(
            phone,
            fields,
            db=db,
            agency_id=agency_id,
        )
    )
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
    from services.notification_matrix import dispatch_lead_matrix_event

    counts = dispatch_lead_matrix_event(db, "new_lead", lead)
    return counts.get("whatsapp", 0)


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

    # Staff email/WhatsApp routed via notification matrix (Admin + Ops Head).


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
        if notice.assigned_changed and lead.assigned_to_id is not None:
            from services.notification_matrix import dispatch_lead_matrix_event

            dispatch_lead_matrix_event(db, "assigned_to_rm", lead)
            from services.email_notifications import notify_lead_assigned_email_by_id

            notify_lead_assigned_email_by_id(lead.id)

        if notice.status_changed and notice.new_status:
            from services.notification_matrix import (
                matrix_event_for_status,
                notify_lead_status_matrix_by_id,
            )

            if matrix_event_for_status(notice.new_status):
                notify_lead_status_matrix_by_id(
                    lead.id,
                    old_status=notice.old_status,
                    new_status=notice.new_status,
                )
            else:
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
        booking = invoice.booking
        customer = booking.customer if booking else None
        lead = None
        if customer is not None:
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
        from services.notification_templates.context import build_invoice_context
        from services.notification_templates.delivery import (
            send_templated_email,
            send_templated_whatsapp,
        )

        variables = build_invoice_context(db, invoice, lead=lead)
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
        if customer is not None:
            if customer.email:
                send_templated_email(
                    db,
                    agency_id=invoice.agency_id,
                    to_email=customer.email,
                    template_id="customer_payment_invoice",
                    variables=variables,
                )
            if customer.phone:
                send_templated_whatsapp(
                    customer.phone,
                    "customer_payment_invoice",
                    variables,
                    db=db,
                    agency_id=invoice.agency_id,
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
        booking = invoice.booking if invoice else None
        customer = booking.customer if booking else None
        lead = None
        if customer is not None:
            lead = db.scalar(
                select(Lead)
                .where(
                    Lead.agency_id == payment.agency_id,
                    Lead.is_deleted.is_(False),
                    Lead.customer_id == customer.id,
                )
                .order_by(Lead.updated_at.desc())
                .limit(1)
            )
        from services.notification_templates.context import build_invoice_context
        from services.notification_templates.delivery import (
            send_templated_email,
            send_templated_whatsapp,
        )

        variables = build_invoice_context(db, invoice, lead=lead, payment=payment) if invoice else {}
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
        if customer is not None and variables:
            if customer.email:
                send_templated_email(
                    db,
                    agency_id=payment.agency_id,
                    to_email=customer.email,
                    template_id="customer_payment_receipt",
                    variables=variables,
                )
            if customer.phone:
                send_templated_whatsapp(
                    customer.phone,
                    "customer_payment_receipt",
                    variables,
                    db=db,
                    agency_id=payment.agency_id,
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
            or_(Lead.status == "ITINERARY_SENT", Lead.status == "PROPOSAL_SENT"),
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
                detail=f"In itinerary stage since {_format_dt(sent_at)}",
                extra=f"Value: ₹{lead.value}",
            ),
        )
        counts["proposal_stuck"] += 1

    from services.notification_matrix import notify_payment_overdue_for_invoice

    overdue_invoices = db.scalars(
        select(Invoice).where(
            Invoice.status == "UNPAID",
            Invoice.due_date < now,
        )
    ).all()
    counts["payment_overdue"] = 0
    for invoice in overdue_invoices:
        if notify_payment_overdue_for_invoice(db, invoice):
            counts["payment_overdue"] += 1

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
