#!/usr/bin/env python3
"""Insert NL-001 through NL-010 Nagaland packages (no images, skip if exists)."""

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
from nagaland_domestic_batch_defs import NAGALAND_DOMESTIC_BUILDERS, NAGALAND_SLUG
from models.destinations import Destination
from services.package_insert import insert_package_if_missing
from utils.db import commit_or_raise


def get_or_create_nagaland_destination(db) -> Destination:
    destination = db.scalar(select(Destination).where(Destination.slug == NAGALAND_SLUG))
    if destination is not None:
        print(f"Using destination: {destination.name} ({destination.id})")
        return destination

    destination = Destination(
        slug=NAGALAND_SLUG,
        name="Nagaland",
        country="India",
        region="domestic",
        india_region="northeast",
        description=(
            "Kohima, Dimapur, Khonoma, Dzukou Valley, Hornbill Festival, Mokokchung, "
            "Tuophema, and Naga tribal heritage."
        ),
        starting_price=0,
        moods=["Culture", "Adventure", "Family", "Luxury"],
        is_published=False,
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
        destination = get_or_create_nagaland_destination(db)
        dest_id = str(destination.id)

        for builder in NAGALAND_DOMESTIC_BUILDERS:
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
