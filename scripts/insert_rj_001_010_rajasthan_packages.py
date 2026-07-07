#!/usr/bin/env python3
"""Insert RJ-001 through RJ-010 Rajasthan packages (no images, skip if serial exists)."""

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
from rajasthan_rj_003_004_006_008_010_domestic_batch_defs import RAJASTHAN_RJ_003_004_006_008_010_BUILDERS
from rj_batch_package_defs import RJ_BUILDERS
from services.package_insert import insert_package_if_missing

RAJASTHAN_SLUG = "rajasthan"

RJ_001_010_BUILDERS = [
    *RJ_BUILDERS,
    *RAJASTHAN_RJ_003_004_006_008_010_BUILDERS,
]


def main() -> None:
    inserted = 0
    skipped = 0

    with SessionLocal() as db:
        destination = db.scalar(select(Destination).where(Destination.slug == RAJASTHAN_SLUG))
        if destination is None:
            print(f"Rajasthan destination not found: {RAJASTHAN_SLUG}", file=sys.stderr)
            sys.exit(1)
        print(f"Using destination: {destination.name} ({destination.id})")
        dest_id = str(destination.id)

        for builder in RJ_001_010_BUILDERS:
            package, itinerary = builder(dest_id)
            label = package.serial_code or package.slug
            print(f"\n--- {label} | {package.slug} ---")
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
