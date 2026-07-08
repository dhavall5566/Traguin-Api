"""Builder functions for AU-005 Australia international domestic packages."""

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

AUSTRALIA_SLUG = "australia"


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


def build_au_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AU-005'
    tour_code = 'TRAGUIN-AU-005-PREMIUM'
    title = 'Grand Australia Discovery: Melbourne • Cairns • Gold Coast • Sydney'
    duration = '10 Nights / 11 Days'
    slug = 'au-005-grand-australia-discovery-melbourne-cairns-gold-coast-sydney'
    itin_slug = 'au-005-grand-australia-discovery-melbourne-cairns-gold-coast-sydney-itinerary'
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
            _ph('Serial code AU-005 | TRAGUIN tour code TRAGUIN-AU-005-PREMIUM', 1),
            _ph('State / Country: Australia | Category: Premium / Luxury Holidays DURATION: 10 Nights / 11 Days', 2),
            _ph('Destinations: Melbourne (3N) • Cairns & Great Barrier Reef (2N) • Gold Coast (2N) • Sydney (3N)', 3),
            _ph('Ideal for: Premium Families, Luxury Leisure Seekers, Honeymooners', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / MAPAI', 7)
        ],
        moods=['Luxury', 'Honeymoon', 'Beach'],
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
        tagline='Grand Australia Discovery: Melbourne',
        overview='Grand Australia Discovery: Melbourne • Cairns • Gold Coast • Sydney 10 NIGHTS / 11 DAYS PREMIUM EXPERIENCE Welcome to a journey crafted exclusively for discerning travelers who demand nothing short of perfection. The Best Australia Tour Package by TRAGUIN unlocks the timeless, sun-drenched landscapes and sophisticated coastal charm of the Southern Hemisphere. From the vibrant laneways of Melbourne to the breathtaking landscapes of the Great Barrier Reef, this Luxury Australia Holiday promises an immersive blend of high-octane adventure and relaxed luxury. Trust TRAGUIN to design unforgettable memories tailored perfectly for your next elite getaway.\n\nTOUR OVERVIEW\nThis strictly bespoke, high-end itinerary represents the pinnacle of TRAGUIN Australia Packages. Designed for a premium FIT (Fully Independent Traveler) or family group looking for seamless connectivity, handpicked hotels, and curated experiences, this operational blueprint ensures zero stress. Enjoy private luxury airport transfers, a comprehensive premium meal plan featuring dynamic local dining options, and an expertly paced route designed by top destination specialists. Route: Melbourne (3 Nights) ➔ Cairns / Great Barrier Reef (2 Nights) ➔ Gold Coast (2 Nights) ➔ Sydney (3 Nights) Vehicle: Private Chauffeur-driven Premium SUV / Luxury Coach Transfers Meal Plan: European Plan / Modified American Plan (Daily Premium Breakfast & Gourmet Dinners) TRAGUIN Curated Experience Note: Includes private yacht charters, exclusive helicopter flight upgrades over the reef, and VIP backstage access to iconic landmarks.\n\nWHY CHOOSE A PREMIUM AUSTRALIA EXPERIENCE?\nAustralia is an ultimate bucket-list destination packed with world-famous attractions and some of the most popular Instagram locations globally. Choosing a Premium Australia Experience through TRAGUIN means trading crowded tourist buses for exclusive, high-end memories. Famous Attractions: The Sydney Opera House, the majestic Great Barrier Reef, the Twelve Apostles on the Great Ocean Road, and Warner Bros. Movie World. Most Searched Experiences: Hot air ballooning at dawn, private wine-tasting masterclasses in Yarra Valley, and sleeping over the Great Barrier Reef. Best Honeymoon / Family Points: Golden beaches of Surfers Paradise provide multi-generational fun, while private dining over Sydney Harbour offers unparalleled romance. Culture & Shopping: Explore the chic boutiques of Melbourne’s Collins Street, high-end retail at Sydney’s Queen Victoria Building, and Indigenous immersive experiences. YOUR BESPOKE DAY-WISE ITINERARY',
        seo_title='AU-005 | Grand Australia Discovery: Melbourne | TRAGUIN',
        seo_description='Premium 10 Nights / 11 Days Australia package (AU-005 / TRAGUIN-AU-005-PREMIUM): Melbourne (3N) • Cairns & Great Barrier Reef (2N) • Gold Coast (2N) • Sydney (3N) with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: MELBOURNE — ARRIVE IN THE CULTURAL CAPITAL & LUXURY WELCOME', 1),
            _ih('Day 02: MELBOURNE — THE GREAT OCEAN ROAD SPECTACULAR DRIVE', 2),
            _ih('Day 03: MELBOURNE — YARRA VALLEY WINE MASTERCLASS & PUFFING BILLY', 3),
            _ih('Day 04: CAIRNS — FLY TO TROPICAL NORTH QUEENSLAND', 4),
            _ih('Day 05: CAIRNS — IMMERSIVE GREAT BARRIER REEF LUXURY CRUISE', 5),
            _ih('Day 06: GOLD COAST — TRANSIT TO THE SUNSHINE PARADISE', 6),
            _ih('Day 07: GOLD COAST — WARNER BROS. MOVIE WORLD VIP ADVENTURE', 7),
            _ih('Day 08: SYDNEY — ARRIVE IN THE ICONIC HARBOUR CITY', 8)
        ],
        days=[
            _day(
                1,
                'MELBOURNE — ARRIVE IN THE CULTURAL CAPITAL & LUXURY WELCOME',
                (
                    'Touchdown in the cultural heart of the country. Your premium Australia Sightseeing voyage commences with a smooth VIP airport pick-up, transferring you directly to your handpicked hotel. Spend your afternoon unwinding or walking down the famous street-art-filled graffiti lanes. As evening falls, settle in for a curated welcome dinner overlooking the Yarra River.'
                ),
                [
                    'Sightseeing Included: Private City orientation, Street Art Laneways',
                    'Evening Experience: Riverside Fine Dining Welcome Experience',
                    'Overnight Stay: Melbourne (Premium Luxury Stay)',
                    'Meals Included: Welcome Dinner',
                ],
            ),
            _day(
                2,
                'MELBOURNE — THE GREAT OCEAN ROAD SPECTACULAR DRIVE',
                (
                    "Prepare for one of the world's most spectacular coastal drives. Your private vehicle guides you through breathtaking landscapes, winding along the rugged southern coast. Arrive at the iconic Twelve Apostles and Loch Ard Gorge. Witness towering limestone stacks rising from the Southern Ocean—a true photographer's paradise and a highlight of this Australia Family Tour."
                ),
                [
                    'Sightseeing Included: Full-Day Great Ocean Road, Twelve Apostles, Apollo Bay',
                    'Optional Activities: Scenic Helicopter Flight over the Apostles',
                    'Overnight Stay: Melbourne',
                    'Meals Included: Breakfast & Gourmet Lunch',
                ],
            ),
            _day(
                3,
                'MELBOURNE — YARRA VALLEY WINE MASTERCLASS & PUFFING BILLY',
                (
                    'Step back in time aboard the historic Puffing Billy steam train through the lush Dandenong Ranges. Afterward, journey into the elegant Yarra Valley for an exclusive premium wine-tasting experience and private lunch at a world-renowned estate. This curated experience balances natural scenic beauty with unmatched culinary indulgence.'
                ),
                [
                    'Sightseeing Included: Puffing Billy Steam Train, Yarra Valley Estate Tour',
                    'Evening Experience: Premium Local Cafe Hopping in Melbourne Labyrinths',
                    'Overnight Stay: Melbourne',
                    'Meals Included: Breakfast & Vineyard Lunch',
                ],
            ),
            _day(
                4,
                'CAIRNS — FLY TO TROPICAL NORTH QUEENSLAND',
                (
                    'Bid farewell to Melbourne as your private luxury transfer drives you to the airport for your flight to tropical Cairns. Welcome to the gateway of the Great Barrier Reef. Upon landing, check into your ultra-luxury resort and absorb the soothing tropical climate. Spend your evening strolling down the lively Cairns Esplanade.'
                ),
                [
                    'Sightseeing Included: Cairns Esplanade exploration',
                    'Evening Experience: Oceanfront Premium Seafood Dining Experience',
                    'Overnight Stay: Cairns (Handpicked Premium Resort)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'CAIRNS — IMMERSIVE GREAT BARRIER REEF LUXURY CRUISE',
                (
                    'Today features the centerpiece of your Luxury Australia Holiday. Board a premium, high-speed luxury catamaran heading out to an exclusive outer reef platform. Indulge in an immersive experience snorkeling alongside exotic marine life, or view the vibrant corals via a semi-submersible observatory. This is an absolute top-searched experience that defines a true premium vacation.'
                ),
                [
                    'Sightseeing Included: Outer Barrier Reef Premium Cruise, Marine Biologist Presentation',
                    'Optional Activities: Certified Scuba Diving, Sea Trek Helmet Walk',
                    'Overnight Stay: Cairns',
                    'Meals Included: Breakfast & Tropical Buffet Lunch',
                ],
            ),
            _day(
                6,
                'GOLD COAST — TRANSIT TO THE SUNSHINE PARADISE',
                (
                    'Fly south to Brisbane or Gold Coast airport. Your private vehicle whisks you away to Surfers Paradise, renowned for its sweeping beaches and endless golden horizons. The Gold Coast is globally recognized as an iconic landmark for luxury entertainment and pristine coastline, ideal for creating unforgettable memories with your loved ones.'
                ),
                [
                    'Sightseeing Included: Surfers Paradise Beach walk, SkyPoint Observation Deck Access',
                    'Evening Experience: High-end dining at Broadbeach Marina',
                    'Overnight Stay: Gold Coast',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                7,
                'GOLD COAST — WARNER BROS. MOVIE WORLD VIP ADVENTURE',
                (
                    'Experience Hollywood on the Gold Coast with premium admission tickets to Warner Bros. Movie World. Perfect for families, this day offers world-class rollercoasters, movie character meet-and-greets, and spectacular stunt shows. It stands out as one of the top tourist places in Australia for premium multi- generational fun.'
                ),
                [
                    'Sightseeing Included: Full Day Warner Bros. Movie World Admission Ticket',
                    'Evening Experience: Luxury Marina Mirage shopping & relaxation',
                    'Overnight Stay: Gold Coast',
                    'Meals Included: Breakfast',
                ],
            ),
            _day(
                8,
                'SYDNEY — ARRIVE IN THE ICONIC HARBOUR CITY',
                (
                    'Fly to Sydney, the crown jewel of Australia. Check into your opulent hotel overlooking the glittering harbor. In the late afternoon, enjoy a private curated tour of the historic Rocks district, tracing the birth of modern Sydney before enjoying a relaxing evening under the stars.'
                ),
                [
                    'Sightseeing Included: Historic Rocks Walking Tour, Darling Harbour Orientation',
                    'Evening Experience: Premium Harbourfront Lounging and Dining',
                    'Overnight Stay: Sydney (Premium Luxury Stay)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                9,
                'SYDNEY | CITY SIGHTSEEING, OPERA HOUSE VIP ACCESS & SHOWBOAT CRUISE',
                (
                    'Discover the finest landmarks of Sydney. Cross the Harbour Bridge, feel the sand at Bondi Beach, and capture breathtaking landscapes from Mrs. Macquarie’s Chair. Enjoy an exclusive inside-guided VIP tour of the magnificent Sydney Opera House. Cap off the night aboard an elegant Sydney Showboat Dinner Cruise with premier cabaret entertainment.'
                ),
                [
                    'Sightseeing Included: Bondi Beach Coastal Visit, Opera House Guided Tour, Sydney Showboat Dinner Cruise',
                    'Optional Activities: Sydney Harbour BridgeClimb Experience',
                    'Overnight Stay: Sydney',
                    'Meals Included: Breakfast & Deluxe Cruise Dinner',
                ],
            ),
            _day(
                10,
                'SYDNEY — BLUE MOUNTAINS WILDLIFE & SCENIC WORLD DISCOVERY',
                (
                    'Head inland towards the dramatic Blue Mountains National Park. Watch the mystical blue haze hovering over deep valleys from Echo Point, looking across at the iconic Three Sisters rock formation. Experience the thrilling Scenic World cableway and railway rides before visiting a premier wildlife park to meet koalas and kangaroos up close.'
                ),
                [
                    'Sightseeing Included: Blue Mountains Eco Point, Scenic World Cable Rides, Featherdale Wildlife Park',
                    'Evening Experience: Farewell Gala Dinner hosted at an award-winning restaurant',
                    'Overnight Stay: Sydney',
                    'Meals Included: Breakfast & Farewell Dinner',
                ],
            ),
            _day(
                11,
                'SYDNEY — DEPARTURE WITH UNFORGETTABLE MEMORIES',
                (
                    'Savor your final premium breakfast in Sydney. Take advantage of last-minute luxury shopping opportunities at the Queen Victoria Building before your private chauffeur transfers you seamlessly to Sydney International Airport for your homeward bound flight. Your unforgettable journey planned by TRAGUIN concludes here. Transfers: Private International Airport Chauffeur Drop'
                ),
                [
                    'Sightseeing Included: Luxury Shopping at QVB (Self-Paced)',
                    'Meals Included: Premium Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Pan Pacific Melbourne | Hilton Cairns | Vibe Hotel Gold Coast | Hyatt Regency Sydney',
                'Melbourne | Cairns | Gold Coast | Sydney',
                '10N multi-city',
                'Deluxe',
                'Premium Room',
                'Daily Premium Breakfast & Gourmet Dinner',
                4,
                1,
                description='OPTION 01 – DELUXE: Pan Pacific Melbourne | Hilton Cairns | Vibe Hotel Gold Coast | Hyatt Regency Sydney',
            ),
            _hotel(
                'The Langham Melbourne | Pullman Reef Hotel Casino | Hilton Surfers Paradise | InterContinental Sydney',
                'Melbourne | Cairns | Gold Coast | Sydney',
                '10N multi-city',
                'Premium',
                'Premium Room',
                'Daily Premium Breakfast & Gourmet Dinner',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Langham Melbourne | Pullman Reef Hotel Casino | Hilton Surfers Paradise | InterContinental Sydney',
            ),
            _hotel(
                'Crown Towers Melbourne | Shangri-La The Marina | The Star Grand Gold Coast | Sofitel Sydney Darling Harbour',
                'Melbourne | Cairns | Gold Coast | Sydney',
                '10N multi-city',
                'Luxury',
                'Premium Room',
                'Daily Premium Breakfast & Gourmet Dinner',
                4,
                3,
                description='OPTION 03 – LUXURY: Crown Towers Melbourne | Shangri-La The Marina | The Star Grand Gold Coast | Sofitel Sydney Darling Harbour',
            ),
            _hotel(
                'The Ritz-Carlton Melbourne | Crystalbrook Riley Luxury Resort | The Langham Gold Coast | Park Hyatt Sydney (Opera View)',
                'Melbourne | Cairns | Gold Coast | Sydney',
                '10N multi-city',
                'Ultra Luxury',
                'Premium Room',
                'Daily Premium Breakfast & Gourmet Dinner',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Ritz-Carlton Melbourne | Crystalbrook Riley Luxury Resort | The Langham Gold Coast | Park Hyatt Sydney (Opera View)',
            )
        ],
        inclusions=[
            _inc_included('Accommodation: 10 Nights stay in handpicked premium hotels based on your chosen tier', 1),
            _inc_included('Meals: Daily gourmet buffet breakfasts and curated multi-course dinners as highlighted in the itinerary', 2),
            _inc_included('Transfers: Private Chauffeur-driven luxury airport and inter-city transfers throughout the trip', 3),
            _inc_included('Sightseeing: Great Ocean Road, Great Barrier Reef Cruise, Warner Bros. Movie World, VIP Opera House Tour, and Sydney Showboat Cruise', 4),
            _inc_included('Welcome Amenities: Personalized luxury travel kits, local SIM cards, and signature welcome gifts upon arrival', 5),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest relations concierge assistance from our local expert team', 6),
            _inc_excluded('International and domestic internal flight tickets (Can be added on actual cost basis)', 7),
            _inc_excluded('Australian Tourist Visa fees and processing charges', 8),
            _inc_excluded('Personal expenses such as laundry, mini-bar, telephone calls, and tips', 9),
            _inc_excluded('Optional adventure activities like skydiving, bridge climbs, or helicopter flights', 10),
            _inc_excluded('Travel insurance coverage (Highly recommended)', 11),
        ],
    )
    return package, itinerary

AU_005_BUILDERS = [
    build_au_005,
]
