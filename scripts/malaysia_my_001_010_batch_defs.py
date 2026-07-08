"""Builder functions for MY-001 through MY-010 Malaysia international packages."""

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

MALAYSIA_SLUG = "malaysia"


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


def _hotel(
    name: str,
    location: str,
    nights_label: str,
    category_label: str,
    room_type: str,
    meal_plan: str,
    stars: int,
    sort_order: int,
    description: str | None = None,
) -> ItineraryHotelNested:
    return ItineraryHotelNested(
        name=name,
        location=location,
        nights_label=nights_label,
        description=description or f"Option {sort_order:02d} — {category_label} tier handpicked property.",
        stars=stars,
        category_label=category_label,
        room_type=room_type,
        meal_plan=meal_plan,
        sort_order=sort_order,
    )


def _inc_included(text: str, sort_order: int) -> ItineraryInclusionNested:
    return ItineraryInclusionNested(kind="included", text=text, sort_order=sort_order)


def _inc_excluded(text: str, sort_order: int) -> ItineraryInclusionNested:
    return ItineraryInclusionNested(kind="excluded", text=text, sort_order=sort_order)


def _ih(text: str, sort_order: int) -> ItineraryHighlightNested:
    return ItineraryHighlightNested(text=text, sort_order=sort_order)


def _ph(text: str, sort_order: int) -> PackageHighlightNested:
    return PackageHighlightNested(text=text, sort_order=sort_order)


def _duration_days(duration_label: str) -> int:
    return int(duration_label.split("/")[-1].strip().split()[0])


