"""Builder functions for CH-007 through CH-019 Chandigarh domestic packages (Punjab destination)."""

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

PUNJAB_DESTINATION_ID = "d4119569-a154-460e-af8e-6eb006ea76f9"


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


def build_ch_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "CH-007"
    tour_code = "TRAGUIN-CH-007"
    title = "Chandigarh & Pinjore Garden Excursion Premium Family Tour"
    duration = "03 Nights / 04 Days"
    slug = "ch-007-chandigarh-pinjore-garden-excursion-premium-family-tour"
    itin_slug = "ch-007-chandigarh-pinjore-garden-itinerary"
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
            _ph("State / Country: Chandigarh, India | Category: Premium Family Getaway", 2),
            _ph("Destinations: Chandigarh City • Sukhna Lake • Rock Garden • Pinjore Mughal Gardens", 3),
            _ph("Ideal for: Families, Leisure Groups & Couples", 4),
            _ph("Best season: September to March", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Private air-conditioned luxury sedan/SUV, local expert guides, sunset boating at Sukhna Lake", 7),
            _ph("TRAGUIN Signature Experience: private family-friendly local interactions and pre-verified seating for garden light shows", 8),
            _ph("Shopping: phulkari dupattas, traditional leather juttis, organic wooden crafts, clay pottery", 9),
            _ph("Cuisine: authentic Punjabi chole bhature, butter chicken at Sector 7, sweet lassi in clay glasses", 10),
            _ph("Travel note: book 5-star properties early; best weather October to March for garden strolls", 11),
        ],
        moods=["Family", "Luxury", "Cultural"],
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
        tagline="An Architectural Masterpiece and Imperial Mughal Heritage Wrapped in Absolute Luxury",
        overview=(
            "Welcome to Chandigarh, India's first planned urban marvel, universally recognized for its unparalleled "
            "architectural layout, grand open vistas, and incredible green spaces. This beautifully balanced Best "
            "Chandigarh Tour Package is thoughtfully orchestrated as a high-end Chandigarh Family Tour and luxury "
            "escape. Perfectly curated by TRAGUIN, this exclusive journey offers your family premium stays at "
            "handpicked hotels, dynamic private luxury transportation, and highly curated experiences that cater "
            "effortlessly to every generation.\n\n"
            "From the dreamlike configurations of the Rock Garden to the timeless royal terraces of Pinjore Gardens, "
            "every detail is elevated by the constant support of TRAGUIN experts to give your loved ones "
            "unforgettable memories.\n\n"
            "TRAGUIN Curated Experience Note: Private air-conditioned luxury sedan/SUV throughout the itinerary, "
            "local expert guides at heritage locations, pre-arranged sunset boating cruise at Sukhna Lake, and "
            "curated breakfast & dinner selections.\n\n"
            "Why schedule a Luxury Chandigarh Holiday? Known as the \"The Beautiful City\", Chandigarh seamlessly "
            "links cosmopolitan infrastructure with historic treasures, claiming some of the highest-rated Top "
            "Tourist Places in Chandigarh. This Premium Chandigarh Experience is ideal for families seeking an "
            "enriching blend of modern landscape art, local shopping expeditions, and majestic Mughal history. "
            "Discover the Best Time to Visit Chandigarh with our exclusive TRAGUIN Chandigarh Packages, highlighting "
            "the region's best culinary stops and most popular Instagram locations for capturing beautiful family "
            "moments."
        ),
        seo_title=f"{serial} | Chandigarh & Pinjore Garden Excursion Family Tour | TRAGUIN",
        seo_description=(
            f"Premium {duration} Chandigarh family package ({serial} / {tour_code}): Sukhna Lake shikhara cruise, "
            "Rock Garden, Rose Garden, Open Hand Monument, Pinjore Mughal Gardens, and handpicked 4-tier hotel options."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Sukhna Lake Waterfront & Private Shikhara Sunset Cruise", 1),
            _ih("Rock Garden — Nek Chand's recycled-material masterpiece", 2),
            _ih("Zakir Hussain Rose Garden — Asia's largest botanical rose sanctuary", 3),
            _ih("Le Corbusier Open Hand Monument", 4),
            _ih("Pinjore Mughal Terraces — Yadavindra Gardens light show", 5),
            _ih("Sector 17 & Elante boutique shopping", 6),
            _ih("Curated by TRAGUIN Experts with paced family-friendly routing", 7),
        ],
        days=[
            _day(
                1,
                "Arrival in Chandigarh & Sukhna Lake Sunset",
                (
                    "Your family's premium vacation springs to life upon arriving at Chandigarh Airport or Railway "
                    "Station. A designated luxury representative from TRAGUIN will greet you warmly and escort your "
                    "family in a spacious private vehicle to your premium handpicked hotel. Following a priority "
                    "check-in and short relaxation period, head out to the iconic Sukhna Lake located at the foothills "
                    "of the Shivalik range. A private shikhara boat ride is exclusively organized for your family by "
                    "TRAGUIN. Glide peacefully over the calm water as the gold and pastel hues of the setting sun "
                    "outline the mountains. Spend your evening exploring the lively waterfront path."
                ),
                [
                    "Sightseeing Included: Sukhna Lake Waterfront, Shivalik Foothills Promenade",
                    "Meals Included: Luxury Buffet Dinner",
                    "Evening Experience: Private family shikhara boat cruise",
                    "Overnight Stay: Handpicked Premium Hotel in Chandigarh",
                ],
            ),
            _day(
                2,
                "Architectural Wonders & Design Cores",
                (
                    "Savor a premium breakfast before exploring the world-famous Rock Garden, an unbelievable "
                    "open-air labyrinth created entirely from recycled industrial and domestic waste material by Nek "
                    "Chand. Wander through majestic waterfalls, artificial plazas, and hundreds of whimsical stone-"
                    "crafted sculptures that serve as a brilliant backdrop for family photographs. Next, take a short "
                    "drive to the Zakir Hussain Rose Garden, Asia's largest botanical rose sanctuary, boasting more "
                    "than 50,000 carefully curated rose varieties. Conclude your daylight hours by capturing photos at "
                    "Le Corbusier's iconic Open Hand Monument, the grand symbol of peace and prosperity."
                ),
                [
                    "Sightseeing Included: Rock Garden, Rose Garden, Sector 17 Plaza, Open Hand Monument",
                    "Meals Included: Gourmet Breakfast & Elegant Dinner",
                    "Photography Points: Recycled glass-bangle walls & blooming rose pathways",
                    "Overnight Stay: Handpicked Premium Hotel in Chandigarh",
                ],
            ),
            _day(
                3,
                "Pinjore Mughal Gardens Excursion",
                (
                    "Embark on a magnificent morning excursion to the historical Pinjore Gardens (also known as "
                    "Yadavindra Gardens), situated a short, comfortable drive outside the main city hub. This "
                    "17th-century architectural masterpiece is built across seven descending multi-level terraces in "
                    "the classic Mughal style. Walk past lines of pristine fountains, grand cypress trees, and historic "
                    "palaces including the Shish Mahal and Hawa Mahal. As dusk approaches, watch the gardens transform "
                    "into a magical wonderland as lights illuminate the historic fountains. Return to Chandigarh in the "
                    "evening for an elite dining experience at a renowned traditional restaurant."
                ),
                [
                    "Sightseeing Included: Pinjore Mughal Terraces, Shish Mahal Pavilion, Illuminated Waterways",
                    "Meals Included: Gourmet Breakfast & Traditional Fine-Dining Dinner",
                    "Exclusive Touch: Reserved premium seating at the royal heritage garden zone",
                    "Overnight Stay: Handpicked Premium Hotel in Chandigarh",
                ],
            ),
            _day(
                4,
                "Local Cultural Commerce & Departure",
                (
                    "Enjoy a relaxed breakfast at your hotel. Spend your final morning browsing the high-end boutique "
                    "stores and craft markets of the famous Sector 17 or Elante complex to pick up souvenirs like "
                    "authentic Punjabi juttis and traditional phulkari textiles. Following a leisurely lunch, your "
                    "private luxury transport driven by a professional chauffeur will ensure a smooth transfer to the "
                    "Chandigarh Airport or Railway Station for your journey home. Return with happy hearts, a refreshed "
                    "bond with your loved ones, and unforgettable memories from your luxury travel itinerary managed "
                    "seamlessly by TRAGUIN."
                ),
                [
                    "Sightseeing Included: Elante Shopping / Sector 17 Craft Boutiques",
                    "Meals Included: Gourmet Breakfast Only",
                    "Transfers: Air-conditioned private luxury departure transfer",
                ],
            ),
        ],
        hotels=[
            _hotel("Lemon Tree Hotel Chandigarh / Hyatt Place", "Chandigarh", "03 Nights", "Deluxe", "Executive Superior Room", "MAP Plan (Breakfast & Dinner)", 4, 1),
            _hotel("The Lalit Chandigarh / Radisson City Centre", "Chandigarh", "03 Nights", "Premium", "Premium Club View Room", "MAP Plan (Breakfast & Dinner)", 5, 2),
            _hotel("Hyatt Regency Chandigarh / Taj Chandigarh", "Chandigarh", "03 Nights", "Luxury", "Luxury Regency / Club Heritage Room", "MAP Plan (Gourmet Double Tier)", 5, 3),
            _hotel("The Oberoi Sukhvilas Spa Resort, New Chandigarh", "New Chandigarh", "03 Nights", "Ultra Luxury", "Premier Luxury Tent / Luxury Villa with Pool", "Bespoke Curated Meal Plan", 5, 4),
        ],
        inclusions=[
            _inc_included("03 Nights premium luxury accommodation at top handpicked properties", 1),
            _inc_included("Daily gourmet buffet breakfasts and fine-dining multi-cuisine dinners", 2),
            _inc_included("Chauffeured private luxury AC vehicle dedicated for all transfers and tours", 3),
            _inc_included("Complimentary private family shikhara cruise voucher at Sukhna Lake", 4),
            _inc_included("All entry tickets and monument passes for Rock Garden and Pinjore Gardens", 5),
            _inc_included("Reliable, round-the-clock TRAGUIN support and guest concierge services", 6),
            _inc_included("All toll charges, state parking fees, driver allowances, and service taxes", 7),
            _inc_excluded("Inbound or outbound airfares and long-distance train tickets", 8),
            _inc_excluded("Personal hotel expenses such as laundry, phone calls, and mini-bar items", 9),
            _inc_excluded("Optional recreational activities, professional cameras fees, or sports rentals", 10),
            _inc_excluded("Extra meals or beverage packages not mentioned in the inclusions", 11),
            _inc_excluded("Comprehensive travel insurance and medical emergency coverage", 12),
        ],
    )
    return package, itinerary


