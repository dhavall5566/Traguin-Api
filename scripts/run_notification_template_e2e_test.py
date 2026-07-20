#!/usr/bin/env python3
"""E2E notification template test — one record, all 18 templates, then cleanup."""

from __future__ import annotations

import sys
import time
import uuid
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal

from sqlalchemy import delete, select

from config import settings
from database import SessionLocal
from models.crm.bookings import Booking
from models.crm.customers import Customer
from models.crm.finance import Invoice, Payment
from models.crm.leads import Lead, LeadActivity, LeadFollowup, LeadNote
from models.crm.tenancy import User
from services.customer_codes import ensure_customer_code
from services.lead_assignment import ASSIGNMENT_PENDING, apply_assignment_on_assign
from services.lead_codes import ensure_lead_code
from services.notification_matrix import dispatch_lead_matrix_event
from services.notification_templates.catalog import TEMPLATE_IDS
from services.notification_templates.context import (
    build_booking_context,
    build_invoice_context,
    build_lead_context,
)
from services.notification_templates.delivery import (
    send_templated_email,
    send_templated_whatsapp,
)
from services.email_notifications import notify_lead_assigned_email_by_id
from services.whatsapp_notifications import (
    notify_invoice_created_by_id,
    notify_payment_received_by_id,
)

TEST_EMAIL = "nicksofficialindia@gmail.com"
TEST_PHONE = "+91 9913135371"
TEST_MARKER = "NOTIF_TEMPLATE_E2E"
DEDUPE_WAIT = 4  # brief pause between sends (matrix dedupe bypassed via unique suffix)


def _log(msg: str) -> None:
    print(msg, flush=True)


def _find_rm_user(db, agency_id: uuid.UUID) -> User:
    user = db.scalar(
        select(User).where(
            User.agency_id == agency_id,
            User.is_deleted.is_(False),
            User.email == TEST_EMAIL,
        )
    )
    if user is None:
        raise RuntimeError(f"RM user with email {TEST_EMAIL} not found in agency {agency_id}")
    return user


def _send_direct(
    db,
    *,
    agency_id: uuid.UUID,
    template_id: str,
    variables: dict[str, str],
    label: str,
) -> None:
    _log(f"  → {label} ({template_id})")
    email_ok = send_templated_email(
        db,
        agency_id=agency_id,
        to_email=TEST_EMAIL,
        template_id=template_id,
        variables=variables,
    )
    wa_ok = send_templated_whatsapp(TEST_PHONE, template_id, variables)
    _log(f"     email={'sent' if email_ok else 'skipped'} whatsapp={'sent' if wa_ok else 'skipped'}")


def _cleanup_test_data(db, *, lead_id: uuid.UUID | None, customer_id: uuid.UUID | None) -> None:
    if lead_id:
        db.execute(delete(LeadActivity).where(LeadActivity.lead_id == lead_id))
        db.execute(delete(LeadNote).where(LeadNote.lead_id == lead_id))
        db.execute(delete(LeadFollowup).where(LeadFollowup.lead_id == lead_id))
        lead = db.get(Lead, lead_id)
        if lead:
            db.delete(lead)
    if customer_id:
        booking_ids = list(
            db.scalars(select(Booking.id).where(Booking.customer_id == customer_id)).all()
        )
        for booking_id in booking_ids:
            invoice_ids = list(
                db.scalars(select(Invoice.id).where(Invoice.booking_id == booking_id)).all()
            )
            for invoice_id in invoice_ids:
                db.execute(delete(Payment).where(Payment.invoice_id == invoice_id))
                inv = db.get(Invoice, invoice_id)
                if inv:
                    db.delete(inv)
            booking = db.get(Booking, booking_id)
            if booking:
                db.delete(booking)
        customer = db.get(Customer, customer_id)
        if customer:
            db.delete(customer)
    db.commit()
    _log("Cleanup complete — test lead, customer, booking, invoice, and payment removed.")


