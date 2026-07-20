from __future__ import annotations

import logging
import re
import time
from dataclasses import dataclass
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

import httpx

from config import settings
from models.crm.tenancy import Agency, User
from models.crm.whatsapp_template_settings import AgencyWhatsAppTemplateSettings
from schemas.crm.whatsapp_template_settings import (
    AgencyWhatsAppTemplateSettingsRead,
    AgencyWhatsAppTemplateSettingsUpdate,
    WhatsAppTemplateCatalogEntry,
)
from services.notification_templates.delivery import send_templated_whatsapp, whatsapp_fields_for_template
from services.notification_templates.renderer import render_whatsapp
from services.whatsapp_notifications import send_whatsapp_template_with_result
from services.notification_templates.catalog import TEMPLATE_IDS, get_template

_DIGITS_ONLY = re.compile(r"^\d+$")
logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class ResolvedWhatsAppTemplate:
    template_id: str
    template_name: str
    template_language: str


@dataclass(frozen=True)
class WhatsAppSendResult:
    ok: bool
    recipient: str = ""
    template_id: str = ""
    template_name: str = ""
    message_id: str = ""
    error: str = ""


# WhatsMarketing internal IDs (not Meta template IDs). Synced from Meta in WhatsMarketing UI.
_CATALOG_WHATSAPP_DEFAULTS: dict[str, ResolvedWhatsAppTemplate] = {
    "customer_inquiry_received": ResolvedWhatsAppTemplate(
        template_id="409886",
        template_name="crm_inquery_received_f",
        template_language="en_US",
    ),
    "customer_enquiry_welcome": ResolvedWhatsAppTemplate(
        template_id="409874",
        template_name="crm_customer_welcom",
        template_language="en_US",
    ),
}

_WM_TEMPLATE_ROWS: dict[str, dict] = {}
_WM_TEMPLATE_ROWS_LOADED_AT = 0.0
_WM_TEMPLATE_CACHE_SECONDS = 300


def get_agency_whatsapp_template_settings(
    db: Session, agency_id: UUID
) -> AgencyWhatsAppTemplateSettings | None:
    return db.scalar(
        select(AgencyWhatsAppTemplateSettings).where(
            AgencyWhatsAppTemplateSettings.agency_id == agency_id
        )
    )


def get_or_create_agency_whatsapp_template_settings(
    db: Session, agency_id: UUID
) -> AgencyWhatsAppTemplateSettings:
    row = get_agency_whatsapp_template_settings(db, agency_id)
    if row is not None:
        return row
    row = AgencyWhatsAppTemplateSettings(agency_id=agency_id)
    db.add(row)
    db.flush()
    return row


def _env_default_template_id() -> str:
    return (settings.whatsapp_template_id or "").strip()


def _env_default_template_name() -> str:
    return (
        (settings.whatsapp_crm_template or settings.whatsapp_lead_template or "")
        .strip()
    )


def _env_template_language() -> str:
    return (settings.whatsapp_lead_template_language or "en").strip() or "en"


def _catalog_default_template(notification_template_key: str | None) -> ResolvedWhatsAppTemplate | None:
    if not notification_template_key:
        return None
    catalog_default = _CATALOG_WHATSAPP_DEFAULTS.get(notification_template_key)
    if catalog_default is None:
        return None
    template_id = (settings.whatsapp_customer_inquiry_template_id or catalog_default.template_id).strip()
    return ResolvedWhatsAppTemplate(
        template_id=template_id,
        template_name=catalog_default.template_name,
        template_language=catalog_default.template_language,
    )


def _normalize_overrides(raw: dict | None) -> dict[str, str]:
    if not raw:
        return {}
    normalized: dict[str, str] = {}
    for key, value in raw.items():
        catalog_id = str(key).strip()
        template_value = str(value or "").strip()
        if not catalog_id or catalog_id not in TEMPLATE_IDS:
            continue
        if template_value:
            normalized[catalog_id] = template_value
    return normalized


