#!/usr/bin/env python3
"""Full E2E evidence report: traguin UI forms → CMS → CRM (no hand-off)."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import time
from datetime import date, timedelta
from pathlib import Path
from uuid import UUID

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import func, select

from database import SessionLocal
from models.crm.customers import Customer
from models.crm.leads import Lead, LeadActivity, LeadNote
from models.crm.tenancy import User
from models.submissions import FormSubmission

TRAGUIN_BASE = "http://127.0.0.1:3001"
CRM_BASE = "http://127.0.0.1:3002"
API_BASE = "http://127.0.0.1:8001"
AGENCY_EMAIL = "admin@traguin-demo.com"
AGENCY_PASSWORD = "Traguin-Demo-2026!"
DEFAULT_AGENCY_ID = UUID("daead252-e21c-4df2-8362-20d25bc523cf")
SYSTEM_USER_ID = UUID("09a685a3-7dcb-48e8-9dd9-f1c872b7cc1e")

TEST_TAG = f"e2e-{int(time.time())}"
SHARED_EMAIL = f"{TEST_TAG}-dup@example.com"

LEAD_FORM_TYPES = [
    "contact_consultation",
    "travel_expert_consultation",
    "plan_my_journey",
    "travel_planner",
    "itinerary_inquiry",
    "hotel_booking",
]

# Populated during UI runs
console_by_form: dict[str, list[str]] = {}
form_post_headers: list[dict] = []
submission_ids: dict[str, UUID] = {}
itinerary_customer_ids: list[UUID] = []
hotel_review_submission_id: UUID | None = None


def sep(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


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

    log = Path(__file__).resolve().parent / f"_verify_server_{port}.log"
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
    sep("0) Starting / waiting for servers")
    api_dir = Path(__file__).resolve().parent.parent
    traguin_dir = api_dir.parent / "traguin"
    crm_dir = api_dir.parent / "travelcrm-main"

    start_server_if_needed(
        8001,
        ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8001"],
        str(api_dir),
        f"{API_BASE}/health/db",
        "API",
    )
    # Warm traguin homepage first (dev compile)
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


def submission_for_tag(form_type: str, *, email: str | None = None, name: str | None = None) -> FormSubmission:
    with SessionLocal() as db:
        q = select(FormSubmission).where(FormSubmission.form_type == form_type)
        if email:
            q = q.where(FormSubmission.email == email.lower())
        if name:
            q = q.where(FormSubmission.name == name)
        q = q.order_by(FormSubmission.created_at.desc()).limit(1)
        row = db.scalar(q)
        if row is None:
            raise AssertionError(f"No form_submission for {form_type}")
        return row


def lead_for_submission(submission_id: UUID) -> Lead | None:
    needle = str(submission_id)
    with SessionLocal() as db:
        notes = db.scalars(select(LeadNote).where(LeadNote.content.contains(needle))).all()
        if not notes:
            return None
        return db.get(Lead, notes[0].lead_id)


def report_form_evidence(form_type: str, *, email: str | None = None, name: str | None = None) -> None:
    sub = submission_for_tag(form_type, email=email, name=name)
    submission_ids[form_type] = sub.id
    lead = lead_for_submission(sub.id)

    print(f"\n--- {form_type} ---")
    print(f"form_submission.id:       {sub.id}")
    print(f"form_submission.form_type:{sub.form_type}")
    print(f"form_submission.name:     {sub.name!r}")
    print(f"form_submission.email:    {sub.email!r}")
    print(f"form_submission.phone:    {sub.phone!r}")
    print(f"form_submission.ip:       {sub.ip_address!r}")
    print(f"form_submission.payload:  {json.dumps(sub.payload, indent=2)[:800]}")

    if lead is None:
        raise AssertionError(f"Expected CRM Lead for {form_type}, none found")

    with SessionLocal() as db:
        customer = db.get(Customer, lead.customer_id) if lead.customer_id else None
        notes = db.scalars(select(LeadNote).where(LeadNote.lead_id == lead.id)).all()
        activities = db.scalars(select(LeadActivity).where(LeadActivity.lead_id == lead.id)).all()
        creator = db.get(User, notes[0].created_by_id) if notes else None

    print(f"Lead.id:                  {lead.id}")
    print(f"Lead.source:              {lead.source!r}")
    print(f"Lead.title:               {lead.title!r}")
    print(f"Lead.value:               {lead.value}")
    print(f"Lead.status:              {lead.status!r}")
    print(f"Customer.id:              {customer.id if customer else None}")
    print(f"Customer.email:           {customer.email if customer else None!r}")
    print(f"Customer.phone:           {customer.phone if customer else None!r}")
    print(f"LeadNote.created_by_id:   {notes[0].created_by_id if notes else None}")
    print(f"LeadNote.created_by:      {creator.email if creator else None!r}")
    print("LeadNote.content:")
    print(notes[0].content if notes else "(none)")
    print("LeadActivity:")
    for act in activities:
        print(f"  [{act.type}] {act.description}")


def track_console(form_key: str):
    console_by_form[form_key] = []

    def handler(msg):
        if msg.type not in ("error", "warning"):
            return
        text = msg.text
        if "favicon" in text.lower():
            return
        console_by_form[form_key].append(f"[{msg.type}] {text}")

    return handler


def capture_form_post(request):
    if "/api/cms/public/form-submissions" in request.url and request.method == "POST":
        headers = {k.lower(): v for k, v in request.headers.items()}
        form_post_headers.append(
            {
                "url": request.url,
                "authorization": headers.get("authorization"),
                "cookie": headers.get("cookie"),
            }
        )


def run_ui_submissions() -> None:
    from playwright.sync_api import sync_playwright

    start = date.today() + timedelta(days=30)
    end = start + timedelta(days=7)
    start_iso = start.isoformat()
    end_iso = end.isoformat()

    sep("1-4) UI form submissions (Playwright → real traguin pages)")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.on("request", capture_form_post)

        # contact_consultation
        page.on("console", track_console("contact_consultation"))
        page.goto(f"{TRAGUIN_BASE}/contact", wait_until="domcontentloaded", timeout=120000)
        page.wait_for_selector("#contact-name", timeout=60000)
        page.fill("#contact-name", f"{TEST_TAG} Contact")
        page.fill("#contact-email", f"{TEST_TAG}-contact@example.com")
        page.fill("#contact-phone", "9876543210")
        page.fill("#contact-message", "Luxury honeymoon consultation for Maldives in December.")
        page.get_by_role("button", name=re.compile("Connect With a Travel Expert", re.I)).click()
        page.get_by_text("Message Sent").wait_for(timeout=30000)
        page.remove_listener("console", track_console("contact_consultation"))

        # travel_expert_consultation
        page.on("console", track_console("travel_expert_consultation"))
        page.goto(f"{TRAGUIN_BASE}/travel-expert", wait_until="domcontentloaded", timeout=120000)
        page.wait_for_selector("#concierge-name", timeout=60000)
        page.fill("#concierge-name", f"{TEST_TAG} Expert")
        page.fill("#concierge-email", f"{TEST_TAG}-expert@example.com")
        page.fill("#concierge-phone", "9876543211")
        page.fill("#concierge-message", "Need visa and concierge support for Europe in August.")
        page.get_by_role("button", name=re.compile("Submit to Travel Expert", re.I)).click()
        page.get_by_text("Request received").wait_for(timeout=30000)
        page.remove_listener("console", track_console("travel_expert_consultation"))

        # plan_my_journey
        page.on("console", track_console("plan_my_journey"))
        page.goto(f"{TRAGUIN_BASE}/", wait_until="domcontentloaded", timeout=120000)
        page.wait_for_selector("#planner-phone", timeout=60000)
        page.fill("#planner-phone", "9876543212")
        page.locator("#plan-my-journey button[type='submit']").click()
        page.get_by_text("Thank you").wait_for(timeout=30000)
        page.remove_listener("console", track_console("plan_my_journey"))

        # travel_planner
        page.on("console", track_console("travel_planner"))
        page.goto(f"{TRAGUIN_BASE}/#planner", wait_until="domcontentloaded", timeout=120000)
        page.wait_for_selector("#planner-destination", timeout=60000)
        page.fill("#planner-destination", "Maldives")
        page.fill("#planner-start-date", start_iso)
        page.fill("#planner-end-date", end_iso)
        page.get_by_role("button", name="Continue").click()
        page.fill("#planner-travelers", "2")
        page.get_by_role("button", name="Continue").click()
        page.fill("#planner-email", f"{TEST_TAG}-planner@example.com")
        page.fill("#planner-phone", "9876543213")
        page.get_by_role("button", name=re.compile("Get Personalized Itinerary", re.I)).click()
        page.get_by_text("Request Received").wait_for(timeout=30000)
        page.remove_listener("console", track_console("travel_planner"))

        # itinerary_inquiry x2 same email
        page.on("console", track_console("itinerary_inquiry"))
        with httpx.Client(timeout=30) as c:
            ir = c.get(f"{API_BASE}/api/cms/public/itineraries?limit=5")
            ir.raise_for_status()
            itin = (ir.json().get("items") or [])[0]
            dest_id = itin["destination_id"]
            dr = c.get(f"{API_BASE}/api/cms/public/destinations?limit=100")
            dr.raise_for_status()
            dest = next(d for d in (dr.json().get("items") or []) if d["id"] == dest_id)
            dest_slug = dest["slug"]
        page.goto(
            f"{TRAGUIN_BASE}/destinations/{dest_slug}#inquiry",
            wait_until="domcontentloaded",
            timeout=120000,
        )
        page.wait_for_selector("#inquiry-name", timeout=60000)
        for attempt in (1, 2):
            page.fill("#inquiry-name", f"{TEST_TAG} Itinerary {attempt}")
            page.fill("#inquiry-email", SHARED_EMAIL)
            page.fill("#inquiry-phone", "9876543214")
            page.fill("#inquiry-dates", "December 2026")
            page.fill("#inquiry-travelers", "2")
            page.fill("#inquiry-message", f"Inquiry attempt {attempt} — same email reuse test.")
            page.get_by_role("button", name=re.compile("Request", re.I)).click()
            page.get_by_text("Inquiry Received").wait_for(timeout=30000)
            if attempt == 1:
                page.reload(wait_until="domcontentloaded")
                page.wait_for_selector("#inquiry-name", timeout=60000)
        page.remove_listener("console", track_console("itinerary_inquiry"))

        # hotel_booking
        page.on("console", track_console("hotel_booking"))
        page.goto(f"{TRAGUIN_BASE}/hotels", wait_until="domcontentloaded", timeout=120000)
        hotel_href = page.locator("a[href^='/hotels/']").first.get_attribute("href")
        assert hotel_href, "no hotel link"
        page.goto(f"{TRAGUIN_BASE}{hotel_href}#hotel-booking", wait_until="domcontentloaded", timeout=120000)
        page.wait_for_selector("#hotel-booking-name", timeout=60000)
        page.fill("#hotel-booking-name", f"{TEST_TAG} Hotel")
        page.fill("#hotel-booking-email", f"{TEST_TAG}-hotel@example.com")
        page.fill("#hotel-booking-phone", "9876543215")
        page.fill("#hotel-booking-dates", "Jan 10–15, 2027")
        page.fill("#hotel-booking-travelers", "2")
        page.get_by_role("button", name=re.compile("Submit Booking Request", re.I)).click()
        page.get_by_text("Booking Request Received").wait_for(timeout=30000)
        page.remove_listener("console", track_console("hotel_booking"))

        # hotel_review (negative)
        page.on("console", track_console("hotel_review"))
        page.goto(f"{TRAGUIN_BASE}{hotel_href}#hotel-review", wait_until="domcontentloaded", timeout=120000)
        page.wait_for_selector("#hotel-review-name", timeout=60000)
        page.fill("#hotel-review-name", f"{TEST_TAG} Reviewer")
        page.locator("#hotel-review button[aria-label='5 stars']").click()
        page.fill(
            "#hotel-review-text",
            "An absolutely wonderful stay with impeccable service throughout our visit.",
        )
        page.get_by_role("button", name=re.compile("Submit Review", re.I)).click()
        page.get_by_text("Thank You").wait_for(timeout=30000)
        page.remove_listener("console", track_console("hotel_review"))

        global hotel_review_submission_id
        review_sub = submission_for_tag("hotel_review", name=f"{TEST_TAG} Reviewer")
        hotel_review_submission_id = review_sub.id

        # CRM dashboard UI
        sep("6) CRM /dashboard/crm visibility (Playwright login)")
        crm = context.new_page()
        crm.on("console", track_console("crm_dashboard"))
        crm.goto(f"{CRM_BASE}/auth/login", wait_until="domcontentloaded", timeout=120000)
        crm.wait_for_selector('input[type="email"]', timeout=60000)
        crm.fill('input[type="email"]', AGENCY_EMAIL)
        crm.fill('input[type="password"]', AGENCY_PASSWORD)
        crm.get_by_role("button", name=re.compile("Sign In Securely", re.I)).click()
        crm.wait_for_url(re.compile(r"/dashboard"), timeout=60000)
        crm.goto(f"{CRM_BASE}/dashboard/crm", wait_until="domcontentloaded", timeout=120000)
        crm.wait_for_timeout(3000)

        visible_sources: list[str] = []
        for src in [
            "Website · contact_consultation",
            "Website · travel_expert_consultation",
            "Website · plan_my_journey",
            "Website · travel_planner",
            "Website · itinerary_inquiry",
            "Website · hotel_booking",
        ]:
            loc = crm.get_by_text(src, exact=False)
            count = loc.count()
            visible_sources.append(f"{src}: {count} visible")
            print(f"  CRM UI — {src}: {count} match(es) on page")

        # Open first website lead drawer for attribution check
        crm.get_by_text("Website ·", exact=False).first.click()
        crm.wait_for_timeout(1500)
        drawer_text = crm.locator("body").inner_text()
        attribution_snippet = "\n".join(
            line for line in drawer_text.splitlines() if "admin@traguin-demo.com" in line or "Website" in line
        )[:1200]
        print("\n  Lead detail attribution snippet (CRM UI):")
        print(attribution_snippet or "(no attribution lines matched)")

        browser.close()


def report_all_evidence() -> None:
    sep("2) DB evidence per lead-eligible form")
    report_form_evidence("contact_consultation", email=f"{TEST_TAG}-contact@example.com")
    report_form_evidence("travel_expert_consultation", email=f"{TEST_TAG}-expert@example.com")
    report_form_evidence("plan_my_journey", name="WhatsApp Callback Request")
    report_form_evidence("travel_planner", email=f"{TEST_TAG}-planner@example.com")
    report_form_evidence("hotel_booking", email=f"{TEST_TAG}-hotel@example.com")

    # itinerary inquiries — two leads, one customer
    sep("4) Duplicate email → same Customer")
    with SessionLocal() as db:
        subs = db.scalars(
            select(FormSubmission)
            .where(
                FormSubmission.form_type == "itinerary_inquiry",
                FormSubmission.email == SHARED_EMAIL,
            )
            .order_by(FormSubmission.created_at.desc())
            .limit(2)
        ).all()
        customer_ids: list[UUID] = []
        for sub in subs:
            lead = lead_for_submission(sub.id)
            assert lead is not None
            customer_ids.append(lead.customer_id)
            print(f"  submission {sub.id} → lead {lead.id} → customer {lead.customer_id}")
        assert len(set(customer_ids)) == 1, f"Expected 1 customer, got {set(customer_ids)}"
        print(f"  ✓ Both itinerary inquiries share Customer.id = {customer_ids[0]}")

    report_form_evidence("itinerary_inquiry", email=SHARED_EMAIL)

    sep("3) hotel_review — submission YES, Lead NO")
    assert hotel_review_submission_id is not None
    review_sub = submission_for_tag("hotel_review", name=f"{TEST_TAG} Reviewer")
    lead = lead_for_submission(review_sub.id)
    print(f"form_submission.id: {review_sub.id}")
    print(f"form_submission.form_type: {review_sub.form_type}")
    print(f"Lead for this submission: {lead}")
    assert lead is None, f"hotel_review must not create lead, got {lead.id if lead else None}"
    with SessionLocal() as db:
        bad = db.scalar(
            select(func.count())
            .select_from(Lead)
            .where(Lead.source.like("%hotel_review%"), Lead.is_deleted.is_(False))
        )
    print(f"Leads with source containing 'hotel_review': {bad}")
    assert bad == 0

    sep("5) No CRM auth on public form POSTs")
    assert form_post_headers, "No form-submissions POST captured from browser"
    for i, h in enumerate(form_post_headers, 1):
        print(f"  POST #{i}: authorization={h['authorization']!r} cookie={h['cookie']!r}")
        assert not h["authorization"], "Bearer token must not be sent from public website"
        assert not h.get("cookie") or "crm" not in (h.get("cookie") or "").lower()

    sep("7) Playwright console errors/warnings per form page")
    for key, items in console_by_form.items():
        errs = [x for x in items if x.startswith("[error]")]
        warns = [x for x in items if x.startswith("[warning]")]
        print(f"  {key}: errors={len(errs)} warnings={len(warns)}")
        for line in items[:5]:
            print(f"    {line}")

    sep("9) IP / inet handling")
    browser_sub = submission_for_tag("contact_consultation", email=f"{TEST_TAG}-contact@example.com")
    print(f"  Browser UI submission ip_address: {browser_sub.ip_address!r} (expect 127.0.0.1 or ::1)")

    from fastapi.testclient import TestClient
    from main import app

    tc = TestClient(app)
    r = tc.post(
        "/api/cms/public/form-submissions",
        json={
            "form_type": "contact_consultation",
            "name": f"{TEST_TAG} TestClient",
            "email": f"{TEST_TAG}-tc@example.com",
            "payload": {"message": "testclient ip probe"},
        },
    )
    assert r.status_code == 201, r.text
    with SessionLocal() as db:
        tc_sub = db.scalar(
            select(FormSubmission)
            .where(FormSubmission.email == f"{TEST_TAG}-tc@example.com")
            .order_by(FormSubmission.created_at.desc())
            .limit(1)
        )
    print(f"  TestClient submission ip_address: {tc_sub.ip_address!r} (expect None — not valid inet)")
    assert tc_sub.ip_address is None, "TestClient host must be stored as NULL, not crash"


def main() -> None:
    print(f"TEST_TAG = {TEST_TAG}")
    ensure_servers()
    run_ui_submissions()
    report_all_evidence()
    sep("DONE — all E2E checks passed")
    print(f"TEST_TAG = {TEST_TAG} (search CRM for this prefix)")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\nFAILED: {exc}", file=sys.stderr)
        raise
