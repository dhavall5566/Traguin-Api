"""Builder functions for CH-001 through CH-003 Switzerland packages (no images)."""

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


def build_ch_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="ch-001-swiss-highlights-family-tour",
        destination_id=destination_id,
        title="Swiss Highlights Family Tour",
        duration_label="06 Nights / 07 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=34,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Zurich (1N) → Lucerne (2N) → Interlaken (3N) family circuit", sort_order=1),
            PackageHighlightNested(text="Chapel Bridge, lake cruise & Mt. Titlis snow adventure", sort_order=2),
            PackageHighlightNested(text="Jungfraujoch — Top of Europe excursion", sort_order=3),
            PackageHighlightNested(text="Scenic Swiss Alps rail journeys & alpine leisure", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-SWI-HIG-2026 | Serial CH-001", sort_order=6),
        ],
        moods=["Family", "Luxury", "Nature", "Adventure"],
    )
    itinerary = ItineraryCreate(
        slug="ch-001-swiss-highlights-itinerary",
        destination_id=destination_id,
        title="Swiss Highlights Family Tour",
        duration_label="06 Nights / 07 Days",
        duration_days=7,
        starting_price=0,
        price_note="On Request (Premium Switzerland Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Zurich • Lucerne • Mt. Titlis • Interlaken • Swiss Alps",
        overview=(
            "Discover the breathtaking beauty of the Swiss Alps with TRAGUIN's curated family expedition. "
            "This comprehensive journey takes your family through pristine lakes, majestic peaks, and scenic rail "
            "journeys across Zurich, Lucerne, and Interlaken — ensuring unforgettable memories in Switzerland's "
            "most stunning landscapes. Includes private executive transfers, handpicked premium family stays, and "
            "24/7 on-ground concierge support. Best season: May to September."
        ),
        seo_title="CH-001 | Swiss Highlights Family Tour | TRAGUIN",
        seo_description=(
            "Premium 06 Nights / 07 Days Switzerland family package (CH-001): Zurich, Lucerne, Mt. Titlis, "
            "Jungfraujoch, and Interlaken with scenic rail journeys."
        ),
        is_featured=True,
        featured_sort_order=34,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Chapel Bridge & Lucerne Lake Cruise", sort_order=1),
            ItineraryHighlightNested(text="Mt. Titlis Cable Car & Snow Activities", sort_order=2),
            ItineraryHighlightNested(text="Jungfraujoch — Top of Europe", sort_order=3),
            ItineraryHighlightNested(text="Interlaken Alpine Leisure", sort_order=4),
            ItineraryHighlightNested(text="Scenic Swiss Rail Journeys", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Zurich", "Arrive in Zurich. Private transfer to your handpicked premium hotel. Evening at leisure to enjoy the city's sophisticated charm.", ["Sightseeing Included: VIP airport reception, private hotel transfer", "Overnight Stay: Zurich (Luxury City Hotel)", "Meals Included: Welcome arrangements on arrival"]),
            _day(2, "Transfer to Lucerne", "Scenic transfer to Lucerne. Visit the iconic Chapel Bridge and take a peaceful lake cruise — a classic Swiss experience.", ["Sightseeing Included: Chapel Bridge walk, Lucerne lake cruise", "Overnight Stay: Lucerne (Premium Lake View Hotel)", "Meals Included: Breakfast"]),
            _day(3, "Mt. Titlis Adventure", "Ascend to Mt. Titlis by cable car. Enjoy snow activities at the summit, creating unforgettable memories for your family.", ["Sightseeing Included: Mt. Titlis cable car ascent, summit snow activities", "Overnight Stay: Lucerne (Premium Lake View Hotel)", "Meals Included: Breakfast"]),
            _day(4, "Transfer to Interlaken", "Transfer to Interlaken, the adventure heart of Switzerland. Check into your luxury alpine retreat.", ["Sightseeing Included: Scenic transfer to Interlaken", "Overnight Stay: Interlaken (Luxury Alpine Retreat)", "Meals Included: Breakfast"]),
            _day(5, "Jungfraujoch Excursion", "A spectacular journey to Jungfraujoch — the Top of Europe. Experience breathtaking panoramic views and high-altitude excitement.", ["Sightseeing Included: Jungfraujoch Top of Europe excursion", "Overnight Stay: Interlaken (Luxury Alpine Retreat)", "Meals Included: Breakfast"]),
            _day(6, "Alpine Leisure & Exploration", "A day of leisure or gentle exploration in the scenic surroundings — perfect for family bonding in the Swiss Alps.", ["Sightseeing Included: Leisure day in Interlaken region", "Overnight Stay: Interlaken (Luxury Alpine Retreat)", "Meals Included: Breakfast"]),
            _day(7, "Departure", "Final luxury breakfast before your TRAGUIN private transfer to the airport, completing your premium Swiss highlights expedition.", ["Sightseeing Included: Private airport transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Luxury City Hotel / similar", location="Zurich", nights_label="01 Night", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Premium Lake View Hotel / similar", location="Lucerne", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=2),
            ItineraryHotelNested(name="Luxury Alpine Retreat / similar", location="Interlaken", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=3),
        ],
        inclusions=_ch001_inclusions(),
    )
    return package, itinerary


def _ch001_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="06 Nights in handpicked premium family hotels across Zurich, Lucerne, and Interlaken", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private executive chauffeur-driven luxury ground transfers", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Mt. Titlis cable car ascent with summit snow activities", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Jungfraujoch — Top of Europe excursion", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Lucerne lake cruise and Chapel Bridge sightseeing", sort_order=5),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated on-ground family concierge support", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Switzerland entry visa processing fees", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=10),
    ]


