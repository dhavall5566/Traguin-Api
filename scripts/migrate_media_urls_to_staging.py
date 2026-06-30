#!/usr/bin/env python3
"""
Rewrite localhost media asset URLs to the staging API base.

Run from api/: python scripts/migrate_media_urls_to_staging.py
Optional: python scripts/migrate_media_urls_to_staging.py --base https://api.traguin.in
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import text

from database import engine

DEFAULT_STAGING_BASE = "https://api.traguin.in"

LOCALHOST_PREFIXES = (
    "http://127.0.0.1:8001",
    "http://localhost:8001",
    "https://127.0.0.1:8001",
    "https://localhost:8001",
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Rewrite localhost media URLs to staging API base.")
    parser.add_argument(
        "--base",
        default=DEFAULT_STAGING_BASE,
        help=f"Target API base URL (default: {DEFAULT_STAGING_BASE})",
    )
    args = parser.parse_args()
    target_base = args.base.rstrip("/")

    total_updated = 0
    with engine.begin() as connection:
        for prefix in LOCALHOST_PREFIXES:
            result = connection.execute(
                text(
                    """
                    UPDATE cms.media_assets
                    SET url = :target_base || substring(url from char_length(:prefix) + 1),
                        updated_at = now()
                    WHERE url LIKE :prefix || '%'
                    """
                ),
                {"target_base": target_base, "prefix": prefix},
            )
            count = result.rowcount or 0
            if count:
                print(f"  {prefix} -> {target_base}: {count} row(s)")
                total_updated += count

    print(f"media_assets URL migration complete ({total_updated} row(s) updated).")


if __name__ == "__main__":
    main()
