"""Builder functions for SG-001 through SG-015 Singapore international packages."""

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

SINGAPORE_SLUG = "singapore"


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


def build_sg_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SG-001'
    tour_code = 'TRG-SIN-HIG-2026'
    title = 'Singapore Highlights Family Tour'
    duration = '03 Nights / 04 Days'
    slug = 'sg-001-singapore-highlights-family-tour'
    itin_slug = 'sg-001-singapore-highlights-itinerary'
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
            _ph('Serial code SG-001 | TRAGUIN tour code TRG-SIN-HIG-2026', 1),
            _ph('Country: Singapore, Asia | Category: Best Singapore Family Tour Package', 2),
            _ph('Destinations: Marina Bay Sands • Gardens by the Bay • Sentosa Island • Night Safari', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Family', 'Luxury', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Singapore Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Singapore Highlights Family Tour',
        overview="Marina Bay Sands • Gardens by the Bay • Sentosa Island • Night Safari 03 Nights / 04 Days Classic Singapore Family Discovery SERIAL CODE: SG-001 TRAGUIN TOUR CODE: TRG-SIN-HIG-2026 STATE / COUNTRY: Singapore CATEGORY: Best Singapore Family Tour Package DURATION: 03 Nights / 04 Days Singapore Highlights\n\nTOUR OVERVIEW\nDive into the vibrant, futuristic city-state of Singapore with our TRAGUIN curated family holiday. Designed for a mix of high-energy exploration and iconic sightseeing, this Singapore Highlights itinerary ensures a flawless balance of fun and discovery, creating unforgettable memories in the heart of Southeast Asia's most spectacular destination. THE IMMERSIVE DAY-WISE ITINERARY",
        seo_title='SG-001 | Singapore Highlights Family Tour | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Singapore package (SG-001 / TRG-SIN-HIG-2026): Marina Bay Sands • Gardens by the Bay • Sentosa Island • Night Safari with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SINGAPORE & MARINA BAY', 1),
            _ih('Day 02: GARDENS BY THE BAY & NIGHT SAFARI', 2),
            _ih('Day 03: SENTOSA ISLAND FUN', 3),
            _ih('Day 04: DEPARTURE', 4)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SINGAPORE & MARINA BAY',
                (
                    'Arrive in Singapore. Private transfer to your handpicked premium hotel. Enjoy the evening exploring Marina Bay, witnessing the spectacular evening light and water show.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'GARDENS BY THE BAY & NIGHT SAFARI',
                (
                    'A full day exploring the futuristic Gardens by the Bay and its iconic Cloud Forest. In the evening, take an exciting exclusive experience at the Night Safari.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'SENTOSA ISLAND FUN',
                (
                    'A day of excitement at Sentosa Island. Explore Universal Studios Singapore or relax on the vibrant sandy beaches, perfect for family fun.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'DEPARTURE',
                (
                    'Final breakfast before your TRAGUIN private transfer to the airport, completing your premium Singapore experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Marina Bay Sands / Shangri-La Singapore',
                'Multi-city Singapore',
                '3N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Marina Bay Sands / Shangri-La Singapore',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Marina Bay Sands',
                '3N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: TRAGUIN Handpicked Premium Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Luxury Property',
                'Marina Bay Sands',
                '3N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Marina Bay Sands',
                '3N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Singapore', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('International and connecting flights as per curated itinerary (where applicable)', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Singapore visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_sg_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SG-002'
    tour_code = 'TRG-SIN-SEN-2026'
    title = 'Singapore & Sentosa Family Tour'
    duration = '04 Nights / 05 Days'
    slug = 'sg-002-singapore-sentosa-family-tour'
    itin_slug = 'sg-002-singapore-sentosa-itinerary'
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
            _ph('Serial code SG-002 | TRAGUIN tour code TRG-SIN-SEN-2026', 1),
            _ph('Country: Singapore, Asia | Category: Best Singapore & Sentosa Family Tour Package', 2),
            _ph('Destinations: Marina Bay Sands • Gardens by the Bay • Sentosa Island Resort • Universal Studios •', 3),
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
        price_note='On Request (Premium Singapore Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Singapore & Sentosa Family Tour',
        overview='Marina Bay Sands • Gardens by the Bay • Sentosa Island Resort • Universal Studios • Adventure Cove 04 Nights / 05 Days Exclusive Singapore & Sentosa Family Expedition SERIAL CODE: SG-002 TRAGUIN TOUR CODE: TRG-SIN-SEN-2026 STATE / COUNTRY: Singapore CATEGORY: Best Singapore & Sentosa Family Tour Package DURATION: 04 Nights / 05 Days Singapore City (2N) + Sentosa Island (2N)\n\nTOUR OVERVIEW\nDiscover the vibrant, futuristic heart of Singapore and the island excitement of Sentosa with this TRAGUIN curated family holiday. Designed for a perfect balance of high-energy exploration and luxury resort leisure, this Singapore-Sentosa Family Discovery itinerary ensures a flawless escape, creating unforgettable memories in Southeast Asia’s most spectacular destination. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='SG-002 | Singapore & Sentosa Family Tour | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Singapore package (SG-002 / TRG-SIN-SEN-2026): Marina Bay Sands • Gardens by the Bay • Sentosa Island Resort • Universal Studios • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL & MARINA BAY GLAMOUR', 1),
            _ih('Day 02: GARDENS BY THE BAY EXPLORATION', 2),
            _ih('Day 03: SENTOSA ISLAND RESORT TRANSIT', 3),
            _ih('Day 04: UNIVERSAL STUDIOS & ADVENTURE COVE', 4),
            _ih('Day 05: DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL & MARINA BAY GLAMOUR',
                (
                    'Arrive in Singapore. Private transfer to your handpicked premium city hotel. Spend the evening at Marina Bay, experiencing the iconic light show.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'GARDENS BY THE BAY EXPLORATION',
                (
                    'Explore the futuristic Gardens by the Bay, including the Cloud Forest and Flower Dome. Discover iconic attractions that define modern Singapore sightseeing.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'SENTOSA ISLAND RESORT TRANSIT',
                (
                    'Transfer to Sentosa Island. Check into an ultra-luxury family resort. Enjoy leisure time, vibrant sandy beaches, and stunning sunset views.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'UNIVERSAL STUDIOS & ADVENTURE COVE',
                (
                    'A full day of excitement at Universal Studios Singapore and Adventure Cove Waterpark. Perfect for family fun and collecting unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'DEPARTURE',
                (
                    'Final breakfast before your TRAGUIN private transfer to the airport, completing your premium Singapore- Sentosa family experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Marina Bay Sands Shangri-La Rasa Sentosa',
                'Multi-city Singapore',
                '4N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Marina Bay Sands Shangri-La Rasa Sentosa',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Marina Bay Sands',
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
                'Marina Bay Sands',
                '4N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Marina Bay Sands',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Singapore', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('International and connecting flights as per curated itinerary (where applicable)', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Singapore visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_sg_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SG-003'
    tour_code = 'TRG-SIN-USS-2026'
    title = 'Singapore Universal Studios Special'
    duration = '04 Nights / 05 Days'
    slug = 'sg-003-singapore-universal-studios-special'
    itin_slug = 'sg-003-singapore-universal-studios-itinerary'
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
            _ph('Serial code SG-003 | TRAGUIN tour code TRG-SIN-USS-2026', 1),
            _ph('Country: Singapore, Asia | Category: Best Universal Studios Family Tour Package', 2),
            _ph('Destinations: Universal Studios Singapore • Adventure Cove • S.E.A. Aquarium • Marina Bay', 3),
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
        price_note='On Request (Premium Singapore Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Singapore Universal Studios Special',
        overview='Universal Studios Singapore • Adventure Cove • S.E.A. Aquarium • Marina Bay 04 Nights / 05 Days Ultimate Singapore Theme Park Family Expedition SERIAL CODE: SG-003 TRAGUIN TOUR CODE: TRG-SIN-USS-2026 STATE / COUNTRY: Singapore CATEGORY: Best Universal Studios Family Tour Package DURATION: 04 Nights / 05 Days Singapore City & Sentosa Island\n\nTOUR OVERVIEW\nDive into the thrilling world of entertainment with our TRAGUIN curated Universal Studios Special family tour. Focused on non-stop excitement and premium theme park access, this Singapore-Sentosa Family Expedition guarantees unforgettable memories, world-class theme park experiences, and seamless family leisure. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='SG-003 | Singapore Universal Studios Special | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Singapore package (SG-003 / TRG-SIN-USS-2026): Universal Studios Singapore • Adventure Cove • S.E.A. Aquarium • Marina Bay with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SINGAPORE & CITY VISTAS', 1),
            _ih('Day 02: UNIVERSAL STUDIOS FULL-DAY IMMERSION', 2),
            _ih('Day 03: ADVENTURE COVE & S.E.A. AQUARIUM', 3),
            _ih('Day 04: SENTOSA ISLAND LEISURE & FUN', 4),
            _ih('Day 05: DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SINGAPORE & CITY VISTAS',
                (
                    'Arrive in Singapore. Private transfer to your premium family hotel. Spend the evening exploring the breathtaking Marina Bay area, enjoying the spectacular water light show.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'UNIVERSAL STUDIOS FULL-DAY IMMERSION',
                (
                    'A full day of excitement at Universal Studios Singapore. With pre-arranged priority express passes, maximize your time on all the top movie-themed thrill rides—a perfect family experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'ADVENTURE COVE & S.E.A. AQUARIUM',
                (
                    'Visit the massive S.E.A. Aquarium to witness spectacular marine life. In the afternoon, cool off at Adventure Cove Waterpark—an essential family tour highlight.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'SENTOSA ISLAND LEISURE & FUN',
                (
                    'A day of leisure on Sentosa Island. Enjoy family-friendly attractions, beach time, and a grand farewell dinner, creating unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'DEPARTURE',
                (
                    'Final breakfast before your TRAGUIN private transfer to the airport, completing your premium theme-park experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Resorts World Sentosa / Family Luxury Hotels',
                'Multi-city Singapore',
                '4N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Resorts World Sentosa / Family Luxury Hotels',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Universal Studios Singapore',
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
                'Universal Studios Singapore',
                '4N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Universal Studios Singapore',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Singapore', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('International and connecting flights as per curated itinerary (where applicable)', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Singapore visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_sg_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SG-004'
    tour_code = 'TRG-SIN-MEL-2026'
    title = 'Singapore & Melbourne Family Tour'
    duration = '07 Nights / 08 Days'
    slug = 'sg-004-singapore-melbourne-family-tour'
    itin_slug = 'sg-004-singapore-melbourne-itinerary'
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
            _ph('Serial code SG-004 | TRAGUIN tour code TRG-SIN-MEL-2026', 1),
            _ph('Country: Singapore, Asia | Category: Premium Family Tour Package', 2),
            _ph('Destinations: Marina Bay Sands • Gardens by the Bay • Melbourne Laneways • Great Ocean Road •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Family', 'Luxury', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Singapore Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Singapore & Melbourne Family Tour',
        overview='Marina Bay Sands • Gardens by the Bay • Melbourne Laneways • Great Ocean Road • Phillip Island 07 Nights / 08 Days Grand Singapore & Australia Family Expedition SERIAL CODE: SG-004 TRAGUIN TOUR CODE: TRG-SIN-MEL-2026 STATE / COUNTRY: Singapore & Australia CATEGORY: Premium Family Tour Package DURATION: 07 Nights / 08 Days Singapore (3N) + Melbourne (4N)\n\nTOUR OVERVIEW\nEmbark on a magnificent multi-country family expedition with our TRAGUIN curated Singapore & Australia explorer package. Connecting the futuristic metropolitan marvels of Singapore with the artistic culture and wild coastlines of Melbourne, this itinerary creates a harmonious blend of adventure, discovery, and unforgettable memories for your family. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='SG-004 | Singapore & Melbourne Family Tour | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Singapore package (SG-004 / TRG-SIN-MEL-2026): Marina Bay Sands • Gardens by the Bay • Melbourne Laneways • Great Ocean Road • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SINGAPORE & MARINA BAY', 1),
            _ih('Day 02: GARDENS BY THE BAY EXPLORATION', 2),
            _ih('Day 03: SINGAPORE FAMILY LEISURE', 3),
            _ih('Day 04: FLIGHT TO MELBOURNE', 4),
            _ih('Day 05: MELBOURNE LANES & ARTS', 5),
            _ih('Day 06: GREAT OCEAN ROAD EXPEDITION', 6),
            _ih('Day 07: PHILLIP ISLAND WILDLIFE GALA', 7),
            _ih('Day 08: DEPARTURE', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SINGAPORE & MARINA BAY',
                (
                    'Arrive in Singapore. Private transfer to your premium hotel. Spend the evening exploring the breathtaking Marina Bay area, enjoying the spectacular light shows.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'GARDENS BY THE BAY EXPLORATION',
                (
                    'Full day at Gardens by the Bay, discovering the Cloud Forest and Flower Dome. A top-tier family experience in Singapore.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'SINGAPORE FAMILY LEISURE',
                (
                    "A relaxing day with family-friendly activities like Sentosa Island's beaches and attractions—creating wonderful, unforgettable memories."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'FLIGHT TO MELBOURNE',
                (
                    'Private transfer to the airport for your flight to Melbourne. Check into your city-centre luxury family hotel.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'MELBOURNE LANES & ARTS',
                (
                    "Private guided walking tour through Melbourne's world-famous street-art laneways and vibrant culture centres."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'GREAT OCEAN ROAD EXPEDITION',
                (
                    'Exhilarating full-day adventure along the Great Ocean Road, witnessing the dramatic breathtaking landscapes of the Twelve Apostles.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'PHILLIP ISLAND WILDLIFE GALA',
                (
                    'Journey to Phillip Island to watch the native wildlife and the famous Penguin Parade—a highlight for the entire family.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                8,
                'DEPARTURE',
                (
                    'Final luxury breakfast before your TRAGUIN private transfer to the airport, completing your premium multi- country family expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Marina Bay Sands / Shangri-La SingaporeThe Langham Melbourne / Crown Towers',
                'Multi-city Singapore',
                '7N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Marina Bay Sands / Shangri-La SingaporeThe Langham Melbourne / Crown Towers',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Marina Bay Sands',
                '7N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: TRAGUIN Handpicked Premium Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Luxury Property',
                'Marina Bay Sands',
                '7N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Marina Bay Sands',
                '7N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Singapore', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('International and connecting flights as per curated itinerary (where applicable)', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Singapore visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_sg_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SG-005'
    tour_code = 'TRG-SIN-LUX-2026'
    title = 'Luxury Singapore Tour'
    duration = '04 Nights / 05 Days'
    slug = 'sg-005-luxury-singapore-tour'
    itin_slug = 'sg-005-luxury-singapore-itinerary'
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
            _ph('Serial code SG-005 | TRAGUIN tour code TRG-SIN-LUX-2026', 1),
            _ph('Country: Singapore, Asia | Category: Ultra-Luxury Singapore Tour Package', 2),
            _ph('Destinations: Marina Bay Sands • Private Yacht Cruise • Michelin Dining • Sentosa Luxury', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Singapore Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Luxury Singapore Tour',
        overview='04 Nights / 05 Days Ultra-Luxury Singapore Expedition SERIAL CODE: SG-005 TRAGUIN TOUR CODE: TRG-SIN-LUX-2026 STATE / COUNTRY: Singapore CATEGORY: Ultra-Luxury Singapore Tour Package DURATION: 04 Nights / 05 Days Singapore City & Sentosa Luxury\n\nTOUR OVERVIEW\nIndulge in the absolute height of sophistication with our TRAGUIN curated luxury Singapore expedition. From opulent five-star stays to private yacht excursions and world-class Michelin dining, this journey is designed for the discerning traveler, ensuring unforgettable memories in the lap of luxury. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='SG-005 | Luxury Singapore Tour | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Singapore package (SG-005 / TRG-SIN-LUX-2026): Marina Bay Sands • Private Yacht Cruise • Michelin Dining • Sentosa Luxury with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: VIP ARRIVAL & MARINA BAY LUXURY', 1),
            _ih('Day 02: GARDENS BY THE BAY & PRIVATE YACHT', 2),
            _ih('Day 03: SENTOSA ULTRA-LUXURY RETREAT', 3),
            _ih('Day 04: MICHELIN DINING & LEISURE', 4),
            _ih('Day 05: DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'VIP ARRIVAL & MARINA BAY LUXURY',
                (
                    'Arrive in Singapore. VIP airport pickup by private luxury chauffeur. Check into a world-class hotel at Marina Bay. Evening private dinner overlooking the skyline.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'GARDENS BY THE BAY & PRIVATE YACHT',
                (
                    'Exclusive tour of the futuristic Gardens by the Bay. Afternoon private yacht cruise through the Singapore harbour, a truly exclusive experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'SENTOSA ULTRA-LUXURY RETREAT',
                (
                    'Transfer to an ultra-luxury Sentosa Island resort. Indulge in personalized spa therapies and absolute serenity by the private beach.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'MICHELIN DINING & LEISURE',
                (
                    "Experience world-class culinary excellence at a Michelin-starred restaurant. Enjoy personalized shopping or leisure in Singapore's most prestigious districts."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'DEPARTURE',
                (
                    'Final luxury breakfast. VIP chauffeur transfer to the airport, concluding your premium Singapore luxury expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Marina Bay Sands',
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
                'Marina Bay Sands',
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
                'Marina Bay Sands',
                '4N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'Marina Bay Sands (Sands SkyPark Suite) / Capella Singapore',
                'Multi-city Singapore',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Marina Bay Sands (Sands SkyPark Suite) / Capella Singapore',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Singapore', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('International and connecting flights as per curated itinerary (where applicable)', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Singapore visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_sg_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SG-006'
    tour_code = 'TRG-SIN-EXP-2026'
    title = 'Singapore Explorer'
    duration = '05 Nights / 06 Days'
    slug = 'sg-006-singapore-explorer-tour'
    itin_slug = 'sg-006-singapore-explorer-itinerary'
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
            _ph('Serial code SG-006 | TRAGUIN tour code TRG-SIN-EXP-2026', 1),
            _ph('Country: Singapore, Asia | Category: Best Singapore Explorer Family Tour Package', 2),
            _ph('Destinations: Marina Bay • Gardens by the Bay • Sentosa Island • Universal Studios • Safari Adventures', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Family', 'Luxury', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Singapore Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Singapore Explorer',
        overview="Marina Bay • Gardens by the Bay • Sentosa Island • Universal Studios • Safari Adventures 05 Nights / 06 Days Comprehensive Singapore Explorer Family Expedition SERIAL CODE: SG-006 TRAGUIN TOUR CODE: TRG-SIN-EXP-2026 STATE / COUNTRY: Singapore CATEGORY: Best Singapore Explorer Family Tour Package DURATION: 05 Nights / 06 Days Comprehensive City & Island Exploration\n\nTOUR OVERVIEW\nEmbark on the ultimate exploration of Singapore with our TRAGUIN curated family itinerary. Designed for discovery, this Singapore Explorer package offers a deep dive into the city's futuristic architecture, lush natural beauty, and theme park excitement, ensuring unforgettable memories in the heart of Southeast Asia's most dynamic destination. THE IMMERSIVE DAY-WISE ITINERARY",
        seo_title='SG-006 | Singapore Explorer | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Singapore package (SG-006 / TRG-SIN-EXP-2026): Marina Bay • Gardens by the Bay • Sentosa Island • Universal Studios • Safari Adventures with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL & MARINA BAY GLOW', 1),
            _ih('Day 02: GARDENS BY THE BAY & CULTURE', 2),
            _ih('Day 03: SENTOSA ISLAND ADVENTURE', 3),
            _ih('Day 04: UNIVERSAL STUDIOS SINGAPORE', 4),
            _ih('Day 05: SAFARI & WILDLIFE DISCOVERY', 5),
            _ih('Day 06: DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL & MARINA BAY GLOW',
                (
                    'Arrive in Singapore. Private transfer to your premium hotel. Evening walking tour of Marina Bay to witness the stunning light and water show.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'GARDENS BY THE BAY & CULTURE',
                (
                    'Explore the wonders of Gardens by the Bay, including the iconic Supertree Grove. A fantastic educational experience for the whole family.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'SENTOSA ISLAND ADVENTURE',
                (
                    'A full day at Sentosa Island, exploring its diverse attractions, sandy beaches, and recreational sites—creating unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'UNIVERSAL STUDIOS SINGAPORE',
                (
                    'A thrilling full day at Universal Studios Singapore, enjoying world-class movie-themed rides and immersive experiences—an essential Singapore family experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'SAFARI & WILDLIFE DISCOVERY',
                (
                    "Explore Singapore's famous wildlife spots, including the Night Safari, offering an exciting and unique exclusive experience."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'DEPARTURE',
                (
                    'Final breakfast before your TRAGUIN private transfer to the airport, completing your premium Singapore explorer expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Marina Bay Sands / Shangri-La Singapore',
                'Multi-city Singapore',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Marina Bay Sands / Shangri-La Singapore',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Marina Bay',
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
                'Marina Bay',
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
                'Marina Bay',
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
            _inc_included('Premium handpicked accommodation across Singapore', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('International and connecting flights as per curated itinerary (where applicable)', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Singapore visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_sg_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SG-007'
    tour_code = 'TRG-SIN-MAL-2026'
    title = 'Singapore & Malaysia Tour'
    duration = '05 Nights / 06 Days'
    slug = 'sg-007-singapore-malaysia-tour'
    itin_slug = 'sg-007-singapore-malaysia-itinerary'
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
            _ph('Serial code SG-007 | TRAGUIN tour code TRG-SIN-MAL-2026', 1),
            _ph('Country: Singapore, Asia | Category: Premium Singapore- Malaysia Combo Family Tour', 2),
            _ph('Destinations: Singapore Highlights • Kuala Lumpur City • Genting Highlands • Batu Caves', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Family', 'Luxury', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Singapore Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Singapore & Malaysia Tour',
        overview='Singapore Highlights • Kuala Lumpur City • Genting Highlands • Batu Caves 05 Nights / 06 Days Classic Singapore & Malaysia Family Expedition SERIAL CODE: SG-007 TRAGUIN TOUR CODE: TRG-SIN-MAL-2026 STATE / COUNTRY: Singapore & Malaysia CATEGORY: Premium Singapore- Malaysia Combo Family Tour DURATION: 05 Nights / 06 Days Singapore (2N) + Malaysia (3N)\n\nTOUR OVERVIEW\nExperience the best of two worlds with our TRAGUIN curated Singapore & Malaysia combo. From the modern marvels of Singapore to the iconic landscapes and highland retreats of Malaysia, this family-friendly expedition offers a perfect mix of cultural discovery, sightseeing, and fun, creating unforgettable memories. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='SG-007 | Singapore & Malaysia Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Singapore package (SG-007 / TRG-SIN-MAL-2026): Singapore Highlights • Kuala Lumpur City • Genting Highlands • Batu Caves with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SINGAPORE & CITY VISTAS', 1),
            _ih('Day 02: GARDENS BY THE BAY & TRANSFER', 2),
            _ih('Day 03: KUALA LUMPUR HIGHLIGHTS', 3),
            _ih('Day 04: BATU CAVES & GENTING HIGHLANDS', 4),
            _ih('Day 05: LEISURE & LOCAL EXPLORATION', 5),
            _ih('Day 06: DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SINGAPORE & CITY VISTAS',
                (
                    'Arrive in Singapore. Private transfer to your premium city hotel. Evening at Marina Bay to witness the spectacular light show.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'GARDENS BY THE BAY & TRANSFER',
                (
                    'Explore the futuristic Gardens by the Bay. Afternoon transfer to Malaysia, enjoying scenic highway views along the way.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'KUALA LUMPUR HIGHLIGHTS',
                (
                    'Tour the iconic Petronas Towers and cultural sites of Kuala Lumpur. Experience the diverse charm of this modern capital.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'BATU CAVES & GENTING HIGHLANDS',
                (
                    'Visit the magnificent Batu Caves. Ascend to Genting Highlands for a day of cool mountain air and family fun, a classic exclusive experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'LEISURE & LOCAL EXPLORATION',
                (
                    'A relaxed day in Kuala Lumpur, perfect for final shopping and enjoying local cuisine, creating unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'DEPARTURE',
                (
                    'Final breakfast before your TRAGUIN private transfer to the airport, completing your premium combo expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Marina Bay Sands / Shangri-LaGrand Hyatt Kuala Lumpur / Genting Resort',
                'Multi-city Singapore',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Marina Bay Sands / Shangri-LaGrand Hyatt Kuala Lumpur / Genting Resort',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Singapore Highlights',
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
                'Singapore Highlights',
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
                'Singapore Highlights',
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
            _inc_included('Premium handpicked accommodation across Singapore', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('International and connecting flights as per curated itinerary (where applicable)', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Singapore visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_sg_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SG-008'
    tour_code = 'TRG-SIN-SHOP-2026'
    title = 'Singapore Ladies Shopping Tour'
    duration = '04 Nights / 05 Days'
    slug = 'sg-008-singapore-ladies-shopping-tour'
    itin_slug = 'sg-008-singapore-ladies-shopping-itinerary'
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
            _ph('Serial code SG-008 | TRAGUIN tour code TRG-SIN-SHOP-2026', 1),
            _ph('Country: Singapore, Asia | Category: Premium Ladies Shopping Tour Package', 2),
            _ph('Destinations: Orchard Road • Marina Bay • Bugis Street • Local Gems • Exclusive Shopping', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Luxury', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Singapore Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Singapore Ladies Shopping Tour',
        overview='Orchard Road • Marina Bay • Bugis Street • Local Gems • Exclusive Shopping 04 Nights / 05 Days Ultimate Singapore Ladies Shopping Expedition SERIAL CODE: SG-008 TRAGUIN TOUR CODE: TRG-SIN-SHOP-2026 STATE / COUNTRY: Singapore CATEGORY: Premium Ladies Shopping Tour Package DURATION: 04 Nights / 05 Days Singapore Shopping Districts\n\nTOUR OVERVIEW\nIndulge in a world-class shopping experience with our TRAGUIN curated Singapore Ladies Shopping Tour. From the high-end luxury boutiques of Orchard Road to the vibrant local gems in Bugis Street, this journey is tailored for style, comfort, and the ultimate retail therapy, ensuring unforgettable memories in Singapore. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='SG-008 | Singapore Ladies Shopping Tour | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Singapore package (SG-008 / TRG-SIN-SHOP-2026): Orchard Road • Marina Bay • Bugis Street • Local Gems • Exclusive Shopping with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL & ORCHARD ROAD PREVIEW', 1),
            _ih('Day 02: ULTIMATE LUXURY RETAIL THERAPY', 2),
            _ih('Day 03: BUGIS STREET & LOCAL TREASURES', 3),
            _ih('Day 04: MARINA BAY & RELAXED SHOPPING', 4),
            _ih('Day 05: DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL & ORCHARD ROAD PREVIEW',
                (
                    'Arrive in Singapore. Private transfer to your premium hotel. Begin your shopping adventure with a leisurely preview of the world-famous Orchard Road.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'ULTIMATE LUXURY RETAIL THERAPY',
                (
                    'A full day dedicated to luxury flagship stores and designer boutiques in the city’s premier shopping belts, an exclusive experience for style lovers.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'BUGIS STREET & LOCAL TREASURES',
                (
                    'Explore the vibrant markets of Bugis Street. Discover unique local gems, trendy fashion, and traditional crafts in this lively Singapore shopping experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'MARINA BAY & RELAXED SHOPPING',
                (
                    'Enjoy upscale shopping at Marina Bay Sands. Conclude the day with a relaxed evening of fine dining, celebrating your unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'DEPARTURE',
                (
                    'Final breakfast before your TRAGUIN private transfer to the airport, completing your premium shopping expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Selected Boutique Shopping Hotels / Luxury City Stays',
                'Multi-city Singapore',
                '4N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Selected Boutique Shopping Hotels / Luxury City Stays',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Orchard Road',
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
                'Orchard Road',
                '4N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Orchard Road',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Singapore', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('International and connecting flights as per curated itinerary (where applicable)', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Singapore visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_sg_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SG-009'
    tour_code = 'TRG-SIN-LEI-2026'
    title = 'Singapore Leisure Tour'
    duration = '04 Nights / 05 Days'
    slug = 'sg-009-singapore-leisure-tour'
    itin_slug = 'sg-009-singapore-leisure-itinerary'
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
            _ph('Serial code SG-009 | TRAGUIN tour code TRG-SIN-LEI-2026', 1),
            _ph('Country: Singapore, Asia | Category: Premium Senior- Friendly Singapore Package', 2),
            _ph('Destinations: Marina Bay Leisure • Botanical Gardens • River Cruise • Cultural Heritage', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Luxury', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Singapore Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Singapore Leisure Tour',
        overview='04 Nights / 05 Days Relaxing Senior-Friendly Singapore Sojourn SERIAL CODE: SG-009 TRAGUIN TOUR CODE: TRG-SIN-LEI-2026 STATE / COUNTRY: Singapore CATEGORY: Premium Senior- Friendly Singapore Package DURATION: 04 Nights / 05 Days Singapore City Leisure\n\nTOUR OVERVIEW\nEnjoy a comfortable, relaxed, and culturally enriching experience in the vibrant city of Singapore with this TRAGUIN curated leisure itinerary. Specifically designed for senior citizens, this Singapore Leisure Sojourn prioritizes comfort, slow-paced sightseeing, and easy access to local culture, guaranteeing unforgettable memories in the serene and modern environment of Singapore. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='SG-009 | Singapore Leisure Tour | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Singapore package (SG-009 / TRG-SIN-LEI-2026): Marina Bay Leisure • Botanical Gardens • River Cruise • Cultural Heritage with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: COMFORTABLE ARRIVAL & MARINA BAY', 1),
            _ih('Day 02: GARDENS BY THE BAY LEISURE', 2),
            _ih('Day 03: RIVER CRUISE & CULTURAL HERITAGE', 3),
            _ih('Day 04: LEISURELY CITY DISCOVERY', 4),
            _ih('Day 05: COMFORTABLE DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'COMFORTABLE ARRIVAL & MARINA BAY',
                (
                    'Arrive in Singapore. Your private chauffeur transfers you to a premium hotel with easy access and beautiful city views. Savor a relaxed evening at Marina Bay.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'GARDENS BY THE BAY LEISURE',
                (
                    'A gentle tour of the magnificent Gardens by the Bay, focusing on accessible pathways and the stunning flora at a relaxed, senior-friendly pace.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'RIVER CRUISE & CULTURAL HERITAGE',
                (
                    'Enjoy a gentle river cruise, soaking in the city’s skyline from a comfortable seat. Followed by a leisurely visit to heritage areas with minimal walking.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'LEISURELY CITY DISCOVERY',
                (
                    'Spend a peaceful day enjoying the scenic beauty of Singapore’s quiet botanical gardens and upscale city districts at a leisurely, personalized pace.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'COMFORTABLE DEPARTURE',
                (
                    'Final luxury breakfast before your TRAGUIN private chauffeur transfers you comfortably to the airport, completing your premium Singapore experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Selected Senior-Friendly City Hotels / Luxury Suites',
                'Multi-city Singapore',
                '4N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Selected Senior-Friendly City Hotels / Luxury Suites',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Marina Bay Leisure',
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
                'Marina Bay Leisure',
                '4N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Marina Bay Leisure',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Singapore', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('International and connecting flights as per curated itinerary (where applicable)', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Singapore visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_sg_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SG-010'
    tour_code = 'TRG-SIN-EDU-2026'
    title = 'Singapore Educational Tour'
    duration = '04 Nights / 05 Days'
    slug = 'sg-010-singapore-educational-tour'
    itin_slug = 'sg-010-singapore-educational-itinerary'
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
            _ph('Serial code SG-010 | TRAGUIN tour code TRG-SIN-EDU-2026', 1),
            _ph('Country: Singapore, Asia | Category: Educational School Tour Package', 2),
            _ph('Destinations: Science Centre • NEWater Visitor Centre • Marina Barrage • Cultural Heritage', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Singapore Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Singapore Educational Tour',
        overview="Science Centre • NEWater Visitor Centre • Marina Barrage • Cultural Heritage 04 Nights / 05 Days Immersive Singapore Educational School Expedition SERIAL CODE: SG-010 TRAGUIN TOUR CODE: TRG-SIN-EDU-2026 STATE / COUNTRY: Singapore CATEGORY: Educational School Tour Package DURATION: 04 Nights / 05 Days Singapore Science & Cultural Learning\n\nTOUR OVERVIEW\nEmpower students with a structured, educational journey into the heart of Singapore's scientific advancement, sustainability practices, and rich cultural diversity. This TRAGUIN curated school expedition offers students a hands-on learning experience at world-class facilities, creating unforgettable memories. THE IMMERSIVE DAY-WISE ITINERARY",
        seo_title='SG-010 | Singapore Educational Tour | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Singapore package (SG-010 / TRG-SIN-EDU-2026): Science Centre • NEWater Visitor Centre • Marina Barrage • Cultural Heritage with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL & ORIENTATION', 1),
            _ih('Day 02: SCIENCE & INNOVATION', 2),
            _ih('Day 03: SUSTAINABILITY & TECHNOLOGY', 3),
            _ih('Day 04: CULTURAL HERITAGE & DISCOVERY', 4),
            _ih('Day 05: DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL & ORIENTATION',
                (
                    'Arrive in Singapore. Private group transfer to your educational basecamp hotel. Briefing on the educational highlights of the tour.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'SCIENCE & INNOVATION',
                (
                    'A full day at the Singapore Science Centre, engaging with interactive exhibits that showcase modern scientific innovation—a top educational experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'SUSTAINABILITY & TECHNOLOGY',
                (
                    'Visit the NEWater Visitor Centre and Marina Barrage to learn about Singapore’s innovative water sustainability and urban planning technological practices.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'CULTURAL HERITAGE & DISCOVERY',
                (
                    "Explore Singapore's vibrant multicultural heritage through interactive visits to museums and cultural centers, focusing on social integration."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'DEPARTURE',
                (
                    'Final group breakfast, educational summary session, and private transfer to the airport, completing your premium Singapore educational school tour. HANDPICKED EDUCATIONAL STAYS Category Singapore Student Accommodations (4N) Option 01: Premium Selected Educational Group Hotels / Hostels'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Selected Educational Group Hotels / Hostels',
                'Multi-city Singapore',
                '4N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Selected Educational Group Hotels / Hostels',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Science Centre',
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
                'Science Centre',
                '4N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Science Centre',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Singapore', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('International and connecting flights as per curated itinerary (where applicable)', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Singapore visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_sg_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SG-011'
    tour_code = 'TRG-SIN-FUN-2026'
    title = 'Singapore Sentosa Fun'
    duration = '04 Nights / 05 Days'
    slug = 'sg-011-singapore-sentosa-fun-tour'
    itin_slug = 'sg-011-singapore-sentosa-fun-itinerary'
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
            _ph('Serial code SG-011 | TRAGUIN tour code TRG-SIN-FUN-2026', 1),
            _ph('Country: Singapore, Asia | Category: Best Sentosa Family Fun Tour Package', 2),
            _ph('Destinations: Sentosa Island • Universal Studios • Adventure Cove • Family Resort Stay', 3),
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
        price_note='On Request (Premium Singapore Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Singapore Sentosa Fun',
        overview='Sentosa Island • Universal Studios • Adventure Cove • Family Resort Stay 04 Nights / 05 Days Ultimate Sentosa Family Fun Expedition SERIAL CODE: SG-011 TRAGUIN TOUR CODE: TRG-SIN-FUN-2026 STATE / COUNTRY: Singapore CATEGORY: Best Sentosa Family Fun Tour Package DURATION: 04 Nights / 05 Days Sentosa Island & Singapore City\n\nTOUR OVERVIEW\nGet ready for non-stop action and thrills with our TRAGUIN curated Sentosa Fun Package. This Singapore- Sentosa family holiday is jam-packed with world-class theme parks, water adventures, and resort relaxation, guaranteeing unforgettable memories in Southeast Asia’s premier entertainment hub. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='SG-011 | Singapore Sentosa Fun | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Singapore package (SG-011 / TRG-SIN-FUN-2026): Sentosa Island • Universal Studios • Adventure Cove • Family Resort Stay with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL & SENTOSA CHECK-IN', 1),
            _ih('Day 02: UNIVERSAL STUDIOS ADVENTURE', 2),
            _ih('Day 03: ADVENTURE COVE & WATER FUN', 3),
            _ih('Day 04: SENTOSA ISLAND DISCOVERY', 4),
            _ih('Day 05: DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL & SENTOSA CHECK-IN',
                (
                    'Arrive in Singapore. Private transfer to your ultra-luxury Sentosa resort. Spend the evening enjoying the island’s serene beach and amenities.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'UNIVERSAL STUDIOS ADVENTURE',
                (
                    'A full day of thrills at Universal Studios Singapore. Enjoy priority access to top movie-themed rides—a perfect family experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'ADVENTURE COVE & WATER FUN',
                (
                    'Experience the excitement of Adventure Cove Waterpark. Perfect for family aquatic fun, ensuring you collect unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'SENTOSA ISLAND DISCOVERY',
                (
                    'Explore Sentosa’s various attractions, from luge rides to cable car vistas. A day of action-packed entertainment and island leisure.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'DEPARTURE',
                (
                    'Final luxury breakfast before your TRAGUIN private transfer to the airport, completing your premium Sentosa family adventure.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Shangri-La Rasa Sentosa / Resorts World Sentosa',
                'Multi-city Singapore',
                '4N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Shangri-La Rasa Sentosa / Resorts World Sentosa',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Sentosa Island',
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
                'Sentosa Island',
                '4N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Sentosa Island',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Singapore', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('International and connecting flights as per curated itinerary (where applicable)', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Singapore visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_sg_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SG-012'
    tour_code = 'TRG-SIN-MAR-2026'
    title = 'Marina Bay Luxury Tour'
    duration = '04 Nights / 05 Days'
    slug = 'sg-012-marina-bay-luxury-tour'
    itin_slug = 'sg-012-marina-bay-luxury-itinerary'
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
            _ph('Serial code SG-012 | TRAGUIN tour code TRG-SIN-MAR-2026', 1),
            _ph('Country: Singapore, Asia | Category: Ultra-Luxury Marina Bay Tour Package', 2),
            _ph('Destinations: Marina Bay Sands • Private Yacht • Michelin Dining • Exclusive City Sojourn', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Culture', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Singapore Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Marina Bay Luxury Tour',
        overview='04 Nights / 05 Days Ultra-Luxury Marina Bay Expedition SERIAL CODE: SG-012 TRAGUIN TOUR CODE: TRG-SIN-MAR-2026 STATE / COUNTRY: Singapore CATEGORY: Ultra-Luxury Marina Bay Tour Package DURATION: 04 Nights / 05 Days Marina Bay Luxury\n\nTOUR OVERVIEW\nIndulge in the absolute height of elegance at the heart of Singapore. This TRAGUIN curated luxury expedition centers around the iconic Marina Bay, offering opulent stays at the world-famous Marina Bay Sands, private yacht excursions, and elite Michelin-starred culinary experiences, ensuring unforgettable memories. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='SG-012 | Marina Bay Luxury Tour | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Singapore package (SG-012 / TRG-SIN-MAR-2026): Marina Bay Sands • Private Yacht • Michelin Dining • Exclusive City Sojourn with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: VIP ARRIVAL & MARINA BAY CHECK-IN', 1),
            _ih('Day 02: SKYPARK & EXCLUSIVE DINING', 2),
            _ih('Day 03: PRIVATE YACHT SOJOURN', 3),
            _ih('Day 04: LEISURE & ARTISTIC DISCOVERY', 4),
            _ih('Day 05: DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'VIP ARRIVAL & MARINA BAY CHECK-IN',
                (
                    'Arrive in Singapore. VIP chauffeur transfer to Marina Bay Sands. Check into your ultra-luxury suite and enjoy a welcome cocktail overlooking the bay.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'SKYPARK & EXCLUSIVE DINING',
                (
                    'Access the exclusive Sands SkyPark. Enjoy a private gourmet dinner at one of the bay’s premier Michelin- starred restaurants.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'PRIVATE YACHT SOJOURN',
                (
                    'Embark on a private yacht cruise around the Singapore Harbour, experiencing the city’s skyline from an exclusive experience point of view.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'LEISURE & ARTISTIC DISCOVERY',
                (
                    'Enjoy a leisurely day of private shopping at luxury boutiques or artistic visits in the Marina Bay area, creating unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'DEPARTURE',
                (
                    'Final luxury breakfast before your TRAGUIN private chauffeur transfer to the airport, concluding your premium Marina Bay luxury expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Marina Bay Sands',
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
                'Marina Bay Sands',
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
                'Marina Bay Sands',
                '4N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'Marina Bay Sands (Sands SkyPark Suite)',
                'Multi-city Singapore',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Marina Bay Sands (Sands SkyPark Suite)',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Singapore', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('International and connecting flights as per curated itinerary (where applicable)', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Singapore visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_sg_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SG-013'
    tour_code = 'TRG-SIN-DLX-2026'
    title = 'Singapore Deluxe Family Tour'
    duration = '05 Nights / 06 Days'
    slug = 'sg-013-singapore-deluxe-family-tour'
    itin_slug = 'sg-013-singapore-deluxe-family-itinerary'
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
            _ph('Serial code SG-013 | TRAGUIN tour code TRG-SIN-DLX-2026', 1),
            _ph('Country: Singapore, Asia | Category: Deluxe Singapore Family Tour Package', 2),
            _ph('Destinations: Marina Bay • Gardens by the Bay • Sentosa Island • Universal Studios • Luxury City', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Family', 'Luxury', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Singapore Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Singapore Deluxe Family Tour',
        overview='Marina Bay • Gardens by the Bay • Sentosa Island • Universal Studios • Luxury City Sojourn 05 Nights / 06 Days Deluxe Singapore Family Expedition SERIAL CODE: SG-013 TRAGUIN TOUR CODE: TRG-SIN-DLX-2026 STATE / COUNTRY: Singapore CATEGORY: Deluxe Singapore Family Tour Package DURATION: 05 Nights / 06 Days Singapore City & Sentosa Deluxe\n\nTOUR OVERVIEW\nEnjoy a perfect blend of comfort, style, and excitement with our TRAGUIN curated Singapore Deluxe Family Tour. From luxurious accommodations to curated theme park access and city tours, this Singapore Deluxe itinerary ensures your family enjoys a premium experience, creating unforgettable memories in the heart of Singapore. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='SG-013 | Singapore Deluxe Family Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Singapore package (SG-013 / TRG-SIN-DLX-2026): Marina Bay • Gardens by the Bay • Sentosa Island • Universal Studios • Luxury City with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL & CITY MARVELS', 1),
            _ih('Day 02: GARDENS BY THE BAY & CULTURAL TOUR', 2),
            _ih('Day 03: SENTOSA ISLAND RESORT LEISURE', 3),
            _ih('Day 04: UNIVERSAL STUDIOS EXCELLENCE', 4),
            _ih('Day 05: CITY DISCOVERY & SHOPPING', 5),
            _ih('Day 06: DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL & CITY MARVELS',
                (
                    'Arrive in Singapore. Private transfer to your handpicked deluxe hotel. Enjoy the evening exploring the breathtaking Marina Bay area.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'GARDENS BY THE BAY & CULTURAL TOUR',
                (
                    'Explore the stunning Gardens by the Bay. Followed by a cultural tour, showcasing the iconic attractions that define Singapore.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'SENTOSA ISLAND RESORT LEISURE',
                (
                    'Transfer to your Sentosa Island resort. Enjoy leisure time, sandy beaches, and island attractions, a fantastic premium family experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'UNIVERSAL STUDIOS EXCELLENCE',
                (
                    'A full day of excitement at Universal Studios Singapore, enjoying top-tier movie-themed rides—creating unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'CITY DISCOVERY & SHOPPING',
                (
                    'Explore Singapore’s vibrant shopping districts and modern landmarks, enjoying the scenic beauty of the city.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'DEPARTURE',
                (
                    'Final luxury breakfast before your TRAGUIN private transfer to the airport, completing your premium Singapore deluxe family expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Selected Deluxe Hotels / Sentosa Beach Resorts',
                'Multi-city Singapore',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Selected Deluxe Hotels / Sentosa Beach Resorts',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Marina Bay',
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
                'Marina Bay',
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
                'Marina Bay',
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
            _inc_included('Premium handpicked accommodation across Singapore', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('International and connecting flights as per curated itinerary (where applicable)', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Singapore visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_sg_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SG-014'
    tour_code = 'TRG-SIN-CORP-2026'
    title = 'Singapore Corporate Tour'
    duration = '04 Nights / 05 Days'
    slug = 'sg-014-singapore-corporate-tour'
    itin_slug = 'sg-014-singapore-corporate-itinerary'
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
            _ph('Serial code SG-014 | TRAGUIN tour code TRG-SIN-CORP-2026', 1),
            _ph('Country: Singapore, Asia | Category: Corporate MICE Tour Package', 2),
            _ph('Destinations: Corporate Conferences • Networking Gala • Marina Bay Business District • Exclusive', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Luxury', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Singapore Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Singapore Corporate Tour',
        overview='Corporate Conferences • Networking Gala • Marina Bay Business District • Exclusive Teambuilding 04 Nights / 05 Days Premier Singapore Corporate MICE Solution SERIAL CODE: SG-014 TRAGUIN TOUR CODE: TRG-SIN-CORP-2026 STATE / COUNTRY: Singapore CATEGORY: Corporate MICE Tour Package DURATION: 04 Nights / 05 Days Singapore Corporate & Networking Focus PROGRAM OVERVIEW Elevate your corporate presence in Singapore with our TRAGUIN curated MICE expedition. Designed for professional excellence, this corporate program integrates seamless conference logistics, exclusive networking venues, and premium teambuilding experiences, ensuring an effective and high-impact corporate trip. THE CURATED PROGRAM ITINERARY',
        seo_title='SG-014 | Singapore Corporate Tour | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Singapore package (SG-014 / TRG-SIN-CORP-2026): Corporate Conferences • Networking Gala • Marina Bay Business District • Exclusive with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: CORPORATE ARRIVAL & NETWORKING', 1),
            _ih('Day 02: CONFERENCE & STRATEGY SESSIONS', 2),
            _ih('Day 03: EXCLUSIVE TEAMBUILDING & NETWORKING', 3),
            _ih('Day 04: INDUSTRY VISITS & STRATEGIC INSIGHTS', 4),
            _ih('Day 05: DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'CORPORATE ARRIVAL & NETWORKING',
                (
                    'Arrive in Singapore. VIP airport greeting and transfer to premium business-focused hotel. Evening welcome cocktail networking reception for all delegates. TRAGUIN Corporate MICE •'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'CONFERENCE & STRATEGY SESSIONS',
                (
                    'Full-day dedicated conference session at a world-class Singapore business hub facility. Professional catering and technical support provided.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'EXCLUSIVE TEAMBUILDING & NETWORKING',
                (
                    'Curated teambuilding experience in a unique Singapore setting, followed by an evening networking gala dinner at a premium Marina Bay venue.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'INDUSTRY VISITS & STRATEGIC INSIGHTS',
                (
                    'Visit key industry partners or innovation hubs in Singapore to gain strategic insights. Evening at leisure for individual networking.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'DEPARTURE',
                (
                    'Final breakfast and wrap-up session before your TRAGUIN private chauffeur transfer to the airport, completing your high-impact corporate expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Marina Bay Sands Business Suites / Grand Hyatt Singapore "Creating Impact Beyond Destinations"',
                'Multi-city Singapore',
                '4N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Marina Bay Sands Business Suites / Grand Hyatt Singapore "Creating Impact Beyond Destinations"',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Corporate Conferences',
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
                'Corporate Conferences',
                '4N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Corporate Conferences',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Singapore', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('International and connecting flights as per curated itinerary (where applicable)', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Singapore visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_sg_015(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SG-015'
    tour_code = 'TRG-SIN-GRD-2026'
    title = 'Grand Singapore Family Tour'
    duration = '05 Nights / 06 Days'
    slug = 'sg-015-grand-singapore-family-tour'
    itin_slug = 'sg-015-grand-singapore-family-itinerary'
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
            _ph('Serial code SG-015 | TRAGUIN tour code TRG-SIN-GRD-2026', 1),
            _ph('Country: Singapore, Asia | Category: Best Grand Singapore Family Tour Package', 2),
            _ph('Destinations: Marina Bay • Gardens by the Bay • Sentosa Resort • Universal Studios • City Highlights', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Family', 'Luxury', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Singapore Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Grand Singapore Family Tour',
        overview='Marina Bay • Gardens by the Bay • Sentosa Resort • Universal Studios • City Highlights 05 Nights / 06 Days Grand Singapore Family Expedition SERIAL CODE: SG-015 TRAGUIN TOUR CODE: TRG-SIN-GRD-2026 STATE / COUNTRY: Singapore CATEGORY: Best Grand Singapore Family Tour Package DURATION: 05 Nights / 06 Days Singapore City & Sentosa Grand Discovery\n\nTOUR OVERVIEW\nDiscover the absolute best of Singapore with our TRAGUIN curated Grand Family Expedition. This comprehensive itinerary blends luxury city stays, immersive nature explorations, and world-class theme park thrills, ensuring your family creates unforgettable memories in this spectacular city-state. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='SG-015 | Grand Singapore Family Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Singapore package (SG-015 / TRG-SIN-GRD-2026): Marina Bay • Gardens by the Bay • Sentosa Resort • Universal Studios • City Highlights with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL & MARINA BAY SPLENDOR', 1),
            _ih('Day 02: GARDENS BY THE BAY & CULTURAL SIGHTS', 2),
            _ih('Day 03: SENTOSA ISLAND DISCOVERY', 3),
            _ih('Day 04: UNIVERSAL STUDIOS SINGAPORE', 4),
            _ih('Day 05: CITY HIGHLIGHTS & SHOPPING', 5),
            _ih('Day 06: DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL & MARINA BAY SPLENDOR',
                (
                    'Arrive in Singapore. Private transfer to your handpicked premium resort. Evening walk through Marina Bay to witness the grand city skyline.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'GARDENS BY THE BAY & CULTURAL SIGHTS',
                (
                    'Explore the stunning Gardens by the Bay. Followed by a grand cultural tour, showcasing the iconic attractions that define Singapore.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'SENTOSA ISLAND DISCOVERY',
                (
                    'Transfer to Sentosa Island. A day of exploration, beach leisure, and island attractions—a perfect premium family experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'UNIVERSAL STUDIOS SINGAPORE',
                (
                    'A full day of thrills at Universal Studios Singapore, enjoying world-class movie-themed rides—creating unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'CITY HIGHLIGHTS & SHOPPING',
                (
                    "A comprehensive tour of Singapore's famous shopping districts and city landmarks, enjoying the scenic beauty of this dynamic metropolis."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'DEPARTURE',
                (
                    'Final luxury breakfast before your TRAGUIN private transfer to the airport, completing your premium grand Singapore family expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Selected Grand City Hotels / Beach Resorts ● TRAGUIN',
                'Multi-city Singapore',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Selected Grand City Hotels / Beach Resorts ● TRAGUIN',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Marina Bay',
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
                'Marina Bay',
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
                'Marina Bay',
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
            _inc_included('Premium handpicked accommodation across Singapore', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven van', 2),
            _inc_included('International and connecting flights as per curated itinerary (where applicable)', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Singapore visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

SINGAPORE_SG_001_015_BUILDERS = [
    build_sg_001,
    build_sg_002,
    build_sg_003,
    build_sg_004,
    build_sg_005,
    build_sg_006,
    build_sg_007,
    build_sg_008,
    build_sg_009,
    build_sg_010,
    build_sg_011,
    build_sg_012,
    build_sg_013,
    build_sg_014,
    build_sg_015,
]
