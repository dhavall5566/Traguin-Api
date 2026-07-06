#!/usr/bin/env python3
"""Insert CH-006 Chandigarh premium family package + itinerary (internal / unpublished)."""

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
)
from services.packages import package_query_with_nested, sync_package_highlights, sync_package_moods
from services.travel_moods import travel_moods_for_package
from utils.db import commit_or_raise

PUNJAB_DESTINATION_ID = "d4119569-a154-460e-af8e-6eb006ea76f9"
PACKAGE_SLUG = "ch-006-beautiful-city-sights-sukhna-lake-chandigarh-family-tour"
ITINERARY_SLUG = "ch-006-beautiful-city-chandigarh-itinerary"

PACKAGE = PackageCreate(
    slug=PACKAGE_SLUG,
    serial_code="CH-006",
    traguin_tour_code="TRAGUIN-CH-006",
    destination_id=PUNJAB_DESTINATION_ID,
    title="Beautiful City Sights & Sukhna Lake Premium Chandigarh Family Tour",
    duration_label="02 Nights / 03 Days",
    price=0,
    rating=Decimal("4.9"),
    is_featured=False,
    featured_sort_order=None,
    is_published=False,
    highlights=[
        PackageHighlightNested(
            text="Serial code CH-006 | TRAGUIN tour code TRAGUIN-CH-006",
            sort_order=1,
        ),
        PackageHighlightNested(
            text="State / Country: Chandigarh, India | Category: Premium Family Tour",
            sort_order=2,
        ),
        PackageHighlightNested(
            text="Destinations: Chandigarh (The Beautiful City Hub) • Sukhna Lake • Rock Garden",
            sort_order=3,
        ),
        PackageHighlightNested(
            text="Ideal for: Families, Leisure Seekers & Modernist Enthusiasts",
            sort_order=4,
        ),
        PackageHighlightNested(
            text="Best season: October to April (Perfect Autumn & Winter)",
            sort_order=5,
        ),
        PackageHighlightNested(
            text="Starting price: On Request (Premium Collection)",
            sort_order=6,
        ),
        PackageHighlightNested(
            text="Private chauffeur multi-row luxury SUV, premium city-center stays, all breakfasts included",
            sort_order=7,
        ),
        PackageHighlightNested(
            text="Fast-track entry facilitation for UNESCO Capitol Complex zone",
            sort_order=8,
        ),
        PackageHighlightNested(
            text="Exclusive sunset cruise package at Sukhna Lake",
            sort_order=9,
        ),
        PackageHighlightNested(
            text="TRAGUIN Signature Experience: private family styling tips, custom itineraries, high-tier vehicle upgrades",
            sort_order=10,
        ),
        PackageHighlightNested(
            text="Shopping: Phulkari embroidery, Punjabi juttis (Sector 22), designer artifacts, organic grain gifts",
            sort_order=11,
        ),
        PackageHighlightNested(
            text="Cuisine: Amritsari Kulchas, Dal Makhani, lassi at Sector 26 or Sector 7 fine dining",
            sort_order=12,
        ),
        PackageHighlightNested(
            text="Travel note: Capitol Complex inner government wings need prior permissions — TRAGUIN desk facilitates on request",
            sort_order=13,
        ),
        PackageHighlightNested(
            text="Travel note: Book 3–4 weeks ahead for premium 5-star property allocation",
            sort_order=14,
        ),
    ],
    moods=["Family", "Luxury", "Cultural"],
)