def build_ch_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="ch-002-romantic-switzerland-honeymoon",
        destination_id=destination_id,
        title="Romantic Switzerland Honeymoon",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=35,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Lucerne (2N) → Interlaken (3N) → Zermatt (2N) romantic circuit", sort_order=1),
            PackageHighlightNested(text="Mt. Pilatus sunset excursion with alpine panorama", sort_order=2),
            PackageHighlightNested(text="Jungfraujoch private photo session at Top of Europe", sort_order=3),
            PackageHighlightNested(text="Lake Brienz boat excursion & Matterhorn-view Zermatt stay", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 honeymoon concierge desk support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-SWI-ROM-2026 | Serial CH-002", sort_order=6),
        ],
        moods=["Romantic", "Luxury", "Nature", "Adventure"],
    )
    itinerary = ItineraryCreate(
        slug="ch-002-romantic-switzerland-itinerary",
        destination_id=destination_id,
        title="Romantic Switzerland Honeymoon",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="On Request (Premium Honeymoon Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Lucerne • Mt. Pilatus • Interlaken • Zermatt • Matterhorn",
        overview=(
            "Begin your life together in one of the world's most breathtaking landscapes. This TRAGUIN curated Swiss "
            "honeymoon sanctuary is designed for intimacy, luxury, and awe-inspiring beauty — perfectly balancing cozy "
            "alpine retreats, scenic romantic excursions, and world-class hospitality across Lucerne, Interlaken, "
            "and Zermatt. Includes private chauffeur transfers, lakeside suites, and 24/7 honeymoon concierge support."
        ),
        seo_title="CH-002 | Romantic Switzerland Honeymoon | TRAGUIN",
        seo_description=(
            "Premium 07 Nights / 08 Days Switzerland honeymoon package (CH-002): Lucerne, Mt. Pilatus, Jungfraujoch, "
            "Lake Brienz, and Zermatt with Matterhorn views."
        ),
        is_featured=True,
        featured_sort_order=35,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Lakeside Welcome in Lucerne", sort_order=1),
            ItineraryHighlightNested(text="Mt. Pilatus Sunset Experience", sort_order=2),
            ItineraryHighlightNested(text="Jungfraujoch Top of Europe Romance", sort_order=3),
            ItineraryHighlightNested(text="Private Lake Brienz Boat Excursion", sort_order=4),
            ItineraryHighlightNested(text="Matterhorn-View Zermatt Celebration", sort_order=5),
        ],
        days=[
            _day(1, "Arrival & Intimate Lucerne Welcome", "Arrive in Zurich and private chauffeur transfer to Lucerne. Check into your romantic lakeside suite. Evening lakeside walk and intimate welcome dinner.", ["Sightseeing Included: VIP airport reception, lakeside orientation walk", "Evening Experience: Intimate welcome dinner", "Overnight Stay: Lucerne (Luxury Lakeside Suites)", "Meals Included: Welcome Dinner"]),
            _day(2, "Mt. Pilatus Sunset Experience", "A gentle day in Lucerne, followed by a sunset excursion to Mt. Pilatus. Witness the spectacular alpine panorama — an exclusive romantic experience.", ["Sightseeing Included: Mt. Pilatus sunset excursion", "Overnight Stay: Lucerne (Luxury Lakeside Suites)", "Meals Included: Breakfast"]),
            _day(3, "Transfer to Interlaken", "Scenic train transfer to Interlaken. Check into your luxury alpine retreat with mountain views, perfect for couples.", ["Sightseeing Included: Scenic rail transfer to Interlaken", "Overnight Stay: Interlaken (Ultra-Luxury Alpine Resort)", "Meals Included: Breakfast"]),
            _day(4, "Jungfraujoch Romance", "A spectacular journey to the Top of Europe. Enjoy a private photo session amidst the pristine snow — creating unforgettable memories.", ["Sightseeing Included: Jungfraujoch Top of Europe excursion, private photo session", "Overnight Stay: Interlaken (Ultra-Luxury Alpine Resort)", "Meals Included: Breakfast"]),
            _day(5, "Alpine Lakes & Leisure", "Leisure day in Interlaken. Enjoy a private boat excursion on Lake Brienz, soaking in the serene mountain beauty together.", ["Sightseeing Included: Private Lake Brienz boat excursion", "Overnight Stay: Interlaken (Ultra-Luxury Alpine Resort)", "Meals Included: Breakfast"]),
            _day(6, "Zermatt Luxury Escape", "Transfer to Zermatt. Check into your ultra-luxury boutique suite with iconic Matterhorn views.", ["Sightseeing Included: Scenic transfer to Zermatt", "Overnight Stay: Zermatt (Luxury Matterhorn-View Suites)", "Meals Included: Breakfast"]),
            _day(7, "Matterhorn Celebration", "Enjoy a day of private leisure and spa treatments in Zermatt, followed by a candlelit farewell dinner celebrating your romantic honeymoon.", ["Evening Experience: Candlelit farewell dinner", "Overnight Stay: Zermatt (Luxury Matterhorn-View Suites)", "Meals Included: Breakfast & Farewell Dinner"]),
            _day(8, "Departure", "Final luxury breakfast before your TRAGUIN private chauffeur transfer to the airport, completing your premium Swiss honeymoon.", ["Sightseeing Included: Private airport transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Luxury Lakeside Suites / similar", location="Lucerne", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Ultra-Luxury Alpine Resort / similar", location="Interlaken", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=2),
            ItineraryHotelNested(name="Luxury Matterhorn-View Suites / similar", location="Zermatt", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=3),
        ],
        inclusions=_ch002_inclusions(),
    )
    return package, itinerary


def _ch002_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="07 Nights in handpicked romantic hotels across Lucerne, Interlaken, and Zermatt", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private chauffeur-driven luxury ground transfers throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Scenic Swiss rail transfer to Interlaken", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Mt. Pilatus sunset excursion and Jungfraujoch Top of Europe visit", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Private Lake Brienz boat excursion for couples", sort_order=5),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated honeymoon concierge support", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Switzerland entry visa processing fees", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=10),
    ]


