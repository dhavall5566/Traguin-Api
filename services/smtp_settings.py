from __future__ import annotations

import smtplib
import ssl
from email.message import EmailMessage
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.crm.smtp_settings import AgencySmtpSettings
from schemas.crm.smtp_settings import AgencySmtpSettingsRead, AgencySmtpSettingsUpdate


def get_agency_smtp_settings(db: Session, agency_id: UUID) -> AgencySmtpSettings | None:
    return db.scalar(select(AgencySmtpSettings).where(AgencySmtpSettings.agency_id == agency_id))


def get_or_create_agency_smtp_settings(db: Session, agency_id: UUID) -> AgencySmtpSettings:
    row = get_agency_smtp_settings(db, agency_id)
    if row is not None:
        return row
    row = AgencySmtpSettings(agency_id=agency_id)
    db.add(row)
    db.flush()
    return row


def smtp_settings_to_read(row: AgencySmtpSettings) -> AgencySmtpSettingsRead:
    return AgencySmtpSettingsRead(
        enabled=row.enabled,
        host=row.host or "",
        port=row.port or 587,
        use_tls=row.use_tls,
        use_ssl=row.use_ssl,
        username=row.username or "",
        from_email=row.from_email or "",
        from_name=row.from_name or "",
        password_configured=bool(row.password),
    )


def normalize_smtp_security(
    port: int | None,
    use_tls: bool,
    use_ssl: bool,
) -> tuple[int, bool, bool]:
    """Align port and encryption mode (587 → STARTTLS, 465 → SSL)."""
    port = port or 587

    if use_ssl and use_tls:
        if port == 465:
            use_tls = False
        else:
            use_ssl = False
            use_tls = True

    if use_ssl and port != 465:
        use_ssl = False
        use_tls = True

    if use_tls and port == 465:
        use_tls = False
        use_ssl = True

    if not use_ssl and not use_tls:
        if port == 465:
            use_ssl = True
        else:
            use_tls = True

    return port, use_tls, use_ssl


def apply_smtp_settings_update(row: AgencySmtpSettings, payload: AgencySmtpSettingsUpdate) -> None:
    data = payload.model_dump(exclude_unset=True)
    password = data.pop("password", None)
    for key, value in data.items():
        if value is None:
            continue
        setattr(row, key, value.strip() if isinstance(value, str) else value)
    if password is not None:
        cleaned = password.strip()
        if cleaned:
            row.password = cleaned

    port, use_tls, use_ssl = normalize_smtp_security(row.port, row.use_tls, row.use_ssl)
    row.port = port
    row.use_tls = use_tls
    row.use_ssl = use_ssl


def send_agency_email(
    row: AgencySmtpSettings,
    *,
    to_email: str,
    subject: str,
    body: str,
    agency_name: str,
) -> None:
    if not row.enabled:
        raise ValueError("SMTP is not enabled for this workspace.")
    if not row.host.strip():
        raise ValueError("SMTP host is required.")
    if not row.from_email.strip():
        raise ValueError("From email is required.")
    if not row.password:
        raise ValueError("SMTP password is required.")

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = (
        f"{row.from_name} <{row.from_email}>" if row.from_name.strip() else row.from_email
    )
    message["To"] = to_email
    message.set_content(body)

    username = row.username.strip() or None
    password = row.password or ""
    port, use_tls, use_ssl = normalize_smtp_security(row.port, row.use_tls, row.use_ssl)
    host = row.host.strip()

    if use_ssl:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(host, port, context=context, timeout=20) as client:
            if username:
                client.login(username, password)
            client.send_message(message)
        return

    with smtplib.SMTP(host, port, timeout=20) as client:
        client.ehlo()
        if use_tls:
            context = ssl.create_default_context()
            client.starttls(context=context)
            client.ehlo()
        if username:
            client.login(username, password)
        client.send_message(message)


def send_smtp_test_email(
    row: AgencySmtpSettings,
    *,
    to_email: str,
    agency_name: str,
) -> None:
    send_agency_email(
        row,
        to_email=to_email,
        subject=f"{agency_name} — SMTP test",
        body=(
            "This is a test email from your TRAGUIN CRM workspace SMTP settings.\n\n"
            "If you received this message, outbound mail is configured correctly."
        ),
        agency_name=agency_name,
    )
