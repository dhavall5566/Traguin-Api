"""Builder functions for IT-001 through IT-005 Italy international packages."""

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

ITALY_SLUG = "italy"


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


def build_it_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'IT-001'
    tour_code = 'TRG-ITA-HIGHLIGHTS-2026'
    title = 'Italy Highlights Family Tour'
    duration = '06 Nights / 07 Days'
    slug = 'it-001-italy-highlights-family-tour'
    itin_slug = 'it-001-italy-highlights-itinerary'
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
            _ph('Serial code IT-001 | TRAGUIN tour code TRG-ITA-HIGHLIGHTS-2026', 1),
            _ph('Country: Italy, Europe | Category: Best Italy Family Tour Package', 2),
            _ph('Destinations: Rome (2N) • Florence /', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury MPV / Buffet Breakfast & Curated Dinners', 7)
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
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Italy Highlights Family Tour',
        overview="Rome • Vatican City • Florence • Tuscany • Venice Canals 06 Nights / 07 Days Classic Italy Family Vacation SERIAL CODE: IT-001 TRAGUIN TOUR CODE: TRG-ITA-HIGHLIGHTS-2026 STATE / COUNTRY: Italy / Europe CATEGORY: Best Italy Family Tour Package DURATION: 06 Nights / 07 Days DESTINATIONS COVERED: Rome (2N) • Florence / Tuscany (2N) • Venice (2N)\n\nTOUR OVERVIEW\nEmbark on an extraordinary European odyssey with our TRAGUIN curated family itinerary. Blending ancient Roman history, Renaissance art in Florence, and the romantic water matrices of Venice, this Luxury Italy Holiday offers unforgettable memories, breathtaking landscapes, and exclusive experiences for your family. Welcome Note from TRAGUIN: Family travel requires precise logistical care. This 7-day optimized expedition includes full luxury ground transit in private vehicles, pre-booked skip-the-line admissions to world heritage monuments, and handpicked hotels to guarantee absolute comfort and premium service.\n\nWHY CHOOSE OUR ITALY HIGHLIGHTS FAMILY TOUR?\nItaly is the ultimate tapestry of cultural marvels, artistic brilliance, and divine culinary heritage, making it the perfect choice for family bonding. Selecting this Best Italy Tour Package promises a seamless journey through Italy's most famous regions. This framework features highly searched keywords for Google ranking, ensuring an exceptional showcase of premier Italy Sightseeing attractions. Discover Top Tourist Places in Italy: wander through the monumental Colosseum in Rome, explore the artistic treasures of Vatican City, cruise along the beautiful Grand Canal in Venice, and admire the rolling hills of Tuscany. It is the absolute Best Time to Visit Italy to experience immersive experiences, photograph scenic beauty, and indulge in an unmatched Premium Italy Experience. THE DEFINITIVE DAY-WISE ITINERARY",
        seo_title='IT-001 | Italy Highlights Family Tour | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Italy package (IT-001 / TRG-ITA-HIGHLIGHTS-2026): Rome (2N) • Florence / with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN ROME & HISTORIC AMBIANCE', 1),
            _ih('Day 02: VATICAN MUSEUMS & THE COLOSSEUM', 2),
            _ih('Day 03: SCENIC HIGHWAY TO RENAISSANCE FLORENCE', 3),
            _ih('Day 04: FLORENCE ARTISANS & TUSCAN VILLAGE EXPLORATION', 4),
            _ih('Day 05: SPEED TRANSIT TO THE CANALS OF VENICE', 5),
            _ih("Day 06: ST. MARK'S SQUARE & ISLAND HOPPING", 6),
            _ih('Day 07: VENICE DEPARTURE', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN ROME & HISTORIC AMBIANCE',
                (
                    "Welcome to the Eternal City! Arrive at Rome Fiumicino Airport, where your private TRAGUIN chauffeur-driven luxury vehicle awaits to transfer you to your hotel. After checking in, enjoy a leisurely evening stroll with your family through the lively Piazza Navona and past the iconic Trevi Fountain. Toss a coin to ensure your family's return to Rome, capturing wonderful photography points. Sightseeing Included: Private luxury vehicle airport transfer, Trevi Fountain & Piazza Navona evening walk. Evening Experience: Family welcome dinner at an upscale Roman trattoria, tasting authentic pasta."
                ),
                [
                    'Overnight Stay: Rome Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: Traditional Italian Welcome Dinner',
                ],
            ),
            _day(
                2,
                'VATICAN MUSEUMS & THE COLOSSEUM',
                (
                    "Enjoy a bountiful buffet breakfast. Today, immerse yourself in ancient history and art. Bypass all public lines with our pre-arranged skip-the-line tickets to enter the Vatican Museums, the Sistine Chapel, and St. Peter's Basilica. In the afternoon, explore the monumental Colosseum and Roman Forum with a private family guide, bringing the gladiatorial tales of Rome to life. Sightseeing Included: Vatican Museums & Sistine Chapel skip-the-line entry, Private Colosseum guided tour."
                ),
                [
                    'Overnight Stay: Rome Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: International Breakfast & Casual Italian Bistro Lunch',
                ],
            ),
            _day(
                3,
                'SCENIC HIGHWAY TO RENAISSANCE FLORENCE',
                (
                    'Travel through the scenic beauty of the rolling Umbrian and Tuscan hills as your private chauffeur drives you north to Florence, the cradle of the Renaissance. Upon arrival and resort check-in, enjoy a panoramic view of the red-tiled city skyline from Piazzale Michelangelo. Later, wander across the historic Ponte Vecchio bridge at an easy pace. Sightseeing Included: Private overland transfer through Tuscany, Piazzale Michelangelo viewpoint, Ponte Vecchio.'
                ),
                [
                    'Overnight Stay: Florence / Tuscany Boutique Resort (Premium Stay)',
                    'Meals Included: International Breakfast & Tuscan Countryside Lunch',
                ],
            ),
            _day(
                4,
                'FLORENCE ARTISANS & TUSCAN VILLAGE EXPLORATION',
                (
                    "Spend a beautiful morning exploring the architectural wonders of the Florence Duomo and viewing Michelangelo's David at the Accademia Gallery with pre-booked passes. In the afternoon, escape into the countryside to visit a historic Tuscan estate. Participate in a private family pizza-making masterclass surrounded by olive groves and vineyard breathtaking landscapes. Sightseeing Included: Accademia Gallery skip-the-line entry, Florence Duomo square stroll. Optional Activities: Private family pizza-making and culinary workshop at a Tuscan villa."
                ),
                [
                    'Overnight Stay: Florence / Tuscany Boutique Resort (Premium Stay)',
                    'Meals Included: International Breakfast & Curated Tuscan Dinner',
                ],
            ),
            _day(
                5,
                'SPEED TRANSIT TO THE CANALS OF VENICE',
                (
                    "Board Europe's high-speed Executive Train to glide seamlessly into Venice, the world's most unique floating city. Arrive directly at the grand water terminal where a private luxury water taxi transfers your family to your hotel. In the evening, relax during a private gondola cruise through secret canals, listening to traditional serenades under the stars. Sightseeing Included: High-speed executive train ticket, private luxury water taxi transit, private Gondola cruise."
                ),
                [
                    'Overnight Stay: Venice Island (Handpicked Premium Water-facing Hotel)',
                    'Meals Included: International Breakfast & Venetian Lagoon Seafood Dinner',
                ],
            ),
            _day(
                6,
                "ST. MARK'S SQUARE & ISLAND HOPPING",
                (
                    "Explore St. Mark's Square and the magnificent Doge's Palace with skip-the-line group entry passes. In the afternoon, cruise across the Venetian lagoon to visit the islands of Murano, famous for its colorful glassblowing demonstrations, and Burano, known for its brightly painted lace-making houses—a favorite popular Instagram location. Sightseeing Included: Doge's Palace entry, private water motorboat excursion to Murano & Burano islands. Evening Experience: Grand farewell dinner party at a traditional canal-side terrace."
                ),
                [
                    'Overnight Stay: Venice Island (Handpicked Premium Water-facing Hotel)',
                    'Meals Included: International Breakfast & Grand Farewell Dinner',
                ],
            ),
            _day(
                7,
                'VENICE DEPARTURE',
                (
                    'Savor your final morning breakfast along the Grand Canal, capturing a final round of family photos. Our concierge handlers take full care of your seamless water checkout and luggage coordination. Board your private water taxi directly to Venice Marco Polo Airport for your departure flight home, concluding an extraordinary premium holiday. Transfers: Private water taxi airport departure transit, complete luggage assistance.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Grand PalatinoHotel Adler Cavalieri Hotel Carlton Grand Canal',
                'Multi-city Italy',
                '6N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Hotel Grand PalatinoHotel Adler Cavalieri Hotel Carlton Grand Canal',
            ),
            _hotel(
                'Starhotels MetropoleNH Collection Palazzo GaddiSplendid Venice Starhotels',
                'Multi-city Italy',
                '6N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Starhotels MetropoleNH Collection Palazzo GaddiSplendid Venice Starhotels',
            ),
            _hotel(
                'Anantara Palazzo Naiadi Villa Cora Florence The Gritti Palace Venice',
                'Multi-city Italy',
                '6N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Anantara Palazzo Naiadi Villa Cora Florence The Gritti Palace Venice',
            ),
            _hotel(
                'Hotel de Russie Four Seasons Firenze Aman Venice / St. Regis',
                'Multi-city Italy',
                '6N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Hotel de Russie Four Seasons Firenze Aman Venice / St. Regis',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Italy', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven MPV', 2),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 3),
            _inc_excluded('International airfare and Schengen visa fees', 4),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 5),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 6),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 7),
        ],
    )
    return package, itinerary

