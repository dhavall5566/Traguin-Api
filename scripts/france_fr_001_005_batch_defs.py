"""Builder functions for FR-001 through FR-005 France international packages."""

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

FRANCE_SLUG = "france"


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


def build_fr_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'FR-001'
    db_serial = 'FR-001'
    tour_code = 'TRG-PAR-HIGHLIGHTS-2026'
    title = 'Paris Highlights Family Tour'
    duration = '04 Nights / 05 Days'
    slug = 'fr-001-paris-highlights-family-tour'
    itin_slug = 'fr-001-paris-highlights-itinerary'
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
            _ph('Serial code FR-001 | TRAGUIN tour code TRG-PAR-HIGHLIGHTS-2026', 1),
            _ph('Country: France | Category: Best Paris Family Tour Package', 2),
            _ph('Destinations: Eiffel Tower • Louvre Museum • Seine River Cruise • Montmartre • Palace of Versailles', 3),
            _ph('Best season: October to March', 4),
            _ph('Starting price: On Request', 5)
        ],
        moods=['Family', 'Romantic'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium France Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Eiffel Tower • Louvre Museum • Seine River Cruise • Montmartre • Palace of Versailles',
        overview='Eiffel Tower • Louvre Museum • Seine River Cruise • Montmartre • Palace of Versailles 04 Nights / 05 Days Classic Paris Family Heritage Expedition SERIAL CODE: FR-001 TRAGUIN TOUR CODE: TRG-PAR-HIGHLIGHTS-2026 STATE / COUNTRY: France CATEGORY: Best Paris Family Tour Package DURATION: 04 Nights / 05 Days Paris Exploration\n\nTOUR OVERVIEW\nDiscover the dazzling charm and historic grandeur of the "City of Light" with our TRAGUIN curated family itinerary. Designed for excitement and comfort, this Paris Family Highlights package offers a flawless blend of monumental exploration, artistic discovery, and leisurely strolls through charming quarters. Experience the best of French hospitality with TRAGUIN\'s handpicked hotels and exclusive services, creating unforgettable memories.\n\nWHY CHOOSE OUR PARIS HIGHLIGHTS FAMILY TOUR?\nParis is a world-class playground for families, offering endless excitement for all ages. From the towering Eiffel Tower to the treasures of the Louvre, our curated experiences promise a premium Paris experience. With TRAGUIN, you get professional support and exclusive experiences that redefine the family holiday. Discover the iconic attractions that make Paris a dream destination. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='FR-001 | Paris Highlights Family Tour | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days France package (FR-001 / TRG-PAR-HIGHLIGHTS-2026): Eiffel Tower • Louvre Museum • Seine River Cruise • Montmartre • Palace of Versailles.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN PARIS & SEINE RIVER CRUISE', 1),
            _ih('Day 02: EIFFEL TOWER & LOUVRE DISCOVERY', 2),
            _ih('Day 03: PALACE OF VERSAILLES', 3),
            _ih('Day 04: MONTMARTRE & ARTISTIC CHARM', 4),
            _ih('Day 05: DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN PARIS & SEINE RIVER CRUISE',
                (
                    'Arrive in elegant Paris. Your private TRAGUIN transfer will escort you to your handpicked hotel. Enjoy a relaxing evening with a scenic Seine River cruise, admiring the city’s stunning landmarks illuminated at night.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'EIFFEL TOWER & LOUVRE DISCOVERY',
                (
                    "Explore the iconic attractions of Paris. Visit the Eiffel Tower and the Louvre Museum. This curated experience offers deep insights into Paris's history, culture, and iconic attractions."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'PALACE OF VERSAILLES',
                (
                    "Embark on a grand excursion to the Palace of Versailles. Explore the breathtaking state apartments, Hall of Mirrors, and the magnificent royal gardens—a highlight of TRAGUIN's exclusive packages."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'MONTMARTRE & ARTISTIC CHARM',
                (
                    'A full day of immersive fun exploring the artistic streets of Montmartre. Visit the Sacré-Cœur Basilica, enjoy local art, and taste French cuisine, creating unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'DEPARTURE',
                (
                    'Enjoy a final family breakfast. Your private TRAGUIN chauffeur ensures a comfortable transfer to the airport, completing your premium Paris experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Le Meurice / The Peninsula Paris / similar',
                'Paris',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'Breakfast',
                5,
                1,
                description='OPTION 01 – ULTRA LUXURY: Le Meurice / The Peninsula Paris',
            )
        ],
        inclusions=[
            _inc_included('04 Nights in handpicked premium hotels across Eiffel Tower • Louvre Museum • Seine River Cruise • Montmartre • Palace of Versailles', 1),
            _inc_included('Private executive chauffeur-driven luxury ground transfers throughout', 2),
            _inc_included('Private guided Paris sightseeing including Eiffel Tower, Louvre, and Versailles', 3),
            _inc_included('Scenic Seine River cruise experience', 4),
            _inc_included('Montmartre and Sacré-Cœur artistic quarter exploration', 5),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 6),
            _inc_excluded('International airfare and France/Schengen entry visa processing fees', 7),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 8),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 9),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 10),
        ],
    )
    return package, itinerary

