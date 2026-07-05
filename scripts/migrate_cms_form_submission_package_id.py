#!/usr/bin/env python3
"""
Add related_package_id to cms.form_submissions (FK → cms.packages).

Run: python scripts/migrate_cms_form_submission_package_id.py
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
                ALTER TABLE cms.form_submissions
                ADD COLUMN IF NOT EXISTS related_package_id UUID NULL
                """
            )
        )
        connection.execute(
            text(
                """
                CREATE INDEX IF NOT EXISTS ix_form_submissions_related_package_id
                ON cms.form_submissions (related_package_id)
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
                        WHERE conname = 'fk_form_submissions_related_package_id'
                    ) THEN
                        ALTER TABLE cms.form_submissions
                        ADD CONSTRAINT fk_form_submissions_related_package_id
                        FOREIGN KEY (related_package_id)
                        REFERENCES cms.packages (id)
                        ON DELETE SET NULL;
                    END IF;
                END $$
                """
            )
        )
        print("  cms.form_submissions.related_package_id (+ FK → cms.packages)")


if __name__ == "__main__":
    main()
