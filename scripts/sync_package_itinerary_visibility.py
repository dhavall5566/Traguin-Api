#!/usr/bin/env python3
"""Align itinerary publish state and destination package_count with published packages."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR.parent) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR.parent))

from database import SessionLocal
from models.destinations import Destination
from models.itineraries import Itinerary
from models.packages import Package
from services.packages import apply_package_visibility_side_effects, sync_destination_package_stats
from utils.db import commit_or_raise


def main() -> None:
    hidden_itineraries = 0
    published_itineraries = 0
    updated_destinations = 0

    with SessionLocal() as db:
        packages = db.scalars(select(Package)).all()
        for package in packages:
            linked = db.scalars(
                select(Itinerary).where(Itinerary.package_id == package.id)
            ).all()
            before = {itinerary.id: itinerary.is_published for itinerary in linked}

            apply_package_visibility_side_effects(db, package)

            for itinerary in linked:
                was_published = before.get(itinerary.id, False)
                if was_published and not itinerary.is_published:
                    hidden_itineraries += 1
                elif not was_published and itinerary.is_published:
                    published_itineraries += 1

        destination_ids = db.scalars(select(Destination.id)).all()
        for destination_id in destination_ids:
            sync_destination_package_stats(db, destination_id)
            updated_destinations += 1

        commit_or_raise(db)

    print(f"Published itineraries for published packages: {published_itineraries}")
    print(f"Hidden itineraries for unpublished packages: {hidden_itineraries}")
    print(f"Synced destination package stats: {updated_destinations}")


if __name__ == "__main__":
    main()