def build_ch_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'CH-008'
    tour_code = 'TRAGUIN-CH-008'
    title = 'Complete Tricity & Shivalik Foothills Premium Chandigarh Family Tour'
    duration = '05 Nights / 06 Days'
    slug = 'ch-008-complete-tricity-shivalik-foothills-premium-chandigarh-family-tour'
    itin_slug = 'ch-008-complete-tricity-shivalik-foothills-itinerary'
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
                    _ph('Serial code CH-008 | TRAGUIN tour code TRAGUIN-CH-008', 1),
            _ph('State / Country: Chandigarh (Tricity), India | Category: Complete Tricity & Foothills Family Tour', 2),
            _ph('Destinations: Chandigarh • Panchkula • Mohali • Pinjore Gardens • Shivalik Foothills', 3),
            _ph('Ideal for: Families, Corporate Retreats & Leisure Seekers', 4),
            _ph('Best season: September to April (Pleasant Year-Round)', 5),
            _ph('Starting price: On Request (Premium Collection)', 6),
            _ph('Dedicated private AC luxury sedan/SUV and local heritage guides at monumental locations', 7),
            _ph('TRAGUIN Signature Experience: private local storytelling guides fluent in multiple languages', 8),
            _ph('Shopping: designer Punjabi Phulkari embroidery, handcrafted juttis, organic honey, walnut crafts', 9),
            _ph('Cuisine: slow-cooked dal makhani, butter chicken, fresh mint lassi in earthen clay cups', 10)
        ],
        moods=['Family', 'Luxury', 'Cultural'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Collection)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='An Architectural Masterpiece Blended with Scenic Beauty, Curated Experiences, and Urban Luxury',
        overview=(
            "Welcome to Chandigarh, the architectural pride of India and famously known as the 'City Beautiful'. Nestled perfectly against the breathtaking landscapes of the Shivalik Foothills, this masterfully planned destination seamlessly integrates wide green avenues with premium lifestyle facilities. This ultra-exclusive Best Chandigarh Tour Package is curated specifically as an immersive Chandigarh Family Tour and top-tier holiday experience.\n\nEvery element of this grand journey is refined by TRAGUIN signature experts. From private premium stays in handpicked hotels to a personal chauffeured luxury vehicle and continuous, round-the-clock TRAGUIN personalized assistance, your family is guaranteed maximum relaxation and unforgettable memories.\n\nTRAGUIN Curated Experience Details: Dedicated private AC luxury sedan/SUV, premium accommodation at top-rated family-friendly properties, daily multi-cuisine buffet breakfasts and dinners, local heritage guides at monumental locations, and special entry passes.\n\nWhy pick this spectacular Luxury Chandigarh Holiday? Chandigarh stands as a beacon of meticulous French architectural planning and pristine greenery, hosting the absolute Top Tourist Places in Chandigarh. Let TRAGUIN Chandigarh Packages create a flawless vacation layout for your loved ones."
        ),
        seo_title='CH-008 | Complete Tricity & Shivalik Foothills Family Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Chandigarh family package (CH-008 / TRAGUIN-CH-008): Sukhna Lake Shikara cruise, Rock Garden, Tricity exploration, Pinjore Mughal Gardens, Shivalik Foothills leisure, and 4-tier hotels.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
                    _ih('Sukhna Lake Sunset Shikara-Style Private Boat Cruise', 1),
            _ih('Nek Chand Rock Garden & Capitol Complex UNESCO Zone', 2),
            _ih('Tricity Exploration — Mohali Cricket Stadium & Mansa Devi Shrine', 3),
            _ih('Pinjore Mughal Gardens Illuminated Night Garden Walk', 4),
            _ih('Optional Shivalik Foothills Timber Trail Cable Car Excursion', 5),
            _ih('Curated by TRAGUIN Experts with paced family-friendly routing', 6)
        ],
        days=[
        _day(
    1,
    'Arrival in Chandigarh & Sukhna Lake Sunset Cruise',
    (
        'Your family vacation starts as your flight or train arrives in Chandigarh. A dedicated TRAGUIN guest executive will receive you with a traditional warm welcome and escort you in a premium private luxury vehicle to your selected premium hotel. After an effortless express check-in, unwind in your spacious executive quarters. In the late afternoon, enjoy a scenic drive down the wide, tree-lined boulevards to the iconic Sukhna Lake. A private Shikara-style boat ride is exclusively arranged for your family to glide across the calm waters as the sun dips behind the distant Shivalik Foothills, creating beautiful gold and purple reflections.'
    ),
    [
        'Sightseeing Included: Sukhna Lake Promenade, Waterfront Shaded Track',
        'Meals Included: Luxury Buffet Dinner',
        'Evening Experience: Private family boat cruise & lakeside walking interactions',
        'Overnight Stay: Handpicked Premium Hotel in Chandigarh'
    ],
),
_day(
    2,
    'Architectural Marvels & Artistic Visions',
    (
        "Savor a delightful gourmet breakfast before starting an incredible Chandigarh Sightseeing expedition. Our first stop is the world-renowned Rock Garden, a massive 40-acre wonderland featuring thousands of sculptures sculpted entirely out of broken glass, pottery tiles, and discarded industrial waste by master creator Nek Chand. Next, visit the nearby Capitol Complex, Le Corbusier's UNESCO World Heritage design, where your personal guide highlights the symbolism behind the majestic Open Hand Monument. In the afternoon, take a relaxed stroll through Zakir Hussain Rose Garden, Asia's largest botanical sanctuary housing over 16,000 unique varieties of roses."
    ),
    [
        'Sightseeing Included: Rock Garden, Rose Garden, Capitol Complex Architectural Zone',
        'Meals Included: Buffet Breakfast & Premium Dinner',
        'Photography Points: Massive waterfalls in Rock Garden & colorful rose fields',
        'Overnight Stay: Handpicked Premium Hotel in Chandigarh'
    ],
),
_day(
    3,
    'Tricity Exploration (Mohali & Panchkula)',
    (
        'After a rich family breakfast, your private luxury transport routes you across the smooth avenues of the Tricity. Drive past the world-class Mohali International Cricket Stadium, capturing grand photos of this legendary sporting venue. Next, transition to the scenic hillsides of Panchkula to pay your respects at the ancient, highly revered Mata Mansa Devi Temple, built in pristine traditional style. Spend your afternoon exploring the elite Elante Mall, the premium shopping center of the region.'
    ),
    [
        'Sightseeing Included: Mohali Cricket Stadium (Exterior), Mansa Devi Shrine, Elante Luxury Zone',
        'Meals Included: Buffet Breakfast & Premium Dinner',
        'Food Suggestions: Authentic Punjabi artisanal clay-oven flatbreads & rich milk sweets',
        'Overnight Stay: Handpicked Premium Hotel in Chandigarh'
    ],
),
_day(
    4,
    'The Mughal Majesty of Pinjore Gardens',
    (
        'Today takes your family slightly outside the main city borders towards the historic town of Pinjore, nestled right at the base of the Shivalik Foothills. Explore Yadavindra Gardens, a masterfully executed 17th-century Mughal layout built across seven grand descending terraces. Walk beneath shaded orchards of mango trees and watch hundreds of historic, synced water fountains dance alongside stone canals. Explore the royal structures of Sheesh Mahal and Rang Mahal. In the evening, watch the entire terraced garden illuminate beautifully with hidden amber lights.'
    ),
    [
        'Sightseeing Included: Pinjore Mughal Gardens, Bhima Devi Temple Heritage Ruins',
        'Meals Included: Buffet Breakfast & Premium Dinner',
        'Exclusive Experience: Special illuminated night garden walk with royal narration',
        'Overnight Stay: Handpicked Premium Hotel in Chandigarh'
    ],
),
_day(
    5,
    'Shivalik Foothills Leisure Retreat',
    (
        'This day is kept beautifully flexible and optimized for ultimate luxury relaxation. Savor a late breakfast at your own pace. Choose to take an unforgettable, optional excursion into the Shivalik Foothills to experience the famous Timber Trail. Board a safe, exhilarating Swiss-built cable car that glides seamlessly across deep, pine-covered mountain gorges to a quiet hill resort perched atop a mountain peak. Return to Chandigarh for a relaxed evening of local leisure walking or premium spa rejuvenation.'
    ),
    [
        'Sightseeing Included: Shivalik Foothills Drive, Optional Cable Car Excursion',
        'Meals Included: Buffet Breakfast & Grand Farewell Dinner',
        'Evening Experience: Specially curated multi-course culinary farewell menu',
        'Overnight Stay: Handpicked Premium Hotel in Chandigarh'
    ],
),
_day(
    6,
    'Farewell Chandigarh Departure',
    (
        'Savor your final morning buffet breakfast at the resort lounge. Take a quiet moment to admire the neat, green urban landscapes before packing your baggage. Your private luxury vehicle driven by a professional chauffeur will arrive right on schedule at the hotel lobby. Enjoy a comfortable executive transfer back to Chandigarh Airport or Railway Station for your onward journey.'
    ),
    [
        'Transfers: Hotel to Airport/Station drop via private luxury vehicle',
        'Meals Included: Buffet Breakfast Only'
    ],
)
        ],
        hotels=[
                    _hotel('Hotel Mountview Chandigarh / Lemon Tree', 'Chandigarh', '05 Nights', 'Deluxe', 'Premium Executive Deluxe Room', 'MAPAI (Breakfast & Dinner)', 4, 1),
            _hotel('The Lalit Chandigarh / Radisson Red Mohali', 'Chandigarh', '05 Nights', 'Premium', 'Luxury Premier Room', 'MAPAI (Breakfast & Dinner)', 5, 2),
            _hotel('Hyatt Regency Chandigarh / Taj Chandigarh', 'Chandigarh', '05 Nights', 'Luxury', 'Club View Luxury Room', 'MAPAI (Premium Buffet Access)', 5, 3),
            _hotel('The Oberoi Sukhvilas Spa Resort (Shivalik Foothills)', 'New Chandigarh', '05 Nights', 'Ultra Luxury', 'Premier Luxury Tent / Private Pool Villa', 'Bespoke Customized Curated Meals', 5, 4),
        ],
        inclusions=[
                    _inc_included('05 Nights luxury accommodation in selected top-tier handpicked hotels', 1),
            _inc_included('Daily premium buffet breakfasts and grand multi-cuisine dinners', 2),
            _inc_included('Chauffeured private AC luxury transportation for all transfers & sightseeing', 3),
            _inc_included('Complimentary Shikara-style family boat cruise on Sukhna Lake', 4),
            _inc_included('Pre-arranged VIP access tickets at Pinjore Gardens and Rock Garden', 5),
            _inc_included('Round-the-clock personalized TRAGUIN support and family care assistance', 6),
            _inc_included('All toll charges, state fuel surcharges, driver allowances, and service taxes', 7),
            _inc_excluded('Inbound or outbound long-distance airfares or railway ticketing', 8),
            _inc_excluded('Personal expenses like luxury spa therapies, laundry, and mini-bar billing', 9),
            _inc_excluded('Optional Timber Trail cable car tickets or high-adventure ride fees', 10),
            _inc_excluded('Camera passes, video recording tickets, or monument fees not listed', 11),
            _inc_excluded('Comprehensive individual medical and travel insurance premiums', 12),
        ],
    )
    return package, itinerary

def build_ch_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'CH-009'
    tour_code = 'TG-CH-009-PREM'
    title = 'Rock Garden & Rose Garden Quick Premium Escape'
    duration = '01 Night / 02 Days'
    slug = 'ch-009-rock-garden-rose-garden-quick-premium-escape'
    itin_slug = 'ch-009-rock-garden-rose-garden-itinerary'
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
                    _ph('Serial code CH-009 | TRAGUIN tour code TG-CH-009-PREM', 1),
                    _ph('State / Country: Chandigarh / India | Category: Weekend Getaway', 2),
                    _ph('Destinations: Rock Garden • Rose Garden • Sukhna Lake', 3),
                    _ph('Ideal for: Couples, Families & Solo Elite Travelers', 4),
                    _ph('Best season: Year-round (Best from Oct to Mar)', 5),
                    _ph('Travel Format: Private Independent Travel (FIT Portfolio)', 6),
                    _ph('TRAGUIN Signature Experience: Private curated sunset boat cruise and personalized local architectural map presentation', 7),
                    _ph('Shopping: Sector 17 Shopping Plaza, Phulkari embroidery, Punjabi Juttis', 8)
        ],
        moods=['Romantic', 'Luxury', 'Cultural'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Weekend Escape)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Discover the elegant architectural precision and natural mastery of India's most beautifully planned urban oasis",
        overview=(
            'Escape the mundane with our finely tailored Premium Chandigarh Experience. This high-end weekend tour is perfectly organized for guests who demand seamless logistics, professional local insights, and relaxed exploration. From your choice of elite luxury accommodations to an entirely private sightseeing rhythm, TRAGUIN handles every operational detail so you can indulge in the true spirit of the City of Joy.\n\nTravel Format: Private Independent Travel (FIT Portfolio). Vehicle: Private Premium Sedan / SUV with professional uniformed chauffeur. Meal Plan: Modified American Plan (Continental Breakfast & Gourmet Dinner Included). Route Map: Chandigarh Arrival → Rock Garden Exploration → Sukhna Lake Cruise → Rose Garden Walk → Elite Departure.\n\nTRAGUIN Curated Touch: Pre-booked skip-the-line VIP entry passes, luxury vehicle refreshments, and highly personalized timing mapping.'
        ),
        seo_title='CH-009 | Rock Garden & Rose Garden Quick Premium Escape | TRAGUIN',
        seo_description='Premium 01 Night / 02 Days Chandigarh weekend package (CH-009 / TG-CH-009-PREM): Rock Garden, Sukhna Lake sunset boating, Rose Garden, and handpicked 4-tier hotels.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
                    _ih('Nek Chand Rock Garden VIP Visit', 1),
                    _ih('Private Sunset Boating at Sukhna Lake', 2),
                    _ih('Zakir Hussain Rose Garden Botanical Walk', 3),
                    _ih('Open Hand Monument Drive', 4),
                    _ih('Curated by TRAGUIN Experts with seamless crowd-free pacing', 5)
        ],
        days=[
        _day(
            1,
            'Chandigarh Arrival • Artistic Marvels & Sunset Lakeside Cruise',
            (
                'Your premium weekend escape begins with a warm welcome as your dedicated TRAGUIN chauffeur meets you at Chandigarh Airport, Railway Station, or your preferred nearby location. Relax inside your private luxury vehicle as you transfer smoothly to your handpicked premium hotel for an effortless check-in. In the afternoon, dive into the creative genius of Chandigarh Sightseeing with a VIP visit to the world-renowned Rock Garden. Marvel at the visionary work of Nek Chand, who transformed discarded industrial and domestic waste into a striking labyrinth of majestic ceramic courts, waterfalls, and stone sculptures. Following this artistic immersion, take a short drive to the peaceful Sukhna Lake just as the sun begins to set. Enjoy a private, curated boating experience on the calm waters, capturing breathtaking landscapes against the Shivalik hills. Wrap up your evening with a gourmet dinner at your premium hotel.'
            ),
            [
                "Sightseeing Included: Nek Chand's Rock Garden, Sukhna Lake Waterfront",
                'Evening Experience: Private Sunset Boating & Lakefront Promenade Walk',
                'Overnight Stay: Chandigarh (Premium / Luxury Selected Hotel)',
                'Meals Included: Gourmet Welcome Dinner'
            ],
        ),
        _day(
            2,
            'Botanical Majesty, Architectural Iconics & Departure',
            (
                "Awaken to a delicious, multi-cuisine continental breakfast at your hotel before embarking on a beautiful morning excursion. Today we explore the stunning Zakir Hussain Rose Garden, Asia's largest botanical garden dedicated entirely to roses. Stroll along manicured paths lined with over 1,600 distinct varieties of roses, capturing exceptional photography points where vibrant petals stretch as far as the eye can see. Next, enjoy a brief driving tour of the famous Capitol Complex and the iconic Open Hand Monument. In the afternoon, indulge in premium boutique shopping or explore fine cafes around the upscale Sector 17 or Elante luxury arcades. Later, your chauffeur will provide a smooth, comfortable transfer back to the airport or railway station as your memorable weekend journey concludes."
            ),
            [
                'Sightseeing Included: Zakir Hussain Rose Garden, Open Hand Monument Drive',
                'Optional Activities: Premium high-street shopping & cafe exploration',
                'Overnight Stay: Tour Concludes / Departure Transfer',
                'Meals Included: Full Buffet Breakfast'
            ],
        )
        ],
        hotels=[
                    _hotel('Lemon Tree Hotel / Hyatt Centric', 'Chandigarh', '01 Night', 'Deluxe', 'Superior Deluxe Room', 'Breakfast & Dinner', 4, 1),
                    _hotel('Novotel Chandigarh Tribune Chowk / Radisson', 'Chandigarh', '01 Night', 'Premium', 'Executive Premium Room', 'Breakfast & Dinner', 5, 2),
                    _hotel('Hyatt Regency Chandigarh / Taj Chandigarh', 'Chandigarh', '01 Night', 'Luxury', 'Club Luxury Heritage Room', 'Breakfast & Dinner', 5, 3),
                    _hotel('The Oberoi Sukhvilas Spa Resort, New Chandigarh', 'New Chandigarh', '01 Night', 'Ultra Luxury', 'Premier Luxury Valley Tent / Villa', 'All-Inclusive Curated Map', 5, 4),
        ],
        inclusions=[
                    _inc_included('01 Night luxury accommodation in premium handpicked hotels', 1),
                    _inc_included('Daily breakfast and custom gourmet dinners at the hotel restaurant', 2),
                    _inc_included('Private luxury transportation with a professional uniformed chauffeur', 3),
                    _inc_included('Pre-booked VIP skip-the-line entrance tickets to the Rock Garden', 4),
                    _inc_included('Private sunset boating experience vouchers on Sukhna Lake', 5),
                    _inc_included('Chilled mineral water, wet tissues, and premium travel snacks inside the vehicle', 6),
                    _inc_included('Comprehensive TRAGUIN support throughout the entire weekend trip', 7),
                    _inc_included('All applicable fuel charges, parking fees, driver allowances, and state toll taxes', 8),
                    _inc_excluded('Flights, rail bookings, or interstate long-distance tickets', 9),
                    _inc_excluded('Personal expenses such as laundry, phone calls, or spa sessions', 10),
                    _inc_excluded('Lunch meals, local alcohol, or specialized private cafe orders', 11),
                    _inc_excluded('Camera, video recording, or professional drone photography fees', 12),
                    _inc_excluded('Personal travel or medical insurance tracking policies', 13),
                    _inc_excluded('Tips for your driver or local monument guides', 14),
        ],
    )
    return package, itinerary

