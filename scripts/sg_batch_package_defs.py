"""Builder functions for SG-001 through SG-004 Singapore packages (no images)."""

from __future__ import annotations

from decimal import Decimal
from uuid import UUID

from schemas.itineraries import (
    ItineraryCreate,
    ItineraryDayNested,
    ItineraryHighlightNested,
    ItineraryHotelNested,
    ItineraryInclusionNested,
)
from schemas.packages import PackageCreate, PackageHighlightNested


def _day(
    day_number: int,
    title: str,
    description: str,
    activities: list[str],
    sort_order: int | None = None,
) -> ItineraryDayNested:
    return ItineraryDayNested(
        day_number=day_number,
        title=title,
        description=description,
        activities=activities,
        sort_order=sort_order if sort_order is not None else day_number,
    )


def build_sg_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="sg-001-singapore-highlights-family-tour",
        destination_id=destination_id,
        title="Singapore Highlights Family Tour",
        duration_label="03 Nights / 04 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=57,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Singapore (3N) classic family discovery", sort_order=1),
            PackageHighlightNested(text="Marina Bay light show & Gardens by the Bay", sort_order=2),
            PackageHighlightNested(text="Night Safari exclusive evening experience", sort_order=3),
            PackageHighlightNested(text="Sentosa Island & Universal Studios fun", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-SIN-HIG-2026 | Serial SG-001", sort_order=6),
        ],
        moods=["Family", "Luxury", "Cultural", "Wildlife", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="sg-001-singapore-highlights-itinerary",
        destination_id=destination_id,
        title="Singapore Highlights Family Tour",
        duration_label="03 Nights / 04 Days",
        duration_days=4,
        starting_price=0,
        price_note="On Request (Premium Singapore Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Marina Bay Sands • Gardens by the Bay • Sentosa • Night Safari",
        overview=(
            "Dive into the vibrant, futuristic city-state of Singapore with TRAGUIN's curated family holiday. "
            "A flawless balance of high-energy exploration and iconic sightseeing — Marina Bay, Gardens by the Bay, "
            "Night Safari, and Sentosa Island — creating unforgettable memories in Southeast Asia's most spectacular destination."
        ),
        seo_title="SG-001 | Singapore Highlights Family Tour | TRAGUIN",
        seo_description=(
            "Premium 03 Nights / 04 Days Singapore family package (SG-001): Marina Bay, Gardens by the Bay, "
            "Night Safari, and Sentosa Island."
        ),
        is_featured=True,
        featured_sort_order=57,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Marina Bay Light & Water Show", sort_order=1),
            ItineraryHighlightNested(text="Gardens by the Bay Cloud Forest", sort_order=2),
            ItineraryHighlightNested(text="Night Safari Exclusive Experience", sort_order=3),
            ItineraryHighlightNested(text="Sentosa Island Family Fun", sort_order=4),
        ],
        days=[
            _day(1, "Arrival in Singapore & Marina Bay", "Arrive in Singapore. Private transfer to handpicked premium hotel. Evening exploring Marina Bay with spectacular light and water show.", ["Sightseeing Included: VIP airport reception, Marina Bay evening exploration", "Overnight Stay: Singapore (Premium Family Hotel)", "Meals Included: Welcome arrangements on arrival"]),
            _day(2, "Gardens by the Bay & Night Safari", "Full day at futuristic Gardens by the Bay including Cloud Forest. Evening exclusive Night Safari experience.", ["Sightseeing Included: Gardens by the Bay, Cloud Forest, Night Safari", "Overnight Stay: Singapore (Premium Family Hotel)", "Meals Included: Breakfast"]),
            _day(3, "Sentosa Island Fun", "Full day of excitement at Sentosa Island. Universal Studios Singapore or vibrant sandy beaches — perfect for family fun.", ["Sightseeing Included: Sentosa Island, Universal Studios or beach leisure", "Overnight Stay: Singapore (Premium Family Hotel)", "Meals Included: Breakfast"]),
            _day(4, "Departure", "Final breakfast before TRAGUIN private transfer to the airport, completing your premium Singapore experience.", ["Sightseeing Included: Private airport transfer", "Meals Included: Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Marina Bay Sands / Shangri-La Singapore", location="Singapore", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=1),
        ],
        inclusions=_sg001_inclusions(),
    )
    return package, itinerary


def _sg001_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="03 Nights in handpicked premium family hotel in Singapore", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private luxury ground transfers throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Marina Bay, Gardens by the Bay, Night Safari, and Sentosa sightseeing", sort_order=3),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated on-ground family concierge support", sort_order=4),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Singapore entry visa processing fees", sort_order=5),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=8),
    ]


