"""Builder functions for JK-001 through JK-010 Kashmir domestic packages."""

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

KASHMIR_SLUG = "kashmir"


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


def build_jk_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JK-001'
    tour_code = 'TRG-KASH-001'
    title = 'Kashmir Paradise — The Ultimate Family Luxury Escape'
    duration = '05 Nights / 06 Days'
    slug = 'jk-001-kashmir-paradise-family'
    itin_slug = 'jk-001-kashmir-paradise-family-itinerary'
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
            _ph('Serial code JK-001 | TRAGUIN tour code TRG-KASH-001', 1),
            _ph('State / Country: Jammu & Kashmir / India | Category: Premium Family', 2),
            _ph('Destinations: Srinagar • Gulmarg • Pahalgam • Sonamarg', 3),
            _ph('Ideal for: Family Vacations, Luxury Explorers & Nature Seekers', 4),
            _ph('Best season: April to October (Lush Greens) / December to March (Snow)', 5),
            _ph('Starting price: On Request (Premium Customised)', 6),
            _ph('Vehicle / Meals: Private Luxury Innova Crysta / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: A private family interaction and traditional Kehwa brewing masterclass', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked properties that ensure standard premium security, absolute', 9),
            _ph('Exclusive Recommendations: Priority check-in assistance and handpicked authentic artisan factory', 10),
            _ph('& TRAVEL INFORMATION', 11),
            _ph('Booking Policy: We highly advise advance bookings at least 45 days prior to travel, especially during', 12)
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
        tagline='Kashmir Paradise — The Ultimate Family Luxury Escape',
        overview='TRAGUIN PREMIUM KASHMIR TOUR PACKAGE KASHMIR PARADISE • THE ULTIMATE FAMILY LUXURY ESCAPE Welcome to a timeless journey across heaven on earth, beautifully crafted by TRAGUIN. Embark on the finest Kashmir Family Tour designed to reveal the breathtaking landscapes, majestic snow-peaks, and serene mirror lakes of this legendary valley. As your trusted premium travel consultants, TRAGUIN transforms your vacation into a seamless luxury holiday filled with handpicked hotels, intimate local experiences, and unparalleled luxury transportation. Let the scenic beauty of the valleys write an emotional chapter for your family, forging unforgettable memories that linger forever.\n\nTOUR OVERVIEW\nThis custom-tailored Kashmir Paradise itinerary offers an exquisite balance between peaceful lake living, Alpine meadows, gushing glacial rivers, and magnificent heritage architecture. Travelling in a dedicated private luxury transport vehicle with a professional chauffeur-driven assistant, your family will enjoy absolute comfort and complete privacy across every mountain pass. With a carefully curated meal plan featuring lavish daily breakfasts and multi-cuisine dinners, this route represents the definitive premium Kashmir experience. Every step of your journey includes the signature touch of TRAGUIN curated experiences, ensuring VIP entry privileges, local storytelling insight, and around-the-clock bespoke support.\n\nWHY CHOOSE THE BEST KASHMIR TOUR PACKAGE?\nWhen considering a Luxury Kashmir Holiday, discerning families seek more than just basic sightseeing; they seek an immersive dive into pristine nature, royal history, and premium hospitality. Kashmir boasts some of the most iconic attractions in the world. From the floating world of Dal Lake in Srinagar to the spectacular meadows of Gulmarg—famed for having one of the highest cable car systems globally—and the majestic pine-fringed valleys of Pahalgam, Kashmir sightseeing is truly spectacular. For families and couples booking a bespoke Kashmir Honeymoon Package or a high-end Kashmir Family Tour, the region reveals highly popular Instagram locations like the floating vegetable markets, the vibrant Mughal Gardens, and the majestic Betaab Valley. Whether you are looking for authentic saffron and pashmina shopping, indulging in traditional Kashmiri Wazwan culinary delights, or experiencing a scenic Shikara cruise at sunset, our signature TRAGUIN Kashmir Packages guarantee premium comfort, handpicked hotels, and curated exclusive experiences that make it the best time to visit Kashmir. TRAGUIN Premium Luxury Proposal — JK-001 2',
        seo_title='JK-001 | Kashmir Paradise — The Ultimate Family Luxury Escape | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Kashmir package (JK-001 / TRG-KASH-001): Srinagar • Gulmarg • Pahalgam • Sonamarg with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SRINAGAR & FLOATING HOUSEBOAT EXPERIENCE', 1),
            _ih('Day 02: SRINAGAR TO GULMARG EXCURSION', 2),
            _ih('Day 03: SRINAGAR TO PAHALGAM', 3),
            _ih('Day 04: PAHALGAM VALLEY EXPLORATION', 4),
            _ih('Day 05: PAHALGAM TO SRINAGAR MUGHAL GARDENS TOUR', 5),
            _ih('Day 06: SRINAGAR TO DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: A private family interaction and traditional Kehwa brewing masterclass', 7),
            _ih('Curated by TRAGUIN Experts: Handpicked properties that ensure standard premium security, absolute', 8),
            _ih('Exclusive Recommendations: Priority check-in assistance and handpicked authentic artisan factory', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SRINAGAR & FLOATING HOUSEBOAT EXPERIENCE',
                (
                    'WELCOME TO THE SUMMER CAPITAL – CHARM OF THE DAL LAKE Your premium Kashmir experience begins as you touch down at Srinagar Airport, where a dedicated private luxury transport vehicle waits to escort you. Transfer directly to the banks of the iconic Dal Lake and step into a meticulously handpicked premium luxury houseboat. After a refreshing afternoon, experience an emotional storytelling moment during a private 1-hour sunset Shikara ride across the mirrored waters, passing floating gardens and local wooden hamlets. Capture perfect family photography points as the golden hour settles behind the Zabarwan range.'
                ),
                [
                    'Sightseeing Included: Dal Lake, Private Sunset Shikara Ride, Floating Markets.',
                    'Evening Experience: Traditional Kashmiri Kehwa welcome drink followed by a curated local dinner on board.',
                    'Overnight Stay: Srinagar (Premium / Luxury Handpicked Houseboat)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'SRINAGAR TO GULMARG EXCURSION',
                (
                    'THE MEADOW OF FLOWERS – HIGHEST ASIA GONDOLA RIDE Awake to a crisp morning mist and enjoy a lavish breakfast before driving to Gulmarg, the crown jewel of Alpine beauty in the region. The scenic route takes you past fields of rice and tall poplar trees. Upon arrival, embark on an immersive experience via the famous Gulmarg Gondola (Phase 1 & 2), riding up to Apharwat Peak at over 13,000 feet. Marvel at the breathtaking landscapes and sweeping views of the line of control. Walk along the verdant meadows, visit the historic St. Mary’s Church, and enjoy high-altitude snow photography with your family. TRAGUIN Premium Luxury Proposal — JK-001 3'
                ),
                [
                    "Sightseeing Included: Gulmarg Meadows, Gondola Cable Car Ride, St. Mary's Church, Golf Course.",
                    'Optional Activities: ATV mountain biking, private snow skiing sessions (winter only).',
                    'Overnight Stay: Srinagar (Premium / Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'SRINAGAR TO PAHALGAM',
                (
                    'THE VALLEY OF SHEPHERDS – SAFFRON FIELDS & GUSHING STREAMS Depart after a sumptuous breakfast towards the legendary valley of Pahalgam. En route, enjoy an exclusive stop at the aromatic Pampore Saffron Fields and the ancient 1100-year-old Awantipora ruins. As you approach Pahalgam, the roaring Lidder River walks alongside your vehicle. Check into your ultra-luxury riverside resort. Spend the afternoon taking an emotional stroll along the pine forests, listening to the rhythmic sounds of nature, completely separated from urban noise.'
                ),
                [
                    'Sightseeing Included: Saffron Fields, Awantipora Ruins, Lidder River Trail.',
                    'Evening Experience: Private riverside family bonfire with premium snacks arranged by TRAGUIN experts.',
                    'Overnight Stay: Pahalgam (Premium Selected Luxury Riverside Resort)',
                    'Meals Included: Breakfast & Traditional Elite Dinner',
                ],
            ),
            _day(
                4,
                'PAHALGAM VALLEY EXPLORATION',
                (
                    'BETAAB VALLEY, ARU VALLEY & CHANDANWARI ICONIC ATTRACTIONS Dedicate your day to exploring the hidden gems of Pahalgam via a localized premium transport loop. Visit Betaab Valley, named after the famous Bollywood movie, where crystal clear streams cut through deep green pastures. Explore the high-altitude meadows of Aru Valley and the snow-bridge vistas of Chandanwari, which serves as the starting point of the holy Amarnath Yatra. It is a highly popular Instagram location perfect for your family portraiture.'
                ),
                [
                    'Sightseeing Included: Betaab Valley, Aru Valley, Chandanwari, local pine meadows.',
                    'Optional Activities: A romantic horse-riding trail up to Baisaran Valley (known as Mini Switzerland).',
                    'Overnight Stay: Pahalgam (Premium Selected Luxury Riverside Resort)',
                    'Meals Included: Breakfast & Exquisite Buffet Dinner',
                ],
            ),
            _day(
                5,
                'PAHALGAM TO SRINAGAR MUGHAL GARDENS TOUR',
                (
                    'ROYAL ARCHITECTURE & HISTORIC SPRING FOUNTAINS Drive back to Srinagar today to experience the manicured royal side of Kashmir sightseeing. Explore the world-famous Mughal Gardens, including Shalimar Bagh (The Abode of Love) and Nishat Bagh (The Garden of Pleasure), built by the great Mughal Emperors along the lake standard. Admire the terraced lawns, cascading fountains, and centuries-old Chinar trees. Later, visit the beautiful Shankaracharya Temple perched atop a hill, offering panoramic views of the entire city. TRAGUIN Premium Luxury Proposal — JK-001 4'
                ),
                [
                    'Sightseeing Included: Nishat Bagh, Shalimar Bagh, Chashme Shahi, Shankaracharya Temple Hill.',
                    'Evening Experience: Farewell family dinner featuring an authentic 7-course Kashmiri Wazwan meal.',
                    'Overnight Stay: Srinagar (Premium / Luxury Stay)',
                    'Meals Included: Breakfast & Farewell Premium Wazwan Dinner',
                ],
            ),
            _day(
                6,
                'SRINAGAR TO DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES OF PARADISE Indulge in a final lavish breakfast at your premium hotel overlooking the mountains. Your private luxury transport will safely drive you to Srinagar Airport for your onward flight home. Return to your routine carrying a rejuvenated spirit, closer family bonds, and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury airport departure transfer.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Grand Mumtaz / similar | Hotel Hilltop / similar | Royal Houseboats / similar',
                'Srinagar | Pahalgam | Dal Lake Houseboat',
                '1N Houseboat|2N Pahalgam|2N Srinagar',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Grand Mumtaz / similar | Hotel Hilltop / similar | Royal Houseboats / similar | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Orchid Retreat / similar | Hotel Heevan / Pine n Peak | Mascot Houseboats / similar',
                'Srinagar | Pahalgam | Dal Lake Houseboat',
                '1N Houseboat|2N Pahalgam|2N Srinagar',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Orchid Retreat / similar | Hotel Heevan / Pine n Peak | Mascot Houseboats / similar | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Radisson Blu Srinagar | Welcomhotel by ITC Pine & Peak | Sukoon Luxury Houseboat',
                'Srinagar | Pahalgam | Dal Lake Houseboat',
                '1N Houseboat|2N Pahalgam|2N Srinagar',
                'Luxury',
                'Luxury Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Radisson Blu Srinagar | Welcomhotel by ITC Pine & Peak | Sukoon Luxury Houseboat | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Taj Palace / The Lalit Grand Palace | The Grand Mumtaz Resorts VVIP | Signature Ultra Luxury Suite',
                'Srinagar | Pahalgam | Dal Lake Houseboat',
                '1N Houseboat|2N Pahalgam|2N Srinagar',
                'Ultra Luxury',
                'Royal Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Taj Palace / The Lalit Grand Palace | The Grand Mumtaz Resorts VVIP | Signature Ultra Luxury Suite | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Premium stays: Handpicked hotels & luxury houseboat as per category.', 1),
            _inc_included('Luxury Transportation: Private AC Innova Crysta for all transfers & sightseeing.', 2),
            _inc_included('Curated Meal Plan: Daily premium breakfast and gourmet dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest experience manager on call.', 4),
            _inc_included('Welcome Amenities: Personalized Kashmiri travel kit and traditional refreshments.', 5),
            _inc_included('Complimentary experiences: 1-Hour private sunset Shikara ride on Dal Lake.', 6),
            _inc_excluded('Airfare / Train tickets to and from Srinagar.', 7),
            _inc_excluded('Gondola ride tickets, monument entry fees, and garden entrance tickets.', 8),
            _inc_excluded('Personal expenses such as laundry, liquor, telephone calls, and horse-riding tips.', 9),
            _inc_excluded('Local internal cab in Pahalgam / Gulmarg if restricted by local unions.', 10),
        ],
    )
    return package, itinerary

