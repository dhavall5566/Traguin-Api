"""Builder functions for KR-001 through KR-003 South Korea packages (no images)."""

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


def build_kr_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="kr-001-seoul-highlights-family-tour",
        destination_id=destination_id,
        title="Seoul Highlights Family Tour",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=51,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Seoul (5N) classic family expedition", sort_order=1),
            PackageHighlightNested(text="Gyeongbokgung Palace & Bukchon Hanok Village", sort_order=2),
            PackageHighlightNested(text="N Seoul Tower panoramic views & Myeongdong shopping", sort_order=3),
            PackageHighlightNested(text="Full-day Lotte World theme park adventure", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-SEO-FAM-2026 | Serial KR-001", sort_order=6),
        ],
        moods=["Family", "Luxury", "Cultural"],
    )
    itinerary = ItineraryCreate(
        slug="kr-001-seoul-highlights-itinerary",
        destination_id=destination_id,
        title="Seoul Highlights Family Tour",
        duration_label="05 Nights / 06 Days",
        duration_days=6,
        starting_price=0,
        price_note="On Request (Premium Seoul Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Gyeongbokgung Palace • N Seoul Tower • Myeongdong • Lotte World",
        overview=(
            "Discover the vibrant capital of South Korea with TRAGUIN's curated family expedition. From historic "
            "Gyeongbokgung Palace and iconic N Seoul Tower to the high-energy entertainment of Lotte World and "
            "the shopping delights of Myeongdong — unforgettable memories in the heart of Seoul."
        ),
        seo_title="KR-001 | Seoul Highlights Family Tour | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days Seoul family package (KR-001): Gyeongbokgung Palace, "
            "N Seoul Tower, Myeongdong, Lotte World, and Bukchon Hanok Village."
        ),
        is_featured=True,
        featured_sort_order=51,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Gyeongbokgung Palace & Royal Guard", sort_order=1),
            ItineraryHighlightNested(text="Bukchon Hanok Village", sort_order=2),
            ItineraryHighlightNested(text="N Seoul Tower Cable Car", sort_order=3),
            ItineraryHighlightNested(text="Lotte World Theme Park", sort_order=4),
        ],
        days=[
            _day(1, "Arrival in Seoul", "Arrive in Seoul. Private transfer to your handpicked premium hotel. Evening at leisure to experience the city's modern neon charm.", ["Sightseeing Included: VIP airport reception, private hotel transfer", "Overnight Stay: Seoul (Luxury City Hotel in Myeongdong)", "Meals Included: Welcome arrangements on arrival"]),
            _day(2, "Historic Palace Tour", "Visit the majestic Gyeongbokgung Palace. Witness the Changing of the Royal Guard and explore Bukchon Hanok Village — a must-see cultural highlight.", ["Sightseeing Included: Gyeongbokgung Palace, Changing of the Royal Guard, Bukchon Hanok Village", "Overnight Stay: Seoul (Luxury City Hotel in Myeongdong)", "Meals Included: Breakfast"]),
            _day(3, "Seoul Skyline & Shopping", "Take the cable car to N Seoul Tower for panoramic views. Spend the afternoon exploring the vibrant shopping streets of Myeongdong.", ["Sightseeing Included: N Seoul Tower cable car, Myeongdong shopping district", "Overnight Stay: Seoul (Luxury City Hotel in Myeongdong)", "Meals Included: Breakfast"]),
            _day(4, "Lotte World Adventure", "A full day of excitement at Lotte World, one of the world's largest indoor theme parks — a perfect family adventure experience.", ["Sightseeing Included: Lotte World full-day admission", "Overnight Stay: Seoul (Luxury City Hotel in Myeongdong)", "Meals Included: Breakfast"]),
            _day(5, "Cultural Exploration & Leisure", "A relaxed day exploring local culture, museums, or visiting traditional markets — enjoying the dynamic metropolis at your own pace.", ["Sightseeing Included: Leisure day for cultural exploration and traditional markets", "Overnight Stay: Seoul (Luxury City Hotel in Myeongdong)", "Meals Included: Breakfast"]),
            _day(6, "Departure", "Final luxury breakfast before your TRAGUIN private transfer to the airport, completing your premium Seoul highlights expedition.", ["Sightseeing Included: Private airport transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Luxury City Hotel in Myeongdong / similar", location="Seoul", nights_label="05 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=1),
        ],
        inclusions=_kr001_inclusions(),
    )
    return package, itinerary


def _kr001_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="05 Nights in handpicked premium luxury hotel in Seoul", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private executive chauffeur-driven luxury ground transfers", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Gyeongbokgung Palace, N Seoul Tower, and Lotte World sightseeing", sort_order=3),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated on-ground family concierge support", sort_order=4),
        ItineraryInclusionNested(kind="excluded", text="International airfare and South Korea entry visa processing fees", sort_order=5),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=8),
    ]


