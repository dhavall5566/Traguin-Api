from __future__ import annotations

import logging
from uuid import UUID

from sqlalchemy.orm import Session

from database import SessionLocal
from models.crm.leads import Lead
from models.crm.tenancy import Agency
from services.lead_mail_settings import list_lead_notification_emails
from services.smtp_settings import get_agency_smtp_settings, send_agency_email

logger = logging.getLogger(__name__)


def _lead_display_name(lead: Lead) -> str:
    return f"{lead.first_name} {lead.last_name}".strip() or lead.title or "New lead"


def _build_new_lead_email_body(*, lead: Lead, agency_name: str) -> str:
    name = _lead_display_name(lead)
    lines = [
        f"A new lead was created in {agency_name}.",
        "",
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


def notify_team_new_lead_email(db: Session, lead: Lead) -> int:
    smtp = get_agency_smtp_settings(db, lead.agency_id)
    if smtp is None or not smtp.enabled:
        return 0

    recipients = list_lead_notification_emails(db, lead.agency_id)
    if not recipients:
        return 0

    agency = db.get(Agency, lead.agency_id)
    agency_name = agency.name if agency is not None else "TRAGUIN CRM"
    subject = f"{agency_name} — New lead: {_lead_display_name(lead)}"
    body = _build_new_lead_email_body(lead=lead, agency_name=agency_name)

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
            logger.exception("Lead alert email failed for %s (lead %s)", email, lead.id)
    return sent


def notify_team_new_lead_email_by_id(lead_id: UUID) -> None:
    db = SessionLocal()
    try:
        lead = db.get(Lead, lead_id)
        if lead is None or lead.is_deleted:
            return
        notify_team_new_lead_email(db, lead)
    except Exception:
        logger.exception("Email new-lead notification failed for %s", lead_id)
    finally:
        db.close()
