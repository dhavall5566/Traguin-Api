#!/usr/bin/env python3
"""Insert UP-002 through UP-010 Uttar Pradesh packages (no images, skip if exists)."""

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
from uttar_pradesh_up_002_010_batch_defs import UTTAR_PRADESH_SLUG, UTTAR_PRADESH_UP_002_010_BUILDERS


def get_or_create_uttar_pradesh_destination(db) -> Destination:
    destination = db.scalar(select(Destination).where(Destination.slug == UTTAR_PRADESH_SLUG))
    if destination is not None:
        print(f"Using destination: {destination.name} ({destination.id})")
        return destination

    destination = Destination(
        slug=UTTAR_PRADESH_SLUG,
        name="Uttar Pradesh",
        country="India",
        region="domestic",
        india_region="north",
        description=(
            "Varanasi, Ayodhya, Prayagraj, Lucknow, Agra, Mathura, Vrindavan — sacred ghats, "
            "Mughal monuments, Nawabi heritage, and India's spiritual heartland."
        ),
        starting_price=0,
        moods=["Family", "Luxury", "Culture", "Spiritual"],
        is_published=True,
    )
    db.add(destination)
    db.flush()
    from utils.db import commit_or_raise

    commit_or_raise(db)
    print(f"Created destination: {destination.slug} ({destination.id})")
    return destination


def main() -> None:
    inserted = 0
    skipped = 0

    with SessionLocal() as db:
        destination = get_or_create_uttar_pradesh_destination(db)
        dest_id = str(destination.id)

        for builder in UTTAR_PRADESH_UP_002_010_BUILDERS:
            package, itinerary = builder(dest_id)
            print(f"\n--- {package.serial_code} | {package.slug} ---")
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
