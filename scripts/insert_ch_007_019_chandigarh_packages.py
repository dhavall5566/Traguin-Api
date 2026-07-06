#!/usr/bin/env python3
"""Insert CH-007 through CH-019 Chandigarh domestic packages (no images)."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from chandigarh_domestic_batch_defs import CHANDIGARH_DOMESTIC_BUILDERS, PUNJAB_DESTINATION_ID
from database import SessionLocal
from models.destinations import Destination
from services.package_insert import upsert_package_without_images


def main() -> None:
    with SessionLocal() as db:
        destination = db.get(Destination, PUNJAB_DESTINATION_ID)
        if destination is None:
            print(f"Punjab destination not found: {PUNJAB_DESTINATION_ID}", file=sys.stderr)
            sys.exit(1)
        print(f"Using destination: {destination.name} ({destination.id})")

        for builder in CHANDIGARH_DOMESTIC_BUILDERS:
            package, itinerary = builder(PUNJAB_DESTINATION_ID)
            print(f"\n--- {package.serial_code} | {package.slug} ---")
            try:
                upsert_package_without_images(
                    db,
                    destination_id=PUNJAB_DESTINATION_ID,
                    package=package,
                    itinerary=itinerary,
                )
            except Exception as exc:
                print(f"Failed {package.slug}: {exc}", file=sys.stderr)
                raise


if __name__ == "__main__":
    main()
