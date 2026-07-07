"""Builder functions for GJ-001 through GJ-019 Gujarat domestic packages."""

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

GUJARAT_SLUG = "gujarat"
GUJARAT_DESTINATION_ID = "07be1b4e-0016-4caa-a680-c130ba86b9f7"


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




def build_gj_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "GJ-001"
    tour_code = "TRG-GJ-PILGRIMAGE-001"
    title = "Dwarka Somnath Pilgrimage"
    duration = "05 Nights / 06 Days"
    slug = "gj-001-dwarka-somnath-pilgrimage"
    itin_slug = "gj-001-dwarka-somnath-pilgrimage-itinerary"
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
            _ph("State / Country: Gujarat / India | Category: Pilgrimage / Luxury Holidays", 2),
            _ph("Destinations: Ahmedabad • Dwarka • Porbandar • Somnath", 3),
            _ph("Ideal for: Family Vacations • Devotional Groups • Senior Citizens", 4),
            _ph("Best season: October to March (Pleasant Weather)", 5),
            _ph("Starting price: On Request (Premium Handpicked Tariffs)", 6),
            _ph("Vehicle: Premium Private AC Sedan / SUV", 7),
            _ph("Meal Plan: MAPAI (Daily Premium Breakfast & Gourmet Dinner Included)", 8),
            _ph("Route Map: Ahmedabad → Dwarka (2N) → Porbandar → Somnath (2N) → Ahmedabad (1N)", 9),
            _ph(
                "TRAGUIN Signature Experience: Professionally vetted chauffeurs intimately familiar with local pilgrimage routes, curated by TRAGUIN Experts to minimize fatigue for elderly family members, premium handpicked hotels, and exclusive recommendations for authentic local vegetarian cuisine.",
                10,
            ),
            _ph(
                "Shopping: Dwarka temple street markets for brass idols and sea-shell ornaments; Porbandar and Somnath for Khadi items and sea-shell mirrors; Ahmedabad Law Garden Night Market for chaniya cholis, silver jewelry, and Gujarati snacks like Khakhra and Fafda.",
                11,
            ),
            _ph(
                "Important: Standard check-in 14:00 hrs, check-out 11:00 hrs. Temple dress code requires modest attire. Coastal areas can be humid—carry lightweight cotton clothes, sunhats, and sunglasses. Advance booking 30-45 days recommended during festivals.",
                12,
            ),
        ],
        moods=["Spiritual", "Heritage", "Family"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Handpicked Tariffs)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Dwarka Somnath Pilgrimage • Sacred Western Coast Circuit",
        overview=(
            "Welcome to the land of legends and timeless spirituality. The Best Gujarat Tour Package by TRAGUIN "
            "brings you a beautifully balanced, premium itinerary covering the most revered shrines of western India. "
            "This Gujarat Pilgrimage itinerary takes you seamlessly from the historic heritage of Ahmedabad to the "
            "sacred, wave-washed shores of Dwarka and Somnath.\n\n"
            "TRAGUIN Curated Experience Note: Every aspect of this trip has been meticulously engineered for "
            "ultimate comfort. From premium stays at handpicked hotels close to the temples to private luxury "
            "transportation and VIP darshan assistance, TRAGUIN ensures that your spiritual focus remains absolute "
            "while we handle the logistics with flawless perfection.\n\n"
            "A pilgrimage to the sacred land of Gujarat is a journey of a lifetime. Home to the Top Tourist Places "
            "in Gujarat, this region attracts millions of devotees and culture enthusiasts annually. Famous attractions "
            "include the architectural marvel of Dwarkadhish Temple, the magnificent shore-bound Somnath Temple, the "
            "peaceful Sabarmati Ashram, and the scenic beauty of the Arabian Sea coastline. The Best Time to Visit "
            "Gujarat is during the cooler months when the sea breeze elevates the divine energy of these sacred destinations."
        ),
        seo_title="GJ-001 | Dwarka Somnath Pilgrimage | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days Gujarat pilgrimage (GJ-001 / TRG-GJ-PILGRIMAGE-001): Dwarkadhish Temple, "
            "Beyt Dwarka, Nageshwar Jyotirlinga, Somnath Temple, Porbandar Kirti Mandir, Sabarmati Ashram, and "
            "4-tier handpicked accommodation"
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Dwarkadhish Temple Evening Aarti, Gomti River Ghats, Beyt Dwarka Island, Nageshwar Jyotirlinga.", 1),
            _ih("Kirti Mandir (Porbandar), Somnath Temple Complex, Light & Sound Show, Triveni Sangam, Bhalka Tirth.", 2),
            _ih("Sabarmati Ashram, Adalaj Stepwell, Law Garden handicraft market.", 3),
            _ih("TRAGUIN Signature Experience: Professionally vetted chauffeurs familiar with local pilgrimage routes and custom schedules.", 4),
            _ih("Curated by TRAGUIN Experts: Itineraries planned to minimize fatigue for elderly family members with smooth, well-timed transfers.", 5),
            _ih("Premium Handpicked Hotels: Properties featuring top-tier safety, excellent sanitation, and outstanding reviews.", 6),
        ],
        days=[
            _day(
                1,
                "AHMEDABAD TO DWARKA • ARRIVAL & JOURNEY TO THE KINGDOM OF KRISHNA",
                (
                    "Your highly anticipated Luxury Gujarat Holiday begins with a warm welcome by a TRAGUIN corporate "
                    "representative at Ahmedabad Airport or Railway Station. Step into your premium, air-conditioned private "
                    "vehicle and embark on a scenic drive toward the ancient, holy city of Dwarka. As you leave the bustling "
                    "cityscape behind, watch the changing landscape turn into pristine rustic terrain. Upon arriving in Dwarka, "
                    "check into your premium handpicked hotel, intentionally chosen for its exceptional hospitality and close "
                    "proximity to sacred sites. In the evening, visit the legendary Dwarkadhish Temple (Jagat Mandir) for an "
                    "immersive experience during the evening Aarti. Stand in awe of the 5-story structure supported by 72 "
                    "pillars, feeling the emotional resonance of centuries-old devotion. Take a peaceful walk along the Gomti "
                    "River banks for perfect sunset photography."
                ),
                [
                    "Sightseeing Included: Dwarkadhish Temple Evening Aarti, Gomti River Ghats, local town walk.",
                    "Evening Experience: Spiritual immersion, listening to temple bells over the sound of ocean waves.",
                    "Overnight Stay: Premium Hotel in Dwarka.",
                    "Meals Included: Welcome Drink & Gourmet Dinner.",
                ],
            ),
            _day(
                2,
                "DWARKA & BEYT DWARKA • EXPLORING HOLY ISLANDS & DIVINE MYSTERIES",
                (
                    "Wake up to a beautiful morning and enjoy a lavish breakfast. Today features an extensive day of Dwarka "
                    "Sightseeing. We drive to Okha port, where an exclusive boat ride takes you across the sea to Beyt Dwarka, "
                    "the historic residence of Lord Krishna. Marvel at the marine birdlife and the breathtaking landscapes along "
                    "the way. On your return journey, visit the iconic Nageshwar Jyotirlinga, one of the 12 sacred Jyotirlingas "
                    "in the world, featuring a majestic 82-foot statue of Lord Shiva. Proceed to Gopi Talav, the sacred pond "
                    "associated with the folklore of Krishna's Gopis, and Rukmini Devi Temple, dedicated to Lord Krishna's "
                    "beloved consort. End your evening exploring local brassware and traditional textile shops in Dwarka's "
                    "historic markets."
                ),
                [
                    "Sightseeing Included: Beyt Dwarka Island, Nageshwar Jyotirlinga, Gopi Talav, Rukmini Devi Temple.",
                    "Optional Activities: Speedboat rental at Okha, local guide storytelling experience.",
                    "Overnight Stay: Premium Hotel in Dwarka.",
                    "Meals Included: Premium Breakfast & Dinner.",
                ],
            ),
            _day(
                3,
                "DWARKA TO SOMNATH VIA PORBANDAR • COASTAL ROADS & HERITAGE TRAILS",
                (
                    "Bid farewell to Dwarka as your TRAGUIN Gujarat Package carries you down the picturesque coastal highway "
                    "towards Somnath. Break your journey at Porbandar, the historic birthplace of Mahatma Gandhi. Visit Kirti "
                    "Mandir, a beautiful monument built adjacent to the three-story ancestral house where Gandhiji was born, "
                    "serving as an emotional window into India's freedom struggle. Continue the drive to Somnath, experiencing "
                    "unmatched scenic beauty where the highway runs parallel to the Arabian Sea. Upon arrival, check into your "
                    "luxury resort. As dusk approaches, head to the world-renowned Somnath Temple. Witness the spellbinding "
                    "architectural grandeur of this eternal shrine that has withstood the test of time, followed by a dramatic "
                    "evening Light & Sound Show highlighting its glorious history."
                ),
                [
                    "Sightseeing Included: Kirti Mandir (Porbandar), Sudama Temple, Somnath Temple Complex, Light & Sound Show.",
                    "Evening Experience: Chanting prayers with ocean waves crashing against the temple's stone foundations.",
                    "Overnight Stay: Premium Luxury Resort in Somnath.",
                    "Meals Included: Premium Breakfast & Dinner.",
                ],
            ),
            _day(
                4,
                "SOMNATH SIGHTSEEING • SACRED CONFLUENCES & INNER PEACE",
                (
                    "Dedicate your day to exploring the spiritual landmarks surrounding Somnath. Following a rich traditional "
                    "breakfast, visit the holy Triveni Sangam, the sacred geographic confluence of three mystical rivers: Hiran, "
                    "Kapila, and Saraswati, where pilgrims take cleansing dips. Next, discover the peaceful Bhalka Tirth, the "
                    "poignant historical site where Lord Krishna was resting under a pipal tree when he was struck by an arrow, "
                    "marking the end of his earthly avatar. Visit the ancient Geeta Mandir and the unique Lakshminarayan Temple. "
                    "Spend your evening at the serene Somnath Beach, capture perfect Instagram photographs, or buy beautiful local "
                    "seashells and handicrafts from local stalls."
                ),
                [
                    "Sightseeing Included: Triveni Sangam Ghats, Bhalka Tirth, Geeta Mandir, Somnath Beach.",
                    "Optional Activities: Camel rides on Somnath Beach, extended meditation sessions at the temple gardens.",
                    "Overnight Stay: Premium Luxury Resort in Somnath.",
                    "Meals Included: Premium Breakfast & Dinner.",
                ],
            ),
            _day(
                5,
                "SOMNATH TO AHMEDABAD • RETURNING TO THE CULTURAL HUB",
                (
                    "Enjoy an early morning breakfast before beginning your journey back to Ahmedabad. The route takes you "
                    "through the heart of Saurashtra, giving you a chance to appreciate the rural charm and traditional life of "
                    "Gujarat. Arrive in Ahmedabad by afternoon and check into your premium luxury city hotel. Spend the rest of "
                    "your day exploring the cultural marvels of India's first UNESCO World Heritage City. Visit the serene "
                    "Sabarmati Ashram, the peaceful home of Mahatma Gandhi along the quiet riverbank, followed by the "
                    "architectural masterpiece of Adalaj Stepwell. Finish your evening with an elite dining experience, savoring "
                    "an authentic, multi-course Gujarati Thali."
                ),
                [
                    "Sightseeing Included: Sabarmati Ashram, Adalaj Stepwell, Law Garden handicraft market.",
                    "Food Suggestion: Traditional Premium Heritage Gujarati Thali at a curated restaurant.",
                    "Overnight Stay: Premium Luxury Hotel in Ahmedabad.",
                    "Meals Included: Premium Breakfast & Farewell Dinner.",
                ],
            ),
            _day(
                6,
                "AHMEDABAD DEPARTURE • MEMORIES OF A DIVINE JOURNEY",
                (
                    "Savor your final breakfast of this unforgettable tour. Depending on your departure schedule, squeeze in some "
                    "last-minute boutique shopping for authentic Patola sarees, traditional Bandhani textiles, and unique terracotta "
                    "souvenirs. Conclude your tour as our private vehicle transfers you smoothly to Ahmedabad Airport or Railway "
                    "Station for your onward journey. Your divine Somnath Family Tour concludes, leaving you with unforgettable "
                    "memories and a renewed spirit, proudly managed by TRAGUIN."
                ),
                [
                    "Transfers Included: Private luxury airport/station drop-off.",
                    "Meals Included: Premium Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Hotel Rudra Plaza / Similar | Lord's Inn Somnath / Similar | Lemon Tree Ahmedabad / Similar",
                "Dwarka (2N) / Somnath (2N) / Ahmedabad (1N)",
                "05 Nights",
                "Deluxe",
                "Standard Room",
                "MAPAI",
                4,
                1,
                description=(
                    "OPTION 01 – DELUXE: Hotel Rudra Plaza / Similar (Dwarka (2N)) | "
                    "Lord's Inn Somnath / Similar (Somnath (2N)) | "
                    "Lemon Tree Ahmedabad / Similar (Ahmedabad (1N)) | MAPAI"
                ),
            ),
            _hotel(
                "Hawthorn Suites by Wyndham | The Fern Residency / Similar | Radisson Blu Ahmedabad",
                "Dwarka (2N) / Somnath (2N) / Ahmedabad (1N)",
                "05 Nights",
                "Premium",
                "Premium Room",
                "MAPAI",
                4,
                2,
                description=(
                    "OPTION 02 – PREMIUM: Hawthorn Suites by Wyndham (Dwarka (2N)) | "
                    "The Fern Residency / Similar (Somnath (2N)) | "
                    "Radisson Blu Ahmedabad (Ahmedabad (1N)) | MAPAI"
                ),
            ),
            _hotel(
                "Mercure Dwarka Resort | Somnath Sagar Resort / Premium | Courtyard by Marriott",
                "Dwarka (2N) / Somnath (2N) / Ahmedabad (1N)",
                "05 Nights",
                "Luxury",
                "Luxury Room",
                "MAPAI",
                5,
                3,
                description=(
                    "OPTION 03 – LUXURY: Mercure Dwarka Resort (Dwarka (2N)) | "
                    "Somnath Sagar Resort / Premium (Somnath (2N)) | "
                    "Courtyard by Marriott (Ahmedabad (1N)) | MAPAI"
                ),
            ),
            _hotel(
                "The Fern Sattva Resort | Taj Wayanad Coastal Select / Equivalent | Hyatt Regency / ITC Narmada",
                "Dwarka (2N) / Somnath (2N) / Ahmedabad (1N)",
                "05 Nights",
                "Ultra Luxury",
                "Ultra Luxury Suite",
                "MAPAI",
                5,
                4,
                description=(
                    "OPTION 04 – ULTRA LUXURY: The Fern Sattva Resort (Dwarka (2N)) | "
                    "Taj Wayanad Coastal Select / Equivalent (Somnath (2N)) | "
                    "Hyatt Regency / ITC Narmada (Ahmedabad (1N)) | MAPAI"
                ),
            ),
        ],
        inclusions=[
            _inc_included("Accommodation: 05 Nights stay in handpicked premium hotels.", 1),
            _inc_included("Meal Plan: Daily breakfast & dinner at hotel restaurants.", 2),
            _inc_included("Luxury Transfers: AC dedicated private vehicle for all transfers & sightseeing.", 3),
            _inc_included("VIP Assistance: Personalized temple arrival coordination by TRAGUIN network.", 4),
            _inc_included("Complimentary Experiences: Complimentary boat tickets for Beyt Dwarka excursion.", 5),
            _inc_included("Welcome Amenities: Traditional non-alcoholic welcome drink on arrival.", 6),
            _inc_included("Taxes: Tolls, parking, driver allowances, and all current applicable GST.", 7),
            _inc_included("TRAGUIN Support: 24/7 dedicated guest relations backend support.", 8),
            _inc_excluded("Flights / Rail: Airfare or train tickets to/from Ahmedabad.", 9),
            _inc_excluded("Entry Tickets: Camera fees, monuments, and Light/Sound show entry passes.", 10),
            _inc_excluded("Personal Expenses: Laundry, telephone calls, tips, and minibar usage.", 11),
            _inc_excluded("Optional Activities: Water sports, special fast-track darshan custom receipts.", 12),
            _inc_excluded("Insurance: Travel medical insurance or unexpected flight delay costs.", 13),
            _inc_excluded("Unspecified Items: Anything not explicitly listed in the inclusions.", 14),
        ],
    )
    return package, itinerary


def build_gj_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "GJ-002"
    tour_code = "TRAGUIN-GJ-002"
    title = "Gujarat Discovery Luxury Itinerary"
    duration = "06 Nights / 07 Days"
    slug = "gj-002-gujarat-discovery-luxury-itinerary"
    itin_slug = "gj-002-gujarat-discovery-luxury-itinerary-itinerary"
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
            _ph("State / Country: Gujarat / India | Category: Family / Luxury", 2),
            _ph("Destinations: Ahmedabad • Dasada • Bhuj • Rann of Kutch", 3),
            _ph("Ideal for: Family Vacations & Heritage Lovers", 4),
            _ph("Best season: October to March", 5),
            _ph("Travel Format: Private Customized Luxury Family Tour (FIT)", 6),
            _ph("Vehicle: Private Air-Conditioned Luxury Vehicle with Dedicated Chauffeur", 7),
            _ph("Meal Plan: Daily gourmet breakfast and dinners as listed in the itinerary", 8),
            _ph("Route Map: Ahmedabad (2N) → Dasada (1N) → Bhuj (1N) → Rann of Kutch (2N) → Ahmedabad (1N)", 9),
            _ph(
                "TRAGUIN Signature Experience: Private sun-downer high-tea inside the vast desert wilderness of Kutch, curated by experts with flexible paced travel plans for families with children or elderly members.",
                10,
            ),
            _ph(
                "Shopping: Bandhani sarees, Ajrakh hand-block print fabrics, Kutchi mirror-work embroidery bags, and traditional silver jewelry at Bhujodi and local markets in Bhuj.",
                11,
            ),
            _ph(
                "Important: Rann permit requires physical/online government permits—carry Aadhaar/Passport copies. Winter desert nights are cold—carry warm layers. Advance bookings recommended during Rann Utsav festival months.",
                12,
            ),
        ],
        moods=["Family", "Culture", "Luxury"],
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
        tagline="Gujarat Discovery Luxury Itinerary • Heritage, Wildlife & White Desert",
        overview=(
            "Welcome to an unforgettable journey curated by TRAGUIN. Immerse your family in the breathtaking landscapes, "
            "ancient legacy, and timeless traditions of Western India. This bespoke Luxury Gujarat Holiday is specifically "
            "designed to bring you the finest Premium Gujarat Experience, blending handpicked hotels, cultural wonders, "
            "and immersive experiences that cater perfectly to a premium family vacation.\n\n"
            "This Best Gujarat Tour Package takes your family through a seamless luxury route starting from the vibrant "
            "heritage city of Ahmedabad, moving into the wild terrains of Dasada (Little Rann of Kutch), and culminating "
            "in the magnificent white salt deserts of Bhuj and the Greater Rann of Kutch. Travelling in a premium, private "
            "air-conditioned vehicle with handpicked heritage and luxury stays, your family will experience comfort at every turn.\n\n"
            "Gujarat stands out as one of the most culturally rich and visually dynamic destinations in Asia. The absolute "
            "highlight of any Gujarat Sightseeing journey is the spellbinding Great Rann of Kutch, famous for its glowing "
            "white salt plains under full moon nights and spectacular desert sunsets. Popular Instagram locations include "
            "colorful tent cities, geometric art of centuries-old stepwells, and intricate traditional embroidery of "
            "nomadic tribes in Bhuj."
        ),
        seo_title="GJ-002 | Gujarat Discovery Luxury Itinerary | TRAGUIN",
        seo_description=(
            "Premium 06 Nights / 07 Days Gujarat package (GJ-002 / TRAGUIN-GJ-002): Sabarmati Ashram, Adalaj Stepwell, "
            "Little Rann safari, Aina Mahal, Great White Rann, Kalo Dungar, Modhera Sun Temple, and 4-tier handpicked accommodation"
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Sabarmati Ashram, Adalaj Stepwell, open jeep safari in Little Rann of Kutch.", 1),
            _ih("Aina Mahal, Prag Mahal, Great White Rann Plains, Kalo Dungar, Nirona Craft Village.", 2),
            _ih("Modhera Sun Temple, Patan Rani Ki Vav (Optional UNESCO Site).", 3),
            _ih("TRAGUIN Signature Experience: Private sun-downer high-tea experience inside the vast desert wilderness of Kutch.", 4),
            _ih("Curated by Experts: Fully flexible, paced travel plans custom tailored for families travelling with children or elderly members.", 5),
            _ih("Local Immersion: Direct access to multi-generational local artisan homes for live heritage craft masterclasses.", 6),
        ],
        days=[
            _day(
                1,
                "AHMEDABAD | ARRIVAL IN THE HERITAGE CITY & SCENIC SIGHTSEEING",
                (
                    "Arrive in Ahmedabad, India's first UNESCO World Heritage City, where you will be greeted by a warm traditional "
                    "welcome arranged by your dedicated chauffeur. Transfer seamlessly in your private premium vehicle to your "
                    "handpicked luxury hotel. In the afternoon, embark on an immersive Ahmedabad Sightseeing tour. Visit the serene "
                    "Sabarmati Ashram, the peaceful historic home of Mahatma Gandhi, located on the tranquil banks of the Sabarmati "
                    "River. Following this, explore the architectural masterpiece of the Adalaj Stepwell, a beautifully carved "
                    "five-story deep structure displaying stunning ancient Indian engineering. In the evening, capture beautiful family "
                    "photographs as the sun sets over the riverfront."
                ),
                [
                    "Sightseeing Included: Sabarmati Ashram, Adalaj Stepwell, Akshardham Temple (Optional).",
                    "Evening Experience: Leisure stroll along the illuminated Sabarmati Riverfront.",
                    "Overnight Stay: Ahmedabad (Luxury Heritage Hotel).",
                    "Meals Included: Welcome Dinner.",
                ],
            ),
            _day(
                2,
                "AHMEDABAD TO DASADA | JOURNEY INTO THE WILD LITTLE RANN OF KUTCH",
                (
                    "Enjoy a gourmet breakfast at your luxury hotel before checking out. Today, your premium journey proceeds toward "
                    "Dasada, the gateway to the Little Rann of Kutch. Upon arrival, check in to an exclusive eco-luxury desert resort. "
                    "In the afternoon, gear up for an exciting open jeep cross-country desert safari across the cracked earth landscapes "
                    "of the sanctuary. This unique habitat is the exclusive home of the rare endangered Asiatic Wild Ass. Marvel at the "
                    "breathtaking landscapes and spectacular desert birds like flamingos and pelicans. As evening approaches, enjoy a "
                    "high-tea setup amidst the desert plains while witnessing a glorious, unobstructed sunset."
                ),
                [
                    "Sightseeing Included: Open Jeep Safari in Little Rann of Kutch Sanctuary, Local Rabari Tribal Village tour.",
                    "Evening Experience: Traditional campfire and folk performance at the luxury resort.",
                    "Overnight Stay: Dasada / Bajana (Premium Desert Resort).",
                    "Meals Included: Breakfast, Lunch & Dinner.",
                ],
            ),
            _day(
                3,
                "DASADA TO BHUJ | PATHWAY TO HISTORIC PALACES & HANDICRAFT HERITAGE",
                (
                    "After a relaxed breakfast, take a scenic drive toward the historic city of Bhuj, the cultural heart of the Kutch "
                    "region. The drive showcases transitioning landscapes from dry scrublands into beautiful arid hills. Arrive in Bhuj "
                    "and check in to your premium suite accommodation. In the afternoon, start your local Bhuj Sightseeing. Visit the "
                    "magnificent Aina Mahal (Palace of Mirrors), showcasing European-inspired glass layouts combined with local "
                    "craftsmanship, followed by the nearby Prag Mahal with its grand Italian-Gothic architecture and panoramic clock "
                    "tower views. Conclude your afternoon exploring the beautiful royal cenotaphs at Chattardi, a highly sought-after "
                    "photography point."
                ),
                [
                    "Sightseeing Included: Aina Mahal, Prag Mahal, Bhujodi Weaver Village, Sharad Baug Palace.",
                    "Evening Experience: Curated shopping at Bhujodi for premium handmade shawls and fabrics.",
                    "Overnight Stay: Bhuj (Premium Luxury Hotel).",
                    "Meals Included: Breakfast & Dinner.",
                ],
            ),
            _day(
                4,
                "BHUJ TO GREATER RANN OF KUTCH | THE MAGIC OF THE WHITE SALT DESERT",
                (
                    "Today marks the pinnacle of your Luxury Gujarat Holiday. Depart Bhuj for the Greater Rann of Kutch, checking "
                    "into a premium luxury tent resort near Dhordo. After settling into your air-conditioned luxury tent, prepare to "
                    "witness one of the top tourist places in Gujarat. In the late afternoon, your vehicle takes you to the edge of the "
                    "endless salt marsh. Step onto the spectacular white desert that stretches into the horizon. The emotional "
                    "storytelling of this place comes alive as you watch the white landscape change colors from soft gold to brilliant "
                    "orange, and finally turn to a pristine silver under the rising moon—an absolute highlight for unforgettable family "
                    "memories."
                ),
                [
                    "Sightseeing Included: Great White Rann Plains, Dhordo Tent City Culture Zone.",
                    "Evening Experience: Cultural music, camel cart rides, and stargazing on the salt desert.",
                    "Overnight Stay: Rann of Kutch / Dhordo (Premium Luxury Tent Resort).",
                    "Meals Included: Breakfast, Lunch & Dinner.",
                ],
            ),
            _day(
                5,
                "EXCURSION TO KALO DUNGAR & INDIGENOUS ARTISAN VILLAGES",
                (
                    "Wake up early to catch a pristine desert sunrise. Following a lavish breakfast, proceed on an excursion to Kalo "
                    "Dungar (Black Hill), the highest point in Kutch. From the summit, enjoy a jaw-dropping panoramic view of the entire "
                    "white desert blending into the horizon and the international border. On the way back, experience an immersive "
                    "cultural tour of local artisan villages like Hodka and Nirona. In Nirona, witness exclusive art forms like Rogan "
                    "painting, traditional lacquer-turned woodcraft, and hand-forged copper bells made by local families using "
                    "generations-old secret techniques."
                ),
                [
                    "Sightseeing Included: Kalo Dungar, Dattatreya Temple, Nirona Craft Village, Hodka Village.",
                    "Evening Experience: Interactive session with national-award-winning Rogan artists.",
                    "Overnight Stay: Rann of Kutch / Dhordo (Premium Luxury Tent Resort).",
                    "Meals Included: Breakfast, Lunch & Dinner.",
                ],
            ),
            _day(
                6,
                "RANN OF KUTCH TO AHMEDABAD | RETURN JOURNEY VIA MODHERA SUN TEMPLE",
                (
                    "Bid farewell to the enchanting salt deserts and drive back toward Ahmedabad. To ensure your return path is just as "
                    "memorable, a special detour is curated to visit the magnificent Sun Temple at Modhera. This 11th-century "
                    "architectural masterpiece is designed so that the rays of the rising sun illuminate the inner sanctum during equinoxes. "
                    "Walk past the grand Surya Kund, a deeply stepped reservoir featuring over a hundred beautifully carved miniature "
                    "shrines. After capturing magnificent photographs of this historic monument, continue your smooth drive back to "
                    "Ahmedabad for a relaxing final night."
                ),
                [
                    "Sightseeing Included: Modhera Sun Temple, Patan Rani Ki Vav (Optional UNESCO Site).",
                    "Evening Experience: Gala farewell family dinner highlighting authentic Gujarati fine dining.",
                    "Overnight Stay: Ahmedabad (Luxury Hotel).",
                    "Meals Included: Breakfast & Farewell Dinner.",
                ],
            ),
            _day(
                7,
                "AHMEDABAD | SOUVENIR SHOPPING & DEPARTURE WITH UNFORGETTABLE MEMORIES",
                (
                    "Savor a late breakfast at your hotel. Depending on your flight or train schedule, indulge in some last-minute luxury "
                    "shopping for souvenirs. Your private vehicle will transfer your family comfortably to the Ahmedabad International "
                    "Airport or Railway Station for your onward journey. Your premium TRAGUIN Gujarat Package concludes here, leaving your "
                    "family with beautiful, deep-seated memories of heritage, wildlife, and pristine white deserts that will be cherished "
                    "for a lifetime."
                ),
                [
                    "Sightseeing Included: Local shopping transfers.",
                    "Meals Included: Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Lemon Tree Premier | Rann Riders Eco Resort | Regenta Resort Bhuj | Rann Resort Dholavira",
                "Ahmedabad (2N) / Dasada (1N) / Bhuj (1N) / Rann of Kutch (2N)",
                "06 Nights",
                "Deluxe",
                "Standard Room / AC Tent",
                "Breakfast & Dinner",
                4,
                1,
                description=(
                    "OPTION 01 – DELUXE: Lemon Tree Premier (Ahmedabad (2N)) | "
                    "Rann Riders Eco Resort (Dasada (1N)) | "
                    "Regenta Resort Bhuj (Bhuj (1N)) | "
                    "Rann Resort Dholavira (Rann of Kutch (2N)) | Breakfast & Dinner"
                ),
            ),
            _hotel(
                "Hyatt Regency | Dasada Desert Lodge | The Fern Residency | White Rann Resort (AC Tent)",
                "Ahmedabad (2N) / Dasada (1N) / Bhuj (1N) / Rann of Kutch (2N)",
                "06 Nights",
                "Premium",
                "Premium Room / AC Tent",
                "Breakfast & Dinner",
                4,
                2,
                description=(
                    "OPTION 02 – PREMIUM: Hyatt Regency (Ahmedabad (2N)) | "
                    "Dasada Desert Lodge (Dasada (1N)) | "
                    "The Fern Residency (Bhuj (1N)) | "
                    "White Rann Resort (AC Tent) (Rann of Kutch (2N)) | Breakfast & Dinner"
                ),
            ),
            _hotel(
                "Taj Skyline / ITC Narmada | Rann Riders (Luxury Suite) | Grand 3D Bhuj | Evoke Rann Resort Luxury Tent",
                "Ahmedabad (2N) / Dasada (1N) / Bhuj (1N) / Rann of Kutch (2N)",
                "06 Nights",
                "Luxury",
                "Luxury Suite / Luxury Tent",
                "Breakfast & Dinner",
                5,
                3,
                description=(
                    "OPTION 03 – LUXURY: Taj Skyline / ITC Narmada (Ahmedabad (2N)) | "
                    "Rann Riders (Luxury Suite) (Dasada (1N)) | "
                    "Grand 3D Bhuj (Bhuj (1N)) | "
                    "Evoke Rann Resort Luxury Tent (Rann of Kutch (2N)) | Breakfast & Dinner"
                ),
            ),
            _hotel(
                "The House of MG (Heritage) | The Desert Courtyard Luxury | Prince Oasis Luxury Resort | The Gateway Rann Resort (Premium)",
                "Ahmedabad (2N) / Dasada (1N) / Bhuj (1N) / Rann of Kutch (2N)",
                "06 Nights",
                "Ultra Luxury",
                "Heritage Suite / Premium Tent",
                "Gourmet Meal Plan",
                5,
                4,
                description=(
                    "OPTION 04 – ULTRA LUXURY: The House of MG (Heritage) (Ahmedabad (2N)) | "
                    "The Desert Courtyard Luxury (Dasada (1N)) | "
                    "Prince Oasis Luxury Resort (Bhuj (1N)) | "
                    "The Gateway Rann Resort (Premium) (Rann of Kutch (2N)) | Gourmet Meal Plan"
                ),
            ),
        ],
        inclusions=[
            _inc_included("Premium Accommodation in handpicked luxury hotels & tent resorts.", 1),
            _inc_included("Daily gourmet breakfast and dinners as listed in the meal plan.", 2),
            _inc_included("All transfers and sightseeing in a private dedicated luxury AC vehicle.", 3),
            _inc_included("Complimentary open jeep desert safari inside Little Rann of Kutch.", 4),
            _inc_included("Special TRAGUIN Signature Welcome Amenities on arrival.", 5),
            _inc_included("Curated artisan village interaction fees and entry assistance.", 6),
            _inc_included("All applicable luxury taxes, toll fees, driver allowances, and parking charges.", 7),
            _inc_included("24/7 personalized remote concierge support via TRAGUIN Experts.", 8),
            _inc_excluded("Airfare or train tickets to and from Ahmedabad.", 9),
            _inc_excluded("Monument entry fees, camera charges, and local guide fees.", 10),
            _inc_excluded("Personal expenses (laundry, telephone calls, mini-bar, tips).", 11),
            _inc_excluded("Optional activities, camel safari upgrades, or hot air balloon rides.", 12),
            _inc_excluded("Any meals or alcoholic beverages not specifically noted in the itinerary.", 13),
            _inc_excluded("Travel insurance coverages (highly recommended).", 14),
            _inc_excluded("Cost arising due to unexpected road closures, weather delays, or flight cancellations.", 15),
        ],
    )
    return package, itinerary