def build_ch_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'CH-010'
    tour_code = 'TG-CH-010-PREM'
    title = 'Premium Chandigarh Urban Architecture Break'
    duration = '02 Nights / 03 Days'
    slug = 'ch-010-premium-chandigarh-urban-architecture-break'
    itin_slug = 'ch-010-chandigarh-urban-architecture-itinerary'
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
                    _ph('Serial code CH-010 | TRAGUIN tour code TG-CH-010-PREM', 1),
                    _ph('State / Country: Chandigarh / India | Category: Leisure Break', 2),
                    _ph('Destinations: Chandigarh Urban Oasis', 3),
                    _ph('Ideal for: Couples, Architects & Families', 4),
                    _ph('Best season: September to March', 5),
                    _ph('Private solar boat cruise at Sukhna Lake', 6),
                    _ph('TRAGUIN Signature Experience: Private architecture walks led by design experts', 7),
                    _ph('Shopping: Sector 17 Market, Phulkari embroidery, Open Hand miniature emblems', 8)
        ],
        moods=['Luxury', 'Cultural', 'Family'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Architecture Break)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Sukhna Lake • Rock Garden • Rose Garden • Capitol Complex',
        overview=(
            'Welcome to Chandigarh, the iconic "City Beautiful" masterminded by the legendary modernist architect Le Corbusier. This ultra-premium weekend getaway, crafted meticulously by TRAGUIN holiday planners, is designed for discerning travelers who wish to experience elite modernist design blended seamlessly with serene natural settings.\n\nTravel Format: Private Independent Travel (FIT) with Elite Concierge Support. Vehicle: Premium Private Chauffeur-Driven Luxury Sedan / SUV. Meal Plan: Modified American Plan (Gourmet Breakfast & Elaborate Dinner Included). TRAGUIN Curated Touch: Pre-arranged fast-track entry permits to the restricted Capitol Complex, curated tables at city-favorite culinary stops, and customized scheduling.'
        ),
        seo_title='CH-010 | Premium Chandigarh Urban Architecture Break | TRAGUIN',
        seo_description='Premium 02 Nights / 03 Days Chandigarh architecture package (CH-010 / TG-CH-010-PREM): Sukhna Lake solar boat cruise, Rock Garden, Rose Garden, UNESCO Capitol Complex, and 4-tier hotels.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
                    _ih('Sukhna Lake Private Solar Boat Cruise', 1),
                    _ih('Nek Chand Rock Garden', 2),
                    _ih('Zakir Hussain Rose Garden', 3),
                    _ih('UNESCO Capitol Complex Architectural Walk', 4),
                    _ih('Sector 17 Piazza Shopping', 5)
        ],
        days=[
        _day(
            1,
            'Arrival in Chandigarh & Sukhna Lake Sunset Experience',
            (
                'Arrive in the beautifully planned grid city of Chandigarh via airport or railway station, where your dedicated private luxury vehicle and executive chauffeur await your presence. Benefit from a seamless transfer to your handpicked premium hotel. After checking in and enjoying a relaxing welcome refreshment, get ready for an elegant late afternoon excursion. We take you directly to Sukhna Lake, a magnificent, pristine water body located at the foothills of the Shivalik range. Enjoy an exclusive, private solar boat ride across the calm waters as the golden sun dips below the horizon. Conclude your evening with a pleasant walk along the tree-lined promenade before heading back to the hotel for a beautifully curated welcome dinner.'
            ),
            [
                'Sightseeing Included: Sukhna Lake Promenade Access, Private Boat Cruise',
                'Evening Experience: Golden Hour photography & premium lakeside tea service',
                'Overnight Stay: Chandigarh (Premium Luxury Hotel)',
                'Meals Included: Welcome Fine Dining Dinner'
            ],
        ),
        _day(
            2,
            'The Legendary Rock Garden, Rose Garden & Capitol Complex',
            (
                "Start your morning with a lavish buffet breakfast. Today, you will explore the world-renowned masterpiece of raw art—the Nek Chand Rock Garden. Be captivated by the emotional storytelling behind this surreal kingdom, sculpted entirely out of discarded urban and industrial materials. Following this immersive experience, a short, smooth drive brings you to the Zakir Hussain Rose Garden, Asia's largest botanical garden dedicated entirely to roses. In the afternoon, explore the majestic UNESCO World Heritage-listed Capitol Complex, featuring the iconic Open Hand Monument, Secretariat, and High Court."
            ),
            [
                'Sightseeing Included: Nek Chand Rock Garden, Zakir Hussain Rose Garden, Capitol Complex Architectural Walk',
                'Optional Activities: Exploring sector-specific luxury European cafes',
                'Overnight Stay: Chandigarh',
                'Meals Included: Breakfast & Dinner'
            ],
        ),
        _day(
            3,
            'Boutique Cafe Culture & Fluid Farewell Transits',
            (
                "Enjoy your final gourmet breakfast at the hotel, checking out by mid-morning. Your luxury vehicle will guide you on an exclusive shopping safari through Sector 17's historic piazza or Elante Mall's high-end flagship stores. Afterward, your chauffeur ensures a seamless transfer to Chandigarh Airport or Railway Station for your departure."
            ),
            [
                'Sightseeing Included: Leisure Drive through Open-Space Boulevards & Sector 17 Piazza',
                'Food Suggestion: Try artisanal bakeries or premium local Punjabi culinary spots',
                'Overnight Stay: Tour Concludes',
                'Meals Included: Lavish Breakfast'
            ],
        )
        ],
        hotels=[
                    _hotel('Hyatt Regency Chandigarh or similar', 'Chandigarh', '02 Nights', 'Deluxe', 'King Bed Club View', 'Breakfast & Dinner', 4, 1),
                    _hotel('Taj Chandigarh', 'Chandigarh', '02 Nights', 'Premium', 'Luxury Superior Room', 'Breakfast & Dinner', 5, 2),
                    _hotel('The Lalit Chandigarh', 'Chandigarh', '02 Nights', 'Luxury', 'Executive Suite Panorama', 'Breakfast & Dinner', 5, 3),
                    _hotel('The Oberoi Sukhvilas Spa Resort', 'New Chandigarh', '02 Nights', 'Ultra Luxury', 'Premier Mud Villa / Luxury Tent', 'All Inclusive Premium Curated', 5, 4),
        ],
        inclusions=[
                    _inc_included('02 Nights luxury stay in premium, handpicked hotels', 1),
                    _inc_included('Daily gourmet breakfast spreads and custom fine-dining dinners', 2),
                    _inc_included('Dedicated premium air-conditioned luxury sedan for all transits', 3),
                    _inc_included('Pre-registered VIP entry entry permits for the UNESCO Capitol Complex', 4),
                    _inc_included('Complimentarty Private Solar Boat experience tickets at Sukhna Lake', 5),
                    _inc_included('Chauffeur allowances, parking fees, road taxes, and toll clearances', 6),
                    _inc_included('Specialized 24/7 TRAGUIN on-ground destination assistance', 7),
                    _inc_excluded('Inbound/Outbound flights or train travel to Chandigarh', 8),
                    _inc_excluded('Personal laundry, bar tabs, premium spirits, and telephone bills', 9),
                    _inc_excluded('Guide services unless explicitly requested in advance', 10),
                    _inc_excluded('Tips, gratuities, and optional camera permits', 11),
                    _inc_excluded('Any travel insurance protection policies', 12),
        ],
    )
    return package, itinerary



