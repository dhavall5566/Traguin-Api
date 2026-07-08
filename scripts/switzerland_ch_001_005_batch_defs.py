"""Builder functions for CH-001 through CH-005 Switzerland international packages."""

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

SWITZERLAND_SLUG = "switzerland"


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


def build_ch_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'CH-001'
    db_serial = 'SW-001'
    tour_code = 'TRG-SWI-HIG-2026'
    title = 'Swiss Highlights Family Tour'
    duration = '06 Nights / 07 Days'
    slug = 'ch-001-swiss-highlights-family-tour'
    itin_slug = 'ch-001-swiss-highlights-itinerary'
    package = PackageCreate(
        slug=slug,
        serial_code=db_serial,
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
            _ph('Serial code CH-001 | TRAGUIN tour code TRG-SWI-HIG-2026', 1),
            _ph('Country: Switzerland | Category: Best Swiss Highlights Family Tour Package', 2),
            _ph('Destinations: Zurich • Lucerne • Mt. Titlis • Interlaken • Swiss Alps • Scenic Rail Journeys', 3),
            _ph('Best season: October to March', 4),
            _ph('Starting price: On Request', 5)
        ],
        moods=['Family'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Switzerland Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Zurich • Lucerne • Mt. Titlis • Interlaken • Swiss Alps • Scenic Rail Journeys',
        overview='Zurich • Lucerne • Mt. Titlis • Interlaken • Swiss Alps • Scenic Rail Journeys 06 Nights / 07 Days Comprehensive Swiss Highlights Family Expedition SERIAL CODE: CH-001 TRAGUIN TOUR CODE: TRG-SWI-HIG-2026 STATE / COUNTRY: Switzerland CATEGORY: Best Swiss Highlights Family Tour Package DURATION: 06 Nights / 07 Days Zurich (1N) + Lucerne (2N) + Interlaken (3N)\n\nTOUR OVERVIEW\nDiscover the breathtaking beauty of the Swiss Alps with our TRAGUIN curated family expedition. This comprehensive journey takes your family through pristine lakes, majestic peaks, and scenic rail journeys, ensuring unforgettable memories in the most stunning landscapes of Switzerland. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='CH-001 | Swiss Highlights Family Tour | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Switzerland package (CH-001 / TRG-SWI-HIG-2026): Zurich • Lucerne • Mt. Titlis • Interlaken • Swiss Alps • Scenic Rail Journeys.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN ZURICH', 1),
            _ih('Day 02: TRANSFER TO LUCERNE', 2),
            _ih('Day 03: MT. TITLIS ADVENTURE', 3),
            _ih('Day 04: TRANSFER TO INTERLAKEN', 4),
            _ih('Day 05: JUNGFRAUJOCH EXCURSION', 5),
            _ih('Day 06: ALPINE LEISURE & EXPLORATION', 6),
            _ih('Day 07: DEPARTURE', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN ZURICH',
                (
                    'Arrive in Zurich. Private transfer to your handpicked premium hotel. Evening at leisure to enjoy the city’s sophisticated charm.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'TRANSFER TO LUCERNE',
                (
                    'Scenic transfer to Lucerne. Visit the iconic Chapel Bridge and take a peaceful lake cruise, a classic Swiss experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'MT. TITLIS ADVENTURE',
                (
                    'Ascend to Mt. Titlis by cable car. Enjoy snow activities at the summit, creating unforgettable memories for your family.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'TRANSFER TO INTERLAKEN',
                (
                    'Transfer to Interlaken, the adventure heart of Switzerland. Check into your luxury alpine retreat.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'JUNGFRAUJOCH EXCURSION',
                (
                    'A spectacular journey to Jungfraujoch—the Top of Europe. Experience breathtaking panoramic views and high-altitude excitement.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'ALPINE LEISURE & EXPLORATION',
                (
                    'A day of leisure or gentle exploration in the scenic surroundings, perfect for family bonding in the Swiss Alps.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'DEPARTURE',
                (
                    'Final luxury breakfast before your TRAGUIN private transfer to the airport, completing your premium Swiss highlights expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Premium Luxury City Hotel / similar',
                'Zurich',
                '1N',
                'Premium',
                'Deluxe Room',
                'Breakfast',
                5,
                1,
                description='OPTION 01 – PREMIUM: Premium Luxury City Hotel',
            ),
            _hotel(
                'Premium Lake View Hotel / similar',
                'Lucerne',
                '2N',
                'Premium',
                'Deluxe Room',
                'Breakfast',
                5,
                2,
                description='OPTION 02 – PREMIUM: Premium Lake View Hotel',
            ),
            _hotel(
                'Luxury Alpine Retreat / similar',
                'Interlaken',
                '3N',
                'Premium',
                'Deluxe Room',
                'Breakfast',
                5,
                3,
                description='OPTION 03 – PREMIUM: Luxury Alpine Retreat',
            )
        ],
        inclusions=[
            _inc_included('06 Nights in handpicked premium hotels across Zurich • Lucerne • Mt. Titlis • Interlaken • Swiss Alps • Scenic Rail Journeys', 1),
            _inc_included('Private executive chauffeur-driven luxury ground transfers throughout', 2),
            _inc_included('Mt. Titlis cable car ascent with summit snow activities', 3),
            _inc_included('Jungfraujoch — Top of Europe excursion', 4),
            _inc_included('Lucerne lake cruise and Chapel Bridge sightseeing', 5),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 6),
            _inc_excluded('International airfare and Switzerland entry visa processing fees', 7),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 8),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 9),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 10),
        ],
    )
    return package, itinerary

def build_ch_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'CH-002'
    db_serial = 'SW-002'
    tour_code = 'TRG-SWI-ROM-2026'
    title = 'Romantic Switzerland Honeymoon'
    duration = '07 Nights / 08 Days'
    slug = 'ch-002-romantic-switzerland-honeymoon'
    itin_slug = 'ch-002-romantic-switzerland-itinerary'
    package = PackageCreate(
        slug=slug,
        serial_code=db_serial,
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
            _ph('Serial code CH-002 | TRAGUIN tour code TRG-SWI-ROM-2026', 1),
            _ph('Country: Switzerland | Category: Premium Honeymoon Couple Tour Package', 2),
            _ph('Destinations: Lucerne Romantic Charm • Mt. Pilatus Sunset • Interlaken Alpine Retreat • Zermatt', 3),
            _ph('Best season: October to March', 4),
            _ph('Starting price: On Request', 5)
        ],
        moods=['Romantic', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Switzerland Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Lucerne Romantic Charm • Mt. Pilatus Sunset • Interlaken Alpine Retreat • Zermatt',
        overview='Lucerne Romantic Charm • Mt. Pilatus Sunset • Interlaken Alpine Retreat • Zermatt Luxury 07 Nights / 08 Days Ultimate Romantic Swiss Couple Sanctuary SERIAL CODE: CH-002 TRAGUIN TOUR CODE: TRG-SWI-ROM-2026 STATE / COUNTRY: Switzerland CATEGORY: Premium Honeymoon Couple Tour Package DURATION: 07 Nights / 08 Days Lucerne (2N) + Interlaken (3N) + Zermatt (2N)\n\nTOUR OVERVIEW\nBegin your life together in the most breathtaking landscape on earth. This TRAGUIN curated Swiss honeymoon sanctuary is designed for intimacy, luxury, and awe-inspiring beauty—perfectly balancing cozy alpine retreats, scenic romantic excursions, and world-class hospitality, ensuring unforgettable memories. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='CH-002 | Romantic Switzerland Honeymoon | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Switzerland package (CH-002 / TRG-SWI-ROM-2026): Lucerne Romantic Charm • Mt. Pilatus Sunset • Interlaken Alpine Retreat • Zermatt.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL & INTIMATE LUCERNE WELCOME', 1),
            _ih('Day 02: MT. PILATUS SUNSET EXPERIENCE', 2),
            _ih('Day 03: TRANSFER TO INTERLAKEN', 3),
            _ih('Day 04: JUNGFRAUJOCH ROMANCE', 4),
            _ih('Day 05: ALPINE LAKES & LEISURE', 5),
            _ih('Day 06: ZERMATT LUXURY ESCAPE', 6),
            _ih('Day 07: MATTERHORN CELEBRATION', 7),
            _ih('Day 08: DEPARTURE', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL & INTIMATE LUCERNE WELCOME',
                (
                    'Arrive in Zurich and private chauffeur transfer to Lucerne. Check into your romantic lakeside suite. Evening lakeside walk and intimate welcome dinner.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'MT. PILATUS SUNSET EXPERIENCE',
                (
                    'A gentle day in Lucerne, followed by a sunset excursion to Mt. Pilatus. Witness the spectacular alpine panorama—an exclusive romantic experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'TRANSFER TO INTERLAKEN',
                (
                    'Scenic train transfer to Interlaken. Check into your luxury alpine retreat with mountain views, perfect for couples.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'JUNGFRAUJOCH ROMANCE',
                (
                    'A spectacular journey to the Top of Europe. Enjoy a private photo session amidst the pristine snow—creating unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'ALPINE LAKES & LEISURE',
                (
                    'Leisure day in Interlaken. Enjoy a private boat excursion on Lake Brienz, soaking in the serene mountain beauty together.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'ZERMATT LUXURY ESCAPE',
                (
                    'Transfer to Zermatt. Check into your ultra-luxury boutique suite with iconic Matterhorn views.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'MATTERHORN CELEBRATION',
                (
                    'Enjoy a day of private leisure and spa treatments in Zermatt, followed by a candlelit farewell dinner celebrating your romantic honeymoon.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                8,
                'DEPARTURE',
                (
                    'Final luxury breakfast before your TRAGUIN private chauffeur transfer to the airport, completing your premium Swiss honeymoon.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Premium Luxury Lakeside Suites / similar',
                'Lucerne',
                '2N',
                'Premium',
                'Deluxe Room',
                'Breakfast',
                5,
                1,
                description='OPTION 01 – PREMIUM: Premium Luxury Lakeside Suites',
            ),
            _hotel(
                'Ultra-Luxury Alpine Resort / similar',
                'Interlaken',
                '3N',
                'Premium',
                'Deluxe Room',
                'Breakfast',
                5,
                2,
                description='OPTION 02 – PREMIUM: Ultra-Luxury Alpine Resort',
            ),
            _hotel(
                'Luxury Matterhorn-View Suites / similar',
                'Zermatt',
                '2N',
                'Premium',
                'Deluxe Room',
                'Breakfast',
                5,
                3,
                description='OPTION 03 – PREMIUM: Luxury Matterhorn-View Suites',
            )
        ],
        inclusions=[
            _inc_included('07 Nights in handpicked premium hotels across Lucerne Romantic Charm • Mt. Pilatus Sunset • Interlaken Alpine Retreat • Zermatt', 1),
            _inc_included('Private executive chauffeur-driven luxury ground transfers throughout', 2),
            _inc_included('Jungfraujoch — Top of Europe excursion', 3),
            _inc_included('Mt. Pilatus sunset excursion with alpine panorama', 4),
            _inc_included('Matterhorn-view luxury stay and exploration in Zermatt', 5),
            _inc_included('Lake Brienz leisure and private boat excursion', 6),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 7),
            _inc_excluded('International airfare and Switzerland entry visa processing fees', 8),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 9),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 10),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 11),
        ],
    )
    return package, itinerary

def build_ch_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'CH-003'
    db_serial = 'SW-003'
    tour_code = 'TRG-SWI-LUX-2026'
    title = 'Luxury Switzerland Tour'
    duration = '08 Nights / 09 Days'
    slug = 'ch-003-luxury-switzerland-tour'
    itin_slug = 'ch-003-luxury-switzerland-itinerary'
    package = PackageCreate(
        slug=slug,
        serial_code=db_serial,
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
            _ph('Serial code CH-003 | TRAGUIN tour code TRG-SWI-LUX-2026', 1),
            _ph('Country: Switzerland | Category: Ultra-Luxury Switzerland Tour Package', 2),
            _ph('Destinations: Zurich Luxury • Lucerne Grandeur • Interlaken Alpine Retreat • Zermatt Elite • Exclusive', 3),
            _ph('Best season: October to March', 4),
            _ph('Starting price: On Request', 5)
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
        price_note='On Request (Premium Switzerland Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Zurich Luxury • Lucerne Grandeur • Interlaken Alpine Retreat • Zermatt Elite • Exclusive',
        overview='Zurich Luxury • Lucerne Grandeur • Interlaken Alpine Retreat • Zermatt Elite • Exclusive Rail Journeys 08 Nights / 09 Days Ultra-Luxury Switzerland Expedition SERIAL CODE: CH-003 TRAGUIN TOUR CODE: TRG-SWI-LUX-2026 STATE / COUNTRY: Switzerland CATEGORY: Ultra-Luxury Switzerland Tour Package DURATION: 08 Nights / 09 Days Zurich (2N) + Lucerne (2N) + Interlaken (3N) + Zermatt (2N)\n\nTOUR OVERVIEW\nIndulge in the absolute height of sophistication across Switzerland with our TRAGUIN curated luxury expedition. From opulent five-star stays and world-class alpine resorts to exclusive private rail journeys and elite culinary experiences, this journey is designed for the discerning traveler, ensuring unforgettable memories in ultimate luxury. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='CH-003 | Luxury Switzerland Tour | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days Switzerland package (CH-003 / TRG-SWI-LUX-2026): Zurich Luxury • Lucerne Grandeur • Interlaken Alpine Retreat • Zermatt Elite • Exclusive.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: VIP ARRIVAL & ZURICH LUXURY', 1),
            _ih('Day 02: EXCLUSIVE ZURICH DISCOVERY', 2),
            _ih('Day 03: TRANSFER TO LUCERNE', 3),
            _ih('Day 04: MT. TITLIS EXCLUSIVE ACCESS', 4),
            _ih('Day 05: SCENIC RAIL TO INTERLAKEN', 5),
            _ih('Day 06: JUNGFRAUJOCH VIP EXPEDITION', 6),
            _ih('Day 07: TRANSFER TO ZERMATT', 7),
            _ih('Day 08: MATTERHORN ELITE EXPERIENCE', 8)
        ],
        days=[
            _day(
                1,
                'VIP ARRIVAL & ZURICH LUXURY',
                (
                    'Arrive in Zurich. VIP chauffeur transfer to your world-class hotel. Evening gourmet welcome dinner overlooking the lake.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'EXCLUSIVE ZURICH DISCOVERY',
                (
                    'Private guided tour of Zurich’s most prestigious districts, boutique shopping, and cultural landmarks—an exclusive experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'TRANSFER TO LUCERNE',
                (
                    'VIP transfer to Lucerne. Check into a premium lakeside palace hotel. Afternoon private lake cruise with gourmet catering.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'MT. TITLIS EXCLUSIVE ACCESS',
                (
                    'Private cable car access to Mt. Titlis summit. Enjoy personal guiding, premium snow experiences, and gourmet dining at the top.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'SCENIC RAIL TO INTERLAKEN',
                (
                    'Embark on an exclusive experience luxury scenic rail journey to Interlaken. Check into an ultra-luxury alpine retreat.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'JUNGFRAUJOCH VIP EXPEDITION',
                (
                    'Private VIP expedition to Jungfraujoch—the Top of Europe. Enjoy personalized guiding and unparalleled panoramic views.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'TRANSFER TO ZERMATT',
                (
                    'Transfer to Zermatt. Check into an ultra-luxury boutique suite with iconic Matterhorn views.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                8,
                'MATTERHORN ELITE EXPERIENCE',
                (
                    'Private leisure day in Zermatt, boutique shopping, and a farewell gala dinner celebrating your luxury Swiss expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                9,
                'DEPARTURE',
                (
                    'Final luxury breakfast. VIP chauffeur transfer to the airport, concluding your premium Switzerland luxury expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Baur au Lac / similar',
                'Zurich',
                '2N',
                'Ultra Luxury',
                'Deluxe Room',
                'Breakfast',
                5,
                1,
                description='OPTION 01 – ULTRA LUXURY: Baur au Lac',
            ),
            _hotel(
                'Bürgenstock Resort / similar',
                'Lucerne',
                '2N',
                'Ultra Luxury',
                'Deluxe Room',
                'Breakfast',
                5,
                2,
                description='OPTION 02 – ULTRA LUXURY: Bürgenstock Resort',
            ),
            _hotel(
                'Victoria-Jungfrau Grand / similar',
                'Interlaken',
                '3N',
                'Ultra Luxury',
                'Deluxe Room',
                'Breakfast',
                5,
                3,
                description='OPTION 03 – ULTRA LUXURY: Victoria-Jungfrau Grand',
            ),
            _hotel(
                'The Omnia / similar',
                'Zermatt',
                '2N',
                'Ultra Luxury',
                'Deluxe Room',
                'Breakfast',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Omnia',
            )
        ],
        inclusions=[
            _inc_included('08 Nights in handpicked premium hotels across Zurich Luxury • Lucerne Grandeur • Interlaken Alpine Retreat • Zermatt Elite • Exclusive', 1),
            _inc_included('Private executive chauffeur-driven luxury ground transfers throughout', 2),
            _inc_included('Mt. Titlis cable car ascent with summit snow activities', 3),
            _inc_included('Jungfraujoch — Top of Europe excursion', 4),
            _inc_included('Lucerne lake cruise and Chapel Bridge sightseeing', 5),
            _inc_included('Matterhorn-view luxury stay and exploration in Zermatt', 6),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 7),
            _inc_excluded('International airfare and Switzerland entry visa processing fees', 8),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 9),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 10),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 11),
        ],
    )
    return package, itinerary

def build_ch_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'CH-004'
    db_serial = 'SW-004'
    tour_code = 'TRG-SWI-JUN-2026'
    title = 'Jungfrau Explorer Family Tour'
    duration = '06 Nights / 07 Days'
    slug = 'ch-004-jungfrau-explorer-family-tour'
    itin_slug = 'ch-004-jungfrau-explorer-family-tour-itinerary'
    package = PackageCreate(
        slug=slug,
        serial_code=db_serial,
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
            _ph('Serial code CH-004 | TRAGUIN tour code TRG-SWI-JUN-2026', 1),
            _ph('Country: Switzerland | Category: Best Jungfrau Family Explorer Tour Package', 2),
            _ph('Destinations: Zurich • Interlaken • Jungfraujoch • Lauterbrunnen • Alpine Adventures', 3),
            _ph('Best season: October to March', 4),
            _ph('Starting price: On Request', 5)
        ],
        moods=['Family', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Switzerland Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Zurich • Interlaken • Jungfraujoch • Lauterbrunnen • Alpine Adventures',
        overview='Zurich • Interlaken • Jungfraujoch • Lauterbrunnen • Alpine Adventures 06 Nights / 07 Days Comprehensive Jungfrau Family Explorer Expedition SERIAL CODE: CH-004 TRAGUIN TOUR CODE: TRG-SWI-JUN-2026 STATE / COUNTRY: Switzerland CATEGORY: Best Jungfrau Family Explorer Tour Package DURATION: 06 Nights / 07 Days Zurich (1N) + Interlaken (5N)\n\nTOUR OVERVIEW\nDiscover the majesty of the Jungfrau region with our TRAGUIN curated family explorer expedition. From the vibrant city of Zurich to the breathtaking alpine landscapes of Interlaken and the legendary Jungfraujoch, this journey ensures your family creates unforgettable memories in the heart of the Swiss Alps. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='CH-004 | Jungfrau Explorer Family Tour | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Switzerland package (CH-004 / TRG-SWI-JUN-2026): Zurich • Interlaken • Jungfraujoch • Lauterbrunnen • Alpine Adventures.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN ZURICH', 1),
            _ih('Day 02: TRANSFER TO INTERLAKEN', 2),
            _ih('Day 03: JUNGFRAUJOCH EXCURSION', 3),
            _ih('Day 04: LAUTERBRUNNEN & VALLEY VIEWS', 4),
            _ih('Day 05: ALPINE ADVENTURE DAY', 5),
            _ih('Day 06: LAKE BRIENZ LEISURE', 6),
            _ih('Day 07: DEPARTURE', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN ZURICH',
                (
                    'Arrive in Zurich. Private transfer to your handpicked premium hotel. Evening at leisure to enjoy the sophisticated city vibe.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'TRANSFER TO INTERLAKEN',
                (
                    'Scenic transfer to Interlaken, nestled between two stunning lakes. Check into your luxury alpine family retreat.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'JUNGFRAUJOCH EXCURSION',
                (
                    'A spectacular journey to Jungfraujoch—the Top of Europe. Experience breathtaking panoramic views, perfect for family discovery.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'LAUTERBRUNNEN & VALLEY VIEWS',
                (
                    'Explore the stunning Lauterbrunnen Valley, known for its dramatic waterfalls and alpine charm—creating unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'ALPINE ADVENTURE DAY',
                (
                    'Enjoy a day of high-altitude adventure, including scenic cable car rides or easy family treks through the glorious mountain landscape.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'LAKE BRIENZ LEISURE',
                (
                    'A relaxing day exploring Lake Brienz or enjoying a gentle boat tour, celebrating your premium Swiss family expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'DEPARTURE',
                (
                    'Final luxury breakfast before your TRAGUIN private transfer to the airport, completing your premium Jungfrau explorer expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Premium Luxury City Hotel / similar',
                'Zurich',
                '1N',
                'Premium',
                'Deluxe Room',
                'Breakfast',
                5,
                1,
                description='OPTION 01 – PREMIUM: Premium Luxury City Hotel',
            ),
            _hotel(
                'Luxury Alpine Family Resort / similar',
                'Interlaken',
                '5N',
                'Premium',
                'Deluxe Room',
                'Breakfast',
                5,
                2,
                description='OPTION 02 – PREMIUM: Luxury Alpine Family Resort',
            )
        ],
        inclusions=[
            _inc_included('06 Nights in handpicked premium hotels across Zurich • Interlaken • Jungfraujoch • Lauterbrunnen • Alpine Adventures', 1),
            _inc_included('Private executive chauffeur-driven luxury ground transfers throughout', 2),
            _inc_included('Jungfraujoch — Top of Europe excursion', 3),
            _inc_included('Lauterbrunnen Valley scenic exploration', 4),
            _inc_included('Lake Brienz leisure and private boat excursion', 5),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 6),
            _inc_excluded('International airfare and Switzerland entry visa processing fees', 7),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 8),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 9),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 10),
        ],
    )
    return package, itinerary

def build_ch_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'CH-005'
    db_serial = 'SW-005'
    tour_code = 'TRG-SWI-GRD-2026'
    title = 'Grand Switzerland Tour'
    duration = '09 Nights / 10 Days'
    slug = 'ch-005-grand-switzerland-tour'
    itin_slug = 'ch-005-grand-switzerland-tour-itinerary'
    package = PackageCreate(
        slug=slug,
        serial_code=db_serial,
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
            _ph('Serial code CH-005 | TRAGUIN tour code TRG-SWI-GRD-2026', 1),
            _ph('Country: Switzerland | Category: Premium Grand Switzerland Tour Package', 2),
            _ph('Destinations: Zurich • Lucerne • Mt. Titlis • Interlaken • Jungfraujoch • Zermatt • Montreux • Geneva', 3),
            _ph('Best season: October to March', 4),
            _ph('Starting price: On Request', 5)
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
        price_note='On Request (Premium Switzerland Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Zurich • Lucerne • Mt. Titlis • Interlaken • Jungfraujoch • Zermatt • Montreux • Geneva',
        overview='Zurich • Lucerne • Mt. Titlis • Interlaken • Jungfraujoch • Zermatt • Montreux • Geneva 09 Nights / 10 Days Grand Switzerland Premium Expedition SERIAL CODE: CH-005 TRAGUIN TOUR CODE: TRG-SWI-GRD-2026 STATE / COUNTRY: Switzerland CATEGORY: Premium Grand Switzerland Tour Package DURATION: 09 Nights / 10 Days Zurich(2N) + Lucerne(2N) + Interlaken(2N) + Zermatt(2N) + Geneva(1N)\n\nTOUR OVERVIEW\nDiscover the absolute best of Switzerland with our TRAGUIN curated Grand Expedition. This comprehensive 10-day journey covers all iconic destinations—from the sophistication of Zurich and Lucerne to the alpine heart of Interlaken, the grandeur of Zermatt, and the lakeside elegance of Geneva—ensuring unforgettable memories in ultimate comfort. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='CH-005 | Grand Switzerland Tour | TRAGUIN',
        seo_description='Premium 09 Nights / 10 Days Switzerland package (CH-005 / TRG-SWI-GRD-2026): Zurich • Lucerne • Mt. Titlis • Interlaken • Jungfraujoch • Zermatt • Montreux • Geneva.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN ZURICH', 1),
            _ih('Day 02: ZURICH CULTURAL DISCOVERY', 2),
            _ih('Day 03: TRANSFER TO LUCERNE', 3),
            _ih('Day 04: MT. TITLIS EXCURSION', 4),
            _ih('Day 05: TRANSFER TO INTERLAKEN', 5),
            _ih('Day 06: JUNGFRAUJOCH EXPEDITION', 6),
            _ih('Day 07: TRANSFER TO ZERMATT', 7),
            _ih('Day 08: MATTERHORN EXPLORATION', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN ZURICH',
                (
                    'Arrive in Zurich. Private transfer to your handpicked premium hotel. Evening at leisure.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'ZURICH CULTURAL DISCOVERY',
                (
                    'Comprehensive city tour covering Zurich’s most famous landmarks, providing a rich educational experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'TRANSFER TO LUCERNE',
                (
                    'Scenic transfer to Lucerne. Visit the iconic Chapel Bridge and take a peaceful lake cruise, a classic Swiss experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'MT. TITLIS EXCURSION',
                (
                    'Ascend to Mt. Titlis by cable car. Enjoy snow activities at the summit, creating unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'TRANSFER TO INTERLAKEN',
                (
                    'Scenic train transfer to Interlaken. Check into your luxury alpine retreat.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'JUNGFRAUJOCH EXPEDITION',
                (
                    'A spectacular journey to Jungfraujoch—the Top of Europe. Experience breathtaking panoramic views and high-altitude excitement.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'TRANSFER TO ZERMATT',
                (
                    'Transfer to Zermatt. Check into an ultra-luxury boutique suite with Matterhorn views.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                8,
                'MATTERHORN EXPLORATION',
                (
                    'Explore Zermatt at your own pace, enjoy boutique shopping, and an exclusive experience viewing the iconic peak.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                9,
                'TRANSFER TO GENEVA',
                (
                    'Scenic transfer to Geneva. Evening farewell dinner gala, celebrating your grand Switzerland expedition.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                10,
                'DEPARTURE',
                (
                    'Final luxury breakfast before your TRAGUIN private transfer to the airport, completing your grand Switzerland journey.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Premium Luxury City Hotel / similar',
                'Zurich',
                '2N',
                'Premium',
                'Deluxe Room',
                'Breakfast',
                5,
                1,
                description='OPTION 01 – PREMIUM: Premium Luxury City Hotel',
            ),
            _hotel(
                'Premium Lake View Hotel / similar',
                'Lucerne',
                '2N',
                'Premium',
                'Deluxe Room',
                'Breakfast',
                5,
                2,
                description='OPTION 02 – PREMIUM: Premium Lake View Hotel',
            ),
            _hotel(
                'Luxury Alpine Retreat / similar',
                'Interlaken',
                '2N',
                'Premium',
                'Deluxe Room',
                'Breakfast',
                5,
                3,
                description='OPTION 03 – PREMIUM: Luxury Alpine Retreat',
            ),
            _hotel(
                'Luxury Matterhorn Suites / similar',
                'Zermatt',
                '2N',
                'Premium',
                'Deluxe Room',
                'Breakfast',
                5,
                4,
                description='OPTION 04 – PREMIUM: Luxury Matterhorn Suites',
            ),
            _hotel(
                'Luxury Lakeside Hotel / similar',
                'Geneva',
                '1N',
                'Premium',
                'Deluxe Room',
                'Breakfast',
                5,
                5,
                description='OPTION 05 – PREMIUM: Luxury Lakeside Hotel',
            )
        ],
        inclusions=[
            _inc_included('09 Nights in handpicked premium hotels across Zurich • Lucerne • Mt. Titlis • Interlaken • Jungfraujoch • Zermatt • Montreux • Geneva', 1),
            _inc_included('Private executive chauffeur-driven luxury ground transfers throughout', 2),
            _inc_included('Mt. Titlis cable car ascent with summit snow activities', 3),
            _inc_included('Jungfraujoch — Top of Europe excursion', 4),
            _inc_included('Lucerne lake cruise and Chapel Bridge sightseeing', 5),
            _inc_included('Matterhorn-view luxury stay and exploration in Zermatt', 6),
            _inc_included('Geneva lakeside elegance and farewell gala dinner', 7),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 8),
            _inc_excluded('International airfare and Switzerland entry visa processing fees', 9),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 10),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 11),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 12),
        ],
    )
    return package, itinerary

SWITZERLAND_CH_001_005_BUILDERS = [
    build_ch_001,
    build_ch_002,
    build_ch_003,
    build_ch_004,
    build_ch_005,
]
