#!/usr/bin/env python3
"""
Add composite indexes for common CMS list and homepage queries.

Run from api/: python scripts/migrate_performance_indexes.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import text

from database import engine

INDEX_STATEMENTS = [
    "CREATE INDEX IF NOT EXISTS ix_gallery_items_published_sort ON cms.gallery_items (is_published, sort_order)",
    "CREATE INDEX IF NOT EXISTS ix_client_stories_published_home_sort ON cms.client_stories (is_published, show_on_home, home_sort_order)",
    "CREATE INDEX IF NOT EXISTS ix_client_stories_published_gallery_sort ON cms.client_stories (is_published, show_in_gallery, gallery_sort_order)",
    "CREATE INDEX IF NOT EXISTS ix_packages_published_featured_sort ON cms.packages (is_published, featured_sort_order, title)",
    "CREATE INDEX IF NOT EXISTS ix_destinations_published_featured_sort ON cms.destinations (is_published, featured_sort_order, name)",
    "CREATE INDEX IF NOT EXISTS ix_itineraries_published_destination ON cms.itineraries (is_published, destination_id)",
    "CREATE INDEX IF NOT EXISTS ix_itineraries_published_package ON cms.itineraries (is_published, package_id)",
    "CREATE INDEX IF NOT EXISTS ix_experiences_homepage_sort ON cms.experiences (is_published, show_on_homepage, homepage_sort_order)",
    "CREATE INDEX IF NOT EXISTS ix_homepage_region_panels_active_sort ON cms.homepage_region_panels (is_active, sort_order)",
    "CREATE INDEX IF NOT EXISTS ix_media_assets_created_at ON cms.media_assets (created_at DESC)",
]


def main() -> None:
    with engine.begin() as connection:
        for statement in INDEX_STATEMENTS:
            connection.execute(text(statement))
    print("performance index migration complete.")


if __name__ == "__main__":
    main()
