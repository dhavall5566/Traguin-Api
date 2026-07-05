#!/usr/bin/env python3
"""
Add package_mode to CRM leads (PRE_BUILT | CUSTOM).

Run: python scripts/migrate_crm_lead_package_mode.py
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
                ALTER TABLE crm.leads
                ADD COLUMN IF NOT EXISTS package_mode VARCHAR(16) NULL
                """
            )
        )
        print("  crm.leads.package_mode")
    print("Migration complete.")


if __name__ == "__main__":
    main()
