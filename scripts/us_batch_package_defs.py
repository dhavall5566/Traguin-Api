"""Builder functions for US-001, US-002, and US-004 USA packages (no images)."""

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


def _us_excluded() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="excluded", text="International and internal domestic airfares unless stated", sort_order=100),
        ItineraryInclusionNested(kind="excluded", text="Optional tours, Broadway show entries, and specialized evening activities", sort_order=101),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, telephone calls, and boutique purchases", sort_order=102),
        ItineraryInclusionNested(kind="excluded", text="Optional helicopter rides or private boat charters", sort_order=103),
        ItineraryInclusionNested(kind="excluded", text="Comprehensive international travel and health insurance", sort_order=104),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and newly introduced government surcharges", sort_order=105),
    ]


def build_us_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="us-001-east-coast-usa-family-tour",
        destination_id=destination_id,
        title="East Coast USA Family Tour",
        duration_label="08 Nights / 09 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=79,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="New York (4N) → Washington D.C. (2N) → Niagara Falls (2N) premium circuit", sort_order=1),
            PackageHighlightNested(text="Statue of Liberty, Empire State Building & Summit One Vanderbilt", sort_order=2),
            PackageHighlightNested(text="Philadelphia heritage, Capitol Hill & Smithsonian museums", sort_order=3),
            PackageHighlightNested(text="Maid of the Mist & Cave of the Winds at Niagara Falls", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRAGUIN-US-001-PREMIUM | Serial US-001", sort_order=6),
        ],
        moods=["Family", "Luxury", "Cultural", "Adventure", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="us-001-east-coast-usa-itinerary",
        destination_id=destination_id,
        title="East Coast USA Family Tour",
        duration_label="08 Nights / 09 Days",
        duration_days=9,
        starting_price=0,
        price_note="On Request (Bespoke Luxury Tier)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="New York • Philadelphia • Washington D.C. • Niagara Falls",
        overview=(
            "Discover the iconic landmarks of America on this ultimate luxury East Coast holiday curated by TRAGUIN. "
            "From the sky-high towers of Manhattan and historic sites of Philadelphia to the political nerve centers "
            "of Washington D.C. and the majestic waters of Niagara Falls — with VIP skip-the-line access and "
            "private executive transfers throughout."
        ),
        seo_title="US-001 | East Coast USA Family Tour | TRAGUIN",
        seo_description=(
            "Premium 08 Nights / 09 Days USA East Coast family package (US-001): New York City, Philadelphia, "
            "Washington D.C., and Niagara Falls with VIP sightseeing."
        ),
        is_featured=True,
        featured_sort_order=79,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Statue of Liberty & Empire State Building", sort_order=1),
            ItineraryHighlightNested(text="Summit One Vanderbilt & Central Park", sort_order=2),
            ItineraryHighlightNested(text="White House, Lincoln Memorial & Smithsonian", sort_order=3),
            ItineraryHighlightNested(text="Maid of the Mist & Cave of the Winds", sort_order=4),
        ],
        days=[
            _day(1, "Arrive in New York City", "Welcome to the energy capital of the world. Upon arrival at JFK or Newark, a TRAGUIN private chauffeur escorts you to your premium Manhattan hotel. Evening orientation walk through Times Square and a wonderful family dinner nearby.", ["Sightseeing Included: Manhattan airport arrival transfer, Times Square evening orientation walk", "Overnight Stay: Handpicked Premium Hotel, Manhattan (New York City)", "Meals Included: Welcome Drinks"]),
            _day(2, "Statue of Liberty & Empire State Building", "Priority ferry to Liberty Island and Ellis Island. Drive past Wall Street, 9/11 Memorial, and SoHo. Ascend the Empire State Building 86th-floor observatory at dusk for breathtaking city views.", ["Sightseeing Included: Statue of Liberty & Ellis Island Ferry, Wall Street, Charging Bull, 9/11 Memorial, Empire State Building 86th Floor Observatory", "Photography Points: Liberty Island shoreline, Empire State sky-views, DUMBO Brooklyn Bridge frame", "Overnight Stay: Handpicked Premium Hotel, Manhattan (New York City)", "Meals Included: Premium Breakfast"]),
            _day(3, "Summit One Vanderbilt & Central Park", "Experience Summit One Vanderbilt's multi-sensory viewpoints. Afternoon stroll through Central Park, Bow Bridge, and Bethesda Fountain. Fifth Avenue premium window shopping and optional Broadway show.", ["Sightseeing Included: Summit One Vanderbilt Entry, Central Park Walking Tour, Fifth Avenue Premium Window Shopping", "Optional Activities: Evening Broadway Premium Theater Show reservation", "Overnight Stay: Handpicked Premium Hotel, Manhattan (New York City)", "Meals Included: Premium Breakfast"]),
            _day(4, "Philadelphia Heritage to Washington D.C.", "Private drive south with stops at the Liberty Bell, Independence Hall, and the Rocky Steps. Continue to Washington D.C. and enjoy an evening walk along the Georgetown waterfront.", ["Sightseeing Included: Philadelphia Historic District, Liberty Bell Center, Independence Hall, Washington D.C. overland transfer", "Overnight Stay: Handpicked Premium Hotel, Washington D.C.", "Meals Included: Premium Breakfast"]),
            _day(5, "Washington D.C. City Tour", "Photo stops at the White House, US Capitol, and Supreme Court. Visit the Lincoln Memorial, World War II Memorial, and Vietnam Veterans Memorial. Afternoon at the Smithsonian Institution.", ["Sightseeing Included: White House & Capitol Exterior Stops, Lincoln Memorial, Washington Monument, Smithsonian Museum Exploration", "Photography Points: Capitol Hill Reflecting Pool, The White House gates, Lincoln Memorial stairs", "Overnight Stay: Handpicked Premium Hotel, Washington D.C.", "Meals Included: Premium Breakfast"]),
            _day(6, "Washington D.C. to Niagara Falls", "Transfer to Buffalo International Airport or enjoy a scenic overland drive. Check into your premium fallsview hotel and witness the illuminated falls in the evening.", ["Sightseeing Included: Airport transfers, Niagara Falls State Park evening illumination stroll", "Evening Experience: Fine dining overlooking Horseshoe Falls", "Overnight Stay: Premium Fallsview Hotel, Niagara Falls (USA Side)", "Meals Included: Premium Breakfast"]),
            _day(7, "Maid of the Mist & Cave of the Winds", "Board the Maid of the Mist to the base of Horseshoe Falls. Experience the Cave of the Winds walkway near Bridal Veil Falls. Afternoon boutique shopping or fashion outlets visit.", ["Sightseeing Included: Maid of the Mist Boat Cruise, Cave of the Winds Gorge Walk, Goat Island Overlooks", "Exclusive Experiences: VIP front-deck boat cruise access, panoramic fallsview family lunch reservation", "Overnight Stay: Premium Fallsview Hotel, Niagara Falls (USA Side)", "Meals Included: Premium Breakfast"]),
            _day(8, "Buffalo to New York City — Farewell Dinner", "Morning views of the mist rising off the falls. Flight back to New York City for your final evening. Farewell dinner at an upscale rooftop lounge overlooking the Manhattan skyline.", ["Sightseeing Included: Inter-city return transfers, evening skyline farewell dinner reservation", "Overnight Stay: Handpicked Premium Hotel, Manhattan (New York City)", "Meals Included: Premium Breakfast"]),
            _day(9, "Departure", "Final premium breakfast before your private chauffeur transfer to the international airport, concluding your East Coast USA holiday.", ["Sightseeing Included: Private Luxury Airport Chauffeur Transfer", "Meals Included: Premium Breakfast"]),
        ],
        hotels=_us001_hotels(),
        inclusions=_us001_inclusions(),
    )
    return package, itinerary


