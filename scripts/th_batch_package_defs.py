"""Builder functions for TH-001..TH-009, TH-011, TH-012 Thailand packages (no images)."""

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


def _bkk_pat_hotels(bkk_n: str, pat_n: str) -> list[ItineraryHotelNested]:
    return [
        ItineraryHotelNested(name="The Sukosol Bangkok / similar", location="Bangkok", nights_label=bkk_n, category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
        ItineraryHotelNested(name="Novotel Pattaya Resort / similar", location="Pattaya", nights_label=pat_n, category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
        ItineraryHotelNested(name="Grande Centre Point Terminal 21", location="Bangkok", nights_label=bkk_n, category_label="Premium", meal_plan="Breakfast", stars=4, sort_order=3),
        ItineraryHotelNested(name="Amari Pattaya Resort", location="Pattaya", nights_label=pat_n, category_label="Premium", meal_plan="Breakfast", stars=4, sort_order=4),
        ItineraryHotelNested(name="Shangri-La Bangkok", location="Bangkok", nights_label=bkk_n, category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=5),
        ItineraryHotelNested(name="Hilton Pattaya Hotel", location="Pattaya", nights_label=pat_n, category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=6),
        ItineraryHotelNested(name="Mandarin Oriental, Bangkok", location="Bangkok", nights_label=bkk_n, category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
        ItineraryHotelNested(name="Grande Centre Point Space Pattaya", location="Pattaya", nights_label=pat_n, category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=8),
    ]


def _bkk_pat_days() -> list[ItineraryDayNested]:
    return [
        _day(1, "Bangkok Arrival & Sunset Orientation", "VIP fast-track reception at Suvarnabhumi Airport. Private luxury van to premium city hotel. Afternoon city orientation drive and curated welcome dinner.", ["Sightseeing Included: VIP airport fast-track, panoramic city orientation drive", "Evening Experience: Relaxed family welcome dinner", "Overnight Stay: Bangkok (Premium Family-Friendly Luxury Hotel)", "Meals Included: Curated International Welcome Dinner"]),
        _day(2, "Bangkok Heritage & Iconic Temples", "Grand Palace, Wat Phra Kaew, and Wat Pho Reclining Buddha. Afternoon premium retail and riverside dinner.", ["Sightseeing Included: Grand Palace, Wat Phra Kaew, Wat Pho, premium retail center", "Overnight Stay: Bangkok (Premium Family-Friendly Luxury Hotel)", "Meals Included: International Breakfast & Traditional Thai Fine Dining Lunch"]),
        _day(3, "Bangkok to Pattaya Coastal Escape", "Scenic private van along Gulf of Thailand to Pattaya beachfront resort. Evening Pattaya night market walk.", ["Sightseeing Included: Private luxury van transit, beach orientation", "Evening Experience: Pattaya night market walking tour", "Overnight Stay: Pattaya (Premium Beachfront Resort)", "Meals Included: International Breakfast & Seaside Family Dinner"]),
        _day(4, "Coral Island Marine Expedition", "Private luxury speedboat to Coral Island with snorkeling and beach relaxation. Farewell seafood lunch.", ["Sightseeing Included: Private speedboat to Coral Island, beach relaxation, reef snorkeling", "Overnight Stay: Pattaya (Premium Beachfront Resort)", "Meals Included: International Breakfast & Beachside Seafood Buffet Lunch"]),
        _day(5, "Departure", "Final breakfast overlooking the coast. Private luxury van to Bangkok airport with souvenir stop.", ["Sightseeing Included: Private departure transfer, artisan souvenir stop", "Meals Included: International Buffet Breakfast"]),
    ]


def build_th_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="th-001-bangkok-pattaya-family-tour",
        destination_id=destination_id,
        title="Bangkok Pattaya Family Tour",
        duration_label="04 Nights / 05 Days",
        price=0, rating=Decimal("4.9"), is_featured=True, featured_sort_order=61, is_published=True,
        highlights=[
            PackageHighlightNested(text="Bangkok (2N) → Pattaya (2N) classic family circuit", sort_order=1),
            PackageHighlightNested(text="Grand Palace, Wat Pho & Coral Island speedboat", sort_order=2),
            PackageHighlightNested(text="VIP airport fast-track & private luxury van throughout", sort_order=3),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=4),
            PackageHighlightNested(text="Tour code TRG-BKK-PAT-2026 | Serial TH-001", sort_order=5),
        ],
        moods=["Family", "Luxury", "Cultural", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="th-001-bangkok-pattaya-itinerary", destination_id=destination_id,
        title="Bangkok Pattaya Family Tour", duration_label="04 Nights / 05 Days", duration_days=5,
        starting_price=0, price_note="On Request (Premium Thailand Experience)", rating=Decimal("4.9"), review_count=0,
        tagline="Bangkok • Grand Palace • Pattaya Beach • Coral Island",
        overview="The Best Bangkok Pattaya Tour Package — iconic metropolitan heritage with serene coastal joy. Grand Palace, Coral Island private speedboat, and TRAGUIN premium logistics across 5 days.",
        seo_title="TH-001 | Bangkok Pattaya Family Tour | TRAGUIN",
        seo_description="Premium 04N/05D Thailand family package (TH-001): Grand Palace, Wat Pho, Pattaya, and Coral Island speedboat.",
        is_featured=True, featured_sort_order=61, is_published=True,
        highlights=[ItineraryHighlightNested(text="Grand Palace & Wat Pho", sort_order=1), ItineraryHighlightNested(text="Coral Island Private Speedboat", sort_order=2), ItineraryHighlightNested(text="Pattaya Beachfront Resort", sort_order=3)],
        days=_bkk_pat_days(), hotels=_bkk_pat_hotels("02 Nights", "02 Nights"),
        inclusions=_th_family_bkk_pat_inclusions(),
    )
    return package, itinerary


def build_th_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="th-002-bangkok-pattaya-family-tour",
        destination_id=destination_id,
        title="Bangkok Pattaya Family Tour",
        duration_label="04 Nights / 05 Days",
        price=0, rating=Decimal("4.9"), is_featured=True, featured_sort_order=62, is_published=True,
        highlights=[
            PackageHighlightNested(text="Bangkok (2N) → Pattaya (2N) premium family holiday", sort_order=1),
            PackageHighlightNested(text="Grand Palace, Wat Pho & Coral Island speedboat", sort_order=2),
            PackageHighlightNested(text="VIP airport fast-track & private luxury van throughout", sort_order=3),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=4),
            PackageHighlightNested(text="Tour code TRG-BKK-PAT-2026 | Serial TH-002", sort_order=5),
        ],
        moods=["Family", "Luxury", "Cultural", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="th-002-bangkok-pattaya-itinerary", destination_id=destination_id,
        title="Bangkok Pattaya Family Tour", duration_label="04 Nights / 05 Days", duration_days=5,
        starting_price=0, price_note="On Request (Premium Thailand Experience)", rating=Decimal("4.9"), review_count=0,
        tagline="Bangkok • Grand Palace • Pattaya Beach • Coral Island",
        overview="Optimized Bangkok Pattaya Classic family holiday — iconic temples, bustling markets, and pristine coral islands with TRAGUIN signature premium logistics.",
        seo_title="TH-002 | Bangkok Pattaya Family Tour | TRAGUIN",
        seo_description="Premium 04N/05D Thailand family package (TH-002): Grand Palace, Wat Pho, Pattaya, and Coral Island speedboat.",
        is_featured=True, featured_sort_order=62, is_published=True,
        highlights=[ItineraryHighlightNested(text="Grand Palace & Wat Pho", sort_order=1), ItineraryHighlightNested(text="Coral Island Private Speedboat", sort_order=2), ItineraryHighlightNested(text="Pattaya Night Market", sort_order=3)],
        days=_bkk_pat_days(), hotels=_bkk_pat_hotels("02 Nights", "02 Nights"),
        inclusions=_th_family_bkk_pat_inclusions(),
    )
    return package, itinerary


def _th_family_bkk_pat_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="04 Nights in handpicked premium family hotels across Bangkok and Pattaya", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private luxury executive van with dedicated chauffeur", sort_order=2),
        ItineraryInclusionNested(kind="included", text="VIP airport fast-track reception and Grand Palace guided tour", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Private luxury speedboat charter to Coral Island", sort_order=4),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated on-ground family concierge support", sort_order=5),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Thailand visa processing fees", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Optional parasailing, sea-walking, and tipping", sort_order=8),
    ]


