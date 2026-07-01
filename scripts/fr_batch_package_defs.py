"""Builder functions for FR-001 through FR-003 France packages (no images)."""

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


def build_fr_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="fr-001-paris-highlights-family-tour",
        destination_id=destination_id,
        title="Paris Highlights Family Tour",
        duration_label="04 Nights / 05 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=37,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Paris (4N) classic family heritage expedition", sort_order=1),
            PackageHighlightNested(text="Eiffel Tower, Louvre Museum & Seine River cruise", sort_order=2),
            PackageHighlightNested(text="Palace of Versailles royal apartments & gardens", sort_order=3),
            PackageHighlightNested(text="Montmartre, Sacré-Cœur & French cuisine experiences", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-PAR-HIGHLIGHTS-2026 | Serial FR-001", sort_order=6),
        ],
        moods=["Family", "Luxury", "Cultural"],
    )
    itinerary = ItineraryCreate(
        slug="fr-001-paris-highlights-itinerary",
        destination_id=destination_id,
        title="Paris Highlights Family Tour",
        duration_label="04 Nights / 05 Days",
        duration_days=5,
        starting_price=0,
        price_note="On Request (Premium Paris Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Eiffel Tower • Louvre • Seine Cruise • Montmartre • Versailles",
        overview=(
            "Discover the dazzling charm and historic grandeur of the City of Light with TRAGUIN's curated family "
            "itinerary. Designed for excitement and comfort, this Paris Family Highlights package offers a flawless "
            "blend of monumental exploration, artistic discovery, and leisurely strolls through charming quarters. "
            "Experience the best of French hospitality with handpicked hotels and exclusive services."
        ),
        seo_title="FR-001 | Paris Highlights Family Tour | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Paris family package (FR-001): Eiffel Tower, Louvre, Seine River cruise, "
            "Versailles, and Montmartre."
        ),
        is_featured=True,
        featured_sort_order=37,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Seine River Night Cruise", sort_order=1),
            ItineraryHighlightNested(text="Eiffel Tower & Louvre Museum", sort_order=2),
            ItineraryHighlightNested(text="Palace of Versailles", sort_order=3),
            ItineraryHighlightNested(text="Montmartre & Sacré-Cœur Basilica", sort_order=4),
        ],
        days=[
            _day(1, "Arrival in Paris & Seine River Cruise", "Arrive in elegant Paris. Your private TRAGUIN transfer will escort you to your handpicked hotel. Enjoy a relaxing evening with a scenic Seine River cruise, admiring the city's stunning landmarks illuminated at night.", ["Sightseeing Included: VIP airport reception, Seine River night cruise", "Overnight Stay: Paris (Ultra Luxury Hotel)", "Meals Included: Welcome arrangements on arrival"]),
            _day(2, "Eiffel Tower & Louvre Discovery", "Explore the iconic attractions of Paris. Visit the Eiffel Tower and the Louvre Museum. This curated experience offers deep insights into Paris's history, culture, and iconic attractions.", ["Sightseeing Included: Eiffel Tower visit, Louvre Museum guided tour", "Overnight Stay: Paris (Ultra Luxury Hotel)", "Meals Included: Breakfast"]),
            _day(3, "Palace of Versailles", "Embark on a grand excursion to the Palace of Versailles. Explore the breathtaking state apartments, Hall of Mirrors, and the magnificent royal gardens.", ["Sightseeing Included: Palace of Versailles, Hall of Mirrors, royal gardens", "Overnight Stay: Paris (Ultra Luxury Hotel)", "Meals Included: Breakfast"]),
            _day(4, "Montmartre & Artistic Charm", "A full day of immersive fun exploring the artistic streets of Montmartre. Visit the Sacré-Cœur Basilica, enjoy local art, and taste French cuisine.", ["Sightseeing Included: Montmartre walking tour, Sacré-Cœur Basilica", "Overnight Stay: Paris (Ultra Luxury Hotel)", "Meals Included: Breakfast"]),
            _day(5, "Departure", "Enjoy a final family breakfast. Your private TRAGUIN chauffeur ensures a comfortable transfer to the airport, completing your premium Paris experience.", ["Sightseeing Included: Private airport transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Le Meurice / The Peninsula Paris", location="Paris", nights_label="04 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=1),
        ],
        inclusions=_fr001_inclusions(),
    )
    return package, itinerary


def _fr001_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="04 Nights in handpicked ultra-luxury family hotel in Paris", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private executive chauffeur-driven luxury ground transfers", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Seine River night cruise on arrival evening", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Eiffel Tower and Louvre Museum guided sightseeing", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Palace of Versailles excursion with royal gardens access", sort_order=5),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated on-ground family concierge support", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="International airfare and France entry visa processing fees", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=10),
    ]


