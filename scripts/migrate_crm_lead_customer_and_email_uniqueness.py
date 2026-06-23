#!/usr/bin/env python3
"""
Migrate CRM schema:
1. Add leads.customer_id FK to customers
2. Replace global customers.email unique index with per-agency partial unique index

Run against live Neon: python scripts/migrate_crm_lead_customer_and_email_uniqueness.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import text

from database import engine


def check_within_agency_duplicate_emails(connection) -> list[tuple]:
    rows = connection.execute(
        text(
            """
            SELECT agency_id, lower(email) AS email, count(*) AS cnt
            FROM crm.customers
            WHERE is_deleted = false
            GROUP BY agency_id, lower(email)
            HAVING count(*) > 1
            ORDER BY cnt DESC
            """
        )
    ).fetchall()
    return [(str(r.agency_id), r.email, r.cnt) for r in rows]


def main() -> None:
    with engine.begin() as connection:
        dupes = check_within_agency_duplicate_emails(connection)
        if dupes:
            print("ERROR: within-agency duplicate emails among active customers:", file=sys.stderr)
            for agency_id, email, cnt in dupes:
                print(f"  agency={agency_id} email={email} count={cnt}", file=sys.stderr)
            sys.exit(1)

        print("Preflight OK: no within-agency duplicate active emails.")

        # leads.customer_id
        connection.execute(
            text(
                """
                ALTER TABLE crm.leads
                ADD COLUMN IF NOT EXISTS customer_id UUID NULL
                REFERENCES crm.customers(id) ON DELETE SET NULL
                """
            )
        )
        connection.execute(
            text(
                """
                CREATE INDEX IF NOT EXISTS ix_leads_customer_id
                ON crm.leads (customer_id)
                """
            )
        )
        print("Added crm.leads.customer_id (if missing).")

        # Drop legacy global unique email index (name from original model)
        connection.execute(text("DROP INDEX IF EXISTS crm.ix_customers_email"))
        print("Dropped crm.ix_customers_email (global unique) if present.")

        connection.execute(
            text(
                """
                CREATE UNIQUE INDEX IF NOT EXISTS uq_customers_agency_id_email
                ON crm.customers (agency_id, email)
                WHERE is_deleted = false
                """
            )
        )
        print("Created partial unique index uq_customers_agency_id_email (agency_id, email).")

    print("Migration complete.")


if __name__ == "__main__":
    main()
