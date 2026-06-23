#!/usr/bin/env python3
"""Insert HP-003 Shimla Manali Classic package from brochure content."""

from __future__ import annotations

import sys
from decimal import Decimal

from sqlalchemy import select

from database import SessionLocal
from models.destinations import Destination
from schemas.itineraries import (
    ItineraryCreate,
    ItineraryDayNested,
    ItineraryHighlightNested,
    ItineraryHotelNested,
    ItineraryInclusionNested,
)
from schemas.packages import PackageCreate, PackageHighlightNested
from services.package_image_specs import HP_003_PEXELS_IMAGES
from services.package_insert import upsert_gujarat_package
from utils.db import commit_or_raise

HIMACHAL_SLUG = "himachal"


def build_package(destination_id: str) -> PackageCreate:
    return PackageCreate(
        slug="hp-003-shimla-manali-classic-alpine-luxury",
        destination_id=destination_id,
    title="Shimla Manali Classic — Alpine Luxury & Escapes",
    duration_label="05 Nights / 06 Days",
    price=0,
    rating=Decimal("4.9"),
    is_featured=True,
    featured_sort_order=6,
    is_published=True,
    highlights=[
        PackageHighlightNested(text="Shimla colonial heritage — Mall Road, Ridge & Viceregal Lodge", sort_order=1),
        PackageHighlightNested(text="Kufri snow peaks, cedar forests & panoramic Himalayan views", sort_order=2),
        PackageHighlightNested(text="Scenic Kullu Valley drive along the Beas River", sort_order=3),
        PackageHighlightNested(text="Solang Valley snow fields, ropeway & adventure sports", sort_order=4),
        PackageHighlightNested(text="Manali — Hadimba Temple, Vashisht springs & Old Manali cafes", sort_order=5),
        PackageHighlightNested(text="Private Innova Crysta with TRAGUIN 24/7 concierge", sort_order=6),
    ],
    moods=["Family", "Romantic", "Nature"],
    )


