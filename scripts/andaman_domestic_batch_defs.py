"""Builder functions for AN-001 through AN-010 Andaman domestic packages."""

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

ANDAMAN_SLUG = "andaman-and-nicobar"


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


def build_an_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AN-001'
    tour_code = 'TRAGUIN-AN-ROM-2026'
    title = 'Premium Andaman Honeymoon'
    duration = '05 Nights / 06 Days'
    slug = 'an-001-premium-andaman-honeymoon'
    itin_slug = 'an-001-premium-andaman-honeymoon-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code AN-001 | TRAGUIN tour code TRAGUIN-AN-ROM-2026', 1),
    _ph('State / Country: Andaman & Nicobar Islands, India | Category: Honeymoon / Luxury Tour', 2),
    _ph('Destinations: Port Blair (2N) • Havelock Island (2N) • Neil Island (1N)', 3),
    _ph('Ideal for: Couples, Honeymooners, Luxury Seekers, Families', 4),
    _ph('Best season: October to May (Pleasant Tropical Breeze)', 5),
    _ph('Starting price: On Request (Premium Handpicked Customization)', 6),
    _ph('Vehicle & Meals: Private Luxury AC Fleet • CPAI (Breakfast Included)', 7),
    _ph('Route: Port Blair (2N) → Havelock Island (2N) → Neil Island (1N) → Port Blair → Departure', 8),
    _ph('TRAGUIN Signature Experience: Fast-track entrance privileges and priority cruise check-in procedures managed by our local handlers.', 9),
    _ph('Curated by TRAGUIN Experts: Custom itineraries developed by destination consultants who perform regular resort quality inspections.', 10),
    _ph('Personalized Assistance: Dedicated local host coordinators located at Port Blair, Havelock Island, and Neil Island checkpoints.', 11),
    _ph('Premium Handpicked Hotels: Elite resort partnerships offering exclusive amenities, pristine cleanliness, and welcoming customer care.', 12),
    _ph('Luxury Transportation: Expertly maintained, air-conditioned private executive fleets with safe, courteous local drivers.', 13),
    _ph('Shopping & Local Experiences: Sagarika Government Handicraft Emporium in Port Blair for authentic mother-of-pearl ornaments, hand-woven coconut shell lamps, and rich padauk wood items. Fine dining at Something Different beachside cafe or Full Moon Cafe on Havelock for wood-fired pizzas and fresh tropical fruit blends.', 14),
    _ph('Important Notes: Cruise Operations: High-speed cruise sailings are subject to weather conditions and technical clearance. Check-in/Check-out: Most island resorts follow an early check-out policy (08:00 AM – 09:00 AM) due to incoming cruise schedules. Network Connectivity: Mobile networks can be unstable on Havelock and Neil Island. BSNL and Airtel work best. Advance Bookings: Water sports and specialized candlelit dining slots are highly demanded—reserve with your TRAGUIN consultant during booking confirmation.', 15),
        ],
        moods=['Honeymoon', 'Luxury', 'Romance', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Handpicked Customization)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Premium Andaman Honeymoon • Port Blair • Havelock • Neil • 05 Nights / 06 Days',
        overview="Welcome to an enchanting tropical wonderland proudly curated for you by TRAGUIN. This exquisite Andaman Honeymoon Package is custom-engineered for sophisticated couples and families who appreciate a seamless fusion of intimate privacy, marine adventures, and flawless high-end hospitality. From the historic landmarks of Port Blair to the world-renowned white beaches of Havelock Island and the tranquil, untamed charisma of Neil Island, every single milestone of your journey is formatted to generate unforgettable memories.\n\nTOUR OVERVIEW\nAs your professional luxury travel planners, TRAGUIN offers an elite, private guest-facing experience. Journey comfortably in high-end private air-conditioned vehicles, skip transit lines via premium cruise connections, and rest in our highly vetted, handpicked hotels. This signature Premium Andaman Experience guarantees breathtaking landscapes, personalized dining additions, and exclusive experiences that redefine luxury island escapes.\n\nTHE DEFINITIVE LUXURY ANDAMAN HOLIDAY DESTINATION GUIDE\nThe Andaman & Nicobar Islands represent India's crown jewel for exotic beach getaways, highly ranked as the ideal sanctuary for a passionate Andaman Honeymoon Package or an enriching Andaman Family Tour. Showcasing many of the officially celebrated Top Tourist Places in Andaman, this oceanic paradise enchants visitors with its crystalline turquoise coastlines, complex coral ecosystems, and lush tropical green canopies. Whether strolling down the white shoreline of Radhanagar Beach—widely rated among Asia's finest beaches—or observing sunset colors at Laxmanpur Beach, the archipelago provides peerless, popular Instagram locations for capturing beautiful travel portraits.",
        seo_title='AN-001 | Premium Andaman Honeymoon | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Andaman honeymoon package (AN-001 / TRAGUIN-AN-ROM-2026): Port Blair, Havelock Radhanagar Beach, Neil Island, Elephant Beach snorkeling, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Cellular Jail National Memorial, Light & Sound Show, and Chidiyatapu sunset', 1),
    _ih('Premium catamaran cruise to Havelock and Radhanagar Beach golden hour sunset', 2),
    _ih('Elephant Beach coral safari with complimentary snorkeling session', 3),
    _ih('Neil Island Natural Coral Bridge, Bharatpur Beach, and Laxmanpur Beach sunset', 4),
    _ih('TRAGUIN Signature Experience: Fast-track entrance privileges and priority cruise check-in procedures', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN PORT BLAIR – COLONIAL HERITAGE & HISTORIC LIGHT & SOUND SHOW', ("Step into the warm, tropical embrace of the Bay of Bengal. Upon arrival at the Veer Savarkar International Airport in Port Blair, you will receive a personalized VIP reception by an assigned TRAGUIN on-ground executive. Your professional chauffeur will escort you in a private, pristine air-conditioned executive vehicle directly to your luxury ocean-view resort. Enjoy an effortless check-in, unpack, and unwind before commencing your detailed Andaman Sightseeing tour. In the afternoon, explore India's historic freedom struggle at the monumental Cellular Jail, a National Memorial reflecting poignant colonial history. As dusk gathers, experience the legendary Light and Sound Show at Cellular Jail."), [
        'Sightseeing Included: Cellular Jail National Memorial entrance, historic Light & Sound Show production.',
        'Evening Experience: Colonial historical audio-visual narrative under the starlit sky.',
        'Photography Points: The vintage architecture of Cellular Jail, panoramic views from the central watchtower.',
        'Food Suggestions: Freshly caught crabs or high-end contemporary continental cuisine at the resort bistro.',
        'Overnight Stay: Port Blair (Premium Ocean-View Resort)',
        'Meals Included: Breakfast & Welcome Drink',
    ]),
    _day(2, 'HIGH-SPEED CRUISE TO HAVELOCK ISLAND – SUNSET AT RADHANAGAR BEACH', ("Awake to a stunning marine sunrise and enjoy a gourmet buffet breakfast. Today, your journey leads you deeper into the emerald waters of the archipelago. A private transfer conveys you to the Phoenix Bay Jetty to board a luxury high-speed catamaran (Nautika / Makruzz) to Havelock Island (Swaraj Dweep). Arriving at Havelock Island, you will be swiftly chauffeured to your premium beachfront resort. In the late afternoon, your driver will transport you to the breathtaking Radhanagar Beach (Beach No. 7), consistently ranked as one of the world's most immaculate coastlines."), [
        'Sightseeing Included: Premium catamaran cruise crossing, Radhanagar Beach nature walk.',
        "Optional Activities: Bespoke couple's beachside professional photography session (arranged by TRAGUIN).",
        'Evening Experience: Beachside barefoot walk during the golden hour sunset.',
        'Photography Points: Radhanagar golden hour horizon, majestic fallen driftwood structures.',
        'Overnight Stay: Havelock Island (Luxury Beachfront Resort)',
        'Meals Included: Breakfast',
    ]),
    _day(3, 'ELEPHANT BEACH CORAL SAFARI – MARINE EXCURSIONS & WATER ADVENTURES', ('Prepare for an adventurous day exploring exotic marine habitats. Following a delicious breakfast, a private speedboat transfers you from the Havelock jetty to Elephant Beach. Noted for its brilliant shallow-water coral beds, Elephant Beach stands as a key highlight for water activities and aquatic exploration. Immerse yourself in underwater beauty with a complimentary snorkeling session guided by a certified marine specialist.'), [
        'Sightseeing Included: Private speedboat ride, Elephant Beach marine access, guided snorkeling session.',
        'Optional Activities: PADI Scuba Diving, Sea Walking tours, high-speed Jet Skiing.',
        'Evening Experience: Relaxing at leisure or indulging in a private beachside candlelit dinner.',
        'Food Suggestions: Authentic wood-fired pizzas and fresh tropical fruit beverages at local beach cafes.',
        'Overnight Stay: Havelock Island (Luxury Beachfront Resort)',
        'Meals Included: Breakfast',
    ]),
    _day(4, 'CRUISE TO NEIL ISLAND – NATURAL STONE BRIDGE & LAXMANPUR BEACH SUNSET', ('Depart Havelock as you board an afternoon luxury catamaran cruise toward Neil Island (Shaheed Dweep). Neil Island is globally celebrated for its rustic charm, peaceful farming hamlets, and untouched tropical wilderness. Your afternoon island excursion starts at Bharatpur Beach, a reef-lined lagoon ideal for glass-bottom boat viewings. Next, visit the spectacular Natural Coral Bridge, a stunning geological rock arch carved by marine tides over centuries.'), [
        'Sightseeing Included: Catamaran cruise to Neil, Bharatpur Beach walk, Natural Bridge archway, Laxmanpur Beach.',
        'Optional Activities: Glass-bottom boat coral viewing reef tours.',
        'Evening Experience: Sunset watching along the expansive sandy flats of Laxmanpur.',
        'Photography Points: The unique rock archway at the Natural Bridge, panoramic open ocean sunset.',
        'Overnight Stay: Neil Island (Premium Luxury Boutique Resort)',
        'Meals Included: Breakfast',
    ]),
    _day(5, 'RETURN TO PORT BLAIR – LOCAL SOUVENIR SHOPPING & CHIDIYATAPU SUNSET', ("Enjoy a relaxed breakfast amidst the peaceful tropical gardens of Neil Island. Capture final photos of this tranquil destination before boarding your luxury afternoon cruise back to Port Blair. In the late afternoon, take a scenic drive through forest reserves to Chidiyatapu, often called Bird Island. Observe a spectacular final sunset over the open ocean. Later in the evening, enjoy a curated shopping trip to Port Blair's handicraft emporiums."), [
        'Sightseeing Included: Luxury catamaran transit to Port Blair, Chidiyatapu Sunset Point drive, artisan markets.',
        'Shopping Highlights: Sagarika Government Handicraft Emporium for genuine sea-shell crafts and pearls.',
        'Evening Experience: Fine dining at the harbor-front or exploring the lively town markets.',
        'Photography Points: Dramatic mangrove silhouettes at Chidiyatapu, local colorful handicraft stalls.',
        'Overnight Stay: Port Blair (Premium Ocean-View Resort)',
        'Meals Included: Breakfast',
    ]),
    _day(6, 'DEPARTURE WITH UNFORGETTABLE MEMORIES', ('As your exceptional Andaman Honeymoon Package draws to a close, enjoy a final breakfast at your resort. Take in the warm tropical breeze and gaze across the beautiful turquoise sea. Your private driver will arrive to transfer you in comfort to the Veer Savarkar International Airport for your flight home. You depart with a refreshed spirit and a collection of unforgettable memories, all seamlessly orchestrated by the destination experts at TRAGUIN.'), [
        'Transfer Included: Private luxury airport vehicle drop-off service.',
        'Consultant Note: We recommend pre-booking a window seat for beautiful aerial views of the archipelago during departure!',
        'Meals Included: Breakfast Only',
    ]),
        ],
        hotels=[
            _hotel('Symphony Palms / Sea Shell', 'Port Blair', '02 Nights', 'Deluxe', 'Deluxe Room', 'CPAI (Breakfast)', 4, 1, description='OPTION 01 – DELUXE: Symphony Palms / Sea Shell (Port Blair, 02 Nights)'),
    _hotel('Symphony Palms Beach Resort', 'Havelock Island', '02 Nights', 'Deluxe', 'Deluxe Room', 'CPAI (Breakfast)', 4, 2, description='OPTION 01 – DELUXE: Symphony Palms Beach Resort (Havelock Island, 02 Nights)'),
    _hotel('Symphony Summer Sands', 'Neil Island', '01 Night', 'Deluxe', 'Deluxe Room', 'CPAI (Breakfast)', 4, 3, description='OPTION 01 – DELUXE: Symphony Summer Sands (Neil Island, 01 Night)'),
    _hotel('Welcomhotel by ITC Bay Island', 'Port Blair', '02 Nights', 'Premium', 'Premium Room', 'CPAI (Breakfast)', 4, 4, description='OPTION 02 – PREMIUM: Welcomhotel by ITC Bay Island (Port Blair, 02 Nights)'),
    _hotel('Sea Shell Havelock / Sandyy Wavess', 'Havelock Island', '02 Nights', 'Premium', 'Premium Room', 'CPAI (Breakfast)', 4, 5, description='OPTION 02 – PREMIUM: Sea Shell Havelock / Sandyy Wavess (Havelock Island, 02 Nights)'),
    _hotel('Sea Shell Neil / Silver Sand', 'Neil Island', '01 Night', 'Premium', 'Premium Room', 'CPAI (Breakfast)', 4, 6, description='OPTION 02 – PREMIUM: Sea Shell Neil / Silver Sand (Neil Island, 01 Night)'),
    _hotel('Coral Reef Resort (Club Room)', 'Port Blair', '02 Nights', 'Luxury', 'Club Room', 'CPAI (Breakfast)', 5, 7, description='OPTION 03 – LUXURY: Coral Reef Resort (Club Room) (Port Blair, 02 Nights)'),
    _hotel('Barefoot at Havelock / Munjoh Ocean', 'Havelock Island', '02 Nights', 'Luxury', 'Luxury Room', 'CPAI (Breakfast)', 5, 8, description='OPTION 03 – LUXURY: Barefoot at Havelock / Munjoh Ocean (Havelock Island, 02 Nights)'),
    _hotel('TSG Aura / Sea Shell Luxury', 'Neil Island', '01 Night', 'Luxury', 'Luxury Room', 'CPAI (Breakfast)', 5, 9, description='OPTION 03 – LUXURY: TSG Aura / Sea Shell Luxury (Neil Island, 01 Night)'),
    _hotel('Taj Exotica Resort (Suite Room)', 'Port Blair', '02 Nights', 'Ultra Luxury', 'Suite Room', 'CPAI (Breakfast)', 5, 10, description='OPTION 04 – ULTRA LUXURY: Taj Exotica Resort (Suite Room) (Port Blair, 02 Nights)'),
    _hotel('Taj Exotica Resort & Spa (Radhanagar)', 'Havelock Island', '02 Nights', 'Ultra Luxury', 'Luxury Villa', 'CPAI (Breakfast)', 5, 11, description='OPTION 04 – ULTRA LUXURY: Taj Exotica Resort & Spa (Radhanagar) (Havelock Island, 02 Nights)'),
    _hotel('Tilar Siro Neil Island (CGH Earth)', 'Neil Island', '01 Night', 'Ultra Luxury', 'Luxury Suite', 'CPAI (Breakfast)', 5, 12, description='OPTION 04 – ULTRA LUXURY: Tilar Siro Neil Island (CGH Earth) (Neil Island, 01 Night)'),
        ],
        inclusions=[
            _inc_included('Premium Stays: 05 Nights inside highly rated premium resorts.', 1),
    _inc_included('Gourmet Dining: 05 Complimentary multi-cuisine buffet breakfasts.', 2),
    _inc_included('Private Mobility: All airport, jetty, and sightseeing transits in a private AC vehicle.', 3),
    _inc_included('High-Speed Cruise: Premium class catamaran slots (Nautika/Makruzz).', 4),
    _inc_included('Curated Experience: Entry tickets, permits, and ferry tokens to all sites.', 5),
    _inc_included('TRAGUIN Snorkeling Bonus: 1 Complimentary snorkeling session at Elephant Beach.', 6),
    _inc_included('Welcome Comforts: VIP non-alcoholic refreshing welcome drinks on check-in.', 7),
    _inc_included('On-Ground Support: 24/7 round-the-clock dedicated TRAGUIN local host assistance.', 8),
    _inc_included('All Taxes Included: Road tolls, driver allowances, parking fees, and GST.', 9),
    _inc_excluded('Flight Costs: Domestic/International airfare bookings to Port Blair.', 10),
    _inc_excluded('Extra Activities: Deep Scuba Diving, Sea Walking, and Parasailing.', 11),
    _inc_excluded('Personal Tabs: Laundry, mini-bar use, room service, and driver tips.', 12),
    _inc_excluded('Unspecified Meals: Daily lunch and dinner orders outside breakfast options.', 13),
    _inc_excluded('Camera Charges: Commercial video camera permits at historical monuments.', 14),
    _inc_excluded('Travel Protection: Personal travel insurance or medical coverage plans.', 15),
    _inc_excluded("Gala Suppers: Mandatory Christmas or New Year's Eve resort gala surcharges.", 16),
        ],
    )
    return package, itinerary

