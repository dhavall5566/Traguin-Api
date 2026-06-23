#!/usr/bin/env python3
"""Cross-check Operations SLA categorization against API data."""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)
MS_HOUR = 3_600_000
ACTIVE = {"NEW", "CONTACTED", "PROPOSAL_SENT", "NEGOTIATION"}


def login() -> dict[str, str]:
    r = client.post(
        "/api/crm/auth/login",
        json={"email": "admin@traguin-demo.com", "password": "Traguin-Demo-2026!"},
    )
    assert r.status_code == 200, r.text
    return {"Authorization": f"Bearer {r.json()['access_token']}"}


def last_touch(lead: dict) -> datetime:
    times = [datetime.fromisoformat(lead["created_at"].replace("Z", "+00:00"))]
    for n in lead.get("notes") or []:
        times.append(datetime.fromisoformat(n["created_at"].replace("Z", "+00:00")))
    for a in lead.get("activities") or []:
        times.append(datetime.fromisoformat(a["created_at"].replace("Z", "+00:00")))
    for f in lead.get("followups") or []:
        if f.get("status") == "COMPLETED":
            times.append(datetime.fromisoformat(f["scheduled_at"].replace("Z", "+00:00")))
    return max(times)


def main() -> None:
    h = login()
    now = datetime.now(timezone.utc)
    leads = client.get("/api/crm/leads?limit=100", headers=h).json()["items"]

    stale = []
    for lead in leads:
        if lead["status"] not in ACTIVE:
            continue
        last = last_touch(lead)
        hours = (now - last).total_seconds() / 3600
        if hours >= 24:
            stale.append((lead["title"], lead["status"], int(hours)))

    print("=== Stale leads (>=24h quiet, open pipeline) ===")
    print(f"count={len(stale)}")
    for row in stale[:5]:
        print(f"  {row[0]} | {row[1]} | {row[2]}h quiet")

    stuck = []
    for lead in leads:
        if lead["status"] != "PROPOSAL_SENT":
            continue
        psa = lead.get("proposal_sent_at")
        if not psa:
            print(f"  WARN: PROPOSAL_SENT lead missing proposal_sent_at: {lead['title']}")
            continue
        entered = datetime.fromisoformat(psa.replace("Z", "+00:00"))
        days = (now - entered).days
        if days >= 7:
            stuck.append((lead["title"], days, psa))

    print("\n=== Stuck proposals (>=7d, PROPOSAL_SENT, proposal_sent_at anchor) ===")
    print(f"count={len(stuck)}")
    for row in stuck[:5]:
        print(f"  {row[0]} | {row[1]}d | anchor={row[2]}")

    invs = client.get("/api/crm/finance/invoices?limit=100", headers=h).json()["items"]
    pays = client.get("/api/crm/finance/payments?limit=100", headers=h).json()["items"]
    paid_by_inv = {}
    for p in pays:
        paid_by_inv[p["invoice_id"]] = paid_by_inv.get(p["invoice_id"], 0) + float(p["amount"])

    due_unpaid = [
        inv
        for inv in invs
        if paid_by_inv.get(inv["id"], 0) < float(inv["amount"]) - 0.01
    ]
    print(f"\n=== Unpaid invoices (any due date) ===")
    print(f"count={len(due_unpaid)}")
    for inv in due_unpaid[:5]:
        print(f"  {inv['invoice_number']} due={inv['due_date'][:10]}")


if __name__ == "__main__":
    main()