def build_gj_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "GJ-003"
    tour_code = "TRG-GIR-003-2026"
    title = "Sasan Gir Wildlife Safari"
    duration = "03 Nights / 04 Days"
    slug = "gj-003-sasan-gir-wildlife-safari"
    itin_slug = "gj-003-sasan-gir-itinerary"
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
            _ph("State / Country: Gujarat / India | Category: Luxury Wildlife & Safaris", 2),
            _ph("Destinations: Sasan Gir National Park", 3),
            _ph("Ideal for: Wildlife Enthusiasts, Families, Luxury Travelers", 4),
            _ph("Best season: October to April", 5),
            _ph("Starting price: On Request (Premium Customised)", 6),
            _ph("Travel Format: FIT / Private Family / Premium Couples", 7),
            _ph("Vehicle: Dedicated Luxury Chauffeur-Driven SUV (Innova Crysta or equivalent)", 8),
            _ph("Meal Plan: All Meals Included (Breakfast, Lunch, and Dinner at the Luxury Resort)", 9),
            _ph("Route Plan: Rajkot/Ahmedabad/Diu Airport → Sasan Gir Sanctuary → Departure Airport", 10),
            _ph(
                "TRAGUIN Curated Advantage: Handpicked wildlife naturalists, pre-booked VIP safari allocations, premium luxury amenities, and 2026 24/7 dedicated concierge assistance.",
                11,
            ),
            _ph(
                "Shopping: Kesar Mangoes (seasonal), hand-embroidered traditional attire, intricate tribal woodwork, and pure organic honey from local craft centers.",
                12,
            ),
            _ph(
                "Important: Gir safari permits require booking 60-90 days in advance. Carry original government ID for park entry. Core zones closed 16 June–15 October. Wear neutral tones during safaris.",
                13,
            ),
        ],
        moods=["Wildlife", "Luxury", "Family"],
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
        tagline="Sasan Gir Wildlife Safari • The Lion's Kingdom",
        overview=(
            "Embark on an extraordinary wildlife expedition curated especially for discerning travelers with the Best "
            "Gujarat Tour Package by TRAGUIN. Venture into the rugged, sun-dappled deciduous forests of Sasan Gir, the "
            "historic last refuge of the majestic Asiatic Lion. This bespoke Gujarat Family Tour offers a brilliant confluence "
            "of untamed wilderness, raw natural beauty, and ultra-luxury hospitality.\n\n"
            "Your premium Luxury Gujarat Holiday is thoroughly planned and executed by professional destination specialists. "
            "From seamlessly synchronized transfers in a private luxury SUV to staying at the finest properties embedded in "
            "nature, every detail reflects the high standards of a signature TRAGUIN curated experience.\n\n"
            "Sasan Gir is universally recognized as the jewel of wildlife tourism in Western India. The absolute pinnacle of "
            "your Gujarat Sightseeing journey is the exclusive Gir Jungle Safari, widely cited as one of the most searched "
            "experiences in worldwide tourism. Our premium TRAGUIN Gujarat Packages are tailored to position you right at "
            "the heart of the wilderness during the Best Time to Visit Gujarat."
        ),
        seo_title="GJ-003 | Sasan Gir Wildlife Safari | TRAGUIN",
        seo_description=(
            "Premium 03 Nights / 04 Days Gujarat wildlife package (GJ-003 / TRG-GIR-003-2026): Gir Jungle Safari, "
            "Devalia Interpretation Zone, Kamleshwar Dam, Maldhari tribal settlement, and 4-tier handpicked accommodation"
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Premium Morning Gir Jungle Safari with certified naturalist guide.", 1),
            _ih("Devalia Interpretation Zone, Kamleshwar Dam Crocodile Breeding Center.", 2),
            _ih("Maldhari tribal settlement walk, Siddi folk performance, exclusive bush dinner.", 3),
            _ih("TRAGUIN Signature Experience: Private bonfire dinner underneath the stars with curated regional menus.", 4),
            _ih("Curated by TRAGUIN Experts: Direct access to top-tier tracks and booking zones within the sanctuary.", 5),
            _ih("Premium Handpicked Hotels: Properties chosen for eco-luxury architecture, zero-noise pollution, and superb hospitality.", 6),
        ],
        days=[
            _day(
                1,
                "ARRIVAL AT RAJKOT/DIU & TRANSFER TO SASAN GIR",
                (
                    "Arrive at the designated airport where a plush, air-conditioned luxury SUV awaits your exclusive arrival. "
                    "Begin your premium journey as you are chauffeured through breathtaking landscapes, changing from urban sprawls "
                    "to rustic, golden-hued countryside roads heading toward Sasan Gir. The crisp air whispers tales of the wild as "
                    "you approach your handpicked luxury eco-resort. Upon arrival, enjoy a traditional, refreshing welcome experience "
                    "meticulously organized by the resort staff under the directive of TRAGUIN. After a lavish lunch curated by master "
                    "chefs, spend your afternoon relaxing at your private sundeck or taking a dip in the pristine azure pool overlooking "
                    "the forest rim. In the evening, walk along the nature-scented trails bordering the Hiran River, a premium "
                    "photography point. Conclude the day with a candlelight gourmet dinner featuring authentic local delicacies "
                    "prepared with a modern twist."
                ),
                [
                    "Sightseeing Included: Scenic countryside drive, orientation walk around the Hiran River trail.",
                    "Optional Activities: Therapeutic wellness spa session at the luxury resort.",
                    "Evening Experience: Tribal folk performance by the local Siddi community around a warm campfire.",
                    "Overnight Stay: Handpicked Luxury Resort (Sasan Gir).",
                    "Meals Included: Lunch & Dinner.",
                ],
            ),
            _day(
                2,
                "THRILLING ASIATIC LION SAFARI & DEEP WILDERNESS TRAIL",
                (
                    "Wake up before dawn to a refreshing hot brew as you prepare for the ultimate highlight of your Gir Safari. Board "
                    "your pre-booked, private open-top 4x4 jungle safari vehicle accompanied by a senior certified naturalist. As the "
                    "morning mist gently clears, enter the pristine core zones of Sasan Gir National Park. Keep your cameras ready for "
                    "iconic attractions and breathtaking landscapes as your naturalist tracks fresh pugmarks. Listen to warning calls "
                    "echoing through the teak canopy before capturing the unforgettable memory of a majestic Asiatic Lion pride resting "
                    "elegantly in their natural domain. After a thrilling morning safari, return to the premium stay for a hearty, "
                    "multi-cuisine breakfast. In the afternoon, embark on an insightful journey to the Gir Interpretation Zone at Devalia, "
                    "ensuring a holistic understanding of the regional conservation efforts. As dusk settles, capture the sunset over the "
                    "dramatic forest landscape, a top-rated Instagram location."
                ),
                [
                    "Sightseeing Included: Premium Morning Gir Jungle Safari, Devalia Interpretation Zone exploration.",
                    "Optional Activities: Private interactive session with a senior wildlife researcher and photographer.",
                    "Evening Experience: Relaxed documentary screening on Lion Conservation followed by high tea.",
                    "Overnight Stay: Handpicked Luxury Resort (Sasan Gir).",
                    "Meals Included: Breakfast, Lunch & Dinner.",
                ],
            ),
            _day(
                3,
                "SECONDARY SAFARI ZONE / CROCODILE PARK & CULTURE WALK",
                (
                    "Dedicate your morning to discovering the finer nuances of the forest ecosystem. Opt for an optional second morning "
                    "safari to explore a different core route of the national park, maximizing your chances of sighting leopards and "
                    "exotic birds. Alternatively, enjoy a peaceful breakfast followed by an exclusive guided tour to the Kamleshwar Dam, "
                    "famously known as the Crocodile Breeding Center, offering panoramic views of the entire sanctuary. In the afternoon, "
                    "experience an immersive cultural highlight as you visit a local Maldhari 'Ness' (settlement). Learn about their unique, "
                    "harmonious co-existence with the wild apex predators. Afterward, browse local artisan workshops to purchase authentic "
                    "hand-woven handicrafts, beautiful bandhani textiles, and pure organic honey as precious souvenirs. Your final evening "
                    "culminates in an extraordinary premium dining layout under a canopy of stars, uniquely curated by your premium travel partner."
                ),
                [
                    "Sightseeing Included: Kamleshwar Dam visit, Maldhari tribal settlement walk, local craft village tour.",
                    "Optional Activities: Secondary morning/afternoon jungle safari track.",
                    "Evening Experience: Exclusive Premium Bush Dinner setup with live instrumental ambient music.",
                    "Overnight Stay: Handpicked Luxury Resort (Sasan Gir).",
                    "Meals Included: Breakfast, Lunch & Dinner.",
                ],
            ),
            _day(
                4,
                "HOMEWARD JOURNEY WITH UNFORGETTABLE MEMORIES",
                (
                    "Awaken to the serene, musical symphony of chirping birds on your final morning in the wilderness. Indulge in an "
                    "exquisite champagne breakfast laid out in the beautifully manicured lawns of your luxury property. Take a final stroll "
                    "through the organic mango orchards within the resort grounds, capturing lasting photographs of your premium TRAGUIN "
                    "experience. Complete the checkout formalities, and board your private luxury SUV. As you are smoothly transferred back "
                    "to Rajkot or Diu Airport for your flight home, reminisce about the breathtaking landscapes, close encounters with the "
                    "King of the Jungle, and the elite pampering that defined your unforgettable holiday."
                ),
                [
                    "Sightseeing Included: Comfortable return transit, short stopover at local souvenir markets.",
                    "Meals Included: Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel("The Fern Gir Forest Resort / Similar", "Sasan Gir", "03 Nights", "Deluxe", "Fern Club Room", "All Meals (AP)", 4, 1),
            _hotel("Woods at Sasan / Similar", "Sasan Gir", "03 Nights", "Premium", "Luxury Pavilion", "All Meals (AP)", 4, 2),
            _hotel("Aramness Gir National Park / Similar", "Sasan Gir", "03 Nights", "Luxury", "Luxury Forest Kothi", "All Meals (AP)", 5, 3),
            _hotel("The Taj Gateway Hotel Gir Forest / Exclusive Villas", "Sasan Gir", "03 Nights", "Ultra Luxury", "Executive Suite / Luxury Villa", "All Meals (AP)", 5, 4),
        ],
        inclusions=[
            _inc_included("Premium Accommodation: 03 Nights stay in handpicked elite wildlife resorts.", 1),
            _inc_included("Full Board Dining: Daily breakfast, gourmet lunches, and premium dinners included.", 2),
            _inc_included("Luxury Transfers: Private, dedicated luxury SUV for all airport transits and sightseeing.", 3),
            _inc_included("Safari Bookings: 01 Premium Private 4x4 Gir Jungle Safari with mandatory permits & professional naturalist guide.", 4),
            _inc_included("Welcome Amenities: Refreshing herbal signature welcome drinks and curated fruit platter upon check-in.", 5),
            _inc_included("Complimentary Experiences: Guided nature trails and culturally rich tribal interaction walks.", 6),
            _inc_included("TRAGUIN Support: Continuous 24/7 priority concierge backing throughout the trip.", 7),
            _inc_excluded("Airfare / Rail: Domestic and International flight tickets to/from Gujarat.", 8),
            _inc_excluded("Additional Safaris: Extra jungle tracks or alternative zone permits not specified.", 9),
            _inc_excluded("Personal Expenses: Laundry, telephone calls, premium alcoholic beverages, and boutique room service.", 10),
            _inc_excluded("Camera Fees: High-end professional video camera equipment permits inside the national park.", 11),
            _inc_excluded("Insurance: Individual travel, medical, or baggage loss insurance cover.", 12),
            _inc_excluded("Tipping: Gratuities for drivers, safari naturalists, and hotel bellboys.", 13),
        ],
    )
    return package, itinerary


def build_gj_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "GJ-004"
    tour_code = "TRG-KUTCH-LUX-004"
    title = "Rann of Kutch Luxury Extravaganza"
    duration = "04 Nights / 05 Days"
    slug = "gj-004-rann-of-kutch-luxury-extravaganza"
    itin_slug = "gj-004-rann-of-kutch-itinerary"
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
            _ph("State / Country: Gujarat / India | Category: Premium Luxury Family Vacation", 2),
            _ph("Destinations: Bhuj • Rann of Kutch • Hodka • Dhordo • Mandvi", 3),
            _ph("Ideal for: Families, Couples, Culture & Photography Enthusiasts", 4),
            _ph("Best season: October to March (Rann Utsav Period)", 5),
            _ph("Starting price: On Request (Premium Custom Luxury Pricing)", 6),
            _ph("Travel Mode: Private Luxury FIT (Flexible Independent Tour)", 7),
            _ph("Vehicle: Chauffeur-Driven Premium Toyota Innova Crysta / Luxury SUV", 8),
            _ph("Meal Plan: MAPAI (Daily Premium Breakfast & Gourmet Dinner) / Full Board at Rann Tent City", 9),
            _ph("Route Map: Bhuj Airport → Hodka/Dhordo (Great Rann) → Mandvi Beach → Bhuj Drop", 10),
            _ph(
                "TRAGUIN Curated Note: Includes exclusive VIP access cards to the sunset viewing gallery, handpicked traditional Kutchi welcome amenities, and private artisan village interactions curated exclusively by TRAGUIN experts.",
                11,
            ),
            _ph(
                "Shopping: Bhujodi Village for traditional shawls, stoles, and handwoven dharis; authentic Kutchi Dabeli, Bajra rotlas, and rich sweet Mawa from local confectioneries.",
                12,
            ),
            _ph(
                "Important: White Desert permits mandatory—provide Aadhaar/Passport copies 7 days before arrival. Winter nights can drop to 8°C. Advance booking essential during Rann Utsav festival.",
                13,
            ),
        ],
        moods=["Culture", "Luxury", "Family"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Custom Luxury Pricing)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Rann of Kutch Luxury Extravaganza • White Desert & Coastal Heritage",
        overview=(
            "Step into a mystical landscape where the earth meets the sky in a seamless sheet of brilliant white salt. "
            "The Best Gujarat Tour Package by TRAGUIN invites your family to witness the ethereal beauty of the Great "
            "Rann of Kutch. This Luxury Gujarat Holiday blends emotional storytelling with seamless comfort, ensuring your "
            "family uncovers breathtaking landscapes, immersive experiences, and handpicked hotels.\n\n"
            "Our meticulously planned TRAGUIN Gujarat Packages are crafted specifically for discerning families who demand "
            "a seamless mixture of cultural immersion and elite relaxation. This personalized FIT package features private "
            "luxury transfers, curated heritage walks, and the absolute finest accommodations available in the Kutch region.\n\n"
            "The Great Rann of Kutch is globally renowned for its breathtaking white salt desert, vibrant handicraft heritage, "
            "and seasonal structural wonders. From the famous Instagram locations of the White Desert under a full moon to the "
            "royal heritage of Bhuj palaces and the peaceful coastal waters of Mandvi Beach, this region provides top tourist "
            "places in Gujarat that appeal to multi-generational families."
        ),
        seo_title="GJ-004 | Rann of Kutch Luxury Extravaganza | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Kutch package (GJ-004 / TRG-KUTCH-LUX-004): Great Rann of Kutch, Kalo Dungar, "
            "Gandhi Nu Gam craft village, Vijay Vilas Palace, Mandvi Beach, Aina Mahal, and 4-tier handpicked accommodation"
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Great Rann of Kutch Border Vistas, Salt Desert Sunset Gallery, Kalo Dungar Viewpoint.", 1),
            _ih("Gandhi Nu Gam Craft Village, Vijay Vilas Palace, Mandvi Private Beach.", 2),
            _ih("Aina Mahal, Prag Mahal, Bhujia Fort, Shree Swaminarayan Temple, Hamirsar Lake.", 3),
            _ih("TRAGUIN Signature Experience: Private interaction with Master Rogan Art craftsmen observing rare ancestral techniques.", 4),
            _ih("Curated by TRAGUIN Experts: Handpicked locations selected for optimized travel comfort and deep heritage representation.", 5),
            _ih("Premium Handpicked Hotels: Properties chosen specifically for high security, family-friendly layouts, and superior cuisine.", 6),
        ],
        days=[
            _day(
                1,
                "BHUJ TO HODKA / DHORDO (THE WHITE DESERT GATEWAY)",
                (
                    "Your premium Kutch Sightseeing holiday commences with a warm traditional welcome at Bhuj Airport or Railway "
                    "Station by your dedicated TRAGUIN professional chauffeur. Board your luxury air-conditioned vehicle as we drive "
                    "through changing vistas towards the gate of the Great Rann. Arrive at your ultra-luxury traditional resort or premium "
                    "Swiss tent city. Complete your seamless check-in and indulge in a lavish lunch prepared by master chefs showcasing "
                    "authentic Kutchi spices. As the afternoon sun mellows, take your first steps onto the salt-crusted plains. Experience "
                    "the emotional thrill of seeing a horizon with absolutely no borders. The white salt desert sparkles like diamonds under "
                    "the changing golden rays of sunset, creating a photography point that is globally unmatched. Return to the resort for "
                    "an evening filled with live folk music and a stargazing session."
                ),
                [
                    "Sightseeing Included: Great Rann of Kutch Border Vistas, Salt Desert Sunset Gallery.",
                    "Optional Activities: Camel Cart Ride across the salt flats, Paramotoring over the white expanse.",
                    "Evening Experience: Live Kutchi Folk Dance and Musical Performance with traditional campfire.",
                    "Overnight Stay: Handpicked Premium Resort Luxury Tents / Traditional Bhunga Suites (Hodka/Dhordo).",
                    "Meals Included: Lunch & Gourmet Dinner.",
                ],
            ),
            _day(
                2,
                "EXCURSION TO KALO DUNGAR & CRAFT VILLAGE IMMERSION",
                (
                    "Awake to a serene morning and enjoy a refreshing hot breakfast. Today we venture towards Kalo Dungar (Black Hill), "
                    "the highest point in Kutch, offering a spectacular panoramic view of the entire ecosystem, including the silent stretch "
                    "of the Indo-Pak border. Hear the captivating local legends from your expert guide at the 400-year-old Dattatreya Temple. "
                    "Descend the hills to enter Gandhi Nu Gam, a beautifully reconstructed heritage craft village. Engage in an immersive "
                    "experience with local artisans who have mastered the world-famous Rogan art, Ajrakh block printing, and intricate leather "
                    "embroidery across generations. End your evening back at the salt plains to experience a magical moonrise over the white "
                    "desert floor."
                ),
                [
                    "Sightseeing Included: Kalo Dungar Viewpoint, Dattatreya Temple, Gandhi Nu Gam Craft Village, Bhirandiyara Village.",
                    "Optional Activities: Professional family photoshoot on the salt desert with traditional costumes.",
                    "Evening Experience: Cultural interaction and luxury high-tea set up at a scenic spot.",
                    "Overnight Stay: Handpicked Premium Resort Luxury Tents / Traditional Bhunga Suites (Hodka/Dhordo).",
                    "Meals Included: Premium Breakfast, Lunch & Dinner.",
                ],
            ),
            _day(
                3,
                "HODKA / DHORDO TO MANDVI (ROYAL BEACH RETREAT)",
                (
                    "After a leisurely breakfast, bid adieu to the spellbinding white plains as our TRAGUIN Gujarat Packages route takes us "
                    "south towards the historic port town of Mandvi. This coastal escape was once the summer retreat for the Maharaos of Kutch. "
                    "Check into your premium beachside resort property and refresh yourself. In the afternoon, discover the magnificent Vijay "
                    "Vilas Palace, a grand heritage building featuring red sandstone architecture, intricate dome ceilings, and classic stone "
                    "carvings. Walk along the high corridors where several famous Bollywood films have been shot. Later, visit the private, "
                    "pristine Mandvi Beach. Walk barefoot on the clean sand, witness the rows of majestic windmills, and view a classic Arabian "
                    "Sea sunset."
                ),
                [
                    "Sightseeing Included: Vijay Vilas Palace, Mandvi Private Beach, Wind Farms Beach.",
                    "Optional Activities: Speed boating, banana boat rides, or a tour of the ancient wooden shipbuilding yard.",
                    "Evening Experience: Romantic seaside walk followed by a luxury coastal dinner experience.",
                    "Overnight Stay: Luxury Beachside Resort / Premium Heritage Palace Stay, Mandvi.",
                    "Meals Included: Premium Breakfast & Dinner.",
                ],
            ),
            _day(
                4,
                "MANDVI TO BHUJ (HISTORIC PALACES & HERITAGE DISCOVERY)",
                (
                    "Enjoy an early breakfast facing the gentle sea waves before driving back to the historic town of Bhuj. Today is dedicated "
                    "to discovering the premium cultural attractions of the city. We begin at the legendary Aina Mahal (Palace of Mirrors), "
                    "showcasing stunning European-style glasswork, royal chandeliers, and mirror plaques created in the 18th century. Right "
                    "adjacent is the majestic Prag Mahal, a grand Italian-Gothic style palace featuring a massive bell tower that offers a "
                    "panoramic look over Bhuj. Later, pay your respects at the beautifully carved Swaminarayan Temple, constructed out of pure "
                    "white marble. Spend your evening exploring the bustling local bazaars of Bhuj, famous for handloom textiles, bandhani "
                    "sarees, and traditional silver ornaments."
                ),
                [
                    "Sightseeing Included: Aina Mahal, Prag Mahal, Bhujia Fort, Shree Swaminarayan Temple, Hamirsar Lake.",
                    "Optional Activities: Guided food trail exploring famous local Kutchi Dabeli and sweet shops.",
                    "Evening Experience: Leisure stroll around Hamirsar Lake with lit fountains.",
                    "Overnight Stay: Handpicked Luxury Business/Heritage Hotel, Bhuj.",
                    "Meals Included: Premium Breakfast & Dinner.",
                ],
            ),
            _day(
                5,
                "BHUJ DEPARTURE WITH UNFORGETTABLE MEMORIES",
                (
                    "Savor a relaxed gourmet breakfast at your luxury hotel. Depending on your flight or train schedule, enjoy a morning at "
                    "leisure for last-minute souvenir purchases. Visit the Bhujodi craft village on the outskirts to pick up beautifully woven "
                    "stoles and carpets directly from traditional looms. At the designated hour, enjoy a comfortable private transfer to Bhuj "
                    "Airport or Railway Station for your onward journey home. Your premium Luxury Gujarat Holiday terminates here, leaving you "
                    "with beautiful photographs, enriched souls, and unforgettable memories curated seamlessly by TRAGUIN."
                ),
                [
                    "Sightseeing Included: Bhujodi Artisan Village Complex (Time permitting).",
                    "Transfers: Dedicated Airport/Station Drop in private premium vehicle.",
                    "Meals Included: Premium Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Gateway To Rann Resort (AC Bhunga) | Serena Beach Resort (Executive) | Regenta Resort Bhuj (Executive Room)",
                "Kutch Rann Region (2N) / Mandvi Beach (1N) / Bhuj City (1N)",
                "04 Nights",
                "Deluxe",
                "Executive Room / AC Bhunga",
                "MAPAI / Full Board at Rann",
                4,
                1,
                description=(
                    "OPTION 01 – DELUXE: Gateway To Rann Resort (AC Bhunga) (Kutch Rann Region (2N)) | "
                    "Serena Beach Resort (Executive) (Mandvi Beach (1N)) | "
                    "Regenta Resort Bhuj (Executive Room) (Bhuj City (1N)) | MAPAI / Full Board at Rann"
                ),
            ),
            _hotel(
                "Rann Resort Dholavira / Evoke Tents | The Beach at Mandvi Palace (Tent) | Hotel Prince Residency (Premium)",
                "Kutch Rann Region (2N) / Mandvi Beach (1N) / Bhuj City (1N)",
                "04 Nights",
                "Premium",
                "Premium Tent / Premium Room",
                "MAPAI / Full Board at Rann",
                4,
                2,
                description=(
                    "OPTION 02 – PREMIUM: Rann Resort Dholavira / Evoke Tents (Kutch Rann Region (2N)) | "
                    "The Beach at Mandvi Palace (Tent) (Mandvi Beach (1N)) | "
                    "Hotel Prince Residency (Premium) (Bhuj City (1N)) | MAPAI / Full Board at Rann"
                ),
            ),
            _hotel(
                "Tent City Dhordo (Premium Tents) | Serena Beach Resort (Luxury Villa) | Grand 3D Bhuj (Suite Room)",
                "Kutch Rann Region (2N) / Mandvi Beach (1N) / Bhuj City (1N)",
                "04 Nights",
                "Luxury",
                "Premium Tent / Luxury Villa / Suite",
                "MAPAI / Full Board at Rann",
                5,
                3,
                description=(
                    "OPTION 03 – LUXURY: Tent City Dhordo (Premium Tents) (Kutch Rann Region (2N)) | "
                    "Serena Beach Resort (Luxury Villa) (Mandvi Beach (1N)) | "
                    "Grand 3D Bhuj (Suite Room) (Bhuj City (1N)) | MAPAI / Full Board at Rann"
                ),
            ),
            _hotel(
                "Tent City Dhordo (Darbari Suite) | The Beach at Mandvi Palace (Royal Suite) | The Fern Residency Bhuj (Presidential Suite)",
                "Kutch Rann Region (2N) / Mandvi Beach (1N) / Bhuj City (1N)",
                "04 Nights",
                "Ultra Luxury",
                "Darbari Suite / Royal Suite / Presidential Suite",
                "Gourmet Meal Plan",
                5,
                4,
                description=(
                    "OPTION 04 – ULTRA LUXURY: Tent City Dhordo (Darbari Suite) (Kutch Rann Region (2N)) | "
                    "The Beach at Mandvi Palace (Royal Suite) (Mandvi Beach (1N)) | "
                    "The Fern Residency Bhuj (Presidential Suite) (Bhuj City (1N)) | Gourmet Meal Plan"
                ),
            ),
        ],
        inclusions=[
            _inc_included("Premium Accommodations: 04 Nights stay at handpicked, top-rated hotels and luxury desert resorts.", 1),
            _inc_included("Cuisine Plan: Daily premium breakfast & dinners at all hotels, plus full board meals during the Tent City Rann stay.", 2),
            _inc_included("Private Luxury Fleet: All transfers, long-distance touring, and local sightseeing via a dedicated chauffeur-driven Toyota Innova Crysta.", 3),
            _inc_included("TRAGUIN Welcome Kit: Premium traditional Kutchi welcome package, including local sweets and a custom destination guide.", 4),
            _inc_included("Exclusive VIP Access: Special fast-track border permit handling for hassle-free entry to the White Desert area.", 5),
            _inc_included("All-Inclusive Pricing: Driver allowances, highway tolls, parking charges, fuel fees, and all state government taxes included.", 6),
            _inc_included("24/7 Concierge Support: Dedicated TRAGUIN digital support manager available throughout the trip duration.", 7),
            _inc_excluded("Airfare, helicopter transfers, or interstate train tickets to and from Bhuj.", 8),
            _inc_excluded("Camera fees, professional monument guide fees, and entry monument tickets.", 9),
            _inc_excluded("Personal charges such as laundry, premium alcoholic beverages, room service orders, and telephone calls.", 10),
            _inc_excluded("Optional adventure sports activities (Paramotoring, ATV rides, camel safaris).", 11),
            _inc_excluded("Any mandatory gala dinner surcharges levied by resorts during Christmas, New Year, or peak festival periods.", 12),
            _inc_excluded("Anything not explicitly mentioned in the Package Inclusions section above.", 13),
        ],
    )
    return package, itinerary


