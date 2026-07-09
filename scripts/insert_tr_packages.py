#!/usr/bin/env python3
"""Insert TR-001 through TR-005 Turkey packages (no images, skip if exists)."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR.parent) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR.parent))
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from tr_batch_package_defs import TR_BUILDERS
from database import SessionLocal
from models.destinations import Destination
from services.package_insert import insert_package_if_missing
from utils.db import commit_or_raise

TURKEY_SLUG = "turkey"


def get_or_create_turkey_destination_id() -> str:
    with SessionLocal() as db:
        destination = db.scalar(select(Destination).where(Destination.slug == TURKEY_SLUG))
        if destination is None:
            destination = Destination(
                slug=TURKEY_SLUG,
                name="Turkey",
                country="Turkey",
                region="international",
                india_region=None,
                description=(
                    "Istanbul, Cappadocia, Ephesus, Antalya, and Bodrum — Ottoman heritage, fairy-tale landscapes, "
                    "ancient ruins, and Mediterranean elegance for families, couples, and discerning travelers."
                ),
                starting_price=0,
                moods=["family", "luxury", "romantic", "cultural", "adventure", "nature", "beach"],
                is_published=True,
            )
            db.add(destination)
            db.flush()
            commit_or_raise(db)
            print(f"Created destination: {destination.slug} ({destination.id})")
        else:
            print(f"Using destination: {destination.slug} ({destination.id})")
        return str(destination.id)


def main() -> None:
    inserted = 0
    skipped = 0

    with SessionLocal() as db:
        dest_id = get_or_create_turkey_destination_id()
        destination = db.scalar(select(Destination).where(Destination.slug == TURKEY_SLUG))
        if destination is None:
            raise RuntimeError("Turkey destination not found after create")

        for builder in TR_BUILDERS:
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
