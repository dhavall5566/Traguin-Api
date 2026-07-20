#!/usr/bin/env python3
"""
Add assignment timer columns on crm.leads for RM accept escalation.

Run: python scripts/migrate_crm_lead_assignment_timers.py
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
                ADD COLUMN IF NOT EXISTS assigned_at TIMESTAMPTZ NULL
                """
            )
        )
        connection.execute(
            text(
                f"""
                ALTER TABLE {table}
                ADD COLUMN IF NOT EXISTS assignment_accepted_at TIMESTAMPTZ NULL
                """
            )
        )
        connection.execute(
            text(
                f"""
                ALTER TABLE {table}
                ADD COLUMN IF NOT EXISTS assignment_escalation_level INTEGER NOT NULL DEFAULT 0
                """
            )
        )
        connection.execute(
            text(
                f"""
                ALTER TABLE {table}
                ADD COLUMN IF NOT EXISTS accept_inactivity_notified BOOLEAN NOT NULL DEFAULT FALSE
                """
            )
        )
        connection.execute(
            text(
                f"""
                UPDATE {table}
                SET assigned_at = updated_at
                WHERE assignment_status = 'PENDING'
                  AND assigned_to_id IS NOT NULL
                  AND assigned_at IS NULL
                """
            )
        )
        connection.execute(
            text(
                f"""
                UPDATE {table}
                SET assignment_accepted_at = updated_at
                WHERE assignment_status = 'ACCEPTED'
                  AND assigned_to_id IS NOT NULL
                  AND assignment_accepted_at IS NULL
                """
            )
        )
    print(f"Added assignment timer columns on {table} (if missing).")
    print("Migration complete.")


if __name__ == "__main__":
    main()
