#!/usr/bin/env python3
"""Verify vendor payout ledger adjustment via live API (no UI PATCH)."""

from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.request

API = "http://127.0.0.1:8001"
EMAIL = "admin@traguin-demo.com"
PASSWORD = "Traguin-Demo-2026!"


def req(method: str, path: str, token: str | None = None, body: dict | None = None):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(f"{API}{path}", data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(r) as resp:
            raw = resp.read().decode()
            return resp.status, json.loads(raw) if raw else None
    except urllib.error.HTTPError as e:
        raw = e.read().decode()
        return e.code, json.loads(raw) if raw else {"detail": str(e)}


def main() -> None:
    ts = int(time.time())
    _, login = req("POST", "/api/crm/auth/login", body={"email": EMAIL, "password": PASSWORD})
    token = login["access_token"]

    _, vendor = req(
        "POST",
        "/api/crm/vendors",
        token,
        {
            "name": f"Ledger Test Vendor {ts}",
            "type": "SERVICE",
            "email": f"ledger.{ts}@example.com",
            "ledger_balance": 10000,
            "services": [{"type": "HOTEL", "name": "Room", "base_rate": 5000, "rates": []}],
            "packages": [],
        },
    )
    vid = vendor["id"]
    _, got = req("GET", f"/api/crm/vendors/{vid}", token)
    start = float(got["ledger_balance"])
    print(f"=== LIVE API (curl-equivalent) ===")
    print(f"  vendor_id={vid}")
    print(f"  ledger_balance BEFORE payout: {start}")

    status, payout = req(
        "POST",
        "/api/crm/finance/vendor-payouts",
        token,
        {"vendor_id": vid, "amount": 2500, "status": "PAID"},
    )
    print(f"  POST vendor-payouts: {status}")
    assert status == 201, payout

    _, after = req("GET", f"/api/crm/vendors/{vid}", token)
    end = float(after["ledger_balance"])
    expected = max(0, start - 2500)
    print(f"  ledger_balance AFTER payout:  {end} (expected {expected})")
    assert end == expected, f"mismatch: {end} != {expected}"
    print("  PASS: ledger updated by payout POST alone")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"FAILED: {e}", file=sys.stderr)
        sys.exit(1)
