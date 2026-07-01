#!/usr/bin/env python3
"""Insert SG-001 through SG-004 Singapore packages (no images)."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from sg_batch_package_defs import SG_BUILDERS
from database import SessionLocal
from models.destinations import Destination
from services.package_insert import upsert_package_without_images
from utils.db import commit_or_raise

SINGAPORE_SLUG = "singapore"


def get_or_create_singapore_destination_id() -> str:
    with SessionLocal() as db:
        destination = db.scalar(select(Destination).where(Destination.slug == SINGAPORE_SLUG))
        if destination is None:
            destination = Destination(
                slug=SINGAPORE_SLUG,
                name="Singapore",
                country="Singapore",
                region="international",
                india_region=None,
                description=(
                    "Marina Bay, Gardens by the Bay, Sentosa Island, and Universal Studios — a futuristic city-state "
                    "of iconic skylines, theme parks, and world-class luxury for families and couples."
                ),
                starting_price=0,
                moods=["family", "luxury", "cultural", "beach", "adventure", "wildlife"],
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
    dest_id = get_or_create_singapore_destination_id()
    with SessionLocal() as db:
        for builder in SG_BUILDERS:
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
