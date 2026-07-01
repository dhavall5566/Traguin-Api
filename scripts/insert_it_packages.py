#!/usr/bin/env python3
"""Insert IT-001 through IT-003 Italy packages (no images)."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from it_batch_package_defs import IT_BUILDERS
from database import SessionLocal
from models.destinations import Destination
from services.package_insert import upsert_package_without_images
from utils.db import commit_or_raise

ITALY_SLUG = "italy"


def get_or_create_italy_destination_id() -> str:
    with SessionLocal() as db:
        destination = db.scalar(select(Destination).where(Destination.slug == ITALY_SLUG))
        if destination is None:
            destination = Destination(
                slug=ITALY_SLUG,
                name="Italy",
                country="Italy",
                region="international",
                india_region=None,
                description=(
                    "Rome, Florence, Tuscany, Venice, Lake Como, and the Amalfi Coast — ancient history, "
                    "Renaissance art, world-class gastronomy, and iconic luxury for families, couples, and discerning travelers."
                ),
                starting_price=0,
                moods=["family", "luxury", "romantic", "cultural", "beach"],
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
    dest_id = get_or_create_italy_destination_id()
    with SessionLocal() as db:
        for builder in IT_BUILDERS:
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