def build_itinerary(destination_id: str) -> ItineraryCreate:
    return ItineraryCreate(
        slug="hp-003-shimla-manali-itinerary",
        destination_id=destination_id,
    title="Shimla Manali Classic — Alpine Luxury & Escapes",
    duration_label="05 Nights / 06 Days",
    duration_days=6,
    starting_price=0,
    price_note="On Request (Premium Curated)",
    rating=Decimal("4.9"),
    review_count=0,
    tagline="Alpine Luxury Across the Queen of Hill Stations",
    overview=(
        "Discover the ultimate Himachal family tour — a premium retreat unveiling majestic peaks, lush valleys, "
        "and charming colonial heritage from historic Shimla to snow-draped Manali. This TRAGUIN bespoke journey "
        "features private alpine chauffeur transfers, handpicked mountain and riverside resorts, gourmet MAPAI "
        "dining, and curated experiences from Kufri panoramas to Solang Valley adventures."
    ),
    seo_title="HP-003 | Shimla Manali Classic Alpine Luxury | TRAGUIN Premium Himachal Tour",
    seo_description=(
        "Luxury 05 Nights / 06 Days Himachal Pradesh package (HP-003) covering Shimla, Kufri, Kullu Valley, "
        "Manali, and Solang Valley with premium stays and private transfers. Ideal for families, honeymooners, "
        "and luxury retreat seekers."
    ),
    is_featured=True,
    featured_sort_order=6,
    is_published=True,
    highlights=[
        ItineraryHighlightNested(text="Shimla & Kufri Excursion", sort_order=1),
        ItineraryHighlightNested(text="Kullu Valley Scenic Drive", sort_order=2),
        ItineraryHighlightNested(text="Solang Valley Adventure", sort_order=3),
        ItineraryHighlightNested(text="Manali Heritage & Old Manali", sort_order=4),
        ItineraryHighlightNested(text="Luxury Mountain & Riverside Stays", sort_order=5),
    ],
    days=[
        ItineraryDayNested(
            day_number=1,
            title="Arrival in Delhi / Chandigarh to Shimla",
            description=(
                "Your premium Himachal experience begins with a warm welcome at Delhi or Chandigarh airport "
                "or railway station. Board your luxury vehicle for a scenic uphill drive through terraced orchards "
                "and pine forests to Shimla. Check into your handpicked mountain resort with sweeping valley views "
                "and enjoy a relaxing evening in the crisp mountain air."
            ),
            activities=[
                "Sightseeing Included: Scenic Himalayan Expressway drive, Pinjore timber trail vistas",
                "Evening Experience: Private veranda high-tea with valley views, arranged by TRAGUIN",
                "Overnight Stay: Shimla (premium / luxury mountain resort)",
                "Meals Included: Welcome refreshment & gourmet buffet dinner",
            ],
            sort_order=1,
        ),
        ItineraryDayNested(
            day_number=2,
            title="Shimla & Kufri Excursion",
            description=(
                "Morning excursion to Kufri for breathtaking Himalayan snow-range views, cedar forests, and "
                "photography points. Return to Shimla to explore colonial heritage — Mall Road, the Ridge, "
                "Christ Church, Scandal Point, and the grand Viceregal Lodge."
            ),
            activities=[
                "Sightseeing Included: Kufri Fun World, Viceregal Lodge, The Ridge, Mall Road, Christ Church, Scandal Point",
                "Optional Activities: Pony trekking in Kufri trails or heritage indoor tour of the Viceregal ballroom",
                "Overnight Stay: Shimla (premium / luxury mountain resort)",
                "Meals Included: Premium breakfast & luxury dinner",
            ],
            sort_order=2,
        ),
        ItineraryDayNested(
            day_number=3,
            title="Shimla to Manali via Kullu Valley",
            description=(
                "Drive through spellbinding Kullu Valley tracing the roaring Beas River past granite cliffs "
                "and emerald pine woodlands. Stop at Pandoh Dam and Kullu handloom factories for authentic "
                "pashmina and woolens before arriving at your luxury riverside hotel in Manali."
            ),
            activities=[
                "Sightseeing Included: Kullu Valley drive, Pandoh Dam, Hanogi Mata Temple overlooks, Beas River vistas",
                "Evening Experience: Riverside bonfire with live traditional music recommendations by TRAGUIN experts",
                "Overnight Stay: Manali (premium customised riverside resort)",
                "Meals Included: Breakfast & lavish buffet dinner",
            ],
            sort_order=3,
        ),
        ItineraryDayNested(
            day_number=4,
            title="Manali Solang Valley Excursion",
            description=(
                "Dedicated day at Solang Valley — globally renowned for glaciers, snowcapped peaks, and outdoor "
                "sports. Enjoy optional paragliding, zorbing, and scenic cable-car ropeway rides. Atal Tunnel or "
                "Rohtang Pass can be added by your TRAGUIN consultant subject to permissions."
            ),
            activities=[
                "Sightseeing Included: Solang Valley meadow, snow point viewpoints, adventure activity arenas",
                "Optional Activities: Tandem paragliding, quad biking over snow, or Atal Tunnel north-portal crossing",
                "Overnight Stay: Manali (premium customised riverside resort)",
                "Meals Included: Premium breakfast & chef's special dinner",
            ],
            sort_order=4,
        ),
        ItineraryDayNested(
            day_number=5,
            title="Manali Local Sightseeing",
            description=(
                "Explore Manali's cultural tapestry — the 16th-century Hadimba Temple in Dhungri Deodar forests, "
                "sacred Vashisht hot water springs, Tibetan Monastery, and the bohemian cafes and boutiques of "
                "Old Manali."
            ),
            activities=[
                "Sightseeing Included: Hadimba Devi Temple, Vashisht Village & springs, Tibetan Monastery, Old Manali lanes",
                "Evening Experience: Leisurely shopping walk on Manali Mall Road with custom local food suggestions",
                "Overnight Stay: Manali (premium customised riverside resort)",
                "Meals Included: Breakfast & farewell grand dinner",
            ],
            sort_order=5,
        ),
        ItineraryDayNested(
            day_number=6,
            title="Manali to Delhi / Chandigarh Departure",
            description=(
                "Enjoy a final luxury breakfast facing the mist-draped Beas valley before checkout. Your private "
                "vehicle drives you back to Chandigarh or New Delhi airport or railway station with unforgettable "
                "memories curated by TRAGUIN."
            ),
            activities=[
                "Transfers Included: Private door-to-door highway departure drop-off",
                "Meals Included: Lavish buffet breakfast",
            ],
            sort_order=6,
        ),
    ],
    hotels=[
        ItineraryHotelNested(
            name="Hotel Willow Banks / East Bourne Resort / Similar",
            location="Shimla (2N)",
            nights_label="02 Nights",
            description="Deluxe mountain resort in Shimla.",
            stars=4,
            category_label="Deluxe",
            room_type="Executive Room",
            meal_plan="MAPAI (Breakfast & Dinner)",
            sort_order=1,
        ),
        ItineraryHotelNested(
            name="Radisson Hotel Shimla / Sterling Kufri / Similar",
            location="Shimla (2N)",
            nights_label="02 Nights",
            description="Premium hill resort with valley views.",
            stars=4,
            category_label="Premium",
            room_type="Premium Room",
            meal_plan="MAPAI (Premium Buffet Menu)",
            sort_order=2,
        ),
        ItineraryHotelNested(
            name="The Taj The Trees, Shimla / Welcomhotel / Similar",
            location="Shimla (2N)",
            nights_label="02 Nights",
            description="Luxury mountain hospitality in Shimla.",
            stars=5,
            category_label="Luxury",
            room_type="Luxury Room / Suite",
            meal_plan="MAPAI (Elite Chef Dynamic Menu)",
            sort_order=3,
        ),
        ItineraryHotelNested(
            name="Wildflower Hall, An Oberoi Resort / Similar",
            location="Shimla (2N)",
            nights_label="02 Nights",
            description="Ultra-luxury Oberoi suite experience in the Himalayas.",
            stars=5,
            category_label="Ultra Luxury",
            room_type="Luxury Suite",
            meal_plan="MAPAI (Bespoke Fine Dining)",
            sort_order=4,
        ),
        ItineraryHotelNested(
            name="The Grand Welcome / Solang Valley Resort / Similar",
            location="Manali (3N)",
            nights_label="03 Nights",
            description="Deluxe riverside resort in Manali.",
            stars=4,
            category_label="Deluxe",
            room_type="Executive Room",
            meal_plan="MAPAI (Breakfast & Dinner)",
            sort_order=5,
        ),
        ItineraryHotelNested(
            name="ManuAllaya Resort / Tiaraa Luxury Resort / Similar",
            location="Manali (3N)",
            nights_label="03 Nights",
            description="Premium riverside resort with alpine views.",
            stars=5,
            category_label="Premium",
            room_type="Premium Room",
            meal_plan="MAPAI (Premium Buffet Menu)",
            sort_order=6,
        ),
        ItineraryHotelNested(
            name="The Himalayan Castle / Span Resort & Spa / Similar",
            location="Manali (3N)",
            nights_label="03 Nights",
            description="Luxury spa resort on the Beas riverside.",
            stars=5,
            category_label="Luxury",
            room_type="Luxury Room / Suite",
            meal_plan="MAPAI (Elite Chef Dynamic Menu)",
            sort_order=7,
        ),
        ItineraryHotelNested(
            name="The Oberoi Sukhvilas / Private Ultra Premium Chalet / Similar",
            location="Manali (3N)",
            nights_label="03 Nights",
            description="Ultra-luxury chalet stay near Manali.",
            stars=5,
            category_label="Ultra Luxury",
            room_type="Ultra Premium Chalet / Suite",
            meal_plan="MAPAI (Bespoke Fine Dining)",
            sort_order=8,
        ),
    ],
    inclusions=[
        ItineraryInclusionNested(
            kind="included",
            text="05 nights premium accommodation at handpicked Shimla and Manali resorts",
            sort_order=1,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Daily elaborate breakfasts and multi-cuisine dinners (MAPAI plan)",
            sort_order=2,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Private chauffeur-driven AC Innova Crysta for all transfers and sightseeing",
            sort_order=3,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="TRAGUIN welcome kit, private bonfire session, and 24/7 concierge support",
            sort_order=4,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Driver allowances, tolls, parking, fuel, and applicable taxes",
            sort_order=5,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Airfare or train tickets to/from Delhi or Chandigarh",
            sort_order=6,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Rohtang Pass NGT permits and local shuttle vehicle charges",
            sort_order=7,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Adventure sport fees (paragliding, zorbing, river rafting)",
            sort_order=8,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Personal incidentals, laundry, tips, room service, and travel insurance",
            sort_order=9,
        ),
    ],
)


def get_or_create_himachal_destination(db) -> Destination:
    existing = db.scalar(select(Destination).where(Destination.slug == HIMACHAL_SLUG))
    if existing is not None:
        return existing

    destination = Destination(
        slug=HIMACHAL_SLUG,
        name="Himachal Pradesh",
        country="India",
        region="domestic",
        india_region="north",
        description="Colonial Shimla charm, Kufri alpine vistas, and Manali's snow-draped Himalayan escapes.",
        starting_price=0,
        moods=["Family", "Romantic", "Nature"],
        is_published=True,
    )
    db.add(destination)
    db.flush()
    print(f"Created destination: {destination.slug} ({destination.id})")
    return destination


def main() -> None:
    with SessionLocal() as db:
        destination = get_or_create_himachal_destination(db)
        commit_or_raise(db)

        dest_id = str(destination.id)
        package = build_package(dest_id)
        itinerary = build_itinerary(dest_id)

        print(f"\n--- {package.slug} ---")
        try:
            upsert_gujarat_package(
                db,
                destination_id=dest_id,
                package=package,
                itinerary=itinerary,
                image_specs=HP_003_PEXELS_IMAGES,
            )
        except Exception as exc:
            print(f"Failed {package.slug}: {exc}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