def build_my_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MY-001'
    tour_code = 'TRG-KUL-GEN-FAM-2026'
    title = 'Kuala Lumpur Genting Family Tour'
    duration = '04 Nights / 05 Days'
    slug = 'my-001-kuala-lumpur-genting-family-tour'
    itin_slug = 'my-001-kuala-lumpur-genting-itinerary'
    package = PackageCreate(
        slug=slug,
        serial_code=serial,
        traguin_tour_code=tour_code,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        price=0,
        rating=Decimal("4.9"),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ph('Serial code MY-001 | TRAGUIN tour code TRG-KUL-GEN-FAM-2026', 1),
            _ph('Country: Malaysia, Asia | Category: Best Kuala Lumpur Genting Family Tour Package', 2),
            _ph('Destinations: Kuala Lumpur (2N) +', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Family', 'Luxury', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Malaysia Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Kuala Lumpur Genting Family Tour',
        overview='Kuala Lumpur • Petronas Towers • Genting Highlands • Theme Parks 04 Nights / 05 Days Classic Malaysia Family Holiday SERIAL CODE: MY-001 TRAGUIN TOUR CODE: TRG-KUL-GEN-FAM-2026 STATE / COUNTRY: Malaysia CATEGORY: Best Kuala Lumpur Genting Family Tour Package DURATION: 04 Nights / 05 Days DESTINATIONS: Kuala Lumpur (2N) + Genting Highlands (2N) IDEAL FOR: Families, Couples, Theme Park EnthusiastsBEST SEASON: Year-Round (Best during school holidays) Dive into an exhilarating family escapade with the Best Kuala Lumpur Genting Tour Package, masterfully curated by TRAGUIN to perfectly bridge city sophistication with mountain-top thrill. From iconic metropolitan landmarks to world-class theme parks, discover breathtaking landscapes and create unforgettable memories on this premier Luxury Malaysia Holiday.\n\nTOUR OVERVIEW\nWelcome to your bespoke Kuala Lumpur & Genting Highlands Family Vacation, a holiday structured explicitly for families who command seamless coordination, children-friendly exploration, and elite hospitality. Across 5 wonderful days, your family will explore the finest metropolitan marvels, mountain retreats, and entertainment centers of Malaysia. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='MY-001 | Kuala Lumpur Genting Family Tour | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Malaysia package (MY-001 / TRG-KUL-GEN-FAM-2026): Kuala Lumpur (2N) + with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN KUALA LUMPUR & CITY LIGHTS', 1),
            _ih('Day 02: KUALA LUMPUR CULTURAL EXPEDITION', 2),
            _ih('Day 03: GENTING HIGHLANDS ESCAPE', 3),
            _ih('Day 04: THE ULTIMATE THEME PARK DAY', 4),
            _ih('Day 05: DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN KUALA LUMPUR & CITY LIGHTS',
                (
                    'THE GARDEN CITY WELCOME – PETRONAS TOWERS TWILIGHT Your Kuala Lumpur family tour begins perfectly as you arrive at KL International Airport. Receive a warm greeting coordinated seamlessly by your TRAGUIN representative. Step into your private luxury van for a scenic transfer to your premium hotel. In the evening, visit the iconic Petronas Twin Towers for breathtaking landscape views of the city skyline. Sightseeing: Petronas Twin Towers observation deck, KL city skyline drive. Stay: Kuala Lumpur (Premium City Hotel)'
                ),
                [
                    'Meals: Welcome Family Dinner',
                ],
            ),
            _day(
                2,
                'KUALA LUMPUR CULTURAL EXPEDITION',
                (
                    'HISTORIC MARVELS – BATU CAVES & METROPOLITAN VIBES Explore the majestic Batu Caves, featuring iconic attractions like the towering golden statue. Afterward, visit the historic Merdeka Square and enjoy a curated city shopping experience. Conclude the day with immersive experiences at local cultural landmarks. Sightseeing: Batu Caves, Merdeka Square, local handicraft market. Stay: Kuala Lumpur (Premium City Hotel)'
                ),
                [
                    'Meals: Breakfast, Local Lunch',
                ],
            ),
            _day(
                3,
                'GENTING HIGHLANDS ESCAPE',
                (
                    'MOUNTAIN THRILLS – CABLE CAR VISTAS & COOL HIGHLAND AIR Transfer to the cool heights of Genting Highlands via a scenic cable car ride. Enjoy breathtaking landscapes as you ascend. Spend the afternoon exploring the indoor and outdoor theme parks, providing endless fun for the family. Sightseeing: Awana SkyWay cable car, Genting Theme Park entry. Stay: Genting Highlands (Handpicked Resort)'
                ),
                [
                    'Meals: Breakfast, Buffet Dinner',
                ],
            ),
            _day(
                4,
                'THE ULTIMATE THEME PARK DAY',
                (
                    'UNFORGETTABLE MEMORIES – ACTION, ADVENTURE & ENTERTAINMENT A full day of immersive fun at Genting’s integrated entertainment hubs. Explore world-class rides and iconic attractions. In the evening, enjoy a grand finale dinner overlooking the mountain valleys. Sightseeing: Full day theme park exploration. Stay: Genting Highlands (Handpicked Resort)'
                ),
                [
                    'Meals: Breakfast, Farewell Family Dinner',
                ],
            ),
            _day(
                5,
                'DEPARTURE',
                (
                    'CHERISHING MEMORIES – DEPARTURE FROM MALAYSIA Enjoy a final morning breakfast before your luxury transfer back to KL International Airport. Your premium Malaysia family tour concludes, leaving you with unforgettable memories crafted by TRAGUIN. Sightseeing: Last-minute souvenir shopping at KL Airport Duty Free.'
                ),
                [
                    'Meals: Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Impiana KLCC First World Hotel',
                'Malaysia',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Impiana KLCC First World Hotel',
            ),
            _hotel(
                'Berjaya Times Square Resorts World Genting',
                'Multi-city Malaysia',
                '4N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Berjaya Times Square Resorts World Genting',
            ),
            _hotel(
                'Shangri-La Kuala Lumpur Crockfords',
                'Malaysia',
                '4N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Shangri-La Kuala Lumpur Crockfords',
            ),
            _hotel(
                'The St. Regis KL Resorts World Genting Suites',
                'Multi-city Malaysia',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — The St. Regis KL Resorts World Genting Suites',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Malaysia', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('Domestic flights and inter-city transfers as per curated itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Malaysia visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_my_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MY-002'
    tour_code = 'TRG-MAL-DIS-2026'
    title = 'Malaysia Discovery Family Tour'
    duration = '05 Nights / 06 Days'
    slug = 'my-002-malaysia-discovery-family-tour'
    itin_slug = 'my-002-malaysia-discovery-itinerary'
    package = PackageCreate(
        slug=slug,
        serial_code=serial,
        traguin_tour_code=tour_code,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        price=0,
        rating=Decimal("4.9"),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ph('Serial code MY-002 | TRAGUIN tour code TRG-MAL-DIS-2026', 1),
            _ph('Country: Malaysia, Asia | Category: Best Malaysia Discovery Family Tour', 2),
            _ph('Destinations: Kuala Lumpur (3N) +', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Family', 'Luxury', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Malaysia Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Malaysia Discovery Family Tour',
        overview="Kuala Lumpur • Batu Caves • Genting Highlands • Putrajaya 05 Nights / 06 Days Classic Malaysia Family Holiday SERIAL CODE: MY-002 TRAGUIN TOUR CODE: TRG-MAL-DIS-2026 STATE / COUNTRY: Malaysia CATEGORY: Best Malaysia Discovery Family Tour DURATION: 05 Nights / 06 Days DESTINATIONS: Kuala Lumpur (3N) + Genting Highlands (2N)\n\nTOUR OVERVIEW\nDiscover the rich heritage and modern wonders of Malaysia with this TRAGUIN curated family itinerary. Designed for comfort and excitement, this Malaysia Discovery package offers a flawless blend of city exploration and highland adventure. Experience the best of Malaysian hospitality with TRAGUIN's handpicked hotels and exclusive services. THE IMMERSIVE DAY-WISE ITINERARY",
        seo_title='MY-002 | Malaysia Discovery Family Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Malaysia package (MY-002 / TRG-MAL-DIS-2026): Kuala Lumpur (3N) + with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN KUALA LUMPUR', 1),
            _ih('Day 02: KUALA LUMPUR EXPLORATION', 2),
            _ih('Day 03: GENTING HIGHLANDS ADVENTURE', 3),
            _ih('Day 04: GENTING HIGHLANDS LEISURE', 4),
            _ih('Day 05: PUTRAJAYA & RETURN TO KL', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN KUALA LUMPUR',
                (
                    'THE GARDEN CITY WELCOME – CITY OF LIGHTS Arrive in Kuala Lumpur, the vibrant capital city. Your private TRAGUIN transfer will escort you to your premium hotel. Spend the evening enjoying the breathtaking landscapes of the city skyline from the KL Tower. Sightseeing: KL Tower observation deck, city orientation. Stay: Kuala Lumpur (Premium Hotel)'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'KUALA LUMPUR EXPLORATION',
                (
                    "ICONIC ATTRACTIONS – PETRONAS TOWERS & BATU CAVES Visit the world-famous Petronas Twin Towers and the iconic Batu Caves. This curated experience offers deep insights into Malaysia's cultural diversity. Enjoy shopping and local food in the vibrant city center. Sightseeing: Petronas Towers, Batu Caves, Merdeka Square. Stay: Kuala Lumpur (Premium Hotel)"
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'GENTING HIGHLANDS ADVENTURE',
                (
                    "MOUNTAIN RETREAT – CABLE CAR VISTAS & THEME PARKS Head towards Genting Highlands. Experience a scenic cable car ride offering breathtaking landscapes. Spend time in the integrated theme parks—a highlight of TRAGUIN's exclusive packages. Sightseeing: Awana SkyWay, Indoor/Outdoor Theme Parks. Stay: Genting Highlands (Handpicked Hotel)"
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'GENTING HIGHLANDS LEISURE',
                (
                    "UNFORGETTABLE MEMORIES – RELAXATION & FAMILY FUN A full day dedicated to leisure and adventure. Explore Genting's exclusive experiences, including shopping malls, cinemas, and entertainment venues. Relax and enjoy the cool mountain weather with your family. Sightseeing: Genting SkyWorlds Theme Park. Stay: Genting Highlands (Handpicked Hotel)"
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'PUTRAJAYA & RETURN TO KL',
                (
                    "SCENIC BEAUTY – ADMINISTRATIVE CAPITAL & FAREWELL Visit Putrajaya, the administrative capital, featuring stunning architecture. Transfer back to Kuala Lumpur for your final evening of shopping and dining, celebrating the trip of a lifetime. Sightseeing: Putrajaya Mosque, Prime Minister's Office view. Stay: Kuala Lumpur (Premium Hotel)"
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Kuala Lumpur (3N) +',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: TRAGUIN Handpicked Deluxe Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Kuala Lumpur (3N) +',
                '5N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: TRAGUIN Handpicked Premium Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Luxury Property',
                'Kuala Lumpur (3N) +',
                '5N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Kuala Lumpur (3N) +',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Malaysia', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('Domestic flights and inter-city transfers as per curated itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Malaysia visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_my_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MY-003'
    tour_code = 'TRG-KUL-LGK-FAM-2026'
    title = 'Kuala Lumpur Langkawi Family Tour'
    duration = '05 Nights / 06 Days'
    slug = 'my-003-kuala-lumpur-langkawi-family-tour'
    itin_slug = 'my-003-kuala-lumpur-langkawi-itinerary'
    package = PackageCreate(
        slug=slug,
        serial_code=serial,
        traguin_tour_code=tour_code,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        price=0,
        rating=Decimal("4.9"),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ph('Serial code MY-003 | TRAGUIN tour code TRG-KUL-LGK-FAM-2026', 1),
            _ph('Country: Malaysia, Asia | Category: Best Kuala Lumpur Langkawi Family Tour', 2),
            _ph('Destinations: Kuala Lumpur • Petronas Towers • Langkawi Island • SkyBridge • Mangrove Cruises', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Family', 'Luxury', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Malaysia Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Kuala Lumpur Langkawi Family Tour',
        overview='Kuala Lumpur • Petronas Towers • Langkawi Island • SkyBridge • Mangrove Cruises 05 Nights / 06 Days Classic Malaysia Family Expedition SERIAL CODE: MY-003 TRAGUIN TOUR CODE: TRG-KUL-LGK-FAM-2026 STATE / COUNTRY: Malaysia CATEGORY: Best Kuala Lumpur Langkawi Family Tour DURATION: 05 Nights / 06 Days Kuala Lumpur (2N) + Langkawi (3N) IDEAL FOR: Families, Couples, Nature Enthusiasts Year-Round\n\nTOUR OVERVIEW\nDiscover the perfect synergy of vibrant city life and tranquil island beauty with our TRAGUIN curated Malaysia expedition. From the iconic towers of Kuala Lumpur to the pristine white sands of Langkawi, this 6-day journey is designed to create unforgettable memories for your family. THE DEFINITIVE DAY-WISE ITINERARY',
        seo_title='MY-003 | Kuala Lumpur Langkawi Family Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Malaysia package (MY-003 / TRG-KUL-LGK-FAM-2026): Kuala Lumpur • Petronas Towers • Langkawi Island • SkyBridge • Mangrove Cruises with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN KUALA LUMPUR', 1),
            _ih('Day 02: KUALA LUMPUR EXPLORATION', 2),
            _ih('Day 03: FLY TO LANGKAWI', 3),
            _ih('Day 04: LANGKAWI ISLAND DISCOVERY', 4),
            _ih('Day 05: MANGROVE & MARINE EXPEDITION', 5),
            _ih('Day 06: DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN KUALA LUMPUR',
                (
                    'Arrive in the heart of Malaysia. Your TRAGUIN private chauffeur will meet you at the airport for a seamless transfer. Spend the evening enjoying the breathtaking landscapes of the city from the observation deck of the iconic Petronas Towers.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'KUALA LUMPUR EXPLORATION',
                (
                    'Explore the cultural pulse of Kuala Lumpur. Visit Batu Caves, a spiritual site of immense scenic beauty, followed by a city tour featuring Merdeka Square and local craft markets.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'FLY TO LANGKAWI',
                (
                    'Transfer to the airport for your flight to the jewel of Kedah, Langkawi. Upon arrival, check into your premium stay and enjoy a relaxing sunset walk on the beach.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'LANGKAWI ISLAND DISCOVERY',
                (
                    'Experience the iconic attractions of Langkawi, including the famous SkyBridge accessible via the SkyCab. Enjoy breathtaking landscapes and immersive experiences exploring the unique geological wonders of this island paradise.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'MANGROVE & MARINE EXPEDITION',
                (
                    "A curated experience exploring Langkawi's mangroves and pristine marine life. Encounter scenic beauty on this guided boat adventure perfect for the whole family."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'DEPARTURE',
                (
                    'Conclude your Malaysian adventure with last-minute shopping before your flight, taking with you a wealth of unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Impiana KLCC Adya Hotel',
                'Malaysia',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Impiana KLCC Adya Hotel',
            ),
            _hotel(
                'Berjaya Times Square Pelangi Beach Resort',
                'Multi-city Malaysia',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Berjaya Times Square Pelangi Beach Resort',
            ),
            _hotel(
                'Shangri-La KL The Westin Langkawi',
                'Malaysia',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Shangri-La KL The Westin Langkawi',
            ),
            _hotel(
                'The St. Regis KL The Datai Langkawi',
                'Multi-city Malaysia',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — The St. Regis KL The Datai Langkawi',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Malaysia', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('Domestic flights and inter-city transfers as per curated itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Malaysia visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_my_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MY-004'
    tour_code = 'TRG-LGK-ROM-2026'
    title = 'Langkawi Romance Package'
    duration = '04 Nights / 05 Days'
    slug = 'my-004-langkawi-romance-package'
    itin_slug = 'my-004-langkawi-romance-itinerary'
    package = PackageCreate(
        slug=slug,
        serial_code=serial,
        traguin_tour_code=tour_code,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        price=0,
        rating=Decimal("4.9"),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ph('Serial code MY-004 | TRAGUIN tour code TRG-LGK-ROM-2026', 1),
            _ph('Country: Malaysia, Asia | Category: Best Langkawi Honeymoon Package', 2),
            _ph('Destinations: Langkawi (4 Nights', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Honeymoon', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Malaysia Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Langkawi Romance Package',
        overview='Langkawi Island • SkyBridge • Kilim Geoforest • Sunset Yacht Cruise 04 Nights / 05 Days Ultra-Luxury Honeymoon Retreat SERIAL CODE: MY-004 TRAGUIN TOUR CODE: TRG-LGK-ROM-2026 STATE / COUNTRY: Malaysia CATEGORY: Best Langkawi Honeymoon Package DURATION: 04 Nights / 05 Days DESTINATIONS: Langkawi (4 Nights Luxury Beachfront Stay)\n\nTOUR OVERVIEW\nEscape into tranquility with our Langkawi Romance getaway, a masterfully crafted TRAGUIN experience designed for couples seeking intimate moments. Nestled in a breathtaking archipelago, Langkawi offers the ultimate setting for romance with scenic beauty, handpicked hotels, and curated experiences that guarantee unforgettable memories. THE LANGKAWI ROMANCE EXPERIENCE Langkawi is the jewel of Malaysia, a paradise of turquoise waters and lush rainforests. Known for its iconic SkyBridge, world-class luxury resorts, and romantic sunset yacht cruises, Langkawi is the ultimate destination for couples. Experience exclusive experiences like private island picnics and serene mangrove explorations in this Luxury Langkawi Holiday. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='MY-004 | Langkawi Romance Package | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Malaysia package (MY-004 / TRG-LGK-ROM-2026): Langkawi (4 Nights with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN LANGKAWI', 1),
            _ih('Day 02: HIGHLAND VISTAS & SKYBRIDGE', 2),
            _ih('Day 03: MANGROVE & GEOFOREST EXPLORATION', 3),
            _ih('Day 04: SUNSET YACHT CRUISE', 4),
            _ih('Day 05: DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN LANGKAWI',
                (
                    'Arrive in Langkawi, where your TRAGUIN concierge greets you for a private transfer to your resort. Enjoy a sunset welcome at your beachfront villa and prepare for a romantic trip ahead.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'HIGHLAND VISTAS & SKYBRIDGE',
                (
                    'Explore breathtaking landscapes via the SkyCab cable car. Walk across the iconic SkyBridge for unparalleled scenic beauty and panoramic island views.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'MANGROVE & GEOFOREST EXPLORATION',
                (
                    'Embark on a private boat journey through the Kilim Geoforest Park. Immersive experiences await as you explore secret caves, hidden lagoons, and diverse wildlife.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'SUNSET YACHT CRUISE',
                (
                    'Indulge in a curated sunset yacht cruise, watching the horizon transform into golden hues. A truly iconic attraction and the perfect romantic end to your Langkawi Honeymoon Package.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'DEPARTURE',
                (
                    'Enjoy a leisurely morning breakfast before your private transfer to the airport. Depart Langkawi with unforgettable memories crafted by TRAGUIN.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Adya Hotel Langkawi',
                'Malaysia',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Adya Hotel Langkawi',
            ),
            _hotel(
                'Pelangi Beach Resort & Spa',
                'Malaysia',
                '4N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Pelangi Beach Resort & Spa',
            ),
            _hotel(
                'The Westin Langkawi',
                'Malaysia',
                '4N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Westin Langkawi',
            ),
            _hotel(
                'The Datai Langkawi',
                'Malaysia',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — The Datai Langkawi',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Malaysia', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('Domestic flights and inter-city transfers as per curated itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Malaysia visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_my_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MY-005'
    tour_code = 'TRG-MAL-LUX-2026'
    title = 'Malaysia Luxury Tour'
    duration = '06 Nights / 07 Days'
    slug = 'my-005-malaysia-luxury-tour'
    itin_slug = 'my-005-malaysia-luxury-itinerary'
    package = PackageCreate(
        slug=slug,
        serial_code=serial,
        traguin_tour_code=tour_code,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        price=0,
        rating=Decimal("4.9"),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ph('Serial code MY-005 | TRAGUIN tour code TRG-MAL-LUX-2026', 1),
            _ph('Country: Malaysia, Asia | Category: Luxury Malaysia Discovery', 2),
            _ph('Destinations: Kuala Lumpur (2N) +', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Malaysia Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Malaysia Luxury Tour',
        overview='06 Nights / 07 Days Ultimate Luxury Malaysia Discovery SERIAL CODE: MY-005 TRAGUIN TOUR CODE: TRG-MAL-LUX-2026 STATE / COUNTRY: Malaysia CATEGORY: Luxury Malaysia Discovery DURATION: 06 Nights / 07 Days DESTINATIONS: Kuala Lumpur (2N) + Cameron Highlands (2N) + Langkawi (2N)\n\nTOUR OVERVIEW\nIndulge in a journey of pure elegance with this TRAGUIN curated luxury Malaysia tour. From the soaring skyscrapers of Kuala Lumpur to the misty tea plantations of Cameron Highlands and the pristine beaches of Langkawi, this luxury Malaysia holiday promises unforgettable memories. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='MY-005 | Malaysia Luxury Tour | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Malaysia package (MY-005 / TRG-MAL-LUX-2026): Kuala Lumpur (2N) + with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN KUALA LUMPUR', 1),
            _ih('Day 02: KUALA LUMPUR TO CAMERON HIGHLANDS', 2),
            _ih('Day 03: CAMERON HIGHLANDS EXPLORATION', 3),
            _ih('Day 04: FLY TO LANGKAWI', 4),
            _ih('Day 05: LANGKAWI ISLAND LUXURY', 5),
            _ih('Day 06: LANGKAWI LEISURE', 6),
            _ih('Day 07: DEPARTURE', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN KUALA LUMPUR',
                (
                    'Arrive in style with our VIP meet-and-greet service. Your TRAGUIN private chauffeur will escort you to your handpicked hotel. Enjoy a panoramic evening tour of iconic attractions including the Petronas Towers.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'KUALA LUMPUR TO CAMERON HIGHLANDS',
                (
                    'Transfer to the cool, breezy Cameron Highlands. Enjoy breathtaking landscapes as we move from the city to the lush green tea plantations. A premium stay awaits in this highland sanctuary.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'CAMERON HIGHLANDS EXPLORATION',
                (
                    'A day of curated experiences: visit tea factories, mossy forests, and strawberry farms. Immerse yourself in the scenic beauty of the highlands.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'FLY TO LANGKAWI',
                (
                    'Take a private charter or premium flight to Langkawi. Check into your luxury beachfront villa and prepare for an exclusive experience on this pristine island.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'LANGKAWI ISLAND LUXURY',
                (
                    "Explore Langkawi's iconic attractions, including the SkyBridge and mangrove forests. Enjoy sunset cocktails on a private yacht—one of our signature exclusive experiences."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'LANGKAWI LEISURE',
                (
                    'Unwind at your handpicked hotel, indulge in spa treatments, or enjoy pristine beaches. Reflect on unforgettable memories created during your luxury Malaysia holiday.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'DEPARTURE',
                (
                    'Final shopping and breakfast before your departure. TRAGUIN ensures a seamless end to your premium journey.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Kuala Lumpur (2N) +',
                '6N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: TRAGUIN Handpicked Deluxe Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Kuala Lumpur (2N) +',
                '6N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: TRAGUIN Handpicked Premium Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Luxury Property',
                'Kuala Lumpur (2N) +',
                '6N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'The St. Regis KL Cameron Highlands Resort The Datai Langkawi',
                'Multi-city Malaysia',
                '6N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — The St. Regis KL Cameron Highlands Resort The Datai Langkawi',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Malaysia', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('Domestic flights and inter-city transfers as per curated itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Malaysia visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_my_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MY-006'
    tour_code = 'TRG-MAL-SHOP-2026'
    title = 'Malaysia Shopping Tour'
    duration = '04 Nights / 05 Days'
    slug = 'my-006-malaysia-shopping-tour'
    itin_slug = 'my-006-malaysia-shopping-itinerary'
    package = PackageCreate(
        slug=slug,
        serial_code=serial,
        traguin_tour_code=tour_code,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        price=0,
        rating=Decimal("4.9"),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ph('Serial code MY-006 | TRAGUIN tour code TRG-MAL-SHOP-2026', 1),
            _ph('Country: Malaysia, Asia | Category: Female Only Shopping Escape', 2),
            _ph('Destinations: Kuala Lumpur (4 Nights)', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Malaysia Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Malaysia Shopping Tour',
        overview="Kuala Lumpur • Pavilion KL • Suria KLCC • Petaling Street 04 Nights / 05 Days Female-Only Luxury Retail Retreat SERIAL CODE: MY-006 TRAGUIN TOUR CODE: TRG-MAL-SHOP-2026 STATE / COUNTRY: Malaysia CATEGORY: Female Only Shopping Escape DURATION: 04 Nights / 05 Days DESTINATIONS: Kuala Lumpur (4 Nights)\n\nTOUR OVERVIEW\nIndulge in a world-class retail retreat with this TRAGUIN curated female-only shopping escape. From high- fashion designer flagships to eclectic local markets, this luxury Malaysia holiday promises unforgettable memories, style, and relaxation in the heart of Kuala Lumpur. THE MALAYSIA SHOPPING EXPERIENCE Kuala Lumpur is a premier retail destination, known for its iconic attractions like Pavilion KL and Suria KLCC. Whether you're seeking luxury designer goods or unique local handicrafts, this Malaysia shopping escape delivers immersive experiences at every turn. Experience the scenic beauty of Malaysia while enjoying our curated experiences. THE IMMERSIVE DAY-WISE ITINERARY",
        seo_title='MY-006 | Malaysia Shopping Tour | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Malaysia package (MY-006 / TRG-MAL-SHOP-2026): Kuala Lumpur (4 Nights) with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL & CITY GLAMOUR', 1),
            _ih('Day 02: HIGH-FASHION RETAIL THERAPY', 2),
            _ih('Day 03: CULTURAL MARKETS & LOCAL CHARM', 3),
            _ih('Day 04: WELLNESS & SPA RETREAT', 4),
            _ih('Day 05: DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL & CITY GLAMOUR',
                (
                    'Arrive in style with our VIP meet-and-greet service. Your TRAGUIN private chauffeur will escort you to your handpicked hotel. Spend the evening enjoying the iconic attractions of KL, including a welcome dinner at a chic rooftop lounge.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'HIGH-FASHION RETAIL THERAPY',
                (
                    'A full day dedicated to the best of Malaysia shopping. Explore Pavilion KL and Suria KLCC, featuring global fashion houses and premium boutiques, designed for a luxury Malaysia holiday.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'CULTURAL MARKETS & LOCAL CHARM',
                (
                    'Discover the vibrant heart of the city at Petaling Street and Central Market. This immersive experience offers local artisan crafts and exclusive experiences that define Malaysian culture.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'WELLNESS & SPA RETREAT',
                (
                    'Take a day to rejuvenate. Indulge in premium stays and luxury spa treatments, a perfect complement to your retail spree. A true luxury Malaysia holiday for any fashionista.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'DEPARTURE',
                (
                    'Final boutique visits and breakfast before departure. TRAGUIN ensures you return home with unforgettable memories and shopping treasures.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Kuala Lumpur (4 Nights)',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: TRAGUIN Handpicked Deluxe Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Kuala Lumpur (4 Nights)',
                '4N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: TRAGUIN Handpicked Premium Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Luxury Property',
                'Kuala Lumpur (4 Nights)',
                '4N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'The St. Regis Kuala Lumpur / Pavilion Hotel',
                'Multi-city Malaysia',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — The St. Regis Kuala Lumpur / Pavilion Hotel',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Malaysia', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('Domestic flights and inter-city transfers as per curated itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Malaysia visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_my_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MY-007'
    tour_code = 'TRG-MAL-REL-2026'
    title = 'Malaysia Relax Senior Tour'
    duration = '05 Nights / 06 Days'
    slug = 'my-007-malaysia-relax-senior-tour'
    itin_slug = 'my-007-malaysia-relax-senior-itinerary'
    package = PackageCreate(
        slug=slug,
        serial_code=serial,
        traguin_tour_code=tour_code,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        price=0,
        rating=Decimal("4.9"),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ph('Serial code MY-007 | TRAGUIN tour code TRG-MAL-REL-2026', 1),
            _ph('Country: Malaysia, Asia | Category: Senior Citizen Relax Tour', 2),
            _ph('Destinations: Kuala Lumpur (3N) +', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Malaysia Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Malaysia Relax Senior Tour',
        overview='Kuala Lumpur • Putrajaya • Malacca Heritage • Cultural Serenity 05 Nights / 06 Days Optimized Leisure & Rejuvenation Tour SERIAL CODE: MY-007 TRAGUIN TOUR CODE: TRG-MAL-REL-2026 STATE / COUNTRY: Malaysia CATEGORY: Senior Citizen Relax Tour DURATION: 05 Nights / 06 Days DESTINATIONS: Kuala Lumpur (3N) + Malacca (2N)\n\nTOUR OVERVIEW\nEmbrace the cultural charm and graceful pace of Malaysia with our TRAGUIN curated senior-friendly holiday. This relaxing Malaysia holiday is designed for comfort, featuring gentle sightseeing, scenic beauty, and exclusive experiences in a serene atmosphere. We ensure every detail is handled, promising unforgettable memories.\n\nWHY CHOOSE OUR MALAYSIA RELAX TOUR?\nMalaysia is the perfect destination for senior travelers seeking a blend of rich heritage, natural beauty, and relaxed exploration. Our curated experiences ensure ease of movement, premium stays, and iconic attractions without the rush. Whether exploring the historical heart of Malacca or the vibrant capital of Kuala Lumpur, experience the scenic beauty of a truly premium Malaysia experience. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='MY-007 | Malaysia Relax Senior Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Malaysia package (MY-007 / TRG-MAL-REL-2026): Kuala Lumpur (3N) + with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN KUALA LUMPUR', 1),
            _ih('Day 02: KUALA LUMPUR SIGHTSEEING', 2),
            _ih('Day 03: PUTRAJAYA & TRANSFER TO MALACCA', 3),
            _ih('Day 04: MALACCA HERITAGE EXPLORATION', 4),
            _ih('Day 05: RELAXATION & LOCAL CULTURE', 5),
            _ih('Day 06: DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN KUALA LUMPUR',
                (
                    'A gentle welcome to Malaysia. Your private TRAGUIN chauffeur-driven transfer ensures comfort from the airport to your handpicked hotel. Enjoy a relaxing evening overlooking the city’s stunning skyline.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'KUALA LUMPUR SIGHTSEEING',
                (
                    'Explore Kuala Lumpur at a leisurely pace. Visit the iconic Petronas Towers and beautiful gardens. Enjoy iconic attractions designed for a relaxed Malaysia sightseeing experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'PUTRAJAYA & TRANSFER TO MALACCA',
                (
                    'Enjoy a scenic drive to the tranquil administrative capital, Putrajaya, followed by a comfortable journey to the historic city of Malacca. Enjoy the scenic beauty of the countryside.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'MALACCA HERITAGE EXPLORATION',
                (
                    "Discover the UNESCO World Heritage sites of Malacca. A gentle boat cruise along the Malacca River provides unforgettable memories of the city's unique cultural landscape."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'RELAXATION & LOCAL CULTURE',
                (
                    'Spend the day in relaxed exploration of Malacca’s charming streets and cafes. Indulge in exclusive experiences, including visiting local artisan markets for unique souvenirs.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'DEPARTURE',
                (
                    'Enjoy a final leisurely breakfast before your TRAGUIN assisted transfer back to the airport, concluding your premium Malaysia experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Kuala Lumpur (3N) +',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: TRAGUIN Handpicked Deluxe Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Kuala Lumpur (3N) +',
                '5N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: TRAGUIN Handpicked Premium Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Luxury Property',
                'Kuala Lumpur (3N) +',
                '5N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'The St. Regis Kuala Lumpur The Majestic Malacca',
                'Multi-city Malaysia',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — The St. Regis Kuala Lumpur The Majestic Malacca',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Malaysia', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('Domestic flights and inter-city transfers as per curated itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Malaysia visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_my_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MY-008'
    tour_code = 'TRG-MAL-FUN-FAM-2026'
    title = 'Malaysia Family Fun Tour'
    duration = '05 Nights / 06 Days'
    slug = 'my-008-malaysia-family-fun-tour'
    itin_slug = 'my-008-malaysia-family-fun-itinerary'
    package = PackageCreate(
        slug=slug,
        serial_code=serial,
        traguin_tour_code=tour_code,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        price=0,
        rating=Decimal("4.9"),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ph('Serial code MY-008 | TRAGUIN tour code TRG-MAL-FUN-FAM-2026', 1),
            _ph('Country: Malaysia, Asia | Category: Best Malaysia Family Fun Tour Package', 2),
            _ph('Destinations: Kuala Lumpur (3N) +', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Family', 'Luxury', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Malaysia Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Malaysia Family Fun Tour',
        overview='Kuala Lumpur • Genting Highlands • Sunway Lagoon • Family Bonding 05 Nights / 06 Days Immersive Malaysia Family Holiday SERIAL CODE: MY-008 TRAGUIN TOUR CODE: TRG-MAL-FUN-FAM-2026 STATE / COUNTRY: Malaysia CATEGORY: Best Malaysia Family Fun Tour Package DURATION: 05 Nights / 06 Days DESTINATIONS: Kuala Lumpur (3N) + Genting Highlands (2N)\n\nTOUR OVERVIEW\nDiscover the perfect blend of metropolitan excitement and mountain-top thrills with our TRAGUIN curated Malaysia family fun tour. Designed specifically for active families, this trip combines world-class theme parks, breathtaking landscapes, and premium stays to ensure unforgettable memories. THE IMMERSIVE MALAYSIA FAMILY EXPERIENCE Malaysia is a premier destination for families, offering endless excitement for all ages. From the high-energy rides of Sunway Lagoon to the cool misty mountain entertainment of Genting Highlands, our curated experiences promise a premium Malaysia experience. With TRAGUIN, you get professional support and exclusive experiences that redefine the family holiday. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='MY-008 | Malaysia Family Fun Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Malaysia package (MY-008 / TRG-MAL-FUN-FAM-2026): Kuala Lumpur (3N) + with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN KUALA LUMPUR', 1),
            _ih('Day 02: SUNWAY LAGOON ADVENTURE', 2),
            _ih('Day 03: KUALA LUMPUR TO GENTING HIGHLANDS', 3),
            _ih('Day 04: GENTING HIGHLANDS THEME PARK', 4),
            _ih('Day 05: RETURN TO KUALA LUMPUR', 5),
            _ih('Day 06: DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN KUALA LUMPUR',
                (
                    'Your TRAGUIN family adventure begins with a seamless arrival. Private luxury transfers bring you to your hotel, ensuring total comfort after your flight. Explore the vibrant city evening at your own pace.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'SUNWAY LAGOON ADVENTURE',
                (
                    "A full day of family fun at Sunway Lagoon, one of Malaysia's premier theme parks. This iconic attraction offers water sports, wildlife encounters, and thrill rides perfect for children and adults alike."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'KUALA LUMPUR TO GENTING HIGHLANDS',
                (
                    "Ascend to Genting Highlands via a scenic cable car. Enjoy breathtaking landscapes and the cool mountain air. Check into your handpicked hotel and enjoy the evening's indoor entertainment."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'GENTING HIGHLANDS THEME PARK',
                (
                    'Experience the ultimate family fun day at Genting SkyWorlds Theme Park. This curated experience offers world-class rides and immersive experiences for the whole family.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'RETURN TO KUALA LUMPUR',
                (
                    'Transfer back to Kuala Lumpur. Spend the afternoon exploring iconic shopping centers and sampling local culinary delights, creating unforgettable memories in the heart of the city.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'DEPARTURE',
                (
                    'Enjoy a final family breakfast. Your private TRAGUIN chauffeur ensures a comfortable transfer to the airport for your journey home.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Kuala Lumpur (3N) +',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: TRAGUIN Handpicked Deluxe Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Kuala Lumpur (3N) +',
                '5N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: TRAGUIN Handpicked Premium Property',
            ),
            _hotel(
                'Shangri-La Kuala Lumpur Resorts World Genting',
                'Multi-city Malaysia',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Shangri-La Kuala Lumpur Resorts World Genting',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Kuala Lumpur (3N) +',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Malaysia', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('Domestic flights and inter-city transfers as per curated itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Malaysia visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_my_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MY-009'
    tour_code = 'TRG-LGK-ADV-2026'
    title = 'Langkawi Adventure Tour'
    duration = '05 Nights / 06 Days'
    slug = 'my-009-langkawi-adventure-tour'
    itin_slug = 'my-009-langkawi-adventure-itinerary'
    package = PackageCreate(
        slug=slug,
        serial_code=serial,
        traguin_tour_code=tour_code,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        price=0,
        rating=Decimal("4.9"),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ph('Serial code MY-009 | TRAGUIN tour code TRG-LGK-ADV-2026', 1),
            _ph('Country: Malaysia, Asia | Category: Best Langkawi Adventure Tour Package', 2),
            _ph('Destinations: Langkawi (5 Nights', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Nature', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Malaysia Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Langkawi Adventure Tour',
        overview='Langkawi • Kilim Geoforest • SkyBridge • Jet Ski Safari • Island Hopping 05 Nights / 06 Days Ultra-Luxury Adventure Expedition SERIAL CODE: MY-009 TRAGUIN TOUR CODE: TRG-LGK-ADV-2026 STATE / COUNTRY: Malaysia CATEGORY: Best Langkawi Adventure Tour Package DURATION: 05 Nights / 06 Days DESTINATIONS: Langkawi (5 Nights Adventure Sanctuary)\n\nTOUR OVERVIEW\nUnleash your spirit of adventure with this TRAGUIN curated Langkawi expedition. Designed for thrill-seekers, this package combines high-octane adventure with the serene luxury of Langkawi’s breathtaking landscapes. Experience curated experiences and create unforgettable memories on the ultimate luxury Malaysia holiday. THE LANGKAWI ADVENTURE EXPERIENCE Langkawi is the perfect playground for adventure enthusiasts. From jet ski safaris through tropical islands to trekking the ancient Kilim Geoforest, this Malaysia adventure tour offers immersive experiences and exclusive experiences that redefine the typical holiday. Enjoy the scenic beauty of a truly premium Langkawi sightseeing experience. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='MY-009 | Langkawi Adventure Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Malaysia package (MY-009 / TRG-LGK-ADV-2026): Langkawi (5 Nights with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN LANGKAWI', 1),
            _ih('Day 02: JET SKI SAFARI & ISLAND HOPPING', 2),
            _ih('Day 03: KILIM GEOFOREST ADVENTURE', 3),
            _ih('Day 04: SKYBRIDGE & MOUNTAIN THRILLS', 4),
            _ih('Day 05: MARINE EXPLORATION', 5),
            _ih('Day 06: DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN LANGKAWI',
                (
                    'Your TRAGUIN adventure begins with a private transfer to your handpicked hotel. Relax and prepare for an action-packed Langkawi sightseeing trip.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'JET SKI SAFARI & ISLAND HOPPING',
                (
                    'Embark on an adrenaline-fueled jet ski safari, one of our exclusive experiences. Explore hidden coves and pristine islands, capturing breathtaking landscapes along the way.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'KILIM GEOFOREST ADVENTURE',
                (
                    "Discover the Kilim Geoforest Park, featuring iconic attractions like floating fish farms and eagle-feeding spots. A curated experience that brings you closer to Malaysia's natural wonders."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'SKYBRIDGE & MOUNTAIN THRILLS',
                (
                    'Ascend the SkyCab to the Langkawi SkyBridge. Experience scenic beauty and breathtaking landscapes from the high peaks. Perfect for thrill-seekers looking for unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'MARINE EXPLORATION',
                (
                    'A full day of marine exploration, including snorkeling in pristine reefs. Enjoy our signature exclusive experiences as you dive into the aquatic life that makes Langkawi a top Langkawi sightseeing spot.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'DEPARTURE',
                (
                    'Enjoy a final adventure breakfast before your TRAGUIN assisted transfer, concluding your premium Langkawi experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Langkawi (5 Nights',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: TRAGUIN Handpicked Deluxe Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Langkawi (5 Nights',
                '5N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: TRAGUIN Handpicked Premium Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Luxury Property',
                'Langkawi (5 Nights',
                '5N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'The Datai Langkawi / The Ritz-Carlton',
                'Multi-city Malaysia',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — The Datai Langkawi / The Ritz-Carlton',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Malaysia', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('Domestic flights and inter-city transfers as per curated itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Malaysia visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_my_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MY-010'
    tour_code = 'TRG-MAL-GRD-2026'
    title = 'Grand Malaysia Luxury Tour'
    duration = '06 Nights / 07 Days'
    slug = 'my-010-grand-malaysia-luxury-tour'
    itin_slug = 'my-010-grand-malaysia-luxury-itinerary'
    package = PackageCreate(
        slug=slug,
        serial_code=serial,
        traguin_tour_code=tour_code,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        price=0,
        rating=Decimal("4.9"),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ph('Serial code MY-010 | TRAGUIN tour code TRG-MAL-GRD-2026', 1),
            _ph('Country: Malaysia, Asia | Category: Ultimate Grand Malaysia Discovery', 2),
            _ph('Destinations: Kuala Lumpur (2N) +', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Malaysia Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Grand Malaysia Luxury Tour',
        overview='Kuala Lumpur • Langkawi Island • Penang • Cultural Heritage 06 Nights / 07 Days Grand Malaysia Luxury Discovery SERIAL CODE: MY-010 TRAGUIN TOUR CODE: TRG-MAL-GRD-2026 STATE / COUNTRY: Malaysia CATEGORY: Ultimate Grand Malaysia Discovery DURATION: 06 Nights / 07 Days DESTINATIONS: Kuala Lumpur (2N) + Penang (2N) + Langkawi (2N)\n\nTOUR OVERVIEW\nIndulge in the ultimate Grand Malaysia exploration with our TRAGUIN curated luxury tour. From the cosmopolitan splendor of Kuala Lumpur to the heritage charm of Penang and the azure serenity of Langkawi, this luxury Malaysia holiday offers unforgettable memories, breathtaking landscapes, and exclusive experiences.\n\nWHY CHOOSE OUR GRAND MALAYSIA LUXURY TOUR?\nMalaysia offers an unparalleled tapestry of culture, adventure, and refinement. Our curated experiences in Kuala Lumpur, Penang, and Langkawi provide the perfect balance for the discerning traveler. With TRAGUIN, enjoy handpicked hotels, private transfers, and a truly premium Malaysia experience. Discover the iconic attractions that make Malaysia a top global destination. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='MY-010 | Grand Malaysia Luxury Tour | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Malaysia package (MY-010 / TRG-MAL-GRD-2026): Kuala Lumpur (2N) + with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN KUALA LUMPUR', 1),
            _ih('Day 02: KUALA LUMPUR TO PENANG', 2),
            _ih('Day 03: PENANG CULTURAL HERITAGE', 3),
            _ih('Day 04: PENANG TO LANGKAWI', 4),
            _ih('Day 05: LANGKAWI ISLAND LUXURY', 5),
            _ih('Day 06: LANGKAWI LEISURE & SUNSET CRUISE', 6),
            _ih('Day 07: DEPARTURE', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN KUALA LUMPUR',
                (
                    "Arrive in style at the capital. Your TRAGUIN private chauffeur will escort you to your handpicked hotel. Enjoy a luxury evening tour of Kuala Lumpur's vibrant city center and iconic attractions."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'KUALA LUMPUR TO PENANG',
                (
                    'Fly to Penang, the food and heritage capital. Discover scenic beauty in George Town, a UNESCO World Heritage site, and stay in one of our premium stays.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'PENANG CULTURAL HERITAGE',
                (
                    'A curated experience exploring Penang’s colorful street art, historic mansions, and temple architecture. Indulge in culinary delights that offer unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'PENANG TO LANGKAWI',
                (
                    "Take a scenic flight to Langkawi, Malaysia's jewel of the Andaman. Your luxury Malaysia holiday continues with an arrival at a world-class premium stay by the beach."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'LANGKAWI ISLAND LUXURY',
                (
                    "A full day of exclusive experiences. Visit the SkyBridge, explore lush mangroves, and enjoy the scenic beauty of Langkawi's turquoise waters."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'LANGKAWI LEISURE & SUNSET CRUISE',
                (
                    'Spend time in paradise with immersive experiences. Conclude your day with a sunset yacht cruise, offering breathtaking landscapes of the island’s archipelago.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'DEPARTURE',
                (
                    'Final relaxation and breakfast before your TRAGUIN assisted transfer. Leave Malaysia with unforgettable memories of a truly grand adventure.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Kuala Lumpur (2N) +',
                '6N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: TRAGUIN Handpicked Deluxe Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Kuala Lumpur (2N) +',
                '6N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: TRAGUIN Handpicked Premium Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Luxury Property',
                'Kuala Lumpur (2N) +',
                '6N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'The St. Regis KL Eastern & Oriental Hotel The Datai Langkawi',
                'Multi-city Malaysia',
                '6N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — The St. Regis KL Eastern & Oriental Hotel The Datai Langkawi',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Malaysia', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('Domestic flights and inter-city transfers as per curated itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Malaysia visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

MALAYSIA_MY_001_010_BUILDERS = [
    build_my_001,
    build_my_002,
    build_my_003,
    build_my_004,
    build_my_005,
    build_my_006,
    build_my_007,
    build_my_008,
    build_my_009,
    build_my_010,
]