def _us001_hotels() -> list[ItineraryHotelNested]:
    return [
        ItineraryHotelNested(name="The Westin New York Times Square", location="New York City", nights_label="04 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
        ItineraryHotelNested(name="Omni Shoreham Hotel", location="Washington D.C.", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
        ItineraryHotelNested(name="Sheraton Niagara Falls", location="Niagara Falls", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=3),
        ItineraryHotelNested(name="InterContinental New York Barclay", location="New York City", nights_label="04 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=4),
        ItineraryHotelNested(name="The Mayflower Hotel, Autograph Collection", location="Washington D.C.", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=5),
        ItineraryHotelNested(name="DoubleTree by Hilton Niagara Falls", location="Niagara Falls", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=4, sort_order=6),
        ItineraryHotelNested(name="JW Marriott Essex House New York", location="New York City", nights_label="04 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
        ItineraryHotelNested(name="Sofitel Washington DC Lafayette Square", location="Washington D.C.", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=8),
        ItineraryHotelNested(name="Seneca Niagara Resort & Casino", location="Niagara Falls", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=9),
        ItineraryHotelNested(name="The Plaza New York / The Ritz-Carlton", location="New York City", nights_label="04 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=10),
        ItineraryHotelNested(name="The St. Regis Washington D.C.", location="Washington D.C.", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=11),
        ItineraryHotelNested(name="The Giacomo, Luxury Boutique Hotel", location="Niagara Falls", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=12),
    ]


def _us001_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="08 Nights in premium handpicked hotels across New York City, Washington D.C., and Niagara Falls", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private executive air-conditioned chauffeur-driven luxury vehicle throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Daily premium American / Continental breakfast at hotels", sort_order=3),
        ItineraryInclusionNested(kind="included", text="VIP skip-the-line entry: Empire State Building, Statue of Liberty ferry, Summit One Vanderbilt, Maid of the Mist", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Philadelphia heritage, Washington D.C. monuments, and Smithsonian museum access", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Signature welcome drinks and personalized TRAGUIN travel kit", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated executive destination manager support", sort_order=7),
        *_us_excluded(),
    ]


def build_us_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="us-002-west-coast-usa-family-tour",
        destination_id=destination_id,
        title="West Coast USA Family Tour",
        duration_label="08 Nights / 09 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=80,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Los Angeles (2N) → Las Vegas (3N) → Grand Canyon (1N) → San Francisco (2N)", sort_order=1),
            PackageHighlightNested(text="Hollywood Walk of Fame & premium studio tour", sort_order=2),
            PackageHighlightNested(text="Las Vegas Strip, Bellagio fountains & world-class entertainment", sort_order=3),
            PackageHighlightNested(text="Grand Canyon breathtaking landscapes & Golden Gate Bridge", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Serial US-002 | West Coast USA Family Tour", sort_order=6),
        ],
        moods=["Family", "Luxury", "Adventure", "Cultural", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="us-002-west-coast-usa-itinerary",
        destination_id=destination_id,
        title="West Coast USA Family Tour",
        duration_label="08 Nights / 09 Days",
        duration_days=9,
        starting_price=0,
        price_note="On Request (Premium West Coast Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Los Angeles • Las Vegas • Grand Canyon • San Francisco",
        overview=(
            "Embark on an unforgettable journey across the iconic West Coast of the USA. From the dazzling lights "
            "of Los Angeles to the breathtaking landscapes of the Grand Canyon and the charm of San Francisco, "
            "TRAGUIN ensures a premium family holiday blending adventure, culture, and luxury."
        ),
        seo_title="US-002 | West Coast USA Family Tour | TRAGUIN",
        seo_description=(
            "Premium 08 Nights / 09 Days USA West Coast family package (US-002): Los Angeles, Las Vegas, "
            "Grand Canyon, and San Francisco."
        ),
        is_featured=True,
        featured_sort_order=80,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Santa Monica Pier & Hollywood Glamour", sort_order=1),
            ItineraryHighlightNested(text="Las Vegas Strip & Bellagio Fountains", sort_order=2),
            ItineraryHighlightNested(text="Grand Canyon Adventure", sort_order=3),
            ItineraryHighlightNested(text="Golden Gate Bridge & Fisherman's Wharf", sort_order=4),
        ],
        days=[
            _day(1, "Los Angeles — Arrival & Relaxation", "Arrival in the City of Angels. Private transfer to your luxury hotel. Evening stroll at Santa Monica Pier for a scenic sunset.", ["Sightseeing Included: Private airport transfer, Santa Monica Pier sunset stroll", "Overnight Stay: Los Angeles (Premium Family Hotel)", "Meals Included: Welcome arrangements on arrival"]),
            _day(2, "Los Angeles — Hollywood Glamour", "Discover iconic attractions including the Hollywood Walk of Fame and a premium studio tour.", ["Sightseeing Included: Hollywood Walk of Fame, premium studio tour", "Overnight Stay: Los Angeles (Premium Family Hotel)", "Meals Included: Premium Breakfast"]),
            _day(3, "Los Angeles to Las Vegas", "Scenic drive to the world's entertainment capital, Las Vegas. Evening exploration of the famous Strip.", ["Sightseeing Included: Scenic private drive to Las Vegas, Strip evening exploration", "Overnight Stay: Las Vegas (Premium Resort)", "Meals Included: Premium Breakfast"]),
            _day(4, "Las Vegas — Spectacular Entertainment", "Experience exclusive shows and premium shopping. Evening fountain show at Bellagio.", ["Sightseeing Included: Premium shopping, Bellagio fountain show", "Overnight Stay: Las Vegas (Premium Resort)", "Meals Included: Premium Breakfast"]),
            _day(5, "Las Vegas — Grand Canyon Adventure", "Witness the breathtaking landscapes of the Grand Canyon — a truly iconic attraction that defines American beauty.", ["Sightseeing Included: Grand Canyon scenic visit and overlooks", "Overnight Stay: Grand Canyon (Premium Lodge)", "Meals Included: Premium Breakfast"]),
            _day(6, "Grand Canyon to Las Vegas", "Relaxing morning with stunning views, returning to Las Vegas for more leisure.", ["Sightseeing Included: Grand Canyon morning views, return drive to Las Vegas", "Overnight Stay: Las Vegas (Premium Resort)", "Meals Included: Premium Breakfast"]),
            _day(7, "Las Vegas to San Francisco", "Flight to San Francisco. Transfer to hotel and evening visit to Fisherman's Wharf.", ["Sightseeing Included: Domestic flight to San Francisco, Fisherman's Wharf evening visit", "Overnight Stay: San Francisco (Premium Family Hotel)", "Meals Included: Premium Breakfast"]),
            _day(8, "San Francisco — Cultural Exploration", "Explore the Golden Gate Bridge and experience the city's unique culture and charm.", ["Sightseeing Included: Golden Gate Bridge visit, San Francisco cultural exploration", "Overnight Stay: San Francisco (Premium Family Hotel)", "Meals Included: Premium Breakfast"]),
            _day(9, "Departure", "Private transfer to the airport for your flight back home, carrying unforgettable memories.", ["Sightseeing Included: Private airport transfer", "Meals Included: Premium Breakfast"]),
        ],
        hotels=_us002_hotels(),
        inclusions=_us002_inclusions(),
    )
    return package, itinerary


def _us002_hotels() -> list[ItineraryHotelNested]:
    return [
        ItineraryHotelNested(name="Selected 4-star properties / similar", location="Los Angeles", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
        ItineraryHotelNested(name="Selected 4-star properties / similar", location="Las Vegas", nights_label="03 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
        ItineraryHotelNested(name="Selected 4-star properties / similar", location="Grand Canyon", nights_label="01 Night", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=3),
        ItineraryHotelNested(name="Selected 4-star properties / similar", location="San Francisco", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=4),
        ItineraryHotelNested(name="Upscale Boutique Hotels / similar", location="Los Angeles", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=4, sort_order=5),
        ItineraryHotelNested(name="Upscale Boutique Hotels / similar", location="Las Vegas", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=4, sort_order=6),
        ItineraryHotelNested(name="Upscale Boutique Hotels / similar", location="Grand Canyon", nights_label="01 Night", category_label="Premium", meal_plan="Breakfast", stars=4, sort_order=7),
        ItineraryHotelNested(name="Upscale Boutique Hotels / similar", location="San Francisco", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=4, sort_order=8),
        ItineraryHotelNested(name="Iconic 5-star Resorts / similar", location="Los Angeles", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=9),
        ItineraryHotelNested(name="Iconic 5-star Resorts / similar", location="Las Vegas", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=10),
        ItineraryHotelNested(name="Iconic 5-star Resorts / similar", location="Grand Canyon", nights_label="01 Night", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=11),
        ItineraryHotelNested(name="Iconic 5-star Resorts / similar", location="San Francisco", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=12),
    ]


def _us002_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="08 Nights in handpicked premium family hotels across Los Angeles, Las Vegas, Grand Canyon, and San Francisco", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private luxury ground transfers throughout the itinerary", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Daily premium breakfast at hotels", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Hollywood Walk of Fame, studio tour, Grand Canyon, and Golden Gate Bridge sightseeing", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Domestic flight Las Vegas to San Francisco", sort_order=5),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated on-ground family concierge support", sort_order=6),
        *_us_excluded(),
    ]


def build_us_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="us-004-luxury-usa-experience",
        destination_id=destination_id,
        title="Luxury USA Experience",
        duration_label="10 Nights / 11 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=81,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="New York (3N) → Las Vegas (3N) → San Francisco (4N) ultra-luxury circuit", sort_order=1),
            PackageHighlightNested(text="Private guided NYC tours — Statue of Liberty, MoMA & VIP Broadway", sort_order=2),
            PackageHighlightNested(text="Strip-front Las Vegas luxury & exclusive Grand Canyon helicopter", sort_order=3),
            PackageHighlightNested(text="Private yacht Golden Gate tour & Napa Valley vineyard visits", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 luxury travel concierge support", sort_order=5),
            PackageHighlightNested(text="Serial US-004 | Ultimate Luxury USA Experience", sort_order=6),
        ],
        moods=["Luxury", "Family", "Cultural", "Adventure", "Nature", "Romantic"],
    )
    itinerary = ItineraryCreate(
        slug="us-004-luxury-usa-itinerary",
        destination_id=destination_id,
        title="Luxury USA Experience",
        duration_label="10 Nights / 11 Days",
        duration_days=11,
        starting_price=0,
        price_note="On Request (Ultra-Luxury USA Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="New York • Las Vegas • Grand Canyon • San Francisco • Napa Valley",
        overview=(
            "Experience the epitome of opulence with a TRAGUIN curated journey across the United States. "
            "From the bustling energy of Manhattan to the neon lights of Las Vegas and the scenic beauty of "
            "San Francisco, this luxury USA holiday offers unforgettable memories with premium handpicked hotels "
            "and private luxury transportation."
        ),
        seo_title="US-004 | Luxury USA Experience | TRAGUIN",
        seo_description=(
            "Ultra-luxury 10 Nights / 11 Days USA package (US-004): New York City, Las Vegas, Grand Canyon "
            "helicopter, San Francisco yacht tour, and Napa Valley."
        ),
        is_featured=True,
        featured_sort_order=81,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="VIP Manhattan Sanctuary & Skyline Dining", sort_order=1),
            ItineraryHighlightNested(text="Statue of Liberty, MoMA & VIP Broadway Access", sort_order=2),
            ItineraryHighlightNested(text="Grand Canyon Helicopter Signature Experience", sort_order=3),
            ItineraryHighlightNested(text="Private Yacht & Napa Valley Vineyards", sort_order=4),
        ],
        days=[
            _day(1, "New York City — Arrival", "Private chauffeur welcome at JFK. Check into a five-star Manhattan sanctuary. Evening dining experience overlooking the skyline.", ["Sightseeing Included: VIP chauffeur airport welcome, private hotel transfer", "Evening Experience: Skyline dining experience", "Overnight Stay: New York City (Ultra-Luxury Hotel)", "Meals Included: Welcome Dinner"]),
            _day(2, "New York City — Iconic Attractions", "Private guided tours of the Statue of Liberty and MoMA. VIP access to a Broadway show — immersive experiences across the Big Apple.", ["Sightseeing Included: Private Statue of Liberty tour, MoMA visit, VIP Broadway access", "Overnight Stay: New York City (Ultra-Luxury Hotel)", "Meals Included: Premium Breakfast"]),
            _day(3, "New York City — Cultural Immersion", "Continue exploring Manhattan's iconic attractions with private guiding. Premium shopping and curated dining in the world's greatest city.", ["Sightseeing Included: Private guided Manhattan cultural tour", "Overnight Stay: New York City (Ultra-Luxury Hotel)", "Meals Included: Premium Breakfast"]),
            _day(4, "Las Vegas — Desert Luxury Arrival", "First-class flight to Las Vegas. Check into a Strip-front luxury resort. Explore world-class dining and exclusive nightlife.", ["Sightseeing Included: First-class flight to Las Vegas, private resort transfer", "Overnight Stay: Las Vegas (Strip-Front Ultra-Luxury Resort)", "Meals Included: Premium Breakfast"]),
            _day(5, "Las Vegas — Premium Leisure", "A day of exclusive leisure on the Strip — premium shopping, world-class dining, and curated entertainment experiences.", ["Sightseeing Included: Premium Strip leisure and dining experiences", "Overnight Stay: Las Vegas (Strip-Front Ultra-Luxury Resort)", "Meals Included: Premium Breakfast"]),
            _day(6, "Grand Canyon — Breathtaking Landscapes", "Exclusive helicopter tour over the Grand Canyon. Witness breathtaking landscapes from the sky — a true TRAGUIN Signature Experience.", ["Sightseeing Included: Exclusive Grand Canyon helicopter tour", "Overnight Stay: Las Vegas (Strip-Front Ultra-Luxury Resort)", "Meals Included: Premium Breakfast"]),
            _day(7, "San Francisco — Scenic Arrival", "Arrival in the Bay Area. Private transfer to your luxury hotel. Evening orientation along the waterfront.", ["Sightseeing Included: Flight to San Francisco, private hotel transfer", "Overnight Stay: San Francisco (Ultra-Luxury Hotel)", "Meals Included: Premium Breakfast"]),
            _day(8, "San Francisco — Yacht & Napa Valley", "Private yacht tour of the Golden Gate Bridge. Intimate visits to Napa Valley's finest vineyards.", ["Sightseeing Included: Private yacht Golden Gate tour, Napa Valley vineyard visits", "Overnight Stay: San Francisco (Ultra-Luxury Hotel)", "Meals Included: Premium Breakfast"]),
            _day(9, "San Francisco — Cultural Delights", "Explore local markets, historic neighborhoods, and high-end shopping on Union Square.", ["Sightseeing Included: Union Square shopping, historic neighborhood tour", "Overnight Stay: San Francisco (Ultra-Luxury Hotel)", "Meals Included: Premium Breakfast"]),
            _day(10, "San Francisco — Pacific Leisure", "Relax in a handpicked luxury hotel overlooking the Pacific. Final evening celebration of your American journey.", ["Evening Experience: Farewell luxury dining", "Overnight Stay: San Francisco (Ultra-Luxury Hotel)", "Meals Included: Premium Breakfast & Farewell Dinner"]),
            _day(11, "Departure", "Private transfer to SFO for your journey home, leaving with memories curated by TRAGUIN.", ["Sightseeing Included: Private airport transfer", "Meals Included: Premium Breakfast"]),
        ],
        hotels=_us004_hotels(),
        inclusions=_us004_inclusions(),
    )
    return package, itinerary