def build_sg_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="sg-002-singapore-sentosa-family-tour",
        destination_id=destination_id,
        title="Singapore & Sentosa Family Tour",
        duration_label="04 Nights / 05 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=58,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Singapore City (2N) → Sentosa Island (2N) family expedition", sort_order=1),
            PackageHighlightNested(text="Marina Bay glamour & Gardens by the Bay", sort_order=2),
            PackageHighlightNested(text="Ultra-luxury Sentosa resort with sunset beaches", sort_order=3),
            PackageHighlightNested(text="Universal Studios & Adventure Cove Waterpark", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-SIN-SEN-2026 | Serial SG-002", sort_order=6),
        ],
        moods=["Family", "Luxury", "Beach", "Adventure"],
    )
    itinerary = ItineraryCreate(
        slug="sg-002-singapore-sentosa-itinerary",
        destination_id=destination_id,
        title="Singapore & Sentosa Family Tour",
        duration_label="04 Nights / 05 Days",
        duration_days=5,
        starting_price=0,
        price_note="On Request (Premium Singapore Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Marina Bay • Gardens by the Bay • Sentosa • Universal Studios • Adventure Cove",
        overview=(
            "Discover the vibrant heart of Singapore and the island excitement of Sentosa with TRAGUIN's curated "
            "family holiday. Perfect balance of high-energy city exploration and luxury resort leisure — from Marina Bay "
            "and Gardens by the Bay to Universal Studios and Adventure Cove."
        ),
        seo_title="SG-002 | Singapore & Sentosa Family Tour | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Singapore family package (SG-002): Marina Bay, Gardens by the Bay, "
            "Sentosa resort, Universal Studios, and Adventure Cove."
        ),
        is_featured=True,
        featured_sort_order=58,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Marina Bay Iconic Light Show", sort_order=1),
            ItineraryHighlightNested(text="Gardens by the Bay Cloud Forest & Flower Dome", sort_order=2),
            ItineraryHighlightNested(text="Sentosa Ultra-Luxury Resort Stay", sort_order=3),
            ItineraryHighlightNested(text="Universal Studios & Adventure Cove", sort_order=4),
        ],
        days=[
            _day(1, "Arrival & Marina Bay Glamour", "Arrive in Singapore. Private transfer to premium city hotel. Evening at Marina Bay experiencing the iconic light show.", ["Sightseeing Included: VIP airport reception, Marina Bay light show", "Overnight Stay: Singapore City (Premium Hotel)", "Meals Included: Welcome arrangements on arrival"]),
            _day(2, "Gardens by the Bay Exploration", "Explore futuristic Gardens by the Bay including Cloud Forest and Flower Dome — iconic modern Singapore sightseeing.", ["Sightseeing Included: Gardens by the Bay, Cloud Forest, Flower Dome", "Overnight Stay: Singapore City (Premium Hotel)", "Meals Included: Breakfast"]),
            _day(3, "Sentosa Island Resort Transit", "Transfer to Sentosa Island. Check into ultra-luxury family resort. Leisure time, vibrant sandy beaches, and stunning sunset views.", ["Sightseeing Included: Transfer to Sentosa Island resort", "Overnight Stay: Sentosa Island (Ultra-Luxury Family Resort)", "Meals Included: Breakfast"]),
            _day(4, "Universal Studios & Adventure Cove", "Full day at Universal Studios Singapore and Adventure Cove Waterpark — perfect for family fun and unforgettable memories.", ["Sightseeing Included: Universal Studios Singapore, Adventure Cove Waterpark", "Overnight Stay: Sentosa Island (Ultra-Luxury Family Resort)", "Meals Included: Breakfast"]),
            _day(5, "Departure", "Final breakfast before TRAGUIN private transfer to the airport, completing your premium Singapore-Sentosa family experience.", ["Sightseeing Included: Private airport transfer", "Meals Included: Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Marina Bay Sands", location="Singapore City", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Shangri-La Rasa Sentosa", location="Sentosa Island", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=2),
        ],
        inclusions=_sg002_inclusions(),
    )
    return package, itinerary


def _sg002_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="04 Nights in premium family hotels across Singapore City and Sentosa", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private luxury ground transfers throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Marina Bay, Gardens by the Bay, Universal Studios, and Adventure Cove", sort_order=3),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated on-ground family concierge support", sort_order=4),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Singapore entry visa processing fees", sort_order=5),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=8),
    ]


