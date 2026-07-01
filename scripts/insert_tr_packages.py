#!/usr/bin/env python3
"""Insert TR-001 through TR-003 Turkey packages (no images)."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from tr_batch_package_defs import TR_BUILDERS
from database import SessionLocal
from models.destinations import Destination
from services.package_insert import upsert_package_without_images
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
    dest_id = get_or_create_turkey_destination_id()
    with SessionLocal() as db:
        for builder in TR_BUILDERS:
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
