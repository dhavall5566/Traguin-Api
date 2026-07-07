"""Builder functions for BR-001 through BR-009 Bihar domestic packages."""

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

BIHAR_SLUG = "bihar"


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


def build_br_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "BR-001"
    tour_code = "TRG-BIH-001"
    title = (
        "TRAGUIN Premium Bihar Tour Package — Bodhgaya Darshan • "
        "Path to Enlightenment & Divine Heritage: Patna • Nalanda • Rajgir • Bodhgaya"
    )
    duration = "03 Nights / 04 Days"
    slug = "br-001-bodhgaya-darshan-patna-nalanda-rajgir-bodhgaya"
    itin_slug = "br-001-bodhgaya-darshan-patna-nalanda-rajgir-bodhgaya-itinerary"
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
            _ph("State / Country: Bihar / India | Category: Pilgrimage / Spiritual Luxury", 2),
            _ph("Destinations: Patna • Nalanda • Rajgir • Bodhgaya", 3),
            _ph("Ideal for: Families, Spiritual Seekers & History Connoisseurs", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Luxury Customized)", 6),
            _ph("Vehicle / Meals: Luxury AC Innova Crysta / MAPAI (Breakfast & Dinner)", 7),
            _ph(
                "Route Plan: Patna Arrival ➔ Rajgir (1N) ➔ Nalanda & Bodhgaya (2N) ➔ Patna Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private scholar-guided tour through the Nalanda Ruins "
                "to unravel hidden historical secrets.",
                9,
            ),
            _ph(
                "Curated by TRAGUIN Experts: Handpicked routing and premium hotels that emphasize "
                "extreme safety, calmness, and absolute privacy.",
                10,
            ),
            _ph(
                "Exclusive Recommendations: Access to quiet, hidden spots around Bodhgaya perfect for "
                "undistracted meditation.",
                11,
            ),
            _ph(
                "Shopping & Local Experiences: Authentic Madhubani paintings, stone carvings, tussar silk; "
                "Tilkut, Litti Chokha, international cuisines near monasteries.",
                12,
            ),
            _ph(
                "Important Notes: Conservative clothing inside temples; light woolens Nov–Feb; "
                "advance booking 45 days ahead during peak meditation season.",
                13,
            ),
        ],
        moods=["Pilgrimage", "Spiritual", "Family", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Luxury Customized)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Bodhgaya Darshan • Patna • Nalanda • Rajgir • Bodhgaya • 03 Nights / 04 Days",
        overview=(
            "Welcome to a soul-stirring spiritual odyssey meticulously crafted by TRAGUIN. Embark on the "
            "definitive Bihar Pilgrimage experience, specifically designed to introduce your family to the "
            "timeless tranquility where Prince Siddhartha achieved ultimate enlightenment.\n\n"
            "TOUR OVERVIEW\n"
            "This custom-tailored luxury holiday package provides an elite balance between sacred traditional "
            "pilgrimage routes and contemporary high-end luxury. Travelling in a dedicated private luxury "
            "transport sedan with a professional chauffeur-driven assistant, your family will enjoy absolute "
            "comfort and privacy across the ancient landscapes of Bihar. With a carefully curated meal plan "
            "featuring lavish breakfasts and specialized dinners, this route represents the definitive premium "
            "Bihar experience. Every step of your journey includes the signature touch of TRAGUIN curated "
            "experiences, ensuring VIP darshan access, expert historical narrative insights, and around-the-clock "
            "bespoke support.\n\n"
            "WHY CHOOSE THE BEST BIHAR TOUR PACKAGE?\n"
            "When planning a Luxury Bihar Holiday, discerning travellers seek more than just standard "
            "sightseeing; they seek a transformative connection to heritage and spiritual peace. Bihar features "
            "some of the most iconic attractions in the world of spiritual tourism. From the internationally "
            "acclaimed Mahabodhi Temple in Bodhgaya—a top tourist place in Bihar and a UNESCO World Heritage "
            "Site—to the majestic ruins of the world's oldest university in Nalanda, this region holds "
            "spectacular historical depth. For families and spiritual seekers, the land reveals highly popular "
            "Instagram locations like the architecturally marveling Vishwa Shanti Stupa in Rajgir and the serene "
            "glass bridge paths. Whether you are looking to purchase authentic Madhubani paintings while "
            "shopping, indulge in traditional local food like Litti Chokha, or experience profound meditation "
            "under the sacred Bodhi Tree, our TRAGUIN Bihar Packages guarantee premium comfort, handpicked "
            "luxury stays, and curated exclusive experiences during the best time to visit Bihar."
        ),
        seo_title="BR-001 | Bodhgaya Darshan Patna Nalanda Rajgir | TRAGUIN",
        seo_description=(
            "Premium 03 Nights / 04 Days Bihar pilgrimage (BR-001 / TRG-BIH-001): Rajgir, Nalanda, "
            "Mahabodhi Temple, Vishwa Shanti Stupa, and 4-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Patna arrival and scenic drive to Rajgir with hot springs on Day 01", 1),
            _ih("Rajgir ropeway, Vishwa Shanti Stupa, Nalanda ruins en route to Bodhgaya on Day 02", 2),
            _ih("Mahabodhi Temple, Bodhi Tree, Great Buddha Statue, monasteries on Day 03", 3),
            _ih("Bodhgaya to Patna departure with handicraft stops on Day 04", 4),
        ],
        days=[
            _day(
                1,
                "ARRIVAL IN PATNA TO RAJGIR | WELCOME TO PALIPUTRA – JOURNEY TO THE IMPERIAL VALLEY",
                (
                    "Your premium Bihar experience begins as you arrive at Patna Airport/Railway Station, "
                    "where a dedicated private luxury transport vehicle waits to escort you. Embark on a "
                    "highly scenic drive toward Rajgir, the ancient capital of the Magadha Empire. On arrival, "
                    "check into your handpicked premium luxury resort. After refreshing, experience a majestic "
                    "evening walk along the nearby hot springs, renowned for their therapeutic values."
                ),
                [
                    "Sightseeing Included: Scenic drive across Bihar plains, Rajgir hot springs, and ancient city walls.",
                    "Evening Experience: An intimate, tranquil welcome dinner at the resort curated by TRAGUIN experts.",
                    "Overnight Stay: Rajgir (Premium / Luxury Wellness Resort).",
                    "Meals Included: Welcome Drink & Luxury Dinner.",
                ],
            ),
            _day(
                2,
                "RAJGIR & NALANDA SIGHTSEEING TO BODHGAYA | ANCIENT WISDOM, ROPEWAYS & SPIRITUAL LANDSCAPES",
                (
                    "Awake to a peaceful mountain sunrise. Ride the scenic aerial ropeway to the peak of "
                    "Ratnagiri Hill to witness the magnificent Vishwa Shanti Stupa, a breathtaking landscape of "
                    "peace. Next, visit Griddhakuta (Vulture's Peak) where Lord Buddha preached. In the afternoon, "
                    "drive to Nalanda to explore the spectacular archaeological ruins of the ancient Nalanda "
                    "University. Walk through the museum before driving through iconic attractions toward the holy "
                    "town of Bodhgaya for your premium stay."
                ),
                [
                    "Sightseeing Included: Vishwa Shanti Stupa, Griddhakuta Hills, Nalanda University Ruins, Nalanda Archaeological Museum.",
                    "Optional Activities: A private guided meditation briefing with an ordained scholar at Rajgir.",
                    "Overnight Stay: Bodhgaya (Premium Luxury Hotel).",
                    "Meals Included: Premium Breakfast & Gourmet Dinner.",
                ],
            ),
            _day(
                3,
                "HOLY BODHGAYA DARSHAN | THE EPIDOME OF ENLIGHTENMENT – MAHABODHI DARSHAN",
                (
                    "Today is dedicated to your deeply emotional and spiritual Bodhgaya Darshan. Visit the "
                    "awe-inspiring Mahabodhi Temple, standing beneath the very Bodhi Tree where Siddhartha "
                    "Gautama attained enlightenment over 2,500 years ago. Sit in silent reflection in the manicured "
                    "meditation gardens. Later, capture beautiful photography points at the Great Buddha Statue "
                    "(80 ft), the Royal Bhutan Monastery, and the stunning Thai Monastery, each showcasing "
                    "immersive experiences of distinct Asian architecture."
                ),
                [
                    "Sightseeing Included: Mahabodhi Temple Complex, Sacred Bodhi Tree, 80-feet Great Buddha Statue, International Monasteries.",
                    "Evening Experience: VIP assisted evening butter-lamp lighting ceremony inside the sacred complex.",
                    "Overnight Stay: Bodhgaya (Premium Luxury Hotel).",
                    "Meals Included: Breakfast & Traditional Elite Dinner.",
                ],
            ),
            _day(
                4,
                "BODHGAYA TO PATNA / DEPARTURE | CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS",
                (
                    "Indulge in a final lavish breakfast at your premium hotel. Your private luxury transport will "
                    "safely drive you back along the smooth national highway to Patna. En route, enjoy short photo "
                    "stops and shopping for authentic handicrafts. Arrive at Patna Airport or Railway Station for "
                    "your onward journey, carrying home a deeply rejuvenated spirit and unforgettable memories "
                    "meticulously designed by TRAGUIN."
                ),
                [
                    "Transfers Included: Private luxury door-to-door drop-off back to Patna terminal.",
                    "Meals Included: Sumptuous Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Hotel Royal Residency / similar | The Bodhi Palace Resort / similar",
                "Rajgir (1 Night) / Bodhgaya (2 Nights)",
                "03 Nights",
                "Deluxe",
                "Deluxe Room",
                "MAPAI (Breakfast & Dinner)",
                4,
                1,
                description="OPTION 01 – DELUXE: Hotel Royal Residency / similar (Rajgir, 1 Night) | The Bodhi Palace Resort / similar (Bodhgaya, 2 Nights) | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "Indo Hokke Hotel / similar | Mantra Bodhgaya / similar",
                "Rajgir (1 Night) / Bodhgaya (2 Nights)",
                "03 Nights",
                "Premium",
                "Premium Room",
                "MAPAI (Breakfast & Dinner)",
                4,
                2,
                description="OPTION 02 – PREMIUM: Indo Hokke Hotel / similar (Rajgir, 1 Night) | Mantra Bodhgaya / similar (Bodhgaya, 2 Nights) | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "The Gargee Gautam Vihar Resort | Marasa Sarovar Premiere / Maha Bodhi Hotel",
                "Rajgir (1 Night) / Bodhgaya (2 Nights)",
                "03 Nights",
                "Luxury",
                "Luxury Room",
                "Premium Custom MAPAI",
                5,
                3,
                description="OPTION 03 – LUXURY: The Gargee Gautam Vihar Resort (Rajgir, 1 Night) | Marasa Sarovar Premiere / Maha Bodhi Hotel (Bodhgaya, 2 Nights) | Premium Custom MAPAI",
            ),
            _hotel(
                "VVIP Private Luxury Wellness Suite | The Zen Resort Bodhgaya (Luxury Villa)",
                "Rajgir (1 Night) / Bodhgaya (2 Nights)",
                "03 Nights",
                "Ultra Luxury",
                "Luxury Villa / Suite",
                "Elite Chef Curated Meals",
                5,
                4,
                description="OPTION 04 – ULTRA LUXURY: VVIP Private Luxury Wellness Suite (Rajgir, 1 Night) | The Zen Resort Bodhgaya Luxury Villa (Bodhgaya, 2 Nights) | Elite Chef Curated Meals",
            ),
        ],
        inclusions=[
            _inc_included("Premium Accommodation: Handpicked hotels as per chosen category.", 1),
            _inc_included("Luxury Transportation: Private AC Innova Crysta for all transfers & sightseeing.", 2),
            _inc_included("Curated Meal Plan: Daily luxury breakfast and gourmet dinners (MAPAI).", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated guest experience manager on call.", 4),
            _inc_included("Welcome Amenities: Customized spiritual travel kit and refreshments upon arrival.", 5),
            _inc_included("Complimentary Experience: Reserved aerial ropeway tickets for Vishwa Shanti Stupa.", 6),
            _inc_excluded("Airfare / Train tickets to and from Patna terminals.", 7),
            _inc_excluded("Monument entry tickets, camera fees, or local monastery donation offerings.", 8),
            _inc_excluded("Personal expenses such as laundry, telephone calls, and tips.", 9),
            _inc_excluded("Any optional meditation sessions or extended tours not explicitly listed.", 10),
        ],
    )
    return package, itinerary


def build_br_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "BR-002"
    tour_code = "TRG-BIH-002"
    title = (
        "TRAGUIN Premium Bihar Tour Package — Buddhist Circuit • "
        "The Path of Enlightenment & Legacy: Patna • Nalanda • Rajgir • Bodhgaya • Vaishali"
    )
    duration = "05 Nights / 06 Days"
    slug = "br-002-buddhist-circuit-patna-nalanda-rajgir-bodhgaya-vaishali"
    itin_slug = "br-002-buddhist-circuit-patna-nalanda-rajgir-bodhgaya-vaishali-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Bihar / India | Category: Pilgrimage / Spiritual Luxury", 2),
            _ph("Destinations: Patna • Nalanda • Rajgir • Bodhgaya • Vaishali", 3),
            _ph("Ideal for: Families, Spiritual Seekers, Historians & Luxury Pilgrims", 4),
            _ph("Best season: October to March (Pleasant & Spiritual Festivals)", 5),
            _ph("Starting price: On Request (Premium Customised Packages)", 6),
            _ph("Vehicle / Meals: Luxury Chauffeur-Driven SUV / MAPAI (Breakfast & Dinner)", 7),
            _ph("Route Plan: Patna (1N) ➔ Vaishali ➔ Nalanda ➔ Rajgir (1N) ➔ Bodhgaya (3N) ➔ Patna Departure", 8),
            _ph("TRAGUIN Signature Experience: Private interaction with a certified archeological researcher before touring Nalanda's ruins.", 9),
            _ph("Curated by TRAGUIN Experts: Meticulously timed transfers to guarantee arriving at the Mahabodhi Tree during peaceful chanting hours.", 10),
            _ph("Premium Handpicked Hotels: Accommodations chosen strictly based on world-class hospitality, absolute tranquility, and gourmet dining safety.", 11),
            _ph("Shopping & Local Experiences: Wooden Buddha statuettes, Madhubani paintings, Bodhi leaf bookmarks; Litti Chokha and Satvik cuisines.", 12),
            _ph("Important Notes: Modest dress at temples; footwear removed before entry; book 30–45 days ahead for winter season.", 13),
        ],
        moods=["Pilgrimage", "Spiritual", "Family", "Luxury", "History"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note="On Request (Premium Customised Packages)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Buddhist Circuit • Patna • Vaishali • Nalanda • Rajgir • Bodhgaya • 05 Nights / 06 Days",
        overview=(
            "Welcome to a transformative pilgrimage of the soul, elegantly crafted by TRAGUIN. Embark on the absolute Best Bihar Tour Package, specifically designed as a comprehensive Bihar Family Tour that retraces the sacred footsteps of Lord Buddha.\n\n"
            "TOUR OVERVIEW\n"
            "This bespoke luxury pilgrimage covers the core spiritual centers of the legendary Buddhist Circuit. Designed as an absolute premium Bihar experience, you will travel effortlessly in a private, high-end luxury vehicle under the guidance of our professional, well-versed local chauffeurs. Enjoy a meticulously planned meal itinerary featuring daily elaborate gourmet breakfasts and fine local-international dinners. Every chapter of this tour is stamped with our signature TRAGUIN curated experiences, offering hassle-free VIP temple entries, expert local historians, and elite personal assistance at every location.\n\n"
            "WHY VISIT THE BUDDHIST CIRCUIT? DISCOVER TOP TOURIST PLACES IN BIHAR\n"
            "For discerning travelers seeking a profound spiritual awakening alongside unparalleled historical context, a Luxury Bihar Holiday presents an incredible timeline of human civilization. Bihar houses some of the most globally renowned iconic attractions. From the sacred town of Bodhgaya to the grand remnants of Nalanda, travelers will encounter popular Instagram locations like the Vishwa Shanti Stupa accessible via a scenic aerial ropeway in Rajgir, the perfectly preserved Ashokan Pillar in Vaishali, and the serene meditative waters of the Niranjana River."
        ),
        seo_title="BR-002 | Buddhist Circuit Patna Vaishali Nalanda Bodhgaya | TRAGUIN",
        seo_description="Premium 05 Nights / 06 Days Buddhist Circuit (BR-002 / TRG-BIH-002): Vaishali, Nalanda, Rajgir, Bodhgaya, Dungeshwari Caves, and 4-tier hotels.",
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Patna arrival with Vaishali Ashokan Pillar excursion on Day 01", 1),
            _ih("Nalanda University ruins and drive to Rajgir on Day 02", 2),
            _ih("Rajgir ropeway, Vishwa Shanti Stupa, and transfer to Bodhgaya on Day 03", 3),
            _ih("Mahabodhi Temple, Bodhi Tree, monasteries on Day 04", 4),
            _ih("Dungeshwari Caves, Sujata Stupa, Niranjana River on Day 05", 5),
            _ih("Bodhgaya to Patna departure on Day 06", 6),
        ],
        days=[
            _day(1, "ARRIVAL IN PATNA & VAISHALI EXCURSION | LEGACIES OF ANCIENT KINGDOMS & THE SACRED PILLARS", (
                "Your premium Bihar experience commences as you land at Patna Airport, where your personal luxury transportation and dedicated representative await. Step into absolute comfort and drive directly towards the ancient city of Vaishali. Explore the historical site where Lord Buddha delivered his final sermon. Marvel at the brilliantly preserved Ashokan Pillar topped by a single lion, and view the sacred Ananda Stupa. Return to Patna by evening to unwind at your handpicked premium luxury hotel."
            ), [
                "Sightseeing Included: Ashokan Pillar at Vaishali, Ananda Stupa, Relic Stupa, Abhishek Pushkarini (Coronation Tank).",
                "Evening Experience: Exclusive welcome note presentation and multi-course traditional luxury dinner.",
                "Overnight Stay: Patna (Premium / Luxury Hotel).",
                "Meals Included: Welcome Drink & Fine-dining Dinner.",
            ]),
            _day(2, "PATNA TO RAJGIR VIA NALANDA | ECHOES OF REKNOWNED KNOWLEDGE & ROYAL REFUGE", (
                "Enjoy a lavish breakfast before driving through scenic rural vistas towards Nalanda, a UNESCO World Heritage site and a key tourist place in Bihar. Walk among the awe-inspiring archaeological ruins of the ancient 5th-century Nalanda University with a private archeology expert. Witness the vast lecture halls, ancient monasteries, and the iconic Sariputra Stupa. Afterward, drive to Rajgir—the capital of the ancient Magadha Empire—and check into your premium wellness resort."
            ), [
                "Sightseeing Included: Nalanda University Archaeological Ruins, Nalanda Archaeological Museum, Xuanzang Memorial Hall.",
                "Optional Activities: Private pottery demonstration or interactive session with a leading local historian.",
                "Overnight Stay: Rajgir (Premium / Luxury Wellness Resort).",
                "Meals Included: Premium Breakfast & Gourmet Dinner.",
            ]),
            _day(3, "RAJGIR SIGHTSEEING TO BODHGAYA | THE AERIAL STUPA & THE SOLEMN CAVES OF MEDITATION", (
                "Awake to the scenic beauty of the Rajgir hills. Embark on a thrilling aerial ropeway ride up to the Gridhakuta Hill (Vulture's Peak), where Lord Buddha delivered many of his defining discourses. Visit the pristine, snow-white Vishwa Shanti Stupa, a highly popular Instagram location. Explore the ancient Bimbisara Jail and the healing hot springs of Rajgir. In the afternoon, your luxury transport brings you to the spiritual epicenter of the world: Bodhgaya."
            ), [
                "Sightseeing Included: Vishwa Shanti Stupa (Ropeway Access), Gridhakuta Hill, Venuvan (Bamboo Grove), Bimbisara Jail.",
                "Evening Experience: A serene sunset introduction to Bodhgaya's global monasteries.",
                "Overnight Stay: Bodhgaya (Bespoke Luxury Hotel).",
                "Meals Included: Premium Breakfast & Dinner.",
            ]),
            _day(4, "THE SACRED HEART OF BODHGAYA | DAWN OF ENLIGHTENMENT UNDER THE IMMORTAL BODHI TREE", (
                "Experience a deeply moving, emotional morning as you walk into the iconic Mahabodhi Temple complex, a UNESCO World Heritage site. Stand before the magnificent golden statue of Buddha and sit in quiet meditation beneath the sacred Bodhi Tree, the exact spot of ultimate enlightenment. Immerse yourself in the serene ambiance of chanting international monks. Later, explore the Great Buddha Statue, the majestic Royal Bhutan Monastery, and the beautifully designed Thai Monastery."
            ), [
                "Sightseeing Included: Mahabodhi Temple, Sacred Bodhi Tree, Vajrasana, Muchalinda Lake, Great Buddha Statue (80ft).",
                "Evening Experience: Reserved private space for the spectacular evening oil-lamp lighting ceremony at Mahabodhi.",
                "Overnight Stay: Bodhgaya (Bespoke Luxury Hotel).",
                "Meals Included: Lavish Breakfast & Satvik-International Dinner.",
            ]),
            _day(5, "BODHGAYA – DUNGESHWARI & RIVERSIDE EXCURSION | THE CAVES OF PENANCE & THE SACRED RIVERBANKS", (
                "Following a premium breakfast, take a scenic short drive to the Dungeshwari Cave Temples (Mahakala Caves), where Prince Siddhartha practiced rigorous penance before attaining enlightenment. The rocky cliffside offers breathtaking landscapes of the plains below. Later, walk along the tranquil banks of the Niranjana River and visit the ancient Sujata Stupa, dedicated to the village maiden who offered milk-rice to the fasting Buddha, sealing a timeless lesson in balance."
            ), [
                "Sightseeing Included: Dungeshwari Caves, Sujata Garh Stupa, Niranjana River bank trails.",
                "Optional Activities: Guided mindfulness meditation class inside an exclusive monastic enclave.",
                "Overnight Stay: Bodhgaya (Bespoke Luxury Hotel).",
                "Meals Included: Premium Breakfast & Farewell Special Dinner.",
            ]),
            _day(6, "BODHGAYA TO PATNA / DEPARTURE | RETURN WITH AN ENLIGHTENED SOUL", (
                "Savor your final luxury breakfast at the resort. Your private chauffeur-driven luxury vehicle will ensure a comfortable smooth highway drive back to Patna Airport (or Gaya Airport depending on flight preferences). Your memorable journey concludes as you depart with a deeply enriched spirit and unforgettable memories meticulously designed for you by TRAGUIN."
            ), [
                "Transfers Included: Private door-to-door highway departure transfer.",
                "Meals Included: Sumptuous Buffet Breakfast.",
            ]),
        ],
        hotels=[
            _hotel("Hotel Maurya / Lemon Tree | The Gargee Gautam Vihar | Hotel Tokyo Vihar / similar", "Patna (1 Night) / Rajgir (1 Night) / Bodhgaya (3 Nights)", "05 Nights", "Deluxe", "Deluxe Room", "MAPAI (Breakfast & Dinner)", 4, 1, description="OPTION 01 – DELUXE: Hotel Maurya / Lemon Tree (Patna, 1 Night) | The Gargee Gautam Vihar (Rajgir, 1 Night) | Hotel Tokyo Vihar / similar (Bodhgaya, 3 Nights)"),
            _hotel("Gargee Grand / similar | Hotel Indo Hokke / similar | Maha Bodhi Hotel & Resort", "Patna (1 Night) / Rajgir (1 Night) / Bodhgaya (3 Nights)", "05 Nights", "Premium", "Premium Room", "MAPAI (Breakfast & Dinner)", 4, 2, description="OPTION 02 – PREMIUM: Gargee Grand / similar (Patna, 1 Night) | Hotel Indo Hokke / similar (Rajgir, 1 Night) | Maha Bodhi Hotel & Resort (Bodhgaya, 3 Nights)"),
            _hotel("Taj City Centre Patna | The Centurion Resort | The Buddha Resort / Sambodhi", "Patna (1 Night) / Rajgir (1 Night) / Bodhgaya (3 Nights)", "05 Nights", "Luxury", "Luxury Room", "MAPAI (Breakfast & Dinner)", 5, 3, description="OPTION 03 – LUXURY: Taj City Centre Patna (Patna, 1 Night) | The Centurion Resort (Rajgir, 1 Night) | The Buddha Resort / Sambodhi (Bodhgaya, 3 Nights)"),
            _hotel("Taj City Centre (Luxury Suite) | VVIP Custom Wellness Villa | The Marasa Sarovar Premiere", "Patna (1 Night) / Rajgir (1 Night) / Bodhgaya (3 Nights)", "05 Nights", "Ultra Luxury", "Luxury Suite / Villa", "MAPAI (Breakfast & Dinner)", 5, 4, description="OPTION 04 – ULTRA LUXURY: Taj City Centre Luxury Suite (Patna, 1 Night) | VVIP Custom Wellness Villa (Rajgir, 1 Night) | The Marasa Sarovar Premiere (Bodhgaya, 3 Nights)"),
        ],
        inclusions=[
            _inc_included("Premium Stays: 05 Nights at elite hotels and wellness resorts.", 1),
            _inc_included("Luxury Transportation: Private air-conditioned luxury SUV for entire circuit routing.", 2),
            _inc_included("Curated Meal Plan: Daily lavish breakfasts and gourmet buffet dinners.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated personal guest relations manager.", 4),
            _inc_included("Welcome Amenities: Personalized spiritual travel kit, refreshing drinks, and wet wipes.", 5),
            _inc_included("Complimentary Experience: Private aerial ropeway tickets for Vishwa Shanti Stupa.", 6),
            _inc_excluded("Domestic or international flights and train fares to Patna/Gaya.", 7),
            _inc_excluded("Monument entrance fees, dynamic camera permissions, and local monastery guide tips.", 8),
            _inc_excluded("Personal expenses such as premium laundry, dry cleaning, telephone calls, or room service.", 9),
            _inc_excluded("Optional meditation courses, private pooja costs, or extra sightseeing tours.", 10),
        ],
    )
    return package, itinerary


