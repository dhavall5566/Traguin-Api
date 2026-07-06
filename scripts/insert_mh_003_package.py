#!/usr/bin/env python3
"""Insert MH-003 Ajanta Ellora heritage package + itinerary (no images)."""

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
from services.packages import package_query_with_nested, sync_package_highlights, sync_package_moods
from services.travel_moods import travel_moods_for_package
from utils.db import commit_or_raise

MAHARASHTRA_SLUG = "maharashtra"
PACKAGE_SLUG = "mh-003-ajanta-ellora-heritage-tour"
ITINERARY_SLUG = "mh-003-ajanta-ellora-itinerary"

PACKAGE = PackageCreate(
    slug=PACKAGE_SLUG,
    destination_id="00000000-0000-0000-0000-000000000000",  # replaced at runtime
    title="Premium Ajanta Ellora Heritage Tour",
    duration_label="03 Nights / 04 Days",
    price=0,
    rating=Decimal("4.9"),
    is_featured=True,
    featured_sort_order=3,
    is_published=True,
    highlights=[
        PackageHighlightNested(
            text="Private premium SUV (Innova Crysta / luxury sedan) for all transfers and sightseeing",
            sort_order=1,
        ),
        PackageHighlightNested(
            text="3 nights in handpicked luxury hotels in Chhatrapati Sambhajinagar (MAPAI)",
            sort_order=2,
        ),
        PackageHighlightNested(
            text="Private certified archeological guides for Ajanta and Ellora Caves",
            sort_order=3,
        ),
        PackageHighlightNested(
            text="Pre-booked VIP monument entry tickets at major heritage sites",
            sort_order=4,
        ),
        PackageHighlightNested(
            text="TRAGUIN signature welcome amenities and 24/7 dedicated concierge support",
            sort_order=5,
        ),
        PackageHighlightNested(
            text="Tour code TRAGUIN-MHA-AJ-EL-003 | Serial MH-003",
            sort_order=6,
        ),
    ],
    moods=["Luxury", "Heritage", "Family"],
)

