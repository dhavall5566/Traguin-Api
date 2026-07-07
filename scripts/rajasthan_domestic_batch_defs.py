"""Builder functions for RJ-011 through RJ-018 Rajasthan domestic packages."""

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

RAJASTHAN_SLUG = "rajasthan"
RAJASTHAN_DESTINATION_ID = "9785e4ac-5485-48a2-a7c9-f91002d73806"


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


def build_rj_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "RJ-011"
    tour_code = "TRAGUIN-RJ-011"
    title = "Pink City Jaipur Short Break"
    duration = "02 Nights / 03 Days"
    slug = "rj-011-pink-city-jaipur-short-break"
    itin_slug = "rj-011-pink-city-jaipur-short-break-itinerary"
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
            _ph("State / Country: Rajasthan, India | Category: Family Vacation / Royal", 2),
            _ph("Destinations: Jaipur (The Pink City)", 3),
            _ph("Ideal for: Families, Leisure & Royal Connoisseurs", 4),
            _ph("Best season: October to March", 5),
            _ph("Vehicle: Dedicated Luxury AC Sedan / SUV (Chauffeur-Driven)", 6),
            _ph("Meal Plan: Continental Luxury Buffet Breakfast & Festive Royal Dinners", 7),
            _ph("Route Details: Jaipur Arrival → Heritage Forts exploration → Local Cultural Hubs → Departure", 8),
            _ph("TRAGUIN Signature Experience: Private curated walk within the City Palace compound.", 9),
            _ph("Curated by Experts: Perfectly planned segments with premium transportation and hassle-free transit routes.", 10),
            _ph("Exclusive Recommendations: Handpicked boutique recommendations for local jewelers and traditional block-printing houses.", 11),
            _ph("Shopping & Local Experiences: Famous Shopping Items: Blue Pottery, Lac Bangles, Kundan Jewelry, Bandhej Textiles. Local Markets: Johari Bazaar, Tripolia Bazaar, Chandpole Bazaar. Instagram Spots: Patrika Gate, Albert Hall Museum, Hawa Mahal Frontage.", 12),
            _ph("Important Notes: Hotel Policies: Rooms are subject to availability. Check-in is usually at 14:00 hrs. Advance Booking: Planning ahead for premium slots at Rambagh Palace is highly recommended. Transport Rules: Our professional vehicle follows strict guidelines for client luggage care and smooth driving.", 13),
        ],
        moods=["Family", "Royal", "Heritage"],
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
        tagline="Pink City Jaipur Short Break • 02 Nights / 03 Days",
        overview=(
            "Welcome to the majestic realm of royalty, heritage, and timeless architecture. Handcrafted meticulously by travel experts at TRAGUIN, this signature Jaipur Honeymoon Package and Rajasthan Family Tour is beautifully designed to immerse your loved ones into a grand, seamless, and aristocratic escape. Experience the captivating spirit of Rajasthan with ultra-premium stays, grand hospitality, and exquisite storytelling.\n\n"
            "TOUR OVERVIEW\n"
            "Vehicle Allocated: Dedicated Luxury AC Sedan / SUV (Chauffeur-Driven)\n"
            "Meal Plan: Continental Luxury Buffet Breakfast & Festive Royal Dinners\n"
            "Route Details: Jaipur Arrival → Heritage Forts exploration → Local Cultural Hubs → Departure\n\n"
            "TRAGUIN Curated Experience Note: This premium itinerary introduces families to iconic attractions without the rush, emphasizing breathtaking landscapes, handpicked hotels, and unique immersive experiences.\n\n"
            "WHY CHOOSE A LUXURY RAJASTHAN HOLIDAY?\n"
            "Rajasthan is an enchanting land where history echoes through majestic sandstone palaces, vibrant bazaars, and beautiful heritage monuments. For those looking for the ultimate Premium Rajasthan Experience or the Best Time to Visit Rajasthan, Jaipur stands as an irreplaceable crown jewel.\n"
            "During your Jaipur Sightseeing journey, you will encounter the Top Tourist Places in Rajasthan including the iconic Amber Fort, the floating Jal Mahal, and the honeycomb facade of Hawa Mahal. Our signature TRAGUIN Rajasthan Packages guarantee handpicked hotels, priority entries, luxury transportation, and unforgettable memories for your family."
        ),
        seo_title="RJ-011 | Pink City Jaipur Short Break | TRAGUIN",
        seo_description="Premium 02 Nights / 03 Days Rajasthan package (RJ-011 / TRAGUIN-RJ-011): Hawa Mahal, Amber Fort, Jal Mahal, City Palace, Jantar Mantar, Chokhi Dhani, and 4-tier handpicked accommodation in Jaipur.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Hawa Mahal, Birla Mandir, Chokhi Dhani Village, Amber Fort, Jal Mahal, City Palace, Jantar Mantar", 1),
            _ih("Johari Bazaar and Bapu Bazaar shopping excursion", 2),
            _ih("TRAGUIN Signature Experience: Private curated walk within the City Palace compound", 3),
            _ih("Curated by Experts: Premium transportation and hassle-free transit routes", 4),
            _ih("Exclusive Recommendations: Handpicked boutique jewelers and traditional block-printing houses", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Jaipur",
                (
                    "Arrive in Jaipur where your premium chauffeured luxury vehicle and TRAGUIN representative welcome you warmly. Transfer smoothly to your magnificent handpicked heritage hotel. After check-in and leisure time, begin your Jaipur Sightseeing at the legendary Hawa Mahal (Palace of Winds), capturing its spectacular honeycomb architecture. Later, visit the pristine Birla Mandir, made of pure white marble, before heading to Chokhi Dhani for an immersive cultural evening featuring traditional folk music, puppet shows, and a spectacular Rajasthani royal feast."
                ),
                [
                    "Sightseeing Included: Hawa Mahal (Photo Stop), Birla Mandir, Chokhi Dhani Village.",
                    "Evening Experience: Live folk dances, camel rides, and authentic cultural culinary arts.",
                    "Overnight Stay: Handpicked Premium Luxury Palace Hotel, Jaipur.",
                    "Meals Included: Welcome Amenities & Festive Dinner.",
                ],
            ),
            _day(
                2,
                "Jaipur Heritage Exploration",
                (
                    "Enjoy a premium buffet breakfast before starting a grand day out. Ascend the majestic hill of Amber Fort like royalty. Wander through the breathtaking Sheesh Mahal (Mirror Palace), where a single candle illuminates the entire hall. Next, stop for stunning photography at the Jal Mahal, floating gracefully in the center of Man Sagar Lake. Proceed to the opulent City Palace, still home to the royal family, and marvel at the giant astronomical instruments at the UNESCO World Heritage listed Jantar Mantar."
                ),
                [
                    "Sightseeing Included: Amber Fort, Jal Mahal Viewpoint, City Palace, Jantar Mantar.",
                    "Photography Points: Mirror reflection shots inside Amber Fort and sunset views at Jal Mahal.",
                    "Overnight Stay: Handpicked Premium Luxury Palace Hotel, Jaipur.",
                    "Meals Included: Gourmet Breakfast & Luxury Dinner.",
                ],
            ),
            _day(
                3,
                "Vibrant Bazaars & Departure",
                (
                    "Savor a luxurious morning breakfast at your hotel. Spend your morning exploring the historic Johari Bazaar and Bapu Bazaar, famous for traditional block-print textiles, blue pottery, royal mojris, and fine kundan jewelry. In the afternoon, enjoy an authentic local lunch, visiting highly recommended artisan cafes. Your private chauffeur will then transfer you comfortably to the Jaipur Airport or Railway Station, bringing your premium TRAGUIN experience to a perfect close."
                ),
                [
                    "Sightseeing Included: Local Heritage Bazaars, Shopping Excursion.",
                    "Meals Included: Sumptuous Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel("Lemon Tree Premier, Jaipur", "Jaipur", "02 Nights", "Deluxe", "Deluxe Room", "CP (Breakfast Only)", 4, 1),
            _hotel("ITC Rajputana - A Luxury Collection Hotel", "Jaipur", "02 Nights", "Premium", "Executive Cabin Room", "MAPAI (Breakfast + Dinner)", 5, 2),
            _hotel("The Raj Palace (Grand Heritage Hotel)", "Jaipur", "02 Nights", "Luxury", "Heritage Palace Suite", "MAPAI (Breakfast + Dinner)", 5, 3),
            _hotel("Rambagh Palace - Taj Luxury Group", "Jaipur", "02 Nights", "Ultra Luxury", "Royal Palace Room", "MAPAI + Private Royal Butler", 5, 4),
        ],
        inclusions=[
            _inc_included("Accommodation: 02 Nights stay at handpicked premium luxury properties.", 1),
            _inc_included("Meals: Daily multi-cuisine buffet breakfasts and premium dinners at designated hotels.", 2),
            _inc_included("Transfers & Sightseeing: All sightseeing via private Chauffeur-driven luxury sedan/SUV.", 3),
            _inc_included("TRAGUIN Support: 24/7 on-call concierge assistance and local guide service.", 4),
            _inc_included("Welcome Amenities: Royal traditional welcome with refreshing garland and premium mineral water.", 5),
            _inc_included("Complimentary Experiences: Cultural Entry and authentic Royal Dinner experience at Chokhi Dhani.", 6),
            _inc_excluded("Airfare or interstate train ticketing charges.", 7),
            _inc_excluded("Monument entry tickets, camera passes, and elephant/jeep ride costs.", 8),
            _inc_excluded("Personal expenses such as laundry, telephone billing, premium beverages, and tipping.", 9),
            _inc_excluded("Any early check-in or late check-out fees.", 10),
        ],
    )
    return package, itinerary