def build_br_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "BR-003"
    tour_code = "TRG-BIH-003"
    title = (
        "TRAGUIN Premium Bihar Tour Package — Bihar Heritage • "
        "Journey Through Enlightenment & Legacies: Patna • Nalanda • Rajgir • Bodhgaya"
    )
    duration = "04 Nights / 05 Days"
    slug = "br-003-bihar-heritage-patna-nalanda-rajgir-bodhgaya"
    itin_slug = "br-003-bihar-heritage-patna-nalanda-rajgir-bodhgaya-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Bihar / India | Category: Premium Family Tour", 2),
            _ph("Destinations: Patna • Nalanda • Rajgir • Bodhgaya", 3),
            _ph("Ideal for: Family Getaways, Cultural Explorers & Heritage Seekers", 4),
            _ph("Best season: October to March (Pleasant Winters)", 5),
            _ph("Starting price: On Request (Premium Customised)", 6),
            _ph("Vehicle / Meals: Private Luxury AC Vehicle / MAPAI (Breakfast & Dinner)", 7),
            _ph("Route Plan: Patna (1N) ➔ Nalanda ➔ Rajgir (1N) ➔ Bodhgaya (2N) ➔ Patna Departure", 8),
            _ph("TRAGUIN Signature Experience: Private local storytelling guide presentation before stepping inside Nalanda University Ruins.", 9),
            _ph("Curated by TRAGUIN Experts: Seamless coordination with local authorities for swift entry permissions into highly regulated glass-bridge facilities.", 10),
            _ph("Premium Handpicked Hotels: Accommodations rigorously audited for family-friendly security, hygiene, and prime tranquility.", 11),
            _ph("Shopping & Local Experiences: Madhubani art, Bhagalpuri silk shawls, stone carvings, Sikki grass handicrafts; Litti Chokha, Tilkut, Khaja.", 12),
            _ph("Important Notes: Check-in 14:00 / check-out 11:00; light winter clothing Nov–Feb; book 30–45 days ahead for glass bridge and Nalanda.", 13),
        ],
        moods=["Family", "Cultural", "Luxury", "History"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note="On Request (Premium Customised)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Bihar Heritage • Patna • Nalanda • Rajgir • Bodhgaya • 04 Nights / 05 Days",
        overview=(
            "Welcome to an unforgettable odyssey of cultural legacy, meticulously curated by TRAGUIN. Embark on the "
            "finest Bihar Family Tour designed to unveil ancient kingdoms, spiritual landmarks, and the timeless roots "
            "of absolute enlightenment.\n\n"
            "TOUR OVERVIEW\n"
            "This custom-tailored Premium Bihar Experience offers a perfect equilibrium of historical discovery, imperial "
            "architectures, and modern relaxed leisure. Travelling in a completely private luxury AC vehicle accompanied "
            "by an experienced, well-mannered chauffeur, your family will enjoy absolute comfort and privacy across cities. "
            "Our specialized meal plan ensures you start and end your days with exquisite buffet spreads featuring both "
            "international dishes and rich local flavors. Every segment of your holiday is stamped with the signature touch "
            "of TRAGUIN curated experiences, promising smooth skip-the-line VIP entries, vetted local heritage guides, "
            "and around-the-clock bespoke support.\n\n"
            "WHY CHOOSE THE BEST BIHAR TOUR PACKAGE?\n"
            "When exploring opportunities for a Luxury Bihar Holiday, travelers search for a profound narrative "
            "connection with history alongside top-tier modern indulgence. Bihar is home to some of the most globally "
            "renowned iconic attractions. From the sacred Mahabodhi Temple to the breathtaking landscapes surrounding the "
            "Rajgir Glass Bridge, the state offers diverse highlights. For families mapping out a rewarding Bihar Family "
            "Tour, the circuit offers multiple popular Instagram locations including the Vishwa Shanti Stupa, Nalanda "
            "University ruins, and Patna Museum."
        ),
        seo_title="BR-003 | Bihar Heritage Patna Nalanda Rajgir Bodhgaya | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Bihar family tour (BR-003 / TRG-BIH-003): Patna, Nalanda, Rajgir, "
            "Bodhgaya, and 4-tier handpicked accommodation."
        ),
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Patna arrival, Golghar, Patna Museum, Ganges riverfront on Day 01", 1),
            _ih("Nalanda University ruins and transfer to Rajgir on Day 02", 2),
            _ih("Rajgir ropeway, Vishwa Shanti Stupa, Glass Bridge, Bodhgaya on Day 03", 3),
            _ih("Mahabodhi Temple, Bodhi Tree, international monasteries on Day 04", 4),
            _ih("Bodhgaya to Patna departure on Day 05", 5),
        ],
        days=[
            _day(1, "ARRIVAL IN PATNA | WELCOME TO ANCIENT PATALIPUTRA – THE GATEWAY OF EMPIRES", (
                "Your luxury Bihar sightseeing tour commences as you arrive at Patna Airport or Railway Station, greeted "
                "warmly by your private luxury transport chauffeur. Transfer smoothly to your handpicked premium hotel in the "
                "city center. After a brief afternoon refresh, step out into a world of antiquity. Visit the magnificent Golghar, "
                "offering a majestic aerial view of the meandering Ganges River. Explore the Patna Museum to witness rare "
                "archaeological discoveries before enjoying a private evening luxury cruise over the sacred Ganges."
            ), [
                "Sightseeing Included: Golghar, Patna Museum, Takht Sri Patna Sahib, Evening Ganges Riverfront.",
                "Evening Experience: Private family riverfront sunset walk followed by a curated local dessert-tasting experience.",
                "Overnight Stay: Patna (Premium / Luxury Selected Hotel).",
                "Meals Included: Welcome Drink & Fine Dining Dinner.",
            ]),
            _day(2, "PATNA TO RAJGIR VIA NALANDA | THE CRADLE OF WISDOM & IMPERIAL RUINS", (
                "After a sumptuous breakfast, check out and drive towards the legendary ruins of Nalanda University, an "
                "internationally celebrated UNESCO World Heritage Site. Walk through the sprawling brick structures where "
                "ancient scholars once studied under expert guidance. Continue to the Nalanda Archaeological Museum to "
                "view beautifully preserved bronze icons. By late afternoon, arrive in Rajgir—a serene valley locked inside "
                "seven majestic hills. Check into your premium resort and relax amidst nature."
            ), [
                "Sightseeing Included: Nalanda University Ruins, Xuanzang Memorial Hall, Nalanda Museum, Rajgir hot springs.",
                "Optional Activities: Guided heritage photography walk with an expert local archeological historian.",
                "Overnight Stay: Rajgir (Premium Wellness Landscape Resort).",
                "Meals Included: Premium Breakfast & Luxury Resort Buffet Dinner.",
            ]),
            _day(3, "RAJGIR EXPLORATION TO BODHGAYA | WALKING AMONG THE CLOUDS & RIDGEWAYS OF PEACE", (
                "An exhilarating day awaits your family in Rajgir. Board the modern aerial ropeway system to ascend the "
                "Ratnagiri hill, reaching the pristine white Vishwa Shanti Stupa (Peace Pagoda). Take in breathtaking "
                "landscapes and peaceful valley vistas. Next, walk along the thrilling Rajgir Glass Bridge (subject to online slot "
                "availability), a popular Instagram location. Visit the ancient Cyclopean Walls and Ajatshatru Fort before your "
                "premium vehicle chauffeurs you to the spiritual destination of Bodhgaya."
            ), [
                "Sightseeing Included: Vishwa Shanti Stupa, Griddhakuta (Vulture's Peak), Glass Flyover Bridge, Bimbisara Jail.",
                "Evening Experience: Private evening drive into Bodhgaya to absorb the soothing chants of global spiritual monasteries.",
                "Overnight Stay: Bodhgaya (Bespoke Luxury Hotel).",
                "Meals Included: Premium Breakfast & Traditional Gourmet Dinner.",
            ]),
            _day(4, "BODHGAYA IMMERSIVE EXPERIENCES | SPIRITUAL ENLIGHTENMENT UNDER THE SACRED BODHI TREE", (
                "Dedicate your day to the core of tranquility—Bodhgaya. Following breakfast, visit the magnificent UNESCO-listed "
                "Mahabodhi Temple complex, housing the exact spot where Prince Siddhartha attained ultimate enlightenment to "
                "become the Buddha. Sit peacefully beneath the sacred Bodhi Tree and observe monks chanting in unison. Spend your "
                "afternoon visiting beautiful global monasteries built by Thailand, Japan, and Bhutan, each displaying brilliant "
                "architectural diversity."
            ), [
                "Sightseeing Included: Mahabodhi Temple, Great Buddha Statue (80 feet), Thai Monastery, Royal Bhutan Monastery, Muchalinda Lake.",
                "Optional Activities: A private guided meditation session inside a quiet garden enclave arranged by TRAGUIN.",
                "Overnight Stay: Bodhgaya (Bespoke Luxury Hotel).",
                "Meals Included: Premium Breakfast & Farewell Celebration Dinner.",
            ]),
            _day(5, "BODHGAYA TO PATNA / DEPARTURE | RETURNING WITH DEEP WISDOM & CHERISHED BONDS", (
                "Enjoy a final lavish breakfast at your luxury hotel. Pack your belongings alongside precious cultural souvenirs. "
                "Your private vehicle will safely transport you back along the smooth national highway to Patna Airport or Gaya "
                "Airport for your flight home. Return to your routine carrying a renewed sense of peace and unforgettable "
                "memories beautifully curated by TRAGUIN."
            ), [
                "Transfers Included: Private door-to-door highway airport/station drop-off.",
                "Meals Included: Sumptuous Buffet Breakfast.",
            ]),
        ],
        hotels=[
            _hotel("Hotel Maurya / Lemon Tree | The Gargee Gautam Vihar | Hotel Delta International", "Patna (1 Night) / Rajgir (1 Night) / Bodhgaya (2 Nights)", "04 Nights", "Deluxe", "Deluxe Room", "MAPAI (Breakfast & Dinner)", 4, 1, description="OPTION 01 – DELUXE: Hotel Maurya / Lemon Tree (Patna, 1 Night) | The Gargee Gautam Vihar (Rajgir, 1 Night) | Hotel Delta International (Bodhgaya, 2 Nights) | MAPAI (Breakfast & Dinner)"),
            _hotel("Gargee Grand / similar | Hotel Indo Hokke / similar | Maha Bodhi Hotel & Resort", "Patna (1 Night) / Rajgir (1 Night) / Bodhgaya (2 Nights)", "04 Nights", "Premium", "Premium Room", "MAPAI (Breakfast & Dinner)", 4, 2, description="OPTION 02 – PREMIUM: Gargee Grand / similar (Patna, 1 Night) | Hotel Indo Hokke / similar (Rajgir, 1 Night) | Maha Bodhi Hotel & Resort (Bodhgaya, 2 Nights) | MAPAI (Breakfast & Dinner)"),
            _hotel("Hotel Chanakya (Suite) | Rajgir Residency Luxury Wing | The Zenland Resort / Marasa Sarovar", "Patna (1 Night) / Rajgir (1 Night) / Bodhgaya (2 Nights)", "04 Nights", "Luxury", "Luxury Room", "MAPAI (Breakfast & Dinner)", 5, 3, description="OPTION 03 – LUXURY: Hotel Chanakya Suite (Patna, 1 Night) | Rajgir Residency Luxury Wing (Rajgir, 1 Night) | The Zenland Resort / Marasa Sarovar (Bodhgaya, 2 Nights) | MAPAI (Breakfast & Dinner)"),
            _hotel("Premium VVIP Club Suite Stay | Bodhgaya Regency Presidential Wing | The Royal Residency Elite Club", "Patna (1 Night) / Rajgir (1 Night) / Bodhgaya (2 Nights)", "04 Nights", "Ultra Luxury", "Luxury Suite / Villa", "MAPAI (Breakfast & Dinner)", 5, 4, description="OPTION 04 – ULTRA LUXURY: Premium VVIP Club Suite Stay (Patna, 1 Night) | Bodhgaya Regency Presidential Wing (Rajgir, 1 Night) | The Royal Residency Elite Club (Bodhgaya, 2 Nights) | MAPAI (Breakfast & Dinner)"),
        ],
        inclusions=[
            _inc_included("Premium Stays: Selected heritage and luxury hotels as per your chosen tier.", 1),
            _inc_included("Luxury Transportation: All transfers & sightseeing in a private chauffeured AC vehicle.", 2),
            _inc_included("Curated Meal Plan: Daily premium breakfast and elaborate dinners (MAPAI).", 3),
            _inc_included("TRAGUIN Support: Dedicated guest relationship executive supervising your tour logistics.", 4),
            _inc_included("Welcome Amenities: Customized luxury welcome pack with regional goodies on day 1.", 5),
            _inc_included("Complimentary Experience: Private family sunset boat ride on the Ganges River.", 6),
            _inc_excluded("Airfare, flight tickets, or cross-state interstate rail passes.", 7),
            _inc_excluded("Monument entrance tickets, local guide tipping, or special pooja receipts.", 8),
            _inc_excluded("Personal expenses such as premium room laundry, mini-bar, or outside drinks.", 9),
            _inc_excluded("Any insurance coverages or additional transport diversions not inside the route.", 10),
        ],
    )
    return package, itinerary


