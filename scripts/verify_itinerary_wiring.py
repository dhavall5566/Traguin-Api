#!/usr/bin/env python3
"""Verify itinerary API CRUD (nested days/items replace-on-PATCH) and lead→customer link."""

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

    print("=== TEST 1: List itineraries (bootstrap account) ===")
    listed = client.get("/api/crm/itineraries?limit=100", headers=h)
    assert listed.status_code == 200, listed.text
    before_total = listed.json()["total"]
    print(f"  total={before_total}")

    print("\n=== TEST 2: Create itinerary with 2 days, 3 items ===")
    create_body = {
        "title": f"Verify Trip {ts}",
        "description": "API wiring verification",
        "status": "DRAFT",
        "markup_margin": 15,
        "tax_rate": 10,
        "is_template": False,
        "total_price": 0,
        "days": [
            {
                "day_number": 1,
                "title": "Day 1: Arrival",
                "description": "First day",
                "items": [
                    {
                        "type": "TRANSFER",
                        "title": "Airport pickup",
                        "details": "Meet & greet",
                        "cost_price": 3000,
                        "selling_price": 4500,
                        "order": 0,
                    },
                    {
                        "type": "HOTEL",
                        "title": "Check-in",
                        "details": "Luxury hotel",
                        "cost_price": 8000,
                        "selling_price": 12000,
                        "order": 1,
                    },
                ],
            },
            {
                "day_number": 2,
                "title": "Day 2: Explore",
                "description": "Second day",
                "items": [
                    {
                        "type": "ACTIVITY",
                        "title": "City tour",
                        "details": "Guided walk",
                        "cost_price": 2000,
                        "selling_price": 3500,
                        "order": 0,
                    },
                ],
            },
        ],
    }
    created = client.post("/api/crm/itineraries", headers=h, json=create_body)
    assert created.status_code == 201, created.text
    itin = created.json()
    itin_id = itin["id"]
    print(f"  id={itin_id}")
    print(f"  days={len(itin['days'])}")
    print(f"  items_day1={len(itin['days'][0]['items'])} items_day2={len(itin['days'][1]['items'])}")
    assert len(itin["days"]) == 2
    assert len(itin["days"][0]["items"]) == 2
    assert len(itin["days"][1]["items"]) == 1
    assert itin["customer_id"] is None

    print("\n=== TEST 3: PATCH replace — add day, remove item, change pricing ===")
    patch_body = {
        "markup_margin": 20,
        "tax_rate": 12,
        "total_price": 25000,
        "days": [
            {
                "day_number": 1,
                "title": "Day 1: Arrival (updated)",
                "description": "Updated first day",
                "items": [
                    {
                        "type": "TRANSFER",
                        "title": "Airport pickup (updated)",
                        "details": "VIP meet",
                        "cost_price": 3500,
                        "selling_price": 5000,
                        "order": 0,
                    },
                ],
            },
            {
                "day_number": 2,
                "title": "Day 2: Explore",
                "description": "Second day",
                "items": [
                    {
                        "type": "ACTIVITY",
                        "title": "City tour",
                        "details": "Guided walk",
                        "cost_price": 2000,
                        "selling_price": 3500,
                        "order": 0,
                    },
                ],
            },
            {
                "day_number": 3,
                "title": "Day 3: Departure",
                "description": "Final day",
                "items": [
                    {
                        "type": "TRANSFER",
                        "title": "Airport drop",
                        "details": "Checkout transfer",
                        "cost_price": 2500,
                        "selling_price": 4000,
                        "order": 0,
                    },
                ],
            },
        ],
    }
    patched = client.patch(f"/api/crm/itineraries/{itin_id}", headers=h, json=patch_body)
    assert patched.status_code == 200, patched.text
    after = patched.json()
    print(f"  days={len(after['days'])} (expect 3)")
    print(f"  day1_items={len(after['days'][0]['items'])} (expect 1, not 2+1 duplicate)")
    print(f"  markup_margin={after['markup_margin']} tax_rate={after['tax_rate']}")
    assert len(after["days"]) == 3
    assert len(after["days"][0]["items"]) == 1
    assert float(after["markup_margin"]) == 20
    assert float(after["tax_rate"]) == 12
    assert after["days"][0]["title"] == "Day 1: Arrival (updated)"

    print("\n=== TEST 4: Lead → Itinerary customer_id handoff ===")
    lead_email = f"itin.handoff.{ts}@example.com"
    lead_res = client.post(
        "/api/crm/leads",
        headers=h,
        json={
            "title": f"Kashmir Escape {ts}",
            "first_name": "Handoff",
            "last_name": "Test",
            "email": lead_email,
            "status": "NEW",
            "value": 50000,
            "source": "Website",
        },
    )
    assert lead_res.status_code == 201, lead_res.text
    lead = lead_res.json()
    lead_id = lead["id"]
    customer_id = lead.get("customer_id")
    print(f"  lead_id={lead_id}")
    print(f"  customer_id={customer_id}")
    assert customer_id, "Lead missing auto-linked customer_id"

    handoff_create = client.post(
        "/api/crm/itineraries",
        headers=h,
        json={
            "title": f"CRM Handoff Trip {ts}",
            "description": f"From lead {lead_id}",
            "customer_id": customer_id,
            "status": "DRAFT",
            "markup_margin": 15,
            "tax_rate": 10,
            "is_template": False,
            "total_price": 0,
            "days": [
                {
                    "day_number": 1,
                    "title": "Day 1",
                    "description": "Handoff day",
                    "items": [
                        {
                            "type": "ACTIVITY",
                            "title": "Welcome",
                            "details": "Lead-linked trip",
                            "cost_price": 1000,
                            "selling_price": 1500,
                            "order": 0,
                        },
                    ],
                },
            ],
        },
    )
    assert handoff_create.status_code == 201, handoff_create.text
    handoff_itin = handoff_create.json()
    print(f"  itinerary_id={handoff_itin['id']}")
    print(f"  itinerary.customer_id={handoff_itin['customer_id']}")
    assert handoff_itin["customer_id"] == customer_id

    fetched = client.get(f"/api/crm/itineraries/{handoff_itin['id']}", headers=h)
    assert fetched.status_code == 200, fetched.text
    refetched = fetched.json()
    assert refetched["customer_id"] == customer_id
    print("  GET after create: customer_id persisted ✓")

    print("\n=== TEST 5: List count increased ===")
    listed_after = client.get("/api/crm/itineraries?limit=100", headers=h)
    assert listed_after.status_code == 200
    after_total = listed_after.json()["total"]
    print(f"  total before={before_total} after={after_total}")
    assert after_total >= before_total + 2

    print("\nAll API itinerary wiring checks passed.")


if __name__ == "__main__":
    main()
