"""Builder functions for WB-002 through WB-005 West Bengal domestic packages."""

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

WEST_BENGAL_SLUG = "west-bengal"


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


def build_wb_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-001'
    tour_code = 'TRG-WB-001'
    title = 'DARJEELING ESCAPE • THE QUEEN OF THE HILLS'
    duration = '03 Nights / 04 Days'
    slug = 'wb-001-darjeeling-escape-the-queen-of-the-hills'
    itin_slug = 'wb-001-darjeeling-escape-the-queen-of-the-hills-itinerary'
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
        is_published=True,
        highlights=[
            _ph('Serial code WB-001 | TRAGUIN tour code TRG-WB-001', 1),
            _ph('State / Country: West Bengal / India | Category: Premium Family Tour', 2),
            _ph('Destinations: Darjeeling • Tiger', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Innova Crysta / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private sunrise coordination at Tiger Hill with reserved premium', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked routing and premium vehicle transfers to ensure a smooth,', 9),
            _ph('Premium Handpicked Hotels: Accommodations selected strictly based on luxury comfort, family safety,', 10),
            _ph('Exclusive Recommendations: Curated list of historic colonial dining spots, artisan tea boutiques, and', 11)
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
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='DARJEELING ESCAPE',
        overview='DARJEELING ESCAPE • THE QUEEN OF THE HILLS Welcome to an exquisite mountain getaway curated exclusively by TRAGUIN. Embark on the finest West Bengal Family Tour designed to reveal the breathtaking landscapes, misty tea plantations, and imperial colonial charm of Darjeeling. As your trusted luxury travel consultants, TRAGUIN transforms your holiday into a highly personalized, elite mountain escape. Wake up to the awe-inspiring view of the Kanchenjunga range, relax in premium stays, and enjoy immersive experiences designed to build unforgettable memories for your family.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers the ultimate escape into the hills of West Bengal. Travelling in a dedicated premium private vehicle with an expert local chauffeur, your family will experience absolute privacy and comfort. With a carefully curated meal plan featuring lavish breakfasts and specialized multi- course dinners at your resort, this route represents the definitive premium Darjeeling experience. Every step of your journey includes the signature touch of TRAGUIN curated experiences, including VIP sunrise access coordinates, private heritage tea-tasting sessions, and around-the-clock elite customer assistance.\n\nWHY CHOOSE THE BEST WEST BENGAL TOUR PACKAGE?\nWhen planning a Luxury West Bengal Holiday, discerning families seek an impeccable mix of grand colonial heritage, crisp alpine weather, and world-class luxury stays. Darjeeling stands out as a timeless gem, making a Darjeeling Family Tour or a romantic Darjeeling Honeymoon Package highly sought-after. From the legendary sunrise over Tiger Hill to the historic UNESCO World Heritage Himalayan Railway toy train, Darjeeling sightseeing offers unique and iconic attractions. For families booking our TRAGUIN West Bengal Packages, the hill station reveals spectacular, highly popular Instagram locations like the Batasia Loop war memorial, the lush Happy Valley Tea Estate, and the architectural masterpiece of the Ghum Monastery. Whether you are looking for authentic local handicraft shopping, indulging in hot Tibetan momos and high-tea at legendary colonial cafes, or capturing panoramic mountain photography points, our carefully scheduled tours ensure you experience the absolute best time to visit West Bengal in complete comfort.',
        seo_title='WB-001 | DARJEELING ESCAPE | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days West Bengal package (WB-001 / TRG-WB-001): Darjeeling • Tiger with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=True,
        highlights=[
            _ih('Day 01: BAGDOGRA / NJP TO DARJEELING', 1),
            _ih('Day 02: TIGER HILL SUNRISE & HERITAGE SIGHTSEEING', 2),
            _ih('Day 03: TEA GARDEN EXCURSION & ROCK GARDEN', 3),
            _ih('Day 04: DEPARTURE FROM DARJEELING', 4),
            _ih('TRAGUIN Signature Experience: Private sunrise coordination at Tiger Hill with reserved premium', 5),
            _ih('Curated by TRAGUIN Experts: Handpicked routing and premium vehicle transfers to ensure a smooth,', 6),
            _ih('Premium Handpicked Hotels: Accommodations selected strictly based on luxury comfort, family safety,', 7)
        ],
        days=[
            _day(
                1,
                'BAGDOGRA / NJP TO DARJEELING',
                (
                    'GATEWAY TO THE HILLS – ASCENT THROUGH THE LUSH TEA ORCHARDS Your premium West Bengal experience begins with a warm welcome at Bagdogra Airport or New Jalpaiguri (NJP) Railway Station by your private luxury transport chauffeur. Embark on a highly scenic route winding through vast emerald tea estates, emerald valleys, and small mountain hamlets. As the air turns crisp and cool, arrive in Darjeeling and check into your handpicked premium luxury resort. After relaxing, enjoy a refreshing evening walk along the famous Mall Road (Chowrasta)—a vibrant social hub ideal for photography points and picking up authentic curios.'
                ),
                [
                    'Sightseeing Included: Scenic Rohini/Kurseong bypass route, Darjeeling Mall Road, Chowrasta.',
                    "Evening Experience: Welcome high-tea session featuring the world's finest authentic first-flush Darjeeling tea.",
                    'Overnight Stay: Darjeeling (Premium Colonial Heritage Property / Luxury Resort)',
                    'Meals Included: Welcome Drink & Luxury Multi-Cuisine Dinner',
                ],
            ),
            _day(
                2,
                'TIGER HILL SUNRISE & HERITAGE SIGHTSEEING',
                (
                    'GOLDEN KANCHENJUNGA SUNRISE & IMPERIAL ICONIC ATTRACTIONS Wake up at 4:00 AM for an elite, emotionally moving excursion to Tiger Hill. Watch in absolute awe as the sun rises over Mount Everest and Mount Kanchenjunga, illuminating the snow-clad peaks in hues of brilliant gold and pink. On your return route, visit the historic Ghum Monastery and the magnificent Batasia Loop, where the toy train makes a dramatic loop amidst a beautifully manicured garden. After a late breakfast, visit the Himalayan Mountaineering Institute (HMI), Padmaja Naidu Himalayan Zoological Park (home to rare Red Pandas and Snow Leopards), and the Tibetan Refugee Self Help Center.'
                ),
                [
                    'Sightseeing Included: Tiger Hill Sunrise, Ghum Monastery, Batasia Loop, Padmaja Naidu Zoo, HMI, Ropeway.',
                    'Optional Activities: A nostalgic ride on the legendary Darjeeling Himalayan Railway Heritage Toy Train.',
                    'Overnight Stay: Darjeeling (Premium / Luxury Resort)',
                    'Meals Included: Premium Breakfast & Specialized Family Dinner',
                ],
            ),
            _day(
                3,
                'TEA GARDEN EXCURSION & ROCK GARDEN',
                (
                    'IMMERSIVE TEA GARDEN TASTING & CASCADING WATERFALLS Following a delicious hot breakfast, proceed on a specialized tour to the Happy Valley Tea Estate. Walk hand- in-hand through the manicured tea rows, interact with local tea pluckers, and discover the delicate art of orthodox tea manufacturing. Next, drive down a thrilling winding mountain road to the beautiful Rock Garden (Barbotey), featuring terraced seating cut out of solid rock around a spectacular natural cascading waterfall. Spend your afternoon at leisure exploring local hillside boutiques or relaxing at your premium resort spa.'
                ),
                [
                    'Sightseeing Included: Happy Valley Tea Estate, Barbotey Rock Garden, Gangamaya Park.',
                    'Evening Experience: Private luxury bonfire night at your resort courtyard with panoramic mountain views.',
                    'Overnight Stay: Darjeeling (Premium / Luxury Resort)',
                    'Meals Included: Premium Breakfast & Farewell Gala Dinner',
                ],
            ),
            _day(
                4,
                'DEPARTURE FROM DARJEELING',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Indulge in a final lavish breakfast as you admire the majestic morning sun over the Himalayan peaks. Pack your bags and board your private luxury vehicle for a smooth, comfortable transfer back to Bagdogra Airport or NJP Railway Station. Your high-end mountain getaway concludes as you catch your onward connection, carrying home a heart filled with sweet family bonds and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door station or airport drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Summit Hermon Hotel & | Spa / similar | Dinner)',
                'Multi-city West Bengal',
                '3N',
                'Deluxe',
                'Room',
                'MAPAI (Breakfast &',
                4,
                1,
                description='OPTION 01 – DELUXE: The Summit Hermon Hotel & | Spa / similar | Dinner)',
            ),
            _hotel(
                'Sinclairs Darjeeling / Ramada | Dinner)',
                'Multi-city West Bengal',
                '3N',
                'Premium',
                'Balcony Room',
                'MAPAI (Breakfast &',
                4,
                2,
                description='OPTION 02 – PREMIUM: Sinclairs Darjeeling / Ramada | Dinner)',
            ),
            _hotel(
                'The Elgin Darjeeling / Mayfair | Hill Resort',
                'Multi-city West Bengal',
                '3N',
                'Luxury',
                'Luxury Heritage Suite',
                'MAPAI + Welcome',
                4,
                3,
                description='OPTION 03 – LUXURY: The Elgin Darjeeling / Mayfair | Hill Resort',
            ),
            _hotel(
                'Windamere Hotel (Colonial | Heritage Estate)',
                'Multi-city West Bengal',
                '3N',
                'Ultra Luxury',
                'Suite',
                'MAPAI Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Windamere Hotel (Colonial | Heritage Estate)',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 03 Nights in handpicked properties as per your chosen category.', 1),
            _inc_included('Luxury Transportation: Private AC Innova Crysta for all transfers & sightseeing.', 2),
            _inc_included('Curated Meal Plan: Daily premium breakfast and gourmet dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest experience manager on call.', 4),
            _inc_included('Welcome Amenities: Customized family travel kit and traditional scarf welcome.', 5),
            _inc_included('Complimentary Experience: Exclusive private tea-tasting tour at a premium estate.', 6),
            _inc_excluded('Airfare, flight tickets, or long-distance train travel to Bagdogra/NJP.', 7),
            _inc_excluded('Darjeeling Himalayan Railway Toy Train ride booking tickets.', 8),
            _inc_excluded('Monument entry tickets, professional guide fees, and camera permits.', 9),
            _inc_excluded('Personal expenses such as laundry, phone calls, liquor, or tips.', 10),
        ],
    )
    return package, itinerary

WEST_BENGAL_WB_001_BUILDERS = [
    build_wb_001,
]
