#!/usr/bin/env python3
"""
Download external/Pexels/ImageKit media URLs and store them on the API server.

Run from api/:
  python scripts/migrate_external_media_to_server.py
  python scripts/migrate_external_media_to_server.py --dry-run
  python scripts/migrate_external_media_to_server.py --base https://api.traguin.in
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import select

from config import settings
from database import SessionLocal
from models.media import MediaAsset
from services.media_upload import ingest_remote_image_url, is_local_media_url
from utils.db import commit_or_raise


def main() -> None:
    parser = argparse.ArgumentParser(description="Mirror external media_assets URLs to local uploads.")
    parser.add_argument("--dry-run", action="store_true", help="List rows only; do not download.")
    parser.add_argument(
        "--base",
        default=settings.api_public_base_url or "https://api.traguin.in",
        help="Public API base used in rewritten media URLs.",
    )
    args = parser.parse_args()
    base = args.base.rstrip("/")

    db = SessionLocal()
    try:
        rows = db.scalars(select(MediaAsset).order_by(MediaAsset.created_at)).all()
        pending = [row for row in rows if not is_local_media_url(row.url)]
        print(f"Found {len(pending)} external media asset(s) out of {len(rows)} total.")

        if args.dry_run:
            for row in pending[:20]:
                print(f"  - {row.id} [{row.source}] {row.url[:100]}")
            if len(pending) > 20:
                print(f"  ... and {len(pending) - 20} more")
            return

        migrated = 0
        failed = 0
        for index, row in enumerate(pending, start=1):
            try:
                _, mime_type, local_url = ingest_remote_image_url(row.url, request_base_url=base)
                row.url = local_url
                row.mime_type = mime_type or row.mime_type
                row.source = "upload"
                migrated += 1
                if index % 10 == 0 or index == len(pending):
                    print(f"  migrated {index}/{len(pending)}")
            except Exception as exc:
                failed += 1
                print(f"  FAILED {row.id}: {exc}")

        commit_or_raise(db)
        print(f"Done — migrated {migrated}, failed {failed}.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
