#!/usr/bin/env python3
"""Verify vendor API CRUD, nested replace, and delete 409."""

from __future__ import annotations

import sys
import time
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

    print("=== TEST 1: Create vendor with service + rate ===")
    created = client.post(
        "/api/crm/vendors",
        headers=h,
        json={
            "name": f"Verify Vendor {ts}",
            "type": "SERVICE",
            "email": f"vendor.{ts}@example.com",
            "services": [
                {
                    "type": "HOTEL",
                    "name": "Deluxe Room",
                    "base_rate": 7500,
                    "rates": [],
                }
            ],
            "packages": [],
        },
    )
    assert created.status_code == 201, created.text
    vendor = created.json()
    vid = vendor["id"]
    print(f"  id={vid} services={len(vendor['services'])}")

    print("\n=== TEST 2: PATCH replace services (add + remove) ===")
    patched = client.patch(
        f"/api/crm/vendors/{vid}",
        headers=h,
        json={
            "services": [
                {
                    "type": "HOTEL",
                    "name": "Deluxe Room Updated",
                    "base_rate": 8200,
                    "rates": [],
                },
                {
                    "type": "ACTIVITY",
                    "name": "City Tour",
                    "base_rate": 3500,
                    "rates": [],
                },
            ],
        },
    )
    assert patched.status_code == 200, patched.text
    after = patched.json()
    print(f"  services={len(after['services'])} names={[s['name'] for s in after['services']]}")

    print("\n=== TEST 3: Payout auto-adjusts ledger (no separate PATCH) ===")
    client.patch(
        f"/api/crm/vendors/{vid}",
        headers=h,
        json={"ledger_balance": 5000},
    )
    before = client.get(f"/api/crm/vendors/{vid}", headers=h).json()
    start_balance = float(before["ledger_balance"])
    print(f"  ledger_balance before payout: {start_balance}")
    payout = client.post(
        "/api/crm/finance/vendor-payouts",
        headers=h,
        json={"vendor_id": vid, "amount": 1500, "status": "PAID"},
    )
    assert payout.status_code == 201, payout.text
    after_payout = client.get(f"/api/crm/vendors/{vid}", headers=h).json()
    end_balance = float(after_payout["ledger_balance"])
    expected = max(0, start_balance - 1500)
    print(f"  ledger_balance after payout:  {end_balance} (expected {expected})")
    assert end_balance == expected, f"ledger not adjusted: {end_balance} != {expected}"

    print("\n=== TEST 4: Delete vendor with payout → 409 ===")
    deleted = client.delete(f"/api/crm/vendors/{vid}", headers=h)
    print(f"  delete status={deleted.status_code} detail={deleted.json().get('detail')}")
    assert deleted.status_code == 409
    assert "Cannot delete vendor" in deleted.json()["detail"]

    print("\nAll vendor API checks passed.")


if __name__ == "__main__":
    main()