def build_an_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AN-002'
    tour_code = 'TRG-AND-2026-V2'
    title = 'Premium Andaman Tour Package'
    duration = '06 Nights / 07 Days'
    slug = 'an-002-premium-andaman-tour-package'
    itin_slug = 'an-002-premium-andaman-tour-package-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code AN-002 | TRAGUIN tour code TRG-AND-2026-V2', 1),
    _ph('State / Country: Andaman & Nicobar Islands, India | Category: Family Holiday / Luxury', 2),
    _ph('Destinations: Port Blair (2N) • Havelock Island (3N) • Neil Island (1N)', 3),
    _ph('Ideal for: Families, Couples, Luxury Seekers', 4),
    _ph('Best season: October to May', 5),
    _ph('Starting price: On Request (Premium)', 6),
    _ph('Vehicle & Meals: Private Premium Executive AC Vehicle (Xylo/Ertiga/Innova) | CP / MAPAI (Premium Buffet Breakfast & Dinner Included)', 7),
    _ph('Route: Port Blair (2N) → Havelock Island (3N) → Neil Island (1N) → Port Blair → Departure', 8),
    _ph('TRAGUIN Signature Experience: Private beachside setup for sunset viewing away from standard tourist crowds.', 9),
    _ph('Curated by TRAGUIN Experts: Custom itineraries dynamically adapted to the comfort of senior citizens and children.', 10),
    _ph('Premium Handpicked Hotels: Properties selected based on strict criteria for direct beach access, service excellence, and safety.', 11),
    _ph("Exclusive Recommendations: Access to a personalized digital map detailing the island's finest hidden culinary hotspots and secret view points.", 12),
    _ph('Shopping & Local Experiences: Sagarika Government Emporium (Port Blair): The ultimate destination for genuine mother-of-pearl jewelry, exotic sea-shell artifacts, and premium hand-carved padauk woodwork souvenirs. Havelock Island Cafes: Freshly caught wood-fired red snapper paired with freshly cracked organic local king coconut water.', 13),
    _ph('Important Notes: Ferry Operations: Inter-island ferry sailings are subject to weather conditions and technical clearances. Mobile Connectivity: Mobile networks can be highly erratic across Havelock and Neil islands—BSNL and Airtel offer the most stable connectivity. Advance Booking: Due to extreme demand for premium private cruise seats and luxury beach villas, we highly recommend securing bookings 45–60 days prior to departure.', 14),
        ],
        moods=['Family', 'Luxury', 'Beach', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Premium Andaman Tour Package • Port Blair • Havelock • Neil • 06 Nights / 07 Days',
        overview="Welcome to an unforgettable journey curated by TRAGUIN. Escape to an emerald paradise floating in the turquoise depths of the Bay of Bengal. This customized Andaman Family Tour opens doors to breathtaking landscapes, dramatic sunsets, and pristine white-sand shores. Indulge in an exquisite blend of rich historical heritage, thrilling underwater adventures, and deeply immersive experiences designed to forge everlasting bonds with your loved ones.\n\nTOUR OVERVIEW\nTRAVEL TYPE: FIT / Private Family Group. FERRY TRANSFERS: Premium Private Cruise (Nautika / Makruzz / Green Ocean). TRAGUIN Curated Experience Note: Enjoy seamless, stress-free transfers with private escorts at every jetty, VIP skip-the-line cruise boarding, handpicked five-star beach resorts, and completely personalized sightseeing pacing that perfectly suits multi-generational families.\n\nWHY CHOOSE THE PREMIUM ANDAMAN EXPERIENCE?\nThe Andaman archipelago stands as India's crown jewel for exotic luxury vacations. From walking along Radhanagar Beach—widely recognized as one of the most stunning popular Instagram locations in Asia—to exploring the rich colonial legacy of Ross Island, the region offers something timeless for every discerning traveler.",
        seo_title='AN-002 | Premium Andaman Tour Package | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Andaman family package (AN-002 / TRG-AND-2026-V2): Port Blair, Havelock Radhanagar Beach, Elephant Beach, Neil Island, Ross Island, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Cellular Jail National Memorial, Light & Sound Show, and Marina Park Promenade', 1),
    _ih('Premium cruise to Havelock and Radhanagar Beach golden hour sunset', 2),
    _ih('Elephant Beach speedboat excursion with glass-bottom boat and snorkeling', 3),
    _ih('Kalapathar Beach sunrise and Neil Island Natural Coral Bridge at Laxmanpur Beach', 4),
    _ih('Ross Island heritage ruins and British-era colonial landmarks', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN PORT BLAIR & HISTORIC CELLULAR JAIL LIGHT AND SOUND SHOW', ("Touchdown at Veer Savarkar International Airport in Port Blair, where your dedicated TRAGUIN travel concierge awaits you with a warm traditional welcome. Transfer seamlessly in your private executive AC vehicle to your luxury hotel. After checking in and relaxing, embark on an insightful journey into India's freedom struggle at the iconic Cellular Jail. As dusk falls, experience the deeply emotional and spectacular Light and Sound Show, bringing the epic history of Kalapani alive through brilliant narration."), [
        'Sightseeing Included: Cellular Jail National Memorial, Evening Light & Sound Show, Marina Park Promenade.',
        'Optional Activities: Pre-arranged local culinary tasting tour or a private late-evening heritage walk.',
        'Evening Experience: Unwind with a leisurely stroll at the seafront Marina Park, catching cool ocean breezes.',
        'Overnight Stay: Premium Ocean-view Resort, Port Blair',
        'Meals Included: Dinner Included',
    ]),
    _day(2, 'PRIVATE CRUISE TO HAVELOCK ISLAND & RADHANAGAR SUNSET', ('Savor an early gourmet breakfast before boarding a premium private luxury cruise (Makruzz/Nautika) to Havelock Island, the epicenter of Andaman Sightseeing. Arrive at shores bordered by towering coconut palms and vibrant turquoise waters. Check into your ultra-luxury beachfront villa. In the afternoon, journey to the world-renowned Radhanagar Beach (Beach No. 7). Witness a truly breathtaking, painterly sunset over the horizon.'), [
        'Sightseeing Included: Luxury Cruise Voyage, Radhanagar Beach Exploration & Golden Hour Sunset.',
        'Optional Activities: Professional private beachside family photoshoot during golden hour.',
        'Evening Experience: A candle-lit, premium seafood dinner experience right on the powdery sands of Havelock.',
        'Overnight Stay: Exquisite Beachside Luxury Resort, Havelock Island',
        'Meals Included: Breakfast & Dinner',
    ]),
    _day(3, 'EXCURSION TO ELEPHANT BEACH & THRILLING MARINE ADVENTURES', ('Prepare for an action-packed morning as a private speed boat sweeps your family away to Elephant Beach, globally celebrated for its shallow coral reefs and spectacular biodiversity. View the mesmerizing underwater world through complimentary glass-bottom boat rides, or plunge deeper with high-quality snorkeling.'), [
        'Sightseeing Included: Elephant Beach Speedboat Excursion, Coral Reef Exploration, Marine Sightseeing.',
        'Optional Activities: Advanced Sea Walking, PADI Discover Scuba Diving, Parasailing over the lagoon.',
        'Evening Experience: Relax at a vibrant local beach cafe, sampling fresh tropical mocktails and local delicacies.',
        'Overnight Stay: Exquisite Beachside Luxury Resort, Havelock Island',
        'Meals Included: Breakfast & Dinner',
    ]),
    _day(4, 'TRANQUIL KALAPATHAR BEACH & ISLAND LEISURE DAY', ('Begin your day witnessing a magical sunrise at Kalapathar Beach, where deep turquoise waters contrast beautifully against striking black rocks lining the shore. The remainder of your day is dedicated to pure unadulterated luxury and leisure. Unwind within your high-end resort, plunge into the infinity pool, pamper yourself with a traditional Balinese spa therapy, or enjoy a tranquil book under a private beach cabana.'), [
        'Sightseeing Included: Kalapathar Beach Sunrise, Scenic Island Coastal Road Drive.',
        'Optional Activities: Premium couples/family spa treatment, private luxury yacht charter for a few hours.',
        'Evening Experience: Curated beach bonfire with live acoustic music under a stellar, unpolluted night sky.',
        'Overnight Stay: Exquisite Beachside Luxury Resort, Havelock Island',
        'Meals Included: Breakfast & Dinner',
    ]),
    _day(5, 'CRUISE TO NEIL ISLAND & LAXMANPUR BEACH NATURAL BRIDGE', ('Bid adieu to Havelock as your premium cruise sails towards the serene, pastoral oasis of Neil Island (Shaheed Dweep). Visit the famous Howrah Bridge—a natural geological rock formation standing majestically against the roaring waves. Later, head to Laxmanpur Beach to witness a pristine sunset while listening to the soothing symphony of crashing waves.'), [
        'Sightseeing Included: Natural Coral Bridge Formation, Laxmanpur Beach Sunset point, Bharatpur Beach.',
        "Optional Activities: Jet ski rides or glass-bottom eco-tours over Neil's shallow, protected coral nurseries.",
        'Evening Experience: Stroll through organic island markets, tasting fresh seasonal fruits and local coconut water.',
        'Overnight Stay: Boutique Eco-Luxury Resort, Neil Island',
        'Meals Included: Breakfast & Dinner',
    ]),
    _day(6, 'RETURN TO PORT BLAIR & ROSS ISLAND HERITAGE EXPLORATION', ('Catch a morning cruise back to Port Blair. After checking into your premium resort, set sail on a brief private boat ride to Netaji Subhash Chandra Bose Island (Ross Island). Once the opulent administrative headquarters of the British, it now stands as an enchanting heritage site where magnificent colonial ruins are beautifully embraced by massive, ancient tree roots.'), [
        "Sightseeing Included: Ross Island Heritage Ruins, British Era Church & Officer's Quarters, Port Blair Markets.",
        'Optional Activities: Souvenir shopping at the government-run Sagarika Emporium for premium woodcrafts.',
        'Evening Experience: A grand, farewell fine-dining dinner experience celebrating your final night in paradise.',
        'Overnight Stay: Premium Ocean-view Resort, Port Blair',
        'Meals Included: Breakfast & Dinner',
    ]),
    _day(7, 'DEPARTURE WITH UNFORGETTABLE MEMORIES', ('Indulge in a final lavish buffet breakfast overlooking the ocean. Pack your bags loaded with unforgettable memories of sun-kissed beaches, pristine blue waters, and delightful family moments. Your private chauffeur will pick you up from the resort lobby and provide a comfortable transfer to Veer Savarkar International Airport for your flight back home.'), [
        'Sightseeing Included: Airport Transfer via Premium Private Vehicle.',
        'Meals Included: Gourmet International Buffet Breakfast.',
    ]),
        ],
        hotels=[
            _hotel('Symphony Palms / Similar', 'Port Blair', '02 Nights', 'Deluxe', 'Deluxe Room', 'CP (Breakfast)', 4, 1, description='OPTION 01 – DELUXE: Symphony Palms / Similar (Port Blair, 02 Nights)'),
    _hotel('Symphony Palms Beach Resort', 'Havelock Island', '03 Nights', 'Deluxe', 'Deluxe Room', 'CP (Breakfast)', 4, 2, description='OPTION 02 – DELUXE: Symphony Palms Beach Resort (Havelock Island, 03 Nights)'),
    _hotel('Summer Sands Beach Resort', 'Neil Island', '01 Night', 'Deluxe', 'Deluxe Room', 'CP (Breakfast)', 4, 3, description='OPTION 03 – DELUXE: Summer Sands Beach Resort (Neil Island, 01 Night)'),
    _hotel('SeaShell Port Blair', 'Port Blair', '02 Nights', 'Premium', 'Premium Room', 'MAP (Breakfast + Dinner)', 4, 4, description='OPTION 04 – PREMIUM: SeaShell Port Blair (Port Blair, 02 Nights)'),
    _hotel('SeaShell Havelock', 'Havelock Island', '03 Nights', 'Premium', 'Premium Room', 'MAP (Breakfast + Dinner)', 4, 5, description='OPTION 05 – PREMIUM: SeaShell Havelock (Havelock Island, 03 Nights)'),
    _hotel('SeaShell Neil', 'Neil Island', '01 Night', 'Premium', 'Premium Room', 'MAP (Breakfast + Dinner)', 4, 6, description='OPTION 06 – PREMIUM: SeaShell Neil (Neil Island, 01 Night)'),
    _hotel('Welcomhotel by ITC Bay Island', 'Port Blair', '02 Nights', 'Luxury', 'Luxury Room', 'MAP (Premium Buffet)', 5, 7, description='OPTION 07 – LUXURY: Welcomhotel by ITC Bay Island (Port Blair, 02 Nights)'),
    _hotel('Taj Exotica Resort & Spa (Villa)', 'Havelock Island', '03 Nights', 'Luxury', 'Luxury Villa', 'MAP (Premium Buffet)', 5, 8, description='OPTION 08 – LUXURY: Taj Exotica Resort & Spa (Villa) (Havelock Island, 03 Nights)'),
    _hotel('Symphony Samudra Jungle Resort', 'Neil Island', '01 Night', 'Luxury', 'Luxury Room', 'MAP (Premium Buffet)', 5, 9, description='OPTION 09 – LUXURY: Symphony Samudra Jungle Resort (Neil Island, 01 Night)'),
    _hotel('Taj Exotica (Premium Sea View)', 'Port Blair', '02 Nights', 'Ultra Luxury', 'Premium Sea View Suite', 'Elite Tailored Menu', 5, 10, description='OPTION 10 – ULTRA LUXURY: Taj Exotica (Premium Sea View) (Port Blair, 02 Nights)'),
    _hotel('Taj Exotica Resort & Spa (Luxury)', 'Havelock Island', '03 Nights', 'Ultra Luxury', 'Luxury Villa', 'Elite Tailored Menu', 5, 11, description='OPTION 11 – ULTRA LUXURY: Taj Exotica Resort & Spa (Luxury) (Havelock Island, 03 Nights)'),
    _hotel('SeaShell Neil (Laguna Villa)', 'Neil Island', '01 Night', 'Ultra Luxury', 'Laguna Villa', 'Elite Tailored Menu', 5, 12, description='OPTION 12 – ULTRA LUXURY: SeaShell Neil (Laguna Villa) (Neil Island, 01 Night)'),
        ],
        inclusions=[
            _inc_included('Curated experiences with 06 Nights elite accommodation.', 1),
    _inc_included('Daily breakfast & gourmet dinners at handpicked premium restaurants.', 2),
    _inc_included('Private AC Executive vehicle for all point-to-point transfers & sightseeing.', 3),
    _inc_included('Premium Private Cruise tickets (Nautika/Makruzz) for inter-island transfers.', 4),
    _inc_included('Special TRAGUIN support with 24/7 on-ground guest assistance.', 5),
    _inc_included('Meet & greet services by local hospitality experts at all arrival points.', 6),
    _inc_included('Speedboat charges for Elephant Beach and Ross Island ferry excursions.', 7),
    _inc_included('Complimentary glass-bottom boat ride at Elephant Beach.', 8),
    _inc_included('All applicable state luxury taxes, fuel charges, toll fees, and parking fees.', 9),
    _inc_excluded('Domestic or international airfare to and from Port Blair.', 10),
    _inc_excluded('Optional water adventure sports (Scuba Diving, Sea Walking, Parasailing).', 11),
    _inc_excluded('Personal expenses (laundry, telephone calls, premium alcoholic beverages).', 12),
    _inc_excluded('Monument/Jail/National Park entry tickets unless explicitly specified.', 13),
    _inc_excluded("Mandatory Christmas Eve or New Year's Gala dinner supplements if applicable.", 14),
    _inc_excluded('Comprehensive travel insurance or emergency evacuation coverage.', 15),
    _inc_excluded('Tips for private drivers, local guides, and resort baggage porters.', 16),
        ],
    )
    return package, itinerary

