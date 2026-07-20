#!/usr/bin/env python3
"""
Create and verify the Traguin CRM WhatsApp template (traguin_crm_alert).

The template is text-only with 5 body variables mapped to field_1 … field_5:
  {{1}} event title
  {{2}} customer / lead name
  {{3}} detail line
  {{4}} extra notes
  {{5}} CRM link

Run:
  PYTHONPATH=. python scripts/setup_whatsapp_crm_template.py
  PYTHONPATH=. python scripts/setup_whatsapp_crm_template.py --test +919913135371
"""

from __future__ import annotations

import argparse
import json
import sys
import time

import httpx

from config import settings
from services.whatsapp_notifications import build_alert_fields, send_whatsapp_template

TEMPLATE_NAME = "traguin_crm_alert"
TEMPLATE_LANGUAGE = "en"
META_TEMPLATE_ID = "1731511801254622"  # created via Meta Graph API
WABA_ID = "1634309514537224"


def _wm_post(path: str, **fields: str) -> dict:
    base = settings.whatsapp_api_base_url.rstrip("/")
    token = settings.whatsapp_api_url or ""
    phone_number_id = (settings.whatsapp_phone_number_id or "").strip()
    data = {"apiToken": token, "phone_number_id": phone_number_id, **fields}
    response = httpx.post(f"{base}{path}", data=data, timeout=30)
    response.raise_for_status()
    return response.json()


def _meta_token() -> str:
    payload = _wm_post("/api/v1/whatsapp/template/list")
    templates = payload.get("message") or []
    if not templates:
        raise RuntimeError("No WhatsMarketing templates returned — check apiToken and phone_number_id")
    return json.loads(templates[0]["template_json"])["access_token"]


def _meta_template_status(meta_token: str) -> dict:
    response = httpx.get(
        f"https://graph.facebook.com/v21.0/{META_TEMPLATE_ID}",
        params={"fields": "name,status,rejected_reason,category,language"},
        headers={"Authorization": f"Bearer {meta_token}"},
        timeout=20,
    )
    response.raise_for_status()
    return response.json()


def _create_meta_template(meta_token: str) -> dict:
    body = {
        "name": TEMPLATE_NAME,
        "language": TEMPLATE_LANGUAGE,
        "category": "UTILITY",
        "components": [
            {
                "type": "BODY",
                "text": (
                    "Traguin CRM notification for your team.\n\n"
                    "Event: {{1}}\n"
                    "Customer: {{2}}\n"
                    "Details: {{3}}\n"
                    "Notes: {{4}}\n"
                    "Link: {{5}}\n\n"
                    "Please open CRM to take action."
                ),
                "example": {
                    "body_text": [
                        [
                            "New Lead",
                            "Priya Sharma",
                            "TEMP202607120001 · Bali",
                            "Priority: High",
                            "https://crm.traguin.in/dashboard/crm",
                        ]
                    ]
                },
            },
            {"type": "FOOTER", "text": "Traguin — Curated Journeys"},
        ],
    }
    response = httpx.post(
        f"https://graph.facebook.com/v21.0/{WABA_ID}/message_templates",
        headers={"Authorization": f"Bearer {meta_token}", "Content-Type": "application/json"},
        json=body,
        timeout=30,
    )
    if response.status_code >= 400:
        return response.json()
    return response.json()


def _find_wm_template() -> dict | None:
    payload = _wm_post("/api/v1/whatsapp/template/list")
    for row in payload.get("message") or []:
        if row.get("template_name") == TEMPLATE_NAME:
            return row
    return None


def _print_env_hint(wm_row: dict | None) -> None:
    print("\nAdd to api/.env:")
    print(f"WHATSAPP_LEAD_TEMPLATE={TEMPLATE_NAME}")
    print(f"WHATSAPP_LEAD_TEMPLATE_LANGUAGE={TEMPLATE_LANGUAGE}")
    if wm_row:
        print(f"WHATSAPP_TEMPLATE_ID={wm_row['id']}")
    else:
        print("# WHATSAPP_TEMPLATE_ID=<set after Load Template in WhatsMarketing>")


def main() -> int:
    parser = argparse.ArgumentParser(description="Setup Traguin CRM WhatsApp template")
    parser.add_argument("--test", metavar="PHONE", help="Send a test WhatsApp after template is ready")
    parser.add_argument("--create", action="store_true", help="Attempt Meta template creation (already submitted)")
    args = parser.parse_args()

    if not settings.whatsapp_api_url or not settings.whatsapp_phone_number_id:
        print("ERROR: Set WHATSAPP_API_URL and WHATSAPP_PHONE_NUMBER_ID in api/.env")
        return 1

    meta_token = _meta_token()
    status = _meta_template_status(meta_token)
    print(f"Meta template {TEMPLATE_NAME}: {status.get('status')} ({status.get('id', META_TEMPLATE_ID)})")
    if status.get("rejected_reason") and status["rejected_reason"] != "NONE":
        print("Rejected reason:", status["rejected_reason"])

    if args.create and status.get("status") == "NOT_FOUND":
        result = _create_meta_template(meta_token)
        print("Create result:", result)

    wm_row = _find_wm_template()
    if wm_row:
        print(
            f"WhatsMarketing template synced: id={wm_row['id']} "
            f"status={wm_row.get('status')} variables={wm_row.get('variable_map')}"
        )
    else:
        print(
            "WhatsMarketing has not synced this template yet.\n"
            "In WhatsMarketing → Templates → click **Load Template** (sync from Meta), then re-run this script."
        )

    _print_env_hint(wm_row)

    if args.test:
        if status.get("status") != "APPROVED":
            print(f"\nCannot test yet — Meta status is {status.get('status')}")
            return 1
        if not wm_row:
            print("\nCannot test yet — template not visible in WhatsMarketing")
            return 1
        fields = build_alert_fields(
            "Traguin CRM test",
            "Nikunj",
            "Template traguin_crm_alert is working",
            "5-field utility template",
            settings.whatsapp_crm_base_url or "https://www.traguin.in",
        )
        ok = send_whatsapp_template(args.test, fields)
        print("Test send:", "OK" if ok else "FAILED")
        return 0 if ok else 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
