#!/usr/bin/env python3
"""Verify CRM audit logging on create/update/delete across entity types."""

from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

AGENCY_A_EMAIL = "admin@traguin-demo.com"
AGENCY_A_PASSWORD = "Traguin-Demo-2026!"
AGENCY_B_EMAIL = "admin-b@traguin-demo.com"
AGENCY_B_PASSWORD = "Traguin-Demo-B-2026!"


def login(email: str, password: str) -> tuple[str, dict]:
    r = client.post("/api/crm/auth/login", json={"email": email, "password": password})
    assert r.status_code == 200, r.text
    body = r.json()
    return body["access_token"], body


def auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def audit_count(token: str) -> int:
    r = client.get("/api/crm/audit-logs?limit=100", headers=auth(token))
    assert r.status_code == 200, r.text
    return r.json()["total"]


def latest_logs(token: str, *, limit: int = 20) -> list[dict]:
    r = client.get(f"/api/crm/audit-logs?limit={limit}", headers=auth(token))
    assert r.status_code == 200, r.text
    return r.json()["items"]


def assert_log(
    logs: list[dict],
    *,
    action: str,
    entity_type: str,
    entity_id: str,
    user_id: str,
    agency_id: str,
    details_contains: str,
) -> dict:
    match = next(
        (
            e
            for e in logs
            if e["action"] == action
            and e["entity_type"] == entity_type
            and e["entity_id"] == entity_id
        ),
        None,
    )
    assert match is not None, (
        f"Missing audit entry action={action} entity_type={entity_type} entity_id={entity_id}\n"
        f"Recent logs:\n{json.dumps(logs[:10], indent=2)}"
    )
    assert match["user_id"] == user_id, match
    assert match["agency_id"] == agency_id, match
    assert details_contains in (match.get("details") or ""), match
    return match


def session(token: str) -> dict:
    r = client.get("/api/crm/auth/me", headers=auth(token))
    assert r.status_code == 200, r.text
    return r.json()


