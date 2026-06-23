#!/usr/bin/env python3
"""Backfill empty last_name values on CRM leads and customers (website intake legacy rows)."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import select

from database import SessionLocal
from models.crm.customers import Customer
from models.crm.leads import Lead

FALLBACK_LAST_NAME = "Visitor"


def _is_empty_last_name(value: str | None) -> bool:
    return not (value or "").strip()


def main() -> None:
    with SessionLocal() as db:
        empty_leads = [
            lead
            for lead in db.scalars(select(Lead)).all()
            if _is_empty_last_name(lead.last_name)
        ]
        empty_customers = [
            customer
            for customer in db.scalars(select(Customer)).all()
            if _is_empty_last_name(customer.last_name)
        ]

        for lead in empty_leads:
            lead.last_name = FALLBACK_LAST_NAME
        for customer in empty_customers:
            customer.last_name = FALLBACK_LAST_NAME

        db.commit()
        print(f"Backfilled {len(empty_leads)} lead(s) and {len(empty_customers)} customer(s) to last_name={FALLBACK_LAST_NAME!r}.")


if __name__ == "__main__":
    main()
