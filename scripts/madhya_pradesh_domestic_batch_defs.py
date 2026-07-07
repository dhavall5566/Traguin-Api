"""Builder functions for MP-011 through MP-015 Madhya Pradesh domestic packages."""

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

MADHYA_PRADESH_SLUG = "madhya-pradesh"


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


def build_mp_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "MP-011"
    tour_code = "TRAGUIN-MP-011"
    title = "Chitrakoot Holy Lord Rama Trail"
    duration = "03 Nights / 04 Days"
    slug = "mp-011-chitrakoot-holy-lord-rama-trail"
    itin_slug = "mp-011-chitrakoot-holy-lord-rama-trail-itinerary"
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
            _ph("State / Country: Madhya Pradesh, India | Category: Premium Spiritual Pilgrimage", 2),
            _ph("Destinations: Chitrakoot (The Holy Lord Rama Trail) • Gupt Godavari • Ramghat", 3),
            _ph("Ideal for: Devotees, Families & Culture Seekers", 4),
            _ph("Best season: July to March (Auspicious Year-Round)", 5),
            _ph("Starting price: On Request (Premium Collection)", 6),
            _ph(
                "TRAGUIN Curated Experience Note: Chauffeured private luxury transportation, premium stays at selected hotels, customized daily vegetarian meal plans, fast-track VIP temple entry, and a private boat ride on the Mandakini River for the evening Deepdaan arti ceremony",
                7,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private, highly informative historical narrations and customized senior-citizen care parameters",
                8,
            ),
            _ph(
                "Shopping: Highly revered Ayurvedic herbs gathered from the Kamadgiri forests, premium wooden handicraft deities, aromatic incense sticks, and pure brass prayer items",
                9,
            ),
            _ph(
                'Local Gastronomic Recommendations: Indulge in the world-famous "Chitrakoot Peda"—a unique milk delicacy roasted to absolute golden perfection over open charcoal ovens',
                10,
            ),
            _ph(
                "Important: Dress code compliance—modest traditional attire highly recommended across all locations; best time October to March; advance booking advised for limited high-end hospitality blocks in Chitrakoot",
                11,
            ),
        ],
        moods=["Pilgrimage", "Spiritual", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Collection)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Chitrakoot Holy Lord Rama Trail • 03 Nights / 04 Days",
        overview=(
            "Welcome to a divine exploration into the heart of India's ancient spirituality. Chitrakoot, the deeply revered forest of legends where Lord Rama, Goddess Sita, and Lakshmana spent more than eleven years of their exile, is a land rich in scenic beauty and absolute cosmic tranquility. This meticulously planned Best Madhya Pradesh Tour Package is crafted exclusively for discerning travelers seeking a highly comfortable, emotionally resonant, and premium Madhya Pradesh Pilgrimage Tour.\n\n"
            "Every single detail of this sacred journey is backed by TRAGUIN personalized assistance. From your dedicated luxury transportation and handpicked hotels to VIP access for spiritual events, TRAGUIN guarantees an experience marked by peace, luxury, and unforgettable memories. This package serves as the perfect Madhya Pradesh Family Tour for multi-generational families who wish to share an exquisite spiritual connection with absolute comfort.\n\n"
            "Why embark on this Premium Madhya Pradesh Experience? Chitrakoot is globally celebrated for housing the most authentic Top Tourist Places in Madhya Pradesh associated with the Ramayana epic. Devotees and luxury travelers seek out these highly searched experiences to touch the sacred soil of Kamadgiri and view the subterranean wonders of Gupt Godavari. It is perfect as a deeply rewarding family retreat, a tranquil cultural getaway, and a prime photography point for capturing pristine natural elements. Discover the absolute Best Time to Visit Madhya Pradesh's holy sites while being pampered by TRAGUIN Madhya Pradesh Packages.\n\n"
            "TRAGUIN Curated Experience Note: Your pilgrimage features chauffeured private luxury transportation, premium stays at selected hotels, customized daily vegetarian meal plans, fast-track VIP temple entry, and a private boat ride on the Mandakini River for the evening Deepdaan arti ceremony."
        ),
        seo_title="MP-011 | Chitrakoot Holy Lord Rama Trail | TRAGUIN",
        seo_description="Premium 03 Nights / 04 Days Madhya Pradesh pilgrimage (MP-011 / TRAGUIN-MP-011): Chitrakoot, Ramghat, Kamadgiri, Gupt Godavari, Sphatik Shela, Sati Anasuya Ashram, Janaki Kund, and 4-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Ramghat, Tulsidas Statue & Mandakini River Cruise with private Deepdaan ritual & VIP seated arti view", 1),
            _ih("Kamadgiri Hill circumambulation, Bharat Milap Temple & Gupt Godavari Caves", 2),
            _ih("Sphatik Shela, Hanuman Dhara (viewpoint) & Sati Anasuya Ashram with heritage speaker narration", 3),
            _ih("Janaki Kund, Raghubir Mandir Darshan & smooth private transfer to Satna / Prayagraj / Khajuraho", 4),
            _ih("TRAGUIN Signature Experience: Private historical narrations and customized senior-citizen care parameters", 5),
        ],
        days=[
            _day(
                1,
                "Arrival & Sacred Mandakini Evening Gala Arti",
                (
                    "Your sacred trail commences upon your arrival at the designated transit point (Satna/Khajuraho or Prayagraj). A senior representative from TRAGUIN will accord you a traditional, elite welcome and escort you in an air-conditioned, private luxury vehicle to the holy township of Chitrakoot. Enjoy a seamless check-in at your premium resort. In the late afternoon, head to Ramghat on the serene banks of the Mandakini River—the very spot where Lord Rama famously met Sant Tulsidas. Relax on a private, cushioned wooden boat exclusively reserved by TRAGUIN to witness the spectacular multi-priest evening Maha Arti. Watch thousands of illuminated clay lamps drift across the river in a breathtaking display of pure faith."
                ),
                [
                    "Sightseeing Included: Ramghat, Tulsidas Statue, Mandakini River Cruise.",
                    "Meals Included: Traditional Vegetarian Dinner.",
                    "Evening Experience: Private Deepdaan ritual & VIP seated arti view.",
                    "Overnight Stay: Handpicked Luxury Resort in Chitrakoot.",
                ],
            ),
            _day(
                2,
                "The Core Divine Trail",
                (
                    "Begin your day with a peaceful early morning breakfast. We set out for Kamadgiri Hill, the primeval heart of Chitrakoot, believed to be the living manifestation of the lord himself. A comfortable, private e-cart ride is arranged to make the circumambulation completely effortless. Explore the moving site of Bharat Milap Temple, where Prince Bharat emotionally requested Lord Rama to return to Ayodhya. In the afternoon, explore the breathtaking subterranean cave structures of Gupt Godavari. Walk through natural stone galleries containing streams of hidden mountain water, where natural rocks form the legendary thrones of the divine triad."
                ),
                [
                    "Sightseeing Included: Kamadgiri Hill, Bharat Milap Temple, Gupt Godavari Caves.",
                    "Meals Included: Gourmet Breakfast & Satvik Dinner.",
                    "Photography Points: The lush foliage of Kamadgiri & unique cave stream reflections.",
                    "Overnight Stay: Handpicked Luxury Resort in Chitrakoot.",
                ],
            ),
            _day(
                3,
                "Sita Kund & Anasuya Ashram Trail",
                (
                    "Savor a premium breakfast before visiting Sphatik Shela, a massive boulder on the riverbank bearing the clear, sacred footprints of Lord Rama and Goddess Sita, set amidst an incredibly peaceful clearing. Next, venture deep into the scenic woods to Sati Anasuya Ashram, a powerful spiritual sanctuary located near the birthplace of the Mandakini River. Listen to timeless, captivating ancient stories told by a local heritage speaker arranged by TRAGUIN. Spend your evening completely at leisure, walking along the beautiful resort lawns or indulging in a personalized holistic wellness consultation."
                ),
                [
                    "Sightseeing Included: Sphatik Shela, Hanuman Dhara (viewpoint), Sati Anasuya Ashram.",
                    "Meals Included: Gourmet Breakfast & Satvik Dinner.",
                    "Optional Activities: Relaxing Vedic chanting session at the ashram quarters.",
                    "Overnight Stay: Handpicked Luxury Resort in Chitrakoot.",
                ],
            ),
            _day(
                4,
                "Departure via Janaki Kund",
                (
                    "On your final morning, enjoy a relaxed breakfast and visit Janaki Kund, a pristine, quiet stretch of water where Goddess Sita is said to have bathed regularly during her stay in the forest. Take a moment to soak in the incredible peace before packing your bags. Your dedicated luxury private transport will arrive seamlessly at the lobby to provide an executive transfer back to your preferred departure airport or railway station. Return home with a deeply renewed spirit and unforgettable memories of a premium travel experience seamlessly orchestrated by TRAGUIN."
                ),
                [
                    "Sightseeing Included: Janaki Kund, Raghubir Mandir Darshan.",
                    "Meals Included: Gourmet Breakfast Only.",
                    "Transfers: Smooth private transfer to Satna / Prayagraj / Khajuraho.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Hotel River Front Chitrakoot / Equivalent",
                "Chitrakoot",
                "03 Nights",
                "Deluxe",
                "Executive Deluxe Room",
                "MAP Plan (Breakfast & Dinner)",
                4,
                1,
            ),
            _hotel(
                "The Ram Kripa Inn / Boutique Heritage Stay",
                "Chitrakoot",
                "03 Nights",
                "Premium",
                "Premium Club Room",
                "MAP Plan (Breakfast & Dinner)",
                4,
                2,
            ),
            _hotel(
                "Aurobindo Heritage Resort / Luxury Retreat",
                "Chitrakoot",
                "03 Nights",
                "Luxury",
                "Luxury Heritage Suite",
                "MAP Plan (Pure Vegetarian Luxury)",
                5,
                3,
            ),
            _hotel(
                "Elite Handpicked Private Spiritual Villas",
                "Chitrakoot",
                "03 Nights",
                "Ultra Luxury",
                "Presidential Wellness Suite",
                "Bespoke Customized Curated Meals",
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included("03 Nights premium accommodation in top-rated handpicked hotels.", 1),
            _inc_included("Daily gourmet breakfasts and specialized multi-cuisine vegetarian dinners.", 2),
            _inc_included("Chauffeured private luxury transportation for all transfers & sightseeing.", 3),
            _inc_included("Round-the-clock personalized TRAGUIN support and guest care.", 4),
            _inc_included("Private chartered boat cruise on Mandakini River for Ramghat Aarti.", 5),
            _inc_included("VIP fast-track temple entries and eco-friendly e-cart bookings.", 6),
            _inc_included("All toll fees, driver allowances, state fuel surcharges, and resort taxes.", 7),
            _inc_excluded("Inbound/Outbound flights or long-distance railway tickets.", 8),
            _inc_excluded("Personal expenses such as laundry, telephone calls, and spa fees.", 9),
            _inc_excluded("Monument entry tickets or camera pass charges where applicable.", 10),
            _inc_excluded("Optional customized excursions or personal offering rituals (Pooja).", 11),
            _inc_excluded("Comprehensive travel and medical insurance coverage.", 12),
        ],
    )
    return package, itinerary


def build_mp_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "MP-012"
    tour_code = "TRAGUIN-MP-012"
    title = "Gwalior Orchha Khajuraho Royal Extravaganza"
    duration = "05 Nights / 06 Days"
    slug = "mp-012-gwalior-orchha-khajuraho-royal-extravaganza"
    itin_slug = "mp-012-gwalior-orchha-khajuraho-royal-extravaganza-itinerary"
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
            _ph("State / Country: Madhya Pradesh, India | Category: Royal Family Getaway", 2),
            _ph("Destinations: Gwalior • Orchha • Khajuraho (The Royal Maratha & Chandel Trail)", 3),
            _ph("Ideal for: Families, History Enthusiasts & Luxury Seekers", 4),
            _ph("Best season: October to April", 5),
            _ph("Starting price: On Request (Royal Signature)", 6),
            _ph(
                "TRAGUIN Curated Experience Note: Chauffeured private luxury vehicle transfers, handpicked hotels & palace properties, guided heritage walking tours, private light & sound show access, and an unforgettable evening high-tea overlooking the Betwa River",
                7,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private historian guides and specialized family itineraries designed to keep all generations engaged",
                8,
            ),
            _ph(
                "Shopping: Exquisite Chanderi and Maheshwari silk sarees from local weaving cooperatives, traditional metal-cast bell figurines, and handcrafted sandstone carvings",
                9,
            ),
            _ph(
                "Local Cuisine Try-outs: Gwalior's famous crispy Bedai Sabzi breakfasts and sweet, saffron-infused Gajak desserts",
                10,
            ),
            _ph(
                "Important: Heritage properties maintain classic layouts—notify TRAGUIN for ground-floor or accessibility needs; best time October to April; early reservations recommended for converted palace suites",
                11,
            ),
        ],
        moods=["Family", "Heritage", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Royal Signature)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Gwalior Orchha Khajuraho Royal Extravaganza • 05 Nights / 06 Days",
        overview=(
            "Step back in time to an era of valiant dynasties, grand royal architecture, and poetic landscapes. This elite Best Madhya Pradesh Tour Package is intentionally designed for families who want to discover the true heart of Central India's heritage without compromising on high-end luxury. Meticulously structured by TRAGUIN, this legendary trail combines premium stays in converted heritage palaces, private luxury transportation, and highly curated experiences for unforgettable memories across generations.\n\n"
            "From the impenetrable hilltop fort of Gwalior to the romantic chhatris of Orchha and the intricate UNESCO stone carvings of Khajuraho, every segment is managed with dedicated 24/7 TRAGUIN personalized assistance. Let us turn an ordinary vacation into a majestic Madhya Pradesh Family Tour filled with immersive experiences.\n\n"
            "Why pick this Luxury Madhya Pradesh Holiday? This region boasts the most iconic Top Tourist Places in Madhya Pradesh, offering a perfect mix of educational context for children and absolute relaxation for adults. It stands as a highly searched option for premium travel, romantic getaways, and luxury holidays. Explore iconic Instagram locations like the blue-tiled Man Singh Palace, or dive into culture with dynamic musical light displays. Discover the Best Time to Visit Madhya Pradesh's golden triangle with TRAGUIN Madhya Pradesh Packages.\n\n"
            "TRAGUIN Curated Experience Note: Your royal holiday includes chauffeured private luxury vehicle transfers, handpicked hotels & palace properties, guided heritage walking tours, private light & sound show access, and an unforgettable evening high-tea overlooking the Betwa River."
        ),
        seo_title="MP-012 | Gwalior Orchha Khajuraho Royal Extravaganza | TRAGUIN",
        seo_description="Premium 05 Nights / 06 Days Madhya Pradesh royal tour (MP-012 / TRAGUIN-MP-012): Gwalior Fort, Jai Vilas Palace, Orchha, Betwa River high-tea, Khajuraho UNESCO temples, and 4-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Gwalior Fort, Man Mandir Palace, Teli Ka Mandir & VIP Gwalior Fort Light and Sound Show", 1),
            _ih("Jai Vilas Palace Museum, Scindia Durbar Hall & scenic drive to Orchha", 2),
            _ih("Jehangir Mahal, Raja Mahal, Ram Raja Temple, Royal Chhatris & private riverside sunset high-tea", 3),
            _ih("Khajuraho Western & Eastern Group UNESCO temples with expert historian & Kandariya Art & Culture show", 4),
            _ih("TRAGUIN Signature Experience: Private historian guides and specialized family itineraries", 5),
        ],
        days=[
            _day(
                1,
                "Gwalior Arrival",
                (
                    "Your premium family getaway begins upon arriving in Gwalior. A TRAGUIN corporate host will welcome your family and drive you in a private luxury vehicle to your handpicked premium hotel. After a seamless check-in, head out to the majestic Gwalior Fort, towering over the city skyline. Walk through the stunning Man Mandir Palace, renowned for its turquoise tile mosaics. As darkness falls, enjoy VIP seats reserved by TRAGUIN for the iconic Light and Sound Show, where the rich history of Tomar and Scindia rulers comes alive through captivating narrations."
                ),
                [
                    "Sightseeing Included: Gwalior Fort, Man Mandir Palace, Teli Ka Mandir.",
                    "Meals Included: Welcome Buffet Dinner.",
                    "Evening Experience: VIP seating at the Gwalior Fort historical sound show.",
                    "Overnight Stay: Converted Heritage Palace Hotel in Gwalior.",
                ],
            ),
            _day(
                2,
                "Gwalior to Orchha",
                (
                    "After a leisurely morning breakfast, explore the magnificent Jai Vilas Palace, the current seat of the Scindia dynasty. Marvel at the Durbar Hall, which houses the world's heaviest pair of crystal chandeliers and the famous silver model train that served fine digestifs to royal guests. In the afternoon, enjoy a scenic drive in your luxury private transport to Orchha, a medieval town beautifully frozen in time. Check into a luxury riverside resort and spend a relaxed evening taking in the serene, unhurried local atmosphere."
                ),
                [
                    "Sightseeing Included: Jai Vilas Palace Museum, Scindia Durbar Hall.",
                    "Meals Included: Gourmet Breakfast & Palace Dinner.",
                    "Photography Points: Golden ceilings of Jai Vilas & pastoral landscapes en route.",
                    "Overnight Stay: Premium Riverside Resort in Orchha.",
                ],
            ),
            _day(
                3,
                "Orchha Exploration",
                (
                    "Savor a premium breakfast before heading out to the historic Orchha Fort complex. Tour the towering Jehangir Mahal, built as a grand gesture of royal welcome for the Mughal Emperor, and the beautiful multi-layered Raja Mahal. Next, visit the Ram Raja Temple, the only shrine in India where Lord Rama is legally revered and honored as a ruling king with regular police guards of honor. In the late afternoon, TRAGUIN has curated an exclusive experience: a private luxury high-tea set up on the banks of the pristine Betwa River, directly facing the majestic royal cenotaphs (Chhatris) as the sun sets over the water."
                ),
                [
                    "Sightseeing Included: Jehangir Mahal, Raja Mahal, Ram Raja Temple, Royal Chhatris.",
                    "Meals Included: Gourmet Breakfast & Regional Bundelkhandi Dinner.",
                    "Exclusive Highlight: Private riverside sunset catering by the Betwa riverbank.",
                    "Overnight Stay: Premium Riverside Resort in Orchha.",
                ],
            ),
            _day(
                4,
                "Orchha to Khajuraho",
                (
                    "Enjoy a relaxed morning breakfast overlooking the river before departing in your private luxury vehicle for Khajuraho, a world-famous UNESCO World Heritage site. Upon arrival, check into your ultra-luxury resort and unwind. In the evening, attend the vibrant Kandariya Art & Culture show, which showcases traditional Indian classical dances. This performance brings to life the stone expressions and legendary architectural history of the monuments you will explore the following day."
                ),
                [
                    "Sightseeing Included: Rural landscapes drive, Evening Cultural Show entry.",
                    "Meals Included: Gourmet Breakfast & Grand Buffet Dinner.",
                    "Optional Activities: Therapeutic Ayurvedic spa therapy session at the resort.",
                    "Overnight Stay: Ultra-Luxury Resort in Khajuraho.",
                ],
            ),
            _day(
                5,
                "Khajuraho Temples Tour",
                (
                    "Today is dedicated to exploring the incredible craftsmanship of the Khajuraho temples, carved from sandstone by Chandel architects over a thousand years ago. Accompanied by an expert historian approved by TRAGUIN, visit the majestic Kandariya Mahadeva Temple, the Lakshmana Temple, and the beautifully preserved Vishvanatha Temple. Admire the stunning geometric precision and expressive stone carvings depicting daily life, celestial alignments, and ancient mythologies. In the afternoon, tour the quiet Eastern Group of temples, which feature beautiful Jain monuments."
                ),
                [
                    "Sightseeing Included: Western Group & Eastern Group of UNESCO Temples.",
                    "Meals Included: Gourmet Breakfast & Farewell Gala Dinner.",
                    "Instagram Spots: The towering spires (Shikhara) of Kandariya Mahadeva.",
                    "Overnight Stay: Ultra-Luxury Resort in Khajuraho.",
                ],
            ),
            _day(
                6,
                "Khajuraho Departure",
                (
                    "Savor a final morning breakfast at your resort at your own leisure. Take a quiet stroll through the beautifully landscaped resort grounds or select some final local souvenirs. Your dedicated luxury vehicle will arrive on schedule to provide a comfortable transfer to Khajuraho Airport or the railway terminal for your onward journey. Return home with closer family bonds, an inspired appreciation for ancient architecture, and unforgettable memories from this Premium Madhya Pradesh Experience brought to life by TRAGUIN."
                ),
                [
                    "Transfers Included: Premium airport/railway station drop-off.",
                    "Meals Included: Gourmet Breakfast Only.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Hotel Radisson Gwalior / Orchha Resort (Riverside)",
                "Gwalior / Orchha / Khajuraho",
                "05 Nights",
                "Deluxe",
                "Standard Room",
                "Breakfast & Dinner",
                4,
                1,
                description="Khajuraho: Ramada by Wyndham.",
            ),
            _hotel(
                "Taj Usha Kiran Palace (Deluxe) / Amar Mahal Orchha",
                "Gwalior / Orchha / Khajuraho",
                "05 Nights",
                "Premium",
                "Premium Room",
                "Breakfast & Dinner",
                5,
                2,
                description="Khajuraho: Radisson Jass Khajuraho.",
            ),
            _hotel(
                "Taj Usha Kiran Palace (Luxury) / Bundelkhand Riverside Palace",
                "Gwalior / Orchha / Khajuraho",
                "05 Nights",
                "Luxury",
                "Luxury Room",
                "Breakfast & Dinner",
                5,
                3,
                description="Khajuraho: The Lalit Temple View.",
            ),
            _hotel(
                "Taj Royal Palace (Royal Suite) / Vilas Palace Private Wing",
                "Gwalior / Orchha / Khajuraho",
                "05 Nights",
                "Ultra Luxury",
                "Royal Suite",
                "Breakfast & Dinner",
                5,
                4,
                description="Khajuraho: The Lalit Temple View (Luxury Suite).",
            ),
        ],
        inclusions=[
            _inc_included("05 Nights royal accommodation in handpicked heritage hotels and top resorts.", 1),
            _inc_included("Daily gourmet breakfasts and specialized multi-cuisine dinners included.", 2),
            _inc_included("Chauffeured, private luxury AC vehicle for all transfers and sightseeing tours.", 3),
            _inc_included("24/7 dedicated TRAGUIN personalized assistance and on-ground support.", 4),
            _inc_included("Private riverside sunset high-tea experience overlooking the Betwa River.", 5),
            _inc_included("VIP fast-track entries, light & sound show tickets, and cultural event passes.", 6),
            _inc_included("All applicable fuel surcharges, driver allowances, toll fees, and resort taxes.", 7),
            _inc_excluded("Inbound or outbound flight tickets or long-distance railway bookings.", 8),
            _inc_excluded("Personal hotel charges such as mini-bar consumption, laundry, and spa therapies.", 9),
            _inc_excluded("Camera tickets, professional videography passes, or monument entry charges.", 10),
            _inc_excluded("Optional customized excursions or personal shopping costs.", 11),
            _inc_excluded("Comprehensive individual travel or medical insurance policies.", 12),
        ],
    )
    return package, itinerary


