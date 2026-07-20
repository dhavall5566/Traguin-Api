#!/usr/bin/env python3
"""
Create crm.customer_flags for internal customer remark flags.

Run: python scripts/migrate_crm_customer_flags.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import text

from database import CRM_SCHEMA, _physical_schema, crm_engine


def _table_ref(name: str) -> str:
    physical = _physical_schema(CRM_SCHEMA)
    return f"{physical}.{name}" if physical else name


def main() -> None:
    flags = _table_ref("customer_flags")
    customers = _table_ref("customers")
    users = _table_ref("users")

    with crm_engine.begin() as connection:
        connection.execute(
            text(
                f"""
                CREATE TABLE IF NOT EXISTS {flags} (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    customer_id UUID NOT NULL REFERENCES {customers}(id) ON DELETE CASCADE,
                    remark TEXT NOT NULL,
                    created_by_id UUID NOT NULL REFERENCES {users}(id) ON DELETE CASCADE,
                    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
                )
                """
            )
        )
        connection.execute(
            text(
                f"""
                CREATE INDEX IF NOT EXISTS ix_customer_flags_customer_id
                ON {flags} (customer_id)
                """
            )
        )
    print(f"Ensured {flags} table exists.")
    print("Migration complete.")


if __name__ == "__main__":
    main()
