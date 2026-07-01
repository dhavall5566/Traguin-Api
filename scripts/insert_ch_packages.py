#!/usr/bin/env python3
"""Insert CH-001 through CH-003 Switzerland packages (no images)."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from ch_batch_package_defs import CH_BUILDERS
from database import SessionLocal
from models.destinations import Destination
from services.package_insert import upsert_package_without_images
from utils.db import commit_or_raise

SWITZERLAND_SLUG = "switzerland"


def get_or_create_switzerland_destination_id() -> str:
    with SessionLocal() as db:
        destination = db.scalar(select(Destination).where(Destination.slug == SWITZERLAND_SLUG))
        if destination is None:
            destination = Destination(
                slug=SWITZERLAND_SLUG,
                name="Switzerland",
                country="Switzerland",
                region="international",
                india_region=None,
                description=(
                    "Zurich, Lucerne, Interlaken, Zermatt, and the Swiss Alps — pristine lakes, majestic peaks, "
                    "scenic rail journeys, and world-class luxury for families, couples, and discerning travelers."
                ),
                starting_price=0,
                moods=["family", "luxury", "romantic", "nature", "adventure"],
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
    dest_id = get_or_create_switzerland_destination_id()
    with SessionLocal() as db:
        for builder in CH_BUILDERS:
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
