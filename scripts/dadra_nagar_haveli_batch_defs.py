"""Builder functions for DN-001 through DN-018 Dadra and Nagar Haveli packages."""

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

DADRA_NAGAR_HAVELI_SLUG = "dadra-and-nagar-haveli"


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




def build_dn_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DN-001"
    tour_code = "TRG-DN-001"
    title = "Silvassa Nature Tour"
    duration = "03 Nights / 04 Days"
    slug = "dn-001-silvassa-nature-tour"
    itin_slug = "dn-001-silvassa-nature-tour-itinerary"
    loc = "Silvassa (2 Nights) / Khanvel (1 Night)"
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
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Dadra and Nagar Haveli / India | Category: Premium Family Nature Tour", 2),
            _ph("Destinations: Silvassa • Khanvel • Dudhani Lake • Vasona", 3),
            _ph("Ideal for: Nature Enthusiasts, Relaxing Family Getaways & Eco-Luxury Seekers", 4),
            _ph("Best season: November to March (Lush Greenery post-monsoon)", 5),
            _ph("Starting price: On Request (Premium Customised Eco-Luxury)", 6),
            _ph("Vehicle / Meals: Private Luxury AC Vehicle / MAPAI Plan (Breakfast & Dinner)", 7),
            _ph(
                "Route Map: Vapi/Mumbai Arrival → Silvassa Heritage & Vanganga → Vasona Safari & Khanvel → "
                "Dudhani Lake → Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private family interaction and briefing detailing unique tribal culture "
                "and history of the region.",
                9,
            ),
            _ph(
                "Shopping & Local Experiences: Warli Art paintings, hand-crafted paper items, bamboo baskets; "
                "fresh river fish and resort barbecue spreads.",
                10,
            ),
            _ph(
                "Important Notes: Book resorts 30 days ahead for weekends; Vasona Lion Safari subject to forest "
                "department guidelines; valid government photo ID required at check-in.",
                11,
            ),
        ],
        moods=["Nature", "Family", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Customised Eco-Luxury)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Silvassa Nature Tour • Escape to Serenity",
        overview=(
            "Welcome to a hidden sanctuary of emerald forests, gentle rivers, and vintage Portuguese heritage, curated "
            "exclusively by TRAGUIN. Embark on the definitive Dadra and Nagar Haveli Family Tour, designed meticulously "
            "for sophisticated families who crave premium stays wrapped inside raw, breathtaking landscapes. As your "
            "bespoke travel planners, TRAGUIN transforms an ordinary weekend getaway into a grand luxury holiday "
            "punctuated by immersive experiences, scenic beauty, and refined hospitality.\n\n"
            "TOUR OVERVIEW\n"
            "This custom-sculpted itinerary promises an elegant escape from urban monotony into the refreshing lap of "
            "nature. Travelling in an exclusive premium AC sedan or SUV with dedicated professional chauffeur assistance, "
            "your family will traverse pristine forested roads in unparalleled comfort. Featuring handpicked hotels that "
            "balance rustic tribal charm with contemporary high-end luxury, our meal plan keeps you energized with "
            "opulent breakfasts and curated multi-cuisine dinners.\n\n"
            "WHY VISIT SILVASSA?\n"
            "When considering the Best Dadra and Nagar Haveli Tour Package, families and couples look for a harmonious "
            "combination of undisturbed wildlife, colonial nostalgia, and modern waterfront relaxation. Silvassa delivers "
            "magnificent attractions such as the Vasona Lion Safari and Vanganga Lake Garden—consistently rated among the "
            "top tourist places in Dadra and Nagar Haveli. Travelers will be enchanted by misty mornings at Dudhani Lake "
            "and the classic Portuguese design of Our Lady of Piety Church."
        ),
        seo_title="DN-001 | Silvassa Nature Tour Premium Family Package | TRAGUIN",
        seo_description=(
            "Premium 03 Nights / 04 Days Silvassa nature package (DN-001 / TRG-DN-001): Vanganga Lake Garden, "
            "Vasona Lion Safari, Dudhani Lake speed-boat, tribal museum, and 4-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Vanganga Lake Garden, Our Lady of Piety Church & Silvassa Tribal Museum on Day 01", 1),
            _ih("Vasona Lion Safari, Satmaliya Deer Park & Khanvel landscape drives on Day 02", 2),
            _ih("Dudhani Lake private speed-boat cruise & Madhuban Dam views on Day 03", 3),
            _ih("Heritage handicraft shopping & smooth departure transfer on Day 04", 4),
            _ih("TRAGUIN Signature Experience: Private family tribal culture and history briefing", 5),
            _ih("Curated by TRAGUIN Experts: Seamlessly coordinated itineraries minimizing travel fatigue", 6),
            _ih("Premium Handpicked Hotels: Properties selected for safety, food ratings, and peaceful environments", 7),
        ],
        days=[
            _day(
                1,
                "Arrival in Silvassa | Portuguese Nostalgia & Manicured Lakeside Gardens",
                (
                    "Your premium Dadra and Nagar Haveli experience begins with a private luxury pick-up from Vapi "
                    "Railway Station or Mumbai Airport. Enjoy a smooth, scenic drive into Silvassa, arriving at a "
                    "beautifully handpicked luxury resort surrounded by towering teak trees. After checking in and "
                    "enjoying your welcome amenities, step out to explore the Vanganga Lake Garden with Japanese-style "
                    "bridges, elegant fountains, and paddle-boating tracks amidst lush foliage. Follow this with a visit "
                    "to the historic Our Lady of Piety Church, a proud testament to Portuguese structural design."
                ),
                [
                    "Sightseeing Included: Vanganga Lake Garden, Our Lady of Piety Church, Silvassa Tribal Museum.",
                    "Evening Experience: Relaxing stroll through the tribal museum followed by a gourmet resort dinner.",
                    "Overnight Stay: Silvassa (Premium Luxury Nature Resort).",
                    "Meals Included: Welcome Drink & Luxury Dinner.",
                ],
            ),
            _day(
                2,
                "Silvassa to Vasona Safari & Khanvel | Wildlife Majesty & the Emerald Forest Hideaway",
                (
                    "Indulge in a lavish breakfast before entering the thrilling wilderness of the Vasona Lion Safari. "
                    "Board a specially secured park vehicle for a close-range view of majestic Asiatic lions roaming in "
                    "their natural deep forest habitat. Next, drive deeper into the territory towards Khanvel, a tranquil "
                    "valley flanked by breathtaking landscapes and rich biodiversity. Spend your afternoon visiting the "
                    "Deer Park at Satmaliya, observing beautiful blackbucks and chitals roaming freely near the waterholes."
                ),
                [
                    "Sightseeing Included: Vasona Lion Safari Park, Satmaliya Deer Park, Khanvel Landscape Drives.",
                    "Optional Activities: Personalized family photography session inside the green meadows of Khanvel.",
                    "Overnight Stay: Khanvel / Silvassa Luxury Forest Villa.",
                    "Meals Included: Premium Breakfast & Dinner.",
                ],
            ),
            _day(
                3,
                "Excursion to Dudhani Lake | The Kashmir of the West – Waterfront Luxury & Water Sports",
                (
                    "Today promises absolute scenic beauty as we venture to Dudhani Lake, a massive stunning waterfront "
                    "formed by the impounded waters of the Madhuban Dam. Fondly called the 'Kashmir of the West', this "
                    "lake is surrounded by hills and dense forests. TRAGUIN has arranged an exclusive private speed-boat "
                    "cruise for your family to enjoy the refreshing lake breeze. Relax along the waterfront, capture "
                    "beautiful sunset landscape frames, and engage in thrilling water sports activities."
                ),
                [
                    "Sightseeing Included: Dudhani Lake Waterfront, Madhuban Dam views, Local Tribal hamlets.",
                    "Evening Experience: Premium high-tea by the lakeside followed by traditional tribal dance observation if scheduled.",
                    "Overnight Stay: Silvassa (Premium Waterfront or Nature Resort).",
                    "Meals Included: Breakfast & Farewell Lakeside Resort Dinner.",
                ],
            ),
            _day(
                4,
                "Silvassa to Departure | Collecting Unforgettable Memories Beyond Destinations",
                (
                    "Savor a final, leisurely morning breakfast overlooking the manicured resort lawns. Spend an hour "
                    "shopping for heritage handicrafts and local Warli items before checking out. Your private premium "
                    "vehicle will comfortably transport you back to Vapi Railway Station or Mumbai Airport for your "
                    "return journey, carrying unforgettable memories of an exceptional eco-luxury holiday designed "
                    "flawlessly by TRAGUIN."
                ),
                [
                    "Transfers Included: Private luxury door-to-door station/airport drop-off.",
                    "Meals Included: Sumptuous Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Ras Resorts / similar | Khanvel Resort (Deluxe Room)",
                loc,
                "03 Nights",
                "Deluxe",
                "Deluxe Room",
                "MAPAI (Breakfast & Dinner)",
                4,
                1,
                description="OPTION 01 – DELUXE: Ras Resorts / similar (Silvassa, 2 Nights) | Khanvel Resort Deluxe Room (Khanvel, 1 Night) | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "Treat Resort Silvassa / similar | Khanvel Resort (Premium Wing)",
                loc,
                "03 Nights",
                "Premium",
                "Premium Wing Room",
                "MAPAI (Breakfast & Dinner)",
                5,
                2,
                description="OPTION 02 – PREMIUM: Treat Resort Silvassa / similar (Silvassa, 2 Nights) | Khanvel Resort Premium Wing (Khanvel, 1 Night) | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "Pluz Resort / Wonderland Resort | Forest Village Luxury Cottage",
                loc,
                "03 Nights",
                "Luxury",
                "Luxury Heritage Suite",
                "Gourmet Buffet Plan",
                5,
                3,
                description="OPTION 03 – LUXURY: Pluz Resort / Wonderland Resort (Silvassa, 2 Nights) | Forest Village Luxury Cottage (Khanvel, 1 Night) | Gourmet Buffet Plan",
            ),
            _hotel(
                "Treat Resort (Executive Luxury Suite) | Premium Private Pool Villa Stay",
                loc,
                "03 Nights",
                "Ultra Luxury",
                "Private Pool Villa",
                "Elite Custom Curated Meals",
                5,
                4,
                description="OPTION 04 – ULTRA LUXURY: Treat Resort Executive Luxury Suite (Silvassa, 2 Nights) | Premium Private Pool Villa Stay (Khanvel, 1 Night) | Elite Custom Curated Meals",
            ),
        ],
        inclusions=[
            _inc_included("Premium Stays: Accommodation at top-tier handpicked hotels and eco-resorts.", 1),
            _inc_included("Luxury Transportation: Private chauffeur-driven AC vehicle for transfers and sightseeing.", 2),
            _inc_included("Curated Culinary Plans: Daily buffet breakfast and lavish multi-cuisine dinners.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated personal concierge assistance.", 4),
            _inc_included("Welcome Kit: Complimentary signature arrival drinks and customized travel accessories.", 5),
            _inc_included("Exclusive Experiences: Private speed-boat ride experience at Dudhani Lake.", 6),
            _inc_excluded("Airfare or train transport tickets to connection points.", 7),
            _inc_excluded("Safari ride entry fees, camera permits, and local guide hire charges.", 8),
            _inc_excluded("Personal items such as laundry, phone calls, alcoholic beverages, or tips.", 9),
            _inc_excluded("Any water sports activity charges at Dudhani Lake beyond the included boat ride.", 10),
        ],
    )
    return package, itinerary


