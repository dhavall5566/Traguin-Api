"""Builder functions for MH-006 through MH-014 Maharashtra domestic packages."""

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


def build_mh_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MH-006'
    tour_code = 'TRAGUIN-MH-006'
    title = 'Maha Jyotirlinga Sacred Circuit'
    duration = '05 Nights / 06 Days'
    slug = 'mh-006-maha-jyotirlinga-sacred-circuit'
    itin_slug = 'mh-006-maha-jyotirlinga-sacred-circuit-itinerary'
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
            _ph('State / Country: Maharashtra, India | Category: Pilgrimage / Luxury', 2),
            _ph('Destinations: Bhimashankar • Trimbakeshwar • Grishneshwar • Aundha Nagnath • Parli Vaijnath', 3),
            _ph('Ideal for: Families & Devotees', 4),
            _ph('Best season: July to March', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Luxury Pilgrimage Circuit (FIT)', 7),
            _ph('Vehicle: Private AC Luxury Innova Crysta / Premium SUV', 8),
            _ph('Meal Plan: Continental Breakfast & Specialized Satvik Dinners Included', 9),
            _ph('Route Map: Pune Arrival → Bhimashankar → Shirdi → Trimbakeshwar → Grishneshwar (Ellora) → Aundha Nagnath → Parli Vaijnath → Pune Departure', 10),
            _ph('TRAGUIN Signature Experience: Handcrafted meticulously by TRAGUIN Experts, this pilgrimage ensures premium luxury vehicle provisions, avoiding crowded transits, and including customized Satvik dining options to preserve your ritual vows seamlessly', 11),
            _ph('Shopping: Nasik Vineyards & Markets — premium raisins, fresh grapes, authentic local copper items; Aurangabad Bazaars — hand-woven Paithani sarees and intricate Himroo stoles', 12),
            _ph('Important: Temple dress codes mandatory (sarees/salwars for women, dhotis/kurtas for men); best time post-monsoon when Western Ghats erupt into vibrant green; book specialized abhishek rituals well in advance through TRAGUIN travel advisor', 13),
        ],
        moods=['Pilgrimage', 'Spiritual', 'Luxury'],
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
        tagline='Maha Jyotirlinga Sacred Circuit • 5 Nights / 6 Days',
        overview=(
            "Embark on a soul-stirring spiritual odyssey across the sacred land of Maharashtra. Custom-tailored to perfection by TRAGUIN, this exclusive 5 Nights / 6 Days pilgrimage circuit seamlessly blends deep spiritual devotion with the luxury of premium stays and chauffeured convenience. Experience the divine aura of all 5 sacred Jyotirlingas of the state, amidst breathtaking landscapes, making for an absolute journey of unforgettable memories.\n\n"
            "Maharashtra holds a uniquely exalted space in spiritual geography, hosting five of the twelve sacred Jyotirlingas. Our premier Maharashtra Family Tour takes you deep into these high-ranking energy centers while ensuring a thoroughly refreshing and elite holiday structure. From the cloud-kissed heights of Bhimashankar nestled in the Western Ghats to the ancient stone architectural marvel of Trimbakeshwar near Nasik, this circuit promises unmatched scenic beauty combined with deep religious history.\n\n"
            "Whether you choose this as a meaningful Maharashtra Honeymoon Package seeking divine blessings for a new beginning, or a comfortable family tour for your parents, the detailed Maharashtra Sightseeing takes you past famous attractions like Ellora Caves, Shirdi Sai Baba Temple, and local artisan markets. Our TRAGUIN Maharashtra Packages ensure that premium stays, immersive experiences, and smooth check-ins keep you comfortable at every step.\n\n"
            "TRAGUIN Curated Experience Note: This Luxury Maharashtra Holiday features VIP Darshan passes (where available), handpicked hotels with top-notch amenities, professional spiritual guides, and private luxury transportation specifically scheduled to eliminate any trace of travel fatigue."
        ),
        seo_title='MH-006 | Maha Jyotirlinga Sacred Circuit | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Maharashtra Jyotirlinga pilgrimage (MH-006 / TRAGUIN-MH-006): Bhimashankar, Shirdi, Trimbakeshwar, Grishneshwar, Ellora Caves, Aundha Nagnath, Parli Vaijnath, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Bhimashankar Jyotirlinga Temple & Gupt Bhimashankar (optional trail)', 1),
            _ih('Shirdi Sai Baba Shrine, Trimbakeshwar Temple & Kushavarta Kund', 2),
            _ih('Grishneshwar Temple, Ellora Caves (Cave 16 - Kailash Temple) & Aundha Nagnath Temple Complex', 3),
            _ih('Parli Vaijnath Mountain Shrine & concluding celebratory high-tea hosted by TRAGUIN manager', 4),
            _ih('TRAGUIN Signature Experience: Handcrafted meticulously by TRAGUIN Experts with premium luxury vehicle provisions and customized Satvik dining options', 5),
        ],
        days=[
            _day(
                1,
                'Pune to Bhimashankar to Shirdi',
                (
                    'Arrive at Pune Airport where your professional TRAGUIN chauffeur welcomes you. Board your private luxury vehicle and proceed directly towards Bhimashankar, the first sacred pillar of light on this circuit. Wind through spectacular ghat routes to reach the shrine located in a dense forest reserve. Experience a tranquil VIP darshan of the swayambhu lingam. After soaking in the pristine spiritual vibrations and scenic beauty, embark on a smooth luxury drive to the holy town of Shirdi. Check in to your premium handpicked hotel for an overnight stay.'
                ),
                [
                    'Sightseeing Included: Bhimashankar Jyotirlinga Temple, Gupt Bhimashankar (optional trail).',
                    'Evening Experience: Relaxing evening check-in followed by a refreshing Satvik dinner.',
                    'Overnight Stay: Premium Luxury Stay, Shirdi.',
                    'Meals Included: Welcome Drink & Dinner.',
                ],
            ),
            _day(
                2,
                'Shirdi to Trimbakeshwar to Nasik',
                (
                    'Wake up early to experience the divine morning Kakad Aarti at the world-renowned Shirdi Sai Baba Temple. After an elegant buffet breakfast, drive through the vineyards toward Nasik to reach Trimbakeshwar Jyotirlinga Temple. Situated at the source of the holy Godavari River, this iconic attraction features a unique three-faced lingam representing Brahma, Vishnu, and Mahesh. Engage in an exclusive curated prayer arranged by TRAGUIN local experts before retiring to your premium stay in Nasik.'
                ),
                [
                    'Sightseeing Included: Shirdi Sai Baba Shrine, Trimbakeshwar Temple, Kushavarta Kund.',
                    'Photography Points: The breathtaking landscapes of Brahmagiri hills framing the temple spires.',
                    'Overnight Stay: Luxury Vineyard Resort / Premium Stay, Nasik.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                3,
                'Nasik to Grishneshwar to Aurangabad',
                (
                    'Following a leisurely morning breakfast, proceed down comfortable highways towards Aurangabad. Your destination is the ancient Grishneshwar Jyotirlinga Temple, built entirely of red basalt rock and renowned as the final or 12th Jyotirlinga of Lord Shiva. After an immersive darshan experience, enjoy an afternoon exploring the nearby UNESCO World Heritage-listed Ellora Caves, a monumental showcase of rock-cut monolithic temple craft.'
                ),
                [
                    'Sightseeing Included: Grishneshwar Temple, Ellora Caves (Cave 16 - Kailash Temple).',
                    'Optional Activities: Shopping for authentic local Himroo silk sarees and traditional weaves.',
                    'Overnight Stay: Ultra-Luxury Heritage Partner Hotel, Aurangabad.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                4,
                'Aurangabad to Aundha Nagnath',
                (
                    'Today, your premium pilgrimage holiday routes towards Marathwada. Travel comfortably in your luxury vehicle to Aundha Nagnath Jyotirlinga Temple, heavily linked to the times of the Mahabharata. Marvel at the intricate Hemadpanti style stone carvings depicting ancient scriptural stories. Witness the subterranean garbha-griha where devotees experience deeply private, immersive spiritual moments.'
                ),
                [
                    'Sightseeing Included: Aundha Nagnath Temple Complex, local heritage stepwells.',
                    'Evening Experience: A slow-paced evening stroll around the temple lake.',
                    'Overnight Stay: Premium Handpicked Stay, Nanded / Hingoli Region.',
                    'Meals Included: Breakfast & Local Cuisine Dinner.',
                ],
            ),
            _day(
                5,
                'Aundha Nagnath to Parli Vaijnath to Pune',
                (
                    'On this final day of temple darshans, drive toward the sacred hillock of Parli Vaijnath Jyotirlinga Temple. Perched elegantly on an elevated stone platform, this sanctuary is revered both as a Jyotirlinga and a house of celestial healing. Ascend the wide, comfortable stone steps to perform your final circuit prayers. After your spiritual fulfillment, commence a smooth highway drive back towards Pune, enjoying the scenic beauty of rural Maharashtra along the way.'
                ),
                [
                    'Sightseeing Included: Parli Vaijnath Mountain Shrine.',
                    'Immersive Experiences: Concluding celebratory high-tea hosted by your TRAGUIN manager.',
                    'Overnight Stay: Premium Luxury Business Hotel, Pune.',
                    'Meals Included: Breakfast & Farewell Festive Dinner.',
                ],
            ),
            _day(
                6,
                'Pune Departure',
                (
                    'Indulge in a late luxurious breakfast at your hotel. Take time to arrange your holy souvenirs and prasadam. Your dedicated premium chauffeur will arrive to transfer you safely to Pune International Airport / Railway Station for your journey home, concluding your premium TRAGUIN Maharashtra Package with unforgettable memories.'
                ),
                [
                    'Transfers Included: Private Airport Drop-off.',
                    'Meals Included: Full Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('Stardust Resort (Shirdi) / Express Inn (Nasik)', 'Shirdi / Nasik', '05 Nights', 'Deluxe', 'Deluxe AC Room', 'CP (Breakfast Only)', 4, 1),
            _hotel('Sun N Sand (Shirdi) / Radisson Blu (Nasik)', 'Shirdi / Nasik', '05 Nights', 'Premium', 'Superior Premium Room', 'MAPAI (Breakfast + Dinner)', 5, 2),
            _hotel('Vivanta (Aurangabad) / Radisson Blu (Pune)', 'Aurangabad / Pune', '05 Nights', 'Luxury', 'Executive Club Room', 'MAPAI (Gourmet Satvik Plan)', 5, 3),
            _hotel('Welcomhotel by ITC Hotels (Ahmednagar) / JW Marriott (Pune)', 'Ahmednagar / Pune', '05 Nights', 'Ultra Luxury', 'Luxury Suite Collection', 'Ultra All-Inclusive Meal Plan', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: 05 Nights luxury stay at our premium handpicked hotels across the circuit.', 1),
            _inc_included('Meals: Curated daily buffet breakfasts and dinners, featuring pure vegetarian culinary themes.', 2),
            _inc_included('Transfers & Sightseeing: Dedicated private AC Innova Crysta throughout the complete loop from Pune.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated remote guest relationship support and local driver-cum-guide assistance.', 4),
            _inc_included('Welcome Amenities: Customized spiritual kit containing traditional premium stoles, copper water tumblers, and sanitizer packs.', 5),
            _inc_excluded('Airfare or main rail tickets to Pune station.', 6),
            _inc_excluded('Special personal pooja arrangement fees and direct dakshina to temple priests.', 7),
            _inc_excluded('Any entry tickets for Ellora Caves or camera permissions.', 8),
            _inc_excluded('Personal items such as laundry, tips, and room-service demands.', 9),
        ],
    )
    return package, itinerary


def build_mh_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MH-007'
    tour_code = 'TRAGUIN-MH-007'
    title = 'Premium Alibaug Offbeat Getaway'
    duration = '02 Nights / 03 Days'
    slug = 'mh-007-premium-alibaug-offbeat-getaway'
    itin_slug = 'mh-007-premium-alibaug-offbeat-getaway-itinerary'
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
            _ph('State / Country: Maharashtra / India | Category: Offbeat / Luxury Coastal Stay', 2),
            _ph('Destinations: Alibaug Luxury Beach Villa Stay', 3),
            _ph('Ideal for: Families, Couples & Corporate Elite', 4),
            _ph('Best season: October to May', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Elite Coastal FIT Getaway', 7),
            _ph('Vehicle: Dedicated Luxury Chauffeur-Driven SUV (Innova Crysta / Premium Sedan) for absolute privacy', 8),
            _ph('Meal Plan: Fully Loaded Modified American Plan (Gourmet Breakfasts & Curated Farm-to-Table Dinners)', 9),
            _ph('Route Map: Mumbai/Pune Arrival → Private Luxury Speedboat to Mandwa Jet / Road Journey → Alibaug Luxury Villa Stay → Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated carefully by TRAGUIN Experts to offer a seamless, worry-free coastal stay with fast-tracked speedboat transfers and exclusive chef-curated dining charts', 11),
            _ph('Shopping: Alibaug Local Markets — authentic white onions, organic cold-pressed coconut oil, traditional homemade spices; Coastal Sweets — authentic local Chikki and fresh coastal Aamras or fruit pulps', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; speedboat schedules dependent on weather and tidal trends; early reservation recommended for limited luxury beach villa inventory', 13),
        ],
        moods=['Beach', 'Leisure', 'Luxury'],
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
        tagline='Premium Alibaug Offbeat Getaway • 02 Nights / 03 Days',
        overview=(
            "Escape the mundane city rush and melt into the serene coastal vibes of Maharashtra's finest beach haven. Carefully curated by TRAGUIN, this private elite getaway delivers a premium Alibaug experience wrapped in premium stays, pristine shores, and tailored luxury hospitality. Step straight into an exclusive beach villa curated thoughtfully for travelers who demand the absolute highest parameters of peace and timeless sophistication.\n\n"
            "Alibaug, renowned for its golden beaches, historic sea forts, and lush coconut plantations, is celebrated as the top luxury holiday destination close to Mumbai. For those actively searching for a high-end Alibaug Family Tour or a romantic Alibaug Honeymoon Package, this premium sanctuary is the ultimate answer.\n\n"
            "From exploring iconic attractions like the ancient Kolaba Fort situated right in the ocean to witnessing the scenic beauty of Kihim Beach and Versoli Beach, your journey is filled with immersive experiences. Unwind at popular Instagram locations inside your private sanctuary or indulge in local culinary arts. Our handpicked hotels and exclusive beach villa collections promise unforgettable memories. Discover the best time to visit Alibaug with TRAGUIN Alibaug Packages, designed entirely to pamper you.\n\n"
            "TRAGUIN Curated Experience Note: This offbeat Alibaug Honeymoon Package & Family Tour focuses on slow-paced premium rejuvenation. Featuring handcrafted meals prepared by a private villa chef, sunset photography points, private beach access, and personalized assistance from booking to return."
        ),
        seo_title='MH-007 | Premium Alibaug Offbeat Getaway | TRAGUIN',
        seo_description='Premium 02 Nights / 03 Days Alibaug beach villa package (MH-007 / TRAGUIN-MH-007): Mandwa speedboat transfer, Kolaba Fort, Kihim Beach, private beach villa stay, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Mandwa Coastal Drive, Exclusive Beach Access & Private Villa Rejuvenation', 1),
            _ih('Kolaba Sea Fort, Kihim Beach / Awas Beach & local organic spice farms', 2),
            _ih('Private speed-boat coordination layout and curated evening beach side setup', 3),
            _ih('TRAGUIN Signature Experience: Curated carefully by TRAGUIN Experts for seamless worry-free coastal stay', 4),
            _ih('Premium Handpicked Stays: 4-tier beach villa and resort options from Radisson Blu to TRAGUIN Private Elite Beach Villa', 5),
        ],
        days=[
            _day(
                1,
                'Mumbai / Pune to Alibaug',
                (
                    'Your premium escape begins with an elite transfer experience. If traveling from Mumbai, board a private luxury speedboat from the Gateway of India to Mandwa Jetty, offering a breathtaking panoramic view of the Arabian Sea. Upon arrival at Mandwa, your private chauffeur-driven luxury vehicle will transfer you directly to your handpicked ultra-luxury beach villa in Alibaug. Enjoy a flawless check-in followed by a refreshing welcome cocktail. Spend your afternoon soaking in the private pool or relaxing amidst pristine coastal layouts. In the evening, walk along the sands of an exclusive beach zone as the sun sets over the ocean horizon.'
                ),
                [
                    'Sightseeing Included: Mandwa Coastal Drive, Exclusive Beach Access, Private Villa Rejuvenation.',
                    'Evening Experience: A private, chef-curated sundowner high-tea served poolside inside your villa premises.',
                    'Overnight Stay: Handpicked Ultra-Luxury Beach Villa, Alibaug.',
                    'Meals Included: Welcome Drink, High-Tea & Curated Seafood/Local Gourmet Dinner.',
                ],
            ),
            _day(
                2,
                'Optional Offbeat Exploration',
                (
                    'Wake up to the relaxing sound of the ocean waves and indulge in a lavish farm-to-table breakfast prepared fresh by your private chef. Today, choose to venture out or remain immersed in your premium stays. If exploring, visit the famous Kolaba Fort, an iconic attraction accessible via a unique low-tide horse carriage ride or a shallow water walk. Later, explore the calm, scenic beauty of Kihim or Awas Beach, highly rated as peaceful tourist spots. Return to your luxury retreat for an evening of luxury, peace, and ultimate personalization.'
                ),
                [
                    'Sightseeing Included: Kolaba Sea Fort, Kihim Beach / Awas Beach, local organic spice farms.',
                    'Photography Points: The ancient stone walls of Kolaba Fort against ocean waves and the serene, line-up of coconut trees at Awas.',
                    'Overnight Stay: Ultra-Luxury Private Beach Villa, Alibaug.',
                    'Meals Included: Multi-Cuisine Gourmet Breakfast & Private Coastal BBQ Dinner Experience.',
                ],
            ),
            _day(
                3,
                'Alibaug to Departure',
                (
                    'Relish a slow, luxurious morning breakfast on your private sit-out deck, taking in the refreshing ocean breeze. Spend your remaining hours indulging in a final swim or picking up high-quality local souvenirs. Your dedicated luxury chauffeur will arrive at your villa door to ensure a smooth and seamless check-out, transferring you safely back to Mandwa Jetty for your private speedboat or back via your customized overland route. Your elite TRAGUIN Alibaug Package concludes, leaving you with unforgettable memories of a blissful premium coastal retreat.'
                ),
                [
                    'Transfers Included: Private Chauffeur Drop-off to Mandwa Jetty / Road Transfer Route.',
                    'Meals Included: Full Artisanal Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('Radisson Blu Resort & Spa, Alibaug', 'Alibaug', '02 Nights', 'Deluxe', 'Executive Spa Suite', 'Breakfast & Dinner (MAP)', 4, 1),
            _hotel('Tropica Beach Resort By The Sea', 'Alibaug', '02 Nights', 'Premium', 'Premium Sea-View Cottage', 'Breakfast & Dinner (MAP)', 5, 2),
            _hotel('The Mansion House, Alibaug', 'Alibaug', '02 Nights', 'Luxury', 'Sky Roof Luxury Suite', 'All Meals Curated', 5, 3),
            _hotel('TRAGUIN Private Elite Beach Villa', 'Alibaug', '02 Nights', 'Ultra Luxury', 'Exclusive Private Pool Ocean Villa', 'Private Chef Dining Plan', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: 02 Nights stay at an ultra-luxury handpicked beach villa or premium resort.', 1),
            _inc_included('Meals: Daily multi-cuisine breakfasts and customized gourmet dinners prepared fresh.', 2),
            _inc_included('Transfers & Sightseeing: Dedicated Chauffeur-driven air-conditioned private luxury vehicle for entire trip itinerary.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated concierge assistance and localized on-ground operational back-up.', 4),
            _inc_included('Welcome Amenities: Cold towels, fresh coconut water refreshers, and premium customized villa welcome basket.', 5),
            _inc_included('Complimentary Experiences: Private speed-boat coordination layout and curated evening beach side setup.', 6),
            _inc_excluded('Flights, train fares, or external connectivity modes outside the itinerary guidelines.', 7),
            _inc_excluded('Any historical site camera fees or monument tickets not specifically mentioned.', 8),
            _inc_excluded('Personal expenses such as premium alcoholic beverages, internal spa therapy sessions, or laundry.', 9),
            _inc_excluded('Extreme water sport activities or additional vehicle usage outside defined operational routing.', 10),
            _inc_excluded('Medical or personal travel insurance.', 11),
        ],
    )
    return package, itinerary

def build_mh_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MH-008'
    tour_code = 'TRAGUIN-MH-008'
    title = 'Sacred Ashtavinayak Darshan Circuit'
    duration = '03 Nights / 04 Days'
    slug = 'mh-008-sacred-ashtavinayak-darshan-circuit'
    itin_slug = 'mh-008-sacred-ashtavinayak-darshan-circuit-itinerary'
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
            _ph('State / Country: Maharashtra, India | Category: Pilgrimage / Spiritual Luxury', 2),
            _ph('Destinations: Morgaon • Siddhatetek • Pali • Mahad • Theur • Lenyadri • Ozar • Ranjangaon', 3),
            _ph('Ideal for: Families, Devotees & Senior Citizens', 4),
            _ph('Best season: July to March', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Luxury Spiritual Pilgrimage Circuit (FIT)', 7),
            _ph('Vehicle: Dedicated Luxury Air-Conditioned Toyota Innova Crysta / Premium Chauffeur Driven Coach', 8),
            _ph('Meal Plan: Modified American Plan (Gourmet Pure Vegetarian Breakfasts & Dinners Included)', 9),
            _ph('Route Circuit: Pune → Morgaon → Siddhatek → Theur → Ranjangaon → Ozar → Lenyadri → Pali → Mahad → Pune', 10),
            _ph('TRAGUIN Signature Experience: Curated carefully by regional travel experts to ensure minimal stress, zero-hurry temple darshans, and premium route mappings that cut down on driving strain', 11),
            _ph('Shopping: Miniature brass idols of Ashtavinayak Ganesha, traditional copper pooja plates, authentic religious literature; Food — Puran Poli, Modak, fresh Bhakarwadi in Pune', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; traditional modest attire mandatory inside all Ashtavinayak temples; advance booking of 30-45 days recommended', 13),
        ],
        moods=['Pilgrimage', 'Spiritual', 'Luxury'],
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
        tagline='Sacred Ganesh Darshan Circuit • 03 Nights / 04 Days',
        overview=(
            "Embark on a divine soulful odyssey spanning the eight self-manifested (Swayambhu) temples of Lord Ganesha in Maharashtra. Thoughtfully designed and seamlessly curated by TRAGUIN, this signature sacred journey balances deep spiritual fulfillment with elite luxury comfort. Let us handle every intricate detail of your pilgrimage, ensuring premium accommodations, top-tier private transit, and exclusive experiences that translate into unforgettable memories.\n\n"
            "The Ashtavinayak Yatra is widely revered as the most sacred pilgrimage circuit in Western India, drawing lakhs of devotees seeking blessings from Lord Ganesha. For families planning a comforting spiritual escape, choosing the Best Maharashtra Tour Package or a personalized Maharashtra Family Tour ensures a completely hassle-free road trip across magnificent Western Ghat landscapes and rustic architectural heritage.\n\n"
            "From the majestic stone fortress style of Mayureshwar temple at Morgaon to the fascinating cave architecture at Lenyadri Hills, our custom Luxury Maharashtra Holiday guarantees unmatched comfort. This meticulously mapped pilgrimage features highly sought-after Maharashtra Sightseeing gems, popular photography points, and serene environments. Our TRAGUIN Maharashtra Packages are specifically tailored with premium stays and luxury vehicles to deliver an immersive experience filled with pure devotion and tranquility.\n\n"
            "TRAGUIN Curated Experience Note: This luxury pilgrimage package focuses heavily on smooth transfers, priority VIP darshan arrangements wherever accessible, senior-citizen friendly pacing, and handpicked hotels offering fine vegetarian dining."
        ),
        seo_title='MH-008 | Sacred Ashtavinayak Darshan Circuit | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Ashtavinayak pilgrimage (MH-008 / TRAGUIN-MH-008): Morgaon, Siddhatek, Theur, Ranjangaon, Ozar, Lenyadri, Pali, Mahad, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Moreshwar Temple (Morgaon), Siddhivinayak Temple (Siddhatek) & Chintamani Temple (Theur)', 1),
            _ih('Mahaganapati Temple (Ranjangaon), Vighneshwar Temple (Ozar) & Girijatmaj Temple (Lenyadri Caves)', 2),
            _ih('Ballaleshwar Temple (Pali), Varadvinayak Temple (Mahad) & Morgaon Return Darshan', 3),
            _ih('TRAGUIN Signature Experience: Curated carefully by regional travel experts with local assistance at each temple site', 4),
            _ih('Premium Handpicked Hotels: 4-tier options from Pride Hotel Pune to The Ritz-Carlton Pune & The Machan Luxury Resort', 5),
        ],
        days=[
            _day(
                1,
                'Pune Arrival • Morgaon • Siddhatek • Theur',
                (
                    'Arrive at Pune Airport or Railway Station, where a premium TRAGUIN corporate representative gives you a warm traditional greeting. Board your private luxury vehicle and proceed directly to begin the sacred Maharashtra Sightseeing yatra. Your first destination is the iconic Moreshwar Temple at Morgaon, the starting point of the circuit featuring an ancient fort-like architecture. After an enriching morning darshan, drive along scenic country routes to the Siddhivinayak Temple at Siddhatek, remarkably perched on a hillock alongside the Bhima River. Complete your evening at the peaceful Chintamani Temple in Theur, beautifully flanked by the Mula-Mutha river. Check in to your premium hotel in Pune for a relaxed night.'
                ),
                [
                    'Sightseeing Included: Moreshwar Temple (Morgaon), Siddhivinayak Temple (Siddhatek), Chintamani Temple (Theur).',
                    'Evening Experience: Witness a soothing evening Maha-Aarti ceremony at Theur Ganesha temple.',
                    'Overnight Stay: Handpicked Luxury Hotel, Pune.',
                    'Meals Included: Courteous Welcome Drink & Premium Vegetarian Dinner.',
                ],
            ),
            _day(
                2,
                'Pune • Ranjangaon • Ozar • Lenyadri',
                (
                    'Savor a nutritious breakfast before driving toward the majestic Mahaganapati Temple at Ranjangaon, famous for its grand gateway and powerful multi-headed representation of Ganesha. Continue your journey through breathtaking landscapes to the riverside town of Ozar to visit the Vighneshwar Temple, enclosed within magnificent stone walls and topped with a glittering golden dome. In the afternoon, explore the dramatic mountain sceneries around Lenyadri. Here, the unique Girijatmaj Temple is beautifully carved directly inside one of the 30 ancient rock-cut Buddhist caves on a mountain face. A comfortable palanquin (doli) service can easily be arranged by your guide for senior citizens to reach the cave smoothly.'
                ),
                [
                    'Sightseeing Included: Mahaganapati Temple (Ranjangaon), Vighneshwar Temple (Ozar), Girijatmaj Temple (Lenyadri Caves).',
                    'Photography Points: Beautiful panoramas from the Kukadi river banks in Ozar and the majestic Lenyadri hill cliffs.',
                    'Overnight Stay: Premium Stay / Luxury Resort, Ozar or Narayangaon.',
                    'Meals Included: Buffet Breakfast & Gourmet Vegetarian Dinner.',
                ],
            ),
            _day(
                3,
                'Lenyadri • Pali • Mahad',
                (
                    'After a relaxed morning breakfast, descend toward the highly scenic coastal Konkan foothills. Arrive at the historical town of Pali to seek blessings at the Ballaleshwar Temple, the only Ashtavinayak shrine named directly after a devoted devotee. The temple features a remarkable architecture designed to let the sunrays fall straight on the deity during festivals. Later, proceed along stunning Western Ghat mountain passes to reach Mahad, home to the sacred Varadvinayak Temple, where an unceasing holy oil lamp (Nanda Deep) has been kept lit for over a century. Check in to your luxury resort nearby and unwind amidst pristine natural landscapes.'
                ),
                [
                    'Sightseeing Included: Ballaleshwar Temple (Pali), Varadvinayak Temple (Mahad).',
                    'Optional Activities: A gentle cultural walk through traditional Konkan-style villages surrounding Pali.',
                    'Overnight Stay: Handpicked Premium Resort, Lonavala / Mahad.',
                    'Meals Included: Full Breakfast & Authentic Regional Maharashtrian Dinner.',
                ],
            ),
            _day(
                4,
                'Mahad • Pune Return & Departure',
                (
                    'On this final day of your Premium Maharashtra Experience, enjoy a lavish breakfast at the resort while admiring the misty hills. According to sacred scriptures, a pilgrim must return to the very first temple to formally close the loop of the yatra. Your luxury vehicle will smoothly take you back to Morgaon for your final logical closing prayers. Conclude your pilgrimage with a comfortable drive back to Pune city. Your professional chauffeur transfers you seamlessly to Pune Airport or Railway Station to board your return transit. Your holy yatra concludes, leaving you with divine blessings and unforgettable memories organized beautifully by TRAGUIN.'
                ),
                [
                    'Sightseeing / Transfers Included: Morgaon Return Darshan, Transit to Pune Airport.',
                    'Meals Included: Rich Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('Pride Hotel, Pune / Hotel Yadnyesh, Ozar', 'Pune / Ozar', '03 Nights', 'Deluxe', 'Standard Room', 'MAP (Breakfast & Dinner)', 4, 1),
            _hotel('The Orchid Hotel, Pune / Tejomaya Luxury Stays, Lenyadri', 'Pune / Lenyadri', '03 Nights', 'Premium', 'Premium Room', 'MAP (Breakfast & Dinner)', 5, 2),
            _hotel('JW Marriott Hotel, Pune / Heritage Agro Resort, Junnar', 'Pune / Junnar', '03 Nights', 'Luxury', 'Luxury Room', 'Gourmet MAP Plan', 5, 3),
            _hotel('The Ritz-Carlton, Pune / The Machan Luxury Resort, Lonavala', 'Pune / Lonavala', '03 Nights', 'Ultra Luxury', 'Luxury Suite', 'Ultra-Luxury Curated Meals', 5, 4),
        ],
        inclusions=[
            _inc_included('Premium Stays: 03 Nights accommodation in handpicked hotels and luxury spiritual wellness resorts.', 1),
            _inc_included('Gourmet Dining: 03 Premium Breakfasts and 03 specially prepared pure vegetarian dinners at the hotels.', 2),
            _inc_included('Luxury Transportation: Private Chauffeur-driven air-conditioned Luxury Toyota Innova Crysta for all point-to-point transit.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated telephone concierge assistance and certified spiritual companion guide.', 4),
            _inc_included('Welcome Amenities: Executive welcome kit including sacred pooja materials, regional destination maps, and bottled mineral water.', 5),
            _inc_included('Complimentary Experiences: Inclusive parking, state highway taxes, driver allowances, and special floral offerings at all 8 Ganesha shrines.', 6),
            _inc_excluded('Airfare or interstate train tickets to and from Pune.', 7),
            _inc_excluded('Individual entry tickets to any monuments, museums, or local doli/palanquin fees at Lenyadri.', 8),
            _inc_excluded('Personal expenses such as laundry, specialty phone calls, tips, and additional ritual dakshina.', 9),
            _inc_excluded('Mandatory travel insurance, medical covers, or emergency evacuation expenses.', 10),
        ],
    )
    return package, itinerary

def build_mh_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MH-009'
    tour_code = 'TRAGUIN-MH-009'
    title = 'Mumbai City Sightseeing & Bollywood Glamour'
    duration = '03 Nights / 04 Days'
    slug = 'mh-009-mumbai-city-sightseeing-bollywood-glamour'
    itin_slug = 'mh-009-mumbai-city-sightseeing-bollywood-glamour-itinerary'
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
            _ph('State / Country: Maharashtra / India | Category: Family Vacation / Luxury Heritage', 2),
            _ph('Destinations: Mumbai City • Bollywood Studios • Juhu', 3),
            _ph('Ideal for: Families, Couples & Film Enthusiasts', 4),
            _ph('Best season: October to May', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Luxury City & Film Industry FIT Experience', 7),
            _ph('Vehicle: Private Executive Air-Conditioned Luxury Sedan / Premium Innova Crysta', 8),
            _ph('Meal Plan: Buffet Breakfast at Premium Luxury Stays & Specialized Bollywood Lunch', 9),
            _ph('Route Map: Mumbai International Airport Arrival → South Mumbai Heritage → Bollywood Studio Tour → Juhu → Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts with seamless coordination, pre-reserved tickets, premium transportation, and private local storytellers at historic landmarks', 11),
            _ph('Shopping: Colaba Causeway & Crawford Market — fine leather goods, antique curios, brass artifacts, organic local spices; Boutiques & High-End Malls — customized luxury fashion from designer studios', 12),
            _ph('Important: Check-in 14:00 hrs; Bollywood live studio visits subject to production schedules with safe equivalent options if restricted', 13),
        ],
        moods=['Heritage', 'City', 'Luxury'],
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
        tagline='Mumbai City Sightseeing & Bollywood Glamour • 03 Nights / 04 Days',
        overview=(
            "Step into the magical realm of India's maximum city. Curated lovingly by TRAGUIN experts, this elite getaway balances high-end coastal luxury with immersive storytelling through historical colonial structures, world-famous coastal drives, and an exclusive insider pass to the vibrant corridors of the Indian Film Industry. Create unforgettable memories with your family on a premium stay meticulously customized for ultimate comfort.\n\n"
            "Mumbai, the beating heart of Maharashtra, offers breathtaking landscapes along the Arabian Sea, iconic attractions, and unmatched cultural depth. Whether you are seeking a premier Maharashtra Family Tour or a memorable Maharashtra Honeymoon Package, this itinerary hits every popular Instagram location flawlessly.\n\n"
            "From capturing historical photos outside the majestic Gateway of India to tracking the elite lifestyle of movie stars at Bandra, our Premium Maharashtra Experience promises deep immersion. Witness the top tourist places in Maharashtra, indulge in boutique shopping markets, and dive deep into historical colonial monuments with the absolute security and peace of mind provided by TRAGUIN Maharashtra Packages.\n\n"
            "TRAGUIN Curated Experience Note: Includes a VIP access pass into real live sets, an expert colonial architectural historian guide, pre-reserved entry tokens, and a dedicated 24/7 personal travel consultant."
        ),
        seo_title='MH-009 | Mumbai City Sightseeing & Bollywood Glamour | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Mumbai package (MH-009 / TRAGUIN-MH-009): Marine Drive, Gateway of India, CSMT, Bollywood studio tour, Juhu Beach, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Marine Drive, Gateway of India, Colaba Promenade & premium high-tea overlooking the Arabian Sea', 1),
            _ih('CSMT Station, Mani Bhavan, Dhobi Ghat & Bandra-Worli Sea Link', 2),
            _ih('Live Shoot Set Tour, Bollywood Museum, Actor Bungalow Drives & Juhu Beach', 3),
            _ih('TRAGUIN Signature Experience: Curated by TRAGUIN Experts with pre-reserved tickets and private local storytellers', 4),
            _ih('Premium Handpicked Hotels: 4-tier options from Trident Nariman Point to The St. Regis Mumbai', 5),
        ],
        days=[
            _day(
                1,
                'Mumbai Arrival',
                (
                    'Arrive in style at Mumbai International Airport where your private elite chauffeur welcomes you with customized amenities. Drive along the beautiful Marine Drive, enjoying the scenic beauty of the city\'s coastline. Check in seamlessly to your handpicked hotel facing the ocean. As the sun sets, walk around the iconic Colaba Causeway for boutique souvenir shopping and premium café experiences.'
                ),
                [
                    'Sightseeing Included: Marine Drive, Gateway of India, Colaba Promenade.',
                    'Evening Experience: Sip on premium high-tea overlooking the Arabian Sea, arranged exclusively by TRAGUIN experts.',
                    'Overnight Stay: Ultra Luxury Sea-Facing Hotel, Mumbai.',
                    'Meals Included: Welcome Drink & Dinner.',
                ],
            ),
            _day(
                2,
                'Mumbai City Sightseeing',
                (
                    'Savor a luxurious buffet breakfast. Embark on a comprehensive Mumbai Sightseeing drive led by an expert guide. Tour the Chhatrapati Shivaji Maharaj Terminus (UNESCO World Heritage Site) to witness stunning Victorian Gothic architecture. Visit Mani Bhavan, the peaceful residence of Mahatma Gandhi, followed by a picturesque drive through the iconic Bandra-Worli Sea Link.'
                ),
                [
                    'Sightseeing Included: Gateway of India, CSMT Station, Dhobi Ghat, Bandra-Worli Sea Link.',
                    'Photography Points: Splendid mid-sea angles from the Bandra-Worli Sea Link bridge.',
                    'Overnight Stay: Handpicked Luxury Resort, Mumbai.',
                    'Meals Included: Gourmet Breakfast & Dinner.',
                ],
            ),
            _day(
                3,
                'Bollywood Experiences',
                (
                    'Today introduces the centerpiece of your holiday—an exclusive, privately guided trip into the legendary world of Bollywood. Enter prominent film studios to view real-world sound stages, post-production edit suites, and a live dance performance. Walk through historic costume galleries before driving past the grand residential bungalows of legendary actors in Bandra and Juhu.'
                ),
                [
                    'Sightseeing Included: Live Shoot Set Tour, Bollywood Museum, Actor Bungalow Drives, Juhu Beach.',
                    'Local Experiences: Try customized recording inside a dubbing studio for a fun family memory.',
                    'Overnight Stay: Premium Luxury Beachfront Resort, Juhu.',
                    'Meals Included: Breakfast, Special Studio Lunch & Dinner.',
                ],
            ),
            _day(
                4,
                'Departure from Mumbai',
                (
                    'Enjoy a relaxed morning beach stroll outside your resort. Following a leisurely breakfast, pack your unique souvenirs and traditional artifacts. Your private luxury vehicle will escort your family back to the airport for your onward journey, successfully concluding your high-end experience.'
                ),
                [
                    'Transfers Included: Private Airport Drop-off.',
                    'Meals Included: Full Breakfast Buffet.',
                ],
            ),
        ],
        hotels=[
            _hotel('Trident, Nariman Point', 'Mumbai', '03 Nights', 'Deluxe', 'Superior Sea View Room', 'CP (Breakfast Only)', 4, 1),
            _hotel('JW Marriott, Juhu Beach', 'Mumbai', '03 Nights', 'Premium', 'Deluxe Ocean View Room', 'MAP (Breakfast + Dinner)', 5, 2),
            _hotel('The Taj Mahal Palace, Colaba', 'Mumbai', '03 Nights', 'Luxury', 'Luxury Heritage Wing Room', 'MAP (Breakfast + Dinner)', 5, 3),
            _hotel('The St. Regis, Mumbai', 'Mumbai', '03 Nights', 'Ultra Luxury', 'St. Regis Suite with Butler Service', 'MAP + VIP Lounge Entry', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: Premium stays at ultra-luxury handpicked hotels with ocean views.', 1),
            _inc_included('Meals: Generous luxury breakfasts daily and a specialized lunch block inside Bollywood studios.', 2),
            _inc_included('Transfers & Sightseeing: Private high-end AC vehicle for all transfers and iconic attractions.', 3),
            _inc_included('TRAGUIN Support: Elite holiday support throughout, with instant priority response parameters.', 4),
            _inc_included('Complimentary Experiences: VIP entry tickets into active filming zones and pre-arranged monument permits.', 5),
            _inc_included('Welcome Amenities: Customized greeting hamper including premium local chocolates, fresh wet wipes, and cold mineral water.', 6),
            _inc_excluded('Airfare / Train tickets to Mumbai.', 7),
            _inc_excluded('Personal spending accounts such as laundry, long-distance phone lines, and room service.', 8),
            _inc_excluded('Professional camera fees inside heritage monuments.', 9),
            _inc_excluded('Comprehensive health or baggage travel insurance covers.', 10),
        ],
    )
    return package, itinerary

def build_mh_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MH-010'
    tour_code = 'TRAGUIN-MH-010'
    title = 'Lavasa Lakeside Resort & Pune Heritage Tour'
    duration = '03 Nights / 04 Days'
    slug = 'mh-010-lavasa-lakeside-resort-pune-heritage-tour'
    itin_slug = 'mh-010-lavasa-lakeside-resort-pune-heritage-tour-itinerary'
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
            _ph('State / Country: Maharashtra, India | Category: Family Vacation / Luxury', 2),
            _ph('Destinations: Pune • Lavasa Lakeside Resort', 3),
            _ph('Ideal for: Families, Leisure & Heritage Seekers', 4),
            _ph('Best season: June to March (Monsoon/Winter)', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Luxury Family FIT Getaway', 7),
            _ph('Vehicle: Private Air-Conditioned Luxury Innova Crysta / Premium Chauffeur-driven Sedan', 8),
            _ph('Meal Plan: Modified American Plan (Buffet Breakfast & Multi-cuisine Dinners Included)', 9),
            _ph('Route Map: Pune Arrival → Shaniwar Wada Heritage Loop → Lavasa Waterfront Retreat → Pune Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts with pre-vetted rooms, guaranteed VIP check-ins, private cruise experience, and premium vehicle logistics', 11),
            _ph('Shopping: Chitale Bandhu Bakarwadi, Laxminarayan Chivda, fine brass souvenirs; Instagram Spots — Lavasa Promenade, Aga Khan Palace, misty lakeside piers', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; monsoon months show mountains at greenest; vehicle exclusively for itinerary routes', 13),
        ],
        moods=['Family', 'Heritage', 'Luxury'],
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
        tagline='Lavasa Lakeside Resort & Pune Heritage Tour • 03 Nights / 04 Days',
        overview=(
            "Step into a mesmerizing blend of royal Maratha history and European lakeside elegance. Carefully hand-crafted by TRAGUIN, this ultra-premium Maharashtra Family Tour whisks your loved ones away to experience majestic forts, ancient palaces, and the stunning waterfront architecture of Lavasa. Let us create unforgettable memories wrapped in comfort, scenic beauty, and customized luxury.\n\n"
            "Whether you are planning a relaxing getaway or seeking a detailed Maharashtra Honeymoon Package, the historical landscape of Pune coupled with the tranquil Western Ghats offers the perfect luxury weekend escape. From the legendary Maratha bravery carved into the walls of Shaniwar Wada to the serene, pastel-colored Italian-style boardwalks of Lavasa, this short-haul getaway is highly sought after by discerning travelers.\n\n"
            "With our signature TRAGUIN Maharashtra Packages, your family travels in absolute style. Discover the Top Tourist Places in Maharashtra, capture breathtaking landscapes on your camera, and unwind at handpicked hotels selected strictly for their elite service and luxury standards. This itinerary presents premium hospitality at its finest, ensuring every detail is expertly managed.\n\n"
            "TRAGUIN Curated Note: A perfectly synchronized balance of slow-paced family relaxation and deep cultural discovery."
        ),
        seo_title='MH-010 | Lavasa Lakeside Resort & Pune Heritage Tour | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Pune & Lavasa package (MH-010 / TRAGUIN-MH-010): Aga Khan Palace, Shaniwar Wada, Lavasa promenade, private Dasve Lake cruise, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Aga Khan Palace, seamless arrival transfers & high-tea briefing by TRAGUIN experts', 1),
            _ih('Shaniwar Wada, Dagdusheth Temple, Lavasa Dasve Viewpoint & sunset over Dasve Lake', 2),
            _ih('Lavasa Promenade Walk, Lakeside Esplanade & exclusive private pontoon boat cruise on Dasve Lake', 3),
            _ih('TRAGUIN Signature Experience: Curated by TRAGUIN Experts for effortless luxury journey', 4),
            _ih('Premium Handpicked Hotels: 4-tier options from Hyatt Pune to The Ritz-Carlton Pune & Elite Villa Suite', 5),
        ],
        days=[
            _day(
                1,
                'Pune Arrival',
                (
                    'Arrive at Pune International Airport or Railway Station where your professional TRAGUIN tour manager greets you with warm local hospitality. Board your private luxury vehicle and transfer smoothly to your handpicked hotel. After checking in, head out for a classic afternoon introduction to Pune Sightseeing. Visit the magnificent Aga Khan Palace, an architectural marvel with Italian arches and vast green lawns that served as a monumental site in India\'s freedom struggle. Conclude your day with a comforting traditional dinner at the hotel.'
                ),
                [
                    'Sightseeing Included: Aga Khan Palace, seamless arrival transfers.',
                    'Evening Experience: A warm high-tea briefing hosted by our travel experts to customize your family parameters.',
                    'Overnight Stay: Premium Luxury Hotel, Pune.',
                    'Meals Included: Welcome Drink & Buffet Dinner.',
                ],
            ),
            _day(
                2,
                'Pune Heritage to Lavasa',
                (
                    'Following a delicious breakfast, deep dive into the iconic history of the Peshwas. Visit Shaniwar Wada, the historical fortification that tells stories of ancient valour and royal intrigue. Next, take a peaceful moment at the sacred Dagdusheth Halwai Ganpati Temple. By afternoon, your luxury chauffeur guides you down a picturesque mountain route into the Western Ghats. Watch the landscape transform into lush green valleys as you arrive at the beautiful lakeside township of Lavasa. Check in to your lakeside luxury resort and enjoy a sunset view over Dasve Lake.'
                ),
                [
                    'Sightseeing Included: Shaniwar Wada, Dagdusheth Temple, Lavasa Dasve Viewpoint.',
                    'Photography Points: The towering stone gates of Shaniwar Wada and the winding mist-laden mountain passes.',
                    'Overnight Stay: Premium Waterfront Resort, Lavasa.',
                    'Meals Included: Full Breakfast & Gourmet Dinner.',
                ],
            ),
            _day(
                3,
                'Lavasa Lakeside Leisure',
                (
                    'Wake up to the gentle lapping of waves. Today is dedicated to immersive experiences along the Lavasa promenade. Take a leisurely family stroll along the colorful European-inspired streets, exploring charming lakeside cafes and boutique shops. In the afternoon, enjoy an exclusive private pontoon boat cruise arranged exclusively by TRAGUIN, letting you glide smoothly across the water while admiring the surrounding green hills. Spend a relaxed evening sharing stories by the lake.'
                ),
                [
                    'Sightseeing Included: Lavasa Promenade Walk, Lakeside Esplanade.',
                    'Optional Activities: Gentle water sports, cycling along the promenade, or a signature spa treatment.',
                    'Evening Experience: Al-fresco lakeside dining experience under a canopy of stars.',
                    'Overnight Stay: Premium Waterfront Resort, Lavasa.',
                    'Meals Included: Full Breakfast & Dinner.',
                ],
            ),
            _day(
                4,
                'Lavasa to Pune Departure',
                (
                    'Indulge in a relaxed breakfast overlooking the misty lake. Pack your bags filled with hand-woven textiles and memorable photographs. Enjoy a comfortable drive back down the mountains directly to Pune Airport or Railway Station for your onward journey. Your premium Luxury Maharashtra Holiday concludes seamlessly, leaving you with memories that linger long after you return home.'
                ),
                [
                    'Transfers Included: Private Luxury Airport / Station Drop-off.',
                    'Meals Included: Full Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('Hyatt Pune / The Waterfront Shaw Apartments', 'Pune / Lavasa', '03 Nights', 'Deluxe', 'Standard Room', 'MAPAI (Breakfast + Dinner)', 4, 1),
            _hotel('Sheraton Grand Pune / Fortune Select Dasve, Lavasa', 'Pune / Lavasa', '03 Nights', 'Premium', 'Premium Room', 'MAPAI (Breakfast + Dinner)', 5, 2),
            _hotel('JW Marriott Hotel Pune / Mercure Lavasa (Valley View Room)', 'Pune / Lavasa', '03 Nights', 'Luxury', 'Valley View Room', 'MAPAI (Gourmet Buffet)', 5, 3),
            _hotel('The Ritz-Carlton, Pune / Elite Villa Suite Luxury Stay', 'Pune / Lavasa', '03 Nights', 'Ultra Luxury', 'Elite Villa Suite', 'MAPAI + High Tea Included', 5, 4),
        ],
        inclusions=[
            _inc_included('Premium Stays: 03 Nights accommodation in handpicked hotels and luxury lakeside resorts.', 1),
            _inc_included('Gourmet Dining: Daily premium breakfast spreads and curated multi-cuisine buffet dinners at all hotels.', 2),
            _inc_included('Luxury Transportation: Dedicated Chauffeur-driven AC Innova Crysta for all airport transfers, inter-city travel, and sightseeing loops.', 3),
            _inc_included('Exclusive Experiences: Private chartered boat cruise on Lavasa\'s Dasve Lake.', 4),
            _inc_included('TRAGUIN Support: 24/7 dedicated remote concierge support and destination assistance.', 5),
            _inc_included('Welcome Amenities: Executive welcome kit including fresh refreshments, wet wipes, and premium packaged drinking water.', 6),
            _inc_included('Taxes: All standard toll taxes, parking fees, fuel surcharges, and state driver allowances.', 7),
            _inc_excluded('Airfare or interstate train tickets to and from Pune.', 8),
            _inc_excluded('Monument entry keys, historical camera permissions, or local guide services.', 9),
            _inc_excluded('Personal incidentals such as laundry, phone tabs, and individual tips.', 10),
            _inc_excluded('Water sports activities or optional adventure tours in Lavasa.', 11),
            _inc_excluded('Any personal medical insurance or contingency expenditures.', 12),
        ],
    )
    return package, itinerary

def build_mh_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MH-011'
    tour_code = 'TRAGUIN-MH-011'
    title = 'Grand Maharashtra Explorer Tour'
    duration = '08 Nights / 09 Days'
    slug = 'mh-011-grand-maharashtra-explorer-tour'
    itin_slug = 'mh-011-grand-maharashtra-explorer-tour-itinerary'
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
            _ph('State / Country: Maharashtra, India | Category: Family / Luxury Escape', 2),
            _ph('Destinations: Mumbai • Lonavala • Mahabaleshwar • Pune • Aurangabad', 3),
            _ph('Ideal for: Families, Leisure Seekers & Heritage Lovers', 4),
            _ph('Best season: October to May', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Grand Maharashtra Explorer FIT Vacation', 7),
            _ph('Vehicle: Private Chauffeur-driven Luxury SUV (Innova Crysta / Premium Coach) equipped with refreshing amenities', 8),
            _ph('Meal Plan: Modified American Plan (Buffet Breakfasts and Gourmet Dinners included at all premium stays)', 9),
            _ph('Route Map: Mumbai (2N) → Lonavala (1N) → Mahabaleshwar (2N) → Pune (1N) → Aurangabad (2N)', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts for families seeking zero-hassle luxury with pre-vetted premium stays and priority check-ins', 11),
            _ph('Shopping: Colaba Causeway & Crawford Market (Mumbai), Bhudwar Peth & Laxmi Road (Pune), Aurangabad Bazaars — Himroo shawls and Bidriware', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; light wrap for hill station evenings; TRAGUIN aligns Ajanta/Ellora cave schedules for closure days', 13),
        ],
        moods=['Family', 'Heritage', 'Luxury'],
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
        tagline='Grand Maharashtra Explorer Tour • 08 Nights / 09 Days',
        overview=(
            "Welcome to a breathtaking journey across the vibrant heart of India. This premium Maharashtra Family Tour, meticulously structured by TRAGUIN, perfectly blends the high-octane luxury of Mumbai, the crisp mountain air of misty hill stations, and the timeless architectural awe of world heritage cave monuments. Specially curated for discerning families, our Premium Maharashtra Experience promises signature comfort, exclusive touches, and unforgettable memories for every generation.\n\n"
            "Why choose a luxury holiday in Maharashtra? As one of India's most diverse domains, it offers an astonishing spectrum of famous attractions ranging from glamorous coastal shorelines to dramatic Western Ghats mountain ridges and centuries-old rock-cut shrines. This definitive Maharashtra Honeymoon Package and family itinerary opens doors to the Top Tourist Places in Maharashtra, making it the highest sought-after travel loop for discerning travelers.\n\n"
            "From capturing the perfect sunset at Marine Drive or tracking historic relics inside the Ajanta and Ellora caves to plucking fresh strawberries in beautiful Mahabaleshwar, your family will experience unmatched cultural and natural depth. The Best Time to Visit Maharashtra falls during the cooler autumn and spring seasons, when the breathtaking landscapes turn into lush panoramic heavens, pristine for photography, adventure, and absolute relaxation.\n\n"
            "TRAGUIN Curated Experience Note: Every detail of this Luxury Maharashtra Holiday has been refined by our experts to ensure seamless transfers, handpicked hotels, VIP fast-track entries to historical attractions, and deeply immersive local culinary journeys."
        ),
        seo_title='MH-011 | Grand Maharashtra Explorer Tour | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days Maharashtra explorer (MH-011 / TRAGUIN-MH-011): Mumbai, Lonavala, Mahabaleshwar, Pune, Ellora, Ajanta, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Gateway of India, Nariman Point, Bandra-Worli Sea Link & Marine Drive evening walk', 1),
            _ih('Elephanta Caves, CSMT, Mani Bhavan, Hanging Gardens & Karla & Bhaja Caves', 2),
            _ih('Venna Lake private boat ride, Arthur\'s Seat, Panchgani Table Land & Mapro Gardens', 3),
            _ih('Shaniwar Wada, Aga Khan Palace, Bibi Ka Maqbara, Ellora Caves & Ajanta Caves excursion', 4),
            _ih('TRAGUIN Signature Experience: Private boat ride on Venna Lake and VIP fast-track entry assistance', 5),
        ],
        days=[
            _day(
                1,
                'Mumbai Arrival',
                (
                    'Touchdown at Mumbai International Airport where your dedicated TRAGUIN tour ambassador welcomes you with a traditional gesture. Board your premium luxury private vehicle and slide comfortably through the metropolis towards your majestic sea-facing iconic hotel. After checking in and relaxing, spend your afternoon discovering the premium neighborhoods of South Mumbai. Wind down with an evening drive across the engineering marvel of the Bandra-Worli Sea Link.'
                ),
                [
                    'Sightseeing Included: Gateway of India, Nariman Point, Bandra-Worli Sea Link.',
                    'Evening Experience: A slow walk along Marine Drive as the lights sparkle into the "Queen\'s Necklace".',
                    'Overnight Stay: Handpicked Luxury Hotel, Mumbai.',
                    'Meals Included: Welcome Amenity & Dinner.',
                ],
            ),
            _day(
                2,
                'Mumbai Urban Exploration',
                (
                    'Relish a gourmet breakfast before taking a luxurious morning ferry ride to the ancient, rock-cut Elephanta Caves, a UNESCO World Heritage site showcasing glorious historic carvings. Return to the mainland for a curated heritage walk through the colossal colonial structures of Fort and Kala Ghoda. Later, discover Mani Bhavan, the serene residence of Mahatma Gandhi, followed by a drive past the iconic Dhobi Ghat and through the elite residential quarters of Malabar Hill.'
                ),
                [
                    'Sightseeing Included: Elephanta Caves, Chhatrapati Shivaji Maharaj Terminus (CSMT), Mani Bhavan, Hanging Gardens.',
                    'Food Suggestions: High-tea and artisanal pastries at an elite heritage café in Colaba.',
                    'Overnight Stay: Handpicked Luxury Hotel, Mumbai.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                3,
                'Mumbai to Lonavala',
                (
                    'Bid farewell to the coastline as your luxury vehicle begins its ascent into the spectacular hills of the Western Ghats. Arrive at the scenic mountain retreat of Lonavala. Check into your premium cliffside private villa or resort. In the afternoon, visit the dramatic Bhaja and Karla Caves, magnificent ancient Buddhist shrines carved deeply into the rock faces. Witness a breathtaking sunset from Khandala\'s Duke\'s Nose viewpoint.'
                ),
                [
                    'Sightseeing Included: Karla & Bhaja Caves, Lonavala Lake, Duke\'s Nose Point.',
                    'Optional Activities: Indulge in an exclusive private spa session overlooking the lush, deep valleys.',
                    'Overnight Stay: Premium Hillside Resort, Lonavala.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                4,
                'Lonavala to Mahabaleshwar',
                (
                    'Enjoy a relaxed breakfast amidst the mist. Your scenic driving route continues south through rolling hills to the high-altitude luxury haven of Mahabaleshwar. Famed for its evergreen forests, pristine lakes, and colonial charm, this town offers the ultimate rejuvenation space. Check into your ultra-luxury eco-resort nestled within private woods. Spend a leisurely evening at the pristine Venna Lake, enjoying an exclusive private boat ride.'
                ),
                [
                    'Sightseeing Included: Venna Lake, Local Highland Boardwalks.',
                    'Evening Experience: Private rowboat experience on Venna Lake with personal refreshments served onboard.',
                    'Overnight Stay: Premium Luxury Resort, Mahabaleshwar.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                5,
                'Mahabaleshwar & Panchgani',
                (
                    'An early morning excursion brings you to Arthur\'s Seat and Elphinstone Point, offering awe-inspiring canyon views of the Savitri river valley. Next, explore the old heritage structures of Mahabaleshwar Temple before moving down to neighboring Panchgani. Wander around the wide volcanic plateau of Table Land and spend your afternoon inside an organic strawberry orchard, plucking ripe seasonal fruits straight from the vine.'
                ),
                [
                    'Sightseeing Included: Arthur\'s Seat, Panchgani Table Land, Mapro Gardens, Strawberry Farms.',
                    'Photography Points: Phenomenal panoramas from the edge of Arthur\'s Seat overlooking deep valley drops.',
                    'Overnight Stay: Premium Luxury Resort, Mahabaleshwar.',
                    'Meals Included: Breakfast & Gourmet Theme Dinner.',
                ],
            ),
            _day(
                6,
                'Mahabaleshwar to Pune',
                (
                    'Descend the mist-laden hills after breakfast and proceed towards Pune, the proud cultural capital of the state. Check into your ultra-modern luxury city hotel. Your afternoon is dedicated to exploring the majestic ruins of Shaniwar Wada, the fortified seat of the Peshwas. Follow this with a comforting visit to the elegant Aga Khan Palace, a tranquil Italianate mansion filled with profound history and Italian arches.'
                ),
                [
                    'Sightseeing Included: Shaniwar Wada, Aga Khan Palace, Dagadusheth Halwai Temple.',
                    'Local Experiences: Taste traditional local Puneri sweets during a private tasting session.',
                    'Overnight Stay: Ultra-Luxury Hotel, Pune.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                7,
                'Pune to Aurangabad',
                (
                    'Embark on a smooth, comfortable morning drive heading north towards Aurangabad. Watch the transforming landscape unfold from green peaks into historical dry-deciduous valley basins. Check into your luxury palace hotel upon arrival. In the afternoon, visit the stunning Bibi Ka Maqbara, a grand 17th-century mausoleum built in memory of Aurangzeb\'s wife, often fondly celebrated as the "Taj of the Deccan".'
                ),
                [
                    'Sightseeing Included: Bibi Ka Maqbara, Panchakki (Ancient Water Mill).',
                    'Evening Experience: Relax within the hotel\'s lush Mughal-style gardens with live classical instrumental music.',
                    'Overnight Stay: Premium Luxury Palace Hotel, Aurangabad.',
                    'Meals Included: Breakfast & Royal Mughlai Dinner.',
                ],
            ),
            _day(
                8,
                'Ellora Caves & Daulatabad',
                (
                    'Prepare for an absolute highlight of your TRAGUIN Maharashtra Package. Travel to the magnificent Ellora Caves, an extraordinary assembly of Hindu, Buddhist, and Jain monuments. Marvel at the incredible Kailash Temple (Cave 16), the largest monolithic rock-cut structure in the world, carved from a single cliff surface downward. On the return route, pause at the impregnable hill fortress of Daulatabad, showcasing medieval military architectural brilliance.'
                ),
                [
                    'Sightseeing Included: Ellora Caves Complex, Kailash Temple, Daulatabad Fort.',
                    'Optional Activities: VIP guided interaction with a veteran archaeological historian at Ellora.',
                    'Overnight Stay: Premium Luxury Palace Hotel, Aurangabad.',
                    'Meals Included: Breakfast & Farewell Festive Dinner.',
                ],
            ),
            _day(
                9,
                'Aurangabad / Ajanta Excursion & Departure',
                (
                    'Following a majestic breakfast, complete your check-out. Depending on your flight timing, enjoy a premium excursion to the world-renowned Ajanta Caves, capturing the ultimate ancient Buddhist frescoes and wall paintings dating back to the 2nd Century BCE. Your private luxury vehicle will then smoothly transfer your family to Aurangabad Airport or back to Mumbai for your onward homebound flight. Your unparalleled travel experience concludes with timeless memories.'
                ),
                [
                    'Transfers Included: Premium Airport drop-off service.',
                    'Meals Included: Full Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('Trident Nariman Point / Fariyas Resort', 'Mumbai / Lonavala', '08 Nights', 'Deluxe', 'Standard Room', 'Breakfast & Dinner', 4, 1, description='Mahabaleshwar/Pune/Aurangabad: Brightland Resort / Hyatt Pune / Welcomhotel by ITC Rama International'),
            _hotel('Taj Mahal Tower / Radisson Resort', 'Mumbai / Lonavala', '08 Nights', 'Premium', 'Premium Room', 'Breakfast & Dinner', 5, 2, description='Mahabaleshwar/Pune/Aurangabad: Le Méridien / JW Marriott Pune / Vivanta Aurangabad'),
            _hotel('The Oberoi Mumbai / Rhythm Lonavala', 'Mumbai / Lonavala', '08 Nights', 'Luxury', 'Luxury Room', 'Breakfast & Dinner', 5, 3, description='Mahabaleshwar/Pune/Aurangabad: Evershine Resort / The Ritz-Carlton / Lemon Tree Amarante Palace'),
            _hotel('The Taj Mahal Palace / Hilton Shillim', 'Mumbai / Lonavala', '08 Nights', 'Ultra Luxury', 'Royal Suite', 'Breakfast & Dinner', 5, 4, description='Mahabaleshwar/Pune/Aurangabad: Le Méridien Forest Resort (Luxury Suite) / Taj Amiriya Palace (Royal Suite)'),
        ],
        inclusions=[
            _inc_included('Accommodation: 08 Nights stay in handpicked premium luxury hotels and world-class heritage resorts.', 1),
            _inc_included('Meals: Daily premium buffet breakfasts and custom-crafted specialty dinners at all stays.', 2),
            _inc_included('Transfers & Sightseeing: All city point-to-point journeys via an elite private air-conditioned vehicle.', 3),
            _inc_included('TRAGUIN Support: Real-time, 24/7 dedicated guest relations assistance and professional guide coordinates.', 4),
            _inc_included('Welcome Amenities: Royal traditional welcome kit, artisanal chocolate platter, and premium mineral water bottles.', 5),
            _inc_included('Complimentary Experiences: Private boat ride on Venna Lake and VIP fast-track entry assistance to historic monuments.', 6),
            _inc_excluded('Airfare or interstate rail passes to Mumbai / from Aurangabad.', 7),
            _inc_excluded('Individual entry tickets to caves, historical museums, and personal activities.', 8),
            _inc_excluded('Personal expenses such as room service, laundry, international call bills, and gratuities.', 9),
            _inc_excluded('Mandatory local holiday luxury tax additions or seasonal travel insurance cover.', 10),
        ],
    )
    return package, itinerary

def build_mh_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MH-012'
    tour_code = 'TRAGUIN-MH-012'
    title = 'Lonavala Khandala Weekend Escape'
    duration = '02 Nights / 03 Days'
    slug = 'mh-012-lonavala-khandala-weekend-escape'
    itin_slug = 'mh-012-lonavala-khandala-weekend-escape-itinerary'
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
            _ph('State / Country: Maharashtra / India | Category: Leisure Weekend Escape', 2),
            _ph('Destinations: Lonavala • Khandala', 3),
            _ph('Ideal for: Families, Couples & Friends', 4),
            _ph('Best season: Monsoons & Winters (June to March)', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Luxury Weekend FIT Getaway', 7),
            _ph('Vehicle: Private Air-Conditioned Premium Sedan / Luxury SUV', 8),
            _ph('Meal Plan: Daily Deluxe Buffet Breakfast Included', 9),
            _ph('Route Map: Mumbai/Pune Arrival → Lonavala Sightseeing → Khandala Hills → Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts with priority check-in assistance, custom handpicked valley-facing suites, and signature travel amenities', 11),
            _ph('Shopping: Maganlal\'s iconic peanut and kaju chikkis, classic mint fudges, traditional roasted savouries; Instagram Spots — Bushi Dam and Tiger\'s Leap', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; monsoon season offers magnificent live waterfalls; early advance bookings recommended for peak weekends', 13),
        ],
        moods=['Nature', 'Leisure', 'Weekend'],
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
        tagline='Lonavala Khandala Weekend Escape • 02 Nights / 03 Days',
        overview=(
            "Escape the mundane city rush and breathe in the mist-laden air of the Western Ghats. Tailored exclusively by luxury experts at TRAGUIN, this signature travel experience blends the natural grandeur of deep green valleys with handpicked premium comfort. Witness cascading seasonal waterfalls, dramatic cliffside panoramas, and historical wonders, creating unforgettable memories with your loved ones.\n\n"
            "Are you planning the absolute Best Maharashtra Tour Package or a romantic Maharashtra Honeymoon Package? Nestled deep within the Sahyadri mountain ranges, the twin hill stations of Lonavala and Khandala present some of the most spectacular breathtaking landscapes in Western India. Known universally for its cool mountain breezes, magnificent mist blankets, and deep valleys, it stands out as the ultimate destination for an elite Maharashtra Family Tour.\n\n"
            "From exploring the historical rock-cut architecture of Karla Caves to admiring the iconic attractions such as Duke's Nose and Tiger's Leap, this luxury retreat covers the top tourist places in Maharashtra. Discover pristine lakes, taste authentic hot local chikkis, and capture stunning visual panoramas at popular Instagram locations. Our meticulously curated TRAGUIN Maharashtra Packages ensure a highly safe, refreshing, and deeply relaxing holiday environment away from the city bustle.\n\n"
            "TRAGUIN Curated Experience Note: This Luxury Maharashtra Holiday features localized premium stays, a private tailored itinerary for maximum relaxation, signature sunset vantage access, and dedicated executive customer support throughout your weekend getaways."
        ),
        seo_title='MH-012 | Lonavala Khandala Weekend Escape | TRAGUIN',
        seo_description='Premium 02 Nights / 03 Days Lonavala Khandala package (MH-012 / TRAGUIN-MH-012): Bushi Dam, Karla Caves, Tiger\'s Leap, Duke\'s Nose, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Bushi Dam, Lonavala Lake, Sunset Point & complimentary chikki tasting experience', 1),
            _ih('Karla Caves, Tiger\'s Leap, Bhaja Caves & Amrutanjan Point', 2),
            _ih('Duke\'s Nose, Khandala Ghat Viewpoint & Local Emporiums', 3),
            _ih('TRAGUIN Signature Experience: Priority check-in assistance and custom handpicked valley-facing suites', 4),
            _ih('Premium Handpicked Hotels: 4-tier options from Fariyas Resort to The Machan treehouse resort', 5),
        ],
        days=[
            _day(
                1,
                'Mumbai / Pune to Lonavala',
                (
                    'Arrive at Mumbai or Pune airport/railway station, where your dedicated executive private vehicle awaits you. Embark on a spectacular scenic route up into the Western Ghats as you approach your luxury hill destination. Check into your premium handpicked resort seamlessly. In the afternoon, begin your introductory tour by visiting the stunning Lonavala Lake and the gorgeous Bushi Dam, where water flows dramatically over stepped stone masonry. Capture beautiful family photography points surrounded by lush hills.'
                ),
                [
                    'Sightseeing Included: Bushi Dam, Lonavala Lake, Sunset Point.',
                    'Evening Experience: Stroll along the vibrant local avenues and indulge in a complimentary warm fudge and chikki tasting experience.',
                    'Overnight Stay: Handpicked Premium Resort, Lonavala.',
                    'Meals Included: Welcome Drink & Gourmet Dinner.',
                ],
            ),
            _day(
                2,
                'Lonavala & Kakadu Valley Exploration',
                (
                    'Savor a luxurious morning breakfast at your resort. Set off to discover the magnificent architectural marvels of the ancient 2nd-century BC Karla Caves and Bhaja Caves, displaying wonderful Buddhist rock-cut shrines. After a delightful traditional Maharashtrian lunch recommendation, drive up to the dramatic cliff edges of Tiger\'s Leap and Amrutanjan Point. Peer down into deep, sheer gorges filled with low-hanging clouds and feel the refreshing valley wind face-to-face.'
                ),
                [
                    'Sightseeing Included: Karla Caves, Tiger\'s Leap, Bhaja Caves, Amrutanjan Point.',
                    'Optional Activities: A light, guided trek to Rajmachi Viewpoint for expansive views of old fortress ruins.',
                    'Overnight Stay: Premium Luxury Mountain Resort, Lonavala.',
                    'Meals Included: Full Buffet Breakfast & Dinner.',
                ],
            ),
            _day(
                3,
                'Khandala Sightseeing to Departure',
                (
                    'Enjoy a relaxed breakfast watching the morning fog clear from the valley below. Check out from your resort and proceed into the neighbouring sister hill station of Khandala. Explore the iconic Duke\'s Nose viewpoint, named after its unique shape resembling the Duke of Wellington. Take a final stop at the panoramic Khandala Ghat Viewpoint for memorable landscape photography. Afterward, your private vehicle will smoothly transfer you back to Mumbai or Pune for your return flight or train home, concluding your premium getaway.'
                ),
                [
                    'Sightseeing Included: Duke\'s Nose, Khandala Ghat Viewpoint, Local Emporiums.',
                    'Food Suggestions: Stop by heritage cafes on the highway for fresh hot Vada Pav and Misal Pav.',
                    'Transfers Included: Private Drop-off to Mumbai or Pune Station/Airport.',
                    'Meals Included: Full Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('Fariyas Resort, Lonavala', 'Lonavala', '02 Nights', 'Deluxe', 'Deluxe Valley View Room', 'CP (Breakfast Only)', 4, 1),
            _hotel('Rhythm Lonavala', 'Lonavala', '02 Nights', 'Premium', 'Cypress Luxury Suite', 'CPAI (Breakfast Included)', 5, 2),
            _hotel('Della Resorts, Lonavala', 'Lonavala', '02 Nights', 'Luxury', 'Luxury Resort Room', 'MAPAI (Breakfast + Dinner)', 5, 3),
            _hotel('The Machan (Boutique Treehouse Resort)', 'Lonavala', '02 Nights', 'Ultra Luxury', 'Canopy Machan / Forest Suite', 'MAPAI + Private High Tea', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: 02 Nights stay at handpicked elite luxury hotels or treehouse villas.', 1),
            _inc_included('Meals: Daily premium gourmet buffet breakfast at the respective hotel dining venues.', 2),
            _inc_included('Transfers & Sightseeing: Dedicated private AC vehicle with professional chauffeur for all transfers and tourist places.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated local customer support and comprehensive concierge assistance.', 4),
            _inc_included('Welcome Amenities: Custom high-quality welcome drink, mineral water bottles, and a special premium chikki hamper.', 5),
            _inc_included('Taxes & Tolls: All state taxes, fuel charges, parking fees, and highway toll expenses included.', 6),
            _inc_excluded('Flights, train fares, or state transit connections to Mumbai/Pune.', 7),
            _inc_excluded('Direct entrance tickets for caves, historical monuments, or specific adventure parks.', 8),
            _inc_excluded('Personal expenses such as premium laundry, internal phone bills, room service, or tips.', 9),
            _inc_excluded('Optional tours, extreme sports, or extra vehicle mileage beyond scheduled destinations.', 10),
            _inc_excluded('Mandatory individual medical or cancellation travel insurance policies.', 11),
        ],
    )
    return package, itinerary


def build_mh_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MH-013'
    tour_code = 'TRAGUIN-MH-013'
    title = 'Mahabaleshwar Panchgani Delight'
    duration = '03 Nights / 04 Days'
    slug = 'mh-013-mahabaleshwar-panchgani-delight'
    itin_slug = 'mh-013-mahabaleshwar-panchgani-delight-itinerary'
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
            _ph('State / Country: Maharashtra / India | Category: Luxury Leisure', 2),
            _ph('Destinations: Mahabaleshwar • Panchgani', 3),
            _ph('Ideal for: Families, Couples & Corporate Leisure', 4),
            _ph('Best season: October to May', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Luxury Hill Station FIT Vacation', 7),
            _ph('Vehicle: Private Chauffeur-driven AC Sedan / Luxury SUV (Crysta)', 8),
            _ph('Meal Plan: Modified American Plan (Daily Premium Breakfast & Dinners Included)', 9),
            _ph('Route Map: Pune/Mumbai Pick-up → Panchgani Heights → Mahabaleshwar Valley → Heritage Exploration → Return Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated carefully by elite domain experts with handpicked hotels, luxury transportation, and direct exclusive access points to legendary views', 11),
            _ph('Shopping: Organic strawberry syrups, locally harvested honey, jellies, fresh chikkis; Handicrafts — Mahabaleshwar leather footwear and custom cane artifacts', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; light cardigans advised for evenings; advance itinerary locking recommended for premium valley suites', 13),
        ],
        moods=['Nature', 'Leisure', 'Luxury'],
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
        tagline='Mahabaleshwar Panchgani Delight • 03 Nights / 04 Days',
        overview=(
            "Welcome to a timeless getaway amidst the misty Western Ghats. Crafted meticulously by TRAGUIN, this high-end Mahabaleshwar Honeymoon Package and Mahabaleshwar Family Tour brings you close to rolling strawberry fields, historic vistas, and pure, crisp mountain breezes. Let us submerge your senses in tailored luxury, seamless private transits, and unforgettable memories across the spectacular landscape.\n\n"
            "Nestled beautifully within the Sahyadri mountain ranges, Mahabaleshwar stands proud as the undisputed king of hill stations in Maharashtra. Highly sought-after by travelers searching for a true Luxury Mahabaleshwar Holiday, this retreat combines rich British-era history, colonial architecture, and deep emerald valleys. From the spectacular sunrise points to panoramic views of Venna Lake, our TRAGUIN Mahabaleshwar Packages bring together all the top tourist places under a grand premium itinerary.\n\n"
            "Whether it is your search for the most popular Instagram spots like Arthur's Seat and Mapro Gardens, or a relaxing stroll through the historical lanes of Panchgani's tablelands, we present highly curated experiences. The region transforms into a paradise during winters and post-monsoon months, making it the Best Time to Visit Mahabaleshwar to capture breathtaking landscapes, enjoy premium stays, and build lifelong bonds with your loved ones.\n\n"
            "TRAGUIN Curated Experience Note: This signature vacation is perfectly designed to feature slow-paced journeys, exclusive resort stays, premium local culinary treats, private entry assistance at viewpoints, and dedicated tour manager tracking for a hassle-free premium holiday."
        ),
        seo_title='MH-013 | Mahabaleshwar Panchgani Delight | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Mahabaleshwar package (MH-013 / TRAGUIN-MH-013): Panchgani Table Land, Arthur\'s Seat, Mapro Garden, Venna Lake, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Panchgani Table Land, Sydney Point & Parsi Point Overlook', 1),
            _ih('Arthur\'s Seat, Echo Point, Old Mahabaleshwar Temple & Mapro Garden', 2),
            _ih('Venna Lake private rowboat cruise, Local Town Bazaar & Lodwick Point', 3),
            _ih('TRAGUIN Signature Experience: Handpicked hotels with direct exclusive access to legendary views', 4),
            _ih('Premium Handpicked Hotels: 4-tier options from Brightland Resort to Courtyard by Marriott Mahabaleshwar', 5),
        ],
        days=[
            _day(
                1,
                'Pune / Mumbai to Panchgani & Mahabaleshwar',
                (
                    'Your premium Mahabaleshwar Sightseeing journey begins with a private luxury pick-up from Pune or Mumbai. Leave the chaotic city lines behind as you ascend the scenic Sahyadri mountain roads. Stop at the gorgeous town of Panchgani to experience the massive volcanic plateau known as Table Land—the second-longest mountain plateau in Asia. Take in the breathtaking landscapes and spectacular valley views below before proceeding to your ultra-luxury resort in Mahabaleshwar for a seamless check-in experience arranged by TRAGUIN.'
                ),
                [
                    'Sightseeing Included: Panchgani Table Land, Sydney Point, Parsi Point Overlook.',
                    'Evening Experience: Relax on your private resort balcony with a fresh pot of hot local tea overlooking the valley.',
                    'Overnight Stay: Handpicked Luxury Resort, Mahabaleshwar.',
                    'Meals Included: Gourmet Buffet Dinner.',
                ],
            ),
            _day(
                2,
                'Mahabaleshwar Valley Exploration',
                (
                    'Indulge in a glorious spread of breakfast before setting out for an immersive full-day tour of the most iconic attractions. Marvel at the dramatic drops at Arthur\'s Seat, often termed the queen of all points due to its fascinating floating-object phenomenon. Discover Elphinstone Point and the ancient architectural wonder of the Mahabaleshwar Temple, housing a natural stone Shiva Lingam. In the afternoon, dive deep into the world-famous Mapro Garden. Witness real fruit processing and treat your tastebuds to their signature fresh strawberry-with-cream delight.'
                ),
                [
                    'Sightseeing Included: Arthur\'s Seat, Echo Point, Old Mahabaleshwar Temple, Mapro Garden.',
                    'Photography Points: Crimson reflections over the valley gates from Kate\'s Point and Elephant\'s Head rock formation.',
                    'Overnight Stay: Handpicked Luxury Resort, Mahabaleshwar.',
                    'Meals Included: Premium Breakfast & Dinner.',
                ],
            ),
            _day(
                3,
                'Venna Lake Leisure & Shopping Scripts',
                (
                    'Wake up to the sounds of nature. Today\'s experience takes a highly leisurely approach. Head to the placid waters of Venna Lake, surrounded entirely by tall, dense trees. Enjoy a private, exclusive rowboat cruise across the lake while mist dances on the surface. In the afternoon, explore the bustling local town market. This evening is reserved for emotional storytelling and bonding around a cozy bonfire at your resort property, organized specially under your curated holiday package.'
                ),
                [
                    'Sightseeing Included: Venna Lake, Local Town Bazaar, Lodwick Point.',
                    'Optional Activities: Horseback riding along the nature trails surrounding Venna Lake.',
                    'Overnight Stay: Handpicked Luxury Resort, Mahabaleshwar.',
                    'Meals Included: Premium Breakfast & Dinner.',
                ],
            ),
            _day(
                4,
                'Mahabaleshwar to Pune / Mumbai Departure',
                (
                    'Cherish your final morning watching the sun rise through the mountain fog. After an extensive breakfast layout, check out comfortably from your premium sanctuary. Your private chauffeur will drive you smoothly down the hills back toward Pune or Mumbai airport/railway station. Your unforgettable premium vacation closes with smiles and beautiful moments shared across the horizons.'
                ),
                [
                    'Transfers Included: Private Chauffeur Drop-off to Mumbai/Pune.',
                    'Meals Included: Premium Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('Brightland Resort & Spa', 'Mahabaleshwar', '03 Nights', 'Deluxe', 'Deluxe Valley View Room', 'MAP (Breakfast + Dinner)', 4, 1),
            _hotel('Evershine Resort & Spa', 'Mahabaleshwar', '03 Nights', 'Premium', 'Executive Garden Room', 'MAP (Breakfast + Dinner)', 5, 2),
            _hotel('Le Méridien Mahabaleshwar Resort', 'Mahabaleshwar', '03 Nights', 'Luxury', 'Classic Forest View Room', 'MAP (Gourmet Buffet)', 5, 3),
            _hotel('Courtyard by Marriott Mahabaleshwar', 'Mahabaleshwar', '03 Nights', 'Ultra Luxury', 'Premium Valley View Suite', 'MAP Plus Signature Perks', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: 03 Nights exquisite stay at ultra-premium handpicked luxury hotels.', 1),
            _inc_included('Meals: 03 Premium Multi-cuisine Breakfasts and 03 Specially Curated Dinners at the properties.', 2),
            _inc_included('Transfers & Sightseeing: All transits using a private luxury dedicated air-conditioned vehicle from start to end.', 3),
            _inc_included('TRAGUIN Support: Priority 24/7 on-call travel concierge support and complete driver assistance.', 4),
            _inc_included('Welcome Amenities: Customized luxury arrival kit with seasonal local fresh fruit baskets and treats.', 5),
            _inc_included('Complimentary Experiences: Private entry boat cruise coupon code for Venna Lake boating.', 6),
            _inc_included('Taxes: All current applicable destination resort taxes, toll fees, driver beta, and fuel prices included.', 7),
            _inc_excluded('Airfare or main train connectivity fares to Mumbai/Pune hubs.', 8),
            _inc_excluded('Individual entry tickets for camera gear or specific adventure sports inside theme areas.', 9),
            _inc_excluded('Personal elements such as dry cleaning, premium alcoholic beverages, and separate room-service orders.', 10),
            _inc_excluded('Optional activities or detours outside the standard route definitions.', 11),
        ],
    )
    return package, itinerary


def build_mh_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MH-014'
    tour_code = 'TRAGUIN-MH-014'
    title = 'Matheran Eco Hill Station Stay'
    duration = '02 Nights / 03 Days'
    slug = 'mh-014-matheran-eco-hill-station-stay'
    itin_slug = 'mh-014-matheran-eco-hill-station-stay-itinerary'
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
            _ph('State / Country: Maharashtra / India | Category: Leisure Vacation / Weekend Getaway', 2),
            _ph('Destinations: Matheran Eco Hill Station', 3),
            _ph('Ideal for: Families, Couples & Nature Lovers', 4),
            _ph('Best season: October to May (Lush green in Monsoons)', 5),
            _ph('Starting price: On Request (Premium Luxury Pricing)', 6),
            _ph('Travel Format: Independent FIT Luxury Escape', 7),
            _ph('Vehicle: Private Air-Conditioned Luxury Sedan for transfers to Dasturi Naka, followed by premium hand-pulled rickshaw or horseback access inside the eco-zone', 8),
            _ph('Meal Plan: Modified American Plan (All gourmet daily breakfasts and curated dinners included)', 9),
            _ph('Route Map: Mumbai/Pune Pick-up → Dasturi Naka → Matheran Eco Hill Station → Dasturi Naka → Mumbai/Pune Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated meticulously by TRAGUIN Experts with personalized assistance, bypass long lines at Dasturi Naka, and access to premium handpicked heritage hotels', 11),
            _ph('Shopping: Handmade leather footwear, exquisite walking sticks, sweet local peanut / honey Chikki; Instagram Spots — vintage locomotive tracks, Charlotte lake shore, Louisa Point', 12),
            _ph('Important: Motor vehicles banned inside Matheran — walking, horseback riding, or hand-pulled rickshaws only; check-in 13:00 hrs, check-out 10:00 hrs; early reservations recommended for heritage boutique hotels', 13),
        ],
        moods=['Nature', 'Eco', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Luxury Pricing)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Matheran Eco Hill Station Stay • 02 Nights / 03 Days',
        overview=(
            "Step into an untamed sanctuary entirely untouched by modern vehicular noise. This exclusive, high-end Matheran Honeymoon Package and family retreat curated by TRAGUIN experts promises an absolute detachment from urban chaos. Nestled smoothly within the Western Ghats, Asia's only automobile-free eco hill station invites you to embrace breathtaking landscapes, panoramic valleys, and timeless luxury heritage.\n\n"
            "Why plan a Luxury Matheran Holiday? Matheran is an extraordinary environmental marvel, celebrated globally for its red-laterite soil pathways, cool mountain breeze, and dense forest canopy. For sophisticated souls hunting for the ideal Matheran Family Tour, this hill station showcases iconic attractions like Panorama Point, Charlotte Lake, and Louisa Point without any vehicular interruption.\n\n"
            "The Best Time to Visit Matheran stretches from the post-monsoon freshness of October through the pleasant summer of May. Our carefully selected ultra-luxury resorts blend seamlessly with nature while offering exceptional modern amenities. Capture highly searched Instagram locations, wander through historical local markets, and experience legendary colonial charm elevated beautifully via high-end TRAGUIN Matheran Packages.\n\n"
            "TRAGUIN Curated Experience Note: This premium itinerary ensures handpicked colonial-style heritage hotels, private companion assistance across scenic trails, localized culinary highlights, and a signature slow-paced immersive travel layout designed to create unforgettable memories."
        ),
        seo_title='MH-014 | Matheran Eco Hill Station Stay | TRAGUIN',
        seo_description='Premium 02 Nights / 03 Days Matheran package (MH-014 / TRAGUIN-MH-014): Dasturi Naka, Echo Point, Louisa Point, Charlotte Lake, heritage toy train tracks, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Dasturi Naka Transition, Echo Point & Alexander Point with artisan high-tea on colonial veranda', 1),
            _ih('Louisa Point, Charlotte Lake, Lord\'s Point & Shivaji\'s Ladder', 2),
            _ih('Matheran Heritage Rail Walk & return transfer via Dasturi Naka', 3),
            _ih('TRAGUIN Signature Experience: Bypass long lines at Dasturi Naka and secure healthiest private trail horses', 4),
            _ih('Premium Handpicked Hotels: 4-tier heritage options from Hotel Point View to The Dune Barr House', 5),
        ],
        days=[
            _day(
                1,
                'Arrival & Welcome to Automobile-Free Paradise',
                (
                    'Your premium holiday unfolds with a smooth pick-up in a luxury air-conditioned vehicle from Mumbai or Pune airport/railway station. Enjoy a magnificent, winding scenic route as you ascend toward the Western Ghats, arriving at Dasturi Naka—the absolute boundary for all motor vehicles. From here, transition into an exclusive horse-carriage or premium hand-pulled rickshaw ride arranged by your dedicated coordinator. Check in smoothly to your handpicked heritage boutique hotel. In the late afternoon, enjoy your first immersive walk to the near-iconic Echo Point and watch the sky change colors over the deep valleys from Alexander Point.'
                ),
                [
                    'Sightseeing Included: Dasturi Naka Transition, Echo Point, Alexander Point.',
                    'Evening Experience: Indulge in an artisan high-tea session served on the colonial veranda of your premium stay.',
                    'Overnight Stay: Handpicked Premium Luxury Resort, Matheran.',
                    'Meals Included: Welcome Amenity & Curated Buffet Dinner.',
                ],
            ),
            _day(
                2,
                'Impeccable Valleys & Charlotte Lake Nostalgia',
                (
                    'Awake to the glorious singing of native birds and enjoy a luxurious breakfast. Today is dedicated to spectacular Matheran Sightseeing. Take a smooth, picturesque horse trail to the breathtaking Louisa Point, which presents unhindered views of the historic Prabal Fort and majestic sheer drops. Proceed across a tranquil shaded path to Charlotte Lake, the pristine primary water source of the hill station, bordered by an ancient temple and lush green foliage. Spend a serene afternoon taking beautiful photographs at Lord\'s Point. In the evening, explore the vibrant town square for classic shopping and delicious local delicacies.'
                ),
                [
                    'Sightseeing Included: Louisa Point, Charlotte Lake, Lord\'s Point, Shivaji\'s Ladder.',
                    'Optional Activities: A guided sunset walk to Panorama Point for a dramatic 360-degree view of the mountain ranges.',
                    'Photography Points: The crisp reflections on Charlotte Lake and the deep chasms around Louisa Point.',
                    'Overnight Stay: Handpicked Premium Luxury Resort, Matheran.',
                    'Meals Included: Full Breakfast & Fine-Dining Dinner.',
                ],
            ),
            _day(
                3,
                'Heritage Toy Train Tracks & Farewell',
                (
                    'Savor a final slow-paced gourmet breakfast at your resort while soaking in the therapeutic forest air. Take a gentle morning stroll alongside the famous narrow-gauge heritage toy train tracks, an iconic marvel of Indian hill travel history. Check out comfortably from your resort. Your private horse or rickshaw transfer will convey you smoothly back to Dasturi Naka, where your luxury private car waits to transfer you back to Mumbai or Pune. Your memorable premium holiday concludes, leaving you with unforgettable memories.'
                ),
                [
                    'Sightseeing Included: Matheran Heritage Rail Walk, Return Transfer.',
                    'Food Suggestions: Sample hot local fudge and spiced chana chaat near the station market before leaving.',
                    'Meals Included: Full Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('Hotel Point View / Similar', 'Matheran', '02 Nights', 'Deluxe', 'Super Deluxe AC Room', 'Breakfast & Dinner', 4, 1),
            _hotel('Adamo The Resort / Similar', 'Matheran', '02 Nights', 'Premium', 'Regent Deluxe Villa Room', 'Breakfast & Dinner', 5, 2),
            _hotel('The Verandah in the Forest (Neemrana Heritage)', 'Matheran', '02 Nights', 'Luxury', 'Heritage Colonial Suite', 'Breakfast & Dinner', 5, 3),
            _hotel('The Dune Barr House (Boutique Heritage Croft)', 'Matheran', '02 Nights', 'Ultra Luxury', 'Elphinstone / Grand Luxury Suite', 'Breakfast & Dinner', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: 02 Nights of premium stays at luxury handpicked hotels or colonial heritage properties.', 1),
            _inc_included('Meals: Daily multi-cuisine buffet breakfasts and premium dinners at the resort restaurant.', 2),
            _inc_included('Transfers: Air-conditioned private luxury sedan transfer from Mumbai/Pune to Dasturi Naka and return.', 3),
            _inc_included('Sightseeing: Guided private trekking or horseback route mappings across all major tourist places.', 4),
            _inc_included('Assistance: Complete 24/7 personalized TRAGUIN backup and local support.', 5),
            _inc_included('Taxes: All applicable luxury resort taxes, toll expenses, and parking charges.', 6),
            _inc_included('Welcome Amenities: Personalized eco-friendly welcome hamper upon arrival.', 7),
            _inc_excluded('Flights, train fares, or interstate permit costs.', 8),
            _inc_excluded('Local eco-station entry taxes (Matheran Municipal Council Chapa tax).', 9),
            _inc_excluded('Personal expenses such as laundry, porter tips, premium alcoholic drinks, and phone calls.', 10),
            _inc_excluded('Optional tours, horse rides, or toy train tickets.', 11),
            _inc_excluded('Comprehensive medical or personal travel insurance.', 12),
        ],
    )
    return package, itinerary


MAHARASHTRA_DOMESTIC_BUILDERS = [
    build_mh_006,
    build_mh_007,
    build_mh_008,
    build_mh_009,
    build_mh_010,
    build_mh_011,
    build_mh_012,
    build_mh_013,
    build_mh_014,
]
