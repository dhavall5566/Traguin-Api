"""Airline-style HTML email shell for Traguin notifications."""

from __future__ import annotations

import html

BRAND = "#0B3D6E"
BRAND_LIGHT = "#1E6BB8"
GOLD = "#C9A227"
MUTED = "#5a6b7d"
TEXT = "#1a2b3c"


def wrap_email_html(
    *,
    subject_line: str,
    hero_title: str | None = None,
    hero_subtitle: str | None = None,
    body_html: str,
    hero_border_color: str = GOLD,
    hero_bg: str | None = None,
    subheader: str = "Curated Journeys · Seamless Experiences",
) -> str:
    hero_block = ""
    if hero_title:
        bg_style = f"background:{hero_bg};" if hero_bg else ""
        hero_block = f"""
        <tr>
          <td style="padding:24px 24px 20px;text-align:center;border-bottom:3px solid {hero_border_color};{bg_style}">
            <h1 style="margin:0 0 6px;font-size:20px;line-height:1.3;color:{BRAND};font-family:Segoe UI,system-ui,sans-serif;">{hero_title}</h1>
            {f'<p style="margin:0;font-size:14px;color:{MUTED};font-family:Segoe UI,system-ui,sans-serif;">{hero_subtitle}</p>' if hero_subtitle else ''}
          </td>
        </tr>"""

    safe_subject = html.escape(subject_line, quote=True)
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;padding:0;background:#eef2f7;font-family:Segoe UI,system-ui,sans-serif;color:{TEXT};">
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#eef2f7;padding:24px 12px;">
    <tr><td align="center">
      <table role="presentation" width="600" cellspacing="0" cellpadding="0" style="max-width:600px;width:100%;background:#fff;border:1px solid #d8e2ec;border-radius:12px;overflow:hidden;">
        <tr>
          <td style="background:{BRAND};color:#fff;padding:20px 24px;text-align:center;">
            <div style="font-size:24px;font-weight:800;letter-spacing:0.12em;">TRAGUIN</div>
            <div style="font-size:12px;opacity:0.9;margin-top:4px;">{html.escape(subheader, quote=True)}</div>
          </td>
        </tr>
        {hero_block}
        <tr>
          <td style="padding:20px 24px 8px;font-size:12px;color:{MUTED};">
            Subject: <strong style="color:{TEXT};">{safe_subject}</strong>
          </td>
        </tr>
        <tr>
          <td style="padding:8px 24px 24px;font-size:14px;line-height:1.55;color:{TEXT};">
            {body_html}
          </td>
        </tr>
        <tr>
          <td style="background:#f1f5f9;padding:16px 24px;text-align:center;font-size:11px;color:{MUTED};border-top:1px solid #d8e2ec;">
            Traguin Travel · Mumbai HQ · <a href="https://www.traguin.com" style="color:{BRAND_LIGHT};">www.traguin.com</a><br>
            © 2026 Traguin. All rights reserved.
          </td>
        </tr>
      </table>
    </td></tr>
  </table>
</body>
</html>"""


def ref_card(label: str, value: str, *, border_color: str = BRAND_LIGHT, extra: str = "") -> str:
    extra_html = (
        f'<div style="font-size:12px;color:{MUTED};margin-top:4px;">{html.escape(extra, quote=True)}</div>'
        if extra
        else ""
    )
    return f"""
<div style="background:linear-gradient(135deg,#f0f6fc,#fff);border:1px solid #d8e2ec;border-left:4px solid {border_color};border-radius:8px;padding:14px 16px;margin:12px 0;">
  <div style="font-size:11px;color:{MUTED};text-transform:uppercase;letter-spacing:0.06em;">{html.escape(label, quote=True)}</div>
  <div style="font-size:18px;font-weight:700;color:{BRAND};letter-spacing:0.04em;margin-top:4px;">{html.escape(value, quote=True)}</div>
  {extra_html}
</div>"""


def detail_grid(rows: list[tuple[str, str]]) -> str:
    cells = []
    for label, value in rows:
        cells.append(
            f"""
            <td style="width:50%;padding:6px 8px 6px 0;vertical-align:top;">
              <div style="font-size:11px;color:{MUTED};text-transform:uppercase;">{html.escape(label, quote=True)}</div>
              <div style="font-size:13px;font-weight:600;color:{TEXT};">{html.escape(value or '—', quote=True)}</div>
            </td>"""
        )
    # pair into rows
    html_rows = []
    for i in range(0, len(cells), 2):
        pair = cells[i : i + 2]
        if len(pair) == 1:
            pair.append('<td style="width:50%;"></td>')
        html_rows.append(f"<tr>{''.join(pair)}</tr>")
    return f'<table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="margin:12px 0;">{"".join(html_rows)}</table>'


def note_box(text: str, *, variant: str = "info") -> str:
    styles = {
        "info": ("#eff6ff", "#93c5fd", "#1e40af"),
        "warn": ("#fffbeb", "#fde68a", "#78350f"),
        "urgent": ("#fef2f2", "#fecaca", "#991b1b"),
    }
    bg, border, color = styles.get(variant, styles["info"])
    return f'<div style="background:{bg};border:1px solid {border};border-radius:6px;padding:12px;margin:12px 0;font-size:13px;color:{color};">{text}</div>'


def cta_button(label: str, href: str, *, variant: str = "primary") -> str:
    colors = {
        "primary": (BRAND_LIGHT, "#fff"),
        "gold": (GOLD, BRAND),
        "danger": ("#b91c1c", "#fff"),
        "outline": ("#fff", BRAND),
    }
    bg, fg = colors.get(variant, colors["primary"])
    border = f"2px solid {BRAND}" if variant == "outline" else "none"
    safe_href = html.escape(href, quote=True)
    safe_label = html.escape(label, quote=True)
    return f"""
<div style="text-align:center;margin:16px 0;">
  <a href="{safe_href}" style="display:inline-block;background:{bg};color:{fg} !important;text-decoration:none;padding:10px 22px;border-radius:6px;font-weight:600;font-size:14px;border:{border};">{safe_label}</a>
</div>"""


def button_pair(accept_href: str, reject_href: str) -> str:
    return f"""
<div style="text-align:center;margin:16px 0;">
  <a href="{html.escape(accept_href, quote=True)}" style="display:inline-block;background:#0d7a4e;color:#fff;text-decoration:none;padding:10px 20px;border-radius:6px;font-weight:600;font-size:14px;margin:4px 6px;">✓ Accept Lead</a>
  <a href="{html.escape(reject_href, quote=True)}" style="display:inline-block;background:#fff;color:#b91c1c;text-decoration:none;padding:9px 18px;border-radius:6px;font-weight:600;font-size:14px;border:2px solid #b91c1c;margin:4px 6px;">✕ Reject Lead</a>
</div>"""