def build_jk_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JK-002'
    tour_code = 'TRG-KASH-002'
    title = 'Srinagar • Gulmarg Premium Family Tour'
    duration = '04 Nights / 05 Days'
    slug = 'jk-002-srinagar-gulmarg-premium-family'
    itin_slug = 'jk-002-srinagar-gulmarg-premium-family-itinerary'
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
            _ph('Serial code JK-002 | TRAGUIN tour code TRG-KASH-002', 1),
            _ph('State / Country: Jammu & Kashmir / India | Category: Premium Family', 2),
            _ph('Destinations: Srinagar • Gulmarg • Dal Lake Houseboat', 3),
            _ph('Ideal for: Family Vacations, Luxury Explorers & Couples', 4),
            _ph('Best season: April to October (Lush Green) / December to March (Snowfall)', 5),
            _ph('Starting price: On Request (Premium Customised)', 6),
            _ph('Vehicle / Meals: Private Luxury Innova Crysta / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private family interaction and artisan paper-mâché craft demonstration.', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked routing to avoid peak tourist congestion, maximizing your', 9),
            _ph('Premium Handpicked Hotels: Accommodations selected strictly based on premium safety standards and', 10),
            _ph('Exclusive Recommendations: VIP access parameters to select lakeside evening dining spaces.', 11),
            _ph('Traditional Souvenirs: Bring home beautiful, authentic hand-knotted Pashmina shawls, walnut wood carvings, and delicate papier-mâché artifacts from local Srinagar markets. Kashmir is also world-famous for its organic saffron, walnuts, and almonds. Gourmet & Cafes: Indulge your palate in rich traditional Kahwa tea, authentic multiple-course Wazwan feasts, and international artisanal pastries across Srinagar’s modern upscale lakeside cafes.', 12),
            _ph('& TRAVEL INFORMATION', 13)
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
        tagline='Srinagar',
        overview='SRINAGAR • GULMARG PREMIUM FAMILY TOUR Welcome to paradise on earth, presented to you through an exquisite journey curated exclusively by TRAGUIN. Embark on the finest Kashmir Family Tour designed to reveal the breathtaking landscapes, misty pine valleys, and grand historic legacies of this magical region. As your premier travel consultants, TRAGUIN transforms your vacation into a seamless luxury holiday filled with handpicked hotels, iconic attractions, and deeply moving local stories. From the peaceful, floating world of a luxury Dal Lake houseboat in Srinagar to the dramatic alpine snow ridges of Gulmarg, every detail is engineered to create unforgettable memories.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers an exquisite balance between peaceful floating lakes, Mughal-era architectural heritage, and alpine mountain thrill. Travelling in a dedicated premium AC vehicle with professional chauffeur-driven assistance, your family will enjoy absolute comfort and privacy. With a carefully curated meal plan featuring lavish breakfasts and traditional multi-cuisine dinners, this route represents the definitive premium Kashmir experience. Every step of your journey includes the signature touch of TRAGUIN curated experiences, ensuring VIP entry privileges, local storytelling insight, and around-the- clock bespoke support.\n\nWHY CHOOSE THE BEST KASHMIR TOUR PACKAGE?\nWhen considering a Luxury Kashmir Holiday, discerning travellers seek more than just standard sightseeing; they seek a deeply immersive dive into culture, heritage, and contemporary comfort. Kashmir boasts some of the most iconic attractions in Northern India. From the internationally acclaimed Mughal Gardens—a top tourist place in Kashmir for heritage walks and photography—to the legendary snow fields and Gondola rides of Gulmarg, the region offers unparalleled depth. For families and couples booking a bespoke Kashmir Honeymoon Package or Kashmir Family Tour, the state reveals highly popular Instagram locations like the Shikara-filled lakes, the classic old architecture, and the stunning mountain backdrops. Whether you are looking for local pashmina shopping, indulging in traditional Wazwan culinary delights, or seeking spiritual peace, our TRAGUIN Kashmir Packages guarantee premium comfort, handpicked luxury stays, and curated exclusive experiences that make it the best time to visit Kashmir.',
        seo_title='JK-002 | Srinagar | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Kashmir package (JK-002 / TRG-KASH-002): Srinagar • Gulmarg • Dal Lake Houseboat with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SRINAGAR & MUGHAL SIGHTSEEING', 1),
            _ih('Day 02: SRINAGAR TO GULMARG EXCURSION', 2),
            _ih('Day 03: GULMARG TO SRINAGAR RETREAT', 3),
            _ih('Day 04: SRINAGAR LUXURY HOUSEBOAT EXPERIENCE', 4),
            _ih('Day 05: DEPARTURE FROM SRINAGAR', 5),
            _ih('TRAGUIN Signature Experience: Private family interaction and artisan paper-mâché craft demonstration.', 6),
            _ih('Curated by TRAGUIN Experts: Handpicked routing to avoid peak tourist congestion, maximizing your', 7),
            _ih('Premium Handpicked Hotels: Accommodations selected strictly based on premium safety standards and', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SRINAGAR & MUGHAL SIGHTSEEING',
                (
                    'WELCOME TO THE SUMMER CAPITAL – GEMS OF MUGHAL ARCHITECTURE Your premium Kashmir experience begins as you arrive at Srinagar Airport, where a dedicated private luxury transport vehicle waits to escort you. Check into your handpicked premium luxury hotel. After a refreshing afternoon, step out for an exclusive evening experience exploring the world-famous Shalimar Bagh and Nishat Bagh. These centuries-old terraced royal gardens boast majestic chinar trees and pristine fountains that create breathtaking landscapes perfect for family photography.'
                ),
                [
                    'Sightseeing Included: Nishat Bagh (Garden of Pleasure), Shalimar Bagh (Abode of Love), Cheshma Shahi.',
                    'Evening Experience: Gourmet dinner at an upscale traditional restaurant curated by TRAGUIN experts.',
                    'Overnight Stay: Srinagar (Premium / Luxury Hotel)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'SRINAGAR TO GULMARG EXCURSION',
                (
                    "MEADOW OF FLOWERS – HIGHEST CABLE CAR & ALPINE GLORY Awake early for a refreshing, crisp morning drive to Gulmarg, one of the top tourist places in Kashmir for alpine beauty. This pristine destination offers breathtaking landscapes and serves as a haven for snow sports and nature lovers. Board the world's second-highest operating cable car, the famous Gulmarg Gondola (Phase 1 & 2 included), taking you up into the clouds of Apharwat Peak. Enjoy spectacular panoramic mountain views and superb photography points."
                ),
                [
                    'Sightseeing Included: Gulmarg Gondola Ride, Strawberry Valley view, St. Mary’s Church, Golf Course.',
                    'Optional Activities: Snow skiing or ATV riding across the pristine mountain slopes.',
                    'Overnight Stay: Gulmarg (Premium Luxury Valley View Resort)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'GULMARG TO SRINAGAR RETREAT',
                (
                    "OLD TOWN LEGACY & ICONIC SHANKARACHARYA VIEWPOINTS Depart after a sumptuous breakfast back towards Srinagar. Revisit the city to scale the majestic Shankaracharya Temple hill, offering a breathtaking bird's-eye view of the entire valley and lake system. Spend your afternoon at leisure exploring local craft boutiques or enjoying the serene manicured gardens of the city. In the evening, unwind with a specialized luxury spa session back at your premium property."
                ),
                [
                    'Sightseeing Included: Shankaracharya Temple, Old City heritage walk, local saffron gardens.',
                    'Evening Experience: Private family interaction and local Kashmiri tea (Kahwa) briefing.',
                    'Overnight Stay: Srinagar (Premium Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'SRINAGAR LUXURY HOUSEBOAT EXPERIENCE',
                (
                    'FLOATING PALACES & THE ROMANTIC SHIKARA CRUISE Today brings a true highlight of your luxury Kashmir holiday. Transfer to a beautifully hand-carved, ultra- premium luxury houseboat permanently anchored on Dal Lake. In the afternoon, embark on an immersive experiences private Shikara cruise, passing through the floating vegetable markets and historic wooden bridges. Witness a pristine sunset over the water—a highly popular Instagram location perfect for your family portraiture.'
                ),
                [
                    'Sightseeing Included: Dal Lake, Floating Gardens, Nehru Park, Char Chinar island.',
                    'Evening Experience: Traditional Wazwan dinner served on board your premium luxury houseboat.',
                    'Overnight Stay: Srinagar (Premium Royal Houseboat)',
                    'Meals Included: Breakfast & Authentic Kashmiri Houseboat Dinner',
                ],
            ),
            _day(
                5,
                'DEPARTURE FROM SRINAGAR',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Indulge in a final lavish breakfast on the wooden deck of your houseboat. Your private luxury transport will safely drive you back to Srinagar International Airport for your onward journey. Return home carrying a heart filled with sweet family bonds and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door airport transfer drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Rose Petal / similar | Hotel Green Heights / similar | Deluxe Wooden Houseboat',
                'Srinagar | Gulmarg | Dal Lake Houseboat',
                '2N Srinagar|1N Gulmarg|1N Houseboat',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Rose Petal / similar | Hotel Green Heights / similar | Deluxe Wooden Houseboat | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Fortune Resort Heevan / similar | The Vintage Gulmarg / similar | Premium Group of Houseboats',
                'Srinagar | Gulmarg | Dal Lake Houseboat',
                '2N Srinagar|1N Gulmarg|1N Houseboat',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Fortune Resort Heevan / similar | The Vintage Gulmarg / similar | Premium Group of Houseboats | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Vivanta Dal View / Radisson Blu | The Khyber Himalayan Resort | Luxury Royal Palace Houseboat',
                'Srinagar | Gulmarg | Dal Lake Houseboat',
                '2N Srinagar|1N Gulmarg|1N Houseboat',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Vivanta Dal View / Radisson Blu | The Khyber Himalayan Resort | Luxury Royal Palace Houseboat | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Lalit Grand Palace (Suite) | The Khyber (Luxury Suite) | Exclusive Ultra-Luxury Private Houseboat',
                'Srinagar | Gulmarg | Dal Lake Houseboat',
                '2N Srinagar|1N Gulmarg|1N Houseboat',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Lalit Grand Palace (Suite) | The Khyber (Luxury Suite) | Exclusive Ultra-Luxury Private Houseboat | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Handpicked hotels as per chosen category.', 1),
            _inc_included('Luxury Transportation: Private AC Innova Crysta for all transfers & sightseeing.', 2),
            _inc_included('Curated Meal Plan: Daily luxury breakfast and gourmet dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest experience manager on call.', 4),
            _inc_included('Welcome Amenities: Customized family travel kit and refreshments upon arrival.', 5),
            _inc_included('Complimentary Experience: Private 1-Hour Shikara ride ticket on Dal Lake.', 6),
            _inc_excluded('Airfare / Train tickets to and from Srinagar.', 7),
            _inc_excluded('Monument entry tickets, camera fees, and local guide charges.', 8),
            _inc_excluded('Personal expenses such as laundry, liquor, telephone calls, and tips.', 9),
            _inc_excluded('Gondola ride tickets (unless specified extra in custom add-ons).', 10),
        ],
    )
    return package, itinerary

def build_jk_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JK-003'
    tour_code = 'TRG-KASH-003'
    title = 'Srinagar • Pahalgam • Gulmarg • Dal Lake'
    duration = '05 Nights / 06 Days'
    slug = 'jk-003-srinagar-pahalgam-gulmarg-dal-lake'
    itin_slug = 'jk-003-srinagar-pahalgam-gulmarg-dal-lake-itinerary'
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
            _ph('Serial code JK-003 | TRAGUIN tour code TRG-KASH-003', 1),
            _ph('State / Country: Jammu & Kashmir / India | Category: Premium Family', 2),
            _ph('Destinations: Srinagar • Pahalgam • Gulmarg • Dal Lake', 3),
            _ph('Ideal for: Family Holidays, Multi-generational Groups & Nature Lovers', 4),
            _ph('Best season: April to October (Lush Green) / December to March (Snow)', 5),
            _ph('Starting price: On Request (Premium Customised)', 6),
            _ph('Vehicle / Meals: Private Luxury Innova Crysta / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private floating family tea session on a high-end Shikara during sunset.', 8),
            _ph('Curated by TRAGUIN Experts: Seamless coordination with local high-altitude suppliers to ensure', 9),
            _ph('Premium Handpicked Hotels: Properties selected meticulously based on insulation comfort, safety, and', 10),
            _ph('Luxury Transportation: Expert drivers well-versed with mountain passes and regional valley regulations.', 11),
            _ph('Local Markets & Souvenirs: Bring home beautiful hand-knotted Pashmina shawls, genuine organic saffron strands from Pampore, hand-carved walnut wood decorative boxes, and sweet Kashmiri apples. Cafes & Food: Enjoy hot, local baked goods at historic bakeries by the river, authentic Wazwan dishes, and a refreshing cup of pink-tinted Noon Chai in Old Srinagar.', 12),
            _ph('& TRAVEL INFORMATION', 13)
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
        tagline='Srinagar',
        overview='SRINAGAR • PAHALGAM • GULMARG • DAL LAKE 05 NIGHTS / 06 DAYS Welcome to paradise on earth, beautifully unveiled through a bespoke itinerary planned exclusively by TRAGUIN. Embark on the finest Kashmir Family Tour designed to reveal the breathtaking landscapes, misty snow peaks, and timeless heritage of this magical valley. As your premier travel consultants, TRAGUIN transforms your vacation into a seamless luxury holiday filled with handpicked hotels, immersive experiences, and magical local stories. From the serene mirror-like waters of Dal Lake in Srinagar to the pine-scented meadows of Pahalgam, every single moment is curated to build unforgettable memories for you and your loved ones.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers an exquisite balance between natural wonders, alpine adventures, historic Mughal architecture, and peaceful floating stays. Travelling in a dedicated premium AC vehicle with a professional chauffeur-driven assistant, your family will experience absolute comfort, privacy, and safety. Featuring a carefully curated meal plan with rich daily breakfasts and authentic multi-course dinners, this route represents the definitive premium Kashmir experience. Every phase of your trip carries the signature touch of TRAGUIN curated experiences, ensuring VIP shikara access, expert local insights, and around-the-clock tailored concierge support.\n\nWHY CHOOSE THE BEST KASHMIR TOUR PACKAGE?\nWhen considering a Luxury Kashmir Holiday, discerning family travelers expect more than just standard sightseeing; they seek an intimate, comfortable, and authentic connection with the valley. Kashmir holds some of the most iconic attractions in India. From the classic Mughal gardens of Srinagar—a top tourist place in Kashmir for family portraits—to the world-famous ski slopes and high-altitude gondolas of Gulmarg, the possibilities are endless. For couples and families looking for a specialized Kashmir Honeymoon Package or Kashmir Family Tour, the valley offers highly popular Instagram locations like the floating vegetable markets of Dal Lake, the sweeping saffron fields of Pampore, and the snow-fed streams of Betaab Valley in Pahalgam. Whether you are bargaining for fine pashminas during local shopping, taking an alpine pony ride, or tasting local salt tea, our TRAGUIN Kashmir Packages provide premium stays, handpicked hotels, and exclusive experiences that make any season the best time to visit Kashmir.',
        seo_title='JK-003 | Srinagar | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Kashmir package (JK-003 / TRG-KASH-003): Srinagar • Pahalgam • Gulmarg • Dal Lake with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SRINAGAR & DAL LAKE LIVING', 1),
            _ih('Day 02: SRINAGAR TO PAHALGAM', 2),
            _ih('Day 03: PAHALGAM VALLEY EXPLORATION', 3),
            _ih('Day 04: PAHALGAM TO GULMARG EXCURSION / SRINAGAR RETREAT', 4),
            _ih('Day 05: SRINAGAR HERITAGE & MUGHAL SPLENDOUR', 5),
            _ih('Day 06: SRINAGAR TO DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private floating family tea session on a high-end Shikara during sunset.', 7),
            _ih('Curated by TRAGUIN Experts: Seamless coordination with local high-altitude suppliers to ensure', 8),
            _ih('Premium Handpicked Hotels: Properties selected meticulously based on insulation comfort, safety, and', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SRINAGAR & DAL LAKE LIVING',
                (
                    'WELCOME TO PARADISE – FLOATING LUXURY & THE MEMORABLE SHIKARA CRUISE Your premium Kashmir experience begins as your flight descends over the snow-capped Himalayan wall into Srinagar. Meet your private professional chauffeur and transfer directly to your handpicked premium luxury houseboat moored on the peaceful waters of Dal Lake. After an afternoon of relaxation and refreshment, step directly from your wooden deck onto a private, decorated Shikara boat. Cruise past floating gardens, local wooden hamlets, and lively water bazaars under a golden sunset.'
                ),
                [
                    'Sightseeing Included: Dal Lake, Floating Markets, Historic Waterways, local shopping outposts.',
                    'Evening Experience: Private sunset Shikara ride with authentic Kashmiri Kehwa tea served hot on board.',
                    'Overnight Stay: Srinagar (Premium / Luxury Selected Houseboat)',
                    'Meals Included: Welcome Drink & Traditional Houseboat Dinner',
                ],
            ),
            _day(
                2,
                'SRINAGAR TO PAHALGAM',
                (
                    'THE VALLEY OF SHEPHERDS – SAFFRON FIELDS & RIVERSIDE SPLENDOUR Depart after a classic breakfast on a scenic highway route toward Pahalgam, the absolute gem of any Kashmir family tour. En route, stop at the historical town of Pampore to view legendary saffron fields, and visit the historic 9th-century Awantipora temple ruins. As you reach Pahalgam, the landscape changes into dense pine forests alongside the rushing, crystal-clear Lidder River. Check into your luxury riverside resort and spend the evening enjoying the scenic beauty of the lawns.'
                ),
                [
                    'Sightseeing Included: Saffron Fields, Awantipora Ruins, Lidder River Front, Pahalgam Valley Viewpoints.',
                    'Optional Activities: Rafting on the Lidder River or a quiet evening riverside trout dinner setup.',
                    'Overnight Stay: Pahalgam (Premium Riverside Luxury Resort)',
                    'Meals Included: Premium Breakfast & Luxury Resort Buffet Dinner',
                ],
            ),
            _day(
                3,
                'PAHALGAM VALLEY EXPLORATION',
                (
                    "BEYOND THE MEADOWS – BETAAB, ARU & CHANDANWARI EXCURSIONS Awake early to a spectacular alpine morning view. Today, board local eco-vehicles for a comprehensive tour of Pahalgam's most famous attractions. Explore Betaab Valley, named after the iconic Bollywood romance film, featuring lush meadows surrounded by steep mountains. Next, ascend to the alpine village of Aru Valley, a perfect photography point. Conclude at Chandanwari, the historical starting point of the holy Amarnath Yatra pilgrimage, where snow bridges last deep into summer."
                ),
                [
                    'Sightseeing Included: Betaab Valley, Aru Eco-Reserve, Chandanwari Snow Points.',
                    'Optional Activities: Guided pony trail trek up to Baisaran Meadow (often called Mini-Switzerland).',
                    'Overnight Stay: Pahalgam (Premium Riverside Luxury Resort)',
                    'Meals Included: Premium Breakfast & Gourmet Dinner',
                ],
            ),
            _day(
                4,
                'PAHALGAM TO GULMARG EXCURSION / SRINAGAR RETREAT',
                (
                    "THE MEADOW OF FLOWERS – WORLD'S HIGHEST GONDOLA EXPERIENCE Today brings a monumental highlight of your luxury Kashmir holiday. Journey to Gulmarg, an incredible alpine meadow of flowers. Board the famous multi-stage Gulmarg Gondola, one of the highest cable car networks on the globe. Ascend through the pine canopy to Kongdoori (Phase 1) and continue upward to the snow slopes of Apharwat Peak (Phase 2) at over 13,000 feet. Experience the breathtaking landscapes of the Pir Panjal range before returning to Srinagar for a relaxing evening."
                ),
                [
                    'Sightseeing Included: Gulmarg Meadow, Outer Circle Drive, Multi-stage Gondola System, Apharwat Peak views.',
                    'Evening Experience: Pre-booked VIP priority passes for the Gondola ride provided via TRAGUIN experts.',
                    'Overnight Stay: Srinagar (Premium Luxury Land Hotel)',
                    'Meals Included: Premium Breakfast & Fine Dining Dinner',
                ],
            ),
            _day(
                5,
                'SRINAGAR HERITAGE & MUGHAL SPLENDOUR',
                (
                    'ROYAL ARCHITECTURE & HISTORIC GARDEN WALKS Spend a beautiful day uncovering the architectural legacy and scenic beauty of Srinagar. Tour the world- renowned Mughal Gardens, including Nishat Bagh (Garden of Pleasure) and Shalimar Bagh (Abode of Love), built by Emperor Shah Jahan along the lake terraces. Visit the beautiful Pari Mahal historic monument and check out the Chashme Shahi royal springs. Spend your afternoon diving into authentic old-city shopping for world-famous Kashmiri paper-mâché art, hand-knotted silk carpets, and walnuts.'
                ),
                [
                    'Sightseeing Included: Nishat Bagh, Shalimar Bagh, Pari Mahal, Chashme Shahi, Shankaracharya Temple Hill.',
                    'Optional Activities: A private traditional Wazwan multi-course royal culinary lunch experience.',
                    'Overnight Stay: Srinagar (Premium Luxury Land Hotel)',
                    'Meals Included: Premium Breakfast & Farewell Special Dinner',
                ],
            ),
            _day(
                6,
                'SRINAGAR TO DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS Enjoy a final luxury breakfast at your premium hotel while looking out over the misty mountain silhouette. Pack your luggage and boarding passes as your private luxury transport vehicle sweeps you smoothly to Srinagar International Airport for your flight home. Return home carrying a mind filled with peace and unforgettable memories designed meticulously by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury airport departure drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Heevan / Rose Petal / similar | Hotel Hilltop / Resort Water View | Royal Houseboat Group / similar',
                'Srinagar | Pahalgam | Dal Lake Houseboat',
                '1N Houseboat|2N Pahalgam|2N Srinagar',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Heevan / Rose Petal / similar | Hotel Hilltop / Resort Water View | Royal Houseboat Group / similar | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Lemon Tree Hotel / similar | Pahalgam Hotel / Grand Mumtaz | Meena Group Houseboats / similar',
                'Srinagar | Pahalgam | Dal Lake Houseboat',
                '1N Houseboat|2N Pahalgam|2N Srinagar',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Lemon Tree Hotel / similar | Pahalgam Hotel / Grand Mumtaz | Meena Group Houseboats / similar | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Radisson Blu Srinagar / Vivanta | Welcomhotel by ITC Pine & Peak | Sukoon Luxury Houseboat / Deluxe',
                'Srinagar | Pahalgam | Dal Lake Houseboat',
                '1N Houseboat|2N Pahalgam|2N Srinagar',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Radisson Blu Srinagar / Vivanta | Welcomhotel by ITC Pine & Peak | Sukoon Luxury Houseboat / Deluxe | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Lalit Grand Palace Srinagar | The Grand Mumtaz Royal Suite View | Signature Super-Luxury Private Suite Houseboat',
                'Srinagar | Pahalgam | Dal Lake Houseboat',
                '1N Houseboat|2N Pahalgam|2N Srinagar',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Lalit Grand Palace Srinagar | The Grand Mumtaz Royal Suite View | Signature Super-Luxury Private Suite Houseboat | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Selected luxury properties and houseboats as listed.', 1),
            _inc_included('Luxury Transportation: Private AC Innova Crysta for all transfers & valley routes.', 2),
            _inc_included('Curated Meal Plan: Daily premium breakfast and grand multi-course dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest relation officer and on-ground help.', 4),
            _inc_included('Welcome Amenities: Personalized kashmiri family welcome pack & dry fruit basket.', 5),
            _inc_included('Complimentary Experience: 01-Hour private sunset Shikara tour on Dal Lake.', 6),
            _inc_included('TRAGUIN Premium Luxury Itinerary — JK-003 5', 7),
            _inc_excluded('Domestic/International flights or train fare to Srinagar.', 8),
            _inc_excluded('Gulmarg Gondola ride tickets and local Pahalgam union taxi charges.', 9),
            _inc_excluded('Personal expenses such as laundry, phone bills, traditional outfits, and tips.', 10),
            _inc_excluded('Any activity fees, horse/pony rides, or extra tours not mentioned.', 11),
        ],
    )
    return package, itinerary