def build_an_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AN-003'
    tour_code = 'TRG-AND-003'
    title = 'Andaman Escape'
    duration = '05 Nights / 06 Days'
    slug = 'an-003-andaman-escape'
    itin_slug = 'an-003-andaman-escape-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code AN-003 | TRAGUIN tour code TRG-AND-003', 1),
    _ph('State / Country: Andaman & Nicobar Islands, India | Category: Premium Family Tour', 2),
    _ph('Destinations: Port Blair (3N) • Havelock Island (2N)', 3),
    _ph('Ideal for: Family Vacations, Luxury Explorers & Beach Lovers', 4),
    _ph('Best season: October to May', 5),
    _ph('Starting price: On Request (Premium Customised)', 6),
    _ph('Vehicle & Meals: Private Luxury AC Vehicle & Premium Cruise / CP + Dinner', 7),
    _ph('Route: Port Blair (3N) → Havelock Island (2N) → Port Blair → Departure', 8),
    _ph('TRAGUIN Signature Experience: Priority embarkation assistance at the ferry terminals to avoid long queues.', 9),
    _ph('Curated by TRAGUIN Experts: Handpicked scheduling ensuring you explore Radhanagar Beach exactly during optimal sunset conditions.', 10),
    _ph('Luxury Transportation: Impeccably clean private vehicles with professional, island-native tourist drivers.', 11),
    _ph("Exclusive Recommendations: Tailored dining recommendations at Havelock's hidden beachfront cafes.", 12),
    _ph("Shopping & Local Experiences: Local Specialities: Take back elegant, genuine mother-of-pearl jewelry, hand-carved coconut shell lamps, and fine wooden tribal artifacts from Port Blair's Sagarika Government Emporium. Beachside Dining: Fresh sea-food preparations at top beach shacks or wood-fired pizzas at boutique cafes hidden under canopy trees in Havelock Island.", 13),
    _ph('Important Notes: Cruise Schedule: Catamaran cruise sailings are subject to weather conditions. TRAGUIN reserves rights to modify timings for guest safety. Activity Bookings: To secure premium time slots for scuba diving or sea-walking, advance booking is highly recommended. Plastic Ban: Andaman is a strict eco-friendly zone. Carrying disposable single-use plastic bags or bottles is heavily restricted.', 14),
        ],
        moods=['Family', 'Luxury', 'Beach', 'Heritage'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Andaman Escape • Tropical Sun, Sand & Serenity • 05 Nights / 06 Days',
        overview="Welcome to an extraordinary tropical getaway hand-curated by TRAGUIN. Immerse your family in the absolute best Andaman Tour Package, carefully designed to offer an exquisite blend of profound historical legacies and serene coastal opulence. From the poignant historical narratives of Port Blair to the pristine, powdery white sands of Havelock Island, every hour is tailored to generate unforgettable memories for your loved ones.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers a sophisticated balance between poignant heritage sites, marine life adventures, and breathtaking landscapes. Traveling across the islands via premium high-speed private cruises (Makruzz/Nautika) and on land within exclusive, air-conditioned private vehicles, your family is guaranteed ultimate privacy and premium comfort.\n\nWHY CHOOSE THE BEST ANDAMAN TOUR PACKAGE?\nAndaman stands out as an exotic paradise hosting some of the most iconic attractions in the world. From the historic walls of Cellular Jail in Port Blair to the world-renowned Radhanagar Beach on Havelock Island—voted among Asia's best beaches—the region offers a beautiful escape.",
        seo_title='AN-003 | Andaman Escape | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Andaman package (AN-003 / TRG-AND-003): Port Blair heritage, Havelock Radhanagar Beach, Elephant Beach snorkeling, Ross Island, Chidiyatapu sunset, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Cellular Jail National Memorial, Carbyn's Cove Beach, and Sound & Light Show", 1),
    _ih('Premium cruise to Havelock and Radhanagar Beach sunset exploration', 2),
    _ih('Elephant Beach speedboat transfer and coral reef snorkeling', 3),
    _ih('Kalapathar Beach and return luxury catamaran cruise to Port Blair', 4),
    _ih('Ross Island ruins and Chidiyatapu Sunset Point & Biological Park', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN PORT BLAIR — HISTORIC ECHOES & ENCHANTING LIGHTS', ('Your premium Andaman experience officially begins as your flight lands at Veer Savarkar International Airport in Port Blair. A dedicated private luxury transport vehicle will warmly greet you and escort your family to your handpicked premium hotel. After a seamless check-in and lunch, proceed to the iconic Cellular Jail, a national memorial holding immense historic significance. Spend your afternoon mapping out the old corridors before settling in for the emotionally moving Sound and Light Show.'), [
        "Sightseeing Included: Cellular Jail National Memorial, Carbyn's Cove Beach, Sound & Light Show.",
        "Evening Experience: Private coastal drive along Carbyn's Cove with fresh coconut water sampling.",
        'Overnight Stay: Port Blair (Premium Ocean-View Property)',
        'Meals Included: Welcome Drink & Luxury Welcome Dinner',
    ]),
    _day(2, 'PORT BLAIR TO HAVELOCK ISLAND — CRUISING UNTO TURQUOISE PARADISE & SUNSET MAJESTY', ('Board a premium high-speed luxury catamaran cruise (Makruzz or Nautika) from Port Blair to Havelock Island, an iconic attraction revered for its unparalleled scenic beauty. Upon arrival at Havelock, enjoy private transfers to your ultra-luxury beachfront resort. In the afternoon, your private vehicle will chauffeur you to Radhanagar Beach (Beach No. 7).'), [
        'Sightseeing Included: Premium Cruise Voyage, Radhanagar Beach Exploration.',
        'Optional Activities: Bespoke beachside high-tea setup or candid family sunset portrait photography.',
        'Overnight Stay: Havelock Island (Luxury Beachfront Resort)',
        'Meals Included: Premium Breakfast & Buffet Dinner',
    ]),
    _day(3, 'HAVELOCK ISLAND — CORAL REEFS & AQUATIC ADVENTURE PLUNGE', ('Embark on a swift, thrilling speed-boat ride to Elephant Beach, widely celebrated as the definitive epicenter for marine life and coral exploration in Andaman. Enjoy complimentary snorkeling, sea walking, or glass-bottom boat rides. Return to your resort by afternoon to unwind amidst the lush tropical flora.'), [
        'Sightseeing Included: Elephant Beach Speedboat Transfer, Coral Reef Snorkeling.',
        'Optional Activities: PADI Certified Discover Scuba Diving session or Sea Walking experience.',
        'Overnight Stay: Havelock Island (Luxury Beachfront Resort)',
        'Meals Included: Breakfast & Exquisite Seafood/Continental Dinner',
    ]),
    _day(4, 'HAVELOCK ISLAND TO PORT BLAIR — KALAPATHAR BEACH & RETURN CRUISE SAFARI', ('Begin your morning with a scenic drive to Kalapathar Beach, a stunning strip of coastline famous for its dramatic black rocks contrasting beautifully against brilliant aqua waters. Following this, head to the jetty to board your premium luxury cruise back to Port Blair. Upon arrival, check back into your hotel and enjoy a relaxed evening exploring local markets.'), [
        'Sightseeing Included: Kalapathar Beach, High-Speed Luxury Catamaran Cruise to Port Blair.',
        "Evening Experience: Relaxed stroll around Port Blair's local handicraft emporiums.",
        'Overnight Stay: Port Blair (Premium Ocean-View Property)',
        'Meals Included: Breakfast & Curated Multi-Cuisine Dinner',
    ]),
    _day(5, 'PORT BLAIR — ROSS ISLAND & CHIDIYATAPU EXCURSION', ('Take a short private ferry ride to Ross Island (Netaji Subhash Chandra Bose Dweep), the erstwhile administrative headquarters of the British regime. Walk amidst historical ruins wrapped in giant banyan tree roots, where friendly deer roam freely. In the afternoon, drive down to Chidiyatapu, fondly referred to as the bird island.'), [
        'Sightseeing Included: Ross Island Ruins, Chidiyatapu Sunset Point & Biological Park.',
        'Optional Activities: Guided heritage trek inside the historic ruins of Ross Island.',
        'Overnight Stay: Port Blair (Premium Ocean-View Property)',
        'Meals Included: Breakfast & Special Farewell Dinner',
    ]),
    _day(6, 'DEPARTURE FROM PORT BLAIR — CHERISHING UNFORGETTABLE EMOTIONS', ('Indulge in a final lavish breakfast overlooking the ocean. Your private luxury transport will safely transfer your family to Veer Savarkar International Airport in Port Blair. Return home carrying a heart full of deep bonds, laughter, and unforgettable memories meticulously designed by TRAGUIN.'), [
        'Transfers Included: Private airport departure drop-off assistance.',
        'Meals Included: Sumptuous Buffet Breakfast',
    ]),
        ],
        hotels=[
            _hotel('Hotel de Roopan / peerless resort', 'Port Blair', '03 Nights', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner (MAPAI)', 4, 1, description='OPTION 01 – DELUXE: Hotel de Roopan / peerless resort (Port Blair, 03 Nights)'),
    _hotel('Symphony Palms Beach Resort', 'Havelock Island', '02 Nights', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner (MAPAI)', 4, 2, description='OPTION 02 – DELUXE: Symphony Palms Beach Resort (Havelock Island, 02 Nights)'),
    _hotel('SeaShell Port Blair / Silver Sand', 'Port Blair', '03 Nights', 'Premium', 'Premium Room', 'Breakfast & Dinner (MAPAI)', 4, 3, description='OPTION 03 – PREMIUM: SeaShell Port Blair / Silver Sand (Port Blair, 03 Nights)'),
    _hotel('Havelock Island Beach Resort', 'Havelock Island', '02 Nights', 'Premium', 'Premium Room', 'Breakfast & Dinner (MAPAI)', 4, 4, description='OPTION 04 – PREMIUM: Havelock Island Beach Resort (Havelock Island, 02 Nights)'),
    _hotel('Welcomhotel by ITC Bay Island', 'Port Blair', '03 Nights', 'Luxury', 'Luxury Room', 'Breakfast & Dinner (Gourmet)', 5, 5, description='OPTION 05 – LUXURY: Welcomhotel by ITC Bay Island (Port Blair, 03 Nights)'),
    _hotel('SeaShell Havelock / Sandyy Wavess', 'Havelock Island', '02 Nights', 'Luxury', 'Luxury Room', 'Breakfast & Dinner (Gourmet)', 5, 6, description='OPTION 06 – LUXURY: SeaShell Havelock / Sandyy Wavess (Havelock Island, 02 Nights)'),
    _hotel('Symphony Samudra (Pool Villa)', 'Port Blair', '03 Nights', 'Ultra Luxury', 'Pool Villa', 'Bespoke Fine Dining Plan', 5, 7, description='OPTION 07 – ULTRA LUXURY: Symphony Samudra (Pool Villa) (Port Blair, 03 Nights)'),
    _hotel('Taj Exotica Resort & Spa, Andamans', 'Havelock Island', '02 Nights', 'Ultra Luxury', 'Luxury Villa', 'Bespoke Fine Dining Plan', 5, 8, description='OPTION 08 – ULTRA LUXURY: Taj Exotica Resort & Spa, Andamans (Havelock Island, 02 Nights)'),
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Handpicked luxury stays as per chosen tier.', 1),
    _inc_included('Island Transfers: Premium High-Speed Cruise tickets (Makruzz / Nautika).', 2),
    _inc_included('Luxury Ground fleet: Chauffeur-driven private AC vehicle for all transfers.', 3),
    _inc_included('TRAGUIN Support: 24/7 dedicated local guest experience manager assistance.', 4),
    _inc_included('Welcome Amenities: Personalized family island welcome kit upon arrival.', 5),
    _inc_included('Complimentary Experience: 1 Session of Snorkeling at Elephant Beach.', 6),
    _inc_excluded('Domestic Airfare to and from Port Blair.', 7),
    _inc_excluded('Optional Scuba Diving, Sea Walking, or Jet-Ski rental charges.', 8),
    _inc_excluded('Personal items such as laundry, extra beverages, tips, and insurance.', 9),
    _inc_excluded('Any item or meal expense not explicitly declared in specifications.', 10),
        ],
    )
    return package, itinerary

def build_an_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AN-004'
    tour_code = 'TRG-AND-004'
    title = 'Romantic Andaman'
    duration = '05 Nights / 06 Days'
    slug = 'an-004-romantic-andaman'
    itin_slug = 'an-004-romantic-andaman-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code AN-004 | TRAGUIN tour code TRG-AND-004', 1),
    _ph('State / Country: Andaman & Nicobar Islands, India | Category: Premium Luxury Honeymoon', 2),
    _ph('Destinations: Port Blair (2N) • Havelock Island (2N) • Neil Island (1N)', 3),
    _ph('Ideal for: Newlyweds, Romance Seekers & Luxury Explorers', 4),
    _ph('Best season: October to May', 5),
    _ph('Starting price: On Request (Bespoke Luxury Honeymoon Edition)', 6),
    _ph('Vehicle & Meals: Private Luxury AC Vehicle & Premium Catamaran Ferry / CP + Candlelight Dinner', 7),
    _ph('Route: Port Blair (2N) → Havelock Island (2N) → Neil Island (1N) → Port Blair → Departure', 8),
    _ph('TRAGUIN Signature Experience: Private beachside candlelight dinner setup with custom floral arrangements and ambient musical themes.', 9),
    _ph('Curated by TRAGUIN Experts: Seamless scheduling for inter-island catamaran transitions that completely removes long queue wait times.', 10),
    _ph('Personalized Assistance: Direct airport and jetty concierge meet-and-greet services handled by dedicated local experts.', 11),
    _ph('Premium Handpicked Hotels: Elite priority access to premium beach resorts offering private shoreline spaces for perfect isolation.', 12),
    _ph('Shopping & Local Experiences: Local Markets & Souvenirs: Premium genuine pearl jewelry, hand-carved coconut shell ornaments, and mother-of-pearl artifacts at Sagarika Government Emporium. Beachside Cafes: Fresh seafood, wood-fired artisanal pizzas, and tropical fruit mocktails.', 13),
    _ph('Important Notes: Ferry Operations: Inter-island ferry schedules depend on local weather conditions. Water Sports: Scuba diving and snorkeling depend on clear sea visibility. Check-in Policies: Early check-out around 08:00 AM – 09:00 AM to align with morning ferry departures.', 14),
        ],
        moods=['Honeymoon', 'Luxury', 'Romance', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Bespoke Luxury Honeymoon Edition)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Romantic Andaman • An Exotic Escape for Newlyweds • 05 Nights / 06 Days',
        overview='Welcome to a timeless paradise of turquoise waves, powder-white shores, and intimate luxury, beautifully curated by TRAGUIN. Embark on the definitive Romantic Andaman Honeymoon Package designed exclusively for couples seeking a sublime, emotional getaway.\n\nTOUR OVERVIEW\nThis meticulously planned Luxury Andaman Holiday provides a perfect balance of privacy, tropical indulgence, and immersive marine explorations. Featuring handpicked hotels with romantic beachside views, customized honeymoon amenities, and a special complimentary candlelight dining setup, this route presents the ultimate Premium Andaman Experience.',
        seo_title='AN-004 | Romantic Andaman Honeymoon | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Romantic Andaman honeymoon (AN-004 / TRG-AND-004): Port Blair, Havelock Radhanagar Beach, Elephant Beach snorkeling, Neil Island Natural Bridge, candlelight dinner, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Cellular Jail National Memorial, Light & Sound Show, and Carbyn's Cove Beach Promenade", 1),
    _ih('Premium cruise to Havelock and Radhanagar Beach sunset experience', 2),
    _ih('Elephant Beach speedboat excursion with coral reef snorkeling and candlelight dinner', 3),
    _ih('Neil Island Bharatpur Beach, Laxmanpur Beach, and Natural Coral Rock Bridge', 4),
    _ih('TRAGUIN Signature Experience: Private beachside candlelight dinner with custom floral arrangements', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN PORT BLAIR — GATEWAY TO PARADISE & COLONIAL CHRONICLES', ('Your Premium Andaman Experience begins at Veer Savarkar International Airport in Port Blair. A TRAGUIN luxury representative will welcome you with a personalized flower bouquet and escort you via a private executive vehicle to your premium sea-facing resort. After an afternoon of relaxation, embark on a private tour of the historic Cellular Jail, concluding with an emotionally moving Light & Sound Show.'), [
        "Sightseeing Included: Cellular Jail National Memorial, Light & Sound Show, Carbyn's Cove Beach Promenade.",
        "Evening Experience: Romantic evening stroll at Carbyn's Cove beach followed by an intimate welcome dinner.",
        'Overnight Stay: Port Blair (Premium / Luxury Resort)',
        'Meals Included: Welcome Refreshment & Gourmet Dinner',
    ]),
    _day(2, 'PORT BLAIR TO HAVELOCK ISLAND — HIGH-SPEED CRUISE TO SHORES OF INFINITE TURQUOISE', ('Board a premium high-speed luxury catamaran cruise to Havelock Island. Upon arrival, check into an ultra-luxury beach resort featuring private shore access. Late in the afternoon, your private chauffeur will escort you to Radhanagar Beach (Beach No. 7), celebrated worldwide for its powdery white sand and pristine waters.'), [
        'Sightseeing Included: Premium Cruise Transfer, Radhanagar Beach Sunset Experience.',
        'Optional Activities: Professional beachside couple portrait session during the golden hour.',
        'Overnight Stay: Havelock Island (Luxury Beachfront Villa)',
        'Meals Included: Buffet Breakfast & Dinner',
    ]),
    _day(3, 'ELEPHANT BEACH CORAL ADVENTURE — IMMERSIVE MARINE LIFE & EXOTIC UNDERWATER WONDERS', ('Embark on a private speed boat excursion to Elephant Beach. Enjoy a complimentary snorkeling session together to witness exotic sea turtles and colourful marine life. In the evening, enjoy TRAGUIN Exclusive: Premium beachside Candlelight Dinner with a complimentary cake.'), [
        'Sightseeing Included: Elephant Beach Speedboat Excursion, Coral Reef Snorkeling.',
        'Optional Activities: Couples Scuba Diving, Sea Walking, or a glass-bottom boat ride.',
        'Evening Experience: TRAGUIN Exclusive: Premium beachside Candlelight Dinner with a complimentary cake.',
        'Overnight Stay: Havelock Island (Luxury Beachfront Villa)',
        'Meals Included: Breakfast & Private Romantic Candlelight Dinner',
    ]),
    _day(4, 'HAVELOCK ISLAND TO NEIL ISLAND — THE SERENITY OF RUSTIC ISLAND LIFE', ('Take a morning catamaran cruise to the peaceful oasis of Neil Island. Check into your premium resort and visit Bharatpur Beach for gentle, calm lagoons. Later, explore Laxmanpur Beach to see its famous natural coral rock formation (Howrah Bridge), followed by a stunning sunset view.'), [
        'Sightseeing Included: Bharatpur Beach, Laxmanpur Beach, Natural Coral Rock Bridge Formation.',
        'Evening Experience: Stargazing on the quiet private beach of your luxury resort.',
        'Overnight Stay: Neil Island (Premium Luxury Resort)',
        'Meals Included: Breakfast & Exquisite Island Buffet Dinner',
    ]),
    _day(5, 'NEIL ISLAND TO PORT BLAIR — RETURN TO THE CAPITAL & PANORAMIC ISLAND VIEWPOINTS', ('Enjoy a beautiful sunrise walk along the shore before boarding your luxury catamaran ferry back to Port Blair. Spend your afternoon visiting Chidiya Tapu or browse local handicraft emporiums for fine wood carvings and pearl souvenirs.'), [
        'Sightseeing Included: Catamaran Return Ferry, Chidiya Tapu Sunset Viewpoint, Sagarika Government Emporium.',
        'Optional Activities: Fine-dining evening cruise along the Port Blair harbour.',
        'Overnight Stay: Port Blair (Premium / Luxury Resort)',
        'Meals Included: Breakfast & Farewell Luxury Dinner',
    ]),
    _day(6, 'DEPARTURE FROM PORT BLAIR — CHERISHING MEMORIES BEYOND DESTINATIONS', ('Indulge in a final lavish tropical breakfast at your resort. Your private vehicle will pick you up for a smooth transfer to Veer Savarkar International Airport.'), [
        'Transfers Included: Private luxury airport drop-off assistance.',
        'Meals Included: Sumptuous Buffet Breakfast',
    ]),
        ],
        hotels=[
            _hotel('Hotel de Roewen / similar', 'Port Blair', '02 Nights', 'Deluxe', 'Deluxe Room', 'CP + Candlelight Dinner', 4, 1, description='OPTION 01 – DELUXE: Hotel de Roewen / similar (Port Blair, 02 Nights)'),
    _hotel('Symphony Palms Beach Resort', 'Havelock Island', '02 Nights', 'Deluxe', 'Deluxe Room', 'CP + Candlelight Dinner', 4, 2, description='OPTION 02 – DELUXE: Symphony Palms Beach Resort (Havelock Island, 02 Nights)'),
    _hotel('Symphony Summer Sands', 'Neil Island', '01 Night', 'Deluxe', 'Deluxe Room', 'CP + Candlelight Dinner', 4, 3, description='OPTION 03 – DELUXE: Symphony Summer Sands (Neil Island, 01 Night)'),
    _hotel('Peerless Resort / Sea Shell', 'Port Blair', '02 Nights', 'Premium', 'Premium Room', 'CP + Candlelight Dinner', 4, 4, description='OPTION 04 – PREMIUM: Peerless Resort / Sea Shell (Port Blair, 02 Nights)'),
    _hotel('Havelock Island Beach Resort', 'Havelock Island', '02 Nights', 'Premium', 'Premium Room', 'CP + Candlelight Dinner', 4, 5, description='OPTION 05 – PREMIUM: Havelock Island Beach Resort (Havelock Island, 02 Nights)'),
    _hotel('Sea Shell Neil / similar', 'Neil Island', '01 Night', 'Premium', 'Premium Room', 'CP + Candlelight Dinner', 4, 6, description='OPTION 06 – PREMIUM: Sea Shell Neil / similar (Neil Island, 01 Night)'),
    _hotel('Welcomhotel by ITC Bay Island', 'Port Blair', '02 Nights', 'Luxury', 'Luxury Room', 'CP + Candlelight Dinner', 5, 7, description='OPTION 07 – LUXURY: Welcomhotel by ITC Bay Island (Port Blair, 02 Nights)'),
    _hotel('Barefoot at Havelock / Sea Shell', 'Havelock Island', '02 Nights', 'Luxury', 'Luxury Room', 'CP + Candlelight Dinner', 5, 8, description='OPTION 08 – LUXURY: Barefoot at Havelock / Sea Shell (Havelock Island, 02 Nights)'),
    _hotel('Silver Sand Beach Resort', 'Neil Island', '01 Night', 'Luxury', 'Luxury Room', 'CP + Candlelight Dinner', 5, 9, description='OPTION 09 – LUXURY: Silver Sand Beach Resort (Neil Island, 01 Night)'),
    _hotel('Taj Exotica Resort & Spa (Suite)', 'Port Blair', '02 Nights', 'Ultra Luxury', 'Suite', 'CP + Candlelight Dinner', 5, 10, description='OPTION 10 – ULTRA LUXURY: Taj Exotica Resort & Spa (Suite) (Port Blair, 02 Nights)'),
    _hotel('Taj Exotica Resort & Spa (Villa)', 'Havelock Island', '02 Nights', 'Ultra Luxury', 'Villa', 'CP + Candlelight Dinner', 5, 11, description='OPTION 11 – ULTRA LUXURY: Taj Exotica Resort & Spa (Villa) (Havelock Island, 02 Nights)'),
    _hotel('Tilar Siro Neil Island (CGH Earth)', 'Neil Island', '01 Night', 'Ultra Luxury', 'Luxury Suite', 'CP + Candlelight Dinner', 5, 12, description='OPTION 12 – ULTRA LUXURY: Tilar Siro Neil Island (CGH Earth) (Neil Island, 01 Night)'),
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Luxury air-conditioned beachside rooms/villas.', 1),
    _inc_included('Luxury Transportation: Private chauffeur-driven AC vehicle at all islands.', 2),
    _inc_included('Catamaran Ferry Tickets: Premium class seat bookings on Makruzz/Nautika cruises.', 3),
    _inc_included('TRAGUIN Support: 24/7 dedicated local island coordinator assistance.', 4),
    _inc_included('Honeymoon Privileges: 1 Private Candlelight Dinner, bed decoration, and cake.', 5),
    _inc_included('Complimentary Experience: 1 Snorkeling session per person at Elephant Beach.', 6),
    _inc_excluded('Domestic airfare to and from Port Blair.', 7),
    _inc_excluded('Optional scuba diving, sea walking, or jet-ski rental fees.', 8),
    _inc_excluded('Personal expenses such as bar bills, laundry, telephone calls, or tips.', 9),
    _inc_excluded('Camera entry tickets or additional guide charges at monuments.', 10),
        ],
    )
    return package, itinerary