def build_rj_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "RJ-012"
    tour_code = "TRAGUIN-RJ-012"
    title = "Mount Abu Hill Station Delight"
    duration = "03 Nights / 04 Days"
    slug = "rj-012-mount-abu-hill-station-delight"
    itin_slug = "rj-012-mount-abu-hill-station-delight-itinerary"
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
            _ph("State / Country: Rajasthan, India | Category: Family Vacation / Hill Station", 2),
            _ph("Destinations: Mount Abu Hill Station", 3),
            _ph("Ideal for: Families, Couples, and Leisure Seekers", 4),
            _ph("Best season: October to March (Pleasant Year-Round)", 5),
            _ph("Vehicle: Private Chauffeur-driven Luxury SUV/Sedan", 6),
            _ph("Meal Plan: Modified American Plan (Daily Premium Breakfast & Dinners Included)", 7),
            _ph("Route Map: Abu Road Arrival → Mount Abu Exploration → Nakki Lake Cruise → Dilwara Temples → Departure", 8),
            _ph("TRAGUIN Curated Experience Note: Includes a private high-tea session overlooking the Nakki Lake, express passes to historic structures, luxury transportation, and 24/7 dedicated local concierge support.", 9),
            _ph("Shopping & Local Experiences: Local Markets: Nakki Lake Market and Rajasthan Government Emporium. Famous Items: Kota Doria sarees, hand-carved marble artifacts, traditional silver jewelry, and beautiful wooden toys. Food Recommendations: Authentic Rabdi (local sweet milk dessert) served hot near Nakki Lake.", 10),
            _ph("Important Notes: Hotel Policies: Standard check-in is at 14:00 hrs and check-out is at 11:00 hrs. Weather Note: Mount Abu remains refreshingly cool at night. A light jacket is recommended. Advance Booking Suggestions: High-season dates require prompt bookings for guaranteed space at ultra-luxury resorts.", 11),
        ],
        moods=["Family", "Hill Station", "Leisure"],
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
        tagline="Mount Abu Hill Station Delight • 03 Nights / 04 Days",
        overview=(
            "Escape into the serene mist-covered mountains of the Aravalli Range. Handcrafted perfectly by TRAGUIN experts, this exclusive Rajasthan Honeymoon Package and Rajasthan Family Tour showcases the gorgeous scenic beauty, unique culture, and iconic attractions of Rajasthan's only hill station. Enjoy absolute comfort, immersive experiences, and handpicked hotels tailored beautifully to generate unforgettable memories.\n\n"
            "TOUR OVERVIEW\n"
            "Vehicle Allocated: Private Chauffeur-driven Luxury SUV/Sedan\n"
            "Meal Plan: Modified American Plan (Daily Premium Breakfast & Dinners Included)\n"
            "Route Map: Abu Road Arrival → Mount Abu Exploration → Nakki Lake Cruise → Dilwara Temples → Departure\n\n"
            "TRAGUIN Curated Experience Note: Includes a private high-tea session overlooking the Nakki Lake, express passes to historic structures, luxury transportation, and 24/7 dedicated local concierge support.\n\n"
            "WHY VISIT MOUNT ABU? A PREMIUM RAJASTHAN EXPERIENCE\n"
            "Mount Abu stands proudly as an oasis in the desert state, offering a unique blend of Rajasthan Sightseeing, spiritual architecture, and cool refreshing breezes. Known for holding some of the Top Tourist Places in Rajasthan, it is the perfect spot for travelers seeking a Luxury Rajasthan Holiday away from the usual heritage city crowds.\n"
            "From the intricate, jaw-dropping architectural marvels of Dilwara Jain Temples to popular Instagram locations like Sunset Point and Honeymoon Point, this hill station is a panoramic paradise. The Best Time to Visit Rajasthan's lush mountain resort is during the pleasant cooler months, where the breathtaking landscapes are draped in soft, romantic mist. With our TRAGUIN Rajasthan Packages, your family receives absolute VIP convenience."
        ),
        seo_title="RJ-012 | Mount Abu Hill Station Delight | TRAGUIN",
        seo_description="Premium 03 Nights / 04 Days Rajasthan package (RJ-012 / TRAGUIN-RJ-012): Dilwara Jain Temples, Nakki Lake Cruise, Guru Shikhar, Achalgarh Fort, and 4-tier handpicked accommodation in Mount Abu.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Dilwara Jain Temples, Nakki Lake Cruise, Toad Rock, Sunset Point, Guru Shikhar Peak", 1),
            _ih("Achalgarh Fort, Achaleshwar Temple, Honeymoon Point sunset views", 2),
            _ih("TRAGUIN Signature Experience: Curated carefully by TRAGUIN experts", 3),
            _ih("Personalized Assistance: Dedicated chauffeur guide for smooth ground logistics", 4),
            _ih("Premium Handpicked Hotels: Properties selected based on premium hospitality scores", 5),
        ],
        days=[
            _day(
                1,
                "Abu Road to Mount Abu",
                (
                    "Arrive at Abu Road Railway Station or Udaipur Airport where your professional TRAGUIN driver will receive you warmly. Embark on a breathtaking, winding uphill drive surrounded by thick forests and jagged rocks. Upon reaching the cool heights of Mount Abu, complete a smooth check-in at your handpicked luxury resort. Spend your afternoon relaxing. In the evening, visit the beautiful Honeymoon Point to watch a stunning sunset drop below the valley lines, presenting incredible photography points."
                ),
                [
                    "Sightseeing Included: Scenic Hill Drive, Honeymoon Point Sunset view.",
                    "Evening Experience: Leisurely walks along the mist-kissed promenade pathways.",
                    "Overnight Stay: Handpicked Luxury Resort, Mount Abu.",
                    "Meals Included: Welcome Amenity Drink & Gourmet Dinner.",
                ],
            ),
            _day(
                2,
                "Mount Abu Cultural & Nature Tour",
                (
                    "Start your morning with a refreshing breakfast. Head out to explore the world-famous Dilwara Jain Temples, globally searched for their stunning marble carvings that date back to the 11th century. Afterward, take a peaceful stroll down to the sacred Nakki Lake, a legendary waterbody said to have been scooped out by the gods using their fingernails. Enjoy an exclusive private boating cruise over its tranquil waters. Conclude your day with a magical sunset experience at the iconic Sunset Point."
                ),
                [
                    "Sightseeing Included: Dilwara Jain Temples, Nakki Lake Cruise, Toad Rock, Sunset Point.",
                    "Optional Activities: Fun traditional horse riding or local street food tasting around Nakki Lake.",
                    "Overnight Stay: Handpicked Luxury Resort, Mount Abu.",
                    "Meals Included: Full Buffet Breakfast & Plated Multi-cuisine Dinner.",
                ],
            ),
            _day(
                3,
                "Highest Peak Exploration",
                (
                    "Drive up to Guru Shikhar, the highest peak in the entire Aravalli Range standing at 1,722 meters above sea level. Feel the clouds pass by you as you look out at panoramic vistas of the surrounding plains. Visit the ancient Dattatreya temple nestled at the apex. Later, explore the ruins of the 14th-century Achalgarh Fort and its famous Achaleshwar Mahadev Temple, known for its mystical naturally occurring features."
                ),
                [
                    "Sightseeing Included: Guru Shikhar Peak Observatory, Achalgarh Fort, Achaleshwar Temple.",
                    "Evening Experience: A curated cozy bonfire night arranged at your premium resort terrace.",
                    "Overnight Stay: Handpicked Luxury Resort, Mount Abu.",
                    "Meals Included: Full Breakfast & Dinner.",
                ],
            ),
            _day(
                4,
                "Departure from Mount Abu",
                (
                    "Enjoy a final sunrise breakfast at the resort courtyard. Relish the peaceful mountain climate one last time. Pack your bags and check out. Your premium private vehicle will transport you comfortably back down to Abu Road Station or Udaipur Airport for your journey home. Your elite TRAGUIN experience concludes beautifully."
                ),
                [
                    "Transfers Included: Private Luxury Airport / Station Drop-off.",
                    "Meals Included: Full Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel("Hotel Hilltone", "Mount Abu", "03 Nights", "Deluxe", "Superior Luxury Room", "MAPAI", 4, 1),
            _hotel("Cama Rajputana Club Resort", "Mount Abu", "03 Nights", "Premium", "Deluxe Garden View Room", "MAPAI", 4, 2),
            _hotel("The Hillock Resort", "Mount Abu", "03 Nights", "Luxury", "Premium Terrace Suite", "MAPAI", 5, 3),
            _hotel("WelcomHeritage Connaught House", "Mount Abu", "03 Nights", "Ultra Luxury", "Royal Heritage Suite", "MAPAI", 5, 4),
        ],
        inclusions=[
            _inc_included("Accommodation: 03 Nights stay at premium handpicked hotels matching your style.", 1),
            _inc_included("Meals: Daily multi-cuisine buffet breakfasts and dinners at the resort restaurant.", 2),
            _inc_included("Transfers & Sightseeing: Dedicated air-conditioned luxury transportation for all points.", 3),
            _inc_included("TRAGUIN Support: 24/7 priority professional assistance throughout the tour.", 4),
            _inc_included("Welcome Amenities: Cold towels, signature traditional sweet boxes, and complimentary bottled water.", 5),
            _inc_included("Complimentary Experiences: Private boat cruise ticket at Nakki Lake.", 6),
            _inc_excluded("Train tickets or flight airfare bookings.", 7),
            _inc_excluded("Direct entry tickets to temples/monuments unless specified.", 8),
            _inc_excluded("Optional tours, laundry, tips, and personal safari rides.", 9),
            _inc_excluded("Goods & Services Tax (GST) and personal travel insurance.", 10),
        ],
    )
    return package, itinerary


def build_rj_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "RJ-013"
    tour_code = "TRAGUIN-RJ-013"
    title = "Jodhpur Jaisalmer Desert Classic"
    duration = "05 Nights / 06 Days"
    slug = "rj-013-jodhpur-jaisalmer-desert-classic"
    itin_slug = "rj-013-jodhpur-jaisalmer-desert-classic-itinerary"
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
            _ph("State / Country: Rajasthan, India | Category: Family Vacation / Royal Luxury", 2),
            _ph("Destinations: Jodhpur • Jaisalmer • Thar Desert", 3),
            _ph("Ideal for: Families, Couples & Elite Groups", 4),
            _ph("Best season: October to March", 5),
            _ph("Vehicle: Private Air-Conditioned Luxury Innova Crysta / Luxury Coach", 6),
            _ph("Meal Plan: Modified American Plan (Buffet Breakfast & Elite Dinners Included)", 7),
            _ph("Route Map: Jodhpur Arrival → Blue City Sightseeing → Jaisalmer Golden City → Thar Desert Dune Camp → Jodhpur Departure", 8),
            _ph("TRAGUIN Curated Experience Note: Includes a private Royal Mehrangarh Fort curated guide, an exclusive private sunset camel safari over Sam Sand Dunes, authentic Rajasthani folk dance performances, and handpicked boutique heritage hotels.", 9),
            _ph("Shopping & Local Experiences: Jodhpur Markets: Purchase authentic Jodhpuri Jutis (leather footwear), hand-dyed Bandhani textiles, and exquisite silver artifacts. Jaisalmer Souvenirs: Bring home beautiful local yellow sandstone crafts, camel leather bags, and intricately woven rugs.", 10),
            _ph("Important Notes: Hotel Policies: Standard check-in time is 14:00 hrs and check-out is 11:00 hrs. Early access depends on premium hotel availability. Desert Weather: Desert temperatures drop pleasantly during winter evenings. Carrying premium light layers and shawls is highly advised. Advance Booking: Luxury desert camps and palace properties experience high demand; advance reservations are highly recommended.", 11),
        ],
        moods=["Family", "Royal", "Desert"],
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
        tagline="Jodhpur • Jaisalmer Desert Classic — 05 Nights / 06 Days",
        overview=(
            "Step into a golden era of timeless royalty, grand fortresses, and shifting sand dunes. Crafted into perfection by travel artisans at TRAGUIN, this ultra-luxury Rajasthan Honeymoon Package and family getaway connects you with the blue-hued alleys of Jodhpur and the majestic desert horizons of Jaisalmer. Expect bespoke hospitality, premium stays, and an emotionally moving journey through India's regal past.\n\n"
            "TOUR OVERVIEW\n"
            "Vehicle Allocated: Private Air-Conditioned Luxury Innova Crysta / Luxury Coach\n"
            "Meal Plan: Modified American Plan (Buffet Breakfast & Elite Dinners Included)\n"
            "Route Map: Jodhpur Arrival → Blue City Sightseeing → Jaisalmer Golden City → Thar Desert Dune Camp → Jodhpur Departure\n\n"
            "TRAGUIN Curated Experience Note: Includes a private Royal Mehrangarh Fort curated guide, an exclusive private sunset camel safari over Sam Sand Dunes, authentic Rajasthani folk dance performances, and handpicked boutique heritage hotels.\n\n"
            "PREMIUM RAJASTHAN EXPERIENCE & HIGHLIGHTS\n"
            "For travelers seeking the ultimate Rajasthan Family Tour or an unforgettable Luxury Rajasthan Holiday, this dynamic circuit unrolls premium travel encounters across the state's most sought-after landmarks. From capturing iconic Instagram-worthy vistas at the glowing golden fort of Jaisalmer to experiencing immersive heritage walks through Jodhpur's ancient quarters, our curated itinerary blends flawless hospitality with high-end cultural storytelling.\n"
            "Discover why the cooler months represent the Best Time to Visit Rajasthan. Our TRAGUIN Rajasthan Packages feature handpicked luxury desert camps, exquisite candlelight dinners under stargazing desert skies, and access to elite local markets overflowing with traditional souvenirs and vibrant textiles."
        ),
        seo_title="RJ-013 | Jodhpur Jaisalmer Desert Classic | TRAGUIN",
        seo_description="Premium 05 Nights / 06 Days Rajasthan package (RJ-013 / TRAGUIN-RJ-013): Mehrangarh Fort, Jaisalmer Golden Fort, Sam Sand Dunes camel safari, Patwon-ki-Haveli, and 4-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Mehrangarh Fort, Jaswant Thada, Umaid Bhawan Palace Museum, Gadisar Lake", 1),
            _ih("Jaisalmer Golden Fort, Patwon-ki-Haveli, Sam Sand Dunes sunset camel safari", 2),
            _ih("TRAGUIN Signature Experience: Curated by TRAGUIN Experts with private check-ins and seamless desert coordination", 3),
            _ih("Private sunset camel ride safari and Rajasthani musical evening at the dunes", 4),
            _ih("Premium handpicked luxury accommodations across Jodhpur, Jaisalmer, and Thar Desert", 5),
        ],
        days=[
            _day(1, "Jodhpur Arrival", "Your premium Rajasthan holiday begins as you land in the historical city of Jodhpur. A dedicated chauffeur-driven luxury vehicle arranged by TRAGUIN will greet you for a comfortable transfer to your premier handpicked heritage hotel. Following a smooth check-in, spend your afternoon relaxing. In the evening, visit the vibrant old markets surrounding the iconic Clock Tower, exploring authentic local handicrafts and multi-hued textiles.", ["Sightseeing Included: Ghanta Ghar (Clock Tower), Sadar Market Heritage Walk.", "Food Suggestions: Taste Jodhpur's legendary Makhaniya Lassi and hot Mawa Kachori at heritage sweet shops.", "Overnight Stay: Handpicked Luxury Heritage Hotel, Jodhpur.", "Meals Included: Welcome Amenities & Gourmet Dinner."]),
            _day(2, "Jodhpur Sightseeing", "Savor a luxurious buffet breakfast before setting off for a full-day Jodhpur Sightseeing tour. Ascend to the breathtaking Mehrangarh Fort, standing majestically over the city skyline. Walk through the exquisite courts of Moti Mahal and Phool Mahal accompanied by an expert historian. Later, explore the serene white-marble cenotaph of Jaswant Thada, often referred to as the Taj Mahal of Marwar, followed by the grand royal museum at Umaid Bhawan Palace.", ["Sightseeing Included: Mehrangarh Fort, Jaswant Thada, Umaid Bhawan Palace Museum.", "Photography Points: Capture the stunning panoramas of blue houses from the ramparts of Mehrangarh Fort.", "Overnight Stay: Handpicked Luxury Heritage Hotel, Jodhpur.", "Meals Included: Full Breakfast & Royal Marwari Dinner."]),
            _day(3, "Jodhpur to Jaisalmer", "Embark on a scenic luxury drive across the scenic landscape of the Thar desert heading toward Jaisalmer. Watch the terrain transform into shimmering gold as you approach the city. Upon arrival, check in seamlessly to your premium luxury resort. As the evening sets in, enjoy a peaceful visit to Gadisar Lake, viewing its beautiful floating shrines casting golden reflections on the water.", ["Sightseeing Included: Gadisar Lake Evening Walk, Scenic Desert Highway.", "Evening Experience: Witness a traditional puppet show at the desert cultural center.", "Overnight Stay: Premium Luxury Resort, Jaisalmer.", "Meals Included: Breakfast & Dinner."]),
            _day(4, "Jaisalmer Fort & Thar Desert Dune Camp", "Spend your morning exploring the living marvel of Jaisalmer Fort (Sonal Quila), an extraordinary structure where thousands still reside inside the walls. Visit the legendary hand-carved stone architecture of Patwon-ki-Haveli and Nathmal-ki-Haveli. Post-lunch, transfer to your ultra-luxury tented camp at the Sam Sand Dunes. Climb aboard camels for an exclusive private sunset safari, followed by a vibrant evening of live folk music, Kalbeliya dances, and a lavish desert dinner beneath a sky full of stars.", ["Sightseeing Included: Jaisalmer Golden Fort, Patwon-ki-Haveli, Sam Sand Dunes.", "Optional Activities: Thrilling 4x4 Jeep Sand Dune Bashing over high crests.", "Overnight Stay: Ultra-Luxury Tented Desert Camp, Thar Desert.", "Meals Included: Breakfast & Traditional Rajasthani Feast Dinner."]),
            _day(5, "Thar Desert to Jodhpur Return", "Awake to a crisp, majestic desert sunrise and enjoy a warm gourmet breakfast at the camp. Board your luxury private transport to comfortably travel back to Jodhpur. Upon arrival, settle back into your premium stay for a relaxed afternoon. Your final evening is perfectly suited for dynamic local shopping or scheduling a premium wellness spa treatment at the hotel.", ["Sightseeing Included: Mandore Gardens (En Route), Leisure Evening.", "Overnight Stay: Premium Luxury Hotel, Jodhpur.", "Meals Included: Breakfast & Dinner."]),
            _day(6, "Jodhpur Departure", "Enjoy a relaxed morning breakfast looking over the hotel's palatial grounds. Your professional TRAGUIN chauffeur will arrive on time to transfer you smoothly to Jodhpur Airport or the Railway Station for your return flight home. Your elite royal holiday concludes, leaving you with unforgettable memories.", ["Transfers Included: Private Luxury Airport / Station Drop-off.", "Meals Included: Full Buffet Breakfast."]),
        ],
        hotels=[
            _hotel("Indana Palace / Fort Rajwada / Desert Springs Resort Tents", "Jodhpur / Jaisalmer / Thar Desert", "05 Nights", "Deluxe", "Heritage Room / Resort Room / Tents", "MAPAI", 4, 1),
            _hotel("Welcomhotel by ITC Hotels / Jaisalmer Marriott Resort / Le Seringapatam Luxury Camp", "Jodhpur / Jaisalmer / Thar Desert", "05 Nights", "Premium", "Deluxe Room / Resort Room / Luxury Camp", "MAPAI", 5, 2),
            _hotel("Taj Hari Mahal / Suryagarh Jaisalmer / The Serai (SUJÁN Luxury Camp)", "Jodhpur / Jaisalmer / Thar Desert", "05 Nights", "Luxury", "Luxury Room / Heritage Suite / Luxury Tent", "MAPAI", 5, 3),
            _hotel("Umaid Bhawan Palace (Taj) / Suryagarh Luxury Suite / SUJÁN Royal Oasis Tents", "Jodhpur / Jaisalmer / Thar Desert", "05 Nights", "Ultra Luxury", "Palace Room / Luxury Suite / Royal Oasis Tent", "MAPAI", 5, 4),
        ],
        inclusions=[
            _inc_included("Accommodation: 05 Nights stay at handpicked elite luxury hotels and desert camps.", 1),
            _inc_included("Meals: Daily multi-cuisine buffet breakfasts and premium dinners.", 2),
            _inc_included("Transfers & Sightseeing: Dedicated Chauffeur-driven luxury AC vehicle for transfers and sightseeing.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated guest concierge assistance and expert monuments guide fees.", 4),
            _inc_included("Complimentary Experiences: Private sunset camel ride safari and Rajasthani musical evening at the dunes.", 5),
            _inc_included("Welcome Amenities: Royal traditional welcoming garland greeting and premium hydration kit.", 6),
            _inc_excluded("Airfare or interstate luxury train tickets.", 7),
            _inc_excluded("Any camera fees, monument entry fees, or dynamic activity prices.", 8),
            _inc_excluded("Personal items such as premium beverages, laundry, and tips.", 9),
            _inc_excluded("4x4 Jeep dune bashing or extra safari rides not listed.", 10),
        ],
    )
    return package, itinerary


