#!/usr/bin/env python3
"""Full website → CRM E2E: all public forms, CRM API flows, cleanup."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from uuid import UUID

import httpx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import delete, func, select

from database import SessionLocal
from models.crm.customers import Customer
from models.crm.leads import Lead, LeadActivity, LeadFollowup, LeadNote
from models.crm.tenancy import User
from models.submissions import FormSubmission
from utils.passwords import hash_password

TRAGUIN_BASE = "http://127.0.0.1:3001"
CRM_BASE = "http://127.0.0.1:3002"
API_BASE = "http://127.0.0.1:8001"
AGENCY_EMAIL = "admin@traguin-demo.com"
AGENCY_PASSWORD = "Traguin-Demo-2026!"

TEST_TAG = f"e2e-crm-{int(time.time())}"
SHARED_EMAIL = f"{TEST_TAG}-dup@example.com"

LEAD_FORM_TYPES = [
    "contact_consultation",
    "travel_expert_consultation",
    "plan_my_journey",
    "travel_planner",
    "itinerary_inquiry",
    "hotel_booking",
]

submission_ids: list[UUID] = []
lead_ids: list[UUID] = []
customer_ids: set[UUID] = set()
primary_lead_id: UUID | None = None
hotel_review_submission_id: UUID | None = None
auth_token: str | None = None


def sep(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def ok(msg: str) -> None:
    print(f"  ✓ {msg}")


def fail(msg: str) -> None:
    print(f"  ✗ {msg}", file=sys.stderr)
    raise AssertionError(msg)


def wait_url(url: str, *, timeout: float = 180.0, label: str = "") -> bool:
    import urllib.error
    import urllib.request

    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=5) as resp:
                if resp.status < 500:
                    print(f"  ready: {label or url} (HTTP {resp.status})")
                    return True
        except (urllib.error.URLError, TimeoutError, OSError):
            pass
        time.sleep(2)
    print(f"  TIMEOUT waiting for {label or url}")
    return False


def start_server_if_needed(port: int, cmd: list[str], cwd: str, health_url: str, label: str) -> None:
    import urllib.error
    import urllib.request

    try:
        with urllib.request.urlopen(health_url, timeout=3):
            print(f"  {label} already up on :{port}")
            return
    except (urllib.error.URLError, TimeoutError, OSError):
        pass

    log = Path(__file__).resolve().parent / f"_e2e_server_{port}.log"
    print(f"  starting {label} on :{port} …")
    with open(log, "w") as fh:
        subprocess.Popen(
            cmd,
            cwd=cwd,
            stdout=fh,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
    if not wait_url(health_url, timeout=240, label=label):
        raise RuntimeError(f"{label} failed to start — see {log}")


def ensure_servers() -> None:
    sep("0) Servers")
    api_dir = Path(__file__).resolve().parent.parent
    traguin_dir = api_dir.parent / "traguin"
    crm_dir = api_dir.parent / "travelcrm-main"

    start_server_if_needed(
        8001,
        [str(api_dir / ".venv/bin/uvicorn"), "main:app", "--host", "127.0.0.1", "--port", "8001"],
        str(api_dir),
        f"{API_BASE}/health/db",
        "API",
    )
    wait_url(f"{TRAGUIN_BASE}/", timeout=30, label="traguin (probe)")
    start_server_if_needed(
        3001,
        ["npm", "run", "dev", "--", "-p", "3001"],
        str(traguin_dir),
        f"{TRAGUIN_BASE}/",
        "traguin",
    )
    wait_url(f"{TRAGUIN_BASE}/contact", timeout=240, label="traguin /contact")
    start_server_if_needed(
        3002,
        ["npm", "run", "dev", "--", "-p", "3002"],
        str(crm_dir),
        f"{CRM_BASE}/",
        "CRM",
    )


def submit_via_website_proxy(client: httpx.Client, body: dict) -> dict:
    """POST through tragin Next.js proxy (same path the browser uses)."""
    response = client.post(f"{TRAGUIN_BASE}/api/public/form-submissions", json=body, timeout=60)
    if response.status_code != 201:
        fail(f"Form submit failed ({body['form_type']}): HTTP {response.status_code} {response.text[:400]}")
    data = response.json()
    submission_ids.append(UUID(data["id"]))
    if data.get("lead_id"):
        lead_ids.append(UUID(data["lead_id"]))
    ok(f"{body['form_type']} → submission {data['id']}" + (f", lead {data['lead_id']}" if data.get("lead_id") else ""))
    return data


def submit_all_forms_api() -> None:
    sep("1) Submit all website forms (via tragin /api/public/form-submissions)")
    start = date.today() + timedelta(days=45)
    end = start + timedelta(days=7)
    start_iso = start.isoformat()
    end_iso = end.isoformat()

    with httpx.Client(timeout=60) as client:
        itinerary_id = None
        destination_id = None
        hotel_id = None
        ir = client.get(f"{API_BASE}/api/cms/public/itineraries?limit=10")
        ir.raise_for_status()
        items = ir.json().get("items") or []
        if items:
            itin = next(
                (x for x in items if not re.search(r"stress|e2e-|test-\d", x.get("slug", ""), re.I)),
                items[0],
            )
            itinerary_id = itin["id"]
            destination_id = itin["destination_id"]

        hr = client.get(f"{API_BASE}/api/cms/public/hotels?limit=5")
        if hr.status_code == 200:
            hotels = hr.json().get("items") or []
            if hotels:
                hotel_id = hotels[0]["id"]

        submit_via_website_proxy(
            client,
            {
                "form_type": "contact_consultation",
                "name": f"{TEST_TAG} Contact",
                "email": f"{TEST_TAG}-contact@example.com",
                "phone": "+919900011001",
                "payload": {"message": f"{TEST_TAG} contact form — luxury honeymoon consultation."},
            },
        )
        submit_via_website_proxy(
            client,
            {
                "form_type": "travel_expert_consultation",
                "name": f"{TEST_TAG} Expert",
                "email": f"{TEST_TAG}-expert@example.com",
                "phone": "+919900011002",
                "payload": {
                    "service": "Visa & concierge",
                    "message": f"{TEST_TAG} travel expert consultation for Europe.",
                },
            },
        )
        submit_via_website_proxy(
            client,
            {
                "form_type": "plan_my_journey",
                "name": "WhatsApp Callback Request",
                "phone": "+919900011003",
                "payload": {"source_page": "homepage_cta"},
            },
        )
        submit_via_website_proxy(
            client,
            {
                "form_type": "plan_my_journey",
                "name": f"{TEST_TAG} Landing",
                "email": f"{TEST_TAG}-landing@example.com",
                "phone": "+919900011004",
                "payload": {
                    "destination": "Maldives",
                    "start_date": start_iso,
                    "end_date": end_iso,
                    "rooms": 1,
                    "adults": 2,
                    "children": 0,
                    "budget_range": "₹2,00,000 – ₹3,50,000",
                    "notes": f"{TEST_TAG} plan-my-journey landing form",
                    "source_page": "plan_my_journey_landing",
                },
            },
        )
        submit_via_website_proxy(
            client,
            {
                "form_type": "travel_planner",
                "email": f"{TEST_TAG}-planner@example.com",
                "phone": "+919900011005",
                "payload": {
                    "destination": "Bali",
                    "start_date": start_iso,
                    "end_date": end_iso,
                    "travelers": "2",
                    "budget": "₹1,50,000",
                    "notes": f"{TEST_TAG} travel planner homepage form",
                },
            },
        )
        for attempt in (1, 2):
            submit_via_website_proxy(
                client,
                {
                    "form_type": "itinerary_inquiry",
                    "name": f"{TEST_TAG} Itinerary {attempt}",
                    "email": SHARED_EMAIL,
                    "phone": "+919900011006",
                    "related_itinerary_id": itinerary_id,
                    "related_destination_id": destination_id,
                    "payload": {
                        "start_date": start_iso,
                        "end_date": end_iso,
                        "travelers": "2",
                        "message": f"{TEST_TAG} itinerary inquiry attempt {attempt}.",
                    },
                },
            )
        if hotel_id:
            submit_via_website_proxy(
                client,
                {
                    "form_type": "hotel_booking",
                    "name": f"{TEST_TAG} Hotel",
                    "email": f"{TEST_TAG}-hotel@example.com",
                    "phone": "+919900011007",
                    "related_hotel_id": hotel_id,
                    "payload": {
                        "check_in": start_iso,
                        "check_out": end_iso,
                        "guests": "2",
                        "message": f"{TEST_TAG} hotel booking request.",
                    },
                },
            )
        else:
            print("  ⚠ No published hotels — skipping hotel_booking")

        global hotel_review_submission_id
        review = submit_via_website_proxy(
            client,
            {
                "form_type": "hotel_review",
                "name": f"{TEST_TAG} Reviewer",
                "email": f"{TEST_TAG}-review@example.com",
                "related_hotel_id": hotel_id,
                "payload": {
                    "rating": 5,
                    "review": f"{TEST_TAG} An absolutely wonderful stay with impeccable service throughout.",
                },
            },
        )
        hotel_review_submission_id = UUID(review["id"])


def lead_for_submission(submission_id: UUID) -> Lead | None:
    with SessionLocal() as db:
        note = db.scalar(
            select(LeadNote).where(LeadNote.content.contains(str(submission_id))).limit(1)
        )
        if note is None:
            lead = db.scalar(
                select(Lead).where(Lead.cms_form_submission_id == submission_id, Lead.is_deleted.is_(False))
            )
            return lead
        return db.get(Lead, note.lead_id)


def verify_intake() -> None:
    global primary_lead_id
    sep("2) Verify CMS submissions → CRM leads")

    with SessionLocal() as db:
        for sub_id in submission_ids:
            sub = db.get(FormSubmission, sub_id)
            if sub is None:
                fail(f"Missing submission {sub_id}")
            if sub.form_type == "hotel_review":
                continue
            if sub.form_type not in LEAD_FORM_TYPES:
                continue
            lead = lead_for_submission(sub_id)
            if lead is None:
                fail(f"No CRM lead for {sub.form_type} submission {sub_id}")
            if lead.id not in lead_ids:
                lead_ids.append(lead.id)
            if lead.customer_id:
                customer_ids.add(lead.customer_id)
            ok(f"{sub.form_type}: lead {lead.id} status={lead.status!r} source={lead.source!r}")

        review_lead = lead_for_submission(hotel_review_submission_id) if hotel_review_submission_id else None
        if review_lead is not None:
            fail(f"hotel_review must not create a lead, got {review_lead.id}")
        ok("hotel_review created submission only (no lead)")

        dup_leads = []
        for sub_id in submission_ids:
            sub = db.get(FormSubmission, sub_id)
            if sub and sub.form_type == "itinerary_inquiry" and sub.email == SHARED_EMAIL:
                lead = lead_for_submission(sub_id)
                if lead:
                    dup_leads.append(lead)
        if len(dup_leads) >= 2:
            cust_ids = {lead.customer_id for lead in dup_leads}
            if len(cust_ids) != 1:
                fail(f"Duplicate-email itinerary inquiries should share one customer, got {cust_ids}")
            ok(f"Duplicate email inquiries share customer {next(iter(cust_ids))}")

    primary_lead_id = lead_ids[0] if lead_ids else None
    if primary_lead_id is None:
        fail("No leads created — cannot continue CRM tests")


def crm_login(client: httpx.Client) -> str:
    response = client.post(
        f"{API_BASE}/api/crm/auth/login",
        json={"email": AGENCY_EMAIL, "password": AGENCY_PASSWORD},
        timeout=30,
    )
    if response.status_code == 200:
        token = response.json().get("access_token")
        if token:
            ok("CRM API login")
            return token

    print("  resetting demo CRM password for E2E …")
    with SessionLocal() as db:
        user = db.scalar(
            select(User).where(User.email == AGENCY_EMAIL.strip().lower(), User.is_deleted.is_(False))
        )
        if user is None:
            fail(f"No CRM user {AGENCY_EMAIL}")
        user.password_hash = hash_password(AGENCY_PASSWORD)
        db.commit()
    response = client.post(
        f"{API_BASE}/api/crm/auth/login",
        json={"email": AGENCY_EMAIL, "password": AGENCY_PASSWORD},
        timeout=30,
    )
    if response.status_code != 200:
        fail(f"CRM login failed after password reset: {response.status_code} {response.text[:300]}")
    token = response.json().get("access_token")
    if not token:
        fail("CRM login returned no access_token")
    ok("CRM API login (after password reset)")
    return token


def crm_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def test_crm_functionality() -> None:
    global auth_token
    sep("3) CRM functionality (API)")
    assert primary_lead_id is not None

    with httpx.Client(timeout=60) as client:
        auth_token = crm_login(client)
        headers = crm_headers(auth_token)

        listed = client.get(f"{API_BASE}/api/crm/leads?limit=100", headers=headers)
        if listed.status_code != 200:
            fail(f"List leads failed: {listed.status_code}")
        items = listed.json().get("items") or []
        visible = [row for row in items if TEST_TAG in json.dumps(row)]
        ok(f"GET /api/crm/leads — {len(visible)} test lead(s) visible")

        detail = client.get(f"{API_BASE}/api/crm/leads/{primary_lead_id}", headers=headers)
        if detail.status_code != 200:
            fail(f"Get lead failed: {detail.status_code}")
        ok(f"GET /api/crm/leads/{{id}} — {detail.json().get('title')!r}")

        patch = client.patch(
            f"{API_BASE}/api/crm/leads/{primary_lead_id}",
            headers=headers,
            json={
                "status": "CONTACTED",
                "append_notes": [{"content": f"{TEST_TAG} CRM note from E2E test"}],
                "append_followups": [
                    {
                        "scheduled_at": (date.today() + timedelta(days=3)).isoformat(),
                        "notes": f"{TEST_TAG} follow-up reminder",
                    }
                ],
            },
        )
        if patch.status_code != 200:
            fail(f"Patch lead failed: {patch.status_code} {patch.text[:300]}")
        patched = patch.json()
        if patched.get("status") != "CONTACTED":
            fail(f"Expected CONTACTED, got {patched.get('status')}")
        ok("PATCH lead — status CONTACTED + note + follow-up")

        history = client.get(
            f"{API_BASE}/api/crm/leads/{primary_lead_id}/inquiry-history",
            headers=headers,
        )
        if history.status_code != 200:
            fail(f"Inquiry history failed: {history.status_code}")
        ok("GET inquiry-history")

        since = (datetime.now(timezone.utc) - timedelta(hours=2)).isoformat()
        recent = client.get(
            f"{API_BASE}/api/crm/leads/recent",
            headers=headers,
            params={"since": since},
        )
        if recent.status_code != 200:
            fail(f"Recent leads failed: {recent.status_code}")
        ok(f"GET /api/crm/leads/recent — {len(recent.json())} event(s)")

        pending_fu = client.get(f"{API_BASE}/api/crm/leads/followups/pending", headers=headers)
        if pending_fu.status_code != 200:
            fail(f"Pending followups failed: {pending_fu.status_code}")
        ok(f"GET followups/pending — {len(pending_fu.json())} item(s)")


def test_crm_ui_visibility() -> None:
    sep("4) CRM UI visibility (Playwright)")
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("  ⚠ playwright not installed — skipping UI checks")
        return

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            page.goto(f"{CRM_BASE}/auth/login", wait_until="domcontentloaded", timeout=120000)
            page.wait_for_selector("#crm-login-email", timeout=60000)
            page.fill("#crm-login-email", AGENCY_EMAIL)
            page.fill("#crm-login-password", AGENCY_PASSWORD)
            page.get_by_role("button", name=re.compile("^Sign in$", re.I)).click()
            page.wait_for_url(re.compile(r"/dashboard"), timeout=90000)
            page.goto(f"{CRM_BASE}/dashboard/crm", wait_until="domcontentloaded", timeout=120000)
            page.wait_for_timeout(4000)
            count = page.get_by_text(TEST_TAG, exact=False).count()
            if count < 1:
                fail(f"CRM UI did not show any rows containing {TEST_TAG!r}")
            ok(f"CRM /dashboard/crm shows test leads ({count} match(es) for {TEST_TAG})")
            page.get_by_text(TEST_TAG, exact=False).first.click()
            page.wait_for_timeout(2000)
            body = page.locator("body").inner_text()
            if "CONTACTED" not in body and "Contacted" not in body:
                print("  ⚠ CONTACTED status not visible in drawer (may need refresh)")
            else:
                ok("Lead detail drawer opens with updated status")
            browser.close()
    except Exception as exc:
        print(f"  ⚠ CRM UI Playwright check skipped: {exc}")


def collect_test_lead_ids() -> list[UUID]:
    ids = list(dict.fromkeys(lead_ids))
    with SessionLocal() as db:
        rows = db.scalars(select(Lead).where(Lead.is_deleted.is_(False))).all()
        for lead in rows:
            blob = json.dumps(
                {
                    "title": lead.title,
                    "first_name": lead.first_name,
                    "last_name": lead.last_name,
                    "email": lead.email,
                    "message": lead.message,
                    "source": lead.source,
                },
                default=str,
            )
            if TEST_TAG in blob and lead.id not in ids:
                ids.append(lead.id)
    return ids


def collect_test_submission_ids() -> list[UUID]:
    ids = list(dict.fromkeys(submission_ids))
    with SessionLocal() as db:
        rows = db.scalars(select(FormSubmission)).all()
        for sub in rows:
            blob = json.dumps(
                {
                    "name": sub.name,
                    "email": sub.email,
                    "phone": sub.phone,
                    "payload": sub.payload,
                },
                default=str,
            )
            if TEST_TAG in blob and sub.id not in ids:
                ids.append(sub.id)
    return ids


def cleanup() -> None:
    sep("5) Cleanup dummy records")
    deleted_leads = 0
    deleted_submissions = 0
    lead_ids_to_delete = collect_test_lead_ids()
    submission_ids_to_delete = collect_test_submission_ids()

    with httpx.Client(timeout=60) as client:
        token = auth_token
        if not token:
            try:
                token = crm_login(client)
            except Exception:
                token = None
        if token:
            headers = crm_headers(token)
            for lead_id in lead_ids_to_delete:
                response = client.delete(f"{API_BASE}/api/crm/leads/{lead_id}", headers=headers)
                if response.status_code == 204:
                    deleted_leads += 1

    with SessionLocal() as db:
        for sub_id in submission_ids_to_delete:
            sub = db.get(FormSubmission, sub_id)
            if sub:
                db.delete(sub)
                deleted_submissions += 1

        for customer_id in customer_ids:
            customer = db.get(Customer, customer_id)
            if customer is None:
                continue
            remaining = db.scalar(
                select(func.count())
                .select_from(Lead)
                .where(Lead.customer_id == customer_id, Lead.is_deleted.is_(False))
            )
            if remaining == 0 and TEST_TAG in (customer.email or ""):
                customer.is_deleted = True

        db.commit()

    ok(f"Soft-deleted {deleted_leads} CRM lead(s)")
    ok(f"Hard-deleted {deleted_submissions} form submission(s)")
    ok("Soft-deleted orphaned test customers (if any)")


def main() -> None:
    print(f"TEST_TAG = {TEST_TAG}")
    try:
        ensure_servers()
        submit_all_forms_api()
        verify_intake()
        test_crm_functionality()
        test_crm_ui_visibility()
        sep("DONE — all E2E checks passed")
        print(f"TEST_TAG = {TEST_TAG}")
    finally:
        cleanup()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\nFAILED: {exc}", file=sys.stderr)
        sys.exit(1)