def build_ch_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'CH-011'
    tour_code = 'TG-CH-011-OBEROI'
    title = 'The Oberoi Sukhvilas Luxury Wellness Retreat • Chandigarh'
    duration = '02 Nights / 03 Days'
    slug = 'ch-011-oberoi-sukhvilas-luxury-wellness-retreat-chandigarh'
    itin_slug = 'ch-011-oberoi-sukhvilas-wellness-itinerary'
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
                    _ph('Serial code CH-011 | TRAGUIN tour code TG-CH-011-OBEROI', 1),
                    _ph('State / Country: Chandigarh / India | Category: Luxury Wellness', 2),
                    _ph('Destinations: Sukhvilas • Rock Garden • Sukhna Lake', 3),
                    _ph('Ideal for: Couples, Executives & Elites', 4),
                    _ph('Best season: October to March', 5),
                    _ph('Complimentary signature 60-minute Oberoi Spa massage per guest', 6),
                    _ph('TRAGUIN Signature Experience: Private sunrise yoga and forest mindfulness breathing sessions', 7),
                    _ph('Shopping: Sector 17 Plaza, Phulkari Handlooms, organic elixirs at resort boutique', 8)
        ],
        moods=['Luxury', 'Romantic', 'Wellness'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Luxury Wellness Retreat)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='The Oberoi Sukhvilas Luxury Wellness Retreat • Chandigarh',
        overview=(
            'Escape into a sanctuary of absolute tranquility, architectural splendor, and bespoke rejuvenation. Perfectly curated by the master travel consultants at TRAGUIN, this signature itinerary invites you to indulge in an ultra-luxury weekend at The Oberoi Sukhvilas Luxury Wellness Resort, nestled against the peaceful backdrop of the Siswan Forest Range near Chandigarh.\n\nTravel Format: Private Ultra-Luxury FIT Escape with Dedicated On-Ground Concierge. Vehicle: Premium Luxury Sedan (Mercedes-Benz / BMW Group) with Professional Chauffeur. Meal Plan: Continental Breakfast & Specially Curated Wellness Dinners at Ananta Mahal. TRAGUIN Curated Touch: Priority check-in, personalized dynamic spa sequencing, and exclusive reservations at the finest city hotspots.'
        ),
        seo_title='CH-011 | Oberoi Sukhvilas Luxury Wellness Retreat | TRAGUIN',
        seo_description='Luxury 02 Nights / 03 Days wellness package (CH-011 / TG-CH-011-OBEROI): Oberoi Sukhvilas stay, Rock Garden, Rose Garden, Sukhna Lake private cruise, and signature spa therapy.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
                    _ih('The Oberoi Sukhvilas Luxury Wellness Resort Stay', 1),
                    _ih('Rock Garden & Rose Garden Chandigarh Sightseeing', 2),
                    _ih('Sukhna Lake Private Sunset Cruise', 3),
                    _ih('60-Minute Signature Oberoi Massage Therapy', 4),
                    _ih('Resort Forest Orientation Trail Walk', 5)
        ],
        days=[
        _day(
            1,
            'Arrival in Chandigarh & Retreat to The Oberoi Sukhvilas',
            (
                'Your luxury journey begins with a smooth arrival experience at Chandigarh Airport or Railway Station, where a uniform-clad TRAGUIN representative and a private luxury sedan await you. Leave the city buzz behind as you take a scenic route towards the Siswan Forest Range. Arrive at the magnificent gates of The Oberoi Sukhvilas Luxury Wellness Resort, where a grand traditional welcome sets the tone for your stay. Check into your beautifully appointed Premier Room or Luxury Tent featuring private garden views. In the evening, meet with an in-house wellness physician for a curated Ayurvedic body profiling, followed by an exquisite multi-cuisine wellness dinner at Ananta Mahal.'
            ),
            [
                'SIGHTSEEING INCLUDED: Resort Forest Orientation Trail Walk',
                'EVENING EXPERIENCE: Personalized Spa Consultation & Gourmet Dinner',
                'OVERNIGHT STAY: The Oberoi Sukhvilas Luxury Wellness Resort',
                'MEALS INCLUDED: Welcome Wellness Dinner'
            ],
        ),
        _day(
            2,
            'Architectural Marvels & Serene Sunset Cruises',
            (
                'Awaken to the soothing sounds of nature and start your day with an energizing yoga session under the forest canopy. After a healthy breakfast, your chauffeur takes you to discover the top tourist places in Chandigarh. Begin your Chandigarh Sightseeing tour at the legendary Nek Chand Rock Garden. Next, take a gentle walk across the Zakir Hussain Rose Garden. In the late afternoon, enjoy an exclusive private boating cruise on the calm waters of Sukhna Lake during a breathtaking sunset view. Return to the resort for an ultra-premium holistic therapy at the Oberoi Spa.'
            ),
            [
                'SIGHTSEEING INCLUDED: Rock Garden, Rose Garden, Sukhna Lake Private Cruise',
                'EXCLUSIVE EXPERIENCE: 60-Minute Signature Oberoi Massage Therapy',
                'OVERNIGHT STAY: The Oberoi Sukhvilas Luxury Wellness Resort',
                'MEALS INCLUDED: Luxury Breakfast & Dinner'
            ],
        ),
        _day(
            3,
            'Inner Peace & Departure with Unforgettable Memories',
            (
                'Your final day begins with a gentle morning meditation session and a lavish breakfast spread at the resort. Enjoy your remaining hours at leisure—indulge in the hydrotherapy facilities, capture photographs across the stunning water bodies, or buy premium wellness oils from the boutique. Your dedicated chauffeur will handle all luggage transfers smoothly. Bid farewell to this serene paradise as you are transferred back to Chandigarh Airport or Station for your onward journey.'
            ),
            [
                'SIGHTSEEING INCLUDED: Capitol Complex Architectural Drive (Optional)',
                'ASSISTANCE: Airport/Station Chauffeur drop-off & luggage assistance',
                'OVERNIGHT STAY: Tour Concludes',
                'MEALS INCLUDED: Fine Dining Breakfast'
            ],
        )
        ],
        hotels=[
                    _hotel('The Oberoi Sukhvilas (Forest Wing)', 'Siswan Forest Range', '02 Nights', 'Deluxe', 'Premier Room with Garden Views', 'Breakfast & Dinner', 5, 1),
                    _hotel('The Oberoi Sukhvilas (Luxury Wing)', 'Siswan Forest Range', '02 Nights', 'Premium', 'Royal Forest Tent with Private Deck', 'Breakfast & Dinner', 5, 2),
                    _hotel('The Oberoi Sukhvilas (Elite Collection)', 'Siswan Forest Range', '02 Nights', 'Luxury', 'Luxury Villa with Private Temperature-Controlled Pool', 'Breakfast & Dinner', 5, 3),
                    _hotel('The Oberoi Sukhvilas (Signature Suite)', 'Siswan Forest Range', '02 Nights', 'Ultra Luxury', 'Kohinoor Presidential Villa', 'All-Inclusive Royal Wellness Plan', 5, 4),
        ],
        inclusions=[
                    _inc_included('02 Nights premium stay at The Oberoi Sukhvilas Luxury Wellness Resort', 1),
                    _inc_included('Daily gourmet breakfast and specially curated wellness dinners at Ananta Mahal', 2),
                    _inc_included('Chauffeur-driven premium luxury sedan for all airport transfers and city tours', 3),
                    _inc_included('Complimentary expert wellness doctor consultation and custom spa profiling', 4),
                    _inc_included('01 Complimentary signature 60-minute spa massage per guest at Oberoi Spa', 5),
                    _inc_included('Private motorboat cruise ride at Sukhna Lake with priority entry', 6),
                    _inc_included('Dedicated 24/7 TRAGUIN on-ground executive assistance', 7),
                    _inc_included('High-speed Wi-Fi access, luxury wellness welcome amenities, and all resort taxes', 8),
                    _inc_excluded('Commercial or private flight tickets / train tickets to Chandigarh', 9),
                    _inc_excluded('Any additional personal spa treatments or specialized medical therapies', 10),
                    _inc_excluded('Custom laundry, telephone bills, and mini-bar consumption charges', 11),
                    _inc_excluded('Entrance fees for optional monument photography clips', 12),
                    _inc_excluded('Gratuities and tips for resort staff and accompanying drivers', 13),
        ],
    )
    return package, itinerary



def build_ch_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'CH-012'
    tour_code = 'TG-CH-012-MICE'
    title = 'Chandigarh Executive Corporate MICE Tour'
    duration = '02 Nights / 03 Days'
    slug = 'ch-012-chandigarh-executive-corporate-mice-tour'
    itin_slug = 'ch-012-corporate-mice-itinerary'
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
                    _ph('Serial code CH-012 | TRAGUIN tour code TG-CH-012-MICE', 1),
                    _ph('State / Country: Chandigarh / India | Category: Corporate MICE', 2),
                    _ph('Destinations: Chandigarh Corporate Hub', 3),
                    _ph('Ideal for: Executive Conferences & Retreats', 4),
                    _ph('Best season: Year-Round (Oct to Mar preferred)', 5),
                    _ph('Full-day ballroom rental with specialized high-tech AV', 6),
                    _ph('TRAGUIN Signature Experience: Private closed-door evening cruise at Sukhna Lake', 7),
                    _ph('Shopping: Sector 17 Shopping Plaza, Elante Luxury Mall, Phulkari apparel', 8)
        ],
        moods=['Corporate', 'Luxury', 'Family'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Corporate MICE Program)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Premium Conference • Elite Network Sessions • Curated Team Building',
        overview=(
            "Welcome to Chandigarh, India's most brilliantly planned urban marvel and an elite destination for corporate leadership programs. This high-impact corporate itinerary, engineered by the specialist team at TRAGUIN, perfectly merges high-tech corporate conference features with luxurious leisure breaks.\n\nTravel Format: Corporate MICE / Executive Team Retreat. Vehicle Fleet: Luxury Executive Sedans and Premium Coaches for delegates. Meal Plan: All-Inclusive Corporate Plan (Breakfast, Mid-Session High Teas, Business Luncheons, Grand Gala Dinner). TRAGUIN Curated Touch: Pre-registered fast-track hotel check-ins, custom branded delegate kits, dedicated on-ground event managers."
        ),
        seo_title='CH-012 | Chandigarh Executive Corporate MICE Tour | TRAGUIN',
        seo_description='Corporate 02 Nights / 03 Days MICE package (CH-012 / TG-CH-012-MICE): conference ballroom, Sukhna Lake networking cruise, Rock Garden sightseeing, and executive hotel options.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
                    _ih('Sukhna Lake Corporate Networking Cruise', 1),
                    _ih('Grand Executive Gala Night', 2),
                    _ih('Rock Garden by Nek Chand Team Visit', 3),
                    _ih('Zakir Hussain Rose Garden Stroll', 4),
                    _ih('Full-Day Strategy Conference Sessions', 5)
        ],
        days=[
        _day(
            1,
            'Delegate Arrival, Check-In & Evening Networking Cruise',
            (
                'Land at Chandigarh International Airport where our dedicated corporate greeting staff welcomes your team with custom delegate badge kits. Board your luxury business coach or private sedan for a smooth transfer to your handpicked hotel. Enjoy an expedited, private group check-in at a dedicated hospitality desk managed entirely by TRAGUIN experts. At 17:00 hrs, gather for a relaxing evening experience at the scenic Sukhna Lake with an exclusive private pontoon boat cruise for your leadership team.'
            ),
            [
                'Sightseeing Included: Sukhna Lake Corporate Promenade',
                'Evening Experience: Sunset Networking Cruise & Welcome Cocktails',
                'Overnight Stay: Chandigarh (Ultra Luxury Corporate Suite)',
                'Meals Included: Premium Welcome Dinner'
            ],
        ),
        _day(
            2,
            'Power Conferences, Keynotes & Executive Gala Night',
            (
                "Begin your morning with an energized breakfast buffet at the hotel's premium dining hall. At 09:00 hrs, the main business session commences in the grand ballroom with seamless audio-visual integration. Take a midday break for a gourmet corporate lunch. The afternoon session continues with targeted workshops or team-building exercises. At 20:00 hrs, step into the outdoor lawns for the Grand Executive Gala Night."
            ),
            [
                'Sightseeing Included: None (Full-day Strategy Sessions)',
                'Evening Experience: Executive Awards Night & Live Gala Dinner',
                'Overnight Stay: Chandigarh',
                'Meals Included: Breakfast, Mid-session High Teas, Business Lunch, Gala Dinner'
            ],
        ),
        _day(
            3,
            'Iconic Sightseeing, Architectural Tours & Departure',
            (
                'Savor a relaxed breakfast before packing up and checking out of your premium stays. Today blends local lifestyle exploration with corporate inspiration as we embark on a premium Chandigarh sightseeing excursion to the Rock Garden and Rose Garden. Following a corporate luncheon at a high-end city club, enjoy a brief shopping stop at Sector 17 Plaza or Elante Mall before coordinated airport transfers.'
            ),
            [
                'Sightseeing Included: Rock Garden by Nek Chand, Zakir Hussain Rose Garden',
                'Shopping Spots: Sector 17 Corporate Boulevard / Elante Elite Hub',
                'Overnight Stay: Tour Concludes',
                'Meals Included: Breakfast & Premium Farewell Luncheon'
            ],
        )
        ],
        hotels=[
                    _hotel('Hyatt Regency Chandigarh', 'Chandigarh', '02 Nights', 'Deluxe', 'Regency King Room + Ballroom Access', 'Corporate Plan', 5, 1),
                    _hotel('Taj Chandigarh', 'Chandigarh', '02 Nights', 'Premium', 'Luxury Superior Room + Boardroom Space', 'Corporate Plan', 5, 2),
                    _hotel('The Lalit Chandigarh', 'Chandigarh', '02 Nights', 'Luxury', 'Executive Suite + Integrated AV Banquet', 'All-Inclusive Executive', 5, 3),
                    _hotel('The Oberoi Sukhvilas Spa Resort', 'New Chandigarh', '02 Nights', 'Ultra Luxury', 'Premium Luxury Villa + Bespoke Corporate Pavilions', 'Ultra Luxury Corporate Elite', 5, 4),
        ],
        inclusions=[
                    _inc_included('02 Nights luxury stay at your choice of handpicked premier business hotels', 1),
                    _inc_included('All-inclusive corporate dining: Breakfast, Lunches, Gala Dinners, and High Teas', 2),
                    _inc_included('Full-day ballroom rental with specialized high-tech AV, dual projectors, microphones, and staging', 3),
                    _inc_included('Dedicated corporate airport pick-up and drop-off using executive vehicles', 4),
                    _inc_included('Private sunset networking cruise on Sukhna Lake with curated appetizers', 5),
                    _inc_included('Premium Chandigarh sightseeing entries with skip-the-line group access', 6),
                    _inc_included('Customized delegate branding kits (Notepads, Executive Pens, Branded Eco-bottles)', 7),
                    _inc_included('24/7 on-site event coordination and logistical support from TRAGUIN experts', 8),
                    _inc_excluded('Domestic or International flights to and from Chandigarh Airport', 9),
                    _inc_excluded('Professional emcee, external celebrity keynotes, or specific live band charges', 10),
                    _inc_excluded('Personal hotel charges (Mini-bar access, premium spa therapies, laundry services)', 11),
                    _inc_excluded('Individual travel insurance plans or medical incident coverage', 12),
                    _inc_excluded('GST and government taxes beyond standard included hospitality quotas', 13),
        ],
    )
    return package, itinerary



