"""Traguin notification template library — email HTML + WhatsApp text."""

from services.notification_templates.catalog import TEMPLATE_IDS, get_template
from services.notification_templates.renderer import render_email, render_plain, render_whatsapp

__all__ = [
    "TEMPLATE_IDS",
    "build_booking_context",
    "build_invoice_context",
    "build_lead_context",
    "get_template",
    "render_email",
    "render_plain",
    "render_whatsapp",
    "send_customer_lead_email",
    "send_team_lead_email",
    "send_templated_email",
    "whatsapp_fields_for_template",
]


def __getattr__(name: str):
    if name in {"build_booking_context", "build_invoice_context", "build_lead_context"}:
        from services.notification_templates import context as ctx

        return getattr(ctx, name)
    if name in {
        "send_customer_lead_email",
        "send_team_lead_email",
        "send_templated_email",
        "whatsapp_fields_for_template",
    }:
        from services.notification_templates import delivery as dlv

        return getattr(dlv, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
