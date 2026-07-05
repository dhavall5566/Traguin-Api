#!/usr/bin/env python3
"""
Link CRM leads to CMS packages (cross-schema reference).

Run: python scripts/migrate_crm_lead_cms_package_id.py
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
                ADD COLUMN IF NOT EXISTS cms_package_id UUID NULL
                """
            )
        )
        connection.execute(
            text(
                """
                CREATE INDEX IF NOT EXISTS ix_leads_cms_package_id
                ON crm.leads (cms_package_id)
                """
            )
        )
        connection.execute(
            text(
                """
                DO $$
                BEGIN
                    IF NOT EXISTS (
                        SELECT 1 FROM pg_constraint
                        WHERE conname = 'fk_leads_cms_package_id'
                    ) THEN
                        ALTER TABLE crm.leads
                        ADD CONSTRAINT fk_leads_cms_package_id
                        FOREIGN KEY (cms_package_id)
                        REFERENCES cms.packages (id)
                        ON DELETE SET NULL;
                    END IF;
                END $$
                """
            )
        )
        print("  crm.leads.cms_package_id (+ FK → cms.packages)")


if __name__ == "__main__":
    main()
