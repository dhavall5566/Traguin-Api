"""Builder functions for MP-001 through MP-010 Madhya Pradesh domestic packages (MP-006 skipped)."""

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


def build_mp_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MP-001'
    tour_code = 'TG-MPHT-2026'
    title = 'The Royal Heritage Trail: Gwalior • Orchha • Khajuraho'
    duration = '05 Nights / 06 Days'
    slug = 'mp-001-the-royal-heritage-trail-gwalior-orchha-khajuraho'
    itin_slug = 'mp-001-the-royal-heritage-trail-gwalior-orchha-khajuraho-itinerary'
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
            _ph('Serial code MP-001 | TRAGUIN tour code TG-MPHT-2026', 1),
            _ph('State / Country: Madhya Pradesh, India | Category: Premium Family Tour', 2),
            _ph('Destinations: Gwalior • Orchha • Khajuraho', 3),
            _ph('Ideal for: Families, Culture & Heritage Enthusiasts', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium Luxury Tier)', 6),
            _ph('Route: Gwalior (1N) ➔ Orchha (2N) ➔ Khajuraho (2N)', 7),
            _ph('Vehicle / Meals: Luxury Toyota Innova Crysta / Luxury Coach | Premium Breakfast & Dinner (MAPAI)', 8),
            _ph('TRAGUIN Curated Experience Note: At TRAGUIN, we believe family vacations should be effortless and deeply enriching. Our signatures on this itinerary include private sound and light shows, royal high tea experiences overlooking pristine rivers, and handpicked local guides who bring centuries-old architecture alive for adults and children alike.', 9),
            _ph('TRAGUIN Signature Experience: Private family high-tea overlooking the ancient Chhatris on the tranquil Betwa River bank.', 10),
            _ph('Shopping & Local Experiences: Gwalior: Chanderi and Maheshwari silk sarees, carpets, and brassware at Patankar Bazaar; Bedai Sabzi and Jalebis. Orchha: Dokra metal crafts and terracotta pottery. Khajuraho: silver jewelry and carved stone miniatures.', 11),
            _ph('Important: Hotel check-in 14:00 / check-out 11:00. Conservative dress at temples. Book Taj Usha Kiran Palace and Lalit Temple View 60–90 days in advance for peak winter.', 12),
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
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='The Royal Heritage Trail: Gwalior • Orchha • Khajuraho • 05 Nights / 06 Days',
        overview="Welcome to the heart of incredible India. The Best Madhya Pradesh Tour Package curated by TRAGUIN invites your family to step back into a golden era of majestic forts, royal palaces, pristine rivers, and UNESCO World Heritage temples. This ultra-curated itinerary seamlessly blends deep historical storytelling with premium comfort, offering an unmatched Luxury Madhya Pradesh Holiday that caters beautifully to multi- generational family bonding. Experience the breathtaking landscapes and profound spirituality that make Central India an elite global destination.\n\nTOUR OVERVIEW\nThis bespoke Madhya Pradesh Family Tour takes you across the magnificent cultural triangle of northern Madhya Pradesh. Beginning in the royal stronghold of Gwalior, traveling down to the frozen-in-time medieval town of Orchha, and culminating at the architectural wonders of Khajuraho, every segment is hand-tailored. Enjoy a flawless private journey with luxury transport, handpicked heritage hotels, and immersive expert-guided walking tours. Travel Dates: Flexible / Custom FIT Group Type: Private Family Vacation Vehicle: Luxury Toyota Innova Crysta / Luxury Coach Meal Plan: Premium Breakfast & Dinner (MAPAI) Route Plan: Gwalior (1N) ➔ Orchha (2N) ➔ Khajuraho (2N)\n\nWHY CHOOSE THE PREMIUM MADHYA PRADESH HERITAGE TRAIL?\nA journey through Madhya Pradesh is an immersion into the very soul of Indian heritage. Recognized globally for hosting some of the most spectacular Top Tourist Places in Madhya Pradesh, this route offers an unparalleled educational and emotional escape for families. Famous Attractions: Explore the impregnable Gwalior Fort (termed the 'Gibraltar of India'), the stunning Jai Vilas Palace, the multi-layered palaces of Orchha on the Betwa River, and the world- renowned UNESCO World Heritage Khajuraho Temples. Most Searched Experiences: Witnessing the surreal evening Aarti on the banks of the Betwa River in Orchha, exploring hidden royal cenotaphs, and enjoying the legendary Light and Sound shows that project history onto ancient stone facades. Family & Honeymoon Highlights: Romantic riverside luxury stays for couples, open-jeep safaris in nearby sanctuaries, and interactive pottery or cultural workshops that keep children fully engaged and inspired. Popular Instagram Locations: The intricate turquoise-tiled facade of Man Singh Palace in Gwalior, the soaring spires of the Chaturbhuj Temple against a setting sun, and the jaw-dropping architectural geometry of the Lakshmana Temple in Khajuraho. Best Time to Visit Madhya Pradesh: The winter months from October to March present perfect weather, featuring crisp mornings and pleasant sunny afternoons, ideal for outdoor Madhya Pradesh Sightseeing and photography.\n\nTRAGUIN Curated Experience Note: At TRAGUIN, we believe family vacations should be effortless and deeply enriching. Our signatures on this itinerary include private sound and light shows, royal high tea experiences overlooking pristine rivers, and handpicked local guides who bring centuries-old architecture alive for adults and children alike.",
        seo_title='MP-001 | The Royal Heritage Trail | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Madhya Pradesh package (MP-001 / TG-MPHT-2026): Gwalior Fort, Jai Vilas Palace, Orchha Chhatris, Khajuraho UNESCO temples, Raneh Falls, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Jai Vilas Palace, Gwalior Fort, Man Mandir Palace & VIP Gwalior Fort Sound & Light Show', 1),
            _ih('Orchha Fort Complex, Ram Raja Temple Aarti, Royal Chhatris & TRAGUIN Riverside High Tea', 2),
            _ih('Khajuraho Southern & Western Group UNESCO temples, Sound & Light Show & Raneh Falls Granite Canyon', 3),
            _ih('TRAGUIN Signature Experience: Private family high-tea overlooking the ancient Chhatris on the Betwa River bank', 4),
        ],
        days=[
            _day(
                1,
                'GWALIOR — ARRIVAL & THE CITADEL OF ROYAL GRANDEUR',
                ("Arrive in the historic city of Gwalior, where you will be warmly received by your dedicated TRAGUIN tour manager and private chauffeur. Transfer in style to your handpicked luxury heritage hotel. After a smooth check-in and an exquisite traditional lunch, embark on your Gwalior Sightseeing journey. Visit the breathtaking Jai Vilas Palace, a grand 19th-century mansion displaying an astonishing blend of Italian, Tuscan, and Corinthian architecture. Marvel at the Durbar Hall housing two of the world's largest crystal chandeliers and the legendary silver model train that served fine spirits and cigars to royal guests across the dining table. In the late afternoon, ascend to the majestic Gwalior Fort, standing high on a sandstone hill. Wander through the striking blue-and-yellow tiled walls of the Man Mandir Palace. As dusk falls, enjoy a Premium Gwalior Experience with VIP seating at the spectacular Sound and Light Show, where the rich history of the Tomar, Mughal, and Scindia dynasties is narratively brought to life."),
                [
                    'Sightseeing Included: Jai Vilas Palace, Gwalior Fort, Man Mandir Palace, Saas-Bahu Temples, Teli Ka Mandir.',
                    'Evening Experience: VIP Tickets to the Gwalior Fort Sound & Light Show.',
                    'Overnight Stay: Premium Heritage Hotel, Gwalior.',
                    'Meals Included: Welcome Drink & Gourmet Dinner.',
                ],
            ),
            _day(
                2,
                'GWALIOR TO ORCHHA — JOURNEY TO THE MEDIEVAL KINGDOM',
                ('Savor a luxurious breakfast at your hotel before departing via a highly scenic driving route toward the medieval gem of Orchha. This hidden treasure, nestled along the pristine Betwa River, looks today exactly as it did in the 16th century under the Bundela kings. Upon arrival, check into an exclusive luxury riverside resort curated meticulously by TRAGUIN specialists. After settling in, start your exploration of the magnificent Orchha Fort Complex. Walk through the sprawling courtyards of the Raja Mahal with its brilliant religious murals, and the Jahangir Mahal, a tier-structured palace built specifically for a single-night imperial visit, offering sweeping panoramic views of the surrounding dense forests and ancient spires. As the sun begins to set, gather at the historic Ram Raja Temple—the only temple in India where Lord Rama is worshiped as a ruling king and given a daily royal guard of honor—for a deeply moving evening prayer ceremony.'),
                [
                    'Sightseeing Included: Scenic drive to Orchha, Raja Mahal, Jahangir Mahal, Camel Stable.',
                    'Evening Experience: Evening Aarti Ceremony at Ram Raja Temple followed by a walk through local bazaars.',
                    'Optional Activities: Soft adventurous river rafting on Betwa River or an artisanal pottery workshop.',
                    'Overnight Stay: Luxury Riverside Resort, Orchha.',
                    'Meals Included: Buffet Breakfast & Traditional Bundelkhandi Dinner.',
                ],
            ),
            _day(
                3,
                'ORCHHA — RIVERSIDE CHHATRIS & IMMERSIVE LOCAL CULTURE',
                ("Wake up to the serene sounds of nature and river water flowing past your resort. Today promises an deeply immersive day of Orchha Sightseeing. Following a leisurely breakfast, visit the iconic Orchha Chhatris—fourteen spectacular cenotaphs lined elegantly along the riverbank, acting as eternal memorials to the Bundela rulers. An expert historian will guide your family through the hidden architectural symbolism of these structures. In the afternoon, enjoy a TRAGUIN Signature Experience: a curated high-tea set up at a private spot overlooking the Betwa River. Later, visit the awe-inspiring Chaturbhuj Temple, an architectural marvel built on a massive stone platform. The evening is yours to relax at the resort's premium spa or join an optional, highly recommended river rafting experience that glides gently past the illuminated cenotaphs under the starry sky."),
                [
                    'Sightseeing Included: Royal Chhatris, Chaturbhuj Temple, Laxminarayan Temple (famous for vibrant ceiling frescoes).',
                    'Evening Experience: Exclusive TRAGUIN Riverside High Tea & Sunset Photography session.',
                    'Optional Activities: Soft adventurous river rafting on Betwa River or an artisanal pottery workshop.',
                    'Overnight Stay: Luxury Riverside Resort, Orchha.',
                    'Meals Included: Breakfast, Royal High Tea, & Curated Dinner.',
                ],
            ),
            _day(
                4,
                'ORCHHA TO KHAJURAHO — THE PINNACLE OF STONE ARTISTRY',
                ('Following an early breakfast, say goodbye to Orchha as your premium vehicle drives you deeper into Bundelkhand to the world-famous town of Khajuraho. This destination is globally celebrated for hosting the Best Khajuraho Tour Package highlights: the unparalleled UNESCO World Heritage site temples. Check into your ultra-luxury resort and relax. In the afternoon, begin an extraordinary journey into ancient Indian artistry as you explore the Southern Group of Temples, including Duladeo and Chaturbhuj temples. These structures are renowned for their slender, elegant carvings and deeply spiritual architecture. In the evening, attend the legendary Khajuraho Sound and Light Show held in the lush gardens of the western complex, narrated beautifully in the iconic voice of Indian cinema, providing a perfect introduction to the architectural mastery you will witness up close the following morning.'),
                [
                    'Sightseeing Included: Countryside drive, Khajuraho Southern Group of Temples.',
                    'Evening Experience: Sound and Light Show at the Western Group of Temples.',
                    'Overnight Stay: Ultra-Luxury Resort, Khajuraho.',
                    'Meals Included: Breakfast & Multi-cuisine Fine Dining Dinner.',
                ],
            ),
            _day(
                5,
                'KHAJURAHO — UNESCO WORLD HERITAGE WONDERS & WILDERNESS',
                ("This morning marks the undisputed highlight of your Luxury Madhya Pradesh Holiday. Accompanied by a government-approved master storyteller guide, spend your morning uncovering the world-renowned Western Group of Temples. Marvel at the soaring Kandariya Mahadeva Temple, an architectural model of the cosmic mountain Shiva, covered in thousands of intricately detailed sculptures depicting celestial musicians, mythical beasts, historical battles, and celebrated erotic art celebrating the joy of life. Visit the pristine Lakshmana and Vishvanatha temples, learning about the advanced engineering used by Chandela architects over a millennium ago. In the afternoon, enjoy a complete change of scenery with an exciting excursion to the breathtaking Raneh Falls. Located just short drive away, this spot features an incredible 5-kilometer-long, 100-foot-deep canyon formed of pure, multi-colored crystalline granite, often called the 'Grand Canyon of India'. Keep your eyes open for wildlife in the adjacent Ken Gharial Sanctuary before returning to your luxury resort for a special farewell dinner organized by the TRAGUIN team."),
                [
                    'Sightseeing Included: Western Group of Temples (Kandariya Mahadeva, Lakshmana, Matangeshwar), Raneh Falls Granite Canyon.',
                    'Optional Activities: Early morning yoga session within resort gardens or a soothing Ayurvedic full-body massage.',
                    'Overnight Stay: Ultra-Luxury Resort, Khajuraho.',
                    'Meals Included: Gourmet Breakfast & Grand Farewell Dinner.',
                ],
            ),
            _day(
                6,
                'KHAJURAHO — DEPARTURE WITH UNFORGETTABLE MEMORIES',
                ("Indulge in a final, sumptuous breakfast at your luxury resort. Enjoy a relaxed morning taking advantage of the resort's premium amenities, swimming pool, or walking paths. Depending on your flight or train schedule, your private chauffeur will provide a seamless transfer to the Khajuraho Airport or Jhansi Railway Station for your onward journey home. Your premium family heritage exploration concludes here, leaving you with beautiful photographs, deep cultural enrichment, and unforgettable memories crafted meticulously by TRAGUIN."),
                [
                    'Sightseeing Included: Airport/Station Private Departure Transfer.',
                    'Meals Included: Premium Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Hotel Neemrana's Deo Bagh | Amar Mahal Palace (Deluxe) | Radisson Jass Khajuraho",
                'Gwalior | Orchha | Khajuraho',
                '05 Nights',
                'Deluxe',
                'Executive Deluxe Room',
                'Breakfast & Dinner',
                4,
                1,
            ),
            _hotel(
                'Taj Usha Kiran Palace (Superior) | Orchha Palace & Convention Centre | Ramada by Wyndham Heritage',
                'Gwalior | Orchha | Khajuraho',
                '05 Nights',
                'Premium',
                'Premium Room',
                'Breakfast & Dinner',
                4,
                2,
            ),
            _hotel(
                'Taj Usha Kiran Palace (Executive) | Amar Mahal (Suite Tier) | The Lalit Temple View Khajuraho',
                'Gwalior | Orchha | Khajuraho',
                '05 Nights',
                'Luxury',
                'Luxury Suite',
                'Breakfast & Dinner',
                5,
                3,
            ),
            _hotel(
                'Taj Usha Kiran Palace (Royal Suite) | The Orchha Resort (Luxury Villas) | The Lalit Temple View (Executive Suite)',
                'Gwalior | Orchha | Khajuraho',
                '05 Nights',
                'Ultra Luxury',
                'Royal Suite',
                'Breakfast & Dinner',
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included('Premium Stays: 05 Nights luxury accommodation across handpicked premium hotels and resorts.', 1),
            _inc_included('Gourmet Dining: Daily buffet breakfast and chef-curated dinners at all hotels.', 2),
            _inc_included('Luxury Transportation: Private air-conditioned luxury vehicle (Toyota Innova Crysta or premium coach) for all sightseeing, transfers, and intercity travel as per the itinerary.', 3),
            _inc_included('Elite Guiding: Private services of local, government-approved master storyteller guides in Gwalior, Orchha, and Khajuraho.', 4),
            _inc_included('TRAGUIN Signatures: Complimentary Riverside High Tea experience in Orchha and customized family photography assistance.', 5),
            _inc_included('Welcome Amenities: Royal traditional welcome at hotels, premium mineral water bottles provided daily inside the vehicle, and custom travel kits.', 6),
            _inc_included('Assistance & Taxes: 24/7 dedicated concierge support from TRAGUIN experts, fuel costs, toll taxes, parking charges, and driver allowances.', 7),
            _inc_excluded('Airfare / Rail: Any domestic or international flights, or main train tickets to Gwalior/from Khajuraho.', 8),
            _inc_excluded('Monument Entry Tickets: Entrance fees to monuments, palaces, and cameras unless specified in final custom pricing.', 9),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, alcoholic beverages, spa treatments, and tips for drivers or guides.', 10),
            _inc_excluded('Optional Activities: River rafting charges, optional safari tickets, or extra items not listed in inclusions.', 11),
            _inc_excluded('Insurance: Travel insurance and medical costs of any kind.', 12),
        ],
    )
    return package, itinerary

def build_mp_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MP-002'
    tour_code = 'TG-MP-KO-05D'
    title = 'Echos of Kings & Gods: Khajuraho • Orchha Heritage Escape'
    duration = '04 Nights / 05 Days'
    slug = 'mp-002-echos-of-kings-gods-khajuraho-orchha-heritage-escape'
    itin_slug = 'mp-002-echos-of-kings-gods-khajuraho-orchha-heritage-escape-itinerary'
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
            _ph('Serial code MP-002 | TRAGUIN tour code TG-MP-KO-05D', 1),
            _ph('State / Country: Madhya Pradesh, India | Category: Premium Family Tour', 2),
            _ph('Destinations: Khajuraho • Orchha', 3),
            _ph('Ideal for: Families, History & Culture Lovers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium/Luxury Tier)', 6),
            _ph('Route: Khajuraho (2 Nights) ➔ Orchha (2 Nights)', 7),
            _ph('Vehicle / Meals: Private Luxury Innova Crysta | Premium Breakfast & Dinner (MAPAI)', 8),
            _ph('TRAGUIN Curated Experience Note: At TRAGUIN, we redefine generic sightseeing. This exclusive package features custom perks, including premium front-row seats at renowned Light & Sound shows, a spectacular high-tea set against historic monuments, and handpicked local guides who reveal the fascinating mysteries of medieval empires.', 9),
            _ph('TRAGUIN Signature Experience: Private family high-tea overlooking the ancient Chhatris on the tranquil Betwa River bank.', 10),
            _ph('Shopping & Local Experiences: Orchha: Dokra metal crafts, miniature paintings, and terracotta pottery. Khajuraho: silver jewelry, stone miniatures, and Bundelkhandi textiles. Culinary: Mawa Bati, Rabri, and savory local snacks.', 11),
            _ph('Important: Hotel check-in 14:00 / check-out 11:00. Conservative dress at temples. Book premium rooms 60–90 days in advance for peak winter.', 12),
        ],
        moods=['Family', 'Heritage', 'Culture'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Echos of Kings & Gods: Khajuraho • Orchha Heritage Escape • 04 Nights / 05 Days',
        overview="Welcome to an unforgettable journey through time. The Best Madhya Pradesh Tour Package proudly curated by TRAGUIN invites you and your loved ones to witness an extraordinary era of royal grandeur and architectural divinity. From the legendary, intricately carved UNESCO World Heritage stone marvels of Khajuraho to the pristine, frozen-in-time riverside palaces of medieval Orchha, this signature Madhya Pradesh Family Tour blends historical storytelling with elite luxury. Immerse yourself in the scenic beauty, breathtaking landscapes, and elite heritage properties that make this a truly unique Premium Madhya Pradesh Experience.\n\nTOUR OVERVIEW\nThis customized Luxury Madhya Pradesh Holiday is meticulously planned to showcase the finest cultural aspects of Central India. Unpack your bags in ultra-comfortable, handpicked premium properties and enjoy smooth transitions in a private luxury vehicle. From evening riverside temple rituals to deep historical insights provided by local scholars, your family's comfort and engagement are guaranteed throughout this tour. Travel Month: Guest Type: October – March (Recommended) Premium Family Vacationers Vehicle: Private Luxury Innova Crysta Meal Plan: Premium Breakfast & Dinner (MAPAI) Route Map: Khajuraho (2 Nights) ➔ Orchha (2 Nights)\n\nTRAGUIN Curated Experience Note: At TRAGUIN, we redefine generic sightseeing. This exclusive package features custom perks, including premium front-row seats at renowned Light & Sound shows, a spectacular high-tea set against historic monuments, and handpicked local guides who reveal the fascinating mysteries of medieval empires. DISCOVER THE WONDERS OF KHAJURAHO & ORCHHA A vacation across Khajuraho and Orchha offers a deeply rewarding journey through the heart of Indian heritage. Recognized globally for housing some of the absolute Top Tourist Places in Madhya Pradesh, this circuit offers the perfect combination of history, peaceful nature, and family bonding. Famous Attractions: The awe-inspiring Kandariya Mahadeva Temple, the elegant Lakshmana Temple, the massive multi-tiered Jahangir Mahal in Orchha, and the royal, architectural stone Chhatris on the banks of the Betwa River. Most Searched Experiences: Attending the evening Aarti at the unique Ram Raja Temple, witnessing sunset views over the Betwa River canyon, and capturing the breathtaking geometry of Chandela dynasty sculptures. Best Family & Honeymoon Points: Romantic riverside heritage stays, exploratory nature walks through orchards, and interactive family multi-cuisine dinners reflecting real Bundelkhand flavors. Popular Instagram Locations: The turquoise-accented stone brackets of Orchha's royal corridors, the massive stone spires of the Chaturbhuj Temple, and the incredibly detailed sculptures of the Western Temple complex. Best Time to Visit Madhya Pradesh: The winter season from October to March offers cool, pleasant days, ideal for exploring sprawling monument complexes and taking stunning photographs.",
        seo_title='MP-002 | Echos of Kings & Gods | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Madhya Pradesh package (MP-002 / TG-MP-KO-05D): Khajuraho UNESCO temples, Eastern & Western groups, Raneh Falls, Orchha Chhatris, Ram Raja Temple, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Eastern Group of Temples & VIP Khajuraho Monument Sound & Light Show', 1),
            _ih('Western Group (Kandariya Mahadeva, Lakshmana, Chitragupta) & Raneh Falls Canyon', 2),
            _ih('Orchha Fort Complex, Royal Chhatris, Chaturbhuj Temple & TRAGUIN Sunset High Tea', 3),
            _ih('TRAGUIN Signature Experience: Private family high-tea overlooking the ancient Chhatris on the Betwa River bank', 4),
        ],
        days=[
            _day(
                1,
                'KHAJURAHO — ARRIVAL & THE POETRY OF SCULPTED STONE',
                ('Your extraordinary Madhya Pradesh Sightseeing journey begins as you step off your flight or train in Khajuraho. You will be warmly welcomed by your professional TRAGUIN tour manager and private chauffeur, then transferred in air-conditioned luxury to your premium resort. Enjoy a seamless check-in and relax over a refreshing gourmet lunch. In the afternoon, begin your immersion into the legendary Eastern Group of Temples, featuring beautifully preserved Hindu and Jain structures like the Parsvanatha and Adinatha temples. Your local expert will decipher the elegant inscriptions and stories carved into these stones over a thousand years ago. As dusk approaches, enjoy a Premium Khajuraho Experience with VIP seating at the famous Sound and Light Show in the Western Complex, where the history of the Chandela rulers comes alive through captivating music and lights.'),
                [
                    'Sightseeing Included: Eastern Group of Temples, Vamana and Brahma temples.',
                    'Evening Experience: VIP access to the Khajuraho Monument Sound & Light Show.',
                    'Optional Activities: An early morning therapeutic spa session or a visit to the Khajuraho Archeological Museum.',
                    'Overnight Stay: Premium Luxury Resort, Khajuraho.',
                    'Meals Included: Welcome Drink & Gourmet Buffet Dinner.',
                ],
            ),
            _day(
                2,
                'KHAJURAHO — ICONIC UNESCO MASTERPIECES & NATURAL CANYONS',
                ('Savor a luxurious morning breakfast before dedicating your day to the unmatched wonders of the UNESCO World Heritage Western Group of Temples. Walk along the manicured lawns to stand before the grand Kandariya Mahadeva Temple, an architectural model of the cosmic mountain, adorned with nearly a thousand intricately detailed sculptures. Admire the stunning craftsmanship of the Lakshmana and Vishvanatha temples, which depict ancient lifestyles, celestial music, and historic battles. In the afternoon, take a scenic drive to the breathtaking Raneh Falls. Witness an incredible 5-kilometer granite canyon displaying shimmering layers of pink, green, and grey crystalline rock—often referred to as India’s mini- Grand Canyon. Look out for local wildlife along the pristine Ken River before returning to your resort for a relaxing evening and a multi-cuisine dinner.'),
                [
                    'Sightseeing Included: Western Group (Kandariya Mahadeva, Lakshmana, Chitragupta), Raneh Falls Canyon.',
                    'Evening Experience: Leisurely walk through the local crafts village.',
                    'Optional Activities: An early morning therapeutic spa session or a visit to the Khajuraho Archeological Museum.',
                    'Overnight Stay: Premium Luxury Resort, Khajuraho.',
                    'Meals Included: Buffet Breakfast & Curated Dinner.',
                ],
            ),
            _day(
                3,
                'KHAJURAHO TO ORCHHA — JOURNEY TO THE HIDDEN MEDIEVAL OASIS',
                ('Following a relaxed breakfast, your chauffeur will guide your luxury vehicle through beautiful rural landscapes towards the medieval town of Orchha. Situated along the peaceful Betwa River, Orchha is a beautiful destination that captures the timeless spirit of old Bundelkhand. Check into your exclusive luxury riverside heritage resort, thoughtfully selected by our team. In the afternoon, begin exploring the majestic Orchha Fort Complex. Walk through the grand multi-tiered courtyards of the Jahangir Mahal, built to celebrate an imperial visit, and the Raja Mahal, famous for its beautifully vibrant religious frescoes. As the sun sets, walk to the historic Ram Raja Temple to witness the moving evening Aarti ceremony, where Lord Rama is uniquely honored as a living king with a traditional royal guard honor.'),
                [
                    'Sightseeing Included: Countryside drive, Jahangir Mahal, Raja Mahal, Rai Praveen Mahal.',
                    'Evening Experience: Guard of Honor & Aarti Ceremony at the Ram Raja Temple.',
                    'Optional Activities: A gentle evening river rafting experience or an interactive local pottery workshop.',
                    'Overnight Stay: Premium Riverside Resort, Orchha.',
                    'Meals Included: Buffet Breakfast & Traditional Bundelkhandi Dinner.',
                ],
            ),
            _day(
                4,
                'ORCHHA — RIVERSIDE CENOTAPHS & ELITE HIGH TEA',
                ("Wake up to crisp morning air and the soothing sound of the river. Today's Orchha Sightseeing highlights the deep local history and timeless architecture of the area. Visit the striking Orchha Chhatris—fourteen magnificent stone cenotaphs lined along the riverbank that serve as timeless monuments to the Bundela rulers. Your guide will walk you through the unique combination of temple and fort architecture found in these structures. Later, explore the massive Chaturbhuj Temple, built on an immense stone platform that rises high into the sky. In the afternoon, enjoy a TRAGUIN Signature Experience: a premium high-tea arranged at a private viewpoint overlooking the river and monuments. Spend your evening relaxing by your resort's pool or taking a quiet nature walk along the riverbanks."),
                [
                    'Sightseeing Included: Royal Chhatris, Chaturbhuj Temple, Laxminarayan Temple (famous for historic ceiling murals).',
                    'Evening Experience: Private TRAGUIN Sunset High Tea overlooking the historic skyline.',
                    'Optional Activities: A gentle evening river rafting experience or an interactive local pottery workshop.',
                    'Overnight Stay: Premium Riverside Resort, Orchha.',
                    'Meals Included: Buffet Breakfast, Signature High Tea, & Grand Farewell Dinner.',
                ],
            ),
            _day(
                5,
                'ORCHHA TO JHANSI / KHAJURAHO — DEPARTURE WITH LIFELONG',
                ('MEMORIES Indulge in a final breakfast at your riverside resort and soak in the serene views. Spend your morning capturing final photographs of this beautiful town or picking up unique local souvenirs. Depending on your travel preferences, your private luxury vehicle will provide a smooth transfer to the nearby Jhansi Railway Station or Khajuraho Airport for your onward journey home. Your luxury family vacation concludes here, leaving you with beautiful photos, deep cultural appreciation, and unforgettable memories crafted with care by TRAGUIN.'),
                [
                    'Sightseeing Included: Airport or Railway Station Private Departure Transfer.',
                    'Meals Included: Premium Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Radisson Jass Khajuraho | Amar Mahal Palace (Deluxe)',
                'Khajuraho | Orchha',
                '04 Nights',
                'Deluxe',
                'Deluxe Room',
                'Breakfast & Dinner',
                4,
                1,
            ),
            _hotel(
                'Ramada by Wyndham Heritage | Orchha Palace & Convention Centre',
                'Khajuraho | Orchha',
                '04 Nights',
                'Premium',
                'Premium Room',
                'Breakfast & Dinner',
                4,
                2,
            ),
            _hotel(
                'The Lalit Temple View Khajuraho | Amar Mahal (Luxury Suite)',
                'Khajuraho | Orchha',
                '04 Nights',
                'Luxury',
                'Luxury Suite',
                'Breakfast & Dinner',
                5,
                3,
            ),
            _hotel(
                'The Lalit Temple View (Executive Suite) | The Orchha Resort (Luxury Villas)',
                'Khajuraho | Orchha',
                '04 Nights',
                'Ultra Luxury',
                'Executive Suite',
                'Breakfast & Dinner',
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included('Premium Stays: 04 Nights luxury accommodation across our finest handpicked hotels and resorts.', 1),
            _inc_included('Gourmet Dining: Daily buffet breakfast and chef-curated dinners at all properties.', 2),
            _inc_included('Luxury Transportation: Private air-conditioned luxury vehicle (Toyota Innova Crysta) for all transfers, sightseeing, and intercity travel as outlined.', 3),
            _inc_included('Elite Guiding: Private services of local, government-approved master historians in Khajuraho and Orchha.', 4),
            _inc_included('TRAGUIN Signatures: Complimentary riverside high-tea and prime front-row tickets to the Light & Sound show.', 5),
            _inc_included('Welcome Amenities: Royal traditional welcome at hotels, fresh mineral water bottles provided daily in the vehicle, and custom travel kits.', 6),
            _inc_included('TRAGUIN Support: 24/7 dedicated concierge support from our core destination experts, including all toll fees, parking, and driver allowances.', 7),
            _inc_excluded('Flights / Trains: Any domestic or international airfares or main train tickets to/from the destination.', 8),
            _inc_excluded('Monument Entry Tickets: General entrance fees, camera fees, or video charges at monuments unless specifically requested.', 9),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, alcoholic beverages, spa therapies, and tipping for drivers or guides.', 10),
            _inc_excluded('Optional Activities: River rafting charges, specialized pottery workshops, or extra items not listed in inclusions.', 11),
            _inc_excluded('Insurance: Personal travel and medical insurance policies.', 12),
        ],
    )
    return package, itinerary

def build_mp_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MP-003'
    tour_code = 'TG-MPWL-2026'
    title = 'The Royal Bengal Tiger Wilderness: Bandhavgarh Safari'
    duration = '03 Nights / 04 Days'
    slug = 'mp-003-royal-bengal-tiger-wilderness-bandhavgarh-safari'
    itin_slug = 'mp-003-royal-bengal-tiger-wilderness-bandhavgarh-safari-itinerary'
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
            _ph('Serial code MP-003 | TRAGUIN tour code TG-MPWL-2026', 1),
            _ph('State / Country: Madhya Pradesh, India | Category: Premium Wildlife Tour', 2),
            _ph('Destinations: Bandhavgarh National Park', 3),
            _ph('Ideal for: Families, Wildlife Photographers, Luxury Seekers', 4),
            _ph('Best season: October to June (Peak Tiger Sightings: Nov-May)', 5),
            _ph('Starting price: On Request (Premium Ultra-Luxury)', 6),
            _ph('Route: Jabalpur / Khajuraho Arrival ➔ Bandhavgarh National Park (3N) ➔ Departure', 7),
            _ph('Vehicle / Meals: Luxury AC SUV for Transfers + Open 4x4 Gypsy for Safaris | All Meals Included (Jungle AP Plan)', 8),
            _ph('TRAGUIN Curated Experience Note: At TRAGUIN, we understand that a truly exceptional safari extends far beyond the drive. Our customized inclusions feature premium bush breakfasts in hidden forest zones, interactive evening presentations with seasoned tiger conservationists, and luxury stargazing sessions around a private campfire.', 9),
            _ph('TRAGUIN Signature Experience: Private bush breakfast setup deep inside the jungle zone during a high-excitement morning safari tracking.', 10),
            _ph('Shopping & Local Experiences: Tala Village: hand-carved wooden tiger sculptures and Gond/Baiga tribal paintings. Lodge organic dining with farm-to-table Bundelkhandi cuisine.', 11),
            _ph('Important: Safari permits open 120 days in advance. Carry original government ID used for permit registration. Wear neutral earthy colors. Core zones closed Wednesday afternoons.', 12),
        ],
        moods=['Wildlife', 'Family', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='The Royal Bengal Tiger Wilderness: Bandhavgarh Safari • 03 Nights / 04 Days',
        overview='Welcome to the untamed heart of Central India. The Best Madhya Pradesh Tour Package for wildlife lovers, curated meticulously by TRAGUIN, invites your family into the legendary realms of Bandhavgarh. Boasting the highest density of Royal Bengal Tigers in the world, this Luxury Madhya Pradesh Holiday seamlessly pairs high-adrenaline 4x4 open-jeep safaris with ultra-luxury forest lodges. Bask in the scenic beauty of ancient rocky cliffs and sprawling meadows while building unforgettable memories on an elite, fully guided wildlife retreat designed uniquely for your family.\n\nTOUR OVERVIEW\nThis premium Madhya Pradesh Family Tour focuses deeply on the world-renowned Bandhavgarh Safari experience. Traveling to the ancient Vindhyan hills, your family will explore deep sal forests and historic landscapes steeped in wildlife lore. This curated FIT package provides seamless private airport transfers, premium handpicked luxury stays, and exclusive pre-booked jungle safaris accompanied by top-tier naturalists. Travel Dates: Flexible / Custom FIT Calendar Group Type: Private Family Vacation Vehicle: Luxury AC SUV for Transfers + Open 4x4 Gypsy for Safaris Meal Plan: All Meals Included (Jungle AP Plan) Route Plan: Jabalpur / Khajuraho Arrival ➔ Bandhavgarh National Park (3N) ➔ Departure\n\nWHY VISIT BANDHAVGARH — TOP TOURIST PLACES IN MADHYA\nPRADESH Bandhavgarh National Park is a premier crown jewel of Indian wilderness, widely searched for its high-density tiger populations and ancient heritage. A custom Madhya Pradesh Sightseeing expedition here offers unique historical and wilderness landscapes: Famous Attractions: Track tigers across pristine zones (Tala, Magadhi, Khitauli), view the ancient 2000-year-old Bandhavgarh Fort perched on a massive cliff, and marvel at the majestic 10th-century reclining sandstone statue of Lord Vishnu (Shesh Shaiya). Most Searched Experiences: Catching a close-up glimpse of a tiger walking down a forest track, exploring misty grasslands at sunrise, and enjoying luxury evening sundowners overlooking wild buffers. Best Family & Luxury Highlights: Multi-bedroom luxury private villas with plunge pools, custom educational junior naturalist programs for kids, and sublime open-air dinners under a canopy of stars. Popular Instagram Locations: The dramatic fort cliff viewpoint against the sunset, the ancient stone gateway of Tala zone, and the beautifully stylized luxury machans of handpicked lodges. Best Time to Visit Madhya Pradesh Wildlife: While the park opens from October to June, the crisp winter months (November to February) offer lush scenic beauty, whereas the warmer months (March to May) provide the highest visibility of tigers near forest watering holes.\n\nTRAGUIN Curated Experience Note: At TRAGUIN, we understand that a truly exceptional safari extends far beyond the drive. Our customized inclusions feature premium bush breakfasts in hidden forest zones, interactive evening presentations with seasoned tiger conservationists, and luxury stargazing sessions around a private campfire.',
        seo_title='MP-003 | The Royal Bengal Tiger Wilderness | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Madhya Pradesh package (MP-003 / TG-MPWL-2026): Bandhavgarh Tala/Magadhi/Khitauli safaris, Shesh Shaiya, bush breakfast, sundowner, and 4-tier jungle lodge accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Scenic countryside drive, lodge orientation & private campfire dining with wildlife film screening', 1),
            _ih('Core Jungle Safaris (Morning & Afternoon), tiger tracking & Baiga tribal folk dance performance', 2),
            _ih('Khitauli Safari Track, Shesh Shaiya Monument, Charanganga River Source & premium sundowner', 3),
            _ih('TRAGUIN Signature Experience: Private bush breakfast setup deep inside the jungle zone during morning safari tracking', 4),
        ],
        days=[
            _day(
                1,
                'ARRIVAL & TRANSITION INTO THE ROYAL WILDERNESS',
                ("Your extraordinary Premium Madhya Pradesh Experience begins with a warm greeting at Jabalpur Airport or Umaria Railway Station by your dedicated TRAGUIN representative. Relax inside your private luxury AC vehicle as you enjoy a scenic chauffeur-driven drive through quaint central Indian villages and stretching paddy fields toward Bandhavgarh. Upon arrival, enjoy a traditional royal welcome at your ultra-luxury wilderness lodge. Check into your private cottage and absorb the peaceful ambiance of the surrounding forest buffer. After a sumptuous lunch crafted from fresh organic ingredients, join your expert resident naturalist for an informative orientation session. Learn about the park's diverse topography, tiger lineages, and safety protocols. Spend your evening relaxing on your private deck, enjoying a gourmet dinner around a cozy open-air campfire under the starlit sky."),
                [
                    'Sightseeing Included: Scenic countryside drive, orientation walk around the estate buffer.',
                    'Evening Experience: Private campfire dining accompanied by an interactive wildlife film screening.',
                    'Overnight Stay: Premium Handpicked Luxury Jungle Lodge, Bandhavgarh.',
                    'Meals Included: Curated Lunch & Multi-course Fine Dining Gourmet Dinner.',
                ],
            ),
            _day(
                2,
                'BANDHAVGARH — MORNING & AFTERNOON DEEP JUNGLE SAFARIS',
                ("Wake up before dawn to the crisp morning air and calls of the wild. After a quick serving of freshly brewed coffee and premium cookies, board your private 4x4 open safari Gypsy. Enter the legendary Tala Zone—the historic heart of tiger country. Experience the thrilling adrenaline rush as your master tracker deciphers fresh pugmarks, frantic langur alarm calls, and deer warning barks. As the golden morning sun pierces the morning mist, enjoy an exclusive TRAGUIN bush breakfast laid out on the bonnet of your safari vehicle in a designated forest clearing. Keep an eye out for leopards, sloth bears, wild boars, and spectacular birdlife. Return to the lodge for a midday swim in the pool and a lavish lunch. In the afternoon, return to the jungle via the Magadhi Zone, exploring massive grassland meadows and tracking the territory of the park's current dominant tigers. Return to your lodge at dusk for a relaxing evening, capped with an authentic tribal dance performance by local villagers."),
                [
                    'Sightseeing Included: Core Jungle Safaris (Morning & Afternoon drives), tracking tigers, checking ancient lookout towers.',
                    'Evening Experience: Traditional Baiga tribal folk dance performance followed by a premium multi-cuisine buffet.',
                    'Overnight Stay: Premium Handpicked Luxury Jungle Lodge, Bandhavgarh.',
                    'Meals Included: Early Morning Coffee, Forest Bush Breakfast, Gourmet Lunch, & Dinner.',
                ],
            ),
            _day(
                3,
                'BANDHAVGARH — TRACKING TIGERS & THE ANCIENT HERITAGE TRAIL',
                ("Another morning brings a fresh opportunity for unparalleled wildlife viewing. Today your Bandhavgarh Safari ventures into the Khitauli Zone, a gorgeous forest strip known for its rich biodiversity, regular sloth bear sightings, and beautiful bamboo thickets. Marvel at the stunning breathtaking landscapes as your naturalist points out unique avian species like the Malabar Pied Hornbill and Asian Paradise Flycatcher. After lunch at the lodge, head out for your afternoon safari focused on the intersection of nature and history. Pay homage at the awe-inspiring Shesh Shaiya, a hidden 35-foot-long monolithic stone statue of Lord Vishnu reclining on a seven-hooded serpent, dating back to the 10th century. Bubbling natural springs originate here, providing vital water to the park's wildlife. End your evening on a stunning cliff plateau edge, enjoying an exclusive luxury sundowner setup with premium snacks as the setting sun paints the Vindhyan cliffs in shades of deep crimson."),
                [
                    'Sightseeing Included: Khitauli Safari Track, Shesh Shaiya Monument, Charanganga River Source.',
                    'Evening Experience: Premium Sundowner with signature appetizers at a scenic forest-view point.',
                    'Overnight Stay: Premium Handpicked Luxury Jungle Lodge, Bandhavgarh.',
                    'Meals Included: Full Breakfast, Gourmet Lunch, & Festive Farewell Dinner.',
                ],
            ),
            _day(
                4,
                'FINAL WILDERNESS MORNING & SEAMLESS ONWARD DEPARTURE',
                ('On your final morning, enjoy a relaxed, late-riser breakfast on the open veranda of your luxury resort, taking in your last views of the lush canopy. Alternatively, opt for an early morning village walk to interact with the warm local communities and learn about sustainable lifestyle co-existence on the jungle fringes. Pack your bags filled with incredible wildlife photographs, safari souvenirs, and unforgettable memories. Check out from the lodge, where your private chauffeur awaits to provide a seamless transfer back to Jabalpur Airport or your preferred railway station for your onward flight home. Your elite TRAGUIN Destination Package experience concludes flawlessly.'),
                [
                    'Sightseeing Included: Buffer village eco-walk (optional), private airport transfer line.',
                    'Meals Included: Premium Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Bandhav Vilas / Nature Heritage Resort',
                'Bandhavgarh',
                '03 Nights',
                'Deluxe',
                'Luxury Villa / Premium Cottage',
                'All Meals (Breakfast, Lunch, Dinner)',
                4,
                1,
            ),
            _hotel(
                'Kings Lodge (Pugdundee Safaris)',
                'Bandhavgarh',
                '03 Nights',
                'Premium',
                'Luxury Forest Cottage',
                'All Meals (Breakfast, Lunch, Dinner)',
                4,
                2,
            ),
            _hotel(
                'Samode Safari Lodge / Tree House Hideaway',
                'Bandhavgarh',
                '03 Nights',
                'Luxury',
                'Ultra-Luxury Villa / Premium Treehouse',
                'All Meals + Select Soft Beverages',
                5,
                3,
            ),
            _hotel(
                'Mahua Kothi (Taj Safaris)',
                'Bandhavgarh',
                '03 Nights',
                'Ultra Luxury',
                'Elite Luxury Kuthiya (Private Suite)',
                'All Luxury Meals + Premium Inclusions',
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included('Premium Stays: 03 Nights accommodation at handpicked luxury jungle lodges with immersive forest backdrops.', 1),
            _inc_included('Gourmet Dining: All daily meals (Buffet/A-la-carte breakfast, lunch, and fine-dining dinners) included at the lodges.', 2),
            _inc_included('Exclusive Safaris: 03 private open-jeep 4x4 Gypsy safaris into core zones with pre-booked permits.', 3),
            _inc_included('Expert Naturalists: Services of highly experienced, English-speaking forest guides and resident lodge naturalists.', 4),
            _inc_included('Luxury Transportation: Private air-conditioned luxury SUV for jabalpur/rail transfers and airport connectivity.', 5),
            _inc_included('TRAGUIN Signatures: One complimentary premium Bush Breakfast on a vehicle bonnet and a signature sunset sundowner event.', 6),
            _inc_included('Welcome Amenities: Royal traditional arrival welcome, customized eco-friendly travel kits, and premium mineral water replenished daily.', 7),
            _inc_included('Complete Assistance: 24/7 real-time concierge support from TRAGUIN destination operations, including driver allowances, toll fees, and park entry taxes.', 8),
            _inc_excluded('Airfare / Rail: Main commercial flights or interstate train tickets to arrival nodes.', 9),
            _inc_excluded('Camera Charges: Any special professional video or lenses fees imposed by the forest department.', 10),
            _inc_excluded('Personal Expenses: Laundry, premium spa massage sessions, alcoholic beverages, and tipping tips for safari drivers or lodge staff.', 11),
            _inc_excluded('Insurance: Personal medical insurance and trip cancellation coverage.', 12),
        ],
    )
    return package, itinerary

def build_mp_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MP-004'
    tour_code = 'TG-MP-KANHA-004'
    title = 'The Ultimate Wilderness Escape • Kanha National Park'
    duration = '04 Nights / 05 Days'
    slug = 'mp-004-ultimate-wilderness-escape-kanha-national-park'
    itin_slug = 'mp-004-ultimate-wilderness-escape-kanha-national-park-itinerary'
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
            _ph('Serial code MP-004 | TRAGUIN tour code TG-MP-KANHA-004', 1),
            _ph('State / Country: Madhya Pradesh, India | Category: Premium Wildlife Tour', 2),
            _ph('Destinations: Kanha National Park & Tiger Reserve', 3),
            _ph('Ideal for: Wildlife Enthusiasts, Families, Photographers', 4),
            _ph('Best season: October to May (Peak sightings Mar-May)', 5),
            _ph('Starting price: On Request (Premium Luxury Tier)', 6),
            _ph('Route: Jabalpur / Nagpur ➔ Kanha National Park (4N) ➔ Departure Hub', 7),
            _ph('Vehicle / Meals: Luxury AC Transfer Vehicle & Private 4x4 Open Jeep | All Meals Included (Jungle American Plan)', 8),
            _ph('TRAGUIN Curated Experience Note: At TRAGUIN, we redefine the classic safari. Our signatures on this Luxury Madhya Pradesh Holiday include handpicked naturalist guides with elite tracking skills, private bush dinner setups under the stars, customized early morning breakfast hampers for your game drives, and carefully vetted premium stays that practice world-class eco-luxury.', 9),
            _ph('TRAGUIN Signature Experience: Private family bush dinner with authentic live Baiga tribal dances under the open jungle sky.', 10),
            _ph('Shopping & Local Experiences: Authentic Gond paintings, handmade wooden toys, organic forest honey, and hand-woven tribal textiles at local weekly markets.', 11),
            _ph('Important: Safari permits open 120 days in advance. Carry original ID used for booking. Wear muted forest colors. Park closed every Wednesday afternoon.', 12),
        ],
        moods=['Wildlife', 'Family', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='The Ultimate Wilderness Escape • Kanha National Park • 04 Nights / 05 Days',
        overview='Welcome to the raw, untamed heart of the Indian wilderness. The Best Madhya Pradesh Tour Package for wildlife lovers, meticulously crafted by TRAGUIN, invites your family into the legendary forests that inspired Rudyard Kipling’s classic, *The Jungle Book*. This ultra-exclusive Kanha Wildlife Tour is designed for discerning travelers seeking an authentic combination of high-end luxury, thrilling open-jeep safaris, and deep natural immersion. Across breathtaking landscapes, expansive sal forests, and lush meadows, experience a Premium Madhya Pradesh Experience tailored to create unforgettable memories.\n\nTOUR OVERVIEW\nThis bespoke Madhya Pradesh Wildlife Tour offers a deep exploration of Kanha National Park, widely acclaimed as one of the finest managed wildlife sanctuaries in Asia. Renowned for its significant Royal Bengal Tiger population and as the exclusive home of the rare Southern Swamp Deer (Barasingha), Kanha promises unmatched biodiversity. Your private journey includes 4x4 open-jeep safaris into exclusive park zones, stay at premium luxury wildlife lodges, gourmet meals, and dedicated naturalist services. Travel Dates: Flexible / Custom FIT Group Type: Private Family / Wildlife FIT Vehicle: Luxury AC Transfer Vehicle & Private 4x4 Open Jeep Meal Plan: All Meals Included (Jungle American Plan) Route Plan: Jabalpur / Nagpur ➔ Kanha National Park (4N) ➔ Departure Hub\n\nWHY VISIT KANHA NATIONAL PARK?\nKanha Tiger Reserve stands as a jewel among the Top Tourist Places in Madhya Pradesh. It offers families and wildlife photographers an immersive getaway far from the clutter of urban life, blending high-octane adventure with deep natural serenity. Famous Attractions: The vast meadows of Kanha Zone, the high-altitude viewpoint of Bamni Dadar (Sunset Point), the state-of-the-art Kanha Museum, and the core zones of Mukki, Kisli, and Sarhi. Most Searched Experiences: Catching a glimpse of the Royal Bengal Tiger stalking through elephant grass, witnessing the iconic hard-ground Barasingha in its natural habitat, and taking early morning drives through mist-shrouded sal forests. Best Honeymoon/Family/Luxury Points: Secluded luxury jungle villas equipped with private plunge pools, intimate evening bonfires featuring local tribal dances, and specialized educational nature trails designed for children. Popular Instagram Locations: Shravan Talok in the early morning light, the towering canopy of ghost trees (Kulu), and spectacular frames of tigers wading through forest watering holes. Best Time to Visit Madhya Pradesh (Wildlife Focus): While the park opens from mid-October to June, the winter months (November to February) offer comfortable weather and stunning misty landscapes, whereas spring (March to May) guarantees the highest probability of tiger sightings near water bodies.\n\nTRAGUIN Curated Experience Note: At TRAGUIN, we redefine the classic safari. Our signatures on this Luxury Madhya Pradesh Holiday include handpicked naturalist guides with elite tracking skills, private bush dinner setups under the stars, customized early morning breakfast hampers for your game drives, and carefully vetted premium stays that practice world-class eco-luxury.',
        seo_title='MP-004 | The Ultimate Wilderness Escape • Kanha National Park | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Madhya Pradesh package (MP-004 / TG-MP-KANHA-004): Kanha core zone safaris, Barasingha tracking, Bamni Dadar sunset, tribal village tour, bush dinner, and 4-tier jungle lodge accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Scenic drive to Kanha, nature walk, wildlife expert presentation & premium bonfire dinner', 1),
            _ih('Morning and Afternoon Core Zone 4x4 Safaris across Kanha Meadows with TRAGUIN picnic breakfast', 2),
            _ih('Barasingha tracking, Bamni Dadar Sunset Point & private signature bush dinner with Baiga tribal dance', 3),
            _ih('Guided buffer zone walk, tribal village cultural tour, Kanha Museum & TRAGUIN bush dinner signature', 4),
        ],
        days=[
            _day(
                1,
                'ARRIVAL & GATEWAY TO THE WILDERNESS',
                ('Your extraordinary Kanha Wildlife Tour begins as you arrive at Jabalpur Airport or Nagpur Airport. You will be warmly greeted by a representative from TRAGUIN and your private chauffeur. Embark on a highly comfortable, scenic drive through charming rural landscapes and dense forest fringes towards Kanha National Park. Upon reaching your ultra-luxury jungle lodge, experience a traditional welcome followed by a smooth check-in. Settle into your premium cottage and enjoy a fresh gourmet lunch. The afternoon is yours to relax and absorb the tranquility of the forest. In the evening, attend an insightful orientation and interactive presentation led by the lodge’s resident naturalist, introducing you to the complex ecosystem of Kanha. Gather around a crackling bonfire for an exquisite multi-course dinner.'),
                [
                    'Sightseeing Included: Scenic drive to Kanha, nature walk within the lodge grounds.',
                    'Evening Experience: Presentation by a wildlife expert and a premium bonfire dinner.',
                    'Overnight Stay: Premium Luxury Jungle Lodge, Kanha.',
                    'Meals Included: Lunch & Gourmet Dinner.',
                ],
            ),
            _day(
                2,
                'IMMERSIVE MORNING & AFTERNOON 4X4 GAME DRIVES',
                ('Wake up before dawn to the call of the wild. Enjoy fresh coffee and cookies before boarding your exclusive 4x4 open safari vehicle for your first morning of Kanha Sightseeing deep in the core zone. As the morning mist lifts over the vast grassy meadows, listen closely for langur and spotted deer alarm calls indicating a predator is on the move. Your expert tracker will navigate the tracks to locate the majestic Royal Bengal Tiger. During the drive, indulge in a curated TRAGUIN picnic breakfast served at a designated camp inside the reserve. Return to the lodge by mid-morning to relax by the pool. Following an early afternoon lunch, head back into a different zone of the national park for your afternoon safari. Watch for leopards, wild dogs (Dholes), Indian bison (Gaur), and sloth bears. Return as dusk falls to enjoy a relaxed evening sharing safari stories over drinks.'),
                [
                    'Sightseeing Included: Morning and Afternoon Core Zone 4x4 Safaris, Kanha Meadows.',
                    'Evening Experience: Star-gazing session from your private deck.',
                    'Overnight Stay: Premium Luxury Jungle Lodge, Kanha.',
                    'Meals Included: Early Breakfast, Mid-day Lunch, & Dinner.',
                ],
            ),
            _day(
                3,
                'DEEP TRACKING & THE LEGENDARY BAMNI DADAR SUNSET',
                ('Dedicate another exhilarating day to exploring the vast horizons of Kanha Tiger Reserve. Your morning safari focuses on tracking the elusive hard-ground Barasingha, an inspiring conservation success story unique to this park. Photograph these magnificent deer as they graze gracefully in the marshy wetlands. After a luxurious lunch back at your lodge, your afternoon safari takes you towards Bamni Dadar, the highest plateau in the park. Known popularly as Sunset Point, it offers a stunning panoramic view of the valley below. Watch grazing herbivores against the backdrop of a spectacular African-style sunset. Return to the resort for an exclusive experience: a signature bush dinner organized by TRAGUIN, featuring live traditional Baiga tribal music and local delicacies under a canopy of stars.'),
                [
                    'Sightseeing Included: Morning Safari, Afternoon Safari to Bamni Dadar Plateau.',
                    'Evening Experience: Private Signature Bush Dinner with Baiga Tribal dance performance.',
                    'Optional Activities: Luxury Ayurvedic massage or a private cooking class featuring Bundelkhandi cuisine.',
                    'Overnight Stay: Premium Luxury Jungle Lodge, Kanha.',
                    'Meals Included: Breakfast, Lunch, & Grand Signature Dinner.',
                ],
            ),
            _day(
                4,
                'NATURE TRAILS, LOCAL CULTURE & BIRDWATCHING',
                ('Today offers a beautifully curated change of pace. Following a relaxed breakfast at the lodge, embark on an immersive guided nature walk along the buffer zone riverbeds. Accompanied by a trained tribal naturalist, learn about medicinal plants, track insect life, and spot some of Kanha’s 300+ bird species, including the Malabar Pied Hornbill and the Asian Paradise Flycatcher. In the afternoon, enjoy a cultural visit to a nearby traditional Baiga and Gond tribal village. This offers an educational experience for families, showing how local communities live in harmony with the surrounding wildlife. Return to the lodge to spend your final evening at leisure, perhaps treating yourself to a signature spa treatment or relaxing with a book on the lodge’s viewing deck.'),
                [
                    'Sightseeing Included: Guided Buffer Zone Walk, Tribal Village Cultural Tour, Kanha Museum visit.',
                    'Optional Activities: Luxury Ayurvedic massage or a private cooking class featuring Bundelkhandi cuisine.',
                    'Overnight Stay: Premium Luxury Jungle Lodge, Kanha.',
                    'Meals Included: Breakfast, Lunch, & Dinner.',
                ],
            ),
            _day(
                5,
                'FINAL SUNRISE & DEPARTURE WITH LASTING MEMORIES',
                ('On your final morning, wake up to the peaceful symphony of the forest. Enjoy a leisurely breakfast on the veranda overlooking the buffer woodlands. Take a final stroll through the resort grounds to capture some last photographs of your luxury jungle getaway. Check out from your lodge, where your private luxury vehicle awaits. Sit back and relax as your chauffeur transfers you smoothly back to Jabalpur or Nagpur Airport for your flight home. Your premium safari journey concludes, leaving you with exceptional photographs and beautiful memories crafted by TRAGUIN.'),
                [
                    'Sightseeing Included: Airport / Railway Station private departure transfer.',
                    'Meals Included: Premium Buffet Breakfast. HANDPICKED PREMIUM & LUXURY ACCOMMODATIONS Our accommodation options are hand-selected to elevate your safari experience. We partner exclusively with premium properties that guarantee top-tier luxury, superior family safety, and sustainable eco-tourism practices. Category Resort Name (Kanha — 4 Nights) Room Type Meal Plan OPTION 01 – DELUXE Singinawa Jungle Lodge / Tuli Tiger Resort Luxury Cottage / Luxury Lounge Cabin All Meals Included OPTION 02 – PREMIUM Chitvan Jungle Lodge / Kanha Earth Lodge Jal Suite / Luxury Eco- Lodge Villa All Meals Included OPTION 03 – LUXURY Shergarh Tented Camp / Pugdundee Kanha Earth Lodge Luxury Safari Tent / Deluxe Forest Bungalow All Meals Included OPTION 04 – ULTRA LUXURY Banjaar Tola (A Taj Safari Lodge) Ultra-Luxury Tented Suite (Private Deck) All Luxury Meals & Drinks PACKAGE INCLUSIONS ✔Premium Stays: 04 Nights luxury accommodation at top-rated jungle lodges. ✔Gourmet Dining: All meals included daily (Breakfast, Lunch, High Tea, and Dinners) during your stay. ✔Private Safaris: 4x4 open-jeep safaris into core zones with mandatory guide fees and route permits included. ✔Luxury Transportation: Private air-conditioned luxury vehicle for airport transfers and intercity travel. ✔TRAGUIN Signatures: Custom early morning breakfast hampers for safaris and a private signature bush dinner under the stars. ✔Welcome Amenities: Refres',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Singinawa Jungle Lodge / Tuli Tiger Resort',
                'Kanha',
                '04 Nights',
                'Deluxe',
                'Luxury Cottage / Luxury Lounge Cabin',
                'All Meals Included',
                4,
                1,
            ),
            _hotel(
                'Chitvan Jungle Lodge / Kanha Earth Lodge',
                'Kanha',
                '04 Nights',
                'Premium',
                'Jal Suite / Luxury Eco-Lodge Villa',
                'All Meals Included',
                4,
                2,
            ),
            _hotel(
                'Shergarh Tented Camp / Pugdundee Kanha Earth Lodge',
                'Kanha',
                '04 Nights',
                'Luxury',
                'Luxury Safari Tent / Deluxe Forest Bungalow',
                'All Meals Included',
                5,
                3,
            ),
            _hotel(
                'Banjaar Tola (A Taj Safari Lodge)',
                'Kanha',
                '04 Nights',
                'Ultra Luxury',
                'Ultra-Luxury Tented Suite (Private Deck)',
                'All Luxury Meals & Drinks',
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included('Premium Stays: 04 Nights luxury accommodation at top-rated jungle lodges.', 1),
            _inc_included('Gourmet Dining: All meals included daily (Breakfast, Lunch, High Tea, and Dinners) during your stay.', 2),
            _inc_included('Private Safaris: 4x4 open-jeep safaris into core zones with mandatory guide fees and route permits included.', 3),
            _inc_included('Luxury Transportation: Private air-conditioned luxury vehicle for airport transfers and intercity travel.', 4),
            _inc_included('TRAGUIN Signatures: Custom early morning breakfast hampers for safaris and a private signature bush dinner under the stars.', 5),
            _inc_included('Welcome Amenities: Refreshing welcome drink upon arrival, daily premium bottled water during safaris, and custom travel kits.', 6),
            _inc_included('Assistance & Taxes: 24/7 dedicated concierge support from TRAGUIN experts, fuel costs, toll taxes, parking fees, and driver allowances.', 7),
            _inc_excluded('Airfare / Rail: Domestic or international flights, or train tickets to Jabalpur/Nagpur.', 8),
            _inc_excluded('Camera Fees: Professional video camera or lens fees imposed by the forest department, if applicable.', 9),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, alcoholic beverages, spa treatments, and tips.', 10),
            _inc_excluded('Optional Activities: Extra safaris, night patrols, or items not specifically detailed in the itinerary.', 11),
            _inc_excluded('Insurance: Comprehensive travel and medical insurance.', 12),
        ],
    )
    return package, itinerary

def build_mp_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MP-005'
    tour_code = 'TG-MPMS-2026'
    title = 'Mahakaleshwar Special Spiritual Trail: Ujjain • Omkareshwar • Indore'
    duration = '03 Nights / 04 Days'
    slug = 'mp-005-mahakaleshwar-special-spiritual-trail-ujjain-omkareshwar-indore'
    itin_slug = 'mp-005-mahakaleshwar-special-spiritual-trail-ujjain-omkareshwar-indore-itinerary'
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
            _ph('Serial code MP-005 | TRAGUIN tour code TG-MPMS-2026', 1),
            _ph('State / Country: Madhya Pradesh, India | Category: Premium Pilgrimage Tour', 2),
            _ph('Destinations: Ujjain • Omkareshwar • Indore', 3),
            _ph('Ideal for: Families, Spiritual Seekers & Elders', 4),
            _ph('Best season: July to March (Pleasant Weather)', 5),
            _ph('Starting price: On Request (Premium Luxury Tier)', 6),
            _ph('Route: Indore Airport ➔ Ujjain (2N) ➔ Omkareshwar ➔ Indore (1N) ➔ Departure', 7),
            _ph('Vehicle / Meals: Luxury Toyota Innova Crysta / Luxury Coach | Premium Breakfast & Dinner (MAPAI)', 8),
            _ph('TRAGUIN Curated Experience Note: At TRAGUIN, we understand that spiritual travel requires effortless coordination, especially when traveling with elders or children. Our standard of luxury includes pre-arranged VIP Darshan accesses, an exclusive private boat cruise at sunset on the holy Narmada River, and expert destination guides who bring the rich mythological history of the Malwa region vibrantly alive.', 9),
            _ph('TRAGUIN Signature Experience: Private family boat ride on the Narmada River with priority access assistance to the island shrine.', 10),
            _ph('Shopping & Local Experiences: Chappan Dukan and Sarafa Bazaar street food in Indore; Bhairavgarh print sarees in Ujjain; Maheshwari & Chanderi sarees at government emporiums.', 11),
            _ph('Important: Bhasma Aarti registration opens 30–60 days in advance—share guest IDs early. Traditional dress for inner sanctum rituals. Hotel check-in 14:00 hrs.', 12),
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
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Mahakaleshwar Special Spiritual Trail: Ujjain • Omkareshwar • Indore • 03 Nights / 04 Days',
        overview="Welcome to the sacred heart of Central India. The Best Madhya Pradesh Tour Package proudly customized by TRAGUIN invites your family to discover an evocative journey of ultimate devotion, royal heritage, and soulful tranquility. Centered around the omnipotent energy of two divine Jyotirlingas, this bespoke Madhya Pradesh Pilgrimage Tour brings you face to face with timeless Vedic history while ensuring unmatched premium comfort. Let us envelope you in an elite luxury proposal where expert storytelling, smooth VIP protocols, and breathtaking landscapes create unforgettable memories for you and your loved ones.\n\nTOUR OVERVIEW\nThis premium Madhya Pradesh Family Tour is an intensively detailed, spiritually uplifting itinerary structured across the highly revered holy axis of Central India. Traveling from the historical and astronomical epicentre of Ujjain on the banks of the Shipra River to the island-om temple of Omkareshwar on the Narmada River, and concluding in the culinary kingdom of Indore, every parameter is elegantly tailored. Enjoy completely private airport transfers, premium handpicked hotels, executive vehicle charters, and highly privileged temple assistance. Travel Dates: Flexible / Custom FIT Calendar Group Type: Private Family Pilgrimage Vehicle: Luxury Toyota Innova Crysta / Luxury Coach Meal Plan: Premium Breakfast & Dinner (MAPAI) Route Plan: Indore Airport ➔ Ujjain (2N) ➔ Omkareshwar ➔ Indore (1N) ➔ Departure\n\nWHY CHOOSE THE PREMIUM MAHAKALESHWAR SPECIAL\nSPIRITUAL TRAIL? Embodying ancient scriptural resonance, a journey through the sacred sites of Madhya Pradesh offers an unmatched sensory and emotional getaway. Known globally for hosting some of the most sought- after Top Tourist Places in Madhya Pradesh, this path provides total mental rejuvenation and profound spiritual alignment. Famous Attractions: Witness the majestic Mahakaleshwar Jyotirlinga Temple, the sprawling Mahakal Lok Corridor, the island sanctuary of Omkareshwar Jyotirlinga, the legendary Harsiddhi Shaktipeeth, Kaal Bhairav, and Indore’s iconic Rajwada Palace. Most Searched Experiences: Attending the breathtaking early morning Bhasma Aarti inside Mahakaleshwar, participating in the divine evening Narmada Maha Aarti, and treating your palate to India's most famous street-food market at Chappan Dukan. Premium Family Points: Senior-citizen friendly slow-paced temple walks, seamless wheel-chair assistance availability, customized pure vegetarian premium dining, and grand architectural corridors tailored for comfortable multi-generational family bonding. Popular Instagram Locations: The grand illuminated sculptures and fountains of the Sri Mahakal Lok, the dramatic suspended footbridge across the churning Narmada at Omkareshwar, and the beautiful royal stepwells of the historic region. Best Time to Visit Madhya Pradesh: The refreshing post-monsoon and crisp winter months from July to March provide delightful temperatures, ideal for peaceful Madhya Pradesh Sightseeing, river rituals, and heritage walks. • • • • • YOUR CUSTOM HANDCRAFTED ITINERARY\n\nTRAGUIN Curated Experience Note: At TRAGUIN, we understand that spiritual travel requires effortless coordination, especially when traveling with elders or children. Our standard of luxury includes pre-arranged VIP Darshan accesses, an exclusive private boat cruise at sunset on the holy Narmada River, and expert destination guides who bring the rich mythological history of the Malwa region vibrantly alive.",
        seo_title='MP-005 | Mahakaleshwar Special Spiritual Trail | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Madhya Pradesh package (MP-005 / TG-MPMS-2026): Mahakaleshwar Bhasma Aarti, Mahakal Lok, Omkareshwar boat cruise, Chappan Dukan, Rajwada Palace, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Harsiddhi Temple, Shri Mahakal Lok Corridor & grand oil-lamp tower lighting ritual', 1),
            _ih('Mahakaleshwar Bhasma Aarti, Kaal Bhairav, Sandipani Ashram, Mangalnath & Ram Ghat', 2),
            _ih('Private Narmada River boat cruise, Omkareshwar & Mamleshwar Temples & Chappan Dukan culinary walk', 3),
            _ih('Rajwada Palace, Kanch Ka Mandir & smooth departure transfer from Indore', 4),
        ],
        days=[
            _day(
                1,
                'INDORE TO UJJAIN — ARRIVAL & IMMERSIVE JOURNEY INTO',
                ("MAHAKAL LOK Your extraordinary Luxury Madhya Pradesh Holiday begins with a warm traditional greeting at the Indore Airport or Railway Station by your elite TRAGUIN tour manager and private chauffeur. Board your luxury vehicle and enjoy a smooth, highly scenic drive to the timeless city of Ujjain, one of India's most sacred Kumbh Mela destinations. Upon arrival, enjoy a seamless check-in at your handpicked premium hotel. After fresh refreshments, begin your premium Ujjain Sightseeing exploration. Your first destination is the awe-inspiring Harsiddhi Temple, a powerful ancient Shaktipeeth where the elbow of Goddess Sati is believed to have fallen. Witness the dramatic evening lighting ceremony of two massive 15- foot iron lamp towers holding hundreds of oil lamps. Next, step into the spectacular Shri Mahakal Lok Corridor, a majestic 900-meter-long architectural wonder. Walk past 108 beautifully carved pillars, massive mudras, and grand murals that depict the timeless past of Lord Shiva. The spiritual energy of the corridor, combined with state-of-the-art light and water fountain displays, makes for an deeply emotional family experience."),
                [
                    'Sightseeing Included: Chauffeur-driven transfer from Indore, Harsiddhi Temple, and comprehensive tour of the Mahakal Lok Corridor.',
                    'Evening Experience: Attendance at the grand oil-lamp tower lighting ritual and night exploration of the illuminated corridor.',
                    'Overnight Stay: Handpicked Premium Luxury Hotel, Ujjain.',
                    'Meals Included: Welcome Signature Mocktails & Gourmet Pure Vegetarian Dinner.',
                ],
            ),
            _day(
                2,
                'UJJAIN — THE DIVINE BHASMA AARTI & SACRED TEMPLES TRAIL',
                ('Wake up in the early hours of dawn for the crown jewel of your Premium Ujjain Experience. With specially pre-arranged support from your TRAGUIN team, proceed to the iconic Mahakaleshwar Jyotirlinga Temple to witness the world-famous Bhasma Aarti. As the majestic temple drums resound and sacred chants echo, marvel at the intensely spiritual ritual where the self-manifested (Swayambhu) south-facing deity is worshiped with sacred ash. This unique divine experience is bound to leave your family deeply moved and spiritually charged. Return to the hotel for a sumptuous buffet breakfast and a well-deserved rest. In the afternoon, set out for a thorough Ujjain Sightseeing trail. Visit the unique Kaal Bhairav Temple, where the deity is traditionally offered liquid spirits as part of a century-old tantric ritual. Drive along the scenic riverbanks to see the ancient Sandipani Ashram, where Lord Krishna, Balarama, and Sudama completed their education under Guru Sandipani. Conclude your day at the scenic Ram Ghat on the holy Shipra River, capturing the beautiful sunset and enjoying a quiet family photography session.'),
                [
                    'Sightseeing Included: Mahakaleshwar Temple, Kaal Bhairav Temple, Sandipani Ashram, Mangalnath Temple, and Ram Ghat.',
                    'Evening Experience: Serene riverside stroll and deep-donation (floating oil lamps) ritual at Ram Ghat.',
                    'Optional Activities: Traditional Vedic astrological reading session arranged inside the city or a private Rudrabhishek Puja.',
                    'Overnight Stay: Handpicked Premium Luxury Hotel, Ujjain.',
                    'Meals Included: Premium Multi-cuisine Breakfast & Traditional Satvik Malwi Dinner.',
                ],
            ),
            _day(
                3,
                'UJJAIN TO OMKARESHWAR & INDORE — SACRED ISLAND CRUISE',
                ("& NARMADA AARTI Following a delicious breakfast, check out of Ujjain and embark on an emotionally captivating route to Omkareshwar, a sacred island town beautifully shaped like the holy Hindu symbol 'OM' (Omkar). Nestled amidst the dramatic meeting of the Narmada and Kaveri rivers, this destination is a premier highlight of our Best Madhya Pradesh Tour Package range. Upon arrival, enjoy a TRAGUIN Signature Experience: a private chartered boat cruise on the gentle, crystal- clear waters of the Narmada River. The boat will take you directly to the cliffside Omkareshwar Jyotirlinga Temple for a highly privileged, priority Darshan. Marvel at the unique architecture and deep peace of the shrine. Afterward, cross the suspension bridge and witness the breathtaking landscapes of Mandhata island. In the late afternoon, proceed to the vibrant commercial and cultural capital of Malwa—Indore. Check into your ultra-luxury urban hotel and unwind."),
                [
                    'Sightseeing Included: Scenic countryside drive, private boat cruise, Omkareshwar Temple, Mamleshwar Temple, and Indore check-in.',
                    'Evening Experience: A legendary culinary walk at the world-renowned Chappan Dukan or Sarafa Bazaar in Indore.',
                    'Overnight Stay: Ultra-Luxury Five-Star Resort, Indore.',
                    'Meals Included: Full Buffet Breakfast & Grand Farewell Dinner.',
                ],
            ),
            _day(
                4,
                'INDORE — ROYAL HERITAGE & DEPARTURE WITH BEAUTIFUL',
                ("MEMORIES Savor a luxurious breakfast at your elite hotel. Today morning is dedicated to a curated exploration of Indore's grand history. Visit the magnificent Rajwada Palace, a stunning seven-story structure showcasing a beautiful blend of Maratha, Mughal, and French architectural styles. Next, marvel at the exquisite Kanch Ka Mandir, a brilliant Jain temple made entirely of thousands of imported glass panels, mirrors, and crystal chandeliers depicting elaborate scriptural stories. After checking out and enjoying an authentic Malwi lunch, your private chauffeur will provide a smooth, comfortable transfer to the Indore Airport or Railway Station for your return flight home. Your premium TRAGUIN Mahakaleshwar Special Itinerary concludes here, leaving your family with deep spiritual satisfaction, beautiful photographs, and unforgettable memories to cherish forever."),
                [
                    'Sightseeing Included: Rajwada Palace, Kanch Ka Mandir, and smooth Airport/Station Private Departure Transfer.',
                    'Meals Included: Luxury Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Imperial Pride / Anjushree (Executive) | Effotel by Sayaji Indore',
                'Ujjain | Indore',
                '03 Nights',
                'Deluxe',
                'Executive Room',
                "Daily Breakfast & Chef's Special Dinner",
                4,
                1,
            ),
            _hotel(
                'Solitaire Hotel & Resort (Premium Room) | Sayaji Hotel Indore (Grand Luxury)',
                'Ujjain | Indore',
                '03 Nights',
                'Premium',
                'Premium Room',
                "Daily Breakfast & Chef's Special Dinner",
                4,
                2,
            ),
            _hotel(
                'The Shipra Residency (MPT Luxury Suites) | Radisson Blu Hotel Indore',
                'Ujjain | Indore',
                '03 Nights',
                'Luxury',
                'Luxury Suite',
                'Daily Breakfast & Gourmet Dinner buffet',
                5,
                3,
            ),
            _hotel(
                'Rudraraksh Luxury Resort / Elite Villas | Suryagarh Indore / Indore Marriott Hotel',
                'Ujjain | Indore',
                '03 Nights',
                'Ultra Luxury',
                'Presidential Suite',
                'Daily Breakfast & Customized Fine Dining',
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included('Premium Stays: 03 Nights luxury accommodation across our finest handpicked hotels and resorts.', 1),
            _inc_included('Gourmet Dining: Daily multi-cuisine buffet breakfasts and specialized pure vegetarian dinners at all hotels.', 2),
            _inc_included('Luxury Transportation: Private air-conditioned luxury vehicle (Toyota Innova Crysta) strictly dedicated for all transfers, intercity travel, and local Madhya Pradesh Sightseeing.', 3),
            _inc_included('Complimentary Experiences: A private chartered boat cruise on the Narmada River in Omkareshwar, custom-tailored by TRAGUIN.', 4),
            _inc_included('Welcome Amenities: Royal traditional welcoming, fresh flower garlands, premium mineral water bottles provided inside your vehicle daily, and customized spiritual travel kits.', 5),
            _inc_included('Elite Assistance & Support: 24/7 dedicated concierge mobile coordination from TRAGUIN experts, including driver allowances, all toll taxes, parking fees, and state transport permits.', 6),
            _inc_excluded('Airfare / Rail: Inter-state flights or main railway tickets to/from Indore.', 7),
            _inc_excluded('Special Ritual Tickets: Government temple booking charges for Bhasma Aarti or specific private Pujas.', 8),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, internal camera tickets, and premium tips for temple priests or drivers.', 9),
            _inc_excluded('Insurance: Personal medical or comprehensive travel insurance policies.', 10),
        ],
    )
    return package, itinerary

def build_mp_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MP-007'
    tour_code = 'TG-MP-PMH-007'
    title = 'The Romantic Satpura Escape • Queen of Satpura Hills'
    duration = '04 Nights / 05 Days'
    slug = 'mp-007-romantic-satpura-escape-queen-of-satpura-hills'
    itin_slug = 'mp-007-romantic-satpura-escape-queen-of-satpura-hills-itinerary'
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
            _ph('Serial code MP-007 | TRAGUIN tour code TG-MP-PMH-007', 1),
            _ph('State / Country: Madhya Pradesh, India | Category: Honeymoon / Romantic Private FIT', 2),
            _ph('Destinations: Pachmarhi (Queen of Satpura)', 3),
            _ph('Ideal for: Newlyweds & Couples seeking Romance', 4),
            _ph('Best season: October to April (All year pleasant greens)', 5),
            _ph('Starting price: On Request (Premium Luxury Tier)', 6),
            _ph('Route: Pipariya / Bhopal Arrival ➔ Pachmarhi (4 Nights) ➔ Departure', 7),
            _ph('Vehicle / Meals: Private AC Sedan / SUV & Exclusive Open Gypsy | Premium MAPAI (Breakfast & Romantic Dinners)', 8),
            _ph('TRAGUIN Curated Experience Note: At TRAGUIN, we understand that a honeymoon is not an ordinary vacation—it is an emotional milestone. Our exclusive signatures on this tour include a private decorated sunset toast at the highest peak of Central India, an intimate couples-only jungle canyon trail, and special celebratory room decorations accompanied by premium welcoming amenities to elevate your romance.', 9),
            _ph('TRAGUIN Signature Experience: Private sunset toast with non-alcoholic sparkling wine at Dhoopgarh, the highest point in Central India.', 10),
            _ph('Shopping & Local Experiences: Organic wild honey and Ayurvedic herbs from Satpura forests; Gond paintings and bamboo crafts; photography at Christ Church and Apsara Vihar.', 11),
            _ph('Important: Forest permits required for many sightseeing spots—carry valid photo ID. Core forest zones require registered open 4x4 gypsies. Book WelcomHeritage Golf View 45–60 days ahead for weekends.', 12),
        ],
        moods=['Honeymoon', 'Romance', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='The Romantic Satpura Escape • Queen of Satpura Hills • 04 Nights / 05 Days',
        overview="Welcome to your forever beginning. The Best Pachmarhi Honeymoon Package, meticulously handcrafted by TRAGUIN, invites you and your significant other to celebrate love amidst the emerald heights of Central India’s single hill station. Known as the 'Queen of Satpura', Pachmarhi is a sanctuary of mist-kissed waterfalls, deep forested ravines, and ancient rock formations. This ultra-curated Luxury Pachmarhi Holiday blends highly romantic, emotional, and intimate experiences with premier comfort. Step into an enchanting paradise filled with breathtaking landscapes, curated experiences, and handpicked hotels designed to turn your initial marital journey into a collection of unforgettable memories.\n\nTOUR OVERVIEW\nThis customized Pachmarhi Honeymoon Package offers an intimate sanctuary from the outside world. From arrival to your reluctant departure, you will experience seamless personalized handling. Bask in private luxury transport, stay in the most romantic handpicked heritage and premium luxury colonial-style properties, and relish chef-curated romantic candlelit dining plans across your stay. Travel Dates: Flexible / Private Customized FIT Guest Type: Honeymoon Couple Vehicle: Private AC Sedan / SUV & Exclusive Open Gypsy Meal Plan: Premium MAPAI (Breakfast & Romantic Dinners) Route Plan: Pipariya / Bhopal Arrival ➔ Pachmarhi (4 Nights) ➔ Departure\n\nWHY CHOOSE THE PREMIUM PACHMARHI HONEYMOON TRAIL?\nA romantic journey through Madhya Pradesh leads directly to the tranquil slopes of Pachmarhi. Renowned for hosting the most pristine Top Tourist Places in Pachmarhi, this nature-clad retreat presents an idyllic setting for couples to slow down, connect, and explore together. Iconic Attractions: Explore the cascading silver waters of Bee Falls, the majestic depths of Handi Khoh ravine, the spiritual aura of Jata Shankar caves, and the magnificent heights of Dhupgarh. Most Searched Experiences: Catching a mesmerizing sunrise over undulating hills, walking hand-in- hand through dense sal forests, enjoying an intimate picnic near Duchess Falls, and viewing the night sky blanketed with infinite stars. Best Honeymoon Points: Quiet sunset viewpoints like Rajendra Giri, serene boating sessions on Pachmarhi Lake, and deep, historical exploration of the ancient Pandav Caves. Popular Instagram Locations: The majestic mist-enshrouded drop of Silver Fall (Rajat Prapat), the geometric historic structures of Pandav Caves against manicured gardens, and panoramic couples' captures at the edge of Dhoopgarh. Best Time to Visit Pachmarhi: October to April offers gorgeous weather with cool breezes and misty mornings, while the monsoon months provide romantic, cloud-kissed emerald panoramas.\n\nTRAGUIN Curated Experience Note: At TRAGUIN, we understand that a honeymoon is not an ordinary vacation —it is an emotional milestone. Our exclusive signatures on this tour include a private decorated sunset toast at the highest peak of Central India, an intimate, couples-only jungle canyon trail, and special celebratory room decorations accompanied by premium welcoming amenities to elevate your romance.",
        seo_title='MP-007 | The Romantic Satpura Escape • Queen of Satpura Hills | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Madhya Pradesh package (MP-007 / TG-MP-PMH-007): Pachmarhi Lake boating, Pandav Caves, Dhoopgarh sunset, Bee Falls, Handi Khoh, Reechgarh, and 4-tier heritage accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Scenic mountain drive, Pachmarhi Lake walk, private boating & romantic candlelit dinner', 1),
            _ih('Pandav Caves, Jata Shankar Caves, Apsara Vihar & sunset toast at Dhoopgarh peak', 2),
            _ih('Bee Falls, Handi Khoh Ravine, Priyadarshini Point & Rajendra Giri Sunset Park', 3),
            _ih('Reechgarh Rock Formations, Christ Church, Bison Lodge Museum & TRAGUIN farewell theme dinner', 4),
        ],
        days=[
            _day(
                1,
                'ARRIVAL & TRANSITION TO THE EMERALD HILL STATION',
                ('Your romantic adventure begins as you arrive at Pipariya Railway Station or Bhopal Airport. There, your dedicated TRAGUIN private chauffeur welcomes you with traditional hospitality and signature welcome amenities. Embark on a highly scenic drive ascending into the Satpura Range. Watch the urban landscapes dissolve into rolling green hills, winding roads, and pristine mountain air. Upon arriving in the serene town of Pachmarhi, check into your romantic handpicked luxury hotel—a beautifully restored colonial-style estate offering quiet privacy. Enjoy a smooth check-in, a special welcome cake, and floral room decorations. In the late afternoon, take a relaxed hand-in-hand stroll around the tranquil Pachmarhi Lake, enjoying a private boat ride as the sky shifts through shades of amber. Return to your resort for a curated candlelit dinner under the stars, creating your very first unforgettable memories together.'),
                [
                    'Sightseeing Included: Scenic mountain drive, Pachmarhi Lake walk, Private Boating experience.',
                    'Evening Experience: Private Lakeside Boat Ride and a Romantic Candlelit Dinner at the resort.',
                    'Overnight Stay: Handpicked Premium Luxury Resort, Pachmarhi.',
                    'Meals Included: Welcome Drinks, Honeymoon Cake, & Gourmet Dinner.',
                ],
            ),
            _day(
                2,
                'MYSTICAL CAVES & THE HIGHEST SUNSET AT DHOOPGARH',
                ("Savor a luxurious, multi-course breakfast at your resort before boarding an exclusive, open-top 4x4 Gypsy for an immersive day of Pachmarhi Sightseeing. Begin your journey at the ancient Pandav Caves, five rock-cut sanctuaries carved into a sandstone hill, wrapped in fascinating mythological lore and surrounded by beautiful, manicured gardens perfect for your first couple's photo session. Next, dive into the spiritual mystique of Jata Shankar Caves, a natural cavern tucked between massive rocks where natural stalagmites resemble the matted locks of Lord Shiva. The crown jewel of your evening is a drive up to Dhoopgarh, the highest peak in Madhya Pradesh and the entire Satpura range. TRAGUIN will secure premium access to this majestic spot. Stand together at the edge of the world, watching a breathtaking sunset cast gold and crimson hues over infinite ridges. Share a quiet, intimate moment with non-alcoholic sparkling wine as the stars begin to illuminate the pristine night sky."),
                [
                    'Sightseeing Included: Pandav Caves, Jata Shankar Caves, Apsara Vihar (Fairy Pool), Dhoopgarh Sunset Peak.',
                    'Evening Experience: Sunset Toast at Dhoopgarh followed by a cozy evening at the property.',
                    'Optional Activities: A soo',
                    'Overnight Stay: Handpicked Premium Luxury Resort, Pachmarhi.',
                    'Meals Included: Buffet Breakfast & Specially Curated Traditional Dinner.',
                ],
            ),
            _day(
                3,
                'CASCADING WATERFALLS & GRAND CANYONS OF SATPURA',
                ('Awake to the soothing sounds of birds and cool mountain mist. Today is dedicated to experiencing the raw, natural wonders of your Pachmarhi Honeymoon Package. After breakfast, head out in your private open Gypsy to the spectacular Bee Falls (Jamuna Prapat). This magnificent perennial waterfall cascades down a rugged cliff into a clear, shaded pool below. Take a light walk through the forest trail to feel the refreshing water spray, a perfect setting for candid photography. In the afternoon, visit the jaw-dropping Handi Khoh—a massive, 300-foot-deep forest-clad ravine with nearly vertical cliffs. Hear the gentle rustle of the wind and old legends that echo through this impressive canyon. Next, proceed to Priyadarshini Point (Forsyth Point), the original vantage point from which Captain Forsyth discovered Pachmarhi in 1857. Conclude your day with a relaxed evening at Rajendra Giri Sunset Park, stroll through its vibrant flower beds, and watch the sun dip quietly behind the hills.'),
                [
                    'Sightseeing Included: Bee Falls, Handi Khoh Ravine, Priyadarshini Point, Rajendra Giri Park.',
                    'Evening Experience: Quiet evening walk through the colonial lanes of Pachmarhi town.',
                    'Optional Activities: A soothing, couples-only Ayurvedic full-body wellness massage at a luxury spa.',
                    'Overnight Stay: Handpicked Premium Luxury Resort, Pachmarhi.',
                    'Meals Included: Premium Breakfast & Multi-cuisine Fine Dining Dinner.',
                ],
            ),
            _day(
                4,
                'HIDDEN VALLEY EXCURSIONS & INTIMATE FOREST TRAILS',
                ("Indulge in a slow, relaxed breakfast. Today, your Premium Pachmarhi Experience takes you off the standard tourist paths into hidden sanctuaries. Embark on an intimate excursion toward Duchess Falls or Reechgarh, an incredible natural amphitheater-like rock formation hidden deep inside the jungle. Walk through a natural stone archway into a quiet cavern where sunlight filters softly through the canopy—an elite, private atmosphere tailored for couples. In the afternoon, enjoy a TRAGUIN Signature Experience: a premium, curated picnic hamper lunch set up at a private, scenic spot deep in the forest. Spend the rest of your afternoon exploring the historic colonial bungalows and quiet churches of Pachmarhi, or pick up unique handcrafted souvenirs from the local town markets. In the evening, return to your resort for a grand farewell dinner arranged specially by the hotel's master chefs to celebrate your final night in this romantic paradise."),
                [
                    'Sightseeing Included: Reechgarh Rock Formations, Christ Church (Colonial architecture), Bison Lodge Museum.',
                    'Evening Experience: Special TRAGUIN Farewell Theme Dinner with a complimentary customized souvenir.',
                    'Overnight Stay: Handpicked Premium Luxury Resort, Pachmarhi.',
                    'Meals Included: Gourmet Breakfast, Signature Picnic Hamper Lunch, & Grand Farewell Dinner.',
                ],
            ),
            _day(
                5,
                'FAREWELL TO THE SATPURA PARADISE — DEPARTURE',
                ("Share a beautiful final morning breakfast on the veranda of your resort, overlooking the lush, green lawns. Take some final couple's photographs amidst the serene settings of your property. Complete your check-out formalities, and meet your private chauffeur for your smooth transfer back to Pipariya Railway Station or Bhopal Airport. Your unforgettable Luxury Pachmarhi Holiday draws to a gentle close. You return home with a deeply strengthened bond, beautiful photographs, and a treasure trove of romantic memories, all curated flawlessly by the travel experts at TRAGUIN."),
                [
                    'Sightseeing Included: Departure transfer via your private luxury vehicle. Meals Included: Premium Buffet Breakfast.',
                    'Meals Included: Premium Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'MPT Champak Bungalow / Rock End Manor',
                'Pachmarhi',
                '04 Nights',
                'Deluxe',
                'Heritage Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
            ),
            _hotel(
                'WelcomHeritage Golf View Premium Regal Room',
                'Pachmarhi',
                '04 Nights',
                'Premium',
                'Premium Regal Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
            ),
            _hotel(
                'WelcomHeritage Golf View Pachmarhi Luxury Pavilion Suite',
                'Pachmarhi',
                '04 Nights',
                'Luxury',
                'Luxury Pavilion Suite',
                'MAPAI & Honeymoon Inclusions',
                5,
                3,
            ),
            _hotel(
                'The Satpura Retreat / Private Luxury Villa Royal Colonial Heritage Suite',
                'Pachmarhi',
                '04 Nights',
                'Ultra Luxury',
                'Royal Colonial Heritage Suite',
                'MAPAI & Tailored VIP Signatures',
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included('Premium Stays: 04 Nights premium accommodation at handpicked luxury heritage properties in Pachmarhi.', 1),
            _inc_included('Gourmet Dining: Daily buffet breakfast and custom-designed romantic dinners at your resort.', 2),
            _inc_included('Luxury Transportation: Private air-conditioned vehicle for airport/station transfers, and an exclusive dedicated open 4x4 Gypsy for forest sightseeing routes.', 3),
            _inc_included('Welcome Amenities: Traditional royal welcome at your hotel, complimentary honeymoon cake, artisanal chocolates, and daily premium mineral water.', 4),
            _inc_included('Complimentary Experiences: A private boat ride on Pachmarhi Lake and a scenic sunset toast at Dhoopgarh peak.', 5),
            _inc_included('TRAGUIN Support: 24/7 dedicated virtual concierge assistance from TRAGUIN honeymoon coordinators, along with covered fuel, toll taxes, parking, and driver allowances.', 6),
            _inc_excluded('Travel Tickets: Commercial flights or railway tickets to/from Bhopal or Pipariya.', 7),
            _inc_excluded('Entry Tickets: Mandatory forest department permits, guide fees, and individual monument entry tickets.', 8),
            _inc_excluded('Personal Expenses: Laundry, premium room service, telephone calls, alcoholic beverages, and tips.', 9),
            _inc_excluded('Optional Tours: Spa therapies, adventure sports, or any activities not explicitly included in the final itinerary.', 10),
            _inc_excluded('Insurance: Travel or medical insurance coverage plans.', 11),
        ],
    )
    return package, itinerary

def build_mp_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MP-008'
    tour_code = 'TG-MP-SCL-008'
    title = 'The Spiritual, Heritage & Wellness Trail of Central India'
    duration = '05 Nights / 06 Days'
    slug = 'mp-008-spiritual-heritage-wellness-trail-central-india'
    itin_slug = 'mp-008-spiritual-heritage-wellness-trail-central-india-itinerary'
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
            _ph('Serial code MP-008 | TRAGUIN tour code TG-MP-SCL-008', 1),
            _ph('State / Country: Madhya Pradesh, India | Category: Senior Citizen / Leisure Private FIT', 2),
            _ph('Destinations: Indore • Ujjain • Mandu • Maheshwar', 3),
            _ph('Ideal for: Senior Citizens, Families, Leisure Travelers', 4),
            _ph('Best season: October to March (Pleasant and Cool Weather)', 5),
            _ph('Starting price: On Request (Premium Luxury Tier)', 6),
            _ph('Route: Indore Arrival ➔ Ujjain (1N) ➔ Mandu (1N) ➔ Maheshwar (2N) ➔ Indore Departure (1N)', 7),
            _ph('Vehicle / Meals: Luxury Toyota Innova Crysta (Plush Seating) | Premium MAPAI (Breakfast & Mild Dinners)', 8),
            _ph('TRAGUIN Curated Experience Note: At TRAGUIN, we believe true luxury means a completely worry-free journey. Our unique touches for senior citizens on this itinerary include VIP fast-track temple entries to bypass long lines, wheelchair assistance on request at key historical sights, slow-paced mornings, and freshly prepared, mild local meals that respect your dietary choices.', 9),
            _ph('TRAGUIN Signature Experience: Private sunset boat cruise along the sacred Narmada River, complete with traditional music and tea.', 10),
            _ph('Shopping & Local Experiences: Maheshwari silk sarees from royal weaving societies; Chanderi sarees in Indore; hand-carved wooden items and Indore Gajak sweets.', 11),
            _ph('Important: All hotels feature lifts and step-free dining access. Late morning starts (~10:30 AM) with afternoon rest 2:00–4:30 PM. Book Ahilya Fort 60–90 days in advance.', 12),
        ],
        moods=['Leisure', 'Spiritual', 'Heritage'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='The Spiritual, Heritage & Wellness Trail of Central India • 05 Nights / 06 Days',
        overview='Welcome to an extraordinary journey planned with your absolute comfort and peace of mind in focus. The Best Madhya Pradesh Tour Package for elderly and relaxed travelers, beautifully customized by TRAGUIN, invites you to rediscover the timeless heritage, sacred temples, and majestic riverside palaces of Central India. This beautifully paced Leisure Madhya Pradesh Holiday avoids rushed itineraries and demanding walks, emphasizing smooth private travel, premium stays, accessible infrastructure, and heartwarming hospitality. Let us introduce you to the breathtaking landscapes, peaceful river ghats, and spiritual tranquility of this ancient land, weaving unforgettable memories to cherish for a lifetime.\n\nTOUR OVERVIEW\nThis customized Madhya Pradesh Senior Citizen Tour introduces travelers to the smooth plains and cultural heart of Malwa and Nimar. Centered around the commercial capital Indore, the legendary holy town of Ujjain, the architectural poetry of Mandu, and the tranquil Narmada riverbanks in Maheshwar, the entire circuit has been handpicked to feature shorter drives, premium hotels with elevator access, and smooth, flat walking surfaces. Travel Dates: Flexible / Custom Tailored FIT Guest Type: Senior Citizens & Leisure Travelers Vehicle: Luxury Toyota Innova Crysta (Plush Seating) Meal Plan: Premium MAPAI (Breakfast & Mild Dinners) Route Plan: Indore Arrival ➔ Ujjain (1N) ➔ Mandu (1N) ➔ Maheshwar (2N) ➔ Indore Departure (1N)\n\nWHY CHOOSE THE PREMIUM LEISURE MADHYA PRADESH EXPERIENCE?\nA specialized holiday through Central India uncovers an exceptional blend of spiritual peace and royal leisure. Highlighted by the most comfortable and legendary Top Tourist Places in Madhya Pradesh, this itinerary offers an unhurried, emotionally satisfying travel experience. Famous Attractions: Pray at the holy Mahakaleshwar Jyotirlinga Temple in Ujjain, admire the architectural beauty of Jahaz Mahal in Mandu, and sit along the pristine Ahilya Ghat in Maheshwar. Most Searched Experiences: Attending the majestic evening Bhasma Aarti or VIP Shringar Darshan, enjoying slow boat rides on the quiet Narmada River, and exploring authentic local textile weaving centers. Senior & Family Leisure Highlights: Spacious luxury hotel rooms, comfortable, smooth vehicle travel, and serene evening classical music programs overlooking flowing waters. Popular Instagram & Photography Locations: The stunning white structure of Rani Roopmati Pavilion, the grand symmetric stone stairways of Maheshwar Fort, and the grand corridors of Lal Bagh Palace in Indore. Best Time to Visit Madhya Pradesh: The winter season from October to March brings lovely cool weather, providing bright sunny afternoons that are ideal for relaxed, comfortable Madhya Pradesh Sightseeing. • • • • • YOUR HANDCRAFTED SLOW-PACED ITINERARY\n\nTRAGUIN Curated Experience Note: At TRAGUIN, we believe true luxury means a completely worry-free journey. Our unique touches for senior citizens on this itinerary include VIP fast-track temple entries to bypass long lines, wheelchair assistance on request at key historical sights, slow-paced mornings, and freshly prepared, mild local meals that respect your dietary choices.',
        seo_title='MP-008 | The Spiritual, Heritage & Wellness Trail of Central India | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Madhya Pradesh package (MP-008 / TG-MP-SCL-008): Mahakal Lok, Mandu Jahaz Mahal, Maheshwar Ahilya Ghat boat ride, Lal Bagh Palace, and senior-friendly 4-tier accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Mahakal Lok Corridor, Harsiddhi Temple & VIP fast-track Darshan at Mahakaleshwar Temple', 1),
            _ih('Jahaz Mahal, Hindola Mahal & Mandu Fort gates with relaxed lakeside tea session', 2),
            _ih('Rani Roopmati Pavilion, Baz Bahadur Palace & luxury heritage palace check-in at Maheshwar', 3),
            _ih('Maheshwar Fort, Ahilya Ghat, Rehwa Weaving Center & private Narmada sunset boat ride', 4),
            _ih('Lal Bagh Palace, Rajwada Palace, Kanch Mandir & managed culinary tour in Indore', 5),
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN INDORE & TRANSITION TO HOLY UJJAIN',
                ('Your gentle, beautiful holiday begins with your arrival at Indore Airport or Railway Station. You will be greeted warmly by your dedicated TRAGUIN tour manager and private chauffeur with a fresh bouquet of flowers and premium welcome amenities. Board your plush, air-conditioned vehicle, equipped with comfortable seating, extra cushions, and refreshing drinks, and enjoy a smooth, 1.5-hour drive on a modern highway to the ancient holy city of Ujjain. Check into your handpicked premium hotel, which features excellent modern amenities and easy access. After a relaxed lunch and a rejuvenating afternoon rest, head out for a comforting Ujjain Sightseeing experience. Visit the massive, accessible corridor of the newly built Mahakal Lok, featuring wide electric-golf-cart paths lined with exquisite statues telling ancient stories. As dusk falls, participate in an exclusive, pre-arranged VIP Darshan at the sacred Mahakaleshwar Jyotirlinga Temple, letting you experience the powerful, peaceful energy of the evening rituals with absolute comfort and no long queues.'),
                [
                    'Sightseeing Included: Mahakal Lok Corridor, accessible paths, Harsiddhi Temple (famous for its historic twin lamp towers).',
                    'Evening Experience: VIP Fast-Track Entry for Darshan at Mahakaleshwar Temple, avoiding crowds.',
                    'Overnight Stay: Handpicked Premium Luxury Hotel, Ujjain.',
                    'Meals Included: Welcome Drink & Gentle, Non-Spicy Multi-Cuisine Dinner.',
                ],
            ),
            _day(
                2,
                'UJJAIN TO MANDU — THE CITY OF JOY AND ETERNAL ROMANCE',
                ("Begin your morning with an optional, early morning peaceful stroll near the shipra riverbanks or enjoy a leisurely breakfast in the hotel dining hall. Say goodbye to Ujjain as your luxury transport drives you through scenic, flat agricultural landscapes toward the hilltop fortress city of Mandu, beautifully dubbed the 'City of Joy'. Arrive and check into your premium lakeside resort curated by TRAGUIN to offer serene nature views and absolute quiet. After a delicious lunch and an unhurried rest, embark on a gentle tour of Mandu’s historic structures. Explore the iconic Jahaz Mahal (Ship Palace), beautifully built between two lakes to resemble a grand royal ship floating on water. Your expert local guide will share poetic stories of ancient kings and queens at a relaxed pace, with multiple comfortable rest stops along the smooth garden paths. Conclude your afternoon looking out over the peaceful lake waters as the sun sets."),
                [
                    'Sightseeing Included: Jahaz Mahal, Hindola Mahal (Swing Palace), and the grand Mandu Fort gates.',
                    'Evening Experience: Relaxed tea session overlooking the lake followed by an informative historical briefing. Meals Included: Buffet Breakfast & Light Local Heritage Dinner.',
                    'Overnight Stay: Premium Lakeside Resort, Mandu.',
                    'Meals Included: Buffet Breakfast & Light Local Heritage Dinner.',
                ],
            ),
            _day(
                3,
                'MANDU TO MAHESHWAR — THE ROYAL RIVERSIDE SANCTUARY',
                ('Wake up to a quiet morning filled with the soft sounds of lakeside nature. After breakfast, take a short, comfortable drive to visit the famous Rani Roopmati Pavilion, standing high on a hill edge. This elegant structure offers breathtaking landscapes looking down at the winding Narmada River far below. For guests who prefer to avoid walking up slopes, we arrange special vehicle access directly to the main pavilion entrance. Later, descend into the peaceful valley and arrive at the holy riverside town of Maheshwar. Check into an exceptional luxury heritage hotel. Maheshwar was the historical home of the legendary, pious Queen Rani Ahilyabai Holkar. Spend your afternoon relaxing inside the cool stone courtyards of the palace, soaking in an elegant world of old-world royalty and spiritual peace.'),
                [
                    'Sightseeing Included: Rani Roopmati Pavilion, Baz Bahadur Palace, and transition drive to Maheshwar.',
                    'Evening Experience: Gentle walking tour of the quiet inner palace complex and traditional welcome.',
                    'Overnight Stay: Luxury Heritage Palace Hotel, Maheshwar.',
                    'Meals Included: Full Breakfast & Traditional Satvik Dinner.',
                ],
            ),
            _day(
                4,
                'MAHESHWAR — SERENE GHATS, BOATING AND HANDLOOM ARTISTRY',
                ('Today brings one of the most relaxing and beautiful highlights of your Leisure Madhya Pradesh Holiday. After an unhurried breakfast, explore the iconic Maheshwar Fort and Ahilya Ghat. The stone paths here are wide, flat, and exceptionally well-maintained, allowing for easy walking. Walk past local artisans and historic shrines, listening to the soothing sound of flowing river waters. In the afternoon, enjoy an exclusive TRAGUIN Signature Experience: a private, smooth boat ride on the sacred Narmada River during the golden sunset hour. Float past the beautifully carved stone chhatris as the sun sets over the water. Later, visit a traditional handloom weaving center supported by the royal family, where you can watch master weavers create world-famous Maheshwari silk sarees and textiles, offering an authentic, slow cultural interaction.'),
                [
                    'Sightseeing Included: Maheshwar Fort, Ahilya Ghat, Royal Cenotaphs, Rehwa Weaving Center.',
                    'Evening Experience: Private sunset boat ride with hot tea and light refreshments served on board. Meals Included: Buffet Breakfast & Special Farewell Royal Dinner.',
                    'Overnight Stay: Luxury Heritage Palace Hotel, Maheshwar.',
                    'Meals Included: Buffet Breakfast & Special Farewell Royal Dinner.',
                ],
            ),
            _day(
                5,
                'MAHESHWAR TO INDORE — ROYAL LEGACIES AND LOCAL FLAVORS',
                ('Enjoy a final sunrise over the holy river before having breakfast at your palace hotel. Board your luxury vehicle for a relaxed drive back to the clean city of Indore. Check into a premier ultra-luxury hotel and unwind in your spacious room. In the afternoon, explore the grand Lal Bagh Palace, which showcases the incredible history and elite European-inspired lifestyle of the Holkar rulers. In the evening, enjoy a customized culinary walk. Indore is globally famous for its food culture, and we provide a comfortable, clean excursion to experience mild, freshly prepared delicacies like soft Khopo or sweet, hot Malpua at a premium culinary stop, ensuring absolute hygiene and health care for senior travelers.'),
                [
                    'Sightseeing Included: Lal Bagh Palace, Rajwada Palace (outer view), Kanch Mandir (Glass Temple).',
                    'Evening Experience: Managed culinary tour with seating and premium hygiene standards.',
                    'Overnight Stay: Premier Ultra-Luxury Hotel, Indore.',
                    'Meals Included: Gourmet Breakfast & Farewell Dinner Celebration.',
                ],
            ),
            _day(
                6,
                'INDORE — RELAXED SHOPPING & DEPARTURE WITH MEMORIES',
                ('Indulge in a beautiful, extensive breakfast at your luxury hotel. Spend your morning relaxing by the pool or packing your bags at your own pace. If time permits, your driver will gladly take you to a premium, air- conditioned local boutique to purchase authentic Chanderi fabrics, local handicrafts, or famous Indore savories to take home for your family. In the afternoon, enjoy a smooth, private transfer to the Indore Airport or Railway Station for your onward journey home. Your premium, slow-paced exploration concludes beautifully, leaving you with countless photographs, renewed spirit, and unforgettable memories crafted with complete love and care by TRAGUIN.'),
                [
                    'Sightseeing Included: Accessible shopping transfer & Airport/Station Departure Drop.',
                    "Meals Included: Comprehensive Buffet Breakfast. HANDPICKED SENIOR-FRIENDLY ACCOMMODATIONS We understand that accessible luxury is vital for senior citizens. TRAGUIN works exclusively with premium properties that offer large rooms, elevator access, wheelchair assistance, and high hygiene standards. Category Tier Ujjain (1 Night) Mandu (1 Night) Maheshwar (2 Nights) Indore (1 Night) DELUXE MPT Avantika / Imperial MPT Malwa Retreat MPT Narmada Retreat Effotel by Sayaji Indore PREMIUM Ananya Marasa / Solitaire MPT Malwa Resort (Lake View) Labhoo's Cafe & Lodge Sayaji Hotel Indore LUXURY Radisson Hotel Ujjain Mandu Heritage Palace Property Ahilya Fort Heritage Palace Radisson Blu Hotel Indore ULTRA LUXURY Radisson Ujjain (Executive) Luxury Private Lakeside Villa Ahilya Fort (Royal Suite) Essential Luxury / Sheraton Indore PACKAGE INCLUSIONS ✔Premium Stays: 05 Nights luxury hotel stays selected carefully for senior citizen accessibility and comfort. ✔Gourmet Mild Dining: Daily extensive buffet breakfast and health-conscious dinners tailored to your taste. ✔Luxury Transportation: Private air-conditioned Toyota Innova Crysta with a highly experienced, gentle corporate driver. ✔VIP Access: Pre-arranged VIP fast-track temple entries in Ujjain to completely avoid long standing queues. ✔TRAGUIN Signatures: Exclusive private sunset boat ride on the Narmada River with tea services on board. ✔On-Sight Assi",
                ],
            ),
        ],
        hotels=[
            _hotel(
                'MPT Avantika / Imperial | MPT Malwa Retreat | MPT Narmada Retreat | Effotel by Sayaji Indore',
                'Ujjain | Mandu | Maheshwar | Indore',
                '05 Nights',
                'Deluxe',
                'Deluxe Room',
                'Daily Breakfast & Dinner',
                4,
                1,
            ),
            _hotel(
                "Ananya Marasa / Solitaire | MPT Malwa Resort (Lake View) | Labhoo's Cafe & Lodge | Sayaji Hotel Indore",
                'Ujjain | Mandu | Maheshwar | Indore',
                '05 Nights',
                'Premium',
                'Premium Room',
                'Daily Breakfast & Dinner',
                4,
                2,
            ),
            _hotel(
                'Radisson Hotel Ujjain | Mandu Heritage Palace Property | Ahilya Fort Heritage Palace | Radisson Blu Hotel Indore',
                'Ujjain | Mandu | Maheshwar | Indore',
                '05 Nights',
                'Luxury',
                'Luxury Room',
                'Daily Breakfast & Dinner',
                5,
                3,
            ),
            _hotel(
                'Radisson Ujjain (Executive) | Luxury Private Lakeside Villa | Ahilya Fort (Royal Suite) | Essential Luxury / Sheraton Indore',
                'Ujjain | Mandu | Maheshwar | Indore',
                '05 Nights',
                'Ultra Luxury',
                'Royal Suite',
                'Daily Breakfast & Customized Fine Dining',
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included('Premium Stays: 05 Nights luxury hotel stays selected carefully for senior citizen accessibility and comfort.', 1),
            _inc_included('Gourmet Mild Dining: Daily extensive buffet breakfast and health-conscious dinners tailored to your taste.', 2),
            _inc_included('Luxury Transportation: Private air-conditioned Toyota Innova Crysta with a highly experienced, gentle corporate driver.', 3),
            _inc_included('VIP Access: Pre-arranged VIP fast-track temple entries in Ujjain to completely avoid long standing queues.', 4),
            _inc_included('TRAGUIN Signatures: Exclusive private sunset boat ride on the Narmada River with tea services on board.', 5),
            _inc_included('On-Sight Assistance: Coordination for wheelchair availability and electric golf cart transfers where requested.', 6),
            _inc_included('Taxes & Fees: Complete toll taxes, parking fees, driver allowances, and 24/7 dedicated travel support from TRAGUIN experts.', 7),
            _inc_excluded('Travel Tickets: Direct flights or train bookings from your hometown to Indore.', 8),
            _inc_excluded('Monument Entry: Individual camera fees or local temple donation tickets.', 9),
            _inc_excluded('Personal Expenses: Laundry services, long-distance telephone bills, or special items ordered at the hotel.', 10),
            _inc_excluded('Insurance: Personal travel insurance or medical coverage plans.', 11),
        ],
    )
    return package, itinerary

