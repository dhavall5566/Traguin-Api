"""Builder functions for VN-001 through VN-010 VIETNAM international packages."""

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

VN_SLUG = "vietnam"


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


def build_vn_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'VN-001'
    tour_code = 'TRG-VNM-EXP-2026'
    title = 'Vietnam Explorer Family Tour'
    duration = '07 Nights / 08 Days'
    slug = 'vn-001-vietnam-explorer-family-tour'
    itin_slug = 'vn-001-vietnam-explorer-itinerary'
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
            _ph('Serial code VN-001 | TRAGUIN tour code TRG-VNM-EXP-2026', 1),
            _ph('Country: Vietnam, Southeast Asia | Category: Premium Vietnam Family Explorer Package', 2),
            _ph('Destinations: Hanoi • Halong Bay • Da Nang • Hoi An • Scenic Heritage Discovery', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Family', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Vietnam Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Vietnam Explorer Family Tour',
        overview='Hanoi • Halong Bay • Da Nang • Hoi An • Scenic Heritage Discovery 07 Nights / 08 Days Comprehensive Vietnam Family Explorer Expedition SERIAL CODE: VN-002 TRAGUIN TOUR CODE: TRG-VNM-EXP-2026 STATE / COUNTRY: Vietnam CATEGORY: Premium Vietnam Family Explorer Package DURATION: 07 Nights / 08 Days Hanoi (2N) + Halong Bay (2N) + Da Nang/Hoi An (3N)\n\nTOUR OVERVIEW\nDiscover the absolute best of Vietnam with our TRAGUIN curated family explorer expedition. From the historic northern charm of Hanoi and the emerald serenity of Halong Bay to the central coastal beauty of Da Nang and Hoi An, this comprehensive journey ensures your family creates unforgettable memories across this stunning nation. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='VN-001 | Vietnam Explorer Family Tour | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Vietnam package (VN-001 / TRG-VNM-EXP-2026): Hanoi • Halong Bay • Da Nang • Hoi An • Scenic Heritage Discovery with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN HANOI & CULTURAL VIBE', 1),
            _ih('Day 02: HANOI HERITAGE EXPLORATION', 2),
            _ih('Day 03: HALONG BAY CRUISE COMMENCEMENT', 3),
            _ih('Day 04: HALONG BAY ADVENTURE', 4),
            _ih('Day 05: FLIGHT TO DA NANG & HOI AN', 5),
            _ih('Day 06: ANCIENT TOWN & CULTURAL MAGIC', 6),
            _ih('Day 07: COASTAL LEISURE & CELEBRATION', 7),
            _ih('Day 08: DEPARTURE', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN HANOI & CULTURAL VIBE',
                (
                    'Arrive in Hanoi. Private transfer to your handpicked premium hotel. Evening at leisure in the historic Old Quarter.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'HANOI HERITAGE EXPLORATION',
                (
                    'Guided city tour of Hanoi’s most significant cultural and historical landmarks. A perfect educational introduction to Vietnam’s heritage.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'HALONG BAY CRUISE COMMENCEMENT',
                (
                    'Transfer to Halong Bay. Board your ultra-luxury cruise vessel. Savor gourmet dining while sailing through the iconic limestone islands.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'HALONG BAY ADVENTURE',
                (
                    'Enjoy exclusive activities aboard the cruise, including cave exploration, swimming in hidden coves, and spectacular sunset deck views—unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'FLIGHT TO DA NANG & HOI AN',
                (
                    'Morning cruise brunch. Transfer to the airport for your flight to Da Nang. Transfer to your luxury coastal resort in Hoi An.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'ANCIENT TOWN & CULTURAL MAGIC',
                (
                    "A guided tour of Hoi An's Ancient Town, a UNESCO World Heritage site known for its charming architecture, night markets, and traditional lanterns."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'COASTAL LEISURE & CELEBRATION',
                (
                    'A day of leisure at your coastal resort, followed by a grand farewell dinner celebrating your premium Vietnam family explorer expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                8,
                'DEPARTURE',
                (
                    'Final breakfast before your TRAGUIN private transfer to the airport, completing your grand Vietnam journey.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Selected Heritage Hotels Ultra-Luxury Cruise Luxury Coastal Resort',
                'Multi-city Vietnam',
                '7N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Selected Heritage Hotels Ultra-Luxury Cruise Luxury Coastal Resort',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Hanoi',
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
                'Hanoi',
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
                'Hanoi',
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
            _inc_included('Premium handpicked accommodation across Vietnam', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven executive van', 2),
            _inc_included('Inter-city transfers and curated sightseeing as per itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Vietnam visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_vn_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'VN-002'
    tour_code = 'TRG-VNM-HIG-2026'
    title = 'Vietnam Highlights Family Tour'
    duration = '07 Nights / 08 Days'
    slug = 'vn-002-vietnam-highlights-family-tour'
    itin_slug = 'vn-002-vietnam-highlights-itinerary'
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
            _ph('Serial code VN-002 | TRAGUIN tour code TRG-VNM-HIG-2026', 1),
            _ph('Country: Vietnam, Southeast Asia | Category: Best Vietnam Family Highlights Tour Package', 2),
            _ph('Destinations: Hanoi • Halong Bay Cruise • Hoi An Ancient Town • Da Nang Beaches', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Family', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Vietnam Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Vietnam Highlights Family Tour',
        overview="Hanoi • Halong Bay Cruise • Hoi An Ancient Town • Da Nang Beaches 07 Nights / 08 Days The Ultimate Vietnam Family Highlights Expedition SERIAL CODE: VN-002 TRAGUIN TOUR CODE: TRG-VNM-HIG-2026 STATE / COUNTRY: Vietnam CATEGORY: Best Vietnam Family Highlights Tour Package DURATION: 07 Nights / 08 Days Hanoi (2N) + Halong Bay (2N) + Da Nang/Hoi An (3N)\n\nTOUR OVERVIEW\nDiscover the absolute highlights of Vietnam with our TRAGUIN curated family expedition. This comprehensive 8-day journey takes your family through the vibrant capital of Hanoi, the serene majesty of Halong Bay, and the cultural charm of Hoi An and Da Nang—creating unforgettable memories across Vietnam's iconic landscapes. THE IMMERSIVE DAY-WISE ITINERARY",
        seo_title='VN-002 | Vietnam Highlights Family Tour | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Vietnam package (VN-002 / TRG-VNM-HIG-2026): Hanoi • Halong Bay Cruise • Hoi An Ancient Town • Da Nang Beaches with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN HANOI', 1),
            _ih('Day 02: HANOI HIGHLIGHTS', 2),
            _ih('Day 03: HALONG BAY CRUISE', 3),
            _ih('Day 04: HALONG BAY ADVENTURE', 4),
            _ih('Day 05: FLIGHT TO DA NANG', 5),
            _ih('Day 06: HOI AN ANCIENT TOWN', 6),
            _ih('Day 07: COASTAL LEISURE & CELEBRATION', 7),
            _ih('Day 08: DEPARTURE', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN HANOI',
                (
                    'Arrive in Hanoi. Private transfer to your handpicked premium hotel. Evening at leisure to enjoy the historic Old Quarter.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'HANOI HIGHLIGHTS',
                (
                    'A comprehensive city tour covering Hanoi’s most famous landmarks, providing a rich educational experience for your family.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'HALONG BAY CRUISE',
                (
                    'Travel to Halong Bay. Board your ultra-luxury cruise vessel for an extraordinary journey through the limestone karsts.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'HALONG BAY ADVENTURE',
                (
                    'Explore hidden caves and enjoy guided activities on the water. A day filled with unforgettable memories and stunning views.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'FLIGHT TO DA NANG',
                (
                    'Morning cruise brunch before transferring to the airport for your flight to Da Nang. Check into a luxury coastal family resort.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'HOI AN ANCIENT TOWN',
                (
                    'Visit the charming Ancient Town of Hoi An, famous for its lantern-lit streets and rich history. A must-see highlight for any Vietnam tour.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'COASTAL LEISURE & CELEBRATION',
                (
                    'A relaxing day at the resort, followed by a grand farewell dinner gala at a beachfront restaurant—an exclusive experience for the family.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                8,
                'DEPARTURE',
                (
                    'Final luxury breakfast before your TRAGUIN private transfer to the airport, completing your premium Vietnam highlights expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Heritage City Hotels Ultra-Luxury Cruise Luxury Beachfront Resort',
                'Multi-city Vietnam',
                '7N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Heritage City Hotels Ultra-Luxury Cruise Luxury Beachfront Resort',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Hanoi',
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
                'Hanoi',
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
                'Hanoi',
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
            _inc_included('Premium handpicked accommodation across Vietnam', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven executive van', 2),
            _inc_included('Inter-city transfers and curated sightseeing as per itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Vietnam visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_vn_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'VN-003'
    tour_code = 'TRG-VNM-ROM-2026'
    title = 'Romantic Vietnam Couple Tour'
    duration = '05 Nights / 06 Days'
    slug = 'vn-003-romantic-vietnam-couple-tour'
    itin_slug = 'vn-003-romantic-vietnam-itinerary'
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
            _ph('Serial code VN-003 | TRAGUIN tour code TRG-VNM-ROM-2026', 1),
            _ph('Country: Vietnam, Southeast Asia | Category: Premium Romantic Couple Tour Package', 2),
            _ph('Destinations: Hanoi Charm • Halong Bay Private Cruise • Hoi An Romantic Streets • Coastal Serenity', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
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
        price_note='On Request (Premium Vietnam Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Romantic Vietnam Couple Tour',
        overview="Hanoi Charm • Halong Bay Private Cruise • Hoi An Romantic Streets • Coastal Serenity 05 Nights / 06 Days Romantic Vietnam Couple Sanctuary SERIAL CODE: VN-003 TRAGUIN TOUR CODE: TRG-VNM-ROM-2026 STATE / COUNTRY: Vietnam CATEGORY: Premium Romantic Couple Tour Package DURATION: 05 Nights / 06 Days Hanoi & Romantic Coastal Retreats\n\nTOUR OVERVIEW\nBegin your romantic journey together in the enchanting landscapes of Vietnam. This TRAGUIN curated couple's sanctuary blends the colonial charm of Hanoi, the serene luxury of a private cruise in Halong Bay, and the intimate streets of Hoi An, ensuring unforgettable memories in a truly romantic setting. THE IMMERSIVE DAY-WISE ITINERARY",
        seo_title='VN-003 | Romantic Vietnam Couple Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Vietnam package (VN-003 / TRG-VNM-ROM-2026): Hanoi Charm • Halong Bay Private Cruise • Hoi An Romantic Streets • Coastal Serenity with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN HANOI & INTIMATE WELCOME', 1),
            _ih('Day 02: HANOI CULTURAL HARMONY', 2),
            _ih('Day 03: HALONG BAY PRIVATE CRUISE', 3),
            _ih('Day 04: HALONG BAY SERENITY', 4),
            _ih('Day 05: HOI AN LANTERN MAGIC', 5),
            _ih('Day 06: DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN HANOI & INTIMATE WELCOME',
                (
                    'Arrive in Hanoi. Private transfer to your intimate boutique hotel. Savor a quiet, romantic welcome dinner in the heart of the city.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'HANOI CULTURAL HARMONY',
                (
                    'A slow-paced, romantic exploration of Hanoi’s hidden streets, museums, and local charms, perfect for couples wanting to discover cultural richness.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'HALONG BAY PRIVATE CRUISE',
                (
                    'Transfer to Halong Bay. Board your ultra-luxury private cruise vessel for an intimate getaway on the emerald waters.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'HALONG BAY SERENITY',
                (
                    'A day of private exploration, featuring sunset deck relaxation, cave visits, and candlelit dinners under the stars —unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'HOI AN LANTERN MAGIC',
                (
                    'Flight to Da Nang, followed by a romantic transfer to Hoi An. Experience the magic of the lantern-lit Ancient Town at night.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'DEPARTURE',
                (
                    'Final luxury breakfast before your TRAGUIN private transfer, completing your premium romantic Vietnam sojourn. HANDPICKED ROMANTIC STAYS Category Hanoi (2N) Halong Bay (2N) Hoi An (1N) Option 01: PremiumBoutique Heritage HotelsUltra-Luxury Private CruiseRomantic Resort Retreat'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Boutique Heritage HotelsUltra-Luxury Private CruiseRomantic Resort Retreat',
                'Multi-city Vietnam',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Boutique Heritage HotelsUltra-Luxury Private CruiseRomantic Resort Retreat',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Hanoi Charm',
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
                'Hanoi Charm',
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
                'Hanoi Charm',
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
            _inc_included('Premium handpicked accommodation across Vietnam', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven executive van', 2),
            _inc_included('Inter-city transfers and curated sightseeing as per itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Vietnam visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_vn_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'VN-004'
    tour_code = 'TRG-VNM-LUX-2026'
    title = 'Luxury Vietnam Tour'
    duration = '06 Nights / 07 Days'
    slug = 'vn-004-luxury-vietnam-tour'
    itin_slug = 'vn-004-luxury-vietnam-itinerary'
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
            _ph('Serial code VN-004 | TRAGUIN tour code TRG-VNM-LUX-2026', 1),
            _ph('Country: Vietnam, Southeast Asia | Category: Ultra-Luxury Vietnam Tour Package', 2),
            _ph('Destinations: Hanoi • Ultra-Luxury Halong Bay Cruise • Da Nang Luxury Resort • Exclusive Heritage', 3),
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
        price_note='On Request (Premium Vietnam Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Luxury Vietnam Tour',
        overview='Tours 06 Nights / 07 Days Ultra-Luxury Vietnam Expedition SERIAL CODE: VN-004 TRAGUIN TOUR CODE: TRG-VNM-LUX-2026 STATE / COUNTRY: Vietnam CATEGORY: Ultra-Luxury Vietnam Tour Package DURATION: 06 Nights / 07 Days Hanoi (2N) + Halong Bay (2N) + Da Nang/Hoi An (2N)\n\nTOUR OVERVIEW\nIndulge in the absolute height of sophistication across Vietnam with our TRAGUIN curated luxury expedition. From opulent five-star stays and private cruises to exclusive cultural tours and premium concierge service, this journey is designed for the discerning traveler, ensuring unforgettable memories in ultimate luxury. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='VN-004 | Luxury Vietnam Tour | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Vietnam package (VN-004 / TRG-VNM-LUX-2026): Hanoi • Ultra-Luxury Halong Bay Cruise • Da Nang Luxury Resort • Exclusive Heritage with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: VIP ARRIVAL & HANOI LUXURY', 1),
            _ih('Day 02: EXCLUSIVE HANOI HERITAGE', 2),
            _ih('Day 03: ULTRA-LUXURY CRUISE COMMENCEMENT', 3),
            _ih('Day 04: HALONG BAY SERENITY', 4),
            _ih('Day 05: FLIGHT TO DA NANG', 5),
            _ih('Day 06: HOI AN PRIVATE DISCOVERY', 6),
            _ih('Day 07: DEPARTURE', 7)
        ],
        days=[
            _day(
                1,
                'VIP ARRIVAL & HANOI LUXURY',
                (
                    'Arrive in Hanoi. VIP chauffeur transfer to your world-class hotel. Evening gourmet welcome dinner overlooking the historic city center.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'EXCLUSIVE HANOI HERITAGE',
                (
                    'Private guided tour of Hanoi’s most prestigious historical landmarks, providing a rich exclusive experience of Vietnamese culture.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'ULTRA-LUXURY CRUISE COMMENCEMENT',
                (
                    'Transfer to Halong Bay. Board your ultra-luxury cruise vessel. Experience gourmet dining while sailing through breathtaking limestone islands.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'HALONG BAY SERENITY',
                (
                    'Enjoy personalized activities, spa therapies, and gourmet relaxation aboard your vessel, surrounded by stunning scenery.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'FLIGHT TO DA NANG',
                (
                    'Morning brunch on the cruise. Private transfer to airport for your flight to Da Nang. Check into an ultra-luxury coastal resort.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'HOI AN PRIVATE DISCOVERY',
                (
                    'Private guided exploration of Hoi An’s Ancient Town, focusing on premium crafts and historical charm. Evening farewell gala dinner.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'DEPARTURE',
                (
                    'Final luxury breakfast. VIP chauffeur transfer to the airport, concluding your premium Vietnam luxury expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Hanoi',
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
                'Hanoi',
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
                'Hanoi',
                '6N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'Sofitel Legend Metropole HanoiElite Cruise VesselsInterContinental Danang Resort',
                'Multi-city Vietnam',
                '6N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Sofitel Legend Metropole HanoiElite Cruise VesselsInterContinental Danang Resort',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Vietnam', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven executive van', 2),
            _inc_included('Inter-city transfers and curated sightseeing as per itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Vietnam visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_vn_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'VN-005'
    tour_code = 'TRG-VNM-LAD-2026'
    title = 'Vietnam Ladies Escape'
    duration = '05 Nights / 06 Days'
    slug = 'vn-005-vietnam-ladies-escape'
    itin_slug = 'vn-005-vietnam-ladies-escape-itinerary'
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
            _ph('Serial code VN-005 | TRAGUIN tour code TRG-VNM-LAD-2026', 1),
            _ph('Country: Vietnam, Southeast Asia | Category: Premium Ladies Escape Tour Package', 2),
            _ph('Destinations: Hanoi Shopping • Boutique Stays • Culinary Masterclasses • Coastal Relaxation', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
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
        price_note='On Request (Premium Vietnam Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Vietnam Ladies Escape',
        overview='05 Nights / 06 Days Premium Vietnam Ladies Retreat SERIAL CODE: VN-005 TRAGUIN TOUR CODE: TRG-VNM-LAD-2026 STATE / COUNTRY: Vietnam CATEGORY: Premium Ladies Escape Tour Package DURATION: 05 Nights / 06 Days Hanoi & Coastal Sanctuary\n\nTOUR OVERVIEW\nRejuvenate, explore, and bond with our TRAGUIN curated Vietnam Ladies Escape. Designed for style and relaxation, this journey combines the chic boutiques of Hanoi, private culinary masterclasses, and ultimate coastal rejuvenation, ensuring unforgettable memories in the most elegant corners of Vietnam. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='VN-005 | Vietnam Ladies Escape | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Vietnam package (VN-005 / TRG-VNM-LAD-2026): Hanoi Shopping • Boutique Stays • Culinary Masterclasses • Coastal Relaxation with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN HANOI & STYLE WELCOME', 1),
            _ih('Day 02: CHIC SHOPPING & HANOI CHARM', 2),
            _ih('Day 03: CULINARY MASTERCLASS', 3),
            _ih('Day 04: COASTAL REJUVENATION', 4),
            _ih('Day 05: COASTAL LEISURE & FAREWELL GALA', 5),
            _ih('Day 06: DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN HANOI & STYLE WELCOME',
                (
                    'Arrive in Hanoi. Private chauffeur transfer to a handpicked boutique hotel. Evening welcome dinner in a stylish, garden-setting restaurant.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'CHIC SHOPPING & HANOI CHARM',
                (
                    'A guided tour of Hanoi’s hidden shopping gems and chic fashion boutiques. Perfect for a day of style and discovery, creating unforgettable memories. TRAGUIN Ladies Retreats •'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'CULINARY MASTERCLASS',
                (
                    'Join an exclusive experience culinary masterclass, learning to prepare authentic Vietnamese dishes in a beautiful, private garden setting.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'COASTAL REJUVENATION',
                (
                    'Transfer to a pristine coastal sanctuary. Spend the day indulging in personalized spa therapies and relaxation by the private beach—a premium retreat.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'COASTAL LEISURE & FAREWELL GALA',
                (
                    "Final day of coastal leisure and boutique shopping, followed by a grand farewell gala dinner under the stars, celebrating the perfect ladies' escape."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'DEPARTURE',
                (
                    'Final luxury breakfast before your TRAGUIN private chauffeur transfer to the airport, completing your premium Vietnam retreat.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Boutique Heritage Hotels Luxury Coastal Resort & Spa TRAGUIN Ladies Retreats •',
                'Multi-city Vietnam',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Boutique Heritage Hotels Luxury Coastal Resort & Spa TRAGUIN Ladies Retreats •',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Hanoi Shopping',
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
                'Hanoi Shopping',
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
                'Hanoi Shopping',
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
            _inc_included('Premium handpicked accommodation across Vietnam', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven executive van', 2),
            _inc_included('Inter-city transfers and curated sightseeing as per itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Vietnam visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_vn_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'VN-006'
    tour_code = 'TRG-VNM-HND-2026'
    title = 'Vietnam Family Highlights Tour'
    duration = '06 Nights / 07 Days'
    slug = 'vn-006-vietnam-family-highlights-tour'
    itin_slug = 'vn-006-vietnam-family-highlights-itinerary'
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
            _ph('Serial code VN-006 | TRAGUIN tour code TRG-VNM-HND-2026', 1),
            _ph('Country: Vietnam, Southeast Asia | Category: Best Vietnam Family Highlights Tour Package', 2),
            _ph('Destinations: Hanoi City • Halong Bay Cruise • Da Nang Coast • Hoi An Heritage', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Family', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Vietnam Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Vietnam Family Highlights Tour',
        overview='Hanoi City • Halong Bay Cruise • Da Nang Coast • Hoi An Heritage 06 Nights / 07 Days Classic Vietnam Family Explorer Expedition SERIAL CODE: VN-006 TRAGUIN TOUR CODE: TRG-VNM-HND-2026 STATE / COUNTRY: Vietnam CATEGORY: Best Vietnam Family Highlights Tour Package DURATION: 06 Nights / 07 Days Hanoi (2N) + Halong Bay (2N) + Da Nang/Hoi An (2N)\n\nTOUR OVERVIEW\nDiscover the absolute highlights of Vietnam with our TRAGUIN curated family expedition. From the historic northern charm of Hanoi and the emerald serenity of Halong Bay to the coastal beauty of Da Nang and Hoi An, this journey ensures your family creates unforgettable memories across the most iconic landscapes of Vietnam. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='VN-006 | Vietnam Family Highlights Tour | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Vietnam package (VN-006 / TRG-VNM-HND-2026): Hanoi City • Halong Bay Cruise • Da Nang Coast • Hoi An Heritage with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN HANOI & CITY VIBE', 1),
            _ih('Day 02: HANOI HERITAGE TOUR', 2),
            _ih('Day 03: HALONG BAY CRUISE', 3),
            _ih('Day 04: HALONG BAY ADVENTURE', 4),
            _ih('Day 05: FLIGHT TO DA NANG', 5),
            _ih('Day 06: HOI AN ANCIENT TOWN', 6),
            _ih('Day 07: DEPARTURE', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN HANOI & CITY VIBE',
                (
                    'Arrive in Hanoi. Private transfer to your handpicked premium hotel. Evening at leisure to enjoy the vibrant Old Quarter.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'HANOI HERITAGE TOUR',
                (
                    'A comprehensive city tour covering Hanoi’s most famous landmarks, providing a rich educational experience for your family.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'HALONG BAY CRUISE',
                (
                    'Travel to Halong Bay. Board your ultra-luxury cruise vessel for an extraordinary journey through the limestone karsts.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'HALONG BAY ADVENTURE',
                (
                    'Enjoy exclusive activities aboard the cruise, including cave exploration, kayaking, and sunset deck relaxation —creating unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'FLIGHT TO DA NANG',
                (
                    'Morning cruise brunch. Transfer to the airport for your flight to Da Nang. Check into a luxury coastal family resort.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'HOI AN ANCIENT TOWN',
                (
                    "Private guided tour of Hoi An's Ancient Town, famous for its unique architecture, lantern-lit streets, and traditional craft workshops."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'DEPARTURE',
                (
                    'Final luxury breakfast before your TRAGUIN private transfer to the airport, completing your premium Vietnam highlights expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Selected Heritage HotelsUltra-Luxury Cruise Luxury Coastal Family Resort',
                'Multi-city Vietnam',
                '6N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Selected Heritage HotelsUltra-Luxury Cruise Luxury Coastal Family Resort',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Hanoi City',
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
                'Hanoi City',
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
                'Hanoi City',
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
            _inc_included('Premium handpicked accommodation across Vietnam', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven executive van', 2),
            _inc_included('Inter-city transfers and curated sightseeing as per itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Vietnam visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_vn_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'VN-007'
    tour_code = 'TRG-VNM-HIG-2026'
    title = 'Vietnam Extended Highlights Tour'
    duration = '07 Nights / 08 Days'
    slug = 'vn-007-vietnam-extended-highlights-tour'
    itin_slug = 'vn-007-vietnam-extended-highlights-itinerary'
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
            _ph('Serial code VN-007 | TRAGUIN tour code TRG-VNM-HIG-2026', 1),
            _ph('Country: Vietnam, Southeast Asia | Category: Best Vietnam Family Highlights Tour Package', 2),
            _ph('Destinations: Hanoi • Halong Bay Cruise • Hoi An Ancient Town • Da Nang Beaches • Mekong Delta', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Family', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Vietnam Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Vietnam Extended Highlights Tour',
        overview="Hanoi • Halong Bay Cruise • Hoi An Ancient Town • Da Nang Beaches • Mekong Delta 07 Nights / 08 Days The Ultimate Vietnam Family Highlights Expedition SERIAL CODE: VN-007 TRAGUIN TOUR CODE: TRG-VNM-HIG-2026 STATE / COUNTRY: Vietnam CATEGORY: Best Vietnam Family Highlights Tour Package DURATION: 07 Nights / 08 Days Hanoi (2N) + Halong Bay (2N) + Hoi An/Da Nang (2N) + HCMC (1N)\n\nTOUR OVERVIEW\nDiscover the absolute highlights of Vietnam with our TRAGUIN curated family expedition. This comprehensive 8-day journey takes your family through the vibrant capital of Hanoi, the serene majesty of Halong Bay, the cultural charm of Hoi An, and the dynamic energy of Ho Chi Minh City—creating unforgettable memories across Vietnam's iconic landscapes. THE IMMERSIVE DAY-WISE ITINERARY",
        seo_title='VN-007 | Vietnam Extended Highlights Tour | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Vietnam package (VN-007 / TRG-VNM-HIG-2026): Hanoi • Halong Bay Cruise • Hoi An Ancient Town • Da Nang Beaches • Mekong Delta with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN HANOI', 1),
            _ih('Day 02: HANOI CULTURAL HIGHLIGHTS', 2),
            _ih('Day 03: HALONG BAY CRUISE', 3),
            _ih('Day 04: HALONG BAY ADVENTURE', 4),
            _ih('Day 05: FLIGHT TO DA NANG', 5),
            _ih('Day 06: HOI AN ANCIENT TOWN', 6),
            _ih('Day 07: HO CHI MINH CITY DISCOVERY', 7),
            _ih('Day 08: DEPARTURE', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN HANOI',
                (
                    'Arrive in Hanoi. Private transfer to your handpicked premium hotel. Evening at leisure to enjoy the historic Old Quarter.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'HANOI CULTURAL HIGHLIGHTS',
                (
                    'A comprehensive city tour covering Hanoi’s most famous landmarks, providing a rich educational experience for your family.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'HALONG BAY CRUISE',
                (
                    'Travel to Halong Bay. Board your ultra-luxury cruise vessel for an extraordinary journey through the limestone karsts.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'HALONG BAY ADVENTURE',
                (
                    'Enjoy exclusive activities aboard the cruise, including cave exploration, kayaking, and sunset deck relaxation —creating unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'FLIGHT TO DA NANG',
                (
                    'Morning cruise brunch. Transfer to the airport for your flight to Da Nang. Check into a luxury coastal family resort.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'HOI AN ANCIENT TOWN',
                (
                    "Private guided tour of Hoi An's Ancient Town, famous for its unique architecture, lantern-lit streets, and traditional craft workshops."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'HO CHI MINH CITY DISCOVERY',
                (
                    'Flight to Ho Chi Minh City. Evening city orientation and final farewell gala dinner—an exclusive experience for the family.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                8,
                'DEPARTURE',
                (
                    'Final luxury breakfast before your TRAGUIN private transfer to the airport, completing your premium Vietnam highlights expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Selected Heritage Hotels Ultra-Luxury Cruise Luxury Coastal Family Resort City Center Luxury Hotel',
                'Multi-city Vietnam',
                '7N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Selected Heritage Hotels Ultra-Luxury Cruise Luxury Coastal Family Resort City Center Luxury Hotel',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Hanoi',
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
                'Hanoi',
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
                'Hanoi',
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
            _inc_included('Premium handpicked accommodation across Vietnam', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven executive van', 2),
            _inc_included('Inter-city transfers and curated sightseeing as per itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Vietnam visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_vn_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'VN-008'
    tour_code = 'TRG-VNM-ADV-2026'
    title = 'Vietnam Adventure Expedition'
    duration = '06 Nights / 07 Days'
    slug = 'vn-008-vietnam-adventure-expedition-tour'
    itin_slug = 'vn-008-vietnam-adventure-itinerary'
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
            _ph('Serial code VN-008 | TRAGUIN tour code TRG-VNM-ADV-2026', 1),
            _ph('Country: Vietnam, Southeast Asia | Category: Premium Vietnam Adventure Tour Package', 2),
            _ph('Destinations: Northern Wilderness • Sapa Trekking • Halong Bay Expedition • Off-Road Exploration', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Vietnam Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Vietnam Adventure Expedition',
        overview="Northern Wilderness • Sapa Trekking • Halong Bay Expedition • Off-Road Exploration 06 Nights / 07 Days High-Octane Vietnam Adventure Expedition SERIAL CODE: VN-008 TRAGUIN TOUR CODE: TRG-VNM-ADV-2026 STATE / COUNTRY: Vietnam CATEGORY: Premium Vietnam Adventure Tour Package DURATION: 06 Nights / 07 Days Hanoi, Sapa & Northern Highlands\n\nTOUR OVERVIEW\nPush your boundaries with our TRAGUIN curated Vietnam Adventure Expedition. Designed for true thrill- seekers, this itinerary plunges into the northern wilderness, featuring rugged mountain trekking in Sapa, off- road exploration through remote landscapes, and intensive nature discovery, ensuring unforgettable memories in Vietnam's untamed heart. THE IMMERSIVE DAY-WISE ITINERARY",
        seo_title='VN-008 | Vietnam Adventure Expedition | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Vietnam package (VN-008 / TRG-VNM-ADV-2026): Northern Wilderness • Sapa Trekking • Halong Bay Expedition • Off-Road Exploration with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN HANOI & BRIEFING', 1),
            _ih('Day 02: JOURNEY TO SAPA HIGHLANDS', 2),
            _ih('Day 03: SAPA MOUNTAIN TREKKING', 3),
            _ih('Day 04: WILDERNESS OFF-ROAD EXPLORATION', 4),
            _ih('Day 05: HALONG BAY ADVENTURE', 5),
            _ih('Day 06: EXTREME MARINE ACTIVITIES', 6),
            _ih('Day 07: DEPARTURE', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN HANOI & BRIEFING',
                (
                    'Arrive in Hanoi. Expedition gear check and briefing. Private transfer to your wilderness-ready lodge.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'JOURNEY TO SAPA HIGHLANDS',
                (
                    'Drive to the Sapa highlands. Immerse yourself in the mountainous terrain, preparing for your multi-day rugged adventure. TRAGUIN Adventure'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'SAPA MOUNTAIN TREKKING',
                (
                    'Intensive guided trek through remote Sapa trails. Experience local tribal life and breathtaking high-altitude vistas.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'WILDERNESS OFF-ROAD EXPLORATION',
                (
                    'Engage in an exclusive experience of off-road vehicle exploration through remote northern valleys, a highlight for serious adventure lovers.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'HALONG BAY ADVENTURE',
                (
                    'Transfer to Halong Bay. Kayak through hidden sea caves and explore remote islands on a premium adventure cruise vessel.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'EXTREME MARINE ACTIVITIES',
                (
                    'A full day of intense marine exploration, from swimming in hidden bays to cliff-side discovery. Celebrating with a celebratory adventure dinner gala.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'DEPARTURE',
                (
                    'Final breakfast before your TRAGUIN private transfer, completing your high-octane Vietnam adventure. HANDPICKED ADVENTURE STAYS Category Sapa & Highlands (3N) Halong Bay (3N) Option 01: Premium Highland Adventure Lodges Premium Adventure Cruise PREMIUM TRAVEL | ADVENTURE HOLIDAYS | CORPORATE MICE | HONEYMOON EXPERTS | FAMILY VACATIONS TRAGUIN Adventure Travel •'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Highland Adventure Lodges Premium Adventure Cruise',
                'Vietnam',
                '6N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Highland Adventure Lodges Premium Adventure Cruise',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Northern Wilderness',
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
                'Northern Wilderness',
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
                'Northern Wilderness',
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
            _inc_included('Premium handpicked accommodation across Vietnam', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven executive van', 2),
            _inc_included('Inter-city transfers and curated sightseeing as per itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Vietnam visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_vn_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'VN-009'
    tour_code = 'TRG-VNM-SEN-2026'
    title = 'Vietnam Senior Leisure Tour'
    duration = '06 Nights / 07 Days'
    slug = 'vn-009-vietnam-senior-leisure-tour'
    itin_slug = 'vn-009-vietnam-senior-leisure-itinerary'
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
            _ph('Serial code VN-009 | TRAGUIN tour code TRG-VNM-SEN-2026', 1),
            _ph('Country: Vietnam, Southeast Asia | Category: Premium Senior- Friendly Vietnam Tour Package', 2),
            _ph('Destinations: Hanoi Cultural Leisure • Halong Bay Scenic Cruise • Da Nang Comfort', 3),
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
        price_note='On Request (Premium Vietnam Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Vietnam Senior Leisure Tour',
        overview='Hanoi Cultural Leisure • Halong Bay Scenic Cruise • Da Nang Comfort 06 Nights / 07 Days Relaxing Vietnam Senior-Friendly Leisure Expedition SERIAL CODE: VN-009 TRAGUIN TOUR CODE: TRG-VNM-SEN-2026 STATE / COUNTRY: Vietnam CATEGORY: Premium Senior- Friendly Vietnam Tour Package DURATION: 06 Nights / 07 Days Hanoi (2N) + Halong Bay (2N) + Da Nang/Hoi An (2N)\n\nTOUR OVERVIEW\nEnjoy a comfortable, relaxed, and culturally enriching experience in Vietnam with this TRAGUIN curated leisure itinerary. Specifically designed for senior citizens, this Vietnam Leisure Sojourn prioritizes comfort, slow-paced sightseeing, and easy access to local culture, guaranteeing unforgettable memories in the serene and beautiful settings of Vietnam. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='VN-009 | Vietnam Senior Leisure Tour | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Vietnam package (VN-009 / TRG-VNM-SEN-2026): Hanoi Cultural Leisure • Halong Bay Scenic Cruise • Da Nang Comfort with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: COMFORTABLE ARRIVAL IN HANOI', 1),
            _ih('Day 02: HANOI CULTURAL DISCOVERY', 2),
            _ih('Day 03: HALONG BAY SCENIC CRUISE', 3),
            _ih('Day 04: RELAXED BAY EXPLORATION', 4),
            _ih('Day 05: FLIGHT TO DA NANG', 5),
            _ih('Day 06: HOI AN LEISURE', 6),
            _ih('Day 07: DEPARTURE', 7)
        ],
        days=[
            _day(
                1,
                'COMFORTABLE ARRIVAL IN HANOI',
                (
                    'Arrive in Hanoi. Private chauffeur transfer to your premium hotel. Evening at leisure, savoring the calm charm of the city. TRAGUIN Senior'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'HANOI CULTURAL DISCOVERY',
                (
                    'A gentle city tour covering significant historical landmarks at a relaxed, senior-friendly pace. Perfect for cultural enrichment.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'HALONG BAY SCENIC CRUISE',
                (
                    'Transfer to Halong Bay. Board your ultra-luxury cruise for a peaceful journey through the scenic limestone islands.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'RELAXED BAY EXPLORATION',
                (
                    'Enjoy serene views, gentle activities, and relaxation on the deck. A perfect day for creating unforgettable memories in total comfort.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'FLIGHT TO DA NANG',
                (
                    'Morning cruise brunch. Transfer to the airport for your flight to Da Nang. Check into a comfortable luxury coastal resort.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'HOI AN LEISURE',
                (
                    'A gentle, relaxed visit to Hoi An’s Ancient Town. Explore at your own pace and enjoy the serene beauty of this heritage site.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'DEPARTURE',
                (
                    'Final luxury breakfast before your TRAGUIN private chauffeur transfers you comfortably to the airport, completing your premium Vietnam leisure expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Selected Senior-Friendly HotelsPremium Leisure CruiseLuxury Coastal Resort TRAGUIN Senior Travel • TRAGUIN Senior Travel •',
                'Multi-city Vietnam',
                '6N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Selected Senior-Friendly HotelsPremium Leisure CruiseLuxury Coastal Resort TRAGUIN Senior Travel • TRAGUIN Senior Travel',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Hanoi Cultural Leisure',
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
                'Hanoi Cultural Leisure',
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
                'Hanoi Cultural Leisure',
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
            _inc_included('Premium handpicked accommodation across Vietnam', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven executive van', 2),
            _inc_included('Inter-city transfers and curated sightseeing as per itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Vietnam visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_vn_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'VN-010'
    tour_code = 'TRG-VNM-GRD-2026'
    title = 'Grand Vietnam Tour'
    duration = '08 Nights / 09 Days'
    slug = 'vn-010-grand-vietnam-tour'
    itin_slug = 'vn-010-grand-vietnam-itinerary'
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
            _ph('Serial code VN-010 | TRAGUIN tour code TRG-VNM-GRD-2026', 1),
            _ph('Country: Vietnam, Southeast Asia | Category: Premium Grand Vietnam Tour Package', 2),
            _ph('Destinations: Hanoi • Halong Bay Cruise • Hoi An • Da Nang • Ho Chi Minh City • Mekong Delta', 3),
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
        price_note='On Request (Premium Vietnam Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Grand Vietnam Tour',
        overview='08 Nights / 09 Days Grand Vietnam Premium Expedition SERIAL CODE: VN-010 TRAGUIN TOUR CODE: TRG-VNM-GRD-2026 STATE / COUNTRY: Vietnam CATEGORY: Premium Grand Vietnam Tour Package DURATION: 08 Nights / 09 Days Hanoi (2N) + Halong (2N) + Da Nang/Hoi An (2N) + Ho Chi Minh (2N)\n\nTOUR OVERVIEW\nExperience the ultimate discovery of Vietnam with our TRAGUIN curated Grand Expedition. This comprehensive 9-day journey covers the most iconic destinations across Vietnam—from the cultural heart of Hanoi and serene Halong Bay to the coastal magic of Hoi An and the vibrant energy of Ho Chi Minh City, ensuring unforgettable memories in ultimate comfort. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='VN-010 | Grand Vietnam Tour | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days Vietnam package (VN-010 / TRG-VNM-GRD-2026): Hanoi • Halong Bay Cruise • Hoi An • Da Nang • Ho Chi Minh City • Mekong Delta with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN HANOI', 1),
            _ih('Day 02: HANOI CULTURAL HIGHLIGHTS', 2),
            _ih('Day 03: HALONG BAY CRUISE COMMENCEMENT', 3),
            _ih('Day 04: HALONG BAY ADVENTURE', 4),
            _ih('Day 05: FLIGHT TO DA NANG', 5),
            _ih('Day 06: HOI AN ANCIENT TOWN', 6),
            _ih('Day 07: FLIGHT TO HO CHI MINH CITY', 7),
            _ih('Day 08: MEKONG DELTA EXPLORATION', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN HANOI',
                (
                    'Arrive in Hanoi. Private transfer to your handpicked premium hotel. Evening at leisure.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'HANOI CULTURAL HIGHLIGHTS',
                (
                    'Comprehensive city tour covering Hanoi’s most famous landmarks, providing a rich educational experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'HALONG BAY CRUISE COMMENCEMENT',
                (
                    'Travel to Halong Bay. Board your ultra-luxury cruise vessel for an extraordinary journey through the limestone karsts.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'HALONG BAY ADVENTURE',
                (
                    'Enjoy exclusive activities aboard the cruise, including cave exploration, kayaking, and sunset deck relaxation —creating unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'FLIGHT TO DA NANG',
                (
                    'Morning cruise brunch. Transfer to airport for your flight to Da Nang. Check into a luxury coastal resort.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'HOI AN ANCIENT TOWN',
                (
                    "Guided tour of Hoi An's Ancient Town, famous for its unique architecture and lantern-lit streets."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'FLIGHT TO HO CHI MINH CITY',
                (
                    'Transfer to Da Nang airport for flight to Ho Chi Minh City. Evening city orientation and luxury dining.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                8,
                'MEKONG DELTA EXPLORATION',
                (
                    'Private full-day excursion to the Mekong Delta, experiencing the lush waterways and local life in an exclusive experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                9,
                'DEPARTURE',
                (
                    'Final luxury breakfast before your TRAGUIN private transfer, completing your premium grand Vietnam expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Heritage Hotels Ultra-Luxury Cruise Luxury Resort Premium City Hotel',
                'Multi-city Vietnam',
                '8N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Premium — Heritage Hotels Ultra-Luxury Cruise Luxury Resort Premium City Hotel',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Hanoi',
                '8N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: TRAGUIN Handpicked Premium Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Luxury Property',
                'Hanoi',
                '8N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Hanoi',
                '8N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Vietnam', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven executive van', 2),
            _inc_included('Inter-city transfers and curated sightseeing as per itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and Vietnam visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

VIETNAM_VN_001_010_BUILDERS = [
    build_vn_001,
    build_vn_002,
    build_vn_003,
    build_vn_004,
    build_vn_005,
    build_vn_006,
    build_vn_007,
    build_vn_008,
    build_vn_009,
    build_vn_010,
]
