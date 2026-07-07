#!/usr/bin/env python3
"""Insert HR-001 through HR-010 Haryana packages (no images, skip if exists)."""

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
from haryana_domestic_batch_defs import HARYANA_DOMESTIC_BUILDERS, HARYANA_SLUG
from models.destinations import Destination
from services.package_insert import insert_package_if_missing
from utils.db import commit_or_raise


def get_or_create_haryana_destination(db) -> Destination:
    destination = db.scalar(select(Destination).where(Destination.slug == HARYANA_SLUG))
    if destination is not None:
        print(f"Using destination: {destination.name} ({destination.id})")
        return destination

    destination = Destination(
        slug=HARYANA_SLUG,
        name="Haryana",
        country="India",
        region="domestic",
        india_region="north",
        description=(
            "Sacred Kurukshetra and Jyotisar, Sultanpur bird sanctuary, Pinjore Mughal gardens, "
            "Gurugram luxury escapes, Panchkula foothills, and royal heritage across North India."
        ),
        starting_price=0,
        moods=["Heritage", "Family", "Luxury", "Spiritual"],
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
    results: list[tuple[str, str, str | None]] = []

    with SessionLocal() as db:
        destination = get_or_create_haryana_destination(db)
        dest_id = str(destination.id)

        for builder in HARYANA_DOMESTIC_BUILDERS:
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
                    results.append((package.serial_code, "SKIPPED", None))
                else:
                    inserted += 1
                    pkg_row, _ = result
                    hero_id = str(pkg_row.hero_media_id) if pkg_row.hero_media_id else None
                    results.append((package.serial_code, "INSERTED", hero_id))
            except Exception as exc:
                print(f"Failed {package.slug}: {exc}", file=sys.stderr)
                results.append((package.serial_code, f"FAILED: {exc}", None))
                raise

    print("\n=== Insert results ===")
    for serial_code, status, hero_media_id in results:
        hero_label = hero_media_id if hero_media_id else "None"
        print(f"{serial_code}: {status} | hero_media_id={hero_label}")
    print(f"\nDone. Inserted: {inserted}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