ITINERARY = ItineraryCreate(
    slug=ITINERARY_SLUG,
    destination_id="00000000-0000-0000-0000-000000000000",  # replaced at runtime
    title="Premium Ajanta Ellora Heritage Tour",
    duration_label="03 Nights / 04 Days",
    duration_days=4,
    starting_price=0,
    price_note="On Request (Premium Customised)",
    rating=Decimal("4.9"),
    review_count=0,
    tagline="The Absolute Finest Heritage Discovery & Luxury Holiday",
    overview=(
        "Welcome to an unforgettable odyssey into antiquity, meticulously crafted by TRAGUIN. "
        "This exclusive luxury Ajanta Ellora tour package unfolds the majestic legacy of ancient "
        "India across the rocky heart of Maharashtra. Journey through two millennia of breathtaking "
        "landscapes, world-renowned rock-cut architecture, and fine spiritual art across "
        "Chhatrapati Sambhajinagar (Aurangabad), Ajanta, and Ellora. "
        "Melding private premium chauffeured comfort, signature handpicked hotels, and world-class "
        "archeological guidance, this premium experience transforms deep cultural exploration into "
        "timeless family memories. "
        "Ideal for heritage connoisseurs, families, and historians. Best season: October to March. "
        "Note: Ajanta Caves are closed on Mondays; Ellora Caves are closed on Tuesdays "
        "(itineraries adjusted by travel dates)."
    ),
    seo_title="MH-003 | Premium Ajanta Ellora Heritage Tour | TRAGUIN Maharashtra",
    seo_description=(
        "Luxury 03 Nights / 04 Days Ajanta Ellora heritage package (MH-003) with private SUV, "
        "handpicked Aurangabad hotels, UNESCO cave excursions, Daulatabad Fort, and Bibi Ka Maqbara. "
        "Ideal for families, historians, and heritage travelers."
    ),
    is_featured=True,
    featured_sort_order=3,
    is_published=True,
    highlights=[
        ItineraryHighlightNested(text="Ajanta Caves UNESCO Frescoes", sort_order=1),
        ItineraryHighlightNested(text="Ellora Kailash Temple Monolith", sort_order=2),
        ItineraryHighlightNested(text="Daulatabad Fort", sort_order=3),
        ItineraryHighlightNested(text="Bibi Ka Maqbara", sort_order=4),
        ItineraryHighlightNested(text="Aurangabad Caves", sort_order=5),
    ],
    days=[
        ItineraryDayNested(
            day_number=1,
            title="Arrival in Chhatrapati Sambhajinagar | Gateway to Deccan Grandeur",
            description=(
                "Arrive at Chhatrapati Sambhajinagar Airport or Railway Station, where a premium "
                "TRAGUIN representative extends a traditional royal welcome. Board your private "
                "chauffeured premium SUV and transfer to your handpicked luxury hotel. In the "
                "afternoon, embark on an immersive city sightseeing tour. Witness Panchakki, an "
                "ancient medieval water mill, and marvel at Bibi Ka Maqbara with its intricate "
                "marble screens and manicured Mughal gardens. Enjoy an intimate walk through the "
                "city's historic textile quarters before a curated multi-course dinner."
            ),
            activities=[
                "Sightseeing Included: Bibi Ka Maqbara, Panchakki, Himroo Weaving Center",
                "Optional Activities: Traditional Deccani high-tea at a heritage courtyard",
                "Evening Experience: Private guided walk through the ancient gates of the city",
                "Overnight Stay: Chhatrapati Sambhajinagar Luxury Hotel",
                "Meals Included: Gourmet Welcome Dinner",
            ],
            sort_order=1,
        ),
        ItineraryDayNested(
            day_number=2,
            title="The Miracles of Ajanta | Exploring Ancient Frescoes & Hidden Ravines",
            description=(
                "Indulge in a lavish breakfast before a scenic excursion to the UNESCO World "
                "Heritage Ajanta Caves, approximately 100 km away. Encircled by forested cliffs, "
                "these 30 rock-cut caves served as monsoon retreats for ancient Buddhist monks. "
                "With a handpicked TRAGUIN archeological storyteller, marvel at masterpieces in "
                "Caves 1, 2, 16, and 17, including Padmapani and Vajrapani, and the Jataka tales "
                "painted with natural minerals. Return to the hotel for a relaxing evening at the "
                "premium resort spa."
            ),
            activities=[
                "Sightseeing Included: Ajanta Cave Complex, Waghur Viewpoint, Archeological Museum",
                "Optional Activities: Panoramic photography trek to the Ajanta horseshoe viewpoint",
                "Evening Experience: Private screening of a documentary on the discovery of Ajanta",
                "Overnight Stay: Chhatrapati Sambhajinagar Luxury Hotel",
                "Meals Included: Breakfast & Gourmet Dinner",
            ],
            sort_order=2,
        ),
        ItineraryDayNested(
            day_number=3,
            title="Monoliths of Ellora & Daulatabad Fort | Architectural Triumphs",
            description=(
                "Following a premium breakfast, journey to the Ellora Caves, focusing first on "
                "Cave 16—the magnificent Kailash Temple carved top-down from a single hill, removing "
                "over 200,000 tons of rock. Explore serene Buddhist viharas and the Jain Indra Sabha "
                "temples. Visit the invincible Daulatabad Fort with its moats, subterranean mazes, "
                "and victory minaret. Conclude at the historic Grishneshwar Jyotirlinga Temple."
            ),
            activities=[
                "Sightseeing Included: Ellora Caves, Kailash Monolith, Daulatabad Fort, Grishneshwar",
                "Optional Activities: Private culinary workshop featuring authentic Naan Qalia dishes",
                "Evening Experience: Sundowner drinks overlooking the majestic plains of Daulatabad",
                "Overnight Stay: Chhatrapati Sambhajinagar Luxury Hotel",
                "Meals Included: Breakfast & Gourmet Dinner",
            ],
            sort_order=3,
        ),
        ItineraryDayNested(
            day_number=4,
            title="Aurangabad Caves & Departure | Preserving Timeless Heritage Memories",
            description=(
                "Savor your final morning breakfast before checkout. Explore the Aurangabad Caves, "
                "twelve rock-cut Buddhist shrines from the 6th and 7th centuries AD with exquisite "
                "sculptures of female deities. Enjoy boutique shopping for authentic regional "
                "handicrafts before your private chauffeur drops you at the airport or railway "
                "station for your homeward journey."
            ),
            activities=[
                "Sightseeing Included: Aurangabad Caves, Local Artisan Markets",
                "Optional Activities: Farewell lunch at an elite city garden restaurant",
                "Evening Experience: Drop-off assistance directly at the departure terminal",
                "Overnight Stay: Departure / End of Services",
                "Meals Included: Rich Buffet Breakfast",
            ],
            sort_order=4,
        ),
    ],
    hotels=[
        ItineraryHotelNested(
            name="Welcomhotel by ITC Hotels, Rama International",
            location="Chhatrapati Sambhajinagar / Aurangabad",
            nights_label="03 Nights",
            description="Deluxe tier handpicked luxury hotel in the heritage capital.",
            stars=4,
            category_label="Deluxe",
            room_type="Executive Room",
            meal_plan="MAPAI (Breakfast & Dinner)",
            sort_order=1,
        ),
        ItineraryHotelNested(
            name="Ambassador Ajanta Hotel",
            location="Chhatrapati Sambhajinagar / Aurangabad",
            nights_label="03 Nights",
            description="Premium tier property with refined Deccan hospitality.",
            stars=4,
            category_label="Premium",
            room_type="Club Room / Executive Suite",
            meal_plan="MAPAI (Breakfast & Dinner)",
            sort_order=2,
        ),
        ItineraryHotelNested(
            name="Vivanta Aurangabad - Taj Hotels",
            location="Chhatrapati Sambhajinagar / Aurangabad",
            nights_label="03 Nights",
            description="Luxury tier Taj hospitality with tranquil garden wings.",
            stars=5,
            category_label="Luxury",
            room_type="Superior Room / Deluxe Garden View Wing",
            meal_plan="MAPAI (Breakfast & Dinner)",
            sort_order=3,
        ),
        ItineraryHotelNested(
            name="Vivanta Aurangabad - Taj Hotels",
            location="Chhatrapati Sambhajinagar / Aurangabad",
            nights_label="03 Nights",
            description="Ultra-luxury heritage suite with private butler concierge.",
            stars=5,
            category_label="Ultra Luxury",
            room_type="Luxury Executive Heritage Suite with Private Butler Concierge",
            meal_plan="MAPAI (Breakfast & Dinner)",
            sort_order=4,
        ),
    ],
    inclusions=[
        ItineraryInclusionNested(
            kind="included",
            text="3 nights in handpicked premium hotels or luxury heritage resorts as selected",
            sort_order=1,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Lavish breakfast spreads and multi-course dinners featuring local and global cuisines (MAPAI)",
            sort_order=2,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Private air-conditioned luxury SUV for all transfers, excursions, and intercity sightseeing",
            sort_order=3,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="TRAGUIN welcome touch: traditional garland welcome, cold towels, and premium amenities on arrival",
            sort_order=4,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Private certified archeological guides for comprehensive Ajanta and Ellora cave tours",
            sort_order=5,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Pre-booked VIP entry tickets for all major monuments, bypassing long tourist lines",
            sort_order=6,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Fuel charges, driver allowances, state permits, toll taxes, and parking fees",
            sort_order=7,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="TRAGUIN 24/7 dedicated elite concierge assistance during the entire vacation",
            sort_order=8,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Domestic or international flights, train ticketing, or terminal surcharges",
            sort_order=9,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Personal expenses: laundry, phone bills, premium mini-bar items, and room service",
            sort_order=10,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Camera, video, or commercial shooting licensing charges at tourist places",
            sort_order=11,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Mid-day meals, lunches, snacks, or alcoholic beverages not specified in the plan",
            sort_order=12,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Mandatory high-season holiday surcharges during major festivals or New Year weeks",
            sort_order=13,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Personal travel insurance and medical emergency provisions",
            sort_order=14,
        ),
    ],
)


