#!/usr/bin/env python3
"""
Add crm.leads.assignment_status and crm.leads.assigned_by_id for assignee accept/reject flow.

Run: python scripts/migrate_crm_lead_assignment_status.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import text

from database import CRM_SCHEMA, _physical_schema, crm_engine


def _table_ref() -> str:
    physical = _physical_schema(CRM_SCHEMA)
    return f"{physical}.leads" if physical else "leads"


def main() -> None:
    table = _table_ref()
    with crm_engine.begin() as connection:
        connection.execute(
            text(
                f"""
                ALTER TABLE {table}
                ADD COLUMN IF NOT EXISTS assignment_status VARCHAR(16) NULL
                """
            )
        )
        connection.execute(
            text(
                f"""
                ALTER TABLE {table}
                ADD COLUMN IF NOT EXISTS assigned_by_id UUID NULL
                """
            )
        )
        connection.execute(
            text(
                f"""
                DO $$
                BEGIN
                  IF NOT EXISTS (
                    SELECT 1 FROM pg_constraint
                    WHERE conname = 'fk_leads_assigned_by_id'
                  ) THEN
                    ALTER TABLE {table}
                    ADD CONSTRAINT fk_leads_assigned_by_id
                    FOREIGN KEY (assigned_by_id) REFERENCES users(id) ON DELETE SET NULL;
                  END IF;
                END $$;
                """
            )
        )
        connection.execute(
            text(
                f"""
                UPDATE {table}
                SET assignment_status = 'ACCEPTED'
                WHERE assigned_to_id IS NOT NULL
                  AND assignment_status IS NULL
                """
            )
        )
    print(f"Added {table}.assignment_status and {table}.assigned_by_id (if missing).")
    print("Migration complete.")


if __name__ == "__main__":
    main()