def build_th_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="th-003-bangkok-phuket-family-tour",
        destination_id=destination_id, title="Bangkok Phuket Family Tour",
        duration_label="05 Nights / 06 Days", price=0, rating=Decimal("4.9"),
        is_featured=True, featured_sort_order=63, is_published=True,
        highlights=[
            PackageHighlightNested(text="Bangkok (2N) → Phuket (3N) family expedition", sort_order=1),
            PackageHighlightNested(text="Grand Palace, ICONSIAM & Phi Phi Islands speedboat", sort_order=2),
            PackageHighlightNested(text="Tropical botanical gardens & farewell gala dinner", sort_order=3),
            PackageHighlightNested(text="Tour code TRG-BKK-HKT-FAM-2026 | Serial TH-003", sort_order=4),
        ], moods=["Family", "Luxury", "Cultural", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="th-003-bangkok-phuket-itinerary", destination_id=destination_id,
        title="Bangkok Phuket Family Tour", duration_label="05 Nights / 06 Days", duration_days=6,
        starting_price=0, price_note="On Request (Premium Thailand Experience)", rating=Decimal("4.9"), review_count=0,
        tagline="Bangkok • Grand Palace • Phuket • Phi Phi Islands",
        overview="Best Bangkok Phuket Family Tour — royal heritage in Bangkok and azure island paradise in Phuket with private Phi Phi speedboat charter.",
        seo_title="TH-003 | Bangkok Phuket Family Tour | TRAGUIN",
        seo_description="Premium 05N/06D Thailand family package (TH-003): Grand Palace, ICONSIAM, Phi Phi Islands, and Phuket botanical gardens.",
        is_featured=True, featured_sort_order=63, is_published=True,
        highlights=[ItineraryHighlightNested(text="Grand Palace & ICONSIAM", sort_order=1), ItineraryHighlightNested(text="Phi Phi Islands Private Speedboat", sort_order=2), ItineraryHighlightNested(text="Phuket Botanical Gardens", sort_order=3)],
        days=[
            _day(1, "Arrival in Bangkok & Riverfront Welcome", "VIP reception at Suvarnabhumi. Private van to premium hotel. Welcome dinner at river-view restaurant.", ["Sightseeing Included: Airport reception, city orientation", "Overnight Stay: Bangkok (Premium Lifestyle Family Hotel)", "Meals Included: International Welcome Buffet Dinner"]),
            _day(2, "Bangkok Heritage & ICONSIAM", "Grand Palace, Wat Phra Kaew, Wat Pho, and ICONSIAM luxury waterfront mall.", ["Sightseeing Included: Grand Palace, Wat Phra Kaew, Wat Pho, ICONSIAM", "Overnight Stay: Bangkok (Premium Lifestyle Family Hotel)", "Meals Included: International Breakfast & Traditional Thai Bistro Lunch"]),
            _day(3, "Bangkok to Phuket Coastal Escape", "Internal flight to Phuket. Beachfront resort check-in and Andaman sunset.", ["Sightseeing Included: Internal flight coordination, beachfront check-in", "Overnight Stay: Phuket (Premium Ocean View Family Resort)", "Meals Included: International Breakfast & Beachfront Family Dinner"]),
            _day(4, "Phi Phi Islands Marine Expedition", "Private speedboat to Phi Phi Islands with snorkeling and island buffet lunch.", ["Sightseeing Included: Private speedboat to Phi Phi Islands, reef snorkeling", "Overnight Stay: Phuket (Premium Ocean View Family Resort)", "Meals Included: International Breakfast & Island Beachside Buffet Lunch"]),
            _day(5, "Cultural Gardens & Farewell Gala", "Tropical botanical gardens tour. Grand farewell gala dinner.", ["Sightseeing Included: Tropical garden botanical tour", "Evening Experience: Grand farewell gala dinner", "Overnight Stay: Phuket (Premium Ocean View Family Resort)", "Meals Included: International Buffet Breakfast & Farewell Dinner"]),
            _day(6, "Phuket Departure", "Final breakfast at resort. Private transfer to Phuket International Airport.", ["Sightseeing Included: Private airport departure transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="The Sukosol Bangkok / similar", location="Bangkok", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="Novotel Phuket Resort / similar", location="Phuket", nights_label="03 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="Grande Centre Point Terminal 21", location="Bangkok", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=4, sort_order=3),
            ItineraryHotelNested(name="Phuket Marriott Merlin Beach", location="Phuket", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=4),
            ItineraryHotelNested(name="Avani+ Riverside Bangkok", location="Bangkok", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="The Westin Siray Bay", location="Phuket", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="Shangri-La Bangkok", location="Bangkok", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="Anantara Layan / Sri Panwa", location="Phuket", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=8),
        ],
        inclusions=_th003_inclusions(),
    )
    return package, itinerary


def _th003_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="05 Nights in premium family hotels across Bangkok and Phuket", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private luxury van and domestic flight coordination to Phuket", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Grand Palace, ICONSIAM, and Phi Phi Islands private speedboat", sort_order=3),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated family concierge support", sort_order=4),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Thailand visa fees", sort_order=5),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses and optional activities", sort_order=6),
    ]