def build_fr_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'FR-002'
    db_serial = 'FR-002'
    tour_code = 'TRG-PAR-ROMANCE-2026'
    title = 'Romantic Paris Honeymoon'
    duration = '05 Nights / 06 Days'
    slug = 'fr-002-romantic-paris-honeymoon'
    itin_slug = 'fr-002-romantic-paris-itinerary'
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
            _ph('Serial code FR-002 | TRAGUIN tour code TRG-PAR-ROMANCE-2026', 1),
            _ph('Country: France | Category: Luxury Romantic Paris Honeymoon Package', 2),
            _ph('Destinations: Eiffel Tower • Seine River Cruise • Montmartre • Versailles • Luxury Dining', 3),
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
        price_note='On Request (Premium France Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Eiffel Tower • Seine River Cruise • Montmartre • Versailles • Luxury Dining',
        overview='Eiffel Tower • Seine River Cruise • Montmartre • Versailles • Luxury Dining 05 Nights / 06 Days Romantic Paris Honeymoon Sanctuary SERIAL CODE: FR-002 TRAGUIN TOUR CODE: TRG-PAR-ROMANCE-2026 STATE / COUNTRY: France CATEGORY: Luxury Romantic Paris Honeymoon Package DURATION: 05 Nights / 06 Days Paris Exploration\n\nTOUR OVERVIEW\nBegin your lifelong love story in the most poetic city in the world. Our TRAGUIN curated Paris honeymoon retreat offers an unparalleled blend of classic French romance, world-class culinary experiences, and iconic landmark exploration. Designed for absolute comfort and privacy, this Romantic Paris journey guarantees unforgettable memories in the heart of the "City of Light".\n\nWHY CHOOSE OUR ROMANTIC PARIS HONEYMOON?\nParis provides an iconic backdrop for honeymoons, featuring breathtaking architecture, charming cobblestone streets, and exquisite dining. Choosing TRAGUIN for your honeymoon ensures premium experiences, from private guided tours to intimate sunset cruises. Discover why Paris remains the dream destination for couples worldwide. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='FR-002 | Romantic Paris Honeymoon | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days France package (FR-002 / TRG-PAR-ROMANCE-2026): Eiffel Tower • Seine River Cruise • Montmartre • Versailles • Luxury Dining.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN PARIS & SEINE RIVER DINNER CRUISE', 1),
            _ih('Day 02: EIFFEL TOWER & ARTISTIC MONTMARTRE', 2),
            _ih('Day 03: PALACE OF VERSAILLES', 3),
            _ih('Day 04: LOUVRE MUSEUM & SHOPPING', 4),
            _ih('Day 05: LEISURE & ROMANTIC DINNER', 5),
            _ih('Day 06: DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN PARIS & SEINE RIVER DINNER CRUISE',
                (
                    'Arrive in Paris, the City of Light. Your private transfer will escort you to your ultra-luxury hotel. Celebrate your first evening with a private dinner cruise on the Seine River, viewing iconic landmarks like the Eiffel Tower illuminated.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'EIFFEL TOWER & ARTISTIC MONTMARTRE',
                (
                    'Visit the iconic Eiffel Tower with skip-the-line access. Later, explore the charming artistic district of Montmartre, visit the Sacré-Cœur Basilica, and enjoy a private artistic walking tour through its quaint streets.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'PALACE OF VERSAILLES',
                (
                    'A private excursion to the majestic Palace of Versailles. Explore the royal apartments and stroll through the expansive, beautiful royal gardens in style, creating unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'LOUVRE MUSEUM & SHOPPING',
                (
                    'Discover artistic treasures at the Louvre Museum. Spend your afternoon enjoying leisurely luxury shopping along the Champs-Élysées, ensuring a perfect premium experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'LEISURE & ROMANTIC DINNER',
                (
                    'Spend a relaxing day exploring local cafes, visiting charming patisseries, and enjoying a farewell candlelight dinner in a romantic garden restaurant.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'DEPARTURE',
                (
                    'Enjoy a final French breakfast before your TRAGUIN private transfer, completing your romantic Paris honeymoon.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Premium Property / similar',
                'Eiffel Tower',
                '05 Nights',
                'Premium',
                'Deluxe Room',
                'Breakfast',
                5,
                1,
                description='OPTION 01 – PREMIUM: TRAGUIN Handpicked Premium Property',
            )
        ],
        inclusions=[
            _inc_included('05 Nights in handpicked premium hotels across Eiffel Tower • Seine River Cruise • Montmartre • Versailles • Luxury Dining', 1),
            _inc_included('Private executive chauffeur-driven luxury ground transfers throughout', 2),
            _inc_included('Private guided Paris sightseeing including Eiffel Tower, Louvre, and Versailles', 3),
            _inc_included('Scenic Seine River cruise experience', 4),
            _inc_included('Montmartre and Sacré-Cœur artistic quarter exploration', 5),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 6),
            _inc_excluded('International airfare and France/Schengen entry visa processing fees', 7),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 8),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 9),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 10),
        ],
    )
    return package, itinerary

