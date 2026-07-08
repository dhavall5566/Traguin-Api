#!/usr/bin/env python3
"""Insert ID-001 through ID-020 Bali packages (no images, skip if exists)."""

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
from indonesia_id_001_020_batch_defs import BALI_SLUG, INDONESIA_ID_001_020_BUILDERS
from models.destinations import Destination
from services.package_insert import insert_package_if_missing
from utils.db import commit_or_raise


def get_or_create_bali_destination(db) -> Destination:
    destination = db.scalar(select(Destination).where(Destination.slug == BALI_SLUG))
    if destination is not None:
        print(f"Using destination: {destination.name} ({destination.id})")
        return destination

    destination = Destination(
        slug=BALI_SLUG,
        name="Bali",
        country="Indonesia",
        region="international",
        india_region=None,
        description=(
            "Ubud, Seminyak, Uluwatu, Nusa Penida, and the Island of the Gods — rice terraces, "
            "temple culture, luxury villas, and world-class beach resorts for families, couples, and adventurers."
        ),
        starting_price=0,
        moods=["Family", "Luxury", "Honeymoon", "Beach", "Culture", "Adventure", "Nature"],
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
        destination = get_or_create_bali_destination(db)
        dest_id = str(destination.id)

        for builder in INDONESIA_ID_001_020_BUILDERS:
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