def build_gj_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "GJ-005"
    tour_code = "TRAGUIN-GJ-005-PREMIUM"
    title = "Divine Statue of Unity Circuit"
    duration = "04 Nights / 05 Days"
    slug = "gj-005-divine-statue-of-unity-circuit"
    itin_slug = "gj-005-divine-statue-of-unity-itinerary"
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
            _ph("State / Country: Gujarat / India | Category: Pilgrimage & Heritage Circuit", 2),
            _ph("Destinations: Ahmedabad • Dwarka • Somnath • Statue of Unity", 3),
            _ph("Ideal for: Families, Devotees & Luxury Seekers", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: INR 48,500/- Per Person", 6),
            _ph("Travel Mode: Private FIT / Customized Luxury Group", 7),
            _ph("Vehicle: Chauffeur-Driven Premium Innova Crysta / Luxury Coach", 8),
            _ph("Meal Plan: Continental Breakfast & Premium Buffet Dinner (MAPAI)", 9),
            _ph("Route Circuit: Ahmedabad → Dwarka → Somnath → Statue of Unity → Ahmedabad", 10),
            _ph(
                "TRAGUIN Curated Experience Note: Every element handpicked by destination specialists to ensure VIP access at major temples, breathtaking scenic drives, and premium stays reflecting absolute opulence.",
                11,
            ),
            _ph(
                "Shopping: Patola Silks, Bandhani textiles, mirror-work traditional embroidery, and authentic brass handicrafts at curated local retail markets.",
                12,
            ),
            _ph(
                "Important: Standard check-in 14:00 hrs, check-out 11:00 hrs. Conservative attire recommended at places of worship. Statue of Unity entry tickets subject to slot availability—advance booking via TRAGUIN highly recommended.",
                13,
            ),
        ],
        moods=["Pilgrimage", "Heritage", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="INR 48,500/- Per Person (Premium)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Divine Statue of Unity Circuit • Pilgrimage Meets Modern Marvel",
        overview=(
            "Embark on a soul-stirring and ultra-luxurious spiritual odyssey across India's western jewel with the premier "
            "Best Gujarat Tour Package curated by TRAGUIN. This masterfully designed Gujarat Family Tour introduces you to "
            "legendary sanctuaries and architectural wonders. Experience an opulent Luxury Gujarat Holiday where ancient "
            "mythology perfectly blends with contemporary architectural triumphs.\n\n"
            "Welcome to a premium, deeply emotional journey custom-tailored for discerning travelers. This exclusive itinerary "
            "covers the ultimate highlights of India's most culturally rich state, leveraging seamless premium transfers, private "
            "guided tours, and elite hospitality. Through this signature TRAGUIN Gujarat Packages experience, travelers will "
            "discover the iconic landmarks that dominate global tourism searches.\n\n"
            "Gujarat stands as one of the most highly sought-after tourist destinations globally, offering a beautiful mosaic of "
            "monumental achievements, ancient heritage, and divine serenity. From the divine morning layout of Dwarka to the "
            "majestic light and sound spectacles near the colossal Statue of Unity, enjoy a truly Premium Gujarat Experience."
        ),
        seo_title="GJ-005 | Divine Statue of Unity Circuit | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Gujarat circuit (GJ-005 / TRAGUIN-GJ-005-PREMIUM): Dwarkadhish Temple, "
            "Bet Dwarka, Somnath Temple, Statue of Unity Viewing Gallery, Valley of Flowers, and 4-tier handpicked accommodation"
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Dwarkadhish Temple, Bet Dwarka Ferry Ride, Nageshwar Jyotirlinga, Gopi Talav, Rukmini Devi Temple.", 1),
            _ih("Kirti Mandir (Porbandar), Somnath Temple, Somnath Light & Sound Show.", 2),
            _ih("Statue of Unity Viewing Gallery, Valley of Flowers, Sardar Sarovar Dam Viewpoint, Laser Light Show.", 3),
            _ih("TRAGUIN Signature Experience: Curated VIP entries designed to save hours of wait times during main temple hours.", 4),
            _ih("Curated by TRAGUIN Experts: Handpicked local English and Hindi-speaking historians for rich storytelling at Kirti Mandir and Statue of Unity.", 5),
            _ih("Luxury Transportation: Professional, multi-lingual, verified uniform-clad chauffeurs who double as local culture curators.", 6),
        ],
        days=[
            _day(
                1,
                "AHMEDABAD TO DWARKA VIA SIGHTSEEING",
                (
                    "Arrive at Ahmedabad Airport or Railway Station where your dedicated private chauffeur welcomes you in a premium "
                    "luxury vehicle. Begin your journey toward the sacred ancient kingdom of Dwarka. This breathtaking scenic route "
                    "transitions beautifully from urban landscapes into rustic countryside views. Upon reaching Dwarka, check into your "
                    "ultra-luxury handpicked hotel. In the evening, immerse your senses in the spectacular spiritual ambiance of the "
                    "Dwarkadhish Temple, witnessing the iconic flag-changing ceremony that has drawn pilgrims for centuries. Take a "
                    "peaceful stroll along the Gomti River for stunning photography opportunities."
                ),
                [
                    "Sightseeing Included: Dwarkadhish Temple, Gomti River Ghats, Local Heritage Markets.",
                    "Evening Experience: Grand Evening Aarti and spiritual orientation session.",
                    "Overnight Stay: Premium Luxury Beach Resort, Dwarka.",
                    "Meals Included: Welcome Drink & Premium Buffer Dinner.",
                ],
            ),
            _day(
                2,
                "DWARKA SACRED CIRCUIT & LOCAL IMPRESSIONS",
                (
                    "Wake up to a gorgeous morning breakfast and set off on an extensive day of exploration. Board a scenic ferry ride "
                    "to Bet Dwarka, an island steeped in ancient legends. Visit the breathtaking Nageshwar Jyotirlinga, one of the 12 "
                    "divine shrines dedicated to Lord Shiva. Proceed to the architectural marvel of Gopi Talav and the unique Rukmini "
                    "Devi Temple, known for its incredible historical significance and beautiful intricate carvings. Spend your evening "
                    "collecting authentic souvenirs, handwoven textiles, and premium traditional Gujarati crafts at the local markets."
                ),
                [
                    "Sightseeing Included: Bet Dwarka Ferry Ride, Nageshwar Jyotirlinga, Gopi Talav, Rukmini Devi Temple.",
                    "Optional Activities: Speedboat rides around Bet Dwarka island.",
                    "Evening Experience: Relaxing sunset views over the Arabian Sea shoreline.",
                    "Overnight Stay: Premium Luxury Beach Resort, Dwarka.",
                    "Meals Included: Continental Breakfast & Gourmet Dinner.",
                ],
            ),
            _day(
                3,
                "DWARKA TO SOMNATH VIA PORBANDAR",
                (
                    "Enjoy a premium breakfast before checking out and driving along the magnificent coastal highway toward Somnath. "
                    "En route, stop at Porbandar—the historic birthplace of Mahatma Gandhi. Visit Kirti Mandir for an emotionally touching "
                    "glimpse into India's history. Continue the drive to Somnath and check into your handpicked premium hotel. As dusk "
                    "falls, visit the iconic Somnath Temple, an architectural wonder positioned directly on the ocean shore. Witness the "
                    "awe-inspiring Light & Sound Show 'Jay Somnath,' which tells the epic tale of the temple's resilience through time."
                ),
                [
                    "Sightseeing Included: Kirti Mandir (Porbandar), Somnath Temple, Triveni Sangam, Geeta Mandir.",
                    "Evening Experience: VIP seating for the world-famous Somnath Light & Sound Show.",
                    "Overnight Stay: Elite Heritage Luxury Hotel, Somnath.",
                    "Meals Included: Breakfast & Premium Dinner Buffet.",
                ],
            ),
            _day(
                4,
                "SOMNATH TO STATUE OF UNITY (KEVADIA)",
                (
                    "After an early morning breakfast, embark on a scenic transfer to Kevadia, the home of the globally renowned Statue "
                    "of Unity. Standing at a monumental 182 meters, it represents a brilliant architectural milestone and is a top-searched "
                    "landmark worldwide. Check into your ultra-luxury glamping tent or premium valley-facing resort room. Ascend to the "
                    "high-level Viewing Gallery for breathtaking panoramic views of the Satpura and Vindhya mountain ranges and the majestic "
                    "Narmada River. Conclude your day with the visually spectacular Laser Light and Sound Show depicting the life of Sardar "
                    "Vallabhbhai Patel."
                ),
                [
                    "Sightseeing Included: Statue of Unity Viewing Gallery, Valley of Flowers, Sardar Sarovar Dam Viewpoint.",
                    "Evening Experience: Spectacular Laser Light Show with high-tech projection mapping.",
                    "Overnight Stay: Premium Luxury Tent City / Exquisite Valley Resort, Kevadia.",
                    "Meals Included: Breakfast & Lavish Multi-Cuisine Dinner.",
                ],
            ),
            _day(
                5,
                "STATUE OF UNITY SIGHTSEEING TO AHMEDABAD DEPARTURE",
                (
                    "Savor a luxurious breakfast amidst pristine nature. Spend your morning exploring curated eco-tourism attractions within "
                    "the circuit, including the unique Glow Garden, the beautifully landscaped Butterfly Garden, or enjoy an optional serene "
                    "boat cruise on the Narmada River. Later, capture your final memorable photographs before driving back to Ahmedabad. "
                    "Your chauffeur will smoothly transfer you to the airport or railway station for your onward journey, leaving you with "
                    "unforgettable memories of a truly majestic holiday."
                ),
                [
                    "Sightseeing Included: Glow Garden, Cactus Garden, Unity Glow Garden photography zones.",
                    "Optional Activities: Narmada River Luxury Boat Cruise.",
                    "Meals Included: Premium Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Hawthorn Suites by Wyndham / Similar | The Fern Residency Somnath / Similar | Tent City 1 (Deluxe Tents) / Similar",
                "Dwarka (2N) / Somnath (1N) / Statue of Unity (1N)",
                "04 Nights",
                "Deluxe",
                "Standard Room / Deluxe Tent",
                "MAPAI",
                4,
                1,
                description=(
                    "OPTION 01 – DELUXE: Hawthorn Suites by Wyndham / Similar (Dwarka (2N)) | "
                    "The Fern Residency Somnath / Similar (Somnath (1N)) | "
                    "Tent City 1 (Deluxe Tents) / Similar (Statue of Unity (1N)) | MAPAI"
                ),
            ),
            _hotel(
                "Mercure Dwarka Resort / Similar | Lords Inn Somnath / Similar | The Fern Sardar Sarovar Resort / Similar",
                "Dwarka (2N) / Somnath (1N) / Statue of Unity (1N)",
                "04 Nights",
                "Premium",
                "Premium Room",
                "MAPAI",
                4,
                2,
                description=(
                    "OPTION 02 – PREMIUM: Mercure Dwarka Resort / Similar (Dwarka (2N)) | "
                    "Lords Inn Somnath / Similar (Somnath (1N)) | "
                    "The Fern Sardar Sarovar Resort / Similar (Statue of Unity (1N)) | MAPAI"
                ),
            ),
            _hotel(
                "Club Mahindra Dwarka / Similar | Somnath Sagar Premium Resort / Similar | Tent City 1 (Premium AC Tents) / Similar",
                "Dwarka (2N) / Somnath (1N) / Statue of Unity (1N)",
                "04 Nights",
                "Luxury",
                "Luxury Room / Premium AC Tent",
                "MAPAI",
                5,
                3,
                description=(
                    "OPTION 03 – LUXURY: Club Mahindra Dwarka / Similar (Dwarka (2N)) | "
                    "Somnath Sagar Premium Resort / Similar (Somnath (1N)) | "
                    "Tent City 1 (Premium AC Tents) / Similar (Statue of Unity (1N)) | MAPAI"
                ),
            ),
            _hotel(
                "Taj Amer Valley Premium Layout / Similar | The Grand Somnath Palace Suites / Similar | Statue of Unity Tent City 1 (Royal Suites)",
                "Dwarka (2N) / Somnath (1N) / Statue of Unity (1N)",
                "04 Nights",
                "Ultra Luxury",
                "Royal Suite / Palace Suite",
                "Gourmet MAPAI",
                5,
                4,
                description=(
                    "OPTION 04 – ULTRA LUXURY: Taj Amer Valley Premium Layout / Similar (Dwarka (2N)) | "
                    "The Grand Somnath Palace Suites / Similar (Somnath (1N)) | "
                    "Statue of Unity Tent City 1 (Royal Suites) (Statue of Unity (1N)) | Gourmet MAPAI"
                ),
            ),
        ],
        inclusions=[
            _inc_included("Luxury Accommodation in handpicked premium properties across the circuit.", 1),
            _inc_included("Daily Buffet Breakfasts and Premium Dinners prepared by elite culinary teams.", 2),
            _inc_included("Dedicated Chauffeur-driven air-conditioned private luxury vehicle for all transfers and sightseeing.", 3),
            _inc_included("VIP Darshan assistance and pre-booked premium entry credentials at high-demand temples.", 4),
            _inc_included("Complimentary high-tech laser show tickets at Somnath and the Statue of Unity.", 5),
            _inc_included("Welcome amenities, mineral water bottles daily, and personalized local guides at historical sites.", 6),
            _inc_included("24/7 dedicated TRAGUIN emergency customer support and travel concierge assistance.", 7),
            _inc_excluded("Airfares, domestic flights, or train ticket costs to and from Ahmedabad.", 8),
            _inc_excluded("Personal expenses such as laundry, premium telephone calls, mini-bar usage, and tips.", 9),
            _inc_excluded("Camera fees, special specialized adventure activity costs, or optional boat ride charges.", 10),
            _inc_excluded("Any meals or lunches not explicitly outlined in the designated daily meal plans.", 11),
            _inc_excluded("Travel insurance coverages and unexpected extensions due to natural delays.", 12),
        ],
    )
    return package, itinerary


def build_gj_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "GJ-006"
    tour_code = "TRAGUIN-GJ-006"
    title = "Statue of Unity & Gir Safari Express"
    duration = "04 Nights / 05 Days"
    slug = "gj-006-statue-of-unity-gir-safari-express"
    itin_slug = "gj-006-statue-of-unity-gir-safari-express-itinerary"
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
            _ph("State / Country: Gujarat / India | Category: Luxury Family Tour", 2),
            _ph("Destinations: Vadodara • Statue of Unity • Sasan Gir National Park", 3),
            _ph("Ideal for: Families & Nature Enthusiasts", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Luxury Family Tour (FIT)", 7),
            _ph("Vehicle: Private Air-Conditioned Luxury Innova Crysta / Premium Chauffeur Driven Sedan", 8),
            _ph("Meal Plan: Daily Deluxe Breakfast & Full Board (All Meals) during your wild resort stay at Sasan Gir", 9),
            _ph("Route Map: Vadodara Arrival → Kevadia (Statue of Unity) → Sasan Gir National Park → Rajkot / Diu Departure", 10),
            _ph("TRAGUIN Signature Experience: Curated by TRAGUIN Experts, this premium journey features guaranteed pre-booked private open-gypsy safari passes to avoid lines, elite resort upgrades, and priority access tickets to ensure maximum comfort and safety for your entire family group.", 11),
            _ph("Shopping: Discover exquisite traditional handlooms, local artisan crafts, and authentic souvenirs from all over India. Sasan Gir Markets: Purchase pure organic forest honey, authentic mango pulps (seasonal), and beautiful local tribal embroidery items.", 12),
            _ph("Important: Standard check-in is at 14:00 hours; early priority check-in is subject to TRAGUIN partner availability. Safari Regulations: Sasan Gir jungle safari permits are non-refundable and require original government identity profiles during verification check gates. Advance Bookings: We highly recommend completing advance bookings at least 45-60 days prior to secure premium safari slots seamlessly.", 13)
        ],
        moods=["Wildlife", "Heritage", "Family"],
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
        tagline="Statue of Unity & Gir Safari Express • Heritage Meets Wilderness",
        overview=(
            "Welcome to an unforgettable journey mapping the heritage and majestic wilderness of Western India. "
            "This high-end luxury proposal curated by TRAGUIN masterfully combines the architectural wonders of "
            "the world's tallest monument with the raw, breathtaking landscapes of Sasan Gir. Cherish premium "
            "stays, curated experiences, and absolute comfort as you witness the timeless pride of Gujarat with "
            "your family.\n\n"
            "Gujarat is a land of fascinating cultural history, vibrant colors, and unparalleled wildlife highlights, "
            "making it an excellent match for a Gujarat Family Tour or a custom Luxury Gujarat Holiday. Travelers "
            "globally look for the Best Gujarat Tour Package to explore iconic attractions that effortlessly merge "
            "modern engineering wonders with untouched wilderness ecosystems. The most searched experiences include "
            "marveling at the colossal 182-meter Statue of Unity at Kevadia and embarking on an adrenaline-inducing "
            "open-gypsy jungle safari inside Sasan Gir National Park—the world's last remaining bastion of the "
            "majestic Asiatic Lion.\n\n"
            "TRAGUIN Curated Touch: This Premium Gujarat Experience is complete with guaranteed VIP entry access "
            "tickets to the Statue of Unity viewing gallery, a private customized wildlife safari booking, "
            "handpicked hotels, and 24/7 dedicated local assistance."
        ),
        seo_title="GJ-006 | Statue of Unity & Gir Safari Express | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Gujarat package (GJ-006 / TRAGUIN-GJ-006): Valley of Flowers, Statue of Unity Viewing Gallery, Sasan Gir jungle safari, Devalia Safari Park, and 4-tier handpicked accommodation"
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Valley of Flowers, Glow Garden, and Laser Light Show.", 1),
            _ih("Monument Viewing Gallery, Museum, Jungle Safari Complex, Narmada Cruise.", 2),
            _ih("Rural landscape views, leisure evening check-in.", 3),
            _ih("TRAGUIN Signature Experience: Curated by TRAGUIN Experts, this premium journey features guaranteed pre-booked private open-gypsy safari passes to avoid lines, elite resort upgrades, and priority access tickets to ensure maximum comfort and safety for your entire family group.", 4),
            _ih("Curated by TRAGUIN Experts: Handpicked luxury hotels and seamless ground logistics", 5),
            _ih("Premium Handpicked Hotels: Properties certified for elite hospitality and safety standards", 6)
        ],
        days=[
            _day(
                1,
                "ARRIVAL VADODARA TO KEVADIA",
                (
                    "Arrive at Vadodara Airport or Station where your dedicated private luxury vehicle and professional tour representative await you. Drive along scenic routes towards Kevadia, the dedicated eco-tourism hub of India. Check in seamlessly to your premium luxury tented resort overlooking Narmada river. In the afternoon, explore the Valley of Flowers and witness the mesmerizing Statue of Unity Sightseeing experience. As evening falls, witness the spectacular high-tech Laser Light and Sound Show narrating the life of Sardar Vallabhbhai Patel."
                ),
                [
                    "Sightseeing Included: Valley of Flowers, Glow Garden, and Laser Light Show.",
                    "Evening Experience: Stroll through the magical illumination patterns at the Unity Glow Garden.",
                    "Overnight Stay: Premium Handpicked Luxury Resort / Tent City, Kevadia.",
                    "Meals Included: Welcome Drink & Gourmet Buffet Dinner."
                ],
            ),
            _day(
                2,
                "KEVADIA EXPLORATION",
                (
                    "Savor a luxurious morning breakfast before heading directly to the monument base. Enjoy priority VIP lift access up to the 153-meter high Viewing Gallery, nestled inside the chest of the monument, for sweeping views of the Vindhya-Satpura mountain ranges and the colossal Sardar Sarovar Dam. Later, experience an immersive excursion through the state-of-the-art Kevadia Jungle Safari park, a uniquely designed zoo housing exotic wildlife from across three continents. Conclude your evening with a peaceful private boat cruise down the pristine Narmada waters."
                ),
                [
                    "Sightseeing Included: Monument Viewing Gallery, Museum, Jungle Safari Complex, Narmada Cruise.",
                    "Photography Points: Majestic panoramic captures from the high-altitude viewing deck.",
                    "Overnight Stay: Premium Luxury Resort, Kevadia.",
                    "Meals Included: Full Buffet Breakfast & Dinner."
                ],
            ),
            _day(
                3,
                "KEVADIA TO SASAN GIR NATIONAL PARK",
                (
                    "Bid farewell to the river plains as you embark on a comfortable private transit across central plains toward the untamed forests of Sasan Gir. This drive offers an authentic look at the traditional countryside and local communities of the state. Arrive by afternoon at your ultra-luxury jungle wilderness resort. Spend your evening relaxing by the poolside or listening to ancestral tales of the Maldhari tribe over a bonfire curated exclusively for your family."
                ),
                [
                    "Sightseeing Included: Rural landscape views, leisure evening check-in.",
                    "Optional Activities: Guided nature trail walks around the resort borders.",
                    "Overnight Stay: Handpicked Wilderness Luxury Resort, Sasan Gir.",
                    "Meals Included: Breakfast, Lunch & Gourmet Resort Dinner."
                ],
            ),
            _day(
                4,
                "SASAN GIR WILDLIFE SAFARI",
                (
                    "Wake up early to the calls of the wild. Board your pre-booked, private open-top 4x4 Gypsy for an exhilarating morning tracking safari inside the core area of Sasan Gir National Park. Accompanied by an expert naturalist tracker, discover pristine teak forests and keep your cameras ready to spot the absolute pride of Asia—the wild Asiatic Lion. Return to the resort for a hearty lunch. In the afternoon, visit the Gir Interpretation Zone at Devalia to explore diverse wildlife conservation initiatives and spot leopards or marsh crocodiles."
                ),
                [
                    "Sightseeing Included: Morning Jungle Safari, Devalia Safari Park, Somnath Temple (Optional evening excursion).",
                    "Immersive Experiences: High-end wildlife tracking session with a certified regional naturalist guide.",
                    "Overnight Stay: Premium Wilderness Luxury Resort, Sasan Gir.",
                    "Meals Included: Full Board (Breakfast, Lunch & Dinner Included)."
                ],
            ),
            _day(
                5,
                "SASAN GIR TO DEPARTURE STATION / AIRPORT",
                (
                    "Indulge in a late gourmet breakfast amidst the tranquil canopy of the jungle. Pack your bags with hand- woven regional fabrics and memorable photographic frames. Your luxury vehicle will drive you comfortably to Rajkot Airport or Diu Airport for your onward flight back home. Your unmatched Statue of Unity & Gir Safari holiday concludes with beautiful, lasting family memories."
                ),
                [
                    "Transfers Included: Private Chauffeur-driven Airport drop-off.",
                    "Meals Included: Full Breakfast."
                ],
            )
        ],
        hotels=[
            _hotel("Tent City 1 (Premium Tents) / The Fern Gir Forest Resort", "Kevadia / Sasan Gir", "04 Nights", "Deluxe", "Premium Tents / Standard Room", "Kevadia: MAPAI | Gir: APAI", 4, 1),
            _hotel("The Fern Sardar Sarovar Resort / Woods at Sasan (Luxury Studio)", "Kevadia / Sasan Gir", "04 Nights", "Premium", "Deluxe Room / Luxury Studio", "Kevadia: MAPAI | Gir: APAI", 5, 2),
            _hotel("Statue of Unity Tent City 1 (Royal Villas) / Aramness Gir (Luxury Kothi)", "Kevadia / Sasan Gir", "04 Nights", "Luxury", "Royal Villas / Luxury Kothi", "Kevadia: APAI | Gir: Gourmet APAI", 5, 3),
            _hotel("The Grand Mercure Kevadia (Luxury Suite) / Taj Safari - The Gateway Hotel Gir", "Kevadia / Sasan Gir", "04 Nights", "Ultra Luxury", "Luxury Suite / Premium Safari Room", "Ultra Luxury Custom Board Plan", 5, 4)
        ],
        inclusions=[
            _inc_included("Accommodation: Premium stays at handpicked luxury hotels and safari resorts across all destinations.", 1),
            _inc_included("Meals: Breakfast & Dinners at Kevadia, All gourmet meals (Breakfast, Lunch, Dinner) included at Sasan Gir.", 2),
            _inc_included("Transfers & Sightseeing: Dedicated private Luxury Innova Crysta with an experienced professional chauffeur.", 3),
            _inc_included("TRAGUIN Support: 24/7 priority concierge support line backed by our specialized vacation coordinators.", 4),
            _inc_included("Complimentary Tickets: Guaranteed VIP access entries to the Statue of Unity Observation Deck.", 5),
            _inc_included("Welcome Amenities: Refreshing regional fruit basket, specialized travel kits, and purified mineral water provisions.", 6),
            _inc_excluded("Flights, rail connections, or long-distance domestic travel fare.", 7),
            _inc_excluded("Optional camera fees or monument entrances not specified in the inclusions list.", 8),
            _inc_excluded("Personal expense accounts like laundry services, phone premium tabs, or specialized porter tips.", 9),
            _inc_excluded("Optional extension excursions or out-of-itinerary luxury private vehicle transfers.", 10)
        ],
    )
    return package, itinerary


