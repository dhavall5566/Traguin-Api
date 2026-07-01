"""Builder functions for ZA-001 through ZA-003 South Africa packages (no images)."""

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


def _za_excluded() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="excluded", text="International and domestic internal flight tickets", sort_order=100),
        ItineraryInclusionNested(kind="excluded", text="South African tourist visa fees and processing charges", sort_order=101),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, premium liquors, telephone calls, and gratuities", sort_order=102),
        ItineraryInclusionNested(kind="excluded", text="Optional adventure activities like shark cage diving, bungee jumping, or skydiving", sort_order=103),
        ItineraryInclusionNested(kind="excluded", text="Comprehensive international travel and health insurance", sort_order=104),
    ]


def build_za_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="za-001-south-africa-family-tour",
        destination_id=destination_id,
        title="South Africa Family Tour",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=87,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Cape Town (4N) → Knysna Garden Route (2N) → Safari Lodge (1N)", sort_order=1),
            PackageHighlightNested(text="Table Mountain, Cape Peninsula & Boulders Beach penguins", sort_order=2),
            PackageHighlightNested(text="Stellenbosch Winelands & Knysna Lagoon catamaran cruise", sort_order=3),
            PackageHighlightNested(text="Cango Caves, Big Five sunset game drive & boma dinner", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRAGUIN-ZA-001-PREMIUM | Serial ZA-001", sort_order=6),
        ],
        moods=["Family", "Luxury", "Wildlife", "Adventure", "Nature", "Cultural"],
    )
    itinerary = ItineraryCreate(
        slug="za-001-south-africa-family-itinerary",
        destination_id=destination_id,
        title="South Africa Family Tour",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="On Request (Premium Curated Pricing)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Cape Town • Garden Route • Knysna • Luxury Safari",
        overview=(
            "The Best South Africa Tour Package by TRAGUIN unlocks untamed natural elegance, spectacular coastal "
            "highways, and thrilling big-game safaris. From Table Mountain to the Garden Route estuaries and a "
            "malaria-free private game reserve — with private executive transfers and handpicked premium hotels."
        ),
        seo_title="ZA-001 | South Africa Family Tour | TRAGUIN",
        seo_description=(
            "Premium 07 Nights / 08 Days South Africa family package (ZA-001): Cape Town, Garden Route, "
            "Knysna, and Shamwari luxury safari."
        ),
        is_featured=True,
        featured_sort_order=87,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Table Mountain & Cape Peninsula", sort_order=1),
            ItineraryHighlightNested(text="Stellenbosch Winelands & Knysna Lagoon", sort_order=2),
            ItineraryHighlightNested(text="Cango Caves & Ostrich Farm", sort_order=3),
            ItineraryHighlightNested(text="Big Five Sunset Safari & Boma Dinner", sort_order=4),
        ],
        days=[
            _day(1, "Cape Town — Arrival & Gourmet Waterfront Welcome", "VIP meet-and-greet at Cape Town International Airport. Transfer to your ultra-luxury harborfront hotel. Evening welcome dinner at a premium V&A Waterfront restaurant.", ["Sightseeing Included: Private airport pick-up, V&A Waterfront luxury exploration", "Evening Experience: Waterfront Fine Dining Welcome Experience", "Overnight Stay: Cape Town (Handpicked Premium Luxury Hotel)", "Meals Included: Welcome Dinner"]),
            _day(2, "Cape Town — Table Mountain & Historic City Sightseeing", "Skip-the-line Table Mountain Aerial Cableway. Explore Bo-Kaap, Company's Gardens, and Castle of Good Hope. Sunset family photography at Signal Hill.", ["Sightseeing Included: Table Mountain (Weather Permitting), Bo-Kaap, City Orientation Tour", "Evening Experience: High-end Cape Malay culinary dinner experience", "Overnight Stay: Cape Town", "Meals Included: Premium Breakfast & Dinner"]),
            _day(3, "Cape Town — Cape Peninsula & Boulders Beach Penguins", "Chapman's Peak Drive to Cape Point Nature Reserve and Flying Dutchman Funicular. Premium close-up African Penguin colony at Boulders Beach.", ["Sightseeing Included: Chapman's Peak Drive, Cape of Good Hope, Boulders Beach Penguins", "Optional Activities: Seal Island private boat cruise from Hout Bay", "Overnight Stay: Cape Town", "Meals Included: Premium Breakfast & Seafood Lunch"]),
            _day(4, "Cape Town — Stellenbosch Winelands & Chocolate Tasting", "Stellenbosch and Franschhoek Cape Dutch estates with wine-tasting for adults and artisanal chocolate workshops for children. Evening leisure at Camps Bay promenade.", ["Sightseeing Included: Stellenbosch historic walk, Premium Estate Tour", "Evening Experience: Relaxed evening leisure walk at Camps Bay promenade", "Overnight Stay: Cape Town", "Meals Included: Premium Breakfast & Estate Lunch"]),
            _day(5, "Knysna — Garden Route & Lagoon Catamaran Cruise", "Scenic private transfer down the Garden Route to Knysna. Premium luxury catamaran cruise across Knysna Lagoon to the Knysna Heads.", ["Sightseeing Included: Scenic Garden Route Highway Drive, Knysna Lagoon Catamaran Cruise", "Evening Experience: Oyster tasting and lagoon-side gourmet dining", "Overnight Stay: Knysna (Premium Waterfront Stay)", "Meals Included: Premium Breakfast & Dinner"]),
            _day(6, "Knysna — Cango Caves & Ostrich Farm Adventure", "Day trip to Oudtshoorn — Cango Caves guided tour and interactive premium ostrich farm experience.", ["Sightseeing Included: Cango Caves Guided Tour, Safari Ostrich Farm Experience", "Optional Activities: Guided meerkat safari at dawn", "Overnight Stay: Knysna", "Meals Included: Premium Breakfast & Braai (BBQ) Lunch"]),
            _day(7, "Private Game Reserve — Luxury Safari & Big Five Sunset Drive", "Transfer to malaria-free private game reserve. Afternoon Big Five game drive with professional ranger. Boma bonfire dinner under the stars.", ["Sightseeing Included: Afternoon Big 5 Game Drive, Luxury Safari High Tea", "Evening Experience: Boma bonfire dinner under the canopy of southern stars", "Overnight Stay: Shamwari / Eastern Cape Luxury Safari Lodge", "Meals Included: Premium Breakfast, Lunch, & Gourmet Boma Dinner"]),
            _day(8, "Gqeberha — Morning Safari & Departure", "Final dawn game drive. Hearty premium breakfast before private transfer to Gqeberha (Port Elizabeth) airport for onward connections.", ["Sightseeing Included: Sunrise Bush Safari Drive", "Transfers: Private Airport Chauffeur Drop", "Meals Included: Premium Breakfast"]),
        ],
        hotels=_za001_hotels(),
        inclusions=_za001_inclusions(),
    )
    return package, itinerary