def build_br_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "BR-004"
    tour_code = "TRG-BIH-004"
    title = (
        "TRAGUIN Premium Bihar Tour Package — Nalanda Rajgir Tour • "
        "Journey Through the Cradle of Enlightenment: Patna • Nalanda • Rajgir • Bodhgaya"
    )
    duration = "04 Nights / 05 Days"
    slug = "br-004-nalanda-rajgir-spiritual-pilgrimage-patna-bodhgaya"
    itin_slug = "br-004-nalanda-rajgir-spiritual-pilgrimage-patna-bodhgaya-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Bihar / India | Category: Premium Spiritual & Pilgrimage Tour", 2),
            _ph("Destinations: Patna • Nalanda • Rajgir • Bodhgaya", 3),
            _ph("Ideal for: Families, Spiritual Seekers & History Enthusiasts", 4),
            _ph("Best season: October to March (Pleasant & Ideal for Sightseeing)", 5),
            _ph("Starting price: On Request (Premium Customised Packages)", 6),
            _ph("Vehicle / Meals: Luxury SUV / MAPAI (Daily Breakfast & Gourmet Dinner)", 7),
            _ph("Route Plan: Patna Arrival ➔ Rajgir (3N) ➔ Nalanda Excursion ➔ Bodhgaya (1N) ➔ Patna Departure", 8),
            _ph("TRAGUIN Signature Experience: Private scholar-led introduction to Nalanda's history before visiting the ruins.", 9),
            _ph("Curated by TRAGUIN Experts: Carefully planned routing that balances sacred pilgrimage sites with comfort and leisure time.", 10),
            _ph("Premium Handpicked Hotels: Accommodations chosen based on excellent safety standards and top comfort ratings.", 11),
            _ph("Shopping & Local Experiences: Madhubani paintings, stone carvings, tusser silk sarees, wooden toys; Khaja, Litti Chokha, Tilkut.", 12),
            _ph("Important Notes: Check-in 14:00 / check-out 11:00; light winter wear Oct–Mar; book 30–45 days ahead.", 13),
        ],
        moods=["Pilgrimage", "Spiritual", "Family", "Luxury", "History"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note="On Request (Premium Customised Packages)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Nalanda Rajgir Spiritual Pilgrimage • Patna • Nalanda • Rajgir • Bodhgaya • 04 Nights / 05 Days",
        overview=(
            "Welcome to a profound spiritual odyssey curated exclusively by TRAGUIN. Embark on the definitive Bihar "
            "Pilgrimage Tour designed to unearth the ancient wisdom, breathtaking landscapes, and imperial legacies of "
            "Nalanda and Rajgir.\n\n"
            "TOUR OVERVIEW\n"
            "This custom-tailored pilgrimage itinerary offers an elite, comfortable journey across the spiritual heartland "
            "of Bihar. Traveling in a premium air-conditioned vehicle with a professional chauffeur, your family will experience "
            "absolute privacy and comfort. Featuring a rich, handpicked culinary meal plan with exquisite breakfasts and "
            "lavish dinners, this route represents the highest tier of the premium Bihar experience. Every part of your "
            "journey comes imbued with the TRAGUIN curated experience note, guaranteeing VIP monument access, expert historian "
            "guides, and round-the-clock specialized assistance.\n\n"
            "WHY VISIT BIHAR? DISCOVER THE BEST BIHAR TOUR PACKAGE\n"
            "When planning a Luxury Bihar Holiday, travelers seek an authentic connection to history, spiritual serenity, "
            "and seamless execution. From the world-famous UNESCO World Heritage ruins of Nalanda University to the misty "
            "valleys and peace pagodas of Rajgir, Bihar sightseeing offers deep intellectual and spiritual illumination."
        ),
        seo_title="BR-004 | Nalanda Rajgir Spiritual Pilgrimage | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days spiritual pilgrimage (BR-004 / TRG-BIH-004): Rajgir, Nalanda, "
            "Bodhgaya, and 4-tier handpicked accommodation."
        ),
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Patna arrival and transfer to Rajgir on Day 01", 1),
            _ih("Nalanda University ruins and museum excursion on Day 02", 2),
            _ih("Rajgir ropeway, Vishwa Shanti Stupa, Glass Bridge, Ghora Katora on Day 03", 3),
            _ih("Rajgir to Bodhgaya, Mahabodhi Temple and monasteries on Day 04", 4),
            _ih("Bodhgaya to Patna departure on Day 05", 5),
        ],
        days=[
            _day(1, "ARRIVAL IN PATNA TO RAJGIR | WELCOME TO THE KINGDOM OF MAGADHA – ENROUTE TO SACRED HILLS", (
                "Your premium Bihar experience begins upon your arrival at Patna Airport or Railway Station, where a "
                "dedicated private luxury transport vehicle waits to escort you. Leave the urban sprawl behind as you drive "
                "towards Rajgir, a city cradled by five majestic hills. On the way, stop for refreshing premium breaks and "
                "capture the scenic beauty of the countryside. Upon arrival in Rajgir, check into your handpicked luxury resort "
                "and enjoy a welcome note amenity kit prepared by our experts."
            ), [
                "Sightseeing Included: Scenic highway drive, rural landscape vistas, evening temple stroll.",
                "Evening Experience: Relaxing traditional spa or foot reflexology session at the luxury resort.",
                "Overnight Stay: Rajgir (Premium Selected Luxury Resort).",
                "Meals Included: Welcome Drink & Gourmet Dinner.",
            ]),
            _day(2, "NALANDA SIGHTSEEING EXCURSION | THE FOUNT OF ANCIENT KNOWLEDGE – REMAINS OF GLORY", (
                "Indulge in a lavish breakfast before departing for Nalanda, home to the top tourist places in Bihar. Walk "
                "among the awe-inspiring red-brick ruins of the ancient Nalanda University, a global epicenter of learning from "
                "the 5th to 12th centuries AD. Your private historian guide will share emotionally resonant stories of monks, "
                "travelers, and ancient libraries. Next, visit the nearby Xuanzang Memorial Hall, a beautiful oriental temple "
                "dedicated to the legendary Chinese traveler."
            ), [
                "Sightseeing Included: Nalanda University Archaeological Ruins, Nalanda Museum, Xuanzang Memorial.",
                "Photography Points: The iconic stupa of Sariputra and manicured university gardens.",
                "Overnight Stay: Rajgir (Premium Selected Luxury Resort).",
                "Meals Included: Premium Breakfast & Authentic Dinner.",
            ]),
            _day(3, "RAJGIR EXPLORATION & ADVENTURE | SPIRITUAL ASCENTS, PEACE PAGODAS & MODERN MARVELS", (
                "Savor an early breakfast to maximize a day packed with immersive experiences. Board the scenic ropeway to "
                "reach the top of Ratnagiri Hill, home to the striking white Vishwa Shanti Stupa (World Peace Pagoda). Walk to "
                "Gridhakuta (Vulture's Peak), where Lord Buddha delivered many of his most significant sermons. In the "
                "afternoon, enjoy a thrilling walk across the high-altitude Rajgir Glass Bridge, a popular Instagram location "
                "offering bird's-eye views of the deep mountain valley. Conclude with a peaceful eco-friendly horse-carriage "
                "ride to Ghora Katora Lake."
            ), [
                "Sightseeing Included: Vishwa Shanti Stupa, Gridhakuta Hill, Rajgir Glass Bridge, Ghora Katora Lake.",
                "Optional Activities: Boating on Ghora Katora Lake, dipping in the therapeutic hot springs of Saptaparni.",
                "Overnight Stay: Rajgir (Premium Selected Luxury Resort).",
                "Meals Included: Premium Breakfast & Fine-Dining Dinner.",
            ]),
            _day(4, "RAJGIR TO BODHGAYA EXCURSION | THE SITE OF GREAT ENLIGHTENMENT – ULTIMATE SERENITY", (
                "Following a rich morning buffet, enjoy a scenic drive to Bodhgaya, the ultimate spiritual destination. Stand "
                "beneath the holy Bodhi Tree inside the magnificent Mahabodhi Temple complex, where Prince Siddhartha attained "
                "supreme enlightenment to become the Buddha. Witness monks from around the globe chanting in unison. Spend your "
                "afternoon visiting the stunning international monasteries built by Japan, Thailand, and Bhutan, each showcasing "
                "unique architectural beauty."
            ), [
                "Sightseeing Included: Mahabodhi Temple (UNESCO site), Great Buddha Statue, Thai Monastery, Indosan Nippon Temple.",
                "Evening Experience: A private meditation session under the Bodhi tree arranged by TRAGUIN experts.",
                "Overnight Stay: Bodhgaya (Premium Luxury Boutique Hotel).",
                "Meals Included: Premium Breakfast & Farewell Dinner.",
            ]),
            _day(5, "BODHGAYA TO PATNA / DEPARTURE | CHERISHING FAITH, HISTORY & UNFORGETTABLE MEMORIES", (
                "Enjoy your last breakfast at your premium hotel, taking in the calm, spiritual atmosphere one final time. Your "
                "luxury transportation will drive you comfortably back along the smooth highway to Patna Airport or Railway "
                "Station. Return home carrying a heart filled with profound peace and unforgettable memories designed "
                "flawlessly by TRAGUIN."
            ), [
                "Transfers Included: Private luxury highway drop-off to Patna airport/station.",
                "Meals Included: Sumptuous Buffet Breakfast.",
            ]),
        ],
        hotels=[
            _hotel("Hotel Indo Hokke / similar | Hotel Tokyo Vihar / similar", "Rajgir (3 Nights) / Bodhgaya (1 Night)", "04 Nights", "Deluxe", "Deluxe Room", "MAPAI (Breakfast & Dinner)", 4, 1, description="OPTION 01 – DELUXE: Hotel Indo Hokke / similar (Rajgir, 3 Nights) | Hotel Tokyo Vihar / similar (Bodhgaya, 1 Night) | MAPAI (Breakfast & Dinner)"),
            _hotel("The Gargee Gautam Vihar / similar | Maha Bodhi Hotel & Resort", "Rajgir (3 Nights) / Bodhgaya (1 Night)", "04 Nights", "Premium", "Premium Room", "MAPAI (Breakfast & Dinner)", 4, 2, description="OPTION 02 – PREMIUM: The Gargee Gautam Vihar / similar (Rajgir, 3 Nights) | Maha Bodhi Hotel & Resort (Bodhgaya, 1 Night) | MAPAI (Breakfast & Dinner)"),
            _hotel("Nalanda Heritage Resort (Premium Suite) | The Lotus Nikko / similar", "Rajgir (3 Nights) / Bodhgaya (1 Night)", "04 Nights", "Luxury", "Luxury Room", "MAPAI + Welcome Fruit Basket", 5, 3, description="OPTION 03 – LUXURY: Nalanda Heritage Resort Premium Suite (Rajgir, 3 Nights) | The Lotus Nikko / similar (Bodhgaya, 1 Night) | MAPAI + Welcome Fruit Basket"),
            _hotel("The Fern Residency Luxury Retreat | The Marasa Sarovar Excellence Suite", "Rajgir (3 Nights) / Bodhgaya (1 Night)", "04 Nights", "Ultra Luxury", "Luxury Suite / Villa", "Bespoke Gourmet Curated Meal Plan", 5, 4, description="OPTION 04 – ULTRA LUXURY: The Fern Residency Luxury Retreat (Rajgir, 3 Nights) | The Marasa Sarovar Excellence Suite (Bodhgaya, 1 Night) | Bespoke Gourmet Curated Meal Plan"),
        ],
        inclusions=[
            _inc_included("Premium Stays: 4 Nights in selected high-end heritage hotels & resorts.", 1),
            _inc_included("Luxury Transportation: Chauffeur-driven AC SUV for the entire tour.", 2),
            _inc_included("Curated Meal Plan: Daily premium breakfast and elaborate dinners (MAPAI).", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated guest experience manager on call.", 4),
            _inc_included("Welcome Amenities: Customized family travel kit and regional refreshments.", 5),
            _inc_included("Complimentary Experience: Private horse-carriage ride to Ghora Katora Lake.", 6),
            _inc_excluded("Airfare, domestic flight tickets, or train tickets.", 7),
            _inc_excluded("Monument entry tickets, camera fees, and local guide charges.", 8),
            _inc_excluded("Personal expenses such as laundry, phone calls, or tips.", 9),
            _inc_excluded("Any optional adventure sports or activities not listed above.", 10),
        ],
    )
    return package, itinerary


