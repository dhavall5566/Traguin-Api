"""Builder functions for PY-001 through PY-010 Puducherry domestic packages."""

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

PUDUCHERRY_SLUG = "puducherry"


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


def build_py_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'PY-001'
    tour_code = 'TG-PY-FAM-001'
    title = 'Premium Puducherry Family Escape'
    duration = '03 Nights / 04 Days'
    slug = 'py-001-premium-puducherry-family-escape'
    itin_slug = 'py-001-premium-puducherry-family-escape-itinerary'
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
            _ph('State / Country: Puducherry, India | Category: Family Tour', 2),
            _ph('Destinations: White Town • Auroville • Paradise Beach • Promenade', 3),
            _ph('Ideal for: Families, Couples, Leisure Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle: Premium Air-Conditioned Private Family MUV (Toyota Innova Crysta / Luxury Segment)', 7),
            _ph('Meal Plan: Premium Buffet Breakfast & Curated Fusion Dinners (MAPAI Plan)', 8),
            _ph('Route Map: Chennai / Puducherry Airport Transfer → White Town Heritage Zone → Auroville → Paradise Beach → Departure', 9),
            _ph('TRAGUIN Signature Experience: Private family heritage storyteller guide to uncover hidden colonial secrets within White Town.', 10),
            _ph('Exclusive Recommendations: Curated list of high-end French cafés and sea-facing dinner tables with priority reservations.', 11),
            _ph('Shopping & Local Experiences: Local Markets: Famous for purchasing handmade paper at Aurobindo paper mill, custom terracotta items, and leather bags at Goubert market. Food Recommendations: Classic wood-fired pizzas at Café Extasi and delicious sea-salt gelato scoops near the old lighthouse.', 12),
            _ph('Important Notes: Booking Tip: Heritage properties in White Town have limited room capacity; booking 45-60 days prior is highly advisable. Dress Code: Kindly wear modest attire covering shoulders and knees when entering Auroville or ashram spaces.', 13),
        ],
        moods=['Family', 'Leisure', 'Coastal'],
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
        tagline='Premium Puducherry Family Escape • 03 Nights / 04 Days',
        overview=(
            'Welcome to the French Riviera of the East. This meticulously organized Puducherry Family Tour designed expertly by TRAGUIN merges vintage colonial architecture, coastal tranquility, and experiential relaxation. Wander down colorful mustard lanes, indulge in warm buttery croissants, and forge unforgettable memories across breathtaking landscapes. From immersive experiences inside spiritual ashrams to private speedboats across turquoise backwaters, rest easy inside premium stays and handpicked hotels offering elite hospitality.\n\nTOUR OVERVIEW\nVehicle Type: Premium Air-Conditioned Private Family MUV (Toyota Innova Crysta / Luxury Segment)\nMeal Plan: Premium Buffet Breakfast & Curated Fusion Dinners (MAPAI Plan)\nRoute Plan: Chennai / Puducherry Airport Transfer → White Town Heritage Zone → Auroville → Paradise Beach → Departure\n\nCurated Note:\nThis premium luxury holiday crafted by TRAGUIN Experts features complimentary French pastry tastings, priority booking for private beach excursions, and comprehensive on-call localized operational TRAGUIN Support.\n\nPuducherry is an incredibly picturesque coastal destination, highly sought after by travelers seeking the Best Puducherry Tour Package or a relaxed Puducherry Honeymoon Package. Offering a distinctive combination of heritage and coastal lifestyle, it presents unparalleled vacation points for family escapes.\n**White Town French Quarter:** Famous for its iconic attractions, pastel-yellow architecture, Bougainvillea-draped walls, and amazing Instagram locations for family portraits.\n**Auroville Matrimandir:** A mesmerizing golden metallic sphere representing unity, highly searched for spiritual immersive experiences.\n**Paradise Beach Lagoon:** An isolated golden beach access accessible via beautiful backwater speedboats, perfect for children and family beach activities.\n**Best Time to Visit Puducherry:** The mild and breezy coastal winter season between October and March offers perfect conditions for seamless Puducherry Sightseeing.'
        ),
        seo_title='PY-001 | Premium Puducherry Family Escape | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Puducherry package (PY-001 / TG-PY-FAM-001): White Town, Auroville, Paradise Beach, Promenade, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('White Town French Quarter, Auroville Matrimandir Viewpoint, and Paradise Beach Lagoon', 1),
            _ih('Chunnambar Backwaters private speedboat charter and Sacred Heart Basilica', 2),
            _ih('TRAGUIN Signature Experience: Private family heritage storyteller guide within White Town', 3),
            _ih('French pastry tasting trail and curated sea-facing dinner reservations', 4),
            _ih('Premium 4-tier handpicked accommodation across heritage and beachfront properties', 5),
        ],
        days=[
            _day(
                1,
                'Arrival & Immersive White Town Coffee Trail',
                (
                    'Arrive in Chennai or Puducherry terminal, where your dedicated TRAGUIN executive receives you with a chilled welcome hamper. Enjoy a scenic route cruise along the East Coast Road to your handpicked luxury hotel. After a seamless check-in, begin your Puducherry Sightseeing with a guided walking tour through the cobblestone paths of White Town. Admire the colonial French villas before enjoying an evening stroll along the bustling Goubert Avenue Promenade beach.'
                ),
                [
                    'Sightseeing Included: White Town Quarter, French War Memorial, Promenade Beachwalk',
                    'Evening Experience: A complimentary French pastry and artisanal coffee tasting at a vintage courtyard cafe.',
                    'Overnight Stay: Puducherry (Premium Boutique French Heritage Hotel)',
                    'Meals Included: Luxury Fusion Dinner',
                ],
            ),
            _day(
                2,
                'Auroville Peace Spirit & Spiritual Ashram Harmony',
                (
                    'Savor an early premium breakfast at your hotel. Today we explore Auroville, the international township of peace. Take a beautiful shaded walking trail to the viewing point of the iconic golden Matrimandir dome. Afterwards, return to the main city center to visit the serene Sri Aurobindo Ashram, soaking in its quiet meditative atmosphere. Spend the late afternoon shopping for organic incense and handmade paper at local boutique stores.'
                ),
                [
                    'Sightseeing Included: Auroville Matrimandir Viewpoint, Aurobindo Ashram, Manakula Vinayagar Temple',
                    'Photography Points: The striking contrast of the golden Matrimandir against the green forest canopy.',
                    'Overnight Stay: Puducherry',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'Boat Cruise to Paradise Beach & Gourmet Lakeside High Tea',
                (
                    'Enjoy a tropical breakfast before driving to Chunnambar Boat House. Board an exclusive private speedboat charter cutting through lush mangrove backwaters to reach the golden sands of Paradise Beach. Spend your morning relaxing on the shores, trying water sports, or swimming safely. In the afternoon, explore the 130-year-old sacred Sacred Heart Basilica before a spectacular family dinner.'
                ),
                [
                    'Sightseeing Included: Chunnambar Backwaters, Paradise Beach, Basilica of the Sacred Heart of Jesus',
                    'Optional Activities: Jet-skiing or tandem beach volleyball arranged by the shore crew.',
                    'Overnight Stay: Puducherry (Premium Luxury Beachfront Resort)',
                    'Meals Included: Breakfast & Seashore Specialty Dinner',
                ],
            ),
            _day(
                4,
                'Boutique Souvenir Selection & Farewell Puducherry',
                (
                    'Indulge in a final delicious breakfast by the poolside. Take advantage of your last morning to pick up authentic souvenirs like clay pottery, hand-woven linens, or French chocolates. Your private chauffeur will then transfer your family comfortably back to the airport or station. Your premium TRAGUIN Puducherry Packages experience concludes here, leaving you with beautiful stories and unforgettable memories.'
                ),
                [
                    'Meals Included: Breakfast',
                    'Assistance: Airport/station baggage handling and priority drop-off assistance by our driver.',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Atithi / Ocean Spray Residency',
                'Puducherry',
                '03 Nights',
                'Deluxe',
                'Standard Comfort Room',
                'MAPAI Plan',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Atithi / Ocean Spray Residency (Standard Comfort Room)',
            ),
            _hotel(
                'Maison Perumal - CGH Earth / Atithi TGI Grand',
                'Puducherry',
                '03 Nights',
                'Premium',
                'Premium Heritage Room',
                'MAPAI Plan',
                4,
                2,
                description='OPTION 02 – PREMIUM: Maison Perumal - CGH Earth / Atithi TGI Grand (Premium Heritage Room)',
            ),
            _hotel(
                'Villa Shanti / Radisson Resort Pondicherry Bay',
                'Puducherry',
                '03 Nights',
                'Luxury',
                'Executive Premium Room',
                'MAPAI Plan',
                5,
                3,
                description='OPTION 03 – LUXURY: Villa Shanti / Radisson Resort Pondicherry Bay (Executive Premium Room)',
            ),
            _hotel(
                'Palais de Mahé - CGH Earth / The Promenade Premium Oceanfront',
                'Puducherry',
                '03 Nights',
                'Ultra Luxury',
                'Luxury Suite',
                'MAPAI Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Palais de Mahé - CGH Earth / The Promenade Premium Oceanfront (Luxury Suite)',
            ),
        ],
        inclusions=[
            _inc_included('Premium handpicked boutique heritage resort accommodations.', 1),
            _inc_included('Daily artisan breakfasts and multi-course specialty dinners.', 2),
            _inc_included('Private luxury AC Innova Crysta for all transfers & touring.', 3),
            _inc_included('Private speedboat charter tickets to Paradise Beach.', 4),
            _inc_included('Complimentary French patisserie tasting trail voucher.', 5),
            _inc_included('Dedicated 24/7 localized emergency and luxury TRAGUIN Support.', 6),
            _inc_excluded('Flights or interstate rail tickets to/from Chennai/Puducherry.', 7),
            _inc_excluded('Monument camera passes or commercial videography permissions.', 8),
            _inc_excluded('Personal laundry, telephone calls, or hard alcoholic beverages.', 9),
            _inc_excluded('Optional watersports or surfing instruction fees.', 10),
        ],
    )
    return package, itinerary

def build_py_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'PY-002'
    tour_code = 'TG-PY-HON-002'
    title = 'Romantic Puducherry Premium Honeymoon Package'
    duration = '03 Nights / 04 Days'
    slug = 'py-002-romantic-puducherry-premium-honeymoon-package'
    itin_slug = 'py-002-romantic-puducherry-premium-honeymoon-package-itinerary'
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
            _ph('State / Country: Puducherry, India | Category: Honeymoon / Romantic Getaway', 2),
            _ph('Destinations: White Town • Paradise Beach • Auroville • Promenade', 3),
            _ph('Ideal for: Honeymooners, Couples, Luxury Seekers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle: Private Premium Chauffeur-Driven Air-Conditioned Sedan', 7),
            _ph('Meal Plan: Breakfast & Curated Candlelight French-Continental Specialty Dinners', 8),
            _ph('Route Map: Chennai / Puducherry Arrival → White Town Heritage Quarter → Paradise Beach → Auroville → Departure', 9),
            _ph('TRAGUIN Signature Experience: Pre-reserved premium table settings at famous heritage cafes with curated taster menus.', 10),
            _ph('Curated by TRAGUIN Experts: Custom-tailored routing schedules to let you avoid peak midday crowds at top attractions.', 11),
            _ph("Shopping & Local Experiences: Famous Souvenirs: Hand-rolled organic candles, Auroville aromatherapy essential oils, handmade leather items, and gourmet French cheese. Top Café Recommendations: Cafe Des Arts, Villa Shanti Restaurant, and Baker's Street for authentic French croissants.", 12),
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
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Romantic Puducherry Premium Honeymoon Package • 03 Nights / 04 Days',
        overview=(
            "Escape to India's own French Riviera. The ultimate Puducherry Honeymoon Package, passionately curated by TRAGUIN, blends old-world French elegance, quiet cobblestone streets, and intimate coastal walks. Stroll past mustard-hued colonial villas, capture breathtaking landscapes, and relax in premium stays and handpicked hotels that whisper luxury and romance. Allow us to craft unforgettable memories for your new beginning through highly exclusive experiences and unparalleled personal hospitality.\n\nTOUR OVERVIEW\nTravel Mode: Private Premium Chauffeur-Driven Air-Conditioned Sedan\nMeal Plan: Breakfast & Curated Candlelight French-Continental Specialty Dinners\nRoute Plan: Chennai / Puducherry Arrival → White Town Heritage Quarter → Paradise Beach → Auroville → Departure\n\nCurated Note:\nThis premium luxury holiday includes customized room amenities, private beach ferry boat transfers, handpicked romantic café reservations, and 24/7 dedicated guest concierge support by TRAGUIN Experts.\n\nPuducherry shines beautifully as a coastal haven, making it a highly searched option for a Best Puducherry Tour Package or a romantic Puducherry Honeymoon Package. Brimming with vintage European charm, artistic cafes, and golden shores, it offers an absolute Premium Puducherry Experience for couples looking for luxury and culture.\n**White Town (French Quarter):** A postcard-perfect neighborhood with vibrant bougainvillea, pastel facades, and unique architectural design—the ultimate popular Instagram location for romance.\n**Paradise Beach:** An isolated shoreline with soft golden sands accessible by a scenic backwater boat ride, offering peaceful seclusion and scenic beauty.\n**Auroville Matrimandir:** A magnificent golden sphere representing harmony and soulfulness, offering deep, immersive experiences for newly married couples.\n**Best Time to Visit Puducherry:** The refreshing winter climate between October and March provides an ideal setting for romantic walks and comprehensive Puducherry Sightseeing."
        ),
        seo_title='PY-002 | Romantic Puducherry Premium Honeymoon Package | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Puducherry honeymoon package (PY-002 / TG-PY-HON-002): White Town, Paradise Beach, Auroville, Promenade, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('White Town Heritage Quarter, Promenade Beach sunset, and Mahatma Gandhi Statue', 1),
            _ih('Auroville Matrimandir Viewpoint, Auroville Beach, and Sri Aurobindo Ashram', 2),
            _ih('Chunnambar Backwaters ferry cruise to Paradise Beach and vintage bicycle heritage tour', 3),
            _ih('TRAGUIN Signature Experience: Private multi-course French-Continental candlelight dinner with artisanal cake setup', 4),
            _ih('Premium 4-tier handpicked romantic heritage accommodation in the French Quarter', 5),
        ],
        days=[
            _day(
                1,
                'Arrival in Puducherry – Charming White Town & Promenade Sunset',
                (
                    'Your romantic journey begins with a smooth drive from Chennai along the scenic East Coast Road. Arrive in Puducherry, where a TRAGUIN coordinator greets you warmly at your handpicked luxury heritage hotel. After checking in, spend a relaxed afternoon discovering the cobblestone lanes of White Town. Walk hand-in-hand past iconic attractions like the French Consulate and Raj Nivas, and watch a beautiful sunset along the beachfront Promenade.'
                ),
                [
                    'Sightseeing Included: White Town Heritage Quarter, Promenade Beach, Mahatma Gandhi Statue',
                    'Welcome Amenities: Complimentary premium pastries, an artisanal chocolate hamper, and customized floral decor in-room.',
                    'Overnight Stay: Puducherry (French Quarter Luxury Heritage Suite)',
                    'Meals Included: Dinner',
                ],
            ),
            _day(
                2,
                'Auroville Spiritual Trails & Private Candlelight Dinner',
                (
                    'Wake up to a classic French-style breakfast. Today, take a short drive to the experimental township of Auroville. Walk through the shaded green trails to reach the viewpoint facing the majestic golden Matrimandir. In the afternoon, explore artistic boutiques and organic cafes nearby. Return to your resort for a luxurious evening, culminating in a highly romantic private candlelight dinner organized exclusively for you.'
                ),
                [
                    'Sightseeing Included: Auroville Matrimandir Viewpoint, Auroville Beach, Sri Aurobindo Ashram',
                    'Exclusive Experiences: Private multi-course French-Continental candlelight dinner with an artisanal cake setup.',
                    'Overnight Stay: Puducherry',
                    'Meals Included: Breakfast & Specialty Candlelight Dinner',
                ],
            ),
            _day(
                3,
                'Paradise Beach Backwater Cruise & Soulful Cycling Tour',
                (
                    'Following a premium breakfast, your private chauffeur takes you to Chunnambar boat house. Board a private ferry boat cruise navigating the calm backwaters to reach the golden shores of Paradise Beach. Enjoy a peaceful afternoon on the sand. In the late afternoon, take a vintage-style guided bicycle tour through the Tamil and French quarters, capturing the unique architecture and local lifestyle.'
                ),
                [
                    'Sightseeing Included: Chunnambar Backwaters, Paradise Beach, Sacred Heart Basilica, Cluny Embroidery Centre',
                    'Photography Points: Bougainvillea hanging over pastel-yellow walls along Rue Romain Rolland.',
                    'Overnight Stay: Puducherry',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'Boutique Shopping, Café Insights & Departure with Forever Memories',
                (
                    'Savor a lazy morning breakfast. Enjoy some final-hour shopping for fine hand-made paper items, aromatic incense, and clay pottery at local boutiques. Take a quiet moment to sit in a French café before your private chauffeur transfers you back to Chennai. Your romantic Luxury Puducherry Holiday and unforgettable honeymoon package concludes here, leaving you with divine blessings and stories to cherish for a lifetime, proudly arranged by TRAGUIN.'
                ),
                [
                    'Meals Included: Breakfast',
                    'Assistance: Airport or railway terminal drop assistance with priority luggage handling support.',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Atithi / Ocean Spray Residency',
                'Puducherry',
                '03 Nights',
                'Deluxe',
                'Standard Comfort Room',
                'Breakfast & Specialty Dinners',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Atithi / Ocean Spray Residency (Standard Comfort Room)',
            ),
            _hotel(
                'Maison Perumal - CGH Earth / Gratitude Heritage',
                'Puducherry',
                '03 Nights',
                'Premium',
                'Premium Heritage Room',
                'Breakfast & Specialty Dinners',
                4,
                2,
                description='OPTION 02 – PREMIUM: Maison Perumal - CGH Earth / Gratitude Heritage (Premium Heritage Room)',
            ),
            _hotel(
                'Villa Shanti / La Villa Pondicherry',
                'Puducherry',
                '03 Nights',
                'Luxury',
                'Luxury Heritage Room',
                'Breakfast & Specialty Dinners',
                5,
                3,
                description='OPTION 03 – LUXURY: Villa Shanti / La Villa Pondicherry (Luxury Heritage Room)',
            ),
            _hotel(
                'Palais de Mahé - CGH Earth / The Promenade Premium Ocean View Suite',
                'Puducherry',
                '03 Nights',
                'Ultra Luxury',
                'Premium Ocean View Suite',
                'Breakfast & Specialty Dinners',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Palais de Mahé - CGH Earth / The Promenade Premium Ocean View Suite',
            ),
        ],
        inclusions=[
            _inc_included('Handpicked heritage boutique accommodations with romantic accents.', 1),
            _inc_included('Daily breakfast & gourmet multi-course dinners.', 2),
            _inc_included('One highly exclusive private candlelight dining experience.', 3),
            _inc_included('Private luxury AC Sedan for all transfers & premium sightseeing routes.', 4),
            _inc_included('Ferry boat tickets for the Paradise Beach cruise.', 5),
            _inc_included('Complimentary vintage guided bicycle heritage tour.', 6),
            _inc_included('Continuous personalized assistance and on-ground TRAGUIN Support.', 7),
            _inc_excluded('Airfare or inter-state train ticket charges.', 8),
            _inc_excluded('Monument or camera entry tickets at sightseeing gates.', 9),
            _inc_excluded('Personal laundry, phone billing, or premium alcoholic beverages.', 10),
            _inc_excluded('Any optional water sports, surfing lessons, or guide tips.', 11),
        ],
    )
    return package, itinerary

def build_py_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'PY-003'
    tour_code = 'TG-PY-FAM-003'
    title = 'Premium Puducherry Family Tour Package'
    duration = '04 Nights / 05 Days'
    slug = 'py-003-premium-puducherry-family-tour-package'
    itin_slug = 'py-003-premium-puducherry-family-tour-package-itinerary'
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
            _ph('State / Country: Puducherry, India | Category: Luxury Family Escape', 2),
            _ph('Destinations: Puducherry (Pondicherry) • Auroville • Paradise Beach', 3),
            _ph('Ideal for: Families, Couples, Leisure Travelers, Culture Seekers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle: Private Premium Air-Conditioned Luxury Sedan / SUV (Dedicated Chauffeur)', 7),
            _ph('Meal Plan: Breakfast & Curated Multi-Cuisine Dinners (French & Coastal Specialty Menus)', 8),
            _ph('Route Map: Chennai Airport/Station → Puducherry French Quarter → Auroville → Chennai Departure', 9),
            _ph('TRAGUIN Signature Experience: Private heritage walking tour with an expert local storyteller detailing the hidden history of French colonial architecture.', 10),
            _ph('Curated by TRAGUIN Experts: Exclusive culinary layout featuring guaranteed reservations at top-rated, hard-to-book hidden French courtyard cafes.', 11),
            _ph('Shopping & Local Experiences: Local Boutiques: Famous for purchasing handmade organic papers from Sri Aurobindo Paper Factory, artisanal terracotta pottery, terracotta jewelry, and premium leather accessories. Food Recommendations: Classic wood-fired pizzas at Café Extasi, freshly baked croissants at Baker Street, and classic French gelato at Gelateria Montecatini Terme.', 12),
            _ph('Important Notes: Advance Booking Suggestion: To enter the inner meditation hall of Matrimandir, bookings must be done individually by guests weeks ahead. TRAGUIN includes viewing area access. Footwear Notice: Most ashram locations require removing shoes before entering; wearing comfortable slip-on footwear is highly advised. Eco-friendly City: Puducherry actively restricts single-use plastics; carrying reusable water bottles is encouraged.', 13),
        ],
        moods=['Family', 'Culture', 'Luxury'],
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
        tagline='Premium Puducherry Family Tour Package • 04 Nights / 05 Days',
        overview=(
            'Welcome to the French Riviera of the East, where quaint colonial charm seamlessly meets deep spiritual tranquility. This masterfully designed Luxury Puducherry Holiday crafted exclusively by TRAGUIN promises your family an exceptional coastal escape. Wander through pastel-colored lanes, indulge in curated culinary journeys, and witness breathtaking landscapes. Our premium stays and handpicked hotels combine absolute luxury with deep structural heritage, crafting unforgettable memories for you and your loved ones.\n\nTOUR OVERVIEW\nTravel Mode: Private Premium Air-Conditioned Luxury Sedan / SUV (Dedicated Chauffeur)\nMeal Plan: Breakfast & Curated Multi-Cuisine Dinners (French & Coastal Specialty Menus)\nRoute Plan: Chennai Airport/Station → Puducherry French Quarter → Auroville → Chennai Departure\n\nCurated Note:\nThis premium TRAGUIN Puducherry Package features pre-cleared VIP passes to the Auroville Matrimandir viewing area, expert local heritage guides, and handpicked gourmet cafe recommendations.\n\nPuducherry shines beautifully as a unique cultural melting pot, making it an incredibly popular selection for a Best Puducherry Tour Package or a relaxing Puducherry Family Tour. Famous for its colonial French architectures, serene beaches, and spiritual enclaves, it offers an incredible mix of leisure and experiential luxury.\n**The French Quarter (White Town):** A mesmerizing district filled with mustard-colored colonial villas, chic boutiques, and iconic attractions that serve as the top Instagram locations in the region.\n**Auroville (City of Dawn):** A world-renowned experimental township focused on human unity, featuring the magnificent golden Matrimandir sphere.\n**Top Tourist Places in Puducherry:** Includes the Promenade Beach, Sri Aurobindo Ashram, Basilica of the Sacred Heart of Jesus, and Chunnambar Boat House.\n**Best Time to Visit Puducherry:** The pleasant and refreshing cooler months from October to March present the most optimal climate to experience extensive Puducherry Sightseeing.'
        ),
        seo_title='PY-003 | Premium Puducherry Family Tour Package | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Puducherry family package (PY-003 / TG-PY-FAM-003): Puducherry, Auroville, Paradise Beach, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('East Coast Road scenic drive, Promenade Beach, and White Town heritage walk', 1),
            _ih('Auroville Matrimandir Viewing Point, Auroville Botanical Gardens, and sustainable craft workshop', 2),
            _ih('Chunnambar Backwaters private speedboat cruise and Paradise Beach private cruise', 3),
            _ih('TRAGUIN Signature Experience: Private heritage walking tour with expert local storyteller', 4),
            _ih('Premium 4-tier handpicked accommodation in White Town and coastal resorts', 5),
        ],
        days=[
            _day(
                1,
                'Arrival & Smooth Transfer to Puducherry – Evening Promenade Walk',
                (
                    'Your luxury vacation starts with a warm welcome by your private TRAGUIN chauffeur at Chennai International Airport or railway station. Embark on a highly scenic drive along the stunning East Coast Road (ECR), watching the waves lap against the shoreline. Upon arrival in Puducherry, check in to your premium heritage hotel in White Town. Spend a relaxing evening walking along the famous Promenade Beach, listening to the roaring waves and breathing in the crisp sea air.'
                ),
                [
                    'Sightseeing Included: East Coast Road Scenic Drive, Promenade Beach, Mahatma Gandhi Statue',
                    'Evening Experience: A family sunset stroll along the rocky beach followed by a welcome dinner featuring fusion Franco-Tamil cuisine.',
                    'Overnight Stay: Puducherry (Premium French Quarter Heritage Boutique Hotel)',
                    'Meals Included: Luxury Buffet Dinner',
                ],
            ),
            _day(
                2,
                'French Quarter Heritage Walk & Spiritual Ashram Immersion',
                (
                    'Awake to a fresh morning and enjoy a delicious breakfast. Meet our expert storyteller guide for a curated walking tour through the tree-lined boulevards of White Town. Admire the stunning architectural preservation of the French villas with their grand arches and bougainvillea gates. Visit the deeply peaceful Sri Aurobindo Ashram, a core spiritual pillar of the city, and spend quiet family moments in its meditative courtyard. Later, explore the magnificent gothic architecture of the Basilica of the Sacred Heart.'
                ),
                [
                    'Sightseeing Included: White Town Heritage Walk, Sri Aurobindo Ashram, Notre Dame des Anges, Sacred Heart Basilica',
                    'Photography Points: The bright pastel yellow walls and retro French street signs of Rue Romain Rolland.',
                    'Overnight Stay: Puducherry',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'Excursion to Auroville – Sparking the Golden Matrimandir Wisdom',
                (
                    'Savor a delightful gourmet breakfast before taking a short comfortable drive to the international township of Auroville. Journey along shaded red-earth pathways to reach the spectacular Matrimandir viewing point, marveling at the giant golden orb built as a symbol of human unity. Introduce your family to sustainable living with a curated lunch at the Auroville solar kitchen area. In the afternoon, explore the local boutique craft shops specializing in organic handmade papers and fine porcelain pottery.'
                ),
                [
                    "Sightseeing Included: Auroville Visitor's Centre, Matrimandir Viewing Point, Auroville Botanical Gardens",
                    'Exclusive Experiences: Private interaction at a sustainable local craft workshop organized by TRAGUIN Experts.',
                    'Overnight Stay: Puducherry',
                    'Meals Included: Breakfast & Specially Curated Farm-to-Table Dinner',
                ],
            ),
            _day(
                4,
                'Sun-Kissed Paradise Beach Cruise & Mangrove Kayak Escape',
                (
                    'Following a refreshing premium breakfast, head south to the Chunnambar Boat House. Board your private speedboat cruise down the backwaters to reach the isolated sands of Paradise Beach. This pristine coastline offers pure soft sands and clear waters, ideal for family beach games and relaxation. For the adventurous, try an optional guided kayak ride through the nearby lush mangrove forests of Arts and Crafts Village before heading back to the hotel.'
                ),
                [
                    'Sightseeing Included: Chunnambar Backwaters, Paradise Beach Private Cruise',
                    'Optional Activities: Guided mangrove kayaking, jet-skiing, or beach volleyball.',
                    'Overnight Stay: Puducherry Luxury Coastal Resort',
                    'Meals Included: Breakfast & Coastal Seafood Barbecue Dinner',
                ],
            ),
            _day(
                5,
                'Cafe Hopping, Artisanal Shopping & Smooth Departure',
                (
                    'Enjoy a lazy breakfast at your resort patio. Spend your final morning cafe-hopping across the trendy French cafes of White Town, sipping artisanal coffees and tasting fresh buttery croissants. Your private chauffeur will then load your luggage and drive you comfortably back to Chennai International Airport or railway station. Your magnificent Premium Puducherry Experience concludes here, leaving your family with beautiful blessings and unforgettable memories to last a lifetime.'
                ),
                [
                    'Meals Included: Breakfast',
                    'Assistance: Airport drop-off coordination and luggage handling by your professional driver.',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Atithi / Ocean Spray Residency',
                'Puducherry',
                '04 Nights',
                'Deluxe',
                'Standard Comfort Room',
                'Breakfast & Multi-Cuisine Dinners',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Atithi / Ocean Spray Residency (Standard Comfort Room)',
            ),
            _hotel(
                'Maison Perumal - CGH Earth / Gratitude Heritage',
                'Puducherry',
                '04 Nights',
                'Premium',
                'Premium Heritage Room',
                'Breakfast & Multi-Cuisine Dinners',
                4,
                2,
                description='OPTION 02 – PREMIUM: Maison Perumal - CGH Earth / Gratitude Heritage (Premium Heritage Room)',
            ),
            _hotel(
                'Villa Shanti / Gratitude Heritage / Radisson Resort Pondicherry',
                'Puducherry',
                '04 Nights',
                'Luxury',
                'Premium Rooms',
                'Breakfast & Multi-Cuisine Dinners',
                5,
                3,
                description='OPTION 03 – LUXURY: Villa Shanti / Gratitude Heritage / Radisson Resort Pondicherry (Premium Rooms)',
            ),
            _hotel(
                'Palais de Mahé - CGH Earth / The Promenade Premium Ocean View',
                'Puducherry',
                '04 Nights',
                'Ultra Luxury',
                'Luxury Suites',
                'Breakfast & Multi-Cuisine Dinners',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Palais de Mahé - CGH Earth / The Promenade Premium Ocean View (Luxury Suites)',
            ),
        ],
        inclusions=[
            _inc_included('Premium luxury heritage hotel stays directly inside White Town or coastal resorts.', 1),
            _inc_included('Daily breakfast & curated multi-course specialty dinners.', 2),
            _inc_included('Private luxury AC Sedan / SUV for all transfers & premium sightseeing routes.', 3),
            _inc_included('Private speedboat charter tickets to Paradise Beach.', 4),
            _inc_included('Complimentary pre-arranged entry passes for Auroville Matrimandir area.', 5),
            _inc_included('Full operational guidance and continuous TRAGUIN Support.', 6),
            _inc_excluded('Domestic or international flight / rail tickets to Chennai.', 7),
            _inc_excluded('Monument camera entry fees or optional local guide gratuities.', 8),
            _inc_excluded('Personal laundry, telephone billing, or premium alcoholic beverages.', 9),
            _inc_excluded('Optional water adventure activities (scuba or mangrove kayaking).', 10),
        ],
    )
    return package, itinerary

def build_py_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'PY-004'
    tour_code = 'TG-PY-LUX-004'
    title = 'Premium Puducherry Tour Package'
    duration = '05 Nights / 06 Days'
    slug = 'py-004-premium-puducherry-tour-package'
    itin_slug = 'py-004-premium-puducherry-tour-package-itinerary'
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
            _ph('State / Country: Puducherry, India | Category: Luxury Island & Coastal Escape', 2),
            _ph('Destinations: French Quarter • Auroville • Paradise Beach • White Town', 3),
            _ph('Ideal for: Couples, Honeymooners, Luxury Travelers, Families', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle: Premium Air-Conditioned Luxury Sedan / Executive SUV (Private Chauffeur)', 7),
            _ph('Meal Plan: Bespoke Continental & Coastal Gourmet Breakfasts & Dinners (MAPAI Plan)', 8),
            _ph('Route Map: Chennai International Airport Arrival → Puducherry French Quarter → Auroville → Chennai Departure', 9),
            _ph('TRAGUIN Signature Experience: Private French baking class conducted by an expert local pastry chef, teaching the art of crafting perfect buttery croissants.', 10),
            _ph('Curated by TRAGUIN Experts: Hand-vetted culinary itineraries matching true European standards for hygiene, atmosphere, and authentic flavor profiles.', 11),
            _ph('Shopping & Local Experiences: Local Markets: Famous for premium handmade paper at Sri Aurobindo Paper Factory, ceramic tableware in Auroville, and aromatic hand-poured candles. Top Instagram Spots: Mustard-colored colonial walls along Rue Romain Rolland and bougainvillea canopies on Suffren Street.', 12),
            _ph('Important Notes: Advance Booking Suggestion: Heritage hotels in White Town possess limited inventory and require booking 60-90 days ahead for peak season travel. Auroville Access Notice: The inner meditation chamber access requires independent in-person booking guidelines managed strictly by the township council. Transport Note: Motorized traffic inside select historic lanes of White Town remains restricted during evening hours to maintain a pleasant pedestrian environment.', 13),
        ],
        moods=['Luxury', 'Coastal', 'Heritage'],
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
        tagline='Premium Puducherry Tour Package • 05 Nights / 06 Days',
        overview=(
            'Welcome to the French Riviera of the East. This meticulously fashioned Luxury Puducherry Holiday curated elegantly by TRAGUIN is expertly tailored for travelers seeking a perfect blend of colonial nostalgia, coastal chic, and bohemian luxury. Wander amidst the pastel-hued lanes of White Town, witness the breathtaking landscapes of secluded beaches, and treasure unforgettable memories within our selected premium stays and handpicked hotels that offer timeless boutique sophistication.\n\nTOUR OVERVIEW\nVehicle Type: Premium Air-Conditioned Luxury Sedan / Executive SUV (Private Chauffeur)\nMeal Plan: Bespoke Continental & Coastal Gourmet Breakfasts & Dinners (MAPAI Plan)\nRoute Plan: Chennai International Airport Arrival → Puducherry French Quarter → Auroville → Chennai Departure\n\nCurated Experience:\nThis premium TRAGUIN Puducherry Package includes a private French Quarter heritage architecture specialist guide, pre-booked VIP passes for the Matrimandir viewing point, and an exclusive yacht lunch cruise.\n\nPuducherry stands out as a unique coastal jewel, making it a heavily searched choice for a Best Puducherry Tour Package or a romantic Puducherry Honeymoon Package. Combining vibrant Tamil culture with historical French heritage, it presents an unparalleled sanctuary for travelers seeking a highly sophisticated Premium Puducherry Experience.\nWhite Town (French Quarter): Famous for its mustard-colored colonial mansions, bougainvillea-laden gates, and charming European cafes, acting as a prominent Instagram location.\nAuroville: An experimental universal township centered around the golden Matrimandir dome, offering immersive experiences in spiritual meditation and sustainable architecture.\nParadise Beach: An isolated spit of pristine white sand accessible via private boat ride, renowned for its coastal scenic beauty.\nBest Time to Visit Puducherry: The soothing coastal winter breeze between October and March provides the absolute best weather conditions for extensive Puducherry Sightseeing.'
        ),
        seo_title='PY-004 | Premium Puducherry Tour Package | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Puducherry luxury package (PY-004 / TG-PY-LUX-004): French Quarter, Auroville, Paradise Beach, White Town, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('East Coast Road coastal drive, Rock Beach Promenade, and French War Memorial', 1),
            _ih('White Town Colonial Heritage Loop, Sri Aurobindo Ashram, and Botanical Gardens', 2),
            _ih('Auroville International Township, Matrimandir Viewing Point, and Paradise Beach excursion', 3),
            _ih('Tamil Heritage Quarter, Cluny Embroidery Center, and private Franco-Tamil fusion farewell dinner', 4),
            _ih('TRAGUIN Signature Experience: Private French baking class with expert local pastry chef', 5),
        ],
        days=[
            _day(
                1,
                'Chennai to Puducherry – The Scenic East Coast Road Odyssey',
                (
                    'Your luxury vacation starts with a direct greeting by your private TRAGUIN chauffeur at Chennai Airport. Embark on a breathtaking drive along the scenic East Coast Road (ECR), catching pristine glimpses of the Bay of Bengal along the route. Arrive in Puducherry and check into your handpicked heritage boutique hotel tucked away in the French Quarter. In the evening, take an easy stroll along the Promenade Beach, feeling the coastal wind and seeing the iconic statue of Mahatma Gandhi.'
                ),
                [
                    'Sightseeing Included: ECR Coastal Drive, Rock Beach Promenade, French War Memorial',
                    'Welcome Amenities: Complimentary bottle of vintage non-alcoholic cider and house-baked French macarons in-suite.',
                    'Overnight Stay: White Town, Puducherry (Premium Heritage Hotel Luxury Suite)',
                    'Meals Included: Gourmet Welcome Dinner',
                ],
            ),
            _day(
                2,
                'Colonial Heritage Architecture Tour & French Bake Trails',
                (
                    'Indulge in a fresh breakfast on a sunny courtyard patio. Meet your private architecture specialist guide for an elite Puducherry Sightseeing walk down the cobblestone grid of White Town. Admire the perfectly restored 18th-century mansions, stately arched entries, and the beautiful Notre Dame des Anges church. In the afternoon, explore the spiritual quarters of the Sri Aurobindo Ashram, soaking in its quiet and profoundly meditative gardens.'
                ),
                [
                    'Sightseeing Included: White Town Colonial Heritage Loop, Sri Aurobindo Ashram, Botanical Gardens',
                    'Exclusive Experiences: Private curated tasting trail checking out iconic French bakeries and artisanal chocolate workshops.',
                    'Overnight Stay: White Town, Puducherry',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'Auroville Expedition – Spiritual Discovery & Matrimandir Viewing',
                (
                    'Following a refreshing gourmet breakfast, drive towards the universal township of Auroville. Journey along shaded red-earth paths to the inner viewing area of the majestic Matrimandir, a massive golden globe symbolizing human unity. Learn about the unique communal design philosophy from an insider specialist. Spend your afternoon browsing boutique stores featuring organic apparel, handcrafted terracotta, and natural essential oils made inside the township.'
                ),
                [
                    'Sightseeing Included: Auroville International Township, Matrimandir Viewing Point, Auroville Beach',
                    'Food Suggestion: Wood-fired organic sourdough pizza and fresh kombucha at a popular Auroville forest cafe.',
                    'Overnight Stay: White Town, Puducherry',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'Escape to Paradise Beach & Private Lagoon Cruise',
                (
                    'Awake to a blissful coastal morning. Today, travel down to Chunnambar boat house where you step aboard a private speed charter boat down the tranquil backwater stream to the secluded Paradise Beach. Spend your morning wandering along the white sands or relaxing inside private shaded gazebos. In the late afternoon, enjoy an exclusive private catamaran cruise across the lagoon, taking in gorgeous sunset colors.'
                ),
                [
                    'Sightseeing Included: Chunnambar Backwaters, Paradise Beach Excursion',
                    'Photography Points: Golden hour silhouettes against the isolated sandbanks of Paradise Beach.',
                    'Overnight Stay: White Town, Puducherry',
                    'Meals Included: Breakfast & Seafood Specialty Dinner',
                ],
            ),
            _day(
                5,
                'Tamil Vintage Tour Across Cul de Sacs & Cafe Hopping',
                (
                    "Enjoy your artisan breakfast. Today, delve into the colorful Heritage Tamil Quarter, exploring the distinct 'Thinai' architectural verandahs that contrast with the French side. Visit the historical Cluny Embroidery Center housed inside a 1780 mansion where underprivileged women craft stunning textile designs. Spend a relaxed afternoon exploring modern art galleries and chic street cafes inside the city's hidden lanes."
                ),
                [
                    'Sightseeing Included: Tamil Heritage Quarter, Cluny Embroidery Center, Goubert Market',
                    'Evening Experience: A special, private five-course Franco-Tamil fusion farewell dinner organized exclusively for you.',
                    'Overnight Stay: White Town, Puducherry (Premium Luxury Stay)',
                    'Meals Included: Breakfast & Specialty Farewell Dinner',
                ],
            ),
            _day(
                6,
                'Farewell Puducherry – Drive Back to Chennai with Timeless Memories',
                (
                    'Relish a peaceful morning breakfast. Take care of any last-minute shopping for French antiques, hand-poured candles, or organic linens. Your private chauffeur will then transfer you comfortably along the ECR back to Chennai International Airport. Your memorable Puducherry Family Tour and premium beach vacation concludes, leaving you with beautifully curated experiences and timeless stories from TRAGUIN.'
                ),
                [
                    'Meals Included: Breakfast',
                    'Assistance: Airport executive baggage handling and trolley assistance upon arrival at the terminal gates.',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Atithi / Ocean Spray Residency',
                'Puducherry',
                '05 Nights',
                'Deluxe',
                'Standard Comfort Room',
                'MAPAI Plan',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Atithi / Ocean Spray Residency (Standard Comfort Room)',
            ),
            _hotel(
                'Maison Perumal - CGH Earth / Gratitude Heritage',
                'Puducherry',
                '05 Nights',
                'Premium',
                'Premium Heritage Room',
                'MAPAI Plan',
                4,
                2,
                description='OPTION 02 – PREMIUM: Maison Perumal - CGH Earth / Gratitude Heritage (Premium Heritage Room)',
            ),
            _hotel(
                'La Villa Puducherry / Le Dupleix Heritage Property',
                'Puducherry',
                '05 Nights',
                'Luxury',
                'Executive Comfort Room',
                'MAPAI Plan',
                5,
                3,
                description='OPTION 03 – LUXURY: La Villa Puducherry / Le Dupleix Heritage Property (Executive Comfort Room)',
            ),
            _hotel(
                'Palais de Mahé - CGH Earth / Villa Shanti',
                'Puducherry',
                '05 Nights',
                'Ultra Luxury',
                'Luxury Deluxe Suite',
                'MAPAI Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Palais de Mahé - CGH Earth / Villa Shanti (Luxury Deluxe Suite)',
            ),
        ],
        inclusions=[
            _inc_included('Boutique luxury heritage stays directly inside the historic White Town.', 1),
            _inc_included('Daily gourmet breakfasts and fine-dining multi-course dinners.', 2),
            _inc_included('Private luxury AC Sedan for all transfers, ECR highway runs, and touring.', 3),
            _inc_included('Private heritage architecture specialist guide for White Town walks.', 4),
            _inc_included('Private speedboat charter tickets to Paradise Beach.', 5),
            _inc_included('Pre-arranged priority entry passes for Auroville Matrimandir viewing.', 6),
            _inc_included('Continuous personalized 24/7 guest service and TRAGUIN Support.', 7),
            _inc_excluded('Airfare or national train tickets to/from Chennai hubs.', 8),
            _inc_excluded('Monument camera fees or optional water sport rentals.', 9),
            _inc_excluded('Personal boutique shopping, laundry expenses, or alcoholic refreshments.', 10),
            _inc_excluded('Any premium medical or holiday travel insurance policies.', 11),
        ],
    )
    return package, itinerary

def build_py_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'PY-005'
    tour_code = 'TG-PY-LEI-005'
    title = 'Premium Puducherry Leisure Tour Package'
    duration = '04 Nights / 05 Days'
    slug = 'py-005-premium-puducherry-leisure-tour-package'
    itin_slug = 'py-005-premium-puducherry-leisure-tour-package-itinerary'
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
            _ph('State / Country: Puducherry, India | Category: Senior Citizen Leisure Tour', 2),
            _ph('Destinations: Puducherry (French Quarter) • Auroville • Paradise Beach', 3),
            _ph('Ideal for: Senior Citizens, Couples, Families, Slow Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle: Premium Air-Conditioned Toyota Innova (Senior-Friendly, Smooth Ride)', 7),
            _ph('Meal Plan: Breakfast & Curated Mild Dinners (Customized Comfort Dining)', 8),
            _ph('Route Map: Chennai International Airport Arrival → Puducherry Coastal Drive → White Town Exploration → Auroville → Chennai Departure', 9),
            _ph("TRAGUIN Signature Experience: Specialized slow-paced routing custom-tailored around senior travelers' maximum comfort and zero physical fatigue.", 10),
            _ph('Curated by Experts: Handpicked restaurants serving exceptionally fresh, high-quality, non-spicy, healthy meal options.', 11),
            _ph('Shopping & Local Experiences: Local Markets & Boutiques: Famous for purchasing organic essential oils, handcrafted clay pottery, and fine linen clothing. Instagram Spots: The sweeping palm-lined view at Promenade Beach and the quaint pastel streets of White Town.', 12),
            _ph('Important Notes: Advance Booking Suggestion: Highly recommended to secure bookings 45–60 days in advance during winter peak months. Weather Note: Light cotton clothes are ideal year-round, along with comfortable flat walking shoes. Wheelchair assistance can be pre-arranged at all heritage sites upon giving 24-hour notice to our team.', 13),
        ],
        moods=['Leisure', 'Senior', 'Relaxed'],
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
        tagline='Premium Puducherry Leisure Tour Package • 04 Nights / 05 Days',
        overview=(
            'Welcome to the French Riviera of the East. Our thoughtfully designed Leisure Puducherry Family Tour by TRAGUIN is expertly crafted for senior citizens, featuring effortless transitions, leisurely pacing, and premium stays. Walk along tree-lined boulevards, behold colonial French architecture, and collect unforgettable memories at an incredibly relaxed pace. Enjoy our handpicked hotels that offer top-tier comfort, easy accessibility, and warm hospitality.\n\nTOUR OVERVIEW\nVehicle Type: Premium Air-Conditioned Toyota Innova (Senior-Friendly, Smooth Ride)\nMeal Plan: Breakfast & Curated Mild Dinners (Customized Comfort Dining)\nRoute Plan: Chennai International Airport Arrival → Puducherry Coastal Drive → White Town Exploration → Auroville → Chennai Departure\n\nCurated Note:\nThis premium holiday package features complete ground support, ground-floor/elevator-accessible rooms, minimal walking barriers, and private vehicle setups for complete peace of mind.\n\nPuducherry is a beautiful coastal enclave, highly searched as a choice for a Best Puducherry Tour Package or a relaxing Puducherry Family Tour. Combining seaside serenity with a quaint Indo-French lifestyle, it offers wonderful spots for an offbeat Luxury Puducherry Holiday.\nWhite Town (French Quarter): Known for pastel-yellow colonial villas, boutique cafes, and cobblestone pathways—the ultimate popular Instagram locations for portrait memories.\nAuroville Matrimandir: A stunning golden metallic sphere representing unity and peace, offering immersive experiences in tranquility and meditation.\nPromenade Beach: A magnificent beachfront boulevard completely closed to vehicular traffic in the evening, ensuring senior citizens can enjoy a peaceful sunset stroll.\nBest Time to Visit Puducherry: The cool, pleasant winter months from October to March present an optimal climate for comfortable Puducherry Sightseeing.'
        ),
        seo_title='PY-005 | Premium Puducherry Leisure Tour Package | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Puducherry leisure package (PY-005 / TG-PY-LEI-005): French Quarter, Auroville, Paradise Beach, and 4-tier senior-friendly accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Scenic East Coast Road drive and leisurely White Town colonial sightseeing', 1),
            _ih('Auroville International Township, Matrimandir Viewpoint, and eco-shuttle golf cart access', 2),
            _ih('Chunnambar Backwater Ferry and Paradise Beach sandbanks with covered luxury ferry', 3),
            _ih("TRAGUIN Signature Experience: Slow-paced routing for senior travelers' maximum comfort", 4),
            _ih('Premium senior-friendly accommodation with elevator-equipped heritage properties', 5),
        ],
        days=[
            _day(
                1,
                'Arrival in Chennai – Scenic East Coast Road Drive to Puducherry',
                (
                    'Arrive at Chennai International Airport, where a dedicated TRAGUIN representative welcomes you and handles your baggage. Board your premium private vehicle for a smooth, scenic drive along the East Coast Road (ECR). Enjoy mesmerizing glimpses of the Bay of Bengal on one side and lush salt pans on the other. Upon arrival in Puducherry, check into your handpicked luxury hotel in the heart of White Town and relax for the evening.'
                ),
                [
                    'Sightseeing Included: Scenic Coastal Road Drive, Leisure Hotel Check-in',
                    'Welcome Amenities: Complimentary cooling herbal tea, traditional stoles, and fresh local flowers upon arrival.',
                    'Overnight Stay: Puducherry (Premium Luxury Heritage Boutique Hotel)',
                    'Meals Included: Dinner',
                ],
            ),
            _day(
                2,
                'White Town Walking Trail & Colonial Indo-French Sightseeing',
                (
                    'Savor a relaxed morning breakfast. Today, your Puducherry Sightseeing journey begins with a beautifully organized, slow-paced exploration of the French Quarter. Travel comfortably via an open-air luxury rickshaw cart or a slow vehicle to admire the iconic attractions, including the Notre Dame des Anges Church and the French War Memorial. In the evening, relax at the paved Promenade Beach boulevard right by the sea.'
                ),
                [
                    'Sightseeing Included: White Town Heritage Buildings, Sri Aurobindo Ashram, Promenade Beach Boulevard',
                    'Photography Points: Vibrant bougainvillea-draped yellow walls of French heritage mansions.',
                    'Overnight Stay: Puducherry',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'Auroville Community & Spiritual Matrimandir Excursion',
                (
                    'Following a refreshing premium breakfast, take a comfortable short drive to Auroville, the international township of peace. Ride a battery-operated eco-shuttle through shaded forest pathways directly to the Matrimandir Viewing Point. Behold the magnificent golden sphere reflecting breathtaking landscapes under the morning sun. Spend a relaxed afternoon exploring sustainable handicraft boutiques and organic cafes.'
                ),
                [
                    'Sightseeing Included: Auroville International Township, Matrimandir Viewpoint, Auroville Visitor Center',
                    'Food Suggestion: Freshly baked local pastries and authentic French-pressed premium coffee.',
                    'Overnight Stay: Puducherry',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'Chunnambar Lagoon Cruise & Paradise Beach Escape',
                (
                    'Indulge in a delicious breakfast. Today, take a brief drive to Chunnambar boat house. Board a safely managed, private covered luxury ferry boat for a gentle cruise down the backwaters to the pristine sandbanks of Paradise Beach. Spend your afternoon relaxing under cozy thatched shacks, listening to the soft waves. Return to your premium stay in the afternoon with plenty of open time for personal relaxation.'
                ),
                [
                    'Sightseeing Included: Chunnambar Backwater Ferry, Paradise Beach Sandbanks',
                    'Evening Experience: A special curated, peaceful dinner inside a converted French colonial villa courtyard.',
                    'Overnight Stay: Puducherry',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'Local Market Souvenirs & Drive Back to Chennai Departure',
                (
                    'Enjoy your final breakfast at the hotel. Spend an hour shopping for premium handmade items, aromatic incense sticks, and fine linens. Your private chauffeur will then drive you comfortably back via ECR to Chennai International Airport. Your memorable Premium Puducherry Experience concludes here, leaving you with beautifully curated experiences and unforgettable memories arranged by TRAGUIN.'
                ),
                [
                    'Meals Included: Breakfast',
                    'Assistance: Complete airport gate porter service and baggage check-in support.',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Atithi / Ocean Spray Residency',
                'Puducherry',
                '04 Nights',
                'Deluxe',
                'Standard Comfort Room',
                'Breakfast & Mild Dinners',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Atithi / Ocean Spray Residency (Standard Comfort Room)',
            ),
            _hotel(
                'Maison Perumal - CGH Earth / Atithi TGI Grand',
                'Puducherry',
                '04 Nights',
                'Premium',
                'Luxury Suite, Elevator Equipped',
                'Breakfast & Mild Dinners',
                4,
                2,
                description='OPTION 02 – PREMIUM: Maison Perumal - CGH Earth / Atithi TGI Grand (Luxury Suite, Elevator Equipped)',
            ),
            _hotel(
                'Maison Perumal - CGH Earth / Atithi TGI Grand',
                'Puducherry',
                '04 Nights',
                'Luxury',
                'Luxury Suite, Elevator Equipped',
                'Breakfast & Mild Dinners',
                5,
                3,
                description='OPTION 03 – PREMIUM: Maison Perumal - CGH Earth / Atithi TGI Grand (Luxury Suite, Elevator Equipped)',
            ),
            _hotel(
                'Palais de Mahé - CGH Earth / The Promenade Premium',
                'Puducherry',
                '04 Nights',
                'Ultra Luxury',
                'Executive Rooms',
                'Breakfast & Mild Dinners',
                5,
                4,
                description='OPTION 04 – LUXURY (Highly Recommended): Palais de Mahé - CGH Earth / The Promenade Premium (Executive Rooms)',
            ),
        ],
        inclusions=[
            _inc_included('Handpicked hotel stays featuring senior-friendly easy access.', 1),
            _inc_included('Daily premium breakfasts and multi-course comforting dinners.', 2),
            _inc_included('Private luxury AC Toyota Innova for all transfers & touring tracks.', 3),
            _inc_included('Complimentary eco-shuttle golf cart tickets inside Auroville.', 4),
            _inc_included('Private covered ferry boat cruise to Paradise Beach.', 5),
            _inc_included('Dedicated 24/7 localized phone and ground TRAGUIN Support.', 6),
            _inc_included('All applicable luxury state taxes, driver tolls, and parking fees.', 7),
            _inc_excluded('Airfare or national train tickets to/from Chennai.', 8),
            _inc_excluded('Camera entry charges or optional local guide fee tips.', 9),
            _inc_excluded('Personal laundry expenditures, telephone billing, or alcohol.', 10),
            _inc_excluded('Any travel or medical insurance coverage plans.', 11),
        ],
    )
    return package, itinerary

def build_py_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'PY-006'
    tour_code = 'TG-PY-GIRLS-006'
    title = 'Premium Puducherry Lifestyle Escape'
    duration = '04 Nights / 05 Days'
    slug = 'py-006-premium-puducherry-lifestyle-escape'
    itin_slug = 'py-006-premium-puducherry-lifestyle-escape-itinerary'
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
            _ph('State / Country: Puducherry (Pondicherry), India | Category: Exclusive Female-Only Girls Trip Retreat', 2),
            _ph('Destinations: White Town • Auroville • Paradise Beach • Serenity Beach', 3),
            _ph('Ideal for: Girlfriends, Solo Female Groups, Luxury Chasers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle: Premium Air-Conditioned Multi-Utility Luxury Car (Dedicated Professional Chauffeur)', 7),
            _ph('Meal Plan: Breakfast & Curated Coastal Bistro Dinners (MAPAI Lifestyle Plan)', 8),
            _ph('Route Map: Chennai International Airport → White Town Puducherry → Auroville → Paradise Coast → Chennai Departure', 9),
            _ph('TRAGUIN Signature Experience: Private local shopping and styling expert to guide you through hidden linen, clay, and leather ateliers.', 10),
            _ph('Curated by TRAGUIN Experts: Strict destination safety screening and elite vehicle allocations ensuring peace of mind for female travel groups.', 11),
            _ph('Shopping & Local Experiences: Local Markets & Ateliers: Famous for Kalki boutique shopping (perfumes, silk clothing), Auroshikha incense, leather accessories on Mission Street, and local handmade paper. Top Instagram Spots: The pastel pink facade of Cluny Embroidery Centre, the seaside rocks of Promenade Beach, and the quaint cafes along Rue Dumas.', 12),
            _ph('Important Notes: Café Reservations: Famous bistros inside White Town get crowded during weekends; dinner reservations are handled in advance by your travel advisor. Attire Courtesy: Modest clothing covering shoulders and knees is recommended inside Sri Aurobindo Ashram and the core inner zones of Auroville. Advance Booking Suggestion: Heritage villas have limited inventory; booking 45 days ahead ensures choice accommodations.', 13),
        ],
        moods=['Girls Trip', 'Lifestyle', 'Luxury'],
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
        tagline='Premium Puducherry Lifestyle Escape • 04 Nights / 05 Days',
        overview=(
            "Escape into a pastel-tinted world where bohemian French heritage marries coastal chic relaxation. This premium female-only Luxury Puducherry Holiday crafted seamlessly by TRAGUIN is expertly designed for discerning women looking for top-tier security, artistic independence, and immersive lifestyle experiences. Wander along sun-drenched colonial boulevards, stay at iconic premium stays and handpicked hotels, and frame unforgettable memories with your favorite circle against breathtaking landscapes.\n\nTOUR OVERVIEW\nVehicle Type: Premium Air-Conditioned Multi-Utility Luxury Car (Dedicated Professional Chauffeur)\nMeal Plan: Breakfast & Curated Coastal Bistro Dinners (MAPAI Lifestyle Plan)\nRoute Plan: Chennai International Airport → White Town Puducherry → Auroville → Paradise Coast → Chennai Departure\n\nCurated Note:\nThis exclusive TRAGUIN Puducherry Package features comprehensive female-centric safety verification protocols, pre-booked café lounge slots, and a specialized local shopping escort for high-end boutique explorations.\n\nPuducherry continues to reign as India's ultimate chic coastal enclave, serving as a highly targeted pick for a Best Puducherry Tour Package or an elegant Puducherry Honeymoon Package / Family Tour. Famed for its mustard-yellow French facades and azure shorelines, it promises unrivaled culinary journeys and artsy retreats.\n**White Town (French Quarter):** A dreamscape of bougainvillea draped over pastel walls—widely celebrated as a popular Instagram location for high-fashion photoshoots.\n**Auroville Matrimandir:** A marvelous soul sanctuary symbolizing global peace, perfect for deep mindfulness and quiet internal connection.\n**Most Searched Experiences:** Indulging in freshly baked artisanal croissants at traditional French bakeries, pottery crafting, and ocean sunrise strolls.\n**Best Time to Visit Puducherry:** The pleasant tropical winter breeze between October and March offers a magical climate for active Puducherry Sightseeing."
        ),
        seo_title='PY-006 | Premium Puducherry Lifestyle Escape | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Puducherry girls trip package (PY-006 / TG-PY-GIRLS-006): White Town, Auroville, Paradise Beach, Serenity Beach, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('East Coast Road coastal route, Promenade Beach Waterfront, and welcome high-tea in White Town', 1),
            _ih('French Quarter architectural trails, organic candle-making or pottery experience at local design studio', 2),
            _ih('Auroville Matrimandir Point, boutique café crawl, and yacht excursion to Paradise Beach', 3),
            _ih('TRAGUIN Signature Experience: Private local shopping and styling expert for hidden ateliers', 4),
            _ih('Premium female-travel security protocols and 24/7 on-call TRAGUIN Support', 5),
        ],
        days=[
            _day(
                1,
                'Coastal Arrival & Welcome High-Tea in White Town',
                (
                    'Arrive at Chennai Airport where a private luxury premium vehicle from TRAGUIN awaits you. Enjoy a scenic, refreshing drive along the famous East Coast Road (ECR) with beautiful ocean views. Arrive in Puducherry and check into your handpicked heritage luxury boutique hotel nestled deep inside the historic French Quarter. Unwind with an exclusive welcome high-tea served in a private colonial courtyard, before taking a relaxed evening stroll along the iconic Promenade Beach.'
                ),
                [
                    'Sightseeing Included: ECR Coastal Route, Promenade Beach Waterfront, French War Memorial',
                    'Evening Experience: A premium high-tea featuring artisanal French pastries, macaroons, and organic local fruit infusions.',
                    'Overnight Stay: White Town Puducherry (Handpicked Elite Luxury Boutique Hotel)',
                    'Meals Included: Welcome High-Tea & Dinner',
                ],
            ),
            _day(
                2,
                'Architectural White Town Detours & Aesthetic Instagram Trails',
                (
                    'Awake to a pleasant morning breeze and relish an exquisite gourmet breakfast. Today, enjoy a highly curated walking architectural trail through the vibrant French Quarter. Wander past iconic pastel structures, historic archways, and boutique design houses. In the afternoon, discover the elegant Notre Dame des Anges Church and the old spiritual sanctuary of Sri Aurobindo Ashram. Cap off the day with a fun, hands-on organic candle-making or pottery experience at a local design studio.'
                ),
                [
                    'Sightseeing Included: French Quarter Lanes, Sri Aurobindo Ashram, Goubert Avenue Waterfront',
                    'Photography Points: Bougainvillea-laden mustard gateways on Rue Romain Rolland.',
                    'Overnight Stay: White Town Puducherry',
                    'Meals Included: Breakfast & Gourmet Bistro Dinner',
                ],
            ),
            _day(
                3,
                'Soul Essence at Auroville & Bohemian Cafe Crawls',
                (
                    "Enjoy a wholesome organic breakfast before driving out to the international township of Auroville. Take a scenic, shaded forest walk to the majestic Matrimandir viewing point, marveling at the giant golden sphere. Spend your afternoon enjoying a boutique café crawl through Auroville's hidden eateries, sampling fine wood-fired pizzas and vegan culinary treats. Browse the local markets for sustainably made garments and natural aromatherapy oils."
                ),
                [
                    'Sightseeing Included: Auroville Matrimandir Point, Auroville Beach, Sustainable Craft Centers',
                    'Food Suggestion: Fresh sourdough treats, kombuchas, and locally harvested single-origin cold brews.',
                    'Overnight Stay: White Town Puducherry',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'Yacht Excursion to Paradise Beach & Sunset Cocktails',
                (
                    'Savor a lazy tropical breakfast at your villa. Head to Chunnambar boat house to board a private luxury speedboat or yacht charter to the secluded shores of Paradise Beach. Spend your morning relaxing on soft white sands, enjoying private beach lounge chairs, or taking a dip in the gentle ocean waters. Return to the city for a pre-booked premium rooftop dining experience, sharing unforgettable memories as you toast to your friendship.'
                ),
                [
                    'Sightseeing Included: Chunnambar Backwaters, Paradise Beach Private Cruise',
                    'Exclusive Experience: Private beach picnic canopy setup with premium cold-pressed juices and fresh finger foods.',
                    'Overnight Stay: White Town Puducherry',
                    'Meals Included: Breakfast & Farewell Rooftop Dinner',
                ],
            ),
            _day(
                5,
                'Souvenir Collecting & Departure with Unforgettable Stories',
                (
                    "Indulge in a final delicious breakfast at your hotel's terrace. Spend your morning checking out local fashion boutiques for unique apparel, handmade paper notebooks, and signature French-style home décor pieces. Your private premium vehicle will pick you up for a smooth transfer back to Chennai International Airport. Your fabulous Puducherry Girls Trip concludes here, leaving your group with beautiful blessings, closer bonds, and memories crafted exclusively by TRAGUIN."
                ),
                [
                    'Meals Included: Breakfast',
                    'Assistance: Airport gate check-in assistance and baggage handling support by your dedicated chauffeur.',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Atithi / Ocean Spray Residency',
                'Puducherry',
                '04 Nights',
                'Deluxe',
                'Standard Comfort Room',
                'MAPAI Lifestyle Plan',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Atithi / Ocean Spray Residency (Standard Comfort Room)',
            ),
            _hotel(
                'Maison Perumal - CGH Earth / Gratitude Heritage',
                'Puducherry',
                '04 Nights',
                'Premium',
                'Premium Heritage Room',
                'MAPAI Lifestyle Plan',
                4,
                2,
                description='OPTION 02 – PREMIUM: Maison Perumal - CGH Earth / Gratitude Heritage (Premium Heritage Room)',
            ),
            _hotel(
                'La Villa Puducherry / Le Dupleix Heritage Property',
                'Puducherry',
                '04 Nights',
                'Luxury',
                'Executive Club Rooms',
                'MAPAI Lifestyle Plan',
                5,
                3,
                description='OPTION 03 – LUXURY: La Villa Puducherry / Le Dupleix Heritage Property (Executive Club Rooms)',
            ),
            _hotel(
                'Palais de Mahe - CGH Earth / Villa Shanti White Town',
                'Puducherry',
                '04 Nights',
                'Ultra Luxury',
                'Luxury Suite Resort',
                'MAPAI Lifestyle Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Palais de Mahe - CGH Earth / Villa Shanti White Town (Luxury Suite Resort)',
            ),
        ],
        inclusions=[
            _inc_included('Premium luxury heritage suite accommodations in White Town.', 1),
            _inc_included('Daily breakfasts and multi-course curated café-style dinners.', 2),
            _inc_included('Private luxury AC vehicle for all transfers, routes, and touring.', 3),
            _inc_included('Exclusive welcome high-tea reception in a heritage courtyard.', 4),
            _inc_included('Private speedboat/yacht charter tickets to Paradise Beach.', 5),
            _inc_included('Complimentary entry passes for Auroville Matrimandir access zones.', 6),
            _inc_included('Dedicated 24/7 on-call female-travel security and TRAGUIN Support.', 7),
            _inc_excluded('Airfare or national train booking tickets to Chennai.', 8),
            _inc_excluded('Personal boutique café lunch expenditures or alcoholic drinks.', 9),
            _inc_excluded('Monument camera entry slips or specialized activity fees.', 10),
            _inc_excluded('Any individual travel insurance or medical coverage plans.', 11),
        ],
    )
    return package, itinerary

def build_py_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'PY-007'
    tour_code = 'TG-PY-FAM-007'
    title = 'Premium Puducherry French Heritage Tour'
    duration = '04 Nights / 05 Days'
    slug = 'py-007-premium-puducherry-french-heritage-tour'
    itin_slug = 'py-007-premium-puducherry-french-heritage-tour-itinerary'
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
            _ph('State / Country: Puducherry, India | Category: French Heritage Family Tour', 2),
            _ph('Destinations: White Town • Auroville • Paradise Beach • Arikamedu', 3),
            _ph('Ideal for: Families, Heritage Enthusiasts, Relaxation Seekers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle: Premium Air-Conditioned Multi-Purpose Vehicle (Private Private Chauffeur)', 7),
            _ph('Meal Plan: Breakfast & Curated French-Tamil Fusion Gourmet Dinners (MAPAI Plan)', 8),
            _ph('Route Map: Chennai International Airport → Puducherry White Town → Auroville → Paradise Beach → Chennai Departure', 9),
            _ph('TRAGUIN Signature Experience: Private expert-guided culinary food walk exploring hidden French cafes and traditional Creole cooking styles.', 10),
            _ph('Curated by Experts: Selective restaurant pairings ensuring premium hygiene parameters and child-friendly meal menus.', 11),
            _ph("Shopping & Local Experiences: Local Boutiques: Cluny Embroidery Center (run by nuns for exquisite linen), Goubert Market for organic spices, and Auroville boutiques for hand-crafted pottery. Cafes & Bakeries: Café des Arts, Baker's Street, and Coromandel Cafe for incredible French culinary treats.", 12),
            _ph('Important Notes: Advance Booking Suggestion: Heritage properties in White Town have limited room configurations and should be secured 60 days ahead for family peak seasonal travels. Auroville Matrimandir Guidelines: Access inside the inner concentration chamber requires separate personal prior reservations which are subject to availability. Dress Code: Light cotton attire is recommended throughout the year; respectful dress covers are required when stepping inside the Ashram premises.', 13),
        ],
        moods=['Heritage', 'Family', 'Culture'],
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
        tagline='Premium Puducherry French Heritage Tour • 04 Nights / 05 Days',
        overview=(
            'Welcome to the French Riviera of the East. This meticulously structured Puducherry Family Tour engineered by TRAGUIN masterfully marries European colonial elegance with serene coastal tranquility. Explore the charming pastel-shaded streets of White Town, step into the utopian peace of Auroville, and enjoy premium stays in beautifully restored boutique properties. Our exclusive experiences ensure your family creates unforgettable memories amidst breathtaking landscapes and deep cultural stories.\n\nTOUR OVERVIEW\nVehicle Type: Premium Air-Conditioned Multi-Purpose Vehicle (Private Private Chauffeur)\nMeal Plan: Breakfast & Curated French-Tamil Fusion Gourmet Dinners (MAPAI Plan)\nRoute Plan: Chennai International Airport → Puducherry White Town → Auroville → Paradise Beach → Chennai Departure\n\nCurated Note:\nThis premium TRAGUIN Puducherry Package boasts priority access tokens for the Auroville Matrimandir viewing point, handpicked child-friendly boutique accommodations, and curated walking maps for the French Quarter.\n\nPuducherry stands out as an unmatched coastal retreat in southern India, offering the ideal ambiance for a Best Puducherry Tour Package or a relaxed Puducherry Family Tour. Famous for its mustard-yellow architecture, cobblestone avenues, and tranquil shores, it promises a rich Premium Puducherry Experience for all generations.\n**White Town (French Quarter):** A beautifully preserved historical grid featuring French colonial villas, trailing bougainvillea, and chic bakeries—the ultimate popular Instagram location.\n**Auroville Matrimandir:** The spectacular golden globe symbolizing human unity, offering deep immersive experiences and quiet introspective paths.\n**Top Tourist Places in Puducherry:** Includes Sri Aurobindo Ashram, Promenade Beach, Sacred Heart Basilica, and Chunnambar Boathouse.\n**Best Time to Visit Puducherry:** The refreshing tropical winter window from October to March is perfect for experiencing comprehensive, relaxed Puducherry Sightseeing.'
        ),
        seo_title='PY-007 | Premium Puducherry French Heritage Tour | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Puducherry French heritage package (PY-007 / TG-PY-FAM-007): White Town, Auroville, Paradise Beach, Arikamedu, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('East Coast Road scenic route, Promenade Beach, and French War Memorial sunset', 1),
            _ih('French Quarter and Tamil Quarter architectural walk, Sri Aurobindo Ashram, and Sacred Heart Basilica', 2),
            _ih('Auroville International Township, Matrimandir Viewpoint, and Auroville Visitors Centre', 3),
            _ih('Paradise Beach speedboat cruise and Arikamedu Archaeological Site heritage excursion', 4),
            _ih('TRAGUIN Signature Experience: Private expert-guided culinary food walk through hidden French cafes', 5),
        ],
        days=[
            _day(
                1,
                'Cozy Road Trip to Puducherry & Promenade Beach Sunset',
                (
                    'Your family vacation kicks off with a scenic drive along the gorgeous East Coast Road (ECR) from Chennai, overlooking the Bay of Bengal. Your dedicated TRAGUIN chauffeur ensures a smooth and comfortable transfer to your handpicked luxury heritage hotel nestled in the heart of White Town. After check-in and relaxation, enjoy a casual evening stroll along the vehicle-free Promenade Beach, watching the waves crash against the rocky shores by the iconic French War Memorial.'
                ),
                [
                    'Sightseeing Included: ECR Scenic Route, Promenade Beach, French War Memorial, Mahatma Gandhi Statue',
                    'Evening Experience: A warm welcome dinner at a historic French estate serving wood-fired pizzas and classic French pastries.',
                    'Overnight Stay: Puducherry (Boutique Heritage French Villa Stays)',
                    'Meals Included: Dinner',
                ],
            ),
            _day(
                2,
                'Architectural Walk Through White Town & Peaceful Ashram Visit',
                (
                    'Wake up to the aroma of fresh filter coffee and croissants. Today, participate in a curated architectural walking tour led by local experts. Discover the structural differences between the French Quarter with its stately walled courtyards and the vibrant Tamil Quarter. Pay a quiet visit to the world-renowned Sri Aurobindo Ashram, offering an immersive experience in serene contemplation. In the afternoon, explore the magnificent Neo-Gothic architecture of the Basilica of the Sacred Heart of Jesus.'
                ),
                [
                    'Sightseeing Included: French Quarter, Tamil Quarter, Sri Aurobindo Ashram, Sacred Heart Basilica',
                    'Photography Points: The bright mustard-colored colonial arches adorned with pink bougainvillea flowers on Rue Romain Rolland.',
                    'Overnight Stay: Puducherry',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'Township Excursion to Auroville & Majestic Golden Matrimandir',
                (
                    'Following a premium breakfast, head to the international township of Auroville, conceived as a universal city where people of all countries can live in peace. Travel along shaded forest pathways to the viewpoint of the magnificent Matrimandir, a jaw-dropping golden sphere that serves as the silent heart of the community. Browse through exclusive boutiques featuring sustainable organic clothing, hand-made papers, and therapeutic pottery items crafted by global residents.'
                ),
                [
                    'Sightseeing Included: Auroville International Township, Matrimandir Viewpoint, Auroville Visitors Centre',
                    'Food Suggestion: Enjoy a wholesome lunch at the Auroville Bakery using organically grown farm-fresh produce.',
                    'Overnight Stay: Puducherry Luxury Resort Base',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'Speedboat Cruise to Paradise Beach & Historical Arikamedu',
                (
                    'Prepare for an exciting morning as we visit the Chunnambar Boathouse. Board a private speedboat cruise heading down the backwaters to the isolated shores of Paradise Beach. With its fine white sands and shallow waters, it provides a safe, delightful space for family beach games and water relaxation. In the afternoon, take a fascinating heritage excursion to the nearby archaeological site of Arikamedu, an ancient Roman trading port dating back to the 2nd century BC.'
                ),
                [
                    'Sightseeing Included: Chunnambar Backwaters, Paradise Beach, Arikamedu Archaeological Site',
                    'Evening Experience: A private beachside family barbecue organized by our hospitality team under the stars.',
                    'Overnight Stay: Puducherry',
                    'Meals Included: Breakfast & Beachside BBQ Dinner',
                ],
            ),
            _day(
                5,
                'Souvenir Shopping & Comfortable Return Transfer to Chennai',
                (
                    'Indulge in a final, slow-paced breakfast at your boutique resort. Spend your morning checking out local artisan boutiques for aromatic candles, handmade leather goods, and organic essential oils. Your private premium vehicle will then carry your family safely back to Chennai International Airport, concluding your luxurious Luxury Puducherry Holiday with beautiful, unforgettable memories curated exclusively by TRAGUIN.'
                ),
                [
                    'Meals Included: Breakfast',
                    'Assistance: Airport drop-off coordination and baggage handling support by your dedicated chauffeur.',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Atithi / Ocean Spray Residency',
                'Puducherry',
                '04 Nights',
                'Deluxe',
                'Standard Comfort Room',
                'MAPAI Plan',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Atithi / Ocean Spray Residency (Standard Comfort Room)',
            ),
            _hotel(
                'Maison Perumal - CGH Earth / Gratitude Heritage',
                'Puducherry',
                '04 Nights',
                'Premium',
                'Premium Heritage Room',
                'MAPAI Plan',
                4,
                2,
                description='OPTION 02 – PREMIUM: Maison Perumal - CGH Earth / Gratitude Heritage (Premium Heritage Room)',
            ),
            _hotel(
                'The Promenade / Shenbaga Hotel & Convention Centre',
                'Puducherry',
                '04 Nights',
                'Luxury',
                'Executive Rooms',
                'MAPAI Plan',
                5,
                3,
                description='OPTION 03 – LUXURY: The Promenade / Shenbaga Hotel & Convention Centre (Executive Rooms)',
            ),
            _hotel(
                'Palais de Mahé - CGH Earth / La Villa Puducherry',
                'Puducherry',
                '04 Nights',
                'Ultra Luxury',
                'Suites',
                'MAPAI Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Palais de Mahé - CGH Earth / La Villa Puducherry (Suites)',
            ),
        ],
        inclusions=[
            _inc_included('Boutique luxury accommodations inside premium heritage properties.', 1),
            _inc_included('Daily fresh breakfasts and multi-course curated gourmet dinners.', 2),
            _inc_included('Private luxury AC vehicle for all point-to-point road transfers.', 3),
            _inc_included('Auroville entry tokens and pre-booked Matrimandir access permissions.', 4),
            _inc_included('Private speedboat charter tickets to Paradise Beach.', 5),
            _inc_included('Consistent 24/7 localized on-call hospitality TRAGUIN Support.', 6),
            _inc_excluded('Flight or main train ticketing fares to Chennai.', 7),
            _inc_excluded('Monument camera passes or commercial videography charges.', 8),
            _inc_excluded('Personalized laundry services, boutique shopping, or alcoholic beverages.', 9),
            _inc_excluded('Any comprehensive medical or travel insurance policies.', 10),
        ],
    )
    return package, itinerary

def build_py_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'PY-008'
    tour_code = 'TG-PY-EDU-008'
    title = 'Premium Puducherry Educational Tour Package'
    duration = '03 Nights / 04 Days'
    slug = 'py-008-premium-puducherry-educational-tour-package'
    itin_slug = 'py-008-premium-puducherry-educational-tour-package-itinerary'
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
            _ph('State / Country: Puducherry, India | Category: Educational School Tour', 2),
            _ph('Destinations: White Town • Auroville • Arikamedu Archaeological Site • Chunnambar', 3),
            _ph('Ideal for: School Students, Educators, Academic Delegations', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle: Premium Air-Conditioned Luxury Coaches (GPS-enabled, First-Aid Equipped)', 7),
            _ph('Meal Plan: All Meals Included (Buffet Breakfast, Balanced Lunch, Healthy Evening High-Tea & Dinner)', 8),
            _ph('Route Map: Chennai/Puducherry Arrival → White Town History Walk → Auroville Township → Arikamedu Site → Departure', 9),
            _ph('TRAGUIN Signature Experience: Specialized learning curricula designed in tandem with institutional syllabi, combining leisure with real academic growth.', 10),
            _ph('Curated by TRAGUIN Experts: Restaurants handpicked to guarantee highly nutritious, child-friendly, hygienic food variations.', 11),
            _ph('Shopping & Local Experiences: Goubert Market & Cluny Embroidery Center: Perfect for exploring local organic cotton weaving and handcrafted lace work. Instagram Spots: The vibrant yellow-walled French alleys of Romain Rolland Street and Suffren Street.', 12),
            _ph('Important Notes: School NOC and student medical files must be updated and provided to TRAGUIN 15 days prior to travel commencement. Carrying sunscreen, comfortable walking shoes, and caps is highly recommended for archaeological field surveys. Due to high institutional movement, coach bookings and entry slot blockings require an early advance confirmation timeline.', 13),
        ],
        moods=['Educational', 'Academic', 'Cultural'],
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
        tagline='Premium Puducherry Educational Tour Package • 03 Nights / 04 Days',
        overview=(
            "Welcome to India's pristine window to French heritage and conscious global living. This bespoke Educational Puducherry Tour curated dynamically by TRAGUIN merges academic learning with high-end comfort, ensuring highly enriching, safe, and immersive experiences for students and educators alike. Walk along historic cobblestone lanes, discover world-class architectural marvels, study archaeological origins, and secure unforgettable memories. Our premium stays and handpicked hotels promise total student safety, top-tier hygiene, and nourishing culinary layouts.\n\nTOUR OVERVIEW\nVehicle Type: Premium Air-Conditioned Luxury Coaches (GPS-enabled, First-Aid Equipped)\nMeal Plan: All Meals Included (Buffet Breakfast, Balanced Lunch, Healthy Evening High-Tea & Dinner)\nRoute Plan: Chennai/Puducherry Arrival → White Town History Walk → Auroville Township → Arikamedu Site → Departure\n\nCurated Note:\nThis premium student holiday features full certified student insurance cover, dedicated educational field guides, mineral water distribution, and 24/7 centralized monitoring backed by TRAGUIN Support.\n\nPuducherry serves as an unparalleled living historical laboratory, making it a highly requested choice for a Best Puducherry Tour Package or an interactive Puducherry Family Tour. Combining Franco-Tamil history, global sociology, and marine ecology, it offers profound knowledge trails for academic groups.\nWhite Town (French Quarter): A colonial architectural masterclass featuring iconic attractions, pastel facades, and unique urban layouts perfect for history mapping.\nAuroville Experimental Township: An inspiring international community centered on human unity, architecture, and sustainability, home to the magnificent Matrimandir.\nArikamedu Archaeological Site: An ancient Indo-Roman trading port dating back to the 2nd Century BC, providing profound lessons in history and maritime trade archaeology.\nBest Time to Visit Puducherry: The pleasant winter window between October and March is the optimal time for outdoor Puducherry Sightseeing and learning journeys."
        ),
        seo_title='PY-008 | Premium Puducherry Educational Tour Package | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Puducherry educational package (PY-008 / TG-PY-EDU-008): White Town, Auroville, Arikamedu Archaeological Site, Chunnambar, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('White Town colonial heritage mapping walk and Franco-Indian history orientation workshop', 1),
            _ih('Auroville Visitors Centre sustainable development briefing and Matrimandir Viewpoint', 2),
            _ih('Arikamedu Archaeological Ruins Indo-Roman trading station and Chunnambar backwater eco-systems', 3),
            _ih('Sri Aurobindo Ashram spiritual education and competitive historic quiz with exclusive rewards', 4),
            _ih('TRAGUIN Signature Experience: Specialized learning curricula aligned with institutional syllabi', 5),
        ],
        days=[
            _day(
                1,
                'Arrival in Puducherry – White Town Colonial Heritage Mapping',
                (
                    'Arrive in the coastal paradise of Puducherry, where your dedicated TRAGUIN tour managers provide a warm corporate welcome. Board your premium luxury coach to transfer smoothly to your handpicked hotel for student-allocated room check-ins. In the afternoon, embark on an insightful, expert-guided architectural heritage walk through White Town. Students will map the historic French layout, view the monument memorials, and study the architectural synthesis of Franco-Tamil neighborhoods.'
                ),
                [
                    'Sightseeing Included: White Town Quarter, French War Memorial, Promenade Beachwalk',
                    'Evening Experience: Interactive student briefing and orientation workshop on Franco-Indian history by a guest historian.',
                    'Overnight Stay: Puducherry (Premium High-Security Hotel/Resort)',
                    'Meals Included: Lunch & Buffet Dinner',
                ],
            ),
            _day(
                2,
                'Auroville Experience – Conscious Sustainability & Matrimandir',
                (
                    'Relish a wholesome, premium breakfast at the hotel restaurant. Today, we journey to the famous international township of Auroville. Students will experience a curated educational briefing at the Auroville Visitors Centre, studying sustainable development, eco-friendly architecture, and water-harvesting models. Walk through organic shaded trails to view the spectacular golden dome of the Matrimandir from the panoramic viewing point, absorbing lessons in modern architecture and global social harmony.'
                ),
                [
                    'Sightseeing Included: Auroville International Township, Matrimandir Viewpoint, Auroville Bamboo Research Center',
                    'Photography Points: The breathtaking landscapes framing the architectural wonder of Matrimandir.',
                    'Overnight Stay: Puducherry',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                3,
                'Arikamedu Indo-Roman Archaeology & Chunnambar Eco-Systems',
                (
                    'Following a refreshing breakfast, travel to the historically legendary Arikamedu Archaeological Site. Guided by an expert archaeological educator, students will explore the ancient ruins of this Indo-Roman trading station, discovering Roman pottery findings, bead-making history, and ancient maritime links. In the afternoon, transition to Chunnambar Boat House for a safe cruise along backwater rivers to learn about coastal marine eco-systems, mangroves, and sandbars.'
                ),
                [
                    'Sightseeing Included: Arikamedu Archaeological Ruins, Chunnambar Backwaters, Paradise Beach Spit',
                    'Local Experience: Group field-notes session and competitive historic quiz with exclusive rewards.',
                    'Overnight Stay: Puducherry',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                4,
                'Spiritual Education & Farewell with Unforgettable Memories',
                (
                    'Indulge in your final morning breakfast. Check out of your premium stays and enjoy a quiet visit to the iconic Sri Aurobindo Ashram, learning about its rich literary, philosophical, and physical education contributions to modern India. Conclude the tour with a short shopping stop to buy handmade paper products or local clay crafts. Transfer comfortably back to your departure terminal as your exceptional Premium Puducherry Experience draws to a close, leaving everyone with deep knowledge and unforgettable memories powered by TRAGUIN.'
                ),
                [
                    'Meals Included: Breakfast & Packed Lunch',
                    'Assistance: Full baggage management and smooth departure boarding facilitation by our tour coaches.',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Atithi / Ocean Spray Residency',
                'Puducherry',
                '03 Nights',
                'Deluxe',
                'Spacious Multi-Bed Student Wings',
                'All Meals Included',
                4,
                1,
                description='OPTION 01 – DELUXE GROUP: Hotel Atithi / Ocean Spray Residency (Spacious Multi-Bed Student Wings)',
            ),
            _hotel(
                'Gratitude Heritage / Shenbaga Hotel',
                'Puducherry',
                '03 Nights',
                'Premium',
                'Club Comfort Room',
                'All Meals Included',
                4,
                2,
                description='OPTION 02 – PREMIUM: Gratitude Heritage / Shenbaga Hotel (Club Comfort Room)',
            ),
            _hotel(
                'Radisson Resort Pondicherry / The Promenade Elite',
                'Puducherry',
                '03 Nights',
                'Luxury',
                'Club Comforts',
                'All Meals Included',
                5,
                3,
                description='OPTION 03 – PREMIUM LUXURY: Radisson Resort Pondicherry / The Promenade Elite (Club Comforts)',
            ),
            _hotel(
                'Radisson Resort Pondicherry / The Promenade Elite',
                'Puducherry',
                '03 Nights',
                'Ultra Luxury',
                'Elite Club Suite',
                'All Meals Included',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Radisson Resort Pondicherry / The Promenade Elite (Elite Club Suite)',
            ),
        ],
        inclusions=[
            _inc_included('Handpicked hotel accommodations with 24/7 security & CCTV coverage.', 1),
            _inc_included('All buffet meals prepared under strict hygiene parameters.', 2),
            _inc_included('Private luxury AC coaches for all transfers and academic travel.', 3),
            _inc_included('Complimentary entry permissions and cruise boat tickets at Chunnambar.', 4),
            _inc_included('Professional educational field guide and historian lecture fee.', 5),
            _inc_included('Comprehensive student group travel insurance coverages.', 6),
            _inc_included('Consistent TRAGUIN Support on-site manager.', 7),
            _inc_excluded('Train fares or commercial flight tickets to airport base.', 8),
            _inc_excluded('Personal purchases, individual room services, or laundry bills.', 9),
            _inc_excluded('Camera or videography permit fees at archaeological centers.', 10),
        ],
    )
    return package, itinerary

def build_py_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'PY-009'
    tour_code = 'TG-PY-FAM-009'
    title = 'Premium Puducherry Family Beach Holiday'
    duration = '04 Nights / 05 Days'
    slug = 'py-009-premium-puducherry-family-beach-holiday'
    itin_slug = 'py-009-premium-puducherry-family-beach-holiday-itinerary'
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
            _ph('State / Country: Puducherry, India | Category: Luxury Family Beach Escape', 2),
            _ph('Destinations: White Town • Paradise Beach • Serenity Beach • Auroville', 3),
            _ph('Ideal for: Families, Multi-generational Groups, Leisure Seekers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle: Premium Private Air-Conditioned Multi-Utility Vehicle (Innova Crysta / Luxury Traveler)', 7),
            _ph('Meal Plan: Breakfast & Curated Family Dinners (French-Indo Fusion Gastronomy Options)', 8),
            _ph('Route Map: Chennai International Airport Arrival → Puducherry French Quarter → Auroville → Paradise Beach → Return Transfer', 9),
            _ph('TRAGUIN Signature Experience: Private family cycling tour through the quiet lanes of the French Quarter at sunrise with safety gears.', 10),
            _ph('Curated by TRAGUIN Experts: Selective dining partners ensuring premium hygiene and distinct child-friendly meal variations.', 11),
            _ph('Shopping & Local Experiences: Shopping Highlights: Auroville boutique soaps, hand-rolled candles, and fine leather goods.', 12),
            _ph('Important Notes: Advance Booking Suggestion: Due to high peak seasonal demand within the boutique heritage hotels of White Town, family suites must be reserved 45–60 days in advance. Dress Code Notice: When visiting the Aurobindo Ashram or the Matrimandir pavilion area, conservative clothing covering shoulders and knees is highly recommended. Weather Advice: Light cotton clothing, sunscreen lotions, and wide hats are optimal for day excursions.', 13),
        ],
        moods=['Family', 'Beach', 'Leisure'],
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
        tagline='Premium Puducherry Family Beach Holiday • 04 Nights / 05 Days',
        overview=(
            "Welcome to the French Riviera of the East. This meticulously designed Luxury Puducherry Holiday curated by TRAGUIN is expertly crafted for family vacations, offering seamless transitions, immersive experiences, and a beautiful blend of heritage and coastal leisure. Walk past pastel colonial mansions, witness breathtaking landscapes over the azure Bay of Bengal, and create unforgettable memories within our handpicked hotels. Relish premium stays that provide exceptional comfort, bespoke children's activities, and elite family-oriented hospitality.\n\nTOUR OVERVIEW\nVehicle Type: Premium Private Air-Conditioned Multi-Utility Vehicle (Innova Crysta / Luxury Traveler)\nMeal Plan: Breakfast & Curated Family Dinners (French-Indo Fusion Gastronomy Options)\nRoute Plan: Chennai International Airport Arrival → Puducherry French Quarter → Auroville → Paradise Beach → Return Transfer\n\nCurated Note:\nThis premium TRAGUIN Puducherry Package features a privately guided architecture trail of White Town, VIP priority speed-boat charters to Paradise Beach, and pre-arranged family passes for a relaxed, stress-free journey.\n\nPuducherry is widely recognized as India's premier coastal sanctuary for cultural fusion, making it a highly searched option for a Best Puducherry Tour Package or a relaxing Puducherry Family Tour. Famous for its colonial French architecture, spiritual retreats, and golden sand beaches, it promises a pristine multi- generational getaway.\nWhite Town (French Quarter): A historic enclave filled with mustard-walled villas, bougainvillea-shaded avenues, and artisanal boutiques—the absolute finest location for family photography.\nParadise Beach: Accessible via a scenic backwater cruise, it offers isolated, clean golden sands, perfect for family beach sports and water recreation.\nTop Tourist Places in Puducherry: Features the famous Promenade Beach, Aurobindo Ashram, Matrimandir viewpoint, and the sacred Sacred Heart Basilica.\nBest Time to Visit Puducherry: The pleasantly refreshing coastal months from October to March present an optimal climate for comprehensive, sun-kissed Puducherry Sightseeing."
        ),
        seo_title='PY-009 | Premium Puducherry Family Beach Holiday | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Puducherry family beach package (PY-009 / TG-PY-FAM-009): White Town, Paradise Beach, Serenity Beach, Auroville, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('East Coast Road drive, Promenade Beach Walk, and French Quarter orientation', 1),
            _ih('French Quarter heritage trail, Sri Aurobindo Ashram, and private family croissant baking masterclass', 2),
            _ih('Chunnambar Backwaters priority speedboat charter and Paradise Beach luxury excursion', 3),
            _ih('Auroville Matrimandir Viewing Pavilion and Serenity Beach Pier sunset', 4),
            _ih('TRAGUIN Signature Experience: Private family cycling tour through French Quarter at sunrise', 5),
        ],
        days=[
            _day(
                1,
                'Chennai to Puducherry – Scenic East Coast Road Drive & French Quarter Check-In',
                (
                    'Your premium family vacation begins with a warm greeting by your private chauffeur at Chennai Airport. Embark on a spectacular drive along the scenic East Coast Road (ECR), catching glimpses of the sparkling ocean. Arrive in Puducherry and check into your handpicked luxury heritage hotel in White Town. Spend a relaxing afternoon settling in. As dusk sets, enjoy an immersive stroll down the beachfront Promenade, feeling the cool sea breeze while viewing the iconic Mahatma Gandhi statue.'
                ),
                [
                    'Sightseeing Included: East Coast Road Drive, Promenade Beach Walk, French Quarter Orientation',
                    "Welcome Amenities: Personalized welcome drinks, a traditional box of French macarons, and custom kids' welcome activity kits.",
                    'Overnight Stay: Puducherry French Quarter (Premium Luxury Heritage Hotel)',
                    'Meals Included: Dinner',
                ],
            ),
            _day(
                2,
                'French Quarter Heritage Trail, Cycling & Experiential Gastronomy',
                (
                    'Savor a delightful gourmet morning breakfast. Today, a private architecture historian leads your family on a highly curated walking or cycling trail across the grid-patterned streets of White Town. Admire the stunning blend of European architecture and traditional Tamil courtyards. Visit the serene Sri Aurobindo Ashram, followed by the majestic Notre Dame des Anges church. In the afternoon, partake in a private family baking masterclass at an artisanal French patisserie.'
                ),
                [
                    'Sightseeing Included: Sri Aurobindo Ashram, Notre Dame Church, French Quarter Architectural Mansions',
                    'Exclusive Experience: 1-Hour Private Family Croissant & Pastry Baking Session with an expert pastry chef.',
                    'Overnight Stay: Puducherry French Quarter',
                    'Meals Included: Breakfast & Family Dinner',
                ],
            ),
            _day(
                3,
                'Paradise Beach Backwater Cruise & Golden Sand Retreat',
                (
                    'Following a refreshing premium breakfast, drive comfortably to Chunnambar Eco-Cruises. Board a private, priority speedboat charter arranged exclusively by TRAGUIN through the lush mangrove-lined backwaters. Step onto the pristine shores of Paradise Beach. Spend a beautiful day enjoying your family holiday—build sandcastles with the children, relax under luxury beach shacks, or engage in safe water sports under professional guidance.'
                ),
                [
                    'Sightseeing Included: Chunnambar Backwaters, Paradise Beach Luxury Excursion',
                    'Photography Points: The sweeping sandy coastlines and turquoise waves of Paradise Beach during midday sun.',
                    'Overnight Stay: Puducherry Beachfront Resort Base',
                    'Meals Included: Breakfast & Beachfront Seafood Barbecue Dinner',
                ],
            ),
            _day(
                4,
                'Auroville Spiritual Eco-Walk & Serenity Beach Sunset',
                (
                    'Wake up to the breathtaking landscapes of the coast. Today, journey on a brief drive to the international township of Auroville. Walk through the peaceful forest paths to reach the viewing pavilion overlooking the magnificent golden globe of the Matrimandir. Learn about this sustainable community model together. In the late afternoon, head to Serenity Beach to watch local surfers and catch a glorious sunset from the rocky pier.'
                ),
                [
                    'Sightseeing Included: Auroville International Township, Matrimandir Viewing Pavilion, Serenity Beach Pier',
                    "Food Suggestion: Wood-fired organic sourdough pizzas at Auroville's famous open-air cafes.",
                    'Overnight Stay: Puducherry Beachfront Resort',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'Souvenir Shopping & Comfortable Return Transfer to Chennai',
                (
                    'Indulge in a late breakfast at your resort patio. Spend your morning shopping for premium hand-made paper items, local terracotta art, organic aromatic oils, and chic resort wear. Your private premium vehicle will then transfer you comfortably back along the ECR to Chennai International Airport. Your magical Premium Puducherry Experience concludes here, leaving your family with beautiful stories and unforgettable memories to treasure forever.'
                ),
                [
                    'Meals Included: Breakfast',
                    'Shopping Highlights: Auroville boutique soaps, hand-rolled candles, and fine leather goods.',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Atithi / Ocean Spray Residency',
                'Puducherry',
                '04 Nights',
                'Deluxe',
                'Standard Comfort Room',
                'Breakfast & Family Dinners',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Atithi / Ocean Spray Residency (Standard Comfort Room)',
            ),
            _hotel(
                'Maison Perumal - CGH Earth / Gratitude Heritage',
                'Puducherry',
                '04 Nights',
                'Premium',
                'Premium Heritage Room',
                'Breakfast & Family Dinners',
                4,
                2,
                description='OPTION 02 – PREMIUM: Maison Perumal - CGH Earth / Gratitude Heritage (Premium Heritage Room)',
            ),
            _hotel(
                'Villa Shanti / Radisson Resort Pondicherry Bay',
                'Puducherry',
                '04 Nights',
                'Luxury',
                'Executive Interconnected Family Rooms',
                'Breakfast & Family Dinners',
                5,
                3,
                description='OPTION 03 – LUXURY: Villa Shanti / Radisson Resort Pondicherry Bay (Executive Interconnected Family Rooms)',
            ),
            _hotel(
                'Palais de Mahé - CGH Earth / InterContinental Resort ECR',
                'Puducherry',
                '04 Nights',
                'Ultra Luxury',
                'Luxury Family Suite',
                'Breakfast & Family Dinners',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Palais de Mahé - CGH Earth / InterContinental Resort ECR (Luxury Family Suite)',
            ),
        ],
        inclusions=[
            _inc_included('Handpicked family-friendly premium accommodations.', 1),
            _inc_included('Daily buffet breakfast & curated gourmet family dinners.', 2),
            _inc_included('Private luxury AC Innova Crysta for all airport transfers & local touring.', 3),
            _inc_included('Private priority speedboat charter for the Paradise Beach tour.', 4),
            _inc_included('Complimentary family pastry baking experience pass.', 5),
            _inc_included('Dedicated 24/7 localized operational and guest TRAGUIN Support.', 6),
            _inc_included('All luxury state entry permits, toll fees, and driver allowances.', 7),
            _inc_excluded('Airfare or national railway train tickets to Chennai.', 8),
            _inc_excluded('Professional camera entry tickets at heritage monuments.', 9),
            _inc_excluded('Personal laundry expenditures, phone calls, or alcoholic drinks.', 10),
            _inc_excluded('Any comprehensive medical or travel insurance policies.', 11),
        ],
    )
    return package, itinerary

def build_py_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'PY-010'
    tour_code = 'TG-PY-FAM-010'
    title = 'Premium Puducherry Complete Family Tour'
    duration = '05 Nights / 06 Days'
    slug = 'py-010-premium-puducherry-complete-family-tour'
    itin_slug = 'py-010-premium-puducherry-complete-family-tour-itinerary'
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
            _ph('State / Country: Puducherry (Pondicherry), India | Category: Complete Family Tour', 2),
            _ph('Destinations: Puducherry French Quarter • Auroville • Paradise Beach • Chidambaram', 3),
            _ph('Ideal for: Families, Couples, Leisure Travelers, Culture Enthusiasts', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle: Premium Air-Conditioned Family Multi-Utility Vehicle (Private Chauffeur)', 7),
            _ph('Meal Plan: Daily Gourmet Breakfast & Multi-Cuisine Specialty Dinners (MAPAI Plan)', 8),
            _ph('Route Map: Chennai Arrival → Puducherry French Quarter → Auroville → Pichavaram Mangroves → Chennai Departure', 9),
            _ph('TRAGUIN Signature Experience: Private French Quarter architecture specialist guide who shares hidden historical tales and local legends with your family.', 10),
            _ph('Curated by TRAGUIN Experts: Handpicked restaurant recommendations that perfectly balance authentic French baking and spicy Tamil culinary arts.', 11),
            _ph("Shopping & Local Experiences: Goubert Market & Nehru Street: Excellent for picking up locally made terracotta items, premium leather footwear, and organic essential oils. Famous Bakeries: Drop by Baker's Street or Café des Arts for world-class buttery croissants, macaroons, and artisanal coffee.", 12),
            _ph('Important Notes: Advance Booking Suggestion: Since boutique heritage properties in White Town have limited room keys, we highly recommend reserving your dates 60 days in advance. Clothing Etiquette: Modest attire covering shoulders and knees is mandatory while entering the Sri Aurobindo Ashram and Chidambaram Temple grounds.', 13),
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
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Premium Puducherry Complete Family Tour • 05 Nights / 06 Days',
        overview=(
            "Welcome to the French Riviera of the East. This exquisite Luxury Puducherry Holiday created passionately by TRAGUIN is expertly designed to offer your family a sublime blend of coastal relaxation, bohemian charm, and historical elegance. Revel in the breathtaking landscapes of cobblestone streets lined with bougainvillea, experience curated culinary and spiritual paths, and create unforgettable memories within premium stays and handpicked hotels that embrace traditional luxury and global sophistication.\n\nTOUR OVERVIEW\nVehicle Type: Premium Air-Conditioned Family Multi-Utility Vehicle (Private Chauffeur)\nMeal Plan: Daily Gourmet Breakfast & Multi-Cuisine Specialty Dinners (MAPAI Plan)\nRoute Plan: Chennai Arrival → Puducherry French Quarter → Auroville → Pichavaram Mangroves → Chennai Departure\n\nCurated Note:\nThis premium TRAGUIN Puducherry Package features pre-cleared VIP passes to Auroville's inner viewing lane, private boat charters in Pichavaram, and a dedicated family travel concierge on call 24/7.\n\nPuducherry is an unmatched cultural and coastal refuge, making it a highly searched option for a Best Puducherry Tour Package or a relaxing Puducherry Family Tour. Famous for its seamless transition between French heritage and deep Indian spiritual roots, it offers exceptional getaways for families and couples.\nThe French Quarter (White Town): A timeless neighborhood boasting mustard-yellow colonial mansions, famous architecture, and the most iconic attractions for heritage walks.\nAuroville Matrimandir: A magnificent golden globe symbolizing universal peace, widely searched as a prime spiritual and Premium Puducherry Experience site.\nPristine Beaches: Features Paradise Beach and Serenity Beach, recognized as popular Instagram locations for sunrise photography and family leisure.\nBest Time to Visit Puducherry: The refreshing and pleasant winter window between October and March provides the absolute best climate for Puducherry Sightseeing."
        ),
        seo_title='PY-010 | Premium Puducherry Complete Family Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Puducherry complete family package (PY-010 / TG-PY-FAM-010): French Quarter, Auroville, Paradise Beach, Pichavaram Mangroves, Chidambaram, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('East Coast Road drive, Promenade Beach Walk, and Gandhi Statue Landmark welcome dinner', 1),
            _ih('White Town French Mansions, Sri Aurobindo Ashram, Sacred Heart Basilica, and Manakula Vinayagar Temple', 2),
            _ih('Auroville Matrimandir Viewpoint, Auroville Beach, and sustainable pottery artisan interaction', 3),
            _ih('Paradise Beach private speedboat charter and Pichavaram Mangrove intertwined channels', 4),
            _ih('Chidambaram Nataraja Temple cosmic-dance Dravidian architecture excursion', 5),
        ],
        days=[
            _day(
                1,
                'Arrival via Chennai & Scenic Coastal Drive to Puducherry',
                (
                    'Arrive at Chennai Airport or Railway Station, where your elite TRAGUIN chauffeur greets your family with refreshing amenities. Board your private premium vehicle for a spectacular, scenic drive down the East Coast Road (ECR), with the shimmering Bay of Bengal accompanying you. Arrive in Puducherry and check into your handpicked luxury hotel in the heart of White Town. Spend a relaxed evening walking along the famous Promenade Beach, feeling the crisp sea breeze.'
                ),
                [
                    'Sightseeing Included: East Coast Road Drive, Promenade Beach Walk, Gandhi Statue Landmark',
                    'Evening Experience: A warm welcome dinner at a heritage French courtyard restaurant inside the resort.',
                    'Overnight Stay: Puducherry (Premium French Colonial Luxury Stay)',
                    'Meals Included: Welcome Dinner',
                ],
            ),
            _day(
                2,
                'French Quarter Heritage Walk & Spiritual Immersion',
                (
                    'Enjoy a gourmet multi-cuisine breakfast. Today, experience a private heritage walking tour through the neat, cobblestone lanes of White Town. Admire the stunning pastel facades, historic arches, and blooming bougainvillea. Visit the serene Sri Aurobindo Ashram, a world-renowned spiritual sanctuary, to enjoy quiet family meditation. Later, visit the spectacular, neo-Gothic Basilica of the Sacred Heart of Jesus and the ancient Arulmigu Manakula Vinayagar Temple.'
                ),
                [
                    'Sightseeing Included: White Town French Mansions, Sri Aurobindo Ashram, Sacred Heart Basilica, Manakula Vinayagar Temple',
                    'Photography Points: The striking contrast of bright yellow walls and white windows on Rue Romain Rolland.',
                    'Overnight Stay: Puducherry',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'Auroville Spiritual Dome & Bohemian Cafe Trail',
                (
                    "Following a refreshing premium breakfast, journey to the international township of Auroville. Walk along shaded, peaceful forest pathways to reach the magnificent golden Matrimandir viewing point, an architectural marvel. Learn about the township's unique vision of human unity. In the afternoon, explore Auroville's creative boutiques and indulge in organic wood-fired artisanal pizzas at a highly recommended forest cafe."
                ),
                [
                    'Sightseeing Included: Auroville International Township, Matrimandir Viewpoint, Auroville Beach',
                    'Exclusive Experiences: Private interaction with local artisans specializing in sustainable pottery and musical instruments.',
                    'Overnight Stay: Puducherry',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'Private Cruise to Paradise Beach & Sunset Chill',
                (
                    'Savor a delightful breakfast before heading to Chunnambar Boat House. Board an exclusive, private speedboat charter cruising through scenic backwaters to reach the isolated sands of Paradise Beach. Known for its soft white sand and clean waters, it is a paradise for family beach games and pure relaxation. Spend your afternoon enjoying coconut water under private shacks. Return to the main town for a relaxed, free evening.'
                ),
                [
                    'Sightseeing Included: Chunnambar Backwaters, Paradise Beach Charter Cruise',
                    'Optional Activities: Fun family beach volleyball or a gentle surf lesson at Serenity Beach.',
                    'Overnight Stay: Puducherry',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'Excursion to Pichavaram Mangrove Forests & Chidambaram',
                (
                    "An extraordinary day of natural wonder awaits. After an early breakfast, drive south to Pichavaram Mangrove Forest, the world's second-largest mangrove system. Board a hand-rowed private boat to navigate deep inside rare, narrow, natural canopy channels where trees emerge out of water—a breathtaking landscape. Later, visit the grand 12th-century Chidambaram Nataraja Temple, showcasing magnificent cosmic-dance Dravidian architecture, before returning north."
                ),
                [
                    'Sightseeing Included: Pichavaram Mangrove Intertwined Channels, Chidambaram Nataraja Temple',
                    'Food Suggestion: Traditional South Indian filter coffee and fresh tiffin delicacies at a heritage stop.',
                    'Overnight Stay: Puducherry (Premium Luxury Suite)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                6,
                'Artisanal Souvenir Shopping & Departure via Chennai',
                (
                    "Indulge in a final delicious breakfast at your resort patio. Spend a leisurely hour shopping for Puducherry's world-famous handmade paper products, aromatic candles, and boutique cotton garments. Your private chauffeur will then drive your family comfortably back to Chennai Airport or Railway Station. Your magical Puducherry Honeymoon or Family Tour concludes here, leaving your loved ones with unforgettable memories curated exclusively by TRAGUIN."
                ),
                [
                    'Meals Included: Breakfast',
                    'Assistance: Priority baggage handling and airport drop assistance from our chauffeur.',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Atithi / Ocean Spray Residency',
                'Puducherry',
                '05 Nights',
                'Deluxe',
                'Standard Comfort Room',
                'MAPAI Plan',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Atithi / Ocean Spray Residency (Standard Comfort Room)',
            ),
            _hotel(
                'Maison Perumal - CGH Earth / Gratitude Heritage',
                'Puducherry',
                '05 Nights',
                'Premium',
                'Premium Heritage Room',
                'MAPAI Plan',
                4,
                2,
                description='OPTION 02 – PREMIUM: Maison Perumal - CGH Earth / Gratitude Heritage (Premium Heritage Room)',
            ),
            _hotel(
                'Villa Shanti / Le Dupleix Heritage Hotel',
                'Puducherry',
                '05 Nights',
                'Luxury',
                'Executive Luxury Room',
                'MAPAI Plan',
                5,
                3,
                description='OPTION 03 – LUXURY: Villa Shanti / Le Dupleix Heritage Hotel (Executive Luxury Room)',
            ),
            _hotel(
                'Palais de Mahé - CGH Earth / The Promenade Premium Oceanfront',
                'Puducherry',
                '05 Nights',
                'Ultra Luxury',
                'Luxury Suite',
                'MAPAI Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Palais de Mahé - CGH Earth / The Promenade Premium Oceanfront (Luxury Suite)',
            ),
        ],
        inclusions=[
            _inc_included('Premium luxury hotel stays in carefully selected family suites.', 1),
            _inc_included('Daily gourmet breakfast buffets and curated multi-course dinners.', 2),
            _inc_included('Private luxury AC Innova/Crysta vehicle for all transfers & sightseeing.', 3),
            _inc_included('Private family speedboat charter to Paradise Beach.', 4),
            _inc_included('Private rowboat excursion deep into Pichavaram Mangrove channels.', 5),
            _inc_included('Pre-arranged passes for Auroville Matrimandir viewing gates.', 6),
            _inc_included('Continuous on-ground TRAGUIN Support and holiday coordination.', 7),
            _inc_excluded('Airfare or interstate express train tickets to Chennai.', 8),
            _inc_excluded('Monument camera entry fees or personal local guide tips.', 9),
            _inc_excluded('Personal laundry, phone calls, or alcoholic refreshments.', 10),
            _inc_excluded('Any travel insurance policies or medical expenses.', 11),
        ],
    )
    return package, itinerary

PUDUCHERRY_DOMESTIC_BUILDERS = [
    build_py_001,
    build_py_002,
    build_py_003,
    build_py_004,
    build_py_005,
    build_py_006,
    build_py_007,
    build_py_008,
    build_py_009,
    build_py_010,
]