def build_ch_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'CH-013'
    tour_code = 'TG-CH-013-HON'
    title = 'Romantic City Escape & Luxury Spa'
    duration = '02 Nights / 03 Days'
    slug = 'ch-013-romantic-city-escape-luxury-spa'
    itin_slug = 'ch-013-romantic-city-escape-itinerary'
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
                    _ph('Serial code CH-013 | TRAGUIN tour code TG-CH-013-HON', 1),
                    _ph('State / Country: Chandigarh / India | Category: Honeymoon / Couple Escape', 2),
                    _ph('Destinations: Chandigarh Romantic Luxury Tour', 3),
                    _ph('Ideal for: Couples, Honeymooners & Seekers of Luxury', 4),
                    _ph('Best season: September to April', 5),
                    _ph('Complimentary private Sunset Shikara Boat Cruise on Sukhna Lake', 6),
                    _ph('TRAGUIN Signature Experience: Private sunset lake cruise combined with premium couples wellness rituals', 7),
                    _ph('Shopping: Phulkari embroidery, Sector 17 & Elante Retail, gourmet sweet delicacies', 8)
        ],
        moods=['Romantic', 'Luxury', 'Wellness'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Honeymoon Escape)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Sukhna Lake • Rock Garden • Zakir Hussain Rose Garden • Elante',
        overview=(
            "Welcome to India's most beautifully planned urban paradise. This highly tailored Chandigarh Honeymoon Package, meticulously designed by the romantic travel experts at TRAGUIN, promises a seamless escape filled with beautiful moments, premium stays, and deeply relaxing experiences.\n\nTravel Format: Private Honeymoon FIT Itinerary with On-Call Concierge Management. Vehicle: Premium luxury sedan. Meal Plan: Modified American Plan (Breakfast & Romantic Curated Dinners Included). TRAGUIN Curated Touch: Welcome chocolate platter, customized room decor setup upon arrival, reserved premium seats for evening experiences."
        ),
        seo_title='CH-013 | Romantic City Escape & Luxury Spa | TRAGUIN',
        seo_description='Honeymoon 02 Nights / 03 Days package (CH-013 / TG-CH-013-HON): private sunset shikara cruise, Rock Garden, Rose Garden, 90-minute couples spa, and luxury hotel options.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
                    _ih('Private Sunset Shikara Cruise on Sukhna Lake', 1),
                    _ih('Nek Chand Rock Garden Artistic Tour', 2),
                    _ih('Zakir Hussain Rose Garden Stroll', 3),
                    _ih('90-Minute Couples Luxury Spa Ritual', 4),
                    _ih('Candlelight Dinner at Award-Winning Rooftop Restaurant', 5)
        ],
        days=[
        _day(
            1,
            'Arrival in Chandigarh & Private Sunset Shikara Cruise',
            (
                'Your magical journey begins with a smooth arrival at Chandigarh Airport or Chandigarh Railway Station. A polished TRAGUIN hospitality representative along with a professional uniform-clad chauffeur will receive you with a beautiful fresh flower bouquet. Check in to your beautifully decorated honeymoon room. In the late afternoon, experience a private, curated sunset cruise on the calm waters of Sukhna Lake. Conclude your day with an intimate candlelight dinner specially reserved for you at an award-winning rooftop restaurant.'
            ),
            [
                'Sightseeing Included: Sukhna Lake Promenade & Waterfront Trail',
                'Evening Experience: Private Sunset Shikara Ride with Refreshments',
                'Overnight Stay: Chandigarh Luxury Hotel / Resort',
                'Meals Included: Specially Arranged Candlelight Dinner'
            ],
        ),
        _day(
            2,
            'The Artistic Rock Garden, Rose Garden & Luxury Couples Spa',
            (
                "Awake to a lavish gourmet floating breakfast inside your luxury suite or resort pool. Mid-morning, step out for a curated day of Chandigarh Sightseeing at Nek Chand's legendary Rock Garden and the Zakir Hussain Rose Garden. The afternoon shifts into an oasis of pure relaxation with an exclusive 90-minute signature couples' aromatherapy massage followed by a steam, sauna, and hot herbal tea session."
            ),
            [
                'Sightseeing Included: Rock Garden, Rose Garden, Sector 17 Plaza Walk',
                'Exclusive Highlight: Premium 90-Minute Couples Luxury Spa Ritual',
                'Overnight Stay: Chandigarh Premium Luxury Stay',
                'Meals Included: Buffet Breakfast & Fine Dining Dinner'
            ],
        ),
        _day(
            3,
            'Premium Cafe Trails, Elante Retail Excursion & Departure',
            (
                'Savor a peaceful breakfast before compiling your bags. Spend the morning checking out the ultra-modern side of the city with a visit to the high-end Elante Mall or the elite designer boutiques of Sector 9. Your private vehicle will then carry you smoothly back to the airport or railway station for your onward flight.'
            ),
            [
                'Sightseeing Included: Elite Sector Shopping Squares & Cafes',
                'Optional Activities: Premium Lunch at a boutique microbrewery/bistro',
                'Overnight Stay: Tour Concludes',
                'Meals Included: Gourmet Buffet Breakfast'
            ],
        )
        ],
        hotels=[
                    _hotel('Hyatt Regency Chandigarh or similar', 'Chandigarh', '02 Nights', 'Deluxe', 'King Room with Club Access', 'Breakfast & Dinner', 5, 1),
                    _hotel('Taj Chandigarh', 'Chandigarh', '02 Nights', 'Premium', 'Luxury Grand Room', 'Breakfast & Dinner', 5, 2),
                    _hotel('The Lalit Chandigarh', 'Chandigarh', '02 Nights', 'Luxury', 'Executive Luxury Suite', 'Breakfast & Curated Dinner', 5, 3),
                    _hotel('The Oberoi Sukhvilas Spa Resort', 'New Chandigarh', '02 Nights', 'Ultra Luxury', 'Premier Room / Luxury Tent with Private Pool', 'All-Inclusive Royal Plan', 5, 4),
        ],
        inclusions=[
                    _inc_included('02 Nights luxury accommodation in handpicked, pre-vetted top luxury hotels', 1),
                    _inc_included('Daily gourmet buffet breakfasts at the hotel dining hall', 2),
                    _inc_included('Dedicated private premium sedan for all transfers & sightseeing as per itinerary', 3),
                    _inc_included('Complimentary private Sunset Shikara Boat Cruise on Sukhna Lake', 4),
                    _inc_included('Premium 90-minute Couples Luxury Spa treatment included once during stay', 5),
                    _inc_included('Special Honeymoon Amenities: Room decoration, fresh cake, and chocolate platter', 6),
                    _inc_included('24/7 dedicated on-ground TRAGUIN customer support & assistance', 7),
                    _inc_included('All applicable luxury hotel taxes, driver allowances, parking, and toll fees', 8),
                    _inc_excluded('Airfare, train tickets, or interstate transit expenses', 9),
                    _inc_excluded('Entrance tickets at monuments and camera fees', 10),
                    _inc_excluded('Lunch meals, laundry, alcoholic beverages, and minibar expenses', 11),
                    _inc_excluded('Optional activities or personal shopping items', 12),
                    _inc_excluded('Travel or medical insurance policies', 13),
        ],
    )
    return package, itinerary



def build_ch_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'CH-014'
    tour_code = 'TG-CH-014-PREM'
    title = 'Premium Chandigarh with Timber Trail Escape'
    duration = '03 Nights / 04 Days'
    slug = 'ch-014-premium-chandigarh-with-timber-trail-escape'
    itin_slug = 'ch-014-chandigarh-timber-trail-itinerary'
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
                    _ph('Serial code CH-014 | TRAGUIN tour code TG-CH-014-PREM', 1),
                    _ph('State / Country: Chandigarh & HP / India | Category: Leisure & Escapes', 2),
                    _ph('Destinations: Chandigarh • Parwanoo (Timber Trail)', 3),
                    _ph('Ideal for: Couples, Families & Weekend Seekers', 4),
                    _ph('Best season: Round the year (October to March ideal)', 5),
                    _ph('Round-trip cable car tickets at Timber Trail Parwanoo', 6),
                    _ph('TRAGUIN Signature Experience: Private sunset boat cruise with prioritized boarding at Sukhna Lake', 7),
                    _ph('Shopping: Elante Mall, Phulkari embroidery, Sector 26 artisanal cafes', 8)
        ],
        moods=['Romantic', 'Luxury', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Timber Trail Escape)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='The Urban Architectural Marvel Meets Breathtaking Shivalik Hills',
        overview=(
            "Welcome to a flawlessly designed urban getaway curated by the destination specialists at TRAGUIN. This exclusive 3 Nights / 4 Days luxury package beautifully unifies the symmetrical, green grandeur of India's most organized city—Chandigarh—with the majestic, cliff-hanging serenity of Timber Trail, Parwanoo.\n\nTravel Format: Private Tailor-made Luxury Getaway (FIT). Vehicle: Chauffeur-driven Premium Segment Sedan / SUV (Innova Crysta). Meal Plan: Modified American Plan (Daily Luxury Buffet Breakfast & Dinner Included). TRAGUIN Curated Touch: Pre-booked private cable car transfers at Timber Trail, VIP seating arrangements during lake excursions, and handpicked premium hotels."
        ),
        seo_title='CH-014 | Premium Chandigarh with Timber Trail Escape | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days package (CH-014 / TG-CH-014-PREM): Sukhna Lake boat ride, Rock Garden, Rose Garden, Pinjore Gardens, Timber Trail cable car, and split-stay hotel options.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
                    _ih('Sukhna Lake Private Boat Ride & Sunset Photography', 1),
                    _ih('Rock Garden, Rose Garden & Pinjore Mughal Gardens', 2),
                    _ih('Timber Trail Cable Car Transfer', 3),
                    _ih('Shivalik Mountain Panoramas at Parwanoo', 4),
                    _ih('Morning Resort Mountain Trails', 5)
        ],
        days=[
        _day(
            1,
            'Arrival in Chandigarh & Sunset Lake Cruise',
            (
                'Arrive at Chandigarh Airport or Railway Station, where you will be greeted with a warm welcome by your dedicated TRAGUIN luxury representative. Step into your premium private vehicle and transfer to your handpicked luxury hotel in the heart of the city. We visit the iconic Sukhna Lake and enjoy a private boat ride on its calm waters as the golden sun dips below the horizon.'
            ),
            [
                'Sightseeing Included: Sukhna Lake & Promenade walk',
                'Evening Experience: Private Boat Ride & sunset photography',
                'Overnight Stay: Chandigarh (Premium Luxury Hotel)',
                'Meals Included: Buffet Dinner'
            ],
        ),
        _day(
            2,
            'Legendary Rock Garden, Rose Garden & Pinjore Gardens',
            (
                'Indulge in a fine breakfast before plunging into the artistic brilliance of Chandigarh Sightseeing at the world-famous Rock Garden and Zakir Hussain Rose Garden. In the afternoon, take a comfortable short drive to the historical Pinjore Gardens (Yadavindra Gardens), built in the Mughal style with cascading terraces and grand fountains.'
            ),
            [
                'Sightseeing Included: Rock Garden, Rose Garden, Pinjore Mughal Gardens',
                'Optional Activities: Shopping at Sector 17 Premium High-Street Market',
                'Overnight Stay: Chandigarh',
                'Meals Included: Breakfast & Dinner'
            ],
        ),
        _day(
            3,
            'Ascent to Timber Trail Parwanoo via Cable Car',
            (
                'Following a sumptuous breakfast, check out from your hotel as we embark on a Luxury Chandigarh Holiday extension towards Parwanoo, Himachal Pradesh. Arrive at the base station of Timber Trail, where a private cable car awaits you. Reach the exclusive mountain resort perched on top of the hill and check into your premium room offering magnificent views of the valley.'
            ),
            [
                'Sightseeing Included: Shivalik Mountain Panoramas, Timber Trail Cable Car Transfer',
                'Evening Experience: Tea/Coffee over a spectacular valley sunset view',
                'Overnight Stay: Parwanoo (Timber Trail Heights Resort)',
                'Meals Included: Breakfast & Grand Valley-View Dinner'
            ],
        ),
        _day(
            4,
            'Memories at the Peak & Farewell to the Hills',
            (
                'Wake up to a crisp morning over the mountains and enjoy a delicious breakfast suspended in nature. Later, glide back down the valley via the cable car where your luxury vehicle is stationed. Enjoy a smooth drive back to Chandigarh as your chauffeur transfers you back to Chandigarh Airport or Railway Station.'
            ),
            [
                'Sightseeing Included: Morning resort mountain trails',
                'Assistance: Departure luggage assistance by chauffeur',
                'Overnight Stay: Tour Concludes',
                'Meals Included: Breakfast'
            ],
        )
        ],
        hotels=[
                    _hotel('Lemon Tree Hotel / Classic City Stay | Timber Trail Resort (Base Wing)', 'Chandigarh / Parwanoo', '03 Nights', 'Deluxe', 'Standard Room / Base Wing', 'Breakfast & Dinner', 4, 1),
                    _hotel('Hyatt Regency Chandigarh / Radisson | Moksha Himalaya Spa Resort / Timber Trail Heights', 'Chandigarh / Parwanoo', '03 Nights', 'Premium', 'Premium Room / Heights Wing', 'Breakfast & Dinner', 5, 2),
                    _hotel('The Lalit Chandigarh / JW Marriott | Moksha Luxury Suite Wing', 'Chandigarh / Parwanoo', '03 Nights', 'Luxury', 'Luxury Suite Wing', 'Breakfast & Dinner', 5, 3),
                    _hotel('The Oberoi Sukhvilas Spa Resort | Moksha Royal Presidential Villa', 'Chandigarh / Parwanoo', '03 Nights', 'Ultra Luxury', 'Royal Presidential Villa', 'All Inclusive Premium', 5, 4),
        ],
        inclusions=[
                    _inc_included('03 Nights luxury stay across handpicked deluxe/premium hotels', 1),
                    _inc_included('Daily premium multi-cuisine buffet breakfast and curated dinners', 2),
                    _inc_included('Air-conditioned private Innova Crysta throughout the complete itinerary', 3),
                    _inc_included('Professional, courteous, English/Hindi-speaking private driver', 4),
                    _inc_included('Round-trip cable car tickets at Timber Trail Parwanoo', 5),
                    _inc_included('Pre-arranged entry fees to Rock Garden, Rose Garden, and Pinjore Gardens', 6),
                    _inc_included('Complimentary premium boat ride voucher at Sukhna Lake', 7),
                    _inc_included('Dedicated 24/7 TRAGUIN helpline & operational guest support', 8),
                    _inc_included('All applicable fuel charges, parking fees, tolls, and driver allowances', 9),
                    _inc_excluded('Airfare / Inter-state train tickets to Chandigarh', 10),
                    _inc_excluded('Personal expenses such as room service, laundry, phone calls, or tips', 11),
                    _inc_excluded('Any lunches or snacks unless specifically outlined', 12),
                    _inc_excluded('Professional camera or video shooting licenses at monuments', 13),
                    _inc_excluded('Comprehensive personal or medical travel insurance', 14),
        ],
    )
    return package, itinerary



