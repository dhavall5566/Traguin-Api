#!/usr/bin/env python3
"""Submit all public website forms to trigger WhatsApp new-lead alerts, then clean up."""

from __future__ import annotations

import sys
import time
from pathlib import Path
from uuid import UUID

import httpx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import delete, select

from database import SessionLocal
from models.crm.customers import Customer
from models.crm.leads import Lead, LeadNote
from models.submissions import FormSubmission
from services.whatsapp_notifications import list_team_notification_phones
from config import settings

API = "http://127.0.0.1:8001"
TAG = f"wa-test-{int(time.time())}"
TEST_EMAIL = f"{TAG}@example.com"
TEST_PHONE = "+919876543210"


def lead_for_submission(db, submission_id: UUID) -> Lead | None:
    needle = str(submission_id)
    note = db.scalar(select(LeadNote).where(LeadNote.content.contains(needle)).limit(1))
    if note is None:
        return None
    return db.get(Lead, note.lead_id)


def submit(client: httpx.Client, form_type: str, body: dict) -> dict:
    r = client.post(f"{API}/api/cms/public/form-submissions", json=body, timeout=60)
    print(f"  POST {form_type}: HTTP {r.status_code}")
    if r.status_code >= 400:
        print(f"    body: {r.text[:500]}")
        r.raise_for_status()
    data = r.json()
    print(f"    submission_id={data.get('id')} lead_id={data.get('lead_id')}")
    return data