def build_br_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "BR-005"
    tour_code = "TRG-BIP-005"
    title = (
        "TRAGUIN Premium Bihar Tour Package — Buddhist Leisure Tour • "
        "An Enlightenment Journey: Patna • Bodhgaya • Rajgir • Nalanda"
    )
    duration = "05 Nights / 06 Days"
    slug = "br-005-buddhist-leisure-senior-citizen-patna-bodhgaya-rajgir-nalanda"
    itin_slug = "br-005-buddhist-leisure-senior-citizen-patna-bodhgaya-rajgir-nalanda-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Bihar / India | Category: Senior Citizen Holiday", 2),
            _ph("Destinations: Patna • Bodhgaya • Rajgir • Nalanda", 3),
            _ph("Ideal for: Senior Citizens, Families, and Spiritual Seekers", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Fully Customized)", 6),
            _ph("Vehicle / Meals: Luxury Tempo Traveller / Innova Crysta (MAPAI)", 7),
            _ph("Route Plan: Patna (2N) ➔ Bodhgaya via Rajgir & Nalanda (3N) ➔ Patna (2N) ➔ Departure", 8),
            _ph("TRAGUIN Signature Experience: Reserved seating arrangements for evening prayer ceremonies inside major temple zones.", 9),
            _ph("Curated by TRAGUIN Experts: Slow-paced routing designed to bypass heavy road bumps, prioritizing maximum passenger relaxation.", 10),
            _ph("Personalized Assistance: Dedicated luggage handlers at check-in points to avoid physical strain for senior citizens.", 11),
            _ph("Shopping & Local Experiences: Madhubani paintings, Bhagalpuri Tussar Silk, stone statues; Khaja, Tilkut, light lentil preparations.", 12),
            _ph("Important Notes: Ground floor rooms prioritized; light shawls Oct–Mar; book 45 days ahead for premium transport.", 13),
        ],
        moods=["Pilgrimage", "Spiritual", "Family", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note="On Request (Premium Fully Customized)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Buddhist Leisure Senior Citizen Tour • Patna • Bodhgaya • Rajgir • Nalanda • 05 Nights / 06 Days",
        overview=(
            "Welcome to an extraordinary spiritual odyssey curated meticulously by TRAGUIN. Embark on the finest "
            "Bihar Senior Citizen Holiday, expertly structured to ensure a smooth, slow-paced, and highly comfortable "
            "journey.\n\n"
            "TOUR OVERVIEW\n"
            "This bespoke luxury holiday is specifically curated for senior citizens who wish to explore the rich history "
            "of Bihar with zero exhaustion. Traveling in a fully sanitized, premium luxury transportation vehicle with an "
            "experienced, patient chauffeur, our guests enjoy total relaxation. The meal plan is thoughtfully tailored with "
            "light, nutritious breakfasts and dinners (MAPAI) suitable for seniors. With special route mapping, minimum "
            "walking tracks, and the signature TRAGUIN curated experience note, we guarantee VIP access to sacred "
            "monuments and smooth, leisurely pacing throughout your itinerary.\n\n"
            "WHY BOOK THE BEST BIHAR TOUR PACKAGE?\n"
            "When considering a Luxury Bihar Holiday, travelers search for seamless logistics, historical depth, and "
            "peaceful environments. Bihar is home to some of the most sacred and iconic attractions in the world, from the "
            "world-famous Mahabodhi Temple in Bodhgaya to the ruins of the ancient Nalanda University."
        ),
        seo_title="BR-005 | Senior Citizen Buddhist Leisure Patna Bodhgaya | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days senior citizen holiday (BR-005 / TRG-BIP-005): Patna, Bodhgaya, "
            "Rajgir, Nalanda, and 4-tier senior-friendly accommodation."
        ),
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Patna arrival, Bihar Museum, Ganga Path sunset on Day 01", 1),
            _ih("Patna to Bodhgaya via Rajgir ropeway and Nalanda on Day 02", 2),
            _ih("Mahabodhi Temple, Bodhi Tree, monasteries on Day 03", 3),
            _ih("Dungeshwari Caves excursion and leisure afternoon on Day 04", 4),
            _ih("Bodhgaya to Patna, Takht Sri Patna Sahib on Day 05", 5),
            _ih("Patna departure on Day 06", 6),
        ],
        days=[
            _day(1, "ARRIVAL IN PATNA | WELCOME TO THE ANCIENT CAPITAL OF PATALIPUTRA", (
                "Your premium Bihar experience begins as you arrive at Patna Airport or Railway Station. A dedicated "
                "representative will receive you with a warm welcome amenity kit and guide you to your private luxury vehicle. "
                "Transfer to your handpicked premium hotel for a smooth check-in. In the afternoon, enjoy a relaxed visit to the "
                "modern Bihar Museum, an absolute masterpiece of art and history. Later, take a calm evening drive along the "
                "Ganga Path (Marine Drive) to witness a beautiful sunset over the holy River Ganges."
            ), [
                "Sightseeing Included: Bihar Museum (with accessible corridors) and comfortable drive along Ganga Path.",
                "Evening Experience: Relaxed welcome dinner at the hotel featuring light local and continental options.",
                "Overnight Stay: Patna (Premium / Luxury Selected Hotel).",
                "Meals Included: Welcome Drink & Luxury Dinner.",
            ]),
            _day(2, "PATNA TO BODHGAYA (VIA NALANDA & RAJGIR) | JOURNEY TO THE LAND OF SPIRITUAL AWAKENING", (
                "Following a wholesome, leisurely breakfast, embark on a smooth scenic drive toward Bodhgaya. En route, we "
                "visit Rajgir, nestled amidst beautiful green hills. Board the safe, enclosed ropeway to ascend the Gridhakuta "
                "Hill (Vulture's Peak) to witness the magnificent Vishwa Shanti Stupa, offering breathtaking landscapes of the "
                "valley below. Afterward, enjoy a brief comfortable stop at the ancient Nalanda University ruins, an iconic "
                "attraction of global heritage, before checking into your premium resort in Bodhgaya."
            ), [
                "Sightseeing Included: Rajgir Ropeway, Peace Stupa, Gridhakuta Hill, Nalanda Archaeological Ruins.",
                "Optional Activities: An electric golf-cart ride through Nalanda ruins for a complete fatigue-free experience.",
                "Overnight Stay: Bodhgaya (Premium Handpicked Luxury Resort).",
                "Meals Included: Premium Breakfast & Resort Dinner.",
            ]),
            _day(3, "HOLY BODHGAYA SIGHTSEEING | IMMERSIVE CALMNESS UNDER THE SACRED BODHI TREE", (
                "Dedicate this day to deep peace and spiritual reflection. Visit the UNESCO World Heritage Mahabodhi Temple "
                "Complex. Sit under the sacred Bodhi Tree where Lord Buddha attained enlightenment over 2,500 years ago. "
                "The emotional storytelling by our expert local guide will transport you back in time. Explore the tranquil "
                "international monasteries nearby, including the Great Buddha Statue, the Thai Monastery, and the Japanese "
                "Temple, all designed with beautiful pathways."
            ), [
                "Sightseeing Included: Mahabodhi Temple, Sacred Bodhi Tree, Mucalinda Lake, 80-foot Great Buddha Statue.",
                "Evening Experience: Private evening meditation session and butter-lamp lighting arranged by TRAGUIN experts.",
                "Overnight Stay: Bodhgaya (Premium Handpicked Luxury Resort).",
                "Meals Included: Nutritious Breakfast & Gourmet Dinner.",
            ]),
            _day(4, "EXCURSION TO DUNGESHWARI CAVES | THE PATH OF ASCETICISM & SCENIC RURAL BEAUTY", (
                "Enjoy a relaxed morning breakfast before heading out on a scenic excursion to the Dungeshwari Cave "
                "Temples (Mahakala Caves), located across the beautiful Falgu River. This is the historic site where Buddha "
                "practiced severe penance before realizing the middle path. The drive features rolling hills and local rustic "
                "scenery. The afternoon is kept completely free for leisure, allowing senior travelers to rest, enjoy the resort's "
                "premium amenities, or enjoy a walk in the meditation gardens."
            ), [
                "Sightseeing Included: Dungeshwari Caves, local village viewpoints, Sujata Stupa.",
                "Optional Activities: Private interactive talk session with a Buddhist scholar at the resort lounge.",
                "Overnight Stay: Bodhgaya (Premium Handpicked Luxury Resort).",
                "Meals Included: Premium Breakfast & Special Diet Dinner.",
            ]),
            _day(5, "BODHGAYA TO PATNA | HERITAGE REVIVAL & LOCAL CULTURAL IMMERSION", (
                "Drive back comfortably to Patna along smooth highways. Upon reaching, check into your luxury hotel. Spend "
                "your afternoon visiting the Takht Sri Patna Sahib, the magnificent birthplace of Guru Gobind Singh Ji, which "
                "offers deep spiritual vibrations and excellent hospitality. Spend your final evening enjoying local shopping for "
                "exquisite Madhubani paintings or relaxing at the hotel's premium wellness center."
            ), [
                "Sightseeing Included: Takht Sri Patna Sahib Gurudwara, local handloom cooperative emporiums.",
                "Evening Experience: A grand farewell dinner showcasing light gourmet cuisines curated for your comfort.",
                "Overnight Stay: Patna (Premium / Luxury Selected Hotel).",
                "Meals Included: Breakfast & Farewell Gala Dinner.",
            ]),
            _day(6, "DEPARTURE FROM PATNA | CHERISHING FAITH, PEACE, AND UNFORGETTABLE MEMORIES", (
                "Indulge in a final lavish breakfast at your premium hotel. Your private luxury transportation vehicle will pick you "
                "up from the lobby and transfer you safely to Patna Airport or Railway Station for your journey home. Depart "
                "with a rejuvenated spirit, absolute peace, and unforgettable memories designed meticulously by TRAGUIN."
            ), [
                "Transfers Included: Private premium terminal drop-off with luggage assistance.",
                "Meals Included: Sumptuous Buffet Breakfast.",
            ]),
        ],
        hotels=[
            _hotel("Hotel Maurya / similar | The Bodhi Palace Resort / similar", "Patna (2 Nights) / Bodhgaya (3 Nights)", "05 Nights", "Deluxe", "Deluxe Room", "MAPAI (Breakfast & Dinner)", 4, 1, description="OPTION 01 – DELUXE: Hotel Maurya / similar (Patna, 2 Nights) | The Bodhi Palace Resort / similar (Bodhgaya, 3 Nights) | Wheelchair Access, Elevator, Senior Friendly | MAPAI"),
            _hotel("Lemon Tree Premier / similar | Maha Bodhi Hotel & Resort", "Patna (2 Nights) / Bodhgaya (3 Nights)", "05 Nights", "Premium", "Premium Room", "MAPAI (Breakfast & Dinner)", 4, 2, description="OPTION 02 – PREMIUM: Lemon Tree Premier / similar (Patna, 2 Nights) | Maha Bodhi Hotel & Resort (Bodhgaya, 3 Nights) | Premium Bedding, Quiet Rooms, Doctor on Call | MAPAI"),
            _hotel("Taj City Centre Patna | Hygge Central Bodhgaya / similar", "Patna (2 Nights) / Bodhgaya (3 Nights)", "05 Nights", "Luxury", "Luxury Room", "MAPAI (Breakfast & Dinner)", 5, 3, description="OPTION 03 – LUXURY: Taj City Centre Patna (Patna, 2 Nights) | Hygge Central Bodhgaya / similar (Bodhgaya, 3 Nights) | Luxury Bathrooms, Garden Walks, Personalized Diet | MAPAI"),
            _hotel("Taj City Centre (Executive Suite) | Marasa Sarovar Premiere (Luxury Villa)", "Patna (2 Nights) / Bodhgaya (3 Nights)", "05 Nights", "Ultra Luxury", "Luxury Suite / Villa", "MAPAI (Breakfast & Dinner)", 5, 4, description="OPTION 04 – ULTRA LUXURY: Taj City Centre Executive Suite (Patna, 2 Nights) | Marasa Sarovar Premiere Luxury Villa (Bodhgaya, 3 Nights) | Private Concierge, Specialized VVIP Ground Care | MAPAI"),
        ],
        inclusions=[
            _inc_included("Premium Stays: Luxury accommodations with senior-friendly ground-floor options.", 1),
            _inc_included("Luxury Transportation: Private smooth-suspension AC vehicle for all transfers.", 2),
            _inc_included("Curated Meal Plan: Daily mild, customized breakfasts and dinners (MAPAI).", 3),
            _inc_included("TRAGUIN Support: 24/7 high-priority guest care and medical coordination support.", 4),
            _inc_included("Welcome Amenities: Specialized travel kits, wet wipes, and healthy refreshments.", 5),
            _inc_included("Complimentary Experience: Private golf-cart ride at ancient heritage landmarks.", 6),
            _inc_excluded("Airfare, flight tickets, or cross-state main train bookings.", 7),
            _inc_excluded("Individual monument ticket entry and specialized camera charges.", 8),
            _inc_excluded("Personal expenses like laundry, optional international calls, or tips.", 9),
            _inc_excluded("Any insurance premiums or medical expenses incurred.", 10),
        ],
    )
    return package, itinerary