def build_it_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'IT-002'
    tour_code = 'TRG-ITA-ROMANCE-2026'
    title = 'Romantic Italy Honeymoon'
    duration = '06 Nights / 07 Days'
    slug = 'it-002-romantic-italy-honeymoon'
    itin_slug = 'it-002-romantic-italy-itinerary'
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
            _ph('Serial code IT-002 | TRAGUIN tour code TRG-ITA-ROMANCE-2026', 1),
            _ph('Country: Italy, Europe | Category: Luxury Romantic Italy Honeymoon Package', 2),
            _ph('Destinations: Venice (2N) • Florence /', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury MPV / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Honeymoon', 'Romantic'],
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
        tagline='Romantic Italy Honeymoon',
        overview='Venice Canals • Florence Twilight • Chianti Wine Roads • Amalfi Coast Cliffside 06 Nights / 07 Days Ultra-Romantic Italy Luxury Honeymoon Celebration SERIAL CODE: IT-002 TRAGUIN TOUR CODE: TRG-ITA-ROMANCE-2026 STATE / COUNTRY: Italy / Europe CATEGORY: Luxury Romantic Italy Honeymoon Package DURATION: 06 Nights / 07 Days DESTINATIONS COVERED: Venice (2N) • Florence / Tuscany (2N) • Amalfi Coast (2N)\n\nTOUR OVERVIEW\nBegin your lifelong love story amid the most poetic realms of the Mediterranean with this signature TRAGUIN curated honeymoon retreat. Crafted specifically for couples pursuing ultimate refinement, this Romantic Italy masterpiece weaves candlelit water matrices, vintage Tuscan road explorations, and spectacular cliffside vistas along the Amalfi coast, guaranteeing unforgettable memories. Honeymoon Note from TRAGUIN: Romance flourishes when details are flawless. This 7-day bespoke expedition incorporates absolute privacy: private luxury water taxis, Mercedes executive ground transits, skip- the-line VIP sanctuary admissions, and candlelit culinary terraces overlooking iconic vistas with 24/7 concierge support.\n\nWHY CHOOSE OUR ROMANTIC ITALY HONEYMOON SANCTUARY?\nItaly is a timeless love letter written in stone, canvas, and vine, offering an unforgettably dramatic backdrop for a luxury honeymoon celebration. Selecting this elite Italy Honeymoon Package delivers an ideal blend of poetic isolation and cultural discovery. This proposal leverages top-tier searched keywords for Google ranking, showcasing premier Italy Sightseeing icons through a deeply emotional lens. Discover Top Tourist Places in Italy tailored for couples: share an intimate gondola serenade through secret Venice waterways, watch the golden sunset over Florence from high Tuscan hilltops, stroll through winding olive groves, and toast your union over the crystalline cliffs of Amalfi. It is the absolute Best Time to Visit Italy to experience private curated experiences, photograph immense scenic beauty, and secure an unparalleled Premium Italy Experience. TRAGUIN Honeymoon Touchpoints: Private water taxi arrivals directly to hotel piers, vintage wooden boat sunset cruise in Venice, personalized wine tasting trails in Chianti, and a front-row ocean-facing candlelight farewell dinner. THE DEFINITIVE DAY-WISE ITINERARY',
        seo_title='IT-002 | Romantic Italy Honeymoon | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Italy package (IT-002 / TRG-ITA-ROMANCE-2026): Venice (2N) • Florence / with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN VENICE & PRIVATE CANAL CRUISE', 1),
            _ih("Day 02: THE ISLANDS OF LOVE & TWILIGHT IN ST. MARK'S", 2),
            _ih('Day 03: HIGH-SPEED TRAIN TO TUSCAN HARMONY', 3),
            _ih('Day 04: VINTAGE DRIVING BLISS & CHIANTI TASTING', 4),
            _ih('Day 05: FLIGHT OF THE SOUL TO THE AMALFI CLIFFS', 5),
            _ih('Day 06: PRIVATE YACHT CRUISE TO CAPRI & FAREWELL GALA', 6),
            _ih('Day 07: SUNSET CHECKOUT & NAPLES DEPARTURE', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN VENICE & PRIVATE CANAL CRUISE',
                (
                    'Your poetic Italy Honeymoon begins with absolute luxury. Arrive at Venice Marco Polo Airport and step into a private TRAGUIN wooden motorboat taxi, slicing through the lagoon to reach your canal-facing hotel pier. In the evening, step into an artisan-carved Gondola for a completely private serenade cruise through hidden, quiet waterways, admiring the historic scenic beauty of the city. Sightseeing Included: Private luxury water taxi airport reception, private candlelit Gondola serenade cruise. Honeymoon Highlight: Complimentary chilled Italian Prosecco and red roses awaiting in your honeymoon suite.'
                ),
                [
                    'Overnight Stay: Venice Lagoon (Handpicked Ultra-Luxury Canal-view Palace Hotel)',
                    'Meals Included: Waterfront Candlelight Welcome Dinner',
                ],
            ),
            _day(
                2,
                "THE ISLANDS OF LOVE & TWILIGHT IN ST. MARK'S",
                (
                    "Enjoy a beautiful breakfast at your hotel porch facing the Grand Canal. Today, embark on a private speedboat excursion to Murano and Burano. Wander past Burano’s iconic brightly painted houses—a premier popular Instagram location. In the evening, walk hand-in-hand through St. Mark's Square as the orchestras begin playing under the golden twilight. Sightseeing Included: Private speedboat excursion to Venetian islands, St. Mark's Basilica twilight trail."
                ),
                [
                    'Overnight Stay: Venice Lagoon (Handpicked Ultra-Luxury Canal-view Palace Hotel)',
                    'Meals Included: International Breakfast & Intimate Venetian Terrace Dinner',
                ],
            ),
            _day(
                3,
                'HIGH-SPEED TRAIN TO TUSCAN HARMONY',
                (
                    'Check out smoothly as your private water taxi transfers you to the rail terminal. Board the high-speed Executive Train to Florence, relaxing in spacious leather recliners. Upon arrival, your private TRAGUIN chauffeur guides you into the Tuscan hills. Check into your countryside boutique resort, enjoying breathtaking landscapes of vineyards stretching across the horizon. Sightseeing Included: High-speed executive rail connection, private Tuscan countryside chauffeured transit.'
                ),
                [
                    'Overnight Stay: Tuscany Countryside (Handpicked Ultra-Luxury Boutique Wine Resort)',
                    'Meals Included: International Breakfast & Traditional Tuscan Farm-to-Table Dinner',
                ],
            ),
            _day(
                4,
                'VINTAGE DRIVING BLISS & CHIANTI TASTING',
                (
                    'An extraordinary honeymoon experience awaits. Take the keys to a beautifully restored vintage Alfa Romeo or classic car for a private self-drive tour through the winding Cypress-lined roads of Chianti. Stop at a medieval castle for a private cellar tour and exclusive wine tasting paired with local truffles, surrounded by scenic vineyards. Sightseeing Included: Vintage sports car rental day, private castle wine tasting tour, San Gimignano panoramic trail.'
                ),
                [
                    'Overnight Stay: Tuscany Countryside (Handpicked Ultra-Luxury Boutique Wine Resort)',
                    'Meals Included: International Breakfast & Gourmet Vineyard Estate Lunch',
                ],
            ),
            _day(
                5,
                'FLIGHT OF THE SOUL TO THE AMALFI CLIFFS',
                (
                    'Bid farewell to Tuscany as your private executive van drives you to the rail station for a fast-track link to Naples. Upon arrival, your Amalfi coastal driver transfers you along the spectacular cliffside highway. Check into an iconic cliff-hanging resort in Positano, where your private balcony overlooks the vertical pastel houses and the deep blue sea. Sightseeing Included: High-speed rail crossing, Amalfi scenic cliffside private transit, Positano village arrival.'
                ),
                [
                    'Overnight Stay: Amalfi Coast / Positano (Handpicked Premium Cliffside Luxury Resort)',
                    'Meals Included: International Breakfast & Ocean-view Mediterranean Dinner',
                ],
            ),
            _day(
                6,
                'PRIVATE YACHT CRUISE TO CAPRI & FAREWELL GALA',
                (
                    'Savor a final full day in paradise. Board a private luxury speed-yacht chartered exclusively by TRAGUIN Experts. Cruise around the dramatic limestone monoliths of Capri, swim inside hidden turquoise sea caves, and have lunch at a secluded beach club. Conclude your honeymoon with an ultimate private candlelight farewell dinner on a cliffside terrace over the Mediterranean waves. Sightseeing Included: Private luxury yacht charter to Capri, Faraglioni Rocks cruise, sea caves exploration. Honeymoon Finale: Private musicians playing acoustic Italian love songs during a multi-course dinner.'
                ),
                [
                    'Overnight Stay: Amalfi Coast / Positano (Handpicked Premium Cliffside Luxury Resort)',
                    'Meals Included: International Breakfast & Grand Honeymoon Finale Candlelight Dinner',
                ],
            ),
            _day(
                7,
                'SUNSET CHECKOUT & NAPLES DEPARTURE',
                (
                    'Enjoy a late morning breakfast on your private balcony, capturing the final, stunning memories of Positano. Our concierge team completely manages your premium checkout and luggage lines. Your private vehicle transfers you comfortably back to Naples International Airport for your departure flights, concluding a flawless dream honeymoon. Transfers: Private luxury highway van transfer to Naples Airport, full luggage assistance.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                "Hotel Carlton Grand Canal Hotel Adler Cavalieri Hotel Conca d'Oro Positano",
                'Multi-city Italy',
                '6N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description="Option 01: Deluxe — Hotel Carlton Grand Canal Hotel Adler Cavalieri Hotel Conca d'Oro Positano",
            ),
            _hotel(
                'Splendid Venice Starhotels Borgo San Luigi ChiantiHotel Poseidon Positano',
                'Multi-city Italy',
                '6N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Splendid Venice Starhotels Borgo San Luigi ChiantiHotel Poseidon Positano',
            ),
            _hotel(
                'The Gritti Palace Venice Castello di Velona ResortLe Sirenuse Positano',
                'Multi-city Italy',
                '6N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Gritti Palace Venice Castello di Velona ResortLe Sirenuse Positano',
            ),
            _hotel(
                'Aman Venice / St. Regis Rosewood Castiglion del Bosco Belmond Hotel Caruso / Monastero Santa Rosa',
                'Multi-city Italy',
                '6N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Aman Venice / St. Regis Rosewood Castiglion del Bosco Belmond Hotel Caruso / Monastero Santa Rosa',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Italy', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven MPV', 2),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 3),
            _inc_excluded('International airfare and Schengen visa fees', 4),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 5),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 6),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 7),
        ],
    )
    return package, itinerary