def build_th_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="th-004-phuket-krabi-family-tour",
        destination_id=destination_id, title="Phuket Krabi Family Tour",
        duration_label="05 Nights / 06 Days", price=0, rating=Decimal("4.9"),
        is_featured=True, featured_sort_order=64, is_published=True,
        highlights=[
            PackageHighlightNested(text="Phuket (3N) → Krabi (2N) Andaman family circuit", sort_order=1),
            PackageHighlightNested(text="Phi Phi Maya Bay & Krabi 4-Islands speed-craft", sort_order=2),
            PackageHighlightNested(text="Big Buddha, Old Phuket Town & Ao Nang fire show", sort_order=3),
            PackageHighlightNested(text="Tour code TRG-HKT-KBV-FAM-2026 | Serial TH-004", sort_order=4),
        ], moods=["Family", "Luxury", "Beach", "Adventure", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="th-004-phuket-krabi-itinerary", destination_id=destination_id,
        title="Phuket Krabi Family Tour", duration_label="05 Nights / 06 Days", duration_days=6,
        starting_price=0, price_note="On Request (Premium Thailand Experience)", rating=Decimal("4.9"), review_count=0,
        tagline="Phuket • Krabi • Phi Phi Islands • Ao Nang Bay",
        overview="Premium Phuket Krabi coastal odyssey — Phi Phi private speedboat, Big Buddha, Old Phuket Town, and Krabi 4-Islands expedition.",
        seo_title="TH-004 | Phuket Krabi Family Tour | TRAGUIN",
        seo_description="Premium 05N/06D Thailand family package (TH-004): Phi Phi Islands, Big Buddha, Krabi 4-Islands, and Ao Nang fire show.",
        is_featured=True, featured_sort_order=64, is_published=True,
        highlights=[ItineraryHighlightNested(text="Phi Phi Maya Bay Speedboat", sort_order=1), ItineraryHighlightNested(text="Big Buddha & Old Phuket Town", sort_order=2), ItineraryHighlightNested(text="Krabi 4-Islands Expedition", sort_order=3)],
        days=[
            _day(1, "Arrival in Phuket & Coastal Welcome", "Traditional Thai greeting at Phuket Airport. Private luxury van to premium beachfront resort. Welcome seaside dinner.", ["Sightseeing Included: Private airport transit, Patong beach orientation", "Overnight Stay: Phuket (Premium Luxury Beachfront Resort)", "Meals Included: Curated Multi-Cuisine Welcome Dinner"]),
            _day(2, "Private Speedboat to Phi Phi Islands", "Private speedboat to Maya Bay, Pileh Lagoon, Bamboo Island, and Viking Cave with island picnic lunch.", ["Sightseeing Included: Private speedboat Phi Phi tour, Maya Bay, Pileh Lagoon, Bamboo Island", "Overnight Stay: Phuket (Premium Luxury Beachfront Resort)", "Meals Included: International Buffet Breakfast & Beachside Island Picnic Lunch"]),
            _day(3, "Phuket Cultural Tour & Departure to Krabi", "Big Buddha, Wat Chalong, Old Phuket Town. Scenic drive to Krabi Ao Nang.", ["Sightseeing Included: Big Buddha, Wat Chalong, Old Phuket Town, cross-province drive", "Overnight Stay: Krabi (Premium Luxury Beachfront Resort)", "Meals Included: International Buffet Breakfast & Thai Fine Dining Lunch"]),
            _day(4, "Krabi 4-Islands Expedition", "Private speed-craft to Tup Island sandbar, Chicken Island snorkeling, Poda Island, and Phra Nang Cave. Ao Nang fire show.", ["Sightseeing Included: Krabi 4-Islands, Tup sandbar, Chicken Island reef, fire show", "Overnight Stay: Krabi (Premium Luxury Beachfront Resort)", "Meals Included: International Buffet Breakfast & Beachside Family Lunch"]),
            _day(5, "Krabi Retreat & Departure", "Final breakfast overlooking the ocean. Private transfer to Krabi International Airport.", ["Sightseeing Included: Boutique souvenir shopping, private airport transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Novotel Phuket Resort / similar", location="Phuket", nights_label="03 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="Ao Nang Cliff Beach Resort / similar", location="Krabi", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="Phuket Marriott Merlin Beach", location="Phuket", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=3),
            ItineraryHotelNested(name="Centara Grand Beach Resort Krabi", location="Krabi", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=4),
            ItineraryHotelNested(name="The Westin Siray Bay", location="Phuket", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="Rayavadee Krabi Resort", location="Krabi", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="Anantara Layan Phuket / Sri Panwa", location="Phuket", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="Phulay Bay, Ritz-Carlton Reserve", location="Krabi", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=8),
        ],
        inclusions=_th004_inclusions(),
    )
    return package, itinerary


def _th004_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="05 Nights in handpicked premium family resorts across Phuket and Krabi", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private luxury van and private speedboat to Phi Phi Islands", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Krabi 4-Islands private speed-craft charter", sort_order=3),
        ItineraryInclusionNested(kind="included", text="VIP front-row seats at Ao Nang beach fire show", sort_order=4),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Thailand visa fees", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses and optional water-sports", sort_order=7),
    ]


