"""Builder functions for DD-001 through DD-014 Daman and Diu packages."""

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

DAMAN_DIU_SLUG = "daman-and-diu"


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


def build_dd_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DD-001"
    tour_code = "TRG-DAM-001"
    title = "Daman Beach Holiday"
    duration = "03 Nights / 04 Days"
    slug = "dd-001-daman-beach-holiday"
    itin_slug = "dd-001-daman-beach-holiday-itinerary"
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
            _ph("State / Country: Daman and Diu / India | Category: Daman Beach Holiday (Premium Family)", 2),
            _ph("Destinations: Moti Daman • Nani Daman • Jampore Beach • Devka Beach", 3),
            _ph("Ideal for: Family Getaways, Beach Lovers & Luxury Seekers", 4),
            _ph("Best season: October to March (Pleasant Coastal Breezes)", 5),
            _ph("Starting price: On Request (Premium Bespoke Package)", 6),
            _ph("Vehicle / Meals: Private Luxury AC Sedan / SUV • Breakfast & Dinner", 7),
            _ph(
                "Route Map: Daman Arrival → Devka Beach → Moti & Nani Daman Heritage → "
                "Jampore Beach & Sunset Cruise → Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private ocean-facing sundowner table reservations at top beach lounges.",
                9,
            ),
            _ph(
                "Curated by TRAGUIN Experts: Handpicked travel flow optimizing daylight hours for beachfront "
                "relaxation and photography.",
                10,
            ),
            _ph(
                "Shopping & Local Experiences: Nani Daman bamboo baskets, leather slippers, sea-shell ornaments; "
                "garlic prawns and Portuguese pastries at beach shacks.",
                11,
            ),
            _ph(
                "Important Notes: Book beachfront resorts 30 days ahead in peak season; light linen and sun protection "
                "recommended; vehicle within day usage limits.",
                12,
            ),
        ],
        moods=["Beach", "Family", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Bespoke Package)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Daman Beach Holiday • Coastal Opulence & Heritage",
        overview=(
            "Welcome to an exquisite coastal escape curated exclusively by TRAGUIN. Embark on the finest Daman "
            "Family Tour, meticulously designed to uncover the breathtaking landscapes, gold-sand coastlines, and "
            "remarkable Portuguese legacy of this tropical enclave. As your trusted luxury travel advisors, TRAGUIN "
            "transforms your beach vacation into a seamless luxury holiday complete with handpicked hotels, immersive "
            "experiences, and soulful oceanside storytelling. From the historic battlements of Moti Daman to the "
            "peaceful golden waves of Jampore Beach, every curated detail ensures you return with unforgettable "
            "memories.\n\n"
            "TOUR OVERVIEW\n"
            "This custom-crafted luxury itinerary presents a flawless blend of relaxed seaside indulgence, historic "
            "colonial fortresses, magnificent Gothic cathedrals, and thrilling sunset cruises. Traveling in your private, "
            "premium chauffeured vehicle, your family will experience absolute privacy and comfort. Featuring a rich "
            "culinary plan with daily exquisite breakfasts and handpicked gourmet dinners, this route delivers the "
            "definitive premium Daman experience. Every step of your holiday includes signature TRAGUIN curated "
            "experiences, offering personalized assistance and exclusive recommendations for the ultimate beach getaway.\n\n"
            "WHY CHOOSE THE BEST DAMAN TOUR PACKAGE?\n"
            "When considering a Luxury Daman Holiday, sophisticated travelers expect more than a simple beach stay; "
            "they look for a beautifully balanced mix of heritage, fine dining, and serene coastal tranquility. Daman is "
            "home to some of the most iconic attractions in Western India. From the formidable Moti Daman Fort and the "
            "beautifully preserved Church of Bom Jesus—top tourist places in Daman for history enthusiasts—to the dynamic "
            "shores of Devka Beach, the destination promises great depth. For families and couples booking a bespoke "
            "Daman Honeymoon Package or Daman Family Tour, the region reveals highly popular Instagram locations like "
            "the scenic jetty promenade, beachside sunset shacks, and colonial-era lighthouses. Whether you wish to browse "
            "local markets for unique handicrafts, indulge in exotic seafood culinary options, or enjoy adrenaline-fueled "
            "water sports, our TRAGUIN Daman Packages ensure high-end hospitality, premium stays, and immersive "
            "experiences during the absolute best time to visit Daman."
        ),
        seo_title="DD-001 | Daman Beach Holiday Premium Family Tour | TRAGUIN",
        seo_description=(
            "Premium 03 Nights / 04 Days Daman beach package (DD-001 / TRG-DAM-001): Moti Daman Fort, "
            "Jampore Beach, Devka Beach, sunset yacht cruise, and 4-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Devka Beach walk, Musical Fountain Park & seaside promenade on Day 01", 1),
            _ih("Moti Daman Fort, Nani Daman Fort, Church of Bom Jesus & Chapel of Our Lady of Rosary on Day 02", 2),
            _ih("Jampore Beach recreation, Light House Vista & private sunset yacht cruise on Day 03", 3),
            _ih("Smooth departure transfer from Daman on Day 04", 4),
            _ih("TRAGUIN Signature Experience: Private ocean-facing sundowner table reservations at top beach lounges", 5),
            _ih("Curated by TRAGUIN Experts: Handpicked travel flow optimizing daylight for beachfront relaxation", 6),
        ],
        days=[
            _day(
                1,
                "Arrival in Daman | Welcome to the Portuguese Riviera – Coastal Sunset Arrival",
                (
                    "Your premium Daman experience begins with a seamless pick-up from Vapi Railway Station, Surat "
                    "Airport, or Mumbai Airport by your private luxury transport vehicle. Arrive in the serene coastal "
                    "town of Daman and check into your handpicked premium resort facing the majestic Arabian Sea. Spend "
                    "your afternoon relaxing amid luxury resort amenities. In the evening, visit the lively Devka Beach "
                    "promenade for a relaxed stroll along the shore, complemented by authentic local food suggestions and "
                    "golden-hour photography points."
                ),
                [
                    "Sightseeing Included: Devka Beach Walk, Musical Fountain Park, Seaside Promenade.",
                    "Evening Experience: Seaside dinner featuring fresh local catches and specialized colonial delicacies.",
                    "Overnight Stay: Daman (Premium / Luxury Beachfront Resort).",
                    "Meals Included: Welcome Drink & Gourmet Dinner.",
                ],
            ),
            _day(
                2,
                "Moti Daman & Nani Daman Heritage Tour | Immersive History, Colonial Forts & Faith",
                (
                    "Awake to the soothing sound of ocean waves and indulge in a lavish breakfast. Today, enjoy a "
                    "beautifully narrated heritage tour across Moti Daman and Nani Daman. Step into the sprawling Moti "
                    "Daman Fort, an architectural masterpiece dating back to the 16th century. Marvel at the intricate "
                    "gold-carved altars inside the legendary Church of Bom Jesus and explore the elegant Governor's Palace. "
                    "Cross the panoramic Damanganga river bridge to explore the Nani Daman Fort and the iconic St. Jerome "
                    "Fort, capturing spectacular family photographs alongside historical battlements."
                ),
                [
                    "Sightseeing Included: Moti Daman Fort, Nani Daman Fort, Church of Bom Jesus, Chapel of Our Lady of Rosary.",
                    "Optional Activities: Bespoke guided walking tour with a local historian to uncover hidden colonial secrets.",
                    "Overnight Stay: Daman (Premium / Luxury Beachfront Resort).",
                    "Meals Included: Premium Breakfast & Crafted Theme Dinner.",
                ],
            ),
            _day(
                3,
                "Jampore Beach Recreation & Sunset Cruise | Golden Sands, Watersports & Tranquility",
                (
                    "Savor a relaxed morning breakfast before driving to Jampore Beach, celebrated for its smooth, dark "
                    "golden sands and exceptionally calm waters—perfect for a premium family tour experience. Spend your "
                    "day enjoying optional beach adventure activities like parasailing, jet-skiing, or quiet horse-drawn "
                    "carriage rides along the shoreline. In the late afternoon, TRAGUIN experts have arranged an exclusive "
                    "experiences highlight: a private sunset yacht cruise along the coast, offering breathtaking landscapes "
                    "as the sun melts gracefully into the Arabian Sea."
                ),
                [
                    "Sightseeing Included: Jampore Beach Pine Groves, Light House Vista, Mirasol Lake Resort garden enclave.",
                    "Evening Experience: Private luxury sunset cruise followed by a celebratory farewell dinner at a premium lounge.",
                    "Overnight Stay: Daman (Premium / Luxury Beachfront Resort).",
                    "Meals Included: Premium Breakfast & Grand Farewell Dinner.",
                ],
            ),
            _day(
                4,
                "Departure from Daman | Cherishing Golden Coastal Memories",
                (
                    "Indulge in a final, opulent breakfast buffet with sweeping views of the ocean. Spend some time picking "
                    "up final souvenirs or capturing last-minute photographs at popular Instagram locations around your "
                    "resort. Later, your private premium vehicle will provide a smooth, comfortable transfer back to Vapi "
                    "Railway Station, Surat Airport, or Mumbai Airport. Return home carrying sweet family bonds and "
                    "unforgettable memories shaped meticulously by TRAGUIN."
                ),
                [
                    "Transfers Included: Private airport/station door-to-door drop-off.",
                    "Meals Included: Sumptuous Breakfast Buffet.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Hotel Miramar / Silver Sands Beach Resort",
                "Daman",
                "03 Nights",
                "Deluxe",
                "Executive Sea Facing Room",
                "MAPAI (Breakfast & Dinner)",
                4,
                1,
            ),
            _hotel(
                "The Gold Beach Resort / Mirasol Resort",
                "Daman",
                "03 Nights",
                "Premium",
                "Premium Ocean View Room",
                "MAPAI (Breakfast & Dinner)",
                5,
                2,
            ),
            _hotel(
                "The Deltin Daman (Luxury Haven)",
                "Daman",
                "03 Nights",
                "Luxury",
                "Grand Superior Suite",
                "MAPAI (Luxury Buffet Plan)",
                5,
                3,
            ),
            _hotel(
                "The Deltin Daman / Elite Private Villa Collection",
                "Daman",
                "03 Nights",
                "Ultra Luxury",
                "Presidential Luxury Private Pool Suite",
                "Bespoke Chef Curated Plan",
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included("Premium Stays: Selected elite beachfront resort accommodation.", 1),
            _inc_included("Luxury Transportation: Private dedicated AC vehicle for all transfers & tours.", 2),
            _inc_included("Curated Meals: Daily extensive buffet breakfasts and gourmet dinners.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated, personalized expert assistance.", 4),
            _inc_included("Welcome Amenities: Cold-pressed mocktails & signature holiday kit on arrival.", 5),
            _inc_included("Exclusive Experience: Elite sunset coastal boating ride access.", 6),
            _inc_excluded("Airfare, flight taxes, or cross-state rail bookings.", 7),
            _inc_excluded("Monument entrance passes, camera permissions, and beach water sports fees.", 8),
            _inc_excluded("Personal items such as laundry, phone bills, premium liquor, and driver tips.", 9),
            _inc_excluded("Optional extensions or custom heritage sightseeing outside the core route.", 10),
        ],
    )
    return package, itinerary


def build_dd_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DD-002"
    tour_code = "TRG-DIU-002"
    title = "Romantic Diu Honeymoon"
    duration = "04 Nights / 05 Days"
    slug = "dd-002-romantic-diu-honeymoon"
    itin_slug = "dd-002-romantic-diu-honeymoon-itinerary"
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
            _ph("State / Country: Daman and Diu / India | Category: Premium Honeymoon Package", 2),
            _ph("Destinations: Romantic Diu • Daman Coastal Getaway", 3),
            _ph("Ideal for: Couples, Honeymooners & Luxury Beach Lovers", 4),
            _ph("Best season: October to March (Pleasant Sea Breezes)", 5),
            _ph("Starting price: On Request (Bespoke Luxury Honeymoon Edition)", 6),
            _ph("Vehicle / Meals: Private Luxury Sedan / CP & Specially Curated Dinners", 7),
            _ph(
                "Route Map: Diu Arrival → Jallandhar Beach → Diu Fort & Naida Caves → Nagoa Beach & Sunset Cruise → "
                "Daman Heritage → Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private beachside floral setup and reserved evening seating "
                "overlooking the sea.",
                9,
            ),
            _ph(
                "Curated by TRAGUIN Experts: Custom pacing designed specifically for honeymooners to avoid rushed "
                "early mornings.",
                10,
            ),
            _ph(
                "Shopping & Local Experiences: Sea-shell handicrafts, bamboo mats, ivory artifacts, premium cashew nuts; "
                "lobster, garlic prawns, and bebinca at coastal lounges.",
                11,
            ),
            _ph(
                "Important Notes: Book 45 days ahead in peak season; valid photo IDs and marriage certificates if required; "
                "October to March ideal for beach activities.",
                12,
            ),
        ],
        moods=["Romantic", "Beach", "Luxury", "Honeymoon"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Bespoke Luxury Honeymoon Edition)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Romantic Diu Honeymoon • Sun, Sea & Portuguese Splendour",
        overview=(
            "Welcome to an enchanting world of coastal romance curated exclusively by TRAGUIN. Escape into the "
            "timeless, golden shores of our custom-crafted Daman & Diu Honeymoon Package, specifically designed for "
            "couples who seek a mixture of historical grandeur, serene luxury, and private beachside bliss. As your "
            "premier travel consultants, TRAGUIN transforms your romantic getaway into a seamless premium Daman & "
            "Diu experience. Let the soft whispers of the Arabian Sea, the majestic silhouette of Portuguese fortresses, "
            "and handpicked premium hotels carve unforgettable memories into your new life together.\n\n"
            "TOUR OVERVIEW\n"
            "This ultra-exclusive 04 Nights / 05 Days romantic escape offers an exquisite balance of relaxation and "
            "exploration across the iconic attractions of Daman & Diu. Travel in absolute comfort with a dedicated private "
            "chauffeured vehicle, fully customized to ensure continuous privacy and flexibility. Your tailored meal plan "
            "features lazy breakfasts overlooking the sea and romantic candlelit dinners arranged at premier seaside "
            "spots. Every element of this route includes exclusive experiences, from private sunset cruises to heritage "
            "walks guided by handpicked storytelling experts, delivering the ultimate luxury Daman & Diu holiday.\n\n"
            "WHY CHOOSE THE BEST DAMAN & DIU HONEYMOON PACKAGE?\n"
            "When planning a Luxury Daman & Diu Holiday, couples look for a tranquil, sophisticated alternative to "
            "crowded coastlines. Diu delivers an exquisite blend of Mediterranean charm, breathtaking landscapes, and "
            "pristine, golden-sand beaches. From the massive, historic ramparts of the Diu Fort to the unique cave "
            "architecture of Naida Caves—one of the most popular Instagram locations in India—every corner tells a "
            "romantic story of a vibrant Portuguese past. Our highly acclaimed Best Daman & Diu Tour Package provides "
            "seamless access to the top tourist places in Daman & Diu. Relax along the scalloped sands of Nagoa Beach, "
            "dive into thrilling water sports, or walk hand-in-hand along the sunset paths of Jallandhar Beach. With "
            "TRAGUIN Daman & Diu Packages, enjoy handpicked luxury stays, tailored heritage trails, and premium coastal "
            "lifestyle curation."
        ),
        seo_title="DD-002 | Romantic Diu Honeymoon Premium Tour | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Daman & Diu honeymoon (DD-002 / TRG-DIU-002): Diu Fort, Naida Caves, "
            "Nagoa Beach, private sunset cruise, Daman heritage, and 4-tier accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Jallandhar Beach, St. Thomas Church Museum & sunset point on Day 01", 1),
            _ih("Diu Fort, Naida Caves, St. Paul's Church & Panikotha viewpoint on Day 02", 2),
            _ih("Nagoa Beach, Hoka Palm groves & private sunset boat cruise on Day 03", 3),
            _ih("Moti Daman Fort, Fort St. Jerome & Devka Beach on Day 04", 4),
            _ih("TRAGUIN Signature Experience: Private beachside floral setup with reserved evening sea-view seating", 5),
            _ih("Honeymoon Special: Welcome cake, floral bedroom decor, and non-alcoholic wine", 6),
        ],
        days=[
            _day(
                1,
                "Arrival in Romantic Diu | Coastal Welcome, Seaside Luxury & Jallandhar Sunset",
                (
                    "Your premium Daman & Diu experience begins as you land at Diu Airport or arrive via your private "
                    "transfer from Rajkot/Veraval. Your dedicated private luxury transport will safely escort you to your "
                    "handpicked premium beachfront resort. Receive a traditional welcome and check into your executive "
                    "sea-view suite. In the late afternoon, step out to explore the serene Jallandhar Beach and visit the "
                    "elegant Diu Museum. Bask in your first romantic sunset over the cliffs, accompanied by premium "
                    "mocktails and fresh sea breezes."
                ),
                [
                    "Sightseeing Included: Jallandhar Beach Promenade, St. Thomas Church Museum, Sunset Point.",
                    "Evening Experience: Private beachside setup with fresh orchids and curated refreshments by TRAGUIN.",
                    "Overnight Stay: Diu (Premium / Luxury Beach Resort).",
                    "Meals Included: Welcome Amenities & Intimate Dinner.",
                ],
            ),
            _day(
                2,
                "Diu Fortress & Naida Caves Exploration | Portuguese Heritage, Mystical Caves & Inspired Photography",
                (
                    "Awake to the beautiful sound of waves and indulge in a lavish breakfast. Today, immerse yourself in "
                    "the rich colonial heritage of Diu. Visit the monumental Diu Fort, a 16th-century Portuguese masterpiece "
                    "boasting majestic stone walls, old iron cannons, and panoramic views of the ocean. Afterwards, explore "
                    "the breathtaking landscapes of Naida Caves, a sun-drenched labyrinth of natural rock formations and a "
                    "highly sought-after Instagram location. Spend your afternoon wandering through the tranquil streets of "
                    "the old town, discovering quaint cafes and beautiful pastel-colored houses."
                ),
                [
                    "Sightseeing Included: Diu Fort, Naida Caves, St. Paul's Church, Panikotha (Fortim do Mar) viewpoint.",
                    "Optional Activities: A professional couple's photography session inside the historic Naida Caves.",
                    "Overnight Stay: Diu (Premium Beachfront Property).",
                    "Meals Included: Premium Breakfast & Authentic Indo-Portuguese Dinner.",
                ],
            ),
            _day(
                3,
                "Nagoa Beach and Thrilling Watersports | Golden Sands, Hoka Palms & Private Sunset Cruise",
                (
                    "Dedicate your morning to Nagoa Beach, famed for its distinct horseshoe shape and rare, beautiful "
                    "African Hoka Palm trees. Take a dip in the calm, crystalline waters or opt for exciting activities like "
                    "parasailing and jet-skiing. In the afternoon, return to your resort for a relaxing luxury spa session. "
                    "As evening falls, step aboard an exclusive private boat cruise arranged by TRAGUIN, raising a toast "
                    "to your love under a magnificent golden sky."
                ),
                [
                    "Sightseeing Included: Nagoa Beach, Hoka Palm groves, Shell Museum.",
                    "Evening Experience: Private sunset boat cruise with customized gourmet appetizers.",
                    "Overnight Stay: Diu (Luxury Resort Suite).",
                    "Meals Included: Breakfast & Romantic Candlelit Seafood Dinner.",
                ],
            ),
            _day(
                4,
                "Daman Coastal Balcony & Heritage Walk | Fort St. Jerome, Devka Beach & Casual Romance",
                (
                    "After breakfast, take a scenic drive or short flight connect to Daman, the sister district overflowing "
                    "with coastal charm. Explore Moti Daman Fort and the historical Fort St. Jerome, featuring a beautiful "
                    "gateway facing the river. Walk through the beautifully manicured gardens of Devka Beach and explore "
                    "local markets. Spend the evening in a luxury beach lounge, reflecting on your unforgettable moments "
                    "and enjoying the tranquil ocean waves."
                ),
                [
                    "Sightseeing Included: Moti Daman Fort, Fort St. Jerome, Devka Beach, Church of Bom Jesus.",
                    "Evening Experience: Gourmet dinner at a top-rated premium sea-lounge.",
                    "Overnight Stay: Daman / Diu Elite Resort Property.",
                    "Meals Included: Breakfast & Luxury Farewell Dinner.",
                ],
            ),
            _day(
                5,
                "Departure with Forever Memories | Farewell to the Sun-Kissed Shores",
                (
                    "Savor a lazy, late-morning breakfast overlooking the ocean. Pack your bags with handwoven souvenirs, "
                    "local artifacts, and wonderful photographs. Your private luxury sedan will provide a comfortable "
                    "transfer to the airport or station for your journey home. Return carrying a deep love and "
                    "unforgettable memories meticulously shaped by TRAGUIN."
                ),
                [
                    "Transfers Included: Private door-to-door luxury airport drop-off.",
                    "Meals Included: Lavish Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Hotel Premium Inn / similar | The Gold Beach Resort (Deluxe)",
                "Diu (3 Nights) / Daman (1 Night)",
                "04 Nights",
                "Deluxe",
                "Deluxe Room",
                "CP Plan (Breakfast Included)",
                4,
                1,
            ),
            _hotel(
                "Kostamar Beach Resort (Premium) | Silver Sands Beach Resort",
                "Diu (3 Nights) / Daman (1 Night)",
                "04 Nights",
                "Premium",
                "Premium Sea View Room",
                "MAPAI (Breakfast & Gourmet Dinner)",
                5,
                2,
            ),
            _hotel(
                "Radisson Blu Resort Diu (Superior) | The Deltin Daman (Luxury Suite)",
                "Diu (3 Nights) / Daman (1 Night)",
                "04 Nights",
                "Luxury",
                "Superior / Luxury Suite",
                "TRAGUIN Honeymoon Inclusion Special",
                5,
                3,
            ),
            _hotel(
                "The Fern Seaside Resort (Ocean Suite) | The Deltin (Presidential Edition)",
                "Diu (3 Nights) / Daman (1 Night)",
                "04 Nights",
                "Ultra Luxury",
                "Ocean Suite / Presidential Edition",
                "VVIP Custom Luxury Inclusions",
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included("Premium Accommodation: Curated sea-facing suites as per chosen tier.", 1),
            _inc_included("Luxury Transportation: Private air-conditioned luxury sedan for seamless transfers.", 2),
            _inc_included("Gourmet Curation: Daily multi-cuisine breakfast and custom romantic dinners.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated local guest relationship manager.", 4),
            _inc_included("Honeymoon Special: Welcome cake, floral bedroom decor, and non-alcoholic wine.", 5),
            _inc_included("Complimentary Experience: Exclusive private sunset boat cruise tickets in Diu.", 6),
            _inc_excluded("Airfare, train tickets, or interstate flight connection costs.", 7),
            _inc_excluded("Monument entrance fees, camera permissions, or local activity tickets.", 8),
            _inc_excluded("Personal expenses such as laundry, phone calls, premium beverages, and tips.", 9),
            _inc_excluded("Any water sports, scuba-diving, or parasailing fees at Nagoa Beach.", 10),
        ],
    )
    return package, itinerary


def build_dd_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DD-003"
    tour_code = "TRG-DIU-003"
    title = "Diu Discovery"
    duration = "03 Nights / 04 Days"
    slug = "dd-003-diu-discovery"
    itin_slug = "dd-003-diu-discovery-itinerary"
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
            _ph("State / Country: Daman and Diu / India | Category: Premium Family Tour", 2),
            _ph("Destinations: Diu Island • Ghoghla Beach • Nagoa Beach • Diu Fort", 3),
            _ph("Ideal for: Family Vacations, Luxury Beach Seekers & Heritage Lovers", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Customised)", 6),
            _ph("Vehicle / Meals: Luxury Private AC Vehicle / MAPAI (Breakfast & Dinner)", 7),
            _ph(
                "Route Map: Diu Arrival → Jalandhar Beach & Sunset Point → Diu Fort & Naida Caves → "
                "Nagoa & Ghoghla Beaches → Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private family interaction and maritime history briefing before visiting "
                "Diu Fort.",
                9,
            ),
            _ph(
                "Curated by TRAGUIN Experts: Handpicked beachfront allocations ensuring your room opens to premium sea "
                "vistas.",
                10,
            ),
            _ph(
                "Shopping & Local Experiences: Shell handicrafts, tortoise-shell artifacts, woven beachwear; lobster "
                "platters and Portuguese-style rolls at seaside bistros.",
                11,
            ),
            _ph(
                "Important Notes: Book 30–45 days ahead in peak season; vehicle dedicated to itinerary route; "
                "check-in 14:00 hrs, check-out 11:00 hrs.",
                12,
            ),
        ],
        moods=["Beach", "Family", "Luxury", "Heritage"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Customised)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Diu Discovery • Sun, Sand & Portuguese Splendour",
        overview=(
            "Welcome to an exquisite coastal retreat curated exclusively by TRAGUIN. Embark on the finest Daman & "
            "Diu Family Tour designed to reveal the breathtaking landscapes, ancient marine fortifications, and golden "
            "beaches of this historic Union Territory. As your elite travel consultants, TRAGUIN transforms your vacation "
            "into a seamless luxury holiday filled with handpicked hotels, immersive experiences, and captivating "
            "sea-faring history. From the massive battlements of the sea-facing Diu Fort to the tranquil shores of Nagoa "
            "Beach, every detail is engineered to create unforgettable memories.\n\n"
            "TOUR OVERVIEW\n"
            "This custom-tailored luxury holiday package offers an exquisite balance between sun-soaked beach "
            "relaxation, maritime history, and colonial Portuguese architecture. Travelling in a dedicated premium AC "
            "vehicle with professional chauffeur-driven assistance, your family will enjoy absolute comfort and privacy. "
            "With a carefully curated meal plan featuring lavish breakfasts and specialized seaside dinners, this route "
            "represents the definitive premium Daman & Diu experience. Every step of your journey includes the signature "
            "touch of TRAGUIN curated experiences, ensuring private sunset excursions, local culinary insights, and "
            "around-the-clock bespoke support.\n\n"
            "WHY CHOOSE THE BEST DAMAN & DIU TOUR PACKAGE?\n"
            "When considering a Luxury Daman & Diu Holiday, discerning travellers seek a tranquil beach escape "
            "seamlessly blended with old-world heritage. Diu Island boasts some of the most iconic attractions in Western "
            "India. From the architectural marvel of St. Paul's Church to the magnificent Diu Fort—a top tourist place in "
            "Daman & Diu for panoramic Arabian Sea vistas—the region offers unparalleled aesthetic depth. For families "
            "and couples booking a bespoke Daman & Diu Honeymoon Package or Daman & Diu Family Tour, the island reveals "
            "highly popular Instagram locations like the Naida Caves, the beautiful walkway of Ghoghla Beach, and the "
            "sunset points overlooking the sea. Our TRAGUIN Daman & Diu Packages guarantee premium comfort, handpicked "
            "luxury stays, and curated exclusive experiences during the absolute best time to visit Daman & Diu."
        ),
        seo_title="DD-003 | Diu Discovery Premium Family Tour | TRAGUIN",
        seo_description=(
            "Premium 03 Nights / 04 Days Diu family package (DD-003 / TRG-DIU-003): Diu Fort, Naida Caves, "
            "Nagoa Beach, Ghoghla Blue Flag Beach, and 4-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Jalandhar Beach, Sunset Point & INS Khukri Memorial on Day 01", 1),
            _ih("Diu Fort, Naida Caves, St. Paul's Church & Sea Shell Museum on Day 02", 2),
            _ih("Nagoa Beach, Ghoghla Blue Flag Beach & Hoka Tree groves on Day 03", 3),
            _ih("Smooth departure from Diu on Day 04", 4),
            _ih("TRAGUIN Signature Experience: Private family maritime history briefing before Diu Fort visit", 5),
            _ih("Complimentary Experience: Reserved family sunset viewing lounge access", 6),
        ],
        days=[
            _day(
                1,
                "Arrival in Diu | Welcome to the Seaside Gem – Sunset and Coastal Serenity",
                (
                    "Your premium Daman & Diu experience begins as you arrive at Diu Airport or the nearby Rajkot/Veraval "
                    "station, where a dedicated private luxury transport vehicle waits to escort you. Transfer smoothly to "
                    "your handpicked premium luxury beachfront resort. After a refreshing afternoon, step out for an exclusive "
                    "evening experience at the Sunset Point near Jalandhar Beach. Enjoy a peaceful evening walk along the "
                    "coast, punctuated by breathtaking landscapes as the golden sun dips into the Arabian Sea."
                ),
                [
                    "Sightseeing Included: Jalandhar Beach, Sunset Point, INS Khukri Memorial.",
                    "Evening Experience: Gourmet coastal welcome dinner curated by TRAGUIN experts.",
                    "Overnight Stay: Diu Island (Premium Beachfront Resort).",
                    "Meals Included: Welcome Drink & Luxury Dinner.",
                ],
            ),
            _day(
                2,
                "Diu Fortress & Colonial Heritage Exploration | Impressive Marine Architecture & Portuguese Splendour",
                (
                    "Awake to the soothing sound of ocean waves. Today, explore the magnificent heritage of Diu. Visit the "
                    "grand Diu Fort, an architectural marvel flanked by the sea on three sides, offering incredible "
                    "photography points. Walk through the beautifully lit paths of Naida Caves, a highly popular Instagram "
                    "location famed for its surreal rock formations and natural light beam displays. Conclude your afternoon "
                    "exploring the intricate woodwork of St. Paul's Church and the historic St. Thomas Church Museum."
                ),
                [
                    "Sightseeing Included: Diu Fort, Naida Caves, St. Paul's Church, Sea Shell Museum.",
                    "Optional Activities: Private heritage walking tour with an expert storyteller guide.",
                    "Overnight Stay: Diu Island (Premium Beachfront Resort).",
                    "Meals Included: Premium Breakfast & Dinner.",
                ],
            ),
            _day(
                3,
                "Nagoa & Ghoghla Beach Relaxation | Pristine Sands, Water Adventure & Sun-Kissed Memories",
                (
                    "Dedicate this day to the incredible beaches of Diu. Spend your morning at Nagoa Beach, famous for its "
                    "unique Hoka palm trees and horse-shoe shaped bay. This beach is perfect for swimming or enjoying "
                    "optional luxury water sports. In the afternoon, visit Ghoghla Beach, a pristine Blue Flag certified "
                    "beach that offers endless scenic beauty and clean walkways. Relax in a private beach lounge arranged "
                    "exclusively for your family."
                ),
                [
                    "Sightseeing Included: Nagoa Beach, Ghoghla Blue Flag Beach, Hoka Tree groves.",
                    "Evening Experience: Private beachside mocktail session and candlelit farewell dinner.",
                    "Overnight Stay: Diu Island (Premium Beachfront Resort).",
                    "Meals Included: Breakfast & Premium Coastal Dinner.",
                ],
            ),
            _day(
                4,
                "Departure from Diu | Cherishing Unforgettable Memories Beyond Destinations",
                (
                    "Indulge in a final lavish breakfast looking out onto the blue horizon. Your private luxury transport "
                    "will safely drive you to Diu Airport or the nearest railway station for your onward journey. Return "
                    "home carrying a heart filled with sweet family bonds and unforgettable memories meticulously designed "
                    "by TRAGUIN."
                ),
                [
                    "Transfers Included: Private luxury door-to-door departure drop-off.",
                    "Meals Included: Sumptuous Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Hotel Kohinoor / similar",
                "Diu",
                "03 Nights",
                "Deluxe",
                "Executive Pool View Room",
                "MAPAI (Breakfast & Dinner)",
                4,
                1,
            ),
            _hotel(
                "The Resort Diu / similar",
                "Diu",
                "03 Nights",
                "Premium",
                "Premium Sea View Room",
                "MAPAI (Breakfast & Dinner)",
                5,
                2,
            ),
            _hotel(
                "Radisson Diu / Azzaro Resorts",
                "Diu",
                "03 Nights",
                "Luxury",
                "Luxury Club Room / Suite",
                "MAPAI (Breakfast & Dinner)",
                5,
                3,
            ),
            _hotel(
                "The Fern Seaside Resort (Villas)",
                "Diu",
                "03 Nights",
                "Ultra Luxury",
                "Private Beachfront Villa",
                "Elite Custom Luxury Dining Plan",
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included("Premium Accommodation: Handpicked seaside resorts as per chosen category.", 1),
            _inc_included("Luxury Transportation: Private AC premium vehicle for all transfers & sightseeing.", 2),
            _inc_included("Curated Meal Plan: Daily luxury breakfast and gourmet dinners (MAPAI).", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated guest experience manager on call.", 4),
            _inc_included("Welcome Amenities: Customized coastal travel kit and refreshing welcome mocktails.", 5),
            _inc_included("Complimentary Experience: Reserved family sunset viewing lounge access.", 6),
            _inc_excluded("Airfare / Train tickets to and from entry gateways.", 7),
            _inc_excluded("Water sports, scuba diving fees, and monument entry tickets.", 8),
            _inc_excluded("Personal expenses such as laundry, phone calls, and tips.", 9),
            _inc_excluded("Any optional activities or extended tours not specified.", 10),
        ],
    )
    return package, itinerary


def build_dd_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DD-004"
    tour_code = "TRG-DAM-004"
    title = "Luxury Daman Escape"
    duration = "04 Nights / 05 Days"
    slug = "dd-004-luxury-daman-escape"
    itin_slug = "dd-004-luxury-daman-escape-itinerary"
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
            _ph("State / Country: Daman and Diu / India | Category: Luxury Travel Escape", 2),
            _ph("Destinations: Moti Daman • Nani Daman • Jampore • Devka Beach", 3),
            _ph("Ideal for: Couples, Families & Discerning Luxury Seekers", 4),
            _ph("Best season: October to May (Tropical Maritime Delight)", 5),
            _ph("Starting price: On Request (Premium Bespoke Curated)", 6),
            _ph("Vehicle / Meals: Private Luxury Sedan / Premium Half Board (MAPAI)", 7),
            _ph(
                "Route Map: Daman Arrival & Devka Beach → Moti Daman Heritage → Nani Daman & Mirasol Lake → "
                "Jampore Beach → Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private sunset beachfront cabana setups with signature non-alcoholic "
                "fruit elixirs.",
                9,
            ),
            _ph(
                "Curated by TRAGUIN Experts: Seamless routing avoiding common weekend entry queues for pure private "
                "relaxation.",
                10,
            ),
            _ph(
                "Shopping & Local Experiences: Leather goods, seashell ornaments, bamboo baskets; fish peri-peri, "
                "butter-garlic prawns, and bebinca at heritage eateries.",
                11,
            ),
            _ph(
                "Important Notes: Lightweight linen recommended; 30-day advance booking advised; extra midnight runs "
                "require pre-coordination.",
                12,
            ),
        ],
        moods=["Beach", "Luxury", "Family", "Leisure"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Bespoke Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Luxury Daman Escape • Sun, Sand & Portuguese Splendour",
        overview=(
            "Welcome to an ultra-premium coastal escape curated passionately by TRAGUIN. Embark on the definitive "
            "Luxury Daman Escape designed exclusively for travelers who appreciate the elegant synthesis of colonial "
            "history, majestic maritime forts, and golden tropical shorelines. As your trusted travel consultants, "
            "TRAGUIN elevates your vacation into a premium luxury holiday complete with handpicked hotels, "
            "breathtaking landscapes, and elite customized care. Let the tranquil whispers of the Arabian Sea and the "
            "grand legacy of Portuguese architecture create unforgettable memories for you and your loved ones.\n\n"
            "TOUR OVERVIEW\n"
            "This meticulously planned Luxury Daman Escape provides a seamless, stress-free route through the most "
            "scenic beauty points of the historic enclave. Traveling in an elite, chauffeur-driven luxury private vehicle, "
            "you will navigate effortlessly between majestic stone fortresses, modern lifestyle boardwalks, and tranquil "
            "coastal sunset viewpoints. Your premium stays feature handpicked beachside resorts offering state-of-the-art "
            "hospitality, bespoke wellness facilities, and gourmet meal plans tailored to perfection. Experience the "
            "hallmark of a TRAGUIN curated experience, delivering private guided storytelling, personalized sunset "
            "setups, and meticulous attention to detail.\n\n"
            "WHY BOOK THE BEST DAMAN & DIU TOUR PACKAGE?\n"
            "For travelers seeking an exclusive, sun-drenched coastal hideaway, a Luxury Daman & Diu Holiday offers "
            "an enchanting alternative to traditional crowded beach destinations. Daman & Diu is globally searched for "
            "its well-preserved 16th-century Portuguese heritage landmarks, massive sea-facing ramparts, and relaxed "
            "maritime rhythm. This itinerary takes you directly to the top tourist places in Daman, including the iconic "
            "Moti Daman Fort, the vibrant Nani Daman jetty, and the pristine sands of Jampore Beach—highly popular "
            "Instagram locations famed for their spectacular golden hour photography. Our TRAGUIN Daman Packages "
            "guarantee the absolute best time to visit Daman, matching immersive experiences with premium comfort."
        ),
        seo_title="DD-004 | Luxury Daman Escape Premium Tour | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Daman luxury package (DD-004 / TRG-DAM-004): Moti Daman Fort, "
            "Mirasol Lake, Jampore Beach, Devka promenade, and 4-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Devka Beachfront, illuminated promenade & ocean-view welcome dinner on Day 01", 1),
            _ih("Moti Daman Fort, Cathedral of Bom Jesus & Church of Our Lady of Remedios on Day 02", 2),
            _ih("Nani Daman Fort, Mirasol Lake Park & handicraft emporiums on Day 03", 3),
            _ih("Jampore Beach cabana access & farewell beachside gala dinner on Day 04", 4),
            _ih("TRAGUIN Signature Experience: Private sunset beachfront cabana with non-alcoholic fruit elixirs", 5),
            _ih("Complimentary Experience: Private Lake Mirasol boat ride passes for the family", 6),
        ],
        days=[
            _day(
                1,
                "Arrival in Daman & Devka Beach | Welcome to the Portuguese Maritime Heaven – Luxury Beginnings",
                (
                    "Your premium Daman experience begins with a VIP greeting by your private luxury chauffeur at Mumbai "
                    "Airport or Vapi Railway Station. Enjoy a smooth, scenic drive to the coastal paradise of Daman. Check "
                    "into your ultra-luxury handpicked resort overlooking the Arabian Sea. After settling into your premium "
                    "stay, spend a relaxed evening exploring the newly transformed Devka Beachfront Promenade. Take a "
                    "leisurely walk along the brilliantly illuminated walkways, capture the crashing waves at sunset "
                    "photography points, and dine on premium culinary selections curated specially by our local experts."
                ),
                [
                    "Sightseeing Included: Devka Beachfront, Modern Illuminated Promenade, Luxury Beach Resort Leisure.",
                    "Evening Experience: Private ocean-view welcome dinner organized exclusively by TRAGUIN travel consultants.",
                    "Overnight Stay: Daman (Premium Beachfront Luxury Resort).",
                    "Meals Included: Welcome Drink & Gourmet Dinner.",
                ],
            ),
            _day(
                2,
                "Moti Daman Heritage Exploration | Colonial Architecture, Ancient Forts & Sacred Cathedrals",
                (
                    "Awake to the soothing sounds of the sea and enjoy a lavish buffet breakfast. Today, delve deep into "
                    "history with an immersive exploration of Moti Daman (Greater Daman). Pass through massive stone "
                    "gateways to enter the historic Moti Daman Fort, constructed in 1559. Wander through quiet, old-world "
                    "streets to witness the architectural marvels of the Cathedral of Bom Jesus and the Church of Our Lady of "
                    "Remedios, featuring breathtaking hand-carved gilded altars. Walk along the historic ramparts looking over "
                    "the Damanganga river confluence before returning to your premium resort for an afternoon of wellness or "
                    "private infinity pool relaxation."
                ),
                [
                    "Sightseeing Included: Moti Daman Fort, Cathedral of Bom Jesus, Church of Our Lady of Remedios, Lighthouse Point.",
                    "Optional Activities: Private heritage walking tour with an expert colonial historian.",
                    "Overnight Stay: Daman (Premium Beachfront Luxury Resort).",
                    "Meals Included: Premium Breakfast & Dinner.",
                ],
            ),
            _day(
                3,
                "Nani Daman & Recreational Escapes | Twin Fort Majesty & Sophisticated Lakeside Leisure",
                (
                    "Following breakfast, explore Nani Daman (Little Daman) to cross the twin fort connection. Tour the "
                    "historic St. Jerome Fort, which houses a beautiful high-arched gateway and the quiet Church of Our Lady "
                    "of the Sea. Next, escape into the lush interiors to visit the beautifully manicured Mirasol Lake Resort "
                    "garden. Enjoy an exclusive experiences package featuring a serene private boat ride across the lake and "
                    "family relaxation among musical fountains. Conclude your afternoon at the modern, premium shopping "
                    "centers of the town for premium artifacts and duty-free souvenirs."
                ),
                [
                    "Sightseeing Included: Nani Daman Fort (St. Jerome), Mirasol Lake Park, Local Handicraft Emporiums.",
                    "Evening Experience: Elegant seaside cocktail trail and gourmet lounge dining overviewing the jetty lights.",
                    "Overnight Stay: Daman (Premium Beachfront Luxury Resort).",
                    "Meals Included: Premium Breakfast & Fusion Dinner.",
                ],
            ),
            _day(
                4,
                "Jampore Beach Shoreline Luxury | Golden Sands, Thrilling Adventures & Sunset Shack Dining",
                (
                    "Dedicate your morning to Jampore Beach, highly searched as the most tranquil and pristine sandy "
                    "shoreline in Daman. Famous for its firm, dark sands and calm waters, it is ideal for family swimming "
                    "and coastal walks. For the adventurous, optional para-sailing, jet-skiing, and ATV beach rides are "
                    "readily accessible. Relax in a premium reserved beach cabana while sipping fresh coconut water. As the "
                    "sun dips below the horizon, casting deep orange hues over the sea—a truly popular Instagram "
                    "location—indulge in a celebratory farewell meal at an elite shoreline establishment."
                ),
                [
                    "Sightseeing Included: Jampore Beach Casuarina Groves, Luxury Private Beach Cabana Access.",
                    "Optional Activities: Thrilling water sports, para-sailing, and high-speed ocean jet skiff riding.",
                    "Overnight Stay: Daman (Premium Beachfront Luxury Resort).",
                    "Meals Included: Premium Breakfast & Farewell Beachside Gala Dinner.",
                ],
            ),
            _day(
                5,
                "Daman to Departure | Farewell Coastal Escape – Cherishing Unforgettable Memories",
                (
                    "Savor a lazy, delicious breakfast at your luxury resort and capture your final family photographs "
                    "against the backdrop of the majestic Arabian Sea. Check out and board your premium private vehicle "
                    "for a comfortable return journey to Mumbai or Vapi. Your Luxury Daman Escape concludes seamlessly "
                    "as you arrive at the airport or station for your onward transit. Return home with revitalized spirits, "
                    "deep bonds, and unforgettable memories designed flawlessly by TRAGUIN."
                ),
                [
                    "Transfers Included: Private luxury door-to-door highway transit return drop-off.",
                    "Meals Included: Sumptuous Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Hotel Miramar / The Gold Beach Resort (Deluxe Wing)",
                "Daman",
                "04 Nights",
                "Deluxe",
                "Superior Sea View Room",
                "Breakfast & Dinner (MAPAI)",
                4,
                1,
            ),
            _hotel(
                "The Gold Beach Resort / Silver Sands Beach Resort",
                "Daman",
                "04 Nights",
                "Premium",
                "Premium Executive Ocean Suite",
                "Breakfast & Dinner (MAPAI)",
                5,
                2,
            ),
            _hotel(
                "The Deltin Daman (5-Star Luxury Resort)",
                "Daman",
                "04 Nights",
                "Luxury",
                "Grand Premium Resort Pool View Suite",
                "Luxury Club Meal Plan",
                5,
                3,
            ),
            _hotel(
                "The Deltin Daman / Custom Private Luxury Beach Villa",
                "Daman",
                "04 Nights",
                "Ultra Luxury",
                "VVIP Presidential Luxury Suite / Villa",
                "Ultra Bespoke Chef Curated Plan",
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included("Premium Accommodation: 04 Nights at handpicked premium resorts.", 1),
            _inc_included("Luxury Transportation: Private Chauffeur-driven AC Sedan for all transits.", 2),
            _inc_included("Curated Meal Plan: Daily premium buffet breakfasts and fine-dining dinners.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated local concierge manager track assistance.", 4),
            _inc_included("Welcome Amenities: Cold towels, floral greetings, and custom luxury travel kits.", 5),
            _inc_included("Complimentary Experience: Private Lake Mirasol boat ride passes for the family.", 6),
            _inc_excluded("Airfare, train tickets, or major multi-state interstate permit taxes.", 7),
            _inc_excluded("All monument, fort camera fees, and local expert guide tip allocations.", 8),
            _inc_excluded("Personal items, laundry, extra bar/liquor spend, and room service tabs.", 9),
            _inc_excluded("Adventure water sports on Jampore beach or optional speed boating.", 10),
        ],
    )
    return package, itinerary


def build_dd_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DD-005"
    tour_code = "TRG-DAM-005"
    title = "Leisure Daman Senior Tour"
    duration = "04 Nights / 05 Days"
    slug = "dd-005-leisure-daman-senior-tour"
    itin_slug = "dd-005-leisure-daman-senior-tour-itinerary"
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
            _ph("State / Country: Daman and Diu / India | Category: Senior Citizen Leisure Tour", 2),
            _ph("Destinations: Daman (Moti Daman • Nani Daman • Devka • Jampore)", 3),
            _ph("Ideal for: Senior Citizens, Leisure Travelers & Heritage Enthusiasts", 4),
            _ph("Best season: October to March (Mild & Pleasant Sea Breezes)", 5),
            _ph("Starting price: On Request (Premium Customised & Accessible)", 6),
            _ph("Special Specs: Relaxed Pace, Wheelchair Assistance (on request), Ground Floor Rooms", 7),
            _ph(
                "Route Map: Daman Arrival → Moti Daman Heritage → Jampore Beach Leisure → "
                "Nani Daman & Devka Gardens → Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Thoroughly audited, step-free access routes verified by travel consultants.",
                9,
            ),
            _ph(
                "Curated by TRAGUIN Experts: Extremely relaxed pace with no early morning wake-up stress.",
                10,
            ),
            _ph(
                "Shopping & Local Experiences: Leather slippers, bamboo mats, sea-shell jewelry; pastel Portuguese walls "
                "and sea-facing herbal tea lounges.",
                11,
            ),
            _ph(
                "Important Notes: Inform coordinators for wheelchair/oxygen needs; book ground-floor rooms 30–45 days "
                "ahead; light shawl advised for evenings.",
                12,
            ),
        ],
        moods=["Leisure", "Family", "Luxury", "Heritage"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Customised & Accessible)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Leisure Daman • Sun, Serenity & Portuguese Heritage",
        overview=(
            "Welcome to a beautifully paced coastal retreat curated exclusively by TRAGUIN. Designed thoughtfully for "
            "our esteemed senior travelers, this bespoke Daman & Diu Tour Package combines the slow-living charm of "
            "an old Portuguese colony with modern luxury amenities. As your dedicated travel consultants, TRAGUIN "
            "invites you to experience breathtaking landscapes, smooth accessible beach promenades, and historic "
            "architecture filled with emotional storytelling. Leave all the details to us as you indulge in handpicked hotels, "
            "premium comfort, and curated experiences engineered to create unforgettable memories.\n\n"
            "TOUR OVERVIEW\n"
            "This special holiday itinerary focuses entirely on a highly relaxed, low-walking, and senior-friendly layout in "
            "Daman. Moving away from rushed travel schedules, this route features late morning starts, gentle drives in a "
            "private premium luxury vehicle, and handpicked premium hotels with accessible facilities. With a tailored meal "
            "plan highlighting light, customized culinary options alongside traditional treats, this holiday ensures complete "
            "physical ease and deep relaxation. Every facet of this trip carries the comforting touch of TRAGUIN "
            "personalized assistance, meaning dedicated airport/station meet-and-greet, priority seating, and a highly "
            "patient, compassionate local chauffeur-guide.\n\n"
            "WHY CHOOSE THE BEST DAMAN & DIU TOUR PACKAGE?\n"
            "When searching for a true Luxury Daman & Diu Holiday, guests look for a peaceful environment away from "
            "overcrowded cityscapes. Daman stands out as one of the most magnificent hidden historical gems on the "
            "western coast. From the monumental ramparts of Moti Daman Fort and the beautiful classic altars of the "
            "Church of Bom Jesus, to the smooth, easily accessible walkways of Jampore Beach, the region presents a "
            "perfect retirement sanctuary or peaceful escape. Choosing our TRAGUIN Daman & Diu Packages means "
            "securing absolute comfort, senior-focused safety, and premium localized hospitality during the absolute best "
            "time to visit Daman & Diu."
        ),
        seo_title="DD-005 | Leisure Daman Senior Citizen Tour | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days senior-friendly Daman package (DD-005 / TRG-DAM-005): Moti Daman "
            "Fort, Jampore Beach, Devka Gardens, accessible stays, and relaxed heritage pacing."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Resort waterfront arrival & gentle ocean sunset on Day 01", 1),
            _ih("Moti Daman Fort, Church of Bom Jesus & Chapel of Our Lady of Rosary on Day 02", 2),
            _ih("Jampore Beach promenade, Casuarina groves & peaceful sunset cruise on Day 03", 3),
            _ih("Nani Daman Fort, St. Jerome Church & Devka Amusement Garden on Day 04", 4),
            _ih("TRAGUIN Signature Experience: Step-free access routes verified by travel consultants", 5),
            _ih("Exclusive Experiences: Reserved comfortable sitting area at Jampore Beach", 6),
        ],
        days=[
            _day(
                1,
                "Arrival in Daman | Welcome to the Coastal Haven – Relaxation & Sea Breezes",
                (
                    "Your premium Daman & Diu sightseeing journey begins with a smooth pickup from Mumbai Airport or "
                    "Vapi Railway Station by your private, air-conditioned luxury transport vehicle. Enjoy a comfortable, "
                    "scenic drive along the national highway straight to the coast. Arrive in Daman and check into your "
                    "handpicked premium resort. TRAGUIN experts have ensured pre-arranged priority check-in and "
                    "accessible room placement. Spend the afternoon resting, followed by a gentle evening stroll along the "
                    "resort's private lawn facing the sea."
                ),
                [
                    "Sightseeing Included: Resort waterfront, panoramic ocean sunset view from the balcony.",
                    "Evening Experience: A warm welcome dinner featuring mild, freshly prepared multi-cuisine options.",
                    "Overnight Stay: Daman (Premium Beachfront Resort).",
                    "Meals Included: Welcome Mocktail & Gourmet Dinner.",
                ],
            ),
            _day(
                2,
                "Moti Daman Heritage Exploration | Portuguese Nostalgia, Majestic Forts & Sacred Cathedrals",
                (
                    "Relish a relaxed breakfast before exploring the rich colonial heritage of Moti Daman, an ancient "
                    "fortified town. Pass through massive stone gateways to see the Church of Bom Jesus, built in 1603, "
                    "showcasing exquisite hand-carved gold-painted wooden altars. The vehicle will drop you directly near "
                    "the flat entrance paths to minimize walking. Listen to emotional storytelling from our guide regarding "
                    "the maritime history of the region. Later, view the historic Governor's Palace and capture beautiful "
                    "photographs of the historic lighthouse."
                ),
                [
                    "Sightseeing Included: Moti Daman Fort, Church of Bom Jesus, Chapel of Our Lady of Rosary, Old Lighthouse.",
                    "Optional Activities: A light, sitting horse-carriage ride inside the historical fort complex.",
                    "Overnight Stay: Daman (Premium Beachfront Resort).",
                    "Meals Included: Premium Breakfast & Dinner.",
                ],
            ),
            _day(
                3,
                "Leisure at Jampore Beach | Silent Shores, Accessible Walks & Golden Sunsets",
                (
                    "Today is dedicated to the scenic beauty of Jampore Beach, famous for its calm, shallow waters and "
                    "firm, level sand texture that allows exceptionally easy walking for senior citizens. A private seaside "
                    "sit-out area is reserved exclusively for your family. Relax under the shade of Casuarina trees, breathe "
                    "in the therapeutic salty air, and watch the waves roll in. In the late afternoon, enjoy a peaceful sunset "
                    "cruise on a modern, safe boat (subject to weather conditions), watching the golden sun sink into the "
                    "Arabian sea."
                ),
                [
                    "Sightseeing Included: Jampore Beach Promenade, Casuarina groves, private sunset viewpoint.",
                    "Evening Experience: Fresh tender coconut water tasting and local mild savory snacks by the shore.",
                    "Overnight Stay: Daman (Premium Beachfront Resort).",
                    "Meals Included: Breakfast & Custom Coastal Dinner.",
                ],
            ),
            _day(
                4,
                "Nani Daman & Devka Gardens | Colourful Markets, Fountains & Gentle Recreation",
                (
                    "Enjoy a late-morning start as your luxury transportation takes you across the twin bridges into Nani "
                    "Daman. Visit the charming St. Jerome Fort, which features an elegant high-walled courtyard view. Next, "
                    "spend a deeply relaxing afternoon at the newly modernized Devka Beach Garden. This beautifully "
                    "landscaped park offers wide, smooth stone pathways, musical fountains, and plenty of comfortable "
                    "benches, allowing you to appreciate the coastal views without any physical strain."
                ),
                [
                    "Sightseeing Included: Nani Daman Fort, St. Jerome Church, Devka Amusement & Promenade Garden.",
                    "Optional Activities: Shopping for soft local traditional textiles and classic willow woven baskets.",
                    "Overnight Stay: Daman (Premium Beachfront Resort).",
                    "Meals Included: Breakfast & Farewell Special Dinner.",
                ],
            ),
            _day(
                5,
                "Departure from Daman | Farewell to the Sun-Drenched Coastline",
                (
                    "Savor your final morning breakfast looking over the ocean. Take some time to pack at your own pace "
                    "before checking out. Your private luxury vehicle will ensure a smooth, bump-free road transfer back to "
                    "Mumbai Airport or Vapi Railway Station. Return home completely rejuvenated, carrying unforgettable "
                    "memories from a deeply peaceful beach holiday crafted perfectly by TRAGUIN."
                ),
                [
                    "Transfers Included: Private door-to-door station/airport highway transfer.",
                    "Meals Included: Lavish Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Hotel Miramar / Silver Sands Beach Resort",
                "Daman",
                "04 Nights",
                "Deluxe",
                "Executive Sea View Room",
                "MAPAI (Breakfast & Dinner)",
                4,
                1,
                description="Elevator Access / Flat shower areas",
            ),
            _hotel(
                "The Gold Beach Resort / Sagar Gems",
                "Daman",
                "04 Nights",
                "Premium",
                "Premium Pool & Ocean View Room",
                "MAPAI (Breakfast & Dinner)",
                5,
                2,
                description="Wide corridors, ground floor options",
            ),
            _hotel(
                "The Deltin Daman (Grand Luxury Property)",
                "Daman",
                "04 Nights",
                "Luxury",
                "Superior Luxury Suite",
                "MAPAI (Breakfast & Dinner)",
                5,
                3,
                description="Full wheelchair compliance, premium service",
            ),
            _hotel(
                "The Deltin Daman / Custom VVIP Beach Villa",
                "Daman",
                "04 Nights",
                "Ultra Luxury",
                "Grand Royal Suite / Private Pool Villa",
                "Bespoke Chef Curated Plan",
                5,
                4,
                description="24/7 dedicated butler assistance",
            ),
        ],
        inclusions=[
            _inc_included("Premium Accommodation: 4 Nights at handpicked accessible beach hotels.", 1),
            _inc_included("Luxury Transportation: Private premium vehicle with dedicated senior-care chauffeur.", 2),
            _inc_included("Curated Meal Plan: Daily customized mild breakfasts and nutritious dinners.", 3),
            _inc_included("TRAGUIN Support: 24/7 priority emergency concierge backing.", 4),
            _inc_included("Welcome Amenities: Fresh seasonal health juices and premium wet wipes upon arrival.", 5),
            _inc_included("Exclusive Experiences: Reserved comfortable sitting area at Jampore Beach.", 6),
            _inc_excluded("Flight tickets / Train booking charges to Mumbai or Vapi.", 7),
            _inc_excluded("Direct entrance tickets to monuments, museums, or local camera fees.", 8),
            _inc_excluded("Personal expenses such as external laundry, specialized medications, or phone bills.", 9),
            _inc_excluded("Any water sports, parasailing, or adventure boat hire.", 10),
        ],
    )
    return package, itinerary

