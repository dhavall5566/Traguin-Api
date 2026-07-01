"""Builder functions for MY-001 through MY-003 Malaysia packages (no images)."""

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


def build_my_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="my-001-kuala-lumpur-genting-family-tour",
        destination_id=destination_id,
        title="Kuala Lumpur Genting Family Tour",
        duration_label="04 Nights / 05 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=54,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Kuala Lumpur (2N) → Genting Highlands (2N) family circuit", sort_order=1),
            PackageHighlightNested(text="Petronas Twin Towers & Batu Caves cultural expedition", sort_order=2),
            PackageHighlightNested(text="Awana SkyWay cable car & Genting theme parks", sort_order=3),
            PackageHighlightNested(text="Full-day theme park adventure & mountain farewell dinner", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-KUL-GEN-FAM-2026 | Serial MY-001", sort_order=6),
        ],
        moods=["Family", "Luxury", "Cultural", "Adventure"],
    )
    itinerary = ItineraryCreate(
        slug="my-001-kuala-lumpur-genting-itinerary",
        destination_id=destination_id,
        title="Kuala Lumpur Genting Family Tour",
        duration_label="04 Nights / 05 Days",
        duration_days=5,
        starting_price=0,
        price_note="On Request (Premium Malaysia Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Kuala Lumpur • Petronas Towers • Genting Highlands • Theme Parks",
        overview=(
            "An exhilarating family escapade bridging Kuala Lumpur's city sophistication with Genting Highlands' "
            "mountain-top thrills. From iconic Petronas Towers and Batu Caves to world-class theme parks and "
            "cable car vistas — a premier luxury Malaysia holiday crafted by TRAGUIN."
        ),
        seo_title="MY-001 | Kuala Lumpur Genting Family Tour | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Malaysia family package (MY-001): Petronas Towers, Batu Caves, "
            "Genting Highlands cable car, and theme parks."
        ),
        is_featured=True,
        featured_sort_order=54,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Petronas Twin Towers Observation Deck", sort_order=1),
            ItineraryHighlightNested(text="Batu Caves & Merdeka Square", sort_order=2),
            ItineraryHighlightNested(text="Awana SkyWay Cable Car to Genting", sort_order=3),
            ItineraryHighlightNested(text="Genting Theme Park Full-Day Adventure", sort_order=4),
        ],
        days=[
            _day(1, "Arrival in Kuala Lumpur & City Lights", "Arrive at KL International Airport with TRAGUIN welcome. Private luxury van to premium hotel. Evening visit to Petronas Twin Towers for breathtaking city skyline views.", ["Sightseeing Included: Petronas Twin Towers observation deck, KL city skyline drive", "Overnight Stay: Kuala Lumpur (Premium City Hotel)", "Meals Included: Welcome Family Dinner"]),
            _day(2, "Kuala Lumpur Cultural Expedition", "Explore majestic Batu Caves with towering golden statue. Visit historic Merdeka Square and enjoy curated city shopping and cultural landmarks.", ["Sightseeing Included: Batu Caves, Merdeka Square, local handicraft market", "Overnight Stay: Kuala Lumpur (Premium City Hotel)", "Meals Included: Breakfast & Local Lunch"]),
            _day(3, "Genting Highlands Escape", "Scenic cable car ride via Awana SkyWay to Genting Highlands. Afternoon exploring indoor and outdoor theme parks.", ["Sightseeing Included: Awana SkyWay cable car, Genting Theme Park entry", "Overnight Stay: Genting Highlands (Handpicked Resort)", "Meals Included: Breakfast & Buffet Dinner"]),
            _day(4, "The Ultimate Theme Park Day", "Full day at Genting's integrated entertainment hubs with world-class rides. Grand finale dinner overlooking mountain valleys.", ["Sightseeing Included: Full day theme park exploration", "Evening Experience: Farewell family dinner overlooking mountain valleys", "Overnight Stay: Genting Highlands (Handpicked Resort)", "Meals Included: Breakfast & Farewell Family Dinner"]),
            _day(5, "Departure", "Final morning breakfast before luxury transfer to KL International Airport. Premium Malaysia family tour concludes with unforgettable TRAGUIN memories.", ["Sightseeing Included: Last-minute souvenir shopping at KL Airport Duty Free", "Meals Included: Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Impiana KLCC / similar", location="Kuala Lumpur", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="First World Hotel / similar", location="Genting Highlands", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=3, sort_order=2),
            ItineraryHotelNested(name="Berjaya Times Square", location="Kuala Lumpur", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=4, sort_order=3),
            ItineraryHotelNested(name="Resorts World Genting", location="Genting Highlands", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=4, sort_order=4),
            ItineraryHotelNested(name="Shangri-La Kuala Lumpur", location="Kuala Lumpur", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="Crockfords", location="Genting Highlands", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="The St. Regis KL", location="Kuala Lumpur", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="Resorts World Genting Suites", location="Genting Highlands", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=8),
        ],
        inclusions=_my001_inclusions(),
    )
    return package, itinerary


