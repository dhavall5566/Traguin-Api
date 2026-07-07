#!/usr/bin/env python3
"""Insert KL-001 through KL-010 Kerala packages (no images, skip if exists)."""

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
from kerala_kl_001_010_domestic_batch_defs import KERALA_KL_001_010_BUILDERS, KERALA_SLUG
from models.destinations import Destination
from services.package_insert import insert_package_if_missing


def get_kerala_destination(db) -> Destination:
    destination = db.scalar(select(Destination).where(Destination.slug == KERALA_SLUG))
    if destination is None:
        raise SystemExit(
            f"Destination slug {KERALA_SLUG!r} not found — create it before running this script."
        )
    print(f"Using destination: {destination.name} ({destination.id})")
    return destination


def main() -> None:
    inserted = 0
    skipped = 0

    with SessionLocal() as db:
        destination = get_kerala_destination(db)
        dest_id = str(destination.id)

        for builder in KERALA_KL_001_010_BUILDERS:
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