def build_gj_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "GJ-007"
    tour_code = "TRAGUIN-GJ-007"
    title = "Ahmedabad Heritage & Science City Premium Vacation"
    duration = "02 Nights / 03 Days"
    slug = "gj-007-ahmedabad-heritage-science-city-premium-vacation"
    itin_slug = "gj-007-ahmedabad-heritage-science-city-premium-vacation-itinerary"
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
            _ph("State / Country: Gujarat / India | Category: Family / Luxury Heritage", 2),
            _ph("Destinations: Ahmedabad • Science City • Adalaj", 3),
            _ph("Ideal for: Family Tour & Tech Enthusiasts", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Luxury Family Tour (FIT)", 7),
            _ph("Vehicle: Private Air-Conditioned Luxury Innova Crysta (Chauffeur Driven)", 8),
            _ph("Meal Plan: Modified American Plan (Gourmet Breakfasts & Specialized Dinners)", 9),
            _ph("Route Map: Ahmedabad Airport Arrival → Heritage Old Quarter → Sabarmati Ashram → Futuristic Science City → Adalaj Stepwell → Departure", 10),
            _ph("TRAGUIN Signature Experience: Curated by TRAGUIN Experts, this package ensures absolute peace of mind. Benefit from skip-the-line entries at scientific parks, premium chauffeured luxury transportation, and highly secure family protocols across your stay.", 11),
            _ph("Shopping: Shop for authentic *Chaniya Cholis*, hand-embroidered wall-hangings, and traditional silver jewelry. Bandhej & Patola Hubs: Buy signature tie-dye fabrics and pure silk Patola sarees. • •", 12),
            _ph("Important: VIP gallery entries are subject to immediate pre-booking schedules. Early confirmation is highly advised. Transport Rules: High-end sedans and SUVs adhere strictly to regional highway timelines. Local toll taxes and parking charges are included. Dry State Regulation: Gujarat is a liquor-regulated dry state. Foreign and out-of-state travelers can apply online for tourist permit facilities.", 13)
        ],
        moods=["Heritage", "Family", "Culture"],
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
        tagline="Ahmedabad Heritage & Science City Premium Vacation • UNESCO Meets Innovation",
        overview=(
            "Step into India's first UNESCO World Heritage City, where ancient craftsmanship seamlessly merges "
            "with futuristic innovation. This Premium Gujarat Experience, meticulously crafted by TRAGUIN, offers "
            "an opulent escape into history, culture, and science. From the stone-carved lattices of legendary "
            "mosques to the mind-bending galleries of Science City, treat your loved ones to a seamless, luxurious "
            "holiday filled with breathtaking landscapes and handpicked hotels.\n\n"
            "Ahmedabad is a timeless treasure trove featuring unmatched living history, world-renowned street food, "
            "and modern architectural marvels. Families searching for the ultimate Gujarat Family Tour or a memorable "
            "Gujarat Honeymoon Package will find the perfect mix of experiences here. Our exclusive TRAGUIN Gujarat "
            "Packages spotlight the absolute Top Tourist Places in Gujarat, including the Adalaj Stepwell, Sabarmati "
            "Riverfront, and Science City.\n\n"
            "TRAGUIN Curated Touch: This signature family holiday balances education, historical storytelling, and "
            "private comforts with pre-booked VIP tickets to the Robotics & Aquatic galleries and custom guided walkovers."
        ),
        seo_title="GJ-007 | Ahmedabad Heritage & Science City Premium Vacation | TRAGUIN",
        seo_description=(
            "Premium 02 Nights / 03 Days Gujarat package (GJ-007 / TRAGUIN-GJ-007): Sidi Saiyyed Mosque, Sabarmati Ashram, Aquatic Gallery, Robotics Gallery, Adalaj Stepwell, and 4-tier handpicked accommodation"
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Sidi Saiyyed Mosque, Sabarmati Ashram, Akshardham Temple (Optional).", 1),
            _ih("Aquatic Gallery, Robotics Gallery, Space Hall, IMAX 3D, Sabarmati Riverfront.", 2),
            _ih("Adalaj Stepwell, Law Garden Artisan Market.", 3),
            _ih("TRAGUIN Signature Experience: Curated by TRAGUIN Experts, this package ensures absolute peace of mind. Benefit from skip-the-line entries at scientific parks, premium chauffeured luxury transportation, and highly secure family protocols across your stay.", 4),
            _ih("Curated by TRAGUIN Experts: Handpicked luxury hotels and seamless ground logistics", 5),
            _ih("Premium Handpicked Hotels: Properties certified for elite hospitality and safety standards", 6)
        ],
        days=[
            _day(
                1,
                "AHMEDABAD ARRIVAL & HERITAGE",
                (
                    "Arrive at Sardar Vallabhbhai Patel International Airport, where a dedicated luxury private vehicle awaits you. Check into your ultra-premium hotel with zero wait-time. Post-lunch, embark on your Gujarat Sightseeing journey. Dive into the historical old quarter to witness the beautiful stone architecture of Sidi Saiyyed Mosque with its legendary tree-of-life lattice window. Later, absorb peaceful moments at Sabarmati Ashram along the riverbank, tracing Mahatma Gandhi's steps before an unforgettable culinary evening."
                ),
                [
                    "Sightseeing Included: Sidi Saiyyed Mosque, Sabarmati Ashram, Akshardham Temple (Optional).",
                    "Evening Experience: Indulge in an exclusive traditional multi-course Gujarati Thali at a fine-dining heritage restaurant.",
                    "Overnight Stay: Handpicked Luxury 5-Star Hotel, Ahmedabad.",
                    "Meals Included: Welcome Drink & Festive Welcome Dinner."
                ],
            ),
            _day(
                2,
                "FUTURISTIC AHMEDABAD",
                (
                    "After a lavish gourmet breakfast, spend the day exploring India’s premier technical wonderland: the Ahmedabad Science City. Enjoy skip-the-line executive entries into the Aquatic Gallery, India’s top-tier inland aquarium showcasing exotic marine life through an immersive walkthrough tunnel. Next, visit the state-of-the-art Robotics Gallery to see automated humanoids, manufacturing units, and robot-led music shows. End the night with a scenic breeze across the modern Sabarmati Riverfront Promenade."
                ),
                [
                    "Sightseeing Included: Aquatic Gallery, Robotics Gallery, Space Hall, IMAX 3D, Sabarmati Riverfront.",
                    "Optional Activities: Ride the Science City high-tech simulators or explore the serene nature park.",
                    "Photography Points: Under-water oceanic tunnel view and the interactive cybernetic installations.",
                    "Overnight Stay: Handpicked Luxury 5-Star Hotel, Ahmedabad.",
                    "Meals Included: Buffet Breakfast & Premium International Dinner."
                ],
            ),
            _day(
                3,
                "ADALAJ STEPWELL & DEPARTURE",
                (
                    "Conclude your luxury holiday with a trip to the magnificent 15th-century Adalaj Stepwell (Rudabai Stepwell). Walk through its multi-story underground pavilions carved with classic floral icons, capturing stunning geometric photos. Afterwards, stop by the Law Garden handicraft avenues to purchase souvenir textiles before arriving back at the airport for your onward flight with unforgettable memories of your premium tour."
                ),
                [
                    "Sightseeing Included: Adalaj Stepwell, Law Garden Artisan Market.",
                    "Food Suggestions: Savor fresh local delights like *Khandvi* and artisanal saffron *Shrikhand* at select premium cafes.",
                    "Meals Included: Full Buffet Breakfast."
                ],
            )
        ],
        hotels=[
            _hotel("Lemon Tree Premier, Ahmedabad", "Ahmedabad", "02 Nights", "Deluxe", "Deluxe King Room", "MAPAI Plan", 4, 1),
            _hotel("Hyatt Regency, Ashram Road", "Ahmedabad", "02 Nights", "Premium", "Club Room", "MAPAI Plan", 5, 2),
            _hotel("Courtyard by Marriott, Sindhu Bhavan Road", "Ahmedabad", "02 Nights", "Luxury", "Executive Heritage Room", "MAPAI Plan", 5, 3),
            _hotel("Taj Skyline, Ahmedabad", "Ahmedabad", "02 Nights", "Ultra Luxury", "Luxury Suite Room", "Gourmet Meal Plan", 5, 4)
        ],
        inclusions=[
            _inc_included("Accommodation: 02 Nights premium stays at highly-rated handpicked hotels.", 1),
            _inc_included("Meals: Daily upscale breakfast spreads and personalized premium dinners.", 2),
            _inc_included("Transfers & Sightseeing: All commutes via an executive air-conditioned Luxury Innova Crysta.", 3),
            _inc_included("Welcome Amenities: Personalized travel packs, local maps, and high-quality packaged mineral water.", 4),
            _inc_included("Complimentary Experiences: VIP Entry passes to the Aquatic & Robotics Galleries at Science City.", 5),
            _inc_included("TRAGUIN Support: 24/7 dedicated local tour manager support for flawless ground logistics.", 6),
            _inc_excluded("Airfare or interstate train ticketing charges.", 7),
            _inc_excluded("Early check-ins or late check-outs not authorized by hotel policies.", 8),
            _inc_excluded("Individual expenses such as laundry, room service, souvenirs, and camera ticketing fees.", 9),
            _inc_excluded("Guide tipping expenses.", 10)
        ],
    )
    return package, itinerary


def build_gj_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "GJ-008"
    tour_code = "TRAGUIN-GJ-008"
    title = "Complete Vibrant Gujarat Mega Tour"
    duration = "09 Nights / 10 Days"
    slug = "gj-008-complete-vibrant-gujarat-mega-tour"
    itin_slug = "gj-008-complete-vibrant-gujarat-mega-tour-itinerary"
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
            _ph("State / Country: Gujarat / India | Category: Family Tour / Luxury Vacation", 2),
            _ph("Destinations: Ahmedabad • Statue of Unity • Bhuj • Rann of Kutch • Dwarka • Somnath", 3),
            _ph("Ideal for: Families, Couples & Culture Seekers", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Luxury Grand Circuit (FIT)", 7),
            _ph("Vehicle: Dedicated Luxury Chauffeur- Driven AC Innova Crysta", 8),
            _ph("Meal Plan: Modified American Plan (Buffet Breakfast & Fine Dining Dinners)", 9),
            _ph("Route Map: Ahmedabad → Kevadia (Statue of Unity) → Bhuj → White Rann of Kutch → Dwarka → Somnath → Ahmedabad Drop", 10),
            _ph("TRAGUIN Signature Experience: Curated by TRAGUIN Experts specifically for families who value slow- paced luxury and immersive cultural discovery. Benefit from priority checking across all premium partner hotels, signature local food tastings, and premium high-safety luxury transportation throughout.", 11),
            _ph("Shopping: Authentic Gujarati handicrafts and regional souvenirs", 12),
            _ph("Important: Standard hotel check-in time is 14:00 hrs; early check-in is strictly subject to room availability. Desert Operations: Rann of Kutch premium tents are highly requested; advance bookings are strongly recommended. Dress Code: Traditional or modest attire is requested when visiting the holy shrines of Dwarka and Somnath.", 13)
        ],
        moods=["Heritage", "Spiritual", "Wildlife"],
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
        tagline="Complete Vibrant Gujarat Mega Tour • Legends, Deserts & Spirituality",
        overview=(
            "Gujarat is a marvelous tapestry of pristine history, spiritual awakening, and dramatic topography, making a Gujarat Family Tour one of the highly ranked journeys across India. Whether seeking a deeply romantic Gujarat Honeymoon Package or an elegant multigenerational exploration, the state delivers iconic attractions that cater flawlessly to luxury expectations. From the UNESCO World Heritage monuments of historical Ahmedabad to the sacred chanting bells of Dwarka and Somnath temples, this Premium Gujarat Experience captures top-searched destinations. Discover popular Instagram locations like the surreal sunset at the White Rann of Kutch and the colossal Statue of Unity. Our selection of premium stays ensures complete comfort alongside mesmerizing cultural highlights.\n\n"
                        "TRAGUIN Curated Touch: Includes VIP fast-track entry to the Statue of Unity, premium tent accommodation at the White Desert, private heritage walking companions, and signature regional culinary guides."
        ),
        seo_title="GJ-008 | Complete Vibrant Gujarat Mega Tour | TRAGUIN",
        seo_description=(
            "Premium 09 Nights / 10 Days Gujarat package (GJ-008 / TRAGUIN-GJ-008): Statue of Unity, White Rann of Kutch, Dwarka, Somnath, Beyt Dwarka, and 4-tier premium hotels"
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Sabarmati Ashram, Adalaj Stepwell, Akshardham Temple (Grand Laser Show).", 1),
            _ih("Statue of Unity Viewing Gallery, Valley of Flowers, Cactus Garden.", 2),
            _ih("Scenic transit, evening orientation of Bhuj markets.", 3),
            _ih("TRAGUIN Signature Experience: Curated by TRAGUIN Experts specifically for families who value slow- paced luxury and immersive cultural discovery. Benefit from priority checking across all premium partner hotels, signature local food tastings, and premium high-safety luxury transportation throughout.", 4),
            _ih("Curated by TRAGUIN Experts: Handpicked luxury hotels and seamless ground logistics", 5),
            _ih("Premium Handpicked Hotels: Properties certified for elite hospitality and safety standards", 6)
        ],
        days=[
            _day(
                1,
                "ARRIVAL IN AHMEDABAD",
                (
                    "Arrive at Ahmedabad International Airport where your elite TRAGUIN tour ambassador welcomes you. Transfer in a private luxury vehicle to your handpicked premium hotel. Following a seamless check-in, begin a leisurely tour of the Top Tourist Places in Gujarat. Visit the serene Sabarmati Ashram, nestled on the quiet banks of the River Sabarmati, followed by the marvelously carved Adalaj Stepwell. Spend a relaxing evening absorbing the local culture."
                ),
                [
                    "Sightseeing Included: Sabarmati Ashram, Adalaj Stepwell, Akshardham Temple (Grand Laser Show).",
                    "Food Suggestions: Enjoy an authentic luxury Gujarati Thali at a heritage rooftop restaurant.",
                    "Overnight Stay: Premium Luxury Hotel, Ahmedabad.",
                    "Meals Included: Welcome Drink & Gourmet Dinner."
                ],
            ),
            _day(
                2,
                "AHMEDABAD TO KEVADIA (STATUE OF UNITY)",
                (
                    "After a delicious early breakfast, travel via a highly comfortable, scenic route to Kevadia, the home of the globally renowned Statue of Unity. Standing proudly at 182 meters, this engineering feat is dedicated to Sardar Vallabhbhai Patel. Check in to your ultra-luxury nature resort. In the afternoon, utilize your pre- booked VIP tickets to access the viewing gallery for breathtaking panoramic views of the Narmada River and Vindhyachal mountain ranges."
                ),
                [
                    "Sightseeing Included: Statue of Unity Viewing Gallery, Valley of Flowers, Cactus Garden.",
                    "Evening Experience: Witness the awe-inspiring high-tech Sound and Light Projection Show.",
                    "Overnight Stay: Premium Luxury Tent/Resort, Kevadia.",
                    "Meals Included: Buffet Breakfast & Multi-cuisine Dinner."
                ],
            ),
            _day(
                3,
                "KEVADIA TO BHUJ",
                (
                    "Enjoy a relaxed morning breakfast overlooking the hills before embarking on a private journey towards Bhuj, the royal gateway to the mystical Kutch district. This drive treats you to altering geological vistas as you head into Western Gujarat. Upon arrival in the evening, check into your heritage boutique hotel and relax."
                ),
                [
                    "Sightseeing Included: Scenic transit, evening orientation of Bhuj markets.",
                    "Photography Points: Gorgeous rural sunset viewpoints along the Kutch transit highway.",
                    "Overnight Stay: Handpicked Premium Resort, Bhuj.",
                    "Meals Included: Buffet Breakfast & Dinner."
                ],
            ),
            _day(
                4,
                "BHUJ SIGHTSEEING TO WHITE RANN OF KUTCH",
                (
                    "Discover the spectacular architecture of Aina Mahal and Prag Mahal in Bhuj. Post lunch, drive deep into the ethereal landscape of the Great Rann of Kutch. Check into your ultra-luxury AC tented villa. As evening approaches, embark on an unforgettable camel-cart safari onto the white salt desert to witness a dramatic, multi-hued sunset that ranks among the world's most sought-after travel sights."
                ),
                [
                    "Sightseeing Included: Aina Mahal, Prag Mahal, Bhujodi Craft Village, White Desert Sunset.",
                    "Evening Experience: Live folk music and cultural dances under the stars at the desert camp.",
                    "Overnight Stay: Premium Luxury Tents, White Rann.",
                    "Meals Included: Breakfast, Lunch & Traditional Kutch Dinner."
                ],
            ),
            _day(
                5,
                "WHITE RANN TO MANDVI BEACH EXPLORATION",
                (
                    "Wake up early for a spectacular sunrise over the salt plains. Following a rich breakfast, drive towards the pristine coastal town of Mandvi. Visit the magnificent Vijay Vilas Palace, a popular Instagram location featuring exquisite Rajput architecture and sprawling private beaches. Walk along the soft sands of Mandvi Beach as the sun sets over the Arabian Sea."
                ),
                [
                    "Sightseeing Included: Vijay Vilas Palace, Shyamji Krishna Varma Memorial, Mandvi Private Beach.",
                    "Optional Activities: Water sports and gentle camel rides along the Mandvi coastline.",
                    "Overnight Stay: Premium Beachfront Luxury Resort, Mandvi / Bhuj.",
                    "Meals Included: Breakfast & Coastal-Inspired Dinner."
                ],
            ),
            _day(
                6,
                "BHUJ TO DWARKA",
                (
                    "Today, your premium private transfer takes you down to the highly revered coastline of Saurashtra towards the sacred ancient city of Dwarka. Cross the iconic Gulf of Kutch during this relaxing journey. Arrive in Dwarka by evening, check into your luxury sea-facing hotel, and feel the spiritual energy of this timeless kingdom."
                ),
                [
                    "Sightseeing Included: Dwarka Coastal Route, evening leisure arrival.",
                    "Evening Experience: Participate in a private, soulful evening Aarti ritual at the majestic Dwarkadhish Temple.",
                    "Overnight Stay: Premium Luxury Hotel, Dwarka.",
                    "Meals Included: Breakfast & Satvik Fine-Dining Dinner."
                ],
            ),
            _day(
                7,
                "DWARKA & BEYT DWARKA FULL DAY TOUR",
                (
                    "Embark on a beautifully curated spiritual exploration. Travel to Okha port and board a private chartered boat to Beyt Dwarka island. Visit the ancient temple ruins and modern marvels. On your return, admire the architectural grandeur of Sudama Setu and the sacred Nageshwar Jyotirlinga, one of the 12 revered holy shrines in India."
                ),
                [
                    "Sightseeing Included: Dwarkadhish Temple, Beyt Dwarka, Nageshwar Jyotirlinga, Rukmini Devi Temple, Gopi Talav.",
                    "Immersive Experiences: Walk along the scenic Sudama Setu suspension bridge over the Gomti River.",
                    "Overnight Stay: Premium Luxury Hotel, Dwarka.",
                    "Meals Included: Breakfast & Gourmet Dinner."
                ],
            ),
            _day(
                8,
                "DWARKA TO SOMNATH via PORBANDAR",
                (
                    "Drive along the beautiful coastal highway towards Somnath. En route, stop at Porbandar, the historic birthplace of Mahatma Gandhi. Tour Kirti Mandir before proceeding to the world-famous Somnath Temple. Standing elegantly on the shore of the Arabian Sea, this historic monument represents resilience and spiritual grandeur."
                ),
                [
                    "Sightseeing Included: Kirti Mandir (Porbandar), Somnath Jyotirlinga Temple, Triveni Sangam, Geeta Mandir.",
                    "Evening Experience: Highly acclaimed Sound & Light Show highlighting Somnath's glorious history.",
                    "Overnight Stay: Handpicked Luxury Resort, Somnath.",
                    "Meals Included: Breakfast & Festive Dinner."
                ],
            ),
            _day(
                9,
                "SOMNATH TO AHMEDABAD via JUNAGADH",
                (
                    "After breakfast, begin your return journey towards Ahmedabad. Stop at historical Junagadh to view the majestic ancient Uparkot Fort and the stunningly designed Mahabat Maqbara, a structural masterpiece. Arrive back in the vibrant city of Ahmedabad in the evening for final souvenir shopping and a farewell celebration."
                ),
                [
                    "Sightseeing Included: Uparkot Fort, Mahabat Maqbara, Law Garden Night Market.",
                    "Shopping Highlight: Buy authentic Patola silk sarees, Bandhani handlooms, and traditional mirror-work garments.",
                    "Overnight Stay: Premium Luxury Hotel, Ahmedabad.",
                    "Meals Included: Breakfast & Farewell Dinner."
                ],
            ),
            _day(
                10,
                "DEPARTURE FROM AHMEDABAD",
                (
                    "Savor a relaxed gourmet breakfast at your hotel. Enjoy a final morning of leisure before your luxury private vehicle arrives to transfer you smoothly to Ahmedabad International Airport. Your unforgettable TRAGUIN Gujarat Package concludes here, leaving you with timeless memories of a premium, perfectly managed holiday."
                ),
                [
                    "Transfers Included: Private Airport/Station VIP Drop-off.",
                    "Meals Included: Full Buffet Breakfast."
                ],
            )
        ],
        hotels=[
            _hotel("Hyatt Regency / Tent City 2", "Ahmedabad / Kevadia", "09 Nights", "Deluxe", "Deluxe Room / Standard Tent", "MAP Plan (Breakfast + Dinner)", 4, 1),
            _hotel("Taj Skyline / SOU Eco Camp", "Ahmedabad / Kevadia", "09 Nights", "Premium", "Club Room / Premium Tent", "MAP Plan (Breakfast + Dinner)", 5, 2),
            _hotel("The Leela Gandhinagar / Tent City 1 Luxury", "Ahmedabad / Kevadia", "09 Nights", "Luxury", "Executive Room / Luxury Tent", "MAP Luxury Gourmet Plan", 5, 3),
            _hotel("ITC Narmada / Statue of Unity Grand Suites", "Ahmedabad / Kevadia", "09 Nights", "Ultra Luxury", "Grand Suite / Royal Villa", "Royal Heritage Dining All-Inclusive", 5, 4)
        ],
        inclusions=[
            _inc_included("Accommodation: 09 Nights stay at handpicked premium luxury properties and tented desert villas.", 1),
            _inc_included("Meals: Daily premium breakfast buffet and 09 curated dinners at elite hotel restaurants.", 2),
            _inc_included("Transfers & Sightseeing: All sightseeing and long-distance travel in a private AC Innova Crysta with a professional chauffeur.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated virtual concierge and certified local destination handlers.", 4),
            _inc_included("Complimentary Experiences: Private chartered boat ride to Beyt Dwarka and VIP fast-track entry to the Statue of Unity.", 5),
            _inc_included("Taxes & Fees: All current toll taxes, state permits, parking fees, and fuel allowances included.", 6),
            _inc_excluded("Domestic or international airfare / train tickets to Ahmedabad.", 7),
            _inc_excluded("Any historical monument entry tickets or professional camera permits not mentioned.", 8),
            _inc_excluded("Personal expenses such as laundry, long-distance phone calls, liquor, or porterage tips.", 9),
            _inc_excluded("Optional activities, water sports, or independent vehicle usage during leisure periods.", 10)
        ],
    )
    return package, itinerary


def build_gj_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "GJ-009"
    tour_code = "TRAGUIN-GJ-009"
    title = "Statue of Unity & Gir Safari Express"
    duration = "04 Nights / 05 Days"
    slug = "gj-009-statue-of-unity-gir-safari-express"
    itin_slug = "gj-009-statue-of-unity-gir-safari-express-itinerary"
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
            _ph("State / Country: Gujarat / India | Category: Family Vacation / Luxury Wildlife", 2),
            _ph("Destinations: Statue of Unity • Sasan Gir National Park", 3),
            _ph("Ideal for: Families, Couples & Photographers", 4),
            _ph("Best season: November to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Luxury Family Tour (FIT)", 7),
            _ph("Vehicle: Private Air-Conditioned Luxury Innova Crysta / Premium Chauffeur Driven Sedan", 8),
            _ph("Meal Plan: Modified American Plan (All Daily Premium Breakfasts & Dinners Included)", 9),
            _ph("Route Map: Vadodara Arrival → Kevadia (Statue of Unity) → Sasan Gir National Park → Rajkot / Diu Departure", 10),
            _ph("TRAGUIN Signature Experience: Curated by our leading travel planners, this itinerary balances luxury transportation and handpicked hotels with flawless seamless execution. Experience stress-free wildlife bookings, express entry management at global heritage monuments, and localized insider dining recommendations for an extraordinary holiday.", 11),
            _ph("Shopping: Purchase handlooms and authentic local handicrafts collected from diverse tribal communities across India. •", 12),
            _ph("Important: Sasan Gir forest safaris are regulated by government authorities and require mandatory permit slot bookings up to 30–45 days in advance. Hotel Policies: Standard check-in time across luxury resorts is 14:00 hrs and check-out is 11:00 hrs. Weather & Safety: Morning safaris can be crisp and chilly; carrying a light jacket or windcheater is highly recommended for complete family comfort.", 13)
        ],
        moods=["Wildlife", "Heritage", "Family"],
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
        tagline="Statue of Unity & Gir Safari Express • Monuments & Majestic Lions",
        overview=(
            "Gujarat stands as one of India's most dynamic and sought-after luxury travel destinations, making the Best Gujarat Tour Package an exceptional choice for travelers worldwide. Whether you are seeking an adventurous Gujarat Family Tour or a beautifully romantic Gujarat Honeymoon Package, this state pairs rich cultural history with breathtaking landscapes. From exploring iconic attractions like the world-record-breaking Statue of Unity to taking part in highly searched wildlife experiences inside Sasan Gir, our Luxury Gujarat Holiday brings you unparalleled comfort. Discover popular Instagram locations including the vibrant Laser Light and Sound show at Kevadia and capture majestic shots of wild lions in their natural habitat. With premium handpicked hotels and exclusive curated tours, our TRAGUIN Gujarat Packages are tailored to redefine your next vacation.\n\n"
                        "TRAGUIN Curated Touch: This custom luxury holiday ensures priority access tickets to the Statue of Unity, guaranteed booking slots for an authentic Gir Safari, handpicked luxury jungle resorts, and dedicated concierge travel assistance throughout."
        ),
        seo_title="GJ-009 | Statue of Unity & Gir Safari Express | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Gujarat package (GJ-009 / TRAGUIN-GJ-009): Laser Light Show, Statue of Unity Viewing Gallery, Unity Glow Garden, Gir jungle safari, Devalia Safari Park, and 4-tier hotels"
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Scenic Route to Kevadia, Evening Laser Light and Sound Show.", 1),
            _ih("Statue of Unity Monument, Viewing Gallery, Valley of Flowers, Unity Glow Garden.", 2),
            _ih("Inter-city scenic transfer, Nature orientation walkthrough.", 3),
            _ih("TRAGUIN Signature Experience: Curated by our leading travel planners, this itinerary balances luxury transportation and handpicked hotels with flawless seamless execution. Experience stress-free wildlife bookings, express entry management at global heritage monuments, and localized insider dining recommendations for an extraordinary holiday.", 4),
            _ih("Curated by TRAGUIN Experts: Handpicked luxury hotels and seamless ground logistics", 5),
            _ih("Premium Handpicked Hotels: Properties certified for elite hospitality and safety standards", 6)
        ],
        days=[
            _day(
                1,
                "VADODARA ARRIVAL TO KEVADIA (STATUE OF UNITY)",
                (
                    "Arrive at Vadodara Airport or Railway Station, where your elite, professional TRAGUIN chauffeur greets you with premium welcome amenities. Board your private luxury air-conditioned vehicle for a smooth, scenic drive to Kevadia, the home of the monumental Statue of Unity. Check-in to your handpicked luxury tented resort or premium hotel. In the late afternoon, witness the epic, emotionally moving Laser Light and Sound Show, which projects the inspiring history of Sardar Vallabhbhai Patel onto the massive 182-meter sculpture."
                ),
                [
                    "Sightseeing Included: Scenic Route to Kevadia, Evening Laser Light and Sound Show.",
                    "Evening Experience: Walk down the illuminated pathways of the Narmada riverbank.",
                    "Overnight Stay: Premium Luxury Tented Resort / Hotel, Kevadia.",
                    "Meals Included: Welcome Drink & Gourmet Dinner."
                ],
            ),
            _day(
                2,
                "STATUE OF UNITY SIGHTSEEING",
                (
                    "Indulge in a premium buffet breakfast before diving into a comprehensive day of exploration. Benefit from priority skip-the-line express tickets to access the Statue of Unity Viewing Gallery, located at an astonishing 153 meters inside the chest of the statue, offering breathtaking panoramic views of the Narmada River and Vindhyachal mountain ranges. Later, enjoy a tranquil stroll through the exotic Valley of Flowers and explore the mesmerizing Unity Glow Garden, an architectural park adorned with illuminated structural installations."
                ),
                [
                    "Sightseeing Included: Statue of Unity Monument, Viewing Gallery, Valley of Flowers, Unity Glow Garden.",
                    "Photography Points: The towering monument facade and the sparkling lights of the Glow Garden.",
                    "Overnight Stay: Premium Luxury Tented Resort / Hotel, Kevadia.",
                    "Meals Included: Full Breakfast & Dinner."
                ],
            ),
            _day(
                3,
                "KEVADIA TO SASAN GIR NATIONAL PARK",
                (
                    "Bid farewell to Kevadia after breakfast as your premium vehicle begins a comfortable cross-state transit to the globally acclaimed Sasan Gir National Park, the sole home of the magnificent wild Asiatic Lions. The journey unfolds through charming rural landscapes and vast agricultural tracts. Reach Sasan Gir by afternoon and check-in to an ultra-luxury jungle lodge. Unwind amidst nature, enjoy an evening cultural folk dance around a bonfire, or listen to wildlife orientation stories curated by expert naturalists."
                ),
                [
                    "Sightseeing Included: Inter-city scenic transfer, Nature orientation walkthrough.",
                    "Evening Experience: Authentic local folk performance at the premium resort premises.",
                    "Overnight Stay: Handpicked Luxury Wilderness Resort, Sasan Gir.",
                    "Meals Included: Full Breakfast & Organic Farm-to-Table Dinner."
                ],
            ),
            _day(
                4,
                "SASAN GIR WILDLIFE JUNGLE SAFARI",
                (
                    "An unforgettable highlight awaits you. Wake up early for an exclusive open-top 4x4 Gypsy Gir Jungle Safari. As the golden morning rays filter through the dry deciduous forest, keep your cameras primed to spot the king of the jungle—the Asiatic Lion—alongside leopards, spotted deer, sambar, and rare bird species. Return to the resort for a late breakfast and relaxation by the luxury pool. In the afternoon, visit the Devalia Safari Park or explore a local organic mango orchard to experience authentic rural village hospitality."
                ),
                [
                    "Sightseeing Included: Open 4x4 Gir National Park Safari, Devalia Interpretation Zone.",
                    "Optional Activities: Guided bird watching trek along the Hiran River.",
                    "Overnight Stay: Handpicked Luxury Wilderness Resort, Sasan Gir.",
                    "Meals Included: Full Breakfast & Farewell Theme Dinner."
                ],
            ),
            _day(
                5,
                "SASAN GIR TO RAJKOT / DIU DEPARTURE",
                (
                    "Enjoy a leisurely breakfast at your wilderness lodge, taking in the serene forest sounds one last time. Pack your bags as your luxury vehicle arrives to escort you comfortably to Rajkot Airport / Station or nearby Diu Airport for your onward flight home. Your premium holiday concludes with endless tales of iconic attractions and wild adventures."
                ),
                [
                    "Transfers Included: Private Airport/Station Drop-off.",
                    "Meals Included: Premium Buffet Breakfast."
                ],
            )
        ],
        hotels=[
            _hotel("Tent City 2, Kevadia / Gir Birding Lodge", "Kevadia / Sasan Gir", "04 Nights", "Deluxe", "Standard Tent / Forest Cottage", "MAPAI (Breakfast + Dinner)", 4, 1),
            _hotel("The Fern Sardar Sarovar Resort / Lords Resorts Sasan Gir", "Kevadia / Sasan Gir", "04 Nights", "Premium", "Deluxe Room / Premium Room", "MAPAI (Breakfast + Dinner)", 5, 2),
            _hotel("Statue of Unity Tent City 1 (Luxury AC Tent) / The Fern Gir Forest Resort", "Kevadia / Sasan Gir", "04 Nights", "Luxury", "Luxury AC Tent / Club Villa", "MAPAI (Breakfast + Dinner)", 5, 3),
            _hotel("Amantara Resort / Ramada Encore Kevadia / Woods at Sasan (Luxury Studio Villa)", "Kevadia / Sasan Gir", "04 Nights", "Ultra Luxury", "Luxury Suite / Studio Villa", "MAPAI + Safari High Tea", 5, 4)
        ],
        inclusions=[
            _inc_included("Accommodation: 04 Nights stay at handpicked premium luxury properties and tented villages.", 1),
            _inc_included("Meals: 04 Premium buffet breakfasts and 04 curated gourmet multi-cuisine dinners.", 2),
            _inc_included("Transfers & Sightseeing: All city-to-city transfers and sightseeings in a private luxury Innova Crysta.", 3),
            _inc_included("Assistance: 24/7 dedicated on-call concierge and expert destination specialist coordination.", 4),
            _inc_included("Taxes: All applicable luxury resort taxes, toll fees, parking fees, and driver allowances.", 5),
            _inc_included("Welcome Amenities: Personalized travel kit containing traditional stoles, organic snacks, and bottled mineral water.", 6),
            _inc_included("Complimentary Experiences: Confirmed access passes to the unique Laser Light Show and Unity Glow Garden.", 7),
            _inc_excluded("Airfare or main-line train tickets to Vadodara / from Rajkot.", 8),
            _inc_excluded("Mandatory Government Forest Safari permit fees or camera tickets.", 9),
            _inc_excluded("Personal expenses such as telephone calls, laundry, alcoholic beverages, and personal tips.", 10),
            _inc_excluded("Optional activities or vehicle detours outside the planned itinerary sequence.", 11),
            _inc_excluded("Personal medical insurance or emergency expenses.", 12)
        ],
    )
    return package, itinerary


