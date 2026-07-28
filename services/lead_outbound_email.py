"""Send outbound email from CRM to a lead's customer address."""

from __future__ import annotations

from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.crm.leads import Lead, LeadActivity
from models.crm.tenancy import Agency, User
from services.smtp_settings import get_agency_smtp_settings, send_agency_email


def send_lead_outbound_email(
    db: Session,
    lead: Lead,
    *,
    actor: User,
    subject: str,
    body: str,
    html_body: str | None = None,
) -> None:
    to_email = (lead.email or "").strip()
    if not to_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This lead has no email address.",
        )

    smtp = get_agency_smtp_settings(db, lead.agency_id)
    if smtp is None or not smtp.enabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Outbound email is not configured. Set up SMTP in Workspace Settings.",
        )

    agency = db.get(Agency, lead.agency_id)
    agency_name = agency.name if agency is not None else "TRAGUIN CRM"

    send_agency_email(
        smtp,
        to_email=to_email,
        subject=subject.strip(),
        body=body.strip(),
        html_body=html_body.strip() if html_body else None,
        agency_name=agency_name,
    )

    preview = subject.strip()
    if len(preview) > 120:
        preview = f"{preview[:117]}…"
    db.add(
        LeadActivity(
            lead_id=lead.id,
            type="EMAIL",
            description=f"Email sent to customer ({to_email}): {preview}",
            created_by_id=actor.id,
        )
    )
