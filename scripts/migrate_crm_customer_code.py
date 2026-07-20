#!/usr/bin/env python3
"""
Add permanent TG customer codes (TG2026070001).

Run: python scripts/migrate_crm_customer_code.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import text

from database import engine


def main() -> None:
    with engine.begin() as connection:
        connection.execute(
            text(
                """
                ALTER TABLE crm.customers
                ADD COLUMN IF NOT EXISTS customer_code VARCHAR(32) NULL
                """
            )
        )
        print("  crm.customers.customer_code column")

        connection.execute(
            text(
                """
                CREATE UNIQUE INDEX IF NOT EXISTS uq_customers_agency_customer_code
                ON crm.customers (agency_id, customer_code)
                WHERE customer_code IS NOT NULL
                """
            )
        )
        print("  unique index uq_customers_agency_customer_code")

    print("Migration complete.")


if __name__ == "__main__":
    main()
