from __future__ import annotations

import logging
import time
from uuid import UUID

from sqlalchemy.orm import Session

from database import SessionLocal
from models.crm.leads import Lead
from models.crm.tenancy import Agency
from schemas.crm.lead_mail_settings import LeadMailEventType
from services.lead_mail_settings import list_lead_notification_emails
from services.smtp_settings import get_agency_smtp_settings, send_agency_email

logger = logging.getLogger(__name__)

_LEAD_EMAIL_DEDUPE_SECONDS = 30
_recent_lead_emails: dict[tuple[str, ...], float] = {}


def _should_skip_duplicate_lead_email(
    lead_id: UUID,
    event_type: LeadMailEventType,
    *,
    dedupe_suffix: str = "",
) -> bool:
    """Suppress duplicate lead alert emails when the same event fires twice in quick succession."""
    key = (str(lead_id), event_type, dedupe_suffix)
    now = time.monotonic()
    sent_at = _recent_lead_emails.get(key)
    if sent_at is not None and now - sent_at < _LEAD_EMAIL_DEDUPE_SECONDS:
        logger.info(
            "Skipping duplicate lead email for lead %s (%s%s)",
            lead_id,
            event_type,
            f" · {dedupe_suffix}" if dedupe_suffix else "",
        )
        return True

    _recent_lead_emails[key] = now
    if len(_recent_lead_emails) > 512:
        cutoff = now - _LEAD_EMAIL_DEDUPE_SECONDS
        stale = [entry for entry, ts in _recent_lead_emails.items() if ts < cutoff]
        for entry in stale:
            _recent_lead_emails.pop(entry, None)
    return False


STATUS_LABELS = {
    "NEW": "New",
    "CONTACTED": "Contacted",
    "QUALIFIED": "Qualified",
    "PROPOSAL": "Proposal",
    "NEGOTIATION": "Negotiation",
    "WON": "Won",
    "LOST": "Lost",
}


def _lead_display_name(lead: Lead) -> str:
    return f"{lead.first_name} {lead.last_name}".strip() or lead.title or "Lead"


def _build_new_lead_email_body(*, lead: Lead, agency_name: str, source_label: str) -> str:
    name = _lead_display_name(lead)
    lines = [
        f"A new lead was created in {agency_name}.",
        "",
        f"Trigger: {source_label}",
        f"Name: {name}",
        f"Lead code: {lead.lead_code or '—'}",
        f"Phone: {lead.phone or '—'}",
        f"Email: {lead.email or '—'}",
        f"Source: {lead.source or 'Unknown'}",
        f"Status: {lead.status}",
        f"Title: {lead.title or '—'}",
    ]
    if lead.message:
        lines.extend(["", "Message:", lead.message.strip()])
    lines.extend(["", "Open your CRM dashboard to review and assign this lead."])
    return "\n".join(lines)


def _build_status_change_email_body(
    *,
    lead: Lead,
    agency_name: str,
    old_status: str | None,
    new_status: str | None,
) -> str:
    name = _lead_display_name(lead)
    old_label = STATUS_LABELS.get((old_status or "").upper(), old_status or "—")
    new_label = STATUS_LABELS.get((new_status or "").upper(), new_status or "—")
    lines = [
        f"A lead status was updated in {agency_name}.",
        "",
        f"Name: {name}",
        f"Lead code: {lead.lead_code or '—'}",
        f"Status: {old_label} → {new_label}",
        f"Phone: {lead.phone or '—'}",
        f"Email: {lead.email or '—'}",
        f"Source: {lead.source or 'Unknown'}",
        f"Title: {lead.title or '—'}",
        "",
        "Open your CRM dashboard to review this lead.",
    ]
    return "\n".join(lines)


def _send_lead_emails(
    db: Session,
    *,
    agency_id: UUID,
    event_type: LeadMailEventType,
    subject: str,
    body: str,
    lead_id: UUID,
    dedupe_suffix: str = "",
) -> int:
    if _should_skip_duplicate_lead_email(lead_id, event_type, dedupe_suffix=dedupe_suffix):
        return 0

    smtp = get_agency_smtp_settings(db, agency_id)
    if smtp is None or not smtp.enabled:
        return 0

    recipients = list_lead_notification_emails(db, agency_id, event_type)
    if not recipients:
        return 0

    agency = db.get(Agency, agency_id)
    agency_name = agency.name if agency is not None else "TRAGUIN CRM"

    sent = 0
    for email in recipients:
        try:
            send_agency_email(
                smtp,
                to_email=email,
                subject=subject,
                body=body,
                agency_name=agency_name,
            )
            sent += 1
        except Exception:
            logger.exception("Lead alert email failed for %s (lead %s)", email, lead_id)
    return sent


def notify_team_new_lead_email(
    db: Session,
    lead: Lead,
    *,
    event_type: LeadMailEventType,
) -> int:
    agency = db.get(Agency, lead.agency_id)
    agency_name = agency.name if agency is not None else "TRAGUIN CRM"
    source_label = {
        "website_lead": "Website lead form",
        "crm_lead": "CRM lead creation",
    }.get(event_type, "New lead")
    subject = f"{agency_name} — New lead: {_lead_display_name(lead)}"
    body = _build_new_lead_email_body(lead=lead, agency_name=agency_name, source_label=source_label)
    return _send_lead_emails(
        db,
        agency_id=lead.agency_id,
        event_type=event_type,
        subject=subject,
        body=body,
        lead_id=lead.id,
    )


def notify_team_new_lead_email_by_id(lead_id: UUID, *, event_type: LeadMailEventType) -> None:
    db = SessionLocal()
    try:
        lead = db.get(Lead, lead_id)
        if lead is None or lead.is_deleted:
            return
        notify_team_new_lead_email(db, lead, event_type=event_type)
    except Exception:
        logger.exception("Email new-lead notification failed for %s", lead_id)
    finally:
        db.close()


def notify_lead_status_change_email_by_id(
    lead_id: UUID,
    *,
    old_status: str | None,
    new_status: str | None,
) -> None:
    db = SessionLocal()
    try:
        lead = db.get(Lead, lead_id)
        if lead is None or lead.is_deleted:
            return
        agency = db.get(Agency, lead.agency_id)
        agency_name = agency.name if agency is not None else "TRAGUIN CRM"
        new_label = STATUS_LABELS.get((new_status or "").upper(), new_status or "Updated")
        subject = f"{agency_name} — Lead status · {new_label}: {_lead_display_name(lead)}"
        body = _build_status_change_email_body(
            lead=lead,
            agency_name=agency_name,
            old_status=old_status,
            new_status=new_status,
        )
        _send_lead_emails(
            db,
            agency_id=lead.agency_id,
            event_type="status_change",
            subject=subject,
            body=body,
            lead_id=lead.id,
            dedupe_suffix=(new_status or "").upper(),
        )
    except Exception:
        logger.exception("Email lead status notification failed for %s", lead_id)
    finally:
        db.close()