def build_ch_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="ch-003-luxury-switzerland-tour",
        destination_id=destination_id,
        title="Luxury Switzerland Tour",
        duration_label="08 Nights / 09 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=36,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Zurich (2N) → Lucerne (2N) → Interlaken (3N) → Zermatt (2N) ultra-luxury circuit", sort_order=1),
            PackageHighlightNested(text="VIP Zurich discovery & exclusive Mt. Titlis summit access", sort_order=2),
            PackageHighlightNested(text="Luxury scenic rail journey & Jungfraujoch VIP expedition", sort_order=3),
            PackageHighlightNested(text="Matterhorn elite experience & farewell gala dinner", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 luxury travel concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-SWI-LUX-2026 | Serial CH-003", sort_order=6),
        ],
        moods=["Luxury", "Family", "Nature", "Adventure"],
    )
    itinerary = ItineraryCreate(
        slug="ch-003-luxury-switzerland-itinerary",
        destination_id=destination_id,
        title="Luxury Switzerland Tour",
        duration_label="08 Nights / 09 Days",
        duration_days=9,
        starting_price=0,
        price_note="On Request (Ultra-Luxury Switzerland Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Zurich • Lucerne • Interlaken • Zermatt • Exclusive Rail Journeys",
        overview=(
            "Indulge in the absolute height of sophistication across Switzerland with TRAGUIN's curated luxury expedition. "
            "From opulent five-star stays and world-class alpine resorts to exclusive private rail journeys and elite "
            "culinary experiences, this journey is designed for the discerning traveler — ensuring unforgettable "
            "memories in ultimate luxury across Zurich, Lucerne, Interlaken, and Zermatt."
        ),
        seo_title="CH-003 | Luxury Switzerland Tour | TRAGUIN",
        seo_description=(
            "Ultra-luxury 08 Nights / 09 Days Switzerland package (CH-003): Baur au Lac, Bürgenstock, Victoria-Jungfrau, "
            "The Omnia, Mt. Titlis, Jungfraujoch, and Matterhorn experiences."
        ),
        is_featured=True,
        featured_sort_order=36,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="VIP Zurich Discovery & Gourmet Welcome", sort_order=1),
            ItineraryHighlightNested(text="Mt. Titlis Exclusive Summit Access", sort_order=2),
            ItineraryHighlightNested(text="Luxury Scenic Rail to Interlaken", sort_order=3),
            ItineraryHighlightNested(text="Jungfraujoch VIP Expedition", sort_order=4),
            ItineraryHighlightNested(text="Matterhorn Elite Experience & Gala Dinner", sort_order=5),
        ],
        days=[
            _day(1, "VIP Arrival & Zurich Luxury", "Arrive in Zurich. VIP chauffeur transfer to your world-class hotel. Evening gourmet welcome dinner overlooking the lake.", ["Sightseeing Included: VIP airport reception, private hotel transfer", "Evening Experience: Gourmet welcome dinner", "Overnight Stay: Zurich (Baur au Lac)", "Meals Included: Welcome Dinner"]),
            _day(2, "Exclusive Zurich Discovery", "Private guided tour of Zurich's most prestigious districts, boutique shopping, and cultural landmarks — an exclusive experience.", ["Sightseeing Included: Private guided Zurich city tour", "Overnight Stay: Zurich (Baur au Lac)", "Meals Included: Breakfast"]),
            _day(3, "Transfer to Lucerne", "VIP transfer to Lucerne. Check into a premium lakeside palace hotel. Afternoon private lake cruise with gourmet catering.", ["Sightseeing Included: Private lake cruise with gourmet catering", "Overnight Stay: Lucerne (Bürgenstock Resort)", "Meals Included: Breakfast"]),
            _day(4, "Mt. Titlis Exclusive Access", "Private cable car access to Mt. Titlis summit. Enjoy personal guiding, premium snow experiences, and gourmet dining at the top.", ["Sightseeing Included: Mt. Titlis private summit access, personal guiding", "Overnight Stay: Lucerne (Bürgenstock Resort)", "Meals Included: Breakfast"]),
            _day(5, "Scenic Rail to Interlaken", "Embark on an exclusive luxury scenic rail journey to Interlaken. Check into an ultra-luxury alpine retreat.", ["Sightseeing Included: Luxury scenic rail journey to Interlaken", "Overnight Stay: Interlaken (Victoria-Jungfrau Grand Hotel & Spa)", "Meals Included: Breakfast"]),
            _day(6, "Jungfraujoch VIP Expedition", "Private VIP expedition to Jungfraujoch — the Top of Europe. Enjoy personalized guiding and unparalleled panoramic views.", ["Sightseeing Included: Jungfraujoch VIP private expedition", "Overnight Stay: Interlaken (Victoria-Jungfrau Grand Hotel & Spa)", "Meals Included: Breakfast"]),
            _day(7, "Transfer to Zermatt", "Transfer to Zermatt. Check into an ultra-luxury boutique suite with iconic Matterhorn views.", ["Sightseeing Included: Scenic transfer to Zermatt", "Overnight Stay: Zermatt (The Omnia)", "Meals Included: Breakfast"]),
            _day(8, "Matterhorn Elite Experience", "Private leisure day in Zermatt, boutique shopping, and a farewell gala dinner celebrating your luxury Swiss expedition.", ["Evening Experience: Farewell gala dinner", "Overnight Stay: Zermatt (The Omnia)", "Meals Included: Breakfast & Gala Dinner"]),
            _day(9, "Departure", "Final luxury breakfast. VIP chauffeur transfer to the airport, concluding your premium Switzerland luxury expedition.", ["Sightseeing Included: VIP airport transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Baur au Lac", location="Zurich", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Bürgenstock Resort", location="Lucerne", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=2),
            ItineraryHotelNested(name="Victoria-Jungfrau Grand Hotel & Spa", location="Interlaken", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=3),
            ItineraryHotelNested(name="The Omnia", location="Zermatt", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=4),
        ],
        inclusions=_ch003_inclusions(),
    )
    return package, itinerary


def _ch003_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="08 Nights in ultra-luxury hotels across Zurich, Lucerne, Interlaken, and Zermatt", sort_order=1),
        ItineraryInclusionNested(kind="included", text="VIP chauffeur-driven luxury ground transfers throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Exclusive luxury scenic rail journey to Interlaken", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Mt. Titlis private summit access with personal guiding", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Jungfraujoch VIP private expedition to the Top of Europe", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Private lake cruise with gourmet catering in Lucerne", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated luxury travel concierge support", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Switzerland entry visa processing fees", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=11),
    ]


CH_BUILDERS = [
    build_ch_001,
    build_ch_002,
    build_ch_003,
]
