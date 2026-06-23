#!/usr/bin/env python3
"""End-to-end verification: website forms → CMS submissions → CRM leads."""

from __future__ import annotations

import json
import re
import sys
import time
from datetime import date, timedelta
from pathlib import Path
from uuid import UUID

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient
from sqlalchemy import func, select

from database import SessionLocal
from main import app
from models.crm.customers import Customer
from models.crm.leads import Lead, LeadActivity, LeadNote
from models.submissions import FormSubmission

client = TestClient(app)

TRAGUIN_BASE = "http://127.0.0.1:3001"
CRM_BASE = "http://127.0.0.1:3002"
AGENCY_EMAIL = "admin@traguin-demo.com"
AGENCY_PASSWORD = "Traguin-Demo-2026!"
DEFAULT_AGENCY_ID = UUID("daead252-e21c-4df2-8362-20d25bc523cf")

TEST_TAG = f"e2e-{int(time.time())}"
SHARED_EMAIL = f"{TEST_TAG}-dup@example.com"


def login_crm() -> str:
    r = client.post("/api/crm/auth/login", json={"email": AGENCY_EMAIL, "password": AGENCY_PASSWORD})
    assert r.status_code == 200, r.text
    return r.json()["access_token"]


def auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def count_leads_for_source(source_suffix: str) -> int:
    with SessionLocal() as db:
        return db.scalar(
            select(func.count())
            .select_from(Lead)
            .where(
                Lead.agency_id == DEFAULT_AGENCY_ID,
                Lead.source.like(f"%{source_suffix}%"),
                Lead.is_deleted.is_(False),
            )
        ) or 0


def latest_submission(form_type: str) -> FormSubmission | None:
    with SessionLocal() as db:
        return db.scalar(
            select(FormSubmission)
            .where(FormSubmission.form_type == form_type)
            .order_by(FormSubmission.created_at.desc())
            .limit(1)
        )


def latest_lead_by_email(email: str) -> Lead | None:
    with SessionLocal() as db:
        return db.scalar(
            select(Lead)
            .where(
                Lead.agency_id == DEFAULT_AGENCY_ID,
                Lead.email == email.lower(),
                Lead.is_deleted.is_(False),
            )
            .order_by(Lead.created_at.desc())
            .limit(1)
        )


def assert_lead_artifacts(lead: Lead, *, form_submission_id: UUID) -> None:
    with SessionLocal() as db:
        notes = db.scalars(select(LeadNote).where(LeadNote.lead_id == lead.id)).all()
        activities = db.scalars(select(LeadActivity).where(LeadActivity.lead_id == lead.id)).all()
    assert notes, "LeadNote missing"
    assert any(str(form_submission_id) in n.content for n in notes), notes[0].content[:200]
    assert activities, "LeadActivity missing"
    assert any("Website intake" in a.description for a in activities), activities[0].description


def verify_public_post_no_auth() -> None:
    r = client.post(
        "/api/cms/public/form-submissions",
        json={
            "form_type": "contact_consultation",
            "name": f"{TEST_TAG} API",
            "email": f"{TEST_TAG}-api@example.com",
            "payload": {
                "name": f"{TEST_TAG} API",
                "email": f"{TEST_TAG}-api@example.com",
                "message": "API smoke test without bearer token",
            },
        },
    )
    assert r.status_code == 201, r.text
    body = r.json()
    assert body["form_type"] == "contact_consultation"
    lead = latest_lead_by_email(f"{TEST_TAG}-api@example.com")
    assert lead is not None, "Lead not created from unauthenticated public POST"
    assert lead.source == "Website · contact_consultation"
    assert_lead_artifacts(lead, form_submission_id=UUID(body["id"]))
    print("✓ Public POST creates submission + lead without CRM JWT")