def build_dn_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DN-002"
    tour_code = "TRG-SIL-DN002"
    title = "Silvassa Weekend"
    duration = "02 Nights / 03 Days"
    slug = "dn-002-silvassa-weekend"
    itin_slug = "dn-002-silvassa-weekend-itinerary"
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
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Dadra and Nagar Haveli / India | Category: Premium Family Weekend Tour", 2),
            _ph("Destinations: Silvassa • Khanvel • Dudhani Waterfront", 3),
            _ph("Ideal for: Premium Family Vacations, Nature Enthusiasts & Luxury Escapes", 4),
            _ph("Best season: November to March (Pleasant Greens)", 5),
            _ph("Starting price: On Request (Bespoke Luxury Pricing)", 6),
            _ph("Vehicle & Meals: Private Luxury AC Innova / Premium MAPAI Plan", 7),
            _ph(
                "Route Map: Vapi/Mumbai Arrival → Vanganga & Tribal Museum → Vasona Safari & Dudhani Shikara → "
                "Swaminarayan Temple & Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Uniquely arranged high-tea basket along the picturesque Dudhani "
                "Waterfront banks.",
                9,
            ),
            _ph(
                "Shopping & Local Experiences: Authentic Warli paintings, bamboo mats, woven baskets, and river fish "
                "preparations at premium resort bistros.",
                10,
            ),
            _ph(
                "Important Notes: Vasona Lion Safari closed on Mondays; carry linen clothes and comfortable walking "
                "shoes; government photo ID required at check-in.",
                11,
            ),
        ],
        moods=["Nature", "Weekend", "Family"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Bespoke Luxury Pricing)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Silvassa Weekend • A Luxury Escape into Tribal Royalty & Nature",
        overview=(
            "Welcome to an exquisite weekend getaway crafted with perfection by TRAGUIN. This hand-tailored Silvassa "
            "Weekend getaway introduces your family to the breathtaking landscapes, Portuguese heritage, and lush green "
            "forests of Dadra and Nagar Haveli. Unwind amidst modern elegance and rustic charm with premium stays, "
            "immersive experiences, and specialized itineraries designed to curate unforgettable memories.\n\n"
            "TOUR OVERVIEW\n"
            "Your meticulously curated travel itinerary provides an idyllic blend of comfort, tribal culture, and pristine "
            "water views. Traveling in an elite, chauffeur-driven private vehicle, your family will enjoy absolute luxury "
            "across every scenic route. Enjoy a premium meal plan encompassing grand breakfasts and specialized culinary "
            "dinners at our handpicked hotels.\n\n"
            "WHY BOOK THE BEST SILVASSA TOUR PACKAGE?\n"
            "Tucked away on the banks of the Daman Ganga River, Silvassa is celebrated for its rich Portuguese past, "
            "beautiful tribal artistry, and iconic attractions. A premium Silvassa Family Tour brings to life highly-rated "
            "experiences such as the Vasona Lion Safari and the deeply immersive Tribal Culture Museum. Whether you want "
            "to enjoy adventure water sports at Dudhani Jetty or shop for rare Warli paintings, our TRAGUIN Silvassa "
            "Packages guarantee unmatched comfort and exclusive experiences."
        ),
        seo_title="DN-002 | Silvassa Weekend Premium Family Tour | TRAGUIN",
        seo_description=(
            "Premium 02 Nights / 03 Days Silvassa weekend package (DN-002 / TRG-SIL-DN002): Vanganga Lake Garden, "
            "Vasona Lion Safari, Dudhani Shikara cruise, Swaminarayan Temple, and 4-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Vanganga Lake Garden, Tribal Culture Museum & Roman Catholic Church on Day 01", 1),
            _ih("Vasona Lion Safari, Satmaliya Deer Park & Dudhani Shikara sunset cruise on Day 02", 2),
            _ih("BAPS Swaminarayan Temple, Kilvani Road shopping & departure on Day 03", 3),
            _ih("TRAGUIN Signature Experience: High-tea basket along the Dudhani Waterfront banks", 4),
            _ih("Curated by TRAGUIN Experts: Seamless safari coordination without standard queue waits", 5),
            _ih("Premium Handpicked Hotels: Resorts verified for safety, family recreation, and hospitality", 6),
        ],
        days=[
            _day(
                1,
                "Arrival in Silvassa | Portuguese Nostalgia, Manicured Gardens & Impressive Eco-Ways",
                (
                    "Your premium Silvassa experience starts with a warm welcome by our professional chauffeur at "
                    "Vapi/Valsad Railway Station or Mumbai Airport. Enjoy a seamless drive into the green capital of "
                    "Dadra and Nagar Haveli. Check into your ultra-luxury resort and relax. In the afternoon, explore "
                    "the beautifully designed Vanganga Lake Island Garden with rustic wooden bridges and manicured "
                    "flower beds. Follow this with a visit to the Tribal Cultural Museum, housing fascinating tribal "
                    "masks, musical instruments, and authentic Warli art artifacts."
                ),
                [
                    "Sightseeing Included: Vanganga Lake Garden, Tribal Culture Museum, Roman Catholic Church architecture.",
                    "Evening Experience: Relaxing paddle-boating on Vanganga Lake followed by a poolside welcome dinner arranged by TRAGUIN.",
                    "Overnight Stay: Silvassa (Premium Luxury Nature Resort).",
                    "Meals Included: Welcome Drink & Premium Buffet Dinner.",
                ],
            ),
            _day(
                2,
                "Silvassa to Khanvel & Dudhani Waterfront | Wild Lions, Mini-Kashmir Waterfront & Sunset Cruise",
                (
                    "Treat yourself to a lavish breakfast before setting out for the thrilling Vasona Lion Safari. Board "
                    "a secured private safari vehicle to spot Asiatic lions roaming in their natural forest habitat. Next, "
                    "take a scenic drive to Khanvel's beautiful green valleys and continue to the breathtaking Dudhani "
                    "Waterfront. Known as the 'Mini-Kashmir of the West', this large expanse of water formed by the "
                    "Madhuban Dam offers spectacular panoramic views. Enjoy a private Shikara boat ride as the sunset "
                    "casts beautiful golden hues over the horizon."
                ),
                [
                    "Sightseeing Included: Vasona Lion Safari Park, Satmaliya Deer Park trails, Dudhani Waterways, Madhuban Dam viewpoints.",
                    "Optional Activities: Speed boating, jet-skiing, or an immersive Warli painting workshop with local tribal artists.",
                    "Overnight Stay: Silvassa / Khanvel Premium Resort Property.",
                    "Meals Included: Premium Breakfast & Specialized Traditional Dinner.",
                ],
            ),
            _day(
                3,
                "Silvassa to Departure | Spiritual Calm, Shopping & Cherishing Sweet Memories",
                (
                    "Awake to the beautiful sounds of nature and enjoy a final breakfast at your resort. Visit the serene "
                    "and architecturally brilliant grand Swaminarayan Temple on the banks of the river, offering a "
                    "peaceful morning experience. Spend your remaining time shopping for authentic local souvenirs before "
                    "your private luxury car drives you comfortably back to Vapi Railway Station or Mumbai Airport."
                ),
                [
                    "Sightseeing Included: BAPS Swaminarayan Temple complex, Kilvani Road shopping avenues.",
                    "Transfers Included: Private door-to-door railway or airport drop-off.",
                    "Meals Included: Sumptuous Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel("Ras Resorts / Treat Resort (Deluxe Wing)", "Silvassa / Khanvel", "02 Nights", "Deluxe", "Executive Garden Room", "MAPAI (Breakfast & Dinner)", 4, 1),
            _hotel("Treat Resort Silvassa / Khanvel Resort", "Silvassa / Khanvel", "02 Nights", "Premium", "Premium Pool View Room", "MAPAI (Breakfast & Dinner)", 5, 2),
            _hotel("Pluz Resort / Khanvel Luxury Villa Complex", "Silvassa / Khanvel", "02 Nights", "Luxury", "Luxury Heritage Suite", "MAPAI (Breakfast & Dinner)", 5, 3),
            _hotel("The Fern Seaside Luxurious Resort / Custom Villa", "Silvassa / Khanvel", "02 Nights", "Ultra Luxury", "VVIP Private Plunge Pool Villa", "Ultra-Luxury Dining Experience", 5, 4),
        ],
        inclusions=[
            _inc_included("Premium Accommodation: 02 Nights stay at handpicked elite green properties.", 1),
            _inc_included("Luxury Transportation: Private AC Innova Crysta throughout the weekend tour.", 2),
            _inc_included("Curated Meals: Multi-cuisine breakfast buffets and signature dinners.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated concierge assistance and booking monitoring.", 4),
            _inc_included("Complimentary Experience: Private Shikara boat cruise ticket at Dudhani Waterfront.", 5),
            _inc_included("Welcome Kit: Regional non-alcoholic welcome drink and travel utilities.", 6),
            _inc_excluded("Flight tickets or main interstate train fares to arrival stations.", 7),
            _inc_excluded("Safari entry permits, museum tickets, and personal tour guide tips.", 8),
            _inc_excluded("Personal expenses such as minibar charges, laundry, and professional spa treatments.", 9),
            _inc_excluded("Any water sports charges or unexpected toll increases.", 10),
        ],
    )
    return package, itinerary


def build_dn_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DN-003"
    tour_code = "TRG-DN-003"
    title = "Leisure Silvassa"
    duration = "03 Nights / 04 Days"
    slug = "dn-003-leisure-silvassa"
    itin_slug = "dn-003-leisure-silvassa-itinerary"
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
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Dadra and Nagar Haveli / India | Category: Senior Citizen Special – Leisure Silvassa", 2),
            _ph("Destinations: Silvassa • Khanvel • Dudhani • Vasona", 3),
            _ph("Ideal for: Senior Citizens, Couples, Leisure Travelers & Nature Lovers", 4),
            _ph("Best season: November to March (Pleasant and Cool)", 5),
            _ph("Starting price: Premium Custom Pricing Available on Request", 6),
            _ph("Vehicle & Meal Plan: Premium Chauffeur AC Vehicle / MAPAI Plan", 7),
            _ph(
                "Route Map: Vapi/Mumbai Arrival → Portuguese Heritage & Gardens → Tribal Museum & Vasona Safari → "
                "Dudhani Pontoon Cruise → Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Slower, deeply thoughtful itinerary pace optimized for senior comfort.",
                9,
            ),
            _ph(
                "Shopping & Local Experiences: Tribal Warli paintings, forest honey, bamboo woodwork, and mild "
                "Gujarati-Maharashtrian fusion cuisine.",
                10,
            ),
            _ph(
                "Important Notes: Check-in 14:00 hrs, check-out 11:00 hrs; Aadhaar or Passport required; book 30 "
                "days ahead for riverbank villa availability.",
                11,
            ),
        ],
        moods=["Leisure", "Nature", "Senior Friendly"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="Premium Custom Pricing Available on Request",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Leisure Silvassa • Tracing Portuguese Legacies & Pure Nature",
        overview=(
            "Welcome to a tranquil world of luxury and absolute relaxation designed especially for our valued elders, "
            "thoughtfully brought to you by TRAGUIN. Embark on the finest Dadra and Nagar Haveli Family Tour, specially "
            "tuned for slow-paced relaxation amidst breathtaking landscapes, exotic Portuguese-influenced history, and "
            "gentle nature sanctuaries.\n\n"
            "TOUR OVERVIEW\n"
            "This meticulously planned luxury holiday itinerary provides a flawless, stress-free route tailored around "
            "comfort and accessibility for senior travelers. Traveling in a premium AC sedan or MPV with professional "
            "assistance and an exceptionally polite chauffeur, your journey remains fully customizable and relaxing. "
            "With curated meal planning presenting gourmet options that look after health and dietary requirements, this "
            "is truly the ultimate senior special vacation.\n\n"
            "WHY BOOK A LUXURY DADRA AND NAGAR HAVELI HOLIDAY?\n"
            "Dadra and Nagar Haveli remains an elite, hidden eco-haven in Western India. Silvassa sightseeing stands "
            "out due to its iconic attractions such as the tribal museum, calm river waterfronts, and sprawling green "
            "gardens. From local Warli painting workshops to peaceful boat cruises, our signature TRAGUIN packages "
            "focus on high comfort and handpicked premium stays."
        ),
        seo_title="DN-003 | Leisure Silvassa Senior Special Tour | TRAGUIN",
        seo_description=(
            "Premium 03 Nights / 04 Days Leisure Silvassa package (DN-003 / TRG-DN-003): Church of Our Lady of Piety, "
            "Tribal Museum, Vasona Lion Safari, Dudhani pontoon cruise, and senior-friendly 4-tier accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Church of Our Lady of Piety, public gardens & peaceful resort high-tea on Day 01", 1),
            _ih("Silvassa Tribal Culture Museum, Vasona Lion Safari & Satmaliya Deer Park on Day 02", 2),
            _ih("Dudhani Lake pontoon cruise & Hirwa Van Terraced Gardens on Day 03", 3),
            _ih("Relaxed farewell breakfast & smooth departure transfer on Day 04", 4),
            _ih("TRAGUIN Signature Experience: Slower itinerary pace optimized for senior comfort", 5),
            _ih("Curated by TRAGUIN Experts: Handpicked resorts with elevators and zero-stair walking paths", 6),
            _ih("Premium Luxury Transportation: Safe driving with hydration breaks and luggage assistance", 7),
        ],
        days=[
            _day(
                1,
                "Arrival in Silvassa | Welcome to Silvassa – Tranquil Check-In & Royal Portuguese Heritage",
                (
                    "Your premium Dadra and Nagar Haveli experience begins with a smooth pickup by your private luxury "
                    "transport at Vapi Railway Station or Mumbai Airport. Enjoy a gentle, seamless drive to Silvassa, "
                    "the lush capital town wrapped in old colonial charm. Check into your premium resort selected for "
                    "easy access, beautiful gardens, and senior-friendly layout. After lunch, proceed for light "
                    "sightseeing to the historic Roman Catholic Church of Our Lady of Piety, built by the Portuguese "
                    "in the late 19th century. Enjoy a quiet, relaxing walk around the manicured pathways of the local "
                    "public gardens."
                ),
                [
                    "Sightseeing Included: Church of Our Lady of Piety, Silvassa Public Gardens & Colonial Walk.",
                    "Evening Experience: A peaceful high-tea session followed by a gentle sit-down dinner at the resort garden.",
                    "Overnight Stay: Silvassa (Premium Luxury Riverside Resort).",
                    "Meals Included: Welcome Drink & Gourmet Dinner.",
                ],
            ),
            _day(
                2,
                "Silvassa Tribal Culture & Vasona Lion Safari | Immersive Tribal History & Wildlife Majesty",
                (
                    "Start your day with a calm breakfast before venturing into the local Silvassa Tribal Museum with "
                    "easy, flat walking paths to explore unique local heritage, musical instruments, historic ornaments, "
                    "and beautiful Warli clay artifacts. Next, head to the Vasona Lion Safari Park and board an enclosed, "
                    "comfortable safari vehicle to observe Asiatic lions roaming naturally inside open forest enclosures. "
                    "Conclude your afternoon at the scenic, well-paved Deer Park at Khanvel to view gentle spotted deer "
                    "resting under natural green canopies."
                ),
                [
                    "Sightseeing Included: Silvassa Tribal Culture Museum, Vasona Lion Safari, Satmaliya Deer Park.",
                    "Optional Activities: A basic interactive Warli painting session with local award-winning artists.",
                    "Overnight Stay: Silvassa / Khanvel Luxury Resort.",
                    "Meals Included: Premium Breakfast & Dinner.",
                ],
            ),
            _day(
                3,
                "Excursion to Dudhani Lake Waterfront | Scenic Beauty & Serene Waterways of Madhuban",
                (
                    "Indulge in a beautiful morning drive through rolling hill slopes and teak forests towards Dudhani, "
                    "a magnificent large lakeside area created by the Madhuban Dam reservoir. TRAGUIN has organized a "
                    "safe, exclusive, private boat ride on a stable luxury pontoon boat for your absolute comfort. Enjoy "
                    "the gentle breeze while gliding over the water. On the return route, stop at the elegant, manicured "
                    "terraces of Hirwa Van Garden to enjoy gentle waterfalls and beautiful seasonal floral arrangements."
                ),
                [
                    "Sightseeing Included: Dudhani Lake Overlook, Private Pontoon Cruise, Hirwa Van Terraced Gardens.",
                    "Evening Experience: Light stroll across local handicraft shops followed by a custom health-conscious dinner.",
                    "Overnight Stay: Silvassa (Premium Handpicked Stay).",
                    "Meals Included: Breakfast & Premium Farewell Dinner.",
                ],
            ),
            _day(
                4,
                "Silvassa to Departure | Cherishing Memories Beyond Destinations",
                (
                    "Wake up to a crisp morning mist rising from the river. Relish a healthy, relaxed buffet breakfast at "
                    "your resort's terrace. Spend your morning capturing final group photos amidst the resort's gardens "
                    "before your luxury vehicle drives you back smoothly to Vapi Railway Station or Mumbai Airport."
                ),
                [
                    "Transfers Included: Private door-to-door transit to airport or railway station.",
                    "Meals Included: Lavish Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel("Ras Resorts Silvassa / similar", "Silvassa", "03 Nights", "Deluxe", "Executive Garden Room", "MAPAI (Breakfast & Dinner)", 4, 1, description="OPTION 01 – DELUXE: Ras Resorts Silvassa / similar (Silvassa, 3 Nights) | Ground-floor allocation on request | MAPAI (Breakfast & Dinner)"),
            _hotel("Treat Resort, Silvassa", "Silvassa", "03 Nights", "Premium", "Premium Pool View Room", "MAPAI (Breakfast & Dinner)", 5, 2, description="OPTION 02 – PREMIUM: Treat Resort, Silvassa (Silvassa, 3 Nights) | Welcome fruit basket & tea pack | MAPAI (Breakfast & Dinner)"),
            _hotel("Khanvel Resort / Pluz Resort", "Silvassa", "03 Nights", "Luxury", "Luxury Garden Villa Suite", "MAPAI (Breakfast & Dinner)", 5, 3, description="OPTION 03 – LUXURY: Khanvel Resort / Pluz Resort (Silvassa, 3 Nights) | Wheelchair assistance & private guide | MAPAI (Breakfast & Dinner)"),
            _hotel("The Fern Seaside Luxurious Hub / Elite Villa", "Silvassa", "03 Nights", "Ultra Luxury", "VVIP Royal Club Suite", "Bespoke Gourmet Plan", 5, 4, description="OPTION 04 – ULTRA LUXURY: The Fern Seaside Luxurious Hub / Elite Villa (Silvassa, 3 Nights) | Private butler & tailored custom meals"),
        ],
        inclusions=[
            _inc_included("Premium Accommodation: Senior-friendly rooms with minimal steps or lift access.", 1),
            _inc_included("Luxury Transportation: Private smooth-riding AC Sedan with a professional assistant chauffeur.", 2),
            _inc_included("Curated Meal Plan: Healthy breakfasts and mild, less-spicy gourmet dinners.", 3),
            _inc_included("TRAGUIN Support: 24/7 round-the-clock dedicated guest safety manager on speed dial.", 4),
            _inc_included("Welcome Amenities: Gentle wellness travel gift pack with hand sanitizers and healthy dry fruits.", 5),
            _inc_included("Exclusive Experience: Safe, private pontoon boat tickets at Dudhani with lifejackets.", 6),
            _inc_excluded("Main flight tickets or long-distance interstate train bookings.", 7),
            _inc_excluded("Historical monument entry passes, special camera permits, and personal tips.", 8),
            _inc_excluded("Personal laundry, room minibar usage, phone calls, and optional medical insurances.", 9),
            _inc_excluded("Any extra sightseeing paths or extended vehicle mileage outside the original route.", 10),
        ],
    )
    return package, itinerary


def build_dn_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DN-004"
    tour_code = "TRG-DNH-004"
    title = "Tribal Nature Escape"
    duration = "04 Nights / 05 Days"
    slug = "dn-004-tribal-nature-escape"
    itin_slug = "dn-004-tribal-nature-escape-itinerary"
    loc = "Silvassa (2 Nights) / Khanvel / Dudhni (2 Nights)"
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
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Dadra and Nagar Haveli / India | Category: Adventure & Tribal Nature Escape", 2),
            _ph("Destinations: Silvassa • Khanvel • Dudhni Lake • Satmaliya • Vasona", 3),
            _ph("Ideal for: Nature Lovers, Adventure Enthusiasts & Culture Seekers", 4),
            _ph("Best season: November to March (Lush Greenery in September/October)", 5),
            _ph("Starting price: On Request (Premium Tailor-Made)", 6),
            _ph("Vehicle / Meals: Private Luxury AC Vehicle / Executive Breakfast & Dinner", 7),
            _ph(
                "Route Map: Silvassa Arrival → Khanvel Safari & Warli Workshop → Dudhni Water Sports → "
                "Silvassa Heritage Trail → Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private Warli heritage art collective tour with interactive tribal "
                "community briefing.",
                9,
            ),
            _ph(
                "Shopping & Local Experiences: Hand-painted Warli artwork, bamboo handicrafts, organic forest honey, "
                "and traditional village cuisine.",
                10,
            ),
            _ph(
                "Important Notes: Check-in 14:00 hrs; government photo IDs required; book safari seats and lake "
                "pontoon experiences well in advance.",
                11,
            ),
        ],
        moods=["Adventure", "Nature", "Cultural"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Tailor-Made)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Tribal Nature Escape • Wilderness, Water Sports & Warli Culture",
        overview=(
            "Welcome to an extraordinary ecosystem of wilderness, untamed water trails, and vivid folklore proudly "
            "crafted by TRAGUIN. This bespoke Dadra and Nagar Haveli Adventure tour has been passionately "
            "conceptualized for modern explorers craving authentic encounters. Immerse your senses into breathtaking "
            "landscapes, emerald-canopied woods, and age-old tribal legacies.\n\n"
            "TOUR OVERVIEW\n"
            "This elite itinerary spans across the lush geography of Dadra and Nagar Haveli, unveiling a pristine world "
            "away from mainland commotion. From thrilling watersports on the vast waters of Dudhni Lake to intimate "
            "tribal Warli art meetups in local villages, every single day is an elevated journey blending rugged "
            "wilderness trail explorations with high-end culinary treats.\n\n"
            "WHY BOOK THE BEST DADRA AND NAGAR HAVELI TOUR PACKAGE?\n"
            "Celebrated for its unique historical blend, Dadra and Nagar Haveli presents some of the finest eco-tourism "
            "landscapes in the country. From the serene waters of Dudhni Lake to the roaring wildlife paths of Vasona "
            "Lion Safari, the territory promises iconic attractions for groups, families, and solo explorers alike."
        ),
        seo_title="DN-004 | Tribal Nature Escape Adventure Tour | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days tribal nature package (DN-004 / TRG-DNH-004): Satmaliya Deer Park, "
            "Vasona Lion Safari, Dudhni jet-ski and sunset cruise, Nakshatra Garden, and 4-tier accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Tribal Cultural Museum, Vanganga Lake Garden & torch-lit resort dinner on Day 01", 1),
            _ih("Satmaliya Deer Park, Vasona Lion Safari & exclusive Warli workshop on Day 02", 2),
            _ih("Dudhni Lake jet-ski, speed-boating & sunset pontoon cruise on Day 03", 3),
            _ih("Swaminarayan Temple, Nakshatra Garden & Tarpa Dance farewell on Day 04", 4),
            _ih("Smooth departure transfer from Silvassa on Day 05", 5),
            _ih("TRAGUIN Signature Experience: Private Warli heritage art collective tour", 6),
            _ih("Curated by TRAGUIN Experts: Itineraries matched to best wildlife viewing and photography lighting", 7),
        ],
        days=[
            _day(
                1,
                "Arrival in Silvassa | Welcome to the Tribal Capital – Portuguese Echoes & Urban Escape",
                (
                    "Your premium Dadra and Nagar Haveli sightseeing experience begins with a warm welcome at Vapi "
                    "Railway Station or Mumbai International Airport by a designated private luxury chauffeur. Enjoy a "
                    "smooth drive into Silvassa and check into your premium handpicked luxury resort surrounded by "
                    "pristine greenery. Spend your afternoon visiting the iconic Tribal Cultural Museum displaying "
                    "ancient musical instruments, fishing gear, and legendary Warli artifacts. Later, take an atmospheric "
                    "stroll through the carefully landscaped paths of Vanganga Lake Garden."
                ),
                [
                    "Sightseeing Included: Tribal Cultural Museum, Vanganga Lake Garden, Silvassa local cathedral.",
                    "Evening Experience: Private torch-lit dinner at the resort featuring premium local cuisine curated by TRAGUIN experts.",
                    "Overnight Stay: Silvassa (Premium Riverscape Resort).",
                    "Meals Included: Welcome Drink & Gourmet Dinner.",
                ],
            ),
            _day(
                2,
                "Silvassa to Khanvel & Satmaliya | Deep Forest Safari, Wildlife Encounters & Tribal Art Insights",
                (
                    "Relish a lavish breakfast before setting off into the dense woods of Khanvel. Your first adventure "
                    "stop is the Satmaliya Deer Park, where a private open-top safari vehicle will take you to see "
                    "Blackbucks, Chinkaras, and Spotted Deer roaming through breathtaking landscapes. Next, proceed to "
                    "the Vasona Lion Safari to witness Asiatic Lions up close in their natural habitat. In the late "
                    "afternoon, enjoy an exclusive tribal Warli workshop, interacting directly with indigenous master "
                    "artists who preserve ancient folklore through geometric canvas paintings."
                ),
                [
                    "Sightseeing Included: Satmaliya Deer Park, Vasona Lion Safari, Khanvel Forest Range.",
                    "Optional Activities: Personalized Warli canvas painting masterclass with take-home souvenir kits.",
                    "Overnight Stay: Khanvel (Premium Luxury Nature Lodge).",
                    "Meals Included: Premium Breakfast & Organic Forest Dinner.",
                ],
            ),
            _day(
                3,
                "Excursion to Dudhni Lake | Adventure Water Sporting Olympus & Sunset Cruise",
                (
                    "Prepare for an action-packed day as you travel to Dudhni Lake, a massive waterfront formed by the "
                    "dammed waters of the Madhuban Reservoir. Enjoy a thrilling premium jet-ski ride and speed-boating "
                    "experience across the expansive lake. In the evening, step aboard a traditional decorated Shikara or "
                    "private luxury pontoon boat for a peaceful sunset cruise, capturing spectacular panoramic views of "
                    "the surrounding hills."
                ),
                [
                    "Sightseeing Included: Dudhni Lake Waterfront, Madhuban Dam outer panoramic vistas, Tribal Waterfront Hamlets.",
                    "Evening Experience: Premium lakeside high-tea and private acoustic musical session during sunset.",
                    "Overnight Stay: Khanvel / Dudhni Waterfront Cottages.",
                    "Meals Included: Breakfast & Exquisite Lakeside Barbecue Dinner.",
                ],
            ),
            _day(
                4,
                "Khanvel to Silvassa Heritage Trail | Meditative Gardens & Architectural Splendour",
                (
                    "Journey back toward Silvassa along winding roads framed by beautiful tall trees. Dedicate your "
                    "afternoon to exploring the magnificent BAPS Swaminarayan Temple, celebrated for its intricate pink "
                    "stone carving architecture. Next, visit the beautiful Nakshatra Garden, an astrological theme park "
                    "featuring diverse therapeutic flora and popular Instagram locations. Conclude your day with a visit "
                    "to the historic Church of Our Lady of Piety, a beautiful reminder of the region's colonial past."
                ),
                [
                    "Sightseeing Included: BAPS Swaminarayan Temple, Nakshatra Garden, Church of Our Lady of Piety.",
                    "Evening Experience: Farewell tribal dance presentation (Tarpa Dance) performed exclusively for TRAGUIN guests.",
                    "Overnight Stay: Silvassa (Premium Luxury Stay).",
                    "Meals Included: Breakfast & Premium Multi-cuisine Dinner.",
                ],
            ),
            _day(
                5,
                "Departure from Silvassa | Collecting Unforgettable Memories Beyond Destinations",
                (
                    "Enjoy a final luxurious breakfast at your resort while taking in the beautiful forest views. Pack "
                    "your bags and load your premium transport vehicle with beautiful memories and souvenirs. Your "
                    "private vehicle will drop you off at Vapi Railway Station or Mumbai International Airport for your "
                    "return home."
                ),
                [
                    "Transfers Included: Private luxury highway drop-off to station/airport.",
                    "Meals Included: Lavish Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Ras Resorts / similar | Khanvel Resort / similar",
                loc,
                "04 Nights",
                "Deluxe",
                "Executive Garden View",
                "MAPAI (Breakfast & Dinner)",
                4,
                1,
                description="OPTION 01 – DELUXE: Ras Resorts / similar (Silvassa, 2 Nights) | Khanvel Resort / similar (Khanvel/Dudhni, 2 Nights) | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "Treat Resort Silvassa / similar | Pluz Resort Khanvel / similar",
                loc,
                "04 Nights",
                "Premium",
                "Premium Pool View Room",
                "MAPAI (Breakfast & Dinner)",
                5,
                2,
                description="OPTION 02 – PREMIUM: Treat Resort Silvassa / similar (Silvassa, 2 Nights) | Pluz Resort Khanvel / similar (Khanvel/Dudhni, 2 Nights) | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "Wonderland Resort Luxury Wing | Dudhni Lakeside Luxury Cottages",
                loc,
                "04 Nights",
                "Luxury",
                "Luxury River Front Cottage",
                "MAPAI (Breakfast & Dinner)",
                5,
                3,
                description="OPTION 03 – LUXURY: Wonderland Resort Luxury Wing (Silvassa, 2 Nights) | Dudhni Lakeside Luxury Cottages (Khanvel/Dudhni, 2 Nights) | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "VVIP Private Villa Wing (Treat) | Bespoke Forest Glamping Villa",
                loc,
                "04 Nights",
                "Ultra Luxury",
                "Private Plunge Pool Suite",
                "Elite Custom Curated Meals",
                5,
                4,
                description="OPTION 04 – ULTRA LUXURY: VVIP Private Villa Wing Treat (Silvassa, 2 Nights) | Bespoke Forest Glamping Villa (Khanvel/Dudhni, 2 Nights) | Elite Custom Curated Meals",
            ),
        ],
        inclusions=[
            _inc_included("Premium Accommodation: Luxury resort stays as specified above.", 1),
            _inc_included("Luxury Transportation: Private chauffeur-driven AC vehicle for transfers and trails.", 2),
            _inc_included("Curated Meal Plan: Lavish daily breakfasts and signature thematic dinners.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated local guest experience executive.", 4),
            _inc_included("Welcome Amenities: Native welcome drink, chilled towels, and a premium travel kit.", 5),
            _inc_included("Exclusive Experiences: Private sunset boat ride ticket at Dudhni Lake.", 6),
            _inc_excluded("Airfare, flight surcharges, and interstate rail travel tickets.", 7),
            _inc_excluded("Watersports equipment rental, jet-ski charges, and additional safari tickets.", 8),
            _inc_excluded("Personal expenses such as laundry, alcohol, minibar, and tips.", 9),
            _inc_excluded("Any insurance premium or costs arising from unpredictable natural occurrences.", 10),
        ],
    )
    return package, itinerary


