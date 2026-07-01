"""Builder functions for RJ-001, RJ-002, RJ-005, RJ-007, and RJ-009 Rajasthan packages (no images)."""

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


def build_rj_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="rj-001-royal-heritage-luxury-expedition",
        destination_id=destination_id,
        title="Royal Heritage Luxury Expedition",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=10,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Jaipur (2N) → Jodhpur (1N) → Udaipur (2N) royal circuit", sort_order=1),
            PackageHighlightNested(text="Private premium luxury sedan / SUV with dedicated chauffeur", sort_order=2),
            PackageHighlightNested(text="MAPAI — royal breakfast and gourmet dinners", sort_order=3),
            PackageHighlightNested(text="Private Lake Pichola sunset boat cruise in Udaipur", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 personalized concierge on-ground support", sort_order=5),
            PackageHighlightNested(text="Tour code TRAGUIN-RJ-HERITAGE-2026 | Serial RJ-001", sort_order=6),
        ],
        moods=["Family", "Heritage", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug="rj-001-royal-heritage-itinerary",
        destination_id=destination_id,
        title="Royal Heritage Luxury Expedition",
        duration_label="05 Nights / 06 Days",
        duration_days=6,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Royal Heritage Luxury Expedition",
        overview=(
            "Embark on an extraordinary journey through time, royalty, and breathtaking landscapes with TRAGUIN's "
            "signature Best Rajasthan Tour Package. Designed for families demanding unrivaled comfort and deep cultural "
            "immersion, this bespoke itinerary unveils the majestic grandeur of India's most celebrated desert kingdom — "
            "from the pink-hued fortresses of Jaipur to the golden ramparts of Jodhpur and the shimmering romantic lakes "
            "of Udaipur. Handpicked premium stays, private chauffeur-driven luxury transportation, and curated local "
            "experiences ensure your family travels like royalty. Best season: October to March."
        ),
        seo_title="RJ-001 | Royal Heritage Luxury Rajasthan Tour | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days Rajasthan family tour (RJ-001): Jaipur, Jodhpur, Udaipur with Amber Fort, "
            "Mehrangarh Fort, Ranakpur Jain Temple, and private Lake Pichola cruise."
        ),
        is_featured=True,
        featured_sort_order=10,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Amber Fort & Sheesh Mahal", sort_order=1),
            ItineraryHighlightNested(text="Mehrangarh Fort & Jaswant Thada", sort_order=2),
            ItineraryHighlightNested(text="Ranakpur Jain Temple", sort_order=3),
            ItineraryHighlightNested(text="Lake Pichola Private Cruise", sort_order=4),
            ItineraryHighlightNested(text="Patrika Gate & City Palace Jaipur", sort_order=5),
        ],
        days=[
            _day(
                1,
                "Jaipur Arrival | Welcome to the Pink City",
                "Your luxury vacation begins with a traditional Rajasthani welcome in Jaipur. Transfer to your ultra-luxury "
                "handpicked resort, visit the vibrant Patrika Gate for family photography, and enjoy an exquisite welcome "
                "dinner with live folk music.",
                [
                    "Sightseeing Included: Patrika Gate, Albert Hall Museum (drive-by illumination)",
                    "Evening Experience: Traditional welcome dinner with live folk music at the resort",
                    "Overnight Stay: Jaipur (Premium Luxury Heritage Hotel)",
                    "Meals Included: Dinner",
                ],
            ),
            _day(
                2,
                "Jaipur Sightseeing | Fortresses, Palaces & Bazaars",
                "Ascend to Amber Fort with a private storyteller, explore City Palace Jaipur, Jantar Mantar, and Hawa Mahal. "
                "Conclude with a curated luxury shopping stroll through Johari Bazaar.",
                [
                    "Sightseeing Included: Amber Fort, Hawa Mahal, City Palace, Jantar Mantar, Jal Mahal",
                    "Optional Activities: Elephant-themed sustainable interaction or royal high tea at a palace cafe",
                    "Evening Experience: Heritage market stroll with private local assistant",
                    "Overnight Stay: Jaipur (Premium Luxury Heritage Hotel)",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                3,
                "Jaipur to Jodhpur | Sunset at Mehrangarh Fort",
                "Glide toward Jodhpur and explore the clifftop Mehrangarh Fort, Jaswant Thada, and Toorji Ka Jhalra stepwell. "
                "Watch the sun dip over the Blue City from a gourmet rooftop dinner.",
                [
                    "Sightseeing Included: Mehrangarh Fort, Jaswant Thada, Toorji Ka Jhalra (Stepwell)",
                    "Evening Experience: Gourmet rooftop dinner overlooking the illuminated fortress",
                    "Overnight Stay: Jodhpur (Premium Palace Hotel)",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                4,
                "Jodhpur to Udaipur via Ranakpur | Venice of the East",
                "Stop at the masterfully engineered Ranakpur Jain Temple with 1,444 uniquely carved marble pillars. "
                "Arrive in Udaipur and enjoy a private lakeside candlelight dinner.",
                [
                    "Sightseeing Included: Ranakpur Jain Marble Temple complex",
                    "Optional Activities: Traditional spa treatment at the premium resort",
                    "Evening Experience: Private lakeside walk and lakeside candlelight dinner",
                    "Overnight Stay: Udaipur (Ultra-Luxury Lakefront Resort)",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                5,
                "Udaipur Sightseeing | Lakeside Splendor & Sunset Cruise",
                "Tour City Palace Udaipur, Jagdish Temple, and Saheliyon-ki-Bari. Experience an exclusive private boat cruise "
                "on Lake Pichola past Lake Palace and Jag Mandir at golden hour.",
                [
                    "Sightseeing Included: City Palace Udaipur, Saheliyon-ki-Bari, Lake Pichola Cruise, Jagdish Temple",
                    "Evening Experience: Dharohar Folk Dance at Bagore Ki Haveli or luxury lakeview lounge dining",
                    "Overnight Stay: Udaipur (Ultra-Luxury Lakefront Resort)",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                6,
                "Udaipur Departure | Cherishing Unforgettable Memories",
                "Savor breakfast overlooking Lake Pichola, collect local souvenirs, and transfer to Udaipur Airport or Railway Station.",
                [
                    "Sightseeing Included: Departure airport drop / local market transit assistance",
                    "Meals Included: Breakfast",
                ],
            ),
        ],
        hotels=[
            ItineraryHotelNested(name="ITC Rajputana / Shiv Vilas", location="Jaipur", nights_label="02 Nights", category_label="Deluxe", room_type="Executive Room", meal_plan="MAPAI", stars=4, sort_order=1),
            ItineraryHotelNested(name="The Lalit Jaipur / Fairmont", location="Jaipur", nights_label="02 Nights", category_label="Premium", room_type="Luxury Room", meal_plan="MAPAI", stars=5, sort_order=2),
            ItineraryHotelNested(name="Taj Jai Mahal Palace", location="Jaipur", nights_label="02 Nights", category_label="Luxury", room_type="Luxury Heritage Room", meal_plan="MAPAI", stars=5, sort_order=3),
            ItineraryHotelNested(name="Taj Rambagh Palace", location="Jaipur", nights_label="02 Nights", category_label="Ultra Luxury", room_type="Palace Suite", meal_plan="MAPAI", stars=5, sort_order=4),
            ItineraryHotelNested(name="Welcomhotel Jodhpur", location="Jodhpur", nights_label="01 Night", category_label="Deluxe", room_type="Deluxe Room", meal_plan="MAPAI", stars=4, sort_order=5),
            ItineraryHotelNested(name="Radisson Jodhpur", location="Jodhpur", nights_label="01 Night", category_label="Premium", room_type="Premium Room", meal_plan="MAPAI", stars=4, sort_order=6),
            ItineraryHotelNested(name="Ajit Bhawan Palace", location="Jodhpur", nights_label="01 Night", category_label="Luxury", room_type="Executive Suite", meal_plan="MAPAI", stars=5, sort_order=7),
            ItineraryHotelNested(name="Taj Umaid Bhawan Palace", location="Jodhpur", nights_label="01 Night", category_label="Ultra Luxury", room_type="Historical Suite", meal_plan="MAPAI", stars=5, sort_order=8),
            ItineraryHotelNested(name="Radisson Blu Palace", location="Udaipur", nights_label="02 Nights", category_label="Deluxe", room_type="Superior Room", meal_plan="MAPAI", stars=4, sort_order=9),
            ItineraryHotelNested(name="The Ananta Resort", location="Udaipur", nights_label="02 Nights", category_label="Premium", room_type="Luxury Villa", meal_plan="MAPAI", stars=5, sort_order=10),
            ItineraryHotelNested(name="Taj Lake Palace / The Oberoi Udaivilas", location="Udaipur", nights_label="02 Nights", category_label="Luxury", room_type="Premier Valley View", meal_plan="MAPAI", stars=5, sort_order=11),
            ItineraryHotelNested(name="The Leela Palace Udaipur", location="Udaipur", nights_label="02 Nights", category_label="Ultra Luxury", room_type="Grand Lake View Suite", meal_plan="MAPAI", stars=5, sort_order=12),
        ],
        inclusions=_rj001_inclusions(),
    )
    return package, itinerary


def _rj001_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="05 Nights stay at handpicked elite luxury properties", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Daily multi-cuisine buffet breakfast and gourmet dinners (MAPAI)", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Dedicated air-conditioned premium vehicle for all transits", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Private sunset boat cruise on Lake Pichola, Udaipur", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Royal traditional welcomes, mocktails, and fresh fruit platters", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Fuel, parking, interstate driver allowances, and state taxes", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 personalized concierge on-ground assistance", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Airfare or train tickets to Jaipur / from Udaipur", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Monument entrance tickets and professional camera fees", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, alcoholic beverages, room mini-bar", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Optional activities or safari rides not specified in the itinerary", sort_order=11),
        ItineraryInclusionNested(kind="excluded", text="Mandatory festive gala dinners (Christmas/New Year Eve) if applicable", sort_order=12),
        ItineraryInclusionNested(kind="excluded", text="Travel insurance and tips/gratuities for guides and drivers", sort_order=13),
    ]


def build_rj_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="rj-002-royal-rajasthan-family-tour",
        destination_id=destination_id,
        title="Royal Rajasthan Family Tour",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=11,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Jaipur (2N) → Jodhpur (1N) → Jaisalmer (2N) → Udaipur (2N)", sort_order=1),
            PackageHighlightNested(text="Premium luxury chauffeur-driven AC SUV throughout", sort_order=2),
            PackageHighlightNested(text="Private camel safari and VVIP desert camp at Sam Sand Dunes", sort_order=3),
            PackageHighlightNested(text="Exclusive Lake Pichola boat cruise in Udaipur", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 priority concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRAGUIN-RJ-002-LUX | Serial RJ-002", sort_order=6),
        ],
        moods=["Family", "Heritage", "Luxury", "Adventure"],
    )
    itinerary = ItineraryCreate(
        slug="rj-002-royal-rajasthan-itinerary",
        destination_id=destination_id,
        title="Royal Rajasthan Family Tour",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="Premium Custom Pricing on Request",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Jaipur • Jodhpur • Jaisalmer • Udaipur",
        overview=(
            "Experience the ultimate Royal Rajasthan Family Tour across India's most celebrated land of kings, fortresses, "
            "and timeless heritage. From the pink-hued corridors of Jaipur to the golden sand dunes of Jaisalmer, every "
            "detail is woven with premium stays, immersive experiences, and handpicked luxury comforts. Route: "
            "Jaipur (2N) → Jodhpur (1N) → Jaisalmer (2N) → Udaipur (2N). Best season: October to March."
        ),
        seo_title="RJ-002 | Royal Rajasthan Family Tour | TRAGUIN",
        seo_description=(
            "Luxury 07 Nights / 08 Days Rajasthan family package (RJ-002) covering Jaipur, Jodhpur, Jaisalmer desert safari, "
            "and Udaipur with handpicked heritage hotels."
        ),
        is_featured=True,
        featured_sort_order=11,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Jaisalmer Living Fort", sort_order=1),
            ItineraryHighlightNested(text="Sam Sand Dunes Desert Safari", sort_order=2),
            ItineraryHighlightNested(text="Mehrangarh Fort", sort_order=3),
            ItineraryHighlightNested(text="Amber Fort & Hawa Mahal", sort_order=4),
            ItineraryHighlightNested(text="Lake Pichola Private Cruise", sort_order=5),
        ],
        days=[
            _day(1, "Jaipur Arrival | Pink City Royal Welcome", "Traditional welcome at your heritage hotel. Visit Birla Mandir and Albert Hall Museum at twilight.", ["Sightseeing Included: Albert Hall Museum, Birla Temple, Traditional Local Markets", "Evening Experience: Johari Bazaar stroll and authentic Rajasthani welcome dinner", "Overnight Stay: Premium Luxury Hotel, Jaipur | Meals: Dinner"]),
            _day(2, "Jaipur | Fortresses of Grandeur", "Comprehensive Jaipur sightseeing: Amber Fort, Hawa Mahal, City Palace, and Jantar Mantar.", ["Sightseeing Included: Amber Fort, Hawa Mahal, City Palace, Jantar Mantar, Jal Mahal", "Optional Activities: Hot air balloon ride over Amber Fort at sunrise", "Overnight Stay: Premium Luxury Hotel, Jaipur | Meals: Breakfast & Dinner"]),
            _day(3, "Jaipur to Jodhpur | Blue City & Mehrangarh", "Scenic drive to Jodhpur. Explore Mehrangarh Fort and Jaswant Thada with panoramic tea service.", ["Sightseeing Included: Mehrangarh Fort, Jaswant Thada, Clock Tower Market", "Evening Experience: Panoramic tea service from a boutique terrace cafe", "Overnight Stay: Handpicked Luxury Heritage Hotel, Jodhpur | Meals: Breakfast & Dinner"]),
            _day(4, "Jodhpur to Jaisalmer | Into the Thar Desert", "Travel to the Golden City. Explore Gadisar Lake at twilight and vibrant local markets.", ["Sightseeing Included: Scenic overland desert route, Gadisar Lake twilight views", "Food Suggestion: Ker Sangri and desert-inspired specialities", "Overnight Stay: Premium Luxury Oasis Resort, Jaisalmer | Meals: Breakfast & Dinner"]),
            _day(5, "Jaisalmer | Living Fort & Sam Sand Dunes Safari", "Explore Jaisalmer Fort, Patwon ki Haveli, and exclusive camel safari with folk performances at Sam Sand Dunes.", ["Sightseeing Included: Jaisalmer Living Fort, Patwon ki Haveli, Sam Sand Dunes", "Curated Experience: VVIP desert camp with live cultural fire dance and stargazing", "Overnight Stay: Luxury Desert Camp / Resort, Sam Dunes | Meals: Breakfast & Royal Desert Dinner"]),
            _day(6, "Jaisalmer to Udaipur | City of Lakes", "Scenic drive across the Aravalli range to Udaipur. Relaxed evening at Lake Pichola.", ["Sightseeing Included: Scenic drive across the Aravalli range, evening at Lake Pichola", "Evening Experience: Lakeside luxury high tea with views of Jag Mandir palace", "Overnight Stay: Ultra-Luxury Lakeside Resort, Udaipur | Meals: Breakfast & Dinner"]),
            _day(7, "Udaipur | City Palace & Private Boat Cruise", "Tour City Palace, Saheliyon-ki-Bari, Jagdish Temple, and private Lake Pichola sunset cruise.", ["Sightseeing Included: Udaipur City Palace, Saheliyon-ki-Bari, Jagdish Temple", "Photography Points: Ambrai Ghat and City Palace balconies", "Overnight Stay: Ultra-Luxury Lakeside Resort, Udaipur | Meals: Breakfast & Grand Finale Dinner"]),
            _day(8, "Udaipur Departure | Farewell to the Land of Royalty", "Leisurely breakfast, souvenir shopping, and transfer to Udaipur Airport or Railway Station.", ["Activities Included: Morning souvenir shopping, scheduled luxury airport/station transfer", "Meals Included: Gourmet Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="The Fern Residency", location="Jaipur", nights_label="02 Nights", category_label="Deluxe", room_type="Executive Room", stars=4, sort_order=1),
            ItineraryHotelNested(name="ITC Rajputana", location="Jaipur", nights_label="02 Nights", category_label="Premium", room_type="Executive Club", stars=5, sort_order=2),
            ItineraryHotelNested(name="Taj Jai Mahal Palace", location="Jaipur", nights_label="02 Nights", category_label="Luxury", room_type="Luxury Room", stars=5, sort_order=3),
            ItineraryHotelNested(name="Taj Rambagh Palace", location="Jaipur", nights_label="02 Nights", category_label="Ultra Luxury", room_type="Palace Room", stars=5, sort_order=4),
            ItineraryHotelNested(name="Fern Residency", location="Jodhpur", nights_label="01 Night", category_label="Deluxe", room_type="Comfort Room", stars=4, sort_order=5),
            ItineraryHotelNested(name="Radisson Blu", location="Jodhpur", nights_label="01 Night", category_label="Premium", room_type="Superior Room", stars=4, sort_order=6),
            ItineraryHotelNested(name="Taj Hari Mahal", location="Jodhpur", nights_label="01 Night", category_label="Luxury", room_type="Deluxe Garden Room", stars=5, sort_order=7),
            ItineraryHotelNested(name="Umaid Bhawan Palace", location="Jodhpur", nights_label="01 Night", category_label="Ultra Luxury", room_type="Palace Room", stars=5, sort_order=8),
            ItineraryHotelNested(name="Desert Tulip Resort / Desert Camp", location="Jaisalmer", nights_label="02 Nights", category_label="Deluxe", room_type="Deluxe Tent", stars=4, sort_order=9),
            ItineraryHotelNested(name="Jaisalkot Resort", location="Jaisalmer", nights_label="02 Nights", category_label="Premium", room_type="Luxury Pavilion", stars=5, sort_order=10),
            ItineraryHotelNested(name="Suryagarh Jaisalmer", location="Jaisalmer", nights_label="02 Nights", category_label="Luxury", room_type="Fort Room", stars=5, sort_order=11),
            ItineraryHotelNested(name="The Serai - SUJÁN", location="Jaisalmer", nights_label="02 Nights", category_label="Ultra Luxury", room_type="Luxury Tented Suite", stars=5, sort_order=12),
            ItineraryHotelNested(name="Hotel Lakend", location="Udaipur", nights_label="02 Nights", category_label="Deluxe", room_type="Lake View Room", stars=4, sort_order=13),
            ItineraryHotelNested(name="Radisson Blu Palace", location="Udaipur", nights_label="02 Nights", category_label="Premium", room_type="Palace Room", stars=5, sort_order=14),
            ItineraryHotelNested(name="The Leela Palace Udaipur", location="Udaipur", nights_label="02 Nights", category_label="Luxury", room_type="Grand Heritage View", stars=5, sort_order=15),
            ItineraryHotelNested(name="Taj Lake Palace", location="Udaipur", nights_label="02 Nights", category_label="Ultra Luxury", room_type="Luxury Lake View", stars=5, sort_order=16),
        ],
        inclusions=_rj002_inclusions(),
    )
    return package, itinerary


def _rj002_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="07 Nights premium accommodation in handpicked heritage hotels", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Daily gourmet buffet breakfast and curated royal multi-cuisine dinners", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Private transfers and sightseeing via luxury AC SUV with professional chauffeur", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Traditional welcome rituals and complimentary welcome amenities upon arrival", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Private camel safari, cultural folk programs, and gala desert dinner", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Exclusive boat cruise experiences on Lake Pichola in Udaipur", sort_order=6),
        ItineraryInclusionNested(kind="included", text="24/7 dedicated TRAGUIN priority concierge support throughout the tour", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Domestic or international airfares / train tickets to destination", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Monument entrance tickets and camera fees during sightseeing", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses such as laundry, mini-bar, telephone calls, and tips", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Optional adventure sports, hot air ballooning, or vintage car rides", sort_order=11),
        ItineraryInclusionNested(kind="excluded", text="Travel insurance policies or medical expenses", sort_order=12),
    ]


