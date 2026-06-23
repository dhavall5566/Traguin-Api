#!/usr/bin/env python3
"""Apply route-based package names to an existing CMS package/itinerary."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from database import SessionLocal
from models.destinations import Destination
from schemas.package_import import (
    ExtractedDestinationDraft,
    ExtractedItineraryDayDraft,
    ExtractedItineraryDraft,
    ExtractedItineraryHotelDraft,
    ExtractedPackageBundle,
    ExtractedPackageDraft,
)
from services.itineraries import itinerary_query_with_nested
from services.package_import_naming import apply_generated_names
from services.packages import package_query_with_nested


def _bundle_from_package(db, package, destination: Destination) -> ExtractedPackageBundle:
    itinerary = (
        itinerary_query_with_nested(db)
        .filter_by(package_id=package.id)
        .one_or_none()
    )
    if itinerary is None:
        raise SystemExit(f"No itinerary linked to package '{package.slug}'.")

    return ExtractedPackageBundle(
        destination=ExtractedDestinationDraft(
            name=destination.name,
            slug=destination.slug,
            country=destination.country,
            region=destination.region,
            india_region=destination.india_region,
            description=destination.description,
            starting_price=destination.starting_price,
            moods=[],
        ),
        package=ExtractedPackageDraft(
            title=package.title,
            slug=package.slug,
            duration_label=package.duration_label,
            starting_price=package.price,
        ),
        itinerary=ExtractedItineraryDraft(
            title=itinerary.title,
            slug=itinerary.slug,
            tagline=itinerary.tagline,
            overview=itinerary.overview,
            duration_label=itinerary.duration_label,
            duration_days=itinerary.duration_days,
            starting_price=itinerary.starting_price,
            price_note=itinerary.price_note,
            days=[
                ExtractedItineraryDayDraft(
                    day_number=day.day_number,
                    title=day.title,
                    description=day.description,
                    activities=list(day.activities or []),
                    sort_order=day.sort_order,
                )
                for day in sorted(itinerary.days, key=lambda item: item.sort_order)
            ],
            hotels=[
                ExtractedItineraryHotelDraft(
                    name=hotel.name,
                    location=hotel.location,
                    nights_label=hotel.nights_label,
                    description=hotel.description,
                    category_label=hotel.category_label,
                    sort_order=hotel.sort_order,
                )
                for hotel in sorted(itinerary.hotels, key=lambda item: item.sort_order)
            ],
        ),
        places_mentioned=[],
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package_slug", help="Existing package slug to rename")
    parser.add_argument(
        "--apply-slugs",
        action="store_true",
        help="Also update package/itinerary slugs (may affect URLs)",
    )
    args = parser.parse_args()

    with SessionLocal() as db:
        package = (
            package_query_with_nested(db)
            .filter_by(slug=args.package_slug)
            .one_or_none()
        )
        if package is None:
            raise SystemExit(f"Package not found: {args.package_slug}")

        destination = db.query(Destination).filter_by(id=package.destination_id).one()
        bundle = _bundle_from_package(db, package, destination)
        named = apply_generated_names(bundle)
        itinerary = (
            itinerary_query_with_nested(db)
            .filter_by(package_id=package.id)
            .one()
        )

        package.title = named.package.title
        itinerary.title = named.itinerary.title
        if args.apply_slugs:
            package.slug = named.package.slug
            itinerary.slug = named.itinerary.slug

        db.commit()
        print(f"Package title: {package.title}")
        print(f"Package slug: {package.slug}")
        print(f"Itinerary title: {itinerary.title}")
        print(f"Itinerary slug: {itinerary.slug}")


if __name__ == "__main__":
    main()