def _my001_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="04 Nights in handpicked premium family hotels across Kuala Lumpur and Genting", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private luxury van ground transfers throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Petronas Towers, Batu Caves, and Genting Theme Park sightseeing", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Awana SkyWay cable car ascent to Genting Highlands", sort_order=4),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated on-ground family concierge support", sort_order=5),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Malaysia entry visa processing fees", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=9),
    ]


def build_my_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="my-002-malaysia-discovery-family-tour",
        destination_id=destination_id,
        title="Malaysia Discovery Family Tour",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=55,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Kuala Lumpur (3N) → Genting Highlands (2N) discovery circuit", sort_order=1),
            PackageHighlightNested(text="KL Tower, Petronas Towers & Batu Caves exploration", sort_order=2),
            PackageHighlightNested(text="Genting SkyWorlds theme park & highland leisure", sort_order=3),
            PackageHighlightNested(text="Putrajaya administrative capital & farewell in KL", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-MAL-DIS-2026 | Serial MY-002", sort_order=6),
        ],
        moods=["Family", "Luxury", "Cultural", "Adventure", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="my-002-malaysia-discovery-itinerary",
        destination_id=destination_id,
        title="Malaysia Discovery Family Tour",
        duration_label="05 Nights / 06 Days",
        duration_days=6,
        starting_price=0,
        price_note="On Request (Premium Malaysia Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Kuala Lumpur • Batu Caves • Genting Highlands • Putrajaya",
        overview=(
            "Discover the rich heritage and modern wonders of Malaysia with TRAGUIN's curated family itinerary. "
            "A flawless blend of city exploration and highland adventure — from KL Tower and Petronas Towers "
            "to Genting theme parks and Putrajaya's stunning architecture."
        ),
        seo_title="MY-002 | Malaysia Discovery Family Tour | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days Malaysia family package (MY-002): Kuala Lumpur, Batu Caves, "
            "Genting Highlands, Putrajaya, and SkyWorlds theme park."
        ),
        is_featured=True,
        featured_sort_order=55,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="KL Tower & Petronas Twin Towers", sort_order=1),
            ItineraryHighlightNested(text="Batu Caves & Merdeka Square", sort_order=2),
            ItineraryHighlightNested(text="Genting SkyWorlds Theme Park", sort_order=3),
            ItineraryHighlightNested(text="Putrajaya Mosque & Architecture", sort_order=4),
        ],
        days=[
            _day(1, "Arrival in Kuala Lumpur", "Arrive in Kuala Lumpur. Private TRAGUIN transfer to premium hotel. Evening breathtaking city skyline views from KL Tower observation deck.", ["Sightseeing Included: KL Tower observation deck, city orientation", "Overnight Stay: Kuala Lumpur (Premium Hotel)", "Meals Included: Welcome arrangements on arrival"]),
            _day(2, "Kuala Lumpur Exploration", "Visit world-famous Petronas Twin Towers and iconic Batu Caves. Shopping and local food in vibrant city center with insights into Malaysia's cultural diversity.", ["Sightseeing Included: Petronas Towers, Batu Caves, Merdeka Square", "Overnight Stay: Kuala Lumpur (Premium Hotel)", "Meals Included: Breakfast"]),
            _day(3, "Genting Highlands Adventure", "Scenic Awana SkyWay cable car ride with breathtaking landscapes. Time in integrated indoor and outdoor theme parks.", ["Sightseeing Included: Awana SkyWay, indoor/outdoor theme parks", "Overnight Stay: Genting Highlands (Handpicked Hotel)", "Meals Included: Breakfast"]),
            _day(4, "Genting Highlands Leisure", "Full day dedicated to leisure and adventure at Genting SkyWorlds Theme Park. Shopping malls, cinemas, and cool mountain weather.", ["Sightseeing Included: Genting SkyWorlds Theme Park", "Overnight Stay: Genting Highlands (Handpicked Hotel)", "Meals Included: Breakfast"]),
            _day(5, "Putrajaya & Return to KL", "Visit Putrajaya administrative capital with stunning architecture including Putrajaya Mosque. Transfer back to Kuala Lumpur for final evening of shopping and dining.", ["Sightseeing Included: Putrajaya Mosque, Prime Minister's Office view", "Overnight Stay: Kuala Lumpur (Premium Hotel)", "Meals Included: Breakfast"]),
            _day(6, "Departure", "Final breakfast before private TRAGUIN transfer to KL International Airport, completing your Malaysia discovery family tour.", ["Sightseeing Included: Private airport transfer", "Meals Included: Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Impiana KLCC / similar", location="Kuala Lumpur", nights_label="03 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="First World Hotel / similar", location="Genting Highlands", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=3, sort_order=2),
            ItineraryHotelNested(name="Berjaya Times Square", location="Kuala Lumpur", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=4, sort_order=3),
            ItineraryHotelNested(name="Resorts World Genting", location="Genting Highlands", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=4, sort_order=4),
            ItineraryHotelNested(name="Shangri-La Kuala Lumpur", location="Kuala Lumpur", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="Crockfords", location="Genting Highlands", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=6),
        ],
        inclusions=_my002_inclusions(),
    )
    return package, itinerary


def _my002_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="05 Nights in handpicked premium family hotels across Kuala Lumpur and Genting", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private luxury van ground transfers throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Petronas Towers, Batu Caves, Genting theme parks, and Putrajaya sightseeing", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Awana SkyWay cable car and Genting SkyWorlds theme park access", sort_order=4),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated on-ground family concierge support", sort_order=5),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Malaysia entry visa processing fees", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=9),
    ]