def build_dn_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DN-005"
    tour_code = "TRG-DN-005"
    title = "Complete Silvassa Escapade"
    duration = "04 Nights / 05 Days"
    slug = "dn-005-complete-silvassa-escapade"
    itin_slug = "dn-005-complete-silvassa-escapade-itinerary"
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
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Dadra and Nagar Haveli / India | Category: Premium Family Tour", 2),
            _ph("Destinations: Silvassa • Khanvel • Dudhani • Vasona • Luhari", 3),
            _ph("Ideal for: Premium Family Holidays, Couples & Nature Enthusiasts", 4),
            _ph("Best season: November to March", 5),
            _ph("Starting price: On Request (Premium Customized Portfolio)", 6),
            _ph("Vehicle & Meal Plan: Chauffeur-Driven Premium AC Sedan/SUV • MAPAI Base", 7),
            _ph(
                "Route Map: Silvassa Arrival → Vasona Safari & Nakshatra → Dudhani Speed Boat → "
                "Khanvel & Luhari → Swaminarayan Temple Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private, slow-travel tribal interactions and curated village art walks.",
                9,
            ),
            _ph(
                "Shopping & Local Experiences: Hand-painted Warli artwork, organic wild honey, bamboo utility "
                "products, and handmade paper lampsheets.",
                10,
            ),
            _ph(
                "Important Notes: Jungle safaris and lake villas require early confirmation; winter ideal for outdoor "
                "exploration; vehicle usage per specified custom schedule map.",
                11,
            ),
        ],
        moods=["Nature", "Family", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Customized Portfolio)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Complete Silvassa Escapade • Forests, Lakes & Portuguese Elegance",
        overview=(
            "Welcome to an unforgettable escape custom-tailored by TRAGUIN. Discover the ultimate Dadra and Nagar "
            "Haveli Family Tour, structured precisely to unlock the mesmerizing scenic beauty, indigenous tribal "
            "heritage, and Portuguese architectural marvels of this serene Union Territory. From the tranquil waters of "
            "Dudhani Lake to the thrilling wildlife tracks of Vasona Lion Safari, immerse yourself in premium luxury "
            "stays and natural brilliance.\n\n"
            "TOUR OVERVIEW\n"
            "This bespoke travel program offers an exquisite balance between luxury relaxation, wildlife discovery, and "
            "deep-rooted cultural exploration. Your family will enjoy private executive door-to-door transit in a premium "
            "vehicle with round-the-clock professional assistance. Featuring a handpicked selection of top-tier jungle "
            "resorts and riverside boutique properties, our specialized meal plan provides an authentic taste of western "
            "regional and international culinary creations.\n\n"
            "WHY CHOOSE THE BEST SILVASSA TOUR PACKAGE?\n"
            "Silvassa boasts some of the most iconic attractions in Western India—from the legendary Swaminarayan "
            "Temple to the lush canopies of Nakshatra Garden and the mesmerizing expanse of the Madhuban Dam. "
            "Whether you look forward to authentic Warli painting workshops or artisanal woodcraft shopping, our "
            "TRAGUIN packages align premium stays and curated exclusive experiences perfectly."
        ),
        seo_title="DN-005 | Complete Silvassa Escapade Premium Tour | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Complete Silvassa package (DN-005 / TRG-DN-005): Tribal Cultural Museum, "
            "Vasona Lion Safari, Dudhani speed boat, Khanvel & Luhari, and 4-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Tribal Cultural Museum, Vanganga Lake Garden & musical fountain show on Day 01", 1),
            _ih("Vasona Lion Safari, Satmali Deer Park & Nakshatra Garden on Day 02", 2),
            _ih("Dudhani private speed boat charter & Warli tribal interactions on Day 03", 3),
            _ih("Khanvel, Bindrabin Temple, Luhari forest paths & Our Lady of Piety Church on Day 04", 4),
            _ih("Swaminarayan Temple visit & smooth departure transfer on Day 05", 5),
            _ih("TRAGUIN Signature Experience: Private slow-travel tribal interactions and village art walks", 6),
            _ih("Curated by TRAGUIN Experts: Seamless routing planned to avoid weekend crowds at major family spots", 7),
        ],
        days=[
            _day(
                1,
                "Arrival in Silvassa | Welcome to the Garden City – Tranquil Landscapes & Luxury Arrival",
                (
                    "Your premium Silvassa experience begins as you arrive at Vapi Railway Station or Mumbai Airport, "
                    "where a private chauffeur-driven luxury vehicle greets your family. Enjoy a smooth drive into "
                    "Silvassa and check into your premium riverside luxury resort. In the afternoon, visit the Tribal "
                    "Cultural Museum showcasing ancient musical instruments, authentic Warli artifacts, and hunting "
                    "tools. Later, visit the beautifully manicured Vanganga Lake Garden for a peaceful evening walk "
                    "across its classic wooden bridges."
                ),
                [
                    "Sightseeing Included: Tribal Cultural Museum, Vanganga Lake Garden, local artisanal markets.",
                    "Evening Experience: Private family musical fountain show viewing with premium resort evening high-tea.",
                    "Overnight Stay: Silvassa (Premium Waterfront / Luxury Riverside Resort).",
                    "Meals Included: Welcome Mocktail & Gourmet Buffet Dinner.",
                ],
            ),
            _day(
                2,
                "Vasona Lion Safari & Satmali Deer Park | Wildlife Majesty & Immersive Eco-Adventures",
                (
                    "Enjoy a lavish morning breakfast before heading out for a thrilling day of wildlife encounters. "
                    "Board a secured private safari vehicle at the Vasona Lion Safari Park to see majestic Asiatic lions "
                    "roaming in their natural habitat. Continue through the deep green woods to the Satmali Deer Park "
                    "to spot sambar, chital, and blackbucks. In the evening, visit the serene Nakshatra Garden, a "
                    "beautifully designed astro-themed park filled with medicinal plants and stunning walkways."
                ),
                [
                    "Sightseeing Included: Vasona Lion Safari, Satmali Deer Park, Nakshatra Garden walking trails.",
                    "Photography Points: Exotic bird observation decks and panoramic woodland viewpoints.",
                    "Overnight Stay: Silvassa (Premium Resort Property).",
                    "Meals Included: Premium Breakfast & Luxury Dinner.",
                ],
            ),
            _day(
                3,
                "Excursion to Dudhani Lake | The Kashmir of the West – Private Waterfront Luxury",
                (
                    "Depart after a delicious breakfast on a scenic drive to Dudhani, a magnificent waterfront "
                    "destination formed by the waters of the Madhuban Dam. TRAGUIN has arranged a private luxury "
                    "speed boat charter across the shimmering waters. Spend a relaxed afternoon interacting with local "
                    "Warli tribes, learning their historical painting techniques, and savoring local culinary specialties."
                ),
                [
                    "Sightseeing Included: Dudhani Waterfront, Madhuban Dam Panoramic Deck, Tribal Artisan Quarter.",
                    "Optional Activities: Jet-skiing, traditional wooden boat rides, or a customized premium lakeside picnic.",
                    "Overnight Stay: Silvassa / Dudhani Lakeside Luxury Resort.",
                    "Meals Included: Premium Breakfast & Authentic Organic Fusion Dinner.",
                ],
            ),
            _day(
                4,
                "Silvassa to Khanvel & Luhari | Serene Jungle Canopies & Historic Portuguese Memories",
                (
                    "Drive down the tree-lined avenues toward Khanvel, a beautiful pastoral landscape surrounded by "
                    "lush green forests. Visit the beautiful Bindrabin Temple situated elegantly on the banks of the "
                    "Sakartod River. Spend the afternoon wandering through the tranquil forest paths of Luhari, which "
                    "offer a completely peaceful escape. In the evening, visit the grand Our Lady of Piety Church, "
                    "built by the Portuguese in 1889, showcasing spectacular stone architecture."
                ),
                [
                    "Sightseeing Included: Khanvel Forest Zone, Bindrabin Temple, Our Lady of Piety Church, Luhari green hills.",
                    "Evening Experience: A relaxed candlelight poolside dinner at your luxury resort, organized by TRAGUIN experts.",
                    "Overnight Stay: Silvassa Luxury Cottage Villa.",
                    "Meals Included: Premium Breakfast & Gala Farewell Dinner.",
                ],
            ),
            _day(
                5,
                "Departure via Swaminarayan Temple | Carrying Home Unforgettable Memories",
                (
                    "Indulge in a final lavish breakfast at your resort before preparing for check-out. Visit the "
                    "magnificent, intricately carved pink stone Swaminarayan Temple, renowned for its architectural "
                    "beauty and peaceful spiritual atmosphere. Later, your private luxury transport vehicle will safely "
                    "drive you back to Vapi Railway Station or Mumbai Airport."
                ),
                [
                    "Transfers Included: Private door-to-door transit drop-off.",
                    "Meals Included: Sumptuous Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel("Pluz Resort / Wonderland Resort / similar", "Silvassa / Khanvel", "04 Nights", "Deluxe", "Executive Deluxe Room", "MAPAI (Breakfast & Dinner)", 4, 1),
            _hotel("Ras Resorts Silvassa / Khanvel Resort / similar", "Silvassa / Khanvel", "04 Nights", "Premium", "Premium Pool View Room", "MAPAI (Breakfast & Dinner)", 5, 2),
            _hotel("Treat Resort Silvassa / similar", "Silvassa / Khanvel", "04 Nights", "Luxury", "Luxury Club Room Suite", "MAPAI (Breakfast & Dinner)", 5, 3),
            _hotel("Treat Resort (Elite Executive Royal Villa)", "Silvassa / Khanvel", "04 Nights", "Ultra Luxury", "Private Pool Luxury Villa", "Bespoke Gourmet Dine Inclusive", 5, 4),
        ],
        inclusions=[
            _inc_included("Premium Accommodation: Handpicked luxury stays as per chosen category portfolio.", 1),
            _inc_included("Luxury Transportation: Private chauffeur-driven AC transit throughout the tour route.", 2),
            _inc_included("Curated Meal Plan: Lavish daily breakfast spread and customized table d'hôte dinners.", 3),
            _inc_included("TRAGUIN Assistance: 24/7 dedicated remote ground operations coordinator.", 4),
            _inc_included("Welcome Amenities: Cold towels, specialized family travel kits, and mineral water supply.", 5),
            _inc_included("Complimentary Experiences: Private speed-boat ride experience voucher at Dudhani Lake.", 6),
            _inc_excluded("Airfare, interstate permits, or long-distance railway tickets.", 7),
            _inc_excluded("Monument entry fees, camera charges, and personal local guide fees.", 8),
            _inc_excluded("Personal expenses such as laundry services, premium beverages, and tipping.", 9),
            _inc_excluded("Any optional watersports, specialized safari bookings, or extension travel routes.", 10),
        ],
    )
    return package, itinerary

def build_dn_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DN-006"
    tour_code = "TG-DN-006-PREM"
    title = "Silvassa Quick Nature Getaway"
    duration = "01 Night / 02 Days"
    slug = "dn-006-silvassa-quick-nature-getaway"
    itin_slug = "dn-006-silvassa-quick-nature-getaway-itinerary"
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
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Dadra and Nagar Haveli / India | Category: Weekend Getaway", 2),
            _ph("Destinations: Silvassa & Surrounding Nature Trails", 3),
            _ph("Ideal for: Couples, Families & Nature Enthusiasts", 4),
            _ph("Best season: November to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Weekend FIT Getaway", 7),
            _ph("Vehicle: Premium Executive Sedan / SUV at disposal", 8),
            _ph("Meal Plan: Modified American Plan (Buffet Breakfast & Chef's Special Dinner)", 9),
            _ph("Route Map: Vapi/Surat Arrival → Silvassa Nature Circuit → Vapi/Surat Departure", 10),
            _ph("TRAGUIN Signature Experience: Private interaction session with local Warli artists", 11),
            _ph("Shopping: Warli Art Masterpieces, Pure Forest Honey, Handcrafted Wooden Artifacts", 12),
            _ph("Important: Wildlife parks operate on restricted timing; book weekends 3 weeks prior", 13),
        ],
        moods=["Nature", "Weekend", "Leisure"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Class)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Silvassa Quick Nature Getaway • Escape Into the Green Lap",
        overview=(
            "Escape the mechanical rush of city life and breathe in the rich emerald air of Silvassa. Carefully "
            "mapped out by the luxury curators at TRAGUIN, this rapid rejuvenation getaway is crafted to maximize "
            "your weekend tranquility. Experience breathtaking landscapes, immersive experiences in tribal cultures, "
            "and serene boat cruises surrounded by pristine woodlands.\n\n"
            "Our Silvassa Quick Nature Getaway offers a brilliant blend of winding forest corridors, Portuguese "
            "architectural remnants, and elite hospitality. Sized perfectly for a swift yet luxurious weekend "
            "breakthrough, this layout ensures zero stress and complete immersion.\n\n"
            "TRAGUIN Curated Touch: Handpicked hotels boasting private riverfront views, pre-booked VIP access "
            "tickets to wildlife reserves, and customized refreshment kits onboard your premium transport.\n\n"
            "Why Visit Dadra and Nagar Haveli: Unparalleled forest canopy density, tranquil lakes, rare wildlife "
            "encounters, and duty-free relaxation zones. Famous Attractions: Vanganga Lake Garden, Tribal Cultural "
            "Museum, Khanvel, and the Nakshatra Garden. Most Searched Experiences: Quiet shikara boat rides on "
            "pristine lake waters, photographing deer herds in natural habitats, and shopping for authentic Warli "
            "tribal paintings. Popular Instagram Locations: The rustic wooden bridges of Vanganga Lake, sunset view "
            "points at Dudhni, and lush avenues of Nakshatra Garden."
        ),
        seo_title="DN-006 | Silvassa Quick Nature Getaway Premium Tour | TRAGUIN",
        seo_description=(
            "Premium 01 Night / 02 Days Silvassa nature package (DN-006 / TG-DN-006-PREM): Tribal Cultural Museum, "
            "Vanganga Lake Garden, Vasona Lion Safari, Nakshatra Garden, and 4-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Tribal Cultural Museum & Vanganga Lake Garden", 1),
            _ih("Vasona Lion Safari & Nakshatra Garden", 2),
            _ih("TRAGUIN Signature Experience: Private interaction session with local Warli artists", 3),
            _ih("Curated by TRAGUIN Experts: Perfect layout sequence designed to minimize travel fatigue", 4),
            _ih("Premium Handpicked Hotels: Properties certified for elite hospitality and safety standards", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Silvassa & Immersion Into Vanco Life",
                (
                    "Your refreshing weekend begins with a scenic drive through smooth country roads as you arrive in "
                    "the capital city of Silvassa. Receive a warm greeting from your dedicated TRAGUIN host and check "
                    "into your handpicked premium resort featuring luxurious rooms looking over manicured lawns or "
                    "flowing river pathways. After standard check-in formalities, refresh yourself and prepare for your "
                    "first deep look at Dadra and Nagar Haveli Sightseeing. We head directly to the famous Tribal "
                    "Cultural Museum, housing rare masks, hunting weapons, and musical instruments that narrate local "
                    "heritage. Next, take a peaceful stroll down the wooden pathways of Vanganga Lake Garden, an iconic "
                    "destination where manicured Japanese style bridges and pedal boating options create the ultimate "
                    "setting for photography and unforgettable memories."
                ),
                [
                    "Sightseeing Included: Tribal Cultural Museum, Vanganga Lake Garden",
                    "Evening Experience: Lakeside walk and organic tea tasting",
                    "Overnight Stay: Silvassa Luxury Riverfront Resort",
                    "Meals Included: Curated Buffet Dinner",
                ],
            ),
            _day(
                2,
                "Wildlife Exploration & Farewell Adieu",
                (
                    "Awake to the beautiful sounds of chirping birds and misty forest air. Indulge in a premium, lavish "
                    "breakfast spread at the resort's open-air café. After checking out, embark on your Premium Dadra and "
                    "Nagar Haveli Experience to explore the wilder side of Silvassa. We take you to the Lion Safari "
                    "Wildlife Park in Vasona, where a secured safari vehicle lets you spot the majestic Asiatic Lions "
                    "roaming safely within their sprawling natural habitat. Conclude your morning with an artistic stop "
                    "at Nakshatra Garden, a meticulously designed astronomical garden packed with medicinal trees and "
                    "stunning flower beds. Following a delightful local lunch at a premium restaurant recommended by "
                    "TRAGUIN experts, begin your comfortable return drive to your departure hub (Vapi or Surat) with "
                    "your mind thoroughly recharged."
                ),
                [
                    "Sightseeing Included: Vasona Lion Safari, Nakshatra Garden",
                    "Photography Points: Lion tracking and exotic medicinal floral arrays",
                    "Overnight Stay: Tour Concludes",
                    "Meals Included: Gourmet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel("Treat Resort Silvassa or similar", "Silvassa", "01 Night", "Deluxe", "Superior Room", "Breakfast & Dinner", 4, 1),
            _hotel("Pluz Resort Silvassa", "Silvassa", "01 Night", "Premium", "Deluxe Pool View Room", "Breakfast & Dinner", 5, 2),
            _hotel("Ras Resorts Silvassa", "Silvassa", "01 Night", "Luxury", "Executive Riverview Suite", "Breakfast & Dinner", 5, 3),
            _hotel(
                "TRAGUIN Handpicked Boutique Nature Luxury Villa",
                "Silvassa",
                "01 Night",
                "Ultra Luxury",
                "Private Pool Signature Villa",
                "All Inclusive Gourmet",
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included("01 Night premium luxury stay at selected property in Silvassa", 1),
            _inc_included("Lavish buffet breakfast and customized dinner curated by resort chefs", 2),
            _inc_included("Private high-end air-conditioned vehicle for all transfers and tours", 3),
            _inc_included("Pre-arranged entry permits and tickets to all mentioned state attractions", 4),
            _inc_included("Dedicated destination support from TRAGUIN customer care network", 5),
            _inc_included("Complimentary welcome non-alcoholic drinks on arrival", 6),
            _inc_excluded("Flights or long-distance train tickets to entry station", 7),
            _inc_excluded("Any personal item spending, tips, laundry, and minibar usage", 8),
            _inc_excluded("Boating activity tickets or camera fees inside parks", 9),
            _inc_excluded("Anything not explicitly detailed in the inclusions list", 10),
        ],
    )
    return package, itinerary


def build_dn_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DN-007"
    tour_code = "TG-DN-007-LUX"
    title = "Khanvel Scenic Green Retreat"
    duration = "02 Nights / 03 Days"
    slug = "dn-007-khanvel-scenic-green-retreat"
    itin_slug = "dn-007-khanvel-scenic-green-retreat-itinerary"
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
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Dadra and Nagar Haveli / India | Category: Leisure Green Retreat", 2),
            _ph("Destinations: Khanvel • Silvassa • Vasona • Dudhni", 3),
            _ph("Ideal for: Families, Couples & Nature Enthusiasts", 4),
            _ph("Best season: November to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Luxury Getaway (FIT)", 7),
            _ph("Vehicle: Premium, ultra-comfortable Air-Conditioned SUV (Innova Crysta)", 8),
            _ph("Meal Plan: Modified American Plan (Buffet Breakfast & Lavish Dinners Included)", 9),
            _ph("Route Map: Vapi/Surat Arrival → Silvassa Sightseeing → Khanvel Green Retreat → Dudhni Lake → Departure", 10),
            _ph("TRAGUIN Signature Experience: Private speed-boating at Dudhni and exclusive Lion Safari viewing decks", 11),
            _ph("Shopping: Warli Art Souvenirs, Local Toddy & Organic Honey, Silvassa Pipria Markets", 12),
            _ph("Important: Check-in 13:00 hrs, check-out 10:00 hrs; Vasona Lion Safari closed on Mondays", 13),
        ],
        moods=["Nature", "Luxury", "Leisure"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Class)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Khanvel Scenic Green Retreat & Silvassa Escape",
        overview=(
            "Escape into an oasis of lush woodlands, rolling meadows, and pristine waterscapes. This exclusive "
            "weekend getaway, meticulously crafted by TRAGUIN travel specialists, offers a high-end luxury retreat "
            "to Khanvel and Silvassa. Unwind amid breathtaking landscapes, indulge in premium stays nestled within "
            "verdant forests, and gather unforgettable memories.\n\n"
            "The Best Dadra and Nagar Haveli Tour Package is carefully organized for those seeking a stylish, "
            "refreshing break away from bustling city life. Managed with flawless attention to detail by TRAGUIN "
            "experts, this tour combines exquisite leisure with curated local insights.\n\n"
            "TRAGUIN Curated Touch: Handpicked resort cottages, private boat chartering at Dudhni, and custom-timed "
            "sunset highlights.\n\n"
            "Why Visit Dadra and Nagar Haveli: A perfect blend of sprawling forest reserves, Portuguese architecture, "
            "cascading lakes, and a relaxing tropical climate. Famous Attractions: Khanvel Forest Lodge, Vasona Lion "
            "Safari, Dudhni Jet Jetty, Swaminarayan Temple, and Nakshatra Garden. Most Searched Experiences: Premium "
            "wildlife spotting, private speed-boating across Madhuban Dam waters, and exploring authentic Warli tribal "
            "art. Best Time to Visit Dadra and Nagar Haveli: Winter months from November to March provide optimal "
            "weather, boasting refreshing breezes and beautifully lush, green post-monsoon foliage."
        ),
        seo_title="DN-007 | Khanvel Scenic Green Retreat | TRAGUIN",
        seo_description=(
            "Premium 02 Nights / 03 Days Khanvel retreat package (DN-007 / TG-DN-007-LUX): Swaminarayan Temple, "
            "Nakshatra Garden, Vasona Lion Safari, Dudhni Waterfront, Tribal Cultural Museum, and 4-tier hotels."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Silvassa Swaminarayan Temple & Nakshatra Garden", 1),
            _ih("Vasona Lion Safari & Dudhni Waterfront with private speed-boat", 2),
            _ih("Tribal Cultural Museum & Local Craft Center", 3),
            _ih("TRAGUIN Signature Experience: Private speed-boating at Dudhni and exclusive Lion Safari viewing decks", 4),
            _ih("Curated by TRAGUIN Experts: Handpicked luxury stays emphasizing peaceful green surroundings", 5),
            _ih("Luxury Transportation: Highly sanitized premium vehicles with experienced local drivers", 6),
        ],
        days=[
            _day(
                1,
                "Arrival & Silvassa Impressions to Khanvel Retreat",
                (
                    "Your luxury weekend begins with a private pickup from Vapi Railway Station or Surat Airport by our "
                    "professional chauffeur. Step into your premium vehicle and enjoy a smooth transfer into the green "
                    "territories of Silvassa. Our first stop is the beautiful, intricately carved Swaminarayan Temple, "
                    "followed by a relaxed walk through the lush Nakshatra Garden, filled with medicinal plants and artistic "
                    "fountains. Afterward, take a scenic drive into Khanvel, a tranquil paradise surrounded by dense forests. "
                    "Check into your ultra-luxury nature resort. As evening sets in, enjoy the premium amenities, relax by "
                    "the pool, or enjoy a tranquil nature walk inside the property to collect unforgettable memories under "
                    "a starry sky."
                ),
                [
                    "Sightseeing Included: Silvassa Swaminarayan Temple, Nakshatra Garden",
                    "Evening Experience: Leisure time at resort, poolside fine dining",
                    "Overnight Stay: Khanvel (Luxury Nature Resort Stay)",
                    "Meals Included: Welcome Dinner",
                ],
            ),
            _day(
                2,
                "Vasona Lion Safari & Private Dudhni Lake Excursion",
                (
                    "Start your day with a delicious breakfast looking out over the misty canopy of Khanvel. Today, we "
                    "experience the top wildlife attraction of the territory—the Vasona Lion Safari. Board a secured luxury "
                    "safari vehicle to see the majestic Asiatic lions roaming in their natural forest habitat. Next, we head "
                    "further down to Dudhni, often called the 'Kashmir of the West' due to its vast, scenic waterfront "
                    "created by the Madhuban Dam. TRAGUIN has curated an exclusive speed-boat experience across the vast "
                    "lake, surrounded by rolling hills. Capture incredible photographs from the water before returning to "
                    "Khanvel to relax. Treat yourself to a premium spa session or a cozy evening bonfire curated especially "
                    "for you."
                ),
                [
                    "Sightseeing Included: Vasona Lion Safari, Dudhni Waterfront, Madhuban Dam backwaters",
                    "Exclusive Experiences: Private chartered speed-boat ride at Dudhni Jetty",
                    "Overnight Stay: Khanvel",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                3,
                "Tribal Heritage Tour & Smooth Departure",
                (
                    "After a relaxing breakfast, check out of your luxury resort. Before concluding your tour, we visit the "
                    "Silvassa Tribal Cultural Museum, which showcases a unique collection of traditional masks, musical "
                    "instruments, hunting tools, and iconic Warli paintings. This provides a great cultural highlight to your "
                    "trip. Spend some time picking up local handicrafts as souvenirs. Finally, your chauffeur will provide a "
                    "smooth transfer back to Vapi or Surat for your onward journey, marking the completion of your premium "
                    "curated vacation."
                ),
                [
                    "Sightseeing Included: Tribal Cultural Museum, Local Craft Center",
                    "Photography Points: Traditional Warli artwork walls",
                    "Overnight Stay: Tour Concludes",
                    "Meals Included: Gourmet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel("Khanvel Resort / Pluz Resort", "Khanvel", "02 Nights", "Deluxe", "Deluxe Pool View Room", "Breakfast & Dinner", 4, 1),
            _hotel("Treat Resort, Silvassa / Khanvel", "Silvassa / Khanvel", "02 Nights", "Premium", "Premium Executive Room", "Breakfast & Dinner", 5, 2),
            _hotel("Ras Resorts, Silvassa (Lakeside)", "Silvassa", "02 Nights", "Luxury", "Luxury Portuguese Suite", "Breakfast & Dinner", 5, 3),
            _hotel("TRAGUIN Signature Forest Cottages & Luxury Villas", "Khanvel", "02 Nights", "Ultra Luxury", "Private Pool Premium Villa", "All Inclusive Gourmet", 5, 4),
        ],
        inclusions=[
            _inc_included("02 Nights luxury stay in our handpicked premium hotels and resorts", 1),
            _inc_included("Daily spread of gourmet breakfast and customized multi-cuisine buffet dinners", 2),
            _inc_included("Private transfers and sightseeing via premium Innova Crysta SUV", 3),
            _inc_included("All entry tickets, Vasona Lion Safari passes, and exclusive boat hire fees", 4),
            _inc_included("Professional chauffeur allowance, toll charges, state taxes, and fuel costs", 5),
            _inc_included("Welcome amenities, fresh fruit platter, and complimentary refreshments inside the vehicle", 6),
            _inc_included("24/7 dedicated TRAGUIN on-trip guest assistance and coordination support", 7),
            _inc_excluded("Train or flight bookings to Vapi, Valsad, or Surat", 8),
            _inc_excluded("Personal items like laundry, liquor, calls, or tips", 9),
            _inc_excluded("Water-sports or optional adventure activities at Dudhni Dam", 10),
            _inc_excluded("Any personal medical insurance coverage", 11),
        ],
    )
    return package, itinerary

def build_dn_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DN-008"
    tour_code = "TG-DN-008-PREM"
    title = "Silvassa Tribal Museum & Heritage Trail"
    duration = "02 Nights / 03 Days"
    slug = "dn-008-silvassa-tribal-museum-heritage-trail"
    itin_slug = "dn-008-silvassa-tribal-museum-heritage-trail-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration, price=0,
        rating=Decimal("4.9"), is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ph("Serial code DN-008 | TRAGUIN tour code TG-DN-008-PREM", 1),
            _ph("State / Country: Dadra and Nagar Haveli / India | Category: Culture & Heritage Trail", 2),
            _ph("Destinations: Silvassa • Khanvel • Dudhani", 3),
            _ph("Ideal for: Culture Enthusiasts & Families", 4),
            _ph("Best season: November to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Tailored FIT Escapes", 7),
            _ph("Vehicle: Premium, luxury segment Sedan / SUV", 8),
            _ph("Meal Plan: Modified American Plan (Breakfast & Gourmet Dinner Included)", 9),
            _ph("Route Map: Vapi / Surat Arrival → Silvassa Heritage Core → Khanvel & Dudhani Waterfront → Departure", 10),
            _ph("TRAGUIN Signature Experience: Private entry and custom workshops with award-winning local artists to discover genuine tribal roots", 11),
            _ph("Shopping: Warli Paintings, Tribal Bamboo Crafts, Local Toddy Pots & Souvenirs", 12),
            _ph("Important: Check-in 13:00 hrs, check-out 10:00 hrs; secure bookings 45 days in advance for holiday weekends", 13),
        ], moods=["Cultural", "Heritage", "Leisure"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title, duration_label=duration,
        duration_days=_duration_days(duration), starting_price=0,
        price_note="On Request (Premium Class)", rating=Decimal("4.9"), review_count=0,
        tagline="Silvassa Tribal Museum & Heritage Trail", overview=(
            "Discover the hidden heart of tribal legacy and Portuguese colonial history in the pristine landscapes of Dadra and Nagar Haveli. This premium heritage holiday, curated by TRAGUIN travel connoisseurs, invites you to witness a brilliant blend of ancient Warli art forms, timeless folklore, and lush green woodlands.\n\nImmerse yourself in a luxurious long weekend getaway with this specialized Dadra and Nagar Haveli Family Tour. Designed meticulously by TRAGUIN experts, this itinerary seamlessly matches cultural insights with deeply relaxing leisure elements.\n\nTRAGUIN Curated Note: Includes private interactions with traditional Warli tribal painters, reserved premium seating during local folk presentations, and curated authentic culinary tasting sessions.\n\nWhy Visit Dadra and Nagar Haveli: A remarkable crossroads of century-old Portuguese architecture, dynamic tribal societies (Kokna, Warli, and Dhodia), and exceptional wildlife reserves. Famous Attractions: Silvassa Tribal Museum, Vanganga Lake Garden, Swaminarayan Temple, and Dudhani Jet Jetty."
        ),
        seo_title="DN-008 | Silvassa Tribal Museum & Heritage Trail | TRAGUIN",
        seo_description=("Premium 02 Nights / 03 Days Dadra and Nagar Haveli package (DN-008 / TG-DN-008-PREM): Portuguese Church, Tribal Museum, Warli workshop, Swaminarayan Temple, Dudhni Waterfront"),
        is_featured=False, featured_sort_order=None, is_published=False, highlights=[
            _ih("Portuguese Church of Our Lady of Piety & Vanganga Lake Garden", 1),
            _ih("Silvassa Tribal Museum & Swaminarayan Temple with Warli workshop", 2),
            _ih("Dudhni Waterfront & Madhuban Dam Panoramic Point", 3),
            _ih("TRAGUIN Signature Experience: Private entry and custom workshops with award-winning local artists", 4),
            _ih("Curated by TRAGUIN Experts: Smoothly paced heritage walk schedules optimized for families", 5),
            _ih("Personalized Assistance: Dedicated destination managers monitoring your journey", 6),
        ], days=[
            _day(1, "Arrival in Silvassa & Colonial Heritage Trails", ("Your exceptional Premium Dadra and Nagar Haveli Experience starts with a smooth private pickup from Vapi railway station or Surat/Mumbai airport. Sit back inside your luxury transport as you are driven into Silvassa, the capital town known for its relaxed aura and deep history. Check into your handpicked premium resort property. Following lunch and time to unwind, your heritage guide will lead you to the historic Church of Our Lady of Piety, an elegantly preserved Portuguese-era church boasting striking stone architecture. As the sun begins to set, stroll through the paths of the Vanganga Lake Garden, a beautiful photography spot filled with Japanese-style bridges, fountains, and vibrant flower beds, establishing unforgettable memories for your opening day."), [
                "Sightseeing Included: Portuguese Church of Our Lady of Piety, Vanganga Lake Garden",
                "Evening Experience: Musical fountain presentation and pedal boat cruise",
                "Overnight Stay: Silvassa Luxury Riverside Resort",
                "Meals Included: Welcome Dinner",
            ]),
            _day(2, "Tribal Museum Chronicles & Warli Art Immersion", ("Dedicate your morning to discovering the indigenous souls of the region. After breakfast, visit the renowned Silvassa Tribal Museum, one of the primary Top Tourist Places in Dadra and Nagar Haveli. Here, marvel at a majestic collection of tribal ornaments, traditional hunting tools, musical instruments, and life-sized clay models reflecting centuries-old rural life. Following this, TRAGUIN brings you an absolute exclusive experience: a private, hands-on workshop led by a master Warli artist. Discover how simple geometric shapes combine to tell complex life stories on canvas. In the afternoon, take a scenic drive to the spectacular Swaminarayan Temple, famous for its intricate pink-stone carvings and deeply peaceful, manicured grounds."), [
                "Sightseeing Included: Silvassa Tribal Museum, Swaminarayan Temple Complex",
                "Exclusive Masterclass: Private Warli Painting workshop with custom souvenirs",
                "Overnight Stay: Silvassa",
                "Meals Included: Breakfast & Gourmet Dinner",
            ]),
            _day(3, "Scenic Dudhni Waterfront Escape & Farewell", ("On your final morning, enjoy a relaxing drive towards the breathtaking landscapes of Dudhni, often hailed as the Kashmir of the West. This spectacular waterfront area is formed by the waters of the Madhuban Dam. We embark on a premium private speed-boat cruise, allowing you to witness the scenic beauty of the vast reservoir surrounded by misty forest ranges. Following this refreshing waterfront escape, return to your resort for check-out. Your chauffeur will ensure a comfortable transfer back to your departure station, bringing an unforgettable close to your expertly curated Heritage Escape."), [
                "Sightseeing Included: Dudhni Waterfront, Madhuban Dam Panoramic Point",
                "Optional Activities: Kayaking or traditional wooden boat ride",
                "Overnight Stay: Tour Concludes",
                "Meals Included: Rich Buffet Breakfast",
            ]),
        ], hotels=[
            _hotel("Treat Resort, Silvassa or similar", "Silvassa", "02 Nights", "Deluxe", "Superior Garden View Room", "Breakfast & Dinner", 4, 1),
            _hotel("Khanvel Resort, Silvassa", "Silvassa", "02 Nights", "Premium", "Deluxe Poolside Room", "Breakfast & Dinner", 5, 2),
            _hotel("Ras Resorts Silvassa", "Silvassa", "02 Nights", "Luxury", "Executive Riverside Suite", "Breakfast & Dinner", 5, 3),
            _hotel("TRAGUIN Private Signature Villas", "Silvassa", "02 Nights", "Ultra Luxury", "Elite Presidential Pool Villa", "All-Inclusive Curated", 5, 4),
        ], inclusions=[
            _inc_included("02 Nights accommodation in premier, handpicked luxury resorts", 1),
            _inc_included("Daily premium buffet breakfasts and tailored dinners at the resort", 2),
            _inc_included("All transfers & city excursions in a private, dedicated luxury vehicle", 3),
            _inc_included("Entry tickets to the Silvassa Tribal Museum, gardens, and monuments", 4),
            _inc_included("Exclusive Warli painting workshop with local tribal experts", 5),
            _inc_included("Private speed-boat or luxury pontoon cruise at Dudhni Waterfront", 6),
            _inc_included("Constant 24/7 on-ground TRAGUIN support & dedicated driver allowances", 7),
            _inc_excluded("Train tickets / flights to entry hubs (Vapi, Surat, Mumbai)", 8),
            _inc_excluded("Personal expenses such as room service, laundry, or premium beverages", 9),
            _inc_excluded("Optional adventure watersports at Dudhani Jetty", 10),
            _inc_excluded("Mandatory travel insurance plans", 11),
            _inc_excluded("Any tips or gratuities for local guides and drivers", 12),
        ],
    )
    return package, itinerary

def build_dn_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DN-009"
    tour_code = "TG-DN-009-WEL"
    title = "Silvassa Wellness & Spa"
    duration = "02 Nights / 03 Days"
    slug = "dn-009-silvassa-wellness-spa"
    itin_slug = "dn-009-silvassa-wellness-spa-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration, price=0,
        rating=Decimal("4.9"), is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ph("Serial code DN-009 | TRAGUIN tour code TG-DN-009-WEL", 1),
            _ph("State / Country: Dadra and Nagar Haveli / India | Category: Luxury Wellness & Spa", 2),
            _ph("Destinations: Silvassa • Khanvel • Dudhni", 3),
            _ph("Ideal for: Couples, Corporate Retreats & Families", 4),
            _ph("Best season: November to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Luxury FIT Itinerary with On-Demand Concierge Services", 7),
            _ph("Vehicle: Premium, ultra-comfortable Luxury Sedan or SUV (with professional chauffeur)", 8),
            _ph("Meal Plan: Modified American Plan (Gourmet Breakfast & Curated Wellness Dinner Included)", 9),
            _ph("Route Map: Vapi/Surat Arrival → Silvassa Wellness Resort → Vanganga Garden → Dudhni Lake → Departure", 10),
            _ph("TRAGUIN Signature Experience: A private sunset cruise on Dudhni Lake combined with customized wellness menus curated by in-house nutritionists", 11),
            _ph("Shopping: Warli Paintings, Handcrafted Bamboo Wares, Organic Local Honey & Herbs", 12),
            _ph("Important: Check-in 14:00 hrs, check-out 11:00 hrs; book spa resorts 45 days in advance", 13),
        ], moods=["Wellness", "Luxury", "Leisure"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title, duration_label=duration,
        duration_days=_duration_days(duration), starting_price=0,
        price_note="On Request (Premium Class)", rating=Decimal("4.9"), review_count=0,
        tagline="Silvassa Wellness & Spa Retreat • Vanganga Lake • Dudhni Waterfront • Khanvel", overview=(
            "Escape the frantic pace of daily life and enter a sanctuary of absolute calm in the hidden green paradise of Western India. This bespoke itinerary, beautifully orchestrated by TRAGUIN travel specialists, offers a refined blend of world-class spa rejuvenation, high-end hospitality, and gentle exploration of Portuguese heritage footprints.\n\nThis exclusive Silvassa Premium Wellness & Spa Tour Package is carefully structured for travelers seeking full mind-body rejuvenation without sacrificing top-tier luxury.\n\nTRAGUIN Curated Touch: A complimentary 60-minute signature Swedish or Ayurvedic massage per guest, priority spa suite reservations, and healthy herbal welcome amenities.\n\nWhy Visit Silvassa: Celebrated for its expansive forest canopies, historical churches, pristine waterfronts, and close proximity to major corporate hubs like Mumbai and Surat."
        ),
        seo_title="DN-009 | Silvassa Wellness & Spa | TRAGUIN",
        seo_description=("Premium 02 Nights / 03 Days Dadra and Nagar Haveli package (DN-009 / TG-DN-009-WEL): Tribal Museum, Vanganga Lake, Dudhni sunset cruise, spa treatment, Our Lady of Piety Church"),
        is_featured=False, featured_sort_order=None, is_published=False, highlights=[
            _ih("Tribal Cultural Museum & Resort Wellness Estate", 1),
            _ih("Vanganga Lake Garden & Dudhni Waterfront with private speed-boat cruise", 2),
            _ih("Our Lady of Piety Church en-route departure", 3),
            _ih("TRAGUIN Signature Experience: Private sunset cruise on Dudhni Lake with customized wellness menus", 4),
            _ih("Curated by TRAGUIN Experts: Expertly spaced itinerary maximizing time in award-winning spa zones", 5),
            _ih("Personalized Assistance: Dedicated 24/7 travel concierge connection", 6),
        ], days=[
            _day(1, "Arrival in Silvassa & Immersive Spa Indulgence", ("Your luxury escape begins as our professional private chauffeur greets you warmly at Vapi Railway Station or Surat Airport. Lean back and enjoy a smooth, highly scenic drive through winding country roads as you arrive at Silvassa. Step past the threshold of your handpicked ultra-luxury resort and enjoy a refreshing tribal herbal welcome drink. After an effortless check-in, unpack and relax in your sprawling premium villa or suite. In the afternoon, visit the Tribal Cultural Museum for a brief, fascinating journey into native history and local lifestyles. Later, surrender to relaxation at the resort's premium spa, where a pre-booked 60-minute signature aromatherapy treatment awaits you to release any residual travel tension, carving out unforgettable memories from day one."), [
                "Sightseeing Included: Tribal Cultural Museum, Resort Wellness Estate",
                "Evening Experience: Complimentary TRAGUIN Signature Spa Treatment",
                "Overnight Stay: Silvassa (Ultra-Luxury Wellness Resort)",
                "Meals Included: Specially Crafted Wellness Dinner",
            ]),
            _day(2, "Scenic Vanganga Lake & Waterfront Cruise at Dudhni", ("Wake up to the sounds of nature and participate in an optional, gentle morning yoga and meditation session led by a certified yoga master on the resort's manicured lawns. Following a sumptuous organic breakfast, we set out to explore the scenic beauty of Vanganga Lake Island Garden, a beautiful Japanese-style park featuring cute wooden bridges, thatched huts, and easily accessible paddle boat pathways. After lunch, we take a smooth drive out to the majestic Dudhni Waterfront, a massive expanse of water formed by the Madhuban Dam. Here, TRAGUIN has curated an exclusive experience: a private, luxury speed-boat cruise across the deep blue waters as the sun begins to dip beneath the horizon. This provides spectacular photography options and a truly magical sunset view."), [
                "Sightseeing Included: Vanganga Lake Garden, Dudhni Waterfront Viewpoint",
                "Exclusive Experience: Private Luxury Speed-Boat Cruise at Sunset",
                "Overnight Stay: Silvassa",
                "Meals Included: Premium Breakfast & Candlelight Lakeside Dinner",
            ]),
            _day(3, "Retreat Closure & Seamless Departure", ("Greet your final morning with a refreshing swim in the resort's infinity pool or enjoy an artisan foot-reflexology path. Indulge in an exquisite, healthy gourmet breakfast spread highlighting locally sourced organic produce. Take some time to stroll around the resort grounds for final photographs or pick up some local handicrafts before checking out. Your private chauffeur will expertly manage your luggage and provide a highly comfortable transfer back to Vapi or Surat for your journey home. You will depart with a deeply rejuvenated spirit, revitalized physical energy, and exceptional stories from your bespoke Premium Silvassa Experience."), [
                "Sightseeing Included: Our Lady of Piety Church (En-route)",
                "Assistance: Full luggage handling & railway/airport transfer",
                "Overnight Stay: Vacation Concludes",
                "Meals Included: Floating Breakfast / Luxury Morning Buffet",
            ]),
        ], hotels=[
            _hotel("Treat Resort, Silvassa or similar", "Silvassa", "02 Nights", "Deluxe", "Superior Executive Room", "Breakfast & Dinner", 4, 1),
            _hotel("Ras Resorts, Silvassa", "Silvassa", "02 Nights", "Premium", "Premium Riverview Room", "Breakfast & Dinner", 5, 2),
            _hotel("Pluz Resort / Khanvel Resort", "Silvassa", "02 Nights", "Luxury", "Luxury Heritage Villa Suite", "Breakfast & Dinner", 5, 3),
            _hotel("TRAGUIN Handpicked Boutique Wellness Sanctuary", "Silvassa", "02 Nights", "Ultra Luxury", "Private Plunge Pool Garden Villa", "All Inclusive Premium Plan", 5, 4),
        ], inclusions=[
            _inc_included("02 Nights premium stay at pre-vetted luxury wellness resorts", 1),
            _inc_included("Curated organic breakfasts and specialty multi-cuisine dinners", 2),
            _inc_included("Dedicated premium air-conditioned luxury sedan or SUV throughout", 3),
            _inc_included("1 Complimentary 60-Minute Signature Massage session per adult", 4),
            _inc_included("Private luxury speed-boat cruise tickets at Dudhni Waterfront", 5),
            _inc_included("Unlimited access to resort wellness facilities (steam, sauna, gym, pools)", 6),
            _inc_included("Complete on-ground assistance and professional TRAGUIN support", 7),
            _inc_included("All toll fees, driver allowances, state permits, and fuel taxes", 8),
            _inc_excluded("Flights or train tickets to and from arrival stations", 9),
            _inc_excluded("Any personal expenditures like laundry, mini-bar, and long-distance calls", 10),
            _inc_excluded("Additional salon or wellness therapies outside the inclusion offer", 11),
            _inc_excluded("Professional camera or drone videography permissions", 12),
            _inc_excluded("Individual personal medical and vacation cancellation insurance", 13),
        ],
    )
    return package, itinerary