def build_an_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AN-005'
    tour_code = 'TRG-AND-005'
    title = 'Scuba Andaman'
    duration = '05 Nights / 06 Days'
    slug = 'an-005-scuba-andaman'
    itin_slug = 'an-005-scuba-andaman-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code AN-005 | TRAGUIN tour code TRG-AND-005', 1),
    _ph('State / Country: Andaman & Nicobar Islands, India | Category: Premium Luxury Adventure & Scuba Tour', 2),
    _ph('Destinations: Port Blair (2N) • Havelock Island (2N) • Neil Island (1N)', 3),
    _ph('Ideal for: Adventure Seekers, Couples, & Luxury Explorers', 4),
    _ph('Best season: October to May (Flawless marine visibility)', 5),
    _ph('Starting price: On Request (Bespoke Luxury Experience)', 6),
    _ph('Vehicle & Meals: Premium Private AC Vehicle & Premium Cruise (Nautika/Makruzz)', 7),
    _ph('Route: Port Blair (2N) → Havelock Island (2N) → Neil Island (1N) → Port Blair → Departure', 8),
    _ph('TRAGUIN Signature Experience: Private pre-dive technical brief with marine biologists for an enhanced reef understanding.', 9),
    _ph('Curated by TRAGUIN Experts: Perfect cruise timing allocations that cut down queue waiting times significantly at all jetties.', 10),
    _ph('Premium Handpicked Hotels: Hand-vetted beach properties offering completely private beach access and elite premium safety standard hospitality.', 11),
    _ph('Exclusive Recommendations: Secret sunset spots and custom local seafood bistros curated exclusively for TRAGUIN patrons.', 12),
    _ph('Shopping & Local Experiences: Local Markets & Souvenirs: Handcrafted mother-of-pearl jewelry, fine sea-shell interior ornaments, traditional coconut shell bowls, and highly fragrant organic spices. Island Cafes: Wood-fired pizzas, fresh tropical mocktails, and local grilled snapper caught fresh daily.', 13),
    _ph('Important Notes: Scuba Guidelines: No prior swimming skill is required for our resort dive programs. Ferry Discretion: Inter-island ferry operations depend entirely on weather elements. Eco-Tourism Norms: Single-use plastic bottles are completely banned at major beaches.', 14),
        ],
        moods=['Adventure', 'Luxury', 'Scuba', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Bespoke Luxury Experience)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Scuba Andaman • Pure Marine Luxury & Adventure • 05 Nights / 06 Days',
        overview='Welcome to an extraordinary tropical odyssey meticulously crafted by TRAGUIN. Embark on the ultimate Scuba Andaman experience designed exclusively for thrill-seekers and luxury lovers.\n\nTOUR OVERVIEW\nThis elite luxury Andaman holiday package offers an exquisite deep-dive itinerary tailored for premium adventure. Travel seamlessly between islands aboard luxury high-speed catamarans with reserved premium class seating. With signature TRAGUIN curated experiences—including custom PADI-certified scuba diving modules and VIP priority boarding—your tropical voyage is guaranteed to exceed the exceptional.',
        seo_title='AN-005 | Scuba Andaman Adventure | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Scuba Andaman package (AN-005 / TRG-AND-005): PADI-certified scuba dive, Elephant Beach, Radhanagar Beach, Neil Island Natural Bridge, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Cellular Jail National Memorial, Marina Park Promenade, and Light & Sound Show', 1),
    _ih('Premium catamaran cruise to Havelock and Radhanagar Beach sunset', 2),
    _ih('PADI-Guided Premium Scuba Dive at Nemo Reef with underwater photography', 3),
    _ih('Neil Island Natural Rock Bridge, Laxmanpur Beach, and Bharatpur Beach', 4),
    _ih('TRAGUIN Signature Experience: Private pre-dive technical brief with marine biologists', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN PORT BLAIR — GATEWAY TO THE EMERALD ISLANDS', ('Your premium Andaman experience begins as you land at Veer Savarkar International Airport in Port Blair. Receive a warm VIP reception by a dedicated TRAGUIN representative and transfer to your luxury hotel overlooking the azure bay. In the afternoon, embark on an immersive historical journey to the iconic Cellular Jail before enjoying the emotionally moving Sound and Light Show.'), [
        'Sightseeing Included: Cellular Jail National Memorial, Marina Park Promenade, Light & Sound Show.',
        'Evening Experience: Exquisite seafood dinner at a handpicked premium seaside lounge.',
        'Overnight Stay: Port Blair (Premium Ocean-View Property)',
        'Meals Included: Welcome Drink & Luxury Dinner',
    ]),
    _day(2, 'PORT BLAIR TO HAVELOCK ISLAND — HIGH-SPEED CRUISE & RADHANAGAR BEACH', ("Board a premium high-speed luxury catamaran (Nautika or Makruzz) in the morning for a smooth cruise across the deep blue sea to Havelock Island. Upon arrival, check into your ultra-luxury beachfront villa. In the late afternoon, your private chauffeur will escort you to Radhanagar Beach, consistently ranked among Asia's finest shores."), [
        'Sightseeing Included: Radhanagar Beach (Beach No. 7), Scenic Island Cruise.',
        'Optional Activities: Private beachside professional couple/family photoshoot during sunset.',
        'Overnight Stay: Havelock Island (Luxury Beachfront Resort)',
        'Meals Included: Premium Breakfast & Seaside Dinner',
    ]),
    _day(3, 'HAVELOCK ISLAND — THE ULTIMATE SCUBA EXPERIENCE', ('Today features the absolute peak of your Scuba Andaman adventure. Wake up early and head to our premier PADI-certified dive center. Under the personal supervision of a private master diver, plunge into the transparent waters of Nemo Reef or Tribe Gate. Spend your afternoon relaxing at Elephant Beach, accessible via a premium speed boat ride.'), [
        'Sightseeing Included: PADI-Guided Premium Scuba Dive, Elephant Beach Excursion, Speedboat Transfers.',
        'Included Activities: Underwater high-definition video and photography capture of your dive.',
        'Overnight Stay: Havelock Island (Luxury Beachfront Resort)',
        'Meals Included: Buffet Breakfast & Curated Fusion Dinner',
    ]),
    _day(4, 'HAVELOCK ISLAND TO NEIL ISLAND — NATURAL CORAL BRIDGES', ('After a delightful morning breakfast, take a premium mid-day cruise to Neil Island. In the afternoon, visit the famous Howrah Bridge natural rock formation—a highly popular Instagram location carved purely by the sea. Follow this with a relaxing stroll along Laxmanpur Beach to observe a spellbinding sunset over shallow coral flats.'), [
        'Sightseeing Included: Natural Rock Bridge, Laxmanpur Beach, Bharatpur Beach.',
        'Evening Experience: Private beach side candlelit dinner with premium wine/mocktails arranged by TRAGUIN.',
        'Overnight Stay: Neil Island (Premium Luxury Resort)',
        'Meals Included: Breakfast & Exclusive Candlelit Dinner',
    ]),
    _day(5, 'NEIL ISLAND TO PORT BLAIR — RETURN & SOUVENIR SHOPPING', ('Enjoy a relaxed morning beach walk or indulge in water sports at Bharatpur Beach. Later, board your luxury catamaran for a smooth return voyage back to Port Blair. Spend your evening exploring the boutique souvenir emporiums of Port Blair.'), [
        'Sightseeing Included: Sagarika Government Emporium, Local Spice Markets.',
        'Optional Activities: Evening dinner cruise with live music along the Port Blair harbor (On Request).',
        'Overnight Stay: Port Blair (Premium Luxury Property)',
        'Meals Included: Breakfast & Farewell Premium Dinner',
    ]),
    _day(6, 'PORT BLAIR — DEPARTURE', ('Indulge in a final gourmet buffet breakfast at your resort. Your private luxury transport will safely convey you to Veer Savarkar International Airport.'), [
        'Transfers Included: Private luxury airport departure drop-off.',
        'Meals Included: Sumptuous Buffet Breakfast',
    ]),
        ],
        hotels=[
            _hotel('Peerless Resort / similar', 'Port Blair', '02 Nights', 'Deluxe', 'Deluxe Room', 'Premium Buffet', 4, 1, description='OPTION 01 – DELUXE: Peerless Resort / similar (Port Blair, 02 Nights)'),
    _hotel('Symphony Palms Beach Resort', 'Havelock Island', '02 Nights', 'Deluxe', 'Deluxe Room', 'Premium Buffet', 4, 2, description='OPTION 02 – DELUXE: Symphony Palms Beach Resort (Havelock Island, 02 Nights)'),
    _hotel('Symphony Samudra Resort', 'Neil Island', '01 Night', 'Deluxe', 'Deluxe Room', 'Premium Buffet', 4, 3, description='OPTION 03 – DELUXE: Symphony Samudra Resort (Neil Island, 01 Night)'),
    _hotel('SeaShell Port Blair / similar', 'Port Blair', '02 Nights', 'Premium', 'Premium Room', 'Premium Buffet', 4, 4, description='OPTION 04 – PREMIUM: SeaShell Port Blair / similar (Port Blair, 02 Nights)'),
    _hotel('Havelock Island Beach Resort', 'Havelock Island', '02 Nights', 'Premium', 'Premium Room', 'Premium Buffet', 4, 5, description='OPTION 05 – PREMIUM: Havelock Island Beach Resort (Havelock Island, 02 Nights)'),
    _hotel('SeaShell Neil Island / similar', 'Neil Island', '01 Night', 'Premium', 'Premium Room', 'Premium Buffet', 4, 6, description='OPTION 06 – PREMIUM: SeaShell Neil Island / similar (Neil Island, 01 Night)'),
    _hotel('Welcomhotel by ITC Bay Island', 'Port Blair', '02 Nights', 'Luxury', 'Luxury Room', 'Premium Buffet', 5, 7, description='OPTION 07 – LUXURY: Welcomhotel by ITC Bay Island (Port Blair, 02 Nights)'),
    _hotel('Barefoot at Havelock / SeaShell', 'Havelock Island', '02 Nights', 'Luxury', 'Luxury Room', 'Premium Buffet', 5, 8, description='OPTION 08 – LUXURY: Barefoot at Havelock / SeaShell (Havelock Island, 02 Nights)'),
    _hotel('Silver Sand Beach Resort', 'Neil Island', '01 Night', 'Luxury', 'Luxury Room', 'Premium Buffet', 5, 9, description='OPTION 09 – LUXURY: Silver Sand Beach Resort (Neil Island, 01 Night)'),
    _hotel('Taj Exotica Resort & Spa (Port Blair Suite)', 'Port Blair', '02 Nights', 'Ultra Luxury', 'Suite', 'Premium Buffet', 5, 10, description='OPTION 10 – ULTRA LUXURY: Taj Exotica Resort & Spa (Port Blair Suite) (Port Blair, 02 Nights)'),
    _hotel('Taj Exotica Resort & Spa, Radhanagar', 'Havelock Island', '02 Nights', 'Ultra Luxury', 'Luxury Villa', 'Premium Buffet', 5, 11, description='OPTION 11 – ULTRA LUXURY: Taj Exotica Resort & Spa, Radhanagar (Havelock Island, 02 Nights)'),
    _hotel('Tiamo Luxury Beach Villa Private Pool', 'Neil Island', '01 Night', 'Ultra Luxury', 'Private Pool Villa', 'Premium Buffet', 5, 12, description='OPTION 12 – ULTRA LUXURY: Tiamo Luxury Beach Villa Private Pool (Neil Island, 01 Night)'),
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Luxury beachfront properties as per chosen tier.', 1),
    _inc_included('Inter-Island Catamaran: Premium class tickets on high-speed Makruzz / Nautika.', 2),
    _inc_included('Luxury Transportation: Private executive AC vehicle for all land sightseeings.', 3),
    _inc_included('TRAGUIN Support: 24/7 dedicated local concierge assistance across islands.', 4),
    _inc_included('Exclusive Adventure: 1 Premium PADI-certified scuba dive with underwater footage.', 5),
    _inc_included('Special Welcome: Signature floral welcome drink and custom island travel kit.', 6),
    _inc_excluded('Domestic airfare from mainland India to Port Blair.', 7),
    _inc_excluded('Optional water activities (Jet Ski, Sea Walk, Parasailing).', 8),
    _inc_excluded('Personal expenses such as laundry, phone bar, tips, and insurance.', 9),
    _inc_excluded('Any service not specifically cited in the inclusions block.', 10),
        ],
    )
    return package, itinerary