def build_th_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="th-005-thailand-premium-family-tour",
        destination_id=destination_id, title="Thailand Premium Family Tour",
        duration_label="07 Nights / 08 Days", price=0, rating=Decimal("4.9"),
        is_featured=True, featured_sort_order=65, is_published=True,
        highlights=[
            PackageHighlightNested(text="Phuket (3N) → Pattaya (2N) → Bangkok (2N) grand circuit", sort_order=1),
            PackageHighlightNested(text="Phi Phi speedboat, Alcazar Show & Coral Island", sort_order=2),
            PackageHighlightNested(text="Chao Phraya dinner cruise & Safari World", sort_order=3),
            PackageHighlightNested(text="Tour code TRG-THA-2026-V5 | Serial TH-005", sort_order=4),
        ], moods=["Family", "Luxury", "Cultural", "Beach", "Adventure", "Wildlife"],
    )
    itinerary = ItineraryCreate(
        slug="th-005-thailand-premium-itinerary", destination_id=destination_id,
        title="Thailand Premium Family Tour", duration_label="07 Nights / 08 Days", duration_days=8,
        starting_price=0, price_note="On Request (Premium Thailand Experience)", rating=Decimal("4.9"), review_count=0,
        tagline="Bangkok • Pattaya • Phuket • Phi Phi Islands",
        overview="Comprehensive 8-day Thailand Discovery — Phuket Phi Phi speedboat, Pattaya Alcazar and Coral Island, Bangkok temples, Chao Phraya cruise, and Safari World.",
        seo_title="TH-005 | Thailand Premium Family Tour | TRAGUIN",
        seo_description="Luxury 07N/08D Thailand family package (TH-005): Phuket, Phi Phi, Pattaya, Coral Island, Bangkok temples, and Safari World.",
        is_featured=True, featured_sort_order=65, is_published=True,
        highlights=[ItineraryHighlightNested(text="Phi Phi Islands Private Speedboat", sort_order=1), ItineraryHighlightNested(text="Alcazar Cabaret VIP Seats", sort_order=2), ItineraryHighlightNested(text="Chao Phraya Dinner Cruise", sort_order=3), ItineraryHighlightNested(text="Safari World & Marine Park", sort_order=4)],
        days=[
            _day(1, "Phuket Arrival", "Warm Thai welcome at Phuket Airport. Transfer to premium beachfront resort. Welcome sunset dinner.", ["Sightseeing Included: Coastal transfer, Patong Beach leisure", "Overnight Stay: Phuket (Premium Luxury Beachfront Resort)", "Meals Included: Curated Welcome Dinner"]),
            _day(2, "Phuket to Phi Phi Islands", "Private speedboat to Maya Bay, Pileh Lagoon, Bamboo Island, Viking Cave, and Monkey Beach.", ["Sightseeing Included: Private speedboat Phi Phi tour", "Overnight Stay: Phuket (Premium Luxury Beachfront Resort)", "Meals Included: International Buffet Breakfast & Beachside Island Lunch"]),
            _day(3, "Phuket City Exploration", "Big Buddha, Wat Chalong, Old Phuket Town, Karon Viewpoint. Sunset at Phromthep Cape.", ["Sightseeing Included: Big Buddha, Wat Chalong, Old Phuket Town, Phromthep Cape", "Overnight Stay: Phuket (Premium Luxury Beachfront Resort)", "Meals Included: International Buffet Breakfast & Traditional Thai Fine Dining"]),
            _day(4, "Phuket to Pattaya", "Flight to Bangkok and drive to Pattaya. VIP Alcazar Cabaret Show with front-row seats.", ["Sightseeing Included: Domestic flight transit, Alcazar Show VIP entry", "Overnight Stay: Pattaya (Premium Ocean View Hotel)", "Meals Included: International Buffet Breakfast & Indian Culinary Buffet Dinner"]),
            _day(5, "Pattaya Coral Island", "Private speedboat to Coral Island with parasailing and banana boat. Fresh seafood lunch.", ["Sightseeing Included: Private speedboat Coral Island, parasailing, banana boat", "Overnight Stay: Pattaya (Premium Ocean View Hotel)", "Meals Included: International Buffet Breakfast & Premium Seafood Lunch"]),
            _day(6, "Pattaya to Bangkok", "Wat Traimit Golden Buddha and Wat Pho. Grand Pearl Chao Phraya dinner cruise.", ["Sightseeing Included: Wat Traimit, Wat Pho, Grand Pearl dinner cruise", "Overnight Stay: Bangkok (Ultra-Luxury Riverside Hotel)", "Meals Included: International Buffet Breakfast & Premium Cruise Dinner"]),
            _day(7, "Bangkok Family Fun & Shopping", "Safari World & Marine Park. ICONSIAM luxury shopping.", ["Sightseeing Included: Safari World drive, marine park shows, ICONSIAM", "Overnight Stay: Bangkok (Ultra-Luxury Riverside Hotel)", "Meals Included: International Buffet Breakfast & Safari World Buffet Lunch"]),
            _day(8, "Bangkok Departure", "Final breakfast. Private transfer to Suvarnabhumi International Airport.", ["Sightseeing Included: Private airport departure transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Novotel Phuket Resort", location="Phuket", nights_label="03 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="Amari Pattaya", location="Pattaya", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="The Sukosol Bangkok", location="Bangkok", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=3),
            ItineraryHotelNested(name="Phuket Marriott Merlin Beach", location="Phuket", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=4),
            ItineraryHotelNested(name="Hilton Pattaya", location="Pattaya", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="Avani+ Riverside Bangkok", location="Bangkok", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="The Westin Siray Bay", location="Phuket", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="Shangri-La Bangkok", location="Bangkok", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=8),
            ItineraryHotelNested(name="Anantara Layan Phuket", location="Phuket", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=9),
            ItineraryHotelNested(name="Mandarin Oriental, Bangkok", location="Bangkok", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=10),
        ],
        inclusions=_th005_inclusions(),
    )
    return package, itinerary


def _th005_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="07 Nights in handpicked premium hotels across Phuket, Pattaya, and Bangkok", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Dedicated luxury van for all transfers and tours", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Private speedboat to Phi Phi Island and Pattaya Coral Island", sort_order=3),
        ItineraryInclusionNested(kind="included", text="VIP Alcazar Show and Grand Pearl Chao Phraya dinner cruise", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Safari World & Marine Park full-day admission", sort_order=5),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated family concierge support", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="International and domestic flight tickets", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Thailand visa fees and personal expenses", sort_order=8),
    ]


def build_th_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="th-006-phuket-honeymoon-package",
        destination_id=destination_id, title="Phuket Honeymoon Package",
        duration_label="04 Nights / 05 Days", price=0, rating=Decimal("4.9"),
        is_featured=True, featured_sort_order=66, is_published=True,
        highlights=[
            PackageHighlightNested(text="Phuket (4N) ultra-luxury romantic island escape", sort_order=1),
            PackageHighlightNested(text="Private catamaran Phi Phi & twilight yacht cruise", sort_order=2),
            PackageHighlightNested(text="120-min couple's spa & beachfront candlelight dinner", sort_order=3),
            PackageHighlightNested(text="Tour code TRG-HKT-HON-2026 | Serial TH-006", sort_order=4),
        ], moods=["Romantic", "Luxury", "Beach", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="th-006-phuket-honeymoon-itinerary", destination_id=destination_id,
        title="Phuket Honeymoon Package", duration_label="04 Nights / 05 Days", duration_days=5,
        starting_price=0, price_note="On Request (Premium Honeymoon Experience)", rating=Decimal("4.9"), review_count=0,
        tagline="Phuket • Phi Phi Islands • Phang Nga Bay • Patong",
        overview="Ultimate Phuket Honeymoon — private pool villa, catamaran Phi Phi cruise, twilight yacht, couple's spa, James Bond Island, and beachfront candlelight dinner.",
        seo_title="TH-006 | Phuket Honeymoon Package | TRAGUIN",
        seo_description="Luxury 04N/05D Phuket honeymoon (TH-006): private catamaran, twilight yacht, couple's spa, and candlelight dinner.",
        is_featured=True, featured_sort_order=66, is_published=True,
        highlights=[ItineraryHighlightNested(text="Private Catamaran Phi Phi Cruise", sort_order=1), ItineraryHighlightNested(text="Twilight Yacht & Promthep Cape", sort_order=2), ItineraryHighlightNested(text="James Bond Island & Couple's Spa", sort_order=3)],
        days=[
            _day(1, "Arrival in Phuket & Sunset Luxury", "Orchid welcome at Phuket Airport. Transfer to ultra-luxury pool villa with sparkling wine. Private beachfront candlelight dinner.", ["Sightseeing Included: Private airport transfer", "Evening Experience: Signature beachfront private candlelight dinner", "Overnight Stay: Phuket (Ultra-Luxury Private Pool Villa)", "Meals Included: 4-Course Gourmet Beachfront Dinner"]),
            _day(2, "Phi Phi Islands by Private Catamaran", "Private catamaran to Maya Bay, Pileh Lagoon, and Bamboo Island with gourmet picnic lunch.", ["Sightseeing Included: Private catamaran cruise to Phi Phi Islands", "Overnight Stay: Phuket (Ultra-Luxury Private Pool Villa)", "Meals Included: Buffet Breakfast & Catamaran Gourmet Picnic Lunch"]),
            _day(3, "Sunset Cruise & Spa Immersion", "Floating breakfast. 120-minute couple's spa therapy. Twilight yacht cruise to Promthep Cape.", ["Sightseeing Included: Twilight yacht cruise, Promthep Cape views", "Overnight Stay: Phuket (Ultra-Luxury Private Pool Villa)", "Meals Included: Floating Villa Breakfast & Twilight Yacht Canapés"]),
            _day(4, "Phang Nga Bay & Heritage Discovery", "James Bond Island, Koh Hong sea cave kayaking, Old Phuket Town, and Karon Viewpoint.", ["Sightseeing Included: James Bond Island, Koh Hong kayaking, Old Phuket Town", "Overnight Stay: Phuket (Ultra-Luxury Private Pool Villa)", "Meals Included: Buffet Breakfast & Authentic Thai Fine Dining Lunch"]),
            _day(5, "Phuket Departure", "Final breakfast at villa. Private transfer to Phuket International Airport.", ["Sightseeing Included: Private airport departure transfer", "Meals Included: Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Pullman Phuket Arcadia Naithon Beach / similar", location="Phuket", nights_label="04 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="The Pavilion Phuket / similar", location="Phuket", nights_label="04 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=2),
            ItineraryHotelNested(name="The Shore at Katathani", location="Phuket", nights_label="04 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=3),
            ItineraryHotelNested(name="Trisara Phuket / Sri Panwa", location="Phuket", nights_label="04 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=4),
        ],
        inclusions=_th006_inclusions(),
    )
    return package, itinerary


def _th006_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="04 Nights in handpicked premium pool villas in Phuket", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Premium sparkling wine, floral decorations, and honeymoon amenities", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Private catamaran Phi Phi cruise and twilight yacht cruise", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Complimentary 120-minute couple's spa treatment", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Beachfront private candlelight dinner", sort_order=5),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 honeymoon concierge support", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Thailand visa fees", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="National park fees and personal expenses", sort_order=8),
    ]


def build_th_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="th-007-phuket-krabi-honeymoon",
        destination_id=destination_id, title="Phuket Krabi Honeymoon",
        duration_label="05 Nights / 06 Days", price=0, rating=Decimal("4.9"),
        is_featured=True, featured_sort_order=67, is_published=True,
        highlights=[
            PackageHighlightNested(text="Phuket (3N) → Krabi (2N) twin-island romantic escape", sort_order=1),
            PackageHighlightNested(text="Catamaran Phi Phi & Krabi 4-Islands candlelight finale", sort_order=2),
            PackageHighlightNested(text="120-min couple's spa & Promthep Cape sunset", sort_order=3),
            PackageHighlightNested(text="Tour code TRG-HKT-KBV-HON-2026 | Serial TH-007", sort_order=4),
        ], moods=["Romantic", "Luxury", "Beach", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="th-007-phuket-krabi-honeymoon-itinerary", destination_id=destination_id,
        title="Phuket Krabi Honeymoon", duration_label="05 Nights / 06 Days", duration_days=6,
        starting_price=0, price_note="On Request (Premium Honeymoon Experience)", rating=Decimal("4.9"), review_count=0,
        tagline="Phuket • Phi Phi Islands • Krabi • Ao Nang Beach",
        overview="Phuket Krabi twin-island honeymoon — catamaran Phi Phi, couple's spa, Krabi 4-Islands, and private beachfront candlelight finale.",
        seo_title="TH-007 | Phuket Krabi Honeymoon | TRAGUIN",
        seo_description="Premium 05N/06D Phuket Krabi honeymoon (TH-007): Phi Phi catamaran, couple's spa, and Krabi candlelight dinner.",
        is_featured=True, featured_sort_order=67, is_published=True,
        highlights=[ItineraryHighlightNested(text="Phi Phi Catamaran Cruise", sort_order=1), ItineraryHighlightNested(text="Old Phuket Town & Couple's Spa", sort_order=2), ItineraryHighlightNested(text="Krabi 4-Islands & Candlelight Finale", sort_order=3)],
        days=[
            _day(1, "Phuket Arrival & Sunset Twilight", "Floral welcome at Phuket Airport. Ocean-facing honeymoon suite with sparkling wine. Promthep Cape sunset.", ["Sightseeing Included: Private transfer, Promthep Cape sunset", "Overnight Stay: Phuket (Premium Luxury Beachfront Resort)", "Meals Included: Gourmet Welcome Dinner"]),
            _day(2, "Phi Phi Islands Escape", "Private catamaran to Maya Bay, Pileh Lagoon, Bamboo Island, and Viking Cave.", ["Sightseeing Included: Premium catamaran Phi Phi tour", "Overnight Stay: Phuket (Premium Luxury Beachfront Resort)", "Meals Included: International Buffet Breakfast & Beachside Gourmet Lunch"]),
            _day(3, "Phuket Heritage & Spa Indulgence", "Floating breakfast. Old Phuket Town, Wat Chalong, Karon Viewpoint. 120-minute couple's aroma-spa.", ["Sightseeing Included: Old Phuket Town, Wat Chalong, Karon Viewpoint", "Overnight Stay: Phuket (Premium Luxury Beachfront Resort)", "Meals Included: International Buffet Breakfast & Thai Fine Dining Platter"]),
            _day(4, "Phuket to Krabi via Scenic Highway", "Scenic drive to Krabi Ao Nang. Evening candlelit seaside dinner.", ["Sightseeing Included: Cross-province scenic drive, Ao Nang orientation", "Overnight Stay: Krabi (Premium Cliffside Resort)", "Meals Included: International Buffet Breakfast & Curated Sunset Dinner"]),
            _day(5, "Krabi 4-Island Adventure & Candlelight Finale", "Private speed-craft to Phra Nang Cave, Tup sandbar, Poda Island, and Chicken Island. Grand beachfront candlelight dinner.", ["Sightseeing Included: Krabi 4-Islands expedition", "Evening Experience: Signature beachfront candlelight dinner", "Overnight Stay: Krabi (Premium Cliffside Resort)", "Meals Included: International Buffet Breakfast & Private Box Dinner"]),
            _day(6, "Krabi Departure", "Final breakfast. Private transfer to Krabi International Airport.", ["Sightseeing Included: Private airport departure transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Novotel Phuket Kamala Beach / similar", location="Phuket", nights_label="03 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="Ao Nang Cliff Beach Resort / similar", location="Krabi", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="Amari Phuket", location="Phuket", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=3),
            ItineraryHotelNested(name="Centara Grand Beach Resort Krabi", location="Krabi", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=4),
            ItineraryHotelNested(name="The Shore at Katathani", location="Phuket", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="Rayavadee Krabi Resort", location="Krabi", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="Sri Panwa Luxury Pool Villa", location="Phuket", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="Phulay Bay, Ritz-Carlton Reserve", location="Krabi", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=8),
        ],
        inclusions=_th007_inclusions(),
    )
    return package, itinerary


def _th007_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="05 Nights in handpicked romantic hotels across Phuket and Krabi", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Honeymoon bed styling, welcome wine, and fruit platters", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Premium catamaran Phi Phi tour and Krabi 4-Islands speed-craft", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Private beachfront candlelight dinner in Krabi", sort_order=4),
        ItineraryInclusionNested(kind="included", text="120-minute premium couple's aroma-spa treatment", sort_order=5),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 honeymoon concierge support", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Thailand visa fees", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="National park fees and personal expenses", sort_order=8),
    ]


def build_th_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="th-008-thailand-romance-package",
        destination_id=destination_id, title="Thailand Romance Package",
        duration_label="06 Nights / 07 Days", price=0, rating=Decimal("4.9"),
        is_featured=True, featured_sort_order=68, is_published=True,
        highlights=[
            PackageHighlightNested(text="Phuket (2N) → Krabi (2N) → Bangkok (2N) multi-destination honeymoon", sort_order=1),
            PackageHighlightNested(text="Phi Phi speedboat & Krabi candlelight dinner", sort_order=2),
            PackageHighlightNested(text="Chao Phraya luxury dinner cruise & ICONSIAM", sort_order=3),
            PackageHighlightNested(text="Tour code TRG-THA-ROM-2026 | Serial TH-008", sort_order=4),
        ], moods=["Romantic", "Luxury", "Cultural", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="th-008-thailand-romance-itinerary", destination_id=destination_id,
        title="Thailand Romance Package", duration_label="06 Nights / 07 Days", duration_days=7,
        starting_price=0, price_note="On Request (Premium Honeymoon Experience)", rating=Decimal("4.9"), review_count=0,
        tagline="Phuket • Krabi • Bangkok",
        overview="Ultimate multi-destination Thailand honeymoon — Phi Phi speedboat, Krabi 4-Islands candlelight dinner, and Bangkok Chao Phraya luxury cruise.",
        seo_title="TH-008 | Thailand Romance Package | TRAGUIN",
        seo_description="Luxury 06N/07D Thailand honeymoon (TH-008): Phuket, Krabi, Bangkok temples, and Chao Phraya cruise.",
        is_featured=True, featured_sort_order=68, is_published=True,
        highlights=[ItineraryHighlightNested(text="Phi Phi Private Speedboat", sort_order=1), ItineraryHighlightNested(text="Krabi Beachfront Candlelight Dinner", sort_order=2), ItineraryHighlightNested(text="Chao Phraya Dinner Cruise", sort_order=3)],
        days=[
            _day(1, "Phuket Arrival & Romantic Sunset", "Floral welcome. Sea-view honeymoon suite with sparkling wine. Phromthep Cape sunset.", ["Sightseeing Included: Private transfer, Phromthep Cape sunset", "Overnight Stay: Phuket (Premium Luxury Beachfront Resort)", "Meals Included: Curated Welcome Dinner"]),
            _day(2, "Phi Phi Islands Adventure", "Private speedboat to Maya Bay, Pileh Lagoon, Bamboo Island, and Viking Cave.", ["Sightseeing Included: Private speedboat Phi Phi tour", "Overnight Stay: Phuket (Premium Luxury Beachfront Resort)", "Meals Included: International Buffet Breakfast & Beachside Island Lunch"]),
            _day(3, "Phuket to Krabi Transit", "Floating breakfast option. Scenic drive to Krabi Ao Nang. Candlelit beachside dinner.", ["Sightseeing Included: Scenic highway drive to Krabi", "Overnight Stay: Krabi (Premium Cliffside Resort)", "Meals Included: International Buffet Breakfast & Curated Sunset Dinner"]),
            _day(4, "Krabi 4-Island Expedition", "Phra Nang Cave, Tup sandbar, Poda Island, Chicken Island. Grand beachfront candlelight finale.", ["Sightseeing Included: Krabi 4-Islands expedition", "Evening Experience: Grand beachfront candlelight dinner", "Overnight Stay: Krabi (Premium Cliffside Resort)", "Meals Included: International Buffet Breakfast & Private Box Dinner"]),
            _day(5, "Krabi to Bangkok", "Flight to Bangkok. Grand Pearl Chao Phraya 5-star dinner cruise.", ["Sightseeing Included: Domestic flight transit, Grand Pearl dinner cruise", "Overnight Stay: Bangkok (Ultra-Luxury Riverside Hotel)", "Meals Included: International Buffet Breakfast & Premium Cruise Dinner"]),
            _day(6, "Bangkok Temples & ICONSIAM", "Wat Traimit Golden Buddha, Wat Pho, and ICONSIAM luxury shopping.", ["Sightseeing Included: Wat Traimit, Wat Pho, ICONSIAM", "Overnight Stay: Bangkok (Ultra-Luxury Riverside Hotel)", "Meals Included: International Buffet Breakfast & Premium Thai Dining Lunch"]),
            _day(7, "Bangkok Departure", "Final breakfast. Private transfer to Suvarnabhumi International Airport.", ["Sightseeing Included: Private airport departure transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Novotel Phuket Resort", location="Phuket", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="Ao Nang Cliff Beach Resort", location="Krabi", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="The Sukosol Bangkok", location="Bangkok", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=3),
            ItineraryHotelNested(name="Phuket Marriott Merlin Beach", location="Phuket", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=4),
            ItineraryHotelNested(name="Centara Grand Beach Resort Krabi", location="Krabi", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="Avani+ Riverside Bangkok", location="Bangkok", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="The Westin Siray Bay", location="Phuket", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="Rayavadee Krabi", location="Krabi", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=8),
            ItineraryHotelNested(name="Anantara Layan Phuket", location="Phuket", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=9),
            ItineraryHotelNested(name="Mandarin Oriental, Bangkok", location="Bangkok", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=10),
        ],
        inclusions=_th008_inclusions(),
    )
    return package, itinerary


def _th008_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="06 Nights in premium honeymoon hotels across Phuket, Krabi, and Bangkok", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private speedboat Phi Phi tour and Krabi 4-Islands charter", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Private beachfront candlelight dinner in Krabi", sort_order=3),
        ItineraryInclusionNested(kind="included", text="5-star Chao Phraya River dinner cruise in Bangkok", sort_order=4),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 honeymoon concierge support", sort_order=5),
        ItineraryInclusionNested(kind="excluded", text="International and domestic flights", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="Thailand visa fees and personal expenses", sort_order=7),
    ]


def build_th_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="th-009-girls-trip-thailand",
        destination_id=destination_id, title="Girls Trip Thailand",
        duration_label="05 Nights / 06 Days", price=0, rating=Decimal("4.9"),
        is_featured=True, featured_sort_order=69, is_published=True,
        highlights=[
            PackageHighlightNested(text="Pattaya (2N) → Bangkok (3N) all-female luxury getaway", sort_order=1),
            PackageHighlightNested(text="Coral Island speedboat & Alcazar VIP show", sort_order=2),
            PackageHighlightNested(text="Mahanakhon SkyWalk & floating market tour", sort_order=3),
            PackageHighlightNested(text="Tour code TRG-THA-FEM-2026 | Serial TH-009", sort_order=4),
        ], moods=["Solo", "Luxury", "Beach", "Cultural"],
    )
    itinerary = ItineraryCreate(
        slug="th-009-girls-trip-thailand-itinerary", destination_id=destination_id,
        title="Girls Trip Thailand", duration_label="05 Nights / 06 Days", duration_days=6,
        starting_price=0, price_note="On Request (Premium Girls Escape)", rating=Decimal("4.9"), review_count=0,
        tagline="Bangkok • Pattaya • Coral Island Escape",
        overview="Ultimate Girls Trip Thailand — Coral Island private speedboat, Alcazar VIP, Mahanakhon SkyWalk, floating market, cafe hop, and group spa retreat.",
        seo_title="TH-009 | Girls Trip Thailand | TRAGUIN",
        seo_description="Premium 05N/06D Thailand girls trip (TH-009): Pattaya Coral Island, Alcazar Show, Mahanakhon SkyWalk, and ICONSIAM.",
        is_featured=True, featured_sort_order=69, is_published=True,
        highlights=[ItineraryHighlightNested(text="Coral Island Private Speedboat", sort_order=1), ItineraryHighlightNested(text="Alcazar Cabaret VIP", sort_order=2), ItineraryHighlightNested(text="Mahanakhon SkyWalk", sort_order=3), ItineraryHighlightNested(text="120-Min Group Spa", sort_order=4)],
        days=[
            _day(1, "Arrival & Transit to Pattaya", "Warm welcome at Suvarnabhumi. Private van to Pattaya ocean-view hotel. Welcome beachfront dinner.", ["Sightseeing Included: Airport pickup, scenic transit to Pattaya", "Overnight Stay: Pattaya (Premium Ocean View Hotel)", "Meals Included: Curated Welcome Dinner"]),
            _day(2, "Coral Island & Cabaret Glamour", "Private speedboat to Coral Island with parasailing and banana boat. VIP Alcazar Cabaret Show.", ["Sightseeing Included: Coral Island speedboat, Alcazar VIP entry", "Overnight Stay: Pattaya (Premium Ocean View Hotel)", "Meals Included: International Buffet Breakfast & Premium Seafood Lunch"]),
            _day(3, "Pattaya to Bangkok & Rooftop Celebration", "Wat Traimit and Wat Pho. Mahanakhon SkyWalk glass tray. Premium rooftop lounge dinner.", ["Sightseeing Included: Wat Traimit, Wat Pho, Mahanakhon SkyWalk VIP entry", "Overnight Stay: Bangkok (Premium Lifestyle City Hotel)", "Meals Included: International Buffet Breakfast & Thai Evening Tasting Platter"]),
            _day(4, "Floating Market & Cafe Trail", "Damnoen Saduak floating market longtail boat. TRAGUIN cafe hop in Ari/Thonglor. Jodd Fairs night bazaar.", ["Sightseeing Included: Damnoen Saduak boat tour, cafe hop, Jodd Fairs", "Overnight Stay: Bangkok (Premium Lifestyle City Hotel)", "Meals Included: International Buffet Breakfast & Cafe Lunch"]),
            _day(5, "Shopping & Luxury Spa Retreat", "ICONSIAM and Siam Paragon shopping. 120-minute group luxury spa and massage. Riverfront farewell dinner.", ["Sightseeing Included: ICONSIAM, Siam Paragon", "Evening Experience: Farewell dinner at riverside restaurant", "Overnight Stay: Bangkok (Premium Lifestyle City Hotel)", "Meals Included: International Buffet Breakfast & Riverfront Farewell Dinner"]),
            _day(6, "Bangkok Departure", "Final breakfast. Private transfer to Suvarnabhumi International Airport.", ["Sightseeing Included: Private airport departure transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Novotel Pattaya / similar", location="Pattaya", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="The Sukosol Bangkok / similar", location="Bangkok", nights_label="03 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="Amari Pattaya Resort", location="Pattaya", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=4, sort_order=3),
            ItineraryHotelNested(name="Grande Centre Point Terminal 21", location="Bangkok", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=4, sort_order=4),
            ItineraryHotelNested(name="Hilton Pattaya", location="Pattaya", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="Avani+ Riverside Bangkok", location="Bangkok", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="Grande Centre Point Space Pattaya", location="Pattaya", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="W Bangkok / Shangri-La Bangkok", location="Bangkok", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=8),
        ],
        inclusions=_th009_inclusions(),
    )
    return package, itinerary


def _th009_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="05 Nights in premium hotels across Pattaya and Bangkok", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private speedboat Coral Island with parasailing and banana boat", sort_order=2),
        ItineraryInclusionNested(kind="included", text="VIP Alcazar Show and Mahanakhon SkyWalk entry", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Damnoen Saduak floating market and 120-minute group spa", sort_order=4),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 female-friendly concierge support", sort_order=5),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Thailand visa fees", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="Personal shopping and rooftop drink extras", sort_order=7),
    ]


def build_th_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="th-011-relax-thailand-senior-tour",
        destination_id=destination_id, title="Relax Thailand Senior Tour",
        duration_label="05 Nights / 06 Days", price=0, rating=Decimal("4.9"),
        is_featured=True, featured_sort_order=70, is_published=True,
        highlights=[
            PackageHighlightNested(text="Pattaya (2N) → Bangkok (3N) senior-friendly calm holiday", sort_order=1),
            PackageHighlightNested(text="Nong Nooch Gardens & Damnoen Saduak floating market", sort_order=2),
            PackageHighlightNested(text="Accessible temples & Chao Phraya dinner cruise", sort_order=3),
            PackageHighlightNested(text="Tour code TRG-THA-SNR-2026 | Serial TH-011", sort_order=4),
        ], moods=["Family", "Luxury", "Cultural", "Spiritual"],
    )
    itinerary = ItineraryCreate(
        slug="th-011-relax-thailand-itinerary", destination_id=destination_id,
        title="Relax Thailand Senior Tour", duration_label="05 Nights / 06 Days", duration_days=6,
        starting_price=0, price_note="On Request (Senior Citizen Special)", rating=Decimal("4.9"), review_count=0,
        tagline="Bangkok • Pattaya • Pure Serenity & Cultural Wonders",
        overview="Relax Thailand senior special — slow-paced exploration, Nong Nooch Botanical Gardens, accessible temples, floating market, and Chao Phraya dinner cruise.",
        seo_title="TH-011 | Relax Thailand Senior Tour | TRAGUIN",
        seo_description="Premium 05N/06D Thailand senior tour (TH-011): Nong Nooch Gardens, floating market, temples, and river cruise.",
        is_featured=True, featured_sort_order=70, is_published=True,
        highlights=[ItineraryHighlightNested(text="Nong Nooch Botanical Gardens", sort_order=1), ItineraryHighlightNested(text="Damnoen Saduak Floating Market", sort_order=2), ItineraryHighlightNested(text="Chao Phraya Dinner Cruise", sort_order=3)],
        days=[
            _day(1, "Arrival & Transit to Pattaya", "Warm concierge reception at Suvarnabhumi. Low step-in luxury van to Pattaya accessible sea-view resort.", ["Sightseeing Included: Private airport reception, highway transit to Pattaya", "Overnight Stay: Pattaya (Premium Accessible Sea-View Resort)", "Meals Included: Mild Welcome Dinner"]),
            _day(2, "Nong Nooch Botanical Gardens", "Electric cart tour of Nong Nooch gardens. Traditional Thai cultural show. Relaxed Pattaya beach stroll.", ["Sightseeing Included: Nong Nooch entry, electric cart tour, cultural show", "Overnight Stay: Pattaya (Premium Accessible Sea-View Resort)", "Meals Included: International Buffet Breakfast & Garden Buffet Lunch"]),
            _day(3, "Pattaya to Bangkok Cultural Transit", "Wat Traimit Golden Buddha and Wat Pho with accessible pathways. Check into riverside hotel.", ["Sightseeing Included: Wat Traimit, Wat Pho, city driving tour", "Overnight Stay: Bangkok (Ultra-Luxury Accessible Riverside Hotel)", "Meals Included: International Buffet Breakfast & Indian Comfort Lunch"]),
            _day(4, "Damnoen Saduak Floating Market", "Private slow canal boat through floating market channels. Afternoon rest at hotel.", ["Sightseeing Included: Damnoen Saduak entry, private padded canal boat", "Overnight Stay: Bangkok (Ultra-Luxury Accessible Riverside Hotel)", "Meals Included: International Buffet Breakfast & Thai-Indian Fusion Lunch"]),
            _day(5, "ICONSIAM & Chao Phraya Dinner Cruise", "ICONSIAM accessible shopping. Grand Pearl 5-star dinner cruise with priority boarding.", ["Sightseeing Included: ICONSIAM, Grand Pearl River Cruise", "Evening Experience: 5-star river dinner cruise with live music", "Overnight Stay: Bangkok (Ultra-Luxury Accessible Riverside Hotel)", "Meals Included: International Buffet Breakfast & Grand Cruise Dinner"]),
            _day(6, "Bangkok Departure", "Final breakfast. Comfortable private transfer to Suvarnabhumi International Airport.", ["Sightseeing Included: Private airport departure transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Novotel Pattaya / similar", location="Pattaya", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="The Sukosol Bangkok / similar", location="Bangkok", nights_label="03 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="Amari Pattaya", location="Pattaya", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=4, sort_order=3),
            ItineraryHotelNested(name="Grande Centre Point Terminal 21", location="Bangkok", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=4, sort_order=4),
            ItineraryHotelNested(name="Hilton Pattaya", location="Pattaya", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="Avani+ Riverside Bangkok", location="Bangkok", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="Grande Centre Point Space Pattaya", location="Pattaya", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="Shangri-La Bangkok / Mandarin Oriental", location="Bangkok", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=8),
        ],
        inclusions=_th011_inclusions(),
    )
    return package, itinerary


def _th011_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="05 Nights in senior-friendly accessible hotels across Pattaya and Bangkok", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Low step-in private luxury van for all transfers", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Nong Nooch Gardens with electric cart and Damnoen Saduak canal boat", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Priority Chao Phraya dinner cruise boarding", sort_order=4),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 senior care concierge assistance", sort_order=5),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Thailand visa fees", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses and optional spa treatments", sort_order=7),
    ]