def build_rj_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "RJ-014"
    tour_code = "TRAGUIN-RJ-014"
    title = "Grand Marwar & Mewar Heritage"
    duration = "07 Nights / 08 Days"
    slug = "rj-014-grand-marwar-mewar-heritage"
    itin_slug = "rj-014-grand-marwar-mewar-heritage-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code, destination_id=destination_id,
        title=title, duration_label=duration, price=0, rating=Decimal("4.9"),
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Rajasthan, India | Category: Culture, Heritage & Luxury", 2),
            _ph("Destinations: Jaipur • Jodhpur • Udaipur", 3),
            _ph("Ideal for: Families, Couples & Heritage Travelers", 4),
            _ph("Best season: October to March (Winter Season)", 5),
            _ph("Travel Dates: Customizable As Per Request | Group / FIT: Private Customized FIT Tour", 6),
            _ph("Vehicle: Dedicated Chauffeur-Driven Luxury SUV (Innova Crysta)", 7),
            _ph("Meal Plan: CP AI (Daily Premium Buffet Breakfast)", 8),
            _ph("Route Details: Jaipur (3N) → Jodhpur (1N) → Udaipur (3N)", 9),
            _ph("TRAGUIN Curated Experience Note: This bespoke luxury itinerary seamlessly pairs iconic attractions with hidden local gems. Travel in absolute style with elite transportation, handpicked hotels, expert guides, and personalized assistance managed by TRAGUIN representatives at every step.", 10),
            _ph("Shopping & Local Experiences: Jaipur Bazaars: Johari Bazaar (famous for fine Kundan jewelry) and Bapu Bazaar (renowned for authentic block-print textiles, bandhani fabrics, and leather mojris). Jodhpur Markets: Clock Tower Market (renowned for premium Mathania red chilies, hand-woven carpets, and antique wooden artifacts). Udaipur Crafts: Hathi Pol Bazaar (best for traditional Pichwai paintings, camel-bone artifacts, and vibrant Rajasthani souvenirs).", 11),
            _ph("Important Notes: Hotel Policies: Standard check-in time is 14:00 hrs and check-out is 11:00/12:00 hrs. Early access or late checks are purely subject to availability. Weather Notes: Day temperatures are pleasantly warm and sunny, while winter nights can become cold. Carrying light jackets or pashmina shawls is strongly advised. Transport Rules: Luggage capacity is restricted to a maximum of 3 large bags and 2 small hand bags per luxury SUV vehicle. Advance Booking Suggestions: Top luxury palace properties require bookings 3–4 months in advance during peak tourism season.", 12),
        ],
        moods=["Culture", "Heritage", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title, duration_label=duration,
        duration_days=_duration_days(duration), starting_price=0, price_note="On Request (Premium Class)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Grand Marwar & Mewar Heritage • 07 Nights / 08 Days",
        overview=(
            "Welcome Note: Experience the timeless royalty, sand-swept fortresses, and shimmering lakeside palaces with the ultimate Luxury Rajasthan Holiday. Meticulously designed by TRAGUIN, this masterfully tailored itinerary takes you through the heart of India's most iconic royal states. From the pink-hued historical avenues of Jaipur to the blue-bricked alleys of Jodhpur and the pristine romantic waters of Udaipur, immerse your senses in an unforgettable journey filled with premium stays and curated experiences that redefine heritage luxury.\n\n"
            "TOUR OVERVIEW\nTravel Dates: Customizable As Per Request\nGroup / FIT: Private Customized FIT Tour\nVehicle Allocated: Dedicated Chauffeur-Driven Luxury SUV (Innova Crysta)\nMeal Plan: CP AI (Daily Premium Buffet Breakfast)\nRoute Details: Jaipur (3N) → Jodhpur (1N) → Udaipur (3N)\n\n"
            "TRAGUIN Curated Experience Note: This bespoke luxury itinerary seamlessly pairs iconic attractions with hidden local gems. Travel in absolute style with elite transportation, handpicked hotels, expert guides, and personalized assistance managed by TRAGUIN representatives at every step.\n\n"
            "WHY VISIT RAJASTHAN? A PREMIUM CULTURAL MASTERPIECE\nRajasthan stands as India's premier luxury travel destination, blending ancient royal legacies with breathtaking landscapes. As the most sought-after choice for a Rajasthan Honeymoon Package or a memorable Rajasthan Family Tour, this majestic land captures hearts with its monumental architecture, vibrant desert bazaars, and legendary hospitality.\n"
            "During this spectacular Rajasthan Sightseeing journey, travelers explore the Top Tourist Places in Rajasthan—from the magnificent Amber Fort in Jaipur to the towering Mehrangarh Fort in Jodhpur and the ethereal Lake Palace in Udaipur. Perfect for capturing popular Instagram locations, experiencing rich Rajasthani culture, traditional puppet shows, and exploring artisanal shopping hubs, these elite TRAGUIN Rajasthan Packages promise absolute luxury and immersive experiences. The Best Time to Visit Rajasthan is during the pleasant winter months, ensuring a highly comfortable, grand Premium Rajasthan Experience."
        ),
        seo_title="RJ-014 | Grand Marwar & Mewar Heritage | TRAGUIN",
        seo_description="Premium 07 Nights / 08 Days Rajasthan package (RJ-014 / TRAGUIN-RJ-014): Jaipur, Jodhpur, Udaipur heritage circuit, Amber Fort, Mehrangarh Fort, Lake Pichola cruise, and 4-tier handpicked accommodation.",
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Amber Fort, Jal Mahal, Hawa Mahal, City Palace, Jantar Mantar, Mehrangarh Fort, Ranakpur Jain Temple", 1),
            _ih("Udaipur City Palace, Jagdish Temple, Saheliyon-ki-Bari, Lake Pichola boat cruise", 2),
            _ih("Sajjangarh Monsoon Palace, Vintage Car Museum, Fatehsagar Lake Drive", 3),
            _ih("TRAGUIN Signature Experience: Handcrafted to ensure zero-stress luxury with direct lane entries and elite vehicle configurations", 4),
            _ih("Private sunset boat cruise on Lake Pichola in Udaipur & TRAGUIN support available 24/7", 5),
        ],
        days=[
            _day(1, "Jaipur", "Arrive at the Jaipur International Airport or Railway Station where your elite TRAGUIN driver and tour coordinator warmly greet you. Board your private luxury vehicle and transfer directly to your handpicked premium heritage hotel. After a smooth, priority check-in, unwind in your royal suite. In the evening, step out for an introductory drive across the brilliantly illuminated pink-hued bazaars or choose to visit Chokhi Dhani for an authentic ethnic village dining experience filled with folk dances and cultural storytelling.", ["Sightseeing Included: Private Airport Transfer, Evening Bazaar Drive.", "Evening Experience: Traditional welcome high-tea hosted at your luxury heritage property.", "Overnight Stay: Handpicked Luxury Heritage Hotel, Jaipur.", "Meals Included: Welcome Drink."]),
            _day(2, "Jaipur", "Savor a luxurious breakfast before embarking on a full day of comprehensive Jaipur Sightseeing. Your first stop is the majestic Amber Fort, perched high on a hill. Enjoy an elite, comfortable ascent up the fort's ancient ramparts. Walk through the stunning Sheesh Mahal (Mirror Palace), listening to historical tales narrated by your expert local guide. Stop for iconic photography points at the water-bound Jal Mahal before heading to the intricate, multi-windowed facade of the world-famous Hawa Mahal (Palace of Winds).", ["Sightseeing Included: Amber Fort, Jal Mahal, Hawa Mahal, Royal Gaitor Cenotaphs.", "Optional Activities: An evening hot air balloon ride overlooking the ancient Aravalli peaks.", "Overnight Stay: Handpicked Luxury Heritage Hotel, Jaipur.", "Meals Included: Premium Buffet Breakfast."]),
            _day(3, "Jaipur", "Continue your deep cultural immersion into the Pink City by visiting the magnificent City Palace Complex, a living royal residence boasting an spectacular blend of Mughal and Rajput architecture. Walk through the private inner courtyards to view the highly searched Instagram location—the Peacock Gate. Right next door, explore the legendary Jantar Mantar, a UNESCO World Heritage site housing the world's largest stone astronomical sundial. Spend the evening browsing bustling local markets for precious gemstones and handcrafted goods.", ["Sightseeing Included: City Palace, Jantar Mantar Observatory, Albert Hall Museum.", "Local Experiences: Private block-printing workshop with national-award-winning master artisans.", "Overnight Stay: Handpicked Luxury Heritage Hotel, Jaipur.", "Meals Included: Premium Buffet Breakfast."]),
            _day(4, "Jaipur to Jodhpur", "Bid farewell to Jaipur after a hearty breakfast and travel comfortably across breathtaking landscapes towards Jodhpur, famously known as the Sun City or Blue City. Upon arrival, catch your first glimpse of the massive Mehrangarh Fort towering over the city's blue-painted skyline. Check into your premium stay and relax. In the late afternoon, enjoy a curated heritage walk through the ancient clock tower area (Ghanta Ghar) and the vibrant, spice-scented Sadar Bazaar.", ["Sightseeing Included: Intercity Luxury Transfer, Ghanta Ghar Heritage Walk, Sadar Bazaar.", "Food Suggestions: Taste the legendary local Makhaniya Lassi and spicy Shahi Samosas at iconic sweet shops.", "Overnight Stay: Premium Luxury Palace Hotel, Jodhpur.", "Meals Included: Premium Buffet Breakfast."]),
            _day(5, "Jodhpur to Udaipur", "Begin your morning with an exclusive tour of the towering Mehrangarh Fort, one of India's largest and most impeccably preserved fortresses. Explore its opulent palaces, including Moti Mahal and Phool Mahal, housing an incredible collection of royal palanquins and armaments. Next, visit the serene white marble cenotaph at Jaswant Thada, often referred to as the Taj Mahal of Marwar. Later, check out and drive towards Udaipur, pausing en route to marvel at the awe-inspiring, intricately carved pillars of the 15th-century Ranakpur Jain Temple.", ["Sightseeing Included: Mehrangarh Fort, Jaswant Thada, Ranakpur Jain Temple Complex.", "Photography Points: Capturing the sweeping blue city panoramic view from Mehrangarh's highest rampart.", "Overnight Stay: Handpicked Luxury Lakeside Resort, Udaipur.", "Meals Included: Premium Buffet Breakfast."]),
            _day(6, "Udaipur", "Awake to the mist rising off Lake Pichola. Today's immersive experiences focus entirely on the romantic jewel of Mewar—Udaipur. Visit the colossal City Palace, India's largest palace complex, standing beautifully along the lake's eastern shore. Wander through its museums, royal courtyards, and hanging gardens. Next, pay respects at the historic 17th-century Jagdish Temple, followed by a relaxing stroll around Saheliyon-ki-Bari (Courtyard of the Maidens), famous for its lush marble fountains and lotus ponds.", ["Sightseeing Included: Udaipur City Palace, Jagdish Temple, Saheliyon-ki-Bari.", "Evening Experience: An exclusive private boat cruise on Lake Pichola, floating past Jag Mandir Palace during a golden sunset.", "Overnight Stay: Handpicked Luxury Lakeside Resort, Udaipur.", "Meals Included: Premium Buffet Breakfast."]),
            _day(7, "Udaipur", "Drive up the winding hills to the hilltop Sajjangarh Monsoon Palace, offering a stunning panoramic vista of Udaipur's surrounding lakes and countryside. In the afternoon, explore the exclusive Vintage & Classic Car Collection Museum, housing a rare array of classic vehicles once owned by the Maharanas of Udaipur. Spend your final evening enjoying a premium lakeside fine-dining experience arranged elegantly by TRAGUIN experts to celebrate your unforgettable memories.", ["Sightseeing Included: Sajjangarh Fort, Vintage Car Museum, Fatehsagar Lake Drive.", "Optional Activities: Attending the Dharohar Live Folk Dance Performance at Bagore-ki-Haveli.", "Overnight Stay: Handpicked Luxury Lakeside Resort, Udaipur.", "Meals Included: Premium Buffet Breakfast & Farewell Lakeside Dinner."]),
            _day(8, "Udaipur Departure", "Indulge in a relaxed, lavish breakfast at your lakeside resort while soaking in the peaceful morning views. At the scheduled hour, your luxury private vehicle arrives to transfer you smoothly to the Udaipur Airport or Railway Station for your return flight home. Your exceptional TRAGUIN Rajasthan Package draws to a close, leaving you with cherished, lifelong royal memories.", ["Transfers Included: Private Luxury Airport / Station Drop-off.", "Meals Included: Premium Buffet Breakfast."]),
        ],
        hotels=[
            _hotel("Mandawa Haveli / Shahpura House / Ranbanka Palace / Indana Palace / Amet Haveli / Radisson Blu Palace", "Jaipur / Jodhpur / Udaipur", "07 Nights", "Deluxe", "Heritage Room / Palace Room / Lakeside Room", "CP AI", 4, 1),
            _hotel("ITC Rajputana / Hilton Jaipur / Welcomhotel by ITC Hotels Jodhpur / The Ananta Resort / Trident Udaipur", "Jaipur / Jodhpur / Udaipur", "07 Nights", "Premium", "Executive Room / Deluxe Room / Resort Room", "CP AI", 5, 2),
            _hotel("The Raj Palace / Jai Mahal Palace / Ajit Bhawan Palace / Raas Jodhpur / The Leela Palace / Taj Lake Palace", "Jaipur / Jodhpur / Udaipur", "07 Nights", "Luxury", "Palace Suite / Heritage Suite / Lake View Suite", "CP AI", 5, 3),
            _hotel("Rambagh Palace (Taj Group) / Umaid Bhawan Palace (Taj Group) / The Oberoi Udaivilas", "Jaipur / Jodhpur / Udaipur", "07 Nights", "Ultra Luxury", "Royal Suite / Palace Room / Kohinoor Suite", "CP AI", 5, 4),
        ],
        inclusions=[
            _inc_included("Accommodation: 07 Nights stay in premier double/twin sharing rooms at handpicked elite hotels.", 1),
            _inc_included("Meals: 07 Extensive Premium Buffet Breakfasts at hotel restaurants.", 2),
            _inc_included("Transfers & Sightseeing: Dedicated Chauffeur-driven AC Luxury Toyota Innova Crysta for all airport, intercity, and local sightseeing transfers.", 3),
            _inc_included("Assistance: Personalized Meet & Greet by TRAGUIN representatives during arrival and departures.", 4),
            _inc_included("Taxes: All applicable luxury hotel taxes, toll taxes, fuel charges, state permits, and driver allowances.", 5),
            _inc_included("Welcome Amenities: Royal welcoming traditional garland, customized travel itinerary kit, and daily packaged mineral water bottles.", 6),
            _inc_included("Complimentary Experiences: A private sunset boat cruise on Lake Pichola in Udaipur & TRAGUIN support available 24/7.", 7),
            _inc_excluded("Airfare or Train tickets to Jaipur and from Udaipur.", 8),
            _inc_excluded("Main entry monuments tickets, guide fees, and camera tickets during sightseeing.", 9),
            _inc_excluded("Personal expenses such as laundry, phone calls, alcoholic or premium beverages, and tips.", 10),
            _inc_excluded("Any adventure activities, elephant rides, or optional tour upgrades not listed in the inclusions.", 11),
            _inc_excluded("Comprehensive travel insurance or medical coverage costs.", 12),
        ],
    )
    return package, itinerary


