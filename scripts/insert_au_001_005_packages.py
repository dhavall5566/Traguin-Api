#!/usr/bin/env python3
"""Insert AU-001 through AU-005 Australia packages (no images, skip if exists)."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR.parent) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR.parent))
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from australia_au_005_batch_defs import AU_005_BUILDERS, AUSTRALIA_SLUG
from au_batch_package_defs import AU_BUILDERS
from database import SessionLocal
from models.destinations import Destination
from services.package_insert import insert_package_if_missing
from utils.db import commit_or_raise

SERIALS = ["AU-001", "AU-002", "AU-003", "AU-004", "AU-005"]


def get_or_create_australia_destination(db) -> Destination:
    destination = db.scalar(select(Destination).where(Destination.slug == AUSTRALIA_SLUG))
    if destination is not None:
        print(f"Using destination: {destination.name} ({destination.id})")
        return destination

    destination = Destination(
        slug=AUSTRALIA_SLUG,
        name="Australia",
        country="Australia",
        region="international",
        india_region=None,
        description=(
            "Sydney, Melbourne, Cairns, the Great Barrier Reef, Whitsunday Islands, and the Gold Coast — "
            "iconic harbours, reef expeditions, rainforest retreats, and world-class family and honeymoon circuits."
        ),
        starting_price=0,
        moods=["family", "luxury", "romantic", "nature", "beach", "wildlife", "adventure"],
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
    builders = [*AU_BUILDERS, *AU_005_BUILDERS]

    with SessionLocal() as db:
        destination = get_or_create_australia_destination(db)
        dest_id = str(destination.id)

        for serial, builder in zip(SERIALS, builders, strict=True):
            package, itinerary = builder(dest_id)
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
