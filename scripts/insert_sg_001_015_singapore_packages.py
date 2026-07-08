#!/usr/bin/env python3
"""Insert SG-001 through SG-015 Singapore packages (no images, skip if exists)."""

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
from models.destinations import Destination
from services.package_insert import insert_package_if_missing
from singapore_sg_001_015_batch_defs import SINGAPORE_SG_001_015_BUILDERS, SINGAPORE_SLUG
from utils.db import commit_or_raise


def get_or_create_singapore_destination(db) -> Destination:
    destination = db.scalar(select(Destination).where(Destination.slug == SINGAPORE_SLUG))
    if destination is not None:
        print(f"Using destination: {destination.name} ({destination.id})")
        return destination

    destination = Destination(
        slug=SINGAPORE_SLUG,
        name="Singapore",
        country="Singapore",
        region="international",
        india_region=None,
        description=(
            "Marina Bay, Sentosa, Gardens by the Bay, and Universal Studios — futuristic skylines, "
            "theme parks, luxury resorts, and world-class family and corporate experiences in Singapore."
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
        destination = get_or_create_singapore_destination(db)
        dest_id = str(destination.id)

        for builder in SINGAPORE_SG_001_015_BUILDERS:
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
