"""Builder functions for TR-001 through TR-005 Turkey packages (no images)."""

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


def build_tr_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="tr-001-turkey-highlights-family-tour",
        destination_id=destination_id,
        title="Turkey Highlights Family Tour",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=72,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Istanbul (3N) → Cappadocia (2N) → Kusadasi (2N) classic family circuit", sort_order=1),
            PackageHighlightNested(text="Hagia Sophia, Blue Mosque & Grand Bazaar heritage tour", sort_order=2),
            PackageHighlightNested(text="Cappadocia hot air balloon & underground cities", sort_order=3),
            PackageHighlightNested(text="Ephesus ancient ruins & Mediterranean coastal leisure", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-TUR-HIG-2026 | Serial TR-001", sort_order=6),
        ],
        moods=["Family", "Luxury", "Cultural", "Adventure", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="tr-001-turkey-highlights-itinerary",
        destination_id=destination_id,
        title="Turkey Highlights Family Tour",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="On Request (Premium Turkey Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Istanbul • Cappadocia • Ephesus • Mediterranean Charm",
        overview=(
            "Discover the absolute highlights of Turkey with TRAGUIN's curated family expedition. "
            "This comprehensive 8-day journey takes your family through the vibrant history of Istanbul, "
            "the magical landscape of Cappadocia, and the ancient ruins of Ephesus — ensuring unforgettable "
            "memories across Turkey's most iconic landscapes."
        ),
        seo_title="TR-001 | Turkey Highlights Family Tour | TRAGUIN",
        seo_description=(
            "Premium 07 Nights / 08 Days Turkey family package (TR-001): Istanbul heritage, Cappadocia hot air "
            "balloons, Ephesus ruins, and Mediterranean coastal charm."
        ),
        is_featured=True,
        featured_sort_order=72,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Istanbul Heritage — Hagia Sophia & Blue Mosque", sort_order=1),
            ItineraryHighlightNested(text="Grand Bazaar & Bosphorus Cruise", sort_order=2),
            ItineraryHighlightNested(text="Cappadocia Hot Air Balloon Sunrise", sort_order=3),
            ItineraryHighlightNested(text="Ephesus Ancient Ruins", sort_order=4),
            ItineraryHighlightNested(text="Coastal Leisure & Farewell Gala", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Istanbul", "Arrive in Istanbul. Private transfer to your handpicked premium hotel. Evening at leisure to enjoy the city's historic charm.", ["Sightseeing Included: VIP airport reception, private hotel transfer", "Overnight Stay: Istanbul (Luxury Historic Hotel)", "Meals Included: Welcome arrangements on arrival"]),
            _day(2, "Istanbul Heritage Tour", "A comprehensive city tour covering Istanbul's most famous landmarks like the Hagia Sophia and Blue Mosque, providing a rich educational experience.", ["Sightseeing Included: Hagia Sophia, Blue Mosque, historic city tour", "Overnight Stay: Istanbul (Luxury Historic Hotel)", "Meals Included: Breakfast"]),
            _day(3, "Bazaar & Bosphorus Cruise", "Explore the vibrant Grand Bazaar and enjoy a premium Bosphorus cruise, showcasing the iconic attractions that define Istanbul.", ["Sightseeing Included: Grand Bazaar visit, premium Bosphorus cruise", "Overnight Stay: Istanbul (Luxury Historic Hotel)", "Meals Included: Breakfast"]),
            _day(4, "Flight to Cappadocia", "Morning transfer to airport for flight to Cappadocia. Check into a luxury boutique cave hotel — an exclusive experience.", ["Sightseeing Included: Domestic flight to Cappadocia, private transfer to cave hotel", "Overnight Stay: Cappadocia (Premium Cave Hotel)", "Meals Included: Breakfast"]),
            _day(5, "Cappadocia Magical Landscapes", "Experience the sunrise in a hot air balloon, followed by a tour of the region's unique valleys and underground cities — unforgettable memories.", ["Sightseeing Included: Hot air balloon sunrise, valley tour, underground cities", "Overnight Stay: Cappadocia (Premium Cave Hotel)", "Meals Included: Breakfast"]),
            _day(6, "Flight to Ephesus / Kusadasi", "Morning transfer to airport for flight to Izmir. Transfer to the coastal town of Kusadasi and visit the ancient ruins of Ephesus.", ["Sightseeing Included: Domestic flight to Izmir, Ephesus ancient ruins tour", "Overnight Stay: Kusadasi (Luxury Coastal Resort)", "Meals Included: Breakfast"]),
            _day(7, "Coastal Leisure & Celebration", "A day of leisure at your coastal resort, followed by a grand farewell dinner gala — an exclusive experience for the family.", ["Evening Experience: Grand farewell dinner gala", "Overnight Stay: Kusadasi (Luxury Coastal Resort)", "Meals Included: Breakfast & Farewell Dinner"]),
            _day(8, "Departure", "Final luxury breakfast before your TRAGUIN private transfer, completing your premium Turkey highlights expedition.", ["Sightseeing Included: Private airport transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Luxury Historic Hotels / similar", location="Istanbul", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Premium Cave Hotel / similar", location="Cappadocia", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=2),
            ItineraryHotelNested(name="Luxury Coastal Resort / similar", location="Kusadasi", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=3),
        ],
        inclusions=_tr001_inclusions(),
    )
    return package, itinerary


def _tr001_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="07 Nights in handpicked premium family hotels across Istanbul, Cappadocia, and Kusadasi", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private executive chauffeur-driven luxury ground transfers", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Domestic flights Istanbul–Cappadocia and Cappadocia–Izmir", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Istanbul heritage tour, Grand Bazaar & Bosphorus cruise", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Cappadocia hot air balloon sunrise and valley exploration", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Ephesus ancient ruins guided tour", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated on-ground family concierge support", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Turkey entry visa processing fees", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=11),
    ]


def build_tr_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="tr-002-romantic-turkey-couple-tour",
        destination_id=destination_id,
        title="Romantic Turkey Couple Tour",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=73,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Istanbul (3N) → Cappadocia (2N) → Antalya (2N) romantic sanctuary", sort_order=1),
            PackageHighlightNested(text="Intimate Bosphorus welcome dinner & sunset cruise", sort_order=2),
            PackageHighlightNested(text="Private Cappadocia balloon sunrise over fairy chimneys", sort_order=3),
            PackageHighlightNested(text="Mediterranean beachfront couple's resort in Antalya", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 honeymoon concierge desk support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-TUR-ROM-2026 | Serial TR-002", sort_order=6),
        ],
        moods=["Romantic", "Luxury", "Cultural", "Beach", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="tr-002-romantic-turkey-itinerary",
        destination_id=destination_id,
        title="Romantic Turkey Couple Tour",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="On Request (Premium Honeymoon Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Istanbul Romance • Cappadocia Balloon • Mediterranean Serenity",
        overview=(
            "Begin your romantic journey together in the enchanting landscapes of Turkey. This TRAGUIN curated "
            "couple's sanctuary blends the vibrant cultural heart of Istanbul, the magical balloon-filled skies "
            "of Cappadocia, and the azure beauty of the Mediterranean coast — ensuring unforgettable memories "
            "in a truly romantic setting."
        ),
        seo_title="TR-002 | Romantic Turkey Couple Tour | TRAGUIN",
        seo_description=(
            "Premium 07 Nights / 08 Days Turkey honeymoon package (TR-002): Istanbul romance, Cappadocia balloon "
            "sunrise, coastal serenity, and exclusive couple getaways."
        ),
        is_featured=True,
        featured_sort_order=73,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Intimate Bosphorus Welcome Dinner", sort_order=1),
            ItineraryHighlightNested(text="Slow-Paced Istanbul Cultural Harmony", sort_order=2),
            ItineraryHighlightNested(text="Private Bosphorus Sunset Cruise", sort_order=3),
            ItineraryHighlightNested(text="Cappadocia Balloon Sunrise & Hidden Vineyards", sort_order=4),
            ItineraryHighlightNested(text="Antalya Beachfront Candlelit Farewell", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Istanbul & Intimate Welcome", "Arrive in Istanbul. Private chauffeur transfer to your intimate luxury hotel. Savor a quiet, romantic welcome dinner with Bosphorus views.", ["Sightseeing Included: VIP airport reception, private chauffeur transfer", "Evening Experience: Romantic welcome dinner with Bosphorus views", "Overnight Stay: Istanbul (Luxury Historic Boutique Hotel)", "Meals Included: Welcome Dinner"]),
            _day(2, "Istanbul Cultural Harmony", "A slow-paced, romantic exploration of Istanbul's iconic historic landmarks, perfect for couples wanting to discover cultural richness together.", ["Sightseeing Included: Historic landmarks tour at a relaxed pace", "Overnight Stay: Istanbul (Luxury Historic Boutique Hotel)", "Meals Included: Breakfast"]),
            _day(3, "Bosphorus Sunset Cruise", "Enjoy a premium private Bosphorus sunset cruise, sipping champagne while taking in the city skyline — unforgettable memories.", ["Sightseeing Included: Premium private Bosphorus sunset cruise", "Overnight Stay: Istanbul (Luxury Historic Boutique Hotel)", "Meals Included: Breakfast"]),
            _day(4, "Flight to Cappadocia", "Transfer to airport for your flight to Cappadocia. Check into an ultra-luxury boutique cave hotel — an exclusive experience.", ["Sightseeing Included: Domestic flight to Cappadocia, private transfer to cave hotel", "Overnight Stay: Cappadocia (Ultra-Luxury Cave Resort)", "Meals Included: Breakfast"]),
            _day(5, "Cappadocia Balloon Sunrise", "Experience the sunrise in a private hot air balloon over fairy chimneys. Afternoon exploration of the magical valleys and hidden vineyards.", ["Sightseeing Included: Private hot air balloon sunrise, valley and vineyard exploration", "Overnight Stay: Cappadocia (Ultra-Luxury Cave Resort)", "Meals Included: Breakfast"]),
            _day(6, "Flight to Antalya", "Transfer to airport for your flight to the Mediterranean coast. Check into a luxury beachfront couple's resort.", ["Sightseeing Included: Domestic flight to Antalya, private resort transfer", "Overnight Stay: Antalya (Luxury Beachfront Couple Retreat)", "Meals Included: Breakfast"]),
            _day(7, "Coastal Serenity & Farewell", "A day of private relaxation on the beach, followed by a candlelit farewell dinner under the stars, celebrating your romantic getaway.", ["Evening Experience: Candlelit farewell dinner under the stars", "Overnight Stay: Antalya (Luxury Beachfront Couple Retreat)", "Meals Included: Breakfast & Farewell Dinner"]),
            _day(8, "Departure", "Final luxury breakfast before your TRAGUIN private chauffeur transfer to the airport, completing your premium Turkey sojourn.", ["Sightseeing Included: Private chauffeur airport transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Luxury Historic Boutique Hotels / similar", location="Istanbul", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Ultra-Luxury Cave Resort / similar", location="Cappadocia", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=2),
            ItineraryHotelNested(name="Luxury Beachfront Couple Retreat / similar", location="Antalya", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=3),
        ],
        inclusions=_tr002_inclusions(),
    )
    return package, itinerary


def _tr002_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="07 Nights in handpicked romantic hotels across Istanbul, Cappadocia, and Antalya", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private chauffeur-driven luxury ground transfers throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Domestic flights Istanbul–Cappadocia and Cappadocia–Antalya", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Private Bosphorus sunset cruise with champagne", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Private Cappadocia hot air balloon sunrise over fairy chimneys", sort_order=5),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated honeymoon concierge support", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Turkey entry visa processing fees", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=10),
    ]


def build_tr_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="tr-003-luxury-turkey-tour",
        destination_id=destination_id,
        title="Luxury Turkey Tour",
        duration_label="08 Nights / 09 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=74,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Istanbul (3N) → Cappadocia (3N) → Bodrum/Antalya (3N) ultra-luxury circuit", sort_order=1),
            PackageHighlightNested(text="VIP Istanbul heritage & private Bosphorus yacht sojourn", sort_order=2),
            PackageHighlightNested(text="Cappadocia sunrise ballooning & private gourmet valley brunch", sort_order=3),
            PackageHighlightNested(text="Artisan workshops, underground cities & coastal spa elegance", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 luxury travel concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-TUR-LUX-2026 | Serial TR-003", sort_order=6),
        ],
        moods=["Luxury", "Family", "Cultural", "Beach", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="tr-003-luxury-turkey-itinerary",
        destination_id=destination_id,
        title="Luxury Turkey Tour",
        duration_label="08 Nights / 09 Days",
        duration_days=9,
        starting_price=0,
        price_note="On Request (Ultra-Luxury Turkey Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Istanbul Ultra-Luxury • Cappadocia Cave Suites • Mediterranean Coastal Elegance",
        overview=(
            "Indulge in the absolute height of sophistication across Turkey with TRAGUIN's curated luxury expedition. "
            "From opulent five-star stays and boutique cave suites to exclusive private tours and elite culinary "
            "experiences, this journey is designed for the discerning traveler — ensuring unforgettable memories "
            "in ultimate luxury."
        ),
        seo_title="TR-003 | Luxury Turkey Tour | TRAGUIN",
        seo_description=(
            "Ultra-luxury 08 Nights / 09 Days Turkey package (TR-003): Four Seasons Bosphorus, Museum Hotel "
            "Cappadocia, Mandarin Oriental Bodrum, private tours, and elite culinary experiences."
        ),
        is_featured=True,
        featured_sort_order=74,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="VIP Arrival & Gourmet Bosphorus Welcome", sort_order=1),
            ItineraryHighlightNested(text="Exclusive Private Istanbul Heritage Tour", sort_order=2),
            ItineraryHighlightNested(text="Private Yacht Bosphorus Sojourn", sort_order=3),
            ItineraryHighlightNested(text="Cappadocia Sunrise Balloon & Gourmet Valley Brunch", sort_order=4),
            ItineraryHighlightNested(text="Coastal Spa Elegance & Farewell Gala", sort_order=5),
        ],
        days=[
            _day(1, "VIP Arrival & Istanbul Luxury", "Arrive in Istanbul. VIP chauffeur transfer to your world-class hotel. Evening gourmet welcome dinner overlooking the Bosphorus.", ["Sightseeing Included: VIP airport reception, private chauffeur transfer", "Evening Experience: Gourmet welcome dinner overlooking the Bosphorus", "Overnight Stay: Istanbul (Four Seasons Bosphorus)", "Meals Included: Welcome Dinner"]),
            _day(2, "Exclusive Istanbul Heritage", "Private guided tour of Istanbul's most prestigious historical landmarks, providing a rich exclusive experience of Ottoman culture.", ["Sightseeing Included: Private guided Istanbul heritage tour", "Overnight Stay: Istanbul (Four Seasons Bosphorus)", "Meals Included: Breakfast"]),
            _day(3, "Private Bosphorus Sojourn", "Experience the city from a private yacht on the Bosphorus. An exclusive experience with premium catering.", ["Sightseeing Included: Private yacht Bosphorus cruise with premium catering", "Overnight Stay: Istanbul (Four Seasons Bosphorus)", "Meals Included: Breakfast"]),
            _day(4, "Flight to Cappadocia", "VIP transfer to airport for your flight to Cappadocia. Check into an ultra-luxury boutique cave resort.", ["Sightseeing Included: Domestic flight to Cappadocia, VIP transfer to cave resort", "Overnight Stay: Cappadocia (Museum Hotel / Argos in Cappadocia)", "Meals Included: Breakfast"]),
            _day(5, "Cappadocia Sunrise Ballooning", "Sunrise hot air balloon flight over unique valleys. Followed by a private gourmet brunch in a secluded valley setting.", ["Sightseeing Included: Hot air balloon sunrise, private gourmet valley brunch", "Overnight Stay: Cappadocia (Museum Hotel / Argos in Cappadocia)", "Meals Included: Breakfast & Gourmet Brunch"]),
            _day(6, "Artisan Discovery", "Private tour of local artisan workshops and underground cities, discovering the rich history and artistry of the region.", ["Sightseeing Included: Private artisan workshop and underground city tour", "Overnight Stay: Cappadocia (Museum Hotel / Argos in Cappadocia)", "Meals Included: Breakfast"]),
            _day(7, "Flight to Coastal Paradise", "Private transfer for your flight to Bodrum or Antalya. Check into an ultra-luxury coastal resort.", ["Sightseeing Included: Domestic flight to Bodrum/Antalya, VIP resort transfer", "Overnight Stay: Bodrum/Antalya (Mandarin Oriental Bodrum)", "Meals Included: Breakfast"]),
            _day(8, "Coastal Elegance & Farewell", "A day of private leisure and spa treatments on the Mediterranean coast. Evening farewell gala dinner, celebrating your luxury expedition.", ["Evening Experience: Farewell gala dinner", "Overnight Stay: Bodrum/Antalya (Mandarin Oriental Bodrum)", "Meals Included: Breakfast & Gala Dinner"]),
            _day(9, "Departure", "Final luxury breakfast. VIP chauffeur transfer to the airport, concluding your premium Turkey luxury expedition.", ["Sightseeing Included: VIP chauffeur airport transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Four Seasons Bosphorus", location="Istanbul", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Museum Hotel / Argos in Cappadocia", location="Cappadocia", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=2),
            ItineraryHotelNested(name="Mandarin Oriental Bodrum", location="Bodrum / Antalya", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=3),
        ],
        inclusions=_tr003_inclusions(),
    )
    return package, itinerary


def _tr003_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="08 Nights in ultra-luxury hotels across Istanbul, Cappadocia, and the Mediterranean coast", sort_order=1),
        ItineraryInclusionNested(kind="included", text="VIP chauffeur-driven luxury ground transfers throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Domestic flights Istanbul–Cappadocia and Cappadocia–Bodrum/Antalya", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Private yacht Bosphorus sojourn with premium catering", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Cappadocia sunrise hot air balloon and private gourmet valley brunch", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Private artisan workshop and underground city tour", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated luxury travel concierge support", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Turkey entry visa processing fees", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=11),
    ]


