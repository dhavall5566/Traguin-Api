#!/usr/bin/env python3
"""Insert LK-001 and LK-002 Lakshadweep packages (no images, skip if exists)."""

from __future__ import annotations

import sys
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR.parent) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR.parent))
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from database import SessionLocal
from lakshadweep_lk_batch_defs import (
    LAKSHADWEEP_DESTINATION_ID,
    build_lk_001,
    build_lk_002,
)
from models.destinations import Destination
from services.package_insert import insert_package_if_missing


def main() -> None:
    inserted = 0
    skipped = 0
    builders = [build_lk_001, build_lk_002]

    with SessionLocal() as db:
        destination = db.get(Destination, LAKSHADWEEP_DESTINATION_ID)
        if destination is None:
            print(f"Lakshadweep destination not found: {LAKSHADWEEP_DESTINATION_ID}", file=sys.stderr)
            sys.exit(1)
        print(f"Using destination: {destination.name} ({destination.id})")

        for builder in builders:
            package, itinerary = builder(LAKSHADWEEP_DESTINATION_ID)
            print(f"\n--- {package.serial_code} | {package.slug} ---")
            try:
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
            except Exception as exc:
                print(f"Failed {package.slug}: {exc}", file=sys.stderr)
                raise

    print(f"\nDone. Inserted: {inserted}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