def build_dn_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DN-010"
    tour_code = "TG-DN-010-HON"
    title = "Honeymoon"
    duration = "03 Nights / 04 Days"
    slug = "dn-010-honeymoon"
    itin_slug = "dn-010-honeymoon-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration, price=0,
        rating=Decimal("4.9"), is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ph("Serial code DN-010 | TRAGUIN tour code TG-DN-010-HON", 1),
            _ph("State / Country: Dadra and Nagar Haveli / India | Category: Honeymoon Package", 2),
            _ph("Destinations: Silvassa • Khanvel • Dudhni Lake", 3),
            _ph("Ideal for: Couples & Honeymooners", 4),
            _ph("Best season: November to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Honeymoon FIT Tour with Dedicated On-Call Concierge", 7),
            _ph("Vehicle: Premium Luxury Sedan (Chauffeur driven with privacy partitions)", 8),
            _ph("Meal Plan: Modified American Plan (Gourmet Breakfast & Intimate Dinners Included)", 9),
            _ph("Route Map: Vapi / Surat Arrival → Silvassa Riverside → Khanvel → Dudhni Lake → Departure", 10),
            _ph("TRAGUIN Signature Experience: Private canopy candlelight dining setup with a customized cake and acoustic music recommendations", 11),
            _ph("Shopping: Warli Paintings, Handcrafted Bamboo Items, Local Toddy & Local Delicacies", 12),
            _ph("Important: Check-in 13:00 hrs; book premium luxury cottages 30-45 days prior", 13),
        ], moods=["Honeymoon", "Romance", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title, duration_label=duration,
        duration_days=_duration_days(duration), starting_price=0,
        price_note="On Request (Premium Class)", rating=Decimal("4.9"), review_count=0,
        tagline="Romantic Riverside Cottage Stay • Silvassa • Dudhni Lake", overview=(
            "Celebrate your union in a hidden sanctuary of love and natural bliss. Crafted exclusively by TRAGUIN travel architects, this romantic escape introduces newlyweds to the serene landscape of Dadra and Nagar Haveli. Unwind in luxury riverside cottages engulfed by lush green canopies, experience smooth boat cruises, and immerse yourselves in private candlelit dinners beside shimmering waters.\n\nThis custom-tailored Dadra and Nagar Haveli Honeymoon Package is built for couples looking for luxury, privacy, and serene relaxation.\n\nTRAGUIN Curated Touch: Complimentary cake, beautiful flower bed decoration, private riverside canopy seating, and handpicked romantic luxury properties.\n\nWhy Visit Dadra and Nagar Haveli: Beautiful, uncrowded forests, winding rivers, romantic weather, and luxurious wellness resorts."
        ),
        seo_title="DN-010 | Honeymoon | TRAGUIN",
        seo_description=("Premium 03 Nights / 04 Days Dadra and Nagar Haveli package (DN-010 / TG-DN-010-HON): Vanganga Lake, Tribal Museum, Dudhni boat cruise, Khanvel drive, Satmaliya Deer Park"),
        is_featured=False, featured_sort_order=None, is_published=False, highlights=[
            _ih("Vanganga Lake Garden Stroll & Private Riverside Candlelight Dinner", 1),
            _ih("Tribal Museum, Nakshatra Garden & Portuguese Church", 2),
            _ih("Dudhni Lake Waterfront Excursion with optional speedboat", 3),
            _ih("Khanvel Landscape Drive & Satmaliya Viewpoint", 4),
            _ih("TRAGUIN Signature Experience: Private canopy candlelight dining with customized cake", 5),
            _ih("Curated by TRAGUIN Experts: Seamlessly structured pacing for utmost privacy", 6),
        ], days=[
            _day(1, "Arrival in Silvassa & Romantic Riverside Check-In", ("Your enchanting journey begins as you arrive at Vapi Railway Station or Surat Airport, where a private luxury vehicle arranged by TRAGUIN awaits you. Take a smooth, comfortable drive to Silvassa, the capital of Dadra and Nagar Haveli. Check in to your ultra-luxury riverside cottage where a beautiful welcome amenity including sparkling juice and a complimentary cake awaits. Spend a relaxed afternoon inside your premium cottage overlooking the flowing waters of the Daman Ganga River. In the evening, visit the Vanganga Lake Garden, a stunning Japanese-style landscape adorned with wooden bridges and pristine water bodies—the perfect spot for your first honeymoon photography session. Return to the resort for an exclusive private candlelight dinner curated by TRAGUIN experts."), [
                "Sightseeing Included: Vanganga Lake Garden Stroll",
                "Evening Experience: Private Riverside Candlelight Dinner",
                "Overnight Stay: Silvassa (Premium Riverside Cottage)",
                "Meals Included: Welcome Honeymoon Dinner",
            ]),
            _day(2, "Silvassa Colonial & Heritage Discovery", ("Savor a delightful breakfast together before exploring the rich cultural heritage of Silvassa. We visit the famous Tribal Cultural Museum, which beautifully showcases the traditional lifestyle, masks, musical instruments, and authentic Warli paintings of the native tribes. Following this, take a lazy stroll through the Nakshatra Garden, a beautifully designed medicinal and astrological garden featuring pristine walkways and calming ponds. After a gourmet lunch at a local boutique cafe, visit the historic Church of Our Lady of Piety, standing as an elegant reminder of Portuguese architecture. The rest of the afternoon is yours to relax and enjoy the premium stays and swimming pools of your resort."), [
                "Sightseeing Included: Tribal Museum, Nakshatra Garden, Portuguese Church",
                "Photography Points: Vintage church exterior, Warli mural walls",
                "Overnight Stay: Silvassa",
                "Meals Included: Breakfast & Gourmet Dinner",
            ]),
            _day(3, "Dudhni Lake Boat Cruise & Sunset Magic", ("Today, after a late morning breakfast, embark on a scenic excursion to Dudhni Lake, often described as the 'Kashmir of the West'. Winding through breathtaking landscapes of green hills and tribal hamlets, you will reach the massive waterfront formed by the Madhuban Dam. TRAGUIN arranges an exclusive private speed boat ride across the lake, allowing you to experience the scenic beauty in complete privacy. For adventure-loving couples, optional jet-skiing and kayaking are available. Sit together by the waterfront as the sun dips below the horizon, painting the sky in deep shades of gold and amber. Return to your resort for a premium open-air dinner."), [
                "Sightseeing Included: Dudhni Lake Waterfront Excursion",
                "Optional Activities: Private Speedboat ride, Water sports",
                "Overnight Stay: Silvassa / Khanvel Resort",
                "Meals Included: Breakfast & Dinner",
            ]),
            _day(4, "Khanvel Forest Trails & Farewell Departure", ("Indulge in a final floating breakfast in your private pool (optional luxury add-on) or enjoy the widespread resort buffet. Check out and drive through the pristine forest landscapes of Khanvel. Visit the Satmaliya Deer Park for a short, peaceful glimpse of wildlife including blackbucks and chitals roaming freely in their natural habitat. Capture your last few honeymoon photographs amidst the towering trees. Afterward, your professional TRAGUIN chauffeur will transfer you back smoothly to Vapi Railway Station or Surat Airport for your journey home, concluding your premium Dadra and Nagar Haveli Experience."), [
                "Sightseeing Included: Khanvel Landscape Drive, Satmaliya Viewpoint",
                "Assistance: Complete luggage support up to your transit point",
                "Overnight Stay: Tour Concludes",
                "Meals Included: Gourmet Breakfast",
            ]),
        ], hotels=[
            _hotel("Ras Resorts Silvassa or similar", "Silvassa", "03 Nights", "Deluxe", "Standard Garden View Room", "Breakfast & Dinner", 4, 1),
            _hotel("Treat Resort, Silvassa / Khanvel", "Silvassa", "03 Nights", "Premium", "Executive Pool View Room", "Breakfast & Dinner", 5, 2),
            _hotel("Pluz Resort / Khanvel Forest Hideaway", "Silvassa", "03 Nights", "Luxury", "Luxury Riverside Villa / Cottage", "Breakfast & Dinner", 5, 3),
            _hotel("TRAGUIN Signature Partner Luxury Villas", "Silvassa", "03 Nights", "Ultra Luxury", "Presidential Pool Villa with Private Deck", "All Inclusive Premium", 5, 4),
        ], inclusions=[
            _inc_included("03 Nights luxury stay in premium handpicked waterfront cottages", 1),
            _inc_included("Daily lavish buffet breakfasts and curated romantic dinners", 2),
            _inc_included("Dedicated private luxury air-conditioned sedan throughout the trip", 3),
            _inc_included("Professional chauffeur with excellent local route knowledge", 4),
            _inc_included("Complimentary honeymoon cake and special room decoration elements", 5),
            _inc_included("1 Premium Private Candlelight Dinner setup by the riverbank", 6),
            _inc_included("All toll fees, parking, driver allowances, and regional taxes", 7),
            _inc_included("24/7 dedicated TRAGUIN on-ground guest assistance", 8),
            _inc_excluded("Flight or train ticket expenses to Vapi / Surat", 9),
            _inc_excluded("Individual entry tickets to gardens and museums", 10),
            _inc_excluded("Water sports charges or private speed boating at Dudhni Lake", 11),
            _inc_excluded("Personal expenses like laundry, alcoholic beverages, and tipping", 12),
            _inc_excluded("Anything not explicitly mentioned in the inclusions list", 13),
        ],
    )
    return package, itinerary