def run() -> int:
    agency_id = settings.traguin_default_agency_id
    system_user_id = settings.traguin_system_user_id
    if agency_id is None or system_user_id is None:
        _log("ERROR: traguin_default_agency_id / traguin_system_user_id not configured.")
        return 1

    db = SessionLocal()
    lead_id: uuid.UUID | None = None
    customer_id: uuid.UUID | None = None

    try:
        rm_user = _find_rm_user(db, agency_id)
        _log(f"Using RM: {rm_user.name} ({rm_user.email})")

        # Remove any leftover test records from a prior failed run
        old_leads = db.scalars(
            select(Lead).where(
                Lead.agency_id == agency_id,
                Lead.message == TEST_MARKER,
            )
        ).all()
        for old in old_leads:
            _cleanup_test_data(db, lead_id=old.id, customer_id=old.customer_id)

        customer = Customer(
            agency_id=agency_id,
            first_name="Nikunj",
            last_name="TemplateTest",
            email=TEST_EMAIL,
            phone=TEST_PHONE,
        )
        db.add(customer)
        db.flush()
        customer_id = customer.id
        ensure_customer_code(db, customer)

        travel_start = date.today() + timedelta(days=30)
        travel_end = travel_start + timedelta(days=6)

        lead = Lead(
            agency_id=agency_id,
            title=f"{TEST_MARKER} — Bali Getaway",
            first_name="Nikunj",
            last_name="TemplateTest",
            email=TEST_EMAIL,
            phone=TEST_PHONE,
            status="NEW",
            value=Decimal("125000.00"),
            source="WEB",
            priority="high",
            travel_destination="Bali, Indonesia",
            travel_date=travel_start,
            arrival_date=travel_end,
            adults_count=2,
            children_count=0,
            travel_type="Honeymoon",
            message=TEST_MARKER,
            customer_id=customer.id,
        )
        db.add(lead)
        db.flush()
        lead_id = lead.id
        ensure_lead_code(db, lead)
        db.commit()
        db.refresh(lead)
        db.refresh(customer)

        _log(f"\nCreated test lead {lead.lead_code} (customer {customer.customer_code})")
        ctx = build_lead_context(db, lead, rm_user=rm_user)

        results: list[str] = []

        def matrix(event: str, **kwargs) -> None:
            counts = dispatch_lead_matrix_event(db, event, lead, dedupe_suffix=str(time.time()), **kwargs)
            _log(f"  → matrix {event}: {counts}")
            results.append(event)

        # 1–2: new lead + team alert
        _log("\n[1] New lead")
        matrix("new_lead")
        time.sleep(DEDUPE_WAIT)

        # 3: assign to RM
        _log("\n[2] Assign to RM")
        apply_assignment_on_assign(
            db,
            lead,
            assignee_id=rm_user.id,
            actor_id=system_user_id,
            agency_id=agency_id,
        )
        lead.assigned_by_id = system_user_id
        db.commit()
        db.refresh(lead)
        matrix("assigned_to_rm")
        notify_lead_assigned_email_by_id(lead.id)
        time.sleep(DEDUPE_WAIT)

        # 4–6: escalation / reminder templates (direct)
        _log("\n[3] RM reminders & escalation (direct)")
        for tid, label, extra in (
            ("team_rm_accept_reminder", "RM accept reminder", {"Elapsed_Time": "15 minutes"}),
            ("team_no_action_after_accept", "No action after accept", {}),
            (
                "team_escalation",
                "Escalation alert",
                {
                    "Escalation_Level": "Tier 3 — Admin alert",
                    "Escalation_Message": "Test escalation — RM did not accept within working hours.",
                    "Elapsed_Time": "45 minutes",
                },
            ),
        ):
            vars_ = {**ctx, **extra}
            _send_direct(db, agency_id=agency_id, template_id=tid, variables=vars_, label=label)
            time.sleep(3)

        # 7: itinerary
        _log("\n[4] Itinerary sent")
        lead.status = "ITINERARY_SENT"
        lead.proposal_sent_at = datetime.now(timezone.utc)
        db.commit()
        ctx = build_lead_context(db, lead, rm_user=rm_user)
        ctx["Nights"] = "6"
        matrix("itinerary_sent")
        time.sleep(DEDUPE_WAIT)

        # 8: quote
        _log("\n[5] Quote approved")
        lead.status = "APPROVED"
        ctx["Quote_Valid_Till"] = (date.today() + timedelta(days=7)).strftime("%d %b %Y")
        db.commit()
        matrix("quote_approved")
        time.sleep(DEDUPE_WAIT)

        # 9–10: booking
        _log("\n[6] Booking confirmed")
        booking = Booking(
            agency_id=agency_id,
            customer_id=customer.id,
            status="CONFIRMED",
        )
        db.add(booking)
        db.flush()
        lead.status = "BOOKED"
        db.commit()
        db.refresh(booking)
        booking_ctx = build_booking_context(db, booking, lead=lead)
        matrix("booking_confirmed")
        time.sleep(DEDUPE_WAIT)

        # 11–12: invoice + overdue
        _log("\n[7] Invoice & payment overdue")
        invoice = Invoice(
            agency_id=agency_id,
            booking_id=booking.id,
            invoice_number=f"TEST-INV-{int(time.time())}",
            amount=Decimal("62500.00"),
            due_date=datetime.now(timezone.utc) - timedelta(days=2),
            status="UNPAID",
        )
        db.add(invoice)
        db.commit()
        db.refresh(invoice)
        invoice_ctx = build_invoice_context(db, invoice, lead=lead)
        notify_invoice_created_by_id(invoice.id)
        time.sleep(5)
        matrix("payment_overdue", variables=invoice_ctx)
        time.sleep(DEDUPE_WAIT)

        # 13: payment receipt
        _log("\n[8] Payment received")
        payment = Payment(
            agency_id=agency_id,
            invoice_id=invoice.id,
            amount=Decimal("62500.00"),
            payment_method="UPI",
            transaction_reference=f"TEST-{int(time.time())}",
            payment_date=datetime.now(timezone.utc),
        )
        db.add(payment)
        invoice.status = "PAID"
        db.commit()
        notify_payment_received_by_id(payment.id)
        time.sleep(5)

        # 14–15: travel docs & pre-departure (not cron-wired)
        _log("\n[9] Travel docs & pre-departure (direct)")
        travel_ctx = {
            **booking_ctx,
            "Docs_Link": f"{settings.whatsapp_crm_base_url or 'http://localhost:3002'}/dashboard/operations",
            "Days_Left": "7",
        }
        _send_direct(
            db,
            agency_id=agency_id,
            template_id="customer_travel_documents",
            variables=travel_ctx,
            label="Travel documents",
        )
        time.sleep(3)
        _send_direct(
            db,
            agency_id=agency_id,
            template_id="customer_pre_departure",
            variables=travel_ctx,
            label="Pre-departure",
        )
        time.sleep(3)

        # 16: dump lead (direct)
        _log("\n[10] Dump lead alert (direct)")
        dump_ctx = {
            **ctx,
            "Attempt_Count": "3",
            "Last_Attempt_Date": date.today().strftime("%d %b %Y"),
        }
        _send_direct(
            db,
            agency_id=agency_id,
            template_id="team_dump_lead",
            variables=dump_ctx,
            label="Dump lead",
        )
        time.sleep(3)

        # 17: trip complete
        _log("\n[11] Trip complete")
        lead.status = "CLOSED"
        db.commit()
        matrix("booking_closed")
        time.sleep(DEDUPE_WAIT)

        _log(f"\n✓ Test run finished — triggered {len(TEMPLATE_IDS)} template types.")
        _log(f"  Check {TEST_EMAIL} and WhatsApp {TEST_PHONE}")
        _log("  Templates covered: " + ", ".join(TEMPLATE_IDS))

    except Exception as exc:
        db.rollback()
        _log(f"\nERROR during test: {exc}")
        import traceback

        traceback.print_exc()
        return 1
    finally:
        try:
            _cleanup_test_data(db, lead_id=lead_id, customer_id=customer_id)
        except Exception as cleanup_exc:
            _log(f"Cleanup error: {cleanup_exc}")
        db.close()

    return 0


if __name__ == "__main__":
    sys.exit(run())
