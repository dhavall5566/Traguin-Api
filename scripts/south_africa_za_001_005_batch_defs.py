"""Builder functions for ZA-001 through ZA-005 South Africa international packages."""

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

ZA_SLUG = "south-africa"


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


def build_za_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ZA-001'
    tour_code = 'TRAGUIN-ZA-001-PREMIUM'
    title = 'South Africa Family Tour'
    duration = '07 Nights / 08 Days'
    slug = 'za-001-south-africa-family-tour'
    itin_slug = 'za-001-south-africa-family-itinerary'
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
            _ph('Serial code ZA-001 | TRAGUIN tour code TRAGUIN-ZA-001-PREMIUM', 1),
            _ph('Country: South Africa, Southern Africa | Category: Family / Premium Luxury Holidays DURATION: 07 Nights / 08 Days', 2),
            _ph('Destinations: Cape Town (4N) • Garden Route / Knysna (2N) • Shamwari Private Game Reserve (1N)', 3),
            _ph('Ideal for: Premium Families, Luxury Leisure Seekers, Wildlife Enthusiasts', 4),
            _ph('Best season: Year-Round (October to April is ideal for beaches; May to September for Safari)', 5),
            _ph('Starting price: On Request (Premium Curated Pricing)', 6),
            _ph('Vehicle / Meals: Modified American Plan (Daily Premium Breakfast & Multi-Course Gourmet Dinners)', 7)
        ],
        moods=['Family', 'Luxury', 'Safari'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium South Africa Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='South Africa Family Tour',
        overview='South Africa Highlights: Cape Town • Garden Route • Luxury Safari 07 NIGHTS / 08 DAYS PREMIUM FAMILY EXPERIENCE Welcome to a majestic adventure meticulously planned for your loved ones. The Best South Africa Tour Package by TRAGUIN unlocks the untamed natural elegance, spectacular coastal highways, and thrilling big- game safaris of the African continent. From the cloud-capped flat top of Table Mountain to the deep emerald estuaries of the Garden Route, this Luxury South Africa Holiday seamlessly balances world-class relaxation with edge-of-your-seat excitement. Count on TRAGUIN to craft handpicked hotels and exclusive experiences that blossom into lifelong memories for your family.\n\nTOUR OVERVIEW\nThis strictly private, top-tier family plan serves as the gold standard of TRAGUIN South Africa Packages. Designed with an optimal family-friendly pace, this operational route minimizes stress and maximizes premium comfort. Bask in private executive transfers, a rich premium meal plan showcasing exquisite culinary artistry, and a hand-curated collection of iconic attractions overseen by seasoned regional tour managers. Route: Cape Town (4 Nights) ➔ Garden Route / Knysna (2 Nights) ➔ Private Game Reserve (1 Night) Vehicle: Private Chauffeur-driven Premium Mercedes Sprinter / Luxury SUV Transfers Meal Plan: Modified American Plan (Daily Premium Breakfast & Multi-Course Gourmet Dinners) TRAGUIN Curated Experience Note: Includes private cable car skip-the-line privileges, curated penguin colony encounters at Boulders Beach, and exclusive 4x4 open-top game drives led by senior game rangers.\n\nWHY CHOOSE A PREMIUM SOUTH AFRICA FAMILY TOUR?\nSouth Africa stands proudly as a world-class premier travel destination, perfectly merging urban European sophistication with raw African wildness. Booking a Premium South Africa Experience with TRAGUIN turns standard sightseeing into an elite, private holiday escape. Famous Attractions: Table Mountain, Cape Point Nature Reserve, Boulders Beach Penguin Colony, Knysna Heads, and the Big Five game reserves. Most Searched Experiences: Standing at the southwesternmost tip of Africa, private whale watching in Hermanus, and watching lions track prey under golden savanna sunsets. Best Honeymoon / Family Points: The V&A Waterfront provides completely secure, high-end family entertainment, boutique dining, and popular Instagram locations for vibrant group photography. Adventure & Shopping: Shop for diamond legacy pieces and gold jewelry at high-end boutiques, zipline through ancient tree canopies, or sample premier artisanal chocolates. YOUR BESPOKE DAY-WISE ITINERARY',
        seo_title='ZA-001 | South Africa Family Tour | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days South Africa package (ZA-001 / TRAGUIN-ZA-001-PREMIUM): Cape Town (4N) • Garden Route / Knysna (2N) • Shamwari Private Game Reserve (1N) with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: CAPE TOWN — ARRIVAL IN THE MOTHER CITY & GOURMET WATERFRONT', 1),
            _ih('Day 02: CAPE TOWN — TABLE MOUNTAIN SUMMIT & HISTORIC CITY SIGHTSEEING', 2),
            _ih('Day 03: CAPE TOWN — FULL DAY CAPE PENINSULA & BOULDERS BEACH PENGUIN', 3),
            _ih('Day 04: CAPE TOWN', 4),
            _ih('Day 05: KNYSNA — JOURNEY TO THE EMERALD GARDEN ROUTE & LAGOON CRUISE', 5),
            _ih('Day 06: KNYSNA — OUDTSHOORN ADVENTURE: CANGO CAVES & OSTRICH FARM', 6),
            _ih('Day 07: PRIVATE GAME RESERVE — LUXURY SAFARI LODGE & BIG FIVE SUNSET GAME', 7),
            _ih('Day 08: GQEBERHA (PORT ELIZABETH) — MORNING SAFARI & HOMEWARD DEPARTURE', 8)
        ],
        days=[
            _day(
                1,
                'CAPE TOWN — ARRIVAL IN THE MOTHER CITY & GOURMET WATERFRONT',
                (
                    'WELCOME Step onto South African soil at Cape Town International Airport. Your premium South Africa Sightseeing vacation launches with an exclusive, warm meet-and-greet by our private chauffeur. Transfer effortlessly to your ultra-luxury harborfront hotel. Spend your afternoon unwinding or soaking in the ocean breeze. In the evening, enjoy a special TRAGUIN welcome dinner at a premium restaurant on the Victoria & Alfred Waterfront.'
                ),
                [
                    'Sightseeing Included: Private airport pick-up, V&A Waterfront luxury exploration',
                    'Evening Experience: Waterfront Fine Dining Welcome Experience',
                    'Overnight Stay: Cape Town (Handpicked Premium Luxury Hotel)',
                    'Meals Included: Welcome Dinner',
                ],
            ),
            _day(
                2,
                'CAPE TOWN — TABLE MOUNTAIN SUMMIT & HISTORIC CITY SIGHTSEEING',
                (
                    "Awake to a gorgeous coastal morning. Today, enjoy skip-the-line access to the revolving Table Mountain Aerial Cableway for panoramic, breathtaking landscapes of the Atlantic Ocean. After descending, explore the rainbow-colored historic homes of Bo-Kaap, the tranquil Company's Gardens, and the majestic Castle of Good Hope. End the day with a relaxed family photography session at Signal Hill during sunset."
                ),
                [
                    'Sightseeing Included: Table Mountain (Weather Permitting), Bo-Kaap, City Orientation Tour',
                    'Evening Experience: High-end Cape Malay culinary dinner experience',
                    'Overnight Stay: Cape Town',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'CAPE TOWN — FULL DAY CAPE PENINSULA & BOULDERS BEACH PENGUIN',
                (
                    "ENCOUNTER Embark on one of the earth's most iconic coastal drives along Chapman’s Peak, capturing rugged cliffs crashing into turquoise waves. Reach Cape Point Nature Reserve and ride the Flying Dutchman Funicular up to the historic lighthouse. After a delicious seafood lunch, stop at Boulders Beach for a premium close-up view of the famous African Penguin colony—a delightful highlight for children and families alike."
                ),
                [
                    'Sightseeing Included: Chapman’s Peak Drive, Cape of Good Hope, Boulders Beach Penguins',
                    'Optional Activities: Seal Island private boat cruise from Hout Bay',
                    'Overnight Stay: Cape Town',
                    'Meals Included: Premium Breakfast & Seafood Lunch',
                ],
            ),
            _day(
                4,
                'CAPE TOWN | STELLENBOSCH WINELANDS & ARTISANAL CHOCOLATE TASTING',
                (
                    'Journey into the sun-drenched valleys of Stellenbosch and Franschhoek, flanked by towering blue mountains. Tour historic Cape Dutch estates where adults can indulge in premium wine-tasting masterclasses while children enjoy artisanal chocolate-making workshops and juice pairings. Stroll through Oak-lined avenues packed with art galleries and premium jewelry boutiques.'
                ),
                [
                    'Sightseeing Included: Stellenbosch historic walk, Premium Estate Estate Tour',
                    'Evening Experience: Relaxed evening leisure walk at Camps Bay promenade',
                    'Overnight Stay: Cape Town',
                    'Meals Included: Premium Breakfast & Estate Lunch',
                ],
            ),
            _day(
                5,
                'KNYSNA — JOURNEY TO THE EMERALD GARDEN ROUTE & LAGOON CRUISE',
                (
                    'Check out and enjoy a scenic private transfer down the world-renowned Garden Route. Pass through lush coastal forests and quaint seaside hamlets, arriving at the romantic lagoon town of Knysna. In the late afternoon, step aboard a premium luxury catamaran cruise across the vast Knysna Lagoon, sailing right to the dramatic sandstone ocean gateway known as the Knysna Heads.'
                ),
                [
                    'Sightseeing Included: Scenic Garden Route Highway Drive, Knysna Lagoon Catamaran Cruise',
                    'Evening Experience: Oyster tasting and lagoon-side gourmet dining',
                    'Overnight Stay: Knysna (Premium Waterfront Stay)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                6,
                'KNYSNA — OUDTSHOORN ADVENTURE: CANGO CAVES & OSTRICH FARM',
                (
                    'Take a day trip across the Outeniqua Pass to Oudtshoorn, the ostrich capital of the world. Go deep into the subterranean chambers of the Cango Caves, marveling at towering limestone stalactites lit with brilliant accent colors. Afterward, enjoy an interactive tour of a premium ostrich farm where the family can feed these magnificent birds and learn about local conservation efforts.'
                ),
                [
                    'Sightseeing Included: Cango Caves Guided Tour, Safari Ostrich Farm Experience',
                    'Optional Activities: Guided meerkat safari at dawn',
                    'Overnight Stay: Knysna',
                    'Meals Included: Premium Breakfast & Braai (BBQ) Lunch',
                ],
            ),
            _day(
                7,
                'PRIVATE GAME RESERVE — LUXURY SAFARI LODGE & BIG FIVE SUNSET GAME',
                (
                    'DRIVE Drive to a renowned malaria-free private game reserve, home to an opulent safari lodge. Check into your premium thatch-roof luxury suite. Following a traditional high tea, climb into a private 4x4 open safari vehicle. Under the expert guidance of a professional ranger, track lions, elephants, leopards, rhinos, and buffaloes. Toast to the sunset with premium drinks right in the middle of the African bush.'
                ),
                [
                    'Sightseeing Included: Afternoon Big 5 Game Drive, Luxury Safari High Tea',
                    'Evening Experience: Boma bonfire dinner under the canopy of southern stars',
                    'Overnight Stay: Shamwari / Eastern Cape Luxury Safari Lodge',
                    'Meals Included: Premium Breakfast, Lunch, & Gourmet Boma Dinner',
                ],
            ),
            _day(
                8,
                'GQEBERHA (PORT ELIZABETH) — MORNING SAFARI & HOMEWARD DEPARTURE',
                (
                    'Set out on a final dawn game drive as the African savanna awakens, capturing beautiful photos of wild animals grazing in the morning mist. Return to the lodge for a hearty premium breakfast. Afterward, your private chauffeur drives you comfortably to Chief Dawid Stuurman International Airport in Gqeberha (Port Elizabeth) for your domestic flight to Johannesburg/Cape Town and onward international flight home. Your elite holiday designed by TRAGUIN concludes seamlessly. Transfers: Private Airport Chauffeur Drop'
                ),
                [
                    'Sightseeing Included: Sunrise Bush Safari Drive',
                    'Meals Included: Premium Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Westin Estate Kariega Lodge',
                'South Africa',
                '7N',
                'Deluxe',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — The Westin Estate Kariega Lodge',
            ),
            _hotel(
                'The Table Bay Hotel • Turbine Hotel & Spa Amakhala Woodbury Lodge',
                'Multi-city South Africa',
                '7N',
                'Premium',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — The Table Bay Hotel • Turbine Hotel & Spa Amakhala Woodbury Lodge',
            ),
            _hotel(
                'The Silo Hotel / One&Only Simola Hotel Country Club & Spa Shamwari Long Lee Manor',
                'Multi-city South Africa',
                '7N',
                'Luxury',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Silo Hotel / One&Only Simola Hotel Country Club & Spa Shamwari Long Lee Manor',
            ),
            _hotel(
                'Cape Grace Hotel Pezula Nature Retreat Shamwari - Eagles Crag Luxury Tented Lodges',
                'Multi-city South Africa',
                '7N',
                'Ultra Luxury',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Cape Grace Hotel Pezula Nature Retreat Shamwari - Eagles Crag Luxury Tented Lodges',
            )
        ],
        inclusions=[
            _inc_included('Meals: Daily gourmet breakfasts, select safari lunches, and curated multi-course dinners as highlighted in the itinerary.', 1),
            _inc_included('Transfers: Private Chauffeur-driven luxury Mercedes van / SUV airport and regional transfers throughout South Africa.', 2),
            _inc_included('Safari Drives: Two exclusive 4x4 open-top game drives inside the private reserve with professional trackers.', 3),
            _inc_included('Sightseeing: All premium admissions including skip-the-line Table Mountain tickets, Cape Point funicular, Boulders Beach, Knysna Lagoon luxury cruise, and Cango Caves entry.', 4),
            _inc_excluded('International and domestic internal flight tickets', 5),
            _inc_excluded('South African Tourist Visa fees and processing charges', 6),
            _inc_excluded('Personal expenses such as laundry, premium liquors, telephone calls, and driver/ranger gratuities', 7),
            _inc_excluded('Optional adventure activities like shark cage diving or bungee jumping', 8),
            _inc_excluded('Travel insurance coverage (Highly recommended)', 9),
            _inc_excluded('International and domestic internal flight tickets', 10),
            _inc_excluded('South African Tourist Visa fees and processing charges', 11),
            _inc_excluded('Personal expenses such as laundry, premium liquors, telephone calls, and driver/ranger gratuities', 12),
            _inc_excluded('Optional adventure activities like shark cage diving or bungee jumping', 13),
        ],
    )
    return package, itinerary

def build_za_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ZA-002'
    tour_code = 'TRAGUIN-ZA-002-HONEYMOON'
    title = 'South Africa Honeymoon'
    duration = '07 Nights / 08 Days'
    slug = 'za-002-south-africa-honeymoon'
    itin_slug = 'za-002-south-africa-honeymoon-itinerary'
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
            _ph('Serial code ZA-002 | TRAGUIN tour code TRAGUIN-ZA-002-HONEYMOON', 1),
            _ph('Country: South Africa, Southern Africa | Category: Honeymoon / Premium Luxury Holidays DURATION: 07 Nights / 08 Days', 2),
            _ph('Destinations: Cape Town (3N) • Franschhoek Winelands (1N) • Knysna Garden Route (2N) • Luxury Safari (1N)', 3),
            _ph('Ideal for: Newlyweds, Couples Seeking Luxury, Romantic Explorers', 4),
            _ph('Best season: October to April (Warm, sunny, perfect for beaches and vineyards)', 5),
            _ph('Starting price: On Request (Strictly Bespoke Honeymoon Pricing)', 6),
            _ph('Vehicle / Meals: Modified American Plan with Private Dining upgrades (Daily Premium Breakfast & Fine-Dining Dinners)', 7)
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
        price_note='On Request (Premium South Africa Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='South Africa Honeymoon',
        overview="Romantic South Africa: Cape Town • Franschhoek • Garden Route • Ultra-Luxury Safari 07 NIGHTS / 08 DAYS EXCLUSIVE ROMANTIC EXPERIENCE Embark on an enchanting love affair with the world's most visually arresting destination. The South Africa Honeymoon Package by TRAGUIN is passionately engineered to deliver romance in its purest, most opulent form. From intimate sunset sailing in the shadow of Table Mountain to private plunge pools overlooking the pristine African bush, this Luxury South Africa Holiday merges raw adventure with high-end luxury. Trust TRAGUIN to design unforgettable memories and handpicked hotels that turn your transition into marital bliss into an absolute masterpiece.\n\nTOUR OVERVIEW\nThis premium signature itinerary reflects the highest tiers of personalized luxury, curated specifically as the definitive Best South Africa Tour Package for couples. Every element is paced dynamically to ensure privacy, romantic leisure, and fluid transfers. Benefit from private executive chauffeur service, hand-selected luxury suites with premium views, VIP honeymoon welcome amenities, and breathtaking landscapes tailored for high-end photography. Route: Cape Town (3 Nights) ➔ Franschhoek Winelands (1 Night) ➔ Knysna (2 Nights) ➔ Private Luxury Game Lodge (1 Night) Vehicle: Private Chauffeur-driven Premium Sedan / Luxury SUV Transfers Meal Plan: Modified American Plan with Private Dining upgrades (Daily Premium Breakfast & Fine-Dining Dinners) TRAGUIN Curated Experience Note: Includes private helicopter flights over Cape Peninsula, couples' side- by-side spa rituals, vintage tram journeys, and private candlelight dining under the African stars.\n\nWHY CHOOSE ROMANTIC SOUTH AFRICA FOR YOUR HONEYMOON?\nSouth Africa represents a dream world for couples, perfectly combining the cosmopolitan seaside charm of the Mediterranean with dramatic wildlife safaris. Choosing a Premium South Africa Experience with TRAGUIN sets your escape apart with unmatched luxury. Famous Attractions: Scenic helicopter tours of Cape Town, Table Mountain sunset, the romantic Cape Winelands, historical Knysna Heads, and world-class Big Five safaris. Most Searched Experiences: Sunset champagne cruises, gourmet vineyard picnics, private candlelight bush dinners, and coastal dolphin spotting. Popular Instagram Locations: The colorful streets of Bo-Kaap, the infinity pools of Franschhoek, dramatic clifftops along Chapman's Peak, and pristine beaches of Camps Bay. Luxury & Culture: Highly curated culinary arts, private artisanal tasting journeys, high-end diamond house tours, and elite wilderness lodge relaxation. YOUR BESPOKE DAY-WISE ITINERARY",
        seo_title='ZA-002 | South Africa Honeymoon | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days South Africa package (ZA-002 / TRAGUIN-ZA-002-HONEYMOON): Cape Town (3N) • Franschhoek Winelands (1N) • Knysna Garden Route (2N) • Luxury Safari (1N) with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: CAPE TOWN', 1),
            _ih('Day 02: CAPE TOWN — PRIVATE HELICOPTER FLIGHT & TABLE MOUNTAIN VIP', 2),
            _ih('Day 03: CAPE TOWN — CAPE PENINSULA ROMANTIC DRIVE & SECLUDED BEACH PICNIC', 3),
            _ih('Day 04: FRANSCHHOEK — CONNOISSEUR WINE TRAM JOURNEY & BOUTIQUE VINEYARD', 4),
            _ih('Day 05: KNYSNA — THE MAGICAL GARDEN ROUTE & EXCLUSIVE LAGOON CRUISE', 5),
            _ih('Day 06: KNYSNA — OUDTSHOORN MYSTERY CAVES & PRIVATE SPA RITUAL', 6),
            _ih('Day 07: LUXURY SAFARI LODGE — HONEYMOON SAFARI, SUNSET BIG FIVE TRACKING &', 7),
            _ih('Day 08: GQEBERHA (PORT ELIZABETH) — SUNRISE BUSH SAFARI & HOMEWARD', 8)
        ],
        days=[
            _day(
                1,
                'CAPE TOWN | ARRIVAL, PRIVATE VIP CHAUFFEUR & ROMANTIC SUNSET CRUISE',
                (
                    'Arrive in the mesmerizing city of Cape Town. Your TRAGUIN South Africa Packages voyage ignites with a VIP greeting by your private luxury chauffeur. Check into your ultra-luxury waterfront sanctuary to find chilled champagne and fresh strawberries waiting. In the late afternoon, step onto a private luxury yacht for a romantic sunset cruise across Table Bay, clinking glasses as the sun dips beneath the Atlantic horizon.'
                ),
                [
                    'Sightseeing Included: Private executive airport transfer, Premium Waterfront check-in',
                    'Evening Experience: Private Yacht Champagne Sunset Cruise',
                    'Overnight Stay: Cape Town (Premium Luxury Ocean Suite)',
                    'Meals Included: Welcome Honeymoon Dinner',
                ],
            ),
            _day(
                2,
                'CAPE TOWN — PRIVATE HELICOPTER FLIGHT & TABLE MOUNTAIN VIP',
                (
                    'EXPERIENCE Savor a lavish breakfast before soaring into the skies on an exclusive private helicopter flight over the Atlantic coastline. Touch down and head straight to Table Mountain with skip-the-line privileges for a breathtaking ride up the cableway. Spend your afternoon strolling through the romantic Kirstenbosch Botanical Gardens, walking along the canopy paths amidst exotic flora.'
                ),
                [
                    'Sightseeing Included: Private Helicopter Coastal Flight, VIP Table Mountain Cableway, Kirstenbosch',
                    'Evening Experience: Candlelight dining at an award-winning oceanfront restaurant in Camps Bay',
                    'Overnight Stay: Cape Town',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'CAPE TOWN — CAPE PENINSULA ROMANTIC DRIVE & SECLUDED BEACH PICNIC',
                (
                    'Travel along the engineering marvel of Chapman’s Peak Drive, holding hands as you navigate dramatic sea cliffs. Arrive at Cape Point Nature Reserve and take a private walk to the iconic lighthouse. Afterward, TRAGUIN arranges a highly exclusive, beautifully styled gourmet seafood picnic on a secluded white-sand beach, complete with premium local wines and private butler service.'
                ),
                [
                    'Sightseeing Included: Chapman’s Peak Drive, Cape Point, Cape of Good Hope, Boulders Beach Penguins',
                    'Evening Experience: Casual luxury lounging at the V&A Waterfront',
                    'Overnight Stay: Cape Town',
                    'Meals Included: Premium Breakfast & Luxury Beach Picnic Lunch',
                ],
            ),
            _day(
                4,
                'FRANSCHHOEK — CONNOISSEUR WINE TRAM JOURNEY & BOUTIQUE VINEYARD',
                (
                    'STAY Check out and journey into the rolling, mist-veiled valleys of Franschhoek, the culinary capital of South Africa. Board the exclusive open-top vintage Wine Tram, hopping off at historic French Huguenot estates. Indulge in private cellar master tours, fine-wine tasting masterclasses, and an exquisite farm-to-table lunch. Check into an ultra-luxury boutique vineyard villa featuring a private heated plunge pool.'
                ),
                [
                    'Sightseeing Included: Franschhoek Valley, Premium Hop-on Hop-off Wine Tram Tour',
                    'Evening Experience: Private estate dinner paired with exclusive museum-release wines',
                    'Overnight Stay: Franschhoek (Ultra-Luxury Vineyard Villa)',
                    'Meals Included: Premium Breakfast & Gourmet Vineyard Lunch',
                ],
            ),
            _day(
                5,
                'KNYSNA — THE MAGICAL GARDEN ROUTE & EXCLUSIVE LAGOON CRUISE',
                (
                    'Drive along the majestic coastal highway of the Garden Route, taking in breathtaking landscapes of pristine wilderness. Arrive at the romantic lagoon hamlet of Knysna. Board an exclusive luxury catamaran cruise through the serene lagoon waters. Sail between the colossal sandstone cliffs of the Knysna Heads into the open ocean as the sky turns a fiery pink.'
                ),
                [
                    'Sightseeing Included: Garden Route Scenic Transit, Private Knysna Heads Catamaran Cruise',
                    'Evening Experience: Oyster & Champagne tasting dinner on the water’s edge',
                    'Overnight Stay: Knysna (Premium Cliffside Luxury Suite)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                6,
                'KNYSNA — OUDTSHOORN MYSTERY CAVES & PRIVATE SPA RITUAL',
                (
                    "Embark on a private day excursion to Oudtshoorn. Explore the deep, limestone fairy world of the Cango Caves on an exclusive guided tour. Return to your premium resort in the afternoon to indulge in an immersive 90-minute side-by-side couple's massage and hydrotherapy ritual, specially curated by TRAGUIN to rejuvenate your body and soul."
                ),
                [
                    'Sightseeing Included: Cango Caves Heritage Tour, Oudtshoorn Valley Drive',
                    'Evening Experience: Relaxed, candlelit lagoon-side dinner',
                    'Overnight Stay: Knysna',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                7,
                'LUXURY SAFARI LODGE — HONEYMOON SAFARI, SUNSET BIG FIVE TRACKING &',
                (
                    'BOMA BONFIRE Depart for a world-renowned, ultra-luxury private game reserve. Check into your opulent safari suite, featuring expansive glass walls looking directly into the wild savanna. Board an exclusive 4x4 open safari vehicle for a sunset game drive. Track elephants, lions, leopards, and rhinos with your senior ranger. As night falls, indulge in a magical, candlelit boma bonfire dinner accompanied by traditional rhythms.'
                ),
                [
                    'Sightseeing Included: Sunset Big Five Safari Drive, Private Lodge High Tea',
                    'Evening Experience: Candlelit Boma Fire Dinner under the Southern Cross constellation',
                    'Overnight Stay: Eastern Cape Luxury Safari Lodge (Ultra-Luxury Suite)',
                    'Meals Included: Premium Breakfast, Lunch, & Elite Safari Dinner',
                ],
            ),
            _day(
                8,
                'GQEBERHA (PORT ELIZABETH) — SUNRISE BUSH SAFARI & HOMEWARD',
                (
                    'DEPARTURE JOURNEY Wake up to the soft calls of the African bush. Savor a final sunrise safari drive, capturing intimate, close-up photos of majestic wildlife in their natural habitat. Return to the lodge for a decadent Champagne breakfast. Your private executive vehicle then transfers you to Gqeberha (Port Elizabeth) International Airport for your connecting flight home. Your unforgettable honeymoon crafted by TRAGUIN concludes in perfection. Transfers: Private Airport Executive Chauffeur Drop'
                ),
                [
                    'Sightseeing Included: Dawn Wildlife Safari Tracking',
                    'Meals Included: Premium Breakfast / Champagne Brunch',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Westin Cape Town Le Kariega Game Reserve - Ukhozi Lounge',
                'Multi-city South Africa',
                '7N',
                'Deluxe',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — The Westin Cape Town Le Kariega Game Reserve - Ukhozi Lounge',
            ),
            _hotel(
                'The Table Bay House Turbine Hotel & Spa Amakhala Bush Lodge',
                'Multi-city South Africa',
                '7N',
                'Premium',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — The Table Bay House Turbine Hotel & Spa Amakhala Bush Lodge',
            ),
            _hotel(
                'One&Only Cape Town Mont Rochelle Simola Country Club Shamwari Private Reserve - Long Lee',
                'Multi-city South Africa',
                '7N',
                'Luxury',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — One&Only Cape Town Mont Rochelle Simola Country Club Shamwari Private Reserve - Long Lee',
            ),
            _hotel(
                'The Silo Hotel Leeu Estates Pezula Nature Retreat Shamwari - Eagles Crag',
                'Multi-city South Africa',
                '7N',
                'Ultra Luxury',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — The Silo Hotel Leeu Estates Pezula Nature Retreat Shamwari - Eagles Crag',
            )
        ],
        inclusions=[
            _inc_included('Accommodation: 7 Nights stay in ultra-luxury honeymoon suites and exclusive vineyard/safari villas', 1),
            _inc_included('Transfers: Dedicated private chauffeur service in luxury modern vehicles throughout the itinerary', 2),
            _inc_included('Flight & Sky Upgrades: 1 Exclusive Private Helicopter Flight over the Cape Peninsula', 3),
            _inc_included('Wellness: Complimentary 90-minute couples side-by-side spa therapy experience', 4),
            _inc_included('TRAGUIN Concierge: 24/7 priority concierge backing from our premier holiday managers', 5),
            _inc_excluded('International and domestic airfare tickets', 6),
            _inc_excluded('Australian/South African visa fees and handling costs', 7),
            _inc_excluded('Personal incidental expenses (mini-bar purchases, telephone, laundry, tips)', 8),
            _inc_excluded('Optional extreme activities like skydiving or cage diving', 9),
        ],
    )
    return package, itinerary

def build_za_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ZA-003'
    tour_code = 'TRAGUIN-ZA-003-FAMILY'
    title = 'Cape Town Safari Family Tour'
    duration = '08 Nights / 09 Days'
    slug = 'za-003-cape-town-safari-family-tour'
    itin_slug = 'za-003-cape-town-safari-itinerary'
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
            _ph('Serial code ZA-003 | TRAGUIN tour code TRAGUIN-ZA-003-FAMILY', 1),
            _ph('Country: South Africa, Southern Africa | Category: Family / Premium Luxury Holidays DURATION: 08 Nights / 09 Days', 2),
            _ph('Destinations: Cape Town (5N) • Shamwari Private Game Reserve (3N)', 3),
            _ph('Ideal for: Premium Families, Multi-Generational Groups, Wildlife Lovers', 4),
            _ph('Best season: Year-Round (October to April for pleasant coastlines; May to September for prime Safari tracking)', 5),
            _ph('Starting price: On Request (Premium Multi-Day Curated Pricing)', 6),
            _ph('Vehicle / Meals: Modified American Plan in Cape Town; All-Inclusive Premium Full Board at Safari Lodge', 7)
        ],
        moods=['Family', 'Luxury', 'Honeymoon'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium South Africa Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Cape Town Safari Family Tour',
        overview="Cape Town & Luxury Safari Deep Dive: Fully Curated Family Expedition 08 NIGHTS / 09 DAYS PREMIUM FAMILY EXPERIENCE Welcome to an immersive family journey engineered to combine rich cosmopolitan relaxation with breathtaking wildlife experiences. The Best South Africa Tour Package by TRAGUIN provides a sophisticated, unhurried exploration focusing deeply on Cape Town's iconic landmarks and the premier, malaria-free wilderness of the Eastern Cape. This Luxury South Africa Holiday is custom-designed for premium families who wish to balance deep cultural exploration with an intense, multi-day Big Five safari adventure. Rely on TRAGUIN to coordinate handpicked hotels, seamless flights, and exclusive activities that promise unforgettable memories for your loved ones.\n\nTOUR OVERVIEW\nThis strictly private itinerary serves as an elite benchmark among TRAGUIN South Africa Packages. By focusing beautifully on two premier hubs—Cape Town and an ultra-luxury Private Game Reserve—we eliminate unnecessary travel fatigue, making it perfect for children and elderly travelers alike. Benefit from private, dedicated luxury vehicle logistics, a comprehensive premium meal plan catering to diverse culinary choices, and high-end tracking safaris supervised by Africa's top qualified game rangers. Route: Cape Town (5 Nights) ➔ Private Luxury Game Reserve (3 Nights) Vehicle: Private Chauffeur-driven Premium Multi-Seater Luxury Coach / SUV Transfers Meal Plan: Modified American Plan in Cape Town; All-Inclusive Premium Full Board at Safari Lodge TRAGUIN Curated Experience Note: Includes private cable car skip-the-line privileges, a personalized marine wildlife ocean safari, behind-the-scenes cheetah rehabilitation center access, and private family bush dinners.\n\nWHY CHOOSE CAPE TOWN & SAFARI FOR YOUR FAMILY VACATIONS?\nA flawless combination of dramatic urban oceanscapes and pristine wilderness makes this route an absolute favorite for elite global travelers. Choosing a Premium South Africa Experience with TRAGUIN adds a touch of pure exclusivity to your family holiday. Famous Attractions: Table Mountain Aerial Cableway, Cape Point Nature Reserve, Boulders Beach Penguin Sanctuary, Two Oceans Aquarium, and the iconic Big Five wildlife corridors. Most Searched Experiences: Standing at the edge of the Cape Peninsula, tracking leopards at dusk, private vineyard family picnics, and luxury helicopter harbor flights. Popular Instagram Locations: The neon-hued walls of Bo-Kaap, panoramic vistas from Mrs. Macquarie-style Signal Hill, Chapman’s Peak seaside loops, and sunset bush platforms. Family & Shopping: Hand-crafted gold jewelry, premium wildlife souvenirs at the V&A Watershed, interactive science hubs for children, and premium multi-generational dining. YOUR BESPOKE DAY-WISE ITINERARY",
        seo_title='ZA-003 | Cape Town Safari Family Tour | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days South Africa package (ZA-003 / TRAGUIN-ZA-003-FAMILY): Cape Town (5N) • Shamwari Private Game Reserve (3N) with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: CAPE TOWN — EXCLUSIVELY CURATED ARRIVAL & WATERFRONT EXPLORATION', 1),
            _ih('Day 02: CAPE TOWN — TABLE MOUNTAIN VIP ENTRY & HISTORIC CITY CULTURE', 2),
            _ih('Day 03: CAPE TOWN — PRIVATE PENINSULA SAFARI & BOULDERS BEACH PENGUINS', 3),
            _ih('Day 04: CAPE TOWN — MARINE WILDLIFE OCEAN CRUISE & ROBBEN ISLAND HISTORY', 4),
            _ih('Day 05: CAPE TOWN — WINELANDS ESTATE PICNIC & KIRSTENBOSCH CANOPY WALK', 5),
            _ih('Day 06: LUXURY SAFARI LODGE — TRANSIT TO THE EASTERN CAPE & SUNSET BIG FIVE', 6),
            _ih('Day 07: LUXURY SAFARI LODGE — DAWN SAFARI & CHEETAH REHABILITATION CENTRE', 7),
            _ih('Day 08: LUXURY SAFARI LODGE — EXPEDITION BUSH WALK & PRIVATE SUNSET GALA', 8)
        ],
        days=[
            _day(
                1,
                'CAPE TOWN — EXCLUSIVELY CURATED ARRIVAL & WATERFRONT EXPLORATION',
                (
                    'Land at Cape Town International Airport, where your family is warmly greeted by our private luxury chauffeur. Relax in comfort as you are transferred directly to your handpicked premium hotel at the secure Victoria & Alfred Waterfront. After check-in, spend a relaxed afternoon strolling around the historic docks, visiting high- end craft markets, or viewing marine life at the Two Oceans Aquarium. In the evening, gather for an exceptional welcome dinner curated by TRAGUIN specialists.'
                ),
                [
                    'Sightseeing Included: Private executive airport transfer, V&A Waterfront family walk',
                    'Evening Experience: Harborfront Premium Seafood Welcome Dinner',
                    'Overnight Stay: Cape Town (Handpicked Premium Luxury Hotel)',
                    'Meals Included: Welcome Dinner',
                ],
            ),
            _day(
                2,
                'CAPE TOWN — TABLE MOUNTAIN VIP ENTRY & HISTORIC CITY CULTURE',
                (
                    'Savor a gourmet breakfast before ascending Table Mountain via its famous revolving aerial cableway, using our pre-arranged skip-the-line VIP passes to enjoy breathtaking landscapes without the wait. Descend to explore the historic city center, walking through the beautifully preserved, brightly painted homes of Bo-Kaap. After an incredible local lunch, take a leisurely stroll through the Company’s Garden and enjoy an elite family sunset viewing at Signal Hill.'
                ),
                [
                    'Sightseeing Included: Table Mountain VIP Cableway, Bo-Kaap Tour, Company’s Garden, Signal Hill Sunset',
                    'Evening Experience: Authentic Cape Malay fine-dining experience',
                    'Overnight Stay: Cape Town',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'CAPE TOWN — PRIVATE PENINSULA SAFARI & BOULDERS BEACH PENGUINS',
                (
                    "Embark on an iconic coastal road trip down Chapman’s Peak Drive, universally hailed as one of the world's most spectacular scenic routes. Travel into the Cape Point Nature Reserve, riding the Flying Dutchman Funicular up to the ancient lighthouse to gaze out where two ocean currents meet. On your loop back, stop for an immersive experience at Boulders Beach to stand within arm's reach of South Africa's world-famous African Penguin colony—an absolute delight for children. Penguins"
                ),
                [
                    'Sightseeing Included: Chapman’s Peak Drive, Cape Point Funicular, Cape of Good Hope, Boulders Beach',
                    'Optional Activities: High-speed private boat ride to Hout Bay Seal Island',
                    'Overnight Stay: Cape Town',
                    'Meals Included: Premium Breakfast & Gourmet Seafood Lunch',
                ],
            ),
            _day(
                4,
                'CAPE TOWN — MARINE WILDLIFE OCEAN CRUISE & ROBBEN ISLAND HISTORY',
                (
                    'Today features an incredible marine safari. Board our pre-booked premium catamaran for an ocean cruise around Table Bay, spotting playful fur seals, heavy sunfish, and breaching whales (seasonal). In the afternoon, take an emotional, deeply moving guided historical cruise to Robben Island, exploring the prison quarters led by an actual former political prisoner—a powerful cultural experience for the whole family.'
                ),
                [
                    'Sightseeing Included: Marine Wildlife Catamaran Cruise, Robben Island Guided Museum Tour',
                    'Evening Experience: Relaxed family leisure strolling at Camps Bay beach promenade',
                    'Overnight Stay: Cape Town',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'CAPE TOWN — WINELANDS ESTATE PICNIC & KIRSTENBOSCH CANOPY WALK',
                (
                    "Escape to the nearby Constantia Valley, South Africa's oldest wine-growing estate hub. While adults indulge in premium wine-tasting masterclasses in historic cellars, children are treated to fresh table-grape juice artisanal pairings. Enjoy a high-end gourmet picnic lunch under centuries-old oak trees. In the afternoon, wander the sky-high 'Boomslang' canopy walkway at Kirstenbosch National Botanical Gardens, offering unparalleled views of the mountain slopes."
                ),
                [
                    'Sightseeing Included: Constantia Historic Estate Tour, Constantia Gourmet Picnic, Kirstenbosch Canopy Walk',
                    'Evening Experience: High-end contemporary dining at the waterfront',
                    'Overnight Stay: Cape Town',
                    'Meals Included: Premium Breakfast & Estate Picnic Lunch',
                ],
            ),
            _day(
                6,
                'LUXURY SAFARI LODGE — TRANSIT TO THE EASTERN CAPE & SUNSET BIG FIVE',
                (
                    'SAFARI Fly from Cape Town to Gqeberha (Port Elizabeth). Your private TRAGUIN luxury safari coach awaits to transfer you to an opulent, malaria-free private game reserve. Check into your premium family villa, complete with a private viewing deck overlooking a high-traffic waterhole. After a decadent high tea, climb into an open- top luxury 4x4 vehicle for your inaugural sunset game drive, tracking elephants, rhinos, and lions under a blazing African sky.'
                ),
                [
                    'Sightseeing Included: Private Reserve Check-in, Sunset 4x4 Big Five Safari Tracking',
                    'Evening Experience: Traditional multi-course gourmet Boma dinner around a roaring wood fire',
                    'Overnight Stay: Eastern Cape Luxury Safari Lodge (Premium Family Suite)',
                    'Meals Included: Premium Breakfast, High Tea, & Luxury Safari Dinner',
                ],
            ),
            _day(
                7,
                'LUXURY SAFARI LODGE — DAWN SAFARI & CHEETAH REHABILITATION CENTRE',
                (
                    "INSIGHT Set out at dawn as the wild plains come alive with activity. Your expert tracker interprets fresh footprints to guide you to active predator prides. Return to the lodge for a magnificent brunch. In the afternoon, enjoy an exclusive, behind-the-scenes educational tour of the reserve's world-renowned wildlife rehabilitation center, learning closely about cheetah and rhino conservation—an educational milestone for young travelers."
                ),
                [
                    'Sightseeing Included: Sunrise Bush Safari, Wildlife Rehabilitation Center VIP Tour',
                    'Evening Experience: Guided night-sky stargazing and constellation storytelling session',
                    'Overnight Stay: Luxury Safari Lodge',
                    'Meals Included: Premium Full Board (Breakfast, Lunch, High Tea, Dinner)',
                ],
            ),
            _day(
                8,
                'LUXURY SAFARI LODGE — EXPEDITION BUSH WALK & PRIVATE SUNSET GALA',
                (
                    'CHAMPAGNE DRIVE After a morning safari drive and breakfast, embark on a secure, low-impact guided bush walk with an armed ranger, exploring the fascinating micro-ecosystems, medicinal plants, and birdlife of the savanna. Re- energize with an elite lunch by the lodge pool. In the late afternoon, set out for your final signature sunset safari drive, pausing on a high plateau for premium drinks and snacks surrounded by untamed wilderness.'
                ),
                [
                    'Sightseeing Included: Dawn Safari Tracking, Guided Ranger Bush Walk, Sundowner Ridge Experience',
                    'Evening Experience: Private Family Farewell Gala Dinner hosted inside a secluded bush clearing',
                    'Overnight Stay: Luxury Safari Lodge',
                    'Meals Included: Premium Full Board (Gourmet Breakfast, Bush Lunch, Farewell Dinner)',
                ],
            ),
            _day(
                9,
                'GQEBERHA (PORT ELIZABETH) — MORNING SAFARI RITUAL & HOMEWARD',
                (
                    'DEPARTURE LOGISTICS Embrace your final sunrise safari drive, capturing memorable close-up photographs of majestic giraffes and zebra herds grazing in the morning mist. Return for a celebratory luxury breakfast. Pack your bags and bid farewell to the lodge rangers as your private executive chauffeur drives you smoothly to Chief Dawid Stuurman International Airport in Gqeberha for your connecting flight home. Your unmatched luxury vacation planned by TRAGUIN concludes in seamless perfection. Transfers: Private Airport Executive Coach Drop'
                ),
                [
                    'Sightseeing Included: Sunrise Safari Tracking Ritual',
                    'Meals Included: Premium Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Westin Interconnecting Rooms) Kariega',
                'South Africa',
                '8N',
                'Deluxe',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — The Westin Interconnecting Rooms) Kariega',
            ),
            _hotel(
                'The Table Bay Hotel Amakhala Lodge',
                'South Africa',
                '8N',
                'Premium',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — The Table Bay Hotel Amakhala Lodge',
            ),
            _hotel(
                'One&Only Marina Suite) Shamwari Lee Manor',
                'South Africa',
                '8N',
                'Luxury',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — One&Only Marina Suite) Shamwari Lee Manor',
            ),
            _hotel(
                'The Silo Hotel Shamwari - Riverdene Family Luxury',
                'Multi-city South Africa',
                '8N',
                'Ultra Luxury',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — The Silo Hotel Shamwari - Riverdene Family Luxury',
            )
        ],
        inclusions=[
            _inc_included('Transfers: Dedicated private chauffeur-driven luxury family coach or premium SUV throughout the trip', 1),
            _inc_included('Wildlife Safaris: 6 Exclusive 4x4 open safari vehicle tracking game drives led by qualified senior rangers', 2),
            _inc_included('TRAGUIN Concierge: 24/7 priority concierge backing from our premier holiday managers', 3),
            _inc_included('Transfers: Dedicated private chauffeur-driven luxury family coach or premium SUV throughout the trip', 4),
            _inc_included('Wildlife Safaris: 6 Exclusive 4x4 open safari vehicle tracking game drives led by qualified senior rangers', 5),
            _inc_excluded('International and domestic internal airfare flight tickets', 6),
            _inc_excluded('South African visa processing fees and handling documentation charges', 7),
            _inc_excluded('Personal incidental expenses (laundry, long-distance telephone, tips, extra spa sessions)', 8),
            _inc_excluded('Optional extreme adrenaline sports like shark cage diving or skydiving', 9),
        ],
    )
    return package, itinerary

def build_za_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ZA-004'
    tour_code = 'TRAGUIN-ZA-004-PREMIUM'
    title = 'Cape Town & Safari Premium Tour'
    duration = '08 Nights / 09 Days'
    slug = 'za-004-cape-town-safari-premium-tour'
    itin_slug = 'za-004-cape-town-safari-premium-itinerary'
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
            _ph('Serial code ZA-004 | TRAGUIN tour code TRAGUIN-ZA-004-PREMIUM', 1),
            _ph('Country: South Africa, Southern Africa | Category: Premium Family Tour & Luxury Safari DURATION: 08 Nights / 09 Days', 2),
            _ph('Destinations: Cape Town • Private Game Reserve Safari IDEAL FOR: Families • Honeymooners • Luxury Seekers', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Daily Premium Breakfast in Cape Town; Ultra All-Inclusive (All Gourmet Meals, Premium Drinks & High Teas) at the Safari Game Lodge Route: Cape Town International Airport → Cape Town Atlantic Seaboard', 7),
            _ph('TRAGUIN Signature Experience: Private champagne/sparkling juice toast at sunset on the peaks of', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked family-friendly travel timing and routes optimized to', 9),
            _ph('Premium Handpicked Hotels: Elite properties featuring direct security access, exceptional central', 10),
            _ph('Personalized Assistance: Directly connected to an executive destination manager from TRAGUIN', 11)
        ],
        moods=['Family', 'Luxury', 'Safari'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium South Africa Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Cape Town & Safari Premium Tour',
        overview='CAPE TOWN • LUXURY PRIVATE GAME RESERVE SAFARI • 08 NIGHTS / 09 DAYS Welcome to an extraordinary journey through the jewel of the African continent. This ultra-luxury, custom- crafted Best South Africa Tour Package offers an immersive escape into world-class sophistication and untamed wilderness. From the iconic silhouette of Table Mountain to the thrilling, heart-pounding encounters of a private luxury safari, every single detail has been meticulously planned by TRAGUIN travel specialists. Witness the dramatic meeting of two oceans, indulge in world-renowned culinary masterworks, and let the rhythmic pulse of Africa create lifelong bonds for your family. This is not just a holiday; it is a signature collection of curated experiences designed to stay in your heart forever, ensuring unforgettable memories for years to come.\n\nTOUR OVERVIEW\nDiscover the pinnacle of bespoke travel with this elite Luxury South Africa Holiday meticulously designed by TRAGUIN. Seamlessly blending the vibrant, cosmopolitan energy of Cape Town with the raw, exhilarating majesty of a premier Big Five private game reserve, this itinerary is optimized for families and couples seeking absolute comfort, safety, and exclusivity. Travel Dates: Flexible / Custom FIT Group / FIT: Fully Independent Customized Family Tour Vehicle: Private Luxury Chauffeur-driven SUV / Sprinter for all ground transfers Meal Plan: Daily Premium Breakfast in Cape Town; Ultra All-Inclusive (All Gourmet Meals, Premium Drinks & High Teas) at the Safari Game Lodge Route: Cape Town International Airport → Cape Town Atlantic Seaboard → Cape Peninsula → Stellenbosch Winelands → Private Luxury Game Reserve Safari → Departure TRAGUIN Curated Experience Note: Enjoy 24/7 VIP concierge assistance from TRAGUIN, priority skip- the-line ticketing at major iconic attractions, handpicked premium stays, and private expert field guides for an elite, immersive wildlife adventure.\n\nWhy Visit Destination: Unmatched juxtaposition of modern luxury living and ancient, raw wilderness.\nFamous Attractions: Table Mountain, Boulders Beach Penguin Colony, Chapman’s Peak Drive, and Cape Point. Most Searched Experiences: Tracking the legendary Big Five in an open-top 4x4 vehicle with professional naturalists. Best Honeymoon/Family/Luxury Points: Private candlelit boma dining under a canopy of stars and ultra- private pool villas. Popular Instagram Locations: Pastel houses of Bo-Kaap, dramatic cliffs of Cape Point, and beachfront views of Camps Bay. Adventure / Shopping / Culture Highlights: Elite boutique shopping at the V&A Waterfront, local historical walking tours, and artisanal wine pairings. YOUR BESPOKE DAY-WISE ITINERARY',
        seo_title='ZA-004 | Cape Town & Safari Premium Tour | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days South Africa package (ZA-004 / TRAGUIN-ZA-004-PREMIUM): Cape Town • Private Game Reserve Safari IDEAL FOR: Families •  Honeymooners •  Luxury Seekers with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: WELCOME TO CAPE TOWN – ARRIVAL IN THE MOTHER CITY', 1),
            _ih('Day 02: TABLE MOUNTAIN ASCENT & HISTORIC BO-KAAP CULTURAL IMMERSION', 2),
            _ih("Day 03: CAPE PENINSULA TOUR – CHAPMAN'S PEAK & BOULDERS BEACH PENGUINS", 3),
            _ih('Day 04: STELLENBOSCH WINELANDS & GOURMET FRANSCHHOEK VALLEY', 4),
            _ih('Day 05: CAPE TOWN TO PRIVATE LUXURY SAFARI RESERVE – THE WILDERNESS AWAITS', 5),
            _ih('Day 06: UNTRACKED WILDERNESS – DAWN & DUSK BIG FIVE GAME DRIVES', 6),
            _ih('Day 07: MASTERING THE BUSH – ECO-AWARENESS & EXCLUSIVE LUXURY SAFARI', 7),
            _ih('Day 08: FINAL GAME DRIVE & TRANSITION BACK TO URBAN GLAMOUR', 8),
            _ih('TRAGUIN Signature Experience: Private champagne/sparkling juice toast at sunset on the peaks of', 9),
            _ih('Curated by TRAGUIN Experts: Handpicked family-friendly travel timing and routes optimized to', 10)
        ],
        days=[
            _day(
                1,
                'WELCOME TO CAPE TOWN – ARRIVAL IN THE MOTHER CITY',
                (
                    'Your extraordinary luxury journey begins the moment your flight touches down at Cape Town International Airport. As you step into the arrival hall, a dedicated TRAGUIN private chauffeur will warmly welcome your family with customized amenities, assisting with your luggage into your premium luxury vehicle. Enjoy a highly scenic route along the sparkling Atlantic Seaboard as you transition toward your handpicked elite hotel. The afternoon is yours to unwind from your travels. Take in the breathtaking landscapes of the majestic mountains framing the urban skyline. In the evening, take a relaxed stroll through the vibrant V&A Waterfront, an iconic attraction offering an electric atmosphere, live music, and deep historical charm. Dine at one of our highly recommended harborside fine-dining restaurants, sampling fresh seafood while watching the harbor lights dance on the water.'
                ),
                [
                    'Sightseeing Included: Scenic orientation drive of the Atlantic Seaboard, V&A Waterfront evening exploration.',
                    'Optional Activities: Sunset catamaran cruise from the harbor.',
                    'Evening Experience: Harbor-view luxury dinner at leisure with panoramic views of Table Mountain.',
                    'Overnight Stay: Handpicked Hotel / Resort, Cape Town.',
                    'Meals Included: Welcome Drinks.',
                ],
            ),
            _day(
                2,
                'TABLE MOUNTAIN ASCENT & HISTORIC BO-KAAP CULTURAL IMMERSION',
                (
                    'Awaken to a delicious artisan breakfast before embarking on a premier Cape Town Sightseeing tour. Today you ascend the legendary Table Mountain, one of the official New Seven Wonders of Nature. With your priority skip-the-line access tickets courtesy of TRAGUIN, step into the state-of-the-art revolving cable car, offering unmatched 360-degree vistas of the sparkling city, vast ocean, and rugged coastline. At the summit, wander along pristine pathways and absorb the truly breathtaking landscapes that make this location a global icon. Descend the mountain to delve deep into the rich cultural tapestry of Cape Town. Visit the historic, brightly painted quarter of Bo-Kaap, a top Instagram location famous for its bright pastel-hued facades and deep Cape Malay heritage. Walk along the historic cobblestone streets, learn about the local community, and discover authentic spice shops. Spend your afternoon exploring the lush, expansive paths of Kirstenbosch National Botanical Garden, nested against the eastern slopes of the mountain. Botanical Gardens.'
                ),
                [
                    'Sightseeing Included: Table Mountain Cableway (weather permitting), Bo-Kaap Historical Quarter, Kirstenbosch',
                    'Photography Points: Table Mountain Summit, Pastel Streets of Bo-Kaap, Kirstenbosch Canopy Walkway.',
                    'Evening Experience: Dinner at a premium fine dining restaurant specializing in contemporary South African cuisine.',
                    'Overnight Stay: Handpicked Hotel / Resort, Cape Town.',
                    'Meals Included: Premium Breakfast.',
                ],
            ),
            _day(
                3,
                "CAPE PENINSULA TOUR – CHAPMAN'S PEAK & BOULDERS BEACH PENGUINS",
                (
                    "Prepare for an awe-inspiring day dedicated to coastal splendor on this ultimate Cape Peninsula circuit. Your private guide will navigate along the spectacular marine drive toward Hout Bay, where an optional private boat trip takes you to Duiker Island to view thousands of wild fur seals in their natural habitat. Next, experience the scenic beauty of Chapman's Peak Drive, widely revered as one of the most magnificent marine touring roads on earth, carved directly into towering ocean cliffs. Continue your journey to the Cape of Good Hope Reserve. Stand at Cape Point, the dramatic southwesternmost tip of Africa, where rugged cliffs plunge vertically into roaring ocean waves. Take the Flying Dutchman funicular to the historic lighthouse for expansive maritime views. Afterward, travel to the world- famous Boulders Beach in Simon’s Town. This unique sanctuary allows your family an immersive experience walking alongside a wild colony of rare African Penguins as they waddle across pristine white sands. Penguin Colony."
                ),
                [
                    "Sightseeing Included: Chapman's Peak Scenic Drive, Cape of Good Hope, Cape Point Funicular, Boulders Beach",
                    "Optional Activities: Hout Bay Seal Island Cruise, ocean-facing coastal seafood lunch in Simon's Town.",
                    'Evening Experience: Relaxed family leisure evening back at the hotel beach promenade.',
                    'Overnight Stay: Handpicked Hotel / Resort, Cape Town.',
                    'Meals Included: Premium Breakfast.',
                ],
            ),
            _day(
                4,
                'STELLENBOSCH WINELANDS & GOURMET FRANSCHHOEK VALLEY',
                (
                    'Indulge your senses today within the rolling, emerald valleys of the Cape Winelands, located just an hour outside the city. This region is a paradise of grand historic Cape Dutch estates, majestic mountain backdrops, and world-class culinary art. Visit the historic town of Stellenbosch, walking beneath avenues of ancient oak trees lined with boutique galleries and historical architecture. Your family will experience an exclusive experience featuring handpicked non-alcoholic artisanal pairings for children and premium, award-winning vintage tastings for adults. Travel onward to the picturesque Franschhoek Valley, recognized as the culinary capital of South Africa. Board the famous open-air Franschhoek Wine Tram for a nostalgic, scenic journey winding through historic vineyards. It is a delightful, sensory-rich day of absolute relaxation, pristine scenic beauty, and unhurried luxury. Exclusive Experiences: Private wine tasting, custom estate lunch reservation, specialized grape juice pairing for kids.'
                ),
                [
                    'Sightseeing Included: Stellenbosch Heritage Walk, Franschhoek Valley, Franschhoek Wine Tram Ride.',
                    'Overnight Stay: Handpicked Hotel / Resort, Cape Town.',
                    'Meals Included: Premium Breakfast.',
                ],
            ),
            _day(
                5,
                'CAPE TOWN TO PRIVATE LUXURY SAFARI RESERVE – THE WILDERNESS AWAITS',
                (
                    'Bid a fond farewell to the coast as your private chauffeur transfers you back to Cape Town Airport for your short flight or luxury transfer to an elite, malaria-free Private Game Reserve. Upon arriving at your ultra-luxury safari lodge, step out into an oasis of pure African opulence. You will be welcomed with chilled refreshments and a decadent lunch overlooking a bustling watering hole where elephants frequently gather. After a refined high tea, climb aboard a customized, open-top 4x4 safari vehicle for your first thrilling afternoon game drive. Guided by an expert ranger and a master native tracker, venture deep into the pristine bush. As dusk falls over the savannah, stop at a scenic viewpoint for traditional sundowner drinks, watching a magnificent African sunset paint the sky in fiery orange and deep violet. Continue tracking nocturnal wildlife by powerful spotlight before returning to the lodge for an extravagant gourmet dinner around an open fire boma under a blanket of brilliant stars. Arrival Experience: VIP welcome drinks, personalized lodge orientation, luxury bush suite check-in.'
                ),
                [
                    'Sightseeing Included: Premium Afternoon/Evening 4x4 Open-Vehicle Guided Game Drive, Wilderness Sundowner.',
                    'Overnight Stay: Ultra-Luxury Safari Lodge (Private Game Reserve).',
                    'Meals Included: Breakfast, Luxury Lunch, Evening High Tea & Five-Star Boma Dinner.',
                ],
            ),
            _day(
                6,
                'UNTRACKED WILDERNESS – DAWN & DUSK BIG FIVE GAME DRIVES',
                (
                    "Your day begins with a gentle sunrise wake-up call. Enjoy freshly brewed coffee and artisanal biscuits before setting off into the cool dawn air. This is prime time for observing majestic predators—lions, leopards, and cheetahs—as they wrap up their nightly hunts. Watch families of elephants move gracefully through the brush and observe majestic rhinos grazing in the early light. Your elite tracker will read subtle signs in the earth, tracking animals off-road to give your family unmatched close-up views. Return to the lodge for a sumptuous late breakfast, followed by hours of pure relaxation. Unwind on your private deck, swim in the rim-flow infinity pool, or indulge in a world-class holistic African spa treatment. Late afternoon brings another luxurious high tea and your evening game drive. Every single drive is completely unique, offering new opportunities to witness rare wildlife behavior. Return to a candlelit dinner, sharing incredible stories of the day's sightings. Immersive Experiences: Close-up tracking of the legendary Big Five, stargazing with astronomers under African skies."
                ),
                [
                    'Sightseeing Included: Sunrise 4x4 Game Drive, Sunset 4x4 Game Drive, Guided Bush Walk (optional).',
                    'Overnight Stay: Ultra-Luxury Safari Lodge (Private Game Reserve).',
                    'Meals Included: All Inclusive (Full Board: Breakfast, Lunch, High Tea, Dinner & Premium Beverages).',
                ],
            ),
            _day(
                7,
                'MASTERING THE BUSH – ECO-AWARENESS & EXCLUSIVE LUXURY SAFARI',
                (
                    'Embrace the timeless rhythm of the wild. Today, alongside your standard spectacular game drives, your children can participate in an exclusive junior tracker program, learning how to identify animal footprints, bird calls, and medicinal plants from native trackers. Adults can embark on an exhilarating guided bush walking safari, stepping directly onto the ancient earth to experience the smaller wonders of the ecosystem safely on foot with armed rangers. In the afternoon, enjoy a uniquely crafted private bush picnic dinner or a beautifully arranged deck lunch. As the sun sets on your final full day in the wild, toast to the beautiful landscapes and the magnificent creatures that call this paradise home. The night concludes with premium vintage African wines around the roaring fireplace, surrounded by the peaceful, distant calls of the wild night.'
                ),
                [
                    'Sightseeing Included: Morning Game Drive, Evening Game Drive, Interactive Junior Ranger Tracker Activity.',
                    'Photography Points: Watering Hole Wildlife Gatherings, Wide-Angle African Bush Sunsets.',
                    'Overnight Stay: Ultra-Luxury Safari Lodge (Private Game Reserve).',
                    'Meals Included: All Inclusive (Full Board: Breakfast, Lunch, High Tea, Dinner & Premium Beverages).',
                ],
            ),
            _day(
                8,
                'FINAL GAME DRIVE & TRANSITION BACK TO URBAN GLAMOUR',
                (
                    "Savor your final morning game drive in the African bush, capturing last-minute photographs of magnificent giraffe silhouettes and playful baboon troops. Return for a celebratory breakfast before bidding a warm farewell to your lodge family. Your private luxury vehicle will be waiting to transfer you safely to the airport for your brief flight back to Cape Town or Johannesburg for your final evening of relaxation. Check back into a premium luxury hotel for your final night. Spend the evening picking up exquisite, premium souvenirs or enjoying a spectacular farewell dinner at an award-winning restaurant, reflecting on the profound, magical moments your family shared across South Africa's stunning cities and untamed wildlands."
                ),
                [
                    'Sightseeing Included: Final Sunrise Tracking Session, Premium Airport Inter-City Transfers.',
                    'Evening Experience: Farewell Elite Dinner Reservation at a critically acclaimed restaurant.',
                    'Overnight Stay: Handpicked Hotel, Cape Town or Johannesburg.',
                    'Meals Included: Premium Breakfast.',
                ],
            ),
            _day(
                9,
                'DEPARTURE – CHERISHING UNFORGETTABLE MEMORIES',
                (
                    'Your ultimate premium vacation concludes today. Enjoy a relaxed morning breakfast at your hotel, taking in your final views of the beautiful landscapes. Depending on your flight schedule, your private vehicle will arrive to transport your family smoothly and comfortably to the international airport for your homeward journey. You depart with cameras filled with stunning photographs and hearts full of unforgettable memories from an elite African journey orchestrated flawlessly by travel experts.'
                ),
                [
                    'Transfers Included: Private Luxury Chauffeur Transfer to the International Airport.',
                    'Meals Included: Premium Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Commodore Hotel / Radisson Blu Waterfront Kariega Game Reserve – Main',
                'Multi-city South Africa',
                '8N',
                'Deluxe',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — The Commodore Hotel / Radisson Blu Waterfront Kariega Game Reserve – Main',
            ),
            _hotel(
                'The Westin Cape Town / Pepperclub Amakhala Game Reserve – Quartermains Bespoke Safari Tented Suite',
                'Multi-city South Africa',
                '8N',
                'Premium',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — The Westin Cape Town / Pepperclub Amakhala Game Reserve – Quartermains Bespoke Safari Tented Suite',
            ),
            _hotel(
                'The Table Bay Hotel / Taj Cape Town Shamwari Private Game Reserve – Long Lee Manor',
                'Multi-city South Africa',
                '8N',
                'Luxury',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Table Bay Hotel / Taj Cape Town Shamwari Private Game Reserve – Long Lee Manor',
            ),
            _hotel(
                'The Silo Hotel / One&Only Cape Town Sabi Sabi Earth Lodge / Singita Ebony Lodge Private Plunge Pool Luxury Villa',
                'Multi-city South Africa',
                '8N',
                'Ultra Luxury',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — The Silo Hotel / One&Only Cape Town Sabi Sabi Earth Lodge / Singita Ebony Lodge Private Plunge Pool Luxury Villa',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Cape Town, Garden Route, and safari lodges', 1),
            _inc_included('Private chauffeur-driven luxury SUV/Sprinter transfers throughout South Africa', 2),
            _inc_included('Curated Big Five safari game drives with professional rangers as per itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and South African visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_za_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ZA-005'
    tour_code = 'TRAGUIN-ZA-005-GRAND'
    title = 'Grand South Africa Tour'
    duration = '10 Nights / 11 Days'
    slug = 'za-005-grand-south-africa-tour'
    itin_slug = 'za-005-grand-south-africa-itinerary'
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
            _ph('Serial code ZA-005 | TRAGUIN tour code TRAGUIN-ZA-005-GRAND', 1),
            _ph('Country: South Africa, Southern Africa | Category: Premium Grand Vacation & Wilderness Exploration DURATION: 10 Nights / 11 Days', 2),
            _ph('Destinations: Cape Town • Oudtshoorn • Knysna (Garden Route) • Private Safari Reserve', 3),
            _ph('Ideal for: Premium Families, High- End FIT Travelers, Luxury Vacationers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Premium Breakfast Daily across city/coastal hotels; Ultra Full Board (All Gourmet Meals, High Teas, and Selection of Fine Wines) during your Luxury Safari Lodge stay. Route: Cape Town → Cape Peninsula', 7),
            _ph('TRAGUIN Signature Experience: Private champagne/sparkling juice toast at sunset on the peaks of', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked family-friendly travel timing and routes optimized to', 9),
            _ph('Premium Handpicked Hotels: Elite properties featuring direct security access, exceptional central', 10),
            _ph('Personalized Assistance: Directly connected to an executive destination manager from TRAGUIN', 11)
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
        price_note='On Request (Premium South Africa Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Grand South Africa Tour',
        overview='CAPE TOWN • SCENIC GARDEN ROUTE • OUDTSHOORN • BIG 5 LUXURY SAFARI • 10N / 11D Welcome to the ultimate exploration of the southern tip of the African continent. This ultra-exclusive, meticulously designed Best South Africa Tour Package offers a sweeping travel experience spanning dramatic oceanscapes, majestic semi-desert valleys, mystical coastal lagoons, and premier untamed big- game territory. Crafted lovingly by TRAGUIN travel specialists, this South Africa Family Tour framework bridges legendary urban landscapes with pristine nature. Whether you are traveling as an absolute luxury seeker or celebrating a milestone on a South Africa Honeymoon Package, this comprehensive expedition promises an collection of curated experiences, premium stays, and unforgettable memories tailored uniquely to you.\n\nTOUR OVERVIEW\nEmbark on the definitive Luxury South Africa Holiday arranged by TRAGUIN. This comprehensive itinerary seamlessly unites the globally celebrated cosmopolitan marvel of Cape Town, the geological wonders of the Klein Karoo semi-desert, the enchanting marine coastal forests of Knysna along the famous Garden Route, and an elite, private safari immersion. Travel Framework: Premium Private FIT (Fully Independent Customized Journey). Luxury Vehicle: Chauffeur-driven executive luxury Mercedes-Benz Sprinter / Luxury SUV throughout all sectors. Meal Plan: Premium Breakfast Daily across city/coastal hotels; Ultra Full Board (All Gourmet Meals, High Teas, and Selection of Fine Wines) during your Luxury Safari Lodge stay. Route: Cape Town → Cape Peninsula → Stellenbosch Winelands → Route 62 → Oudtshoorn → Knysna → George Airport → Eastern Cape Luxury Game Reserve → Departure. TRAGUIN Curated Experience Note: Includes absolute priority skip-the-line ticketing at major world attractions, private expert destination drivers, premium room layout upgrades, and 24/7 dedicated local operations desk backing.\n\nWHY VISIT DESTINATION: PREMIUM SOUTH AFRICA INSIGHTS\nExploring the Top Tourist Places in South Africa requires a sophisticated route mapping that captures the true essence of its diverse geography. Knowing the Best Time to Visit South Africa ensures magnificent weather patterns, pristine coastal clarity, and peak wildlife viewing. Famous Attractions: Table Mountain Cableway, Cango Caves, Knysna Heads, and Boulders Beach African Penguin Colony. Most Searched Experiences: Walking inside ancient subterranean limestone formations, cruising scenic ocean lagoons at sunset, and tracking lions and leopards off-road in open-top 4x4 vehicles. Popular Instagram Locations: Chapman’s Peak cliffside overlooks, the wooden boardwalks of Knysna Waterfront, and early morning wilderness sunrise frames. Culture & Gastronomy: Private estate wine-tastings, authentic Cape Malay dining, and five-star outdoor bush boma braais under southern constellations. YOUR COMPREHENSIVE DAY-WISE ITINERARY',
        seo_title='ZA-005 | Grand South Africa Tour | TRAGUIN',
        seo_description='Premium 10 Nights / 11 Days South Africa package (ZA-005 / TRAGUIN-ZA-005-GRAND): Cape Town • Oudtshoorn • Knysna (Garden Route) • Private Safari Reserve with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: WELCOME TO CAPE TOWN – ARRIVAL & V&A WATERFRONT EXPLORATION', 1),
            _ih('Day 02: TABLE MOUNTAIN CABLEWAY & BO-KAAP COLONIAL HERITAGE', 2),
            _ih('Day 03: CAPE PENINSULA EXPEDITION – CHAPMAN’S PEAK & BOULDERS BEACH PENGUINS', 3),
            _ih('Day 04: STELLENBOSCH CULINARY ESTATES & FRANSCHHOEK TRAM', 4),
            _ih('Day 05: CAPE TOWN TO OUDTSHOORN VIA ROUTE 62 – THE SEMI-DESERT WONDERS', 5),
            _ih('Day 06: CANGO CAVES GEOLOGICAL WONDERS TO SCENIC KNYSNA LAGOON', 6),
            _ih('Day 07: EXPLORING THE GARDEN ROUTE – TSITSIKAMMA NATIONAL PARK RAINFORESTS', 7),
            _ih('Day 08: KNYSNA TO PRIVATE SAFARI RESERVE – WELCOME TO THE WILDERNESS', 8),
            _ih('TRAGUIN Signature Experience: Private champagne/sparkling juice toast at sunset on the peaks of', 9),
            _ih('Curated by TRAGUIN Experts: Handpicked family-friendly travel timing and routes optimized to', 10)
        ],
        days=[
            _day(
                1,
                'WELCOME TO CAPE TOWN – ARRIVAL & V&A WATERFRONT EXPLORATION',
                (
                    'Your grand tour begins with your arrival at Cape Town International Airport. A TRAGUIN private luxury vehicle and executive chauffeur will receive your family, loading your luggage comfortably. Embark on a spectacular coastal orientation drive along the Atlantic Seaboard towards your premium city hotel. Spend the afternoon relaxing at your premium hotel property. In the evening, explore the historic V&A Waterfront, an iconic attraction rich with shopping boutiques, lively local music, and outstanding maritime views. Dine at one of our premium recommended dockside establishments.'
                ),
                [
                    'Sightseeing Included: Atlantic Seaboard scenic orientation drive, V&A Waterfront evening walking loop.',
                    'Overnight Stay: Handpicked Premium Hotel / Resort, Cape Town.',
                    'Meals Included: Welcome Amenities.',
                ],
            ),
            _day(
                2,
                'TABLE MOUNTAIN CABLEWAY & BO-KAAP COLONIAL HERITAGE',
                (
                    "Enjoy a luxurious artisan breakfast before setting out on your premium Cape Town Sightseeing circuit. Ascend Table Mountain using pre-booked priority skip-the-line tickets provided by TRAGUIN. Ride the revolving cable car to experience stunning 360-degree vistas of the city bowl and the ocean below. Descend the mountain to walk the cobblestone alleyways of Bo-Kaap, capturing beautiful family photographs against the iconic pastel-colored houses. Spend your afternoon wandering through the majestic tree canopies of Kirstenbosch National Botanical Garden, crossing the famous 'Boomslang' aerial walkway."
                ),
                [
                    'Sightseeing Included: Table Mountain Cableway, Bo-Kaap Historic Quarter, Kirstenbosch Botanical Gardens.',
                    'Photography Points: Table Mountain Summit, Pastel Frontages of Bo-Kaap, Tree Canopy Walkway.',
                    'Overnight Stay: Handpicked Premium Hotel / Resort, Cape Town.',
                    'Meals Included: Premium Breakfast.',
                ],
            ),
            _day(
                3,
                'CAPE PENINSULA EXPEDITION – CHAPMAN’S PEAK & BOULDERS BEACH PENGUINS',
                (
                    'Dedicate today to exploring the stunning Cape Peninsula. Travel via Hout Bay along the cliffside engineering marvel of Chapman’s Peak Drive, absorbing the incredible scenic beauty of ocean waves crashing hundreds of feet below. Proceed to the Cape of Good Hope, taking the Flying Dutchman funicular to the Cape Point lighthouse overlook. In the afternoon, visit the world-renowned Boulders Beach to experience an immersive experience standing alongside rare, wild African Penguins. Travel back through Simon’s Town historic naval port to wrap up a truly iconic coastal touring day. Penguin Colony.'
                ),
                [
                    'Sightseeing Included: Chapman’s Peak Drive, Cape of Good Hope Reserve, Cape Point Funicular, Boulders Beach',
                    'Optional Activities: Duiker Island seal spotting cruise from Hout Bay.',
                    'Overnight Stay: Handpicked Premium Hotel / Resort, Cape Town.',
                    'Meals Included: Premium Breakfast.',
                ],
            ),
            _day(
                4,
                'STELLENBOSCH CULINARY ESTATES & FRANSCHHOEK TRAM',
                (
                    'Journey today into the elegant Cape Winelands. Explore the historic heritage streets of Stellenbosch, appreciating its stately oak avenues and Cape Dutch architecture. Indulge in an exclusive experience featuring private estate cellar tours with artisanal juice pairings for younger guests and curated vintage selections for adults. Travel onwards to Franschhoek Valley, boarding the delightful open-air Franschhoek Wine Tram for a memorable journey winding through gorgeous vineyard backdrops and spectacular mountain valleys. Ride.'
                ),
                [
                    'Sightseeing Included: Stellenbosch Historic Walking Tour, Franschhoek Mountain Valley, Franschhoek Wine Tram',
                    'Overnight Stay: Handpicked Premium Hotel / Resort, Cape Town.',
                    'Meals Included: Premium Breakfast & Private Estate Tastings.',
                ],
            ),
            _day(
                5,
                'CAPE TOWN TO OUDTSHOORN VIA ROUTE 62 – THE SEMI-DESERT WONDERS',
                (
                    'Depart Cape Town this morning, traveling inland along the famous Route 62, celebrated as one of the most beautiful road-trip routes in the country. Watch the lush coastal scenery shift into the rugged, beautiful plains of the semi-desert Klein Karoo valley. Arrive in Oudtshoorn, the ostrich capital of the world. In the afternoon, visit a premier ostrich farm for an entertaining and educational tour. Check into your luxury country lodge and savor an authentic Karoo dinner under the vast desert sky.'
                ),
                [
                    'Sightseeing Included: Route 62 Scenic Driving Corridor, Oudtshoorn High-End Ostrich Farm Tour.',
                    'Evening Experience: Traditional multi-course Karoo farm-to-table dinner at your lodge.',
                    'Overnight Stay: Luxury Country Lodge / Boutique Estate, Oudtshoorn.',
                    'Meals Included: Premium Breakfast & Fine Dining Dinner.',
                ],
            ),
            _day(
                6,
                'CANGO CAVES GEOLOGICAL WONDERS TO SCENIC KNYSNA LAGOON',
                (
                    'Begin your morning exploring the ancient Cango Caves, a spectacular underground network of towering limestone caverns. Accompanied by an expert local guide, walk through massive chambers adorned with ancient stalactites and stalagmites formed over millions of years. Afterwards, your private vehicle will cross the breathtaking Outeniqua Mountain Pass, returning to the lush coast to join the legendary Garden Route. Arrive at the picturesque town of Knysna, nestled alongside a stunning marine lagoon. Relax with a premium sunset cruise out to the famous Knysna Heads cliffs where the lagoon meets the Indian Ocean.'
                ),
                [
                    'Sightseeing Included: Cango Caves Heritage Guided Walk, Outeniqua Pass Drive, Knysna Lagoon Sunset Cruise.',
                    'Overnight Stay: Handpicked Premium Waterfront Hotel, Knysna.',
                    'Meals Included: Premium Breakfast.',
                ],
            ),
            _day(
                7,
                'EXPLORING THE GARDEN ROUTE – TSITSIKAMMA NATIONAL PARK RAINFORESTS',
                (
                    'Embark on a spectacular day trip along the Garden Route toward Tsitiskamma National Park. Walk along the dramatic suspension bridges spanning the wild Storms River Mouth, where the river meets powerful ocean swells. Stroll through serene indigenous yellowwood forests, soaking in the pristine air and incredible coastal views. On your return, visit the coastal town of Plettenberg Bay to walk its white-sand beaches, before returning to Knysna Waterfront for an evening of fresh local oysters and fine dining.'
                ),
                [
                    'Sightseeing Included: Tsitsikamma Suspension Bridges, Storms River Gorge, Plettenberg Bay Beach stop.',
                    'Optional Activities: Bloukrans Bridge view point stop, local elephant sanctuary interaction.',
                    'Overnight Stay: Handpicked Premium Waterfront Hotel, Knysna.',
                    'Meals Included: Premium Breakfast.',
                ],
            ),
            _day(
                8,
                'KNYSNA TO PRIVATE SAFARI RESERVE – WELCOME TO THE WILDERNESS',
                (
                    'Bid farewell to the Garden Route as your private chauffeur transfers you to George Airport for a short domestic connection, or drive onward directly into an elite Private Game Reserve in the Eastern Cape. Check into your ultra-luxury safari lodge and unwind with chilled drinks while looking out over the African bushveld. Following a premium afternoon high tea, climb into an open-top 4x4 safari vehicle for your first thrilling evening game drive with your expert ranger and tracker, looking for the legendary Big Five. Enjoy sundowner drinks as the sun sets over the wilderness, before returning to the lodge for a magnificent boma dinner.'
                ),
                [
                    'Sightseeing Included: Evening Open-Top 4x4 Big Five Guided Tracking Session, Wilderness Sundowner.',
                    'Overnight Stay: Ultra-Luxury Safari Lodge (Private Game Reserve).',
                    'Meals Included: Premium Breakfast, Lodge Lunch, Afternoon High Tea & Five-Star Boma Dinner.',
                ],
            ),
            _day(
                9,
                'UNTAMED WILDERNESS – DAWN & DUSK BIG FIVE GAME TRACKING',
                (
                    'Wake to a gentle dawn call and enjoy hot coffee before heading out into the crisp morning air. This is the absolute best time to catch large predators active at the end of their night hunt. Watch elephant families move past and view lions and rhinos grazing in the early light. Return to the lodge for a grand breakfast, followed by a relaxing afternoon. Unwind on your private deck, swim in the infinity pool, or indulge in a signature African spa treatment. Head out again in the late afternoon for another unique game drive, wrapping up the night with a spectacular dinner around the open fire.'
                ),
                [
                    'Sightseeing Included: Sunrise 4x4 Game Drive, Sunset 4x4 Game Drive, Guided Bush Walk (optional).',
                    'Overnight Stay: Ultra-Luxury Safari Lodge (Private Game Reserve).',
                    'Meals Included: All Inclusive (Full Board: Breakfast, Lunch, High Tea, Dinner & Selected Beverages).',
                ],
            ),
            _day(
                10,
                'DEEP BUSH IMMERSION & CELEBRATORY SUNSET SAFARI',
                (
                    "Savor another beautiful day in the wild. Alongside your morning and evening game drives, adults can participate in an exciting guided walking safari to learn about tracking and the bush ecosystem up close. Younger guests can enjoy interactive conservation activities with native trackers. Celebrate your final evening in the African wilderness with a private bush picnic dinner or sunset cocktails, toast to the beautiful landscapes and incredible wildlife memories you've shared."
                ),
                [
                    'Sightseeing Included: Morning Game Drive, Evening Game Drive, Interactive Bush Craft Tracker Session.',
                    'Overnight Stay: Ultra-Luxury Safari Lodge (Private Game Reserve).',
                    'Meals Included: All Inclusive (Full Board: Breakfast, Lunch, High Tea, Dinner & Selected Beverages).',
                ],
            ),
            _day(
                11,
                'FINAL SAFARI DRIVE & HOMEWARD DEPARTURE',
                (
                    'Enjoy a final morning game drive, capturing your last photos of giraffes and wildlife against the sunrise. Return to the lodge for a celebratory breakfast before bidding farewell to your lodge hosts. Your TRAGUIN private luxury vehicle will transfer your family smoothly to the airport for your flight home, concluding an incredible Grand South Africa experience.'
                ),
                [
                    'Transfers Included: Private Luxury Chauffeur Airport Transfer.',
                    'Meals Included: Premium Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Commodore Buffelsdrift Game Lodge / Knysna Log-Inn Kariega Game Reserve – Main Lodge',
                'Multi-city South Africa',
                '10N',
                'Deluxe',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — The Commodore Buffelsdrift Game Lodge / Knysna Log-Inn Kariega Game Reserve – Main Lodge',
            ),
            _hotel(
                'The Westin Cape Town Executive Club Suite Rosenhof Boutique Manor / Turbine Hotel Amakhala Game Reserve – Bush Lodge Bespoke Safari Tent',
                'Multi-city South Africa',
                '10N',
                'Premium',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — The Westin Cape Town Executive Club Suite Rosenhof Boutique Manor / Turbine Hotel Amakhala Game Reserve – Bush Lodge Bes',
            ),
            _hotel(
                'Taj Cape Town Table Mountain Suite De Zeekoe Guest Farm / Simola Golf Resort Shamwari Private Reserve – Long Lee Manor',
                'Multi-city South Africa',
                '10N',
                'Luxury',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Taj Cape Town Table Mountain Suite De Zeekoe Guest Farm / Simola Golf Resort Shamwari Private Reserve – Long Lee Manor',
            ),
            _hotel(
                'One&Only Cape Town Suite Alkantmooi Resort / Pezula Nature Retreat Sabi Sabi Earth Lodge / Singita Ebony Private Pool Villa',
                'Multi-city South Africa',
                '10N',
                'Ultra Luxury',
                'Deluxe Room / Suite',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — One&Only Cape Town Suite Alkantmooi Resort / Pezula Nature Retreat Sabi Sabi Earth Lodge / Singita Ebony Private Pool Vi',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Cape Town, Garden Route, and safari lodges', 1),
            _inc_included('Private chauffeur-driven luxury SUV/Sprinter transfers throughout South Africa', 2),
            _inc_included('Curated Big Five safari game drives with professional rangers as per itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('PACKAGE INCLUSIONS', 5),
        ],
    )
    return package, itinerary

SOUTH_AFRICA_ZA_001_005_BUILDERS = [
    build_za_001,
    build_za_002,
    build_za_003,
    build_za_004,
    build_za_005,
]