def build_fr_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="fr-002-romantic-paris-honeymoon",
        destination_id=destination_id,
        title="Romantic Paris Honeymoon",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=38,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Paris (5N) romantic honeymoon sanctuary", sort_order=1),
            PackageHighlightNested(text="Private Seine River dinner cruise with Eiffel Tower views", sort_order=2),
            PackageHighlightNested(text="Eiffel Tower skip-the-line & Montmartre artistic walk", sort_order=3),
            PackageHighlightNested(text="Versailles, Louvre & Champs-Élysées luxury shopping", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 honeymoon concierge desk support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-PAR-ROMANCE-2026 | Serial FR-002", sort_order=6),
        ],
        moods=["Romantic", "Luxury", "Cultural"],
    )
    itinerary = ItineraryCreate(
        slug="fr-002-romantic-paris-itinerary",
        destination_id=destination_id,
        title="Romantic Paris Honeymoon",
        duration_label="05 Nights / 06 Days",
        duration_days=6,
        starting_price=0,
        price_note="On Request (Premium Honeymoon Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Eiffel Tower • Seine Cruise • Montmartre • Versailles • Luxury Dining",
        overview=(
            "Begin your lifelong love story in the most poetic city in the world. TRAGUIN's curated Paris honeymoon "
            "retreat offers an unparalleled blend of classic French romance, world-class culinary experiences, and "
            "iconic landmark exploration. Designed for absolute comfort and privacy, this Romantic Paris journey "
            "guarantees unforgettable memories in the heart of the City of Light."
        ),
        seo_title="FR-002 | Romantic Paris Honeymoon | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days Paris honeymoon package (FR-002): Seine dinner cruise, Eiffel Tower, "
            "Versailles, Louvre, Montmartre, and candlelight farewell dinner."
        ),
        is_featured=True,
        featured_sort_order=38,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Private Seine River Dinner Cruise", sort_order=1),
            ItineraryHighlightNested(text="Eiffel Tower Skip-the-Line Access", sort_order=2),
            ItineraryHighlightNested(text="Palace of Versailles Private Excursion", sort_order=3),
            ItineraryHighlightNested(text="Louvre Museum & Champs-Élysées", sort_order=4),
            ItineraryHighlightNested(text="Candlelight Farewell Dinner", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Paris & Seine River Dinner Cruise", "Arrive in Paris, the City of Light. Your private transfer will escort you to your ultra-luxury hotel. Celebrate your first evening with a private dinner cruise on the Seine River, viewing iconic landmarks like the Eiffel Tower illuminated.", ["Sightseeing Included: VIP airport reception, private Seine dinner cruise", "Evening Experience: Private dinner cruise with Eiffel Tower views", "Overnight Stay: Paris (Ultra Luxury Hotel)", "Meals Included: Welcome Dinner"]),
            _day(2, "Eiffel Tower & Artistic Montmartre", "Visit the iconic Eiffel Tower with skip-the-line access. Later, explore the charming artistic district of Montmartre, visit the Sacré-Cœur Basilica, and enjoy a private artistic walking tour through its quaint streets.", ["Sightseeing Included: Eiffel Tower skip-the-line, Montmartre private walking tour, Sacré-Cœur Basilica", "Overnight Stay: Paris (Ultra Luxury Hotel)", "Meals Included: Breakfast"]),
            _day(3, "Palace of Versailles", "A private excursion to the majestic Palace of Versailles. Explore the royal apartments and stroll through the expansive, beautiful royal gardens in style.", ["Sightseeing Included: Private Palace of Versailles excursion, royal gardens", "Overnight Stay: Paris (Ultra Luxury Hotel)", "Meals Included: Breakfast"]),
            _day(4, "Louvre Museum & Shopping", "Discover artistic treasures at the Louvre Museum. Spend your afternoon enjoying leisurely luxury shopping along the Champs-Élysées.", ["Sightseeing Included: Louvre Museum guided visit, Champs-Élysées leisure time", "Overnight Stay: Paris (Ultra Luxury Hotel)", "Meals Included: Breakfast"]),
            _day(5, "Leisure & Romantic Dinner", "Spend a relaxing day exploring local cafes, visiting charming patisseries, and enjoying a farewell candlelight dinner in a romantic garden restaurant.", ["Evening Experience: Candlelight farewell dinner in garden restaurant", "Overnight Stay: Paris (Ultra Luxury Hotel)", "Meals Included: Breakfast & Farewell Dinner"]),
            _day(6, "Departure", "Enjoy a final French breakfast before your TRAGUIN private transfer, completing your romantic Paris honeymoon.", ["Sightseeing Included: Private airport transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="The Ritz Paris / Shangri-La Paris", location="Paris", nights_label="05 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=1),
        ],
        inclusions=_fr002_inclusions(),
    )
    return package, itinerary


