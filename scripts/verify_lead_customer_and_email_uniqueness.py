#!/usr/bin/env python3
"""Verify lead→customer auto-link and per-agency email uniqueness."""

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
    new_email = f"autolink.verify.{ts}@example.com"
    shared_email = f"shared.cross.{ts}@example.com"

    token_a = login("admin@traguin-demo.com", "Traguin-Demo-2026!")
    token_b = login("admin-b@traguin-demo.com", "Traguin-Demo-B-2026!")

    print("=== TEST 1: Lead auto-link (new email) ===")
    r1 = client.post(
        "/api/crm/leads",
        headers=auth(token_a),
        json={
            "title": "AutoLink Verify",
            "first_name": "Auto",
            "last_name": "Link",
            "email": new_email,
            "status": "NEW",
            "value": 0,
            "source": "Website",
        },
    )
    assert r1.status_code == 201, r1.text
    lead1 = r1.json()
    cust1_id = lead1.get("customer_id")
    print(f"  lead_id={lead1['id']}")
    print(f"  customer_id={cust1_id}")
    print(f"  activities={[a['description'] for a in lead1.get('activities', [])]}")
    assert cust1_id, "Lead missing customer_id"

    customers = client.get("/api/crm/customers?limit=100", headers=auth(token_a))
    assert customers.status_code == 200, customers.text
    match = [c for c in customers.json()["items"] if c["email"] == new_email]
    assert len(match) == 1, f"Expected 1 customer, got {len(match)}"
    assert match[0]["id"] == cust1_id
    assert match[0]["first_name"] == "Auto"
    print(f"  customer in DB: {match[0]['id']} {match[0]['first_name']} {match[0]['last_name']}")

    print("\n=== TEST 2: Second lead reuses customer ===")
    before = customers.json()["total"]
    r2 = client.post(
        "/api/crm/leads",
        headers=auth(token_a),
        json={
            "title": "AutoLink Reuse",
            "first_name": "Other",
            "last_name": "Lead",
            "email": new_email,
            "status": "NEW",
            "value": 0,
            "source": "Referral",
        },
    )
    assert r2.status_code == 201, r2.text
    cust2_id = r2.json().get("customer_id")
    after = client.get("/api/crm/customers?limit=100", headers=auth(token_a)).json()["total"]
    print(f"  lead2 customer_id={cust2_id}")
    print(f"  reused={cust1_id == cust2_id} customer_count before={before} after={after}")
    assert cust1_id == cust2_id
    assert before == after

    print("\n=== TEST 3: Cross-agency same email ===")
    ca = client.post(
        "/api/crm/customers",
        headers=auth(token_a),
        json={"first_name": "Shared", "last_name": "AgencyA", "email": shared_email},
    )
    print(f"  Agency A create: HTTP {ca.status_code} id={ca.json().get('id') if ca.status_code == 201 else ca.text}")
    assert ca.status_code == 201

    cb = client.post(
        "/api/crm/customers",
        headers=auth(token_b),
        json={"first_name": "Shared", "last_name": "AgencyB", "email": shared_email},
    )
    print(f"  Agency B create: HTTP {cb.status_code} id={cb.json().get('id') if cb.status_code == 201 else cb.text}")
    assert cb.status_code == 201
    assert ca.json()["id"] != cb.json()["id"]

    dup = client.post(
        "/api/crm/customers",
        headers=auth(token_a),
        json={"first_name": "Dup", "last_name": "AgencyA", "email": shared_email},
    )
    print(f"  Agency A duplicate: HTTP {dup.status_code} detail={dup.json().get('detail')}")
    assert dup.status_code == 409
    assert "your agency" in dup.json()["detail"].lower()

    print("\nAll verification checks passed.")


if __name__ == "__main__":
    main()
