"""Builder functions for ID-001, ID-002, ID-005, ID-006, ID-007 Bali packages (no images)."""

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


def build_id_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="id-001-premium-bali-honeymoon",
        destination_id=destination_id,
        title="Premium Bali Honeymoon",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=40,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Ubud → Seminyak → Uluwatu romantic honeymoon circuit", sort_order=1),
            PackageHighlightNested(text="Tegalalang Rice Terraces & Sacred Monkey Forest", sort_order=2),
            PackageHighlightNested(text="Premium beach clubs, couple's spa & cafe culture", sort_order=3),
            PackageHighlightNested(text="Uluwatu Temple & Kecak Fire Dance at sunset", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 honeymoon concierge support", sort_order=5),
            PackageHighlightNested(text="Serial ID-001 | Category: Honeymoon", sort_order=6),
        ],
        moods=["Romantic", "Luxury", "Beach", "Cultural", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="id-001-premium-bali-honeymoon-itinerary",
        destination_id=destination_id,
        title="Premium Bali Honeymoon",
        duration_label="05 Nights / 06 Days",
        duration_days=6,
        starting_price=0,
        price_note="On Request (Premium Bali Honeymoon)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Ubud • Seminyak • Uluwatu",
        overview=(
            "Embark on an enchanting TRAGUIN curated Bali honeymoon designed for intimate moments, "
            "breathtaking landscapes, and premium stays. From the lush jungles of Ubud to the romantic sunsets "
            "of Uluwatu, every detail is crafted for an unforgettable romantic escape on the Island of the Gods."
        ),
        seo_title="ID-001 | Premium Bali Honeymoon | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days Bali honeymoon (ID-001): Ubud, Seminyak, Uluwatu Temple, "
            "Kecak Fire Dance, rice terraces, and Sacred Monkey Forest."
        ),
        is_featured=True,
        featured_sort_order=40,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Candlelit Welcome Dinner in Ubud", sort_order=1),
            ItineraryHighlightNested(text="Tegalalang Rice Terraces & Monkey Forest", sort_order=2),
            ItineraryHighlightNested(text="Seminyak Beach Bliss & Couple's Spa", sort_order=3),
            ItineraryHighlightNested(text="Uluwatu Temple Kecak Fire Dance", sort_order=4),
        ],
        days=[
            _day(1, "Arrival in Bali — The Romantic Beginning", "Arrive at Denpasar Airport and receive a warm TRAGUIN welcome. Transfer to your handpicked hotel in Ubud. Enjoy a candlelit dinner to start your romantic journey.", ["Sightseeing Included: VIP airport reception, private transfer to Ubud", "Evening Experience: Candlelit welcome dinner", "Overnight Stay: Ubud (Premium Handpicked Hotel)", "Meals Included: Dinner"]),
            _day(2, "Ubud — Cultural Immersion", "Visit the Tegalalang Rice Terraces and the Sacred Monkey Forest. Immerse yourselves in the culture of Bali with curated experiences in local markets.", ["Sightseeing Included: Tegalalang Rice Terraces, Sacred Monkey Forest, local markets", "Overnight Stay: Ubud (Premium Handpicked Hotel)", "Meals Included: Breakfast & Dinner"]),
            _day(3, "Ubud to Seminyak — Scenic Transfer", "Travel to Seminyak, exploring waterfalls along the way. Enjoy the scenic beauty of Bali's coast.", ["Sightseeing Included: Scenic transfer with waterfall stops", "Overnight Stay: Seminyak (Premium Handpicked Hotel)", "Meals Included: Breakfast & Dinner"]),
            _day(4, "Seminyak — Beach Bliss", "Relax at premium beach clubs or indulge in a couple's spa treatment. Enjoy the vibrant shopping and cafe culture.", ["Sightseeing Included: Beach club leisure, couple's spa treatment", "Overnight Stay: Seminyak (Premium Handpicked Hotel)", "Meals Included: Breakfast & Dinner"]),
            _day(5, "Uluwatu — Sunset Romance", "Visit the iconic Uluwatu Temple. Witness the mesmerizing Kecak Fire Dance at sunset, one of the top tourist places in Bali.", ["Sightseeing Included: Uluwatu Temple, Kecak Fire Dance at sunset", "Overnight Stay: Uluwatu / Seminyak (Premium Handpicked Hotel)", "Meals Included: Breakfast & Dinner"]),
            _day(6, "Departure", "Enjoy breakfast before your transfer to the airport. TRAGUIN ensures a seamless departure after your unforgettable memories.", ["Sightseeing Included: Private airport transfer", "Meals Included: Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Premium Handpicked Resort / similar", location="Ubud", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast & Dinner", stars=5, sort_order=1),
            ItineraryHotelNested(name="Premium Handpicked Beach Resort / similar", location="Seminyak", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast & Dinner", stars=5, sort_order=2),
            ItineraryHotelNested(name="Premium Handpicked Cliff Resort / similar", location="Uluwatu / Seminyak", nights_label="01 Night", category_label="Premium", meal_plan="Breakfast & Dinner", stars=5, sort_order=3),
        ],
        inclusions=_id001_inclusions(),
    )
    return package, itinerary


def _id001_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="05 Nights premium accommodation across Ubud, Seminyak, and Uluwatu", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Daily breakfast and romantic dinners", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Private luxury airport transfers", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Complimentary honeymoon amenities", sort_order=4),
        ItineraryInclusionNested(kind="included", text="TRAGUIN expert assistance throughout the tour", sort_order=5),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Indonesia visa on arrival fees", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=9),
    ]


def build_id_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="id-002-bali-ubud-love-escape",
        destination_id=destination_id,
        title="Bali Ubud Love Escape",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=41,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="05 Nights luxury villa stay in Ubud rainforest", sort_order=1),
            PackageHighlightNested(text="Floral bath welcome & romantic starlit dinners", sort_order=2),
            PackageHighlightNested(text="Couple's spa, cooking class & Tegenungan Waterfall", sort_order=3),
            PackageHighlightNested(text="Tegalalang Rice Terraces & Sacred Monkey Forest", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 personal assistance", sort_order=5),
            PackageHighlightNested(text="Serial ID-002 | Category: Honeymoon", sort_order=6),
        ],
        moods=["Romantic", "Luxury", "Nature", "Cultural", "Spiritual"],
    )
    itinerary = ItineraryCreate(
        slug="id-002-bali-ubud-love-escape-itinerary",
        destination_id=destination_id,
        title="Bali Ubud Love Escape",
        duration_label="05 Nights / 06 Days",
        duration_days=6,
        starting_price=0,
        price_note="On Request (Premium Ubud Honeymoon)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Ubud — The Heart of Romantic Bali",
        overview=(
            "Escape to the serene landscapes of Ubud with this TRAGUIN curated honeymoon experience. "
            "Luxury stays nestled in lush tropical jungles provide a tranquil and romantic setting for your "
            "premium Bali holiday — from private villa experiences to intimate cultural tours."
        ),
        seo_title="ID-002 | Bali Ubud Love Escape | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days Ubud honeymoon (ID-002): luxury villa, rice terraces, "
            "couple's spa, cooking class, and Tegenungan Waterfall."
        ),
        is_featured=True,
        featured_sort_order=41,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Floral Bath & Romantic Dinner Welcome", sort_order=1),
            ItineraryHighlightNested(text="Tegalalang Rice Terraces & Monkey Forest", sort_order=2),
            ItineraryHighlightNested(text="Couple's Jungle Spa Retreat", sort_order=3),
            ItineraryHighlightNested(text="Private Balinese Cooking Class", sort_order=4),
            ItineraryHighlightNested(text="Tegenungan Waterfall & Starlit Dinner", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Ubud — A Dreamy Welcome", "Arrive in Bali and take a private transfer to your handpicked hotel in the lush heart of Ubud. Enjoy a relaxing evening with a floral bath and a romantic dinner setup by TRAGUIN experts.", ["Sightseeing Included: VIP airport reception, private transfer to Ubud", "Evening Experience: Floral bath and romantic dinner setup", "Overnight Stay: Ubud (Luxury Villa)", "Meals Included: Dinner"]),
            _day(2, "Ubud — Nature's Embrace", "Explore the iconic Tegalalang Rice Terraces and the Sacred Monkey Forest. Experience scenic beauty and take photos at the most popular Instagram spots in Ubud.", ["Sightseeing Included: Tegalalang Rice Terraces, Sacred Monkey Forest", "Overnight Stay: Ubud (Luxury Villa)", "Meals Included: Breakfast & Dinner"]),
            _day(3, "Ubud — Wellness & Relaxation", "Indulge in a couple's spa retreat with a traditional Balinese massage in a jungle-view setting. Spend the evening at a boutique cafe in downtown Ubud.", ["Sightseeing Included: Couple's spa retreat, traditional Balinese massage", "Overnight Stay: Ubud (Luxury Villa)", "Meals Included: Breakfast & Dinner"]),
            _day(4, "Ubud — Cultural Exploration", "Visit the Ubud Art Market for local souvenirs. Participate in a private cooking class to learn the flavors of Bali.", ["Sightseeing Included: Ubud Art Market, private Balinese cooking class", "Overnight Stay: Ubud (Luxury Villa)", "Meals Included: Breakfast & Dinner"]),
            _day(5, "Ubud — Waterfall Adventure", "Discover the hidden gems of Ubud, including the stunning Tegenungan Waterfall. Enjoy a final romantic evening with a private dinner under the stars.", ["Sightseeing Included: Tegenungan Waterfall", "Evening Experience: Private dinner under the stars", "Overnight Stay: Ubud (Luxury Villa)", "Meals Included: Breakfast & Dinner"]),
            _day(6, "Farewell Bali", "Enjoy a leisurely breakfast before your private transfer to the airport. TRAGUIN ensures a seamless end to your perfect Ubud Love Escape.", ["Sightseeing Included: Private airport transfer", "Meals Included: Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Luxury Villa / similar", location="Ubud", nights_label="05 Nights", category_label="Premium", meal_plan="Breakfast & Dinner", stars=5, sort_order=1),
        ],
        inclusions=_id002_inclusions(),
    )
    return package, itinerary