def get_or_create_maharashtra_destination(db) -> Destination:
    existing = db.scalar(select(Destination).where(Destination.slug == MAHARASHTRA_SLUG))
    if existing is not None:
        return existing

    destination = Destination(
        slug=MAHARASHTRA_SLUG,
        name="Maharashtra",
        country="India",
        region="domestic",
        india_region="west",
        description=(
            "Chhatrapati Sambhajinagar (Aurangabad), the UNESCO Ajanta and Ellora cave complexes, "
            "Deccan forts, and Maharashtra's rich heritage and culinary traditions."
        ),
        starting_price=0,
        moods=["cultural", "luxury", "family"],
        is_published=True,
    )
    db.add(destination)
    db.flush()
    print(f"Created destination: {destination.slug} ({destination.id})")
    return destination


def main() -> None:
    with SessionLocal() as db:
        destination = get_or_create_maharashtra_destination(db)
        dest_id = destination.id

        package_data = PACKAGE.model_copy(update={"destination_id": dest_id})
        itinerary_data = ITINERARY.model_copy(update={"destination_id": dest_id})

        existing_pkg = db.scalar(select(Package).where(Package.slug == PACKAGE_SLUG))
        moods = travel_moods_for_package(package_data.slug, package_data.moods)
        if existing_pkg:
            print(f"Package already exists: {PACKAGE_SLUG} ({existing_pkg.id})")
            package = existing_pkg
            current_moods = [m.mood for m in package.moods]
            if current_moods != moods:
                sync_package_moods(db, package, moods)
                print(f"  Updated moods: {current_moods} -> {moods}")
        else:
            pkg_data = package_data.model_dump()
            highlights = pkg_data.pop("highlights")
            pkg_data.pop("moods", None)
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
            sync_itinerary_nested_content(db, itinerary, itinerary_data)
            print(
                f"  Synced nested content: days={len(itinerary_data.days)} "
                f"hotels={len(itinerary_data.hotels)} inclusions={len(itinerary_data.inclusions)}"
            )
        else:
            itin_data = itinerary_data.model_dump()
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
        itinerary = itinerary_query_with_nested(db).filter_by(id=itinerary.id).one()
        package = package_query_with_nested(db).filter_by(id=package.id).one()
        print(f"Linked package {package.slug} -> itinerary {itinerary.slug}")
        print(
            f"Days: {len(itinerary.days)} | Hotels: {len(itinerary.hotels)} | "
            f"Inclusions: {len(itinerary.inclusions)} | Hero image: none"
        )


if __name__ == "__main__":
    main()