def build_ch_015(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'CH-015'
    tour_code = 'TG-CH-015-ARCH'
    title = 'Premium Chandigarh Architecture Tour Package'
    duration = '02 Nights / 03 Days'
    slug = 'ch-015-premium-chandigarh-architecture-tour-package'
    itin_slug = 'ch-015-le-corbusier-architecture-itinerary'
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
                    _ph('Serial code CH-015 | TRAGUIN tour code TG-CH-015-ARCH', 1),
                    _ph('State / Country: Chandigarh / India | Category: Culture & Architecture', 2),
                    _ph('Destinations: Chandigarh Architecture Trail', 3),
                    _ph('Ideal for: Design Enthusiasts, Scholars, Couples', 4),
                    _ph('Best season: October to March', 5),
                    _ph('Architectural expert tour guide for all monument walks', 6),
                    _ph('TRAGUIN Signature Experience: Private architecture walkthroughs and exclusive Modulor reference material', 7),
                    _ph('Shopping: Sector 17 Shopping Piazza, Phulkari, Open Hand miniature models', 8)
        ],
        moods=['Cultural', 'Luxury', 'Family'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Architecture Trail)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Le Corbusier Heritage Architecture Trail',
        overview=(
            'Welcome to Chandigarh, the manifestation of modernist architectural genius. This meticulously designed exploration, customized by TRAGUIN travel specialists, is a profound immersion into the Le Corbusier Heritage Architecture Trail.\n\nTravel Format: Private Tailored Architectural FIT Experience. Vehicle: Luxury Sedan / Premium SUV. Meal Plan: Modified American Plan (Gourmet Breakfast & Fine-Dining Dinner). TRAGUIN Curated Touch: Pre-booked VIP permissions for restricted areas of the Secretariat and High Court, private architecture specialist guide.'
        ),
        seo_title='CH-015 | Premium Chandigarh Architecture Tour | TRAGUIN',
        seo_description='Architecture 02 Nights / 03 Days package (CH-015 / TG-CH-015-ARCH): Le Corbusier Centre, UNESCO Capitol Complex, Rock Garden, Government Museum, Rose Garden, and 4-tier hotels.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
                    _ih('Le Corbusier Centre Sector 19', 1),
                    _ih('UNESCO Capitol Complex VIP Walkthrough', 2),
                    _ih('Nek Chand Rock Garden', 3),
                    _ih('Government Museum and Art Gallery Sector 10', 4),
                    _ih('Zakir Hussain Rose Garden', 5)
        ],
        days=[
        _day(
            1,
            'Arrival in the City of Joyful Design & Sunset Cruise',
            (
                'Arrive at Chandigarh International Airport or the railway station, where your private TRAGUIN luxury transport and expert architectural guide await you. After check-in and lunch at leisure, begin your exploration at the Le Corbusier Centre in Sector 19. As the evening sets in, enjoy a peaceful private boat cruise on the tranquil waters of Sukhna Lake.'
            ),
            [
                'Sightseeing Included: Le Corbusier Centre, Sukhna Lake Promenade',
                'Evening Experience: Private Boat Cruise & Lakeside High Tea',
                'Overnight Stay: Chandigarh (Premium Luxury Hotel)',
                'Meals Included: Curated Welcome Dinner'
            ],
        ),
        _day(
            2,
            'The UNESCO Capitol Complex & Brutalist Masterpieces',
            (
                "Dedicate your morning to the crown jewel of the Premium Chandigarh Experience: the UNESCO World Heritage Listed Capitol Complex in Sector 1. Stand before the monumental Open Hand Monument. In the afternoon, shift to Nek Chand's legendary Rock Garden and conclude with a drive through Pierre Jeanneret's residential sectors."
            ),
            [
                'Sightseeing Included: Capitol Complex, Open Hand, Rock Garden',
                'Exclusive Masterclass: Guided Walkthrough on Jeanneret Furniture Design',
                'Overnight Stay: Chandigarh',
                'Meals Included: Breakfast & Fine-Dining Dinner'
            ],
        ),
        _day(
            3,
            'Heritage Museums, Botanical Beauty & Departure',
            (
                'After a morning gourmet breakfast, check out and visit the Government Museum and Art Gallery in Sector 10. Afterward, take a leisurely stroll through the expansive Zakir Hussain Rose Garden. Savor a final boutique culinary lunch at a premium cafe in Sector 7 before your private chauffeur transfers you to the airport.'
            ),
            [
                'Sightseeing Included: Government Museum & Gallery, Rose Garden',
                'Shopping & Souvenirs: Miniature Open Hand models, Local phulkari crafts',
                'Overnight Stay: Tour Concludes',
                'Meals Included: Breakfast & Premium Lunch'
            ],
        )
        ],
        hotels=[
                    _hotel('Hyatt Regency Chandigarh or similar', 'Chandigarh', '02 Nights', 'Deluxe', 'King Room / City View', 'Breakfast & Dinner', 5, 1),
                    _hotel('Taj Chandigarh, Sector 17', 'Chandigarh', '02 Nights', 'Premium', 'Luxury Garden View Room', 'Breakfast & Dinner', 5, 2),
                    _hotel('The Lalit Chandigarh', 'Chandigarh', '02 Nights', 'Luxury', 'Executive Suite', 'Breakfast & Dinner', 5, 3),
                    _hotel('The Oberoi Sukhvilas Spa Resort', 'New Chandigarh', '02 Nights', 'Ultra Luxury', 'Luxury Tent / Private Pool Villa', 'All Inclusive Premium Curated', 5, 4),
        ],
        inclusions=[
                    _inc_included('02 Nights premium luxury stay in handpicked hotels', 1),
                    _inc_included('Daily gourmet buffet breakfast and specialized regional dinners', 2),
                    _inc_included('Private luxury transportation with a dedicated professional chauffeur', 3),
                    _inc_included('Architectural expert tour guide for all monument walks', 4),
                    _inc_included('Pre-arranged VIP permits for the UNESCO Capitol Complex buildings', 5),
                    _inc_included('Private sunset boat cruise entry at Sukhna Lake', 6),
                    _inc_included('All applicable luxury taxes, toll fees, and driver allowances', 7),
                    _inc_included('Specialized 24/7 TRAGUIN customer support and concierge assistance', 8),
                    _inc_excluded('Airfare, train tickets, or interstate transit fares', 9),
                    _inc_excluded('Personal items such as laundry, telephone bills, or tips', 10),
                    _inc_excluded('Customary alcoholic beverages or premium mini-bar snacks', 11),
                    _inc_excluded('Camera/drone operational fees inside specific heritage zones', 12),
                    _inc_excluded('Comprehensive personal medical and travel insurance policies', 13),
        ],
    )
    return package, itinerary



def build_ch_016(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'CH-016'
    tour_code = 'TG-CH-016-LUX'
    title = 'Premium Chandigarh Shopping Extravaganza'
    duration = '02 Nights / 03 Days'
    slug = 'ch-016-premium-chandigarh-shopping-extravaganza'
    itin_slug = 'ch-016-shopping-extravaganza-itinerary'
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
                    _ph('Serial code CH-016 | TRAGUIN tour code TG-CH-016-LUX', 1),
                    _ph('State / Country: Chandigarh / India | Category: Shopping & Leisure Extravaganza', 2),
                    _ph('Destinations: Sector 17 Plaza • Elante Mall • Sukhna Lake', 3),
                    _ph('Ideal for: Shopaholics, Fashionistas & Families', 4),
                    _ph('Best season: Year-Round (October to March Ideal)', 5),
                    _ph('Hands-free retail assistance (chauffeur bag collection service)', 6),
                    _ph('TRAGUIN Signature Experience: Private concierge guide access to exclusive ethnic couture boutiques', 7),
                    _ph('Shopping: Phulkari embroidery, Punjabi Juttis, upscale cafes & microbreweries', 8)
        ],
        moods=['Luxury', 'Family', 'Cultural'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Shopping Extravaganza)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Sector 17 Plaza • Elante Retail Luxury • Sukhna Leisure Trails',
        overview=(
            'Welcome to Chandigarh, the beautifully planned "City Beautiful" where urban sophistication seamlessly merges with vibrant shopping culture and serene landscapes. This exclusive luxury weekend getaway, custom-crafted by TRAGUIN travel specialists, is designed for discerning shopaholics and fashion enthusiasts.\n\nTravel Format: Private Customized Luxury Retail Tour (FIT). Vehicle: Premium, spacious luxury sedan / SUV. Meal Plan: Modified American Plan (Gourmet Breakfast & Curated Dinner Included). TRAGUIN Curated Touch: Hands-free shopping assistance, pre-booked VIP lounge access, and curated culinary tasting menus.'
        ),
        seo_title='CH-016 | Premium Chandigarh Shopping Extravaganza | TRAGUIN',
        seo_description='Luxury 02 Nights / 03 Days shopping package (CH-016 / TG-CH-016-LUX): Sector 17 Plaza, Elante Mall VIP district, Sukhna Lake boardwalk, and 4-tier hotel options.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
                    _ih('Sector 17 Plaza Heritage Retail Walking Tour', 1),
                    _ih('Elante Mall VIP Shopping District', 2),
                    _ih('Sukhna Lake Boardwalk Walkway', 3),
                    _ih('Heritage High-Tea & Local Street Food Tasting', 4),
                    _ih('Optional Rock Garden Visit', 5)
        ],
        days=[
        _day(
            1,
            'Chandigarh Arrival & Sector 17 Plaza Heritage Retail',
            (
                'Arrive in style at Chandigarh Airport or Railway Station, where your dedicated professional chauffeur greets you with a warm welcome. By late afternoon, dive into your Chandigarh Sightseeing journey at the iconic Sector 17 Plaza. Stroll leisurely past fountains and grand tree-lined walkways to discover high-end showrooms, upscale boutiques, and authentic government emporiums.'
            ),
            [
                'Sightseeing Included: Sector 17 Plaza Walking Tour, Phulkari Emporium Trail',
                'Evening Experience: Heritage high-tea & local street food tasting',
                'Overnight Stay: Chandigarh (Premium Luxury Hotel)',
                'Meals Included: Curated Welcome Dinner'
            ],
        ),
        _day(
            2,
            'Elante Mall Ultimate Retail Luxury Extravaganza',
            (
                "Prepare for an unparalleled day of premium retail therapy. After a lavish breakfast, your chauffeur whisks you away to the magnificent Elante Mall. Enjoy a hands-free shopping experience as your chauffeur takes care of your shopping bags directly from the stores. In the evening, step out to experience Chandigarh's upscale nightlife with dinner at an elite microbrewery or lounge."
            ),
            [
                'Sightseeing Included: Elante Mall VIP Shopping District',
                'Optional Activities: Premium salon therapies or luxury cinema viewing',
                'Overnight Stay: Chandigarh',
                'Meals Included: Gourmet Breakfast & Fine-Dining Dinner'
            ],
        ),
        _day(
            3,
            'Leisure at Sukhna Lake & Departure with Memories',
            (
                'Begin your final morning with a peaceful, early breakfast at the hotel. Before heading home, take a gentle, relaxing stroll along the pristine waters of Sukhna Lake. Return briefly to the hotel to pack your newly acquired luxury goods and complete your smooth check-out.'
            ),
            [
                'Sightseeing Included: Sukhna Lake Boardwalk Walkway, Rock Garden (Optional)',
                'Photography Points: Sukhna Lake view frame, Shivalik hill backdrop',
                'Overnight Stay: Tour Concludes',
                'Meals Included: Sumptuous Breakfast'
            ],
        )
        ],
        hotels=[
                    _hotel('Hyatt Regency Chandigarh or similar', 'Chandigarh', '02 Nights', 'Deluxe', 'Standard King Room', 'Breakfast & Dinner', 5, 1),
                    _hotel('The Lalit Chandigarh', 'Chandigarh', '02 Nights', 'Premium', 'Deluxe Valley View Room', 'Breakfast & Dinner', 5, 2),
                    _hotel('Taj Chandigarh', 'Chandigarh', '02 Nights', 'Luxury', 'Luxury Club Room', 'Breakfast & Dinner', 5, 3),
                    _hotel('The Oberoi Sukhvilas Spa Resort', 'New Chandigarh', '02 Nights', 'Ultra Luxury', 'Premier Room / Luxury Tent', 'All Inclusive Curated', 5, 4),
        ],
        inclusions=[
                    _inc_included('02 Nights premium luxury stay at your chosen handpicked hotel', 1),
                    _inc_included('Daily multi-cuisine buffet breakfasts and curated fine-dining dinners', 2),
                    _inc_included('Dedicated private luxury sedan / SUV throughout the entire itinerary', 3),
                    _inc_included('Seamless airport / railway station transfers with professional chauffeur', 4),
                    _inc_included('Hands-free retail assistance (chauffeur bag collection service)', 5),
                    _inc_included('Complimentary welcome amenities and custom welcome drinks on arrival', 6),
                    _inc_included('Complete roadside, parking, state toll, and driver allowances included', 7),
                    _inc_included('24/7 dedicated TRAGUIN on-ground concierge support', 8),
                    _inc_excluded('Airfare or train tickets to/from Chandigarh', 9),
                    _inc_excluded('Personal shopping expenses, clothing purchases, and retail billing', 10),
                    _inc_excluded('Alcoholic beverages, laundry, tips, and room-service orders', 11),
                    _inc_excluded('Any monument entrance tickets or movie passes', 12),
                    _inc_excluded('Mandatory travel and personal medical insurance policies', 13),
                    _inc_excluded('Optional extended tours, spa treatments, or late check-out charges', 14),
        ],
    )
    return package, itinerary