def main() -> None:
    ts = int(time.time())
    token_a = login(AGENCY_A_EMAIL, AGENCY_A_PASSWORD)[0]
    h = auth(token_a)
    me = session(token_a)
    user_id = me["user"]["id"]
    agency_id = me["user"]["agency_id"]

    before_a = audit_count(token_a)
    print(f"=== BEFORE: Agency A audit log count = {before_a} ===")

    print("\n=== LEAD: create / update / delete ===")
    lead = client.post(
        "/api/crm/leads",
        headers=h,
        json={
            "title": f"Audit Lead {ts}",
            "first_name": "Audit",
            "last_name": "Tester",
            "email": f"audit.lead.{ts}@example.com",
            "status": "NEW",
            "value": 5000,
        },
    )
    assert lead.status_code == 201, lead.text
    lead_id = lead.json()["id"]

    lead_patch = client.patch(
        f"/api/crm/leads/{lead_id}",
        headers=h,
        json={"status": "CONTACTED", "value": 7500},
    )
    assert lead_patch.status_code == 200, lead_patch.text

    lead_del = client.delete(f"/api/crm/leads/{lead_id}", headers=h)
    assert lead_del.status_code == 204, lead_del.text

    print("\n=== VENDOR: create / update / delete ===")
    vendor = client.post(
        "/api/crm/vendors",
        headers=h,
        json={
            "name": f"Audit Vendor {ts}",
            "type": "SERVICE",
            "email": f"audit.vendor.{ts}@example.com",
            "services": [],
            "packages": [],
        },
    )
    assert vendor.status_code == 201, vendor.text
    vendor_id = vendor.json()["id"]

    vendor_patch = client.patch(
        f"/api/crm/vendors/{vendor_id}",
        headers=h,
        json={"name": f"Audit Vendor Updated {ts}"},
    )
    assert vendor_patch.status_code == 200, vendor_patch.text

    vendor_del = client.delete(f"/api/crm/vendors/{vendor_id}", headers=h)
    assert vendor_del.status_code == 204, vendor_del.text

    print("\n=== INVOICE: create / update / delete ===")
    bookings = client.get("/api/crm/bookings?limit=1", headers=h)
    assert bookings.status_code == 200 and bookings.json()["items"], "Need at least one booking"
    booking_id = bookings.json()["items"][0]["id"]

    invoice = client.post(
        "/api/crm/finance/invoices",
        headers=h,
        json={
            "booking_id": booking_id,
            "invoice_number": f"AUD-INV-{ts}",
            "amount": 12000,
            "due_date": (datetime.now(timezone.utc) + timedelta(days=14)).isoformat(),
            "status": "UNPAID",
        },
    )
    assert invoice.status_code == 201, invoice.text
    invoice_id = invoice.json()["id"]

    invoice_patch = client.patch(
        f"/api/crm/finance/invoices/{invoice_id}",
        headers=h,
        json={"amount": 15000},
    )
    assert invoice_patch.status_code == 200, invoice_patch.text

    invoice_del = client.delete(f"/api/crm/finance/invoices/{invoice_id}", headers=h)
    assert invoice_del.status_code == 204, invoice_del.text

    after_a = audit_count(token_a)
    print(f"\n=== AFTER: Agency A audit log count = {after_a} (delta +{after_a - before_a}) ===")
    assert after_a >= before_a + 9, f"Expected at least 9 new entries, got {after_a - before_a}"

    logs = latest_logs(token_a, limit=50)
    print("\n=== Sample recent audit entries (Agency A) ===")
    for entry in logs[:12]:
        print(
            f"  {entry['action']:6} {entry['entity_type']:12} "
            f"{entry['entity_id'][:8]}… user={entry['user_id'][:8]}… "
            f"details={entry.get('details', '')[:80]}"
        )

    assert_log(
        logs,
        action="CREATE",
        entity_type="Lead",
        entity_id=lead_id,
        user_id=user_id,
        agency_id=agency_id,
        details_contains=f'Audit Lead {ts}',
    )
    assert_log(
        logs,
        action="UPDATE",
        entity_type="Lead",
        entity_id=lead_id,
        user_id=user_id,
        agency_id=agency_id,
        details_contains="status",
    )
    assert_log(
        logs,
        action="DELETE",
        entity_type="Lead",
        entity_id=lead_id,
        user_id=user_id,
        agency_id=agency_id,
        details_contains=f'Audit Lead {ts}',
    )
    assert_log(
        logs,
        action="CREATE",
        entity_type="Vendor",
        entity_id=vendor_id,
        user_id=user_id,
        agency_id=agency_id,
        details_contains=f"Audit Vendor {ts}",
    )
    assert_log(
        logs,
        action="CREATE",
        entity_type="Invoice",
        entity_id=invoice_id,
        user_id=user_id,
        agency_id=agency_id,
        details_contains=f"AUD-INV-{ts}",
    )

    print("\n=== Tenant isolation: Agency B should not see Agency A entries ===")
    token_b = login(AGENCY_B_EMAIL, AGENCY_B_PASSWORD)[0]
    me_b = session(token_b)
    agency_b_id = me_b["user"]["agency_id"]
    assert agency_b_id != agency_id

    logs_b = latest_logs(token_b, limit=100)
    leaked = [
        e
        for e in logs_b
        if e["entity_id"] in {lead_id, vendor_id, invoice_id}
    ]
    assert not leaked, f"Agency B saw Agency A audit entries: {leaked}"

    for entry in logs_b[:5]:
        assert entry["agency_id"] == agency_b_id, entry

    print("  No cross-tenant leakage for test entity IDs.")
    print(f"  Agency B sample count (total field from API): {audit_count(token_b)}")

    print("\nAll audit logging checks passed.")


if __name__ == "__main__":
    main()
