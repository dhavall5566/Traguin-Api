"""Builder functions for IT-001 through IT-003 Italy packages (no images)."""

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


def build_it_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="it-001-italy-highlights-family-tour",
        destination_id=destination_id,
        title="Italy Highlights Family Tour",
        duration_label="06 Nights / 07 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=45,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Rome (2N) → Florence/Tuscany (2N) → Venice (2N) family circuit", sort_order=1),
            PackageHighlightNested(text="Vatican Museums, Sistine Chapel & Colosseum skip-the-line", sort_order=2),
            PackageHighlightNested(text="Tuscan pizza-making masterclass & high-speed train to Venice", sort_order=3),
            PackageHighlightNested(text="Private gondola cruise & Murano/Burano island hopping", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-ITA-HIGHLIGHTS-2026 | Serial IT-001", sort_order=6),
        ],
        moods=["Family", "Luxury", "Cultural"],
    )
    itinerary = ItineraryCreate(
        slug="it-001-italy-highlights-itinerary",
        destination_id=destination_id,
        title="Italy Highlights Family Tour",
        duration_label="06 Nights / 07 Days",
        duration_days=7,
        starting_price=0,
        price_note="On Request (Premium Italy Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Rome • Vatican City • Florence • Tuscany • Venice",
        overview=(
            "Embark on an extraordinary European odyssey with TRAGUIN's curated family itinerary. Blending ancient "
            "Roman history, Renaissance art in Florence, and the romantic water matrices of Venice, this luxury Italy "
            "holiday offers unforgettable memories with private ground transit, skip-the-line admissions, and handpicked "
            "premium family hotels."
        ),
        seo_title="IT-001 | Italy Highlights Family Tour | TRAGUIN",
        seo_description=(
            "Premium 06 Nights / 07 Days Italy family package (IT-001): Rome, Vatican, Colosseum, "
            "Florence, Tuscany, Venice gondola, and Murano/Burano islands."
        ),
        is_featured=True,
        featured_sort_order=45,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Vatican Museums & Sistine Chapel", sort_order=1),
            ItineraryHighlightNested(text="Colosseum & Roman Forum", sort_order=2),
            ItineraryHighlightNested(text="Florence Duomo & Accademia Gallery", sort_order=3),
            ItineraryHighlightNested(text="Private Gondola Cruise in Venice", sort_order=4),
            ItineraryHighlightNested(text="Murano & Burano Island Excursion", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Rome & Historic Ambiance", "Arrive at Rome Fiumicino Airport with private TRAGUIN chauffeur transfer. Evening stroll through Piazza Navona and Trevi Fountain. Family welcome dinner at an upscale Roman trattoria.", ["Sightseeing Included: Private airport transfer, Trevi Fountain & Piazza Navona evening walk", "Evening Experience: Family welcome dinner at upscale Roman trattoria", "Overnight Stay: Rome Centre (Handpicked Premium Family Hotel)", "Meals Included: Traditional Italian Welcome Dinner"]),
            _day(2, "Vatican Museums & The Colosseum", "Skip-the-line entry to Vatican Museums, Sistine Chapel, and St. Peter's Basilica. Afternoon private guided tour of the Colosseum and Roman Forum.", ["Sightseeing Included: Vatican Museums & Sistine Chapel skip-the-line, private Colosseum guided tour", "Overnight Stay: Rome Centre (Handpicked Premium Family Hotel)", "Meals Included: International Breakfast & Casual Italian Bistro Lunch"]),
            _day(3, "Scenic Highway to Renaissance Florence", "Private chauffeur drive through Umbrian and Tuscan hills to Florence. Panoramic view from Piazzale Michelangelo and stroll across Ponte Vecchio.", ["Sightseeing Included: Private overland transfer through Tuscany, Piazzale Michelangelo, Ponte Vecchio", "Overnight Stay: Florence / Tuscany Boutique Resort (Premium Stay)", "Meals Included: International Breakfast & Tuscan Countryside Lunch"]),
            _day(4, "Florence Artisans & Tuscan Village Exploration", "Explore Florence Duomo and Michelangelo's David at Accademia Gallery. Afternoon private family pizza-making masterclass at a historic Tuscan estate.", ["Sightseeing Included: Accademia Gallery skip-the-line, Florence Duomo square stroll", "Optional Activities: Private family pizza-making workshop at Tuscan villa", "Overnight Stay: Florence / Tuscany Boutique Resort (Premium Stay)", "Meals Included: International Breakfast & Curated Tuscan Dinner"]),
            _day(5, "Speed Transit to the Canals of Venice", "High-speed executive train to Venice. Private luxury water taxi to hotel. Evening private gondola cruise through secret canals with traditional serenades.", ["Sightseeing Included: High-speed executive train, private water taxi, private gondola cruise", "Overnight Stay: Venice Island (Handpicked Premium Water-facing Hotel)", "Meals Included: International Breakfast & Venetian Lagoon Seafood Dinner"]),
            _day(6, "St. Mark's Square & Island Hopping", "Explore St. Mark's Square and Doge's Palace with skip-the-line entry. Afternoon motorboat excursion to Murano and Burano islands. Grand farewell dinner on canal-side terrace.", ["Sightseeing Included: Doge's Palace entry, Murano & Burano island motorboat excursion", "Evening Experience: Grand farewell dinner on canal-side terrace", "Overnight Stay: Venice Island (Handpicked Premium Water-facing Hotel)", "Meals Included: International Breakfast & Grand Farewell Dinner"]),
            _day(7, "Venice Departure", "Final morning breakfast along the Grand Canal. Private water taxi to Venice Marco Polo Airport with luggage assistance.", ["Transfers Included: Private water taxi airport departure, luggage assistance", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Hotel Grand Palatino / similar", location="Rome", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="Hotel Adler Cavalieri / similar", location="Florence / Tuscany", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="Hotel Carlton Grand Canal / similar", location="Venice", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=3),
            ItineraryHotelNested(name="Starhotels Metropole", location="Rome", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=4),
            ItineraryHotelNested(name="NH Collection Palazzo Gaddi", location="Florence", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="Splendid Venice Starhotels", location="Venice", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="Anantara Palazzo Naiadi", location="Rome", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="Villa Cora Florence", location="Florence", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=8),
            ItineraryHotelNested(name="The Gritti Palace Venice", location="Venice", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=9),
            ItineraryHotelNested(name="Hotel de Russie", location="Rome", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=10),
            ItineraryHotelNested(name="Four Seasons Firenze", location="Florence", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=11),
            ItineraryHotelNested(name="Aman Venice / St. Regis", location="Venice", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=12),
        ],
        inclusions=_it001_inclusions(),
    )
    return package, itinerary


def _it001_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="06 Nights accommodation in family-friendly premium luxury rooms across Rome, Florence, and Venice", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Bountiful daily breakfasts and curated specialty dinners", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Private luxury overland vehicles, executive train connections, and water taxis", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Pre-booked skip-the-line entry to Colosseum, Vatican, and Doge's Palace", sort_order=4),
        ItineraryInclusionNested(kind="included", text="TRAGUIN local English-speaking destination experts and 24/7 guest care hotline", sort_order=5),
        ItineraryInclusionNested(kind="excluded", text="International flight tickets and Schengen visa processing fees", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, hotel laundry, telephone calls, mini-bar consumption", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, or optional sightseeing not mentioned", sort_order=8),
    ]


def build_it_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="it-002-romantic-italy-honeymoon",
        destination_id=destination_id,
        title="Romantic Italy Honeymoon",
        duration_label="06 Nights / 07 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=46,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Venice (2N) → Tuscany (2N) → Amalfi Coast (2N) romantic circuit", sort_order=1),
            PackageHighlightNested(text="Private gondola serenade & Murano/Burano speedboat excursion", sort_order=2),
            PackageHighlightNested(text="Vintage Chianti drive & private castle wine tasting", sort_order=3),
            PackageHighlightNested(text="Private yacht cruise to Capri & cliffside farewell gala", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 honeymoon concierge desk support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-ITA-ROMANCE-2026 | Serial IT-002", sort_order=6),
        ],
        moods=["Romantic", "Luxury", "Cultural", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="it-002-romantic-italy-itinerary",
        destination_id=destination_id,
        title="Romantic Italy Honeymoon",
        duration_label="06 Nights / 07 Days",
        duration_days=7,
        starting_price=0,
        price_note="On Request (Premium Honeymoon Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Venice • Florence • Chianti • Amalfi Coast",
        overview=(
            "Begin your lifelong love story amid the most poetic realms of the Mediterranean with TRAGUIN's curated "
            "honeymoon retreat. Candlelit water matrices, vintage Tuscan road explorations, and spectacular cliffside "
            "vistas along the Amalfi coast — with private water taxis, skip-the-line VIP access, and 24/7 concierge support."
        ),
        seo_title="IT-002 | Romantic Italy Honeymoon | TRAGUIN",
        seo_description=(
            "Premium 06 Nights / 07 Days Italy honeymoon (IT-002): Venice gondola, Tuscany Chianti, "
            "Amalfi Coast Positano, and private Capri yacht cruise."
        ),
        is_featured=True,
        featured_sort_order=46,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Private Gondola Serenade in Venice", sort_order=1),
            ItineraryHighlightNested(text="Murano & Burano Private Speedboat", sort_order=2),
            ItineraryHighlightNested(text="Vintage Chianti Drive & Wine Tasting", sort_order=3),
            ItineraryHighlightNested(text="Positano Cliffside Resort Stay", sort_order=4),
            ItineraryHighlightNested(text="Private Yacht Cruise to Capri", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Venice & Private Canal Cruise", "Arrive at Venice Marco Polo Airport and board a private TRAGUIN wooden motorboat taxi to your canal-facing hotel. Evening private candlelit gondola serenade through hidden waterways.", ["Sightseeing Included: Private water taxi airport reception, private gondola serenade cruise", "Honeymoon Highlight: Complimentary Prosecco and red roses in honeymoon suite", "Overnight Stay: Venice Lagoon (Ultra-Luxury Canal-view Palace Hotel)", "Meals Included: Waterfront Candlelight Welcome Dinner"]),
            _day(2, "The Islands of Love & Twilight in St. Mark's", "Private speedboat excursion to Murano and Burano. Evening walk through St. Mark's Square at golden twilight.", ["Sightseeing Included: Private speedboat to Murano & Burano, St. Mark's Basilica twilight trail", "Overnight Stay: Venice Lagoon (Ultra-Luxury Canal-view Palace Hotel)", "Meals Included: International Breakfast & Intimate Venetian Terrace Dinner"]),
            _day(3, "High-Speed Train to Tuscan Harmony", "Private water taxi to rail terminal. High-speed executive train to Florence and private chauffeur into Tuscan hills. Check into countryside boutique wine resort.", ["Sightseeing Included: High-speed executive rail, private Tuscan countryside transit", "Overnight Stay: Tuscany Countryside (Ultra-Luxury Boutique Wine Resort)", "Meals Included: International Breakfast & Traditional Tuscan Farm-to-Table Dinner"]),
            _day(4, "Vintage Driving Bliss & Chianti Tasting", "Restored vintage Alfa Romeo self-drive through Chianti cypress-lined roads. Private castle cellar tour and exclusive wine tasting with local truffles.", ["Sightseeing Included: Vintage sports car day, private castle wine tasting, San Gimignano panoramic trail", "Overnight Stay: Tuscany Countryside (Ultra-Luxury Boutique Wine Resort)", "Meals Included: International Breakfast & Gourmet Vineyard Estate Lunch"]),
            _day(5, "Flight of the Soul to the Amalfi Cliffs", "Private executive van to Naples via high-speed rail. Amalfi coastal drive to Positano cliff-hanging resort with balcony overlooking the sea.", ["Sightseeing Included: High-speed rail crossing, Amalfi scenic cliffside transit, Positano arrival", "Overnight Stay: Amalfi Coast / Positano (Premium Cliffside Luxury Resort)", "Meals Included: International Breakfast & Ocean-view Mediterranean Dinner"]),
            _day(6, "Private Yacht Cruise to Capri & Farewell Gala", "Private luxury speed-yacht charter to Capri. Swim in turquoise sea caves. Ultimate candlelight farewell dinner with acoustic Italian musicians.", ["Sightseeing Included: Private yacht charter to Capri, Faraglioni Rocks cruise, sea caves", "Honeymoon Finale: Private musicians during multi-course cliffside dinner", "Overnight Stay: Amalfi Coast / Positano (Premium Cliffside Luxury Resort)", "Meals Included: International Breakfast & Grand Honeymoon Finale Dinner"]),
            _day(7, "Sunset Checkout & Naples Departure", "Late morning breakfast on private balcony. Private transfer to Naples International Airport with luggage assistance.", ["Transfers Included: Private luxury van to Naples Airport, luggage assistance", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Hotel Carlton Grand Canal / similar", location="Venice", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="Hotel Adler Cavalieri / similar", location="Tuscany", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="Hotel Conca d'Oro Positano / similar", location="Amalfi Coast / Positano", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=3),
            ItineraryHotelNested(name="Splendid Venice Starhotels", location="Venice", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=4),
            ItineraryHotelNested(name="Borgo San Luigi Chianti", location="Tuscany", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="Hotel Poseidon Positano", location="Positano", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="The Gritti Palace Venice", location="Venice", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="Castello di Velona Resort", location="Tuscany", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=8),
            ItineraryHotelNested(name="Le Sirenuse Positano", location="Positano", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=9),
            ItineraryHotelNested(name="Aman Venice / St. Regis", location="Venice", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=10),
            ItineraryHotelNested(name="Rosewood Castiglion del Bosco", location="Tuscany", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=11),
            ItineraryHotelNested(name="Belmond Hotel Caruso / Monastero Santa Rosa", location="Amalfi Coast", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=12),
        ],
        inclusions=_it002_inclusions(),
    )
    return package, itinerary


def _it002_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="06 Nights in ultra-luxury canal-view, vineyard, and cliffside honeymoon suites", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Complimentary premium prosecco, seasonal fruits, and floral setups on arrival", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Private luxury water crafts, high-speed executive trains, and Mercedes transits", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Private gondola serenade, Chianti wine tasting, and luxury Capri yacht cruise", sort_order=4),
        ItineraryInclusionNested(kind="included", text="VIP skip-the-line entries and TRAGUIN 24/7 honeymoon concierge support", sort_order=5),
        ItineraryInclusionNested(kind="excluded", text="International flight tickets and Schengen visa processing fees", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar billing", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Vintage car fuel insurance upgrades or extra sightseeing not specified", sort_order=8),
    ]


def build_it_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="it-003-luxury-italy-grand-expedition",
        destination_id=destination_id,
        title="Luxury Italy Grand Expedition",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=47,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Rome (2N) → Tuscany (2N) → Lake Como (2N) → Venice (1N) sovereign circuit", sort_order=1),
            PackageHighlightNested(text="Colosseum Gladiator's Gate & after-hours Vatican access", sort_order=2),
            PackageHighlightNested(text="Private helicopter to Tuscany & Riva yacht on Lake Como", sort_order=3),
            PackageHighlightNested(text="Uffizi, Accademia VIP & Bellagio botanical gardens", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 personal butler coordination", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-ITA-LUXURY-2026 | Serial IT-003", sort_order=6),
        ],
        moods=["Luxury", "Family", "Cultural", "Romantic"],
    )
    itinerary = ItineraryCreate(
        slug="it-003-luxury-italy-itinerary",
        destination_id=destination_id,
        title="Luxury Italy Grand Expedition",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="On Request (Ultra-Luxury Italy Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Rome • Tuscany • Lake Como • Venice",
        overview=(
            "Indulge in the absolute zenith of European opulence with TRAGUIN's sovereign expedition. Private after-hours "
            "Vatican access, helicopter flight across Tuscan vineyards, custom Riva yacht on Lake Como, and historic "
            "Venetian palazzo stays — designed for the world's most discerning travelers."
        ),
        seo_title="IT-003 | Luxury Italy Grand Expedition | TRAGUIN",
        seo_description=(
            "Ultra-luxury 07 Nights / 08 Days Italy package (IT-003): Colosseum private access, after-hours Vatican, "
            "helicopter to Tuscany, Lake Como Riva yacht, and Venice palazzo stay."
        ),
        is_featured=True,
        featured_sort_order=47,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Colosseum Gladiator's Gate Private Entry", sort_order=1),
            ItineraryHighlightNested(text="After-Hours Vatican & Sistine Chapel", sort_order=2),
            ItineraryHighlightNested(text="Private Helicopter to Tuscany", sort_order=3),
            ItineraryHighlightNested(text="Mahogany Riva Yacht on Lake Como", sort_order=4),
            ItineraryHighlightNested(text="Venice Grand Canal Palazzo Stay", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Rome & Private Colosseum Entry", "VIP aircraft-side greeting at Rome Fiumicino. Private luxury transfer to hotel. Exclusive Colosseum tour through the Gladiator's Gate to the arena floor. Michelin-starred rooftop welcome dinner.", ["Sightseeing Included: VIP aircraft-side greeting, Colosseum private arena floor entrance", "Evening Experience: Michelin-starred rooftop welcome dinner overlooking Roman Forum", "Overnight Stay: Rome Centre (Ultra-Luxury Heritage Palace Hotel)", "Meals Included: Gourmet Tasting Menu Welcome Dinner"]),
            _day(2, "Private After-Hours Vatican Access", "Relaxed morning shopping on Via Condotti. Private after-hours tour of Vatican Museums and Sistine Chapel with historian guide.", ["Sightseeing Included: Exclusive after-hours private Vatican Museums & Sistine Chapel opening", "Overnight Stay: Rome Centre (Ultra-Luxury Heritage Palace Hotel)", "Meals Included: International Breakfast & Traditional Roman Fine Dining Lunch"]),
            _day(3, "Rome to Tuscany via Private Helicopter", "Luxury helicopter flight across Val d'Orcia to medieval castle wine estate. Private Brunello cellar tasting with head sommelier.", ["Sightseeing Included: Private helicopter Rome to Tuscany, Brunello private cellar tasting", "Overnight Stay: Tuscany Estate (Ultra-Luxury Wine Resort & Sanctuary)", "Meals Included: International Breakfast & Exclusive Vineyard Estate Pairing Lunch"]),
            _day(4, "Privileged Florence Concierge & Duomo Trail", "Private VIP access to Uffizi and Accademia Galleries. Private shopping with fashion consultant in Florence leather workshops. Return to countryside estate.", ["Sightseeing Included: Uffizi & Accademia VIP private entry, Duomo private terrace balcony", "Overnight Stay: Tuscany Estate (Ultra-Luxury Wine Resort & Sanctuary)", "Meals Included: International Breakfast & Fine Dining Tuscan Gastronomy Dinner"]),
            _day(5, "Tuscany to Lake Como via Riva Yacht Charter", "Private executive transfer to Lake Como. Board custom mahogany-hulled Riva speedboat past Villa d'Este and Villa del Balbianello to lakeside palace resort.", ["Sightseeing Included: Private transfer, private mahogany Riva yacht charter cruise", "Overnight Stay: Lake Como (Ultra-Luxury Waterfront Palace Resort)", "Meals Included: International Breakfast & Lakeside Al Fresco Gourmet Dinner"]),
            _day(6, "Lake Como Seclusion & Bellagio Charm", "Morning at resort spa and floating pool. Private water craft to Bellagio. Villa Melzi botanical gardens with private guide.", ["Sightseeing Included: Villa Melzi botanical private pass, private water taxi to Bellagio", "Overnight Stay: Lake Como (Ultra-Luxury Waterfront Palace Resort)", "Meals Included: International Breakfast & Fine Dining Lakefront Dinner"]),
            _day(7, "High-Speed Rail to Venice & Grand Canal Apex", "High-speed executive train to Venice. Private water taxi to grand canal palazzo. Vintage wooden vessel sunset cruise. Grand farewell candlelight dinner on private terrace.", ["Sightseeing Included: High-speed executive rail, private water taxi, vintage vessel sunset cruise", "Evening Experience: Grand farewell candlelight dinner facing Grand Canal", "Overnight Stay: Venice Island (Grand Luxury Canal-view Palace Hotel)", "Meals Included: International Breakfast & Grand Farewell Venetian Dinner"]),
            _day(8, "High-End Resort Farewell & Departure", "Luxurious breakfast on private terrace. Personal butler handles checkout. Private water taxi to Venice Marco Polo VIP terminal.", ["Transfers Included: Private water taxi to airport VIP terminal, luggage coordination", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Hotel Grand Palatino / similar", location="Rome", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="Hotel Adler Cavalieri / similar", location="Tuscany", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="Grand Hotel Tremezzo / similar", location="Lake Como", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=5, sort_order=3),
            ItineraryHotelNested(name="Hotel Carlton Grand Canal / similar", location="Venice", nights_label="01 Night", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=4),
            ItineraryHotelNested(name="Starhotels Metropole", location="Rome", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="Borgo San Luigi Chianti", location="Tuscany", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="Villa d'Este Lake Como", location="Lake Como", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="Splendid Venice Starhotels", location="Venice", nights_label="01 Night", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=8),
            ItineraryHotelNested(name="Anantara Palazzo Naiadi", location="Rome", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=9),
            ItineraryHotelNested(name="Castello di Velona Resort", location="Tuscany", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=10),
            ItineraryHotelNested(name="Mandarin Oriental Como", location="Lake Como", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=11),
            ItineraryHotelNested(name="The Gritti Palace Venice", location="Venice", nights_label="01 Night", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=12),
            ItineraryHotelNested(name="Hotel de Russie", location="Rome", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=13),
            ItineraryHotelNested(name="Rosewood Castiglion del Bosco", location="Tuscany", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=14),
            ItineraryHotelNested(name="Il Sereno / Villa d'Este Palace", location="Lake Como", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=15),
            ItineraryHotelNested(name="Aman Venice / St. Regis Grand", location="Venice", nights_label="01 Night", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=16),
        ],
        inclusions=_it003_inclusions(),
    )
    return package, itinerary


def _it003_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="07 Nights in world-renowned ultra-luxury palaces, wine resorts, and lake-view suites", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private after-hours Vatican Museums access and Colosseum Gladiator's Gate entries", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Private helicopter flight from Rome to Tuscan estate", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Private mahogany Riva yacht day on Lake Como and vintage vessel cruise in Venice", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Full ground transits in private high-end vehicles and executive first-class trains", sort_order=5),
        ItineraryInclusionNested(kind="included", text="TRAGUIN dedicated 24/7 personal butler coordination and destination experts", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="International flight tickets and Schengen visa processing fees", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, room service, dry cleaning, and mini-bar billing", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Optional tours or individual gourmet dinners not specified in the itinerary", sort_order=9),
    ]


IT_BUILDERS = [
    build_it_001,
    build_it_002,
    build_it_003,
]
