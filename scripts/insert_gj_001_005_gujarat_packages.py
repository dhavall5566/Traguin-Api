#!/usr/bin/env python3
"""Insert GJ-001 through GJ-005 Gujarat packages (no images, skip if exists)."""

from __future__ import annotations

import sys
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR.parent) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR.parent))
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from database import SessionLocal
from gujarat_domestic_batch_defs import (
    GUJARAT_DESTINATION_ID,
    build_gj_001,
    build_gj_002,
    build_gj_003,
    build_gj_004,
    build_gj_005,
)
from models.destinations import Destination
from services.package_insert import insert_package_if_missing
from utils.db import commit_or_raise

GJ_001_005_BUILDERS = [
    build_gj_001,
    build_gj_002,
    build_gj_003,
    build_gj_004,
    build_gj_005,
]


def main() -> None:
    inserted = 0
    skipped = 0
    results: list[tuple[str, str]] = []

    with SessionLocal() as db:
        destination = db.get(Destination, GUJARAT_DESTINATION_ID)
        if destination is None:
            print(f"Gujarat destination not found: {GUJARAT_DESTINATION_ID}", file=sys.stderr)
            sys.exit(1)
        print(f"Using destination: {destination.name} ({destination.id})")

        for builder in GJ_001_005_BUILDERS:
            package, itinerary = builder(GUJARAT_DESTINATION_ID)
            print(f"\n--- {package.serial_code} | {package.slug} ---")
            try:
                result = insert_package_if_missing(
                    db,
                    destination_id=GUJARAT_DESTINATION_ID,
                    package=package,
                    itinerary=itinerary,
                )
                if result is None:
                    skipped += 1
                    results.append((package.serial_code, "SKIPPED"))
                else:
                    inserted += 1
                    results.append((package.serial_code, "INSERTED"))
            except Exception as exc:
                print(f"Failed {package.slug}: {exc}", file=sys.stderr)
                results.append((package.serial_code, f"FAILED: {exc}"))
                raise

        commit_or_raise(db)

    print("\n=== Insert results ===")
    for serial_code, status in results:
        print(f"{serial_code}: {status}")
    print(f"\nDone. Inserted: {inserted}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
