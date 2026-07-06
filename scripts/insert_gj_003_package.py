#!/usr/bin/env python3
"""Insert GJ-003 Sasan Gir package + itinerary from brochure content."""

from __future__ import annotations

import sys
from decimal import Decimal

from sqlalchemy import select

from database import SessionLocal
from models.destinations import Destination
from models.itineraries import Itinerary
from models.packages import Package
from schemas.itineraries import (
    ItineraryCreate,
    ItineraryDayNested,
    ItineraryHighlightNested,
    ItineraryHotelNested,
    ItineraryInclusionNested,
)
from schemas.packages import PackageCreate, PackageHighlightNested
from services.itineraries import (
    itinerary_query_with_nested,
    sync_itinerary_days,
    sync_itinerary_highlights,
    sync_itinerary_hotels,
    sync_itinerary_inclusions,
    sync_itinerary_nested_content,
)
from services.media_from_pexels import apply_pexels_images_to_package
from services.package_image_specs import GJ_003_PEXELS_IMAGES
from services.packages import package_query_with_nested, sync_package_highlights, sync_package_moods
from services.travel_moods import travel_moods_for_package
from utils.db import commit_or_raise

GUJARAT_DESTINATION_ID = "07be1b4e-0016-4caa-a680-c130ba86b9f7"
PACKAGE_SLUG = "gj-003-sasan-gir-wildlife-safari"
ITINERARY_SLUG = "gj-003-sasan-gir-itinerary"

PACKAGE = PackageCreate(
    slug=PACKAGE_SLUG,
    destination_id=GUJARAT_DESTINATION_ID,
    title="Sasan Gir Wildlife Safari",
    duration_label="03 Nights / 04 Days",
    price=0,
    rating=Decimal("4.9"),
    is_featured=True,
    featured_sort_order=3,
    is_published=True,
    highlights=[
        PackageHighlightNested(text="Premium private Gir Jungle Safari with naturalist", sort_order=1),
        PackageHighlightNested(text="Handpicked luxury eco-resorts in Sasan Gir", sort_order=2),
        PackageHighlightNested(text="Dedicated luxury chauffeur-driven SUV transfers", sort_order=3),
        PackageHighlightNested(text="Devalia Interpretation Zone & Kamleshwar Dam visit", sort_order=4),
        PackageHighlightNested(text="Maldhari tribal settlement cultural walk", sort_order=5),
        PackageHighlightNested(text="TRAGUIN 24/7 premium concierge support", sort_order=6),
    ],
    moods=["Wildlife", "Luxury", "Family"],
)