def build_th_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="th-012-luxury-phuket-retreat",
        destination_id=destination_id, title="Luxury Phuket Retreat",
        duration_label="06 Nights / 07 Days", price=0, rating=Decimal("4.9"),
        is_featured=True, featured_sort_order=71, is_published=True,
        highlights=[
            PackageHighlightNested(text="Phuket (6N) ultra-luxury bespoke island retreat", sort_order=1),
            PackageHighlightNested(text="Private yacht Phi Phi & James Bond Island speed-craft", sort_order=2),
            PackageHighlightNested(text="150-min spa, Michelin dining & beach candlelight finale", sort_order=3),
            PackageHighlightNested(text="Tour code TRG-HKT-LUX-2026 | Serial TH-012", sort_order=4),
        ], moods=["Luxury", "Romantic", "Family", "Beach", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="th-012-luxury-phuket-retreat-itinerary", destination_id=destination_id,
        title="Luxury Phuket Retreat", duration_label="06 Nights / 07 Days", duration_days=7,
        starting_price=0, price_note="On Request (Ultra-Luxury Retreat)", rating=Decimal("4.9"), review_count=0,
        tagline="Phuket Island • Phi Phi Islands • Phang Nga Bay",
        overview="Luxury Phuket Retreat — VIP fast-track arrival, private yacht Phi Phi charter, James Bond Island, 150-min spa, Michelin dining, and private beach candlelight finale.",
        seo_title="TH-012 | Luxury Phuket Retreat | TRAGUIN",
        seo_description="Ultra-luxury 06N/07D Phuket retreat (TH-012): private yacht, James Bond Island, Michelin dining, and beach candlelight dinner.",
        is_featured=True, featured_sort_order=71, is_published=True,
        highlights=[ItineraryHighlightNested(text="Private Yacht Phi Phi Charter", sort_order=1), ItineraryHighlightNested(text="James Bond Island & Sea Cave Canoeing", sort_order=2), ItineraryHighlightNested(text="Michelin Star Gastronomy Dinner", sort_order=3), ItineraryHighlightNested(text="Private Beach Candlelight Finale", sort_order=4)],
        days=[
            _day(1, "Phuket Arrival & Private Villa Indulgence", "VIP fast-track at Phuket Airport. Transfer to ultra-luxury pool villa with champagne welcome. Private chef poolside dinner.", ["Sightseeing Included: VIP fast-track arrival, private resort transfer", "Evening Experience: Bespoke 4-course private villa welcome dinner", "Overnight Stay: Phuket (Ultra-Luxury Ocean-View Pool Villa)", "Meals Included: Bespoke Private Villa Welcome Dinner"]),
            _day(2, "Private Luxury Yacht to Phi Phi Islands", "Full-day private yacht charter to Maya Bay, Pileh Lagoon, Bamboo Island, and Viking Cave with onboard gourmet lunch.", ["Sightseeing Included: Private yacht Phi Phi charter", "Overnight Stay: Phuket (Ultra-Luxury Ocean-View Pool Villa)", "Meals Included: International Buffet Breakfast & Onboard Yacht Gourmet Lunch"]),
            _day(3, "Heritage & Ultra-Wellness Immersion", "Floating breakfast. Old Phuket Town heritage walk. 150-minute rejuvenation spa package. Cliffside sunset cocktails.", ["Sightseeing Included: Old Phuket Town, Wat Chalong, Karon Viewpoint", "Overnight Stay: Phuket (Ultra-Luxury Ocean-View Pool Villa)", "Meals Included: Premium Floating Breakfast & Contemporary Thai Dinner"]),
            _day(4, "Phang Nga Bay Sea Cave Canoeing", "Private speed-craft to James Bond Island. Koh Hong sea cave canoeing and Koh Panyee floating village.", ["Sightseeing Included: James Bond Island, Koh Hong canoeing, Koh Panyee", "Overnight Stay: Phuket (Ultra-Luxury Ocean-View Pool Villa)", "Meals Included: International Buffet Breakfast & Koh Panyee Seafood Lunch"]),
            _day(5, "Leisure & Michelin Dining Experience", "Resort leisure day. Evening Michelin-starred or top-rated contemporary tasting menu dinner.", ["Evening Experience: Bespoke Michelin tasting menu dining", "Overnight Stay: Phuket (Ultra-Luxury Ocean-View Pool Villa)", "Meals Included: International Buffet Breakfast & Michelin Star Gastronomy Dinner"]),
            _day(6, "Boutique Shopping & Candlelight Finale", "Central Phuket Floresta luxury shopping. Signature private beachfront candlelight grand finale dinner.", ["Sightseeing Included: Central Phuket Floresta", "Evening Experience: Grand finale private beachfront candlelight dinner", "Overnight Stay: Phuket (Ultra-Luxury Ocean-View Pool Villa)", "Meals Included: International Buffet Breakfast & 5-Course Beachside Dinner"]),
            _day(7, "Phuket Departure", "Final breakfast at villa veranda. Private transfer to Phuket International Airport with premium lounge assistance.", ["Sightseeing Included: Private airport transfer, premium lounge entry", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Pullman Phuket Arcadia Naithon Beach / similar", location="Phuket", nights_label="06 Nights", category_label="Deluxe Luxury", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="The Westin Siray Bay Resort & Spa", location="Phuket", nights_label="06 Nights", category_label="Premium Luxury", meal_plan="Breakfast", stars=5, sort_order=2),
            ItineraryHotelNested(name="The Shore at Katathani", location="Phuket", nights_label="06 Nights", category_label="Elite Luxury", meal_plan="Breakfast", stars=5, sort_order=3),
            ItineraryHotelNested(name="Trisara Phuket / Sri Panwa", location="Phuket", nights_label="06 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=4),
        ],
        inclusions=_th012_inclusions(),
    )
    return package, itinerary


def _th012_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="06 Nights in ultra-luxury ocean pool villas in Phuket", sort_order=1),
        ItineraryInclusionNested(kind="included", text="VIP fast-track airport reception and customs clearance", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Private luxury yacht charter to Phi Phi Islands with gourmet lunch", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Private speed-craft James Bond Island tour with sea canoeing", sort_order=4),
        ItineraryInclusionNested(kind="included", text="150-minute premium rejuvenating massage and Michelin dining experience", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Private beachfront candlelight grand finale dinner", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated luxury concierge support", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Thailand visa fees", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="National park fees and personal expenses", sort_order=9),
    ]


TH_BUILDERS = [
    build_th_001, build_th_002, build_th_003, build_th_004, build_th_005,
    build_th_006, build_th_007, build_th_008, build_th_009, build_th_011, build_th_012,
]
