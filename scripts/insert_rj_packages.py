#!/usr/bin/env python3
"""Insert RJ-001, RJ-002, RJ-005, RJ-007, and RJ-009 Rajasthan packages (no images)."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from database import SessionLocal
from models.destinations import Destination
from rj_batch_package_defs import RJ_BUILDERS
from services.package_insert import upsert_package_without_images
from utils.db import commit_or_raise

RAJASTHAN_SLUG = "rajasthan"


def get_or_create_rajasthan_destination_id() -> str:
    with SessionLocal() as db:
        destination = db.scalar(select(Destination).where(Destination.slug == RAJASTHAN_SLUG))
        if destination is None:
            destination = Destination(
                slug=RAJASTHAN_SLUG,
                name="Rajasthan",
                country="India",
                region="domestic",
                india_region="north",
                description=(
                    "Jaipur, Jodhpur, Udaipur, Jaisalmer, and Pushkar — royal forts, desert dunes, "
                    "lake palaces, and Rajasthan's living heritage hospitality."
                ),
                starting_price=0,
                moods=["cultural", "luxury", "family", "romantic"],
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
    dest_id = get_or_create_rajasthan_destination_id()
    with SessionLocal() as db:
        for builder in RJ_BUILDERS:
            package, itinerary = builder(dest_id)
            package = package.model_copy(update={"destination_id": dest_id})
            itinerary = itinerary.model_copy(update={"destination_id": dest_id})
            print(f"\n--- {package.slug} ---")
            try:
                upsert_package_without_images(
                    db,
                    destination_id=dest_id,
                    package=package,
                    itinerary=itinerary,
                )
            except Exception as exc:
                print(f"Failed {package.slug}: {exc}", file=sys.stderr)
                raise


if __name__ == "__main__":
    main()