def build_rj_015(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "RJ-015"
    tour_code = "TRAGUIN-RJ-015"
    title = "Pushkar Camel Fair Experience"
    duration = "03 Nights / 04 Days"
    slug = "rj-015-pushkar-camel-fair-experience"
    itin_slug = "rj-015-pushkar-camel-fair-experience-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code, destination_id=destination_id,
        title=title, duration_label=duration, price=0, rating=Decimal("4.9"),
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Rajasthan, India | Category: Culture & Festivals", 2),
            _ph("Destinations: Pushkar • Ajmer", 3),
            _ph("Ideal for: Cultural Explorers, Families & Photographers", 4),
            _ph("Best season: November (Fair Dates)", 5),
            _ph("Travel Dates: Dynamic (November Fair Framework) | Group / FIT: Customized Private Luxury FIT Tour", 6),
            _ph("Vehicle: Dedicated Chauffeur-driven AC Luxury Sedan / Innova Crysta", 7),
            _ph("Meal Plan: Modified American Plan (Daily Premium Breakfast & Dinners)", 8),
            _ph("Route Map: Jaipur / Ajmer Arrival → Pushkar Desert Fair Grounds → Ajmer Sharif → Departure", 9),
            _ph("TRAGUIN Curated Experience: VIP seating at cultural events & private camel safari sunset high-tea.", 10),
            _ph("Shopping & Local Experiences: Local Markets: Pushkar Bazaars, Sarafa Bazaar, and Sadar Bazaar. Famous Shopping Items: Silver tribal jewelry, block-print textiles, leather camel goods, rose water oils, and terracotta pottery. Instagram Spots: Colorful camel herds, Brahma temple gates, Varaha Ghat lakeside mirrors, and sand dunes at dusk.", 11),
            _ph("Important Notes: Hotel Policies: Check-in time opens from 14:00 hours; check-out finishes at 11:00 hours. Pre-booking guarantees promptness. Weather Notes: Day conditions are warmly sunny while evening desert temperatures decrease swiftly. Carry light cardigans. Advance Booking Suggestions: Due to extreme global search volumes for the Pushkar Fair, advanced token payments are highly recommended.", 12),
        ],
        moods=["Culture", "Festivals", "Family"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title, duration_label=duration,
        duration_days=_duration_days(duration), starting_price=0, price_note="On Request (Premium Class)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Pushkar Camel Fair Experience • 03 Nights / 04 Days",
        overview=(
            "Step into a vibrant kaleidoscope of culture, heritage, and timeless spirituality. Carefully crafted by TRAGUIN, this premium Rajasthan Honeymoon Package and Rajasthan Family Tour brings you face-to-face with the legendary Pushkar Camel Fair. Experience the dramatic desert landscapes, thousands of beautifully adorned camels, nomadic folklore, and luxury tented premium stays that will fill your heart with unforgettable memories.\n\n"
            "TOUR OVERVIEW\nTravel Dates: Dynamic (November Fair Framework)\nGroup / FIT: Customized Private Luxury FIT Tour\nVehicle Allocated: Dedicated Chauffeur-driven AC Luxury Sedan / Innova Crysta\nMeal Plan: Modified American Plan (Daily Premium Breakfast & Dinners)\nRoute Map: Jaipur / Ajmer Arrival → Pushkar Desert Fair Grounds → Ajmer Sharif → Departure\n\n"
            "TRAGUIN Curated Experience: VIP seating at cultural events & private camel safari sunset high-tea.\n\n"
            "PREMIUM RAJASTHAN EXPERIENCE & FAIR INSIGHTS\nThe sacred town of Pushkar hosts the world-famous Pushkar Camel Fair, which stands out as one of the most searched iconic attractions and popular Instagram locations globally. When planning a Luxury Rajasthan Holiday, understanding the Best Time to Visit Rajasthan points directly to this November festival, where thousands of pastoralists gather under a full moon desert sky.\n"
            "From capturing rich adventure photography of traditional turban-tying or mustache competitions to engaging in spiritual Rajasthan Sightseeing along the 52 holy ghats of the sacred Pushkar Lake, our handpicked hotels and luxury desert camps ensure an immersive experience. Discover top tourist places in Rajasthan through an expert travel consultant tone, designed meticulously with zero-hassle logistical flow."
        ),
        seo_title="RJ-015 | Pushkar Camel Fair Experience | TRAGUIN",
        seo_description="Premium 03 Nights / 04 Days Rajasthan package (RJ-015 / TRAGUIN-RJ-015): Pushkar Camel Fair, Brahma Temple, Ajmer Sharif Dargah, private camel safari, and 4-tier handpicked accommodation.",
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Pushkar Camel Fair immersion, camel exhibition fields, cultural amphitheater grounds", 1),
            _ih("Jagatpita Brahma Temple, Pushkar Lake Ghats, Ajmer Sharif Dargah, Ana Sagar Lake", 2),
            _ih("TRAGUIN Signature Experience: Private entry access passes to traditional sand-dune cultural show arenas", 3),
            _ih("Private sunset camel safari ride followed by luxury dune high-tea", 4),
            _ih("Curated by TRAGUIN Experts: Handpicked accommodations selected carefully for ultimate comfort and heritage proximity", 5),
        ],
        days=[
            _day(1, "Arrival & Desert Transition", "Arrive at Jaipur International Airport or Ajmer Railway Station, where a premium greeting arranged by TRAGUIN awaits you. Drive comfortably through the breathtaking landscapes of the Aravalli range to arrive at the sacred desert enclave of Pushkar. Check into your ultra-luxury handpicked desert camp or boutique luxury resort. In the late afternoon, witness the spectacular opening sights of the fairgrounds as herds of decorated camels cover the sand dunes.", ["Sightseeing Included: Fairground Orientation, Desert Sunset Views.", "Evening Experience: Gather around a private bonfire to enjoy traditional Rajasthani Kalbelia dance and live folk musicians.", "Overnight Stay: Handpicked Luxury Desert Camp / Premium Resort, Pushkar.", "Meals Included: Traditional Royal Welcome Drink & Festive Buffet Dinner."]),
            _day(2, "Pushkar Camel Fair Immersion", "Awake early for a crisp desert sunrise. Today you dive deep into the cultural core of the iconic attractions. Spend the morning wandering through the colorful trading fields, interacting with nomadic traders and craftsmen. In the afternoon, embark on an exclusive private camel caravan safari across the golden dunes, culminating in a luxury sunset high-tea prepared specially by our local handlers. Witness standard heritage contests such as the matching turban displays and tribal dance rituals.", ["Sightseeing Included: Camel Exhibition Fields, Cultural Amphitheater Grounds.", "Photography Points: Vibrant colorful crowds, traditional camel decor, and panoramic sand dunes against the setting sun.", "Overnight Stay: Luxury Desert Camp / Premium Resort, Pushkar.", "Meals Included: Premium Breakfast & Dinner."]),
            _day(3, "Holy Pushkar & Ajmer Heritage", "Devote your morning to the rich spiritual heritage of Pushkar. Visit the legendary Brahma Temple, one of the very few existing temples in the world dedicated to Lord Brahma. Take a peaceful walking tour along the sacred Pushkar Lake Ghats to witness ancient prayer chants. In the afternoon, enjoy a short comfortable drive to Ajmer to experience the profound spiritual acoustics of the world-renowned Dargah Sharif of Khwaja Moinuddin Chishti, a sanctuary visited by millions seeking blessings.", ["Sightseeing Included: Jagatpita Brahma Temple, Pushkar Lake Ghats, Ajmer Sharif Dargah, Ana Sagar Lake.", "Food Suggestions: Taste the famous hot local Malpua and crispy Rabdi sweet treats at heritage bazaars.", "Overnight Stay: Premium Luxury Resort, Pushkar.", "Meals Included: Premium Breakfast & Dinner."]),
            _day(4, "Departure from Desert Realms", "Savor your final luxury breakfast while taking in panoramic views of the desert sands. Before departure, explore the local artisanal stalls to buy handicraft souvenirs. Your private luxury vehicle will then smoothly transfer you to Jaipur Airport or Ajmer Railway Station for your journey homeward, concluding a highly elite and immersive heritage holiday experience.", ["Transfers Included: Private Departure Airport / Station Drop-off.", "Meals Included: Full Buffet Breakfast."]),
        ],
        hotels=[
            _hotel("Pushkar Resort / Aaram Baagh", "Pushkar", "03 Nights", "Deluxe", "Deluxe Heritage Room", "MAPAI", 4, 1),
            _hotel("The Westin Pushkar Resort & Spa", "Pushkar", "03 Nights", "Premium", "Premium Luxury Villa", "MAPAI", 5, 2),
            _hotel("Greenhouse Resort Pushkar", "Pushkar", "03 Nights", "Luxury", "Luxury Air-Conditioned Canvas Tent", "MAPAI", 5, 3),
            _hotel("Taj Pratap Mahal / Orchard Tents Pushkar", "Pushkar", "03 Nights", "Ultra Luxury", "Royal Heritage Suite / Signature Tent", "MAPAI", 5, 4),
        ],
        inclusions=[
            _inc_included("Accommodation: 03 Nights accommodation in handpicked hotels or luxury camps.", 1),
            _inc_included("Meals: Daily premium breakfast buffet and royal curated dinners as specified.", 2),
            _inc_included("Transfers & Sightseeing: Dedicated Chauffeur-driven private luxury sedan / SUV vehicle.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated local concierge and professional companion field guides.", 4),
            _inc_included("Welcome Amenities: Royal traditional garland welcoming, mineral water bottles, and handpicked local mementos.", 5),
            _inc_included("Complimentary Experiences: Private sunset camel safari ride followed by luxury dune high-tea.", 6),
            _inc_included("Taxes: All toll taxes, fuel charges, state permissions, and parking expenses.", 7),
            _inc_excluded("Airfare or interstate railway booking tickets to Rajasthan.", 8),
            _inc_excluded("Individual entry monuments or inner camera ticket passes.", 9),
            _inc_excluded("Personal nature services: laundry bills, souvenir retail, premium spirits, tipping.", 10),
            _inc_excluded("Alternative optional tours or extra vehicle transit distance requests.", 11),
            _inc_excluded("Medical or personal travel insurance protocols.", 12),
        ],
    )
    return package, itinerary


