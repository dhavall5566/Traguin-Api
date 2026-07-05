from uuid import UUID

import smtplib

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_agency_scope, require_crm_user
from models.crm.tenancy import Agency, User
from schemas.crm.lead_mail_settings import (
    AgencyLeadMailSettingsRead,
    AgencyLeadMailSettingsUpdate,
)
from schemas.crm.smtp_settings import (
    AgencySmtpSettingsRead,
    AgencySmtpSettingsUpdate,
    MessageResponse,
    SmtpTestEmailRequest,
)
from services.crm_audit import audit_update
from services.lead_mail_settings import (
    apply_lead_mail_settings_update,
    get_agency_lead_mail_settings,
    get_or_create_agency_lead_mail_settings,
    lead_mail_settings_to_read,
)
from services.smtp_settings import (
    apply_smtp_settings_update,
    get_agency_smtp_settings,
    get_or_create_agency_smtp_settings,
    send_smtp_test_email,
    smtp_settings_to_read,
)
from utils.db import commit_or_raise

router = APIRouter()


def _get_agency(db: Session, agency_id: UUID) -> Agency:
    agency = db.get(Agency, agency_id)
    if agency is None or agency.is_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agency not found.")
    return agency


@router.get("/smtp", response_model=AgencySmtpSettingsRead)
def get_smtp_settings(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    row = get_agency_smtp_settings(db, agency_id)
    if row is None:
        return AgencySmtpSettingsRead()
    return smtp_settings_to_read(row)


@router.put("/smtp", response_model=AgencySmtpSettingsRead)
def update_smtp_settings(
    payload: AgencySmtpSettingsUpdate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    agency = _get_agency(db, agency_id)
    row = get_or_create_agency_smtp_settings(db, agency_id)
    apply_smtp_settings_update(row, payload)
    audit_update(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="AgencySmtpSettings",
        entity_id=row.id,
        details="Updated workspace SMTP settings",
        changed_fields=["enabled", "host", "port", "use_tls", "use_ssl", "username", "from_email", "from_name"],
    )
    commit_or_raise(db)
    db.refresh(row)
    return smtp_settings_to_read(row)


@router.post("/smtp/test", response_model=MessageResponse)
def test_smtp_settings(
    payload: SmtpTestEmailRequest,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    agency = _get_agency(db, agency_id)
    row = get_or_create_agency_smtp_settings(db, agency_id)
    if not row.enabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Enable SMTP before sending a test email.",
        )

    to_email = (payload.to_email or current_user.email or "").strip()
    if not to_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Provide a test recipient email or ensure your user profile has an email.",
        )

    try:
        send_smtp_test_email(row, to_email=to_email, agency_name=agency.name)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except smtplib.SMTPException as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"SMTP server rejected the message: {exc}",
        ) from exc
    except OSError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Could not connect to the SMTP server: {exc}",
        ) from exc

    return MessageResponse(message=f"Test email sent to {to_email}.")