def build_mp_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MP-009'
    tour_code = 'TG-RMP-UX7D'
    title = 'The Grand Heritage & Tiger Trail Experience'
    duration = '06 Nights / 07 Days'
    slug = 'mp-009-grand-heritage-tiger-trail-experience'
    itin_slug = 'mp-009-grand-heritage-tiger-trail-experience-itinerary'
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
            _ph('Serial code MP-009 | TRAGUIN tour code TG-RMP-UX7D', 1),
            _ph('State / Country: Madhya Pradesh, India | Category: Luxury Heritage & Wilderness Private FIT', 2),
            _ph('Destinations: Gwalior • Orchha • Khajuraho • Panna', 3),
            _ph('Ideal for: Elite Families, Couples & Connoisseurs', 4),
            _ph('Best season: October to April', 5),
            _ph('Starting price: On Request (Ultra-Luxury Tier)', 6),
            _ph('Route: Gwalior (1N) ➔ Orchha (2N) ➔ Khajuraho & Panna (3N)', 7),
            _ph('Vehicle / Meals: Private AC Luxury SUV & Exclusive 4x4 Park Jeeps | Premium MAPAI (Breakfast & Chef-Curated Dinners)', 8),
            _ph('TRAGUIN Curated Experience Note: At TRAGUIN, we provide access to worlds others only see from afar. Our signature touches on this itinerary include private royal champagne welcomes, exclusive high tea settings along the boulder-strewn Ken River, a private classical musical demonstration in Khajuraho, and expertly tracking the royal Bengal tiger alongside master naturalists.', 9),
            _ph('TRAGUIN Signature Experience: Private riverfront high tea set up elegantly along the Betwa River bank.', 10),
            _ph('Shopping & Local Experiences: Gwalior silks at Patankar Bazaar; Orchha Dokra crafts; Khajuraho stone miniatures and silver jewelry.', 11),
            _ph('Important: Temple conservative attire recommended. Panna safari permits regulated—book 60–90 days ahead. Limited inventory at Taj Usha Kiran and Pashan Garh.', 12),
        ],
        moods=['Heritage', 'Wildlife', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='The Grand Heritage & Tiger Trail Experience • 06 Nights / 07 Days',
        overview='Welcome to a realm of legendary kings and untamed forests. The Best Madhya Pradesh Tour Package, designed exclusively by TRAGUIN, invites you to immerse yourself in the sovereign spirit of India’s most regal state. This ultra-customized Luxury Madhya Pradesh Holiday seamlessly bridges the ancient grandeur of imperial forts with the raw adrenaline of wild tiger domains. Traverse breathtaking landscapes, step inside architectural masterpieces, and indulge in pristine royal hospitality. From private historic walks to majestic river sunset high teas, this curated journey promises to weave an elegant tapestry of unforgettable memories across the heart of Central India.\n\nTOUR OVERVIEW\nThe **Royal M.P.** itinerary is a masterfully balanced Madhya Pradesh Family Tour and luxury escape. It connects the historic fortresses of Gwalior, the frozen-in-time medieval towers of Orchha, the world-renowned UNESCO World Heritage temples of Khajuraho, and the elite wildlife preserves of Panna National Park. Travelers enjoy private luxury transportation, premier palace stays, expert local historians, and VIP park entry permissions. Travel Dates: Flexible / Bespoke Custom FIT Guest Type: Luxury Leisure Travelers / Family Vehicle: Private AC Luxury SUV & Exclusive 4x4 Park Jeeps Meal Plan: Premium MAPAI (Breakfast & Chef-Curated Dinners) Route Plan: Gwalior (1N) ➔ Orchha (2N) ➔ Khajuraho & Panna (3N)\n\nWHY EXPERIENCE THE PREMIUM ROYAL MADHYA PRADESH CIRCUIT?\nEmbarking on a premium journey across Central India opens doors to the finest Top Tourist Places in Madhya Pradesh. It stands out as an incomparable route for families, heritage enthusiasts, and luxury seekers alike. Iconic Attractions: Explore the soaring cliffside walls of Gwalior Fort, the stunning Italianate Jai Vilas Palace, the beautiful riverside towers of Orchha, the intricately carved Kandariya Mahadeva Temple in Khajuraho, and the rich wilderness of Panna. Most Searched Experiences: Walking amidst ancient erotically carved stone sculptures, attending the moving evening Aarti by the Betwa River, tracking majestic predators on an open jeep safari, and seeing ancient rock-paintings. Premium Honeymoon & Family Highlights: Intimate dining experiences overlooking ancient monuments, romantic jungle safaris, and engaging interactive workshops introducing age-old arts to children. Popular Instagram Locations: The majestic blue-and-gold mosaic tiled walls of Man Singh Palace, sunset framing the towering spires of Chaturbhuj Temple, and sunlight gleaming off the granite walls of Raneh Canyons. Best Time to Visit Madhya Pradesh: The refreshing cooler months from October to April provide pristine daytime conditions for immersive Madhya Pradesh Sightseeing and rich photography sessions.\n\nTRAGUIN Curated Experience Note: At TRAGUIN, we provide access to worlds others only see from afar. Our signature touches on this itinerary include private royal champagne welcomes, exclusive high tea settings along the boulder-strewn Ken River, an private classical musical demonstration in Khajuraho, and expertly tracking the royal Bengal tiger alongside master naturalists.',
        seo_title='MP-009 | The Grand Heritage & Tiger Trail Experience | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Madhya Pradesh package (MP-009 / TG-RMP-UX7D): Gwalior Fort, Orchha Chhatris high-tea, Khajuraho UNESCO temples, Raneh Canyon, Panna tiger safari, and 4-tier palace and lodge accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Jai Vilas Palace, Gwalior Fort & VIP Gwalior Fort Light & Sound Show', 1),
            _ih('Orchha Fort Complex, Ram Raja Temple Aarti & private Riverside High Tea', 2),
            _ih('Southern Group temples, Khajuraho Light & Sound Show & Western Group with Raneh Falls', 3),
            _ih('Panna Jungle Safari, campfire gathering & sunrise safari before departure', 4),
        ],
        days=[
            _day(
                1,
                'GWALIOR — ARRIVAL & THE LEGACY OF IMPERIAL DYNASTIES',
                ("Your grand journey begins as your flight lands in Gwalior. Receive a warm greeting from your dedicated TRAGUIN tour manager and private chauffeur, who will escort you in a luxury SUV to your premium palace hotel. After a seamless check-in and an authentic lunch, embark on your Gwalior Sightseeing circuit. Explore the breathtaking Jai Vilas Palace, a 19th-century royal estate showcasing European classical style. Marvel at the grand Durbar Hall, which houses two of the world's heaviest crystal chandeliers, and observe the iconic silver model train that delivered fine digestifs around the royal table. In the late afternoon, wind your way up to the majestic Gwalior Fort. Walk through the blue-tiled walls of Man Mandir Palace and step back into centuries of royal intrigue. As darkness sweeps across the valley, enjoy a Premium Gwalior Experience with VIP seating at the Gwalior Fort Sound & Light Show, bringing history alive before your eyes."),
                [
                    'Sightseeing Included: Jai Vilas Palace museum, Gwalior Fort walls, Teli Ka Mandir, Saas-Bahu Temples.',
                    'Evening Experience: VIP Tickets to the spectacular Gwalior Fort Light & Sound Show.',
                    'Overnight Stay: Elite Heritage Palace Hotel, Gwalior.',
                    'Meals Included: Welcome Signature Drink & Gourmet Multi-course Dinner.',
                ],
            ),
            _day(
                2,
                'GWALIOR TO ORCHHA — APPROACHING THE MEDIEVAL RIVERSIDE CAPITAL',
                ('Savor a luxurious breakfast at the palace before initiating a highly scenic cross-country drive toward Orchha. Hidden elegantly on the banks of the boulder-strewn Betwa River, Orchha remains beautifully preserved from its 16th-century foundation under Bundela kings. Check into your private luxury riverside retreat curated carefully by TRAGUIN designers. In the afternoon, begin exploring the vast Orchha Fort Complex. Enter the sprawling plazas of the Raja Mahal to view its colorful religious murals, and walk through Jahangir Mahal, a beautiful multi-tiered palace offering endless panoramic views of dense jungles and ancient spires. As the sun begins to set, join the locals at the historic Ram Raja Temple—the only shrine in India where Lord Rama is revered as a literal king and honored with a daily military guard—for an emotional evening Aarti ceremony.'),
                [
                    'Sightseeing Included: Countryside drive, Raja Mahal, Jahangir Mahal, Rai Praveen Mahal.',
                    'Evening Experience: Traditional evening Aarti prayer at the royal Ram Raja Temple.',
                    'Optional Activities: Scenic river rafting down the Betwa River or an interactive pottery class with local artisans.',
                    'Overnight Stay: Premium Luxury Riverside Resort, Orchha.',
                    'Meals Included: Buffet Breakfast & Traditional Bundelkhandi Palace Dinner.',
                ],
            ),
            _day(
                3,
                'ORCHHA — THE ROYAL CENOTAPHS & SUNSET RIVER HIGH TEA',
                ('Wake up to the refreshing sound of rushing water and forest mist. Today offers an immersive look into Orchha Sightseeing gems. Following breakfast, visit the majestic Orchha Chhatris—fourteen towering stone cenotaphs standing gracefully along the river edge. A private historian will join you, revealing the deep structural symbolism and history written into these royal monuments. Later, explore the immense Chaturbhuj Temple, an architectural marvel standing on an elevated stone base. In the afternoon, enjoy an exclusive TRAGUIN Signature Experience: a premium high-tea set up elegantly at a quiet spot overlooking the Betwa River. Spend your evening relaxing with a wellness therapy at your resort or participating in an optional gentle rafting excursion floating past the illuminated historic cenotaphs.'),
                [
                    'Sightseeing Included: Royal Cenotaphs (Chhatris), Chaturbhuj Temple, Laxminarayan Temple.',
                    'Evening Experience: Private Riverside High Tea and a Sunset Photography session.',
                    'Optional Activities: Scenic river rafting down the Betwa River or an interactive pottery class with local artisans.',
                    'Overnight Stay: Premium Luxury Riverside Resort, Orchha.',
                    'Meals Included: Breakfast, Curated High Tea, & Fine Dining Dinner.',
                ],
            ),
            _day(
                4,
                'ORCHHA TO KHAJURAHO — ENTRY TO THE KINGDOM OF STONE ART',
                ("After a leisurely breakfast, depart Orchha as your private luxury vehicle drives you toward the world-famous village of Khajuraho. This destination is home to the most iconic highlights of our Best Khajuraho Tour Package: the magnificent UNESCO World Heritage temples. Arrive and check into your ultra-luxury resort, where your room looks directly toward the ancient monument towers. In the afternoon, begin exploring the Southern Group of Temples, including Duladeo and Chaturbhuj temples, known for their slender stone carvings. As dusk falls, attend the Khajuraho Sound and Light Show. Recline in comfort as the epic history of Chandela kings is projected against the temple walls, accompanied by dramatic narration that serves as an ideal introduction for tomorrow's explorations."),
                [
                    'Sightseeing Included: Intercity drive, Southern Group of Temples.',
                    'Evening Experience: VIP seating at the Khajuraho Temple Complex Light & Sound Show.',
                    'Overnight Stay: Ultra-Luxury Resort, Khajuraho.',
                    "Meals Included: Breakfast & Multi-cuisine Chef's Table Dinner.",
                ],
            ),
            _day(
                5,
                'KHAJURAHO — MASTERPIECES OF THE WESTERN TEMPLE GROUP',
                ("This morning brings the central highlight of your Luxury Madhya Pradesh Holiday. Alongside a renowned scholar guide, tour the exquisite Western Group of Temples. Spend your morning marveling at the towering Kandariya Mahadeva Temple, an extraordinary representation of cosmic geometry covered in thousands of intricate sculptures depicting deities, mythical beasts, daily court life, and celebrated erotic art panels celebrating worldly joys. Tour the Lakshmana and Vishvanatha temples to understand the incredible civil engineering used over a thousand years ago. In the afternoon, enjoy a short drive out to Raneh Falls. Here, discover an extraordinary 5-kilometer granite canyon displaying vivid shades of red, green, and grey crystalline rock—often celebrated as India's mini Grand Canyon. Scan the riverside for wildlife at the Ken Gharial Sanctuary before returning to your luxury resort for a quiet evening."),
                [
                    'Sightseeing Included: Western Group (Kandariya Mahadeva, Lakshmana, Devi Jagadambi), Raneh Falls Granite Canyon.',
                    'Evening Experience: Private classical sitar demonstration at the resort gardens.',
                    'Overnight Stay: Ultra-Luxury Resort, Khajuraho.',
                    'Meals Included: Gourmet Breakfast & Specialized Regional Dinner.',
                ],
            ),
            _day(
                6,
                'KHAJURAHO TO PANNA NATIONAL PARK — INTO THE TIGER KINGDOM',
                ('Following breakfast, take a short, scenic drive into the dense teak forests of Panna National Park, an elite sanctuary renowned for its thriving Royal Bengal Tiger population. Check into a lavish luxury wilderness lodge positioned on the edges of the reserve. After lunch and an introductory briefing from a master naturalist, board an open-top private 4x4 safari vehicle for your deep-woods jungle safari. Wind through the dramatic valleys of Panna, keeping an eye out for leopards, sloth bears, striped hyenas, and the majestic Bengal Tiger. Watch the forest change colors as the sun goes down, and return to your lodge for a private safari dinner served around a crackling campfire, creating memories that will last a lifetime.'),
                [
                    'Sightseeing Included: Panna Jungle Safari, Wilderness Drive.',
                    'Evening Experience: Campfire Gathering and Star-gazing session led by an expert naturalist guide.',
                    'Overnight Stay: Luxury Wilderness Safari Lodge, Panna.',
                    'Meals Included: Breakfast, Safari Lunch, & Bush Dinner.',
                ],
            ),
            _day(
                7,
                'PANNA TO KHAJURAHO — FINAL SUNRISE SAFARI & DEPARTURE',
                ('Wake up early for a morning hot beverage before entering the national park for a pristine sunrise safari. See the forest wake up as birds fill the canopy and morning mist drifts over the Ken River. This safari provides excellent opportunities to capture wildlife photographs in the beautiful morning light. Return to your lodge for a premium buffet breakfast, and enjoy a relaxed morning. In the afternoon, your private luxury vehicle will transfer you seamlessly back to Khajuraho Airport or Jhansi Station for your journey home. Your premium heritage and wilderness experience concludes here, leaving you with beautiful photos and **unforgettable memories** crafted beautifully by TRAGUIN.'),
                [
                    'Sightseeing Included: Sunrise Jungle Safari, Private Airport/Station Departure Transfer.',
                    "Meals Included: Full Wilderness Breakfast. HANDPICKED PREMIUM & LUXURY ACCOMMODATIONS Your accommodation is an essential part of your travel story. TRAGUIN partners exclusively with properties that maintain exceptional luxury, safety, and heritage charm. Category Gwalior (1N) Orchha (2N) Khajuraho (2N) Panna (1N) DELUXE Neemrana's Deo Bagh Amar Mahal Palace Radisson Jass Khajuraho Ken River Lodge PREMIUM Taj Usha Kiran Palace Orchha Palace Resort Ramada by Wyndham Tented Camp Panna LUXURY Taj Usha Kiran (Suite) Amar Mahal (Luxury Suite) The Lalit Temple View Tashila Tiger Resort ULTRA LUXURY Taj Usha Kiran (Royal) The Orchha Luxury Villas The Lalit (Executive Suite) Taj Pashan Garh Wilderness Lodge PACKAGE INCLUSIONS ✔Premium Stays: 06 Nights elite accommodation across handpicked palaces and safari lodges. ✔Gourmet Dining: Daily breakfast and specialized dinners included at all properties. ✔Luxury Transportation: AC Luxury SUV for all transfers and drives, plus dedicated 4x4 open safaris. ✔Elite Guiding: Private services of local historians and certified park naturalists. ✔TRAGUIN Signatures: Private River High Tea in Orchha and an evening sitar session in Khajuraho. ✔Assistance & Taxes: 24/7 dedicated concierge service from TRAGUIN experts, tolls, parking, and resort taxes. PACKAGE EXCLUSIONS ✘Air / Train Tickets: Main transport fares to Gwalior and from Khajuraho. ✘Monument Fees: Indiv",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Neemrana's Deo Bagh | Amar Mahal Palace | Radisson Jass Khajuraho | Ken River Lodge",
                'Gwalior | Orchha | Khajuraho | Panna',
                '06 Nights',
                'Deluxe',
                'Deluxe Room',
                'Breakfast & Dinner',
                4,
                1,
            ),
            _hotel(
                'Taj Usha Kiran Palace | Orchha Palace Resort | Ramada by Wyndham | Tented Camp Panna',
                'Gwalior | Orchha | Khajuraho | Panna',
                '06 Nights',
                'Premium',
                'Premium Room',
                'Breakfast & Dinner',
                4,
                2,
            ),
            _hotel(
                'Taj Usha Kiran (Suite) | Amar Mahal (Luxury Suite) | The Lalit Temple View | Tashila Tiger Resort',
                'Gwalior | Orchha | Khajuraho | Panna',
                '06 Nights',
                'Luxury',
                'Luxury Suite',
                'Breakfast & Dinner',
                5,
                3,
            ),
            _hotel(
                'Taj Usha Kiran (Royal) | The Orchha Luxury Villas | The Lalit (Executive Suite) | Taj Pashan Garh Wilderness Lodge',
                'Gwalior | Orchha | Khajuraho | Panna',
                '06 Nights',
                'Ultra Luxury',
                'Royal Suite',
                'Breakfast & Dinner',
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included('Premium Stays: 06 Nights elite accommodation across handpicked palaces and safari lodges.', 1),
            _inc_included('Gourmet Dining: Daily breakfast and specialized dinners included at all properties.', 2),
            _inc_included('Luxury Transportation: AC Luxury SUV for all transfers and drives, plus dedicated 4x4 open safaris.', 3),
            _inc_included('Elite Guiding: Private services of local historians and certified park naturalists.', 4),
            _inc_included('TRAGUIN Signatures: Private River High Tea in Orchha and an evening sitar session in Khajuraho.', 5),
            _inc_included('Assistance & Taxes: 24/7 dedicated concierge service from TRAGUIN experts, tolls, parking, and resort taxes.', 6),
            _inc_excluded('Air / Train Tickets: Main transport fares to Gwalior and from Khajuraho.', 7),
            _inc_excluded('Monument Fees: Individual entry tickets and camera permits at temples and forts.', 8),
            _inc_excluded('Personal Items: Laundry, premium beverages, spa therapies, and personal tips.', 9),
            _inc_excluded('Optional Extras: Optional boat trips, additional safaris, or travel insurance.', 10),
        ],
    )
    return package, itinerary

def build_mp_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MP-010'
    tour_code = 'TG-MP-CMP-010'
    title = 'The Ultimate Central Indian Legacy — Palaces, Forts & Tigers'
    duration = '08 Nights / 09 Days'
    slug = 'mp-010-ultimate-central-indian-legacy-palaces-forts-tigers'
    itin_slug = 'mp-010-ultimate-central-indian-legacy-palaces-forts-tigers-itinerary'
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
            _ph('Serial code MP-010 | TRAGUIN tour code TG-MP-CMP-010', 1),
            _ph('State / Country: Madhya Pradesh, India | Category: Complete Luxury Heritage & Wildlife', 2),
            _ph('Destinations: Gwalior • Orchha • Khajuraho • Panna • Kanha', 3),
            _ph('Ideal for: Families, Culture Seekers & Wildlife Enthusiasts', 4),
            _ph('Best season: October to April', 5),
            _ph('Starting price: On Request (Premium Luxury Tier)', 6),
            _ph('Route: Gwalior (1N) ➔ Orchha (2N) ➔ Khajuraho / Panna (2N) ➔ Kanha National Park (3N)', 7),
            _ph('Vehicle / Meals: Private AC Luxury SUV & Exclusive 4x4 Open Jeeps | Premium MAPAI (Daily Breakfast & Chef-Curated Dinners)', 8),
            _ph('TRAGUIN Curated Experience Note: At TRAGUIN, we excel at transforming regular itineraries into exclusive collections of memories. Our custom touches on this majestic trail include private light and sound shows, a curated twilight high-tea on the shores of the Betwa River, private classical musical performances, and early morning game drives led by senior naturalists deep within the tiger kingdoms.', 9),
            _ph('TRAGUIN Signature Experience: Private riverfront high tea set up elegantly along the Betwa River bank.', 10),
            _ph('Shopping & Local Experiences: Gwalior Patankar Bazaar silks; Orchha Dokra crafts; Khajuraho stone sculptures; Kanha Gond paintings and organic forest honey.', 11),
            _ph('Important: Conservative temple attire. Kanha and Panna safari permits book 60–90 days ahead. Limited inventory at Taj Usha Kiran and Banjaar Tola.', 12),
        ],
        moods=['Family', 'Heritage', 'Wildlife'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='The Ultimate Central Indian Legacy — Palaces, Forts & Tigers • 08 Nights / 09 Days',
        overview="Welcome to the grand tapestry of Central India. The definitive Best Madhya Pradesh Tour Package, exclusively brought to life by TRAGUIN, invites your loved ones to witness a mesmerizing land where imperial history and untamed nature exist side by side. This masterfully orchestrated Luxury Madhya Pradesh Holiday offers a seamless panoramic sweep across the state's most magnificent assets. Traverse breathtaking landscapes, step inside massive hill-forts, wonder at thousand-year-old temple architecture, and plunge into premier tiger reserves. Every single day of this grand trail has been designed to treat your family to premium stays, deeply immersive experiences, and handpicked hotels, leaving you with nothing less than a lifetime of unforgettable memories.\n\nTOUR OVERVIEW\nThe **Complete M.P.** signature route stands out as the ultimate Madhya Pradesh Family Tour. Over 9 days, it comprehensively captures the majestic northern cultural triangle before carrying your family deep into the world's most celebrated wildlife ecosystems. Starting in the historic royal bastion of Gwalior, you will descend into the romantic medieval village of Orchha, marvel at the UNESCO World Heritage wonders of Khajuraho, scan the rugged gorges of Panna, and culminate in the timeless sal forests of Kanha National Park. Enjoy private luxury ground transportation, elite local scholars, and pre-arranged premium safaris. Travel Dates: Flexible / Private Customized FIT Group Type: Premium Family Vacation Vehicle: Private AC Luxury SUV & Exclusive 4x4 Open Jeeps Meal Plan: Premium MAPAI (Daily Breakfast & Chef-Curated Dinners) Route Plan: Gwalior (1N) ➔ Orchha (2N) ➔ Khajuraho / Panna (2N) ➔ Kanha National Park (3N)\n\nWHY CHOOSE THE COMPLETE MADHYA PRADESH FAMILY TOUR?\nA panoramic journey across Central India provides access to the very best Top Tourist Places in Madhya Pradesh. It remains an unmatched educational and emotional adventure that caters brilliantly to multi- generational family bonding. Famous Attractions: Tour the impenetrable Gwalior Fort, the beautiful Jai Vilas Palace, the stunning multi-layered palaces of Orchha, the world-famous Kandariya Mahadeva temple complex in Khajuraho, and the dense jungles of Panna and Kanha. Most Searched Experiences: Standing before thousand-year-old erotic stone sculptures, listening to the evening Aarti on the Betwa riverbank, tracking majestic Bengal Tigers from open-top 4x4 gypsies, and relaxing around campfires. Family & Luxury Highlights: Staying inside authentic, living palaces managed by Taj, private riverside picnics, interactive workshops for children, and pristine spa retreats for parents. Popular Instagram Locations: The iconic blue-and-yellow tiled facade of Man Singh Palace, sunset over the sharp spires of Chaturbhuj Temple, and raw dramatic landscape shots within the grand crystalline canyon of Raneh Falls. Best Time to Visit Madhya Pradesh: The winter window from October to April features crisp mornings and glorious sunny afternoons, perfect for expansive Madhya Pradesh Sightseeing and rich wildlife photography.\n\nTRAGUIN Curated Experience Note: At TRAGUIN, we excel at transforming regular itineraries into exclusive collections of memories. Our custom touches on this majestic trail include private light and sound shows, a curated twilight high-tea on the shores of the Betwa River, private classical musical performances, and early morning game drives led by senior naturalists deep within the tiger kingdoms.",
        seo_title='MP-010 | The Ultimate Central Indian Legacy — Palaces, Forts & Tigers | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days Madhya Pradesh package (MP-010 / TG-MP-CMP-010): Gwalior, Orchha, Khajuraho, Panna, Kanha safaris, Barasingha, tribal village walk, and 4-tier palace and safari lodge accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Jai Vilas Palace, Gwalior Fort & VIP Gwalior Fort Light & Sound Show', 1),
            _ih('Orchha Fort Complex, Royal Chhatris & private Riverside High Tea on the Betwa River', 2),
            _ih('Khajuraho Southern & Western temples, Raneh Falls & private classical sitar demonstration', 3),
            _ih('Panna forest excursion, scenic drive to Kanha & deep jungle safaris with Baiga tribal village walk', 4),
        ],
        days=[
            _day(
                1,
                'GWALIOR — ARRIVAL & ENTRY INTO THE IMPERIAL STRONGHOLD',
                ('Your grand expedition begins as you touch down in the historic city of Gwalior. Your dedicated TRAGUIN private chauffeur and tour manager welcome you with refreshing amenities, escorting you in style to your handpicked luxury heritage palace hotel. After a seamless check-in and an exquisite lunch, start your Gwalior Sightseeing circuit. Visit the incredible Jai Vilas Palace, a grand 19th-century estate combining Italianate, Tuscan, and Corinthian styles. Gaze up at the massive crystal chandeliers in the Durbar Hall and watch the legendary silver model train deliver fine digestifs across the royal dining table. In the late afternoon, ascend the massive cliff roads up to the historic Gwalior Fort. Explore the majestic blue-and- yellow tiled facades of the Man Mandir Palace. As darkness falls over the valley, enjoy a Premium Gwalior Experience with VIP seating at the Gwalior Fort Sound & Light Show, witnessing history come alive in stone.'),
                [
                    'Sightseeing Included: Jai Vilas Palace, Gwalior Fort, Man Mandir Palace, Saas-Bahu Temples, Teli Ka Mandir.',
                    'Evening Experience: VIP Seating at the Gwalior Fort Light & Sound Show.',
                    'Overnight Stay: Elite Heritage Palace Hotel, Gwalior.',
                    'Meals Included: Welcome Signature Refreshments & Gourmet Palace Dinner.',
                ],
            ),
            _day(
                2,
                'GWALIOR TO ORCHHA — TRANSITION TO THE MEDIEVAL RIVER KINGDOM',
                ('Indulge in a premium breakfast at the palace before initiating a highly scenic driving route south toward the enchanting town of Orchha. Hidden beautifully along the banks of the pristine Betwa River, Orchha looks today exactly as it did under the Bundela kings in the 16th century. Upon arrival, check into an exclusive luxury riverside resort handpicked by TRAGUIN specialists for its unparalleled quietude. After settling in, begin your immersion into the sprawling Orchha Fort Complex. Walk through the vast interior courtyards of the Raja Mahal, adorned with beautiful religious murals, and explore the multi-tiered Jahangir Mahal, an architectural jewel built to honor a single-night imperial visit. As the sky turns amber, gather at the historic Ram Raja Temple—the only shrine in India where Lord Rama is officially worshiped as a king and given a military guard of honor—for a deeply emotional evening Aarti ceremony.'),
                [
                    'Sightseeing Included: Scenic cross-country drive, Raja Mahal, Jahangir Mahal, Camel Stables.',
                    'Evening Experience: Evening Aarti Ceremony at Ram Raja Temple followed by a walk through ancient town markets.',
                    'Optional Activities: Soft river rafting down the Betwa River or an interactive pottery class with local village artisans.',
                    'Overnight Stay: Premium Luxury Riverside Resort, Orchha.',
                    'Meals Included: Buffet Breakfast & Traditional Bundelkhandi Dinner.',
                ],
            ),
            _day(
                3,
                'ORCHHA — THE RIVERSIDE CENOTAPHS & SUNSET HIGH TEA',
                ("Wake up to the refreshing sound of rushing water and forest birdcalls. Today promises a fully immersive day of Orchha Sightseeing wonders. Following breakfast, tour the iconic Orchha Chhatris—fourteen towering stone cenotaphs standing elegantly along the riverbank as memorials to the old rulers. A private expert historian will walk your family through the hidden architectural symbolism written into these monuments. Later, visit the magnificent Chaturbhuj Temple, built atop a massive stone platform. In the afternoon, enjoy a TRAGUIN Signature Experience: a premium high-tea set up elegantly at a private spot right on the shore of the Betwa River. Spend the late evening relaxing at your resort's spa or join an optional, highly recommended river rafting experience floating past the illuminated historic cenotaphs."),
                [
                    'Sightseeing Included: Royal Cenotaphs (Chhatris), Chaturbhuj Temple, Laxminarayan Temple.',
                    'Evening Experience: Private Riverside High Tea and a Sunset Family Photography session.',
                    'Optional Activities: Soft river rafting down the Betwa River or an interactive pottery class with local village artisans.',
                    'Overnight Stay: Premium Luxury Riverside Resort, Orchha.',
                    'Meals Included: Breakfast, Curated High Tea, & Fine Dining Dinner.',
                ],
            ),
            _day(
                4,
                'ORCHHA TO KHAJURAHO — JOURNEY TO THE APEX OF STONE ART',
                ("Following breakfast, bid farewell to Orchha as your private vehicle drives your family toward the world-famous town of Khajuraho. This destination is home to the most iconic highlights of our Best Khajuraho Tour Package: the magnificent UNESCO World Heritage temples. Arrive and check into your premium luxury resort, offering beautiful views of the historic monument gardens. In the afternoon, begin exploring the Southern Group of Temples, including Duladeo and Chaturbhuj temples, known for their slender stone carvings. As dusk falls, attend the Khajuraho Sound and Light Show. Recline in comfort as the epic history of Chandela kings is projected against the temple walls, accompanied by dramatic narration that serves as an ideal introduction for tomorrow's explorations."),
                [
                    'Sightseeing Included: Countryside drive, Southern Group of Temples.',
                    'Evening Experience: VIP seating at the Khajuraho Temple Complex Light & Sound Show.',
                    'Overnight Stay: Ultra-Luxury Resort, Khajuraho.',
                    'Meals Included: Breakfast & Multi-cuisine Fine Dining Dinner.',
                ],
            ),
            _day(
                5,
                'KHAJURAHO — UNESCO HERITAGE MASTERPIECES & CRYSTALLINE CANYONS',
                ("This morning brings the central highlight of your Luxury Madhya Pradesh Holiday. Alongside a renowned scholar guide, tour the exquisite Western Group of Temples. Spend your morning marveling at the towering Kandariya Mahadeva Temple, an extraordinary representation of cosmic geometry covered in thousands of intricate sculptures depicting deities, mythical beasts, daily court life, and celebrated erotic art panels celebrating worldly joys. Tour the Lakshmana and Vishvanatha temples to understand the incredible civil engineering used over a thousand years ago. In the afternoon, enjoy a short drive out to Raneh Falls. Here, discover an extraordinary 5-kilometer granite canyon displaying vivid shades of red, green, and grey crystalline rock—often celebrated as India's mini Grand Canyon. Scan the river for wildlife at the Ken Gharial Sanctuary before returning to your luxury resort for a quiet evening."),
                [
                    'Sightseeing Included: Western Group (Kandariya Mahadeva, Lakshmana, Devi Jagadambi), Raneh Falls Granite Canyon.',
                    'Evening Experience: Private classical sitar demonstration in the resort gardens.',
                    'Overnight Stay: Ultra-Luxury Resort, Khajuraho.',
                    'Meals Included: Gourmet Breakfast & Specialized Regional Dinner.',
                ],
            ),
            _day(
                6,
                'KHAJURAHO TO PANNA & TRANSFER TO THE WILD HEART OF KANHA',
                ('Wake up early for a morning drive out to the adjacent Panna National Park ecosystem for a light forest safari trail. Following breakfast, embark on a long and beautifully scenic cross-country drive or luxury train transition heading south into the deep, legendary forests of the Maikal Hills—the wild domain of Kanha National Park. This is globally celebrated as the setting that inspired Rudyard Kipling’s *The Jungle Book* and is a core pillar of any elite Madhya Pradesh Family Tour. Upon entering the buffer zone of Kanha, check into an ultra-luxury wilderness safari lodge curated carefully by TRAGUIN experts. Enjoy a warm traditional welcome around an open fire, followed by a chef-curated bush dinner while listening to the nocturnal calls of the deep jungle.'),
                [
                    'Sightseeing Included: Excursion through Panna forest roads, scenic drive across Central Indian tribal landscapes to Kanha.',
                    'Evening Experience: Traditional welcome at the safari lodge followed by an educational talk with a senior naturalist.',
                    'Overnight Stay: Ultra-Luxury Wilderness Safari Lodge, Kanha.',
                    'Meals Included: Breakfast, Packed Lunch, & Gourmet Wilderness Dinner.',
                ],
            ),
            _day(
                7,
                'KANHA NATIONAL PARK — DEEP JUNGLE SAFARIS & TIGER TRACKING',
                ('Awake before dawn to the crisp morning air of the forest. Board your private, open-top 4x4 safari gypsy accompanied by a highly experienced forest tracker. Enter the core zone of Kanha National Park just as the sun begins to break through the dense canopy of ancient Sal trees. Drive through the expansive meadows where herds of the rare, hard-ground Barasingha (Swamp Deer)—the absolute pride of Kanha—graze peacefully in the morning mist. Track the fresh pugmarks of the royal Bengal Tiger through the tall grass. Your naturalist will interpret the sharp alarm calls of langurs and spotted deer echoing through the trees. Enjoy a premium packed picnic breakfast inside a designated forest spot. Return to the lodge for lunch and a few hours of relaxation before embarking on your afternoon safari, exploring a different zone of the reserve to optimize your wildlife encounters and capture beautiful photographs.'),
                [
                    'Sightseeing Included: Morning & Afternoon Core Zone Safaris (Kanha/Kisli/Mukki zones).',
                    'Evening Experience: Multi-course campfire dinner accompanied by local tribal folk dances performed under the stars. Meals Included: Forest Picnic Breakfast, Luxury Lodge Lunch, & Campfire Dinner.',
                    'Overnight Stay: Ultra-Luxury Wilderness Safari Lodge, Kanha.',
                    'Meals Included: Forest Picnic Breakfast, Luxury Lodge Lunch, & Campfire Dinner.',
                ],
            ),
            _day(
                8,
                'KANHA — SUNRISE GAME DRIVE & IMMERSIVE TRIBAL WALKS',
                ("Set out on your final morning sunrise safari into Kanha's rich core zones. Focus your lenses on capturing the incredible birdlife, including the golden oriole, racket-tailed drongo, and majestic Indian rollers. After a thrilling morning tracking predators, return to your lodge for a sumptuous lunch. In the afternoon, enjoy a highly immersive cultural walk through an adjacent Baiga tribal village. Learn about their ancient lifestyle, traditional body tattoos, and deep, harmonious connection with the surrounding wilderness. Conclude your last evening in the wilderness with a special TRAGUIN farewell dinner organized in a private corner of the resort grounds, celebrating your family's incredible journey across Central India."),
                [
                    'Sightseeing Included: Morning Sunrise Safari, Baiga Tribal Village Cultural Walk.',
                    'Evening Experience: Private Farewell Theme Dinner with customized family travel souvenirs.',
                    'Overnight Stay: Ultra-Luxury Wilderness Safari Lodge, Kanha.',
                    'Meals Included: Lodge Breakfast, Gourmet Lunch, & Grand Farewell Dinner.',
                ],
            ),
            _day(
                9,
                'KANHA TO JABALPUR / RAIPUR — DEPARTURE WITH LIFELONG MEMORIES',
                ('Indulge in a final, late breakfast at your safari resort while enjoying the beautiful forest views. Take some time to share your favorite moments with your family and pack your bags. Your private luxury vehicle will provide a smooth transfer to Jabalpur Airport (or Raipur Airport) for your onward flight home. Your comprehensive Complete M.P. legacy journey concludes here. Your family leaves with beautiful photographs, deep cultural enrichment, and unforgettable memories crafted flawlessly by the travel specialists at TRAGUIN.'),
                [
                    'Sightseeing Included: Airport / Station Private Departure Transfer.',
                    'Meals Included: Premium Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Hotel Neemrana's Deo Bagh | Amar Mahal Palace (Deluxe) | Radisson Jass Khajuraho | MPT Tiger Resort Kanha",
                'Gwalior | Orchha | Khajuraho | Kanha',
                '08 Nights',
                'Deluxe',
                'Deluxe Room',
                'Breakfast & Dinner',
                4,
                1,
            ),
            _hotel(
                'Taj Usha Kiran (Superior) | Orchha Palace Resort | Ramada by Wyndham | Chitvan Jungle Lodge',
                'Gwalior | Orchha | Khajuraho | Kanha',
                '08 Nights',
                'Premium',
                'Premium Room',
                'Breakfast & Dinner',
                4,
                2,
            ),
            _hotel(
                'Taj Usha Kiran (Executive) | Amar Mahal (Suite Tier) | The Lalit Temple View | Singinawa Jungle Lodge',
                'Gwalior | Orchha | Khajuraho | Kanha',
                '08 Nights',
                'Luxury',
                'Luxury Suite',
                'Breakfast & Dinner',
                5,
                3,
            ),
            _hotel(
                'Taj Usha Kiran (Royal Suite) | The Orchha Luxury Villas | The Lalit (Executive Suite) | Taj Banjaar Tola Safari Lodge',
                'Gwalior | Orchha | Khajuraho | Kanha',
                '08 Nights',
                'Ultra Luxury',
                'Royal Suite',
                'Breakfast & Dinner',
                5,
                4,
            ),
        ],
        inclusions=[
            _inc_included('Premium Stays: 08 Nights elite accommodation across handpicked palaces, luxury hotels, and safari lodges.', 1),
            _inc_included('Gourmet Dining: Daily buffet breakfast and chef-curated multi-course dinners across all properties.', 2),
            _inc_included('Luxury Transportation: Private air-conditioned luxury vehicle for all ground transfers, intercity travel, and sightseeing as per the itinerary.', 3),
            _inc_included('Elite Guiding: Private services of local historians in cultural zones and certified park naturalists during safaris.', 4),
            _inc_included('TRAGUIN Signatures: Private Riverside High Tea in Orchha and an evening sitar musical presentation in Khajuraho.', 5),
            _inc_included('Welcome Amenities: Royal traditional welcomes, fresh honeymoon/anniversary treats, and premium mineral water bottles inside the vehicle daily.', 6),
            _inc_included('Assistance & Taxes: 24/7 dedicated support from TRAGUIN holiday specialists, covered tolls, fuel costs, and driver allowances.', 7),
            _inc_excluded('Air / Train Fares: Intercity transport tickets to Gwalior and from Jabalpur/Raipur.', 8),
            _inc_excluded('Monument Entry Fees: Individual entrance tickets and camera permits at forts and temples.', 9),
            _inc_excluded('Jungle Safari Permits: Core zone gypsy safari permit fees unless explicitly added to final custom pricing.', 10),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, alcoholic beverages, spa therapies, and personal tips.', 11),
        ],
    )
    return package, itinerary

MADHYA_PRADESH_MP_001_010_BUILDERS = [
    build_mp_001,
    build_mp_002,
    build_mp_003,
    build_mp_004,
    build_mp_005,
    build_mp_007,
    build_mp_008,
    build_mp_009,
    build_mp_010,
]