def build_br_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "BR-006"
    tour_code = "TRG-BIH-006"
    title = (
        "TRAGUIN Premium Bihar Tour Package — Ancient Bihar • "
        "The Cradle of Empires & Enlightenment: Patna • Nalanda • Rajgir • Bodhgaya • Vaishali"
    )
    duration = "05 Nights / 06 Days"
    slug = "br-006-ancient-bihar-heritage-culture-patna-vaishali-nalanda-rajgir-bodhgaya"
    itin_slug = "br-006-ancient-bihar-heritage-culture-patna-vaishali-nalanda-rajgir-bodhgaya-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Bihar / India | Category: Premium Heritage & Culture", 2),
            _ph("Destinations: Patna • Nalanda • Rajgir • Bodhgaya • Vaishali", 3),
            _ph("Ideal for: Family Heritage Tours, Spiritual Seekers & History Connoisseurs", 4),
            _ph("Best season: October to March (Pleasant & Spiritual Festivals)", 5),
            _ph("Starting price: On Request (Premium Bespoke Package)", 6),
            _ph("Vehicle / Meals: Luxury Chauffeur-Driven MUV (Innova Crysta) / MAPAI Plan", 7),
            _ph("Route Plan: Patna (2N) ➔ Vaishali ➔ Nalanda ➔ Rajgir (1N) ➔ Bodhgaya (2N) ➔ Departure", 8),
            _ph("TRAGUIN Signature Experience: Private guided interactive walk with an acclaimed local archeological expert at Nalanda Ruins.", 9),
            _ph("Curated by TRAGUIN Experts: Seamlessly structured routing avoiding peak-hour highway bottlenecks, optimizing leisure hours.", 10),
            _ph("Exclusive Recommendations: VIP seating coordination during evening spiritual temple assemblies and special historic walks.", 11),
            _ph("Shopping & Local Experiences: Madhubani hand-paintings, Bhagalpuri Tussar Silk, Sikki grass basketry, stone carvings; Tilkut, Khaja, Litti Chokha.", 12),
            _ph("Important Notes: Check-in 14:00 / check-out 11:00; valid government ID required; book 30–45 days ahead.", 13),
        ],
        moods=["Family", "Cultural", "History", "Spiritual", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note="On Request (Premium Bespoke Package)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Ancient Bihar Heritage & Culture • Patna • Vaishali • Nalanda • Rajgir • Bodhgaya • 05 Nights / 06 Days",
        overview=(
            "Welcome to a deeply spiritual and historic exploration curated exclusively by TRAGUIN. Embark on the "
            "finest Bihar Family Tour, masterfully designed to unfold the breathtaking landscapes, ancient universities, "
            "and hallowed spiritual grounds of this timeless land.\n\n"
            "TOUR OVERVIEW\n"
            "This custom-tailored luxury holiday package presents an unparalleled immersion into the profound historic "
            "roots of Buddhism, Jainism, and ancient Indian empires. Travelling in absolute opulence within a dedicated "
            "premium AC vehicle driven by a highly professional, background-verified chauffeur, your family will experience "
            "flawless connectivity across cities. Savor a meticulously curated meal plan featuring lavish morning spreads "
            "and specialized regional dinners. Every segment of your route incorporates the exclusive TRAGUIN curated "
            "experience note, ensuring private local guides, seamless check-ins, and bespoke personalized support.\n\n"
            "WHY CHOOSE THE BEST BIHAR TOUR PACKAGE?\n"
            "When planning a Luxury Bihar Holiday, travelers seek more than an average vacation; they desire an "
            "enlightening connection with history and soul-stirring cultural depth. Bihar is the birthplace of ancient "
            "spiritual paths and magnificent dynasties, from the UNESCO World Heritage Site of Bodhgaya to the majestic "
            "cyclopean walls of Rajgir."
        ),
        seo_title="BR-006 | Ancient Bihar Heritage Culture Vaishali Nalanda | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days heritage tour (BR-006 / TRG-BIH-006): Patna, Vaishali, Nalanda, "
            "Rajgir, Bodhgaya, and 4-tier handpicked accommodation."
        ),
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Patna arrival, Golghar, Patna Museum, Takht Sri Patna Sahib on Day 01", 1),
            _ih("Vaishali Ashokan Pillar and stupas excursion on Day 02", 2),
            _ih("Nalanda University ruins and Rajgir ropeway on Day 03", 3),
            _ih("Rajgir to Bodhgaya, Mahabodhi Temple on Day 04", 4),
            _ih("International monasteries and Sujata Kuti on Day 05", 5),
            _ih("Bodhgaya to Patna departure on Day 06", 6),
        ],
        days=[
            _day(1, "ARRIVAL IN PATNA | WELCOME TO ANCIENT PATALIPUTRA – EMPIRE LEGACIES", (
                "Your premium Bihar experience initiates upon arrival at Patna Airport or Railway Station, where a premium "
                "private vehicle awaits your family. Transfer smoothly to your handpicked premium luxury hotel. In the "
                "afternoon, set out to explore the historic capital. Visit the massive granary of Golghar, offering scenic beauty "
                "and a sweeping view of the Ganges river, followed by the modern landmark of Patna Museum, showcasing "
                "pristine Mauryan sculptures."
            ), [
                "Sightseeing Included: Golghar, Patna Museum, Takht Sri Patna Sahib Gurudwara (Birthplace of Guru Gobind Singh Ji).",
                "Evening Experience: Bespoke heritage briefing and welcome gourmet dinner curated by TRAGUIN experts.",
                "Overnight Stay: Patna (Premium Executive Hotel).",
                "Meals Included: Welcome Mocktail & Gourmet Dinner.",
            ]),
            _day(2, "PATNA TO VAISHALI EXCURSION | THE WORLD'S FIRST REPUBLIC & FAREWELL SACRED SERMONS", (
                "Savor a lavish breakfast before heading north across the mighty Ganges to Vaishali, an iconic attraction "
                "deeply sacred to both Buddhists and Jains. Vaishali is revered as the world's first democratic republic. Walk "
                "through the breathtaking landscapes hosting the Ashokan Pillar, topped by a magnificent single-piece lion "
                "capital, and visit the Relic Stupa where the sacred ashes of Lord Buddha were enshrined. Photograph the "
                "pristine peace pagoda before driving back to Patna."
            ), [
                "Sightseeing Included: Ashokan Pillar, Ananda Stupa, Abhishek Pushkarini (Sacred Coronation Tank), Shanti Stupa.",
                "Optional Activities: Private pottery demonstration or interactive session with traditional local Madhubani artisans.",
                "Overnight Stay: Patna (Premium Executive Hotel).",
                "Meals Included: Premium Breakfast & Crafted Dinner.",
            ]),
            _day(3, "PATNA TO NALANDA & RAJGIR | THE SEAT OF GLOBAL KNOWLEDGE & ROYAL VALLEY FORTRESSES", (
                "Depart early along scenic country routes towards the magnificent archeological ruins of Nalanda University, "
                "the global seat of learning from the 5th century. Accompanied by an expert historian, explore the vast brick "
                "monastic cells, ancient temples, and the Nalanda Archaeological Museum. In the afternoon, proceed to Rajgir, "
                "surrounded by five majestic hills. Experience the exciting aerial ropeway to the spectacular Vishwa Shanti "
                "Stupa located on Ratnagiri Hill."
            ), [
                "Sightseeing Included: Nalanda University Ruins, Hiuen Tsang Memorial Hall, Rajgir Ropeway, Gridhakuta Peak (Vulture's Peak).",
                "Evening Experience: A walk across the ultra-modern Rajgir Glass Skywalk for panoramic sunset mountain views.",
                "Overnight Stay: Rajgir (Premium / Selected Luxury Resort).",
                "Meals Included: Premium Breakfast & Regional Buffet Dinner.",
            ]),
            _day(4, "RAJGIR TO BODHGAYA | JOURNEY TO THE LAND OF ENLIGHTENMENT", (
                "Explore the historical wonders of Rajgir in the morning, including the ancient Cyclopean Wall and the unique "
                "Son Bhandar Caves. Afterward, board your luxury vehicle for a pleasant drive to Bodhgaya, the ultimate "
                "spiritual epicenter of the Buddhist world. Check into your premium resort. As twilight descends, enjoy an "
                "emotionally moving walk through the sacred Mahabodhi Temple complex, absorbing the serene chants and "
                "meditative energy of pilgrims from across the globe."
            ), [
                "Sightseeing Included: Cyclopean Wall, Son Bhandar, Mahabodhi Temple introductory tour, Great Buddha Statue.",
                "Evening Experience: Private meditation session arranged near the sacred Bodhi Tree under expert guidance.",
                "Overnight Stay: Bodhgaya (Bespoke Luxury Resort Stay).",
                "Meals Included: Breakfast & Lavish Resort Dinner.",
            ]),
            _day(5, "IMMERSIVE BODHGAYA EXCURSION | GLOBAL MONASTERIES & TRANQUIL REFLECTIONS", (
                "Dedicate this day to exploring the architectural brilliance and cultural diversity of international monasteries in "
                "Bodhgaya. Visit the beautiful Thai Monastery, the intricate Japanese Temple, and the vibrant Bhutanese "
                "Monastery, each highlighting unique artistic heritages. In the afternoon, visit Sujata Kuti across the Niranjana "
                "River, where the historic milk-rice offering was presented to Lord Buddha prior to his enlightenment."
            ), [
                "Sightseeing Included: Thai, Japanese, Bhutanese Monasteries, Sujata Kuti, Niranjana River bank trails.",
                "Optional Activities: Exclusive photography walk highlighting the detailed ancient rock-carving art forms.",
                "Overnight Stay: Bodhgaya (Bespoke Luxury Resort Stay).",
                "Meals Included: Premium Breakfast & Elegant Farewell Dinner.",
            ]),
            _day(6, "BODHGAYA TO PATNA / DEPARTURE | CHERISHING THE SPIRIT OF ENLIGHTENMENT", (
                "Indulge in a final lavish breakfast at your luxury resort. Your private premium transport will guide you safely "
                "back along the smooth highway to Patna Airport or Gaya Airport for your onward journey. Return home "
                "carrying a heart filled with spiritual peace and unforgettable memories meticulously custom-crafted by TRAGUIN."
            ), [
                "Transfers Included: Private door-to-door luxury airport or railway drop-off.",
                "Meals Included: Sumptuous Buffet Breakfast.",
            ]),
        ],
        hotels=[
            _hotel("Hotel Maurya / Lemon Tree Premier | Hotel Gargee Gautam Vihar / similar | The Royal Residency / similar", "Patna (2 Nights) / Rajgir (1 Night) / Bodhgaya (2 Nights)", "05 Nights", "Deluxe", "Deluxe Room", "MAPAI (Breakfast & Dinner)", 4, 1, description="OPTION 01 – DELUXE: Hotel Maurya / Lemon Tree Premier (Patna, 2 Nights) | Hotel Gargee Gautam Vihar / similar (Rajgir, 1 Night) | The Royal Residency / similar (Bodhgaya, 2 Nights) | MAPAI"),
            _hotel("Hotel Chanakya / Panache Patna | Rajgir Residency / Elite Stay | Maha Bodhi Hotel & Resort", "Patna (2 Nights) / Rajgir (1 Night) / Bodhgaya (2 Nights)", "05 Nights", "Premium", "Premium Room", "MAPAI (Breakfast & Dinner)", 4, 2, description="OPTION 02 – PREMIUM: Hotel Chanakya / Panache Patna (Patna, 2 Nights) | Rajgir Residency / Elite Stay (Rajgir, 1 Night) | Maha Bodhi Hotel & Resort (Bodhgaya, 2 Nights) | MAPAI"),
            _hotel("Taj City Centre Patna (Superior Room) | The Indo Hokke Hotel (Premium Heritage) | Marasa Sarovar Premiere Bodhgaya", "Patna (2 Nights) / Rajgir (1 Night) / Bodhgaya (2 Nights)", "05 Nights", "Luxury", "Luxury Room", "MAPAI (Breakfast & Dinner)", 5, 3, description="OPTION 03 – LUXURY: Taj City Centre Patna Superior Room (Patna, 2 Nights) | The Indo Hokke Hotel Premium Heritage (Rajgir, 1 Night) | Marasa Sarovar Premiere Bodhgaya (Bodhgaya, 2 Nights) | MAPAI"),
            _hotel("Taj City Centre Patna (Luxury Executive Suite) | VVIP Custom Heritage Private Villa | The Bodhi Palace Resort / Hyatt Regency style premium setup", "Patna (2 Nights) / Rajgir (1 Night) / Bodhgaya (2 Nights)", "05 Nights", "Ultra Luxury", "Luxury Suite / Villa", "MAPAI (Breakfast & Dinner)", 5, 4, description="OPTION 04 – ULTRA LUXURY: Taj City Centre Patna Luxury Executive Suite (Patna, 2 Nights) | VVIP Custom Heritage Private Villa (Rajgir, 1 Night) | The Bodhi Palace Resort / Hyatt Regency style premium setup (Bodhgaya, 2 Nights) | MAPAI"),
        ],
        inclusions=[
            _inc_included("Premium Stays: Luxury accommodations as per selected option.", 1),
            _inc_included("Luxury Transportation: Private air-conditioned Innova Crysta throughout.", 2),
            _inc_included("Curated Meal Plan: Daily premium breakfast and gourmet multi-cuisine dinners.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated local guest relationship manager.", 4),
            _inc_included("Welcome Amenities: Personalized welcome kit, mineral water, and premium snacks.", 5),
            _inc_included("Complimentary Experience: Reserved aerial ropeway and skywalk tickets in Rajgir.", 6),
            _inc_excluded("Airfare or main railway ticket pricing to/from Patna.", 7),
            _inc_excluded("Monument entry fees, camera permits, and personal local guide fees.", 8),
            _inc_excluded("Personal expenses such as laundry, phone calls, premium beverages, and tips.", 9),
            _inc_excluded("Any optional adventure, extended tours, or individual activity charges.", 10),
        ],
    )
    return package, itinerary