def build_my_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="my-003-kuala-lumpur-langkawi-family-tour",
        destination_id=destination_id,
        title="Kuala Lumpur Langkawi Family Tour",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=56,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Kuala Lumpur (2N) → Langkawi (3N) city & island circuit", sort_order=1),
            PackageHighlightNested(text="Petronas Towers, Batu Caves & Merdeka Square", sort_order=2),
            PackageHighlightNested(text="Langkawi SkyBridge via SkyCab cable car", sort_order=3),
            PackageHighlightNested(text="Mangrove & marine family boat expedition", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-KUL-LGK-FAM-2026 | Serial MY-003", sort_order=6),
        ],
        moods=["Family", "Luxury", "Cultural", "Nature", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="my-003-kuala-lumpur-langkawi-itinerary",
        destination_id=destination_id,
        title="Kuala Lumpur Langkawi Family Tour",
        duration_label="05 Nights / 06 Days",
        duration_days=6,
        starting_price=0,
        price_note="On Request (Premium Malaysia Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Kuala Lumpur • Petronas Towers • Langkawi • SkyBridge • Mangroves",
        overview=(
            "The perfect synergy of vibrant city life and tranquil island beauty. From Kuala Lumpur's iconic towers "
            "and Batu Caves to Langkawi's pristine beaches, SkyBridge, and mangrove cruises — a 6-day TRAGUIN "
            "family expedition designed for unforgettable memories."
        ),
        seo_title="MY-003 | Kuala Lumpur Langkawi Family Tour | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days Malaysia family package (MY-003): Kuala Lumpur, Langkawi SkyBridge, "
            "Batu Caves, and mangrove boat expedition."
        ),
        is_featured=True,
        featured_sort_order=56,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Petronas Twin Towers Observation Deck", sort_order=1),
            ItineraryHighlightNested(text="Batu Caves & Merdeka Square", sort_order=2),
            ItineraryHighlightNested(text="Langkawi SkyBridge & SkyCab", sort_order=3),
            ItineraryHighlightNested(text="Mangrove & Marine Boat Expedition", sort_order=4),
        ],
        days=[
            _day(1, "Arrival in Kuala Lumpur", "TRAGUIN private chauffeur meets you at the airport. Seamless transfer to premium hotel. Evening breathtaking city views from Petronas Towers observation deck.", ["Sightseeing Included: Petronas Twin Towers observation deck", "Overnight Stay: Kuala Lumpur (Premium City Hotel)", "Meals Included: Welcome arrangements on arrival"]),
            _day(2, "Kuala Lumpur Exploration", "Visit spiritual Batu Caves with immense scenic beauty. City tour featuring Merdeka Square and local craft markets.", ["Sightseeing Included: Batu Caves, Merdeka Square, local craft markets", "Overnight Stay: Kuala Lumpur (Premium City Hotel)", "Meals Included: Breakfast"]),
            _day(3, "Fly to Langkawi", "Transfer to airport for flight to Langkawi, the jewel of Kedah. Check into premium beach stay and enjoy relaxing sunset walk on the beach.", ["Sightseeing Included: Domestic flight coordination to Langkawi, beach sunset walk", "Overnight Stay: Langkawi (Premium Beach Resort)", "Meals Included: Breakfast"]),
            _day(4, "Langkawi Island Discovery", "Iconic Langkawi SkyBridge accessible via SkyCab cable car. Explore unique geological wonders and breathtaking island landscapes.", ["Sightseeing Included: Langkawi SkyCab, SkyBridge, island geological wonders", "Overnight Stay: Langkawi (Premium Beach Resort)", "Meals Included: Breakfast"]),
            _day(5, "Mangrove & Marine Expedition", "Curated boat adventure exploring Langkawi's mangroves and pristine marine life — perfect for the whole family.", ["Sightseeing Included: Guided mangrove and marine boat expedition", "Overnight Stay: Langkawi (Premium Beach Resort)", "Meals Included: Breakfast"]),
            _day(6, "Departure", "Last-minute shopping before flight home. Conclude your Malaysian adventure with unforgettable TRAGUIN memories.", ["Sightseeing Included: Private airport transfer", "Meals Included: Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Impiana KLCC / similar", location="Kuala Lumpur", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="Adya Hotel / similar", location="Langkawi", nights_label="03 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="Berjaya Times Square", location="Kuala Lumpur", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=4, sort_order=3),
            ItineraryHotelNested(name="Pelangi Beach Resort", location="Langkawi", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=4, sort_order=4),
            ItineraryHotelNested(name="Shangri-La Kuala Lumpur", location="Kuala Lumpur", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="The Westin Langkawi", location="Langkawi", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="The St. Regis KL", location="Kuala Lumpur", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="The Datai Langkawi", location="Langkawi", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=8),
        ],
        inclusions=_my003_inclusions(),
    )
    return package, itinerary


def _my003_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="05 Nights in handpicked premium family hotels across Kuala Lumpur and Langkawi", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private chauffeur-driven luxury ground transfers throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Domestic flight coordination from Kuala Lumpur to Langkawi", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Petronas Towers, Batu Caves, SkyBridge, and mangrove boat expedition", sort_order=4),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated on-ground family concierge support", sort_order=5),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Malaysia entry visa processing fees", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=9),
    ]


MY_BUILDERS = [
    build_my_001,
    build_my_002,
    build_my_003,
]