def _split_template_value(value: str) -> tuple[str, str]:
    text = (value or "").strip()
    if not text:
        return "", ""
    if _DIGITS_ONLY.match(text):
        return text, ""
    return "", text


def _load_wm_template_rows() -> dict[str, dict]:
    global _WM_TEMPLATE_ROWS, _WM_TEMPLATE_ROWS_LOADED_AT
    now = time.monotonic()
    if _WM_TEMPLATE_ROWS and now - _WM_TEMPLATE_ROWS_LOADED_AT < _WM_TEMPLATE_CACHE_SECONDS:
        return _WM_TEMPLATE_ROWS

    api_token = (settings.whatsapp_api_url or "").strip()
    phone_number_id = (settings.whatsapp_phone_number_id or "").strip()
    if not api_token or "|" not in api_token or not phone_number_id:
        return _WM_TEMPLATE_ROWS

    try:
        response = httpx.post(
            f"{settings.whatsapp_api_base_url.rstrip('/')}/api/v1/whatsapp/template/list",
            data={"apiToken": api_token, "phone_number_id": phone_number_id},
            timeout=20.0,
        )
        response.raise_for_status()
        rows: dict[str, dict] = {}
        for row in response.json().get("message") or []:
            wm_id = str(row.get("id") or "").strip()
            if wm_id:
                rows[wm_id] = row
        _WM_TEMPLATE_ROWS = rows
        _WM_TEMPLATE_ROWS_LOADED_AT = now
    except (httpx.HTTPError, TypeError, ValueError) as exc:
        logger.warning("WhatsMarketing template list lookup failed: %s", exc)
    return _WM_TEMPLATE_ROWS


def enrich_resolved_whatsapp_template(
    resolved: ResolvedWhatsAppTemplate,
) -> ResolvedWhatsAppTemplate:
    if not resolved.template_id:
        return resolved
    row = _load_wm_template_rows().get(resolved.template_id)
    if row is None:
        return resolved
    locale = str(row.get("locale") or resolved.template_language or "en_US").replace("-", "_")
    template_name = str(row.get("template_name") or resolved.template_name or "").strip()
    return ResolvedWhatsAppTemplate(
        template_id=resolved.template_id,
        template_name=template_name,
        template_language=locale,
    )


def get_whatsapp_sender_display_phone() -> str:
    from services.whatsapp_notifications import get_whatsapp_sender_phone

    return get_whatsapp_sender_phone()


def whatsapp_template_catalog() -> list[WhatsAppTemplateCatalogEntry]:
    entries: list[WhatsAppTemplateCatalogEntry] = []
    for template_id in TEMPLATE_IDS:
        spec = get_template(template_id)
        if template_id.startswith("customer_"):
            audience = "customer"
        elif template_id.startswith("team_"):
            audience = "team"
        else:
            audience = "other"
        catalog_binding = _CATALOG_WHATSAPP_DEFAULTS.get(template_id)
        entries.append(
            WhatsAppTemplateCatalogEntry(
                id=template_id,
                subject=spec.subject,
                whatsapp_enabled=bool(spec.whatsapp_text),
                audience=audience,
                whatsapp_text=spec.whatsapp_text or "",
                default_template_id=catalog_binding.template_id if catalog_binding else "",
                default_template_name=catalog_binding.template_name if catalog_binding else "",
            )
        )
    return entries


def whatsapp_settings_to_read(
    row: AgencyWhatsAppTemplateSettings | None,
) -> AgencyWhatsAppTemplateSettingsRead:
    if row is None:
        return AgencyWhatsAppTemplateSettingsRead(
            env_default_template_id=_env_default_template_id(),
            env_default_template_name=_env_default_template_name(),
            env_template_language=_env_template_language(),
            sender_display_phone=get_whatsapp_sender_display_phone(),
        )
    return AgencyWhatsAppTemplateSettingsRead(
        default_template_id=row.default_template_id or "",
        default_template_name=row.default_template_name or "",
        template_language=row.template_language or "en",
        overrides=_normalize_overrides(row.template_overrides),
        env_default_template_id=_env_default_template_id(),
        env_default_template_name=_env_default_template_name(),
        env_template_language=_env_template_language(),
        sender_display_phone=get_whatsapp_sender_display_phone(),
    )