def build_it_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'IT-003'
    tour_code = 'TRG-ITA-LUXURY-2026'
    title = 'Luxury Italy Grand Expedition'
    duration = '07 Nights / 08 Days'
    slug = 'it-003-luxury-italy-grand-expedition'
    itin_slug = 'it-003-luxury-italy-itinerary'
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
            _ph('Serial code IT-003 | TRAGUIN tour code TRG-ITA-LUXURY-2026', 1),
            _ph('Country: Italy, Europe | Category: Luxury Italy Holiday Grand Expedition', 2),
            _ph('Destinations: Rome (2N) • Florence /', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury MPV / Buffet Breakfast & Curated Dinners', 7)
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
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Luxury Italy Grand Expedition',
        overview="Rome Private After-Hours • Private Tuscan Estate • Lake Como Riva Charter • Venetian Palace Stays 07 Nights / 08 Days Ultimate Ultra-Luxury Italy Sovereign Showcase SERIAL CODE: IT-003 TRAGUIN TOUR CODE: TRG-ITA-LUXURY-2026 STATE / COUNTRY: Italy / Europe CATEGORY: Luxury Italy Holiday Grand Expedition DURATION: 07 Nights / 08 Days DESTINATIONS COVERED: Rome (2N) • Florence / Tuscany (2N) • Lake Como (2N) • Venice (1N)\n\nTOUR OVERVIEW\nIndulge in the absolute zenith of European opulence with our crown jewel TRAGUIN curated sovereign expedition. Meticulously designed for the world's most discerning travelers, this Luxury Italy Holiday links high-security ancient private openings, Michelin-starred gastronomic estates, classic wood-hulled lake transits, and historic grand canal palaces to create seamless, unforgettable memories. Sovereign Note from TRAGUIN: Uncompromised discretion is our signature. This 8-day private journey includes comprehensive VIP airfield arrivals, dedicated luxury ground logistics in private high-end vehicles, priority fast-track entry protocols, and personal concierge managers handling all movement lines perfectly.\n\nWHY CHOOSE OUR ULTIMATE LUXURY ITALY FRAMEWORK?\nItaly represents the world's finest canvas of lifestyle heritage, majestic architecture, and sartorial craftsmanship. Booking our flagship Premium Italy Experience guarantees an unparalleled curation of the country's ultimate treasures. This professional proposal format relies on highly searches keywords for Google ranking, ensuring an exceptional client presentation format for elite travelers looking for high-end Italy Sightseeing marvels. Discover Top Tourist Places in Italy through unprecedented access: walk through the Colosseum via private gladiator gates, access Vatican collections after-hours, cruise on custom-crafted Riva yachts past legendary Lake Como villas, and reside inside historic Venetian palazzos. It is the absolute Best Time to Visit Italy to experience curated experiences, celebrate exclusive experiences, and photograph breathtaking landscapes in ultimate sophistication. TRAGUIN Luxury Signatures: Private after-hours access to the Vatican Museums, helicopter flight across the Tuscan vineyards, private chartered wooden Riva boat day on Lake Como, and elite personal butler assignments throughout the grand stays. THE DEFINITIVE DAY-WISE ITINERARY",
        seo_title='IT-003 | Luxury Italy Grand Expedition | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Italy package (IT-003 / TRG-ITA-LUXURY-2026): Rome (2N) • Florence / with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN THE ETERNAL CITY & PRIVATE COLOSSEUM ENTRY', 1),
            _ih('Day 02: PRIVATE AFTER-HOURS VATICAN ACCESS', 2),
            _ih('Day 03: ROME TO TUSCANY VIA PRIVATE HELICOPTER FLIGHT', 3),
            _ih('Day 04: PRIVILEGED FLORENCE CONCIERGE & DUOMO TRAIL', 4),
            _ih('Day 05: TUSCANY TO LAKE COMO VIA RIVA YACHT CHARTER', 5),
            _ih('Day 06: LAKE COMO SECLUSION & BELLAGIO CHARM', 6),
            _ih('Day 07: HIGH-SPEED LUXURY RAIL TRANSIT TO VENICE BALCONIES', 7),
            _ih('Day 08: HIGH-END RESORT FAREWELL & DEPARTURE', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN THE ETERNAL CITY & PRIVATE COLOSSEUM ENTRY',
                (
                    "ROME SOVEREIGN ARRIVAL – EXCLUSIVE GLADIATOR GATE PATHWAYS Your ultimate Luxury Italy Holiday begins with VIP aircraft-side greeting at Rome Fiumicino Airport. Skip all customs lines via private pathways as your dedicated TRAGUIN luxury chauffeur transfers you to your hotel in a premium high-end sedan. In the afternoon, enjoy an exclusive, private tour of the monumental Colosseum, entering directly through the Gladiator's Gate to stand alone on the arena floor away from public access corridors. Sightseeing Included: VIP aircraft-side airfield greeting, Colosseum private arena floor entrance. Evening Experience: Welcome multi-course dinner at a Michelin-starred rooftop restaurant overlooking the Roman Forum."
                ),
                [
                    'Overnight Stay: Rome Centre (Handpicked Ultra-Luxury Heritage Palace Hotel)',
                    'Meals Included: Gourmet Tasting Menu Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PRIVATE AFTER-HOURS VATICAN ACCESS',
                (
                    "SISTINE CHAPEL IN SILENCE – UNPRECEDENTED ARTISTIC PRIVILEGE Savor a gourmet breakfast served privately in your suite. Spend a relaxed morning shopping for tailored couture along Via Condotti. In the evening, experience the ultimate milestone: a private, after-hours tour of the Vatican Museums and the Sistine Chapel after the doors close to the public. Walk through the hall of maps in complete silence and stand directly under Michelangelo's ceiling alone with your private historian guide. Sightseeing Included: Exclusive after-hours private Vatican Museums & Sistine Chapel opening."
                ),
                [
                    'Overnight Stay: Rome Centre (Handpicked Ultra-Luxury Heritage Palace Hotel)',
                    'Meals Included: International Breakfast & Traditional Roman Fine Dining Lunch',
                ],
            ),
            _day(
                3,
                'ROME TO TUSCANY VIA PRIVATE HELICOPTER FLIGHT',
                (
                    "SKYWARD LUXURY – VAL D'ORCIA VISTAS & PRIVATE WINE RETREAT Check out as your chauffeur transfers you to the private helipad. Board a luxury helicopter for a breathtaking flight north across the rolling, cypress-lined breathtaking landscapes of Tuscany's Val d'Orcia. Land directly on the lawn of an ultra-exclusive medieval castle wine estate. Spend your afternoon enjoying a private vineyard tour and a rare vintage Brunello collection tasting with the estate's head sommelier. Sightseeing Included: Private helicopter flight from Rome to Tuscany, Brunello private cellar tasting."
                ),
                [
                    'Overnight Stay: Tuscany Estate (Handpicked Ultra-Luxury Wine Resort & Sanctuary)',
                    'Meals Included: International Breakfast & Exclusive Vineyard Estate Pairing Lunch',
                ],
            ),
            _day(
                4,
                'PRIVILEGED FLORENCE CONCIERGE & DUOMO TRAIL',
                (
                    "RENAISSANCE MASTERY – MICHELANGELO'S DAVID IN PRIVATE VIEW Your private chauffeur transfers you to Florence in a high-end luxury vehicle. Enjoy private, priority access to the Uffizi Gallery and Accademia Gallery to stand face-to-face with Michelangelo's David. Later, enjoy private fashion ateliers before returning to your serene countryside estate. Sightseeing Included: Uffizi & Accademia VIP private entry, Duomo private terrace balcony look."
                ),
                [
                    "shopping: with an expert personal fashion consultant inside the city's historic leather workshops and high-",
                    'Overnight Stay: Tuscany Estate (Handpicked Ultra-Luxury Wine Resort & Sanctuary)',
                    'Meals Included: International Breakfast & Fine Dining Tuscan Gastronomy Dinner',
                ],
            ),
            _day(
                5,
                'TUSCANY TO LAKE COMO VIA RIVA YACHT CHARTER',
                (
                    "ALPINE GLAMOUR – THE WATERWAY ENTRANCE TO SUNSET VILLAS Travel north via a private executive transfer to the spectacular alpine shores of Lake Como. Arrive at the private pier to board a custom, mahogany-hulled Riva speedboat chartered exclusively by TRAGUIN Experts. Cruise past legendary historic villas like Villa d'Este and Villa del Balbianello, sipping fine champagne as you arrive directly at your ultra-luxury lakeside palace resort. Sightseeing Included: Private high-end overland transfer, private mahogany Riva Yacht charter cruise."
                ),
                [
                    'Overnight Stay: Lake Como (Handpicked Ultra-Luxury Waterfront Palace Resort)',
                    'Meals Included: International Breakfast & Lakeside Al Fresco Gourmet Dinner',
                ],
            ),
            _day(
                6,
                'LAKE COMO SECLUSION & BELLAGIO CHARM',
                (
                    "AMPHIBIOUS REFINEMENT – PRIVATE SPEEDED EXPEDITIONS Spend a relaxing morning enjoying your resort's floating swimming pool and private world-class spa facilities. In the afternoon, your private water craft escorts you to the beautiful village of Bellagio. Explore the terraced botanical gardens of Villa Melzi with a private guide, capturing magnificent view blocks of the sapphire lake water and surrounding mountain peaks. Sightseeing Included: Villa Melzi botanical private pass, private water taxi transfers to Bellagio."
                ),
                [
                    'Overnight Stay: Lake Como (Handpicked Ultra-Luxury Waterfront Palace Resort)',
                    'Meals Included: International Breakfast & Fine Dining Lakefront Dinner',
                ],
            ),
            _day(
                7,
                'HIGH-SPEED LUXURY RAIL TRANSIT TO VENICE BALCONIES',
                (
                    'THE FLOATING PALAZZO – PRIVATE WATER TAXI & GRAND CANAL APEX Board the high-speed Executive Train to Venice, enjoying total privacy. Upon arrival, a private luxury water taxi escorts your family to your grand canal palazzo hotel. In the evening, enjoy a private sunset cruise aboard a historic vintage wooden vessel, sipping refreshments while drifting past the magnificent Venetian architecture as the city lights illuminate. Sightseeing Included: High-speed executive rail transit, private water taxi, vintage vessel sunset cruise. Evening Experience: Grand farewell candlelight dinner event on a private terrace facing the Grand Canal.'
                ),
                [
                    'Overnight Stay: Venice Island (Handpicked Grand Luxury Canal-view Palace Hotel)',
                    'Meals Included: International Breakfast & Grand Farewell Venetian Dinner',
                ],
            ),
            _day(
                8,
                'HIGH-END RESORT FAREWELL & DEPARTURE',
                (
                    "SOVEREIGN CLOSING – SEAMLESS AIRPORT WATER TRANSIT Savor a luxurious breakfast on your private terrace overlooking the Venetian lagoon. Your dedicated personal butler handles all checkout lines and luggage coordination seamlessly. Board your private water taxi directly to Venice Marco Polo Airport's VIP terminal for your departure flight home, concluding an extraordinary grand vacation. Transfers: Private luxury water taxi airport departure transit, VIP luggage coordination. HANDPICKED ELITE SOVEREIGN ACCOMMODATIONS Category Rome Centre (2N) Tuscany Hills (2N)Lake Como Resort (2N) Venice Palazzo (1N) OPTION 01 – DELUXE Hotel Grand Palatino Hotel Adler CavalieriGrand Hotel Tremezzo Hotel Carlton Grand Canal OPTION 02 – PREMIUM Starhotels Metropole Borgo San Luigi Chianti Villa d'Este Lake Como Splendid Venice Starhotels OPTION 03 – LUXURY Anantara Palazzo Naiadi Castello di Velona Resort Mandarin Oriental Como The Gritti Palace Venice OPTION 04 – ULTRA LUXURY Hotel de Russie Rosewood Castiglion del Bosco Il Sereno / Villa d'Este Palace Aman Venice / St. Regis Grand"
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Grand Palatino Hotel Adler CavalieriGrand Hotel Tremezzo Hotel Carlton Grand Canal',
                'Multi-city Italy',
                '7N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Hotel Grand Palatino Hotel Adler CavalieriGrand Hotel Tremezzo Hotel Carlton Grand Canal',
            ),
            _hotel(
                "Starhotels Metropole Borgo San Luigi Chianti Villa d'Este Lake Como Splendid Venice Starhotels",
                'Multi-city Italy',
                '7N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description="Option 02: Premium — Starhotels Metropole Borgo San Luigi Chianti Villa d'Este Lake Como Splendid Venice Starhotels",
            ),
            _hotel(
                'Anantara Palazzo Naiadi Castello di Velona Resort Mandarin Oriental Como The Gritti Palace Venice',
                'Multi-city Italy',
                '7N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Anantara Palazzo Naiadi Castello di Velona Resort Mandarin Oriental Como The Gritti Palace Venice',
            ),
            _hotel(
                "Hotel de Russie Rosewood Castiglion del Bosco Il Sereno / Villa d'Este Palace Aman Venice / St. Regis Grand",
                'Multi-city Italy',
                '7N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description="Option 04: Ultra Luxury — Hotel de Russie Rosewood Castiglion del Bosco Il Sereno / Villa d'Este Palace Aman Venice / St. Regis Grand",
            )
        ],
        inclusions=[
            _inc_included('Elite Stays: 07 Nights in world-renowned ultra-luxury palaces, wine resorts, and lake-view suites', 1),
            _inc_included("VIP Entrances: Private After-Hours Vatican Museums access and Colosseum Gladiator's Gate entries", 2),
            _inc_included('Air Logistics: Private Helicopter Flight from Rome to your Tuscan estate lawn', 3),
            _inc_included('Ground & Rail: Full ground transits in private high-end vehicles and executive first-class train layouts', 4),
            _inc_included('TRAGUIN Concierge: Dedicated 24/7 on-call personal butler coordination and local destination experts', 5),
            _inc_included('Elite Stays: 07 Nights in world-renowned ultra-luxury palaces, wine resorts, and lake-view suites', 6),
            _inc_included("VIP Entrances: Private After-Hours Vatican Museums access and Colosseum Gladiator's Gate entries", 7),
            _inc_included('Air Logistics: Private Helicopter Flight from Rome to your Tuscan estate lawn', 8),
            _inc_included('Ground & Rail: Full ground transits in private high-end vehicles and executive first-class train layouts', 9),
            _inc_included('TRAGUIN Concierge: Dedicated 24/7 on-call personal butler coordination and local destination experts', 10),
            _inc_excluded('International flight tickets and Schengen Visa entry processing fees', 11),
            _inc_excluded('Personal expenses, hotel room service, dry cleaning, mini-bar billing', 12),
            _inc_excluded('Optional extreme tours or individual gourmet dinners not specified in the flow', 13),
        ],
    )
    return package, itinerary

