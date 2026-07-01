#!/usr/bin/env python3
"""Insert AU-001 through AU-004 Australia packages (no images)."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from au_batch_package_defs import AU_BUILDERS
from database import SessionLocal
from models.destinations import Destination
from services.package_insert import upsert_package_without_images
from utils.db import commit_or_raise

AUSTRALIA_SLUG = "australia"


def get_or_create_australia_destination_id() -> str:
    with SessionLocal() as db:
        destination = db.scalar(select(Destination).where(Destination.slug == AUSTRALIA_SLUG))
        if destination is None:
            destination = Destination(
                slug=AUSTRALIA_SLUG,
                name="Australia",
                country="Australia",
                region="international",
                india_region=None,
                description=(
                    "Sydney, Melbourne, Cairns, the Great Barrier Reef, Whitsunday Islands, and the Gold Coast — "
                    "iconic harbours, reef expeditions, rainforest retreats, and world-class family and honeymoon circuits."
                ),
                starting_price=0,
                moods=["family", "luxury", "romantic", "nature", "beach", "wildlife", "adventure"],
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
    dest_id = get_or_create_australia_destination_id()
    with SessionLocal() as db:
        for builder in AU_BUILDERS:
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
