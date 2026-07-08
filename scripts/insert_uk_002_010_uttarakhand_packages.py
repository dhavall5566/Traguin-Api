#!/usr/bin/env python3
"""Insert UK-002 through UK-010 Uttarakhand packages (no images, skip if exists)."""

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
from uk_batch_package_defs import UK_BUILDERS
from utils.db import commit_or_raise

UTTARAKHAND_SLUG = "uttarakhand"

UK_002_010_BUILDERS = UK_BUILDERS[1:]  # skip UK-001


def get_or_create_uttarakhand_destination(db) -> Destination:
    destination = db.scalar(select(Destination).where(Destination.slug == UTTARAKHAND_SLUG))
    if destination is not None:
        print(f"Using destination: {destination.name} ({destination.id})")
        return destination

    destination = Destination(
        slug=UTTARAKHAND_SLUG,
        name="Uttarakhand",
        country="India",
        region="domestic",
        india_region="north",
        description=(
            "Nainital, Mussoorie, Rishikesh, Haridwar, Auli, and the Char Dham — Himalayan lakes, "
            "hill stations, river spirituality, alpine meadows, and Devbhoomi's sacred pilgrimage circuits."
        ),
        starting_price=0,
        moods=["nature", "spiritual", "family", "adventure", "romantic", "luxury"],
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
        destination = get_or_create_uttarakhand_destination(db)
        dest_id = str(destination.id)

        for idx, builder in enumerate(UK_002_010_BUILDERS, start=2):
            package, itinerary = builder(dest_id)
            serial = f"UK-{idx:03d}"
            package = package.model_copy(update={"serial_code": serial, "destination_id": dest_id})
            itinerary = itinerary.model_copy(update={"destination_id": dest_id})
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