def build_kr_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="kr-002-romantic-korea-honeymoon",
        destination_id=destination_id,
        title="Romantic Korea Honeymoon",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=52,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Seoul (3N) → Jeju Island (2N) romantic K-drama circuit", sort_order=1),
            PackageHighlightNested(text="N Seoul Tower love padlock & Han River sunset yacht", sort_order=2),
            PackageHighlightNested(text="VIP Gyeongbokgung in Hanbok & Nami Island speedboat", sort_order=3),
            PackageHighlightNested(text="Seongsan Ilchulbong sunrise & Manjanggul lava cave", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 honeymoon concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRAGUIN-SEOUL-JEJU-ROMANCE | Serial KR-002", sort_order=6),
        ],
        moods=["Romantic", "Luxury", "Cultural", "Nature", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="kr-002-romantic-korea-itinerary",
        destination_id=destination_id,
        title="Romantic Korea Honeymoon",
        duration_label="05 Nights / 06 Days",
        duration_days=6,
        starting_price=0,
        price_note="On Request (Premium Tier)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Seoul • Nami Island • Jeju Island",
        overview=(
            "Step into a real-life K-drama narrative where cutting-edge luxury harmonizes with ancient traditions. "
            "From Seoul's neon skylines to Jeju's serene emerald shores — with private chauffeured sedan, handpicked "
            "luxury accommodations, fast-tracked entries, and TRAGUIN curated romantic experiences."
        ),
        seo_title="KR-002 | Romantic Korea Honeymoon | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days South Korea honeymoon (KR-002): Seoul, Nami Island, Jeju Island, "
            "Han River yacht, and Seongsan Ilchulbong sunrise."
        ),
        is_featured=True,
        featured_sort_order=52,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="N Seoul Tower Love Padlock Ceremony", sort_order=1),
            ItineraryHighlightNested(text="VIP Gyeongbokgung & Hanbok Experience", sort_order=2),
            ItineraryHighlightNested(text="Nami Island & Gangchon Rail-Bike", sort_order=3),
            ItineraryHighlightNested(text="Han River Private Sunset Yacht", sort_order=4),
            ItineraryHighlightNested(text="Jeju Seongsan Ilchulbong Sunrise", sort_order=5),
        ],
        days=[
            _day(1, "Seoul — Arrival & Seoul Sightseeing", "VIP meet at Incheon Airport with expedited immigration. Premium sedan to ultra-luxury Han River hotel. N Seoul Tower at dusk with custom TRAGUIN love padlock ceremony. Michelin-starred candlelit dinner.", ["Sightseeing Included: N Seoul Tower observation deck, Mt. Namsan cable car, Han River evening boardwalk", "Evening Experience: Love-lock ceremony at N Seoul Tower, fine-dining culinary showcase", "Overnight Stay: Seoul (Signiel Seoul / Four Seasons Seoul)", "Meals Included: Welcome Premium Dinner"]),
            _day(2, "Seoul — Dynastic Majesty & K-Culture Immersion", "VIP tour of Gyeongbokgung Palace in premium silk Hanboks. Bukchon Hanok Village stroll. VIP shopping in Gangnam and Apgujeong Rodeo Street.", ["Sightseeing Included: Gyeongbokgung Palace VIP access, Bukchon Hanok Village, Insadong, Gangnam", "Evening Experience: Private sunset yacht charter on Han River with wine and live acoustic music", "Overnight Stay: Seoul (Signiel Seoul / Four Seasons Seoul)", "Meals Included: Gourmet Breakfast & Luxury Korean BBQ Lunch"]),
            _day(3, "Nami Island — Enchanted Romance", "Scenic drive to Nami Island via private speedboat. Metasequoia tree paths. Gangchon romantic rail-bike experience. Craft cocktails on Lotte World Tower 100th floor.", ["Sightseeing Included: Nami Island eco-reserve, Metasequoia Lane, Gangchon rail-bike, private speedboat transfers", "Evening Experience: High-altitude craft cocktail session at Lotte World Tower", "Overnight Stay: Seoul (Signiel Seoul / Four Seasons Seoul)", "Meals Included: Gourmet Breakfast & Chuncheon Dakgalbi Lakeside Lunch"]),
            _day(4, "Seoul to Jeju Island — Coastal Romance", "Premium domestic flight to Jeju. Luxury SUV along Aewol Coastal Road. Cheonjiyeon Waterfall and Jungmun Saekdal Beach sunset stroll.", ["Sightseeing Included: Aewol scenic coastal road, Cheonjiyeon waterfall, Jungmun beach walk", "Evening Experience: Exquisite seafood fine-dining with private chef on the beach", "Overnight Stay: Jeju Island (Grand Hyatt Jeju / Shilla Jeju Luxury Pool Villa)", "Meals Included: Gourmet Breakfast & Premium Coastal Fusion Dinner"]),
            _day(5, "Jeju Island — Volcanic Wonders & Sunrise Serenade", "Early sunrise at UNESCO Seongsan Ilchulbong. Manjanggul lava cave. O'sulloc Green Tea Plantation with private skincare workshop.", ["Sightseeing Included: Seongsan Ilchulbong sunrise peak, Manjanggul UNESCO lava cave, O'sulloc tea plantation", "Evening Experience: Farewell premium beachside campfire luxury barbecue with curated wines", "Overnight Stay: Jeju Island (Grand Hyatt Jeju / Shilla Jeju Luxury Pool Villa)", "Meals Included: Gourmet Breakfast, Jeju Black Pork Lunch & Farewell Wine Dinner"]),
            _day(6, "Jeju to Seoul — Farewell", "Final breakfast overlooking the ocean. Dongmun Traditional Market for souvenirs. Flight to Incheon for international departure.", ["Sightseeing Included: Dongmun Traditional Market, Jeju duty-free lounge access", "Meals Included: Gourmet Breakfast served in-villa"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Lotte Hotel Seoul / similar", location="Seoul", nights_label="03 Nights", category_label="Deluxe", meal_plan="Daily Buffet Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Maison Glad Jeju / similar", location="Jeju Island", nights_label="02 Nights", category_label="Deluxe", meal_plan="Daily Buffet Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="The Shilla Seoul", location="Seoul", nights_label="03 Nights", category_label="Premium", meal_plan="Executive Lounge Access", stars=5, sort_order=3),
            ItineraryHotelNested(name="Parnas Hotel Jeju", location="Jeju Island", nights_label="02 Nights", category_label="Premium", meal_plan="Curated Breakfast", stars=5, sort_order=4),
            ItineraryHotelNested(name="Four Seasons Hotel Seoul", location="Seoul", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="Grand Hyatt Jeju", location="Jeju Island", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="Signiel Seoul", location="Seoul", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="The Shilla Jeju Luxury Private Pool Villa", location="Jeju Island", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=8),
        ],
        inclusions=_kr002_inclusions(),
    )
    return package, itinerary


