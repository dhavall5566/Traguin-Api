#!/usr/bin/env python3
"""Insert CH-001 through CH-005 Chandigarh domestic packages (no images, skip if exists)."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR.parent) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR.parent))
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from chandigarh_domestic_batch_defs import (
    PUNJAB_DESTINATION_ID,
    PUNJAB_SLUG,
    build_ch_001,
    build_ch_002,
    build_ch_003,
    build_ch_004,
    build_ch_005,
)
from database import SessionLocal
from models.destinations import Destination
from services.package_insert import insert_package_if_missing
from utils.db import commit_or_raise

CH_001_005_BUILDERS = [
    build_ch_001,
    build_ch_002,
    build_ch_003,
    build_ch_004,
    build_ch_005,
]


def get_or_create_punjab_destination(db) -> Destination:
    destination = db.get(Destination, PUNJAB_DESTINATION_ID)
    if destination is not None:
        print(f"Using destination: {destination.name} ({destination.id})")
        return destination

    destination = db.scalar(select(Destination).where(Destination.slug == PUNJAB_SLUG))
    if destination is not None:
        print(f"Using destination: {destination.name} ({destination.id})")
        return destination

    destination = Destination(
        slug=PUNJAB_SLUG,
        name="Punjab",
        country="India",
        region="domestic",
        india_region="north",
        description=(
            "Chandigarh planned city architecture, Sukhna Lake, Rock Garden, Amritsar Golden Temple, "
            "Punjabi cuisine, Phulkari textiles, and North India cultural heritage."
        ),
        starting_price=0,
        moods=["Family", "Luxury", "Cultural", "Spiritual", "Food"],
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
    results: list[tuple[str, str]] = []

    with SessionLocal() as db:
        destination = get_or_create_punjab_destination(db)
        dest_id = str(destination.id)

        for builder in CH_001_005_BUILDERS:
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
                    results.append((package.serial_code, "SKIPPED"))
                else:
                    inserted += 1
                    results.append((package.serial_code, "INSERTED"))
            except Exception as exc:
                print(f"Failed {package.slug}: {exc}", file=sys.stderr)
                results.append((package.serial_code, f"FAILED: {exc}"))
                raise

    print("\n=== Insert results ===")
    for serial_code, status in results:
        print(f"{serial_code}: {status}")
    print(f"\nDone. Inserted: {inserted}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
