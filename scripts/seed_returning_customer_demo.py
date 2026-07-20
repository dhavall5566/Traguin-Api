#!/usr/bin/env python3
"""Seed past travel / inquiry history for a returning-customer demo on a lead."""

from __future__ import annotations

import argparse
import sys
import uuid
from datetime import datetime, timedelta, timezone
from decimal import Decimal

from sqlalchemy import delete, select

from config import settings
from database import SessionLocal
from models.crm.bookings import Booking
from models.crm.customer_flags import CustomerFlag
from models.crm.customers import Customer
from models.crm.leads import Lead, LeadActivity, LeadNote
from services.customer_codes import ensure_customer_code
from services.customer_inquiry_history import build_customer_inquiry_history
from services.lead_codes import ensure_lead_code

DEMO_MARKER = "DUMMY_PAST_TRAVEL_DEMO"


def _utc(days_ago: int) -> datetime:
    return datetime.now(timezone.utc) - timedelta(days=days_ago)


def _find_lead(db, *, lead_code: str) -> Lead:
    lead = db.scalars(
        select(Lead).where(
            Lead.lead_code == lead_code,
            Lead.is_deleted.is_(False),
        )
    ).first()
    if lead is None:
        raise RuntimeError(f"Lead {lead_code!r} not found")
    return lead


def _existing_demo_leads(db, *, agency_id: uuid.UUID, customer_id: uuid.UUID) -> list[Lead]:
    return list(
        db.scalars(
            select(Lead).where(
                Lead.agency_id == agency_id,
                Lead.customer_id == customer_id,
                Lead.message == DEMO_MARKER,
                Lead.is_deleted.is_(False),
            )
        ).all()
    )


def _clear_demo_data(db, *, agency_id: uuid.UUID, customer_id: uuid.UUID) -> None:
    demo_leads = _existing_demo_leads(db, agency_id=agency_id, customer_id=customer_id)
    demo_lead_ids = [lead.id for lead in demo_leads]

    if demo_lead_ids:
        db.execute(delete(LeadNote).where(LeadNote.lead_id.in_(demo_lead_ids)))
        db.execute(delete(LeadActivity).where(LeadActivity.lead_id.in_(demo_lead_ids)))
        for lead in demo_leads:
            db.delete(lead)

    demo_bookings = list(
        db.scalars(
            select(Booking).where(
                Booking.agency_id == agency_id,
                Booking.customer_id == customer_id,
            )
        ).all()
    )
    for booking in demo_bookings:
        db.delete(booking)

    demo_flags = list(
        db.scalars(
            select(CustomerFlag).where(
                CustomerFlag.customer_id == customer_id,
                CustomerFlag.remark.like(f"{DEMO_MARKER}%"),
            )
        ).all()
    )
    for flag in demo_flags:
        db.delete(flag)

    db.flush()