def build_an_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AN-006'
    tour_code = 'TRG-AND-006'
    title = 'Luxury Andaman Escape'
    duration = '06 Nights / 07 Days'
    slug = 'an-006-luxury-andaman-escape'
    itin_slug = 'an-006-luxury-andaman-escape-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code AN-006 | TRAGUIN tour code TRG-AND-006', 1),
    _ph('State / Country: Andaman & Nicobar Islands, India | Category: Luxury Travel Escape', 2),
    _ph('Destinations: Port Blair (3N) • Havelock Island (2N) • Neil Island (1N)', 3),
    _ph('Ideal for: Honeymooners, Luxury Connoisseurs & Discerning Families', 4),
    _ph('Best season: October to May', 5),
    _ph('Starting price: On Request (Bespoke Ultra-Luxury Pricing)', 6),
    _ph('Vehicle & Meals: Private Luxury AC Vehicle & Premium Cruise (Nautika/Makruzz Premium)', 7),
    _ph('Route: Port Blair (3N) → Havelock Island (2N) → Neil Island (1N) → Port Blair → Departure', 8),
    _ph('TRAGUIN Signature Experience: Private beach setup at Radhanagar with refreshments during sunset hour.', 9),
    _ph('Curated by TRAGUIN Experts: Direct premium seat upgrades on island cruise vessels bypassing long public queues.', 10),
    _ph('Personalized Assistance: Dedicated coordinators present at every jetty point to manage luggage and ticketing seamlessly.', 11),
    _ph('Luxury Transportation: Elite premium private fleet matching meticulous maintenance schedules.', 12),
    _ph('Shopping & Local Experiences: Sagarika Emporium & Local Markets: Authentic mother-of-pearl jewelry, hand-carved coconut shell artifacts, and premium wooden spice boxes. Beachfront Cafes: Fresh catch lobster and international woodfired pizzas at high-end seaside cafes in Havelock Island.', 13),
    _ph('Important Notes: Ferry Operations: Catamaran cruise sailings depend entirely on sea weather conditions and technical clearance. Hotel Policies: Island check-out times are early, usually around 08:00 hrs to 09:00 hrs, aligned with cruise schedules. Advance Bookings: Highly recommended to book 45-60 days ahead during peak travel season (October through May).', 14),
        ],
        moods=['Luxury', 'Honeymoon', 'Family', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Bespoke Ultra-Luxury Pricing)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Luxury Andaman Escape • Tropical Opulence & Paradise Beachfronts • 06 Nights / 07 Days',
        overview="Welcome to an unforgettable journey curated exclusively by TRAGUIN. Embark on the finest Luxury Andaman Escape, specifically engineered to offer an exquisite fusion of breathtaking landscapes, premium stays, and immersive experiences across India's premier tropical paradise.\n\nTOUR OVERVIEW\nThis elite 06 Nights / 07 Days itinerary takes you across the turquoise expanses of the Bay of Bengal, traversing Port Blair, Havelock Island, and Neil Island. Traveling in seamless, air-conditioned executive luxury vehicles with private assistance at every jetty, you will sail past the open seas via the premium cabins of high-speed luxury catamarans.",
        seo_title='AN-006 | Luxury Andaman Escape | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Luxury Andaman Escape (AN-006 / TRG-AND-006): Port Blair, Havelock Radhanagar Beach, Elephant Beach, Neil Island candlelight dinner, Ross Island, North Bay, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Cellular Jail Museum, Carbyn's Cove Beach Promenade, and Light & Sound Show", 1),
    _ih('Radhanagar Beach and luxury catamaran island transit to Havelock', 2),
    _ih('Elephant Beach guided snorkeling and private speedboat transfers', 3),
    _ih('Laxmanpur Natural Bridge, Bharatpur Coral Beach, and private oceanside dinner on Neil Island', 4),
    _ih('Ross Island Ruins, North Bay Lighthouse Island, and glass-bottom coral viewing', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN PORT BLAIR — WELCOME TO THE TROPICAL GATEWAY', ('Your premium Andaman experience begins as you step onto the runway of Veer Savarkar International Airport in Port Blair. Your private luxury chauffeur-driven vehicle and a dedicated TRAGUIN guest coordinator await to escort you to your premium hotel. After check-in and an exquisite lunch, explore the poignant national heritage of Cellular Jail. As dusk falls, enjoy VIP-seated access to the legendary Light and Sound Show.'), [
        "Sightseeing Included: Cellular Jail Museum, Carbyn's Cove Beach Promenade, National Memorial Light & Sound Show.",
        'Evening Experience: Exclusive welcoming seafood culinary dinner curated by TRAGUIN experts.',
        'Overnight Stay: Port Blair (Premium Ocean-View Resort)',
        'Meals Included: Welcome Exotic Beverage & Luxury Dinner',
    ]),
    _day(2, 'PORT BLAIR TO HAVELOCK ISLAND — HIGH-SPEED LUXURY CRUISE', ('Board an executive high-speed luxury catamaran (Nautika or Makruzz) from Haddo Jetty to Havelock Island. Upon arrival at Havelock, transfer smoothly to your ultra-luxury beachfront villa. In the afternoon, journey to Radhanagar Beach, universally celebrated for its powdery white sand and breathtaking landscapes.'), [
        'Sightseeing Included: Radhanagar Beach (Beach No. 7), Luxury Catamaran Island Transit.',
        "Evening Experience: Private beachside starlit stroll along the resort's restricted coastline.",
        'Overnight Stay: Havelock Island (Ultra-Luxury Beachfront Resort)',
        'Meals Included: Premium Buffet Breakfast & Multi-cuisine Dinner',
    ]),
    _day(3, 'ELEPHANT BEACH AQUATIC EXCURSION — IMMERSIVE MARINE LIFE', ('Embark on a private speedboat charter heading directly to Elephant Beach, a prime hotspot for marine adventure and popular Instagram locations. Known for its turquoise water and brilliant shallow coral reefs, it provides the perfect setting for curated experiences like snorkeling and sea-walking. Return to your resort by afternoon for an exclusive luxury spa session.'), [
        'Sightseeing Included: Elephant Beach, Guided Snorkeling Session, Private Speedboat Transfers.',
        'Optional Activities: PADI Discover Scuba Diving with a private instructor and underwater photography.',
        'Overnight Stay: Havelock Island (Ultra-Luxury Beachfront Resort)',
        "Meals Included: Breakfast & Special Chef's Choice Dinner",
    ]),
    _day(4, 'HAVELOCK ISLAND TO NEIL ISLAND — EXPLORING SHAHEED DWEEP', ('Sail via cruise to Neil Island, an oasis of agricultural serenity and quiet iconic attractions. Check into your premium stay and venture out to Laxmanpur Beach to view its famous natural rock arch bridge. Later, travel to Bharatpur Beach for a quiet evening watching the gentle tide break across a vibrant coral shelf.'), [
        'Sightseeing Included: Laxmanpur Natural Bridge, Bharatpur Coral Beach, Inter-Island Premium Cruise.',
        'Evening Experience: A private candlelight dinner directly on the sandy shores, arranged by TRAGUIN.',
        'Overnight Stay: Neil Island (Premium Luxury Resort)',
        'Meals Included: Breakfast & Private Oceanside Dinner',
    ]),
    _day(5, 'NEIL ISLAND TO PORT BLAIR — SUNSET PANORAMAS AT CHIDIYATAPU', ('Catch a late-morning luxury cruise back to Port Blair. After checking in to your premium suite, take a scenic coastal drive to Chidiyatapu, famed for its breathtaking landscapes and dense mangrove woods. Walk up to the sunset point to view the sun dip below the horizon of the open ocean.'), [
        'Sightseeing Included: Chidiyatapu Sunset Viewpoint, Biological Park trail, Local Souvenir Emporium.',
        'Optional Activities: High-end shopping for genuine pearl jewelry and rare shell handicrafts.',
        'Overnight Stay: Port Blair (Premium Luxury Resort)',
        'Meals Included: Breakfast & Premium Continental Dinner',
    ]),
    _day(6, 'ROSS ISLAND & NORTH BAY EXCURSION — VICTORIAN RUINS', ('Board a premium private boat to Ross Island (Netaji Subhash Chandra Bose Island), the historic British administrative headquarters now draped in beautiful ficus tree roots and wandering deer. Continue onward to North Bay Island, whose iconic lighthouse is immortalized on the Indian twenty-rupee note. Experience a glass-bottom boat ride to look into the coral ecosystem without getting wet.'), [
        'Sightseeing Included: Ross Island Ruins, North Bay Lighthouse Island, Glass-Bottom Coral Viewing.',
        'Evening Experience: Farewell cocktail session and a curated dinner review with your guest manager.',
        'Overnight Stay: Port Blair (Premium Luxury Resort)',
        'Meals Included: Breakfast & Gala Farewell Dinner',
    ]),
    _day(7, 'PORT BLAIR — DEPARTURE', ('Indulge in a final lavish breakfast looking out over the sea. Your private luxury car will transport you seamlessly to Veer Savarkar International Airport for your return flight.'), [
        'Transfers Included: Private luxury airport departure drop-off.',
        'Meals Included: Sumptuous Buffet Breakfast',
    ]),
        ],
        hotels=[
            _hotel('Peerless Resort / similar', 'Port Blair', '03 Nights', 'Deluxe', 'Deluxe Room', 'MAPAI (Breakfast & Dinner)', 4, 1, description='OPTION 01 – DELUXE: Peerless Resort / similar (Port Blair, 03 Nights)'),
    _hotel('Symphony Palms Beach Resort', 'Havelock Island', '02 Nights', 'Deluxe', 'Deluxe Room', 'MAPAI (Breakfast & Dinner)', 4, 2, description='OPTION 02 – DELUXE: Symphony Palms Beach Resort (Havelock Island, 02 Nights)'),
    _hotel('Symphony Summer Sands', 'Neil Island', '01 Night', 'Deluxe', 'Deluxe Room', 'MAPAI (Breakfast & Dinner)', 4, 3, description='OPTION 03 – DELUXE: Symphony Summer Sands (Neil Island, 01 Night)'),
    _hotel('SeaShell Hotel / Lemon Tree', 'Port Blair', '03 Nights', 'Premium', 'Premium Room', 'MAPAI (Breakfast & Dinner)', 4, 4, description='OPTION 04 – PREMIUM: SeaShell Hotel / Lemon Tree (Port Blair, 03 Nights)'),
    _hotel('SeaShell Havelock / Sandyy Wavess', 'Havelock Island', '02 Nights', 'Premium', 'Premium Room', 'MAPAI (Breakfast & Dinner)', 4, 5, description='OPTION 05 – PREMIUM: SeaShell Havelock / Sandyy Wavess (Havelock Island, 02 Nights)'),
    _hotel('SeaShell Neil / Silver Sand Beach', 'Neil Island', '01 Night', 'Premium', 'Premium Room', 'MAPAI (Breakfast & Dinner)', 4, 6, description='OPTION 06 – PREMIUM: SeaShell Neil / Silver Sand Beach (Neil Island, 01 Night)'),
    _hotel('Welcomhotel by ITC Bay Island', 'Port Blair', '03 Nights', 'Luxury', 'Luxury Room', 'MAPAI (Breakfast & Dinner)', 5, 7, description='OPTION 07 – LUXURY: Welcomhotel by ITC Bay Island (Port Blair, 03 Nights)'),
    _hotel('Barefoot at Havelock / Symphony Samudra', 'Havelock Island', '02 Nights', 'Luxury', 'Luxury Room', 'MAPAI (Breakfast & Dinner)', 5, 8, description='OPTION 08 – LUXURY: Barefoot at Havelock / Symphony Samudra (Havelock Island, 02 Nights)'),
    _hotel('Silver Sand Sentinel Luxury Suite', 'Neil Island', '01 Night', 'Luxury', 'Luxury Suite', 'MAPAI (Breakfast & Dinner)', 5, 9, description='OPTION 09 – LUXURY: Silver Sand Sentinel Luxury Suite (Neil Island, 01 Night)'),
    _hotel('Taj Exotica Resort & Spa (Suite)', 'Port Blair', '03 Nights', 'Ultra Luxury', 'Suite', 'MAPAI (Breakfast & Dinner)', 5, 10, description='OPTION 10 – ULTRA LUXURY: Taj Exotica Resort & Spa (Suite) (Port Blair, 03 Nights)'),
    _hotel('Taj Exotica Resort & Spa (Havelock)', 'Havelock Island', '02 Nights', 'Ultra Luxury', 'Luxury Villa', 'MAPAI (Breakfast & Dinner)', 5, 11, description='OPTION 11 – ULTRA LUXURY: Taj Exotica Resort & Spa (Havelock) (Havelock Island, 02 Nights)'),
    _hotel('SeaShell Neil Island (Luxury Lagoon Villa)', 'Neil Island', '01 Night', 'Ultra Luxury', 'Luxury Lagoon Villa', 'MAPAI (Breakfast & Dinner)', 5, 12, description='OPTION 12 – ULTRA LUXURY: SeaShell Neil Island (Luxury Lagoon Villa) (Neil Island, 01 Night)'),
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury accommodations at handpicked hotels.', 1),
    _inc_included('Cruise Transits: Premium seat ticket allocations on Nautika / Makruzz.', 2),
    _inc_included('Luxury Transportation: Private executive AC vehicles throughout the tour.', 3),
    _inc_included('TRAGUIN Support: 24/7 dedicated local island coordinator assistance.', 4),
    _inc_included('Curated Meals: Lavish daily breakfasts and premium gourmet dinners.', 5),
    _inc_included('Welcome Amenities: Customized floral lei welcome and airport travel kit.', 6),
    _inc_included('Exclusive Experiences: Private candlelight dinner experience on Neil Island.', 7),
    _inc_included('Taxes & Permits: All island entry permits, forest fees, and taxes included.', 8),
    _inc_excluded('Domestic or international flights to Port Blair.', 9),
    _inc_excluded('Optional Scuba Diving, Sea-walking, or advanced water sports.', 10),
    _inc_excluded('Personal expenses such as bar bills, laundry, and guide tips.', 11),
    _inc_excluded('Additional extensions caused by flight delays or weather conditions.', 12),
        ],
    )
    return package, itinerary