def build_gj_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "GJ-010"
    tour_code = "TRAGUIN-GJ-010"
    title = "Ahmedabad Heritage & Science City Explorer"
    duration = "02 Nights / 03 Days"
    slug = "gj-010-ahmedabad-heritage-science-city-explorer"
    itin_slug = "gj-010-ahmedabad-heritage-science-city-explorer-itinerary"
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
            _ph("State / Country: Gujarat / India | Category: Family Vacation / Leisure", 2),
            _ph("Destinations: Ahmedabad Heritage • Science City", 3),
            _ph("Ideal for: Families, Kids & Seniors", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Luxury Family Tour (FIT)", 7),
            _ph("Vehicle: Dedicated Luxury AC Sedan / SUV (Innova Crysta)", 8),
            _ph("Meal Plan: Modified American Plan (Premium Daily Breakfast & Dinners Included)", 9),
            _ph("Route Map: Ahmedabad Arrival → Sabarmati → Heritage City Walk → Science City → Departure", 10),
            _ph("TRAGUIN Signature Experience: Curated by TRAGUIN Experts, this package guarantees priority check-ins, top-tier luxury vehicle deployments, handpicked family-centric hotels, and pre-arranged, hassle-free admission passes to all iconic attractions to minimize wait times for children and seniors alike.", 11),
            _ph("Shopping: Law Garden & Sindhu Bhavan Road — hand-embroidered Chaniya Cholis, traditional Bandhani sarees, Patola silks, and upscale boutique cafes; hand-carved wooden artifacts, terracotta designs, and traditional silver jewelry", 12),
            _ph("Important: Standard check-in begins at 14:00 hrs and check-out finishes by 11:00 hrs. Early check-in requests are subject to availability. Science City Rule: The Science City complex remains completely closed to visitors every Monday for routine upkeep. Itinerary timing may adjust accordingly. Dress Guidelines: Modest clothing is recommended when exploring spiritual locations like Sabarmati Ashram and Sarkhej Roza.", 13)
        ],
        moods=["Heritage", "Family", "Leisure"],
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
        tagline="Ahmedabad Heritage & Science City Explorer • Old Quarters to Future Tech",
        overview=(
            "Step into India's first UNESCO World Heritage City coupled with futuristic human marvels. Crafted "
            "expertly by TRAGUIN, this premium itinerary offers families a perfect balance of deep historical "
            "narrative, scenic beauty, and fascinating technological exhibits. Your loved ones will collect "
            "unforgettable memories through curated experiences that guarantee absolute comfort, premium stays, "
            "and smooth luxury transportation.\n\n"
            "Ahmedabad is the vibrant heart of the region, housing some of the top tourist places in Gujarat. "
            "For discerning travelers looking for a Gujarat Honeymoon Package or an enriching Gujarat Family Tour, "
            "the combination of old-world architecture and modern development offers an unparalleled travel "
            "landscape. From the peaceful, spiritual riverbanks of the Sabarmati Ashram to the highly interactive "
            "and educational zones of Ahmedabad Science City, this Premium Gujarat Experience satisfies all age "
            "groups.\n\n"
            "TRAGUIN Curated Touch: Includes an expert-led private heritage walking tour, premium entry passes "
            "to Science City's Aquatic and Robotic Galleries, a traditional Gujarati fine-dining feast, and full "
            "concierge support."
        ),
        seo_title="GJ-010 | Ahmedabad Heritage & Science City Explorer | TRAGUIN",
        seo_description=(
            "Premium 02 Nights / 03 Days Gujarat package (GJ-010 / TRAGUIN-GJ-010): Sabarmati Ashram, Heritage Walk, Science City Aquatic Gallery, Robotics Gallery, Sarkhej Roza, and 4-tier hotels"
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Sabarmati Ashram, Adalaj Stepwell, Sabarmati Riverfront Walk.", 1),
            _ih("Heritage Old City Walk, Siddi Saiyyed Mosque, Ahmedabad Science City.", 2),
            _ih("Sarkhej Roza, Law Garden Crafts Market (Leisure Visit).", 3),
            _ih("TRAGUIN Signature Experience: Curated by TRAGUIN Experts, this package guarantees priority check-ins, top-tier luxury vehicle deployments, handpicked family-centric hotels, and pre-arranged, hassle-free admission passes to all iconic attractions to minimize wait times for children and seniors alike.", 4),
            _ih("Curated by TRAGUIN Experts: Handpicked luxury hotels and seamless ground logistics", 5),
            _ih("Premium Handpicked Hotels: Properties certified for elite hospitality and safety standards", 6)
        ],
        days=[
            _day(
                1,
                "ARRIVAL IN AHMEDABAD",
                (
                    "Arrive at Ahmedabad Airport / Railway Station where your elite TRAGUIN driver will welcome you warmly. Board your private luxury vehicle and transfer smoothly to your premium hotel. After checking in and relaxing, begin your Gujarat Sightseeing journey with a visit to the historic Sabarmati Ashram, the serene home of Mahatma Gandhi. Experience emotional storytelling as you walk along the peaceful banks of the Sabarmati Riverfront, followed by a mesmerizing view of the architectural marvel, Adalaj Stepwell."
                ),
                [
                    "Sightseeing Included: Sabarmati Ashram, Adalaj Stepwell, Sabarmati Riverfront Walk.",
                    "Evening Experience: A relaxing evening walk down the riverfront promenade as the city lights up.",
                    "Photography Points: Symmetrical stone carvings of Adalaj Stepwell and the scenic river sunset.",
                    "Overnight Stay: Premium Luxury Hotel, Ahmedabad.",
                    "Meals Included: Welcome Drink & Premium Buffet Dinner."
                ],
            ),
            _day(
                2,
                "AHMEDABAD HERITAGE TO FUTURE",
                (
                    "Start your day early with an immersive, guided Heritage Walk through the old quarters of Ahmedabad, exploring beautiful traditional 'Pols' and unique wooden architecture. Return to the hotel for a lavish breakfast, then head over to the state-of-the- art Ahmedabad Science City. Your premium entry tickets give your family front-row access to the world-class Aquatic Gallery (India's largest walk-through underwater tunnel aquarium) and the fascinating Robotics Gallery, where interactive humanoids greet you warmly."
                ),
                [
                    "Sightseeing Included: Heritage Old City Walk, Siddi Saiyyed Mosque, Ahmedabad Science City.",
                    "Optional Activities: Experiencing the thrill of the 5D Theatre or space exploration ride inside Science City.",
                    "Food Suggestions: Enjoy a luxurious, authentic Gujarati Thali lunch at a renowned heritage restaurant.",
                    "Overnight Stay: Premium Luxury Hotel, Ahmedabad.",
                    "Meals Included: Full Breakfast & Gourmet Dinner."
                ],
            ),
            _day(
                3,
                "CULTURAL EXPERIENCE & DEPARTURE",
                (
                    "Savor a final relaxed breakfast at the hotel. Visit the architectural masterpiece, Sarkhej Roza, often referred to as the 'Acropolis of Ahmedabad' due to its elegant Islamic design blending gracefully with Hindu elements. Spend your afternoon exploring high-end traditional boutiques or local markets for famous regional souvenirs. Later, your private vehicle will drop you off safely at the airport or station as your signature TRAGUIN Gujarat Holiday concludes."
                ),
                [
                    "Sightseeing Included: Sarkhej Roza, Law Garden Crafts Market (Leisure Visit).",
                    "Local Experiences: Witnessing local artisans demonstrate traditional block-printing or Bandhani textile arts.",
                    "Meals Included: Full Breakfast."
                ],
            )
        ],
        hotels=[
            _hotel("Lemon Tree Premier, Ahmedabad", "Ahmedabad", "02 Nights", "Deluxe", "Deluxe Room", "MAP (Breakfast + Dinner)", 4, 1),
            _hotel("The Pride Plaza Hotel, Ahmedabad", "Ahmedabad", "02 Nights", "Premium", "Premium Superior Room", "MAP (Breakfast + Dinner)", 5, 2),
            _hotel("Hyatt Regency, Ashram Road", "Ahmedabad", "02 Nights", "Luxury", "Club King Room with River View", "MAP (Breakfast + Dinner)", 5, 3),
            _hotel("ITC Narmada, a Luxury Collection Hotel", "Ahmedabad", "02 Nights", "Ultra Luxury", "Executive Club Room / Premium Suite", "MAP Premium Dining", 5, 4)
        ],
        inclusions=[
            _inc_included("Accommodation: 02 Nights stay at handpicked premium hotels based on your preferred choice.", 1),
            _inc_included("Meals: 02 Premium Buffet Breakfasts and 02 curated gourmet Dinners at the hotel restaurants.", 2),
            _inc_included("Transfers & Sightseeing: All commutes via an private, air-conditioned luxury vehicle with an experienced professional driver.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated concierge assistance and digital travel companion guides.", 4),
            _inc_included("Complimentary Experiences: VIP Entry Passes to the Aquatic and Robotics Galleries at Science City.", 5),
            _inc_included("Welcome Amenities: Personalized family travel welcome pack with mineral water bottles and refreshing wet wipes.", 6),
            _inc_included("Taxes: All applicable luxury lodging taxes, toll fees, parking tickets, and fuel charges included.", 7),
            _inc_excluded("Airfare or interstate train ticketing to and from Ahmedabad.", 8),
            _inc_excluded("Camera or video equipment licensing fees at individual historical sites.", 9),
            _inc_excluded("Personal discretionary items such as laundry, phone calls, room service, or tips.", 10),
            _inc_excluded("Optional extra vehicle usage or specialized excursions outside the pre-planned route.", 11),
            _inc_excluded("Individual medical or travel interruption insurance covers.", 12)
        ],
    )
    return package, itinerary


def build_gj_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "GJ-011"
    tour_code = "TRAGUIN-GJ-011"
    title = "Complete Saurashtra Panorama"
    duration = "07 Nights / 08 Days"
    slug = "gj-011-complete-saurashtra-panorama"
    itin_slug = "gj-011-complete-saurashtra-panorama-itinerary"
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
            _ph("State / Country: Gujarat / India | Category: Leisure / Heritage & Wildlife", 2),
            _ph("Destinations: Ahmedabad • Dasada • Jamnagar • Dwarka • Somnath • Gir National Park", 3),
            _ph("Ideal for: Families, Couples & Culture Enthusiasts", 4),
            _ph("Best season: October to March (Winter Season)", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Tailor-made Luxury Independent Travel (FIT)", 7),
            _ph("Vehicle: Dedicated Luxury Chauffeur-driven AC Innova Crysta", 8),
            _ph("Meal Plan: Modified American Plan (Daily Premium Breakfast & Dinners Included)", 9),
            _ph("Route Map: Ahmedabad → Little Rann of Kutch (Dasada) → Jamnagar → Dwarka Coastline → Somnath Temple → Gir National Park → Ahmedabad Heritage Return", 10),
            _ph("TRAGUIN Signature Experience: Curated by TRAGUIN Experts to offer the ultimate balance of historic immersion and modern comfort. Benefit from zero-wait hotel check-ins, top-tier private transportation, priority access to historical landmarks, and custom culinary menus prepared by regional chefs.", 11),
            _ph("Shopping: Purchase world-famous Bandhani tie-dye sarees, fine block-printed fabrics, and traditional silver artifacts. Saurashtra Souvenirs: Pick up genuine terracotta pottery items, hand-woven mirror-work fabrics, and regional artifacts.", 12),
            _ph("Important: Standard regional check-in is at 14:00 hrs and check-out is at 11:00 hrs. Early check-in requests depend entirely on room availability. • • •", 13)
        ],
        moods=["Heritage", "Spiritual", "Wildlife"],
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
        tagline="Complete Saurashtra Panorama • Coastlines, Temples & Lions",
        overview=(
            "COMPLETE SAURASHTRA PANORAMA • 07 NIGHTS / 08 DAYS Embark on a magnificent, soul-stirring journey across the land of legends with this signature Gujarat Honeymoon Package and elite Gujarat Family Tour. Specially curated by travel specialists at TRAGUIN, this exclusive journey reveals the breathtaking landscapes of the Saurashtra peninsula. From timeless structural wonders and holy architectural edifices to the deep roars of untamed Asiatic lions, treat your senses to unparalleled luxury, premium stays, and deeply immersive experiences.\n\n"
                        "Saurashtra is globally celebrated as a cornerstone of Indian culture, wildlife preservation, and timeless coastal beauty. For discerning globetrotters searching for a Premium Gujarat Experience or seeking out the finest Gujarat Sightseeing landmarks, this circuit seamlessly weaves royal history with natural magnificence. Here you will experience the pristine white salt fields of the Little Rann, the tranquil maritime beauty of Jamnagar, the legendary spirituality at Dwarka and Somnath, and the thrilling biodiversity of Sasan Gir. Our meticulously designed itinerary showcases the top highly searched tourism attractions, highly optimized for an exceptional vacation structure. Stay at handpicked hotels boasting unparalleled regional elegance and luxury amenities, coupled with smooth logistics that keep transitions comfortable. Whether capturing memories at popular Instagram locations or savoring authentic Kathiyawadi cuisines, this holiday guarantees unforgettable memories. HERITAGE GATEWAY & LITTLE RANN OF KUTCH SUN TEMPLE MARVEL & ROYAL LAKESIDES\n\n"
                        "TRAGUIN Curated Touch: Private safari vehicle arrangements, local companion guides, priority temple darsan entry cards, and 24/7 dedicated travel advisor care."
        ),
        seo_title="GJ-011 | Complete Saurashtra Panorama | TRAGUIN",
        seo_description=(
            "Premium 07 Nights / 08 Days Gujarat package (GJ-011 / TRAGUIN-GJ-011): Little Rann safari, Modhera Sun Temple, Dwarka, Beyt Dwarka, Somnath, Sasan Gir safari, and 4-tier hotels"
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Little Rann of Kutch Wildlife Safari, Salt Pan Views.", 1),
            _ih("Modhera Sun Temple, Lakhota Lake & Palace Museum, Bala Hanuman Temple.", 2),
            _ih("Dwarkadhish Temple Complex, Gomti Ghat Walkways.", 3),
            _ih("TRAGUIN Signature Experience: Curated by TRAGUIN Experts to offer the ultimate balance of historic immersion and modern comfort. Benefit from zero-wait hotel check-ins, top-tier private transportation, priority access to historical landmarks, and custom culinary menus prepared by regional chefs.", 4),
            _ih("Curated by TRAGUIN Experts: Handpicked luxury hotels and seamless ground logistics", 5),
            _ih("Premium Handpicked Hotels: Properties certified for elite hospitality and safety standards", 6)
        ],
        days=[
            _day(
                1,
                "AHMEDABAD TO DASADA",
                (
                    "Begin your spectacular Premium Gujarat Experience as you arrive in the historic city of Ahmedabad. Meet your elite TRAGUIN chauffeur at the terminal and travel smoothly via a scenic rural expressway to Dasada, the gateway to the legendary Little Rann of Kutch. Check in seamlessly at your eco-luxury resort. In the afternoon, enjoy an exclusive cross-desert safari in a customized private open-top 4x4 vehicle. Witness the breathtaking landscapes of the salt pans and encounter the rare Asiatic Wild Ass (Khur), desert foxes, and majestic birds gliding over the horizon."
                ),
                [
                    "Sightseeing Included: Little Rann of Kutch Wildlife Safari, Salt Pan Views.",
                    "Photography Points: Sunset over the expansive barren desert salt crust.",
                    "Evening Experience: Stargazing beneath a perfectly clear desert canopy with traditional high-tea.",
                    "Overnight Stay: Handpicked Luxury Desert Resort, Dasada.",
                    "Meals Included: Welcome Refreshments & Gourmet Dinner."
                ],
            ),
            _day(
                2,
                "DASADA TO JAMNAGAR via MODHERA",
                (
                    "Savor a delightful organic breakfast before departing for the historic port city of Jamnagar. En route, pause to behold the breathtaking architectural precision of the 11th-century Modhera Sun Temple, an iconic attraction designed so that the first rays of dawn illuminate the inner sanctum. Arrive in Jamnagar by early afternoon and check in to your premium luxury accommodation. Later, explore the elegant Lakhota Lake and Palace museum, an absolute highlight for culture lovers."
                ),
                [
                    "Sightseeing Included: Modhera Sun Temple, Lakhota Lake & Palace Museum, Bala Hanuman Temple.",
                    "Local Experiences: Witness the continuous spiritual chants (Guinness Record) at the Bala Hanuman temple.",
                    "Overnight Stay: Premium Luxury Heritage Hotel, Jamnagar.",
                    "Meals Included: Full Buffet Breakfast & Dinner."
                ],
            ),
            _day(
                3,
                "JAMNAGAR TO DWARKA",
                (
                    "Following a leisurely breakfast, embark on a smooth coastal drive toward the sacred city of Dwarka, one of India's ancient Chardham destinations. The route offers glimpses of local windmills and tranquil seaside panoramas. Check in to your ultra-luxury seaside property with time to relax. In the late afternoon, proceed to the glorious Dwarkadhish Temple (Jagat Mandir), standing tall against the crashing Arabian Sea waves. Your TRAGUIN package provides priority entry cards, letting you immerse in the spiritual evening aarti with complete ease."
                ),
                [
                    "Sightseeing Included: Dwarkadhish Temple Complex, Gomti Ghat Walkways.",
                    "Optional Activities: A peaceful evening meditation session on the banks of the Gomti River.",
                    "Overnight Stay: Handpicked Luxury Resort, Dwarka.",
                    "Meals Included: Breakfast & Choice of Authentic Regional Cuisine Dinner."
                ],
            ),
            _day(
                4,
                "DWARKA EXCURSIONS",
                (
                    "Dedicate your morning to an exclusive excursion to Beyt Dwarka Island, traveling via a premium private speedboat ride across the blue Gulf of Kutch waters. Discover ancient temples and historical structures hidden amidst the island. On your return route, visit the magnificent Nageshwar Jyotirlinga Temple and Gopi Talav. Conclude your day at the scenic Rukmini Devi Temple before catching a brilliant sunset over Shivrajpur Beach, a globally accredited Blue Flag destination perfect for peaceful photography."
                ),
                [
                    "Sightseeing Included: Beyt Dwarka, Nageshwar Jyotirlinga, Rukmini Temple, Shivrajpur Blue-Flag Beach.",
                    "Instagram Spots: The majestic white sand dunes and crystal clear waters of Shivrajpur.",
                    "Overnight Stay: Handpicked Luxury Resort, Dwarka.",
                    "Meals Included: Full Breakfast & Gourmet Dinner."
                ],
            ),
            _day(
                5,
                "DWARKA TO SOMNATH via PORBANDAR",
                (
                    "Drive along a spectacular marine highway from Dwarka to Somnath. En route, make a premium stop at Porbandar to explore Kirti Mandir, the heritage birthplace of Mahatma Gandhi. Continue your drive toward the timeless town of Somnath. Check in to your premium handpicked stay. In the evening, visit the magnificent Somnath Temple, an architectural masterpiece standing prominently on the shores of the Arabian Sea. Witness a breathtaking Light & Sound show highlighting the resilience of this sacred temple."
                ),
                [
                    "Sightseeing Included: Kirti Mandir, Somnath Shore Temple, Light & Sound Projection Show.",
                    "Evening Experience: Watch the shoreline light up as a symphony of chimes and ocean waves fill the air.",
                    "Overnight Stay: Premium Luxury Resort, Somnath.",
                    "Meals Included: Breakfast & Full Multi-cuisine Dinner."
                ],
            ),
            _day(
                6,
                "SOMNATH TO SASAN GIR NATIONAL PARK",
                (
                    "After a morning breakfast, take a pleasant 1.5-hour drive into the thick teak forests of Gir National Park, the absolute last habitat of the endangered wild Asiatic Lions. Check in to your ultra-luxury forest wilderness lodge and unwind. In the afternoon, embark on an immersive open-jeep wildlife safari deep inside the sanctuary core. Guided by a certified expert tracker, look out for leopards, marsh crocodiles, spotted deer, and the magnificent King of the Forest."
                ),
                [
                    "Sightseeing Included: Sasan Gir Forest Core Safari, Wildlife Tracking.",
                    "Food Suggestions: Enjoy an authentic organic meal at a boutique farm-to-table forest estate.",
                    "Overnight Stay: Ultra-Luxury Wilderness Lodge, Sasan Gir.",
                    "Meals Included: Full Breakfast & Luxury Resort Buffet Dinner."
                ],
            ),
            _day(
                7,
                "SASAN GIR TO AHMEDABAD via JUNAGADH",
                (
                    "Enjoy a serene breakfast surrounded by forest birds. Depart towards Ahmedabad, pausing along the way at the ancient heritage city of Junagadh. Explore the historic Uparkot Fort, an ancient citadel featuring deep stepwells like Adi Kadi Vav and Navghan Kuwo carved right from monolithic rock faces. Continue your smooth drive to Ahmedabad and check in to your ultra-premium hotel for your final evening in Gujarat."
                ),
                [
                    "Sightseeing Included: Junagadh Uparkot Fort, Mahabat Maqbara architectural wonder. Shopping: Browse authentic local markets for fine brassware and intricate single-ikat Patola silk.",
                    "Overnight Stay: Premium Luxury Business Hotel, Ahmedabad.",
                    "Meals Included: Full Breakfast & Celebration Farewell Dinner."
                ],
            ),
            _day(
                8,
                "AHMEDABAD SIGHTSEEING & DEPARTURE",
                (
                    "Conclude your landmark TRAGUIN Gujarat Package with a relaxed morning exploration of Ahmedabad, India's first UNESCO World Heritage City. Visit the tranquil Sabarmati Ashram along the riverfront, once the epicenter of India’s freedom movement. Admire the marvelous stone lattice-work at the Sidi Saiyyed Mosque. Later, your private vehicle will drop you off smoothly at the Ahmedabad International Airport for your journey home, carrying a treasure trove of unforgettable memories."
                ),
                [
                    "Sightseeing Included: Sabarmati Ashram, Sidi Saiyyed Mosque, Airport Drop Transfer.",
                    "Meals Included: Full Breakfast Buffet."
                ],
            )
        ],
        hotels=[
            _hotel("Rann Riders (Dasada) / Lords Inn (Dwarka) / Fern Residency (Somnath)", "Multi-City Saurashtra", "07 Nights", "Deluxe", "Standard Deluxe / Executive AC", "MAP (Breakfast + Dinner)", 4, 1),
            _hotel("Desert Coursers (Dasada) / Hawthorn Suites by Wyndham (Dwarka) / Woods at Sasan (Gir)", "Multi-City Saurashtra", "07 Nights", "Premium", "Premium Suite / Studio Villa", "MAP (Breakfast + Dinner)", 5, 2),
            _hotel("The Fern Crown (Sasangir) / Lemon Tree Premier (Dwarka) / Hyatt Regency (Ahmedabad)", "Multi-City Saurashtra", "07 Nights", "Luxury", "Luxury Heritage / Riverview Club", "MAP (Breakfast + Dinner)", 5, 3),
            _hotel("Taj Gateway Gir Forest Resort / Taj Club House (Dwarka) / ITC Narmada (Ahmedabad)", "Multi-City Saurashtra", "07 Nights", "Ultra Luxury", "Presidential Villa / Royal Suite", "Gourmet MAP All-Inclusive", 5, 4)
        ],
        inclusions=[
            _inc_included("Accommodation: 07 Nights stay at handpicked premium luxury hotels and wilderness safari lodges.", 1),
            _inc_included("Meals: 07 Buffet Breakfasts and 07 curated dinners across your premium hotel stops.", 2),
            _inc_included("Transfers & Sightseeing: Dedicated AC Innova Crysta for all airport routes, inter-city travel, and tourist places.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated travel concierge assistance and professional local guides at key sites.", 4),
            _inc_included("Complimentary Experiences: Private chartered boat tickets at Beyt Dwarka and pre-booked Light & Sound show seats in Somnath.", 5),
            _inc_included("Welcome Amenities: Personalized travel kit containing traditional stoles, organic sanitizers, and premium packed mineral water.", 6),
            _inc_excluded("Airfare or interstate train tickets to and from Gujarat.", 7),
            _inc_excluded("Jungle Safari permit charges and camera tickets inside Sasan Gir National Park.", 8),
            _inc_excluded("Personal expenses such as laundry services, phone calls, premium beverages, and tipping.", 9),
            _inc_excluded("Any optional adventure activities or detour vehicle usage beyond the itinerary path.", 10),
            _inc_excluded("Mandatory travel and health insurance premiums.", 11)
        ],
    )
    return package, itinerary