ITINERARY = ItineraryCreate(
    slug=ITINERARY_SLUG,
    destination_id=GUJARAT_DESTINATION_ID,
    title="Sasan Gir Wildlife Safari",
    duration_label="03 Nights / 04 Days",
    duration_days=4,
    starting_price=0,
    price_note="On Request (Premium Customised)",
    rating=Decimal("4.9"),
    review_count=0,
    tagline="Welcome to the Lion's Kingdom",
    overview=(
        "Embark on an extraordinary wildlife expedition into Sasan Gir, the last refuge of the "
        "majestic Asiatic Lion. This bespoke TRAGUIN premium journey blends untamed wilderness, "
        "raw natural beauty, and ultra-luxury hospitality with private luxury SUV transfers, "
        "handpicked wilderness resorts, pre-booked VIP safari allocations, and immersive natural "
        "and cultural experiences across Gujarat's most iconic wildlife sanctuary."
    ),
    seo_title="GJ-003 | Sasan Gir Wildlife Safari | TRAGUIN Premium Gujarat Tour",
    seo_description=(
        "Luxury 03 Nights / 04 Days Sasan Gir National Park safari package (GJ-003) with private "
        "Gir jungle safari, premium eco-resorts, Devalia zone visit, and curated cultural "
        "experiences. Ideal for wildlife enthusiasts, families, and luxury travelers."
    ),
    is_featured=True,
    featured_sort_order=3,
    is_published=True,
    highlights=[
        ItineraryHighlightNested(text="Asiatic Lion Safari", sort_order=1),
        ItineraryHighlightNested(text="Devalia Interpretation Zone", sort_order=2),
        ItineraryHighlightNested(text="Kamleshwar Dam & Crocodile Park", sort_order=3),
        ItineraryHighlightNested(text="Maldhari Tribal Settlement", sort_order=4),
        ItineraryHighlightNested(text="Luxury Eco-Resort Stay", sort_order=5),
    ],
    days=[
        ItineraryDayNested(
            day_number=1,
            title="Arrival at Rajkot/Diu & Transfer to Sasan Gir",
            description=(
                "Arrive at Rajkot or Diu airport and meet your private luxury SUV chauffeur for a "
                "scenic transfer through golden countryside to Sasan Gir. Check in at your handpicked "
                "luxury eco-resort with a refreshing welcome experience. After a lavish lunch, relax "
                "at the pool or private sundeck, then enjoy an evening nature walk along the Hiran "
                "River trail before a candlelight gourmet dinner."
            ),
            activities=[
                "Sightseeing Included: Scenic countryside drive, orientation walk around the Hiran River trail",
                "Optional Activities: Therapeutic wellness spa session at the luxury resort",
                "Evening Experience: Tribal folk performance by the local Siddi community around a warm campfire",
                "Overnight Stay: Handpicked Luxury Resort (Sasan Gir)",
                "Meals Included: Lunch & Dinner",
            ],
            sort_order=1,
        ),
        ItineraryDayNested(
            day_number=2,
            title="Thrilling Asiatic Lion Safari & Deep Wilderness Trail",
            description=(
                "Begin before dawn for the highlight Gir Jungle Safari in a private open-top 4x4 with a "
                "senior certified naturalist. Track pugmarks through teak forests and watch for Asiatic "
                "lion prides, leopards, and exotic birds. Return for a hearty breakfast, then visit the "
                "Gir Interpretation Zone at Devalia. Capture sunset over the forest landscape as dusk settles."
            ),
            activities=[
                "Sightseeing Included: Premium Morning Gir Jungle Safari, Devalia Interpretation Zone exploration",
                "Optional Activities: Private interactive session with a senior wildlife researcher and photographer",
                "Evening Experience: Relaxed documentary screening on Lion Conservation followed by high tea",
                "Overnight Stay: Handpicked Luxury Resort (Sasan Gir)",
                "Meals Included: Breakfast, Lunch & Dinner",
            ],
            sort_order=2,
        ),
        ItineraryDayNested(
            day_number=3,
            title="Secondary Safari Zone / Crocodile Park & Culture Walk",
            description=(
                "Choose an optional second morning safari or enjoy a peaceful breakfast followed by a guided "
                "visit to Kamleshwar Dam and the Crocodile Breeding Center. In the afternoon, visit a local "
                "Maldhari settlement and browse artisan workshops for bandhani textiles and organic honey. "
                "Conclude with an exclusive premium bush dinner under the stars."
            ),
            activities=[
                "Sightseeing Included: Kamleshwar Dam visit, Maldhari tribal settlement walk, local craft village tour",
                "Optional Activities: Secondary morning/afternoon jungle safari track",
                "Evening Experience: Exclusive Premium Bush Dinner setup with live instrumental ambient music",
                "Overnight Stay: Handpicked Luxury Resort (Sasan Gir)",
                "Meals Included: Breakfast, Lunch & Dinner",
            ],
            sort_order=3,
        ),
        ItineraryDayNested(
            day_number=4,
            title="Homeward Journey with Unforgettable Memories",
            description=(
                "Wake to birdsong and enjoy an exquisite champagne breakfast on the resort lawns. Stroll "
                "through organic mango orchards for final photographs before checkout. Transfer back to "
                "Rajkot or Diu airport in your private luxury SUV, with an optional stop at local souvenir markets."
            ),
            activities=[
                "Sightseeing Included: Comfortable return transit, short stopover at local souvenir markets",
                "Meals Included: Breakfast",
            ],
            sort_order=4,
        ),
    ],
    hotels=[
        ItineraryHotelNested(
            name="The Fern Gir Forest Resort / Similar",
            location="Sasan Gir",
            nights_label="03 Nights",
            description="Deluxe tier handpicked luxury eco-resort embedded in nature.",
            stars=4,
            category_label="Deluxe",
            room_type="Fern Club Room",
            meal_plan="All Meals (AP)",
            sort_order=1,
        ),
        ItineraryHotelNested(
            name="Woods at Sasan / Similar",
            location="Sasan Gir",
            nights_label="03 Nights",
            description="Premium tier pavilion stay with forest views.",
            stars=5,
            category_label="Premium",
            room_type="Luxury Pavilion",
            meal_plan="All Meals (AP)",
            sort_order=2,
        ),
        ItineraryHotelNested(
            name="Aramness Gir National Park / Similar",
            location="Sasan Gir",
            nights_label="03 Nights",
            description="Luxury forest kothi with refined wilderness hospitality.",
            stars=5,
            category_label="Luxury",
            room_type="Luxury Forest Kothi",
            meal_plan="All Meals (AP)",
            sort_order=3,
        ),
        ItineraryHotelNested(
            name="The Taj Gateway Hotel Gir Forest / Similar",
            location="Sasan Gir",
            nights_label="03 Nights",
            description="Ultra-luxury villas and suites for discerning wildlife travelers.",
            stars=5,
            category_label="Ultra Luxury",
            room_type="Executive Suite / Luxury Villa",
            meal_plan="All Meals (AP)",
            sort_order=4,
        ),
    ],
    inclusions=[
        ItineraryInclusionNested(
            kind="included",
            text="03 Nights premium accommodation in handpicked elite wildlife resorts",
            sort_order=1,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Full board dining — daily breakfast, gourmet lunches, and premium dinners",
            sort_order=2,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Private dedicated luxury SUV for all airport transits and sightseeing",
            sort_order=3,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="01 Premium Private 4x4 Gir Jungle Safari with permits and naturalist guide",
            sort_order=4,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Welcome amenities, guided nature trails, and Maldhari cultural interaction walks",
            sort_order=5,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="TRAGUIN 24/7 priority concierge support throughout the trip",
            sort_order=6,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Domestic and international airfare or rail tickets to/from Gujarat",
            sort_order=7,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Additional safaris, personal expenses, laundry, and premium alcoholic beverages",
            sort_order=8,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="High-end professional video camera permits inside the national park",
            sort_order=9,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Travel/medical insurance and gratuities for drivers, naturalists, and hotel staff",
            sort_order=10,
        ),
    ],
)