def build_rj_016(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "RJ-016"
    tour_code = "TRAGUIN-RJ-016"
    title = "Ajmer Sharif Divine Blessing & Shrinathji Sacred Darshan Express"
    duration = "03 Nights / 04 Days"
    slug = "rj-016-ajmer-sharif-shrinathji-sacred-darshan-express"
    itin_slug = "rj-016-ajmer-sharif-shrinathji-sacred-darshan-express-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code, destination_id=destination_id,
        title=title, duration_label=duration, price=0, rating=Decimal("4.9"),
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Rajasthan, India | Category: Luxury Pilgrimage & Devotion", 2),
            _ph("Destinations: Udaipur • Nathdwara (Shrinathji) • Ajmer Sharif • Pushkar", 3),
            _ph("Ideal for: Families, Couples & Senior Pilgrims", 4),
            _ph("Best season: October to March", 5),
            _ph("Vehicle: Private AC Luxury Innova Crysta / Premium Chauffeur Sedan", 6),
            _ph("Meal Plan: Modified American Plan (Gourmet Breakfast & Dinners Included)", 7),
            _ph("Route Map: Udaipur Arrival → Nathdwara → Pushkar Holy Lake → Ajmer Sharif Dargah → Jaipur / Udaipur Departure", 8),
            _ph("TRAGUIN Curated Experience Note: This exclusive spiritual journey focuses on VIP skip-the-line assistance where applicable, highly professional travel companion coordination, zero-hassle check-ins, and meticulously handpicked hotels optimized for premium physical comfort.", 9),
            _ph("Shopping & Local Souvenirs: Nathdwara Markets: Purchase highly searched traditional Pichwai paintings, intricate silver ornaments, and local terracotta handicrafts. Pushkar Bazaars: Famous for aromatic rose water, pure rose oils, camel leather artifacts, and ethnic silver jewelry souvenirs.", 10),
            _ph("Important Notes: Hotel Policies: Standard hotel check-in time is 14:00 hours; check-out is 11:00 hours. Early allocations are managed by TRAGUIN based on availability. Dress Code Guidelines: Modest traditional attire covering shoulders and knees is strictly mandatory for entries inside Ajmer Sharif Dargah and Shrinathji Temple. Headcover scarves are required for all pilgrims.", 11),
        ],
        moods=["Pilgrimage", "Spiritual", "Family"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title, duration_label=duration,
        duration_days=_duration_days(duration), starting_price=0, price_note="On Request (Premium Class)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Ajmer Sharif Divine Blessing & Shrinathji Sacred Darshan Express",
        overview=(
            "Embark on a soul-stirring spiritual odyssey across the royal land of Rajasthan. Thoughtfully curated by TRAGUIN experts, this premium package bridges two of the most iconic spiritual sanctuaries of India—the mystical divine court of Hazrat Khwaja Moinuddin Chishti at Ajmer Sharif and the enchanting, ornate palace temple of Shrinathji at Nathdwara. Experience absolute spiritual bliss wrapped completely in majestic comfort, premium stays, and seamless logistics.\n\n"
            "TOUR OVERVIEW\nVehicle Allocated: Private AC Luxury Innova Crysta / Premium Chauffeur Sedan\nMeal Plan: Modified American Plan (Gourmet Breakfast & Dinners Included)\nRoute Map: Udaipur Arrival → Nathdwara → Pushkar Holy Lake → Ajmer Sharif Dargah → Jaipur / Udaipur Departure\n\n"
            "TRAGUIN Curated Experience Note: This exclusive spiritual journey focuses on VIP skip-the-line assistance where applicable, highly professional travel companion coordination, zero-hassle check-ins, and meticulously handpicked hotels optimized for premium physical comfort.\n\n"
            "WHY BOOK THE BEST RAJASTHAN TOUR PACKAGE?\nRajasthan is not just a land of palaces and deserts; it is home to some of the country's most searched holy destinations. For multi-generational families planning a highly rewarding Rajasthan Family Tour or couples seeking a meaningful Rajasthan Honeymoon Package, this route balances serene architecture with timeless mystical legacies.\n"
            "By selecting this Luxury Rajasthan Holiday, you guarantee smooth transfers between the pristine lakeside palaces of Udaipur, the vibrant bustling bazaar surroundings of Ajmer, and the peaceful sacred spiritual atmosphere of Pushkar. Our specialized TRAGUIN Rajasthan Packages feature handpicked luxury hotels, exceptional local insight, and breathtaking landscapes that turn a simple holiday into a repository of unforgettable memories."
        ),
        seo_title="RJ-016 | Ajmer Sharif Divine Blessing & Shrinathji Sacred Darshan Express | TRAGUIN",
        seo_description="Premium 03 Nights / 04 Days Rajasthan pilgrimage package (RJ-016 / TRAGUIN-RJ-016): Shrinathji Temple, Pushkar Lake, Brahma Temple, Ajmer Sharif Dargah, and 4-tier handpicked accommodation.",
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Shrinathji Temple Darshan, Nathdwara Local Bazaar, Pushkar Lake, Lord Brahma Temple", 1),
            _ih("Ajmer Sharif Dargah, Ana Sagar Lake, Adhai Din Ka Jhonpra", 2),
            _ih("TRAGUIN Signature Experience: Curated by TRAGUIN Experts with specialized assistance during holy crowd peak hours", 3),
            _ih("Savitri Temple via comfortable ropeway and optional Ana Sagar Lake boat cruise", 4),
            _ih("Handpicked premium stays, high-end private vehicle transfers, and localized professional support", 5),
        ],
        days=[
            _day(1, "Arrival Udaipur to Nathdwara", "Arrive at Udaipur Airport or Railway Station, where a premium TRAGUIN guest representative warmly welcomes you. Board your private luxury vehicle and transfer through scenic rocky valley routes toward the holy town of Nathdwara. Check in smoothly at your ultra-premium hotel. In the afternoon, proceed to the Shrinathji Temple for a highly immersive experience of the 'Shringar' or 'Utthapan' Darshan of Lord Krishna depicted as a 7-year-old child lifting the Govardhan hill. Stroll around the vibrant local craft temple square afterwards.", ["Sightseeing Included: Shrinathji Temple Darshan, Nathdwara Local Bazaar.", "Evening Experience: Participate in local devotional storytelling and hymns inside the temple complex.", "Overnight Stay: Premium Luxury Hotel, Nathdwara.", "Meals Included: Welcome Drink & Premium Vegetarian Dinner."]),
            _day(2, "Nathdwara to Pushkar Holy Town", "Witness an optional serene early morning Mangla Darshan at the temple. Return to your hotel for a hearty breakfast before departing towards the timeless city of Pushkar. As one of the oldest existing cities in India, Pushkar cradles the sacred Pushkar Lake with 52 bathing ghats. Visit the iconic attractions including the rare, world-renowned Jagatpita Brahma Temple. Take a peaceful walk along the ghats during sunset as hundreds of oil lamps create reflections on the pristine water.", ["Sightseeing Included: Pushkar Lake, Lord Brahma Temple, Savitri Temple (via comfortable ropeway).", "Photography Points: Capture the breathtaking sunset vistas over Varaha Ghat.", "Overnight Stay: Handpicked Premium Heritage Resort, Pushkar.", "Meals Included: Buffet Breakfast & Dinner."]),
            _day(3, "Pushkar to Ajmer Sharif Divine Pilgrimage", "Savor a gourmet breakfast before taking a short, scenic hill-pass drive toward the iconic city of Ajmer. Today you step into the world-famous Ajmer Sharif Dargah—the holy shrine of the Sufi saint Khwaja Moinuddin Chishti. Guided by a dedicated local companion coordinator arranged by TRAGUIN, skip the unorganized paths to offer a traditional 'Chadar' and floral tribute inside the inner sanctum. Experience the legendary emotional storytelling sung via live Qawwali music inside the courtyard, absorbing absolute spiritual rejuvenation.", ["Sightseeing Included: Ajmer Sharif Dargah, Ana Sagar Lake, Adhai Din Ka Jhonpra.", "Optional Activities: A peaceful private evening boat cruise on the serene waters of Ana Sagar Lake.", "Overnight Stay: Luxury Stay / Premium Heritage Property, Ajmer / Pushkar.", "Meals Included: Full Breakfast & Dinner."]),
            _day(4, "Departure via Udaipur / Jaipur", "Relish your final luxury breakfast at the resort property. Depending on your homeward travel schedule, your private chauffeur-driven luxury vehicle will drive you comfortably to either the Udaipur or Jaipur International Airport. Your unforgettable Premium Rajasthan Experience concludes smoothly with blessings in your heart and beautiful memories for a lifetime.", ["Transfers Included: Private Chauffeur Airport Drop-off.", "Meals Included: Full Buffet Breakfast."]),
        ],
        hotels=[
            _hotel("Hotel Radhika Palace / The Master Paradise, Pushkar", "Nathdwara / Pushkar / Ajmer", "03 Nights", "Deluxe", "Deluxe Room / Heritage Room", "MAPAI", 4, 1),
            _hotel("Justa Brij Bhoomi, Nathdwara / Hotel Mansingh Palace, Ajmer", "Nathdwara / Pushkar / Ajmer", "03 Nights", "Premium", "Premium Room / Deluxe Room", "MAPAI", 4, 2),
            _hotel("The Gulaal Luxury Resort / Pushkar Fort / Westin Pushkar Resort", "Nathdwara / Pushkar / Ajmer", "03 Nights", "Luxury", "Luxury Suite / Heritage Suite", "MAPAI", 5, 3),
            _hotel("Mirana Resort (Premium Suite) / The Westin Pushkar Resort & Spa (Pool Villa)", "Nathdwara / Pushkar / Ajmer", "03 Nights", "Ultra Luxury", "Premium Suite / Pool Villa", "MAPAI", 5, 4),
        ],
        inclusions=[
            _inc_included("Accommodation: 03 Nights accommodation in handpicked hotels matching your selected category.", 1),
            _inc_included("Meals: 03 Premium Buffet Breakfasts and 03 curated gourmet Dinners at hotel restaurants.", 2),
            _inc_included("Transfers & Sightseeing: Entire journey via private, sanitized, chauffeur-driven AC Innova Crysta.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated local concierge assistance and specialized Dargah & Temple guides.", 4),
            _inc_included("Taxes & Amenities: All toll taxes, state parking charges, driver allowances, and complimentary packaged mineral water included.", 5),
            _inc_excluded("Train tickets or commercial/chartered airfare costs to Rajasthan.", 6),
            _inc_excluded("Personal expenses such as premium laundry services, tips, telephone calls, and individual soft drinks.", 7),
            _inc_excluded("Special pooja materials, direct donation slips, or custom floral offerings.", 8),
            _inc_excluded("Camera entry fees or special inner sanctum entry tickets where applicable.", 9),
        ],
    )
    return package, itinerary


