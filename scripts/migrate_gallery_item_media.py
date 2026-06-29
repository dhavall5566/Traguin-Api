#!/usr/bin/env python3
"""
Add gallery_item_media junction table and backfill from gallery_items.media_id.

Run from api/: python scripts/migrate_gallery_item_media.py
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
                CREATE TABLE IF NOT EXISTS cms.gallery_item_media (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    gallery_item_id UUID NOT NULL REFERENCES cms.gallery_items(id) ON DELETE CASCADE,
                    media_id UUID NOT NULL REFERENCES cms.media_assets(id) ON DELETE CASCADE,
                    sort_order INTEGER NOT NULL DEFAULT 0,
                    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
                )
                """
            )
        )
        connection.execute(
            text(
                """
                CREATE INDEX IF NOT EXISTS ix_gallery_item_media_gallery_item_id
                ON cms.gallery_item_media (gallery_item_id)
                """
            )
        )
        connection.execute(
            text(
                """
                CREATE INDEX IF NOT EXISTS ix_gallery_item_media_sort
                ON cms.gallery_item_media (gallery_item_id, sort_order)
                """
            )
        )
        connection.execute(
            text(
                """
                INSERT INTO cms.gallery_item_media (gallery_item_id, media_id, sort_order)
                SELECT gi.id, gi.media_id, 0
                FROM cms.gallery_items gi
                WHERE gi.media_id IS NOT NULL
                  AND NOT EXISTS (
                    SELECT 1
                    FROM cms.gallery_item_media gim
                    WHERE gim.gallery_item_id = gi.id
                      AND gim.media_id = gi.media_id
                  )
                """
            )
        )
        connection.execute(
            text(
                """
                ALTER TABLE cms.gallery_items
                ALTER COLUMN media_id DROP NOT NULL
                """
            )
        )
    print("gallery_item_media migration complete.")


if __name__ == "__main__":
    main()
