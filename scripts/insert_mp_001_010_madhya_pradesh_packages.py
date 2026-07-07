#!/usr/bin/env python3
"""Insert MP-001 through MP-005 and MP-007 through MP-010 Madhya Pradesh packages (no images, skip if exists)."""

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
from madhya_pradesh_mp_001_010_domestic_batch_defs import (
    MADHYA_PRADESH_MP_001_010_BUILDERS,
    MADHYA_PRADESH_SLUG,
)
from models.destinations import Destination
from services.package_insert import insert_package_if_missing


def main() -> None:
    inserted = 0
    skipped = 0

    with SessionLocal() as db:
        destination = db.scalar(select(Destination).where(Destination.slug == MADHYA_PRADESH_SLUG))
        if destination is None:
            print(f"Madhya Pradesh destination not found: {MADHYA_PRADESH_SLUG}", file=sys.stderr)
            sys.exit(1)
        print(f"Using destination: {destination.name} ({destination.id})")
        dest_id = str(destination.id)

        for builder in MADHYA_PRADESH_MP_001_010_BUILDERS:
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