def build_it_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'IT-004'
    tour_code = 'TRG-ITA-CLASSIC-2026'
    title = 'Italy Classical Family Tour'
    duration = '07 Nights / 08 Days'
    slug = 'it-004-italy-classical-family-tour'
    itin_slug = 'it-004-italy-classical-family-itinerary'
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
            _ph('Serial code IT-004 | TRAGUIN tour code TRG-ITA-CLASSIC-2026', 1),
            _ph('Country: Italy, Europe | Category: Best Italy Family Tour Package', 2),
            _ph('Destinations: Rome • Vatican City • Venice Canals • Murano Island • Renaissance Florence • Tuscany', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury MPV / Buffet Breakfast & Curated Dinners', 7)
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
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Italy Classical Family Tour',
        overview="Rome • Vatican City • Venice Canals • Murano Island • Renaissance Florence • Tuscany Village 07 Nights / 08 Days Complete Italy Classical Family Vacation SERIAL CODE: IT-004 TRAGUIN TOUR CODE: TRG-ITA-CLASSIC-2026 STATE / COUNTRY: Italy / Europe CATEGORY: Best Italy Family Tour Package DURATION: 07 Nights / 08 Days Rome (3N) • Venice (2N) • Florence (2N)\n\nTOUR OVERVIEW\nUnveil the rich heritage of Europe with this definitive TRAGUIN curated classical family vacation. Seamlessly connecting the ancient architectural spires of Rome, the mesmerizing floating canals of Venice, and the unmatched artistic legacy of Florence, this Luxury Italy Holiday guarantees a beautiful combination of deep education, relaxed leisure, and unforgettable memories for all generations. Family Comfort Note from TRAGUIN: Multi-generational journeys require pristine logistical design. This 8- day optimized expedition relies on private, spacious executive land sprinters, first-class high-speed train allocations, pre-booked fast-track group entries to avoid all tedious queues, and pre-vetted family-oriented dining venues backed by our 24/7 on-ground guest care support.\n\nWHY CHOOSE OUR CLASSICAL ROME, VENICE & FLORENCE FAMILY\nTOUR? Italy remains the undisputed capital of historical storytelling, scenic diversity, and world-beloved gastronomy, providing the ultimate environment for deep family bonding. Selecting this Best Italy Tour Package guarantees comprehensive discovery across the country's three most iconic pillars. Our copy is optimized with highly searched travel keywords for Google ranking, ensuring a stellar client quotation and corporate presentation format for elite Italy Sightseeing paths. Explore the premier iconic attractions: stand inside the colossal Roman Colosseum, enjoy private water taxis along Venice's Grand Canal, and witness Michelangelo's masterpieces in Florence. It is the absolute Best Time to Visit Italy to experience private curated experiences, photograph immense breathtaking landscapes, and secure an unmatched Premium Italy Experience. TRAGUIN Family Inclusions: Private gladiator-gate entry to the Colosseum, skip-the-line early access to Vatican collections, private group glassblowing showcase on Murano Island, family pasta-making workshop in Florence, and first-class Eurostar rail tickets. THE DEFINITIVE DAY-WISE ITINERARY",
        seo_title='IT-004 | Italy Classical Family Tour | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Italy package (IT-004 / TRG-ITA-CLASSIC-2026): Rome • Vatican City • Venice Canals • Murano Island • Renaissance Florence • Tuscany with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN ROME & WELCOME GEOMETRIES', 1),
            _ih('Day 02: PRIVATE COLOSSEUM ARENA & ANCIENT FORUMS', 2),
            _ih('Day 03: VATICAN CITY MONUMENTS & TIMELESS ART', 3),
            _ih('Day 04: FIRST-CLASS HIGH-SPEED RAIL TRANSIT TO VENICE CANALS', 4),
            _ih("Day 05: ST. MARK'S REVELATIONS & MURANO GLASS EXCURSION", 5),
            _ih('Day 06: VENICE TO THE FLORENCE DUOMO SPLENDOR', 6),
            _ih('Day 07: ACCADEMIA GALLERY & FAMILY COOKING GALA', 7),
            _ih('Day 08: HIGH-END TRANSIT & FLORENCE DEPARTURE', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN ROME & WELCOME GEOMETRIES',
                (
                    'Welcome to Rome! Your classical family vacation begins with a seamless airport welcome. Your private TRAGUIN chauffeur-driven executive vehicle transfers you safely to your central hotel. In the evening, enjoy a slow orientation walk through the historic core, throwing coins into the dazzling Trevi Fountain and wandering past the monumental Pantheon, capturing beautiful family photographs. Sightseeing Included: Private luxury vehicle airport reception, Trevi Fountain & Pantheon architectural walk. Evening Experience: Family welcome dinner at an upscale traditional Roman pizzeria.'
                ),
                [
                    'Overnight Stay: Rome City Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: Traditional Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PRIVATE COLOSSEUM ARENA & ANCIENT FORUMS',
                (
                    "Enjoy a bountiful buffet breakfast. Today, step into antiquity with our private family historian guide. Skip all public crowds via pre-booked fast-track passes to step directly onto the Colosseum's Arena Floor. Explore the ruins of the Roman Forum and Palatine Hill, learning the fascinating myths of Rome's founding fathers at an easy family-friendly pace. Sightseeing Included: Colosseum Arena Floor skip-the-line entrance, Roman Forum & Palatine Hill guided trail."
                ),
                [
                    'Overnight Stay: Rome City Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: International Breakfast & Casual Roman Trattoria Lunch',
                ],
            ),
            _day(
                3,
                'VATICAN CITY MONUMENTS & TIMELESS ART',
                (
                    "Savor breakfast before heading to the sovereign Vatican City. Utilizing our priority skip-the-line group entry passes, explore the vast Vatican Museums, the geographical map galleries, and the majestic Sistine Chapel to admire Michelangelo's frescoes. Conclude the afternoon wandering through St. Peter's Square, enjoying a free evening for premium shopping. Sightseeing Included: Vatican Museums & Sistine Chapel priority entry, St. Peter's Basilica architectural tour."
                ),
                [
                    'Overnight Stay: Rome City Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: International Breakfast & Executive Square Lunch',
                ],
            ),
            _day(
                4,
                'FIRST-CLASS HIGH-SPEED RAIL TRANSIT TO VENICE CANALS',
                (
                    "Check out after a late breakfast. Board Italy's high-speed Eurostar train in First-Class Comfort, watching the country's scenic beauty zip past your large panoramic windows. Arrive at Venice water station, where a private luxury water taxi transfers your family directly to your hotel pier. In the evening, share a quiet family Gondola cruise through the serene secondary canals. Sightseeing Included: First-Class high-speed train tickets, private water taxi transfers, private group Gondola cruise."
                ),
                [
                    'Overnight Stay: Venice Island (Handpicked Premium Water-facing Hotel)',
                    'Meals Included: International Breakfast & Venetian Lagoon Canal-side Dinner',
                ],
            ),
            _day(
                5,
                "ST. MARK'S REVELATIONS & MURANO GLASS EXCURSION",
                (
                    "Explore the stunning Byzantine design of St. Mark's Basilica and the historic chambers of Doge's Palace with pre-booked group passes. In the afternoon, cruise aboard a private motorboat to Murano Island for an exclusive, private family demonstration by a master glassblower, witnessing fragile silica transformed into incredible art pieces. Sightseeing Included: Doge's Palace entry, private motorboat excursion to Murano Island, master glass show."
                ),
                [
                    'Overnight Stay: Venice Island (Handpicked Premium Water-facing Hotel)',
                    'Meals Included: International Breakfast & Island Seafood Lunch',
                ],
            ),
            _day(
                6,
                'VENICE TO THE FLORENCE DUOMO SPLENDOR',
                (
                    'Board your morning first-class rail connection south to Florence. Upon check-in at your premium boutique hotel, enjoy a private guided walking tour of the Renaissance core. Visit the monumental Florence Duomo square, Giotto’s Bell Tower, and the historic Piazza della Signoria, learning about the powerful Medici rulers who shaped history. Sightseeing Included: First-class train transit, Florence historic core walking tour, Duomo square trail.'
                ),
                [
                    'Overnight Stay: Florence Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: International Breakfast & Traditional Tuscan Osteria Dinner',
                ],
            ),
            _day(
                7,
                'ACCADEMIA GALLERY & FAMILY COOKING GALA',
                (
                    'Visit the Accademia Gallery with skip-the-line tickets to view the magnificent sculpture of David. In the afternoon, participate in a highlights event: a private family pizza and pasta-making masterclass led by an expert Italian chef. Roll dough, create authentic sauces, and celebrate your final evening together with a grand feast, cementing unforgettable memories. Sightseeing Included: Accademia Gallery David skip-the-line entrance, private family culinary academy masterclass. Evening Experience: Grand farewell family culinary graduation dinner event.'
                ),
                [
                    'Overnight Stay: Florence Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: International Breakfast & Hand-crafted Farewell Dinner Party',
                ],
            ),
            _day(
                8,
                'HIGH-END TRANSIT & FLORENCE DEPARTURE',
                (
                    'Savor your final morning breakfast at your premium hotel. Our concierge assistants coordinate your smooth checkout and take full care of all family luggage handling. Your private vehicle transfers your family comfortably to Florence Peretola Airport (or Rome connection) for your flight home, concluding your classical expedition. Transfers: Private luxury sprinter airport departure transfer, comprehensive luggage assistance.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Grand Palatino Hotel Carlton Grand Canal Hotel Adler Cavalieri',
                'Multi-city Italy',
                '7N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Hotel Grand Palatino Hotel Carlton Grand Canal Hotel Adler Cavalieri',
            ),
            _hotel(
                'Starhotels Metropole Splendid Venice Starhotels NH Collection Palazzo Gaddi',
                'Multi-city Italy',
                '7N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Starhotels Metropole Splendid Venice Starhotels NH Collection Palazzo Gaddi',
            ),
            _hotel(
                'Anantara Palazzo NaiadiThe Gritti Palace VeniceVilla Cora Florence',
                'Multi-city Italy',
                '7N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Anantara Palazzo NaiadiThe Gritti Palace VeniceVilla Cora Florence',
            ),
            _hotel(
                'Hotel de Russie Aman Venice / St. RegisFour Seasons Firenze',
                'Multi-city Italy',
                '7N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Hotel de Russie Aman Venice / St. RegisFour Seasons Firenze',
            )
        ],
        inclusions=[
            _inc_included('Stays: 07 Nights accommodation in family-friendly premium luxury interconnecting or family suites', 1),
            _inc_included('Catering: Bountiful daily breakfasts and curated specialty family dinners as per itinerary', 2),
            _inc_included('Rail & Ground: First-class high-speed train tickets and private executive luxury vans', 3),
            _inc_included('Specialty Event: Private Family Pizza & Pasta Making Masterclass with an Italian culinary expert', 4),
            _inc_excluded('International Flight tickets and Schengen Visa entry processing fees', 5),
            _inc_excluded('Personal expenses, hotel room service, dry cleaning, mini-bar billing', 6),
            _inc_excluded('Tipping, porterage fees, or optional sightseeing excursions not mentioned in the flow', 7),
        ],
    )
    return package, itinerary

