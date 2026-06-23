#!/usr/bin/env python3
"""Verify Payment creation updates Invoice.status transactionally."""

from __future__ import annotations

import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def login(email: str, password: str) -> str:
    r = client.post("/api/crm/auth/login", json={"email": email, "password": password})
    assert r.status_code == 200, r.text
    return r.json()["access_token"]


def auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def main() -> None:
    ts = int(time.time())
    token = login("admin@traguin-demo.com", "Traguin-Demo-2026!")
    h = auth(token)

    bookings = client.get("/api/crm/bookings?limit=1", headers=h)
    assert bookings.status_code == 200 and bookings.json()["items"], "Need at least one booking"
    booking_id = bookings.json()["items"][0]["id"]

    created = client.post(
        "/api/crm/finance/invoices",
        headers=h,
        json={
            "booking_id": booking_id,
            "invoice_number": f"INV-VERIFY-{ts}",
            "amount": 10000,
            "due_date": (datetime.now(timezone.utc) + timedelta(days=30)).isoformat(),
            "status": "UNPAID",
        },
    )
    assert created.status_code == 201, created.text
    inv = created.json()
    inv_id = inv["id"]
    print(f"=== Invoice created ===")
    print(f"  id={inv_id} status={inv['status']} amount={inv['amount']}")

    partial = client.post(
        "/api/crm/finance/payments",
        headers=h,
        json={
            "invoice_id": inv_id,
            "amount": 4000,
            "payment_method": "BANK_TRANSFER",
            "transaction_reference": f"TXN-PART-{ts}",
        },
    )
    assert partial.status_code == 201, partial.text
    after_partial = client.get(f"/api/crm/finance/invoices/{inv_id}", headers=h).json()
    print(f"\n=== Partial payment (4000) ===")
    print(f"  status BEFORE: UNPAID → AFTER: {after_partial['status']} (expected PARTIALLY_PAID)")
    assert after_partial["status"] == "PARTIALLY_PAID"

    final = client.post(
        "/api/crm/finance/payments",
        headers=h,
        json={
            "invoice_id": inv_id,
            "amount": 6000,
            "payment_method": "UPI",
            "transaction_reference": f"TXN-FULL-{ts}",
        },
    )
    assert final.status_code == 201, final.text
    after_full = client.get(f"/api/crm/finance/invoices/{inv_id}", headers=h).json()
    print(f"\n=== Final payment (6000) ===")
    print(f"  status AFTER: {after_full['status']} (expected PAID)")
    assert after_full["status"] == "PAID"

    print("\nAll payment → invoice status checks passed.")


if __name__ == "__main__":
    main()