def apply_whatsapp_template_settings_update(
    row: AgencyWhatsAppTemplateSettings,
    payload: AgencyWhatsAppTemplateSettingsUpdate,
) -> None:
    data = payload.model_dump(exclude_unset=True)
    overrides = data.pop("overrides", None)
    for key, value in data.items():
        if value is None:
            continue
        setattr(row, key, str(value).strip() if key != "template_language" else str(value).strip())
    if overrides is not None:
        row.template_overrides = _normalize_overrides(overrides)


def resolve_whatsapp_template(
    db: Session | None,
    agency_id: UUID | None,
    notification_template_key: str | None = None,
) -> ResolvedWhatsAppTemplate:
    template_id = ""
    template_name = ""
    template_language = _env_template_language()

    row: AgencyWhatsAppTemplateSettings | None = None
    if db is not None and agency_id is not None:
        row = get_agency_whatsapp_template_settings(db, agency_id)

    if row is not None:
        template_language = (row.template_language or "").strip() or template_language
        override_value = ""
        if notification_template_key:
            override_value = str((row.template_overrides or {}).get(notification_template_key, "")).strip()
        if override_value:
            template_id, template_name = _split_template_value(override_value)
        elif notification_template_key:
            catalog_default = _catalog_default_template(notification_template_key)
            if catalog_default is not None:
                return enrich_resolved_whatsapp_template(catalog_default)
            template_id = (row.default_template_id or "").strip()
            template_name = (row.default_template_name or "").strip()
        else:
            template_id = (row.default_template_id or "").strip()
            template_name = (row.default_template_name or "").strip()

    if not template_id and not template_name and notification_template_key:
        catalog_default = _catalog_default_template(notification_template_key)
        if catalog_default is not None:
            return enrich_resolved_whatsapp_template(catalog_default)

    if not template_id and not template_name:
        template_id = _env_default_template_id()
        template_name = _env_default_template_name()

    return enrich_resolved_whatsapp_template(
        ResolvedWhatsAppTemplate(
            template_id=template_id,
            template_name=template_name,
            template_language=template_language,
        )
    )


def sample_notification_variables(*, user: User, agency: Agency | None = None) -> dict[str, str]:
    """Sample placeholder values for WhatsApp template trial sends."""
    from datetime import date, timedelta

    from services.notification_templates.context import DEFAULT_EMERGENCY_PHONE, DEFAULT_SUPPORT_PHONE

    agency_name = agency.name if agency is not None else "Traguin Travel"
    rm_name = (user.name or "Travel Expert").strip() or "Travel Expert"
    travel_start = date.today() + timedelta(days=30)
    travel_end = travel_start + timedelta(days=6)
    crm_base = (settings.whatsapp_crm_base_url or "http://localhost:3002").rstrip("/")
    crm_link = f"{crm_base}/dashboard/crm"
    return {
        "Customer_Name": "Test Customer",
        "Temp_ID": "TEMP202607080001-WEB",
        "Customer_ID": "CUS-TEST-001",
        "Booking_ID": "BK-TEST-001",
        "Destination": "Bali, Indonesia",
        "Travel_Dates": f"{travel_start.strftime('%d %b %Y')} – {travel_end.strftime('%d %b %Y')}",
        "Travel_Start": travel_start.strftime("%d %b %Y"),
        "Travel_End": travel_end.strftime("%d %b %Y"),
        "Guests": "2",
        "RM_Name": rm_name,
        "RM_Phone": (user.phone or DEFAULT_SUPPORT_PHONE).strip() or DEFAULT_SUPPORT_PHONE,
        "Phone": "+91 98765 43210",
        "Priority": "High",
        "Inquiry_Count": "1",
        "Active_Enquiry_1": "Bali inquiry",
        "Active_Enquiry_2": "—",
        "Customer_Flags": "Test send",
        "CRM_Link": crm_link,
        "Accept_Link": f"{crm_link}?assignmentAction=accept",
        "Reject_Link": f"{crm_link}?assignmentAction=reject",
        "Support_Phone": DEFAULT_SUPPORT_PHONE,
        "Emergency_Phone": DEFAULT_EMERGENCY_PHONE,
        "Elapsed_Time": "15 minutes",
        "Escalation_Level": "Tier 2 — Ops Head",
        "Escalation_Message": f"Test escalation alert from {agency_name}.",
        "Nights": "6",
        "Quote_Valid_Till": (date.today() + timedelta(days=7)).strftime("%d %b %Y"),
        "Total_Amount": "1,25,000.00",
        "Inclusions_Summary": "Flights, hotel, transfers, breakfast",
        "Invoice_No": "INV-TEST-001",
        "Due_Date": (date.today() + timedelta(days=7)).strftime("%d %b %Y"),
        "Due_Amount": "62,500.00",
        "Payment_Link": f"{crm_base}/dashboard/finance",
        "Receipt_No": "RCPT-TEST-001",
        "Paid_Amount": "62,500.00",
        "Payment_Date": date.today().strftime("%d %b %Y"),
        "Balance_Remaining": "₹0.00",
        "Balance_Message": "Your booking is fully paid.",
        "Docs_Link": f"{crm_base}/dashboard/documents",
        "Days_Left": "7",
        "Feedback_Link": "https://traguin.in/feedback",
        "Attempt_Count": "3",
        "Detail": "Trial WhatsApp template send from CRM settings.",
    }