def build_tr_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="tr-004-turkey-family-explorer-tour",
        serial_code="TR-004",
        traguin_tour_code="TRG-TUR-FAM-2026",
        destination_id=destination_id,
        title="Turkey Family Explorer Tour",
        duration_label="06 Nights / 07 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=False,
        featured_sort_order=None,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Istanbul (3N) → Cappadocia (3N) classic family explorer circuit", sort_order=1),
            PackageHighlightNested(text="Istanbul cultural highlights, Grand Bazaar & Bosphorus cruise", sort_order=2),
            PackageHighlightNested(text="Cappadocia hot air balloon sunrise & underground cities", sort_order=3),
            PackageHighlightNested(text="Family-friendly boutique cave hotel stay in Cappadocia", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-TUR-FAM-2026 | Serial TR-004", sort_order=6),
        ],
        moods=["Family", "Luxury", "Cultural", "Adventure", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="tr-004-turkey-family-explorer-itinerary",
        destination_id=destination_id,
        title="Turkey Family Explorer Tour",
        duration_label="06 Nights / 07 Days",
        duration_days=7,
        starting_price=0,
        price_note="On Request (Premium Turkey Family Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Istanbul Heritage • Cappadocia Hot Air Balloons • Family Adventures",
        overview=(
            "Discover the magic of Istanbul and the otherworldly landscapes of Cappadocia with our TRAGUIN curated "
            "family expedition. This comprehensive 7-day journey balances the historical wonders of the imperial city "
            "with the adventurous spirit of Cappadocia, ensuring unforgettable memories for your entire family."
        ),
        seo_title="TR-004 | Turkey Family Explorer Tour | TRAGUIN",
        seo_description=(
            "Premium 06 Nights / 07 Days Turkey family package (TR-004): Istanbul heritage, Cappadocia hot air "
            "balloons, underground cities, and family adventures."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Istanbul Cultural Highlights & Bosphorus Discovery", sort_order=1),
            ItineraryHighlightNested(text="Grand Bazaar Exploration", sort_order=2),
            ItineraryHighlightNested(text="Cappadocia Hot Air Balloon Sunrise", sort_order=3),
            ItineraryHighlightNested(text="Underground Cities & Valley Exploration", sort_order=4),
            ItineraryHighlightNested(text="Artisan Workshops & Leisure Discovery", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Istanbul", "Arrive in Istanbul. Private transfer to your handpicked premium hotel. Evening at leisure to enjoy the city's historic charm.", ["Sightseeing Included: VIP airport reception, private hotel transfer", "Overnight Stay: Istanbul (Premium Luxury Boutique Hotel)", "Meals Included: Welcome arrangements on arrival"]),
            _day(2, "Istanbul Cultural Highlights", "A comprehensive city tour covering Istanbul's most famous landmarks, providing a rich educational experience for your family.", ["Sightseeing Included: Istanbul cultural highlights city tour", "Overnight Stay: Istanbul (Premium Luxury Boutique Hotel)", "Meals Included: Breakfast"]),
            _day(3, "Bazaar & Bosphorus Discovery", "Explore the vibrant Grand Bazaar and enjoy a Bosphorus cruise, showcasing the iconic attractions of the city.", ["Sightseeing Included: Grand Bazaar visit, Bosphorus cruise", "Overnight Stay: Istanbul (Premium Luxury Boutique Hotel)", "Meals Included: Breakfast"]),
            _day(4, "Flight to Cappadocia", "Morning flight to Cappadocia. Check into a family-friendly boutique cave hotel — an exclusive experience.", ["Sightseeing Included: Domestic flight to Cappadocia, private transfer to cave hotel", "Overnight Stay: Cappadocia (Premium Cave Suites)", "Meals Included: Breakfast"]),
            _day(5, "Cappadocia Adventure", "Experience the sunrise in a hot air balloon, followed by a tour of the region's unique valleys and underground cities — unforgettable memories.", ["Sightseeing Included: Hot air balloon sunrise, valley tour, underground cities", "Overnight Stay: Cappadocia (Premium Cave Suites)", "Meals Included: Breakfast"]),
            _day(6, "Exploration & Leisure", "Explore the region's natural wonders and artisan workshops at a relaxed pace, perfect for family discovery.", ["Sightseeing Included: Artisan workshops and landscape exploration", "Overnight Stay: Cappadocia (Premium Cave Suites)", "Meals Included: Breakfast"]),
            _day(7, "Departure", "Final luxury breakfast before your TRAGUIN private transfer, completing your premium Turkey highlights expedition.", ["Sightseeing Included: Private airport transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Premium Luxury Boutique Hotels / similar", location="Istanbul", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Premium Cave Suites / similar", location="Cappadocia", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=2),
        ],
        inclusions=_tr004_inclusions(),
    )
    return package, itinerary


def _tr004_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="06 Nights in handpicked premium family hotels across Istanbul and Cappadocia", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private executive chauffeur-driven luxury ground transfers", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Domestic flight Istanbul–Cappadocia", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Istanbul cultural highlights tour, Grand Bazaar & Bosphorus cruise", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Cappadocia hot air balloon sunrise and underground city exploration", sort_order=5),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated on-ground family concierge support", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Turkey entry visa processing fees", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=10),
    ]