def build_rj_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="rj-005-palace-honeymoon-udaipur-jodhpur",
        destination_id=destination_id,
        title="Premium Rajasthan Palace Honeymoon",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=12,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Udaipur (3N) → Jodhpur (2N) romantic palace circuit", sort_order=1),
            PackageHighlightNested(text="Chauffeur-driven luxury sedan with CP breakfast plan", sort_order=2),
            PackageHighlightNested(text="Complimentary private Lake Pichola boat cruise", sort_order=3),
            PackageHighlightNested(text="Welcome honeymoon amenities — cake and floral decor", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRAGUIN-RJ-005 | Serial RJ-005", sort_order=6),
        ],
        moods=["Romantic", "Luxury", "Heritage"],
    )
    itinerary = ItineraryCreate(
        slug="rj-005-palace-honeymoon-itinerary",
        destination_id=destination_id,
        title="Premium Rajasthan Palace Honeymoon",
        duration_label="05 Nights / 06 Days",
        duration_days=6,
        starting_price=0,
        price_note="On Request (Premium Custom)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Udaipur • Jodhpur — 05 Nights / 06 Days of Royal Romance",
        overview=(
            "The Best Rajasthan Tour Package beckons lovers into an immersive realm of heritage hospitality, timeless "
            "romance, and majestic architectural marvels. This meticulously planned Rajasthan Honeymoon Package weaves "
            "together the ethereal lakes of Udaipur and the sun-kissed blue fortresses of Jodhpur. Private FIT tour with "
            "dedicated chauffeur-driven executive vehicle. Route: Udaipur Arrival → Udaipur Sightseeing → Ranakpur Enroute → "
            "Jodhpur Sightseeing → Jodhpur Departure. Best season: October to March."
        ),
        seo_title="RJ-005 | Premium Rajasthan Palace Honeymoon | TRAGUIN",
        seo_description=(
            "Luxury 05 Nights / 06 Days Rajasthan honeymoon (RJ-005): Udaipur and Jodhpur with Lake Pichola cruise, "
            "City Palace, Mehrangarh Fort, and Ranakpur Jain Temple."
        ),
        is_featured=True,
        featured_sort_order=12,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Lake Pichola Sunset Cruise", sort_order=1),
            ItineraryHighlightNested(text="City Palace Udaipur", sort_order=2),
            ItineraryHighlightNested(text="Sajjangarh Monsoon Palace", sort_order=3),
            ItineraryHighlightNested(text="Mehrangarh Fort", sort_order=4),
            ItineraryHighlightNested(text="Ranakpur Jain Temple", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Udaipur | Romantic Arrival & Sunset Boat Cruise", "Traditional royal welcome and private boat cruise on Lake Pichola at golden hour with views of Jag Mandir and City Palace.", ["Sightseeing Included: Lake Pichola Cruise, Jag Mandir Views, Local Romantic Promenades", "Optional Activities: Couples' traditional attire photoshoot", "Evening Experience: Lakeside candlelit fine-dining recommendation", "Overnight Stay: Udaipur (Handpicked Palace/Resort)"]),
            _day(2, "Udaipur Exploration | Royal Grandeur & Couturier Markets", "Tour City Palace, Jagdish Temple, Saheliyon-ki-Bari, and Vintage Car Museum. Evening miniature painting session and Hathipole Bazaar shopping.", ["Sightseeing Included: City Palace, Jagdish Temple, Saheliyon-ki-Bari, Vintage Car Museum", "Optional Activities: Cable car ride to Mansapurna Karni Mata Temple", "Evening Experience: Live folk dance at Bagore Ki Haveli", "Overnight Stay: Udaipur Palace Resort"]),
            _day(3, "Udaipur Excursion | Monsoon Palace & Lakeside Serenity", "Visit Sajjangarh Monsoon Palace for panoramic vistas. Peaceful afternoon at Fateh Sagar Lake and Nehru Park.", ["Sightseeing Included: Sajjangarh Monsoon Palace, Fateh Sagar Circuit, Nehru Park", "Optional Activities: Speedboating on Fateh Sagar Lake", "Evening Experience: Private sunset viewing from a mountain vantage point", "Overnight Stay: Udaipur Palace Resort"]),
            _day(4, "Udaipur to Jodhpur via Ranakpur | Sacred Architecture", "En-route visit to Ranakpur Jain Temple with 1,444 uniquely carved marble pillars. Arrive in Jodhpur and check into heritage palace hotel.", ["Sightseeing Included: Ranakpur Jain Temple, Scenic Aravali Highway Drive", "Optional Activities: Authentic Rajasthani Thali lunch en route", "Evening Experience: Leisure time at your luxury heritage property", "Overnight Stay: Jodhpur Luxury Palace"]),
            _day(5, "Jodhpur Sightseeing | Mehrangarh Fort & Royal Cenotaphs", "Explore Mehrangarh Fort, Jaswant Thada, Clock Tower, and Sadar Market. Optional zip-lining over fort moats.", ["Sightseeing Included: Mehrangarh Fort, Jaswant Thada, Clock Tower, Umaid Bhawan Museum", "Optional Activities: Zip-lining over the Mehrangarh Fort moats", "Evening Experience: Romantic rooftop dinner overlooking the illuminated fort", "Overnight Stay: Jodhpur Luxury Palace"]),
            _day(6, "Jodhpur Departure | Royal Farewell", "Final breakfast, optional souvenir shopping for local sweets and block-printed textiles, and transfer to Jodhpur Airport.", ["Sightseeing Included: Local markets, souvenir stops", "Meals Included: Premium Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="The Fern Residency", location="Udaipur", nights_label="03 Nights", category_label="Deluxe", room_type="Standard Room", meal_plan="CP (Breakfast)", stars=4, sort_order=1),
            ItineraryHotelNested(name="Radisson Blu Palace", location="Udaipur", nights_label="03 Nights", category_label="Premium", room_type="Superior Room", meal_plan="CP (Breakfast)", stars=5, sort_order=2),
            ItineraryHotelNested(name="The Leela Palace / Taj Lake Palace", location="Udaipur", nights_label="03 Nights", category_label="Luxury", room_type="Premier Room", meal_plan="CP (Breakfast)", stars=5, sort_order=3),
            ItineraryHotelNested(name="Oberoi Udaivilas", location="Udaipur", nights_label="03 Nights", category_label="Ultra Luxury", room_type="Luxury Suite", meal_plan="CP + Welcome Mix", stars=5, sort_order=4),
            ItineraryHotelNested(name="Fern Residency", location="Jodhpur", nights_label="02 Nights", category_label="Deluxe", room_type="Standard Room", meal_plan="CP (Breakfast)", stars=4, sort_order=5),
            ItineraryHotelNested(name="Welcomhotel by ITC", location="Jodhpur", nights_label="02 Nights", category_label="Premium", room_type="Executive Room", meal_plan="CP (Breakfast)", stars=5, sort_order=6),
            ItineraryHotelNested(name="Taj Hari Mahal", location="Jodhpur", nights_label="02 Nights", category_label="Luxury", room_type="Deluxe Room", meal_plan="CP (Breakfast)", stars=5, sort_order=7),
            ItineraryHotelNested(name="Umaid Bhawan Palace", location="Jodhpur", nights_label="02 Nights", category_label="Ultra Luxury", room_type="Palace Room", meal_plan="CP + Welcome Mix", stars=5, sort_order=8),
        ],
        inclusions=_rj005_inclusions(),
    )
    return package, itinerary


def _rj005_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="Luxury handpicked heritage palace/hotel accommodation", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Daily premium multi-cuisine buffet breakfasts (CP plan)", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Dedicated executive chauffeur-driven air-conditioned vehicle", sort_order=3),
        ItineraryInclusionNested(kind="included", text="All interstate taxes, tolls, parking, and driver allowances", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Complimentary private boat cruise on Lake Pichola", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Welcome honeymoon amenities (cake, floral decor arrangement)", sort_order=6),
        ItineraryInclusionNested(kind="included", text="24/7 dedicated TRAGUIN concierge support", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Domestic or international airfares/train bookings", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Monument entry tickets, camera fees, and local guide fees", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses (laundry, telephone calls, mini-bar)", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Optional activities (zip-lining, cable car, special dinners)", sort_order=11),
        ItineraryInclusionNested(kind="excluded", text="Mandatory festival or peak season gala dinner surcharges", sort_order=12),
        ItineraryInclusionNested(kind="excluded", text="Travel insurance coverage", sort_order=13),
    ]