def _za001_hotels() -> list[ItineraryHotelNested]:
    return [
        ItineraryHotelNested(name="The Westin Cape Town", location="Cape Town", nights_label="04 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=5, sort_order=1),
        ItineraryHotelNested(name="Knysna Hollow Country Estate", location="Knysna", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
        ItineraryHotelNested(name="Kariega Game Reserve - Main Lodge", location="Private Game Reserve", nights_label="01 Night", category_label="Deluxe", meal_plan="Full Board", stars=5, sort_order=3),
        ItineraryHotelNested(name="The Table Bay Hotel", location="Cape Town", nights_label="04 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=4),
        ItineraryHotelNested(name="Turbine Hotel & Spa", location="Knysna", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=5),
        ItineraryHotelNested(name="Amakhala Game Reserve - Woodbury Lodge", location="Private Game Reserve", nights_label="01 Night", category_label="Premium", meal_plan="Full Board", stars=5, sort_order=6),
        ItineraryHotelNested(name="The Silo Hotel / One&Only", location="Cape Town", nights_label="04 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
        ItineraryHotelNested(name="Simola Hotel Country Club & Spa", location="Knysna", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=8),
        ItineraryHotelNested(name="Shamwari Private Game Reserve - Long Lee Manor", location="Private Game Reserve", nights_label="01 Night", category_label="Luxury", meal_plan="Full Board", stars=5, sort_order=9),
        ItineraryHotelNested(name="Cape Grace Hotel (Marina Suite)", location="Cape Town", nights_label="04 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=10),
        ItineraryHotelNested(name="Pezula Nature Retreat (Villa Stay)", location="Knysna", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=11),
        ItineraryHotelNested(name="Shamwari - Eagles Crag Luxury Tented Lodges", location="Private Game Reserve", nights_label="01 Night", category_label="Ultra Luxury", meal_plan="Full Board", stars=5, sort_order=12),
    ]


def _za001_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="07 Nights in handpicked premium hotels and safari lodges across Cape Town, Knysna, and private game reserve", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private chauffeur-driven premium Mercedes van / luxury SUV transfers throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Daily gourmet breakfasts, select safari lunches, and curated multi-course dinners", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Two exclusive 4x4 open-top game drives with professional trackers", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Skip-the-line Table Mountain, Cape Point funicular, Boulders Beach, Knysna Lagoon cruise, and Cango Caves entry", sort_order=5),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated guest relations concierge assistance", sort_order=6),
        *_za_excluded(),
    ]


def build_za_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="za-002-south-africa-honeymoon",
        destination_id=destination_id,
        title="South Africa Honeymoon",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=88,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Cape Town (3N) → Franschhoek (1N) → Knysna (2N) → Safari Lodge (1N)", sort_order=1),
            PackageHighlightNested(text="Private yacht sunset cruise & helicopter flight over Cape Peninsula", sort_order=2),
            PackageHighlightNested(text="Franschhoek Wine Tram & ultra-luxury vineyard villa", sort_order=3),
            PackageHighlightNested(text="Knysna lagoon catamaran & couples' spa ritual", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 honeymoon concierge desk support", sort_order=5),
            PackageHighlightNested(text="Tour code TRAGUIN-ZA-002-HONEYMOON | Serial ZA-002", sort_order=6),
        ],
        moods=["Romantic", "Luxury", "Wildlife", "Adventure", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="za-002-south-africa-honeymoon-itinerary",
        destination_id=destination_id,
        title="South Africa Honeymoon",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="On Request (Strictly Bespoke Honeymoon Pricing)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Cape Town • Franschhoek • Garden Route • Ultra-Luxury Safari",
        overview=(
            "The South Africa Honeymoon Package by TRAGUIN delivers romance in its purest, most opulent form. "
            "From intimate sunset sailing in the shadow of Table Mountain to private plunge pools overlooking the "
            "African bush — with VIP honeymoon amenities and breathtaking landscapes tailored for couples."
        ),
        seo_title="ZA-002 | South Africa Honeymoon | TRAGUIN",
        seo_description=(
            "Premium 07 Nights / 08 Days South Africa honeymoon (ZA-002): Cape Town yacht cruise, helicopter "
            "flight, Franschhoek winelands, Knysna, and luxury safari."
        ),
        is_featured=True,
        featured_sort_order=88,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Private Yacht Champagne Sunset Cruise", sort_order=1),
            ItineraryHighlightNested(text="Helicopter Flight & VIP Table Mountain", sort_order=2),
            ItineraryHighlightNested(text="Franschhoek Wine Tram Journey", sort_order=3),
            ItineraryHighlightNested(text="Candlelit Boma Safari Dinner", sort_order=4),
        ],
        days=[
            _day(1, "Cape Town — Arrival & Romantic Sunset Cruise", "VIP greeting by private luxury chauffeur. Ultra-luxury waterfront sanctuary with champagne welcome. Private luxury yacht sunset cruise across Table Bay.", ["Sightseeing Included: Private executive airport transfer, Premium Waterfront check-in", "Evening Experience: Private Yacht Champagne Sunset Cruise", "Overnight Stay: Cape Town (Premium Luxury Ocean Suite)", "Meals Included: Welcome Honeymoon Dinner"]),
            _day(2, "Cape Town — Helicopter Flight & Table Mountain VIP", "Exclusive private helicopter flight over the Atlantic coastline. Skip-the-line Table Mountain cableway. Kirstenbosch Botanical Gardens canopy paths.", ["Sightseeing Included: Private Helicopter Coastal Flight, VIP Table Mountain Cableway, Kirstenbosch", "Evening Experience: Candlelight dining at award-winning oceanfront restaurant in Camps Bay", "Overnight Stay: Cape Town", "Meals Included: Premium Breakfast & Dinner"]),
            _day(3, "Cape Town — Cape Peninsula & Secluded Beach Picnic", "Chapman's Peak Drive to Cape Point. Exclusive gourmet seafood picnic on a secluded white-sand beach with private butler service.", ["Sightseeing Included: Chapman's Peak Drive, Cape Point, Cape of Good Hope, Boulders Beach Penguins", "Evening Experience: Casual luxury lounging at the V&A Waterfront", "Overnight Stay: Cape Town", "Meals Included: Premium Breakfast & Luxury Beach Picnic Lunch"]),
            _day(4, "Franschhoek — Wine Tram & Boutique Vineyard Stay", "Vintage Wine Tram through Franschhoek valley. Private cellar tours and fine-wine masterclasses. Ultra-luxury vineyard villa with private heated plunge pool.", ["Sightseeing Included: Franschhoek Valley, Premium Hop-on Hop-off Wine Tram Tour", "Evening Experience: Private estate dinner paired with exclusive museum-release wines", "Overnight Stay: Franschhoek (Ultra-Luxury Vineyard Villa)", "Meals Included: Premium Breakfast & Gourmet Vineyard Lunch"]),
            _day(5, "Knysna — Garden Route & Exclusive Lagoon Cruise", "Scenic Garden Route drive to Knysna. Exclusive luxury catamaran cruise through Knysna Heads as the sky turns pink.", ["Sightseeing Included: Garden Route Scenic Transit, Private Knysna Heads Catamaran Cruise", "Evening Experience: Oyster & Champagne tasting dinner on the water's edge", "Overnight Stay: Knysna (Premium Cliffside Luxury Suite)", "Meals Included: Premium Breakfast & Dinner"]),
            _day(6, "Knysna — Cango Caves & Private Spa Ritual", "Private Cango Caves guided tour. 90-minute side-by-side couple's massage and hydrotherapy ritual at your premium resort.", ["Sightseeing Included: Cango Caves Heritage Tour, Oudtshoorn Valley Drive", "Evening Experience: Relaxed, candlelit lagoon-side dinner", "Overnight Stay: Knysna", "Meals Included: Premium Breakfast & Dinner"]),
            _day(7, "Luxury Safari Lodge — Honeymoon Safari & Boma Bonfire", "Ultra-luxury private game reserve suite. Sunset Big Five game drive. Candlelit boma bonfire dinner under the Southern Cross.", ["Sightseeing Included: Sunset Big Five Safari Drive, Private Lodge High Tea", "Evening Experience: Candlelit Boma Fire Dinner under the Southern Cross constellation", "Overnight Stay: Eastern Cape Luxury Safari Lodge (Ultra-Luxury Suite)", "Meals Included: Premium Breakfast, Lunch, & Elite Safari Dinner"]),
            _day(8, "Gqeberha — Sunrise Safari & Departure", "Final sunrise safari drive. Decadent Champagne breakfast. Private transfer to Gqeberha (Port Elizabeth) International Airport.", ["Sightseeing Included: Dawn Wildlife Safari Tracking", "Transfers: Private Airport Executive Chauffeur Drop", "Meals Included: Premium Breakfast / Champagne Brunch"]),
        ],
        hotels=_za002_hotels(),
        inclusions=_za002_inclusions(),
    )
    return package, itinerary


def _za002_hotels() -> list[ItineraryHotelNested]:
    return [
        ItineraryHotelNested(name="The Westin Cape Town", location="Cape Town", nights_label="03 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=5, sort_order=1),
        ItineraryHotelNested(name="Le Franschhoek Hotel", location="Franschhoek", nights_label="01 Night", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
        ItineraryHotelNested(name="Knysna Hollow Estate", location="Knysna", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=3),
        ItineraryHotelNested(name="Kariega Game Reserve - Ukhozi Lounge", location="Luxury Safari Lodge", nights_label="01 Night", category_label="Deluxe", meal_plan="Full Board", stars=5, sort_order=4),
        ItineraryHotelNested(name="The Table Bay Hotel", location="Cape Town", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=5),
        ItineraryHotelNested(name="Franschhoek Country House", location="Franschhoek", nights_label="01 Night", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=6),
        ItineraryHotelNested(name="Turbine Hotel & Spa", location="Knysna", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=7),
        ItineraryHotelNested(name="Amakhala Bush Lodge", location="Luxury Safari Lodge", nights_label="01 Night", category_label="Premium", meal_plan="Full Board", stars=5, sort_order=8),
        ItineraryHotelNested(name="One&Only Cape Town", location="Cape Town", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=9),
        ItineraryHotelNested(name="Mont Rochelle (Virgin Limited)", location="Franschhoek", nights_label="01 Night", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=10),
        ItineraryHotelNested(name="Simola Country Club", location="Knysna", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=11),
        ItineraryHotelNested(name="Shamwari Private Reserve - Long Lee Manor", location="Luxury Safari Lodge", nights_label="01 Night", category_label="Luxury", meal_plan="Full Board", stars=5, sort_order=12),
        ItineraryHotelNested(name="The Silo Hotel (Penthouse)", location="Cape Town", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=13),
        ItineraryHotelNested(name="Leeu Estates (Studio Room)", location="Franschhoek", nights_label="01 Night", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=14),
        ItineraryHotelNested(name="Pezula Nature Retreat (Villa)", location="Knysna", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=15),
        ItineraryHotelNested(name="Shamwari - Eagles Crag Luxury Lodge", location="Luxury Safari Lodge", nights_label="01 Night", category_label="Ultra Luxury", meal_plan="Full Board", stars=5, sort_order=16),
    ]


def _za002_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="07 Nights in ultra-luxury honeymoon suites across Cape Town, Franschhoek, Knysna, and safari lodge", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Honeymoon privileges: premium champagne, welcome flowers, and private candlelight dining upgrades", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Dedicated private chauffeur service in luxury vehicles throughout", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Exclusive private helicopter flight over the Cape Peninsula", sort_order=4),
        ItineraryInclusionNested(kind="included", text="VIP Table Mountain, Wine Tram passes, private lagoon catamaran cruise, and two premium safari drives", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Complimentary 90-minute couples side-by-side spa therapy experience", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 priority honeymoon concierge support", sort_order=7),
        *_za_excluded(),
    ]


def build_za_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="za-003-cape-town-safari-family-tour",
        destination_id=destination_id,
        title="Cape Town Safari Family Tour",
        duration_label="08 Nights / 09 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=89,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Cape Town (5N) → Shamwari Private Game Reserve (3N) deep-dive circuit", sort_order=1),
            PackageHighlightNested(text="Table Mountain VIP, Cape Peninsula & marine wildlife cruise", sort_order=2),
            PackageHighlightNested(text="Robben Island history & Kirstenbosch canopy walk", sort_order=3),
            PackageHighlightNested(text="Six Big Five safaris, cheetah rehab centre & bush walk", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRAGUIN-ZA-003-FAMILY | Serial ZA-003", sort_order=6),
        ],
        moods=["Family", "Luxury", "Wildlife", "Adventure", "Nature", "Cultural"],
    )
    itinerary = ItineraryCreate(
        slug="za-003-cape-town-safari-itinerary",
        destination_id=destination_id,
        title="Cape Town Safari Family Tour",
        duration_label="08 Nights / 09 Days",
        duration_days=9,
        starting_price=0,
        price_note="On Request (Premium Multi-Day Curated Pricing)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Cape Town • Shamwari • Big Five Safari • Marine Wildlife",
        overview=(
            "An immersive family journey combining rich cosmopolitan relaxation with breathtaking wildlife experiences. "
            "Focus deeply on Cape Town's iconic landmarks and the premier malaria-free wilderness of the Eastern Cape — "
            "custom-designed for premium families balancing cultural exploration with multi-day Big Five safari adventure."
        ),
        seo_title="ZA-003 | Cape Town Safari Family Tour | TRAGUIN",
        seo_description=(
            "Premium 08 Nights / 09 Days South Africa family package (ZA-003): Cape Town deep dive and "
            "3-night Shamwari luxury safari with cheetah rehabilitation centre."
        ),
        is_featured=True,
        featured_sort_order=89,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Table Mountain VIP & Cape Peninsula", sort_order=1),
            ItineraryHighlightNested(text="Marine Wildlife Cruise & Robben Island", sort_order=2),
            ItineraryHighlightNested(text="Winelands Picnic & Kirstenbosch Canopy", sort_order=3),
            ItineraryHighlightNested(text="6 Safari Drives & Cheetah Rehab Centre", sort_order=4),
        ],
        days=[
            _day(1, "Cape Town — Arrival & Waterfront Exploration", "Warm greeting at Cape Town International Airport. Transfer to premium V&A Waterfront hotel. Two Oceans Aquarium and welcome harborfront dinner.", ["Sightseeing Included: Private executive airport transfer, V&A Waterfront family walk", "Evening Experience: Harborfront Premium Seafood Welcome Dinner", "Overnight Stay: Cape Town (Handpicked Premium Luxury Hotel)", "Meals Included: Welcome Dinner"]),
            _day(2, "Cape Town — Table Mountain VIP & Historic Culture", "Skip-the-line VIP Table Mountain cableway. Bo-Kaap, Company's Garden, and Signal Hill sunset viewing.", ["Sightseeing Included: Table Mountain VIP Cableway, Bo-Kaap Tour, Company's Garden, Signal Hill Sunset", "Evening Experience: Authentic Cape Malay fine-dining experience", "Overnight Stay: Cape Town", "Meals Included: Premium Breakfast & Dinner"]),
            _day(3, "Cape Town — Peninsula Safari & Boulders Beach Penguins", "Chapman's Peak Drive to Cape Point Funicular and Cape of Good Hope. Immersive African Penguin colony at Boulders Beach.", ["Sightseeing Included: Chapman's Peak Drive, Cape Point Funicular, Cape of Good Hope, Boulders Beach Penguins", "Optional Activities: High-speed private boat ride to Hout Bay Seal Island", "Overnight Stay: Cape Town", "Meals Included: Premium Breakfast & Gourmet Seafood Lunch"]),
            _day(4, "Cape Town — Marine Wildlife Cruise & Robben Island", "Premium catamaran marine safari around Table Bay. Guided historical tour of Robben Island led by a former political prisoner.", ["Sightseeing Included: Marine Wildlife Catamaran Cruise, Robben Island Guided Museum Tour", "Evening Experience: Relaxed family leisure at Camps Bay beach promenade", "Overnight Stay: Cape Town", "Meals Included: Premium Breakfast & Dinner"]),
            _day(5, "Cape Town — Winelands Picnic & Kirstenbosch Canopy Walk", "Constantia Valley historic estate tour and gourmet picnic. Boomslang canopy walkway at Kirstenbosch National Botanical Gardens.", ["Sightseeing Included: Constantia Historic Estate Tour, Constantia Gourmet Picnic, Kirstenbosch Canopy Walk", "Evening Experience: High-end contemporary dining at the waterfront", "Overnight Stay: Cape Town", "Meals Included: Premium Breakfast & Estate Picnic Lunch"]),
            _day(6, "Luxury Safari Lodge — Transit & Sunset Big Five Safari", "Fly Cape Town to Gqeberha (Port Elizabeth). Transfer to malaria-free private game reserve. Inaugural sunset Big Five game drive and boma dinner.", ["Sightseeing Included: Private Reserve Check-in, Sunset 4x4 Big Five Safari Tracking", "Evening Experience: Traditional multi-course gourmet Boma dinner around a roaring wood fire", "Overnight Stay: Eastern Cape Luxury Safari Lodge (Premium Family Suite)", "Meals Included: Premium Breakfast, High Tea, & Luxury Safari Dinner"]),
            _day(7, "Luxury Safari Lodge — Dawn Safari & Cheetah Rehabilitation", "Dawn safari with expert tracker. Behind-the-scenes VIP tour of wildlife rehabilitation centre. Evening stargazing and constellation storytelling.", ["Sightseeing Included: Sunrise Bush Safari, Wildlife Rehabilitation Center VIP Tour", "Evening Experience: Guided night-sky stargazing and constellation storytelling session", "Overnight Stay: Luxury Safari Lodge", "Meals Included: Premium Full Board (Breakfast, Lunch, High Tea, Dinner)"]),
            _day(8, "Luxury Safari Lodge — Bush Walk & Farewell Gala Dinner", "Guided bush walk with armed ranger. Final signature sunset safari with sundowner ridge experience. Private family farewell gala dinner in a secluded bush clearing.", ["Sightseeing Included: Dawn Safari Tracking, Guided Ranger Bush Walk, Sundowner Ridge Experience", "Evening Experience: Private Family Farewell Gala Dinner hosted inside a secluded bush clearing", "Overnight Stay: Luxury Safari Lodge", "Meals Included: Premium Full Board (Gourmet Breakfast, Bush Lunch, Farewell Dinner)"]),
            _day(9, "Gqeberha — Morning Safari & Departure", "Final sunrise safari drive. Celebratory luxury breakfast. Private transfer to Gqeberha airport for connecting flight home.", ["Sightseeing Included: Sunrise Safari Tracking Ritual", "Transfers: Private Airport Executive Coach Drop", "Meals Included: Premium Breakfast"]),
        ],
        hotels=_za003_hotels(),
        inclusions=_za003_inclusions(),
    )
    return package, itinerary


