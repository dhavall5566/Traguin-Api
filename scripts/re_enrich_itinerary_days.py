#!/usr/bin/env python3
"""Re-enrich CMS itinerary day plans (categorized activities) via Groq."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from database import SessionLocal
from schemas.itineraries import ItineraryDayNested
from schemas.package_import import (
    ExtractedItineraryDayDraft,
    ExtractedItineraryDraft,
    ExtractedItineraryHotelDraft,
    ExtractedItineraryInclusionDraft,
)
from services.groq_extract import enrich_itinerary_day_plans
from services.itineraries import itinerary_query_with_nested, sync_itinerary_days


def _itinerary_draft_from_orm(itinerary) -> ExtractedItineraryDraft:
    return ExtractedItineraryDraft(
        title=itinerary.title,
        slug=itinerary.slug,
        tagline=itinerary.tagline,
        overview=itinerary.overview,
        duration_label=itinerary.duration_label,
        duration_days=itinerary.duration_days,
        starting_price=int(itinerary.starting_price),
        price_on_request=False,
        price_note=itinerary.price_note,
        days=[
            ExtractedItineraryDayDraft(
                day_number=day.day_number,
                title=day.title,
                description=day.description,
                activities=list(day.activities or []),
                sort_order=day.sort_order,
            )
            for day in sorted(itinerary.days, key=lambda d: d.sort_order)
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
            for hotel in sorted(itinerary.hotels, key=lambda h: h.sort_order)
        ],
        inclusions=[
            ExtractedItineraryInclusionDraft(
                kind=inc.kind,
                text=inc.text,
                sort_order=inc.sort_order,
            )
            for inc in sorted(itinerary.inclusions, key=lambda i: i.sort_order)
        ],
        highlights=[],
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", help="Itinerary slug (e.g. gujarat-pilgrimage-itinerary)")
    parser.add_argument(
        "--pdf-text-file",
        help="Optional path to raw PDF text to improve enrichment accuracy",
    )
    args = parser.parse_args()

    pdf_text = ""
    if args.pdf_text_file:
        pdf_text = Path(args.pdf_text_file).read_text(encoding="utf-8")

    with SessionLocal() as db:
        itinerary = itinerary_query_with_nested(db).filter_by(slug=args.slug).one_or_none()
        if itinerary is None:
            raise SystemExit(f"Itinerary not found: {args.slug}")

        draft = _itinerary_draft_from_orm(itinerary)
        enriched = enrich_itinerary_day_plans(draft, pdf_text=pdf_text)

        nested_days = [
            ItineraryDayNested.model_validate(day.model_dump())
            for day in enriched.days
        ]
        sync_itinerary_days(db, itinerary, nested_days)
        db.commit()

        print(f"Updated {len(nested_days)} days for itinerary '{args.slug}':")
        for day in nested_days:
            print(f"\nDay {day.day_number}: {day.title}")
            print(f"  {day.description}")
            for activity in day.activities:
                print(f"  - {activity}")


if __name__ == "__main__":
    main()