def build_sg_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="sg-003-singapore-universal-studios-special",
        destination_id=destination_id,
        title="Singapore Universal Studios Special",
        duration_label="04 Nights / 05 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=59,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Singapore & Sentosa (4N) ultimate theme park expedition", sort_order=1),
            PackageHighlightNested(text="Universal Studios with priority express passes", sort_order=2),
            PackageHighlightNested(text="S.E.A. Aquarium & Adventure Cove Waterpark", sort_order=3),
            PackageHighlightNested(text="Sentosa leisure & grand farewell dinner", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-SIN-USS-2026 | Serial SG-003", sort_order=6),
        ],
        moods=["Family", "Luxury", "Adventure", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="sg-003-singapore-universal-studios-itinerary",
        destination_id=destination_id,
        title="Singapore Universal Studios Special",
        duration_label="04 Nights / 05 Days",
        duration_days=5,
        starting_price=0,
        price_note="On Request (Premium Theme Park Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Universal Studios • Adventure Cove • S.E.A. Aquarium • Marina Bay",
        overview=(
            "Dive into the thrilling world of entertainment with TRAGUIN's Universal Studios Special family tour. "
            "Focused on non-stop excitement and premium theme park access — Universal Studios express passes, "
            "S.E.A. Aquarium, Adventure Cove, and Sentosa leisure."
        ),
        seo_title="SG-003 | Singapore Universal Studios Special | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Singapore theme park package (SG-003): Universal Studios express passes, "
            "S.E.A. Aquarium, Adventure Cove, and Marina Bay."
        ),
        is_featured=True,
        featured_sort_order=59,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Marina Bay Water Light Show", sort_order=1),
            ItineraryHighlightNested(text="Universal Studios Express Passes", sort_order=2),
            ItineraryHighlightNested(text="S.E.A. Aquarium Marine Life", sort_order=3),
            ItineraryHighlightNested(text="Adventure Cove Waterpark", sort_order=4),
        ],
        days=[
            _day(1, "Arrival in Singapore & City Vistas", "Arrive in Singapore. Private transfer to premium family hotel. Evening exploring breathtaking Marina Bay with spectacular water light show.", ["Sightseeing Included: VIP airport reception, Marina Bay water light show", "Overnight Stay: Singapore & Sentosa (Premium Family Hotel)", "Meals Included: Welcome arrangements on arrival"]),
            _day(2, "Universal Studios Full-Day Immersion", "Full day at Universal Studios Singapore with pre-arranged priority express passes on all top movie-themed thrill rides.", ["Sightseeing Included: Universal Studios Singapore full-day admission, express passes", "Overnight Stay: Singapore & Sentosa (Premium Family Hotel)", "Meals Included: Breakfast"]),
            _day(3, "Adventure Cove & S.E.A. Aquarium", "Visit massive S.E.A. Aquarium to witness spectacular marine life. Afternoon at Adventure Cove Waterpark.", ["Sightseeing Included: S.E.A. Aquarium, Adventure Cove Waterpark", "Overnight Stay: Singapore & Sentosa (Premium Family Hotel)", "Meals Included: Breakfast"]),
            _day(4, "Sentosa Island Leisure & Fun", "Day of leisure on Sentosa Island with family-friendly attractions, beach time, and grand farewell dinner.", ["Sightseeing Included: Sentosa Island leisure and attractions", "Evening Experience: Grand farewell dinner", "Overnight Stay: Singapore & Sentosa (Premium Family Hotel)", "Meals Included: Breakfast & Farewell Dinner"]),
            _day(5, "Departure", "Final breakfast before TRAGUIN private transfer to the airport, completing your premium theme-park experience.", ["Sightseeing Included: Private airport transfer", "Meals Included: Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Resorts World Sentosa / Family Luxury Hotel", location="Singapore & Sentosa", nights_label="04 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=1),
        ],
        inclusions=_sg003_inclusions(),
    )
    return package, itinerary


def _sg003_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="04 Nights in premium family hotel at Resorts World Sentosa or similar", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private luxury ground transfers throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Universal Studios Singapore with priority express passes", sort_order=3),
        ItineraryInclusionNested(kind="included", text="S.E.A. Aquarium and Adventure Cove Waterpark admission", sort_order=4),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated on-ground family concierge support", sort_order=5),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Singapore entry visa processing fees", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=9),
    ]