def build_fr_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'FR-003'
    db_serial = 'FR-003'
    tour_code = 'TRG-FRA-LUX-2026'
    title = 'Luxury France Tour'
    duration = '06 Nights / 07 Days'
    slug = 'fr-003-luxury-france-tour'
    itin_slug = 'fr-003-luxury-france-itinerary'
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
            _ph('Serial code FR-003 | TRAGUIN tour code TRG-FRA-LUX-2026', 1),
            _ph('Country: France | Category: Luxury France Tour Package', 2),
            _ph('Destinations: Paris • Versailles • French Riviera (Nice/Monaco) • Provence Lavender Fields', 3),
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
        price_note='On Request (Premium France Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Paris • Versailles • French Riviera (Nice/Monaco) • Provence Lavender Fields',
        overview='06 Nights / 07 Days Ultra-Luxury French Elegance Showcase SERIAL CODE: FR-003 TRAGUIN TOUR CODE: TRG-FRA-LUX-2026 STATE / COUNTRY: France CATEGORY: Luxury France Tour Package DURATION: 06 Nights / 07 Days Paris (3N) • French Riviera (3N)\n\nTOUR OVERVIEW\nDiscover the height of sophistication and style with this TRAGUIN curated luxury French expedition. From the iconic streets of Paris to the shimmering azure coast of the French Riviera, experience an unmatched journey of culture, gastronomy, and breathtaking beauty. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='FR-003 | Luxury France Tour | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days France package (FR-003 / TRG-FRA-LUX-2026): Paris • Versailles • French Riviera (Nice/Monaco) • Provence Lavender Fields.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN PARIS & SEINE CRUISE', 1),
            _ih('Day 02: PARIS ART & GASTRONOMY', 2),
            _ih('Day 03: PALACE OF VERSAILLES & SHOPPING', 3),
            _ih('Day 04: FLY TO FRENCH RIVIERA', 4),
            _ih('Day 05: MONACO & MONTE CARLO', 5),
            _ih("Day 06: PROVENCE LAVENDER & CÔTE D'AZUR", 6),
            _ih('Day 07: DEPARTURE', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN PARIS & SEINE CRUISE',
                (
                    'Arrive in elegant Paris. Private transfer to your ultra-luxury hotel. Enjoy a private Seine River cruise with champagne at sunset.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'PARIS ART & GASTRONOMY',
                (
                    'Exclusive private tour of the Louvre followed by a gourmet French cooking class in a historic Parisian kitchen.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'PALACE OF VERSAILLES & SHOPPING',
                (
                    'Private excursion to Versailles. Afternoon dedicated to high-end shopping in the legendary boutiques of the Golden Triangle.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'FLY TO FRENCH RIVIERA',
                (
                    'Private flight to Nice. Check into a world-class seaside resort. Enjoy the vibrant colors and lifestyle of the French Riviera.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'MONACO & MONTE CARLO',
                (
                    "Day trip to Monaco and Monte Carlo. Explore the prince's palace and the famous casino, enjoying the exclusive experiences of the elite coast."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                "PROVENCE LAVENDER & CÔTE D'AZUR",
                (
                    "Visit the lavender fields of Provence followed by a coastal drive along the stunning Côte d'Azur. A premium French experience."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'DEPARTURE',
                (
                    'Final luxury breakfast. Private transfer to Nice airport for departure, completing your premium France experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Four Seasons George V / similar',
                'Paris',
                '3N',
                'Ultra Luxury',
                'Deluxe Room',
                'Breakfast',
                5,
                1,
                description='OPTION 01 – ULTRA LUXURY: Four Seasons George V',
            ),
            _hotel(
                '/ / similar',
                'French Riviera',
                '3N',
                'Ultra Luxury',
                'Deluxe Room',
                'Breakfast',
                5,
                2,
                description='OPTION 02 – ULTRA LUXURY: /',
            )
        ],
        inclusions=[
            _inc_included('06 Nights in handpicked premium hotels across Paris • Versailles • French Riviera (Nice/Monaco) • Provence Lavender Fields', 1),
            _inc_included('Private executive chauffeur-driven luxury ground transfers throughout', 2),
            _inc_included('Private guided Paris sightseeing including Eiffel Tower, Louvre, and Versailles', 3),
            _inc_included('Scenic Seine River cruise experience', 4),
            _inc_included('French Riviera and Monaco elite coastal experiences', 5),
            _inc_included('Curated wine country and heritage castle experiences', 6),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 7),
            _inc_excluded('International airfare and France/Schengen entry visa processing fees', 8),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 9),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 10),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 11),
        ],
    )
    return package, itinerary

def build_fr_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'FR-004'
    db_serial = 'FR-004'
    tour_code = 'TRG-PAR-SWI-2026'
    title = 'Paris & Swiss Family Tour'
    duration = '07 Nights / 08 Days'
    slug = 'fr-004-paris-swiss-family-tour'
    itin_slug = 'fr-004-paris-swiss-family-itinerary'
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
        is_published=True,
        highlights=[
            _ph('Serial code FR-004 | TRAGUIN tour code TRG-PAR-SWI-2026', 1),
            _ph('Country: France | Category: Best Family Tour Package', 2),
            _ph('Destinations: Paris, France • Lucerne/Interlaken, Switzerland', 3),
            _ph('Best season: October to March', 4),
            _ph('Starting price: On Request', 5)
        ],
        moods=['Family', 'Romantic', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium France Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Paris, France • Lucerne/Interlaken, Switzerland',
        overview="Paris • Eiffel Tower • Lucerne • Mt. Titlis • Interlaken 07 Nights / 08 Days Classic Paris & Swiss Family Vacation SERIAL CODE: FR-004 TRAGUIN TOUR CODE: TRG-PAR-SWI-2026 DESTINATIONS: Paris, France • Lucerne/Interlaken, Switzerland CATEGORY: Best Family Tour Package DURATION: 07 Nights / 08 Days Paris (3N) • Switzerland (4N)\n\nTOUR OVERVIEW\nDiscover the dazzling charm of Paris and the breathtaking alpine beauty of Switzerland with this TRAGUIN curated family itinerary. Designed for excitement and comfort, this Paris-Swiss Combo package offers a flawless blend of monumental exploration and scenic mountain adventure. Experience the best of European hospitality with TRAGUIN's handpicked hotels and exclusive services, creating unforgettable memories.\n\nWHY CHOOSE OUR PARIS & SWISS FAMILY TOUR?\nParis and Switzerland are world-class playgrounds for families, offering endless excitement for all ages. From the towering Eiffel Tower to the snow-capped peaks of Mt. Titlis, our curated experiences promise a premium European experience. With TRAGUIN, you get professional support and exclusive experiences that redefine the family holiday. THE IMMERSIVE DAY-WISE ITINERARY",
        seo_title='FR-004 | Paris & Swiss Family Tour | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days France package (FR-004 / TRG-PAR-SWI-2026): Paris, France • Lucerne/Interlaken, Switzerland.',
        is_featured=False,
        featured_sort_order=None,
        is_published=True,
        highlights=[
            _ih('Day 01: ARRIVAL IN PARIS', 1),
            _ih('Day 02: PARIS LANDMARKS', 2),
            _ih('Day 03: PARIS TO SWITZERLAND', 3),
            _ih('Day 04: MT. TITLIS ADVENTURE', 4),
            _ih('Day 05: INTERLAKEN SCENERY', 5),
            _ih('Day 06: SWISS MOUNTAIN LEISURE', 6),
            _ih('Day 07: RETURN TO PARIS / DEPARTURE PREP', 7),
            _ih('Day 08: DEPARTURE', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN PARIS',
                (
                    'Arrive in elegant Paris. Your private TRAGUIN transfer will escort you to your handpicked hotel. Enjoy a relaxing evening overlooking the city.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'PARIS LANDMARKS',
                (
                    'Explore the iconic Eiffel Tower and take a scenic Seine River cruise. Witness the iconic attractions that define luxury Paris sightseeing.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'PARIS TO SWITZERLAND',
                (
                    'High-speed train journey to Switzerland. Arrive in the scenic city of Lucerne, renowned for its lake and mountain views.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'MT. TITLIS ADVENTURE',
                (
                    'Experience the snow-capped majesty of Mt. Titlis with a cable car ride—a premium Swiss experience for the whole family.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'INTERLAKEN SCENERY',
                (
                    'Explore the charming town of Interlaken, nestled between two stunning lakes, offering endless breathtaking landscapes.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'SWISS MOUNTAIN LEISURE',
                (
                    'Enjoy a leisurely day exploring Swiss villages and local chocolate factories, creating unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'RETURN TO PARIS / DEPARTURE PREP',
                (
                    'Travel back to Paris for final shopping and leisure time before your premium experience concludes.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                8,
                'DEPARTURE',
                (
                    'Final luxury breakfast before your private TRAGUIN transfer to the airport.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Le Meurice / similar',
                'Paris',
                '3N',
                'Ultra Luxury',
                'Deluxe Room',
                'Breakfast',
                5,
                1,
                description='OPTION 01 – ULTRA LUXURY: Le Meurice',
            ),
            _hotel(
                'Bürgenstock Resort / similar',
                'Switzerland',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'Breakfast',
                5,
                2,
                description='OPTION 02 – ULTRA LUXURY: Bürgenstock Resort',
            )
        ],
        inclusions=[
            _inc_included('07 Nights in handpicked premium hotels across Paris, France • Lucerne/Interlaken, Switzerland', 1),
            _inc_included('Private executive chauffeur-driven luxury ground transfers throughout', 2),
            _inc_included('Private guided Paris sightseeing including Eiffel Tower, Louvre, and Versailles', 3),
            _inc_included('Scenic Seine River cruise experience', 4),
            _inc_included('High-speed rail and alpine experiences in Switzerland', 5),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 6),
            _inc_excluded('International airfare and France/Schengen entry visa processing fees', 7),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 8),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 9),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 10),
        ],
    )
    return package, itinerary

def build_fr_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'FR-005'
    db_serial = 'FR-005'
    tour_code = 'TRG-FRA-GRD-2026'
    title = 'Grand France Tour'
    duration = '08 Nights / 09 Days'
    slug = 'fr-005-grand-france-tour'
    itin_slug = 'fr-005-grand-france-itinerary'
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
        is_published=True,
        highlights=[
            _ph('Serial code FR-005 | TRAGUIN tour code TRG-FRA-GRD-2026', 1),
            _ph('Country: France | Category: Grand Luxury France Tour Package', 2),
            _ph('Destinations: Paris • Versailles • Loire Valley Castles • Bordeaux Vineyards • French Riviera (Nice/', 3),
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
        price_note='On Request (Premium France Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Paris • Versailles • Loire Valley Castles • Bordeaux Vineyards • French Riviera (Nice/',
        overview='Monaco) 08 Nights / 09 Days Ultra-Luxury Grand France Showcase SERIAL CODE: FR-005 TRAGUIN TOUR CODE: TRG-FRA-GRD-2026 STATE / COUNTRY: France CATEGORY: Grand Luxury France Tour Package DURATION: 08 Nights / 09 Days Paris (3N) • Loire Valley (2N) • Bordeaux (2N) • French Riviera (2N)\n\nTOUR OVERVIEW\nDiscover the absolute pinnacle of French elegance with our TRAGUIN curated Grand Expedition. This ultimate journey explores the royal architecture of Paris and Versailles, the historic fairytale castles of the Loire Valley, the prestigious vineyards of Bordeaux, and the glamour of the French Riviera. A truly unforgettable experience for the most discerning travelers. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='FR-005 | Grand France Tour | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days France package (FR-005 / TRG-FRA-GRD-2026): Paris • Versailles • Loire Valley Castles • Bordeaux Vineyards • French Riviera (Nice/.',
        is_featured=False,
        featured_sort_order=None,
        is_published=True,
        highlights=[
            _ih('Day 01: ARRIVAL IN PARIS', 1),
            _ih('Day 02: PARIS ART & HISTORY', 2),
            _ih('Day 03: PALACE OF VERSAILLES', 3),
            _ih('Day 04: LOIRE VALLEY CASTLES', 4),
            _ih('Day 05: LOIRE VALLEY WINERIES', 5),
            _ih('Day 06: BORDEAUX VINEYARDS', 6),
            _ih('Day 07: BORDEAUX HERITAGE', 7),
            _ih('Day 08: FRENCH RIVIERA GLAMOUR', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN PARIS',
                (
                    'Arrive in Paris, private transfer to a palatial hotel. Enjoy a welcome dinner at a Michelin-starred restaurant with views of the Eiffel Tower.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'PARIS ART & HISTORY',
                (
                    'Private guided tour of the Louvre followed by a walk through the charming Marais district. Evening private Seine cruise.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'PALACE OF VERSAILLES',
                (
                    "Private tour of Versailles' Royal Apartments and the expansive gardens. Evening at leisure."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'LOIRE VALLEY CASTLES',
                (
                    'Travel to the Loire Valley. Private exploration of the stunning Château de Chambord and Château de Chenonceau.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'LOIRE VALLEY WINERIES',
                (
                    'Enjoy a private tasting tour at local vineyards followed by an afternoon in the charming city of Tours.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'BORDEAUX VINEYARDS',
                (
                    'Travel to Bordeaux. Private visit to legendary wine estates of Saint-Émilion. Gastronomic dinner featuring local wines.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'BORDEAUX HERITAGE',
                (
                    'Explore the historic centre of Bordeaux, a UNESCO World Heritage site, and its contemporary wine museum, La Cité du Vin.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                8,
                'FRENCH RIVIERA GLAMOUR',
                (
                    'Flight to the Riviera. Check into a world-class seaside palace hotel in Nice. Sunset walk along the Promenade des Anglais.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                9,
                'MONACO & DEPARTURE',
                (
                    'Private excursion to Monaco. Explore the Prince’s Palace and the Monte Carlo Casino before your flight from Nice.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Peninsula Paris / similar',
                'Paris',
                '3N',
                'Ultra Luxury',
                'Deluxe Room',
                'Breakfast',
                5,
                1,
                description='OPTION 01 – ULTRA LUXURY: The Peninsula Paris',
            ),
            _hotel(
                'Château de la Bourdaisière / similar',
                'Bordeaux',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'Breakfast',
                5,
                2,
                description='OPTION 02 – ULTRA LUXURY: Château de la Bourdaisière',
            ),
            _hotel(
                'Grand-Hôtel du Cap-Ferrat / similar',
                'Riviera',
                '2N',
                'Ultra Luxury',
                'Deluxe Room',
                'Breakfast',
                5,
                3,
                description='OPTION 03 – ULTRA LUXURY: Grand-Hôtel du Cap-Ferrat',
            )
        ],
        inclusions=[
            _inc_included('08 Nights in handpicked premium hotels across Paris • Versailles • Loire Valley Castles • Bordeaux Vineyards • French Riviera (Nice/', 1),
            _inc_included('Private executive chauffeur-driven luxury ground transfers throughout', 2),
            _inc_included('Private guided Paris sightseeing including Eiffel Tower, Louvre, and Versailles', 3),
            _inc_included('Scenic Seine River cruise experience', 4),
            _inc_included('French Riviera and Monaco elite coastal experiences', 5),
            _inc_included('Curated wine country and heritage castle experiences', 6),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 7),
            _inc_excluded('International airfare and France/Schengen entry visa processing fees', 8),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 9),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 10),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 11),
        ],
    )
    return package, itinerary

FRANCE_FR_001_005_BUILDERS = [
    build_fr_001,
    build_fr_002,
    build_fr_003,
    build_fr_004,
    build_fr_005,
]
