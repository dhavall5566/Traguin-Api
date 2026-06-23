#!/usr/bin/env python3
"""Light E2E verification: one UI submit + API/DB checks."""

from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path
from uuid import UUID

import httpx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient
from sqlalchemy import select

from database import SessionLocal
from main import app
from models.crm.customers import Customer
from models.crm.leads import Lead, LeadActivity, LeadNote
from models.crm.tenancy import User
from models.submissions import FormSubmission

API = "http://127.0.0.1:8001"
TRAGUIN = "http://localhost:3001"
AGENCY_EMAIL = "admin@traguin-demo.com"
AGENCY_PASSWORD = "Traguin-Demo-2026!"

TAG = f"light-{int(time.time())}"
UI_EMAIL = f"{TAG}-ui@example.com"
DUP_EMAIL = f"{TAG}-dup@example.com"

ui_post_headers: dict | None = None
ui_submission_id: UUID | None = None


def sep(n: int, title: str) -> None:
    print(f"\n{'=' * 60}\n[{n}] {title}\n{'=' * 60}")


def lead_for_submission(submission_id: UUID) -> Lead | None:
    needle = str(submission_id)
    with SessionLocal() as db:
        note = db.scalar(select(LeadNote).where(LeadNote.content.contains(needle)).limit(1))
        if note is None:
            return None
        return db.get(Lead, note.lead_id)


def report_submission_lead(submission_id: UUID, label: str) -> tuple[FormSubmission, Lead]:
    with SessionLocal() as db:
        sub = db.get(FormSubmission, submission_id)
        if sub is None:
            raise AssertionError(f"No submission {submission_id}")
        lead = lead_for_submission(submission_id)
        if lead is None:
            raise AssertionError(f"No lead for submission {submission_id}")
        customer = db.get(Customer, lead.customer_id) if lead.customer_id else None
        notes = db.scalars(select(LeadNote).where(LeadNote.lead_id == lead.id)).all()
        activities = db.scalars(select(LeadActivity).where(LeadActivity.lead_id == lead.id)).all()
        creator = db.get(User, notes[0].created_by_id) if notes else None

    print(f"--- {label} ---")
    print(f"form_submission.id:        {sub.id}")
    print(f"form_submission.form_type: {sub.form_type}")
    print(f"form_submission.name:      {sub.name!r}")
    print(f"form_submission.email:     {sub.email!r}")
    print(f"form_submission.phone:     {sub.phone!r}")
    print(f"form_submission.related_itinerary_id: {sub.related_itinerary_id}")
    print(f"form_submission.ip_address: {sub.ip_address!r}")
    print(f"form_submission.payload:   {json.dumps(sub.payload, indent=2)}")
    print(f"Lead.id:                   {lead.id}")
    print(f"Lead.source:               {lead.source!r}")
    print(f"Lead.title:                {lead.title!r}")
    print(f"Lead.value:                {lead.value}")
    print(f"Lead.status:               {lead.status!r}")
    print(f"Customer.id:               {customer.id if customer else None}")
    print(f"Customer.email:              {customer.email if customer else None!r}")
    print(f"Customer.phone:              {customer.phone if customer else None!r}")
    print(f"LeadNote.created_by_id:      {notes[0].created_by_id if notes else None}")
    print(f"LeadNote.created_by email:   {creator.email if creator else None!r}")
    print("LeadNote.content:")
    print(notes[0].content if notes else "(none)")
    print("LeadActivity:")
    for a in activities:
        print(f"  [{a.type}] {a.description}")
    return sub, lead


def part_servers_ready() -> None:
    sep(1, "Servers ready (started externally)")
    with httpx.Client(timeout=180) as c:
        api = c.get(f"{API}/health/db")
        print(f"  API health: {api.status_code} {api.text[:80]}")
        tr = c.get(f"{TRAGUIN}/", follow_redirects=True)
        print(f"  traguin /: {tr.status_code}")