def build_br_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "BR-007"
    tour_code = "TRG-BIH-007"
    title = (
        "TRAGUIN Premium Bihar Tour Package — Educational Bihar • "
        "Footsteps of Scholars & Emperors: Patna • Nalanda • Rajgir • Bodhgaya"
    )
    duration = "04 Nights / 05 Days"
    slug = "br-007-educational-bihar-patna-nalanda-rajgir-bodhgaya"
    itin_slug = "br-007-educational-bihar-patna-nalanda-rajgir-bodhgaya-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Bihar / India | Category: School Educational Tour", 2),
            _ph("Destinations: Patna • Nalanda • Rajgir • Bodhgaya", 3),
            _ph("Ideal for: Students, Academic Batches & Institutions", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Institutional Special Group Pricing)", 6),
            _ph("Vehicle / Meals: Luxury AC Coaches / API (All Meals Included)", 7),
            _ph("Route Plan: Patna (1N) ➔ Nalanda ➔ Rajgir (1N) ➔ Bodhgaya (2N) ➔ Patna Departure", 8),
            _ph("TRAGUIN Signature Experience: Private archaeology workshops led by local research professors at Nalanda.", 9),
            _ph("Curated by TRAGUIN Experts: Safe, seamless itineraries balancing educational value with comfortable breaks.", 10),
            _ph("Personalized Assistance: Dedicated group trackers, certified student escorts, and 1 complimentary teacher slot per 15 students.", 11),
            _ph("Shopping & Local Experiences: Madhubani art, stone sculptures, bamboo craftwork, handloom textiles; Khaja and Tilkut.", 12),
            _ph("Important Notes: Institutional authorization required; book 45–60 days ahead; light pullovers and walking shoes recommended.", 13),
        ],
        moods=["Cultural", "History", "Family"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note="On Request (Institutional Special Group Pricing)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Educational Bihar • Patna • Nalanda • Rajgir • Bodhgaya • 04 Nights / 05 Days",
        overview=(
            "Welcome to an enriching historical journey curated exclusively by TRAGUIN. Embark on a premium Bihar "
            "Educational Tour specifically designed to immerse student cohorts into the breathtaking landscapes, "
            "glorious empires, and legendary seats of ancient knowledge.\n\n"
            "TOUR OVERVIEW\n"
            "This elite institutional field trip represents the ultimate premium Bihar experience for modern school groups. "
            "Travelling in a dedicated fleet of luxury AC multi-axle coaches accompanied by senior TRAGUIN tour "
            "managers, local historians, and certified medical assistance, safety is paired seamlessly with exploration. "
            "Featuring an all-inclusive buffet meal plan tailored for healthy, student-friendly dining, this route flows past "
            "iconic attractions effortlessly. Every student and educator will enjoy specialized TRAGUIN curated "
            "experiences including VIP monument entry, interactive group quizzes, and immersive storytelling workshops "
            "that transcend the boundaries of classroom textbooks.\n\n"
            "WHY CHOOSE THE BEST BIHAR TOUR PACKAGE FOR STUDENTS?\n"
            "When shortlisting a Luxury Bihar Holiday or student learning journey, educational institutions choose a path "
            "rich in ancient history, socio-political legacy, and cultural heritage. Bihar remains the cradle of ancient Indian "
            "civilization, from the ruins of the world-famous Nalanda University to the historic Cyclopean Walls of Rajgir."
        ),
        seo_title="BR-007 | Educational Bihar School Tour Patna Nalanda | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days school educational tour (BR-007 / TRG-BIH-007): Patna, Nalanda, "
            "Rajgir, Bodhgaya, API meals, and 4-tier accommodation."
        ),
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Patna arrival, Bihar Museum, Golghar orientation on Day 01", 1),
            _ih("Nalanda University ruins and transfer to Rajgir on Day 02", 2),
            _ih("Rajgir ropeway, Cyclopean Walls, Bodhgaya on Day 03", 3),
            _ih("Mahabodhi Temple, international monasteries on Day 04", 4),
            _ih("Bodhgaya to Patna departure on Day 05", 5),
        ],
        days=[
            _day(1, "ARRIVAL IN PATNA | LEGACY OF PATALIPUTRA – EXPLORING THE SEAT OF EMPIRES", (
                "Your educational premium Bihar experience begins as your student group lands at Patna Airport or arrives at "
                "the railway station, greeted warmly by the dedicated TRAGUIN logistics team. Board your luxury AC coach "
                "and transfer to your handpicked premium stay. After lunch, visit the futuristic Bihar Museum, a world-class "
                "architectural masterpiece holding treasures from the Maurya and Gupta eras. Next, explore the Golghar to "
                "understand historical grain storage systems and capture stunning photography points overlooking the holy Ganges."
            ), [
                "Sightseeing Included: Bihar Museum interactive galleries, Golghar, Gandhi Maidan promenade.",
                "Evening Experience: An orientation seminar and ice-breaking educational briefing conducted by TRAGUIN experts.",
                "Overnight Stay: Patna (Premium Business Hotel).",
                "Meals Included: Welcome Drink, Student Buffet Lunch & Dinner.",
            ]),
            _day(2, "PATNA TO NALANDA & RAJGIR | ANCIENT KNOWLEDGE & THE GLORY OF THE FIRST UNIVERSITY", (
                "Depart early after a nutritious buffet breakfast towards Nalanda, a UNESCO World Heritage site and an "
                "essential anchor for any top-tier school excursion. Here, students will experience immersive storytelling while "
                "touring the extensive brick ruins of the 5th-century Nalanda University. Walk past ancient classrooms, "
                "monasteries, and grand libraries. Visit the Multimedia Nalanda Museum before continuing the drive through "
                "breathtaking landscapes to Rajgir, the ancient capital of Magadha."
            ), [
                "Sightseeing Included: Nalanda University Archaeological Ruins, Xuanzang Memorial Hall, Nalanda Museum.",
                "Optional Activities: Inter-school interactive debate session on ancient versus modern education patterns.",
                "Overnight Stay: Rajgir (Premium Eco-Resort / Hotel).",
                "Meals Included: Full Board (Breakfast, Lunch & Dinner).",
            ]),
            _day(3, "RAJGIR EXPLORATION TO BODHGAYA | ROYAL FORTRESSES, ROPEWAYS & SPIRITUAL GEOGRAPHY", (
                "Embark on an exhilarating day exploring Rajgir's famous attractions. Ride the scenic aerial ropeway to the top "
                "of Ratnagiri Hill to witness the gleaming white Vishwa Shanti Stupa (Peace Pagoda). Explore the ancient "
                "Cyclopean Walls, Venu Vana, and Bimbisara Jail, offering real-world historical context to textbook chapters on "
                "Buddhism and Jainism. In the afternoon, take a picturesque drive to Bodhgaya, checking into a highly secure "
                "premium hotel."
            ), [
                "Sightseeing Included: Vishwa Shanti Stupa Ropeway, Gridhakuta Hill, Cyclopean Wall segments, Venu Vana.",
                "Evening Experience: Peaceful group meditation walk around the outer ring of spiritual monuments.",
                "Overnight Stay: Bodhgaya (Premium Handpicked Hotel).",
                "Meals Included: Full Board (Breakfast, Institutional Lunch & Dinner).",
            ]),
            _day(4, "BODHGAYA ENLIGHTENMENT TOUR | WORLD HERITAGE IMMERSION & GLOBAL ARCHITECTURE STUDY", (
                "Spend a magnificent day exploring Bodhgaya, the world's ultimate center for Buddhist learning. Visit the "
                "magnificent UNESCO World Heritage Mahabodhi Temple, standing beside the sacred Bodhi Tree where "
                "Prince Siddhartha attained supreme enlightenment. Students will learn about ancient stone carvings and "
                "global religious history. Later, visit the diverse international monasteries including the Japanese, Thai, and "
                "Tibetan temples to observe varied architectural styles."
            ), [
                "Sightseeing Included: Mahabodhi Temple, Sacred Bodhi Tree, Great Buddha Statue, Royal Thai Monastery.",
                "Optional Activities: Live workshop with local artists focused on practicing authentic Madhubani painting.",
                "Overnight Stay: Bodhgaya (Premium Handpicked Hotel).",
                "Meals Included: Full Board (Breakfast, Lunch & Special Farewell Dinner).",
            ]),
            _day(5, "BODHGAYA TO PATNA / DEPARTURE | CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS", (
                "Indulge in a final hearty breakfast at your premium hotel before boarding your luxury coach. Enjoy a relaxed "
                "drive back to Patna. Your coach will deliver the group directly to Patna Airport or Patna Junction Railway "
                "Station for your departure. Return home with expanded minds, rich academic journals, and unforgettable "
                "memories shaped beautifully by TRAGUIN."
            ), [
                "Transfers Included: Private luxury group drop-off with luggage assistance.",
                "Meals Included: Sumptuous Buffet Breakfast & Packed Highway Lunch.",
            ]),
        ],
        hotels=[
            _hotel("Hotel Maurya Central / similar | Hotel Rajgir Residency / similar | Hotel Bodhgaya Regency / similar", "Patna (1 Night) / Rajgir (1 Night) / Bodhgaya (2 Nights)", "04 Nights", "Deluxe", "Deluxe Room", "API (All Meals Included)", 4, 1, description="OPTION 01 – DELUXE: Hotel Maurya Central / similar (Patna, 1 Night) | Hotel Rajgir Residency / similar (Rajgir, 1 Night) | Hotel Bodhgaya Regency / similar (Bodhgaya, 2 Nights) | API (All Meals Included)"),
            _hotel("Lemon Tree Premier Patna | The Gargee Gautam Vihar | The Lotus Nikko / similar", "Patna (1 Night) / Rajgir (1 Night) / Bodhgaya (2 Nights)", "04 Nights", "Premium", "Premium Room", "API (All Meals Included)", 4, 2, description="OPTION 02 – PREMIUM: Lemon Tree Premier Patna (Patna, 1 Night) | The Gargee Gautam Vihar (Rajgir, 1 Night) | The Lotus Nikko / similar (Bodhgaya, 2 Nights) | API (All Meals Included)"),
            _hotel("Hotel Chanakya Luxury Suites | Indo Hokke Hotel Luxury Wings | The Mahabodhi Hotel & Resort", "Patna (1 Night) / Rajgir (1 Night) / Bodhgaya (2 Nights)", "04 Nights", "Luxury", "Luxury Room", "API (All Meals Included)", 5, 3, description="OPTION 03 – LUXURY: Hotel Chanakya Luxury Suites (Patna, 1 Night) | Indo Hokke Hotel Luxury Wings (Rajgir, 1 Night) | The Mahabodhi Hotel & Resort (Bodhgaya, 2 Nights) | API (All Meals Included)"),
            _hotel("Taj City Centre Patna (Premium) | VVIP Custom Luxury Heritage Block | Marasa Sarovar Premiere Bodhgaya", "Patna (1 Night) / Rajgir (1 Night) / Bodhgaya (2 Nights)", "04 Nights", "Ultra Luxury", "Luxury Suite / Villa", "API (All Meals Included)", 5, 4, description="OPTION 04 – ULTRA LUXURY: Taj City Centre Patna Premium (Patna, 1 Night) | VVIP Custom Luxury Heritage Block (Rajgir, 1 Night) | Marasa Sarovar Premiere Bodhgaya (Bodhgaya, 2 Nights) | API (All Meals Included)"),
        ],
        inclusions=[
            _inc_included("Premium Stays: Triple/Quad sharing student setups in handpicked safe hotels.", 1),
            _inc_included("Luxury Transportation: High-end AC Coaches with reliable, certified commercial drivers.", 2),
            _inc_included("All-Inclusive Meal Plan: Daily nutritious breakfast, lunch, and dinner buffet (API).", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated tour managers and on-board operations executive.", 4),
            _inc_included("Complimentary Access: All pre-booked entry tickets to monuments and Rajgir ropeway passes.", 5),
            _inc_included("Welcome Kit: Educational journals, student badges, hats, and maps for everyone.", 6),
            _inc_excluded("Flights or train fares from your home institutional location.", 7),
            _inc_excluded("Personal student purchases, laundry, and individual room service bills.", 8),
            _inc_excluded("Any medical tests, specific customized health care, or individual insurance.", 9),
            _inc_excluded("Optional specialized historic workshops not mentioned in the main track.", 10),
        ],
    )
    return package, itinerary