def _fr002_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="05 Nights in handpicked ultra-luxury honeymoon hotel in Paris", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private chauffeur-driven luxury ground transfers throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Private Seine River dinner cruise on arrival evening", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Eiffel Tower skip-the-line access and Louvre Museum visit", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Private Palace of Versailles excursion with royal gardens", sort_order=5),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated honeymoon concierge support", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="International airfare and France entry visa processing fees", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=10),
    ]


def build_fr_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="fr-003-luxury-france-tour",
        destination_id=destination_id,
        title="Luxury France Tour",
        duration_label="06 Nights / 07 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=39,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Paris (3N) → French Riviera (3N) ultra-luxury circuit", sort_order=1),
            PackageHighlightNested(text="Louvre private tour & gourmet French cooking class", sort_order=2),
            PackageHighlightNested(text="Versailles & Golden Triangle high-end shopping", sort_order=3),
            PackageHighlightNested(text="Monaco, Monte Carlo & Provence lavender fields", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 luxury travel concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-FRA-LUX-2026 | Serial FR-003", sort_order=6),
        ],
        moods=["Luxury", "Family", "Cultural", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="fr-003-luxury-france-itinerary",
        destination_id=destination_id,
        title="Luxury France Tour",
        duration_label="06 Nights / 07 Days",
        duration_days=7,
        starting_price=0,
        price_note="On Request (Ultra-Luxury France Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Paris • Versailles • French Riviera • Monaco • Provence",
        overview=(
            "Discover the height of sophistication and style with TRAGUIN's curated luxury French expedition. "
            "From the iconic streets of Paris to the shimmering azure coast of the French Riviera, experience an "
            "unmatched journey of culture, gastronomy, and breathtaking beauty across Paris, Nice, Monaco, and Provence."
        ),
        seo_title="FR-003 | Luxury France Tour | TRAGUIN",
        seo_description=(
            "Ultra-luxury 06 Nights / 07 Days France package (FR-003): Paris, Versailles, French Riviera, Monaco, "
            "Monte Carlo, and Provence lavender fields."
        ),
        is_featured=True,
        featured_sort_order=39,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Private Seine Champagne Sunset Cruise", sort_order=1),
            ItineraryHighlightNested(text="Louvre Private Tour & French Cooking Class", sort_order=2),
            ItineraryHighlightNested(text="Palace of Versailles & Golden Triangle Shopping", sort_order=3),
            ItineraryHighlightNested(text="Monaco & Monte Carlo Elite Day Trip", sort_order=4),
            ItineraryHighlightNested(text="Provence Lavender Fields & Côte d'Azur Drive", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Paris & Seine Cruise", "Arrive in elegant Paris. Private transfer to your ultra-luxury hotel. Enjoy a private Seine River cruise with champagne at sunset.", ["Sightseeing Included: VIP airport reception, private Seine champagne sunset cruise", "Overnight Stay: Paris (Four Seasons George V / Ritz Paris)", "Meals Included: Welcome arrangements on arrival"]),
            _day(2, "Paris Art & Gastronomy", "Exclusive private tour of the Louvre followed by a gourmet French cooking class in a historic Parisian kitchen.", ["Sightseeing Included: Private Louvre tour, gourmet French cooking class", "Overnight Stay: Paris (Four Seasons George V / Ritz Paris)", "Meals Included: Breakfast"]),
            _day(3, "Palace of Versailles & Shopping", "Private excursion to Versailles. Afternoon dedicated to high-end shopping in the legendary boutiques of the Golden Triangle.", ["Sightseeing Included: Private Versailles excursion, Golden Triangle shopping", "Overnight Stay: Paris (Four Seasons George V / Ritz Paris)", "Meals Included: Breakfast"]),
            _day(4, "Fly to French Riviera", "Private flight to Nice. Check into a world-class seaside resort. Enjoy the vibrant colors and lifestyle of the French Riviera.", ["Sightseeing Included: Private flight to Nice, French Riviera resort check-in", "Overnight Stay: French Riviera (Grand-Hôtel du Cap-Ferrat)", "Meals Included: Breakfast"]),
            _day(5, "Monaco & Monte Carlo", "Day trip to Monaco and Monte Carlo. Explore the prince's palace and the famous casino, enjoying the exclusive experiences of the elite coast.", ["Sightseeing Included: Monaco & Monte Carlo day trip, Prince's Palace, famous casino", "Overnight Stay: French Riviera (Grand-Hôtel du Cap-Ferrat)", "Meals Included: Breakfast"]),
            _day(6, "Provence Lavender & Côte d'Azur", "Visit the lavender fields of Provence followed by a coastal drive along the stunning Côte d'Azur.", ["Sightseeing Included: Provence lavender fields, Côte d'Azur coastal drive", "Overnight Stay: French Riviera (Grand-Hôtel du Cap-Ferrat)", "Meals Included: Breakfast"]),
            _day(7, "Departure", "Final luxury breakfast. Private transfer to Nice airport for departure, completing your premium France experience.", ["Sightseeing Included: Private transfer to Nice airport", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Four Seasons George V / Ritz Paris", location="Paris", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Grand-Hôtel du Cap-Ferrat", location="French Riviera (Nice)", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=2),
        ],
        inclusions=_fr003_inclusions(),
    )
    return package, itinerary


def _fr003_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="06 Nights in ultra-luxury hotels across Paris and the French Riviera", sort_order=1),
        ItineraryInclusionNested(kind="included", text="VIP chauffeur-driven luxury ground transfers throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Private Seine champagne sunset cruise in Paris", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Private Louvre tour and gourmet French cooking class", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Private flight coordination from Paris to Nice", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Monaco & Monte Carlo day trip and Provence lavender excursion", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated luxury travel concierge support", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="International airfare and France entry visa processing fees", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=11),
    ]


FR_BUILDERS = [
    build_fr_001,
    build_fr_002,
    build_fr_003,
]
