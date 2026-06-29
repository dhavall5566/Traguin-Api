#!/usr/bin/env python3
"""
Drop removed client story columns (slug, destination_label, trip_type, title, caption).

Run from api/: python scripts/migrate_client_stories_simplify.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import text

from database import engine


def main() -> None:
    with engine.begin() as connection:
        connection.execute(text("DROP INDEX IF EXISTS cms.ix_client_stories_slug"))
        connection.execute(text("ALTER TABLE cms.client_stories DROP COLUMN IF EXISTS slug"))
        connection.execute(
            text("ALTER TABLE cms.client_stories DROP COLUMN IF EXISTS destination_label")
        )
        connection.execute(text("ALTER TABLE cms.client_stories DROP COLUMN IF EXISTS trip_type"))
        connection.execute(text("ALTER TABLE cms.client_stories DROP COLUMN IF EXISTS title"))
        connection.execute(text("ALTER TABLE cms.client_stories DROP COLUMN IF EXISTS caption"))
    print("client_stories simplify migration complete.")


if __name__ == "__main__":
    main()
