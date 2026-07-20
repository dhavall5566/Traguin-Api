"""Permanent TG customer IDs assigned on first booking."""

from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.crm.customers import Customer
from utils.lead_codes import CUSTOMER_CODE_RE, format_customer_code


def _current_year_month() -> str:
    now = datetime.now(timezone.utc)
    return now.strftime("%Y%m")


def next_customer_sequence(db: Session, agency_id: UUID, year_month: str | None = None) -> int:
    ym = year_month or _current_year_month()
    prefix = f"TG{ym}"
    codes = db.scalars(
        select(Customer.customer_code).where(
            Customer.agency_id == agency_id,
            Customer.customer_code.isnot(None),
            Customer.customer_code.like(f"{prefix}%"),
        )
    ).all()
    max_seq = 0
    for code in codes:
        match = CUSTOMER_CODE_RE.match(code or "")
        if match and match.group(1) == ym:
            max_seq = max(max_seq, int(match.group(2)))
    return max_seq + 1


def assign_customer_code(db: Session, customer: Customer, *, year_month: str | None = None) -> str:
    if customer.customer_code:
        return customer.customer_code
    ym = year_month or _current_year_month()
    sequence = next_customer_sequence(db, customer.agency_id, ym)
    customer.customer_code = format_customer_code(ym, sequence)
    db.flush()
    return customer.customer_code


def ensure_customer_code(db: Session, customer: Customer) -> str:
    if customer.customer_code:
        return customer.customer_code
    return assign_customer_code(db, customer)


def ensure_customer_code_by_id(db: Session, customer_id: UUID, agency_id: UUID) -> str | None:
    customer = db.get(Customer, customer_id)
    if customer is None or customer.agency_id != agency_id or customer.is_deleted:
        return None
    return ensure_customer_code(db, customer)