def build_gj_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "GJ-012"
    tour_code = "TRAGUIN-GJ-012"
    title = "Complete Vibrant Gujarat Mega Tour"
    duration = "09 Nights / 10 Days"
    slug = "gj-012-complete-vibrant-gujarat-mega-tour"
    itin_slug = "gj-012-complete-vibrant-gujarat-mega-tour-itinerary"
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
            _ph("State / Country: Gujarat / India | Category: Family Vacation / Luxury", 2),
            _ph("Destinations: Ahmedabad • Dasada • Bhuj • Rann of Kutch • Dwarka • Somnath • Sasan Gir", 3),
            _ph("Ideal for: Families & Luxury Travelers", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Luxury Grand Circuit (FIT)", 7),
            _ph("Vehicle: Private Air-Conditioned Luxury Innova Crysta / Luxury Coach", 8),
            _ph("Meal Plan: Modified American Plan (Daily Premium Breakfast & Authentic Gourmet Dinners)", 9),
            _ph("Route Map: Ahmedabad → Dasada (Little Rann) → Bhuj & Great Rann of Kutch → Dwarka → Somnath → Sasan Gir → Ahmedabad Departure", 10),
            _ph("TRAGUIN Signature Experience: Curated by TRAGUIN Experts to offer an optimal balance of adventure and luxury. Benefit from priority hotel check-ins, VIP fast-track coordination at primary shrines, handpicked family-friendly stays, and reliable transportation networks throughout the vast state.", 11),
            _ph("Shopping: Purchase gorgeous bandhani textiles and mirror-work attire at Law Garden market. Kutch Handicrafts: Pick up genuine Ajrakh block prints, rogue pottery craft work, and leather bags directly from rural artisans.", 12),
            _ph("Important: Standard check-in time is 14:00 hrs and check-out is 11:00 hrs. Early check-in requests are subject to availability. Weather Notes: Winter months offer lovely weather. Light woolens are recommended for desert nights in Kutch and morning jungle safaris in Gir. Booking Suggestions: Advance booking for Sasan Gir safaris is strongly advised as permits are limited and controlled strictly by the forest department.", 13)
        ],
        moods=["Heritage", "Spiritual", "Wildlife"],
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
        tagline="Complete Vibrant Gujarat Mega Tour • Rann, Coast & Gir Wilderness",
        overview=(
            "Are you planning a highly immersive Luxury Gujarat Holiday? As one of India's most diverse territories, a comprehensive Gujarat Sightseeing expedition opens doors to incredible landmarks and deeply rooted history. Visitors flock from around the globe to observe the top tourist places in Gujarat, including India’s first UNESCO World Heritage City (Ahmedabad), the historic stepwells of Patan, and the ancient seaside temples. Our meticulously organized TRAGUIN Gujarat Packages are optimized perfectly to cover every major Instagram-famous location, local shopping hotspot, and cultural milestone. Whether you seek the spiritual bliss of the Gujarat Honeymoon Package or an expansive family exploration, the best time to visit Gujarat is during the crisp winter months when the salt plains glow under the full moon and wildlife sightings are at their peak.\n\n"
                        "TRAGUIN Curated Touch: This Premium Gujarat Experience incorporates private guided heritage walks, elite tented comfort in the salt deserts, VIP temple darshan management, and exclusive open-jeep safaris designed flawlessly for your family's extreme relaxation."
        ),
        seo_title="GJ-012 | Complete Vibrant Gujarat Mega Tour | TRAGUIN",
        seo_description=(
            "Premium 09 Nights / 10 Days Gujarat package (GJ-012 / TRAGUIN-GJ-012): Little Rann, White Rann, Aina Mahal, Dwarka, Somnath, Sasan Gir safari, and 4-tier premium hotels"
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Sabarmati Ashram, Adalaj Stepwell, Riverfront Promenade.", 1),
            _ih("Little Rann Salt-Flats, Wild Ass Sanctuary Safari.", 2),
            _ih("Ajrakhpur Craft Village, Bhuj Local Heritage Avenues.", 3),
            _ih("TRAGUIN Signature Experience: Curated by TRAGUIN Experts to offer an optimal balance of adventure and luxury. Benefit from priority hotel check-ins, VIP fast-track coordination at primary shrines, handpicked family-friendly stays, and reliable transportation networks throughout the vast state.", 4),
            _ih("Curated by TRAGUIN Experts: Handpicked luxury hotels and seamless ground logistics", 5),
            _ih("Premium Handpicked Hotels: Properties certified for elite hospitality and safety standards", 6)
        ],
        days=[
            _day(
                1,
                "ARRIVAL IN AHMEDABAD",
                (
                    "Arrive at Ahmedabad Airport where your dedicated premium private vehicle and TRAGUIN holiday manager await your family. Enjoy a smooth transfer to your handpicked hotel. In the afternoon, explore the tranquil pathways of Sabarmati Ashram, the historic residence of Mahatma Gandhi. As twilight falls, witness the magnificent architecture of Adalaj Stepwell, a breathtaking showcase of ancient underground masonry."
                ),
                [
                    "Sightseeing Included: Sabarmati Ashram, Adalaj Stepwell, Riverfront Promenade.",
                    "Evening Experience: Savor an exclusive welcome feast featuring an authentic heritage Gujarati Thali.",
                    "Overnight Stay: Handpicked Luxury Hotel, Ahmedabad.",
                    "Meals Included: Welcome Drink & Gourmet Dinner."
                ],
            ),
            _day(
                2,
                "AHMEDABAD TO DASADA",
                (
                    "After a luxurious breakfast, enjoy a comfortable drive to Dasada, situated right beside the Little Rann of Kutch. Check into your premium desert eco-resort. In the afternoon, board an exclusive open-top safari vehicle to explore the Wild Ass Sanctuary. This unique salt-marsh landscape houses the last remaining population of the elegant Asiatic Wild Ass, alongside desert foxes and beautiful migratory birds."
                ),
                [
                    "Sightseeing Included: Little Rann Salt-Flats, Wild Ass Sanctuary Safari.",
                    "Photography Points: Crimson sunset over the flat expanses of the sun-baked salt marsh.",
                    "Overnight Stay: Premium Luxury Safari Resort, Dasada.",
                    "Meals Included: Full Breakfast & Dinner."
                ],
            ),
            _day(
                3,
                "DASADA TO BHUJ VIA AJRAKHPUR",
                (
                    "Journey deeper into Kutch today as your premium vehicle drives smoothly toward Bhuj. Along this highly scenic route, halt at the famous artisan village of Ajrakhpur. Witness an immersive live demonstration of traditional block-printing techniques handed down through centuries. Arrive in Bhuj by evening and check into your handpicked premium stay."
                ),
                [
                    "Sightseeing Included: Ajrakhpur Craft Village, Bhuj Local Heritage Avenues.",
                    "Optional Activities: Evening interaction with national award-winning master craftsmen.",
                    "Overnight Stay: Premium Luxury Resort, Bhuj.",
                    "Meals Included: Breakfast & Dinner."
                ],
            ),
            _day(
                4,
                "BHUJ TO GREAT RANN OF KUTCH",
                (
                    "Transfer to an ultra-luxury tented camp located directly on the fringes of the Great Rann of Kutch. After checking in, prepare to be completely spellbound. Walk along the legendary salt plains as they glisten brilliantly like diamonds. This breathtaking landscape offers an emotional, once-in-a-lifetime sunset experience that defines the peak of your family trip."
                ),
                [
                    "Sightseeing Included: White Salt Desert Vista, Tented Village Celebrations.",
                    "Evening Experience: Live folk music performances under the starry desert sky.",
                    "Overnight Stay: Ultra-Luxury Tented Resort, Rann of Kutch.",
                    "Meals Included: Breakfast, Lunch & Festive Desert Dinner."
                ],
            ),
            _day(
                5,
                "RANN OF KUTCH TO BHUJ SIGHTSEEING",
                (
                    "Bid farewell to the salt desert after breakfast and drive back to Bhuj for an intensive exploration of its royal landmarks. Tour the famous Aina Mahal (Palace of Mirrors) and the European-gothic styled Prag Mahal. Ascend Bhujia Hill for spectacular aerial views of the entire valley before returning to your luxury resort."
                ),
                [
                    "Sightseeing Included: Aina Mahal, Prag Mahal, Kutch Museum, Swaminarayan Temple.",
                    "Instagram Spots: The intricate marble mirror pools inside Aina Mahal.",
                    "Overnight Stay: Premium Luxury Resort, Bhuj.",
                    "Meals Included: Full Breakfast & Dinner."
                ],
            ),
            _day(
                6,
                "BHUJ TO DWARKA",
                (
                    "Embark on a scenic spiritual drive as you trace the western coastline down towards the holy city of Dwarka. Check into your luxury seaside hotel. In the evening, step inside the ancient and breathtaking Dwarkadhish Temple (Jagat Mandir), standing majestically on the banks of the Gomti River, and take part in the moving evening Aarti ceremony."
                ),
                [
                    "Sightseeing Included: Dwarkadhish Temple, Gomti Ghat Walkway.",
                    "Optional Activities: A relaxing evening holy dip or boat ride at the meeting point of the river and ocean.",
                    "Overnight Stay: Premium Handpicked Luxury Hotel, Dwarka.",
                    "Meals Included: Breakfast & Dinner."
                ],
            ),
            _day(
                7,
                "DWARKA EXCURSION TO BEYT DWARKA",
                (
                    "Board an exclusive private ferry to reach Beyt Dwarka island, believed to be the original residential palace of Lord Krishna. On your return route, visit the sacred Nageshwar Jyotirlinga temple, housing one of the 12 primary divine shrines of Lord Shiva. Pause at Rukmini Devi Temple to hear fascinating local folklore told by specialized destination guides."
                ),
                [
                    "Sightseeing Included: Beyt Dwarka, Nageshwar Jyotirlinga, Rukmini Temple, Gopi Talav.",
                    "Immersive Experiences: Private fast-track VIP darshan access managed expertly by TRAGUIN support.",
                    "Overnight Stay: Premium Handpicked Luxury Hotel, Dwarka.",
                    "Meals Included: Full Breakfast & Dinner."
                ],
            ),
            _day(
                8,
                "DWARKA TO SOMNATH VIA PORBANDAR",
                (
                    "Drive along a beautiful coastal highway towards Porbandar to explore Kirti Mandir, the historic birthplace of Mahatma Gandhi. Continue onward to the legendary Somnath Temple. Standing proud right on the edge of the Arabian Sea, this iconic attraction has been rebuilt beautifully across history. In the evening, watch a spectacular Sound and Light show projected directly onto the temple facade."
                ),
                [
                    "Sightseeing Included: Kirti Mandir, Somnath Temple, Light & Sound Show, Triveni Sangam.",
                    "Overnight Stay: Premium Luxury Hotel, Somnath.",
                    "Meals Included: Breakfast & Dinner."
                ],
            ),
            _day(
                9,
                "SOMNATH TO SASAN GIR NATIONAL PARK",
                (
                    "Drive to the lush, deciduous woods of Sasan Gir, the last remaining bastion of the majestic wild Asiatic Lions. Check into your ultra-luxury wilderness resort. In the afternoon, set out on an exclusive open-jeep jungle safari through the core national park zone, tracking apex predators and diverse wildlife under the guidance of certified naturalists."
                ),
                [
                    "Sightseeing Included: Sasan Gir Jungle Safari, Crocodile Breeding Centre.",
                    "Food Suggestions: Relish organic forest-to-table cuisine prepared by premium resort chefs.",
                    "Overnight Stay: Ultra-Luxury Wilderness Resort, Sasan Gir.",
                    "Meals Included: Breakfast, Lunch & Farewell Dinner."
                ],
            ),
            _day(
                10,
                "SASAN GIR TO AHMEDABAD DEPARTURE",
                (
                    "Enjoy a final leisurely breakfast amidst the bird calls of Sasan Gir. Embark on a comfortable drive back to Ahmedabad. Your luxury private vehicle transfers you smoothly to the airport or railway station for your onward transit. Your exceptional TRAGUIN Gujarat Package concludes here, leaving your family with memories that will stay with you forever."
                ),
                [
                    "Transfers Included: Private Luxury Airport Drop-off.",
                    "Meals Included: Full Buffet Breakfast."
                ],
            )
        ],
        hotels=[
            _hotel("Regenta Central / Seven Sky Resort / Rann Resort / Gir Birding Lodge", "Ahmedabad / Bhuj / Rann / Gir", "09 Nights", "Deluxe", "Deluxe Room / Standard Tent", "MAPAI (Breakfast + Dinner)", 4, 1),
            _hotel("Hyatt Regency / Grand 3D Bhuj / White Rann Resort / Asiatic Lion Lodge", "Ahmedabad / Bhuj / Rann / Gir", "09 Nights", "Premium", "Premium Room / Executive Tent", "MAPAI (Breakfast + Dinner)", 5, 2),
            _hotel("Taj Skyline / Regenta Resort Bhuj / The Gateway Resort / Woods at Sasan", "Ahmedabad / Bhuj / Rann / Gir", "09 Nights", "Luxury", "Executive Room / Luxury Pavilion", "MAPAI (Breakfast + Dinner)", 5, 3),
            _hotel("ITC Narmada / Amã Stays & Trails Kutch / Rann Utsav Tent City (Premium AC) / The Fern Gir Forest Resort", "Ahmedabad / Bhuj / Rann / Gir", "09 Nights", "Ultra Luxury", "Grand Suite / Premium AC Tent / Kothi", "Gourmet MAPAI + High Tea", 5, 4)
        ],
        inclusions=[
            _inc_included("Accommodation: 09 Nights stay at premium handpicked luxury hotels, safari lodges, and desert resorts.", 1),
            _inc_included("Meals: 09 Premium Buffet Breakfasts and 09 curated regional dinners at the properties.", 2),
            _inc_included("Transfers & Sightseeing: Chauffeur-driven air-conditioned Luxury Innova Crysta throughout the complete itinerary.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated travel consultant assistance and on-ground hospitality managers.", 4),
            _inc_included("Complimentary Experiences: Private ferry crossings to Beyt Dwarka and curated textile village walk in Kutch.", 5),
            _inc_included("Taxes & Welcome Amenities: All parking, state toll fees, hotel luxury taxes, and a customized family welcoming pack.", 6),
            _inc_excluded("Airfare or interstate train tickets to and from Ahmedabad.", 7),
            _inc_excluded("National Park permit fees and camera entry tickets at Sasan Gir.", 8),
            _inc_excluded("Personal expenses such as laundry, premium beverages, and tipping.", 9),
            _inc_excluded("Optional city excursions or extra vehicle usage beyond scheduled route hours.", 10),
            _inc_excluded("Travel insurance premium policies.", 11)
        ],
    )
    return package, itinerary


def build_gj_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "GJ-013"
    tour_code = "TRAGUIN-GJ-013"
    title = "Rann of Kutch White Desert Festival Experience"
    duration = "03 Nights / 03 Days"
    slug = "gj-013-rann-of-kutch-white-desert-festival-experience"
    itin_slug = "gj-013-rann-of-kutch-white-desert-festival-experience-itinerary"
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
            _ph("State / Country: Gujarat / India | Category: Culture / Heritage Luxury", 2),
            _ph("Destinations: Bhuj • Dhordo • Rann of Kutch White Desert", 3),
            _ph("Ideal for: Culture Enthusiasts & Elite Families", 4),
            _ph("Best season: November to February (Rann Utsav)", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Luxury Cultural Tour (FIT)", 7),
            _ph("Vehicle: Private Executive Air-Conditioned Luxury Transportation / Innova Crysta", 8),
            _ph("Meal Plan: All Meals Included (Traditional Kutchi & International Gourmet Buffet Cuisine)", 9),
            _ph("Route Map: Bhuj Arrival → Heritage Craft Villages → White Desert Gate (Dhordo) → Bhuj Departure", 10),
            _ph("TRAGUIN Signature Experience: Curated by TRAGUIN Experts, this high-end proposal layout integrates immersive cultural masterclasses with zero-stress logistics. Receive priority check-in rights at festival properties, luxury transportation comforts, and handpicked local guides to unravel the historical essence of Kutch beautifully.", 11),
            _ph("Shopping: Buy original Rogan art paintings, gorgeous Bandhani tie-dye silk fabrics, and elegant Kutchi leather slippers. Silver Souvenirs: Explore Bhuj's traditional silver bazaars for intricate hand-carved tribal ornaments and jewelry.", 12),
            _ph("Important: Standard property check-in is schedule-tracked at 12:30 PM, with departures fixed at 10:00 AM inside the desert resorts. Weather Guidelines: Kutch winter temperatures can vary significantly. Days are warm and dry while nights become cold; bringing proper woolen clothing is strongly recommended. Advance Booking Suggestions: Due to heavy international ranking demand for the Rann Utsav full- moon phases, secure bookings 60–90 days in advance to lock premium inventory.", 13)
        ],
        moods=["Culture", "Heritage", "Adventure"],
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
        tagline="Rann of Kutch White Desert Festival Experience • Salt Desert Splendor",
        overview=(
            "RANN OF KUTCH WHITE DESERT FESTIVAL EXPERIENCE • 3 NIGHTS / 3 DAYS Step into a surreal landscape where earth meets the sky in an endless sheet of salt. Carefully designed by TRAGUIN, this exclusive Luxury Gujarat Holiday introduces you to the magical colors, heritage crafts, and breathtaking landscapes of the Rann of Kutch White Desert Festival. Experience impeccable luxury hospitality amidst cultural brilliance, curated specifically to form unforgettable memories.\n\n"
                        "The Rann of Kutch White Desert Festival is universally celebrated as India's ultimate desert extravaganza, transforming a salt marsh desert into a vibrant canvas of folk music, traditional dances, and exquisite craftsmanship. If you are looking for the perfect Gujarat Family Tour or a distinctive cultural getaway, the Top Tourist Places in Gujarat nestled around Kutch provide a marvelous mixture of adventure, shopping, and historical wealth. The absolute Best Time to Visit Gujarat for desert sightseeing is during the pleasant winter full-moon nights when the vast landscape shimmers like silver diamonds. This tour is packed with popular Instagram locations, from the iconic mirror-work mud houses called 'Bhungas' to dramatic horizons of the salt flats at sunset. Indulge in premium stays at handpicked luxury heritage setups managed seamlessly with flawless TRAGUIN Gujarat Packages. WELCOME TO THE LAND OF ARTISTRY SUNSET GLORY ON THE WHITE SALT MARSH\n\n"
                        "TRAGUIN Curated Touch: This elite cultural holiday includes VIP entry access to the Rann Utsav festival grounds, premium handpicked hotels/luxury tented cottages, sunset camel safaris, and a dedicated travel consultant manager at every step."
        ),
        seo_title="GJ-013 | Rann of Kutch White Desert Festival Experience | TRAGUIN",
        seo_description=(
            "Premium 03 Nights / 03 Days Gujarat package (GJ-013 / TRAGUIN-GJ-013): Bhujodi weaving, Rann Utsav, Kalo Dungar, Aina Mahal, Prag Mahal, and 4-tier desert accommodation"
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Bhujodi Weaving Center, Ajrakhpur Block-Printing Hub, Swaminarayan Temple.", 1),
            _ih("Dhordo Tent City, Rann Utsav Cultural Arena, Sunset Salt Desert Vista.", 2),
            _ih("Kalo Dungar Hills, Dattatreya Temple, Great Rann Moonlight View.", 3),
            _ih("TRAGUIN Signature Experience: Curated by TRAGUIN Experts, this high-end proposal layout integrates immersive cultural masterclasses with zero-stress logistics. Receive priority check-in rights at festival properties, luxury transportation comforts, and handpicked local guides to unravel the historical essence of Kutch beautifully.", 4),
            _ih("Curated by TRAGUIN Experts: Handpicked luxury hotels and seamless ground logistics", 5),
            _ih("Premium Handpicked Hotels: Properties certified for elite hospitality and safety standards", 6)
        ],
        days=[
            _day(
                1,
                "BHUJ ARRIVAL & HERITAGE TEXTILE VILLAGES",
                (
                    "Arrive at Bhuj Airport/Railway Station where your private luxury transport chauffeur and your expert TRAGUIN coordinator await you with an authentic royal welcome. Begin your journey with a scenic route tour into the craft heartlands of Kutch. Visit the artisan village of Bhujodi, famed for its master handloom weaving, followed by a trip to Ajrakhpur to witness block-printing art dating back generations. Conclude your evening with a premium check-in at your luxury hotel, followed by an elegant welcome briefing session."
                ),
                [
                    "Sightseeing Included: Bhujodi Weaving Center, Ajrakhpur Block-Printing Hub, Swaminarayan Temple.",
                    "Food Suggestions: Enjoy a hot, comforting traditional Gujarati Thali with clarified butter (Ghee) and local buttermilk at a premier heritage bistro.",
                    "Photography Points: Vibrant colorful threads across open-air handlooms in Bhujodi.",
                    "Overnight Stay: Premium Handpicked Luxury Hotel, Bhuj.",
                    "Meals Included: Traditional Welcome Drink & Gourmet Buffet Dinner."
                ],
            ),
            _day(
                2,
                "BHUJ TO THE WHITE DESERT FESTIVAL (DHORDO)",
                (
                    "Following a delicious, lavish breakfast, drive comfortably north toward the grand venue of the Rann of Kutch White Desert Festival in Dhordo. Check into your ultra-premium handpicked luxury air- conditioned tented resort. In the afternoon, explore the lively festival grounds, experiencing iconic attractions like folk musical instruments, live puppet shows, and local acrobatics. As twilight approaches, embark on an immersive camel cart safari into the endless white expanse to watch a breathtaking sunset that paint the salt desert in brilliant crimson hues."
                ),
                [
                    "Sightseeing Included: Dhordo Tent City, Rann Utsav Cultural Arena, Sunset Salt Desert Vista.",
                    "Evening Experience: A dazzling exclusive experience featuring spectacular live Kutchi folk dances under the stars.",
                    "Optional Activities: Parasailing or ATVs across the desert fringes for adventure lovers.",
                    "Overnight Stay: Ultra-Luxury AC Premium Tent / Ethnic Bhunga Suite, Dhordo Resort.",
                    "Meals Included: Breakfast, Royal Lunch, High Tea & Festive Desert Dinner."
                ],
            ),
            _day(
                3,
                "KALO DUNGAR & FULL MOON SPLENDOR",
                (
                    "Wake up early to catch a glorious sunrise over the serene salt flats. After breakfast, head towards Kalo Dungar (Black Hill), the highest geographic elevation in Kutch, offering panoramic birds-eye vistas of the ecosystem stretching into the Great Rann. Visit the historic 400-year-old Dattatreya temple at the peak. Return to the resort for lunch. Spend the late evening experiencing the ultimate magical view: walking upon the white desert floor as it glows intensely under the starry moonlit skies."
                ),
                [
                    "Sightseeing Included: Kalo Dungar Hills, Dattatreya Temple, Great Rann Moonlight View.",
                    "Local Experiences: Interaction with village elders to hear ancient lore of the Kutchi landscape.",
                    "Photography Points: Breathtaking views over the salt horizon from the watchpoint at Black Hill.",
                    "Overnight Stay: Ultra-Luxury AC Premium Tent / Ethnic Bhunga Suite, Dhordo Resort.",
                    "Meals Included: Breakfast, Regional Lunch, Evening Snacks & Grand Gala Dinner."
                ],
            ),
            _day(
                4,
                "BHUJ ROYAL SIGHTSEEING & DEPARTURE",
                (
                    "Enjoy a relaxed breakfast before checking out and driving back to Bhuj for your final leg of Gujarat Sightseeing. Explore the majestic 18th-century Italian-Gothic-styled Prag Mahal and the delicate mirror-adorned corridors of Aina Mahal. Visit the historic Sharad Baug Palace grounds. In the afternoon, your premium private luxury vehicle will transfer you comfortably to Bhuj Airport/Railway Station for your return journey home, carrying unforgettable memories of your premium TRAGUIN experience."
                ),
                [
                    "Sightseeing Included: Aina Mahal Palace, Prag Mahal, Bhuj Royal Cenotaphs.",
                    "Shopping Stops: Luxury stopovers for purchasing elite embroidery artifacts and silver collectibles.",
                    "Meals Included: Full Buffet Breakfast & Farewell Lunch."
                ],
            )
        ],
        hotels=[
            _hotel("Regenta Resort, Bhuj / White Rann Resort (Standard AC Tents)", "Bhuj / Dhordo", "03 Nights", "Deluxe", "Deluxe Room / Standard AC Tent", "All Meals Included", 4, 1),
            _hotel("The Fern Residency, Bhuj / Rann Visamo Village Resort (AC Bhunga)", "Bhuj / Dhordo", "03 Nights", "Premium", "Premium Room / AC Bhunga", "All Meals Included", 5, 2),
            _hotel("Serenity Resort Bhuj / White Rann Resort (Premium Executive Tents)", "Bhuj / Dhordo", "03 Nights", "Luxury", "Executive Room / Premium Executive Tent", "All Meals Included", 5, 3),
            _hotel("Hotel Prince Residency, Bhuj / Official Rann Utsav Tent City (VIP Premium Tents)", "Bhuj / Dhordo", "03 Nights", "Ultra Luxury", "Luxury Suite / VIP Premium Tent", "All Meals + VVIP Club Perks", 5, 4)
        ],
        inclusions=[
            _inc_included("Accommodation: 01 Night luxury stay in Bhuj and 02 Nights stay in premium AC Tents/Bhungas at Dhordo.", 1),
            _inc_included("Meals: Comprehensive gourmet catering plan including 03 Buffet Breakfasts, 03 Lunches, and 03 Festive Dinners.", 2),
            _inc_included("Transfers & Sightseeing: All-inclusive executive sightseeing via a dedicated chauffeur-driven AC Luxury Innova Crysta.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated travel concierge assistance and a professional local accompanying guide.", 4),
            _inc_included("Complimentary Experiences: Private desert camel cart safari and VIP entry credentials for the main Rann Utsav exhibition areas.", 5),
            _inc_included("Welcome Amenities: Executive welcome kit upon arrival with mineral water supplies, organic wet wipes, and a traditional hand-woven Kutchi stole.", 6),
            _inc_excluded("Airfare or Mainline Railway tickets to and from Bhuj city.", 7),
            _inc_excluded("Individual monument photography passes or specific camera admission tickets.", 8),
            _inc_excluded("Personal nature outlays like luxury spa services, laundry bills, premium phone calls, and tips.", 9),
            _inc_excluded("Adventure sports add-ons (like paramotoring or specialized ATV trail riding).", 10),
            _inc_excluded("Personal holiday travel protection insurance or individual emergency medical coverage.", 11)
        ],
    )
    return package, itinerary


