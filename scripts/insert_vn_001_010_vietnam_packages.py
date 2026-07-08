#!/usr/bin/env python3
"""Insert VN-001 through VN-010 Vietnam packages (no images, skip if exists)."""

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
from services.package_insert import insert_package_if_missing
from utils.db import commit_or_raise
from vietnam_vn_001_010_batch_defs import VIETNAM_VN_001_010_BUILDERS, VN_SLUG


def get_or_create_vietnam_destination(db) -> Destination:
    destination = db.scalar(select(Destination).where(Destination.slug == VN_SLUG))
    if destination is not None:
        print(f"Using destination: {destination.name} ({destination.id})")
        return destination

    destination = Destination(
        slug=VN_SLUG,
        name="Vietnam",
        country="Vietnam",
        region="international",
        india_region=None,
        description=(
            "Hanoi, Halong Bay, Da Nang, Hoi An, Ho Chi Minh City, Sapa, and the Mekong Delta — "
            "family explorer circuits, romantic getaways, luxury cruises, adventure treks, "
            "and senior-friendly leisure across Vietnam."
        ),
        starting_price=0,
        moods=["Family", "Luxury", "Honeymoon", "Culture", "Nature", "Adventure"],
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
        destination = get_or_create_vietnam_destination(db)
        dest_id = str(destination.id)

        for builder in VIETNAM_VN_001_010_BUILDERS:
            package, itinerary = builder(dest_id)
            serial = package.serial_code or package.slug
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
