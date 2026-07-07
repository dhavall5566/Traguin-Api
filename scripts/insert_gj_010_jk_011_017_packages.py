#!/usr/bin/env python3
"""Insert GJ-010 (skip if exists) and JK-011 through JK-017 Kashmir packages (no images)."""

from __future__ import annotations

import sys
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR.parent) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR.parent))
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from database import SessionLocal
from gujarat_domestic_batch_defs import GUJARAT_DESTINATION_ID, build_gj_010
from kashmir_domestic_batch_defs import KASHMIR_DESTINATION_ID, KASHMIR_DOMESTIC_BUILDERS
from models.destinations import Destination
from services.package_insert import insert_package_if_missing


def main() -> None:
    inserted = 0
    skipped = 0

    with SessionLocal() as db:
        gujarat = db.get(Destination, GUJARAT_DESTINATION_ID)
        if gujarat is None:
            print(f"Gujarat destination not found: {GUJARAT_DESTINATION_ID}", file=sys.stderr)
            sys.exit(1)

        kashmir = db.get(Destination, KASHMIR_DESTINATION_ID)
        if kashmir is None:
            print(f"Kashmir destination not found: {KASHMIR_DESTINATION_ID}", file=sys.stderr)
            sys.exit(1)

        print(f"Using destination: {gujarat.name} ({gujarat.id})")
        package, itinerary = build_gj_010(GUJARAT_DESTINATION_ID)
        print(f"\n--- {package.serial_code} | {package.slug} ---")
        result = insert_package_if_missing(
            db,
            destination_id=GUJARAT_DESTINATION_ID,
            package=package,
            itinerary=itinerary,
        )
        if result is None:
            skipped += 1
        else:
            inserted += 1

        print(f"\nUsing destination: {kashmir.name} ({kashmir.id})")
        for builder in KASHMIR_DOMESTIC_BUILDERS:
            package, itinerary = builder(KASHMIR_DESTINATION_ID)
            print(f"\n--- {package.serial_code} | {package.slug} ---")
            try:
                result = insert_package_if_missing(
                    db,
                    destination_id=KASHMIR_DESTINATION_ID,
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
