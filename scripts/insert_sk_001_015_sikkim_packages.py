#!/usr/bin/env python3
"""Insert SK-001 through SK-015 Sikkim packages (no images, skip if exists)."""

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
from sikkim_domestic_batch_defs import SIKKIM_DOMESTIC_BUILDERS, SIKKIM_SLUG
from utils.db import commit_or_raise


def get_or_create_sikkim_destination(db) -> Destination:
    destination = db.scalar(select(Destination).where(Destination.slug == SIKKIM_SLUG))
    if destination is not None:
        print(f"Using destination: {destination.name} ({destination.id})")
        return destination

    destination = Destination(
        slug=SIKKIM_SLUG,
        name="Sikkim",
        country="India",
        region="domestic",
        india_region="northeast",
        description=(
            "Gangtok, Tsomgo Lake, Nathula Pass, Pelling, North Sikkim, Lachen, "
            "Lachung, Yumthang Valley, Gurudongmar Lake, and Himalayan monasteries."
        ),
        starting_price=0,
        moods=["Nature", "Family", "Luxury", "Adventure"],
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
        destination = get_or_create_sikkim_destination(db)
        dest_id = str(destination.id)

        for builder in SIKKIM_DOMESTIC_BUILDERS:
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
