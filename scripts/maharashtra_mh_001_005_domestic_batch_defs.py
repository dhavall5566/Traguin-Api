"""Builder functions for MH-001 through MH-005 Maharashtra domestic packages."""

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

MAHARASHTRA_SLUG = "maharashtra"
MAHARASHTRA_DESTINATION_ID = "b2dd36c1-dc9b-47bf-92d3-08bfa5f7de59"


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


def build_mh_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "MH-001"
    tour_code = "TRAGUIN-MUM-LON-001"
    title = "Mumbai & Lonavala Luxury Family Tour"
    duration = "04 Nights / 05 Days"
    slug = "mh-001-mumbai-lonavala-luxury-family-tour"
    itin_slug = "mh-001-mumbai-lonavala-luxury-family-tour-itinerary"
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
            _ph("State / Country: Maharashtra, India | Category: Premium Family Vacation", 2),
            _ph("Destinations: Mumbai • Lonavala • Khandala", 3),
            _ph("Ideal for: Families, Couples, Luxury Seekers", 4),
            _ph("Best season: October to March (Plus Lush Monsoons)", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Luxury Family Tour (FIT)", 7),
            _ph("Vehicle: Private Premium SUV (Innova Crysta / Luxury Sedan)", 8),
            _ph("Meal Plan: Breakfast & Handpicked Curated Dinners (MAPAI)", 9),
            _ph("Route Map: Mumbai (2N) ➔ Lonavala & Khandala (2N) ➔ Mumbai Departure", 10),
            _ph(
                "TRAGUIN Signature Experience: Bespoke amenities and 24/7 dedicated concierge support with private sunset yacht sailing in South Mumbai",
                11,
            ),
            _ph(
                "Shopping: Colaba Causeway antiquities and Palladium designer malls; Maganlal Chikki and warm Bhutta at Tiger Point in Lonavala",
                12,
            ),
            _ph(
                "Important: Standard check-in 14:00 hrs, check-out 11:00 hrs; monsoon may affect Elephanta ferry; book 45 days ahead in peak season",
                13,
            ),
        ],
        moods=["Family", "Luxury", "Couples"],
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
        tagline="The Ultimate Mumbai & Lonavala Luxury Family Tour • 4 Nights / 5 Days",
        overview=(
            "Welcome to an extraordinary journey meticulously crafted by TRAGUIN. This exclusive luxury Maharashtra holiday seamlessly bridges the high-octane energy, heritage romance, and glamorous allure of India's commercial capital, Mumbai, with the serene mist-kissed highlands, breathtaking landscapes, and emerald-green valleys of Lonavala and Khandala. Designed to deliver an unparalleled, deeply immersive family experience, this bespoke getaway effortlessly blends world-class luxury, private chauffeured transfers, signature handpicked accommodations, and deeply engaging historical explorations to construct memories that will be cherished for a lifetime.\n\n"
            "Your bespoke TRAGUIN travel itinerary begins in Mumbai, where the colonial-era architecture stands gracefully alongside shimmering modern skyscrapers. Experience the absolute finest elements of a premium Mumbai vacation package, spanning from private luxury yacht sailings against the Arabian Sea sunset to intimate, privately guided walks down historic lanes. You will then ascend to the Sahyadri mountains via a beautifully scenic route to immerse yourselves in a premium Lonavala experience. Surrounded by cascading seasonal waterfalls, dramatic cliffs, and absolute tranquility, your family will discover the pinnacle of luxury, rejuvenation, and comfort.\n\n"
            "Why Visit Mumbai and Lonavala? This iconic pairing delivers the ultimate dual-world Indian holiday—combining an ultra-luxury urban experience with an exquisite mountain retreat. Mumbai, widely celebrated as the City of Dreams, captivates multi-generational families with its magnificent UNESCO World Heritage architectural sites, rich Bollywood culture, and phenomenal seaside promenades. Lonavala complements this high-energy vibe by providing a refreshing alpine sanctuary famous for its pristine natural eco-systems, majestic ancient rock-cut caves, and panoramic viewpoints.\n\n"
            "Top Tourist Places & Instagram Locations: Capture striking family photographs at the monumental Gateway of India, the iconic sea-skimming Marine Drive arc, the dramatic Taj Mahal Palace, the historic Chhatrapati Shivaji Maharaj Terminus, and the spectacular, misty cliffs of Tiger Point and Duke's Nose in Lonavala. This specialized TRAGUIN Maharashtra package guarantees that you experience these world-famous sightseeing marvels completely away from the crowds, utilizing expertly timed VIP access passes and private localized guidance."
        ),
        seo_title="MH-001 | Mumbai & Lonavala Luxury Family Tour | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Mumbai & Lonavala luxury family tour (MH-001 / TRAGUIN-MUM-LON-001): "
            "Gateway of India, Elephanta Caves, Karla & Bhaja Caves, Tiger Point, private yacht cruise, and 4-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Gateway of India, Marine Drive, Colaba & Private Sunset Harbor Cruise", 1),
            _ih("Elephanta Caves UNESCO Heritage, Bandra, Juhu Beach, Mani Bhavan & Sea Link", 2),
            _ih("Khandala Valley, Karla & Bhaja Caves, Bhushi Dam, Tiger Point & Duke's Nose", 3),
            _ih("TRAGUIN Signature Experience: Private family sunset sailing in South Mumbai with dedicated on-board hospitality", 4),
            _ih("Premium Handpicked Hotels: Rigorously inspected properties across Mumbai and Lonavala with elite service", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Mumbai | Welcome to the Glamorous City of Dreams",
                (
                    "Arrive at Mumbai's Chhatrapati Shivaji Maharaj International Airport or terminal, where a dedicated "
                    "TRAGUIN luxury travel representative will warmly greet your family with premium welcome amenities and a "
                    "private chauffeured luxury vehicle. Transfer smoothly to your iconic heritage luxury hotel overlooking the sea. "
                    "After checking in and relaxing, embark on an enchanting afternoon exploration of South Mumbai's architectural "
                    "treasures. Drive past the majestic Victoria Terminus and the regal Buildings of Fort, concluding with an evocative "
                    "stroll at the Gateway of India. As evening falls, step onto a private luxury sailing boat arranged exclusively for you "
                    "by TRAGUIN, enjoying the refreshing ocean breeze and a stunning golden hour view over the Arabian Sea skyline."
                ),
                [
                    "Sightseeing Included: Gateway of India, Marine Drive, Colaba, Private Sailing",
                    "Optional Activities: High-tea at The Taj Mahal Palace Sea Lounge",
                    "Evening Experience: Sunset private harbor cruise with customized mocktails",
                    "Overnight Stay: Mumbai Premium Luxury Hotel",
                    "Meals Included: Gourmet Dinner",
                ],
            ),
            _day(
                2,
                "Comprehensive Mumbai Sightseeing | Heritage, Culture & Coastal Glamour",
                (
                    "Savor a magnificent multi-cuisine breakfast before diving into the definitive Mumbai sightseeing experience. "
                    "Begin your morning with a fascinating private ferry cruise to the legendary, ancient rock-cut Elephanta Caves, a "
                    "beautifully preserved UNESCO World Heritage Site filled with mystical carvings. Returning to the mainland, enjoy a "
                    "bespoke lunch at a celebrated fine-dining restaurant in Colaba. In the afternoon, take a highly scenic drive across the "
                    "engineering marvel that is the Rajiv Gandhi Sea Link to explore the upscale neighborhoods of Bandra, driving past the "
                    "luxurious private residences of Bollywood's most iconic superstars. Conclude your evening with an unwinding walk along "
                    "the Queen's Necklace at Marine Drive as the entire city lights up."
                ),
                [
                    "Sightseeing Included: Elephanta Caves, Bandra, Juhu Beach, Mani Bhavan, Sea Link",
                    "Optional Activities: Private Bollywood studio tour with dance experience",
                    "Evening Experience: Coastal fine-dining and seaside sunset photography",
                    "Overnight Stay: Mumbai Premium Luxury Hotel",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                3,
                "Mumbai to Lonavala | Ascending to the Mystical Sahyadri Highlands",
                (
                    "Bid farewell to the coastal metropolis as your premium chauffeured SUV begins a highly scenic journey toward the "
                    "mountains for your exclusive Lonavala family tour. Ascend into the beautiful western ghats via the expansive expressway, "
                    "stopping along the way to witness the breathtaking landscapes and misty panoramas of Khandala. Check into your ultra-luxury "
                    "mountain resort, a handpicked sanctuary featuring private temperature-controlled plunge pools and spectacular views of the "
                    "valley. Spend your afternoon enjoying an immersive private nature trail curated by TRAGUIN experts to witness native flora "
                    "and hidden streams, or unwind completely within the resort's premium luxury spa facility."
                ),
                [
                    "Sightseeing Included: Khandala Valley, Amrutanjan Point, Resort Eco-Trails",
                    "Optional Activities: Premium organic aroma-therapy spa treatment",
                    "Evening Experience: Private candle-lit patio dinner overlooking illuminated cliffs",
                    "Overnight Stay: Lonavala Ultra-Luxury Hill Resort",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                4,
                "Lonavala Sightseeing | Ancient Caves, Waterfalls & Iconic Viewpoints",
                (
                    "Awaken to the soothing sounds of mountain birds and a refreshing alpine breeze. Today features the definitive Lonavala "
                    "sightseeing journey. Visit the historical Karla and Bhaja Caves, extraordinary ancient Buddhist shrines carved intricately "
                    "into rock faces dating back to the 2nd century BC. Next, visit the sparkling waters of Bhushi Dam, followed by an exclusive "
                    "afternoon excursion to Lonavala Lake. As late afternoon approaches, your private guide will escort you to Tiger Point and "
                    "Duke's Nose, where clouds literally drift past your feet. Indulge in hot local delicacies and tea while watching the sunset "
                    "over deeply carved canyons, capturing unforgettable family memories."
                ),
                [
                    "Sightseeing Included: Karla Caves, Bhushi Dam, Tiger Point, Celebrity Wax Museum",
                    "Optional Activities: Hot-air balloon flight over the lush valley landscapes",
                    "Evening Experience: Local shopping trail for premium hand-crafted Chikki and crafts",
                    "Overnight Stay: Lonavala Ultra-Luxury Hill Resort",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                5,
                "Lonavala to Mumbai | Cherishing Unforgettable Premium Memories",
                (
                    "Enjoy a leisurely breakfast on your private balcony, taking in the serene mountain scenery one final time. Spend your morning "
                    "at absolute relaxation inside the resort, enjoying a family swim or purchasing artisanal local souvenirs. At the designated "
                    "check-out time, your professional chauffeur will assist with luggage and drive you safely down the hills back to Mumbai. Your "
                    "dedicated TRAGUIN holiday concludes as you are smoothly dropped off at the airport, railway terminal, or your residence, carrying "
                    "a treasure trove of unforgettable luxury memories from your premium Maharashtra escape."
                ),
                [
                    "Sightseeing Included: Scenic return drive across the Western Ghats",
                    "Optional Activities: En-route gourmet lunch stop at a premium highway estate",
                    "Evening Experience: Warm farewell at the airport departure gate",
                    "Overnight Stay: Departure / End of Services",
                    "Meals Included: Rich Buffet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Trident Nariman Point / Vivanta Cuffe Parade | Fariyas Resort Lonavala / Citrus Hotel",
                "Mumbai (2N) / Lonavala (2N)",
                "04 Nights",
                "Deluxe",
                "Superior Sea-View Room (CP) / Deluxe Valley View Room (MAP)",
                "CP Mumbai & MAP Lonavala",
                4,
                1,
            ),
            _hotel(
                "The St. Regis Mumbai / InterContinental | Della Resorts Lonavala",
                "Mumbai (2N) / Lonavala (2N)",
                "04 Nights",
                "Premium",
                "Premium City / Sea Vista Room (CP) / Luxury Resort Room (MAP)",
                "CP Mumbai & MAP Lonavala",
                5,
                2,
            ),
            _hotel(
                "The Taj Mahal Palace & Tower | The Machan / Hilton Shillim Estate Spa Retreat",
                "Mumbai (2N) / Lonavala (2N)",
                "04 Nights",
                "Luxury",
                "Luxury Tower Sea View Wing (CP) / Canopy Machan or Valley Villa (MAP)",
                "CP Mumbai & MAP Lonavala",
                5,
                3,
            ),
            _hotel(
                "The Taj Mahal Palace - Palace Wing | Hilton Shillim Estate Spa Retreat",
                "Mumbai (2N) / Lonavala (2N)",
                "04 Nights",
                "Ultra Luxury",
                "Luxury Grand Heritage Suite with Private Butler (CP) / Private Pool Villa with Wellness Concierge (MAP)",
                "CP Mumbai & MAP Lonavala",
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included("Elite Accommodation: 04 Nights stay in handpicked, premier luxury properties across Mumbai & Lonavala.", 1),
            _inc_included("Bespoke Meal Plan: Daily lavish breakfast spreads and specialized multi-course culinary dinners.", 2),
            _inc_included(
                "Luxury Transportation: All transfers, long-distance touring, and city sightseeing via an exclusive private premium SUV.",
                3,
            ),
            _inc_included(
                "TRAGUIN Signature Welcoming: Traditional flower garland welcome, cold towels, and a premium curated fruit basket upon arrival.",
                4,
            ),
            _inc_included("Private Nautical Sailing: 1-Hour exclusive sunset luxury yacht cruise on the Arabian Sea in Mumbai.", 5),
            _inc_included(
                "VIP Access & Entry: Pre-booked entry tickets and private professional guides for Elephanta Caves and Karla Caves.",
                6,
            ),
            _inc_included(
                "Full Professional Coverage: All toll fees, border taxes, driver allowances, fuel charges, and state permits are completely covered.",
                7,
            ),
            _inc_included("TRAGUIN Support: Continuous 24/7 real-time remote concierge support from senior travel specialists.", 8),
            _inc_excluded("Domestic or International airfares, flight bookings, or main interstate train ticket expenses.", 9),
            _inc_excluded(
                "Personal incidental expenses such as laundry services, mini-bar consumption, telephone calls, and room service.",
                10,
            ),
            _inc_excluded(
                "Any specialized adventure activities, camera/video usage fees at monuments, or optional sightseeing detours.",
                11,
            ),
            _inc_excluded("Any meals, lunches, or beverage selections not specifically detailed in the official itinerary.", 12),
            _inc_excluded(
                "Mandatory peak festive season surcharges (applicable during Christmas, New Year, and major national holiday weeks).",
                13,
            ),
            _inc_excluded("Travel insurance coverage and medical expenses of any nature.", 14),
        ],
    )
    return package, itinerary


def build_mh_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "MH-002"
    tour_code = "TRAGUIN-SHIRDI-002"
    title = "Premium Shirdi Pilgrimage Package"
    duration = "02 Nights / 03 Days"
    slug = "mh-002-premium-shirdi-pilgrimage-package"
    itin_slug = "mh-002-premium-shirdi-pilgrimage-package-itinerary"
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
            _ph("State / Country: Maharashtra, India | Category: Premium Pilgrimage / Divine Escape", 2),
            _ph("Destinations: Shirdi • Shani Shingnapur • Nashik", 3),
            _ph("Ideal for: Families, Devotees, Multi-generational Groups", 4),
            _ph("Best season: Year-round (Pleasant Winters Oct-Mar)", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Luxury Pilgrimage Tour (FIT)", 7),
            _ph("Vehicle: Private Premium SUV (Innova Crysta / Luxury Coach)", 8),
            _ph("Meal Plan: Gourmet Vegetarian Breakfast & Dinner (MAPAI)", 9),
            _ph("Route Map: Mumbai/Pune ➔ Shirdi (2N) ➔ Shani Shingnapur ➔ Nashik ➔ Return", 10),
            _ph(
                "TRAGUIN Signature Experience: VIP Pass arrangement and 24/7 dedicated concierge with private family VIP Darshan coordination",
                11,
            ),
            _ph(
                "Shopping: Authentic brass Sai Baba idols, incense, Rudraksha beads, Ladoo Prasad; Nashik table grapes and raisins",
                12,
            ),
            _ph(
                "Important: Conservative traditional clothing at temples; mobile phones prohibited in Samadhi Mandir; book 30 days ahead for VIP slots",
                13,
            ),
        ],
        moods=["Pilgrimage", "Spiritual", "Family"],
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
        tagline="The Ultimate Shirdi Darshan & Divine Family Tour • 2 Nights / 3 Days",
        overview=(
            "Welcome to a divine spiritual journey thoughtfully curated by TRAGUIN. This exclusive luxury Shirdi holiday is designed to soothe your soul and elevate your spiritual senses, guiding you seamlessly through the most sacred thresholds of Maharashtra. Experience the tranquil divinity of the world-renowned Shirdi Sai Baba Temple, coupled with unique visits to the magical, doorless village of Shani Shingnapur and the ancient riverside heritage of Nashik. Combining absolute comfort, private VIP entries, premium handpicked hotels, and a flawless chauffeured ride, this premium travel itinerary ensures your family returns transformed, bearing unforgettable memories of profound peace.\n\n"
            "Your bespoke TRAGUIN pilgrimage begins with your arrival in Mumbai or Pune, from where a private premium vehicle sweeps you across beautiful highway corridors directly to the spiritual capital of Shirdi. Your exclusive tour incorporates a perfectly timed VIP Shirdi Darshan experience, shielding your multi-generational family from tedious waiting times. Delve deep into the local lore, witness the evening or early-morning sacred Kakad Aarti, and explore breathtaking landscapes and historic temples along the sacred Godavari riverbanks, all while surrounded by exceptional luxury and personalized assistance.\n\n"
            "Why Visit Shirdi and Surrounding Shrines? As India's most highly venerated spiritual epicenter, a Shirdi family tour serves as a beautiful anchor for family bonding, reflection, and rejuvenation. Millions seek out the benevolent gaze of Sai Baba, making a Luxury Shirdi Holiday one of the most searched experiences in heritage tourism. Beyond the main temple, the adjoining destinations offer immersive experiences: the profound planetary energy at Shani Shingnapur and the epic Ramayana heritage landmarks situated in holy Nashik.\n\n"
            "Top Tourist Places & Instagram Locations: Capture beautifully serene and timeless frames at the intricately adorned Sai Baba Samadhi Mandir, the historical Dwarkamai mosque, the peaceful Lendi Baug gardens, the colossal stone idol of Shani Dev, and the dramatic, ancient steps of Panchavati and Ram Kund along the river in Nashik. This custom TRAGUIN Shirdi package prioritizes specialized timing and localized private support to maximize comfort and photography options for your elders and children alike."
        ),
        seo_title="MH-002 | Premium Shirdi Pilgrimage Package | TRAGUIN",
        seo_description=(
            "Premium 02 Nights / 03 Days Shirdi pilgrimage package (MH-002 / TRAGUIN-SHIRDI-002): "
            "VIP Shirdi Darshan, Shani Shingnapur, Nashik Panchavati, Kalaram Temple, and 4-tier handpicked Shirdi accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Sai Baba Samadhi Temple, Dwarkamai, Chavadi, Gurusthan & Kakad Aarti", 1),
            _ih("VIP Shirdi Darshan, Shani Shingnapur Temple & Lendi Baug", 2),
            _ih("Panchavati, Kalaram Temple, Sita Gufi & Ram Kund Godavari", 3),
            _ih("TRAGUIN Signature Experience: Private family VIP Darshan coordination with a dedicated local representative", 4),
            _ih("Premium Handpicked Hotels: Serene, smoke-free properties with pure, high-quality vegetarian food options", 5),
        ],
        days=[
            _day(
                1,
                "Arrival & Shirdi Transfer | Stepping into the Realm of Serenity",
                (
                    "Your premium spiritual adventure commences as your private luxury chauffeur welcomes you directly at your airport terminal "
                    "or doorstep in Mumbai/Pune. Settle into your premium vehicle and embark on a smooth, scenic journey to the holy town of Shirdi. "
                    "Upon your arrival, enjoy a seamless, prioritized check-in at your handpicked premium resort. After settling into your spacious "
                    "luxury suite, step out for an introductory visit to the main temple complex. TRAGUIN has arranged prioritized entry cards for "
                    "your evening Shirdi sightseeing, giving you direct access to the main shrine, the sacred flame at Dwarkamai, and Chavadi, where "
                    "Sai Baba spent his historical nights."
                ),
                [
                    "Sightseeing Included: Sai Baba Samadhi Temple, Dwarkamai, Chavadi, Gurusthan",
                    "Optional Activities: Participation in the magnificent evening Dhoop Aarti",
                    "Evening Experience: Spiritual stroll through the historical alleys of Shirdi town",
                    "Overnight Stay: Shirdi Premium Luxury Resort",
                    "Meals Included: Gourmet Vegetarian Dinner",
                ],
            ),
            _day(
                2,
                "VIP Shirdi Darshan & Shani Shingnapur Excursion | Divine Radiance",
                (
                    "Awaken early for the soul-stirring Kakad Aarti or a premium morning VIP Shirdi Darshan session precisely coordinated by your "
                    "TRAGUIN travel advisor to ensure absolute ease. Experience a profound sense of calm standing before the radiant white marble idol "
                    "of Sai Baba. Return to your resort for a hearty, multi-cuisine breakfast. In the afternoon, enjoy a highly scenic drive through "
                    "rural Maharashtra to visit the legendary Shani Shingnapur temple. This fascinating village is globally famous because houses feature "
                    "no doors or locks, protected by the deep faith in Lord Shani. Pay your respects at the open-sky rock shrine before returning to "
                    "Shirdi for a relaxed evening."
                ),
                [
                    "Sightseeing Included: Early Morning Shrine Access, Shani Shingnapur Temple, Lendi Baug",
                    "Optional Activities: Private Satyanarayan Pooja inside temple vicinity",
                    "Evening Experience: Soulful meditation session within the resort's private gardens",
                    "Overnight Stay: Shirdi Premium Luxury Resort",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                3,
                "Shirdi to Nashik Heritage Exploration | Departure via Holy Panchavati",
                (
                    "Enjoy a leisurely breakfast before checking out of your hotel. Your private chauffeur will drive you to the historical temple city "
                    "of Nashik, a key site of the ancient Kumbh Mela. Explore the holy Panchavati region, visiting the ancient Kalaram Temple and the "
                    "mystical Sita Gufi caves, where Ramayana legends come to life. Witness the sacred rituals at Ram Kund on the Godavari riverbanks, "
                    "capturing the spiritual essence of India. Following a premium lunch at a heritage estate, your luxury vehicle carries you back "
                    "smoothly to Mumbai or Pune, concluding your magnificent TRAGUIN Shirdi package with hearts full of blessings and unforgettable memories."
                ),
                [
                    "Sightseeing Included: Panchavati, Kalaram Temple, Sita Gufi, Ram Kund Godavari",
                    "Optional Activities: Traditional family blessing ritual along the holy riverbanks",
                    "Evening Experience: Scenic highway return ride with sunset photography stops",
                    "Overnight Stay: Departure / End of Services",
                    "Meals Included: Rich Buffet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Sun N Sand Shirdi / Hotel Sai Jharokha",
                "Shirdi",
                "02 Nights",
                "Deluxe",
                "Executive Room",
                "Buffet Breakfast & Dinner (MAP)",
                4,
                1,
            ),
            _hotel(
                "St Laurn The Spiritual Resort Shirdi",
                "Shirdi",
                "02 Nights",
                "Premium",
                "Premium Pool-View Room",
                "Buffet Breakfast & Dinner (MAP)",
                4,
                2,
            ),
            _hotel(
                "Marigold Regency / Goradia's Lords Inn",
                "Shirdi",
                "02 Nights",
                "Luxury",
                "Luxury Heritage Suite",
                "Premium Ala-Carte Menu (MAP)",
                5,
                3,
            ),
            _hotel(
                "The Gateway Hotel (Ambad Nashik / Shirdi Luxury Wing)",
                "Shirdi",
                "02 Nights",
                "Ultra Luxury",
                "Executive Sanctuary Suite with VIP Escort",
                "Curated Wellness Meals (MAP)",
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included("Premium Stays: 02 Nights accommodation in selected top-tier spiritual luxury properties in Shirdi.", 1),
            _inc_included("Gourmet Dining: Daily expansive vegetarian breakfasts and multi-course buffet dinners at the resorts.", 2),
            _inc_included("Private Transfers: Entire route and sightseeing covered via an exclusive premium SUV (Innova Crysta).", 3),
            _inc_included("TRAGUIN VIP Assistance: Pre-arranged VIP Darshan passes for seamless, queue-free temple access.", 4),
            _inc_included("Welcome Amenities: Traditional shawl presentation, fresh coconut welcoming drinks, and holy sweets boxes.", 5),
            _inc_included("Expert Local Guiding: Private knowledgeable heritage guides at Shani Shingnapur and Nashik Panchavati.", 6),
            _inc_included(
                "All-Inclusive Coverage: All parking, toll charges, driver allowances, state fuel taxes, and night surcharges are included.",
                7,
            ),
            _inc_included("TRAGUIN Support: Continuous 24/7 dedicated telephone and on-ground assistance from our senior team.", 8),
            _inc_excluded("Airfares, helicopter ticketing, or main interstate railway tickets.", 9),
            _inc_excluded(
                "Personal charges like laundry, telephone calls, mini-bar orders, or specialized temple offerings (Prasad/Dakshina).",
                10,
            ),
            _inc_excluded("Specialized video camera permissions or additional pooja costs inside the temples.", 11),
            _inc_excluded("Any mid-day meals or lunches not explicitly detailed in the final confirmation voucher.", 12),
            _inc_excluded("Festival peak period surcharges (e.g., Guru Purnima, Dussehra, Diwali, or New Year weeks).", 13),
            _inc_excluded("Travel insurance protections or personal medical expenses.", 14),
        ],
    )
    return package, itinerary


def build_mh_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "MH-003"
    tour_code = "TRAGUIN-MHA-AJ-EL-003"
    title = "Premium Ajanta Ellora Heritage Tour"
    duration = "03 Nights / 04 Days"
    slug = "mh-003-ajanta-ellora-heritage-tour"
    itin_slug = "mh-003-ajanta-ellora-itinerary"
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
            _ph("State / Country: Maharashtra, India | Category: Luxury Heritage Journey", 2),
            _ph("Destinations: Chhatrapati Sambhajinagar (Aurangabad) • Ajanta • Ellora", 3),
            _ph("Ideal for: Heritage Connoisseurs, Families, Historians", 4),
            _ph("Best season: October to March (Ideal Weather)", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Luxury Heritage Tour (FIT)", 7),
            _ph("Vehicle: Private Premium SUV (Innova Crysta / Luxury Sedan)", 8),
            _ph("Meal Plan: Breakfast & Curated Local Gourmet Dinners (MAPAI)", 9),
            _ph("Route Map: Sambhajinagar Arrival ➔ Ajanta Caves ➔ Ellora Caves & Fort ➔ Departure", 10),
            _ph(
                "TRAGUIN Signature Experience: Archeological guide encounters tracing ancient trade routes with 24/7 dedicated concierge support",
                11,
            ),
            _ph(
                "Shopping: Himroo shawls and Paithani silk sarees at genuine artisan looms; Aurangabadi Naan Qalia heritage cuisine",
                12,
            ),
            _ph(
                "Important: Ajanta closed Mondays, Ellora closed Tuesdays; eco-friendly shuttle required for final mile to Ajanta; book 30-45 days ahead",
                13,
            ),
        ],
        moods=["Heritage", "Luxury", "Family"],
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
        tagline="The Absolute Finest Heritage Discovery & Luxury Holiday • 3 Nights / 4 Days",
        overview=(
            "Welcome to an unforgettable odyssey into antiquity, meticulously crafted by the destination experts at TRAGUIN. This exclusive luxury Ajanta Ellora tour package unfolds the majestic legacy of ancient India across the rocky heart of Maharashtra. Journey back through two millennia to unravel breathtaking landscapes, world-renowned rock-cut architecture, and fine spiritual art. Melding private, premium chauffeured comfort, signature handpicked hotels, and world-class archeological guidance, this premium experience promises to transform a deep cultural exploration into timeless family memories.\n\n"
            "Your bespoke TRAGUIN travel itinerary centers on Chhatrapati Sambhajinagar (formerly Aurangabad), the ultimate gateway to India's most celebrated UNESCO World Heritage architectural sites. On this luxury holiday, you will stand in awe before the majestic monoliths of Ellora, step into the fresco-adorned sanctuaries of the ancient Ajanta Caves, and trace the royal legacy of the Deccan at Bibi Ka Maqbara and Daulatabad Fort. Experience a perfectly paced, premium family tour complete with private luxury transfers, gourmet dining, and our signature hospitality amenities.\n\n"
            "Why Visit Ajanta and Ellora? Considered the pinnacle of ancient architectural engineering, these twin temple networks present a profound artistic journey. The Ajanta Caves house masterfully preserved Buddhist frescoes dating back to the 2nd century BCE, positioned within a dramatic, horseshoe-shaped river ravine. Meanwhile, the Ellora Caves celebrate India's ancient pluralism with 34 stunning Buddhist, Hindu, and Jain sanctuaries carved side-by-side out of the basaltic Charanandri hills.\n\n"
            "Top Tourist Places & Famous Attractions: This definitive Ajanta Ellora package covers iconic sights such as the unbelievable Kailash Temple (Cave 16)—the world's largest single rock-cut monolithic structure. You will also photograph the dramatic heights of Daulatabad Fort, the spectacular Mughal artistry of Bibi Ka Maqbara (the Taj of the Deccan), and the sacred Panchakki water mill, guaranteeing timeless photographs at popular Instagram locations away from common crowds."
        ),
        seo_title="MH-003 | Premium Ajanta Ellora Heritage Tour | TRAGUIN",
        seo_description=(
            "Premium 03 Nights / 04 Days Ajanta Ellora heritage tour (MH-003 / TRAGUIN-MHA-AJ-EL-003): "
            "Ajanta Caves, Ellora Kailash Temple, Daulatabad Fort, Bibi Ka Maqbara, Aurangabad Caves, and 4-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Bibi Ka Maqbara, Panchakki & Himroo Weaving Center", 1),
            _ih("Ajanta Cave Complex, Waghur Viewpoint & Archeological Museum", 2),
            _ih("Ellora Caves, Kailash Monolith, Daulatabad Fort & Grishneshwar", 3),
            _ih("Aurangabad Caves & Local Artisan Markets", 4),
            _ih("TRAGUIN Signature Experience: Archeological guide encounters tracing ancient trade routes", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Chhatrapati Sambhajinagar | Gateway to Deccan Grandeur",
                (
                    "Arrive at Chhatrapati Sambhajinagar Airport or Railway Station, where a premium TRAGUIN representative awaits to extend a "
                    "traditional royal welcome. Board your private chauffeured premium SUV and transfer to your handpicked luxury hotel. In the "
                    "afternoon, embark on an immersive city sightseeing tour. Witness the architectural wonder of Panchakki, an ancient medieval water "
                    "mill engineered to power a flour mill. Next, marvel at Bibi Ka Maqbara, a stunning monument of matrimonial devotion built by Prince "
                    "Azam Shah, featuring intricate marble screens and manicured Mughal gardens. As the evening sets in, enjoy an intimate walk through "
                    "the city's historic textile quarters before enjoying a curated multi-course dinner."
                ),
                [
                    "Sightseeing Included: Bibi Ka Maqbara, Panchakki, Himroo Weaving Center",
                    "Optional Activities: Traditional Deccani high-tea at a heritage courtyard",
                    "Evening Experience: Private guided walk through the ancient gates of the city",
                    "Overnight Stay: Chhatrapati Sambhajinagar Luxury Hotel",
                    "Meals Included: Gourmet Welcome Dinner",
                ],
            ),
            _day(
                2,
                "The Miracles of Ajanta | Exploring Ancient Frescoes & Hidden Ravines",
                (
                    "Indulge in a lavish breakfast before setting off on a scenic excursion to the world-renowned Ajanta Caves, a breathtaking UNESCO "
                    "World Heritage site located approximately 100 km away. Encircled by lush forested cliffs, these 30 rock-cut caves served as secluded "
                    "monsoon retreats for ancient Buddhist monks. Accompanied by a handpicked TRAGUIN archeological storyteller, marvel at the timeless "
                    "masterpieces of ancient Indian art in Caves 1, 2, 16, and 17, including the iconic paintings of Padmapani and Vajrapani. Learn the "
                    "emotional narratives behind the Jataka tales painted with natural minerals that have glowed silently through centuries. Return to the "
                    "hotel in the late afternoon for a relaxing evening at the premium resort spa."
                ),
                [
                    "Sightseeing Included: Ajanta Cave Complex, Waghur Viewpoint, Archeological Museum",
                    "Optional Activities: Panoramic photography trek to the Ajanta horseshoe viewpoint",
                    "Evening Experience: Private screening of a documentary detailing the discovery of Ajanta",
                    "Overnight Stay: Chhatrapati Sambhajinagar Luxury Hotel",
                    "Meals Included: Breakfast & Gourmet Dinner",
                ],
            ),
            _day(
                3,
                "Monoliths of Ellora & Daulatabad Fort | Architectural Triumphs",
                (
                    "Following a premium breakfast, journey toward the jaw-dropping Ellora Caves. Your curated experience focuses first on Cave 16—the "
                    "magnificent Kailash Temple. This architectural marvel was carved from the top down out of a single solid hill, removing over 200,000 "
                    "tons of rock to reveal a structure double the size of the Parthenon. Continue onwards to explore the serene Buddhist viharas and the "
                    "detailed Jain Indra Sabha temples. In the afternoon, visit the invincible Daulatabad Fort, an extraordinary medieval hilltop fortress "
                    "featuring a complex system of defensive moats, subterranean mazes, and a soaring victory minaret. Conclude the day by paying respects "
                    "at the historic Grishneshwar Jyotirlinga Temple."
                ),
                [
                    "Sightseeing Included: Ellora Caves, Kailash Monolith, Daulatabad Fort, Grishneshwar",
                    "Optional Activities: Private culinary workshop featuring authentic Naan Qalia dishes",
                    "Evening Experience: Sundowner drinks looking out over the majestic plains of Daulatabad",
                    "Overnight Stay: Chhatrapati Sambhajinagar Luxury Hotel",
                    "Meals Included: Breakfast & Gourmet Dinner",
                ],
            ),
            _day(
                4,
                "Aurangabad Caves & Departure | Preserving Timeless Heritage Memories",
                (
                    "Savor your final morning breakfast at the resort before checking out. Today, explore the hidden gem known as the Aurangabad Caves, "
                    "twelve rock-cut Buddhist shrines carved into the hills during the 6th and 7th centuries AD, presenting exquisite sculptures of female "
                    "deities and serene spiritual iconography. Following this, enjoy some light boutique shopping for authentic regional handicrafts. Your "
                    "memorable TRAGUIN Ajanta Ellora experience draws to a close as your private chauffeur drops you off at the airport or railway station "
                    "for your homeward journey, carrying exceptional stories and unforgettable memories."
                ),
                [
                    "Sightseeing Included: Aurangabad Caves, Local Artisan Markets",
                    "Optional Activities: Farewell lunch at an elite city garden restaurant",
                    "Evening Experience: Drop-off assistance directly at the departure terminal",
                    "Overnight Stay: Departure / End of Services",
                    "Meals Included: Rich Buffet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Welcomhotel by ITC Hotels, Rama International",
                "Chhatrapati Sambhajinagar / Aurangabad",
                "03 Nights",
                "Deluxe",
                "Executive Room",
                "MAPAI (Breakfast & Dinner)",
                4,
                1,
            ),
            _hotel(
                "Ambassador Ajanta Hotel",
                "Chhatrapati Sambhajinagar / Aurangabad",
                "03 Nights",
                "Premium",
                "Club Room / Executive Suite",
                "MAPAI (Breakfast & Dinner)",
                4,
                2,
            ),
            _hotel(
                "Vivanta Aurangabad - Taj Hotels",
                "Chhatrapati Sambhajinagar / Aurangabad",
                "03 Nights",
                "Luxury",
                "Superior Room / Deluxe Garden View Wing",
                "MAPAI (Breakfast & Dinner)",
                5,
                3,
            ),
            _hotel(
                "Vivanta Aurangabad - Taj Hotels",
                "Chhatrapati Sambhajinagar / Aurangabad",
                "03 Nights",
                "Ultra Luxury",
                "Luxury Executive Heritage Suite with Private Butler Concierge",
                "MAPAI (Breakfast & Dinner)",
                5,
                4,
                description="Ultra-luxury heritage suite with private butler concierge.",
            ),
        ],
        inclusions=[
            _inc_included("Elite Stays: 3 Nights in handpicked premium hotels or luxury heritage resorts as selected.", 1),
            _inc_included("Gourmet Food: Lavish breakfast spreads and multi-course dinners featuring local and global cuisines.", 2),
            _inc_included(
                "Premium Vehicles: Private air-conditioned luxury SUV available for all transfers, excursions, and intercity sightseeing.",
                3,
            ),
            _inc_included(
                "TRAGUIN Welcome Touch: Personalized traditional garland welcome, refreshing cold towels, and premium amenities on arrival.",
                4,
            ),
            _inc_included("Expert Storytelling: Private certified archeological guides for comprehensive tours of Ajanta and Ellora Caves.", 5),
            _inc_included("VIP Convenience: Pre-booked VIP entry tickets for all major monuments, bypassing long tourist lines.", 6),
            _inc_included(
                "Complete Coverage: Fuel charges, driver allowances, state permits, toll taxes, and parking fees are completely included.",
                7,
            ),
            _inc_included("TRAGUIN Support: 24/7 dedicated elite concierge assistance during the entire vacation.", 8),
            _inc_excluded("Domestic or international flights, train ticketing expenses, or terminal surcharges.", 9),
            _inc_excluded("Personal expenses such as laundry services, phone bills, premium mini-bar items, and room service.", 10),
            _inc_excluded("Camera, video, or commercial shooting licensing charges at any tourist places.", 11),
            _inc_excluded("Any mid-day meals, lunches, snacks, or alcoholic beverages not specified in the plan.", 12),
            _inc_excluded("Mandatory high-season holiday surcharges during major festivals or New Year weeks.", 13),
            _inc_excluded("Personal travel insurance and medical emergency provisions.", 14),
        ],
    )
    return package, itinerary


def build_mh_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "MH-004"
    tour_code = "TRAGUIN-KONKAN-004"
    title = "Premium Konkan Coast Tour Package"
    duration = "05 Nights / 06 Days"
    slug = "mh-004-premium-konkan-coast-tour-package"
    itin_slug = "mh-004-premium-konkan-coast-tour-package-itinerary"
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
            _ph("State / Country: Maharashtra, India | Category: Premium Family Vacation", 2),
            _ph("Destinations: Ratnagiri • Ganpatipule • Malvan • Tarkarli", 3),
            _ph("Ideal for: Families, Coastal Explorers, Luxury Seekers", 4),
            _ph("Best season: October to May (Best Time to Visit Konkan Coast)", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Luxury Coastal Family Tour (FIT)", 7),
            _ph("Vehicle: Private Luxury SUV (Innova Crysta) with Professional Captain", 8),
            _ph("Meal Plan: Gourmet Breakfast & Signature Coastal Dinners (MAPAI)", 9),
            _ph("Route Map: Ratnagiri (1N) ➔ Ganpatipule (1N) ➔ Tarkarli / Malvan (3N)", 10),
            _ph(
                "TRAGUIN Signature Experience: Private sunset dolphin cruise on the backwaters with customized refreshments on-board",
                11,
            ),
            _ph(
                "Shopping: Organic cashew nuts, Amba Poli, Kokum sherbet concentrate, and Malvani masala from Malvan Bazaar",
                12,
            ),
            _ph(
                "Important: Scuba diving weather-dependent; book 60 days ahead for ultra-luxury beachfront villas; check-in 14:00, check-out 11:00",
                13,
            ),
        ],
        moods=["Family", "Luxury", "Beach"],
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
        tagline="The Ultimate Coastal Maharashtra Luxury Family Tour • 5 Nights / 6 Days",
        overview=(
            "Welcome to an unforgettable luxury coastal escape exclusively masterminded by TRAGUIN. This premium Konkan Coast tour package invites your family to discover the pristine, sun-kissed, and culturally rich maritime heritage of Maharashtra. Traversing from the historic fortress horizons of Ratnagiri and the sacred beachfronts of Ganpatipule to the emerald-hued waters and white sands of Malvan and Tarkarli, this holiday brings together breathtaking landscapes, exquisite luxury stays, and exclusive experiences. Unwind with private oceanfront villas, curated heritage trails, and exhilarating marine safaris custom-tailored for your absolute peace of mind.\n\n"
            "Your highly-coveted TRAGUIN Konkan Coast package begins with a luxury overland transition into Maharashtra's most majestic maritime landscapes. Travel past scenic coastal cliffs, traditional Alphonso mango orchards, and iconic historic bastions inside a premium private SUV. Designed exclusively as an elite, family-focused FIT program, this luxury Konkan Coast holiday offers handpicked beach resorts, seamless daily pacing, an indulgent local coastal meal plan featuring fresh premium delicacies, and immersive private guidance across some of the most sought-after hidden paradises in India.\n\n"
            "Why Visit the Konkan Coast? Widely regarded as one of India's most breathtaking secret coastlines, the Konkan Coast offers a pristine sanctuary completely away from overcrowded tourist tracks. It stands out as the ultimate choice for a luxury Konkan Coast holiday, blending dramatic geographical escarpments, warm local hospitality, historic sea forts, and unblemished, soft white sands.\n\n"
            "Famous Attractions & Most Searched Experiences: This itinerary brings you face-to-face with the top tourist places in the Konkan Coast, featuring the magnificent seaside Swayambhu Ganpati Temple, the massive seafaring Sindhudurg Fort, and the calm waters of the Karli backwaters. This targeted TRAGUIN Konkan Coast experience ensures your family participates in popular Instagram locations like the panoramic Arey Warey Twin Beaches and the historic sands of Tarkarli Beach with exclusive, stress-free private logistics."
        ),
        seo_title="MH-004 | Premium Konkan Coast Tour Package | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days Konkan Coast tour (MH-004 / TRAGUIN-KONKAN-004): "
            "Ratnagiri, Ganpatipule, Sindhudurg Fort, Tarkarli, Karli backwaters, scuba diving, and 4-tier handpicked coastal accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Ratnadurg Fort, Thiba Palace & Mandvi Black Sand Beach", 1),
            _ih("Arey Warey Twin Beaches, Ganpatipule Temple & Prachin Konkan", 2),
            _ih("Sindhudurg Sea Fort, Rock Garden Malvan & Tarkarli Shoreline", 3),
            _ih("Karli Backwaters, Devbagh Sangam & Tsunami Island", 4),
            _ih("TRAGUIN Signature Experience: Private sunset dolphin cruise on the backwaters with customized refreshments", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Ratnagiri | Gateway to Heritage, History & Mango Orchards",
                (
                    "Your premium Konkan Coast sightseeing trip begins as your family arrives at Ratnagiri, where a premier, uniformed TRAGUIN chauffeur "
                    "welcomes you with customized amenities. Board your private luxury SUV and transfer smoothly to your premium resort on the cliffside. "
                    "In the afternoon, explore the magnificent Ratnadurg Fort, a majestic sea-girt fortress offering panoramic views over the Arabian Sea. Next, "
                    "visit the historical Thiba Palace, the elegant exile home of the last King of Burma, surrounded by beautifully manicured grounds. Wrap up "
                    "your day at Mandvi Black Sand Beach to witness an evocative sunset, capturing spectacular family photographs alongside the iconic gateway jetty."
                ),
                [
                    "Sightseeing Included: Ratnadurg Fort, Thiba Palace, Mandvi Beach",
                    "Optional Activities: Specialized Alphonso Mango estate walk (seasonal)",
                    "Evening Experience: Private candlelit terrace dinner facing the ocean waves",
                    "Overnight Stay: Ratnagiri Premium Luxury Cliff Resort",
                    "Meals Included: Gourmet Dinner",
                ],
            ),
            _day(
                2,
                "Ratnagiri to Ganpatipule | Scenic Coastal Drives & Sacred White Sands",
                (
                    "Savor a lavish multi-cuisine breakfast before embarking on one of the most beautiful coastal drives in India—the legendary Arey Warey Road. "
                    "This scenic route curves along dramatic sea-cliffs and turquoise bays, perfect for photography spots. Upon arriving at the tranquil beach "
                    "town of Ganpatipule, check into your ultra-luxury beachfront villa. In the afternoon, enjoy a private VIP guided visit to the 400-year-old "
                    "Swayambhu Ganpati Temple, located right on the sandy shore. Spend your late afternoon walking together across the pristine, uncrowded sands "
                    "of Ganpatipule Beach as the tide recedes under a golden sky."
                ),
                [
                    "Sightseeing Included: Arey Warey Twin Beaches, Ganpatipule Temple, Prachin Konkan",
                    "Optional Activities: Open-air museum cultural tour at Prachin Konkan",
                    "Evening Experience: Spiritual seaside Aarti experience followed by a beach walk",
                    "Overnight Stay: Ganpatipule Ultra-Luxury Beachfront Resort",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                3,
                "Ganpatipule to Tarkarli | Journey into Pristine Malvan Waters",
                (
                    "Enjoy an early morning breakfast by the beach before checking out. Your private vehicle will sweep your family southward down the stunning "
                    "Konkan Coast toward Malvan and Tarkarli. This gorgeous route crosses over estuaries, tranquil backwaters, and lush coconut plantations. Arrive "
                    "in Tarkarli in the afternoon and check into your exclusive beachfront eco-cottage, where the white sands are just steps from your private "
                    "sundeck. Spend your evening completely at ease, listening to the soothing waves and enjoying the absolute peace of this handpicked sanctuary."
                ),
                [
                    "Sightseeing Included: Malvan Coastal Route, Tarkarli Beachfront Exploration",
                    "Optional Activities: Traditional Konkani culinary masterclass at the resort",
                    "Evening Experience: Private bonfire night on the beach with local seafood specialties",
                    "Overnight Stay: Tarkarli Luxury Beachfront Eco-Resort",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                4,
                "Malvan Marine Safari | The Legendary Sindhudurg Fort & Coral Waters",
                (
                    "Today highlights the ultimate Premium Konkan Coast Experience. After a hearty breakfast, head to the historical Malvan jetty. Board a private "
                    "speed boat to explore the grand Sindhudurg Fort, built right in the sea by Chhatrapati Shivaji Maharaj in the 17th century. Walk past its "
                    "massive, enduring rock walls with your private historian guide. In the afternoon, head to the calm, crystal-clear marine zones near the fort "
                    "walls for a curated scuba diving and snorkeling experience. Accompanied by certified professional instructors, your family can discover vibrant "
                    "coral reefs and colorful marine life, creating unforgettable memories together."
                ),
                [
                    "Sightseeing Included: Sindhudurg Sea Fort, Rock Garden Malvan, Tarkarli Shoreline",
                    "Optional Activities: Private Scuba Diving, Snorkeling & Jet-ski safaris",
                    "Evening Experience: Stroll through Malvan Marine Rock Garden for sunset views",
                    "Overnight Stay: Tarkarli Luxury Beachfront Eco-Resort",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                5,
                "Karli Backwaters Cruise | Devbagh Beach & Extravagant Dolphin Spotting",
                (
                    "Awaken early for a truly magical morning. Board a private luxury houseboat at the Karli River estuary for a peaceful cruise through the tranquil "
                    "backwaters where the river meets the sea. Watch for playful wild dolphins leaping near Devbagh Sangam point. Step ashore onto the thin, secluded "
                    "sands of Tsunami Island to enjoy premium water sports or a relaxing mud-walk. Spend your afternoon at leisure, relaxing under the palm trees or "
                    "enjoying a refreshing dip in the warm ocean waters."
                ),
                [
                    "Sightseeing Included: Karli Backwaters, Devbagh Sangam, Tsunami Island",
                    "Optional Activities: Parasailing, Banana-boat rides, Speedboat cruising",
                    "Evening Experience: Signature multi-course farewell dinner hosted by the resort",
                    "Overnight Stay: Tarkarli Luxury Beachfront Eco-Resort",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                6,
                "Tarkarli to Departure | Carrying Home a Lifetime of Sun-Kissed Memories",
                (
                    "Wake up to the gentle murmur of the Arabian Sea one last time. Savor a final breakfast on your private veranda and take a quiet morning stroll "
                    "across the white sands. At check-out time, your professional chauffeur will assist with luggage and drive you smoothly toward Kudal / Ratnagiri "
                    "railway station, or directly back to Goa / Mumbai airport. Your premium holiday seamlessly concludes here, leaving you with beautiful, sun-kissed "
                    "family memories from your exclusive TRAGUIN Maharashtra Package."
                ),
                [
                    "Sightseeing Included: Scenic return drive through the Western Ghats foothills",
                    "Optional Activities: Shopping stop at a government-approved organic cashew outlet",
                    "Evening Experience: Warm assistance at the departure terminal gates",
                    "Overnight Stay: Departure / End of Services",
                    "Meals Included: Rich Buffet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Kohinoor Samudra Beach Resort / MTDC | Blue Water Resort Tarkarli / Golven Resort",
                "Ratnagiri & Ganpatipule (2N) / Malvan & Tarkarli (3N)",
                "05 Nights",
                "Deluxe",
                "Executive Sea View Room (CP) / Beachfront Eco Cottage (MAP)",
                "CP Ratnagiri-Ganpatipule & MAP Tarkarli",
                4,
                1,
            ),
            _hotel(
                "The Fern Courtyard Resort Ganpatipule | Tarkarli Niwas Nyahari / United 21 Beach Resort",
                "Ratnagiri & Ganpatipule (2N) / Malvan & Tarkarli (3N)",
                "05 Nights",
                "Premium",
                "Winter Green Valley View Room (CP) / Premium Ocean View Cabin (MAP)",
                "CP Ratnagiri-Ganpatipule & MAP Tarkarli",
                4,
                2,
            ),
            _hotel(
                "Blue Ocean Resort & Spa by Coastal Riva | Nivati Rock Resort / Devbagh Beach Stay",
                "Ratnagiri & Ganpatipule (2N) / Malvan & Tarkarli (3N)",
                "05 Nights",
                "Luxury",
                "Luxury Executive Beachfront Villa (CP) / Premium Sea-Facing Chalet (MAP)",
                "CP Ratnagiri-Ganpatipule & MAP Tarkarli",
                5,
                3,
            ),
            _hotel(
                "Blue Ocean Resort - Private Pool Villa Wing | Coco Shambhala Sindhudurg",
                "Ratnagiri & Ganpatipule (2N) / Malvan & Tarkarli (3N)",
                "05 Nights",
                "Ultra Luxury",
                "Royal Ocean-Front Pool Villa with Butler (CP) / Exclusive Bespoke Luxury Tree-Top Pavilion (MAP)",
                "CP Ratnagiri-Ganpatipule & MAP Tarkarli",
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included(
                "Elite Accommodation: 05 Nights stay in handpicked, premier luxury coastal resorts and oceanfront properties.",
                1,
            ),
            _inc_included("Bespoke Meal Plan: Daily lavish breakfast spreads and specialized multi-course traditional coastal dinners.", 2),
            _inc_included(
                "Luxury Transportation: All transfers, long-distance touring, and city sightseeing via an exclusive private premium SUV.",
                3,
            ),
            _inc_included(
                "TRAGUIN Signature Welcoming: Welcome drinks, cold towels, and a premium seasonal Konkan fruit hamper upon arrival.",
                4,
            ),
            _inc_included("Private Backwater Cruise: Exclusive private boat cruise along the Karli River backwaters for dolphin spotting.", 5),
            _inc_included(
                "VIP Guided Excursions: Pre-booked entry tickets and private professional guides for Sindhudurg Sea Fort and Thiba Palace.",
                6,
            ),
            _inc_included(
                "Full Professional Coverage: All toll fees, border taxes, driver allowances, fuel charges, and state permits are completely covered.",
                7,
            ),
            _inc_included("TRAGUIN Support: Continuous 24/7 real-time remote concierge support from senior travel specialists.", 8),
            _inc_excluded("Domestic or International airfares, flight bookings, or main interstate train ticket expenses.", 9),
            _inc_excluded(
                "Personal incidental expenses such as laundry services, mini-bar consumption, telephone calls, and room service.",
                10,
            ),
            _inc_excluded(
                "Any specialized adventure water sports (scuba diving, parasailing, jet-skiing) unless added as an optional extra.",
                11,
            ),
            _inc_excluded("Any meals, lunches, or beverage selections not specifically detailed in the official itinerary.", 12),
            _inc_excluded("Mandatory peak festive season surcharges (applicable during Diwali, Christmas, and New Year weeks).", 13),
            _inc_excluded("Travel insurance coverage and medical expenses of any nature.", 14),
        ],
    )
    return package, itinerary


def build_mh_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "MH-005"
    tour_code = "TRAGUIN-MAHA-HON-005"
    title = "Premium Mahabaleshwar Honeymoon Package"
    duration = "04 Nights / 05 Days"
    slug = "mh-005-premium-mahabaleshwar-honeymoon-package"
    itin_slug = "mh-005-premium-mahabaleshwar-honeymoon-package-itinerary"
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
            _ph("State / Country: Maharashtra, India | Category: Luxury Honeymoon Package", 2),
            _ph("Destinations: Mahabaleshwar • Panchgani • Pratapgad", 3),
            _ph("Ideal for: Honeymooners, Couples, Romance Seekers", 4),
            _ph("Best season: October to March (Plus Lush romantic Monsoons)", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Luxury Honeymoon Tour (FIT)", 7),
            _ph("Vehicle: Private Chauffeur Sedan / Premium SUV (Crysta)", 8),
            _ph("Meal Plan: Breakfast & Special Romantic Dinners (MAPAI)", 9),
            _ph("Route Map: Pune/Mumbai ➔ Panchgani ➔ Mahabaleshwar (4N) ➔ Departure", 10),
            _ph(
                "TRAGUIN Honeymoon Special Amenities: Complimentary floral bed decor, chocolate cake, and farm-fresh strawberries",
                11,
            ),
            _ph(
                "Shopping: Kolhapuri leather footwear, organic honey, berry syrups at Mapro Garden; artisanal leather at Town Market",
                12,
            ),
            _ph(
                "Important: Monsoon fog may reduce viewpoint visibility; book 45 days ahead in peak autumn/winter; check-in 14:00, check-out 11:00",
                13,
            ),
        ],
        moods=["Honeymoon", "Romance", "Luxury"],
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
        tagline="An Ultimate Romantic Escapade Amidst Cloud-Kissed Valleys • 4 Nights / 5 Days",
        overview=(
            "Welcome to an unforgettable journey into romance, beautifully tailored by TRAGUIN. This exclusive Mahabaleshwar Honeymoon Package sweeps you away into the emerald heart of the Sahyadri Hills. Known for its mesmerizing breathtaking landscapes, mist-shrouded viewpoints, and sweet berry plantations, a Luxury Mahabaleshwar Holiday offers newlywed couples a perfect sanctuary of privacy and rejuvenation. Melding private premium transfers, highly romantic candle-lit dining, immersive natural trails, and handpicked hotels, we invite you to design memories that will look beautiful forever.\n\n"
            "Your romantic journey on this Best Mahabaleshwar Tour Package begins with a private premium pickup from Pune or Mumbai, sweeping upwards into the majestic evergreen ranges. Experience the finest elements of a Premium Mahabaleshwar Experience meticulously designed for modern couples. From private strawberry farm pickings to intimate sunset boat rides on Venna Lake and historic fort walks, every element of this itinerary reflects premium attention. Escape the frantic city rush and let your love blossom against the spectacular scenic beauty of cloud-filled valleys and waterfalls.\n\n"
            "Why Choose a Mahabaleshwar Honeymoon? Crowned as the ultimate honeymoon capital of Western India, Mahabaleshwar seamlessly balances old-world colonial romance with dramatic natural topography. For couples seeking a premium mountain getaway, it provides cooler alpine breezes, beautiful rolling valleys, and iconic attractions that naturally inspire bonding and closeness.\n\n"
            "Top Tourist Places & Instagram Locations: Capture striking romantic memories at the dramatic Arthur's Seat (known as the Queen of Points), the majestic Elphinstone Point, the serene Venna Lake, Mapro Garden, and the spectacular, breeze-swept Table Land in Panchgani. This customized TRAGUIN Mahabaleshwar Packages setup ensures you explore these highly sought-after destinations during perfect daylight intervals with zero crowded rushing, prioritizing couple intimacy."
        ),
        seo_title="MH-005 | Premium Mahabaleshwar Honeymoon Package | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Mahabaleshwar honeymoon package (MH-005 / TRAGUIN-MAHA-HON-005): "
            "Panchgani Table Land, Arthur's Seat, Venna Lake, Pratapgad Fort, strawberry farms, and 4-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Table Land, Sydney Point & Parsi Point Panchgani", 1),
            _ih("Old Mahabaleshwar Temple, Arthur's Seat, Eco Point & Venna Lake", 2),
            _ih("Pratapgad Fort, Afzal Khan Tomb & Private Strawberry Farms", 3),
            _ih("Bombay Point, Lodwick Point & Elephant's Head Rock", 4),
            _ih("TRAGUIN Signature Experience: Private early morning strawberry picking trail with local farm owners", 5),
        ],
        days=[
            _day(
                1,
                "Arrival & Transit via Panchgani | Gateway to Alpine Serenity",
                (
                    "Your specialized Mahabaleshwar Family Tour & Honeymoon vehicle will receive you warmly at Pune Airport or Mumbai Airport. Enjoy a "
                    "wonderfully scenic route winding uphill through rolling green ranges. Stop along the way at the picturesque town of Panchgani to walk "
                    "hand-in-hand over Table Land, the second longest volcanic plateau in Asia, offering panoramic mountain views. Enjoy local fresh strawberry "
                    "creams together before reaching your ultra-luxury resort in Mahabaleshwar. Receive a custom TRAGUIN welcome mocktail, check into your "
                    "master honeymoon suite, and relax in absolute comfort."
                ),
                [
                    "Sightseeing Included: Table Land, Sydney Point, Parsi Point Panchgani",
                    "Optional Activities: Couple Tandem Paragliding at Panchgani hills",
                    "Evening Experience: Intimate welcome drink by the resort infinity pool",
                    "Overnight Stay: Mahabaleshwar Luxury Honeymoon Resort",
                    "Meals Included: Romantic Welcome Dinner",
                ],
            ),
            _day(
                2,
                "Mahabaleshwar Sightseeing | Iconic Viewpoints & Floating Romance",
                (
                    "Wake up to a golden morning mist rising over the valley. After a premium breakfast, begin your targeted Mahabaleshwar Sightseeing "
                    "exploration. Visit the timeless Mahabaleshwar Temple to experience the cultural history of the Krishna River source. Then, head to the "
                    "dramatic heights of Arthur's Seat, where lightweight objects float due to unique air currents. In the late afternoon, your driver will usher "
                    "you to the iconic Venna Lake. Step into a privately decorated rowboat under a quiet canopy, watching the sun dip cleanly into the shimmering "
                    "waters while creating unforgettable memories together."
                ),
                [
                    "Sightseeing Included: Old Mahabaleshwar Temple, Arthur's Seat, Eco Point, Venna Lake",
                    "Optional Activities: Horse-riding along the lakeside paths",
                    "Evening Experience: Private lakeside walk followed by local sweet treats",
                    "Overnight Stay: Mahabaleshwar Luxury Honeymoon Resort",
                    "Meals Included: Breakfast & Speciality Dinner",
                ],
            ),
            _day(
                3,
                "Heritage Exploration at Pratapgad Fort | Love in a Historic Fortress",
                (
                    "Indulge in a rich breakfast before venturing onto a scenic forest drive to the legendary Pratapgad Fort, a majestic historical citadel "
                    "positioned high among mountain ridges. Walk with your private historical guide down ancient stone corridors, learning tales of bravery while "
                    "taking spectacular photographs against deep-cut green drop-offs. In the afternoon, return to town and stop at a handpicked organic strawberry "
                    "plantation. Hand-pick sweet premium berries right off the vine together—an immersive experience curated specifically by TRAGUIN experts to "
                    "capture pure joy."
                ),
                [
                    "Sightseeing Included: Pratapgad Fort, Afzal Khan Tomb, Private Strawberry Farms",
                    "Optional Activities: Trekking up the watchtowers for sweeping horizon views",
                    "Evening Experience: Honeymoon Special Candle-light dinner with complimentary cake",
                    "Overnight Stay: Mahabaleshwar Luxury Honeymoon Resort",
                    "Meals Included: Breakfast & Candle-Light Dinner",
                ],
            ),
            _day(
                4,
                "Leisure, Deep Rejuvenation & Spectacular Sunsets",
                (
                    "Dedicate this day to ultimate relaxation and deep individual connection. Sleep in and relish breakfast served directly to your room balcony. "
                    "In the afternoon, partake in an exclusive premium couple's spa ritual at your resort to completely de-stress. Around 4 PM, travel down shaded "
                    "woodland paths toward Bombay Point (Sunset Point). This spot is globally loved for its wide panoramic vistas of the valley glowing gold. Sit "
                    "quietly on manicured lawns, toast to your beautiful life ahead, and enjoy the magical, scenic beauty of the Sahyadris."
                ),
                [
                    "Sightseeing Included: Bombay Point, Lodwick Point, Elephant's Head Rock",
                    "Optional Activities: Premium Ayurvedic Wellness Spa Therapy for Couples",
                    "Evening Experience: Live music lounge visit or starlit poolside cocktail hour",
                    "Overnight Stay: Mahabaleshwar Luxury Honeymoon Resort",
                    "Meals Included: Breakfast & Chef's Special Fare",
                ],
            ),
            _day(
                5,
                "Bidding Farewell | Taking Back Endless Romantic Memories",
                (
                    "Savor your final morning breakfast in this high-altitude haven. Take a slow stroll through the resort's beautifully manicured gardens for a "
                    "few final souvenir photographs. Complete your seamless check-out, and join your private chauffeur for the smooth descent back down towards Pune "
                    "or Mumbai. Stop briefly at the famous Mapro Gardens to buy fresh syrups, chocolates, and unique souvenirs for family back home. Your unmatched "
                    "TRAGUIN Mahabaleshwar Package finishes as you arrive at the airport or train terminal, completely rejuvenated and deeply in love."
                ),
                [
                    "Sightseeing Included: Mapro Garden Retail Outlet, Return Hill Drive",
                    "Optional Activities: Buying artisanal leather footwear at the local town market",
                    "Evening Experience: Drop-off assistance at your homeward terminal",
                    "Overnight Stay: Departure / End of Luxury Services",
                    "Meals Included: Rich Buffet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Brightland Resort & Spa / Evershine Resort",
                "Mahabaleshwar",
                "04 Nights",
                "Deluxe",
                "Premium Valley View Room",
                "Breakfast & Dinner (MAP)",
                4,
                1,
                description="Deluxe tier with welcome drink included.",
            ),
            _hotel(
                "Le Méridien Mahabaleshwar Resort & Spa",
                "Mahabaleshwar",
                "04 Nights",
                "Premium",
                "Classic Forest King Room",
                "Breakfast & Dinner (MAP)",
                5,
                2,
                description="Premium tier with 15% spa discount voucher.",
            ),
            _hotel(
                "Courtyard by Marriott Mahabaleshwar / Ramsukh Resorts",
                "Mahabaleshwar",
                "04 Nights",
                "Luxury",
                "Premium Valley View Deck Room",
                "Breakfast & Special Dinner (MAP)",
                5,
                3,
                description="Luxury tier with private farm access.",
            ),
            _hotel(
                "Le Méridien Luxury Valley View Suite / Ramsukh Private Pool Villa",
                "Mahabaleshwar",
                "04 Nights",
                "Ultra Luxury",
                "Exclusive Couple Suite with Plunge Pool",
                "Gourmet MAPAI Plan",
                5,
                4,
                description="Ultra-luxury with private butler, floral bed decor and cake.",
            ),
        ],
        inclusions=[
            _inc_included(
                "Elite Accommodation: 04 Nights luxury stay in handpicked premium properties with great mountain views.",
                1,
            ),
            _inc_included("Bespoke Meal Plan: Daily elaborate breakfasts and custom multi-course dinners.", 2),
            _inc_included(
                "Luxury Transportation: All long-distance touring, hill climbing, and private airport transits via a premium vehicle.",
                3,
            ),
            _inc_included(
                "TRAGUIN Honeymoon Welcoming: Complimentary floral bed arrangement, rich chocolate cake, and farm-fresh strawberries.",
                4,
            ),
            _inc_included("Private Boating Experience: Exclusive couple's rowboat hire on the serene Venna Lake.", 5),
            _inc_included("VIP Access & Entry: Pre-booked entry tickets and private local guides for Pratapgad Fort.", 6),
            _inc_included(
                "Full Professional Coverage: All toll fees, mountain parking passes, driver allowances, and fuel charges are fully paid.",
                7,
            ),
            _inc_included("TRAGUIN Support: Continuous 24/7 dedicated remote concierge support from elite luxury travel planners.", 8),
            _inc_excluded("Domestic or International flight fares, train tickets, or major transit terminal expenses.", 9),
            _inc_excluded(
                "Personal incidental expenses such as laundry, mini-bar usage, phone calls, and optional room service meals.",
                10,
            ),
            _inc_excluded("Any outdoor paragliding, heavy camera/drone licenses, or optional adventure sports fees.", 11),
            _inc_excluded("Any lunch meals, roadside snacks, or alcoholic beverage packages not specifically outlined above.", 12),
            _inc_excluded(
                "Mandatory peak holiday surcharges (applicable during long weekends, Diwali, Christmas, and New Year blocks).",
                13,
            ),
            _inc_excluded("Travel insurance coverage and medical expenses of any nature.", 14),
        ],
    )
    return package, itinerary


MAHARASHTRA_MH_001_005_BUILDERS = [
    build_mh_001,
    build_mh_002,
    build_mh_003,
    build_mh_004,
    build_mh_005,
]