def build_rj_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="rj-007-maharaja-rajasthan-luxury-tour",
        destination_id=destination_id,
        title="Maharaja Rajasthan Luxury Tour",
        duration_label="08 Nights / 09 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=13,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Jaipur (2N) → Jodhpur (2N) → Jaisalmer (1N) → Udaipur (3N) grand circuit", sort_order=1),
            PackageHighlightNested(text="Private executive luxury SUV with personal chauffeur", sort_order=2),
            PackageHighlightNested(text="Camel safari and luxury desert camp at Sam Sand Dunes", sort_order=3),
            PackageHighlightNested(text="Complimentary Lake Pichola sunset cruise", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 priority concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRAGUIN-RJ-007 | Serial RJ-007", sort_order=6),
        ],
        moods=["Luxury", "Family", "Heritage", "Adventure"],
    )
    itinerary = ItineraryCreate(
        slug="rj-007-maharaja-rajasthan-itinerary",
        destination_id=destination_id,
        title="Maharaja Rajasthan Luxury Tour",
        duration_label="08 Nights / 09 Days",
        duration_days=9,
        starting_price=0,
        price_note="On Request (Ultra Luxury bespoke)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Jaipur • Jodhpur • Jaisalmer • Udaipur — 08 Nights / 09 Days",
        overview=(
            "Embark on an epic voyage across a land defined by ancient forts, opulent heritage, and timeless grandeur. "
            "The Best Rajasthan Tour Package by TRAGUIN merges spectacular sights with majestic palaces across Jaipur, "
            "Jodhpur, Jaisalmer desert dunes, and Udaipur's romantic lakes. Elite FIT holiday with private executive "
            "luxury transport and TRAGUIN verified handpicked palace resorts. Meal plan: CP/MAPAI (breakfast and gourmet dinner). "
            "Best season: October to March."
        ),
        seo_title="RJ-007 | Maharaja Rajasthan Luxury Tour | TRAGUIN",
        seo_description=(
            "Ultra-luxury 08 Nights / 09 Days Rajasthan tour (RJ-007): Jaipur, Jodhpur, Jaisalmer desert camp, and Udaipur "
            "with Amber Fort, Mehrangarh Fort, and Lake Pichola cruise."
        ),
        is_featured=True,
        featured_sort_order=13,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Amber Fort Elephant Ride", sort_order=1),
            ItineraryHighlightNested(text="Sam Sand Dunes Camel Safari", sort_order=2),
            ItineraryHighlightNested(text="Jaisalmer Living Fort", sort_order=3),
            ItineraryHighlightNested(text="Mehrangarh Fort", sort_order=4),
            ItineraryHighlightNested(text="Lake Pichola Cruise", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Jaipur | Royal Greetings & Chokhi Dhani", "Traditional royal welcome and evening at Chokhi Dhani ethnic village with folk dances and Rajasthani feast.", ["Sightseeing Included: Royal Welcome, Chauffeured Hotel Transfer, Ethnic Cultural Village", "Meals Included: Traditional Gourmet Welcome Dinner", "Evening Experience: Cultural dance viewings and pottery workshops", "Overnight Stay: Jaipur (Handpicked Luxury Palace)"]),
            _day(2, "Jaipur Full Day Sightseeing | Amber Fort & Hawa Mahal", "Amber Fort with elephant or jeep ride, Sheesh Mahal, Hawa Mahal, City Palace, and Jantar Mantar.", ["Sightseeing Included: Amber Fort, Hawa Mahal, City Palace, Jantar Mantar", "Optional Activities: Hot air balloon ride over historic fortresses", "Evening Experience: Shopping for precious gems at Johari Bazaar", "Overnight Stay: Jaipur Luxury Palace"]),
            _day(3, "Jaipur to Jodhpur | Journey to the Sun City", "Premium intercity drive to Jodhpur with sunset views over the blue city horizons.", ["Sightseeing Included: Intercity scenic drive, blue city old quarter view", "Meals Included: Premium Buffet Breakfast", "Evening Experience: Relaxed evening walk inside old town streets", "Overnight Stay: Jodhpur (Premium Heritage Hotel)"]),
            _day(4, "Jodhpur Sightseeing | Mehrangarh Fort & Jaswant Thada", "Explore Mehrangarh Fort museums and Jaswant Thada white marble cenotaph. Optional zip-lining.", ["Sightseeing Included: Mehrangarh Fort, Jaswant Thada, Umaid Bhawan Palace Museum", "Optional Activities: Flying Fox zip-lining across fort battlements", "Evening Experience: Fine dining at a rooftop restaurant facing the fort", "Overnight Stay: Jodhpur Premium Hotel"]),
            _day(5, "Jodhpur to Jaisalmer | Camel Safari & Luxury Desert Camping", "Sunset camel safari at Sam Sand Dunes with ultra-luxury tented stay, folk music, and stargazing.", ["Sightseeing Included: Thar Desert dunes, Sunset Camel Trek", "Optional Activities: Dune-bashing in a private 4x4 vehicle", "Evening Experience: Live folk music performance and stargazing", "Overnight Stay: Luxury Tented Desert Camp"]),
            _day(6, "Jaisalmer Fort to Udaipur | Living Fortress & Regal Lakes", "Explore Jaisalmer Fort, Patwon-ki-Haveli, Salim Singh-ki-Haveli, and Gadisar Lake before transfer to Udaipur.", ["Sightseeing Included: Golden Jaisalmer Fort, Historic Havelis, Gadisar Lake", "Meals Included: Premium Breakfast", "Evening Experience: Relaxing late evening arrival check-in at Udaipur", "Overnight Stay: Udaipur (Premium Lakefront Resort)"]),
            _day(7, "Udaipur | City Palace & Lake Pichola Cruise", "City Palace complex tour and private scenic boat cruise to Jag Mandir Palace.", ["Sightseeing Included: City Palace, Lake Pichola Cruise, Jagdish Temple", "Optional Activities: Crystal Gallery private tour", "Evening Experience: Traditional dance show at Bagore-ki-Haveli", "Overnight Stay: Udaipur Lakefront Resort"]),
            _day(8, "Udaipur | Saheliyon-ki-Bari & Monsoon Palace", "Visit Saheliyon-ki-Bari gardens and Sajjangarh Monsoon Palace with panoramic lake views.", ["Sightseeing Included: Saheliyon-ki-Bari, Sajjangarh Monsoon Palace, Fateh Sagar Lake", "Optional Activities: Speedboating on Fateh Sagar Lake", "Evening Experience: Farewell lakeside gala dinner", "Overnight Stay: Udaipur Lakefront Resort"]),
            _day(9, "Udaipur Departure | Royal Farewell", "Final luxury breakfast, souvenir shopping, and transfer to Udaipur Airport.", ["Sightseeing Included: Airport departure transfer", "Meals Included: Premium Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="The Fern Residency", location="Jaipur", nights_label="02 Nights", category_label="Deluxe", sort_order=1),
            ItineraryHotelNested(name="Radisson Blu Palace", location="Jaipur", nights_label="02 Nights", category_label="Premium", sort_order=2),
            ItineraryHotelNested(name="ITC Rajputana", location="Jaipur", nights_label="02 Nights", category_label="Luxury", sort_order=3),
            ItineraryHotelNested(name="Rambagh Palace", location="Jaipur", nights_label="02 Nights", category_label="Ultra Luxury", sort_order=4),
            ItineraryHotelNested(name="Fern Residency", location="Jodhpur", nights_label="02 Nights", category_label="Deluxe", sort_order=5),
            ItineraryHotelNested(name="Welcomhotel by ITC", location="Jodhpur", nights_label="02 Nights", category_label="Premium", sort_order=6),
            ItineraryHotelNested(name="Taj Hari Mahal", location="Jodhpur", nights_label="02 Nights", category_label="Luxury", sort_order=7),
            ItineraryHotelNested(name="Umaid Bhawan Palace", location="Jodhpur", nights_label="02 Nights", category_label="Ultra Luxury", sort_order=8),
            ItineraryHotelNested(name="Desert Dune Tents", location="Jaisalmer", nights_label="01 Night", category_label="Deluxe", sort_order=9),
            ItineraryHotelNested(name="Luxury Desert Camp", location="Jaisalmer", nights_label="01 Night", category_label="Premium", sort_order=10),
            ItineraryHotelNested(name="Serai Oasis Camp", location="Jaisalmer", nights_label="01 Night", category_label="Luxury", sort_order=11),
            ItineraryHotelNested(name="The Serai", location="Jaisalmer", nights_label="01 Night", category_label="Ultra Luxury", sort_order=12),
            ItineraryHotelNested(name="The Fern Residency", location="Udaipur", nights_label="03 Nights", category_label="Deluxe", sort_order=13),
            ItineraryHotelNested(name="Radisson Blu Palace", location="Udaipur", nights_label="03 Nights", category_label="Premium", sort_order=14),
            ItineraryHotelNested(name="The Leela Palace", location="Udaipur", nights_label="03 Nights", category_label="Luxury", sort_order=15),
            ItineraryHotelNested(name="Taj Lake Palace / Udaivilas", location="Udaipur", nights_label="03 Nights", category_label="Ultra Luxury", sort_order=16),
        ],
        inclusions=_rj007_inclusions(),
    )
    return package, itinerary


def _rj007_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="Bespoke luxury stays at handpicked hotels and palace resorts", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Daily multi-cuisine buffet breakfasts and dinners as listed", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Private air-conditioned transport with an executive chauffeur", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Complimentary sunset cruise on Lake Pichola in Udaipur", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Traditional welcome amenities and personalized honeymoon treats", sort_order=5),
        ItineraryInclusionNested(kind="included", text="All parking fees, toll taxes, fuel costs, and driver allowances", sort_order=6),
        ItineraryInclusionNested(kind="included", text="24/7 priority concierge support from TRAGUIN", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Domestic or international airfares and train tickets", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Monument entry fees, camera permits, and local guide hire", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses (laundry, room service, telephone calls)", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Optional adventure activities like zip-lining or dune-bashing", sort_order=11),
        ItineraryInclusionNested(kind="excluded", text="Peak seasonal surcharges or mandatory gala dinner fees", sort_order=12),
        ItineraryInclusionNested(kind="excluded", text="Comprehensive travel insurance coverage", sort_order=13),
    ]