def _kr002_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="05 Nights in top-tier luxury accommodations across Seoul and Jeju", sort_order=1),
        ItineraryInclusionNested(kind="included", text="VIP entry to all palaces and monuments mentioned in the itinerary", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Private air-conditioned luxury sedan throughout", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Return premium domestic flights between Seoul and Jeju Island", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Daily luxury breakfasts and designated fine-dining experiences", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Complimentary champagne, love padlocks, and fresh local fruits on arrival", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated on-ground client care and assistance", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="International roundtrip airfares", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="South Korea tourist visa application charges", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, premium drinks, and tips", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Optional activities and travel insurance", sort_order=11),
    ]


def build_kr_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="kr-003-south-korea-luxury-tour",
        destination_id=destination_id,
        title="South Korea Luxury Tour",
        duration_label="06 Nights / 07 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=53,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Seoul (2N) → Gyeongju (1N) → Busan (1N) → Jeju (2N) luxury circuit", sort_order=1),
            PackageHighlightNested(text="VIP Hanbok Gyeongbokgung & Han River sunset yacht", sort_order=2),
            PackageHighlightNested(text="Bulguksa Temple, Gamcheon Village & Busan catamaran", sort_order=3),
            PackageHighlightNested(text="Jeju volcanic wonders & Haenyeo diver experience", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated concierge assistance", sort_order=5),
            PackageHighlightNested(text="Tour code TRAGUIN-K luxury-003 | Serial KR-003", sort_order=6),
        ],
        moods=["Luxury", "Family", "Cultural", "Nature", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="kr-003-south-korea-luxury-itinerary",
        destination_id=destination_id,
        title="South Korea Luxury Tour",
        duration_label="06 Nights / 07 Days",
        duration_days=7,
        starting_price=0,
        price_note="On Request (Premium FIT)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Seoul • Gyeongju • Busan • Jeju Island",
        overview=(
            "An extraordinary exploration curated by TRAGUIN — where hyper-modern skylines blend with ancient "
            "dynastic traditions. Premium FIT itinerary connecting Seoul, Gyeongju, Busan, and Jeju Island with "
            "private executive MPV, five-star accommodations, and TRAGUIN curated experiences."
        ),
        seo_title="KR-003 | South Korea Luxury Tour | TRAGUIN",
        seo_description=(
            "Luxury 06 Nights / 07 Days South Korea package (KR-003): Seoul, Gyeongju, Busan, Jeju Island, "
            "KTX first class, Han River yacht, and Busan catamaran cruise."
        ),
        is_featured=True,
        featured_sort_order=53,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="VIP Incheon Fast-Track Arrival", sort_order=1),
            ItineraryHighlightNested(text="Gyeongbokgung Palace Private Hanbok Walk", sort_order=2),
            ItineraryHighlightNested(text="Bulguksa Temple & Wolji Pond Illumination", sort_order=3),
            ItineraryHighlightNested(text="Busan Catamaran & Gwangan Bridge", sort_order=4),
            ItineraryHighlightNested(text="Jeju Seongsan Ilchulbong & Haenyeo Experience", sort_order=5),
        ],
        days=[
            _day(1, "Seoul — Grand Arrival & Ultra-Luxury Welcome", "VIP airport concierge at jet bridge with fast-track immigration. Luxury sedan along Han River. Evening drive to Namsan Seoul Tower for panoramic city views. Welcome dinner at Michelin-starred Gaon.", ["Sightseeing Included: Incheon VIP fast-track, Namsan Tower view", "Evening Experience: Welcome dinner at Michelin-starred Gaon", "Overnight Stay: Seoul (Signiel Seoul — Ultra Luxury)", "Meals Included: Welcome Drink & Dinner"]),
            _day(2, "Seoul — Dynastic Majesty & Immersive K-Culture", "Private early-access Gyeongbokgung Palace walk in custom Hanboks. Bukchon Hanok Village and Insadong. Private K-Pop dance masterclass or Samsung Innovation Museum. Premium tea blending ceremony.", ["Sightseeing Included: Gyeongbokgung Palace, Bukchon Hanok Village, Insadong", "Evening Experience: Han River luxury sunset yacht cruise", "Overnight Stay: Seoul (Signiel Seoul — Ultra Luxury)", "Meals Included: Breakfast"]),
            _day(3, "Gyeongju — The Ancient Kingdom of Shilla", "First-class KTX bullet train to Gyeongju. UNESCO Bulguksa Temple and Seokguram Grotto. Daereungwon Tomb Complex. Evening illumination of Donggung Palace and Wolji Pond.", ["Sightseeing Included: Bulguksa Temple, Daereungwon, Wolji Pond illumination", "Evening Experience: Starlight walk by Cheomseongdae Observatory", "Overnight Stay: Gyeongju (Lahan Select — Premium Lake View)", "Meals Included: Breakfast"]),
            _day(4, "Busan — Maritime Grandeur & Coastal Sophistication", "Haedong Yonggungsa Temple on ocean cliffs. Gamcheon Culture Village. Haeundae Blueline Park sky capsules. Private luxury catamaran from Suyeongman Marina under Gwangan Diamond Bridge.", ["Sightseeing Included: Haedong Yonggungsa, Gamcheon Culture Village, Haeundae Blueline Park", "Evening Experience: Private catamaran yacht cruise with fireworks", "Overnight Stay: Busan (Park Hyatt Busan — Ocean View Suite)", "Meals Included: Breakfast"]),
            _day(5, "Jeju Island — Volcanic Wonders & Pristine Nature", "Premium flight to Jeju. Seongsan Ilchulbong sunrise peak. Manjanggul lava tunnel. Exclusive Haenyeo female diver experience with freshly caught seafood on shore.", ["Sightseeing Included: Seongsan Ilchulbong, Manjanggul cave, Haenyeo experience", "Evening Experience: Traditional black pork BBQ fine dining", "Overnight Stay: Jeju Island (The Shilla Jeju — Luxury Resort)", "Meals Included: Breakfast"]),
            _day(6, "Jeju Island — Tea Plantations & Majestic Waterfalls", "Osulloc Tea Museum and green tea fields with private tea-stone class. Cheonjiyeon Waterfall and Jusangjeolli Cliff hexagonal rock formations. TRAGUIN premium family farewell dinner.", ["Sightseeing Included: Osulloc Tea Museum, Cheonjiyeon Falls, Jusangjeolli Cliff", "Evening Experience: Exclusive multi-course royal court farewell dinner", "Overnight Stay: Jeju Island (The Shilla Jeju — Luxury Resort)", "Meals Included: Breakfast"]),
            _day(7, "Departure — End of a Luxury Odyssey", "Leisurely breakfast at luxury resort. Private chauffeur to Jeju International Airport for domestic flight to Seoul Incheon connecting with international departure.", ["Sightseeing Included: Private departure transfer to Jeju airport", "Meals Included: Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Lotte Hotel Seoul (Superior) / similar", location="Seoul", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Commodore Hotel Gyeongju / similar", location="Gyeongju", nights_label="01 Night", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="Avani Central Busan / similar", location="Busan", nights_label="01 Night", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=3),
            ItineraryHotelNested(name="Grand Hyatt Jeju / similar", location="Jeju Island", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=5, sort_order=4),
            ItineraryHotelNested(name="Four Seasons Seoul", location="Seoul", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="Lahan Select Gyeongju (Lake View)", location="Gyeongju", nights_label="01 Night", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="Ananti at Busan Cove", location="Busan", nights_label="01 Night", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="Parnas Hotel Jeju", location="Jeju Island", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=8),
            ItineraryHotelNested(name="The Shilla Seoul", location="Seoul", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=9),
            ItineraryHotelNested(name="Park Hyatt Busan (Ocean View)", location="Busan", nights_label="01 Night", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=10),
            ItineraryHotelNested(name="The Shilla Jeju (Terrace)", location="Jeju Island", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=11),
            ItineraryHotelNested(name="Signiel Seoul (Premier Suite)", location="Seoul", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=12),
            ItineraryHotelNested(name="The Shilla Jeju (Grand Suite)", location="Jeju Island", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=13),
        ],
        inclusions=_kr003_inclusions(),
    )
    return package, itinerary


def _kr003_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="06 Nights in ultra-luxury handpicked hotels across Seoul, Gyeongju, Busan, and Jeju", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Dedicated private executive MPV (Kia Carnival or similar) throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="KTX high-speed train first-class tickets (Seoul to Gyeongju)", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Han River sunset yacht and Busan catamaran cruises", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Professional English-speaking elite guides for all sightseeing", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Custom VIP arrival kit and traditional welcome gifts", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated concierge assistance line", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="International and domestic flight tickets", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="K-ETA or South Korea entry visa processing", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, mini-bar, and unspecified meals", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Gratuities and comprehensive travel insurance", sort_order=11),
    ]


KR_BUILDERS = [
    build_kr_001,
    build_kr_002,
    build_kr_003,
]