def run_playwright_forms() -> list[str]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("⚠ playwright not installed — skipping UI tests (pip install playwright && playwright install chromium)")
        return ["playwright skipped"]

    console_errors: list[str] = []
    start = date.today() + timedelta(days=30)
    end = start + timedelta(days=7)
    start_iso = start.isoformat()
    end_iso = end.isoformat()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        def on_console(msg):
            if msg.type in ("error", "warning"):
                text = msg.text
                if "favicon" in text.lower() or "404" in text and "favicon" in text.lower():
                    return
                console_errors.append(f"[{msg.type}] {text}")

        page.on("console", on_console)

        # 1 contact_consultation
        page.goto(f"{TRAGUIN_BASE}/contact#consultation", wait_until="domcontentloaded", timeout=60000)
        page.wait_for_selector("#contact-name", timeout=30000)
        page.fill("#contact-name", f"{TEST_TAG} Contact")
        page.fill("#contact-email", f"{TEST_TAG}-contact@example.com")
        page.fill("#contact-phone", "9876543210")
        page.fill("#contact-message", "Looking for a luxury honeymoon consultation please.")
        page.get_by_role("button", name=re.compile("Connect With a Travel Expert", re.I)).click()
        page.get_by_text("Message Sent").wait_for(timeout=15000)
        print("✓ UI contact_consultation")

        # 2 travel_expert_consultation
        page.goto(f"{TRAGUIN_BASE}/travel-expert#consultation", wait_until="domcontentloaded", timeout=60000)
        page.wait_for_selector("#concierge-name", timeout=30000)
        page.fill("#concierge-name", f"{TEST_TAG} Expert")
        page.fill("#concierge-email", f"{TEST_TAG}-expert@example.com")
        page.fill("#concierge-phone", "9876543211")
        page.fill("#concierge-message", "Need visa and concierge support for Europe in August.")
        page.get_by_role("button", name=re.compile("Submit to Travel Expert", re.I)).click()
        page.get_by_text("Request received").wait_for(timeout=15000)
        print("✓ UI travel_expert_consultation")

        # 3 plan_my_journey
        page.goto(f"{TRAGUIN_BASE}/#plan-my-journey", wait_until="domcontentloaded", timeout=60000)
        page.wait_for_selector("#planner-phone", timeout=30000)
        page.fill("#planner-phone", "9876543212")
        page.locator("#plan-my-journey button[type='submit']").click()
        page.get_by_text("Thank you").wait_for(timeout=15000)
        print("✓ UI plan_my_journey")

        # 4 travel_planner
        page.goto(f"{TRAGUIN_BASE}/#planner", wait_until="domcontentloaded", timeout=60000)
        page.wait_for_selector("#planner-destination", timeout=30000)
        page.fill("#planner-destination", "Maldives")
        page.fill("#planner-start-date", start_iso)
        page.fill("#planner-end-date", end_iso)
        page.get_by_role("button", name="Continue").click()
        page.fill("#planner-travelers", "2")
        page.get_by_role("button", name="Continue").click()
        page.fill("#planner-email", f"{TEST_TAG}-planner@example.com")
        page.fill("#planner-phone", "9876543213")
        page.get_by_role("button", name=re.compile("Get Personalized Itinerary", re.I)).click()
        page.get_by_text("Request Received").wait_for(timeout=15000)
        print("✓ UI travel_planner")

        # 5 & 6 itinerary_inquiry duplicate email test — find first itinerary link
        page.goto(f"{TRAGUIN_BASE}/itineraries", wait_until="domcontentloaded", timeout=60000)
        itinerary_link = page.locator("a[href^='/itineraries/']").first
        href = itinerary_link.get_attribute("href")
        assert href, "No itinerary link found"
        page.goto(f"{TRAGUIN_BASE}{href}#inquiry", wait_until="domcontentloaded", timeout=60000)
        page.wait_for_selector("#inquiry-name", timeout=30000)
        for attempt in (1, 2):
            page.fill("#inquiry-name", f"{TEST_TAG} Itinerary {attempt}")
            page.fill("#inquiry-email", SHARED_EMAIL)
            page.fill("#inquiry-phone", "9876543214")
            page.fill("#inquiry-dates", "December 2026")
            page.fill("#inquiry-travelers", "2")
            page.fill("#inquiry-message", f"Itinerary inquiry attempt {attempt} for duplicate customer test.")
            page.get_by_role("button", name=re.compile("Request", re.I)).click()
            page.get_by_text("Inquiry Received").wait_for(timeout=15000)
            if attempt == 1:
                page.reload(wait_until="domcontentloaded")
                page.wait_for_selector("#inquiry-name", timeout=30000)

        with SessionLocal() as db:
            customers = db.scalars(
                select(Customer).where(
                    Customer.agency_id == DEFAULT_AGENCY_ID,
                    Customer.email == SHARED_EMAIL,
                    Customer.is_deleted.is_(False),
                )
            ).all()
        assert len(customers) == 1, f"Expected 1 customer for duplicate email, got {len(customers)}"
        print("✓ UI itinerary_inquiry x2 reuses single Customer")

        # 7 hotel_booking + 8 hotel_review
        page.goto(f"{TRAGUIN_BASE}/hotels", wait_until="domcontentloaded", timeout=60000)
        hotel_href = page.locator("a[href^='/hotels/']").first.get_attribute("href")
        assert hotel_href, "No hotel link found"
        page.goto(f"{TRAGUIN_BASE}{hotel_href}#hotel-booking", wait_until="domcontentloaded", timeout=60000)
        page.wait_for_selector("#hotel-booking-name", timeout=30000)
        page.fill("#hotel-booking-name", f"{TEST_TAG} Hotel")
        page.fill("#hotel-booking-email", f"{TEST_TAG}-hotel@example.com")
        page.fill("#hotel-booking-phone", "9876543215")
        page.fill("#hotel-booking-dates", "Jan 10–15, 2027")
        page.fill("#hotel-booking-travelers", "2")
        page.get_by_role("button", name=re.compile("Submit Booking Request", re.I)).click()
        page.get_by_text("Booking Request Received").wait_for(timeout=15000)
        print("✓ UI hotel_booking")

        review_count_before = count_leads_for_source("hotel_review")
        page.goto(f"{TRAGUIN_BASE}{hotel_href}#hotel-review", wait_until="domcontentloaded", timeout=60000)
        page.wait_for_selector("#hotel-review-name", timeout=30000)
        page.fill("#hotel-review-name", f"{TEST_TAG} Reviewer")
        page.locator("#hotel-review button[aria-label='5 stars']").click()
        page.fill("#hotel-review-text", "An absolutely wonderful stay with impeccable service throughout our visit.")
        page.get_by_role("button", name=re.compile("Submit Review", re.I)).click()
        page.get_by_text("Thank You").wait_for(timeout=15000)
        review_count_after = count_leads_for_source("hotel_review")
        assert review_count_after == review_count_before, "hotel_review must NOT create CRM leads"
        sub = latest_submission("hotel_review")
        assert sub is not None and sub.name == f"{TEST_TAG} Reviewer"
        print("✓ UI hotel_review submission without CRM lead")

        browser.close()

    if console_errors:
        print("Console issues during UI tests:")
        for item in console_errors[:20]:
            print(" ", item)
    else:
        print("✓ No console errors/warnings on form pages")

    return console_errors


