#!/usr/bin/env python3
"""Insert LK-009 (skip if exists), skip MP-006/CH-006, insert MP-011 through MP-015."""

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
from lakshadweep_lk_batch_defs import LAKSHADWEEP_DESTINATION_ID, build_lk_009
from madhya_pradesh_domestic_batch_defs import MADHYA_PRADESH_DOMESTIC_BUILDERS, MADHYA_PRADESH_SLUG
from models.destinations import Destination
from models.packages import Package
from services.package_insert import insert_package_if_missing
from utils.db import commit_or_raise


def get_or_create_madhya_pradesh_destination(db) -> Destination:
    destination = db.scalar(select(Destination).where(Destination.slug == MADHYA_PRADESH_SLUG))
    if destination is not None:
        print(f"Using destination: {destination.name} ({destination.id})")
        return destination

    destination = Destination(
        slug=MADHYA_PRADESH_SLUG,
        name="Madhya Pradesh",
        country="India",
        region="domestic",
        india_region="central",
        description=(
            "Khajuraho temples, Gwalior forts, Bandhavgarh and Pench tiger reserves, "
            "Panna diamond country, Chitrakoot pilgrimage, and the heart of incredible India."
        ),
        starting_price=0,
        moods=["Wildlife", "Family", "Luxury", "Cultural"],
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
        lakshadweep = db.get(Destination, LAKSHADWEEP_DESTINATION_ID)
        if lakshadweep is None:
            print(f"Lakshadweep destination not found: {LAKSHADWEEP_DESTINATION_ID}", file=sys.stderr)
            sys.exit(1)

        print(f"Using destination: {lakshadweep.name} ({lakshadweep.id})")
        package, itinerary = build_lk_009(LAKSHADWEEP_DESTINATION_ID)
        print(f"\n--- {package.serial_code} | {package.slug} ---")
        result = insert_package_if_missing(
            db,
            destination_id=LAKSHADWEEP_DESTINATION_ID,
            package=package,
            itinerary=itinerary,
        )
        if result is None:
            skipped += 1
        else:
            inserted += 1

        ch006 = db.scalar(select(Package).where(Package.serial_code == "CH-006"))
        print("\n--- MP-006.pdf (contains CH-006 Chandigarh) ---")
        if ch006:
            print(f"Skipping CH-006: package already exists ({ch006.id})")
            skipped += 1
        else:
            print("Note: MP-006.pdf contains CH-006 content; CH-006 not in DB — no MP builder for this file.")

        destination = get_or_create_madhya_pradesh_destination(db)
        dest_id = str(destination.id)

        for builder in MADHYA_PRADESH_DOMESTIC_BUILDERS:
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