def build_rj_017(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "RJ-017"
    tour_code = "TRAGUIN-RJ-017"
    title = "Kumbhalgarh Fort Jawai Leopard Hills Udaipur Heritage"
    duration = "04 Nights / 05 Days"
    slug = "rj-017-kumbhalgarh-fort-jawai-leopard-hills-udaipur-heritage"
    itin_slug = "rj-017-kumbhalgarh-fort-jawai-leopard-hills-udaipur-heritage-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code, destination_id=destination_id,
        title=title, duration_label=duration, price=0, rating=Decimal("4.9"),
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Rajasthan, India | Category: Offbeat Luxury & Wildlife", 2),
            _ph("Destinations: Udaipur • Kumbhalgarh Fort • Jawai Leopard Reserve", 3),
            _ph("Ideal for: Wildlife Lovers, Couples & Families", 4),
            _ph("Best season: October to March", 5),
            _ph("Vehicle: Private Luxury Chauffeur-driven Innova Crysta / Premium SUV", 6),
            _ph("Meal Plan: Modified American Plan (All Breakfasts & Dinners Included, Jungle-side Lunch at Jawai)", 7),
            _ph("Route Map: Udaipur Arrival → Kumbhalgarh → Jawai Leopard Hills → Udaipur Heritage Departure", 8),
            _ph("TRAGUIN Curated Experience Note: A premium Rajasthan experience seamlessly combining high-end private 4x4 open-top leopard safaris, historical storytelling at India's grandest fort wall, handpicked hotels, and customized local cultural interactions.", 9),
            _ph("Shopping & Local Experiences: Local Artisan Crafts: Pick up hand-painted Mewari miniature paintings and authentic terracotta items. Traditional Attire: Purchase premium Bandhani textiles, silver tribal ornaments, and camel leather crafts from local markets.", 10),
            _ph("Important Notes: Hotel Policies: Check-in window opens at 14:00 hours; check-out is expected by 11:00 hours. High-tier upgrades are subject to calendar availability. Safari Regulations: Safaris are managed under strict wildlife preservation codes. Keep identification documents handy for checkpoint verifications. Weather Alerts: Desert evenings can become quite cold between November and January. Packing an adequate layer of warm clothing is recommended.", 11),
        ],
        moods=["Wildlife", "Offbeat", "Heritage"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title, duration_label=duration,
        duration_days=_duration_days(duration), starting_price=0, price_note="On Request (Premium Class)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Kumbhalgarh Fort • Jawai Leopard Hills • Udaipur Heritage",
        overview=(
            "Step into an uncharted realm of royal grandeur and wild wilderness. Curated exclusively by TRAGUIN, this offbeat masterpiece unveils the hidden treasures of Rajasthan. From the massive, infinite defensive walls of Kumbhalgarh Fort to the dramatic granite monoliths of Jawai where leopards roam freely alongside humans, prepare yourself for curated experiences, premium stays, and unforgettable memories.\n\n"
            "TOUR OVERVIEW\nVehicle Allocated: Private Luxury Chauffeur-driven Innova Crysta / Premium SUV\nMeal Plan: Modified American Plan (All Breakfasts & Dinners Included, Jungle-side Lunch at Jawai)\nRoute Map: Udaipur Arrival → Kumbhalgarh → Jawai Leopard Hills → Udaipur Heritage Departure\n\n"
            "TRAGUIN Curated Experience Note: A premium Rajasthan experience seamlessly combining high-end private 4x4 open-top leopard safaris, historical storytelling at India's grandest fort wall, handpicked hotels, and customized local cultural interactions.\n\n"
            "WHY VISIT OFFBEAT RAJASTHAN? A PREMIUM EXPERIENCE\nFor travelers hunting for the Best Rajasthan Tour Package or a completely unique Rajasthan Family Tour, the rugged terrain of Kumbhalgarh and Jawai delivers unmatched scenic beauty. Beyond the usual palace trails, a Luxury Rajasthan Holiday allows you to explore the second-longest continuous wall in the world at Kumbhalgarh Fort and look closer into the mystical cave temples of local Rabari herdsmen.\n"
            "The most searched experiences center around the legendary Jawai Leopard Reserve, renowned globally for its unique rock-dwelling leopards that peacefully live among the local communities. This itinerary is an ultimate choice for a high-end Rajasthan Honeymoon Package or an immersive wildlife retreat, pairing legendary hospitality with popular Instagram locations and dramatic mountain sunsets. Experience exceptional Rajasthan Sightseeing through the highly protective and premium guidance of custom TRAGUIN Rajasthan Packages."
        ),
        seo_title="RJ-017 | Kumbhalgarh Fort Jawai Leopard Hills Udaipur Heritage | TRAGUIN",
        seo_description="Premium 04 Nights / 05 Days Rajasthan offbeat package (RJ-017 / TRAGUIN-RJ-017): Kumbhalgarh Fort, Jawai Leopard Reserve safaris, Lake Pichola cruise, and 4-tier handpicked accommodation.",
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Kumbhalgarh Fort Palace, Badal Mahal, Neelkanth Mahadev Temple, Sound & Light Show", 1),
            _ih("Jawai Dam Backwaters, Evening Private 4x4 Leopard Safari, Morning Jawai Safari", 2),
            _ih("Exclusive Lake Pichola Boat Cruise, Saheliyon-ki-Bari, City Palace", 3),
            _ih("TRAGUIN Signature Experience: Curated by TRAGUIN Experts with custom-vetted safari routes and private sunset points", 4),
            _ih("Two fully private 4x4 open-top jungle safaris in Jawai with experienced naturalists", 5),
        ],
        days=[
            _day(1, "Udaipur to Kumbhalgarh", "Arrive at Udaipur Airport where a dedicated private luxury transport arranged by TRAGUIN awaits your presence. Escape the city sprawl and take a scenic route winding through the Aravali hills towards Kumbhalgarh. As you ascend, witness the landscape change into thick forests and sharp ridges. Arrive and check into your handpicked heritage resort offering breathtaking landscapes. Spend the afternoon relaxing or photographing the beautiful valley mist from your private balcony.", ["Sightseeing Included: Panoramic Hill Drive, Leisure Resort Experience.", "Evening Experience: Traditional welcome high-tea served with royal Mewari hospitality over a private valley deck.", "Overnight Stay: Handpicked Luxury Resort, Kumbhalgarh.", "Meals Included: Welcome Drink & Royal Dinner."]),
            _day(2, "Kumbhalgarh Fort Sightseeing", "Devote your day to extensive Kumbhalgarh Sightseeing. Stand in awe before the majestic Kumbhalgarh Fort, a UNESCO World Heritage site featuring a defensive wall stretching over 36 kilometers. Walk along the broad ramparts as your certified guide relates stories of Maharana Pratap. Climb to the Badal Mahal at the highest point for stunning 360-degree views. In the evening, witness the stone walls come alive during the grand Sound & Light Show, displaying the legendary history of Mewar.", ["Sightseeing Included: Kumbhalgarh Fort Palace, Badal Mahal, Neelkanth Mahadev Temple, Sound & Light Show.", "Photography Points: Continuous fort battlements from the watchtowers and the multi-tiered pillars of ancient shrines.", "Overnight Stay: Handpicked Luxury Resort, Kumbhalgarh.", "Meals Included: Full Buffet Breakfast & Specialized Dinner."]),
            _day(3, "Kumbhalgarh to Jawai Leopard Hills", "After a premium breakfast, drive through countryside roads down to the wild plains of Jawai. The scenery dramatically shifts into ancient granite rocks and pristine water bodies. Check into an ultra-luxury glamping tented resort. In the late afternoon, step into a private open-top 4x4 safari vehicle. Travel deep into the rocky terrain with an expert tracker to look for the majestic wild leopards. Watch the sun dip below the granite hills while enjoying luxury refreshments served in the wilderness.", ["Sightseeing Included: Jawai Dam Backwaters, Evening Private 4x4 Leopard Safari.", "Exclusive Experiences: Sunset bush-hospitality with live snacks served on top of a granite monolith.", "Overnight Stay: Ultra-Luxury Glamping Wilderness Camp, Jawai.", "Meals Included: Breakfast, Farm-to-Table Lunch & Wilderness Dinner."]),
            _day(4, "Jawai Leopard Hills to Udaipur", "Wake up early for a morning private safari to spot leopards returning from their nocturnal hunts, along with migratory birds near the Jawai Dam. Return for a lavish breakfast, then drive back towards Udaipur. Check into a luxurious lakeside hotel. In the evening, enjoy an exclusive private boat cruise on Lake Pichola, watching the illuminated structures of City Palace and Jag Mandir sparkle against the dark water.", ["Sightseeing Included: Morning Jawai Safari, Exclusive Lake Pichola Boat Cruise.", "Popular Instagram Locations: Center of Lake Pichola with the glittering City Palace backdrop.", "Overnight Stay: Premium Lakeside Luxury Hotel, Udaipur.", "Meals Included: Breakfast & Lakeside Farewell Dinner."]),
            _day(5, "Udaipur Departure", "Indulge in a final breakfast looking over the calm lake waters. If flight timings permit, take a brief curated walk through the beautiful gardens of Saheliyon-ki-Bari or the corridors of City Palace. Your luxury vehicle will ensure a comfortable transfer to Udaipur Airport for your departure flight. Your offbeat TRAGUIN Rajasthan Package concludes, leaving you with memories to cherish forever.", ["Transfers Included: Private Airport Drop-off.", "Meals Included: Full Buffet Breakfast."]),
        ],
        hotels=[
            _hotel("The Aodhi (HRH Heritage) / Jawai Castle Resort / Trident Udaipur", "Kumbhalgarh / Jawai / Udaipur", "04 Nights", "Deluxe", "Heritage Room / Resort Room / Lake View Room", "MAPAI", 4, 1),
            _hotel("Kumbhalgarh Forest Retreat / Amritara Jawai Sagar / Radisson Blu Palace Resort", "Kumbhalgarh / Jawai / Udaipur", "04 Nights", "Premium", "Forest Room / Safari Room / Deluxe Room", "MAPAI", 4, 2),
            _hotel("The Fateh Safari Suites / Bijapur Lodge Jawai / The Leela Palace Udaipur", "Kumbhalgarh / Jawai / Udaipur", "04 Nights", "Luxury", "Safari Suite / Lodge Room / Palace Suite", "MAPAI", 5, 3),
            _hotel("Maharana Pratap Palace Suites / Sujan Jawai Leopard Camp / Taj Lake Palace Udaipur", "Kumbhalgarh / Jawai / Udaipur", "04 Nights", "Ultra Luxury", "Palace Suite / Luxury Tent / Lake Palace Room", "MAPAI", 5, 4),
        ],
        inclusions=[
            _inc_included("Accommodation: 04 Nights luxury stay at handpicked premium resorts and high-end wild glamping setups.", 1),
            _inc_included("Meals: Daily buffet breakfast and dinners at all properties plus one farm-to-table lunch at Jawai.", 2),
            _inc_included("Transfers & Sightseeing: Dedicated Chauffeur-driven AC Innova Crysta for smooth inter-city travel and sightseeing routes.", 3),
            _inc_included("TRAGUIN Support: 24/7 personalized assistance from our expert operations team.", 4),
            _inc_included("Exclusive Safaris: Two fully private 4x4 open-top jungle safaris in Jawai with experienced naturalists.", 5),
            _inc_included("Welcome Amenities: Royal refreshment hampers, traditional welcome stoles, and premium packed drinking water.", 6),
            _inc_excluded("Airfare or rail connectivity to and from Udaipur.", 7),
            _inc_excluded("Entry tickets to monuments, camera charges, and personal activity passes.", 8),
            _inc_excluded("Individual overheads like laundry, telephone bills, alcoholic beverages, and staff tips.", 9),
            _inc_excluded("Optional tours or extended vehicle runtime outside the itinerary parameters.", 10),
        ],
    )
    return package, itinerary