def build_an_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AN-007'
    tour_code = 'TRG-AND-007'
    title = 'Andaman Explorer'
    duration = '07 Nights / 08 Days'
    slug = 'an-007-andaman-explorer'
    itin_slug = 'an-007-andaman-explorer-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code AN-007 | TRAGUIN tour code TRG-AND-007', 1),
    _ph('State / Country: Andaman & Nicobar Islands, India | Category: Premium Family Tour', 2),
    _ph('Destinations: Port Blair (4N) • Havelock Island (2N) • Neil Island (1N)', 3),
    _ph('Ideal for: Family Vacations, Luxury Explorers & Beach Lovers', 4),
    _ph('Best season: October to May', 5),
    _ph('Starting price: On Request (Premium Customized Luxury)', 6),
    _ph('Vehicle & Meals: Private Luxury AC Vehicle / MAPAI (Breakfast & Dinner)', 7),
    _ph('Route: Port Blair (4N) → Havelock Island (2N) → Neil Island (1N) → Port Blair → Departure', 8),
    _ph('TRAGUIN Signature Experience: Private, fast-track boarding at all inter-island ferry jetties, completely bypassing standard crowds.', 9),
    _ph('Curated by TRAGUIN Experts: Handpicked premium beachfront resort accommodations featuring reserved private beach access.', 10),
    _ph('Luxury Transportation: Chauffeur-driven, private, spotless luxury vehicles across all islands, matched with elite cruise classes.', 11),
    _ph('Exclusive Recommendations: VIP seating reservations for cellular jail evening light shows and popular beachfront sunset lounges.', 12),
    _ph("Shopping & Local Experiences: Local Souvenirs: Exquisite mother-of-pearl jewelry, hand-carved padauk wood artifacts, artisanal coconut-shell bowls, and beautiful beach resort wear. Cafes & Gastronomy: Fresh grilled lobster at premium beachside shacks and handcrafted tropical mocktails at Havelock's elite cafes.", 13),
    _ph('Important Notes: Booking Policy: We highly advise securing reservations at least 45–60 days in advance. Ferry Operations: Cruise timings are subject to weather conditions—TRAGUIN seamlessly manages all re-routing contingencies. Hotel Policies: Island check-in is generally at 12:00 PM and check-out is at 09:00 AM to align with cruise schedules.', 14),
        ],
        moods=['Family', 'Luxury', 'Beach', 'Explorer'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Customized Luxury)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Andaman Explorer • Tropical Paradise & Unmatched Luxury • 07 Nights / 08 Days',
        overview='Welcome to a timeless paradise sculpted from turquoise waters and ivory sand shores, curated precisely by TRAGUIN. Embark on the most exquisite Andaman Family Tour designed to connect your loved ones with breathtaking landscapes, moving historical echoes, and deep ocean wonders.\n\nTOUR OVERVIEW\nThis meticulously plotted luxury holiday package offers an exceptional balance between coastal indulgence, dynamic marine adventure, and historic heritage explorations. Traveling across islands via elite high-speed private catamarans (Makruzz/Nautika) and arriving at your destinations with dedicated private luxury AC vehicles, your family is guaranteed absolute comfort.',
        seo_title='AN-007 | Andaman Explorer | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Andaman Explorer package (AN-007 / TRG-AND-007): Port Blair, Havelock Radhanagar Beach, Elephant Beach, Neil Island Natural Bridge, Ross Island, North Bay, Chidiyatapu, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Cellular Jail National Memorial, Carbyn's Cove Beach, and Light and Sound Show", 1),
    _ih('Radhanagar Beach and private luxury cruise transit to Havelock', 2),
    _ih('Elephant Beach speedboat transfer, coral reef exploration, and snorkeling', 3),
    _ih('Natural Rock Bridge Structure, reef eco-walk, and return catamaran cruise', 4),
    _ih('Ross Island British Ruins, North Bay Island Lighthouse, and Chidiyatapu Biological Park', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN PORT BLAIR — WELCOME TO THE VEIL OF HISTORY', ('Your premium Andaman experience begins as your flight glides over magnificent azure waves into Veer Savarkar International Airport in Port Blair. A dedicated private luxury transport escort from TRAGUIN warmly welcomes you and transfers your family to a handpicked premium stay overlooking the sea. Proceed to the iconic Cellular Jail for a profoundly moving afternoon walk, followed by the famed Light and Sound Show.'), [
        "Sightseeing Included: Cellular Jail National Memorial, Carbyn's Cove Beach, High-Tech Light and Sound Show.",
        "Evening Experience: Private sunset cocktail hour or fresh coconut dynamic tasting at Carbyn's Cove promenade.",
        'Overnight Stay: Port Blair (Premium Ocean-View Hotel / Resort)',
        'Meals Included: Welcome Drink & Luxury Welcome Dinner',
    ]),
    _day(2, 'PORT BLAIR TO HAVELOCK ISLAND — VOYAGE ACROSS THE AZURE WATERS', ('Board an elite private high-speed catamaran cruise in the premium cabin class towards Havelock Island (Swaraj Dweep). Upon arrival at Havelock, check into your ultra-luxury beachfront villa resort. In the late afternoon, your private vehicle takes you to the legendary Radhanagar Beach.'), [
        "Sightseeing Included: Radhanagar Beach (Asia's Top Ranked Coastal Wonder), Private Luxury Cruise Transit.",
        'Evening Experience: Bespoke candlelit family dinner setup under the stars arranged by TRAGUIN experts.',
        'Overnight Stay: Havelock Island (Bespoke Luxury Beachfront Resort)',
        'Meals Included: Premium Breakfast & Gourmet Beachfront Dinner',
    ]),
    _day(3, 'ELEPHANT BEACH AQUATIC EXCURSION — VIBRANT REEFS', ('An exhilarating morning awaits as you cruise to Elephant Beach, the absolute epicentre for aquatic sightseeing in Andaman. Your family will enjoy a complimentary glass-bottom boat ride or customized snorkeling session. Return to the resort by afternoon to relax amidst tropical foliage.'), [
        'Sightseeing Included: Elephant Beach Speedboat Transfer, Coral Reef Exploration, Shallow Reef Snorkeling.',
        'Optional Activities: Premium PADI Scuba Diving, Sea Walking, Parasailing over the turquoise lagoon.',
        'Overnight Stay: Havelock Island (Bespoke Luxury Beachfront Resort)',
        'Meals Included: Resort Breakfast & Master Chef Specially Curated Dinner',
    ]),
    _day(4, 'HAVELOCK ISLAND TO NEIL ISLAND — TRANQUIL ISLAND VIBES', ('Bid farewell to Havelock and board the mid-day premium cruise to Neil Island (Shaheed Dweep). In the afternoon, explore Bharatpur Beach, where you can walk deep into the calm waters, and Laxmanpur Beach, where beautiful sunset photography points showcase the dramatic artistic power of nature.'), [
        'Sightseeing Included: Bharatpur Beach coral zone, Laxmanpur Beach twilight point, Inter-island Cruise.',
        'Evening Experience: Relaxed stroll through local island fruit orchards and organic produce markets.',
        'Overnight Stay: Neil Island (Premium Luxury Private Villa Resort)',
        'Meals Included: Sumptuous Breakfast & Fresh Catch Specialty Dinner',
    ]),
    _day(5, 'NEIL ISLAND EXCURSION TO PORT BLAIR — THE NATURAL ROCK BRIDGE ARCH', ('Wake up to the sound of chirping tropical birds and visit the remarkable Natural Coral Bridge, a geological masterpiece and a highly popular Instagram location. Late in the afternoon, board your premium return cruise back to Port Blair.'), [
        'Sightseeing Included: Natural Rock Bridge Structure, Reef Eco-Walk, Return High-Speed Catamaran Cruise.',
        'Evening Experience: Premium lounge dining overlooking the harbor in Port Blair.',
        'Overnight Stay: Port Blair (Premium Luxury Stay)',
        'Meals Included: Breakfast & Continental Luxury Dinner',
    ]),
    _day(6, 'ROSS ISLAND & NORTH BAY EXCURSION — COLONIAL RUINS', ('Board a private luxury speed vessel to Ross Island (Netaji Subhash Chandra Bose Dweep), the former British administrative capital. Afterward, visit North Bay Island—the iconic island featured on the back of the Indian twenty-rupee note—famous for its signature lighthouse and glass-bottom semi-submarine coral viewing safaris.'), [
        'Sightseeing Included: Ross Island British Ruins, North Bay Island Lighthouse, Semi-Submarine Safari (optional).',
        'Special Highlight: A guided historical walk through the remnants of the old Presbyterian church and bakery.',
        'Overnight Stay: Port Blair (Premium Luxury Stay)',
        'Meals Included: Premium Breakfast & Regional Fusion Dinner',
    ]),
    _day(7, 'CHIDIYATAPU BIODIVERSITY & SUNSET CRUISE — THE SUNSET CHRONICLES', ("Dedicate your morning to luxury shopping and culture in Port Blair's high-end souvenir boutiques. In the afternoon, travel along a scenic forest drive to Chidiyatapu, famously called the Bird Island of Andaman. Relax at Munda Pahar Beach as you watch the final sunset of your luxury holiday."), [
        'Sightseeing Included: Chidiyatapu Biological Park, Munda Pahar Beach, Luxury Wood Handicraft Emporium.',
        'Evening Experience: A grand, multi-course farewell dinner meticulously crafted by TRAGUIN culinary experts.',
        'Overnight Stay: Port Blair (Premium Luxury Stay)',
        'Meals Included: Breakfast & Gala Farewell Dinner',
    ]),
    _day(8, 'DEPARTURE FROM PORT BLAIR — FOREVER EMBEDDED IN PARADISE', ('Enjoy a final luxury breakfast overlooking the tropical sea. Your private premium vehicle safely transfers your family to Veer Savarkar International Airport.'), [
        'Transfers Included: Private luxury airport departure transfer.',
        'Meals Included: Lavish Buffet Breakfast',
    ]),
        ],
        hotels=[
            _hotel('Hotel Sentinel / Peerless Resort', 'Port Blair', '04 Nights', 'Deluxe', 'Deluxe Room', 'MAPAI (Breakfast & Dinner)', 4, 1, description='OPTION 01 – DELUXE: Hotel Sentinel / Peerless Resort (Port Blair, 04 Nights)'),
    _hotel('Symphony Palms Beach Resort', 'Havelock Island', '02 Nights', 'Deluxe', 'Deluxe Room', 'MAPAI (Breakfast & Dinner)', 4, 2, description='OPTION 02 – DELUXE: Symphony Palms Beach Resort (Havelock Island, 02 Nights)'),
    _hotel('Summer Sands Beach Resort', 'Neil Island', '01 Night', 'Deluxe', 'Deluxe Room', 'MAPAI (Breakfast & Dinner)', 4, 3, description='OPTION 03 – DELUXE: Summer Sands Beach Resort (Neil Island, 01 Night)'),
    _hotel('SeaShell Port Blair / similar', 'Port Blair', '04 Nights', 'Premium', 'Premium Room', 'MAPAI (Breakfast & Dinner)', 4, 4, description='OPTION 04 – PREMIUM: SeaShell Port Blair / similar (Port Blair, 04 Nights)'),
    _hotel('Havelock Island Beach Resort', 'Havelock Island', '02 Nights', 'Premium', 'Premium Room', 'MAPAI (Breakfast & Dinner)', 4, 5, description='OPTION 05 – PREMIUM: Havelock Island Beach Resort (Havelock Island, 02 Nights)'),
    _hotel('SeaShell Neil / similar', 'Neil Island', '01 Night', 'Premium', 'Premium Room', 'MAPAI (Breakfast & Dinner)', 4, 6, description='OPTION 06 – PREMIUM: SeaShell Neil / similar (Neil Island, 01 Night)'),
    _hotel('Welcomhotel by ITC Bay Island', 'Port Blair', '04 Nights', 'Luxury', 'Luxury Room', 'MAPAI (Breakfast & Dinner)', 5, 7, description='OPTION 07 – LUXURY: Welcomhotel by ITC Bay Island (Port Blair, 04 Nights)'),
    _hotel('Barefoot at Havelock / Symphony Samudra', 'Havelock Island', '02 Nights', 'Luxury', 'Luxury Room', 'MAPAI (Breakfast & Dinner)', 5, 8, description='OPTION 08 – LUXURY: Barefoot at Havelock / Symphony Samudra (Havelock Island, 02 Nights)'),
    _hotel('Silver Sand Beach Resort (Luxury Villa)', 'Neil Island', '01 Night', 'Luxury', 'Luxury Villa', 'MAPAI (Breakfast & Dinner)', 5, 9, description='OPTION 09 – LUXURY: Silver Sand Beach Resort (Luxury Villa) (Neil Island, 01 Night)'),
    _hotel('Taj Exotica Resort & Spa (Port Blair Suite)', 'Port Blair', '04 Nights', 'Ultra Luxury', 'Suite', 'MAPAI (Breakfast & Dinner)', 5, 10, description='OPTION 10 – ULTRA LUXURY: Taj Exotica Resort & Spa (Port Blair Suite) (Port Blair, 04 Nights)'),
    _hotel('Taj Exotica Resort & Spa (Radhanagar Beach)', 'Havelock Island', '02 Nights', 'Ultra Luxury', 'Luxury Villa', 'MAPAI (Breakfast & Dinner)', 5, 11, description='OPTION 11 – ULTRA LUXURY: Taj Exotica Resort & Spa (Radhanagar Beach) (Havelock Island, 02 Nights)'),
    _hotel('SeaShell Neil (Exclusive Lagoon Villa)', 'Neil Island', '01 Night', 'Ultra Luxury', 'Lagoon Villa', 'MAPAI (Breakfast & Dinner)', 5, 12, description='OPTION 12 – ULTRA LUXURY: SeaShell Neil (Exclusive Lagoon Villa) (Neil Island, 01 Night)'),
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Luxury beachfront properties as per chosen category.', 1),
    _inc_included('Luxury Transportation: Private AC premium vehicles for all airport/jetty transfers.', 2),
    _inc_included('Premium Cruise Transfers: High-speed luxury catamaran tickets (Makruzz/Nautika) in premium cabin class.', 3),
    _inc_included('TRAGUIN Support: 24/7 dedicated on-ground guest experience concierge.', 4),
    _inc_included('Welcome Amenities: Personalized coconut water welcome toast, flower garlands, and a custom family beach kit.', 5),
    _inc_included('Complimentary Experience: Private snorkeling or glass-bottom boat excursion at Elephant Beach.', 6),
    _inc_excluded('Domestic flights to and from Port Blair.', 7),
    _inc_excluded('Scuba diving, sea walking, or advanced water adventure sports fees.', 8),
    _inc_excluded('Personal expenses such as laundry, premium bar selections, room service, and tips.', 9),
    _inc_excluded('Optional localized island excursions not mentioned in the core itinerary.', 10),
        ],
    )
    return package, itinerary

def build_an_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AN-008'
    tour_code = 'TRG-AND-008'
    title = 'Ladies Island Tour'
    duration = '05 Nights / 06 Days'
    slug = 'an-008-ladies-island-tour'
    itin_slug = 'an-008-ladies-island-tour-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code AN-008 | TRAGUIN tour code TRG-AND-008', 1),
    _ph('State / Country: Andaman & Nicobar Islands, India | Category: Female-Only / Ladies Island Tour', 2),
    _ph('Destinations: Port Blair (2N) • Havelock Island (2N) • Neil Island (1N)', 3),
    _ph('Ideal for: Solo Women Travelers, Girlfriends Getaways & Female Explorers', 4),
    _ph('Best season: October to May', 5),
    _ph('Starting price: On Request (Premium Bespoke Package)', 6),
    _ph('Vehicle & Meals: Private Luxury AC Vehicle / CP Plus (Daily Gourmet Breakfast)', 7),
    _ph('Route: Port Blair (2N) → Havelock Island (2N) → Neil Island (1N) → Port Blair → Departure', 8),
    _ph("TRAGUIN Signature Experience: Private, secured beach side yoga and meditation circles designed exclusively for our ladies' cohort.", 9),
    _ph('Curated by TRAGUIN Experts: Direct priority booking parameters for private luxury cruises to eliminate long boarding queues.', 10),
    _ph('Personalized Assistance: Elite, vetted local drivers and safety marshals specialized in hosting premium female groups.', 11),
    _ph('Exclusive Recommendations: Pre-arranged table reservations at the most highly rated hidden beachside cafes and live music lounges.', 12),
    _ph('Shopping & Local Experiences: Local Markets & Souvenirs: Authentic ocean pearls, beautifully polished coconut shell lamps, and rich wooden curios. Aberdeen Bazar in Port Blair is an exceptional place for unique sea-shell curios. Instagram Spots: Leaning palms of Radhanagar Beach and chic cafes of Havelock Island.', 13),
    _ph('Important Notes: Weather Considerations: Light cotton garments, sunscreen, hats, and reliable anti-slip beach footwear are highly advised. Ferry Operations: Cruise timings are subject to weather elements—in the rare event of ferry cancellation, TRAGUIN provides instant alternate arrangements. Advance Booking: Advanced booking of 45-60 days is highly recommended for luxury categories.', 14),
        ],
        moods=['Women', 'Luxury', 'Beach', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Bespoke Package)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Ladies Island Tour • Tropical Luxury for the Modern Woman • 05 Nights / 06 Days',
        overview='Welcome to an extraordinary tropical getaway crafted exclusively for women, proudly presented by TRAGUIN. This bespoke Ladies Getaway is conceptualized for those who seek to lose themselves in breathtaking landscapes, absolute security, and matchless island indulgence.\n\nTOUR OVERVIEW\nThis meticulously planned Female-Only itinerary presents the gold standard of island hospitality. From the moment you touch down in Port Blair, your safety, luxury, and peace of mind are managed entirely by our dedicated team. With a dedicated TRAGUIN curated experience note, you will enjoy unique touches like exclusive ladies-only beach side yoga sessions and private photography assistants.',
        seo_title='AN-008 | Ladies Island Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Ladies Island Tour (AN-008 / TRG-AND-008): Port Blair, Havelock Radhanagar Beach, Elephant Beach snorkeling, Neil Island Natural Bridge, and 4-tier handpicked accommodation for female travelers.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Cellular Jail National Memorial, Corbyn's Cove Beach, and Historic Sound & Light Show", 1),
    _ih('Premium cruise transfer and Radhanagar Beach sunset exploration', 2),
    _ih('Elephant Beach speedboat cruise and coral reef snorkeling session', 3),
    _ih('Natural Rock Bridge formation, Laxmanpur Beach Sunset, and Bharatpur Beach', 4),
    _ih("TRAGUIN Signature Experience: Private, secured beach side yoga and meditation circles for ladies' cohort", 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN PORT BLAIR — WELCOME TO THE EMERALD ISLANDS', ("Your premium Andaman experience officially begins at Port Blair Airport, where our professional female-friendly representative welcomes you with custom floral garlands. Transfer smoothly in a private luxury AC coach to your handpicked premium stay. In the afternoon, visit the historic Cellular Jail, followed by a spectacular private sunset view at Corbyn's Cove Beach. Conclude the day with a VIP seat at the legendary Sound and Light Show."), [
        "Sightseeing Included: Cellular Jail National Memorial, Corbyn's Cove Beach, Historic Sound & Light Show.",
        'Evening Experience: An elegant welcome dinner at a premium seaside deck curated by TRAGUIN experts.',
        'Overnight Stay: Port Blair (Premium Ocean-View Hotel)',
        'Meals Included: Welcome Drink & Sumptuous Buffet Breakfast',
    ]),
    _day(2, 'PORT BLAIR TO HAVELOCK ISLAND — SAILING TO PARADISE', ('Board a high-speed luxury private cruise (Nautika/Makruzz) in the premium class cabin towards Havelock Island. Upon arrival, check into an ultra-luxury beachfront resort. Late afternoon is reserved for Radhanagar Beach, a breathtaking landscape of smooth white sands and pristine blue surf.'), [
        'Sightseeing Included: Premium Cruise Transfer, Radhanagar Beach (Beach No. 7) sunset exploration.',
        'Optional Activities: Professional beachside sunset group photoshoot with a dedicated stylist.',
        'Overnight Stay: Havelock Island (Luxury Beachfront Villa Stay)',
        'Meals Included: Gourmet Breakfast',
    ]),
    _day(3, 'HAVELOCK ISLAND — UNDERWATER IMMERSION & CORAL GARDENS', ('An exhilarating day awaits at Elephant Beach, reached via a short, scenic speed-boat ride. Enjoy a complimentary session of snorkeling or try an optional sea-walk experience to walk amongst exotic tropical fish. Spend your afternoon relaxing at a premium beachside cafe.'), [
        'Sightseeing Included: Elephant Beach Speedboat Cruise, Coral Reef Snorkeling Session.',
        'Immersive Experiences: Guided marine interaction explaining the local coral restoration programs.',
        'Overnight Stay: Havelock Island (Luxury Beachfront Villa Stay)',
        'Meals Included: Gourmet Breakfast',
    ]),
    _day(4, 'HAVELOCK TO NEIL ISLAND — SERENITY & THE NATURAL BRIDGE', ('Take an early afternoon cruise to the quaint, idyllic paradise of Neil Island. Explore the unique Natural Coral Bridge, a magnificent geological marvel formed by ancient dead corals. Later, visit Laxmanpur Beach to watch the horizon turn into brilliant shades of amber and rose.'), [
        'Sightseeing Included: Natural Rock Bridge formation, Laxmanpur Beach Sunset, Bharatpur Beach.',
        'Evening Experience: Private beachside stargazing and storytelling circle with signature Mocktails.',
        'Overnight Stay: Neil Island (Premium Luxury Boutique Resort)',
        'Meals Included: Gourmet Breakfast',
    ]),
    _day(5, 'NEIL ISLAND TO PORT BLAIR — RETURN CRUISE & SOUVENIR SHOPPING', ('Catch a morning private cruise back to Port Blair. After checking back into your luxury city property, explore local culture and premium handicraft centers. Spend your afternoon selecting authentic shell jewelry, premium pearl items, and hand-carved padauk wood artifacts at Sagarika Government Emporium.'), [
        'Sightseeing Included: Sagarika Emporium, Local Spice plantations (optional), Anthropological Museum.',
        'Optional Activities: A fine-dining dinner experience overlooking the harbor waters.',
        'Overnight Stay: Port Blair (Premium Ocean-View Hotel)',
        'Meals Included: Gourmet Breakfast',
    ]),
    _day(6, 'PORT BLAIR — DEPARTURE', ('Indulge in your final lavish breakfast overlooking the tropical ocean. Your private luxury transport will pick you up and safely drop you to Port Blair Airport for your flight back home.'), [
        'Transfers Included: Private luxury airport transfer with assistance.',
        'Meals Included: Sumptuous Buffet Breakfast',
    ]),
        ],
        hotels=[
            _hotel('Hotel Sentinel / Peerless Resort', 'Port Blair', '02 Nights', 'Deluxe', 'Deluxe Room', 'CP Plus (Breakfast)', 4, 1, description='OPTION 01 – DELUXE: Hotel Sentinel / Peerless Resort (Port Blair, 02 Nights)'),
    _hotel('Symphony Palms Beach Resort', 'Havelock Island', '02 Nights', 'Deluxe', 'Deluxe Room', 'CP Plus (Breakfast)', 4, 2, description='OPTION 02 – DELUXE: Symphony Palms Beach Resort (Havelock Island, 02 Nights)'),
    _hotel('Summer Sands Beach Resort', 'Neil Island', '01 Night', 'Deluxe', 'Deluxe Room', 'CP Plus (Breakfast)', 4, 3, description='OPTION 03 – DELUXE: Summer Sands Beach Resort (Neil Island, 01 Night)'),
    _hotel('SeaShell Port Blair / similar', 'Port Blair', '02 Nights', 'Premium', 'Premium Room', 'CP Plus (Breakfast)', 4, 4, description='OPTION 04 – PREMIUM: SeaShell Port Blair / similar (Port Blair, 02 Nights)'),
    _hotel('Havelock Island Beach Resort', 'Havelock Island', '02 Nights', 'Premium', 'Premium Room', 'CP Plus (Breakfast)', 4, 5, description='OPTION 05 – PREMIUM: Havelock Island Beach Resort (Havelock Island, 02 Nights)'),
    _hotel('SeaShell Neil Island / similar', 'Neil Island', '01 Night', 'Premium', 'Premium Room', 'CP Plus (Breakfast)', 4, 6, description='OPTION 06 – PREMIUM: SeaShell Neil Island / similar (Neil Island, 01 Night)'),
    _hotel('Welcomhotel by ITC Bay Island', 'Port Blair', '02 Nights', 'Luxury', 'Luxury Room', 'CP Plus (Breakfast)', 5, 7, description='OPTION 07 – LUXURY: Welcomhotel by ITC Bay Island (Port Blair, 02 Nights)'),
    _hotel('Barefoot at Havelock / SeaShell', 'Havelock Island', '02 Nights', 'Luxury', 'Luxury Room', 'CP Plus (Breakfast)', 5, 8, description='OPTION 08 – LUXURY: Barefoot at Havelock / SeaShell (Havelock Island, 02 Nights)'),
    _hotel('Silver Sand Beach Resort', 'Neil Island', '01 Night', 'Luxury', 'Luxury Room', 'CP Plus (Breakfast)', 5, 9, description='OPTION 09 – LUXURY: Silver Sand Beach Resort (Neil Island, 01 Night)'),
    _hotel('Symphony Samudra (Pool Villa)', 'Port Blair', '02 Nights', 'Ultra Luxury', 'Pool Villa', 'CP Plus (Breakfast)', 5, 10, description='OPTION 10 – ULTRA LUXURY: Symphony Samudra (Pool Villa) (Port Blair, 02 Nights)'),
    _hotel('Taj Exotica Resort & Spa, Andamans', 'Havelock Island', '02 Nights', 'Ultra Luxury', 'Luxury Villa', 'CP Plus (Breakfast)', 5, 11, description='OPTION 11 – ULTRA LUXURY: Taj Exotica Resort & Spa, Andamans (Havelock Island, 02 Nights)'),
    _hotel('Tilar Siro Neil Island (CGH Earth)', 'Neil Island', '01 Night', 'Ultra Luxury', 'Luxury Suite', 'CP Plus (Breakfast)', 5, 12, description='OPTION 12 – ULTRA LUXURY: Tilar Siro Neil Island (CGH Earth) (Neil Island, 01 Night)'),
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Standard/Villa options across handpicked beachfront hotels.', 1),
    _inc_included('Private Cruise Tickets: High-speed luxury cruise transfers in Premium Class.', 2),
    _inc_included('Luxury Transportation: Private air-conditioned luxury vehicle for transfers & sightseeing.', 3),
    _inc_included('TRAGUIN Support: Dedicated female guest assistance manager and 24/7 helpline.', 4),
    _inc_included('Welcome Amenities: Personalized travel kit, floral welcome, and island maps.', 5),
    _inc_included('Complimentary Experience: One special introductory snorkeling session at Elephant Beach.', 6),
    _inc_excluded('Domestic/International airfare to Port Blair.', 7),
    _inc_excluded('Optional water sports (Scuba Diving, Sea Walking, Jet Skiing).', 8),
    _inc_excluded('Personal expenses such as bar bills, phone calls, laundry, and tips.', 9),
    _inc_excluded('Any additional meals or beverages not stated under the meal plan.', 10),
        ],
    )
    return package, itinerary