def build_jk_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JK-004'
    tour_code = 'TRG-KASH-004'
    title = 'Romantic Kashmir — An Ethereal Love Story in Paradise'
    duration = '05 Nights / 06 Days'
    slug = 'jk-004-romantic-kashmir-honeymoon'
    itin_slug = 'jk-004-romantic-kashmir-honeymoon-itinerary'
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
            _ph('Serial code JK-004 | TRAGUIN tour code TRG-KASH-004', 1),
            _ph('State / Country: Jammu & Kashmir / India | Category: Luxury', 2),
            _ph('Destinations: Srinagar • Gulmarg • Pahalgam • Dal Lake Houseboat', 3),
            _ph('Ideal for: Newlyweds, Couples & Romantic Travelers', 4),
            _ph('Best season: April to October (Lush Greens) / December to March (Snowfall)', 5),
            _ph('Starting price: On Request (Premium Bespoke Customization)', 6),
            _ph('Vehicle / Meals: Private Luxury Innova Crysta / MAPAI Plan', 7),
            _ph('TRAGUIN Signature Experience: Private family or couple orientation briefing with local heritage', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked routing to guarantee scenic luxury drives while avoiding', 9),
            _ph('Premium Handpicked Hotels: Accommodations thoroughly evaluated for safety, spectacular valley-facing', 10),
            _ph('Exclusive Recommendations: Tailored dining recommendations at highly rated hidden gems across Old', 11),
            _ph('Traditional Souvenirs: Bring home world-renowned genuine Pashmina shawls, fine hand-knotted silk carpets, exquisite paper mâché art decor, walnut wood carvings, and authentic organic Kashmiri saffron. Cafes & Food: Indulge in traditional local bakeries (Kandur tsot), sip authentic pink noon-chai, visit chic lake- view cafés, and savor a legendary multi-course royal Wazwan meal banquet.', 12),
            _ph('& TRAVEL INFORMATION', 13)
        ],
        moods=['Romantic', 'Honeymoon', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Bespoke Customization)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Romantic Kashmir — An Ethereal Love Story in Paradise',
        overview='ROMANTIC KASHMIR • AN ETHEREAL LOVE STORY IN PARADISE Welcome to paradise on earth, intimately curated by TRAGUIN. Embark on the definitive Kashmir Honeymoon Package, designed to weave your love story into the breathtaking landscapes, misty valleys, and calm crystalline waters of this heavenly region. As your trusted luxury travel consultants, TRAGUIN guarantees an elite experience characterized by handpicked hotels, private premium stays, and deeply moving storytelling. From romantic Shikara rides at sunset to the majestic white peaks of Gulmarg, every destination promises to leave you with unforgettable memories.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package represents the absolute pinnacle of luxury travel. Your journey traces a magnificent route across Kashmir, blending high-end adventure, historical Mughal grandeur, and quiet alpine privacy. Travelling in a dedicated private premium vehicle with an experienced local chauffeur, you will enjoy seamless transfers. With a meticulously planned meal plan featuring lavish breakfasts and specialized traditional dinners, this itinerary embodies a premium Kashmir experience. Every day features signature TRAGUIN curated experiences, assuring personalized VIP assistance and romantic surprises along the way.\n\nWHY CHOOSE THE BEST KASHMIR TOUR PACKAGE?\nWhen planning a Luxury Kashmir Holiday, discerning couples seek an exquisite balance of royal heritage, alpine adventure, and pristine natural beauty. Kashmir stands unrivaled as an elite romantic destination, making a specialized Kashmir Honeymoon Package the ultimate celebration of your union. From the poetic tranquility of a luxury Dal Lake houseboat to the snow-covered gondola phases, Kashmir sightseeing provides an unmatched timeless escape. Our comprehensive Kashmir Family Tour and couple itineraries connect you directly to the top tourist places in Kashmir, including the ancient Shalimar Bagh, Nishat Bagh, the sweeping Betaab Valley, and the majestic meadow of gold—Sonamarg. Capture everlasting memories at highly popular Instagram locations like the floating flower markets or inside traditional hand-carved cedarwood corridors. Book your trip during the best time to visit Kashmir to experience local saffron farm walks, exquisite Pashmina shawl shopping, and authentic Wazwan cuisine. With our premier TRAGUIN Kashmir Packages, you enjoy curated exclusive experiences and handpicked hotels that elevate your vacation into pure magic.',
        seo_title='JK-004 | Romantic Kashmir — An Ethereal Love Story in Paradise | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Kashmir package (JK-004 / TRG-KASH-004): Srinagar • Gulmarg • Pahalgam • Dal Lake Houseboat with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SRINAGAR & LUXURY HOUSEBOAT STAY', 1),
            _ih('Day 02: SRINAGAR TO GULMARG EXCURSION', 2),
            _ih('Day 03: GULMARG TO PAHALGAM', 3),
            _ih('Day 04: PAHALGAM VALLEY EXPLORATION', 4),
            _ih('Day 05: PAHALGAM TO SRINAGAR MUGHAL SIGHTSEEING', 5),
            _ih('Day 06: SRINAGAR / DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private family or couple orientation briefing with local heritage', 7),
            _ih('Curated by TRAGUIN Experts: Handpicked routing to guarantee scenic luxury drives while avoiding', 8),
            _ih('Premium Handpicked Hotels: Accommodations thoroughly evaluated for safety, spectacular valley-facing', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SRINAGAR & LUXURY HOUSEBOAT STAY',
                (
                    'ROMANTIC SHIKARA RIDE & THE FLOATING PARADISE Your premium Kashmir experience begins as you step off the plane at Srinagar Airport. You will be warmly welcomed by your private luxury transport chauffeur who will transfer you seamlessly to a beautifully handpicked ultra-luxury houseboat docked gracefully on Dal Lake. After checking in and enjoying traditional Kashmiri Kahwa, embark on an immersive 1-hour private Shikara cruise across the lake. Witness the breathtaking landscapes of the Zabarwan mountain range reflecting off the water as the sun dips below the horizon. deck candlelight setup.'
                ),
                [
                    'Sightseeing Included: Dal Lake, Private Sunset Shikara Ride, Floating Gardens, local wooden markets.',
                    'Evening Experience: Honeymoon Special: Custom wedding cake, romantic floral bed decoration, and a private',
                    'Overnight Stay: Srinagar (Premium / Ultra-Luxury Carved Houseboat)',
                    'Meals Included: Welcome Drink, Kahwa & Gourmet Houseboat Dinner',
                ],
            ),
            _day(
                2,
                'SRINAGAR TO GULMARG EXCURSION',
                (
                    'THE MEADOW OF FLOWERS & HIGHEST GONDOLA EXPERIENCE Awake to a serene lakeside morning and indulge in a lavish breakfast. Today, take a scenic route to Gulmarg, a world-famous alpine meadow and a top tourist place in Kashmir. Board the iconic high-altitude Gulmarg Gondola (Phase 1 & 2), ascending above 13,000 feet into the clouds. Marvel at the breathtaking landscapes of the Apharwat Peak, completely covered in glistening pristine white snow. Walk hand-in-hand through the snow meadows or capture beautiful cinematic photos. Palace.'
                ),
                [
                    "Sightseeing Included: Gulmarg Meadows, Gondola Cable Car Ride (Phases I & II), St. Mary's Church, Maharaja",
                    'Optional Activities: Snow biking, professional alpine couple photography session, or high-altitude skiing.',
                    'Overnight Stay: Gulmarg (Premium Mountain Luxury Resort)',
                    'Meals Included: Premium Breakfast & Exquisite Dinner Buffet',
                ],
            ),
            _day(
                3,
                'GULMARG TO PAHALGAM',
                (
                    "THE VALLEY OF SHEPHERDS & SAFFRON FIELDS ROUTE Depart after a sumptuous breakfast toward the breathtaking valley of Pahalgam. En route, your private vehicle will pause at the legendary Pampore Saffron Fields, where the world's most premium spices grow. Drive past the historic Awantipora Ruins and continue alongside the sparkling Lidder River. Upon arrival in Pahalgam, check into a handpicked premium hotel offering unmatched views of pine forests and snowy crags."
                ),
                [
                    'Sightseeing Included: Saffron Field Trails, Lidder River Front, Awantipora Heritage Temple Ruins.',
                    'Evening Experience: A private riverside bonfire experience with customized acoustic soft music setup.',
                    'Overnight Stay: Pahalgam (Luxury Valley-Facing Premium Resort)',
                    'Meals Included: Breakfast & Traditional Elite Wazwan-inspired Dinner',
                ],
            ),
            _day(
                4,
                'PAHALGAM VALLEY EXPLORATION',
                (
                    'CINEMATIC VALLEYS & SCENIC RIVERSIDE MAJESTY Spend a magnificent day exploring the legendary valleys of Pahalgam in a localized eco-transport system. Visit Betaab Valley, famously named after the Bollywood film and known for its lush green meadows and rushing crystal streams. Explore Aru Valley, a serene, postcard-perfect eco-village, and Chandanwari, the historical starting base of the holy Amarnath Yatra. It is a highly popular Instagram location perfect for romantic couple portraits. ride).'
                ),
                [
                    'Sightseeing Included: Betaab Valley, Aru Valley, Chandanwari Snowy Trails, Baisaran Valley (Optional via pony',
                    'Food Suggestions: Try authentic wood-fired Trout fish at an upscale riverside bistro.',
                    'Overnight Stay: Pahalgam (Luxury Valley-Facing Premium Resort)',
                    "Meals Included: Premium Breakfast & Gourmet Chef's Special Dinner",
                ],
            ),
            _day(
                5,
                'PAHALGAM TO SRINAGAR MUGHAL SIGHTSEEING',
                (
                    "ROYAL GARDENS & IMPERIAL HERITAGE Drive back to Srinagar today to discover its historic Mughal splendor. Tour the world-famous Nishat Bagh (Garden of Pleasure) and Shalimar Bagh (Abode of Love), built by Mughal emperors for their beloved queens. Stroll alongside fountains, terrace pools, and ancient chinar trees. Later, visit the spectacular Pari Mahal overlooks, offering panoramic bird's-eye views of the entire Dal Lake valley before checking into your city resort."
                ),
                [
                    'Sightseeing Included: Shalimar Bagh, Nishat Bagh, Chashme Shahi, Pari Mahal, Shankaracharya Temple Hilltop.',
                    'Optional Activities: Private heritage artisan tour to witness the live weaving of elite Pashmina carpets.',
                    'Overnight Stay: Srinagar (Premium Luxury City Hotel)',
                    'Meals Included: Breakfast & Farewell Premium Candlelight Dinner',
                ],
            ),
            _day(
                6,
                'SRINAGAR / DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Indulge in a final lavish breakfast at your premium hotel. Spend some quiet moments packing souvenirs and handicrafts. Your private luxury transport will safely drive you to Srinagar Airport for your onward journey home. Return with a heart filled with endless love and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door airport drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Grand Mumtaz | Hotel Royal Park / similar | Hotel Mountview / similar | Meena Group Houseboats / similar',
                'Srinagar | Gulmarg | Pahalgam | Dal Lake Houseboat',
                '1N Houseboat|1N Srinagar|1N Gulmarg|2N Pahalgam',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Grand Mumtaz | Hotel Royal Park / similar | Hotel Mountview / similar | Meena Group Houseboats / similar | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Hotel Hilltop / Grand Mumtaz | Hotel Hilltop / Grand Mumtaz | Pahalgam Hotel / Hotel Heavan | Wangnoo Luxury Houseboats / Fortun',
                'Srinagar | Gulmarg | Pahalgam | Dal Lake Houseboat',
                '1N Houseboat|1N Srinagar|1N Gulmarg|2N Pahalgam',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Hotel Hilltop / Grand Mumtaz | Hotel Hilltop / Grand Mumtaz | Pahalgam Hotel / Hotel Heavan | Wangnoo Luxury Houseboats / Fortune Heavan | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Vivanta by Taj Dal View | The Vintage Gulmarg / The Rosewood | Welcomhotel by ITC Pine n Peak | Mascot Luxury Houseboats / Vivan',
                'Srinagar | Gulmarg | Pahalgam | Dal Lake Houseboat',
                '1N Houseboat|1N Srinagar|1N Gulmarg|2N Pahalgam',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Vivanta by Taj Dal View | The Vintage Gulmarg / The Rosewood | Welcomhotel by ITC Pine n Peak | Mascot Luxury Houseboats / Vivanta by Taj Dal View | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Lalit Grand Palace | The Khyber Himalayan Resort & Spa | The Grand Mumtaz Royal Suites / Private Villa | Sukoon Luxury House',
                'Srinagar | Gulmarg | Pahalgam | Dal Lake Houseboat',
                '1N Houseboat|1N Srinagar|1N Gulmarg|2N Pahalgam',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Lalit Grand Palace | The Khyber Himalayan Resort & Spa | The Grand Mumtaz Royal Suites / Private Villa | Sukoon Luxury Houseboat / The Lalit Grand Palace | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury accommodations as per chosen tier.', 1),
            _inc_included('Luxury Transportation: Private dedicated AC Innova Crysta for all sightseeing.', 2),
            _inc_included('Curated Meal Plan: Lavish daily breakfast and customized gourmet dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest experience manager assistance.', 4),
            _inc_included('Welcome Amenities: Personalized travel kits, flower bouquets, and arrival treats.', 5),
            _inc_included('Complimentary Experience: 1-Hour private sunset Shikara boat cruise.', 6),
            _inc_included('TRAGUIN Premium Luxury Itinerary — JK-004 5', 7),
            _inc_excluded('Airfare, flight tickets, or long-distance train bookings.', 8),
            _inc_excluded('Gulmarg Gondola tickets (must be booked online via JKVDC directly).', 9),
            _inc_excluded('Pony ride charges, local valley internal cabs, and ski kit rentals.', 10),
            _inc_excluded('Personal expenses such as laundry, phone calls, or tips.', 11),
        ],
    )
    return package, itinerary