def _us004_hotels() -> list[ItineraryHotelNested]:
    return [
        ItineraryHotelNested(name="Four Seasons / Ritz-Carlton / Waldorf Astoria", location="New York City", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=1),
        ItineraryHotelNested(name="Four Seasons / Ritz-Carlton / Waldorf Astoria", location="Las Vegas", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=2),
        ItineraryHotelNested(name="Four Seasons / Ritz-Carlton / Waldorf Astoria", location="San Francisco", nights_label="04 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=3),
        ItineraryHotelNested(name="The St. Regis New York", location="New York City", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=4),
        ItineraryHotelNested(name="Wynn Las Vegas (Tower Suites)", location="Las Vegas", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=5),
        ItineraryHotelNested(name="Fairmont San Francisco (Presidential Suites)", location="San Francisco", nights_label="04 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=6),
    ]


def _us004_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="10 Nights in ultra-luxury hotels across New York City, Las Vegas, and San Francisco", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private chauffeur-driven VIP airport and ground transfers", sort_order=2),
        ItineraryInclusionNested(kind="included", text="First-class / premium domestic flights between cities", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Private guided Statue of Liberty, MoMA, and VIP Broadway access in New York", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Exclusive Grand Canyon helicopter tour — TRAGUIN Signature Experience", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Private yacht Golden Gate tour and Napa Valley vineyard visits", sort_order=6),
        ItineraryInclusionNested(kind="included", text="Welcome amenities and TRAGUIN 24/7 luxury concierge support", sort_order=7),
        *_us_excluded(),
    ]


US_BUILDERS = [
    build_us_001,
    build_us_002,
    build_us_004,
]
