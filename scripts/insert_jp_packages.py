#!/usr/bin/env python3
"""Insert JP-001 through JP-003 Japan packages (no images)."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from jp_batch_package_defs import JP_BUILDERS
from database import SessionLocal
from models.destinations import Destination
from services.package_insert import upsert_package_without_images
from utils.db import commit_or_raise

JAPAN_SLUG = "japan"


def get_or_create_japan_destination_id() -> str:
    with SessionLocal() as db:
        destination = db.scalar(select(Destination).where(Destination.slug == JAPAN_SLUG))
        if destination is None:
            destination = Destination(
                slug=JAPAN_SLUG,
                name="Japan",
                country="Japan",
                region="international",
                india_region=None,
                description=(
                    "Tokyo, Kyoto, Osaka, Mt. Fuji, and Hakone — ancient shrines, bullet trains, neon cityscapes, "
                    "onsen retreats, and world-class luxury for families, couples, and discerning travelers."
                ),
                starting_price=0,
                moods=["family", "luxury", "romantic", "cultural", "nature", "adventure"],
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
    dest_id = get_or_create_japan_destination_id()
    with SessionLocal() as db:
        for builder in JP_BUILDERS:
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