def seed_returning_customer_demo(*, lead_code: str = "TRG003-PJ", refresh: bool = False) -> dict:
    agency_id = settings.traguin_default_agency_id
    system_user_id = settings.traguin_system_user_id
    if agency_id is None or system_user_id is None:
        raise RuntimeError("traguin_default_agency_id / traguin_system_user_id not configured")

    with SessionLocal() as db:
        current_lead = _find_lead(db, lead_code=lead_code)
        if current_lead.customer_id is None:
            raise RuntimeError(f"Lead {lead_code} is not linked to a customer profile")

        customer = db.get(Customer, current_lead.customer_id)
        if customer is None:
            raise RuntimeError("Linked customer record not found")

        ensure_customer_code(db, customer)

        existing = _existing_demo_leads(db, agency_id=agency_id, customer_id=customer.id)
        if existing and not refresh:
            history = build_customer_inquiry_history(
                db,
                agency_id=agency_id,
                phone=current_lead.phone,
                email=current_lead.email,
                customer_id=customer.id,
                current_lead_id=current_lead.id,
            )
            db.commit()
            return {
                "status": "already_seeded",
                "lead_code": lead_code,
                "customer_code": customer.customer_code,
                "total_inquiries": history.total_inquiry_count,
                "bookings": len(history.bookings),
                "demo_leads": [row.lead_code for row in existing],
            }

        if refresh and existing:
            _clear_demo_data(db, agency_id=agency_id, customer_id=customer.id)

        contact_email = customer.email
        contact_phone = customer.phone or current_lead.phone

        past_trips: list[dict] = [
            {
                "title": "Plan My Journey — Thailand",
                "destination": "Phuket & Krabi, Thailand",
                "status": "CLOSED",
                "value": Decimal("118500.00"),
                "source": "Website - plan_my_journey",
                "created_days_ago": 390,
                "note": (
                    "Completed Jul 2025 trip. Package included 5N Phuket + 2N Krabi, "
                    "private transfers, and island hopping. Guest requested Bali next time."
                ),
                "activity": "Trip completed successfully. Voucher and feedback collected.",
                "booking_status": "CLOSED",
            },
            {
                "title": "Plan My Journey — Singapore",
                "destination": "Singapore",
                "status": "DUMP_LEAD",
                "value": Decimal("0.00"),
                "source": "Website - plan_my_journey",
                "created_days_ago": 210,
                "note": "Budget mismatch on Sentosa package. Guest parked enquiry for later.",
                "activity": None,
                "booking_status": None,
            },
        ]

        created_leads: list[str] = []
        created_bookings = 0

        for trip in past_trips:
            created_at = _utc(trip["created_days_ago"])
            lead = Lead(
                agency_id=agency_id,
                title=trip["title"],
                first_name=customer.first_name,
                last_name=customer.last_name,
                email=contact_email,
                phone=contact_phone,
                status=trip["status"],
                value=trip["value"],
                source=trip["source"],
                travel_destination=trip["destination"],
                message=DEMO_MARKER,
                customer_id=customer.id,
                created_at=created_at,
                updated_at=created_at + timedelta(days=21),
            )
            db.add(lead)
            db.flush()
            ensure_lead_code(db, lead)
            created_leads.append(lead.lead_code or str(lead.id))

            if trip["note"]:
                db.add(
                    LeadNote(
                        lead_id=lead.id,
                        content=trip["note"],
                        created_by_id=system_user_id,
                        created_at=created_at + timedelta(days=4),
                    )
                )

            if trip["activity"]:
                db.add(
                    LeadActivity(
                        lead_id=lead.id,
                        type="STAGE_CHANGE",
                        description=trip["activity"],
                        created_by_id=system_user_id,
                        created_at=created_at + timedelta(days=28),
                    )
                )

            if trip["booking_status"]:
                booking = Booking(
                    agency_id=agency_id,
                    customer_id=customer.id,
                    status=trip["booking_status"],
                    created_at=created_at + timedelta(days=25),
                    updated_at=created_at + timedelta(days=25),
                )
                db.add(booking)
                db.flush()
                created_bookings += 1

        db.add(
            CustomerFlag(
                customer_id=customer.id,
                remark=(
                    f"{DEMO_MARKER}: Repeat guest — completed Thailand package in Jul 2025. "
                    "Prefers premium hotels and private transfers."
                ),
                created_by_id=system_user_id,
                created_at=_utc(14),
            )
        )

        history = build_customer_inquiry_history(
            db,
            agency_id=agency_id,
            phone=contact_phone,
            email=contact_email,
            customer_id=customer.id,
            current_lead_id=current_lead.id,
        )
        db.commit()

        return {
            "status": "refreshed" if refresh else "seeded",
            "lead_code": lead_code,
            "customer_code": customer.customer_code,
            "created_leads": created_leads,
            "created_bookings": created_bookings,
            "total_inquiries": history.total_inquiry_count,
            "inquiry_number": history.inquiry_number,
            "bookings": len(history.bookings),
            "flags": len(history.flags),
            "interactions": len(history.interactions),
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lead-code", default="TRG003-PJ")
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Replace existing demo history for this customer.",
    )
    args = parser.parse_args()
    try:
        result = seed_returning_customer_demo(lead_code=args.lead_code, refresh=args.refresh)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
