#!/usr/bin/env python3
"""
Add packages.sold_last_month for homepage "Sold in the last month" display.

Run: python scripts/migrate_packages_sold_last_month.py
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
                ALTER TABLE cms.packages
                ADD COLUMN IF NOT EXISTS sold_last_month INTEGER NOT NULL DEFAULT 0
                """
            )
        )
    print("packages.sold_last_month migration complete.")


if __name__ == "__main__":
    main()