def verify_crm_ui_visibility(token: str) -> None:
    r = client.get("/api/crm/leads?limit=100", headers=auth(token))
    assert r.status_code == 200, r.text
    items = r.json()["items"]
    sources = {item["source"] for item in items}
    expected = {
        "Website · contact_consultation",
        "Website · travel_expert_consultation",
        "Website · plan_my_journey",
        "Website · travel_planner",
        "Website · itinerary_inquiry",
        "Website · hotel_booking",
    }
    missing = expected - sources
    assert not missing, f"CRM list missing sources: {missing}\nFound: {sorted(sources)}"
    print("✓ CRM /api/crm/leads shows all website intake sources for bootstrap agency")


def main() -> None:
    print(f"=== Form intake E2E verification ({TEST_TAG}) ===")
    verify_public_post_no_auth()
    ui_errors = run_playwright_forms()
    token = login_crm()
    verify_crm_ui_visibility(token)

    # Spot-check latest travel_planner lead value/title
    sub = latest_submission("travel_planner")
    assert sub is not None
    lead = latest_lead_by_email(f"{TEST_TAG}-planner@example.com")
    assert lead is not None
    assert "Maldives" in lead.title
    assert float(lead.value) == 250000.0
    assert lead.status == "NEW"
    print("✓ travel_planner lead title/value/status")

    if any("error" in e.lower() for e in ui_errors):
        sys.exit(1)

    print("\nAll form intake checks passed.")


if __name__ == "__main__":
    main()
