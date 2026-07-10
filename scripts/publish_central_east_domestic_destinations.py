#!/usr/bin/env python3
"""Publish Central and East India domestic destinations and their packages in CMS."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import func, select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR.parent) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR.parent))

from database import SessionLocal
from models.destinations import Destination
from models.itineraries import Itinerary
from models.packages import Package
from utils.db import commit_or_raise

# Two additional Central India state destinations (beyond Chhattisgarh)
CENTRAL_DESTINATION_SLUGS = ("madhya-pradesh", "jharkhand")

# Four additional East India state destinations
EAST_DESTINATION_SLUGS = ("odisha", "bihar", "assam", "sikkim")

DESTINATION_REGION_OVERRIDES: dict[str, str] = {
    "madhya-pradesh": "central",
    "jharkhand": "central",
    "chhattisgarh": "central",
    "odisha": "east",
    "bihar": "east",
    "assam": "north-east",
    "sikkim": "northeast",
}


def publish_destination_tree(db, slug: str) -> dict[str, int]:
    destination = db.scalar(select(Destination).where(Destination.slug == slug))
    if destination is None:
        print(f"  ! Destination not found: {slug}")
        return {"packages": 0, "itineraries": 0}

    region_override = DESTINATION_REGION_OVERRIDES.get(slug)
    if region_override and destination.india_region != region_override:
        print(f"  Updated india_region: {destination.india_region} -> {region_override}")
        destination.india_region = region_override

    if not destination.is_published:
        destination.is_published = True
        print(f"  Published destination: {destination.name}")

    packages = db.scalars(
        select(Package).where(Package.destination_id == destination.id).order_by(Package.price)
    ).all()
    published_packages = 0
    published_itineraries = 0

    for package in packages:
        if not package.is_published:
            package.is_published = True
            published_packages += 1

        itinerary = db.scalar(select(Itinerary).where(Itinerary.package_id == package.id))
        if itinerary is not None and not itinerary.is_published:
            itinerary.is_published = True
            published_itineraries += 1

    if packages:
        destination.starting_price = min(pkg.price for pkg in packages)
        destination.package_count = len(packages)
    else:
        print(f"  ! No packages found for {slug}")

    commit_or_raise(db)
    print(
        f"  {destination.name}: {len(packages)} packages total, "
        f"{published_packages} newly published packages, "
        f"{published_itineraries} newly published itineraries"
    )
    return {"packages": published_packages, "itineraries": published_itineraries}


def main() -> None:
    totals = {"packages": 0, "itineraries": 0}

    with SessionLocal() as db:
        print("=== Central India (2 states) ===")
        for slug in CENTRAL_DESTINATION_SLUGS:
            print(f"\n[{slug}]")
            result = publish_destination_tree(db, slug)
            totals["packages"] += result["packages"]
            totals["itineraries"] += result["itineraries"]

        print("\n[chhattisgarh]")
        result = publish_destination_tree(db, "chhattisgarh")
        totals["packages"] += result["packages"]
        totals["itineraries"] += result["itineraries"]

        print("\n=== East India (4 states) ===")
        for slug in EAST_DESTINATION_SLUGS:
            print(f"\n[{slug}]")
            result = publish_destination_tree(db, slug)
            totals["packages"] += result["packages"]
            totals["itineraries"] += result["itineraries"]

        print("\n=== Summary ===")
        central_count = db.scalar(
            select(func.count())
            .select_from(Destination)
            .where(
                Destination.region == "domestic",
                Destination.india_region == "central",
                Destination.is_published.is_(True),
            )
        )
        east_count = db.scalar(
            select(func.count())
            .select_from(Destination)
            .where(
                Destination.region == "domestic",
                Destination.india_region.in_(("east", "north-east", "northeast")),
                Destination.is_published.is_(True),
            )
        )
        print(f"Published central destinations: {central_count}")
        print(f"Published east / north-east destinations: {east_count}")
        print(
            f"Newly published packages: {totals['packages']}, "
            f"itineraries: {totals['itineraries']}"
        )


if __name__ == "__main__":
    main()