def part_a_ui() -> None:
    global ui_post_headers, ui_submission_id
    from playwright.sync_api import sync_playwright

    sep(2, "PART A — UI itinerary_inquiry (single browser, one page)")

    # Resolve destination page URL (itinerary inquiry form lives on /destinations/{slug})
    with httpx.Client(timeout=30) as c:
        ir = c.get(f"{API}/api/cms/public/itineraries?limit=5")
        ir.raise_for_status()
        items = ir.json().get("items") or []
        if not items:
            raise RuntimeError("No published itineraries in CMS")
        # Prefer a real marketing itinerary over stress-test rows from prior runs.
        itin = next(
            (
                x
                for x in items
                if not re.search(r"stress|test|\d{8,}", x.get("slug", ""), re.I)
            ),
            items[0],
        )
        slug = itin["slug"]
        cms_id = itin["id"]
        dest_id = itin["destination_id"]
        dr = c.get(f"{API}/api/cms/public/destinations?limit=100")
        dr.raise_for_status()
        dests = dr.json().get("items") or []
        dest = next((d for d in dests if d["id"] == dest_id), None)
        if dest is None:
            raise RuntimeError(f"No destination for itinerary destination_id={dest_id}")
        dest_slug = dest["slug"]
    print(f"  using itinerary slug={slug!r} cms_id={cms_id} dest_slug={dest_slug!r}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        captured: list[dict] = []

        def on_request(req):
            if "/api/cms/public/form-submissions" in req.url and req.method == "POST":
                h = {k.lower(): v for k, v in req.headers.items()}
                captured.append(
                    {
                        "url": req.url,
                        "authorization": h.get("authorization"),
                        "cookie": h.get("cookie"),
                    }
                )

        page.on("request", on_request)
        target = f"{TRAGUIN}/destinations/{dest_slug}#inquiry"
        print(f"  navigating: {target}")
        page.goto(target, wait_until="domcontentloaded", timeout=180000)
        page.wait_for_selector("#inquiry-name", timeout=180000)
        page.wait_for_function(
            "() => !document.querySelector('.page-loader')",
            timeout=15000,
        )

        def fill_field(selector: str, value: str) -> None:
            loc = page.locator(selector)
            loc.click(force=True)
            loc.fill(value)
            loc.dispatch_event("input")
            loc.dispatch_event("change")

        fill_field("#inquiry-name", "Light Verify User")
        fill_field("#inquiry-email", UI_EMAIL)
        fill_field("#inquiry-phone", "9876501234")
        fill_field("#inquiry-dates", "March 2027")
        fill_field("#inquiry-travelers", "3")
        fill_field(
            "#inquiry-message",
            f"UI light verify {TAG} — interested in this itinerary.",
        )

        with page.expect_response(
            lambda r: "form-submissions" in r.url and r.request.method == "POST",
            timeout=60000,
        ):
            page.locator("#inquiry button[type=submit]").click()
        page.get_by_text("Inquiry Received").wait_for(timeout=60000)
        browser.close()

    if not captured:
        raise RuntimeError("No form-submissions POST captured from browser")
    ui_post_headers = captured[-1]
    print("  UI success state shown.")
    print(f"  Captured POST headers: {json.dumps(ui_post_headers, indent=2)}")

    with SessionLocal() as db:
        sub = db.scalar(
            select(FormSubmission)
            .where(FormSubmission.email == UI_EMAIL)
            .order_by(FormSubmission.created_at.desc())
            .limit(1)
        )
    if sub is None:
        raise RuntimeError(f"No form_submission for {UI_EMAIL}")
    ui_submission_id = sub.id

    sep(3, "PART A — DB evidence for UI submission")
    report_submission_lead(sub.id, "UI itinerary_inquiry")


def part_b_hotel_review() -> UUID:
    sep(5, "hotel_review exclusion (API POST, no Lead)")
    payload = {
        "form_type": "hotel_review",
        "name": f"{TAG} Reviewer",
        "payload": {
            "name": f"{TAG} Reviewer",
            "rating": 5,
            "review": "Wonderful stay with excellent service throughout our visit here.",
            "hotel_name": "Test Hotel",
        },
    }
    with httpx.Client(timeout=30) as c:
        r = c.post(f"{API}/api/cms/public/form-submissions", json=payload)
    print(f"  POST status: {r.status_code}")
    print(f"  POST body: {r.text[:400]}")
    assert r.status_code == 201, r.text
    sub_id = UUID(r.json()["id"])

    lead = lead_for_submission(sub_id)
    print(f"  Lead linked to submission {sub_id}: {lead}")
    assert lead is None, f"hotel_review must not create lead, got {lead.id if lead else None}"

    with httpx.Client(timeout=30) as c:
        login = c.post(
            f"{API}/api/crm/auth/login",
            json={"email": AGENCY_EMAIL, "password": AGENCY_PASSWORD},
        )
    token = login.json()["access_token"]
    with httpx.Client(timeout=30) as c:
        leads = c.get(
            f"{API}/api/crm/leads?limit=100",
            headers={"Authorization": f"Bearer {token}"},
        )
    items = leads.json().get("items", [])
    review_leads = [x for x in items if x.get("source") and "hotel_review" in x.get("source", "")]
    print(f"  GET /api/crm/leads — leads with hotel_review source: {len(review_leads)}")
    assert len(review_leads) == 0
    print("  ✓ form_submission created, no CRM Lead")
    return sub_id


def part_b_dup_email() -> tuple[UUID, UUID]:
    sep(6, "Duplicate email dedup (two API POSTs, same email)")
    customer_ids: list[str] = []
    lead_ids: list[str] = []
    for i in (1, 2):
        body = {
            "form_type": "itinerary_inquiry",
            "name": f"{TAG} Dup {i}",
            "email": DUP_EMAIL,
            "phone": "9876505678",
            "payload": {
                "name": f"{TAG} Dup {i}",
                "email": DUP_EMAIL,
                "phone": "9876505678",
                "travelers": 2,
                "dates": "April 2027",
                "message": f"API dup test attempt {i}",
                "itinerary_slug": "test-slug",
                "itinerary_title": "Test Itinerary",
            },
        }
        with httpx.Client(timeout=30) as c:
            r = c.post(f"{API}/api/cms/public/form-submissions", json=body)
        print(f"  POST #{i} status: {r.status_code} submission_id={r.json().get('id')}")
        sub_id = UUID(r.json()["id"])
        lead = lead_for_submission(sub_id)
        assert lead is not None
        lead_ids.append(str(lead.id))
        customer_ids.append(str(lead.customer_id))
        print(f"  POST #{i} → Lead {lead.id} → Customer {lead.customer_id}")

    print(f"  Customer IDs: {customer_ids[0]} vs {customer_ids[1]}")
    assert customer_ids[0] == customer_ids[1], "Second submission must reuse same Customer"
    print("  ✓ Same Customer ID on both submissions")
    return UUID(customer_ids[0]), UUID(lead_ids[0])


def part_no_auth() -> None:
    sep(7, "No CRM auth on public form POST")
    assert ui_post_headers is not None
    print(json.dumps(ui_post_headers, indent=2))
    assert not ui_post_headers.get("authorization"), "Must not send Authorization"
    cookie = ui_post_headers.get("cookie") or ""
    assert "travelcrm" not in cookie.lower() and "session" not in cookie.lower() or not cookie
    print("  ✓ No Bearer token, no CRM session cookie on UI POST")


def part_crm_visibility(ui_lead_id: UUID, dup_lead_id: UUID) -> None:
    sep(8, "CRM visibility via API login + GET /api/crm/leads")
    with httpx.Client(timeout=30) as c:
        login = c.post(
            f"{API}/api/crm/auth/login",
            json={"email": AGENCY_EMAIL, "password": AGENCY_PASSWORD},
        )
    print(f"  login status: {login.status_code}")
    token = login.json()["access_token"]
    with httpx.Client(timeout=30) as c:
        r = c.get(
            f"{API}/api/crm/leads?limit=100",
            headers={"Authorization": f"Bearer {token}"},
        )
    items = r.json().get("items", [])
    sources = sorted({x.get("source") for x in items if x.get("source")})
    print(f"  total leads returned: {len(items)}")
    print(f"  distinct sources (sample): {[s for s in sources if s and 'Website' in s][:10]}")

    ui_lead = next((x for x in items if x["id"] == str(ui_lead_id)), None)
    dup_lead = next((x for x in items if x["id"] == str(dup_lead_id)), None)
    print(f"  UI lead visible: {ui_lead is not None}")
    if ui_lead:
        print(f"    id={ui_lead['id']} source={ui_lead.get('source')!r} title={ui_lead.get('title')!r}")
    print(f"  Dup lead visible: {dup_lead is not None}")
    if dup_lead:
        print(f"    id={dup_lead['id']} source={dup_lead.get('source')!r} title={dup_lead.get('title')!r}")
    assert ui_lead and ui_lead.get("source") == "Website · itinerary_inquiry"
    assert dup_lead and dup_lead.get("source") == "Website · itinerary_inquiry"


def part_created_by_sanity(ui_lead_id: UUID) -> None:
    sep(9, "created_by_id sanity (API data)")
    with httpx.Client(timeout=30) as c:
        login = c.post(
            f"{API}/api/crm/auth/login",
            json={"email": AGENCY_EMAIL, "password": AGENCY_PASSWORD},
        )
    token = login.json()["access_token"]
    with httpx.Client(timeout=30) as c:
        r = c.get(
            f"{API}/api/crm/leads/{ui_lead_id}",
            headers={"Authorization": f"Bearer {token}"},
        )
    lead = r.json()
    print(json.dumps(
        {
            "id": lead.get("id"),
            "source": lead.get("source"),
            "title": lead.get("title"),
            "notes_count": len(lead.get("notes") or []),
            "activities_count": len(lead.get("activities") or []),
            "first_note_preview": (lead.get("notes") or [{}])[0].get("content", "")[:200],
            "first_activity": (lead.get("activities") or [{}])[0].get("description"),
        },
        indent=2,
    ))
    notes = lead.get("notes") or []
    activities = lead.get("activities") or []
    assert lead.get("source", "").startswith("Website ·")
    assert any("Form submission ID:" in (n.get("content") or "") for n in notes)
    assert any("Website intake" in (a.get("description") or "") for a in activities)
    print(
        "  Assessment: Lead.source clearly says 'Website · …'; note/activity text references "
        "form_submission_id and 'Website intake'. created_by_id on notes is the bootstrap admin "
        "server-side only — not exposed as misleading 'created by admin' on the lead list row; "
        "acceptable for v1. Optional future: dedicated system user or 'via Website' badge."
    )


def part_ip_code_review() -> None:
    sep(10, "IP fix scoping (code review)")
    path = Path(__file__).resolve().parent.parent / "utils" / "request.py"
    print(path.read_text())
    print(
        "  Conditions:\n"
        "  • NULL if request.client missing, host empty, or host fails ipaddress.ip_address()\n"
        "  • Real IP stored only when host parses as valid IPv4/IPv6 (e.g. 127.0.0.1 from browser)\n"
        "  • TestClient host 'testclient' → NULL (avoids inet DB error)\n"
        "  Gap: no log line when invalid IP is dropped — silent NULL. Flag only, not fixing now."
    )


def part_ip_runtime() -> None:
    sep(10, "IP fix runtime spot-check")
    tc = TestClient(app)
    email = f"{TAG}-tc@example.com"
    r = tc.post(
        "/api/cms/public/form-submissions",
        json={
            "form_type": "contact_consultation",
            "email": email,
            "payload": {"message": "testclient probe"},
        },
    )
    assert r.status_code == 201
    with SessionLocal() as db:
        sub = db.scalar(
            select(FormSubmission).where(FormSubmission.email == email).limit(1)
        )
    print(f"  TestClient submission ip_address: {sub.ip_address!r} (expect None)")
    assert sub.ip_address is None


def main() -> None:
    print(f"TAG={TAG}")
    part_servers_ready()
    part_a_ui()
    part_b_hotel_review()
    _, dup_lead_id = part_b_dup_email()
    part_no_auth()
    assert ui_submission_id
    ui_lead = lead_for_submission(ui_submission_id)
    assert ui_lead
    part_crm_visibility(ui_lead.id, dup_lead_id)
    part_created_by_sanity(ui_lead.id)
    part_ip_code_review()
    part_ip_runtime()
    print(f"\n{'=' * 60}\nALL LIGHT CHECKS PASSED  TAG={TAG}\n{'=' * 60}")


if __name__ == "__main__":
    main()