def build_an_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AN-009'
    tour_code = 'TRG-AND-009'
    title = 'Leisure Andaman'
    duration = '06 Nights / 07 Days'
    slug = 'an-009-leisure-andaman'
    itin_slug = 'an-009-leisure-andaman-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code AN-009 | TRAGUIN tour code TRG-AND-009', 1),
    _ph('State / Country: Andaman & Nicobar Islands, India | Category: Senior Citizen Leisure & Luxury', 2),
    _ph('Destinations: Port Blair (3N) • Havelock Island (2N) • Neil Island (1N)', 3),
    _ph('Ideal for: Senior Citizens, Relaxed Pace Travelers & Luxury Leisure Seekers', 4),
    _ph('Best season: October to May (Tropical Bliss)', 5),
    _ph('Starting price: On Request (Premium Bespoke Package)', 6),
    _ph('Vehicle & Meals: Private Luxury AC Vehicle / MAPAI (Breakfast & Gourmet Dinner)', 7),
    _ph('Route: Port Blair (3N) → Havelock Island (2N) → Neil Island (1N) → Port Blair → Departure', 8),
    _ph('TRAGUIN Signature Experience: Private luggage porterage at all ferry terminals, ensuring a completely hands-free journey for seniors.', 9),
    _ph('Curated by TRAGUIN Experts: Carefully timed ferry schedules that avoid early morning rush hours, prioritizing your comfort.', 10),
    _ph('Personalized Assistance: A dedicated tour coordinator at every island dock to ensure comfortable embarkation and disembarkation.', 11),
    _ph('Exclusive Recommendations: Access to quiet, senior-accessible ocean-view viewpoints perfect for beautiful landscape photography.', 12),
    _ph('Shopping & Local Experiences: Sagarika Emporium: Premium hand-carved mother-of-pearl jewelry, authentic sea-shell artifacts, and fine local wooden handicrafts. Island Cafes: Organic coconut water elixirs, artisan single-origin coffees, and exquisite global baking selections at top beachfront cafes.', 13),
    _ph('Important Notes: Ferry Operations: Catamaran sailings are subject to weather conditions—TRAGUIN will coordinate alternative travel arrangements smoothly. Luggage Rules: Ferries allow up to 25kg of checked baggage per passenger with transit handling assistance. Advance Bookings: We highly recommend booking 45–60 days in advance to secure the finest premium catamaran seating classes.', 14),
        ],
        moods=['Senior', 'Leisure', 'Luxury', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Bespoke Package)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Leisure Andaman • An Oasis of Serenity and Absolute Comfort • 06 Nights / 07 Days',
        overview='Welcome to an unforgettable escape uniquely curated by TRAGUIN. Designed specifically as a senior citizen leisure holiday, this bespoke itinerary invites you to witness the breathtaking landscapes, calm turquoise waters, and powdery white sands of the Andaman islands at an ease-filled, leisurely pace.\n\nTOUR OVERVIEW\nThis elite Luxury Andaman Holiday proposal offers a masterfully relaxed routing crafted with senior travelers in mind, avoiding rushed transfers or physically strenuous paths. Your journey features private luxury AC vehicles for all transfers, priority boarding across premium catamaran ferries, and dedicated physical assistance at every dock.',
        seo_title='AN-009 | Leisure Andaman Senior Tour | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Leisure Andaman package (AN-009 / TRG-AND-009): Senior-friendly pacing, Radhanagar Beach, Kalapathar Beach, Neil Island Natural Bridge, Ross Island golf cart, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Cellular Jail National Memorial and Historic Light & Sound Show with VIP seating', 1),
    _ih('Radhanagar Beach scenic catamaran cruise and forest road drive', 2),
    _ih('Kalapathar Beach viewpoint and coastal village plantation drive', 3),
    _ih('Laxmanpur Beach Natural Coral Archway and Bharatpur Beach glass-bottom boat', 4),
    _ih('Ross Island Heritage Ruins with complimentary private golf cart ride for seniors', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN PORT BLAIR — EMERALD LANDFALL & COLONIAL MEMORIES', ('Your premium Andaman experience begins as your flight lands at Veer Savarkar International Airport in Port Blair. A dedicated TRAGUIN guest experience executive will receive you with personalized placards and fresh floral welcomes, escorting you in a private luxury transport vehicle directly to your handpicked premium resort. Enjoy an elegant visit to the National Memorial Cellular Jail followed by VIP reserved seats for the emotionally moving Sound and Light Show.'), [
        'Sightseeing Included: Cellular Jail National Memorial, Historic Light & Sound Show.',
        'Evening Experience: VIP reserved seating for the sound show followed by a welcome dinner curated by TRAGUIN experts.',
        'Overnight Stay: Port Blair (Premium Ocean-View Resort)',
        'Meals Included: Welcome Drink & Gourmet Dinner',
    ]),
    _day(2, 'PORT BLAIR TO HAVELOCK ISLAND — CRUISING THE AZURE WATER', ('Savor an early premium breakfast before heading to the Phoenix Bay Jetty. Board your luxury private catamaran (Makruzz / Nautika in Premium Royal Class) for a silky-smooth cruise to Havelock Island. In the late afternoon, your chauffeur will drive you to the world-famous Radhanagar Beach (Beach No. 7) for a curated high-tea experience as you watch a breathtaking sunset.'), [
        'Sightseeing Included: Radhanagar Beach, Scenic Catamaran Cruise, Forest Road Drive.',
        'Optional Activities: Professional beachfront sunset family portrait photography session.',
        'Overnight Stay: Havelock Island (Premium Luxury Beachfront Villa)',
        'Meals Included: Premium Breakfast & Luxury Resort Dinner',
    ]),
    _day(3, 'HAVELOCK ISLAND — POWDERY SANDS & EXCLUSIVE LAGOON LEISURE', ("Today features a highly relaxed, immersive experience at Elephant Beach or Kalapathar Beach, based entirely on your personal comfort preference. Kalapathar Beach offers a stunning, serene setting where black rocks contrast beautifully against brilliant aqua waters. Spend your afternoon reading under native shade trees or indulging in a premium traditional Ayurvedic massage at your resort's luxury wellness center."), [
        'Sightseeing Included: Kalapathar Beach Viewpoint, Coastal Village Plantation Drive.',
        'Evening Experience: Private candlelit dinner overlooking the ocean with a customized menu.',
        'Overnight Stay: Havelock Island (Premium Luxury Beachfront Villa)',
        "Meals Included: Breakfast & Chef's Special Seafood / Vegetarian Dinner",
    ]),
    _day(4, 'HAVELOCK ISLAND TO NEIL ISLAND — TRANSITION TO RUSTIC TRANQUILITY', ('Following a leisurely breakfast, board a premium mid-day catamaran cruise connecting you to the peaceful shores of Neil Island. In the afternoon, visit Laxmanpur Beach to view its famous natural limestone arch structure (Howrah Bridge). The walk is flat, easily accessible, and perfectly managed by your private guide.'), [
        'Sightseeing Included: Laxmanpur Beach, Natural Coral Archway, Inter-Island Catamaran Voyage.',
        'Evening Experience: Stargazing on the open resort deck with premium mocktails and light live music.',
        'Overnight Stay: Neil Island (Luxury Boutique Eco-Resort)',
        'Meals Included: Breakfast & Multi-cuisine Fusion Dinner',
    ]),
    _day(5, 'NEIL ISLAND TO PORT BLAIR — SERENE AQUAMARINE LAGOONS', ('Start your morning with a gentle visit to Bharatpur Beach, celebrated for its calm, crystal-clear lagoon waters. Senior travelers can enjoy a relaxed private glass-bottom boat ride here, viewing vibrant live corals and colorful tropical fish without ever having to step into the water. After lunch, cruise back via premium catamaran to Port Blair.'), [
        'Sightseeing Included: Bharatpur Beach, Sagarika Government Handicraft Emporium.',
        'Optional Activities: Private Glass-Bottom Eco-Boat Tour over the shallow reefs.',
        'Overnight Stay: Port Blair (Premium Ocean-View Resort)',
        'Meals Included: Breakfast & Traditional Continental Dinner',
    ]),
    _day(6, 'PORT BLAIR — EXCURSION TO ROSS ISLAND', ("After breakfast, take a brief and highly comfortable 15-minute private speed boat ride to Ross Island, the former British administrative capital. Today, the island presents an enchanting sight, with historic colonial ruins gracefully intertwined with the roots of ancient banyan trees. To ensure absolute comfort for our senior guests, a private battery-operated golf cart will guide you effortlessly along the island's flat paved pathways."), [
        'Sightseeing Included: Ross Island Heritage Ruins, British Era Artifact Trails.',
        'Evening Experience: Grand farewell buffet dinner with specialized menu items curated by the chef.',
        'Overnight Stay: Port Blair (Premium Ocean-View Resort)',
        'Meals Included: Breakfast & Premium Farewell Dinner',
    ]),
    _day(7, 'DEPARTURE FROM PORT BLAIR — CREATING MEMORIES BEYOND DESTINATIONS', ('Enjoy your final lavish tropical breakfast overlooking the ocean. Your private luxury transport will pick you up from the resort lobby and transfer you seamlessly to Veer Savarkar International Airport for your flight home.'), [
        'Transfers Included: Private airport departure drop-off service.',
        'Meals Included: Sumptuous Buffet Breakfast',
    ]),
        ],
        hotels=[
            _hotel('Hotel Sentinel / Peerless Resort', 'Port Blair', '03 Nights', 'Deluxe', 'Deluxe Room', 'MAPAI (Breakfast & Dinner)', 4, 1, description='OPTION 01 – DELUXE: Hotel Sentinel / Peerless Resort (Port Blair, 03 Nights)'),
    _hotel('Symphony Palms Beach Resort', 'Havelock Island', '02 Nights', 'Deluxe', 'Deluxe Room', 'MAPAI (Breakfast & Dinner)', 4, 2, description='OPTION 02 – DELUXE: Symphony Palms Beach Resort (Havelock Island, 02 Nights)'),
    _hotel('Pearl Park Beach Resort', 'Neil Island', '01 Night', 'Deluxe', 'Deluxe Room', 'MAPAI (Breakfast & Dinner)', 4, 3, description='OPTION 03 – DELUXE: Pearl Park Beach Resort (Neil Island, 01 Night)'),
    _hotel('SeaShell Port Blair / similar', 'Port Blair', '03 Nights', 'Premium', 'Premium Room', 'MAPAI (Breakfast & Dinner)', 4, 4, description='OPTION 04 – PREMIUM: SeaShell Port Blair / similar (Port Blair, 03 Nights)'),
    _hotel('SeaShell Havelock / Silver Sand', 'Havelock Island', '02 Nights', 'Premium', 'Premium Room', 'MAPAI (Breakfast & Dinner)', 4, 5, description='OPTION 05 – PREMIUM: SeaShell Havelock / Silver Sand (Havelock Island, 02 Nights)'),
    _hotel('SeaShell Neil / Silver Sand Neil', 'Neil Island', '01 Night', 'Premium', 'Premium Room', 'MAPAI (Breakfast & Dinner)', 4, 6, description='OPTION 06 – PREMIUM: SeaShell Neil / Silver Sand Neil (Neil Island, 01 Night)'),
    _hotel('Welcomhotel by ITC Bay Island', 'Port Blair', '03 Nights', 'Luxury', 'Luxury Room', 'MAPAI (Breakfast & Dinner)', 5, 7, description='OPTION 07 – LUXURY: Welcomhotel by ITC Bay Island (Port Blair, 03 Nights)'),
    _hotel('Barefoot at Havelock / Symphony Samudra', 'Havelock Island', '02 Nights', 'Luxury', 'Luxury Room', 'MAPAI (Breakfast & Dinner)', 5, 8, description='OPTION 08 – LUXURY: Barefoot at Havelock / Symphony Samudra (Havelock Island, 02 Nights)'),
    _hotel('Summer Sands Beach Resort (Suite)', 'Neil Island', '01 Night', 'Luxury', 'Suite', 'MAPAI (Breakfast & Dinner)', 5, 9, description='OPTION 09 – LUXURY: Summer Sands Beach Resort (Suite) (Neil Island, 01 Night)'),
    _hotel('Taj Exotica Resort & Spa (Port Blair Suite)', 'Port Blair', '03 Nights', 'Ultra Luxury', 'Suite', 'MAPAI (Breakfast & Dinner)', 5, 10, description='OPTION 10 – ULTRA LUXURY: Taj Exotica Resort & Spa (Port Blair Suite) (Port Blair, 03 Nights)'),
    _hotel('Taj Exotica Resort & Spa, Radhanagar', 'Havelock Island', '02 Nights', 'Ultra Luxury', 'Luxury Villa', 'MAPAI (Breakfast & Dinner)', 5, 11, description='OPTION 11 – ULTRA LUXURY: Taj Exotica Resort & Spa, Radhanagar (Havelock Island, 02 Nights)'),
    _hotel('Tilar Siro Andaman (Luxury Villa)', 'Neil Island', '01 Night', 'Ultra Luxury', 'Luxury Villa', 'MAPAI (Breakfast & Dinner)', 5, 12, description='OPTION 12 – ULTRA LUXURY: Tilar Siro Andaman (Luxury Villa) (Neil Island, 01 Night)'),
        ],
        inclusions=[
            _inc_included('Premium Stays: Handpicked senior-friendly luxury resort rooms.', 1),
    _inc_included('Luxury Transportation: Private AC luxury vehicle for transfers & sightseeing.', 2),
    _inc_included('Premium Cruise Tickets: High-speed private luxury catamaran seats.', 3),
    _inc_included('Curated Meal Plan: Daily lavish breakfasts & gourmet multi-course dinners.', 4),
    _inc_included('TRAGUIN Support: 24/7 on-ground assistance and dedicated baggage handlers.', 5),
    _inc_included('Golf Cart Service: Complimentary private golf cart ride on Ross Island.', 6),
    _inc_excluded('Domestic or International Airfare tickets to Port Blair.', 7),
    _inc_excluded('Optional adventure sports (Scuba Diving, Sea Walking, Snorkeling).', 8),
    _inc_excluded('Personal expenses such as room service, laundry, premium alcohol, and tips.', 9),
    _inc_excluded('Travel Insurance policies or medical evacuation costs.', 10),
        ],
    )
    return package, itinerary