def build_jk_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JK-005'
    tour_code = 'TRG-KASH-005'
    title = 'Tulip Romance — A Dreamy Luxury Kashmir Holiday'
    duration = '04 Nights / 05 Days'
    slug = 'jk-005-tulip-romance-kashmir-honeymoon'
    itin_slug = 'jk-005-tulip-romance-kashmir-honeymoon-itinerary'
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
            _ph('Serial code JK-005 | TRAGUIN tour code TRG-KASH-005', 1),
            _ph('State / Country: Jammu & Kashmir / India | Category: Premium', 2),
            _ph('Destinations: Srinagar • Gulmarg • Pahalgam • Dal Lake Houseboat', 3),
            _ph('Ideal for: Newlyweds, Romantics & Luxury Enthusiasts', 4),
            _ph('Best season: April to May (Tulip Festival Peak Season)', 5),
            _ph('Starting price: On Request (Bespoke Luxury Honeymoon)', 6),
            _ph('Vehicle / Meals: Private Luxury Innova Crysta / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private family interaction and historical storytelling briefing before', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked routing to avoid highway traffic, maximizing your leisure and', 9),
            _ph('Exclusive Recommendations: VIP access parameters to select evening ceremonies and fine-dining', 10),
            _ph("Local Markets & Souvenirs: Explore the heritage bazaars to find hand-knotted silk carpets, authentic pashmina shawls, walnut wood carvings, and beautiful papier-mâché artifacts. Don't forget to pick up premium Kashmiri saffron and fresh almonds. Cafes & Food: Old Srinagar features lovely, historic tea lounges where you can sip traditional hot Kashmiri Kahwa (saffron green tea with almonds) and try delicious, authentic bakery treats like baked Girda bread.", 11),
            _ph('& TRAVEL INFORMATION', 12)
        ],
        moods=['Romantic', 'Honeymoon', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Bespoke Luxury Honeymoon)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Tulip Romance — A Dreamy Luxury Kashmir Holiday',
        overview='TULIP ROMANCE • A DREAMY LUXURY KASHMIR HOLIDAY Welcome to paradise on earth, a romantic fairytale designed flawlessly by TRAGUIN. Embark on our exclusive Kashmir Honeymoon Package, specifically timed with the world-renowned spring awakening of millions of blooming flowers. As your trusted premium travel consultants, TRAGUIN transforms this scenic getaway into a flawless luxury holiday complete with premium stays, romantic surprises, and immersive experiences. Witness the breathtaking landscapes of snow-dusted mountains framing oceans of multi- colored tulips, building unforgettable memories that you will cherish together forever.\n\nTOUR OVERVIEW\nThis elite curated itinerary offers the perfect balance between high-altitude mountain romance, timeless cultural heritage, and sheer natural bliss. Traveling in a fully private, chauffeured premium vehicle, you will traverse alpine routes in absolute seclusion and luxury. Enjoy an exquisite meal plan that provides lavish breakfast buffers and private candlelit dinners across the journey. Complete with specialized honeymoon add- ons—such as a premium Shikara photo session, floral room art, and a gourmet cake celebration—this represents the ultimate premium Kashmir experience. Every phase features the signature touch of TRAGUIN curated experiences, elevating your trip from a standard vacation to a true masterpiece.\n\nWHY CHOOSE THE BEST KASHMIR TOUR PACKAGE?\nWhen planning a Luxury Kashmir Holiday, couples look for unparalleled mountain beauty, historical architecture, and unmatched intimacy. Srinagar, the heart of the valley, stands out as a dream destination, making a specialized Kashmir Honeymoon Package the ultimate choice for couples. From strolling through the legendary, manicured Mughal Gardens to experiencing the absolute magic of the Indira Gandhi Memorial Tulip Garden—the primary iconic attraction during spring—Kashmir sightseeing offers deep emotional storytelling and spectacular sensory wonder. Our tailored Kashmir Family Tour and romantic designs guide you effortlessly through top tourist places in Kashmir. Take a striking photo at popular Instagram locations like the floating markets of Dal Lake, the golden alpine meadow views of Gulmarg, and the rushing turquoise rivers of Pahalgam. Whether you are indulging in local walnut wood handicraft shopping at the historic markets, relishing an upscale multi-course authentic Kashmiri Wazwan meal, or flying above pine-lined forests on the Gulmarg Gondola, our specialized TRAGUIN Kashmir Packages provide handpicked hotels and exclusive experiences that align perfectly with the best time to visit Kashmir.',
        seo_title='JK-005 | Tulip Romance — A Dreamy Luxury Kashmir Holiday | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Kashmir package (JK-005 / TRG-KASH-005): Srinagar • Gulmarg • Pahalgam • Dal Lake Houseboat with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SRINAGAR & DAL LAKE HOUSEBOAT', 1),
            _ih('Day 02: SRINAGAR MUGHAL GARDENS & TULIP FESTIVAL', 2),
            _ih('Day 03: SRINAGAR TO GULMARG EXCURSION', 3),
            _ih('Day 04: SRINAGAR TO PAHALGAM EXCURSION', 4),
            _ih('Day 05: DEPARTURE FROM SRINAGAR', 5),
            _ih('TRAGUIN Signature Experience: Private family interaction and historical storytelling briefing before', 6),
            _ih('Curated by TRAGUIN Experts: Handpicked routing to avoid highway traffic, maximizing your leisure and', 7),
            _ih('Exclusive Recommendations: VIP access parameters to select evening ceremonies and fine-dining', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SRINAGAR & DAL LAKE HOUSEBOAT',
                (
                    'FLOATING LUXURY & THE MAGIC OF THE SHIKARA CRUISE Your premium Kashmir experience begins as you land at Srinagar Airport, where a dedicated private luxury transport vehicle waits to escort you. Transfer directly to the shores of the serene Dal Lake and board a traditionally crafted luxury wooden houseboat. After a refreshing afternoon rest, step out for an exclusive, private evening Shikara experience. Glide along the mirror-calm waters while listening to soft folk tunes, passing floating gardens and ancient wooden houses during sunset. houseboat suite.'
                ),
                [
                    'Sightseeing Included: Dal Lake, Floating Markets, Historic wooden architecture canals.',
                    'Evening Experience: Honeymoon Special: Custom arrival cake and a beautiful floral decoration in your premium',
                    'Overnight Stay: Srinagar (Premium Luxury Floating Houseboat)',
                    'Meals Included: Welcome Drink & Royal Kashmiri Dinner',
                ],
            ),
            _day(
                2,
                'SRINAGAR MUGHAL GARDENS & TULIP FESTIVAL',
                (
                    'THE TULIP ROMANCE – OCEANS OF SPRING COLOURS Awake to a peaceful misty lake view and enjoy breakfast before entering the world-renowned Indira Gandhi Memorial Tulip Garden, nestled beautifully against the Zabarwan mountain range. Walk hand-in-hand past rows of millions of blooming tulips, making this a highly popular Instagram location for couple portraits. Continue your premium Kashmir experience into the majestic Mughal heritage grounds, exploring the terraced lawns of Nishat Bagh (Garden of Pleasure) and Shalimar Bagh (Abode of Love), filled with cascading stone fountains. tulips.'
                ),
                [
                    'Sightseeing Included: Indira Gandhi Memorial Tulip Garden, Nishat Bagh, Shalimar Bagh, Chashme Shahi.',
                    'Optional Activities: Bespoke couple photography session in traditional Kashmiri attire (Pheran) amidst the',
                    'Overnight Stay: Srinagar (Handpicked Premium Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Gourmet Dinner',
                ],
            ),
            _day(
                3,
                'SRINAGAR TO GULMARG EXCURSION',
                (
                    'MEADOW OF GOLD & THE HIGH-ALTITUDE GONDOLA EXPERIENCE Depart after breakfast on a scenic mountain drive to Gulmarg, the crown jewel of winter sports and pristine alpine meadows. Board the world’s second-highest cable car, the Gulmarg Gondola. Ascend past towering pine forests up to Phase 1 (Kongdoori) and Phase 2 (Apharwat Peak), where breathtaking landscapes of pure white snow meet the deep blue sky. Walk along the high ridges or capture unforgettable memories with a dramatic couple photoshoot. Return to Srinagar in the late evening. hotel.'
                ),
                [
                    "Sightseeing Included: Gulmarg Alpine Meadows, Gondola Rides (Phase 1 & 2), St. Mary's Heritage Church.",
                    'Evening Experience: Bespoke candlelit dinner with a premium menu curated by TRAGUIN experts back at your',
                    'Overnight Stay: Srinagar (Handpicked Premium Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Intimate Candlelit Dinner',
                ],
            ),
            _day(
                4,
                'SRINAGAR TO PAHALGAM EXCURSION',
                (
                    'THE VALLEY OF SHEPHERDS – RIVERSIDE SERENITY Today, take a breathtaking drive through expansive saffron fields and pine-fringed roads to Pahalgam. Known as the Valley of Shepherds, this iconic attraction is famous for its raw scenic beauty. Walk along the rushing Lidder River, listen to the water against the rocks, and explore the beautiful Betaab Valley, named after a famous Bollywood romance film. Enjoy a quiet stroll through the meadows of Aru Valley before heading back to Srinagar. Switzerland).'
                ),
                [
                    'Sightseeing Included: Lidder River Valley, Betaab Valley, Aru Valley, Saffron Field viewpoints.',
                    'Optional Activities: Private horseback trail ride up to the high panoramic meadows of Baisaran (Mini',
                    'Overnight Stay: Srinagar (Handpicked Premium Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Farewell Multi-cuisine Dinner',
                ],
            ),
            _day(
                5,
                'DEPARTURE FROM SRINAGAR',
                (
                    'CHERISHING THE PARADISE – MEMORIES BEYOND DESTINATIONS Indulge in a final lavish breakfast at your premium hotel, overlooking the misty hills. Take a quiet morning walk for any last-minute souvenir shopping before your private luxury transport vehicle carries you safely back to Srinagar Airport. Board your flight home with a heart full of romance and unforgettable memories designed meticulously by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury airport departure drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Pine Spring / Orchard Retreat | Royal Group Houseboats / similar',
                'Srinagar | Dal Lake Houseboat',
                '1N Houseboat|3N Srinagar',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Pine Spring / Orchard Retreat | Royal Group Houseboats / similar | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Lemon Tree Hotel / Fortune Riviera | Kashmir Oasis Houseboat / similar',
                'Srinagar | Dal Lake Houseboat',
                '1N Houseboat|3N Srinagar',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Lemon Tree Hotel / Fortune Riviera | Kashmir Oasis Houseboat / similar | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Radisson Collection / Vivanta Dal View | The Grand Palace Houseboat Group',
                'Srinagar | Dal Lake Houseboat',
                '1N Houseboat|3N Srinagar',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Radisson Collection / Vivanta Dal View | The Grand Palace Houseboat Group | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Lalit Grand Palace (Heritage Suite) | Sukoon Luxury Cruise Houseboat',
                'Srinagar | Dal Lake Houseboat',
                '1N Houseboat|3N Srinagar',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Lalit Grand Palace (Heritage Suite) | Sukoon Luxury Cruise Houseboat | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 04 Nights split between a luxury houseboat and handpicked hotels.', 1),
            _inc_included('Luxury Transportation: Private AC Innova Crysta for all point-to-point transfers.', 2),
            _inc_included('Curated Meal Plan: Daily premium buffet breakfast and multi-course dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated local guest experience manager assistance.', 4),
            _inc_included('Welcome Amenities: Personalized travel welcome kit and refreshing beverages.', 5),
            _inc_included('Complimentary Experience: 01-Hour private evening Shikara cruise on Dal Lake.', 6),
            _inc_excluded('Domestic or international flight tickets to and from Srinagar.', 7),
            _inc_excluded('Gondola cable car ride tickets (can be pre- booked on request).', 8),
            _inc_excluded('Monument entry tickets, local camera permissions, and destination guide fees.', 9),
            _inc_excluded('Personal expenses such as laundry, liquor, telephone calls, or driver tips.', 10),
        ],
    )
    return package, itinerary