def build_rj_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="rj-009-premium-heritage-senior-circuit",
        destination_id=destination_id,
        title="Premium Heritage Rajasthan Senior Circuit",
        duration_label="06 Nights / 07 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=14,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Jaipur (2N) → Pushkar (1N) → Jodhpur (2N) → Udaipur (1N) comfort circuit", sort_order=1),
            PackageHighlightNested(text="Senior-friendly pacing with Innova Crysta MUV and step-stool boarding", sort_order=2),
            PackageHighlightNested(text="Elevator access at Mehrangarh Fort and golf-cart at City Palace", sort_order=3),
            PackageHighlightNested(text="CP plan with relaxed buffet breakfasts", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated concierge assistance", sort_order=5),
            PackageHighlightNested(text="Tour code TRAGUIN-RJ-009 | Serial RJ-009", sort_order=6),
        ],
        moods=["Family", "Heritage", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug="rj-009-premium-heritage-senior-itinerary",
        destination_id=destination_id,
        title="Premium Heritage Rajasthan Senior Circuit",
        duration_label="06 Nights / 07 Days",
        duration_days=7,
        starting_price=0,
        price_note="On Request (Premium Custom)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Jaipur • Pushkar • Jodhpur • Udaipur — 06 Nights / 07 Days Comfort Circuit",
        overview=(
            "Welcome to a timeless journey crafted with exceptional care, patience, and warmth. This exclusive "
            "Rajasthan Family Tour and senior-focused circuit balances gentle pacing with royal grandeur, seamlessly "
            "connecting majestic forts, peaceful lakes, and sacred landscapes. Features a dedicated smooth-riding luxury "
            "Innova Crysta with professional chauffeur, handpicked hotels with elevator access and minimal walking, "
            "and curated experiences designed for absolute comfort. Route: Jaipur → Pushkar → Jodhpur → Udaipur. "
            "Best season: October to March."
        ),
        seo_title="RJ-009 | Premium Heritage Rajasthan Senior Circuit | TRAGUIN",
        seo_description=(
            "Comfort-focused 06 Nights / 07 Days Rajasthan tour (RJ-009) for senior citizens: Jaipur, Pushkar, Jodhpur, "
            "Udaipur with accessible fort visits and private Lake Pichola cruise."
        ),
        is_featured=True,
        featured_sort_order=14,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Amer Fort (Vehicle Access)", sort_order=1),
            ItineraryHighlightNested(text="Pushkar Brahma Temple & Holy Lake", sort_order=2),
            ItineraryHighlightNested(text="Mehrangarh Fort with Elevator", sort_order=3),
            ItineraryHighlightNested(text="Ranakpur Jain Temple", sort_order=4),
            ItineraryHighlightNested(text="Lake Pichola Private Cruise", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Jaipur | Royal Greetings & Relaxed Evening", "Warm traditional greeting, comfortable transfer to premium hotel, and gentle drive past illuminated Albert Hall Museum with welcome dinner.", ["Sightseeing Included: Albert Hall illuminated drive, local heritage walks", "Optional Activities: Visit to the local handicraft emporium", "Evening Experience: Relaxed sit-down traditional dinner", "Overnight Stay: Jaipur (Handpicked Premium Hotel)"]),
            _day(2, "Jaipur Royal Exploration | Comfortable Fort Ascent", "Amer Fort with vehicle access to main courtyard, Hawa Mahal photo stop, and accessible golf-cart tour of City Palace.", ["Sightseeing Included: Amer Fort Courtyard, Hawa Mahal Photo Stop, City Palace via Golf-Cart", "Optional Activities: Private block-printing demonstration", "Evening Experience: Leisurely stroll through the accessible gardens of Kanak Vrindavan", "Overnight Stay: Jaipur"]),
            _day(3, "Jaipur to Pushkar | Holy Lake & Brahma Temple", "Short drive to Pushkar. Gentle walk to Pushkar Lake ghats and Brahma Temple. Evening prayer ceremonies by the lake.", ["Sightseeing Included: Brahma Temple, Pushkar Holy Lake Ghats, Rose Gardens", "Optional Activities: Relaxing traditional foot massage at the resort spa", "Evening Experience: Spiritually uplifting sunset chants by the lake", "Overnight Stay: Pushkar (Premium Heritage Resort)"]),
            _day(4, "Pushkar to Jodhpur | Sunset Fort Views", "Leisurely drive to Jodhpur with comfort stops. Evening terrace views of illuminated Mehrangarh Fort.", ["Sightseeing Included: Highway landscape viewing, palace grounds exploration", "Optional Activities: Tea tasting featuring classic Marwari blends", "Evening Experience: Private family dinner under the stars", "Overnight Stay: Jodhpur (Premium Palace Hotel)"]),
            _day(5, "Jodhpur Sightseeing | Mehrangarh with Elevator Access", "Mehrangarh Fort with exclusive lift access, Jaswant Thada gardens, and Umaid Bhawan vintage car museum.", ["Sightseeing Included: Mehrangarh Fort with Elevator, Jaswant Thada Gardens, Umaid Bhawan Car Collection", "Optional Activities: Soft handicraft shopping at Sadar bazaar with private pickup", "Evening Experience: Fine-dining dinner featuring signature Rajasthani delicacies", "Overnight Stay: Jodhpur"]),
            _day(6, "Jodhpur to Udaipur | Ranakpur & Sunset Lakeside Cruise", "En-route Ranakpur Jain Temple. Private boat cruise on Lake Pichola at sunset with Jag Mandir views.", ["Sightseeing Included: Ranakpur Temple, Lake Pichola Private Cruise, Jag Mandir Views", "Optional Activities: Photography session during sunset", "Evening Experience: Lakeside fine-dining dinner organized by your concierge", "Overnight Stay: Udaipur (Premium Lakeside Resort)"]),
            _day(7, "Udaipur Sightseeing & Departure | Royal Gardens & Farewell", "Visit Saheliyon-ki-Bari gardens, final lunch, and transfer to Udaipur Airport.", ["Sightseeing Included: Saheliyon-ki-Bari, local arts emporium", "Meals Included: Premium Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="The Fern Residency", location="Jaipur", nights_label="02 Nights", category_label="Deluxe", meal_plan="CP (Breakfast)", stars=4, sort_order=1),
            ItineraryHotelNested(name="Radisson Blu Palace", location="Jaipur", nights_label="02 Nights", category_label="Premium", meal_plan="CP (Breakfast)", stars=5, sort_order=2),
            ItineraryHotelNested(name="ITC Rajputana", location="Jaipur", nights_label="02 Nights", category_label="Luxury", meal_plan="CP (Breakfast)", stars=5, sort_order=3),
            ItineraryHotelNested(name="Rambagh Palace", location="Jaipur", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="CP (Breakfast)", stars=5, sort_order=4),
            ItineraryHotelNested(name="Pushkar Resort", location="Pushkar", nights_label="01 Night", category_label="Deluxe", meal_plan="CP (Breakfast)", stars=4, sort_order=5),
            ItineraryHotelNested(name="Bhanwar Singh Palace", location="Pushkar", nights_label="01 Night", category_label="Premium", meal_plan="CP (Breakfast)", stars=4, sort_order=6),
            ItineraryHotelNested(name="Ananta Spa & Resort", location="Pushkar", nights_label="01 Night", category_label="Luxury", meal_plan="CP (Breakfast)", stars=5, sort_order=7),
            ItineraryHotelNested(name="The Westin Pushkar", location="Pushkar", nights_label="01 Night", category_label="Ultra Luxury", meal_plan="CP (Breakfast)", stars=5, sort_order=8),
            ItineraryHotelNested(name="Fern Residency", location="Jodhpur", nights_label="02 Nights", category_label="Deluxe", meal_plan="CP (Breakfast)", stars=4, sort_order=9),
            ItineraryHotelNested(name="Welcomhotel by ITC", location="Jodhpur", nights_label="02 Nights", category_label="Premium", meal_plan="CP (Breakfast)", stars=5, sort_order=10),
            ItineraryHotelNested(name="Taj Hari Mahal", location="Jodhpur", nights_label="02 Nights", category_label="Luxury", meal_plan="CP (Breakfast)", stars=5, sort_order=11),
            ItineraryHotelNested(name="Umaid Bhawan Palace", location="Jodhpur", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="CP (Breakfast)", stars=5, sort_order=12),
            ItineraryHotelNested(name="The Fern Residency", location="Udaipur", nights_label="01 Night", category_label="Deluxe", meal_plan="CP (Breakfast)", stars=4, sort_order=13),
            ItineraryHotelNested(name="Radisson Blu Udaipur", location="Udaipur", nights_label="01 Night", category_label="Premium", meal_plan="CP (Breakfast)", stars=5, sort_order=14),
            ItineraryHotelNested(name="The Leela Palace", location="Udaipur", nights_label="01 Night", category_label="Luxury", meal_plan="CP (Breakfast)", stars=5, sort_order=15),
            ItineraryHotelNested(name="Oberoi Udaivilas", location="Udaipur", nights_label="01 Night", category_label="Ultra Luxury", meal_plan="CP (Breakfast)", stars=5, sort_order=16),
        ],
        inclusions=_rj009_inclusions(),
    )
    return package, itinerary


def _rj009_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="Comfort-driven premium hotel stays with accessible rooms", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Daily multi-cuisine buffet breakfasts with dietary preferences", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Dedicated executive chauffeur-driven Innova Crysta vehicle", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Exclusive elevator/lift access passes at Mehrangarh Fort", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Complimentary smooth private boat cruise on Lake Pichola", sort_order=5),
        ItineraryInclusionNested(kind="included", text="All road taxes, parking, toll fees, and driver allowances", sort_order=6),
        ItineraryInclusionNested(kind="included", text="24/7 dedicated TRAGUIN concierge assistance", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Domestic or international airfares/train bookings", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Monument entry fees, camera costs, and local guide gratuities", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Personal laundry, telephone bills, or mini-bar usage", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Optional activities such as village safaris or special spa sessions", sort_order=11),
        ItineraryInclusionNested(kind="excluded", text="Surcharges for peak festival dates or gala dinners", sort_order=12),
        ItineraryInclusionNested(kind="excluded", text="Personal travel and medical insurance", sort_order=13),
    ]


RJ_BUILDERS = [
    build_rj_001,
    build_rj_002,
    build_rj_005,
    build_rj_007,
    build_rj_009,
]