def build_sg_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="sg-004-singapore-melbourne-family-tour",
        destination_id=destination_id,
        title="Singapore & Melbourne Family Tour",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=60,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Singapore (3N) → Melbourne (4N) multi-country family expedition", sort_order=1),
            PackageHighlightNested(text="Marina Bay, Gardens by the Bay & Sentosa leisure", sort_order=2),
            PackageHighlightNested(text="Melbourne laneways street-art walking tour", sort_order=3),
            PackageHighlightNested(text="Great Ocean Road Twelve Apostles & Phillip Island penguins", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-SIN-MEL-2026 | Serial SG-004", sort_order=6),
        ],
        moods=["Family", "Luxury", "Cultural", "Nature", "Wildlife", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="sg-004-singapore-melbourne-itinerary",
        destination_id=destination_id,
        title="Singapore & Melbourne Family Tour",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="On Request (Premium Multi-Country Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Singapore • Marina Bay • Melbourne • Great Ocean Road • Phillip Island",
        overview=(
            "A magnificent multi-country family expedition connecting Singapore's futuristic metropolitan marvels "
            "with Melbourne's artistic culture and wild coastlines. Gardens by the Bay, Sentosa, Melbourne laneways, "
            "Great Ocean Road, and Phillip Island Penguin Parade — a harmonious blend of adventure and discovery."
        ),
        seo_title="SG-004 | Singapore & Melbourne Family Tour | TRAGUIN",
        seo_description=(
            "Premium 07 Nights / 08 Days Singapore & Australia family package (SG-004): Marina Bay, "
            "Gardens by the Bay, Melbourne laneways, Great Ocean Road, and Phillip Island."
        ),
        is_featured=True,
        featured_sort_order=60,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Marina Bay & Gardens by the Bay", sort_order=1),
            ItineraryHighlightNested(text="Sentosa Island Family Leisure", sort_order=2),
            ItineraryHighlightNested(text="Melbourne Street-Art Laneways", sort_order=3),
            ItineraryHighlightNested(text="Great Ocean Road Twelve Apostles", sort_order=4),
            ItineraryHighlightNested(text="Phillip Island Penguin Parade", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Singapore & Marina Bay", "Arrive in Singapore. Private transfer to premium hotel. Evening exploring breathtaking Marina Bay with spectacular light shows.", ["Sightseeing Included: VIP airport reception, Marina Bay evening exploration", "Overnight Stay: Singapore (Premium Family Hotel)", "Meals Included: Welcome arrangements on arrival"]),
            _day(2, "Gardens by the Bay Exploration", "Full day at Gardens by the Bay discovering Cloud Forest and Flower Dome — a top-tier Singapore family experience.", ["Sightseeing Included: Gardens by the Bay, Cloud Forest, Flower Dome", "Overnight Stay: Singapore (Premium Family Hotel)", "Meals Included: Breakfast"]),
            _day(3, "Singapore Family Leisure", "Relaxing day with family-friendly Sentosa Island beaches and attractions.", ["Sightseeing Included: Sentosa Island beaches and attractions", "Overnight Stay: Singapore (Premium Family Hotel)", "Meals Included: Breakfast"]),
            _day(4, "Flight to Melbourne", "Private transfer to airport for flight to Melbourne. Check into city-centre luxury family hotel.", ["Sightseeing Included: Private airport transfer, domestic/international flight coordination to Melbourne", "Overnight Stay: Melbourne (Premium Family Hotel)", "Meals Included: Breakfast"]),
            _day(5, "Melbourne Lanes & Arts", "Private guided walking tour through Melbourne's world-famous street-art laneways and vibrant culture centres.", ["Sightseeing Included: Melbourne laneways street-art guided walking tour", "Overnight Stay: Melbourne (Premium Family Hotel)", "Meals Included: Breakfast"]),
            _day(6, "Great Ocean Road Expedition", "Exhilarating full-day adventure along the Great Ocean Road witnessing dramatic Twelve Apostles landscapes.", ["Sightseeing Included: Great Ocean Road day trip, Twelve Apostles viewpoint", "Overnight Stay: Melbourne (Premium Family Hotel)", "Meals Included: Breakfast & Picnic Lunch"]),
            _day(7, "Phillip Island Wildlife Gala", "Journey to Phillip Island to watch native wildlife and the famous Penguin Parade — a highlight for the entire family.", ["Sightseeing Included: Phillip Island Penguin Parade tickets, wildlife viewing", "Overnight Stay: Melbourne (Premium Family Hotel)", "Meals Included: Breakfast & Dinner"]),
            _day(8, "Departure", "Final luxury breakfast before TRAGUIN private transfer to Melbourne airport, completing your premium multi-country family expedition.", ["Sightseeing Included: Private airport transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Marina Bay Sands / Shangri-La Singapore", location="Singapore", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="The Langham Melbourne / Crown Towers", location="Melbourne", nights_label="04 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=2),
        ],
        inclusions=_sg004_inclusions(),
    )
    return package, itinerary


def _sg004_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="07 Nights in premium family hotels across Singapore and Melbourne", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private luxury ground transfers throughout both destinations", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Flight coordination from Singapore to Melbourne", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Marina Bay, Gardens by the Bay, Great Ocean Road, and Phillip Island sightseeing", sort_order=4),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated on-ground family concierge support", sort_order=5),
        ItineraryInclusionNested(kind="excluded", text="International airfare and visa processing fees for Singapore and Australia", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=9),
    ]


SG_BUILDERS = [
    build_sg_001,
    build_sg_002,
    build_sg_003,
    build_sg_004,
]