def build_jk_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JK-006'
    tour_code = 'TRG-KASH-006'
    title = 'Luxury Kashmir Escape — Paradise on Earth Reimagined'
    duration = '06 Nights / 07 Days'
    slug = 'jk-006-luxury-kashmir-escape'
    itin_slug = 'jk-006-luxury-kashmir-escape-itinerary'
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
            _ph('Serial code JK-006 | TRAGUIN tour code TRG-KASH-006', 1),
            _ph('State / Country: Jammu & Kashmir / India | Category: Luxury Holiday /', 2),
            _ph('Destinations: Srinagar • Gulmarg • Pahalgam • Sonamarg', 3),
            _ph('Ideal for: Couples, Connoisseurs of Luxury, Family Milestones', 4),
            _ph('Best season: April to October (Lush Greenery) / December to March (Snow)', 5),
            _ph('Starting price: Premium Bespoke Quote On Request', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / Premium MAPAI Breakfast & Dinner', 7),
            _ph('TRAGUIN Signature Experience: Private family tea ceremony on a floating platform in the middle of Dal', 8),
            _ph('Curated by TRAGUIN Experts: Seamlessly planned daily routes to ensure you beat the crowds at major', 9),
            _ph('Premium Handpicked Hotels: Accommodations vetted for top-tier central heating, spectacular balcony', 10),
            _ph('Personalized Assistance: Dedicated airport check-in support and luggage handler privileges.', 11),
            _ph('Local Markets & Souvenirs: Visit historic artisan showrooms to discover authentic Pashmina shawls, intricate hand-knotted silk carpets, hand-painted paper-mâché decorative items, and pure organic Kashmiri saffron. Food Recommendations: Savor a traditional slow-cooked Wazwan feast, sample street-side hot mutton seekh kababs at Khayam Chowk, and enjoy soothing pink Noon Chai alongside flaky local Bakarkhani breads.', 12),
            _ph('& TRAVEL INFORMATION', 13)
        ],
        moods=['Luxury', 'Family', 'Honeymoon'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='Premium Bespoke Quote On Request',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Luxury Kashmir Escape — Paradise on Earth Reimagined',
        overview='LUXURY KASHMIR ESCAPE • PARADISE ON EARTH REIMAGINED Welcome to a timeless journey into absolute paradise, masterfully designed by TRAGUIN. Embark on the definitive Luxury Kashmir Holiday created specifically to connect your soul with the breathtaking landscapes, emerald valleys, and snow-draped horizons of India’s crown jewel. As your elite travel consultants, TRAGUIN transforms this vacation into an extraordinary masterpiece filled with premium stays, intimate cultural encounters, and seamless hospitality. Every element of this itinerary has been handpicked to give you and your loved ones a lifetime of unforgettable memories.\n\nTOUR OVERVIEW\nThis elite Premium Kashmir Experience features an extraordinary route weaving through the historic charm of Srinagar, the high-altitude meadows of Gulmarg, the serene pine-scented rivers of Pahalgam, and the glacier-carved pathways of Sonamarg. Travelling in an exclusive, chauffeur-driven luxury vehicle, you will experience the peaks of safety and relaxation. Our bespoke meal plan features extensive gourmet breakfasts and decadent dinners at each property. Enhanced by a specialized TRAGUIN curated experience note, your holiday grants you private access privileges, handpicked hotels, and premium assistance at every stage.\n\nWHY CHOOSE THE BEST KASHMIR TOUR PACKAGE?\nWhen considering the ultimate Luxury Kashmir Holiday, travelers demand a perfect marriage of pristine natural scenery and curated exclusive experiences. Kashmir boasts some of the most iconic attractions in the world. From the tranquil waters of Dal Lake to the famous Mughal Gardens, Srinagar sightseeing offers a portal into royal history. For couples planning a dreamy Kashmir Honeymoon Package or families booking a comprehensive Kashmir Family Tour, the region reveals highly sought-after, popular Instagram locations such as the vibrant floating flower markets, the Gondola cable car lines in Gulmarg, and the rolling meadows of Betaab Valley. Whether you seek high-altitude alpine adventures, premium shopping for exquisite Pashmina and carpets, or quiet meditation amidst scenic beauty, our signature TRAGUIN Kashmir Packages provide unparalleled hospitality during the best time to visit Kashmir.',
        seo_title='JK-006 | Luxury Kashmir Escape — Paradise on Earth Reimagined | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Kashmir package (JK-006 / TRG-KASH-006): Srinagar • Gulmarg • Pahalgam • Sonamarg with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SRINAGAR & DAL LAKE CRUISE', 1),
            _ih('Day 02: SRINAGAR MUGHAL GARDENS SIGHTSEEING', 2),
            _ih('Day 03: SRINAGAR TO SONAMARG EXCURSION', 3),
            _ih('Day 04: SRINAGAR TO GULMARG MEADOW OF FLOWERS', 4),
            _ih('Day 05: GULMARG TO PAHALGAM THE VALLEY OF SHEPHERDS', 5),
            _ih('Day 06: PAHALGAM VALLEY EXCURSION', 6),
            _ih('Day 07: PAHALGAM TO SRINAGAR / DEPARTURE', 7),
            _ih('TRAGUIN Signature Experience: Private family tea ceremony on a floating platform in the middle of Dal', 8),
            _ih('Curated by TRAGUIN Experts: Seamlessly planned daily routes to ensure you beat the crowds at major', 9),
            _ih('Premium Handpicked Hotels: Accommodations vetted for top-tier central heating, spectacular balcony', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SRINAGAR & DAL LAKE CRUISE',
                (
                    'WELCOME TO THE CITY OF LAKES – ICONIC SHIKARA EXPERIENCE Your exceptional luxury vacation begins as you touch down at Srinagar Airport. You will be greeted with a warm traditional welcome note by your dedicated private chauffeur and escorted in a premium luxury SUV. Check into an ultra-luxury handpicked Houseboat anchored elegantly on Dal Lake. In the afternoon, enjoy a private, hand-paddled Shikara cruise across the glass-like waters, passing floating gardens and historic wooden hamlets. Take stunning photographs against the dramatic Zabarwan mountain range as the sun sets over the valley. houseboat.'
                ),
                [
                    'Sightseeing Included: Dal Lake, Floating Markets, Historic Water Channels, Charcoal Sunset Cruise.',
                    'Evening Experience: An exclusive multi-course Kashmiri Wazwan welcoming dinner onboard the luxury',
                    'Overnight Stay: Srinagar (Premium Ultra-Luxury Royal Houseboat)',
                    'Meals Included: Welcome Kehwa, Premium High-Tea & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'SRINAGAR MUGHAL GARDENS SIGHTSEEING',
                (
                    'ROYAL ARCHITECTURE, BLOSSOMING TERRACES & HERITAGE PERFECTION Awake to the soothing sounds of water and indulge in a lavish breakfast. Spend your day discovering the magnificent top tourist places in Kashmir. Explore Nishat Bagh (The Garden of Pleasure) and Shalimar Bagh (The Abode of Love), built by Mughal Emperors with flowing water cascades and ancient chinar trees. Later, visit the beautiful Pari Mahal terraced lawn for a panoramic view of the entire valley, followed by a visit to the historic Shankaracharya Temple perched on a hilltop.'
                ),
                [
                    'Sightseeing Included: Shalimar Bagh, Nishat Bagh, Pari Mahal, Chashme Shahi, Shankaracharya Temple.',
                    'Optional Activities: A private guided tour of old heritage heritage stepways and ancient shrines.',
                    'Overnight Stay: Srinagar (Premium Luxury Resort / Five-Star Heritage Hotel)',
                    'Meals Included: Gourmet Breakfast & Fine Dining Dinner',
                ],
            ),
            _day(
                3,
                'SRINAGAR TO SONAMARG EXCURSION',
                (
                    "THE MEADOW OF GOLD & MAJESTIC THAJIWAS GLACIER Embark on a spectacular day trip to Sonamarg, aptly named the 'Meadow of Gold'. The scenic route traces the roaring Sindh River, flanked by towering alpine peaks and dense pine forests. Upon arrival, ride a local mountain pony up to the Thajiwas Glacier, where fields of pristine snow and ice sparkle beneath the mountain sun. Walk hand-in-hand along the quiet meadows and capture beautiful photographs at these popular Instagram locations. experts."
                ),
                [
                    'Sightseeing Included: Sindh River Valley, Sonamarg Meadows, Thajiwas Glacier Viewpoint.',
                    'Evening Experience: Riverside tea service with premium kashmiri bakery delicacies, organized by TRAGUIN',
                    'Overnight Stay: Srinagar (Premium Luxury Resort / Five-Star Heritage Hotel)',
                    'Meals Included: Premium Breakfast & Luxury Dinner',
                ],
            ),
            _day(
                4,
                'SRINAGAR TO GULMARG MEADOW OF FLOWERS',
                (
                    "HIGH-ALTITUDE GRANDEUR & WORLD-FAMOUS GONDOLA RIDE Travel towards Gulmarg, the spectacular 'Meadow of Flowers', widely known as a premier luxury destination. Check into your ultra-luxury resort and gaze out at the pristine snowscapes. Board the world’s highest cable car, the Gulmarg Gondola. Phase 1 takes you to Kungdoor Vineyard plains, and Phase 2 rises above 13,000 feet to Apharwat Peak, putting you right on top of the world. Touch the clouds, play in the powdery snow, and witness breathtaking landscapes that defy imagination."
                ),
                [
                    "Sightseeing Included: Gulmarg Golf Course, Gondola Ride (Both Phases), St. Mary's Historic Church.",
                    'Optional Activities: Private luxury snow-biking and expert-led alpine ski experiences.',
                    'Overnight Stay: Gulmarg (Premium Luxury Heated Resort / The Khyber or similar)',
                    'Meals Included: Premium Breakfast & Heated Luxury Buffer Dinner',
                ],
            ),
            _day(
                5,
                'GULMARG TO PAHALGAM THE VALLEY OF SHEPHERDS',
                (
                    "SAFFRON FIELDS, AVANTIPURA RUINS & ROARING RIVERS Drive towards Pahalgam, the charming 'Valley of Shepherds'. En route, pass through the historic town of Pampore to admire blooming saffron fields and explore the ancient Avantipura ruins. As you reach Pahalgam, the soothing sound of the Lidder River welcomes you. Check into an exceptional riverside luxury property. Spend the afternoon sitting on the grassy riverbanks, soaking in the pristine scenic beauty and mountain air."
                ),
                [
                    'Sightseeing Included: Pampore Saffron Fields, Avantipura Ruins, Lidder River Front.',
                    'Evening Experience: Private bonfire gathering under a star-filled sky at your luxury mountain lodge.',
                    'Overnight Stay: Pahalgam (Premium Five-Star Luxury Riverside Resort)',
                    'Meals Included: Premium Breakfast & Gourmet Chef-Curated Dinner',
                ],
            ),
            _day(
                6,
                'PAHALGAM VALLEY EXCURSION',
                (
                    'EXPLORING BETAAB VALLEY, ARU VALLEY & CHANDANWARI Board a local private vehicle to explore the hidden gems of Pahalgam. Visit Betaab Valley, named after the iconic Bollywood movie, featuring gorgeous pine forests and rolling meadows. Explore Chandanwari, the starting point of the holy Amarnath Yatra, and finish your excursion in the picturesque alpine village of Aru Valley. In the afternoon, return to town for high-end wood-carving shopping and cozy café hopping along the river market.'
                ),
                [
                    'Sightseeing Included: Betaab Valley, Aru Valley Alpine Meadows, Chandanwari Snow Point.',
                    'Optional Activities: Private riverside fly-fishing experience or horse-riding up to Baisaran Meadow.',
                    'Overnight Stay: Pahalgam (Premium Five-Star Luxury Riverside Resort)',
                    'Meals Included: Premium Breakfast & Farewell Celebration Dinner',
                ],
            ),
            _day(
                7,
                'PAHALGAM TO SRINAGAR / DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES OF PARADISE Enjoy a final morning breakfast as the sun lights up the Lidder River. Your private luxury transport vehicle will drive you back to Srinagar Airport for your departure flight. Return home carrying a heart filled with deep peace, romantic memories, and unforgettable moments designed meticulously by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private airport terminal drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Fortune Resort Heevan / similar | Hotel Royal Park / similar | Hotel Heevan Pahalgam / similar',
                'Srinagar | Gulmarg | Pahalgam',
                '3N Srinagar|1N Gulmarg|2N Pahalgam',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Fortune Resort Heevan / similar | Hotel Royal Park / similar | Hotel Heevan Pahalgam / similar | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Radisson Collection Silk Route | Grand Mumtaz Resort / similar | Welcomhotel by ITC Pine N Peak',
                'Srinagar | Gulmarg | Pahalgam',
                '3N Srinagar|1N Gulmarg|2N Pahalgam',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Collection Silk Route | Grand Mumtaz Resort / similar | Welcomhotel by ITC Pine N Peak | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Vivanta Dal View by Taj / Lalit | The Khyber Himalayan Resort | The Grand Mumtaz / Pahalgam Hotel',
                'Srinagar | Gulmarg | Pahalgam',
                '3N Srinagar|1N Gulmarg|2N Pahalgam',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Vivanta Dal View by Taj / Lalit | The Khyber Himalayan Resort | The Grand Mumtaz / Pahalgam Hotel | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Lalit Grand Palace (Royal Suite) | The Khyber (Luxury Chalet) | Bespoke Private Luxury Villa Stay',
                'Srinagar | Gulmarg | Pahalgam',
                '3N Srinagar|1N Gulmarg|2N Pahalgam',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Lalit Grand Palace (Royal Suite) | The Khyber (Luxury Chalet) | Bespoke Private Luxury Villa Stay | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury luxury accommodation as per selected matrix.', 1),
            _inc_included('Luxury Transportation: Chauffeur-driven executive SUV at your command.', 2),
            _inc_included('Curated Meal Plan: Lavish daily breakfast and dinners at all properties.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated local concierge assistance.', 4),
            _inc_included('Welcome Amenities: Customized luxury arrival package with Kashmiri walnuts.', 5),
            _inc_included('Complimentary Experience: 1-Hour private Shikara ride on Dal Lake.', 6),
            _inc_excluded('Domestic flights or train fares to Srinagar.', 7),
            _inc_excluded('Gondola cable car ride tickets (can be pre- booked).', 8),
            _inc_excluded('Pahalgam local green-vehicle union transport fee.', 9),
            _inc_excluded('Personal expenses, tips, and items not specified.', 10),
        ],
    )
    return package, itinerary

