"""Builder functions for TH-002 through TH-040 Thailand international domestic packages."""

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

THAILAND_SLUG = "thailand"


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


def build_th_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-002'
    tour_code = 'TRG-BKK-PAT-2026'
    title = 'BANGKOK PATTAYA FAMILY TOUR Bangkok • Grand Palace • Pattaya Beach • Coral Island • Cultural Immersion'
    duration = '04 Nights / 05 Days'
    slug = 'th-002-bangkok-pattaya-family-tour-bangkok-grand-palace-pattaya-beach-coral-island-cultural-immersion'
    itin_slug = 'th-002-bangkok-pattaya-family-tour-bangkok-grand-palace-pattaya-beach-coral-island-cultural-immersion-itinerary'
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
            _ph('Serial code TH-002 | TRAGUIN tour code TRG-BKK-PAT-2026', 1),
            _ph('State / Country: Thailand | Category: Best Bangkok Pattaya Family Tour', 2),
            _ph('Destinations: Bangkok (2 Nights) + Pattaya (2 Nights)', 3),
            _ph('Ideal for: Families, Multi- generational Groups, First-Time Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Executive Van / Buffet Breakfast (CP), Selected Lunches & Fine Dinners', 7)
        ],
        moods=['Family', 'Culture', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='BANGKOK PATTAYA FAMILY TOUR Bangkok',
        overview="Bangkok • Grand Palace • Pattaya Beach • Coral Island • Cultural Immersion 04 Nights / 05 Days Classic Thailand Family Holiday SERIAL CODE: TH-002 TRAGUIN TOUR CODE: TRG-BKK-PAT-2026 STATE / COUNTRY: Thailand CATEGORY: Best Bangkok Pattaya Family Tour DURATION: 04 Nights / 05 Days DESTINATIONS COVERED: Bangkok (2 Nights) + Pattaya (2 Nights) IDEAL FOR: Families, Multi- generational Groups, First-Time Travelers BEST SEASON: November to April VEHICLE TYPE: Private Luxury Executive Van MEAL PLAN: Buffet Breakfast (CP), Selected Lunches & Fine Dinners Create lifelong bonds with the Best Bangkok Pattaya Tour Package, expertly crafted by TRAGUIN to combine iconic metropolitan heritage with serene coastal joy. This spectacular Family Tour offers a perfect balance of comfort, culture, and coastal adventure, promising breathtaking landscapes and unforgettable memories for all ages.\n\nTOUR OVERVIEW\nWelcome to your optimized Bangkok Pattaya Classic family holiday, a masterfully structured journey designed to showcase the vibrant heart of Thailand. Across 5 spectacular days, your family will explore iconic temples, bustling markets, and pristine coral islands, all supported by TRAGUIN's signature premium logistics. TRAGUIN Curated Experience Note: We ensure absolute perfection at every milestone. From pre-allocated VIP airport fast-track arrivals and spacious luxury family vans to pre-vetted fine dining and children-friendly leisure paths, our on-ground concierge team manages every detail of your trip 24/7.\n\nWHY CHOOSE OUR BANGKOK PATTAYA FAMILY TOUR?\nBangkok and Pattaya represent the absolute gold standard for family travel in Thailand, effortlessly pairing urban royal heritage with pristine tropical coastal sanctuaries. Opting for a signature TRAGUIN Thailand Package guarantees access to exclusive benefits. This proposal integrates top searched tourism keywords for Google ranking, showcasing an elite layout of premier Thailand Sightseeing wonders. Explore Top Tourist Places in Thailand: the golden spires of Bangkok’s Grand Palace, the crystal-blue waters of Coral Island, and the vibrant culture of local night bazaars. It is widely recognized as the Best Time to Visit Thailand to capture iconic photography points, try authentic local cuisine, and indulge in a truly Premium Thailand Experience. TRAGUIN Family Signatures: Private guided tours of the Grand Palace, exclusive speedboat charter to Coral Island, front-row premium seating at cultural shows, and dedicated luxury van transfers throughout your stay. THE DEFINITIVE DAY-WISE ITINERARY",
        seo_title='TH-002 | BANGKOK PATTAYA FAMILY TOUR Bangkok | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Thailand package (TH-002 / TRG-BKK-PAT-2026): Bangkok (2 Nights) + Pattaya (2 Nights) with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: BANGKOK ARRIVAL & SUNSET ORIENTATION', 1),
            _ih('Day 02: BANGKOK HERITAGE & ICONIC TEMPLES', 2),
            _ih('Day 03: BANGKOK TO PATTAYA COASTAL ESCAPE', 3),
            _ih('Day 04: CORAL ISLAND MARINE EXPEDITION', 4),
            _ih('Day 05: DEPARTURE & CHERISHING MEMORIES', 5)
        ],
        days=[
            _day(
                1,
                'BANGKOK ARRIVAL & SUNSET ORIENTATION',
                (
                    'CITY OF ANGELS WELCOME – LUXURY TRANSIT TO YOUR COASTAL-READY BASE Your spectacular Thailand Family Tour begins the moment your family arrives at Bangkok’s Suvarnabhumi International Airport. Receive our VIP Fast-Track Reception, clearing all customs procedures within minutes. Your private, elegant luxury van waits to transfer your party smoothly to your ultra-luxury city hotel. Check into your spacious family suite. In the afternoon, take a brief, gentle city orientation drive, capturing beautiful photography points of the urban metropolis before settling in for a curated welcome dinner. This sets the stage for an unforgettable vacation. Sightseeing Included: VIP airport fast-track reception, panoramic city orientation drive. Evening Experience: Relaxed family welcome dinner featuring authentic international cuisine.'
                ),
                [
                    'Overnight Stay: Bangkok (Premium Family-Friendly Luxury Hotel)',
                    'Meals Included: Curated International Welcome Dinner',
                ],
            ),
            _day(
                2,
                'BANGKOK HERITAGE & ICONIC TEMPLES',
                (
                    "SIAMESE SPLENDOR – THE GRAND PALACE & GOLDEN SHINES Start your day with a magnificent buffet breakfast before embarking on a descriptive Bangkok Sightseeing cultural tour. Navigate the walled Grand Palace complex, the historic residence of the Kings of Siam. Admire the stunning gold-leaf spires and explore the sacred Temple of the Emerald Buddha (Wat Phra Kaew). Continue to Wat Pho to stand before the monumental 46-meter Reclining Buddha temple, perfect for iconic family portraits. In the afternoon, explore the high-fashion retail centers of the city, picking up local crafts and silk souvenirs before a gentle dinner at a riverside restaurant overlooking the city's illuminated spires. Sightseeing Included: The Grand Palace, Wat Phra Kaew, Wat Pho, premium retail center visit. Optional Activities: A private longtail boat cruise through Bangkok's historic Thonburi canal network."
                ),
                [
                    'Overnight Stay: Bangkok (Premium Family-Friendly Luxury Hotel)',
                    'Meals Included: International Breakfast & Traditional Thai Fine Dining Lunch',
                ],
            ),
            _day(
                3,
                'BANGKOK TO PATTAYA COASTAL ESCAPE',
                (
                    "THE GULF COAST JOURNEY – SCENIC TRANSIT & BEACHFRONT RETREAT Enjoy your morning breakfast before checking out. Your private luxury van picks your family up for a smooth, scenic journey along the Gulf of Thailand coastline towards Pattaya. Pattaya is loved globally for its gorgeous beaches, making it an essential chapter for any true Luxury Thailand Holiday. Arrive at your premium beachfront resort and check into your suite. Spend your afternoon unwinding inside the resort's pool or taking a slow walk along the white sand beach. In the evening, explore the vibrant Pattaya beach road, filled with local street food and charming cafes. Sightseeing Included: Private luxury van highway transit, scenic resort beach orientation. Evening Experience: Walking tour of the vibrant Pattaya night market stalls."
                ),
                [
                    'Overnight Stay: Pattaya (Premium Beachfront Resort)',
                    'Meals Included: International Breakfast & Seaside Family Dinner',
                ],
            ),
            _day(
                4,
                'CORAL ISLAND MARINE EXPEDITION',
                (
                    'TROPICAL BLUE – PRIVATE SPEEDBOAT & PRISTINE SANDS Prepare for an action-packed day of aquatic discovery. Following breakfast, board a private luxury speedboat charter, cutting across the blue waves of the Gulf of Thailand to land on a pristine white-sand bay at Coral Island. Avoid all public tour crowds as TRAGUIN manages your entire aquatic itinerary. Spend time swimming in shallow, crystalline water or relaxing on beach loungers with fresh coconut juice. For the adventure lovers, take part in optional parasailing or snorkeling over the reef. Enjoy a fresh seafood lunch by the shore before cruising back to the mainland for a grand finale farewell dinner. Sightseeing Included: Private luxury speedboat charter to Coral Island, beach relaxation, reef snorkeling. Optional Activities: High-speed parasailing bundle or sea-walking tour.'
                ),
                [
                    'Overnight Stay: Pattaya (Premium Beachfront Resort)',
                    'Meals Included: International Breakfast & Beachside Seafood Buffet Lunch',
                ],
            ),
            _day(
                5,
                'DEPARTURE & CHERISHING MEMORIES',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER UNITED Enjoy your final morning breakfast looking out over the sparkling coast, capturing a final round of group family photos across the gardens. At the designated hour, your private luxury van arrives to transfer your party comfortably back to Bangkok airport for your departure flight. Your premium Thailand Family Tour concludes, leaving your loved ones with unforgettable memories crafted to perfection by TRAGUIN. Sightseeing Included: Private luxury van departure transfer, shopping stop for local artisan souvenirs.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Sukosol Bangkok Novotel Pattaya Resort',
                'Multi-city Thailand',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — The Sukosol Bangkok Novotel Pattaya Resort',
            ),
            _hotel(
                'Grande Centre Point Terminal 21Amari Pattaya Resort',
                'Multi-city Thailand',
                '4N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Grande Centre Point Terminal 21Amari Pattaya Resort',
            ),
            _hotel(
                'Shangri-La Bangkok Hilton Pattaya Hotel',
                'Multi-city Thailand',
                '4N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Shangri-La Bangkok Hilton Pattaya Hotel',
            ),
            _hotel(
                'Mandarin Oriental, Bangkok Grande Centre Point Space Pattaya',
                'Multi-city Thailand',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Mandarin Oriental, Bangkok Grande Centre Point Space Pattaya',
            )
        ],
        inclusions=[
            _inc_included('Handpicked premium accommodation as per selected hotel tier', 1),
            _inc_included('Private luxury vehicle transfers and sightseeing as per itinerary', 2),
            _inc_included('Daily buffet breakfast and curated meals as specified', 3),
            _inc_included('VIP airport fast-track reception and dedicated TRAGUIN concierge support', 4),
            _inc_excluded('International airfare and Thailand visa fees', 5),
            _inc_excluded('Personal expenses, laundry, mini-bar, and tips', 6),
            _inc_excluded('Optional activities not mentioned in the itinerary', 7),
            _inc_excluded('Travel insurance (strongly recommended)', 8),
        ],
    )
    return package, itinerary

def build_th_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-003'
    tour_code = 'TRG-BKK-HKT-FAM-2026'
    title = 'BANGKOK PHUKET FAMILY TOUR Bangkok • Grand Palace • Phuket • Phi Phi Islands • Phang Nga Bay'
    duration = '05 Nights / 06 Days'
    slug = 'th-003-bangkok-phuket-family-tour-bangkok-grand-palace-phuket-phi-phi-islands-phang-nga-bay'
    itin_slug = 'th-003-bangkok-phuket-family-tour-bangkok-grand-palace-phuket-phi-phi-islands-phang-nga-bay-itinerary'
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
            _ph('Serial code TH-003 | TRAGUIN tour code TRG-BKK-HKT-FAM-2026', 1),
            _ph('State / Country: Thailand | Category: Best Bangkok Phuket Family Tour Package', 2),
            _ph('Destinations: Bangkok (2N) + Phuket', 3),
            _ph('Ideal for: Families, Multi- generational Groups, First-time Explorers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Executive Van / Buffet Breakfast (CP), Private Island Picnics & Seafood Dinners', 7)
        ],
        moods=['Family', 'Culture', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='BANGKOK PHUKET FAMILY TOUR Bangkok',
        overview="Bangkok • Grand Palace • Phuket • Phi Phi Islands • Phang Nga Bay 05 Nights / 06 Days Classic Thailand Family Expedition SERIAL CODE: TH-003 TRAGUIN TOUR CODE: TRG-BKK-HKT- FAM-2026 STATE / COUNTRY: Thailand CATEGORY: Best Bangkok Phuket Family Tour Package DURATION: 05 Nights / 06 Days DESTINATIONS: Bangkok (2N) + Phuket (3N) IDEAL FOR: Families, Multi- generational Groups, First-time Explorers BEST SEASON: November to April VEHICLE TYPE: Private Luxury Executive Van MEAL PLAN: Buffet Breakfast (CP), Private Island Picnics & Seafood Dinners Create lifelong bonds with the Best Bangkok Phuket Family Tour Package, expertly crafted by TRAGUIN to combine iconic metropolitan heritage with serene Andaman coastal joy. This spectacular Family Tour offers a perfect balance of comfort, culture, and coastal adventure, promising breathtaking landscapes and unforgettable memories for all ages.\n\nTOUR OVERVIEW\nWelcome to your optimized Bangkok Phuket Family Expedition, a comprehensive journey designed by TRAGUIN Experts for families who demand seamless coordination, children-friendly exploration paces, and elite hospitality layouts. Across 6 wonderful days, your family will uncover Bangkok’s royal heritage and the azure island paradise of Phuket. TRAGUIN Curated Experience Note: We ensure absolute comfort at every milestone. Traveling in private, air-conditioned luxury vans with dedicated chauffeurs allows your family to completely bypass all public transport lines. Backed by handpicked premium stays and pre-vetted family dining paths, your group will experience a flawless trip protected by our 24/7 dedicated local concierge assistance.\n\nWHY CHOOSE OUR BANGKOK & PHUKET FAMILY HOLIDAY?\nBangkok and Phuket represent the gold standard for family travel in Thailand, effortlessly pairing urban royal heritage with pristine tropical island sanctuaries. Choosing a signature TRAGUIN Thailand Package guarantees access to exclusive privileges. This proposal integrates targeted tourism keywords for Google ranking, ensuring the ultimate showcase of Bangkok Sightseeing and Phuket Sightseeing wonders. Explore Top Tourist Places in Thailand: the monumental architecture of Bangkok's temples, the crystal blue waters of Phi Phi islands, and the high-fashion shopping arcades of the capital. It is widely recognized as the Best Time to Visit Thailand to capture iconic photography points, indulge in premium family-friendly marine athletics, and collect immersive experiences that define a truly Premium Thailand Experience. TRAGUIN Family Signatures: Priority group entry passes for Bangkok's landmarks, a private luxury yacht charter to the Phi Phi islands, front-row premium tables at cultural shows, and dedicated luxury van transfers throughout your stay. THE DEFINITVE DAY-WISE ITINERARY",
        seo_title='TH-003 | BANGKOK PHUKET FAMILY TOUR Bangkok | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-003 / TRG-BKK-HKT-FAM-2026): Bangkok (2N) + Phuket with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BANGKOK & RIVERFRONT WELCOME', 1),
            _ih('Day 02: BANGKOK HERITAGE & ICONSIAM', 2),
            _ih('Day 03: BANGKOK TO PHUKET COASTAL ESCAPE', 3),
            _ih('Day 04: PHI PHI ISLANDS MARINE EXPEDITION', 4),
            _ih('Day 05: CULTURAL GARDENS & FAREWELL GALA', 5),
            _ih('Day 06: PHUKET DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BANGKOK & RIVERFRONT WELCOME',
                (
                    'THE CAPITAL WELCOME – METROPOLITAN GLAMOUR BEGINS Your spectacular Thailand Family Tour begins perfectly the moment your family arrives at Bangkok’s Suvarnabhumi Airport. Receive our VIP reception, managed seamlessly by your dedicated TRAGUIN tour director. Step into your private, air-conditioned luxury van, ensuring a comfortable transit into the center of the metropolis. Check into your premium handpicked hotel, centrally located to maximize your exploration time. Take a brief orientation tour around the neighborhood to discover local cafes and conveniences before the group gathers for a welcome dinner. This sets the stage for an unforgettable family vacation. Sightseeing Included: Airport group reception, city orientation drive. Evening Experience: Family welcome dinner at an upscale river-view restaurant.'
                ),
                [
                    'Overnight Stay: Bangkok (Premium Lifestyle Family Hotel)',
                    'Meals Included: International Welcome Buffet Dinner',
                ],
            ),
            _day(
                2,
                'BANGKOK HERITAGE & ICONSIAM',
                (
                    "SIAMESE SPLENDOR – THE GRAND PALACE & URBAN RETAIL THERAPY Fuel up with a bountiful buffet breakfast. Today showcases the historical grandeur of Bangkok. Your luxury group van transfers you to the historic core to visit the Grand Palace and the Temple of the Emerald Buddha (Wat Phra Kaew), an essential Thailand Sightseeing highlight. Admire the golden spires and intricate detailing that represent the architectural genius of the Thai kingdom. In the afternoon, proceed to ICONSIAM, the crown jewel of Bangkok's shopping malls. Featuring an indoor floating market, massive luxury brand flagship stores, and phenomenal waterfront spaces, it is an unparalleled location for premium shopping. Return for a casual group dinner, celebrating the city's beautiful skyline. Sightseeing Included: Grand Palace, Wat Phra Kaew, Wat Pho, ICONSIAM Luxury Waterfront Mall. Optional Activities: Traditional longtail boat cruise through historic Thonburi canal networks."
                ),
                [
                    'Overnight Stay: Bangkok (Premium Lifestyle Family Hotel)',
                    'Meals Included: International Breakfast & Traditional Thai Bistro Lunch',
                ],
            ),
            _day(
                3,
                'BANGKOK TO PHUKET COASTAL ESCAPE',
                (
                    'TRANSIT TO THE PEARL OF THE ANDAMAN – COASTAL FAMILY BLISS Check out after breakfast as your group transfers to the airport for your internal flight to Phuket. Phuket is globally celebrated for its sapphire horizons and dramatic limestone monoliths, making it an essential chapter for your Luxury Thailand Holiday. Arrive at your premium beachfront resort and check into your spacious family suite. Spend your afternoon unwinding by the lagoon swimming pool or taking a slow walk along the white sand beach, watching the horizon transform into a vibrant sunset tapestry—a perfect start to your island adventure. Sightseeing Included: Internal flight logistics, coastal transfer, beachfront resort check-in. Evening Experience: Relaxed beachfront evening enjoying the gentle Andaman breeze.'
                ),
                [
                    'Overnight Stay: Phuket (Premium High-Rise Family Resort with Ocean View)',
                    'Meals Included: International Breakfast & Beachfront Family Dinner',
                ],
            ),
            _day(
                4,
                'PHI PHI ISLANDS MARINE EXPEDITION',
                (
                    'TROPICAL BLUE – PRIVATE SPEEDBOAT & PRISTINE SANDS Start your day with a hearty, energizing breakfast. Today is the ultimate highlight of your Phuket Sightseeing program: an expedition to the iconic Phi Phi Islands. Your group will board a private speed-craft charter, cutting across the blue waves of the Andaman Sea to land on pristine, secret bays. Spend time swimming in shallow, crystalline water or snorkeling among vibrant coral reefs. Enjoy a group buffet lunch by the shore before cruising back to the resort in the late afternoon to refresh for the evening celebration. Sightseeing Included: Private luxury speedboat charter to Phi Phi Islands, reef snorkeling. Optional Activities: Professional family photography session against the Andaman seascape backdrop.'
                ),
                [
                    'Overnight Stay: Phuket (Premium High-Rise Family Resort with Ocean View)',
                    'Meals Included: International Breakfast & Island Beachside Buffet Lunch',
                ],
            ),
            _day(
                5,
                'CULTURAL GARDENS & FAREWELL GALA',
                (
                    'BOTANICAL MARVELS & CHERISHING UNFORGETTABLE MEMORIES Enjoy a final buffet breakfast before heading to one of the most stunning popular Instagram locations: the local tropical botanical gardens. This massive valley showcases spectacular floral arrangements and traditional Thai culture, all accessible via our group-chartered open-air carts. In the evening, celebrate with a special farewell gala dinner party, raised to toast an extraordinary journey. Look back on an exceptional collection of curated experiences, breathtaking landscapes, and unforgettable group memories crafted beautifully by TRAGUIN. Sightseeing Included: Tropical garden botanical tour, premium family photography session. Evening Experience: Grand farewell gala dinner celebration.'
                ),
                [
                    'Overnight Stay: Phuket (Premium High-Rise Family Resort with Ocean View)',
                    'Meals Included: International Buffet Breakfast & Farewell Dinner',
                ],
            ),
            _day(
                6,
                'PHUKET DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER UNITED Savor your final morning breakfast at your premium resort, capturing a final round of group family photos across the tropical landscaped gardens. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless group checkout and handle luggage logistics. At the designated hour, your private luxury van arrives to transfer your family comfortably to Phuket International Airport for your return flight. Your premium Thailand Family Tour concludes beautifully, leaving your loved ones with unforgettable memories crafted to perfection by TRAGUIN. Sightseeing Included: Private luxury airport departure transfer, luggage assistance.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Sukosol Bangkok Novotel Phuket Resort',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — The Sukosol Bangkok Novotel Phuket Resort',
            ),
            _hotel(
                'Grande Centre Point Terminal 21 Phuket Marriott Merlin Beach',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Grande Centre Point Terminal 21 Phuket Marriott Merlin Beach',
            ),
            _hotel(
                'Avani+ Riverside Bangkok The Westin Siray Bay',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Avani+ Riverside Bangkok The Westin Siray Bay',
            ),
            _hotel(
                'Shangri-La Bangkok Anantara Layan / Sri Panwa',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Shangri-La Bangkok Anantara Layan / Sri Panwa',
            )
        ],
        inclusions=[
            _inc_included('Handpicked premium accommodation as per selected hotel tier', 1),
            _inc_included('Private luxury vehicle transfers and sightseeing as per itinerary', 2),
            _inc_included('Daily buffet breakfast and curated meals as specified', 3),
            _inc_included('VIP airport fast-track reception and dedicated TRAGUIN concierge support', 4),
            _inc_excluded('International airfare and Thailand visa fees', 5),
            _inc_excluded('Personal expenses, laundry, mini-bar, and tips', 6),
            _inc_excluded('Optional activities not mentioned in the itinerary', 7),
            _inc_excluded('Travel insurance (strongly recommended)', 8),
        ],
    )
    return package, itinerary

def build_th_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-004'
    tour_code = 'TRG-HKT-KBV-FAM-2026'
    title = 'PHUKET KRABI FAMILY TOUR Phuket • Krabi • Phi Phi Islands • Ao Nang Bay • 4-Islands Expedition'
    duration = '05 Nights / 06 Days'
    slug = 'th-004-phuket-krabi-family-tour-phuket-krabi-phi-phi-islands-ao-nang-bay-4-islands-expedition'
    itin_slug = 'th-004-phuket-krabi-family-tour-phuket-krabi-phi-phi-islands-ao-nang-bay-4-islands-expedition-itinerary'
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
            _ph('Serial code TH-004 | TRAGUIN tour code TRG-HKT-KBV-FAM-2026', 1),
            _ph('State / Country: Thailand | Category: Best Phuket Krabi Family Tour Package', 2),
            _ph('Destinations: Phuket (3N) + Krabi', 3),
            _ph('Ideal for: Families, Multi- generational Groups, Marine Explorers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Executive Van Buffet Breakfast (CP), Island Picnics & Fine Seafood Dinners Embrace the quintessential Andaman coastal odyssey with the Best Phuket Krabi Family Tour Package, masterfully', 7)
        ],
        moods=['Family', 'Beach', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='PHUKET KRABI FAMILY TOUR Phuket',
        overview="Phuket • Krabi • Phi Phi Islands • Ao Nang Bay • 4-Islands Expedition 05 Nights / 06 Days Premium Coastal Family Holiday SERIAL CODE: TH-004 TRAGUIN TOUR CODE: TRG-HKT-KBV- FAM-2026 STATE / COUNTRY: Thailand CATEGORY: Best Phuket Krabi Family Tour Package DURATION: 05 Nights / 06 Days DESTINATIONS: Phuket (3N) + Krabi (2N) IDEAL FOR: Families, Multi- generational Groups, Marine Explorers BEST SEASON: November to April VEHICLE TYPE: Private Luxury Executive Van Buffet Breakfast (CP), Island Picnics & Fine Seafood Dinners Embrace the quintessential Andaman coastal odyssey with the Best Phuket Krabi Family Tour Package, masterfully curated by TRAGUIN to perfectly bridge exhilarating marine discovery with family-oriented luxury comfort. From dramatic limestone monoliths and turquoise lagoons to handpicked premium resorts, discover breathtaking landscapes and create unforgettable memories on this premier Luxury Thailand Holiday.\n\nTOUR OVERVIEW\nWelcome to your bespoke Phuket Krabi Family Vacation, a meticulously designed holiday structured explicitly for families who command seamless coordination, children-friendly exploration paces, and elite hospitality layouts. Across 6 wonderful days, your family will explore the finest islands, marine reserves, and cultural wonders of Thailand's coastal paradise. TRAGUIN Curated Experience Note: We ensure absolute comfort at every milestone. Traveling in private, air-conditioned luxury vans with dedicated chauffeurs allows your family to completely bypass public queues. Backed by handpicked premium stays and pre-vetted family dining paths, your group will experience a flawless trip protected by our 24/7 dedicated local concierge assistance.\n\nWHY CHOOSE OUR LUXURY PHUKET KRABI FAMILY VACATION?\nPhuket and Krabi have evolved into the ultimate adventure and family entertainment capital of Southeast Asia, offering an unmatched variety of marine sanctuaries, emerald lagoons, and spectacular limestone coastlines. Choosing a high-end TRAGUIN Phuket Krabi Package or an exceptional Thailand Family Tour through us means stepping past generic travel routes into a world of exclusive privileges. This proposal integrates top searched tourism keywords for Google ranking, ensuring the ultimate showcase of Phuket Sightseeing and Krabi Sightseeing wonders. Uncover iconic attractions: the world-famous sheer cliffs of Railay Beach, the crystal-clear shallow waters of the Phi Phi islands, the vibrant therapeutic Emerald Pool, and the iconic coastal towers. It is universally recognized as the Best Time to Visit Thailand to explore popular Instagram locations, engage in safe children-friendly marine athletics, and collect immersive experiences that your family will cherish for a lifetime. TRAGUIN Family Signatures: Private luxury speedboat charter to the Phi Phi Islands, front-row premium tables at beachside fire-show galas, expert-led kayaking through hidden sea-caves, and dedicated private luxury van transfers. THE DEFINITVE DAY-WISE ITINERARY",
        seo_title='TH-004 | PHUKET KRABI FAMILY TOUR Phuket | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-004 / TRG-HKT-KBV-FAM-2026): Phuket (3N) + Krabi with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN PHUKET & COASTAL WELCOME', 1),
            _ih('Day 02: PRIVATE SPEEDBOAT TO PHI PHI ISLANDS', 2),
            _ih('Day 03: PHUKET CULTURAL TOUR & DEPARTURE TO KRABI', 3),
            _ih('Day 04: KRABI 4-ISLANDS EXPEDITION', 4),
            _ih('Day 05: KRABI RETREAT & DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN PHUKET & COASTAL WELCOME',
                (
                    'WELCOME TO THE PEARL – THE FAMILY TROPICAL HOLIDAY BEGINS Your spectacular Phuket Krabi Family Tour begins perfectly the moment your family arrives at Phuket International Airport. Receive a warm, traditional Thai greeting, coordinated seamlessly by your dedicated TRAGUIN tour representative. Step directly into your air-conditioned private luxury van, ensuring a completely relaxed, scenic transfer straight to your handpicked premium resort. Arrive at your premium resort and check into your spacious family suite, featuring special welcome amenities. Spend the afternoon unwinding by the panoramic swimming pool or taking your first family photos overlooking the sunset. In the evening, your private van takes you to an upscale seaside restaurant for a welcome buffet dinner filled with familiar comforts, ensuring a restful start for an unforgettable family vacation. Sightseeing Included: Private luxury van airport transit, scenic coastal drive, Patong beach orientation. Evening Experience: Family welcome dinner at an upscale restaurant with gorgeous ocean vistas.'
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: Curated Multi-Cuisine Family Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PRIVATE SPEEDBOAT TO PHI PHI ISLANDS',
                (
                    'TURQUOISE LAGOONS, SNORKELING ESCAPADES & MAYA BAY Wake up to a gorgeous morning over the ocean and enjoy a lavish buffet breakfast. Today hosts a cornerstone Premium Thailand Experience: an exclusive private island-hopping expedition to the Phi Phi Islands. Avoid all crowded commercial public tour boats as TRAGUIN arranges a private, high-speed luxury speedboat to pick up your family directly from the resort beachfront. Cruise over crystal-clear turquoise waters to arrive at the vertical limestone walls of Maya Bay, offering a premium photography point for the family. The kids can swim in the calm shallow waters while the adults snorkel in the emerald basin of Pileh Lagoon. Savor a delicious fresh gourmet lunch served right on the white sands of Bamboo Island. Conclude the day exploring the historic Viking Cave before cruising back home. Sightseeing Included: Private Speedboat to Phi Phi Islands, Maya Bay entry, Pileh Lagoon snorkeling, Bamboo Island beach stop, Viking Cave. Optional Activities: Undersea Sea-Walking or Glass-Bottom Boat coral reef viewing for children and seniors.'
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Beachside Island Picnic Lunch',
                ],
            ),
            _day(
                3,
                'PHUKET CULTURAL TOUR & DEPARTURE TO KRABI',
                (
                    'BIG BUDDHA PANORAMA, OLD TOWN STREETS & COASTAL TRANSIT Enjoy a beautiful morning breakfast before starting a comprehensive Phuket Sightseeing cultural day. Your private chauffeur navigates your family up the Nakkerd Hills to stand at the base of the majestic 45-meter Big Buddha monument. This peak offers a staggering 360-degree panorama of Chalong Bay and Phuket Town— consistently ranked among the most popular Instagram locations. Continue your premium tour to Wat Chalong monastery and the historic Sino-Portuguese colonial streets of Old Phuket Town. Walk past beautiful mansions and artisan boutiques. In the afternoon, board your private luxury van for a smooth, scenic journey along the coastline towards Krabi. Arrive at your premium beachfront resort and check into your family-friendly suite. Sightseeing Included: The Big Buddha, Wat Chalong Temple, Old Phuket Town, scenic cross-province highway drive. Evening Experience: Strolling down the vibrant Ao Nang walking street, sampling local street food.'
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Contemporary Thai Fine Dining Lunch',
                ],
            ),
            _day(
                4,
                'KRABI 4-ISLANDS EXPEDITION',
                (
                    'NATURAL SANDBARS, CORAL REEFS & PRISTINE TROPICAL BEAUTY Today unveils the crowning beauty of your Krabi Sightseeing itinerary. After breakfast, a private speed-craft launches directly from the resort sands for a thrilling day across Krabi’s legendary 4-Islands. Visit Phra Nang Cave Beach, renowned for its vertical rock face climbers, before speeding towards Tup Island, where a unique natural sandbar emerges at low tide, allowing your party to walk between islands on crystal water—a perfect photography point. Snorkel over the live barrier reefs of Chicken Island, surrounded by schools of tropical fish. Return to the resort to refresh for your evening leisure time. Sightseeing Included: Tup Island Sandbar walk, Chicken Island reef snorkeling, Poda Island, Phra Nang Cave. Evening Experience: Private front-row premium table at a spectacular Ao Nang beachside fire show.'
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Beachside Family Lunch',
                ],
            ),
            _day(
                5,
                'KRABI RETREAT & DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER UNITED Enjoy your final morning buffet breakfast overlooking the ocean, capturing a final round of group family photos across the tropical landscaped gardens. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless checkout and handle all luggage logistics. At the designated hour, your private luxury van arrives to transfer your family comfortably to Krabi International Airport for your departure flight back home. Your premium Phuket Krabi Family Tour concludes beautifully, leaving your loved ones with unforgettable memories crafted to perfection by TRAGUIN. Sightseeing Included: Boutique souvenir shopping, private luxury airport departure transfer.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Phuket Marriott Merlin Beach Premium Family Pool View Room Centara Grand Beach Resort Krabi Deluxe Ocean Face Room',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Phuket Marriott Merlin Beach Premium Family Pool View Room Centara Grand Beach Resort Krabi Deluxe Ocean Face Room',
            ),
            _hotel(
                'The Westin Siray Bay Resort Luxury Seaview Family Suite Rayavadee Krabi Resort Deluxe Pavilion Estate',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Westin Siray Bay Resort Luxury Seaview Family Suite Rayavadee Krabi Resort Deluxe Pavilion Estate',
            ),
            _hotel(
                'Anantara Layan Phuket / Sri Panwa Pool Villa / Luxury Ocean Suite Phulay Bay, Ritz-Carlton Reserve Reserve Pavilion Pool Villa',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Anantara Layan Phuket / Sri Panwa Pool Villa / Luxury Ocean Suite Phulay Bay, Ritz-Carlton Reserve Reserve Pavilion Pool',
            )
        ],
        inclusions=[
            _inc_included('Daily Meals: 5 International Buffet Breakfast layouts with children-friendly sections.', 1),
            _inc_included('Private Vehicles: Private air-conditioned luxury van with an experienced driver for all transfers.', 2),
            _inc_included('Island Cruises: Private Speedboat to Phi Phi Islands with beachside family lunch.', 3),
            _inc_included('VIP Sightseeing: Priority front-row seats at Ao Nang beach fire show.', 4),
            _inc_included("Marine Excursions: Private speed-craft charter for Krabi's 4-Islands.", 5),
            _inc_included('TRAGUIN Support: 24/7 dedicated local on- ground family concierge assistance.', 6),
            _inc_included('Flights: International flight tickets from your home country to Thailand.', 7),
            _inc_excluded('"Creating Memories Beyond Destinations" PREMIUM TRAVEL | LUXURY HOLIDAYS | CORPORATE MICE | HONEYMOON EXPERTS | FAMILY VACATIONS Accommodation: 05 Nights stay in handpicked premium family resorts.', 8),
            _inc_excluded('Visa Fees: Thailand Visa-on-Arrival or fast-track electronic visa processing fees.', 9),
        ],
    )
    return package, itinerary

def build_th_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-005'
    tour_code = 'TRG-THA-2026-V5'
    title = 'THAILAND TOUR PACKAGE Bangkok • Pattaya • Phuket • Phi Phi Islands'
    duration = '07 Nights / 08 Days'
    slug = 'th-005-thailand-tour-package-bangkok-pattaya-phuket-phi-phi-islands'
    itin_slug = 'th-005-thailand-tour-package-bangkok-pattaya-phuket-phi-phi-islands-itinerary'
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
            _ph('Serial code TH-005 | TRAGUIN tour code TRG-THA-2026-V5', 1),
            _ph('State / Country: Thailand | Category: Premium Family Tour', 2),
            _ph('Destinations: Phuket (3N) + Pattaya', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van (Toyota Commuter) / Buffet Breakfast (CP) & Curated Dinners', 7),
            _ph('TRAGUIN Signature Experience: Private luxury speedboats tailored for families, avoiding standard', 8),
            _ph("Curated by TRAGUIN Experts: Handpicked safety-certified hotels featuring dedicated children's", 9),
            _ph('Personalized Assistance: English-speaking local tour guides to navigate local traditions smoothly.', 10),
            _ph('Luxury Transportation: High-roof premium vans with complimentary Wi-Fi and cold refreshments', 11)
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
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='THAILAND TOUR PACKAGE Bangkok',
        overview="Bangkok • Pattaya • Phuket • Phi Phi Islands 07 Nights / 08 Days Premium Family Tour SERIAL CODE: TH-005 TRAGUIN TOUR CODE: TRG-THA-2026-V5 STATE / COUNTRY: Thailand CATEGORY: Premium Family Tour DURATION: 07 Nights / 08 Days DESTINATIONS: Phuket (3N) + Pattaya (2N) + Bangkok (2N) IDEAL FOR: Families, Couples, Luxury Seekers BEST SEASON: November to April VEHICLE TYPE: Private Luxury Van (Toyota Commuter) MEAL PLAN: Buffet Breakfast (CP) & Curated Dinners Embark on an enchanting tropical escape with the Best Thailand Tour Package, curated explicitly by TRAGUIN to offer an unmatched blend of ultra-luxury stays, breathtaking landscapes, and deeply immersive cultural treasures. From the sun-kissed sands of Andaman's signature shores to the electric high-rises of Bangkok, your family will experience an unforgettable luxury Thailand holiday.\n\nTOUR OVERVIEW\nWelcome to your bespoke Thailand Discovery vacation, meticulously designed for modern families who command the finer nuances of high-end travel. On this comprehensive 8-day itinerary, your party will enjoy handpicked premium accommodations, private seamless logistics in chauffeured vehicles, and curated local culinary journeys. TRAGUIN Curated Experience Note: Every phase of your itinerary has been vetted by our local destination experts. We guarantee personalized, on-ground assistance, priority fast-track entry at key sights, and exclusive access to premium vantage points ensuring your memories are completely beyond ordinary destinations.\n\nWHY CHOOSE OUR LUXURY THAILAND HOLIDAY?\nThailand remains the world’s most coveted tropical haven, seamlessly interweaving ancient Siamese culture with ultra-modern luxury. When booking a Thailand Family Tour through TRAGUIN, you step past the conventional tourist path. This itinerary targets the most highly searched tourism keywords for Google ranking, ensuring an incredibly balanced exploration of top tourist places in Thailand. Our signature itinerary uncovers stunning Thailand Sightseeing wonders: the emerald-hued waters of the Phi Phi Islands, the vibrant nightlife and cabaret shows of Pattaya, and the golden-spired architectural marvels of Bangkok's Grand Palace. It is widely considered the Best Time to Visit Thailand to capture iconic, high-fashion Instagram locations while enjoying absolute safety, children-friendly activity hubs, and premium shopping arcades packed with high-end global labels and delicate local crafts. TRAGUIN Signature Inclusions: Exclusive private speedboat transfers to Phi Phi Island, front-row premium seating at the Alcazar Cabaret Show, VIP entry tickets to Mahanakhon SkyWalk, and dedicated 24/7 concierge travel support. THE DEFINITIVE DAY-WISE ITINERARY",
        seo_title='TH-005 | THAILAND TOUR PACKAGE Bangkok | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Thailand package (TH-005 / TRG-THA-2026-V5): Phuket (3N) + Pattaya with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: PHUKET ARRIVAL', 1),
            _ih('Day 02: PHUKET TO PHI PHI ISLANDS', 2),
            _ih('Day 03: PHUKET CITY EXPLORATION', 3),
            _ih('Day 04: PHUKET TO PATTAYA', 4),
            _ih('Day 05: PATTAYA CORAL ISLAND', 5),
            _ih('Day 06: PATTAYA TO BANGKOK', 6),
            _ih('Day 07: BANGKOK FAMILY FUN & SHOPPING', 7),
            _ih('Day 08: BANGKOK DEPARTURE', 8),
            _ih('TRAGUIN Signature Experience: Private luxury speedboats tailored for families, avoiding standard', 9),
            _ih("Curated by TRAGUIN Experts: Handpicked safety-certified hotels featuring dedicated children's", 10)
        ],
        days=[
            _day(
                1,
                'PHUKET ARRIVAL',
                (
                    'SAWADDEE THAILAND – WELCOME TO THE PEARL OF THE ANDAMAN Your spectacular Thailand Discovery family expedition begins the moment you touch down at Phuket International Airport. As you emerge from the terminal, a warm, traditional Thai welcome awaits your family, coordinated seamlessly by your dedicated TRAGUIN tour representative. You will be escorted to an air- conditioned luxury private van, ensuring a completely relaxed, scenic cross-island transfer straight to your handpicked premium resort. Phuket is globally celebrated for its breathtaking landscapes, dramatic limestone cliffs, and vibrant coastal culture, making it the perfect start for a Luxury Thailand Holiday. Arrive at your luxury resort and check into your premium sea-view room. Spend the afternoon unwinding by the infinity pool or strolling along the powdery sand beaches. As evening approaches, watch the horizon transform into a vibrant tapestry of pastel hues, offering a picture-perfect photography opportunity for the family. Sightseeing Included: Scenic coastal transfer from airport to resort, leisure walk at Patong Beach. Evening Experience: Welcome Cocktail/Mocktail at a premium beachfront lounge with sunset views.'
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: Curated Multi-cuisine Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PHUKET TO PHI PHI ISLANDS',
                (
                    'EXCLUSIVE PRIVATE SPEEDBOAT ESCAPADE TO PHI PHI & MAYA BAY Wake up to the soothing sound of the waves and enjoy a lavish buffet breakfast. Today hosts one of the most searched experiences in the world: an exclusive island-hopping expedition across the Andaman Sea. Avoid the crowded regular tour boats as TRAGUIN arranges a private, high-speed luxury speedboat to whisk your family away to the iconic Phi Phi Islands. Cruise over crystal-clear turquoise waters directly toward Maya Bay, the world-famous paradise sheltered by towering 100-meter cliffs. Step onto the soft sand for a premium photography session amidst one of the top tourist places in Thailand. Next, snorkel over the brilliant coral reefs of Pileh Lagoon, a natural emerald swimming pool. Savor an exquisite, private beachfront gourmet lunch specially arranged at a quiet luxury spot on Phi Phi Don. Conclude the day exploring Monkey Beach and the historic Viking Cave, capturing unforgettable memories with your family. Sightseeing Included: Maya Bay, Pileh Lagoon, Bamboo Island snorkeling, Viking Cave, Monkey Beach. Optional Activities: Deep-sea scuba diving under expert PADI guidance, sea-kayaking through hidden caves.'
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Beachside Island Lunch',
                ],
            ),
            _day(
                3,
                'PHUKET CITY EXPLORATION',
                (
                    "CULTURAL IMMERSION, COLONIAL HERITAGE & ICONIC VIEWPOINTS Today, dive deep into the multi-layered heritage of Thailand's largest island. Following breakfast, embark on a comprehensive Phuket Sightseeing tour. Your private chauffeur will navigate you up the Nakkerd Hills to stand at the base of the majestic 45-meter Big Buddha. This vantage point offers an incredible 360-degree panorama of Chalong Bay and Phuket Town—consistently ranked among the most popular Instagram locations in Southeast Asia. Continue your premium cultural journey to Wat Chalong, Phuket’s most revered Buddhist monastery, adorned with intricate golden filigree. In the afternoon, transition to the charming streets of Old Phuket Town. Walk past beautifully preserved Sino-Portuguese colonial mansions, vibrant street art, and quirky artisan cafes. It's an exceptional location for shopping for authentic handcrafted souvenirs, batik textiles, and premium local cashew treats. Sightseeing Included: The Big Buddha, Wat Chalong Temple, Old Phuket Town, Karon Viewpoint. Evening Experience: Catching the breathtaking, iconic sunset at Phromthep Cape, the southernmost tip of Phuket."
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Traditional Thai Fine Dining',
                ],
            ),
            _day(
                4,
                'PHUKET TO PATTAYA',
                (
                    'TRANSIT TO THE RIVIERA OF THAILAND & VIP ALCAZAR SHOW After a hearty breakfast, check out of your resort. Your private vehicle will transfer you to Phuket Airport for your short domestic flight to Bangkok (Suvarnabhumi/Don Mueang). Upon arrival, your family will immediately step into your waiting TRAGUIN private vehicle for a smooth, scenic drive along the coast to the dynamic resort city of Pattaya. Pattaya has evolved into an incredible playground for family entertainment and premium beach luxury. Upon check-in at your high-end hotel, take a few hours to enjoy the luxury amenities. In the evening, we have reserved premium VIP front-row seats for your family at the globally acclaimed Alcazar Cabaret Show. Witness an absolute masterclass in theatrical production, featuring mesmerizing costumes, state-of-the-art light effects, and spectacular international dance sequences. Sightseeing Included: Domestic flight transit, coastal highway drive, VIP entry to Alcazar Show. Evening Experience: Post-show night walk along the neon-lit, energetic Pattaya Beach Road.'
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Ocean View Hotel)',
                    'Meals Included: International Buffet Breakfast & Indian Culinary Buffet Dinner',
                ],
            ),
            _day(
                5,
                'PATTAYA CORAL ISLAND',
                (
                    'EXHILARATING CORAL ISLAND ESCAPE & WATERSPORTS ADVENTURE Prepare for an action-packed morning on the golden sands of Koh Larn, affectionately known as Coral Island. After breakfast, a private speedboat picks your family up directly from Pattaya beach. Cut through the Gulf of Thailand to arrive at a secluded stretch of pristine white sand, far from the commercial crowds. This area is the gold standard for a Thailand Family Tour looking for high-octane fun. The day is packed with premium adventures. Your package includes an exhilarating parasailing flight, offering birds-eye views of the coast, alongside a thrilling banana boat ride. Spend the afternoon swimming in the warm, crystal-clear water or exploring the vibrant coral reefs below on a glass-bottom boat. Return to the mainland for a fresh seafood lunch, leaving the late afternoon open for an optional premium Thai spa experience. Sightseeing Included: Private Speedboat to Coral Island, Parasailing, Banana Boat Ride. Optional Activities: Undersea Sea-Walking, Jet Skiing, Underwater Jet-scooters.'
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Ocean View Hotel)',
                    'Meals Included: International Buffet Breakfast & Premium Local Seafood Lunch',
                ],
            ),
            _day(
                6,
                'PATTAYA TO BANGKOK',
                (
                    "MAJESTIC TEMPLES & AN INCREDIBLE LUXURY DINNER CRUISE ON CHAO PHRAYA Bid farewell to Pattaya as your private vehicle drives your family back towards the historic heart of the kingdom: Bangkok. Along the way, experience authentic Bangkok Sightseeing by stopping at two of the capital's most legendary shrines. Visit Wat Traimit to view the astounding Golden Buddha—a 5.5-ton solid gold statue dating back to the Sukhothai period. Next, explore Wat Pho, home to the monumental 46-meter Reclining Buddha covered in exquisite gold leaf. Arrive at your ultra-luxury hotel overlooking the River of Kings. In the evening, dress in your finest resort wear for a hallmark TRAGUIN Premium Thailand Experience: a 5-star luxury dinner cruise aboard the Grand Pearl Cruise liner on the Chao Phraya River. Glide past the brilliantly illuminated Grand Palace and Wat Arun (The Temple of Dawn) while enjoying a sumptuous international buffet, live jazz music, and classical Thai dance performances. Sightseeing Included: Wat Traimit (Golden Buddha), Wat Pho (Reclining Buddha), City Driving Tour. Evening Experience: 5-Star Luxury Chao Phraya River Dinner Cruise with live performances."
                ),
                [
                    'Overnight Stay: Bangkok (Ultra-Luxury Riverside Hotel)',
                    'Meals Included: International Buffet Breakfast & Premium Cruise Dinner',
                ],
            ),
            _day(
                7,
                'BANGKOK FAMILY FUN & SHOPPING',
                (
                    "SAFARI WORLD & MARINE PARK TO HIGH-FASHION ICONSIAM SHOPPING Dedicate today to pure family joy and world-class retail luxury. After breakfast, head to Safari World & Marine Park—Thailand’s premier open-air wildlife sanctuary. Drive through vast African-style savannas to see lions, tigers, and giraffes roaming completely free. Afterward, enter the Marine Park to witness spectacular, high- production animal shows, including the famous Hollywood Cowboy Stunt Spectacular and the intelligent Dolphin Show, an absolute favorite for children. In the late afternoon, your private van will drop you at ICONSIAM, the crown jewel of Bangkok's shopping malls. Featuring an indoor floating market, high-fashion luxury brand flagships, and phenomenal waterfront views, it is an unparalleled location for premium shopping. Find exquisite silks, high-end electronics, and unique local designer pieces to commemorate your trip. Sightseeing Included: Safari Park Drive, Marine Park Shows, ICONSIAM Luxury Mall. Optional Activities: Mahanakhon SkyWalk glass tray experience at 314 meters above the city skyline."
                ),
                [
                    'Overnight Stay: Bangkok (Ultra-Luxury Riverside Hotel)',
                    'Meals Included: International Buffet Breakfast & Safari World Buffet Lunch',
                ],
            ),
            _day(
                8,
                'BANGKOK DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS Enjoy your final decadent buffet breakfast at your luxury hotel, capturing a final round of panoramic family photos overlooking the bustling Chao Phraya River. Depending on your flight departure schedule, the morning is yours to relax, squeeze in last-minute souvenir shopping, or enjoy a final authentic Thai iced tea. At the designated hour, your professional, chauffeured vehicle will arrive to provide a seamless private transfer to Suvarnabhumi International Airport for your return flight home. As you board your aircraft, look back on an exceptional collection of curated experiences, breathtaking landscapes, and unforgettable family memories crafted beautifully by TRAGUIN. Your premium Thailand Discovery tour concludes, leaving you with stories to pass down through generations. Sightseeing Included: Private luxury airport departure transfer.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Phuket Resort Superior Ocean Room (BB) Amari Pattaya Deluxe Ocean View (BB) The Sukosol Bangkok Premier Room (BB)',
                'Multi-city Thailand',
                '7N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Novotel Phuket Resort Superior Ocean Room (BB) Amari Pattaya Deluxe Ocean View (BB) The Sukosol Bangkok Premier Room (BB',
            ),
            _hotel(
                'Phuket Marriott Resort, Merlin Beach Pool View Room (BB) Hilton Pattaya Executive Ocean Front (BB) Avani+ Riverside Bangkok Hotel Avani River View Room (BB)',
                'Multi-city Thailand',
                '7N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Phuket Marriott Resort, Merlin Beach Pool View Room (BB) Hilton Pattaya Executive Ocean Front (BB) Avani+ Riverside Bang',
            ),
            _hotel(
                'The Westin Siray Bay Resort & Spa Luxury Seaview Suite (BB) Grande Centre Point Space Pattaya Space Premium Room (BB) Shangri-La Bangkok Deluxe Horizon River Room (BB)',
                'Multi-city Thailand',
                '7N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Westin Siray Bay Resort & Spa Luxury Seaview Suite (BB) Grande Centre Point Space Pattaya Space Premium Room (BB) Sh',
            ),
            _hotel(
                'Anantara Layan Phuket Resort Deluxe Pool Villa (BB) InterContinental Pattaya Resort Club Panoramic Ocean Suite (BB) Mandarin Oriental, Bangkok Deluxe Chao Phraya Suite (BB)',
                'Multi-city Thailand',
                '7N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Anantara Layan Phuket Resort Deluxe Pool Villa (BB) InterContinental Pattaya Resort Club Panoramic Ocean Suite (BB) Mand',
            )
        ],
        inclusions=[
            _inc_included('Daily Meals: 7 International Buffet Breakfasts, 3 Premium Lunches, 3 Curated Dinners.', 1),
            _inc_included('Private Transfers: Dedicated luxury air- conditioned Toyota Commuter Van for all transfers and tours.', 2),
            _inc_included('Exclusive Sightseeing: Private Speedboat to Phi Phi Island and Pattaya Coral Island.', 3),
            _inc_included('International Flights: Main airline tickets from home country to Thailand and back.', 4),
            _inc_excluded('Accommodation: 07 Nights stay in handpicked premium hotels.', 5),
            _inc_excluded('Domestic Flights: Internal airfare for Phuket to Bangkok route (Can be added on request).', 6),
            _inc_excluded('Visa Fees: Thailand Visa-on-Arrival or E-Visa processing fees.', 7),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, premium mini-bar items, and tips.', 8),
            _inc_excluded('Optional Tours: Mahanakhon Skywalk tickets, undersea sea-walking, and scuba diving.', 9),
        ],
    )
    return package, itinerary

def build_th_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-006'
    tour_code = 'TRG-HKT-HON-2026'
    title = 'PHUKET HONEYMOON PACKAGE Phuket • Patong • Phi Phi Islands • Phang Nga Bay'
    duration = '04 Nights / 05 Days'
    slug = 'th-006-phuket-honeymoon-package-phuket-patong-phi-phi-islands-phang-nga-bay'
    itin_slug = 'th-006-phuket-honeymoon-package-phuket-patong-phi-phi-islands-phang-nga-bay-itinerary'
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
            _ph('Serial code TH-006 | TRAGUIN tour code TRG-HKT-HON-2026', 1),
            _ph('State / Country: Thailand | Category: Luxury Honeymoon Package', 2),
            _ph('Destinations: Phuket Romantic Island', 3),
            _ph('Ideal for: Honeymooners, Couples, Romance Seekers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Sedan (BMW / Mercedes Class available) / Buffet Breakfast (CP) & Private Candlelight Dinner Celebrate your new beginning with the ultimate Phuket Honeymoon Package, meticulously curated', 7),
            _ph('TRAGUIN Signature Experience: Private Catamaran and Luxury Yacht cruises, completely avoiding', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked romantic properties featuring ultimate seclusion, infinity', 9),
            _ph('Personalized Assistance: Dedicated on-ground coordinator to handle seamless transfers, dinner', 10),
            _ph('Luxury Transportation: Elite private sedans stocked with chilled water, music preferences, and wet', 11)
        ],
        moods=['Luxury', 'Honeymoon', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='PHUKET HONEYMOON PACKAGE Phuket',
        overview="Phuket • Patong • Phi Phi Islands • Phang Nga Bay 04 Nights / 05 Days Ultra-Luxury Romantic Escape SERIAL CODE: TH-006 TRAGUIN TOUR CODE: TRG-HKT-HON-2026 STATE / COUNTRY: Thailand CATEGORY: Luxury Honeymoon Package DURATION: 04 Nights / 05 Days DESTINATIONS: Phuket Romantic Island Escape (4N) IDEAL FOR: Honeymooners, Couples, Romance Seekers BEST SEASON: November to May VEHICLE TYPE: Private Luxury Sedan (BMW / Mercedes Class available) MEAL PLAN: Buffet Breakfast (CP) & Private Candlelight Dinner Celebrate your new beginning with the ultimate Phuket Honeymoon Package, meticulously curated by TRAGUIN to immerse your love story in breathtaking landscapes, absolute seclusion, and timeless coastal elegance. From exclusive private sunset cruises to tailored couple therapies, experience the finest Luxury Phuket Holiday.\n\nTOUR OVERVIEW\nWelcome to your meticulously designed Romantic Phuket getaway, tailored exclusively for couples who expect a flawless blend of intimacy and elite personalization. On this premium 5-day getaway, TRAGUIN brings you handpicked premium stays featuring private plunge pools, intimate beachfront dining under a blanket of stars, and private, chauffeured transfers. TRAGUIN Curated Experience Note: Every moment is uniquely designed by our romance experts to forge unforgettable memories. From private boat journeys to secluded shores to decorated honeymoon suites, your transition into forever will be nothing short of magical.\n\nWHY CHOOSE OUR PREMIUM PHUKET EXPERIENCE?\nPhuket is the crown jewel of romance in Southeast Asia, world-renowned for its emerald waters, hidden coves, and spectacular tropical sunsets. Opting for a Phuket Family Tour or a dedicated Phuket Honeymoon Package through TRAGUIN ensures you sidestep ordinary tourist routes for a completely elevated experience. This itinerary integrates heavily searched tourism keywords to guarantee elite positioning while focusing on the finest Phuket Sightseeing highlights. From exploring the iconic limestone monoliths of James Bond Island to walking the historic streets of Old Phuket Town, our itinerary captures the top tourist places in Phuket. It is the absolute Best Time to Visit Phuket to indulge in high-fashion couples' photo sessions across popular Instagram locations, exclusive candlelit sea-cave dining, and premium beachfront beach club culture. TRAGUIN Signature Honeymoon Amenities: Complimentary bottle of premium sparkling wine, customized floral room decorations, private luxury catamaran cruise at sunset, and an immersive 120-minute couple's aroma-spa therapy. THE ROMANTIC DAY-WISE ITINERARY",
        seo_title='TH-006 | PHUKET HONEYMOON PACKAGE Phuket | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Thailand package (TH-006 / TRG-HKT-HON-2026): Phuket Romantic Island with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN PHUKET & SUNSET LUXURY', 1),
            _ih('Day 02: PHI PHI ISLANDS BY PRIVATE CATAMARAN', 2),
            _ih('Day 03: PHUKET SUNSET CRUISE & SPA IMMERSION', 3),
            _ih('Day 04: PHANG NGA BAY & HERITAGE DISCOVERY', 4),
            _ih('Day 05: PHUKET DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private Catamaran and Luxury Yacht cruises, completely avoiding', 6),
            _ih('Curated by TRAGUIN Experts: Handpicked romantic properties featuring ultimate seclusion, infinity', 7),
            _ih('Personalized Assistance: Dedicated on-ground coordinator to handle seamless transfers, dinner', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN PHUKET & SUNSET LUXURY',
                (
                    'WELCOME TO PARADISE – UNVEILING YOUR ROMANTIC ESCAPE Your dream Phuket Honeymoon Package unfolds perfectly as you arrive at Phuket International Airport. Step into the tropical breeze where your private TRAGUIN lifestyle manager greets you with fresh orchids and cold refreshments. A private executive vehicle transfers you seamlessly along the beautiful Andaman coastline to your ultra-luxury pool villa. Check into your handpicked resort, where a beautifully arranged honeymoon floral setup and a chilled bottle of premium sparkling wine await you. Spend the afternoon in complete privacy, unwinding inside your private pool or listening to the waves. In the evening, step down to a secluded section of the beach for a private candlelight dinner curated by an executive chef, creating your very first unforgettable memories together. Sightseeing Included: Private luxury airport-to-resort transfer, check-in assistance. Evening Experience: Signature TRAGUIN Beachfront Private Candlelight Dinner under the stars.'
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Private Pool Villa)',
                    'Meals Included: 4-Course Gourmet Beachfront Dinner',
                ],
            ),
            _day(
                2,
                'PHI PHI ISLANDS BY PRIVATE CATAMARAN',
                (
                    "CRYSTAL WATERS & SECRETS OF MAYA BAY – AN INTIMATE VOYAGE Wake up to a beautiful morning breakfast overlooking the ocean. Today, avoid the standard group tours as TRAGUIN arranges a private luxury catamaran charter to the world-famous Phi Phi Islands. Sail over pure turquoise waters towards Maya Bay, the breathtaking setting made famous globally by Hollywood, enclosed by colossal karst cliffs. Dive into the crystal-clear waters of Pileh Lagoon for an intimate swimming and snorkeling experience amidst vibrant coral gardens. Your crew will serve a premium gourmet picnic lunch on the white sands of Bamboo Island. Conclude your voyage cruising past the dramatic Viking Cave and Monkey Beach, toast to your love with champagne as the sun dips below the horizon, providing a world-class photography point. Sightseeing Included: Private Catamaran Cruise to Maya Bay, Pileh Lagoon, Bamboo Island. Optional Activities: Professional drone couples' photography session on the beach."
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Private Pool Villa)',
                    'Meals Included: Buffet Breakfast & Luxury Catamaran Gourmet Picnic Lunch',
                ],
            ),
            _day(
                3,
                'PHUKET SUNSET CRUISE & SPA IMMERSION',
                (
                    "TOTAL RENEWAL & TWILIGHT SAILING ON THE ANDAMAN SEA Dedicate your morning to absolute relaxation and wellness. After a floating breakfast inside your pool villa, your chauffeur will transfer you to an award-winning luxury wellness sanctuary. Indulge in an exclusive 120- minute TRAGUIN Signature Couple's Spa, featuring a traditional Thai herbal steam, organic body scrubs, and a therapeutic aromatic hot stone oil massage side-by-side. In the late afternoon, experience an iconic Phuket Sightseeing highlight. Board a luxury twilight yacht at Chalong Pier. Sip premium wine and enjoy fine canapés as you cruise towards Promthep Cape—one of the most celebrated popular Instagram locations in Thailand. Witness an unforgettable tropical sunset from the deck of your yacht as the sea turns into deep golden shades. Sightseeing Included: Twilight Yacht Cruise, Promthep Cape coastal views from the ocean. Evening Experience: Sunset sailing with live acoustic music, premium wine, and gourmet tapas on deck."
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Private Pool Villa)',
                    'Meals Included: Floating Villa Breakfast & Twilight Yacht Canapés',
                ],
            ),
            _day(
                4,
                'PHANG NGA BAY & HERITAGE DISCOVERY',
                (
                    'MYSTICAL SEA CAVES & HERITAGE WALK IN OLD PHUKET TOWN Today combines dramatic nature with cultural heritage. Following breakfast, travel north to Phang Nga Bay. Board a luxury long-tail speed-craft to glide through towering limestone pillars. Explore the sea caves of Koh Panak and kayak into the hidden lagoons of Koh Hong, before visiting the legendary James Bond Island. In the afternoon, your private vehicle heads into Old Phuket Town. Walk hand-in-hand through historic avenues lined with elegant Sino-Portuguese architecture, colorful shophouses, and local boutique galleries. Stop at a high-end local cafe for a refreshing artisanal coffee or Thai iced tea before driving up to the Karon Viewpoint to witness a sweeping three-beach panorama. Sightseeing Included: James Bond Island, Koh Hong Sea Cave Kayaking, Old Phuket Town, Karon Viewpoint. Optional Activities: Helicopter flight over Phang Nga Bay for an incredible birds-eye view of the landscape.'
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Private Pool Villa)',
                    'Meals Included: Buffet Breakfast & Authentic Local Thai Fine Dining Lunch',
                ],
            ),
            _day(
                5,
                'PHUKET DEPARTURE',
                (
                    'MEMORIES BEYOND DESTINATIONS – FOREVER ENTWINED Savor your final morning breakfast at your villa. Enjoy a leisurely dip in your private pool and capture final photos across the tropical gardens. Depending on your flight schedule, your TRAGUIN concierge can arrange last-minute visits to premium souvenir shops or premium local leather outlets. Your private luxury vehicle arrives to transfer you comfortably to Phuket International Airport for your journey home. As you board your flight, look back on a beautifully curated Premium Phuket Experience that has seamlessly joined luxury, adventure, and romance into a beautiful story to last a lifetime. Sightseeing Included: Private luxury airport departure transfer.'
                ),
                [
                    'Meals Included: Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Pullman Phuket Arcadia Naithon Beach Deluxe Ocean Room Complimentary Honeymoon Cake & Bed Decoration',
                'Multi-city Thailand',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Pullman Phuket Arcadia Naithon Beach Deluxe Ocean Room Complimentary Honeymoon Cake & Bed Decoration',
            ),
            _hotel(
                'The Pavilion Phuket Spa & Pool Pavilion Suite Bed Decoration, Welcome Fruit Platter & 1 Cocktails Voucher',
                'Multi-city Thailand',
                '4N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — The Pavilion Phuket Spa & Pool Pavilion Suite Bed Decoration, Welcome Fruit Platter & 1 Cocktails Voucher',
            ),
            _hotel(
                'The Shore at Katathani Seaview Pool Villa Sparkling Wine Bottle, Floral Bath Setup & Floating Breakfast',
                'Multi-city Thailand',
                '4N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Shore at Katathani Seaview Pool Villa Sparkling Wine Bottle, Floral Bath Setup & Floating Breakfast',
            ),
            _hotel(
                'Trisara Phuket / Sri Panwa Luxury Resort Ocean View Luxury Pool Villa Premium Champagne, 60-min Couple Spa & Private Beachside Pavilion Access',
                'Multi-city Thailand',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Trisara Phuket / Sri Panwa Luxury Resort Ocean View Luxury Pool Villa Premium Champagne, 60-min Couple Spa & Private Bea',
            )
        ],
        inclusions=[
            _inc_included('Honeymoon Kit: Premium Sparkling Wine, floral decorations, and floating breakfast setup.', 1),
            _inc_included('Private Transfers: Air-conditioned luxury private sedan for all transfers and tours.', 2),
            _inc_included('Exclusive Sailing: Private Luxury Catamaran Cruise to Phi Phi Islands with gourmet lunch.', 3),
            _inc_included('Twilight Experience: Luxury Yacht Cruise to Promthep Cape with wine & canapés.', 4),
            _inc_included('Wellness: Complimentary 120-minute Premium Couple’s Spa Treatment.', 5),
            _inc_included('Dining: 4 Buffet Breakfasts, 1 Catamaran Lunch, 1 Beachfront Candlelight Dinner.', 6),
            _inc_included('TRAGUIN Support: 24/7 dedicated on-ground concierge travel assistance.', 7),
            _inc_included('Flights: International airfares from home country to Phuket.', 8),
            _inc_excluded('Accommodation: 04 Nights stay in handpicked premium pool villas.', 9),
            _inc_excluded('Visa Cost: Thailand entry visa charges or fast- track processing fees.', 10),
            _inc_excluded('Personal Expenses: Laundry, room service orders, telephone charges, and tips.', 11),
            _inc_excluded('National Park Fees: Island marine conservation park fees (to be paid directly in local currency).', 12),
            _inc_excluded('Insurance: International medical and travel insurance coverage.', 13),
        ],
    )
    return package, itinerary

def build_th_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-007'
    tour_code = 'TRG-HKT-KBV-HON-2026'
    title = 'PHUKET KRABI HONEYMOON PACKAGE Phuket • Phi Phi Islands • Krabi • Ao Nang Beach'
    duration = '05 Nights / 06 Days'
    slug = 'th-007-phuket-krabi-honeymoon-package-phuket-phi-phi-islands-krabi-ao-nang-beach'
    itin_slug = 'th-007-phuket-krabi-honeymoon-package-phuket-phi-phi-islands-krabi-ao-nang-beach-itinerary'
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
            _ph('Serial code TH-007 | TRAGUIN tour code TRG-HKT-KBV-HON-2026', 1),
            _ph('State / Country: Thailand | Category: Luxury Honeymoon Package', 2),
            _ph('Destinations: Phuket (3N) + Krabi', 3),
            _ph('Ideal for: Honeymooners, Couples, Romantic Seekers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Executive Chauffeur Van / Buffet Breakfast (CP) & Private Special Dinners Ignite your romantic narrative with the ultimate Phuket Krabi Honeymoon Package, precisely tailored by TRAGUIN', 7),
            _ph('TRAGUIN Signature Experience: Private custom speedboats and premium catamarans, completely', 8),
            _ph('Curated by TRAGUIN Experts: Safety-certified luxury romantic resorts featuring maximum isolation,', 9),
            _ph('Personalized Assistance: English-fluent dedicated local island guides to manage reservation priorities', 10),
            _ph('Luxury Transportation: Executive modern vans equipped with on-board cooling, music controls, and', 11)
        ],
        moods=['Luxury', 'Honeymoon', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='PHUKET KRABI HONEYMOON PACKAGE Phuket',
        overview="Phuket • Phi Phi Islands • Krabi • Ao Nang Beach 05 Nights / 06 Days Premium Romantic Twin-Island Escape SERIAL CODE: TH-007 TRAGUIN TOUR CODE: TRG-HKT-KBV- HON-2026 STATE / COUNTRY: Thailand CATEGORY: Luxury Honeymoon Package DURATION: 05 Nights / 06 Days DESTINATIONS: Phuket (3N) + Krabi (2N) IDEAL FOR: Honeymooners, Couples, Romantic Seekers BEST SEASON: November to May VEHICLE TYPE: Private Luxury Executive Chauffeur Van MEAL PLAN: Buffet Breakfast (CP) & Private Special Dinners Ignite your romantic narrative with the ultimate Phuket Krabi Honeymoon Package, precisely tailored by TRAGUIN to combine the vibrant coastal energy of Phuket with the serene limestone majesty of Krabi. Walk hand-in-hand along dramatic shores, sail past breathtaking landscapes, and craft unforgettable memories on a truly elite Luxury Thailand Holiday.\n\nTOUR OVERVIEW\nWelcome to your meticulously designed twin-island paradise vacation, curated explicitly by TRAGUIN for discerning couples who demand exceptional design and elite privileges. On this 6-day itinerary, you will move seamlessly between premium stays, enjoy private speed-craft charters to hidden sandbars, and sink into immersive experiences. TRAGUIN Curated Experience Note: From beautifully arranged honeymoon suites to a secluded beachfront candlelight dinner, every step is overseen by our on-ground destination management experts. Your romantic journey is protected by 24/7 dedicated assistance to ensure absolute luxury.\n\nWHY CHOOSE OUR LUXURY PHUKET & KRABI TWIN-ISLAND\nHOLIDAY? The combination of Phuket and Krabi stands as the world’s most iconic romantic corridor. Selecting a Thailand Honeymoon Package or an elegant Thailand Family Tour via TRAGUIN unlocks private access to hidden jewels. This itinerary optimizes highly searched tourism keywords for Google ranking, presenting an exquisite layout of the finest Phuket Sightseeing and Krabi Sightseeing spots. Witness top tourist places in Thailand: the crystal lagoon of Maya Bay, the iconic dramatic vertical cliffs of Krabi’s Railay Beach, and the high-fashion avenues of Patong. It is widely recognized as the absolute Best Time to Visit Thailand to discover popular Instagram locations, authentic local night bazaars, high-end couples' wellness treatments, and unforgettable romantic settings. TRAGUIN Signature Inclusions: Private beachfront candlelight dinner in Krabi, premium catamaran sunset cruise in Phuket, luxury private van transfers between regions, and specialized honeymoon room amenities. THE DEFINITIVE DAY-WISE ITINERARY",
        seo_title='TH-007 | PHUKET KRABI HONEYMOON PACKAGE Phuket | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-007 / TRG-HKT-KBV-HON-2026): Phuket (3N) + Krabi with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: PHUKET ARRIVAL & SUNSET TWILIGHT', 1),
            _ih('Day 02: PHI PHI ISLANDS ESCAPE', 2),
            _ih('Day 03: PHUKET HERITAGE & SPA INDULGENCE', 3),
            _ih('Day 04: PHUKET TO KRABI VIA SCENIC HIGHWAY', 4),
            _ih('Day 05: KRABI 4-ISLAND ADVENTURE', 5),
            _ih('Day 06: KRABI DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private custom speedboats and premium catamarans, completely', 7),
            _ih('Curated by TRAGUIN Experts: Safety-certified luxury romantic resorts featuring maximum isolation,', 8),
            _ih('Personalized Assistance: English-fluent dedicated local island guides to manage reservation priorities', 9)
        ],
        days=[
            _day(
                1,
                'PHUKET ARRIVAL & SUNSET TWILIGHT',
                (
                    "WELCOME TO THE ISLAND OF ROMANCE – UNVEILING PARADISE Your ultimate Phuket Krabi Honeymoon Package initiates flawlessly as you disembark at Phuket International Airport. Step through arrival gates to receive a warm Thai floral welcome arranged by your dedicated TRAGUIN tour manager. Avoid the stress of standard queues as your premium private vehicle delivers you to your handpicked luxury beachfront resort. Step into your ocean-facing honeymoon sanctuary, elegantly detailed with specialized floral architecture and a chilled complimentary bottle of premium sparkling wine. Relax together through the afternoon. At twilight, your private vehicle drives you along the scenic coastal paths to Promthep Cape, one of Thailand's most popular Instagram locations, to witness a gorgeous sunset painting the Andaman sea in soft golden tones. Sightseeing Included: Coastal scenic airport-to-resort private transit, Promthep Cape sunset view point. Evening Experience: Romantic welcome mocktails at an exclusive cliffside lounge overlooking Patong Beach."
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: Gourmet Multi-Cuisine Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PHI PHI ISLANDS ESCAPE',
                (
                    'EXCLUSIVE CATAMARAN SAILING TO PHI PHI ISLANDS & EMERALD LAGOONS Wake up to the gentle murmur of the tide and enjoy a lavish buffet breakfast. Today hosts a cornerstone Premium Thailand Experience: an intimate sailing journey to the globally celebrated Phi Phi Islands. Your private luxury catamaran waits to glide you away from public crowds, charting a custom course directly toward the iconic limestone amphitheater of Maya Bay. Swim and snorkel hand-in-hand within the calm, emerald waters of Pileh Lagoon, a pristine natural basin. Enjoy a premium, intimate beachfront seafood lunch organized away from commercial zones. Spend your afternoon wandering the soft white sands of Bamboo Island or discovering the mysterious shapes of Viking Cave, taking stunning couple photos at key photography points before sailing back under a gorgeous sunset. Sightseeing Included: Maya Bay, Pileh Lagoon, Bamboo Island beach access, Viking Cave exploration. Optional Activities: Professional underwater photography session during snorkeling over live coral reefs.'
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Beachside Gourmet Lunch',
                ],
            ),
            _day(
                3,
                'PHUKET HERITAGE & SPA INDULGENCE',
                (
                    "COLONIAL OLD TOWN CULTURE & AN IMMERSIVE COUPLES SPA RETREAT Embrace a slow-paced morning starting with a beautiful floating breakfast inside your pool villa or a sea-view breakfast pavilion. Begin your comprehensive Phuket Sightseeing tour by driving to the historic center of Old Phuket Town. Walk hand-in-hand past beautiful Sino-Portuguese colonial mansions, vibrant street murals, and charming independent boutiques perfect for picking up local souvenirs. In the afternoon, transition to absolute relaxation. TRAGUIN has reserved an exclusive 120-minute couple’s aroma-spa therapy session within an award-winning luxury sanctuary. Melt away travel fatigue with exotic Thai herbal wraps and deep-tissue oil massages. Spend your evening enjoying the chic beach clubs of Bang Tao beach, relaxing to chilled house beats right at the water's edge. Sightseeing Included: Old Phuket Town Heritage Quarter, Wat Chalong Monastic Shrine, Karon Viewpoint. Evening Experience: VVIP access to a premium oceanfront beach club for sunset dining."
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Thai Fine Dining Evening Platter',
                ],
            ),
            _day(
                4,
                'PHUKET TO KRABI VIA SCENIC HIGHWAY',
                (
                    "TRANSIT TO THE LAND OF VERTICAL CLIFFS & AAO NANG NIGHTS Following a leisurely breakfast, check out of your Phuket resort. Your private luxury van picks you up for a smooth, exceptionally scenic journey past rubber plantations and coastal villages heading into Krabi. This land is universally adored for its staggering limestone towers rising straight from emerald waters—making it a centerpiece for any true Luxury Thailand Holiday. Arrive at your premium resort nestled adjacent to the dramatic Ao Nang cliffs. After a relaxed check-in, the rest of your afternoon is free to enjoy your resort's luxury infinity pool. As the evening sets in, your driver delivers you to the vibrant Ao Nang walking street, full of vibrant cafes, local markets, and great photography opportunities along the rocky shoreline. Sightseeing Included: Cross-province private highway driving tour, Ao Nang bay orientation stroll. Evening Experience: Intimate walk down Ao Nang beach followed by a candlelit seaside Italian dinner."
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Cliffside or Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Curated Sunset Dinner',
                ],
            ),
            _day(
                5,
                'KRABI 4-ISLAND ADVENTURE',
                (
                    'MYSTICAL SEA LAGOONS, RAILAY BEACH & PRIVATE CANDLELIGHT FINALE Today unveils the crowning beauty of your Krabi Sightseeing itinerary. After breakfast, a private speed-craft picks you up from the shore for an island-hopping voyage across Krabi’s iconic 4-Islands. Visit Phra Nang Cave Beach, renowned for its sacred princess shrine and towering rock face climbers. Then explore Tup Island, where a unique natural sandbar emerges at low tide, allowing you to walk between islands on crystal water. Cruise onwards to Poda Island for a relaxing beach swim, before stopping near Chicken Island for excellent snorkeling among multi-colored schools of fish. Return to the resort to refresh for your final night. TRAGUIN has arranged a signature surprise: an intimate private beachfront candlelight dinner set in a secluded cove. Toast your future together under a beautiful sky as gentle waves roll in. Sightseeing Included: Phra Nang Cave, Tup Island Sandbar, Poda Island, Chicken Island reefs. Optional Activities: Sunset rock-climbing lesson or sea-kayaking through hidden mangrove forests. Evening Experience: Signature TRAGUIN Grand Finale Beachfront Candlelight Dinner.'
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Cliffside or Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Beachside Private Box Dinner',
                ],
            ),
            _day(
                6,
                'KRABI DEPARTURE',
                (
                    "CHERISHING ROMANTIC MEMORIES BEYOND DESTINATIONS Wake up to a quiet morning in beautiful Krabi, enjoying a long breakfast overlooking the tropical gardens. Take a final walk on the soft sand of Ao Nang beach or relax by the resort's pool to reflect on your incredible journey together. At the designated hour, your private luxury van arrives to transfer you comfortably to Krabi International Airport for your flight back home. Your premium Phuket Krabi Honeymoon Package concludes beautifully, leaving your hearts full of unforgettable memories and a love story crafted to perfection by TRAGUIN. Sightseeing Included: Private luxury airport departure transfer."
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Phuket Kamala Beach Ocean Room (BB) Ao Nang Cliff Beach Resort Ocean View Room (BB)',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Novotel Phuket Kamala Beach Ocean Room (BB) Ao Nang Cliff Beach Resort Ocean View Room (BB)',
            ),
            _hotel(
                'Amari Phuket Superior Ocean Wing (BB) Centara Grand Beach Resort Krabi Deluxe Garden View (BB)',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Amari Phuket Superior Ocean Wing (BB) Centara Grand Beach Resort Krabi Deluxe Garden View (BB)',
            ),
            _hotel(
                'The Shore at Katathani Seaview Pool Villa (BB) Rayavadee Krabi Resort Deluxe Pavilion Suite (BB)',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Shore at Katathani Seaview Pool Villa (BB) Rayavadee Krabi Resort Deluxe Pavilion Suite (BB)',
            ),
            _hotel(
                'Sri Panwa Luxury Pool Villa Resort Luxury Ocean Suite Villa (BB) Phulay Bay, a Ritz-Carlton Reserve Reserve Pavilion Pool Villa (BB)',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Sri Panwa Luxury Pool Villa Resort Luxury Ocean Suite Villa (BB) Phulay Bay, a Ritz-Carlton Reserve Reserve Pavilion Poo',
            )
        ],
        inclusions=[
            _inc_included('Daily Breakfast: 5 International Buffet Breakfast layouts.', 1),
            _inc_included('Romantic Add-ons: Specialized honeymoon bed styling, welcome wine bottle, and fruit platters.', 2),
            _inc_included('Private Vehicles: Private air-conditioned luxury van for all point-to-point tours and transfers.', 3),
            _inc_included('Phuket Cruises: Premium Catamaran day tour across the Phi Phi Islands with lunch.', 4),
            _inc_included("Krabi Cruises: Private speed-craft charter for Krabi's 4-Islands exploration.", 5),
            _inc_included('Special Dining: 1 Private Beachfront Candlelight Dinner under the stars in Krabi.', 6),
            _inc_included('International Flights: Main airline tickets connecting home country with Thailand.', 7),
            _inc_excluded('Accommodation: 05 Nights stay in handpicked romantic hotels.', 8),
            _inc_excluded('Visa Costs: Thailand Visa-on-Arrival or E-Visa processing fees.', 9),
            _inc_excluded('National Park Entry: Marine conservation island entry fees (payable directly on site).', 10),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, mini-bar billing, and tips.', 11),
            _inc_excluded('Insurance Cover: Overseas comprehensive medical and trip cancellation insurance.', 12),
        ],
    )
    return package, itinerary

def build_th_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-008'
    tour_code = 'TRG-THA-ROM-2026'
    title = 'THAILAND ROMANCE PACKAGE Phuket • Phi Phi Islands • Krabi • Bangkok'
    duration = '06 Nights / 07 Days'
    slug = 'th-008-thailand-romance-package-phuket-phi-phi-islands-krabi-bangkok'
    itin_slug = 'th-008-thailand-romance-package-phuket-phi-phi-islands-krabi-bangkok-itinerary'
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
            _ph('Serial code TH-008 | TRAGUIN tour code TRG-THA-ROM-2026', 1),
            _ph('State / Country: Thailand | Category: Luxury Honeymoon Package', 2),
            _ph('Destinations: Phuket (2N) + Krabi', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Executive Sedans / Vans / Buffet Breakfast (CP) & Specialized Dinners Begin your journey together with the Best Thailand Honeymoon Package, elegantly curated by TRAGUIN. Immerse your lo', 7),
            _ph('TRAGUIN Signature Experience: Private custom speedboats and premium catamarans, completely', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked romantic properties featuring maximum isolation, infinity', 9),
            _ph('Personalized Assistance: English-fluent dedicated local island guides to manage reservation priorities', 10),
            _ph('Luxury Transportation: Executive modern vans equipped with on-board cooling, music controls, and', 11)
        ],
        moods=['Luxury', 'Honeymoon', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='THAILAND ROMANCE PACKAGE Phuket',
        overview="TOUR OVERVIEW\nWelcome to a bespoke romantic journey spanning across Thailand’s most premium vacation hubs. Hand- tailored by the romance experts at TRAGUIN, this signature 7-day multi-destination itinerary seamlessly weaves absolute private luxury with unforgettable memories. Couples will indulge in world-class handpicked hotels, private premium vehicle transfers, and highly exclusive beach and river cruises. TRAGUIN Curated Experience Note: Your romantic getaway is enhanced with priority scheduling, VIP fast- track entry at iconic attractions, and premium culinary surprises. Trust our 24/7 on-ground concierge network to provide elite assistance at every step. THE ALLURE OF A LUXURY THAILAND HOLIDAY Thailand remains the undisputed masterpiece of tropical romance, offering couples an unparalleled mix of serene island privacy and pulsating city style. When selecting one of our high-end TRAGUIN Thailand Packages, you rise above ordinary itineraries. This proposal features top searched keywords for Google ranking, showcasing an elite selection of Top Tourist Places in Thailand. Uncover iconic Thailand Sightseeing destinations: the golden beaches of Phuket, the secluded coves of Krabi's Railay Bay, and the historic temples of Bangkok. It is universally considered the Best Time to Visit Thailand to experience highly sought-after popular Instagram locations, high-fashion retail markets, authentic local street cafes, and deep cultural milestones wrapped in absolute opulence. TRAGUIN Honeymoon Highlights: Exclusive private speedboat island-hopping in Phuket, private beachfront candlelight dinner under the stars in Krabi, a 5-star luxury river dinner cruise in Bangkok, and dedicated premium amenities. THE DEFINITIVE DAY-WISE ITINERARY",
        seo_title='TH-008 | THAILAND ROMANCE PACKAGE Phuket | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Thailand package (TH-008 / TRG-THA-ROM-2026): Phuket (2N) + Krabi with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: PHUKET ARRIVAL & ROMANTIC SUNSET', 1),
            _ih('Day 02: PHI PHI ISLANDS ADVENTURE', 2),
            _ih('Day 03: PHUKET TO KRABI TRANSIT', 3),
            _ih('Day 04: KRABI 4-ISLAND EXPEDITION', 4),
            _ih('Day 05: KRABI TO BANGKOK FLY-IN', 5),
            _ih('Day 06: BANGKOK ANCIENT TEMPLES & HIGH-FASHION RETREAT', 6),
            _ih('Day 07: BANGKOK DEPARTURE', 7),
            _ih('TRAGUIN Signature Experience: Private custom speedboats and premium catamarans, completely', 8),
            _ih('Curated by TRAGUIN Experts: Handpicked romantic properties featuring maximum isolation, infinity', 9),
            _ih('Personalized Assistance: English-fluent dedicated local island guides to manage reservation priorities', 10)
        ],
        days=[
            _day(
                1,
                'PHUKET ARRIVAL & ROMANTIC SUNSET',
                (
                    'WELCOME TO PARADISE – UNVEILING LUXURY AND ROMANCE Your spectacular Luxury Thailand Holiday begins the moment you step off your plane at Phuket International Airport. You will receive a traditional Thai floral welcome from your private TRAGUIN tour representative. Avoid the hassle of airport queues as you are escorted directly to your air-conditioned private luxury vehicle for a smooth transfer to your handpicked premium beachfront resort. Check into your sea-view honeymoon sanctuary, detailed with elegant custom floral setups and a complimentary bottle of sparkling wine. Spend the afternoon relaxing by the infinity pool. At twilight, your private vehicle drives you along the dramatic coastline to Phromthep Cape, one of the most popular Instagram locations in Thailand, to watch a breathtaking sunset melt into the Andaman Sea, capturing wonderful initial photos together. Sightseeing Included: Private premium airport-to-resort transfer, Phromthep Cape sunset viewpoint. Evening Experience: Welcome mocktails at a high-end cliffside lounge overlooking the bay.'
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: Curated International Buffet Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PHI PHI ISLANDS ADVENTURE',
                (
                    'EXCLUSIVE SPEEDBOAT CRUISE TO PHI PHI ISLANDS & MAYA BAY Savor a beautiful breakfast before starting an incredible island adventure. Skip the large commercial groups as TRAGUIN arranges an exclusive, high-speed private speedboat to explore the legendary Phi Phi Islands. Cruise across turquoise waters directly to Maya Bay, an absolute highlight of Phuket Sightseeing, surrounded by colossal rock formations. Swim hand-in-hand in the emerald waters of Pileh Lagoon, a beautiful natural limestone pool. Savor an exquisite, private beachfront gourmet lunch organized away from commercial zones. Spend the afternoon walking the white sands of Bamboo Island or discovering the historic Viking Cave. Capture beautiful memories at premium photography points before cruising back under a golden sky. Sightseeing Included: Maya Bay entry, Pileh Lagoon swimming, Bamboo Island beach access, Viking Cave view. Optional Activities: Deep-sea tandem scuba diving or private sea-kayaking through hidden caves.'
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Beachside Island Lunch',
                ],
            ),
            _day(
                3,
                'PHUKET TO KRABI TRANSIT',
                (
                    "SCENIC COASTAL DRIVE & ROMANTIC AO NANG HIGHLIGHTS Enjoy a relaxed morning breakfast, perhaps opting for a romantic floating breakfast inside your pool villa. Check out of your resort as your private luxury van prepares for a scenic drive past rubber plantations and coastal villages heading into Krabi. Krabi is adored globally for its staggering limestone towers rising straight from emerald waters. Arrive at your premium resort nestled adjacent to the dramatic Ao Nang cliffs. After a relaxed check-in, the afternoon is free to enjoy your resort's luxury infinity pool. As the evening sets in, your driver delivers you to the vibrant Ao Nang walking street, full of local food, boutique markets, and great photography opportunities along the rocky shoreline. Sightseeing Included: Cross-province scenic highway private drive, Ao Nang coastline drive. Evening Experience: Strolling down the sands of Ao Nang beach followed by a candlelit beachside dinner."
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Cliffside or Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Curated Sunset Dinner',
                ],
            ),
            _day(
                4,
                'KRABI 4-ISLAND EXPEDITION',
                (
                    'MYSTICAL SANDBARS, RAILAY BEACH & PRIVATE BEACHFRONT DINNER Today unveils the crowning beauty of your Krabi Sightseeing itinerary. After breakfast, a private speed- craft picks you up from the shore for an island-hopping voyage across Krabi’s iconic 4-Islands. Visit Phra Nang Cave Beach, renowned for its sacred princess shrine and towering rock face climbers. Then explore Tup Island, where a unique natural sandbar emerges at low tide, allowing you to walk between islands on crystal water. Cruise onwards to Poda Island for a relaxing beach swim, before stopping near Chicken Island for excellent snorkeling among multi-colored schools of fish. Return to the resort to refresh for your final night. TRAGUIN has arranged a signature surprise: an intimate private beachfront candlelight dinner set in a secluded cove. Toast your future together under a beautiful sky as gentle waves roll in. Sightseeing Included: Phra Nang Cave, Tup Island Sandbar, Poda Island, Chicken Island reefs. Optional Activities: Sunset rock-climbing lesson or sea-kayaking through hidden mangrove forests. Evening Experience: Signature TRAGUIN Grand Finale Beachfront Candlelight Dinner.'
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Cliffside or Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Beachside Private Box Dinner',
                ],
            ),
            _day(
                5,
                'KRABI TO BANGKOK FLY-IN',
                (
                    'TRANSIT TO THE CITY OF ANGELS & LUXURY CHAO PHRAYA RIVER DINNER CRUISE After a leisurely breakfast, check out of your resort. Your private vehicle transfers you to Krabi Airport for your domestic flight to Bangkok. Upon arrival in the capital, your waiting private premium vehicle provides a smooth transfer to your high-end riverside hotel overlooking the majestic River of Kings. Bangkok is the epicenter of culture and high-fashion retail. In the evening, dress in elegant resort wear for a classic Premium Thailand Experience: a 5-star luxury dinner cruise aboard the Grand Pearl Cruise liner on the Chao Phraya River. Glide past the brilliantly illuminated Grand Palace and Wat Arun (The Temple of Dawn) while enjoying a sumptuous international buffet, live jazz music, and classical Thai performances. Sightseeing Included: Domestic flight transit, Bangkok city drive, River Cruise tour. Evening Experience: 5-Star Luxury Chao Phraya River Dinner Cruise with live performances.'
                ),
                [
                    'Overnight Stay: Bangkok (Ultra-Luxury Riverside Hotel)',
                    'Meals Included: International Buffet Breakfast & Premium Cruise Dinner',
                ],
            ),
            _day(
                6,
                'BANGKOK ANCIENT TEMPLES & HIGH-FASHION RETREAT',
                (
                    "GOLDEN SIAMESE TEMPLES TO ICONSIAM WATERFRONT LUXURY Dedicate today to deep cultural exploration and world-class retail luxury. Following breakfast, start a descriptive Bangkok Sightseeing temple tour. Visit Wat Traimit to view the astounding Golden Buddha—a 5.5-ton solid gold statue dating back to the Sukhothai period. Next, explore Wat Pho, home to the monumental 46-meter Reclining Buddha covered in exquisite gold leaf. In the afternoon, your private vehicle drops you at ICONSIAM, the crown jewel of Bangkok's shopping malls. Featuring an indoor floating market, high-fashion luxury brand flagships, and phenomenal waterfront views, it is an unparalleled location for premium shopping. Find exquisite silks, high-end electronics, and unique local designer pieces to commemorate your trip. Sightseeing Included: Wat Traimit (Golden Buddha), Wat Pho (Reclining Buddha), ICONSIAM Luxury Mall. Optional Activities: Mahanakhon SkyWalk glass tray experience at 314 meters above the city skyline."
                ),
                [
                    'Overnight Stay: Bangkok (Ultra-Luxury Riverside Hotel)',
                    'Meals Included: International Buffet Breakfast & Premium Local Thai Dining Lunch',
                ],
            ),
            _day(
                7,
                'BANGKOK DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS Enjoy your final decadent buffet breakfast at your luxury hotel, capturing a final round of panoramic couple photos overlooking the bustling Chao Phraya River. Depending on your flight departure schedule, the morning is yours to relax, squeeze in last-minute souvenir shopping, or enjoy a final authentic Thai iced tea. At the designated hour, your professional, chauffeured vehicle will arrive to provide a seamless private transfer to Suvarnabhumi International Airport for your return flight home. As you board your aircraft, look back on an exceptional collection of curated experiences, breathtaking landscapes, and unforgettable family memories crafted beautifully by TRAGUIN. Your premium tour concludes, leaving you with stories to pass down through generations. Sightseeing Included: Private luxury airport departure transfer.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Phuket Resort Superior Ocean Room Ao Nang Cliff Beach Resort Ocean View Room The Sukosol Bangkok Premier Room',
                'Multi-city Thailand',
                '6N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Novotel Phuket Resort Superior Ocean Room Ao Nang Cliff Beach Resort Ocean View Room The Sukosol Bangkok Premier Room',
            ),
            _hotel(
                'Phuket Marriott, Merlin Beach Pool View Room Centara Grand Beach Krabi Deluxe Garden View Avani+ Riverside Bangkok Hotel Avani River View Room',
                'Multi-city Thailand',
                '6N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Phuket Marriott, Merlin Beach Pool View Room Centara Grand Beach Krabi Deluxe Garden View Avani+ Riverside Bangkok Hotel',
            ),
            _hotel(
                'The Westin Siray Bay Resort Luxury Seaview Suite Rayavadee Krabi Resort Deluxe Pavilion Suite Shangri-La Bangkok Deluxe Horizon River Room',
                'Multi-city Thailand',
                '6N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Westin Siray Bay Resort Luxury Seaview Suite Rayavadee Krabi Resort Deluxe Pavilion Suite Shangri-La Bangkok Deluxe ',
            ),
            _hotel(
                'Anantara Layan Phuket Resort Deluxe Pool Villa Phulay Bay, Ritz-Carlton Reserve Pavilion Pool Villa Mandarin Oriental, Bangkok Deluxe Chao Phraya Suite',
                'Multi-city Thailand',
                '6N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Anantara Layan Phuket Resort Deluxe Pool Villa Phulay Bay, Ritz-Carlton Reserve Pavilion Pool Villa Mandarin Oriental, B',
            )
        ],
        inclusions=[
            _inc_included('Handpicked premium accommodation as per selected hotel tier', 1),
            _inc_included('Private luxury vehicle transfers and sightseeing as per itinerary', 2),
            _inc_included('Daily buffet breakfast and curated meals as specified', 3),
            _inc_included('VIP airport fast-track reception and dedicated TRAGUIN concierge support', 4),
            _inc_excluded('PACKAGE INCLUSIONS', 5),
        ],
    )
    return package, itinerary

def build_th_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-009'
    tour_code = 'TRG-THA-FEM-2026'
    title = 'GIRLS TRIP THAILAND PACKAGE Bangkok • Pattaya • Coral Island Escape'
    duration = '05 Nights / 06 Days'
    slug = 'th-009-girls-trip-thailand-package-bangkok-pattaya-coral-island-escape'
    itin_slug = 'th-009-girls-trip-thailand-package-bangkok-pattaya-coral-island-escape-itinerary'
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
            _ph('Serial code TH-009 | TRAGUIN tour code TRG-THA-FEM-2026', 1),
            _ph('State / Country: Thailand | Category: Girls Trip Thailand / Female Only', 2),
            _ph('Destinations: Pattaya (2N) + Bangkok', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Safe Luxury Van with Women-Friendly Assistance / Buffet Breakfast (CP), Chic Cafes & Sunset Dinners Gather your closest girlfriends for the ultimate Girls Trip Thailand, an exceptional itinera', 7),
            _ph('TRAGUIN Signature Experience: Private custom speedboats and exclusive cafe routes, completely', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium hotels located centrally next to major lifestyle', 9),
            _ph('Personalized Assistance: English-fluent dedicated local island coordinators to manage reservation', 10),
            _ph('Luxury Transportation: Executive modern vehicles equipped with cooling, onboard Wi-Fi connectivity,', 11)
        ],
        moods=['Luxury', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='GIRLS TRIP THAILAND PACKAGE Bangkok',
        overview="Bangkok • Pattaya • Coral Island Escape 05 Nights / 06 Days All-Female Luxury Getaway SERIAL CODE: TH-009 TRAGUIN TOUR CODE: TRG-THA-FEM-2026 STATE / COUNTRY: Thailand CATEGORY: Girls Trip Thailand / Female Only DURATION: 05 Nights / 06 Days DESTINATIONS: Pattaya (2N) + Bangkok (3N) IDEAL FOR: Girls Gangs, Solo Female Groups, SistersBEST SEASON: Year-round (Best: November to April) VEHICLE TYPE: Private Safe Luxury Van with Women-Friendly Assistance MEAL PLAN: Buffet Breakfast (CP), Chic Cafes & Sunset Dinners Gather your closest girlfriends for the ultimate Girls Trip Thailand, an exceptional itinerary beautifully curated by TRAGUIN to perfectly fuse high-end shopping, glamorous nightlife, decadent wellness spa sessions, and stunning coastal scenery. From absolute safety protocols to breathtaking landscapes, prepare for a Luxury Thailand Holiday full of laughter and unforgettable memories.\n\nTOUR OVERVIEW\nWelcome to your meticulously designed Girls Trip Thailand escape, specifically structured for women who want to experience the vibrant pulse of Thailand with complete comfort, privacy, and style. On this 6-day holiday, TRAGUIN provides premium stays at highly rated lifestyle hotels, private secure vehicles, and curated experiences designed around cafe-hopping, high-fashion styling, and iconic landmarks. TRAGUIN Curated Experience Note: Your group's security and luxury are our absolute priorities. From female-friendly local coordinators to custom-picked night bazaar trails and elite rooftop lounge tables, your travel circle will enjoy a completely flawless and immersive holiday experience.\n\nWHY CHOOSE OUR PREMIUM GIRLS TRIP THAILAND PACKAGE?\nThailand is the ultimate destination for an all-female getaway, seamlessly offering everything from tropical white-sand beaches to world-class retail therapy. By choosing a dedicated Thailand Family Tour variant or our specialized female-only itinerary through TRAGUIN, you gain access to safe, exclusive travel benefits. This proposal targets top searched keywords for Google ranking, ensuring the ultimate showcase of the best Thailand Sightseeing destinations. Uncover iconic attractions: the high-octane beachfront energy of Pattaya, the turquoise clear water of Coral Island, and the beautiful royal palaces of Bangkok. It is the absolute Best Time to Visit Thailand to explore popular Instagram locations, chic rooftop cafes, local floating markets, and award-winning luxury spas, creating a perfect Premium Thailand Experience. TRAGUIN Girls Trip Exclusives: Private speed-craft island excursion with beachside mocktails, premium front-row seats at the Alcazar Cabaret Show, sunset entry to the spectacular Mahanakhon SkyWalk, and an authentic 120-minute Thai spa treatment. THE FUN & GLAMOROUS DAY-WISE ITINERARY",
        seo_title='TH-009 | GIRLS TRIP THAILAND PACKAGE Bangkok | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-009 / TRG-THA-FEM-2026): Pattaya (2N) + Bangkok with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BANGKOK & TRANSIT TO PATTAYA', 1),
            _ih('Day 02: CORAL ISLAND EXCURSION & CABARET GLAMOUR', 2),
            _ih('Day 03: PATTAYA TO BANGKOK & ROOFTOP CELEBRATION', 3),
            _ih('Day 04: THE ICONIC FLOATING MARKET & CHIC CAFE TRAIL', 4),
            _ih('Day 05: HIGH-FASHION SHOPPING & LUXURY SPA RETREAT', 5),
            _ih('Day 06: BANGKOK DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private custom speedboats and exclusive cafe routes, completely', 7),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium hotels located centrally next to major lifestyle', 8),
            _ih('Personalized Assistance: English-fluent dedicated local island coordinators to manage reservation', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BANGKOK & TRANSIT TO PATTAYA',
                (
                    "WELCOME TO THE LAND OF SMILES – THE GIRLS' GETAWAY BEGINS Your highly anticipated Girls Trip Thailand begins perfectly the moment your group arrives at Bangkok's Suvarnabhumi Airport. A warm Thai welcome coordinates seamlessly with your private TRAGUIN travel concierge, who will escort you to your air-conditioned private luxury van. Enjoy a relaxed, music-filled drive along the coast as you head down to the lively resort town of Pattaya. Check into your handpicked premium high-rise hotel featuring stunning ocean views. Take some time to freshen up, unpack your outfits, and take your first group pictures by the rooftop infinity pool. In the evening, your private van takes you to a chic beachfront restaurant for a welcome dinner filled with local seafood, great cocktails, and beautiful panoramic sunset views. Sightseeing Included: Private airport pickup and scenic highway transit to Pattaya, beach road drive. Evening Experience: Group welcome dinner at an upscale beachfront lounge with great photo points."
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Ocean View Hotel)',
                    'Meals Included: Curated Multi-Cuisine Welcome Dinner',
                ],
            ),
            _day(
                2,
                'CORAL ISLAND EXCURSION & CABARET GLAMOUR',
                (
                    'SUN-KISSED BEACHES, PRIVATE SPEEDBOAT CRUISE & ALCAZAR VIP Savor a decadent buffet breakfast before picking out your best beach wear. Today features a classic tropical island adventure: an exclusive private speedboat cruise to Koh Larn, beautifully known as Coral Island. Skip the large commercial tour groups as your private boat takes you directly to a quieter, pristine stretch of white sand, showcasing Thailand’s breathtaking landscapes. The day is tailored for pure fun. Take part in exciting parasailing flights or a fast banana boat ride over the waves. Relax on beach loungers with fresh coconut water, creating unforgettable memories together. Return to the mainland for a delicious lunch. In the evening, dress up for front-row VIP seats at the iconic Alcazar Cabaret Show, a world-famous mix of grand costumes, dance, and state-of-the-art theatrical production. Sightseeing Included: Private Speedboat to Coral Island, beach active access, VIP entry to Alcazar Show. Optional Activities: Undersea walking tour or custom jet-skiing across the bay under certified guidance.'
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Ocean View Hotel)',
                    'Meals Included: International Buffet Breakfast & Premium Seafood Lunch',
                ],
            ),
            _day(
                3,
                'PATTAYA TO BANGKOK & ROOFTOP CELEBRATION',
                (
                    'GOLDEN SHINES, RIVER TRANSIT & GLAMOROUS SKYLINE DINING Check out of Pattaya after breakfast as your private vehicle drives your group back into the historical capital, Bangkok. Your first stop features classic Bangkok Sightseeing at Wat Traimit to view the magnificent solid Golden Buddha temple. Next, visit Wat Pho to see the historic 46-meter Reclining Buddha temple, covered in gold leaf—providing a wonderful background for group photography. Arrive at your premium lifestyle city hotel. In the late afternoon, head up to the Mahanakhon SkyWalk, standing 314 meters above the streets on a massive glass tray—consistently named one of the top popular Instagram locations in Thailand. End your night with VIP tables reserved at a premium rooftop lounge, celebrating your friendship over delicious dining and spectacular skyline views. Sightseeing Included: Wat Traimit, Wat Pho temple tour, Mahanakhon SkyWalk VIP entry ticket. Evening Experience: Premium cocktails and high-fashion dining at a top-tier sky lounge.'
                ),
                [
                    'Overnight Stay: Bangkok (Premium Lifestyle City Hotel)',
                    'Meals Included: International Buffet Breakfast & Traditional Thai Evening Tasting Platter',
                ],
            ),
            _day(
                4,
                'THE ICONIC FLOATING MARKET & CHIC CAFE TRAIL',
                (
                    "DAMNOEN SADUAK RIDE & INSTAGRAM-WORTHY CAFE HOPPING Today offers a beautiful mix of local culture and high-end aesthetic dining. Wake up early for a private drive to the world-famous Damnoen Saduak Floating Market. Board a traditional wooden longtail boat to glide through narrow canals filled with local vendors selling fresh fruits, flowers, and handmade crafts right from their boats —making it a top searched experience. Return to the city center for a custom-tailored TRAGUIN Cafe Hop. Your guide will navigate you through Bangkok's trendiest neighborhoods (like Ari or Thonglor) to visit stunning, plant-filled boutique cafes. Enjoy artisan lattes, custom pastries, and excellent aesthetic photo opportunities. Spend your evening exploring the lively stalls of the Jodd Fairs Night Bazaar, a fantastic spot for stylish streetwear, unique accessories, and trendy local snacks. Sightseeing Included: Damnoen Saduak Floating Market boat tour, Ari/Thonglor design quarters, Jodd Fairs. Optional Activities: An evening private luxury canal boat cruise with wine and tapas."
                ),
                [
                    'Overnight Stay: Bangkok (Premium Lifestyle City Hotel)',
                    'Meals Included: International Buffet Breakfast & Selected Cafe Lunch Menu',
                ],
            ),
            _day(
                5,
                'HIGH-FASHION SHOPPING & LUXURY SPA RETREAT',
                (
                    "RETAIL THERAPY AT ICONSIAM & A 120-MINUTE REJUVENATION RETREAT Dedicate today to world-class shopping and ultimate body pampering. After breakfast, head to ICONSIAM, the crown jewel of Bangkok's shopping malls. Featuring an indoor floating market, incredible waterfront spaces, and massive luxury brand flagship stores, it is an unparalleled location for premium shopping. Find unique silk garments, boutique cosmetics, and local designer items. In the afternoon, escape the city bustle into a premier luxury wellness spa. TRAGUIN has reserved an exclusive 120-minute relaxation package for your girls' group. Indulge side-by-side in traditional Thai herbal steam rooms, aromatic body scrubs, and therapeutic body oil massages. Conclude your final night celebrating with an elegant dinner overlooking the Chao Phraya River. Sightseeing Included: ICONSIAM waterfront lifestyle destination, Siam Paragon shopping district. Evening Experience: Farewell dinner party at a premium riverside restaurant with live music."
                ),
                [
                    'Overnight Stay: Bangkok (Premium Lifestyle City Hotel)',
                    'Meals Included: International Buffet Breakfast & 3-Course Riverfront Farewell Dinner',
                ],
            ),
            _day(
                6,
                'BANGKOK DEPARTURE',
                (
                    "CHERISHING MEMORIES BEYOND DESTINATIONS Enjoy your final decadent buffet breakfast at your hotel, taking a final round of group photos by the pool. Depending on your flight departure schedule, spend your morning relaxing at the hotel, visiting a nearby local market, or grabbing a final cup of Thai iced tea with your friends. At the designated hour, your professional private van will arrive to provide a seamless private transfer to Suvarnabhumi International Airport for your return flight home. As you board your aircraft, look back on an exceptional collection of curated experiences, breathtaking landscapes, and unforgettable memories beautifully crafted by TRAGUIN. Your premium girls' trip concludes, leaving your friend circle closer than ever before. Sightseeing Included: Private luxury airport departure transfer."
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Pattaya Rescue Bay Superior Sea View Room The Sukosol Bangkok Premier Corner Room',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Novotel Pattaya Rescue Bay Superior Sea View Room The Sukosol Bangkok Premier Corner Room',
            ),
            _hotel(
                'Amari Pattaya Resort Deluxe Ocean Horizon Room Grande Centre Point Terminal 21 Premium Deluxe Room',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Amari Pattaya Resort Deluxe Ocean Horizon Room Grande Centre Point Terminal 21 Premium Deluxe Room',
            ),
            _hotel(
                'Hilton Pattaya Hotel Executive Ocean Front Room Avani+ Riverside Bangkok Hotel Avani Panorama River Room',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Hilton Pattaya Hotel Executive Ocean Front Room Avani+ Riverside Bangkok Hotel Avani Panorama River Room',
            ),
            _hotel(
                'Grande Centre Point Space Pattaya Space Premium Balcony Suite W Bangkok / Shangri-La Bangkok Marvelous Suite / Horizon Club Room',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Grande Centre Point Space Pattaya Space Premium Balcony Suite W Bangkok / Shangri-La Bangkok Marvelous Suite / Horizon C',
            )
        ],
        inclusions=[
            _inc_included('Daily Meals: 5 International Buffet Breakfasts, 2 Premium Lunches, 2 Curated Dinners.', 1),
            _inc_included('Private Vehicles: Dedicated safe luxury van with an experienced driver for all tours.', 2),
            _inc_included('Pattaya Cruise: Private Speedboat to Coral Island with parasailing and banana boat rides.', 3),
            _inc_included('VIP Sightseeing: Premium seats at Alcazar Cabaret Show and Mahanakhon SkyWalk entry.', 4),
            _inc_included('Local Tours: Longtail boat ride through Damnoen Saduak Floating Market.', 5),
            _inc_included('Wellness: 120-minute Premium Group Luxury Spa & Massage session.', 6),
            _inc_included('TRAGUIN Support: 24/7 dedicated local female-friendly on-ground concierge assistance.', 7),
            _inc_included('Airfare: International flight tickets from your home country.', 8),
            _inc_excluded('Accommodation: 05 Nights stay in handpicked premium hotels.', 9),
            _inc_excluded('Visa Fees: Thailand Visa-on-Arrival or fast-track electronic visa processing.', 10),
        ],
    )
    return package, itinerary

def build_th_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-010'
    tour_code = 'TRG-HKT-LAD-2026'
    title = 'PHUKET LADIES ESCAPE Phuket • Patong • Phi Phi Islands • James Bond Island'
    duration = '05 Nights / 06 Days'
    slug = 'th-010-phuket-ladies-escape-phuket-patong-phi-phi-islands-james-bond-island'
    itin_slug = 'th-010-phuket-ladies-escape-phuket-patong-phi-phi-islands-james-bond-island-itinerary'
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
            _ph('Serial code TH-010 | TRAGUIN tour code TRG-HKT-LAD-2026', 1),
            _ph('State / Country: Thailand | Category: Girls Trip Thailand / Female Only', 2),
            _ph('Destinations: Phuket Premium Island', 3),
            _ph("Ideal for: Women's Groups, Girl Gangs, Female Solo Groups", 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Safe Luxury Van with Dedicated Driver Assistance / Buffet Breakfast (CP), Oceanfront Lunches & Sunset Dinners Escape to island paradise with the ultimate Girls Trip Thailand, an exquisite itin', 7),
            _ph('TRAGUIN Signature Experience: Private custom speedboats and premium catamarans, completely', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium beachfront hotels located centrally next to', 9),
            _ph('Personalized Assistance: English-fluent dedicated local island guides to manage reservation', 10)
        ],
        moods=['Family', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='PHUKET LADIES ESCAPE Phuket',
        overview="05 Nights / 06 Days All-Female Luxury Island Getaway SERIAL CODE: TH-010 TRAGUIN TOUR CODE: TRG-HKT-LAD-2026 STATE / COUNTRY: Thailand CATEGORY: Girls Trip Thailand / Female Only DURATION: 05 Nights / 06 Days DESTINATIONS: Phuket Premium Island Escape (5N) IDEAL FOR: Women's Groups, Girl Gangs, Female Solo Groups BEST SEASON: November to May VEHICLE TYPE: Private Safe Luxury Van with Dedicated Driver Assistance MEAL PLAN: Buffet Breakfast (CP), Oceanfront Lunches & Sunset Dinners Escape to island paradise with the ultimate Girls Trip Thailand, an exquisite itinerary uniquely curated by TRAGUIN to blend sun-drenched beach relaxation, high-end shopping, luxury catamaran cruising, and deep body rejuvenation. Offering top-tier comfort, absolute safety protocols, and breathtaking landscapes, this is the definitive Luxury Phuket Holiday tailored for extraordinary women.\n\nTOUR OVERVIEW\nWelcome to your meticulously designed Phuket Ladies Escape, an exclusive 6-day holiday structured specifically for women who want to explore Thailand’s premier island destination in absolute style, safety, and luxury. TRAGUIN ensures an unparalleled travel experience featuring premium handpicked resorts, private secure logistics, beach club VIP accesses, and custom-tailored lifestyle itineraries. TRAGUIN Curated Experience Note: Your group's security and luxury are our absolute priorities. From women-friendly destination experts to private speed-craft voyages and front-row seats at top entertainment venues, your ladies' circle will experience a completely flawless, relaxed, and immersive holiday.\n\nWHY CHOOSE OUR LUXURY PHUKET LADIES ESCAPE PACKAGE?\nPhuket is a haven for premium female travel, offering a beautiful mix of private white-sand coves, award- winning luxury day spas, chic seaside cafes, and safe local night markets. Opting for a specialized female- only getaway or a dedicated Thailand Family Tour configuration with TRAGUIN opens doors to exclusive privileges. This itinerary targets the most highly searched tourism keywords for Google ranking, ensuring the ultimate layout of Phuket Sightseeing highlights. Discover Top Tourist Places in Thailand: the crystal clear waters of Maya Bay, the iconic limestone cliffs of Phang Nga Bay, and the heritage charm of Old Phuket Town. It is the absolute Best Time to Visit Thailand to capture beautiful group photos across popular Instagram locations, indulge in boutique retail therapy, and enjoy an unforgettable Premium Thailand Experience. TRAGUIN Ladies Escape Exclusives: Private luxury catamaran day cruise to Phi Phi Islands, front-row premium seating at the Simon Cabaret Show, a 120-minute traditional Thai massage and aromatic spa, and a sunset dinner party at a top beach club. THE DEFINITIVE DAY-WISE ITINERARY",
        seo_title='TH-010 | PHUKET LADIES ESCAPE Phuket | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-010 / TRG-HKT-LAD-2026): Phuket Premium Island with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: PHUKET ARRIVAL & CHIC SUNSET MEETUP', 1),
            _ih('Day 02: PHI PHI ISLANDS BY PRIVATE CATAMARAN', 2),
            _ih('Day 03: HERITAGE TOUR & LUXURY SPA PAMPERING', 3),
            _ih('Day 04: MYSTICAL PHANG NGA BAY SEA RIDE', 4),
            _ih('Day 05: PREMIUM SHOPPING & SIMON CABARET GLAMOUR', 5),
            _ih('Day 06: PHUKET DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private custom speedboats and premium catamarans, completely', 7),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium beachfront hotels located centrally next to', 8),
            _ih('Personalized Assistance: English-fluent dedicated local island guides to manage reservation', 9)
        ],
        days=[
            _day(
                1,
                'PHUKET ARRIVAL & CHIC SUNSET MEETUP',
                (
                    "WELCOME TO PARADISE – UNVEILING THE LADIES ESCAPE Your highly anticipated Girls Trip Thailand begins flawlessly as your group lands at Phuket International Airport. Receive a traditional Thai floral welcome coordinated seamlessly by your private TRAGUIN representative. Bypass the airport crowd as you step directly into your private, secure luxury air-conditioned van for a smooth scenic transfer to your premium beachfront resort. Check into your sea-view premium rooms, detailed with specialized welcome amenities and a chilled complimentary bottle of sparkling wine. Take the afternoon to unpack, relax, and take your first group photos by the resort's infinity pool. In the evening, dress up for a welcome sunset dinner party at a chic beachfront lounge, celebrating the start of an unforgettable luxury vacation. Sightseeing Included: Private premium airport-to-resort transfer, leisure beach stroll. Evening Experience: Sunset welcome cocktail/mocktail mixer at a high-end beachside lounge."
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: Curated International Buffet Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PHI PHI ISLANDS BY PRIVATE CATAMARAN',
                (
                    'SAILING THE ANDAMAN – CRYSTAL WATER COVES & GOURMET PICNIC Wake up to the sound of waves and savor a lavish buffet breakfast. Today hosts a cornerstone Premium Thailand Experience: an intimate sailing journey across the Andaman Sea. Avoid the crowded commercial tourist boats as TRAGUIN arranges a private, high-speed luxury catamaran to cruise your group away to the iconic Phi Phi Islands. Sail directly into the famous Maya Bay, a spectacular setting of vertical rock walls and powdery white sand, perfect for a high-fashion group photography session. Swim and snorkel among multi-colored marine life in the emerald basin of Pileh Lagoon. Enjoy a delicious, private beachfront gourmet picnic lunch set up specially on the soft sands of Bamboo Island before cruising home under a glorious golden sunset. Sightseeing Included: Maya Bay, Pileh Lagoon swimming, Bamboo Island beach stop, Viking Cave viewpoint. Optional Activities: Professional drone photography session for the group on the beach.'
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Luxury Catamaran Gourmet Lunch',
                ],
            ),
            _day(
                3,
                'HERITAGE TOUR & LUXURY SPA PAMPERING',
                (
                    'COLONIAL OLD TOWN QUARTER & 120-MINUTE DEEP REJUVENATION RETREAT Enjoy a relaxed morning, perhaps starting with a beautiful floating breakfast inside your pool villa. In the afternoon, start a comprehensive Phuket Sightseeing cultural tour by driving to the historic center of Old Phuket Town. Walk hand-in-hand past beautiful Sino-Portuguese colonial mansions, vibrant street murals, and charming independent cafes—consistently named a top popular Instagram location. Following your heritage walk, transition into absolute body wellness. TRAGUIN has reserved exclusive group slots at an award-winning luxury day spa sanctuary. Pamper yourselves with a 120-minute traditional Thai package featuring herbal steam baths, organic body scrubs, and therapeutic aromatic oil massages side-by- side. In the evening, explore the local night markets for boutique crafts and souvenirs. Sightseeing Included: Old Phuket Town Heritage Quarter, Wat Chalong Temple, Karon Viewpoint. Evening Experience: Boutique retail trail at the lively Chillva Night Market with local street food snacks.'
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Premium Local Thai Dining Lunch',
                ],
            ),
            _day(
                4,
                'MYSTICAL PHANG NGA BAY SEA RIDE',
                (
                    'JAMES BOND ISLAND LIMESTONES & SEA CAVE CANOEING Prepare for an awe-inspiring day exploring one of the most spectacular landscapes in Southeast Asia. After breakfast, transfer to the northern pier where a premium speed-craft takes your group across Phang Nga Bay. Cruise past hundreds of vertical limestone karsts rising dramatically out of the calm sea. Arrive at Khao Phing Kan, famously known as James Bond Island, an iconic attraction of Phuket Sightseeing. Take fantastic group pictures in front of the floating rock monolith. Next, enjoy a relaxing canoeing experience guided through the mystical sea caves and hidden mangrove lagoons of Koh Hong. Savor a fresh seafood buffet lunch at the unique stilted floating village of Koh Panyee before returning to the resort. Sightseeing Included: James Bond Island, Koh Hong sea cave canoeing, Koh Panyee floating village. Optional Activities: Sunset paddle-boarding at the resort beach or local Thai cooking masterclass.'
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Koh Panyee Seafood Buffet Lunch',
                ],
            ),
            _day(
                5,
                'PREMIUM SHOPPING & SIMON CABARET GLAMOUR',
                (
                    'RETAIL THERAPY AT CENTRAL FLORESTA & STAGE THEATRICS Dedicate today to world-class retail therapy and high-end glamour. Following breakfast, your private van takes you to Central Phuket Floresta, the island’s premier luxury mall. Discover massive luxury flagship stores, designer labels, and boutique Thai silk shops—making it an unparalleled location for premium shopping. Find unique jewelry pieces, high-end cosmetics, and fashion souvenirs. In the evening, dress in your finest outfits for a grand night out. TRAGUIN has reserved premium front-row VIP seats for your group at the famous Phuket Simon Cabaret Show. Witness an absolute masterclass in theatrical production, featuring spectacular costumes, state-of-the-art light effects, and brilliant international musical dance sequences that will leave the group fully entertained. Sightseeing Included: Central Phuket Floresta Luxury Mall, VIP access to Simon Cabaret Show. Evening Experience: Farewell group dinner party at an upscale beach club with live music and DJ sets.'
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & 3-Course Oceanfront Farewell Dinner',
                ],
            ),
            _day(
                6,
                'PHUKET DEPARTURE',
                (
                    "CHERISHING MEMORIES BEYOND DESTINATIONS Savor your final decadent buffet breakfast overlooking the ocean, capturing a final round of group photos across the tropical resort gardens. Depending on your flight departure schedule, spend your morning relaxing by the pool or enjoying a final authentic Thai iced tea on the sand. At the designated hour, your private luxury van arrives to provide a seamless transfer to Phuket International Airport for your return flight home. As you board your aircraft, look back on an exceptional collection of curated experiences, breathtaking landscapes, and unforgettable group memories crafted beautifully by TRAGUIN. Your premium ladies' escape concludes, leaving your circle with bonds and stories to last a lifetime. Sightseeing Included: Private luxury airport departure transfer."
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Phuket Kamala Beach Superior Ocean Room Complimentary Welcome Drinks & Beachside Yoga Session',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Novotel Phuket Kamala Beach Superior Ocean Room Complimentary Welcome Drinks & Beachside Yoga Session',
            ),
            _hotel(
                'Phuket Marriott Resort, Merlin Beach Pool View Room Welcome Fruit Baskets & 1 Group Cocktail Voucher',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Phuket Marriott Resort, Merlin Beach Pool View Room Welcome Fruit Baskets & 1 Group Cocktail Voucher',
            ),
            _hotel(
                'The Westin Siray Bay Resort & Spa Luxury Seaview Suite Complimentary Floating Breakfast Setup & Spa Discounts',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Westin Siray Bay Resort & Spa Luxury Seaview Suite Complimentary Floating Breakfast Setup & Spa Discounts',
            ),
            _hotel(
                'Anantara Layan Phuket Resort / Sri Panwa Deluxe Pool Villa / Luxury Ocean Suite Premium Champagne Bottle, 60-min Extension Spa & Private Pavilion Access',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Anantara Layan Phuket Resort / Sri Panwa Deluxe Pool Villa / Luxury Ocean Suite Premium Champagne Bottle, 60-min Extensi',
            )
        ],
        inclusions=[
            _inc_included('Handpicked premium accommodation as per selected hotel tier', 1),
            _inc_included('Private luxury vehicle transfers and sightseeing as per itinerary', 2),
            _inc_included('Daily buffet breakfast and curated meals as specified', 3),
            _inc_included('VIP airport fast-track reception and dedicated TRAGUIN concierge support', 4),
            _inc_excluded('PACKAGE INCLUSIONS', 5),
        ],
    )
    return package, itinerary

def build_th_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-011'
    tour_code = 'TRG-THA-SNR-2026'
    title = 'RELAX THAILAND TOUR PACKAGE Bangkok • Pattaya • Pure Serenity & Cultural Wonders'
    duration = '05 Nights / 06 Days'
    slug = 'th-011-relax-thailand-tour-package-bangkok-pattaya-pure-serenity-cultural-wonders'
    itin_slug = 'th-011-relax-thailand-tour-package-bangkok-pattaya-pure-serenity-cultural-wonders-itinerary'
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
            _ph('Serial code TH-011 | TRAGUIN tour code TRG-THA-SNR-2026', 1),
            _ph('State / Country: Thailand | Category: Senior Citizen Special / Relax Thailand', 2),
            _ph('Destinations: Pattaya (2N) + Bangkok', 3),
            _ph('Ideal for: Senior Citizens, Families, Couples Seeking Relaxation', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Ultra- Comfortable Large Van with Low Step-In / Buffet Breakfast (CP) & Soft Authentic Indian/ Thai Dinners Experience the timeless charm of the kingdom with the most thoughtfully crafted Best', 7),
            _ph('TRAGUIN Signature Experience: Private custom electric carts and priority boarding ramps,', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium accessible hotels located in peaceful zones', 9),
            _ph('Personalized Assistance: English-fluent dedicated local island guides to manage reservation', 10),
            _ph('Luxury Transportation: Executive modern vans equipped with specialized suspension systems,', 11)
        ],
        moods=['Honeymoon', 'Beach', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='RELAX THAILAND TOUR PACKAGE Bangkok',
        overview="Bangkok • Pattaya • Pure Serenity & Cultural Wonders 05 Nights / 06 Days Senior Citizen Special Calm Holiday SERIAL CODE: TH-011 TRAGUIN TOUR CODE: TRG-THA-SNR-2026 STATE / COUNTRY: Thailand CATEGORY: Senior Citizen Special / Relax Thailand DURATION: 05 Nights / 06 Days DESTINATIONS: Pattaya (2N) + Bangkok (3N) IDEAL FOR: Senior Citizens, Families, Couples Seeking Relaxation BEST SEASON: November to April (Mild Weather Months) VEHICLE TYPE: Private Ultra- Comfortable Large Van with Low Step-In MEAL PLAN: Buffet Breakfast (CP) & Soft Authentic Indian/ Thai Dinners Experience the timeless charm of the kingdom with the most thoughtfully crafted Best Thailand Tour Package, curated exclusively by TRAGUIN for our esteemed senior travelers. Prioritizing slow-paced exploration, zero-strain transfers, breathtaking landscapes, and premium stays, this Luxury Thailand Holiday offers a deeply emotional and smooth journey into cultural splendor.\n\nTOUR OVERVIEW\nWelcome to Relax Thailand, a premium vacation designed for travelers who prefer comfort, ease, and depth over rushed itineraries. Hand-crafted by senior-travel experts at TRAGUIN, this 6-day holiday features handpicked hotels with excellent accessibility, private comfortable vehicles with dedicated drivers, and mild, immersive experiences. TRAGUIN Curated Experience Note: We understand that a great trip is defined by peace of mind. Your itinerary includes relaxed morning starts, wheelchair accessibility options wherever requested, easily digestible authentic culinary menus, and 24/7 dedicated on-ground personal assistance. THE BEAUTY OF A SENIOR CITIZEN SPECIAL THAILAND HOLIDAY Thailand is not just for adventure seekers; it is a profound sanctuary of spirituality, royal history, and tranquil coastal vistas. Opting for a specialized Thailand Family Tour or a dedicated senior-focused holiday package through TRAGUIN ensures a restful and deeply satisfying vacation. This itinerary naturally incorporates highly searched keywords for Google ranking, showcasing the absolute best of Thailand Sightseeing. Explore legendary attractions: the majestic golden spires of Bangkok's sacred temples, the calm botanical pathways of Nong Nooch, and the peaceful evening waters of the Gulf of Thailand. It is the absolute Best Time to Visit Thailand to discover popular Instagram locations at a comfortable pace, enjoy traditional cultural music shows, and experience a genuinely therapeutic and premium holiday. TRAGUIN Senior Care Specials: Private accessible VIP seating at the cultural cultural theater, private soft- boat ride across the scenic floating market channels, priority fast-track check-ins, and easily accessible vehicle parking paths at every monument. THE THOUGHTFUL & RELAXED DAY-WISE ITINERARY",
        seo_title='TH-011 | RELAX THAILAND TOUR PACKAGE Bangkok | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-011 / TRG-THA-SNR-2026): Pattaya (2N) + Bangkok with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BANGKOK & TRANSIT TO PATTAYA', 1),
            _ih('Day 02: NONG NOOCH BOTANICAL GARDENS TOUR', 2),
            _ih('Day 03: PATTAYA TO BANGKOK CULTURAL TRANSIT', 3),
            _ih('Day 04: THE TRADITIONAL FLOATING MARKET RIDE', 4),
            _ih('Day 05: SIGHTSEEING FROM THE WATER & ICONSIAM VISITING', 5),
            _ih('Day 06: BANGKOK DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private custom electric carts and priority boarding ramps,', 7),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium accessible hotels located in peaceful zones', 8),
            _ih('Personalized Assistance: English-fluent dedicated local island guides to manage reservation', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BANGKOK & TRANSIT TO PATTAYA',
                (
                    'SAWADDEE THAILAND – A WARM WELCOME TO COMFORT AND CARE Your peaceful Relax Thailand journey begins seamlessly as your plane touches down at Bangkok’s Suvarnabhumi Airport. As you clear the gates, a warm greeting awaits your party, managed beautifully by your private TRAGUIN travel concierge. Avoid the strain of long walking paths as your group is guided directly to a premium, air-conditioned vehicle featuring high-cushion seating and a low step-in layout, perfect for senior comfort. Enjoy a smooth, relaxed drive along the coastal highway to the peaceful resort bay of Pattaya. Arrive at your premium handpicked hotel, where our representative handles all check-in procedures and luggage transfers on your behalf. Spend your afternoon resting in your spacious room or watching the sunset over the water from the terrace, capturing a beautiful opening photography point for your trip diary. Sightseeing Included: Private airport concierge reception, smooth private highway transit to Pattaya. Evening Experience: Relaxed introductory dinner at the resort’s quiet sea-facing garden restaurant.'
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Accessible Sea-View Resort)',
                    'Meals Included: Mild Multi-Cuisine Indian/Thai Welcome Dinner',
                ],
            ),
            _day(
                2,
                'NONG NOOCH BOTANICAL GARDENS TOUR',
                (
                    'BREATHTAKING LANDSCAPES & TRADITIONAL THAI CULTURAL SPECTACLE Savor a leisurely breakfast with freshly prepared global dishes. Today features an elite highlight of Pattaya Sightseeing: a visit to the magnificent Nong Nooch Botanical Gardens. Spanning over 500 acres of meticulously designed themed valleys, it is an absolute paradise of floral beauty. TRAGUIN arranges private electric open-air carts to guide your group through the French gardens and orchid paths without any physical strain. Enjoy a beautiful Thai Cultural Show inside the air-conditioned theater complex, showcasing traditional dance, sword-fighting, and festive drumming rhythms. After a relaxing buffet lunch inside the gardens, return to your resort for a restful afternoon nap. In the evening, take a slow stroll down the quiet, sandy shores of Pattaya beach, feeling the gentle ocean breeze. Sightseeing Included: Nong Nooch Orchid Gardens entry, open electric cart tour, Traditional Cultural Show. Optional Activities: A mild foot reflexology session or an easy elephant feeding experience at the reserve.'
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Accessible Sea-View Resort)',
                    'Meals Included: International Buffet Breakfast & Nong Nooch Garden Buffet Lunch',
                ],
            ),
            _day(
                3,
                'PATTAYA TO BANGKOK CULTURAL TRANSIT',
                (
                    'SACRED SHRINES & THE MAJESTIC SACRED TEMPLES OF BANGKOK Check out comfortably after breakfast as your private vehicle drives you smoothly back towards the historical royal heart of the kingdom: Bangkok. Today features deep cultural discovery and authentic Bangkok Sightseeing. Your first stop is Wat Traimit to view the astounding Golden Buddha—a 5.5-ton solid gold statue dating back to the historic Sukhothai period, accessible via elevator walkways. Continue your premium tour to Wat Pho, home to the monumental 46-meter Reclining Buddha covered in exquisite gold leaf. The flat stone pathways here allow a very comfortable pace for walking. Check into your ultra-luxury riverside hotel overlooking the River of Kings, offering unmatched scenic beauty right from your bedroom window. Sightseeing Included: Wat Traimit (Golden Buddha), Wat Pho (Reclining Buddha), City Driving Tour. Evening Experience: Relaxing over traditional Thai herbal tea while watching the boat traffic along the river.'
                ),
                [
                    'Overnight Stay: Bangkok (Ultra-Luxury Accessible Riverside Hotel)',
                    'Meals Included: International Buffet Breakfast & Authentic Indian Comfort Lunch',
                ],
            ),
            _day(
                4,
                'THE TRADITIONAL FLOATING MARKET RIDE',
                (
                    'DAMNOEN SADUAK CHANNELS & PRIVATE HANDICRAFT TRAILS Enjoy a relaxed morning schedule today. Following breakfast, your private vehicle takes your group to the iconic Damnoen Saduak Floating Market, a highly sought-after cultural hallmark. To ensure zero physical strain, TRAGUIN books a private, slow-moving traditional wooden canal boat equipped with comfortable seating cushions and canvas sun-roofs for protection. Glide gently along the historic waterways, watching local floating vendors sell colorful fruits, sweets, and local art pieces right from their watercraft. It is an amazing photography point to capture authentic Thai life. Return to Bangkok in the afternoon for a delicious lunch, leaving your late afternoon entirely free for a peaceful rest at the hotel. Sightseeing Included: Damnoen Saduak floating village entry, private padded canal boat ride tour. Optional Activities: A visit to a traditional premium gemstone artisan center or silk weaving gallery.'
                ),
                [
                    'Overnight Stay: Bangkok (Ultra-Luxury Accessible Riverside Hotel)',
                    'Meals Included: International Buffet Breakfast & Selected Thai-Indian Fusion Lunch',
                ],
            ),
            _day(
                5,
                'SIGHTSEEING FROM THE WATER & ICONSIAM VISITING',
                (
                    "ICONSIAM WATERFRONT LUXURY & CHAO PHRAYA RIVER DINNER CRUISE Dedicate today to light, premium shopping and a flagship Premium Thailand Experience. In the afternoon, your driver drops your group at ICONSIAM, the crown jewel of Bangkok's shopping plazas. The mall is fully air-conditioned, feature-packed with wide flat walkways and elevators, and includes an indoor floating market on the ground level, making it a perfect spot for senior citizen shopping for local souvenirs and silks. In the evening, embark on a 5-star luxury dinner cruise aboard the Grand Pearl Cruise liner on the Chao Phraya River. Avoid any crowd congestion with our pre-booked priority ramp boarding. Glide smoothly past the brilliantly lit Grand Palace and the luminous spires of Wat Arun (The Temple of Dawn) while enjoying a sumptuous international and Indian buffet dinner with soft live jazz background music. Sightseeing Included: ICONSIAM luxury lifestyle destination, Chao Phraya Grand Pearl River Cruise. Evening Experience: 5-Star Luxury River Dinner Cruise with live classical music and light traditional dances."
                ),
                [
                    'Overnight Stay: Bangkok (Ultra-Luxury Accessible Riverside Hotel)',
                    'Meals Included: International Buffet Breakfast & Grand Cruise Dinner Buffet',
                ],
            ),
            _day(
                6,
                'BANGKOK DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS Enjoy your final decadent buffet breakfast at your luxury hotel, capturing a final round of group photos overlooking the bustling Chao Phraya River. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless checkout. At the designated hour, your comfortable private vehicle arrives to provide a smooth transfer to Suvarnabhumi International Airport for your flight back home. As you board your aircraft, look back on an exceptional collection of curated experiences, breathtaking landscapes, and unforgettable memories crafted beautifully by TRAGUIN. Your premium vacation concludes, leaving you rested, fulfilled, and full of stories. Sightseeing Included: Private luxury airport departure transfer.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Pattaya Resort Superior Accessible Room (BB) The Sukosol Bangkok Premier Garden View (BB)',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Novotel Pattaya Resort Superior Accessible Room (BB) The Sukosol Bangkok Premier Garden View (BB)',
            ),
            _hotel(
                'Amari Pattaya Deluxe Garden Accessible (BB) Grande Centre Point Terminal 21 Premium Deluxe Room (BB)',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Amari Pattaya Deluxe Garden Accessible (BB) Grande Centre Point Terminal 21 Premium Deluxe Room (BB)',
            ),
            _hotel(
                'Hilton Pattaya Executive Ocean View Suite (BB) Avani+ Riverside Bangkok Hotel Avani River View Room (BB)',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Hilton Pattaya Executive Ocean View Suite (BB) Avani+ Riverside Bangkok Hotel Avani River View Room (BB)',
            ),
            _hotel(
                'Grande Centre Point Space Pattaya Space Premium Balcony Suite (BB) Shangri-La Bangkok / Mandarin Oriental Deluxe Horizon River Room (BB)',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Grande Centre Point Space Pattaya Space Premium Balcony Suite (BB) Shangri-La Bangkok / Mandarin Oriental Deluxe Horizon',
            )
        ],
        inclusions=[
            _inc_included('Handpicked premium accommodation as per selected hotel tier', 1),
            _inc_included('Private luxury vehicle transfers and sightseeing as per itinerary', 2),
            _inc_included('Daily buffet breakfast and curated meals as specified', 3),
            _inc_included('VIP airport fast-track reception and dedicated TRAGUIN concierge support', 4),
            _inc_excluded('PACKAGE INCLUSIONS', 5),
        ],
    )
    return package, itinerary

def build_th_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-012'
    tour_code = 'TRG-HKT-LUX-2026'
    title = 'PHUKET RETREAT Phuket Island • Nai Harn • Phi Phi Islands • Phang Nga Bay'
    duration = '06 Nights / 07 Days'
    slug = 'th-012-phuket-retreat-phuket-island-nai-harn-phi-phi-islands-phang-nga-bay'
    itin_slug = 'th-012-phuket-retreat-phuket-island-nai-harn-phi-phi-islands-phang-nga-bay-itinerary'
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
            _ph('Serial code TH-012 | TRAGUIN tour code TRG-HKT-LUX-2026', 1),
            _ph('State / Country: Thailand | Category: Luxury Vacation / Premium Retreat', 2),
            _ph('Destinations: Phuket Ultra-Luxury', 3),
            _ph('Ideal for: Luxury Travelers, Couples, Families Seeking Premium Stays', 4),
            _ph('Best season: November to May (Prime Sunshine Months)', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Chauffeur- Driven Executive European Sedan / SUV / Bespoke Floating Breakfasts & Fine Dining Journeys Indulge in the ultimate tropical sanctuary with the Best Phuket Tour Package, masterfully', 7),
            _ph('TRAGUIN Signature Experience: Private custom yachts and premium speed-craft charters,', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified luxury romantic resorts featuring maximum isolation,', 9),
            _ph('Personalized Assistance: English-fluent dedicated local island guides to manage reservation priorities', 10),
            _ph('Luxury Transportation: Elite executive vehicles equipped with specialized suspension systems,', 11)
        ],
        moods=['Luxury', 'Honeymoon', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='PHUKET RETREAT Phuket Island',
        overview="TOUR OVERVIEW\nWelcome to the Luxury Phuket Retreat, a flagship island holiday designed for sophisticated travelers who demand seamless operational perfection and elite privacy. Over 7 magnificent days, TRAGUIN will immerse you in the best of the Andaman Sea. Enjoy absolute island sanctuary inside private pool villas, travel in elite executive vehicles, and take part in customized marine charters. TRAGUIN Curated Experience Note: Every phase of this retreat is actively managed by our luxury concierge desk. From fast-track VIP arrivals to customized private chef menus, we guarantee an immaculate, stress-free holiday designed to create memories far beyond ordinary destinations. THE DEFINITION OF A PREMIUM PHUKET EXPERIENCE Phuket stands as an international masterpiece of luxury travel, effortlessly blending dramatic vertical cliffs with ultra-modern private estates and Michelin-starred dining options. Choosing one of our signature TRAGUIN Destination Packages or a premium Phuket Honeymoon Package ensures an itinerary far superior to generic options. This proposal targets top searched keywords for Google ranking, ensuring the ultimate showcase of premier Phuket Sightseeing. Discover legendary attractions: the striking clear lagoons of the Phi Phi Islands, the mystical hidden sea caves of Phang Nga Bay, and the colorful colonial streets of Old Phuket Town. It is the absolute Best Time to Visit Phuket to lounge at ultra-exclusive beach clubs, capture stunning photographs at popular Instagram locations, and enjoy a deeply therapeutic and premium holiday. TRAGUIN Luxury Retreat Specials: Private luxury yacht cruise across the Andaman Sea, an exclusive 150- minute multi-tier couple's spa therapy, helicopter sightseeing options, and private beachfront candlelight dining. THE SOPHISTICATED DAY-WISE ITINERARY",
        seo_title='TH-012 | PHUKET RETREAT Phuket Island | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Thailand package (TH-012 / TRG-HKT-LUX-2026): Phuket Ultra-Luxury with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: PHUKET ARRIVAL & PRIVATE VILLA INDULGENCE', 1),
            _ih('Day 02: PRIVATE LUXURY YACHT TO PHI PHI ISLANDS', 2),
            _ih('Day 03: HERITAGE EXPLORATION & ULTRA-WELLNESS IMMERSION', 3),
            _ih('Day 04: PHANG NGA BAY SEA CAVE CANOEING BY SPEED-CRAFT', 4),
            _ih('Day 05: LEISURE RESORT RETREAT & MICHELIN DINING EXPERIENCE', 5),
            _ih('Day 06: BOUTIQUE SHOPPING & PRIVATE BEACH CANCELLIGHT FINALE', 6),
            _ih('Day 07: PHUKET DEPARTURE', 7),
            _ih('TRAGUIN Signature Experience: Private custom yachts and premium speed-craft charters,', 8),
            _ih('Curated by TRAGUIN Experts: Safety-verified luxury romantic resorts featuring maximum isolation,', 9),
            _ih('Personalized Assistance: English-fluent dedicated local island guides to manage reservation priorities', 10)
        ],
        days=[
            _day(
                1,
                'PHUKET ARRIVAL & PRIVATE VILLA INDULGENCE',
                (
                    'WELCOME TO PARADISE – STEPPING INTO ABSOLUTE SANCTUARY Your ultimate Luxury Phuket Holiday begins flawlessly as your flight lands at Phuket International Airport. Step through the gate to receive our VIP Airport Fast-Track service, clearing custom formalities without any lines. Your private, elegant European sedan or executive SUV waits to transfer you smoothly along the scenic shoreline to your ultra-luxury pool villa resort. Check into your handpicked estate, where a chilled complimentary bottle of premium champagne and specialized welcome fruits await you. Spend your afternoon relaxing inside your private infinity pool or strolling down the resort’s private beach access. At twilight, enjoy a custom 4-course welcome dinner served on your private poolside deck by a personal chef, establishing an unforgettable memory for your first night. Sightseeing Included: VIP airport reception and fast-track clearance, scenic private luxury resort transfer. Evening Experience: Bespoke welcome dinner party at your private villa deck with a customized chef menu.'
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Private Ocean-View Pool Villa)',
                    'Meals Included: Bespoke 4-Course Private Villa Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PRIVATE LUXURY YACHT TO PHI PHI ISLANDS',
                (
                    'ANDAMAN HORIZONS – EXCLUSIVE SAILING, MAYA BAY & EMERALD REEFS Wake up to a gorgeous sunrise over the water and enjoy a decadent buffet breakfast. Today hosts an elite signature experience: a full-day private luxury yacht charter to explore the world-famous Phi Phi Islands. Skip all standard public crowds as your captain steers your magnificent vessel through the deep blue waters directly toward the towering rock amphitheater of Maya Bay. Swim and snorkel hand-in-hand within the calm, emerald waters of Pileh Lagoon, a beautiful natural limestone basin filled with colorful marine life. Your onboard personal crew serves a premium gourmet lunch paired with fine wines as you anchor near Bamboo Island. Spend your afternoon walking on soft, powdery sands or taking beautiful photographs from the yacht deck before cruising home under a glorious pastel sunset. Sightseeing Included: Private Yacht Cruise to Maya Bay, Pileh Lagoon, Bamboo Island beach access, Viking Cave. Optional Activities: Professional drone photography session for couples or families on the private yacht.'
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Private Ocean-View Pool Villa)',
                    'Meals Included: International Buffet Breakfast & Onboard Yacht Gourmet Lunch with Fine Wine',
                ],
            ),
            _day(
                3,
                'HERITAGE EXPLORATION & ULTRA-WELLNESS IMMERSION',
                (
                    'COLONIAL OLD TOWN ARCHITECTURE & A 150-MINUTE MASTER SPA TREATMENT Savor a beautiful floating breakfast served right inside your private infinity pool. In the afternoon, your private chauffeur takes you on an immersive Phuket Sightseeing cultural tour. Discover the historic center of Old Phuket Town, walking past beautifully preserved Sino-Portuguese colonial mansions, vibrant street murals, and independent artisan boutiques perfect for premium souvenir shopping. Following your heritage walk, transition into absolute body wellness. TRAGUIN has reserved an exclusive 150-minute rejuvenation package at an award-winning luxury day spa sanctuary. Melt away travel tension with exotic Thai herbal wraps, deep-tissue hot stone oil massages, and an organic facial treatment. Spend your evening relaxing at a high-end cliffside lounge watching the sunset. Sightseeing Included: Old Phuket Town Heritage District, Wat Chalong Temple, Karon Viewpoint. Evening Experience: VIP lounge access at an ultra-exclusive oceanfront cliff club for sunset cocktails.'
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Private Ocean-View Pool Villa)',
                    'Meals Included: Premium Floating Breakfast & Fine Dining Contemporary Thai Dinner',
                ],
            ),
            _day(
                4,
                'PHANG NGA BAY SEA CAVE CANOEING BY SPEED-CRAFT',
                (
                    'MYSTICAL LIMESTONE MONOLITHS & ICONIC JAMES BOND ISLAND Prepare for an awe-inspiring day exploring one of the most magnificent landscapes in Southeast Asia. After breakfast, transfer to the northern pier where a private premium speed-craft takes your group across Phang Nga Bay. Cruise past hundreds of vertical limestone karsts rising dramatically out of the calm sea. Arrive at James Bond Island, an iconic attraction of Phuket Sightseeing, and capture fantastic pictures in front of the floating rock monolith. Next, enjoy a relaxing canoeing experience guided through the mystical sea caves and hidden mangrove lagoons of Koh Hong. Savor a fresh seafood lunch at the unique stilted floating village of Koh Panyee before returning to the resort for an evening of relaxation. Sightseeing Included: James Bond Island entry, Koh Hong sea cave canoeing, Koh Panyee village view. Optional Activities: Private helicopter sightseeing flight over the islands for a stunning birds-eye view.'
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Private Ocean-View Pool Villa)',
                    'Meals Included: International Buffet Breakfast & Koh Panyee Seafood Lunch',
                ],
            ),
            _day(
                5,
                'LEISURE RESORT RETREAT & MICHELIN DINING EXPERIENCE',
                (
                    "UNWINDING IN PARADISE & THE CULINARY HIGHLIGHT OF PHUKET Dedicate today entirely to personalized relaxation and enjoyment inside your ultra-luxury resort. Enjoy a slow morning breakfast on your private veranda. Spend the day reading by the private beach, playing a round of golf at a nearby championship course, or taking a private yoga class overlooking the Andaman Sea. In the evening, dress in elegant luxury wear for an incredible culinary highlight. TRAGUIN has pre-booked a prime table at one of Phuket's Michelin-starred or top-rated contemporary restaurants. Indulge in a spectacular multi-course tasting menu prepared by world-renowned chefs, blending authentic Thai flavors with high-end global techniques. Sightseeing Included: Bespoke luxury resort leisure schedule, private evening dining transfers. Evening Experience: Bespoke Multi-Course Michelin Tasting Menu Dining."
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Private Ocean-View Pool Villa)',
                    'Meals Included: International Buffet Breakfast & Michelin Star Gastronomy Dinner',
                ],
            ),
            _day(
                6,
                'BOUTIQUE SHOPPING & PRIVATE BEACH CANCELLIGHT FINALE',
                (
                    'PREMIUM RETAIL THERAPY & A SIGNATURE BEACH COVE GRAND FINALE Enjoy your morning breakfast before heading out for some premium retail therapy. Your private chauffeur takes your group to Central Phuket Floresta, the island’s premier luxury mall. Discover massive luxury flagship stores, global designer labels, and boutique Thai silk shops—making it an unparalleled location for premium shopping. Find unique jewelry pieces, high-end cosmetics, and fashion souvenirs. Return to the resort to refresh for your final night. TRAGUIN has arranged our ultimate signature surprise: an intimate, completely private beachfront candlelight dinner set in a secluded cove of the resort. Toast your holiday together with a glass of vintage wine under a beautiful sky as gentle waves roll in, creating a memory to last a lifetime. Sightseeing Included: Central Phuket Floresta Luxury Plaza, Private Beach Cove access. Evening Experience: Signature TRAGUIN Grand Finale Private Beachfront Candlelight Dinner.'
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Private Ocean-View Pool Villa)',
                    'Meals Included: International Buffet Breakfast & Ultra-Luxury Beachside 5-Course Dinner',
                ],
            ),
            _day(
                7,
                'PHUKET DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS Savor your final morning breakfast at your villa veranda, taking a final round of panoramic photos across the tropical resort gardens. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless checkout. At the designated hour, your private luxury executive vehicle arrives to transfer you comfortably to Phuket International Airport. Your travel manager assists with check-in and luggage procedures, escorting you to the premium departure lounge. Your luxury Phuket Retreat concludes beautifully, leaving your heart full of unforgettable memories and stories crafted to perfection by TRAGUIN. Sightseeing Included: Private luxury airport departure transfer, premium lounge entry. HANDPICKED ULTRA-LUXURY ACCOMMODATIONS We believe that elite accommodations are the true soul of a premium vacation. TRAGUIN has handpicked the most exceptional properties across Phuket, featuring maximum isolation, infinity-edge private pools, and magnificent ocean views. Category Phuket Ultra-Luxury Stay (06 Nights) Exclusive Included Privilege Option 01: Deluxe Luxury Pullman Phuket Arcadia Naithon Beach Ocean Luxury Pool Villa Complimentary Honeymoon Setup & 1 Bottle of Wine Option 02: Premium Luxury The Westin Siray Bay Resort & Spa Two-Bedroom Ocean View Pool Villa Daily Floating Breakfast Setup & Late Check-out Guarantee Option 03: Elite Luxury The Shore at Katathani Seaview Premium Pool Villa Sparkling Champagne, Floral Bath Setup & 60-min Couple Massage Option 04: Ultra Luxury Trisara Phuket / Sri Panwa Luxury Resort Ocean Front Luxury Pool Villa Premium Vintage Champagne, Private Beach Pavilion Access & 24/7 Butler Support'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Luxury Pullman Phuket Arcadia Naithon Beach Ocean Luxury Pool Villa Complimentary Honeymoon Setup & 1 Bottle of Wine',
                'Multi-city Thailand',
                '6N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Luxury Pullman Phuket Arcadia Naithon Beach Ocean Luxury Pool Villa Complimentary Honeymoon Setup & 1 Bottle of Wine',
            ),
            _hotel(
                'Luxury The Westin Siray Bay Resort & Spa Two-Bedroom Ocean View Pool Villa Daily Floating Breakfast Setup & Late Check-out Guarantee',
                'Multi-city Thailand',
                '6N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Luxury The Westin Siray Bay Resort & Spa Two-Bedroom Ocean View Pool Villa Daily Floating Breakfast Setup & Late Check-o',
            ),
            _hotel(
                'Trisara Phuket / Sri Panwa Luxury Resort Ocean Front Luxury Pool Villa Premium Vintage Champagne, Private Beach Pavilion Access & 24/7 Butler Support',
                'Multi-city Thailand',
                '6N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Trisara Phuket / Sri Panwa Luxury Resort Ocean Front Luxury Pool Villa Premium Vintage Champagne, Private Beach Pavilion',
            )
        ],
        inclusions=[
            _inc_included('Handpicked premium accommodation as per selected hotel tier', 1),
            _inc_included('Private luxury vehicle transfers and sightseeing as per itinerary', 2),
            _inc_included('Daily buffet breakfast and curated meals as specified', 3),
            _inc_included('VIP airport fast-track reception and dedicated TRAGUIN concierge support', 4),
            _inc_excluded('PACKAGE INCLUSIONS', 5),
        ],
    )
    return package, itinerary

def build_th_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-013'
    tour_code = 'TRG-BKK-HKT-LUX-2026'
    title = 'BANGKOK PHUKET PACKAGE Bangkok • Chao Phraya River • Phuket • Phi Phi Islands'
    duration = '07 Nights / 08 Days'
    slug = 'th-013-bangkok-phuket-package-bangkok-chao-phraya-river-phuket-phi-phi-islands'
    itin_slug = 'th-013-bangkok-phuket-package-bangkok-chao-phraya-river-phuket-phi-phi-islands-itinerary'
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
            _ph('Serial code TH-013 | TRAGUIN tour code TRG-BKK-HKT-LUX-2026', 1),
            _ph('State / Country: Thailand | Category: Luxury Holiday / Premium Experience', 2),
            _ph('Destinations: Bangkok (3N) + Phuket', 3),
            _ph('Ideal for: Luxury Travelers, Couples, Families, VIP Retreats', 4),
            _ph('Best season: November to May (Optimal Weather Window)', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Chauffeur- Driven Mercedes-Benz / BMW Sedan / Luxury Van / Buffet Breakfast (CP), Michelin Dining & Cruise Gala Dinners', 7),
            _ph('TRAGUIN Signature Experience: Private custom speedboats and premium river cruises, completely', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified luxury romantic resorts featuring maximum isolation,', 9),
            _ph('Personalized Assistance: English-fluent dedicated local island guides to manage reservation priorities', 10),
            _ph('Luxury Transportation: Elite executive vehicles equipped with specialized suspension systems,', 11)
        ],
        moods=['Luxury', 'Honeymoon', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='BANGKOK PHUKET PACKAGE Bangkok',
        overview='TOUR OVERVIEW\nWelcome to the Luxury Bangkok Phuket vacation, a masterfully structured multi-destination escape designed exclusively for sophisticated world travelers. Across 8 spectacular days, TRAGUIN brings you a flawless mix of urban exploration and private island serenity. Enjoy private chauffeured luxury transfers, fast- track VIP arrivals, private marine yachting charters, and exceptional fine-dining venues. TRAGUIN Curated Experience Note: We ensure absolute perfection at every milestone. From your pre- allocated executive honeymoon setups to private beach coves and 5-star cruising lounges, your vacation is managed 24/7 by our dedicated on-ground premium concierge network. THE ALLURE OF OUR PREMIUM THAILAND EXPERIENCE The combination of Bangkok and Phuket remains the gold standard of luxury travel in Southeast Asia. Booking a signature TRAGUIN Thailand Package or an ultra-exclusive Phuket Honeymoon Package guarantees access to hidden domains and priority privileges. This proposal integrates top searched keywords for Google ranking, showcasing an elite layout of premier Thailand Sightseeing. Uncover legendary attractions: the historic golden spires of the Grand Palace, the breathtaking landscape of Maya Bay, and the high-fashion retail malls of the capital. It is universally known as the Best Time to Visit Thailand to indulge in award-winning wellness therapies, capture stunning couple and group photos at popular Instagram locations, and enjoy a truly unforgettable romantic or family holiday. TRAGUIN Elite Inclusions: VIP Fast-Track airport arrival service, 5-star luxury Chao Phraya River cruise, private speedboat charter across the Andaman Sea, and private beachfront candlelight dining. THE DEFINITIVE DAY-WISE ITINERARY',
        seo_title='TH-013 | BANGKOK PHUKET PACKAGE Bangkok | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Thailand package (TH-013 / TRG-BKK-HKT-LUX-2026): Bangkok (3N) + Phuket with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: BANGKOK ARRIVAL & VIP CRUISE', 1),
            _ih('Day 02: BANGKOK HERITAGE & TEMPLES TOUR', 2),
            _ih('Day 03: HIGH-FASHION RETAIL THERAPY & SKYWALK SUNSET', 3),
            _ih('Day 04: BANGKOK TO PHUKET FLY-IN', 4),
            _ih('Day 05: EXCLUSIVE PHI PHI ISLANDS ESCAPE', 5),
            _ih('Day 06: PHUKET CULTURE & SPA IMMERSION', 6),
            _ih('Day 07: PHANG NGA BAY SEACAVE CANOEING & GRAND FINALE DINNER', 7),
            _ih('Day 08: PHUKET DEPARTURE', 8),
            _ih('TRAGUIN Signature Experience: Private custom speedboats and premium river cruises, completely', 9),
            _ih('Curated by TRAGUIN Experts: Safety-verified luxury romantic resorts featuring maximum isolation,', 10)
        ],
        days=[
            _day(
                1,
                'BANGKOK ARRIVAL & VIP CRUISE',
                (
                    'WELCOME TO THE CITY OF ANGELS – MULTI-CENTURY METROPOLITAN GLAMOUR Your spectacular Luxury Thailand Holiday begins the moment you touch down at Bangkok’s Suvarnabhumi International Airport. Step through the gate to receive our VIP Fast-Track Reception, clearing all customs and immigration procedures within minutes. Your private, elegant Mercedes-Benz or executive sedan waits to transfer you smoothly to your ultra-luxury riverside hotel overlooking the River of Kings. Check into your handpicked premium riverfront room. In the evening, dress in elegant luxury resort wear for a definitive Premium Thailand Experience: a 5-star luxury dinner cruise aboard the Grand Pearl Cruise liner on the Chao Phraya River. Glide past the brilliantly lit Grand Palace and the luminous spires of Wat Arun (The Temple of Dawn) while enjoying a sumptuous international buffet, live jazz music, and classical Thai dance performances. Sightseeing Included: VIP airport fast-track reception, scenic river highway transfer, Chao Phraya cruising. Evening Experience: 5-Star Luxury Chao Phraya River Dinner Cruise with live jazz background music.'
                ),
                [
                    'Overnight Stay: Bangkok (Ultra-Luxury Riverside Resort)',
                    'Meals Included: Premium Cruise Gala Buffet Dinner',
                ],
            ),
            _day(
                2,
                'BANGKOK HERITAGE & TEMPLES TOUR',
                (
                    'SIAMESE SPLENDOR – THE GRAND PALACE & GOLDEN SHINES Savor a magnificent buffet breakfast before starting a descriptive Bangkok Sightseeing cultural tour. Your private chauffeur navigates you to the walled complex of the Grand Palace, the historic residence of the Kings of Siam. Admire the stunning gold-leaf spires and explore the sacred Temple of the Emerald Buddha (Wat Phra Kaew), capturing magnificent photos at key photography points. Continue your heritage journey to Wat Pho to stand before the monumental 46-meter Reclining Buddha temple. Following a gourmet Thai lunch at a waterfront restaurant, visit Wat Traimit to view the astounding Golden Buddha—a 5.5-ton solid gold statue dating back to the historic Sukhothai period. Spend your evening relaxing back at the resort or exploring the nearby cultural markets. Sightseeing Included: The Grand Palace, Wat Phra Kaew, Wat Pho, Wat Traimit (Golden Buddha). Evening Experience: Relaxing over traditional Thai herbal tea while watching the sunset from your riverside terrace.'
                ),
                [
                    'Overnight Stay: Bangkok (Ultra-Luxury Riverside Resort)',
                    'Meals Included: International Buffet Breakfast & Traditional Thai Fine Dining Lunch',
                ],
            ),
            _day(
                3,
                'HIGH-FASHION RETAIL THERAPY & SKYWALK SUNSET',
                (
                    "WORLD-CLASS SHOPPING & MAHANAKHON SKYLINE ADVENTURE Dedicate today to world-class retail therapy and ultra-modern architecture. Following breakfast, your private vehicle drops your group at ICONSIAM, the crown jewel of Bangkok's shopping plazas. Featuring an indoor floating market, incredible waterfront spaces, and massive luxury brand flagship stores, it is an unparalleled location for premium shopping. Find unique silk garments, boutique cosmetics, and local designer items. In the afternoon, proceed to Siam Paragon and CentralWorld for high-fashion global labels. At twilight, head up to the Mahanakhon SkyWalk, standing 314 meters above the streets on a massive glass tray— consistently named one of the top popular Instagram locations in Thailand. End your night with VIP tables reserved at a premium rooftop lounge, celebrating your stay over delicious dining and spectacular skyline views. Sightseeing Included: ICONSIAM Mall, Siam Paragon, Mahanakhon SkyWalk VIP Entry Ticket. Evening Experience: Premium cocktails and high-fashion dining at a top-tier sky lounge overlooking the city."
                ),
                [
                    'Overnight Stay: Bangkok (Ultra-Luxury Riverside Resort)',
                    'Meals Included: International Buffet Breakfast & Rooftop Gastronomy Dinner',
                ],
            ),
            _day(
                4,
                'BANGKOK TO PHUKET FLY-IN',
                (
                    "TRANSIT TO THE PEARL OF THE ANDAMAN SEA – OCEANFRONT BLISS Enjoy your final morning breakfast looking out over the Chao Phraya River before checking out. Your private vehicle transfers you to the airport for your short domestic flight to Phuket. Upon arrival on Thailand's largest island, your waiting private premium vehicle provides a smooth transfer along the beautiful Andaman coastline to your ultra-luxury pool villa resort. Phuket is globally celebrated for its breathtaking landscapes, dramatic limestone cliffs, and vibrant coastal culture, making it the perfect continuation for a Luxury Thailand Holiday. Check into your premium villa, detailed with a chilled complimentary bottle of sparkling wine. Spend the afternoon unwinding by your private pool or strolling along the powdery sand beaches, watching the horizon transform into a vibrant tapestry of pastel sunset hues. Sightseeing Included: Domestic flight transit, coastal scenic private resort transfer, beach sunset lounge walk. Evening Experience: Welcome cocktails at an exclusive beach club with live acoustic background music."
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Ocean-Front Private Pool Villa)',
                    'Meals Included: International Buffet Breakfast & Curated Coastal Seafood Dinner',
                ],
            ),
            _day(
                5,
                'EXCLUSIVE PHI PHI ISLANDS ESCAPE',
                (
                    'PRIVATE SPEEDBOAT SAILING TO MAYA BAY & TURQUOISE LAGOONS Wake up to the gentle murmur of the tide and enjoy a lavish buffet breakfast. Today hosts one of the most searched experiences in the world: an exclusive island-hopping expedition across the Andaman Sea. Avoid the crowded regular tour boats as TRAGUIN arranges an exclusive, high-speed private speedboat to explore the legendary Phi Phi Islands. Cruise across turquoise waters directly to Maya Bay, an absolute highlight of Phuket Sightseeing, surrounded by colossal rock formations. Swim and snorkel hand-in-hand within the calm, emerald waters of Pileh Lagoon, a beautiful natural limestone basin filled with colorful marine life. Your crew serves a premium gourmet picnic lunch on the white sands of Bamboo Island. Conclude the day exploring Monkey Beach and the historic Viking Cave, capturing unforgettable memories with your family. Sightseeing Included: Maya Bay entry, Pileh Lagoon swimming, Bamboo Island beach stop, Viking Cave view. Optional Activities: Deep-sea tandem scuba diving under expert PADI guidance, or sea-kayaking through hidden caves.'
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Ocean-Front Private Pool Villa)',
                    'Meals Included: International Buffet Breakfast & Island Beachfront Gourmet Lunch',
                ],
            ),
            _day(
                6,
                'PHUKET CULTURE & SPA IMMERSION',
                (
                    'THE MAJESTIC BIG BUDDHA & AN AWARD-WINNING COUPLES SPA RETREAT Savor a beautiful floating breakfast served right inside your private infinity pool. In the afternoon, your private chauffeur takes you on a panoramic island tour. Drive up the Nakkerd Hills to stand at the base of the majestic 45-meter Big Buddha. This vantage point offers an incredible 360-degree panorama of Chalong Bay and Phuket Town—consistently ranked among the most popular Instagram locations in Southeast Asia. Following your scenic mountain tour, transition into absolute body wellness. TRAGUIN has reserved an exclusive 120-minute rejuvenation package at an award-winning luxury day spa sanctuary. Melt away travel tension with exotic Thai herbal wraps, deep-tissue hot stone oil massages, and an organic body treatment. Spend your evening relaxing at a high-end cliffside lounge watching the sunset over the sea. Sightseeing Included: The Big Buddha monument, Wat Chalong Temple, Karon Viewpoint. Evening Experience: Catching the breathtaking, iconic sunset at Phromthep Cape, the southernmost tip of Phuket.'
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Ocean-Front Private Pool Villa)',
                    'Meals Included: Premium Floating Breakfast & Contemporary Thai Fine Dining Dinner',
                ],
            ),
            _day(
                7,
                'PHANG NGA BAY SEACAVE CANOEING & GRAND FINALE DINNER',
                (
                    'JAMES BOND ISLAND LIMESTONES & PRIVATE BEACH COVE CELEBRATION Prepare for an awe-inspiring day exploring one of the most magnificent landscapes in Southeast Asia. After breakfast, transfer to the northern pier where a premium speed-craft takes your group across Phang Nga Bay. Cruise past hundreds of vertical limestone karsts rising dramatically out of the calm sea. Arrive at Khao Phing Kan, famously known as James Bond Island, and capture fantastic pictures in front of the floating rock monolith. Next, enjoy a relaxing canoeing experience guided through the mystical sea caves and hidden mangrove lagoons of Koh Hong. Return to the resort to refresh for your final night. TRAGUIN has arranged our ultimate signature surprise: an intimate, completely private beachfront candlelight dinner set in a secluded cove of the resort. Toast your holiday together with a glass of vintage wine under a beautiful sky as gentle waves roll in. Sightseeing Included: James Bond Island, Koh Hong sea cave canoeing, Koh Panyee floating village. Evening Experience: Signature TRAGUIN Grand Finale Private Beachfront Candlelight Dinner.'
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Ocean-Front Private Pool Villa)',
                    'Meals Included: International Buffet Breakfast & Ultra-Luxury Beachside 5-Course Dinner',
                ],
            ),
            _day(
                8,
                'PHUKET DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS Enjoy your final decadent buffet breakfast at your villa veranda, taking a final round of panoramic photos across the tropical resort gardens. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless checkout. At the designated hour, your private luxury executive vehicle arrives to transfer you comfortably to Phuket International Airport. Your travel manager assists with all check-in and luggage procedures, escorting you to the premium departure lounge. Your luxury Bangkok Phuket holiday concludes beautifully, leaving your heart full of unforgettable memories and stories crafted to perfection by TRAGUIN. Sightseeing Included: Private luxury airport departure transfer, premium lounge entry. HANDPICKED ULTRA-LUXURY ACCOMMODATIONS We believe that elite accommodations are the true soul of a premium vacation. TRAGUIN has handpicked the most exceptional properties across Bangkok and Phuket, balancing maximum privacy, top-tier service, and spectacular views. Category Bangkok Stay (3 Nights) Phuket Stay (4 Nights) Option 01: Deluxe Luxury The Sukosol Bangkok Premier Corner Room Novotel Phuket Resort Superior Ocean View Villa Option 02: Premium LuxuryAvani+ Riverside Bangkok Hotel Avani Panorama River Room Phuket Marriott, Merlin Beach Pool View Luxury Room Option 03: Elite Luxury Shangri-La Bangkok Deluxe Horizon River Suite The Shore at Katathani Seaview Premium Pool Villa Option 04: Ultra Luxury Mandarin Oriental, Bangkok Deluxe Chao Phraya Suite Trisara Phuket / Sri Panwa Resort Ocean Front Luxury Pool Villa'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Luxury The Sukosol Bangkok Premier Corner Room Novotel Phuket Resort Superior Ocean View Villa',
                'Multi-city Thailand',
                '7N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Luxury The Sukosol Bangkok Premier Corner Room Novotel Phuket Resort Superior Ocean View Villa',
            ),
            _hotel(
                'LuxuryAvani+ Riverside Bangkok Hotel Avani Panorama River Room Phuket Marriott, Merlin Beach Pool View Luxury Room',
                'Multi-city Thailand',
                '7N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — LuxuryAvani+ Riverside Bangkok Hotel Avani Panorama River Room Phuket Marriott, Merlin Beach Pool View Luxury Room',
            ),
            _hotel(
                'Mandarin Oriental, Bangkok Deluxe Chao Phraya Suite Trisara Phuket / Sri Panwa Resort Ocean Front Luxury Pool Villa',
                'Multi-city Thailand',
                '7N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Mandarin Oriental, Bangkok Deluxe Chao Phraya Suite Trisara Phuket / Sri Panwa Resort Ocean Front Luxury Pool Villa',
            )
        ],
        inclusions=[
            _inc_included('VIP Airport Access: Fast-track airport reception and customs clearance on arrival.', 1),
            _inc_included('Private Vehicles: Private air-conditioned luxury European sedan or van for all transfers.', 2),
            _inc_included('Bespoke Yachting: Private Speedboat Charter to Phi Phi Islands with beachfront lunch.', 3),
            _inc_included('Bay Cruise: Private premium speed-craft tour to James Bond Island with sea canoeing.', 4),
            _inc_included('Special Dining: 1 Private Beachfront Candlelight Grand Finale Dinner & 1 Cruise Gala dinner.', 5),
            _inc_included("Wellness: 120-minute Premium Rejuvenating Group/Couple's Massage session.", 6),
            _inc_included('Flights: International flight tickets connecting home country with Thailand.', 7),
            _inc_excluded('Accommodation: 07 Nights stay in handpicked premium hotels and pool villas.', 8),
            _inc_excluded('Domestic Flights: Internal airfare for Bangkok to Phuket route (Can be added on request).', 9),
            _inc_excluded('Visa Cost: Thailand entry visa charges or fast- track electronic processing fees.', 10),
            _inc_excluded('National Park Fees: Island marine conservation park fees (payable directly on site).', 11),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, mini-bar billing, and tips.', 12),
        ],
    )
    return package, itinerary

def build_th_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-014'
    tour_code = 'TRG-THA-ADV-2026'
    title = 'Phuket • Phi Phi Islands • Krabi • James Bond Island • Koh Yao Noi'
    duration = '06 Nights / 07 Days'
    slug = 'th-014-phuket-phi-phi-islands-krabi-james-bond-island-koh-yao-noi'
    itin_slug = 'th-014-phuket-phi-phi-islands-krabi-james-bond-island-koh-yao-noi-itinerary'
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
            _ph('Serial code TH-014 | TRAGUIN tour code TRG-THA-ADV-2026', 1),
            _ph('State / Country: Thailand | Category: Island Hopping Thailand / Adventure Tour', 2),
            _ph('Destinations: Phuket (3N) + Krabi', 3),
            _ph('Ideal for: Adventure Seekers, Active Families, Thrill Couples', 4),
            _ph('Best season: November to May (Perfect Sailing & Diving Skies)', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Buffet Breakfast (CP), Sea-Cave Barbecues & Cliffside Dinners Unleash your inner explorer with the ultimate Best Thailand Tour Package, meticulously engineered by', 7),
            _ph('TRAGUIN Signature Experience: Private custom speedboats and off-road SUVs, completely avoiding', 8),
            _ph('Curated by TRAGUIN Experts: Safety-certified luxury adventure resorts featuring private beach', 9),
            _ph('Personalized Assistance: English-fluent dedicated local island safety guides to manage activity', 10),
            _ph('Luxury Transportation: Elite executive vehicles equipped with specialized suspension systems,', 11)
        ],
        moods=['Honeymoon', 'Beach', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Phuket',
        overview="TOUR OVERVIEW\nWelcome to the definitive Island Hopping Thailand adventure expedition, uniquely tailored for bold travelers who want to combine rugged marine explorations with elite styling and personal care. Over 7 action-packed days, TRAGUIN will lead your party across spectacular limestone archipelagos. Experience high-speed private speed-craft sailing, deep sea snorkeling over live barrier reefs, sea-cave kayaking, and cliff-scaling adventures. TRAGUIN Curated Experience Note: Your safety and premium status are our top operational priorities. This adventure itinerary features professional PADI-certified guides, top-tier private marine crafts, zero-queue fast- track entries into National Marine Reserves, and 24/7 dedicated local concierge assistance. THE EPIC APPEAL OF A LUXURY THAILAND ADVENTURE TOUR Thailand’s marine geography is an absolute masterpiece of nature, drawing outdoor enthusiasts globally to its jagged limestone karsts and hidden turquoise lagoons. Opting for a specialized Thailand Family Tour or an active Thailand Honeymoon Package configured by TRAGUIN ensures an extraordinary holiday far superior to public group programs. This proposal optimizes top searched keywords for Google ranking, laying out an exceptional overview of premier Thailand Sightseeing. Explore the world's most coveted marine highlights: the famous sheer rock columns of James Bond Island, the crystal-clear diving channels of the Phi Phi Islands, and the vertical climbing walls of Krabi’s Railay Beach. It is the absolute Best Time to Visit Thailand to discover popular Instagram locations from a unique vantage point on the water, try open-ocean sea kayaking, and indulge in a premium holiday experience. TRAGUIN Adventure Signatures: Private high-speed catamaran for island-hopping, sea-cave canoeing through Koh Hong lagoons, professional tandem parasailing, and a sunset beach barbecue dinner on a secluded sandbar. THE ACTION-PACKED DAY-WISE ITINERARY",
        seo_title='TH-014 | Phuket | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Thailand package (TH-014 / TRG-THA-ADV-2026): Phuket (3N) + Krabi with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: PHUKET ARRIVAL & COASTAL OFF-ROAD ORIENTATION', 1),
            _ih('Day 02: DEEP-SEA PHI PHI ISLANDS EXPLORATION', 2),
            _ih('Day 03: PHANG NGA BAY MYSTICAL CANOEING TRAIL', 3),
            _ih('Day 04: PHUKET TO KRABI VIA KOH YAO NOI CORRIDOR', 4),
            _ih('Day 05: KRABI 4-ISLAND ADVENTURE BY SPEED-CRAFT', 5),
            _ih('Day 06: RAILAY BEACH ROCK CLIMBING & COVE BARBECUE FINALE', 6),
            _ih('Day 07: KRABI DEPARTURE', 7),
            _ih('TRAGUIN Signature Experience: Private custom speedboats and off-road SUVs, completely avoiding', 8),
            _ih('Curated by TRAGUIN Experts: Safety-certified luxury adventure resorts featuring private beach', 9),
            _ih('Personalized Assistance: English-fluent dedicated local island safety guides to manage activity', 10)
        ],
        days=[
            _day(
                1,
                'PHUKET ARRIVAL & COASTAL OFF-ROAD ORIENTATION',
                (
                    'WELCOME TO THE EXPEDITION BASE – THE ADVENTURE COMMENCES Your spectacular Island Hopping Thailand expedition hits the ground running the moment you disembark at Phuket International Airport. Clear the arrival gates to receive a premium welcome from your dedicated TRAGUIN tour manager. Avoid the stress of generic coach transfers as you step into your private, rugged luxury 4x4 SUV, designed for maximum comfort and style across coastal paths. Check into your handpicked luxury beachfront resort and gear up for an exciting afternoon. Your guide navigates you up the challenging jungle trails of Nakkerd Hills to stand at the base of the majestic 45-meter Big Buddha monument. This peak offers a staggering 360-degree photography point across Chalong Bay, a perfect opening for your trip gallery. End your day driving down to a high-end surf-side lounge for an absolute welcome dinner under a pastel sky. Sightseeing Included: Private luxury 4x4 SUV airport transit, Nakkerd Hills jungle driving trail, Big Buddha. Evening Experience: Welcome dinner party at a trendy oceanfront surf lounge with live fire-dancing shows.'
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: Curated Grilled Seafood Welcome Dinner',
                ],
            ),
            _day(
                2,
                'DEEP-SEA PHI PHI ISLANDS EXPLORATION',
                (
                    'PRIVATE CATAMARAN SAILING – LAGOON REEFS & SEA-CAVE SNORKELING Savor an early, energizing buffet breakfast layout. Today hosts a cornerstone Premium Thailand Experience: an intense marine voyage across the Andaman Sea. Skip all crowded public ferries as TRAGUIN provides a private high-speed catamaran charter to glide you directly toward the vertical limestone amphitheater of the Phi Phi Islands. Sail right up to Maya Bay, the world-famous paradise sheltered by towering cliffs, to capture high-fashion group pictures on the soft sand. Next, dive into the emerald waters of Pileh Lagoon for an immersive snorkeling session among brilliant coral reefs and multi-colored marine life. Enjoy a private beachfront gourmet lunch specially arranged at a quiet spot on Phi Phi Don, before exploring the historic Viking Cave and Monkey Beach. Sightseeing Included: Maya Bay marine access, Pileh Lagoon reef snorkeling, Bamboo Island sandbar, Viking Cave. Optional Activities: Deep-sea tandem scuba diving under expert PADI instruction over live deep barrier reefs.'
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Beachfront Island Island Lunch',
                ],
            ),
            _day(
                3,
                'PHANG NGA BAY MYSTICAL CANOEING TRAIL',
                (
                    'JUNGLE SEA LAGOONS, HONG ISLAND CAVES & JAMES BOND ISLAND Prepare for an action-packed day uncovering hidden geographical wonders. Following breakfast, board your private speed-craft to explore Phang Nga Bay. Cruise past hundreds of staggering limestone towers rising straight out of the calm sea, a prominent highlight of Phuket Sightseeing. Anchor near Koh Hong where professional sea-kayakers guide your canoes through narrow rocky arches into hidden interior lagoons completely isolated from the outer ocean—consistently named a top popular Instagram location. Next, speed towards James Bond Island to photograph the iconic needle-shaped rock monolith. Enjoy a fresh seafood lunch at the stilted floating village of Koh Panyee before heading back to base. Sightseeing Included: James Bond Island, Koh Hong sea-cave canoeing, Koh Panyee stilted village exploration. Evening Experience: Night walk through the energetic Patong street markets for boutique shopping and street food.'
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Floating Village Seafood Lunch',
                ],
            ),
            _day(
                4,
                'PHUKET TO KRABI VIA KOH YAO NOI CORRIDOR',
                (
                    "SOCIALLY DISTANCED ISLAND TRANSIT & ACTIVE AO NANG EXPLORATION Check out of Phuket after breakfast. Today's transit is an absolute adventure in itself. TRAGUIN charts a custom marine route via a private speedboat across the Phang Nga archipelago, making a special stop at the pristine island of Koh Yao Noi. Rent local scooters or off-road bicycles to explore rustic coconut fields and quiet sand beaches, capturing spectacular landscapes. In the afternoon, cruise directly into the docks of Krabi, transitioning seamlessly to your premium cliffside resort near Ao Nang beach. Krabi is adored globally for its sheer vertical rock faces, making it a dream for a Luxury Thailand Holiday. Spend your evening exploring the lively Ao Nang walking street, packed with authentic street cafes and artisan shops. Sightseeing Included: Private Speedboat island transit, Koh Yao Noi interior cycling tour, Ao Nang arrival. Evening Experience: Catching the breathtaking sunset from a stylish cliffside bar overlooking Ao Nang Bay."
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Cliffside or Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Local Thai Open-Air Bistro Lunch',
                ],
            ),
            _day(
                5,
                'KRABI 4-ISLAND ADVENTURE BY SPEED-CRAFT',
                (
                    'SECRET SANDBARS, CORAL REEFS & HIGH-ADRENALINE GULF SPORTS Gear up for an iconic highlight of Krabi Sightseeing. After breakfast, a private speed-craft picks your group up directly from the resort beach for a thrilling day across Krabi’s 4-Islands. Visit Phra Nang Cave Beach, renowned for its vertical rock climbers and sea shrines, before speeding towards Tup Island, where a magnificent natural sandbar emerges at low tide, allowing you to walk on water between islands. The afternoon brings high-adrenaline action. Your package includes an exhilarating parasailing flight for incredible birds-eye views of the coast, alongside an exciting banana boat ride at Poda Island. Snorkel over the vibrant coral reefs of Chicken Island, surrounded by schools of tropical fish. Return to the resort to refresh before an incredible evening dinner party. Sightseeing Included: Phra Nang Cave, Tup Island Sandbar, Poda Island beach access, Chicken Island reefs. Optional Activities: Undersea sea-walking or high-speed private jet-ski tours around the outer limestone towers.'
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Cliffside or Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Premium Beachside Seafood Barbecue Lunch',
                ],
            ),
            _day(
                6,
                'RAILAY BEACH ROCK CLIMBING & COVE BARBECUE FINALE',
                (
                    "VERTICAL THRILLS & A SIGNATURE GRAND FINALE SANDBAR DINNER Dedicate today to one of the top tourist places in Thailand: the secluded peninsula of Railay Beach, cut off from the mainland by massive vertical walls. Following breakfast, transfer by longtail boat to Railay's iconic limestone faces. Under the supervision of certified expert instructors, enjoy a private 4-hour rock-climbing lesson, reaching views overlooking the entire turquoise gulf. Spend your afternoon exploring hidden caves or swimming at Railay West beach. For your final night, TRAGUIN has arranged our ultimate signature surprise: an intimate private beachfront candlelight dinner barbecue set in a secluded cove. Toast your adventure holiday with a glass of fine wine under a starlit sky as gentle waves roll in. Sightseeing Included: Railay Beach peninsula access, private guided rock-climbing session, sea-cave walking. Evening Experience: Signature TRAGUIN Grand Finale Private Beachfront Candlelight Barbecue Dinner."
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Cliffside or Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & 5-Course Cove Barbecue Dinner',
                ],
            ),
            _day(
                7,
                'KRABI DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER FEARLESS Savor your final morning breakfast looking out over the majestic Krabi cliffs. Take a final dip in your resort’s infinity pool or enjoy a late walk along the sand, capturing your final group pictures to commemorate an exceptional adventure. At the designated hour, your private luxury SUV arrives to transfer you comfortably to Krabi International Airport for your departure flight back home. As you board your aircraft, look back on an exceptional collection of curated experiences, breathtaking landscapes, and unforgettable family memories crafted beautifully by TRAGUIN. Your premium expedition concludes, leaving you inspired and forever fearless. Sightseeing Included: Private luxury airport departure transfer.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Phuket Resort Superior Ocean View Room (BB) Ao Nang Cliff Beach Resort Ocean View Suite (BB)',
                'Multi-city Thailand',
                '6N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Novotel Phuket Resort Superior Ocean View Room (BB) Ao Nang Cliff Beach Resort Ocean View Suite (BB)',
            ),
            _hotel(
                'Phuket Marriott Resort, Merlin Beach Pool View Luxury Room (BB) Centara Grand Beach Resort Krabi Deluxe Ocean Face Room (BB)',
                'Multi-city Thailand',
                '6N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Phuket Marriott Resort, Merlin Beach Pool View Luxury Room (BB) Centara Grand Beach Resort Krabi Deluxe Ocean Face Room ',
            ),
            _hotel(
                'The Westin Siray Bay Resort & Spa Luxury Seaview Suite (BB) Rayavadee Krabi Resort Deluxe Pavilion Estate (BB)',
                'Multi-city Thailand',
                '6N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Westin Siray Bay Resort & Spa Luxury Seaview Suite (BB) Rayavadee Krabi Resort Deluxe Pavilion Estate (BB)',
            ),
            _hotel(
                'Trisara Phuket / Sri Panwa Resort Ocean Front Luxury Pool Villa (BB) Phulay Bay, a Ritz-Carlton Reserve Reserve Pavilion Pool Villa (BB)',
                'Multi-city Thailand',
                '6N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Trisara Phuket / Sri Panwa Resort Ocean Front Luxury Pool Villa (BB) Phulay Bay, a Ritz-Carlton Reserve Reserve Pavilion',
            )
        ],
        inclusions=[
            _inc_included('Flights: International flight tickets connecting home country with Thailand.', 1),
            _inc_excluded('PACKAGE INCLUSIONS', 2),
        ],
    )
    return package, itinerary

def build_th_015(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-015'
    tour_code = 'TRG-KBV-ADV-2026'
    title = 'KRABI ADVENTURE ITINERARY Ao Nang Bay • Railay Peninsula • Koh Hong Lagoons • Tiger Cave Peak'
    duration = '05 Nights / 06 Days'
    slug = 'th-015-krabi-adventure-itinerary-ao-nang-bay-railay-peninsula-koh-hong-lagoons-tiger-cave-peak'
    itin_slug = 'th-015-krabi-adventure-itinerary-ao-nang-bay-railay-peninsula-koh-hong-lagoons-tiger-cave-peak-itinerary'
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
            _ph('Serial code TH-015 | TRAGUIN tour code TRG-KBV-ADV-2026', 1),
            _ph('State / Country: Thailand | Category: Adventure Holiday / Luxury Expedition', 2),
            _ph('Destinations: Krabi Wild & Coastal', 3),
            _ph('Ideal for: Thrill Seekers, Active Families, Adventure Honeymooners', 4),
            _ph('Best season: November to May (Clear Turquoise Diving Conditions)', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Buffet Breakfast (CP), Jungle Barbecues & Cliffside Sunset Dinners Challenge your boundaries with the absolute Best Krabi Tour Package, masterfully engineered by', 7),
            _ph('TRAGUIN Signature Experience: Private custom speedboats and off-road SUVs, completely avoiding', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified luxury adventure resorts featuring private beach', 9),
            _ph('Personalized Assistance: English-fluent dedicated local island safety guides to manage activity', 10),
            _ph('Luxury Transportation: Elite executive vehicles equipped with specialized suspension systems,', 11)
        ],
        moods=['Luxury', 'Honeymoon', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='KRABI ADVENTURE ITINERARY Ao Nang Bay',
        overview="Ao Nang Bay • Railay Peninsula • Koh Hong Lagoons • Tiger Cave Peak 05 Nights / 06 Days High-Octane Luxury Action Expedition SERIAL CODE: TH-015 TRAGUIN TOUR CODE: TRG-KBV-ADV-2026 STATE / COUNTRY: Thailand / Krabi CATEGORY: Adventure Holiday / Luxury Expedition DURATION: 05 Nights / 06 Days DESTINATIONS: Krabi Wild & Coastal Reserves (5N) IDEAL FOR: Thrill Seekers, Active Families, Adventure Honeymooners BEST SEASON: November to May (Clear Turquoise Diving Conditions) VEHICLE & CRAFT: Private Luxury SUV & Dedicated High-Speed Private Marine Crafts MEAL PLAN: Buffet Breakfast (CP), Jungle Barbecues & Cliffside Sunset Dinners Challenge your boundaries with the absolute Best Krabi Tour Package, masterfully engineered by TRAGUIN to drop your travel squad straight into Thailand's most dramatic landscape. This elite Luxury Krabi Holiday weaves adrenaline-pumping vertical rock climbs and hidden mangrove sea-cave trails into premium stays, providing breathtaking landscapes and unforgettable memories.\n\nTOUR OVERVIEW\nWelcome to the definitive Krabi Adventure blueprint, an elite 6-day active vacation structured by TRAGUIN for travelers who refuse standard tourist tracks. Your expedition group will explore pure turquoise marine canyons, scale ancient limestone monoliths rising from the sea, trek through wild rainforest pools, and pilot sea canoes into isolated sea chambers. Enjoy seamless private logistics in robust 4x4 luxury SUVs and high- performance private speed-crafts. TRAGUIN Curated Experience Note: Your safety and VIP status remain our absolute operational benchmark. This active itinerary includes dedicated PADI-certified marine masters, professional rock-climbing safety marshals, fast-track entry into national marine reserves, and 24/7 dedicated on-ground concierge support. THE THRILL OF A LUXURY THAILAND ADVENTURE HOLIDAY Krabi is globally recognized as the ultimate geological playground for active luxury, drawing outdoor enthusiasts to its iconic vertical rock cliffs and mysterious marine networks. Choosing a premium Krabi Family Tour or a dedicated Krabi Honeymoon Package through TRAGUIN guarantees private access to hidden islands away from commercial crowds. This proposal utilizes highly searched keywords to deliver an exceptional layout of premier Krabi Sightseeing spots. Explore top tourist places in Krabi: the towering sheer monoliths of Railay Beach, the luminous emerald interior pools of the Crystal Lagoon, and the breathtaking vertical steps of the Tiger Cave Temple. It is the absolute Best Time to Visit Krabi to discover popular Instagram locations from a completely unique, active vantage point, indulge in luxury eco-resorts, and collect deep, immersive experiences. TRAGUIN Adventure Inclusions: Private speedboat charter to the Koh Hong Archipelago, expert longtail boat passage to Railay Peninsula, a private 4-hour guided rock-climbing program, and an exclusive jungle cliff sunset dinner party. THE HIGH-OCTANE DAY-WISE ITINERARY",
        seo_title='TH-015 | KRABI ADVENTURE ITINERARY Ao Nang Bay | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-015 / TRG-KBV-ADV-2026): Krabi Wild & Coastal with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN KRABI & SCENIC JUNGLE TREK TO EMERALD POOL', 1),
            _ih('Day 02: RAILAY PENINSULA VERTICAL ROCK CLIMBING', 2),
            _ih('Day 03: HONG ISLANDS ARCHIPELAGO BY PRIVATE SPEEDBOAT', 3),
            _ih('Day 04: THE TIGER CAVE TEMPLE PEAK CHALLENGE', 4),
            _ih('Day 05: KRABI 4-ISLANDS MARINE ATHLETICS & COVE BBQ FINALE', 5),
            _ih('Day 06: KRABI DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private custom speedboats and off-road SUVs, completely avoiding', 7),
            _ih('Curated by TRAGUIN Experts: Safety-verified luxury adventure resorts featuring private beach', 8),
            _ih('Personalized Assistance: English-fluent dedicated local island safety guides to manage activity', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN KRABI & SCENIC JUNGLE TREK TO EMERALD POOL',
                (
                    'WELCOME TO THE WILD SANCTUARY – UNLEASHING THE COASTAL EXPEDITION Your spectacular Krabi Adventure begins the moment your plane lands at Krabi International Airport. Step through arrival to receive your VIP welcome from your private TRAGUIN expedition coordinator. Skip the delays of public transfers as you step directly into your private, high-chassis luxury 4x4 SUV. Drive through scenic plantation corridors toward the interior tropical rainforest of Khao Phra Bang Khram Nature Reserve. Embark on a mild, immersive 1.5-kilometer jungle trek along raised wooden walkways under giant fan palms. Arrive at the spectacular Emerald Pool (Sa Morakot), a natural freshwater basin filled with crystal-clear, therapeutic geothermal water originating from deep volcanic streams. Swim inside this natural pool before walking further up to the magical Blue Pool, a vibrant photography point. Transfer to your premium beachfront resort in Ao Nang to unpack and refresh, concluding with an open-air welcome dinner. Sightseeing Included: Private luxury 4x4 SUV airport transit, Khao Phra Bang Khram jungle trek, Emerald Pool, Blue Pool. Evening Experience: Welcome dinner party at a trendy seaside surf lounge featuring traditional live fire-spinning artists.'
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Beachfront or Cliffside Resort)',
                    'Meals Included: Curated Grilled Seafood Welcome Dinner',
                ],
            ),
            _day(
                2,
                'RAILAY PENINSULA VERTICAL ROCK CLIMBING',
                (
                    'LIMESTONE VERTICAL THRILLS & HIDDEN PHRA NANG SEA CAVES Savor an early, high-protein buffet breakfast at your resort. Board a private longtail speed-craft from Ao Nang beach to cruise past colossal limestone cliffs to the isolated Railay Peninsula, accessible entirely by water. Railay is adored globally as the gold standard for vertical rock athletics, making it a dream destination for a Luxury Krabi Holiday. Meet your certified expert climbing safety marshals for a private 4-hour rock-climbing masterclass on the sheer limestone face of Phra Nang Cliff. Scale vertical paths tailored to your skill level, reaching breathtaking viewpoints overlooking the entire turquoise gulf. Spend your afternoon exploring the mystical Phra Nang Cave beach, observing historic sea shrines and taking fantastic group pictures before cruising back to your resort base. Sightseeing Included: Private boat transit, Railay West beach access, 4-hour guided rock climbing, Phra Nang Cave. Optional Activities: Trekking the steep, challenging muddy trail up to the hidden internal Railay Lagoon.'
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Cliffside or Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Cliffside Bistro Lunch Layout',
                ],
            ),
            _day(
                3,
                'HONG ISLANDS ARCHIPELAGO BY PRIVATE SPEEDBOAT',
                (
                    'DEEP-SEA SPEED-CRAFT SAILING – SEA CAVE CANOEING & THE 360 PANORAMA Prepare for an action-packed day uncovering hidden geographical wonders. Following breakfast, board your private high-performance speed-craft to explore the Koh Hong Archipelago, a prominent highlight of Krabi Sightseeing. Skip the crowded tourist schedules as your boat glides past dramatic rock pillars directly to the narrow entrance of Hong Island’s interior secret lagoon. Pilot your stable sea canoes hand-in-hand through the shallow water of the mangrove lagoon, completely enclosed by massive vertical cliffs—consistently named a top popular Instagram location. Next, land at Hong Island beach to ascend the spectacular 419-step metal walkway up to the 360-degree viewpoint platform. Witness a breathtaking panorama across hundreds of tiny islands in Phang Nga Bay. Enjoy a beachfront picnic lunch before snorkeling among reef fish. Sightseeing Included: Private Speedboat charter, Koh Hong Lagoon entry, 360-degree Viewpoint climb, Lading Island. Optional Activities: Deep-sea tandem sea-scuba diving or high-speed sea jet-skiing under specialist instruction.'
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Cliffside or Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Beachfront Gourmet Picnic Lunch',
                ],
            ),
            _day(
                4,
                'THE TIGER CAVE TEMPLE PEAK CHALLENGE',
                (
                    "1,260 VERTICAL CHALLENGING STEPS & SACRED SIAMESE HISTORY Today combines serious physical challenge with deep spiritual reward. After breakfast, your private luxury SUV transfers you inland to the ancient Wat Tham Suea, beautifully known as the Tiger Cave Temple. Nestled inside a valley of ancient trees, this site is a prominent landmark of Top Tourist Places in Krabi. Begin the intense vertical ascent up the mountain side, climbing exactly 1,260 challenging concrete steps. Challenge your limits alongside your group, navigating steep paths home to local monkey troops. Arrive at the mountain summit to stand before a massive golden Buddha statue and an ancient pagoda. The peak offers a staggering panoramic view across Krabi's rolling green plains and limestone formations. Return to your resort for a well-deserved afternoon spa treatment. Sightseeing Included: Tiger Cave Temple mountain climb, internal archaeological labyrinth cave exploration. Evening Experience: A therapeutic 90-minute sport muscle relaxation massage at a premium day spa pavilion."
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Cliffside or Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Authentic Local Thai Bistro Lunch',
                ],
            ),
            _day(
                5,
                'KRABI 4-ISLANDS MARINE ATHLETICS & COVE BBQ FINALE',
                (
                    'SECRET SANDBAR WALKING, PARASAILING THRILLS & CANDLELIGHT CELEBRATION Gear up for an iconic finale across Krabi’s legendary marine parks. Following breakfast, a private speed-craft launches directly from the resort sands for a thrilling multi-island journey. Visit Tup Island, where a unique natural sandbar emerges at low tide, allowing your group to walk on crystal water between islands. Snorkel over the live barrier reefs of Chicken Island, surrounded by schools of tropical fish. Take part in exciting marine athletics at Poda Island, featuring an exhilarating parasailing flight for birds-eye views of the coast, alongside an exciting banana boat ride. For your final evening, TRAGUIN has arranged our ultimate signature surprise: an intimate, completely private beachfront candlelight barbecue dinner set in a secluded cove. Toast your adventure holiday with a glass of fine wine under a starlit sky as gentle waves roll in. Sightseeing Included: Tup Island Sandbar walk, Chicken Island reef snorkeling, Poda Island beach access, Parasailing. Evening Experience: Signature TRAGUIN Grand Finale Private Beachfront Candlelight Barbecue Dinner.'
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Cliffside or Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & 5-Course Private Cove Barbecue Dinner',
                ],
            ),
            _day(
                6,
                'KRABI DEPARTURE',
                (
                    'CHERISHING ROMANTIC MEMORIES BEYOND DESTINATIONS – FOREVER REFRESHED Savor your final morning breakfast looking out over the majestic Krabi limestone cliffs. Take a final dip in your resort’s infinity edge pool or enjoy a slow walk along the soft sand of Ao Nang beach, capturing your final group pictures to commemorate an exceptional trip. Your private luxury SUV arrives to transfer your party comfortably to Krabi International Airport for your departure flight back home. As you board your aircraft, look back on an exceptional collection of curated experiences, breathtaking landscapes, and unforgettable family memories crafted beautifully by TRAGUIN. Your premium active vacation concludes, leaving you rested, fulfilled, and full of stories. Sightseeing Included: Private luxury airport departure transfer.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Ao Nang Cliff Beach Resort Ocean View Suite Complimentary Welcome Drinks & Free Rock-Climbing Map Guide',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Ao Nang Cliff Beach Resort Ocean View Suite Complimentary Welcome Drinks & Free Rock-Climbing Map Guide',
            ),
            _hotel(
                'Centara Grand Beach Resort Krabi Deluxe Ocean Face Room Private Speedboat Dock Access & 1 Beachfront Cocktail Voucher per guest',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Centara Grand Beach Resort Krabi Deluxe Ocean Face Room Private Speedboat Dock Access & 1 Beachfront Cocktail Voucher pe',
            ),
            _hotel(
                'Rayavadee Krabi Resort Deluxe Pavilion Estate Daily Fruit Basket, Pre-Booked Railay Climbing safety marshals & Bath Setup',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Rayavadee Krabi Resort Deluxe Pavilion Estate Daily Fruit Basket, Pre-Booked Railay Climbing safety marshals & Bath Setu',
            ),
            _hotel(
                'Phulay Bay, a Ritz-Carlton Reserve Reserve Pavilion Pool Villa Premium Vintage Champagne Bottle, Private Cove access & 24/7 Personal Butler Support',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Phulay Bay, a Ritz-Carlton Reserve Reserve Pavilion Pool Villa Premium Vintage Champagne Bottle, Private Cove access & 2',
            )
        ],
        inclusions=[
            _inc_included('Daily Meals: 5 International Buffet Breakfasts, 3 Adventure Lunches, 2 Curated Dinners.', 1),
            _inc_included('Private Vehicles: Dedicated luxury 4x4 SUV for all point-to-point tours and airport transits.', 2),
            _inc_included('Bespoke Charters: Private Speedboat for Koh Hong Archipelago and Krabi 4-Islands.', 3),
            _inc_included('Adrenaline Kit: Included Parasailing flight, Banana Boat ride, and Railay Rock Climbing gear.', 4),
            _inc_included('Rainforest Access: Included entry tickets to Emerald Pool and Tiger Cave Temple.', 5),
            _inc_included('Flights: International flight tickets connecting home country with Krabi.', 6),
            _inc_excluded('Accommodation: 05 Nights stay in handpicked premium adventure hotels.', 7),
            _inc_excluded('Visa Costs: Thailand entry visa charges or fast- track electronic visa processing fees.', 8),
            _inc_excluded('National Park Entry: Island marine conservation park entry fees (payable directly on site).', 9),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, mini-bar billing, and tips.', 10),
            _inc_excluded('Optional Activities: Deep-sea tandem scuba diving or private jet-ski tours.', 11),
        ],
    )
    return package, itinerary

def build_th_016(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-016'
    tour_code = 'TRG-PAT-FAM-2026'
    title = 'Pattaya Beach • Coral Island • Nong Nooch • Columbia Pictures Aquaverse'
    duration = '04 Nights / 05 Days'
    slug = 'th-016-pattaya-beach-coral-island-nong-nooch-columbia-pictures-aquaverse'
    itin_slug = 'th-016-pattaya-beach-coral-island-nong-nooch-columbia-pictures-aquaverse-itinerary'
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
            _ph('Serial code TH-016 | TRAGUIN tour code TRG-PAT-FAM-2026', 1),
            _ph('State / Country: Thailand | Category: Premium Family Tour', 2),
            _ph('Destinations: Pattaya (4 Nights Luxury', 3),
            _ph('Ideal for: Families, Multi- generational Groups, Kids Special', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Safe Luxury Van (Toyota Commuter / Majestic) / Buffet Breakfast (CP) & Specialized Indian/Thai Family Dinners Treat your loved ones to a magical tropical vacation with the Best Pattaya Tour Pa', 7),
            _ph('TRAGUIN Signature Experience: Private custom speedboats and theme park fast-track passes,', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 9),
            _ph('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 10),
            _ph('Luxury Transportation: Executive modern vehicles equipped with cooling, on-board entertainment', 11)
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
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Pattaya Beach',
        overview='TOUR OVERVIEW\nWelcome to your meticulously designed Pattaya Family Fun escape, precisely structured for modern families who expect seamless coordination, children-friendly paces, and elite hospitality. Across 5 incredible days, TRAGUIN ensures a flawless holiday format filled with curated experiences. Travel in completely safe, private, air-conditioned luxury vans with dedicated chauffeurs, completely bypassing the exhaustion of public coach queues. TRAGUIN Curated Experience Note: From spacious interconnected family suites to kid-special attraction access and pre-arranged authentic Indian dining choices, your holiday is managed by our dedicated destination team. Our 24/7 on-ground assistance guarantees peace of mind at every step. THE MAGIC OF A LUXURY PATTAYA HOLIDAY Pattaya has evolved into the ultimate family entertainment capital of Southeast Asia, offering an unmatched variety of interactive wildlife reserves, massive water parks, and beautiful coastal islands. Choosing one of our high-end TRAGUIN Pattaya Packages or an exceptional Thailand Family Tour means stepping past generic travel routes into a world of exclusive benefits. This proposal targets top searched tourism keywords for Google ranking, ensuring the ultimate showcase of Pattaya Sightseeing. Discover Top Tourist Places in Pattaya: the crystal lagoons of Coral Island, the world’s first Columbia Pictures movie theme park, and the breathtaking botanical valley of Nong Nooch. It is universally recognized as the Best Time to Visit Pattaya to explore popular Instagram locations, engage in exciting marine sports, and collect immersive experiences that your children will cherish for a lifetime. TRAGUIN Family Signatures: Private speedboat charter to Coral Island with safe kid-friendly water sports, premium VIP front-row seating at the Alcazar Show, full-day access to Columbia Pictures Aquaverse, and dedicated family transportation. THE DEFINITIVE DAY-WISE ITINERARY',
        seo_title='TH-016 | Pattaya Beach | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Thailand package (TH-016 / TRG-PAT-FAM-2026): Pattaya (4 Nights Luxury with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: BANGKOK ARRIVAL & PRIVATE TRANSIT TO PATTAYA', 1),
            _ih('Day 02: PRIVATE SPEEDBOAT TO CORAL ISLAND', 2),
            _ih('Day 03: NONG NOOCH GARDENS TOUR & SANCTUARY OF TRUTH', 3),
            _ih('Day 04: COLUMBIA PICTURES AQUAVERSE FULL-DAY ADVENTURE', 4),
            _ih('Day 05: PATTAYA RETREAT & BANGKOK DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private custom speedboats and theme park fast-track passes,', 6),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 7),
            _ih('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 8)
        ],
        days=[
            _day(
                1,
                'BANGKOK ARRIVAL & PRIVATE TRANSIT TO PATTAYA',
                (
                    'WELCOME TO THAILAND – THE FAMILY CELEBRATION COMMENCES Your spectacular Pattaya Family Tour begins perfectly the moment your family arrives at Bangkok’s Suvarnabhumi or Don Mueang International Airport. As you emerge from the arrival gates, a warm, traditional Thai greeting awaits your party, coordinated seamlessly by your dedicated TRAGUIN tour representative. You will be escorted to your air-conditioned private luxury van, ensuring a completely relaxed, scenic cross- province highway transfer down to the beautiful resort bay of Pattaya. Arrive at your handpicked premium resort and check into your ocean-facing room, featuring special welcome amenities for the children. Spend the afternoon unwinding by the massive lagoon swimming pool or taking your first family photos overlooking the sunset. In the evening, your private van takes you to a premium Indian restaurant for a welcome buffet dinner filled with familiar comforts, ensuring a restful start for an unforgettable family vacation. Sightseeing Included: Private luxury van airport transit, scenic coastal highway drive, Pattaya Beach Road orientation. Evening Experience: Family welcome dinner at an upscale restaurant with gorgeous ocean vistas.'
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Family Resort with Water Slides)',
                    'Meals Included: Curated Multi-Cuisine Indian Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PRIVATE SPEEDBOAT TO CORAL ISLAND',
                (
                    'SUN-KISSED SANDS, AQUATIC SPORTS & ALCAZAR THEATER GALA Wake up to a gorgeous morning over the water and enjoy a lavish buffet breakfast. Today hosts one of the most searched experiences in the region: an island-hopping trip across the Gulf of Thailand to Koh Larn, affectionately known as Coral Island. Avoid the crowded regular public tour boats as TRAGUIN arranges a private, high-speed luxury speedboat to pick up your family directly from the resort beach front. Cruise over crystal-clear turquoise waters to arrive at a secluded stretch of soft sand, offering a premium photography point for the family. The kids can swim in the calm shallow waters while the adults take part in exciting parasailing flights or a fast banana boat ride over the waves. Savor a delicious fresh seafood or Indian lunch served right by the beach. Return to the mainland to refresh before heading to the globally acclaimed Alcazar Cabaret Show, where we have pre-booked premium VIP front-row seats for your family to enjoy world-class theatrical dance sequences. Sightseeing Included: Private Speedboat to Coral Island, beach active access, VIP entry to Alcazar Show. Optional Activities: Undersea Sea-Walking or Glass-Bottom Boat coral reef viewing for children and seniors.'
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Family Resort with Water Slides)',
                    'Meals Included: International Buffet Breakfast & Beachside Family Lunch',
                ],
            ),
            _day(
                3,
                'NONG NOOCH GARDENS TOUR & SANCTUARY OF TRUTH',
                (
                    'BOTANICAL MARVELS, CULTURAL DRAMA & SIAMESE ARCHITECTURE Enjoy a beautiful morning breakfast before starting a comprehensive Pattaya Sightseeing cultural tour. Your private chauffeur navigates your family to the world-famous Nong Nooch Botanical Gardens. Spanning over 500 acres of meticulously designed themed valleys, it features breathtaking landscapes. TRAGUIN provides private open-air electric carts to guide your family through the orchid paths and dinosaur valleys without any physical fatigue. Enjoy a spectacular Thai Cultural and Elephant show inside the air-conditioned theater complex. Following a beautiful buffet lunch inside the gardens, continue to the awe-inspiring Sanctuary of Truth. This monumental 100-meter-tall seaside structure is constructed entirely of hand-carved wood without a single metal nail, representing ancient philosophies. It stands as an incredible popular Instagram location, perfect for iconic family portraits. Return to your resort for an evening of leisure or explore the local night bazaars. Sightseeing Included: Nong Nooch Gardens entry, electric cart tour, Cultural Show, Sanctuary of Truth tour. Evening Experience: Boutique shopping and street food snacks exploration at the Pattaya Floating Market.'
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Family Resort with Water Slides)',
                    'Meals Included: International Buffet Breakfast & Nong Nooch Garden Buffet Lunch',
                ],
            ),
            _day(
                4,
                'COLUMBIA PICTURES AQUAVERSE FULL-DAY ADVENTURE',
                (
                    "CINEMATIC WATER SLIDES, THRILLING SURF ZONES & GOURMET FINALE Dedicate today to pure, high-octane family joy at Columbia Pictures Aquaverse—the world's very first fully branded movie theme water park. Following a hearty breakfast, your private luxury van drops your group at the entrance gates with pre-arranged fast-track tickets. Step into highly immersive zones themed around blockbuster movies like *Ghostbusters*, *Jumanji*, *Hotel Transylvania*, and *Bad Boys*. The children will be fully entertained exploring massive water play structures, riding thrilling water coasters, and swimming in the giant wave pool featuring live music entertainment. Adults can test their balance at the Surf's Up flow-rider machine or relax along the scenic lazy river channels. For your final evening, TRAGUIN has arranged a special grand finale dinner party at an elegant oceanfront rooftop restaurant, allowing you to toast to an extraordinary family holiday under a starlit sky. Sightseeing Included: Full-day admission pass to Columbia Pictures Aquaverse, private theme park transits. Optional Activities: Go-Kart racing at EasyKart Pattaya or a visit to Underwater World Pattaya marine tunnels. Evening Experience: Signature TRAGUIN Grand Finale Oceanfront Family Dinner Party with live music."
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Family Resort with Water Slides)',
                    'Meals Included: International Buffet Breakfast & 4-Course Oceanfront Farewell Dinner',
                ],
            ),
            _day(
                5,
                'PATTAYA RETREAT & BANGKOK DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER UNITED Savor your final morning breakfast at your premium resort, capturing a final round of group family photos across the tropical landscaped gardens. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless checkout. Depending on your flight departure schedule from Bangkok, your private van remains available for last-minute souvenir shopping or a brief stop at a seaside cafe to grab an authentic Thai iced tea. Your private vehicle delivers you safely to Suvarnabhumi or Don Mueang International Airport for your return flight home. Your premium Pattaya Family Fun tour concludes beautifully, leaving your loved ones with unforgettable memories crafted to perfection by TRAGUIN. Sightseeing Included: Private luxury airport departure transfer, souvenir shopping stop.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Pattaya Modus Beachfront Resort Deluxe Family Ocean Room Complimentary Welcome Drinks & Access to Kids Club Play Zone',
                'Multi-city Thailand',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Novotel Pattaya Modus Beachfront Resort Deluxe Family Ocean Room Complimentary Welcome Drinks & Access to Kids Club Play',
            ),
            _hotel(
                'Amari Pattaya Resort Deluxe Family Horizon Suite Welcome Fruit Platters, Free Ice Cream for Kids & Large Water Pool Access',
                'Multi-city Thailand',
                '4N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Amari Pattaya Resort Deluxe Family Horizon Suite Welcome Fruit Platters, Free Ice Cream for Kids & Large Water Pool Acce',
            ),
            _hotel(
                'Centara Grand Mirage Beach Resort Pattaya Premium Deluxe Ocean View Family Suite Full Lost-World Waterpark Access & Pre-booked Kids Entertainment Vouchers',
                'Multi-city Thailand',
                '4N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Centara Grand Mirage Beach Resort Pattaya Premium Deluxe Ocean View Family Suite Full Lost-World Waterpark Access & Pre-',
            ),
            _hotel(
                'Grande Centre Point Space Pattaya Space Premium Interconnected Family Suite Bespoke Space-Themed Waterpark Passes, Private Token Vouchers & 24/7 Butler Care',
                'Multi-city Thailand',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Grande Centre Point Space Pattaya Space Premium Interconnected Family Suite Bespoke Space-Themed Waterpark Passes, Priva',
            )
        ],
        inclusions=[
            _inc_included('Daily Meals: 4 International Buffet Breakfast layouts with children-friendly sections.', 1),
            _inc_included('Private Vehicles: Private air-conditioned luxury van with an experienced driver for all transfers.', 2),
            _inc_included('Pattaya Cruise: Private Speedboat to Coral Island with parasailing and banana boat rides.', 3),
            _inc_included('VIP Sightseeing: Premium front-row seats at the Alcazar Cabaret Show with private transfers.', 4),
            _inc_included('Airfare: International flight tickets from your home country to Bangkok.', 5),
            _inc_excluded('Accommodation: 04 Nights stay in handpicked premium family resorts.', 6),
            _inc_excluded('Visa Fees: Thailand Visa-on-Arrival or fast-track electronic visa processing fees.', 7),
        ],
    )
    return package, itinerary

def build_th_017(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-017'
    tour_code = 'TRG-PAT-CRL-2026'
    title = 'CORAL ISLAND SPECIAL Pattaya Beach • Coral Island Ultra Escape • Nong Nooch Gardens • Underwater World'
    duration = '04 Nights / 05 Days'
    slug = 'th-017-coral-island-special-pattaya-beach-coral-island-ultra-escape-nong-nooch-gardens-underwater-world'
    itin_slug = 'th-017-coral-island-special-pattaya-beach-coral-island-ultra-escape-nong-nooch-gardens-underwater-world-itinerary'
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
            _ph('Serial code TH-017 | TRAGUIN tour code TRG-PAT-CRL-2026', 1),
            _ph('State / Country: Thailand | Category: Coral Island Special Family Tour', 2),
            _ph('Destinations: Pattaya (4 Nights', 3),
            _ph('Ideal for: Families, Ocean Lovers, Multi-generational Groups', 4),
            _ph('Best season: November to April (Pristine Coral Underwater Visibility)', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Executive Van (Toyota Commuter / Majestic) / Buffet Breakfast (CP), Private Island Lunch & Themed Dinners Surrender to the coastal charm of the Gulf of Thailand with the Best Pattaya To', 7),
            _ph('TRAGUIN Signature Experience: Private custom speedboats and marine park fast-track passes,', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 9),
            _ph('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 10),
            _ph('Luxury Transportation: Executive modern vehicles equipped with cooling, on-board entertainment', 11)
        ],
        moods=['Family', 'Honeymoon', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='CORAL ISLAND SPECIAL Pattaya Beach',
        overview='04 Nights / 05 Days Premium Family Tour Package SERIAL CODE: TH-017 TRAGUIN TOUR CODE: TRG-PAT-CRL-2026 STATE / COUNTRY: Thailand CATEGORY: Coral Island Special Family Tour DURATION: 04 Nights / 05 Days DESTINATIONS: Pattaya (4 Nights Executive Beach Side Stay) IDEAL FOR: Families, Ocean Lovers, Multi-generational Groups BEST SEASON: November to April (Pristine Coral Underwater Visibility) VEHICLE TYPE: Private Luxury Executive Van (Toyota Commuter / Majestic) MEAL PLAN: Buffet Breakfast (CP), Private Island Lunch & Themed Dinners Surrender to the coastal charm of the Gulf of Thailand with the Best Pattaya Tour Package, explicitly engineered by TRAGUIN to highlight the turquoise glory of Koh Larn. This specialized Pattaya Family Tour brings you a magnificent Luxury Pattaya Holiday wrapped in beautiful premium stays, presenting breathtaking landscapes and creating unforgettable memories for your entire family circle.\n\nTOUR OVERVIEW\nWelcome to your bespoke Coral Island Special holiday proposal, carefully crafted for discerning families who seek the perfect balance of premium relaxation and deep ocean discoveries. Over 5 spectacular days, TRAGUIN ensures an immaculate travel experience featuring handpicked hotels, private premium transfers, and exclusive marine craft access, letting your family bypass all public transit crowds. TRAGUIN Curated Experience Note: We believe that an extraordinary vacation lies in precise personalization. From specialized family suites featuring spectacular views to private speed-craft ocean crossings and pre-arranged fine Indian dining blocks, our on-ground destination management experts secure your absolute comfort with 24/7 dedicated assistance. THE MAGIC OF OUR CORAL ISLAND SPECIAL VACATION Pattaya is highly celebrated as the coastal crown jewel of family vacation spaces, offering a beautiful mix of world-class themed water reserves, massive botanical parks, and crystal-clear offshore archipelagos. Choosing a signature TRAGUIN Pattaya Package or a specialized all-inclusive Thailand Family Tour opens up an unmatched world of elite privileges. This proposal targets top searched tourism keywords for Google ranking, ensuring the ultimate layout of Pattaya Sightseeing. Uncover iconic attractions: the gorgeous shallow sandy beaches of Coral Island, the multi-million wooden frames of the Sanctuary of Truth, and the vibrant deep marine tunnels of Underwater World. It is widely recognized as the absolute Best Time to Visit Pattaya to discover popular Instagram locations, engage in safe children-friendly marine athletics, and collect deep, immersive experiences that will be cherished for generations. TRAGUIN Coral Island Highlights: Private luxury speedboat charter to a secluded sand bay on Coral Island, premium parasailing and banana boat bundles, front-row VIP tickets to the spectacular Alcazar Show, and dedicated private luxury van transfers. THE DEFINITIVE DAY-WISE ITINERARY',
        seo_title='TH-017 | CORAL ISLAND SPECIAL Pattaya Beach | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Thailand package (TH-017 / TRG-PAT-CRL-2026): Pattaya (4 Nights with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: BANGKOK ARRIVAL & PRIVATE HIGHWAY TRANSIT TO PATTAYA', 1),
            _ih('Day 02: CORAL ISLAND PREMIUM ESCAPE & WATERSPORTS SPECIAL', 2),
            _ih('Day 03: NONG NOOCH BOTANICAL VALLEYS & UNDERWATER WORLD', 3),
            _ih('Day 04: THE SANCTUARY OF TRUTH & PATTONA RECREATION', 4),
            _ih('Day 05: PATTAYA RETREAT & BANGKOK DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private custom speedboats and marine park fast-track passes,', 6),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 7),
            _ih('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 8)
        ],
        days=[
            _day(
                1,
                'BANGKOK ARRIVAL & PRIVATE HIGHWAY TRANSIT TO PATTAYA',
                (
                    'WELCOME TO THE RECLINING KINGDOM – THE LUXURY VACATION BEGINS Your spectacular Pattaya Family Tour begins perfectly the moment your family arrives at Bangkok’s Suvarnabhumi or Don Mueang International Airport. As you emerge from the arrival gates, a warm, traditional Thai greeting awaits your party, coordinated seamlessly by your dedicated TRAGUIN tour representative. You will be escorted to your air-conditioned private luxury van, ensuring a completely relaxed, scenic cross- province highway transfer down to the beautiful resort bay of Pattaya. Arrive at your handpicked premium resort and check into your ocean-facing room, featuring special welcome amenities for the family. Spend the afternoon unwinding by the massive lagoon swimming pool or taking your first family photos overlooking the sunset. In the evening, your private van takes you to a premium Indian restaurant for a welcome buffet dinner filled with familiar comforts, ensuring a restful start for an unforgettable family vacation. Sightseeing Included: Private luxury van airport transit, scenic coastal highway drive, Pattaya Beach Road orientation. Evening Experience: Family welcome dinner at an upscale restaurant with gorgeous ocean vistas.'
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Family Resort with Ocean Front Balcony)',
                    'Meals Included: Curated Multi-Cuisine Indian Welcome Dinner',
                ],
            ),
            _day(
                2,
                'CORAL ISLAND PREMIUM ESCAPE & WATERSPORTS SPECIAL',
                (
                    'TURQUOISE LAGOONS, PRIVATE SPEEDBOAT ESCAPADE & ALCAZAR SHOW GALA Wake up to a gorgeous morning over the water and enjoy a lavish buffet breakfast. Today hosts the ultimate centerpiece of your Best Pattaya Tour Package: an exclusive island-hopping trip across the Gulf of Thailand to Koh Larn, beautifully known as Coral Island. Avoid the crowded regular public tour boats as TRAGUIN arranges a private, high-speed luxury speedboat to pick up your family directly from the resort beach front. Cruise over crystal-clear turquoise waters to arrive at a secluded stretch of soft sand, offering a premium photography point for the family. The kids can swim in the calm shallow waters while the adults take part in exciting parasailing flights or a fast banana boat ride over the waves. Savor a delicious fresh seafood or Indian lunch served right by the beach. Return to the mainland to refresh before heading to the globally acclaimed Alcazar Cabaret Show, where we have pre-booked premium VIP front-row seats for your family to enjoy world-class theatrical dance sequences. Sightseeing Included: Private Speedboat to Coral Island, beach active access, VIP entry to Alcazar Show. Optional Activities: Undersea Sea-Walking or Glass-Bottom Boat coral reef viewing for children and seniors.'
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Family Resort with Ocean Front Balcony)',
                    'Meals Included: International Buffet Breakfast & Beachside Family Lunch Layout',
                ],
            ),
            _day(
                3,
                'NONG NOOCH BOTANICAL VALLEYS & UNDERWATER WORLD',
                (
                    'EXOTIC ORCHID PATHWAYS, CULTURAL THEATER & DEEP MARINE TUNNELS Enjoy a beautiful morning breakfast before starting a comprehensive Pattaya Sightseeing cultural and wildlife day. Your private chauffeur navigates your family to the world-famous Nong Nooch Botanical Gardens. Spanning over 500 acres of meticulously designed themed valleys, it features breathtaking landscapes. TRAGUIN provides private open-air electric carts to guide your family through the orchid paths and dinosaur valleys without any physical fatigue. Enjoy a spectacular Thai Cultural and Elephant show inside the air- conditioned theater complex. Following a beautiful buffet lunch inside the gardens, your private luxury van transfers you to Underwater World Pattaya. Walk through the monumental 100-meter-long acrylic underwater tunnels to view giant manta rays, sharks, and multi-colored schools of tropical fish swimming completely around you—consistently named a top popular Instagram location for families. Return to your resort for an evening of relaxation or explore the local night bazaars. Sightseeing Included: Nong Nooch Gardens entry, electric cart tour, Cultural Show, Underwater World tunnels. Evening Experience: Boutique shopping and local street food discovery at the lively Jomtien Night Market.'
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Family Resort with Ocean Front Balcony)',
                    'Meals Included: International Buffet Breakfast & Nong Nooch Garden Buffet Lunch',
                ],
            ),
            _day(
                4,
                'THE SANCTUARY OF TRUTH & PATTONA RECREATION',
                (
                    "MYSTICAL SEAWOOD CARVINGS, ELEPHANT SANCTUARIES & FAREWELL GALA Dedicate today to deep cultural exploration and world-class architectural marvels. Following breakfast, travel to the majestic Sanctuary of Truth. This monumental 100-meter-tall seaside structure is constructed entirely of hand-carved wood without a single metal nail, representing ancient philosophies. It stands as an incredible popular Instagram location, perfect for iconic family portraits. In the afternoon, enjoy a mild visit to a local elephant sanctuary, feeding and interacting with rescued giants in an ethical environment, an absolute favorite for children. For your final evening, TRAGUIN has arranged a special grand finale dinner party at an elegant oceanfront rooftop restaurant, allowing you to toast to an extraordinary family holiday under a starlit sky. Sightseeing Included: Sanctuary of Truth guided tour, ethical elephant feeding experience, viewpoint photo stops. Optional Activities: Go-Kart racing at EasyKart Pattaya or high-speed ziplining over Pattaya's jungle park. Evening Experience: Signature TRAGUIN Grand Finale Oceanfront Family Dinner Party with live music."
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Family Resort with Ocean Front Balcony)',
                    'Meals Included: International Buffet Breakfast & 4-Course Oceanfront Farewell Dinner',
                ],
            ),
            _day(
                5,
                'PATTAYA RETREAT & BANGKOK DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER UNITED Savor your final morning breakfast at your premium resort, capturing a final round of group family photos across the tropical landscaped gardens. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless checkout. Depending on your flight departure schedule from Bangkok, your private van remains available for last-minute souvenir shopping or a brief stop at a seaside cafe to grab an authentic Thai iced tea. Your private vehicle delivers you safely to Suvarnabhumi or Don Mueang International Airport for your return flight home. Your premium Coral Island Special tour concludes beautifully, leaving your loved ones with unforgettable memories crafted to perfection by TRAGUIN. Sightseeing Included: Private luxury airport departure transfer, souvenir shopping stop.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Pattaya Modus Beachfront Resort Deluxe Family Ocean Room Complimentary Welcome Drinks & Access to Kids Club Play Zone',
                'Multi-city Thailand',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Novotel Pattaya Modus Beachfront Resort Deluxe Family Ocean Room Complimentary Welcome Drinks & Access to Kids Club Play',
            ),
            _hotel(
                'Amari Pattaya Resort Deluxe Family Horizon Suite Welcome Fruit Platters, Free Ice Cream for Kids & Large Water Pool Access',
                'Multi-city Thailand',
                '4N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Amari Pattaya Resort Deluxe Family Horizon Suite Welcome Fruit Platters, Free Ice Cream for Kids & Large Water Pool Acce',
            ),
            _hotel(
                'Centara Grand Mirage Beach Resort Pattaya Premium Deluxe Ocean View Family Suite Full Lost-World Waterpark Access & Pre-booked Kids Entertainment Vouchers',
                'Multi-city Thailand',
                '4N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Centara Grand Mirage Beach Resort Pattaya Premium Deluxe Ocean View Family Suite Full Lost-World Waterpark Access & Pre-',
            ),
            _hotel(
                'Grande Centre Point Space Pattaya Space Premium Interconnected Family Suite Bespoke Space-Themed Waterpark Passes, Private Token Vouchers & 24/7 Butler Care',
                'Multi-city Thailand',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Grande Centre Point Space Pattaya Space Premium Interconnected Family Suite Bespoke Space-Themed Waterpark Passes, Priva',
            )
        ],
        inclusions=[
            _inc_included('Daily Meals: 4 International Buffet Breakfast layouts with children-friendly sections.', 1),
            _inc_included('Private Vehicles: Private air-conditioned luxury van with an experienced driver for all transfers.', 2),
            _inc_included('Pattaya Cruise: Private Speedboat to Coral Island with parasailing and banana boat rides.', 3),
            _inc_included('VIP Sightseeing: Premium front-row seats at the Alcazar Cabaret Show with private transfers.', 4),
            _inc_included('Airfare: International flight tickets from your home country to Bangkok.', 5),
            _inc_excluded('Accommodation: 04 Nights stay in handpicked premium family resorts.', 6),
            _inc_excluded('Visa Fees: Thailand Visa-on-Arrival or fast-track electronic visa processing fees.', 7),
            _inc_excluded('National Park Entry: Island marine conservation park entry fees (payable directly on site).', 8),
        ],
    )
    return package, itinerary

def build_th_018(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-018'
    tour_code = 'TRG-PAT-FAM-2026'
    title = 'Pattaya Beach • Coral Island • Nong Nooch • Columbia Pictures Aquaverse'
    duration = '04 Nights / 05 Days'
    slug = 'th-018-pattaya-beach-coral-island-nong-nooch-columbia-pictures-aquaverse'
    itin_slug = 'th-018-pattaya-beach-coral-island-nong-nooch-columbia-pictures-aquaverse-itinerary'
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
            _ph('Serial code TH-018 | TRAGUIN tour code TRG-PAT-FAM-2026', 1),
            _ph('State / Country: Thailand | Category: Premium Family Tour', 2),
            _ph('Destinations: Pattaya (4 Nights Luxury', 3),
            _ph('Ideal for: Families, Multi- generational Groups, Kids Special', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Safe Luxury Van (Toyota Commuter / Majestic) / Buffet Breakfast (CP) & Specialized Indian/Thai Family Dinners Treat your loved ones to a magical tropical vacation with the Best Pattaya Tour Pa', 7),
            _ph('TRAGUIN Signature Experience: Private custom speedboats and theme park fast-track passes,', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 9),
            _ph('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 10),
            _ph('Luxury Transportation: Executive modern vehicles equipped with cooling, on-board entertainment', 11)
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
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Pattaya Beach',
        overview='TOUR OVERVIEW\nWelcome to your meticulously designed Pattaya Family Fun escape, precisely structured for modern families who expect seamless coordination, children-friendly paces, and elite hospitality. Across 5 incredible days, TRAGUIN ensures a flawless holiday format filled with curated experiences. Travel in completely safe, private, air-conditioned luxury vans with dedicated chauffeurs, completely bypassing the exhaustion of public coach queues. TRAGUIN Curated Experience Note: From spacious interconnected family suites to kid-special attraction access and pre-arranged authentic Indian dining choices, your holiday is managed by our dedicated destination team. Our 24/7 on-ground assistance guarantees peace of mind at every step. THE MAGIC OF A LUXURY PATTAYA HOLIDAY Pattaya has evolved into the ultimate family entertainment capital of Southeast Asia, offering an unmatched variety of interactive wildlife reserves, massive water parks, and beautiful coastal islands. Choosing one of our high-end TRAGUIN Pattaya Packages or an exceptional Thailand Family Tour means stepping past generic travel routes into a world of exclusive benefits. This proposal targets top searched tourism keywords for Google ranking, ensuring the ultimate showcase of Pattaya Sightseeing. Discover Top Tourist Places in Pattaya: the crystal lagoons of Coral Island, the world’s first Columbia Pictures movie theme park, and the breathtaking botanical valley of Nong Nooch. It is universally recognized as the Best Time to Visit Pattaya to explore popular Instagram locations, engage in exciting marine sports, and collect immersive experiences that your children will cherish for a lifetime. TRAGUIN Family Signatures: Private speedboat charter to Coral Island with safe kid-friendly water sports, premium VIP front-row seating at the Alcazar Show, full-day access to Columbia Pictures Aquaverse, and dedicated family transportation. THE DEFINITIVE DAY-WISE ITINERARY',
        seo_title='TH-018 | Pattaya Beach | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Thailand package (TH-018 / TRG-PAT-FAM-2026): Pattaya (4 Nights Luxury with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: BANGKOK ARRIVAL & PRIVATE TRANSIT TO PATTAYA', 1),
            _ih('Day 02: PRIVATE SPEEDBOAT TO CORAL ISLAND', 2),
            _ih('Day 03: NONG NOOCH GARDENS TOUR & SANCTUARY OF TRUTH', 3),
            _ih('Day 04: COLUMBIA PICTURES AQUAVERSE FULL-DAY ADVENTURE', 4),
            _ih('Day 05: PATTAYA RETREAT & BANGKOK DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private custom speedboats and theme park fast-track passes,', 6),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 7),
            _ih('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 8)
        ],
        days=[
            _day(
                1,
                'BANGKOK ARRIVAL & PRIVATE TRANSIT TO PATTAYA',
                (
                    'WELCOME TO THAILAND – THE FAMILY CELEBRATION COMMENCES Your spectacular Pattaya Family Tour begins perfectly the moment your family arrives at Bangkok’s Suvarnabhumi or Don Mueang International Airport. As you emerge from the arrival gates, a warm, traditional Thai greeting awaits your party, coordinated seamlessly by your dedicated TRAGUIN tour representative. You will be escorted to your air-conditioned private luxury van, ensuring a completely relaxed, scenic cross- province highway transfer down to the beautiful resort bay of Pattaya. Arrive at your handpicked premium resort and check into your ocean-facing room, featuring special welcome amenities for the children. Spend the afternoon unwinding by the massive lagoon swimming pool or taking your first family photos overlooking the sunset. In the evening, your private van takes you to a premium Indian restaurant for a welcome buffet dinner filled with familiar comforts, ensuring a restful start for an unforgettable family vacation. Sightseeing Included: Private luxury van airport transit, scenic coastal highway drive, Pattaya Beach Road orientation. Evening Experience: Family welcome dinner at an upscale restaurant with gorgeous ocean vistas.'
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Family Resort with Water Slides)',
                    'Meals Included: Curated Multi-Cuisine Indian Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PRIVATE SPEEDBOAT TO CORAL ISLAND',
                (
                    'SUN-KISSED SANDS, AQUATIC SPORTS & ALCAZAR THEATER GALA Wake up to a gorgeous morning over the water and enjoy a lavish buffet breakfast. Today hosts one of the most searched experiences in the region: an island-hopping trip across the Gulf of Thailand to Koh Larn, affectionately known as Coral Island. Avoid the crowded regular public tour boats as TRAGUIN arranges a private, high-speed luxury speedboat to pick up your family directly from the resort beach front. Cruise over crystal-clear turquoise waters to arrive at a secluded stretch of soft sand, offering a premium photography point for the family. The kids can swim in the calm shallow waters while the adults take part in exciting parasailing flights or a fast banana boat ride over the waves. Savor a delicious fresh seafood or Indian lunch served right by the beach. Return to the mainland to refresh before heading to the globally acclaimed Alcazar Cabaret Show, where we have pre-booked premium VIP front-row seats for your family to enjoy world-class theatrical dance sequences. Sightseeing Included: Private Speedboat to Coral Island, beach active access, VIP entry to Alcazar Show. Optional Activities: Undersea Sea-Walking or Glass-Bottom Boat coral reef viewing for children and seniors.'
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Family Resort with Water Slides)',
                    'Meals Included: International Buffet Breakfast & Beachside Family Lunch',
                ],
            ),
            _day(
                3,
                'NONG NOOCH GARDENS TOUR & SANCTUARY OF TRUTH',
                (
                    'BOTANICAL MARVELS, CULTURAL DRAMA & SIAMESE ARCHITECTURE Enjoy a beautiful morning breakfast before starting a comprehensive Pattaya Sightseeing cultural tour. Your private chauffeur navigates your family to the world-famous Nong Nooch Botanical Gardens. Spanning over 500 acres of meticulously designed themed valleys, it features breathtaking landscapes. TRAGUIN provides private open-air electric carts to guide your family through the orchid paths and dinosaur valleys without any physical fatigue. Enjoy a spectacular Thai Cultural and Elephant show inside the air-conditioned theater complex. Following a beautiful buffet lunch inside the gardens, continue to the awe-inspiring Sanctuary of Truth. This monumental 100-meter-tall seaside structure is constructed entirely of hand-carved wood without a single metal nail, representing ancient philosophies. It stands as an incredible popular Instagram location, perfect for iconic family portraits. Return to your resort for an evening of leisure or explore the local night bazaars. Sightseeing Included: Nong Nooch Gardens entry, electric cart tour, Cultural Show, Sanctuary of Truth tour. Evening Experience: Boutique shopping and street food snacks exploration at the Pattaya Floating Market.'
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Family Resort with Water Slides)',
                    'Meals Included: International Buffet Breakfast & Nong Nooch Garden Buffet Lunch',
                ],
            ),
            _day(
                4,
                'COLUMBIA PICTURES AQUAVERSE FULL-DAY ADVENTURE',
                (
                    "CINEMATIC WATER SLIDES, THRILLING SURF ZONES & GOURMET FINALE Dedicate today to pure, high-octane family joy at Columbia Pictures Aquaverse—the world's very first fully branded movie theme water park. Following a hearty breakfast, your private luxury van drops your group at the entrance gates with pre-arranged fast-track tickets. Step into highly immersive zones themed around blockbuster movies like *Ghostbusters*, *Jumanji*, *Hotel Transylvania*, and *Bad Boys*. The children will be fully entertained exploring massive water play structures, riding thrilling water coasters, and swimming in the giant wave pool featuring live music entertainment. Adults can test their balance at the Surf's Up flow-rider machine or relax along the scenic lazy river channels. For your final evening, TRAGUIN has arranged a special grand finale dinner party at an elegant oceanfront rooftop restaurant, allowing you to toast to an extraordinary family holiday under a starlit sky. Sightseeing Included: Full-day admission pass to Columbia Pictures Aquaverse, private theme park transits. Optional Activities: Go-Kart racing at EasyKart Pattaya or a visit to Underwater World Pattaya marine tunnels. Evening Experience: Signature TRAGUIN Grand Finale Oceanfront Family Dinner Party with live music."
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Family Resort with Water Slides)',
                    'Meals Included: International Buffet Breakfast & 4-Course Oceanfront Farewell Dinner',
                ],
            ),
            _day(
                5,
                'PATTAYA RETREAT & BANGKOK DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER UNITED Savor your final morning breakfast at your premium resort, capturing a final round of group family photos across the tropical landscaped gardens. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless checkout. Depending on your flight departure schedule from Bangkok, your private van remains available for last-minute souvenir shopping or a brief stop at a seaside cafe to grab an authentic Thai iced tea. Your private vehicle delivers you safely to Suvarnabhumi or Don Mueang International Airport for your return flight home. Your premium Pattaya Family Fun tour concludes beautifully, leaving your loved ones with unforgettable memories crafted to perfection by TRAGUIN. Sightseeing Included: Private luxury airport departure transfer, souvenir shopping stop.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Pattaya Modus Beachfront Resort Deluxe Family Ocean Room Complimentary Welcome Drinks & Access to Kids Club Play Zone',
                'Multi-city Thailand',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Novotel Pattaya Modus Beachfront Resort Deluxe Family Ocean Room Complimentary Welcome Drinks & Access to Kids Club Play',
            ),
            _hotel(
                'Amari Pattaya Resort Deluxe Family Horizon Suite Welcome Fruit Platters, Free Ice Cream for Kids & Large Water Pool Access',
                'Multi-city Thailand',
                '4N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Amari Pattaya Resort Deluxe Family Horizon Suite Welcome Fruit Platters, Free Ice Cream for Kids & Large Water Pool Acce',
            ),
            _hotel(
                'Centara Grand Mirage Beach Resort Pattaya Premium Deluxe Ocean View Family Suite Full Lost-World Waterpark Access & Pre-booked Kids Entertainment Vouchers',
                'Multi-city Thailand',
                '4N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Centara Grand Mirage Beach Resort Pattaya Premium Deluxe Ocean View Family Suite Full Lost-World Waterpark Access & Pre-',
            ),
            _hotel(
                'Grande Centre Point Space Pattaya Space Premium Interconnected Family Suite Bespoke Space-Themed Waterpark Passes, Private Token Vouchers & 24/7 Butler Care',
                'Multi-city Thailand',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Grande Centre Point Space Pattaya Space Premium Interconnected Family Suite Bespoke Space-Themed Waterpark Passes, Priva',
            )
        ],
        inclusions=[
            _inc_included('Daily Meals: 4 International Buffet Breakfast layouts with children-friendly sections.', 1),
            _inc_included('Private Vehicles: Private air-conditioned luxury van with an experienced driver for all transfers.', 2),
            _inc_included('Pattaya Cruise: Private Speedboat to Coral Island with parasailing and banana boat rides.', 3),
            _inc_included('VIP Sightseeing: Premium front-row seats at the Alcazar Cabaret Show with private transfers.', 4),
            _inc_included('Airfare: International flight tickets from your home country to Bangkok.', 5),
            _inc_excluded('Accommodation: 04 Nights stay in handpicked premium family resorts.', 6),
            _inc_excluded('Visa Fees: Thailand Visa-on-Arrival or fast-track electronic visa processing fees.', 7),
        ],
    )
    return package, itinerary

def build_th_019(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-019'
    tour_code = 'TRG-THA-MICE-2026'
    title = 'THAILAND INCENTIVE TOUR Bangkok • Chao Phraya River • Pattaya • Coral Island Private Retreat'
    duration = '04 Nights / 05 Days'
    slug = 'th-019-thailand-incentive-tour-bangkok-chao-phraya-river-pattaya-coral-island-private-retreat'
    itin_slug = 'th-019-thailand-incentive-tour-bangkok-chao-phraya-river-pattaya-coral-island-private-retreat-itinerary'
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
            _ph('Serial code TH-019 | TRAGUIN tour code TRG-THA-MICE-2026', 1),
            _ph('State / Country: Thailand | Category: Corporate MICE & Corporate Presentation', 2),
            _ph('Destinations: Pattaya (2N) + Bangkok (2N)', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Buffet Breakfast (CP) & Corporate Themed Gala Dinners Inspire elite performance and foster executive unity with the ultimate Best Thailand Tour Package, curated specifically by', 7)
        ],
        moods=['Luxury', 'Beach', 'Corporate'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='THAILAND INCENTIVE TOUR Bangkok',
        overview="04 Nights / 05 Days High-Impact Corporate MICE Proposal SERIAL CODE: TH-019 TRAGUIN TOUR CODE: TRG-THA-MICE-2026 STATE / COUNTRY:Thailand CATEGORY: Corporate MICE & Corporate Presentation DURATION: 04 Nights / 05 Days DESTINATIONS COVERED: Pattaya (2N) + Bangkok (2N) IDEAL FOR: Corporate Executives, Dealers, Reward Groups BEST SEASON: November to June (Perfect for Corporate Galas) VEHICLE LOGISTICS:Private Luxury Coaches & Airport Fast-Track Vans MEAL PLAN: Buffet Breakfast (CP) & Corporate Themed Gala Dinners Inspire elite performance and foster executive unity with the ultimate Best Thailand Tour Package, curated specifically by TRAGUIN to combine luxury lifestyle elements, immersive team-building, and high-impact corporate gala setups. Across spectacular architectural spaces and breathtaking landscapes, this premium Thailand Incentive Tour rewards your top players with an unforgettable corporate presentation getaway.\n\nTOUR OVERVIEW\nWelcome to your bespoke Thailand Incentive Tour, a high-end corporate presentation framework engineered explicitly for modern organizations demanding operational perfection, upscale stays, and highly motivating group interactions. Over 5 meticulously planned days, your delegates will transition between team- building sports along the Pattaya coastline and majestic network galas across the skyline of Bangkok. TRAGUIN Curated Experience Note: Every element of this corporate quotation has been optimized by our specialized corporate MICE desks. We guarantee dedicated airport fast-track immigration protocols, private luxury logistics coaches equipped with branding potential, priority VIP entry setups at major attractions, and on-ground management staff delivering round-the-clock professional assistance. TRAGUIN Corporate MICE Services • Confidential Proposal WHY CHOOSE THAILAND FOR YOUR NEXT CORPORATE INCENTIVE TOUR? Thailand remains the world's premier destination for high-end corporate incentive groups, interweaving advanced business infrastructures with breathtaking landscapes and unforgettable memories. Planning your next group movement through a specialized TRAGUIN Destination Package guarantees a beautifully run operation. This itinerary integrates key targeted industry search keywords to deliver an unmatched layout of top-tier Thailand Sightseeing wonders. Expose your executive network to the Top Tourist Places in Thailand: the crystal water coves of Coral Island, the massive tropical valleys of Nong Nooch, and the iconic architectural heritage temples of Bangkok. It is universally acknowledged as the absolute Best Time to Visit Thailand to establish impactful executive alignment, experience popular Instagram locations for team photography, source delicate artisan souvenirs, and experience a genuinely rewarding Premium Thailand Experience. TRAGUIN Corporate Presentation Privileges: Private luxury speed-craft charters for sea activities, premium front- row reserved spaces at international theater events, VIP fast-track airport customs immigration clear paths, and high-tech hotel ballroom venues. THE CORPORATE DAY-WISE ITINERARY\n\nWHY CHOOSE THAILAND FOR YOUR NEXT CORPORATE INCENTIVE\nTOUR? Thailand remains the world's premier destination for high-end corporate incentive groups, interweaving advanced business infrastructures with breathtaking landscapes and unforgettable memories. Planning your next group movement through a specialized TRAGUIN Destination Package guarantees a beautifully run operation. This itinerary integrates key targeted industry search keywords to deliver an unmatched layout of top-tier Thailand Sightseeing wonders. Expose your executive network to the Top Tourist Places in Thailand: the crystal water coves of Coral Island, the massive tropical valleys of Nong Nooch, and the iconic architectural heritage temples of Bangkok. It is universally acknowledged as the absolute Best Time to Visit Thailand to establish impactful executive alignment, experience popular Instagram locations for team photography, source delicate artisan souvenirs, and experience a genuinely rewarding Premium Thailand Experience. TRAGUIN Corporate Presentation Privileges: Private luxury speed-craft charters for sea activities, premium front- row reserved spaces at international theater events, VIP fast-track airport customs immigration clear paths, and high-tech hotel ballroom venues. THE CORPORATE DAY-WISE ITINERARY",
        seo_title='TH-019 | THAILAND INCENTIVE TOUR Bangkok | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Thailand package (TH-019 / TRG-THA-MICE-2026): Pattaya (2N) + Bangkok (2N) with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: BANGKOK ARRIVAL & SCENIC ROAD TRANSIT TO PATTAYA', 1),
            _ih('Day 02: PRIVATE SPEEDBOAT TO CORAL ISLAND & CABARET GALA', 2),
            _ih('Day 03: PATTAYA TO BANGKOK CULTURAL NAVIGATION', 3),
            _ih('Day 04: THE CORPORATE GALA PRESENTATION & ICONSIAM SHOPPING', 4),
            _ih('Day 05: BANGKOK DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'BANGKOK ARRIVAL & SCENIC ROAD TRANSIT TO PATTAYA',
                (
                    'EXECUTIVE WELCOME – SMOOTH PRIVATE VEHICLE HIGHWAY NAVIGATION Your spectacular Thailand Incentive Tour initiates flawlessly the moment your corporate delegation arrives at Bangkok’s Suvarnabhumi International Airport. Step through the gate to receive our VIP Airport Fast-Track Immigration service, where dedicated airport staff clear passport control queues within minutes. Your group is then greeted by a dedicated TRAGUIN logistics manager and escorted directly to premium, branded private luxury coaches for a comfortable cross-province drive down to Pattaya. Arrive at your handpicked premium resort in Pattaya, where our on-ground team coordinates quick check-in frameworks and handles all luggage delivery on your behalf. Spend your afternoon resting or engaging in initial team photography around the resort pool terraces. In the evening, gather your executives for an upscale multi-cuisine welcome dinner party at a seaside lounge, establishing an inspiring initial networking forum for an unforgettable Luxury Thailand Holiday. Sightseeing Included: VIP airport fast-track reception & clearance, private luxury coach transit to Pattaya coast. Evening Experience: Corporate welcome cocktail mixer and ice-breaking forum at an oceanfront lounge space. TRAGUIN Corporate MICE Services • Confidential Proposal'
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Accessible Beachfront Corporate Hotel)',
                    'Meals Included: Curated Multi-Cuisine Executive Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PRIVATE SPEEDBOAT TO CORAL ISLAND & CABARET GALA',
                (
                    'TEAM BUILDING ADVENTURES – TURQUOISE WATER ATHLETICS & ALCAZAR VIP Wake up to a beautiful morning over the water and enjoy a lavish buffet breakfast layout. Today hosts a flagship element of your corporate presentation getaway: an exclusive team-building marine trip across the Gulf of Thailand to Koh Larn, beautifully known as Coral Island. Avoid all crowded commercial passenger tour boats as TRAGUIN provides high-speed private speedboat charters to land your delegates directly on a secluded stretch of soft sand. Engage in high-impact team challenges or enjoy premium aquatic sports, including exciting parasailing flights and fast banana boat rides over the waves. Savor a premium fresh seafood or Indian beach barbecue lunch specially arranged under a private canopy. Return to the mainland to refresh before heading to the globally acclaimed Alcazar Cabaret Show, where we have pre-booked premium VIP front-row seats for your family of executives to enjoy world-class theatrical sequences. Sightseeing Included: Private Speedboat to Coral Island, beach active access, VIP entry to Alcazar Show. Optional Activities: Undersea walking or glass-bottom boat coral reef viewing for executive teams. TRAGUIN Corporate MICE Services • Confidential Proposal'
                ),
                [
                    'Overnight Stay: Pattaya (Premium High-Rise Accessible Beachfront Corporate Hotel)',
                    'Meals Included: International Buffet Breakfast & Beachfront Gourmet Barbecue Lunch',
                ],
            ),
            _day(
                3,
                'PATTAYA TO BANGKOK CULTURAL NAVIGATION',
                (
                    'SACRED TEMPLES & THE GLAMOROUS GRAND CHAO PHRAYA RIVER DINNER CRUISE Check out comfortably after breakfast as your private luxury coaches drive you back to the historical heart of the kingdom: Bangkok. Today features deep cultural discovery and authentic Bangkok Sightseeing. Stop at Wat Traimit to view the astounding Golden Buddha—a 5.5-ton solid gold statue dating back to the historic Sukhothai period. Next, visit Wat Pho to stand before the monumental 46-meter Reclining Buddha covered in exquisite gold leaf, perfect for corporate team pictures. Check into your ultra-luxury hotel overlooking the River of Kings. In the evening, dress in elegant attire for an incredible hallmark Premium Thailand Experience: a 5-star luxury dinner cruise aboard the Grand Pearl Cruise liner on the Chao Phraya River. Glide past the brilliantly lit Grand Palace and the luminous spires of Wat Arun (The Temple of Dawn) while enjoying a sumptuous international and Indian buffet dinner with soft live jazz background music. Sightseeing Included: Wat Traimit (Golden Buddha), Wat Pho (Reclining Buddha), City Driving Tour. Evening Experience: 5-Star Luxury Chao Phraya River Dinner Cruise with live classical music and light traditional dances. TRAGUIN Corporate MICE Services • Confidential Proposal'
                ),
                [
                    'Overnight Stay: Bangkok (Ultra-Luxury Riverside Corporate Hotel)',
                    'Meals Included: International Buffet Breakfast & Premium Cruise Dinner Buffet',
                ],
            ),
            _day(
                4,
                'THE CORPORATE GALA PRESENTATION & ICONSIAM SHOPPING',
                (
                    "EXECUTIVE ALIGNMENT CONFERENCE & WATERFRONT HIGH-FASHION GALA Dedicate your morning to your high-tech executive presentation or dealer award summit. Following breakfast, gather your delegates inside the hotel’s state-of-the-art tech ballroom. TRAGUIN has pre-arranged complete audio-visual systems, custom corporate stage structures, and dedicated business catering options to ensure a flawless presentation and memorable reward event. In the afternoon, your private coaches transfer the delegation to ICONSIAM, the crown jewel of Bangkok's includes an indoor floating market on the ground level, making it a perfect spot for corporate group shopping for premium local souvenirs, silks, and international luxury apparel brands. End your final evening celebrating at an elite rooftop sky lounge overlooking the illuminated metropolis skyline. Sightseeing Included: Corporate Ballroom Event Support, ICONSIAM Luxury Mall, Siam Paragon District. Evening Experience: Grand finale corporate celebration party at an upscale rooftop sky lounge."
                ),
                [
                    'shopping: plazas. The mall is fully air-conditioned, feature-packed with wide flat walkways and elevators, and',
                    'Overnight Stay: Bangkok (Ultra-Luxury Riverside Corporate Hotel)',
                    'Meals Included: International Buffet Breakfast & 4-Course Corporate Gala Dinner',
                ],
            ),
            _day(
                5,
                'BANGKOK DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER ALIGNED Enjoy your final decadent buffet breakfast at your luxury hotel, capturing a final round of panoramic team photos overlooking the bustling Chao Phraya River. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless group checkout. At the designated hour, your comfortable private coaches arrive to provide a smooth transfer to Suvarnabhumi International Airport for your return flight home. As you board your aircraft, look back on an exceptional collection of curated experiences, breathtaking landscapes, and unforgettable corporate alignment memories crafted beautifully by TRAGUIN. Your premium Thailand Incentive Tour concludes, leaving your team inspired and forever aligned. Sightseeing Included: Private luxury coach airport transfer, check-in logistics support. TRAGUIN Corporate MICE Services • Confidential Proposal'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Pattaya Modus Beachfront Resort Deluxe Group Room The Sukosol Bangkok Premier Corner Room',
                'Multi-city Thailand',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Novotel Pattaya Modus Beachfront Resort Deluxe Group Room The Sukosol Bangkok Premier Corner Room',
            ),
            _hotel(
                'Amari Pattaya Resort Deluxe Ocean Horizon Room Grande Centre Point Terminal 21 Premium Deluxe Room',
                'Multi-city Thailand',
                '4N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Amari Pattaya Resort Deluxe Ocean Horizon Room Grande Centre Point Terminal 21 Premium Deluxe Room',
            ),
            _hotel(
                'Hilton Pattaya Hotel Executive Ocean Front Room Avani+ Riverside Bangkok Hotel Avani River View Room',
                'Multi-city Thailand',
                '4N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Hilton Pattaya Hotel Executive Ocean Front Room Avani+ Riverside Bangkok Hotel Avani River View Room',
            ),
            _hotel(
                'Grande Centre Point Space Pattaya Space Premium Balcony Suite Shangri-La Bangkok / Mandarin Oriental Deluxe Horizon River Room',
                'Multi-city Thailand',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Grande Centre Point Space Pattaya Space Premium Balcony Suite Shangri-La Bangkok / Mandarin Oriental Deluxe Horizon Rive',
            )
        ],
        inclusions=[
            _inc_included('Daily Breakfast: 4 International Buffet Breakfast layouts at main kitchens.', 1),
            _inc_included('MICE Venues: Half-day high-tech conference hall rentals with complete AV tech systems.', 2),
            _inc_included('Private Coaches: Private branded luxury buses with experienced drivers for all transits.', 3),
            _inc_included('Pattaya Cruise: Private Speedboat charters to Coral Island with aquatic sports.', 4),
            _inc_included('VIP Sightseeing: Priority fast-track ramp entry for Chao Phraya River Dinner Cruise.', 5),
            _inc_included('Welcome Kit: Custom corporate badges, luggage flags, cold towels, and fresh fruits.', 6),
            _inc_included('TRAGUIN Support: 24/7 dedicated on-ground personal assistant and MICE specialists.', 7),
            _inc_included('Flights: International flight tickets from your home country connecting to Bangkok.', 8),
            _inc_excluded('Accommodation: 04 Nights stay in handpicked premium corporate hotels.', 9),
            _inc_excluded('Visa Fees: Thailand Visa-on-Arrival or fast-track electronic visa processing fees.', 10),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, individual mini-bar billing, and tips.', 11),
            _inc_excluded('Extra Branding: Corporate banner printing outside pre-booked options.', 12),
            _inc_excluded('Insurance Cover: Overseas comprehensive medical insurance with group policy add-ons.', 13),
        ],
    )
    return package, itinerary

def build_th_020(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-020'
    tour_code = 'TRG-THA-EDU-2026'
    title = 'Bangkok • Science Museums • Pattaya • Coral Island Eco Exploration'
    duration = '05 Nights / 06 Days'
    slug = 'th-020-bangkok-science-museums-pattaya-coral-island-eco-exploration'
    itin_slug = 'th-020-bangkok-science-museums-pattaya-coral-island-eco-exploration-itinerary'
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
            _ph('Serial code TH-020 | TRAGUIN tour code TRG-THA-EDU-2026', 1),
            _ph('State / Country: Thailand | Category: Educational Thailand / School Group Tour', 2),
            _ph('Destinations: Bangkok (3N) + Pattaya (2N)', 3),
            _ph('Ideal for: Schools, International Institutions, Students, Educators', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Full Board (Breakfast, Lunch & Dinner tailored for students) Expand global perspective and foster academic curiosity with the ultimate Best Thailand Tour Package, meticulously engineered by', 7)
        ],
        moods=['Family', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Bangkok',
        overview='TOUR OVERVIEW\nWelcome to your custom-crafted Educational Thailand group program, an intellectual and exploratory journey specifically engineered for institutions requiring high educational standards, complete student welfare, and handpicked premium hotel spaces. Over 6 high-impact days, students will engage with marine ecosystem projects in Pattaya and explore world-class interactive science spaces and royal antiquities across Bangkok. TRAGUIN Curated Experience Note: Student group movements demand exceptional protection, strict timeline management, and high engagement. This curated itinerary is backed by emergency medical TRAGUIN Educational Travel • Student Group Proposal planning, private safe coaches, pre-vetted buffet meal logs catering to pure vegetarian and continental diets, and senior local managers providing 24/7 dedicated assistance.\n\nWHY CHOOSE THAILAND FOR A SCHOOL TRAVEL PROGRAM?\nThailand serves as an extraordinary living classroom for global history, green marine science, innovative engineering, and biodiversity conservation. Orchestrating an educational field trip through a specialized TRAGUIN Destination Package guarantees a balanced curriculum mixed with safe leisure elements. This proposal optimizes targeted travel search keywords for search ranking, presenting an impeccable layout of premier Thailand Sightseeing marvels. Expose your students to the Top Tourist Places in Thailand: the ancient golden chambers of Bangkok’s palaces, the interactive marine pathways of Underwater World, and the pristine marine ecosystems of Coral Island. It is widely recognized as the absolute Best Time to Visit Thailand to capture architectural concepts, explore popular Instagram locations for academic journals, purchase local artisan souvenirs, and experience a world-class Premium Thailand Experience. TRAGUIN Student Safety & Academic Features: Dedicated English-speaking educational docents, pre-cleared fast-track admissions at museums, private safe marine speed-crafts with safety jackets, and certified child-safe hotel accommodations. TRAGUIN Educational Travel • Student Group Proposal THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='TH-020 | Bangkok | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-020 / TRG-THA-EDU-2026): Bangkok (3N) + Pattaya (2N) with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BANGKOK & TRANSIT TO PATTAYA', 1),
            _ih('Day 02: CORAL ISLAND ECO-EXPLORATION & UNDERWATER WORLD TUNNELS', 2),
            _ih('Day 03: PATTAYA TO BANGKOK CULTURAL TRANSIT', 3),
            _ih('Day 04: THE NATIONAL SCIENCE MUSEUM & INTERACTIVE LEARNING', 4),
            _ih('Day 05: SAFARI WORLD OPEN AIR FIELD TRIP', 5),
            _ih('Day 06: BANGKOK DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BANGKOK & TRANSIT TO PATTAYA',
                (
                    'SIAMESE RECEPTION – COMFORTABLE PRIVATE DELUXE COACH TRANSIT Your spectacular Educational Thailand student program takes flight flawlessly the moment your young scholars touch down at Bangkok’s Suvarnabhumi International Airport. Clear the arrival gates to a warm, organized reception managed directly by your TRAGUIN tour directors. Students are immediately guided to our pre-vetted, air-conditioned private luxury coaches, ensuring a structured and comfortable transit down to the coastal classroom of Pattaya. Arrive at your handpicked premium resort in Pattaya, where our on-ground managers handle smooth group check-in and room assignments. After an initial safety and orientation briefing by the tour director, students can take group photos along the coastal pathways, capturing a beautiful photography point. End the day with a healthy, well-planned international dinner buffet at the hotel, allowing the group to rest for an active itinerary ahead. Sightseeing Included: Group airport logistics management, private deluxe coach highway transit to Pattaya. Evening Experience: Interactive ice-breaking and orientation session regarding Thai traditions and safety rules. TRAGUIN Educational Travel • Student Group Proposal'
                ),
                [
                    'Overnight Stay: Pattaya (Premium Student-Friendly Beachside Corporate Hotel)',
                    'Meals Included: Curated Healthy Multi-Cuisine Dinner Buffet',
                ],
            ),
            _day(
                2,
                'CORAL ISLAND ECO-EXPLORATION & UNDERWATER WORLD TUNNELS',
                (
                    'MARINE BIOLOGY IN PRACTICE – AQUATIC REEFS & BIODIVERSITY STUDY Fuel up with a hearty buffet breakfast layout. Today hosts a primary cornerstone of your experiential curriculum: an interactive marine trip across the Gulf of Thailand to Koh Larn, beautifully known as Coral Island. Avoid all commercial passenger tour boats as TRAGUIN provides private speed-craft charts to drop your group directly onto a clean beach zone under strict supervisor control. Students can study coastal geography, observe coral sand structures, and take part in safe banana boat rides or supervised swimming with mandatory life jackets. Enjoy a healthy lunch. In the afternoon, return to the mainland to explore the massive acrylic tunnels of Underwater World Pattaya. Here, students complete interactive worksheets as they walk through deep marine habitats observing large manta rays, reef sharks, and rare sea creatures, creating unforgettable memories. Sightseeing Included: Private Speedboat to Coral Island, beach observation access, entry to Underwater World tunnels. Optional Activities: A special presentation by a local marine biology expert regarding coral preservation projects.'
                ),
                [
                    'Overnight Stay: Pattaya (Premium Student-Friendly Beachside Corporate Hotel)',
                    'Meals Included: International Breakfast, Hot Island Lunch & Student Comfort Dinner',
                ],
            ),
            _day(
                3,
                'PATTAYA TO BANGKOK CULTURAL TRANSIT',
                (
                    'HISTORIC ROYAL EMBASSIES – GOLDEN SHINES & CHAO PHRAYA DINNER CRUISE Check out comfortably after breakfast as your private coaches drive back to the metropolitan heart of the kingdom: Bangkok. Today features deep cultural discovery and authentic Bangkok Sightseeing. Stop at Wat Traimit to view the astounding Golden Buddha—a 5.5-ton solid gold statue dating back to the historic Sukhothai period. Next, visit Wat Pho to view the monumental 46-meter Reclining Buddha covered in gold leaf, mapping ancient Siamese architecture. Check into your premium handpicked hotel. In the evening, dress in smart attire for a memorable hallmark Premium Thailand Experience: a 5-star luxury dinner cruise aboard the Grand Pearl Cruise liner on the Chao Phraya River. Glide safely past the illuminated Grand Palace and the luminous spires of Wat Arun (The Temple of Dawn), enjoying a massive buffet and listening to historical descriptions via on-board narrations. Sightseeing Included: Wat Traimit (Golden Buddha), Wat Pho (Reclining Buddha), City Driving Tour. Evening Experience: 5-Star Luxury Chao Phraya River Dinner Cruise with classical music and cultural storytelling. TRAGUIN Educational Travel • Student Group Proposal'
                ),
                [
                    'Overnight Stay: Bangkok (Premium Centrally Located Lifestyle Hotel)',
                    'Meals Included: International Breakfast, Indian Comfort Lunch & River Cruise Dinner Buffet',
                ],
            ),
            _day(
                4,
                'THE NATIONAL SCIENCE MUSEUM & INTERACTIVE LEARNING',
                (
                    "TECHNOLOGY, FUTURISTIC INNOVATION & MAHANAKHON SKYWALK GEOGRAPHY Dedicate your morning to science and space technology. Following breakfast, your private coaches transfer the group to the National Science Museum (NSM) in Pathum Thani. Famous for its iconic cube-shaped architecture, it features extensive halls of interactive physics, environmental science, and digital automation exhibits. Students take part in hands-on workshop experiments, learning about modern aerodynamic concepts. In the afternoon, head back to central Bangkok. At twilight, ascend to the spectacular Mahanakhon SkyWalk, standing 314 meters above the streets on a massive glass tray—consistently named a top popular Instagram location. Under educator supervision, students can study urban geography and town-planning concepts while viewing the breathtaking landscape below, taking iconic group photography. Sightseeing Included: National Science Museum full entry and workshops, Mahanakhon SkyWalk VIP entry ticket. Evening Experience: Group evaluation circle and journal mapping at the hotel's private assembly hall."
                ),
                [
                    'Overnight Stay: Bangkok (Premium Centrally Located Lifestyle Hotel)',
                    'Meals Included: International Breakfast, Box Museum Lunch & 4-Course Student Farewell Dinner',
                ],
            ),
            _day(
                5,
                'SAFARI WORLD OPEN AIR FIELD TRIP',
                (
                    'AFRICAN SAVANNA ZOOLOGY & CONSERVATION STUDIES Dedicate today to zoological study and wildlife protection. After breakfast, head to Safari World & Marine Park —Thailand’s premier open-air wildlife sanctuary. Drive through vast African-style savannas inside your secure coaches to see lions, rhinos, and giraffes roaming completely free in large natural reserves, allowing students to map animal behavior. Afterward, enter the Marine Park to observe high-production animal intelligence shows, including the famous Dolphin Show and sea lion educational briefings. In the late afternoon, your coaches stop at a modern retail venue like ICONSIAM for light shopping. Students can pick up traditional silk items, handcrafted wooden art pieces, and delicious local food products to bring home to their parents. Sightseeing Included: Safari Park Drive, Marine Park Shows, ICONSIAM Waterfront area. Evening Experience: Relaxed student packing and casual group dinner at a local Indian restaurant. TRAGUIN Educational Travel • Student Group Proposal'
                ),
                [
                    'Overnight Stay: Bangkok (Premium Centrally Located Lifestyle Hotel)',
                    'Meals Included: International Breakfast, Safari World Buffet Lunch & Indian Buffet Dinner',
                ],
            ),
            _day(
                6,
                'BANGKOK DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – GLOBAL SHOLARS UNITED Enjoy your final decadent buffet breakfast at your hotel, taking a final round of group photos to commemorate your field trip. Our on-ground concierge team coordinates with teachers and hotel staff to manage a seamless group check-out and handle luggage logistics. At the designated hour, your comfortable private coaches deliver you safely to Suvarnabhumi International Airport for your return flight home. As you board your aircraft, look back on an exceptional collection of curated experiences, breathtaking landscapes, and unforgettable academic memories crafted beautifully by TRAGUIN. Your premium Educational Thailand tour concludes, leaving your student circle inspired, enriched, and globally aware. Sightseeing Included: Private luxury coach airport transfer, airport check-in assistance.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Pattaya Modus Beachfront Resort Deluxe Triple Sharing The Sukosol Bangkok Premier Triple Room',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Novotel Pattaya Modus Beachfront Resort Deluxe Triple Sharing The Sukosol Bangkok Premier Triple Room',
            ),
            _hotel(
                'Amari Pattaya Resort Deluxe Family Horizon Suite Grande Centre Point Terminal 21 Premium Triple Room',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Amari Pattaya Resort Deluxe Family Horizon Suite Grande Centre Point Terminal 21 Premium Triple Room',
            ),
            _hotel(
                'Hilton Pattaya Hotel Executive Family Twin Suites Avani+ Riverside Bangkok Hotel Avani Panorama Twin Room',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Hilton Pattaya Hotel Executive Family Twin Suites Avani+ Riverside Bangkok Hotel Avani Panorama Twin Room',
            ),
            _hotel(
                'Grande Centre Point Space Pattaya Space Premium Interconnected Suite Shangri-La Bangkok / Mandarin Oriental Deluxe Horizon Club Twin Room',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Grande Centre Point Space Pattaya Space Premium Interconnected Suite Shangri-La Bangkok / Mandarin Oriental Deluxe Horiz',
            )
        ],
        inclusions=[
            _inc_included('Flights: International flight tickets from your home country connecting to Bangkok.', 1),
            _inc_excluded('PACKAGE INCLUSIONS', 2),
        ],
    )
    return package, itinerary

def build_th_021(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-021'
    tour_code = 'TRG-BKK-KBV-FAM-2026'
    title = 'BANGKOK KRABI FAMILY PACKAGE Bangkok • Chao Phraya River • Krabi • Ao Nang Beach • 4 Islands'
    duration = '05 Nights / 06 Days'
    slug = 'th-021-bangkok-krabi-family-package-bangkok-chao-phraya-river-krabi-ao-nang-beach-4-islands'
    itin_slug = 'th-021-bangkok-krabi-family-package-bangkok-chao-phraya-river-krabi-ao-nang-beach-4-islands-itinerary'
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
            _ph('Serial code TH-021 | TRAGUIN tour code TRG-BKK-KBV-FAM-2026', 1),
            _ph('State / Country: Thailand | Category: Best Bangkok Krabi Tour Package', 2),
            _ph('Destinations: Bangkok (2N) + Krabi', 3),
            _ph('Ideal for: Families, Multi- generational Groups, Couples', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van (Toyota Commuter / Majestic) / Buffet Breakfast (CP) & Private Cruise Dinners Discover the perfect combination of dynamic city lights and pristine island tranquility with the Best B', 7),
            _ph('TRAGUIN Signature Experience: Private custom speedboats and luxury river cruises, completely', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium family resorts featuring private beach access', 9),
            _ph('Personalized Assistance: English-fluent dedicated local island guides to manage activity priorities,', 10),
            _ph('Luxury Transportation: Executive modern vans equipped with dual cooling, fire protection kits, and', 11)
        ],
        moods=['Family', 'Honeymoon', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='BANGKOK KRABI FAMILY PACKAGE Bangkok',
        overview='Bangkok • Chao Phraya River • Krabi • Ao Nang Beach • 4 Islands 05 Nights / 06 Days Premium Family Tour Vacation SERIAL CODE: TH-021 TRAGUIN TOUR CODE: TRG-BKK-KBV- FAM-2026 STATE / COUNTRY: Thailand CATEGORY: Best Bangkok Krabi Tour Package DURATION: 05 Nights / 06 Days DESTINATIONS: Bangkok (2N) + Krabi (3N) IDEAL FOR: Families, Multi- generational Groups, Couples BEST SEASON: November to April VEHICLE TYPE: Private Luxury Van (Toyota Commuter / Majestic) MEAL PLAN: Buffet Breakfast (CP) & Private Cruise Dinners Discover the perfect combination of dynamic city lights and pristine island tranquility with the Best Bangkok Krabi Tour Package, artfully structured by TRAGUIN. This specialized Bangkok Krabi Family Tour presents a signature Luxury Thailand Holiday, taking your loved ones through breathtaking landscapes, majestic heritage landmarks, and iconic marine reserves to create unforgettable memories.\n\nTOUR OVERVIEW\nWelcome to your meticulously designed Bangkok Krabi Family Tour vacation, curated explicitly for families who appreciate operational perfection, children-friendly exploration paces, and elite hospitality layouts. Across 6 wonderful days, your family will explore the majestic gold-plated temples and high-fashion shopping arcades of Bangkok before flying down to immerse themselves in the quiet limestone beauty and turquoise lagoons of Krabi. TRAGUIN Curated Experience Note: We ensure absolute comfort at every milestone. Traveling in private, air-conditioned luxury vans with dedicated chauffeurs allows your family to completely bypass public queues. Backed by handpicked premium stays and pre-vetted family dining paths, your group will experience a flawless trip protected by our 24/7 dedicated local concierge assistance. THE ALLURE OF OUR PREMIUM BANGKOK & KRABI VACATION Thailand’s unique geography provides an elite travel blueprint, seamlessly pairing urban royal heritage with pristine tropical island coastlines. Opting for a tailored Bangkok Krabi Family Tour or a dedicated Bangkok Krabi Honeymoon Package through TRAGUIN unlocks private access to hidden sandbars and premium dining spots. This proposal integrates top searched keywords for Google ranking, ensuring the ultimate layout of Bangkok Sightseeing and Krabi Sightseeing highlights. Uncover iconic attractions and top tourist places in Thailand: the historic golden spires of Wat Pho, the massive retail zones of ICONSIAM, the dramatic vertical limestone cliffs of Railay Beach, and the natural sandbars of Krabi’s 4 Islands. It is universally recognized as the Best Time to Visit Thailand to capture stunning family photographs at popular Instagram locations, enjoy a professional Premium Thailand Experience, and indulge in a deeply rewarding luxury holiday. TRAGUIN Family Inclusions: VIP Fast-Track airport arrival service, 5-star luxury Chao Phraya River dinner cruise, private speedboat charter across Krabi’s 4 Islands, and an intimate grand finale dinner party. THE DEFINITIVE DAY-WISE ITINERARY',
        seo_title='TH-021 | BANGKOK KRABI FAMILY PACKAGE Bangkok | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-021 / TRG-BKK-KBV-FAM-2026): Bangkok (2N) + Krabi with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BANGKOK & LUXURY RIVER DINNER CRUISE', 1),
            _ih('Day 02: BANGKOK ANCIENT TEMPLES & HIGH-FASHION ICONSIAM SHOPPING', 2),
            _ih('Day 03: BANGKOK TO KRABI FLY-IN & AO NANG SUNSET RETREAT', 3),
            _ih('Day 04: KRABI 4-ISLANDS ECO EXPEDITION BY PRIVATE SPEEDBOAT', 4),
            _ih('Day 05: KOH HONG LAGOON EXCURSION & BEACH BBQ FINALE', 5),
            _ih('Day 06: KRABI DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private custom speedboats and luxury river cruises, completely', 7),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium family resorts featuring private beach access', 8),
            _ih('Personalized Assistance: English-fluent dedicated local island guides to manage activity priorities,', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BANGKOK & LUXURY RIVER DINNER CRUISE',
                (
                    'WELCOME TO THE METROPOLIS – EMBARKING ON THE LUXURY VACATION Your spectacular Bangkok Krabi Family Tour initiates flawlessly the moment your family arrives at Bangkok’s Suvarnabhumi International Airport. Receive our VIP Fast-Track Reception, clearing all customs and immigration procedures within minutes. Your private, elegant luxury van waits to transfer you smoothly to your ultra-luxury hotel overlooking the River of Kings. Check into your handpicked premium riverfront rooms. In the evening, dress in elegant clothing for a definitive Premium Thailand Experience: a 5-star luxury dinner cruise aboard the Grand Pearl Cruise liner on the Chao Phraya River. Glide past the brilliantly lit Grand Palace and the luminous spires of Wat Arun (The Temple of Dawn) while enjoying a sumptuous international and Indian buffet, live jazz music, and classical Thai performances, capturing a beautiful opening photography point. Sightseeing Included: VIP airport fast-track reception & clearance, scenic private luxury van city transfer, Chao Phraya cruising. Evening Experience: 5-Star Luxury Chao Phraya River Dinner Cruise with live jazz background entertainment.'
                ),
                [
                    'Overnight Stay: Bangkok (Ultra-Luxury Riverside Resort)',
                    'Meals Included: Premium Cruise Gala Buffet Dinner',
                ],
            ),
            _day(
                2,
                'BANGKOK ANCIENT TEMPLES & HIGH-FASHION ICONSIAM SHOPPING',
                (
                    "GOLDEN SIAMESE HERITAGE TO WORLD-CLASS WATERFRONT LUXURY Savor a magnificent buffet breakfast before starting a descriptive Bangkok Sightseeing cultural tour. Your private chauffeur navigates your family to Wat Traimit to view the astounding Golden Buddha—a 5.5-ton solid gold statue dating back to the historic Sukhothai period. Next, visit Wat Pho to stand before the monumental 46-meter Reclining Buddha covered in gold leaf, perfect for iconic family portraits. In the afternoon, your private vehicle drops your group at ICONSIAM, the crown jewel of Bangkok's shopping plazas. Featuring an indoor floating market, incredible waterfront spaces, and massive luxury brand flagship stores, it is an unparalleled location for premium shopping. Find unique silk garments, boutique cosmetics, and local designer items. At night, ascend to the Mahanakhon SkyWalk to stand 314 meters above the streets on a massive glass tray—consistently named a top popular Instagram location. Sightseeing Included: Wat Traimit (Golden Buddha), Wat Pho (Reclining Buddha), ICONSIAM Luxury Mall, Mahanakhon SkyWalk. Optional Activities: A traditional wooden longtail boat tour through the historic Thonburi canal networks."
                ),
                [
                    'Overnight Stay: Bangkok (Ultra-Luxury Riverside Resort)',
                    'Meals Included: International Buffet Breakfast & Traditional Thai Fine Dining Lunch',
                ],
            ),
            _day(
                3,
                'BANGKOK TO KRABI FLY-IN & AO NANG SUNSET RETREAT',
                (
                    'TRANSIT TO THE RIVIERA – COASTAL ORIENTATION & CLIFFSIDE DINING Enjoy a relaxed morning breakfast looking out over the Chao Phraya River before checking out. Your private luxury van transfers your group comfortably to the airport for your domestic flight to Krabi. Upon arrival in this tropical paradise, your waiting private premium vehicle provides a smooth transfer along the beautiful shoreline to your ultra-luxury beachfront resort near Ao Nang beach. Krabi is adored globally for its staggering limestone towers rising straight from emerald waters—making it a center for any true Luxury Thailand Holiday. Check into your premium resort and take some time to rest. In the late afternoon, your driver delivers you to the vibrant Ao Nang coastline. Take a slow walk along the soft sand beach before gathering at a high-end cliffside restaurant for a sunset dinner, capturing spectacular landscapes. Sightseeing Included: Domestic flight airport transfers, scenic coastal highway drive, Ao Nang bay orientation walk. Evening Experience: Sunset family dining at an upscale restaurant overlooking the rocky Ao Nang horizon.'
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Cliffside or Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Curated Coastal Sunset Dinner',
                ],
            ),
            _day(
                4,
                'KRABI 4-ISLANDS ECO EXPEDITION BY PRIVATE SPEEDBOAT',
                (
                    'MYSTICAL SANDBAR WALKING, PHRA NANG SEA SHRINES & CANOEING Gear up for an iconic highlight of your Krabi Sightseeing itinerary. Following a delicious breakfast, an exclusive private speed-craft launches directly from the resort sands for a thrilling multi-island journey. Avoid all crowded commercial passenger tour boats as you speed towards Tup Island, where a unique natural sandbar emerges at low tide, allowing your family to walk on crystal water between islands. Continue to Phra Nang Cave Beach, renowned for its vertical rock climbers and sacred sea shrines. The children can swim safely in the shallow bays of Poda Island while the adults relax on soft sands or take part in exciting parasailing flights. Snorkel over the live barrier reefs of Chicken Island, surrounded by schools of tropical fish. Enjoy a premium lunch layout before cruising back to your resort base. Sightseeing Included: Tup Island Sandbar walk, Chicken Island reef snorkeling, Poda Island beach access, Phra Nang Cave. Optional Activities: Supervised undersea sea-walking or high-speed sea jet-skiing around the limestone towers.'
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Cliffside or Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Premium Beachside Seafood Buffet Lunch',
                ],
            ),
            _day(
                5,
                'KOH HONG LAGOON EXCURSION & BEACH BBQ FINALE',
                (
                    'EMERALD CANYONS, THE 360 PLATFORM CLIMB & CANDLELIGHT GALA Prepare for another awe-inspiring day exploring hidden geographical wonders. After breakfast, board your private speedboat charter to explore the Koh Hong Archipelago. Skip the public crowds as your captain steers your vessel through narrow rocky arches into Hong Island’s interior secret lagoon, a natural emerald basin enclosed by colossal vertical rock faces. Land at the beach to ascend the spectacular 419-step metal walkway up to the 360-degree viewpoint platform, capturing a breathtaking panorama across hundreds of tiny islands. For your final evening, TRAGUIN has arranged our ultimate signature surprise: an intimate, completely private beachfront candlelight barbecue dinner set in a secluded cove. Toast your vacation with a glass of fine wine under a starlit sky as gentle waves roll in. Sightseeing Included: Koh Hong Lagoon entry, 360 Viewpoint platform ascend, Lading Island beach access. Evening Experience: Signature TRAGUIN Grand Finale Private Beachfront Candlelight Barbecue Dinner.'
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Cliffside or Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & 5-Course Private Cove Barbecue Dinner',
                ],
            ),
            _day(
                6,
                'KRABI DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER UNITED Savor your final morning breakfast looking out over the majestic Krabi limestone cliffs. Take a final dip in your resort’s infinity edge pool or enjoy a slow walk along the soft sand of Ao Nang beach, capturing your final group pictures to commemorate an exceptional family vacation. Your private luxury van arrives to transfer your party comfortably to Krabi International Airport for your departure flight back home. As you board your aircraft, look back on an exceptional collection of curated experiences, breathtaking landscapes, and unforgettable family memories crafted beautifully by TRAGUIN. Your premium vacation concludes, leaving your family inspired, fulfilled, and forever united. Sightseeing Included: Private luxury van airport departure transfer, checkout assistance.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Sukosol Bangkok Premier Corner Room Ao Nang Cliff Beach Resort Ocean View Suite',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — The Sukosol Bangkok Premier Corner Room Ao Nang Cliff Beach Resort Ocean View Suite',
            ),
            _hotel(
                'Avani+ Riverside Bangkok Hotel Avani River View Room Centara Grand Beach Resort Krabi Deluxe Ocean Face Room',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Avani+ Riverside Bangkok Hotel Avani River View Room Centara Grand Beach Resort Krabi Deluxe Ocean Face Room',
            ),
            _hotel(
                'Shangri-La Bangkok Deluxe Horizon River Room Rayavadee Krabi Resort Deluxe Pavilion Estate',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Shangri-La Bangkok Deluxe Horizon River Room Rayavadee Krabi Resort Deluxe Pavilion Estate',
            ),
            _hotel(
                'Mandarin Oriental, Bangkok Deluxe Chao Phraya Suite Phulay Bay, a Ritz-Carlton Reserve Reserve Pavilion Pool Villa',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Mandarin Oriental, Bangkok Deluxe Chao Phraya Suite Phulay Bay, a Ritz-Carlton Reserve Reserve Pavilion Pool Villa',
            )
        ],
        inclusions=[
            _inc_included('Handpicked premium accommodation as per selected hotel tier', 1),
            _inc_included('Private luxury vehicle transfers and sightseeing as per itinerary', 2),
            _inc_included('Daily buffet breakfast and curated meals as specified', 3),
            _inc_included('VIP airport fast-track reception and dedicated TRAGUIN concierge support', 4),
            _inc_excluded('PACKAGE INCLUSIONS', 5),
        ],
    )
    return package, itinerary

def build_th_022(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-022'
    tour_code = 'TRG-HKT-FAM-2026-V22'
    title = 'PHUKET FAMILY FUN PACKAGE Phuket • Patong • Phi Phi Islands • Phang Nga Bay • Carnival Magic'
    duration = '05 Nights / 06 Days'
    slug = 'th-022-phuket-family-fun-package-phuket-patong-phi-phi-islands-phang-nga-bay-carnival-magic'
    itin_slug = 'th-022-phuket-family-fun-package-phuket-patong-phi-phi-islands-phang-nga-bay-carnival-magic-itinerary'
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
            _ph('Serial code TH-022 | TRAGUIN tour code TRG-HKT-FAM-2026-V22', 1),
            _ph('State / Country: Thailand | Category: Best Phuket Tour Package', 2),
            _ph('Destinations: Phuket Island (5 Nights', 3),
            _ph('Ideal for: Families, Multi- generational Groups, Kids Special', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Safe Luxury Van (Toyota Commuter) / Buffet Breakfast (CP), Private Island Lunch & Special Dinners Treat your loved ones to an extraordinary tropical getaway with the Best Phuket Tour Package,', 7),
            _ph('TRAGUIN Signature Experience: Private custom speedboats and theme park fast-track passes,', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 9),
            _ph('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 10),
            _ph('Luxury Transportation: Executive modern vehicles equipped with cooling, on-board entertainment', 11)
        ],
        moods=['Family', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='PHUKET FAMILY FUN PACKAGE Phuket',
        overview="Phuket • Patong • Phi Phi Islands • Phang Nga Bay • Carnival Magic 05 Nights / 06 Days Premium Family Tour Vacation SERIAL CODE: TH-022 TRAGUIN TOUR CODE: TRG-HKT-FAM-2026- V22 STATE / COUNTRY: Thailand CATEGORY: Best Phuket Tour Package DURATION: 05 Nights / 06 Days DESTINATIONS: Phuket Island (5 Nights Premium Family Stay) IDEAL FOR: Families, Multi- generational Groups, Kids Special BEST SEASON: November to May (Clear Skies & Calm Seas) VEHICLE TYPE: Private Safe Luxury Van (Toyota Commuter) MEAL PLAN: Buffet Breakfast (CP), Private Island Lunch & Special Dinners Treat your loved ones to an extraordinary tropical getaway with the Best Phuket Tour Package, masterfully designed by TRAGUIN to combine thrilling theme parks, pristine sand shores, and deep cultural marvels. This spectacular Phuket Family Tour balances world-class children's entertainment with premium stays, presenting breathtaking landscapes and creating unforgettable memories for every generation.\n\nTOUR OVERVIEW\nWelcome to your meticulously designed Phuket Family Fun escape, precisely structured for modern families who expect seamless coordination, children-friendly exploration paces, and elite hospitality layouts. Across 6 incredible days, your family will explore the finest theme parks, cultural spectacles, and crystal-clear marine reserves of Thailand's largest island. TRAGUIN Curated Experience Note: We ensure absolute comfort at every milestone. Traveling in private, air-conditioned luxury vans with dedicated chauffeurs allows your family to completely bypass public queues. Backed by handpicked premium stays and pre-vetted family dining paths, your group will experience a flawless trip protected by our 24/7 dedicated local concierge assistance. THE MAGIC OF OUR LUXURY PHUKET FAMILY TOUR Phuket has evolved into the ultimate family entertainment capital of Southeast Asia, offering an unmatched variety of interactive wildlife sanctuaries, massive water parks, and beautiful offshore archipelagos. Choosing one of our high-end TRAGUIN Phuket Packages or an exceptional Phuket Honeymoon Package means stepping past generic travel routes into a world of exclusive benefits. This proposal targets top searched tourism keywords for Google ranking, ensuring the ultimate showcase of Phuket Sightseeing wonders. Discover Top Tourist Places in Thailand: the crystal lagoons of the Phi Phi Islands, the mystical hidden sea caves of Phang Nga Bay, and the world-record-breaking dazzling lights of Carnival Magic. It is universally recognized as the Best Time to Visit Thailand to explore popular Instagram locations, engage in safe children-friendly marine athletics, and collect immersive experiences that your family will cherish for a lifetime. TRAGUIN Family Signatures: Private speedboat charter to Phi Phi Islands with safe kid-friendly water sports, VIP entry tickets to Carnival Magic and its grand regal buffet, and dedicated chauffeured luxury van transfers throughout the island. THE FUN & IMMERSIVE DAY-WISE ITINERARY",
        seo_title='TH-022 | PHUKET FAMILY FUN PACKAGE Phuket | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-022 / TRG-HKT-FAM-2026-V22): Phuket Island (5 Nights with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN PHUKET & LEISURE OCEANFRONT WELCOME', 1),
            _ih('Day 02: PRIVATE SPEEDBOAT TO PHI PHI ISLANDS', 2),
            _ih('Day 03: PHUKET LANDMARKS TOUR & CARNIVAL MAGIC EXTRAVAGANZA', 3),
            _ih('Day 04: PHANG NGA BAY SEA CAVE CANOEING & ETHICAL ELEPHANT ENCOUNTER', 4),
            _ih('Day 05: ANDAMANDA WATERPARK FULL-DAY FAMILY ATHLETICS', 5),
            _ih('Day 06: BOUTIQUE SHOPPING & PHUKET DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private custom speedboats and theme park fast-track passes,', 7),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 8),
            _ih('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN PHUKET & LEISURE OCEANFRONT WELCOME',
                (
                    'WELCOME TO PARADISE – THE FAMILY TROPICAL HOLIDAY BEGINS Your spectacular Phuket Family Tour begins perfectly the moment your family lands at Phuket International Airport. As you emerge from the arrival gates, a warm, traditional Thai greeting awaits your party, coordinated seamlessly by your dedicated TRAGUIN tour representative. You will be escorted to your air-conditioned private luxury van, ensuring a completely relaxed, scenic transfer straight to your handpicked premium resort. Arrive at your premium resort and check into your ocean-facing room, featuring special welcome amenities for the family. Spend the afternoon unwinding by the massive lagoon swimming pool or taking your first family photos overlooking the sunset. In the evening, your private van takes you to a premium restaurant for a welcome buffet dinner filled with familiar comforts, ensuring a restful start for an unforgettable family vacation. Sightseeing Included: Private luxury van airport transit, scenic coastal driving layout, Patong Beach orientation. Evening Experience: Family welcome dinner at an upscale beachfront restaurant with gorgeous ocean vistas.'
                ),
                [
                    'Overnight Stay: Phuket (Premium High-Rise Family Resort with Water Slides)',
                    'Meals Included: Curated Multi-Cuisine Family Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PRIVATE SPEEDBOAT TO PHI PHI ISLANDS',
                (
                    'CRYSTAL LAGOONS, SNORKELING ESCAPADES & MAYA BAY VIEWPOINTS Wake up to a gorgeous morning over the water and enjoy a lavish buffet breakfast. Today hosts the ultimate centerpiece of your Best Phuket Tour Package: an exclusive island-hopping trip across the Andaman Sea to the legendary Phi Phi Islands. Avoid the crowded regular public tour boats as TRAGUIN arranges a private, high-speed luxury speedboat to pick up your family directly from the resort beachfront or private pier. Cruise over crystal-clear turquoise waters to arrive at the vertical limestone walls of Maya Bay, offering a premium photography point for the family. The kids can swim in the calm shallow waters while the adults snorkel in the emerald basin of Pileh Lagoon. Savor a delicious fresh beachfront gourmet lunch served right on the soft sands of Bamboo Island. Conclude the day exploring Monkey Beach and the historic Viking Cave before cruising back to your resort base. Sightseeing Included: Private Speedboat to Phi Phi Islands, Maya Bay entry, Pileh Lagoon snorkeling, Bamboo Island sandbar. Optional Activities: Supervised Glass-Bottom Boat coral reef viewing or sea-kayaking through hidden coves for children.'
                ),
                [
                    'Overnight Stay: Phuket (Premium High-Rise Family Resort with Water Slides)',
                    'Meals Included: International Buffet Breakfast & Island Beachfront Gourmet Lunch',
                ],
            ),
            _day(
                3,
                'PHUKET LANDMARKS TOUR & CARNIVAL MAGIC EXTRAVAGANZA',
                (
                    "SACRED TEMPLES, COLONIAL HERITAGE & THE WORLD'S HIGHLIGHT ILLUMINATION SHOW Enjoy a beautiful morning breakfast before starting a comprehensive Phuket Sightseeing cultural and entertainment day. Your private chauffeur navigates your family up the Nakkerd Hills to stand at the base of the majestic 45-meter Big Buddha monument. This vantage point offers an incredible 360-degree panorama of Chalong Bay and Phuket Town—consistently ranked among the most popular Instagram locations in Southeast Asia. Continue your premium tour to Wat Chalong, Phuket’s most revered Buddhist monastery, and explore the charming Sino-Portuguese colonial mansions of Old Phuket Town. In the late afternoon, experience an absolute milestone: Carnival Magic theme park. Spanning 40 acres of dazzling neon lights, it holds multiple Guinness World Records. Enjoy a regal dinner buffet inside the giant Bird of Paradise restaurant before witnessing the magnificent River Palace Parade and illumination show, fully entertaining the children. Sightseeing Included: The Big Buddha, Wat Chalong Temple, Old Phuket Town, Carnival Magic entry ticket & Parade Show. Evening Experience: Immerse in the Kingdom of Lights walk-through, showcasing over 40 million dazzling lights."
                ),
                [
                    'Overnight Stay: Phuket (Premium High-Rise Family Resort with Water Slides)',
                    'Meals Included: International Buffet Breakfast & Royal Carnival Dinner Buffet',
                ],
            ),
            _day(
                4,
                'PHANG NGA BAY SEA CAVE CANOEING & ETHICAL ELEPHANT ENCOUNTER',
                (
                    'JAMES BOND ISLAND LIMESTONES, SEA CAVE CANOEING & ELEPHANT FEEDING Prepare for an awe-inspiring day exploring one of the most magnificent landscapes in Southeast Asia. After breakfast, transfer to the northern pier where a premium speed-craft takes your family across Phang Nga Bay. Cruise past hundreds of vertical limestone karsts rising dramatically out of the calm sea. Arrive at James Bond Island, an iconic attraction of Phuket Sightseeing, and capture fantastic family photos in front of the floating rock monolith. Next, enjoy a relaxing canoeing experience guided through the mystical sea caves and hidden mangrove lagoons of Koh Hong. Savor a fresh seafood lunch at the unique stilted floating village of Koh Panyee. In the afternoon, return to the mainland for a heartwarming visit to an ethical elephant sanctuary. The children can interact with and feed rescued gentle giants in a safe environment. Return to the resort for an evening of relaxation or explore the local night bazaars. Sightseeing Included: James Bond Island, Koh Hong sea cave canoeing, Koh Panyee village, Ethical Elephant Sanctuary. Optional Activities: A therapeutic family foot reflexology or traditional massage session at the resort day spa pavilion.'
                ),
                [
                    'Overnight Stay: Phuket (Premium High-Rise Family Resort with Water Slides)',
                    'Meals Included: International Buffet Breakfast & Koh Panyee Seafood Lunch',
                ],
            ),
            _day(
                5,
                'ANDAMANDA WATERPARK FULL-DAY FAMILY ATHLETICS',
                (
                    'THRILLING WATER COASTERS, GIANT WAVE POOLS & GRAND OCEANFRONT FINALE Dedicate today to pure, high-octane family joy at Andamanda Phuket Waterpark—the island’s largest and most spectacular water park based on authentic Thai mythology. Following a hearty breakfast, your private luxury van drops your group at the entrance gates with pre-arranged fast-track tickets. Step into five highly immersive zones packed with world-class water slides and lazy rivers. The children will be fully entertained exploring massive water play structures and riding thrilling water coasters, while adults can relax at the sand-fringed wave pool or swim up to a luxury pool bar. For your final evening, TRAGUIN has arranged our ultimate signature surprise: an intimate private family dinner party set at an elegant oceanfront rooftop restaurant, allowing you to toast to an extraordinary family holiday under a starlit sky. Sightseeing Included: Full-day admission pass to Andamanda Waterpark, private waterpark van transfers. Evening Experience: Signature TRAGUIN Grand Finale Oceanfront Family Dinner Party with live soft acoustic music.'
                ),
                [
                    'Overnight Stay: Phuket (Premium High-Rise Family Resort with Water Slides)',
                    'Meals Included: International Buffet Breakfast & 4-Course Oceanfront Farewell Dinner',
                ],
            ),
            _day(
                6,
                'BOUTIQUE SHOPPING & PHUKET DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER UNITED Savor your final morning breakfast at your premium resort, capturing a final round of group family photos across the tropical landscaped gardens. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless group checkout. Your private luxury van remains available for last-minute souvenir shopping at Central Phuket Floresta or a brief stop at a seaside cafe to grab an authentic Thai iced tea. Your private vehicle delivers your family safely to Phuket International Airport for your departure flight back home. Your premium Phuket Family Tour concludes beautifully, leaving your loved ones with unforgettable memories crafted to perfection by TRAGUIN. Sightseeing Included: Central Phuket Floresta shopping access, private luxury airport departure transfer.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Phuket Resort (Patong) Deluxe Family Ocean Room Complimentary Welcome Drinks & Access to Kids Club Play Zone',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Novotel Phuket Resort (Patong) Deluxe Family Ocean Room Complimentary Welcome Drinks & Access to Kids Club Play Zone',
            ),
            _hotel(
                'Phuket Marriott Resort, Merlin Beach Premium Family Pool View Room Welcome Fruit Platters, Free Ice Cream for Kids & Reef Educational Walk',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Phuket Marriott Resort, Merlin Beach Premium Family Pool View Room Welcome Fruit Platters, Free Ice Cream for Kids & Ree',
            ),
            _hotel(
                'The Westin Siray Bay Resort & Spa Luxury Seaview Family Suite Complimentary Floating Breakfast Setup & Kids Spa Discount Vouchers',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Westin Siray Bay Resort & Spa Luxury Seaview Family Suite Complimentary Floating Breakfast Setup & Kids Spa Discount',
            ),
            _hotel(
                'Anantara Layan Phuket / Sri Panwa Ocean View Luxury Pool Villa / Suite Premium Vintage Champagne Bottle, Private Beach Access & 24/7 Butler Care',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Anantara Layan Phuket / Sri Panwa Ocean View Luxury Pool Villa / Suite Premium Vintage Champagne Bottle, Private Beach A',
            )
        ],
        inclusions=[
            _inc_included('Daily Breakfast: 5 International Buffet Breakfast layouts with children-friendly sections.', 1),
            _inc_included('Private Vehicles: Private air-conditioned luxury van with an experienced driver for all transfers.', 2),
            _inc_included('Phuket Cruise: Private Speedboat to Phi Phi Islands with beachfront buffet lunch.', 3),
            _inc_included('Bay Excursion: Premium Speed-craft tour to James Bond Island with sea canoeing & lunch.', 4),
            _inc_included('Airfare: International flight tickets from your home country to Phuket.', 5),
            _inc_excluded('Accommodation: 05 Nights stay in handpicked premium family resorts.', 6),
            _inc_excluded('Visa Fees: Thailand Visa-on-Arrival or fast-track electronic visa processing fees.', 7),
            _inc_excluded('National Park Entry: Island marine conservation park entry fees (payable directly on site).', 8),
        ],
    )
    return package, itinerary

def build_th_023(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-023'
    tour_code = 'TRG-CNX-FAM-2026-V23'
    title = 'CHIANG MAI EXPLORER Chiang Mai • Doi Suthep • Elephant Nature Park • Chiang Rai • Golden Triangle'
    duration = '05 Nights / 06 Days'
    slug = 'th-023-chiang-mai-explorer-chiang-mai-doi-suthep-elephant-nature-park-chiang-rai-golden-triangle'
    itin_slug = 'th-023-chiang-mai-explorer-chiang-mai-doi-suthep-elephant-nature-park-chiang-rai-golden-triangle-itinerary'
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
            _ph('Serial code TH-023 | TRAGUIN tour code TRG-CNX-FAM-2026-V23', 1),
            _ph('State / Country: Thailand | Category: Best Chiang Mai Tour Package', 2),
            _ph('Destinations: Chiang Mai (5 Nights', 3),
            _ph('Ideal for: Families, Culture Seekers, Multi- generational Groups', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van (Toyota Commuter Executive) / Buffet Breakfast (CP), Traditional Khantoke Lunch & Special Dinners', 7),
            _ph('TRAGUIN Signature Experience: Private custom Mekong River longtail boats and cultural attraction', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium family resorts located in secure highland', 9),
            _ph('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 10),
            _ph('Luxury Transportation: Executive modern vans equipped with cooling, on-board entertainment', 11)
        ],
        moods=['Family', 'Culture', 'Wildlife'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='CHIANG MAI EXPLORER Chiang Mai',
        overview="05 Nights / 06 Days Premium Family Tour Vacation SERIAL CODE: TH-023 TRAGUIN TOUR CODE: TRG-CNX-FAM-2026- V23 STATE / COUNTRY: Thailand / Northern Region CATEGORY: Best Chiang Mai Tour Package DURATION: 05 Nights / 06 Days DESTINATIONS: Chiang Mai (5 Nights Premium Highland Stay) IDEAL FOR: Families, Culture Seekers, Multi- generational Groups BEST SEASON: October to March (Cool Mountain Breeze) VEHICLE TYPE: Private Luxury Van (Toyota Commuter Executive) MEAL PLAN: Buffet Breakfast (CP), Traditional Khantoke Lunch & Special Dinners Step into the majestic cultural soul of Northern Thailand with the Best Chiang Mai Tour Package, masterfully curated by TRAGUIN to offer an enchanting mix of misty mountain peaks, ancient gold-leaf temples, and ethical wildlife encounters. This spectacular Chiang Mai Family Tour balances immersive cultural treasures with premium stays, presenting breathtaking landscapes and creating unforgettable memories for your loved ones.\n\nTOUR OVERVIEW\nWelcome to your meticulously designed Chiang Mai Explorer escape, precisely structured for modern families who expect seamless coordination, children-friendly exploration paces, and elite hospitality layouts. Across 6 incredible days, your family will explore the finest historical treasures, high-mountain views, and majestic sanctuary valleys of Lanna Kingdom. TRAGUIN Curated Experience Note: We ensure absolute comfort at every milestone. Traveling in private, air-conditioned luxury vans with dedicated chauffeurs allows your family to completely bypass public transit lines. Backed by handpicked premium stays and pre-vetted family dining paths, your group will experience a flawless trip protected by our 24/7 dedicated local concierge assistance. THE MAGIC OF OUR LUXURY CHIANG MAI FAMILY TOUR Chiang Mai has evolved into the ultimate cultural and eco-tourism capital of Southeast Asia, offering an unmatched variety of ethical animal sanctuaries, misty mountain ranges, and historic royal temples. Choosing one of our high-end TRAGUIN Chiang Mai Packages or an exceptional Chiang Mai Honeymoon Package means stepping past generic travel routes into a world of exclusive benefits. This proposal targets top searched tourism keywords for Google ranking, ensuring the ultimate showcase of Chiang Mai Sightseeing wonders. Discover Top Tourist Places in Thailand: the golden mountain spires of Wat Phra That Doi Suthep, the pristine valleys of an ethical elephant sanctuary, and the surreal architectural wonder of Chiang Rai's White Temple. It is universally recognized as the Best Time to Visit Thailand to explore popular Instagram locations, engage in safe children-friendly mountain adventures, source delicate artisan silk handicrafts, and collect immersive experiences that your family will cherish for a lifetime. TRAGUIN Family Signatures: Private guided ethical elephant bathing session, VIP entry to the traditional Khantoke Royal Lanna Dinner & Dance Show, full-day luxury excursion to Chiang Rai and the Golden Triangle, and dedicated private luxury van transits. THE FUN & IMMERSIVE DAY-WISE ITINERARY",
        seo_title='TH-023 | CHIANG MAI EXPLORER Chiang Mai | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-023 / TRG-CNX-FAM-2026-V23): Chiang Mai (5 Nights with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN CHIANG MAI & HIGHLAND SUNSET WELCOME', 1),
            _ih('Day 02: GOLDEN DOI SUTHEP TEMPLE & BHUBING PALACE CRUISE', 2),
            _ih('Day 03: ETHICAL ELEPHANT NATURE SANCTUARY EXCURSION', 3),
            _ih('Day 04: FULL-DAY CHIANG RAI & GOLDEN TRIANGLE EXPEDITION', 4),
            _ih('Day 05: SAN KAMPHAENG CRAFT ARTISANS & HIGHLAND HOT SPRINGS', 5),
            _ih('Day 06: CHIANG MAI RETREAT & DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private custom Mekong River longtail boats and cultural attraction', 7),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium family resorts located in secure highland', 8),
            _ih('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN CHIANG MAI & HIGHLAND SUNSET WELCOME',
                (
                    'WELCOME TO THE LANNA CAPITAL – THE FAMILY EXPLORATION BEGINS Your spectacular Chiang Mai Family Tour begins perfectly the moment your family lands at Chiang Mai International Airport. As you emerge from the arrival gates, a warm, traditional Northern Thai greeting awaits your party, coordinated seamlessly by your dedicated TRAGUIN tour representative. You will be escorted to your air-conditioned private luxury van, ensuring a completely relaxed transfer straight to your handpicked premium resort. Arrive at your premium valley resort and check into your mountain-facing room, featuring special welcome amenities for the family. Spend the afternoon unwinding by the panoramic swimming pool or taking your first family photos overlooking the misty hills. In the evening, your private van takes you to an upscale restaurant for a welcome buffet dinner filled with familiar comforts, ensuring a restful start for an unforgettable family vacation. Sightseeing Included: Private luxury van airport transit, scenic old city driving layout, night bazaar orientation walk. Evening Experience: Family welcome dinner at an upscale mountain-view restaurant with gorgeous valley vistas.'
                ),
                [
                    'Overnight Stay: Chiang Mai (Premium Luxury Heritage Resort)',
                    'Meals Included: Curated Multi-Cuisine Family Welcome Dinner',
                ],
            ),
            _day(
                2,
                'GOLDEN DOI SUTHEP TEMPLE & BHUBING PALACE CRUISE',
                (
                    "GOLDEN MOUNTAIN SPIRES, ROYAL GARDENS & PANORAMIC CITY VIEWS Wake up to a crisp morning over the mountains and enjoy a lavish buffet breakfast. Today hosts the ultimate centerpiece of your Best Chiang Mai Tour Package: an excursion up the winding roads of Doi Suthep mountain. Avoid the public transport crowds as your private vehicle drives your family up to Wat Phra That Doi Suthep, the island's most revered mountain temple dating back to 1383. Ascend the majestic 306-step naga snake staircase or ride the premium glass cable car to stand before the monument's monumental golden chedi, offering an incredible photography point for the family. In the afternoon, explore the Bhubing Royal Palace and its spectacular rose gardens. Return to the city for a classic Chiang Mai Sightseeing highlight: the traditional Khantoke Royal Lanna Dinner, where your family enjoys Northern Thai delicacies while watching magnificent cultural dance sequences. Sightseeing Included: Doi Suthep Temple entry, Naga staircase photo stop, Bhubing Palace gardens, Khantoke Royal Show. Optional Activities: A traditional blessing session by a senior Buddhist monk inside the golden chedi pavilion."
                ),
                [
                    'Overnight Stay: Chiang Mai (Premium Luxury Heritage Resort)',
                    'Meals Included: International Buffet Breakfast & Traditional Khantoke Royal Dinner Show',
                ],
            ),
            _day(
                3,
                'ETHICAL ELEPHANT NATURE SANCTUARY EXCURSION',
                (
                    'HEARTWARMING JUNGLE ENCOUNTERS, ELEPHANT BATHING & WATERFALL POOLS Enjoy a beautiful morning breakfast before starting a highly anticipated ethical wildlife day. Your private luxury van transfers your family deep into the lush Mae Taeng valley to an award-winning ethical elephant sanctuary. Change into traditional mahout attire and follow expert conservationists to meet rescued gentle giants roaming completely free in large natural reserves, allowing your family to map animal behavior. The children will be fully entertained preparing organic dietary supplements, hand-feeding bananas, and walking alongside the elephants down to the river basin. Take part in a spectacular, safe elephant bathing and splashing session in the shallow river water—consistently named a top popular Instagram location for families. Savor a fresh jungle buffet lunch at the sanctuary before a brief stop at a natural mountain waterfall on the drive back to base. Sightseeing Included: Ethical Elephant Sanctuary full experience, river bathing access, Mae Sa Waterfall stop. Evening Experience: Boutique shopping and street food discovery at the lively Chiang Mai Sunday Walking Street.'
                ),
                [
                    'Overnight Stay: Chiang Mai (Premium Luxury Heritage Resort)',
                    'Meals Included: International Buffet Breakfast & Sanctuary Jungle Buffet Lunch',
                ],
            ),
            _day(
                4,
                'FULL-DAY CHIANG RAI & GOLDEN TRIANGLE EXPEDITION',
                (
                    'SURREAL WHITE TEMPLE, MYSTICAL BLUE TEMPLE & THREE-BORDER PANORAMA Prepare for an awe-inspiring day exploring the northernmost borders of Thailand. Following an early breakfast, your private van sets off on a scenic highway drive to Chiang Rai province. Your first stop features the world-famous Wat Rong Khun (The White Temple), a monumental masterpiece designed entirely in pure white glass filigree, creating a spectacular background for iconic family portraits. Next, visit the surreal Wat Rong Suea Ten (The Blue Temple) to admire its brilliant sapphire interiors. Following a gourmet lunch, your private vehicle drives to the historic Golden Triangle viewpoint, where the borders of Thailand, Laos, and Myanmar intersect along the Mekong River. Board a private longtail boat to cruise gently along the river channels, absorbing historical descriptions via on-board narrations before returning to your Chiang Mai resort base. Sightseeing Included: Chiang Rai White Temple, Blue Temple, Golden Triangle viewpoint, Mekong River private boat cruise. Optional Activities: A brief visit to the historic Union of Hill Tribes village to witness traditional long-neck paduang culture.'
                ),
                [
                    'Overnight Stay: Chiang Mai (Premium Luxury Heritage Resort)',
                    'Meals Included: International Buffet Breakfast & Chiang Rai Fine Dining Lunch',
                ],
            ),
            _day(
                5,
                'SAN KAMPHAENG CRAFT ARTISANS & HIGHLAND HOT SPRINGS',
                (
                    'SILK WEAVING MASTERCLASSES, GEMSTONE GALLERIES & FAREWELL DINNER Dedicate today to light, premium shopping and a flagship Premium Thailand Experience. In the afternoon, your driver drops your group at the San Kamphaeng Handicraft District, the artisan soul of Northern Thailand. The area features traditional factories where families can observe master craftsmen weaving delicate Thai silk garments, painting iconic paper umbrellas, and carving solid teak wood art pieces, making it an unparalleled location for premium souvenir shopping. Continue your relaxing drive to the San Kamphaeng Hot Springs, a natural park fully feature-packed with wide flat walkways and volcanic mineral pools. Dip your feet inside the warm therapeutic water or boil local eggs in the geyser streams, an absolute favorite for children. For your final evening, TRAGUIN has arranged our ultimate signature surprise: an intimate private grand-finale dinner party set at an elegant riverfront restaurant, allowing you to toast to an extraordinary family holiday under a starlit sky. Sightseeing Included: San Kamphaeng Silk & Umbrella Village, San Kamphaeng Hot Springs park entry. Evening Experience: Signature TRAGUIN Grand Finale Riverfront Family Dinner Party with live soft music.'
                ),
                [
                    'Overnight Stay: Chiang Mai (Premium Luxury Heritage Resort)',
                    'Meals Included: International Buffet Breakfast & 4-Course Riverfront Farewell Dinner',
                ],
            ),
            _day(
                6,
                'CHIANG MAI RETREAT & DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER UNITED Savor your final morning breakfast at your premium resort, capturing a final round of group family photos across the tropical landscaped gardens. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless group checkout. Depending on your flight departure schedule, your private van remains available for last-minute boutique delivers your family safely to Chiang Mai International Airport for your return flight home. Your premium Chiang Mai Family Tour concludes beautifully, leaving your loved ones with unforgettable memories crafted to perfection by TRAGUIN. Sightseeing Included: Nimman road artistic district access, private luxury airport departure transfer.'
                ),
                [
                    'shopping: or a brief stop at a trendy Nimman road cafe to grab an authentic Thai iced tea. Your private vehicle',
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Siripanna Villa Resort & Spa Chiang Mai Deluxe Lanna Room Complimentary Welcome Drinks & Access to Rice Padi Activity Zone',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Siripanna Villa Resort & Spa Chiang Mai Deluxe Lanna Room Complimentary Welcome Drinks & Access to Rice Padi Activity Zo',
            ),
            _hotel(
                'Shangri-La Chiang Mai Premier Family Room Welcome Fruit Platters, Free Ice Cream for Kids & Giant Splash Pool Access',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Shangri-La Chiang Mai Premier Family Room Welcome Fruit Platters, Free Ice Cream for Kids & Giant Splash Pool Access',
            ),
            _hotel(
                'Anantara Chiang Mai Resort Bespoke Kasara River View Suite Complimentary Floating Breakfast Setup & Kids Spa Discount Vouchers',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Anantara Chiang Mai Resort Bespoke Kasara River View Suite Complimentary Floating Breakfast Setup & Kids Spa Discount Vo',
            ),
            _hotel(
                'Four Seasons Resort Chiang Mai / 137 Pillars House Luxury Pavilion Villa / Rajah Brooke Suite Premium Vintage Champagne Bottle, Private Garden Access & 24/7 Butler Care',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Four Seasons Resort Chiang Mai / 137 Pillars House Luxury Pavilion Villa / Rajah Brooke Suite Premium Vintage Champagne ',
            )
        ],
        inclusions=[
            _inc_included('Daily Breakfast: 5 International Buffet Breakfast layouts with children-friendly sections.', 1),
            _inc_included('Private Vehicles: Private air-conditioned luxury van with an experienced driver for all transfers.', 2),
            _inc_included('Excursions: Full-day guided trip to Chiang Rai and the Golden Triangle with private boat.', 3),
            _inc_included('VIP Sightseeing: Premium front-row seats at the Khantoke Traditional Royal Dinner Show.', 4),
            _inc_included('Wildlife Parks: Entry tickets to ethical Elephant Nature Sanctuary with river bathing.', 5),
            _inc_included('Airfare: International and main internal domestic flight tickets to Chiang Mai.', 6),
            _inc_excluded('Accommodation: 05 Nights stay in handpicked premium family resorts.', 7),
            _inc_excluded('Visa Fees: Thailand Visa-on-Arrival or fast-track electronic visa processing fees.', 8),
        ],
    )
    return package, itinerary

def build_th_024(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-024'
    tour_code = 'TRG-USM-FAM-2026-V24'
    title = 'KOH SAMUI ESCAPE Chaweng Beach • Angthong National Marine Park • Koh Tan • Fishermans Village'
    duration = '05 Nights / 06 Days'
    slug = 'th-024-koh-samui-escape-chaweng-beach-angthong-national-marine-park-koh-tan-fishermans-village'
    itin_slug = 'th-024-koh-samui-escape-chaweng-beach-angthong-national-marine-park-koh-tan-fishermans-village-itinerary'
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
            _ph('Serial code TH-024 | TRAGUIN tour code TRG-USM-FAM-2026-V24', 1),
            _ph('State / Country: Thailand | Category: Best Koh Samui Tour Package', 2),
            _ph('Destinations: Koh Samui (5 Nights', 3),
            _ph('Ideal for: Families, Multi- generational Groups, Luxury Seekers', 4),
            _ph('Best season: December to September (Longest Sunshine Window)', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / Executive Van (Toyota Commuter) / Buffet Breakfast (CP), Private Yacht Lunch & Beachside Dinners Escape to a pristine paradise of swaying coconut palms and sapphire waters with th', 7),
            _ph('TRAGUIN Signature Experience: Private custom luxury yachts and island speed-craft charters,', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 9),
            _ph('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 10),
            _ph('Luxury Transportation: Executive modern vehicles equipped with cooling, on-board entertainment', 11)
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
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='KOH SAMUI ESCAPE Chaweng Beach',
        overview="05 Nights / 06 Days Premium Family Tour Vacation SERIAL CODE: TH-024 TRAGUIN TOUR CODE: TRG-USM-FAM-2026- V24 STATE / COUNTRY: Thailand / Gulf Coast CATEGORY: Best Koh Samui Tour Package DURATION: 05 Nights / 06 Days DESTINATIONS: Koh Samui (5 Nights Premium Island Stay) IDEAL FOR: Families, Multi- generational Groups, Luxury Seekers BEST SEASON: December to September (Longest Sunshine Window) VEHICLE TYPE: Private Luxury SUV / Executive Van (Toyota Commuter) MEAL PLAN: Buffet Breakfast (CP), Private Yacht Lunch & Beachside Dinners Escape to a pristine paradise of swaying coconut palms and sapphire waters with the Best Koh Samui Tour Package, thoughtfully designed by TRAGUIN. This specialized Koh Samui Family Tour presents a spectacular Luxury Koh Samui Holiday wrapped in premium stays, exposing your loved ones to breathtaking landscapes, hidden islands, and immersive cultural wonders to create unforgettable memories.\n\nTOUR OVERVIEW\nWelcome to your meticulously designed Koh Samui Escape, precisely structured for modern families who expect seamless coordination, children-friendly exploration paces, and elite hospitality layouts. Across 6 incredible days, your family will explore the finest marine sanctuaries, private yacht routes, and majestic cultural highlights of Thailand’s second-largest island. TRAGUIN Curated Experience Note: We ensure absolute comfort at every milestone. Traveling in private, air-conditioned luxury vans with dedicated chauffeurs allows your family to completely bypass public transit lines. Backed by handpicked premium stays and pre-vetted family dining paths, your group will experience a flawless trip protected by our 24/7 dedicated local concierge assistance. THE CHARM OF OUR LUXURY KOH SAMUI FAMILY TOUR Koh Samui has evolved into the ultimate island sanctuary for premium family travel, offering an unmatched variety of ethical animal encounters, private island archipelagos, and world-class culinary beachfront lanes. Choosing one of our high-end TRAGUIN Koh Samui Packages or an exceptional Koh Samui Honeymoon Package means stepping past generic travel routes into a world of exclusive benefits. This proposal targets top searched tourism keywords for Google ranking, ensuring the ultimate showcase of Koh Samui Sightseeing wonders. Discover Top Tourist Places in Thailand: the monumental Big Buddha Temple towering over the coast, the emerald volcanic lagoon of Angthong National Marine Park, and the colorful historic pathways of Fisherman’s Village. It is universally recognized as the Best Time to Visit Thailand to explore popular Instagram locations, engage in safe children-friendly marine athletics, and collect immersive experiences that your family will cherish for a lifetime. TRAGUIN Family Signatures: Private luxury yacht charter to Angthong Marine Park with sea-kayaks, an intimate coral reef snorkeling excursion to Koh Tan via private speed-craft, front-row family tables at Fisherman's Village beach fire shows, and dedicated luxury transportation. THE FUN & IMMERSIVE DAY-WISE ITINERARY",
        seo_title='TH-024 | KOH SAMUI ESCAPE Chaweng Beach | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-024 / TRG-USM-FAM-2026-V24): Koh Samui (5 Nights with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN KOH SAMUI & CHAWENG BEACH SUNSET', 1),
            _ih('Day 02: PRIVATE LUXURY YACHT TO ANGTHONG NATIONAL MARINE PARK', 2),
            _ih('Day 03: ISLAND HIGHLIGHTS TOUR & FISHERMANS VILLAGE FIRE SHOW', 3),
            _ih('Day 04: PRIVATE SPEEDBOAT EXPEDITION TO KOH TAN & KOH MADSUM', 4),
            _ih('Day 05: NA MUANG WATERFALLS & PRIVATE BEACH BBQ FINALE', 5),
            _ih('Day 06: KOH SAMUI RETREAT & DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private custom luxury yachts and island speed-craft charters,', 7),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 8),
            _ih('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN KOH SAMUI & CHAWENG BEACH SUNSET',
                (
                    'WELCOME TO PARADISE – THE TROPICAL COCONUT ISLAND ESCAPE BEGINS Your spectacular Koh Samui Family Tour begins perfectly the moment your family touches down at the charming, open-air Koh Samui International Airport. As you emerge from the arrival terminal, a warm, traditional Thai greeting awaits your party, coordinated seamlessly by your dedicated TRAGUIN tour representative. You will be escorted to your air-conditioned private luxury vehicle, ensuring a completely relaxed transfer straight to your handpicked premium beachfront resort. Arrive at your premium resort and check into your ocean-facing suite, featuring special welcome amenities for the family. Spend the afternoon unwinding by the panoramic infinity pool or taking your first family photos walking along the soft white sands of Chaweng Beach. In the evening, your private vehicle transfers your group to an upscale beachside restaurant for a welcome buffet dinner, allowing you to watch the sunset paint the Gulf of Thailand in pastel hues. Sightseeing Included: Private luxury van airport transit, scenic coastal driving layout, Chaweng Beach shoreline walk. Evening Experience: Family welcome dinner at an upscale beachfront restaurant with gorgeous ocean vistas.'
                ),
                [
                    'Overnight Stay: Koh Samui (Premium Luxury Beachfront Resort)',
                    'Meals Included: Curated Multi-Cuisine Family Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PRIVATE LUXURY YACHT TO ANGTHONG NATIONAL MARINE PARK',
                (
                    'MYSTICAL VOLCANIC LAGOONS, EMERALD LAKE & HIGHLAND VIEWS Savor a decadent breakfast with freshly prepared global dishes. Today hosts the ultimate centerpiece of your Best Koh Samui Tour Package: an exclusive private yacht charter to Angthong National Marine Park—a breathtaking archipelago of 42 pristine limestone islands. Avoid all crowded commercial passenger tour boats as your private luxury yacht glides smoothly over deep blue waters, offering an incredible photography point for the family. Anchor at Koh Mae Koh to discover the spectacular Emerald Lake (Talay Nai), a hidden saltwater lagoon completely enclosed by sheer cliffs. The children will be fully entertained exploring the island pathways or paddling stable sea-kayaks through giant rocky arches. Savor a magnificent gourmet lunch prepared fresh onboard by your personal crew. Spend your afternoon snorkeling among vibrant marine life or relaxing on a secluded white-sand sandbar before sailing back under a glorious golden sunset. Sightseeing Included: Private Yacht cruise, Angthong Marine Park entry, Emerald Lake viewing, Koh Mae Koh kayaking. Optional Activities: Hiking the steep, challenging cliffside trail up to the main Angthong 360-degree viewpoint.'
                ),
                [
                    'Overnight Stay: Koh Samui (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Onboard Luxury Yacht Gourmet Lunch',
                ],
            ),
            _day(
                3,
                'ISLAND HIGHLIGHTS TOUR & FISHERMANS VILLAGE FIRE SHOW',
                (
                    "THE BIG BUDDHA, HIN TA HIN YAI MONOLITHS & WATERFRONT CULTURE Enjoy a beautiful morning breakfast before starting a comprehensive Koh Samui Sightseeing cultural and natural wonder day. Your private chauffeur navigates your family to the iconic Big Buddha Temple (Wat Phra Yai), a majestic 12-meter golden statue towering over a rocky islet, offering panoramic coastal views. Next, visit the nearby colorful Wat Plai Laem to admire its 18-armed statue of Guanyin, the Goddess of Mercy. Continue your premium tour down the coast to the famous Hin Ta and Hin Yai (Grandfather and Grandmother) rock formations, naturally shaped monoliths rising from the clear sea—consistently named a top popular Instagram location. After a delicious Thai buffet lunch, spend your afternoon resting at the resort. In the evening, visit the historic Fisherman’s Village in Bophut. Walk past old wooden shophouses, enjoy boutique performances. Sightseeing Included: The Big Buddha Temple, Wat Plai Laem, Hin Ta Hin Yai rocks, Fisherman's Village walk. Evening Experience: VIP beachfront dining facing the world-famous Koh Samui spectacular fire-dancing show."
                ),
                [
                    'shopping: ,  and  sit  down  at  a  front-row  family  table  for  Pattaya-style  spectacular  beach  fire-dancing',
                    'Overnight Stay: Koh Samui (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Beachfront Family Dinner',
                ],
            ),
            _day(
                4,
                'PRIVATE SPEEDBOAT EXPEDITION TO KOH TAN & KOH MADSUM',
                (
                    "CORAL REEF SNORKELING & THE FAMOUS BEACH PIG ENCOUNTER Dedicate today to pure family joy and pristine island exploration. Following a hearty breakfast, your private speed-craft launches directly from the southern bay of the island. Cruise over calm waters to Koh Tan, a peaceful reef paradise completely free from cars. Put on your high-grade snorkeling gear to swim through vibrant shallow coral reefs teeming with friendly neon fish, an absolute favorite for children. Next, speed towards Koh Madsum (Pig Island). This unique island is globally celebrated for its friendly resident family of beach pigs that swim in the warm ocean water and relax with travelers on the sand. The kids will be fully entertained hand-feeding the piglets and taking incredible group portraits on the white sandshore. Savor a fresh local island lunch before cruising back to the main resort for an afternoon of relaxation. Sightseeing Included: Private Speedboat charter, Koh Tan reef snorkeling, Koh Madsum beach pig encounter. Optional Activities: A therapeutic 90-minute organic coconut oil massage at the resort's premium spa pavilion."
                ),
                [
                    'Overnight Stay: Koh Samui (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Pig Island Local Lunch',
                ],
            ),
            _day(
                5,
                'NA MUANG WATERFALLS & PRIVATE BEACH BBQ FINALE',
                (
                    "JUNGLE CASCADES, COCONUT FOREST TRAILS & CANDLELIGHT CELEBRATION Today combines lush interior nature with our crowning signature surprise. Following breakfast, your private luxury van transfers your family deep into the island's interior jungle to the magnificent Na Muang Waterfall 1. Witness a dramatic 18-meter fresh mountain cascade plunging into a natural pool surrounded by dense purple rock formations, providing excellent family photography opportunities. Take a short, easy walk through the surrounding coconut forests before returning to the resort to refresh for your final evening. TRAGUIN has arranged our ultimate signature highlight: an intimate, completely private beachfront candlelight barbecue dinner set in a secluded cove of the resort. Toast your family vacation with a glass of fine wine under a starlit sky as gentle waves roll in, celebrating a collection of unforgettable memories. Sightseeing Included: Na Muang Waterfall 1, coconut forest walking trails, private cove beach access. Evening Experience: Signature TRAGUIN Grand Finale Private Beachfront Candlelight Barbecue Dinner."
                ),
                [
                    'Overnight Stay: Koh Samui (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & 5-Course Private Cove Barbecue Dinner',
                ],
            ),
            _day(
                6,
                'KOH SAMUI RETREAT & DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER UNITED Savor your final morning breakfast at your premium resort, capturing a final round of group family photos across the tropical landscaped gardens. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless group checkout. Depending on your flight departure schedule, your private vehicle remains available for last-minute boutique to grab an authentic Thai iced tea. Your private vehicle delivers your family safely back to Koh Samui International Airport for your departure flight back home. Your premium Koh Samui Family Tour concludes beautifully, leaving your loved ones with unforgettable memories crafted to perfection by TRAGUIN. Sightseeing Included: Boutique souvenir shopping access, private luxury airport departure transfer.'
                ),
                [
                    'shopping: for local organic virgin coconut oils and handcrafted wood carvings, or a brief stop at a cliffside cafe',
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Outrigger Koh Samui Beach Resort Deluxe Ocean View Room Complimentary Welcome Drinks & Access to Coral Kids Club Play Zone',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Outrigger Koh Samui Beach Resort Deluxe Ocean View Room Complimentary Welcome Drinks & Access to Coral Kids Club Play Zo',
            ),
            _hotel(
                'Melia Koh Samui Premium Pool Access Family Room Welcome Fruit Platters, Free Ice Cream for Kids & Mini Waterpark Access',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Melia Koh Samui Premium Pool Access Family Room Welcome Fruit Platters, Free Ice Cream for Kids & Mini Waterpark Access',
            ),
            _hotel(
                'Anantara Bophut Koh Samui Resort Bespoke Anantara Sea View Family Suite Complimentary Floating Breakfast Setup & Kids Spa Discount Vouchers',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Anantara Bophut Koh Samui Resort Bespoke Anantara Sea View Family Suite Complimentary Floating Breakfast Setup & Kids Sp',
            ),
            _hotel(
                'Four Seasons Resort Koh Samui / W Koh Samui Ocean Front Luxury Pool Villa / Oasis Villa Premium Vintage Champagne Bottle, Private Beach Access & 24/7 Personal Butler Care',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Four Seasons Resort Koh Samui / W Koh Samui Ocean Front Luxury Pool Villa / Oasis Villa Premium Vintage Champagne Bottle',
            )
        ],
        inclusions=[
            _inc_included('Daily Breakfast: 5 International Buffet Breakfast layouts with children-friendly sections.', 1),
            _inc_included('Private Vehicles: Private air-conditioned luxury SUV / van with an experienced driver for all transfers.', 2),
            _inc_included('Bespoke Yachting: Private Luxury Yacht Charter to Angthong Marine Park with onboard lunch.', 3),
            _inc_included('Airfare: International and main domestic flight tickets to Koh Samui airport.', 4),
            _inc_excluded('Accommodation: 05 Nights stay in handpicked premium beachfront hotels.', 5),
            _inc_excluded('Visa Fees: Thailand Visa-on-Arrival or fast-track electronic visa processing fees.', 6),
            _inc_excluded('National Park Entry: Angthong Marine Park conservation entry fees (payable directly on site).', 7),
        ],
    )
    return package, itinerary

def build_th_025(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-025'
    tour_code = 'TRG-USM-HON-2026-V25'
    title = "KOH SAMUI ROMANCE Chaweng Beach • Angthong Marine Reserve • Koh Tan Private Cruise • Fisherman's Village"
    duration = '05 Nights / 06 Days'
    slug = 'th-025-koh-samui-romance-chaweng-beach-angthong-marine-reserve-koh-tan-private-cruise-fisherman-s-village'
    itin_slug = 'th-025-koh-samui-romance-chaweng-beach-angthong-marine-reserve-koh-tan-private-cruise-fisherman-s-village-itinerary'
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
            _ph('Serial code TH-025 | TRAGUIN tour code TRG-USM-HON-2026-V25', 1),
            _ph('State / Country: Thailand | Category: Luxury Honeymoon Package / Romance Escape', 2),
            _ph('Destinations: Koh Samui (5 Nights', 3),
            _ph('Ideal for: Honeymooners, Couples, Romance Seekers', 4),
            _ph('Best season: December to September (Remarkable Sunny Horizon)', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury European Sedan / Premium SUV (Chauffeur-Driven) / Bespoke Floating Breakfasts & Beachfront Candlelight Dinners Ignite your shared journey of love amidst a pristine sanctuary of swaying', 7),
            _ph('TRAGUIN Signature Experience: Private custom luxury yachts and island speed-craft charters,', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 9),
            _ph('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 10),
            _ph('Luxury Transportation: Executive modern vehicles equipped with cooling, on-board entertainment', 11)
        ],
        moods=['Luxury', 'Honeymoon', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='KOH SAMUI ROMANCE Chaweng Beach',
        overview="Village 05 Nights / 06 Days Ultra-Luxury Romantic Honeymoon Escape SERIAL CODE: TH-025 TRAGUIN TOUR CODE: TRG-USM-HON-2026- V25 STATE / COUNTRY: Thailand / Gulf Coast CATEGORY: Luxury Honeymoon Package / Romance Escape DURATION: 05 Nights / 06 Days DESTINATIONS: Koh Samui (5 Nights Ultra-Luxury Romance Sanctuary) IDEAL FOR: Honeymooners, Couples, Romance Seekers BEST SEASON: December to September (Remarkable Sunny Horizon) VEHICLE TYPE: Private Luxury European Sedan / Premium SUV (Chauffeur-Driven) MEAL PLAN: Bespoke Floating Breakfasts & Beachfront Candlelight Dinners Ignite your shared journey of love amidst a pristine sanctuary of swaying coconut palms and endless sapphire water with the absolute Koh Samui Honeymoon Package, masterfully engineered by TRAGUIN. This exclusive Luxury Koh Samui Holiday places your love story inside breathtaking landscapes, majestic private domains, and handpicked hotels, yielding immersive cultural wonders and unforgettable memories to cherish forever.\n\nTOUR OVERVIEW\nWelcome to your meticulously designed Koh Samui Romance escape, precisely structured for discerning couples who expect absolute operational perfection, seamless privacy, and elite hospitality layouts. Across 6 magical days, your love story will unfold across the finest marine sanctuaries, private yacht charters, and sunset beachfront sanctuaries of Thailand’s most elegant island. TRAGUIN Curated Experience Note: We believe that an extraordinary honeymoon lies in precise personalization. From pre-allocated private pool suites featuring spectacular views to private speed-craft ocean crossings and pre-arranged fine beachfront dining blocks, our on-ground destination management experts secure your absolute comfort with 24/7 dedicated assistance.\n\nWHY CHOOSE OUR LUXURY KOH SAMUI HONEYMOON EXPERIENCE?\nKoh Samui stands as an undisputed tropical masterpiece of high-end romance, combining tranquil ivory shores with private pool villa sanctuaries and world-class beachfront fine dining. Opting for a specialized Koh Samui Honeymoon Package or one of our ultra-exclusive TRAGUIN Koh Samui Packages ensures an itinerary far superior to generic public packages. This proposal targets top searched tourism keywords for Google ranking, ensuring the ultimate showcase of Koh Samui Sightseeing. Discover Top Tourist Places in Thailand: the golden mountain spires of the Big Buddha Temple towering over the coast, the emerald volcanic lagoon of Angthong National Marine Park, and the colorful historic pathways of Fisherman’s Village. It is universally recognized as the Best Time to Visit Thailand to explore popular Instagram locations, indulge in therapeutic couple's wellness spa rituals, capture stunning couple photos at premium photography points, and enjoy an unforgettable romantic holiday. TRAGUIN Honeymoon Signatures: Private luxury sunset yacht cruise to Angthong Marine Park with fine champagne, an intimate coral reef snorkeling excursion to Koh Tan via private speed-craft, front-row couple tables at Fisherman's Village beach fire shows, and dedicated luxury transportation. THE FUN & IMMERSIVE DAY-WISE ITINERARY",
        seo_title='TH-025 | KOH SAMUI ROMANCE Chaweng Beach | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-025 / TRG-USM-HON-2026-V25): Koh Samui (5 Nights with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN KOH SAMUI & CHAWENG BEACH SUNSET COCKTAIL', 1),
            _ih('Day 02: PRIVATE LUXURY YACHT TO ANGTHONG NATIONAL MARINE PARK', 2),
            _ih('Day 03: ISLAND HIGHLIGHTS TOUR & FISHERMANS VILLAGE GALA WATERFRONT', 3),
            _ih('Day 04: SPEEDBOAT TO KOH TAN REEFS & DEEP WELLNESS RETREAT', 4),
            _ih('Day 05: NA MUANG WATERFALLS & COVE BEACH BBC GRAND FINALE', 5),
            _ih('Day 06: KOH SAMUI RETREAT & DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private custom luxury yachts and island speed-craft charters,', 7),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 8),
            _ih('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN KOH SAMUI & CHAWENG BEACH SUNSET COCKTAIL',
                (
                    'WELCOME TO PARADISE – STEPPING INTO COCONUT ISLAND SANCTUARY Your spectacular Koh Samui Honeymoon Package begins perfectly the moment you touch down at the charming, open-air Koh Samui International Airport. Clear the arrival terminal to receive a warm Thai floral welcome from your private TRAGUIN lifestyle representative. Avoid all transport stress as you step directly into your chauffeured luxury executive sedan or premium SUV for a smooth scenic transfer straight to your handpicked ultra-luxury resort. Check into your ultra-luxury beachfront villa, detailed with a beautifully arranged honeymoon floral setup and a chilled complimentary bottle of premium sparkling wine. Spend the afternoon in complete privacy, unwinding inside your private infinity pool or walking hand-in-hand along the soft white sands of Chaweng Beach. In the evening, step down to a beachfront lounge for a welcome dinner, watching the sun paint the Gulf of Thailand in gorgeous pastel hues. Sightseeing Included: Private luxury vehicle airport transit, scenic coastal driving layout, Chaweng Beach shoreline walk. Evening Experience: Welcome dinner and tropical cocktail mixer at an upscale beachfront lounge with sunset vistas.'
                ),
                [
                    'Overnight Stay: Koh Samui (Ultra-Luxury Beachfront Private Pool Villa Resort)',
                    'Meals Included: Curated Multi-Cuisine Romantic Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PRIVATE LUXURY YACHT TO ANGTHONG NATIONAL MARINE PARK',
                (
                    "ANDAMAN COVES – EXCLUSIVE SAILING, EMERALD VOLCANIC LAGOON & CHAMPAGNE Wake up to a gorgeous morning over the water and enjoy a lavish buffet breakfast. Today hosts the ultimate centerpiece of your Best Koh Samui Tour Package: an exclusive private yacht charter to Angthong National Marine Park—a breathtaking archipelago of 42 pristine limestone islands. Avoid all crowded commercial passenger tour boats as your private luxury yacht glides smoothly over deep blue waters, offering an incredible photography point for your honeymoon diary. Anchor at Koh Mae Koh to discover the spectacular Emerald Lake (Talay Nai), a hidden saltwater lagoon completely enclosed by sheer cliffs. Explore the island pathways or paddle stable sea-kayaks through giant rocky arches. Savor a magnificent gourmet lunch prepared fresh onboard by your personal crew and paired with fine champagne. Spend your afternoon snorkeling among vibrant marine life or relaxing on a secluded white-sand sandbar before sailing back under a glorious golden sunset. Sightseeing Included: Private Yacht cruise, Angthong Marine Park entry, Emerald Lake viewing, Koh Mae Koh kayaking. Optional Activities: Professional drone couples' photography session on the yacht deck with the limestone karsts backdrop."
                ),
                [
                    'Overnight Stay: Koh Samui (Ultra-Luxury Beachfront Private Pool Villa Resort)',
                    'Meals Included: International Buffet Breakfast & Onboard Luxury Yacht Gourmet Lunch with Champagne',
                ],
            ),
            _day(
                3,
                'ISLAND HIGHLIGHTS TOUR & FISHERMANS VILLAGE GALA WATERFRONT',
                (
                    "THE BIG BUDDHA, HIN TA HIN YAI MONOLITHS & WATERFRONT CULTURE Enjoy a beautiful morning breakfast before starting a comprehensive Koh Samui Sightseeing cultural and natural wonder day. Your private chauffeur navigates to the iconic Big Buddha Temple (Wat Phra Yai), a majestic 12-meter golden statue towering over a rocky islet, offering panoramic coastal views. Next, visit the nearby colorful Wat Plai Laem to admire its 18-armed statue of Guanyin, the Goddess of Mercy. Continue your premium tour down the coast to the famous Hin Ta and Hin Yai (Grandfather and Grandmother) rock formations, naturally shaped monoliths rising from the clear sea—consistently named a top popular Instagram location. After a delicious Thai buffet lunch, spend your afternoon resting at the resort. In the evening, visit the historic Fisherman’s Village in Bophut. Walk past old wooden shophouses, enjoy boutique performances. Sightseeing Included: The Big Buddha Temple, Wat Plai Laem, Hin Ta Hin Yai rocks, Fisherman's Village walk. Evening Experience: VIP beachfront dining facing the world-famous Koh Samui spectacular fire-dancing show."
                ),
                [
                    'shopping: ,  and  sit  down  at  a  front-row  couple  table  for  Pattaya-style  spectacular  beach  fire-dancing',
                    'Overnight Stay: Koh Samui (Ultra-Luxury Beachfront Private Pool Villa Resort)',
                    'Meals Included: International Buffet Breakfast & Beachfront Intimate Seafood Dinner',
                ],
            ),
            _day(
                4,
                'SPEEDBOAT TO KOH TAN REEFS & DEEP WELLNESS RETREAT',
                (
                    "CORAL GARDENS SNORKELING & A 120-MINUTE REJUVENATION RETREAT Dedicate your morning to coral exploration and crystalline horizons. Following a hearty breakfast, your private speed-craft launches directly from the resort bay. Cruise over calm waters to Koh Tan, a peaceful reef paradise completely free from crowds. Put on your high-grade snorkeling gear to swim hand-in-hand through vibrant shallow coral reefs teeming with friendly neon fish, an absolute favorite experience. Next, land on the white sands of Koh Madsum (Pig Island) for beach walking and relaxation. Return to the main island in the afternoon and escape into an award-winning luxury day spa sanctuary. TRAGUIN has reserved an exclusive 120-minute couple's massage package. Indulge side-by-side in traditional Thai herbal steam rooms, aromatic body scrubs, and therapeutic aromatic oil massages using organic cold-pressed coconut oils, leaving your bodies fully refreshed. Sightseeing Included: Private Speedboat charter, Koh Tan reef snorkeling, Koh Madsum beach access. Optional Activities: A visit to a traditional artisan studio or a local organic coconut wellness farm."
                ),
                [
                    'Overnight Stay: Koh Samui (Ultra-Luxury Beachfront Private Pool Villa Resort)',
                    'Meals Included: International Buffet Breakfast & Premium Local Thai Dining Lunch',
                ],
            ),
            _day(
                5,
                'NA MUANG WATERFALLS & COVE BEACH BBC GRAND FINALE',
                (
                    "JUNGLE CASCADES, COCONUT FOREST TRAILS & CANDLELIGHT CELEBRATION Today combines lush interior nature with our crowning signature romantic surprise. Following a beautiful floating breakfast served right inside your private infinity pool villa, your private luxury van transfers you deep into the island's interior jungle to the magnificent Na Muang Waterfall 1. Witness a dramatic 18-meter fresh mountain cascade plunging into a natural pool surrounded by dense purple rock formations, providing excellent photography opportunities. Take a short, easy walk through the surrounding coconut forests before returning to the resort to refresh for your final evening. TRAGUIN has arranged our ultimate signature romantic highlight: an intimate, completely private beachfront candlelight barbecue dinner set in a secluded cove of the resort. Toast your honeymoon holiday with a glass of fine wine under a starlit sky as gentle waves roll in, celebrating a collection of unforgettable memories. Sightseeing Included: Na Muang Waterfall 1, coconut forest walking trails, private cove beach access. Evening Experience: Signature TRAGUIN Grand Finale Private Beachfront Candlelight Barbecue Dinner."
                ),
                [
                    'Overnight Stay: Koh Samui (Ultra-Luxury Beachfront Private Pool Villa Resort)',
                    'Meals Included: Bespoke Floating Villa Breakfast & Ultra-Luxury Beachside 5-Course Dinner',
                ],
            ),
            _day(
                6,
                'KOH SAMUI RETREAT & DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER UNITED Savor your final morning breakfast at your villa veranda, capturing a final round of couple photos across the tropical landscaped gardens. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless group checkout. Depending on your flight departure schedule, your private vehicle remains available for last-minute boutique to grab an authentic Thai iced tea. Your private vehicle delivers your family safely back to Koh Samui International Airport for your departure flight back home. Your premium Koh Samui Honeymoon Package concludes beautifully, leaving your hearts full of unforgettable memories crafted to perfection by TRAGUIN. Sightseeing Included: Boutique souvenir shopping access, private luxury airport departure transfer.'
                ),
                [
                    'shopping: for local organic virgin coconut oils and handcrafted wood carvings, or a brief stop at a cliffside cafe',
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Outrigger Koh Samui Beach Resort Deluxe Pool Villa Complimester Honeymoon Cake & Bed Floral Styling',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Outrigger Koh Samui Beach Resort Deluxe Pool Villa Complimester Honeymoon Cake & Bed Floral Styling',
            ),
            _hotel(
                'Melia Koh Samui Premium Pool Access Family Room Welcome Fruit Platters, Free Bed Decoration & 1 Bottle of Wine',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Melia Koh Samui Premium Pool Access Family Room Welcome Fruit Platters, Free Bed Decoration & 1 Bottle of Wine',
            ),
            _hotel(
                'Anantara Bophut Koh Samui Resort Bespoke Anantara Sea View Family Suite Complimentary Floating Breakfast Setup & Kids Spa Discount Vouchers',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Anantara Bophut Koh Samui Resort Bespoke Anantara Sea View Family Suite Complimentary Floating Breakfast Setup & Kids Sp',
            ),
            _hotel(
                'Four Seasons Resort Koh Samui / W Koh Samui Ocean Front Luxury Pool Villa / Oasis Villa Premium Vintage Champagne Bottle, Private Beach Access & 24/7 Personal Butler Care',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Four Seasons Resort Koh Samui / W Koh Samui Ocean Front Luxury Pool Villa / Oasis Villa Premium Vintage Champagne Bottle',
            )
        ],
        inclusions=[
            _inc_included('Daily Breakfast: 5 International Buffet Breakfast layouts with children-friendly sections.', 1),
            _inc_included('Private Vehicles: Private air-conditioned luxury SUV / van with an experienced driver for all transfers.', 2),
            _inc_included('Bespoke Yachting: Private Luxury Yacht Charter to Angthong Marine Park with onboard lunch.', 3),
            _inc_included('Airfare: International and main domestic flight tickets to Koh Samui airport.', 4),
            _inc_excluded('Accommodation: 05 Nights stay in handpicked premium beachfront hotels.', 5),
            _inc_excluded('Visa Fees: Thailand Visa-on-Arrival or fast-track electronic visa processing fees.', 6),
            _inc_excluded('National Park Entry: Angthong Marine Park conservation entry fees (payable directly on site).', 7),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, mini-bar billing, and tips.', 8),
            _inc_excluded('Insurance: Overseas comprehensive family medical and travel insurance protection.', 9),
        ],
    )
    return package, itinerary

def build_th_026(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-026'
    tour_code = 'TRG-USM-LUX-HON-2026'
    title = 'LUXURY KOH SAMUI TOUR PACKAGE Chaweng Beach • Choeng Mon • Angthong Marine Park • Koh Tao Private Cruise'
    duration = '06 Nights / 07 Days'
    slug = 'th-026-luxury-koh-samui-tour-package-chaweng-beach-choeng-mon-angthong-marine-park-koh-tao-private-cruise'
    itin_slug = 'th-026-luxury-koh-samui-tour-package-chaweng-beach-choeng-mon-angthong-marine-park-koh-tao-private-cruise-itinerary'
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
            _ph('Serial code TH-026 | TRAGUIN tour code TRG-USM-LUX-HON-2026', 1),
            _ph('State / Country: Thailand | Category: Luxury Koh Samui Holiday / Honeymoon Package', 2),
            _ph('Destinations: Koh Samui Private Pool', 3),
            _ph('Ideal for: Honeymooners, Discerning Couples, Luxury Seekers', 4),
            _ph('Best season: December to September (Remarkable Year- Round Sunshine)', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Chauffeur- Driven Mercedes-Benz / BMW Executive Sedan / Bespoke Champagne Floating Breakfasts & Michelin-Standard Dining Begin your lifelong journey of together-ness inside an ethereal paradis', 7),
            _ph('TRAGUIN Signature Experience: Private custom luxury yachts and island speed-craft charters,', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 9),
            _ph('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 10),
            _ph('Luxury Transportation: Executive modern vehicles equipped with cooling, on-board entertainment', 11)
        ],
        moods=['Luxury', 'Honeymoon', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='LUXURY KOH SAMUI TOUR PACKAGE Chaweng Beach',
        overview="Chaweng Beach • Choeng Mon • Angthong Marine Park • Koh Tao Private Cruise 06 Nights / 07 Days Ultra-Luxury Romantic Honeymoon Sanctuary SERIAL CODE: TH-026 TRAGUIN TOUR CODE: TRG-USM-LUX- HON-2026 STATE / COUNTRY: Thailand / Gulf Coast CATEGORY: Luxury Koh Samui Holiday / Honeymoon Package DURATION: 06 Nights / 07 Days DESTINATIONS: Koh Samui Private Pool Villa Sanctuary (6 Nights) IDEAL FOR: Honeymooners, Discerning Couples, Luxury Seekers BEST SEASON: December to September (Remarkable Year- Round Sunshine) VEHICLE TYPE: Private Chauffeur- Driven Mercedes-Benz / BMW Executive Sedan MEAL PLAN: Bespoke Champagne Floating Breakfasts & Michelin-Standard Dining Begin your lifelong journey of together-ness inside an ethereal paradise of pristine white sands, private sanctuaries, and swaying coconut canopies with the ultimate Koh Samui Honeymoon Package, meticulously crafted by TRAGUIN. This flagship Luxury Koh Samui Holiday places your romantic narrative across breathtaking landscapes, handpicked hotels of global distinction, and exclusive experiences to create unforgettable memories. • Luxury Koh Samui Proposal TOUR OVERVIEW Welcome to your masterfully structured Luxury Koh Samui honeymoon itinerary, designed for couples who expect flawless operational execution, absolute seclusion, and elite lifestyle inclusions. Across 7 magnificent days, TRAGUIN will wrap your holiday in pure indulgence. Enjoy VIP fast-track arrivals, private chauffeur- driven executive European sedans, custom multi-island marine charters, and private chef culinary journeys. TRAGUIN Curated Experience Note: We ensure absolute perfection at every milestone. From pre-allocated private pool suites featuring spectacular ocean view settings to private yacht crossings and pre-arranged fine beachfront dining zones, your honeymoon is managed 24/7 by our dedicated on-ground premium concierge network. THE ALLURE OF OUR PREMIUM KOH SAMUI EXPERIENCE Koh Samui stands as an undisputed global masterpiece of high-end romance, combining tranquil azure horizons with award-winning private pool villas, cliffside wellness sanctuaries, and elite beach club cultures. Booking a signature Koh Samui Honeymoon Package or one of our ultra-exclusive TRAGUIN Koh Samui Packages guarantees access to hidden domains and priority privileges. This proposal integrates top searched keywords for Google ranking, showcasing an elite layout of premier Koh Samui Sightseeing. Uncover iconic attractions and top tourist places in Thailand: the monumental Big Buddha Temple towering over the coast, the emerald volcanic lagoon of Angthong National Marine Park, and the colorful historic pathways of Fisherman’s Village. It is universally recognized as the Best Time to Visit Thailand to explore popular Instagram locations, indulge in therapeutic couple's wellness spa rituals, capture stunning photos at premium photography points, and enjoy an unforgettable romantic holiday. TRAGUIN Honeymoon Highlights: Exclusive private sunset yacht cruise across the Angthong Archipelago, an intimate coral reef snorkeling excursion to Koh Tan via private speed-craft, a 150-minute luxury couple's aroma-spa treatment, and an elite private beach cove candlelight gala. • Luxury Koh Samui Proposal THE ROMANTIC DAY-WISE ITINERARY\n\nTOUR OVERVIEW\nWelcome to your masterfully structured Luxury Koh Samui honeymoon itinerary, designed for couples who expect flawless operational execution, absolute seclusion, and elite lifestyle inclusions. Across 7 magnificent days, TRAGUIN will wrap your holiday in pure indulgence. Enjoy VIP fast-track arrivals, private chauffeur- driven executive European sedans, custom multi-island marine charters, and private chef culinary journeys. TRAGUIN Curated Experience Note: We ensure absolute perfection at every milestone. From pre-allocated private pool suites featuring spectacular ocean view settings to private yacht crossings and pre-arranged fine beachfront dining zones, your honeymoon is managed 24/7 by our dedicated on-ground premium concierge network. THE ALLURE OF OUR PREMIUM KOH SAMUI EXPERIENCE Koh Samui stands as an undisputed global masterpiece of high-end romance, combining tranquil azure horizons with award-winning private pool villas, cliffside wellness sanctuaries, and elite beach club cultures. Booking a signature Koh Samui Honeymoon Package or one of our ultra-exclusive TRAGUIN Koh Samui Packages guarantees access to hidden domains and priority privileges. This proposal integrates top searched keywords for Google ranking, showcasing an elite layout of premier Koh Samui Sightseeing. Uncover iconic attractions and top tourist places in Thailand: the monumental Big Buddha Temple towering over the coast, the emerald volcanic lagoon of Angthong National Marine Park, and the colorful historic pathways of Fisherman’s Village. It is universally recognized as the Best Time to Visit Thailand to explore popular Instagram locations, indulge in therapeutic couple's wellness spa rituals, capture stunning photos at premium photography points, and enjoy an unforgettable romantic holiday. TRAGUIN Honeymoon Highlights: Exclusive private sunset yacht cruise across the Angthong Archipelago, an intimate coral reef snorkeling excursion to Koh Tan via private speed-craft, a 150-minute luxury couple's aroma-spa treatment, and an elite private beach cove candlelight gala. • Luxury Koh Samui Proposal THE ROMANTIC DAY-WISE ITINERARY",
        seo_title='TH-026 | LUXURY KOH SAMUI TOUR PACKAGE Chaweng Beach | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Thailand package (TH-026 / TRG-USM-LUX-HON-2026): Koh Samui Private Pool with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN KOH SAMUI & PRIVATE VILLA SANCTUARY RETREAT', 1),
            _ih('Day 02: PRIVATE LUXURY YACHT TO ANGTHONG MARINE ARCHIPELAGO', 2),
            _ih('Day 03: SOUTHERN ISLES CHARTER TO KOH TAN & PIG ISLAND', 3),
            _ih('Day 04: KOH SAMUI CULTURAL HIGHLIGHTS & FINE DINING RETREAT', 4),
            _ih('Day 05: AWARD-WINNING COUPLES SPA & FISHERMANS VILLAGE GALA', 5),
            _ih('Day 06: NA MUANG JUNGLE CASCADES & SECLUDED COVE GRAND FINALE', 6),
            _ih('Day 07: KOH SAMUI DEPARTURE', 7),
            _ih('TRAGUIN Signature Experience: Private custom luxury yachts and island speed-craft charters,', 8),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 9),
            _ih('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN KOH SAMUI & PRIVATE VILLA SANCTUARY RETREAT',
                (
                    'WELCOME TO PARADISE – STEPPING INTO COCONUT ISLAND OPULENCE Your spectacular Koh Samui Honeymoon Package unfolds perfectly the moment you touch down at the charming, open-air Koh Samui International Airport. Clear the arrival terminal via our pre-arranged VIP fast- track protocol to receive a warm Thai floral welcome from your private TRAGUIN lifestyle representative. Avoid all transport queues as you step directly into your chauffeured luxury executive sedan for a smooth scenic transfer straight to your handpicked ultra-luxury resort. Check into your ultra-luxury beachfront pavilion, detailed with a beautifully arranged honeymoon floral setup and a chilled complimentary bottle of premium champagne. Spend the afternoon in complete privacy, unwinding inside your private pool or walking hand-in-hand along the soft white sands. In the evening, step down to a private villa deck for a curated welcome dinner, watching the sun paint the Gulf of Thailand in gorgeous pastel hues, creating your first unforgettable memories together. Sightseeing Included: VIP airport fast-track reception & clearance, scenic private luxury vehicle transfer, private beach walk. Evening Experience: Bespoke welcome dinner party at your private villa deck with a customized personal chef menu. • Luxury Koh Samui Proposal'
                ),
                [
                    'Overnight Stay: Koh Samui (Ultra-Luxury Beachfront Private Pool Villa Resort)',
                    'Meals Included: Bespoke 4-Course Private Villa Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PRIVATE LUXURY YACHT TO ANGTHONG MARINE ARCHIPELAGO',
                (
                    "ANDAMAN COVES – EXCLUSIVE SAILING, EMERALD VOLCANIC LAGOON & CHAMPAGNE Wake up to a gorgeous morning over the water and enjoy a lavish buffet breakfast. Today hosts the ultimate centerpiece of your Best Koh Samui Tour Package: an exclusive private yacht charter to Angthong National Marine Park—a breathtaking archipelago of 42 pristine limestone islands. Avoid all crowded commercial passenger tour boats as your private luxury yacht glides smoothly over deep blue waters, offering an incredible photography point for your honeymoon diary. Anchor at Koh Mae Koh to discover the spectacular Emerald Lake (Talay Nai), a hidden saltwater lagoon completely enclosed by sheer cliffs. Explore the island pathways or paddle stable sea-kayaks through giant rocky arches. Savor a magnificent gourmet lunch prepared fresh onboard by your personal crew and paired with fine vintage wines. Spend your afternoon snorkeling among vibrant marine life or relaxing on a secluded white-sand sandbar before sailing back under a glorious golden sunset. Sightseeing Included: Private Yacht cruise, Angthong Marine Park entry, Emerald Lake viewing, Koh Mae Koh kayaking. Optional Activities: Professional drone couples' photography session on the yacht deck with the limestone karsts backdrop. • Luxury Koh Samui Proposal"
                ),
                [
                    'Overnight Stay: Koh Samui (Ultra-Luxury Beachfront Private Pool Villa Resort)',
                    'Meals Included: International Buffet Breakfast & Onboard Luxury Yacht Gourmet Lunch with Vintage Wine',
                ],
            ),
            _day(
                3,
                'SOUTHERN ISLES CHARTER TO KOH TAN & PIG ISLAND',
                (
                    'TURQUOISE REEF SNORKELING & INTIMATE MADSUM SANDSHORE SUNSET Savor a beautiful breakfast before starting an incredible island adventure. Skip the large commercial groups as TRAGUIN arranges an exclusive private speedboat charter to explore the hidden southern isles of Koh Tan and Koh Madsum. Cruise over calm waters to Koh Tan, a peaceful reef paradise completely free from crowds, where you can swim hand-in-hand through vibrant shallow coral gardens teeming with marine life. Next, land on the white sands of Koh Madsum (Pig Island), world-famous for its friendly resident beach pigs that swim in the warm ocean water. The couple can enjoy unique photography points hand-feeding the piglets on the sandshore. Savor a fresh local island seafood lunch served right under a private canopy. Return to the main island in the late afternoon to witness a striking sunset from your resort balcony. Sightseeing Included: Private Speedboat charter, Koh Tan reef snorkeling, Koh Madsum beach pig encounter. Evening Experience: Relaxing beachfront lounge access with customized mocktails and panoramic horizon views.'
                ),
                [
                    'Overnight Stay: Koh Samui (Ultra-Luxury Beachfront Private Pool Villa Resort)',
                    'Meals Included: International Buffet Breakfast & Pig Island Local Seafood Lunch',
                ],
            ),
            _day(
                4,
                'KOH SAMUI CULTURAL HIGHLIGHTS & FINE DINING RETREAT',
                (
                    'THE BIG BUDDHA, HIN TA HIN YAI SHORES & CHIC WATERFRONT GALA Enjoy a beautiful morning breakfast before starting a comprehensive Koh Samui Sightseeing cultural and natural wonder day. Your private chauffeur navigates your family of two to the iconic Big Buddha Temple (Wat Phra Yai), a majestic 12-meter golden statue towering over a rocky islet, offering panoramic coastal views. Next, visit the nearby colorful Wat Plai Laem to admire its 18-armed statue of Guanyin, the Goddess of Mercy. Continue your premium tour down the coast to the famous Hin Ta and Hin Yai (Grandfather and Grandmother) rock formations, naturally shaped monoliths rising from the clear sea—consistently named a top popular Instagram location. Savor a delicious contemporary Thai fine dining lunch at a cliffside venue. Spend your afternoon relaxing at the resort before an evening of leisure or exploring the local lifestyle bazaars. Sightseeing Included: The Big Buddha Temple, Wat Plai Laem, Hin Ta Hin Yai rocks, driving panoramic orientation. Evening Experience: A relaxed romantic walk through the upscale beachfront walkways of Chaweng beach. • Luxury Koh Samui Proposal'
                ),
                [
                    'Overnight Stay: Koh Samui (Ultra-Luxury Beachfront Private Pool Villa Resort)',
                    'Meals Included: International Buffet Breakfast & Cliffside Gastronomy Lunch',
                ],
            ),
            _day(
                5,
                'AWARD-WINNING COUPLES SPA & FISHERMANS VILLAGE GALA',
                (
                    "150 MINUTES OF DEEP REJUVENATION & SPECTACULAR BEACH FIRE PERFORMANCE Dedicate your morning to absolute body wellness and relaxation. Following breakfast, your private chauffeur transfers you to an award-winning luxury day spa sanctuary nestled inside a tropical jungle enclave. Indulge in an exclusive 150-minute TRAGUIN Signature Couple's Spa, featuring a traditional Thai herbal steam, organic coconut scrubs, and a therapeutic aromatic hot stone oil massage side-by-side, leaving your bodies fully refreshed. In the evening, head towards the historic Fisherman’s Village in Bophut. Walk past old wooden shophouses, explore boutique fashion markets, and find exquisite local souvenirs. TRAGUIN has reserved a premium front-row couple's table at a high-end beachfront restaurant. Enjoy a delicious meal while watching Koh Samui’s world-famous spectacular fire-dancing show right on the sandshore. Sightseeing Included: Fisherman's Village Bophut walk, VIP beachfront show access. Evening Experience: Front-row couples' dining facing the spectacular seaside acrobatic fire show. • Luxury Koh Samui Proposal"
                ),
                [
                    'Overnight Stay: Koh Samui (Ultra-Luxury Beachfront Private Pool Villa Resort)',
                    'Meals Included: International Buffet Breakfast & Beachfront Fine Dining Dinner',
                ],
            ),
            _day(
                6,
                'NA MUANG JUNGLE CASCADES & SECLUDED COVE GRAND FINALE',
                (
                    'MISTY WATERFALLS, FLOTING BREAKFAST & BEACH CANDLELIGHT CELEBRATION Today combines lush interior nature with our crowning signature romantic surprise. Savor a magnificent premium floating breakfast served right inside your private infinity pool villa. In the afternoon, your chauffeur transfers you deep into the interior jungle to the magnificent Na Muang Waterfall 1. Witness a dramatic 18- meter fresh mountain cascade plunging into a natural pool surrounded by dense rock formations. Return to the resort to refresh for your final night. TRAGUIN has arranged our ultimate signature romantic highlight: an intimate, completely private beachfront candlelight barbecue dinner set in a secluded cove of the resort. Toast your honeymoon holiday with a glass of vintage wine under a starlit sky as gentle waves roll in, celebrating an exceptional collection of unforgettable memories. Sightseeing Included: Na Muang Waterfall 1, coconut forest walking trails, private cove beach access. Evening Experience: Signature TRAGUIN Grand Finale Private Beachfront Candlelight Barbecue Dinner.'
                ),
                [
                    'Overnight Stay: Koh Samui (Ultra-Luxury Beachfront Private Pool Villa Resort)',
                    'Meals Included: Premium Floating Breakfast & Ultra-Luxury Beachside 5-Course Dinner',
                ],
            ),
            _day(
                7,
                'KOH SAMUI DEPARTURE',
                (
                    'CHERISHING ROMANTIC MEMORIES BEYOND DESTINATIONS – FOREVER REFRESHED Savor your final morning breakfast at your villa veranda, capturing a final round of couple photos across the tropical landscaped gardens. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless group checkout. Your private luxury executive sedan delivers you safely back to Koh Samui International Airport for your departure flight back home, where our staff assists with premium lounge clearance. Your premium Koh Samui Honeymoon Package concludes beautifully, leaving your hearts full of unforgettable memories crafted to perfection by TRAGUIN. Sightseeing Included: Boutique souvenir shopping access, private luxury airport departure transfer. • Luxury Koh Samui Proposal'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Luxury Outrigger Koh Samui Beach Resort Deluxe Private Pool Villa Complimentary Honeymoon Cake & Bed Floral Decoration',
                'Multi-city Thailand',
                '6N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Luxury Outrigger Koh Samui Beach Resort Deluxe Private Pool Villa Complimentary Honeymoon Cake & Bed Floral Decoration',
            ),
            _hotel(
                'Luxury Melia Koh Samui Premium Pool Access Family Suite Welcome Fruit Platter, Free Bed Decoration & 1 Bottle of Fine Wine',
                'Multi-city Thailand',
                '6N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Luxury Melia Koh Samui Premium Pool Access Family Suite Welcome Fruit Platter, Free Bed Decoration & 1 Bottle of Fine Wi',
            ),
            _hotel(
                'Four Seasons Resort Koh Samui / W Koh Samui Ocean Front Luxury Pool Villa / Oasis Ocean Villa Premium Vintage Champagne Bottle, Private Beach Access & 24/7 Personal Butler Care',
                'Multi-city Thailand',
                '6N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Four Seasons Resort Koh Samui / W Koh Samui Ocean Front Luxury Pool Villa / Oasis Ocean Villa Premium Vintage Champagne ',
            )
        ],
        inclusions=[
            _inc_included('Daily Breakfast: 6 International Buffet Breakfast layouts with children-friendly variants.', 1),
            _inc_included('Private Vehicles: Private air-conditioned luxury European sedan or van with driver.', 2),
            _inc_included('Bespoke Yachting: Private Luxury Yacht Charter to Angthong Marine Park with onboard lunch.', 3),
            _inc_included('Island Excursion: Private Speedboat tour to Koh Tan coral reefs and Koh Madsum Pig Island.', 4),
            _inc_included('Airfare: International and main domestic flight tickets to Koh Samui airport.', 5),
            _inc_excluded('Accommodation: 06 Nights stay in handpicked premium beachfront pool villas.', 6),
            _inc_excluded('Visa Fees: Thailand Visa-on-Arrival or fast-track electronic visa processing fees.', 7),
            _inc_excluded('National Park Entry: Angthong Marine Park conservation entry fees (payable directly on site).', 8),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, mini-bar billing, and tips.', 9),
        ],
    )
    return package, itinerary

def build_th_027(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-027'
    tour_code = 'TRG-BKK-FEM-SHOP-2026'
    title = 'ICONSIAM • Siam Paragon • EmSphere • Chatuchak Weekend Market'
    duration = '04 Nights / 05 Days'
    slug = 'th-027-iconsiam-siam-paragon-emsphere-chatuchak-weekend-market'
    itin_slug = 'th-027-iconsiam-siam-paragon-emsphere-chatuchak-weekend-market-itinerary'
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
            _ph('Serial code TH-027 | TRAGUIN tour code TRG-BKK-FEM-SHOP-2026', 1),
            _ph('State / Country: Thailand | Category: Female Only / Luxury Shopping Retreat', 2),
            _ph('Destinations: Bangkok (4 Nights', 3),
            _ph('Ideal for: Girl Gangs, Trendsetters, Solo Female Shoppers, Mother-Daughter Duos', 4),
            _ph('Best season: Year-Round (Amazing Mid-Year & Year-End Mega Sales)', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Safe Luxury Van with Dedicated Driver & Cargo Capacity / Buffet Breakfast (CP), Chic Designer Cafes & Skyline Dinners Indulge your inner fashionista with the absolute Best Bangkok Tour Package', 7),
            _ph('TRAGUIN Signature Experience: Private custom retail assistant tracks and premium sky-view', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium luxury hotels located directly adjacent to main', 9),
            _ph('Personalized Assistance: English-fluent dedicated local coordinators to manage mall reservation', 10)
        ],
        moods=['Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='ICONSIAM',
        overview="TOUR OVERVIEW\nWelcome to your meticulously designed Bangkok Shopping Festival escape, precisely structured for stylish women who expect absolute operational perfection, maximum safety, and elite hospitality layouts. Across 5 incredible days, TRAGUIN ensures an unparalleled retail itinerary featuring premium stays at centrally located luxury hotels, private secure logistics with extensive trunk space, and curated lifestyle experiences designed around high-fashion collections and sensory pampering. TRAGUIN Curated Experience Note: Your group's security and luxury are our absolute priorities. From female-friendly local coordinators to custom-picked designer night market paths and pre-booked tables at elite rooftop sky lounges, your ladies' circle will experience a completely flawless, relaxed, and immersive holiday. THE APPEAL OF A LUXURY BANGKOK RETAIL GETAWAY Bangkok stands as the undisputed shopping capital of Southeast Asia, effortlessly blending massive ultra- modern luxury plazas with historic floating markets, independent artisan quarters, and bohemian fashion bazaars. Opting for a specialized female-only getaway or a dedicated Thailand Family Tour variant through TRAGUIN opens up an unmatched world of elite privileges. This proposal targets the most highly searched tourism keywords for Google ranking, ensuring the ultimate showcase of Bangkok Sightseeing wonders. Discover Top Tourist Places in Thailand: the monumental waterfront architectural spaces of ICONSIAM, the high-fashion designer boutiques of Siam Paragon, and the bustling independent craft stalls of Chatuchak. It is universally recognized as the Best Time to Visit Thailand to explore popular Instagram locations, enjoy a professional Premium Thailand Experience, indulge in therapeutic couple and group day spa rituals, and collect deep, immersive experiences that define high-end travel. TRAGUIN Retail Special Exclusives: VIP Fast-Track airport arrival service, a private personal shopping assistant voucher, front-row premium seating at a traditional luxury dinner cruise, sunset access to Mahanakhon SkyWalk, and an immersive 120-minute aromatherapy wellness package. THE HIGH-FASHION DAY-WISE ITINERARY",
        seo_title='TH-027 | ICONSIAM | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Thailand package (TH-027 / TRG-BKK-FEM-SHOP-2026): Bangkok (4 Nights with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BANGKOK & LUXURY RIVER DINNER CRUISE', 1),
            _ih('Day 02: ICONSIAM WATERFRONT LUXURY & MAHANAKHON SKYWALK SUNSET', 2),
            _ih('Day 03: DESIGNER LABELS AT SIAM PARAGON & EMSPHERE LIFESTYLE TRAIL', 3),
            _ih('Day 04: CHATUCHAK BOHEMIAN BAZAAR & AWARD-WINNING DAY SPA RETREAT', 4),
            _ih('Day 05: BANGKOK RETREAT & DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private custom retail assistant tracks and premium sky-view', 6),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium luxury hotels located directly adjacent to main', 7),
            _ih('Personalized Assistance: English-fluent dedicated local coordinators to manage mall reservation', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BANGKOK & LUXURY RIVER DINNER CRUISE',
                (
                    'WELCOME TO THE CITY OF ANGELS – COUTURES, COCKTAILS & THE RIVER OF KINGS Your highly anticipated Bangkok Shopping Festival journey hits the runway flawlessly the moment your group lands at Bangkok’s Suvarnabhumi International Airport. Receive our elite VIP Fast-Track Reception, clearing all customs and immigration procedures within minutes via premium fast channels. Your private, elegant luxury van waits to transfer you smoothly past the city lines to your handpicked high-end central lifestyle hotel. Check into your premium rooms, featuring special welcome amenities and a chilled complimentary bottle of sparkling wine. Take the afternoon to unpack your outfits, rest, and snap your first group photos by the rooftop infinity pool. In the evening, dress in your finest attire for a classic Premium Thailand Experience: a 5-star luxury dinner cruise aboard the Grand Pearl Cruise liner on the Chao Phraya River. Glide past the brilliantly lit Grand Palace and the luminous spires of Wat Arun (The Temple of Dawn) while enjoying a sumptuous international buffet and live jazz music, capturing a beautiful opening photography point. Sightseeing Included: VIP airport fast-track reception & clearance, scenic city transfer, Chao Phraya cruising. Evening Experience: 5-Star Luxury Chao Phraya River Dinner Cruise with live jazz background entertainment.'
                ),
                [
                    'Overnight Stay: Bangkok (Ultra-Luxury Riverside or Central Lifestyle Hotel)',
                    'Meals Included: Premium Cruise Gala Buffet Dinner',
                ],
            ),
            _day(
                2,
                'ICONSIAM WATERFRONT LUXURY & MAHANAKHON SKYWALK SUNSET',
                (
                    "RETAIL OPULENCE – GLOBAL ICONIC FLAGSHIPS & GLASS TRAY SKYLINES Savor a magnificent buffet breakfast before picking out your best designer walking shoes. Today features the ultimate centerpiece of your retail itinerary: a private transfer to ICONSIAM, the crown jewel of Bangkok's local Thai crafts with multi-story flagship pavilions of the world's most elite luxury fashion houses, offering an unparalleled location for premium shopping. Find unique silk garments, custom jewelry pieces, and international high-fashion apparel collections while enjoying panoramic views of the river. At twilight, your private vehicle escorts your group to the spectacular Mahanakhon SkyWalk. Ascend to stand 314 meters above the metropolis on a massive glass tray— consistently named a top popular Instagram location. End your night with VIP tables reserved at a premium rooftop sky lounge, celebrating your friendship over delicious dining and breathtaking skyline views. Sightseeing Included: ICONSIAM Luxury Waterfront Mall, Mahanakhon SkyWalk VIP entry ticket. Evening Experience: Premium cocktails and high-fashion dining at a top-tier sky lounge overlooking the city."
                ),
                [
                    'shopping: plazas. This monumental lifestyle complex seamlessly blends an indoor floating market showcasing',
                    'Overnight Stay: Bangkok (Ultra-Luxury Riverside or Central Lifestyle Hotel)',
                    'Meals Included: International Buffet Breakfast & Rooftop Gastronomy Dinner',
                ],
            ),
            _day(
                3,
                'DESIGNER LABELS AT SIAM PARAGON & EMSPHERE LIFESTYLE TRAIL',
                (
                    "THE FASHION CORRIDOR – CENTRAL SPREE, RETRO FINDS & CHIC CAFE HOPPING Enjoy another beautiful morning breakfast before launching back into your premier shopping spree. Your private van transfers your group to the Siam District, the definitive fashion corridor of the capital. Explore the sprawling designer galleries of Siam Paragon and the trendy independent Thai label boutiques of Siam Center, mapping out the latest collections. Take a mid-day break for a custom-tailored TRAGUIN Cafe Hop, stepping into one of Bangkok's trendiest, plant-filled boutique cafes for artisan lattes and aesthetic photo opportunities. In the afternoon, cruise down Sukhumvit road to EmSphere, Bangkok's newest and most futuristic retail district. Melding industrial design with high-end global retail hubs, it is an amazing spot to track contemporary street style, avant-garde cosmetics, and luxury lifestyle accessories. In the evening, explore the lively neon-lit lanes of Jodd Fairs Night Bazaar, a fantastic spot for picking up custom graphic apparel, chic leather boots, and trendy local street snacks. Sightseeing Included: Siam Paragon, Siam Center, EmSphere Retail Quarter, Jodd Fairs Night Bazaar. Evening Experience: Boutique street fashion hunting and gourmet local food tasting at Jodd Fairs."
                ),
                [
                    'Overnight Stay: Bangkok (Ultra-Luxury Riverside or Central Lifestyle Hotel)',
                    'Meals Included: International Buffet Breakfast & Selected Designer Cafe Lunch Menu',
                ],
            ),
            _day(
                4,
                'CHATUCHAK BOHEMIAN BAZAAR & AWARD-WINNING DAY SPA RETREAT',
                (
                    "VINTAGE TREASURES, LOCAL ARTISAN CRAFTS & 120-MINUTE DEEP REJUVENATION Today combines local bohemian street shopping with ultimate body pampering. Following breakfast, your private van drops your group at the massive Chatuchak Weekend Market (or the premium indoor MBK Center/Platinum Mall if weekday traveling). Walk through thousands of bustling stalls packed with hand- woven beach dresses, vintage ceramic ornaments, local home décor pieces, and unique silver accessories, making it an unparalleled location for collecting souvenirs and authentic Thai crafts. In the afternoon, escape the vibrant market lines into an award-winning luxury wellness day spa sanctuary. TRAGUIN has reserved exclusive group slots for your ladies' circle. Indulge side-by-side in traditional Thai herbal steam rooms, organic aromatic body scrubs, and therapeutic aromatic body oil massages using premium local essential oils. For your final evening, celebrate with an elegant 3-course farewell dinner overlooking the glittering city, raised to toast an extraordinary getaway. Sightseeing Included: Chatuchak Weekend Market or Platinum Fashion Mall, Luxury Spa Sanctuary access. Evening Experience: Grand finale all-female farewell dinner party at a premium waterfront restaurant with live music."
                ),
                [
                    'Overnight Stay: Bangkok (Ultra-Luxury Riverside or Central Lifestyle Hotel)',
                    'Meals Included: International Buffet Breakfast & 3-Course Riverfront Farewell Dinner',
                ],
            ),
            _day(
                5,
                'BANGKOK RETREAT & DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER ULTRA-STYLISH Enjoy your final decadent buffet breakfast at your luxury hotel, capturing a final round of group fashion photos by the pool or across the tropical landscaped lounges. Take your time packing your shopping bags while our on-ground concierge team coordinates with hotel reception to manage your seamless checkout and handle luggage logistics. Depending on your flight departure schedule, your private luxury van remains available for last-minute boutique shopping for traditional Thai silks or premium spa oils, or a brief stop at a chic city cafe to grab a final cup of authentic Thai iced tea. Your private vehicle delivers your group safely to Suvarnabhumi International Airport for your return flight home. Your premium Bangkok Shopping Festival tour concludes beautifully, leaving your friend circle closer and more stylish than ever before, with stories crafted to perfection by TRAGUIN. Sightseeing Included: Boutique souvenir shopping access, private luxury airport departure transfer.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Sukosol Bangkok Premier Corner Room Complimentary Welcome Mocktails & Central Shopping Map Guide',
                'Multi-city Thailand',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — The Sukosol Bangkok Premier Corner Room Complimentary Welcome Mocktails & Central Shopping Map Guide',
            ),
            _hotel(
                'Grande Centre Point Terminal 21 Premium Deluxe Room Welcome Fruit Platters, Free BTS Skytrain 1-Day Pass per guest',
                'Multi-city Thailand',
                '4N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Grande Centre Point Terminal 21 Premium Deluxe Room Welcome Fruit Platters, Free BTS Skytrain 1-Day Pass per guest',
            ),
            _hotel(
                'Avani+ Riverside Bangkok Hotel Avani Panorama River Room Complimentary Floating Breakfast Setup & Rooftop Lounge Discount Vouchers',
                'Multi-city Thailand',
                '4N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Avani+ Riverside Bangkok Hotel Avani Panorama River Room Complimentary Floating Breakfast Setup & Rooftop Lounge Discoun',
            ),
            _hotel(
                'Mandarin Oriental, Bangkok / Siam Kempinski Deluxe Chao Phraya Suite / Executive Cabana Room Premium Vintage Champagne Bottle, Private Personal Shopper Lounge Access & 24/7 Butler Support',
                'Multi-city Thailand',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Mandarin Oriental, Bangkok / Siam Kempinski Deluxe Chao Phraya Suite / Executive Cabana Room Premium Vintage Champagne B',
            )
        ],
        inclusions=[
            _inc_included('Daily Meals: 4 International Buffet Breakfast layouts with wellness and fruit corners.', 1),
            _inc_included('Private Vehicles: Dedicated safe luxury van with an experienced chauffeur and extra cargo room for all tours.', 2),
            _inc_included('VIP Sightseeing: Priority fast-track ramp entry for Chao Phraya River Dinner Cruise & Mahanakhon SkyWalk.', 3),
            _inc_included('Wellness Luxury: 120-minute Premium Group Day Spa & Rejuvenating Massage session.', 4),
            _inc_included('Flights: International flight tickets connecting your home country with Bangkok.', 5),
            _inc_excluded('Accommodation: 04 Nights stay in centrally located premium luxury hotels.', 6),
            _inc_excluded('Visa Fees: Thailand Visa-on-Arrival or fast-track electronic visa processing fees.', 7),
        ],
    )
    return package, itinerary

def build_th_028(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-028'
    tour_code = 'TRG-HKT-WEL-2026'
    title = 'Phuket • Cape Panwa • Bang Tao Bay • Racha Yai Island'
    duration = '05 Nights / 06 Days'
    slug = 'th-028-phuket-cape-panwa-bang-tao-bay-racha-yai-island'
    itin_slug = 'th-028-phuket-cape-panwa-bang-tao-bay-racha-yai-island-itinerary'
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
            _ph('Serial code TH-028 | TRAGUIN tour code TRG-HKT-WEL-2026', 1),
            _ph('State / Country: Thailand | Category: Wellness Retreat / Premium Sanctuary', 2),
            _ph('Destinations: Phuket Clean Living', 3),
            _ph('Ideal for: Wellness Seekers, Couples, Families Seeking Rejuvenation', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Executive Van with Mindful Assistance / Organic Wellness Breakfast (CP) & Detox Culinary Dinners Restore absolute equilibrium to your mind, body, and soul with the definitive Best Phuke', 7),
            _ph('TRAGUIN Signature Experience: Private custom yachts and premium speed-craft charters,', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified luxury romantic resorts featuring maximum isolation,', 9),
            _ph('Personalized Assistance: English-fluent dedicated local island safety guides to manage activity', 10),
            _ph('Luxury Transportation: Elite executive vehicles equipped with specialized suspension systems,', 11)
        ],
        moods=['Luxury', 'Honeymoon', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Phuket',
        overview='TOUR OVERVIEW\nWelcome to your meticulously designed Phuket Wellness Retreat, a signature luxury holiday structured by TRAGUIN Experts for travelers who seek deep cellular rejuvenation, stress relief, and mindful restoration. Over 6 magnificent days on Thailand’s largest island, you will reside inside world-class health domains. Enjoy seamless private logistics in robust executive luxury vehicles, specialized organic farm-to-table culinary plans, and immersive holistic wellness programs. TRAGUIN Wellness Retreats • TRAGUIN Curated Experience Note: Your group’s well-being and absolute privacy are our ultimate parameters. From personalized consultations with resident Ayurvedic and traditional Thai physicians to private speed-craft sails to secluded, energy-rich island shores, every milestone is protected by our 24/7 dedicated on-ground assistance network. THE THERAPEUTIC ESSENCE OF A LUXURY PHUKET HOLIDAY Phuket has evolved far beyond a mere leisure space into the ultimate wellness capital of Southeast Asia, interweaving natural coastal energy lines with state-of-the-art holistic centers and Michelin-endorsed organic dining. Opting for a specialized wellness journey or a dedicated Phuket Honeymoon Package variant with TRAGUIN unlocks private access to hidden islands and premium healing sanctuaries. This proposal targets the most highly searched tourism keywords for Google ranking, ensuring the ultimate layout of Phuket Sightseeing wonders. Discover Top Tourist Places in Thailand: the peaceful sunrise horizons over Cape Panwa, the crystalline, energy-rich waters of Racha Yai Island, and the magnificent golden spires of Wat Chalong. It is universally recognized as the Best Time to Visit Thailand to explore popular Instagram locations for mindful reflection, indulge in a custom Thailand Family Tour centered on health, and capture deep, immersive experiences that redefine modern luxury travel. TRAGUIN Wellness Retreat Exclusives: Private health consultation on arrival, 180 minutes of medical- grade traditional Thai massage and specialized body wraps, a private yacht sunset meditation sail to Racha Island, and customized daily detox meal plans. TRAGUIN Wellness Retreats • THE THOUGHTFUL & RESTORATIVE DAY-WISE ITINERARY',
        seo_title='TH-028 | Phuket | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-028 / TRG-HKT-WEL-2026): Phuket Clean Living with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN PHUKET & HOLISTIC CONSULTATION', 1),
            _ih('Day 02: DAILY YOGA & PRIVATE CRUISE TO RACHA YAI ISLAND', 2),
            _ih('Day 03: PHUKET CULTURAL SIGHTSEEING & MEDICAL SPA ADVENTURE', 3),
            _ih('Day 04: THE MAJESTIC BIG BUDDHA & PHANG NGA BAY CANOEING', 4),
            _ih('Day 05: HOLISTIC WELLNESS IMMERSION & PRIVATE GRAND FINALE', 5),
            _ih('Day 06: PHUKET RETREAT & DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private custom yachts and premium speed-craft charters,', 7),
            _ih('Curated by TRAGUIN Experts: Safety-verified luxury romantic resorts featuring maximum isolation,', 8),
            _ih('Personalized Assistance: English-fluent dedicated local island safety guides to manage activity', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN PHUKET & HOLISTIC CONSULTATION',
                (
                    'WELCOME TO THE SANCTUARY – STEPPING INTO INDULGENCE AND RENEWAL Your life-changing Phuket Wellness Retreat journey unfolds flawlessly the moment your flight lands at Phuket International Airport. Avoid the standard crowds as a private TRAGUIN lifestyle concierge welcomes you with cold lemongrass towels and fresh coconut water, escorting you through premium lines directly to your waiting executive private luxury vehicle. Transfer smoothly along the scenic shoreline to your ultra-luxury health resort tucked inside Cape Panwa. Check into your sea-view villa, detailed with custom aromatherapy diffusers and organic welcome teas. In the afternoon, take part in your private wellness assessment with the resort’s resident holistic physician. Map out your specialized therapies and select your organic detox meal tracks. End your opening evening with a gentle sunset beach walk followed by a curated organic welcome dinner served on an open-air oceanfront pavilion. Sightseeing Included: Private premium airport-to-sanctuary transfer, Cape Panwa coastal path orientation. Evening Experience: Mindful beach walk followed by a starlit welcome dinner featuring organic ingredients. TRAGUIN Wellness Retreats •'
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Wellness Resort & Sanctuary)',
                    'Meals Included: Curated Organic Farm-to-Table Welcome Dinner',
                ],
            ),
            _day(
                2,
                'DAILY YOGA & PRIVATE CRUISE TO RACHA YAI ISLAND',
                (
                    "SOUND HEALING, CRYSTAL WATERS & SUNSET MINDFULNESS SAILING Wake up to a crisp morning over the ocean and gather at the beachfront pavilion for a guided sunrise yoga and Tibetan sound bowl meditation session. Following a nutritious breakfast rich in superfoods, embark on a flagship marine trip: an exclusive private speed-craft cruise to Racha Yai Island, celebrated for its pure turquoise waters and highly searched diving reef zones. Swim and snorkel hand-in-hand through the clear water among vibrant marine ecosystems, absorbing the natural energy of the Andaman Sea. Savor a magnificent gourmet wellness lunch prepared fresh by a personal crew on a secluded sandshore, capturing beautiful photography points for your journal. In the late afternoon, enjoy an onboard sunset mindfulness meditation session as your yacht glides home under a golden sky. Sightseeing Included: Racha Yai Island marine access, private speedboat cruise, coral reef snorkeling. Optional Activities: Professional underwater couples' photography session or private sea-kayaking through hidden bays. TRAGUIN Wellness Retreats •"
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Wellness Resort & Sanctuary)',
                    'Meals Included: Organic Wellness Breakfast & Island Beachfront Gourmet Picnic Lunch',
                ],
            ),
            _day(
                3,
                'PHUKET CULTURAL SIGHTSEEING & MEDICAL SPA ADVENTURE',
                (
                    'WAT CHALONG SPIRITUALITY, HERITAGE QUARTERS & DETOXBODY WRAPS Savor a beautiful morning breakfast before launching into a slow-paced Phuket Sightseeing cultural day. Your private chauffeur navigates your group to Wat Chalong, Phuket’s most revered Buddhist monastery, adorned with intricate golden filigree. Walk around the historic temple complex to appreciate Lanna architectural concepts and learn about ancient meditation systems. In the afternoon, your private vehicle heads into Old Phuket Town. Walk past beautifully preserved Sino- Portuguese colonial mansions, vibrant street murals, and charming independent herb boutiques. Return to the resort for an intense medical-grade spa experience: a 120-minute traditional Thai massage followed by a therapeutic volcanic clay detox body wrap side-by-side, leaving your body fully refreshed. Sightseeing Included: Wat Chalong Temple tour, Old Phuket Town Heritage District, Karon Viewpoint. Evening Experience: Resting at a quiet, plant-filled boutique cafe sampling local organic herbal tea blends.'
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Wellness Resort & Sanctuary)',
                    'Meals Included: Organic Wellness Breakfast & Local Thai Fine Dining Lunch',
                ],
            ),
            _day(
                4,
                'THE MAJESTIC BIG BUDDHA & PHANG NGA BAY CANOEING',
                (
                    '360-DEGREE VIEWPOINT PANORAMAS & MYSTICAL HONG ISLAND CAVES Dedicate your morning to deep geological exploration and spectacular landscapes. After a beachside breathing workshop, drive up the Nakkerd Hills to stand at the base of the majestic 45-meter Big Buddha monument—consistently named a top popular Instagram location. The peak offers a staggering 360-degree panorama over Chalong Bay, perfect for a high-fashion group photography session. In the afternoon, transfer to the northern pier where a premium speed-craft takes your group across Phang Nga Bay. Pilot stable sea canoes guided through the mystical sea caves and hidden mangrove lagoons of Koh Hong, completely enclosed by massive vertical limestone walls. Savor a fresh vegetarian buffet lunch at the stilted floating village of Koh Panyee before returning to the resort base. Sightseeing Included: The Big Buddha, Phang Nga Bay speed-craft transit, Koh Hong sea cave canoeing, Koh Panyee. Optional Activities: A private helicopter flight over the limestone karsts of the bay for an incredible birds-eye view. TRAGUIN Wellness Retreats •'
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Wellness Resort & Sanctuary)',
                    'Meals Included: Organic Wellness Breakfast & Koh Panyee Healthy Seafood Lunch',
                ],
            ),
            _day(
                5,
                'HOLISTIC WELLNESS IMMERSION & PRIVATE GRAND FINALE',
                (
                    "HYDROTHERAPY LABYRINTHS & A SIGNATURE BEACH COVE CANDLELIGHT CELEBRATION Dedicate today to complete personalized rest and fluid hydro-healing. Start your morning with a beautiful premium floating breakfast served right inside your private infinity pool villa. Spend your day navigating the resort's thermal hydrotherapy labyrinths, steam caves, and cold-plunge pools under expert guidance, finalizing your wellness tracks. Return to your villa to refresh for your final night. TRAGUIN has arranged our ultimate signature romantic highlight: an intimate, completely private beachfront candlelight dinner set in a secluded cove of the resort. Toast your wellness holiday with a glass of organic fine wine under a starlit sky as gentle waves roll in, celebrating a collection of unforgettable memories. Sightseeing Included: Thermal Hydrotherapy Park access, private beach cove reservation. Evening Experience: Signature TRAGUIN Grand Finale Private Beachfront Candlelight Dinner under the stars."
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Wellness Resort & Sanctuary)',
                    'Meals Included: Premium Floating Breakfast & Ultra-Luxury Beachside 5-Course Dinner',
                ],
            ),
            _day(
                6,
                'PHUKET RETREAT & DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER ALIGNED Savor your final morning wellness breakfast at your villa veranda, taking a final round of group photos across the tropical landscaped gardens. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless checkout and handle luggage logistics. Depending on your flight departure schedule, your private vehicle remains available for last-minute boutique seaside cafe. Your private vehicle delivers your group safely back to Phuket International Airport, where our staff assists with premium check-in. Your premium tour concludes beautifully, leaving your bodies fully refreshed and aligned, with stories crafted to perfection by TRAGUIN. Sightseeing Included: Central Phuket Floresta shopping access, private luxury airport departure transfer. TRAGUIN Wellness Retreats •'
                ),
                [
                    'shopping: for traditional Thai silk items or organic essential oils at Central Phuket Floresta, or a brief stop at a',
                    'Meals Included: Organic Wellness Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Amatara Welleisure Resort Bay View Suite Complimentary Physical Consultation & 1 Signature Hammam Voucher',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Amatara Welleisure Resort Bay View Suite Complimentary Physical Consultation & 1 Signature Hammam Voucher',
            ),
            _hotel(
                'The Slate Phuket (Nai Yang) Pearl Bed Suite Welcome Fruit Basket, Free Coqoon Spa Ritual & Yoga Access',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — The Slate Phuket (Nai Yang) Pearl Bed Suite Welcome Fruit Basket, Free Coqoon Spa Ritual & Yoga Access',
            ),
            _hotel(
                'Banyan Tree Phuket (Laguna) Banyan Pool Villa Complimentary Floating Breakfast Setup & Daily In- Villa Well-Being Activities',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Banyan Tree Phuket (Laguna) Banyan Pool Villa Complimentary Floating Breakfast Setup & Daily In- Villa Well-Being Activi',
            ),
            _hotel(
                'Amanpuri Phuket / Thanyapura Wellness Ocean View Pavilion / Pool Villa Premium Vintage Champagne Bottle, Private Personal Trainer & 24/7 Butler Care',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Amanpuri Phuket / Thanyapura Wellness Ocean View Pavilion / Pool Villa Premium Vintage Champagne Bottle, Private Persona',
            )
        ],
        inclusions=[
            _inc_included('Daily Meals: 5 Organic Wellness Breakfast layouts and specialized detox dinners.', 1),
            _inc_included('Private Vehicles: Private air-conditioned luxury van with an experienced driver for all transfers.', 2),
            _inc_included('Phuket Cruise: Private Speedboat Charter to Racha Yai Island with onboard lunch.', 3),
            _inc_included('Bay Excursion: Premium Speed-craft tour to James Bond Island with sea canoeing & lunch.', 4),
            _inc_included('Medical Spa: Included 180-minute total body therapeutic wrap and traditional Thai massage.', 5),
            _inc_included('Airfare: International and main flight tickets connecting home country with Phuket.', 6),
            _inc_excluded('Accommodation: 05 Nights stay in handpicked premium wellness resorts.', 7),
            _inc_excluded('Visa Fees: Thailand Visa-on-Arrival or fast-track electronic visa processing fees.', 8),
            _inc_excluded('National Park Entry: Island marine conservation park entry fees (payable directly on site).', 9),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, mini-bar billing, and tips.', 10),
            _inc_excluded('Extra Medical: Individual diagnostic blood profiling or private health checks outside program.', 11),
        ],
    )
    return package, itinerary

def build_th_029(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-029'
    tour_code = 'TRG-CEI-ADV-2026-V29'
    title = 'Chiang Rai • The Golden Triangle • Mekong River • Doi Mae Salong • Khun Korn Waterfall'
    duration = '05 Nights / 06 Days'
    slug = 'th-029-chiang-rai-the-golden-triangle-mekong-river-doi-mae-salong-khun-korn-waterfall'
    itin_slug = 'th-029-chiang-rai-the-golden-triangle-mekong-river-doi-mae-salong-khun-korn-waterfall-itinerary'
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
            _ph('Serial code TH-029 | TRAGUIN tour code TRG-CEI-ADV-2026-V29', 1),
            _ph('State / Country: Thailand | Category: Chiang Rai Adventure Tour', 2),
            _ph('Destinations: Chiang Rai Highland', 3),
            _ph('Ideal for: Active Families, Thrill Seekers, Nature Explorers', 4),
            _ph('Best season: October to March (Cool, Mist-Kissed Mountain Weather)', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury 4x4 SUV / Executive Commuter Van / Buffet Breakfast (CP), Jungle Barbecues & Mountain-View Dinners Unleash your untamed spirit of exploration with the Best Chiang Rai Tour Package, mast', 7),
            _ph('TRAGUIN Signature Experience: Private custom river longtails and off-road 4x4 SUVs, completely', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium adventure resorts featuring private', 9),
            _ph('Personalized Assistance: English-fluent dedicated local mountain guides to manage activity priorities,', 10),
            _ph('Luxury Transportation: Executive modern vehicles equipped with specialized suspension systems,', 11)
        ],
        moods=['Adventure', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Chiang Rai',
        overview="xciting 1.4-kilometer jungle trek along a winding river trail surrounded by massive bamboo trees and exotic wild orchids, mapping animal behavior and tropical geography. Arrive at the spectacular Khun Korn Waterfall, Krabi-style vertical rock faces where a dramatic 70-meter freshwater cascade plunges into a natural pool. Swim inside the refreshing mountain water before heading to the Kok River pier. Board a private, traditional bamboo raft guided by local river masters to glide down the rapids, experiencing a thrilling and unforgettable adventure. Return to the resort for an evening of absolute relaxation. Sightseeing Included: Khun Korn jungle trek, waterfall swimming access, private Kok River bamboo rafting. Optional Activities: A therapeutic 90-minute muscle relaxation oil massage at the resort's premium spa pavilion. Overnight Stay: Chiang Rai (Premium Luxury Valley Resort) Meals Included: International Buffet Breakfast & Premium Jungle Picnic Lunch TRAGUIN Adventure Expeditions •\n\nTOUR OVERVIEW\nWelcome to your meticulously designed Chiang Rai Adventure blueprint, an elite 6-day active vacation structured by TRAGUIN Experts for travelers who reject conventional tourist tracks. Your expedition group will navigate the winding ridges of the Golden Triangle, trek through dense bamboo jungles to roaring TRAGUIN Adventure Expeditions • cascades, cruise the legendary Mekong River channels, and explore surreal, world-famous architectural temples. Enjoy seamless private logistics in robust 4x4 luxury SUVs and executive mountain vehicles. TRAGUIN Curated Experience Note: Your group's safety and premium comfort remain our absolute operational benchmarks. This active itinerary includes dedicated local safety marshals, professional mountain guides, fast-track entry into national parks, pre-vetted family dining paths, and senior local managers providing 24/7 dedicated on-ground personal assistance. THE THRILL OF A PREMIUM CHIANG RAI EXPERIENCE Chiang Rai’s mountain geography is an absolute masterpiece of nature, drawing outdoor enthusiasts globally to its jagged jungle ridges, roaring waterfalls, and misty tea plantations. Choosing a specialized Chiang Rai Family Tour or an active Chiang Rai Honeymoon Package configured by TRAGUIN ensures an extraordinary holiday far superior to generic public group tours. This proposal optimizes top searched keywords for Google ranking, laying out an exceptional overview of premier Chiang Rai Sightseeing marvels. Explore the region's most coveted highlights: the surreal glass filigree of the iconic White Temple, the sapphire depths of the Blue Temple, the roaring drops of Khun Korn Waterfall, and the three-border panorama of the Golden Triangle. It is widely recognized as the Best Time to Visit Thailand to discover popular Instagram locations from a unique vantage point on the water, try authentic local hill-tribe coffee, explore bamboo forest tracks, and collect deep, immersive experiences that define high-end travel. TRAGUIN Adventure Signatures: Private longtail boat cruise on the Mekong River at the Golden Triangle, private off-road 4x4 SUV expedition to Doi Mae Salong tea mountains, private bamboo rafting on the Kok River, and an exclusive grand finale mountain-view dinner party. TRAGUIN Adventure Expeditions • THE HIGH-OCTANE DAY-WISE ITINERARY",
        seo_title='TH-029 | Chiang Rai | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-029 / TRG-CEI-ADV-2026-V29): Chiang Rai Highland with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN CHIANG RAI & SCENIC HIGHLAND ORIENTATION', 1),
            _ih('Day 02: SURREAL WHITE TEMPLE, BLUE TEMPLE & BLACK HOUSE ARCHITECTURE', 2),
            _ih('Day 03: KHUN KORN JUNGLE TREK & KOK RIVER BAMBOO RAFTING', 3),
            _ih('Day 04: THE GOLDEN TRIANGLE EXPEDITION & MEKONG CRUISE', 4),
            _ih('Day 05: OFF-ROAD SUV DRIVE TO DOI MAE SALONG TEA VILLAGE', 5),
            _ih('Day 06: CHIANG RAI RETREAT & DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private custom river longtails and off-road 4x4 SUVs, completely', 7),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium adventure resorts featuring private', 8),
            _ih('Personalized Assistance: English-fluent dedicated local mountain guides to manage activity priorities,', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN CHIANG RAI & SCENIC HIGHLAND ORIENTATION',
                (
                    'WELCOME TO THE JUNGLE BASE – THE NORTHERN EXPEDITION COMMENCES Your spectacular Chiang Rai Adventure hits the ground running the moment your group touches down at Chiang Rai International Airport (Mae Fah Luang). Clear the arrival gates to receive a premium welcome from your dedicated TRAGUIN tour representative. Avoid the hassle of generic public transport lines as you step directly into your private, robust luxury 4x4 SUV or executive van, engineered for maximum comfort across mountain tracks. Transfer to your handpicked premium resort nestled inside a lush valley and check into your mountain-facing suite. Take the afternoon to unpack your gear, relax, and capture your first group photos by the infinity pool overlooking the misty hills. In the evening, your private vehicle transfers the group to an upscale restaurant for a welcome dinner filled with local delicacies and international favorites, establishing an inspiring initial networking forum for an unforgettable luxury vacation. Sightseeing Included: Private luxury vehicle airport transfer, scenic highland driving layout, night bazaar orientation walk. Evening Experience: Welcome dinner party at an upscale valley-view restaurant with gorgeous panorama TRAGUIN Adventure Expeditions •'
                ),
                [
                    'photography points: .',
                    'Overnight Stay: Chiang Rai (Premium Luxury Valley Resort)',
                    'Meals Included: Curated Northern Thai Welcome Dinner',
                ],
            ),
            _day(
                2,
                'SURREAL WHITE TEMPLE, BLUE TEMPLE & BLACK HOUSE ARCHITECTURE',
                (
                    'THE ARTISTIC TRIANGLE – ICONSIAM-STYLE DESIGN CRAFTS & VISUAL SPECTACLES Savor a magnificent buffet breakfast before picking out your best outfits. Today features a primary cornerstone of your Chiang Rai Sightseeing itinerary: an architectural masterclass. Your private chauffeur navigates your group to the world-famous Wat Rong Khun (The White Temple), a monumental masterpiece designed entirely in pure white glass filigree, creating a spectacular background for iconic group portraits. Next, visit the surreal Wat Rong Suea Ten (The Blue Temple) to admire its brilliant sapphire interiors and towering white Buddha statue. Following a gourmet lunch at a riverside bistro, explore the mysterious Baandam Museum (The Black House), a collection of 40 dark teak structures displaying local avant-garde art and bone carvings. This complex stands as an incredible popular Instagram location, perfect for capturing deep cultural milestones wrapped in premium travel. Sightseeing Included: The White Temple, The Blue Temple, Baandam Black House entry tickets. Evening Experience: Relaxing walk through the clock tower square followed by artisan coffee-tasting at a boutique cafe. TRAGUIN Adventure Expeditions •'
                ),
                [
                    'Overnight Stay: Chiang Rai (Premium Luxury Valley Resort)',
                    'Meals Included: International Buffet Breakfast & Riverside Bistro Lunch',
                ],
            ),
            _day(
                3,
                'KHUN KORN JUNGLE TREK & KOK RIVER BAMBOO RAFTING',
                (
                    "DEEP JUNGLE ADVENTURE – BAMBOO FOREST TRAILS & HIGH-ADRENALINE MARINE ATHLETICS Fuel up with a hearty breakfast layout before putting on your hiking gear. Today, TRAGUIN drops you straight into the heart of the wild Northern mountains. Drive to the Khun Korn Forest Park and embark on an exciting 1.4-kilometer jungle trek along a winding river trail surrounded by massive bamboo trees and exotic wild orchids, mapping animal behavior and tropical geography. Arrive at the spectacular Khun Korn Waterfall, Krabi-style vertical rock faces where a dramatic 70-meter freshwater cascade plunges into a natural pool. Swim inside the refreshing mountain water before heading to the Kok River pier. Board a private, traditional bamboo raft guided by local river masters to glide down the rapids, experiencing a thrilling and unforgettable adventure. Return to the resort for an evening of absolute relaxation. Sightseeing Included: Khun Korn jungle trek, waterfall swimming access, private Kok River bamboo rafting. Optional Activities: A therapeutic 90-minute muscle relaxation oil massage at the resort's premium spa pavilion. TRAGUIN Adventure Expeditions •"
                ),
                [
                    'Overnight Stay: Chiang Rai (Premium Luxury Valley Resort)',
                    'Meals Included: International Buffet Breakfast & Premium Jungle Picnic Lunch',
                ],
            ),
            _day(
                4,
                'THE GOLDEN TRIANGLE EXPEDITION & MEKONG CRUISE',
                (
                    'THREE-BORDER HORIZONS – SECLUDED WATERWAYS & THE OPIUM MUSEUM LESSONS Gear up for an iconic highlight of your Best Chiang Rai Tour Package. Following breakfast, your private luxury SUV transfers you north to Chiang Saen to the historic Golden Triangle—the mystical geographical node where the borders of Thailand, Laos, and Myanmar intersect along the Mekong River. It stands as a premier attraction and a top tourist place in Thailand. Avoid all crowded commercial passenger tour boats as TRAGUIN books an exclusive private longtail speed- craft charter. Cruise gently along the wide channels of the Mekong River, capturing unique photographs facing the borders. Disembark to explore the world-class House of Opium Museum, an interactive learning center tracing the deep history of the region. Return past local night markets to stock up on handcrafted wooden souvenirs and silk fabrics. Sightseeing Included: Golden Triangle viewpoint, private Mekong River cruise, House of Opium Museum entry ticket. Optional Activities: A short boat landing at Don Sao Island (Laos border zone) for authentic local market exploration. TRAGUIN Adventure Expeditions •'
                ),
                [
                    'Overnight Stay: Chiang Rai (Premium Luxury Valley Resort)',
                    'Meals Included: International Buffet Breakfast & Local Mekong Riverside Lunch',
                ],
            ),
            _day(
                5,
                'OFF-ROAD SUV DRIVE TO DOI MAE SALONG TEA VILLAGE',
                (
                    'MISTY TEA RIDGE TRAILS, CHINESE HERITAGE & PRIVATE GALA FINALE Dedicate today to high-altitude exploration and our crowning signature surprise. Following breakfast, your private 4x4 SUV scales the winding, scenic roads up to Doi Mae Salong, a spectacular high-mountain settlement settled by Chinese soldiers. Drive past endless green tea plantations terraced neatly along sharp ridges—consistently ranked among the most beautiful landscapes in Northern Thailand. Walk hand-in-hand through the tea fields to participate in an authentic oolong tea-tasting ceremony at a high- end plantation kiosk. For your final evening, return to the resort valley where TRAGUIN has arranged our ultimate signature highlight: an intimate, completely private candlelight dinner party set on an open-air riverfront lawn. Toast your adventure holiday with a glass of fine wine under a starlit sky as local acoustic music plays softly. Sightseeing Included: Doi Mae Salong mountain driving tour, terraced tea plantation access, tea-tasting workshop. Evening Experience: Signature TRAGUIN Grand Finale Private Candlelight Dinner under the stars with live music blocks. Dinner'
                ),
                [
                    'Overnight Stay: Chiang Rai (Premium Luxury Valley Resort)',
                    'Meals Included: International Buffet Breakfast & Yunnanese Hill-Top Lunch Array & 5-Course Gala Finale',
                ],
            ),
            _day(
                6,
                'CHIANG RAI RETREAT & DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER FEARLESS Savor your final morning breakfast at your premium resort, capturing a final round of group family photos across the tropical landscaped gardens. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless checkout and handle luggage logistics. Depending on your flight departure schedule, your private vehicle remains available for last-minute boutique cafe to grab an authentic Thai iced tea. Your private vehicle delivers your group safely back to Chiang Rai International Airport for your departure flight back home. Your premium Chiang Rai Adventure tour concludes beautifully, leaving you inspired and forever fearless. Sightseeing Included: Boutique souvenir shopping trail, private luxury airport transfer. TRAGUIN Adventure Expeditions •'
                ),
                [
                    'shopping: for local hill-tribe embroidered apparel or premium organic tea leaves, or a brief stop at a riverside',
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Chiang Rai Highland',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: TRAGUIN Handpicked Deluxe Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Chiang Rai Highland',
                '5N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: TRAGUIN Handpicked Premium Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Luxury Property',
                'Chiang Rai Highland',
                '5N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Chiang Rai Highland',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included('Daily Meals: 5 International Buffet Breakfast layouts, 4 Mountain Lunches, 2 Curated Dinners.', 1),
            _inc_included('Private Vehicles: Private air-conditioned luxury 4x4 SUV or van for all transfers and tours.', 2),
            _inc_included('Bespoke River Charters: Private Mekong River longtail boat cruise and private Kok River bamboo rafting.', 3),
            _inc_included('Admissions Included: Entry tickets to White Temple, Blue Temple, Opium Museum, and Khun Korn Park.', 4),
            _inc_included('International Flights: Main airline tickets connecting home country with Thailand.', 5),
            _inc_excluded('Accommodation: 05 Nights stay in handpicked premium adventure hotels.', 6),
            _inc_excluded('Domestic Flights: Internal airfare connecting Bangkok with Chiang Rai airport.', 7),
            _inc_excluded('Visa Fees: Thailand Visa-on-Arrival or fast-track electronic visa processing fees.', 8),
        ],
    )
    return package, itinerary

def build_th_030(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-030'
    tour_code = 'TRG-THA-ULT-2026'
    title = 'THAILAND TOUR Bangkok • Phuket • Phi Phi Islands • Phang Nga Bay • Krabi'
    duration = '08 Nights / 09 Days'
    slug = 'th-030-thailand-tour-bangkok-phuket-phi-phi-islands-phang-nga-bay-krabi'
    itin_slug = 'th-030-thailand-tour-bangkok-phuket-phi-phi-islands-phang-nga-bay-krabi-itinerary'
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
            _ph('Serial code TH-030 | TRAGUIN tour code TRG-THA-ULT-2026', 1),
            _ph('State / Country: Thailand | Category: Ultimate Luxury Holiday', 2),
            _ph('Destinations: Bangkok (3N) + Phuket', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Chauffeur- Driven Luxury Sedans & Executive Vans / Bespoke Floating Breakfasts, Michelin Dining & Sunset Galas', 7),
            _ph('TRAGUIN Signature Experience: Private custom yachts and premium river cruises, completely', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium luxury resorts featuring maximum isolation,', 9),
            _ph('Personalized Assistance: English-fluent dedicated local island guides to manage reservation priorities', 10),
            _ph('Luxury Transportation: Elite executive vehicles equipped with specialized suspension systems,', 11)
        ],
        moods=['Luxury', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='THAILAND TOUR Bangkok',
        overview="pic voyage of opulence with the Best Thailand Tour Package, curated exclusively by TRAGUIN to unite the high-fashion metropolitan energy of Bangkok, the azure island serenity of Phuket, and the limestone majesty of Krabi. This definitive Luxury Thailand Holiday uncovers breathtaking landscapes, places you inside handpicked hotels of worldwide distinction, and crafts unforgettable memories.\n\nTOUR OVERVIEW\nWelcome to your bespoke Ultimate Thailand adventure, a comprehensive luxury experience designed for guests who command seamless operational perfection, absolute private security, and elite lifestyle inclusions. Across 9 spectacular days, TRAGUIN brings you a flawless mix of urban glamour, private marine yachting, and total rejuvenation within premier retreats. TRAGUIN Curated Experience Note: Every phase of your holiday is actively managed by our luxury concierge desk. From pre-allocated fast-track airport arrivals to personalized chef-driven dining tracks and custom multi-destination logistics, we ensure every detail of your journey is flawlessly immersive.\n\nWHY CHOOSE OUR ULTIMATE THAILAND LUXURY PACKAGE?\nThailand remains an international masterpiece of luxury travel, effortlessly combining ancient royal heritage with ultra-modern private estates and Michelin-starred culinary landscapes. Selecting one of our signature TRAGUIN Thailand Packages or an elite Thailand Honeymoon Package guarantees access to hidden domains and priority privileges. This proposal utilizes top searched keywords for Google ranking, showcasing an elite layout of premier Thailand Sightseeing marvels. Uncover legendary attractions: the historical grandeur of Bangkok's Grand Palace, the breathtaking emerald lagoons of the Phi Phi Islands, the sheer vertical limestone monuments of Krabi’s Railay Beach, and the high- fashion retail centers of the capital. It is widely recognized as the Best Time to Visit Thailand to experience highly sought-after popular Instagram locations, authentic local crafts, world-class wellness therapies, and collect deep, immersive experiences that redefine the modern Premium Thailand Experience. TRAGUIN Ultimate Retreat Signatures: VIP fast-track airport arrivals in Bangkok, private luxury yacht charter to Phi Phi Islands, an exclusive 180-minute couple's spa rejuvenation, and a grand finale beachfront candlelight gala in Krabi. THE DEFINITVE DAY-WISE ITINERARY",
        seo_title='TH-030 | THAILAND TOUR Bangkok | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days Thailand package (TH-030 / TRG-THA-ULT-2026): Bangkok (3N) + Phuket with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: BANGKOK ARRIVAL & RIVERFRONT OPULENCE', 1),
            _ih('Day 02: HERITAGE TEMPLES & ICONSIAM SHOPPING', 2),
            _ih('Day 03: BANGKOK TO PHUKET & COASTAL LUXURY', 3),
            _ih('Day 04: PRIVATE YACHT TO PHI PHI ISLANDS', 4),
            _ih('Day 05: PHANG NGA BAY & JAMES BOND ISLAND EXPEDITION', 5),
            _ih('Day 06: PHUKET TO KRABI TRANSIT & THE AONANG CLIFFS', 6),
            _ih('Day 07: KRABI 4-ISLAND EXPEDITION & GRAND FINALE', 7),
            _ih('Day 08: KRABI RETREAT & DEPARTURE', 8),
            _ih('TRAGUIN Signature Experience: Private custom yachts and premium river cruises, completely', 9),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium luxury resorts featuring maximum isolation,', 10)
        ],
        days=[
            _day(
                1,
                'BANGKOK ARRIVAL & RIVERFRONT OPULENCE',
                (
                    'THE CAPITAL WELCOME – METROPOLITAN GLAMOUR & CHAO PHRAYA TWILIGHT Your spectacular Ultimate Thailand vacation begins the moment you touch down at Bangkok International Airport. Receive our VIP Airport Fast-Track Reception, clearing all customs and immigration procedures within minutes. Your private, elegant European sedan or luxury SUV waits to transfer you smoothly along the scenic highway to your ultra-luxury riverside resort. Check into your handpicked premium riverfront room. In the evening, dress in elegant luxury wear for a classic Premium Thailand Experience: a 5-star luxury dinner cruise aboard the Grand Pearl Cruise liner on the Chao Phraya River. Glide past the brilliantly lit Grand Palace and the luminous spires of Wat Arun while enjoying a sumptuous buffet, live jazz music, and classical Thai performances, setting a stunning photography point for your opening night. Sightseeing Included: VIP airport fast-track clearance, luxury sedan city transfer, Chao Phraya dinner cruising. Evening Experience: 5-Star Luxury River Dinner Cruise with live performances.'
                ),
                [
                    'Overnight Stay: Bangkok (Ultra-Luxury Riverside Resort)',
                    'Meals Included: Premium Cruise Gala Buffet Dinner',
                ],
            ),
            _day(
                2,
                'HERITAGE TEMPLES & ICONSIAM SHOPPING',
                (
                    "SIAMESE SPLENDOR – THE GRAND PALACE & WORLD-CLASS RETAIL THERAPY Savor a magnificent buffet breakfast before embarking on a descriptive Bangkok Sightseeing cultural tour. Your private chauffeur navigates your party to the walled Grand Palace complex. Admire the golden spires and explore the sacred Temple of the Emerald Buddha, a world-famous landmark. Continue to Wat Pho to stand before the monumental 46-meter Reclining Buddha covered in gold leaf—perfect for iconic family portraits. In the afternoon, proceed to ICONSIAM, the crown jewel of Bangkok's shopping malls. Featuring an indoor floating market, massive luxury brand flagship stores, and phenomenal waterfront spaces, it is an unparalleled location for premium shopping. Find unique silk garments, boutique cosmetics, and designer items. In the evening, explore the nearby sky-lounges for cocktails overlooking the illuminated metropolitan skyline. Sightseeing Included: Grand Palace, Wat Phra Kaew, Wat Pho, ICONSIAM Luxury Waterfront Mall. Optional Activities: Mahanakhon SkyWalk glass tray adventure at 314 meters above the city skyline."
                ),
                [
                    'Overnight Stay: Bangkok (Ultra-Luxury Riverside Resort)',
                    'Meals Included: International Buffet Breakfast & Traditional Thai Fine Dining Lunch',
                ],
            ),
            _day(
                3,
                'BANGKOK TO PHUKET & COASTAL LUXURY',
                (
                    "TRANSIT TO THE PEARL OF THE ANDAMAN – TROPICAL VILLA INDULGENCE Enjoy your final Bangkok breakfast looking out over the river. Your private vehicle transfers you to the airport for your short domestic flight to Phuket. Upon arrival on Thailand's largest island, your waiting private premium vehicle provides a smooth, scenic transfer along the beautiful Andaman coastline to your handpicked, ultra-luxury pool villa resort. Phuket is globally celebrated for its breathtaking landscapes, dramatic limestone cliffs, and vibrant coastal culture, making it an essential chapter for your Luxury Thailand Holiday. Arrive at your premium villa, detailed with a chilled complimentary bottle of champagne. Spend your afternoon unwinding inside your private infinity pool or strolling along the powdery sand beaches, watching the horizon transform into a vibrant sunset tapestry. Sightseeing Included: Domestic flight transit, scenic coastal private resort transfer, beach sunset walk. Evening Experience: Private chef-prepared welcome barbecue on your villa’s sun-deck."
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Private Pool Villa Resort)',
                    'Meals Included: International Buffet Breakfast & Private Chef Villa Barbecue',
                ],
            ),
            _day(
                4,
                'PRIVATE YACHT TO PHI PHI ISLANDS',
                (
                    'CRYSTAL LAGOONS, SNORKELING ESCAPADES & MAYA BAY VIEWPOINTS Wake up to a beautiful morning and enjoy a lavish floating breakfast inside your pool villa. Today hosts an elite signature experience: a full-day private luxury yacht charter to explore the legendary Phi Phi Islands. Skip all standard public crowds as your captain steers your magnificent vessel directly toward the vertical limestone walls of Maya Bay, offering a premium photography point for your vacation. Swim and snorkel hand-in-hand in the emerald waters of Pileh Lagoon, a beautiful natural limestone basin filled with colorful marine life. Savor a premium gourmet picnic lunch specially arranged on the soft sands of Bamboo Island. Conclude your voyage cruising past the dramatic Viking Cave and Monkey Beach, toasting with fine wine as the sun dips below the horizon, providing a world-class photography point for the trip. Sightseeing Included: Private Yacht cruise, Maya Bay entry, Pileh Lagoon swimming, Bamboo Island beach access, Viking Cave view. Optional Activities: Tandem deep-sea scuba diving under PADI guidance or sea-kayaking through hidden coves.'
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Private Pool Villa Resort)',
                    'Meals Included: Bespoke Floating Villa Breakfast & Private Yacht Gourmet Picnic Lunch',
                ],
            ),
            _day(
                5,
                'PHANG NGA BAY & JAMES BOND ISLAND EXPEDITION',
                (
                    "MYSTICAL SEA LAGOONS, LIMESTONE MONOLITHS & KAYAK ADVENTURES Prepare for an awe-inspiring day exploring one of the most magnificent landscapes in Southeast Asia. After breakfast, transfer to the pier where a premium speed-craft takes your group across Phang Nga Bay. Cruise past hundreds of vertical limestone karsts rising dramatically out of the calm sea. Arrive at James Bond Island, an iconic attraction of Phuket Sightseeing, and capture fantastic pictures in front of the floating rock monolith. Next, enjoy a relaxing canoeing experience guided through the mystical sea caves and hidden mangrove lagoons of Koh Hong. Savor a fresh seafood lunch at the unique stilted floating village of Koh Panyee. Return to the resort to refresh for the evening, enjoying a therapeutic 150-minute couple's aroma-spa treatment before a relaxing cliffside dinner. Sightseeing Included: James Bond Island, Koh Hong sea cave canoeing, Koh Panyee floating village, Spa sanctuary. Optional Activities: Helicopter flight over Phang Nga Bay for an incredible birds-eye view of the landscape."
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Private Pool Villa Resort)',
                    'Meals Included: International Buffet Breakfast & Koh Panyee Seafood Lunch',
                ],
            ),
            _day(
                6,
                'PHUKET TO KRABI TRANSIT & THE AONANG CLIFFS',
                (
                    "SCENIC COASTAL DRIVE & DRAMATIC VERTICAL CLIFFS OF KRABI Following breakfast, check out of your Phuket villa. Your private luxury van picks you up for a smooth, exceptionally scenic journey past rubber plantations and coastal villages heading into Krabi. Krabi is adored globally for its staggering limestone towers rising straight from emerald waters—making it a centerpiece for any true Luxury Thailand Holiday. Arrive at your premium resort nestled adjacent to the dramatic Ao Nang cliffs. After a relaxed check-in, the afternoon is free to enjoy your resort's luxury infinity pool. As the evening sets in, your driver delivers you to the vibrant Ao Nang walking street, full of vibrant cafes, local artisan shops, and great photography opportunities along the rocky shoreline. Sightseeing Included: Cross-province scenic highway private drive, Ao Nang orientation. Evening Experience: Romantic sunset dinner at a cliffside bistro overlooking the rocky Ao Nang horizon."
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Cliffside or Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Coastal Sunset Dinner',
                ],
            ),
            _day(
                7,
                'KRABI 4-ISLAND EXPEDITION & GRAND FINALE',
                (
                    'MYSTICAL SANDBARS, CORAL REEFS & A PRIVATE BEACHFRONT CANDLELIGHT GALA Today unveils the crowning beauty of your Krabi Sightseeing itinerary. After breakfast, a private speed-craft launches directly from the resort sands for a thrilling day across Krabi’s legendary 4-Islands. Visit Phra Nang Cave Beach, renowned for its vertical rock face climbers, before speeding towards Tup Island, where a unique natural sandbar emerges at low tide, allowing your party to walk between islands on crystal water. Snorkel over the live barrier reefs of Chicken Island, surrounded by schools of tropical fish. Return to the resort to refresh for your final night. TRAGUIN has arranged our ultimate signature surprise: an intimate, completely private beachfront candlelight dinner set in a secluded cove of the resort. Toast your holiday with a glass of fine wine under a starlit sky as gentle waves roll in, creating a memory to last a lifetime. Sightseeing Included: Tup Island Sandbar walk, Chicken Island reef snorkeling, Poda Island, Phra Nang Cave. Evening Experience: Signature TRAGUIN Grand Finale Private Beachfront Candlelight Barbecue Dinner.'
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Cliffside or Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & 5-Course Private Cove Barbecue Dinner',
                ],
            ),
            _day(
                8,
                'KRABI RETREAT & DEPARTURE',
                (
                    "CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER REFRESHED Wake up to a quiet morning in beautiful Krabi, enjoying a long breakfast overlooking the tropical gardens. Take a final walk on the soft sand or relax by the resort's pool to reflect on your incredible journey. At the designated hour, your private luxury executive vehicle arrives to transfer you comfortably to Krabi International Airport for your departure flight back home. Your premium Ultimate Thailand Tour concludes beautifully, leaving your hearts full of unforgettable memories and stories crafted to perfection by TRAGUIN. Sightseeing Included: Private luxury airport departure transfer."
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Sukosol Bangkok Premier Corner Room Novotel Resort/Ao Nang Cliff Superior Ocean Suite',
                'Multi-city Thailand',
                '8N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — The Sukosol Bangkok Premier Corner Room Novotel Resort/Ao Nang Cliff Superior Ocean Suite',
            ),
            _hotel(
                'Avani+ Riverside Bangkok Avani Panorama River Room Phuket Marriott/Centara Grand Krabi Deluxe Pool View Room',
                'Multi-city Thailand',
                '8N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Avani+ Riverside Bangkok Avani Panorama River Room Phuket Marriott/Centara Grand Krabi Deluxe Pool View Room',
            ),
            _hotel(
                'Shangri-La Bangkok Deluxe Horizon River Room The Shore at Katathani/Rayavadee Pool Villa / Pavilion Suite',
                'Multi-city Thailand',
                '8N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Shangri-La Bangkok Deluxe Horizon River Room The Shore at Katathani/Rayavadee Pool Villa / Pavilion Suite',
            ),
            _hotel(
                'Mandarin Oriental, Bangkok Deluxe Chao Phraya Suite Trisara Phuket/Phulay Bay Reserve Ocean View Pool Villa',
                'Multi-city Thailand',
                '8N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Mandarin Oriental, Bangkok Deluxe Chao Phraya Suite Trisara Phuket/Phulay Bay Reserve Ocean View Pool Villa',
            )
        ],
        inclusions=[
            _inc_included('International Flights: Main airline tickets connecting home country with Thailand.', 1),
            _inc_excluded('PACKAGE INCLUSIONS', 2),
        ],
    )
    return package, itinerary

def build_th_031(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-031'
    tour_code = 'TRG-KBV-FAM-2026'
    title = 'KRABI FAMILY VACATION Ao Nang Bay • Railay Peninsula • Koh Hong Lagoons • Emerald Pool'
    duration = '05 Nights / 06 Days'
    slug = 'th-031-krabi-family-vacation-ao-nang-bay-railay-peninsula-koh-hong-lagoons-emerald-pool'
    itin_slug = 'th-031-krabi-family-vacation-ao-nang-bay-railay-peninsula-koh-hong-lagoons-emerald-pool-itinerary'
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
            _ph('Serial code TH-031 | TRAGUIN tour code TRG-KBV-FAM-2026', 1),
            _ph('State / Country: Thailand | Category: Best Krabi Family Tour Package', 2),
            _ph('Destinations: Krabi Coastal Sanctuary', 3),
            _ph('Ideal for: Families, Multi- generational Groups, Nature Enthusiasts', 4),
            _ph('Best season: November to April (Pristine Marine Visibility)', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Executive Van / Buffet Breakfast (CP), Private Island Picnics & Themed Dinners Embrace a tropical odyssey with the Best Krabi Family Tour Package, masterfully curated by TRAGUIN to perf', 7),
            _ph('TRAGUIN Signature Experience: Private custom speedboats and national park fast-track passes,', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 9),
            _ph('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 10),
            _ph('Luxury Transportation: Executive modern vehicles equipped with cooling, on-board entertainment', 11)
        ],
        moods=['Family', 'Beach', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='KRABI FAMILY VACATION Ao Nang Bay',
        overview="05 Nights / 06 Days Premium Family Adventure Holiday SERIAL CODE: TH-031 TRAGUIN TOUR CODE: TRG-KBV-FAM-2026 STATE / COUNTRY: Thailand CATEGORY: Best Krabi Family Tour Package DURATION: 05 Nights / 06 Days DESTINATIONS: Krabi Coastal Sanctuary (5 Nights) IDEAL FOR: Families, Multi- generational Groups, Nature Enthusiasts BEST SEASON: November to April (Pristine Marine Visibility) VEHICLE TYPE: Private Luxury Executive Van MEAL PLAN: Buffet Breakfast (CP), Private Island Picnics & Themed Dinners Embrace a tropical odyssey with the Best Krabi Family Tour Package, masterfully curated by TRAGUIN to perfectly bridge exhilarating marine discovery with family-oriented luxury comfort. From dramatic limestone monoliths and turquoise lagoons to handpicked premium resorts, discover breathtaking landscapes and create unforgettable memories on this premier Luxury Krabi Holiday.\n\nTOUR OVERVIEW\nWelcome to your bespoke Krabi Family Vacation, a meticulously designed holiday structured explicitly for families who command seamless coordination, children-friendly exploration paces, and elite hospitality layouts. Across 6 incredible days, your family will explore the finest islands, marine reserves, and cultural wonders of Thailand’s coastal paradise. TRAGUIN Curated Experience Note: We ensure absolute comfort at every milestone. Traveling in private, air-conditioned luxury vans with dedicated chauffeurs allows your family to completely bypass public queues. Backed by handpicked premium stays and pre-vetted family dining paths, your group will experience a flawless trip protected by our 24/7 dedicated local concierge assistance.\n\nWHY CHOOSE OUR LUXURY KRABI FAMILY VACATION?\nKrabi has evolved into the ultimate adventure and family entertainment capital of Southeast Asia, offering an unmatched variety of marine sanctuaries, emerald lagoons, and spectacular limestone coastlines. Choosing a high-end TRAGUIN Krabi Package or an exceptional Thailand Family Tour through us means stepping past generic travel routes into a world of exclusive privileges. This proposal integrates top searched tourism keywords for Google ranking, ensuring the ultimate showcase of Krabi Sightseeing wonders. Uncover iconic attractions: the world-famous sheer cliffs of Railay Beach, the crystal-clear shallow waters of the 4-Islands, the vibrant therapeutic Emerald Pool, and the historic Tiger Cave temple complex. It is universally recognized as the Best Time to Visit Thailand to explore popular Instagram locations, engage in safe children-friendly marine athletics, and collect immersive experiences that your family will cherish for a lifetime. TRAGUIN Family Signatures: Private luxury speedboat charter to Krabi's 4 Islands, front-row premium tables at theAo Nang beachside fire show, expert-led kayaking through hidden sea-caves, and dedicated private luxury van transfers. THE DEFINITVE DAY-WISE ITINERARY",
        seo_title='TH-031 | KRABI FAMILY VACATION Ao Nang Bay | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-031 / TRG-KBV-FAM-2026): Krabi Coastal Sanctuary with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN KRABI & SCENIC COASTAL WELCOME', 1),
            _ih('Day 02: PRIVATE SPEEDBOAT TO KRABI 4-ISLANDS', 2),
            _ih('Day 03: EMERALD POOLS, HOT SPRINGS & TIGER CAVE TEMPLE', 3),
            _ih('Day 04: KOH HONG ARCHIPELAGO BY PRIVATE SPEED-CRAFT', 4),
            _ih('Day 05: KRABI RETREAT & DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private custom speedboats and national park fast-track passes,', 6),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 7),
            _ih('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN KRABI & SCENIC COASTAL WELCOME',
                (
                    'WELCOME TO THE LIMESTONE PARADISE – THE FAMILY VACATION BEGINS Your spectacular Krabi Family Tour begins perfectly the moment your family arrives at Krabi International Airport. Receive a warm, traditional Thai greeting, coordinated seamlessly by your dedicated TRAGUIN tour representative. Step directly into your air-conditioned private luxury van, ensuring a completely relaxed, scenic transfer straight to your handpicked premium resort. Arrive at your premium beachfront resort and check into your spacious family suite, featuring special welcome amenities. Spend the afternoon unwinding by the panoramic swimming pool or taking your first family photos overlooking the sunset. In the evening, your private van takes you to an upscale seaside restaurant for a welcome buffet dinner filled with familiar comforts, ensuring a restful start for an unforgettable family vacation. Sightseeing Included: Private luxury van airport transit, scenic coastal drive, Ao Nang orientation. Evening Experience: Family welcome dinner at an upscale restaurant with gorgeous ocean vistas.'
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Beachfront or Cliffside Resort)',
                    'Meals Included: Curated Multi-Cuisine Family Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PRIVATE SPEEDBOAT TO KRABI 4-ISLANDS',
                (
                    'TURQUOISE LAGOONS, SNORKELING ESCAPADES & SANDBAR WALKING Wake up to a gorgeous morning over the ocean and enjoy a lavish buffet breakfast. Today hosts a cornerstone Premium Thailand Experience: an exclusive island-hopping expedition across the Andaman Sea. Avoid all crowded regular public tour boats as TRAGUIN arranges a private, high-speed luxury speedboat to pick up your family directly from the resort beachfront. Cruise over crystal-clear waters to Tup Island, where a unique natural sandbar emerges at low tide, allowing your family to walk between islands on crystal water—a perfect photography point. Snorkel over the vibrant coral reefs of Chicken Island, surrounded by schools of tropical fish. Savor a delicious fresh gourmet lunch served right on the beach at Poda Island. Spend your afternoon swimming in the warm, clear water or relaxing under the coconut trees before cruising back home. Sightseeing Included: Private Speedboat to 4-Islands, Phra Nang Cave, Tup Island Sandbar, Chicken Island reef snorkeling. Optional Activities: Exhilarating parasailing flight or private jet-ski tours around the limestone pillars.'
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Beachfront or Cliffside Resort)',
                    'Meals Included: International Buffet Breakfast & Beachside Family Island Lunch',
                ],
            ),
            _day(
                3,
                'EMERALD POOLS, HOT SPRINGS & TIGER CAVE TEMPLE',
                (
                    'JUNGLE CASCADES, THERAPEUTIC WATERS & THE MONUMENTAL PEAK CLIMB Enjoy a beautiful morning breakfast before starting a comprehensive Krabi Sightseeing natural wonder day. Your private luxury van navigates your family deep into the interior tropical rainforest of Khao Phra Bang Khram. Walk along elevated wooden pathways to the spectacular Emerald Pool (Sa Morakot), a natural freshwater basin filled with therapeutic, crystal-clear geothermal water. Swim and relax amidst the lush forest canopy. Continue to the nearby hot springs for a relaxing dip in warm volcanic mineral waters, before heading to the iconic Tiger Cave Temple. Those who enjoy an active challenge can climb the majestic stairs to the mountaintop viewpoint, capturing an incredible panoramic photography point across Krabi. Return to your resort for an evening of leisure, or explore the local night markets for handcrafted souvenirs and artisan treats. Sightseeing Included: Emerald Pool, Hot Springs nature park, Tiger Cave Temple mountaintop view. Evening Experience: Strolling down the Ao Nang walking street, sampling local street food, and shopping for artisan gifts.'
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Beachfront or Cliffside Resort)',
                    'Meals Included: International Buffet Breakfast & Healthy Jungle Bistro Lunch',
                ],
            ),
            _day(
                4,
                'KOH HONG ARCHIPELAGO BY PRIVATE SPEED-CRAFT',
                (
                    "SECRET LAGOONS, CANOEING TRAILS & SUNSET BEACHFRONT GALA Prepare for an awe-inspiring day exploring one of the most magnificent landscapes in the region. Following breakfast, board your private speed-craft to explore the Koh Hong Archipelago, a prominent highlight of Krabi Sightseeing. Skip the public crowds as your captain steers your boat through narrow rocky arches into the island's interior secret lagoon, an emerald basin completely enclosed by sheer vertical limestone walls. The children will be fully entertained exploring stable sea-canoes through hidden mangrove lagoons and snorkeling in the clear lagoon water. Land at the white sands of Hong Island to ascend the spectacular 360- degree viewpoint platform, capturing a breathtaking panorama of the bay. For your final evening, TRAGUIN has arranged our ultimate signature surprise: an intimate, completely private beachfront candlelight dinner party set in a secluded resort cove. Toast your family vacation with a glass of fine wine under a starlit sky as gentle waves roll in, creating a memory to last a lifetime. Sightseeing Included: Private Speedboat charter, Koh Hong Lagoon canoeing, 360-degree Viewpoint climb, Lading Island beach access. Optional Activities: Professional family photography session against the backdrop of the vertical limestone towers."
                ),
                [
                    'Overnight Stay: Krabi (Premium Luxury Beachfront or Cliffside Resort)',
                    'Meals Included: International Buffet Breakfast & 5-Course Beachfront Private Dinner Party',
                ],
            ),
            _day(
                5,
                'KRABI RETREAT & DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER UNITED Savor your final morning buffet breakfast overlooking the ocean, capturing a final round of group family photos across the tropical landscaped gardens. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless checkout and handle luggage logistics. At the designated hour, your private luxury van arrives to transfer your family comfortably to Krabi International Airport for your departure flight back home. Your premium Krabi Family Tour concludes beautifully, leaving your loved ones with unforgettable memories crafted to perfection by TRAGUIN. Sightseeing Included: Boutique souvenir shopping, private luxury airport departure transfer.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Ao Nang Cliff Beach Resort Ocean View Suite Complimentary Welcome Drinks & Access to Kids Activity Zone',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Ao Nang Cliff Beach Resort Ocean View Suite Complimentary Welcome Drinks & Access to Kids Activity Zone',
            ),
            _hotel(
                'Centara Grand Beach Resort Krabi Deluxe Ocean Face Room Welcome Fruit Platters, Free Kids Activity Vouchers & Water Pool Access',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Centara Grand Beach Resort Krabi Deluxe Ocean Face Room Welcome Fruit Platters, Free Kids Activity Vouchers & Water Pool',
            ),
            _hotel(
                'Rayavadee Krabi Resort Deluxe Pavilion Estate Complimentary Floating Breakfast Setup & Kids Spa Discount Vouchers',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Rayavadee Krabi Resort Deluxe Pavilion Estate Complimentary Floating Breakfast Setup & Kids Spa Discount Vouchers',
            ),
            _hotel(
                'Phulay Bay, a Ritz-Carlton Reserve Reserve Pavilion Pool Villa Premium Vintage Champagne Bottle, Private Beach Pavilion Access & 24/7 Butler Care',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Phulay Bay, a Ritz-Carlton Reserve Reserve Pavilion Pool Villa Premium Vintage Champagne Bottle, Private Beach Pavilion ',
            )
        ],
        inclusions=[
            _inc_included('Daily Meals: 5 International Buffet Breakfast layouts with children-friendly sections.', 1),
            _inc_included('Private Vehicles: Private air-conditioned luxury van with an experienced driver for all transfers.', 2),
            _inc_included('Krabi Cruise: Private Speedboat to 4-Islands with parasailing and banana boat rides.', 3),
            _inc_included('Marine Excursion: Private speed-craft charter for Koh Hong Archipelago with 360 viewpoint access.', 4),
            _inc_included('Special Dining: 1 Signature Grand Finale Private Beachfront Candlelight Barbecue Dinner.', 5),
            _inc_included('Flights: International flight tickets from your home country to Krabi.', 6),
            _inc_excluded('Accommodation: 05 Nights stay in handpicked premium family resorts.', 7),
            _inc_excluded('Visa Fees: Thailand Visa-on-Arrival or fast-track electronic visa processing fees.', 8),
            _inc_excluded('National Park Entry: Island marine conservation park entry fees (payable directly on site).', 9),
        ],
    )
    return package, itinerary

def build_th_032(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-032'
    tour_code = 'TRG-HKT-PHI-FAM-2026'
    title = 'PHUKET PHI PHI ISLANDS FAMILY TOUR Phuket • Patong Beach • Phi Phi Islands • Maya Bay • James Bond Island'
    duration = '05 Nights / 06 Days'
    slug = 'th-032-phuket-phi-phi-islands-family-tour-phuket-patong-beach-phi-phi-islands-maya-bay-james-bond-island'
    itin_slug = 'th-032-phuket-phi-phi-islands-family-tour-phuket-patong-beach-phi-phi-islands-maya-bay-james-bond-island-itinerary'
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
            _ph('Serial code TH-032 | TRAGUIN tour code TRG-HKT-PHI-FAM-2026', 1),
            _ph('State / Country: Thailand | Category: Phuket Phi Phi Islands Family Tour', 2),
            _ph('Destinations: Phuket Island Base (5', 3),
            _ph('Ideal for: Families, Ocean Explorers, Multi- generational Groups', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van (Toyota Commuter Executive) / Buffet Breakfast (CP), Private Island Picnics & Fine Seafood Dinners', 7),
            _ph('TRAGUIN Signature Experience: Private custom speedboats and theater fast-track passes, avoiding', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 9),
            _ph('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 10),
            _ph('Luxury Transportation: Executive modern vehicles equipped with cooling, on-board entertainment', 11)
        ],
        moods=['Family', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='PHUKET PHI PHI ISLANDS FAMILY TOUR Phuket',
        overview="Phuket • Patong Beach • Phi Phi Islands • Maya Bay • James Bond Island 05 Nights / 06 Days Premium Family Tour Vacation SERIAL CODE: TH-032 TRAGUIN TOUR CODE: TRG-HKT-PHI- FAM-2026 STATE / COUNTRY: Thailand CATEGORY: Phuket Phi Phi Islands Family Tour DURATION: 05 Nights / 06 Days DESTINATIONS: Phuket Island Base (5 Nights Premium Family Stay) IDEAL FOR: Families, Ocean Explorers, Multi- generational Groups BEST SEASON: November to May (Ideal Marine Visibility) VEHICLE TYPE: Private Luxury Van (Toyota Commuter Executive) MEAL PLAN: Buffet Breakfast (CP), Private Island Picnics & Fine Seafood Dinners Embark on a magnificent tropical odyssey with the Best Phuket Tour Package, meticulously curated by TRAGUIN to seamlessly blend high-adventure island hopping with refined family relaxation. Immerse your loved ones in the breathtaking landscapes of the Phi Phi Islands, discover iconic architectural treasures, and create unforgettable memories on a truly premium Luxury Phuket Holiday.\n\nTOUR OVERVIEW\nWelcome to your bespoke Phuket Phi Phi Islands Family Tour, a meticulously designed vacation structured explicitly for families who command seamless coordination, children-friendly exploration paces, and elite hospitality layouts. Across 6 wonderful days, your family will explore the finest marine sanctuaries, private yacht routes, and majestic cultural wonders of Thailand's island heart. TRAGUIN Curated Experience Note: We ensure absolute comfort at every milestone. Traveling in private, air-conditioned luxury vans with dedicated chauffeurs allows your family to completely bypass all public transport lines. Backed by handpicked premium stays and pre-vetted family dining paths, your group will experience a flawless trip protected by our 24/7 dedicated local concierge assistance. THE MAGIC OF OUR LUXURY PHUKET PHI PHI FAMILY VACATION Phuket and the surrounding Phi Phi archipelagos stand as the world's most iconic tropical sanctuary, effortlessly blending ivory white-sand coves, towering limestone monoliths, and high-fashion seaside leisure. Selecting one of our high-end TRAGUIN Phuket Packages or a specialized Thailand Family Tour means stepping past generic travel routes into a world of exclusive benefits. This proposal targets top searched tourism keywords for Google ranking, ensuring the ultimate showcase of Phuket Sightseeing wonders. Discover Top Tourist Places in Thailand: the crystal emerald lagoons of Maya Bay, the iconic dramatic vertical rock faces of the Phi Phi Islands, and the historic cultural charm of Old Phuket Town. It is universally recognized as the Best Time to Visit Thailand to explore popular Instagram locations, engage in safe children-friendly marine athletics, and collect immersive experiences that your family will cherish for a lifetime. TRAGUIN Family Signatures: Private luxury speedboat charter to the Phi Phi Islands, premium front-row tables at beachside fire-show galas, private guided tours of James Bond Island, and dedicated luxury van transfers. THE DEFINITIVE DAY-WISE ITINERARY",
        seo_title='TH-032 | PHUKET PHI PHI ISLANDS FAMILY TOUR Phuket | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-032 / TRG-HKT-PHI-FAM-2026): Phuket Island Base (5 with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN PHUKET & SUNSET BEACHFRONT WELCOME', 1),
            _ih('Day 02: PRIVATE LUXURY SPEEDBOAT TO PHI PHI ISLANDS', 2),
            _ih('Day 03: PHANG NGA BAY & JAMES BOND ISLAND EXPEDITION', 3),
            _ih('Day 04: PHUKET CULTURAL TOUR & SIMON CABARET GLAMOUR', 4),
            _ih('Day 05: LEISURE & GRAND BEACHFRONT FINALE', 5),
            _ih('Day 06: PHUKET DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private custom speedboats and theater fast-track passes, avoiding', 7),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 8),
            _ih('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN PHUKET & SUNSET BEACHFRONT WELCOME',
                (
                    'WELCOME TO THE PEARL OF THE ANDAMAN – THE FAMILY TROPICAL HOLIDAY BEGINS Your spectacular Phuket Phi Phi Islands Family Tour begins perfectly the moment your family lands at Phuket International Airport. As you emerge from the arrival gates, a warm, traditional Thai greeting awaits your party, coordinated seamlessly by your dedicated TRAGUIN tour representative. You will be escorted to your air-conditioned private luxury van, ensuring a completely relaxed, scenic coastal transfer straight to your handpicked premium resort. Arrive at your premium resort and check into your spacious family suite, featuring special welcome amenities. Spend the afternoon unwinding by the lagoon swimming pool or taking your first family photos overlooking the sunset. In the evening, your private van takes you to a premium restaurant for a welcome buffet dinner filled with familiar comforts, ensuring a restful start for an unforgettable family vacation. Sightseeing Included: Private luxury van airport transit, scenic coastal drive, Patong Beach orientation. Evening Experience: Family welcome dinner at an upscale restaurant with gorgeous ocean vistas.'
                ),
                [
                    'Overnight Stay: Phuket (Premium High-Rise Family Resort with Ocean View)',
                    'Meals Included: Curated Multi-Cuisine Family Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PRIVATE LUXURY SPEEDBOAT TO PHI PHI ISLANDS',
                (
                    'TURQUOISE LAGOONS, SNORKELING ESCAPADES & MAYA BAY VIEWPOINTS Wake up to a gorgeous morning over the ocean and enjoy a lavish buffet breakfast. Today hosts the ultimate centerpiece of your Best Phuket Tour Package: an exclusive private island-hopping expedition to the legendary Phi Phi Islands. Avoid all crowded commercial public tour boats as TRAGUIN provides a private, high-speed luxury speedboat to pick up your family directly from the resort beachfront. Cruise over crystal-clear turquoise waters to arrive at the vertical limestone walls of Maya Bay, offering a premium photography point for the family. The kids can swim in the calm shallow waters while the adults snorkel in the emerald basin of Pileh Lagoon. Savor a delicious fresh gourmet lunch served right on the white sands of Bamboo Island. Conclude the day exploring the historic Viking Cave before cruising back home. Sightseeing Included: Private Speedboat to Phi Phi Islands, Maya Bay entry, Pileh Lagoon snorkeling, Bamboo Island beach stop, Viking Cave. Optional Activities: Undersea Sea-Walking or Glass-Bottom Boat coral reef viewing for children and seniors.'
                ),
                [
                    'Overnight Stay: Phuket (Premium High-Rise Family Resort with Ocean View)',
                    'Meals Included: International Buffet Breakfast & Beachside Island Picnic Lunch',
                ],
            ),
            _day(
                3,
                'PHANG NGA BAY & JAMES BOND ISLAND EXPEDITION',
                (
                    'MYSTICAL SEA CAVES, MONOLITH ROCK TOWERS & FLOATING VILLAGE LUNCH Prepare for an awe-inspiring day uncovering hidden geographical wonders. Following a beautiful breakfast, your private van navigates the group to the pier for a premium speed-craft cruise across Phang Nga Bay. Cruise past hundreds of vertical limestone karsts rising dramatically out of the calm sea, a prominent highlight of Phuket Sightseeing. Arrive at James Bond Island, an iconic attraction, and capture fantastic pictures in front of the floating rock monolith. Next, enjoy a relaxing canoeing experience guided through the mystical sea caves and hidden mangrove lagoons of Koh Hong. Savor a fresh seafood lunch at the unique stilted floating village of Koh Panyee. Return to the resort to refresh for an evening of relaxation or boutique shopping at local street markets. Sightseeing Included: James Bond Island, Koh Hong sea cave canoeing, Koh Panyee stilted village exploration. Evening Experience: Strolling through the colorful local night markets for traditional Thai souvenirs and snacks.'
                ),
                [
                    'Overnight Stay: Phuket (Premium High-Rise Family Resort with Ocean View)',
                    'Meals Included: International Buffet Breakfast & Koh Panyee Floating Village Seafood Lunch',
                ],
            ),
            _day(
                4,
                'PHUKET CULTURAL TOUR & SIMON CABARET GLAMOUR',
                (
                    'THE BIG BUDDHA PANORAMA, OLD TOWN ARCHITECTURE & VIP THEATRICS Enjoy a relaxed morning before starting a comprehensive Phuket Sightseeing cultural day. Your private chauffeur navigates your family up the Nakkerd Hills to stand at the base of the majestic 45-meter Big Buddha monument. This peak offers a staggering 360-degree panorama of Chalong Bay and Phuket Town— consistently ranked among the most popular Instagram locations. Continue your premium tour to Wat Chalong monastery and the historic Sino-Portuguese colonial streets of Old Phuket Town. Walk past beautiful mansions, vibrant street murals, and artisan boutiques. In the evening, dress in your finest outfits for a grand night out. TRAGUIN has reserved premium front-row VIP seats for your family at the globally acclaimed Simon Cabaret Show. Witness a masterclass in theatrical production featuring spectacular costumes and dance sequences. Sightseeing Included: The Big Buddha, Wat Chalong Temple, Old Phuket Town, VIP entry to Simon Cabaret Show. Optional Activities: A visit to a traditional premium gemstone artisan gallery or a local organic honey farm.'
                ),
                [
                    'Overnight Stay: Phuket (Premium High-Rise Family Resort with Ocean View)',
                    'Meals Included: International Buffet Breakfast & Contemporary Thai Fine Dining Lunch',
                ],
            ),
            _day(
                5,
                'LEISURE & GRAND BEACHFRONT FINALE',
                (
                    'RELAXATION IN PARADISE & A SIGNATURE BEACH CANDLELIGHT DINNER Dedicate today to pure family joy and well-deserved relaxation. Spend the morning lounging by the lagoon pool or walking along the soft sand beach, capturing final group photos. For your final evening, TRAGUIN has arranged our ultimate signature surprise: an intimate, completely private beachfront candlelight dinner set in a secluded cove of the resort. Toast your family vacation with a glass of fine wine under a starlit sky as gentle waves roll in, creating a memory to last a lifetime. Sightseeing Included: Resort leisure schedule, private beach cove reservation. Evening Experience: Signature TRAGUIN Grand Finale Private Beachfront Candlelight Family Dinner.'
                ),
                [
                    'Overnight Stay: Phuket (Premium High-Rise Family Resort with Ocean View)',
                    'Meals Included: International Buffet Breakfast & 4-Course Oceanfront Farewell Dinner',
                ],
            ),
            _day(
                6,
                'PHUKET DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER UNITED Savor your final morning breakfast at your premium resort, capturing a final round of group family photos across the tropical landscaped gardens. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless group checkout and handle luggage logistics. At the designated hour, your private luxury van arrives to transfer your family comfortably to Phuket International Airport for your return flight home. As you board your aircraft, look back on an exceptional collection of curated experiences, breathtaking landscapes, and unforgettable family memories crafted beautifully by TRAGUIN. Your premium Phuket Family Tour concludes beautifully, leaving your loved ones with stories to pass down through generations. Sightseeing Included: Private luxury airport departure transfer.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Phuket Resort (Patong) Deluxe Family Ocean Room Complimentary Welcome Drinks & Access to Kids Club Play Zone',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Novotel Phuket Resort (Patong) Deluxe Family Ocean Room Complimentary Welcome Drinks & Access to Kids Club Play Zone',
            ),
            _hotel(
                'Phuket Marriott Resort, Merlin Beach Premium Family Pool View Room Welcome Fruit Platters, Free Ice Cream for Kids & Large Water Pool Access',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Phuket Marriott Resort, Merlin Beach Premium Family Pool View Room Welcome Fruit Platters, Free Ice Cream for Kids & Lar',
            ),
            _hotel(
                'The Westin Siray Bay Resort & Spa Luxury Seaview Family Suite Complimentary Floating Breakfast Setup & Kids Spa Discount Vouchers',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Westin Siray Bay Resort & Spa Luxury Seaview Family Suite Complimentary Floating Breakfast Setup & Kids Spa Discount',
            ),
            _hotel(
                'Anantara Layan Phuket Resort / Sri Panwa Deluxe Pool Villa / Luxury Ocean Suite Premium Champagne Bottle, Private Beach Access & 24/7 Butler Care',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Anantara Layan Phuket Resort / Sri Panwa Deluxe Pool Villa / Luxury Ocean Suite Premium Champagne Bottle, Private Beach ',
            )
        ],
        inclusions=[
            _inc_included('Handpicked premium accommodation as per selected hotel tier', 1),
            _inc_included('Private luxury vehicle transfers and sightseeing as per itinerary', 2),
            _inc_included('Daily buffet breakfast and curated meals as specified', 3),
            _inc_included('VIP airport fast-track reception and dedicated TRAGUIN concierge support', 4),
            _inc_excluded('PACKAGE INCLUSIONS', 5),
        ],
    )
    return package, itinerary

def build_th_033(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-033'
    tour_code = 'TRG-KBV-HON-2026'
    title = 'ROMANTIC KRABI HONEYMOON Ao Nang Bay • Railay Peninsula • Koh Hong Lagoons • Sunset Catamaran'
    duration = '05 Nights / 06 Days'
    slug = 'th-033-romantic-krabi-honeymoon-ao-nang-bay-railay-peninsula-koh-hong-lagoons-sunset-catamaran'
    itin_slug = 'th-033-romantic-krabi-honeymoon-ao-nang-bay-railay-peninsula-koh-hong-lagoons-sunset-catamaran-itinerary'
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
            _ph('Serial code TH-033 | TRAGUIN tour code TRG-KBV-HON-2026', 1),
            _ph('State / Country: Thailand | Category: Romantic Krabi Honeymoon Package', 2),
            _ph('Destinations: Krabi Coastal Sanctuary', 3),
            _ph('Ideal for: Honeymooners, Couples, Romance Seekers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Chauffeur- Driven Luxury Sedan / SUV / Bespoke Breakfasts, Island Picnics & Candlelight Dinners Ignite your love story in a sanctuary of vertical limestone monoliths and turquoise lagoons with', 7),
            _ph('TRAGUIN Signature Experience: Private luxury yacht charters, completely avoiding standard tourist', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked romantic properties featuring maximum isolation, infinity', 9),
            _ph('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities and', 10),
            _ph('Luxury Transportation: Elite private executive sedans stocked with chilled water, music preferences,', 11)
        ],
        moods=['Honeymoon', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='ROMANTIC KRABI HONEYMOON Ao Nang Bay',
        overview="Ao Nang Bay • Railay Peninsula • Koh Hong Lagoons • Sunset Catamaran 05 Nights / 06 Days Ultra-Luxury Romantic Couple's Escape SERIAL CODE: TH-033 TRAGUIN TOUR CODE: TRG-KBV-HON-2026 STATE / COUNTRY: Thailand CATEGORY: Romantic Krabi Honeymoon Package DURATION: 05 Nights / 06 Days DESTINATIONS COVERED: Krabi Coastal Sanctuary (5 Nights) IDEAL FOR: Honeymooners, Couples, Romance Seekers BEST SEASON: November to May (Pristine Coastal Skies) VEHICLE TYPE: Private Chauffeur- Driven Luxury Sedan / SUV MEAL PLAN: Bespoke Breakfasts, Island Picnics & Candlelight Dinners Ignite your love story in a sanctuary of vertical limestone monoliths and turquoise lagoons with the Best Krabi Honeymoon Package, meticulously engineered by TRAGUIN to offer an unmatched blend of seclusion and coastal elegance. This signature Luxury Krabi Holiday places your romantic narrative across breathtaking landscapes, handpicked hotels of worldwide distinction, and exclusive experiences to create unforgettable memories.\n\nTOUR OVERVIEW\nWelcome to your bespoke Romantic Krabi getaway, tailored explicitly for couples who demand an exquisite blend of intimacy, elite personalization, and serene island beauty. On this 6-day holiday, TRAGUIN ensures a flawless travel experience featuring premium pool villas, private speed-craft charters to hidden sandbars, and tailored culinary evenings. TRAGUIN Curated Experience Note: Every milestone of this honeymoon proposal is curated by our romance-specialist concierge team. We guarantee private logistics, personalized daily surprise moments, and absolute on-ground support to ensure your journey into forever is completely seamless.\n\nWHY CHOOSE OUR LUXURY KRABI HONEYMOON?\nKrabi stands as the undisputed masterpiece of tropical romance, interweaving rugged limestone tower vistas with ivory sands and crystal marine corridors. Choosing a specialized Krabi Honeymoon Package or one of our ultra-exclusive TRAGUIN Thailand Packages ensures you transcend ordinary tourist tracks. This proposal integrates top searched keywords for Google ranking, ensuring the ultimate showcase of Krabi Sightseeing wonders. Uncover iconic attractions: the dramatic vertical monoliths of Railay Peninsula, the mystical secret sea caves of the Hong Archipelago, and the serene geothermal pools of the interior forest. It is universally recognized as the Best Time to Visit Thailand to capture stunning photography points at popular Instagram locations, indulge in high-end couple's spa treatments, and enjoy a truly unforgettable Premium Thailand Experience. TRAGUIN Romance Signatures: Private high-speed catamaran cruise to isolated coves, a 150-minute luxury couple’s aroma-spa therapy session, exclusive sunset beachfront candlelight dining, and dedicated 24/7 personal travel concierge support. THE ROMANTIC DAY-WISE ITINERARY",
        seo_title='TH-033 | ROMANTIC KRABI HONEYMOON Ao Nang Bay | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-033 / TRG-KBV-HON-2026): Krabi Coastal Sanctuary with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN KRABI & SUNSET LUXURY', 1),
            _ih('Day 02: PRIVATE CATAMARAN TO THE HONG ISLANDS', 2),
            _ih('Day 03: RAILAY PENINSULA ADVENTURE & REJUVENATION RETREAT', 3),
            _ih('Day 04: THE 4-ISLANDS EXPEDITION & SANDBAR ROMANCE', 4),
            _ih('Day 05: JUNGLE CASCADES & GRAND FINALE CELEBRATION', 5),
            _ih('Day 06: KRABI DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private luxury yacht charters, completely avoiding standard tourist', 7),
            _ih('Curated by TRAGUIN Experts: Handpicked romantic properties featuring maximum isolation, infinity', 8),
            _ih('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities and', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN KRABI & SUNSET LUXURY',
                (
                    'WELCOME TO THE LIMESTONE PARADISE – THE JOURNEY INTO ETERNITY BEGINS Your spectacular Romantic Krabi Honeymoon unfolds perfectly as you arrive at Krabi International Airport. Step through the gate to receive a warm, traditional Thai floral welcome coordinated seamlessly by your dedicated TRAGUIN lifestyle representative. Avoid the hassle of standard airport transfers as you step directly into your private, executive luxury sedan for a smooth, scenic drive along the coast to your ultra-luxury pool villa sanctuary. Check into your handpicked premium honeymoon suite, detailed with elegant custom floral architecture and a chilled complimentary bottle of premium champagne. Spend your afternoon in complete privacy, unwinding inside your private infinity pool or walking hand-in-hand along the quiet resort beach. In the evening, step down to a secluded beachfront pavilion for a curated candlelight dinner, creating your first unforgettable memories together under a beautiful sky. Sightseeing Included: Private luxury vehicle airport transit, Ao Nang shoreline orientation stroll. Evening Experience: Signature TRAGUIN Beachfront Private Candlelight Dinner under the stars.'
                ),
                [
                    'Overnight Stay: Krabi (Ultra-Luxury Private Pool Villa Resort)',
                    'Meals Included: 4-Course Gourmet Private Dinner',
                ],
            ),
            _day(
                2,
                'PRIVATE CATAMARAN TO THE HONG ISLANDS',
                (
                    "EMERALD LAGOON CANOEING & THE 360-DEGREE VIEWPOINT ASCENT Wake up to the gentle murmur of the ocean and enjoy a lavish buffet breakfast. Today hosts a cornerstone Premium Thailand Experience: an exclusive private sailing voyage across the emerald waters of the Hong Archipelago. Skip the large commercial group tours as TRAGUIN arranges a private luxury catamaran charter to glide your couple directly into the hidden interior lagoon, enclosed by colossal limestone towers. Pilot your stable sea canoes hand-in-hand into the narrow rock entrance of the hidden lagoon, a perfect photography point. Ascend the spectacular 419-step metal walkway up to the 360-degree viewpoint platform, capturing a breathtaking panorama of the bay. Savor a premium gourmet picnic lunch served right on the white sandshore. Return to your resort to refresh for a relaxing evening at a stylish cliffside bar. Sightseeing Included: Private Catamaran cruise, Koh Hong Lagoon sea-cave canoeing, 360-degree Viewpoint climb. Optional Activities: Professional drone couples' photography session on the white sands of Hong Island."
                ),
                [
                    'Overnight Stay: Krabi (Ultra-Luxury Private Pool Villa Resort)',
                    'Meals Included: International Buffet Breakfast & Luxury Catamaran Gourmet Picnic Lunch',
                ],
            ),
            _day(
                3,
                'RAILAY PENINSULA ADVENTURE & REJUVENATION RETREAT',
                (
                    "VERTICAL MONOLITHS, SACRED SHRINES & 150-MINUTE COUPLE'S SPA Embrace a slow-paced morning. Following breakfast, board a private longtail speed-craft to the isolated Railay Peninsula, accessible only by water. Walk through the dramatic limestone caves to Railay West beach, witnessing the monumental vertical rock faces that make this a top tourist place in Thailand. Explore the legendary Phra Nang Cave, a sacred site adorned with floral garlands. Return to the resort to transition into absolute wellness. TRAGUIN has reserved an exclusive 150-minute couple's spa package featuring traditional Thai steam rituals, organic body scrubs, and therapeutic aromatic oil massages side-by-side. Spend the remainder of your afternoon lounging in your private pool or enjoying a quiet sunset walk along the resort’s hidden cove. Sightseeing Included: Private longtail boat transit, Railay peninsula rock-climbing viewpoints, Phra Nang Cave shrine. Evening Experience: Relaxing over traditional Thai herbal tea at a peaceful cliff-edge lounge."
                ),
                [
                    'Overnight Stay: Krabi (Ultra-Luxury Private Pool Villa Resort)',
                    'Meals Included: International Buffet Breakfast & Contemporary Thai Dining Lunch',
                ],
            ),
            _day(
                4,
                'THE 4-ISLANDS EXPEDITION & SANDBAR ROMANCE',
                (
                    'SECRET SANDBARS, CRYSTAL REEFS & SUNSET YACHT CRUISING Dedicate today to pristine island discovery. Following breakfast, your private luxury boat launches for an iconic journey across Krabi’s 4-Islands. Visit Tup Island, where a unique natural sandbar emerges at low tide, allowing you to walk between islands on crystal water—a perfect photography point. Snorkel over the live barrier reefs of Chicken Island, surrounded by multi-colored schools of fish. In the afternoon, board your private luxury yacht for an exclusive sunset sailing expedition. Sip premium wine and enjoy gourmet tapas as you cruise towards the limestone pillars of the gulf. Witness an unforgettable tropical sunset from the deck of your yacht as the horizon turns into deep golden shades. It is an exceptional experience to celebrate your love on this Luxury Krabi Holiday. Sightseeing Included: Tup Island Sandbar walk, Chicken Island reef snorkeling, Poda Island beach access, Sunset Yacht Cruise. Optional Activities: A private couple’s sunset meditation session on the yacht deck with local instructors.'
                ),
                [
                    'Overnight Stay: Krabi (Ultra-Luxury Private Pool Villa Resort)',
                    'Meals Included: International Buffet Breakfast & Luxury Yacht Sunset Tapas & Wine',
                ],
            ),
            _day(
                5,
                'JUNGLE CASCADES & GRAND FINALE CELEBRATION',
                (
                    'NATURAL GEOTHERMAL POOLS & A SIGNATURE BEACH COVE GALA Today combines lush interior nature with our crowning signature romantic surprise. Savor a decadent floating breakfast served right inside your private pool villa. In the afternoon, your private driver transfers your group inland to the emerald geothermal pools, where you can dip your feet inside the therapeutic mineral water. Take a short, easy walk through the surrounding coconut forests before returning to the resort to refresh for your final evening. For your grand finale, TRAGUIN has arranged our ultimate signature surprise: an intimate, completely private beachfront candlelight dinner set in a secluded cove of the resort. Toast your honeymoon holiday with a glass of vintage wine under a starlit sky as gentle waves roll in, celebrating a collection of unforgettable memories. Sightseeing Included: Emerald Pool geothermal sanctuary, coconut forest walking trails, private cove beach access. Evening Experience: Signature TRAGUIN Grand Finale Private Beachfront Candlelight Dinner under the stars.'
                ),
                [
                    'Overnight Stay: Krabi (Ultra-Luxury Private Pool Villa Resort)',
                    'Meals Included: Premium Floating Villa Breakfast & 5-Course Beachside Finale Dinner',
                ],
            ),
            _day(
                6,
                'KRABI DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER ENTWINED Enjoy your final morning breakfast looking out over the misty mountain vistas. Capture final photos across the tropical garden sanctuaries. Depending on your flight schedule, the morning is yours to relax or squeeze in last-minute souvenir shopping for premium Thai herbal oils and artisan crafts. At the designated hour, your private luxury executive vehicle arrives to transfer you comfortably to Krabi International Airport for your journey home. As you board your aircraft, look back on an exceptional collection of curated experiences, breathtaking landscapes, and unforgettable romantic memories crafted beautifully by TRAGUIN. Your premium Krabi Honeymoon Package concludes perfectly. Sightseeing Included: Private luxury vehicle airport departure transfer.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Ao Nang Cliff Beach Resort Deluxe Ocean View Suite Complimentary Honeymoon Cake & Bed Decoration',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Ao Nang Cliff Beach Resort Deluxe Ocean View Suite Complimentary Honeymoon Cake & Bed Decoration',
            ),
            _hotel(
                'Centara Grand Beach Resort Krabi Deluxe Garden Pavilion Bed Decoration, Welcome Fruit Platter & 1 Cocktails Voucher',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Centara Grand Beach Resort Krabi Deluxe Garden Pavilion Bed Decoration, Welcome Fruit Platter & 1 Cocktails Voucher',
            ),
            _hotel(
                'Rayavadee Krabi Resort Deluxe Pavilion Estate Sparkling Wine Bottle, Floral Bath Setup & Floating Breakfast',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Rayavadee Krabi Resort Deluxe Pavilion Estate Sparkling Wine Bottle, Floral Bath Setup & Floating Breakfast',
            ),
            _hotel(
                'Phulay Bay, a Ritz-Carlton Reserve Reserve Pavilion Pool Villa Premium Champagne, 150-min Couple Spa & Private Beachfront Pavilion Access',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Phulay Bay, a Ritz-Carlton Reserve Reserve Pavilion Pool Villa Premium Champagne, 150-min Couple Spa & Private Beachfron',
            )
        ],
        inclusions=[
            _inc_included('Handpicked premium accommodation as per selected hotel tier', 1),
            _inc_included('Private luxury vehicle transfers and sightseeing as per itinerary', 2),
            _inc_included('Daily buffet breakfast and curated meals as specified', 3),
            _inc_included('VIP airport fast-track reception and dedicated TRAGUIN concierge support', 4),
            _inc_excluded('PACKAGE INCLUSIONS', 5),
        ],
    )
    return package, itinerary

def build_th_034(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-034'
    tour_code = 'TRG-THA-GRP-2026'
    title = 'THAILAND FIXED DEPARTURE Bangkok • Pattaya • Coral Island • Marine Discovery'
    duration = '05 Nights / 06 Days'
    slug = 'th-034-thailand-fixed-departure-bangkok-pattaya-coral-island-marine-discovery'
    itin_slug = 'th-034-thailand-fixed-departure-bangkok-pattaya-coral-island-marine-discovery-itinerary'
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
            _ph('Serial code TH-034 | TRAGUIN tour code TRG-THA-GRP-2026', 1),
            _ph('State / Country: Thailand | Category: Fixed Departure Group Tour', 2),
            _ph('Destinations: Bangkok (3N) + Pattaya', 3),
            _ph('Ideal for: Social Groups, Travel Enthusiasts, Friends Gangs', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Premium Private Group Coach / Buffet Breakfast (CP), Selected Lunches & Dinners Experience the vibrant essence of the kingdom with the Best Thailand Tour Package specifically curated for group travele', 7),
            _ph('TRAGUIN Signature Experience: Private group speedboats and museum fast-track passes,', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium group hotels located directly adjacent to main', 9),
            _ph('Personalized Assistance: English-fluent dedicated local group coordinators to manage reservation', 10),
            _ph('Luxury Transportation: Executive modern coaches equipped with cooling, on-board entertainment', 11)
        ],
        moods=['Family', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='THAILAND FIXED DEPARTURE Bangkok',
        overview="Bangkok • Pattaya • Coral Island • Marine Discovery 05 Nights / 06 Days Optimized Group Discovery Tour SERIAL CODE: TH-034 TRAGUIN TOUR CODE: TRG-THA-GRP-2026 STATE / COUNTRY: Thailand CATEGORY: Fixed Departure Group Tour DURATION: 05 Nights / 06 Days DESTINATIONS COVERED: Bangkok (3N) + Pattaya (2N) IDEAL FOR: Social Groups, Travel Enthusiasts, Friends Gangs BEST SEASON: November to April (Optimal Weather) VEHICLE TYPE: Premium Private Group Coach MEAL PLAN: Buffet Breakfast (CP), Selected Lunches & Dinners Experience the vibrant essence of the kingdom with the Best Thailand Tour Package specifically curated for group travelers by TRAGUIN. This high-energy Thailand Fixed Departure itinerary expertly captures breathtaking landscapes, iconic attractions, and local culture, delivering unforgettable memories through flawlessly organized logistics.\n\nTOUR OVERVIEW\nWelcome to your optimized Thailand Fixed Departure vacation, structured by TRAGUIN Experts to deliver maximum cultural engagement, social interaction, and seamless logistical flow for group travelers. Over 6 action-packed days, your party will bridge the gap between Bangkok's historic royal palaces and Pattaya's vibrant coastal entertainment scene, all managed within our elite travel framework. TRAGUIN Fixed Departure Group • TRAGUIN Curated Experience Note: Fixed departure groups deserve operational precision. Our itinerary includes priority fast-track group entry protocols at key sights, premium air-conditioned group coaches, pre- vetted buffet meal logs catering to dietary diversity, and dedicated professional group tour managers providing 24/7 personal assistance.\n\nWHY CHOOSE OUR THAILAND FIXED DEPARTURE HOLIDAY?\nThailand remains the world’s most versatile destination for vibrant group holidays, effortlessly balancing high- octane entertainment with serene ancient history. Choosing this organized Thailand Fixed Departure package through TRAGUIN ensures a stress-free group movement optimized for social bonding and comprehensive discovery. This itinerary integrates key targeted tourism keywords for Google ranking, ensuring an exceptional overview of premier Thailand Sightseeing wonders. Discover Top Tourist Places in Thailand: the monumental architecture of Bangkok's temples, the crystal blue waters of Coral Island, and the lively shopping streets of the Gulf Coast. It is universally recognized as the Best Time to Visit Thailand to explore popular Instagram locations, indulge in high-energy marine athletics, shop for local handicrafts, and enjoy a genuinely rewarding Premium Thailand Experience. TRAGUIN Group Signatures: Priority group entry passes for Bangkok landmarks, dedicated private group coach transport throughout the itinerary, an immersive Coral Island day expedition, and a pre-arranged gala dinner event. TRAGUIN Fixed Departure Group • THE DEFINITIVE DAY-WISE ITINERARY",
        seo_title='TH-034 | THAILAND FIXED DEPARTURE Bangkok | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-034 / TRG-THA-GRP-2026): Bangkok (3N) + Pattaya with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BANGKOK & LOCAL ORIENTATION', 1),
            _ih('Day 02: BANGKOK ROYAL TEMPLES & GRAND CANALS', 2),
            _ih('Day 03: BANGKOK TO PATTAYA & BEACHSIDE RELAXATION', 3),
            _ih('Day 04: CORAL ISLAND MARINE EXPEDITION', 4),
            _ih('Day 05: NONG NOOCH GARDENS & DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private group speedboats and museum fast-track passes,', 6),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium group hotels located directly adjacent to main', 7),
            _ih('Personalized Assistance: English-fluent dedicated local group coordinators to manage reservation', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BANGKOK & LOCAL ORIENTATION',
                (
                    "THE CAPTIVATING WELCOME – SMOOTH TRANSIT TO THE HEART OF ASIA Your dynamic Thailand Fixed Departure tour hits the ground running the moment your group touches down at Bangkok’s Suvarnabhumi Airport. Clear the arrival gates to be greeted by your friendly TRAGUIN group tour leader. Step into our premium, air-conditioned group coach, ensuring a smooth, air-conditioned transit into the heart of the metropolis. Check into your premium handpicked hotel, centrally located to maximize your exploration time. Take a brief orientation tour around the hotel neighborhood to discover local cafes and conveniences before the group gathers for a welcome dinner. This casual dinner session acts as the perfect forum to align the itinerary, share expectations, and build team rapport for the adventure ahead, ensuring your holiday starts on a high note. Sightseeing Included: Airport group reception, city orientation tour. Evening Experience: Group welcome dinner and briefing session at the hotel's central dining hall. TRAGUIN Fixed Departure Group •"
                ),
                [
                    'Overnight Stay: Bangkok (Premium Lifestyle Hotel)',
                    'Meals Included: International Welcome Dinner Buffet',
                ],
            ),
            _day(
                2,
                'BANGKOK ROYAL TEMPLES & GRAND CANALS',
                (
                    'SIAMESE SPLENDOR – THE GRAND PALACE & RIVER WAYS Fuel up with a bountiful buffet breakfast. Today showcases the historical grandeur of Bangkok. Your luxury group coach transfers you to the historic core to visit the Grand Palace and the Temple of the Emerald Buddha (Wat Phra Kaew), an essential Thailand Sightseeing highlight. Admire the golden spires and intricate detailing that represent the architectural genius of the Lanna and Rattanakosin eras. Continue to Wat Pho to stand before the 46-meter Reclining Buddha temple, a truly iconic attraction. In the afternoon, board a group-chartered wooden longtail boat to cruise through the historic Thonburi canal network. Witness traditional Thai wooden stilt houses and small community temples, capturing beautiful Sightseeing Included: The Grand Palace, Wat Phra Kaew, Wat Pho, private longtail canal boat ride. Optional Activities: Shopping at the famous MBK Center for local tech and fashion bargains.'
                ),
                [
                    'photography points: before returning to the city center for a casual group dinner and shopping time.',
                    'Overnight Stay: Bangkok (Premium Lifestyle Hotel)',
                    'Meals Included: International Breakfast & Local Thai Bistro Lunch',
                ],
            ),
            _day(
                3,
                'BANGKOK TO PATTAYA & BEACHSIDE RELAXATION',
                (
                    "COASTAL ESCAPE – MOTORWAY TRANSIT & OCEAN SUNSET Check out after breakfast as your group moves towards the coastal resort city of Pattaya. Enjoy a smooth highway drive. Upon arrival, proceed for a brief check-in to your premium seaside resort. Spend the remainder of your afternoon unwinding by the pool or enjoying the warm ocean air—it's the perfect time to capture breathtaking landscapes along the gulf coast. In the evening, stroll along the vibrant Pattaya Beach Road, filled with light, music, and local energy. Choose from the diverse range of waterfront dining options to enjoy a relaxed dinner, perhaps trying fresh seafood catch-of-the-day while discussing the exciting island excursion planned for tomorrow. Sightseeing Included: Group coastal highway transit, Pattaya beach orientation stroll. Evening Experience: Independent exploring of the vibrant Pattaya night bazaar market. TRAGUIN Fixed Departure Group •"
                ),
                [
                    'Overnight Stay: Pattaya (Premium Beachside Family Resort)',
                    'Meals Included: International Breakfast & Casual Seaside Dinner',
                ],
            ),
            _day(
                4,
                'CORAL ISLAND MARINE EXPEDITION',
                (
                    'TROPICAL BLUE – SPEED-CRAFT SAILING & MARINE SPORTS Start your day with a hearty, energizing breakfast. Today is the ultimate highlight of your Pattaya Sightseeing program: an expedition to Koh Larn (Coral Island). Your group will board a private speed-craft charter, cutting across the blue waves of the Gulf of Thailand to land on a pristine white-sand bay. The day is packed with group fun. Spend time swimming in shallow, crystalline water or relaxing on beach loungers with fresh coconut water. For the adventure lovers, take part in optional parasailing or sea-walking explorations over the reef. Enjoy a group buffet lunch by the shore before cruising back to the resort in the late afternoon to refresh for the evening celebration. Sightseeing Included: Private group speed-craft charter, Koh Larn beach day. Optional Activities: Exhilarating parasailing, sea-walking, or banana boat sports bundle.'
                ),
                [
                    'Overnight Stay: Pattaya (Premium Beachside Family Resort)',
                    'Meals Included: International Breakfast & Island Beachside Buffet Lunch',
                ],
            ),
            _day(
                5,
                'NONG NOOCH GARDENS & DEPARTURE',
                (
                    'BOTANICAL VALLEY MARVELS & CHERISHING UNFORGETTABLE MEMORIES Enjoy a final buffet breakfast before heading to one of the most stunning popular Instagram locations: Nong Nooch Botanical Gardens. This massive tropical valley showcases spectacular floral arrangements, dinosaur valleys, and traditional Thai culture, all accessible via our group-chartered open-air electric carts. After taking your final group photos, your coach transfers your group back towards Bangkok for your flight home. As you board, look back on an exceptional collection of curated experiences, breathtaking landscapes, and unforgettable group memories crafted beautifully by TRAGUIN. Your premium Thailand Fixed Departure tour concludes perfectly. Sightseeing Included: Nong Nooch Botanical Gardens entry, electric cart exploration. Evening Experience: Group departure logistics at Suvarnabhumi International Airport. TRAGUIN Fixed Departure Group •'
                ),
                [
                    'Overnight Stay: N/A',
                    'Meals Included: International Buffet Breakfast & Farewell Lunch',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Sukosol Bangkok Premier Group Rooms Novotel Pattaya Beachfront Superior Ocean Rooms',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — The Sukosol Bangkok Premier Group Rooms Novotel Pattaya Beachfront Superior Ocean Rooms',
            ),
            _hotel(
                'Grande Centre Point Terminal 21 Premium Deluxe Rooms Amari Pattaya Deluxe Garden View Rooms',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Grande Centre Point Terminal 21 Premium Deluxe Rooms Amari Pattaya Deluxe Garden View Rooms',
            ),
            _hotel(
                'Avani+ Riverside Bangkok Avani River View Rooms Hilton Pattaya Executive Ocean Rooms',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Avani+ Riverside Bangkok Avani River View Rooms Hilton Pattaya Executive Ocean Rooms',
            ),
            _hotel(
                'Shangri-La Bangkok Horizon Club River View Grande Centre Point Space Pattaya Space Premium Suites',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Shangri-La Bangkok Horizon Club River View Grande Centre Point Space Pattaya Space Premium Suites',
            )
        ],
        inclusions=[
            _inc_included('Daily Meals: 4 Buffet Breakfasts, 2 Lunches, 1 Group Welcome Dinner.', 1),
            _inc_included('Private Vehicles: Private air-conditioned luxury coach with an experienced driver for all transfers.', 2),
            _inc_included('Island Excursion: Private high-speed speedboat charter to Coral Island.', 3),
            _inc_included('VIP Sightseeing: VIP front-row seating for the Alcazar Cabaret Show.', 4),
            _inc_included('Culture Entry: Admission tickets to Grand Palace, Wat Pho, Nong Nooch & Waterparks.', 5),
            _inc_included('TRAGUIN Support: 24/7 dedicated local on- ground concierge group assistance.', 6),
            _inc_included('Flights: International flight tickets connecting home country with Thailand.', 7),
            _inc_excluded('Accommodation: 04 Nights stay in handpicked premium group-friendly hotels.', 8),
            _inc_excluded('Visa Costs: Thailand entry visa charges or fast-track electronic processing fees.', 9),
        ],
    )
    return package, itinerary

def build_th_035(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-035'
    tour_code = 'TRG-THA-FEST-2026'
    title = 'Bangkok • Pattaya • Loy Krathong / Songkran Festive Experience • Cultural Galas'
    duration = '05 Nights / 06 Days'
    slug = 'th-035-bangkok-pattaya-loy-krathong-songkran-festive-experience-cultural-galas'
    itin_slug = 'th-035-bangkok-pattaya-loy-krathong-songkran-festive-experience-cultural-galas-itinerary'
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
            _ph('Serial code TH-035 | TRAGUIN tour code TRG-THA-FEST-2026', 1),
            _ph('State / Country: Thailand | Category: Thailand Festival Tour / Cultural Group Tour', 2),
            _ph('Destinations: Bangkok (3 Nights) +', 3),
            _ph('Ideal for: Social Groups, Culture Enthusiasts, Festival Lovers', 4),
            _ph('Best season: During Thai Festive Seasons (Songkran / Loy Krathong)', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Premium Group Coach / Buffet Breakfast (CP), Themed Festive Lunches & Gala Dinners Join the jubilant spirit of the kingdom with the Best Thailand Festival Tour Package, meticulously curated by', 7),
            _ph('TRAGUIN Signature Experience: Private group speedboats and museum fast-track passes,', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium group hotels located directly adjacent to main', 9),
            _ph('Personalized Assistance: English-fluent dedicated local group coordinators to manage reservation', 10),
            _ph('Luxury Transportation: Executive modern coaches equipped with cooling, on-board entertainment', 11)
        ],
        moods=['Family', 'Honeymoon', 'Culture'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Bangkok',
        overview="TOUR OVERVIEW\nWelcome to your optimized Thailand Festival Tour, a cultural and high-energy journey specifically engineered by TRAGUIN Experts for group travelers who require high engagement, authentic celebrations, and handpicked premium host venues. Over 6 action-packed days, your group will experience the heartbeat TRAGUIN Festive Group Tours • of Thai traditions, whether it's the exuberant water splashing of Songkran or the ethereal glowing lanterns of Loy Krathong. TRAGUIN Curated Experience Note: Festival group movements demand exceptional logistics management. Our itinerary includes priority group access to designated celebration zones, private festival-ready coaches, pre-cleared buffet meal logs catering to all tastes, and senior local managers providing 24/7 dedicated professional assistance.\n\nWHY CHOOSE OUR THAILAND FESTIVAL TOUR?\nThailand’s national festivals are globally renowned for their vibrancy, color, and deep-rooted communal spirit, making them an extraordinary platform for group travelers. Orchestrating your festival pilgrimage through a specialized TRAGUIN Destination Package guarantees a beautifully run operation. This proposal integrates targeted tourism keywords for Google ranking, presenting an impeccable layout of premier Thailand Sightseeing wonders. Expose your group to the Top Tourist Places in Thailand: the ancient golden chambers of Bangkok’s palaces, the bustling floating markets of the central region, and the scenic coastal bays of Pattaya. It is universally acknowledged as the Best Time to Visit Thailand to capture architectural concepts, explore popular Instagram locations, participate in world-famous street celebrations, and experience a genuinely rewarding Premium Thailand Experience. TRAGUIN Festive & Cultural Features: Dedicated group viewing areas for festival parades, private festive- themed gala dinner with live entertainment, fast-track museum entries, and private group coaches for seamless inter-city movement. TRAGUIN Festive Group Tours • THE IMMERSIVE DAY-WISE ITINERARY",
        seo_title='TH-035 | Bangkok | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-035 / TRG-THA-FEST-2026): Bangkok (3 Nights) + with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BANGKOK & WELCOME GALA', 1),
            _ih('Day 02: BANGKOK ROYAL HERITAGE & FESTIVAL CENTER', 2),
            _ih('Day 03: BANGKOK TO PATTAYA & COASTAL ENERGY', 3),
            _ih('Day 04: CORAL ISLAND MARINE EXPEDITION', 4),
            _ih('Day 05: CULTURAL GARDENS & FAREWELL GALA', 5),
            _ih('TRAGUIN Signature Experience: Private group speedboats and museum fast-track passes,', 6),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium group hotels located directly adjacent to main', 7),
            _ih('Personalized Assistance: English-fluent dedicated local group coordinators to manage reservation', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BANGKOK & WELCOME GALA',
                (
                    'THE FESTIVE GATEWAY – COMFORTABLE PRIVATE COACH TRANSIT Your spectacular Thailand Festival Tour takes flight flawlessly the moment your group touches down at Bangkok’s Suvarnabhumi International Airport. Clear the arrival gates to a warm, organized reception managed directly by your TRAGUIN tour directors. Guests are immediately guided to our pre-vetted, air- conditioned private luxury coaches, ensuring a structured and comfortable transit into the center of the celebration hub. Arrive at your handpicked premium resort, centrally located to maximize your exploration time. After an initial safety and festival-prep briefing by the tour director, your group can take group photos along the city avenues, capturing a beautiful photography point. End the day with a healthy, well-planned international dinner buffet at the hotel, allowing the group to rest and prepare for the festivities ahead. Sightseeing Included: Group airport logistics management, city orientation drive. Evening Experience: Interactive ice-breaking and festival briefing session regarding local traditions and celebration rules. TRAGUIN Festive Group Tours •'
                ),
                [
                    'Overnight Stay: Bangkok (Premium Lifestyle Group Hotel)',
                    'Meals Included: International Welcome Buffet Dinner',
                ],
            ),
            _day(
                2,
                'BANGKOK ROYAL HERITAGE & FESTIVAL CENTER',
                (
                    'CULTURAL MASTERPIECES – GRAND PALACE & THE HEART OF THE FESTIVAL Fuel up with a bountiful buffet breakfast. Today showcases the historical grandeur of Bangkok. Your luxury group coach transfers you to the historic core to visit the Grand Palace and the Temple of the Emerald Buddha (Wat Phra Kaew), an essential Thailand Sightseeing highlight. Admire the golden spires and intricate detailing that represent the architectural genius of the Thai kingdom. Continue to Wat Pho to stand before the 46-meter Reclining Buddha temple, a truly iconic attraction. In the afternoon, your private coach drops the group at a main festival celebration zone (such as the riverside or a city park), where the local festivities are at their peak. Participate in the traditional activities, enjoy street entertainment, and soak in the vibrant atmosphere. Return for a casual group dinner and shopping time. Sightseeing Included: The Grand Palace, Wat Phra Kaew, Wat Pho, official festival celebration zone entry. Optional Activities: A private traditional Thai costume photo shoot at a local temple site.'
                ),
                [
                    'Overnight Stay: Bangkok (Premium Lifestyle Group Hotel)',
                    'Meals Included: International Breakfast & Traditional Thai Bistro Lunch',
                ],
            ),
            _day(
                3,
                'BANGKOK TO PATTAYA & COASTAL ENERGY',
                (
                    "TROPICAL TRANSIT – HIGHWAY DISCOVERY & PATTAYA SUNSET Check out comfortably after breakfast as your group moves towards the coastal resort city of Pattaya. Enjoy a smooth highway drive. Upon arrival, proceed for a brief check-in to your premium seaside resort. Spend the remainder of your afternoon unwinding by the pool or enjoying the warm ocean air—it's the perfect time to capture breathtaking landscapes along the gulf coast. In the evening, stroll along the vibrant Pattaya Beach Road, filled with light, music, and local energy. Choose from the diverse range of waterfront dining options to enjoy a relaxed dinner, perhaps trying fresh seafood catch-of-the-day while discussing the exciting island excursion planned for tomorrow. Sightseeing Included: Group coastal highway transit, Pattaya beach orientation stroll. Evening Experience: Independent exploring of the vibrant Pattaya night bazaar market. TRAGUIN Festive Group Tours •"
                ),
                [
                    'Overnight Stay: Pattaya (Premium Beachside Family Resort)',
                    'Meals Included: International Breakfast & Casual Seaside Dinner',
                ],
            ),
            _day(
                4,
                'CORAL ISLAND MARINE EXPEDITION',
                (
                    'TROPICAL BLUE – SPEED-CRAFT SAILING & MARINE SPORTS Start your day with a hearty, energizing breakfast. Today is the ultimate highlight of your Pattaya Sightseeing program: an expedition to Koh Larn (Coral Island). Your group will board a private speed-craft charter, cutting across the blue waves of the Gulf of Thailand to land on a pristine white-sand bay. The day is packed with group fun. Spend time swimming in shallow, crystalline water or relaxing on beach loungers. For the adventure lovers, take part in optional parasailing or sea-walking explorations over the reef. Enjoy a group buffet lunch by the shore before cruising back to the resort in the late afternoon to refresh for the evening celebration. Sightseeing Included: Private group speed-craft charter, Koh Larn beach day. Optional Activities: Exhilarating parasailing, sea-walking, or banana boat sports bundle.'
                ),
                [
                    'Overnight Stay: Pattaya (Premium Beachside Family Resort)',
                    'Meals Included: International Breakfast & Island Beachside Buffet Lunch',
                ],
            ),
            _day(
                5,
                'CULTURAL GARDENS & FAREWELL GALA',
                (
                    'BOTANICAL MARVELS & CHERISHING UNFORGETTABLE MEMORIES Enjoy a final buffet breakfast before heading to one of the most stunning popular Instagram locations: Nong Nooch Botanical Gardens. This massive tropical valley showcases spectacular floral arrangements, dinosaur valleys, and traditional Thai culture, all accessible via our group-chartered open-air electric carts. After taking your final group photos, your coach transfers your group back towards Bangkok for your flight home. As you board, look back on an exceptional collection of curated experiences, breathtaking landscapes, and unforgettable group memories crafted beautifully by TRAGUIN. Your premium Thailand Festival Tour concludes perfectly. Sightseeing Included: Nong Nooch Botanical Gardens entry, electric cart exploration. Evening Experience: Group departure logistics at Suvarnabhumi International Airport. TRAGUIN Festive Group Tours •'
                ),
                [
                    'Overnight Stay: N/A',
                    'Meals Included: International Buffet Breakfast & Farewell Lunch',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Sukosol Bangkok Premier Group Rooms Novotel Pattaya Beachfront Superior Ocean Rooms',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — The Sukosol Bangkok Premier Group Rooms Novotel Pattaya Beachfront Superior Ocean Rooms',
            ),
            _hotel(
                'Grande Centre Point Terminal 21 Premium Deluxe Rooms Amari Pattaya Deluxe Garden View Rooms',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Grande Centre Point Terminal 21 Premium Deluxe Rooms Amari Pattaya Deluxe Garden View Rooms',
            ),
            _hotel(
                'Avani+ Riverside Bangkok Avani River View Rooms Hilton Pattaya Executive Ocean Rooms',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Avani+ Riverside Bangkok Avani River View Rooms Hilton Pattaya Executive Ocean Rooms',
            ),
            _hotel(
                'Shangri-La Bangkok Horizon Club River View Grande Centre Point Space Pattaya Space Premium Suites',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Shangri-La Bangkok Horizon Club River View Grande Centre Point Space Pattaya Space Premium Suites',
            )
        ],
        inclusions=[
            _inc_included('Daily Meals: 4 Buffet Breakfasts, 2 Lunches, 1 Group Welcome Dinner.', 1),
            _inc_included('Private Vehicles: Private air-conditioned luxury coach with an experienced driver for all transfers.', 2),
            _inc_included('Island Excursion: Private high-speed speedboat charter to Coral Island.', 3),
            _inc_included('VIP Sightseeing: Priority fast-track group entry for festivals and main landmarks.', 4),
            _inc_included('Culture Entry: Admission tickets to Grand Palace, Wat Pho, Nong Nooch & Gardens.', 5),
            _inc_included('TRAGUIN Support: 24/7 dedicated local on- ground concierge group assistance.', 6),
            _inc_included('Flights: International flight tickets connecting home country with Thailand.', 7),
            _inc_excluded('Accommodation: 05 Nights stay in handpicked premium group-friendly hotels.', 8),
            _inc_excluded('Visa Costs: Thailand entry visa charges or fast-track electronic visa processing fees.', 9),
        ],
    )
    return package, itinerary

def build_th_036(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-036'
    tour_code = 'TRG-HKT-LUX-2026-V36'
    title = 'PHUKET LUXURY PACKAGE Phuket • Cape Panwa • Phang Nga Bay • Racha Yai Private Island'
    duration = '06 Nights / 07 Days'
    slug = 'th-036-phuket-luxury-package-phuket-cape-panwa-phang-nga-bay-racha-yai-private-island'
    itin_slug = 'th-036-phuket-luxury-package-phuket-cape-panwa-phang-nga-bay-racha-yai-private-island-itinerary'
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
            _ph('Serial code TH-036 | TRAGUIN tour code TRG-HKT-LUX-2026-V36', 1),
            _ph('State / Country: Thailand | Category: Best Phuket Luxury Tour Package', 2),
            _ph('Destinations: Phuket Island (6 Nights', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Executive Sedan / Mercedes-Benz / Bespoke Floating Breakfasts, Michelin Dining & Sunset Galas Discover the unparalleled coastal grandeur of the Andaman Sea with the Best Phuket Luxury T', 7),
            _ph('TRAGUIN Signature Experience: Private custom luxury yachts and marine charters, completely', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium luxury resorts featuring maximum isolation,', 9),
            _ph('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities and', 10),
            _ph('Luxury Transportation: Elite executive vehicles equipped with specialized suspension systems,', 11)
        ],
        moods=['Luxury', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='PHUKET LUXURY PACKAGE Phuket',
        overview="Phuket • Cape Panwa • Phang Nga Bay • Racha Yai Private Island 06 Nights / 07 Days Ultra-Luxury Coastal Sanctuary SERIAL CODE: TH-036 TRAGUIN TOUR CODE: TRG-HKT-LUX-2026- V36 STATE / COUNTRY: Thailand CATEGORY: Best Phuket Luxury Tour Package DURATION: 06 Nights / 07 Days DESTINATIONS COVERED: Phuket Island (6 Nights Premium Coastal Sanctuary) IDEAL FOR: Luxury Travelers, Couples, VIP Retreats BEST SEASON: November to May (Ideal Marine Visibility) VEHICLE TYPE: Private Luxury Executive Sedan / Mercedes-Benz MEAL PLAN: Bespoke Floating Breakfasts, Michelin Dining & Sunset Galas Discover the unparalleled coastal grandeur of the Andaman Sea with the Best Phuket Luxury Tour Package, meticulously engineered by TRAGUIN to offer an elite sanctuary of rest and discovery. Immerse yourself in a Premium Phuket Experience where breathtaking landscapes, world-renowned handpicked hotels, and exclusive experiences combine to create unforgettable memories.\n\nTOUR OVERVIEW\nWelcome to your bespoke Phuket Luxury holiday, a signature immersive journey structured explicitly by TRAGUIN Experts for guests who command seamless operational perfection, private security, and elite hospitality. Across 7 magnificent days, your party will reside in some of the world's finest coastal domains. Enjoy seamless private logistics in executive European sedans, personal yacht charters to hidden coves, and chef-driven culinary adventures. TRAGUIN Curated Experience Note: Your group’s well-being and absolute privacy are our ultimate parameters. From personalized consultations on arrival to private speed-craft sails to secluded, energy-rich island shores, every milestone is protected by our 24/7 dedicated local on-ground concierge network. THE ALLURE OF OUR PREMIUM PHUKET LUXURY EXPERIENCE Phuket has evolved far beyond a leisure space into the ultimate sanctuary of premium luxury, interweaving natural coastal energy lines with state-of-the-art holistic retreats and Michelin-endorsed organic dining. Opting for a specialized luxury holiday or a dedicated Phuket Honeymoon Package variant through TRAGUIN unlocks private access to hidden islands and elite maritime sanctuaries. This proposal targets the most highly searched tourism keywords for Google ranking, ensuring the ultimate showcase of Phuket Sightseeing wonders. Discover Top Tourist Places in Thailand: the peaceful sunrise horizons over Cape Panwa, the crystalline, energy-rich waters of Racha Yai Island, and the magnificent golden spires of Wat Chalong. It is universally recognized as the Best Time to Visit Thailand to explore popular Instagram locations for mindful reflection, indulge in a custom family tour centered on high-end luxury, and capture deep, immersive experiences that redefine the modern Premium Phuket Experience. TRAGUIN Luxury Signature Exclusives: Private VIP airport fast-track clearance, an elite private yacht sunset cruise to Racha Yai Island, 150 minutes of medical-grade spa rejuvenation, and a bespoke beachfront candlelight gala dinner in a secluded resort cove. THE DEFINITVE DAY-WISE ITINERARY",
        seo_title='TH-036 | PHUKET LUXURY PACKAGE Phuket | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Thailand package (TH-036 / TRG-HKT-LUX-2026-V36): Phuket Island (6 Nights with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN PHUKET & PRIVATE VILLA SANCTUARY', 1),
            _ih('Day 02: PRIVATE YACHT TO RACHA YAI ISLAND', 2),
            _ih('Day 03: CULTURAL HERITAGE & SPA REJUVENATION', 3),
            _ih('Day 04: PHANG NGA BAY SEA CAVE CANOEING', 4),
            _ih('Day 05: HOLISTIC WELLNESS & PRIVATE GRAND FINALE', 5),
            _ih('Day 06: PHUKET SHOPPING & DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private custom luxury yachts and marine charters, completely', 7),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium luxury resorts featuring maximum isolation,', 8),
            _ih('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities and', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN PHUKET & PRIVATE VILLA SANCTUARY',
                (
                    "WELCOME TO THE PEARL – STEPPING INTO INDULGENCE AND RENEWAL Your life-changing Phuket Luxury holiday unfolds flawlessly the moment your flight lands at Phuket International Airport. Avoid the standard crowds as a private TRAGUIN lifestyle concierge welcomes you with cold lemongrass towels, escorting you through premium lines directly to your waiting executive private luxury vehicle. Transfer smoothly along the scenic shoreline to your ultra-luxury beachfront sanctuary resort. Check into your sea-view pavilion, detailed with custom aromatherapy diffusers and organic welcome teas. In the afternoon, take a private tour of the resort's magnificent grounds or unwind inside your private infinity pool. End your opening evening with a gentle sunset beach walk followed by a curated organic welcome dinner served on an open-air oceanfront pavilion, setting a stunning photography point for your opening night. Sightseeing Included: Private premium airport-to-sanctuary transfer, Cape Panwa coastal path orientation. Evening Experience: Mindful beach walk followed by a starlit welcome dinner featuring organic ingredients."
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Beachfront Private Pool Villa Resort)',
                    'Meals Included: Curated Organic Farm-to-Table Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PRIVATE YACHT TO RACHA YAI ISLAND',
                (
                    "AZURE HORIZONS – CRYSTAL WATERS, REEF SNORKELING & CHAMPAGNE SAILING Wake up to a gorgeous morning over the ocean and enjoy a lavish buffet breakfast. Today hosts the ultimate centerpiece of your Best Phuket Tour Package: an exclusive private yacht charter to Racha Yai Island, celebrated for its pure turquoise waters and highly searched reef snorkeling zones. Avoid all commercial passenger boats as your private luxury yacht glides smoothly over deep blue waters, offering an incredible photography point. Swim and snorkel hand-in-hand through the clear water among vibrant marine ecosystems, absorbing the natural energy of the Andaman Sea. Savor a magnificent gourmet lunch prepared fresh onboard by your personal crew and paired with fine vintage wines. Spend your afternoon relaxing on a secluded white-sand sandbar before sailing back under a glorious golden sunset, a perfect premium experience. Sightseeing Included: Private Luxury Yacht cruise, Racha Yai Island marine access, reef snorkeling, white-sand sandbar. Optional Activities: Professional drone couples' photography session on the yacht deck with the open sea backdrop. Wine"
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Beachfront Private Pool Villa Resort)',
                    'Meals Included: International Buffet Breakfast & Onboard Luxury Yacht Gourmet Picnic Lunch with Vintage',
                ],
            ),
            _day(
                3,
                'CULTURAL HERITAGE & SPA REJUVENATION',
                (
                    'BIG BUDDHA PANORAMA, OLD TOWN ARCHITECTURE & DETOX RITUALS Savor a beautiful morning breakfast before launching into a slow-paced Phuket Sightseeing cultural day. Your private chauffeur navigates your group up the Nakkerd Hills to stand at the base of the majestic 45- meter Big Buddha monument—consistently named a top popular Instagram location. The peak offers a staggering 360-degree panorama of Chalong Bay, perfect for a high-fashion group photography session. Continue your premium tour to Wat Chalong, Phuket’s most revered Buddhist monastery, and explore the charming Sino-Portuguese colonial mansions of Old Phuket Town. Walk past beautiful mansions, vibrant street murals, and artisan boutiques. Return to the resort for an intense spa experience: a 150-minute traditional Thai massage followed by a therapeutic detox body wrap side-by-side, leaving your bodies fully refreshed. Sightseeing Included: The Big Buddha monument, Wat Chalong Temple, Old Phuket Town Heritage District. Evening Experience: A relaxed romantic walk through the upscale resort beachfront.'
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Beachfront Private Pool Villa Resort)',
                    'Meals Included: International Buffet Breakfast & Local Thai Fine Dining Lunch',
                ],
            ),
            _day(
                4,
                'PHANG NGA BAY SEA CAVE CANOEING',
                (
                    'MYSTICAL LAGOONS, LIMESTONE MONOLITHS & JAMES BOND ISLAND Dedicate your morning to deep geological exploration and spectacular landscapes. After a beachside breathing workshop, transfer to the pier where a premium speed-craft takes your group across Phang Nga Bay. Cruise past hundreds of vertical limestone karsts rising dramatically out of the calm sea, a prominent highlight of Phuket Sightseeing. Arrive at James Bond Island, an iconic attraction, and capture fantastic pictures in front of the floating rock monolith. Next, enjoy a relaxing canoeing experience guided through the mystical sea caves and hidden mangrove lagoons of Koh Hong, completely enclosed by massive vertical limestone walls. Savor a fresh seafood lunch at the unique stilted floating village of Koh Panyee before returning to the resort base. Sightseeing Included: James Bond Island, Phang Nga Bay speed-craft transit, Koh Hong sea cave canoeing, Koh Panyee. Optional Activities: A private helicopter flight over the limestone karsts of the bay for an incredible birds-eye view.'
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Beachfront Private Pool Villa Resort)',
                    'Meals Included: International Buffet Breakfast & Koh Panyee Healthy Seafood Lunch',
                ],
            ),
            _day(
                5,
                'HOLISTIC WELLNESS & PRIVATE GRAND FINALE',
                (
                    "HYDROTHERAPY LABYRINTHS & A SIGNATURE BEACH COVE CELEBRATION Dedicate today to complete personalized rest and fluid hydro-healing. Start your morning with a beautiful premium floating breakfast served right inside your private infinity pool villa. Spend your day navigating the resort's thermal hydrotherapy labyrinths, steam caves, and cold-plunge pools under expert guidance, finalizing your wellness tracks. Return to your villa to refresh for your final night. TRAGUIN has arranged our ultimate signature romantic highlight: an intimate, completely private beachfront candlelight dinner barbecue set in a secluded cove of the resort. Toast your holiday with a glass of organic fine wine under a starlit sky as gentle waves roll in, celebrating a collection of unforgettable memories. Sightseeing Included: Thermal Hydrotherapy Park access, private beach cove reservation. Evening Experience: Signature TRAGUIN Grand Finale Private Beachfront Candlelight Dinner under the stars."
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Beachfront Private Pool Villa Resort)',
                    'Meals Included: Premium Floating Villa Breakfast & 5-Course Beachside Finale Dinner',
                ],
            ),
            _day(
                6,
                'PHUKET SHOPPING & DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER ALIGNED Savor your final morning wellness breakfast at your villa veranda, taking a final round of photos across the tropical landscaped gardens. Take your time packing while our on-ground concierge team coordinates with hotel reception to manage your seamless checkout and handle luggage logistics. Depending on your flight departure schedule, your private vehicle remains available for last-minute boutique seaside cafe. Your private vehicle delivers your group safely to Phuket International Airport for your departure flight back home. Your premium Luxury Phuket Holiday concludes beautifully, leaving your bodies fully refreshed and aligned, with stories crafted to perfection by TRAGUIN. Sightseeing Included: Central Phuket Floresta shopping access, private luxury airport departure transfer.'
                ),
                [
                    'shopping: for traditional Thai silk items or organic essential oils at Central Phuket Floresta, or a brief stop at a',
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Amatara Welleisure Resort Bay View Suite Complimentary Physical Consultation & 1 Signature Hammam Voucher',
                'Multi-city Thailand',
                '6N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Amatara Welleisure Resort Bay View Suite Complimentary Physical Consultation & 1 Signature Hammam Voucher',
            ),
            _hotel(
                'The Slate Phuket (Nai Yang) Pearl Bed Suite Welcome Fruit Basket, Free Coqoon Spa Ritual & Yoga Access',
                'Multi-city Thailand',
                '6N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — The Slate Phuket (Nai Yang) Pearl Bed Suite Welcome Fruit Basket, Free Coqoon Spa Ritual & Yoga Access',
            ),
            _hotel(
                'Banyan Tree Phuket (Laguna) Banyan Pool Villa Complimentary Floating Breakfast Setup & Daily Well- Being Activities',
                'Multi-city Thailand',
                '6N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Banyan Tree Phuket (Laguna) Banyan Pool Villa Complimentary Floating Breakfast Setup & Daily Well- Being Activities',
            ),
            _hotel(
                'Amanpuri Phuket / Thanyapura Wellness Ocean View Pavilion / Pool Villa Premium Vintage Champagne Bottle, Private Personal Trainer & 24/7 Butler Care',
                'Multi-city Thailand',
                '6N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Amanpuri Phuket / Thanyapura Wellness Ocean View Pavilion / Pool Villa Premium Vintage Champagne Bottle, Private Persona',
            )
        ],
        inclusions=[
            _inc_included('Handpicked premium accommodation as per selected hotel tier', 1),
            _inc_included('Private luxury vehicle transfers and sightseeing as per itinerary', 2),
            _inc_included('Daily buffet breakfast and curated meals as specified', 3),
            _inc_included('VIP airport fast-track reception and dedicated TRAGUIN concierge support', 4),
            _inc_excluded('PACKAGE INCLUSIONS', 5),
        ],
    )
    return package, itinerary

def build_th_037(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-037'
    tour_code = 'TRG-BKK-HHQ-FAM-2026'
    title = 'BANGKOK HUA HIN FAMILY PACKAGE Bangkok • Grand Palace • Hua Hin Beach • Maruekhathaiyawan Palace'
    duration = '05 Nights / 06 Days'
    slug = 'th-037-bangkok-hua-hin-family-package-bangkok-grand-palace-hua-hin-beach-maruekhathaiyawan-palace'
    itin_slug = 'th-037-bangkok-hua-hin-family-package-bangkok-grand-palace-hua-hin-beach-maruekhathaiyawan-palace-itinerary'
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
            _ph('Serial code TH-037 | TRAGUIN tour code TRG-BKK-HHQ-FAM-2026', 1),
            _ph('State / Country: Thailand | Category: Best Bangkok Hua Hin Family Tour', 2),
            _ph('Destinations: Bangkok (2N) + Hua Hin', 3),
            _ph('Ideal for: Families, Multi- generational Groups, History Lovers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Safe Luxury Van (Toyota Commuter / Majestic) / Buffet Breakfast (CP) & Private Seaside Family Dinners Combine the dynamic energy of Bangkok with the regal coastal serenity of Hua Hin with the', 7),
            _ph('TRAGUIN Signature Experience: Private custom city and coastal luxury transits, completely avoiding', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 9),
            _ph('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 10),
            _ph('Luxury Transportation: Executive modern vehicles equipped with cooling, on-board entertainment', 11)
        ],
        moods=['Family', 'Honeymoon', 'Culture'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='BANGKOK HUA HIN FAMILY PACKAGE Bangkok',
        overview="Bangkok • Grand Palace • Hua Hin Beach • Maruekhathaiyawan Palace 05 Nights / 06 Days Premium Family Tour Vacation SERIAL CODE: TH-037 TRAGUIN TOUR CODE: TRG-BKK-HHQ- FAM-2026 STATE / COUNTRY: Thailand CATEGORY: Best Bangkok Hua Hin Family Tour DURATION: 05 Nights / 06 Days DESTINATIONS COVERED: Bangkok (2N) + Hua Hin (3N) IDEAL FOR: Families, Multi- generational Groups, History Lovers BEST SEASON: November to April (Pleasant Coastal Skies) VEHICLE TYPE: Private Safe Luxury Van (Toyota Commuter / Majestic) MEAL PLAN: Buffet Breakfast (CP) & Private Seaside Family Dinners Combine the dynamic energy of Bangkok with the regal coastal serenity of Hua Hin with the Best Bangkok Hua Hin Family Tour Package, masterfully curated by TRAGUIN to bring your family closer together. This spectacular Bangkok Hua Hin Family Tour balances world-class metropolitan shopping, historical exploration, and premium royal-style seaside stays, creating unforgettable memories across breathtaking landscapes.\n\nTOUR OVERVIEW\nWelcome to your meticulously designed Bangkok Hua Hin Family Vacation, a journey structured for families who expect seamless coordination, children-friendly exploration paces, and elite hospitality layouts. Across 6 wonderful days, your family will explore the finest royal palaces, vibrant night markets, and pristine white-sand beaches of Thailand. TRAGUIN Curated Experience Note: We ensure absolute comfort at every milestone. Traveling in private, air-conditioned luxury vans with dedicated chauffeurs allows your family to completely bypass all public transport lines. Backed by handpicked premium hotels and pre-vetted family dining paths, your group will experience a flawless trip protected by our 24/7 dedicated local concierge assistance. THE ALLURE OF A PREMIUM BANGKOK HUA HIN FAMILY HOLIDAY Bangkok and Hua Hin provide the perfect coastal escape and urban heritage mix for a family vacation, pairing deep royal history with pristine gulf beach relaxation. Choosing one of our high-end TRAGUIN Thailand Packages or an exceptional Bangkok Family Tour means stepping past generic travel routes into a world of exclusive benefits. This proposal targets top searched tourism keywords for Google ranking, ensuring the ultimate showcase of Bangkok Sightseeing and Hua Hin Sightseeing wonders. Discover Top Tourist Places in Thailand: the historic golden spires of Bangkok's temples, the royal beach pathways of Hua Hin, and the vibrant local evening bazaars. It is universally recognized as the Best Time to Visit Thailand to explore popular Instagram locations, engage in safe children-friendly coastal activities, source artisan handicrafts, and collect deep, immersive experiences that define a truly Premium Thailand Experience. TRAGUIN Family Signatures: Private guided tours of Bangkok's Grand Palace, front-row premium tables at local festive shows, a full-day Hua Hin royal heritage expedition, and dedicated luxury van transfers. THE DEFINITIVE DAY-WISE ITINERARY",
        seo_title='TH-037 | BANGKOK HUA HIN FAMILY PACKAGE Bangkok | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-037 / TRG-BKK-HHQ-FAM-2026): Bangkok (2N) + Hua Hin with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BANGKOK & RIVERFRONT WELCOME', 1),
            _ih('Day 02: BANGKOK ROYAL HERITAGE & ICONSIAM', 2),
            _ih('Day 03: BANGKOK TO HUA HIN COASTAL RETREAT', 3),
            _ih('Day 04: HUA HIN ROYAL HERITAGE & BOTANICAL EXPLORATION', 4),
            _ih('Day 05: HUA HIN WATERPARK FAMILY FUN', 5),
            _ih('Day 06: HUA HIN DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private custom city and coastal luxury transits, completely avoiding', 7),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium family hotels located in secure oceanfront', 8),
            _ih('Personalized Assistance: English-fluent dedicated local guides to manage reservation priorities,', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BANGKOK & RIVERFRONT WELCOME',
                (
                    'WELCOME TO THE CITY OF ANGELS – URBAN GLAMOUR BEGINS Your spectacular Bangkok Hua Hin Family Tour begins perfectly the moment your family arrives at Bangkok’s Suvarnabhumi International Airport. Receive our VIP reception, coordinated seamlessly by your dedicated TRAGUIN tour representative. Step into your air-conditioned private luxury van, ensuring a completely relaxed transfer straight to your handpicked premium riverside resort. Check into your spacious family suite, featuring special welcome amenities. Spend the afternoon unwinding by the massive lagoon swimming pool or taking your first family photos overlooking the sunset. In the evening, your private vehicle takes you to a premium restaurant for a welcome buffet dinner filled with familiar comforts, ensuring a restful start for an unforgettable family vacation. Sightseeing Included: Private luxury van airport transit, scenic Bangkok riverfront orientation. Evening Experience: Family welcome dinner at an upscale restaurant with gorgeous river vistas.'
                ),
                [
                    'Overnight Stay: Bangkok (Premium Lifestyle Family Hotel)',
                    'Meals Included: Curated Multi-Cuisine Family Welcome Dinner',
                ],
            ),
            _day(
                2,
                'BANGKOK ROYAL HERITAGE & ICONSIAM',
                (
                    "GOLDEN SIAMESE ARCHITECTURE & WORLD-CLASS WATERFRONT SHOPPING Savor a magnificent buffet breakfast before starting a descriptive Bangkok Sightseeing cultural tour. Your private chauffeur navigates your family to the walled Grand Palace complex. Admire the stunning gold-leaf spires and explore the sacred Temple of the Emerald Buddha (Wat Phra Kaew). Continue to Wat Pho to stand before the monumental 46-meter Reclining Buddha, perfect for iconic family portraits. In the afternoon, proceed to ICONSIAM, the crown jewel of Bangkok's shopping malls. Featuring an indoor floating market, massive luxury brand flagship stores, and phenomenal waterfront spaces, it is an unparalleled location for premium shopping. Find unique silk garments, boutique cosmetics, and local designer items. Return to your resort for an evening of leisure or explore local night markets. Sightseeing Included: Grand Palace, Wat Phra Kaew, Wat Pho, ICONSIAM Luxury Waterfront Mall. Optional Activities: Traditional wooden longtail boat tour through the historic Thonburi canal networks."
                ),
                [
                    'Overnight Stay: Bangkok (Premium Lifestyle Family Hotel)',
                    'Meals Included: International Buffet Breakfast & Traditional Thai Fine Dining Lunch',
                ],
            ),
            _day(
                3,
                'BANGKOK TO HUA HIN COASTAL RETREAT',
                (
                    'ROYAL COASTAL ESCAPE – SCENIC HIGHWAY TRANSIT TO HUA HIN Enjoy your morning breakfast before checking out. Your private luxury van picks your family up for a smooth, scenic journey along the Gulf of Thailand coastline towards the royal resort town of Hua Hin. Hua Hin is adored globally for its quiet coastal charm and historic royal villas, making it an essential chapter for your Bangkok Hua Hin Family Tour. Arrive at your premium beachfront resort and check into your family-friendly suite. Spend your afternoon unwinding by the pool or taking a slow walk along the white sand beach. In the evening, explore the famous Hua Hin Night Market, packed with authentic street cafes, artisan shops, and local food recommendations, perfect for picking up handcrafted souvenirs. Sightseeing Included: Cross-province scenic luxury drive, Hua Hin beach orientation walk. Evening Experience: Family walk through the lively night bazaar for local food tasting.'
                ),
                [
                    'Overnight Stay: Hua Hin (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Seaside Family Dinner',
                ],
            ),
            _day(
                4,
                'HUA HIN ROYAL HERITAGE & BOTANICAL EXPLORATION',
                (
                    'PALACES, ARTISAN MARKETS & ROYAL-STYLE SEASIDE RELAXATION Dedicate your morning to deep history. Your private chauffeur transfers you to the Maruekhathaiyawan Palace, the beautiful "Palace of Love and Hope," an intricate wooden structure built by King Rama VI featuring stunning royal garden landscapes—a prominent highlight of Hua Hin Sightseeing. Continue to the Hua Hin Railway Station, a colorful historical landmark perfect for family photography. After a gourmet seafood lunch, explore the nearby Cicada Market, a high-fashion, open-air bazaar showcasing local artist crafts and unique handmade accessories. Return to your resort to refresh for your evening. TRAGUIN has arranged our ultimate signature surprise: an intimate private beachfront dinner barbecue set in a secluded cove of the resort. Sightseeing Included: Maruekhathaiyawan Palace, Hua Hin Railway Station, Cicada Market. Evening Experience: Signature TRAGUIN Grand Finale Private Beachfront Candlelight Barbecue Dinner.'
                ),
                [
                    'Overnight Stay: Hua Hin (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & 5-Course Beachside Finale Dinner',
                ],
            ),
            _day(
                5,
                'HUA HIN WATERPARK FAMILY FUN',
                (
                    'THRILLING SLIDES, WAVE POOLS & LAST-MINUTE COASTAL TREASURES Dedicate today to pure, high-octane family joy at the Vana Nava Water Jungle—Asia’s first environmentally friendly water jungle park. Following a hearty breakfast, your private luxury van drops your group at the entrance gates with pre-arranged fast-track tickets. Step into highly immersive zones packed with world-class water slides, thrilling water coasters, and a massive wave pool. After a day of exhilarating water sports, spend your late afternoon exploring boutique shopping arcades near the beach. For your final evening, celebrate with an elegant seaside dinner, allowing you to toast to an extraordinary family holiday under a starlit sky. Sightseeing Included: Full-day admission pass to Vana Nava Water Jungle, boutique coastal shopping access. Evening Experience: Grand finale seaside dinner party featuring traditional music.'
                ),
                [
                    'Overnight Stay: Hua Hin (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Seaside Family Farewell Dinner',
                ],
            ),
            _day(
                6,
                'HUA HIN DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER UNITED Enjoy your final morning breakfast at your premium resort, capturing a final round of group family photos across the tropical landscaped gardens. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless checkout. Your private luxury van arrives to transfer your party comfortably to Bangkok International Airport for your departure flight back home. Your premium Bangkok Hua Hin Family Tour concludes beautifully, leaving your loved ones with unforgettable memories crafted to perfection by TRAGUIN. Sightseeing Included: Private luxury van airport departure transfer.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Sukosol Bangkok Premier Family Room Novotel Hua Hin Resort Superior Ocean Suite',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — The Sukosol Bangkok Premier Family Room Novotel Hua Hin Resort Superior Ocean Suite',
            ),
            _hotel(
                'Grande Centre Point Terminal 21 Premium Deluxe Suite Amari Hua Hin Deluxe Garden Family Room',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Grande Centre Point Terminal 21 Premium Deluxe Suite Amari Hua Hin Deluxe Garden Family Room',
            ),
            _hotel(
                'Avani+ Riverside Bangkok Avani Panorama Family Suite Centara Grand Beach Resort Hua Hin Deluxe Ocean Face Room',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Avani+ Riverside Bangkok Avani Panorama Family Suite Centara Grand Beach Resort Hua Hin Deluxe Ocean Face Room',
            ),
            _hotel(
                'Shangri-La Bangkok Horizon Club Family Room InterContinental Hua Hin Resort Premium Suite / Pool Villa',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Shangri-La Bangkok Horizon Club Family Room InterContinental Hua Hin Resort Premium Suite / Pool Villa',
            )
        ],
        inclusions=[
            _inc_included('Airfare: International flight tickets from your home country to Thailand.', 1),
            _inc_excluded('PACKAGE INCLUSIONS', 2),
        ],
    )
    return package, itinerary

def build_th_038(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-038'
    tour_code = 'TRG-HKT-SR-2026'
    title = 'PHUKET LEISURE RETREAT Phuket Beachfront • Old Town Heritage • Scenic Bay Cruises • Botanical Gardens'
    duration = '05 Nights / 06 Days'
    slug = 'th-038-phuket-leisure-retreat-phuket-beachfront-old-town-heritage-scenic-bay-cruises-botanical-gardens'
    itin_slug = 'th-038-phuket-leisure-retreat-phuket-beachfront-old-town-heritage-scenic-bay-cruises-botanical-gardens-itinerary'
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
            _ph('Serial code TH-038 | TRAGUIN tour code TRG-HKT-SR-2026', 1),
            _ph('State / Country: Thailand | Category: Senior Citizen Leisure Tour', 2),
            _ph('Destinations: Phuket Island Coastal', 3),
            _ph('Ideal for: Senior Citizens, Relaxed Travelers, Gentle Pacing', 4),
            _ph('Best season: November to May (Ideal Dry, Comfortable Weather)', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Executive Van (Easy Access) / Buffet Breakfast (CP) & Gentle Seafood/ Continental Dining Experience the timeless tranquility of the Andaman Coast with the Best Phuket Tour Package for s', 7),
            _ph('TRAGUIN Signature Experience: Private custom leisure itineraries, completely avoiding standard', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified premium luxury resorts featuring flat-floor access,', 9),
            _ph('Personalized Assistance: English-fluent dedicated local coordinators to manage group priorities and', 10),
            _ph('Luxury Transportation: Executive modern vans equipped with special suspension, medical-first-aid', 11)
        ],
        moods=['Culture', 'Beach', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='PHUKET LEISURE RETREAT Phuket Beachfront',
        overview='05 Nights / 06 Days Optimized Leisure & Rejuvenation Tour SERIAL CODE: TH-038 TRAGUIN TOUR CODE: TRG-HKT-SR-2026 STATE / COUNTRY: Thailand CATEGORY: Senior Citizen Leisure Tour DURATION: 05 Nights / 06 Days DESTINATIONS COVERED: Phuket Island Coastal Sanctuary (5 Nights) IDEAL FOR: Senior Citizens, Relaxed Travelers, Gentle Pacing BEST SEASON: November to May (Ideal Dry, Comfortable Weather) VEHICLE TYPE: Private Luxury Executive Van (Easy Access) MEAL PLAN: Buffet Breakfast (CP) & Gentle Seafood/ Continental Dining Experience the timeless tranquility of the Andaman Coast with the Best Phuket Tour Package for seniors, thoughtfully curated by TRAGUIN to combine comfortable pace, cultural heritage, and scenic beauty. This gentle Luxury Phuket Holiday focuses on ease of movement, premium stays, and unforgettable memories within a peaceful island setting.\n\nTOUR OVERVIEW\nWelcome to your bespoke Phuket Leisure Retreat, a gracefully designed holiday structured explicitly for senior travelers who prioritize ease, comfort, safety, and cultural enrichment. Across 6 majestic days, your journey explores gentle marine landscapes, historical architecture, and the rich cultural fabric of Phuket, all managed with the utmost care and professional support from TRAGUIN Experts. TRAGUIN Curated Experience Note: We understand the importance of a relaxed, stress-free tempo. Our itinerary is optimized with spacious vehicles featuring easy-access steps, handpicked hotels with flat-floor TRAGUIN Leisure Retreats • accessibility, and pre-vetted dining paths accommodating specific dietary needs. Our 24/7 senior-specialist concierge team ensures your comfort is protected at every milestone.\n\nWHY CHOOSE OUR PHUKET SENIOR LEISURE PACKAGE?\nPhuket is globally beloved for its perfect blend of serene coastal beauty, fascinating colonial architecture, and world-class healthcare infrastructures, making it the perfect sanctuary for senior travelers. Orchestrating your retreat through a specialized TRAGUIN Destination Package guarantees a beautifully run, relaxed operation. This proposal integrates targeted tourism keywords for Google ranking, presenting an impeccable layout of premier Phuket Sightseeing wonders designed for comfort. Expose your group to the Top Tourist Places in Thailand: the peaceful golden spires of Wat Chalong, the quiet colonial heritage lanes of Old Phuket Town, and the breathtaking sunset panoramas of cape view locations. It is widely recognized as the Best Time to Visit Thailand to enjoy gentle cultural experiences, capture iconic architecture for photography, and enjoy a genuinely rewarding Premium Thailand Experience. TRAGUIN Wellness & Accessibility Features: Priority group assistance at all landmark entrances, private climate-controlled executive vans, handpicked accessible resort venues, and 24/7 dedicated senior-specialist support. TRAGUIN Leisure Retreats • THE GENTLE & IMMERSIVE DAY-WISE ITINERARY',
        seo_title='TH-038 | PHUKET LEISURE RETREAT Phuket Beachfront | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-038 / TRG-HKT-SR-2026): Phuket Island Coastal with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN PHUKET & COASTAL WELCOME', 1),
            _ih('Day 02: PHUKET CULTURAL ORIENTATION TOUR', 2),
            _ih('Day 03: SCENIC BAY CRUISING & SUNSET VIEWS', 3),
            _ih('Day 04: BOTANICAL WONDERS & ARTISAN MARKETS', 4),
            _ih('Day 05: LEISURE RETREAT & FAREWELL GALA', 5),
            _ih('Day 06: DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private custom leisure itineraries, completely avoiding standard', 7),
            _ih('Curated by TRAGUIN Experts: Safety-verified premium luxury resorts featuring flat-floor access,', 8),
            _ih('Personalized Assistance: English-fluent dedicated local coordinators to manage group priorities and', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN PHUKET & COASTAL WELCOME',
                (
                    'THE ISLAND WELCOME – SEAMLESS TRANSIT TO YOUR COASTAL SANCTUARY Your spectacular Phuket Leisure Retreat begins flawlessly the moment your group lands at Phuket International Airport. Receive a warm, organized welcome managed directly by your senior-specialist TRAGUIN tour director. Our staff handles all baggage logistics as you are guided to a spacious, air- conditioned private executive luxury van, ensuring a comfortable transit directly to your peaceful resort. Check into your premium, accessible resort suite. Spend your afternoon unwinding in the lush tropical gardens or relaxing by the quiet poolside. In the evening, enjoy a curated, gentle welcome dinner at the resort, allowing you to settle in comfortably for the relaxing itinerary ahead. Sightseeing Included: Group airport logistics management, scenic island drive. Evening Experience: Relaxed group welcome dinner at a tranquil resort oceanfront space. TRAGUIN Leisure Retreats •'
                ),
                [
                    'Overnight Stay: Phuket (Premium Accessible Beachfront Resort)',
                    'Meals Included: Curated International Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PHUKET CULTURAL ORIENTATION TOUR',
                (
                    'SPIRITUAL HERITAGE – WAT CHALONG & OLD TOWN ARCHITECTURE Fuel up with a bountiful, nutrient-rich buffet breakfast. Today showcases the cultural grandeur of Phuket at a comfortable, leisurely pace. Your luxury group coach transfers you to the historic Wat Chalong, Phuket’s most revered Buddhist monastery, adorned with intricate golden architecture, perfect for peaceful group reflection and photography. Continue to Old Phuket Town, where you can stroll along flat walkways to admire beautiful Sino-Portuguese colonial mansions and vibrant street murals. This historical quarter is perfect for artisan shopping and gentle cultural discovery. Return to the resort for an afternoon of leisure, perhaps enjoying a therapeutic foot reflexology session, before a relaxed dinner. Sightseeing Included: Wat Chalong monastery, Old Phuket Town colonial architecture walk. Optional Activities: A visit to a nearby premium Thai silk boutique or herb gallery.'
                ),
                [
                    'Overnight Stay: Phuket (Premium Accessible Beachfront Resort)',
                    'Meals Included: International Breakfast & Traditional Thai Bistro Lunch',
                ],
            ),
            _day(
                3,
                'SCENIC BAY CRUISING & SUNSET VIEWS',
                (
                    "THE CALM WATERS – BAY SAILING & COASTAL PANORAMA Enjoy a relaxed morning breakfast. Today features a gentle marine experience: a private, stable bay-cruising vessel charter tailored for comfort. Glide across the calm waters of Phuket's coastline to witness the dramatic limestone cliffs from a stable, comfortable vantage point, skipping any high-speed turbulence. The afternoon offers a scenic drive to the famous Karon Viewpoint, where you can capture incredible by the ocean, observing the sunset over the horizon while enjoying your favorite refreshments. Sightseeing Included: Private bay-cruising vessel, Karon Viewpoint. Evening Experience: Relaxed seaside evening enjoying the gentle ocean breeze. TRAGUIN Leisure Retreats •"
                ),
                [
                    'photography points: across three stunning beaches. Return to your resort for an evening of gentle relaxation',
                    'Overnight Stay: Phuket (Premium Accessible Beachfront Resort)',
                    'Meals Included: International Breakfast & Seaside Light Lunch',
                ],
            ),
            _day(
                4,
                'BOTANICAL WONDERS & ARTISAN MARKETS',
                (
                    'TROPICAL FLORA – THE BOTANICAL VALLEYS & CULTURAL ARTISTRY Dedicate your morning to lush natural beauty. Following breakfast, your private van transfers the group to one of the most stunning popular Instagram locations: the local botanical gardens. This massive tropical valley showcases spectacular floral arrangements, perfect for gentle walking and photography, all managed comfortably at your own pace. In the afternoon, explore a local artisan market renowned for delicate handcrafted souvenirs, high-quality Thai silk fabrics, and traditional wooden art. It is the perfect spot for leisurely shopping. Conclude the day with a group dinner, sharing stories of your journey so far. Sightseeing Included: Botanical gardens entry, local artisan shopping bazaar. Evening Experience: Group dinner sharing stories and cultural insights.'
                ),
                [
                    'Overnight Stay: Phuket (Premium Accessible Beachfront Resort)',
                    'Meals Included: International Breakfast & Garden-view Lunch',
                ],
            ),
            _day(
                5,
                'LEISURE RETREAT & FAREWELL GALA',
                (
                    "RESTORATION & CHERISHING UNFORGETTABLE MEMORIES Enjoy a final buffet breakfast before a day devoted to total relaxation at your leisure. The resort's pristine facilities, spa, and library are yours to explore. This time is perfectly suited for taking final group photos or enjoying a final beachside walk at your own pace. In the evening, celebrate with a special farewell gala dinner party, raised to toast an extraordinary journey. Look back on an exceptional collection of curated experiences, breathtaking landscapes, and unforgettable memories crafted beautifully by TRAGUIN. Sightseeing Included: Leisure schedule, final group photo session. Evening Experience: Grand farewell gala dinner celebration. TRAGUIN Leisure Retreats •"
                ),
                [
                    'Overnight Stay: Phuket (Premium Accessible Beachfront Resort)',
                    'Meals Included: International Breakfast & Farewell Dinner',
                ],
            ),
            _day(
                6,
                'DEPARTURE',
                (
                    'CHERISHING MEMORIES – FOREVER UNITED Savor your final morning breakfast at your premium resort. Our on-ground concierge team coordinates with the hotel to manage seamless check-out and handle all luggage logistics for the group. At the designated hour, your luxury van transfers your party comfortably to Phuket International Airport for your departure flight. Your premium Phuket Leisure Retreat concludes perfectly. Sightseeing Included: Private luxury van airport transfer, luggage assistance.'
                ),
                [
                    'Meals Included: International Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Phuket Resort Deluxe Garden Rooms Complimentary Welcome Drinks & Accessibility Assistance',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Novotel Phuket Resort Deluxe Garden Rooms Complimentary Welcome Drinks & Accessibility Assistance',
            ),
            _hotel(
                'Phuket Marriott, Merlin Beach Premium Ocean View Rooms Welcome Fruit Platters, Free Resort Activity Vouchers',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Phuket Marriott, Merlin Beach Premium Ocean View Rooms Welcome Fruit Platters, Free Resort Activity Vouchers',
            ),
            _hotel(
                'Banyan Tree Phuket Luxury Pool Villa Complimentary Daily Afternoon Tea & Butler Care',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Banyan Tree Phuket Luxury Pool Villa Complimentary Daily Afternoon Tea & Butler Care',
            ),
            _hotel(
                'Amanpuri Phuket Ocean View Pavilion Premium Vintage Champagne, Private Beach Access & 24/7 Butler Care',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Amanpuri Phuket Ocean View Pavilion Premium Vintage Champagne, Private Beach Access & 24/7 Butler Care',
            )
        ],
        inclusions=[
            _inc_included('Flights: International flight tickets connecting home country with Phuket.', 1),
            _inc_excluded('PACKAGE INCLUSIONS', 2),
        ],
    )
    return package, itinerary

def build_th_039(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-039'
    tour_code = 'TRG-THA-WAT-2026'
    title = 'Phuket • Phi Phi Islands • Phang Nga Bay • Coral Island • High-Octane Action'
    duration = '05 Nights / 06 Days'
    slug = 'th-039-phuket-phi-phi-islands-phang-nga-bay-coral-island-high-octane-action'
    itin_slug = 'th-039-phuket-phi-phi-islands-phang-nga-bay-coral-island-high-octane-action-itinerary'
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
            _ph('Serial code TH-039 | TRAGUIN tour code TRG-THA-WAT-2026', 1),
            _ph('State / Country: Thailand | Category: Adventure / Water Sports Tour', 2),
            _ph('Destinations: Thailand', 3),
            _ph('Ideal for: Thrill Seekers, Active Travelers, Adventure Lovers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury SUV & Exclusive High-Speed Marine Craft / Buffet Breakfast (CP), Beachfront Barbecues & Seafood Fine Dining Dive into the ultimate aquatic thrill with the Best Thailand Water Sports Tou', 7)
        ],
        moods=['Honeymoon', 'Beach', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Phuket',
        overview="TOUR OVERVIEW\nWelcome to your definitive Thailand Water Sports expedition, an immersive 6-day journey engineered by TRAGUIN Experts for active adventurers. Experience elite high-speed marine explorations, deep-sea snorkeling over live coral reefs, sea-cave kayaking adventures, and cliff-scaling thrills. TRAGUIN Adventure Expeditions • TRAGUIN Curated Experience Note: Your safety and performance are our benchmarks. This active itinerary features professional PADI-certified guides, top-tier private high-speed marine crafts, priority fast-track entry into national marine reserves, and 24/7 dedicated local concierge assistance to manage every high-octane detail. THE EPIC APPEAL OF THAILAND WATER SPORTS Thailand’s marine landscape is a masterpiece of nature, attracting adventurers globally to its turquoise waters and hidden limestone caverns. Selecting a specialized Thailand Water Sports Tour Package through TRAGUIN guarantees private access to elite reefs and untouched coves. This proposal utilizes top searched tourism keywords to ensure the ultimate layout of Thailand Sightseeing highlights. Explore the world's most coveted marine highlights: the stunning vertical karsts of the Phi Phi Islands, the crystalline coves of Coral Island, and the mystical mangrove channels of Phang Nga Bay. It is the absolute Best Time to Visit Thailand to discover popular Instagram locations from a unique vantage point on the water, try deep-sea snorkeling, and indulge in a truly unforgettable luxury holiday. TRAGUIN Adventure Signatures: Private high-speed yacht charter for multi-island hopping, expert-led kayaking in secluded sea caves, tandem parasailing above the Andaman Sea, and a signature sunset beach barbecue on a private sandbar. TRAGUIN Adventure Expeditions • THE HIGH-OCTANE DAY-WISE ITINERARY",
        seo_title='TH-039 | Phuket | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Thailand package (TH-039 / TRG-THA-WAT-2026): Thailand with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN PHUKET & COASTAL ORIENTATION', 1),
            _ih('Day 02: PHI PHI ISLANDS MARINE EXPEDITION', 2),
            _ih('Day 03: PHANG NGA BAY SEA-CAVE CANOEING', 3),
            _ih('Day 04: CORAL ISLAND AQUATIC ADRENALINE', 4),
            _ih('Day 05: CULTURE & PRIVATE COVE GALA', 5),
            _ih('Day 06: PHUKET DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN PHUKET & COASTAL ORIENTATION',
                (
                    'WELCOME TO THE EXPEDITION BASE – THE THRILL BEGINS Your ultimate Thailand Adventure Tour hits the ground running the moment you land at Phuket International Airport. Receive a premium welcome from your dedicated TRAGUIN tour manager. Step into your private luxury SUV, engineered for comfort across coastal routes, as you transfer to your ultra-luxury beachfront sanctuary. Check into your resort and gear up for an exciting afternoon of beach exploration. Your guide navigates you along the coastline for initial sightseeing, capturing magnificent photos at scenic photography points. End your day at a high-end, surf-side lounge for an exclusive welcome dinner under a pastel sunset. Sightseeing Included: Private luxury vehicle airport transit, coastal scenic orientation drive. Evening Experience: Welcome dinner party at a trendy oceanfront lounge with live fire-spinning shows.'
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: Curated Seafood Welcome Dinner',
                ],
            ),
            _day(
                2,
                'PHI PHI ISLANDS MARINE EXPEDITION',
                (
                    'PRIVATE CATAMARAN SAILING – REEFS, LAGOONS & SEA-CAVE SNORKELING Fuel up with a hearty breakfast. Today hosts a cornerstone Premium Thailand Experience: an intense marine voyage across the Andaman Sea. Avoid all public ferry crowds as TRAGUIN provides a private, high- speed catamaran to guide your group directly toward the vertical limestone amphitheaters of the Phi Phi Islands. Sail into Maya Bay, sheltered by colossal cliffs, to capture iconic group photos on the soft sands. Next, snorkel into the emerald waters of Pileh Lagoon among brilliant coral reefs. Enjoy a private gourmet picnic lunch on a secluded sandshore before exploring the Viking Cave. Sightseeing Included: Maya Bay marine access, Pileh Lagoon snorkeling, Viking Cave, Bamboo Island stop. Optional Activities: Deep-sea tandem scuba diving with PADI instruction or high-speed sea-kayaking. TRAGUIN Adventure Expeditions •'
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Beachside Island Picnic Lunch',
                ],
            ),
            _day(
                3,
                'PHANG NGA BAY SEA-CAVE CANOEING',
                (
                    'MYSTICAL LIMESTONE TOWERS & HIDDEN MANGROVE CHANNELS Prepare for an action-packed day uncovering hidden geographical wonders. After breakfast, board your private speed-craft to explore the iconic Phang Nga Bay. Cruise past hundreds of vertical limestone karsts rising dramatically out of the calm sea, a prominent highlight of Phuket Sightseeing. Anchor near Koh Hong where expert guides steer your canoes through narrow rocky arches into hidden interior sea-caves and mangrove lagoons. Next, speed towards James Bond Island to photograph the famous needle-shaped rock monolith. Enjoy a fresh seafood lunch at the stilted floating village of Koh Panyee before returning to the resort base. Sightseeing Included: James Bond Island, Koh Hong sea cave canoeing, Koh Panyee stilted village exploration. Evening Experience: Relaxing evening at a high-end cliffside lounge watching the sunset over the sea.'
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Floating Village Seafood Lunch',
                ],
            ),
            _day(
                4,
                'CORAL ISLAND AQUATIC ADRENALINE',
                (
                    'PARASAILING, BANANA BOATING & VIBRANT UNDERWATER WORLDS Dedicate today to pure aquatic thrill at Coral Island. Following breakfast, transfer by private speedboat to this marine sanctuary known for high-energy water sports. Your package includes an exhilarating tandem parasailing flight, providing breathtaking landscapes of the island coast, alongside a high-speed banana boat ride. Snorkel directly off the beach into vibrant coral channels filled with schools of tropical fish, capturing unforgettable memories with your group. Enjoy a relaxed beachside lunch before returning to the mainland for an afternoon of leisure or exploring boutique shopping centers. Sightseeing Included: Coral Island private speedboat transfer, parasailing, banana boating, reef snorkeling. Evening Experience: Exploring local artisan shops for traditional crafts and authentic Thai spices. TRAGUIN Adventure Expeditions •'
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & Beachside Barbecue Lunch',
                ],
            ),
            _day(
                5,
                'CULTURE & PRIVATE COVE GALA',
                (
                    'CULTURAL MAJESTY & A SIGNATURE BEACHFRONT CANDLELIGHT FINALE Spend your morning at leisure or explore the cultural marvels of Phuket. Visit the iconic Big Buddha monument, providing incredible panoramic photography points. For your final evening, TRAGUIN has arranged our ultimate signature highlight: an intimate, completely private beachfront candlelight dinner barbecue set in a secluded cove of the resort. Toast your adventure holiday with a glass of fine wine under a starlit sky as gentle waves roll in. Sightseeing Included: The Big Buddha monument, panoramic island viewpoint drive. Evening Experience: Signature TRAGUIN Grand Finale Private Beachfront Candlelight Barbecue Dinner.'
                ),
                [
                    'Overnight Stay: Phuket (Premium Luxury Beachfront Resort)',
                    'Meals Included: International Buffet Breakfast & 5-Course Cove Barbecue Dinner',
                ],
            ),
            _day(
                6,
                'PHUKET DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER FEARLESS Enjoy your final morning buffet breakfast at your resort, taking a final round of panoramic photos across the gardens. At the designated hour, your private luxury SUV arrives to transfer you comfortably to Phuket International Airport for your departure flight back home. Your premium Thailand Water Sports tour concludes beautifully, leaving your heart full of unforgettable memories and stories crafted to perfection by TRAGUIN. Sightseeing Included: Private luxury airport departure transfer.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                    'Optional Activities: Deep-sea tandem scuba diving',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Phuket Resort Superior Ocean View Room',
                'Multi-city Thailand',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Novotel Phuket Resort Superior Ocean View Room',
            ),
            _hotel(
                'Phuket Marriott Resort, Merlin Beach Pool View Luxury Room TRAGUIN Adventure Expeditions •',
                'Multi-city Thailand',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Phuket Marriott Resort, Merlin Beach Pool View Luxury Room TRAGUIN Adventure Expeditions •',
            ),
            _hotel(
                'The Westin Siray Bay Resort & Spa Luxury Seaview Suite',
                'Multi-city Thailand',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Westin Siray Bay Resort & Spa Luxury Seaview Suite',
            ),
            _hotel(
                'Trisara Phuket / Sri Panwa Resort Ocean Front Luxury Pool Villa',
                'Multi-city Thailand',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Trisara Phuket / Sri Panwa Resort Ocean Front Luxury Pool Villa',
            )
        ],
        inclusions=[
            _inc_included('Handpicked premium accommodation as per selected hotel tier', 1),
            _inc_included('Private luxury vehicle transfers and sightseeing as per itinerary', 2),
            _inc_included('Daily buffet breakfast and curated meals as specified', 3),
            _inc_included('VIP airport fast-track reception and dedicated TRAGUIN concierge support', 4),
            _inc_excluded('PACKAGE INCLUSIONS', 5),
        ],
    )
    return package, itinerary

def build_th_040(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TH-040'
    tour_code = 'TRG-THA-GRD-2026'
    title = 'GRAND THAILAND TOUR Bangkok • Chiang Mai • Phuket • Phi Phi Islands • Phang Nga Bay'
    duration = '08 Nights / 09 Days'
    slug = 'th-040-grand-thailand-tour-bangkok-chiang-mai-phuket-phi-phi-islands-phang-nga-bay'
    itin_slug = 'th-040-grand-thailand-tour-bangkok-chiang-mai-phuket-phi-phi-islands-phang-nga-bay-itinerary'
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
            _ph('Serial code TH-040 | TRAGUIN tour code TRG-THA-GRD-2026', 1),
            _ph('State / Country: Thailand | Category: Ultimate Luxury Discovery Tour', 2),
            _ph('Destinations: Bangkok (3N) + Chiang', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: November to May (Ideal Marine & Highland Weather)', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Chauffeur- Driven Luxury Sedans & Executive Vans / Buffet Breakfast (CP), Private Yacht Lunches & Michelin Fine Dining', 7)
        ],
        moods=['Luxury', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='GRAND THAILAND TOUR Bangkok',
        overview="TOUR OVERVIEW\nWelcome to your bespoke Ultimate Grand Thailand discovery, a comprehensive luxury experience designed for guests who command seamless operational perfection, absolute private security, and elite lifestyle inclusions. Across 9 spectacular days, TRAGUIN brings you a flawless mix of urban glamour, northern heritage immersion, and private marine yachting. TRAGUIN Curated Experience Note: Every phase of your holiday is actively managed by our luxury concierge desk. From pre-allocated fast-track airport arrivals to personalized chef-driven dining tracks and custom multi-destination logistics, we ensure every detail is immersive and exclusively yours.\n\nWHY CHOOSE OUR ULTIMATE GRAND THAILAND EXPERIENCE?\nThailand remains an international masterpiece of luxury travel, effortlessly combining ancient royal heritage with ultra-modern private estates and Michelin-starred culinary landscapes. Selecting one of our signature TRAGUIN Thailand Packages or an elite Thailand Honeymoon Package guarantees access to hidden domains and priority privileges. This proposal utilizes top searched tourism keywords for Google ranking, showcasing an elite layout of premier Thailand Sightseeing marvels. Uncover iconic attractions: the historical grandeur of Bangkok's Grand Palace, the misty mountain temples of Chiang Mai, and the breathtaking emerald lagoons of the Phi Phi Islands. It is widely recognized as the Best Time to Visit Thailand to experience highly sought-after popular Instagram locations, authentic local crafts, world-class wellness therapies, and collect deep, immersive experiences that define a truly Premium Thailand Experience. TRAGUIN Ultimate Luxury Exclusives: VIP fast-track airport arrivals in Bangkok, private jet-speed yacht charters to the Phi Phi Islands, an exclusive 180-minute couple's spa rejuvenation, and a grand finale beachfront candlelight gala dinner in Phuket. THE DEFINITIVE DAY-WISE ITINERARY",
        seo_title='TH-040 | GRAND THAILAND TOUR Bangkok | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days Thailand package (TH-040 / TRG-THA-GRD-2026): Bangkok (3N) + Chiang with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BANGKOK & RIVERFRONT OPULENCE', 1),
            _ih('Day 02: BANGKOK HERITAGE & ICONSIAM', 2),
            _ih('Day 03: BANGKOK TO CHIANG MAI HIGHLANDS', 3),
            _ih('Day 04: DOI SUTHEP TEMPLE & ETHICAL ELEPHANT SANCTUARY', 4),
            _ih('Day 05: CHIANG MAI TO PHUKET COASTAL FLIGHT', 5),
            _ih('Day 06: PRIVATE LUXURY YACHT TO PHI PHI ISLANDS', 6),
            _ih('Day 07: PHANG NGA BAY & JAMES BOND ISLAND', 7),
            _ih('Day 08: PHUKET RETREAT & PRIVATE FINALE', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BANGKOK & RIVERFRONT OPULENCE',
                (
                    'METROPOLITAN GLAMOUR – THE CITY OF ANGELS WELCOME Your spectacular Ultimate Thailand vacation begins the moment you touch down at Bangkok International Airport. Receive our VIP Airport Fast-Track Reception, clearing all customs and immigration procedures within minutes. Your private European sedan or luxury SUV waits to transfer you smoothly along the scenic highway to your ultra-luxury riverside resort. Check into your handpicked premium riverfront room. In the evening, dress in elegant luxury wear for a classic Premium Thailand Experience: a 5-star luxury dinner cruise aboard the Grand Pearl Cruise liner on the Chao Phraya River. Glide past the brilliantly lit Grand Palace and the luminous spires of Wat Arun while enjoying a sumptuous international buffet and live jazz music. Sightseeing Included: VIP airport fast-track clearance, luxury sedan city transfer, Chao Phraya dinner cruising. Evening Experience: 5-Star Luxury River Dinner Cruise with live jazz background entertainment.'
                ),
                [
                    'Overnight Stay: Bangkok (Ultra-Luxury Riverside Resort)',
                    'Meals Included: Premium Cruise Gala Buffet Dinner',
                ],
            ),
            _day(
                2,
                'BANGKOK HERITAGE & ICONSIAM',
                (
                    "SIAMESE SPLENDOR – GRAND PALACE & WORLD-CLASS RETAIL THERAPY Savor a magnificent buffet breakfast before embarking on a descriptive Bangkok Sightseeing cultural tour. Your private chauffeur navigates your party to the walled Grand Palace complex. Admire the golden spires and explore the sacred Temple of the Emerald Buddha. Continue to Wat Pho to stand before the monumental 46-meter Reclining Buddha. In the afternoon, proceed to ICONSIAM, the crown jewel of Bangkok's shopping malls. Featuring massive luxury brand flagship stores and phenomenal waterfront spaces, it is an unparalleled location for premium premium rooftop lounge, celebrating the city's skyline. Sightseeing Included: Grand Palace, Wat Phra Kaew, Wat Pho, ICONSIAM Luxury Waterfront Mall. Optional Activities: Mahanakhon SkyWalk glass tray adventure at 314 meters above the city skyline."
                ),
                [
                    'shopping: . Find unique silk garments and designer items. End your night with VIP tables reserved at a',
                    'Overnight Stay: Bangkok (Ultra-Luxury Riverside Resort)',
                    'Meals Included: International Buffet Breakfast & Traditional Thai Fine Dining Lunch',
                ],
            ),
            _day(
                3,
                'BANGKOK TO CHIANG MAI HIGHLANDS',
                (
                    'TRANSIT TO THE LANNA CAPITAL – MISTY PEAKS & CULTURAL CHARM Enjoy your final Bangkok breakfast before checking out. Your private vehicle transfers you to the airport for your short domestic flight to Chiang Mai. Upon arrival in the misty northern highlands, your waiting private premium vehicle provides a smooth transfer to your ultra-luxury heritage valley resort. Chiang Mai is globally celebrated for its majestic mountain spires, ancient royal heritage, and ethical animal sanctuaries. Arrive at your premium resort, detailed with a chilled complimentary bottle of premium sparkling wine. Spend your afternoon unwinding by the panoramic infinity pool or strolling through the tropical gardens, watching the horizon transform into vibrant sunset hues. Sightseeing Included: Domestic flight transit, scenic highland driving layout, resort valley walk. Evening Experience: Traditional Khantoke Royal Lanna Dinner and cultural dance show.'
                ),
                [
                    'Overnight Stay: Chiang Mai (Ultra-Luxury Heritage Valley Resort)',
                    'Meals Included: International Buffet Breakfast & Traditional Lanna Dinner Show',
                ],
            ),
            _day(
                4,
                'DOI SUTHEP TEMPLE & ETHICAL ELEPHANT SANCTUARY',
                (
                    'GOLDEN SPIRES, ETHICAL ENCOUNTERS & MISTY HIGHLAND TRAILS Wake up to a beautiful morning and enjoy a lavish buffet breakfast. Today hosts a cornerstone Premium Thailand Experience: a private excursion to the majestic Wat Phra That Doi Suthep mountain temple. Ascend the monumental golden naga staircase to view the monumental golden chedi, offering an incredible photography point. In the afternoon, transfer to an award-winning ethical elephant sanctuary. Engage in a respectful, up-close encounter with gentle rescued elephants, walking alongside them through the lush jungle and bathing them in a shallow river basin. This immersive experience is designed to be completely respectful and safe, creating truly unforgettable memories for every traveler. Sightseeing Included: Doi Suthep mountain temple, ethical elephant sanctuary, river bathing interaction. Optional Activities: Explore the historic Old City of Chiang Mai by private tuk-tuk or walking tour.'
                ),
                [
                    'Overnight Stay: Chiang Mai (Ultra-Luxury Heritage Valley Resort)',
                    'Meals Included: International Buffet Breakfast & Sanctuary Farm-to-Table Picnic Lunch',
                ],
            ),
            _day(
                5,
                'CHIANG MAI TO PHUKET COASTAL FLIGHT',
                (
                    'TRANSIT TO THE PEARL OF THE ANDAMAN – COASTAL VILLA BLISS Savor a beautiful Highland breakfast before departing for the airport. Your domestic flight brings you south to Phuket, the Pearl of the Andaman Sea. Upon arrival, your waiting private premium vehicle provides a smooth coastal transfer to your ultra-luxury pool villa resort. Check into your premium villa, detailed with a chilled complimentary bottle of champagne. Spend your afternoon unwinding inside your private pool or strolling along the powdery sand beaches, watching the horizon transform into a vibrant sunset tapestry—a perfect start for the coastal finale of your Ultimate Thailand vacation. Sightseeing Included: Domestic flight transit, coastal scenic private resort transfer. Evening Experience: Welcome cocktails at an exclusive beach club with live acoustic background music.'
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Private Pool Villa Resort)',
                    'Meals Included: International Buffet Breakfast & Curated Coastal Seafood Dinner',
                ],
            ),
            _day(
                6,
                'PRIVATE LUXURY YACHT TO PHI PHI ISLANDS',
                (
                    "CRYSTAL LAGOONS, SNORKELING ESCAPADES & MAYA BAY VIEWPOINTS Wake up to a gorgeous morning and enjoy a lavish floating breakfast inside your pool villa. Today hosts an elite signature experience: a full-day private luxury yacht charter to explore the legendary Phi Phi Islands. Skip all standard public crowds as TRAGUIN arranges an exclusive vessel to guide your party directly toward the vertical limestone walls of Maya Bay, offering a premium photography point for your journey. Swim and snorkel hand-in-hand in the emerald waters of Pileh Lagoon, a beautiful natural limestone basin filled with colorful marine life. Savor a premium gourmet picnic lunch specially arranged on the soft sands of Bamboo Island. Conclude your voyage cruising past the dramatic Viking Cave and Monkey Beach, toasting with fine wine as the sun dips below the horizon. Sightseeing Included: Private Luxury Yacht cruise, Maya Bay entry, Pileh Lagoon swimming, Bamboo Island, Viking Cave. Optional Activities: Professional couple's underwater photography session with reef backdrop."
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Private Pool Villa Resort)',
                    'Meals Included: Bespoke Floating Villa Breakfast & Private Yacht Gourmet Picnic Lunch',
                ],
            ),
            _day(
                7,
                'PHANG NGA BAY & JAMES BOND ISLAND',
                (
                    "LIMESTONE MONOLITHS, SEA-CAVE CANOEING & SPA REJUVENATION Prepare for an awe-inspiring day uncovering hidden geographical wonders. After breakfast, transfer to the pier where a premium speed-craft takes your group across Phang Nga Bay. Cruise past hundreds of vertical limestone karsts rising dramatically out of the calm sea. Arrive at James Bond Island, an iconic attraction, and capture fantastic pictures in front of the floating rock monolith. Next, enjoy a relaxing canoeing experience guided through the mystical sea caves and hidden mangrove lagoons of Koh Hong. Savor a fresh seafood lunch at the unique stilted floating village of Koh Panyee. Return to the resort to refresh, enjoying a 150-minute luxury couple’s aroma-spa rejuvenation treatment, leaving your body fully refreshed before your final dinner. Sightseeing Included: James Bond Island, Koh Hong sea cave canoeing, Koh Panyee village, 150-min Luxury Couple's Spa. Evening Experience: Relaxing over contemporary Thai fine dining at the resort's signature restaurant."
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Private Pool Villa Resort)',
                    'Meals Included: International Buffet Breakfast & Koh Panyee Seafood Lunch',
                ],
            ),
            _day(
                8,
                'PHUKET RETREAT & PRIVATE FINALE',
                (
                    'PRIVATE COVE CELEBRATION – THE ULTIMATE GALA DINNER Dedicate today to pure rejuvenation and rest. Spend the morning lounging by your private pool or enjoying a slow walk along the sand, capturing your final group pictures to commemorate an exceptional journey. In the afternoon, enjoy an easy schedule of leisure or boutique shopping at high-end coastal galleries. For your grand finale, TRAGUIN has arranged our ultimate signature surprise: an intimate, completely private beachfront candlelight dinner set in a secluded cove of the resort. Toast your holiday with a glass of fine wine under a starlit sky as gentle waves roll in, creating a memory to last a lifetime. Sightseeing Included: Leisure schedule, private cove beach access. Evening Experience: Signature TRAGUIN Grand Finale Private Beachfront Candlelight Dinner.'
                ),
                [
                    'Overnight Stay: Phuket (Ultra-Luxury Private Pool Villa Resort)',
                    'Meals Included: International Buffet Breakfast & Ultra-Luxury Beachside 5-Course Dinner',
                ],
            ),
            _day(
                9,
                'PHUKET DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – FOREVER REFRESHED Enjoy your final decadent buffet breakfast at your villa veranda, taking a final round of panoramic photos across the tropical resort gardens. Take your time packing your bags while our on-ground concierge team coordinates with hotel reception to manage your seamless checkout. At the designated hour, your private luxury executive vehicle arrives to transfer you comfortably to Phuket International Airport. Your travel manager assists with all check-in procedures, escorting you to the premium departure lounge. Your Ultimate Thailand vacation concludes beautifully, leaving your heart full of unforgettable memories crafted to perfection by TRAGUIN. Sightseeing Included: Private luxury airport departure transfer.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Sukosol Bangkok Novotel Phuket Resort',
                'Multi-city Thailand',
                '8N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — The Sukosol Bangkok Novotel Phuket Resort',
            ),
            _hotel(
                'Avani+ Riverside Bangkok Phuket Marriott, Merlin Beach',
                'Multi-city Thailand',
                '8N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Avani+ Riverside Bangkok Phuket Marriott, Merlin Beach',
            ),
            _hotel(
                'Shangri-La Bangkok The Shore at Katathani',
                'Multi-city Thailand',
                '8N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Shangri-La Bangkok The Shore at Katathani',
            ),
            _hotel(
                'Mandarin Oriental, Bangkok Trisara Phuket / Sri Panwa',
                'Multi-city Thailand',
                '8N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Mandarin Oriental, Bangkok Trisara Phuket / Sri Panwa',
            )
        ],
        inclusions=[
            _inc_included('Handpicked premium accommodation as per selected hotel tier', 1),
            _inc_included('Private luxury vehicle transfers and sightseeing as per itinerary', 2),
            _inc_included('Daily buffet breakfast and curated meals as specified', 3),
            _inc_included('VIP airport fast-track reception and dedicated TRAGUIN concierge support', 4),
            _inc_excluded('PACKAGE INCLUSIONS', 5),
            _inc_excluded('Flights: International flight tickets', 6),
            _inc_excluded('Visa Costs: Thailand entry visa charges', 7),
            _inc_excluded('National Park Fees: Marine conservation park fees', 8),
        ],
    )
    return package, itinerary

THAILAND_TH_002_040_BUILDERS = [
    build_th_002,
    build_th_003,
    build_th_004,
    build_th_005,
    build_th_006,
    build_th_007,
    build_th_008,
    build_th_009,
    build_th_010,
    build_th_011,
    build_th_012,
    build_th_013,
    build_th_014,
    build_th_015,
    build_th_016,
    build_th_017,
    build_th_018,
    build_th_019,
    build_th_020,
    build_th_021,
    build_th_022,
    build_th_023,
    build_th_024,
    build_th_025,
    build_th_026,
    build_th_027,
    build_th_028,
    build_th_029,
    build_th_030,
    build_th_031,
    build_th_032,
    build_th_033,
    build_th_034,
    build_th_035,
    build_th_036,
    build_th_037,
    build_th_038,
    build_th_039,
    build_th_040,
]
