#!/usr/bin/env python3
"""
Add homepage_region_panels.is_active for frontend visibility toggles.

Run: python scripts/migrate_homepage_region_panels_is_active.py
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
                ALTER TABLE cms.homepage_region_panels
                ADD COLUMN IF NOT EXISTS is_active BOOLEAN NOT NULL DEFAULT TRUE
                """
            )
        )
        connection.execute(
            text(
                """
                CREATE INDEX IF NOT EXISTS ix_homepage_region_panels_is_active
                ON cms.homepage_region_panels (is_active)
                """
            )
        )
    print("homepage_region_panels.is_active migration complete.")


if __name__ == "__main__":
    main()