def build_jk_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JK-007'
    tour_code = 'TRG-KASH-007'
    title = 'Kashmir Great Lakes Trek — The Ultimate Alpine Expedition'
    duration = '08 Nights / 09 Days'
    slug = 'jk-007-kashmir-great-lakes-trek'
    itin_slug = 'jk-007-kashmir-great-lakes-trek-itinerary'
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
            _ph('Serial code JK-007 | TRAGUIN tour code TRG-KASH-007', 1),
            _ph('State / Country: Jammu & Kashmir / India | Category: Premium', 2),
            _ph('Destinations: Srinagar • Sonamarg • Nichnai • Vishansar • Gadsar • Satsar • Gangabal • Naranag', 3),
            _ph('Ideal for: Adventure Enthusiasts, Luxury Trekkers & Nature Photographers', 4),
            _ph('Best season: July to September (Alpine Bloom Season)', 5),
            _ph('Starting price: On Request (Premium Customised Expedition)', 6),
            _ph('Vehicle / Meals: Private Luxury SUV (Transfers) / All Meals on Trek', 7),
            _ph('TRAGUIN Signature Experience: Private pre-trek conditioning review and exclusive dinner onboard a', 8),
            _ph('Curated by TRAGUIN Experts: Custom trek pacing including a dedicated acclimatization timeline to', 9),
            _ph('Premium Handpicked Hotels: Transition properties chosen for fine dining, hot showers, and perfect city', 10),
            _ph('Luxury Transportation: Chauffeur-driven, private, luxury tourist vehicles for all highway stretches.', 11),
            _ph("Local Markets & Bazaars: Browse Srinagar's historic Lal Chowk or local craft houses for hand-knotted silk carpets, hand-carved walnut wood souvenirs, pure saffron, and premium Kashmiri almonds. Cafes & Food: Enjoy hot traditional Kahwa (saffron green tea with almonds) inside riverside tents, fresh oven- baked local breads (Girda) from traditional bakeries, and fusion dishes in Old Srinagar cafes.", 12),
            _ph('& TRAVEL INFORMATION', 13)
        ],
        moods=['Adventure', 'Nature', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised Expedition)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Kashmir Great Lakes Trek — The Ultimate Alpine Expedition',
        overview="KASHMIR GREAT LAKES TREK • THE ULTIMATE ALPINE EXPEDITION Welcome to an extraordinary high-altitude alpine expedition curated exclusively by TRAGUIN. Embark on the finest Kashmir Adventure Tour, custom-designed to reveal the breathtaking landscapes, virgin alpine meadows, and turquoise glacial lakes of this paradise on earth. As your trusted luxury travel consultants, TRAGUIN upgrades your raw outdoor exploration into a seamless, high-end premium adventure featuring luxury high-altitude camping, personal mountain guides, and handpicked hotels for your transit stays. From the quiet ripples of Dal Lake to the grand rugged passes and seven mystical high-altitude lakes, every day is designed to weave unforgettable memories.\n\nTOUR OVERVIEW\nThis elite trek itinerary offers a unparalleled blend of raw Himalayan wilderness and premium expedition hospitality. Travel from Srinagar in a dedicated private luxury transport vehicle to the base camp at Sonamarg. Throughout the trek, your journey features a high-end support crew, spacious weather-proof dome tents, gourmet alpine kitchens, and premium quality equipment. With an premium menu designed to sustain and indulge you in sub-zero temperatures, this route represents the definitive premium Kashmir experience. Every phase of your expedition includes the exclusive TRAGUIN curated experience note, providing unmatched safety, expert mountain leadership, and luxury touches in the wild.\n\nWHY VISIT KASHMIR FOR THE GREAT LAKES TREK?\nWhen elite travelers plan a Luxury Kashmir Holiday, they look for experiences that transcend traditional tourism. The Kashmir Great Lakes Trek is recognized globally as India's most beautiful high-altitude trek, making it the premier choice for a Kashmir Adventure Tour. Witnessing the top tourist places in Kashmir— from the wild rivers of Sonamarg to the pristine, untouched waters of Vishansar, Kishansar, and Gangabal lakes—offers a deep spiritual connection with nature. For active couples and thrill-seeking groups booking a tailored Kashmir Honeymoon Package or Kashmir Family Tour, the expedition unfolds spectacular, viral-worthy popular Instagram locations such as the silver birch forests of Nichnai, the wildflower fields of Gadsar, and the imposing peak of Mount Haramukh reflecting on twin glacial pools. From local dry fruit shopping in Srinagar's old bazaars to the serene luxury of a premium houseboat stay, our TRAGUIN Kashmir Packages guarantee premium stays, immersive experiences, and elite execution during the absolute best time to visit Kashmir.",
        seo_title='JK-007 | Kashmir Great Lakes Trek — The Ultimate Alpine Expedition | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days Kashmir package (JK-007 / TRG-KASH-007): Srinagar • Sonamarg • Nichnai • Vishansar • Gadsar • Satsar • Gangabal • Naranag with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SRINAGAR', 1),
            _ih('Day 02: SRINAGAR TO SONAMARG (BASE CAMP)', 2),
            _ih('Day 03: SONAMARG TO NICHNAI', 3),
            _ih('Day 04: NICHNAI TO VISHANSAR LAKE', 4),
            _ih('Day 05: VISHANSAR TO GADSAR LAKE VIA GADSAR PASS', 5),
            _ih('Day 06: GADSAR TO SATSAR LAKES', 6),
            _ih('Day 07: SATSAR TO GANGABAL TWIN LAKES', 7),
            _ih('Day 08: GANGABAL TO NARANAG TO SRINAGAR', 8),
            _ih('Day 09: SRINAGAR / DEPARTURE', 9),
            _ih('TRAGUIN Signature Experience: Private pre-trek conditioning review and exclusive dinner onboard a', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SRINAGAR',
                (
                    "WELCOME TO PARADISE – ROYAL HOUSEBOAT LUXURY & SHIKARA EXPERIENCE Your premium Kashmir experience begins the moment you touch down at Srinagar Airport. A private luxury transport vehicle awaits to sweep you away to an exclusive, handpicked premium luxury houseboat docked elegantly on Dal Lake. Enjoy a traditional welcome drink as you settle into your intricately carved wooden suite. In the late afternoon, enjoy an immersive Shikara ride through the floating gardens and hidden canals. Witness a cinematic sunset reflecting on the valley's mountains. houseboat."
                ),
                [
                    'Sightseeing Included: Dal Lake, Floating Gardens, Char Chinar viewpoint, Local Heritage Waterways.',
                    'Evening Experience: Traditional four-course Wazwan dinner curated by TRAGUIN experts onboard the',
                    'Overnight Stay: Srinagar (Premium Luxury Houseboat)',
                    'Meals Included: Welcome Amenities & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'SRINAGAR TO SONAMARG (BASE CAMP)',
                (
                    'DRIVE ALONG SINDH RIVER TO THE MEADOW OF GOLD After a grand breakfast, check out and enjoy a gorgeous drive to Sonamarg, your official trek base camp. The route follows the roaring Sindh River, passing through breathtaking landscapes of pine forests and terraced villages. Upon arrival at Shitkadi/Sonamarg, check into your high-end luxury alpine campsite. Spend the afternoon in a mandatory acclimatization walk through surrounding meadows and meet your expedition leader for an extensive pre-trek brief.'
                ),
                [
                    'Sightseeing Included: Sindh River Valley, Thajiwas Glacier viewpoints, Shitkadi Meadow.',
                    'Optional Activities: Private photography walk with a professional landscape mentor.',
                    'Overnight Stay: Sonamarg (Premium Luxury Glamping Tents)',
                    'Meals Included: Premium Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                3,
                'SONAMARG TO NICHNAI',
                (
                    'THE FIRST ASCENT – MEADOWS, SHEEPMEN TRAIL & SILVER BIRCH FORESTS The epic trek begins today. Wake up early for hot mountain tea and a nutrient-rich breakfast before packing your duffels onto the support horses. Hike uphill through golden meadows and dense birch forests, opening up to panoramic views of the Sonamarg valley. The trail descends gently to the Nichnai stream. Here, your luxury alpine camp is already set up by our advance team, complete with a hot soup welcome.'
                ),
                [
                    'Sightseeing Included: Nichnai Stream, Silver Birch Forests, Shakhdar Meadow Viewpoint.',
                    'Evening Experience: Stargazing session in the crisp, unpolluted air of the high Nichnai valley.',
                    'Overnight Stay: Nichnai Alpine Campsite (High-Altitude Premium Dome Tents)',
                    'Meals Included: All Fresh Mountain Meals (Breakfast, Packed Lunch, Hot Snacks, Dinner)',
                ],
            ),
            _day(
                4,
                'NICHNAI TO VISHANSAR LAKE',
                (
                    'CROSSING THE NICHNAI PASS TO THE LAKE OF LORD VISHNU A challenging and deeply rewarding day as you cross the high Nichnai Pass (13,100 ft). Take a slow, steady ascent enjoying the dramatic mountain views. Reach the top of the pass for views of the majestic valleys ahead. Descend into sprawling alpine grasslands carpeted with rare wildflowers. By afternoon, catch your first glimpse of Vishansar Lake, a vast turquoise glacial pool that changes colors through the day.'
                ),
                [
                    'Sightseeing Included: Nichnai Pass, Alpine Wildflower Meadows, Vishansar Glacial Lake.',
                    'Optional Activities: Catch-and-release fly fishing for endemic Himalayan Trout (subject to permit).',
                    'Overnight Stay: Vishansar Lake Base Camp (Premium All-Weather High-Altitude Tents)',
                    'Meals Included: All Fresh Mountain Meals (High-Protein Alpine Diet)',
                ],
            ),
            _day(
                5,
                'VISHANSAR TO GADSAR LAKE VIA GADSAR PASS',
                (
                    'CONQUERING THE HIGHEST PASS & TREKKING THROUGH THE VALLEY OF FLOWERS Prepare for an emotionally moving day of unmatched scenic beauty. Begin with a climb past Kishansar Lake before attacking the steep Gadsar Pass (13,750 ft), the highest point of your premium adventure. From the summit, view the twin lakes of Vishansar and Kishansar side by side. Descend past pristine snowfields into the Gadsar valley, arriving at the untouched, emerald waters of Gadsar Lake.'
                ),
                [
                    'Sightseeing Included: Kishansar Lake, Gadsar Pass Summit, Gadsar Glacial Lake, Snow Bridges.',
                    'Evening Experience: Warm gourmet dining experience inside our heated dining dome tent.',
                    'Overnight Stay: Gadsar Alpine Campsite (Premium High-Altitude Setup)',
                    'Meals Included: All Fresh Mountain Meals (Chef-Curated Expedition Menu)',
                ],
            ),
            _day(
                6,
                'GADSAR TO SATSAR LAKES',
                (
                    'TREKKING ACROSS THE ALPINO FLATS TO THE SEVEN CASCADING POOLS An easier but remarkably surreal day of trekking. Climb out of the Gadsar valley onto a wide alpine plateau known as the Maenigal Flats. Enjoy unobstructed views of the surrounding rugged peaks. Cross a series of gentle ridges to reach Satsar—a collection of seven interconnected alpine lakes nestled in a rocky mountain pocket. Spend the afternoon exploring the edges of these pristine pools.'
                ),
                [
                    'Sightseeing Included: Maenigal Alpine Flats, Satsar Interconnected Lakes, Boulder Field Trails.',
                    'Optional Activities: Portrait photography with local nomadic shepherds (Bakarwals).',
                    'Overnight Stay: Satsar Lake Campsite (Premium High-Altitude Tents)',
                    'Meals Included: All Fresh Mountain Meals',
                ],
            ),
            _day(
                7,
                'SATSAR TO GANGABAL TWIN LAKES',
                (
                    'THE ZAJ PASS RIDGE & THE ROYAL MAJESTY OF MOUNT HARAMUKH A dramatic day of trekking across boulder fields before ascending the Zaj Pass (13,400 ft). At the ridge, the view opens up to the twin lakes of Gangabal and Nandkol, sitting at the base of the massive Mount Haramukh. Descend through green meadows to camp beside Gangabal Lake, the largest and most sacred alpine lake of the entire expedition.'
                ),
                [
                    'Sightseeing Included: Zaj Pass Summit, Gangabal Lake, Nandkol Lake, Mount Haramukh Glacier view.',
                    'Evening Experience: Special campfire celebration dinner with live traditional music by local porters.',
                    'Overnight Stay: Gangabal Lake Meadows (Premium Lakesier Tents)',
                    'Meals Included: All Fresh Mountain Meals & Celebration Cake',
                ],
            ),
            _day(
                8,
                'GANGABAL TO NARANAG TO SRINAGAR',
                (
                    'THE FINAL DESCENT THROUGH MEADOWS & ANCIENT ARCHAEOLOGICAL RUINS Your final day of trekking takes you across rolling green ridges before a steep descent through thick pine forests into Naranag village. Visit the 8th-century Naranag Temple ruins, an ancient stone complex built by Lalitaditya. Here, your private luxury transport SUV waits to drive you smoothly back to Srinagar. Check into your premium hotel and enjoy a hot shower. Visit an exclusive Kashmiri handicraft cottage for authentic Pashmina shawls. Srinagar (Premium Luxury Hotel / Resort)'
                ),
                [
                    'Sightseeing Included: Naranag Ancient Temple Ruins, Pine Forest Trails, Srinagar Evening Boulevard walk.',
                    'Shopping: Point:',
                    'Meals Included: Breakfast, Packed Lunch & Farewell Premium Dinner',
                ],
            ),
            _day(
                9,
                'SRINAGAR / DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES OF THE KASHMIR ALPS Indulge in a final morning breakfast looking out over the misty Srinagar valley. Your private luxury transport will safely drive you back to Srinagar Airport for your flight home. Return with an enriched soul, enhanced fitness, and unforgettable memories designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door airport drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Premium Deluxe Houseboat / Hotel Rose Petal | Hotel Village Walk / similar | Standard Professional High-Altitude Camps',
                'Srinagar | Sonamarg | Alpine Trek',
                '2N Srinagar|1N Sonamarg|5N Trek',
                'Deluxe',
                'Deluxe Room | Standard Camp',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Premium Deluxe Houseboat / Hotel Rose Petal | Hotel Village Walk / similar | Standard Professional High-Altitude Camps | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Grand Kaisar / Lemon Tree Srinagar | Radisson Hotel Sonamarg | Premium Dome Camps with Elevated Foam Beds',
                'Srinagar | Sonamarg | Alpine Trek',
                '2N Srinagar|1N Sonamarg|5N Trek',
                'Premium',
                'Premium Room | Dome Camp',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Grand Kaisar / Lemon Tree Srinagar | Radisson Hotel Sonamarg | Premium Dome Camps with Elevated Foam Beds | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Vivanta Dal View by Taj / Fortune Hevan | Hotel Glacier Heights Luxury Suite | Luxury Camps with Cots, Pillow Sets & Heated Dini',
                'Srinagar | Sonamarg | Alpine Trek',
                '2N Srinagar|1N Sonamarg|5N Trek',
                'Luxury',
                'Luxury Suite | Heated Camp',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Vivanta Dal View by Taj / Fortune Hevan | Hotel Glacier Heights Luxury Suite | Luxury Camps with Cots, Pillow Sets & Heated Dining | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Lalit Grand Palace (Royal Suite) | The Khyber style luxury villa transit | VVIP Custom Camps with Private Toilet Tents & Per',
                'Srinagar | Sonamarg | Alpine Trek',
                '2N Srinagar|1N Sonamarg|5N Trek',
                'Ultra Luxury',
                'Royal Suite | VVIP Camp',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Lalit Grand Palace (Royal Suite) | The Khyber style luxury villa transit | VVIP Custom Camps with Private Toilet Tents & Personal Porter | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury Houseboat, Hotel, and high-altitude alpine dome camping.', 1),
            _inc_included('Luxury Transportation: Private SUV (Innova Crysta) for all city transfers.', 2),
            _inc_included('Gourmet Meal Plan: MAPAI in cities; all fresh high-protein hot mountain meals on trek.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated mountain concierge and satellite-linked safety support.', 4),
            _inc_included('Expedition Team: Certified Mountaineering Guides, Wilderness First-Responders, and Camp Chefs.', 5),
            _inc_included('Equipment Support: Premium sub-zero sleeping bags, insulated mats, oxygen cylinders.', 6),
            _inc_included('TRAGUIN Premium Luxury Itinerary — JK-007 6', 7),
            _inc_excluded('Domestic flights or train travel to/from Srinagar.', 8),
            _inc_excluded('Personal trekking gear (Boots, rucksacks, jackets).', 9),
            _inc_excluded('Insurance coverage, emergency evacuation or heli- rescue charges.', 10),
            _inc_excluded('Tips for mountain guides, porters, and camp staff.', 11),
        ],
    )
    return package, itinerary

def build_jk_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JK-008'
    tour_code = 'TRG-KSH-008'
    title = 'Kashmir Ladies Escape — Sisterhood Amidst Paradise'
    duration = '05 Nights / 06 Days'
    slug = 'jk-008-kashmir-ladies-escape'
    itin_slug = 'jk-008-kashmir-ladies-escape-itinerary'
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
            _ph('Serial code JK-008 | TRAGUIN tour code TRG-KSH-008', 1),
            _ph('State / Country: Jammu & Kashmir / India | Category: Female Only Group', 2),
            _ph('Destinations: Jharkhand', 3),
            _ph("Ideal for: Women Travelers, Girlfriends' Reunion & Solo Explorers", 4),
            _ph('Best season: April to October (Lush Meadows) / December to March (Snow)', 5),
            _ph('Starting price: On Request (Premium Curated Group / FIT)', 6),
            _ph('Vehicle / Meals: Luxury Tempo Traveller / Innova • MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private riverside evening musical bonfire circle organized exclusively', 8),
            _ph('Curated by TRAGUIN Experts: Pre-booked, skip-the-line ticketing parameters for key attractions to', 9),
            _ph('Premium Handpicked Hotels: Accommodations thoroughly audited for elite hospitality standards and', 10),
            _ph('Personalized Assistance: Background-verified local travel concierges who share rich stories of Kashmiri', 11),
            _ph('Local Markets & Souvenirs: Take time to buy world-class hand-knotted Silk Carpets, authentic Walnut Wood decorative boxes, premium Saffron threads from Pampore, and beautiful Paper Mache artwork from local boutiques. Cafes & Food: Old Srinagar features elegant, cozy tea rooms overlooking the river, where you can sample freshly baked local breads like Girda and Chochwor along with artisanal honey.', 12),
            _ph('& TRAVEL INFORMATION', 13)
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
        price_note='On Request (Premium Curated Group / FIT)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Kashmir Ladies Escape — Sisterhood Amidst Paradise',
        overview="KASHMIR LADIES ESCAPE • SISTERHOOD AMIDST PARADISE Welcome to a breathtaking heavenly retreat designed exclusively for women by TRAGUIN. Embark on the finest Kashmir Ladies Escape, an extraordinary Kashmir Family Tour & All-Women getaway created to showcase the jaw-dropping landscapes, mountain valleys, and royal hospitality of the valley. As your trusted premium travel consultants, TRAGUIN transforms this vacation into a highly secure, luxury holiday filled with premium stays, exquisite culinary journeys, and deep emotional storytelling. Let the scenic beauty of chinar trees, floating gardens, and snowy peaks form the perfect setting to forge bonds and build unforgettable memories together.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers the perfect balance of leisure, high-end security, shared camaraderie, and cultural depth across the top tourist places in Kashmir. Travelling in a dedicated, high-end private vehicle accompanied by a well-versed concierge, your safety and sheer comfort are our top priorities. Indulge in an exquisite meal plan that highlights authentic Kashmiri Wazwan, lavish hotel breakfasts, and evening high-teas by the stream. Every single detail includes the signature touch of TRAGUIN curated experiences, offering handpicked hotels, VIP shikara pathways, and localized expert assistance.\n\nWHY VISIT DESTINATION: THE PREMIUM KASHMIR EXPERIENCE\nWhen exploring choices for the Best Kashmir Tour Package, women travelers seek flawless hospitality, security, and true artistic immersion. Kashmir features iconic attractions that have captured the imagination of travelers for centuries. From the historic Mughal Gardens and peaceful waters of Dal Lake to the snow- covered alpine slopes of Gulmarg and the roaring pine valleys of Pahalgam, Kashmir sightseeing is an emotional journey in itself. For contemporary women's groups or those booking a bespoke Kashmir Honeymoon Package or Kashmir Family Tour, the valley provides endless popular Instagram locations. Capture stunning pictures wearing traditional Pherans in a floating saffron market, experience soul-soothing mountain walks, enjoy high-quality pashmina shawl shopping, or relax at a cozy cafe in Srinagar. Choosing our specialty TRAGUIN Kashmir Packages ensures you visit at the best time to visit Kashmir with access to curated exclusive experiences and luxury stays.",
        seo_title='JK-008 | Kashmir Ladies Escape — Sisterhood Amidst Paradise | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Kashmir package (JK-008 / TRG-KSH-008): Jharkhand with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SRINAGAR & DAL LAKE', 1),
            _ih('Day 02: SRINAGAR MUGHAL GARDENS EXPLORATION', 2),
            _ih('Day 03: SRINAGAR TO GULMARG EXCURSION', 3),
            _ih('Day 04: SRINAGAR TO PAHALGAM', 4),
            _ih('Day 05: PAHALGAM ALPINES & VALLEY EXCURSION', 5),
            _ih('Day 06: PAHALGAM TO SRINAGAR AIRPORT DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private riverside evening musical bonfire circle organized exclusively', 7),
            _ih('Curated by TRAGUIN Experts: Pre-booked, skip-the-line ticketing parameters for key attractions to', 8),
            _ih('Premium Handpicked Hotels: Accommodations thoroughly audited for elite hospitality standards and', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SRINAGAR & DAL LAKE',
                (
                    'WELCOME TO PARADISE – FLOATING LUXURY & EMOTIONAL STORYTELLING Your magical all-women adventure begins as you step out of Srinagar Airport, where a dedicated private luxury transport escort extends a warm traditional welcome. Transfer directly to the banks of the iconic Dal Lake and step into a beautifully carved premium luxury houseboat. After checking in, enjoy a fresh cup of traditional Kashmiri Kahwa. In the late afternoon, embark on an exclusive 2-hour sunset Shikara ride across the lake. Glide past floating gardens and local handicraft shops, documenting stunning photography points with your fellow travelers.'
                ),
                [
                    'Sightseeing Included: Dal Lake, Floating Markets, Nehru Park, Private Shikara Cruise.',
                    'Evening Experience: An elegant welcome high-tea reception followed by a gourmet dinner onboard.',
                    'Overnight Stay: Srinagar (Premium Handpicked Luxury Houseboat)',
                    'Meals Included: Welcome Kahwa Drink & Traditional Luxury Dinner',
                ],
            ),
            _day(
                2,
                'SRINAGAR MUGHAL GARDENS EXPLORATION',
                (
                    'ROYAL BOTANICAL MAJESTY & LOCAL EMBROIDERY ARTS Awake to a serene lakeside morning and a lavish breakfast. Spend your day discovering the classic architectural heritage and scenic beauty of the legendary Mughal Gardens. Walk through Nishat Bagh (Garden of Pleasure) and Shalimar Bagh (Abode of Love), built by Emperor Jahangir. Marvel at the cascading water fountains and century-old chinar trees. In the afternoon, visit an exclusive heritage handloom house to witness master craftsmen delicately weaving authentic Pashmina shawls and handcrafted Kashmiri carpets.'
                ),
                [
                    'Sightseeing Included: Nishat Bagh, Shalimar Bagh, Cheshma Shahi, Heritage Craft center.',
                    'Optional Activities: A group dress-up session in beautiful traditional Kashmiri Pherans for iconic group photos.',
                    'Overnight Stay: Srinagar (Premium Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Authentic Buffet Dinner',
                ],
            ),
            _day(
                3,
                'SRINAGAR TO GULMARG EXCURSION',
                (
                    'THE MEADOW OF FLOWERS & THE HIGHEST GONDOLA RIDE Following an early breakfast, enjoy a breathtakingly scenic mountain drive to Gulmarg, the crown alpine meadow of Kashmir. Gulmarg is world-famous for its sweeping golf courses and winter snow fields. Your group will skip the long queues with pre-booked tickets for the famous Gulmarg Gondola (Phase 1). Ride high above the pine-covered slopes up to Kungdoor station, enjoying stunning views of the surrounding peaks. Take time to relax at a high-altitude mountain café with your circle.'
                ),
                [
                    'Sightseeing Included: Gulmarg Meadows, Tangmarg Valley viewpoints, Gondola Phase 1.',
                    'Optional Activities: Gondola Phase 2 excursion up to Apharwat Peak for touchable snow experiences.',
                    'Overnight Stay: Srinagar or Gulmarg Premium Resort (Based on selection)',
                    'Meals Included: Premium Breakfast & Gourmet Dinner',
                ],
            ),
            _day(
                4,
                'SRINAGAR TO PAHALGAM',
                (
                    'THE VALLEY OF SHEPHERDS & SAFFRON MEADOWS Check out from your hotel and drive towards the beautiful valley of Pahalgam. En route, pass through the iconic Pampore Saffron Fields, where the air carries a light, floral fragrance. Stop at the ancient Awantipora Ruins to admire historical architecture and capture artistic group photos. Continue onwards as the road matches the curves of the turquoise Lidder River, arriving in Pahalgam by afternoon to check into an ultra- luxury riverside resort.'
                ),
                [
                    'Sightseeing Included: Pampore Saffron Fields, Lidder River Valley, Awantipora Temple Ruins.',
                    'Evening Experience: A beautiful riverside bonfire circle with music, custom-designed by TRAGUIN experts.',
                    'Overnight Stay: Pahalgam (Premium Luxury Riverside Resort)',
                    'Meals Included: Breakfast & Premium Riverside Dinner',
                ],
            ),
            _day(
                5,
                'PAHALGAM ALPINES & VALLEY EXCURSION',
                (
                    'PRISTINE VALLEYS, PINE FOREST TREKS & SISTERHOOD DINNER Today, explore the spectacular valleys surrounding Pahalgam in dedicated local vehicles. Discover Betaab Valley, named after a famous Bollywood movie and celebrated for its romantic meadows and crystal-clear streams. Visit Chandanwari, the historical starting point of the holy Amarnath Yatra, and Aru Valley, an alpine village surrounded by dense pine woods. In the evening, return to the resort to rest, relax, and share stories of your incredible journey.'
                ),
                [
                    'Sightseeing Included: Betaab Valley, Aru Valley alpine meadows, Chandanwari stream points.',
                    'Evening Experience: Special Ladies Farewell Dinner celebration featuring a multi-course Wazwan platter.',
                    'Overnight Stay: Pahalgam (Premium Luxury Riverside Resort)',
                    'Meals Included: Breakfast & Special Farewell Wazwan Dinner',
                ],
            ),
            _day(
                6,
                'PAHALGAM TO SRINAGAR AIRPORT DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS Enjoy a leisurely morning breakfast while taking in the pristine mountain views. Pack your bags and gather your lovely souvenirs. Your private luxury transport vehicle will drive you back to Srinagar Airport for your return flight. Head home carrying closer friendships, absolute rejuvenation, and unforgettable memories designed with love by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury highway drop-off directly to Srinagar Airport terminal.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Paradise / Fortune Heevan / similar | Hotel Heevan / Grand Mumtaz / similar',
                'Srinagar | Pahalgam',
                '3N Srinagar|2N Pahalgam',
                'Deluxe',
                'Deluxe Room with Heating',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Paradise / Fortune Heevan / similar | Hotel Heevan / Grand Mumtaz / similar | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Radisson Srinagar / Lemon Tree / similar | Pine n Peak / Welcomhotel / similar',
                'Srinagar | Pahalgam',
                '3N Srinagar|2N Pahalgam',
                'Premium',
                'Premium Balcony View Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Srinagar / Lemon Tree / similar | Pine n Peak / Welcomhotel / similar | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Grand Lalit / Vivanta Dal View by Taj | The Kolahoi Green Resort / similar suites',
                'Srinagar | Pahalgam',
                '3N Srinagar|2N Pahalgam',
                'Luxury',
                'Luxury Valley View Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Grand Lalit / Vivanta Dal View by Taj | The Kolahoi Green Resort / similar suites | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Grand Lalit (Palace Heritage Suite) | The Khyber Resort / Private Luxury Villas',
                'Srinagar | Pahalgam',
                '3N Srinagar|2N Pahalgam',
                'Ultra Luxury',
                'VVIP Heritage Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Grand Lalit (Palace Heritage Suite) | The Khyber Resort / Private Luxury Villas | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 05 Nights accommodation in selected high-end properties.', 1),
            _inc_included('Luxury Transportation: Chauffeur-driven private luxury AC transport vehicle.', 2),
            _inc_included('Meal Plan: Morning breakfast spreads and elegant dinners (MAPAI scheme).', 3),
            _inc_included('TRAGUIN Support: 24/7 priority emergency concierge for female groups.', 4),
            _inc_included('Welcome Amenities: Personalized travel kit, security brief, and fresh Kahwa.', 5),
            _inc_included('Complimentary Experiences: Private 2-Hour sunset Shikara cruise tickets.', 6),
            _inc_included('TRAGUIN Premium Luxury Itinerary — JK-008 5', 7),
            _inc_excluded('Airfare, domestic flights, or train access tickets to Srinagar.', 8),
            _inc_excluded('Local union taxi charges in Pahalgam/Gulmarg (if mandatory).', 9),
            _inc_excluded('Personal items, laundry, extra beverages, and gratitude tips.', 10),
            _inc_excluded('Phase 2 Gondola tickets or individual adventure equipment rentals.', 11),
        ],
    )
    return package, itinerary