def build_dn_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DN-011"
    tour_code = "TG-DN-011-PREM"
    title = "Kauncha Tribal Village"
    duration = "03 Nights / 04 Days"
    slug = "dn-011-kauncha-tribal-village"
    itin_slug = "dn-011-kauncha-tribal-village-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration, price=0,
        rating=Decimal("4.9"), is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ph("Serial code DN-011 | TRAGUIN tour code TG-DN-011-PREM", 1),
            _ph("State / Country: Dadra and Nagar Haveli / India | Category: Offbeat Tribal Experience", 2),
            _ph("Destinations: Silvassa • Kauncha Village • Dudhni Lake", 3),
            _ph("Ideal for: Culture Enthusiasts & Nature Lovers", 4),
            _ph("Best season: November to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Independent Tour (FIT) / Luxury Cultural Escape", 7),
            _ph("Vehicle: Executive Air-Conditioned Sedan / SUV for all transfers and tours", 8),
            _ph("Meal Plan: Modified American Plan (Daily Premium Breakfast & Gourmet Dinner Included)", 9),
            _ph("Route Map: Vapi/Surat Arrival → Silvassa → Kauncha Village → Dudhni Lake → Departure", 10),
            _ph("TRAGUIN Signature Experience: An immersive tribal culinary journey with an organic lunch sourced and cooked directly by a Warli family", 11),
            _ph("Shopping: Original Warli Paintings, Handmade Bamboo Crafts, Silvassa Toddy & Local Wines", 12),
            _ph("Important: Check-in 14:00 hrs, check-out 11:00 hrs; Kauncha village visits require TRAGUIN advance reservations", 13),
        ], moods=["Cultural", "Tribal", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title, duration_label=duration,
        duration_days=_duration_days(duration), starting_price=0,
        price_note="On Request (Premium Class)", rating=Decimal("4.9"), review_count=0,
        tagline="Kauncha Tribal Village Experience • Silvassa • Dudhni Waterfront", overview=(
            "Escape into a world unchanged by time. Carefully curated by TRAGUIN destination experts, this immersive getaway invites you into the beating cultural heart of Dadra and Nagar Haveli. Journey beyond the tourist maps into Kauncha Tribal Village, a beautiful sanctuary of the Warli community.\n\nDiscover an unfiltered side of Western India on this luxury weekend escape. From the dense wood forests of Silvassa to the tranquil waterfront of Dudhni, every single day is tailored to deliver maximum comfort alongside deep immersive experiences.\n\nTRAGUIN Curated Touch: Private Warli painting masterclass and an exclusive evening tribal dance performance around a lakeside bonfire."
        ),
        seo_title="DN-011 | Kauncha Tribal Village | TRAGUIN",
        seo_description=("Premium 03 Nights / 04 Days Dadra and Nagar Haveli package (DN-011 / TG-DN-011-PREM): Tribal Museum, Kauncha village, Warli masterclass, Dudhni Shikara, Tarpa dance"),
        is_featured=False, featured_sort_order=None, is_published=False, highlights=[
            _ih("Tribal Cultural Museum & Vanganga Lake Garden", 1),
            _ih("Kauncha Heritage Walk & Private Warli Painting Class with tribal lunch", 2),
            _ih("Dudhni Water Sports Waterfront & Private Tarpa Dance Performance", 3),
            _ih("Church of Our Lady of Piety & Local Craft Emporium", 4),
            _ih("TRAGUIN Signature Experience: Immersive tribal culinary journey with organic Warli family lunch", 5),
            _ih("Curated by TRAGUIN Experts: Handpicked travel routes avoiding crowded roads", 6),
        ], days=[
            _day(1, "Arrival in Silvassa & Cultural Awakening", ("Your luxury journey begins as you arrive at Vapi or Surat station/airport, where a private TRAGUIN chauffeur greets you warmly. Enjoy a smooth drive into Silvassa, the capital of Dadra and Nagar Haveli, passing through lovely rural landscapes. Check in at your premium resort and take some time to refresh. In the afternoon, explore the Top Tourist Places in Dadra and Nagar Haveli, beginning with the fascinating Tribal Cultural Museum. Here, life-sized displays, musical instruments, and ancient hunting gear tell an emotional story of the region's indigenous clans. Later, enjoy a relaxing walk through the beautifully landscaped Vanganga Lake Garden, where Japanese-style bridges and peaceful boating streams create unforgettable memories."), [
                "Sightseeing Included: Tribal Cultural Museum, Vanganga Lake Garden",
                "Evening Experience: Lakeside stroll and welcome drinks at the resort",
                "Overnight Stay: Silvassa (Premium Resort)",
                "Meals Included: Welcome Buffet Dinner",
            ]),
            _day(2, "The Heart of Kauncha Village & Private Warli Masterclass", ("Awake to the crisp morning air and enjoy a delicious breakfast. Today, we venture deep into the wilderness to experience the authentic Kauncha Tribal Village Experience. Set against the expansive backdrop of the Madhuban Dam reservoir, Kauncha is a pristine village where the Warli tribe lives in harmony with nature. TRAGUIN guests will enjoy an exclusive, handpicked interaction with the village elders. Step into a traditional mud-and-bamboo house to witness a private masterclass in Warli painting led by a master artisan. Learn how simple geometric shapes create breathtaking representations of community life. Savor a traditional, freshly prepared local organic lunch inside the village before returning to your luxury resort for an evening of absolute leisure."), [
                "Sightseeing Included: Kauncha Heritage Walk, Warli Artisan Village",
                "Exclusive Experiences: Private Warli Painting Class, Traditional Village Lunch",
                "Overnight Stay: Silvassa / Dudhni Waterfront Resort",
                "Meals Included: Breakfast, Tribal Lunch, and Dinner",
            ]),
            _day(3, "Dudhni Lake Water Scenery & Ritualistic Tarpa Dance", ("Following breakfast, take a scenic drive to the majestic Dudhni Water Sports Complex, often called the 'Kashmir of the West'. The vast waterfront, created by the waters of the Madhuban Dam, offers stunning panoramic views of rolling green hills. Embark on a private luxury Shikara boat cruise across the pristine waters, curated exclusively by TRAGUIN. In the evening, gather around a cozy bonfire at the resort to witness the hypnotic Tarpa Dance. Watch as tribal dancers form a seamless circle, moving to the deep sounds of the wind instrument made from dried gourd, offering an immersive cultural experience that connects you deeply to the spirit of the land."), [
                "Sightseeing Included: Dudhni Water Sports Waterfront, Madhuban Viewpoint",
                "Evening Experience: Private Tarpa Dance Performance around a Bonfire",
                "Overnight Stay: Dudhni / Silvassa Luxury Resort",
                "Meals Included: Breakfast & Grand Farewell Dinner",
            ]),
            _day(4, "Portuguese Memories & Homeward Journey", ("On your final morning, indulge in a relaxed gourmet breakfast at the resort. Before concluding your family holiday, take a short drive to see the beautiful Church of Our Lady of Piety, a historic stone church built by the Portuguese in the late 19th century. Marvel at its exquisite altar and classic architecture. Afterward, your private chauffeur will assist with your luggage and provide a comfortable drive back to Vapi or Surat for your homeward journey, leaving you with a treasure trove of unforgettable memories from your specialized TRAGUIN holiday."), [
                "Sightseeing Included: Church of Our Lady of Piety, Local Craft Emporium",
                "Assistance: Luggage handling and smooth drop-off service",
                "Overnight Stay: Tour Concludes",
                "Meals Included: Deluxe Breakfast",
            ]),
        ], hotels=[
            _hotel("Ras Resorts Silvassa or similar", "Silvassa", "03 Nights", "Deluxe", "Garden View Room", "Breakfast & Dinner", 4, 1),
            _hotel("Treat Resort Silvassa", "Silvassa", "03 Nights", "Premium", "Superior Luxury Room", "Breakfast & Dinner", 5, 2),
            _hotel("Khanvel Resort / Pluz Resort", "Silvassa", "03 Nights", "Luxury", "Executive Suite", "Breakfast & Dinner", 5, 3),
            _hotel("TRAGUIN Exclusive Waterfront Eco-Resort", "Dudhni", "03 Nights", "Ultra Luxury", "Premium Lakeside Cottage", "All Inclusive Curated", 5, 4),
        ], inclusions=[
            _inc_included("03 Nights accommodation in premium, top-rated luxury hotels/resorts", 1),
            _inc_included("Daily buffet breakfast and custom gourmet multi-cuisine dinners", 2),
            _inc_included("Dedicated private executive sedan/SUV for all airport/station transfers & sightseeing", 3),
            _inc_included("Exclusive entry permits, activity charges, and private Shikara boat cruise at Dudhni", 4),
            _inc_included("Curated private Warli art masterclass with local village artisans", 5),
            _inc_included("Special private Tarpa tribal dance performance with bonfire setup", 6),
            _inc_included("24/7 on-tour customer support from dedicated TRAGUIN experts", 7),
            _inc_included("All toll taxes, fuel charges, parking fees, and driver allowances", 8),
            _inc_excluded("Airfare or main train tickets to the arrival gateway", 9),
            _inc_excluded("Personal items such as laundry, phone calls, or spa therapies", 10),
            _inc_excluded("Meals or drinks not specifically outlined in the daily schedule", 11),
            _inc_excluded("Speedboat or optional motorized high-speed water sports at Dudhni", 12),
            _inc_excluded("Tips, gratuities, and mandatory travel medical insurance", 13),
        ],
    )
    return package, itinerary