def send_whatsapp_template_test(
    db: Session,
    *,
    agency_id: UUID,
    user: User,
    catalog_id: str,
    to_phone: str | None = None,
    template_override: str | None = None,
) -> WhatsAppSendResult:
    catalog_key = catalog_id.strip()
    if catalog_key not in TEMPLATE_IDS:
        raise ValueError("Unknown notification template.")

    spec = get_template(catalog_key)
    if not spec.whatsapp_text:
        raise ValueError("This notification does not support WhatsApp.")

    if not settings.whatsapp_notifications_enabled:
        raise ValueError("WhatsApp notifications are disabled on the server.")

    recipient = (to_phone or user.phone or "").strip()
    if not recipient:
        raise ValueError("Provide a test phone number or add one to your user profile.")

    agency = db.get(Agency, agency_id)
    variables = sample_notification_variables(user=user, agency=agency)
    variables["Customer_Name"] = (user.name or "Test Customer").strip() or "Test Customer"

    override_value = (template_override or "").strip()
    if override_value:
        template_id, template_name = _split_template_value(override_value)
        resolved = ResolvedWhatsAppTemplate(
            template_id=template_id,
            template_name=template_name,
            template_language=_env_template_language(),
        )
    else:
        resolved = resolve_whatsapp_template(db, agency_id, catalog_key)

    resolved = enrich_resolved_whatsapp_template(resolved)

    if not resolved.template_id and not resolved.template_name:
        raise ValueError(
            "No WhatsApp template configured. Set a default template or enter an override."
        )

    preview = render_whatsapp(catalog_key, variables)
    fields = whatsapp_fields_for_template(catalog_key, variables)
    result = send_whatsapp_template_with_result(
        recipient,
        fields,
        db=db,
        agency_id=agency_id,
        notification_template_key=catalog_key,
        force_template_id=resolved.template_id or None,
        force_template_name=resolved.template_name or None,
        force_template_language=resolved.template_language,
    )
    if not result.ok:
        raise ValueError(
            result.error
            or "WhatsApp provider did not accept the test message. "
            "Check API credentials, template approval, and phone number."
        )

    logger.info(
        "WhatsApp template test sent (%s) to %s template=%s/%s message_id=%s preview=%s",
        catalog_key,
        result.recipient,
        resolved.template_id,
        resolved.template_name,
        result.message_id,
        preview[:120],
    )
    return result