def build_br_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "BR-008"
    tour_code = "TRG-BIH-008"
    title = (
        "TRAGUIN Premium Bihar Tour Package — Bihar Explorer • "
        "An Epic Voyage Through Eternity: Patna • Rajgir • Nalanda • Bodhgaya"
    )
    duration = "05 Nights / 06 Days"
    slug = "br-008-bihar-explorer-family-patna-rajgir-nalanda-bodhgaya"
    itin_slug = "br-008-bihar-explorer-family-patna-rajgir-nalanda-bodhgaya-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Bihar / India | Category: Premium Family Tour", 2),
            _ph("Destinations: Patna • Rajgir • Nalanda • Bodhgaya", 3),
            _ph("Ideal for: Family Getaways, Cultural Explorers & Luxury Travelers", 4),
            _ph("Best season: October to March (Pleasant Autumn / Winter)", 5),
            _ph("Starting price: On Request (Bespoke Luxury Customization)", 6),
            _ph("Vehicle / Meals: Private Luxury Innova Crysta / MAPAI (Breakfast & Dinner)", 7),
            _ph("Route Plan: Patna (1N) ➔ Rajgir (2N) ➔ Nalanda Excursion ➔ Bodhgaya (2N) ➔ Departure", 8),
            _ph("TRAGUIN Signature Experience: Private family interaction with a certified spiritual history scholar in Bodhgaya.", 9),
            _ph("Curated by TRAGUIN Experts: Smooth routing to bypass highway traffic, prioritizing family relaxation and comfort.", 10),
            _ph("Exclusive Recommendations: Priority access passes to the Rajgir Glass Skywalk to minimize waiting time.", 11),
            _ph("Shopping & Local Experiences: Madhubani artworks, Bhagalpuri Tussar silk, stone Buddha replicas; Tilkut, Anarsa, Litti Chokha.", 12),
            _ph("Important Notes: Book 30–45 days ahead; check-in 14:00 / check-out 11:00; river cruise subject to seasonal conditions.", 13),
        ],
        moods=["Family", "Cultural", "Luxury", "History"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note="On Request (Bespoke Luxury Customization)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Bihar Explorer Family Tour • Patna • Rajgir • Nalanda • Bodhgaya • 05 Nights / 06 Days",
        overview=(
            "Welcome to an extraordinary exploration curated exclusively by TRAGUIN. Embark on the definitive Bihar "
            "Family Tour designed to reveal the roots of civilization, spiritual enlightenment, and royal legends.\n\n"
            "TOUR OVERVIEW\n"
            "This meticulously customized premium luxury travel itinerary blends comfort and legacy for families seeking "
            "an immersive vacation. Travel seamlessly across ancient empires in an exclusive chauffeur-driven luxury "
            "vehicle under a comprehensive meal plan featuring exquisite regional and international cuisines. From private "
            "boat cruises at sunset on the Ganges to exploring ancient monolithic ruins with elite historians, every detail is "
            "elevated by the trademark TRAGUIN curated experience note, ensuring comfort, priority access, and "
            "seamless travel logistics.\n\n"
            "WHY CHOOSE THE BEST BIHAR TOUR PACKAGE?\n"
            "When planning a Luxury Bihar Holiday, travelers look for deep cultural heritage balanced with modern "
            "hospitality. Bihar stands as a land of transformation, boasting some of the most globally iconic attractions, "
            "from the ruins of Nalanda University to the sacred Mahabodhi Temple complex in Bodhgaya."
        ),
        seo_title="BR-008 | Bihar Explorer Family Patna Rajgir Nalanda Bodhgaya | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days Bihar family explorer (BR-008 / TRG-BIH-008): Patna, Rajgir, "
            "Nalanda, Bodhgaya, and 4-tier handpicked accommodation."
        ),
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Patna arrival, Golghar, Patna Museum, private Ganga cruise on Day 01", 1),
            _ih("Patna to Rajgir, ropeway, Glass Skywalk on Day 02", 2),
            _ih("Nalanda University excursion from Rajgir on Day 03", 3),
            _ih("Rajgir to Bodhgaya, Mahabodhi Temple on Day 04", 4),
            _ih("International monasteries tour on Day 05", 5),
            _ih("Bodhgaya or Patna departure on Day 06", 6),
        ],
        days=[
            _day(1, "ARRIVAL IN PATNA | WELCOME TO ANCIENT PATALIPUTRA – RIVERSIDE OPULENCE", (
                "Your premium Bihar experience begins as you arrive at Patna Airport/Railway Station, where a private luxury "
                "transport vehicle waits to welcome you. Transfer to your handpicked premium luxury hotel for a smooth check-in. "
                "In the afternoon, embark on an insightful city tour visiting Patna Museum's rare artifacts and the spectacular "
                "ancient granary of Golghar. In the evening, enjoy a private sunset boat cruise over the holy River Ganges "
                "arranged exclusively by TRAGUIN experts."
            ), [
                "Sightseeing Included: Golghar, Patna Museum, Takht Sri Patna Sahib, Private Ganga Cruise.",
                "Evening Experience: Ganga Aarti viewing from a reserved private deck with local refreshments.",
                "Overnight Stay: Patna (Premium / Luxury Selected Hotel).",
                "Meals Included: Welcome Drink & Luxury Welcome Dinner.",
            ]),
            _day(2, "PATNA TO RAJGIR | THE ROYAL SEAT OF KINGS – ARCHAEOLOGY & THRILLS", (
                "After a lavish breakfast, drive towards Rajgir, a valley surrounded by five green hills showcasing breathtaking "
                "landscapes. Check into your luxury resort and prepare for an exceptional afternoon. Take the aerial ropeway "
                "up to the Vishwa Shanti Stupa (Peace Pagoda) for panoramic views. Visit the ancient Cyclopean Walls, the "
                "Bimbisara Jail, and experience the thrilling Rajgir Glass Skywalk—a popular Instagram location offering "
                "spectacular forest views below."
            ), [
                "Sightseeing Included: Vishwa Shanti Stupa, Venu Vana, Griddhakuta (Vulture's Peak), Rajgir Glass Skywalk.",
                "Optional Activities: A relaxing dip in the sacred Brahmakund natural hot water springs.",
                "Overnight Stay: Rajgir (Handpicked Premium Eco-Luxury Resort).",
                "Meals Included: Premium Breakfast & Authentic Fine Dinner.",
            ]),
            _day(3, "RAJGIR TO NALANDA EXCURSION | THE UNIVERSAL SEAT OF KNOWLEDGE – HERITAGE EMBARKATION", (
                "Today, delve deep into ancient history with an excursion to Nalanda, a UNESCO World Heritage Site. Walk "
                "through the sprawling brick ruins of Nalanda University, which dates back to the 5th century. A specialized "
                "heritage storyteller will bring the ancient libraries, monasteries, and lecture halls to life. Later, visit the Nalanda "
                "Archaeological Museum and the Xuanzang Memorial Hall before returning to Rajgir for a premium evening "
                "spa treatment."
            ), [
                "Sightseeing Included: Nalanda University Ruins, Archaeological Museum, Xuanzang Memorial Hall.",
                "Evening Experience: Traditional organic family dinner inside a private luxury cottage tent.",
                "Overnight Stay: Rajgir (Handpicked Premium Eco-Luxury Resort).",
                "Meals Included: Premium Breakfast & Specialized Dinner.",
            ]),
            _day(4, "RAJGIR TO BODHGAYA | JOURNEY TO ENLIGHTENMENT – QUIETUDE & SPIRITUAL GRACE", (
                "Following a delicious breakfast, travel through scenic countryside roads towards Bodhgaya, the most sacred "
                "place in the Buddhist world. Check into your ultra-luxury sanctuary hotel. Spend your afternoon on a calm, "
                "spiritually moving walking tour of the Mahabodhi Temple complex. Stand beneath the sacred Bodhi Tree, "
                "where Prince Siddhartha attained ultimate enlightenment to become Lord Buddha. The atmospheric evening "
                "chants provide an unforgettable immersive experience."
            ), [
                "Sightseeing Included: Mahabodhi Temple, Sacred Bodhi Tree, Animesh Lochan Chaitya, Muchalinda Lake.",
                "Evening Experience: Private guided meditation session with an ordained monk under the Bodhi tree.",
                "Overnight Stay: Bodhgaya (Bespoke Luxury Boutique Hotel).",
                "Meals Included: Premium Breakfast & Gourmet Dinner.",
            ]),
            _day(5, "BODHGAYA INTERNATIONAL MONASTERIES TOUR | GLOBAL ARCHITECTURAL SPLENDOUR & ARTISTIC SIGHTSEEING", (
                "Dedicate your day to exploring the diverse international monasteries of Bodhgaya. Visit the towering 80-foot "
                "Great Buddha Statue, followed by the Thai Monastery, the ornate Royal Bhutan Monastery, and the stunning "
                "Japanese Temple. Each site displays unique architecture and pristine, manicured gardens. In the afternoon, "
                "explore local artisan markets for premium stone carvings and handmade silk souvenirs."
            ), [
                "Sightseeing Included: Great Buddha Statue, Thai, Japanese, Bhutanese and Tibetan Monasteries, Sujata Kuti.",
                "Optional Activities: A private introductory lesson in authentic Buddhist philosophy and thangka painting.",
                "Overnight Stay: Bodhgaya (Bespoke Luxury Boutique Hotel).",
                "Meals Included: Premium Breakfast & Farewell Celebration Dinner.",
            ]),
            _day(6, "BODHGAYA / PATNA TO DEPARTURE | CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS", (
                "Enjoy a final luxury breakfast at your hotel. Depending on your flight choices, enjoy a smooth direct transfer to "
                "Gaya Airport or a scenic drive back to Patna Airport/Station. Return home carrying deep wisdom, refined "
                "family bonds, and unforgettable memories designed flawlessly by TRAGUIN."
            ), [
                "Transfers Included: Private luxury door-to-door station or airport drop-off.",
                "Meals Included: Sumptuous Buffet Breakfast.",
            ]),
        ],
        hotels=[
            _hotel("Hotel Maurya / similar | The Gargee Gautam Vihar / similar | Hotel Delta International / similar", "Patna (1 Night) / Rajgir (2 Nights) / Bodhgaya (2 Nights)", "05 Nights", "Deluxe", "Deluxe Room", "MAPAI (Breakfast & Dinner)", 4, 1, description="OPTION 01 – DELUXE: Hotel Maurya / similar (Patna, 1 Night) | The Gargee Gautam Vihar / similar (Rajgir, 2 Nights) | Hotel Delta International / similar (Bodhgaya, 2 Nights) | MAPAI (Breakfast & Dinner)"),
            _hotel("Lemon Tree Premier / similar | Rajgir Residency / similar | The Buddha Resort / similar", "Patna (1 Night) / Rajgir (2 Nights) / Bodhgaya (2 Nights)", "05 Nights", "Premium", "Premium Room", "MAPAI (Breakfast & Dinner)", 4, 2, description="OPTION 02 – PREMIUM: Lemon Tree Premier / similar (Patna, 1 Night) | Rajgir Residency / similar (Rajgir, 2 Nights) | The Buddha Resort / similar (Bodhgaya, 2 Nights) | MAPAI (Breakfast & Dinner)"),
            _hotel("Taj City Centre Patna | Indo Hokke Hotel / Premium Suite | Maha Bodhi Hotel & Resort", "Patna (1 Night) / Rajgir (2 Nights) / Bodhgaya (2 Nights)", "05 Nights", "Luxury", "Luxury Room", "MAPAI (Breakfast & Dinner)", 5, 3, description="OPTION 03 – LUXURY: Taj City Centre Patna (Patna, 1 Night) | Indo Hokke Hotel Premium Suite (Rajgir, 2 Nights) | Maha Bodhi Hotel & Resort (Bodhgaya, 2 Nights) | MAPAI (Breakfast & Dinner)"),
            _hotel("Taj City Centre (Executive Suite) | Bespoke Private Luxury Villa Resort | The Zen Resort / Hyatt Place Style Heritage", "Patna (1 Night) / Rajgir (2 Nights) / Bodhgaya (2 Nights)", "05 Nights", "Ultra Luxury", "Luxury Suite / Villa", "MAPAI (Breakfast & Dinner)", 5, 4, description="OPTION 04 – ULTRA LUXURY: Taj City Centre Executive Suite (Patna, 1 Night) | Bespoke Private Luxury Villa Resort (Rajgir, 2 Nights) | The Zen Resort / Hyatt Place Style Heritage (Bodhgaya, 2 Nights) | MAPAI (Breakfast & Dinner)"),
        ],
        inclusions=[
            _inc_included("Premium Stays: 5 Nights in handpicked hotels as per chosen category.", 1),
            _inc_included("Luxury Transportation: Private AC Innova Crysta for all transfers & sightseeing.", 2),
            _inc_included("Curated Meal Plan: Daily luxury breakfast and gourmet dinners (MAPAI).", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated guest experience manager on call.", 4),
            _inc_included("Welcome Amenities: Customized family travel kit and traditional welcome drinks.", 5),
            _inc_included("Complimentary Experience: Private sunset boat cruise tickets on the Ganges.", 6),
            _inc_excluded("Airfare or long-distance interstate train tickets.", 7),
            _inc_excluded("Monument entry tickets, camera permits, and local guide charges.", 8),
            _inc_excluded("Personal expenses such as laundry, phone calls, and tips.", 9),
            _inc_excluded("Any optional adventure activities or local shopping costs.", 10),
        ],
    )
    return package, itinerary