def build_dn_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DN-012"
    tour_code = "TG-DN-MICE-012"
    title = "Corporate MICE"
    duration = "02 Nights / 03 Days"
    slug = "dn-012-corporate-mice"
    itin_slug = "dn-012-corporate-mice-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration, price=0,
        rating=Decimal("4.9"), is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ph("Serial code DN-012 | TRAGUIN tour code TG-DN-MICE-012", 1),
            _ph("State / Country: Dadra and Nagar Haveli / India | Category: Corporate MICE & Retreat", 2),
            _ph("Destinations: Silvassa • Khanvel • Dudhni Lake", 3),
            _ph("Ideal for: Corporate Executives & Teams", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Corporate Team Retreat (FIT / Corporate Group)", 7),
            _ph("Vehicle: High-end luxury coaches and executive SUVs for airport/city transfers", 8),
            _ph("Meal Plan: All Inclusive Executive Corporate Plan (Premium Breakfast, Curated Lunches, and Gala Dinners)", 9),
            _ph("Route Map: Luxury Resort Check-in → Silvassa Business Forum → Dudhni Lake Waterfront Summit", 10),
            _ph("TRAGUIN Signature Experience: A designated strategic brainstorming layout on a private floating platform on Dudhni Lake", 11),
            _ph("Shopping: Warli tribal art team-building workshops, waterfront speedboating summits", 12),
            _ph("Important: Check-in 14:00 hrs; share final presentations and dietary preferences 10 days before arrival", 13),
        ], moods=["Corporate", "MICE", "Retreat"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title, duration_label=duration,
        duration_days=_duration_days(duration), starting_price=0,
        price_note="On Request (Premium Class)", rating=Decimal("4.9"), review_count=0,
        tagline="Silvassa Executive Corporate MICE & Luxury Retreat", overview=(
            "Welcome to a seamless blend of high-impact strategic alignment and tranquil rejuvenation. Carefully engineered by TRAGUIN Corporate Travel Experts, this signature Silvassa Executive Corporate MICE program is tailored for progressive corporate teams seeking a sophisticated escape.\n\nThis elite corporate proposal handles every structural element of a business retreat with perfection. Managed end-to-end by senior corporate consultants at TRAGUIN, your executives can step out of business routines and transition effortlessly into a curated environment designed to maximize professional bonding, strategic focus, and luxury relaxation.\n\nTRAGUIN Curated MICE Advantage: State-of-the-art audio-visual setups, private cocktail networking zones, customized corporate branding backdrops, and dedicated team-building facilitators."
        ),
        seo_title="DN-012 | Corporate MICE | TRAGUIN",
        seo_description=("Premium 02 Nights / 03 Days Dadra and Nagar Haveli package (DN-012 / TG-DN-MICE-012): Vanganga Lake, Dudhni waterfront forum, Warli team-building, Tribal Museum, Swaminarayan Temple"),
        is_featured=False, featured_sort_order=None, is_published=False, highlights=[
            _ih("Vanganga Lake Garden & Luxury Resort Grounds with AV-equipped Keynote forum", 1),
            _ih("Dudhni Lake Jet Skiing & Warli Art Challenge with themed Gala Dinner", 2),
            _ih("Tribal Museum Silvassa & Swaminarayan Temple", 3),
            _ih("TRAGUIN Signature Experience: Strategic brainstorming on private floating platform at Dudhni Lake", 4),
            _ih("Curated by TRAGUIN Experts: Seamless routing maximizing business outcomes and rejuvenation", 5),
            _ih("Personalized Assistance: Dedicated on-site MICE coordinator throughout the tour", 6),
        ], days=[
            _day(1, "Arrival in Silvassa & High-Impact Leadership Convening", ("Your executive delegation arrives in Silvassa, welcomed warmly by the specialized corporate reception team from TRAGUIN. Seamless check-in procedures are executed at your handpicked ultra-luxury resort, with premium welcome amenities pre-arranged in each executive suite. After a premium networking lunch at the poolside pavilion, the delegation gathers in the grand ballroom for the opening session of your Silvassa Corporate MICE Experience. State-of-the-art audio-visual layouts are deployed for your initial presentation and strategic alignment. As evening falls, enjoy a tranquil walking tour of the nearby Vanganga Lake Garden, exploring its scenic beauty and manicured Portuguese-style lawns—providing a perfect backdrop for casual executive interactions and unforgettable memories."), [
                "Sightseeing Included: Vanganga Lake Garden, Luxury Resort Grounds",
                "Corporate Session: Ice-breaker meeting & AV-equipped Keynote forum",
                "Overnight Stay: Silvassa (Premium Luxury Business Resort)",
                "Meals Included: Premium Networking Lunch & Executive Gala Dinner",
            ]),
            _day(2, "Strategic Waterfront Forum at Dudhni & Tribal Team-Building", ("The morning begins with an expansive breakfast buffet before expanding into our prime immersive experiences. The team transfers via premium luxury transport to the sparkling expanse of Dudhni Lake, often described as the 'Kashmir of the West'. Here, TRAGUIN orchestrates a unique 'Waterfront Strategy Session' aboard a private luxury house-boat/jetty. Following business deliberations, your team takes part in high-octane speed-boating activities across the vast waters. In the afternoon, return to the resort for a curated Warli Tribal Art Workshop—an exclusive experience where executives collaborate on massive canvases, fostering creative teamwork. The evening features an exquisite open-air themed Gala Dinner complete with premium entertainment and live interactive cooking stations."), [
                "Dadra and Nagar Haveli Sightseeing: Dudhni Lake Jet Skiing & Jet Boat Cruising",
                "Team Bonding: Collaborative Warli Art Challenge & Dynamic CSR Activity",
                "Overnight Stay: Silvassa Luxury Hub",
                "Meals Included: Breakfast, Lakeside Buffet Lunch & Themed Gala Night Dinner",
            ]),
            _day(3, "Cultural Ethos, Reflection & Executive Departure", ("Begin your final day with a refreshing yoga session on the resort's manicured lawns, overlooking pristine pool views. After an executive breakfast, check out and visit the fascinating Tribal Cultural Museum in Silvassa, which houses an iconic collection of indigenous artifacts, hunting tools, and traditional musical instruments. This visit serves as an intellectual anchor to understand the history of Dadra and Nagar Haveli. Conclude your tour with a short visit to the architectural marvel of the Swaminarayan Temple, featuring intricately carved pink stones. Following a final wrap-up lunch, your high-end corporate coach takes you back to your departure station, bringing to a successful end an unforgettable Premium Dadra and Nagar Haveli Experience curated to perfection by TRAGUIN."), [
                "Sightseeing Included: Tribal Museum Silvassa & Swaminarayan Temple",
                "Optional Activities: Procurement of local authentic Warli handicrafts",
                "Overnight Stay: Tour Concludes Successfully",
                "Meals Included: Buffet Breakfast & Executive Farewell Lunch",
            ]),
        ], hotels=[
            _hotel("Treat Resort, Silvassa or similar", "Silvassa", "02 Nights", "Deluxe", "Superior Executive Rooms", "Breakfast, Conference Lunch & Dinner", 4, 1),
            _hotel("Ras Resorts, Silvassa", "Silvassa", "02 Nights", "Premium", "Premium River-View Rooms", "Breakfast, Conference Lunch & Gala Dinner", 5, 2),
            _hotel("The Fern Seaside Luxurious Hub / Khanvel Resort", "Silvassa", "02 Nights", "Luxury", "Luxury Club Suites", "All Inclusive Premium Package", 5, 3),
            _hotel("TRAGUIN Exclusive Handpicked Corporate Villas", "Silvassa", "02 Nights", "Ultra Luxury", "Presidential Premium Villas", "Ultra Luxury Customized Menu Plan", 5, 4),
        ], inclusions=[
            _inc_included("02 Nights ultra-luxury accommodations at handpicked premium business resorts", 1),
            _inc_included("1 Full-Day Main Conference Hall usage with advanced acoustics & premium Wi-Fi", 2),
            _inc_included("2 Hi-Tea sessions daily during conferences with assorted gourmet platter options", 3),
            _inc_included("High-end luxury coaches for all group transit & executive airport connections", 4),
            _inc_included("Private motorboat cruise bookings and speed-boating experiences at Dudhni Lake", 5),
            _inc_included("Corporate gala setup with themed backdrops, audio sound structures & lighting arrays", 6),
            _inc_included("All entry permits, monument admissions, and local guiding fees", 7),
            _inc_included("Uncompromised, around-the-clock TRAGUIN Corporate Desk Support", 8),
            _inc_excluded("Flight, rail, or interstate transit expenses to the primary terminal", 9),
            _inc_excluded("Personal resort incidental charges (Mini-bar access, laundry services, spa)", 10),
            _inc_excluded("Hard liquor allocations for the Gala evening unless formally authorized", 11),
            _inc_excluded("Comprehensive medical coverage plans for individual attendees", 12),
            _inc_excluded("Additional technical setup rentals not detailed in the core inclusions", 13),
        ],
    )
    return package, itinerary

def build_dn_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DN-013"
    tour_code = "TG-DN-013-NAT"
    title = "Nakshatra Van Nature Escape"
    duration = "02 Nights / 03 Days"
    slug = "dn-013-nakshatra-van-nature-escape"
    itin_slug = "dn-013-nakshatra-van-nature-escape-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration, price=0,
        rating=Decimal("4.9"), is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ph("Serial code DN-013 | TRAGUIN tour code TG-DN-013-NAT", 1),
            _ph("State / Country: Dadra and Nagar Haveli / India | Category: Nature & Leisure Escape", 2),
            _ph("Destinations: Silvassa • Nakshatra Van • Hirwa Van", 3),
            _ph("Ideal for: Families, Couples, Nature Enthusiasts", 4),
            _ph("Best season: November to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Weekend FIT Tour (Fully Flexible)", 7),
            _ph("Vehicle: Premium, spacious air-conditioned sedan / SUV with seasoned chauffeur", 8),
            _ph("Meal Plan: Modified American Plan (Daily Premium Breakfast & Gourmet Dinner Included)", 9),
            _ph("Route Map: Arrival → Silvassa → Nakshatra Van → Hirwa Van → Vanganga Garden → Departure", 10),
            _ph("TRAGUIN Signature Experience: Private bonfire arrangement and live traditional music performance at the resort (subject to weather)", 11),
            _ph("Shopping: Warli Art Souvenirs, Local Toddy & Honey, Handmade Bamboo Crafts", 12),
            _ph("Important: Check-in 13:00 hrs, check-out 10:00 hrs; book 30 days in advance during peak weekends", 13),
        ], moods=["Nature", "Family", "Leisure"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title, duration_label=duration,
        duration_days=_duration_days(duration), starting_price=0,
        price_note="On Request (Premium Class)", rating=Decimal("4.9"), review_count=0,
        tagline="Nakshatra Van • Hirwa Van • Vanganga Lake • Silvassa Nature Escape", overview=(
            "Escape into the serene embrace of lush woodlands, blooming gardens, and historic Portuguese influences. Handcrafted perfectly by the travel designers at TRAGUIN, this ultimate luxury weekend getaway brings you closer to nature's tranquility in Silvassa.\n\nDiscover the hidden jewel of western India with our luxury Dadra and Nagar Haveli Family Tour. Designed as a high-end, smooth, and relaxing weekend retreat, this itinerary avoids rushed schedules and offers curated experiences that appeal to both relaxation seekers and nature lovers.\n\nTRAGUIN Curated Experience Note: Private guided nature walks, pre-arranged fast-track entrance tickets, and a dedicated local holiday expert always available on call."
        ),
        seo_title="DN-013 | Nakshatra Van Nature Escape | TRAGUIN",
        seo_description=("Premium 02 Nights / 03 Days Dadra and Nagar Haveli package (DN-013 / TG-DN-013-NAT): Nakshatra Van, Hirwa Van, Vanganga Lake boating, Tribal Cultural Museum"),
        is_featured=False, featured_sort_order=None, is_published=False, highlights=[
            _ih("Nakshatra Van Astro-Garden & Musical Fountains", 1),
            _ih("Hirwa Van Garden & Vanganga Lake Garden with private paddle boating", 2),
            _ih("Tribal Cultural Museum & Craft Center with Warli paintings", 3),
            _ih("TRAGUIN Signature Experience: Private bonfire and live traditional music at resort", 4),
            _ih("Curated by TRAGUIN Experts: Flexible timing templates at your preferred pace", 5),
            _ih("Exclusive Recommendations: Handpicked local food spots for regional rustic cuisine", 6),
        ], days=[
            _day(1, "Arrival in Silvassa & Astro-Botanical Exploration at Nakshatra Van", ("Your refreshing retreat starts with a premium private pickup from your preferred location (Surat / Mumbai / Vapi / Silvassa station) by a dedicated TRAGUIN representative. Enjoy a smooth drive along tree-lined highways into Silvassa. Upon arrival, check into your handpicked premium resort. After an exquisite lunch and some relaxation, your chauffeur will drive you to the spectacular Nakshatra Van. This highly searched astro-botanical garden is thoughtfully designed around Indian astrology, showcasing an expansive variety of medicinal plants, trees, and shrubs connected with zodiac signs and constellations. Stroll along well-maintained pathways, witness the musical fountains dancing to classic rhythms, and enjoy a premium family photography session organized amid stunning floral landscapes."), [
                "Sightseeing Included: Nakshatra Van Astro-Garden, Musical Fountains",
                "Evening Experience: Lakeside relaxation & welcome mocktails",
                "Overnight Stay: Silvassa Luxury Nature Resort",
                "Meals Included: Luxury Buffet Dinner",
            ]),
            _day(2, "Misty Refreshment at Hirwa Van Garden & Vanganga Lake Retreat", ("Awaken to the soothing sounds of birds and relish a luxurious breakfast spread at your resort. Today, we delve deeper into the top tourist places in Dadra and Nagar Haveli. First, explore Hirwa Van Garden, a beautifully curated man-made forest paradise. Be mesmerized by twin waterfalls cascading over rock formations, rustic wooden walkways, and a spectacular variety of vibrant flowers. TRAGUIN experts highly recommend this spot for peaceful morning meditation or romantic photography. In the afternoon, enjoy an immersive experience at Vanganga Lake Garden. This Japanese-style botanical garden features a sprawling lake, paddle-boating experiences, and quaint bridges over water bodies. It is widely known as a popular filming location. Spend a relaxed evening taking a private boat ride or enjoying tea along the lake."), [
                "Sightseeing Included: Hirwa Van Garden, Vanganga Lake Garden & Boating",
                "Optional Activities: Silvassa Tribal Museum to witness Warli Art",
                "Overnight Stay: Silvassa Luxury Nature Resort",
                "Meals Included: Gourmet Breakfast & Gala Dinner",
            ]),
            _day(3, "Tribal Heritage Appreciation & Farewell Transfers", ("Savor a lazy breakfast looking out over the resort's pool or garden. Check out and proceed for a short, exclusive visit to the Silvassa Tribal Cultural Museum. The museum showcases rare traditional hunting tools, hand-woven attire, musical instruments, and iconic Warli paintings that portray the regional lifestyle. It's the perfect opportunity to buy authentic souvenirs and gifts for family. Conclude your premium Dadra and Nagar Haveli experience as your chauffeur drives you comfortably back to your departure terminal (Vapi / Surat / Mumbai), leaving you with unforgettable memories from your TRAGUIN weekend escape."), [
                "Sightseeing Included: Tribal Cultural Museum & Craft Center",
                "Shopping Highlight: Buy authentic local handmade Warli paintings",
                "Overnight Stay: Tour Concludes",
                "Meals Included: Lavish Breakfast",
            ]),
        ], hotels=[
            _hotel("Pluz Resort or similar", "Silvassa", "02 Nights", "Deluxe", "Deluxe Garden View Room", "Breakfast & Dinner", 4, 1),
            _hotel("Treat Resort, Silvassa", "Silvassa", "02 Nights", "Premium", "Superior Pool-Facing Room", "Breakfast & Dinner", 5, 2),
            _hotel("Khanvel Resort or Ras Resorts", "Silvassa", "02 Nights", "Luxury", "Executive Premium Suite", "Breakfast & Dinner", 5, 3),
            _hotel("TRAGUIN Signature Partner Luxury Villas", "Silvassa", "02 Nights", "Ultra Luxury", "Private Pool Heritage Villa", "All Inclusive Premium", 5, 4),
        ], inclusions=[
            _inc_included("02 Nights luxury accommodation in premium handpicked hotels", 1),
            _inc_included("Daily multi-cuisine buffet breakfasts and premium dinners", 2),
            _inc_included("Private dedicated AC luxury vehicle for all transfers & sightseeing", 3),
            _inc_included("Pre-booked entrance tickets to Nakshatra Van, Hirwa Van, & Vanganga", 4),
            _inc_included("Private paddle boating experience at Vanganga Lake Garden", 5),
            _inc_included("Welcome non-alcoholic amenities & premium seasonal fruit basket on arrival", 6),
            _inc_included("Round-the-clock professional TRAGUIN customer support", 7),
            _inc_included("Inclusive of all toll charges, fuel costs, driver allowances, & service taxes", 8),
            _inc_excluded("Airfare, train tickets, or major transit terminal expenses", 9),
            _inc_excluded("Personal charges like laundry, liquor, calls, or room service orders", 10),
            _inc_excluded("Camera or professional video fees at tourist attractions", 11),
            _inc_excluded("Comprehensive travel or medical insurance", 12),
            _inc_excluded("Tips, gratuities, or expenses caused by unexpected natural road blockages", 13),
        ],
    )
    return package, itinerary

