#!/usr/bin/env python3
"""
Remove short-film support from client_stories (rows, columns).

Run from api/: python scripts/migrate_remove_client_story_films.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import text

from database import engine


def main() -> None:
    with engine.begin() as connection:
        connection.execute(text("DELETE FROM cms.client_stories WHERE is_film IS TRUE"))
        connection.execute(
            text("ALTER TABLE cms.client_stories DROP COLUMN IF EXISTS is_film")
        )
        connection.execute(
            text("ALTER TABLE cms.client_stories DROP COLUMN IF EXISTS video_url")
        )
        connection.execute(
            text("ALTER TABLE cms.client_stories DROP COLUMN IF EXISTS poster_media_id")
        )
    print("client_stories short-film migration complete.")


if __name__ == "__main__":
    main()
