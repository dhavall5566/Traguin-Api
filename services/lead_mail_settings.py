from __future__ import annotations

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from models.crm.lead_mail_settings import (
    LEAD_MAIL_EVENT_CRM_LEAD,
    LEAD_MAIL_EVENT_STATUS_CHANGE,
    LEAD_MAIL_EVENT_TYPES,
    LEAD_MAIL_EVENT_WEBSITE_LEAD,
    AgencyLeadMailRecipient,
    AgencyLeadMailSettings,
)
from models.crm.tenancy import User
from schemas.crm.lead_mail_settings import (
    AgencyLeadMailSettingsRead,
    AgencyLeadMailSettingsUpdate,
    LeadMailEventRead,
    LeadMailEventUpdate,
    LeadMailEventType,
    LeadMailRecipientRead,
)

_EVENT_ENABLED_ATTR: dict[LeadMailEventType, str] = {
    LEAD_MAIL_EVENT_WEBSITE_LEAD: "website_lead_enabled",
    LEAD_MAIL_EVENT_CRM_LEAD: "crm_lead_enabled",
    LEAD_MAIL_EVENT_STATUS_CHANGE: "status_change_enabled",
}


def get_agency_lead_mail_settings(db: Session, agency_id: UUID) -> AgencyLeadMailSettings | None:
    return db.scalar(
        select(AgencyLeadMailSettings)
        .where(AgencyLeadMailSettings.agency_id == agency_id)
        .options(selectinload(AgencyLeadMailSettings.recipients).selectinload(AgencyLeadMailRecipient.user))
    )


def get_or_create_agency_lead_mail_settings_for_update(
    db: Session,
    agency_id: UUID,
    *,
    lock: bool = True,
) -> AgencyLeadMailSettings:
    """Load settings for writes. Row lock only when recipient rows may change."""
    query = select(AgencyLeadMailSettings).where(AgencyLeadMailSettings.agency_id == agency_id)
    if lock:
        query = query.with_for_update()
    row = db.scalar(query)
    if row is not None:
        return row
    row = AgencyLeadMailSettings(agency_id=agency_id, enabled=True)
    db.add(row)
    db.flush()
    return row


def get_or_create_agency_lead_mail_settings(db: Session, agency_id: UUID) -> AgencyLeadMailSettings:
    row = get_agency_lead_mail_settings(db, agency_id)
    if row is not None:
        return row
    row = AgencyLeadMailSettings(agency_id=agency_id, enabled=True)
    db.add(row)
    db.flush()
    return row


def _event_enabled(row: AgencyLeadMailSettings, event_type: LeadMailEventType) -> bool:
    attr = _EVENT_ENABLED_ATTR[event_type]
    return bool(getattr(row, attr))


def _recipients_for_event(
    row: AgencyLeadMailSettings,
    event_type: LeadMailEventType,
) -> tuple[list[UUID], list[LeadMailRecipientRead]]:
    recipient_user_ids: list[UUID] = []
    recipients: list[LeadMailRecipientRead] = []
    for recipient in row.recipients:
        if recipient.event_type != event_type:
            continue
        user = recipient.user
        if user is None or user.is_deleted or not (user.email or "").strip():
            continue
        recipient_user_ids.append(user.id)
        recipients.append(
            LeadMailRecipientRead(
                user_id=user.id,
                name=user.name,
                email=user.email,
            )
        )
    return recipient_user_ids, recipients


def lead_mail_settings_to_read(row: AgencyLeadMailSettings | None) -> AgencyLeadMailSettingsRead:
    if row is None:
        return AgencyLeadMailSettingsRead(
            events=[
                LeadMailEventRead(event_type=event_type, enabled=event_type != LEAD_MAIL_EVENT_STATUS_CHANGE)
                for event_type in LEAD_MAIL_EVENT_TYPES
            ]
        )

    events: list[LeadMailEventRead] = []
    for event_type in LEAD_MAIL_EVENT_TYPES:
        recipient_user_ids, recipients = _recipients_for_event(row, event_type)
        events.append(
            LeadMailEventRead(
                event_type=event_type,
                enabled=_event_enabled(row, event_type),
                recipient_user_ids=recipient_user_ids,
                recipients=recipients,
            )
        )
    return AgencyLeadMailSettingsRead(events=events)


def _apply_event_update(
    db: Session,
    row: AgencyLeadMailSettings,
    agency_id: UUID,
    payload: LeadMailEventUpdate,
) -> None:
    attr = _EVENT_ENABLED_ATTR[payload.event_type]
    if payload.enabled is not None:
        setattr(row, attr, payload.enabled)
        row.enabled = any(_event_enabled(row, event_type) for event_type in LEAD_MAIL_EVENT_TYPES)

    if payload.recipient_user_ids is None:
        return

    if not payload.recipient_user_ids:
        existing_for_event = db.scalars(
            select(AgencyLeadMailRecipient).where(
                AgencyLeadMailRecipient.settings_id == row.id,
                AgencyLeadMailRecipient.event_type == payload.event_type,
            )
        ).all()
        for recipient in existing_for_event:
            db.delete(recipient)
        db.expire(row, ["recipients"])
        db.flush()
        return

    desired_user_ids = list(dict.fromkeys(payload.recipient_user_ids))

    valid_users = db.scalars(
        select(User).where(
            User.agency_id == agency_id,
            User.is_deleted.is_(False),
            User.id.in_(desired_user_ids),
            User.email.is_not(None),
            User.email != "",
        )
    ).all()
    valid_by_id = {user.id: user for user in valid_users}
    desired_set = {user_id for user_id in desired_user_ids if user_id in valid_by_id}

    existing_for_event = db.scalars(
        select(AgencyLeadMailRecipient).where(
            AgencyLeadMailRecipient.settings_id == row.id,
            AgencyLeadMailRecipient.event_type == payload.event_type,
        )
    ).all()
    existing_by_user = {recipient.user_id: recipient for recipient in existing_for_event}

    for user_id, recipient in existing_by_user.items():
        if user_id not in desired_set:
            db.delete(recipient)

    for user_id in desired_user_ids:
        if user_id not in valid_by_id or user_id in existing_by_user:
            continue
        db.add(
            AgencyLeadMailRecipient(
                settings_id=row.id,
                user_id=user_id,
                event_type=payload.event_type,
            )
        )

    db.expire(row, ["recipients"])
    db.flush()


def apply_lead_mail_settings_update(
    db: Session,
    row: AgencyLeadMailSettings,
    agency_id: UUID,
    payload: AgencyLeadMailSettingsUpdate,
) -> None:
    if not payload.events:
        return
    for event in payload.events:
        _apply_event_update(db, row, agency_id, event)


def lead_mail_update_needs_row_lock(payload: AgencyLeadMailSettingsUpdate) -> bool:
    if not payload.events:
        return False
    return any(event.recipient_user_ids is not None for event in payload.events)


def list_lead_notification_emails(
    db: Session,
    agency_id: UUID,
    event_type: LeadMailEventType,
) -> list[str]:
    row = get_agency_lead_mail_settings(db, agency_id)
    if row is None or not _event_enabled(row, event_type):
        return []

    emails: list[str] = []
    seen: set[str] = set()
    for recipient in row.recipients:
        if recipient.event_type != event_type:
            continue
        user = recipient.user
        if user is None or user.is_deleted:
            continue
        email = (user.email or "").strip().lower()
        if not email or email in seen:
            continue
        seen.add(email)
        emails.append(email)
    return emails
