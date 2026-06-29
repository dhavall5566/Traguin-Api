#!/usr/bin/env python3
"""Sync package and destination travel moods from curated brochure mappings."""

from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

_API_ROOT = Path(__file__).resolve().parents[1]
if str(_API_ROOT) not in sys.path:
    sys.path.insert(0, str(_API_ROOT))

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from database import SessionLocal
from models.destinations import Destination
from models.packages import Package
from services.packages import sync_package_moods
from services.travel_moods import aggregate_destination_moods, travel_moods_for_package
from utils.db import commit_or_raise


def main() -> None:
    with SessionLocal() as db:
        packages = db.scalars(
            select(Package).options(selectinload(Package.moods)).order_by(Package.slug)
        ).all()

        moods_by_destination: dict[str, list[list[str]]] = defaultdict(list)
        updated_packages = 0

        for package in packages:
            current = [m.mood for m in package.moods]
            target = travel_moods_for_package(package.slug, current)
            if current != target:
                sync_package_moods(db, package, target)
                updated_packages += 1
                print(f"  {package.slug}: {current} -> {target}")
            else:
                print(f"  {package.slug}: ok {target}")
            moods_by_destination[str(package.destination_id)].append(target)

        destinations = db.scalars(select(Destination)).all()
        updated_destinations = 0
        for destination in destinations:
            target = aggregate_destination_moods(
                moods_by_destination.get(str(destination.id), [])
            )
            if destination.moods != target:
                print(f"  {destination.slug}: {destination.moods} -> {target}")
                destination.moods = target
                updated_destinations += 1
            elif target:
                print(f"  {destination.slug}: ok {target}")

        commit_or_raise(db)
        print(
            f"\nDone. Updated {updated_packages} package(s), "
            f"{updated_destinations} destination(s)."
        )


if __name__ == "__main__":
    main()
