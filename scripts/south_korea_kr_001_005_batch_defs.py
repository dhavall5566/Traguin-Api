"""Builder functions for KR-001, KR-002, KR-003, and KR-005 South Korea international packages."""

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

SOUTH_KOREA_SLUG = "south-korea"


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


def build_kr_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KR-001'
    tour_code = 'TRG-SEO-FAM-2026'
    title = 'Seoul Highlights Family Tour'
    duration = '05 Nights / 06 Days'
    slug = 'kr-001-seoul-highlights-family-tour'
    itin_slug = 'kr-001-seoul-highlights-itinerary'
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
            _ph('Serial code KR-001 | TRAGUIN tour code TRG-SEO-FAM-2026', 1),
            _ph('Country: South Korea, Asia | Category: Premium Seoul Family Tour Package', 2),
            _ph('Destinations: Gyeongbokgung Palace • N Seoul Tower • Myeongdong Shopping • Lotte World', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Executive Sedan / Buffet Breakfast & Curated Dinners', 7)
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
        price_note='On Request (Premium South Korea Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Seoul Highlights Family Tour',
        overview='Gyeongbokgung Palace • N Seoul Tower • Myeongdong Shopping • Lotte World Adventure 05 Nights / 06 Days Classic Seoul Family Expedition SERIAL CODE: KR-001 TRAGUIN TOUR CODE: TRG-SEO-FAM-2026 STATE / COUNTRY: South Korea CATEGORY: Premium Seoul Family Tour Package DURATION: 05 Nights / 06 Days Seoul Highlights\n\nTOUR OVERVIEW\nDiscover the vibrant capital of South Korea with our TRAGUIN curated family expedition. From the historic Gyeongbokgung Palace and iconic N Seoul Tower to the high-energy entertainment of Lotte World and the shopping delights of Myeongdong, this journey ensures your family creates unforgettable memories in the heart of Seoul. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='KR-001 | Seoul Highlights Family Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days South Korea package (KR-001 / TRG-SEO-FAM-2026): Gyeongbokgung Palace • N Seoul Tower • Myeongdong Shopping • Lotte World with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SEOUL', 1),
            _ih('Day 02: HISTORIC PALACE TOUR', 2),
            _ih('Day 03: SEOUL SKYLINE & SHOPPING', 3),
            _ih('Day 04: LOTTE WORLD ADVENTURE', 4),
            _ih('Day 05: CULTURAL EXPLORATION & LEISURE', 5),
            _ih('Day 06: DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SEOUL',
                (
                    "Arrive in Seoul. Private transfer to your handpicked premium hotel. Evening at leisure to experience the city's modern neon charm."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'HISTORIC PALACE TOUR',
                (
                    'Visit the majestic Gyeongbokgung Palace. Witness the Changing of the Royal Guard and explore Bukchon Hanok Village—a must-see cultural highlight.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'SEOUL SKYLINE & SHOPPING',
                (
                    'Take the cable car to N Seoul Tower for panoramic views. Spend the afternoon exploring the vibrant shopping streets of Myeongdong—unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'LOTTE WORLD ADVENTURE',
                (
                    "A full day of excitement at Lotte World, one of the world's largest indoor theme parks—a perfect family adventure experience."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'CULTURAL EXPLORATION & LEISURE',
                (
                    'A relaxed day exploring local culture, museums, or visiting the traditional markets, enjoying the dynamic metropolis at your own pace.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'DEPARTURE',
                (
                    'Final luxury breakfast before your TRAGUIN private transfer to the airport, completing your premium Seoul highlights expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Gyeongbokgung Palace',
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
                'Gyeongbokgung Palace',
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
                'Gyeongbokgung Palace',
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
                'Gyeongbokgung Palace',
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
            _inc_included('Premium handpicked accommodation across South Korea', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven executive transport', 2),
            _inc_included('KTX high-speed rail and domestic connections as per itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated bilingual on-ground concierge support', 4),
            _inc_excluded('International airfare and South Korea visa or K-ETA fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_kr_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KR-002'
    tour_code = 'TRAGUIN-SEOUL-JEJU-ROMANCE'
    title = 'Romantic Korea Honeymoon'
    duration = '05 Nights / 06 Days'
    slug = 'kr-002-romantic-korea-honeymoon'
    itin_slug = 'kr-002-romantic-korea-itinerary'
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
            _ph('Serial code KR-002 | TRAGUIN tour code TRAGUIN-SEOUL-JEJU-ROMANCE', 1),
            _ph('Country: South Korea, Asia | Category: Couple / Romantic HolidayDURATION: 05 Nights / 06 Days', 2),
            _ph('Destinations: Seoul (3N) • Jeju Island (2N)IDEAL FOR: Honeymooners, Couples', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Daily luxury breakfasts and designated fine-dining experiences. ✔', 7),
            _ph('TRAGUIN Signature Experience: Private, romantic evening yacht charter complete with premium wine on', 8),
            _ph('Curated by TRAGUIN Experts: Fast-track VIP entry passes to all historical palaces and high-altitude', 9),
            _ph('Personalized Assistance: A dedicated local lifestyle coordinator available via phone or messaging apps', 10),
            _ph('Premium Handpicked Hotels: Direct, guaranteed room upgrades to high-floor panoramic or full ocean', 11)
        ],
        moods=['Luxury', 'Honeymoon'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium South Korea Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Romantic Korea Honeymoon',
        overview="TOUR OVERVIEW\nThis bespoke South Korea Family Tour & Couple Itinerary is fully customized as a Private FIT (Flexible Independent Travel) experience, promising absolute flexibility and absolute luxury. Travel through the highly sought-after Top Tourist Places in South Korea in a chauffeured premium sedan, enjoying handpicked luxury accommodations, fast-tracked entry tickets, and specialized local guides. Indulge in an exquisite culinary journey featuring daily gourmet breakfasts and specialized fine dining experiences. Every single detail is refined through a signature TRAGUIN Curated Experience Note to offer unparalleled peace of mind.\n\nWHY CHOOSE A LUXURY SOUTH KOREA HOLIDAY?\nSouth Korea has rapidly emerged as a leading global hotspot for ultra-luxury couples' travel and high-end tourism. Seeking the Best South Korea Tour Package means unlocking a mesmerizing world of sophisticated contrasts. Couples can explore timeless dynastic architectural marvels, unwind in world-class wellness retreats, and capture stunning cinematic photos across South Korea's iconic Instagram locations. Whether it’s wandering through the historic, whisper-quiet alleyways of Bukchon Hanok Village or witnessing a fiery, majestic sunrise over the dramatic coastal cliffs of Jeju Island, a South Korea Honeymoon Package arranged by TRAGUIN ensures you experience the absolute pinnacle of luxury, heritage, and timeless romance.",
        seo_title='KR-002 | Romantic Korea Honeymoon | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days South Korea package (KR-002 / TRAGUIN-SEOUL-JEJU-ROMANCE): Seoul (3N) • Jeju Island (2N)IDEAL FOR: Honeymooners, Couples with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: SEOUL – ARRIVAL IN THE LAND OF THE MORNING CALM & SEOUL', 1),
            _ih('Day 02: SEOUL – TIMELESS DYNASTIC MAJESTY & PRIVATE K-CULTURE', 2),
            _ih('Day 03: NAMI ISLAND – ENCHANTED ROMANCE & THE FOREST OF FAIRY TALES', 3),
            _ih('Day 04: SEOUL TO JEJU ISLAND – THE HAWAII OF ASIA & COASTAL ROMANCE', 4),
            _ih('Day 05: JEJU ISLAND – MAJESTIC VOLCANIC WONDERS & SUNRISE SERENADE', 5),
            _ih('Day 06: JEJU TO SEOUL – FAREWELL TO THE MAGIC OF SOUTH KOREA', 6),
            _ih('TRAGUIN Signature Experience: Private, romantic evening yacht charter complete with premium wine on', 7),
            _ih('Curated by TRAGUIN Experts: Fast-track VIP entry passes to all historical palaces and high-altitude', 8),
            _ih('Personalized Assistance: A dedicated local lifestyle coordinator available via phone or messaging apps', 9)
        ],
        days=[
            _day(
                1,
                'SEOUL – ARRIVAL IN THE LAND OF THE MORNING CALM & SEOUL',
                (
                    'SIGHTSEEING Your extraordinary journey begins the moment you touch down at Incheon International Airport. Your dedicated private TRAGUIN travel concierge will meet you directly at the arrival gate to assist with expedited immigration and baggage handling. Step into your premium luxury private sedan for a smooth, scenic drive into the vibrant heart of Seoul. Arrive at your handpicked ultra-luxury hotel overlooking the serene Han River, where a chilled bottle of premium champagne and bespoke welcome amenities await you. In the late afternoon, embark on your first exclusive Seoul Sightseeing experience. Ascend the iconic N Seoul Tower on Mt. Namsan just as dusk begins to settle over the city. Walk out onto the legendary observation deck to hang your custom-engraved TRAGUIN Love Padlock against a backdrop of twinkling city lights. Conclude your perfect first evening with an intimate, candlelit fine-dining experience at a Michelin-starred contemporary Korean restaurant. Sightseeing Included: N Seoul Tower Observation Deck, Mt. Namsan Cable Car, Han River Luxury Evening Boardwalk. Optional Activities: Private traditional Hanbok high-fashion photography session at a premium studio. Evening Experience: Romantic custom love-lock ceremony at N Seoul Tower followed by a fine-dining culinary showcase.'
                ),
                [
                    'Overnight Stay: Seoul (Signiel Seoul / Four Seasons Seoul)',
                    'Meals Included: Welcome Premium Dinner (Curated by TRAGUIN)',
                ],
            ),
            _day(
                2,
                'SEOUL – TIMELESS DYNASTIC MAJESTY & PRIVATE K-CULTURE',
                (
                    'IMMERSION Immerse yourselves in the magnificent history of South Korea today. Following a lavish breakfast, your private guide will escort you on a VIP tour of Gyeongbokgung Palace, the grandest of the Five Grand Palaces. Walk hand-in-hand through the majestic Geoncheonggung Residence, bypassing standard tourist queues. To truly elevate this Premium Seoul Experience, step into custom-tailored, premium silk Hanboks, allowing you to capture stunning, cinematic photographs against the backdrop of ancient pavilions and pristine dynastic gardens. In the afternoon, enjoy a peaceful stroll through the winding, historic lanes of Bukchon Hanok Village, home to hundreds of beautifully preserved traditional Korean stone and wooden houses. Later, transition into the ultra-modern side of town with an exclusive VIP personal shopping experience in the luxurious fashion districts of Gangnam and Apgujeong Rodeo Street, beautifully arranged under the professional guidance of your TRAGUIN lifestyle consultant. Sightseeing Included: Gyeongbokgung Palace (VIP Access), Bukchon Hanok Village, Insadong Antique Cultural Street, Gangnam District. Optional Activities: Private luxury Korean tea tasting ceremony conducted by a master artisan in an exclusive Hanok. Evening Experience: Sunset private yacht charter along the Han River with premium wine, cheeses, and live acoustic music.'
                ),
                [
                    'Overnight Stay: Seoul (Signiel Seoul / Four Seasons Seoul)',
                    'Meals Included: Gourmet Breakfast & Luxury Korean BBQ Lunch Experience',
                ],
            ),
            _day(
                3,
                'NAMI ISLAND – ENCHANTED ROMANCE & THE FOREST OF FAIRY TALES',
                (
                    "Today, journey outside the bustling capital to the ethereal, fairytale world of Nami Island—a corner-stone of any premium South Korea Honeymoon Package. After a comfortable, scenic drive, board a private luxury speedboat to reach the island. Famed globally as the filming location for iconic K-dramas, Nami Island offers unparalleled natural beauty. Walk along the breathtaking, towering paths of Metasequoia trees, capturing memories that will last a lifetime. In the afternoon, enjoy an exclusive, intimate rail-bike experience at Gangchon, pedaling along historic, abandoned railway tracks while taking in sweeping panoramic views of the beautiful Bukhangang River valley. Return to Seoul in the evening, where TRAGUIN has reserved a premium table for you at a high- end lounge overlooking the glittering city skyline. Sightseeing Included: Nami Island Eco-Reserve, Metasequoia Lane, Gangchon Romantic Rail-Bike Track, Private Speedboat Transfers. Optional Activities: Couples' holistic wellness spa therapy session using rare, organic Korean ginseng at an award-winning spa. Evening Experience: High-altitude craft cocktail tasting session on the 100th floor of the Lotte World Tower."
                ),
                [
                    'Overnight Stay: Seoul (Signiel Seoul / Four Seasons Seoul)',
                    'Meals Included: Gourmet Breakfast & Local Chuncheon Dakgalbi Lakeside Lunch',
                ],
            ),
            _day(
                4,
                'SEOUL TO JEJU ISLAND – THE HAWAII OF ASIA & COASTAL ROMANCE',
                (
                    'Bid a temporary farewell to Seoul as your private chauffeur drives you to Gimpo Airport for a premium domestic flight to Jeju Island. Universally celebrated as one of the Top Tourist Places in South Korea for couples, Jeju welcomes you with warm tropical breezes and stunning emerald waters. A luxury SUV will pick you up at Jeju International Airport and drive you along the beautiful Aewol Coastal Road, a prime Instagram location renowned for its dramatic black basalt cliffs and fashionable seaside cafes. Check into your stunning ultra-luxury private pool villa at the legendary Jeju Shinhwa World or The Cliff House. Spend the afternoon exploring the magical, cascading waters of Cheonjiyeon Waterfall, hidden deep within lush, subtropical forests. As the sun begins to set, stroll hand-in-hand along the soft, golden sands of Jungmun Saekdal Beach. Sightseeing Included: Aewol Scenic Coastal Road, Cheonjiyeon Hidden Waterfall, Jungmun Romantic Beach Walk. Optional Activities: Premium submarine dive tour to explore the vibrant, colourful coral reefs of Seogwipo. Evening Experience: An exquisite seafood fine-dining experience featuring fresh catch prepared by a private chef right on the beach.'
                ),
                [
                    'Overnight Stay: Jeju Island (Grand Hyatt Jeju / Shilla Jeju Luxury Pool Villa)',
                    'Meals Included: Gourmet Breakfast & Premium Coastal Fusion Dinner',
                ],
            ),
            _day(
                5,
                'JEJU ISLAND – MAJESTIC VOLCANIC WONDERS & SUNRISE SERENADE',
                (
                    "Begin your morning early with a truly unforgettable experience curated specially by TRAGUIN. Journey to Seongsan Ilchulbong, a breathtaking UNESCO World Heritage tuff cone rising dramatically out of the ocean. Watch the spectacular sunrise paint the sky in deep shades of gold and crimson. This is widely considered the ultimate photography point across all TRAGUIN South Korea Packages. Following a relaxing breakfast back at your resort, explore the surreal, moss-covered depths of Manjanggul Cave, one of the finest lava tunnels anywhere on Earth. Spend your afternoon wandering through the beautifully fragrant, endless green terraces of the O'sulloc Green Tea Plantation. Sip artisanal matcha lattes while overlooking the peaceful fields, and treat yourselves to a private premium skincare workshop at the nearby Innisfree Jeju House. Sightseeing Included: Seongsan Ilchulbong Sunrise Peak, Manjanggul UNESCO Lava Cave, O'sulloc Premium Green Tea Plantation. Optional Activities: Scenic private helicopter ride over the majestic, snow-capped crater of Mt. Hallasan. Evening Experience: Farewell premium beachside campfire luxury barbecue with curated wines, organized exclusively by TRAGUIN."
                ),
                [
                    'Overnight Stay: Jeju Island (Grand Hyatt Jeju / Shilla Jeju Luxury Pool Villa)',
                    'Meals Included: Gourmet Breakfast, Traditional Jeju Black Pork Lunch Feast, & Farewell Wine Dinner',
                ],
            ),
            _day(
                6,
                'JEJU TO SEOUL – FAREWELL TO THE MAGIC OF SOUTH KOREA',
                (
                    "Savor your final luxurious breakfast overlooking the beautiful ocean. Spend a peaceful morning relaxing inside your private pool villa or picking up unique, local souvenirs like Jeju mandarin chocolates and organic skincare products at the bustling Dongmun Traditional Market. In the afternoon, your private chauffeur will drive you to Jeju International Airport for your flight back to Incheon International Airport in Seoul, where you will board your international flight home. You leave with spirits renewed and a heart filled with unforgettable memories, courtesy of your premier travel partner, TRAGUIN. Sightseeing Included: Dongmun Traditional Market, Jeju Duty-Free Lounge Access. Optional Activities: Last-minute premium relaxation session inside the airport's exclusive first-class VIP lounge."
                ),
                [
                    'Meals Included: Gourmet Breakfast served in-villa.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Lotte Hotel Seoul Deluxe Room Maison Glad Jeju Premium Room Daily Buffet Breakfast, Wi-Fi, Welcome Mocktails Tier / Option Seoul Stays (03 Nights) Jeju Stays (02 Nights) Inclusions & Features',
                'Multi-city South Korea',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Lotte Hotel Seoul Deluxe Room Maison Glad Jeju Premium Room Daily Buffet Breakfast, Wi-Fi, Welcome Mocktails Tier / Opti',
            ),
            _hotel(
                'The Shilla Seoul Executive Business Room Parnas Hotel Jeju Deluxe Ocean View Executive Lounge Access, High Tea, Curated Breakfast',
                'Multi-city South Korea',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — The Shilla Seoul Executive Business Room Parnas Hotel Jeju Deluxe Ocean View Executive Lounge Access, High Tea, Curated ',
            ),
            _hotel(
                'Four Seasons Hotel Seoul Premier Room (City View) Grand Hyatt Jeju Grand Suite Ocean View Champagne on Arrival, Spa Credits, Dedicated Concierge',
                'Multi-city South Korea',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Four Seasons Hotel Seoul Premier Room (City View) Grand Hyatt Jeju Grand Suite Ocean View Champagne on Arrival, Spa Cred',
            ),
            _hotel(
                'Signiel Seoul Premier Suite (Han River View) The Shilla Jeju Luxury Private Pool Villa Personalized Butler, Private Yacht Cruise, TRAGUIN VIP Support ✔',
                'Multi-city South Korea',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Signiel Seoul Premier Suite (Han River View) The Shilla Jeju Luxury Private Pool Villa Personalized Butler, Private Yach',
            )
        ],
        inclusions=[
            _inc_included('Handpicked Hotels: 05 Nights in top-tier luxury accommodations.', 1),
            _inc_included('Curated Experiences: VIP entry to all palaces and monuments mentioned.', 2),
            _inc_included('Luxury Transportation: Private, air-conditioned sedan throughout the tour.', 3),
            _inc_included('Domestic Flights: Return premium flights between Seoul and Jeju Island.', 4),
            _inc_included('Gourmet Meal Plan: Daily luxury breakfasts and designated fine-dining experiences.', 5),
            _inc_included('TRAGUIN Support: 24/7 dedicated on-ground client care and assistance.', 6),
            _inc_included('Welcome Amenities: Complementary champagne, love padlocks, and fresh local fruits.', 7),
            _inc_excluded('International Flights: Main roundtrip international airfares.', 8),
            _inc_excluded('Visa Fees: South Korea tourist visa application charges.', 9),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, premium drinks, and tips.', 10),
            _inc_excluded('Insurance: International travel and comprehensive medical insurance.', 11),
            _inc_excluded('Optional Tours: Any activities or excursions listed as optional in the itinerary.', 12),
        ],
    )
    return package, itinerary

def build_kr_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KR-003'
    tour_code = 'TRAGUIN-KLUXURY-003'
    title = 'South Korea Luxury Tour'
    duration = '06 Nights / 07 Days'
    slug = 'kr-003-south-korea-luxury-tour'
    itin_slug = 'kr-003-south-korea-luxury-itinerary'
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
            _ph('Serial code KR-003 | TRAGUIN tour code TRAGUIN-KLUXURY-003', 1),
            _ph('Country: South Korea, Asia | Category: Luxury Travel DURATION: 06 Nights / 07 Days', 2),
            _ph('Destinations: Seoul • Gyeongju • Busan • Jeju Island', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Royal Korean Breakfast daily, with exclusive fine-dining Michelin recommendations. Route Guide: Seoul (2N) → Gyeongju (1N) → Busan (1N) → Jeju Island (2N) DESTINATION SEO INSIGHT & HIGHLIGHTS When sel', 7),
            _ph('TRAGUIN Signature Experience: Private, after-hours custom tea blending session with a master tea', 8),
            _ph('Curated by TRAGUIN Experts: Every itinerary element is vetted by our global destination designers to', 9),
            _ph('Personalized Concierge: Seamless real-time adjustments, premium restaurant reservations, and priority', 10)
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
        price_note='On Request (Premium South Korea Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='South Korea Luxury Tour',
        overview="Seoul • Gyeongju • Busan • Jeju Island 06 Nights / 07 Days Premium Experiential Journey SERIAL CODE: KR-003 STATE / COUNTRY: South Korea CATEGORY: Luxury Travel DURATION: 06 Nights / 07 Days IDEAL FOR: Families & Discerning Couples BEST SEASON: Spring (Apr–Jun) & Autumn (Sep–Nov) STARTING PRICE: On Request (Premium FIT) TRAGUIN TOUR CODE: TRAGUIN-KLUXURY-003 Welcome to an extraordinary exploration curated exclusively by TRAGUIN. This Best South Korea Tour Package invitations you to immerse your family into a realm where hyper-modern futuristic skylines seamlessly blend with ancient, serene dynastic traditions. Experience the ultimate Luxury South Korea Holiday, traversing through historical palaces, private high-tech culinary journeys, and breathtaking coastal landscapes, all wrapped in flawless, personalized signature hospitality.\n\nTOUR OVERVIEW\nThis bespoke South Korea Family Tour is crafted as a premium FIT (Fully Independent Traveler) itinerary, utilizing top-tier private executive transport and handpicked five-star accommodations. Your journey connects the ultra-chic energy of Seoul, the regal timelessness of Gyeongju, the dynamic marine elegance of Busan, and the volcanic wonders of Jeju Island. Every single day features TRAGUIN curated experiences designed to create unforgettable family memories. Travel Mechanism: Private Chauffeur-driven Premium Executive MPV throughout. Meal Plan: Royal Korean Breakfast daily, with exclusive fine-dining Michelin recommendations. Route Guide: Seoul (2N) → Gyeongju (1N) → Busan (1N) → Jeju Island (2N)\n\nWhy Visit Now: A perfect synergy of historic Joseon dynasty grandeur, UNESCO world heritage sites,\ncutting-edge skincare wellness clinics, and world-renowned K-culture aesthetics. Famous Attractions Covered: Gyeongbokgung Palace, Bukchon Hanok Village, Bulguksa Temple, Haeundae Beach, and Seongsan Ilchulbong. Most Searched Luxury Experiences: Private VIP Hanbok photoshoots, authentic Korean tea ceremonies in hidden courtyard estates, high-speed KTX First Class transits, and helicopter or luxury private yacht charters. Instagram & Photography Coordinates: Starfield Library, Gamcheon Culture Village, and the sunset vistas over Jeju's dramatic black-lava basalt coastlines.",
        seo_title='KR-003 | South Korea Luxury Tour | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days South Korea package (KR-003 / TRAGUIN-KLUXURY-003): Seoul • Gyeongju • Busan • Jeju Island with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: SEOUL — GRAND ARRIVAL & ULTRA-LUXURY WELCOME', 1),
            _ih('Day 02: SEOUL — DYNASTIC MAJESTY & IMMERSIVE K-CULTURE', 2),
            _ih('Day 03: GYEONGJU — THE ANCIENT KINGDOM OF SHILLA', 3),
            _ih('Day 04: BUSAN — MARITIME GRANDEUR & COASTAL SOPHISTICATION', 4),
            _ih('Day 05: JEJU ISLAND — VOLCANIC WONDERS & PRISTINE NATURE', 5),
            _ih('Day 06: JEJU ISLAND — TEA PLANTATIONS & MAJESTIC WATERFALLS', 6),
            _ih('Day 07: DEPARTURE — END OF A LUXURY ODYSSEY', 7),
            _ih('TRAGUIN Signature Experience: Private, after-hours custom tea blending session with a master tea', 8),
            _ih('Curated by TRAGUIN Experts: Every itinerary element is vetted by our global destination designers to', 9),
            _ih('Personalized Concierge: Seamless real-time adjustments, premium restaurant reservations, and priority', 10)
        ],
        days=[
            _day(
                1,
                'SEOUL — GRAND ARRIVAL & ULTRA-LUXURY WELCOME',
                (
                    'Touch down at Incheon International Airport where your private TRAGUIN VIP Airport Concierge greets you at the jet bridge, fast-tracking you through immigration and customs. Step into a luxury executive sedan and enjoy a smooth, scenic transfer along the Han River into the heart of Seoul. Check into your ultra-luxury handpicked hotel, hovering elegantly above the city skyline. Spend your afternoon unwinding in your premium suite or exploring the high-end boutique avenues of Apgujeong Rodeo Street. As twilight falls, embark on a private chauffeured evening drive to Namsan Seoul Tower for a panoramic introductory gaze at this glittering mega-city. SIGHTSEEING: Incheon VIP Fast-track, Namsan Tower View OPTIONAL: Sulwhasoo Spa Treatment EVENING: Welcome Dinner at Michelin Starred Gaon OVERNIGHT: Signiel Seoul (Ultra- Luxury)'
                ),
                [
                    'MEALS: Welcome Drink',
                ],
            ),
            _day(
                2,
                'SEOUL — DYNASTIC MAJESTY & IMMERSIVE K-CULTURE',
                (
                    'Begin your morning with a premium Seoul Sightseeing experience. Adorn custom-tailored silk Hanboks for a private, early-access guided walk through Gyeongbokgung Palace, capturing stunning family photographs before the crowds arrive. Meander through the labyrinthine alleys of Bukchon Hanok Village, where aristocrats resided centuries ago. In the afternoon, transition from the old world to the ultra-new with a private tour of the Samsung Innovation Museum or an exclusive private K-Pop dance masterclass for the family. Conclude the day with a serene, premium traditional tea blending ceremony inside a private wooden courtyard house in Insadong. SIGHTSEEING: Gyeongbokgung Palace, Bukchon, Insadong OPTIONAL: Private Hanbok VIP Photoshoot EVENING: Han River Luxury Sunset Yacht Cruise OVERNIGHT: Signiel Seoul (Ultra- Luxury)'
                ),
                [
                    'MEALS: Breakfast',
                ],
            ),
            _day(
                3,
                'GYEONGJU — THE ANCIENT KINGDOM OF SHILLA',
                (
                    'Board the high-speed KTX bullet train in First Class, transitioning swiftly southwards to Gyeongju, affectionately termed "the museum without walls." Your private TRAGUIN local expert historian meets you at the station. Spend a profound afternoon exploring the UNESCO-listed Bulguksa Temple, a masterpiece of Buddhist architecture, alongside the mystical Seokguram Grotto. Walk amidst the colossal royal burial mounds at Daereungwon Tomb Complex, feeling the spiritual echoes of old kings. As night falls, witness the breathtaking illumination of Donggung Palace and Wolji Pond, where ancient royalty held lavish banquets, perfectly reflecting across the glass-like water. SIGHTSEEING: Bulguksa Temple, Daereungwon, Wolji Pond OPTIONAL: Traditional Pottery Making Workshop EVENING: Starlight walk by Cheomseongdae Observatory OVERNIGHT: Lahan Select Gyeongju (Premium Lake View)'
                ),
                [
                    'MEALS: Breakfast',
                ],
            ),
            _day(
                4,
                'BUSAN — MARITIME GRANDEUR & COASTAL SOPHISTICATION',
                (
                    "A short luxury drive brings your family to Busan, South Korea's vibrant, sophisticated maritime metropolis. Your first destination is the breathtaking Haedong Yonggungsa Temple, uniquely situated directly on the craggy ocean cliffs. Spend the afternoon wandering through the multi-colored, artistic slopes of Gamcheon Culture Village, collecting unique artisanal souvenirs and stopping at trendy panoramic cafes. Later, experience the spectacular Haeundae Blueline Park sky capsules, gliding gracefully above the ocean. In the evening, step onto a private luxury catamaran charter from Suyeongman Marina, sipping champagne under the neon majesty of the Gwangan Diamond Bridge. SIGHTSEEING: Haedong Yonggungsa, Gamcheon, Haeundae OPTIONAL: Jagalchi Premium Seafood Culinary Tour EVENING: Private Catamaran Yacht Cruise with Fireworks OVERNIGHT: Park Hyatt Busan (Ocean View Suite)"
                ),
                [
                    'MEALS: Breakfast',
                ],
            ),
            _day(
                5,
                'JEJU ISLAND — VOLCANIC WONDERS & PRISTINE NATURE',
                (
                    "Transfer to Gimhae Airport for a premium short flight to Jeju Island, a legendary paradise of natural wonders. Upon landing, board your luxury private MPV and head straight towards the dramatic east coast. Witness the awe-inspiring Seongsan Ilchulbong (Sunrise Peak), a magnificent volcanic tuff cone rising majestically from the sea. Next, explore the mysterious underground world of Manjanggul Cave, one of the finest lava tunnels globally. In the afternoon, enjoy an exclusive interaction with Jeju's iconic 'Haenyeo' female divers, learning about their legendary free-diving heritage and enjoying freshly caught premium seafood prepared right on the shore. SIGHTSEEING: Seongsan Ilchulbong, Manjanggul, Haenyeo Experience OPTIONAL: Horseback Riding on Black Sand Beaches EVENING: Traditional Black Pork BBQ Fine Dining OVERNIGHT: The Shilla Jeju (Luxury Resort)"
                ),
                [
                    'MEALS: Breakfast',
                ],
            ),
            _day(
                6,
                'JEJU ISLAND — TEA PLANTATIONS & MAJESTIC WATERFALLS',
                (
                    "Dedicate your final exploration day to Jeju's serene southern coast. Stroll through the lush, emerald expanses of the Osulloc Tea Museum and green tea fields, participating in a premium private tea-stone class. Discover the majestic, multi-tiered Cheonjiyeon Waterfall, shrouded in rich local mythology, followed by the striking Jusangjeolli Cliff hexagonal rock formations, sculpted intricately by ancient volcanic lava flows. Spend your final evening enjoying a premium family farewell dinner arranged by TRAGUIN, reflecting on an incredible week of shared moments. SIGHTSEEING: Osulloc Tea, Cheonjiyeon Falls, Jusangjeolli OPTIONAL: Hello Kitty Island (For Families with Kids) EVENING: Exclusive Multi-course Royal Court Dinner OVERNIGHT: The Shilla Jeju (Luxury Resort)"
                ),
                [
                    'MEALS: Breakfast',
                ],
            ),
            _day(
                7,
                'DEPARTURE — END OF A LUXURY ODYSSEY',
                (
                    'Enjoy a leisurely morning breakfast at your luxury resort before checking out. Your private chauffeur will transfer your family seamlessly back to Jeju International Airport for your domestic flight to Seoul Incheon, perfectly timed to connect with your international departure home. Carry along beautiful, unforgettable family memories curated flawlessly by TRAGUIN. SIGHTSEEING: None / Departure Transfer OPTIONAL: Airport Duty-Free VIP Escort EVENING: Board International Flight OVERNIGHT: In Flight'
                ),
                [
                    'MEALS: Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'GYEONGJU STAYS',
                'Seoul',
                '6N',
                'Nights)',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – NIGHTS): GYEONGJU STAYS | Deluxe Room | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Deluxe (4★ / 5★',
                'Seoul',
                '6N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – DELUXE: Deluxe (4★ / 5★ | Deluxe Room | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Parnas Hotel Jeju',
                'Seoul',
                '6N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – PREMIUM: Parnas Hotel Jeju | Deluxe Room | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                '5★)',
                'Seoul',
                '6N',
                'Luxury',
                'Lahan Select (Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – LUXURY: 5★) | Lahan Select (Suite | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 06 Nights in ultra-luxury, handpicked hotels.', 1),
            _inc_included('Transport: Dedicated private executive MPV (Kia Carnival or similar).', 2),
            _inc_included('Transit: KTX High-Speed Train First Class tickets (Seoul to Gyeongju).', 3),
            _inc_included('Curated Experiences: Han River Sunset Yacht & Busan Catamaran Cruises.', 4),
            _inc_included('Guiding: Professional English-speaking elite guides for all sightseeing.', 5),
            _inc_included('Welcome Amenities: Custom VIP arrival kit and traditional gifts.', 6),
            _inc_included('Support: 24/7 dedicated TRAGUIN concierge assistance line.', 7),
            _inc_excluded('Airfare: International and domestic flight tickets.', 8),
            _inc_excluded('Visas: K-ETA or formal South Korea entry visa processing.', 9),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, mini-bar billing.', 10),
            _inc_excluded('Meals: Lunches and dinners not specified in the final plan.', 11),
            _inc_excluded('Tipping: Gratuities for elite guides and private chauffeurs.', 12),
            _inc_excluded('Insurance: Comprehensive premium international travel insurance.', 13),
        ],
    )
    return package, itinerary

def build_kr_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KR-005'
    tour_code = 'KR-005-PREM'
    title = 'Premium South Korea Tour'
    duration = '6 Nights / 7 Days'
    slug = 'kr-005-premium-south-korea-tour'
    itin_slug = 'kr-005-premium-south-korea-itinerary'
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
            _ph('Serial code KR-005 | TRAGUIN tour code KR-005-PREM', 1),
            _ph('Country: South Korea, Asia | Category: Premium Luxury', 2),
            _ph('Destinations: Seoul • Nami Island • Busan | 6 Nights / 7 Days', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Executive Sedan / Buffet Breakfast & Curated Dinners', 7)
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
        price_note='On Request (Premium South Korea Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Premium South Korea Tour',
        overview='TOUR DETAILS SERIAL CODE: KR-005 COUNTRY: South Korea CATEGORY: Premium Luxury DURATION: 6 Nights / 7 Days IDEAL FOR: Family, Couples, Luxury Travelers TRAGUIN TOUR CODE: KR-005-PREM\n\nTOUR OVERVIEW\nExperience the perfect blend of ancient heritage and futuristic innovation with our TRAGUIN curated experience in South Korea. From the bustling streets of Seoul to the serene beauty of Nami Island and the coastal charm of Busan, this luxury holiday is designed to create unforgettable memories. Our TRAGUIN experts have handpicked premium stays to ensure your comfort.\n\nWhy visit South Korea? Because it offers\niconic attractions like Gyeongbokgung Palace, the futuristic N Seoul Tower, and breathtaking landscapes in Busan. The Best South Korea Tour Package ensures you see it all. Popular Instagram locations include the vibrant Myeongdong market and the stunning architecture of Dongdaemun Design Plaza. Experience the Premium South Korea Experience with TRAGUIN.',
        seo_title='KR-005 | Premium South Korea Tour | TRAGUIN',
        seo_description='Premium 6 Nights / 7 Days South Korea package (KR-005 / KR-005-PREM): Seoul • Nami Island • Busan | 6 Nights / 7 Days with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SEOUL', 1),
            _ih('Day 02: SEOUL CITY TOUR', 2),
            _ih('Day 03: NAMI ISLAND & GARDEN OF MORNING CALM', 3),
            _ih('Day 04: SEOUL TO BUSAN (BY KTX)', 4),
            _ih('Day 05: BUSAN HIGHLIGHTS', 5),
            _ih('Day 06: BUSAN TO SEOUL', 6),
            _ih('Day 07: DEPARTURE', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SEOUL',
                (
                    'Welcome to South Korea! Upon arrival, our representative will assist you to your premium hotel. Enjoy a luxury check-in experience curated by TRAGUIN. Evening at leisure to explore nearby luxury boutiques.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'SEOUL CITY TOUR',
                (
                    'Explore Gyeongbokgung Palace, Bukchon Hanok Village, and the N Seoul Tower. Discover why this is the Best South Korea Tour Package for families. Dinner featuring authentic Korean cuisine.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'NAMI ISLAND & GARDEN OF MORNING CALM',
                (
                    'A scenic drive to Nami Island. Enjoy breathtaking landscapes and immersive experiences. This Luxury South Korea Holiday highlight is perfect for photography.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'SEOUL TO BUSAN (BY KTX)',
                (
                    'Travel in comfort via the high-speed KTX train to Busan. Check into your ultra-luxury resort. Experience the coastal beauty of this top tourist place in South Korea.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'BUSAN HIGHLIGHTS',
                (
                    'Visit Gamcheon Culture Village, Haeundae Beach, and Haedong Yonggungsa Temple. TRAGUIN ensures exclusive recommendations for your family trip.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'BUSAN TO SEOUL',
                (
                    'Return to Seoul for final shopping at Dongdaemun. Indulge in premium dining experiences.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'DEPARTURE',
                (
                    'After breakfast, transfer to the airport for your flight back home with unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Seoul',
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
                'Seoul',
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
                'Seoul',
                '6N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Seoul',
                '6N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included('Luxury Accommodation (6 Nights)', 1),
            _inc_included('Daily Breakfast & Selected Dinners', 2),
            _inc_included('Private Luxury Transfers', 3),
            _inc_excluded('International airfare and South Korea visa or K-ETA fees', 4),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 5),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 6),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 7),
        ],
    )
    return package, itinerary

SOUTH_KOREA_KR_001_005_BUILDERS = [
    build_kr_001,
    build_kr_002,
    build_kr_003,
    build_kr_005,
]