def _id002_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="05 Nights luxury villa accommodation in Ubud", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Daily breakfast and romantic dinners", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Private luxury transfers throughout", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Complimentary honeymoon set-up (flower petals, cake)", sort_order=4),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 personal assistance", sort_order=5),
        ItineraryInclusionNested(kind="included", text="All taxes and service charges included", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Indonesia visa on arrival fees", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=10),
    ]


def build_id_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="id-005-premium-bali-family-tour",
        destination_id=destination_id,
        title="Premium Bali Family Tour",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=42,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Ubud (3N) → Seminyak/Kuta (4N) with Nusa Penida day cruise", sort_order=1),
            PackageHighlightNested(text="Bali Swing, Monkey Forest & Kintamani volcano views", sort_order=2),
            PackageHighlightNested(text="Tanah Lot, Uluwatu Kecak Fire Dance & Jimbaran seafood feast", sort_order=3),
            PackageHighlightNested(text="Private MPV with English-speaking guide throughout", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 premium concierge helpdesk", sort_order=5),
            PackageHighlightNested(text="Tour code TRAGUIN-BALI-PREMIUM-005 | Serial ID-005", sort_order=6),
        ],
        moods=["Family", "Luxury", "Beach", "Cultural", "Nature", "Adventure"],
    )
    itinerary = ItineraryCreate(
        slug="id-005-premium-bali-itinerary",
        destination_id=destination_id,
        title="Premium Bali Family Tour",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="On Request (Premium Custom)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Ubud • Kuta • Seminyak • Nusa Penida",
        overview=(
            "The ultimate Bali family tour — a majestic journey through mystical emerald rice terraces, iconic sea temples, "
            "and exclusive experiences designed for multi-generational families. Includes premium handpicked stays, "
            "Nusa Penida catamaran cruise, private MPV with professional guide, and TRAGUIN 24/7 concierge support. "
            "Best season: April to October."
        ),
        seo_title="ID-005 | Premium Bali Family Tour | TRAGUIN",
        seo_description=(
            "Luxury 07 Nights / 08 Days Bali family package (ID-005): Ubud, Nusa Penida, Tanah Lot, "
            "Uluwatu, Kintamani, and Seminyak with private MPV and catamaran cruise."
        ),
        is_featured=True,
        featured_sort_order=42,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Tegalalang Rice Terraces & Private Bali Swing", sort_order=1),
            ItineraryHighlightNested(text="Kintamani Volcano & Tirta Empul Temple", sort_order=2),
            ItineraryHighlightNested(text="Nusa Penida Catamaran Cruise", sort_order=3),
            ItineraryHighlightNested(text="Uluwatu Kecak Fire Dance", sort_order=4),
            ItineraryHighlightNested(text="Tanah Lot Sea Temple at Sunset", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Bali & Transfer to Ubud", "Arrive at Ngurah Rai International Airport with a warm Balinese welcome. Traditional cold towel and flower garlands before your scenic drive to Ubud. Check into your premium handpicked luxury resort villa.", ["Sightseeing Included: Airport meet & greet, Ubud scenic transfer", "Overnight Stay: Ubud (Premium Handpicked Resort Villa)", "Meals Included: Welcome drink & premium curated dinner"]),
            _day(2, "Ubud Cultural Immersion — Emerald Rice Terraces", "Visit the breathtaking Tegalalang Rice Terraces with private Bali Swing experience. Walk through the Sacred Monkey Forest and Ubud Royal Palace. Organic farm-to-table lunch overlooking the landscape.", ["Sightseeing Included: Tegalalang Rice Terraces, Bali Swing, Monkey Forest, Ubud Royal Palace", "Overnight Stay: Ubud (Premium Handpicked Resort Villa)", "Meals Included: Breakfast & gourmet lunch"]),
            _day(3, "Kintamani Volcano Majesty & Sacred Purification", "Journey to Kintamani for panoramic Mount Batur views. Visit Pura Tirta Empul holy water temple and local coffee and spice plantations.", ["Sightseeing Included: Kintamani volcano viewpoint, Tirta Empul Temple, coffee plantations", "Overnight Stay: Ubud (Premium Handpicked Resort Villa)", "Meals Included: Breakfast & lunch at volcano-view restaurant"]),
            _day(4, "Tanah Lot & Transition to Coastal Luxury", "Visit the mystical Tanah Lot Temple en route to Seminyak/Kuta. Check into your ultra-luxury beachfront resort.", ["Sightseeing Included: Tanah Lot sea temple, southern coastal highlights", "Evening Experience: Sunset at premium Seminyak beach club cabana", "Overnight Stay: Seminyak / Kuta (Luxury Beachfront Resort)", "Meals Included: Breakfast & premium seafood dinner"]),
            _day(5, "Nusa Penida Exclusive Cruise", "Premium high-speed catamaran day cruise to Nusa Penida. Visit Kelingking Beach, Angel's Billabong, and Broken Beach.", ["Sightseeing Included: Nusa Penida catamaran cruise, Kelingking Beach, Angel's Billabong, Broken Beach", "Overnight Stay: Seminyak / Kuta (Luxury Beachfront Resort)", "Meals Included: Breakfast & international buffet lunch on cruise"]),
            _day(6, "Uluwatu Cliff Temple & Fire Dance", "Explore the majestic Uluwatu Temple perched on a 70-meter cliff. Premium reserved seats for the Kecak Fire Dance at sunset. Candlelit family dinner on Jimbaran Bay sand.", ["Sightseeing Included: Uluwatu cliff temple, premium Kecak Fire Dance, Jimbaran Bay", "Evening Experience: Jimbaran Bay seafood feast on the sand", "Overnight Stay: Seminyak / Kuta (Luxury Beachfront Resort)", "Meals Included: Breakfast & Jimbaran seafood feast"]),
            _day(7, "Leisure, Spa & Luxury Shopping", "Complimentary Balinese massage at resort spa. Curated shopping tour of Seminyak luxury boutiques. Grand farewell dinner.", ["Sightseeing Included: Seminyak luxury retail tour, beachfront leisure", "Evening Experience: Grand farewell dinner at Indonesian heritage estate", "Overnight Stay: Seminyak / Kuta (Luxury Beachfront Resort)", "Meals Included: Breakfast & grand farewell dinner"]),
            _day(8, "Farewell Bali", "Final gourmet breakfast before private chauffeur transfer to Ngurah Rai International Airport.", ["Sightseeing Included: Private airport departure transfer", "Meals Included: Gourmet buffet breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Alaya Resort Ubud / similar", location="Ubud", nights_label="03 Nights", category_label="Deluxe", meal_plan="Bed & Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="The Haven Bali Seminyak / similar", location="Seminyak", nights_label="04 Nights", category_label="Deluxe", meal_plan="Bed & Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="Maya Ubud Resort & Spa / similar", location="Ubud", nights_label="03 Nights", category_label="Premium", meal_plan="Bed & Breakfast", stars=5, sort_order=3),
            ItineraryHotelNested(name="Courtyard by Marriott Seminyak / similar", location="Seminyak", nights_label="04 Nights", category_label="Premium", meal_plan="Bed & Breakfast", stars=5, sort_order=4),
            ItineraryHotelNested(name="The Kayon Resort by Pramana", location="Ubud", nights_label="03 Nights", category_label="Luxury", meal_plan="Bed & Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="The Seminyak Beach Resort & Spa", location="Seminyak", nights_label="04 Nights", category_label="Luxury", meal_plan="Breakfast + Dynamic Dining", stars=5, sort_order=6),
            ItineraryHotelNested(name="Mandapa, a Ritz-Carlton Reserve", location="Ubud", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Premium Ultra All-Inclusive", stars=5, sort_order=7),
            ItineraryHotelNested(name="The Legian Seminyak, Bali", location="Seminyak", nights_label="04 Nights", category_label="Ultra Luxury", meal_plan="Premium Ultra All-Inclusive", stars=5, sort_order=8),
        ],
        inclusions=_id005_inclusions(),
    )
    return package, itinerary


def _id005_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="07 Nights accommodation at selected luxury handpicked hotels", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Dedicated private MPV with English-speaking professional guide", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Daily premium breakfasts, 3 specialty lunches, and 4 high-end dinners", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Nusa Penida high-speed catamaran cruise with premium island sightseeing", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Traditional Balinese flower garlands, welcome drinks, and aromatherapy towels", sort_order=5),
        ItineraryInclusionNested(kind="included", text="One complimentary 60-minute Balinese spa treatment per adult guest", sort_order=6),
        ItineraryInclusionNested(kind="included", text="Private front-row reserved seating at Uluwatu Kecak Fire Dance", sort_order=7),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated local emergency assistance and concierge", sort_order=8),
        ItineraryInclusionNested(kind="included", text="Local government tourism taxes, service charges, and fuel surcharges", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="International airfare to/from Denpasar", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Indonesia Visa on Arrival fees", sort_order=11),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, mini-bar, and optional water-sports", sort_order=12),
        ItineraryInclusionNested(kind="excluded", text="Discretionary gratuities and travel insurance", sort_order=13),
    ]


def build_id_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="id-006-bali-girls-escape",
        destination_id=destination_id,
        title="Bali Girls Escape",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=43,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Seminyak (3N) → Ubud (2N) all-female luxury retreat", sort_order=1),
            PackageHighlightNested(text="Canggu VIP beach club & boutique shopping tour", sort_order=2),
            PackageHighlightNested(text="Uluwatu cliffs, Tanah Lot & Tegalalang Bali Swing", sort_order=3),
            PackageHighlightNested(text="Luxury flower bath & floating villa breakfast", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 priority concierge support", sort_order=5),
            PackageHighlightNested(text="Serial ID-006 | Category: Female Only / Girls Escape", sort_order=6),
        ],
        moods=["Solo", "Luxury", "Beach", "Cultural", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="id-006-bali-girls-escape-itinerary",
        destination_id=destination_id,
        title="Bali Girls Escape",
        duration_label="05 Nights / 06 Days",
        duration_days=6,
        starting_price=0,
        price_note="On Request (Premium Girls Escape)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Seminyak • Canggu • Uluwatu • Ubud",
        overview=(
            "An ultra-luxury journey exclusively arranged by TRAGUIN for discerning all-female travel collectives. "
            "This tropical retreat balances chic beach clubs, premium boutique shopping, dramatic cliffside sunsets, "
            "and soulful rainforest wellness across Seminyak and Ubud. Ideal for bachelorette parties and friends' getaways."
        ),
        seo_title="ID-006 | Bali Girls Escape | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days Bali girls escape (ID-006): Seminyak, Canggu beach clubs, "
            "Uluwatu, Tanah Lot, Ubud rice terraces, and luxury flower bath."
        ),
        is_featured=True,
        featured_sort_order=43,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Canggu VIP Beach Club Daybed Access", sort_order=1),
            ItineraryHighlightNested(text="Uluwatu Cliffside Sunset Dining", sort_order=2),
            ItineraryHighlightNested(text="Tanah Lot Sea Shrine", sort_order=3),
            ItineraryHighlightNested(text="Private Bali Swing & Tegalalang Terraces", sort_order=4),
            ItineraryHighlightNested(text="Floating Villa Breakfast Farewell", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Bali — Elite Welcome to Seminyak", "VIP airport meet & greet with flower garlands. Private luxury transfer to your handpicked hotel or pool villa in Seminyak. Welcome sunset cocktail at a premier beachfront lounge.", ["Sightseeing Included: VIP airport meet & greet, private luxury transfer", "Evening Experience: Welcome sunset cocktail at oceanfront lounge", "Overnight Stay: Seminyak (Premium Luxury Resort / Pool Villa)", "Meals Included: Welcome refreshments & curated welcome dinner"]),
            _day(2, "Canggu Lifestyle — Boutique Shopping & VIP Beach Club", "Guided shopping tour through Canggu's premium boutiques and designer shops. Pre-booked VIP oceanfront cabana at a world-famous beach club.", ["Sightseeing Included: Canggu guided shopping tour, VIP beach club daybed access", "Overnight Stay: Seminyak (Premium Luxury Resort / Pool Villa)", "Meals Included: Breakfast & VIP beach club lunch platter"]),
            _day(3, "Uluwatu Cliffside Majesty & Sunset Dining", "Visit Uluwatu Temple perched 70 meters above the Indian Ocean. Candlelit fine dining at an exclusive cliff-edge restaurant with live acoustic music.", ["Sightseeing Included: Uluwatu cliff temple, guided coastal panoramic tour", "Evening Experience: Luxury seafood sunset dinner at cliff-edge restaurant", "Overnight Stay: Seminyak (Premium Luxury Resort / Pool Villa)", "Meals Included: Breakfast & luxury seafood sunset dinner"]),
            _day(4, "Tanah Lot & Journey to Ubud Rainforest", "Visit Tanah Lot Temple en route to Ubud. Check into ultra-luxury rainforest resort with pre-arranged Balinese flower-petal bath in your villa.", ["Sightseeing Included: Tanah Lot temple, scenic Ubud interior transfer", "Evening Experience: Organic farm-to-table dinner under the stars", "Overnight Stay: Ubud (Ultra-Luxury Rainforest Resort Villa)", "Meals Included: Breakfast & Balinese luxury fusion dinner"]),
            _day(5, "Tegalalang Rice Terraces & Private Bali Swing", "Morning at Tegalalang Rice Terraces with private VIP Bali Swing access. Hidden jungle waterfall and Ubud artisan market. Grand TRAGUIN signature celebration dinner.", ["Sightseeing Included: Tegalalang terraces, private Bali Swing, hidden waterfall, artisan market", "Evening Experience: Grand farewell celebration feast", "Overnight Stay: Ubud (Ultra-Luxury Rainforest Resort Villa)", "Meals Included: Signature floating villa breakfast & premium farewell dinner"]),
            _day(6, "Soulful Farewell", "Floating breakfast in your private villa infinity pool. Private luxury transfer to Ngurah Rai International Airport.", ["Sightseeing Included: Private airport departure transfer", "Meals Included: Premium floating or buffet resort breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Wina Holiday Villa Kuta / Seminyak / similar", location="Seminyak", nights_label="03 Nights", category_label="Deluxe", meal_plan="Daily Buffet Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="Sthala, a Tribute Portfolio Hotel, Ubud / similar", location="Ubud", nights_label="02 Nights", category_label="Deluxe", meal_plan="Daily Buffet Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="Hotel Indigo Bali Seminyak Beach / similar", location="Seminyak", nights_label="03 Nights", category_label="Premium", meal_plan="Daily Gourmet Breakfast", stars=5, sort_order=3),
            ItineraryHotelNested(name="Komaneka at Bisma, Ubud / similar", location="Ubud", nights_label="02 Nights", category_label="Premium", meal_plan="Daily Gourmet Breakfast", stars=5, sort_order=4),
            ItineraryHotelNested(name="W Bali — Seminyak", location="Seminyak", nights_label="03 Nights", category_label="Elite Luxury", meal_plan="Daily Breakfast + 1 Signature Dinner", stars=5, sort_order=5),
            ItineraryHotelNested(name="The Kayon Jungle Resort by Pramana", location="Ubud", nights_label="02 Nights", category_label="Elite Luxury", meal_plan="Daily Breakfast + 1 Signature Dinner", stars=5, sort_order=6),
            ItineraryHotelNested(name="The Legian Seminyak, Bali", location="Seminyak", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Bespoke All-Inclusive", stars=5, sort_order=7),
            ItineraryHotelNested(name="Como Shambhala Estate, Ubud", location="Ubud", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Bespoke All-Inclusive", stars=5, sort_order=8),
        ],
        inclusions=_id006_inclusions(),
    )
    return package, itinerary


def _id006_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="05 Nights at premium handpicked hotels or private pool villas", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Dedicated private luxury MPV with English-speaking chauffeur", sort_order=2),
        ItineraryInclusionNested(kind="included", text="5 breakfasts (including 1 signature floating villa breakfast) and 3 specialty dinners", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Pre-booked premium entry and daybed access at Canggu elite beach club", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Complimentary iconic Balinese luxury flower bath arrangement per guest", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Private entry tickets and unlimited swings at premier Bali Swing location", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 priority concierge backing", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="International airfare to/from Denpasar", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Indonesia Visa on Arrival and customs declaration fees", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Extra food, premium alcoholic beverages, laundry, and shopping", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Voluntary tips and travel insurance", sort_order=11),
    ]


def build_id_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="id-007-luxury-bali-retreat",
        destination_id=destination_id,
        title="Luxury Bali Retreat",
        duration_label="06 Nights / 07 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=44,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Nusa Dua (3N) → Ubud (3N) ultra-luxury signature circuit", sort_order=1),
            PackageHighlightNested(text="VIP fast-track arrival & private lagoon catamaran cruise", sort_order=2),
            PackageHighlightNested(text="Uluwatu VIP Kecak Fire Dance & Tanah Lot temple", sort_order=3),
            PackageHighlightNested(text="Mount Batur, Tirta Empul purification & Bali Swing", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated priority concierge", sort_order=5),
            PackageHighlightNested(text="Serial ID-007 | Category: Ultra-Luxury Signature", sort_order=6),
        ],
        moods=["Luxury", "Romantic", "Family", "Beach", "Cultural", "Nature", "Spiritual"],
    )
    itinerary = ItineraryCreate(
        slug="id-007-luxury-bali-retreat-itinerary",
        destination_id=destination_id,
        title="Luxury Bali Retreat",
        duration_label="06 Nights / 07 Days",
        duration_days=7,
        starting_price=0,
        price_note="On Request (Ultra-Luxury Signature Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Nusa Dua • Uluwatu • Ubud • Mount Batur",
        overview=(
            "An ultra-luxury signature journey crafted by TRAGUIN for discerning world travelers. Experience white-glove "
            "logistics, elite culinary journeys, and stays within the world's most acclaimed resort estates — from the "
            "tranquil beaches of Nusa Dua and majestic cliffs of Uluwatu to the spiritual heartbeat of Ubud."
        ),
        seo_title="ID-007 | Luxury Bali Retreat | TRAGUIN",
        seo_description=(
            "Ultra-luxury 06 Nights / 07 Days Bali retreat (ID-007): Nusa Dua, Uluwatu, Tanah Lot, Ubud, "
            "Mount Batur, Tirta Empul purification, and VIP Kecak Fire Dance."
        ),
        is_featured=True,
        featured_sort_order=44,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="VIP Fast-Track Airport Arrival", sort_order=1),
            ItineraryHighlightNested(text="Private Nusa Dua Lagoon Catamaran Cruise", sort_order=2),
            ItineraryHighlightNested(text="VIP Uluwatu Kecak Fire Dance", sort_order=3),
            ItineraryHighlightNested(text="Mount Batur & Kintamani Panoramas", sort_order=4),
            ItineraryHighlightNested(text="Priest-Guided Tirta Empul Purification", sort_order=5),
        ],
        days=[
            _day(1, "Arrival — VIP Fast-Track & Nusa Dua Luxury Repose", "Fast-track VIP customs clearance at Ngurah Rai Airport. Private luxury chauffeur transfer to Nusa Dua beachfront resort. Elegant multi-course coastal welcome dinner.", ["Sightseeing Included: VIP fast-track airport arrival, private luxury transfer", "Evening Experience: Welcome dinner at beachfront pavilion", "Overnight Stay: Nusa Dua (Elite Luxury Oceanfront Resort)", "Meals Included: Welcome refreshments & curated welcome dinner"]),
            _day(2, "Exclusive Lagoon Cruise & Water Blow", "Private luxury catamaran charter along Nusa Dua reef lagoons with snorkeling. Visit the dramatic Water Blow site. Reserved premium private beach cabana with butler service.", ["Sightseeing Included: Private lagoon cruise, Water Blow guided walk, premium beach cabana", "Overnight Stay: Nusa Dua (Elite Luxury Oceanfront Resort)", "Meals Included: Breakfast, oceanfront lunch & premium beachside dinner"]),
            _day(3, "Uluwatu Sea Shrine & VIP Kecak Fire Dance", "Visit Uluwatu Temple on dramatic limestone cliffs. Pre-reserved front-row VIP seats for the Kecak Fire Dance at sunset. Multi-course dinner at award-winning cliff-edge restaurant.", ["Sightseeing Included: Uluwatu cliff temple, VIP amphitheater Kecak Fire Dance seating", "Evening Experience: Luxury fine dining cliff dinner", "Overnight Stay: Nusa Dua (Elite Luxury Oceanfront Resort)", "Meals Included: Breakfast & luxury fine dining cliff dinner"]),
            _day(4, "Tanah Lot & Transfer to Ubud Valley Sanctuary", "Visit world-renowned Tanah Lot Temple. Continue inland to Ubud and check into ultra-luxury valley estate villa with infinity pool over the jungle canopy.", ["Sightseeing Included: Tanah Lot temple exclusive access, scenic inland luxury drive", "Evening Experience: Farm-to-table degustation dinner overlooking valley canyon", "Overnight Stay: Ubud (Ultra-Luxury Rainforest Valley Pool Villa)", "Meals Included: Breakfast & gourmet valley degustation dinner"]),
            _day(5, "Kintamani Highlands & Mount Batur Vistas", "Spectacular panorama of Mount Batur and caldera lake from Kintamani. Private tour through artisanal organic coffee estate. Fine dining dinner at acclaimed Ubud gastronomy destination.", ["Sightseeing Included: Kintamani volcano panoramic tour, Mount Batur caldera, private coffee estate", "Overnight Stay: Ubud (Ultra-Luxury Rainforest Valley Pool Villa)", "Meals Included: Breakfast, luxury highland lunch & fine dining dinner"]),
            _day(6, "Tegalalang Terraces, Bali Swing & Tirta Empul Purification", "Morning at Tegalalang Rice Terraces with private VIP Bali Swing. Priest-guided purification ritual at Tirta Empul Holy Water Temple. TRAGUIN signature celebration dinner in villa grounds.", ["Sightseeing Included: Tegalalang terraces, private Bali Swing, Tirta Empul priest-guided purification", "Evening Experience: Private gala farewell dinner with butler service", "Overnight Stay: Ubud (Ultra-Luxury Rainforest Valley Pool Villa)", "Meals Included: Signature floating villa breakfast & private gala farewell dinner"]),
            _day(7, "Floating Pool Breakfast & Departure", "Iconic floating breakfast in private villa infinity pool. Private luxury transfer to Ngurah Rai Airport with departure concierge assistance.", ["Sightseeing Included: Private luxury airport transfer, departure concierge assistance", "Meals Included: Premium floating infinity pool breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="The Westin Resort Nusa Dua, Bali / similar", location="Nusa Dua", nights_label="03 Nights", category_label="Deluxe", meal_plan="Daily Luxury Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Alila Ubud / similar", location="Ubud", nights_label="03 Nights", category_label="Deluxe", meal_plan="Daily Luxury Breakfast", stars=5, sort_order=2),
            ItineraryHotelNested(name="The St. Regis Bali Resort", location="Nusa Dua", nights_label="03 Nights", category_label="Premium", meal_plan="Daily Gourmet Breakfast", stars=5, sort_order=3),
            ItineraryHotelNested(name="Mandapa, a Ritz-Carlton Reserve", location="Ubud", nights_label="03 Nights", category_label="Premium", meal_plan="Daily Gourmet Breakfast", stars=5, sort_order=4),
            ItineraryHotelNested(name="The Ritz-Carlton, Bali", location="Nusa Dua", nights_label="03 Nights", category_label="Elite Luxury", meal_plan="Daily Breakfast + 1 Specialty Dinner", stars=5, sort_order=5),
            ItineraryHotelNested(name="Viceroy Bali, Ubud", location="Ubud", nights_label="03 Nights", category_label="Elite Luxury", meal_plan="Daily Breakfast + 1 Specialty Dinner", stars=5, sort_order=6),
            ItineraryHotelNested(name="Amanusa (Aman Villas Nusa Dua)", location="Nusa Dua", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Bespoke Ultra-Inclusive", stars=5, sort_order=7),
            ItineraryHotelNested(name="Amandari, Ubud", location="Ubud", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Bespoke Ultra-Inclusive", stars=5, sort_order=8),
        ],
        inclusions=_id007_inclusions(),
    )
    return package, itinerary


def _id007_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="06 Nights at premium handpicked hotels or private luxury pool villas", sort_order=1),
        ItineraryInclusionNested(kind="included", text="VIP fast-track arrival immigration greeting services at airport", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Dedicated luxury Alphard/MPV with professional English-fluent tour guide", sort_order=3),
        ItineraryInclusionNested(kind="included", text="6 breakfasts (including 1 signature floating breakfast) and 4 specialty dinners", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Private luxury catamaran lagoon cruise along Nusa Dua reef", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Pre-reserved front-row VIP tickets at Uluwatu Kecak Fire Dance", sort_order=6),
        ItineraryInclusionNested(kind="included", text="Priest-guided traditional purification session at Tirta Empul Temple", sort_order=7),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated priority operations and on-ground concierge", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="International airfare to/from Denpasar", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Indonesia Visa on Arrival and customs declaration costs", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Extra food, vintage alcoholic beverages, laundry, and personal shopping", sort_order=11),
        ItineraryInclusionNested(kind="excluded", text="Gratuities and comprehensive travel insurance", sort_order=12),
    ]


ID_BUILDERS = [
    build_id_001,
    build_id_002,
    build_id_005,
    build_id_006,
    build_id_007,
]