def build_gj_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "GJ-014"
    tour_code = "TRAGUIN-GJ-014"
    title = "Heritage Palace Trail Gondal Wankaner"
    duration = "04 Nights / 05 Days"
    slug = "gj-014-heritage-palace-trail-gondal-wankaner"
    itin_slug = "gj-014-heritage-palace-trail-gondal-wankaner-itinerary"
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
            _ph("State / Country: Gujarat / India | Category: Culture & Heritage Luxury", 2),
            _ph("Destinations: Rajkot • Gondal • Wankaner", 3),
            _ph("Ideal for: Heritage Lovers, Connoisseurs & Families", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Luxury Heritage Tour (FIT)", 7),
            _ph("Vehicle: Private Chauffeur-driven Luxury Sedan / SUV (AC Innova Crysta Premium Class)", 8),
            _ph("Meal Plan: Modified American Plan (Gourmet Breakfasts & Royal Palace Dinners Included)", 9),
            _ph("Route Map: Rajkot Arrival → Gondal Royal Estates → Wankaner Palace Stay → Rajkot Departure", 10),
            _ph("TRAGUIN Signature Experience: Curated carefully by TRAGUIN Experts, this journey treats you like a personal guest of the royal families. Enjoy exclusive behind-the-scenes palace access, crowd-free view points, and personalized luxury transportation that elevates your entire holiday experience.", 11),
            _ph("Shopping: Purchase authentic hand-woven cotton textiles, fine brass artifacts, and classical silverware collectibles. Instagram Spots: The vintage carriage house and the grandiose spiral staircases inside Ranjit Vilas Palace. Food Recommendations: Sample authentic Kathiawadi specialities including Ringan No Oro and traditional hot Baajra Roti with fresh local white butter.", 12),
            _ph("Important: Check-in is at 14:00 hours and check-out is at 11:00 hours. Early block allocations are subject to TRAGUIN premium room availability. Welcome Amenities: Royalty greeting ritual including fresh welcome beverages and a personalized travel kit. ✔ Complimentary Experiences: VIP entrance tickets to the Private Vintage Car Collection and special access to Wankaner's royal horse stables. ✔ Domestic or international airfares, train tickets, or airport passenger taxes.✘ Camera charges, professional guide gratuities, and monument fees not detailed in the itinerary.✘ Personal expenditures such as laundry, premium alcoholic beverages, telephone bills, or boutique purchases. ✘ Optional external tours, adventure activities, or additional vehicle mileage outside schedule hours.✘ Comprehensive multi-risk travel or medical emergency insurance coverage.✘ • • • • Dress Codes: While exploring traditional properties, respectful or smart-casual attire is highly recommended. Advance Bookings: Because heritage palace properties have limited inventories, we suggest securing bookings 45–60 days before your travel month.", 13)
        ],
        moods=["Heritage", "Culture", "Luxury"],
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
        tagline="Heritage Palace Trail Gondal Wankaner • Royal Kathiawar Legacy",
        overview=(
            "Unveil the timeless grandeur of India’s most regal state with the Best Gujarat Tour Package. Perfect as an opulent Gujarat Honeymoon Package or an enriching Gujarat Family Tour, the Heritage Palace Trail takes you deep into the legendary kingdoms of Saurashtra. The Premium Gujarat Experience centers around majestic architectural wonders, living museums, and elite vintage collections that populate the top tourist places in Gujarat. Our handpicked luxury heritage hotels bridge old-world aristocracy with 21st-century comfort. While designing these unique TRAGUIN Gujarat Packages, our destination specialists emphasize rich storytelling and exclusive high-end highlights. Experience the Best Time to Visit Gujarat in complete security, moving flawlessly from the intricately carved arches of Gondal to the sweeping panoramic minarets of Wankaner. This is the definitive Gujarat Sightseeing odyssey for discerning travelers who want more than a typical vacation.\n\n"
                        "TRAGUIN Curated Touch: This signature luxury holiday itinerary includes exclusive personal audience opportunities with local estate historians, premium handpicked hotels, dynamic palace view photography access, and curated culinary trails showcasing long- preserved royal Kathiawadi recipes."
        ),
        seo_title="GJ-014 | Heritage Palace Trail Gondal Wankaner | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Gujarat package (GJ-014 / TRAGUIN-GJ-014): Royal Vintage Car Collection, Naulakha Palace, Ranjit Vilas Palace, heritage palace stays, and 4-tier accommodation"
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Arrival Transfer, Leisurely Palace Estate Walk.", 1),
            _ih("Royal Vintage Car Garage, Naulakha Palace Museum, Swaminarayan Temple, Artisan Handloom Center.", 2),
            _ih("Scenic Intercity Drive, Ranjit Vilas Palace Grounds.", 3),
            _ih("TRAGUIN Signature Experience: Curated carefully by TRAGUIN Experts, this journey treats you like a personal guest of the royal families. Enjoy exclusive behind-the-scenes palace access, crowd-free view points, and personalized luxury transportation that elevates your entire holiday experience.", 4),
            _ih("Curated by TRAGUIN Experts: Handpicked luxury hotels and seamless ground logistics", 5),
            _ih("Premium Handpicked Hotels: Properties certified for elite hospitality and safety standards", 6)
        ],
        days=[
            _day(
                1,
                "RAJKOT TO GONDAL",
                (
                    "Arrive at Rajkot Airport where your private elite chauffeur and a professional TRAGUIN ambassador wait to receive you. Board your executive class vehicle for a smooth, scenic drive to the historic princely state of Gondal. Upon reaching the stunning Riverside Palace or Orchard Palace estate, experience a traditional royal greeting with flower garlands and refreshing local welcome drinks. Check-in seamlessly and spend your afternoon unwinding in suites adorned with period-style antiques and historic brass accents."
                ),
                [
                    "Sightseeing Included: Arrival Transfer, Leisurely Palace Estate Walk.",
                    "Evening Experience: Sip high tea by the manicured lawns while reviewing your premium travel itinerary with your TRAGUIN advisor.",
                    "Overnight Stay: Handpicked Premium Heritage Stay (Riverside Palace / Orchard Palace), Gondal.",
                    "Meals Included: Premium High Tea & Welcome Dinner."
                ],
            ),
            _day(
                2,
                "GONDAL HERITAGE TRAIL",
                (
                    "Indulge in a glorious sunrise breakfast within the palace dining pavilion. Today’s immersive experiences begin at the Private Royal Vintage & Classic Car Collection of the Maharaja, showcasing rare automotive wonders from a 1935 Packard to iconic old-world convertibles. Next, journey to the architectural marvel of Naulakha Palace, dating back to the 17th century, to admire its breathtaking stone-carved balconies and historic royal armory. Conclude your day with a special visit to a local Khadi weaving workshop to observe traditional handloom artisans preserving generations of texturing heritage."
                ),
                [
                    "Sightseeing Included: Royal Vintage Car Garage, Naulakha Palace Museum, Swaminarayan Temple, Artisan Handloom Center.",
                    "Photography Points: The legendary stone facades of Naulakha Palace and the polished chrome of the royal vintage cars.",
                    "Overnight Stay: Luxury Heritage Estate, Gondal.",
                    "Meals Included: Full Buffet Breakfast & Royal Traditional Thali Dinner."
                ],
            ),
            _day(
                3,
                "GONDAL TO WANKANER",
                (
                    "Enjoy a lavish breakfast before departing Gondal toward the spellbinding township of Wankaner. The scenic route offers beautiful views of the rugged Kathiawar topography. Arrive at the iconic Ranjit Vilas Palace, perched majestically on a hill overlooking the plains. This architectural masterpiece features an incredible fusion of Gothic, Italianate, and Rajput styles. Check into the royal guest house block, meticulously upgraded into a premium stay, where historic charm meets ultimate modern luxury."
                ),
                [
                    "Sightseeing Included: Scenic Intercity Drive, Ranjit Vilas Palace Grounds.",
                    "Evening Experience: An exclusive curated walkthrough of the palace family collection guided by an expert local companion historian.",
                    "Overnight Stay: Ranjit Vilas Palace Heritage Suite, Wankaner.",
                    "Meals Included: Breakfast & Multi-cuisine Regal Dinner."
                ],
            ),
            _day(
                4,
                "WANKANER PALACE EXPLORATION",
                (
                    "Following a leisurely royal breakfast, dive into a comprehensive exploration of Wankaner's hidden treasures. Admire the three-tiered stepwells located within the estate grounds and discover the palace’s famous clock towers and antique weapon collections. Spend your afternoon soaking in the vintage atmosphere, exploring the royal stables housing fine Kathiawadi horses, or unwinding in the grand drawing rooms that trace decades of diplomatic and noble history."
                ),
                [
                    "Sightseeing Included: Royal Stables, Private Palace Collections, Heritage Stepwells.",
                    "Optional Activities: Sunset photography sessions on the palace terrace overlooking the town of Wankaner.",
                    "Overnight Stay: Ranjit Vilas Palace Heritage Suite, Wankaner.",
                    "Meals Included: Gourmet Breakfast & Farewell Royal Dinner."
                ],
            ),
            _day(
                5,
                "WANKANER TO RAJKOT DEPARTURE",
                (
                    "Cherish a relaxed final breakfast at the palace while taking in the stunning panoramic views one last time. Your premium luxury air-conditioned vehicle will ensure a comfortable transfer back to Rajkot Airport for your return journey home. Your signature TRAGUIN Gujarat Holiday concludes here, leaving you with unforgettable memories of royal Indian hospitality."
                ),
                [
                    "Transfers Included: Private Luxury Airport Drop-off.",
                    "Meals Included: Full Breakfast."
                ],
            )
        ],
        hotels=[
            _hotel("Orchard Palace - Heritage Wing / Royal Oasis Resort", "Gondal / Wankaner", "04 Nights", "Deluxe", "Heritage Room / Deluxe Heritage Wing", "MAP Plan (Breakfast & Dinner)", 4, 1),
            _hotel("Riverside Palace - Deluxe Suite / Palace Guest House Block", "Gondal / Wankaner", "04 Nights", "Premium", "Deluxe Suite / Art-Deco Suite", "MAP Plan (Breakfast & Dinner)", 5, 2),
            _hotel("Riverside Palace - Royal Suite / Ranjit Vilas Heritage Chamber", "Gondal / Wankaner", "04 Nights", "Luxury", "Royal Suite / Heritage Chamber", "MAP Luxury Upgrade Plan", 5, 3),
            _hotel("Orchard Palace - The Maharaja Suite / Ranjit Vilas Palace Royal Suite", "Gondal / Wankaner", "04 Nights", "Ultra Luxury", "Maharaja Suite / Royal Suite", "Ultra-Luxury Full Board & High Tea", 5, 4)
        ],
        inclusions=[
            _inc_included("Accommodation: 04 Nights stay at premier, handpicked heritage hotels and legendary palace properties.", 1),
            _inc_included("Meals: 04 Executive Buffet Breakfasts and 04 tailored fine-dining dinners inside palace banquet halls.", 2),
            _inc_included("Transfers & Sightseeing: All chauffeured transfers and sightseeing journeys via private luxury AC Innova Crysta.", 3),
            _inc_included("TRAGUIN Support: 24/7 priority concierge assistance and certified local companion guides.", 4),
            _inc_included("Welcome Amenities: Royalty greeting ritual including fresh welcome beverages and a personalized travel kit.", 5),
            _inc_included("Complimentary Experiences: VIP entrance tickets to the Private Vintage Car Collection and special access to Wankaner's royal horse stables.", 6),
            _inc_excluded("Domestic or international airfares, train tickets, or airport passenger taxes.", 7),
            _inc_excluded("Camera charges, professional guide gratuities, and monument fees not detailed in the itinerary.", 8),
            _inc_excluded("Personal expenditures such as laundry, premium alcoholic beverages, telephone bills, or boutique purchases.", 9),
            _inc_excluded("Optional external tours, adventure activities, or additional vehicle mileage outside schedule hours.", 10),
            _inc_excluded("Comprehensive multi-risk travel or medical emergency insurance coverage.", 11)
        ],
    )
    return package, itinerary


def build_gj_015(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "GJ-015"
    tour_code = "TRAGUIN-GJ-015"
    title = "Premium Gujarat Heritage Palace Trail"
    duration = "04 Nights / 05 Days"
    slug = "gj-015-premium-gujarat-heritage-palace-trail"
    itin_slug = "gj-015-premium-gujarat-heritage-palace-trail-itinerary"
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
            _ph("State / Country: Gujarat / India | Category: Culture & Heritage", 2),
            _ph("Destinations: Rajkot • Gondal • Wankaner", 3),
            _ph("Ideal for: Heritage Lovers & Families", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Luxury Heritage Tour (FIT)", 7),
            _ph("Vehicle: Private Air-Conditioned Luxury Chauffeur-Driven SUV (Innova Crysta)", 8),
            _ph("Meal Plan: Royal Continental and Traditional Cuisine (Breakfast & Dinners Included)", 9),
            _ph("Route Map: Rajkot Arrival → Gondal Royal Estates → Wankaner Palace Grounds → Rajkot Departure", 10),
            _ph("TRAGUIN Signature Experience: Curated by TRAGUIN Experts, this palace trail features fully personalized assistance, exclusive access paths, and ultra-comfortable luxury transportation. Revel in smooth priority check-ins, curated regional delicacies, and bespoke insider guidance at every grand estate.", 11),
            _ph("Shopping: Acquire beautiful authentic Khadi textiles, traditional hand-woven cotton fabrics, and intricate local woodcraft ornaments. Rajkot Patola: Purchase world-renowned Patola silk sarees, unique mirror-work embroidery pieces, and pristine silver artwork.", 12),
            _ph("Important: Standard palace check-in hours begin at 14:00 hrs and check-out completes by 11:00 hrs. Early access requests depend on TRAGUIN room vacancy reserves. Weather Alert: Saurashtra exhibits warm days and cool, breezy nights. Carrying casual evening layers or a light shawl is highly recommended. Palace Decorum: Certain private sections within active operational royal residences may require modest attire or restricted smartphone photography.", 13)
        ],
        moods=["Heritage", "Culture", "Luxury"],
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
        tagline="Premium Gujarat Heritage Palace Trail • Sleep Like Royalty",
        overview=(
            "Welcome to the land of royal legacies and grand hospitality. This exclusive luxury palace trail curated "
            "by TRAGUIN uncovers the magnificent aristocratic history of Saurashtra. Sleep like royalty in grand "
            "handpicked heritage palaces, marvel at breathtaking royal vintage car collections, and immerse yourself "
            "beautifully in the rich cultural legacy of Wankaner and Gondal.\n\n"
            "The princely state heritage of Saurashtra, Gujarat, provides an unparalleled window into imperial luxury "
            "and architectural brilliance. From exploring the breathtaking Naulakha Palace in Gondal to admiring the "
            "Italianate-Gothic hybrid structures of the Ranjit Vilas Palace in Wankaner, our Luxury Gujarat Holiday "
            "seamlessly brings history to life.\n\n"
            "TRAGUIN Curated Touch: This signature itinerary focuses on private entries into royal garage reserves, "
            "curated palace culinary recipes, and premium stays inside genuine operational royal residencies."
        ),
        seo_title="GJ-015 | Premium Gujarat Heritage Palace Trail | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Gujarat package (GJ-015 / TRAGUIN-GJ-015): Naulakha Palace, Royal Vintage Car Garage, Ranjit Vilas Palace, palace dining, and 4-tier heritage stays"
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Smooth Airport Transfer, Leisure Evening on Palace Grounds.", 1),
            _ih("Naulakha Palace, Royal Vintage Car Garage, Swaminarayan Temple.", 2),
            _ih("Ranjit Vilas Palace Insider Walk, Wankaner Stepwell/Eco-spots.", 3),
            _ih("TRAGUIN Signature Experience: Curated by TRAGUIN Experts, this palace trail features fully personalized assistance, exclusive access paths, and ultra-comfortable luxury transportation. Revel in smooth priority check-ins, curated regional delicacies, and bespoke insider guidance at every grand estate.", 4),
            _ih("Curated by TRAGUIN Experts: Handpicked luxury hotels and seamless ground logistics", 5),
            _ih("Premium Handpicked Hotels: Properties certified for elite hospitality and safety standards", 6)
        ],
        days=[
            _day(
                1,
                "ARRIVAL IN RAJKOT TO GONDAL",
                (
                    "Arrive at Rajkot Airport or Railway Station, where your elite TRAGUIN representative coordinates a seamless traditional welcome. Board your premium private luxury vehicle and transfer through scenic rural landscapes to the historic kingdom of Gondal. Check in to the majestic Riverside Palace or Orchard Palace. Relax in the luxury of high ceilings and authentic antique furniture. Spend your afternoon soaking in the royal gardens before savoring a curated candlelit dinner."
                ),
                [
                    "Sightseeing Included: Smooth Airport Transfer, Leisure Evening on Palace Grounds.",
                    "Evening Experience: Sip customized royal high-tea on the sprawling palace verandas.",
                    "Overnight Stay: Handpicked Luxury Heritage Palace, Gondal.",
                    "Meals Included: Welcome Amenity & Traditional Palace Dinner."
                ],
            ),
            _day(
                2,
                "GONDAL ROYAL SIGHTSEEING",
                (
                    "Indulge in a grand gourmet breakfast. Today, experience iconic attractions within the royal town of Gondal. Visit the spectacular 17th-century Naulakha Palace, boasting breathtaking stone carvings, exquisite balconies, and a stunning collection of princely state scale models. Later, explore the world-renowned Royal Vintage Car Collection of the Maharaja of Gondal, displaying rare classics from Delage to old-world Daimlers. Visit local Khadi weaving centers to appreciate the true culture highlights of Saurashtra."
                ),
                [
                    "Sightseeing Included: Naulakha Palace, Royal Vintage Car Garage, Swaminarayan Temple.",
                    "Photography Points: The shimmering chandeliers of Naulakha and magnificent vintage automotive grids.",
                    "Overnight Stay: Handpicked Luxury Heritage Palace, Gondal.",
                    "Meals Included: Full Buffet Breakfast & Imperial Dinner."
                ],
            ),
            _day(
                3,
                "GONDAL TO WANKANER",
                (
                    "After a relaxed breakfast, check out and drive comfortably towards the scenic hilltop town of Wankaner. Arrive at the striking Ranjit Vilas Palace, a masterpiece blending Italianate, Gothic, and Mughal architecture. Take a private insider tour of the estate with a heritage guide, observing an array of historical weaponry, royal portraits, and magnificent spiral marble staircases. Retreat into your premium stay designed to feel like a timeless royal retreat."
                ),
                [
                    "Sightseeing Included: Ranjit Vilas Palace Insider Walk, Wankaner Stepwell/Eco-spots.",
                    "Evening Experience: A private storytelling session outlining the fascinating princely histories of Wankaner.",
                    "Overnight Stay: Royal Oasis Palace Resort / Heritage Rooms, Wankaner.",
                    "Meals Included: Breakfast & Custom Dinner."
                ],
            ),
            _day(
                4,
                "WANKANER CULTURE & CERAMICS EXCURSION",
                (
                    "Begin your day with a royal breakfast. Discover the culture and craftsmanship of the Wankaner region. Witness a live demonstration of local clay artisans and historic textile pottery. In the afternoon, explore the majestic watchtowers of the old palace complex or simply unwind next to the pristine stepwells within the royal premises. Conclude your day with a special farewell dinner featuring curated authentic recipes."
                ),
                [
                    "Sightseeing Included: Heritage Craft Demonstrations, Palace Watchtowers, Local Architectural Walks.",
                    "Immersive Experiences: Private royal estate dining experience curated uniquely by TRAGUIN experts.",
                    "Overnight Stay: Royal Oasis Palace Resort / Heritage Rooms, Wankaner.",
                    "Meals Included: Breakfast & Farewell Festive Palace Dinner."
                ],
            ),
            _day(
                5,
                "WANKANER TO RAJKOT DEPARTURE",
                (
                    "Savor your final luxury breakfast within the calm palace halls. Check out and board your premium luxury car for a smooth drive back to Rajkot. Take a brief stop to acquire pristine local souvenirs or try legendary street food options before being safely transferred to Rajkot Airport or Station for your onward journey. Your majestic TRAGUIN Gujarat Holiday concludes with beautiful royal memories."
                ),
                [
                    "Transfers Included: Private Chauffeur-Driven Airport/Station Drop-off.",
                    "Meals Included: Full Breakfast."
                ],
            )
        ],
        hotels=[
            _hotel("Orchard Palace (Standard Heritage Room) / Royal Oasis (Deluxe Heritage Wing)", "Gondal / Wankaner", "04 Nights", "Deluxe", "Standard Heritage Room / Deluxe Heritage Wing", "MAP (Breakfast + Dinner)", 4, 1),
            _hotel("Riverside Palace (Executive Suite) / Royal Oasis (Art-Deco Suite)", "Gondal / Wankaner", "04 Nights", "Premium", "Executive Suite / Art-Deco Suite", "MAP (Breakfast + Dinner)", 5, 2),
            _hotel("Riverside Palace (Maharani / Maharaja Suite) / Ranjit Vilas Heritage Residency Wing", "Gondal / Wankaner", "04 Nights", "Luxury", "Maharani / Maharaja Suite / Heritage Residency", "MAP (Royal Culinary Special)", 5, 3),
            _hotel("Orchard Palace (Exclusive Royal Wing) / Ranjit Vilas Palace (VIP Private Guest Chambers)", "Gondal / Wankaner", "04 Nights", "Ultra Luxury", "Exclusive Royal Wing / VIP Private Guest Chambers", "All-Inclusive Palace Premium Plan", 5, 4)
        ],
        inclusions=[
            _inc_included("Accommodation: 04 Nights luxury stay across premium handpicked heritage palaces.", 1),
            _inc_included("Meals: Daily multi-cuisine breakfasts and customized royal dinners inside palace dining halls.", 2),
            _inc_included("Transfers & Sightseeing: Entire journey via private air-conditioned Luxury Innova Crysta with dedicated chauffeur.", 3),
            _inc_included("TRAGUIN Support: 24/7 priority holiday concierge assistance and certified local palace historians.", 4),
            _inc_included("Complimentary Experiences: Private entry ticket pass to Gondal's Maharaja Vintage Car Garage and exclusive palace garden walks.", 5),
            _inc_included("Welcome Amenities: Personalized arrival toolkit including mineral water reserves, royal welcome sweets, and wet-wipes.", 6),
            _inc_excluded("Flight / Train tickets to and from Rajkot.", 7),
            _inc_excluded("Individual entry tickets to monuments or camera passes outside of specified inclusions.", 8),
            _inc_excluded("Personal expenses such as laundry, phone calls, premium spirits, or tips.", 9),
            _inc_excluded("Optional extension excursions or out-of-hours vehicle assignments.", 10),
            _inc_excluded("Mandatory holiday insurance or health coverage plans.", 11)
        ],
    )
    return package, itinerary


def build_gj_016(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "GJ-016"
    tour_code = "TRAGUIN-GJ-016"
    title = "Sasan Gir National Park Special"
    duration = "02 Nights / 03 Days"
    slug = "gj-016-sasan-gir-national-park-special"
    itin_slug = "gj-016-sasan-gir-national-park-special-itinerary"
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
            _ph("State / Country: Gujarat / India | Category: Nature & Wildlife Luxury", 2),
            _ph("Destinations: Sasan Gir National Park • Devalia Safari Park", 3),
            _ph("Ideal for: Wildlife Enthusiasts, Families, Honeymooners", 4),
            _ph("Best season: November to April", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Luxury Wildlife Tour (FIT)", 7),
            _ph("Vehicle: Private AC Luxury SUV for all intercity transfers and resort connections.", 8),
            _ph("Meal Plan: Jungle All-Inclusive Plan (All breakfasts, lunches, and dinners included).", 9),
            _ph("Route Map: Rajkot/Ahmedabad Arrival → Sasan Gir Wildlife Sanctuary → Devalia Zone → Departure", 10),
            _ph("TRAGUIN Signature Experience: Curated carefully by TRAGUIN Experts to offer flawless scheduling. Skip the lines with priority jungle permit arrangements, travel in immaculate premium vehicles, and unlock exclusive handpicked boutique stays with specialized naturalist access.", 11),
            _ph("Shopping: Purchase famous sweet Kesar Mangoes (seasonal) and traditional hand-woven organic cotton garments. Artisanal Crafts: Take home beautiful tribal pottery models and pure forest honey bottles harvested by local communities. • •", 12),
            _ph("Important: Forest permits are non-refundable and require advanced passport/ID copies during booking confirmation. Best Time to Visit: The main park pathways remain open between mid-October to mid-June. Dress Guidelines: Earthy or desaturated colored apparel (khaki, brown, olive green) is highly recommended for safety during open safari drives.", 13)
        ],
        moods=["Wildlife", "Nature", "Luxury"],
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
        tagline="Sasan Gir National Park Special • Kingdom of the Asiatic Lion",
        overview=(
            "As the sole home of the magnificent Asiatic Lion outside of Africa, Sasan Gir stands as a crown jewel in any Luxury Gujarat Holiday. Travelers searching for the definitive Gujarat Family Tour or a romance-filled Gujarat Honeymoon Package will find the dramatic wilderness, scenic beauty, and diverse flora and fauna of the park completely spellbinding. From adrenaline-fueled encounters with apex predators during a Gujarat Sightseeing drive to the rich cultural encounters with local Maldhari tribes, our handpicked hotels offer world-class spa amenities, private plunge pools, and organic dining. Let TRAGUIN Gujarat Packages guide your family into the wild with unrivaled refinement and safety.\n\n"
                        "TRAGUIN Curated Touch: Includes pre-booked open-gypsy jungle safari permits, certified expert tribal track-finders, luxury resort campfire evenings, and dedicated 24/7 client coordination."
        ),
        seo_title="GJ-016 | Sasan Gir National Park Special | TRAGUIN",
        seo_description=(
            "Premium 02 Nights / 03 Days Gujarat package (GJ-016 / TRAGUIN-GJ-016): Core zone jungle safari, Devalia Safari Park, Siddi tribal dance, forest resort stays, and 4-tier accommodation"
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Resort Wilderness Walk, Tribal Village Orientation.", 1),
            _ih("Morning Core Zone Safari, Afternoon Devalia Safari Park Tour.", 2),
            _ih("TRAGUIN Signature Experience: Curated carefully by TRAGUIN Experts to offer flawless scheduling. Skip the lines with priority jungle permit arrangements, travel in immaculate premium vehicles, and unlock exclusive handpicked boutique stays with specialized naturalist access.", 3),
            _ih("Curated by TRAGUIN Experts: Handpicked luxury hotels and seamless ground logistics", 4),
            _ih("Premium Handpicked Hotels: Properties certified for elite hospitality and safety standards", 5)
        ],
        days=[
            _day(
                1,
                "ARRIVAL SASAN GIR",
                (
                    "Arrive at Rajkot / Diu / Ahmedabad airport where your private luxury chauffeur welcomes you with warm traditional hospitality. Enjoy a scenic, smooth drive into the lush peripheries of Sasan Gir National Park. Check into your stunning premium eco-luxury forest resort. Spend your afternoon relaxing by the poolside or listening to the soothing sounds of the Hiran River. In the evening, attend an exclusive wildlife orientation briefing hosted by your expert companion guide."
                ),
                [
                    "Sightseeing Included: Resort Wilderness Walk, Tribal Village Orientation.",
                    "Evening Experience: Local Siddi Tribal Dhamal Folk Dance show arranged exclusively at the resort lounge.",
                    "Overnight Stay: Ultra-Luxury Wilderness Resort, Sasan Gir.",
                    "Meals Included: Welcome Drink, Gourmet Lunch & Organic Dinner."
                ],
            ),
            _day(
                2,
                "SASAN GIR NATIONAL PARK",
                (
                    "Wake up to the crisp morning calls of the forest. Sip fresh organic coffee before boarding your pre- arranged, private 4x4 open-top safari gypsy. Head deep into the core zones of Sasan Gir National Park during the prime hours of wildlife activity. Under the watchful guidance of your expert tracker, search for the majestic Asiatic Lion, elusive leopards, striped hyenas, and spotted deer. Return to the resort for a grand celebratory buffet lunch. In the late afternoon, enjoy an immersive driving experience through the Devalia Safari Park zone to guarantee beautiful up-close wildlife photography."
                ),
                [
                    "Sightseeing Included: Morning Core Zone Safari, Afternoon Devalia Safari Park Tour.",
                    "Photography Points: Golden hour sunrays piercing through teak forests, close-up frames of predatory bird species.",
                    "Overnight Stay: Ultra-Luxury Wilderness Resort, Sasan Gir.",
                    "Meals Included: Jungle Breakfast, Luxury Lunch, and Farewell Barbecue Dinner."
                ],
            ),
            _day(
                3,
                "DEPARTURE FROM SASAN GIR",
                (
                    "Indulge in a luxurious, leisurely breakfast amidst nature. Take a quiet final stroll through the resort's organic gardens. Check out seamlessly as your premium private vehicle arrives to transfer you comfortably back to the airport or railway station for your onward travel home. Your ultra-premium jungle escape wraps up with magnificent stories and memories to cherish forever."
                ),
                [
                    "Transfers Included: Private Airport/Station Departure Drop.",
                    "Meals Included: Full Buffet Breakfast."
                ],
            )
        ],
        hotels=[
            _hotel("Gir Birding Lodge", "Sasan Gir", "02 Nights", "Deluxe", "Forest Cottage", "APAI (All Meals Included)", 4, 1),
            _hotel("The Fern Gir Forest Resort", "Sasan Gir", "02 Nights", "Premium", "Fern Club Villa", "APAI (All Meals Included)", 5, 2),
            _hotel("Woods at Sasan", "Sasan Gir", "02 Nights", "Luxury", "Luxury Pavilion Studio", "APAI + Wellness Sessions", 5, 3),
            _hotel("Aramness Gir Wildlife Lodge", "Sasan Gir", "02 Nights", "Ultra Luxury", "Standalone Kothi with Private Pool", "Ultra-All-Inclusive + Private Butler", 5, 4)
        ],
        inclusions=[
            _inc_included("Accommodation: 02 Nights stay at handpicked premium luxury forest resorts.", 1),
            _inc_included("Meals: All daily breakfasts, premium multi-cuisine lunches, and forest dinners.", 2),
            _inc_included("Transfers & Sightseeing: Dedicated Chauffeur-driven air-conditioned private luxury vehicle for all point-to- point connections.", 3),
            _inc_included("TRAGUIN Support: 24/7 real-time concierge and certified wildlife track companion assistance.", 4),
            _inc_included("Complimentary Experiences: Standard pre-booked safari permit processing fee, high-tea over riverbanks, and tribal interaction walks.", 5),
            _inc_excluded("Airfare or main railway tickets to the arrival gateway.", 6),
            _inc_excluded("Camera lens charges or separate forest department entry taxes.", 7),
            _inc_excluded("Personal items such as laundry, phone calls, or spa treatment requests.", 8),
            _inc_excluded("Gratuities for safari drivers and local naturalists.", 9)
        ],
    )
    return package, itinerary


