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


def build_tr_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TRP-001'
    tour_code = 'TRAGUIN-TR-001'
    title = 'Agartala • Neermahal • Sepahijala • Unakoti • Udaipur'
    duration = '04 Nights / 05 Days'
    slug = 'tr-001-agartala-neermahal-sepahijala-unakoti-udaipur'
    itin_slug = 'tr-001-agartala-neermahal-sepahijala-unakoti-udaipur-itinerary'
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
            _ph('Serial code TRP-001 | TRAGUIN tour code TRAGUIN-TR-001', 1),
            _ph('State / Country: Tripura / India | Category: FAMILY VACATION', 2),
            _ph('Destinations: Agartala • Neermahal • Sepahijala • Unakoti • Udaipur', 3),
            _ph('Ideal for: Families, Culture Seekers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Luxury Innova / Crysta (Private) Meal Plan: | Route: TRAGUIN Premium Luxury Travels Page 1 of 6 MAPAI (Breakfast & Dinner Included) Agartala → Sepahijala → Neermahal ', 7),
            _ph('TRAGUIN Signature Experience: Private royal high-tea overlooking Ujjayanta Palace.✦', 8),
            _ph('Curated by TRAGUIN Experts: Custom-tailored low-pace itinerary perfectly suited for family comfort.✦', 9),
            _ph('Personalized Assistance: Dedicated on-ground coordinators managing priority entry points.✦', 10),
            _ph('Premium Handpicked Hotels: Properties scrutinized meticulously for hygiene, service, and luxury amenities.✦', 11)
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
        tagline='Agartala',
        overview='Tour Type: Premium Family Tour (FIT) Vehicle: Luxury Innova / Crysta (Private) Meal Plan: Route: TRAGUIN Premium Luxury Travels Page 1 of 6 MAPAI (Breakfast & Dinner Included) Agartala → Sepahijala → Neermahal → Udaipur → Unakoti → Agartala TRAGUIN Curated Experience Note: Every element of this Luxury Tripura Holiday has been handpicked by our destination experts. From seamless, comfortable private transfers ideal for families to curated local culinary degustations and prioritized palace entry permissions, TRAGUIN ensures a flawless and prestigious travel experience. WHY VISIT TRIPURA?',
        seo_title='TR-001 | Agartala | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Tripura package (TR-001 / TRAGUIN-TR-001): Agartala • Neermahal • Sepahijala • Unakoti • Udaipur with handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=True,
        highlights=[
            _ih('Day 01: AGARTALA', 1),
            _ih('Day 02: SEPAHIJALA & NEERMAHAL', 2),
            _ih('Day 03: UDAIPUR', 3),
            _ih('Day 04: UNAKOTI EXCURSION', 4),
            _ih('Day 05: AGARTALA DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private royal high-tea overlooking Ujjayanta Palace.✦', 6),
            _ih('Curated by TRAGUIN Experts: Custom-tailored low-pace itinerary perfectly suited for family comfort.✦', 7),
            _ih('Personalized Assistance: Dedicated on-ground coordinators managing priority entry points.✦', 8)
        ],
        days=[
            _day(
                1,
                'AGARTALA',
                (
                    'ROYAL ARRIVAL & IMMERSIVE HERITAGE EXPERIENCE IN THE CAPITAL Arrive at Maharaja Bir Bikram Airport in Agartala, where your dedicated luxury chauffeur and TRAGUIN representative welcome your family with traditional stoles and refreshing welcome amenities. Transfer seamlessly to your premium hotel in a luxury private vehicle. After checking in and relaxing, embark on your first evening of Tripura Sightseeing. Visit the magnificent Ujjayanta Palace, a stunning Greco-Roman structure built by Maharaja Radha Kishore Manikya, nestled in the heart of the capital surrounded by Mughal- style gardens. Witness the spectacular musical fountains in the evening, capturing timeless family memories at one of the most popular Instagram locations in the region.'
                ),
                [
                    'Sightseeing Included: Ujjayanta Palace, Heritage Gardens, Local Craft Emporium.',
                    'Evening Experience: Musical Fountain Show followed by a high-tea featuring traditional indigenous delicacies.',
                    'Overnight Stay: Handpicked Premium Hotel, Agartala.',
                    'Meals Included: Welcome Dinner.',
                ],
            ),
            _day(
                2,
                'SEPAHIJALA & NEERMAHAL',
                (
                    "WILDLIFE ENCOUNTERS & THE BREATHTAKING WATER PALACE OF THE EAST Savor a lavish breakfast before driving through scenic rubber plantations to the Sepahijala Wildlife Sanctuary, a biodiverse haven famous as the home of the rare Phayre's Langur (Spectacled Monkey). Enjoy a curated private golf-cart safari through the sanctuary, an exceptional highlight for both children and elders. Continue your journey to Melaghar to witness the crowning jewel of your Luxury Tripura Holiday—the iconic Neermahal Water Palace. Situated right in the center of the shimmering Rudrasagar Lake, this fairytale palace blends Hindu and Islamic architectural forms perfectly. Board a private motorboat across the lake to explore the royal pavilions, open-air courtyards, and enchanting light reflections that redefine premium luxury storytelling."
                ),
                [
                    'Sightseeing Included: Sepahijala Wildlife Sanctuary, Rudrasagar Lake, Neermahal Water Palace.',
                    'Optional Activities: Boating and migratory bird photography on Rudrasagar Lake.',
                    'Overnight Stay: Premium Heritage Resort, Melaghar / Agartala.',
                    'Meals Included: Breakfast & Gourmet Dinner.',
                ],
            ),
            _day(
                3,
                'UDAIPUR',
                (
                    'SPIRITUAL ODYSSEY TO THE SACRED MATABARI & ROYAL LAKES Following a wonderful breakfast, proceed to Udaipur, historically known as Rangamati, the ancient capital of the Manikya kings. Here, your family will experience deep spiritual tranquility at the revered Tripura Sundari Temple (Matabari), one of the 51 sacred Shakti Peethas. TRAGUIN arranges a VIP expedited Darshan for your family to ensure complete comfort for senior citizens. Walk along the Kalyan Sagar lake situated behind the temple to feed the historic giant tortoises. Later, explore the spectacular ruins of Bhubaneswari Temple on the banks of the Gomati River, immortalized in Rabindranath Tagore’s famous plays, offering an immersive cultural experience found nowhere else.'
                ),
                [
                    'Sightseeing Included: Tripura Sundari Temple, Kalyan Sagar, Bhubaneswari Temple, Gunabati Group of Temples.',
                    'Evening Experience: Serene lakeside walk and traditional evening Aarti experience.',
                    'Overnight Stay: Handpicked Premium Hotel, Agartala / Udaipur.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                4,
                'UNAKOTI EXCURSION',
                (
                    'MYSTICAL ROCK-CUT CARVINGS & RUGGED SCENIC BEAUTY Dedicate today to a legendary highlight of your TRAGUIN Tripura Packages—a private excursion to Unakoti, meaning "one less than a crore" in Bengali. Deep inside the lush green hills of Northern Tripura, marvel at the colossal rock-cut bas-relief sculptures dating back to the 7th–9th centuries. The centerpiece is the awe- inspiring 30-foot-tall Unakotiswara Kal Bhairava carving. Walk along the beautifully maintained paths while our expert guide narrates fascinating mythological legends of Lord Shiva\'s journey. This site represents a gold- standard destination for unparalleled family photography and breathtaking natural heritage. Return to Agartala through rolling hills and picturesque tea gardens.'
                ),
                [
                    'Sightseeing Included: Unakoti Rock Carvings, Central Shiva Relief, Hillside Waterfalls, Local Tea Estate.',
                    'Optional Activities: Interactive tea-leaf plucking experience and interaction with local artisans.',
                    'Overnight Stay: Premium Luxury Hotel, Agartala.',
                    'Meals Included: Breakfast & Grand Farewell Dinner.',
                ],
            ),
            _day(
                5,
                'AGARTALA DEPARTURE',
                (
                    'SOUVENIR HUNTING & FOND FAREWELLS On your final morning of this spectacular Tripura Family Tour, enjoy a relaxed gourmet breakfast. Visit the local Purbasha Handloom and Handicrafts Emporium to buy premium, globally acclaimed bamboo screens, exquisite cane furniture, and authentic tripuri handloom sarees. Your luxury vehicle will then escort you comfortably to the Maharaja Bir Bikram Airport for your departure flight. Return home with unforgettable memories and stories of royal luxury, proudly curated by TRAGUIN.'
                ),
                [
                    'Sightseeing Included: Purbasha Handicrafts Emporium, Albert Ekka War Memorial.',
                    'Meals Included: Sumptuous Buffet Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Welcome Palace / Ginger Agartala Executive Room MAPAI (Breakfast & Dinner) TRAGUIN Premium Luxury Travels Page 4 of 6 CATE',
                'Agartala',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Welcome Palace / Ginger Agartala Executive Room MAPAI (Breakfast & Dinner) TRAGUIN Premium Lux',
            ),
            _hotel(
                'Hotel Polo Towers Agartala Premier Room MAPAI (Breakfast & Dinner)',
                'Agartala',
                '4N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Hotel Polo Towers Agartala Premier Room MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Tripura Castle Heritage Stay / Polo Towers Luxury Suite MAPAI (Breakfast & Dinner)',
                'Agartala',
                '4N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Tripura Castle Heritage Stay / Polo Towers Luxury Suite MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'TRAGUIN Signature Heritage Villa Selection Royal Presidential Suite Premium Curated Meals',
                'Agartala',
                '4N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Signature Heritage Villa Selection Royal Presidential Suite Premium Curated Meals',
            )
        ],
        inclusions=[
            _inc_included('transfers and sightseeing.', 1),
            _inc_included('selected luxury tier.', 2),
            _inc_included('all transfers and sightseeing.', 3),
            _inc_included('stoles and fresh fruits.', 4),
            _inc_included('at Neermahal & VIP Darshan at Matabari.', 5),
            _inc_excluded('explicitly stated.', 6),
            _inc_excluded('alcoholic beverages.', 7),
            _inc_excluded('performances.', 8),
            _inc_excluded('standard booking.', 9),
        ],
    )
    return package, itinerary

TRIPURA_TR_001_BUILDERS = [
    build_tr_001,
]