def _za003_hotels() -> list[ItineraryHotelNested]:
    return [
        ItineraryHotelNested(name="The Westin Cape Town (Family Interconnecting Rooms)", location="Cape Town", nights_label="05 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=5, sort_order=1),
        ItineraryHotelNested(name="Kariega Game Reserve - Main Lodge (Family Chalet)", location="Luxury Safari Lodge", nights_label="03 Nights", category_label="Deluxe", meal_plan="Full Board", stars=5, sort_order=2),
        ItineraryHotelNested(name="The Table Bay Hotel (Luxury Twin/Family Facing)", location="Cape Town", nights_label="05 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=3),
        ItineraryHotelNested(name="Amakhala Game Reserve - Woodbury Lodge", location="Luxury Safari Lodge", nights_label="03 Nights", category_label="Premium", meal_plan="Full Board", stars=5, sort_order=4),
        ItineraryHotelNested(name="One&Only Cape Town (Two-Bedroom Marina Suite)", location="Cape Town", nights_label="05 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=5),
        ItineraryHotelNested(name="Shamwari Private Game Reserve - Long Lee Manor", location="Luxury Safari Lodge", nights_label="03 Nights", category_label="Luxury", meal_plan="Full Board", stars=5, sort_order=6),
        ItineraryHotelNested(name="The Silo Hotel (Two-Bedroom Family Duplex Penthouse)", location="Cape Town", nights_label="05 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
        ItineraryHotelNested(name="Shamwari - Riverdene Family Luxury Lodge (Private Pool)", location="Luxury Safari Lodge", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Full Board", stars=5, sort_order=8),
    ]


def _za003_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="08 Nights: 5 in Cape Town and 3 in ultra-luxury malaria-free safari lodge", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Daily gourmet breakfasts and dinners in Cape Town; all-inclusive premium full board at safari lodge", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Dedicated private chauffeur-driven luxury family coach or premium SUV throughout", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Six exclusive 4x4 open safari game drives led by qualified senior rangers", sort_order=4),
        ItineraryInclusionNested(kind="included", text="VIP Table Mountain, Cape Point funicular, Boulders Beach, marine catamaran, and Robben Island tickets", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Wildlife Rehabilitation Centre behind-the-scenes tour and family bush clearing farewell dinner", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 priority family concierge support", sort_order=7),
        *_za_excluded(),
    ]


ZA_BUILDERS = [
    build_za_001,
    build_za_002,
    build_za_003,
]
