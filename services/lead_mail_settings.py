from __future__ import annotations

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from models.crm.lead_mail_settings import AgencyLeadMailRecipient, AgencyLeadMailSettings
from models.crm.tenancy import User
from schemas.crm.lead_mail_settings import (
    AgencyLeadMailSettingsRead,
    AgencyLeadMailSettingsUpdate,
    LeadMailRecipientRead,
)


def get_agency_lead_mail_settings(db: Session, agency_id: UUID) -> AgencyLeadMailSettings | None:
    return db.scalar(
        select(AgencyLeadMailSettings)
        .where(AgencyLeadMailSettings.agency_id == agency_id)
        .options(selectinload(AgencyLeadMailSettings.recipients).selectinload(AgencyLeadMailRecipient.user))
    )


def get_or_create_agency_lead_mail_settings(db: Session, agency_id: UUID) -> AgencyLeadMailSettings:
    row = get_agency_lead_mail_settings(db, agency_id)
    if row is not None:
        return row
    row = AgencyLeadMailSettings(agency_id=agency_id, enabled=True)
    db.add(row)
    db.flush()
    return row


def lead_mail_settings_to_read(row: AgencyLeadMailSettings | None) -> AgencyLeadMailSettingsRead:
    if row is None:
        return AgencyLeadMailSettingsRead()
    recipients = []
    recipient_user_ids: list[UUID] = []
    for recipient in row.recipients:
        user = recipient.user
        if user is None or user.is_deleted or not user.email.strip():
            continue
        recipient_user_ids.append(user.id)
        recipients.append(
            LeadMailRecipientRead(
                user_id=user.id,
                name=user.name,
                email=user.email,
            )
        )
    return AgencyLeadMailSettingsRead(
        enabled=row.enabled,
        recipient_user_ids=recipient_user_ids,
        recipients=recipients,
    )


def apply_lead_mail_settings_update(
    db: Session,
    row: AgencyLeadMailSettings,
    agency_id: UUID,
    payload: AgencyLeadMailSettingsUpdate,
) -> None:
    data = payload.model_dump(exclude_unset=True)
    recipient_user_ids = data.pop("recipient_user_ids", None)

    if "enabled" in data and data["enabled"] is not None:
        row.enabled = data["enabled"]

    if recipient_user_ids is None:
        return

    valid_users = db.scalars(
        select(User).where(
            User.agency_id == agency_id,
            User.is_deleted.is_(False),
            User.id.in_(recipient_user_ids),
            User.email.is_not(None),
            User.email != "",
        )
    ).all()
    valid_by_id = {user.id: user for user in valid_users}

    row.recipients.clear()
    for user_id in recipient_user_ids:
        user = valid_by_id.get(user_id)
        if user is None:
            continue
        row.recipients.append(AgencyLeadMailRecipient(settings_id=row.id, user_id=user.id))


def list_lead_notification_emails(db: Session, agency_id: UUID) -> list[str]:
    row = get_agency_lead_mail_settings(db, agency_id)
    if row is None or not row.enabled:
        return []

    emails: list[str] = []
    seen: set[str] = set()
    for recipient in row.recipients:
        user = recipient.user
        if user is None or user.is_deleted:
            continue
        email = (user.email or "").strip().lower()
        if not email or email in seen:
            continue
        seen.add(email)
        emails.append(email)
    return emails