ITINERARY = ItineraryCreate(
    slug=ITINERARY_SLUG,
    destination_id=PUNJAB_DESTINATION_ID,
    title="Beautiful City Sights & Sukhna Lake Premium Chandigarh Family Tour",
    duration_label="02 Nights / 03 Days",
    duration_days=3,
    starting_price=0,
    price_note="On Request (Premium Collection)",
    rating=Decimal("4.9"),
    review_count=0,
    tagline="An Elite Urban Retreat to India's Most Organized City Filled with Curated Experiences & Modernist Splendor",
    overview=(
        "Welcome to Chandigarh, a stunning triumph of modern design and pristine green living, famously envisioned by "
        "the master architect Le Corbusier. This exclusive Best Chandigarh Tour Package is thoughtfully orchestrated to "
        "serve as a high-end, comfortable, and luxury Chandigarh Family Tour. Specially designed by TRAGUIN, this short "
        "family getaway ensures minimal travel exhaustion, spacious accommodation blocks, handpicked hotels, and "
        "dedicated luxury transportation.\n\n"
        "Whether you are cruising the calm waters of Sukhna Lake or walking past the eccentric masterpieces of the Rock "
        "Garden, this urban paradise offers families a sophisticated escape. Experience unmatched professional handling "
        "and personalized assistance every step of the way with the iconic TRAGUIN signature quality touch.\n\n"
        "TRAGUIN Curated Experience Note: Your premium trip includes a private, chauffeured multi-row luxury SUV, "
        "premium stays at top-rated city center resorts, all breakfasts included, special fast-track entry to "
        "monumental zones, and an exclusive sunset cruise package at Sukhna Lake.\n\n"
        "Why visit the beautiful city of Chandigarh? Chandigarh remains one of the country's most searched metropolitan "
        "getaways for families seeking clean air, magnificent gardens, and sophisticated architecture. This Premium "
        "Chandigarh Experience introduces you to world-famous attractions, popular Instagram locations, and rich "
        "shopping and food highlights. It serves as an idyllic Chandigarh Honeymoon Package or a pleasant corporate break "
        "due to its scenic beauty and iconic urban landmarks, making it a stellar highlight among TRAGUIN Chandigarh Packages."
    ),
    seo_title="CH-006 | Beautiful City Sights & Sukhna Lake Chandigarh Family Tour | TRAGUIN",
    seo_description=(
        "Premium 02 Nights / 03 Days Chandigarh family package (CH-006 / TRAGUIN-CH-006): Sukhna Lake sunset cruise, "
        "Rock Garden, Rose Garden, Capitol Complex UNESCO site, Sector 17 shopping, and handpicked 5-star hotel options."
    ),
    is_featured=False,
    featured_sort_order=None,
    is_published=False,
    highlights=[
        ItineraryHighlightNested(text="Sukhna Lake Waterfront & Sunset Boat Cruise", sort_order=1),
        ItineraryHighlightNested(text="Rock Garden — Nek Chand's open-air masterpiece", sort_order=2),
        ItineraryHighlightNested(text="Zakir Hussain Rose Garden — Asia's largest of its kind", sort_order=3),
        ItineraryHighlightNested(text="Capitol Complex UNESCO World Heritage & Open Hand Monument", sort_order=4),
        ItineraryHighlightNested(text="Sector 17 upscale shopping boulevard & musical fountains", sort_order=5),
        ItineraryHighlightNested(
            text="Curated by TRAGUIN Experts: historical context, family entertainment, gourmet suggestions",
            sort_order=6,
        ),
        ItineraryHighlightNested(
            text="Premium handpicked accommodations pre-audited for health, security, and guest care",
            sort_order=7,
        ),
    ],
    days=[
        ItineraryDayNested(
            day_number=1,
            title="Arrival & Elevated Sukhna Lake Sunset Experience",
            description=(
                "Welcome reception, luxury check-in & a serene evening on the shores. Your premium family holiday begins "
                "the moment you arrive at Chandigarh Airport or Railway Station. A dedicated corporate representative from "
                "TRAGUIN will welcome you warmly and escort your family in a spacious private luxury vehicle to your "
                "handpicked premium hotel. Take time for a smooth check-in and lunch at your own leisure. In the late "
                "afternoon, embark on an exquisite tour of the iconic Sukhna Lake—a peaceful oasis lying at the foothills "
                "of the Shivalik range. Enjoy a private, relaxing boat ride across the calm blue waters while taking in a "
                "spectacular sunset. Afterward, enjoy a family walk along the lively promenade, perfect for photography "
                "points and a relaxed evening drink at the lakefront lounge."
            ),
            activities=[
                "Sightseeing Included: Sukhna Lake Waterfront, Sunset Boat Cruise",
                "Evening Experience: Leisure family walk & high-tea at the lake club",
                "Meals Included: Premium Welcome Drink & Luxury Buffet Dinner",
                "Overnight Stay: Selected Premium 5-Star Hotel in Chandigarh",
            ],
            sort_order=1,
        ),
        ItineraryDayNested(
            day_number=2,
            title="Architectural Wonders & Famous Gardens",
            description=(
                "Eccentric chronicles: Rock Garden, Rose Garden & premium Sector shopping. Savor a magnificent buffet "
                "breakfast before stepping out to discover the most celebrated top tourist places in Chandigarh. Your "
                "first stop is the world-renowned Rock Garden, a brilliant maze of interlinked open-air galleries built "
                "entirely from industrial and domestic waste by Nek Chand. Next, cross over to the Zakir Hussain Rose "
                "Garden, Asia's largest botanical garden of its kind, displaying over 50,000 rose bushes spanning hundreds "
                "of rare varieties. In the evening, your private luxury transport will drop you off at Sector 17—"
                "Chandigarh's upscale commercial promenade—where your family can enjoy high-end brand shopping, premium "
                "cafes, and spectacular musical fountain shows."
            ),
            activities=[
                "Sightseeing Included: Rock Garden, Rose Garden, Sector 17 Shopping Boulevard",
                "Food Suggestions: Authentic gourmet Punjabi cuisine at iconic fine dining venues",
                "Meals Included: Gourmet Buffet Breakfast Only",
                "Overnight Stay: Selected Premium 5-Star Hotel in Chandigarh",
            ],
            sort_order=2,
        ),
        ItineraryDayNested(
            day_number=3,
            title="Majestic Capitol Complex & Smooth Departure",
            description=(
                "Le Corbusier's legacy: Capitol Complex & fulfilling homeward drops. After a relaxed breakfast, your "
                "family will explore the prestigious Capitol Complex, a UNESCO World Heritage site housing the magnificent "
                "High Court, Secretariat, and the monumental Open Hand Monument symbol of the city's philosophy. This "
                "architectural marvel offers deep design insights and serves as an exceptional photography point for modern "
                "families. Following checkout, indulge in a final family lunch at a premium boutique cafe before your "
                "private luxury transport provides a smooth drop-off to Chandigarh Airport or Railway Station. Return home "
                "with joyful spirits and unforgettable memories from your premium Luxury Chandigarh Holiday meticulously "
                "curated by TRAGUIN."
            ),
            activities=[
                "Sightseeing Included: Capitol Complex, Open Hand Monument, Sector 35 Cafes",
                "Transfers: Effortless airport/station drops in private luxury vehicle",
                "Meals Included: Gourmet Buffet Breakfast Included",
            ],
            sort_order=3,
        ),
    ],
    hotels=[
        ItineraryHotelNested(
            name="Hotel Mountview Chandigarh / Lemon Tree Premium",
            location="Chandigarh",
            nights_label="02 Nights",
            description="Option 01 — Deluxe tier handpicked premium city hotel.",
            stars=4,
            category_label="Deluxe",
            room_type="Executive Deluxe Room",
            meal_plan="CP Plan (Breakfast Only)",
            sort_order=1,
        ),
        ItineraryHotelNested(
            name="Hyatt Regency Chandigarh / Radisson Chandigarh",
            location="Chandigarh",
            nights_label="02 Nights",
            description="Option 02 — Premium tier city-center luxury property.",
            stars=5,
            category_label="Premium",
            room_type="Club View Room",
            meal_plan="CP Plan (Breakfast Only)",
            sort_order=2,
        ),
        ItineraryHotelNested(
            name="Taj Chandigarh / JW Marriott Hotel Chandigarh",
            location="Chandigarh",
            nights_label="02 Nights",
            description="Option 03 — Luxury tier premier city landmark hotels.",
            stars=5,
            category_label="Luxury",
            room_type="Luxury Premier Room",
            meal_plan="Gourmet Breakfast Plan",
            sort_order=3,
        ),
        ItineraryHotelNested(
            name="The Oberoi Sukhvilas Spa Resort, New Chandigarh",
            location="New Chandigarh",
            nights_label="02 Nights",
            description="Option 04 — Ultra Luxury resort escape near the city.",
            stars=5,
            category_label="Ultra Luxury",
            room_type="Premier Luxury Tent / Villa",
            meal_plan="Bespoke Curated Meal Plan",
            sort_order=4,
        ),
    ],
    inclusions=[
        ItineraryInclusionNested(
            kind="included",
            text="02 Nights premium accommodation in top-rated handpicked city hotels",
            sort_order=1,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Daily gourmet buffet breakfast across all designated hotel stays",
            sort_order=2,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Chauffeured private luxury AC vehicle for all transfers & sightseeing tours",
            sort_order=3,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Round-the-clock professional TRAGUIN assistance and coordination",
            sort_order=4,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Private boating tickets for the sunset cruise experience at Sukhna Lake",
            sort_order=5,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Fast-track entry facilitation for UNESCO Capitol Complex zone",
            sort_order=6,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="All city tolls, parking fees, driver surcharges, and state taxes",
            sort_order=7,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Inbound/outbound flight tickets or interstate rail bookings",
            sort_order=8,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Personal hotel expenditures like mini-bar, laundry, and room service",
            sort_order=9,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Main lunch and dinner meals unless specified in individual hotel options",
            sort_order=10,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Camera tickets or optional guided trail expenses within gardens",
            sort_order=11,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Comprehensive individual medical or holiday travel insurance",
            sort_order=12,
        ),
    ],
)