def build_ch_017(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'CH-017'
    tour_code = 'TG-CH-017-PREM'
    title = 'Premium Chandigarh & Morni Hills Retreat'
    duration = '03 Nights / 04 Days'
    slug = 'ch-017-premium-chandigarh-morni-hills-retreat'
    itin_slug = 'ch-017-chandigarh-morni-hills-itinerary'
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
                    _ph('Serial code CH-017 | TRAGUIN tour code TG-CH-017-PREM', 1),
                    _ph('State / Country: Chandigarh & Haryana / India | Category: Offbeat Getaway', 2),
                    _ph('Destinations: Chandigarh • Morni Hills • Tikkar Taal', 3),
                    _ph('Ideal for: Nature Lovers, Couples, Families', 4),
                    _ph('Best season: September to March', 5),
                    _ph('TRAGUIN Exclusive Private Lakeside High-Tea experience at Tikkar Taal', 6),
                    _ph('TRAGUIN Signature Experience: Private luxury high-tea on the banks of Tikkar Taal lake', 7),
                    _ph('Shopping: Sector 22 & 17 Plazas, organic mountain honey, local rock crafts', 8)
        ],
        moods=['Nature', 'Romantic', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Morni Hills Offbeat Getaway)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Sukhna Lake • Morni Hills Nature Trails • Tikkar Taal Escape',
        overview=(
            'Escape into a world where modern structural planning elegantly meets untamed highland wilderness. Curated exclusively by travel design experts at TRAGUIN, this offbeat journey unrolls the serene, manicured architecture of Chandigarh before ascending into the mist-covered valleys of Morni Hills.\n\nTravel Format: Private Customized Premium Tour (FIT). Vehicle: Dedicated Executive Luxury Sedan / SUV. Meal Plan: Modified American Plan (Daily Buffet Breakfast & Curated Dinners). TRAGUIN Curated Touch: Private lakeside high-tea, customized nature walks guided by local naturalists.'
        ),
        seo_title='CH-017 | Premium Chandigarh & Morni Hills Retreat | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days offbeat package (CH-017 / TG-CH-017-PREM): Rock Garden, Sukhna Lake boating, Morni Fort, Tikkar Taal lakes, TRAGUIN lakeside high-tea, and split-stay hotels.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
                    _ih('Rock Garden, Rose Garden & Sukhna Lake Private Boating', 1),
                    _ih('Scenic Shivalik Drive & Heritage Morni Fort Tour', 2),
                    _ih('Tikkar Taal Twin Lakes Exploration', 3),
                    _ih('TRAGUIN Signature Lakeside Premium High-Tea', 4),
                    _ih('Pine Forest Trails at Morni Hills', 5)
        ],
        days=[
        _day(
            1,
            'Arrival in Chandigarh & Sunset Lake Cruise',
            (
                'Welcome to the City of Joy and Architecture. Arrive at Chandigarh Airport or Railway Station where your private TRAGUIN chauffeur greets you warmly. Begin your Chandigarh Sightseeing at the Rock Garden and Rose Garden. As twilight approaches, arrive at the iconic Sukhna Lake for a private boat cruise across its tranquil waters.'
            ),
            [
                'Sightseeing Included: Rock Garden, Rose Garden, Sukhna Lake Private Boating',
                'Evening Experience: Lakeside stroll & premium cafe coffee stop',
                'Overnight Stay: Chandigarh (Premium Handpicked Luxury Hotel)',
                'Meals Included: Luxury Buffet Dinner'
            ],
        ),
        _day(
            2,
            'Scenic Ascent to Morni Hills & Historic Fort Trails',
            (
                'Relish a lavish breakfast at your hotel before check-out. Today we leave the city grid behind, ascending the winding, tree-lined roads toward Morni Hills. Upon arrival, check into your upscale hillside resort. In the afternoon, visit the historic Morni Fort, a restored heritage monument surrounded by old trees.'
            ),
            [
                'Sightseeing Included: Scenic Shivalik Drive, Heritage Morni Fort Tour',
                'Photography Points: Mountain viewpoints, historic fort battlements',
                'Overnight Stay: Morni Hills (Premium Boutique Mountain Resort)',
                'Meals Included: Breakfast & Dinner'
            ],
        ),
        _day(
            3,
            'Essence of Tikkar Taal Lakes & Nature Immersion',
            (
                'Wake up to a crisp mountain breeze and a glorious sunrise over the peaks. Embark on a short drive to Tikkar Taal, a stunning valley featuring two interconnected, beautiful lakes. TRAGUIN has curated an exclusive premium high-tea setup by the lake margin, allowing you to relax comfortably amidst the breathtaking landscapes.'
            ),
            [
                'Sightseeing Included: Tikkar Taal Twin Lakes Exploration, Pine Forest Trails',
                'Exclusive Highlight: TRAGUIN Signature Lakeside Premium High-Tea',
                'Overnight Stay: Morni Hills',
                'Meals Included: Breakfast & Farewell Hillside Dinner'
            ],
        ),
        _day(
            4,
            'Hillside Breakfast & Seamless Departure',
            (
                'Savor your final morning meal overlooking the mist-filled valley of Morni Hills. At your preferred time, your private chauffeur manages a smooth descent back down the hills. If time permits, stop at a premium shopping plaza in Chandigarh before heading to the airport or railway station.'
            ),
            [
                'Sightseeing Included: En-route valley photography, brief city shopping stop',
                'Assistance: Complete baggage handling and terminal drop-off',
                'Overnight Stay: Tour Concludes',
                'Meals Included: Gourmet Breakfast'
            ],
        )
        ],
        hotels=[
                    _hotel('Lemon Tree Hotel / Classic Sector Hotel | Morni Heights Resort / Similar', 'Chandigarh / Morni Hills', '03 Nights', 'Deluxe', 'Standard Room / Heights Wing', 'Breakfast & Dinner', 4, 1),
                    _hotel('Novotel Chandigarh / Radisson City Centre | Royal Hills Resort (Premium Valley View)', 'Chandigarh / Morni Hills', '03 Nights', 'Premium', 'Premium Valley View Room', 'Breakfast & Dinner', 5, 2),
                    _hotel('Hyatt Regency / Marriott Chandigarh | Golden Tulip Resort Morni Hills (Luxury Wing)', 'Chandigarh / Morni Hills', '03 Nights', 'Luxury', 'Luxury Wing Room', 'Breakfast & Dinner', 5, 3),
                    _hotel('The Oberoi Sukhvilas Spa Resort | TRAGUIN Exclusive Handpicked Luxury Villa', 'Chandigarh / Morni Hills', '03 Nights', 'Ultra Luxury', 'Handpicked Luxury Villa', 'All Inclusive Premium Plan', 5, 4),
        ],
        inclusions=[
                    _inc_included('03 Nights accommodation in highly rated premium handpicked hotels', 1),
                    _inc_included('Daily lavish breakfast spreads and custom curated dinner courses', 2),
                    _inc_included('Private luxury transportation with dedicated executive chauffeur', 3),
                    _inc_included('All specialized inner-route permits, highway tolls, and parking tickets', 4),
                    _inc_included('Private boating tokens at Sukhna Lake and dedicated entry to Rock Garden', 5),
                    _inc_included('TRAGUIN Exclusive Private Lakeside High-Tea experience at Tikkar Taal', 6),
                    _inc_included('Premium welcome amenities and consistent on-ground TRAGUIN customer support', 7),
                    _inc_excluded('Airfare or interstate rail travel tickets to Chandigarh', 8),
                    _inc_excluded('Personal laundry, bar tabs, room service orders, and tips', 9),
                    _inc_excluded('Adventure sports tickets at Tikkar Taal (Boating, Zip-lining)', 10),
                    _inc_excluded('Individual travel or medical insurance documents', 11),
                    _inc_excluded('Any entry fees or adjustments outside the detailed itinerary', 12),
        ],
    )
    return package, itinerary



