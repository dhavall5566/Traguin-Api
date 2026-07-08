#!/usr/bin/env python3
"""Insert JP-001 through JP-005 Japan packages (no images, skip if exists)."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR.parent) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR.parent))
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from database import SessionLocal
from japan_jp_001_005_batch_defs import JAPAN_JP_001_005_BUILDERS, JAPAN_SLUG
from models.destinations import Destination
from services.package_insert import insert_package_if_missing
from utils.db import commit_or_raise


def get_or_create_japan_destination(db) -> Destination:
    destination = db.scalar(select(Destination).where(Destination.slug == JAPAN_SLUG))
    if destination is not None:
        print(f"Using destination: {destination.name} ({destination.id})")
        return destination

    destination = Destination(
        slug=JAPAN_SLUG,
        name="Japan",
        country="Japan",
        region="international",
        india_region=None,
        description=(
            "Tokyo, Kyoto, Osaka, Mt. Fuji, and Hakone — ancient shrines, bullet trains, neon cityscapes, "
            "onsen retreats, and world-class luxury for families, couples, and discerning travelers."
        ),
        starting_price=0,
        moods=["Family", "Luxury", "Romantic", "Culture", "Nature", "Adventure"],
        is_published=True,
    )
    db.add(destination)
    db.flush()
    commit_or_raise(db)
    print(f"Created destination: {destination.slug} ({destination.id})")
    return destination


def main() -> None:
    inserted = 0
    skipped = 0

    with SessionLocal() as db:
        destination = get_or_create_japan_destination(db)
        dest_id = str(destination.id)

        for builder in JAPAN_JP_001_005_BUILDERS:
            package, itinerary = builder(dest_id)
            serial = package.serial_code or package.slug
            print(f"\n--- {serial} | {package.slug} ---")
            try:
                result = insert_package_if_missing(
                    db,
                    destination_id=dest_id,
                    package=package,
                    itinerary=itinerary,
                )
                if result is None:
                    skipped += 1
                else:
                    inserted += 1
            except Exception as exc:
                print(f"Failed {package.slug}: {exc}", file=sys.stderr)
                raise

    print(f"\nDone. Inserted: {inserted}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
