"""Send rendered notification templates via email and WhatsApp."""

from __future__ import annotations

import logging
from uuid import UUID

from sqlalchemy.orm import Session

from models.crm.leads import Lead
from models.crm.tenancy import Agency, User
from services.notification_templates.catalog import get_template
from services.notification_templates.context import build_lead_context
from services.notification_templates.renderer import render_email, render_plain, render_whatsapp
from services.smtp_settings import get_agency_smtp_settings, send_agency_email
from services.whatsapp_notifications import send_whatsapp_template

logger = logging.getLogger(__name__)

_MATRIX_CUSTOMER_TEMPLATE: dict[str, str] = {
    "new_lead": "customer_inquiry_received",
    "assigned_to_rm": "customer_enquiry_welcome",
    "itinerary_sent": "customer_itinerary_sent",
    "quote_approved": "customer_quote",
    "booking_confirmed": "customer_booking_confirmed",
    "payment_overdue": "customer_payment_overdue",
    "booking_closed": "customer_trip_complete",
}

# Events mapped to None skip customer WhatsApp (email may still send).
_MATRIX_CUSTOMER_WHATSAPP_TEMPLATE: dict[str, str | None] = {
    "assigned_to_rm": None,
}

_MATRIX_STAFF_TEMPLATE: dict[str, str] = {
    "new_lead": "team_new_lead",
    "assigned_to_rm": "team_new_lead",
    "booking_confirmed": "team_booking_confirmed",
    "payment_overdue": "team_payment_overdue",
    "no_answer_calls": "team_dump_lead",
}


def whatsapp_fields_for_template(template_id: str, variables: dict[str, str]) -> dict[str, str]:
    """Map catalog WhatsApp copy into WhatsMarketing/Meta template fields."""
    if template_id == "customer_inquiry_received":
        return {
            "field_1": (variables.get("Customer_Name") or "Customer")[:200],
        }

    if template_id == "customer_enquiry_welcome":
        return {
            "field_1": (variables.get("Customer_Name") or "Customer")[:200],
            "field_2": (variables.get("Temp_ID") or "—")[:200],
            "field_3": (variables.get("Destination") or "—")[:200],
            "field_4": (variables.get("Travel_Dates") or "—")[:200],
            "field_5": (variables.get("RM_Name") or "—")[:200],
        }

    spec = get_template(template_id)
    rendered = render_whatsapp(template_id, variables)
    lines = [line.strip() for line in rendered.splitlines() if line.strip()]
    title = lines[0] if lines else spec.subject
    body = "\n".join(lines[1:]) if len(lines) > 1 else rendered
    link = variables.get("CRM_Link") or variables.get("Accept_Link") or variables.get("Payment_Link") or "—"
    return {
        "field_1": title[:200],
        "field_2": (variables.get("Customer_Name") or variables.get("Temp_ID") or "—")[:200],
        "field_3": body[:200],
        "field_4": (variables.get("Destination") or variables.get("Detail") or body[200:400] or "—")[:200],
        "field_5": link[:200],
    }


def send_templated_email(
    db: Session,
    *,
    agency_id: UUID,
    to_email: str,
    template_id: str,
    variables: dict[str, str],
) -> bool:
    to_email = (to_email or "").strip()
    if not to_email:
        return False
    smtp = get_agency_smtp_settings(db, agency_id)
    if smtp is None or not smtp.enabled:
        return False
    agency = db.get(Agency, agency_id)
    agency_name = agency.name if agency is not None else "TRAGUIN"
    try:
        subject, html_body = render_email(template_id, variables)
        plain_body = render_plain(template_id, variables)
        send_agency_email(
            smtp,
            to_email=to_email,
            subject=subject,
            body=plain_body,
            html_body=html_body,
            agency_name=agency_name,
        )
        return True
    except Exception:
        logger.exception("Templated email failed (%s) to %s", template_id, to_email)
        return False


def send_templated_whatsapp(
    phone: str,
    template_id: str,
    variables: dict[str, str],
    *,
    db: Session | None = None,
    agency_id: UUID | None = None,
    force_template_id: str | None = None,
    force_template_name: str | None = None,
    force_template_language: str | None = None,
) -> bool:
    spec = get_template(template_id)
    if not spec.whatsapp_text:
        return False
    fields = whatsapp_fields_for_template(template_id, variables)
    return send_whatsapp_template(
        phone,
        fields,
        db=db,
        agency_id=agency_id,
        notification_template_key=template_id,
        force_template_id=force_template_id,
        force_template_name=force_template_name,
        force_template_language=force_template_language,
    )


def send_customer_lead_email(
    db: Session,
    lead: Lead,
    template_id: str,
    *,
    extra_variables: dict[str, str] | None = None,
) -> bool:
    if not (lead.email or "").strip():
        return False
    variables = build_lead_context(db, lead)
    if extra_variables:
        variables.update(extra_variables)
    return send_templated_email(
        db,
        agency_id=lead.agency_id,
        to_email=lead.email or "",
        template_id=template_id,
        variables=variables,
    )


def send_team_lead_email(
    db: Session,
    lead: Lead,
    user: User,
    template_id: str,
    *,
    extra_variables: dict[str, str] | None = None,
) -> bool:
    variables = build_lead_context(db, lead, rm_user=user)
    if extra_variables:
        variables.update(extra_variables)
    if not (user.email or "").strip():
        return False
    return send_templated_email(
        db,
        agency_id=lead.agency_id,
        to_email=user.email or "",
        template_id=template_id,
        variables=variables,
    )


def matrix_customer_template(event: str) -> str | None:
    return _MATRIX_CUSTOMER_TEMPLATE.get(event)


def matrix_customer_whatsapp_template(event: str) -> str | None:
    if event in _MATRIX_CUSTOMER_WHATSAPP_TEMPLATE:
        return _MATRIX_CUSTOMER_WHATSAPP_TEMPLATE[event]
    email_template_id = matrix_customer_template(event)
    if not email_template_id:
        return None
    spec = get_template(email_template_id)
    return email_template_id if spec.whatsapp_text else None


def matrix_staff_template(event: str) -> str | None:
    return _MATRIX_STAFF_TEMPLATE.get(event)
