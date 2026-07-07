#!/usr/bin/env python3
"""Insert DN-001 through DN-005 Dadra and Nagar Haveli packages (no images, skip if exists)."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR.parent) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR.parent))
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from dadra_nagar_haveli_batch_defs import (
    DADRA_NAGAR_HAVELI_SLUG,
    build_dn_001,
    build_dn_002,
    build_dn_003,
    build_dn_004,
    build_dn_005,
)
from database import SessionLocal
from models.destinations import Destination
from services.package_insert import insert_package_if_missing
from utils.db import commit_or_raise

DN_001_005_BUILDERS = [
    build_dn_001,
    build_dn_002,
    build_dn_003,
    build_dn_004,
    build_dn_005,
]


def get_or_create_dadra_nagar_haveli_destination(db) -> Destination:
    destination = db.scalar(select(Destination).where(Destination.slug == DADRA_NAGAR_HAVELI_SLUG))
    if destination is not None:
        print(f"Using destination: {destination.name} ({destination.id})")
        return destination

    destination = Destination(
        slug=DADRA_NAGAR_HAVELI_SLUG,
        name="Dadra and Nagar Haveli",
        country="India",
        region="domestic",
        india_region="west",
        description=(
            "Silvassa's emerald woodlands, Vanganga Lake Garden, Khanvel retreats, Dudhni waterfront, "
            "Vasona Lion Safari, tribal Warli heritage, and serene nature escapes near the Gujarat border."
        ),
        starting_price=0,
        moods=["Nature", "Family", "Luxury", "Romantic"],
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
        destination = get_or_create_dadra_nagar_haveli_destination(db)
        dest_id = str(destination.id)

        for builder in DN_001_005_BUILDERS:
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
