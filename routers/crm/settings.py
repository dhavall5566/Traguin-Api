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
from schemas.crm.notification_matrix import NotificationMatrixRowRead
from schemas.crm.smtp_settings import (
    AgencySmtpSettingsRead,
    AgencySmtpSettingsUpdate,
    MessageResponse,
    SmtpTestEmailRequest,
)
from schemas.crm.whatsapp_template_settings import (
    AgencyWhatsAppTemplateSettingsRead,
    AgencyWhatsAppTemplateSettingsUpdate,
    WhatsAppTemplateCatalogEntry,
    WhatsAppTemplateTestRequest,
)
from services.crm_audit import audit_update
from services.lead_mail_settings import (
    apply_lead_mail_settings_update,
    get_agency_lead_mail_settings,
    get_or_create_agency_lead_mail_settings_for_update,
    lead_mail_settings_to_read,
    lead_mail_update_needs_row_lock,
)
from services.smtp_settings import (
    apply_smtp_settings_update,
    get_agency_smtp_settings,
    get_or_create_agency_smtp_settings,
    send_smtp_test_email,
    smtp_settings_to_read,
)
from services.whatsapp_template_settings import (
    apply_whatsapp_template_settings_update,
    get_agency_whatsapp_template_settings,
    get_or_create_agency_whatsapp_template_settings,
    get_whatsapp_sender_display_phone,
    send_whatsapp_template_test,
    whatsapp_settings_to_read,
    whatsapp_template_catalog,
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


@router.get("/lead-mail", response_model=AgencyLeadMailSettingsRead)
def get_lead_mail_settings(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    row = get_agency_lead_mail_settings(db, agency_id)
    return lead_mail_settings_to_read(row)


@router.put("/lead-mail", status_code=status.HTTP_204_NO_CONTENT)
def update_lead_mail_settings(
    payload: AgencyLeadMailSettingsUpdate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    _ = current_user
    row = get_or_create_agency_lead_mail_settings_for_update(
        db,
        agency_id,
        lock=lead_mail_update_needs_row_lock(payload),
    )
    apply_lead_mail_settings_update(db, row, agency_id, payload)
    commit_or_raise(db)


@router.get("/notification-matrix", response_model=list[NotificationMatrixRowRead])
def get_notification_matrix(
    agency_id: UUID = Depends(require_agency_scope),
):
    _ = agency_id
    from services.notification_matrix import matrix_catalog

    return [NotificationMatrixRowRead.model_validate(row) for row in matrix_catalog()]


@router.get("/whatsapp-templates/catalog", response_model=list[WhatsAppTemplateCatalogEntry])
def get_whatsapp_template_catalog(
    agency_id: UUID = Depends(require_agency_scope),
):
    _ = agency_id
    return whatsapp_template_catalog()


@router.get("/whatsapp-templates", response_model=AgencyWhatsAppTemplateSettingsRead)
def get_whatsapp_template_settings(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    row = get_agency_whatsapp_template_settings(db, agency_id)
    return whatsapp_settings_to_read(row)


@router.put("/whatsapp-templates", response_model=AgencyWhatsAppTemplateSettingsRead)
def update_whatsapp_template_settings(
    payload: AgencyWhatsAppTemplateSettingsUpdate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    _get_agency(db, agency_id)
    row = get_or_create_agency_whatsapp_template_settings(db, agency_id)
    apply_whatsapp_template_settings_update(row, payload)
    audit_update(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="AgencyWhatsAppTemplateSettings",
        entity_id=row.id,
        details="Updated workspace WhatsApp template settings",
        changed_fields=[
            "default_template_id",
            "default_template_name",
            "template_language",
            "template_overrides",
        ],
    )
    commit_or_raise(db)
    db.refresh(row)
    return whatsapp_settings_to_read(row)


@router.post("/whatsapp-templates/test", response_model=MessageResponse)
def test_whatsapp_template(
    payload: WhatsAppTemplateTestRequest,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    _get_agency(db, agency_id)
    try:
        result = send_whatsapp_template_test(
            db,
            agency_id=agency_id,
            user=current_user,
            catalog_id=payload.catalog_id,
            to_phone=payload.to_phone,
            template_override=payload.template_override,
        )
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    template_label = result.template_id or result.template_name or payload.catalog_id
    sender = get_whatsapp_sender_display_phone()
    detail = (
        f"Test WhatsApp sent to {result.recipient} using template {template_label}."
    )
    if result.message_id:
        detail = f"{detail} Message ID: {result.message_id}"
    if sender:
        detail = f"{detail} Check WhatsApp from Traguin ({sender})."
    return MessageResponse(message=detail)