def build_mp_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "MP-013"
    tour_code = "TRAGUIN-MP-013"
    title = "Pench National Park Mowgli Land"
    duration = "03 Nights / 04 Days"
    slug = "mp-013-pench-national-park-mowgli-land"
    itin_slug = "mp-013-pench-national-park-mowgli-land-itinerary"
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
            _ph("State / Country: Madhya Pradesh, India | Category: Luxury Family Wilderness Tour", 2),
            _ph("Destinations: Pench National Park (Mowgli Land Wilderness Reserve)", 3),
            _ph("Ideal for: Families, Nature Enthusiasts & Kids", 4),
            _ph("Best season: October to May", 5),
            _ph("Starting price: On Request (Premium Collection)", 6),
            _ph(
                "TRAGUIN Curated Experience Note: Round-trip luxury private transfers, handpicked ultra-comfort jungle eco-lodges, all premium daily meals, fully pre-booked private open-top jeep safaris with certified local trackers, a family jungle survival workshop, and surprise welcome gifts for kids",
                7,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private bonfire storyteller encounters and curated children's educational kits tailored for an unforgettable holiday",
                8,
            ),
            _ph(
                "Shopping: Beautiful handmade clay pottery from Pachdhar village, pure organic forest honey, beautifully carved wooden animals, and authentic Gond tribal paintings",
                9,
            ),
            _ph(
                'Local Culinary Try-outs: Traditional roasted "Saoji" preparations, fresh local millet bread, and refreshing coolers made from wild Mahua flowers',
                10,
            ),
            _ph(
                "Important: Core zone permits strictly regulated—early booking essential; park closed Wednesday afternoons; earthy-toned clothing recommended for safaris",
                11,
            ),
        ],
        moods=["Wildlife", "Family", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Collection)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Pench National Park Mowgli Land • 03 Nights / 04 Days",
        overview=(
            "Welcome to the mythical woods of Pench National Park, the genuine geographic muse behind Rudyard Kipling's legendary creation, 'The Jungle Book'. This meticulously designed Best Madhya Pradesh Tour Package is curated specifically to bring families closer together in a world of raw breathtaking landscapes, towering teak woods, and exquisite biodiversity. Handcrafted as a high-end Madhya Pradesh Family Tour, this journey offers the perfect balance of heart-racing wilderness exploration, interactive learning for children, and premium stays where your complete relaxation is guaranteed.\n\n"
            "Every element of this wilderness vacation is backed by flawless TRAGUIN personalized assistance. From your private luxury transportation arriving directly at Nagpur airport to premium open-top 4x4 safari vehicles and handpicked jungle resorts, TRAGUIN delivers an unbeatable luxury experience. This custom-tailored Luxury Madhya Pradesh Holiday promises deep bonding moments and unforgettable memories for every member of your family.\n\n"
            "Why pick this Premium Madhya Pradesh Experience? Pench National Park holds a unique place among the Top Tourist Places in Madhya Pradesh due to its incredible tiger sightings, leopards, dholes (wild dogs), and beautiful birds. It is widely recognized as one of the best family points for a thrilling multi-day escape, serving as a popular Instagram location for wildlife enthusiasts and a rich hub for indigenous tribal culture. Let us guide you during the absolute Best Time to Visit Madhya Pradesh's pristine wilderness regions while enjoying the professional care of our specialized TRAGUIN Madhya Pradesh Packages.\n\n"
            "TRAGUIN Curated Experience Note: Your vacation package covers round-trip luxury private transfers, handpicked ultra-comfort jungle eco-lodges, all premium daily meals, fully pre-booked private open-top jeep safaris with certified local trackers, a family jungle survival workshop, and surprise welcome gifts for kids."
        ),
        seo_title="MP-013 | Pench National Park Mowgli Land | TRAGUIN",
        seo_description="Premium 03 Nights / 04 Days Pench wildlife package (MP-013 / TRAGUIN-MP-013): Mowgli Land safaris, Pachdhar pottery village, bonfire naturalist stories, night safari option, and 4-tier jungle lodge accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Forest property nature trails, bird watching deck & interactive bonfire naturalist stories", 1),
            _ih("Core Jungle Safaris (Turia/Karmajhiri Zones) with morning & afternoon Shere Khan tracking", 2),
            _ih("Pachdhar Pottery Village, Buffer Zone Trail Walk & optional night safari in Wolf Sanctuary zone", 3),
            _ih("In-resort photography session & private luxury transfer to Nagpur Airport/Railway Station", 4),
            _ih("TRAGUIN Signature Experience: Private bonfire storyteller encounters and curated children's educational kits", 5),
        ],
        days=[
            _day(
                1,
                "Arrival & Welcome to Mowgli's Domain",
                (
                    "Your family's wilderness escape begins upon your arrival at Nagpur Airport or Railway Station. A designated professional chauffeur from TRAGUIN will greet you at the arrival terminal and transfer your family in an air-conditioned, private luxury vehicle through smooth highways and local rural lanes directly to your premium safari lodge in Pench. Check into your beautifully appointed forest cottage and unwind amidst the ambient sounds of nature. In the evening, the family is invited to an exclusive open-air bonfire area. Savor fine refreshments while an experienced resident naturalist shares fascinating local stories about the real-life historical animals that inspired the world-famous characters of Shere Khan and Baloo."
                ),
                [
                    "Sightseeing Included: Forest property nature trails & bird watching deck.",
                    "Meals Included: Luxury Welcome High-Tea & Elaborate Buffet Dinner.",
                    "Evening Experience: Interactive stargazing session for the kids.",
                    "Overnight Stay: Handpicked Premium Jungle Resort in Pench.",
                ],
            ),
            _day(
                2,
                "Deep Wilderness Jungle Book Safaris",
                (
                    "An early morning wake-up call accompanied by fresh hot cocoa and coffee sets the stage for adventure. Board your private, open-top 4x4 safari jeep, completely pre-arranged by TRAGUIN with premium seating configurations. Enter the forest gates as dawn breaks to witness golden beams of light piercing through ghost trees and dry teak forests. Track warning calls of langurs and spotted deer to locate majestic Royal Bengal Tigers. Enjoy a curated gourmet picnic breakfast inside the park's designated core zone. Return to the resort to escape the midday heat by the infinity pool. In the afternoon, head back out for another thrilling safari track to witness spectacular wildlife activity near pristine local water holes."
                ),
                [
                    "Sightseeing Included: Core Jungle Safaris (Turia/Karmajhiri Zones).",
                    "Meals Included: Bush Picnic Breakfast, Buffet Lunch, and Dinner.",
                    "Photography Points: Spectacular tiger tracks, scenic rocky hills, and majestic owls.",
                    "Overnight Stay: Handpicked Premium Jungle Resort in Pench.",
                ],
            ),
            _day(
                3,
                "Pottery Village Tour & Cooney Jungle Walk",
                (
                    "After a late, relaxed breakfast, take an easy, premium drive to the charming local artisan village of Pachdhar. This specialized cultural excursion introduces your family to generations of traditional potters. Children can try out ancient throwing wheels to craft their own clay souvenirs. Return to your resort for a delicious lunch featuring organic ingredients grown in the resort's private kitchen garden. In the late afternoon, enjoy an easy nature walk along the park's buffer perimeter. As night falls, embark on an optional thrilling night safari inside the Wolf Sanctuary zone to witness secretive nocturnal animals like civets, porcupines, and leopards under the stars."
                ),
                [
                    "Sightseeing Included: Pachdhar Pottery Village, Buffer Zone Trail Walk.",
                    "Meals Included: Gourmet Breakfast, Organic Lunch, and Themed Barbecue Dinner.",
                    "Optional Activities: High-thrill night safari booking option.",
                    "Overnight Stay: Handpicked Premium Jungle Resort in Pench.",
                ],
            ),
            _day(
                4,
                "Farewell to Mowgli Land",
                (
                    "Wake up to a relaxed morning and enjoy a final lavish breakfast overlooking the peaceful forest canopies. Take a walk along the resort grounds to capture beautiful family photos at dedicated photography points. Your private luxury vehicle, arranged by TRAGUIN, will be waiting at the reception area to take your family on a smooth, comfortable transfer back to Nagpur Airport or Railway Station for your onward journey home. Return with an enriched understanding of India's wild ecosystems, a strong sense of revitalized energy, and unforgettable memories of a perfect family vacation."
                ),
                [
                    "Sightseeing Included: In-resort photography session.",
                    "Meals Included: Full Breakfast Buffet.",
                    "Transfers: Private luxury drop off to Nagpur Airport.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Tuli Tiger Corridor / Pench Jungle Camp",
                "Pench",
                "03 Nights",
                "Deluxe",
                "Luxury Safari Tent / Cottage",
                "Jungle Full Board (All Meals)",
                4,
                1,
            ),
            _hotel(
                "Pench Tree House Hideaway / Equivalent",
                "Pench",
                "03 Nights",
                "Premium",
                "Premium Elevated Tree House",
                "Jungle Full Board (All Meals)",
                4,
                2,
            ),
            _hotel(
                "Kipling Camp / Taj Baghvan Wildlife Lodge",
                "Pench",
                "03 Nights",
                "Luxury",
                "Luxury Wilderness Suite",
                "Elite Gourmet Board (All Meals)",
                5,
                3,
            ),
            _hotel(
                "The Jamtara Wilderness Camp (Elite Private Reserve)",
                "Pench",
                "03 Nights",
                "Ultra Luxury",
                "Luxury Machinery Star-Bed Suite",
                "Bespoke Customized Curated Dining",
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included("03 Nights premium accommodation in top-rated jungle lodges.", 1),
            _inc_included("All daily breakfast, lunch, high-tea, and dinners included.", 2),
            _inc_included("Private luxury AC transportation dedicated for all highway transfers.", 3),
            _inc_included("Pre-arranged open-top 4x4 private jeep safaris with expert trackers.", 4),
            _inc_included("Exclusive pottery interaction and artisan village access fees.", 5),
            _inc_included("Dedicated 24/7 TRAGUIN personalized assistance and safari gate coordination.", 6),
            _inc_included("All park permits, forest entrance fees, tolls, and hospitality taxes.", 7),
            _inc_excluded("Inbound or outbound flight tickets or train tickets to Nagpur.", 8),
            _inc_excluded("Personal expenses such as laundry, phone calls, spa treatments, and bar tabs.", 9),
            _inc_excluded("Camera fees for high-end professional telephoto lenses inside the park.", 10),
            _inc_excluded("Tips for forest drivers, safari guides, and lodge staff.", 11),
            _inc_excluded("Optional evening/night safari booking charges.", 12),
        ],
    )
    return package, itinerary


def build_mp_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "MP-014"
    tour_code = "TRAGUIN-MP-014"
    title = "Panna Diamond Mines & Safari Splendors"
    duration = "03 Nights / 04 Days"
    slug = "mp-014-panna-diamond-mines-safari-splendors"
    itin_slug = "mp-014-panna-diamond-mines-safari-splendors-itinerary"
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
            _ph("State / Country: Madhya Pradesh, India | Category: Premium Family Wilderness", 2),
            _ph("Destinations: Panna National Park • Diamond Mines District • Ken River Reserve • Khajuraho Temples", 3),
            _ph("Ideal for: Families, Nature Enthusiasts & Adventure Seekers", 4),
            _ph("Best season: October to May", 5),
            _ph("Starting price: On Request (Elite Family Tier)", 6),
            _ph(
                "TRAGUIN Curated Family Highlight: Private chauffeured luxury AC SUV throughout the trip, pre-booked exclusive open-top core zone safaris, specialized mineralogical guide for diamond tours, and fully curated kids-friendly menu modifications at all boutique forest lodges",
                7,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private, expertly guided geology and wildlife tracking sessions perfect for family bonding",
                8,
            ),
            _ph(
                "Shopping: Beautiful hand-carved stone replicas from Khajuraho, organic forest honey, authentic tribal paintings, and glittering mineral souvenirs",
                9,
            ),
            _ph(
                "Local Cuisine Experience: Fresh, locally caught river fish preparations, regional Bundelkhandi stews, and traditional hot malpuas at the local village markets",
                10,
            ),
            _ph(
                "Important: Original passport or government ID required for core zone entries; earthy muted tones recommended for safaris; early reservations essential for jeep permits",
                11,
            ),
        ],
        moods=["Wildlife", "Family", "Adventure"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Elite Family Tier)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Panna Diamond Mines & Safari Splendors • 03 Nights / 04 Days",
        overview=(
            "Welcome to an unforgettable venture designed to capture the imaginations of both parents and children alike. Panna is a fascinating land where the natural gleam of raw volcanic diamond deposits effortlessly meets the raw, deep roars of royal Bengal tigers. This meticulously managed Best Madhya Pradesh Tour Package is curated specifically as a premium Madhya Pradesh Family Tour and comprehensive wildlife retreat.\n\n"
            "Handcrafted by travel experts at TRAGUIN, this private itinerary strikes a perfect harmony between high-octane open-jeep jungle safaris, unique mineral discovery tours, and ultra-comfortable premium stays. Travel effortlessly with your loved ones while enjoying dedicated TRAGUIN personalized assistance every step of the way, ensuring completely stress-free logistics, unforgettable memories, and top-tier luxury transportation.\n\n"
            "Panna ranks at the absolute top of highly searched destinations for a true Luxury Madhya Pradesh Holiday. It blends world-class conservation successes with ancient geology. Families get the rare chance to witness wild tigers, leopards, and crocodiles in their native habitats alongside the unique, highly searched diamond mining tours. It offers pristine, scenic beauty across the Ken River and is filled with incredible popular Instagram locations like Raneh Canyons. Discover the absolute Best Time to Visit Madhya Pradesh's emerald forests with our premium, handpicked TRAGUIN Madhya Pradesh Packages.\n\n"
            "TRAGUIN Curated Family Highlight: Private chauffeured luxury AC SUV throughout the trip, pre-booked exclusive open-top core zone safaris, specialized mineralogical guide for diamond tours, and fully curated kids-friendly menu modifications at all boutique forest lodges."
        ),
        seo_title="MP-014 | Panna Diamond Mines & Safari Splendors | TRAGUIN",
        seo_description="Premium 03 Nights / 04 Days Panna wildlife package (MP-014 / TRAGUIN-MP-014): Ken River crocodile cruise, core zone safari, Pandav Falls, diamond mines, Raneh Canyon, Khajuraho temples, and 4-tier jungle lodge accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Ken River Sanctuary, Boat Cruise & Wilderness Trails with stargazing campfire orientation", 1),
            _ih("Core Jungle Zone Safari, Pandav Falls & Eco-Museum with expert naturalist", 2),
            _ih("Panna Diamond Mining District tour with mineralogical guide & Raneh Falls and Canyons", 3),
            _ih("UNESCO Western Group of Khajuraho Temples & Local Art Market before departure", 4),
            _ih("TRAGUIN Signature Experience: Private geology and wildlife tracking sessions for family bonding", 5),
        ],
        days=[
            _day(
                1,
                "Arrival & Enchanting Ken River Cruise",
                (
                    "Your family's thrilling wilderness getaway begins upon your arrival at Khajuraho Airport or Satna Station. A dedicated TRAGUIN corporate host will receive you warmly and escort your family in a spacious, private luxury SUV to your premium jungle lodge nestled right on the fringes of Panna National Park. After a smooth priority check-in and an exquisite lunch, embark on a relaxed afternoon drive to the pristine Ken Crocodile Sanctuary. Board a private wooden boat cruise to witness spectacular mugger crocodiles basking along the scenic beauty of the riverbanks as the sun sets over the dense forest canopy."
                ),
                [
                    "Sightseeing Included: Ken River Sanctuary, Boat Cruise, Wilderness Trails.",
                    "Meals Included: Welcome High-Tea & Multi-Cuisine Dinner.",
                    "Evening Experience: Stargazing and brief wildlife orientation over a campfire.",
                    "Overnight Stay: Handpicked Premium Jungle Lodge at Panna.",
                ],
            ),
            _day(
                2,
                "Exclusive Panna Jungle Safari",
                (
                    "Wake up to a crisp forest morning with fresh coffee for a thrilling dawn safari. Board your pre-booked, private 4x4 open-top jeep with an expert local naturalist assigned by TRAGUIN. Drive deep into the core zones of Panna National Park to spot the Royal Bengal Tiger, leopards, sloth bears, and herds of spotted deer grazing in the mist. Return to the resort for a hearty lunch. In the afternoon, take a smooth drive to Pandav Falls—a breathtaking natural waterfall cascading into a clear, emerald pool where the Pandavas are legendary to have sought shelter, making for magnificent family photography points."
                ),
                [
                    "Sightseeing Included: Core Jungle Zone Safari, Pandav Falls, Eco-Museum.",
                    "Meals Included: Jungle Breakfast & Estate Dinner.",
                    "Photography Points: Tiger tracks, Pandav caves, sweeping canyon vistas.",
                    "Overnight Stay: Handpicked Premium Jungle Lodge at Panna.",
                ],
            ),
            _day(
                3,
                "Panna Diamond Mines & Raneh Canyon",
                (
                    "Today brings a truly unique geological adventure. After breakfast, head out for a specialized tour of the famous Panna Diamond Mining District. Accompanied by a specialized mineral guide, your family will explore the history of diamond excavation and learn how precious gems are searched and sorted from volcanic soils. In the afternoon, drive to the spectacular Raneh Falls and Canyons. This natural masterpiece features a deep, stunning gorge carved out of pure crystalline granite in multi-hued shades of pink, green, and grey, earning it the title of India's mini-Grand Canyon."
                ),
                [
                    "Sightseeing Included: Diamond Mining Information Area, Raneh Canyon Gorge.",
                    "Meals Included: Buffet Breakfast & Special Themes Farewell Dinner.",
                    "Optional Activities: Interactive pottery or tribal painting workshop at the lodge.",
                    "Overnight Stay: Handpicked Premium Jungle Lodge at Panna.",
                ],
            ),
            _day(
                4,
                "Khajuraho Heritage & Departure",
                (
                    "Savor a lazy morning breakfast overlooking the forest. Pack your bags for a short, smooth drive to the UNESCO World Heritage Site of Khajuraho. Tour the stunning Western Group of Temples, widely celebrated for their architectural brilliance and intricate stone carvings that bring ancient Indian art vividly to life. Following a fine lunch at a luxury boutique hotel, your private vehicle will drop your family at Khajuraho Airport or the station for your return journey. Head home carrying sparkling diamond stories and thrilling tiger memories from your premium family getaway managed perfectly by TRAGUIN."
                ),
                [
                    "Sightseeing Included: UNESCO Western Group of Temples, Local Art Market.",
                    "Meals Included: Gourmet Breakfast Only.",
                    "Transfers: Final drop at Khajuraho Airport/Station via private luxury SUV.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Ken River Lodge / Tendu Leaf Jungle Resort",
                "Panna",
                "03 Nights",
                "Deluxe",
                "Luxury Forest Cottage",
                "All Meals Plan (Jungle Full Board)",
                4,
                1,
            ),
            _hotel(
                "Panna Tiger Resort / The Sarai at Toria",
                "Panna",
                "03 Nights",
                "Premium",
                "Premium River-View Villa",
                "All Meals Plan (Jungle Full Board)",
                4,
                2,
            ),
            _hotel(
                "Taj Pashan Garh / Symphony Forest Resort",
                "Panna",
                "03 Nights",
                "Luxury",
                "Elite Stone Cottage",
                "Gourmet Curated Dining Tier",
                5,
                3,
            ),
            _hotel(
                "The Oberoi Forest Villas / Private Jungle Reserve",
                "Panna",
                "03 Nights",
                "Ultra Luxury",
                "Presidential Pool Suite / Ultra Villa",
                "Bespoke Personal Chef Services",
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included("03 Nights premium accommodation in top-rated handpicked safari lodges.", 1),
            _inc_included("All meals included across stays (Breakfast, Lunch, High-Tea, and Dinner).", 2),
            _inc_included("Private luxury AC SUV dedicated throughout the trip for all transfers.", 3),
            _inc_included("Pre-booked private 4x4 open-jeep safari with certified naturalists.", 4),
            _inc_included("Specialized mineralogical guide fee for the Panna Diamond Mine tour.", 5),
            _inc_included("Round-the-clock personalized TRAGUIN support and family coordination.", 6),
            _inc_included("All park entry fees, vehicle toll cards, and state wilderness surcharges.", 7),
            _inc_excluded("Airfare tickets or train bookings to and from Khajuraho/Satna.", 8),
            _inc_excluded("Personal lodge expenses (mini-bar, specialized spa, or laundry fees).", 9),
            _inc_excluded("Camera tickets or video camera surcharges inside core park gates.", 10),
            _inc_excluded("Optional activities or extra safaris not specifically itemized.", 11),
            _inc_excluded("Travel and medical insurance premiums.", 12),
        ],
    )
    return package, itinerary


def build_mp_015(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "MP-015"
    tour_code = "TRAGUIN-MP-015"
    title = "Heart of Incredible India Mega Vacation"
    duration = "09 Nights / 10 Days"
    slug = "mp-015-heart-of-incredible-india-mega-vacation"
    itin_slug = "mp-015-heart-of-incredible-india-mega-vacation-itinerary"
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
            _ph("State / Country: Madhya Pradesh, India | Category: Heart of Incredible India Mega", 2),
            _ph("Destinations: Gwalior • Orchha • Khajuraho • Bandhavgarh National Park • Jabalpur • Bhopal", 3),
            _ph("Ideal for: Families, Luxury Vacationers & Connoisseurs", 4),
            _ph("Best season: October to April", 5),
            _ph("Starting price: On Request (Premium Scale)", 6),
            _ph(
                "TRAGUIN Curated Family Note: Premium chauffeured luxury group transportation, fully handpicked 5-star & heritage hotels, inclusive multi-cuisine breakfasts and dinners, private expert city-guides, fast-track monument permits, and reserved open-top 4x4 jungle jeeps",
                7,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private history lecturers and customized storytelling sessions at key heritage monuments",
                8,
            ),
            _ph(
                "Shopping: Exquisite hand-woven Chanderi and Maheshwari sarees, beautiful Bell Metal handicrafts from Datia, organic tribal paintings, and local marble sculptures from Bhedaghat",
                9,
            ),
            _ph(
                "Local Cuisine Try-outs: Traditional Indori Poha Jalebi for breakfast, rich Bhopali Mughlai stews, and sweet, creamy Shrikhand",
                10,
            ),
            _ph(
                "Important: Bandhavgarh tiger safari permits open 120 days in advance; best time October to April; inform TRAGUIN of dietary or room preferences before arrival",
                11,
            ),
        ],
        moods=["Family", "Heritage", "Wildlife"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Scale)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Heart of Incredible India Mega Vacation • 09 Nights / 10 Days",
        overview=(
            "Welcome to the grandest exploration of Central India. Unfolding across sprawling historical landscapes, legendary wildlife sanctuaries, and royal architectural relics, this comprehensive Best Madhya Pradesh Tour Package is thoughtfully orchestrated to be the ultimate premium Madhya Pradesh Family Tour. Every step of this timeless route has been selectively refined by TRAGUIN to guarantee seamless long-distance connectivity, absolute premium stays, and deeply engaging cultural sub-narratives suited perfectly for family groups.\n\n"
            "Traverse majestic hill-fortresses, ancient world-heritage sanctuaries, pristine jungle reserves home to the royal Bengal tiger, and grand crystalline water-canyons. Backed by round-the-clock TRAGUIN personalized assistance, this private holiday guarantees that you and your loved ones build unforgettable memories in absolute luxury, traveling in elite private transportation with curated high-end hospitality at every stop.\n\n"
            "Why visit Central India with your family? This Premium Madhya Pradesh Experience unlocks the absolute finest selection of Top Tourist Places in Madhya Pradesh. It bridges the dramatic battlements of Gwalior, the riverside royal cenotaphs of Orchha, and the UNESCO world-heritage temple carvings of Khajuraho. Families looking for high-end wilderness thrills can view pristine jungle domains at Bandhavgarh, capture stunning photography points at Jabalpur's Marble Rocks, and view ancient history at Bhopal. Discover the absolute Best Time to Visit Madhya Pradesh while being pampered by specialized TRAGUIN Madhya Pradesh Packages tailored for multi-generational families.\n\n"
            "TRAGUIN Curated Family Note: This elite package features premium chauffeured luxury group transportation, fully handpicked 5-star & heritage hotels, inclusive multi-cuisine breakfasts and dinners, private expert city-guides, fast-track monument permits, and reserved open-top 4x4 jungle jeeps."
        ),
        seo_title="MP-015 | Heart of Incredible India Mega Vacation | TRAGUIN",
        seo_description="Premium 09 Nights / 10 Days Madhya Pradesh mega tour (MP-015 / TRAGUIN-MP-015): Gwalior, Orchha, Khajuraho, Bandhavgarh safaris, Jabalpur Marble Rocks, Sanchi Stupa, Bhimbetka, Bhopal, and 4-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Jai Vilas Palace Museum, Gwalior Fort, Man Mandir Palace & Orchha riverside resort", 1),
            _ih("Jehangir Mahal, Betwa Cenotaphs, Khajuraho Western & Eastern temples & Sound & Light Show", 2),
            _ih("Bandhavgarh core zone morning & afternoon jeep safaris with resident naturalist presentation", 3),
            _ih("Dhuandhar Falls, Marble Rocks Gorge private cruise, Sanchi Stupa & Bhimbetka Rock Shelters", 4),
            _ih("Taj-ul-Masajid, MP Tribal Museum, Bhopal lakeside farewell & TRAGUIN history lecturers", 5),
        ],
        days=[
            _day(
                1,
                "Gwalior Arrival",
                (
                    "Your epic family expedition begins as you arrive in the historic city of Gwalior. A dedicated TRAGUIN corporate host will welcome your family warmly at the transit terminal and escort you in a private, air-conditioned luxury vehicle to your iconic heritage hotel. After a priority check-in and short rest, explore the opulent Jai Vilas Palace. Marvel at its spectacular European architecture, the world-famous golden chandeliers, and the legendary silver model train that glides across the royal dining table."
                ),
                [
                    "Sightseeing Included: Jai Vilas Palace Museum, Scindia Dynasty Grounds.",
                    "Meals Included: Luxury Buffet Dinner.",
                    "Evening Experience: Leisure stroll around royal manicured palace gardens.",
                    "Overnight Stay: Gwalior Premium Heritage Property.",
                ],
            ),
            _day(
                2,
                "Gwalior Fort to Orchha",
                (
                    "Savor an early morning breakfast before driving up the imposing stone ramparts of Gwalior Fort, described by Emperor Babur as the pearl among Indian fortresses. Tour the stunning turquoise-tiled Man Mandir Palace and the historic Saas-Bahu temples. Following an early lunch, take a beautiful drive to the hidden riverside kingdom of Orchha. Check-in at your premium resort overlooking the Betwa River and relax as the evening breeze filters through nearby royal spires."
                ),
                [
                    "Sightseeing Included: Gwalior Fort, Teli Ka Mandir, Transit to Orchha.",
                    "Meals Included: Breakfast & Gourmet Dinner.",
                    "Photography Point: Panoramic views of Gwalior city from the fortress walls.",
                    "Overnight Stay: Orchha Premium Riverside Resort.",
                ],
            ),
            _day(
                3,
                "Orchha Splendors to Khajuraho",
                (
                    "Discover the medieval magic of Orchha today. Visit the grand Orchha Palace complex, including the spectacular multi-tiered Jehangir Mahal and Raja Mahal, showcasing beautiful Bundela murals. Stand beside the iconic Chhatris (royal cenotaphs) aligned along the river bank. In the afternoon, take a smooth private drive to the UNESCO World Heritage site of Khajuraho. Check-in at your luxury 5-star hotel and enjoy a completely relaxed evening at the spa."
                ),
                [
                    "Sightseeing Included: Jehangir Mahal, Betwa Cenotaphs, Transit to Khajuraho.",
                    "Meals Included: Breakfast & Grand Buffet Dinner.",
                    "Evening Experience: Attending the iconic Khajuraho Sound & Light Show.",
                    "Overnight Stay: Khajuraho Luxury 5-Star Hotel.",
                ],
            ),
            _day(
                4,
                "Khajuraho Architectural Wonders",
                (
                    "Immerse your family in world-class art and heritage. Accompanied by a handpicked expert historian, spend your day touring the world-famous Western Group of Temples, highlighting the grand Kandariya Mahadeva Temple and Lakshmana Temple. Marvel at the intricate thousand-year-old sandstone carvings that celebrate human life, beauty, and spirituality. In the afternoon, explore the peaceful Eastern Group of Jain shrines before enjoying a relaxed dinner."
                ),
                [
                    "Sightseeing Included: Kandariya Mahadeva, Lakshmana, Parsvanatha Temples.",
                    "Meals Included: Breakfast & Premium Dinner.",
                    "Local Interaction: Curated artisan workshop viewing ancient carving replication.",
                    "Overnight Stay: Khajuraho Luxury 5-Star Hotel.",
                ],
            ),
            _day(
                5,
                "Khajuraho to Bandhavgarh",
                (
                    "Following a leisurely breakfast, leave the temple valley behind and take a scenic countryside drive toward the dense forests of Bandhavgarh National Park—boasting one of the highest densities of Royal Bengal Tigers in the world. Arrive at your luxury wilderness lodge, where your family will check into private, air-conditioned cottages. Enjoy a presentation on the local wildlife by a resident naturalist before dinner under the stars."
                ),
                [
                    "Sightseeing Included: Countryside Scenic Drive, Jungle Lodge Orientation.",
                    "Meals Included: Full Board (Breakfast, Lunch & Dinner).",
                    "Wild Highlight: Evening stargazing & wildlife documentary viewing.",
                    "Overnight Stay: Bandhavgarh Premium Wilderness Lodge.",
                ],
            ),
            _day(
                6,
                "Bandhavgarh Wilderness Safaris",
                (
                    "An exhilarating day of wildlife safaris. Head out at dawn in an open-top 4x4 jeep into the core zones of Bandhavgarh National Park. Listen to the morning calls of langurs and deer warning of a predator nearby. Look for leopards, sloth bears, and the magnificent Royal Bengal Tiger roaming past ancient fort ruins. Return to the lodge for a hearty lunch and a swim, then head out for an afternoon safari to view different eco-zones before sunset."
                ),
                [
                    "Sightseeing Included: Morning & Afternoon Core Zone Jeep Safaris.",
                    "Meals Included: Full Board (Breakfast, Lunch & Dinner).",
                    "Exclusive Feature: Private open-top gypsy vehicle with expert local track guides.",
                    "Overnight Stay: Bandhavgarh Premium Wilderness Lodge.",
                ],
            ),
            _day(
                7,
                "Bandhavgarh to Jabalpur",
                (
                    "Say goodbye to the jungle and drive south to Jabalpur, located on the banks of the Narmada River. Head straight to Bhedaghat to witness Dhuandhar Falls, where the river plunges dramatically, creating a mist that resembles smoke. Next, take a private family boat ride through the narrow Marble Rocks gorge, where towering white marble cliffs reflect beautifully on the deep river water."
                ),
                [
                    "Sightseeing Included: Dhuandhar Falls, Marble Rocks Gorge Private Cruise.",
                    "Meals Included: Breakfast & Multi-Cuisine Dinner.",
                    "Photography Point: Shimmering marble walls under the soft afternoon sun.",
                    "Overnight Stay: Jabalpur Premium Luxury Hotel.",
                ],
            ),
            _day(
                8,
                "Jabalpur to Bhopal via Sanchi",
                (
                    "Embark on a fascinating road trip toward Bhopal, the capital city. En route, explore the legendary Sanchi Stupa, a world-renowned UNESCO World Heritage site commissioned by Emperor Ashoka in the 3rd century BCE. Admire the beautifully preserved stone toranas (gateways) depicting stories from the Jataka tales. Continue your drive to Bhopal and check into your luxury resort overlooking the serene Upper Lake."
                ),
                [
                    "Sightseeing Included: Great Stupa of Sanchi, Ashoka Pillars, Bhopal Arrival.",
                    "Meals Included: Breakfast & Premium Dinner.",
                    "Evening Experience: Peaceful lakeside twilight walk at your luxury resort.",
                    "Overnight Stay: Bhopal Luxury Lakefront Property.",
                ],
            ),
            _day(
                9,
                "Bhopal & Bhimbetka Excursion",
                (
                    "Today features a short drive to the extraordinary Bhimbetka Rock Shelters, a UNESCO World Heritage site containing prehistoric rock paintings dating back over 30,000 years. Return to Bhopal to tour the impressive Taj-ul-Masajid—one of Asia's largest mosques—and visit the beautifully curated Tribal Museum, showcasing the vibrant art and lifestyle of Central India's indigenous communities."
                ),
                [
                    "Sightseeing Included: Bhimbetka Caves, Taj-ul-Masajid, MP Tribal Museum.",
                    "Meals Included: Breakfast & Elegant Farewell Dinner.",
                    "Family Highlight: Special farewell dinner featuring traditional local signature dishes.",
                    "Overnight Stay: Bhopal Luxury Lakefront Property.",
                ],
            ),
            _day(
                10,
                "Bhopal Departure",
                (
                    "Savor a final morning breakfast together at the resort. Enjoy a peaceful view of the lake as you pack your bags. Your dedicated TRAGUIN luxury private coach will arrive at the hotel lobby to provide a smooth, comfortable transfer to Bhopal Airport or Railway Station for your journey home. Return home with revitalized spirits, closer family bonds, and unforgettable memories of this incredible vacation."
                ),
                [
                    "Transfers Included: Hotel lobby to Bhopal airport/station drop-off.",
                    "Meals Included: Premium Breakfast Only.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Tansen Residency / Amar Mahal | Hotel Radisson / Tiger Trails | Grand Heritage / Hotel Palash",
                "Gwalior / Orchha | Khajuraho / Bandhavgarh | Jabalpur / Bhopal",
                "09 Nights",
                "Deluxe",
                "Standard Room",
                "Breakfast & Dinner",
                4,
                1,
            ),
            _hotel(
                "Usha Kiran Palace / Orchha Resort | Ramada Grand / Kings Lodge | Vilas Jabalpur / Noor-Us-Sabah",
                "Gwalior / Orchha | Khajuraho / Bandhavgarh | Jabalpur / Bhopal",
                "09 Nights",
                "Premium",
                "Premium Room",
                "Breakfast & Dinner",
                4,
                2,
            ),
            _hotel(
                "Taj Usha Kiran Palace (Club) | The Lalit Temple View / Samode | The Kalchuri / Jehan Numa Palace",
                "Gwalior / Orchha | Khajuraho / Bandhavgarh | Jabalpur / Bhopal",
                "09 Nights",
                "Luxury",
                "Luxury Room",
                "Breakfast & Dinner",
                5,
                3,
            ),
            _hotel(
                "Taj Royal Presidential Suite | The Lalit Luxury Suite / Tree House | Vilas Executive / Jehan Numa Retreat",
                "Gwalior / Orchha | Khajuraho / Bandhavgarh | Jabalpur / Bhopal",
                "09 Nights",
                "Ultra Luxury",
                "Royal Suite",
                "Breakfast & Dinner",
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included("09 Nights premium accommodation in handpicked top-rated hotels.", 1),
            _inc_included("Daily buffet breakfasts and multi-cuisine dinners across all locations.", 2),
            _inc_included("Private luxury AC vehicle dedicated for all long-distance transfers.", 3),
            _inc_included("Exclusive TRAGUIN VIP assistance at airports and hotels.", 4),
            _inc_included("Two core-zone open 4x4 jungle jeep safaris in Bandhavgarh.", 5),
            _inc_included("Private family boat cruise at Bhedaghat Marble Rocks gorge.", 6),
            _inc_included("All applicable state taxes, fuel charges, driver allowances, and tolls.", 7),
            _inc_excluded("Inbound or outbound flights and railway tickets to Madhya Pradesh.", 8),
            _inc_excluded("Monument entry fees, camera passes, and personal porterage fees.", 9),
            _inc_excluded("Personal expenses like laundry, phone calls, drinks, and spa treatments.", 10),
            _inc_excluded("Optional customized extensions or activities outside the itinerary.", 11),
            _inc_excluded("Comprehensive individual medical and travel insurance premiums.", 12),
        ],
    )
    return package, itinerary


MADHYA_PRADESH_DOMESTIC_BUILDERS = [
    build_mp_011,
    build_mp_012,
    build_mp_013,
    build_mp_014,
    build_mp_015,
]