def build_rj_018(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "RJ-018"
    tour_code = "TRAGUIN-RJ-018"
    title = "Chittorgarh & Bundi Historic Trail"
    duration = "04 Nights / 05 Days"
    slug = "rj-018-chittorgarh-bundi-historic-trail"
    itin_slug = "rj-018-chittorgarh-bundi-historic-trail-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code, destination_id=destination_id,
        title=title, duration_label=duration, price=0, rating=Decimal("4.9"),
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Rajasthan / India | Category: Culture & Heritage Trail", 2),
            _ph("Destinations: Chittorgarh • Bundi Historic Trail", 3),
            _ph("Ideal for: Heritage Lovers, Families & Couples", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Luxury) | Budget Category: Elite Luxury / Premium Stays", 6),
            _ph("Vehicle: Private Luxury Chauffeur-Driven Air-Conditioned Vehicle", 7),
            _ph("Meal Plan: Modified American Plan (Breakfast & Gourmet Dinners)", 8),
            _ph("Route Map: Udaipur/Jaipur Arrival → Chittorgarh Fort → Bundi Palace → Stepwells Exploration → Departure", 9),
            _ph("TRAGUIN Curated Experience Note: This bespoke itinerary focuses on immersive experiences, handpicked hotels, and cultural storytelling. Enjoy VIP access to monumental forts, local artisan encounters, and luxury stays away from regular crowds.", 10),
            _ph("Shopping & Local Experiences: Chittorgarh Markets: Famous for Akola printed textiles, traditional wooden toys, and leather handicrafts. Bundi Bazaars: Pick up genuine hand-painted miniatures, local Kota Doria silk sarees, and traditional silver jewelry. Food Recommendations: Do not miss out on authentic Dal Baati Churma, Mawa Kachori, and local organic ginger-mint teas at historical palace cafes.", 11),
            _ph("Important Notes: Hotel Policies: Standard check-in begins at 14:00 hrs and check-out finishes by 11:00 hrs. Early check-ins are subject to room availability. Weather Notes: Daytimes are beautifully clear and sunny, while evenings can become quite cold. Carrying light jackets or pashminas is advised. Advance Booking Suggestions: Rajasthan packages sell out quickly during high season. Early reservations are recommended to secure premier properties.", 12),
        ],
        moods=["Culture", "Heritage", "Family"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title, duration_label=duration,
        duration_days=_duration_days(duration), starting_price=0, price_note="On Request (Premium Luxury)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Chittorgarh & Bundi Historic Trail • 04 Nights / 05 Days",
        overview=(
            "Welcome to an unforgettable journey back in time. This exclusive Rajasthan Honeymoon Package and Rajasthan Family Tour, masterfully curated by TRAGUIN Experts, takes you deep into the heart of heroic legends, architectural wonders, and breathtaking landscapes. Experience a Premium Rajasthan Experience designed to leave you with unforgettable memories.\n\n"
            "TOUR OVERVIEW\nVehicle Allocated: Private Luxury Chauffeur-Driven Air-Conditioned Vehicle\nMeal Plan: Modified American Plan (Breakfast & Gourmet Dinners)\nRoute Map: Udaipur/Jaipur Arrival → Chittorgarh Fort → Bundi Palace → Stepwells Exploration → Departure\n\n"
            "TRAGUIN Curated Experience Note: This bespoke itinerary focuses on immersive experiences, handpicked hotels, and cultural storytelling. Enjoy VIP access to monumental forts, local artisan encounters, and luxury stays away from regular crowds.\n\n"
            "WHY VISIT CHITTORGARH & BUNDI? A LUXURY RAJASTHAN HOLIDAY\nRajasthan is a land of vibrant heritage, but the historic trail of Chittorgarh and Bundi offers an exclusive look into pure royalty, untouched by commercialization. Chittorgarh is home to India's largest fort complex, representing unparalleled valor and breathtaking landscapes. Meanwhile, Bundi boasts magnificent stepwells, frescoed palaces, and serene lakes that serve as popular Instagram locations for discerning luxury travelers.\n"
            "Whether you are planning a romantic couples' retreat or a rich educational family vacation, this Premium Rajasthan Experience showcases the absolute best of local culture, historic sightseeing, and traditional architecture. The Best Time to Visit Rajasthan is during the cooler months when the marble palaces shine and traditional evening festivals come to life. Let TRAGUIN Rajasthan Packages turn your travel dreams into reality."
        ),
        seo_title="RJ-018 | Chittorgarh & Bundi Historic Trail | TRAGUIN",
        seo_description="Premium 04 Nights / 05 Days Rajasthan heritage package (RJ-018 / TRAGUIN-RJ-018): Chittorgarh Fort, Bundi Palace, Taragarh Fort, Chitrashala, and 4-tier handpicked accommodation.",
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Chittorgarh Fort, Vijay Stambha, Kirti Stambha, Padmini Palace, Rana Kumbha Palace", 1),
            _ih("Raniji ki Baori, Nawal Sagar Lake, Bundi Palace, Taragarh Fort, Chitrashala, Sukh Mahal", 2),
            _ih("TRAGUIN Signature Experience: Handcrafted meticulously by destination experts for seamless heritage discovery", 3),
            _ih("Private workshop meeting traditional artists specializing in authentic Bundi school of art paintings", 4),
            _ih("Complimentary private artisan encounter and specialized miniature art demonstration in Bundi", 5),
        ],
        days=[
            _day(1, "Arrival & Transfer to Chittorgarh", "Arrive at the airport/railway station where your private luxury vehicle and professional chauffeur await. Enjoy a scenic, comfortable drive through the rural landscape as you head toward the historic fortress town of Chittorgarh. Check into your handpicked premium heritage stay and unwind with premium welcome amenities. In the evening, witness a magnificent sunset view over the Mewar plains.", ["Sightseeing Included: En-route scenic photo spots, evening leisure walk.", "Evening Experience: A private welcome briefing and refreshing high-tea organized by your travel consultant.", "Overnight Stay: Handpicked Luxury Heritage Hotel in Chittorgarh.", "Meals Included: Welcome Drink & Gourmet Dinner."]),
            _day(2, "Chittorgarh Sightseeing", "Devote your day to an epic exploration of the iconic Chittorgarh Fort, a UNESCO World Heritage site standing as the epitome of Rajput courage. Walk through ancient palaces, marvel at the intricately carved 9-story Vijay Stambha (Tower of Victory), and view the serene Padmini Palace surrounded by water. Hear the emotional storytelling of royal legends from our certified expert guide before enjoying a local shopping walk for traditional textiles in the afternoon.", ["Sightseeing Included: Chittorgarh Fort, Vijay Stambha, Kirti Stambha, Padmini Palace, Rana Kumbha Palace.", "Photography Points: Breathtaking panoramic shots from the fort ramparts and the reflective pools of Padmini Palace.", "Overnight Stay: Premium Heritage Hotel in Chittorgarh.", "Meals Included: Buffet Breakfast & Specialized Palace Dinner."]),
            _day(3, "Chittorgarh to Bundi", "After a relaxed breakfast, check out and drive comfortably towards the charming town of Bundi, famous for its blue-painted houses, majestic palaces, and ornate stepwells. Upon arrival, check into your ultra-luxury palace hotel. In the afternoon, dive into history by visiting the pristine Raniji ki Baori (Queen's Stepwell), an architectural masterpiece showcasing intricate stone carvings that tell beautiful ancient stories.", ["Sightseeing Included: Raniji ki Baori, Nawal Sagar Lake.", "Evening Experience: A tranquil lakeside walk watching the palace reflection illuminate the water at twilight.", "Overnight Stay: Handpicked Premium Palace Resort in Bundi.", "Meals Included: Elegant Breakfast & Chef's Special Dinner."]),
            _day(4, "Bundi Palace & Taragarh Exploration", "Uncover the gems of Bundi by exploring the spectacular Garh Palace and the dramatic Taragarh Fort. Step inside the world-renowned Chitrashala (Picture Gallery) to marvel at the vibrant, centuries-old miniature paintings that remain exceptionally preserved. Walk down the narrow heritage lanes of the old town, interacting with local miniature artists and exploring traditional bazaars filled with unique souvenirs.", ["Sightseeing Included: Bundi Palace, Taragarh Fort, Chitrashala, Sukh Mahal.", "Local Experiences: Private workshop meeting traditional artists specializing in authentic Bundi school of art paintings.", "Overnight Stay: Premium Palace Resort in Bundi.", "Meals Included: Royal Breakfast & Farewell Theme Dinner."]),
            _day(5, "Departure", "Savor your final luxury breakfast overlooking the palace grounds. Enjoy a relaxed morning capturing your last photography points around the estate. Your private chauffeur will arrive punctually to transfer you comfortably to the airport or railway station for your onward flight home, concluding your premium holiday experience.", ["Transfers Included: Private Chauffeur-Driven Airport/Station Drop-off.", "Meals Included: Full Buffet Breakfast."]),
        ],
        hotels=[
            _hotel("Bassie Fort Heritage Resort / Hadoti Palace, Bundi", "Chittorgarh / Bundi", "04 Nights", "Deluxe", "Heritage Room / Palace Room", "MAP (Breakfast + Dinner)", 4, 1),
            _hotel("Fort Begu Heritage Palace / Classic Bundi Vilas", "Chittorgarh / Bundi", "04 Nights", "Premium", "Heritage Suite / Deluxe Room", "MAP (Breakfast + Dinner)", 4, 2),
            _hotel("Castle Bijaipur Heritage Hotel / Rajmahal Palace Resort", "Chittorgarh / Bundi", "04 Nights", "Luxury", "Heritage Suite / Palace Suite", "MAP (Gourmet Buffet)", 5, 3),
            _hotel("Jodhas Heritage Fort Stay / Brahm Niwas Luxury Palace", "Chittorgarh / Bundi", "04 Nights", "Ultra Luxury", "Fort Suite / Luxury Palace Room", "MAP + Traditional High Tea", 5, 4),
        ],
        inclusions=[
            _inc_included("Accommodation: 04 Nights premium stay at handpicked luxury heritage hotels and palace resorts.", 1),
            _inc_included("Meals: 04 Multi-cuisine Buffet Breakfasts and 04 specially curated gourmet dinners at the hotels.", 2),
            _inc_included("Transfers & Sightseeing: Dedicated private air-conditioned luxury transportation with professional chauffeur for all sightseeings.", 3),
            _inc_included("TRAGUIN Support: 24/7 on-ground concierge support and certified heritage companion guide assistance.", 4),
            _inc_included("Welcome Amenities: Personalized welcome kit on arrival including traditional dynamic stoles, sanitizers, and mineral water.", 5),
            _inc_included("Complimentary Experiences: A private artisan encounter and specialized miniature art demonstration in Bundi.", 6),
            _inc_excluded("Airfare or interstate train tickets to arrival city.", 7),
            _inc_excluded("Standard monument entry tickets, camera permissions, or light show passes.", 8),
            _inc_excluded("Personal expenses such as laundry, phone calls, premium beverages, and tipping.", 9),
            _inc_excluded("Any optional tours or extensions outside the pre-planned itinerary map.", 10),
            _inc_excluded("Travel insurance or medical coverage for emergency services.", 11),
        ],
    )
    return package, itinerary


RAJASTHAN_DOMESTIC_BUILDERS = [
    build_rj_011,
    build_rj_012,
    build_rj_013,
    build_rj_014,
    build_rj_015,
    build_rj_016,
    build_rj_017,
    build_rj_018,
]
