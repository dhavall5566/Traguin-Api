"""Builder functions for KL-001 through KL-010 Kerala domestic packages."""

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

KERALA_SLUG = "kerala"
KERALA_DESTINATION_ID = "2d170ff5-019f-4284-9eec-a403e2b49749"


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


def build_kl_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-001'
    tour_code = 'TG-KRL-FAM-06D'
    title = 'Munnar • Thekkady • Alleppey • Cochin'
    duration = '05 Nights / 06 Days'
    slug = 'kl-001-munnar-thekkady-alleppey-family'
    itin_slug = 'kl-001-munnar-thekkady-alleppey-family-itinerary'
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
            _ph('Serial code KL-001 | TRAGUIN tour code TG-KRL-FAM-06D', 1),
            _ph('State / Country: Kerala / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Jharkhand', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury air-conditioned Executive Vehicle reserved for your entire journey.', 7),
            _ph('Route: Cochin → Munnar (2N) → Thekkady (1N) → Alleppey (1N) → Cochin (1N)', 8),
            _ph('& TRAVEL GUIDELINES', 9),
            _ph('luxury Alleppey houseboat.', 10)
        ],
        moods=['Family', 'Luxury', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Munnar',
        overview="Immerse your family in the timeless magic of God's Own Country. From the emerald green velvet slopes of the finest tea plantations in Munnar to the pristine, serene waters of Kerala's iconic backwaters, TRAGUIN curates a tapestry of breathtaking landscapes, premium stays, and unforgettable memories tailored exclusively for your loved ones.\n\nTOUR OVERVIEW\nThe TRAGUIN Curated Experience: This bespoke itinerary represents the gold standard of hospitality. We handpick elite premium properties known for exceptional family comfort, safety, and pristine location. Enjoy seamless transfers, localized destination expertise, and personalized, continuous concierge assistance throughout your luxury Kerala holiday. DISCOVER KERALA: THE ULTIMATE PREMIUM DESTINATION EXPERIENCE When searching for the Best Kerala Tour Package or a highly personalized Kerala Family Tour, the timeless allure of southern India's most pristine state stands unmatched. Kerala offers an unmatched spectrum of travel experiences, blending mist-clad mountain peaks, exotic spice sanctuaries, and tranquil aquatic pathways. As a premier destination for a luxury Kerala holiday, it delivers a harmonious blend of nature's scenic beauty and legendary warm hospitality. Route: Cochin → Munnar (2N) → Thekkady (1N) → Alleppey (1N) → Cochin (1N) Vehicle Type: Private Luxury air-conditioned Executive Vehicle reserved for your entire journey. Meal Plan: Royal Breakfast at all premium hotels; All Meals (Breakfast, Lunch, Dinner) included on the Houseboat. TRAGUIN | Premium Travel & Luxury Holidays Our carefully structured TRAGUIN Kerala Packages ensure you unlock the top tourist places in Kerala without the rush. From capturing the iconic, highly searched popular Instagram locations like the rolling tea carpets of Munnar and the architectural wonders of Cochin's Chinese Fishing Nets, to experiencing the deep cultural immersion of traditional Kathakali arts, your family will discover why this is universally hailed as an essential lifetime travel destination. Whether it is your first family vacation or a dedicated Kerala Honeymoon Package, the magical rhythm of the backwaters and fresh mountain breeze offers a profound sense of rejuvenation. YOUR BESPOKE DAY-WISE ITINERARY",
        seo_title='KL-001 | Munnar | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Kerala package (KL-001 / TG-KRL-FAM-06D): Jharkhand with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: COCHIN TO MUNNAR', 1),
            _ih('Day 02: MUNNAR SIGHTSEEING', 2),
            _ih('Day 03: MUNNAR TO THEKKADY', 3),
            _ih('Day 04: THEKKADY TO ALLEPPEY', 4),
            _ih('Day 05: ALLEPPEY TO COCHIN', 5),
            _ih('Day 06: DEPARTURE FROM COCHIN', 6)
        ],
        days=[
            _day(
                1,
                'COCHIN TO MUNNAR',
                (
                    "ASCENT TO THE EMERALD HILLS & WHISPERING CASCADES Your luxury Kerala holiday commences with a warm, personalized reception upon your arrival at Cochin International Airport or Railway Station. Your dedicated TRAGUIN professional chauffeur greets your family and assists with luggage before you step into your executive premium vehicle. Bid farewell to the urban coastal plains as you begin a scenic, winding ascent toward Munnar, the crown jewel of the Western Ghats. The road to Munnar serves as a prelude to the region's breathtaking landscapes. En route, your private vehicle pauses at the spectacular Cheeyappara Waterfalls, which cascade down a seven-tiered rock face, providing an exceptional photography point for your first family portrait. Feel the air turn crisp and cool as you pass Valara Waterfalls, embraced by dense, verdant forests. Upon arriving in Munnar, check into your handpicked ultra-luxury resort overlooking cloud-kissed ridges. Spend a peaceful evening relaxing in your premium room, absorbing the tranquil atmosphere of the hills. Photo Points. authentic Nilgiri tea amidst the evening mist. TRAGUIN | Premium Travel & Luxury Holidays"
                ),
                [
                    'SIGHTSEEING INCLUDED: Cheeyappara Waterfalls, Valara Waterfalls, Panoramic Mountain Passes, Scenic',
                    'EVENING EXPERIENCE: Leisurely walks around the premium resort estate or enjoying a warm cup of',
                    'OVERNIGHT STAY: Premium Resort / Handpicked Hotel in Munnar',
                    'MEALS INCLUDED: Welcome Drink & Gourmet Buffet Dinner',
                ],
            ),
            _day(
                2,
                'MUNNAR SIGHTSEEING',
                (
                    "VALLEYS OF VELVET TEA & THE ETHEREAL ECHOES Awaken to a misty morning and indulge in an opulent breakfast at your resort before embarking on a comprehensive, premium Munnar sightseeing tour. Today's immersive experiences bring you face-to-face with the pristine ecological wonders that make Munnar the most sought-after component of any premium Kerala tour package. Your first stop is the iconic Mattupetty Dam and its pristine reservoir. Here, your family can choose an optional speed-boat ride across the azure waters, framed by steep pine forests. Continue to the enchanting Echo Point, a natural auditory phenomenon where your voice resonates across the placid lake and forested slopes—a lighthearted, joyful experience for children and elders alike. Next, wander through the manicured greenery of Kundala Lake and visit the sprawling, historic Tata Tea Museum to understand the art of tea crafting from leaf to cup. If environmental conditions permit, we visit Eravikulam National Park (Rajamalai), the sacred sanctuary of the endangered Nilgiri Tahr, offering panoramic vistas from the highest peaks. Eravikulam National Park. TRAGUIN | Premium Travel & Luxury Holidays"
                ),
                [
                    'SIGHTSEEING INCLUDED: Mattupetty Dam, Echo Point, Kundala Lake, Tea Museum, Photo Gardens,',
                    'OPTIONAL ACTIVITIES: Speed-boating at Mattupetty, traditional paddle-boating on Kundala Lake, or',
                    'shopping: for rare exotic oils.',
                    'OVERNIGHT STAY: Premium Resort / Handpicked Hotel in Munnar',
                    'MEALS INCLUDED: Sumptuous Breakfast & Elegant Dinner',
                ],
            ),
            _day(
                3,
                'MUNNAR TO THEKKADY',
                (
                    'JOURNEY INTO THE HEARTLAND OF SPICES & WILDERNESS Following a rich breakfast, check out of Munnar and chart a southerly path through spice-laden hills to Thekkady (Periyar), India’s premier wildlife and spice sanctuary. The drive itself is an immersive sensory experience, where the aroma of fresh cardamom, black pepper, and clove trees wafts naturally through your windows. Arrive in Thekkady and settle into your premium boutique resort, which blends seamlessly with the surrounding wilderness. In the afternoon, TRAGUIN takes you on an exclusive, guided Spice Plantation Tour. A knowledgeable local expert walks you through plantations to touch, taste, and learn about organic cultivation methods of world-famous Kerala spices. As the sun dips below the horizon, witness a breathtaking, powerful performance of Kathakali (the traditional classical dance-drama of Kerala) or Kalaripayattu (one of the oldest ancient martial arts in the world) at a cultural center, showcasing incredible artistry and storytelling. TRAGUIN | Premium Travel & Luxury Holidays'
                ),
                [
                    'SIGHTSEEING INCLUDED: Spice Plantation Walk, Periyar Wilderness Outskirts, High-Range Viewpoints.',
                    'EVENING EXPERIENCE: Live traditional Kathakali performance & vibrant Kalaripayattu martial arts show.',
                    'OVERNIGHT STAY: Premium Wilderness Resort in Thekkady',
                    'MEALS INCLUDED: Breakfast & Multi-cuisine Buffet Dinner',
                ],
            ),
            _day(
                4,
                'THEKKADY TO ALLEPPEY',
                (
                    "THE ULTIMATE HOUSEBOAT CRUISE IN LIQUID SANCTUARY Savor an early breakfast before checking out for the piece de resistance of your trip: the pristine backwaters of Alleppey. Arrive at the private jetty by noon to a traditional, warm welcome aboard your private, ultra-luxury TRAGUIN houseboat. Constructed using eco-friendly bamboo, coir, and local wood, your floating palace features fully air-conditioned bedrooms, ensuite modern bathrooms, and a magnificent open deck. As your private vessel glides effortlessly onto the calm waters of Vembanad Lake, the world slows to a beautiful crawl. Observe the unique local life of rural Kerala—children canoeing to school, fishermen balancing on narrow country boats, and endless rows of swaying coconut palms reflecting perfectly on the water's surface. Your on-board private chef prepares an extraordinary, authentic lunch featuring local delicacies like Karimeen Pollichathu (pearl spot fish) and traditional red rice. Watch the dramatic sunset turn the waters into gold before anchoring in a tranquil bay for a peaceful night under the stars. Vistas. canal stops. fresh onboard. TRAGUIN | Premium Travel & Luxury Holidays"
                ),
                [
                    'SIGHTSEEING INCLUDED: Vembanad Lake, Alleppey Backwater Canals, Remote Riverine Islands, Paddy Field',
                    'OPTIONAL ACTIVITIES: Ayurvedic Rejuvenation Massage at a premium backwater spa facility during brief',
                    'OVERNIGHT STAY: Private Luxury Air-Conditioned Houseboat (Anchored)',
                    'MEALS INCLUDED: Full Board: Traditional Lunch, High Tea with snacks, Dinner, and Breakfast cooked',
                ],
            ),
            _day(
                5,
                'ALLEPPEY TO COCHIN',
                (
                    'COLONIAL ECHOES & COASTAL CHARM OF HISTORIC FORT KOCHI Enjoy a breakfast served on the deck of your houseboat as it cruises back to the mainland jetty. Disembark and travel comfortably back to Cochin—the historic "Queen of the Arabian Sea." Check into your elite luxury city hotel and prepare to explore one of India\'s richest heritage hubs. In the afternoon, your chauffeured vehicle guides you through the historic quarter of Fort Kochi. Stand in awe before the massive, iconic Chinese Fishing Nets, an ancient mechanical fishing method that remains highly photographed at sunset. Stroll down cobblestone pathways to the St. Francis Church, the oldest European-built church in India where Vasco da Gama was originally buried. Explore the vibrant Jew Town, visit the historic Paradesi Synagogue, and marvel at the mythological murals inside the Mattancherry Dutch Palace. Conclude your day with some premium shopping for exquisite souvenirs. Mattancherry Dutch Palace, Jew Town. witness the city lights.'
                ),
                [
                    'SIGHTSEEING INCLUDED: Fort Kochi Beach, Chinese Fishing Nets, St. Francis Church, Santa Cruz Basilica,',
                    'EVENING EXPERIENCE: Leisurely café hopping in Fort Kochi or walking along the Marine Drive promenade to',
                    'OVERNIGHT STAY: Premium / Ultra-Luxury Hotel in Cochin',
                    'MEALS INCLUDED: Gourmet Breakfast & Farewell Dinner',
                ],
            ),
            _day(
                6,
                'DEPARTURE FROM COCHIN',
                (
                    'CHERISHED MEMORIES BEYOND HORIZONS Your exceptional TRAGUIN Kerala Package concludes today. Indulge in a final, luxurious buffet breakfast at your hotel and enjoy some relaxed leisure time during the morning. You can use this time for any last- minute shopping for high-quality tea leaves, handpicked organic spices, banana chips, or authentic Kerala handloom garments. At the designated hour, your private executive vehicle will transfer your family smoothly to Cochin International Airport or the railway station. As you prepare for your journey homeward, look back fondly on your week filled with breathtaking landscapes, premium stays, deep cultural immersion, and unforgettable memories curated with perfection by TRAGUIN experts. TRAGUIN | Premium Travel & Luxury Holidays'
                ),
                [
                    'SIGHTSEEING INCLUDED: Lulu Mall (optional for international-brand shopping) or local Cochin markets.',
                    'MEALS INCLUDED: Grand Institutional Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Leaf Munnar / Amber Dale | Elephant Court / Poetree | Premium AC Houseboat (Private) | Trident Cochin / Radisson',
                'Munnar | Thekkady | Alleppey | Cochin',
                '2N Munnar|1N Thekkady|1N Alleppey|1N Cochin',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: The Leaf Munnar / Amber Dale | Elephant Court / Poetree | Premium AC Houseboat (Private) | Trident Cochin / Radisson | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Blanket Hotel / Fragrant Nature | Greenwoods Resort / Spice Village | Luxury Glass-Walled Houseboat | Crowne Plaza / Marriott',
                'Munnar | Thekkady | Alleppey | Cochin',
                '2N Munnar|1N Thekkady|1N Alleppey|1N Cochin',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Blanket Hotel / Fragrant Nature | Greenwoods Resort / Spice Village | Luxury Glass-Walled Houseboat | Crowne Plaza / Marriott | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                "Chandy's Windy Woods / Panoramic Getaway | The Niraamaya Retreats Cardamom Club | Ultra-Luxury Suite Houseboat | Grand Hyatt Bol",
                'Munnar | Thekkady | Alleppey | Cochin',
                '2N Munnar|1N Thekkady|1N Alleppey|1N Cochin',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description="OPTION 03 – LUXURY: Chandy's Windy Woods / Panoramic Getaway | The Niraamaya Retreats Cardamom Club | Ultra-Luxury Suite Houseboat | Grand Hyatt Bolgatty / Le Meridien | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                'The Panoramic Getaway (Presidential) | Spice Village (Private Pool Villa) | TRAGUIN Signature Royal Houseboat | Brunton Boatyard',
                'Munnar | Thekkady | Alleppey | Cochin',
                '2N Munnar|1N Thekkady|1N Alleppey|1N Cochin',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Panoramic Getaway (Presidential) | Spice Village (Private Pool Villa) | TRAGUIN Signature Royal Houseboat | Brunton Boatyard / Taj Malabar Resort | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Houseboat Experience: Private, fully air-conditioned luxury houseboat stay.', 1),
            _inc_included('Gourmet Meal Plan: Daily extensive breakfasts, all meals included on the Houseboat.', 2),
            _inc_included('Chauffeured Vehicle: Private AC Executive Sedan or SUV for all transfers and sightseeing.', 3),
            _inc_included('Welcome Amenities: Personalized welcome drinks, fruit basket, and local specialties upon check-in.', 4),
            _inc_included('Complimentary Experiences: Guided Spice Plantation walk and entry tickets to cultural evening shows.', 5),
            _inc_included('All Taxes & Tolls: Inclusive of fuel charges, interstate taxes, toll fees, and driver allowances.', 6),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest relations manager available on call.', 7),
            _inc_included('Airfare/Rail Tickets: Inbound and outbound long- distance transit costs.', 8),
            _inc_excluded('Premium Accommodation: Double sharing rooms in top-reviewed properties.', 9),
            _inc_excluded('Monuments Entry Fees: Camera fees, activity charges, and specialized local site guide fees.', 10),
            _inc_excluded('Optional Activities: Speed-boating, elephant safaris, jeep rides, and adventure sports.', 11),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, alcoholic beverages, and mini-bar consumption.', 12),
            _inc_excluded('Surcharges: Festival/peak season surcharges if applicable during specific calendar blocks.', 13),
            _inc_excluded('Insurance: Travel or comprehensive medical insurance policies.', 14),
        ],
    )
    return package, itinerary

def build_kl_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-002'
    tour_code = 'TG-KRL-GRD-08D'
    title = 'Cochin • Munnar • Thekkady • Alleppey • Kovalam'
    duration = '07 Nights / 08 Days'
    slug = 'kl-002-cochin-munnar-kovalam-grand-family'
    itin_slug = 'kl-002-cochin-munnar-kovalam-grand-family-itinerary'
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
            _ph('Serial code KL-002 | TRAGUIN tour code TG-KRL-GRD-08D', 1),
            _ph('State / Country: Kerala / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Jharkhand', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury air-conditioned Executive SUV/Van exclusively assigned for your family party.', 7),
            _ph('Route: Cochin (1N) → Munnar (2N) → Thekkady (1N) → Alleppey (1N) → Kovalam (2N) → Trivandrum Drop', 8),
            _ph('& TRAVEL GUIDELINES', 9)
        ],
        moods=['Family', 'Luxury', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Cochin',
        overview='Cochin • Munnar • Thekkady • Alleppey • Kovalam Embark on a grand exploratory odyssey across God\'s Own Country. From colonial history and cloud-swept high-altitude tea valleys to pristine spice forests, peaceful houseboats, and majestic golden beach sunrises, TRAGUIN orchestrates a seamless masterpiece of curated experiences, premium stays, and unforgettable memories for your family.\n\nTOUR OVERVIEW\nThe TRAGUIN Signature Promise: This comprehensive grand exploration represents our highest standard of elite holiday curation. Your family will enjoy handpicked hotels renowned for supreme scenic beauty, elite localized guidance, VIP entries, and our continuous, personalized 24/7 concierge support network throughout your entire luxury Kerala holiday.\n\nWHY VISIT GOD\'S OWN COUNTRY: THE GRAND PREMIUM DESTINATION\nEXPERIENCE When searching for the absolute Best Kerala Tour Package or planning a timeless Kerala Family Tour, the comprehensive "hills-to-beach" grand route remains unmatched. Kerala encompasses an unparalleled spectrum of micro-climates and environments, effortlessly shifting from historic spice ports and mist-shrouded Route: Cochin (1N) → Munnar (2N) → Thekkady (1N) → Alleppey (1N) → Kovalam (2N) → Trivandrum Drop Vehicle Type: Private Luxury air-conditioned Executive SUV/Van exclusively assigned for your family party. Meal Plan: Extensive daily gourmet buffet breakfasts at luxury resorts; All meals included fresh onboard the private houseboat. TRAGUIN | Premium Travel & Luxury Holidays mountain ridges to serene backwater networks and world-class resort cliffs. It is this multi-faceted terrain that establishes it as a bucket-list destination for an immersive luxury Kerala holiday. Our signature TRAGUIN Kerala Packages ensure your family uncovers top tourist places in Kerala with unhurried grace. Explore famous attractions including the historical quarters of Fort Kochi, the endangered Nilgiri Tahr sanctuaries of Munnar, Periyar\'s wild elephant reserves, and the popular Instagram locations like the massive crescent beaches of Kovalam. This circuit perfectly matches the requirements for a romantic Kerala Honeymoon Package or an expansive cross-generational family reunion, offering authentic culture, culinary artistry, and unparalleled photographic points at every turn. YOUR BESPOKE DAY-WISE ITINERARY',
        seo_title='KL-002 | Cochin | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Kerala package (KL-002 / TG-KRL-GRD-08D): Jharkhand with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN COCHIN & HERITAGES OF FORT KOCHI', 1),
            _ih('Day 02: COCHIN TO MUNNAR', 2),
            _ih('Day 03: MUNNAR HILL EXPLORATION', 3),
            _ih('Day 04: MUNNAR TO THEKKADY', 4),
            _ih('Day 05: THEKKADY TO ALLEPPEY', 5),
            _ih('Day 06: ALLEPPEY TO KOVALAM', 6),
            _ih('Day 07: KOVALAM BEACH & TRIVANDRUM HERITAGE EXPLORATION', 7),
            _ih('Day 08: KOVALAM TO TRIVANDRUM & DEPARTURE', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN COCHIN & HERITAGES OF FORT KOCHI',
                (
                    'GATEWAY TO THE QUEEN OF THE ARABIAN SEA Your grand Kerala family tour begins with an elegant VIP welcome right upon your arrival at Cochin International Airport or Railway Station. Your designated TRAGUIN premium chauffeur greets your family, supervises luggage handling, and drives you in absolute comfort to your luxury urban hotel. After checking in and refreshing, step out to experience the multi-cultural colonial tapestry of Fort Kochi. Stroll past the massive, iconic Chinese Fishing Nets, erected centuries ago and still fully functional along the shoreline. Explore the historic Jew Town, admire the antique crystal chandeliers of the Paradesi Synagogue, and tour the Mattancherry Dutch Palace to view ancient royal artifacts and detailed mythological murals. Conclude the day at St. Francis Church, the historic final resting place of explorer Vasco da Gama. Kochi Heritage Pathways. Fort Kochi. TRAGUIN | Premium Travel & Luxury Holidays'
                ),
                [
                    'SIGHTSEEING INCLUDED: Chinese Fishing Nets, Jew Town, Paradesi Synagogue, Mattancherry Palace, Fort',
                    'EVENING EXPERIENCE: A pleasant sunset ferry ride or walking down the vibrant, café-lined walkways of old',
                    'OVERNIGHT STAY: Premium Oceanfront Hotel in Cochin',
                    'MEALS INCLUDED: Welcome Amenities & Grand Welcoming Dinner',
                ],
            ),
            _day(
                2,
                'COCHIN TO MUNNAR',
                (
                    "JOURNEY INTO CLOUD-KISSED TEA HORIZONS Indulge in a magnificent breakfast at your hotel before checking out and shifting your route eastward toward Munnar—the magnificent tea capital of Southern India. Leaving the coast, your premium vehicle navigates gentle winding mountain passes that display some of the Western Ghats' most breathtaking landscapes. Pause along the scenic mountain route to witness the spectacular Cheeyappara Waterfalls cascading across natural rocky shelves. A few kilometers ahead, witness the Valara Waterfalls nestled inside deep, dense sub-tropical woods. As you ascend further, notice the air transform into a crisp, invigorating chill. Arrive at your ultra-luxury hill resort, settle into your premium suite, and watch the evening mist roll gracefully across the valley. Bridge. TRAGUIN | Premium Travel & Luxury Holidays"
                ),
                [
                    'SIGHTSEEING INCLUDED: Cheeyappara Waterfalls, Valara Waterfalls, Adimali Spice Markets, Neriamangalam',
                    'PHOTOGRAPHY POINTS: Panoramic mountain gaps and early-evening mist settling over high-altitude valleys.',
                    'OVERNIGHT STAY: Handpicked Luxury Tea Resort in Munnar',
                    'MEALS INCLUDED: Gourmet Breakfast & Fine-Dining Buffet Dinner',
                ],
            ),
            _day(
                3,
                'MUNNAR HILL EXPLORATION',
                (
                    'VALLEYS OF VELVET GREENERY & NATURAL ECHOES Wake up to a pristine mountain sunrise and enjoy a hearty breakfast. Today, TRAGUIN unlocks the finest natural treasures of Munnar. Your private vehicle moves toward the serene Mattupetty Dam, where the calm water reservoir reflects deep green pine forests. Here, enjoy an exciting private speed-boat tour across the lake. Continue to the natural acoustic theater of Echo Point, a favorite spot for families to listen to their voices reverberate across the mountain slopes. Visit Kundala Lake to see its historic arch dam, followed by a guided tour of the Tata Tea Museum to observe classical tea processing and sample premium infusions. Later, visit Eravikulam National Park, the protected sanctuary where you can catch rare glimpses of the majestic Nilgiri Tahr mountain goats roaming high-altitude grasslands. program. Park. TRAGUIN | Premium Travel & Luxury Holidays'
                ),
                [
                    'Optional Activities: Private speed-boating, estate tea shopping, or an optional elephant interaction',
                    'SIGHTSEEING INCLUDED: Mattupetty Dam, Echo Point, Kundala Arch Lake, Tea Museum, Eravikulam National',
                    'OVERNIGHT STAY: Handpicked Luxury Tea Resort in Munnar',
                    'MEALS INCLUDED: Resort Breakfast & Curated Theme Dinner',
                ],
            ),
            _day(
                4,
                'MUNNAR TO THEKKADY',
                (
                    "SPICE SANCTUM & WILD PERIYAR WOODLANDS After breakfast, check out of your resort and travel south toward Thekkady, India's legendary spice capital. This highway journey is flanked by vast cardamom hills and pepper vines, turning your drive into an incredible sensory experience. Arrive at your wilderness resort and settle into your premium cottage. In the afternoon, join a resident botanist for an exclusive, private Spice Plantation Tour. Discover how gourmet vanilla, cinnamon, nutmeg, and organic ginger are cultivated and harvested. As twilight falls, take your seats at the cultural center for a powerful presentation of Kalaripayattu, the ancient martial art form, followed by an elegant Kathakali dance-drama performance that highlights epic mythological storytelling."
                ),
                [
                    'SIGHTSEEING INCLUDED: Periyar Forest Borders, Cardamom Estates, Local Handicraft Centers.',
                    'EVENING EXPERIENCE: VIP seating for authentic Kathakali and Kalaripayattu cultural performances.',
                    'OVERNIGHT STAY: Premium Wilderness Resort in Thekkady',
                    'MEALS INCLUDED: Full Breakfast & Authentic High-Range Dinner',
                ],
            ),
            _day(
                5,
                'THEKKADY TO ALLEPPEY',
                (
                    'FLOATING PALACES & TRANQUIL LIQUID ROADS Enjoy an early breakfast before departing the highlands for the classic centerpiece of your luxury vacation: the emerald backwaters of Alleppey. Arrive at the private lake jetty by noon to step directly aboard your exclusive, ultra-luxury private TRAGUIN houseboat. Your floating home features fully air-conditioned living spaces, plush bedrooms, and an expansive open observation deck. As the boat cruises smoothly onto Vembanad Lake, enjoy a fresh gourmet lunch prepared by your onboard private chef. Glide past rural lakeside villages, ancient temples, and vast emerald paddy fields. Watch the golden sunset over the calm waters before anchoring in a peaceful canal bay for a quiet night. the horizon. TRAGUIN | Premium Travel & Luxury Holidays'
                ),
                [
                    'SIGHTSEEING INCLUDED: Vembanad Lake, Alleppey Main Canals, Village Lagoons, Kuttanad Paddy Basins.',
                    'EVENING EXPERIENCE: Relaxing on the open deck with fresh local snacks and hot tea as the sun dips below',
                    'OVERNIGHT STAY: Private Luxury Air-Conditioned Houseboat (Anchored)',
                    'MEALS INCLUDED: Full Onboard Boarding (Breakfast, Lunch, High Tea & Dinner)',
                ],
            ),
            _day(
                6,
                'ALLEPPEY TO KOVALAM',
                (
                    "SOUTHERN TRANSIT TO THE MAJESTIC CRESCENT CLIFFS Wake up to the gentle lapping of waves against the hull. Enjoy a fresh breakfast on deck as your houseboat completes its morning loop back to the mainland jetty. Disembark and reunite with your private chauffeur to head south along the scenic coastal highway toward Kovalam—one of India's most iconic beach destinations. Arrive at Kovalam in the afternoon and check into your elite cliff-top luxury resort, which commands uninterrupted views of the Arabian Sea. Spend the afternoon relaxing in your premium room or walking along the soft sands of Lighthouse Beach, named after the prominent red-and-white striped Vizhinjam Lighthouse that watches over the rocky bay."
                ),
                [
                    'SIGHTSEEING INCLUDED: Lighthouse Beach, Hawah Beach, Coastal Highway Lookouts.',
                    'OPTIONAL ACTIVITIES: Climbing the Vizhinjam Lighthouse tower for sweeping, birds-eye coastal views.',
                    'OVERNIGHT STAY: Premium Cliffside Beach Resort in Kovalam',
                    'MEALS INCLUDED: Fresh Houseboat Breakfast & Coastal Resort Dinner',
                ],
            ),
            _day(
                7,
                'KOVALAM BEACH & TRIVANDRUM HERITAGE EXPLORATION',
                (
                    "ROYAL SPIRIT OF THE CAPITAL CITY & SUNSET SANDS Enjoy a beautiful beachside breakfast before taking a short drive to Trivandrum, the historic capital city of the Travancore Royal Family. Today combines majestic royal architecture with relaxing beachside luxury. Stand in awe before the towering, gold-gilded structure of the Sree Padmanabhaswamy Temple, globally renowned for its architectural grandeur. Next, explore the Kuthira Malika Palace (Horse Palace), featuring rare wood carvings and royal family collections. Return to Kovalam in the afternoon to relax on the beach or experience an authentic, deeply relaxing Ayurvedic family body massage at your resort's wellness center. Napier Museum grounds. crashing waves. TRAGUIN | Premium Travel & Luxury Holidays"
                ),
                [
                    'SIGHTSEEING INCLUDED: Sree Padmanabhaswamy Temple (outer structures/entry), Kuthira Malika Palace,',
                    'EVENING EXPERIENCE: A private family celebration dinner arranged right on the beach sands, serenaded by',
                    'OVERNIGHT STAY: Premium Cliffside Beach Resort in Kovalam',
                    'MEALS INCLUDED: Gourmet Breakfast & Farewell Seafood Dinner',
                ],
            ),
            _day(
                8,
                'KOVALAM TO TRIVANDRUM & DEPARTURE',
                (
                    'ENDLESS HORIZONS & CHERISHED MEMORIES Enjoy a relaxed morning breakfast overlooking the azure ocean. Take some time for a final swim in the infinity pool or a stroll down the beach. Complete your check-out formalities at noon. Your premium chauffeur will transfer your family smoothly to Trivandrum International Airport or Kochuveli Railway Station. As you prepare for your departure, take along a collection of unforgettable memories, shared smiles, and beautiful stories curated to perfection by your trusted travel partner, TRAGUIN. flight timeline.'
                ),
                [
                    'TRANSFERS INCLUDED: Direct private executive transfer to Trivandrum Airport / Station according to your',
                    'MEALS INCLUDED: Grand Institutional Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Trident / Radisson | The Leaf / Amber Dale | Elephant Court / Poetree | Premium Private Houseboat | Isola Di Cocco / Travancore',
                'Cochin | Munnar | Thekkady | Alleppey | Kovalam',
                '1N Cochin|2N Munnar|1N Thekkady|1N Alleppey|2N Kovalam',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Trident / Radisson | The Leaf / Amber Dale | Elephant Court / Poetree | Premium Private Houseboat | Isola Di Cocco / Travancore | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Crowne Plaza / Marriott | Blanket Hotel / Fragrant Nature | Greenwoods / Spice Village | Luxury Glass-Walled Cruise | Turtle on ',
                'Cochin | Munnar | Thekkady | Alleppey | Kovalam',
                '1N Cochin|2N Munnar|1N Thekkady|1N Alleppey|2N Kovalam',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Crowne Plaza / Marriott | Blanket Hotel / Fragrant Nature | Greenwoods / Spice Village | Luxury Glass-Walled Cruise | Turtle on the Beach / Travancore | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                "Grand Hyatt Bolgatty Resort | Chandy's Windy Woods Luxury | Niraamaya Cardamom Club | Ultra-Luxury Private Suite Boat | The Leel",
                'Cochin | Munnar | Thekkady | Alleppey | Kovalam',
                '1N Cochin|2N Munnar|1N Thekkady|1N Alleppey|2N Kovalam',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description="OPTION 03 – LUXURY: Grand Hyatt Bolgatty Resort | Chandy's Windy Woods Luxury | Niraamaya Cardamom Club | Ultra-Luxury Private Suite Boat | The Leela Kovalam (Garden Suite) | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                'Brunton Boatyard / Taj Malabar | The Panoramic Getaway (Suites) | Spice Village (Private Pool Villa) | TRAGUIN Signature Royal B',
                'Cochin | Munnar | Thekkady | Alleppey | Kovalam',
                '1N Cochin|2N Munnar|1N Thekkady|1N Alleppey|2N Kovalam',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Brunton Boatyard / Taj Malabar | The Panoramic Getaway (Suites) | Spice Village (Private Pool Villa) | TRAGUIN Signature Royal Boat | The Leela Kovalam (Club Ocean View) | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Explore the vibrant local culture through authentic shopping recommendations. Your private chauffeur will comfortably guide you to trusted local markets and government-approved emporiums: Luxury Resort Stays: Double sharing accommodation in handpicked properties.', 1),
            _inc_included('Houseboat Sailing: Fully private, premium air- conditioned backwater houseboat cruise.', 2),
            _inc_included('Fine Dining: Daily multi-cuisine breakfast spreads, plus all meals fresh onboard the houseboat.', 3),
            _inc_included('Executive Fleet: Dedicated private AC Executive Vehicle for all transfers, drives, and sightseeing.', 4),
            _inc_included('VIP Welcome: Personalized greeting, refresh face towels, and fresh seasonal fruit platter on arrival.', 5),
            _inc_included('Cultural Entrées: Pre-booked entry access to traditional Kathakali and Kalaripayattu theater shows.', 6),
            _inc_included('All-Inclusive Handling: Fully covers fuel, road taxes, interstate permits, parking, tolls, and driver allowances.', 7),
            _inc_included('Airfare/Rail tickets: Inbound and outbound long- distance interstate transit.', 8),
            _inc_excluded('Monument entry costs: Direct temple entry tickets, camera fees, or local localized site guides.', 9),
            _inc_excluded('Adventure Activities: Optional speed-boating, elephant rides, jeep trekking, or watersports.', 10),
            _inc_excluded('Personal Extras: Laundry, telephone calls, room service snacks, and alcoholic beverages.', 11),
            _inc_excluded('Seasonal Surcharges: Peak calendar blocks or mandatory holiday gala dinner supplements.', 12),
            _inc_excluded('Medical Coverage: Comprehensive medical or personal travel cancellation insurance.', 13),
        ],
    )
    return package, itinerary

def build_kl_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-003'
    tour_code = 'TRAGUIN-MNNR-05'
    title = 'Munnar • Kochi Family Getaway'
    duration = '04 Nights / 05 Days'
    slug = 'kl-003-munnar-kochi-family'
    itin_slug = 'kl-003-munnar-kochi-family-itinerary'
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
            _ph('Serial code KL-003 | TRAGUIN tour code TRAGUIN-MNNR-05', 1),
            _ph('State / Country: Kerala / India | Category: Premium Family Tour Package', 2),
            _ph('Destinations: Kochi • Munnar • Kochi', 3),
            _ph('Ideal for: Families, Couples, Leisure Travelers', 4),
            _ph('Best season: September to March', 5),
            _ph('Starting price: On Request (Premium Tier)', 6),
            _ph('Vehicle / Meals: Private Luxury Innova Crysta', 7),
            _ph('Route: Cochin International Airport → Kochi → Munnar (3 Nights) → Kochi (1 Night) → Departure', 8),
            _ph('TRAGUIN Signature Experience: Private, high-tea set up at an exclusive scenic viewpoint in Munnar', 9),
            _ph('Curated by Experts: Fully customizable pacing, flexible timing, and multi-generational family-friendly', 10),
            _ph('TRAGUIN Premium Luxury Holidays', 11),
            _ph('Premium Handpicked Hotels: Properties holding excellent safety, premium culinary, and top-tier', 12)
        ],
        moods=['Family', 'Luxury', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Tier)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Munnar',
        overview="Welcome to an enchanting world of emerald hill stations, misty mountains, and timeless colonial charm. Carefully structured for sophisticated travelers, this Best Kerala Tour Package delivers an immersive journey through the breathtaking landscapes of God's Own Country. From the historic spice ports of Kochi to the endless rolling tea estates of Munnar, every aspect of your holiday is curated to provide unforgettable memories. Experience a seamless fusion of natural scenic beauty, handpicked hotels, and customized local sightseeing designed exclusively for your family's ultimate comfort and relaxation.\n\nTOUR OVERVIEW\nThis exclusive family tour connects the historical coastal city of Kochi with the mist-laden peaks of Munnar. Travel in absolute luxury with a dedicated private vehicle, stay at the finest premium properties, and savor exquisite culinary spreads throughout your journey. Route: Cochin International Airport → Kochi → Munnar (3 Nights) → Kochi (1 Night) → Departure Meal Plan: Modified American Plan (Daily Premium Buffet Breakfast & Dinner) TRAGUIN Curated Experience Note: Your vacation features handpicked boutique resorts, private chauffeur-driven luxury transit, fast-track sightseeing entry clearances, and personalized multi- generational family activities meticulously arranged by TRAGUIN travel experts. TRAGUIN Premium Luxury Holidays Page 1\n\nWHY VISIT KERALA? – DESTINATION INSIGHTS & SEO HIGHLIGHTS\nKerala remains India's premier destination for luxury family vacations and romantic escapes. A Kerala Honeymoon Package or Kerala Family Tour opens up a world of rich cultural tapestry, refreshing mountain air, and unparalleled tranquility. Munnar, the crown jewel of Western Ghats, is globally renowned for its sweeping tea plantations, rare flora like the Neelakurinji, and cascading waterfalls, making it one of the most searched experiences in Asian tourism. Capture gorgeous family portraits at popular Instagram locations like the Lock Heart Gap, Mattupetty Dam, and the historical streets of Fort Kochi. Whether you seek soft adventure trekking at Eravikulam National Park, therapeutic Ayurvedic wellness sessions, or premium shopping for authentic spices and traditional handloom silk, this Premium Kerala Experience satisfies every travel desire perfectly. DAY WISE ITINERARY",
        seo_title='KL-003 | Munnar | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Kerala package (KL-003 / TRAGUIN-MNNR-05): Kochi • Munnar • Kochi with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: KOCHI TO MUNNAR', 1),
            _ih('Day 02: MUNNAR SIGHTSEEING', 2),
            _ih('Day 03: MUNNAR OFFBEAT EXPERIENCES', 3),
            _ih('Day 04: MUNNAR TO KOCHI', 4),
            _ih('Day 05: KOCHI DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private, high-tea set up at an exclusive scenic viewpoint in Munnar', 6),
            _ih('Curated by Experts: Fully customizable pacing, flexible timing, and multi-generational family-friendly', 7),
            _ih('TRAGUIN Premium Luxury Holidays', 8)
        ],
        days=[
            _day(
                1,
                'KOCHI TO MUNNAR',
                (
                    'ARRIVE IN COCHIN & ASCEND TO THE MISTY HILLS OF MUNNAR Arrive at the Cochin International Airport where your professional TRAGUIN tour representative warmly welcomes you. Step into your private luxury vehicle and commence a highly scenic drive toward Munnar, the ultimate destination for a Luxury Kerala Holiday. As you ascend into the Western Ghats, the air transforms into a crisp, refreshing breeze, and the urban landscape gives way to endless canopies of green. En route, enjoy beautiful photography points at the majestic Cheeyappara and Valara Waterfalls, tumbling down rocky cliffs amidst lush forests. Pass through local spice villages where the aroma of fresh cardamom, pepper, and vanilla fills the air. Upon arrival in Munnar, complete a seamless check-in at your handpicked luxury resort. Spend the evening relaxing on your private balcony, taking in the breathtaking landscapes of the surrounding cloud-kissed mountains.'
                ),
                [
                    'Sightseeing Included: Cheeyappara Waterfalls, Valara Waterfalls, Spice Plantation viewpoints.',
                    'Evening Experience: Leisurely resort walk, high tea overlooking valleys, and traditional welcome dinner.',
                    'Optional Activities: Traditional Ayurvedic rejuvenation massage at the resort spa.',
                    'Overnight Stay: Munnar (Premium/Luxury Resort)',
                    'Meals Included: Dinner',
                ],
            ),
            _day(
                2,
                'MUNNAR SIGHTSEEING',
                (
                    'EXPLORING THE TEA EMPIRE & ICONIC ATTRACTIONS OF MUNNAR Wake up to a glorious mountain sunrise and enjoy a sumptuous buffet breakfast. Today is dedicated to comprehensive Munnar Sightseeing, discovering why this region is crowned among the top tourist places in Kerala. Drive first to the famous Eravikulam National Park (Rajamalai), the natural sanctuary of the TRAGUIN Premium Luxury Holidays Page 2 endangered Nilgiri Tahr. Ride the eco-friendly park transit up the slopes and enjoy a light trek enveloped in rolling mountain mist. Later, visit the Tata Tea Museum to understand the legacy of tea processing in the region, followed by an aromatic tea-tasting session. Continue to the scenic Mattupetty Dam and Lake, where your family can experience an exhilarating speed-boat cruise. Conclude your afternoon at Eco Point, famous for its natural acoustics, and the tranquil Kundala Lake, surrounded by towering pine trees. Return to your premium estate stay for an evening of luxury hospitality. Lake.'
                ),
                [
                    'Sightseeing Included: Eravikulam National Park, Tata Tea Museum, Mattupetty Dam, Eco Point, Kundala',
                    'Evening Experience: Strolling through the old Munnar town market, sampling fresh local banana fritters.',
                    'Optional Activities: Speed boating at Mattupetty; Professional family photoshoot amidst tea gardens.',
                    'Overnight Stay: Munnar (Premium/Luxury Resort)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'MUNNAR OFFBEAT EXPERIENCES',
                (
                    "HIDDEN VALLEYS, DEEP GORGES & PANORAMIC VISTAS After a delicious breakfast, embark on an offbeat exploration designed for a true Premium Kerala Experience. Head towards the spectacular Lock Heart Gap, a vantage point offering sweeping views of emerald valleys, winding roads, and distant tribal hamlets. Walk together through neatly manicured tea pathways, learning the art of tea plucking from local estate workers. In the afternoon, visit the magnificent Blossom Hydel Park, featuring beautiful flower gardens, water paths, and soft adventure play zones for children. Next, head to the Pothamedu Viewpoint, which offers panoramic vistas of Munnar's vast tea, coffee, and cardamom plantations. As the sun sets, return to your luxury resort to enjoy a cozy campfire session arranged exclusively for your family. walks."
                ),
                [
                    'Sightseeing Included: Lock Heart Gap, Blossom Hydel Park, Pothamedu Viewpoint, Tea Estate interactive',
                    'Evening Experience: Exclusive family campfire with live acoustic music or traditional storytelling.',
                    "Optional Activities: Jeep Safari to Kolukkumalai (the world's highest tea estate) for sunset views.",
                    'Overnight Stay: Munnar (Premium/Luxury Resort)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'MUNNAR TO KOCHI',
                (
                    "TRAGUIN Premium Luxury Holidays Page 3 RETURN TO THE COLONIAL CHARM OF HERITAGE COCHIN Relish your final breakfast overlooking the misty valleys of Munnar before checking out. Descend smoothly back towards the coastal heritage plains of Kochi. Upon arrival, check into your premium city hotel or historical boutique property in Fort Cochin. Kochi, historically known as Cochin, is an architectural mosaic blending Portuguese, Dutch, British, and Malabar design elements. In the afternoon, set out for comprehensive Kochi Sightseeing. See the iconic Chinese Fishing Nets silhouetted against the Arabian Sea, visit the historic St. Francis Church (India's oldest European church), and explore the vibrant 400-year-old Jewish Synagogue in Jew Town. Wander along the ancient lanes of Mattancherry Palace (Dutch Palace) to admire its intricate, historic mythological murals. Palace."
                ),
                [
                    'Sightseeing Included: Fort Kochi Chinese Fishing Nets, St. Francis Church, Jewish Synagogue, Dutch',
                    'Evening Experience: Sunset harbor cruise observing the shipping channels, followed by a gourmet dinner.',
                    'Optional Activities: Attending an authentic evening Kathakali classical dance performance.',
                    'Overnight Stay: Kochi (Premium Business / Heritage Luxury Hotel)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'KOCHI DEPARTURE',
                (
                    "SOUVENIR SHOPPING & FOND FAREWELLS Enjoy a leisurely morning breakfast at your hotel. Depending on your flight schedule, indulge in premium souvenir shopping around Kochi's upscale districts. Pick up vacuum-sealed organic spices, exotic tea blends, premium cashew nuts, and traditional Kerala handloom attire as mementos of your luxury holiday. At the designated hour, your private chauffeur will transfer your family seamlessly back to Cochin International Airport for your onward journey, concluding your magnificent vacation designed by TRAGUIN."
                ),
                [
                    'Sightseeing Included: Jew Town shopping walk, Lulu Mall visit (optional based on flight timing).',
                    'Meals Included: Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Leaf Munnar / Amber Dale | Trident Cochin / Radisson Blu',
                'Munnar | Cochin',
                '3N Munnar|1N Kochi',
                'Deluxe',
                'Deluxe Room',
                'Breakfast & Dinner (MAP)',
                4,
                1,
                description='OPTION 01 – DELUXE: The Leaf Munnar / Amber Dale | Trident Cochin / Radisson Blu | Breakfast & Dinner (MAP)',
            ),
            _hotel(
                'Blanket Hotel / Fragrant Nature | Brunton Boatyard / Grand Hyatt Bolgatty',
                'Munnar | Cochin',
                '3N Munnar|1N Kochi',
                'Premium',
                'Deluxe Room',
                'Breakfast & Dinner (MAP)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Blanket Hotel / Fragrant Nature | Brunton Boatyard / Grand Hyatt Bolgatty | Breakfast & Dinner (MAP)',
            ),
            _hotel(
                "Chandy's Windy Woods / Elixir Hills | Cochin Marriott / Taj Malabar Resort",
                'Munnar | Cochin',
                '3N Munnar|1N Kochi',
                'Luxury',
                'Deluxe Room',
                'Breakfast & Dinner (MAP)',
                5,
                3,
                description="OPTION 03 – LUXURY: Chandy's Windy Woods / Elixir Hills | Cochin Marriott / Taj Malabar Resort | Breakfast & Dinner (MAP)",
            ),
            _hotel(
                'Spice Tree / Windermere Estate | Taj Malabar Heritage / Grand Hyatt Presidential',
                'Munnar | Cochin',
                '3N Munnar|1N Kochi',
                'Ultra Luxury',
                'Deluxe Room',
                'Premium Curated Meals (MAP)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Spice Tree / Windermere Estate | Taj Malabar Heritage / Grand Hyatt Presidential | Premium Curated Meals (MAP)',
            )
        ],
        inclusions=[
            _inc_included('Munnar.', 1),
            _inc_included('01 Night premium heritage/business accommodation in Kochi.', 2),
            _inc_included('Daily buffet breakfasts and dinners prepared by master chefs.', 3),
            _inc_included('Entire transit via private luxury AC Innova Crysta with a professional driver-guide.', 4),
            _inc_included('Complimentary premium resort amenities, Wi-Fi, and recreational club access.', 5),
            _inc_included('Welcome non-alcoholic drinks and traditional floral garlanding on arrival.', 6),
            _inc_included('All applicable state tolls, parking fees, driver allowances, and fuel taxes.', 7),
            _inc_included('Dedicated 24/7 digital concierge support from your personal travel advisor.', 8),
            _inc_included('Domestic or International Airfare / Train tickets.', 9),
            _inc_excluded('Monument entry tickets, camera fees, and local guide charges.', 10),
            _inc_excluded('Optional activities (Speed boating, Kathakali show, Jeep safaris).', 11),
            _inc_excluded('Personal expenses like laundry, mini-bar, telephone calls, and tips.', 12),
            _inc_excluded("Mandatory Gala Dinner surcharges during Christmas or New Year's Eve.", 13),
            _inc_excluded('Any personal travel, medical, or baggage cancellation insurance.', 14),
            _inc_excluded('Anything not explicitly mentioned in the detailed inclusions list.', 15),
        ],
    )
    return package, itinerary

def build_kl_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-004'
    tour_code = 'TRAGUIN-KL-004-FAM'
    title = 'Premium Kerala Family Tour'
    duration = '05 Nights / 06 Days'
    slug = 'kl-004-premium-kerala-family-beach-vacation'
    itin_slug = 'kl-004-premium-kerala-family-beach-vacation-itinerary'
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
            _ph('Serial code KL-004 | TRAGUIN tour code TRAGUIN-KL-004-FAM', 1),
            _ph('State / Country: Kerala / India | Category: Family Holiday / Luxury Beaches', 2),
            _ph('Destinations: Cochin • Alleppey • Kovalam • Poovar', 3),
            _ph('Ideal for: Families, Couples, Luxury Travelers', 4),
            _ph('Best season: September to March', 5),
            _ph('Starting price: On Request (Premium Curated)', 6),
            _ph('Vehicle / Meals: Private Executive Chauffeur-Driven Luxury SUV Meal Plan: Modified American Plan (Breakfast & Dinner Included)', 7),
            _ph('Route: Cochin Arrival → Alleppey Backwaters → Kovalam Beach → Poovar Island → Trivandrum Departure', 8)
        ],
        moods=['Family', 'Luxury', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Curated)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Premium Kerala Family Tour',
        overview='When booking a Kerala Honeymoon Package or planning a comprehensive Kerala Family Tour, selecting the right destinations makes all the difference. Kerala offers an incredible mosaic of experiences, from ancient historical trade centers to emerald backwaters and world-class coastal resorts. The Best Time to Visit Kerala spans from autumn to early spring, when the weather remains beautifully temperate and perfect for comprehensive Kerala Sightseeing. Among the Top Tourist Places in Kerala, the backwaters of Alleppey and the spectacular cliffs of Kovalam stand out as top-tier, highly searched destinations. These popular Instagram locations provide perfect backdrops for capturing family moments and romantic milestones. From embarking on a premium backwater cruise to exploring vibrant local spice markets and indulging in traditional Ayurvedic wellness, this Premium Kerala Experience guarantees complete rejuvenation for every generations in your family.\n\nTOUR OVERVIEW\n"A custom-tailored itinerary meticulously designed for discerning families. This TRAGUIN curated experience note promises private, air-conditioned luxury transportation, premium handpicked hotels, and hand-selected cultural immersions across Kerala\'s most iconic attractions." Travel Dates: Flexible / Custom FIT Route: Cochin Arrival → Alleppey Backwaters → Kovalam Beach → Poovar Island → Trivandrum Departure Vehicle: Private Executive Chauffeur-Driven Luxury SUV Meal Plan: Modified American Plan (Breakfast & Dinner Included) TRAGUIN Edge: 24/7 Concierge, handpicked premium luxury properties, and specialized local guides. TRAGUIN Premium Holidays • Kerala Family Tour Package',
        seo_title='KL-004 | Premium Kerala Family Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Kerala package (KL-004 / TRAGUIN-KL-004-FAM): Cochin • Alleppey • Kovalam • Poovar with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN COCHIN TO ALLEPPEY', 1),
            _ih('Day 02: ALLEPPEY TO KOVALAM', 2),
            _ih('Day 03: KOVALAM BEACH SIGHTSEEING', 3),
            _ih('Day 04: EXCURSION TO POOVAR ISLAND', 4),
            _ih('Day 05: TRIVANDRUM HERITAGE DAY TOUR', 5),
            _ih('Day 06: DEPARTURE FROM TRIVANDRUM', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN COCHIN TO ALLEPPEY',
                (
                    "THE JOURNEY BEGINS: GATEWAY TO SOULFUL BACKWATERS Arrive at Cochin International Airport where your professional TRAGUIN tour representative warmly welcomes your family with traditional Kerala greetings. Board your premium luxury private vehicle and proceed towards Alleppey—the globally acclaimed 'Venice of the East'. As you drive through winding roads flanked by rows of coconut palms, feel the urban stress melt away into breathtaking landscapes. Upon reaching Alleppey, check in to your premium luxury backwater resort. Prepare for an enchanting evening country boat ride along narrow canals, catching glimpses of local village life, traditional fishing practices, and beautiful water lilies. Savor local delicacies and dynamic culinary flavors during dinner at the resort restaurant."
                ),
                [
                    'Sightseeing Included: Fort Cochin (En-route glance), Alleppey backwater sunset view, evening canal ride.',
                    'Evening Experience: Relaxed poolside dinner with traditional live instrumental music.',
                    'Overnight Stay: Alleppey (Premium Luxury Backwater Resort)',
                    'Meals Included: Welcome Drinks & Dinner',
                ],
            ),
            _day(
                2,
                'ALLEPPEY TO KOVALAM',
                (
                    'CRUISING THE EMERALD LAGOONS TO THE SUNSET COAST Wake up to the soft chirping of birds over the tranquil lagoons. After a sumptuous breakfast, experience a truly iconic attraction: a private cruise on a luxury houseboat curated exclusively for you. Glide through the vast Vembanad Lake, capturing stunning family photographs against the lush green shorelines. This immersive experience highlights why Alleppey remains central to every Best Kerala Tour Package. In the afternoon, disembark and drive south toward Kovalam, the jewel of the Arabian Sea. The route treats your family to scenic beauty that evolves from peaceful inland waterways to dramatic oceanic vistas. Upon arrival in Kovalam, check in to an ultra-luxury cliffside resort overlooking pristine beaches. TRAGUIN Premium Holidays • Kerala Family Tour Package'
                ),
                [
                    'Sightseeing Included: Vembanad Lake Cruise, Alleppey Beach, Pathiramanal Island views.',
                    'Optional Activities: Authentic Ayurvedic foot massage at the resort wellness center.',
                    'Evening Experience: Walking along the crescent-shaped shores of Kovalam Beach.',
                    'Overnight Stay: Kovalam (Ultra Luxury Beach Resort)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'KOVALAM BEACH SIGHTSEEING',
                (
                    'EXPLORING EXCLUSIVE COASTAL CHARMS AND SUN-KISSED SHORES Dedicate today to experiencing the very best of a Luxury Kerala Holiday. After a leisurely gourmet breakfast, visit the famous lighthouse beach, climbing to the top of the iconic red-and-white striped Vizhinjam Lighthouse for spectacular panoramic views of the Arabian Sea coast. Walk down to Hawa Beach and Samudra Beach, noting the unique rock formations that create calm bays ideal for wading. In the afternoon, head out for a curated family photography session at sunset. Your TRAGUIN local expert knows the absolute finest vantage points away from tourist crowds, letting you capture unforgettable memories. Cap off the night with an exceptional beachside candlelight family dinner featuring fresh catches of the day.'
                ),
                [
                    'Sightseeing Included: Vizhinjam Lighthouse, Marine Aquarium, Hawa Beach, Samudra Beach.',
                    'Optional Activities: Speedboat rides or professional surfing lessons under expert supervision.',
                    'Evening Experience: Private seafood dinner on a secluded deck area with wave-front views.',
                    'Overnight Stay: Kovalam (Ultra Luxury Beach Resort)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'EXCURSION TO POOVAR ISLAND',
                (
                    'WHERE THE RIVER, CANALS, AND OCEAN CONVERGE UNQUELY After a magnificent breakfast, take a short drive to Poovar Island, an exquisite estuary where the Neyyar River meets the Arabian Sea. Board a customized motorized boat to navigate through dense mangrove forests. The dramatic sight of a pristine golden sand beach separating the sweet river waters from the salty ocean is an extraordinary natural marvel. Enjoy lunch at a floating restaurant, feeling the gentle sway of the water beneath you. Spend your afternoon relaxing on the isolated golden sand beach, widely recognized as one of the most exclusive, peaceful, and romantic spots in southern India. Return to Kovalam in the evening to relax in the comfort of your luxury hotel room. TRAGUIN Premium Holidays • Kerala Family Tour Package'
                ),
                [
                    'Sightseeing Included: Poovar Estuary, Mangrove Forests, Golden Sand Beach, Floating Village.',
                    'Optional Activities: Traditional archery or traditional rowing boat trials in calm river channels.',
                    'Evening Experience: Cultural Kathakali dance demonstration inside your resort arena.',
                    'Overnight Stay: Kovalam (Ultra Luxury Beach Resort)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'TRIVANDRUM HERITAGE DAY TOUR',
                (
                    'ROYAL LEGACIES, SACRED TEMPLES, AND SOUVENIR TREASURES Venture into Trivandrum, the royal capital city of Kerala, for a deep dive into heritage and architecture. Visit the magnificent Sree Padmanabhaswamy Temple, globally celebrated for its immense spiritual significance and architectural scale. Next, explore the Kuthiramalika Palace Museum, admiring its fine wood carvings and rare royal artifacts. Spend the afternoon hunting for authentic souvenirs and gifts. Shop for premium handloom Kasavu sarees, fine brass lamps, and aromatic spices at selected premium boutiques recommended by TRAGUIN. End your final tour night with a special farewell dinner to toast to a magical vacation.'
                ),
                [
                    'Sightseeing Included: Padmanabhaswamy Temple, Kuthiramalika Palace, Napier Museum, Art Gallery.',
                    'Optional Activities: Interactive guided walk through the botanical gardens.',
                    'Evening Experience: Multi-course fine dining showcasing traditional Kerala Sadya flavors.',
                    'Overnight Stay: Kovalam (Ultra Luxury Beach Resort)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                6,
                'DEPARTURE FROM TRIVANDRUM',
                (
                    "FAREWELL TO GOD'S OWN COUNTRY Enjoy a slow, late-morning breakfast while looking out over the blue waters of the ocean one last time. Take advantage of the resort facilities, perhaps going for a refreshing dip in the infinity pool or packing your bags with treasured memories and local souvenirs. At your requested time, check out from the resort. Your private luxury vehicle will transfer your family smoothly to Trivandrum International Airport for your flight back home. Board your flight with an abundance of beautiful family photographs, renewed bonds, and unforgettable memories courtesy of your personalized TRAGUIN holiday package."
                ),
                [
                    'Sightseeing Included: Airport departure transfer via scenic coastal highway route.',
                    'Meals Included: Premium Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Ramada by Wyndham / Lake Palace | Isola Di Cocco / Uday Samudra',
                'Alleppey | Kovalam',
                '1N Alleppey|4N Kovalam / Poovar',
                'Deluxe',
                'Superior Sea View',
                'MAPAI',
                4,
                1,
                description='OPTION 01 – DELUXE: Ramada by Wyndham / Lake Palace | Isola Di Cocco / Uday Samudra | MAPAI',
            ),
            _hotel(
                'Kumarakom Lake Resort / Vasundhara | The Raviz Kovalam / Niraamaya',
                'Alleppey | Kovalam',
                '1N Alleppey|4N Kovalam / Poovar',
                'Premium',
                'Premium Heritage Villa',
                'MAPAI',
                4,
                2,
                description='OPTION 02 – PREMIUM: Kumarakom Lake Resort / Vasundhara | The Raviz Kovalam / Niraamaya | MAPAI',
            ),
            _hotel(
                'Forte Kochi / Marari Beach Resort | Taj Green Cove Resort & Spa',
                'Alleppey | Kovalam',
                '1N Alleppey|4N Kovalam / Poovar',
                'Luxury',
                'Luxury Garden Cottage',
                'MAPAI',
                5,
                3,
                description='OPTION 03 – LUXURY: Forte Kochi / Marari Beach Resort | Taj Green Cove Resort & Spa | MAPAI',
            ),
            _hotel(
                'The Oberoi Vrinda Luxury Cruiser | The Leela Kovalam (Club Rooms)',
                'Alleppey | Kovalam',
                '1N Alleppey|4N Kovalam / Poovar',
                'Ultra Luxury',
                'The Club Suite Ocean View',
                'MAPAI',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Oberoi Vrinda Luxury Cruiser | The Leela Kovalam (Club Rooms) | MAPAI',
            )
        ],
        inclusions=[
            _inc_included('Accommodation: 05 Nights in handpicked premium hotels and luxury resorts.', 1),
            _inc_included('Meals: Daily gourmet breakfasts and multi-cuisine dinners as specified.', 2),
            _inc_included('Transfers: Complete private transfers in a dedicated luxury air-conditioned SUV.', 3),
            _inc_included('Sightseeing: Full curated itineraries including private boat charters at Poovar and Alleppey.', 4),
            _inc_included('Welcome Amenities: Traditional non-alcoholic welcome drinks, fruit platter, and custom sweets.', 5),
            _inc_included('TRAGUIN Support: 24/7 dedicated professional guest relations assistance.', 6),
            _inc_included('Taxes & Fuel: All toll fees, state taxes, driver allowances, and parking charges.', 7),
            _inc_excluded('Airfare / Rail: Domestic or international flight tickets to Cochin / from Trivandrum.', 8),
            _inc_excluded('Monuments Fees: Entry tickets, camera charges, and historical site guide fees.', 9),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, alcoholic drinks, and mini-bar items.', 10),
            _inc_excluded('Optional Tours: Water sports, premium spa treatments, and activities marked as optional.', 11),
            _inc_excluded('Insurance: Travel insurance, medical costs, and emergency evacuation expenses.', 12),
            _inc_excluded('Surcharges: Festival season or peak high occupancy room surcharges if applicable.', 13),
        ],
    )
    return package, itinerary

def build_kl_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-005'
    tour_code = 'TRG-KLR-2026-005'
    title = 'Munnar • Alleppey Houseboat • Cochin Luxury Escape'
    duration = '04 Nights / 05 Days'
    slug = 'kl-005-romantic-honeymoon-munnar-alleppey'
    itin_slug = 'kl-005-romantic-honeymoon-munnar-alleppey-itinerary'
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
            _ph('Serial code KL-005 | TRAGUIN tour code TRG-KLR-2026-005', 1),
            _ph('State / Country: Kerala / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Jharkhand', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / MAPAI', 7),
            _ph('TRAGUIN Signature Experience: Private, romantic, candlelight dinner arranged in a hidden', 8),
            _ph('Curated by Experts: Fully customisable day-to-day pacing designed around your personal comfort', 9),
            _ph('Premium Handpicked Hotels: Properties verified rigorously for top-tier hygiene, absolute safety, and', 10),
            _ph('Exclusive Recommendations: Access to a hand-selected list of local artisan shops, authentic', 11),
            _ph("Kerala is world-famous for its organic treasures. In Munnar, don't miss purchasing fresh CTC and green teas, premium quality spices (such as green cardamom, cinnamon, cloves, and black pepper), and homemade artisanal chocolates. When in Cochin, explore the antique markets of Jew Town for rare colonial-era souvenirs, handcrafted wooden artifacts, and elegant traditional Kerala Kasavu sarees characterized by their striking golden borders.", 12),
            _ph('& GUIDELINES', 13)
        ],
        moods=['Romantic', 'Honeymoon', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Munnar',
        overview='aptivating journey designed exclusively for love. This bespoke Kerala Honeymoon Package weaves together the mist-kissed emerald hills of Munnar and the romantic, shimmering backwaters of Alleppey. Specially curated by TRAGUIN, this itinerary transforms your post-wedding getaway into an unforgettable premium experience of timeless intimacy, breathtaking landscapes, and immersive tropical luxury. SERIAL CODE: KL-005 TRAGUIN TOUR CODE: TRG-KLR-2026-005 STATE / COUNTRY: Kerala / India CATEGORY: Honeymoon / Luxury Romance DURATION: 04 Nights / 05 Days DESTINATIONS COVERED: Cochin • Munnar • Alleppey IDEAL FOR: Newlyweds, Couples, Luxury Travelers BEST SEASON: September to March (Pleasant & Lush) STARTING PRICE: On Request (Premium Luxury Tier) MEAL PLAN: CPAI (Munnar) & APAI (Houseboat)\n\nTOUR OVERVIEW\nWelcome to your meticulously designed Kerala Family Tour and romantic honeymoon itinerary. This signature voyage features private premium stays in handpicked boutique resorts, private transfers via a luxury air-conditioned vehicle, and dedicated elite hospitality managed continuously by your personal TRAGUIN vacation specialist. From the iconic attractions of Cochin to the scenic beauty of the Western Ghats, every singular detail has been refined to ensure seamless comfort and unparalleled romantic indulgence.\n\nWHY CHOOSE THE BEST KERALA TOUR PACKAGE?\nKnown universally as "God\'s Own Country," Kerala stands as India’s ultimate flagship destination for an ultra- premium, intimate holiday. A Kerala Honeymoon Package provides couples with the perfect blend of dramatic geographical diversity and rich, soul-stirring cultural heritage. This curated route hits the absolute top tourist places in Kerala, effortlessly capturing the most sought-after Instagram locations, vibrant tea plantation walks, misty waterfalls, and authentic local culinary experiences. TRAGUIN • Premium Luxury Holidays Page 1 Most Searched Kerala Sightseeing & Experiences Included: Munnar Sightseeing: Eravikulam National Park (home to the rare Nilgiri Tahr), Mattupetty Dam, Echo Point, and pristine tea estates perfect for professional couples\' photography. Alleppey Backwaters: Private luxury houseboat cruising across the tranquil Vembanad Lake with local Kuttanadan delicacies served onboard. Popular Romantic Highlights: Candlelight dining beneath a canopy of stars, premium aromatherapy couples\' massages, and breathtaking sunset viewing points. YOUR BESPOKE DAY-WISE ITINERARY',
        seo_title='KL-005 | Munnar | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Kerala package (KL-005 / TRG-KLR-2026-005): Jharkhand with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: COCHIN TO MUNNAR', 1),
            _ih('Day 02: MUNNAR SIGHTSEEING', 2),
            _ih('Day 03: MUNNAR TO ALLEPPEY', 3),
            _ih('Day 04: ALLEPPEY TO COCHIN', 4),
            _ih('Day 05: DEPARTURE FROM COCHIN', 5),
            _ih('TRAGUIN Signature Experience: Private, romantic, candlelight dinner arranged in a hidden', 6),
            _ih('Curated by Experts: Fully customisable day-to-day pacing designed around your personal comfort', 7),
            _ih('Premium Handpicked Hotels: Properties verified rigorously for top-tier hygiene, absolute safety, and', 8)
        ],
        days=[
            _day(
                1,
                'COCHIN TO MUNNAR | WELCOME TO THE EMERALD HILLS',
                (
                    'Upon your arrival at Cochin International Airport, you will be warmly received by a dedicated TRAGUIN representative. Your luxury transport awaits to sweep you away on a stunningly scenic drive toward Munnar, the undisputed crown jewel of South Indian hill stations. As the urban landscape transitions seamlessly into steep winding roads, you will experience the cooling mountain air and spectacular vistas of the Western Ghats. Along the way, stop to admire the majestic Cheeyappara and Valara waterfalls cascading down rocky cliffs amidst dense tropical forests. Arrive at your handpicked luxury resort in Munnar, where a seamless check-in experience and special honeymoon welcome amenities await you. Karadipara View Point, Scenic Mountain Highway Drive. or Kalaripayattu cultural performance check-in. organic gardens followed by a tailored multi-course dinner. Munnar.'
                ),
                [
                    'Sightseeing Included: Cheeyappara & Valara Waterfalls,',
                    'Optional Activities: Evening traditional Kathakali',
                    "Evening Experience: Private stroll through the resort's",
                    'Overnight Stay: Handpicked Premium Resort in',
                    'Meals Included: Welcome Drink & Dinner.',
                ],
            ),
            _day(
                2,
                'MUNNAR SIGHTSEEING | MIST, MOUNTAINS & ROMANCE',
                (
                    "Awake to the crisp mountain breeze and a magnificent breakfast overlooking sun-kissed valleys. Today is dedicated to exploring the finest tourist places in Munnar. Your private chauffeur will escort you to Eravikulam National Park, where you can walk hand-in-hand along the misty pathways looking for the endangered Nilgiri Tahr. Next, visit the structural marvel of Mattupetty Dam and the serene Kundala Lake, where a private speed- boat or pedal-boat ride can be arranged. Share a playful whisper at the famous Echo Point, and capture incredible photographs amidst the perfectly manicured, endless green carpets of the Tata Tea Estates. Dam, Echo Point, Kundala Lake, Photo Point, Tea Museum. tasting session or a private couple's plantation trek. TRAGUIN • Premium Luxury Holidays Page 2 Experience: A romantic, candlelit dinner arranged in a private pavilion. in Munnar."
                ),
                [
                    'Sightseeing Included: Eravikulam National Park, Mattupetty',
                    'Optional Activities: Guided premium tea',
                    'Evening Experience: An exclusive TRAGUIN Signature',
                    'Overnight Stay: Handpicked Premium Resort',
                    'Meals Included: Breakfast & Candlelight Dinner.',
                ],
            ),
            _day(
                3,
                'MUNNAR TO ALLEPPEY | CRUISE OF ETERNAL TOGETHERNESS',
                (
                    'After a leisurely breakfast, bid farewell to the misty mountains as you descend toward the enchanting lowlands of Alleppey—the world-renowned "Venice of the East." This afternoon, step aboard an exclusive, fully private luxury houseboat, an absolute pinnacle of any premium Luxury Kerala Holiday. As you gently glide through the labyrinth of palm-fringed canals, vast paddy fields, and traditional lakeside villages, the sheer tranquility provides a profound sense of romance. A dedicated onboard chef will prepare traditional, hyper-local delicacies tailored strictly to your preferences. Sip on fresh coconut water as the golden tropical sun sets dramatically over the endless backwaters. Alleppey narrow backwater canals, local rural life viewing. through the ultra-narrow canals for authentic photography. stars; overnight anchoring in the serene heart of the lake. (Air Conditioned).'
                ),
                [
                    'Sightseeing Included: Vembanad Lake cruising,',
                    'Optional Activities: A traditional village canoe ride',
                    'Evening Experience: Relaxing on the open deck under',
                    'Overnight Stay: Premium Private Luxury Houseboat',
                    'Meals Included: Breakfast, Traditional Lunch, Evening Snacks, and Gourmet Dinner (Full Board / APAI).',
                ],
            ),
            _day(
                4,
                'ALLEPPEY TO COCHIN | HERITAGE & COASTAL LUXURY',
                (
                    'Witness a breathtaking sunrise over the water as your houseboat slowly glides back to the jetty. After a comforting traditional breakfast, disembark and travel back to the historic port city of Cochin. Spend your afternoon discovering the layers of history embedded within Fort Cochin and Mattancherry. Walk alongside the iconic Chinese Fishing Nets standing tall against the Arabian Sea, explore the 400-year-old Paradesi Synagogue in Jew Town, and marvel at the exquisite mythological murals within the Mattancherry Dutch Palace. This evening offers the perfect opportunity to visit upscale boutiques for high-quality spices, traditional handloom sarees, and exquisite artifacts. St. Francis Church, Mattancherry Palace, Jew Town. or high-tea at a historical heritage waterfront hotel. seafood specialty restaurant in Cochin. TRAGUIN • Premium Luxury Holidays Page 3'
                ),
                [
                    'Sightseeing Included: Fort Cochin, Chinese Fishing Nets,',
                    'Optional Activities: Premium harbor sunset cruise',
                    'Evening Experience: Gourmet dining at a renowned',
                    'Overnight Stay: Premium Luxury Hotel in Cochin.',
                    'Meals Included: Breakfast & Luxury Farewell Dinner.',
                ],
            ),
            _day(
                5,
                'DEPARTURE FROM COCHIN | CHERISHED FOREVER',
                (
                    'Savor your final morning breakfast in the beautiful coastal capital. Depending on your flight schedule, enjoy a relaxed morning at your luxury property or squeeze in some last-minute artisan souvenir shopping. At the designated hour, your private luxury vehicle will transfer you back to Cochin International Airport for your journey home. Your premium TRAGUIN Kerala Romance tour concludes here, leaving you with timeless bonds, breathtaking landscape photographs, and unforgettable memories of a love celebrated in paradise. optional brief stopovers for local spice purchases. before check-out if flight time permits.'
                ),
                [
                    'Sightseeing Included: Airport transit route viewing,',
                    'Optional Activities: Morning premium spa session',
                    'Evening Experience: Flight departure back home.',
                    'Overnight Stay: None.',
                    'Meals Included: Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Leaf Munnar (Valley View Room) | Premium AC Houseboat (Private) | Trident Cochin (Superior Room)',
                'Munnar | Alleppey | Cochin',
                '2N Munnar|1N Alleppey|1N Cochin',
                'Deluxe',
                'Deluxe Room',
                'CPAI (Munnar) & APAI (Houseboat)',
                4,
                1,
                description='OPTION 01 – DELUXE: The Leaf Munnar (Valley View Room) | Premium AC Houseboat (Private) | Trident Cochin (Superior Room) | CPAI (Munnar) & APAI (Houseboat)',
            ),
            _hotel(
                'Blanket Hotel & Spa (Premier Room) | Luxury Glass Houseboat (Private) | Brunton Boatyard (Sea Facing Room)',
                'Munnar | Alleppey | Cochin',
                '2N Munnar|1N Alleppey|1N Cochin',
                'Premium',
                'Deluxe Room',
                'CPAI (Munnar) & APAI (Houseboat)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Blanket Hotel & Spa (Premier Room) | Luxury Glass Houseboat (Private) | Brunton Boatyard (Sea Facing Room) | CPAI (Munnar) & APAI (Houseboat)',
            ),
            _hotel(
                "Chandy's Windy Woods (Super Deluxe) | Super Luxury Cruise (Upper Deck) | Grand Hyatt Bolgatty (Club Room)",
                'Munnar | Alleppey | Cochin',
                '2N Munnar|1N Alleppey|1N Cochin',
                'Luxury',
                'Deluxe Room',
                'CPAI (Munnar) & APAI (Houseboat)',
                5,
                3,
                description="OPTION 03 – LUXURY: Chandy's Windy Woods (Super Deluxe) | Super Luxury Cruise (Upper Deck) | Grand Hyatt Bolgatty (Club Room) | CPAI (Munnar) & APAI (Houseboat)",
            ),
            _hotel(
                'Spice Tree Munnar (Classic Pool Villa) | TRAGUIN Signature Elite Houseboat | The Leela Kovalam / Cochin Elite',
                'Munnar | Alleppey | Cochin',
                '2N Munnar|1N Alleppey|1N Cochin',
                'Ultra Luxury',
                'Deluxe Room',
                'CPAI (Munnar) & APAI (Houseboat)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Spice Tree Munnar (Classic Pool Villa) | TRAGUIN Signature Elite Houseboat | The Leela Kovalam / Cochin Elite | CPAI (Munnar) & APAI (Houseboat)',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Handpicked properties on twin-sharing basis.', 1),
            _inc_included('Curated Houseboat: Private cruise with all onboard meals.', 2),
            _inc_included('Transfers: Air-conditioned private luxury vehicle for all transits.', 3),
            _inc_included('TRAGUIN • Premium Luxury Holidays Page 4', 4),
            _inc_included('Welcome Amenities: Honeymoon cake, floral bed decoration, and sparkling juice.', 5),
            _inc_included('Signature Dining: One exclusive candlelight dinner in Munnar.', 6),
            _inc_included('Expert Support: 24/7 dedicated TRAGUIN guest assistance.', 7),
            _inc_included('Taxes: All applicable luxury resort and toll taxes.', 8),
            _inc_excluded('Airfare: Domestic or International flights to/from Cochin.', 9),
            _inc_excluded('Entry Tickets: National park, museum fees, or activity charges.', 10),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, tips, and minibar.', 11),
            _inc_excluded('Optional Tours: Any activities not mentioned explicitly.', 12),
            _inc_excluded('Insurance: Travel or medical insurance policies.', 13),
            _inc_excluded('Surcharges: Peak seasonal festival surcharges if applicable.', 14),
        ],
    )
    return package, itinerary

def build_kl_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-006'
    tour_code = 'TRAGUIN-KL-ROMANCE-06'
    title = 'Munnar • Thekkady • Alleppey • Kovalam'
    duration = '05 Nights / 06 Days'
    slug = 'kl-006-honeymoon-romance-munnar-kovalam'
    itin_slug = 'kl-006-honeymoon-romance-munnar-kovalam-itinerary'
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
            _ph('Serial code KL-006 | TRAGUIN tour code TRAGUIN-KL-ROMANCE-06', 1),
            _ph('State / Country: Kerala / India | Category: Honeymoon / Luxury Holidays', 2),
            _ph('Destinations: Munnar (2N) • Thekkady (1N) • Alleppey Houseboat (1N) • Kovalam (1N)', 3),
            _ph('Ideal for: Couples, Honeymooners, Luxury Travelers', 4),
            _ph('Best season: October to March (Pleasant Weather)', 5),
            _ph('Starting price: On Request (Premium Handpicked Selection)', 6),
            _ph('Vehicle / Meals: Chauffeur-Driven Premium Sedan / Luxury SUV Meal Plan: CP / MAPAI (Breakfast & Dinner Included)', 7),
            _ph("Route: Cochin → Munnar → Thekkady → Alleppey → Kovalam → Trivandrum DESTINATION SEO INSIGHT & HIGHLIGHTS Kerala is globally ranked among the top iconic attractions for experiential luxury travel. This customized Luxury Kerala Holiday highlights the very best of South India's scenic beauty. Whether you are seeking the most popular Instagram locations amidst the tea gardens of Munnar, looking to sample authentic Malabar cuisine at fine-dining beachside retreats, or hoping to uncover the historic spice trade routes in Thekkady, this tour captures every dimension. It stands as the quintessential luxury package for honeymooners, offering secluded privacy, candlelit dinners, sunset backwater cruises, and rejuvenating traditional Ayurvedic wellness therapies.", 8),
            _ph('TRAGUIN Signature Experience: Private candlelight dining arrangements overlooking the mist-filled', 9),
            _ph('Curated by TRAGUIN Experts: Handpicked properties selected strictly for outstanding hospitality,', 10),
            _ph('Personalized Assistance: Seamless coordination with zero waiting times for hotel check-ins and smooth', 11),
            _ph('Luxury Transportation: Professional, polite, and English/Hindi-speaking tourist drivers with clean', 12),
            _ph('& BOOKING POLICIES', 13),
            _ph('Hotel Policies: Standard check-in time is 14:00 hrs and check-out is 11:00 hrs. Early check-ins are', 14)
        ],
        moods=['Romantic', 'Honeymoon', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Handpicked Selection)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Munnar',
        overview="Welcome to an enchanting world crafted exclusively for love. The Best Kerala Tour Package presented by TRAGUIN invites you to immerse yourselves in a sanctuary of emerald landscapes, pristine misty mountains, and timeless aquatic highways. Designed as the ultimate Kerala Honeymoon Package, this itinerary weaves together the aromatic romance of Munnar's high-altitude tea plantations, the exotic wildlife mysteries of Thekkady, the sublime solitude of an exclusive Alleppey backwater cruise, and the dramatic clifftop coastlines of Kovalam. Let TRAGUIN orchestrate your magical journey through God’s Own Country, where premium hospitality meets breathtaking landscapes to forge unforgettable memories. TRAGUIN Premium Travel Experience\n\nTOUR OVERVIEW\nThis strictly curated Kerala Family Tour and honeymoon plan is seamlessly orchestrated to eliminate travel stress while maximizing immersive experiences. Your package includes private premium transportation across all destinations, handpicked ultra-luxury resort accommodations, sensory-rich meals, and specialized local interactions curated by TRAGUIN destination experts. Group / FIT: Private FIT (Fully Customized Private Tour) Vehicle: Chauffeur-Driven Premium Sedan / Luxury SUV Meal Plan: CP / MAPAI (Breakfast & Dinner Included) Route: Cochin → Munnar → Thekkady → Alleppey → Kovalam → Trivandrum",
        seo_title='KL-006 | Munnar | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Kerala package (KL-006 / TRAGUIN-KL-ROMANCE-06): Munnar (2N) • Thekkady (1N) • Alleppey Houseboat (1N) • Kovalam (1N) with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: COCHIN ARRIVAL TO MUNNAR', 1),
            _ih('Day 02: MUNNAR SIGHTSEEING', 2),
            _ih('Day 03: MUNNAR TO THEKKADY', 3),
            _ih('Day 04: THEKKADY TO ALLEPPEY', 4),
            _ih('Day 05: ALLEPPEY TO KOVALAM', 5),
            _ih('Day 06: KOVALAM TO TRIVANDRUM', 6),
            _ih('TRAGUIN Signature Experience: Private candlelight dining arrangements overlooking the mist-filled', 7),
            _ih('Curated by TRAGUIN Experts: Handpicked properties selected strictly for outstanding hospitality,', 8),
            _ih('Personalized Assistance: Seamless coordination with zero waiting times for hotel check-ins and smooth', 9)
        ],
        days=[
            _day(
                1,
                'COCHIN ARRIVAL TO MUNNAR | MISTY HILLS & CASCADE WELCOME',
                (
                    'Arrive at Cochin International Airport or railway station, where a professional TRAGUIN travel representative warmly welcomes you with fresh traditional garlands and private premium transport. Begin your scenic drive toward Munnar, a premium hill station renowned for its rolling carpets of green. As the road ascends, feel the crisp mountain air replace the coastal warmth. Traverse winding roads passing through the spectacular Cheeyappara and Valara Waterfalls—perfect photography points to capture your initial steps into paradise. Arrive at your ultra-luxury handpicked resort in Munnar, complete your seamless private check-in, and unwind in your private balcony overlooking the clouds. TRAGUIN Premium Travel Experience'
                ),
                [
                    'Sightseeing Included: Cheeyappara & Valara Waterfalls, Adimali Spice Markets, Scenic Mountain Drive.',
                    'Optional Activities: Traditional Kerala Ayurvedic Welcome Massage at the resort.',
                    'Evening Experience: Private candlelight dining orientation over looking the mist-clad valley.',
                    'Overnight Stay: Premium Resort in Munnar.',
                    'Meals Included: Welcome Drink & Dinner.',
                ],
            ),
            _day(
                2,
                'MUNNAR SIGHTSEEING | PRIVATE TEA ESTATE TRAILS & ICONIC',
                (
                    'PEAKS Wake up to a glorious mountain sunrise and indulge in a lavish buffet breakfast. Today, enjoy an immersive Munnar Sightseeing tour curated for deeper exploration. Visit the beautiful Mattupetty Dam and Lake, where an optional speed-boat ride offers thrilling panoramic views. Whisper your vows at the iconic Echo Point, and stroll through the manicured greenery of Kundala Lake. Later, experience an exclusive walk through private Tata Tea Plantations with a local naturalist, learning the delicate art of tea leaf plucking, followed by a gourmet tea-tasting session. Conclude your day with a visit to Eravikulam National Park (Rajamalai), the natural habitat of the endangered Nilgiri Tahr. handmade chocolates.'
                ),
                [
                    'Sightseeing Included: Eravikulam National Park, Mattupetty Dam, Echo Point, Kundala Lake, Tea Museum.',
                    "Optional Activities: Speed boating at Mattupetty, Private Couples' Photo Session in tea gardens.",
                    'Evening Experience: Leisurely walk down the local colonial-era Munnar town market for rare spices and',
                    'Overnight Stay: Premium Resort in Munnar.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                3,
                'MUNNAR TO THEKKADY | WILDLIFE ENCOUNTERS & SPICE ODYSSEY',
                (
                    "Following a delicious breakfast, check out and drive through the Western Ghats to Thekkady, India's premier spice destination. The route is an absolute visual treat, lined with rubber plantations, open valleys, and dense tropical forests. Check in to your luxury boutique wilderness resort. In the afternoon, enjoy an immersive spice plantation tour, where you will smell, taste, and learn about fresh cardamom, black pepper, vanilla, and cinnamon. Later, proceed for a tranquil boating experience on Periyar Lake inside the Periyar Tiger Reserve, keeping a sharp eye out for wild elephants, gaur, and rare birds drinking along the water's edge. TRAGUIN Premium Travel Experience"
                ),
                [
                    'Sightseeing Included: Periyar Lake Boating, Spice Plantation Tour, Periyar Tiger Reserve.',
                    'Optional Activities: Elephant Interaction Program, Guided Jungle Night Patrol Walk.',
                    'Evening Experience: VIP seating at the local theatre for Kalaripayattu (Martial Arts) and Kathakali cultural shows.',
                    'Overnight Stay: Luxury Spice Resort in Thekkady.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                4,
                'THEKKADY TO ALLEPPEY | THE ULTIMATE PRIVATE BACKWATER',
                (
                    'CRUISE After breakfast, depart for Alleppey, the crown jewel of your Premium Kerala Experience. At noon, step onto your exclusive, private luxury traditional Houseboat (Kettuvallam) waiting at the jetty. Your dedicated onboard crew—comprising a private captain, chef, and butler—welcomes you with fresh coconut water. As your boat glides effortlessly along the tranquil Vembanad Lake and narrow palm- fringed canals, admire the quintessential sights of rural Kerala lifestyle. Enjoy an exquisite multi-course lunch featuring traditional pearl spot fish (Karimeen Pollichathu) cooked fresh onboard. This is the centerpiece of your Kerala Honeymoon Package, offering unrivaled intimate luxury and peace. dinner.'
                ),
                [
                    'Sightseeing Included: Vembanad Lake, Alleppey Backwater Canals, Paddy Field Views.',
                    'Optional Activities: Traditional village canoe cruise to explore narrow water alleys.',
                    'Evening Experience: Watch the breathtaking sunset from the houseboat deck, followed by a romantic candlelit',
                    'Overnight Stay: Private Luxury Houseboat (Anchored in the serene backwaters).',
                    'Meals Included: Breakfast, Traditional Lunch, Evening Snacks, & Candlelight Dinner.',
                ],
            ),
            _day(
                5,
                'ALLEPPEY TO KOVALAM | SUN-KISSED CLIFFS & ARABIAN SEA',
                (
                    'LUXURY Enjoy breakfast while cruising smoothly back to the jetty. Disembark and drive south toward Kovalam, the world-famous pristine beach destination of Kerala. Upon arrival, check in to a spectacular premium clifftop resort that offers endless views of the Arabian Sea. Spend your afternoon relaxing on the golden sands of Lighthouse Beach, Hawa Beach, or Samudra Beach. The dramatic black rocks against the blue sea create one of the most popular Instagram locations in India. Unwind under palm trees, enjoy the cool sea breeze, and let the soothing rhythm of the waves enhance your romantic getaway. TRAGUIN Premium Travel Experience'
                ),
                [
                    'Sightseeing Included: Kovalam Beach Circuit, Vizhinjam Lighthouse, Marine Aquarium.',
                    'Optional Activities: Authentic full-body Ayurvedic rejuvenation therapy at a beachside spa.',
                    'Evening Experience: Private seaside sundowner cocktail session followed by a gourmet seafood dinner.',
                    'Overnight Stay: Luxury Beach Resort in Kovalam.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                6,
                'KOVALAM TO TRIVANDRUM | DEPARTURE WITH FOREVER MEMORIES',
                (
                    'Conclude your remarkable luxury holiday with a relaxed breakfast by the ocean. Depending on your flight or train schedule, check out of your resort and enjoy a brief city tour of Trivandrum. Visit the breathtaking, historic Sree Padmanabhaswamy Temple, known for its grand architecture and spiritual heritage. Afterwards, your private chauffeur transfers you to Trivandrum International Airport or the railway station for your onward journey. Your majestic itinerary with TRAGUIN ends here, leaving you with beautifully curated experiences and unforgettable memories to cherish for a lifetime. Museum.'
                ),
                [
                    'Sightseeing Included: Sree Padmanabhaswamy Temple (Outer View / Entry subject to dress code), Napier',
                    'Meals Included: Premium Buffet Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Fog Munnar / Leaf Resort | Greenwoods Resort / Poetree | Premium Private Houseboat | Soma Palmshore / Travancore',
                'Munnar | Thekkady | Alleppey | Kovalam',
                '2N Munnar|1N Thekkady|1N Alleppey|1N Kovalam',
                'Deluxe',
                'Valley View / Deluxe Room / Deluxe AC Cabin / Standard Sea View',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: The Fog Munnar / Leaf Resort | Greenwoods Resort / Poetree | Premium Private Houseboat | Soma Palmshore / Travancore | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Blanket Hotel / Amber Dale | Elephant Court / Spice Village | Luxury Private Houseboat | Turtle on the Beach / Isola Di Cocco',
                'Munnar | Thekkady | Alleppey | Kovalam',
                '2N Munnar|1N Thekkady|1N Alleppey|1N Kovalam',
                'Premium',
                'Premier Valley View / Patio Room / Luxury Glass AC Cabin / Premium Sea View',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Blanket Hotel / Amber Dale | Elephant Court / Spice Village | Luxury Private Houseboat | Turtle on the Beach / Isola Di Cocco | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                "Fragrant Nature / Chandy's Windy Woods | Cardamom County / Niraamaya Wilderness | Ultra Luxury Houseboat | The Leela Kovalam / T",
                'Munnar | Thekkady | Alleppey | Kovalam',
                '2N Munnar|1N Thekkady|1N Alleppey|1N Kovalam',
                'Luxury',
                'Executive Suite / Garden Cottage / Suite AC Cruise Cabin / Garden View Pavilion',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description="OPTION 03 – LUXURY: Fragrant Nature / Chandy's Windy Woods | Cardamom County / Niraamaya Wilderness | Ultra Luxury Houseboat | The Leela Kovalam / Taj Green Cove | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                'Elixir Hills / Windermere Estate | Spice Village - CGH Earth | Xandari Riverscapes Houseboat | The Leela Kovalam / Taj Green Cov',
                'Munnar | Thekkady | Alleppey | Kovalam',
                '2N Munnar|1N Thekkady|1N Alleppey|1N Kovalam',
                'Ultra Luxury',
                'Private Pool Suite / Private Spice Garden Villa / Ultra Premium Premium Deck / Club Premium Sea View Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Elixir Hills / Windermere Estate | Spice Village - CGH Earth | Xandari Riverscapes Houseboat | The Leela Kovalam / Taj Green Cove | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Accommodation: Double sharing in premium handpicked hotels.', 1),
            _inc_included('Private Houseboat: Fully exclusive luxury cruise in Alleppey.', 2),
            _inc_included('Meal Plan: Daily breakfast and dinners at resorts; all meals onboard houseboat.', 3),
            _inc_included('Luxury Transportation: Private AC premium vehicle for all transfers and tours.', 4),
            _inc_included('Welcome Amenities: Honeymoon cake, floral bed decoration, and candlelit setup.', 5),
            _inc_included('Curated Experiences: Guided spice plantation walk and tea estate trail.', 6),
            _inc_included('TRAGUIN Support: 24/7 dedicated local concierge assistance.', 7),
            _inc_included('Taxes: All current fuel, toll, parking, and luxury hospitality taxes.', 8),
            _inc_excluded('Flights / Train: Domestic or international airfares.', 9),
            _inc_excluded('Entry Tickets: Historic monument fees, national park tickets.', 10),
            _inc_excluded('Optional Activities: Kathakali shows, boat rides, adventure sports.', 11),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, alcoholic beverages, tipping.', 12),
            _inc_excluded('Surge Charges: Peak festive season surcharges (if applicable).', 13),
            _inc_excluded('Insurance: Travel, medical, or baggage loss insurance.', 14),
        ],
    )
    return package, itinerary

def build_kl_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-007'
    tour_code = 'TG-KRL-MNNR-06D'
    title = 'Munnar Thekkady Alleppey Honeymoon'
    duration = '05 Nights / 06 Days'
    slug = 'kl-007-munnar-thekkady-alleppey-honeymoon'
    itin_slug = 'kl-007-munnar-thekkady-alleppey-honeymoon-itinerary'
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
            _ph('Serial code KL-007 | TRAGUIN tour code TG-KRL-MNNR-06D', 1),
            _ph('State / Country: Kerala / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Jharkhand', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Air-conditioned premium vehicle for all transfers, airport pickups, and daily sightseeing. ✔TRAGUIN Honeymoon Elements: Complimentary honeymoon cake, floral bed decor, and a candle-lit dining experience. ✔Elite Logistics: Inclusive of fuel charges, interstate toll taxes, driver night bata, and private parking fees. ✔24/7 Dedicated Support: Direct concierge access to senior TRAGUIN tour managers throughout. ✘ PACKAGE EXCLUSIONS ✘Airfare / Train Tickets: Domestic or international flight tickets to/from Cochin. ✘Monument Fees: Entry tickets to national parks, museums, boating, and sanctuary cruises. ✘Personal Expenses: Laundry service, telephone calls, premium alcoholic beverages, and tipping. ✘Optional Activities: Adventure sports, Ayurvedic wellness spa procedures, or alternative safaris. ✘Surcharges: Any peak festive season hikes or mandatory gala dinners (Christmas/New Year). ✘Insurance: Travel or medical insurance coverage plans. SPECIAL TRAGUIN SIGNATURE HIGHLIGHTS Curated by TRAGUIN Experts: Every route and property is personally vetted by destination experts to guarantee a flawless, elite guest experience. Premium Handpicked Hotels: Properties are hand-selected based on exceptional hospitality ratings, premium locales, and stunning panoramic views. Bespoke Personalized Assistance: You receive an elite, dedicated digital concierge service handling seamless check-ins, local restaurant table bookings, and unexpected adjustments. Luxury Transportation: Highly professional, knowledgeable, and courteous local multi-lingual drivers who function as excellent local guides. ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪', 7)
        ],
        moods=['Romantic', 'Honeymoon', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Munnar Thekkady Alleppey Honeymoon',
        overview="05 Nights / 06 Days Luxury Romantic Escapade SERIAL CODE: KL-007 TRAGUIN TOUR CODE: TG-KRL-MNNR-06D STATE / COUNTRY: Kerala / India Category: Honeymoon / Premium Luxury DURATION: 05 Nights / 06 Days Destinations Covered: Cochin • Munnar • Thekkady • Alleppey IDEAL FOR: Munnar Luxury Couple / Honeymooners Best Season: September to May (All Year Allure) STARTING PRICE: On Request (Premium Curated) Meal Plan: MAPAI (Breakfast & Dinner) / All Meals in Houseboat Welcome to an enchanting romantic saga sketched across God's Own Country. Designed exclusively for discerning lovebirds, this Best Kerala Tour Package unfolds like a classic love poem. From the emerald velvet hills of Munnar wrapped in misty embraces to the legendary tranquil backwaters of Alleppey, every single detail has been intricately stitched together. Let TRAGUIN elevate your celebration of togetherness with bespoke intimacy, premium stays, and mesmerizing local immersive experiences that turn fleeting moments into lifelong treasures. TRAGUIN • Premium Travel & Luxury Holidays\n\nTOUR OVERVIEW\nThis flagship TRAGUIN Kerala Packages itinerary is engineered to deliver a seamless blend of relaxation, premium luxury, and curated exploration. Handpicked for a premium Munnar Luxury Couple experience, the journey covers Kerala's most iconic attractions using an elite private chauffeur-driven vehicle and stays at ultra-refined properties. Route Profile Cochin Arrival → Munnar (2N) → Thekkady (1N) → Alleppey Houseboat (1N) → Cochin Departure (1N) Vehicle Details Premium Executive Air-Conditioned Sedan / Luxury SUV (Private Chauffeur) Group Type FIT - Exclusive Private Couple Tour (Honeymoon Special) TRAGUIN Touch Complimentary honeymoon cake, romantic floral bed decoration, candle-lit dining, and 24/7 dedicated guest relations assistance.\n\nWHY BOOK A LUXURY KERALA HOLIDAY WITH TRAGUIN?\nKerala stands globally acclaimed as one of the ultimate romance capitals. A customized Kerala Honeymoon Package offers an unmatched tapestry of diverse terrains—cool high-altitude hill stations, exotic wildlife sanctuaries, and pristine backwaters—all within close proximity. Most Searched Experiences & Top Tourist Places in Kerala: Munnar Sightseeing: Walking hand-in-hand through the iconic tea fields of Eravikulam National Park and capturing memories at Mattupetty Dam. Popular Instagram Locations: The majestic, roaring cascades of Athirappilly Waterfalls, the breathtaking sunrise views from Lock Heart Gap, and sunset over the Arabian Sea at Fort Cochin. Romantic Culture & Highlights: Traditional Kathakali performances, rejuvenating Ayurvedic couple therapies, and shopping for authentic spices and premium handloom sarees in local markets. With the tailored Premium Kerala Experience by TRAGUIN, you transcend ordinary sightseeing. We bypass the crowds to introduce you to secret vantage points, gourmet culinary experiences, and exquisite handpicked hotels that turn your vacation into a grand luxury celebration. ▪ ▪ ▪ TRAGUIN • Premium Travel & Luxury Holidays",
        seo_title='KL-007 | Munnar Thekkady Alleppey Honeymoon | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Kerala package (KL-007 / TG-KRL-MNNR-06D): Jharkhand with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: COCHIN ARRIVAL TO MUNNAR', 1),
            _ih('Day 02: MUNNAR SIGHTSEEING', 2),
            _ih('Day 03: MUNNAR TO THEKKADY', 3),
            _ih('Day 04: THEKKADY TO ALLEPPEY HOUSEBOAT', 4),
            _ih('Day 05: ALLEPPEY TO COCHIN', 5),
            _ih('Day 06: COCHIN DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'COCHIN ARRIVAL TO MUNNAR',
                (
                    "Your spectacular Kerala Family Tour and romantic holiday begins as you land at Cochin International Airport. You will be warmly received with traditional hospitality by a specialized TRAGUIN representative. Step into your premium luxury private vehicle and set forth on a visually stunning scenic route toward Munnar—the crown jewel of South India's hill stations. As the road winds upwards, witness the dramatic landscape transformation from bustling coastal plains into rolling layers of emerald hills. En route, make a stop at the breathtaking Cheeyappara and Valara Waterfalls, where sheets of water tumble down rocky cliffs amid dense forests, offering the perfect backdrop for your first couple photography points. Arrive in Munnar, breathe in the crisp, spice-scented mountain air, and check into your handpicked ultra-luxury resort. Enjoy a private, hassle-free check-in experience. Waterfalls, Scenic Neriamangalam Bridge, Tea Valley Viewpoint. plantation walk or traditional Kalaripayattu martial arts show. resort lounge followed by a gourmet multi-cuisine dinner. Munnar."
                ),
                [
                    'Sightseeing Included: Cheeyappara & Valara',
                    'Optional Activities: Evening organic spice',
                    'Evening Experience: A cozy, relaxing evening at the',
                    'Overnight Stay: Handpicked Luxury Resort in',
                    'Meals Included: Welcome Drink & Dinner',
                ],
            ),
            _day(
                2,
                'MUNNAR SIGHTSEEING',
                (
                    'Wake up to the gentle chirping of exotic birds and hills draped gracefully in morning fog. Today is dedicated to an extensive, premium Munnar Sightseeing experience. After a lavish spread for breakfast, visit the famous Eravikulam National Park (Rajamalai), the natural sanctuary of the endangered Nilgiri Tahr. Walk hand-in-hand along the beautifully paved hill pathways soaking in the panoramic vistas of the Anamudi Peak. Later, stop by the fascinating Tata Tea Museum to learn about the heritage of tea crafting. Continue your romance-filled afternoon visiting the serene Mattupetty Dam and Lake, where you can opt for a high- speed private boat ride. Pause at Eco Point to hear your names echo across the tranquil waters and forests, and take a romantic stroll around Kundala Lake. Wrap up your day with local food suggestions Gateway to the Misty Mountains & Valleys of Love Exploring the Endless Emerald Tea Carpets & Wildlife Encounters TRAGUIN • Premium Travel & Luxury Holidays like authentic Malabar parotta with curries or freshly brewed plantation coffee at a premium boutique cafe. Mattupetty Dam, Eco Point, Kundala Lake, Tea Museum, Blossom Hydel Park. Mattupetty, traditional couple attire photography in tea gardens. arranged by TRAGUIN: a private Candle-lit dinner amidst nature. Munnar. TRAGUIN • Premium Travel & Luxury Holidays'
                ),
                [
                    'Sightseeing Included: Eravikulam National Park,',
                    'Optional Activities: Private speed boating at',
                    'Evening Experience: A bespoke romantic surprise',
                    'Overnight Stay: Premium Luxury Resort in',
                    'Meals Included: Breakfast & Romantic Candle-lit Dinner',
                ],
            ),
            _day(
                3,
                'MUNNAR TO THEKKADY',
                (
                    "Bid a temporary farewell to the misty heights of Munnar as your Luxury Kerala Holiday progresses down toward Thekkady (Periyar), India's premier spice and wildlife wonderland. The driving route is an absolute feast for the eyes, characterized by sweeping views of deep valleys, dramatic ridges, and sprawling commercial plantations of cardamom, pepper, and cinnamon. Upon entering Thekkady, check into your ultra-premium jungle resort that perfectly blends rustic wilderness with sophisticated high-end luxury. In the afternoon, head out for an unforgettable boat cruise across the scenic Periyar Lake. Keep your cameras primed at the photography points to capture herds of wild elephants, bison, sambar deer, and rare waterbirds drinking along the water's edge. Later, explore the vibrant local spice markets for premium souvenirs. Periyar Lake Cruise, Spice Plantation Tour. guided jungle night trekking, Kathakali cultural dance show. markets followed by an authentic Keralan clay-pot dining experience. Thekkady."
                ),
                [
                    'Sightseeing Included: Periyar Wildlife Sanctuary,',
                    'Optional Activities: Elephant bathing experience,',
                    'Evening Experience: Exploring bustling local',
                    'Overnight Stay: Elite Wilderness Resort in',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'THEKKADY TO ALLEPPEY HOUSEBOAT',
                (
                    'Prepare your senses for the absolute highlight of your Destination Honeymoon Package. After a hearty breakfast, drive down the hills to Alleppey (Alappuzha), fondly referred to as the Venice of the East. At noon, step aboard your private, ultra-luxury, handpicked traditional Kettuvallam (Houseboat), floating gracefully on the pristine waters of the Vembanad Lake. As your private floating palace glides through intricate networks of canals, look out at vibrant green paddy fields, towering coconut groves, and charming lakeside hamlets. Your dedicated on-board master chef will prepare exquisite local culinary masterpieces using fresh local catch and organic farm produce. Sip tender coconut water, recline on the sun deck, and watch one of the most spectacular, globally acclaimed sunsets over the backwaters. This is the ultimate TRAGUIN Signature Experience. Backwater Canals, Pathiramanal Island view. village canoe ride, authentic Toddy shop visit. anchorage over the calm, glass-like backwaters. (Full AC). Journey Through Spice-Scented Woods & Pristine Wildlife Sanctums Cruising the Majestic Emerald Backwaters in Absolute Privacy TRAGUIN • Premium Travel & Luxury Holidays TRAGUIN • Premium Travel & Luxury Holidays'
                ),
                [
                    'Sightseeing Included: Vembanad Lake, Alleppey',
                    'Optional Activities: Traditional narrow-canal',
                    'Evening Experience: Star-lit peaceful night',
                    'Overnight Stay: Private Ultra-Luxury Houseboat',
                    'Meals Included: Breakfast, Traditional Lunch, Evening Snacks & Luxury Seafood Dinner',
                ],
            ),
            _day(
                5,
                'ALLEPPEY TO COCHIN',
                (
                    'Enjoy your morning coffee as the houseboat gently glides back toward the jetty. Disembark after a memorable breakfast and travel back to the historic port city of Cochin. Known as the Queen of the Arabian Sea, Cochin flawlessly fuses old-world colonial charm with ultra-modern coastal luxury. Check into your ultra-luxury heritage hotel in Fort Cochin or a contemporary waterfront property. Spend your afternoon uncovering centuries of history. Visit the legendary Fort Cochin Beach and the iconic Chinese Fishing Nets, which stand tall as monuments of ancient global maritime trade. Wander through the artistic streets of Mattancherry, marvel at the murals inside the Dutch Palace, explore the historic Jewish Synagogue, and stroll through Jew Town shopping for exquisite antiques and essential oils. Francis Church, Santa Cruz Basilica, Mattancherry Dutch Palace, Jewish Synagogue & Jew Town. Sea sunset harbor cruise, upscale seafood fine-dining. global cafes along the Fort Cochin walkways. Hotel in Cochin.'
                ),
                [
                    'Sightseeing Included: Fort Cochin Chinese Fishing Nets, St.',
                    'Optional Activities: Luxury Arabian',
                    'Evening Experience: Fine boutique shopping and exploring chic',
                    'Overnight Stay: High-End Premium',
                    'Meals Included: Breakfast & Gourmet Farewell Dinner',
                ],
            ),
            _day(
                6,
                'COCHIN DEPARTURE',
                (
                    "Your magical, premium journey through paradise draws to a gentle close today. Savor your lavish spread for breakfast at the hotel, reflecting upon the incredible sights, deep relaxation, and enchanting moments you've experienced over the last six days. Depending on your flight timings, you can complete some last-minute high-end souvenir shopping at LuLu Mall, Asia’s premier shopping mall destination, purchasing world-famous Kerala banana chips, aromatic spices, and traditional artifacts. Your private chauffeur will then drive you smoothly to Cochin International Airport for your onward flight home. You depart with a rejuvenated soul and a treasure chest of unforgettable memories curated meticulously by TRAGUIN. (Time permitting). relaxation. memories. Colonial Heritage, Coastal Allure & Vibrant City Life Cherishing Unforgettable Memories of God's Own Country TRAGUIN • Premium Travel & Luxury Holidays TRAGUIN • Premium Travel & Luxury Holidays"
                ),
                [
                    'Sightseeing Included: Lulu Mall or local handicraft emporium visit',
                    'Optional Activities: Airport lounge',
                    'Evening Experience: Safe flight back home with wonderful',
                    'Overnight Stay: None.',
                    'Meals Included: Premium Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Leaf Munnar / Amber Dale Luxury Resort | Elephant Court / Poetree Sarovar Portico | Premium Private Houseboat Alliance | Tri',
                'Munnar | Thekkady | Alleppey | Cochin',
                '2N Munnar|1N Thekkady|1N Alleppey|1N Cochin',
                'Deluxe',
                'Valley View Room / Patio Room / Deluxe AC Cabin / Superior Room',
                'MAPAI',
                4,
                1,
                description='OPTION 01 – DELUXE: The Leaf Munnar / Amber Dale Luxury Resort | Elephant Court / Poetree Sarovar Portico | Premium Private Houseboat Alliance | Trident Cochin / Radisson Blu | MAPAI',
            ),
            _hotel(
                'Fragrant Nature Munnar / Elixir Hills Suites | Greenwoods Resort / Spice Village CGH Earth | Luxury Cruise Lines Alleppey | Brun',
                'Munnar | Thekkady | Alleppey | Cochin',
                '2N Munnar|1N Thekkady|1N Alleppey|1N Cochin',
                'Premium',
                'Tropic Green Suite / Aranya Room / Premium Glass-Wall AC / Sea Facing Room',
                'MAPAI',
                4,
                2,
                description='OPTION 02 – PREMIUM: Fragrant Nature Munnar / Elixir Hills Suites | Greenwoods Resort / Spice Village CGH Earth | Luxury Cruise Lines Alleppey | Brunton Boatyard CGH Earth / Casino Hotel | MAPAI',
            ),
            _hotel(
                "Blanket Hotel & Spa / Chandy's Windy Woods | The Niraamaya Retreats Cardamom Club | Our Land Island Resort / Xandari Riverscapes",
                'Munnar | Thekkady | Alleppey | Cochin',
                '2N Munnar|1N Thekkady|1N Alleppey|1N Cochin',
                'Luxury',
                'Executive Suite / Luxury Garden Cottage / Ultra Luxury Houseboat / Club Lake View Room',
                'MAPAI',
                5,
                3,
                description="OPTION 03 – LUXURY: Blanket Hotel & Spa / Chandy's Windy Woods | The Niraamaya Retreats Cardamom Club | Our Land Island Resort / Xandari Riverscapes | Grand Hyatt Bolgatty / Kochi Marriott | MAPAI",
            ),
            _hotel(
                'Windermere Estate / Spice Tree Munnar | The Elephant Court Elite Pool Villas | Kumarakom Lake Resort / Spice Coast Cruises | The',
                'Munnar | Thekkady | Alleppey | Cochin',
                '2N Munnar|1N Thekkady|1N Alleppey|1N Cochin',
                'Ultra Luxury',
                'Private Pool Villa / Private Pool Suite / Presidential Suite Cruise / Grand Harbour Suite',
                'MAPAI',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Windermere Estate / Spice Tree Munnar | The Elephant Court Elite Pool Villas | Kumarakom Lake Resort / Spice Coast Cruises | The Brunton Boatyard Premium Sea Suites | MAPAI',
            )
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Stays at handpicked elite luxury properties listed above.', 1),
            _inc_included('Curated Meal Plans: Decadent daily breakfast & gourmet dinners at resorts.', 2),
            _inc_included('All-Inclusive Houseboat: Breakfast, traditional lunch, high tea, snacks, and seafood dinner on board.', 3),
            _inc_included('Private Luxury Vehicle: Air-conditioned premium vehicle for all transfers, airport pickups, and daily sightseeing.', 4),
            _inc_included('TRAGUIN Honeymoon Elements: Complimentary honeymoon cake, floral bed decor, and a candle-lit dining experience.', 5),
            _inc_included('Elite Logistics: Inclusive of fuel charges, interstate toll taxes, driver night bata, and private parking fees.', 6),
            _inc_included('24/7 Dedicated Support: Direct concierge access to senior TRAGUIN tour managers throughout.', 7),
            _inc_excluded('Airfare / Train Tickets: Domestic or international flight tickets to/from Cochin.', 8),
            _inc_excluded('Monument Fees: Entry tickets to national parks, museums, boating, and sanctuary cruises.', 9),
            _inc_excluded('Personal Expenses: Laundry service, telephone calls, premium alcoholic beverages, and tipping.', 10),
            _inc_excluded('Optional Activities: Adventure sports, Ayurvedic wellness spa procedures, or alternative safaris.', 11),
            _inc_excluded('Surcharges: Any peak festive season hikes or mandatory gala dinners (Christmas/New Year).', 12),
            _inc_excluded('Insurance: Travel or medical insurance coverage plans.', 13),
        ],
    )
    return package, itinerary

def build_kl_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-008'
    tour_code = 'TRAGUIN-KL-WE-008'
    title = 'Kerala Wellness Escape'
    duration = '05 Nights / 06 Days'
    slug = 'kl-008-kerala-wellness-escape'
    itin_slug = 'kl-008-kerala-wellness-escape-itinerary'
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
            _ph('Serial code KL-008 | TRAGUIN tour code TRAGUIN-KL-WE-008', 1),
            _ph('State / Country: Kerala / India | Category: Female Only Wellness', 2),
            _ph('Destinations: Munnar • Thekkady • Alleppey • Cochin', 3),
            _ph('Ideal for: Women Solo Travelers & Girl Groups', 4),
            _ph('Best season: September to March', 5),
            _ph('Starting price: On Request (Premium Luxury)', 6),
            _ph('Vehicle / Meals: Premium Chauffeur- Driven Luxury SUV', 7),
            _ph('TRAGUIN Signature Experience: A completely private, high-security, meticulously verified luxury', 8),
            _ph('TRAGUIN Premium Luxury Holidays', 9),
            _ph('& BOOKING POLICIES', 10),
            _ph('Hotel Check-in/out: Standard Check-in is at 14:00 hrs and Check-out is at 11:00 hrs. Early arrivals are strictly subject to', 11)
        ],
        moods=['Wellness', 'Luxury', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Luxury)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Kerala Wellness Escape',
        overview='E sc ape Welcome to an ultra-exclusive, female-focused rejuvenation journey meticulously handcrafted by TRAGUIN. This bespoke Kerala Wellness Escape is thoughtfully conceptualized for the modern woman seeking a sanctuary of peace, mindfulness, and luxury. From the mist-kissed emerald slopes of Munnar to the spice- scented air of Thekkady, and the tranquil, mirror-like waters of Alleppey, immerse your senses in a blissful blend of authentic Ayurvedic wellness, restorative luxury stays, and heartwarming local cultural interactions. Allow TRAGUIN to handle every fine detail while you rediscover your inner harmony in God’s Own Country.\n\nTOUR OVERVIEW\nThis curated luxury itinerary is tailor-made as a Private FIT tour, catering specifically to an all-female elite clientele who demand security, luxury, and cultural depth. Your journey unfolds across pristine landscapes, seamlessly shifting from mountain retreats to therapeutic backwater cruises. Every element of this trip features premium handpicked hotels, refreshing daily yoga sessions, customized organic meals, and curated experiences that guarantee unforgettable memories. Route Outline: Cochin Arrival ➔ Munnar (2 Nights) ➔ Thekkady (1 Night) ➔ Alleppey Houseboat (1 Night) ➔ Cochin (1 Night & Departure) TRAGUIN Premium Luxury Holidays Meal Plan: Modified American Plan (Breakfast & Gourmet Dinners included; All Meals included onboard Houseboat) TRAGUIN Curated Note: Includes a dedicated premium women-friendly professional English-speaking chauffeur, personalized welcome amenities, 24/7 concierge support, and signature Ayurvedic wellness consultations.\n\nWhy Choose the Best Kerala Tour Package for Women? Kerala is universally acclaimed as one of the safest,\nmost visually spectacular, and deeply rejuvenating tourist destinations across the globe. A Kerala Honeymoon Package offers legendary romanticism, but a specialized Kerala Family Tour or a dedicated Female Only Wellness Escape opens the gates to profound self-care and empowerment. Top Tourist Places in Kerala & Famous Attractions: This luxury itinerary covers iconic highlights including the breathtaking Eravikulam National Park (home to the endangered Nilgiri Tahr), the expansive Mattupetty Dam, the serene Periyar Wildlife Sanctuary, and the majestic Chinese Fishing Nets of historic Fort Cochin. Most Searched Experiences & Instagram Locations: Capture exquisite, viral-ready photographs at the world- renowned Kolukkumalai Tea Estate during a golden sunrise, strike a meditative pose on the sun-dappled deck of a luxury Alleppey Houseboat, or wander through the historic, art-strewn lanes of Jew Town in Cochin. This Luxury Kerala Holiday perfectly balances holistic wellness rituals, therapeutic spice plantation strolls, artisanal shopping tours, and world-class culinary masterclasses. Best Time to Visit Kerala: While the emerald state boasts a unique charm during the lush monsoon seasons for hardcore Ayurvedic treatments, the absolute premium window for general sightseeing and comfortable weather spans from late September through to the delightful breeze of March. TRAGUIN Premium Luxury Holidays DAY WISE ITINERARY',
        seo_title='KL-008 | Kerala Wellness Escape | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Kerala package (KL-008 / TRAGUIN-KL-WE-008): Munnar • Thekkady • Alleppey • Cochin with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: COCHIN TO MUNNAR', 1),
            _ih('Day 02: MUNNAR HILL STATION', 2),
            _ih('Day 03: MUNNAR TO THEKKADY', 3),
            _ih('Day 04: THEKKADY TO ALLEPPEY', 4),
            _ih('Day 05: ALLEPPEY TO COCHIN', 5),
            _ih('Day 06: COCHIN DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: A completely private, high-security, meticulously verified luxury', 7),
            _ih('TRAGUIN Premium Luxury Holidays', 8)
        ],
        days=[
            _day(
                1,
                'COCHIN TO MUNNAR',
                (
                    'ARRIVAL IN COCHIN & SCENIC ESCAPE TO THE EMERALD HILLS OF MUNNAR Your highly anticipated Kerala Wellness Escape commences with a grand welcome at Cochin International Airport by a designated TRAGUIN guest relations executive. Step into your premium, air-conditioned luxury SUV equipped with refreshing towels, healthy snacks, and organic refreshments. Begin your panoramic ascent towards Munnar, a mesmerizing hill station renowned globally for its breathtaking landscapes and expansive tea estates. As your vehicle glides through winding mountain passes, pause to witness the spectacular cascades of the Valara and Cheeyappara waterfalls, capturing stunning photographs amidst the mist. Upon arriving in Munnar, check into your ultra-luxury hillside resort. Sip on a complimentary local cardamom-infused welcome tea, unwind, and soak in the majestic mountain views. TRAGUIN Premium Luxury Holidays'
                ),
                [
                    'Sightseeing Included: Cheeyappara & Valara Waterfalls, Scenic Western Ghats Drive.',
                    'Evening Experience: Private orientation with an in-house wellness consultant to personalize your stay.',
                    'Overnight Stay: Handpicked Luxury Resort in Munnar.',
                    'Meals Included: Gourmet Dinner.',
                ],
            ),
            _day(
                2,
                'MUNNAR HILL STATION',
                (
                    'IMMERSIVE TEA EXPERIENCE, MIST-LADEN PEAKS & REJUVENATION Awaken to the soothing symphony of mountain birds and a refreshing sunrise yoga session tailored for all skill levels. Today’s premium Munnar Sightseeing tour delves deep into the soul of this iconic hill station. Visit the pristine Mattupetty Dam and the enchanting Echo Point, where your voice resonates beautifully across the mist-shrouded lake. Later, enjoy an exclusive, curated walk through a private tea estate, interacting with female tea pluckers and learning the delicate art of harvesting leaves. Conclude your afternoon at the Tata Tea Museum for a private tea-tasting session. Return to your luxury sanctuary for a signature deeply relaxing Ayurvedic Abhyangam massage, melting away any residual stress. gardens.'
                ),
                [
                    'Sightseeing Included: Mattupetty Dam, Echo Point, Kundala Lake, Tea Museum, Blossom Hydel Park.',
                    'Optional Activities: Soft trekking in the Letchmi Hills or a specialized professional photography session in the tea',
                    'Evening Experience: Interactive organic cooking demonstration highlighting traditional healthy Kerala cuisine.',
                    'Overnight Stay: Handpicked Luxury Resort in Munnar.',
                    'Meals Included: Breakfast & Gourmet Dinner.',
                ],
            ),
            _day(
                3,
                'MUNNAR TO THEKKADY',
                (
                    'JOURNEY THROUGH SPICE VALLEYS & PERIYAR WILDERNESS ELEVATION After a nourishing organic breakfast, checking out and embarking on a visually spectacular drive to Thekkady, the spice capital of India. The route is a sensory delight, punctuated by endless views of rubber, pepper, cardamom, and coffee plantations. Arrive at your premium boutique jungle resort by noon. In the afternoon, enjoy a privately guided walking tour through a lush spice plantation. Learn about the therapeutic and culinary properties of fresh spices, purchasing premium organic extracts directly from the source. In the evening, witness a captivating live performance of Kalaripayattu—the ancient, powerful martial art form of Kerala, celebrating raw strength and deep focus. TRAGUIN Premium Luxury Holidays'
                ),
                [
                    'Sightseeing Included: Spice Plantation Tour, Kalaripayattu Cultural Show.',
                    'Optional Activities: A serene, private boat cruise on the tranquil waters of Periyar Lake.',
                    'Evening Experience: Aromatherapy spa treatment using freshly distilled local oils at the resort wellness center.',
                    'Overnight Stay: Premium Eco-Luxury Resort in Thekkady.',
                    'Meals Included: Breakfast & Gourmet Dinner.',
                ],
            ),
            _day(
                4,
                'THEKKADY TO ALLEPPEY',
                (
                    'LUXURY ALLEPPEY HOUSEBOAT EMBARKATION & SERENE BACKWATER ODYSSEY Bid farewell to the hills as your TRAGUIN chauffeur expertly guides your vehicle down to Alleppey, the world- famous "Venice of the East." Here, an extraordinary highlight awaits: step on board an exclusive, private premium luxury houseboat configured perfectly for your utmost privacy and comfort. Set sail through an intricate network of emerald canals, vast glassy lakes, and pristine lagoons. Observe the slow, graceful rhythm of local life along the banks—women weaving coir, fishermen in traditional canoes, and endless rows of swaying coconut palms. Feast on a lavish, freshly prepared traditional lunch onboard, featuring exotic local flavors and freshwater delicacies curated by your private onboard chef. water. TRAGUIN Premium Luxury Holidays'
                ),
                [
                    'Sightseeing Included: Alleppey Backwaters, Rural Village Vistas, Vembanad Lake.',
                    'Optional Activities: Guided village walk or a traditional narrow canoe ride down the ultra-thin, peaceful canals.',
                    'Evening Experience: Watch a majestic, golden sunset from the upper deck, followed by a candlelit dinner on the',
                    'Overnight Stay: Premium Private Houseboat (Air-conditioned).',
                    'Meals Included: Breakfast, Traditional Lunch, Evening Snacks & Luxury Dinner.',
                ],
            ),
            _day(
                5,
                'ALLEPPEY TO COCHIN',
                (
                    'HISTORIC FORT COCHIN COLONIAL CHRONICLES & HERITAGE ENCOUNTERS Wake up to the soft lap of waves against your boat and enjoy a peaceful morning breakfast on the water. Disembark and drive back to the vibrant heritage city of Cochin. Check into an exquisite, premium boutique heritage hotel located right in the heart of historic Fort Cochin. Spend your afternoon exploring the rich, multi-cultural tapestry of this coastal city. Stroll down to see the iconic Chinese Fishing Nets, marvel at the ancient murals inside the Mattancherry Dutch Palace, and walk through the historic paths of the Jewish Synagogue. Cochin is renowned for its incredible cafes and fine dining scene, offering excellent opportunities to unwind and celebrate your final evening together. cuisine.'
                ),
                [
                    'Sightseeing Included: Fort Cochin, Chinese Fishing Nets, Dutch Palace, Jewish Synagogue, St. Francis Church.',
                    'Optional Activities: A classical evening Kathakali dance drama show or an exclusive high-end boutique garment',
                    'shopping: tour.',
                    'Evening Experience: Farewell dinner at a celebrated fine-dining restaurant featuring modern coastal fusion',
                    'Overnight Stay: Premium Heritage Hotel in Cochin.',
                    'Meals Included: Breakfast & Farewell Dinner.',
                ],
            ),
            _day(
                6,
                'COCHIN DEPARTURE',
                (
                    'MINDFUL REFLECTIONS & FOND FAREWELL TO GOD’S OWN COUNTRY Savor a leisurely breakfast at your heritage hotel, reflecting on the peaceful transformations, unforgettable memories, and deep bonds forged over the past six days. Depending on your flight schedule, enjoy some last-minute luxury souvenir shopping in Jew Town, collecting high-grade essential oils, premium spices, and traditional handwoven Kasavu sarees. Your dedicated TRAGUIN chauffeur will then drive you comfortably to Cochin International Airport for your onward journey home, carrying a renewed spirit and radiant energy. TRAGUIN Premium Luxury Holidays'
                ),
                [
                    'Sightseeing Included: Flexible morning shopping and cafe hops based on departure timing.',
                    'Meals Included: Premium Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Fog Munnar (Valley View Room) | Elephant Court (Patio Room) | Premium A/C Luxury Houseboat | Trident Cochin (Superior Room)',
                'Munnar | Thekkady | Alleppey | Cochin',
                '2N Munnar|1N Thekkady|1N Alleppey|1N Cochin',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: The Fog Munnar (Valley View Room) | Elephant Court (Patio Room) | Premium A/C Luxury Houseboat | Trident Cochin (Superior Room) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Blanket Hotel & Spa | Spice Village | Ultra-Luxury Private Houseboat | Fragrant Nature Cochin',
                'Munnar | Thekkady | Alleppey | Cochin',
                '2N Munnar|1N Thekkady|1N Alleppey|1N Cochin',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Blanket Hotel & Spa | Spice Village | Ultra-Luxury Private Houseboat | Fragrant Nature Cochin | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                "Chandy's Windy Woods | Cardamom County | TRAGUIN Signature Cruise | Brunton Boatyard",
                'Munnar | Thekkady | Alleppey | Cochin',
                '2N Munnar|1N Thekkady|1N Alleppey|1N Cochin',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description="OPTION 03 – LUXURY: Chandy's Windy Woods | Cardamom County | TRAGUIN Signature Cruise | Brunton Boatyard | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                'The Panoramic Getaway | Niraamaya Cardamom Club | Elite Glass-Enclosed Vessel | Malabar House',
                'Munnar | Thekkady | Alleppey | Cochin',
                '2N Munnar|1N Thekkady|1N Alleppey|1N Cochin',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Panoramic Getaway | Niraamaya Cardamom Club | Elite Glass-Enclosed Vessel | Malabar House | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Luxury accommodation in handpicked top-rated female-friendly resorts.', 1),
            _inc_included('Daily buffet breakfasts and expertly curated nutritious gourmet dinners.', 2),
            _inc_included('All meals included during the luxury Alleppey Houseboat stay.', 3),
            _inc_included('Premium private Chauffeur-driven luxury SUV for all transfers and sightseeing.', 4),
            _inc_included('Complimentary traditional Ayurvedic wellness consultation upon arrival.', 5),
            _inc_included('Complimentary guided organic Spice Plantation tour in Thekkady.', 6),
            _inc_included('Special welcome amenities and premium TRAGUIN on-ground support.', 7),
            _inc_included('All current fuel, toll, parking, and driver allowances included.', 8),
            _inc_excluded('Domestic or International airfares and train tickets.', 9),
            _inc_excluded('Entry tickets to monuments, museums, and national parks.', 10),
            _inc_excluded('Personal expenses like laundry, phone calls, and alcoholic beverages.', 11),
            _inc_excluded('Optional activities, specialized treks, or extra spa treatments.', 12),
            _inc_excluded('Any camera or video tracking fees at sight locations.', 13),
            _inc_excluded('Travel and medical insurance policies.', 14),
            _inc_excluded('GST/TCS or extra regulatory taxes if applicable.', 15),
        ],
    )
    return package, itinerary

def build_kl_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-009'
    tour_code = 'TRAGUIN-KL-SR-009'
    title = 'Cochin • Munnar • Kumarakom • Alleppey — Relax Kerala Passage'
    duration = '05 Nights / 06 Days'
    slug = 'kl-009-senior-citizen-kumarakom-relaxed'
    itin_slug = 'kl-009-senior-citizen-kumarakom-relaxed-itinerary'
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
            _ph('Serial code KL-009 | TRAGUIN tour code TRAGUIN-KL-SR-009', 1),
            _ph('State / Country: Kerala / India | Category: Senior Citizen Relaxed', 2),
            _ph('Destinations: Cochin • Munnar • Kumarakom • Alleppey', 3),
            _ph('Ideal for: Seniors, Elders & Relaxed Families', 4),
            _ph('Best season: October to March (Pleasant Breeze)', 5),
            _ph('Starting price: Premium Luxury Tier (On Request)', 6),
            _ph('Vehicle / Meals: Ultra-Comfortable Full- Sized Luxury Captain- Seat Van', 7),
            _ph('TRAGUIN experts.', 8),
            _ph('TRAGUIN Signature Experience: A thoroughly personalized, stress-free travel plan designed', 9),
            _ph('Curated by TRAGUIN Experts: Handpicked properties featuring elevators, flat walkways, excellent', 10),
            _ph('TRAGUIN Luxury Proposals | Senior Citizens Special', 11),
            _ph('& RESORT POLICIES', 12),
            _ph('Check-In/Check-Out: Standard check-in is at 14:00 hrs and check-out is at 11:00 hrs. Early access can be requested', 13)
        ],
        moods=['Family', 'Luxury', 'Wellness'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='Premium Luxury Tier (On Request)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Cochin',
        overview='Welcome to a gracefully paced, ultra-comfortable journey through God’s Own Country, uniquely designed and masterfully curated by TRAGUIN. This "Relax Kerala" passage is purposefully designed for senior citizens and discerning travelers who appreciate premium stays, majestic vistas, and immersive experiences without any rushed schedules. From slow-paced walks among the tea gardens of Munnar to the therapeutic breeze over the backwaters of Kumarakom and Alleppey, every aspect focuses on ease, accessibility, and luxury. Let TRAGUIN take care of all details while you make unforgettable memories in complete comfort.\n\nTOUR OVERVIEW\nThis elite itinerary operates as a private, high-end FIT tour designed specifically to ensure zero fatigue, minimal walking stress, and maximum luxury for our senior guests. Traveling via a premium, extra-cushioned vehicle with an experienced, highly courteous personal chauffeur, your route bypasses difficult terrains in favor of smooth, scenic beauty. Route Map: Cochin Arrival ➔ Munnar (2 Nights) ➔ Kumarakom Backwater Resort (2 Nights) ➔ Alleppey Day Cruise ➔ Cochin (1 Night & Departure) Meal Plan: Premium MAPAI (Sumptuous Breakfast & Custom Low-Spice Gourmet Dinners included; Full Board on Cruise) TRAGUIN Luxury Proposals | Senior Citizens Special TRAGUIN Curated Experience Note: Features step-free or ground-floor luxury room assignments, light traditional Ayurvedic oil treatments, highly flexible departure timings, wheel-chair accessibility options at major sights, and round-the- clock remote concierge care.\n\nWhy Choose the Best Kerala Tour Package for Seniors? Kerala is highly searched as a safe, peaceful, and\nclean haven for elderly travelers. A tailored Kerala Family Tour or a dedicated Premium Kerala Experience guarantees a perfect blend of slow exploration and absolute physical comfort. While a Kerala Honeymoon Package captures romance, our custom senior-citizen layout provides deep relaxation, clean traditional food, and accessible paths. Top Tourist Places in Kerala & Iconic Attractions: This custom package features access to world-famous sites such as the beautiful Mattupetty Lake, the historical Fort Cochin colonial quarters, the relaxing bird sanctuaries of Kumarakom, and the smooth, historic Chinese Fishing Nets. Most Searched Experiences & Popular Instagram Locations: Take stunning family and couple portraits against the majestic backdrop of tea plantations without steep climbing, enjoy a relaxing afternoon tea on a classic luxury houseboat cruise, or witness a private, seated Kathakali cultural show. This Luxury Kerala Holiday focuses heavily on serene lakeside properties, mild aromatic spice garden walks, handloom shopping, and fresh, easily digestible local dishes. Best Time to Visit Kerala: For senior travelers, the ideal months are from mid-October to early March when humidity levels drop and a gentle, pleasant breeze blows across the backwater lagoons. TRAGUIN Luxury Proposals | Senior Citizens Special DAY WISE ITINERARY',
        seo_title='KL-009 | Cochin | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Kerala package (KL-009 / TRAGUIN-KL-SR-009): Cochin • Munnar • Kumarakom • Alleppey with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: COCHIN TO MUNNAR', 1),
            _ih('Day 02: MUNNAR HILLS EXPLORATION', 2),
            _ih('Day 03: MUNNAR TO KUMARAKOM', 3),
            _ih('Day 04: KUMARAKOM LAKESIDE SERENITY', 4),
            _ih('Day 05: ALLEPPEY CRUISE TO COCHIN', 5),
            _ih('Day 06: COCHIN DEPARTURE', 6),
            _ih('TRAGUIN experts.', 7),
            _ih('TRAGUIN Signature Experience: A thoroughly personalized, stress-free travel plan designed', 8),
            _ih('Curated by TRAGUIN Experts: Handpicked properties featuring elevators, flat walkways, excellent', 9)
        ],
        days=[
            _day(
                1,
                'COCHIN TO MUNNAR',
                (
                    'WARM WELCOME AT COCHIN & SMOOTH DRIVE TO THE MIST-KISSED HILLS OF MUNNAR Your wonderful journey begins with a smooth arrival at Cochin International Airport, where a dedicated TRAGUIN guest relations officer will welcome you with fresh flower garlands. Step into a spacious, premium luxury vehicle featuring wide doors, step-stools, and captain-style seats. As you begin your smooth road trip toward Munnar, enjoy the changing scenery of rubber plantations and rolling hills. The drive features pre-mapped stops at scenic spots. Pause by the roadside to admire the beautiful Cheeyappara Waterfalls without needing to walk far. Arrive at your luxury mountain resort, check into your easily accessible room, and enjoy a warm cup of herbal tea while taking in the fresh mountain air.'
                ),
                [
                    'Sightseeing Included: Roadside views of Cheeyappara & Valara Falls, Western Ghats Scenic Drive.',
                    'Evening Experience: A relaxed evening at the resort garden terrace with light classical flute music.',
                    'Overnight Stay: Handpicked Senior-Friendly Luxury Resort in Munnar.',
                    'Meals Included: Custom Gourmet Dinner (Mild Spices).',
                ],
            ),
            _day(
                2,
                'MUNNAR HILLS EXPLORATION',
                (
                    'TEA GARDEN PANORAMAS, GENTLE LAKES & REFRESHING MOUNTAIN BREEZE Enjoy a relaxed morning breakfast overlooking the mist-filled valley. Today’s gentle Munnar Sightseeing tour avoids steep walking paths. Relax in your premium vehicle as you drive past expansive emerald tea estates. Stop at the calm Mattupetty Dam, where you can admire the lakeside view right from the promenade. Later, visit a historical tea museum featuring flat entry walkways, and watch an interesting film on how Munnar became a premier hill destination. In the afternoon, enjoy a flat, curated walk through a beautifully maintained organic spice and tea nursery, perfect for capturing memorable photos. methods. TRAGUIN Luxury Proposals | Senior Citizens Special'
                ),
                [
                    'Sightseeing Included: Mattupetty Dam viewpoint, Echo Point flat trail, Tea Museum, Lockhart Garden Gallery.',
                    'Optional Activities: A mild, refreshing Ayurvedic foot reflexology treatment at the resort wellness center.',
                    'Evening Experience: A private interactive session with a local tea master demonstrating artisanal brewing',
                    'Overnight Stay: Handpicked Senior-Friendly Luxury Resort in Munnar.',
                    'Meals Included: Breakfast & Gourmet Dinner.',
                ],
            ),
            _day(
                3,
                'MUNNAR TO KUMARAKOM',
                (
                    'DESCENT TO THE TRANQUIL LAKES AND PRESTIGIOUS RESORTS OF KUMARAKOM After a leisurely breakfast, check out of your resort. Your professional chauffeur will carefully guide the luxury vehicle down the smooth slopes toward Kumarakom, a peaceful destination located on the banks of Vembanad Lake. Arrive by afternoon at your luxury waterfront resort, famous for its senior-friendly layouts and flat walking paths. Check into your premium room or cottage. Spend the afternoon relaxing under shady coconut palms, listening to the gentle lapping of the lake waters, or watching local houseboats glide across the horizon. relaxation. onboard.'
                ),
                [
                    'Sightseeing Included: Scenic downhill drive, Kumarakom Lake Vistas.',
                    'Optional Activities: A gentle, authentic Ayurvedic full-body rejuvenation massage focusing on joint comfort and',
                    'Evening Experience: Relaxing sunset boat cruise directly from the resort jetty with traditional light snacks',
                    'Overnight Stay: Premium Waterfront Luxury Resort in Kumarakom.',
                    'Meals Included: Breakfast & Lakeside Dinner.',
                ],
            ),
            _day(
                4,
                'KUMARAKOM LAKESIDE SERENITY',
                (
                    "DAY OF ABSOLUTE REST, EXQUISITE BIRD SIGHTINGS & LAKESIDE MINDFULNESS A completely relaxed day designed to ensure you feel refreshed and rejuvenated. Wake up early for an optional, gentle chair-yoga or breathing session guided by an expert instructor. Enjoy a long breakfast featuring fresh tropical fruits and customized local specialties. In the afternoon, enjoy a short, electric-golf-cart tour of your expansive resort property, stopping to admire beautiful lotus ponds. Spend time relaxing with a book by the water, or take a gentle stroll around the resort's private walkways. TRAGUIN Luxury Proposals | Senior Citizens Special"
                ),
                [
                    'Sightseeing Included: Kumarakom Bird Sanctuary entry (accessible flat paths or golf-cart views where available).',
                    'Optional Activities: Pottery making, traditional indoor games, or a consultation with a traditional wellness expert.',
                    'Evening Experience: Watch a classic Kathakali dance performance from comfortable, reserved front-row seats.',
                    'Overnight Stay: Premium Waterfront Luxury Resort in Kumarakom.',
                    'Meals Included: Breakfast & Gourmet Dinner.',
                ],
            ),
            _day(
                5,
                'ALLEPPEY CRUISE TO COCHIN',
                (
                    'PREMIUM LUXURY ALLEPPEY HOUSEBOAT DAY CRUISE & HISTORIC COCHIN RETREAT After breakfast, take a short, comfortable drive to the nearby Alleppey boarding point. Step onto an exclusive, ultra-luxury private houseboat for a premium day cruise along the famous backwaters. The houseboat features single-level flat decks, wide seating areas, and fully air-conditioned interiors. Relax in comfort as the boat glides smoothly past peaceful water villages, historic churches, and vast paddy fields. Enjoy a freshly prepared, mild lunch curated by your onboard chef. In the afternoon, disembark and drive to your heritage hotel in Fort Cochin for a relaxed final evening. beach promenade.'
                ),
                [
                    'Sightseeing Included: 4-Hour Exclusive Backwater Cruise, Alleppey Lagoons, Fort Cochin Heritage Drive.',
                    'Evening Experience: A relaxed stroll to see the historic Chinese Fishing Nets at sunset, directly from the paved',
                    'Overnight Stay: Premium Heritage Luxury Hotel in Cochin.',
                    'Meals Included: Breakfast, Traditional Houseboat Lunch & Farewell Dinner.',
                ],
            ),
            _day(
                6,
                'COCHIN DEPARTURE',
                (
                    'FOND MEMORIES & A COMFORTABLE FAREWELL JOURNEY HOME Enjoy a relaxed breakfast at your heritage hotel. Depending on your flight schedule, take a smooth drive through Cochin’s old quarters. Stop at a luxury boutique center to purchase high-quality souvenirs such as premium handwoven shawls, local tea blends, or pure aromatic spices. Your dedicated TRAGUIN chauffeur will ensure a comfortable transfer to Cochin International Airport, assisting with your luggage to guarantee a smooth and stress-free journey home.'
                ),
                [
                    'Sightseeing Included: Flexible morning drive through Fort Cochin or localized boutique shopping.',
                    'Meals Included: Premium Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Fog Munnar (Ground Floor Valley) | Abad Whispering Palms (Garden Room) | Trident Cochin (Accessible Superior)',
                'Munnar | Kumarakom | Cochin',
                '2N Munnar|2N Kumarakom|1N Cochin',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: The Fog Munnar (Ground Floor Valley) | Abad Whispering Palms (Garden Room) | Trident Cochin (Accessible Superior) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Blanket Hotel & Spa (Executive Suite) | Kumarakom Lake Resort (Luxury Pavilion) | Fragrant Nature Cochin (Executive Room)',
                'Munnar | Kumarakom | Cochin',
                '2N Munnar|2N Kumarakom|1N Cochin',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Blanket Hotel & Spa (Executive Suite) | Kumarakom Lake Resort (Luxury Pavilion) | Fragrant Nature Cochin (Executive Room) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                "Chandy's Windy Woods (Premium Suite) | The Zuri Kumarakom (Waterfront Villa) | Brunton Boatyard (Heritage Room)",
                'Munnar | Kumarakom | Cochin',
                '2N Munnar|2N Kumarakom|1N Cochin',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description="OPTION 03 – LUXURY: Chandy's Windy Woods (Premium Suite) | The Zuri Kumarakom (Waterfront Villa) | Brunton Boatyard (Heritage Room) | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                'The Panoramic Getaway (Elite Suite) | Niraamaya Retreats Backwaters & Beyond | The Malabar House (Grand Premium Suite)',
                'Munnar | Kumarakom | Cochin',
                '2N Munnar|2N Kumarakom|1N Cochin',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Panoramic Getaway (Elite Suite) | Niraamaya Retreats Backwaters & Beyond | The Malabar House (Grand Premium Suite) | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Daily breakfasts and custom low-spice dinners at all resorts.', 1),
            _inc_included('A private 4-hour luxury Alleppey Houseboat day cruise with a custom lunch.', 2),
            _inc_included('A premium, extra-comfortable luxury vehicle with captain seating for all transport.', 3),
            _inc_included('An experienced, highly patient personal chauffeur trained for senior guest care.', 4),
            _inc_included('Complimentary traditional welcome amenities and healthy wellness drinks.', 5),
            _inc_included('A complimentary relaxing sunset cruise on Vembanad Lake.', 6),
            _inc_included('All fuel costs, road tolls, parking fees, and driver allowances.', 7),
            _inc_included('24/7 dedicated remote concierge support from TRAGUIN experts.', 8),
            _inc_included('Airfares, airport taxes, and train tickets.', 9),
            _inc_excluded('Luxury hotel stays with step-free or easily accessible ground-floor rooms.', 10),
            _inc_excluded('Entry tickets for monuments, historical palaces, or national parks.', 11),
            _inc_excluded('Personal expenses such as laundry, phone calls, and mineral water.', 12),
            _inc_excluded('Additional specialized medical, travel, or luggage insurance.', 13),
            _inc_excluded('Optional heavy treks or extra intensive spa therapies.', 14),
            _inc_excluded('Any camera or professional video equipment entry fees.', 15),
            _inc_excluded('GST, TCS, or any additional government regulatory taxes.', 16),
            _inc_excluded('TRAGUIN Signature Experience: A thoroughly personalized, stress-free travel plan designed specifically for senior citizens and elderly couples.', 17),
            _inc_excluded('✦ Curated by TRAGUIN Experts: Handpicked properties featuring elevators, flat walkways, excellent medical access, and exceptional hospitality standards.', 18),
        ],
    )
    return package, itinerary

def build_kl_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-010'
    tour_code = 'TG-WYN-ADV-2026'
    title = 'TRAGUIN Wayanad Adventure Escape'
    duration = '04 Nights / 05 Days'
    slug = 'kl-010-wayanad-adventure-escape'
    itin_slug = 'kl-010-wayanad-adventure-escape-itinerary'
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
            _ph('Serial code KL-010 | TRAGUIN tour code TG-WYN-ADV-2026', 1),
            _ph('State / Country: Kerala / India | Category: Adventure & Luxury Eco-', 2),
            _ph('Destinations: Jharkhand', 3),
            _ph('Ideal for: Adventure Seekers, Couples, Families', 4),
            _ph('Best season: September to May', 5),
            _ph('Starting price: INR 28,500/- Per Person PREMIUM KERALA TOUR PACKAGE TRAGUIN WAYANAD ADVENTURE ESCAPE 04 Nights / 05 Days of Curated Experiences & Breathtaking Landscapes Embark on an extraordinary journey with the Best Wayanad Tour Package, exclusively conceptualized by TRAGUIN to give you an immersive blend of high-octane thrill and pristine nature. Nestled amidst the Western Ghats, this Wayanad Honeymoon Package and Wayanad Family Tour unveils a world of misty mountains, cascading waterfalls, and uncharted wilderness. Our Luxury Wayanad Holiday is meticulously planned to take you through the finest Wayanad Sightseeing spots while wrapping you in absolute premium comfort. From trekking up rugged peaks to exploring prehistoric caves, every aspect of this Premium Wayanad Experience promises unforgettable memories. Experience the true definition of TRAGUIN • Premium Luxury Travel Proposals bespoke wanderlust through our signature TRAGUIN Wayanad Packages, designed for travelers who seek both the adrenaline of raw adventure and the solace of handpicked premium stays.', 6),
            _ph('Vehicle / Meals: Premium Private SUV (Innova Crysta)', 7),
            _ph('TRAGUIN Signature Experience: Private plantation walk with a senior horticulturist followed by', 8),
            _ph('Curated by TRAGUIN Experts: Strict safety audited equipment validation for all trekking, bamboo', 9),
            _ph('Personalized Assistance: Dynamic WhatsApp group integration combining driver, local operations', 10),
            _ph('Luxury Transportation: Sanitized vehicles equipped with premium upholstery, visual infotainment', 11),
            _ph('MAP Maximize your luxury itinerary by visiting the iconic Santhi Spice Markets in Sulthan Bathery and the boutique stores around Kalpetta. Highly recommended local culinary items include the famous Malabar Biryani, spicy Kozhikodan Halwa, and traditional Puttu with Kadala Curry at selected hygienic premium dine-outs recommended by your chauffeur. Do not miss buying authentic Wayanad Wild Honey, Bamboo artifacts, and freshly roasted single-origin Robusta coffee beans.', 12)
        ],
        moods=['Adventure', 'Nature', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='INR 28,500/- Per Person PREMIUM KERALA TOUR PACKAGE TRAGUIN WAYANAD ADVENTURE ESCAPE 04 Nights / 05 Days of Curated Experiences & Breathtaking Landscapes Embark on an extraordinary journey with the Best Wayanad Tour Package, exclusively conceptualized by TRAGUIN to give you an immersive blend of high-octane thrill and pristine nature. Nestled amidst the Western Ghats, this Wayanad Honeymoon Package and Wayanad Family Tour unveils a world of misty mountains, cascading waterfalls, and uncharted wilderness. Our Luxury Wayanad Holiday is meticulously planned to take you through the finest Wayanad Sightseeing spots while wrapping you in absolute premium comfort. From trekking up rugged peaks to exploring prehistoric caves, every aspect of this Premium Wayanad Experience promises unforgettable memories. Experience the true definition of TRAGUIN • Premium Luxury Travel Proposals bespoke wanderlust through our signature TRAGUIN Wayanad Packages, designed for travelers who seek both the adrenaline of raw adventure and the solace of handpicked premium stays.',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='TRAGUIN Wayanad Adventure Escape',
        overview="xtraordinary journey with the Best Wayanad Tour Package, exclusively conceptualized by TRAGUIN to give you an immersive blend of high-octane thrill and pristine nature. Nestled amidst the Western Ghats, this Wayanad Honeymoon Package and Wayanad Family Tour unveils a world of misty mountains, cascading waterfalls, and uncharted wilderness. Our Luxury Wayanad Holiday is meticulously planned to take you through the finest Wayanad Sightseeing spots while wrapping you in absolute premium comfort. From trekking up rugged peaks to exploring prehistoric caves, every aspect of this Premium Wayanad Experience promises unforgettable memories. Experience the true definition of TRAGUIN • Premium Luxury Travel Proposals bespoke wanderlust through our signature TRAGUIN Wayanad Packages, designed for travelers who seek both the adrenaline of raw adventure and the solace of handpicked premium stays.\n\nTOUR OVERVIEW\nTravel Scheme: Fully Customized FIT (Flexible Independent Travel) / Luxury Group Escape Route Protocol: Calicut (CCJ) Airport/Station • Vythiri • Kalpetta • Sulthan Bathery • Calicut Meal Plan: Modified American Plan (MAP - Daily Premium Breakfast & Luxury Buffet Dinner) Vehicle Logistics: Dedicated Premium AC Chauffeur-Driven SUV at disposal for all transits and sightseeing TRAGUIN Curated Experience Note: This itinerary features specialized local adventure guides, skip-the-line passes to high-demand trekking zones, private off-road 4x4 jeep safaris, and night campfire networking experiences handpicked by our travel experts.\n\nWHY CHOOSE A LUXURY WAYANAD HOLIDAY?\nThe Ultimate Adventure & Honeymoon Destination Wayanad stands out as the crown jewel of Kerala eco-tourism, famous for its deep mist-clad valleys, spice-scented air, and unparalleled trekking trails. It is highly searched as the perfect mix for an action- packed family vacation or a highly romantic honeymoon sanctuary. Top Tourist Places & Most Searched Experiences Our itinerary covers the highest-ranked Google tourism hotspots including the famous heart-shaped lake on Chembra Peak, the ancient rock-carvings of Edakkal Caves, the thrilling Banasura Sagar Dam (India's largest earth dam), and the untamed trails of Kuruvadweep. Popular Instagram Locations & Cultural Highlights Capture breathtaking landscapes at the 900 Kandi skywalk, snap iconic panoramic photos from Lakkidi View Point, immerse yourself in tribal culture, taste the authentic Malabar culinary spreads, and shop for premium handpicked organic spices, honey, and tea souvenirs.",
        seo_title='KL-010 | TRAGUIN Wayanad Adventure Escape | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Kerala package (KL-010 / TG-WYN-ADV-2026): Jharkhand with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: CALICUT TO WAYANAD', 1),
            _ih('Day 02: CHEMBRA PEAK TREKKING & BANASURA DAM', 2),
            _ih('Day 03: EDAKKAL CAVES & DEEP FOREST JEEP SAFARI', 3),
            _ih('Day 04: 900 KANDI OFF-ROAD & KURUVA ISLAND', 4),
            _ih('Day 05: WAYANAD TO CALICUT DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private plantation walk with a senior horticulturist followed by', 6),
            _ih('Curated by TRAGUIN Experts: Strict safety audited equipment validation for all trekking, bamboo', 7),
            _ih('Personalized Assistance: Dynamic WhatsApp group integration combining driver, local operations', 8)
        ],
        days=[
            _day(
                1,
                'CALICUT TO WAYANAD',
                (
                    'GATEWAY TO THE MISTY HILLS & CLOUD-KISSED VALLEYS TRAGUIN • Premium Luxury Travel Proposals Your luxury adventure begins as you arrive at Calicut Airport or Railway Station, where a premium, chauffeured vehicle arranged by TRAGUIN welcomes you. As you leave the coast behind, the road winds upward through the legendary Lakkidi Ghat Pass, featuring 9 hairpin curves offering breathtaking landscapes of the valley below. Pause at the Lakkidi View Point for a refreshing mountain breeze and your first Instagram-perfect photography session. Arrive at your luxury eco-resort in Vythiri, nestled amidst dense rainforests. Check-in and experience our signature welcome amenities. Spend your evening exploring the lush properties or taking a guided nature walk around the stream. Conclude the night with a sumptuous buffet dinner under the starlit sky. SIGHTSEEING INCLUDED Lakkidi Ghat Pass, Lakkidi View Point, Ficus Tree (Chain Tree) Legend Site. EVENING EXPERIENCE Private indoor candle-lit ambient tea tasting session.'
                ),
                [
                    'OPTIONAL ACTIVITIES: Premium Ayurvedic Spa rejuvenation therapy at the resort.',
                    'OVERNIGHT STAY: Handpicked Luxury Eco-Resort, Vythiri / Kalpetta.',
                    'MEALS INCLUDED: Luxury Buffet Dinner.',
                ],
            ),
            _day(
                2,
                'CHEMBRA PEAK TREKKING & BANASURA DAM',
                (
                    'CONQUERING THE HIGHEST PEAK & HEART-SHAPED LAKE SIGHTSEEING Rise early for an exhilarating trek up the majestic Chembra Peak, the highest summit in the region and a cornerstone of our Wayanad Adventure. Accompanied by a certified local tracker, you will traverse sprawling tea estates before climbing into the dense shola forests. Reaching the natural, perennial heart-shaped lake (Hridayasaras) is an emotional storytelling highlight that makes this the ultimate Wayanad Honeymoon Package experience. After a hearty lunch, proceed to Banasura Sagar Dam, India’s largest earth dam. Here, speed boating across the vast reservoir surrounded by islands offers an immersive experience filled with scenic beauty. SIGHTSEEING INCLUDED Chembra Peak Trekking, Heart-Shaped Lake, Banasura Sagar Dam, Karlad Lake. EVENING EXPERIENCE Zipline over water bodies, catching the golden sunset views. Handpicked Luxury Eco-Resort, Vythiri / Kalpetta.'
                ),
                [
                    'OPTIONAL ACTIVITIES: High-speed zip-lining and rock climbing at Karlad Lake adventure hub.',
                    'OVERNIGHT STAY: TRAGUIN • Premium Luxury Travel Proposals',
                    'MEALS INCLUDED: Premium Breakfast & Luxury Buffet Dinner.',
                ],
            ),
            _day(
                3,
                'EDAKKAL CAVES & DEEP FOREST JEEP SAFARI',
                (
                    'PREHISTORIC CHRONICLES & UNTAMED WILDERNESS EXPLORATION Unveil the pages of history today as we head towards the magnificent Edakkal Caves located on Ambukuthi Mala. A short, energetic trek leads you to these incredible natural rock clefts housing Neolithic petroglyphs dating back over 8,000 years. Feel the ancient spiritual energy before descending to explore the historical exhibits of Sulthan Bathery. In the afternoon, shift gears into high-adrenaline mode with an exclusive 4x4 open jeep safari into the fringes of Muthanga Wildlife Sanctuary or the deep woods of Wayanad. Keep your lenses ready to capture wild elephants, spotted deer, and rare exotic birds in their natural habitats. SIGHTSEEING INCLUDED Edakkal Caves, Sulthan Bathery Jain Temple, Muthanga Wildlife Sanctuary Zone. EVENING EXPERIENCE Traditional live multi-course dinner accompanied by a light campfire network setting.'
                ),
                [
                    'OPTIONAL ACTIVITIES: Tribal archery interaction and local bamboo crafts workshop.',
                    'OVERNIGHT STAY: Premium Boutique Resort, Sulthan Bathery.',
                    'MEALS INCLUDED: Premium Breakfast & Luxury Buffet Dinner.',
                ],
            ),
            _day(
                4,
                '900 KANDI OFF-ROAD & KURUVA ISLAND',
                (
                    'DEEP JUNGLE CANOPY WALKWAY & BAMBOO RAFTING ADVENTURE Prepare for the highlight of your TRAGUIN Wayanad Packages—the hidden valley of 900 Kandi. Board a specialized rugged off-road vehicle to conquer boulders and muddy streams to reach a breathtaking glass bridge suspended high above the jungle canopy. Walk over the glass for a thrilling view of the dense rainforest beneath your feet. Afterward, head to Kuruvadweep (Kuruva Island), a protected delta on the Kabini River. Glide down the calm, shaded waters on a traditional hand-woven bamboo raft managed by local tribal rowers, making this an unforgettable memory of serene eco- tourism. TRAGUIN • Premium Luxury Travel Proposals SIGHTSEEING INCLUDED 900 Kandi Eco-Park, Glass Bridge Walkway, Kuruvadweep Bamboo Rafting, Soochipara Waterfalls. EVENING EXPERIENCE Bespoke interactive session with a professional naturalist outlining Western Ghats biodiversity.'
                ),
                [
                    'OPTIONAL ACTIVITIES: River trekking and wild stream bathing under expert safety supervision.',
                    'OVERNIGHT STAY: Premium Boutique Resort, Sulthan Bathery.',
                    'MEALS INCLUDED: Premium Breakfast & Luxury Buffet Dinner.',
                ],
            ),
            _day(
                5,
                'WAYANAD TO CALICUT DEPARTURE',
                (
                    'SOUVENIR HUNTING & FAREWELL TO THE LAND OF SPICES Enjoy your final morning amidst the rustling leaves and chirping birds of Wayanad. Relish an elite breakfast spread before completing check-out formalities. As your premium vehicle cruises back down towards Calicut, we stop at famous local spice plantations where you can pick up exotic souvenirs like organic cardamom, premium vanilla pods, homemade chocolates, and signature Malabar tea leaves. Depending on your flight or train schedule, you will be transferred to Calicut International Airport or Station. Bid farewell to your unforgettable Luxury Wayanad Holiday, knowing that TRAGUIN has etched a permanent, beautiful memory in your travel chronicles. SIGHTSEEING INCLUDED Pookode Lake (En-route boating), Local Spice and Tea Plantations. EVENING EXPERIENCE Transit to departure terminal. TRAGUIN • Premium Luxury Travel Proposals'
                ),
                [
                    'OPTIONAL ACTIVITIES: Last-minute Malabar halwa and banana chips shopping in Calicut town.',
                    'OVERNIGHT STAY: Not Applicable.',
                    'MEALS INCLUDED: Premium Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Vythiri Village Resort / Wayanad Silver Woods',
                'Wayanad',
                '4N Wayanad',
                'Deluxe',
                'Deluxe Hill View Room',
                'MAP (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Vythiri Village Resort / Wayanad Silver Woods | MAP (Breakfast & Dinner)',
            ),
            _hotel(
                'The Woods Resorts / After the Rains',
                'Wayanad',
                '4N Wayanad',
                'Premium',
                'Premium Cottage Block',
                'MAP (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Woods Resorts / After the Rains | MAP (Breakfast & Dinner)',
            ),
            _hotel(
                'Mountain Shadows Resort / Pepper Trail Luxury',
                'Wayanad',
                '4N Wayanad',
                'Luxury',
                'Luxury Lake View Villa',
                'MAP (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Mountain Shadows Resort / Pepper Trail Luxury | MAP (Breakfast & Dinner)',
            ),
            _hotel(
                'Evolve Back Kabini / Vythiri Resort Treehouse',
                'Wayanad',
                '4N Wayanad',
                'Ultra Luxury',
                'Private Pool Villa / Luxury Treehouse',
                'MAP (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Evolve Back Kabini / Vythiri Resort Treehouse | MAP (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Daily sumptuous buffet breakfast and dinner spreads at resort restaurants.', 1),
            _inc_included('Complete point-to-point ground logistics using a private air-conditioned SUV.', 2),
            _inc_included('Dedicated corporate-trained chauffeur cum destination holiday companion.', 3),
            _inc_included('Complimentary 4x4 Jeep Safari off-road transit passes for 900 Kandi.', 4),
            _inc_included('Bamboo Rafting entry vouchers for Kuruva Island ecosystem.', 5),
            _inc_included('Welcome traditional non-alcoholic drinks and high-speed Wi-Fi access at all resorts.', 6),
            _inc_included('All current state Tolls, Interstate border permits, Chauffeur allowances, and fuel surcharges.', 7),
            _inc_included('24/7 Premium Remote Concierge Support via TRAGUIN Guest Relations Board.', 8),
            _inc_included('Domestic or International airfares / Mainline rail ticket expenses.', 9),
            _inc_excluded('Premium Accommodation for 04 Nights at handpicked luxury properties.', 10),
            _inc_excluded('Personal nature bills (Laundry, mini-bar usage, telephone calls, room service).', 11),
            _inc_excluded('Camera entry fees at national parks, monuments, and historical sanctuaries.', 12),
            _inc_excluded('Optional heavy-adventure sports charges (Zip-lining, rock-climbing, speed-boating).', 13),
            _inc_excluded('Mandatory peak holiday season supplements or Gala Dinner additions (Christmas/New Year).', 14),
        ],
    )
    return package, itinerary

KERALA_KL_001_010_BUILDERS = [
    build_kl_001,
    build_kl_002,
    build_kl_003,
    build_kl_004,
    build_kl_005,
    build_kl_006,
    build_kl_007,
    build_kl_008,
    build_kl_009,
    build_kl_010,
]