def build_dn_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DN-014"
    tour_code = "TG-DNH-014-PREM"
    title = "Grand Exploration"
    duration = "05 Nights / 06 Days"
    slug = "dn-014-grand-exploration"
    itin_slug = "dn-014-grand-exploration-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration, price=0,
        rating=Decimal("4.9"), is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ph("Serial code DN-014 | TRAGUIN tour code TG-DNH-014-PREM", 1),
            _ph("State / Country: Dadra and Nagar Haveli / India | Category: Leisure & Wildlife Exploration", 2),
            _ph("Destinations: Silvassa • Khanvel • Dudhni • Vasona", 3),
            _ph("Ideal for: Nature Lovers, Families & Leisure Seekers", 4),
            _ph("Best season: November to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Personalized Private Tour (FIT Exclusive)", 7),
            _ph("Vehicle: Luxury Premium Sedan / SUV with dedicated professional chauffeur", 8),
            _ph("Meal Plan: Modified American Plan (Daily Buffet Breakfast & Luxury Dinners)", 9),
            _ph("Route Map: Vapi/Surat Arrival → Silvassa Capital Exploration → Vasona Wildlife Sanctuary → Dudhni Waterfront → Khanvel Nature Retreat → Departure", 10),
            _ph("TRAGUIN Signature Experience: Private, exclusive interactions with tribal folk art masters and personalized luxury lakeside dining setups at Dudhni", 11),
            _ph("Shopping: Warli Paintings, Handcrafted Bamboo Items, Local Toddy & Tribal Cuisine", 12),
            _ph("Important: Check-in 13:00 hrs, check-out 10:00 hrs; early reservation recommended for Dudhni peak winter travel", 13),
        ], moods=["Wildlife", "Nature", "Leisure"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title, duration_label=duration,
        duration_days=_duration_days(duration), starting_price=0,
        price_note="On Request (Premium Class)", rating=Decimal("4.9"), review_count=0,
        tagline="Silvassa • Vasona Lion Safari • Dudhni Lake Resort • Khanvel", overview=(
            "Discover a hidden paradise tucked away between the borders of Gujarat and Maharashtra. This bespoke Dadra and Nagar Haveli Honeymoon Package and family retreat, masterfully curated by travel experts at TRAGUIN, presents a serene escape into lush Portuguese-influenced heritage, breathtaking landscapes, and thrilling wildlife encounters.\n\nThe Premium Dadra and Nagar Haveli Experience is a beautifully paced journey crafted for discerning guests seeking tranquility, luxury, and absolute privacy.\n\nTRAGUIN Curated Touch: Private tribal dance showcase, premium waterfront seating arrangements, and customized flexible timing schedules."
        ),
        seo_title="DN-014 | Grand Exploration | TRAGUIN",
        seo_description=("Premium 05 Nights / 06 Days Dadra and Nagar Haveli package (DN-014 / TG-DNH-014-PREM): Vanganga Lake, Vasona Lion Safari, Dudhni waterfront, Satmaliya Deer Park, Nakshatra Garden"),
        is_featured=False, featured_sort_order=None, is_published=False, highlights=[
            _ih("Vanganga Lake Garden Exploration", 1),
            _ih("Vasona Lion Safari, Tribal Museum & Swaminarayan Temple", 2),
            _ih("Madhuban Dam backwaters & Dudhni Waterfront with optional jet skiing", 3),
            _ih("Satmaliya Deer Park & Khanvel Terraced Landscapes", 4),
            _ih("Nakshatra Garden, Hirwa Van Garden & artisan trails", 5),
            _ih("TRAGUIN Signature Experience: Private tribal folk art interactions and luxury lakeside dining at Dudhni", 6),
        ], days=[
            _day(1, "Arrival in Silvassa – The Colonial Escape", ("Your ultimate Luxury Dadra and Nagar Haveli Holiday begins with a seamless pick-up from Vapi Railway Station or Surat Airport by your dedicated TRAGUIN luxury chauffeur. Enjoy a smooth and picturesque drive into Silvassa, the capital of this enchanting territory. Upon arrival, check in to your premium handpicked hotel where a refreshing welcome drink awaits you. In the afternoon, embark on an easy, slow-paced introduction to the town with a visit to the beautifully landscaped Vanganga Lake Garden. Stroll across its charming Japanese-style wooden bridges, admire the musical fountains, and capture stunning photographs as the sun dips below the horizon, creating unforgettable memories on your arrival day."), [
                "Sightseeing Included: Vanganga Lake Garden Exploration",
                "Evening Experience: Leisure stroll & luxury hotel welcome amenities",
                "Overnight Stay: Silvassa Capital Luxury Resort",
                "Meals Included: Welcome Dinner",
            ]),
            _day(2, "Tribal Heritage & Captivating Lion Safari at Vasona", ("Savor a delightful gourmet breakfast before diving into the rich cultural roots of Dadra and Nagar Haveli. We start with the fascinating Tribal Cultural Museum in Silvassa, displaying an impressive collection of ancient hunting gear, musical instruments, and intricate Warli artwork. Next, elevate the thrill with a private excursion to the highly searched Vasona Lion Safari. Board a specially designed secure safari vehicle to venture deep into the 20-hectare sanctuary, offering an unmatched opportunity to witness the majestic Asiatic Lions roaming freely in their natural habitat. Conclude your evening by admiring the intricate stone carvings of the grand Swaminarayan Temple along the banks of the Daman Ganga River."), [
                "Sightseeing Included: Vasona Lion Safari, Tribal Museum, Swaminarayan Temple",
                "Photography Points: Asiatic Lion encounters, Warli artifacts, Temple architecture",
                "Overnight Stay: Silvassa",
                "Meals Included: Breakfast & Dinner",
            ]),
            _day(3, "Dudhni Waterfront Escape – Scenic Beauty and Water Adventure", ("Today, our TRAGUIN Dadra and Nagar Haveli Packages take you on a highly scenic drive towards Dudhni, located about 40 kms from Silvassa. Dudhni Lake is formed by the waters of the Madhuban Dam and is widely celebrated as the Kashmir of the West due to its breathtaking landscapes and vast water expanse. Check into a stunning waterfront resort. In the afternoon, indulge in an immersive experience on the water—whether you prefer a tranquil Shikara ride or high-speed motorboating. The lake is surrounded by hills inhabited by local tribes, providing excellent cultural and photographic insights. Enjoy a candle-lit lakeside dinner under the stars tonight."), [
                "Sightseeing Included: Madhuban Dam backwaters view, Dudhni Waterfront",
                "Optional Activities: Jet Skiing, Kayaking, or traditional Shikara cruise",
                "Overnight Stay: Dudhni Premium Waterfront Resort",
                "Meals Included: Breakfast & Dinner",
            ]),
            _day(4, "Journey to Khanvel – Tranquil Nature Retreat", ("Witness a spectacular sunrise over the mist-clad Dudhni Lake before driving to the pristine forest enclave of Khanvel. Khanvel is a haven of absolute tranquility, lined with lush green lawns and terraced gardens. Check into your ultra-luxury nature resort surrounded by majestic trees. Spend your afternoon visiting the Deer Park at Satmaliya, where you can spot diverse species of deer, antelopes, and various species of woodland birds from a rustic watchtower. It is an exceptional highlight for any family tour. Spend the late evening relaxing by the azure swimming pool of your resort, enjoying premium stays at their finest."), [
                "Sightseeing Included: Satmaliya Deer Park, Khanvel Terraced Landscapes",
                "Evening Experience: Luxury spa treatment or nature walk at the resort",
                "Overnight Stay: Khanvel Nature Resort",
                "Meals Included: Breakfast & Dinner",
            ]),
            _day(5, "Botanical Majesty & Local Artisanal Trails", ("Enjoy a lavish morning breakfast before heading out to discover the therapeutic wonders of the region. We visit the sprawling Nakshatra Garden in Silvassa, a beautifully arranged Astro-Botanical garden featuring a massive variety of medicinal and spiritual plants linked closely to the zodiac signs. Spend your afternoon meeting local artisans who specialize in authentic Warli painting and bamboo crafts. This is your premier opportunity to support local craftsmanship and take home a valuable piece of tribal heritage. End the final night of your premium tour package with an intimate, luxury dinner organized exclusively by your travel consultant."), [
                "Sightseeing Included: Nakshatra Garden, Hirwa Van Garden",
                "Food Suggestion: Try authentic local Gujarati-style and tribal platters",
                "Overnight Stay: Silvassa / Khanvel",
                "Meals Included: Breakfast & Farewell Gala Dinner",
            ]),
            _day(6, "Departure with Unforgettable Memories", ("Relish your final breakfast overlooking the gorgeous forest canopy. Your professional chauffeur will assist you with your luggage and drive you safely back to Vapi Railway Station or Surat Airport for your onward connection. Your magical journey comes to an end, leaving you with a treasure trove of unforgettable memories of this Premium Dadra and Nagar Haveli Experience, curated meticulously by the holiday experts at TRAGUIN."), [
                "Sightseeing Included: None (Airport / Station Transfer)",
                "Assistance: Complete seamless luggage handling service",
                "Overnight Stay: Tour Concludes",
                "Meals Included: Gourmet Breakfast",
            ]),
        ], hotels=[
            _hotel("Ras Resorts Silvassa / Similar", "Silvassa", "05 Nights", "Deluxe", "Standard Garden View Room", "Breakfast & Dinner", 4, 1),
            _hotel("Treat Resort Silvassa / Khanvel", "Silvassa / Khanvel", "05 Nights", "Premium", "Superior Executive Room", "Breakfast & Dinner", 5, 2),
            _hotel("Pluz Resort Silvassa / Khanvel", "Silvassa / Khanvel", "05 Nights", "Luxury", "Luxury Premium Villa Wing", "Breakfast & Dinner", 5, 3),
            _hotel("TRAGUIN Exclusive Handpicked Boutique Villas", "Silvassa", "05 Nights", "Ultra Luxury", "Presidential Pool Suite", "All Inclusive Premium Plan", 5, 4),
        ], inclusions=[
            _inc_included("05 Nights stay at selected premium handpicked hotels & luxury resorts", 1),
            _inc_included("Comprehensive meal plan featuring daily buffet breakfasts and dinners", 2),
            _inc_included("Dedicated premium air-conditioned sedan/SUV with professional driver", 3),
            _inc_included("All top tourist places in Dadra and Nagar Haveli sightseeing as per itinerary", 4),
            _inc_included("Entry tickets for Vasona Lion Safari and select garden premises", 5),
            _inc_included("Personalized TRAGUIN ground support and welcome amenities", 6),
            _inc_included("Tolls, fuel charges, state taxes, parking fees, and driver allowances", 7),
            _inc_excluded("Airfare or train tickets to reach Surat or Vapi", 8),
            _inc_excluded("Personal expenses such as laundry, phone calls, or tips", 9),
            _inc_excluded("Optional water sports and speed boating charges at Dudhni Lake", 10),
            _inc_excluded("Medical insurance and items not specifically listed in inclusions", 11),
        ],
    )
    return package, itinerary

def build_dn_015(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DN-015"
    tour_code = "TG-DN-015-FAM"
    title = "Family Getaway"
    duration = "02 Nights / 03 Days"
    slug = "dn-015-family-getaway"
    itin_slug = "dn-015-family-getaway-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration, price=0,
        rating=Decimal("4.9"), is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ph("Serial code DN-015 | TRAGUIN tour code TG-DN-015-FAM", 1),
            _ph("State / Country: Dadra and Nagar Haveli / India | Category: Family Getaway", 2),
            _ph("Destinations: Silvassa • Vanganga Lake • Khanvel", 3),
            _ph("Ideal for: Families & Leisure Seekers", 4),
            _ph("Best season: November to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Family Holiday (FIT) with Custom Concierge", 7),
            _ph("Vehicle: Premium, spacious Multi-Purpose Luxury Vehicle (Innova Crysta)", 8),
            _ph("Meal Plan: Modified American Plan (All Breakfasts & Dinners Included)", 9),
            _ph("Route Map: Vapi/Surat Arrival → Silvassa → Vanganga Lake → Khanvel → Departure", 10),
            _ph("TRAGUIN Signature Experience: A beautiful evening family photo session set against the picturesque bridges of Vanganga Lake", 11),
            _ph("Shopping: Warli Tribal Art, Local Silvassa Bakeries Portuguese-inspired baked goods", 12),
            _ph("Important: Check-in 13:00 hrs, check-out 10:00 hrs; winter months ideal for outdoor park strolls", 13),
        ], moods=["Family", "Leisure", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title, duration_label=duration,
        duration_days=_duration_days(duration), starting_price=0,
        price_note="On Request (Premium Class)", rating=Decimal("4.9"), review_count=0,
        tagline="Vanganga Lake & Garden Delight Family Escapade", overview=(
            "Escape the rush of city life and immerse your family in the serene, verdant paradise of Silvassa with the Best Dadra and Nagar Haveli Tour Package curated exclusively by TRAGUIN. Known for its breathtaking landscapes, lush Portuguese-influenced heritage, and charming waterfront paths, this destination is a true sanctuary for relaxation.\n\nTreat your family to a Premium Dadra and Nagar Haveli Experience that seamlessly combines natural wonder with cultural exploration.\n\nTRAGUIN Curated Touch: Handpicked family-centric luxury resorts with pool access, customized kids' activity kits, and specialized evening garden picnics."
        ),
        seo_title="DN-015 | Family Getaway | TRAGUIN",
        seo_description=("Premium 02 Nights / 03 Days Dadra and Nagar Haveli package (DN-015 / TG-DN-015-FAM): Vanganga Lake paddle boating, Tribal Museum, Nakshatra Garden, Madhuban Dam, Church of Our Lady of Piety"),
        is_featured=False, featured_sort_order=None, is_published=False, highlights=[
            _ih("Vanganga Lake Garden & Family Paddle Boating", 1),
            _ih("Tribal Museum, Nakshatra Garden & Madhuban Dam Viewpoint", 2),
            _ih("Church of Our Lady of Piety & Local Souvenir Market", 3),
            _ih("TRAGUIN Signature Experience: Evening family photo session at Vanganga Lake bridges", 4),
            _ih("Curated by TRAGUIN Experts: Relaxed, kid-friendly and senior-friendly schedules", 5),
            _ih("Premium Handpicked Hotels: Resorts with world-class child facilities and expansive lawns", 6),
        ], days=[
            _day(1, "Arrival in Silvassa & Immersive Vanganga Lake Cruise", ("Your wonderful Dadra and Nagar Haveli Sightseeing journey begins with a smooth pickup by your private TRAGUIN luxury chauffeur at Vapi railway station or Surat airport. Enjoy a scenic, relaxing drive into Silvassa, the capital of Dadra and Nagar Haveli, passing by large canopy trees and quaint local houses. Arrive at your premium handpicked resort and check in. In the afternoon, we head towards the stunning Vanganga Lake Garden, a premier highlight among the Top Tourist Places in Dadra and Nagar Haveli. This Japanese-style manicured park features charming thatched cottages, wooden bridges, and clear water channels. We arrange a private paddle-boating ride for your family to enjoy the scenic beauty together. As dusk settles, watch the garden illuminate beautifully, capturing gorgeous family photographs at the signature suspension bridge."), [
                "Sightseeing Included: Vanganga Lake Garden & Family Paddle Boating",
                "Evening Experience: Lakeside photography and illuminated fountain strolls",
                "Overnight Stay: Silvassa Luxury Resort",
                "Meals Included: Welcome Buffet Dinner",
            ]),
            _day(2, "Tribal Heritage Exploration & Nakshatra Garden Delight", ("After a delicious breakfast, set off to discover the cultural soul of the region. We visit the Silvassa Tribal Cultural Museum, an extraordinary venue showing wedding attire, ancient hunting tools, and exquisite Warli clay art. Our guide shares emotional local stories that connect you to the region's history. Afterward, explore the famous Nakshatra Garden, an astrological park designed around celestial constellations. Walk along smooth walkways flanked by rare medicinal plants and vibrant flowerbeds. In the afternoon, take a relaxing drive to the grand Madhuban Dam on the Damanganga River, where breathtaking landscapes stretch out before your eyes. In the evening, return to your resort for a curated culinary dinner."), [
                "Sightseeing Included: Tribal Museum, Nakshatra Garden, Madhuban Dam Viewpoint",
                "Optional Activities: Interactive Warli canvas painting workshop for kids",
                "Overnight Stay: Silvassa Luxury Resort",
                "Meals Included: Breakfast & Dinner",
            ]),
            _day(3, "Colonial Portuguese Memories & Departure", ("On the final morning of your TRAGUIN Dadra and Nagar Haveli Packages, visit the beautiful Church of Our Lady of Piety, a reminder of the region's historical Portuguese connection built in the late 19th century. Walk through its quiet, structural arches before stopping by the local handicraft outlets to purchase authentic tribal souvenirs. Return to your resort to pack your bags and check out. Your premium vehicle will then transfer you comfortably back to Vapi or Surat for your onward journey, concluding an unforgettable family vacation."), [
                "Sightseeing Included: Church of Our Lady of Piety, Local Souvenir Market",
                "Assistance: Complete luggage management up to the station/airport",
                "Overnight Stay: Tour Concludes",
                "Meals Included: Gourmet Breakfast",
            ]),
        ], hotels=[
            _hotel("Treat Resort Silvassa or similar", "Silvassa", "02 Nights", "Deluxe", "Superior Family Room", "Breakfast & Dinner", 4, 1),
            _hotel("Ras Resorts, Silvassa", "Silvassa", "02 Nights", "Premium", "Executive Garden View Room", "Breakfast & Dinner", 5, 2),
            _hotel("Pluz Resort, Silvassa", "Silvassa", "02 Nights", "Luxury", "Luxury Suite Room", "Breakfast & Dinner", 5, 3),
            _hotel("TRAGUIN Signature Forest Villas", "Silvassa", "02 Nights", "Ultra Luxury", "Private Pool Premium Villa", "All Inclusive Custom", 5, 4),
        ], inclusions=[
            _inc_included("02 Nights premium stay at handpicked hotels and resorts", 1),
            _inc_included("Daily multi-cuisine breakfast and custom-tailored dinners", 2),
            _inc_included("Private, dedicated luxury Innova Crysta for all transfers and sightseeing", 3),
            _inc_included("Complimentary paddle-boating tickets at Vanganga Lake Garden", 4),
            _inc_included("All entry fees and parking charges covered seamlessly", 5),
            _inc_included("Welcome drinks and specialized kids' amenity basket upon arrival", 6),
            _inc_included("Comprehensive 24/7 TRAGUIN on-ground customer support", 7),
            _inc_excluded("Train tickets or flights to Vapi / Surat", 8),
            _inc_excluded("Personal expenses such as laundry, phone calls, and tips", 9),
            _inc_excluded("Any alcoholic drinks and meals not mentioned above", 10),
            _inc_excluded("Camera or drone photography fees inside gardens", 11),
            _inc_excluded("Optional specialized tribal art workshops", 12),
        ],
    )
    return package, itinerary

def build_dn_016(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DN-016"
    tour_code = "TG-DN-016-FAM"
    title = "Satmaliya Deer Park"
    duration = "02 Nights / 03 Days"
    slug = "dn-016-satmaliya-deer-park"
    itin_slug = "dn-016-satmaliya-deer-park-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration, price=0,
        rating=Decimal("4.9"), is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ph("Serial code DN-016 | TRAGUIN tour code TG-DN-016-FAM", 1),
            _ph("State / Country: Dadra and Nagar Haveli / India | Category: Family Getaway", 2),
            _ph("Destinations: Silvassa • Satmaliya • Khanvel • Vanganga", 3),
            _ph("Ideal for: Families & Nature Lovers", 4),
            _ph("Best season: November to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Tour (FIT) with Full Concierge Assistance", 7),
            _ph("Vehicle: Premium, ultra-spacious Ertiga / Innova Crysta for smooth, elegant land transits", 8),
            _ph("Meal Plan: Modified American Plan (Daily Premium Breakfast & Gourmet Dinner Included)", 9),
            _ph("Route Map: Vapi / Silvassa Arrival → Satmaliya Safari → Dudhni Lake → Vanganga Garden → Departure", 10),
            _ph("TRAGUIN Signature Experience: Private family boat cruise across Dudhni Lake and an exclusive live workshop with an authentic local Warli tribal artisan", 11),
            _ph("Shopping: Handmade Warli Art paintings, Authentic Forest Products, Local Bamboo Crafts", 12),
            _ph("Important: Resort check-in 13:00 hrs, check-out 10:00 hrs; life jackets mandatory for Dudhni water activities", 13),
        ], moods=["Family", "Wildlife", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title, duration_label=duration,
        duration_days=_duration_days(duration), starting_price=0,
        price_note="On Request (Premium Class)", rating=Decimal("4.9"), review_count=0,
        tagline="Silvassa • Satmaliya Deer Park Safari • Dudhni Lake • Vanganga Garden", overview=(
            "Escape into a world of lush forest canopies, winding rivers, and nostalgic Portuguese heritage. This premium weekend getaway, exclusively crafted by TRAGUIN travel specialists, offers a meticulously organized, high-comfort journey into Dadra and Nagar Haveli. From thrilling open-jeep wildlife safaris at Satmaliya Deer Park to tranquil, romantic boat rides across Dudhni Lake, every detail is engineered to create unforgettable memories.\n\nOur Dadra and Nagar Haveli Family Tour is intentionally designed for families seeking a premium, refreshing getaway without long, exhausting travel times.\n\nTRAGUIN Curated Touch: Pre-booked, priority safari tickets to avoid queues, guaranteed lake-view rooms, and complimentary tribal art demonstration for the family."
        ),
        seo_title="DN-016 | Satmaliya Deer Park | TRAGUIN",
        seo_description=("Premium 02 Nights / 03 Days Dadra and Nagar Haveli package (DN-016 / TG-DN-016-FAM): Vanganga Garden, Satmaliya Safari, Dudhni boat cruise, Church of Our Lady of Piety, Nakshatra Garden"),
        is_featured=False, featured_sort_order=None, is_published=False, highlights=[
            _ih("Vanganga Garden & Tribal Museum Silvassa", 1),
            _ih("Satmaliya Safari & Dudhni Water Sports Complex with family boat cruise", 2),
            _ih("Church of Our Lady of Piety & Nakshatra Garden", 3),
            _ih("TRAGUIN Signature Experience: Private family boat cruise and live Warli artisan workshop", 4),
            _ih("Curated by TRAGUIN Experts: Personalized smooth travel pace with kid-friendly rest breaks", 5),
            _ih("Luxury Transportation: Elite fleet of pristine vehicles with professional chauffeurs", 6),
        ], days=[
            _day(1, "Arrival in Silvassa & Enchanting Vanganga Garden", ("Your refreshing journey begins with a smooth pickup from Vapi Railway Station or an onward drive from Mumbai/Surat in your premium TRAGUIN luxury vehicle. Arrive in Silvassa, the capital of Dadra and Nagar Haveli, and experience a flawless check-in at your handpicked luxury resort. After relaxing, step out for a gentle afternoon tour of the famous Vanganga Garden. This beautifully landscaped Japanese-style garden features a wooden bridge, paddle boating, and paved walkways surrounded by towering trees. It is an exceptionally popular Instagram location due to its picture-perfect scenery. As the sun sets, visit the nearby Tribal Cultural Museum to view authentic collections of tribal musical instruments, hunting tools, and lifestyle models, offering an immersive cultural perspective. Enjoy a gourmet dinner at your resort."), [
                "Sightseeing Included: Vanganga Garden, Tribal Museum Silvassa",
                "Evening Experience: Leisure stroll, family photo session by the lake",
                "Overnight Stay: Silvassa (Premium Luxury Resort)",
                "Meals Included: Welcome Buffet Dinner",
            ]),
            _day(2, "Satmaliya Deer Safari & Dudhni Lake Water Sports", ("Wake up to a crisp morning and enjoy a delicious breakfast. Today, experience a major highlight of your Premium Dadra and Nagar Haveli Experience—the Satmaliya Deer Park Safari. Board a private open-jeep to venture deep into the sanctuary. Watch for magnificent herds of Chital (spotted deer), Blackbucks, Sambar deer, and a variety of vibrant migratory birds feeding in their completely natural habitat. Next, take a smooth, scenic drive to Dudhni Lake, formed by the waters of the Madhuban Dam. This pristine reservoir is affectionately called the Kashmir of the West due to its vast expanse and surrounding hills. TRAGUIN includes an exclusive family motorboat cruise across the tranquil lake. For thrill-seekers, optional jet skiing, speed boating, and kayaking are available. Return to the resort for a special evening featuring a local Warli art painting demonstration, followed by a grand farewell dinner."), [
                "Sightseeing Included: Satmaliya Safari, Dudhni Water Sports Complex",
                "Exclusive Highlights: Private open-jeep safari, premium family boat cruise",
                "Overnight Stay: Silvassa",
                "Meals Included: Breakfast & Farewell Dinner",
            ]),
            _day(3, "Portuguese Heritage & Departure", ("Savor a leisurely breakfast looking out over the resort's green lawns. Check out and head to the historic Church of Our Lady of Piety, a beautifully preserved stone structure built by the Portuguese in the late 19th century that highlights the region's fascinating colonial history. Next, make a quick stop at the sprawling Nakshatra Garden, known for its extensive variety of medicinal plants and astro-themed layouts. Pick up unique handmade souvenirs, local crafts, and organic forest honey. Your professional chauffeur will then assist with your luggage and provide a comfortable drop-off at Vapi Railway Station or your home destination. Your refreshing weekend tour concludes, leaving you with unforgettable memories from your TRAGUIN Dadra and Nagar Haveli Packages."), [
                "Sightseeing Included: Church of Our Lady of Piety, Nakshatra Garden",
                "Shopping stop: Kilvani Road local handicraft stores",
                "Overnight Stay: Tour Concludes",
                "Meals Included: Gourmet Breakfast",
            ]),
        ], hotels=[
            _hotel("Treat Resort Silvassa or similar", "Silvassa", "02 Nights", "Deluxe", "Deluxe Garden View Room", "Breakfast & Dinner", 4, 1),
            _hotel("Ras Resorts Silvassa", "Silvassa", "02 Nights", "Premium", "Executive River-Facing View", "Breakfast & Dinner", 5, 2),
            _hotel("Khanvel Resort (Premium Wing)", "Khanvel", "02 Nights", "Luxury", "Luxury Club Room / Cottage", "Breakfast & Dinner", 5, 3),
            _hotel("TRAGUIN Handpicked Luxury Boutique Villas", "Silvassa", "02 Nights", "Ultra Luxury", "Private Pool Premium Suite", "All Inclusive Premium", 5, 4),
        ], inclusions=[
            _inc_included("02 Nights premium resort accommodation as per selected tier", 1),
            _inc_included("Daily buffet breakfast and custom gourmet dinners at the resort", 2),
            _inc_included("Private luxury transportation for all transfers & sightseeing tours", 3),
            _inc_included("Pre-booked entry tickets for Satmaliya Deer Park Safari & Vanganga Garden", 4),
            _inc_included("Complimentary private boat cruise for the family at Dudhni Lake", 5),
            _inc_included("In-vehicle amenities: mineral water, wet tissues, and kids' snacks", 6),
            _inc_included("Professional 24/7 dedicated TRAGUIN on-ground assistance", 7),
            _inc_included("All applicable state taxes, fuel charges, parking, and tolls", 8),
            _inc_excluded("Train tickets / Flight charges to reach the gateway point", 9),
            _inc_excluded("High-speed adventure water sports activities at Dudhni Lake", 10),
            _inc_excluded("Personal expenses: laundry, alcoholic drinks, or room service tips", 11),
            _inc_excluded("Professional camera or video camera shooting fees", 12),
            _inc_excluded("Optional extensions or personal porterage charges", 13),
        ],
    )
    return package, itinerary