def build_it_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'IT-005'
    tour_code = 'TRG-ITA-GRAND-2026'
    title = 'Grand Italy Tour'
    duration = '09 Nights / 10 Days'
    slug = 'it-005-grand-italy-tour'
    itin_slug = 'it-005-grand-italy-itinerary'
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
            _ph('Serial code IT-005 | TRAGUIN tour code TRG-ITA-GRAND-2026', 1),
            _ph('Country: Italy, Europe | Category: Premium Grand Italy Tour Package', 2),
            _ph('Destinations: Rome • Vatican City • Florence • Chianti Vineyards • Venice • Lake Como • Milan', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury MPV / Buffet Breakfast & Curated Dinners', 7)
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
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Grand Italy Tour',
        overview="09 Nights / 10 Days Grand Italy Panoramic Luxury Exploration SERIAL CODE: IT-005 TRAGUIN TOUR CODE: TRG-ITA-GRAND-2026 STATE / COUNTRY: Italy / Europe CATEGORY: Premium Grand Italy Tour Package DURATION: 09 Nights / 10 Days Rome (2N) • Florence (2N) • Venice (2N) • Lake Como (2N) • Milan (1N)\n\nTOUR OVERVIEW\nUnveil the definitive masterpiece of European exploration with this comprehensive TRAGUIN curated panoramic itinerary. Sweeping seamlessly through the historic core of Rome, the artistic cradles of Florence, the floating canals of Venice, the alpine glamour of Lake Como, and the haute-couture lanes of Milan, this Luxury Italy Holiday guarantees a beautiful combination of deep cultural enrichment, scenic wonder, and unforgettable memories across generations. Welcome Note from TRAGUIN: Prestige demands flawless logistical design. This 10-day optimized grand expedition includes private executive ground travel throughout, first-class high-speed rail layouts, pre-vetted skip-the-line VIP entrances to world heritage treasures, and handpicked premium properties providing unparalleled comfort.\n\nWHY CHOOSE OUR GRAND ITALY PANORAMIC PACKAGE?\nItaly remains the world's most dramatic storybook of majestic architecture, historic empires, and iconic culinary arts, creating a sublime canvas for an all-encompassing vacation. Selecting this Best Italy Tour Package promises a flawless, expertly paced traversal across five distinct regional cultures. This master TRAGUIN World • framework features top-performing travel keywords optimized for Google ranking, ensuring an exceptional presentation format for high-end Italy Sightseeing paths. Explore all premier iconic attractions: stand alone on the Colosseum's historic floor via exclusive gates, navigate Venice's Grand Canal via private water taxis, cruise on custom wooden speedboats across Lake Como, and admire Milan's monumental Duomo cathedral. It is the absolute Best Time to Visit Italy to experience private curated experiences, celebrate exclusive experiences, photograph immense breathtaking landscapes, and secure an unparalleled Premium Italy Experience. TRAGUIN Grand Signatures: Gladiator-gate entry at the Colosseum, private fast-track access to Vatican galleries, private wine-pairing masterclass at a Chianti estate, private mahogany Riva speedboat day on Lake Como, and first-class Eurostar rail connections. THE DEFINITIVE DAY-WISE ITINERARY",
        seo_title='IT-005 | Grand Italy Tour | TRAGUIN',
        seo_description='Premium 09 Nights / 10 Days Italy package (IT-005 / TRG-ITA-GRAND-2026): Rome • Vatican City • Florence • Chianti Vineyards • Venice • Lake Como • Milan with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN THE ETERNAL CITY & ROMAN EVENING WALK', 1),
            _ih('Day 02: EXCLUSIVE COLOSSEUM ARENA & VATICAN PALACES', 2),
            _ih('Day 03: TRANQUIL TRANSIT THROUGH CHIANTI TO FLORENCE', 3),
            _ih('Day 04: RENAISSANCE MASTERPIECES & FLORENCE WALKING TRAILS', 4),
            _ih('Day 05: FIRST-CLASS EUROSTAR RAIL TO VENICE PALACES', 5),
            _ih("Day 06: ST. MARK'S LAGOON SECRETS & BURANO EXCURSION", 6),
            _ih('Day 07: CROSSING TO ALP GLAMOUR LAKE COMO', 7),
            _ih('Day 08: PRIVATE RIVA SPEEDBOAT EXPEDITION & BELLAGIO', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN THE ETERNAL CITY & ROMAN EVENING WALK',
                (
                    'Welcome to Rome! Your grand panoramic journey begins with a seamless airport reception. Your private TRAGUIN chauffeur-driven executive coach transfers you comfortably to your central property. In the evening, enjoy a slow orientation walk through the historic cobblestone core, throwing coins into the dazzling Trevi Fountain and wandering past the monumental Pantheon, capturing beautiful photography points. Sightseeing Included: Private luxury vehicle airport reception, Trevi Fountain & Pantheon evening trail. Evening Experience: Family welcome dinner at an upscale traditional Roman trattoria. TRAGUIN World •'
                ),
                [
                    'Overnight Stay: Rome Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: Traditional Italian Welcome Dinner',
                ],
            ),
            _day(
                2,
                'EXCLUSIVE COLOSSEUM ARENA & VATICAN PALACES',
                (
                    "Savor a bountiful buffet breakfast. Today, immerse yourself in ancient history and art with your private guide. Skip all crowded public queues with fast-track passes to step directly onto the Colosseum's Arena Floor. In the afternoon, explore the magnificent Vatican Museums, the Hall of Maps, and the Sistine Chapel to view Michelangelo's majestic frescoes in complete comfort. Sightseeing Included: Colosseum Gladiator-gate entrance, Vatican Museums & Sistine Chapel priority entry."
                ),
                [
                    'Overnight Stay: Rome Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: International Breakfast & Executive Square Lunch',
                ],
            ),
            _day(
                3,
                'TRANQUIL TRANSIT THROUGH CHIANTI TO FLORENCE',
                (
                    'Travel through the scenic beauty of the rolling Tuscan hills as your private chauffeur drives you north. Stop deep in the Chianti wine region at a historic medieval castle estate. Participate in an exclusive, private wine- pairing lunch featuring local truffles and oils surrounded by vineyard breathtaking landscapes, before checking into your Florence hotel. Sightseeing Included: Private overland transfer through Tuscany, Chianti estate private cellar tour & tasting.'
                ),
                [
                    'Overnight Stay: Florence Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: International Breakfast & Gourmet Chianti Estate Lunch',
                ],
            ),
            _day(
                4,
                'RENAISSANCE MASTERPIECES & FLORENCE WALKING TRAILS',
                (
                    "Explore the cradle of the Renaissance. Visit the Accademia Gallery with pre-booked skip-the-line tickets to stand face-to-face with Michelangelo’s monumental David. Later, enjoy a guided walking tour of Florence Duomo square, Giotto's bell tower, and cross the historic leather boutiques on the Ponte Vecchio at an easy family-friendly pace. Sightseeing Included: Accademia David skip-the-line entry, Florence Duomo core walking tour, Ponte Vecchio. TRAGUIN World •"
                ),
                [
                    'Overnight Stay: Florence Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: International Breakfast & Traditional Tuscan Osteria Dinner',
                ],
            ),
            _day(
                5,
                'FIRST-CLASS EUROSTAR RAIL TO VENICE PALACES',
                (
                    'Board Italy’s high-speed Eurostar train in First-Class Comfort, watching the countryside zip past your large window panes. Arrive at Venice water station, where a private luxury water taxi transfers your group directly to your hotel pier. In the evening, share a quiet, romantic Gondola cruise through secret secondary canals. Sightseeing Included: First-Class high-speed train tickets, private water taxi transfers, private Gondola cruise.'
                ),
                [
                    'Overnight Stay: Venice Island (Handpicked Premium Water-facing Hotel)',
                    'Meals Included: International Breakfast & Venetian Lagoon Canal-side Dinner',
                ],
            ),
            _day(
                6,
                "ST. MARK'S LAGOON SECRETS & BURANO EXCURSION",
                (
                    "Explore the stunning Byzantine architecture of St. Mark's Basilica and Doge's Palace with skip-the-line passes. In the afternoon, cruise aboard a private motorboat across the lagoon to Burano island, famous for its brightly painted houses—a premier popular Instagram location—and view traditional lace workshops. Sightseeing Included: Doge's Palace entry, private motorboat excursion to Burano & Murano islands."
                ),
                [
                    'Overnight Stay: Venice Island (Handpicked Premium Water-facing Hotel)',
                    'Meals Included: International Breakfast & Island Seafood Lunch',
                ],
            ),
            _day(
                7,
                'CROSSING TO ALP GLAMOUR LAKE COMO',
                (
                    "Travel west via an executive ground coach to the deep sapphire waters of alpine Lake Como. Check into your ultra-luxury waterfront palace resort. Spend your afternoon relaxing at your resort's floating swimming pool or taking a slow walk along the flat, elegant promenades, capturing magnificent sunset view blocks. Sightseeing Included: Private ground transit to Lake Como, lakefront palace orientation check-in. TRAGUIN World •"
                ),
                [
                    'Overnight Stay: Lake Como (Handpicked Ultra-Luxury Waterfront Palace Resort)',
                    'Meals Included: International Breakfast & Lakeside Al Fresco Gourmet Dinner',
                ],
            ),
            _day(
                8,
                'PRIVATE RIVA SPEEDBOAT EXPEDITION & BELLAGIO',
                (
                    'The crown jewel highlight of your lake stay. Board a custom, mahogany-hulled Riva speedboat chartered exclusively by TRAGUIN Experts. Cruise past magnificent historical estates like Villa del Balbianello and land on the terraces of Bellagio village. Explore its terraced botanical networks with a private guide. Sightseeing Included: Private mahogany Riva Yacht charter cruise, Bellagio village guided botanical entry.'
                ),
                [
                    'Overnight Stay: Lake Como (Handpicked Ultra-Luxury Waterfront Palace Resort)',
                    'Meals Included: International Breakfast & Bellagio Lakefront Lunch',
                ],
            ),
            _day(
                9,
                'TRANSIT TO METROPOLITAN MILAN & GALA CLOSING',
                (
                    "A brief morning drive brings your delegation to Italy's design and fashion capital, Milan. Tour the jaw-dropping Duomo Cathedral square and walk through the glass-vaulted Galleria Vittorio Emanuele II high-fashion arcade. Celebrate your final evening with a grand farewell dinner party, toasting an extraordinary vacation. Sightseeing Included: Milan city drive, Duomo Square exploration, Galleria Vittorio Emanuele II arcade walk. Evening Experience: Grand farewell candlelight dinner party at a premier Milanese restaurant."
                ),
                [
                    'Overnight Stay: Milan Centre (Handpicked Premium Fashion-district Hotel)',
                    'Meals Included: International Breakfast & Grand Farewell Dinner',
                ],
            ),
            _day(
                10,
                'SEAMLESS AIRPORT TRANSIT & DEPARTURE',
                (
                    'Savor your final breakfast, packing your baggage while our concierge assistants manage your smooth checkout and handle all luggage logistics. Your private vehicle transfers your family comfortably to Milan Malpensa Airport for your departure flight home, concluding your epic grand holiday. Transfers: Private luxury coach airport transfer, comprehensive luggage coordination. TRAGUIN World •'
                ),
                [
                    'Meals Included: International固定 Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Grand Palatino Hotel Carlton Grand Canal Grand Hotel Tremezzo',
                'Multi-city Italy',
                '9N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Hotel Grand Palatino Hotel Carlton Grand Canal Grand Hotel Tremezzo',
            ),
            _hotel(
                "Starhotels Metropole Splendid Venice Starhotels Villa d'Este Lake Como",
                'Multi-city Italy',
                '9N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description="Option 02: Premium — Starhotels Metropole Splendid Venice Starhotels Villa d'Este Lake Como",
            ),
            _hotel(
                'Anantara Palazzo NaiadiThe Gritti Palace VeniceMandarin Oriental Como',
                'Multi-city Italy',
                '9N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Anantara Palazzo NaiadiThe Gritti Palace VeniceMandarin Oriental Como',
            ),
            _hotel(
                "Hotel de Russie Aman Venice / St. RegisIl Sereno / Villa d'Este Palace",
                'Multi-city Italy',
                '9N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description="Option 04: Ultra Luxury — Hotel de Russie Aman Venice / St. RegisIl Sereno / Villa d'Este Palace",
            )
        ],
        inclusions=[
            _inc_included('Specialty Curation: Private wine-pairing masterclass feast at a historic Chianti medieval castle estate', 1),
            _inc_included('Specialty Curation: Private wine-pairing masterclass feast at a historic Chianti medieval castle estate', 2),
            _inc_excluded('International flight tickets and Schengen Visa generation processing fees', 3),
            _inc_excluded('Personal expenses, hotel room service laundry bills, mini-bar billing', 4),
            _inc_excluded('Tipping, porterage fees, or optional sightseeing excursions not mentioned in the flow', 5),
            _inc_excluded('International flight tickets and Schengen Visa generation processing fees', 6),
            _inc_excluded('Personal expenses, hotel room service laundry bills, mini-bar billing', 7),
            _inc_excluded('Tipping, porterage fees, or optional sightseeing excursions not mentioned in the flow', 8),
        ],
    )
    return package, itinerary

ITALY_IT_001_005_BUILDERS = [
    build_it_001,
    build_it_002,
    build_it_003,
    build_it_004,
    build_it_005,
]
