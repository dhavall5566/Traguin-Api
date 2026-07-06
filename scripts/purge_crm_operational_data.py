"""
Purge CRM operational data while preserving workspace configuration.

KEPT:
  - agencies, users, roles, permissions, role_permissions, user_roles (Team access)
  - agency_smtp_settings, agency_lead_mail_settings, agency_lead_mail_recipients (Email setup)

REMOVED:
  - leads (+ notes, activities, followups), customers, bookings, itineraries,
    vendors, finance records, audit logs

CMS packages (Packages tab) live in the CMS database and are not touched.

Run:
  python scripts/purge_crm_operational_data.py --confirm
  python scripts/purge_crm_operational_data.py --confirm --agency-id <uuid>
"""

from __future__ import annotations

import argparse
import sys
from uuid import UUID

from sqlalchemy import delete, func, select
from sqlalchemy.orm import Session

from database import SessionLocal, crm_engine
from models.crm.audit import AuditLog
from models.crm.bookings import Booking
from models.crm.customers import Customer
from models.crm.finance import Expense, Invoice, Payment, Quotation, VendorPayout
from models.crm.itineraries import Itinerary, ItineraryDay, ItineraryItem
from models.crm.leads import Lead, LeadActivity, LeadFollowup, LeadNote
from models.crm.vendors import Vendor, VendorPackage, VendorRate, VendorService

_PURGE_MODELS: tuple[type, ...] = (
    Payment,
    Invoice,
    VendorPayout,
    Expense,
    Quotation,
    Booking,
    LeadFollowup,
    LeadActivity,
    LeadNote,
    Lead,
    ItineraryItem,
    ItineraryDay,
    Itinerary,
    VendorRate,
    VendorService,
    VendorPackage,
    Vendor,
    Customer,
    AuditLog,
)


def _count(db: Session, model: type, agency_id: UUID | None) -> int:
    query = select(func.count()).select_from(model)
    if agency_id is not None and hasattr(model, "agency_id"):
        query = query.where(model.agency_id == agency_id)
    return int(db.scalar(query) or 0)


def purge_crm_operational_data(db: Session, *, agency_id: UUID | None = None) -> dict[str, int]:
    before = {model.__tablename__: _count(db, model, agency_id) for model in _PURGE_MODELS}

    for model in _PURGE_MODELS:
        stmt = delete(model)
        if agency_id is not None and hasattr(model, "agency_id"):
            stmt = stmt.where(model.agency_id == agency_id)
        db.execute(stmt)

    db.commit()

    after = {model.__tablename__: _count(db, model, agency_id) for model in _PURGE_MODELS}
    return {table: before[table] - after[table] for table in before}


def main() -> int:
    parser = argparse.ArgumentParser(description="Purge CRM operational data (keep team + email setup).")
    parser.add_argument(
        "--confirm",
        action="store_true",
        help="Required flag — actually delete data.",
    )
    parser.add_argument(
        "--agency-id",
        type=UUID,
        default=None,
        help="Limit purge to one agency (default: all agencies).",
    )
    args = parser.parse_args()

    if not args.confirm:
        print("Refusing to run without --confirm.", file=sys.stderr)
        return 1

    scope = f"agency {args.agency_id}" if args.agency_id else "all agencies"
    print(f"Purging CRM operational data for {scope} on {crm_engine.url.render_as_string(hide_password=True)}")

    db = SessionLocal()
    try:
        removed = purge_crm_operational_data(db, agency_id=args.agency_id)
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

    total = 0
    for table, count in removed.items():
        if count:
            print(f"  {table}: removed {count}")
            total += count
    print(f"Done — {total} row(s) removed across {sum(1 for c in removed.values() if c)} table(s).")
    print("Preserved: agencies, users, roles, permissions, SMTP + email alert settings.")
    print("CMS packages unchanged (Packages tab).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
