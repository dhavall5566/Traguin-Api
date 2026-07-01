#!/usr/bin/env python3
"""Insert US-001, US-002, and US-004 USA packages (no images)."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from us_batch_package_defs import US_BUILDERS
from database import SessionLocal
from models.destinations import Destination
from services.package_insert import upsert_package_without_images
from utils.db import commit_or_raise

USA_SLUG = "usa"


def get_or_create_usa_destination_id() -> str:
    with SessionLocal() as db:
        destination = db.scalar(select(Destination).where(Destination.slug == USA_SLUG))
        if destination is None:
            destination = Destination(
                slug=USA_SLUG,
                name="USA",
                country="United States",
                region="international",
                india_region=None,
                description=(
                    "New York, Washington D.C., Niagara Falls, Los Angeles, Las Vegas, Grand Canyon, and San Francisco — "
                    "iconic skylines, natural wonders, and world-class luxury for families and discerning travelers."
                ),
                starting_price=0,
                moods=["family", "luxury", "romantic", "cultural", "adventure", "nature"],
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
    dest_id = get_or_create_usa_destination_id()
    with SessionLocal() as db:
        for builder in US_BUILDERS:
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