def build_dd_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DD-006"
    tour_code = "TG-DIU-006-PREM"
    title = "Diu Quick Beach Escape"
    duration = "02 Nights / 03 Days"
    slug = "dd-006-diu-quick-beach-escape"
    itin_slug = "dd-006-diu-quick-beach-escape-itinerary"
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
            _ph("State / Country: Daman and Diu / India | Category: Weekend Beach Getaway", 2),
            _ph("Destinations: Diu Island Exploration", 3),
            _ph("Ideal for: Couples, Families & Executives", 4),
            _ph("Best season: October to May", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Independent Tour (FIT) / Luxury Weekend Corporate Escapade", 7),
            _ph("Vehicle: Private Premium Sedan / SUV at full disposal", 8),
            _ph("Meal Plan: Modified American Plan (Daily Premium Breakfast & Gourmet Dinner Included)", 9),
            _ph("Route Map: Diu Arrival → Nagoa Beach → Diu Fort & Sightseeing → Ghoghla Beach → Departure", 10),
            _ph("TRAGUIN Signature Experience: Private ocean-facing sunset high-tea near INS Khukri cliffs", 11),
            _ph("Shopping: Custom handcrafted sea shell souvenirs, Portuguese-inspired cafes", 12),
            _ph("Important: Resort check-in 14:00 hrs, check-out 11:00 hrs; water sports subject to weather", 13),
        ],
        moods=["Beach", "Luxury", "Leisure"],
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
        tagline="Diu Quick Beach Escape • Premium Weekend Retreat",
        overview=(
            "Escape into a coastal paradise where old-world Portuguese charm effortlessly meets modern beachfront "
            "luxury. Specially curated by travel experts at TRAGUIN, this customized luxury package takes you on an "
            "immersive journey across the sun-drenched sands, historic ramparts, and breathtaking landscapes of Diu. "
            "Designed for discerning travelers seeking a premium weekend getaway, this luxury proposal balances "
            "relaxed relaxation on pristine golden shores with rich heritage storytelling, providing unforgettable "
            "memories from the moment you step foot onto the island.\n\n"
            "Indulge in a meticulously crafted weekend itinerary planned for effortless execution. From luxury "
            "beachfront accommodation options to exclusive private transfers, your comfort remains our utmost priority. "
            "Experience the majestic scenic beauty of the Arabian Sea accompanied by the premium travel touch that "
            "TRAGUIN uniquely provides.\n\n"
            "TRAGUIN Curated Touch: Handpicked sea-facing luxury hotel rooms, guaranteed express check-in, premium "
            "curated twilight experiences, and personalized destination assistance.\n\n"
            "Why Visit Diu: Exceptionally clean, uncrowded golden sand beaches, majestic Portuguese heritage sites, "
            "tax-free premium lounges, and an incredibly safe, peaceful island atmosphere. Top Tourist Places in Diu: "
            "The iconic Diu Fort, Naida Caves, St. Paul's Church, INS Khukri Memorial, Nagoa Beach, and Ghoghla Beach. "
            "Most Searched Experiences: Exploring illuminated fort ramparts during twilight, capturing beautiful surreal "
            "photography inside the golden Naida Caves, and enjoying thrilling water sports at Ghoghla Beach. Best Time "
            "to Visit Diu: November through March, when soft refreshing sea breezes pair perfectly with crisp sunny days "
            "for comfortable outdoor beach sightseeing."
        ),
        seo_title="DD-006 | Diu Quick Beach Escape Premium Weekend Tour | TRAGUIN",
        seo_description=(
            "Premium 02 Nights / 03 Days Diu beach package (DD-006 / TG-DIU-006-PREM): Nagoa Beach, Diu Fort, "
            "Naida Caves, Ghoghla Blue Flag Beach, and 4-tier handpicked luxury hotel options."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Nagoa Beach Relaxation & Hoka Groves", 1),
            _ih("Diu Fort, Naida Caves, St. Paul's Church & INS Khukri Memorial", 2),
            _ih("Blue Flag Ghoghla Beach Shoreline Walk", 3),
            _ih("TRAGUIN Signature Experience: Private ocean-facing sunset high-tea near INS Khukri cliffs", 4),
            _ih("Curated by TRAGUIN Experts: Handpicked sea-facing luxury stays with elite hospitality", 5),
            _ih("Luxury Transportation: Reliable private vehicle setups ensuring flexible travel pace", 6),
        ],
        days=[
            _day(
                1,
                "Arrival in Diu & Sunset at Nagoa Beach",
                (
                    "Arrive at Diu Airport or the nearby railway terminal where your dedicated TRAGUIN luxury chauffeur "
                    "welcomes you with customized amenities. Transfer smoothly to your chosen premium hotel resort. Enjoy "
                    "a hassle-free check-in process into your sea-view room and take some time to unwind. In the afternoon, "
                    "we head out to the famous horseshoe-shaped Nagoa Beach. Known for its distinct Hoka trees brought by "
                    "Portuguese sailors from Africa, this beach features incredibly calm and clear waters. Walk along the "
                    "soft sand or simply sit back at a premium beachside pavilion, watching the golden sun sink into the "
                    "vast Arabian Sea. It's a wonderful beginning to your premium getaway."
                ),
                [
                    "Sightseeing Included: Nagoa Beach Relaxation & Hoka Groves",
                    "Optional Activities: Parasailing & Banana Boat Rides",
                    "Overnight Stay: Diu (Premium Beachfront Resort)",
                    "Meals Included: Luxury Welcome Dinner",
                ],
            ),
            _day(
                2,
                "Diu Sightseeing: Colonial Colossus & Naida Caves",
                (
                    "Start your morning with an expansive multi-cuisine buffet breakfast. Today, enjoy a comprehensive "
                    "guided exploration of Diu's iconic attractions. We begin at the colossal 16th-century Diu Fort, a "
                    "historic Portuguese citadel surrounded by the sea on three sides. Stroll along its robust stone "
                    "ramparts where iron cannons still look out over the ocean. Next, we visit the beautiful St. Paul's "
                    "Church, famous for its intricate baroque wood carvings. By mid-day, enter the mystical Naida Caves, "
                    "a spectacular network of natural rock formations lit by natural sunbeams cutting through the ceiling. "
                    "It is easily one of the top Instagram locations in Diu. Conclude your evening at the poignant INS "
                    "Khukri Memorial, honoring a brave Indian Navy ship, while taking in panoramic views of the coastal "
                    "sunset."
                ),
                [
                    "Sightseeing Included: Diu Fort, Naida Caves, St. Paul's Church, INS Khukri Memorial",
                    "Evening Experience: Sunset photography & premium seafood lounge trail",
                    "Overnight Stay: Diu",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                3,
                "Blue Flag Ghoghla Beach & Seamless Departure",
                (
                    "Wake up to the gentle sound of crashing waves and enjoy breakfast overlooking the water. Check out "
                    "from the resort and spend your morning at the pristine Ghoghla Beach, proudly holding the prestigious "
                    "international 'Blue Flag' certification for its immaculate cleanliness, safety, and excellent "
                    "eco-amenities. Take a peaceful walk along the expansive shoreline or capture your final photos of the "
                    "island. Afterward, your chauffeur ensures a comfortable transfer back to Diu Airport or Veraval/Rajkot "
                    "station for your journey home, concluding your premium holiday managed seamlessly by TRAGUIN."
                ),
                [
                    "Sightseeing Included: Blue Flag Ghoghla Beach Shoreline Walk",
                    "Assistance: Complete premium baggage handling by chauffeur",
                    "Overnight Stay: Tour Concludes",
                    "Meals Included: Gourmet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel("Hotel Kohinoor Diu or similar", "Diu", "02 Nights", "Deluxe", "Club Heritage Room", "Breakfast & Dinner", 4, 1),
            _hotel("Azzaro Resorts & Spa, Diu", "Diu", "02 Nights", "Premium", "Premium Pool View Villa", "Breakfast & Dinner", 5, 2),
            _hotel("Radisson Resort Diu Vanakbara", "Diu", "02 Nights", "Luxury", "Superior Sea View Balcony Room", "Breakfast & Dinner", 5, 3),
            _hotel(
                "TRAGUIN Curated Private Signature Beachfront Suites",
                "Diu",
                "02 Nights",
                "Ultra Luxury",
                "Executive Oceanfront Plunge Pool Suite",
                "All Inclusive Premium Plan",
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included("02 Nights accommodation in handpicked, top-rated premium resorts", 1),
            _inc_included("Daily lavish buffet breakfasts and curated multi-cuisine specialty dinners", 2),
            _inc_included("All transfers & city excursions in a private premium air-conditioned vehicle", 3),
            _inc_included("Professional chauffeur charges, state tolls, parking, and route fuel allowances", 4),
            _inc_included("Express check-in privileges and welcome amenities directly at the resort", 5),
            _inc_included("All entry tickets to Diu Fort, museums, and historical heritage landmarks", 6),
            _inc_included("Continuous dedicated on-trip TRAGUIN support & customized assistance", 7),
            _inc_excluded("Flights or long-distance train tickets connecting to Diu", 8),
            _inc_excluded("Any personal expenses like laundry, alcoholic beverages, and minibar usage", 9),
            _inc_excluded("Voluntary tips or gratuities for local drivers and guides", 10),
            _inc_excluded("Cost for specialized water sports activities at Ghoghla Beach", 11),
            _inc_excluded("Anything not specifically detailed in the inclusions list", 12),
        ],
    )
    return package, itinerary


def build_dd_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DD-007"
    tour_code = "TG-DD-007-HRG"
    title = "Premium Daman & Diu Heritage Tour"
    duration = "03 Nights / 04 Days"
    slug = "dd-007-premium-daman-diu-heritage-tour"
    itin_slug = "dd-007-premium-daman-diu-heritage-itinerary"
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
            _ph("State / Country: Daman and Diu / India | Category: Heritage & Leisure", 2),
            _ph("Destinations: Diu Fort • St. Paul's • Naida Caves • Ghoghla", 3),
            _ph("Ideal for: Couples, Families, History Enthusiasts", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Heritage Tour (FIT)", 7),
            _ph("Vehicle: Premium, air-conditioned Luxury Sedan / SUV with dedicated chauffeur", 8),
            _ph("Meal Plan: Modified American Plan (Daily Buffet Breakfast & Curated Dinners)", 9),
            _ph("Route Map: Diu Airport / Rajkot Arrival → Diu Fort Complex → Naida Caves → Ghoghla Beach → Departure", 10),
            _ph("TRAGUIN Signature Experience: Private sunset sailing excursion with panoramic Panikota fortress views", 11),
            _ph("Shopping: Handcrafted shell souvenirs, Portuguese-inspired artifacts, premium local cashews", 12),
            _ph("Important: Resort check-in 14:00 hrs, check-out 11:00 hrs; book beachfront suites in advance", 13),
        ],
        moods=["Heritage", "Luxury", "Cultural"],
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
        tagline="Portuguese Forts, Baroque Churches & Golden Sandy Beaches",
        overview=(
            "Immerse yourself in a fascinating blend of Mediterranean charm and sun-kissed coastal luxury. "
            "Specially curated by our experts, this premium getaway invites you to explore the timeless allure of "
            "legendary Portuguese architecture, magnificent sea forts, and serene shorelines. TRAGUIN details every "
            "corner of your holiday, offering boutique beachfront hospitality, privately chauffeured coastal journeys, "
            "and unforgettable memories filled with history, golden sunsets, and premium relaxation.\n\n"
            "Discover the majestic remnants of Portuguese India with the ultimate Daman and Diu Tour Package. "
            "Designed as a high-end luxury vacation, this itinerary perfectly balances guided heritage explorations of "
            "architectural marvels with relaxing hours along peaceful sea waves. TRAGUIN handles every element from "
            "your initial airport arrival to premium stays at handpicked hotels.\n\n"
            "TRAGUIN Curated Touch: Private sunset sailing excursion, skip-the-line heritage entry passes, and "
            "reservations at the most exclusive seaside dining establishments.\n\n"
            "Why Visit Daman and Diu: Unrivaled colonial sea architecture, uncrowded white-sand beaches, and clean "
            "maritime air steeped in five centuries of rich Portuguese lineage. Famous Attractions: The Grand Diu Fort, "
            "St. Paul's Church, Naida Caves, Moti Daman Fort, and Ghoghla Beach. Most Searched Experiences: Walking "
            "through the surreal geological structures of Naida Caves, sunset photography over the Arabian Sea bastions, "
            "and indulging in fresh coastal seafood. Best Time to Visit Daman and Diu: October to March, when cool sea "
            "breezes create the perfect climate for outdoor sightseeing and beachside dining."
        ),
        seo_title="DD-007 | Premium Daman & Diu Heritage Tour | TRAGUIN",
        seo_description=(
            "Premium 03 Nights / 04 Days Daman and Diu heritage package (DD-007 / TG-DD-007-HRG): Diu Fort, "
            "St. Paul's Church, Naida Caves, Ghoghla Beach, exclusive sunset boat cruise, and 4-tier hotels."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Ghoghla Beach evening walk & welcome mocktails sundowner session", 1),
            _ih("Diu Fort, St. Paul's Church, Naida Caves & Panikota Fort View", 2),
            _ih("Ghoghla Beach leisure, Nagoa Beach drive & exclusive sunset boat cruise", 3),
            _ih("INS Khukri Memorial & seamless departure assistance", 4),
            _ih("TRAGUIN Signature Experience: Private sunset sailing with illuminated Panikota sea fortress views", 5),
            _ih("Curated by TRAGUIN Experts: Handpicked local heritage guides sharing colonial legends", 6),
        ],
        days=[
            _day(
                1,
                "Arrival in Diu – Private Transfer & Sunset Beach Walk",
                (
                    "Your exceptional coastal retreat begins the moment you touch down. A premium, air-conditioned vehicle "
                    "managed by TRAGUIN will receive you at the airport for a smooth transfer to your handpicked beachfront "
                    "resort. Check into your luxury sea-view room, unpack at your own pace, and soak in the soothing ocean "
                    "breeze. In the late afternoon, step out to explore the scenic beauty of the pristine coast. Walk along "
                    "the soft sands as the warm golden sun dips elegantly below the Arabian Sea horizon, marking the official "
                    "beginning of your premium experience."
                ),
                [
                    "Sightseeing Included: Relaxed evening walk at Ghoghla Beach",
                    "Evening Experience: Welcome mocktails & beachside sundowner session",
                    "Overnight Stay: Diu (Premium Luxury Beachfront Resort)",
                    "Meals Included: Welcome Buffet Dinner",
                ],
            ),
            _day(
                2,
                "Portuguese Maritime Bastions & Impressive Baroque Churches",
                (
                    "Savor a delightful breakfast before diving deep into history. Your day begins at the iconic Diu Fort, a "
                    "massive 16th-century Portuguese fortress surrounded by sea water on three sides. Stroll along the ancient "
                    "ramparts, admire the bronze cannons pointing out to the ocean, and capture panoramic views of the coast. "
                    "Next, visit the magnificent St. Paul's Church, a masterpiece of baroque architecture featuring intricate "
                    "white wood carvings. Continue your heritage tour to the Church of St. Francis of Assisi, now converted "
                    "into an archaeological museum. Conclude your historical exploration with an immersive experience inside the "
                    "mysterious Naida Caves, where natural rock formations and sunlight create a dreamlike setting for photography."
                ),
                [
                    "Sightseeing Included: Diu Fort, St. Paul's Church, Naida Caves, Panikota Fort View",
                    "Photography Points: Naida Caves sunbeams, Fort bastions",
                    "Overnight Stay: Diu",
                    "Meals Included: Breakfast & Gourmet Dinner",
                ],
            ),
            _day(
                3,
                "Golden Sandy Beaches & Exclusive Sunset Boat Cruise",
                (
                    "Dedicate your morning to absolute relaxation or thrilling water activities. Head to the beautifully clean "
                    "Ghoghla Beach, widely recognized as one of the finest Blue Flag certified beaches in India. Relax under a "
                    "private canopy or participate in exciting optional activities such as parasailing or jet-skiing. In the "
                    "afternoon, return to your premium resort for a refreshing spa session. As evening approaches, TRAGUIN "
                    "hosts an exclusive private boat cruise along the coast, offering stunning views of the illuminated Panikota "
                    "sea fort while you enjoy customized appetizers."
                ),
                [
                    "Sightseeing Included: Ghoghla Beach Leisure, Nagoa Beach Drive",
                    "Optional Activities: Parasailing, Jet-Skiing, Speedboat Rides",
                    "Overnight Stay: Diu",
                    "Meals Included: Breakfast & Farewell Seafood Dinner",
                ],
            ),
            _day(
                4,
                "Final Chrome Corner & Departure with Memories",
                (
                    "Enjoy a relaxed gourmet breakfast looking out at the beautiful ocean waves. If time permits, take a final "
                    "walk through the quaint local markets to purchase souvenirs and unique handcrafted items. Your professional "
                    "chauffeur will assist you with your luggage and provide a comfortable private transfer to the airport or "
                    "station for your journey home, concluding your premium getaway."
                ),
                [
                    "Sightseeing Included: Brief stop at INS Khukri Memorial",
                    "Assistance: Complete luggage handling and departure drop",
                    "Overnight Stay: Tour Concludes",
                    "Meals Included: Gourmet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel("Hotel Rasal / The Resort Diu or similar", "Diu", "03 Nights", "Deluxe", "Deluxe Sea View Room", "Breakfast & Dinner", 4, 1),
            _hotel("Radhika Beach Resort, Diu", "Diu", "03 Nights", "Premium", "Premium Poolside Room", "Breakfast & Dinner", 5, 2),
            _hotel("Azzaro Resorts & Spa, Diu", "Diu", "03 Nights", "Luxury", "Club Royal Suite", "Breakfast & Dinner", 5, 3),
            _hotel("TRAGUIN Handpicked Elite Beach Villas", "Diu", "03 Nights", "Ultra Luxury", "Presidential Oceanfront Villa", "All-Inclusive Luxury", 5, 4),
        ],
        inclusions=[
            _inc_included("03 Nights luxury stay at premium, top-rated beachfront properties", 1),
            _inc_included("Daily premium buffet breakfasts and custom multi-cuisine dinners", 2),
            _inc_included("Dedicated premium air-conditioned luxury vehicle throughout the tour", 3),
            _inc_included("All sightseeing entry tickets, monument passes, and cave entry permits", 4),
            _inc_included("Exclusive sunset boat cruise experience with light refreshments", 5),
            _inc_included("Welcome drinks, fresh seasonal fruits, and amenities upon arrival", 6),
            _inc_included("Comprehensive 24/7 internal concierge TRAGUIN support", 7),
            _inc_included("All applicable resort taxes, driver allowances, tolls, and parking fees", 8),
            _inc_excluded("Domestic airfare or train tickets to the destination", 9),
            _inc_excluded("Water sports charges (parasailing, jet-skiing, scuba diving)", 10),
            _inc_excluded("Personal items (laundry, phone calls, premium alcohol, tips)", 11),
            _inc_excluded("Any camera or professional video recording fees at sites", 12),
            _inc_excluded("Comprehensive travel and personal medical insurance", 13),
        ],
    )
    return package, itinerary


def build_dd_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DD-008"
    tour_code = "TG-DD-008-ADV"
    title = "Diu Water Sports & Parasailing Special Experience"
    duration = "02 Nights / 03 Days"
    slug = "dd-008-diu-water-sports-parasailing"
    itin_slug = "dd-008-diu-water-sports-parasailing-itinerary"
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
            _ph("State / Country: Daman and Diu / India | Category: Adventure Weekend Getaway", 2),
            _ph("Destinations: Diu Island • Ghoghla Beach • Nagoa Beach", 3),
            _ph("Ideal for: Adventure Seekers & Couples", 4),
            _ph("Best season: October to May", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Tour / FIT / Corporate Getaway", 7),
            _ph("Vehicle: Premium Air-Conditioned Sedan / SUV at disposal", 8),
            _ph("Meal Plan: Deluxe Continental Breakfast and Table d'Hôte Dinners", 9),
            _ph("Route Map: Diu Airport/Delvada Arrival → Ghoghla Beach → Nagoa Beach → Diu Fort → Departure", 10),
            _ph("TRAGUIN Signature Experience: VIP fast-track water sports with Go-Pro recordings included", 11),
            _ph("Shopping: Custom leather goods, Portuguese souvenirs, Nagoa beachside cafes", 12),
            _ph("Important: Water sports depend on weather; book parasailing 3 weeks in advance", 13),
        ],
        moods=["Adventure", "Beach", "Luxury"],
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
        tagline="Diu Water Sports & Parasailing Special Experience",
        overview=(
            "Prepare yourself for an exhilarating escape to the sun-soaked coasts of India's premier island retreat. "
            "Curated specifically by TRAGUIN adventure consultants, this high-octane Daman and Diu Tour Package "
            "seamlessly blends heart-pounding water sports with the serene luxury of coastal living. From flying high "
            "on a thrilling parasailing journey over the Arabian Sea to exploring historical fortress ruins, every single "
            "moment is tailored to produce unforgettable memories. Relax in handpicked hotels, experience curated "
            "experiences, and let the magnificent scenic beauty of Diu captivate your soul.\n\n"
            "This elite Daman and Diu Family Tour & Adventure layout is crafted to maximize your weekend thrill without "
            "compromising on premium relaxation. TRAGUIN guarantees precision execution, providing private premium "
            "transfers, fully certified professional water sports instructors, high-end equipment, and luxury beachside "
            "properties.\n\n"
            "TRAGUIN Curated Touch: VIP fast-track coupons for water sports lines, dedicated safety marshals, and a "
            "complimentary seaside sundowner mocktail experience.\n\n"
            "Why Visit Daman and Diu: Exceptionally clean blue-flag certified beaches, uncrowded waves, and "
            "adrenaline-pumping world-class water sports activities. Famous Attractions: Ghoghla Beach, Diu Fort, Nagoa "
            "Beach, Naida Caves, and St. Paul's Church. Most Searched Experiences: Tandem parasailing over pristine "
            "bays, jet-skiing trails, high-speed speedboating, and watching sunsets over historic bastions. Best Time to "
            "Visit Daman and Diu: October to May when coastal breezes are calm and skies are absolutely crystal clear "
            "for aerial sports."
        ),
        seo_title="DD-008 | Diu Water Sports & Parasailing Adventure Tour | TRAGUIN",
        seo_description=(
            "Premium 02 Nights / 03 Days Diu adventure package (DD-008 / TG-DD-008-ADV): parasailing, jet ski, "
            "speedboat, private sunset cruise, Diu Fort, Naida Caves, and 4-tier beach resorts."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Ghoghla Beach exploration & private sunset cruise with candlelit welcome dinner", 1),
            _ih("Parasailing, Jet Skiing & Speedboat rides at Ghoghla Water Sports Zone", 2),
            _ih("Nagoa Beach relaxation & optional Quad Biking on beach dunes", 3),
            _ih("Diu Fort, Naida Caves & St. Paul's Church heritage trails", 4),
            _ih("TRAGUIN Signature Experience: Line-skipping priority water sports with Go-Pro recordings", 5),
            _ih("Exclusive Recommendations: Restricted beach vantage points for pristine sunset imagery", 6),
        ],
        days=[
            _day(
                1,
                "Arrival in Diu, Sunset Cruise & Exclusive Beach Dining",
                (
                    "Your ultimate coastal adventure commences the moment you arrive at Diu Airport or the nearby station, "
                    "where a private chauffeur extends a warm welcome on behalf of TRAGUIN. Relax in your premium vehicle "
                    "during a smooth transfer to your handpicked resort. After settling into your premium stays, step onto "
                    "the soft golden sands of Ghoghla Beach. In the late afternoon, enjoy an exclusive private sunset boat "
                    "cruise across the calm waters, witnessing the breathtaking landscapes as the orange sun sinks beneath "
                    "the horizon. Conclude your evening with a curated seaside seafood or multi-cuisine specialty dinner "
                    "served right by the sea breeze."
                ),
                [
                    "Sightseeing Included: Ghoghla Beach Exploration, Private Sunset Cruise",
                    "Evening Experience: Candlelit welcome dinner with coastal views",
                    "Overnight Stay: Diu Island (Premium Beachfront Resort)",
                    "Meals Included: Luxury Welcome Dinner",
                ],
            ),
            _day(
                2,
                "Adrenaline Unleashed: Parasailing, Jet Ski & Water Sports Extravaganza",
                (
                    "Wake up to the refreshing sound of ocean waves and enjoy a healthy breakfast. Today marks the centerpiece "
                    "of your Premium Daman and Diu Experience. We head to the pristine, Blue Flag-certified Ghoghla Beach where "
                    "your private instructors await. Strap in for an elite Parasailing flight, soaring high into the sky for a "
                    "spectacular birds-eye view of the entire coastline. Next, feel the speed with an intense Jet Ski session "
                    "across the waves, followed by a fun-filled Speedboat ride or a bumpy Banana Boat tour. In the afternoon, "
                    "transition over to Nagoa Beach to relax beneath branching Hoka palm trees, or indulge in an optional Quad "
                    "Biking adventure on the beach dunes."
                ),
                [
                    "Sightseeing Included: Nagoa Beach, Ghoghla Water Sports Zone",
                    "Included Activities: Parasailing, Jet Skiing, Speedboat Ride",
                    "Overnight Stay: Diu Island",
                    "Meals Included: Gourmet Breakfast & Dinner",
                ],
            ),
            _day(
                3,
                "Portuguese Heritage Trails & Farewell Transfers",
                (
                    "Following breakfast, explore the historic side of Diu. We begin at the magnificent Diu Fort, a 16th-century "
                    "Portuguese masterpiece surrounded by sea water on three sides. Walk along its ancient stone walls to "
                    "photograph the grand old cannons pointing out to the ocean. Next, explore the otherworldly Naida Caves, a "
                    "dream location for Instagram photography due to its natural sunbeams filtering through hollow rock "
                    "formations. Finally, your chauffeur ensures a seamless, relaxed transfer to the airport or station, "
                    "concluding your exceptional, action-packed weekend retreat."
                ),
                [
                    "Sightseeing Included: Diu Fort, Naida Caves, St. Paul's Church",
                    "Photography Points: Naida Caves rock sunbeams, Fort cannons",
                    "Overnight Stay: Tour Concludes",
                    "Meals Included: Breakfast Buffet",
                ],
            ),
        ],
        hotels=[
            _hotel("Hotel Kohinoor Diu or similar", "Diu", "02 Nights", "Deluxe", "Club Premium Room", "Breakfast & Dinner", 4, 1),
            _hotel("Azzaro Resorts & Spa, Diu", "Diu", "02 Nights", "Premium", "Grand Nirvana Room", "Breakfast & Dinner", 5, 2),
            _hotel("Radisson Diu / The Fern Seaside Resort", "Diu", "02 Nights", "Luxury", "Luxury Ocean View Studio", "Breakfast & Dinner", 5, 3),
            _hotel("TRAGUIN Private Elite Beach Pavilion", "Diu", "02 Nights", "Ultra Luxury", "VVIP Private Plunge Pool Villa", "All Inclusive Premium", 5, 4),
        ],
        inclusions=[
            _inc_included("02 Nights premium stay at the finest handpicked beach resorts", 1),
            _inc_included("Daily lavish buffet breakfasts and specially curated chef dinners", 2),
            _inc_included("Fully pre-paid Premium Parasailing, Jet Skiing, and Speedboat vouchers", 3),
            _inc_included("Private dedicated AC luxury vehicle for all sightseeing and transfers", 4),
            _inc_included("VIP entry tickets to Diu Fort and exclusive access to Naida Caves", 5),
            _inc_included("Exclusive private sunset cruise along the Diu coast", 6),
            _inc_included("Personalized assistance and 24/7 TRAGUIN on-ground care", 7),
            _inc_included("Complimentary welcome amenities and tropical fruit baskets", 8),
            _inc_excluded("Flights, rail, or interstate travel tickets to Diu", 9),
            _inc_excluded("Additional water activities like Scuba Diving or Windsurfing", 10),
            _inc_excluded("Personal expenses (laundry, alcoholic bar orders, tips)", 11),
            _inc_excluded("Any mandatory gala dinners or peak seasonal surcharges", 12),
            _inc_excluded("Travel insurance policies", 13),
        ],
    )
    return package, itinerary


def build_dd_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DD-009"
    tour_code = "TG-DD-009-PREM"
    title = "Daman Devka & Jampore Beach Escape"
    duration = "02 Nights / 03 Days"
    slug = "dd-009-daman-devka-jampore-beach-escape"
    itin_slug = "dd-009-daman-devka-jampore-beach-itinerary"
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
            _ph("State / Country: Daman and Diu / India | Category: Leisure Beach Break", 2),
            _ph("Destinations: Devka Beach • Jampore Beach • Moti Daman", 3),
            _ph("Ideal for: Couples, Families & Weekend Seekers", 4),
            _ph("Best season: October to May", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Premium Tour (FIT)", 7),
            _ph("Vehicle: Executive Air-Conditioned Sedan / SUV with dedicated professional chauffeur", 8),
            _ph("Meal Plan: Modified American Plan (Daily Premium Breakfast & Gourmet Dinner Included)", 9),
            _ph("Route Map: Arrival → Devka Beach Sunset → Moti Daman Exploration → Jampore Beach → Departure", 10),
            _ph("TRAGUIN Signature Experience: Private guided heritage walk around Moti Daman Fort battlements", 11),
            _ph("Shopping: Handcrafted leather goods, fresh seafood treats, beachside shell souvenirs", 12),
            _ph("Important: Check-in 14:00 hrs; adhere to safety flags at Jampore and Devka beaches", 13),
        ],
        moods=["Beach", "Luxury", "Leisure"],
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
        tagline="Daman Devka & Jampore Beach Escape",
        overview=(
            "Welcome to a timeless coastal paradise where historical Portuguese opulence effortlessly meets the breezy "
            "rhythm of the Arabian Sea. Meticulously curated by travel experts at TRAGUIN, this luxury itinerary offers a "
            "sublime weekend escape away from the city clamor. Indulge in premium stays, admire breathtaking landscapes, "
            "and stroll along sun-kissed sands. From the historic fortifications of Moti Daman to the peaceful tranquility of "
            "Jampore Beach, every moment promises immersive experiences and unforgettable memories tailored exclusively for you.\n\n"
            "Your upcoming Best Daman and Diu Tour Package guarantees a perfectly paced weekend itinerary designed for "
            "absolute relaxation. Every aspect of your transfers, sightseeing routes, and culinary moments is expertly "
            "overseen by TRAGUIN. Relax in handpicked hotels offering elite seaside access and premium custom amenities.\n\n"
            "TRAGUIN Curated Advantage: Handpicked sea-facing luxury room upgrades, pre-arranged sunset beach loungers, "
            "and highly recommended local seafood culinary maps.\n\n"
            "Why Visit Daman and Diu: The dual destinations blend magnificent 16th-century Portuguese defensive fortresses, "
            "quiet tropical coastlines, and a relaxed union-territory lifestyle. Famous Attractions: Moti Daman Fort, Devka "
            "Beach Amusement Park, Jampore Beach water trails, and the Church of Bom Jesus. Most Searched Experiences: "
            "Sunset parasailing on the coast, enjoying a candlelit seaside dinner, and capturing heritage architecture for "
            "popular Instagram locations. Best Time to Visit Daman and Diu: The cooler autumn and spring months provide the "
            "ideal climate for sun-basking and heritage walks."
        ),
        seo_title="DD-009 | Daman Devka & Jampore Beach Escape | TRAGUIN",
        seo_description=(
            "Premium 02 Nights / 03 Days Daman beach package (DD-009 / TG-DD-009-PREM): Devka Beach, Moti Daman Fort, "
            "Church of Bom Jesus, Jampore Beach, and 4-tier handpicked resort options."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Devka Beach Promenade, Musical Fountain Park & sundowner coastal photography", 1),
            _ih("Moti Daman Fort, Church of Bom Jesus & Jampore Beach leisure", 2),
            _ih("Local Daman shopping & heritage market walk with Parsi delicacies", 3),
            _ih("TRAGUIN Signature Experience: Private guided heritage walk at Moti Daman Fort", 4),
            _ih("Luxury Transportation: Premium vehicles with Wi-Fi, refreshments, and cool towels", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Daman | Coastal Welcome & Devka Beach Sunset",
                (
                    "Your premium coastal holiday begins with a personalized pick-up by a TRAGUIN representative from Vapi "
                    "Railway Station or Surat/Mumbai Airport. Enjoy a comfortable, smooth drive in your private vehicle into "
                    "the tranquil town of Daman. Upon arriving, check into your meticulously handpicked luxury beachfront resort "
                    "and refresh your senses. In the afternoon, step out for an atmospheric walk along Devka Beach. Admire the "
                    "breaking waves, stroll through the nearby musical fountain park, or simply sit back and take in the "
                    "panoramic scenic beauty. End your evening at a stylish seaside cafe with dynamic sunset photography points "
                    "before returning for an exquisite welcome dinner at your resort."
                ),
                [
                    "Sightseeing Included: Devka Beach Promenade, Musical Fountain Park",
                    "Evening Experience: Sundowner drinks and coastal photography sessions",
                    "Overnight Stay: Premium Luxury Beach Resort, Daman",
                    "Meals Included: Welcome Gourmet Dinner",
                ],
            ),
            _day(
                2,
                "Colonial Soul & the Golden Sands of Jampore Beach",
                (
                    "Treat yourself to a lavish breakfast buffet before starting a captivating cultural discovery of Daman's "
                    "glorious past. Explore the majestic Moti Daman Fort, a grand structure housing the iconic 400-year-old "
                    "Church of Bom Jesus, known for its intricate gold-gilded wooden altars and remarkable Portuguese "
                    "architecture. In the afternoon, shift to the golden shorelines of Jampore Beach, universally celebrated "
                    "as one of the top tourist places in Daman and Diu. This beach is highly loved for its clean, low-tide "
                    "waters that are perfect for swimming and leisure walks. For adventure seekers, optional beach sports like "
                    "parasailing and jet-skiing are readily available. End your evening on pre-reserved luxury beach recliners "
                    "under the shade of casuarina trees, making unforgettable memories under a starry sky."
                ),
                [
                    "Sightseeing Included: Moti Daman Fort, Church of Bom Jesus, Jampore Beach",
                    "Optional Activities: High-speed jet skiing, parasailing, horse-carriage rides",
                    "Overnight Stay: Premium Luxury Beach Resort, Daman",
                    "Meals Included: Premium Breakfast & Candlelit Dinner",
                ],
            ),
            _day(
                3,
                "Local Souvenir Trails & Seamless Departure",
                (
                    "Awake to the soothing rhythm of waves crashing near your window. After a relaxing breakfast, take some "
                    "time to explore the vibrant local markets of Daman. Pick up excellent souvenirs, fine leather crafts, and "
                    "premium traditional items. Your dedicated chauffeur will then provide a smooth transfer back to Vapi Railway "
                    "Station or the airport for your onward journey home. Your premium holiday concludes, leaving you completely "
                    "refreshed by this unmatched, curated holiday experience from TRAGUIN."
                ),
                [
                    "Sightseeing Included: Local Daman Shopping & Heritage Market Walk",
                    "Food Suggestion: Try signature authentic Parsi delicacies at local cafes",
                    "Overnight Stay: Tour Concludes",
                    "Meals Included: Luxury Buffet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel("Hotel Miramar Daman or similar", "Daman", "02 Nights", "Deluxe", "Superior Sea View Room", "Breakfast & Dinner", 4, 1),
            _hotel("The Deltin Hotel, Daman", "Daman", "02 Nights", "Premium", "Superior Luxury Room", "Breakfast & Dinner", 5, 2),
            _hotel("Cidade de Daman Beach Resort", "Daman", "02 Nights", "Luxury", "Premium Ocean Front Suite", "Breakfast & Dinner", 5, 3),
            _hotel("TRAGUIN Handpicked Signature Villas", "Daman", "02 Nights", "Ultra Luxury", "Private Pool Ocean Villa", "All Inclusive Premium", 5, 4),
        ],
        inclusions=[
            _inc_included("02 Nights premium stay in handpicked sea-facing resorts", 1),
            _inc_included("Daily multi-cuisine buffet breakfasts and curated dinners", 2),
            _inc_included("Private AC Premium vehicle for all transfers and sightseeing tours", 3),
            _inc_included("Professional, well-experienced local chauffeur", 4),
            _inc_included("Pre-reserved sunset beach seating loungers at Jampore Beach", 5),
            _inc_included("Welcome drinks, fresh mocktails, and seasonal fruits upon arrival", 6),
            _inc_included("Full package taxes, toll ways, fuel charges, and driver fees", 7),
            _inc_included("Continuous 24/7 on-ground TRAGUIN concierge support", 8),
            _inc_excluded("Train tickets or flights to/from your home city", 9),
            _inc_excluded("Any personal shopping, tipping, laundry, or phone charges", 10),
            _inc_excluded("Water sports activities like parasailing or jet-skiing fees", 11),
            _inc_excluded("Mid-day lunches and any snacks or beverages not specified", 12),
            _inc_excluded("Complete comprehensive medical or travel insurance policies", 13),
        ],
    )
    return package, itinerary


def build_dd_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DD-010"
    tour_code = "TG-DD-010-PREM"
    title = "Naida Caves & Sea Shell Museum Offbeat Exploration"
    duration = "02 Nights / 03 Days"
    slug = "dd-010-naida-caves-sea-shell-museum"
    itin_slug = "dd-010-naida-caves-sea-shell-museum-itinerary"
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
            _ph("State / Country: Daman and Diu / India | Category: Offbeat Exploration", 2),
            _ph("Destinations: Diu • Naida Caves • Sea Shell Museum", 3),
            _ph("Ideal for: Couples, Families & Photographers", 4),
            _ph("Best season: October to May", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Luxe Tour (FIT)", 7),
            _ph("Vehicle: Private Premium Sedan / SUV with dedicated chauffeur", 8),
            _ph("Meal Plan: Modified American Plan (Daily Buffet Breakfast & Chef's Special Dinner)", 9),
            _ph("Route Map: Diu Arrival → Naida Caves → Sea Shell Museum → Ghoghla Beach → Departure", 10),
            _ph("TRAGUIN Signature Experience: Early morning guided Naida Caves walk before tourist crowds", 11),
            _ph("Shopping: Handcrafted shell souvenirs, Portuguese-style handicrafts, famous local cafes", 12),
            _ph("Important: Check-in 14:00 hrs; book boutique resorts 30-45 days in advance", 13),
        ],
        moods=["Offbeat", "Cultural", "Luxury"],
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
        tagline="Naida Caves & Sea Shell Museum Offbeat Exploration",
        overview=(
            "Discover the hidden coastal marvels and sun-soaked Portuguese heritage of India's iconic seaside enclave. "
            "This highly immersive offbeat escape, meticulously designed by TRAGUIN travel specialists, invites you to "
            "unravel the mysteries of the sun-dappled Naida Caves, explore the whimsical collections of the Sea Shell "
            "Museum, and relax along pristine, golden shores. Crafted beautifully to offer a balance of leisure, rich "
            "cultural storytelling, and breathtaking landscapes, this luxury proposal guarantees premium stays, handpicked "
            "hotel comforts, and unforgettable memories.\n\n"
            "Unwind with our expertly curated Daman and Diu Holiday, tailored precisely for discerning travelers seeking "
            "an elegant mix of coastal relaxation, vintage Portuguese architecture, and unusual geological formations. This "
            "private retreat is fully escorted by our top-tier destination concierges, ensuring seamless travel and highly "
            "personalized hospitality throughout your journey.\n\n"
            "TRAGUIN Curated Touch: Early-morning exclusive entry slots to photography locations, curated seafood "
            "tastings, and customized sunset beach setups.\n\n"
            "Why Visit Daman and Diu: Home to dramatic rocky caves, ancient towering Portuguese forts, uncrowded "
            "white-sand beaches, and rich maritime museums. Famous Attractions: Diu Fort, Naida Caves, Ghoghla Beach, "
            "St. Paul's Church, and the unusual Sea Shell Museum. Most Searched Experiences: Catching the golden hour "
            "inside the sun-streaked labyrinth of Naida Caves and studying thousands of rare maritime shells from across "
            "the globe. Popular Instagram Locations: The natural rock windows inside Naida Caves, the majestic whitewashed "
            "ramparts of Diu Fort overlooking the Arabian Sea, and colorful old quarters."
        ),
        seo_title="DD-010 | Naida Caves & Sea Shell Museum Offbeat Tour | TRAGUIN",
        seo_description=(
            "Premium 02 Nights / 03 Days Diu offbeat package (DD-010 / TG-DD-010-PREM): Diu Fort, Naida Caves, "
            "Sea Shell Museum, Ghoghla Beach, Jallandhar Beach, and 4-tier seaside resorts."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Diu Fort, St. Paul's Church & Jallandhar Beach curated sunset mocktails", 1),
            _ih("Naida Caves, Sea Shell Museum & Ghoghla Beach with photography assistance", 2),
            _ih("Golden hour beach stroll & seamless departure transfer", 3),
            _ih("TRAGUIN Signature Experience: Early morning Naida Caves walk before tourist crowds", 4),
            _ih("Premium Handpicked Hotels: Elite properties with prime ocean-view positions", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Diu, Portuguese Heritage Trail & Sunset Beach Memories",
                (
                    "Your exceptional coastal retreat begins the moment you arrive in Diu. You will be warmly greeted by your "
                    "dedicated TRAGUIN chauffeur who will escort you to your premium beachfront resort in a luxury private "
                    "vehicle. Check in to your beautifully appointed room and unwind as the calming sea breeze welcomes you. "
                    "In the afternoon, start your exploration along the stunning vintage lanes of the town. Visit the grand "
                    "Diu Fort, an impressive 16th-century Portuguese fortress surrounded by the sea on three sides. Stroll "
                    "along its majestic ramparts, view the ancient iron cannons, and photograph the panoramic ocean vistas. "
                    "Next, witness the intricate baroque architecture of St. Paul's Church before spending a magical evening "
                    "at Jallandhar Beach, where a private sunset setup awaits to create unforgettable memories."
                ),
                [
                    "Sightseeing Included: Diu Fort, St. Paul's Church, Jallandhar Beach",
                    "Evening Experience: Curated sunset mocktails by the shore",
                    "Overnight Stay: Diu (Premium Luxury Beach Resort)",
                    "Meals Included: Welcome Dinner",
                ],
            ),
            _day(
                2,
                "The Mystical Naida Caves & Exclusive Sea Shell Museum Exploration",
                (
                    "Awaken to the soothing sounds of waves and enjoy a lavish buffet breakfast. Today, experience the absolute "
                    "highlights of our TRAGUIN Daman and Diu Packages. We head early to the surreal Naida Caves, a spectacular "
                    "labyrinth of hollowed-out rock formations right outside the city walls. Walk through the natural tunnels "
                    "and witness the dramatic interplay of sunlight beaming through the open ceiling onto the orange rocks — "
                    "a true paradise for photographers. Afterward, we enjoy an immersive experience at the unique Sea Shell "
                    "Museum. Curated over decades by a dedicated merchant navy captain, this iconic attraction houses over "
                    "3,000 distinct specimens of rare sea shells from all corners of the globe. Spend your evening relaxing on "
                    "the golden sands of Ghoghla Beach, one of the cleanest and finest Blue Flag certified beaches in India, "
                    "enjoying optional water adventures."
                ),
                [
                    "Sightseeing Included: Naida Caves, Sea Shell Museum, Ghoghla Beach",
                    "Photography Points: Sunbeams in Naida Caves, exotic shell displays",
                    "Overnight Stay: Diu",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                3,
                "Golden Hour Beach Stroll & Farewell to Diu",
                (
                    "Indulge in a peaceful morning stroll on the pristine beach during the golden hour, taking in the "
                    "breathtaking landscapes one last time. Return to your luxury resort for a final gourmet breakfast. Your "
                    "chauffeur will assist you with your baggage and provide a smooth, comfortable transfer to Diu Airport or "
                    "the nearest railhead for your onward journey. This premium holiday concludes, leaving you with timeless "
                    "stories and immersive experiences curated perfectly by the travel experts at TRAGUIN."
                ),
                [
                    "Sightseeing Included: None (Airport/Station transfer only)",
                    "Assistance: Full luxury vehicle service & baggage handling",
                    "Overnight Stay: Tour Concludes",
                    "Meals Included: Gourmet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel("Rasal Beach Resort or similar", "Diu", "02 Nights", "Deluxe", "Deluxe Sea View Room", "Breakfast & Dinner", 4, 1),
            _hotel("Azzaro Resorts & Spa, Diu", "Diu", "02 Nights", "Premium", "Club Premium Room", "Breakfast & Dinner", 5, 2),
            _hotel("Radisson Resort Diu Vanakbara", "Diu", "02 Nights", "Luxury", "Superior Balcony Room", "Breakfast & Dinner", 5, 3),
            _hotel("TRAGUIN Handpicked Executive Beach Villas", "Diu", "02 Nights", "Ultra Luxury", "Exclusive Oceanfront Suite", "All Inclusive Premium", 5, 4),
        ],
        inclusions=[
            _inc_included("02 Nights premium stay at handpicked seaside resorts", 1),
            _inc_included("Daily multi-cuisine buffet breakfast and curated specialized dinners", 2),
            _inc_included("Air-conditioned private luxury vehicle for all transfers & sightseeing", 3),
            _inc_included("VIP entry tickets to the Sea Shell Museum and Diu Fort monuments", 4),
            _inc_included("Exclusive photographic walk assistance inside the Naida Caves", 5),
            _inc_included("Complimentary welcome non-alcoholic amenities and fresh coastal beverages", 6),
            _inc_included("Comprehensive 24/7 on-ground TRAGUIN support and concierge service", 7),
            _inc_included("All applicable luxury resort taxes, driver allowances, and tolls", 8),
            _inc_excluded("Airfare, flight extensions, or train tickets to Diu", 9),
            _inc_excluded("Personal expenses such as laundry, telephone calls, or tips", 10),
            _inc_excluded("Optional water sports, parasailing, or jet-ski charges at Ghoghla Beach", 11),
            _inc_excluded("Alcoholic drinks or snacks outside the planned meal menu", 12),
            _inc_excluded("Personal travel or medical insurance", 13),
        ],
    )
    return package, itinerary


def build_dd_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DD-011"
    tour_code = "TG-DD-011-MICE"
    title = "Diu Beachfront Corporate MICE Retreat"
    duration = "02 Nights / 03 Days"
    slug = "dd-011-diu-beachfront-corporate-mice-retreat"
    itin_slug = "dd-011-diu-beachfront-corporate-mice-itinerary"
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
            _ph("State / Country: Daman and Diu / India | Category: Corporate MICE & Team Retreat", 2),
            _ph("Destinations: Diu Beachfront & Historic Forts", 3),
            _ph("Ideal for: Corporate Delegations & Executives", 4),
            _ph("Best season: October to May", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Corporate MICE Retreat / Group Inclusive Tour (GIT)", 7),
            _ph("Vehicle: Private Premium Luxury AC Coaches for airport transfers and group sightseeing", 8),
            _ph("Meal Plan: All-Inclusive Corporate Plan (Breakfast, High Teas, Lunches, Gala Dinners)", 9),
            _ph("Route Map: Diu Airport Arrival → Nagoa Beachfront → Diu Fort → Ghoghla Beach → Departure", 10),
            _ph("TRAGUIN Signature Experience: Private oceanfront barbecue gala with corporate styling and AV setup", 11),
            _ph("Shopping: Portuguese souvenirs, premium coastal seafood, iconic ocean-view cafes", 12),
            _ph("Important: Group check-in IDs 7 days prior; confirm MICE bookings 30-45 days in advance", 13),
        ],
        moods=["Corporate", "Beach", "Luxury"],
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
        tagline="Premium Business & Leisure Beachfront Experience",
        overview=(
            "Welcome to the premium coastal escape of Daman and Diu. This state-of-the-art corporate itinerary, "
            "thoughtfully engineered by the corporate travel division at TRAGUIN, perfectly merges high-end corporate "
            "presentation requirements with premium leisure experiences. Designed to maximize team bonding, visual "
            "inspiration, and relaxed executive discussions, this travel plan covers pristine beachfront luxury hotels, "
            "state-of-the-art conference amenities, and spectacular coastal monuments. Let TRAGUIN manage your corporate "
            "delegation seamlessly while your team makes unforgettable memories on the sunny beaches of Diu.\n\n"
            "This elite Daman and Diu Corporate MICE Tour Package is curated specifically for organizations that seek "
            "high-impact corporate planning sessions alongside high-end relaxation. From private group luxury "
            "transportation to custom seaside corporate theme dinners, every detail is flawlessly executed by professional "
            "TRAGUIN coordinators.\n\n"
            "TRAGUIN Curated MICE Touch: Private state-of-the-art conference rooms with audio-visual support, seamless "
            "group fast-track check-ins, custom company branding setups at venues, and dedicated tour coordinators.\n\n"
            "Why Visit Daman and Diu for MICE: Excellent beachfront luxury properties, tax-friendly corporate options, "
            "uncrowded premium beaches, and top-tier connectivity. Famous Attractions: Diu Fort, Naida Caves, Nagoa Beach, "
            "Ghoghla Beach, and St. Paul's Church. Most Searched Experiences: Beachfront team-building exercises, "
            "historical fortress tours, premium seafood dining trails, and sunset team catamaran cruises."
        ),
        seo_title="DD-011 | Diu Beachfront Corporate MICE Retreat | TRAGUIN",
        seo_description=(
            "Premium 02 Nights / 03 Days Diu corporate MICE package (DD-011 / TG-DD-011-MICE): conference rooms, "
            "Nagoa Beach sundowner, Naida Caves, Diu Fort, Ghoghla Beachfront gala dinner, and 4-tier resorts."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Nagoa Beach promenade sundowner & half-day conference room with AV setup", 1),
            _ih("Naida Caves, Diu Fort, St. Paul's Church & beachfront gala dinner with DJ", 2),
            _ih("Leisure beach walk, group check-out & fast-track baggage handling", 3),
            _ih("TRAGUIN Signature Experience: Private oceanfront barbecue gala with corporate styling", 4),
            _ih("Premium Transportation: Luxury tourist coaches with executive seat arrangements", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Diu, Beachfront Welcome & Strategic Insight Sessions",
                (
                    "Arrive at Diu Airport, where your team will be greeted with an exclusive red-carpet airport arrival "
                    "experience curated by TRAGUIN managers. Board your private luxury air-conditioned coaches and transition "
                    "smoothly to your handpicked premium beachfront resort. Enjoy a refreshing non-alcoholic welcome cocktail "
                    "check-in sequence with customized corporate badges and room-drop amenities. After a gourmet international "
                    "lunch buffet, gather at the ocean-facing state-of-the-art conference hall for your first corporate "
                    "presentation or briefing session, complemented by premium high tea. As evening approaches, transition "
                    "from corporate focus to team bonding with a premium beachside sundowner event at Nagoa Beach, showcasing "
                    "fresh local mocktails, curated finger foods, and soft acoustic music along the scenic beauty of the ocean."
                ),
                [
                    "Sightseeing Included: Nagoa Beach Promenade & Coastal Sunset Views",
                    "MICE Special: Half-Day Conference room usage with AV Setup",
                    "Overnight Stay: Diu Beachfront Premium Resort",
                    "Meals Included: Buffet Lunch, High Tea, and Beachside Theme Welcome Dinner",
                ],
            ),
            _day(
                2,
                "Naida Caves Exploration, Team Bonding & Beachfront Gala Night",
                (
                    "Energize your group with an early morning beach yoga or team jog session, followed by a widespread "
                    "breakfast buffet. Today, experience iconic attractions and engage in outdoor team-building events. We visit "
                    "the labyrinthine Naida Caves, where dramatic naturally chiseled rock formations and sunlit spaces offer a "
                    "highly popular photography point for a group corporate portrait. Next, move to the historic 16th-century "
                    "Diu Fort. Walk the massive stone ramparts overlooking the vast Arabian Sea, capturing breathtaking "
                    "landscapes. In the afternoon, return to the resort for an indoor team dynamics workshop or leisure time. "
                    "The grand finale of this Premium Daman and Diu Experience is a spectacular Beachfront Gala Dinner on a "
                    "private stretch of Ghoghla Beach, complete with a live DJ, customized corporate awards ceremony, and a "
                    "lavish coastal seafood and multi-cuisine barbecue spread managed meticulously by TRAGUIN support."
                ),
                [
                    "Sightseeing Included: Naida Caves, Historic Diu Fort, St. Paul's Church",
                    "Evening Experience: Private Beachfront Gala Dinner with DJ and Awards Ceremony",
                    "Overnight Stay: Diu Beachfront Premium Resort",
                    "Meals Included: Breakfast, Curated Lunch, and Beachfront Gala BBQ Dinner",
                ],
            ),
            _day(
                3,
                "Leisure Beachfront Trails & Departure with Unforgettable Memories",
                (
                    "Conclude your corporate retreat with a relaxed, celebratory morning breakfast overlooking the gentle waves. "
                    "Take this time for final collaborative team photos on the beachfront or engage in casual networking by the "
                    "resort's premium infinity pool. After a smooth corporate group check-out process managed fully by your "
                    "TRAGUIN tour handlers, pack your bags with souvenirs and team trophies. Board your premium luxury coaches "
                    "for a comfortable final transfer to Diu Airport for your onward corporate journey. Your team departs "
                    "rejuvenated, tightly knit, and thoroughly motivated, carrying home unforgettable memories of a perfectly "
                    "balanced corporate MICE retreat."
                ),
                [
                    "Sightseeing Included: Leisure beach walk & final photography points",
                    "Assistance: Complete group check-out and fast-track baggage handling",
                    "Overnight Stay: Tour Concludes",
                    "Meals Included: Full Gourmet Breakfast Buffet",
                ],
            ),
        ],
        hotels=[
            _hotel("The Resort Hoka / Similar", "Diu", "02 Nights", "Deluxe", "Premium Deluxe Pool View", "Standard Conference Hall", 4, 1),
            _hotel("Radhika Beach Resort, Diu", "Diu", "02 Nights", "Premium", "Superior Ocean Breeze Room", "Executive Boardrooms & Lawn", 5, 2),
            _hotel("Azzaro Resorts & Spa, Diu", "Diu", "02 Nights", "Luxury", "Club Opula Room / Premium Suite", "Grand Ballroom & AV Sound Systems", 5, 3),
            _hotel("TRAGUIN Signature Handpicked Beachfront Villa Resorts", "Diu", "02 Nights", "Ultra Luxury", "Private Executive Oceanfront Suite", "Exclusive Private Beach Arena & Pavilion", 5, 4),
        ],
        inclusions=[
            _inc_included("02 Nights luxury stay at a premium beachfront resort in Diu", 1),
            _inc_included("Full board meals (02 Breakfasts, 02 Mid-day Lunches, 02 Gala Theme Dinners)", 2),
            _inc_included("Full-day state-of-the-art conference room access with projection & audio setup", 3),
            _inc_included("Private premium AC luxury coach transportation for all group sightseeing and airport transfers", 4),
            _inc_included("Custom beachfront team-building setup and entry management for all group sightseeing", 5),
            _inc_included("Corporate welcome amenities, customized badges, and signage setups", 6),
            _inc_included("Professional 24/7 dedicated TRAGUIN on-ground MICE coordinator support", 7),
            _inc_included("All applicable luxury resort taxes, driver allowances, and tolls", 8),
            _inc_excluded("Domestic/International flights or train travel to Diu Airport", 9),
            _inc_excluded("Individual room personal services (laundry, minibar consumption, telephone bills)", 10),
            _inc_excluded("Extra alcoholic or specialized premium bar drinks not configured in the gala menu", 11),
            _inc_excluded("Individual comprehensive medical and travel insurance policies", 12),
            _inc_excluded("Optional high-octane individual motorized water sports at the beaches", 13),
        ],
    )
    return package, itinerary


def build_dd_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DD-012"
    tour_code = "TG-DD-012-PREM"
    title = "Ghoghla Beach Relaxing Getaway"
    duration = "03 Nights / 04 Days"
    slug = "dd-012-ghoghla-beach-relaxing-getaway"
    itin_slug = "dd-012-ghoghla-beach-relaxing-getaway-itinerary"
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
            _ph("State / Country: Daman and Diu / India | Category: Leisure Coastal Escape", 2),
            _ph("Destinations: Diu • Ghoghla Beach • Naida Caves", 3),
            _ph("Ideal for: Couples, Families & Luxury Seekers", 4),
            _ph("Best season: October to May", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Luxury Holiday (FIT)", 7),
            _ph("Vehicle: Private, executive air-conditioned sedan/SUV with professional chauffeur", 8),
            _ph("Meal Plan: Modified American Plan (Daily Premium Breakfast & Gourmet Dinner Included)", 9),
            _ph("Route Map: Diu Airport Arrival → Ghoghla Beach → Diu Fort Heritage → Naida Caves → Departure", 10),
            _ph("TRAGUIN Signature Experience: Private ocean sunset cruise with coastal tasting platters", 11),
            _ph("Shopping: Local handicrafts, Hoka palm fruits, seaside cafes with fresh fish", 12),
            _ph("Important: Check-in 14:00 hrs; follow lifeguard safety flags at Ghoghla Beach", 13),
        ],
        moods=["Beach", "Luxury", "Leisure"],
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
        tagline="Ghoghla Beach Relaxing Getaway • Diu Sightseeing Exploration",
        overview=(
            "Escape to a pristine sun-soaked sanctuary where gold-sand shores meet rich Portuguese heritage. This premium "
            "coastal itinerary, meticulously customized by TRAGUIN holiday planners, invites you to experience a highly "
            "satisfying, slow-paced luxury retreat on the renowned shores of Ghoghla Beach. From the dramatic, sun-dappled "
            "passageways of Naida Caves to the majestic sea-facing battlements of the ancient Diu Fort, every detail is "
            "engineered to create unforgettable memories. Relax in handpicked hotels, savor immersive experiences, and "
            "surrender to the soothing rhythm of breathtaking landscapes across this beautiful destination.\n\n"
            "This curated Daman and Diu Honeymoon Package and family retreat offers a magnificent blend of leisure, seaside "
            "privacy, and historic exploration. Managed from end-to-end by TRAGUIN experts, the tour guarantees premium "
            "stays, premium private transportation, and beautifully paced excursions that give you ample time to relax on "
            "the beach without feeling rushed.\n\n"
            "TRAGUIN Curated Touch: Reserved sea-view beachfront seating, personalized welcome amenities, and handpicked "
            "hotels offering exclusive experiences.\n\n"
            "Why Visit Daman and Diu: Home to some of India's cleanest Blue Flag certified beaches, legendary Portuguese "
            "cathedrals, and beautifully preserved colossal sea forts. Famous Attractions: Ghoghla Beach, Diu Fort, Naida "
            "Caves, St. Paul's Church, and Jallandhar Beach. Most Searched Experiences: Waterfront dining, sunset cruises "
            "on the Arabian Sea, exploring naturally illuminated rock labyrinths, and thrilling water sports. Best Time to "
            "Visit Daman and Diu: October to May, when the weather is beautifully warm with refreshing sea breezes."
        ),
        seo_title="DD-012 | Ghoghla Beach Relaxing Getaway Diu Tour | TRAGUIN",
        seo_description=(
            "Premium 03 Nights / 04 Days Diu leisure package (DD-012 / TG-DD-012-PREM): Ghoghla Beach, Diu Fort, "
            "Naida Caves, private sunset cruise, and 4-tier luxury beach resorts."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Ghoghla Beach evening stroll & romantic candle-lit beachside dining", 1),
            _ih("Diu Fort, Naida Caves & St. Paul's Church heritage exploration", 2),
            _ih("Ghoghla Beach leisure, optional water sports & private sunset cruise", 3),
            _ih("TRAGUIN Signature Experience: Private ocean sunset cruise with coastal tasting platters", 4),
            _ih("Personalized Assistance: Dedicated chauffeur guide with flexible photo stops", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Diu & Magnificent Sunset at Ghoghla Beach",
                (
                    "Your luxury getaway begins as you land at Diu Airport or arrive via a private transfer. A dedicated "
                    "TRAGUIN representative will receive you with a warm welcome and escort you in your executive private "
                    "vehicle to your premium beachfront resort overlooking the golden sands. Check in and unwind in your "
                    "sea-view room. In the late afternoon, step directly onto Ghoghla Beach, celebrated as one of the "
                    "cleanest and longest beaches in the region. Walk along the tranquil shore, let the gentle waves lap at "
                    "your feet, and witness a breathtaking sunset that paints the sky in shades of amber and violet. In the "
                    "evening, enjoy a candle-lit welcome dinner at the resort, featuring fresh coastal delicacies."
                ),
                [
                    "Sightseeing Included: Ghoghla Beach evening stroll",
                    "Evening Experience: Romantic candle-lit beachside dining",
                    "Overnight Stay: Luxury Resort at Ghoghla Beach / Diu",
                    "Meals Included: Welcome Gourmet Dinner",
                ],
            ),
            _day(
                2,
                "Diu Fort Heritage & the Mystical Naida Caves Exploration",
                (
                    "Savor a magnificent breakfast with views of the ocean before setting off on a fascinating Daman and Diu "
                    "Sightseeing tour. Our first stop is the iconic Diu Fort, a colossal 16th-century Portuguese coastal "
                    "citadel surrounded by the sea on three sides. Stroll along its robust stone ramparts, admire the old "
                    "bronze cannons pointing at the horizon, and take in the panoramic views of the ocean. Next, we journey "
                    "into the surreal Naida Caves, a spectacular network of naturally carved rock formations and sun-drenched "
                    "labyrinths that rank among the most popular Instagram locations in India. Sunlight breaks through the rock "
                    "openings, creating an ethereal interplay of light and shadow perfect for photography. Conclude the "
                    "afternoon with a visit to the intricately carved St. Paul's Church, a masterpiece of Baroque architecture."
                ),
                [
                    "Sightseeing Included: Diu Fort, Naida Caves, St. Paul's Church",
                    "Photography Points: Naida Caves sunbeams, Diu Fort sea-ramparts",
                    "Overnight Stay: Luxury Resort at Ghoghla Beach / Diu",
                    "Meals Included: Premium Breakfast & Dinner",
                ],
            ),
            _day(
                3,
                "Leisure Beach Day, Optional Water Sports & Sunset Cruise",
                (
                    "Embrace a slow-paced morning to experience the ultimate Premium Daman and Diu Experience. Spend your day "
                    "fully relaxing by the resort's infinity pool or on the soft sand of Ghoghla Beach. For those seeking a "
                    "bit of excitement, optional premium water sports are available, including safe parasailing, jet-skiing, "
                    "and banana boat rides supervised by certified instructors. In the late afternoon, TRAGUIN curates an "
                    "exclusive private sunset cruise on the Arabian Sea. Sip on refreshing beverages and listen to soft music "
                    "as the sun dips beneath the horizon. It's a wonderful, immersive experience that will leave you with "
                    "beautiful memories."
                ),
                [
                    "Sightseeing Included: Ghoghla Beach Leisure, Private Sunset Cruise",
                    "Optional Activities: Parasailing, Jet-Skiing, Speedboat tours",
                    "Overnight Stay: Luxury Resort at Ghoghla Beach / Diu",
                    "Meals Included: Premium Breakfast & Farewell Dinner",
                ],
            ),
            _day(
                4,
                "Bid Farewell to the Sun-Kissed Shores",
                (
                    "Wake up to the soothing sound of the ocean waves and enjoy a final, luxurious breakfast spread at your "
                    "resort. Take a morning stroll along the beach to collect a few unique sea shells as souvenirs. Your "
                    "dedicated private chauffeur will assist you with your luggage and provide a comfortable, air-conditioned "
                    "transfer to Diu Airport or the designated railway station for your onward flight home. Your premium "
                    "holiday concludes, leaving you with a refreshed spirit and beautiful memories designed by TRAGUIN."
                ),
                [
                    "Sightseeing Included: None (Airport/Station transfer only)",
                    "Assistance: Seamless baggage handling and check-in support",
                    "Overnight Stay: Tour Concludes",
                    "Meals Included: Gourmet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel("The Resort Diu / Hotel Premium Inn", "Diu", "03 Nights", "Deluxe", "Deluxe Sea Facing Room", "Breakfast & Dinner", 4, 1),
            _hotel("Azzaro Resorts & Spa, Diu", "Diu", "03 Nights", "Premium", "Club Premium Room", "Breakfast & Dinner", 5, 2),
            _hotel("Radisson Diu / Kostamar Beach Resort", "Diu", "03 Nights", "Luxury", "Grande Ocean View Suite", "Breakfast & Dinner", 5, 3),
            _hotel("TRAGUIN Exclusive Handpicked Beach Villas", "Diu", "03 Nights", "Ultra Luxury", "Private Plunge Pool Royal Villa", "All Inclusive Premium", 5, 4),
        ],
        inclusions=[
            _inc_included("03 Nights premium stay at handpicked luxury beach resorts", 1),
            _inc_included("Daily lavish buffet breakfasts and curated gourmet dinners", 2),
            _inc_included("Private air-conditioned premium vehicle for all transfers & tours", 3),
            _inc_included("Complimentary private sunset boat cruise on the Arabian Sea", 4),
            _inc_included("All monument entry tickets, parking fees, tolls, and driver allowances", 5),
            _inc_included("Dedicated welcome amenities and signature fruit basket upon check-in", 6),
            _inc_included("24/7 TRAGUIN on-ground guest assistance and concierge support", 7),
            _inc_excluded("Airfare, flight tickets, or train bookings to Diu", 8),
            _inc_excluded("Cost of optional adventure water sports activities", 9),
            _inc_excluded("Personal expenses such as laundry, phone calls, or bar bills", 10),
            _inc_excluded("Tips, gratuities, and camera/video recording charges", 11),
            _inc_excluded("Any insurance policies or expenses from unforeseen events", 12),
        ],
    )
    return package, itinerary


def build_dd_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DD-013"
    tour_code = "TG-DD-013-HER"
    title = "Moti Daman & Nani Daman Heritage Walk"
    duration = "02 Nights / 03 Days"
    slug = "dd-013-moti-daman-nani-daman-heritage-walk"
    itin_slug = "dd-013-moti-daman-nani-daman-heritage-itinerary"
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
            _ph("State / Country: Daman and Diu / India | Category: History & Heritage Walk", 2),
            _ph("Destinations: Moti Daman • Nani Daman", 3),
            _ph("Ideal for: History Buffs, Couples, Families", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Tailor-made Getaway (FIT) with Dedicated Local Assistance", 7),
            _ph("Vehicle: Premium air-conditioned Sedan / SUV for effortless private transfers", 8),
            _ph("Meal Plan: Modified American Plan (Breakfast & Gourmet Dinner Included)", 9),
            _ph("Route Map: Arrival → Nani Daman → Moti Daman Heritage Walk → Devka & Jampore Beach → Departure", 10),
            _ph("TRAGUIN Signature Experience: Private walking tour with local historian at 16th-century chapels", 11),
            _ph("Shopping: Handcrafted leather items, seaside shell souvenirs, local coastal bistros", 12),
            _ph("Important: Check-in 14:00 hrs; book peak weekends 4-6 weeks in advance", 13),
        ],
        moods=["Heritage", "Cultural", "Luxury"],
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
        tagline="Moti Daman & Nani Daman Heritage Walk",
        overview=(
            "Step back in time into a world where Portuguese grand architecture blends gracefully with coastal India's "
            "timeless charm. This exclusive heritage journey, meticulously curated by TRAGUIN travel architects, offers an "
            "elegant exploration of Daman and Diu. From the thick bastion walls of Moti Daman to the busy coastal quarters "
            "of Nani Daman, every moment unfolds into a beautiful historic narrative. Enjoy curated experiences, premium "
            "stays at beachfront properties, and specialized heritage walks led by local experts to create unforgettable "
            "memories.\n\n"
            "Immerse yourself in a beautifully paced historical weekend getaway. This luxury travel experience is structured "
            "around the iconic fortifications, cathedrals, and serene coastlines of Daman and Diu. Handpicked hotels offer "
            "unparalleled premium comfort, allowing you to relax deeply after engaging heritage walks arranged seamlessly by "
            "TRAGUIN experts.\n\n"
            "TRAGUIN Curated Experience Note: Private guided sunset strolls, exclusive entry coordination at ancient "
            "cathedral chapels, and handpicked local culinary tasting menus.\n\n"
            "Why Visit Daman and Diu: Home to remarkably preserved 16th-century European fortresses, stunning Baroque "
            "churches, and tranquil golden-sand beaches. Famous Attractions: Moti Daman Fort, Nani Daman Fort, Church of "
            "Our Lady of Remedios, Jampore Beach, and Devka Beach. Most Searched Experiences: Walking through ancient stone "
            "gateways, sampling colonial-influenced coastal cuisine, and photographing sunsets over old ramparts."
        ),
        seo_title="DD-013 | Moti Daman & Nani Daman Heritage Walk | TRAGUIN",
        seo_description=(
            "Premium 02 Nights / 03 Days Daman heritage package (DD-013 / TG-DD-013-HER): Nani Daman Fort, Moti Daman "
            "Fort, Church of Bom Jesus, Jampore Beach sunset, and authorized local heritage guides."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Nani Daman Fort, St. Jerome Fort & Devka Beach welcome dinner", 1),
            _ih("Moti Daman Fort Citadel, Church of Bom Jesus & Jampore Beach sunset", 2),
            _ih("Local Heritage Market Trail, Perna Market & lighthouse photography", 3),
            _ih("TRAGUIN Signature Experience: Private historian-led walk unlocking chapel secrets", 4),
            _ih("Premium Handpicked Hotels: Elite properties with beautiful proximity to the shore", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Daman & Nani Daman Fort Exploration",
                (
                    "Arrive in the elegant seaside enclave of Daman, where your dedicated TRAGUIN private chauffeur will greet "
                    "you warmly. Transfer comfortably to your premium handpicked resort facing the serene sea. After an "
                    "effortless check-in and some time to settle in, begin your discovery with the iconic Nani Daman Fort. "
                    "Walk beneath the grand stone archway bearing the coat of arms of the Portuguese kings. Stroll past the "
                    "high stone walls overlooking the busy river docks where traditional fishing boats line up. End your "
                    "afternoon at the beautiful Church of Our Lady of the Sea, soaking in the panoramic coastal views and "
                    "breathtaking landscapes that mark the beginning of an unforgettable weekend getaway."
                ),
                [
                    "Sightseeing Included: Nani Daman Fort, St. Jerome Fort, Old River Docks",
                    "Evening Experience: Leisure stroll along Devka Beach followed by an elegant welcome dinner",
                    "Overnight Stay: Daman (Premium Oceanfront Resort)",
                    "Meals Included: Gourmet Welcome Dinner",
                ],
            ),
            _day(
                2,
                "Moti Daman Heritage Walk & Sunset at Jampore Beach",
                (
                    "Savor a delightful breakfast before diving into the highlight of your trip: the Premium Moti Daman "
                    "Experience. Accompanied by our expert local historian, walk through the massive gates of the Moti Daman "
                    "Fort, an expansive citadel dating back to 1559. Wander past rows of historic pastel-hued administrative "
                    "buildings and centuries-old residences. Marvel at the stunning Baroque interiors of the Church of Our "
                    "Lady of Remedios and the breathtaking, gold-gilded carvings within the Chapel of Church of Bom Jesus. "
                    "In the late afternoon, your driver will take you to the pristine Jampore Beach. Unwind with an exclusive "
                    "experience — a private beachside sit-out where you can witness a glorious Arabian Sea sunset, creating "
                    "unforgettable memories."
                ),
                [
                    "Sightseeing Included: Moti Daman Fort Citadel, Church of Bom Jesus, Dominican Monastery Ruins",
                    "Optional Activities: Horse carriage ride along Jampore Beach or watersports",
                    "Overnight Stay: Daman",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                3,
                "Local Artisanal Trails & Farewell to Daman",
                (
                    "Wake up to the soothing sound of ocean waves and enjoy a relaxed breakfast. Check out from your premium "
                    "resort and take a gentle driving tour through the remaining hidden heritage quarters. Stop briefly at local "
                    "markets to browse through unique Portuguese-inspired crafts, customized leather footwear, and coastal "
                    "souvenirs. Reflect on the historic tales and scenic beauty encountered during this classic heritage walk "
                    "before your private chauffeur transfers you safely back to the airport or railway station for your onward "
                    "journey, marking a perfect completion of your TRAGUIN Daman and Diu Packages."
                ),
                [
                    "Sightseeing Included: Local Heritage Market Trail, Perna Market",
                    "Photography Points: Lighthouse vistas, colorful colonial townhouses",
                    "Overnight Stay: Tour Concludes",
                    "Meals Included: Gourmet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel("The Deltin Daman or similar", "Daman", "02 Nights", "Deluxe", "Superior Room", "Breakfast & Dinner", 4, 1),
            _hotel("The Gold Beach Resort, Daman", "Daman", "02 Nights", "Premium", "Deluxe Ocean View Room", "Breakfast & Dinner", 5, 2),
            _hotel("Miramar Resort Daman / Cidade de Daman", "Daman", "02 Nights", "Luxury", "Premium Sea Facing Suite", "Breakfast & Dinner", 5, 3),
            _hotel("TRAGUIN Exclusive Handpicked Heritage Stays", "Daman", "02 Nights", "Ultra Luxury", "Signature Executive Ocean Suite", "All Inclusive Premium Menu", 5, 4),
        ],
        inclusions=[
            _inc_included("02 Nights premium stay at handpicked beachfront resorts", 1),
            _inc_included("Daily multi-cuisine buffet breakfast and curated gourmet dinners", 2),
            _inc_included("Private dedicated AC Sedan/SUV for all transfers and sightseeing", 3),
            _inc_included("Authorized local heritage guide for Moti Daman & Nani Daman walks", 4),
            _inc_included("All entry tickets to forts, monuments, and historic chapels", 5),
            _inc_included("Tailored welcome amenities and mineral water in the vehicle", 6),
            _inc_included("Complete on-ground TRAGUIN customer support and assistance", 7),
            _inc_included("Inclusive of all toll taxes, parking, and driver allowances", 8),
            _inc_excluded("Airfare / Train tickets to nearest hub (Surat/Mumbai/Vapi)", 9),
            _inc_excluded("Personal expenses like laundry, phone calls, or mini-bar usage", 10),
            _inc_excluded("Meals and liquor not explicitly mentioned in the plan", 11),
            _inc_excluded("Optional water sports, camera tickets, or tips", 12),
            _inc_excluded("Mandatory travel or medical insurance", 13),
        ],
    )
    return package, itinerary


def build_dd_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DD-014"
    tour_code = "TG-DD-014-PREM"
    title = "Grand Coastal Daman & Diu Panorama"
    duration = "06 Nights / 07 Days"
    slug = "dd-014-grand-coastal-daman-diu-panorama"
    itin_slug = "dd-014-grand-coastal-daman-diu-panorama-itinerary"
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
            _ph("State / Country: Daman and Diu / India | Category: Leisure Coastal Panorama", 2),
            _ph("Destinations: Daman • Diu Coastal Belt", 3),
            _ph("Ideal for: Families, Couples & Luxury Seekers", 4),
            _ph("Best season: November to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Independent Travel (FIT) with 24/7 dedicated local assistance", 7),
            _ph("Vehicle: Premium, ultra-comfortable Air-Conditioned Sedan / SUV at your disposal", 8),
            _ph("Meal Blueprint: Modified American Plan (Sumptuous Daily Breakfast & Curated Dinners)", 9),
            _ph("Route Map: Daman Enclave (2 Nights) → Coastal Transit / Flight → Diu Enclave (4 Nights)", 10),
            _ph("TRAGUIN Signature Experience: Private sunset boat cruise and curated colonial heritage walks", 11),
            _ph("Shopping: Handmade leather goods, sea shell artifacts, authentic Portuguese port wine", 12),
            _ph("Important: Check-in 14:00 hrs; cooperate with Diu speed limits; ideal season November to March", 13),
        ],
        moods=["Beach", "Heritage", "Luxury"],
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
        tagline="Grand Coastal Daman & Diu Panorama • 06 Nights / 07 Days",
        overview=(
            "Immerse yourself in the captivating colonial charm and golden coastal horizons of India's twin paradises. "
            "Beautifully curated by TRAGUIN travel experts, this premium luxury itinerary offers a breathtaking combination "
            "of sun-kissed beaches, grand Portuguese architecture, and absolute serenity. From the imposing ramparts of Diu "
            "Fort to the tranquil shores of Jampore Beach, every single detail is precisely arranged. Indulge in premium "
            "stays at handpicked hotels, explore iconic attractions through highly personalized sightseeing tours, and create "
            "unforgettable memories along the pristine Arabian Sea coastline.\n\n"
            "This flagship Best Daman and Diu Tour Package is customized explicitly for discerning guests looking to escape "
            "into a world of maritime history and relaxed coastal luxury. To avoid long road transits, TRAGUIN recommends "
            "utilizing regional flight connections or high-end private transfers, ensuring complete relaxation across both "
            "beautiful enclaves.\n\n"
            "TRAGUIN Curated Note: Includes a private sundowner yacht experience, priority access to historical sites, and "
            "specialized seafood tasting menus tailored to your culinary preferences.\n\n"
            "Why Visit Daman & Diu: Unique fusion of vibrant Portuguese heritage, exceptionally clean beaches, tax-friendly "
            "leisure lanes, and spectacular coastal seafood cuisine. Famous Attractions: Moti Daman Fort, St. Paul's Church "
            "Diu, Naida Caves, Nagoa Beach, and Jampore Beach. Most Searched Experiences: Exploring the illuminated paths of "
            "Naida Caves, sunset sailing, and walking through the historic quarters of Moti Daman."
        ),
        seo_title="DD-014 | Grand Coastal Daman & Diu Panorama 07-Day Tour | TRAGUIN",
        seo_description=(
            "Premium 06 Nights / 07 Days Daman and Diu panorama package (DD-014 / TG-DD-014-PREM): Jampore Beach, "
            "Moti Daman Fort, Diu Fort, Naida Caves, Ghoghla Beach, sunset boat cruise, and dual-city luxury stays."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Jampore Beach promenade & exclusive TRAGUIN beachside high-tea sunset", 1),
            _ih("Moti Daman Fort, Church of Bom Jesus, Devka Beach & colonial market walk", 2),
            _ih("Gangeshwar Mahadev Temple & Diu Fort, St. Paul's Church, St. Thomas Museum", 3),
            _ih("Naida Caves, Nagoa Beach & Blue Flag Ghoghla Beach with Portuguese quarters", 4),
            _ih("TRAGUIN Signature Experience: Private sunset boat cruise and heritage walks", 5),
            _ih("Personalized Assistance: Dedicated on-ground travel manager for smooth transits", 6),
        ],
        days=[
            _day(
                1,
                "Arrival in Daman | Coastal Sundowner Experience",
                (
                    "Begin your grand vacation as you arrive in the historic port town of Daman. Our professional TRAGUIN "
                    "representative will receive you with premium welcome amenities and escort you directly to your handpicked "
                    "beachside luxury resort. After a smooth check-in, take your time to unpack and relax. In the late afternoon, "
                    "we drive to the famous Jampore Beach, known for its dark sands and exceptionally calm waters. Enjoy an "
                    "immersive experience as you stroll along the newly constructed seaside promenade, feeling the gentle sea "
                    "breeze. Toast to the beginning of your journey with a private beachside high-tea arrangement, watching "
                    "the sun dip elegantly below the Arabian Sea."
                ),
                [
                    "Sightseeing Included: Jampore Beach & Promenade Walk",
                    "Evening Experience: Exclusive TRAGUIN Beachside High-Tea Sunset Experience",
                    "Overnight Stay: Daman (Premium Beachfront Property)",
                    "Meals Included: Curated Dinner",
                ],
            ),
            _day(
                2,
                "Moti Daman Architecture & Devka Beach Vibes",
                (
                    "Savor a delightful breakfast before diving deep into the history of Daman. We cross the river to explore "
                    "Moti Daman Fort, an expansive 16th-century Portuguese fortress enclosing beautifully preserved colonial "
                    "buildings. Walk inside the Church of Bom Jesus to marvel at its magnificent gold-gilded altars and detailed "
                    "woodwork. Later, visit the Dominican Monastery ruins, showcasing dramatic stone arches perfect for "
                    "photography. In the afternoon, explore Devka Beach, where you can unwind at premium beachside cafes. End "
                    "your day with a drive through the local markets, looking at traditional leather crafts and woven mats."
                ),
                [
                    "Sightseeing Included: Moti Daman Fort, Church of Bom Jesus, Devka Beach",
                    "Optional Activities: Guided photography walk through colonial streets",
                    "Overnight Stay: Daman",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                3,
                "Transit to Diu | Welcome to the Sun-Kissed Island",
                (
                    "After breakfast, bid farewell to Daman as you proceed with a comfortable transfer to the magical island of "
                    "Diu (via a short regional flight or a seamless private highway transfer). Upon stepping foot in Diu, the "
                    "refreshing island breeze welcomes you. Check into your ultra-luxury resort near Nagoa Beach. Spend your "
                    "afternoon relaxing inside a private beach cabana or enjoying the premium wellness spa at your resort. In the "
                    "evening, visit the serene Gangeshwar Mahadev Temple, where five ancient Shiva Lingas sit on the rocky "
                    "shore, gently washed by the tidal waves of the sea — a deeply moving spiritual experience."
                ),
                [
                    "Sightseeing Included: Gangeshwar Mahadev Coastal Temple",
                    "Evening Experience: Leisure resort time & beachside starlight walk",
                    "Overnight Stay: Diu (Luxury Oceanfront Resort)",
                    "Meals Included: Breakfast & Gourmet Dinner",
                ],
            ),
            _day(
                4,
                "Imposing Diu Fort & St. Paul's Colonial Grandeur",
                (
                    "Dedicate your morning to discovering the iconic historical sites of Diu. We begin at the majestic Diu Fort, a "
                    "massive sandstone structure surrounded by the sea on three sides. Walk past old iron cannons, look out at "
                    "the deep blue sea, and visit the lighthouse for panoramic views of the island. Next, visit St. Paul's "
                    "Church, famous for its magnificent white Baroque facade and intricate wood carvings. In the afternoon, step "
                    "inside the nearby Diu Museum, housed in the old St. Thomas Church. This evening, TRAGUIN schedules an "
                    "exclusive sunset boat cruise along the coast, giving you unmatched views of the illuminated fortress from "
                    "the water."
                ),
                [
                    "Sightseeing Included: Diu Fort, St. Paul's Church, St. Thomas Museum",
                    "Evening Experience: Exclusive TRAGUIN Private Sunset Boat Cruise",
                    "Overnight Stay: Diu",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                5,
                "Mystical Naida Caves & Nagoa Beach Adventure",
                (
                    "Prepare for an unforgettable morning at the spectacular Naida Caves, located just outside the city walls. "
                    "This natural labyrinth of rock formations features hollowed roofs, allowing shafts of sunlight to cut "
                    "through the darkness, creating an incredible setting for photography. Spend hours exploring the caves before "
                    "heading to Nagoa Beach, a beautiful horse-shoe shaped bay known for its calm waters and unique Hoka palm "
                    "trees. For adventure seekers, optional water sports like parasailing, jet-skiing, and speed boating are "
                    "available under expert supervision."
                ),
                [
                    "Sightseeing Included: Naida Caves exploration, Nagoa Beach leisure",
                    "Optional Activities: High-end water sports & paramotoring adventures",
                    "Overnight Stay: Diu",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                6,
                "Ghoghla Beach Retreat & Insular Village Trails",
                (
                    "On your final full day in paradise, visit Ghoghla Beach, the largest and cleanest golden-sand beach in Diu, "
                    "proud holder of the international Blue Flag certification. This destination offers a peaceful escape from "
                    "the crowds, perfect for swimming or sunbathing. In the afternoon, enjoy a curated heritage tour through the "
                    "quiet lanes of local fishing villages and Portuguese quarters, observing old houses decorated with "
                    "traditional tiles. Conclude your evening with an exclusive seafood culinary dinner hosted by our resort "
                    "chef, celebrating your magnificent coastal journey."
                ),
                [
                    "Sightseeing Included: Blue Flag Ghoghla Beach, Old Portuguese Quarters",
                    "Evening Experience: Grand Seafood Fare & Farewell Wine Tasting",
                    "Overnight Stay: Diu",
                    "Meals Included: Breakfast & Farewell Dinner",
                ],
            ),
            _day(
                7,
                "Bid Adieu to the Coastal Enclaves",
                (
                    "Savor a beautiful final breakfast at your resort, watching the morning waves wash onto the shore. Your "
                    "dedicated chauffeur will assist you with your bags and provide a smooth transfer to Diu Airport or your "
                    "designated exit station. Your luxury travel experience concludes seamlessly, leaving you with unforgettable "
                    "memories and stories of a lifetime."
                ),
                [
                    "Sightseeing Included: None (Departure transfer only)",
                    "Assistance: Full baggage handling & check-in coordination",
                    "Overnight Stay: Tour Concludes",
                    "Meals Included: Elite Buffet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel("The Deltin, Daman (Superior Room) / Radisson Diu / Hotel Kohinoor", "Daman & Diu", "02N Daman + 04N Diu", "Deluxe", "Superior Room / Deluxe Room", "Breakfast & Dinner", 4, 1),
            _hotel("Gold Beach Resort (Ocean View) / Azzaro Resorts & Spa (Club Room)", "Daman & Diu", "02N Daman + 04N Diu", "Premium", "Ocean View / Club Room", "Breakfast & Dinner", 5, 2),
            _hotel("The Fern Seaside Luxurious Resort / The Fern Seaside Resort, Diu", "Daman & Diu", "02N Daman + 04N Diu", "Luxury", "Luxury Sea View Suite", "Breakfast & Dinner", 5, 3),
            _hotel("TRAGUIN Private Executive Suites / TRAGUIN Custom Beachfront Villas", "Daman & Diu", "02N Daman + 04N Diu", "Ultra Luxury", "Executive Suite / Beachfront Villa", "All Inclusive Gourmet", 5, 4),
        ],
        inclusions=[
            _inc_included("02 Nights in Daman & 04 Nights in Diu at premium stays", 1),
            _inc_included("Daily multi-cuisine buffet breakfasts and premium dinners", 2),
            _inc_included("Dedicated private air-conditioned vehicle for all transfers and tours", 3),
            _inc_included("Certified English/Hindi speaking local expert guides", 4),
            _inc_included("All entry tickets to forts, museums, and churches included", 5),
            _inc_included("Exclusive private sunset boat cruise in Diu handled by TRAGUIN", 6),
            _inc_included("Full package taxes, toll charges, driver allowances, and parking fees", 7),
            _inc_included("Round-the-clock remote concierge TRAGUIN support", 8),
            _inc_excluded("National / International flights or train ticketing", 9),
            _inc_excluded("Personal items such as laundry, phone calls, or tips", 10),
            _inc_excluded("Water sports fees, paramotoring, and optional excursions", 11),
            _inc_excluded("Any additional food or alcoholic beverages not specified", 12),
            _inc_excluded("Comprehensive travel or medical insurance", 13),
        ],
    )
    return package, itinerary


DAMAN_DIU_BUILDERS = [
    build_dd_001,
    build_dd_002,
    build_dd_003,
    build_dd_004,
    build_dd_005,
    build_dd_006,
    build_dd_007,
    build_dd_008,
    build_dd_009,
    build_dd_010,
    build_dd_011,
    build_dd_012,
    build_dd_013,
    build_dd_014,
]
