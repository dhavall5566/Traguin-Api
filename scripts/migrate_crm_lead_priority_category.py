#!/usr/bin/env python3
"""
Add crm.leads.priority and crm.leads.lead_category for CRM pipeline fields.

Run: python scripts/migrate_crm_lead_priority_category.py
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
                ADD COLUMN IF NOT EXISTS priority VARCHAR(16) NULL
                """
            )
        )
        connection.execute(
            text(
                f"""
                ALTER TABLE {table}
                ADD COLUMN IF NOT EXISTS lead_category VARCHAR(32) NULL
                """
            )
        )
    print(f"Added {table}.priority and {table}.lead_category (if missing).")
    print("Migration complete.")


if __name__ == "__main__":
    main()
