"""Builder functions for TR-002 through TR-010 Tripura domestic packages."""

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

TRIPURA_SLUG = "tripura"


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


def build_tr_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TRP-002'
    tour_code = 'TRAGUIN-TR-002'
    title = 'Ujjayanta Palace • Neermahal • Udaipur • Heritage Exploration'
    duration = '03 Nights / 04 Days'
    slug = 'tr-002-ujjayanta-palace-neermahal-udaipur-heritage-exploration'
    itin_slug = 'tr-002-ujjayanta-palace-neermahal-udaipur-heritage-exploration-itinerary'
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
        is_published=True,
        highlights=[
            _ph('Serial code TRP-002 | TRAGUIN tour code TRAGUIN-TR-002', 1),
            _ph('State / Country: Tripura / India | Category: HERITAGE HOLIDAY', 2),
            _ph('Destinations: Ujjayanta Palace • Neermahal • Udaipur • Heritage Exploration', 3),
            _ph('Ideal for: Family, History Lovers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Meal Plan: TRAGUIN Luxury Proposal Page 1 of 5 Premium Air-Conditioned Luxury Vehicle MAPAI (Breakfast & Gourmet Dinner) | TRAGUIN Luxury Proposal Page 1 of 5 Premium Air-Conditioned Luxury Vehicle MA', 7)
        ],
        moods=['Family', 'Culture'],
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
        tagline='Ujjayanta Palace',
        overview='Travel Dates: As Per Request Group / FIT: Private Family Tour (FIT) Vehicle: Meal Plan: TRAGUIN Luxury Proposal Page 1 of 5 Premium Air-Conditioned Luxury Vehicle MAPAI (Breakfast & Gourmet Dinner) Route: Agartala → Neermahal (Melaghar) → Udaipur → Agartala TRAGUIN Curated Experience Note: This elite Luxury Tripura Holiday offers prioritized, exclusive access to grand royal halls, custom historical storytellers, and private cruise transfers. We take care of every minor detail so your family can travel with complete ease and prestige.',
        seo_title='TR-002 | Ujjayanta Palace | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Tripura package (TRP-002 / TRAGUIN-TR-002): Ujjayanta Palace • Neermahal • Udaipur • Heritage Exploration with handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=True,
        highlights=[
            _ih('Day 01: ARRIVAL IN AGARTALA', 1),
            _ih('Day 02: AGARTALA TO MELAGHAR (NEERMAHAL)', 2),
            _ih('Day 03: EXCURSION TO UDAIPUR', 3),
            _ih('Day 04: DEPARTURE FROM AGARTALA', 4)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN AGARTALA',
                (
                    'THE GRAND ROYALS WELCOME & THE GLORY OF UJJAYANTA PALACE Begin your grand journey as you arrive at the Maharaja Bir Bikram Airport in Agartala. Your dedicated private chauffeur and a senior TRAGUIN concierge welcome your family with fine traditional handloom stoles and refreshing welcome amenities. Board your premium luxury transportation and transfer smoothly to your luxury hotel. In the afternoon, start your majestic Tripura Sightseeing at the legendary Ujjayanta Palace. This stunning white marble structure, built by Maharaja Radha Kishore Manikya, spans across massive grounds featuring Romanesque architecture, tiled floors, and grand wooden ceilings. As dusk falls, capture incredible family portraits at one of the top Instagram locations as the palace grounds illuminate during a brilliant musical fountain show.'
                ),
                [
                    'Sightseeing Included: Ujjayanta Palace, Mughal-inspired Royal Gardens, Albert Ekka Memorial Park.',
                    'Evening Experience: Exclusive evening light and musical fountain show inside the royal gates.',
                    'Overnight Stay: Premium Handpicked Luxury Hotel, Agartala.',
                    'Meals Included: Welcome Dinner.',
                ],
            ),
            _day(
                2,
                'AGARTALA TO MELAGHAR (NEERMAHAL)',
                (
                    'CRUISING TO THE JEWEL OF RUDRASAGAR - THE FLOATING WATER PALACE Indulge in a lavish breakfast before departing towards Melaghar to experience the crowning architectural jewel of your Luxury Tripura Holiday—the magnificent Neermahal Water Palace. Built as a summer resort by Maharaja Bir Bikram Kishore Manikya in the center of Rudrasagar Lake, this mesmerizing palace gracefully combines Hindu and Islamic architectural accents. Your family will step onto a private motorboat to cruise across the lake, arriving directly at the royal water pavilions. Explore the open-air terraces, grand multi-tiered balconies, and residential quarters, capturing scenic beauty that feels frozen in time. In the afternoon, drive past tranquil rubber plantations before returning to Agartala for a cozy family evening.'
                ),
                [
                    'Sightseeing Included: Neermahal Water Palace, Rudrasagar Lake Cruise, Local Rubber Plantation trails.',
                    'Optional Activities: Handicraft interaction at a traditional local bamboo-weaving settlement.',
                    'Overnight Stay: Premium Handpicked Luxury Hotel, Agartala.',
                    'Meals Included: Breakfast & Gourmet Dinner.',
                ],
            ),
            _day(
                3,
                'EXCURSION TO UDAIPUR',
                (
                    'SACRED HERITAGE, ANCIENT TEMPLES & ROYAL LAKES After a hearty breakfast, your premium family tour heads to Udaipur, historically known as Rangamati, the ancient seat of the Manikya kings. Here, your family will enjoy a deeply moving spiritual experience at the sacred Tripura Sundari Temple (Matabari), one of the venerated 51 Shakti Peethas. To guarantee maximum comfort for your family, TRAGUIN arranges a prioritized VIP Darshan. Walk behind the shrine to see Kalyan Sagar Lake, home to giant historic tortoises. Later, visit the nostalgic lakeside ruins of Bhubaneswari Temple on the banks of the river Gomati, providing the perfect blend of emotional storytelling and vintage photography points.'
                ),
                [
                    'Sightseeing Included: Tripura Sundari Temple, Kalyan Sagar, Bhubaneswari Temple, Gunabati Temple Complex.',
                    'Evening Experience: Traditional evening high-tea by the royal lakes of Udaipur.',
                    'Overnight Stay: Premium Handpicked Luxury Hotel, Agartala.',
                    'Meals Included: Breakfast & Farewell Dinner.',
                ],
            ),
            _day(
                4,
                'DEPARTURE FROM AGARTALA',
                (
                    'CRAFT SOUVENIRS & HERITAGE FAREWELLS Enjoy a relaxed morning breakfast spread. Conclude your magnificent heritage tour with a visit to the Purbasha Government Handicrafts Emporium. This is the ultimate spot to collect authentic souvenirs, such as intricate bamboo screens, decorative cane items, and premium hand-woven Tripuri sarees. Your luxury vehicle will then transfer you comfortably to the Maharaja Bir Bikram Airport for your journey home. Your premium holiday concludes, leaving behind beautiful memories curated proudly by TRAGUIN.'
                ),
                [
                    'Sightseeing Included: Purbasha Handicrafts Emporium, Local Agartala Markets.',
                    'Meals Included: Buffet Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Ginger Hotel Agartala / SimilarStandard Executive Room MAPAI (Breakfast & Dinner)',
                'Agartala',
                '3N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Ginger Hotel Agartala / SimilarStandard Executive Room MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Hotel Polo Towers Agartala Premier Luxury RoomMAPAI (Breakfast & Dinner)',
                'Agartala',
                '3N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Hotel Polo Towers Agartala Premier Luxury RoomMAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Hotel Polo Towers / Selected Boutique Stay Executive Suite MAPAI (Breakfast & Dinner)',
                'Agartala',
                '3N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Hotel Polo Towers / Selected Boutique Stay Executive Suite MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'TRAGUIN Private Premium Collection Royal Presidential Suite Curated Gourmet Meals',
                'Agartala',
                '3N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Private Premium Collection Royal Presidential Suite Curated Gourmet Meals',
            )
        ],
        inclusions=[
            _inc_included('Accommodation: Premium stays at handpicked', 1),
            _inc_included('Meals: Breakfasts and Dinners included as per', 2),
            _inc_included('Transfers: All transfers via luxury private', 3),
            _inc_included('transportation.', 4),
            _inc_included('Sightseeing: Comprehensive heritage routes as', 5),
            _inc_included('Assistance: 24/7 dedicated TRAGUIN assistance.✔', 6),
            _inc_included('Activities: Any optional tours or personal', 7),
            _inc_included('Assistance: 24/7 dedicated TRAGUIN assistance.', 8),
            _inc_included('floral greetings.', 9),
            _inc_included('motorboat cruise.', 10),
            _inc_excluded('Flights: Domestic / International airtickets to Agartala.✘', 11),
            _inc_excluded('Entry Tickets: Monument entry tickets and camera', 12),
            _inc_excluded('Personal Expenses: Laundry, mini-bar, phone calls,', 13),
            _inc_excluded('Flights: Domestic / International airtickets to Agartala.', 14),
        ],
    )
    return package, itinerary

