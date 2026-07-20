"""Render {{Variable}} placeholders in notification templates."""

from __future__ import annotations

import html
import re

from services.notification_templates.catalog import NotificationTemplate, get_template
from services.notification_templates.layout import wrap_email_html

_PLACEHOLDER_RE = re.compile(r"\{\{(\w+)\}\}")


def _escape(value: str | None) -> str:
    return html.escape((value or "—").strip() or "—", quote=True)


def render_text(template: str, variables: dict[str, str], *, html_escape: bool = False) -> str:
    def repl(match: re.Match[str]) -> str:
        key = match.group(1)
        raw = variables.get(key, "")
        return _escape(raw) if html_escape else (raw or "—")

    return _PLACEHOLDER_RE.sub(repl, template)


def render_email(template_id: str, variables: dict[str, str]) -> tuple[str, str]:
    spec = get_template(template_id)
    subject = render_text(spec.subject, variables)
    inner = render_text(spec.email_body_html, variables, html_escape=True)
    html_doc = wrap_email_html(
        subject_line=subject,
        hero_title=render_text(spec.hero_title, variables, html_escape=True) if spec.hero_title else None,
        hero_subtitle=render_text(spec.hero_subtitle, variables, html_escape=True) if spec.hero_subtitle else None,
        body_html=inner,
        hero_border_color=spec.hero_border_color,
        hero_bg=spec.hero_bg,
        subheader=spec.email_subheader,
    )
    plain = render_plain(template_id, variables)
    return subject, html_doc if spec.wrap_layout else inner


def render_plain(template_id: str, variables: dict[str, str]) -> str:
    spec = get_template(template_id)
    if spec.plain_body:
        return render_text(spec.plain_body, variables)
    return render_text(spec.whatsapp_text or spec.email_body_html, variables)


def render_whatsapp(template_id: str, variables: dict[str, str]) -> str:
    spec = get_template(template_id)
    if not spec.whatsapp_text:
        return render_plain(template_id, variables)
    return render_text(spec.whatsapp_text, variables)