def main() -> None:
    with SessionLocal() as db:
        destination = db.get(Destination, PUNJAB_DESTINATION_ID)
        if destination is None:
            print("Punjab destination not found.", file=sys.stderr)
            sys.exit(1)

        existing_pkg = db.scalar(select(Package).where(Package.slug == PACKAGE_SLUG))
        if existing_pkg:
            print(f"Package already exists: {PACKAGE_SLUG} ({existing_pkg.id})")
            package = existing_pkg
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

        commit_or_raise(db)

        itin_row = db.scalar(select(Itinerary).where(Itinerary.slug == ITINERARY_SLUG))
        pkg_row = package_query_with_nested(db).filter_by(id=package.id).one()
        itin_row = itinerary_query_with_nested(db).filter_by(id=itin_row.id).one()
        print(f"Linked package {pkg_row.slug} -> itinerary {itin_row.slug}")
        print(f"Published: package={pkg_row.is_published} itinerary={itin_row.is_published}")
        print(
            f"Highlights: pkg={len(pkg_row.highlights)} itin={len(itin_row.highlights)} | "
            f"Days: {len(itin_row.days)} | Hotels: {len(itin_row.hotels)} | "
            f"Inclusions: {len(itin_row.inclusions)}"
        )


if __name__ == "__main__":
    main()
