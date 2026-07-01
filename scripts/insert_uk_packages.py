#!/usr/bin/env python3
"""Insert UK-001 through UK-010 Uttarakhand packages (no images)."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from database import SessionLocal
from models.destinations import Destination
from services.package_insert import upsert_package_without_images
from uk_batch_package_defs import UK_BUILDERS
from utils.db import commit_or_raise

UTTARAKHAND_SLUG = "uttarakhand"


def get_or_create_uttarakhand_destination_id() -> str:
    with SessionLocal() as db:
        destination = db.scalar(select(Destination).where(Destination.slug == UTTARAKHAND_SLUG))
        if destination is None:
            destination = Destination(
                slug=UTTARAKHAND_SLUG,
                name="Uttarakhand",
                country="India",
                region="domestic",
                india_region="north",
                description=(
                    "Nainital, Mussoorie, Rishikesh, Haridwar, Auli, and the Char Dham — Himalayan lakes, "
                    "hill stations, river spirituality, alpine meadows, and Devbhoomi's sacred pilgrimage circuits."
                ),
                starting_price=0,
                moods=["nature", "spiritual", "family", "adventure", "romantic", "luxury"],
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
    dest_id = get_or_create_uttarakhand_destination_id()
    with SessionLocal() as db:
        for builder in UK_BUILDERS:
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