def main() -> None:
    with SessionLocal() as db:
        destination = db.get(Destination, GUJARAT_DESTINATION_ID)
        if destination is None:
            print("Gujarat destination not found.", file=sys.stderr)
            sys.exit(1)

        existing_pkg = db.scalar(select(Package).where(Package.slug == PACKAGE_SLUG))
        if existing_pkg:
            print(f"Package already exists: {PACKAGE_SLUG} ({existing_pkg.id})")
            package = existing_pkg
            moods = travel_moods_for_package(PACKAGE.slug, PACKAGE.moods)
            current_moods = [m.mood for m in package.moods]
            if current_moods != moods:
                sync_package_moods(db, package, moods)
                print(f"  Updated moods: {current_moods} -> {moods}")
        else:
            pkg_data = PACKAGE.model_dump()
            highlights = pkg_data.pop("highlights")
            pkg_data.pop("moods", None)
            moods = travel_moods_for_package(PACKAGE.slug, PACKAGE.moods)
            package = Package(**pkg_data)
            db.add(package)
            db.flush()
            sync_package_highlights(db, package, highlights)
            sync_package_moods(db, package, moods)
            print(f"Created package: {package.slug} ({package.id})")

        existing_itin = db.scalar(select(Itinerary).where(Itinerary.slug == ITINERARY_SLUG))
        if existing_itin:
            print(f"Itinerary already exists: {ITINERARY_SLUG} ({existing_itin.id})")
            itinerary = itinerary_query_with_nested(db).filter_by(id=existing_itin.id).one()
            if itinerary.package_id != package.id:
                itinerary.package_id = package.id
            sync_itinerary_nested_content(db, itinerary, ITINERARY)
            print(
                f"  Synced nested content: days={len(ITINERARY.days)} "
                f"hotels={len(ITINERARY.hotels)} inclusions={len(ITINERARY.inclusions)}"
            )
        else:
            itin_data = ITINERARY.model_dump()
            itin_data["package_id"] = package.id
            highlights = itin_data.pop("highlights")
            days = itin_data.pop("days")
            hotels = itin_data.pop("hotels")
            inclusions = itin_data.pop("inclusions")
            itin_data.pop("gallery_media_ids", None)

            itinerary = Itinerary(**itin_data)
            db.add(itinerary)
            db.flush()
            sync_itinerary_highlights(db, itinerary, highlights)
            sync_itinerary_days(db, itinerary, days)
            sync_itinerary_hotels(db, itinerary, hotels)
            sync_itinerary_inclusions(db, itinerary, inclusions)
            print(f"Created itinerary: {itinerary.slug} ({itinerary.id})")

        assets = apply_pexels_images_to_package(
            db,
            package=package,
            itinerary=itinerary,
            image_specs=GJ_003_PEXELS_IMAGES,
        )
        commit_or_raise(db)
        itinerary = itinerary_query_with_nested(db).filter_by(id=itinerary.id).one()
        package = package_query_with_nested(db).filter_by(id=package.id).one()
        print(f"Linked package {package.slug} -> itinerary {itinerary.slug}")
        print(f"Days: {len(itinerary.days)} | Hotels: {len(itinerary.hotels)} | Inclusions: {len(itinerary.inclusions)}")
        if assets:
            print(f"Pexels images attached: {len(assets)} (hero: {assets[0].slug})")
        else:
            print("Warning: no Pexels images were attached (check PEXELS_API_KEY).")


if __name__ == "__main__":
    main()