def build_jk_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JK-009'
    tour_code = 'TRG-KASH-009'
    title = 'Leisure Kashmir — Serenade of Paradise'
    duration = '05 Nights / 06 Days'
    slug = 'jk-009-leisure-kashmir-serenade'
    itin_slug = 'jk-009-leisure-kashmir-serenade-itinerary'
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
            _ph('Serial code JK-009 | TRAGUIN tour code TRG-KASH-009', 1),
            _ph('State / Country: Jammu & Kashmir / India | Category: Senior Citizen', 2),
            _ph('Destinations: Srinagar • Gulmarg • Pahalgam • Dal Lake', 3),
            _ph('Ideal for: Senior Citizens, Families & Leisure Travelers', 4),
            _ph('Best season: April to October (Pleasant Meadows)', 5),
            _ph('Starting price: On Request (Bespoke Luxury Standard)', 6),
            _ph('Vehicle / Meals: Luxury Innova Crysta / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Priority fast-track Gondola ticket arrangement to skip long passenger', 8),
            _ph('Curated by TRAGUIN Experts: Custom-paced itinerary with later morning starts, tailored for a relaxed,', 9),
            _ph('Personalized Assistance: Dedicated on-ground local support available at all major tourist hubs for', 10),
            _ph('Premium Handpicked Hotels: Accommodations chosen specifically for their excellent accessibility,', 11),
            _ph('Local Markets & Souvenirs: Shop for fine, authentic Pashmina shawls, pure organic saffron from Pampore, walnut wood carvings, and world-class papier-mâché artifacts at Lal Chowk or the government handicraft emporiums. Cafes & Food: Savor a traditional multicourse Wazwan meal, sip steaming hot salt tea (Noon Chai) at a local bakery, or enjoy global cuisines at cozy wood-furnished cafes overlooking the Lidder River.', 12),
            _ph('& TRAVEL INFORMATION', 13)
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
        price_note='On Request (Bespoke Luxury Standard)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Leisure Kashmir — Serenade of Paradise',
        overview="LEISURE KASHMIR • SERENADE OF PARADISE Welcome to a timeless paradise crafted with utmost care, leisure, and sophistication by TRAGUIN. Embark on a spectacular Kashmir Senior Citizen Tour uniquely designed to reveal the breathtaking landscapes, calm reflecting waters, and snow-kissed alpine valleys of heaven on earth. As your trusted luxury travel experts, TRAGUIN transforms this journey into an effortlessly relaxed luxury holiday. Featuring highly accessible routes, premium stays with top-tier hospitality, and immersive experiences, we focus heavily on absolute comfort, slow-paced exploration, and deep emotional storytelling to ensure you return with unforgettable memories.\n\nTOUR OVERVIEW\nThis bespoke leisure tour offers the ultimate, non-tiring Premium Kashmir Experience carefully optimized for mature travelers. Travelling in a dedicated private luxury transport vehicle with a courteous, background- verified chauffeur, you are assured of safe, seamless transits across the valley. With an elite meal plan comprising fresh, nourishing breakfasts and elaborate dinners at handpicked hotels, the route captures the absolute essence of paradise without any rushed timetables. Every destination highlights a specialized TRAGUIN curated experience note, encompassing wheel-chair assistance where required, priority check-ins, and smooth ground support.\n\nWHY CHOOSE THE BEST KASHMIR TOUR PACKAGE?\nWhen exploring options for a Luxury Kashmir Holiday, discerning travelers look for magnificent scenery coupled with a gentle pace of travel. Kashmir features some of the world's most iconic attractions. From the iconic Mughal Gardens of Srinagar to the rolling golden meadows of Gulmarg and the tranquil streams of Pahalgam, Kashmir sightseeing is deeply poetic. For travelers seeking a relaxed Kashmir Family Tour or an intimate Kashmir Honeymoon Package, the region offers countless popular Instagram locations such as the vibrant floating flower markets, historical wooden houseboats, and majestic chinar groves. Whether it is enjoying local saffron Kehwa, shopping for world-renowned hand-knotted carpets, or exploring top tourist places in Kashmir with minimal walking, our customized TRAGUIN Kashmir Packages provide premium comfort and exclusive experiences during the best time to visit Kashmir.",
        seo_title='JK-009 | Leisure Kashmir — Serenade of Paradise | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Kashmir package (JK-009 / TRG-KASH-009): Srinagar • Gulmarg • Pahalgam • Dal Lake with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SRINAGAR & SHIKARA CRUISE', 1),
            _ih('Day 02: SRINAGAR MUGHAL GARDENS SIGHTSEEING', 2),
            _ih('Day 03: SRINAGAR TO GULMARG EXCURSION', 3),
            _ih('Day 04: GULMARG TO PAHALGAM', 4),
            _ih('Day 05: LEISURE IN PAHALGAM (AURA VALLEY)', 5),
            _ih('Day 06: PAHALGAM TO SRINAGAR DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Priority fast-track Gondola ticket arrangement to skip long passenger', 7),
            _ih('Curated by TRAGUIN Experts: Custom-paced itinerary with later morning starts, tailored for a relaxed,', 8),
            _ih('Personalized Assistance: Dedicated on-ground local support available at all major tourist hubs for', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SRINAGAR & SHIKARA CRUISE',
                (
                    'WELCOME TO PARADISE – FLOATING LUXURY ON THE DAL LAKE Your wonderful journey begins as you step out of Srinagar Airport, where your specialized private luxury transport vehicle and representative welcome you with fresh marigold garlands. Transfer smoothly to your luxury houseboat or premium lakeside resort. After an easy lunch and ample rest, indulge in a therapeutic, slow-paced 1-hour Shikara ride across the glassy waters of Dal Lake. Witness the scenic beauty of the Zabarwan mountains reflecting perfectly on the water.'
                ),
                [
                    'Sightseeing Included: Dal Lake cruise, floating handicraft gardens, historic water lanes.',
                    'Evening Experience: Freshly brewed traditional saffron Kehwa greeting on the deck at sunset.',
                    'Overnight Stay: Srinagar (Premium Luxury Houseboat / Handpicked Hotel)',
                    'Meals Included: Welcome Drink & Gourmet Dinner',
                ],
            ),
            _day(
                2,
                'SRINAGAR MUGHAL GARDENS SIGHTSEEING',
                (
                    "ROYAL ARCHITECTURE & TIMELESS CHINAR GROVES Savor a delightful breakfast before enjoying a highly relaxed Srinagar sightseeing tour. Explore the beautifully manicured terraced lawns of Shalimar Bagh ('Abode of Love') and Nishat Bagh ('Garden of Pleasure'), built by the Mughal Emperors. These historic sites feature gentle walkways, elegant stone fountains, and old chinar trees. Later, visit the serene Chasme Shahi spring, renowned for its sweet medicinal water, ensuring a peaceful, comfortable day out."
                ),
                [
                    'Sightseeing Included: Nishat Bagh, Shalimar Bagh, Cheshma Shahi, Pari Mahal vistas.',
                    'Optional Activities: Traditional Kashmiri Pheran attire photography session inside the royal gardens.',
                    'Overnight Stay: Srinagar (Premium Lakeside Resort)',
                    'Meals Included: Premium Breakfast & Authentic Multi-course Dinner',
                ],
            ),
            _day(
                3,
                'SRINAGAR TO GULMARG EXCURSION',
                (
                    'THE MEADOW OF FLOWERS – MAJESTIC ALPINE GLORY Drive along a highly scenic route lined with tall pine trees towards Gulmarg. Sprawled at an altitude of 2,730 meters, this vast green meadow offers breathtaking landscapes that soothe the soul. For our senior travelers, a smooth ride on the famous Gulmarg Gondola (Phase 1) is pre-arranged, taking you seamlessly up into the clouds to view pristine snowscapes without any steep trekking or physical strain.'
                ),
                [
                    "Sightseeing Included: Gulmarg Meadow, Gondola Cable Car Ride (Phase 1), St. Mary's Church plains.",
                    'Evening Experience: Relaxed high-tea session overlooking the highest golf course in the world.',
                    'Overnight Stay: Gulmarg (Luxury Centrally-Heated Mountain Resort)',
                    'Meals Included: Premium Breakfast & Warm Luxury Dinner',
                ],
            ),
            _day(
                4,
                'GULMARG TO PAHALGAM',
                (
                    'THE VALLEY OF SHEPHERDS – RIVERSIDE SERENITY Embark on an easy morning drive through cascading hills toward Pahalgam. En route, pass through the famous saffron fields of Pampore and stop to witness ancient ruins. Arrive in Pahalgam, where the stunning Lidder River flows gracefully through steep pine forests. Check into your luxury valley resort and spend the afternoon unwinding in lush, green manicured lawns while listening to the calming sounds of the mountain river.'
                ),
                [
                    'Sightseeing Included: Pampore Saffron Farms view, Lidder River trail, Apple Orchards walk.',
                    'Evening Experience: Private riverside bonfire and musical acoustic evening arranged at the resort.',
                    'Overnight Stay: Pahalgam (Premium River-Facing Luxury Stay)',
                    'Meals Included: Premium Breakfast & Elegant Riverside Dinner',
                ],
            ),
            _day(
                5,
                'LEISURE IN PAHALGAM (AURA VALLEY)',
                (
                    'EXPLORING PICTURESQUE MEADOWS & PRISTINE VALLEYS Enjoy a relaxed morning breakfast. Board local eco-friendly union vehicles for a comfortable drive to Betaab Valley, named after the Bollywood classic, and Aru Valley. These locations offer magnificent, easily accessible flat walking trails with outstanding photography points. Sit comfortably on wooden benches, admire the cascading waterfalls, and soak in the fresh mountain air.'
                ),
                [
                    'Sightseeing Included: Betaab Valley meadows, Aru Valley ecosystems, Chandanwari vistas.',
                    'Optional Activities: Gentle, assisted pony rides through the flat pine forests.',
                    'Overnight Stay: Pahalgam (Premium River-Facing Luxury Stay)',
                    'Meals Included: Premium Breakfast & Special Farewell Dinner',
                ],
            ),
            _day(
                6,
                'PAHALGAM TO SRINAGAR DEPARTURE',
                (
                    'CHERISHING THE MEMORIES OF HEAVEN ON EARTH Indulge in a final hearty breakfast amidst the mountains. Your private luxury transport will safely drive you back to Srinagar Airport. As you board your flight home, return with refreshed spirits, deep rejuvenation, and unforgettable memories carefully designed by the experts at TRAGUIN.'
                ),
                [
                    'Transfers Included: Direct highway luxury drop-off to airport terminals.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Grand Mumtaz / Deluxe Houseboat | Hotel Royal Park / similar | Grand Mumtaz Resort / similar',
                'Srinagar | Gulmarg | Pahalgam',
                '2N Srinagar|1N Gulmarg|2N Pahalgam',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Grand Mumtaz / Deluxe Houseboat | Hotel Royal Park / similar | Grand Mumtaz Resort / similar | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Fortune Resort Heevan / similar | Hotel Vintage / similar | Heevan Resort / Hotel Pine N Peak',
                'Srinagar | Gulmarg | Pahalgam',
                '2N Srinagar|1N Gulmarg|2N Pahalgam',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Fortune Resort Heevan / similar | Hotel Vintage / similar | Heevan Resort / Hotel Pine N Peak | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Orchid Retreat / Vivanta Dal View | The Khyber Himalayan Resort (Luxury Room) | Welcomhotel Pine N Peak (Superior Suite)',
                'Srinagar | Gulmarg | Pahalgam',
                '2N Srinagar|1N Gulmarg|2N Pahalgam',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Orchid Retreat / Vivanta Dal View | The Khyber Himalayan Resort (Luxury Room) | Welcomhotel Pine N Peak (Superior Suite) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Lalit Grand Palace (Heritage Palace Suite) | The Khyber Himalayan Resort (Presidential) | The Grand Mumtaz Resorts Premium C',
                'Srinagar | Gulmarg | Pahalgam',
                '2N Srinagar|1N Gulmarg|2N Pahalgam',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Lalit Grand Palace (Heritage Palace Suite) | The Khyber Himalayan Resort (Presidential) | The Grand Mumtaz Resorts Premium Chalet | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury accommodations with central heating options.', 1),
            _inc_included('Luxury Transportation: Private Innova Crysta with an experienced valley driver.', 2),
            _inc_included('Curated Meal Plan: Lavish daily breakfasts and fine dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 priority ground handling and senior guest assistance.', 4),
            _inc_included('Welcome Amenities: Kashmiri herbal immunity drinks and custom travel cushions.', 5),
            _inc_included('Complimentary Experience: 1-Hour pre-paid private Shikara cruise on Dal Lake.', 6),
            _inc_excluded('Airfare or train tickets to and from Srinagar Airport.', 7),
            _inc_excluded('Internal union taxi services for Rohtang/Aru if modified.', 8),
            _inc_excluded('Personal expenses such as laundry, phone calls, or tips.', 9),
            _inc_excluded('Medical insurance or personal expenses during travel.', 10),
        ],
    )
    return package, itinerary