def build_gj_017(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "GJ-017"
    tour_code = "TRAGUIN-GJ-017"
    title = "Saputara Hill Station Escape"
    duration = "02 Nights / 03 Days"
    slug = "gj-017-saputara-hill-station-escape"
    itin_slug = "gj-017-saputara-hill-station-escape-itinerary"
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
            _ph("State / Country: Gujarat / India | Category: Weekend Gateway / Luxury", 2),
            _ph("Destinations: Saputara Hill Station • Gira Waterfalls", 3),
            _ph("Ideal for: Families, Couples & Corporate Elites", 4),
            _ph("Best season: Monsoon & Winter (July to March)", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Luxury Weekend Getaway (FIT)", 7),
            _ph("Vehicle: Private Air-Conditioned Premium Luxury Sedan / SUV", 8),
            _ph("Meal Plan: Modified American Plan (Daily Gourmet Breakfast & Dinners)", 9),
            _ph("Route Map: Surat/Nashik Arrival → Saputara Lake → Sunset Point → Gira Waterfalls → Departure", 10),
            _ph("TRAGUIN Signature Experience: Curated carefully by TRAGUIN Experts to maximize premium holiday comfort. • Exclusive Recommendations: VIP line-skipping passes for the Ropeway ride during crowded holiday weekends. • Personalized Assistance: Enjoy premium handpicked hotels, highly trained local drivers, and tailored photography points across the route.", 11),
            _ph("Shopping: Pick up authentic bamboo crafts, dynamic tribal pottery, and pure forest honey from the Dangs cooperative markets. Instagram Spots: The beautiful lake mist during morning hours and the sunset perspective from Pushpak Cable Car.", 12),
            _ph("Important: Check-in time is 14:00 hrs; check-out is 11:00 hrs. Early access depends on room availability. Weather Aspect: Heavy mist covers the region during monsoons; temperatures drop in winters. Carrying a light windcheater or fleece jacket is highly recommended. Advance Booking Suggestions: Weekend luxury properties sell out fast; booking 3-4 weeks ahead ensures premium room categories.", 13)
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
        tagline="Saputara Hill Station Escape • Misty Sahyadri Retreat",
        overview=(
            "Are you planning the perfect Saputara Honeymoon Package or a refreshing Saputara Family Tour? As the crown jewel of tourism in South Gujarat, Saputara Hill Station stands as one of the most searched weekend getaway hubs. It offers an incredible combination of rich tribal culture, biological reserves, and scenic beauty that satisfies any refined traveler looking for a high-end escape. From exploring the misty banks of Saputara Lake to capturing spectacular snapshots at the top popular Instagram locations like Governor’s Hill and Sunrise Point, our premium itinerary secures the finest highlights. Experience the Best Time to Visit Saputara with TRAGUIN Saputara Packages, taking advantage of exclusive access, curated sightseeing paths, and elite wellness amenities hidden within the tranquil woods.\n\n"
                        "TRAGUIN Curated Touch: Indulge in a premium Saputara experience featuring handpicked hotels with direct valley views, a private cable car glide over misty gorges, and local tribal art interactions tailored seamlessly for an unparalleled luxurious family or couple vacation."
        ),
        seo_title="GJ-017 | Saputara Hill Station Escape | TRAGUIN",
        seo_description=(
            "Premium 02 Nights / 03 Days Gujarat package (GJ-017 / TRAGUIN-GJ-017): Saputara Lake, Pushpak Ropeway, Artist Village, Sunset Point, Gira Waterfalls, and 4-tier hill resorts"
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Saputara Lake, Step Garden, Lake Promenade Walk.", 1),
            _ih("Pushpak Ropeway, Artist Village, Governor's Hill, Sunset Point.", 2),
            _ih("Gira Waterfalls, Waghai Botanical Garden.", 3),
            _ih("TRAGUIN Signature Experience: Curated carefully by TRAGUIN Experts to maximize premium holiday comfort. • Exclusive Recommendations: VIP line-skipping passes for the Ropeway ride during crowded holiday weekends. • Personalized Assistance: Enjoy premium handpicked hotels, highly trained local drivers, and tailored photography points across the route.", 4),
            _ih("Curated by TRAGUIN Experts: Handpicked luxury hotels and seamless ground logistics", 5),
            _ih("Premium Handpicked Hotels: Properties certified for elite hospitality and safety standards", 6)
        ],
        days=[
            _day(
                1,
                "ARRIVAL & SAPUTARA LAKE CHRONICLES",
                (
                    "Arrive at Surat Airport or Nashik Railway Station where your professional TRAGUIN chauffeur welcomes you. Embark on a breathtakingly scenic mountain road climb winding through lush bamboo groves and cascading valleys. Arrive at Saputara Hill Station and experience a seamless priority check-in at your handpicked luxury resort. In the late afternoon, enjoy a relaxing private boat cruise across the calm waters of Saputara Lake, surrounded by towering trees and rolling clouds. As evening colors fill the sky, stroll through the vibrant Step Garden for spectacular photography points."
                ),
                [
                    "Sightseeing Included: Saputara Lake, Step Garden, Lake Promenade Walk.",
                    "Evening Experience: Local hot-spiced premium tea session hosted by the lakeside.",
                    "Overnight Stay: Ultra-Luxury Resort with Valley View, Saputara.",
                    "Meals Included: Welcome Signature Drink & Curated Buffet Dinner."
                ],
            ),
            _day(
                2,
                "ICONIC ATTRACTIONS & VALLEYS",
                (
                    "Savor a luxurious morning breakfast overlooking the mist-filled valley. Today, dive into the ultimate Saputara Sightseeing collection. Take an exclusive private cable car (Pushpak Ropeway) ride that glides effortlessly over high mountain chasms, offering panoramic views of the dense Dangs forest. Visit the fascinating Artist Village to interact with tribal artisans and witness authentic Warli paintings. In the evening, your vehicle takes you up to the majestic Sunset Point, where you will witness the sun melting beautifully behind the Sahyadri mountains—creating unforgettable memories."
                ),
                [
                    "Sightseeing Included: Pushpak Ropeway, Artist Village, Governor's Hill, Sunset Point.",
                    "Optional Activities: Paragliding from Governor's hill (seasonal/weather permitting).",
                    "Overnight Stay: Ultra-Luxury Resort with Valley View, Saputara.",
                    "Meals Included: Premium Breakfast & Candlelit Theme Dinner."
                ],
            ),
            _day(
                3,
                "GIRA WATERFALLS & DEPARTURE",
                (
                    "After an early gourmet breakfast, check out and drive towards the spectacular Gira Waterfalls, a magnificent 75-foot natural drop that roars majestically into the Ambika River (best viewed during monsoon and winter seasons). Capture stunning panoramic photos and breathe in the refreshing forest spray. Afterwards, your luxury private vehicle ensures a smooth, comfortable drive back to Surat or Nashik to catch your onward flight or train, concluding your premium TRAGUIN Saputara Experience."
                ),
                [
                    "Sightseeing Included: Gira Waterfalls, Waghai Botanical Garden.",
                    "Food Suggestions: Enjoy authentic hot local organic corn delicacies near the falls.",
                    "Meals Included: Full Buffet Breakfast."
                ],
            )
        ],
        hotels=[
            _hotel("Patang Residency, Saputara", "Saputara", "02 Nights", "Deluxe", "Premium Lake View Room", "MAP (Breakfast + Dinner)", 4, 1),
            _hotel("Savshanti Hill Resort", "Saputara", "02 Nights", "Premium", "Super Deluxe Valley View Room", "MAP (Breakfast + Dinner)", 5, 2),
            _hotel("Aakar Lords Inn, Saputara", "Saputara", "02 Nights", "Luxury", "Elite Pavilion Club Room", "MAP (Breakfast + Dinner)", 5, 3),
            _hotel("Sunil Resort / Villa Luxury Suites", "Saputara", "02 Nights", "Ultra Luxury", "Grand Presidential Suite with Private Jacuzzi", "MAP Premium Dining", 5, 4)
        ],
        inclusions=[
            _inc_included("Accommodation: 02 Nights premium stay at handpicked luxury hotels with sweeping valley/lake views.", 1),
            _inc_included("Meals: 02 Lavish Multi-cuisine Breakfasts & 02 Chef-curated Dinners at premium hotel restaurants.", 2),
            _inc_included("Transfers & Sightseeing: All point-to-point tours via private premium air-conditioned luxury transportation.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated digital concierge assistance and personalized itinerary tracking.", 4),
            _inc_included("Welcome Amenities: Refreshing wellness drink on arrival and complimentary basket of local artisanal fresh fruits.", 5),
            _inc_included("Complimentary Experiences: Exclusive ticket access to the Pushpak Ropeway cable car and private boating pass.", 6),
            _inc_excluded("Flight tickets or train fares from your home destination.", 7),
            _inc_excluded("Any personal shopping expenses, premium mini-bar bills, and laundry service charges.", 8),
            _inc_excluded("Entry tickets to adventure activity parks or camera charges at sites.", 9),
            _inc_excluded("Optional tours, extensions, or detour mileage fees not mentioned.", 10)
        ],
    )
    return package, itinerary


def build_gj_018(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "GJ-018"
    tour_code = "TRAGUIN-GJ-018"
    title = "Palitana & Ambaji Divine Circuit Tour"
    duration = "05 Nights / 06 Days"
    slug = "gj-018-palitana-ambaji-divine-circuit-tour"
    itin_slug = "gj-018-palitana-ambaji-divine-circuit-tour-itinerary"
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
            _ph("State / Country: Gujarat / India | Category: Pilgrimage / Divine Circuit", 2),
            _ph("Destinations: Ahmedabad • Palitana • Bhavnagar • Ambaji", 3),
            _ph("Ideal for: Families, Seniors & Pilgrims", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Luxury Pilgrimage Circuit (FIT)", 7),
            _ph("Vehicle: Dedicated Luxury Chauffeur- Driven Air-Conditioned Innova Crysta / Premium Sedan", 8),
            _ph("Meal Plan: Modified American Plan (Daily Premium Buffet Breakfast & Authentic Pure- Vegetarian Dinners)", 9),
            _ph("Route Map: Ahmedabad → Bhavnagar → Palitana Hills → Ahmedabad → Ambaji → Ahmedabad Departure", 10),
            _ph("TRAGUIN Signature Experience: Curated by TRAGUIN Experts, this divine pilgrimage balances strict dietary needs with executive transport accessibility. Enjoy VIP priority assistance across sacred places, private check-ins, and curated culinary experiences designed uniquely for a premium family holiday.", 11),
            _ph("Shopping: Law Garden and Ratanpole for traditional Chaniya Cholis, Patola sarees, and authentic handloom fabrics. Spiritual Keepsakes: Blessed marble miniature shrines from Palitana and sacred kumkum tokens from Ambaji.", 12),
            _ph("Important: Pure-vegetarian rules are strictly maintained across all listed properties and partner resorts. Dress Codes: Respectful clothing covering shoulders and knees is mandatory for entries to Palitana and Ambaji temples. Advance Booking Suggestions: Securing your doli services at Palitana 3-4 weeks in advance through your TRAGUIN consultant is recommended.", 13)
        ],
        moods=["Spiritual", "Heritage", "Culture"],
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
        tagline="Palitana & Ambaji Divine Circuit Tour • Sacred Western India",
        overview=(
            "Embark on a sacred journey into the spiritual heart of Western India with our exclusive Gujarat Family Tour "
            "and Honeymoon Package collections. Carefully designed by TRAGUIN travel consultants, this premium "
            "pilgrimage circuit takes you across breathtaking landscapes to the timeless holy hill of Palitana and the "
            "highly revered shaktipeeth of Ambaji. Experience absolute serenity and immersive experiences through "
            "handpicked hotels, seamless premium stays, and luxury private transport.\n\n"
            "Gujarat is universally renowned for its timeless sacred architecture, incredible archaeological heritage, "
            "and exceptional hospitality. Our circuit combines the world's most unique Jain temple city, Palitana, "
            "boasting over 800 beautifully hand-carved marble temples atop Mount Shatrunjaya, alongside the ancient "
            "powers of Ambaji temple nested in the Aravalli ranges.\n\n"
            "TRAGUIN Curated Touch: This Premium Gujarat Experience provides senior-friendly customized paces, VIP "
            "temple darshan coordination, premium doli/palki pre-arrangements for Shatrunjaya hill climbs, and local "
            "companion destination experts ensuring an unforgettable memory."
        ),
        seo_title="GJ-018 | Palitana & Ambaji Divine Circuit Tour | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days Gujarat package (GJ-018 / TRAGUIN-GJ-018): Mount Shatrunjaya temples, Sabarmati Ashram, Ambaji Shaktipeeth, Gabbar Hill Ropeway, and 4-tier hotels"
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Scenic Transfer, Nilambag Heritage Compound walk.", 1),
            _ih("Mount Shatrunjaya Temples, Adishwar Temple, Chaumukha Complex.", 2),
            _ih("Sabarmati Ashram, Adalaj Stepwell, Akshardham Temple (Laser Show optional).", 3),
            _ih("TRAGUIN Signature Experience: Curated by TRAGUIN Experts, this divine pilgrimage balances strict dietary needs with executive transport accessibility. Enjoy VIP priority assistance across sacred places, private check-ins, and curated culinary experiences designed uniquely for a premium family holiday.", 4),
            _ih("Curated by TRAGUIN Experts: Handpicked luxury hotels and seamless ground logistics", 5),
            _ih("Premium Handpicked Hotels: Properties certified for elite hospitality and safety standards", 6)
        ],
        days=[
            _day(
                1,
                "ARRIVAL IN AHMEDABAD TO BHAVNAGAR",
                (
                    "Arrive at Ahmedabad Airport/Railway Station, where your elite TRAGUIN tour representative welcomes you with specialized assistance. Board your private luxury vehicle and commence your scenic beauty drive to Bhavnagar. Upon arrival, check in smoothly to your premium handpicked heritage hotel. Spend a relaxed evening exploring the breathtaking landscapes of Nilambag Palace or enjoying quiet meditation."
                ),
                [
                    "Sightseeing Included: Scenic Transfer, Nilambag Heritage Compound walk.",
                    "Evening Experience: A refreshing high-tea briefing with curated recommendations from your travel consultant.",
                    "Overnight Stay: Premium Luxury Heritage Stay, Bhavnagar.",
                    "Meals Included: Welcome Drink & Gourmet Vegetarian Dinner."
                ],
            ),
            _day(
                2,
                "BHAVNAGAR – PALITANA SACRED DARSHAN",
                (
                    "Wake up early for an extraordinary day of Palitana Sightseeing. Drive to the base of Mount Shatrunjaya. For maximum senior citizen comfort, premium pre-arranged Palki / Doli services can be availed to ascend the sacred hill gracefully. Witness the sunrise illuminating hundreds of spectacular marble carvings. Spend an immersive day seeking divine blessings before descending for a traditional, pristine lunch at the foothills."
                ),
                [
                    "Sightseeing Included: Mount Shatrunjaya Temples, Adishwar Temple, Chaumukha Complex.",
                    "Photography Points: Panorama of the Shetrunji river from the fortressed peak walls.",
                    "Overnight Stay: Handpicked Luxury Resort / Premium Hotel, Palitana / Bhavnagar.",
                    "Meals Included: Early Breakfast & Pure Satvik Dinner."
                ],
            ),
            _day(
                3,
                "PALITANA / BHAVNAGAR TO AHMEDABAD",
                (
                    "After a premium breakfast, proceed on a relaxing drive back to Ahmedabad, the historic mega-city of Gujarat. Check in to your luxury urban oasis hotel. In the afternoon, enjoy iconic attractions like the peaceful Sabarmati Ashram and the architectural marvel of Adalaj Stepwell, capturing perfect Instagram locations along the way."
                ),
                [
                    "Sightseeing Included: Sabarmati Ashram, Adalaj Stepwell, Akshardham Temple (Laser Show optional).",
                    "Evening Experience: Leisurely stroll or shopping for authentic Patola and Bandhani handlooms.",
                    "Overnight Stay: Premium Luxury Hotel, Ahmedabad.",
                    "Meals Included: Rich Traditional Breakfast & Multicuisine Dinner."
                ],
            ),
            _day(
                4,
                "AHMEDABAD TO AMBAJI SHAKTIPEETH",
                (
                    "Journey northward today towards the pristine Aravalli mountain borders to reach Ambaji, one of the primary 51 Shaktipeeths of India. Arrive and check into your handpicked premium luxury stay. As dusk falls, join the majestic evening prayer circle at the main temple, observing the sacred Akhand Divo that has burned for centuries."
                ),
                [
                    "Sightseeing Included: Main Ambaji Temple Compound, Holy Heritage Walks.",
                    "Optional Activities: Spend the afternoon at leisure amidst lush hill surrounds.",
                    "Overnight Stay: Premium Luxury Stay, Ambaji.",
                    "Meals Included: Full Breakfast & Divine Temple-Style Dinner."
                ],
            ),
            _day(
                5,
                "GABBAR HILL EXPLORATION TO AHMEDABAD",
                (
                    "Visit the historical Gabbar Hill early today, the exact original site of the divine manifestation. Board a safe, smooth premium ropeway cabin to glide effortlessly to the hilltop temple shrine. View the holy footprints of Goddess Amba and take in the beautiful scenery. Later, enjoy a smooth return highway drive back to Ahmedabad."
                ),
                [
                    "Sightseeing Included: Gabbar Hill Ropeway Experience, Kamakshi Devi Temple Complex.",
                    "Overnight Stay: Luxury Premium Stay, Ahmedabad.",
                    "Meals Included: Buffet Breakfast & Festive Farewell Dinner."
                ],
            ),
            _day(
                6,
                "DEPARTURE FROM AHMEDABAD",
                (
                    "Savor your lavish morning breakfast at the hotel. If flight timings permit, visit local handloom craft outlets for fine Gujarati handicraft souvenirs. Your private luxury car will arrive precisely to drop you off at Ahmedabad Airport or Railway Station, bringing your premium TRAGUIN pilgrimage package to a blissful conclusion."
                ),
                [
                    "Transfers Included: Private Airport/Station drop-off service.",
                    "Meals Included: Gourmet Buffet Breakfast."
                ],
            )
        ],
        hotels=[
            _hotel("Efcee Sarovar Portico / Lemon Tree Premier / Vivanta Inn", "Bhavnagar / Ahmedabad / Ambaji", "05 Nights", "Deluxe", "Deluxe Room / Standard Room", "MAP (Breakfast + Dinner)", 4, 1),
            _hotel("Iscon Club & Resort / Radisson Blu Ahmedabad / Hotel Ambaji International", "Bhavnagar / Ahmedabad / Ambaji", "05 Nights", "Premium", "Premium Room / Club Room", "MAP (Breakfast + Dinner)", 5, 2),
            _hotel("Nilambag Palace Heritage Hotel / ITC Narmada Luxury Hotel / The Grand Ambaji Resort", "Bhavnagar / Ahmedabad / Ambaji", "05 Nights", "Luxury", "Heritage Room / Executive Room / Luxury Suite", "MAP (Breakfast + Dinner)", 5, 3),
            _hotel("The Blackbuck Lodge (Velavadar) / The Leela Gandhinagar / VIP Heritage Suite Executive", "Bhavnagar / Ahmedabad / Ambaji", "05 Nights", "Ultra Luxury", "Presidential Suite / Royal Suite / VIP Heritage Suite", "Gourmet MAP Premium Plan", 5, 4)
        ],
        inclusions=[
            _inc_included("Accommodation: 05 Nights stay at handpicked premium luxury hotels and heritage palaces.", 1),
            _inc_included("Meals: Daily premium breakfast buffet and multi-course pure vegetarian dinners.", 2),
            _inc_included("Transfers & Sightseeing: All luxury transportation in AC Innova Crysta with a dedicated chauffeur.", 3),
            _inc_included("Assistance & Taxes: 24/7 dedicated local concierge support and all applicable luxury resort taxes.", 4),
            _inc_included("Welcome Amenities: Specialized premium welcome kit with traditional stoles and healthy mineral water.", 5),
            _inc_included("Complimentary Experiences: Pre-booked premium tickets for the Gabbar Hill Ropeway.", 6),
            _inc_excluded("Airfare or interstate train tickets to Ahmedabad.", 7),
            _inc_excluded("Individual doli/palki or porter charges during the Palitana climb.", 8),
            _inc_excluded("Personal elements such as laundry, specialized telephone calls, and custom tips.", 9),
            _inc_excluded("Entrance tickets or camera passes inside monument compounds.", 10),
            _inc_excluded("Any optional tour modifications not detailed above.", 11)
        ],
    )
    return package, itinerary


def build_gj_019(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "GJ-019"
    tour_code = "TRAGUIN-GJ-019"
    title = "Polo Forest Weekend Exploration"
    duration = "02 Nights / 03 Days"
    slug = "gj-019-polo-forest-weekend-exploration"
    itin_slug = "gj-019-polo-forest-weekend-exploration-itinerary"
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
            _ph("State / Country: Gujarat / India | Category: Offbeat / Nature Escape", 2),
            _ph("Destinations: Ahmedabad • Polo Forest • Vijaynagar", 3),
            _ph("Ideal for: Families, Couples & Nature Lovers", 4),
            _ph("Best season: September to March (Monsoon & Winter)", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Customized Luxury Nature Escape (FIT)", 7),
            _ph("Vehicle: Dedicated Executive Luxury SUV (Innova Crysta)", 8),
            _ph("Meal Plan: All Meals Included (Breakfast, Traditional Lunch, & Gourmet Dinner)", 9),
            _ph("Route Map: Ahmedabad Arrival → Polo Forest (Vijaynagar) → Heritage Exploration → Ahmedabad Departure", 10),
            _ph("TRAGUIN Signature Experience: Curated meticulously by TRAGUIN experts to bring forward a perfect balance of heritage and relaxation. Our handpicked premium hotels guarantee absolute luxury, while our specialized routes minimize driving fatigue, making this weekend getaway completely blissful.", 11),
            _ph("Shopping: Shop for traditional pottery, tribal bamboo artworks, and exquisite handwoven garments from nearby Idar and Vijaynagar markets. • • • • • • • • • • • • • •", 12),
            _ph("Important: Standard eco-resort check-in is at 14:00 hrs and check-out is at 11:00 hrs. Weather & Clothing: Light breathable cotton clothing is recommended for daytime exploration; carrying good walking or hiking shoes is necessary for forest trails. Network Advisory: Mobile network inside dense parts of Polo Forest can be limited, helping you enjoy an uninterrupted digital detox experience.", 13)
        ],
        moods=["Nature", "Heritage", "Weekend"],
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
        tagline="Polo Forest Weekend Exploration • Hidden Jungle Sanctuary",
        overview=(
            "Tucked away near Vijaynagar, Polo Forest is one of the most stunning hidden gems in Western India, perfect for a rejuvenating Gujarat Family Tour or an offbeat Gujarat Honeymoon Package. Known for its historical significance and breathtaking landscapes, this sanctuary hosts ancient Hindu and Jain temple architectures seamlessly entwined with wild jungle vines and the gentle flow of the Harnav River. As one of the highly searched Top Tourist Places in Gujarat, visitors are drawn to its unique ecosystem, scenic beauty, and rich bio-diversity. The Best Time to Visit Gujarat's Polo Forest is right after the monsoon rains when the waterfalls are cascading and the foliage turns completely emerald green. Choosing our tailored TRAGUIN Gujarat Packages ensures premium stays, exclusive access to historical secrets, and unforgettable memories for your loved ones.\n\n"
                        "TRAGUIN Curated Touch: Enjoy an immersive nature trail led by certified naturalists, exclusive campfire storytelling sessions under the stars, premium handpicked eco-resort accommodations, and priority travel assistance."
        ),
        seo_title="GJ-019 | Polo Forest Weekend Exploration | TRAGUIN",
        seo_description=(
            "Premium 02 Nights / 03 Days Gujarat package (GJ-019 / TRAGUIN-GJ-019): Sharaneshwar Temple, Lakhena ruins, Vanaj Dam, Harnav River trails, eco-resort stays, and 4-tier accommodation"
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Riverside Walking Trails, Eco-Resort orientation.", 1),
            _ih("Sharaneshwar Temple, Lakhena Temple Ruins, Vanaj Dam, Harnav River Walk.", 2),
            _ih("En-route photography points, Ahmedabad Departure Transfer.", 3),
            _ih("TRAGUIN Signature Experience: Curated meticulously by TRAGUIN experts to bring forward a perfect balance of heritage and relaxation. Our handpicked premium hotels guarantee absolute luxury, while our specialized routes minimize driving fatigue, making this weekend getaway completely blissful.", 4),
            _ih("Curated by TRAGUIN Experts: Handpicked luxury hotels and seamless ground logistics", 5),
            _ih("Premium Handpicked Hotels: Properties certified for elite hospitality and safety standards", 6)
        ],
        days=[
            _day(
                1,
                "ARRIVAL AHMEDABAD TO POLO FOREST",
                (
                    "Arrive at Ahmedabad Airport/Railway Station where your private chauffeur welcomes you. Board your luxury sedan/SUV and embark on a scenic drive toward the pristine wilderness of Vijaynagar. Upon arrival at Polo Forest, check in seamlessly to your premium handpicked eco-luxury resort. After refreshing yourself, enjoy a peaceful guided orientation walk around the Harnav River bank, soaking in the serene evening breeze."
                ),
                [
                    "Sightseeing Included: Riverside Walking Trails, Eco-Resort orientation.",
                    "Evening Experience: A warm welcome high-tea followed by an introductory presentation about Polo Forest's biodiversity.",
                    "Overnight Stay: Handpicked Luxury Eco-Resort, Polo Forest.",
                    "Meals Included: Traditional Lunch & Gourmet Dinner."
                ],
            ),
            _day(
                2,
                "POLO FOREST SIGHTSEEING",
                (
                    "Awake to the peaceful chirping of exotic birds. Today features a complete day of deep, immersive exploration. Visit the iconic 15th-century Sharaneshwar Shiva Temple, featuring gorgeous stone carvings without a roof. Explore the ancient Jain temples hidden deep within the foliage, followed by a visit to the historic Lakhena Jain Temple ruins. In the afternoon, visit the massive Vanaj Dam, an incredible photography point offering panoramic views of the water reservoir nestled among mountains."
                ),
                [
                    "Sightseeing Included: Sharaneshwar Temple, Lakhena Temple Ruins, Vanaj Dam, Harnav River Walk.",
                    "Local Experiences: A curated nature walk with an expert naturalist identifying medicinal flora and bird species.",
                    "Overnight Stay: Premium Eco-Resort, Polo Forest.",
                    "Meals Included: Full Breakfast, Picnic Lunch & Campfire Dinner."
                ],
            ),
            _day(
                3,
                "POLO FOREST TO AHMEDABAD DEPARTURE",
                (
                    "Indulge in a luxurious early morning breakfast amidst nature. Take a final stroll around the manicured paths of your forest property or capture the early morning sun filtering through the dense canopy at popular Instagram locations. Check out from your resort and drive comfortably back to Ahmedabad. If time permits, enjoy brief historical Gujarat Sightseeing options in Ahmedabad before dropping off at the airport/station for your onward journey."
                ),
                [
                    "Sightseeing Included: En-route photography points, Ahmedabad Departure Transfer.",
                    "Meals Included: Full Buffet Breakfast."
                ],
            )
        ],
        hotels=[
            _hotel("Polo Retreat Resort", "Polo Forest", "02 Nights", "Deluxe", "Deluxe Forest Room", "API (All Meals Included)", 4, 1),
            _hotel("Polo Tent City & Resort", "Polo Forest", "02 Nights", "Premium", "Premium Luxury Cottage", "API (All Meals Included)", 5, 2),
            _hotel("The Fern Forest Resort, Polo Forest", "Polo Forest", "02 Nights", "Luxury", "Winter Green Room", "API Premium Plan", 5, 3),
            _hotel("The Fern Forest Resort (Premium Villa Wing)", "Polo Forest", "02 Nights", "Ultra Luxury", "Fern Club Studio Villa with Deck", "API Premium Plan", 5, 4)
        ],
        inclusions=[
            _inc_included("Accommodation: 02 Nights stay at handpicked luxury forest resorts / tent properties.", 1),
            _inc_included("Meals: Complete plan covering all breakfasts, traditional lunches, and dinners as per itinerary.", 2),
            _inc_included("Transfers & Sightseeing: Chauffeur-driven executive luxury private vehicle (AC on hills turned off for safety).", 3),
            _inc_included("Assistance: Personalized 24/7 remote operations support and expert trip curation.", 4),
            _inc_included("Taxes: All applicable luxury resort taxes, state highway toll permits, and parking.", 5),
            _inc_included("Welcome Amenities: Handcrafted welcome refresher drinks and custom forest exploration guide kit.", 6),
            _inc_included("Complimentary Experiences: Guided nature exploration walk with a professional local naturalist.", 7),
            _inc_included("TRAGUIN Support: Priority support desk access throughout the short holiday.", 8),
            _inc_excluded("Airfare or interstate train tickets arriving into Ahmedabad.", 9),
            _inc_excluded("Individual entry tickets for archaeological ruins, camera permits, or local activities.", 10),
            _inc_excluded("Personal expenses such as laundry, intercom orders, extra snacks, and premium beverages.", 11),
            _inc_excluded("Insurance premiums or emergency medical support protocols.", 12),
            _inc_excluded("Optional extended site tours or extra driver night running.", 13)
        ],
    )
    return package, itinerary


GUJARAT_DOMESTIC_BUILDERS = [
    build_gj_001,
    build_gj_002,
    build_gj_003,
    build_gj_004,
    build_gj_005,
    build_gj_006,
    build_gj_007,
    build_gj_008,
    build_gj_009,
    build_gj_010,
    build_gj_011,
    build_gj_012,
    build_gj_013,
    build_gj_014,
    build_gj_015,
    build_gj_016,
    build_gj_017,
    build_gj_018,
    build_gj_019,
]
