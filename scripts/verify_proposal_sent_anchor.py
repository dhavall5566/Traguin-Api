#!/usr/bin/env python3
"""Verify proposal_sent_at is set for UI and direct API status transitions."""

from __future__ import annotations

import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient

from main import app
from services.lead_status import ENTERED_PROPOSAL_SENT_ACTIVITY

client = TestClient(app)


def login() -> tuple[str, dict[str, str]]:
    r = client.post(
        "/api/crm/auth/login",
        json={"email": "admin@traguin-demo.com", "password": "Traguin-Demo-2026!"},
    )
    assert r.status_code == 200, r.text
    token = r.json()["access_token"]
    return token, {"Authorization": f"Bearer {token}"}


def main() -> None:
    ts = int(time.time())
    _, h = login()
    before = datetime.now(timezone.utc)

    print("=== UI-style: status + STAGE_CHANGE append_activities ===")
    ui_lead = client.post(
        "/api/crm/leads",
        headers=h,
        json={
            "title": f"UI Proposal Anchor {ts}",
            "first_name": "UI",
            "last_name": "Anchor",
            "email": f"ui.anchor.{ts}@example.com",
            "status": "NEW",
        },
    )
    assert ui_lead.status_code == 201, ui_lead.text
    ui_id = ui_lead.json()["id"]

    ui_patch = client.patch(
        f"/api/crm/leads/{ui_id}",
        headers=h,
        json={
            "status": "PROPOSAL_SENT",
            "append_activities": [
                {
                    "type": "STAGE_CHANGE",
                    "description": "Moved stage from NEW to PROPOSAL_SENT",
                }
            ],
        },
    )
    assert ui_patch.status_code == 200, ui_patch.text
    ui_body = ui_patch.json()
    assert ui_body["proposal_sent_at"] is not None, ui_body
    ui_psa = datetime.fromisoformat(ui_body["proposal_sent_at"].replace("Z", "+00:00"))
    assert ui_psa >= before
    ui_marker = [a for a in ui_body["activities"] if a["type"] == ENTERED_PROPOSAL_SENT_ACTIVITY]
    assert len(ui_marker) == 1, ui_body["activities"]
    print(f"  proposal_sent_at={ui_body['proposal_sent_at']}")
    print(f"  ENTERED_PROPOSAL_SENT activity id={ui_marker[0]['id']}")

    print("\n=== Direct API: status only (no append_activities) ===")
    api_lead = client.post(
        "/api/crm/leads",
        headers=h,
        json={
            "title": f"API Proposal Anchor {ts}",
            "first_name": "API",
            "last_name": "Anchor",
            "email": f"api.anchor.{ts}@example.com",
            "status": "CONTACTED",
        },
    )
    assert api_lead.status_code == 201, api_lead.text
    api_id = api_lead.json()["id"]

    api_patch = client.patch(
        f"/api/crm/leads/{api_id}",
        headers=h,
        json={"status": "PROPOSAL_SENT"},
    )
    assert api_patch.status_code == 200, api_patch.text
    api_body = api_patch.json()
    assert api_body["proposal_sent_at"] is not None, api_body
    api_psa = datetime.fromisoformat(api_body["proposal_sent_at"].replace("Z", "+00:00"))
    assert api_psa >= before
    api_marker = [a for a in api_body["activities"] if a["type"] == ENTERED_PROPOSAL_SENT_ACTIVITY]
    assert len(api_marker) == 1, api_body["activities"]
    print(f"  proposal_sent_at={api_body['proposal_sent_at']}")
    print(f"  ENTERED_PROPOSAL_SENT activity id={api_marker[0]['id']}")

    print("\n=== Create with initial PROPOSAL_SENT ===")
    create_ps = client.post(
        "/api/crm/leads",
        headers=h,
        json={
            "title": f"Born Proposal {ts}",
            "first_name": "Born",
            "last_name": "Proposal",
            "email": f"born.proposal.{ts}@example.com",
            "status": "PROPOSAL_SENT",
        },
    )
    assert create_ps.status_code == 201, create_ps.text
    born = create_ps.json()
    assert born["proposal_sent_at"] is not None
    print(f"  proposal_sent_at={born['proposal_sent_at']}")

    print("\nAll proposal_sent_at checks passed.")


if __name__ == "__main__":
    main()