def build_ch_018(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'CH-018'
    tour_code = 'TG-CH-018-PREM'
    title = 'Chandigarh & Kasauli Hills Escape'
    duration = '04 Nights / 05 Days'
    slug = 'ch-018-chandigarh-kasauli-hills-escape'
    itin_slug = 'ch-018-chandigarh-kasauli-hills-itinerary'
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
                    _ph('Serial code CH-018 | TRAGUIN tour code TG-CH-018-PREM', 1),
                    _ph('State / Country: Chandigarh & HP / India | Category: Leisure Escape', 2),
                    _ph('Destinations: Chandigarh • Kasauli Hills', 3),
                    _ph('Ideal for: Families, Couples & Leisurists', 4),
                    _ph('Best season: Round the year (Oct to Jun ideal)', 5),
                    _ph('Private solar boat cruise experience at Sukhna Lake', 6),
                    _ph('TRAGUIN Signature Experience: Private twilight valley-view dining and customized historical walks', 7),
                    _ph('Shopping: Kasauli hand-woven shawls, artisanal fruit wines, Phulkari embroidery', 8)
        ],
        moods=['Nature', 'Romantic', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Kasauli Hills Escape)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='The Urban Masterpiece Meet Sublime Alpine Serenity',
        overview=(
            'Experience a perfectly orchestrated transition from urban architectural luxury to serene alpine grandeur with the Premium Chandigarh Experience curated by TRAGUIN travel specialists. This hand-tailored luxury holiday brings together the structural elegance of Chandigarh and the colonial timeless charm of Kasauli Hills.\n\nTravel Setup: Fully Private Customized Leisure Tour (FIT). Vehicle Allocation: Luxury Premium Sedan / SUV (Innova Crysta). Meal Plan: Modified American Plan (Daily Premium Breakfast & Gourmet Dinner). TRAGUIN Curated Experience Note: VIP access entry at key sites, private candlelit dinner option in Kasauli.'
        ),
        seo_title='CH-018 | Chandigarh & Kasauli Hills Escape | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days package (CH-018 / TG-CH-018-PREM): Sukhna Lake solar boat cruise, Rock Garden, Kasauli Heritage Mall Road, Gilbert Trail, Manki Point, and split-stay hotels.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
                    _ih('Sukhna Lake Private Sunset Boat Cruise', 1),
                    _ih('Nek Chand Rock Garden & Rose Garden', 2),
                    _ih('Kasauli Heritage Mall Road & Christ Church', 3),
                    _ih('Gilbert Trail Nature Walk', 4),
                    _ih('Manki Point Panoramic Lookout', 5)
        ],
        days=[
        _day(
            1,
            'Arrival in Chandigarh & Sukhna Lake Luxury Cruise',
            (
                'Welcome to the City of Joy and structural perfection. Arrive at Chandigarh Airport or Railway Station, where your dedicated TRAGUIN luxury chauffeur awaits. After a smooth check-in, begin your exploration with a visit to the iconic Sukhna Lake. We have curated an exclusive private solar boat cruise for you during sunset.'
            ),
            [
                'Sightseeing Included: Sukhna Lake Promenade & Waterfront Walk',
                'Evening Experience: Private Sunset Boat Cruise Experience',
                'Overnight Stay: Chandigarh (Premium Luxury Hotel)',
                'Meals Included: Gourmet Welcome Dinner'
            ],
        ),
        _day(
            2,
            'Revealing Architectural Wonders & Rose Garden Balm',
            (
                "Savor a lavish morning buffet breakfast before venturing out to see the finest landmarks of Chandigarh Sightseeing at Nek Chand's famous Rock Garden and the Zakir Hussain Rose Garden. In the afternoon, explore the architectural landmarks of the Capitol Complex or enjoy premium high-street shopping at Sector 17 Plaza."
            ),
            [
                'Sightseeing Included: Nek Chand Rock Garden, Rose Garden, Sector 17 Architectural Tour',
                'Photography Points: Recycled sculpture galleries, blooming rose beds',
                'Overnight Stay: Chandigarh',
                'Meals Included: Premium Breakfast & Dinner'
            ],
        ),
        _day(
            3,
            'Journey to Kasauli Hills & Colonial Mall Road Walks',
            (
                'Bid adieu to the plains as we take a smooth, winding, scenic drive upward into the crisp mountain air of Kasauli Hills. Upon arrival in Kasauli, check into your ultra-premium boutique resort. In the afternoon, take a leisurely stroll down the historic colonial Heritage Mall Road and visit the neo-gothic Christ Church.'
            ),
            [
                'Sightseeing Included: Heritage Mall Road, Colonial Christ Church Walk',
                'Evening Experience: Mountain tea-tasting & bonfire at your resort',
                'Overnight Stay: Kasauli Hills (Luxury Valley-View Resort)',
                'Meals Included: Premium Breakfast & Valley-view Dinner'
            ],
        ),
        _day(
            4,
            'Hiking Gilbert Trail & Panoramic Manki Point View',
            (
                'Awake to the birds singing and a magnificent sunrise cutting through the mountain mist. We begin with the famous Gilbert Trail, a short, flat, yet highly scenic nature walk along a cliff edge. Later, we drive up to the historical Manki Point, the highest point in Kasauli. Spend your final evening enjoying an exclusive, curated dinner setup beneath the stars.'
            ),
            [
                'Sightseeing Included: Gilbert Trail Nature Walk, Manki Point Lookout',
                'Exclusive Recommendation: Sip traditional hot Himachali apple cider',
                'Overnight Stay: Kasauli Hills',
                'Meals Included: Premium Breakfast & Candlelit Farewell Dinner'
            ],
        ),
        _day(
            5,
            'Farewell to the Hills & Departure from Chandigarh',
            (
                'Enjoy a leisurely breakfast on the terrace deck of your resort. Your TRAGUIN luxury transport will pick you up for a smooth downhill drive back to Chandigarh, delivering you comfortably to Chandigarh Airport or Railway Station for your return flight home.'
            ),
            [
                'Sightseeing Included: En-route scenic photo stops in Pinjore Valley',
                'Assistance: Complete baggage handling and airport gate drop-off',
                'Overnight Stay: Tour Concludes',
                'Meals Included: Hearty Buffet Breakfast'
            ],
        )
        ],
        hotels=[
                    _hotel('Hotel Hyatt Regency / Lemon Tree | Kasauli Exotica / Fortune Resort', 'Chandigarh / Kasauli', '04 Nights', 'Deluxe', 'Standard Room / Resort Room', 'Breakfast & Dinner', 4, 1),
                    _hotel('Taj Chandigarh (Superior Room) | The Fern Surya Resort / Rosetum', 'Chandigarh / Kasauli', '04 Nights', 'Premium', 'Superior Room / Valley Room', 'Breakfast & Dinner', 5, 2),
                    _hotel('The Lalit Chandigarh (Luxury Suite) | Welcomhotel by ITC Hotels, Kasauli', 'Chandigarh / Kasauli', '04 Nights', 'Luxury', 'Luxury Suite / Premium Room', 'Breakfast & Dinner', 5, 3),
                    _hotel('The Oberoi Sukhvilas Spa Resort | TRAGUIN Private Elite Villas & Spas', 'Chandigarh / Kasauli', '04 Nights', 'Ultra Luxury', 'Private Elite Villa', 'All Inclusive Premium', 5, 4),
        ],
        inclusions=[
                    _inc_included('02 Nights in Chandigarh & 02 Nights in Kasauli at handpicked premium hotels', 1),
                    _inc_included('Daily multi-cuisine buffet breakfast and curated chef-crafted dinners', 2),
                    _inc_included('Dedicated private luxury Innova Crysta for all transfers and tours', 3),
                    _inc_included('Private solar boat cruise experience at Sukhna Lake', 4),
                    _inc_included('All monument entry passes, parking fees, highway tolls, and driver allowances', 5),
                    _inc_included('Complimentary welcome amenities, fresh seasonal fruits, and mineral water bottles', 6),
                    _inc_included('Specialized 24/7 TRAGUIN on-ground destination support', 7),
                    _inc_excluded('Inter-state flights or railway tickets to Chandigarh', 8),
                    _inc_excluded('Personal items such as laundry, phone charges, or liquor', 9),
                    _inc_excluded('Additional adventure sports, paragliding, or porter tips', 10),
                    _inc_excluded('Medical insurance and items not declared in the inclusions', 11),
        ],
    )
    return package, itinerary



def build_ch_019(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'CH-019'
    tour_code = 'TG-CH-019-TAJ'
    title = 'Taj Chandigarh Premium Stay Experience'
    duration = '02 Nights / 03 Days'
    slug = 'ch-019-taj-chandigarh-premium-stay-experience'
    itin_slug = 'ch-019-taj-chandigarh-premium-stay-itinerary'
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
                    _ph('Serial code CH-019 | TRAGUIN tour code TG-CH-019-TAJ', 1),
                    _ph('State / Country: Chandigarh / India | Category: Luxury Weekend', 2),
                    _ph('Destinations: Chandigarh (Taj Stay)', 3),
                    _ph('Ideal for: Couples, Corporate & Discerning Travelers', 4),
                    _ph('Best season: Year-Round (October to March preferred)', 5),
                    _ph('02 Nights ultra-luxury accommodation at Taj Chandigarh', 6),
                    _ph('TRAGUIN Signature Experience: Private reserved sunset cruise across Sukhna Lake followed by gourmet high-tea', 7),
                    _ph('Shopping: Sector 17 Plaza, Phulkari handicrafts, gourmet dining at Dera and Black Lotus', 8)
        ],
        moods=['Luxury', 'Romantic', 'Cultural'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Taj Premium Stay)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Rock Garden • Rose Garden • Sukhna Lake Luxury Cruise',
        overview=(
            'Welcome to the masterfully planned "Beautiful City" of India. This premium luxury proposal, artfully designed by TRAGUIN holiday planners, presents a flawless 2-Night getaway centered around the legendary hospitality of Taj Chandigarh. Perfect for discerning guests seeking immersive experiences, this holiday effortlessly blends the iconic attractions of Le Corbusier\'s architectural marvel with premium stays and scenic beauty.\n\nTravel Dates / Format: Fully Customized Luxury FIT Proposal. Vehicle: Chauffeur-driven Premium Luxury Sedan. Meal Plan: Modified American Plan (Gourmet Breakfast & Elaborate Dinner at Taj). TRAGUIN Curated Touch: Reserved sunset shikara/boat cruise at Sukhna Lake, private guided monument walk, and priority access check-ins.'
        ),
        seo_title='CH-019 | Taj Chandigarh Premium Stay Experience | TRAGUIN',
        seo_description='Luxury 02 Nights / 03 Days Taj stay package (CH-019 / TG-CH-019-TAJ): Sukhna Lake sunset cruise, Rock Garden, Rose Garden, Jiva Spa leisure, and 4-tier hotel options.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
                    _ih('Sukhna Lake Private Sunset Boat Cruise', 1),
                    _ih('Nek Chand Rock Garden & Rose Garden Tour', 2),
                    _ih('Taj Chandigarh Premium Luxury Room Stay', 3),
                    _ih('Sector 17 Open-Air Plaza or Elante Mall Transit', 4),
                    _ih('Optional Jiva Spa Therapeutic Massage', 5)
        ],
        days=[
        _day(
            1,
            'Arrival in Chandigarh & Sunset Sukhna Cruise',
            (
                'Your ultimate luxury getaway begins the moment you step foot in the city. You will be greeted with a warm welcome at Chandigarh Airport or Chandigarh Railway Station by our professional chauffeur. Transfer immediately in your premium luxury sedan to the iconic Taj Chandigarh. Your private vehicle will chauffeur you to the scenic Sukhna Lake for an exclusive, private sunset boat ride arranged by TRAGUIN.'
            ),
            [
                'Sightseeing Included: Sukhna Lake Lakefront Walk, Private Boat Cruise',
                'Evening Experience: Luxury lakeside high-tea and sunset photography',
                'Overnight Stay: Taj Chandigarh (Premium Luxury Room)',
                'Meals Included: Welcome Buffet Dinner at Black Lotus / Dera'
            ],
        ),
        _day(
            2,
            'The Magic of Rock Garden & Botanical Rose Garden Tour',
            (
                "Awaken to a lavish, curated breakfast at Cafe 17. Our first destination is Nek Chand's world-renowned Rock Garden. Next, enjoy a brief drive to the beautiful Zakir Hussain Rose Garden, Asia's largest botanical rose sanctuary. In the evening, explore the upscale Sector 17 market plaza for exclusive premium shopping before returning to the Taj for a signature dining experience."
            ),
            [
                "Sightseeing Included: Nek Chand's Rock Garden, Zakir Hussain Rose Garden",
                'Optional Activities: Guided architectural walk at the Capitol Complex',
                'Overnight Stay: Taj Chandigarh',
                "Meals Included: Gourmet Breakfast & Chef's Special Farewell Dinner"
            ],
        ),
        _day(
            3,
            'Luxury Spa Retreat & Departure with Memories',
            (
                'Indulge in a luxurious late morning breakfast at the hotel. Today is yours to relax and experience the premium indoor amenities of Taj Chandigarh. We highly recommend treating yourself to an immersive therapeutic massage at the award-winning Jiva Spa. After checking out from your room at noon, your private vehicle will be ready for departure to the airport or station.'
            ),
            [
                'Sightseeing Included: Sector 17 open-air plaza or luxury mall transit',
                'Assistance: Complete executive handling up to the departure lounge',
                'Overnight Stay: Tour Concludes',
                'Meals Included: Rich Buffet Breakfast'
            ],
        )
        ],
        hotels=[
                    _hotel('Hyatt Regency Chandigarh', 'Chandigarh', '02 Nights', 'Deluxe', 'Standard King Room', 'Breakfast Only', 5, 1),
                    _hotel('The Oberoi Sukhvilas Spa Resort', 'New Chandigarh', '02 Nights', 'Premium', 'Premier Room', 'Breakfast Only', 5, 2),
                    _hotel('Taj Chandigarh (Primary Highlight)', 'Chandigarh', '02 Nights', 'Luxury', 'Superior Luxury City View Room', 'Breakfast & Dinner', 5, 3),
                    _hotel('Taj Chandigarh / Sukhvilas Luxury Suites', 'Chandigarh', '02 Nights', 'Ultra Luxury', 'Luxury Executive Suite with Jacuzzi', 'All Inclusive Premium Plan', 5, 4),
        ],
        inclusions=[
                    _inc_included('02 Nights ultra-luxury accommodation at Taj Chandigarh', 1),
                    _inc_included('Lavish daily breakfast spread and curated multi-course dinners at Taj signature restaurants', 2),
                    _inc_included('Private dedicated luxury sedan/SUV transfers throughout your stay', 3),
                    _inc_included('All monumental entry tickets, priority parking passes, and private boat fees at Sukhna Lake', 4),
                    _inc_included('Complimentary welcome amenities, fresh flowers, and fresh seasonal fruit basket upon arrival', 5),
                    _inc_included('24/7 dedicated TRAGUIN customer support and on-ground travel concierge', 6),
                    _inc_included('Full taxes, fuel charges, toll payments, and chauffeur allowances', 7),
                    _inc_excluded('Inter-city airfare, flight charges, or train tickets to Chandigarh', 8),
                    _inc_excluded('Personal expenses such as telephone calls, laundry, or premium mini-bar items', 9),
                    _inc_excluded('Spa therapies, salon treatments, or specialized dynamic body massages at Jiva Spa', 10),
                    _inc_excluded('Camera or professional video fees at heritage sites', 11),
                    _inc_excluded('Travel and personal medical insurance plans', 12),
        ],
    )
    return package, itinerary

CHANDIGARH_DOMESTIC_BUILDERS = [
    build_ch_007,
    build_ch_008,
    build_ch_009,
    build_ch_010,
    build_ch_011,
    build_ch_012,
    build_ch_013,
    build_ch_014,
    build_ch_015,
    build_ch_016,
    build_ch_017,
    build_ch_018,
    build_ch_019,
]