def build_br_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "BR-009"
    tour_code = "TRG-BIH-009"
    title = (
        "TRAGUIN Premium Bihar Tour Package — Jain Bihar Circuit • "
        "Path of Enlightenment & Pure Devotion: Patna • Pawapuri • Rajgir • Nalanda • Kundalpur • Vaishali"
    )
    duration = "05 Nights / 06 Days"
    slug = "br-009-jain-spiritual-circuit-patna-pawapuri-rajgir-vaishali"
    itin_slug = "br-009-jain-spiritual-circuit-patna-pawapuri-rajgir-vaishali-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Bihar / India | Category: Pilgrimage / Jain Spiritual Circuit", 2),
            _ph("Destinations: Patna • Pawapuri • Rajgir • Nalanda • Kundalpur • Vaishali", 3),
            _ph("Ideal for: Devotees, Spiritual Seekers & Jain Families", 4),
            _ph("Best season: October to March (Pleasant Winters)", 5),
            _ph("Starting price: On Request (Premium Customized)", 6),
            _ph("Vehicle / Meals: Private Luxury AC Vehicle / Custom Pure Vegetarian Plan", 7),
            _ph("Route Plan: Patna (3N) ➔ Pawapuri ➔ Rajgir (2N) ➔ Kundalpur & Nalanda ➔ Vaishali ➔ Patna Departure", 8),
            _ph("TRAGUIN Signature Experience: Private, pre-arranged priority temple entry to Pawapuri Jal Mandir with a dedicated priest escort.", 9),
            _ph("Curated by TRAGUIN Experts: Custom routing that optimizes travel times while aligning perfectly with traditional Jain fasting and dining schedules.", 10),
            _ph("Premium Handpicked Hotels: Accommodations rigorously vetted to ensure exemplary sanitation and absolute family-oriented comfort.", 11),
            _ph("Shopping & Local Experiences: Madhubani Paintings, Bhagalpuri Silk sarees, stone sculptures, bamboo craftwork; Khaja, sugarcane juice, Satvik snacks.", 12),
            _ph("Important Notes: Pure veg / Jain meal customization available; check-in 14:00 / check-out 11:00; book 45 days ahead for Rajgir peak season.", 13),
        ],
        moods=["Pilgrimage", "Spiritual", "Family", "Luxury", "Cultural"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note="On Request (Premium Customized)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Jain Bihar Spiritual Circuit • Patna • Pawapuri • Rajgir • Kundalpur • Vaishali • 05 Nights / 06 Days",
        overview=(
            "Welcome to a sacred, deeply transformative journey curated exclusively by TRAGUIN. Embark on the "
            "ultimate Bihar Pilgrimage Tour, meticulously structured to trace the divine footprints of Tirthankaras through "
            "the magnificent landscape of Bihar.\n\n"
            "TOUR OVERVIEW\n"
            "This custom-designed spiritual itinerary serves as the definitive premium Bihar experience for modern Jain "
            "families and devotees. Travelling in a completely private, premium air-conditioned vehicle with a professional "
            "chauffeur well-versed in local routes, your comfort remains paramount. Our carefully curated meal plan offers "
            "specialized, strictly pure vegetarian (and optional authentic Jain) meals prepared with the highest standards of "
            "hygiene and respect. Every step of this sacred passage includes the signature touch of TRAGUIN curated "
            "experiences, providing personalized assistance, VIP temple darshan coordination, and around-the-clock "
            "bespoke travel support.\n\n"
            "WHY CHOOSE THE BEST BIHAR TOUR PACKAGE?\n"
            "When planning a Luxury Bihar Holiday or a sacred family pilgrimage, discerning travelers seek an "
            "environment that honors both religious sensitivities and high-end lifestyle needs. Bihar stands as the historic "
            "cradle of Jainism, highlighting iconic attractions including the legendary Pawapuri Jal Mandir, Kundalpur, "
            "Vaishali, and the world-renowned ruins of Nalanda University."
        ),
        seo_title="BR-009 | Jain Spiritual Circuit Patna Pawapuri Rajgir Vaishali | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days Jain spiritual circuit (BR-009 / TRG-BIH-009): Pawapuri, Rajgir, "
            "Kundalpur, Vaishali, pure vegetarian meals, and 4-tier accommodation."
        ),
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Patna arrival, Kamaldah Jain Temple on Day 01", 1),
            _ih("Pawapuri Jal Mandir and transfer to Rajgir on Day 02", 2),
            _ih("Rajgir Jain hill shrines, ropeway, Son Bhandar on Day 03", 3),
            _ih("Kundalpur, Nalanda ruins, return to Patna on Day 04", 4),
            _ih("Vaishali Basokund Mahavira birthplace on Day 05", 5),
            _ih("Patna departure on Day 06", 6),
        ],
        days=[
            _day(1, "ARRIVAL IN PATNA | WELCOME TO ANCIENT PATALIPUTRA – LAND OF HOLY BEGINNINGS", (
                "Your premium Bihar experience begins the moment you arrive at Patna Airport or Railway Station. You will be "
                "greeted warmly by your dedicated private luxury transport coordinator and driven to your handpicked premium "
                "luxury hotel. After checking in and relaxing, enjoy a refined evening tour of Patna, visiting the Kamaldah Jain "
                "Temple, the oldest Jain monument in Patna belonging to the Digambara sect, housing the holy footsteps of "
                "Sthulabhadra Muni."
            ), [
                "Sightseeing Included: Kamaldah Jain Temple, ancient city orientation, overview of Ganga riverfront.",
                "Evening Experience: Bespoke orientation briefing and welcome dinner curated by TRAGUIN experts.",
                "Overnight Stay: Patna (Premium / Luxury Selected Hotel).",
                "Meals Included: Welcome Mocktail & Gourmet Pure Vegetarian Dinner.",
            ]),
            _day(2, "PATNA TO PAWAPURI & RAJGIR | THE NIRVANA BHUMI OF LORD MAHAVIRA – FLOATING MARBLE SANCTUARY", (
                "Depart early after a nutritious breakfast towards Pawapuri, a site of profound emotional and spiritual gravity. "
                "Arrive at the world-famous Jal Mandir, a breathtakingly beautiful white marble temple floating gracefully in the "
                "center of a huge water tank filled with pink lotuses, marking the exact spot of Lord Mahavira's Moksha. "
                "Experience quiet meditation inside the sanctum. Afterwards, visit the Gaon Mandir before driving to Rajgir to "
                "check into your scenic premium resort."
            ), [
                "Sightseeing Included: Pawapuri Jal Mandir, Gaon Mandir, Samosharan Temple complex.",
                "Optional Activities: Private interaction with local temple scholars for deep scriptural insights.",
                "Overnight Stay: Rajgir (Premium / Eco-Luxury Resort Stay).",
                "Meals Included: Premium Breakfast & Authentic Satvik Dinner.",
            ]),
            _day(3, "RAJGIR HOLY HILLS SIGHTSEEING | SACRED HILL PEAKS & SPIRITUAL VIBRATIONS OF THE TIRTHANKARAS", (
                "Dedicate your day to the magnificent scenic beauty and divine hills of Rajgir, heavily blessed by the frequent "
                "visits of Lord Mahavira. Take a romantic and thrilling aerial ropeway ride up to the Peace Pagoda (Vishwa "
                "Shanti Stupa). Devotees can comfortably ascend the sacred Vaibhavgiri or Vipulachal hills to explore "
                "beautifully preserved ancient Jain shrines. Later, capture timeless photography points at the ancient "
                "Cyclopean Walls and the legendary Son Bhandar Caves."
            ), [
                "Sightseeing Included: Vishwa Shanti Stupa, Aerial Ropeway, Son Bhandar Caves, Jain Hill Shrines.",
                "Evening Experience: Relaxing soak in the mineral-rich hot springs of Rajgir with private assistance.",
                "Overnight Stay: Rajgir (Premium / Eco-Luxury Resort Stay).",
                "Meals Included: Premium Breakfast & Specialized Jain Dinner.",
            ]),
            _day(4, "NALANDA, KUNDALPUR EXCURSION & RETURN TO PATNA | THE KNOWLEDGE SEED & BIRTHPLACE OF THE GAUDAMA GANADHARA", (
                "After a breakfast of traditional delights, proceed to Kundalpur, revered by many traditions as the holy "
                "birthplace of Gautam Swamiji, the chief disciple of Lord Mahavira. Tour the sprawling white complex "
                "containing 72 magnificent idols of Tirthankaras. Next, enjoy an immersive private tour of the UNESCO World "
                "Heritage ruins of Nalanda University, the pinnacle of global ancient education, followed by a visit to the nearby "
                "Nalanda Archaeological Museum. Return to Patna by evening."
            ), [
                "Sightseeing Included: Kundalpur Digambar Temple, Nalanda University Ruins, Xuanzang Memorial Hall.",
                "Evening Experience: Leisurely highway travel in luxury transport with refreshment stops.",
                "Overnight Stay: Patna (Premium / Luxury Selected Hotel).",
                "Meals Included: Premium Breakfast & Elegant Multi-cuisine Vegetarian Dinner.",
            ]),
            _day(5, "EXCURSION TO VAISHALI | THE BIRTHPLACE OF LORD MAHAVIRA – SACRED KUNDALPUR / BASOKUND", (
                "Today, drive across the majestic Mahatma Gandhi Setu over the Ganges to historic Vaishali, a pinnacle "
                "destination for your Bihar Pilgrimage Tour. Visit Basokund, widely celebrated as the exact birthplace of Lord "
                "Mahavira, the 24th Tirthankara. Experience deep reverence at the pristine Vishwa Shanti Stupa beside the "
                "coronation tank and see the legendary Ashokan Pillar. Return to Patna for your final evening of souvenir "
                "shopping."
            ), [
                "Sightseeing Included: Basokund Mahavira Birthplace, Ashokan Pillar, Abhishek Pushkarini (Coronation Tank).",
                "Optional Activities: Sunset photography near the banks of the historic ancient lake.",
                "Overnight Stay: Patna (Premium / Luxury Selected Hotel).",
                "Meals Included: Breakfast & Farewell Special Vegetarian Dinner.",
            ]),
            _day(6, "PATNA DEPARTURE | CHERISHING FAITH & UNFORGETTABLE MEMORIES", (
                "Savor a final peaceful breakfast at your luxury property. Your private luxury transport vehicle will be ready to "
                "escort you safely to Patna Airport or Patna Railway Station for your departure. Return home with your soul "
                "deeply enriched with spiritual peace, family bonds, and unforgettable memories custom-designed for you by "
                "TRAGUIN."
            ), [
                "Transfers Included: Private luxury station or airport departure drop-off.",
                "Meals Included: Sumptuous Buffet Breakfast.",
            ]),
        ],
        hotels=[
            _hotel("Hotel Maurya / Lemon Tree Premier | Hotel Gridhakuta International / similar", "Patna (3 Nights) / Rajgir (2 Nights)", "05 Nights", "Deluxe", "Deluxe Room", "Pure Veg MAPAI Plan", 4, 1, description="OPTION 01 – DELUXE: Hotel Maurya / Lemon Tree Premier (Patna, 3 Nights) | Hotel Gridhakuta International / similar (Rajgir, 2 Nights) | Pure Veg MAPAI Plan"),
            _hotel("Hotel Patliputra Exotica / similar | The Indo Hokke Hotel / similar", "Patna (3 Nights) / Rajgir (2 Nights)", "05 Nights", "Premium", "Premium Room", "Pure Veg MAPAI Plan", 4, 2, description="OPTION 02 – PREMIUM: Hotel Patliputra Exotica / similar (Patna, 3 Nights) | The Indo Hokke Hotel / similar (Rajgir, 2 Nights) | Pure Veg MAPAI Plan"),
            _hotel("Gargee Grand / Lemon Tree luxury club | Rajgir Residency Luxury Wing", "Patna (3 Nights) / Rajgir (2 Nights)", "05 Nights", "Luxury", "Luxury Room", "Custom Jain Strict Menu", 5, 3, description="OPTION 03 – LUXURY: Gargee Grand / Lemon Tree luxury club (Patna, 3 Nights) | Rajgir Residency Luxury Wing (Rajgir, 2 Nights) | Custom Jain Strict Menu"),
            _hotel("VVIP Selected Premium Executive Suite | Premium Private Villa Eco-Resort Wing", "Patna (3 Nights) / Rajgir (2 Nights)", "05 Nights", "Ultra Luxury", "Luxury Suite / Villa", "Elite Chef Curated Meals", 5, 4, description="OPTION 04 – ULTRA LUXURY: VVIP Selected Premium Executive Suite (Patna, 3 Nights) | Premium Private Villa Eco-Resort Wing (Rajgir, 2 Nights) | Elite Chef Curated Meals"),
        ],
        inclusions=[
            _inc_included("Premium Stays: 05 Nights accommodation in top-rated hospitality venues.", 1),
            _inc_included("Luxury Transportation: Private dedicated AC Innova / Sedan for seamless transit.", 2),
            _inc_included("Satvik Culinary Plan: Strictly pure vegetarian breakfast and gourmet dinners daily.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated guest relations officer on standby.", 4),
            _inc_included("Welcome Kit: Holy literature guide, dry fruit platter, and refreshing hand towels.", 5),
            _inc_included("Complimentary Experience: Reserved aerial ropeway passes for Vishwa Shanti Stupa.", 6),
            _inc_excluded("Airfare, flight tickets, or trans-state long-distance train tickets.", 7),
            _inc_excluded("Personal temple donation charges or specialized ritual material costs.", 8),
            _inc_excluded("Personal laundry, premium telephone calls, soft drinks, or tips.", 9),
            _inc_excluded("Any optional excursions or monument video camera operational permits.", 10),
        ],
    )
    return package, itinerary


BIHAR_DOMESTIC_BUILDERS = [
    build_br_001,
    build_br_002,
    build_br_003,
    build_br_004,
    build_br_005,
    build_br_006,
    build_br_007,
    build_br_008,
    build_br_009,
]
