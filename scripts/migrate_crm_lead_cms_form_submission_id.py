#!/usr/bin/env python3
"""
Link CRM leads back to CMS form submissions (cross-schema reference).

Run: python scripts/migrate_crm_lead_cms_form_submission_id.py
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
                ADD COLUMN IF NOT EXISTS cms_form_submission_id UUID NULL
                """
            )
        )
        connection.execute(
            text(
                """
                CREATE INDEX IF NOT EXISTS ix_leads_cms_form_submission_id
                ON crm.leads (cms_form_submission_id)
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
                        WHERE conname = 'fk_leads_cms_form_submission_id'
                    ) THEN
                        ALTER TABLE crm.leads
                        ADD CONSTRAINT fk_leads_cms_form_submission_id
                        FOREIGN KEY (cms_form_submission_id)
                        REFERENCES cms.form_submissions (id)
                        ON DELETE SET NULL;
                    END IF;
                END $$
                """
            )
        )
        print("  crm.leads.cms_form_submission_id (+ FK → cms.form_submissions)")


if __name__ == "__main__":
    main()