def build_jk_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JK-010'
    tour_code = 'TRG-KASH-010'
    title = 'Kashmir Complete — Paradise on Earth Rediscovered'
    duration = '07 Nights / 08 Days'
    slug = 'jk-010-kashmir-complete'
    itin_slug = 'jk-010-kashmir-complete-itinerary'
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
            _ph('Serial code JK-010 | TRAGUIN tour code TRG-KASH-010', 1),
            _ph('State / Country: Jammu & Kashmir / India | Category: Premium Family', 2),
            _ph('Destinations: Srinagar • Gulmarg • Pahalgam • Sonamarg • Dal Lake', 3),
            _ph('Ideal for: Family Vacations, Luxury Explorers & Couples', 4),
            _ph('Best season: April to October (Lush Greens) / December to March (Snow)', 5),
            _ph('Starting price: On Request (Premium Customised Offering)', 6),
            _ph('Vehicle / Meals: Private Luxury Innova Crysta / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private family interaction and historical storytelling briefing before', 8),
            _ph('Curated by TRAGUIN Experts: Seamless coordination for local valley transitions in Pahalgam with zero', 9),
            _ph('Premium Handpicked Hotels: Accommodations evaluated stringently for safety, hospitality, and', 10),
            _ph('Luxury Transportation: Chauffeurs extensively trained in navigating high-altitude mountain terrain with', 11),
            _ph('Local Markets & Souvenirs: Explore Lal Chowk and the local floating lake markets to find authentic, hand- knotted Pashmina shawls, organic saffron, walnut wood carvings, and exquisite hand-painted papier-mâché crafts. Cafes & Food: Indulge in an authentic multi-course Wazwan dinner, sample freshly baked traditional breads at local bakeries, and enjoy specialty coffees at upscale cafes overlooking the Lidder River in Pahalgam.', 12),
            _ph('& TRAVEL INFORMATION', 13)
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
        price_note='On Request (Premium Customised Offering)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Kashmir Complete — Paradise on Earth Rediscovered',
        overview='KASHMIR COMPLETE • PARADISE ON EARTH REDISCOVERED Welcome to an unforgettable journey into paradise, beautifully curated by TRAGUIN. Embark on the finest Kashmir Family Tour designed to reveal the breathtaking landscapes, majestic snow peaks, and timeless hospitality of the valley. As your premier travel consultants, TRAGUIN transforms your vacation into a seamless luxury holiday filled with handpicked hotels, intimate shikara experiences, and deeply touching cultural stories. From the floating fields of Dal Lake to the alpine meadows of Gulmarg, the pine-bordered rivers of Pahalgam, and the dramatic glaciers of Sonamarg, every moment is crafted to generate unforgettable memories.\n\nTOUR OVERVIEW\nThis custom-crafted Premium Kashmir Experience offers an exquisite balance between natural wonders, adventure excursions, cultural immersion, and absolute comfort. Travelling in a dedicated private luxury transport vehicle with a professional chauffeur-driven assistant, your family will experience flawless connectivity and total privacy. With a comprehensive meal plan featuring gourmet daily breakfasts and curated signature multi-course dinners, this itinerary represents the absolute pinnacle of luxury travel. Every aspect includes the definitive TRAGUIN curated experience note, ensuring priority VIP permissions, seamless houseboat transitions, and around-the-clock bespoke support.\n\nWHY CHOOSE THE BEST KASHMIR TOUR PACKAGE?\nWhen exploring a Luxury Kashmir Holiday, families and couples look for a harmonious combination of sweeping alpine beauty, traditional heritage, and elite comfort. Kashmir is adorned with some of the most iconic attractions in the world. From the world-famous Gondola cable car ride in Gulmarg—a top tourist place in Kashmir for winter sports and panoramic vistas—to the therapeutic betaab valley and Aru Valley paths in Pahalgam, Kashmir sightseeing is deeply mesmerizing. For couples finalizing an intimate Kashmir Honeymoon Package or families scheduling an expansive Kashmir Family Tour, the valley offers highly sought-after popular Instagram locations like the floating vegetable markets, the fields of saffron in Pampore, and the symmetric terraced geometry of Mughal Gardens. Whether your focus is shopping for premium pashminas, tasting authentic multi-course Kashmiri Wazwan, or simply resting under ancient chinar trees, our TRAGUIN Kashmir Packages provide exceptional handpicked hotels, premium stays, and exclusive experiences during the absolute best time to visit Kashmir.',
        seo_title='JK-010 | Kashmir Complete — Paradise on Earth Rediscovered | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Kashmir package (JK-010 / TRG-KASH-010): Srinagar • Gulmarg • Pahalgam • Sonamarg • Dal Lake with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SRINAGAR & DAL LAKE HOUSEBOAT', 1),
            _ih('Day 02: SRINAGAR MUGHAL GARDENS SIGHTSEEING', 2),
            _ih('Day 03: SRINAGAR TO SONAMARG EXCURSION', 3),
            _ih('Day 04: SRINAGAR TO PAHALGAM VIA PAMPORE', 4),
            _ih('Day 05: PAHALGAM VALLEY EXPLORATION', 5),
            _ih('Day 06: PAHALGAM TO GULMARG', 6),
            _ih('Day 07: HIGHEST GONDOLA CABLE CAR EXPERIENCE', 7),
            _ih('Day 08: GULMARG TO SRINAGAR / DEPARTURE', 8),
            _ih('TRAGUIN Signature Experience: Private family interaction and historical storytelling briefing before', 9),
            _ih('Curated by TRAGUIN Experts: Seamless coordination for local valley transitions in Pahalgam with zero', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SRINAGAR & DAL LAKE HOUSEBOAT',
                (
                    'WELCOME TO PARADISE – FLOATING LUXURY & THE MAGIC SHIKARA Your premium Kashmir experience begins as you touch down at Srinagar International Airport, where a dedicated private luxury transport vehicle waits to escort you. Transfer smoothly to the banks of the legendary Dal Lake and step aboard an ultra-luxury, hand-carved cedarwood Houseboat. After a refreshing afternoon, indulge in a classic 1-hour Shikara boat ride across the tranquil waters, passing floating gardens, vibrant local water-bazaars, and breathtaking landscapes as the golden sun sets behind the Zabarwan range.'
                ),
                [
                    'Sightseeing Included: Dal Lake, Floating Markets, Historic Waterways, Sunset Views.',
                    'Evening Experience: Traditional Kahwa welcome drink followed by a curated candlelit dinner onboard.',
                    'Overnight Stay: Srinagar (Premium / Luxury Houseboat on Dal Lake)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'SRINAGAR MUGHAL GARDENS SIGHTSEEING',
                (
                    "ROYAL ARCHITECTURE, SYMMETRY & SENSE OF HISTORY Awake to the peaceful call of nature on the lake. Following a lavish breakfast, proceed for an extensive tour of Srinagar's iconic attractions. Discover the majestic Mughal Gardens, including Nishat Bagh (The Garden of Pleasure) and Shalimar Bagh (Abode of Love), built by Emperor Jehangir for his beloved wife. Later, ascend the hill to the ancient Shankaracharya Temple to enjoy a spectacular, panoramic bird's-eye view of the entire Srinagar cityscape and the winding Beas-fed canals."
                ),
                [
                    'Sightseeing Included: Nishat Bagh, Shalimar Bagh, Chashme Shahi, Shankaracharya Temple, Hazratbal Shrine.',
                    'Optional Activities: Traditional Kashmiri Pheran attire dress-up photography session within the royal gardens.',
                    'Overnight Stay: Srinagar (Premium / Luxury Boutique Hotel)',
                    'Meals Included: Premium Breakfast & Luxury Dinner',
                ],
            ),
            _day(
                3,
                'SRINAGAR TO SONAMARG EXCURSION',
                (
                    "THE MEADOW OF GOLD & ALPINES OF THAJIWAS GLACIER Embark on a magnificent day excursion to Sonamarg, beautifully named the 'Meadow of Gold'. The scenic route snakes alongside the sparkling Sindh River, offering breathtaking landscapes of steep pine-forested mountains. Upon arrival, immerse yourself in the awe-inspiring alpine scenery. You can ride local ponies up to the spectacular Thajiwas Glacier, where snow remains intact throughout the year, making it a dream destination for photography points and unforgettable memories."
                ),
                [
                    'Sightseeing Included: Sonamarg Meadows, Sindh River Valley, Thajiwas Glacier viewpoints.',
                    'Evening Experience: Private tea session served on the green riverside meadows before returning to Srinagar.',
                    'Overnight Stay: Srinagar (Premium / Luxury Boutique Hotel)',
                    'Meals Included: Premium Breakfast & Multi-cuisine Dinner',
                ],
            ),
            _day(
                4,
                'SRINAGAR TO PAHALGAM VIA PAMPORE',
                (
                    "THE VALLEY OF SHEPHERDS – SAFFRON FIELDS & RIVERSIDE BLISS Depart today for Pahalgam, the celebrated 'Valley of Shepherds'. En route, cruise past the endless lavender and saffron fields of Pampore, pausing to purchase authentic Kashmiri saffron and almonds. Drive past the historic ruins of Avantipur temples. As you approach Pahalgam, the dramatic roar of the Lidder River will welcome your family. Check into your ultra-luxury riverside resort and unwind amidst the soothing pine breeze."
                ),
                [
                    'Sightseeing Included: Pampore Saffron Fields, Avantipur Ruins, Lidder River Valley.',
                    'Evening Experience: A beautiful nature walk through pine forests along the flowing banks of the Lidder River.',
                    'Overnight Stay: Pahalgam (Premium Riverside Luxury Resort)',
                    'Meals Included: Breakfast & Exquisite Buffet Dinner',
                ],
            ),
            _day(
                5,
                'PAHALGAM VALLEY EXPLORATION',
                (
                    'BETAAB VALLEY, ARU VALLEY & CHANDANWARI MYSTIQUE Indulge in a glorious morning overlooking the misty valley. Board your designated local eco-transport vehicle for an immersive experience inside the iconic valleys of Pahalgam. Explore Betaab Valley, named after the famous Bollywood movie, surrounded by snow peaks and crystal streams. Venture into Chandanwari, the historical starting point of the holy Amarnath Yatra, and Aru Valley, an alpine meadow offering unparalleled scenic beauty. Switzerland).'
                ),
                [
                    'Sightseeing Included: Betaab Valley, Aru Valley, Chandanwari, Film-shooting spots.',
                    'Optional Activities: White-water rafting on the Lidder River or horse riding to Baisaran Meadow (Mini',
                    'Overnight Stay: Pahalgam (Premium Riverside Luxury Resort)',
                    'Meals Included: Breakfast & Special Kashmiri Infused Dinner',
                ],
            ),
            _day(
                6,
                'PAHALGAM TO GULMARG',
                (
                    "THE MEADOW OF FLOWERS – MAJESTIC HIGHLANDS & SNOWY PEAKS Following a rich breakfast, your luxury vehicle charts a scenic path towards Gulmarg, the famed 'Meadow of Flowers'. Ascending to an altitude of 2,730 meters, watch the landscape shift into vast expanses of green golf courses and dense pine woods. Gulmarg stands as a pinnacle location in any Luxury Kashmir Holiday. Check into your mountain chalet resort, featuring heated interior parameters and breathtaking views of the majestic Apharwat mountain peak."
                ),
                [
                    'Sightseeing Included: Gulmarg Golf Course, Outer Circle Walk, St. Mary’s Heritage Church.',
                    'Evening Experience: Hot cocoa service near the traditional Bukhari fireplace inside the resort.',
                    'Overnight Stay: Gulmarg (Premium Mountain Luxury Chalet)',
                    'Meals Included: Breakfast & Premium Buffet Dinner',
                ],
            ),
            _day(
                7,
                'HIGHEST GONDOLA CABLE CAR EXPERIENCE',
                (
                    'TOUCHING THE SKY AT KONGDOORI & APHARWAT PEAKS Today highlights an extraordinary, high-altitude curated experience. Board the iconic Gulmarg Gondola, one of the highest cable cars in the world. Ascend through Phase 1 (Kongdoori) up to Phase 2 (Apharwat Peak) at a staggering height of 4,200 meters. Stand amidst absolute alpine purity, touching the clouds and looking over the mighty Karakoram range. It is a highly acclaimed popular Instagram location, ideal for capturing unforgettable family moments.'
                ),
                [
                    'Sightseeing Included: Gondola Cable Car Ride (Both Phases), Apharwat Snowfields.',
                    'Optional Activities: Snow skiing, snowmobiling across high ridges, or professional mountain portraiture.',
                    'Overnight Stay: Gulmarg (Premium Mountain Luxury Chalet)',
                    'Meals Included: Breakfast & Farewell Premium Gala Dinner',
                ],
            ),
            _day(
                8,
                'GULMARG TO SRINAGAR / DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS Indulge in a final, opulent breakfast at your premium chalet. Bid farewell to the snow peaks as your private luxury transport drives you safely down the mountain highway to Srinagar International Airport for your onward journey home. Return with your heart overflowing with deep family bonds and unforgettable memories meticulously structured by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury highway airport transfer drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Royal Milestone / Deluxe Houseboat | Hotel Pine Spring / similar | Hotel Foothills / similar',
                'Srinagar | Gulmarg | Pahalgam',
                '3N Srinagar|2N Pahalgam|2N Gulmarg',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Royal Milestone / Deluxe Houseboat | Hotel Pine Spring / similar | Hotel Foothills / similar | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Fortune Resort Heevan / Premium Houseboat | The Vintage Gulmarg / similar | Hotel Heevan / Pine N Peak',
                'Srinagar | Gulmarg | Pahalgam',
                '3N Srinagar|2N Pahalgam|2N Gulmarg',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Fortune Resort Heevan / Premium Houseboat | The Vintage Gulmarg / similar | Hotel Heevan / Pine N Peak | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Vivanta Dal View Srinagar / The Lalit Grand | The Khyber Himalayan Resort & Spa | Welcomhotel Pine N Peak (Grand Suite)',
                'Srinagar | Gulmarg | Pahalgam',
                '3N Srinagar|2N Pahalgam|2N Gulmarg',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Vivanta Dal View Srinagar / The Lalit Grand | The Khyber Himalayan Resort & Spa | Welcomhotel Pine N Peak (Grand Suite) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Lalit Grand Palace (Royal Suite Stay) | The Khyber Resort (Luxury Private Chalet) | Pahalgam Hotel (VVIP Premium Bungalow)',
                'Srinagar | Gulmarg | Pahalgam',
                '3N Srinagar|2N Pahalgam|2N Gulmarg',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Lalit Grand Palace (Royal Suite Stay) | The Khyber Resort (Luxury Private Chalet) | Pahalgam Hotel (VVIP Premium Bungalow) | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 07 Nights in chosen premium properties & luxury houseboat.', 1),
            _inc_included('Luxury Transportation: Private dedicated AC Innova Crysta throughout the journey.', 2),
            _inc_included('Curated Meal Plan: Daily elaborate breakfast spreads and gourmet dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated local guest relationship manager on call.', 4),
            _inc_included('Welcome Amenities: Personalized traditional Kahwa tasting on arrival & family travel kit.', 5),
            _inc_included('Complimentary Experience: 1-Hour private royal Shikara ride on Dal Lake.', 6),
            _inc_excluded('Airfare, flight tickets, or airport taxes.', 7),
            _inc_excluded('Gulmarg Gondola ride tickets (can be pre-booked on request).', 8),
            _inc_excluded('Pony ride charges in Sonamarg, Gulmarg, or Pahalgam.', 9),
            _inc_excluded('Personal expenses such as laundry, phone calls, or tips.', 10),
        ],
    )
    return package, itinerary

KASHMIR_JK_001_010_BUILDERS = [
    build_jk_001,
    build_jk_002,
    build_jk_003,
    build_jk_004,
    build_jk_005,
    build_jk_006,
    build_jk_007,
    build_jk_008,
    build_jk_009,
    build_jk_010,
]