def build_dn_017(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DN-017"
    tour_code = "TG-DN-017-FAM"
    title = "Bindrabin Temple"
    duration = "02 Nights / 03 Days"
    slug = "dn-017-bindrabin-temple"
    itin_slug = "dn-017-bindrabin-temple-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration, price=0,
        rating=Decimal("4.9"), is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ph("Serial code DN-017 | TRAGUIN tour code TG-DN-017-FAM", 1),
            _ph("State / Country: Dadra and Nagar Haveli / India | Category: Family Getaways", 2),
            _ph("Destinations: Silvassa • Bindrabin • Khanvel", 3),
            _ph("Ideal for: Families & Spiritual Seekers", 4),
            _ph("Best season: November to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Family Tour (FIT)", 7),
            _ph("Vehicle: Private, luxury air-conditioned vehicle with family-friendly chauffeur", 8),
            _ph("Meal Plan: Modified American Plan (Breakfast & Dinner Included)", 9),
            _ph("Route Map: Vapi/Surat Arrival → Silvassa Sights → Bindrabin → Swaminarayan Mandir → Departure", 10),
            _ph("TRAGUIN Signature Experience: Curated family photo session in front of the grand Swaminarayan Temple's carved stone facades", 11),
            _ph("Shopping: Warli Paintings, Bamboo Crafts, Local Toddy/Wine Varieties", 12),
            _ph("Important: Modest clothing recommended at temples; book weekend resort slots 3-4 weeks in advance", 13),
        ], moods=["Spiritual", "Family", "Heritage"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title, duration_label=duration,
        duration_days=_duration_days(duration), starting_price=0,
        price_note="On Request (Premium Class)", rating=Decimal("4.9"), review_count=0,
        tagline="Bindrabin Temple • Swaminarayan Sights • Silvassa Heritage", overview=(
            "Welcome to a hidden sanctuary of verdant woodlands, tranquil rivers, and magnificent architectural wonders. Handcrafted by the travel specialists at TRAGUIN, this multi-generational weekend retreat balances soul-stirring spiritual discovery with enriching leisure highlights. From the ornate stone carvings of the grand Swaminarayan Temple to the historic, peaceful riverside layout of Bindrabin Temple, this journey promises a delightful getaway.\n\nThis Dadra and Nagar Haveli Family Tour is designed to provide families with a refreshing, stress-free holiday.\n\nTRAGUIN Curated Touch: Reserved priority seating for evening temple darshans, curated traditional thali lunch recommendations, and specialized itinerary pacing."
        ),
        seo_title="DN-017 | Bindrabin Temple | TRAGUIN",
        seo_description=("Premium 02 Nights / 03 Days Dadra and Nagar Haveli package (DN-017 / TG-DN-017-FAM): Swaminarayan Temple, Bindrabin Temple, Tribal Museum, Vanganga Lake, Satmaliya Deer Park"),
        is_featured=False, featured_sort_order=None, is_published=False, highlights=[
            _ih("Swaminarayan Temple Complex & Silvassa Riverside Gardens", 1),
            _ih("Bindrabin Temple, Tribal Museum & Vanganga Lake Garden", 2),
            _ih("Satmaliya Deer Park (Drive-by View) & Local Souvenir Emporium", 3),
            _ih("TRAGUIN Signature Experience: Family photo session at Swaminarayan Temple facades", 4),
            _ih("Curated by TRAGUIN Experts: Handpicked routes maximizing scenic beauty with short drives", 5),
            _ih("Personalized Assistance: Dedicated destination managers monitoring your schedule", 6),
        ], days=[
            _day(1, "Arrival in Silvassa & Magnificent Swaminarayan Darshan", ("Embark on your Premium Dadra and Nagar Haveli Experience with a comfortable arrival transfer from Vapi or Surat station/airport. Your private chauffeur will welcome you and ensure a smooth drive to Silvassa, the capital of Dadra and Nagar Haveli. Check into your premium resort and relax before an afternoon exploration. Our first stop is the magnificent BAPS Swaminarayan Temple, an architectural masterpiece built along the banks of the Daman Ganga River. Marvel at the intricate pink sandstone carvings, pristine marble pillars, and beautifully manicured lawns. This spot is widely known as a top Instagram location due to its grand structure. Spend the evening soaking in the spiritual ambiance and listening to traditional hymns, creating unforgettable memories with your family."), [
                "Sightseeing Included: Swaminarayan Temple Complex, Silvassa Riverside Gardens",
                "Evening Experience: Serene evening stroll & dynamic illumination view",
                "Overnight Stay: Silvassa (Premium Handpicked Resort)",
                "Meals Included: Welcome Dinner",
            ]),
            _day(2, "Sacred Bindrabin Temple & Vanganga Lake Leisure Trails", ("Enjoy a delicious breakfast before heading out on your Dadra and Nagar Haveli Sightseeing journey towards the sacred Bindrabin Temple, affectionately known as Vrudhavan. Dedicated to Lord Shiva, this historic temple is located on the riverbanks, surrounded by grand, tall trees, providing a peaceful retreat for families. Absorb the calming spiritual vibes and explore the riverside walkways. In the afternoon, return to the city center to visit the Tribal Cultural Museum, where children can learn about authentic musical instruments, traditional hunting gear, and historic wedding attire. Conclude your day at the Vanganga Lake Garden, a beautifully landscaped Japanese-style garden featuring quaint wooden bridges, pleasant fountains, and calm waters, perfect for a relaxing family paddle boat ride."), [
                "Sightseeing Included: Bindrabin Temple, Tribal Museum, Vanganga Lake Garden",
                "Optional Activities: Family paddle boating & Warli art workshop interaction",
                "Overnight Stay: Silvassa",
                "Meals Included: Breakfast & Dinner",
            ]),
            _day(3, "Deer Park Visit & Farewell to the Green Haven", ("Start your final morning with an optional early morning visit to the Satmaliya Deer Park to spot diverse deer species roaming freely in their natural habitat. Return to the resort for a hearty breakfast and check out. Before your departure, your guide will take you to local handicraft outlets to pick up authentic souvenirs. Your private vehicle will then provide a smooth transfer back to Vapi or Surat, concluding your highly rewarding TRAGUIN Dadra and Nagar Haveli Packages holiday with a heart full of joy."), [
                "Sightseeing Included: Satmaliya Deer Park (Drive-by View) & Local Souvenir Emporium",
                "Assistance: Complete luggage handling and departure drop-off",
                "Overnight Stay: Tour Concludes",
                "Meals Included: Breakfast",
            ]),
        ], hotels=[
            _hotel("Ras Resorts Silvassa or similar", "Silvassa", "02 Nights", "Deluxe", "Standard Garden View Room", "Breakfast & Dinner", 4, 1),
            _hotel("Treat Resort Silvassa", "Silvassa", "02 Nights", "Premium", "Superior Family Pool View Room", "Breakfast & Dinner", 5, 2),
            _hotel("Pluz Resort Silvassa", "Silvassa", "02 Nights", "Luxury", "Luxury Villa / Premium Suite", "Breakfast & Dinner", 5, 3),
            _hotel("TRAGUIN Handpicked Luxury Boutiques", "Silvassa", "02 Nights", "Ultra Luxury", "Signature Executive Suite", "All Inclusive Premium Plan", 5, 4),
        ], inclusions=[
            _inc_included("02 Nights luxury stay in top-rated family resorts", 1),
            _inc_included("Daily multi-cuisine buffet breakfasts and specialized dinners", 2),
            _inc_included("Private dedicated AC luxury vehicle for the entire itinerary", 3),
            _inc_included("All toll taxes, fuel charges, parking fees, and driver allowances", 4),
            _inc_included("Complimentary entry passes to gardens and temple complexes", 5),
            _inc_included("Custom welcome amenities & kid-friendly refreshment packs in-car", 6),
            _inc_included("Continuous 24/7 TRAGUIN on-ground destination assistance", 7),
            _inc_excluded("Train tickets / Airfare to the gateway cities", 8),
            _inc_excluded("Any personal expenses like laundry, minibar, or telephone calls", 9),
            _inc_excluded("Boating tickets or charges for optional workshops", 10),
            _inc_excluded("Medical and travel insurance policies", 11),
            _inc_excluded("Anything not explicitly listed under inclusions", 12),
        ],
    )
    return package, itinerary

def build_dn_018(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DN-018"
    tour_code = "TG-DN-018-FAM"
    title = "Family Leisure"
    duration = "04 Nights / 05 Days"
    slug = "dn-018-family-leisure"
    itin_slug = "dn-018-family-leisure-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration, price=0,
        rating=Decimal("4.9"), is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ph("Serial code DN-018 | TRAGUIN tour code TG-DN-018-FAM", 1),
            _ph("State / Country: Dadra and Nagar Haveli & Daman / India | Category: Family Leisure Vacation", 2),
            _ph("Destinations: Silvassa • Daman Beaches • Khanvel", 3),
            _ph("Ideal for: Families & Multi-Generational Groups", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Family FIT Tour", 7),
            _ph("Vehicle: Premium, spacious AC Innova Crysta throughout the journey", 8),
            _ph("Meal Plan: Modified American Plan (All Breakfasts & Dinners Included)", 9),
            _ph("Route Map: Vapi/Surat Arrival → Silvassa (2N) → Khanvel Excursion → Daman Beaches (2N) → Departure", 10),
            _ph("TRAGUIN Signature Experience: A beautiful private sunset high-tea lounge experience custom set up right on the sands of Daman for your family", 11),
            _ph("Shopping: Warli Tribal Art pieces, Colonial Leather Crafts, Sea-Shell Souvenirs", 12),
            _ph("Important: Check-in 13:00 or 14:00 hrs, check-out 11:00 AM; beach sports subject to tide and weather conditions", 13),
        ], moods=["Family", "Beach", "Leisure"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title, duration_label=duration,
        duration_days=_duration_days(duration), starting_price=0,
        price_note="On Request (Premium Class)", rating=Decimal("4.9"), review_count=0,
        tagline="Silvassa Wildlife • Khanvel Gardens • Devka & Jampore Beaches", overview=(
            "Discover a wonderful mixture of lush greenery, Portuguese history, and serene coastlines. This customized signature itinerary by TRAGUIN is carefully designed for families seeking a premium escape from city life. From the dense green forests, deer parks, and tribal heritage museums of Silvassa to the grand, golden sands and historical forts of Daman, we ensure your family experiences premium stays, curated experiences, and absolute comfort.\n\nOur Dadra and Nagar Haveli Family Tour brings you the absolute best of two diverse worlds—the tranquil nature of Silvassa and the scenic beaches of Daman.\n\nTRAGUIN Curated Touch: Private beach-side family high-tea setup, VIP entries to lion safaris, and handpicked rooms featuring private balconies."
        ),
        seo_title="DN-018 | Family Leisure | TRAGUIN",
        seo_description=("Premium 04 Nights / 05 Days Dadra and Nagar Haveli package (DN-018 / TG-DN-018-FAM): Vanganga Lake, Vasona Lion Safari, Satmaliya Deer Park, Nakshatra Garden, Jampore Beach, Moti Daman Fort, Devka Beach"),
        is_featured=False, featured_sort_order=None, is_published=False, highlights=[
            _ih("Vanganga Lake Garden & Boating Experience", 1),
            _ih("Vasona Lion Safari, Satmaliya Deer Park, Tribal Museum & Swaminarayan Temple", 2),
            _ih("Khanvel Nakshatra Garden & Jampore Beach with TRAGUIN beach-side high-tea", 3),
            _ih("Moti Daman Fort, Church of Bom Jesus, Nani Daman Fort & Devka Beach Promenade", 4),
            _ih("TRAGUIN Signature Experience: Private sunset high-tea lounge on Daman sands", 5),
            _ih("Curated by TRAGUIN Experts: Timed itineraries ideal for multi-generational families", 6),
        ], days=[
            _day(1, "Arrival & Welcome to Silvassa – The Green Heart", ("Your luxury family holiday begins with a warm welcome by your dedicated TRAGUIN chauffeur at Vapi Railway Station or Surat Airport. Board your premium private vehicle and enjoy a smooth, scenic drive to Silvassa, the green capital of Dadra and Nagar Haveli. Arrive at your luxury riverside resort, check in, and unpack at leisure. In the afternoon, we visit the beautiful Vanganga Lake Garden. This Japanese-style manicured park features charming wooden bridges, floating paddle-boats, and lush lawns perfect for a relaxed family walk. As night falls, return to the resort for an exclusive multi-cuisine dinner."), [
                "Sightseeing Included: Vanganga Lake Garden & Boating Experience",
                "Evening Experience: Traditional welcome non-alcoholic cocktails & resort leisure",
                "Overnight Stay: Silvassa (Premium Luxury Resort)",
                "Meals Included: Welcome Family Dinner",
            ]),
            _day(2, "Wildlife Safari & Tribal Culture Trails in Silvassa", ("Treat your family to an exciting morning after breakfast as we explore the Top Tourist Places in Dadra and Nagar Haveli. Our first stop is the Vasona Lion Safari, where you board a secured park vehicle to spot Asiatic lions roaming in their natural habitat. Next, we head to the Satmaliya Deer Park to see beautiful herds of sambar, chital, and blackbucks. After lunch, visit the Silvassa Tribal Museum to view authentic tribal ornaments, ancient hunting gear, and stunning Warli paintings. Wrap up your afternoon at the grand, intricately carved Swaminarayan Temple, renowned for its peaceful spiritual ambiance and magnificent architecture."), [
                "Sightseeing Included: Vasona Lion Safari, Satmaliya Deer Park, Tribal Museum, Swaminarayan Temple",
                "Photography Points: Lion spotting zones, temple marble facades, Warli wall murals",
                "Overnight Stay: Silvassa",
                "Meals Included: Breakfast & Dinner",
            ]),
            _day(3, "Scenic Drive to Daman via Khanvel Lush Valley", ("Check out from your resort after breakfast and drive through the beautiful valleys of Khanvel. Stop to visit the Nakshatra Garden, a well-planned astrological park featuring therapeutic medicinal herbs and gorgeous seasonal blooms. Continue your journey to the historic coastal city of Daman. Upon arrival, check in to your premium beachfront resort. The late afternoon is dedicated to exploring Jampore Beach, famous for its firm, dark sands and calm waters. Your family can indulge in optional exciting activities like parasailing, ATV rides, and jet skiing, followed by a complimentary, curated beach-side high-tea experience provided exclusively by TRAGUIN."), [
                "Sightseeing Included: Khanvel Nakshatra Garden, Jampore Beach Sunset Walk",
                "Evening Experience: Exclusive TRAGUIN Beach-side Family High-Tea setup",
                "Overnight Stay: Daman (Beachfront Premium Stay)",
                "Meals Included: Breakfast & Seafood Special Dinner",
            ]),
            _day(4, "Portuguese Fort Heritage & Devka Beach Promenade", ("Immerse yourself in history today as we explore the ancient architectural wonders of Daman. We visit Moti Daman Fort, an imposing 16th-century Portuguese fortress housing the breathtaking Church of Bom Jesus, famous for its magnificent golden altarpieces and intricate woodwork. Next, explore Nani Daman Fort, which looks over the bustling harbor where traditional fishing boats anchor. Spend your evening at the newly renovated Devka Beach Promenade. Walk along the beautifully illuminated coastal path, let the children play in the amusement parks, and enjoy delicious local street food while listening to the relaxing ocean waves."), [
                "Sightseeing Included: Moti Daman Fort, Church of Bom Jesus, Nani Daman Fort, Devka Beach Promenade",
                "Optional Activities: Duty-free shopping for global premium brands in local markets",
                "Overnight Stay: Daman",
                "Meals Included: Breakfast & Farewell Grand Dinner",
            ]),
            _day(5, "Farewell Family Memories & Departure", ("Enjoy a luxurious beachside breakfast with panoramic ocean views. Spend your morning relaxing by the resort's swimming pool or taking a final stroll along the shore. Check out from your resort by noon, where your professional TRAGUIN chauffeur will assist you with all luggage. Transfer comfortably back to Vapi Railway Station or Surat Airport for your onward journey home, carrying a treasure trove of unforgettable memories from this perfect family combo vacation."), [
                "Sightseeing Included: None (Airport/Station transfer only)",
                "Assistance: Complete baggage handling and exit drop service",
                "Overnight Stay: Tour Concludes",
                "Meals Included: Gourmet Buffet Breakfast",
            ]),
        ], hotels=[
            _hotel("Ras Resorts Silvassa or similar / Hotel Silver Sands Beach Resort", "Silvassa / Daman", "02N Silvassa + 02N Daman", "Deluxe", "Standard Room", "Breakfast & Dinner", 4, 1),
            _hotel("Treat Resort Silvassa (Deluxe Wing) / The Deltin Daman (Superior Room)", "Silvassa / Daman", "02N Silvassa + 02N Daman", "Premium", "Superior Room", "Breakfast & Dinner", 5, 2),
            _hotel("Pluz Resort / Khanvel Resort (Suites) / The Gold Beach Resort (Ocean View)", "Silvassa / Daman", "02N Silvassa + 02N Daman", "Luxury", "Luxury Suite / Ocean View", "Breakfast & Dinner", 5, 3),
            _hotel("TRAGUIN Luxury Signature Villas / The Deltin (Luxury Presidential Suite)", "Silvassa / Daman", "02N Silvassa + 02N Daman", "Ultra Luxury", "Presidential Suite", "All Inclusive Premium", 5, 4),
        ], inclusions=[
            _inc_included("04 Nights luxury accommodation in handpicked family resorts", 1),
            _inc_included("Daily premium buffet breakfast and lavish dinner menus", 2),
            _inc_included("Private AC Innova Crysta for all transfers and sightseeing tours", 3),
            _inc_included("Complimentarty private family High-Tea experience at Jampore Beach", 4),
            _inc_included("Entry passes for Vasona Lion Safari & Vanganga Lake Garden boating", 5),
            _inc_included("Driver allowance, fuel fees, toll charges, and private parking expenses", 6),
            _inc_included("Dedicated 24/7 on-ground TRAGUIN support concierge", 7),
            _inc_included("Complimentary welcome amenities and refreshing packed juices inside the car", 8),
            _inc_excluded("Flights / Train tickets to Surat or Vapi", 9),
            _inc_excluded("Beach water sports (parasailing, jet-skiing, ATV rides)", 10),
            _inc_excluded("Personal expenses like laundry, phone calls, and tips", 11),
            _inc_excluded("Custom alcohol or beverage orders during lunches", 12),
            _inc_excluded("Travel and medical insurance coverages", 13),
        ],
    )
    return package, itinerary

DADRA_NAGAR_HAVELI_BUILDERS = [
    build_dn_001,
    build_dn_002,
    build_dn_003,
    build_dn_004,
    build_dn_005,
    build_dn_006,
    build_dn_007,
    build_dn_008,
    build_dn_009,
    build_dn_010,
    build_dn_011,
    build_dn_012,
    build_dn_013,
    build_dn_014,
    build_dn_015,
    build_dn_016,
    build_dn_017,
    build_dn_018,
]
