#!/usr/bin/env python3
"""Insert remaining domestic packages: TN-001, UP-001, WB-001, Tripura TRP-001..003."""

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
from tamil_nadu_tn_001_batch_defs import TAMIL_NADU_SLUG, TAMIL_NADU_TN_001_BUILDERS
from tripura_tr_001_batch_defs import TRIPURA_SLUG, TRIPURA_TR_001_BUILDERS
from tripura_tr_002_010_batch_defs import build_tr_002, build_tr_003
from uttar_pradesh_up_001_batch_defs import UTTAR_PRADESH_SLUG, UTTAR_PRADESH_UP_001_BUILDERS
from utils.db import commit_or_raise
from west_bengal_wb_001_batch_defs import WEST_BENGAL_SLUG, WEST_BENGAL_WB_001_BUILDERS


def get_or_create_destination(db, *, slug: str, name: str, india_region: str) -> Destination:
    destination = db.scalar(select(Destination).where(Destination.slug == slug))
    if destination is not None:
        print(f"Using destination: {destination.name} ({destination.id})")
        return destination

    destination = Destination(
        slug=slug,
        name=name,
        country="India",
        region="domestic",
        india_region=india_region,
        description=f"{name} — TRAGUIN premium domestic tour packages.",
        starting_price=0,
        moods=["Family", "Luxury", "Cultural"],
        is_published=True,
    )
    db.add(destination)
    db.flush()
    commit_or_raise(db)
    print(f"Created destination: {destination.slug} ({destination.id})")
    return destination


def insert_builders(db, *, destination_id: str, builders: list, label: str) -> tuple[int, int]:
    inserted = 0
    skipped = 0
    print(f"\n=== {label} ===")
    for builder in builders:
        package, itinerary = builder(destination_id)
        serial = package.serial_code or package.slug
        print(f"\n--- {serial} | {package.slug} ---")
        result = insert_package_if_missing(
            db,
            destination_id=destination_id,
            package=package,
            itinerary=itinerary,
        )
        if result is None:
            skipped += 1
        else:
            inserted += 1
    return inserted, skipped


def main() -> None:
    total_inserted = 0
    total_skipped = 0

    with SessionLocal() as db:
        jobs = [
            (TAMIL_NADU_SLUG, "Tamil Nadu", "south", TAMIL_NADU_TN_001_BUILDERS, "Tamil Nadu TN-001"),
            (UTTAR_PRADESH_SLUG, "Uttar Pradesh", "north", UTTAR_PRADESH_UP_001_BUILDERS, "Uttar Pradesh UP-001"),
            (WEST_BENGAL_SLUG, "West Bengal", "east", WEST_BENGAL_WB_001_BUILDERS, "West Bengal WB-001"),
            (TRIPURA_SLUG, "Tripura", "northeast", TRIPURA_TR_001_BUILDERS, "Tripura TRP-001"),
        ]
        for slug, name, region, builders, label in jobs:
            destination = get_or_create_destination(db, slug=slug, name=name, india_region=region)
            ins, skip = insert_builders(db, destination_id=str(destination.id), builders=builders, label=label)
            total_inserted += ins
            total_skipped += skip

        tripura = get_or_create_destination(db, slug=TRIPURA_SLUG, name="Tripura", india_region="northeast")
        ins, skip = insert_builders(
            db,
            destination_id=str(tripura.id),
            builders=[build_tr_002, build_tr_003],
            label="Tripura TRP-002..003",
        )
        total_inserted += ins
        total_skipped += skip

    print(f"\nDone. Inserted: {total_inserted}, Skipped: {total_skipped}")


if __name__ == "__main__":
    main()