def build_tr_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TRP-003'
    tour_code = 'TRAGUIN-TR-003'
    title = 'AGARTALA ESCAPE EXCLUSIVE ITINERARY'
    duration = '03 Nights / 04 Days'
    slug = 'tr-003-agartala-escape-exclusive-itinerary'
    itin_slug = 'tr-003-agartala-escape-exclusive-itinerary-itinerary'
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
        is_published=True,
        highlights=[
            _ph('Serial code TRP-003 | TRAGUIN tour code TRAGUIN-TR-003', 1),
            _ph('State / Country: Tripura / India | Category: FAMILY / ESCAPE', 2),
            _ph('Destinations: COVERED: Agartala • Neermahal Water Palace • Sepahijala • Udaipur (Matabari)', 3),
            _ph('Ideal for: Luxury Family Quick Breaks', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Luxury AC Innova CrystaMeal Plan: MAPAI (Breakfast & Gourmet Dinner) | MAPAI (Breakfast & Gourmet Dinner)', 7)
        ],
        moods=['Family', 'Luxury'],
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
        tagline='AGARTALA ESCAPE EXCLUSIVE ITINERARY',
        overview='Travel Dates: Flexible / Customized Group / FIT: Private FIT Family Tour Vehicle: Luxury AC Innova CrystaMeal Plan: MAPAI (Breakfast & Gourmet Dinner) Route: Agartala → Sepahijala → Neermahal → Udaipur → Agartala TRAGUIN Curated Experience Note: This refined Agartala Escape balances leisurely transit with deep cultural immersion. Enjoy private boat charters, swift VIP darshans, and hand-selected culinary previews designed by local culinary specialists exclusively for TRAGUIN guests.',
        seo_title='TR-003 | AGARTALA ESCAPE EXCLUSIVE ITINERARY | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Tripura package (TRP-003 / TRAGUIN-TR-003): COVERED: Agartala • Neermahal Water Palace • Sepahijala • Udaipur (Matabari) with handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=True,
        highlights=[
            _ih('Day 01: AGARTALA', 1),
            _ih('Day 02: SEPAHIJALA & NEERMAHAL WATER PALACE', 2),
            _ih('Day 03: UDAIPUR HOLY SPIRITUAL TOUR', 3),
            _ih('Day 04: DEPARTURE FROM AGARTALA', 4)
        ],
        days=[
            _day(
                1,
                'AGARTALA',
                (
                    "ROYAL ARRIVAL, GRECO-ROMAN ARCHITECTURE & CAPITAL SIGHTSEEING Your premium journey begins as you land at Maharaja Bir Bikram Airport in Agartala. A dedicated TRAGUIN luxury chauffeur and tour concierge welcome you with traditional floral hospitality and crisp welcome amenities. Transfer smoothly in your private luxury vehicle to one of our premium handpicked hotels. After check-in and short relaxation, begin your curated Tripura Sightseeing at the brilliant Ujjayanta Palace. This majestic white structure features magnificent Mughal-style tiles, soaring domes, and reflection pools. Stroll hand-in-hand through the royal courtyard as the evening lights turn on. Witness the spectacular musical fountain show, capturing perfect family memories at one of Northeast India's premier photography points. Illuminated Palace stroll followed by a gourmet tasting menu of authentic local fusion treats."
                ),
                [
                    'Sightseeing Included: Ujjayanta Palace, Royal State Museum, Heritage Fountains.',
                    'Evening Experience: Overnight Stay: Premium Scrutinized Luxury Hotel, Agartala.',
                    'Meals Included: Welcome Dinner.',
                ],
            ),
            _day(
                2,
                'SEPAHIJALA & NEERMAHAL WATER PALACE',
                (
                    'PRISTINE NATURE RESERVES & THE FLOATING JEWEL OF THE EAST Wake up to a lavish breakfast buffet before heading southwards through scenic routes lined with fragrant rubber plantations. Arrive at the Sepahijala Wildlife Sanctuary, a pristine bio-diversity sanctuary famous for housing the exotic Phayre’s Langur (Spectacled Monkey). Enjoy an immersive, private eco-safari across the parklands. Afterward, travel to Melaghar to experience the crowning luxury of your trip—the majestic Neermahal Water Palace. Situated beautifully in the center of Rudrasagar Lake, this marvelous palace is a breathtaking fusion of Hindu and Islamic artistic architecture. Board a private speed-boat charter across the tranquil lake waters to step inside the royal corridors, open-air sun terraces, and pristine brick columns that reflect perfectly in the water.'
                ),
                [
                    'Sightseeing Included: Sepahijala Sanctuary, Rudrasagar Lake, Neermahal Water Palace.',
                    'Optional Activities: Private country-boat sunset cruise with professional local birdwatching guides.',
                    'Overnight Stay: Premium Heritage Resort / Luxury Capital Hotel.',
                    'Meals Included: Breakfast & Gourmet Lakeside Dinner.',
                ],
            ),
            _day(
                3,
                'UDAIPUR HOLY SPIRITUAL TOUR',
                (
                    "ANCIENT TEMPLES, ROYAL LAKES & SACRED INHERITANCE Indulge in a beautiful breakfast before driving to Udaipur, historically celebrated as the city of lakes and ancient capital of the kings. Experience deep spiritual energy at the historic Tripura Sundari Temple (Matabari), a sacred powerhouse recognized as one of the 51 holy Shakti Peethas. TRAGUIN arranges exclusive VIP priority entry passes for your family's perfect peace of mind. Walk along the tranquil banks of Kalyan Sagar to see the ancient giant turtles that live there. Following this, explore the mystical ruins of the riverside Bhubaneswari Temple, the famous setting that inspired Nobel Laureate Rabindranath Tagore’s legendary plays. Return to the capital through picturesque rolling hills as the sun sets. Temple."
                ),
                [
                    'Sightseeing Included: Tripura Sundari Shakti Peetha, Kalyan Sagar, Bhubaneswari Heritage Site, Jagannath',
                    'Evening Experience: Curated family dinner featuring traditional artisan organic recipes at a luxury venue.',
                    'Overnight Stay: Handpicked Premium Hotel, Agartala.',
                    'Meals Included: Breakfast & Farewell Dinner.',
                ],
            ),
            _day(
                4,
                'DEPARTURE FROM AGARTALA',
                (
                    'AUTHENTIC SOUVENIR SHOPPING & FOND DEPARTURES Conclude your beautiful Premium Tripura Experience with a leisurely breakfast. Before your flight, enjoy an exclusive shopping trip to the Purbasha Handloom & Handicrafts Emporium. Here, you can find premium souvenirs such as authentic hand-loomed Risa silks, delicate cane furniture, and sophisticated bamboo arts carved by master craftsman. Your luxury private vehicle then escorts you smoothly to Maharaja Bir Bikram Airport for your departure flight, carrying home beautiful, unforgettable memories curated perfectly by TRAGUIN.'
                ),
                [
                    'Sightseeing Included: Purbasha State Craft Centre, Local Heritage Markets.',
                    'Meals Included: Sumptuous Buffet Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Welcome Palace / Ginger Agartala Superior Executive Room MAPAI (Breakfast & Dinner)',
                'Agartala',
                '3N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Welcome Palace / Ginger Agartala Superior Executive Room MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Hotel Polo Towers Agartala Premier Luxury Room MAPAI (Breakfast & Dinner)',
                'Agartala',
                '3N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Hotel Polo Towers Agartala Premier Luxury Room MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Tripura Castle Heritage Stay Selection Exclusive Club SuiteMAPAI (Breakfast & Dinner)',
                'Agartala',
                '3N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Tripura Castle Heritage Stay Selection Exclusive Club SuiteMAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'TRAGUIN Signature Boutique Villa Collection Royal Presidential Suite Premium Curated Meals PACKAGE EXCLUSIONS Flights: Flight ti',
                'Agartala',
                '3N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Signature Boutique Villa Collection Royal Presidential Suite Premium Curated Meals PACKAGE E',
            )
        ],
        inclusions=[
            _inc_included('SPECIAL TRAGUIN HIGHLIGHTS', 1),
            _inc_included('properties.', 2),
            _inc_included('assistance.', 3),
            _inc_included('support desk.', 4),
            _inc_included('state taxes.', 5),
            _inc_included('with premium fruit hampers.', 6),
            _inc_included('tickets to Neermahal Palace.', 7),
            _inc_excluded('Flights: Flight tickets to and from Agartala.', 8),
            _inc_excluded('Entry Tickets: Camera fees or specialized guide tips.', 9),
            _inc_excluded('Activities: Any optional water sports or optional tours.', 10),
            _inc_excluded('Insurance: Travel or health insurance policies.', 11),
            _inc_excluded('outside standard bookings.', 12),
        ],
    )
    return package, itinerary

def build_tr_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TRP-004'
    tour_code = 'TG-TR-PIL-004'
    title = 'PILGRIMAGE Agartala • Matabari Tripura Sundari Temple • Neermahal Palace Embark on a profound spiritual journey to one of the 51 sacred Shakti Peethas. The Tripura Sundari Tour meticulously curated by'
    duration = '03 Nights / 04 Days'
    slug = 'tr-004-pilgrimage-agartala-matabari-tripura-sundari-temple-neermahal-palace-embark-on-a-profound-spiritual-journey-to'
    itin_slug = 'tr-004-pilgrimage-agartala-matabari-tripura-sundari-temple-neermahal-palace-embark-on-a-profound-spiritual-journey-to-itinerary'
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
            _ph('Serial code TR-004 | TRAGUIN tour code TG-TR-PIL-004', 1),
            _ph('State / Country: Tripura / India | Category: HOLY PILGRIMAGE TOUR', 2),
            _ph('Destinations: PILGRIMAGE', 3),
            _ph('Ideal for: Devotees, Families, Spiritual Seekers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Premium Air-Conditioned Sedan / SUV (Dedicated Private Chauffeur) Meal Plan: Breakfast & Pure Vegetarian Divine Dinners  | Breakfast & Pure Vegetarian Divine Dinners (MAPAI Plan) TRAGUIN Premium Pilgr', 7)
        ],
        moods=['Culture'],
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
        tagline='PILGRIMAGE Agartala',
        overview="Vehicle Type: Premium Air-Conditioned Sedan / SUV (Dedicated Private Chauffeur) Meal Plan: Breakfast & Pure Vegetarian Divine Dinners (MAPAI Plan) TRAGUIN Premium Pilgrimage Page 1 of 5 Route Plan: MBB Agartala Airport → Agartala City → Udaipur (Matabari) → Melaghar (Neermahal) → Agartala Departure Curated Note: This premium tour features pre-arranged VIP Darshan passes at the holy Tripura Sundari Temple, avoiding long queues, alongside special traditional prasadam offerings managed by TRAGUIN Experts. TRIPURA PILGRIMAGE TOURISM KEYWORDS & SEO CONTENT Tripura is an incredibly sacred destination for travelers seeking a Best Tripura Tour Package or a spiritually fulfilling Tripura Honeymoon / Family Tour. Unlocking rich historical narratives, it is widely famous for its striking archaeological sites and royal palaces. Tripura Sundari Temple (Matabari): Built by Maharaja Dhanya Manikya in 1501, it is worshipped as the vital 'Kurma Peetha' and forms the cornerstone of every luxury Tripura Pilgrimage Package. Neermahal Palace: The iconic water palace of Northeast India, beautifully situated in the center of Lake Rudrasagar, showcasing scenic beauty and exceptional photo opportunities. Top Tourist Places in Tripura: Includes Ujjayanta Palace, Unakoti rock cuts, and Kasba Kali Temple. Best Time to Visit Tripura: October to March offers exceptionally pleasant temperatures for divine Tripura Sightseeing.",
        seo_title='TR-004 | PILGRIMAGE Agartala | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Tripura package (TR-004 / TG-TR-PIL-004): PILGRIMAGE with handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN AGARTALA – THE PRINCELY REALM OF TRIPURA', 1),
            _ih('Day 02: HOLY DARSHAN AT MATABARI TRIPURA SUNDARI TEMPLE', 2),
            _ih('Day 03: NEERMAHAL PALACE – IMAGINATIVE ROYAL WATER PALACE', 3),
            _ih('Day 04: SPIRITUAL SOUVENIRS & DEPARTURE FROM AGARTALA', 4)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN AGARTALA – THE PRINCELY REALM OF TRIPURA',
                (
                    'Arrive at Maharaja Bir Bikram Airport in Agartala, where a professional TRAGUIN holiday representative greets you with floral garlands. Enjoy a comfortable premium transfer to your luxury hotel. In the afternoon, start your Tripura Sightseeing with the magnificent white Ujjayanta Palace, a masterpiece of Indo-Saracenic architecture built by Maharaja Radha Kishore Manikya, followed by a peaceful sunset at the Akhaura International Border Checkpost. • • • •'
                ),
                [
                    'Sightseeing Included: Ujjayanta Palace, Akhaura Border Retreat Ceremony',
                    'Evening Experience: A gorgeous musical fountain show inside the illuminated royal gardens.',
                    'Overnight Stay: Agartala (Premium Handpicked Luxury Hotel)',
                    'Meals Included: Dinner',
                ],
            ),
            _day(
                2,
                'HOLY DARSHAN AT MATABARI TRIPURA SUNDARI TEMPLE',
                (
                    'An auspicious day begins. After an early morning breakfast, take a smooth scenic drive to the holy town of Udaipur, historically known as Rangamati. Experience your TRAGUIN Signature VIP Darshan at the revered Tripura Sundari Temple. Witness the beautiful black stone deity of Maa Kali (Chotti Maa). After offering prayers, spend time feeding the sacred giant turtles at the Kalyan Sagar lake situated right behind the shrine. Curated Experience: Special interaction with chief priests and distribution of authentic holy mahaprasadam.'
                ),
                [
                    'Sightseeing Included: Matabari Temple, Kalyan Sagar Lake, Bhuvneshwari Temple ruins',
                    'Overnight Stay: Agartala / Udaipur Luxury Stay',
                    'Meals Included: Breakfast & Pure Vegetarian Dinner',
                ],
            ),
            _day(
                3,
                'NEERMAHAL PALACE – IMAGINATIVE ROYAL WATER PALACE',
                (
                    "EXCURSION Savor your premium morning breakfast before proceeding to Melaghar to see the famous Neermahal Water Palace. Board an exclusive private motorboat to cruise over Rudrasagar Lake and reach this stunning palace architecture. Explore the royal pavilions, courtyard gardens, and the Maharaja's private quarters. On the return drive, stop at the historical Kasba Kali Temple overlooking the Bangladesh border. Photography Points: Phenomenal reflections of Neermahal architecture inside the lake waters at noon."
                ),
                [
                    'Sightseeing Included: Neermahal Water Palace, Rudrasagar Boat Cruise, Kasba Kali Temple',
                    'Overnight Stay: Agartala',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'SPIRITUAL SOUVENIRS & DEPARTURE FROM AGARTALA',
                (
                    'Enjoy your last breakfast at the luxury hotel. Before heading to the airport, spend a short immersive hour at the local Purbasha state emporium shopping for world-renowned Tripura bamboo handicrafts and authentic handloom fabrics. Your premium chauffeured vehicle will bring you smoothly to the airport, concluding your sacred TRAGUIN Tripura Packages pilgrimage with unforgettable memories and divine blessings. Shopping Highlights: Exquisite organic Cane Furniture, Bamboo Sculptures, and Tripura Silk Sarees.'
                ),
                [
                    'Meals Included: Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Ginger Agartala / Polo Towers Premium Elite (Executive Club Rooms)',
                'Agartala',
                '3N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                1,
                description='OPTION 01 – LUXURY: Ginger Agartala / Polo Towers Premium Elite (Executive Club Rooms)',
            ),
            _hotel(
                'Hotel Woodland Park / Sonar Tori Agartala (Premium Deluxe Accommodations)',
                'Agartala',
                '3N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Hotel Woodland Park / Sonar Tori Agartala (Premium Deluxe Accommodations)',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked hotels with top modern comfort', 1),
            _inc_included('Daily breakfast & carefully customized satvik dinners.', 2),
            _inc_included('Private luxury AC sedan transfers and local sightseeing.', 3),
            _inc_included('VIP quick-entry passes for Matabari Temple.', 4),
            _inc_included('Private motorboat rides across Rudrasagar Lake to', 5),
            _inc_included('Dedicated TRAGUIN Support throughout your journey.', 6),
            _inc_included('Personal temple ritual donation fees or personal charity.', 7),
            _inc_included('Premium handpicked hotels with top modern comfort amenities. Daily breakfast & carefully customized satvik dinners. Private luxury AC sedan transfers and local sightseeing. VIP quick-entry passes for Matabari Temple. Private motorboat rides across Rudrasagar Lake to Neermahal. Dedicated TRAGUIN Support throughout your journey.', 8),
            _inc_excluded('Flight, rail fares, or long-distance travel transfers.', 9),
            _inc_excluded('Any laundry, phone bills, or additional lunch meals.', 10),
            _inc_excluded('Travel insurance policies or emergency medical costs.', 11),
            _inc_excluded('Flight, rail fares, or long-distance travel transfers. Personal temple ritual donation fees or personal charity. Any laundry, phone bills, or additional lunch meals. Travel insurance policies or emergency medical costs.', 12),
            _inc_excluded('Dedicated TRAGUIN Support throughout your journey.', 13),
        ],
    )
    return package, itinerary

def build_tr_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TRP-005'
    tour_code = 'TG-TR-LEI-005'
    title = 'Agartala • Royal Water Palace Neermahal • Sacred Udaipur • Matabari'
    duration = '04 Nights / 05 Days'
    slug = 'tr-005-agartala-royal-water-palace-neermahal-sacred-udaipur-matabari'
    itin_slug = 'tr-005-agartala-royal-water-palace-neermahal-sacred-udaipur-matabari-itinerary'
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
            _ph('Serial code TR-005 | TRAGUIN tour code TG-TR-LEI-005', 1),
            _ph('State / Country: Tripura / India | Category: SENIOR CITIZEN LEISURE TOUR', 2),
            _ph('Destinations: Agartala • Udaipur • Neermahal • Sepahijala', 3),
            _ph('Ideal for: Senior Citizens, Mature Couples, Family Vacations', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Dedicated Luxury SUV (Innova Crysta with custom senior accessibility setup) Meal Strategy: Breakfast & Hot, Wholesome Di | Breakfast & Hot, Wholesome Dinners (MAPAI Plan - Mild, Nutritious Options)', 7),
            _ph('TRAGUIN Signature Experience: Thoroughly customized, slow-paced routing schedules specifically', 8),
            _ph('Curated by Experts: Dining stops at hygiene-vetted properties offering gentle, customizable culinary', 9),
            _ph('Personalized Assistance: Dedicated destination-handling associates to manage internal logistics', 10)
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
        tagline='Agartala',
        overview='Vehicle Layout: Dedicated Luxury SUV (Innova Crysta with custom senior accessibility setup) Meal Strategy: Breakfast & Hot, Wholesome Dinners (MAPAI Plan - Mild, Nutritious Options) Route Overview: Agartala Airport → Royal City Sights → Sepahijala Wildlife Sanctuary → Melaghar Lake District → Historical Udaipur Shrine → Agartala Departure TRAGUIN Curated Care: This premium package guarantees low-step vehicle entries, smooth pacing with zero rushing, wheelchair availability at major tourist spots, and round-the-clock emergency assistance.',
        seo_title='TR-005 | Agartala | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Tripura package (TR-005 / TG-TR-LEI-005): Agartala • Udaipur • Neermahal • Sepahijala with handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN AGARTALA – ROYAL HOSPITALITY WELCOME', 1),
            _ih('Day 02: SEPAHIJALA NATURE SANCTUARY & IMMERSIVE BOTANICAL', 2),
            _ih('Day 03: NEERMAHAL PALACE – SPECTACULAR LAKESIDE FLOATING', 3),
            _ih('Day 04: SACRED UDAIPUR SIGHTSEEING – TRIPURA SUNDARI DARSHAN', 4),
            _ih('Day 05: LOCAL SOUVENIR SELECTION & FAREWELL TO THE LAND OF KINGS', 5),
            _ih('TRAGUIN Signature Experience: Thoroughly customized, slow-paced routing schedules specifically', 6),
            _ih('Curated by Experts: Dining stops at hygiene-vetted properties offering gentle, customizable culinary', 7),
            _ih('Personalized Assistance: Dedicated destination-handling associates to manage internal logistics', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN AGARTALA – ROYAL HOSPITALITY WELCOME',
                (
                    'As you touch down at Maharaja Bir Bikram Airport in Agartala, your specialized TRAGUIN travel manager will greet you outside the lounge with a warm greeting and fresh local refreshments. Relax inside your premium private vehicle as we handle your luggage and drive you to your luxury handpicked hotel. Spend a comfortable afternoon at leisure. In the evening, step out for a calm stroll along the beautifully manicured green lawns of the majestic white Ujjayanta Palace, a stunning heritage monument.'
                ),
                [
                    'Sightseeing Included: Ujjayanta Palace Grounds, Evening Heritage Light Walk',
                    'Evening Experience: A private welcome tea briefing with your tour manager detailing the days ahead.',
                    'Overnight Stay: Agartala (Premium Executive Stay)',
                    'Meals Included: Dinner',
                ],
            ),
            _day(
                2,
                'SEPAHIJALA NATURE SANCTUARY & IMMERSIVE BOTANICAL',
                (
                    "TRAILS Following a delicious premium breakfast, take a smooth, short journey out to the pristine Sepahijala Wildlife Sanctuary. This destination is widely celebrated for its rich natural biodiversity and scenic beauty. Experience a highly personalized, senior-accessible safari inside the sanctuary's core zones to observe the rare Phayre's Leaf Monkey (Spectacled Monkey) in its natural habitat. Later, enjoy a highly comforting pontoon boat ride over the calm, still waters of Amrit Sagar lake. Photography Points: The scenic tree lines reflecting on Amrit Sagar Lake."
                ),
                [
                    'Sightseeing Included: Sepahijala Orchid House, Botanical Gardens, Spectacled Monkey Enclosures',
                    'Overnight Stay: Agartala',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'NEERMAHAL PALACE – SPECTACULAR LAKESIDE FLOATING',
                (
                    'MARVEL Indulge in breakfast before we drive down towards Melaghar to experience the legendary Neermahal Water Palace. Built as a summer escape by Maharaja Bir Bikram Kishore Manikya, this structural marvel stands beautifully positioned right in the center of Rudrasagar Lake. Board a safely guarded, exclusive private motorboat to cruise over the waters and explore the royal courtyards, stone arcs, and historical inner chambers with absolutely no tedious walking tracks involved.'
                ),
                [
                    'Sightseeing Included: Neermahal Royal Floating Palace, Rudrasagar Private Cruise',
                    'Optional Activities: Serene bird-watching during the late afternoon boat ride.',
                    'Overnight Stay: Melaghar / Udaipur Lakeside Premium Resort',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'SACRED UDAIPUR SIGHTSEEING – TRIPURA SUNDARI DARSHAN',
                (
                    'Today is dedicated to the ultimate spiritual highlight of your Premium Tripura Experience. Drive into the historic city of Udaipur to offer your prayers at the highly revered 500-year-old Tripura Sundari Temple (Matabari). Your TRAGUIN Experts will facilitate VIP quick-access passes to ensure a completely seamless, crowd-free sacred darshan. Spend peaceful moments sitting by the steps of the adjacent Kalyan Sagar lake before returning to Agartala. Food Suggestions: Savoring the delicious, traditional hot milk pedas outside the temple gates.'
                ),
                [
                    'Sightseeing Included: Tripura Sundari Shakti Peeth, Kalyan Sagar, Historic Bhuvneshwari Temple Ruins',
                    'Overnight Stay: Agartala (Premium Handpicked Hotel)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'LOCAL SOUVENIR SELECTION & FAREWELL TO THE LAND OF KINGS',
                (
                    'Savor your final morning breakfast at your leisure. Before heading to the terminal, visit the local artisan emporium to browse through some world-famous Tripura cane sculptures, bamboo works, and traditional handwoven textiles. Your private chauffeur will then assist you safely to the Maharaja Bir Bikram Airport. Your luxurious and rejuvenating getaway concludes as you board your flight home with unforgettable memories and true peace of mind. TRAGUIN Support: Complimentary airport baggage porterage assistance for all senior guests.'
                ),
                [
                    'Meals Included: Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Polo Towers Agartala (Executive Suite Room Layout)',
                'Agartala',
                '4N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                1,
                description='OPTION 01 – ULTRA LUXURY: Polo Towers Agartala (Executive Suite Room Layout)',
            ),
            _hotel(
                'Ginger Luxury Partner / Hotel Sonar Tori (Premium Deluxe Room with Lift Access)',
                'Agartala',
                '4N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Ginger Luxury Partner / Hotel Sonar Tori (Premium Deluxe Room with Lift Access)',
            )
        ],
        inclusions=[
            _inc_included('Handpicked hotel accommodation with customized', 1),
            _inc_included('senior citizen features.', 2),
            _inc_included('Daily fresh breakfasts and nutritious, mild, multi-course', 3),
            _inc_included('Private luxury AC vehicle with a highly reliable,', 4),
            _inc_included('professional driver.', 5),
            _inc_included('VIP quick-entry darshan passes at Matabari Temple.', 6),
            _inc_included('Private guarded motorboat seating at Rudrasagar', 7),
            _inc_included('All entry tolls, parking tickets, and local state holiday', 8),
            _inc_included('Dedicated 24/7 on-ground TRAGUIN Support.', 9),
            _inc_included('Main airline tickets or long-distance railway bookings.', 10),
            _inc_included('Personalized custom temple rituals or sacrificial', 11),
            _inc_included('Any optional sightseeing deviations or driver tips.', 12),
            _inc_included('Handpicked hotel accommodation with customized senior citizen features. Daily fresh breakfasts and nutritious, mild, multi-course dinners. Private luxury AC vehicle with a highly reliable, professional driver. VIP quick-entry darshan passes at Matabari Temple. Private guarded motorboat seating at Rudrasagar Lake. All entry tolls, parking tickets, and local state holiday taxes. Dedicated 24/7 on-ground TRAGUIN Support.', 13),
            _inc_excluded('Laundry service, telephone charges, or alcoholic', 14),
            _inc_excluded('minibar treats.', 15),
            _inc_excluded('Medical or comprehensive travel insurance plans.', 16),
            _inc_excluded('Main airline tickets or long-distance railway bookings. Personalized custom temple rituals or sacrificial prayers. Laundry service, telephone charges, or alcoholic minibar treats. Medical or comprehensive travel insurance plans. Any optional sightseeing deviations or driver tips.', 17),
            _inc_excluded('Dedicated 24/7 on-ground TRAGUIN Support.', 18),
        ],
    )
    return package, itinerary

def build_tr_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TR-006'
    tour_code = 'TG-TR-LUX-006'
    title = 'Agartala • Jampui Hills • Sepahijala • Neermahal Water Palace • Udaipur'
    duration = '05 Nights / 06 Days'
    slug = 'tr-006-agartala-jampui-hills-sepahijala-neermahal-water-palace-udaipur'
    itin_slug = 'tr-006-agartala-jampui-hills-sepahijala-neermahal-water-palace-udaipur-itinerary'
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
            _ph('Serial code TR-006 | TRAGUIN tour code TG-TR-LUX-006', 1),
            _ph('State / Country: Tripura / India | Category: ULTRA LUXURY HOLIDAY', 2),
            _ph('Destinations: Agartala • Tripura', 3),
            _ph('Ideal for: High-End Leisure, Couples, VIP Families', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Premium Full Board / Modified American Plan (Exquisite Gourmet Dining)', 7),
            _ph('TRAGUIN Signature Experience: Private chartered speed-boat excursions across Rudrasagar Lake', 8),
            _ph('Curated by TRAGUIN Experts: Direct behind-the-scenes interactions with master silk-weavers in', 9),
            _ph('Luxury Transportation: Elite top-tier private vehicles driven by highly trained, polite, and safe travel', 10)
        ],
        moods=['Luxury', 'Honeymoon', 'Culture'],
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
        tagline='Agartala',
        overview='Travel Dates / Type:Bespoke FIT (Fully Customized Private Luxury Itinerary) Vehicle Class: Premium Elite Chauffeur-Driven SUV (Luxury Toyota Innova Crysta / Luxury Coach) Meal Plan: Premium Full Board / Modified American Plan (Exquisite Gourmet Dining) Route Plan: Agartala International Airport → Jampui Hills → Sepahijala Wildlife Sanctuary → Neermahal → Udaipur → Agartala Departure TRAGUIN Curated Note: This premium itinerary features VIP access privileges at historical temples, private exclusive motorboat charters, artisanal culinary tables, and continuous 24/7 localized operational concierge assistance.',
        seo_title='TR-006 | Agartala | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Tripura package (TR-006 / TG-TR-LUX-006): Agartala • Tripura with handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN AGARTALA – WELCOME TO THE REALM OF', 1),
            _ih('Day 02: SCENIC DRIVE TO JAMPUI HILLS – THE MISTY HIGHLANDS', 2),
            _ih('Day 03: JAMPUI HILLS SUNRISE – DRIVE TO SEPAHIJALA WILDLIFE', 3),
            _ih('Day 04: EXCLUSIVE PRIVATE BOAT CRUISE TO NEERMAHAL WATER', 4),
            _ih('Day 05: EXCURSION TO UDAIPUR & DIVINE TRIPURA SUNDARI DARSHAN', 5),
            _ih('Day 06: PURBASHA ARTISANAL SHOPPING – FAREWELL TRIPURA', 6),
            _ih('TRAGUIN Signature Experience: Private chartered speed-boat excursions across Rudrasagar Lake', 7),
            _ih('Curated by TRAGUIN Experts: Direct behind-the-scenes interactions with master silk-weavers in', 8),
            _ih('Luxury Transportation: Elite top-tier private vehicles driven by highly trained, polite, and safe travel', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN AGARTALA – WELCOME TO THE REALM OF',
                (
                    'MAHARAJAS Touch down at Maharaja Bir Bikram Airport in Agartala, where your private premium TRAGUIN tour director awaits to provide a high-end VIP welcome. Be escorted via your luxury private vehicle to a handpicked premium suite. Following a gourmet lunch, step into the royal past during a curated private tour of the majestic Ujjayanta Palace. Wander through shimmering fountains, high ceilings, and royal galleries. master chefs.'
                ),
                [
                    'Sightseeing Included: Ujjayanta Palace Private Tour, Akhaura Border Flag Down Ceremony',
                    'Evening Experience: Fine-dining royal banquet serving premium traditional recipes reimagined by',
                    'Overnight Stay: Agartala (Ultra-Luxury Suite)',
                    'Meals Included: Lunch & Dinner',
                ],
            ),
            _day(
                2,
                'SCENIC DRIVE TO JAMPUI HILLS – THE MISTY HIGHLANDS',
                (
                    'Savor an early morning gourmet breakfast before tracking northwards towards the gorgeous Jampui Hills, the highest mountain ridge in the state. Wind through scenic beauty, passing lush eco-forests, organic spice farms, and terraced orchards. Check into your exclusive hill-top boutique lodge. Spend the afternoon taking interactive walks through pristine local Mizo tribal hamlets to experience immersive cultural traditions first-hand. at sunset.'
                ),
                [
                    'Sightseeing Included: Vanghmun Village Walk, Betlingshib Peak Panoramic Viewpoint',
                    'Evening Experience: Private bonfire coupled with premium high-tea overlooking a stunning sea of clouds',
                    'Overnight Stay: Jampui Hills (Premium Luxury Eco-Lodge)',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                3,
                'JAMPUI HILLS SUNRISE – DRIVE TO SEPAHIJALA WILDLIFE',
                (
                    "SANCTUARY Awake early to witness a breathtaking sunrise painting the rolling hills of Chittagong. After a relaxed brunch, journey back down the valley to the premium Sepahijala Wildlife Sanctuary. Enjoy a private guided bio-safari inside the reserve to observe the exotic Phayre's Langur (spectacled monkey) and unique native birdlife, before driving directly to your luxury lakeside resort. Photography Points: Golden hour mist over the dense canopy woods of Sepahijala."
                ),
                [
                    'Sightseeing Included: Jampui Sunrise Point, Sepahijala Sanctuary Bio-Safari, Botanical Gardens',
                    'Overnight Stay: Melaghar / Agartala Premium Resort',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                4,
                'EXCLUSIVE PRIVATE BOAT CRUISE TO NEERMAHAL WATER',
                (
                    'PALACE An extraordinary highlight of your Luxury Tripura Holiday awaits today. Board an exclusive private luxury speed-boat across the expansive waters of Rudrasagar Lake. Arrive at the iconic Neermahal Water Palace, the spectacular summer home built by Maharaja Bir Bikram Kishore Manikya. Tour the massive royal pavilions, intricate inner moats, and stone balconies rising beautifully directly out of the lake water.'
                ),
                [
                    'Sightseeing Included: Neermahal Water Palace Exclusive Access, Rudrasagar Lake Speed-Boat Tour',
                    'Optional Activities: Private high-tea served on a luxury boat at sunset.',
                    'Overnight Stay: Agartala (Premium Luxury Stay)',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                5,
                'EXCURSION TO UDAIPUR & DIVINE TRIPURA SUNDARI DARSHAN',
                (
                    "Today, delve deep into sacred heritage during an exclusive excursion to Udaipur, the historical capital city. Enjoy a seamless, pre-arranged TRAGUIN VIP Darshan at the 500-year-old Tripura Sundari Temple (Matabari), one of the iconic 51 Shakti Peethas. Later, visit the beautiful lakeside palace ruins of Bhubaneshwari Temple, immortalized by Rabindranath Tagore in his classic literature. Ruins Local Food Suggestion: Traditional 'Peda' sweets handmade with dense organic milk solids."
                ),
                [
                    'Sightseeing Included: Tripura Sundari Temple VIP Darshan, Kalyan Sagar, Bhubaneshwari Temple',
                    'Overnight Stay: Agartala (Ultra-Luxury Suite)',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                6,
                'PURBASHA ARTISANAL SHOPPING – FAREWELL TRIPURA',
                (
                    'Enjoy a relaxed final morning breakfast at your premium resort. Complete your luxury holiday with a curated visit to the Purbasha State Crafts Emporium to acquire elegant high-end bamboo sculptures and legendary Tripura silk sarees. Your private premium vehicle will then transfer you comfortably to Agartala International Airport for your departure flight, carrying home unforgettable memories of a magnificent Tripura Family Tour.'
                ),
                [
                    'Meals Included: Breakfast',
                    'Assistance: Complete airport luggage trolley handling and premium gate concierge assistance.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Polo Towers Agartala / Premium Presidential Suite (Executive Club Floor)',
                'Agartala',
                '5N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                1,
                description='OPTION 01 – ULTRA LUXURY: Polo Towers Agartala / Premium Presidential Suite (Executive Club Floor)',
            ),
            _hotel(
                'Ginger Elite Premium Club / Lakeside Palace Resort Partner (Luxury Vista Rooms)',
                'Agartala',
                '5N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                2,
                description='OPTION 02 – LUXURY: Ginger Elite Premium Club / Lakeside Palace Resort Partner (Luxury Vista Rooms)',
            )
        ],
        inclusions=[
            _inc_included('suites and eco-lodges.', 1),
            _inc_included('✔ Meals: All daily gourmet breakfasts, lunches, and curated traditional dinners.', 2),
            _inc_included('✔ Transfers: Elite private AC SUV vehicle dedicated throughout the entire routing.', 3),
            _inc_included('✔ Sightseeing: Complete Tripura Sightseeing inclusions with VIP quick-access tickets.', 4),
            _inc_included('✔ Assistance: Specialized TRAGUIN Support with a dedicated personal travel concierge.', 5),
            _inc_included('✔ Taxes & Amenities: Luxury welcome amenities, seasonal fruit baskets, and all government taxes.', 6),
            _inc_included('PACKAGE EXCLUSIONS', 7),
            _inc_included('Optional extended monument guides or driver tips.', 8),
            _inc_included('Accommodation: Premium ultra-luxury handpicked hotel suites and eco-lodges.', 9),
            _inc_included('Meals: All daily gourmet breakfasts, lunches, and curated traditional dinners.', 10),
            _inc_included('Transfers: Elite private AC SUV vehicle dedicated throughout the entire routing.', 11),
            _inc_included('Sightseeing: Complete Tripura Sightseeing inclusions with VIP quick-access tickets.', 12),
            _inc_included('Assistance: Specialized TRAGUIN Support with a dedicated personal travel concierge.', 13),
            _inc_excluded('✘ Domestic or International flight tickets to/from Agartala.', 14),
            _inc_excluded('✘ Camera recording permits or drone photography authorization charges.', 15),
            _inc_excluded('✘ Personal expenditures (laundry, premium cellar spirits, international phone calls).', 16),
            _inc_excluded('Domestic or International flight tickets to/from Agartala.', 17),
            _inc_excluded('Camera recording permits or drone photography authorization charges.', 18),
            _inc_excluded('Personal expenditures (laundry, premium cellar spirits, international phone calls).', 19),
        ],
    )
    return package, itinerary

def build_tr_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TR-007'
    tour_code = 'TG-TR-HER-007'
    title = 'FAMILY TOUR Agartala • Ujjayanta • Neermahal • Unakoti Rock Cuts • Matabari'
    duration = '05 Nights / 06 Days'
    slug = 'tr-007-family-tour-agartala-ujjayanta-neermahal-unakoti-rock-cuts-matabari'
    itin_slug = 'tr-007-family-tour-agartala-ujjayanta-neermahal-unakoti-rock-cuts-matabari-itinerary'
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
            _ph('Serial code TR-007 | TRAGUIN tour code TG-TR-HER-007', 1),
            _ph('State / Country: Tripura / India | Category: FAMILY HERITAGE HOLIDAY', 2),
            _ph('Destinations: Agartala • Ujjayanta • Neermahal • Unakoti • Udaipur', 3),
            _ph('Ideal for: Families, Heritage Enthusiasts, Historians', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Premium Air-Conditioned Luxury Coach / Private SUV (Family Sized) Meal Plan: Breakfast & Curated Gourmet Family Dinners  | Breakfast & Curated Gourmet Family Dinners (MAP Plan)', 7),
            _ph('TRAGUIN Signature Experience: Private, highly informative historical walk led by a certified heritage', 8),
            _ph('Curated by Experts: Carefully managed family routing designed with comfortable travel breaks and fresh', 9)
        ],
        moods=['Family', 'Culture'],
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
        tagline='FAMILY TOUR Agartala',
        overview='Vehicle Type: Premium Air-Conditioned Luxury Coach / Private SUV (Family Sized) Meal Plan: Breakfast & Curated Gourmet Family Dinners (MAP Plan) Route Plan: Agartala Airport → Ujjayanta Palace → Unakoti → Neermahal (Melaghar) → Udaipur → Agartala Departure Curated Note: This premium family package boasts specialized local guides at archaeological sites, VIP entry passes, private boat charters, and continuous on-ground TRAGUIN customer support. DESTINATION HERITAGE INSIGHTS & SEO SUMMARY Tripura is emerging rapidly as one of the ultimate locations for travelers seeking the Best Tripura Tour Package or an enriching Tripura Honeymoon Package. Brimming with imperial architectural marvels, it offers an outstanding backdrop for a Tripura Family Tour. Why Visit Tripura: A perfect blend of royal history at Ujjayanta and Neermahal, mixed with unparalleled archaeological scale at Unakoti. Top Tourist Places in Tripura: Unakoti Rock Carvings, Neermahal Water Palace, Tripura Sundari Temple, and Chabimura. Popular Instagram Locations: The white marble reflection pools of Ujjayanta Palace and sunset speed- boating across Rudrasagar Lake. Best Time to Visit Tripura: The cooler window between October and March is absolutely the premium season to book your unforgettable Luxury Tripura Holiday and enjoy detailed Tripura Sightseeing. • • • • TRAGUIN Premium Luxury Holidays Page 2 of 6',
        seo_title='TR-007 | FAMILY TOUR Agartala | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Tripura package (TR-007 / TG-TR-HER-007): Agartala • Ujjayanta • Neermahal • Unakoti • Udaipur with handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN AGARTALA – WELCOME TO THE LAND OF THE MANIKYAS', 1),
            _ih('Day 02: THE MYSTICAL WONDER OF UNAKOTI ROCK CUTS', 2),
            _ih('Day 03: NEERMAHAL PALACE – EXCLUSIVE PRIVATE BOAT CRUISE', 3),
            _ih('Day 04: PRINCELY UDAIPUR & HOLY MATABARI DARSHAN', 4),
            _ih('Day 05: AMAZON OF THE EAST – CHABIMURA RIVER CANYON CARVINGS', 5),
            _ih('Day 06: SOUVENIR SHOPPING & DEPARTURE WITH UNFORGETTABLE', 6),
            _ih('TRAGUIN Signature Experience: Private, highly informative historical walk led by a certified heritage', 7),
            _ih('Curated by Experts: Carefully managed family routing designed with comfortable travel breaks and fresh', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN AGARTALA – WELCOME TO THE LAND OF THE MANIKYAS',
                (
                    'Arrive at Maharaja Bir Bikram Airport in Agartala, where your family will be warmly received by your dedicated TRAGUIN chauffeur. Board your luxury air-conditioned vehicle and transfer smoothly to your handpicked premium hotel. After a refreshing afternoon check-in, begin your Tripura Sightseeing at the stunning Ujjayanta Palace. Standing in the heart of the city, this magnificent white-marble palace features Mughal-inspired gardens, grand chandeliers, and royal museum galleries that showcase ancient royal lifestyles.'
                ),
                [
                    'Sightseeing Included: Ujjayanta Palace, Heritage Park, Jagannath Temple',
                    'Evening Experience: A family walk through the illuminated fountains of the palace grounds.',
                    'Overnight Stay: Agartala (Premium Luxury Hotel)',
                    'Meals Included: Dinner',
                ],
            ),
            _day(
                2,
                'THE MYSTICAL WONDER OF UNAKOTI ROCK CUTS',
                (
                    'Enjoy an early premium breakfast as we venture out on a full-day excursion to the legendary Unakoti, nestled deep within breathtaking landscapes. Unakoti, meaning "one less than a crore" in Bengali, is an ancient Shaivite pilgrimage site featuring colossal rock-cut reliefs carved into forested hillsides. Marvel at the central 30-foot-tall head of Lord Shiva (Unakotiswara Kal Bhairava) while an expert guide recounts fascinating mythological stories to your family. Photography Points: Wide-angle frames capturing the family against the monumental hill carvings.'
                ),
                [
                    'Sightseeing Included: Unakoti Rock-Cut Reliefs, Kal Bhairava Carvings',
                    'Overnight Stay: Agartala (Premium Handpicked Hotel)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'NEERMAHAL PALACE – EXCLUSIVE PRIVATE BOAT CRUISE',
                (
                    'Following breakfast, journey south towards Melaghar to discover the spectacular Neermahal Water Palace, a premier destination-specific experience. Built by Maharaja Bir Bikram Kishore Manikya as a summer resort, this architectural wonder sits right in the middle of Rudrasagar Lake. Board a private TRAGUIN chartered motorboat to reach the palace, exploring its royal residential wings, open-air courtyards, and beautiful pavilions that fuse Hindu and Islamic architecture.'
                ),
                [
                    'Sightseeing Included: Neermahal Palace, Rudrasagar Lake Boat Excursion',
                    'Optional Activities: Family speed-boating or traditional row-boat experience at sunset.',
                    'Overnight Stay: Luxury Lake Resort (Melaghar / Agartala)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'PRINCELY UDAIPUR & HOLY MATABARI DARSHAN',
                (
                    "Today, travel to Udaipur, the historic former capital of Tripura. Explore the ancient lakes that dot the town before visiting the sacred Tripura Sundari Temple (Matabari), one of the highly revered 51 Shakti Peethas. Skip the crowds with your VIP access organized by TRAGUIN Experts. Witness the traditional morning rituals and stroll along the banks of Kalyan Sagar to see the ancient, sacred giant turtles. Local Experience: Tasting the legendary sweet 'Peda' prasad outside the temple gates."
                ),
                [
                    'Sightseeing Included: Tripura Sundari Temple, Kalyan Sagar, Bhubaneswari Temple Ruins',
                    'Overnight Stay: Agartala',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'AMAZON OF THE EAST – CHABIMURA RIVER CANYON CARVINGS',
                (
                    'Embark on an immersive, adventurous eco-tour to Chabimura, often called the Amazon of the East. Drift along the Gomati River on a secured traditional motorized boat through steep, deep-green rocky canyons. Feast your eyes on massive rock-cut panels carved directly onto vertical cliff faces over the rushing waters, depicting historical deities, before returning to Agartala for a relaxed evening.'
                ),
                [
                    'Sightseeing Included: Chabimura Rock Panels, Gomati River Boat Cruise',
                    'Evening Experience: Farewell family dinner at a premium ethnic restaurant, arranged by TRAGUIN.',
                    'Overnight Stay: Agartala',
                    'Meals Included: Breakfast & Farewell Dinner',
                ],
            ),
            _day(
                6,
                'SOUVENIR SHOPPING & DEPARTURE WITH UNFORGETTABLE',
                (
                    'MEMORIES Savor your final luxury breakfast. Spend your morning shopping for beautiful indigenous souvenirs before your private premium vehicle drops you safely at Maharaja Bir Bikram Airport. Your spectacular TRAGUIN Tripura Packages journey draws to a close here, leaving your family with warm hearts and stories to cherish for a lifetime.'
                ),
                [
                    'Meals Included: Breakfast',
                    'Assistance: Complete luggage and airport check-in assistance from our travel coordinators.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Polo Towers Agartala (Presidential Suite / Executive Club Rooms)',
                'Agartala',
                '5N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                1,
                description='OPTION 01 – LUXURY: Polo Towers Agartala (Presidential Suite / Executive Club Rooms)',
            ),
            _hotel(
                'Ginger Agartala / Sonar Tori Premium (Luxury Interconnected Rooms)',
                'Agartala',
                '5N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Ginger Agartala / Sonar Tori Premium (Luxury Interconnected Rooms)',
            )
        ],
        inclusions=[
            _inc_included('Accommodation in handpicked luxury hotels and', 1),
            _inc_included('Daily breakfast and multi-course gourmet dinners.', 2),
            _inc_included('Private family luxury AC vehicle for all transfers and', 3),
            _inc_included('sightseeing tours.', 4),
            _inc_included('Private boat charters at Neermahal & Chabimura River.', 5),
            _inc_included('VIP entry passes at Tripura Sundari Temple.', 6),
            _inc_included('Dedicated TRAGUIN Support available throughout.', 7),
            _inc_included('Accommodation in handpicked luxury hotels and resorts. Daily breakfast and multi-course gourmet dinners.', 8),
            _inc_excluded('Airfare, rail tickets, or airport departure taxes.', 9),
            _inc_excluded('Personal expenses like laundry, minibar, or telephone', 10),
            _inc_excluded('Camera or professional videography licensing fees.', 11),
            _inc_excluded('Travel medical insurance coverage.', 12),
            _inc_excluded('Optional adventure sport excursions or water sports.', 13),
            _inc_excluded('Airfare, rail tickets, or airport departure taxes. Personal expenses like laundry, minibar, or telephone calls. Private family luxury AC vehicle for all transfers and sightseeing tours. Private boat charters at Neermahal & Chabimura River. VIP entry passes at Tripura Sundari Temple. Dedicated TRAGUIN Support available throughout. Camera or professional videography licensing fees. Travel medical insurance coverage. Optional adventure sport excursions or water sports.', 14),
            _inc_excluded('Daily breakfast and multi-course gourmet dinners.', 15),
        ],
    )
    return package, itinerary

def build_tr_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TR-008'
    tour_code = 'TG-TR-EDU-008'
    title = 'EXPEDITION Agartala • Unakoti Rock Cuts • Sepahijala Bio-Reserve • Neermahal Palace'
    duration = '04 Nights / 05 Days'
    slug = 'tr-008-expedition-agartala-unakoti-rock-cuts-sepahijala-bio-reserve-neermahal-palace'
    itin_slug = 'tr-008-expedition-agartala-unakoti-rock-cuts-sepahijala-bio-reserve-neermahal-palace-itinerary'
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
            _ph('Serial code TR-008 | TRAGUIN tour code TG-TR-EDU-008', 1),
            _ph('State / Country: Tripura / India | Category: SCHOOL EDUCATIONAL TOUR', 2),
            _ph('Destinations: Agartala • Sepahijala • Udaipur • Melaghar • Unakoti', 3),
            _ph('Ideal for: Students, Teachers, Educational Institutes', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Premium Air-Conditioned Luxury Coaches (Student Safe, GPS Tracked) Meal Plan: All Meals Included (Breakfast, Lunch, Even | All Meals Included (Breakfast, Lunch, Evening Snacks & Dinner — Balanced Stud', 7),
            _ph('TRAGUIN Signature Experience: Specialized student activity workbooks and project logs provided to', 8),
            _ph('TRAGUIN Educational Expeditions Page 5 of 6', 9),
            _ph('Curated by TRAGUIN Experts: Strict safety protocol checklist, including student name tags, emergency', 10),
            _ph('Exclusive Recommendations: Fun interactive group evening quizzes with exciting trophies for the', 11)
        ],
        moods=['Culture', 'Educational'],
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
        tagline='EXPEDITION Agartala',
        overview="Vehicle Type: Premium Air-Conditioned Luxury Coaches (Student Safe, GPS Tracked) Meal Plan: All Meals Included (Breakfast, Lunch, Evening Snacks & Dinner — Balanced Student Nutrition) Route Plan: Agartala Airport → Sepahijala → Udaipur → Melaghar → Unakoti → Agartala Departure Curated Note: This premium student holiday features 24/7 dedicated medical assistance on standby, continuous security marshals, interactive educational worksheet handbooks curated by TRAGUIN Experts, and specialized tour guides explaining the history, geology, and ecology of the region. DESTINATION EDUCATIONAL MERITS & SEO CONTENT Tripura is rapidly emerging as a top destination for academic travel, offering a uniquely dynamic curriculum landscape. Selecting the Best Tripura Tour Package for students provides deep historical insights, geographical wonders, and social immersion. Whether organizing a Tripura Family Tour or an active group expedition, the state serves up rich academic data. Unakoti Archaeological Wonders: Home to the colossal bas-relief stone carvings of Shiva dating back centuries, it presents an extraordinary mystery in history and architecture for student analysis. Sepahijala Wildlife Sanctuary: A thriving bio-reserve renowned for its research on the Spectacled Monkey (Phayre's langur), offering direct insights into zoology and environmental science. Top Tourist Places in Tripura: From the structural dynamics of Neermahal Water Palace to the historic archives within Ujjayanta Palace, children absorb legacy through immersive experiences. Best Time to Visit Tripura: The refreshing winter window from October to March ensures excellent weather for outdoor field trips and continuous Tripura Sightseeing. • • • • TRAGUIN Educational Expeditions Page 2 of 6",
        seo_title='TR-008 | EXPEDITION Agartala | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Tripura package (TR-008 / TG-TR-EDU-008): Agartala • Sepahijala • Udaipur • Melaghar • Unakoti with handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN AGARTALA – DISCOVERING PRINCELY CHRONICLES', 1),
            _ih('Day 02: SEPAHIJALA ECO-SYSTEM STUDY & UDAIPUR HISTORIC CHRONICLES', 2),
            _ih('Day 03: NEERMAHAL PALACE – AN ARCHITECTURAL & HYDRAULIC MARVEL', 3),
            _ih('Day 04: EXCURSION TO UNAKOTI – MYSTERIES ENCRYPTED IN STONE', 4),
            _ih('Day 05: INDUSTRIAL LEARNING, HANDLOOMS & HOMEDWARD BOUND JOURNEY', 5),
            _ih('TRAGUIN Signature Experience: Specialized student activity workbooks and project logs provided to', 6),
            _ih('TRAGUIN Educational Expeditions Page 5 of 6', 7),
            _ih('Curated by TRAGUIN Experts: Strict safety protocol checklist, including student name tags, emergency', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN AGARTALA – DISCOVERING PRINCELY CHRONICLES',
                (
                    'Arrive at Maharaja Bir Bikram Airport in Agartala, where a warm hospitality greeting awaits from your TRAGUIN educational coordinator. Check into your secure premium hotel. Post lunch, begin your academic Tripura Sightseeing at the legendary white Ujjayanta Palace. Students will participate in an interactive architectural quiz session exploring the historic mix of British and Mughal styles, followed by a visit to the state central library.'
                ),
                [
                    'Sightseeing Included: Ujjayanta Royal Palace, State Heritage Museum, Indo-Bangla Border Post',
                    'Evening Experience: A structured group briefing over dinner detailing the geological map of Tripura.',
                    'Overnight Stay: Agartala (Premium Student-Friendly Selected Hotel)',
                    'Meals Included: Lunch & Dinner',
                ],
            ),
            _day(
                2,
                'SEPAHIJALA ECO-SYSTEM STUDY & UDAIPUR HISTORIC CHRONICLES',
                (
                    'Embark on an early morning field trip to Sepahijala Wildlife Sanctuary. Guided by wildlife naturalists, students will survey the bio-reserve, studying the endemic flora, migratory birds, and the unique behavior of the Clouded Leopard. In the afternoon, travel to the historic town of Udaipur to examine ancient archaeological structures at Bhubneshwari Temple and view the famous 500-year-old architecture of the Tripura Sundari Temple. Local Experiences: Interaction with local environmentalists to discuss forest conservation and ecological balance.'
                ),
                [
                    'Sightseeing Included: Sepahijala Bio-Reserve, Botanical Gardens, Matabari Temple Complex',
                    'Overnight Stay: Agartala / Udaipur Base Camp',
                    'Meals Included: Breakfast, Packed Field Lunch, Dinner',
                ],
            ),
            _day(
                3,
                'NEERMAHAL PALACE – AN ARCHITECTURAL & HYDRAULIC MARVEL',
                (
                    'Drive down to Melaghar today to discover the fascinating Neermahal Water Palace, situated gracefully right in the center of Rudrasagar Lake. Board large, safety-certified passenger boats to access the island palace. Students will evaluate the innovative engineering mechanics behind this summer palace, studying its historical rainwater harvesting design, cooling mechanisms, and the surrounding lake ecology. Photography Points: Group photographs against the expansive white stone structures of Neermahal.'
                ),
                [
                    'Sightseeing Included: Neermahal Royal Palace, Rudrasagar Wetland Exploration',
                    'Overnight Stay: Agartala',
                    'Meals Included: Breakfast, Hot Lunch, Dinner',
                ],
            ),
            _day(
                4,
                'EXCURSION TO UNAKOTI – MYSTERIES ENCRYPTED IN STONE',
                (
                    "Set out on an exciting travel highlight day to the deep northern hills of Unakoti. Known for its jaw- dropping stone sculptures carved directly into the mountain rockfaces, students will analyze historic lore, archaeological dating, and the unique geology of rock weathering. This immersive experience highlights Tripura's remarkable contribution to art history. Return late evening to your hotel after an unforgettable day of field research. journey."
                ),
                [
                    'Sightseeing Included: Unakoti Hill Archaeological Site, Rock-cut bas-relief structures',
                    'Optional Activities: Group debate session on protecting ancient heritage sites during the return bus',
                    'Overnight Stay: Agartala',
                    'Meals Included: Breakfast, Mid-route Lunch, Dinner',
                ],
            ),
            _day(
                5,
                'INDUSTRIAL LEARNING, HANDLOOMS & HOMEDWARD BOUND JOURNEY',
                (
                    'Savor your final group breakfast. To complete the economic and industrial segment of the curriculum, visit a local state bamboo-processing and handloom unit, observing the production cycle of fine organic cane products. Gather your personalized certificates of exploration issued by TRAGUIN before transferring comfortably to the airport for your return journey, carrying back invaluable lessons and unforgettable memories. Souvenir Recommendations: Eco-friendly bamboo stationery notebooks and local hand-woven bookmarks.'
                ),
                [
                    'Meals Included: Breakfast & Lunch',
                ],
            )
        ],
        hotels=[
            _hotel(
                'INSTITUTIONAL SELECTION: Hotel Polo Towers Agartala / Executive Group Wings (Quad/Triple Sharing for Students, Twin Sharing for ',
                'Agartala',
                '4N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – PREMIUM: INSTITUTIONAL SELECTION: Hotel Polo Towers Agartala / Executive Group Wings (Quad/Triple Sharing for',
            ),
            _hotel(
                'COMFORT ACCOMMODATION: Hotel Sonar Tori / Central Plaza Agartala (Spacious, Safe Layout with 24/7 Security Controls)',
                'Agartala',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – DELUXE: COMFORT ACCOMMODATION: Hotel Sonar Tori / Central Plaza Agartala (Spacious, Safe Layout with 24/7 Se',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked hotels vetted strictly for school', 1),
            _inc_included('safety and sanitation.', 2),
            _inc_included('All buffet meals (Breakfast, Lunch, Dinner) cooked with', 3),
            _inc_included('mild spices.', 4),
            _inc_included('Private luxury AC coaches for comfortable student', 5),
            _inc_included('sightseeing routes.', 6),
            _inc_included('Complimentary entry fees to all palaces, bio-reserves,', 7),
            _inc_included('and museums.', 8),
            _inc_included('Certified mineral water bottles provided continuously', 9),
            _inc_included('during transits.', 10),
            _inc_included('Complete TRAGUIN Support with assigned tour', 11),
            _inc_included('Any room-service orders or extra items not on the buffet', 12),
            _inc_included('Premium handpicked hotels vetted strictly for school safety and sanitation. All buffet meals (Breakfast, Lunch, Dinner) cooked with mild spices. Private luxury AC coaches for comfortable student sightseeing routes. Complimentary entry fees to all palaces, bio-reserves, and museums. Certified mineral water bottles provided continuously during transits. Complete TRAGUIN Support with assigned tour managers.', 13),
            _inc_excluded('Airfare or railway tickets to/from Agartala base.', 14),
            _inc_excluded('Personal purchases, laundry, or optional video-camera', 15),
            _inc_excluded('Airfare or railway tickets to/from Agartala base. Personal purchases, laundry, or optional video-camera tickets. Any room-service orders or extra items not on the buffet menu.', 16),
        ],
    )
    return package, itinerary

def build_tr_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TR-009'
    tour_code = 'TG-TR-HON-009'
    title = 'Agartala • Neermahal Royal Water Palace • Udaipur Romantic Escapes'
    duration = '04 Nights / 05 Days'
    slug = 'tr-009-agartala-neermahal-royal-water-palace-udaipur-romantic-escapes'
    itin_slug = 'tr-009-agartala-neermahal-royal-water-palace-udaipur-romantic-escapes-itinerary'
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
            _ph('Serial code TR-009 | TRAGUIN tour code TG-TR-HON-009', 1),
            _ph('State / Country: Tripura / India | Category: ROMANTIC HONEYMOON LUXURY ESCAPE', 2),
            _ph('Destinations: Agartala • Neermahal (Melaghar) • Udaipur • Sepahijala', 3),
            _ph('Ideal for: Honeymooners, Couples, Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Premium Air-Conditioned Luxury Sedan (Private, Chauffeur-Driven) Meal Plan: Breakfast & Curated Candlelight Specialty Di | Breakfast & Curated Candlelight Specialty Dinners (MAPAI Plan)', 7)
        ],
        moods=['Luxury', 'Honeymoon', 'Culture'],
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
        tagline='Agartala',
        overview="Vehicle Type: Premium Air-Conditioned Luxury Sedan (Private, Chauffeur-Driven) Meal Plan: Breakfast & Curated Candlelight Specialty Dinners (MAPAI Plan) Route Plan: Agartala Airport → Sepahijala Sanctuary → Melaghar (Neermahal) → Udaipur → Agartala Departure Curated Note: This premium luxury holiday includes exclusive couples' experiences, complimentary welcome amenities, private lake cruise charters, and dedicated 24/7 VIP assistance by TRAGUIN Experts. TRIPURA HONEYMOON SEO CONTENT & INSIGHTS Tripura is emerging rapidly as one of India's most fascinating and offbeat spots for a Luxury Tripura Holiday or a romantic Tripura Honeymoon Package. Brimming with gorgeous architecture and pristine lakes, it promises perfect seclusion and cultural grandeur for couples. Neermahal Palace: The iconic water palace of Northeast India, located magically in the middle of Lake Rudrasagar—the ultimate romantic Instagram location. Ujjayanta Palace: A majestic ivory-white royal structure with Mughal-inspired geometric gardens, providing elite backdrops for couples' photography. Tripura Sundari Temple: A historic 500-year-old sacred Shakti Peeth, perfect for couples seeking divine blessings for their new journey together. Best Time to Visit Tripura: The pleasantly refreshing winter months from October to March present a gorgeous climate for premium Tripura Sightseeing. • • • • TRAGUIN Romantic Escapes • TR-009 Page 2 of 6",
        seo_title='TR-009 | Agartala | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Tripura package (TR-009 / TG-TR-HON-009): Agartala • Neermahal (Melaghar) • Udaipur • Sepahijala with handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN AGARTALA – ROYAL BANQUET & LUXURY WELCOME', 1),
            _ih('Day 02: SEPAHIJALA LAGOONS & ROMANTIC SUNSET CRUISE AT NEERMAHAL', 2),
            _ih('Day 03: MYSTICAL UDAIPUR – HOLY DARSHAN & ANCIENT LAKES', 3),
            _ih("Day 04: HERITAGE TRAILS, KASBA KALI & EXCLUSIVE COUPLES' SPA", 4),
            _ih('Day 05: EXQUISITE SOUVENIR SHOPPING & DEPARTURE WITH FOREVER', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN AGARTALA – ROYAL BANQUET & LUXURY WELCOME',
                (
                    'Arrive at Maharaja Bir Bikram Airport in Agartala, where a luxury TRAGUIN coordinator welcomes you with exotic floral bouquets. Board your private premium vehicle for a swift transfer to your luxury suite. After a refreshing check-in, enjoy an immersive afternoon touring the grand Ujjayanta Palace. Walk hand-in-hand through its fountains and magnificent halls, capturing stunning photos. In the evening, witness the patriotic retreat ceremony at the Akhaura Indo-Bangladesh border. Welcome Amenities: Complimentary sparkling juice, hand-crafted chocolates, and fresh orchids in-room.'
                ),
                [
                    'Sightseeing Included: Ujjayanta Palace, Akhaura Border Checkpost',
                    'Overnight Stay: Agartala (Premium Executive Suite)',
                    'Meals Included: Dinner',
                ],
            ),
            _day(
                2,
                'SEPAHIJALA LAGOONS & ROMANTIC SUNSET CRUISE AT NEERMAHAL',
                (
                    'Savor a delightful morning breakfast. Drive through lush greenery to the serene Sepahijala Wildlife Sanctuary, enjoying a romantic boat ride over its quiet lake surrounded by rich woodlands. Afterward, head to Melaghar to witness the legendary Neermahal Water Palace. Board a private speed cruise across Rudrasagar Lake to explore this royal pavilion. End the day with a dramatic sunset over the water.'
                ),
                [
                    'Sightseeing Included: Sepahijala Sanctuary, Neermahal Royal Palace, Rudrasagar Cruise',
                    'Evening Experience: A private, curated lakeside candlelight dinner at your premium resort.',
                    'Overnight Stay: Melaghar / Rudrasagar Luxury Lakefront Property',
                    'Meals Included: Breakfast & Specialized Candlelight Dinner',
                ],
            ),
            _day(
                3,
                'MYSTICAL UDAIPUR – HOLY DARSHAN & ANCIENT LAKES',
                (
                    "After a morning breakfast overlooking the lake, drive comfortably to the historic capital city of Udaipur. Experience a priority VIP Darshan at the sacred Tripura Sundari Temple, an iconic attraction and prominent Shakti Peeth. Walk along the steps of Kalyan Sagar lake to watch the giant turtles. Later, discover the beautiful stone carvings of Bhuvneshwari Temple, the timeless muse of Rabindranath Tagore's literature. Photography Points: The old brick ruins of Bhuvneshwari Temple during golden hour light."
                ),
                [
                    'Sightseeing Included: Tripura Sundari Temple, Kalyan Sagar, Bhuvneshwari Temple, Jagannath Dighi',
                    'Overnight Stay: Agartala (Luxury Handpicked Hotel)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                "HERITAGE TRAILS, KASBA KALI & EXCLUSIVE COUPLES' SPA",
                (
                    "Relish a relaxed morning. Today, enjoy a scenic drive to the Kasba Kali Temple, situated dramatically on a hillock right along the edge of the international border line. Return to Agartala for an exclusive, complimentary luxury couples' therapeutic spa session at a premium wellness center. Spend your Complimentary Experience: 60-Minute Premium Aromatherapy Couples' Relaxation Massage."
                ),
                [
                    'evening: exploring local craft cafes or relaxing at your own pace.',
                    'Sightseeing Included: Kasba Kali Temple, Heritage Park Agartala',
                    'Overnight Stay: Agartala',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'EXQUISITE SOUVENIR SHOPPING & DEPARTURE WITH FOREVER',
                (
                    'MEMORIES Indulge in a late breakfast at your hotel. Visit the premium Purbasha Handloom Emporium to purchase souvenirs like exquisite cane artifacts or Tripura silk sarees. Your private chauffeur will then transfer you comfortably to Agartala Airport. Your romantic TRAGUIN Tripura Package concludes here, leaving you with beautiful blessings and unforgettable memories to last a lifetime. PREMIUM LUXURY'
                ),
                [
                    'Meals Included: Breakfast',
                    'Assistance: Airport executive assistance for smooth priority check-in.',
                    'sightseeing: .',
                    'Optional: adventure activities or local tips.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Polo Towers Agartala (Presidential Honeymoon Suite)',
                'Agartala',
                '4N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                1,
                description='OPTION 01 – ULTRA LUXURY: Polo Towers Agartala (Presidential Honeymoon Suite)',
            ),
            _hotel(
                'Ginger Luxury Partner Elite / Hotel Sonar Tori (Executive Club Room)',
                'Agartala',
                '4N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                2,
                description='OPTION 02 – LUXURY: Ginger Luxury Partner Elite / Hotel Sonar Tori (Executive Club Room)',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked luxury honeymoon suite', 1),
            _inc_included('accommodations.', 2),
            _inc_included('Daily breakfast & curated multi-course romantic', 3),
            _inc_included('One exclusive lakeside private Candlelight Dinner with', 4),
            _inc_included('Private luxury AC Sedan for all transfers & premium', 5),
            _inc_included('sightseeing.', 6),
            _inc_included('Private speed-boat charter to Neermahal Water Palace.', 7),
            _inc_included("Complimentary couples' aromatherapy spa massage", 8),
            _inc_included('VIP quick-entry passes for Matabari Tripura Sundari', 9),
            _inc_included('Full operational backup and continuous TRAGUIN', 10),
            _inc_included('refreshments.', 11),
            _inc_included("Premium handpicked luxury honeymoon suite accommodations. Daily breakfast & curated multi-course romantic dinners. One exclusive lakeside private Candlelight Dinner with cake. Private luxury AC Sedan for all transfers & premium sightseeing. Private speed-boat charter to Neermahal Water Palace. Complimentary couples' aromatherapy spa massage voucher. VIP quick-entry passes for Matabari Tripura Sundari Temple. Full operational backup and continuous TRAGUIN Support.", 12),
            _inc_excluded('Domestic or international flights/rail tickets.', 13),
            _inc_excluded('Professional camera entry tickets at monument gates.', 14),
            _inc_excluded('Personal laundry, telephone billing, or alcoholic', 15),
            _inc_excluded('Optional adventure activities or local tips.', 16),
            _inc_excluded('Domestic or international flights/rail tickets. Professional camera entry tickets at monument gates. Personal laundry, telephone billing, or alcoholic refreshments. Optional adventure activities or local tips.', 17),
        ],
    )
    return package, itinerary

def build_tr_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TR-010'
    tour_code = 'TG-TR-FAM-010'
    title = 'Agartala • Jampui Hills • Unakoti Rock Carvings • Neermahal • Udaipur'
    duration = '06 Nights / 07 Days'
    slug = 'tr-010-agartala-jampui-hills-unakoti-rock-carvings-neermahal-udaipur'
    itin_slug = 'tr-010-agartala-jampui-hills-unakoti-rock-carvings-neermahal-udaipur-itinerary'
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
            _ph('Serial code TR-010 | TRAGUIN tour code TG-TR-FAM-010', 1),
            _ph('State / Country: Tripura / India | Category: COMPLETE FAMILY TOUR PACKAGE', 2),
            _ph('Destinations: Agartala • Jampui Hills • Unakoti • Udaipur • Neermahal', 3),
            _ph('Ideal for: Families, Nature Lovers, Heritage Enthusiasts', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Premium Air-Conditioned SUV / Family Coach (Dedicated Private Chauffeur) Meal Plan: Daily Buffet Breakfast & Elaborate F | Daily Buffet Breakfast & Elaborate Family Dinners (MAPAI Plan)', 7),
            _ph('TRAGUIN Signature Experience: A dedicated, private family coach ensuring plenty of room for luggage', 8),
            _ph('Curated by Experts: Selective restaurant stops featuring reliable hygiene and a broad variety of child-', 9),
            _ph('TRAGUIN Premium Holidays • TR-010 Page 6 of 7', 10),
            _ph('Luxury Transportation: Highly trained, safe, and courteous drivers for smooth mountain driving through', 11)
        ],
        moods=['Family', 'Culture', 'Adventure'],
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
        tagline='Agartala',
        overview='Vehicle Type: Premium Air-Conditioned SUV / Family Coach (Dedicated Private Chauffeur) Meal Plan: Daily Buffet Breakfast & Elaborate Family Dinners (MAPAI Plan) Route Plan: Agartala → Jampui Hills → Unakoti (Kailashahar) → Agartala → Udaipur → Neermahal → Agartala Curated Note: This premium Tripura Family Tour includes seamless intercity transit across mountain passes, local cultural coordinators, and 24/7 dedicated assistance by TRAGUIN Experts. TRIPURA TOURISM SEO CONTENT & INSIGHTS Tripura stands out as an exceptional choice for a Luxury Tripura Holiday or a complete multi-day Tripura Family Tour. Unlocking rich tribal cultures and princely heritage, the state offers top tourist places in Tripura that cater perfectly to all age groups. Unakoti Rock Carvings: The legendary hill of "one less than a crore" rock-cut sculptures, capturing the absolute essence of historical Tripura Sightseeing. Jampui Hills: The highest hill range in the state, celebrated for its eternal spring weather, sprawling orange orchards, and panoramic mountain views. Neermahal Palace & Udaipur: Combining the magical floating water palace of Rudrasagar Lake with the historic temples of Udaipur city. Best Time to Visit Tripura: The refreshing, dry autumn and winter months between October and April provide the perfect climate for outdoor activities. • • • • TRAGUIN Premium Holidays • TR-010 Page 2 of 7',
        seo_title='TR-010 | Agartala | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Tripura package (TR-010 / TG-TR-FAM-010): Agartala • Jampui Hills • Unakoti • Udaipur • Neermahal with handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN AGARTALA – WELCOME TO THE CITY OF PALACES', 1),
            _ih('Day 02: SCENIC DRIVE TO JAMPUI HILLS – THE HIGHEST PEAK', 2),
            _ih('Day 03: MYSTICAL UNAKOTI ROCK CUTS – THE HILL OF WONDERS', 3),
            _ih('Day 04: ECO-TRAILS AT SEPAHIJALA WILDLIFE PARK & RETURN TO AGARTALA', 4),
            _ih('Day 05: SACRED UDAIPUR – HISTORIC TEMPLES & LAKES', 5),
            _ih('Day 06: NEERMAHAL WATER PALACE – THE CROWN JEWEL OF LAKES', 6),
            _ih('Day 07: SOUVENIR SHOPPING & FAREWELL TRIPURA', 7),
            _ih('TRAGUIN Signature Experience: A dedicated, private family coach ensuring plenty of room for luggage', 8),
            _ih('Curated by Experts: Selective restaurant stops featuring reliable hygiene and a broad variety of child-', 9),
            _ih('TRAGUIN Premium Holidays • TR-010 Page 6 of 7', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN AGARTALA – WELCOME TO THE CITY OF PALACES',
                (
                    'Arrive at Maharaja Bir Bikram Airport in Agartala, where your courteous TRAGUIN tour representative will warmly receive your family. Transfer via a private premium vehicle to your handpicked luxury hotel. After checking in and relaxing, head out for your first Tripura Sightseeing experience at the stunning Ujjayanta Palace. Walk through the sprawling Mughal-inspired fountains and gardens, and witness the patriotic flag-lowering ceremony at the Akhaura Indo-Bangladesh border in the evening.'
                ),
                [
                    'Sightseeing Included: Ujjayanta Palace, Akhaura Border Ceremony',
                    'Evening Experience: A wonderful walk around the beautifully lit palace compound.',
                    'Overnight Stay: Agartala (Premium Luxury Stay)',
                    'Meals Included: Dinner',
                ],
            ),
            _day(
                2,
                'SCENIC DRIVE TO JAMPUI HILLS – THE HIGHEST PEAK',
                (
                    'Enjoy a hearty family breakfast before checking out. Embark on an incredible, scenic drive towards the pristine Jampui Hills, ascending winding mountain roads lined with lush bamboo groves and small hill stations. Arrive by afternoon at this serene mountain retreat. Experience the welcoming culture of the local Mizo tribes, stroll through sweet-scented orange orchards (seasonal), and watch a spectacular sunset over the Chittagong Hill Tracts from Betlingship peak. Photography Points: Continuous panoramic mountain views from the Jampui ridge lines.'
                ),
                [
                    'Sightseeing Included: Betlingship Viewpoint, Tribal Village Walk, Orange Orchards',
                    'Overnight Stay: Jampui Hills (Premium Eco-Resort / Hill Cottages)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'MYSTICAL UNAKOTI ROCK CUTS – THE HILL OF WONDERS',
                (
                    'Savor a crisp morning breakfast in the hills. Travel down towards Kailashahar to explore Unakoti, the jewel of Tripura Sightseeing. Hike gently along mountain stairways to marvel at the massive 30-foot- tall rock-cut face of Lord Shiva (Unakotiswara Kal Bhairava) carved into the hill walls. Discover the surrounding stone carvings tucked away inside deep green forests, creating an immersive experience for children and adults alike.'
                ),
                [
                    'Sightseeing Included: Unakoti Archaeological Site, Central Shiva Reliefs',
                    'Optional Activities: Group family portraits against the giant ancient stone carvings.',
                    'Overnight Stay: Kailashahar / Kumarghat Premium Heritage Stay',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'ECO-TRAILS AT SEPAHIJALA WILDLIFE PARK & RETURN TO AGARTALA',
                (
                    "Following breakfast, journey back towards the capital city. En route, stop for an immersive family excursion at the lush Sepahijala Wildlife Sanctuary. Enjoy a peaceful family paddle-boating session on the lake and visit the nature park to spot the unique Phayre's Leaf Monkey (the state animal of Tripura). Arrive in Agartala by evening and check back into your luxury hotel."
                ),
                [
                    'Sightseeing Included: Sepahijala Wildlife Sanctuary, Botanical Gardens',
                    'Evening Experience: Relaxed evening leisure time to enjoy the premium hotel pool or amenities.',
                    'Overnight Stay: Agartala',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'SACRED UDAIPUR – HISTORIC TEMPLES & LAKES',
                (
                    'After breakfast, enjoy a short drive to the historical city of Udaipur, affectionately known as the city of lakes. Experience a seamless VIP entry at the iconic Tripura Sundari Temple (Matabari), one of the 51 revered Shakti Peethas. Gather around the historic Kalyan Sagar lake behind the temple to feed the ancient giant turtles. Afterwards, explore the beautifully weathered brick ruins of Bhuvneshwari Temple along the banks of the Gomati River. Food Suggestion: Try the famous hot local milk pedas served outside the Matabari shrine.'
                ),
                [
                    'Sightseeing Included: Matabari Temple, Kalyan Sagar Lake, Bhuvneshwari Temple, Jagannath Dighi',
                    'Overnight Stay: Agartala / Udaipur Luxury Retreat',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                6,
                'NEERMAHAL WATER PALACE – THE CROWN JEWEL OF LAKES',
                (
                    "Today features a highlight of your Premium Tripura Experience. After breakfast, head to Melaghar to explore the majestic Neermahal Water Palace. Board a private family motorboat to cross Rudrasagar Lake and reach this magnificent royal structure. Explore the Maharaja's summer suites, royal courtyards, and scenic pavilions. On your way back to Agartala, pause to see the Kasba Kali Temple overlooking the international border line."
                ),
                [
                    'Sightseeing Included: Neermahal Palace, Rudrasagar Family Boat Ride, Kasba Kali Temple',
                    'Evening Experience: A special farewell family dinner arranged at a premier restaurant in Agartala.',
                    'Overnight Stay: Agartala',
                    'Meals Included: Breakfast & Farewell Dinner',
                ],
            ),
            _day(
                7,
                'SOUVENIR SHOPPING & FAREWELL TRIPURA',
                (
                    'Relish your final breakfast at the hotel. Spend your morning at the Purbasha Government Emporium picking out authentic handwoven silk textiles, exquisite bamboo sculptures, and cane artifacts. Your private driver will drop your family safely at the Agartala Airport, concluding your incredible TRAGUIN Tripura Packages vacation with timeless stories and unforgettable memories.'
                ),
                [
                    'Meals Included: Breakfast',
                    'Assistance: Complete luggage handing and terminal gate drop-off assistance.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Polo Towers Agartala (Grand Family Suites)',
                'Agartala',
                '6N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                1,
                description='OPTION 01 – ULTRA LUXURY: Polo Towers Agartala (Grand Family Suites)',
            ),
            _hotel(
                'Ginger Agartala By IHCL / Hotel Sonar Tori (Premium Interconnected Rooms)',
                'Agartala',
                '6N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                2,
                description='OPTION 02 – LUXURY: Ginger Agartala By IHCL / Hotel Sonar Tori (Premium Interconnected Rooms)',
            ),
            _hotel(
                'Jampui Eden Tourist Lodge / Kailashahar Heritage Stay (Deluxe Cottages)',
                'Agartala',
                '6N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – PREMIUM: Jampui Eden Tourist Lodge / Kailashahar Heritage Stay (Deluxe Cottages)',
            )
        ],
        inclusions=[
            _inc_included('Handpicked family hotel stays with modern amenities.', 1),
            _inc_included('Daily premium breakfasts and multi-course buffet', 2),
            _inc_included('Private luxury AC SUV / Coach for all transfers &', 3),
            _inc_included('Private motorboat charter for the family at Neermahal.', 4),
            _inc_included('VIP quick-entry passes for Matabari Temple.', 5),
            _inc_included('Continuous guidance and full TRAGUIN Support.', 6),
            _inc_included('All state permits, highway tolls, and parking taxes.', 7),
            _inc_included('Handpicked family hotel stays with modern amenities. Daily premium breakfasts and multi-course buffet dinners. Private luxury AC SUV / Coach for all transfers & touring. Private motorboat charter for the family at Neermahal. VIP quick-entry passes for Matabari Temple. Continuous guidance and full TRAGUIN Support. All state permits, highway tolls, and parking taxes.', 8),
            _inc_excluded('Airfare or national train tickets to Agartala.', 9),
            _inc_excluded('Professional camera entry fees at archaeological', 10),
            _inc_excluded('Personal laundry, telephone bills, or alcoholic drinks.', 11),
            _inc_excluded('Travel insurance or emergency medical cover.', 12),
            _inc_excluded('Airfare or national train tickets to Agartala. Professional camera entry fees at archaeological monuments. Personal laundry, telephone bills, or alcoholic drinks. Travel insurance or emergency medical cover.', 13),
            _inc_excluded('All state permits, highway tolls, and parking taxes.', 14),
        ],
    )
    return package, itinerary

TRIPURA_TR_002_010_BUILDERS = [
    build_tr_002,
    build_tr_003,
    build_tr_004,
    build_tr_005,
    build_tr_006,
    build_tr_007,
    build_tr_008,
    build_tr_009,
    build_tr_010,
]