def build_tr_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="tr-005-grand-turkey-tour",
        serial_code="TR-005",
        traguin_tour_code="TRG-TUR-GRD-2026",
        destination_id=destination_id,
        title="Grand Turkey Tour",
        duration_label="09 Nights / 10 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=False,
        featured_sort_order=None,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Istanbul (3N) → Cappadocia (3N) → Coastal (3N) grand expedition", sort_order=1),
            PackageHighlightNested(text="Istanbul cultural highlights & Bosphorus discovery", sort_order=2),
            PackageHighlightNested(text="Cappadocia balloon sunrise, valleys & underground cities", sort_order=3),
            PackageHighlightNested(text="Ephesus ancient ruins & Mediterranean coastal leisure", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated luxury travel concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-TUR-GRD-2026 | Serial TR-005", sort_order=6),
        ],
        moods=["Family", "Luxury", "Cultural", "Adventure", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="tr-005-grand-turkey-itinerary",
        destination_id=destination_id,
        title="Grand Turkey Tour",
        duration_label="09 Nights / 10 Days",
        duration_days=10,
        starting_price=0,
        price_note="On Request (Premium Grand Turkey Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Istanbul • Cappadocia • Ephesus • Pamukkale • Antalya • Mediterranean Coast",
        overview=(
            "Discover the absolute best of Turkey with our TRAGUIN curated Grand Expedition. This comprehensive "
            "10-day journey covers the most iconic destinations—from the cultural heart of Istanbul and the mystical "
            "landscapes of Cappadocia to the ancient ruins and coastal beauty of the Mediterranean, ensuring "
            "unforgettable memories in ultimate comfort."
        ),
        seo_title="TR-005 | Grand Turkey Tour | TRAGUIN",
        seo_description=(
            "Premium 09 Nights / 10 Days Turkey grand package (TR-005): Istanbul, Cappadocia, Ephesus, "
            "Pamukkale, Antalya, and Mediterranean coastal charm."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Istanbul Cultural Highlights & Bosphorus Discovery", sort_order=1),
            ItineraryHighlightNested(text="Cappadocia Balloon Sunrise & Underground Cities", sort_order=2),
            ItineraryHighlightNested(text="Artisan & Landscape Discovery in Cappadocia", sort_order=3),
            ItineraryHighlightNested(text="Ephesus Ancient Ruins Guided Tour", sort_order=4),
            ItineraryHighlightNested(text="Coastal Leisure & Farewell Gala Dinner", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Istanbul", "Arrive in Istanbul. Private transfer to your handpicked premium hotel. Evening at leisure.", ["Sightseeing Included: VIP airport reception, private hotel transfer", "Overnight Stay: Istanbul (Premium Luxury Historic Hotel)", "Meals Included: Welcome arrangements on arrival"]),
            _day(2, "Istanbul Cultural Highlights", "Comprehensive city tour covering Istanbul's most famous landmarks, providing a rich educational experience.", ["Sightseeing Included: Istanbul cultural highlights city tour", "Overnight Stay: Istanbul (Premium Luxury Historic Hotel)", "Meals Included: Breakfast"]),
            _day(3, "Bosphorus & Bazaar Discovery", "Explore the Grand Bazaar and enjoy a Bosphorus cruise, showcasing the iconic attractions of Istanbul.", ["Sightseeing Included: Grand Bazaar visit, Bosphorus cruise", "Overnight Stay: Istanbul (Premium Luxury Historic Hotel)", "Meals Included: Breakfast"]),
            _day(4, "Flight to Cappadocia", "Travel to Cappadocia. Check into a luxury boutique cave hotel — an exclusive experience.", ["Sightseeing Included: Domestic flight to Cappadocia, private transfer to cave hotel", "Overnight Stay: Cappadocia (Premium Cave Suites)", "Meals Included: Breakfast"]),
            _day(5, "Cappadocia Adventure", "Sunrise hot air balloon flight. Followed by a tour of unique valleys and underground cities, creating unforgettable memories.", ["Sightseeing Included: Hot air balloon sunrise, valley tour, underground cities", "Overnight Stay: Cappadocia (Premium Cave Suites)", "Meals Included: Breakfast"]),
            _day(6, "Artisan & Landscape Discovery", "Explore artisan workshops and enjoy the breathtaking landscapes of Cappadocia at a relaxed, premium pace.", ["Sightseeing Included: Artisan workshops and landscape exploration", "Overnight Stay: Cappadocia (Premium Cave Suites)", "Meals Included: Breakfast"]),
            _day(7, "Flight to Coastal Paradise", "Transfer to airport for your flight to the coast. Check into a luxury coastal resort.", ["Sightseeing Included: Domestic flight to coast, VIP resort transfer", "Overnight Stay: Coastal (Luxury Coastal Resort)", "Meals Included: Breakfast"]),
            _day(8, "Ephesus & Ancient Ruins", "Guided exploration of the legendary Ephesus ruins. A must-see highlight of the Turkish coast.", ["Sightseeing Included: Ephesus ancient ruins guided tour", "Overnight Stay: Coastal (Luxury Coastal Resort)", "Meals Included: Breakfast"]),
            _day(9, "Coastal Leisure & Celebration", "Leisure at the resort, followed by a farewell dinner gala — celebrating your grand Turkey premium expedition.", ["Evening Experience: Farewell dinner gala", "Overnight Stay: Coastal (Luxury Coastal Resort)", "Meals Included: Breakfast & Farewell Dinner"]),
            _day(10, "Departure", "Final luxury breakfast before your TRAGUIN private transfer, completing your grand Turkey journey.", ["Sightseeing Included: Private airport transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Premium Luxury Historic Hotels / similar", location="Istanbul", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Premium Cave Suites / similar", location="Cappadocia", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=2),
            ItineraryHotelNested(name="Luxury Coastal Resort / similar", location="Coastal", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=3),
        ],
        inclusions=_tr005_inclusions(),
    )
    return package, itinerary


def _tr005_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="09 Nights in handpicked premium hotels across Istanbul, Cappadocia, and the coast", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private executive chauffeur-driven luxury ground transfers", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Domestic flights Istanbul–Cappadocia and Cappadocia–coast", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Istanbul cultural tour, Grand Bazaar & Bosphorus cruise", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Cappadocia hot air balloon sunrise and underground city exploration", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Ephesus ancient ruins guided tour", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated luxury travel concierge support", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Turkey entry visa processing fees", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=11),
    ]


TR_BUILDERS = [
    build_tr_001,
    build_tr_002,
    build_tr_003,
    build_tr_004,
    build_tr_005,
]