def build_an_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AN-010'
    tour_code = 'TRG-AND-010'
    title = 'Complete Andaman'
    duration = '08 Nights / 09 Days'
    slug = 'an-010-complete-andaman'
    itin_slug = 'an-010-complete-andaman-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code AN-010 | TRAGUIN tour code TRG-AND-010', 1),
    _ph('State / Country: Andaman & Nicobar Islands, India | Category: Complete Andaman Premium Family Tour', 2),
    _ph('Destinations: Port Blair (4N) • Havelock Island (2N) • Neil Island (2N) • Baratang Island (Day Trip)', 3),
    _ph('Ideal for: Family Getaways, Honeymooners, Beach Lovers & Luxury Seekers', 4),
    _ph('Best season: October to May', 5),
    _ph('Starting price: On Request (Premium Customised)', 6),
    _ph('Vehicle & Meals: Private Luxury AC Vehicle & Private Cruise / MAPAI (Breakfast & Dinner)', 7),
    _ph('Route: Port Blair (4N) → Havelock Island (2N) → Neil Island (2N) → Baratang Day Trip → Port Blair → Departure', 8),
    _ph('TRAGUIN Signature Experience: Private luggage porterage and priority boarding lanes across cruise terminals.', 9),
    _ph('Curated by TRAGUIN Experts: Custom-timed departures designed to completely avoid peak tourist crowds at beaches.', 10),
    _ph('Luxury Transportation: Premium air-conditioned luxury fleet with local bilingual expert drivers.', 11),
    _ph('Exclusive Recommendations: Handpicked selections for premium evening lounges, beach clubs, and dining spots.', 12),
    _ph('Shopping & Local Experiences: Local Markets: Explore Aberdeen Bazaar and the Sagarika Emporium in Port Blair. Famous Shopping Items: Elegant South Sea pearls, mother-of-pearl artifacts, handmade coconut shell jewelry, and aromatic spice selections.', 13),
    _ph('Important Notes: Hotel Policies: Island hotels enforce strict check-in at 12:00 PM and check-out at 09:00 AM due to scheduled cruise timings. Weather Notes: Activities are subject to dynamic weather conditions and port authority safety permissions. Advance Booking Suggestions: Cruise seats and premium beachfront properties fill quickly; we advise booking 45–60 days in advance.', 14),
        ],
        moods=['Family', 'Luxury', 'Complete', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Complete Andaman • Tropical Paradise Unleashed • 08 Nights / 09 Days',
        overview="Welcome to an extraordinary tropical getaway crafted meticulously by TRAGUIN. Experience the ultimate Andaman Family Tour designed to show you breathtaking landscapes, pristine turquoise waters, and untouched white-sand shorelines.\n\nTOUR OVERVIEW\nThis bespoke 8-Night / 9-Day itinerary offers a complete exploration of the Bay of Bengal's most majestic jewels. Your family will enjoy private, air-conditioned road transfers and high-speed luxury catamaran cruise journeys between islands. Benefit from TRAGUIN curated experiences including skip-the-line cruise boarding, personalized dock assistance, and expertly guided sightseeing tours.",
        seo_title='AN-010 | Complete Andaman Tour | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days Complete Andaman package (AN-010 / TRG-AND-010): Port Blair, Havelock Radhanagar Beach, Elephant Beach, Neil Island Natural Bridge, Baratang Limestone Caves, Ross Island, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Cellular Jail National Memorial, Light & Sound Show, and Chidiyatapu Sunset Point', 1),
    _ih('Premium cruise transfer and Radhanagar Beach (Beach No. 7) exploration', 2),
    _ih('Elephant Beach speedboat cruise, live coral reef viewing, and snorkeling', 3),
    _ih('Neil Island Natural Rock Bridge eco-walk and inter-island premium cruise', 4),
    _ih('Baratang mangrove canopy boat safari, Limestone Caves, and Ross Island heritage walk', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN PORT BLAIR & CELLULAR JAIL — HISTORIC CHRONICLES & CHIDIYATAPU SUNSET', ('Your premium Andaman experience starts with a warm welcome at Veer Savarkar International Airport in Port Blair by our dedicated local representative. Transfer smoothly to your luxury sea-facing hotel in a private AC vehicle. After lunch, take an emotional tour of the historic Cellular Jail. Later, drive along a pristine coastline to Chidiyatapu for magnificent sunset views. Wrap up your evening with a VIP pass to the moving Light and Sound Show inside the Cellular Jail.'), [
        'Sightseeing Included: Cellular Jail National Memorial, Light & Sound Show, Chidiyatapu Sunset Point.',
        'Evening Experience: Reserved lounge seating for the historical light and sound production.',
        'Overnight Stay: Port Blair (Premium Luxury Sea-View Resort)',
        'Meals Included: Welcome Drink & Gourmet Dinner',
    ]),
    _day(2, 'PORT BLAIR TO HAVELOCK ISLAND BY LUXURY CRUISE — CRUISING INTO AZURE WATERS', ('Board a premium high-speed luxury cruise (Nautika / Makruzz) from Haddo Wharf for a scenic voyage across the cerulean sea to Havelock Island (Swaraj Dweep). Upon docking, proceed to your ultra-luxury beachfront villa resort. In the afternoon, head out to the iconic Radhanagar Beach, universally celebrated as one of the top tourist places in Andaman.'), [
        'Sightseeing Included: Premium Cruise Transfer, Radhanagar Beach (Beach No. 7) Exploration.',
        'Evening Experience: Exclusive private family beachside dinner setup organized by TRAGUIN experts.',
        'Overnight Stay: Havelock Island (Luxury Beachfront Resort)',
        'Meals Included: Buffet Breakfast & Beachfront Dinner',
    ]),
    _day(3, 'ELEPHANT BEACH AQUATIC ADVENTURE — CORAL REEF DISCOVERY', ("Embark on a private speed-boat charter heading out to Elephant Beach, the island's ultimate adventure hub. Enjoy a complimentary snorkeling session, or choose to try sea-walking and scuba diving. Return to your resort in the afternoon to unwind by the pool or enjoy a premium luxury spa therapy session."), [
        'Sightseeing Included: Elephant Beach Speedboat Cruise, Live Coral Reef Viewing, Snorkeling.',
        'Optional Activities: PADI Discover Scuba Diving, Undersea Sea Walk, Parasailing.',
        'Overnight Stay: Havelock Island (Luxury Beachfront Resort)',
        'Meals Included: Premium Breakfast & Multi-Cuisine Dinner',
    ]),
    _day(4, 'HAVELOCK ISLAND TO NEIL ISLAND — SHAHEED DWEEP TRANQUILITY', ('Check out from your hotel and step onto a luxury inter-island catamaran cruise bound for Neil Island (Shaheed Dweep). Check into your boutique luxury bungalow resort. Spend your afternoon relaxing at Bharatpur Beach before heading over to Laxmanpur Beach to witness a magnificent sunset view.'), [
        'Sightseeing Included: Inter-Island Premium Cruise, Bharatpur Beach, Laxmanpur Sunset Beach.',
        'Evening Experience: Stargazing stroll along the tranquil, private sands of Laxmanpur.',
        'Overnight Stay: Neil Island (Premium Boutique Resort)',
        "Meals Included: Breakfast & Chef's Special Seafood/Vegetarian Dinner",
    ]),
    _day(5, 'NEIL ISLAND NATURAL BRIDGE TO PORT BLAIR — GEOLOGICAL MARVELS', ('Wake up early to catch the low tide at Laxmanpur Beach No. 2, home to the famous Natural Coral Bridge. This remarkable geological formation is a highly popular Instagram location, decorated with live sea anemones, starfish, and tiny crabs in natural rock pools. Later, check out and board your afternoon luxury cruise back to Port Blair.'), [
        'Sightseeing Included: Natural Rock Bridge Eco-Walk, Return High-Speed Cruise to Port Blair.',
        'Optional Activities: Glass-bottom boat ride over the outer reefs of Neil Island.',
        'Overnight Stay: Port Blair (Premium Hilltop or Sea-View Hotel)',
        'Meals Included: Breakfast & Elegant Buffet Dinner',
    ]),
    _day(6, 'BARATANG ISLAND DAY EXCURSION — MANGROVE CREEK SAFARI & LIMESTONE CAVES', ('Set out on an exciting early-morning road expedition to Baratang Island, traveling through the dense Andaman tropical rain forests. Board a private speed boat for an incredible safari through thick, winding mangrove creeks. Trek through rural tropical trails to reach the ancient Limestone Caves, filled with massive stalactites and stalagmites formed over millions of years.'), [
        'Sightseeing Included: Baratang Rainforest Drive, Mangrove Canopy Boat Safari, Limestone Caves.',
        'Food Suggestion: Taste delicious, traditional coastal curries at an authentic local island diner.',
        'Overnight Stay: Port Blair (Premium Hilltop or Sea-View Hotel)',
        'Meals Included: Packed Early Breakfast & Luxury Dinner',
    ]),
    _day(7, 'ROSS ISLAND — BRITISH COLONIAL RUINS & PLAYFUL WILD DEER', ("Board a private ferry for a short ride to Ross Island, the historic capital of the British administration. Walk among evocative colonial ruins, including a grand old church, ballroom, and chief commissioner's house, now wrapped in giant banyan tree roots. The island features tame deer roaming freely, making it a wonderful experience for a family vacation."), [
        'Sightseeing Included: Ross Island Heritage Walk, British Historical Ruins, Deer Sanctuary.',
        'Evening Experience: Relaxing evening high-tea at a premium harbor-view bistro.',
        'Overnight Stay: Port Blair (Premium Hilltop or Sea-View Hotel)',
        'Meals Included: Breakfast & International Cuisine Dinner',
    ]),
    _day(8, "PORT BLAIR CITY TOUR & CORBYN'S COVE — CULTURAL EXPLORATION", ("Enjoy a complete city tour of Port Blair, beginning with the Anthropological Museum to learn about the deep-rooted heritage of the indigenous Andaman tribes. Visit the Samudrika Naval Marine Museum, followed by a scenic drive to Corbyn's Cove Beach, a beautiful crescent-shaped shore lined with tall coconut palms. Spend your final evening shopping for authentic pearls and local wood handicrafts."), [
        "Sightseeing Included: Anthropological Museum, Samudrika Marine Museum, Corbyn's Cove Beach.",
        'Shopping Highlights: Sagarika Government Emporium for exquisite pearl jewelry and shell crafts.',
        'Overnight Stay: Port Blair (Premium Luxury Stay)',
        'Meals Included: Breakfast & Farewell Premium Gala Dinner',
    ]),
    _day(9, 'DEPARTURE FROM PORT BLAIR — CREATING MEMORIES BEYOND DESTINATIONS', ('Indulge in a final lavish breakfast looking out over the blue waters of the Bay of Bengal. Your private luxury transport will pick you up from your resort and transfer you safely to Veer Savarkar International Airport for your flight home.'), [
        'Transfers Included: Private luxury airport departure transfer.',
        'Meals Included: Sumptuous Buffet Breakfast',
    ]),
        ],
        hotels=[
            _hotel('Hotel Shompen / Sea Shell Pride', 'Port Blair', '04 Nights', 'Deluxe', 'Deluxe Room', 'MAPAI (Breakfast & Dinner)', 4, 1, description='OPTION 01 – DELUXE: Hotel Shompen / Sea Shell Pride (Port Blair, 04 Nights)'),
    _hotel('Symphony Palms Beach Resort', 'Havelock Island', '02 Nights', 'Deluxe', 'Deluxe Room', 'MAPAI (Breakfast & Dinner)', 4, 2, description='OPTION 02 – DELUXE: Symphony Palms Beach Resort (Havelock Island, 02 Nights)'),
    _hotel('Summer Sands Beach Resort', 'Neil Island', '02 Nights', 'Deluxe', 'Deluxe Room', 'MAPAI (Breakfast & Dinner)', 4, 3, description='OPTION 03 – DELUXE: Summer Sands Beach Resort (Neil Island, 02 Nights)'),
    _hotel('Peerless Resort / Lemon Tree', 'Port Blair', '04 Nights', 'Premium', 'Premium Room', 'MAPAI (Breakfast & Dinner)', 4, 4, description='OPTION 04 – PREMIUM: Peerless Resort / Lemon Tree (Port Blair, 04 Nights)'),
    _hotel('Havelock Island Beach Resort', 'Havelock Island', '02 Nights', 'Premium', 'Premium Room', 'MAPAI (Breakfast & Dinner)', 4, 5, description='OPTION 05 – PREMIUM: Havelock Island Beach Resort (Havelock Island, 02 Nights)'),
    _hotel('Silver Sand Beach Resort', 'Neil Island', '02 Nights', 'Premium', 'Premium Room', 'MAPAI (Breakfast & Dinner)', 4, 6, description='OPTION 06 – PREMIUM: Silver Sand Beach Resort (Neil Island, 02 Nights)'),
    _hotel('SeaShell Port Blair / Welcomhotel', 'Port Blair', '04 Nights', 'Luxury', 'Luxury Room', 'MAPAI (Breakfast & Dinner)', 5, 7, description='OPTION 07 – LUXURY: SeaShell Port Blair / Welcomhotel (Port Blair, 04 Nights)'),
    _hotel('SeaShell Havelock / Barefoot', 'Havelock Island', '02 Nights', 'Luxury', 'Luxury Room', 'MAPAI (Breakfast & Dinner)', 5, 8, description='OPTION 08 – LUXURY: SeaShell Havelock / Barefoot (Havelock Island, 02 Nights)'),
    _hotel('SeaShell Neil / Symphony Samudra', 'Neil Island', '02 Nights', 'Luxury', 'Luxury Room', 'MAPAI (Breakfast & Dinner)', 5, 9, description='OPTION 09 – LUXURY: SeaShell Neil / Symphony Samudra (Neil Island, 02 Nights)'),
    _hotel('Symphony Samudra (Pool Villa)', 'Port Blair', '04 Nights', 'Ultra Luxury', 'Pool Villa', 'MAPAI (Breakfast & Dinner)', 5, 10, description='OPTION 10 – ULTRA LUXURY: Symphony Samudra (Pool Villa) (Port Blair, 04 Nights)'),
    _hotel('Taj Exotica Resort & Spa (Villa)', 'Havelock Island', '02 Nights', 'Ultra Luxury', 'Luxury Villa', 'MAPAI (Breakfast & Dinner)', 5, 11, description='OPTION 11 – ULTRA LUXURY: Taj Exotica Resort & Spa (Villa) (Havelock Island, 02 Nights)'),
    _hotel('Tilar Siro Neil Island (Luxury Suite)', 'Neil Island', '02 Nights', 'Ultra Luxury', 'Luxury Suite', 'MAPAI (Breakfast & Dinner)', 5, 12, description='OPTION 12 – ULTRA LUXURY: Tilar Siro Neil Island (Luxury Suite) (Neil Island, 02 Nights)'),
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Handpicked hotels as per chosen luxury tier.', 1),
    _inc_included('Luxury Transfers: High-speed luxury catamaran cruise tickets (Private Class).', 2),
    _inc_included('Curated Meal Plan: Daily lavish breakfasts and elite multi-cuisine dinners (MAPAI).', 3),
    _inc_included('TRAGUIN Support: 24/7 dedicated on-ground coordinator & priority assistance.', 4),
    _inc_included('Welcome Amenities: Refreshments upon arrival, shell garlands, and customized travel map.', 5),
    _inc_included('Complimentary Experience: 1 Snorkeling session per person at Elephant Beach.', 6),
    _inc_excluded('Airfare or entry seaport tickets to Port Blair.', 7),
    _inc_excluded('Optional scuba diving, sea walk, or custom water sports.', 8),
    _inc_excluded('Personal items, laundry, room service tips, and drinks.', 9),
    _inc_excluded('Camera entrance fees at monument sites.', 10),
        ],
    )
    return package, itinerary

ANDAMAN_DOMESTIC_BUILDERS = [
    build_an_001,
    build_an_002,
    build_an_003,
    build_an_004,
    build_an_005,
    build_an_006,
    build_an_007,
    build_an_008,
    build_an_009,
    build_an_010,
]