def main() -> None:
    print(f"WhatsApp form test TAG={TAG}")
    print(f"Notifications will go to team phones on agency {settings.traguin_default_agency_id}")

    with SessionLocal() as db:
        phones = list_team_notification_phones(db, settings.traguin_default_agency_id)
        print(f"Team notification phones: {phones}")
        if "+919913135371" not in phones:
            print("WARNING: Nick (+919913135371) not in notification list")

    from sqlalchemy import select as sa_select
    from models.itineraries import Itinerary

    with SessionLocal() as db:
        it = db.scalar(sa_select(Itinerary).limit(1))
        itinerary_id = str(it.id) if it else None
        itinerary_title = it.title if it else "Test Itinerary"
        itinerary_slug = it.slug if it else "test-itinerary"

    submission_ids: list[UUID] = []
    lead_ids: list[UUID] = []

    with httpx.Client() as client:
        forms = [
            (
                "contact_consultation",
                {
                    "form_type": "contact_consultation",
                    "name": f"{TAG} Contact",
                    "email": TEST_EMAIL,
                    "phone": TEST_PHONE,
                    "payload": {
                        "name": f"{TAG} Contact",
                        "email": TEST_EMAIL,
                        "phone": TEST_PHONE,
                        "message": f"{TAG} contact form WhatsApp test",
                    },
                },
            ),
            (
                "travel_expert_consultation",
                {
                    "form_type": "travel_expert_consultation",
                    "name": f"{TAG} Expert",
                    "email": TEST_EMAIL,
                    "phone": TEST_PHONE,
                    "payload": {
                        "name": f"{TAG} Expert",
                        "email": TEST_EMAIL,
                        "phone": TEST_PHONE,
                        "service": "Bespoke Journeys",
                        "message": f"{TAG} travel expert consultation test",
                    },
                },
            ),
            (
                "plan_my_journey",
                {
                    "form_type": "plan_my_journey",
                    "name": f"{TAG} Journey",
                    "email": TEST_EMAIL,
                    "phone": TEST_PHONE,
                    "related_itinerary_id": itinerary_id,
                    "payload": {
                        "name": f"{TAG} Journey",
                        "email": TEST_EMAIL,
                        "phone": TEST_PHONE,
                        "destination": "Goa",
                        "start_date": "2026-08-01",
                        "end_date": "2026-08-07",
                        "rooms": 1,
                        "adults": 2,
                        "children": 0,
                        "child_ages": [],
                        "traveling_with_pets": False,
                        "budget": "200000",
                        "notes": f"{TAG} plan my journey test",
                        "itinerary_slug": itinerary_slug,
                        "itinerary_title": itinerary_title,
                    },
                },
            ),
            (
                "travel_planner",
                {
                    "form_type": "travel_planner",
                    "email": TEST_EMAIL,
                    "phone": TEST_PHONE,
                    "payload": {
                        "destination": "Kerala",
                        "start_date": "2026-09-01",
                        "end_date": "2026-09-08",
                        "travelers": 2,
                        "budget": 500000,
                        "style": "luxury",
                        "notes": f"{TAG} travel planner test",
                        "email": TEST_EMAIL,
                        "phone": TEST_PHONE,
                    },
                },
            ),
            (
                "itinerary_inquiry",
                {
                    "form_type": "itinerary_inquiry",
                    "name": f"{TAG} Inquiry",
                    "email": TEST_EMAIL,
                    "phone": TEST_PHONE,
                    "related_itinerary_id": itinerary_id,
                    "payload": {
                        "name": f"{TAG} Inquiry",
                        "email": TEST_EMAIL,
                        "phone": TEST_PHONE,
                        "travelers": 2,
                        "dates": "October 2026",
                        "message": f"{TAG} itinerary inquiry test",
                        "itinerary_slug": itinerary_slug,
                        "itinerary_title": itinerary_title,
                    },
                },
            ),
            (
                "hotel_booking",
                {
                    "form_type": "hotel_booking",
                    "name": f"{TAG} Hotel",
                    "email": TEST_EMAIL,
                    "phone": TEST_PHONE,
                    "payload": {
                        "name": f"{TAG} Hotel",
                        "email": TEST_EMAIL,
                        "phone": TEST_PHONE,
                        "travelers": 2,
                        "dates": "November 2026",
                        "message": f"{TAG} hotel booking test",
                        "hotel_name": "Test Luxury Hotel",
                    },
                },
            ),
            (
                "hotel_review",
                {
                    "form_type": "hotel_review",
                    "name": f"{TAG} Reviewer",
                    "payload": {
                        "name": f"{TAG} Reviewer",
                        "rating": 5,
                        "review": f"{TAG} excellent stay — WhatsApp test only, no lead expected.",
                        "hotel_name": "Test Hotel",
                    },
                },
            ),
        ]

        for form_type, body in forms:
            print(f"\n→ {form_type}")
            data = submit(client, form_type, body)
            submission_ids.append(UUID(data["id"]))
            if data.get("lead_id"):
                lead_ids.append(UUID(data["lead_id"]))
            if form_type != "plan_my_journey":
                time.sleep(3)

    print("\nWaiting 30s for background intake + WhatsApp delivery before cleanup…")
    time.sleep(30)

    with SessionLocal() as db:
        for sub_id in submission_ids:
            lead = lead_for_submission(db, sub_id)
            sub = db.get(FormSubmission, sub_id)
            print(
                f"  {sub.form_type if sub else '?'}: submission={sub_id} "
                f"lead={lead.id if lead else None}"
            )
            if lead and lead.id not in lead_ids:
                lead_ids.append(lead.id)

    print(f"\nSubmitted {len(submission_ids)} forms; {len(lead_ids)} leads should have triggered WhatsApp.")
    print("Check Nick's WhatsApp (+919913135371) for new_lead_alert messages.")
    print("\nCleaning up test data…")

    with SessionLocal() as db:
        for lead_id in lead_ids:
            lead = db.get(Lead, lead_id)
            if lead:
                db.delete(lead)

        db.execute(delete(FormSubmission).where(FormSubmission.id.in_(submission_ids)))

        customers = db.scalars(
            select(Customer).where(Customer.email == TEST_EMAIL, Customer.is_deleted.is_(False))
        ).all()
        for customer in customers:
            remaining = db.scalar(
                select(Lead).where(Lead.customer_id == customer.id, Lead.is_deleted.is_(False))
            )
            if remaining is None:
                customer.is_deleted = True

        db.commit()

    print(f"Deleted {len(lead_ids)} test leads and {len(submission_ids)} form submissions.")
    print(f"Soft-deleted test customers for {TEST_EMAIL} (if unused).")
    print("Done.")


if __name__ == "__main__":
    main()
