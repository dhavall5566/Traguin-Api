"""Builder functions for GA-001 through GA-025 Goa packages (excluding GA-011)."""

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

GOA_SLUG = "goa"


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


def build_ga_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-001'
    tour_code = 'TRAGUIN-GA-001'
    title = 'TRAGUIN Premium Romantic Goa Escape'
    duration = '03 Nights / 04 Days'
    slug = 'ga-001-premium-romantic-goa-escape'
    itin_slug = 'ga-001-premium-romantic-goa-escape-itinerary'
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
            _ph('Serial code GA-001 | TRAGUIN tour code TRAGUIN-GA-001', 1),
            _ph('State / Country: Goa / India | Category: Romantic Couple', 2),
            _ph('Destinations: North Goa Private Retreat • South Goa Heritage Circuit', 3),
            _ph('Ideal for: Honeymooners & Couples', 4),
            _ph('Best season: October to May', 5),
            _ph('Starting price: On Request (Premium Custom)', 6),
            _ph('Vehicle / Meals: Chauffeur-Driven Luxury Sedan', 7),
            _ph('Route: Goa Airport Arrival → North Goa Beaches → Latin Quarter Walk → South Goa', 8),
            _ph('TRAGUIN Signature Experience: Exclusive access to hidden coastal spots and private local dining', 9),
            _ph('Curated by TRAGUIN Experts: Every detail is carefully crafted by travel specialists passionate', 10),
            _ph('Premium Handpicked Hotels: Resorts are thoroughly vetted for privacy, high-end hospitality, and', 11),
            _ph('Personalized Assistance: Enjoy 24/7 direct access to our helpful concierge team throughout your', 12),
            _ph("Goa Local Markets: Discover the lively atmosphere of the Anjuna Flea Market or the Saturday Night Market in Arpora. These markets are excellent places to find handmade jewelry, bohemian clothing, and unique local arts. Souvenirs & Cafes: Explore the stylish boutiques of Panaji for beautiful Mario Miranda artwork and hand- painted Azulejos ceramic tiles. Don't miss out on enjoying locally grown, artisanal coffee at the charming cafes hidden throughout Fontainhas.", 13),
            _ph('Standard check-in begins at 14:00 hrs, and check-out is at 11:00 hrs across all luxury beachfront', 14)
        ],
        moods=['Romantic', 'Beach', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Custom)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='TRAGUIN Premium Romantic Goa Escape',
        overview="LUXURY Unveil the magic of an idyllic tropical haven designed exclusively for two. The Best Goa Tour Package invites you to step into a world of swaying palms, pristine shorelines, and vibrant cultural tapestries. Crafted specifically as an ultra-romantic Goa Honeymoon Package, this itinerary seamlessly balances intimate moments with exhilarating coastal explorations. Discover a truly Luxury Goa Holiday where sun-kissed beaches, golden sunsets, and premium stays come together to etch beautiful, lifelong memories.\n\nTOUR OVERVIEW\nThis romantic coastal escape is meticulously designed as an independent FIT tour, assuring absolute privacy and bespoke attention. Your private getaway is serviced by an executive chauffeur-driven premium vehicle to escort you effortlessly between scenic coastlines and historic attractions. Every element of your trip is coordinated through the signature luxury hospitality of TRAGUIN, guaranteeing handpicked beachfront boutique hotels, exclusive experiences, and tailored romantic surprises.\n\nTHE ULTIMATE PREMIUM GOA EXPERIENCE\nPlanning a Goa Family Tour or a romantic retreat provides access to some of the most celebrated Top Tourist Places in Goa. Renowned globally for its breathtaking landscapes and world-class hospitality, Goa effortlessly blends relaxation with vibrant energy. From capturing beautiful couples' portraits at popular Instagram locations like Fontainhas to indulging in immersive experiences like luxury yacht cruises, our custom-tailored TRAGUIN Goa Packages ensure you discover the very best of this coastal paradise during the absolute Best Time to Visit Goa.",
        seo_title='GA-001 | TRAGUIN Premium Romantic Goa Escape | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Goa package (GA-001 / TRAGUIN-GA-001): North Goa Private Retreat • South Goa Heritage Circuit.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA & SUNSET LUXURY', 1),
            _ih('Day 02: NORTH GOA ROMANTIC EXPLORATION', 2),
            _ih('Day 03: FONTAINHAS HERITAGE WALK & SOUTH GOA TRANQUILITY', 3),
            _ih('Day 04: LEISURELY MORNING & DEPARTURE', 4)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA & SUNSET LUXURY',
                (
                    'WELCOME TO COASTAL PARADISE – TRAGUIN MEET & GREET & PRIVATE SUNSET CRUISE Your dream Premium Goa Experience begins the moment you touch down. Upon your arrival at Goa Airport, you will receive an exclusive, warm welcome arranged by your dedicated TRAGUIN concierge representative. A private chauffeur will assist with your baggage and escort you in a premium, climate-controlled vehicle to your handpicked luxury beachfront resort. After checking into your ocean-view room and relaxing, prepare for an unforgettable evening. You will be driven to a private jetty to board an exclusive luxury sunset cruise along the Mandovi River. Savor refreshing champagne and light bites as you witness the mesmerizing golden sun dipping below the Arabian Sea. This spectacular setting serves as a perfect photography point to capture your first evening together. Coastal Drive. session. beach. Resort).'
                ),
                [
                    'Sightseeing Included: Mandovi River Cruise, Scenic',
                    "Optional Activities: Premium couples' resort spa",
                    'Evening Experience: Candlelit cabana dinner on the',
                    'Overnight Stay: Goa (Handpicked Beachfront Luxury',
                ],
            ),            _day(
                2,
                'NORTH GOA ROMANTIC EXPLORATION',
                (
                    "FORTRESS VISTAS & CHIC BEACHSIDE HANGOUTS Wake up to the soothing sound of ocean waves and enjoy a lavish buffet breakfast. Today's beautifully paced Goa Sightseeing features the iconic highlights of North Goa. Your first stop is the historic 17th-century Fort Aguada, where you can take in panoramic ocean vistas from the ancient lighthouse bastions. Following your fort visit, enjoy a scenic drive past Sinquerim Beach toward the vibrant stretches of Vagator and Anjuna. Spend your afternoon relaxing at an exclusive beachfront club, enjoying artisanal cocktails and local seafood delicacies. Before returning to your resort, capture the sunset from the dramatic clifftops overlooking Chapora Fort, famously known for its cinematic views. Chapora Fort Viewpoint. Sinquerim Beach. acclaimed cliffside restaurant."
                ),
                [
                    'Sightseeing Included: Fort Aguada, Vagator Beach,',
                    'Optional Activities: Parasailing or jet-skiing at',
                    'Evening Experience: Fine-dining at a critically',
                    'Overnight Stay: Goa Luxury Resort.',
                ],
            ),            _day(
                3,
                'FONTAINHAS HERITAGE WALK & SOUTH GOA TRANQUILITY',
                (
                    "LATIN QUARTER CHARM & PRIVATE SUN-KISSED BAY COMFORT After breakfast, immerse yourselves in the cultural heart of Goa. Your private guide will escort you on a charming walk through Fontainhas, Panaji's famous Latin Quarter. This popular Instagram location features brightly colored Portuguese-style houses, quaint wrought-iron balconies, and narrow winding alleys. In the afternoon, travel south to experience the peaceful side of Goa. Visit the stunning Basilica of Bom Jesus, a UNESCO World Heritage site, before heading to the quiet, powdery white sands of Utorda or Varca beach. This tranquil setting is perfect for reflecting on your journey and enjoying peaceful moments away from the crowds. Basilica of Bom Jesus, South Goa White Sand Beaches. a traditional Goan lunch. historic mansion lounge."
                ),
                [
                    'Sightseeing Included: Fontainhas Heritage Walk,',
                    'Optional Activities: High-end spice plantation tour with',
                    'Evening Experience: Live acoustic music session at a',
                    'Overnight Stay: Goa Luxury Resort.',
                ],
            ),            _day(
                4,
                'LEISURELY MORNING & DEPARTURE',
                (
                    "SAYING GOODBYE TO THE COAST – MEMORIES BEYOND DESTINATIONS Savor your last morning with a relaxed breakfast served on your private balcony. Enjoy a final swim in the resort's infinity pool or take a quiet stroll along the beach to collect seashells. Depending on your flight time, your private chauffeur will be ready to take you for some last-minute shopping for local souvenirs, fine cashew nuts, or traditional feni. Your luxury holiday concludes with a private transfer to Goa Airport, leaving you with beautiful, lifelong memories curated by TRAGUIN. stops."
                ),
                [
                    'Sightseeing Included: Local markets, artisanal craft',
                    'Meals Included: Premium Gourmet Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Lemon Tree Amarante Beach Resort / Similar',
                'Goa (3 Nights)',
                '03 Nights',
                'Deluxe',
                'Superior Room',
                'CP (Breakfast)',
                4,
                1,
                description='OPTION 01 – DELUXE: Lemon Tree Amarante Beach Resort / Similar (Goa (3 Nights)) | CP (Breakfast)',
            ),
            _hotel(
                'Novotel Goa Resort & Spa / Similar',
                'Goa (3 Nights)',
                '03 Nights',
                'Premium',
                'Luxury Room',
                'CP (Breakfast)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Novotel Goa Resort & Spa / Similar (Goa (3 Nights)) | CP (Breakfast)',
            ),
            _hotel(
                'Taj Fort Aguada Resort & Spa / Taj Holiday Village',
                'Goa (3 Nights)',
                '03 Nights',
                'Luxury',
                'Premium Sea View Cottage',
                'CP (Breakfast)',
                5,
                3,
                description='OPTION 03 – LUXURY: Taj Fort Aguada Resort & Spa / Taj Holiday Village (Goa (3 Nights)) | CP (Breakfast)',
            ),
            _hotel(
                'The Leela Goa / W Goa (Vagator)',
                'Goa (3 Nights)',
                '03 Nights',
                'Ultra Luxury',
                'Luxury Lagoon Suite / Marvelous Chalet',
                'CP + Welcome Mix',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Leela Goa / W Goa (Vagator) (Goa (3 Nights)) | CP + Welcome Mix',
            )
        ],
        inclusions=[
            _inc_excluded('Luxury beachfront accommodation in handpicked', 1),
            _inc_excluded('properties.', 2),
            _inc_excluded('Daily premium multi-cuisine buffet breakfasts.', 3),
            _inc_excluded('Domestic or International airfares/train bookings.', 4),
            _inc_excluded('Monument entry tickets or water sports activity fees.', 5),
            _inc_excluded('Private executive chauffeur-driven air-conditioned', 6),
            _inc_excluded('vehicle.', 7),
            _inc_excluded('Exclusive private sunset cruise on a luxury boat/yacht.', 8),
            _inc_excluded('Guided romantic heritage walk through the Latin', 9),
            _inc_excluded('Quarter (Fontainhas).', 10),
            _inc_excluded('Special welcome amenities (chocolates and sparkling', 11),
            _inc_excluded('wine).', 12),
            _inc_excluded('24/7 dedicated TRAGUIN concierge support.', 13),
            _inc_excluded('Personal expenses (laundry, telephone calls, room', 14),
            _inc_excluded('mini-bar).', 15),
            _inc_excluded('Optional dinner bookings or premium beach club', 16),
            _inc_excluded('access tickets.', 17),
            _inc_excluded('Mandatory peak season or festival gala dinner', 18),
            _inc_excluded('surcharges.', 19),
            _inc_excluded('Travel or medical insurance coverage.', 20),
            _inc_excluded('Any items not explicitly listed under inclusions.', 21),
        ],
    )
    return package, itinerary

def build_ga_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-002'
    tour_code = 'TRAGUIN-GA-002'
    title = 'TRAGUIN Premium Goa Family Tour Package'
    duration = '04 Nights / 05 Days'
    slug = 'ga-002-goa-family-fun'
    itin_slug = 'ga-002-goa-family-fun-itinerary'
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
            _ph('Serial code GA-002 | TRAGUIN tour code TRAGUIN-GA-002', 1),
            _ph('State / Country: Goa / India | Category: Goa Family Fun', 2),
            _ph('Destinations: North Goa (2N) • South Goa (2N) - Complete Family Experience', 3),
            _ph('Ideal for: Family Vacations & Multi- Gen Groups', 4),
            _ph('Best season: November to April', 5),
            _ph('Starting price: On Request (Premium Family Custom)', 6),
            _ph('Vehicle / Meals: Private Luxury Air-', 7),
            _ph('Route: Goa Airport Arrival → North Goa Beachfront → South Goa Heritage → Goa Airport Departure', 8),
            _ph('Curated by TRAGUIN Experts: Itineraries balanced perfectly for all ages, combining exciting beach', 9),
            _ph('Personalized Assistance: Continuous contact with our dedicated concierge team to adjust daily', 10),
            _ph('Premium Handpicked Hotels: Resorts selected for their excellent family amenities, large swimming', 11),
            _ph('Luxury Transportation: High-end, spacious vehicles with safe, professional drivers who know the', 12),
            _ph('North Goa Shopping & Dining: Visit the lively Wednesday Anjuna Flea Market or the Saturday Night Market in Arpora for unique handmade crafts, beachwear, and local artwork. Enjoy a family meal at Brittos or Curlies for classic Goan fish curry. South Goa Souvenirs: Pick up delicious, freshly baked Bebinca cake and traditional Goan sweets at historic bakeries in Panaji. Shop for high-quality organic cashews, local spices, and beautiful hand-painted ceramic tiles (Azulejos) to take home.', 13)
        ],
        moods=['Family', 'Beach', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Family Custom)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='TRAGUIN Premium Goa Family Tour Package',
        overview='HERITAGE Welcome to a sun-kissed, multi-generational getaway curated to delight every single member of your group. The Best Goa Tour Package invites your loved ones to dive into a vibrant mix of pristine coastal expanses, architectural marvels, and lively entertainment. This carefully designed Goa Family Tour strikes the perfect balance between action-packed beach excursions and peaceful, culturally rich sights, offering a genuinely refreshing Luxury Goa Holiday. Cherish premium stays, share unforgettable memories, and enjoy a deeply immersive travel experience tailored for your complete relaxation.\n\nTOUR OVERVIEW\nThis elite family vacation is organized as a fully private FIT journey with dedicated, child-friendly and elder- accessible logistics. Your customized schedule features a spacious, private chauffeur-driven executive vehicle that guarantees seamless transfers between your premium beachfront properties. Every moment is crafted around the signature hospitality of TRAGUIN, offering handpicked hotels, excellent meal arrangements, and curated family activities that let you enjoy Goa completely at your own pace.',
        seo_title='GA-002 | TRAGUIN Premium Goa Family Tour Package | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Goa package (GA-002 / TRAGUIN-GA-002): North Goa (2N) • South Goa (2N) - Complete Family Experience.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA & NORTH GOA LEISURE', 1),
            _ih('Day 02: NORTH GOA SIGHTSEEING & ADVENTURE', 2),
            _ih('Day 03: NORTH GOA TO SOUTH GOA VIA SPICE PLANTATION', 3),
            _ih('Day 04: SOUTH GOA HERITAGE & CRUISE', 4),
            _ih('Day 05: SOUTH GOA DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA & NORTH GOA LEISURE',
                (
                    "WELCOME TO COASTAL PARADISE – SEASIDE CHILL & EVENING BEACH WALK Your refreshing Premium Goa Experience starts the moment you land. Upon arrival at Goa Airport, your family will receive a warm welcome from a dedicated TRAGUIN holiday representative. Step into your private, spacious air-conditioned vehicle and enjoy a smooth transfer to your premium resort in North Goa. After check-in, take some time to relax, settle in, and explore the resort's luxury amenities, beach access, and swimming pools. In the late afternoon, enjoy a peaceful family stroll along the golden sands of Calangute or Candolim Beach. Take in the scenic beauty as the sun dips below the horizon, and capture your first family photos of the trip. Beach Walk, Luxury Resort Exploration. with live music. beachfront shacks. Resort)."
                ),
                [
                    'Sightseeing Included: Calangute/Candolim Sunset',
                    'Optional Activities: Evening family beachside dinner',
                    'Evening Experience: Leisure time along the lively',
                    'Overnight Stay: North Goa (Handpicked Luxury Beach',
                ],
            ),            _day(
                2,
                'NORTH GOA SIGHTSEEING & ADVENTURE',
                (
                    'FORTS & FOAMING WAVES – FORT AGUADA, FAMILY WATERSPORTS & SUNSET VIEWS Start your day with a delicious buffet breakfast before heading out for a full day of Goa Sightseeing in the north. Your first stop is the historic 17th-century Fort Aguada. Walk through the well-preserved Portuguese ramparts and climb the iconic lighthouse, which offers panoramic views of the Arabian Sea—a fantastic photography point for families. Next, head to Baga Beach, where your family can choose from a variety of thrilling water activities like banana boat rides, parasailing, and jet skiing, all handled with professional safety gear. Conclude your afternoon with a visit to Anjuna Beach to see its famous rocky coastline, followed by a relaxed family dinner at a trendy clifftop restaurant in Vagator. Anjuna Viewpoint, Vagator Cliffs. Speedboat rides. the sea.'
                ),
                [
                    'Sightseeing Included: Fort Aguada, Baga Beach,',
                    'Optional Activities: Jet-skiing, Parasailing, and',
                    'Evening Experience: Clifftop sunset dining overlooking',
                    'Overnight Stay: North Goa.',
                ],
            ),            _day(
                3,
                'NORTH GOA TO SOUTH GOA VIA SPICE PLANTATION',
                (
                    'SENSES & SPICES – TROPICAL PLANTATION TOUR & PANJIM LATIN QUARTER WALK Check out from North Goa and drive toward the peaceful landscapes of South Goa. Along the way, enjoy an authentic, immersive experience at a lush tropical Spice Plantation in Ponda. Take a guided family walk under the canopy of clove, pepper, and nutmeg trees, and learn about traditional organic farming practices. Savor a traditional Goan buffet lunch served fresh on banana leaves. In the afternoon, enjoy a pleasant walk through Fontainhas in Panaji, the famous Latin Quarter of Goa. Wander past beautifully preserved Portuguese-style homes painted in bright yellows, blues, and reds. This charming neighborhood is one of the top popular Instagram locations in the region. Afterward, cross the river to check into your luxury South Goa resort. Fontainhas Latin Quarter, Panaji Promenade. cashew nuts and handicrafts in Panaji. at your South Goa resort. Haven).'
                ),
                [
                    'Sightseeing Included: Ponda Spice Plantation,',
                    'Optional Activities: Shopping for authentic local',
                    'Evening Experience: Relaxed check-in and leisure time',
                    'Overnight Stay: South Goa (Premium Beachfront',
                ],
            ),            _day(
                4,
                'SOUTH GOA HERITAGE & CRUISE',
                (
                    'HISTORY & MANDOPHIL HARMONIES – OLD GOA CHURCHES & EXCLUSIVE RIVER CRUISE Dedicate your morning to discovering the rich history of South Goa. Visit Old Goa to see the magnificent Basilica of Bom Jesus, a UNESCO World Heritage site that houses the sacred remains of St. Francis Xavier. Directly across the square, admire the grand architecture of the Se Cathedral, famous for its magnificent golden bell. In the afternoon, relax on the pristine, white sands of Colva or Varca Beach, known for its calm and peaceful environment. As evening falls, enjoy a private, scenic boat cruise along the Mandovi River. Relax on board as a family while watching traditional Goan folk dances and listening to live music under the starlit sky. Cathedral, Colva Beach, Mandovi River Cruise. dinner. cruise boat.'
                ),
                [
                    'Sightseeing Included: Basilica of Bom Jesus, Se',
                    'Optional Activities: Private luxury yacht charter with',
                    'Evening Experience: Live cultural music on a river',
                    'Overnight Stay: South Goa.',
                ],
            ),            _day(
                5,
                'SOUTH GOA DEPARTURE',
                (
                    'FOND FAREWELLS – CAPTURING THE LAST COASTAL MOMENTS Enjoy a final, relaxed breakfast at your luxury resort. Spend your morning taking a final dip in the pool or gathering for a family photo on the beach. Depending on your flight schedule, your private vehicle will be available for any last-minute shopping for unique local souvenirs, traditional Bebinca cake, or Goan spices. Your memorable family vacation concludes with a private transfer to Goa Airport, leaving you with beautiful, lasting memories curated carefully by TRAGUIN. transfer.'
                ),
                [
                    'Sightseeing Included: Local souvenir stops, airport',
                    'Meals Included: Premium Buffet Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Lemon Tree Amarante Beach Resort | Heritage Village Resort & Spa',
                'North Goa (2 Nights) / South Goa (2 Nights)',
                '04 Nights',
                'Deluxe',
                'Deluxe Room',
                'CP (Breakfast)',
                4,
                1,
                description='OPTION 01 – DELUXE: Lemon Tree Amarante Beach Resort (North Goa (2 Nights)) | Heritage Village Resort & Spa (South Goa (2 Nights)) | CP (Breakfast)',
            ),
            _hotel(
                'Novotel Goa Resort & Spa | Caravela Beach Resort',
                'North Goa (2 Nights) / South Goa (2 Nights)',
                '04 Nights',
                'Premium',
                'Premium Room',
                'CP (Breakfast)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Novotel Goa Resort & Spa (North Goa (2 Nights)) | Caravela Beach Resort (South Goa (2 Nights)) | CP (Breakfast)',
            ),
            _hotel(
                'Taj Holiday Village Resort & Spa | The Leela Goa (Lagoon Suite)',
                'North Goa (2 Nights) / South Goa (2 Nights)',
                '04 Nights',
                'Luxury',
                'Luxury Villa / Suite',
                'CP (Breakfast)',
                5,
                3,
                description='OPTION 03 – LUXURY: Taj Holiday Village Resort & Spa (North Goa (2 Nights)) | The Leela Goa (Lagoon Suite) (South Goa (2 Nights)) | CP (Breakfast)',
            ),
            _hotel(
                'W Goa (Marvelous Suite) | Taj Exotica Resort & Spa (Sea Villa)',
                'North Goa (2 Nights) / South Goa (2 Nights)',
                '04 Nights',
                'Ultra Luxury',
                'Ultra Luxury Sea Facing',
                'CP + Welcome Mix',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: W Goa (Marvelous Suite) (North Goa (2 Nights)) | Taj Exotica Resort & Spa (Sea Villa) (South Goa (2 Nights)) | CP + Welcome Mix',
            )
        ],
        inclusions=[
            _inc_excluded('Premium accommodations at handpicked beachfront', 1),
            _inc_excluded('family resorts.', 2),
            _inc_excluded("Daily multi-cuisine buffet breakfasts with kids' dining", 3),
            _inc_excluded('options.', 4),
            _inc_excluded('Private executive chauffeur-driven air-conditioned', 5),
            _inc_excluded('vehicle for all transfers.', 6),
            _inc_excluded('Guided plantation tour at Ponda with an authentic', 7),
            _inc_excluded('Goan buffet lunch.', 8),
            _inc_excluded('Complimentary tickets for the evening Mandovi River', 9),
            _inc_excluded('cultural cruise.', 10),
            _inc_excluded('Special family welcome drink and arrival amenities.', 11),
            _inc_excluded('24/7 dedicated TRAGUIN on-ground support.', 12),
            _inc_excluded('Domestic or International flights/train tickets to Goa.', 13),
            _inc_excluded('Monument entry fees, camera costs, and local guide', 14),
            _inc_excluded('Water sports activities (payable directly at the beach', 15),
            _inc_excluded('with safety teams).', 16),
            _inc_excluded('Personal expenses (laundry, long-distance phone', 17),
            _inc_excluded('calls, mini-bar items).', 18),
            _inc_excluded('Mandatory peak season or festival dinner surcharges.', 19),
            _inc_excluded('Personal travel insurance coverage.', 20),
            _inc_excluded('Any services not explicitly listed in the inclusions.', 21),
        ],
    )
    return package, itinerary

def build_ga_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-003'
    tour_code = 'TRAGUIN-GA-003'
    title = 'TRAGUIN Premium Girls Trip Goa Package'
    duration = '03 Nights / 04 Days'
    slug = 'ga-003-girls-trip-goa-package'
    itin_slug = 'ga-003-girls-trip-goa-package-itinerary'
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
            _ph('Serial code GA-003 | TRAGUIN tour code TRAGUIN-GA-003', 1),
            _ph('State / Country: Goa / India | Category: Female Only / Girls Trip', 2),
            _ph('Destinations: North Goa (Baga/Candolim) • South Goa Luxury Excursion', 3),
            _ph('Ideal for: Girls Getaway, Bachelorette Groups', 4),
            _ph('Best season: November to February', 5),
            _ph('Starting price: On Request (Premium Custom)', 6),
            _ph('Vehicle / Meals: Private Luxury Executive SUV', 7),
            _ph('Route: Mopa/Dabolim Airport Arrival → North Goa Chic Beach Circuit → South Goa Heritage', 8),
            _ph('Curated by TRAGUIN Experts: Itineraries tailored to bring you the best in local style, dining, and', 9),
            _ph('Personalized Assistance: Dedicated communication with our support team to help you handle', 10),
            _ph('Premium Handpicked Hotels: Resorts selected for their fantastic locations, top-tier service, and', 11),
            _ph('Luxury Transportation: Private, clean premium vehicles with experienced chauffeurs for', 12),
            _ph('Standard check-in begins at 14:00 hrs, and check-out is at 11:00 hrs across all premium beach resorts.', 13),
            _ph('Please share any club or lounge preferences with us early so we can secure the best table bookings', 14)
        ],
        moods=['Beach', 'Luxury', 'Romantic'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Custom)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='TRAGUIN Premium Girls Trip Goa Package',
        overview="SIZZLE & SISTERHOOD Get ready for an extraordinary beach escape designed entirely for you and your inner circle. The Best Goa Tour Package for an all-female getaway invites your squad to unwind along sun-kissed coastlines, explore high-end beach clubs, and dive into a vibrant tropical paradise. This curated Goa Honeymoon Package or exclusive girl group itinerary seamlessly blends luxury beachside relaxation with sophisticated nightlife, boutique shopping, and stunning backdrops. Experience a true Luxury Goa Holiday where your safety, comfort, and celebration come together perfectly.\n\nTOUR OVERVIEW\nThis premium getaway is customized as an independent, private FIT tour with an emphasis on style, safety, and curated lifestyle experiences. Your squad will travel in a dedicated private executive vehicle with a professional, vetted chauffeur throughout the journey. From high-end beach stays and handpicked hotels to exclusive entry reservations at legendary sunset lounges, every detail is seamlessly managed by TRAGUIN to give you unforgettable memories and a flawlessly executed vacation.\n\nWHY CHOOSE A PREMIUM GOA EXPERIENCE?\nA Goa Family Tour or an all-girls escape brings you straight to the heart of India's most vibrant coastal lifestyle. Home to the legendary Top Tourist Places in Goa, this beautiful destination blends Portuguese- inspired heritage with breathtaking landscapes and dynamic seaside energy. From taking photos at popular Instagram locations like Fontainhas and modern oceanfront infinity pools to discovering hidden bohemian boutiques, this trip has it all. Whether you are looking for the excitement of premium water sports, a relaxing high-end spa afternoon, or top-tier dining, our unique TRAGUIN Goa Packages unlock exclusive experiences, luxury hospitality, and endless fun.",
        seo_title='GA-003 | TRAGUIN Premium Girls Trip Goa Package | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Goa package (GA-003 / TRAGUIN-GA-003): North Goa (Baga/Candolim) • South Goa Luxury Excursion.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA & SUNSETS', 1),
            _ih('Day 02: NORTH GOA CHIC EXPLORATION', 2),
            _ih('Day 03: FONTAINHAS & SOUTH GOA CRUISE', 3),
            _ih('Day 04: CAFÉ CULTURE & DEPARTURE', 4)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA & SUNSETS',
                (
                    'WELCOME TO PARADISE – PREMIUM ARRIVAL, CHIC LOUNGE & SUNSET VIBES Your ultimate girl-power vacation begins with a warm, stylish welcome. Arrive at Goa Airport, where your professional, private chauffeur will greet you with custom refreshments and hand over your exclusive TRAGUIN welcome kits. Sit back and enjoy a smooth drive to your premium beach resort in North Goa, chosen for its chic design, top-tier amenities, and excellent security. After checking in and unpacking your favorite vacation looks, head out for a memorable evening. We have reserved a premium table for your squad at an iconic oceanfront venue like Thalassa or Antares in Vagator. Sip artisan cocktails, savor fresh Mediterranean dishes, and enjoy a spectacular sunset view over the cliffs—a perfect photo point to kick off your trip. Cliffs, Ozran Beach sunset views. group photoshoot. music at a cliffside beach lounge. Beach Resort).'
                ),
                [
                    'Sightseeing Included: Vagator Panoramic Coastal',
                    'Optional Activities: Dedicated professional beachside',
                    'Evening Experience: Premium sunset dining and',
                    'Overnight Stay: North Goa (Handpicked Premium',
                ],
            ),            _day(
                2,
                'NORTH GOA CHIC EXPLORATION',
                (
                    "COASTAL SIZZLE – SIGHTSEEING, BOUTIQUE MARKET SHOPPING & PREMIUM BEACH CLUBBING Start your day with a delicious multi-cuisine breakfast by the pool before heading out for a fun day of Goa Sightseeing. Take a morning walk through the historic Aguada Fort complex to enjoy stunning panoramic views of the Arabian Sea. Next, head to the chic boutiques of Assagao, often called the 'South Kensington of Goa,' to browse high-end resort wear, indie jewelry, and beautiful home decor. Spend your afternoon at a luxury beach club, such as Purple Martini or Titlie, relaxing on premium daybeds, enjoying great music, and tasting delicious fusion food. As night falls, dive into Goa's famous nightlife at an exclusive club like Tito’s Lane or a stylish speakeasy, with safe private transfers arranged for you. Assagao Boutique District. parasailing at Calangute. club with dedicated transport."
                ),
                [
                    'Sightseeing Included: Fort Aguada, Sinquerim Beach,',
                    'Optional Activities: Thrilling luxury jet-skiing or',
                    'Evening Experience: VIP table access at a premium',
                    'Overnight Stay: North Goa Beach Resort.',
                ],
            ),            _day(
                3,
                'FONTAINHAS & SOUTH GOA CRUISE',
                (
                    'LATIN QUARTERS & YACHT CHIC – INSTAGRAMMABLE HERITAGE & PRIVATE CATAMARAN ESCAPE Discover the rich history and culture of Goa today. After breakfast, head to Panaji to explore Fontainhas, the famous old Latin Quarter. Take a gentle walk among beautiful Portuguese-style homes painted in bright yellows, blues, and maroons. This is one of the top popular Instagram locations in the region, perfect for capturing colorful group photos. In the afternoon, head to the Mandovi River for an exclusive luxury experience: a private catamaran yacht cruise arranged just for your group. Enjoy your favorite music, light snacks, and cold beverages while sailing along the beautiful coast as the sun sets over the ocean, making for an unforgettable highlight of your trip. Panjim Church, Miramar Beach coastline. Goan feni. private luxury yacht.'
                ),
                [
                    'Sightseeing Included: Fontainhas Latin Quarter,',
                    'Optional Activities: Private guided tasting tour of local',
                    'Evening Experience: Sunset celebration aboard your',
                    'Overnight Stay: North Goa Beach Resort.',
                ],
            ),            _day(
                4,
                'CAFÉ CULTURE & DEPARTURE',
                (
                    "BRUNCH VIBES & ROYAL FAREWELL – MEMORIES BEYOND DESTINATIONS Enjoy a relaxed morning at your resort, sleeping in or taking a final dip in the pool. After checking out, your private chauffeur will take your group to one of Goa's trendy brunch spots, like Baba Au Rhum or Mojigao, nestled in a lush tropical forest. Enjoy freshly baked pastries, artisanal coffee, and great conversation as you look back on your amazing trip. Afterward, pick up any last-minute local treats or souvenirs, like spiced cashews and local bebinca, before a smooth transfer to the airport for your journey home. Your premium holiday concludes seamlessly, leaving you with beautiful, lifelong memories curated by TRAGUIN. gourmet shops."
                ),
                [
                    'Sightseeing Included: Bohemian café hubs, local',
                    'Meals Included: Premium Gourmet Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Lemon Tree Amarante Beach Resort / Hard Rock Hotel Goa',
                'North Goa (3 Nights)',
                '03 Nights',
                'Deluxe',
                'Superior Deluxe Room',
                'CP (Includes Breakfast)',
                4,
                1,
                description='OPTION 01 – DELUXE: Lemon Tree Amarante Beach Resort / Hard Rock Hotel Goa (North Goa (3 Nights)) | CP (Includes Breakfast)',
            ),
            _hotel(
                'Novotel Goa Resort & Spa / Fairfield by Marriott Anjuna',
                'North Goa (3 Nights)',
                '03 Nights',
                'Premium',
                'Premium Balcony Room',
                'CP (Includes Breakfast)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Novotel Goa Resort & Spa / Fairfield by Marriott Anjuna (North Goa (3 Nights)) | CP (Includes Breakfast)',
            ),
            _hotel(
                'W Goa (Vagator) / Taj Holiday Village Resort & Spa',
                'North Goa (3 Nights)',
                '03 Nights',
                'Luxury',
                'Wonderful Room / Luxury Cottage',
                'CP (Includes Breakfast)',
                5,
                3,
                description='OPTION 03 – LUXURY: W Goa (Vagator) / Taj Holiday Village Resort & Spa (North Goa (3 Nights)) | CP (Includes Breakfast)',
            ),
            _hotel(
                'The Leela Goa (Club Suites) / Taj Exotica Resort & Spa',
                'North Goa (3 Nights)',
                '03 Nights',
                'Ultra Luxury',
                'Private Plunge Pool Villa',
                'CP + Welcome Champagne',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Leela Goa (Club Suites) / Taj Exotica Resort & Spa (North Goa (3 Nights)) | CP + Welcome Champagne',
            )
        ],
        inclusions=[
            _inc_excluded('Chic hotel stays at highly rated, secure premium', 1),
            _inc_excluded('resorts.', 2),
            _inc_excluded('Daily gourmet buffet breakfast with refreshing morning', 3),
            _inc_excluded('mocktails.', 4),
            _inc_excluded('Dedicated private luxury executive vehicle throughout', 5),
            _inc_excluded('the trip.', 6),
            _inc_excluded('Pre-reserved sunset table booking at a premier beach', 7),
            _inc_excluded('lounge.', 8),
            _inc_excluded('All road taxes, parking fees, fuel costs, and driver', 9),
            _inc_excluded('allowances.', 10),
            _inc_excluded('Complimentary welcome drinks and custom squad', 11),
            _inc_excluded('amenities.', 12),
            _inc_excluded('24/7 priority concierge support from the TRAGUIN', 13),
            _inc_excluded('Domestic or International flights and airport terminal', 14),
            _inc_excluded('taxes.', 15),
            _inc_excluded('Food and beverage costs at clubs, unless specified.', 16),
            _inc_excluded('Monument entry tickets, camera fees, and water', 17),
            _inc_excluded('sports rides.', 18),
            _inc_excluded('Personal expenses like laundry, room service, and', 19),
            _inc_excluded('mini-bar items.', 20),
            _inc_excluded('Surcharges for holiday weekends or special party', 21),
            _inc_excluded('nights.', 22),
            _inc_excluded('Personal travel insurance.', 23),
            _inc_excluded('Any services not listed under the inclusions section.', 24),
        ],
    )
    return package, itinerary

def build_ga_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-004'
    tour_code = 'TRAGUIN-GA-004'
    title = 'TRAGUIN Premium Goa Tour Package — Luxury South Goa Private Sanctuary'
    duration = '05 Nights / 06 Days'
    slug = 'ga-004-luxury-south-goa-private-sanctuary'
    itin_slug = 'ga-004-luxury-south-goa-private-sanctuary-itinerary'
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
            _ph('Serial code GA-004 | TRAGUIN tour code TRAGUIN-GA-004', 1),
            _ph('State / Country: Goa / India | Category: Luxury Holiday', 2),
            _ph('Destinations: Luxury South Goa (5N) - Elite Coastal Escape', 3),
            _ph('Ideal for: Couples, Families, Connoisseurs', 4),
            _ph('Best season: November to February', 5),
            _ph('Starting price: On Request (Ultra Luxury Custom)', 6),
            _ph('Vehicle / Meals: Private Luxury SUV', 7),
            _ph('Route: Goa Airport Arrival → Luxury South Goa Beachfront Resort Sanctuary → Curated', 8),
            _ph('TRAGUIN Signature Experience: A private, luxury chartered yacht cruise complete with champagne', 9),
            _ph('Curated by TRAGUIN Experts: Handpicked five-star beachfront resorts chosen for their exceptional', 10),
            _ph('Personalized Assistance: Round-the-clock contact with our luxury travel coordinators to handle any', 11),
            _ph('Luxury Transportation: Premium, private SUVs driven by professional, courteous chauffeurs who', 12),
            _ph('South Goa Boutiques: Explore high-end lifestyle boutiques in Margao and Panaji for customized linen resort- wear, organic coconut-oil beauty products, and handmade azulejos tiles. Food & Cafes: We recommend visiting fine-dining restaurants like Cavatina in Benaulim for a modern take on classic Goan food, or stopping by artisanal bakeries in Fontainhas for traditional treats.', 13),
            _ph('Standard check-in begins at 15:00 hrs, and check-out is at 11:00 hrs across all major luxury beach resorts.', 14)
        ],
        moods=['Luxury', 'Beach', 'Romantic', 'Family'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Ultra Luxury Custom)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Luxury South Goa Private Sanctuary',
        overview='Welcome to a masterfully designed tropical retreat where pristine white sands, swaying palms, and endless azure ocean views unite. The Best Goa Tour Package invites you to step away from the everyday and immerse yourself in the tranquil, exclusive luxury of South Goa. Perfect as a high-end Goa Honeymoon Package or an elegant Goa Family Tour, this journey balances peaceful relaxation with curated cultural discoveries. Experience a true Luxury Goa Holiday where world-class beach resorts and refined coastal living create a spectacular canvas for your vacation.\n\nTOUR OVERVIEW\nThis elite coastal holiday is curated as an independent FIT tour, designed for travelers who value complete privacy, flexibility, and unmatched elegance. Your escape features a dedicated, professional chauffeur-driven luxury vehicle for all transfers and evening excursions. Every element is brought together by the signature hospitality of TRAGUIN, guaranteeing bespoke comfort, stays at finest handpicked hotels, and unique immersive experiences that create unforgettable memories.\n\nTHE ESSENCE OF A PREMIUM GOA EXPERIENCE\nWhy choose South Goa for your luxury holiday? While the north pulses with high-energy crowds, South Goa is celebrated for its breathtaking landscapes, clean shores, and peaceful, old-world charm. It features the most sought-after Top Tourist Places in Goa, including majestic heritage mansions and quiet spice plantations. From finding beautiful, popular Instagram locations along the cliffs of Cabo de Rama to tasting fresh seafood at private, upscale beachfront shacks, our tailored TRAGUIN Goa Packages offer a wonderful blend of relaxation, adventure, and culture. It is simply the Best Time to Visit Goa to enjoy a sophisticated beach retreat.',
        seo_title='GA-004 | Goa | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Goa package (GA-004 / TRAGUIN-GA-004): Luxury South Goa (5N) - Elite Coastal Escape.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA – WELCOME TO PARADISE', 1),
            _ih('Day 02: SOUTH GOA CULTURE & HERITAGE EXPLORATION', 2),
            _ih('Day 03: COASTAL CASTLES & HIDDEN HORIZONS', 3),
            _ih('Day 04: PRIVATE LUXURY YACHT CRUISE EXPERIENCE', 4),
            _ih('Day 05: OLD GOA SPIRITUAL SPLENDOR & FONTAINHAS ART WALKS', 5),
            _ih('Day 06: LEISURELY DEPARTURE FROM GOA', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA – WELCOME TO PARADISE',
                (
                    "ELITE TROPICAL RECEPTION & PRIVATE BEACHFRONT SUNSET REST Your ultimate luxury getaway begins the moment you touch down. Upon arrival at Goa Airport, receive a warm, private welcome arranged under exclusive TRAGUIN guest protocols. Your professional chauffeur will escort you to a luxury private vehicle, refreshing you with chilled towels and artisanal beverages en route to your five-star beach resort in South Goa. After a seamless check-in to your premium ocean-view suite, spend the afternoon relaxing amidst the resort's lush tropical gardens or grand infinity pools. In the late afternoon, take a peaceful stroll along the soft sands of Varca or Cavelossim Beach. As the sun dips below the horizon, enjoy your first sunset with a complimentary glass of fine wine at a private beachfront pavilion. resort luxury facilities. massage. table arrangement. Resort)."
                ),
                [
                    'Sightseeing Included: Private beachfront access,',
                    "Optional Activities: In-room therapeutic couple's",
                    'Evening Experience: Fine-dining beachside candlelit',
                    'Overnight Stay: South Goa (Handpicked Ultra-Luxury',
                ],
            ),            _day(
                2,
                'SOUTH GOA CULTURE & HERITAGE EXPLORATION',
                (
                    'PORTUGUESE NOBILITY – COLONIAL MANSIONS & RAINFOREST SPICE IMMERSION Savor a magnificent breakfast before embarking on a curated day of Goa Sightseeing. Your morning features a private guided visit to the spectacular Palacio do Deao in Quepem, a 213-year-old historic mansion blending Portuguese and Indian architecture. Walk through its lush, formal pleasure gardens and enjoy heritage tea on a terrace overlooking the Kushavati River. Next, head deep into the green hills for an immersive experience at a premium, organic spice plantation. Take a gentle, private walking tour to learn about local flora, vanilla pods, and fresh cardamoms. Conclude your tour with an authentic, traditional Goan buffet lunch served in earthen pots, creating a beautiful blend of local flavors. Organic Spice Plantation, Quepem Heritage Valley. (subject to availability). lounge listening to live jazz performance.'
                ),
                [
                    'Sightseeing Included: Palacio do Deao, Premium',
                    'Optional Activities: Elephant bathing experience',
                    'Evening Experience: Relaxed evening by the resort',
                    'Overnight Stay: South Goa.',
                ],
            ),            _day(
                3,
                'COASTAL CASTLES & HIDDEN HORIZONS',
                (
                    'THE CLIFFS OF CABO DE RAMA – SECLUDED VISTAS & INSTAGRAM SPOTLIGHTS Enjoy a leisurely morning by the ocean before driving south to Cabo de Rama Fort. Perched dramatically over steep sea cliffs, this historic fortress offers sweeping, panoramic views of the Arabian Sea. It is a fantastic photography point and one of the most celebrated popular Instagram locations in the region. After taking in the stunning views, descend to a boutique cliffside beach club for a relaxed gourmet lunch. Spend the afternoon resting on private sun loungers, listening to the waves crash below, and soaking in the majestic coastal beauty. Panoramic Viewpoints. overlooking the sea cliffs.'
                ),
                [
                    'Sightseeing Included: Cabo de Rama Fort, Cliffside',
                    'Optional Activities: Guided sea-kayaking near the bay.',
                    'Evening Experience: Premium sunset cocktails',
                    'Overnight Stay: South Goa.',
                ],
            ),            _day(
                4,
                'PRIVATE LUXURY YACHT CRUISE EXPERIENCE',
                (
                    'SAILING THE AZURE WATERWAYS – PRIVATE CHARTER & DOLPHIN WATCHING Today offers a truly unforgettable highlight of your Premium Goa Experience. Late in the morning, travel to a private jetty to board an exclusive, luxury chartered yacht. Cruise along the calm river backwaters and out into the open sea, enjoying absolute privacy and attentive service. Sip on fine champagne and enjoy delicious canapés as you spot dolphins playing in the water. Drop anchor near a quiet, secluded cove for a private swim or a gourmet lunch prepared onboard by your personal chef. Return to land just after sunset, having experienced the coast from a beautiful new perspective. habitats, Mandovi/Zuari river mouths. the yacht deck. winning resort restaurant.'
                ),
                [
                    'Sightseeing Included: Secluded coastal coves, dolphin',
                    'Optional Activities: Deep-sea fishing or jet-skiing from',
                    'Evening Experience: Gourmet dinner at an award-',
                    'Overnight Stay: South Goa.',
                ],
            ),            _day(
                5,
                'OLD GOA SPIRITUAL SPLENDOR & FONTAINHAS ART WALKS',
                (
                    'HISTORIC BASILICAS & LATIN QUARTER VIBRANCY – ARCHITECTURE & ART Venture out to discover the timeless architecture of Old Goa. Visit the world-famous Basilica of Bom Jesus, a UNESCO World Heritage Site that showcases fine Baroque architecture. Next, explore the grand Se Cathedral, taking in its peaceful atmosphere and historic chapels. In the afternoon, enjoy a private guided walking tour through Fontainhas, the old Latin Quarter of Panaji. Stroll past brightly colored Portuguese-style houses with elegant overhanging balconies. Stop to visit a local contemporary art gallery and relax at a boutique café for classic Portuguese egg tarts and freshly brewed local coffee. Cathedral, Fontainhas Latin Quarter. Goan curator. highlighting modern Goan food.'
                ),
                [
                    'Sightseeing Included: Basilica of Bom Jesus, Se',
                    'Optional Activities: Private art buying session with a',
                    'Evening Experience: A curated, upscale tasting dinner',
                    'Overnight Stay: South Goa.',
                ],
            ),            _day(
                6,
                'LEISURELY DEPARTURE FROM GOA',
                (
                    'FINAL OCEAN DIP & FOND FAREWELLS TO THE COAST Enjoy a relaxed morning at your own pace. Take a final swim in the warm ocean, walk along the pristine beach, or enjoy a long breakfast on the sun terrace. Check out of your room by mid-day. Depending on your flight time, your private vehicle is available for a visit to a luxury lifestyle boutique for fine resort-wear, artisanal feni, or local organic crafts. Your memorable journey concludes as you are transferred smoothly to Goa Airport, taking with you beautiful, lifelong memories curated by TRAGUIN. premium boutiques.'
                ),
                [
                    'Sightseeing Included: Resort beach access, local',
                    'Meals Included: Premium Buffet Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Caravela Beach Resort / ITC Grand Goa (Garden view)',
                'South Goa (5 Nights)',
                '05 Nights',
                'Deluxe',
                'Superior Garden Room',
                'CP (Breakfast)',
                4,
                1,
                description='OPTION 01 – DELUXE: Caravela Beach Resort / ITC Grand Goa (Garden view) (South Goa (5 Nights)) | CP (Breakfast)',
            ),
            _hotel(
                'The Leela Goa / Alila Diwa Goa',
                'South Goa (5 Nights)',
                '05 Nights',
                'Premium',
                'Premier Garden View Room',
                'CP (Breakfast)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Leela Goa / Alila Diwa Goa (South Goa (5 Nights)) | CP (Breakfast)',
            ),
            _hotel(
                'Taj Exotica Resort & Spa, Goa',
                'South Goa (5 Nights)',
                '05 Nights',
                'Luxury',
                'Luxury Ocean View Room',
                'CP (Breakfast)',
                5,
                3,
                description='OPTION 03 – LUXURY: Taj Exotica Resort & Spa, Goa (South Goa (5 Nights)) | CP (Breakfast)',
            ),
            _hotel(
                'The Leela Goa (The Club Sanctuaries) / Taj Exotica (Plunge Pool Villa)',
                'South Goa (5 Nights)',
                '05 Nights',
                'Ultra Luxury',
                'Exclusive Club Suite / Luxury Villa',
                'CP + Private Butler',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Leela Goa (The Club Sanctuaries) / Taj Exotica (Plunge Pool Villa) (South Goa (5 Nights)) | CP + Private Butler',
            )
        ],
        inclusions=[
            _inc_excluded('Five-star ultra-luxury beachfront resort', 1),
            _inc_excluded('accommodations.', 2),
            _inc_excluded('Daily premium multi-cuisine buffet breakfasts.', 3),
            _inc_excluded('Dedicated private luxury SUV with a professional', 4),
            _inc_excluded('chauffeur.', 5),
            _inc_excluded('Complimentary 4-hour private chartered luxury yacht', 6),
            _inc_excluded('cruise.', 7),
            _inc_excluded('All airport transfers, parking fees, tolls, and driver', 8),
            _inc_excluded('allowances.', 9),
            _inc_excluded('Traditional Goan welcome drink and premium', 10),
            _inc_excluded('seasonal fruit platters.', 11),
            _inc_excluded('24/7 dedicated TRAGUIN concierge support.', 12),
            _inc_excluded('Domestic or International airfares to/from Goa.', 13),
            _inc_excluded('Monument entrance tickets, heritage guide fees, and', 14),
            _inc_excluded('camera permits.', 15),
            _inc_excluded('Personal expenses (such as laundry, long-distance', 16),
            _inc_excluded('phone calls, mini-bar items).', 17),
            _inc_excluded('Meals and drinks not explicitly listed in the inclusions.', 18),
            _inc_excluded('Surcharges for peak holiday dates, Christmas, or New', 19),
            _inc_excluded('Year gala dinners.', 20),
            _inc_excluded('Travel and comprehensive medical insurance', 21),
            _inc_excluded('coverage.', 22),
            _inc_excluded('Any extra activities not detailed in the itinerary.', 23),
        ],
    )
    return package, itinerary

def build_ga_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-005'
    tour_code = 'TRAGUIN-GA-005-LUX'
    title = 'TRAGUIN Premium Goa Tour Package — Leisure Goa for Senior Citizens'
    duration = '04 Nights / 05 Days'
    slug = 'ga-005-leisure-goa-senior-citizens'
    itin_slug = 'ga-005-leisure-goa-senior-citizens-itinerary'
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
            _ph('Serial code GA-005 | TRAGUIN tour code TRAGUIN-GA-005-LUX', 1),
            _ph('State / Country: Goa / India | Category: Senior Citizen / Leisure Goa', 2),
            _ph('Destinations: North Goa • South Goa', 3),
            _ph('Ideal for: Senior Citizens, Couples, Leisure Seekers', 4),
            _ph('Best season: October to May (Monsoon Leisure: June to September)', 5),
            _ph('Starting price: On Request (Premium Tier Pricing)', 6),
            _ph('Vehicle / Meals: Private Premium Innova', 7),
            _ph('Route: Mopa or Dabolim Airport • South Goa Coastal Belt • Old Goa Heritage District • Panaji • Return', 8),
            _ph('TRAGUIN Signature Experience: Private, smooth, crowd-free access routes to all cultural monuments and heritage', 9),
            _ph('Curated by TRAGUIN Experts: An itinerary thoughtfully designed with minimal walking, frequent rest stops, and', 10),
            _ph('Premium Handpicked Hotels: Properties meticulously chosen based on stringent comfort, luxury, safety, and', 11),
            _ph('Goa is renowned for its iconic local specialties. Your private vehicle is at your disposal to visit the calm, state-run emporiums where you can shop stress-free for the highest-grade Goan cashews, artisanal hand-painted Azulejos ceramic tiles, premium spice baskets, and pure organic coconut oils. For food lovers, your driver will introduce you to beautiful, tranquil heritage cafes that serve perfectly mild, authentic Goan vegetable curries and delicious bibinca desserts.', 12),
            _ph('Hotel Policies: Standard check-in is at 14:00 hrs and check-out is at 11:00 hrs. Early check-in requests are subject to', 13)
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
        price_note='On Request (Premium Tier Pricing)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Leisure Goa for Senior Citizens',
        overview="L E I S U R E G O A F O R S E N I O R C I T I Z E N S • 0 4 N I G H T S / 0 5 D AY S SERIAL CODE: GA-005 STATE / COUNTRY: Goa / India CATEGORY: Senior Citizen / Leisure Goa DURATION: 04 Nights / 05 Days DESTINATIONS COVERED: South Goa (Serene Heritage) & North Goa (Tranquil Escapes) IDEAL FOR: Senior Citizens, Couples, Leisure Seekers BEST SEASON: October to May (Monsoon Leisure: June to September) STARTING PRICE: On Request (Premium Tier Pricing) TRAGUIN TOUR CODE: TRAGUIN-GA-005-LUX\n\nTOUR OVERVIEW\nWelcome to an elite, meticulously crafted escape designed exclusively by TRAGUIN. This Best Goa Tour Package is structured specifically for senior citizens who wish to experience the coastal paradise at a relaxed, unhurried pace. From the architectural grandeur of Old Goa's legendary churches to the soul-soothing, sun- dappled sands of South Goa beaches, every element of this itinerary guarantees absolute comfort, safety, and immersive luxury. Travel effortlessly in a private, temperature-controlled vehicle, stay in handpicked premium resorts featuring world-class accessibility, and let the classic elegance of Goa create unforgettable memories for you. TRA GUIN TRAGUIN Premium Luxury Holidays\n\nDESTINATION SEO CONTENT & INSIGHTS\nGoa, universally celebrated for its breathtaking landscapes and harmonious blend of Indo-Portuguese history, offers an unparalleled sanctuary for mature travelers seeking a peaceful holiday. Choosing a specialized Goa Honeymoon Package or a relaxed Goa Family Tour with us ensures you avoid the chaotic party crowds and instead dive deep into the cultural heart and scenic beauty of India’s most iconic coastal state. This comprehensive Luxury Goa Holiday centers around slow-paced exploration, minimal walking distances, smooth transfers, and premium stays. Why Visit Goa for Leisure? Beyond its energetic nightlife lies a tranquil, spiritual world of historic Latin quarters, serene riverside cruises, spice plantations alive with aroma, and pristine beaches with gentle waves. It is highly regarded as one of the top destinations for health-focused, relaxing vacations where the sea breeze works wonders for rejuvenation. Famous Attractions & Most Searched Experiences: Explore iconic architectural landmarks like the Basilica of Bom Jesus and Se Cathedral, take in the majestic sights of Miramar Beach, and experience the cultural charm of the Fontainhas Latin Quarter. Enjoy popular Instagram locations such as the colorful Portuguese houses and the stunning, gentle backwaters of the Mandovi River, all while savoring authentic, non-spicy Goan culinary masterpieces designed for discerning palates. Best Time to Visit Goa: While November to February remains the absolute peak season for Goa Sightseeing, the shoulder months of October and March offer incredibly pleasant weather with fewer tourists, making it the perfect timeframe for senior citizens to relish the top tourist places in Goa in complete tranquility.",
        seo_title='GA-005 | Goa | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Goa package (GA-005 / TRAGUIN-GA-005-LUX): North Goa • South Goa.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA – WELCOME TO THE LAND OF SOULFUL SERENITY', 1),
            _ih('Day 02: OLD GOA HERITAGE & THE SPIRITUAL SOUL OF THE SOUTH', 2),
            _ih('Day 03: MANAFUL MANDOVI RIVER CRUISE & PANAJI PROMENADE', 3),
            _ih('Day 04: NORTH GOA TRANQUILITY & HANDCRAFTED SOUVENIR SHOPPING', 4),
            _ih('Day 05: DEPARTURE WITH CHERISHED FOREVER MEMORIES', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA – WELCOME TO THE LAND OF SOULFUL SERENITY',
                (
                    'Arrive at Manohar International Airport (Mopa) or Dabolim Airport, where your professional, courteous chauffeur will warmly welcome you, displaying a personalized TRAGUIN placard. Step into your premium, air-conditioned luxury vehicle, fully equipped with refreshing amenities and specialized seating comfort. Enjoy a highly scenic, smooth drive past swaying coconut grooves and traditional Goan villages as you make your way to your handpicked beachside luxury resort in South Goa. Upon arrival, skip the standard queues with our pre-arranged private check-in service. Sip on a refreshing, signature tropical welcome drink and settle comfortably into your elegantly appointed room designed for maximum relaxation. Spend the late afternoon resting and soaking in the premium resort amenities. TRAGUIN Premium Luxury Holidays Sightseeing Included: Chauffeur-driven airport transfer, scenic countryside drive. magnificent, glowing golden sunset over the Arabian Sea.'
                ),
                [
                    'Evening Experience: A gentle, slow-paced stroll along the soft, private sands of Utorda or Varca Beach to witness a',
                    'Overnight Stay: Luxury Beach Resort & Spa, South Goa.',
                    'Meals Included: Dinner (Curated light gourmet buffet at the resort’s fine dining restaurant).',
                ],
            ),            _day(
                2,
                'OLD GOA HERITAGE & THE SPIRITUAL SOUL OF THE SOUTH',
                (
                    'Awaken to the soothing sounds of birds and the gentle ocean tide. Enjoy a lavish, healthy breakfast spread at the resort. Today, embark on a wonderfully relaxed Goa Sightseeing tour focused on Old Goa’s iconic spiritual history. Your first stop is the magnificent Basilica of Bom Jesus, a UNESCO World Heritage site known for its awe-inspiring baroque architecture and profound serenity. With minimal walking required from the vehicle drop-off point, you can easily admire its historic beauty. Directly across the beautifully landscaped square sits the monumental Se Cathedral, celebrated for its majestic Golden Bell. Afterward, take a leisurely drive through the legendary Fontainhas Latin Quarter in Panaji, marveling at the bright, impeccably preserved Portuguese houses. Conclude the afternoon with a specially organized traditional lunch at a lush, organic spice plantation, where you will receive a warm, aromatic welcome. Sightseeing Included: Basilica of Bom Jesus, Se Cathedral, Fontainhas Latin Quarter, Heritage Spice Plantation Tour. music.'
                ),
                [
                    'Optional Activities: A gentle elephant interaction and traditional Ayurvedic foot reflexology session at the spice farm.',
                    'Evening Experience: A relaxed, accessible evening back at your premium resort, enjoying light, soothing live instrumental',
                    'Overnight Stay: Luxury Beach Resort & Spa, South Goa.',
                    'Meals Included: Breakfast & Dinner (Resort) + Specialized Traditional Lunch at the Spice Plantation.',
                ],
            ),            _day(
                3,
                'MANAFUL MANDOVI RIVER CRUISE & PANAJI PROMENADE',
                (
                    "Indulge in a late, leisurely breakfast at your own pace. The morning is yours to fully experience the resort’s premium wellness facilities, take a gentle dip in the temperature-controlled pool, or sit comfortably with a book amidst the beautifully manicured tropical gardens. In the mid-afternoon, take a pleasant drive toward Panaji to explore the scenic Miramar Beach and its elegant waterfront promenade. As the sun begins to lower, board a highly exclusive, double- decker luxury cruise boat on the calm waters of the Mandovi River. Relax in comfortable, reserved premium seats on the deck, enjoying gentle sea breezes, live traditional Goan manddo folk music, and classic Portuguese dance performances. The cruise offers breathtaking photography points to capture the glowing illuminated coastline of Goa's capital city. Sightseeing Included: Miramar Beach Waterfront, Sunset Mandovi River Cruise. TRAGUIN Premium Luxury Holidays"
                ),
                [
                    'Evening Experience: A relaxed driving tour of Panaji city under twinkling evening lights, followed by a gourmet dinner.',
                    'Overnight Stay: Luxury Beach Resort & Spa, South Goa.',
                    'Meals Included: Breakfast & Dinner (Resort).',
                ],
            ),            _day(
                4,
                'NORTH GOA TRANQUILITY & HANDCRAFTED SOUVENIR SHOPPING',
                (
                    'Following a delightful breakfast, your dedicated chauffeur will guide you on a custom-paced journey to the highly picturesque regions of North Goa. Designed to avoid steep climbs or crowded spots, this tour focuses entirely on scenic beauty. Visit the historic Aguada Fort area, stopping at a stunning, easily accessible panoramic viewpoint that overlooks the endless blue ocean. Next, take a gentle drive along the famous Calangute and Candolim coastal roads, pausing to enjoy a premium lunch at a beautifully restored, beachside heritage cafe. The afternoon is dedicated to a relaxed shopping experience at premium government-approved handicraft emporiums. Here, you can comfortably browse for authentic Goan cashew nuts, world-renowned local feni, handcrafted ceramics, and beautiful traditional textiles to take home as precious keepsakes. Sightseeing Included: Aguada Scenic Point, Candolim Heritage Drive, Premium Handicrafts Emporium. night.'
                ),
                [
                    'Optional Activities: High Tea at an award-winning Indo-Portuguese villa converted into a luxury cafe.',
                    "Evening Experience: A special Farewell Gala Dinner hosted inside the resort's premium restaurant to celebrate your final",
                    'Overnight Stay: Luxury Beach Resort & Spa, South Goa.',
                    'Meals Included: Breakfast & Premium Farewell Dinner.',
                ],
            ),            _day(
                5,
                'DEPARTURE WITH CHERISHED FOREVER MEMORIES',
                (
                    'Your beautiful, leisurely journey comes to a seamless conclusion today. Enjoy a relaxed, final breakfast at the resort, savoring freshly brewed coffee and premium global cuisine. Take some time to capture beautiful photos in the resort’s lush gardens alongside your dedicated travel companions. Complete your smooth, late check-out with the full assistance of our concierge team. Your private chauffeur will then arrive to transfer you comfortably to Manohar International Airport (Mopa) or Dabolim Airport for your journey home. Depart with a rejuvenated spirit, a smile on your face, and beautiful memories of your premium holiday, thoughtfully curated by the travel experts at TRAGUIN. Sightseeing Included: Private airport drop-off via luxury vehicle. TRAGUIN Premium Luxury Holidays'
                ),
                [
                    'Meals Included: Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Heritage Village Resort & Spa, South Goa',
                'South Goa (4 Nights)',
                '04 Nights',
                'Deluxe',
                'Superior Garden View Room',
                'Breakfast & Dinner (MAP)',
                4,
                1,
                description='OPTION 01 – DELUXE: Heritage Village Resort & Spa, South Goa (South Goa (4 Nights)) | Breakfast & Dinner (MAP)',
            ),
            _hotel(
                'ITC Grand Goa, a Luxury Collection Resort',
                'South Goa (4 Nights)',
                '04 Nights',
                'Premium',
                'Garden View Room with Balcony',
                'Breakfast & Dinner (MAP)',
                4,
                2,
                description='OPTION 02 – PREMIUM: ITC Grand Goa, a Luxury Collection Resort (South Goa (4 Nights)) | Breakfast & Dinner (MAP)',
            ),
            _hotel(
                'The Leela Goa, Cavelossim',
                'South Goa (4 Nights)',
                '04 Nights',
                'Luxury',
                'Lagoon Terrace Suite',
                'Premium Curated Breakfast & Dinner',
                5,
                3,
                description='OPTION 03 – LUXURY: The Leela Goa, Cavelossim (South Goa (4 Nights)) | Premium Curated Breakfast & Dinner',
            ),
            _hotel(
                'Taj Exotica Resort & Spa, Benaulim',
                'South Goa (4 Nights)',
                '04 Nights',
                'Ultra Luxury',
                'Luxury Plunge Pool Villa',
                'Bespoke Personalized Dining Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Taj Exotica Resort & Spa, Benaulim (South Goa (4 Nights)) | Bespoke Personalized Dining Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Premium Accommodation: 04 Nights’ luxurious stay at handpicked elite resorts featuring ground-floor access and', 1),
            _inc_excluded('senior-citizen friendly design elements.', 2),
            _inc_excluded('Meals Plan: Nutritious, expertly prepared daily breakfasts and dinners as specified in the hotel tier matrix.', 3),
            _inc_excluded('Luxury Transfers: All private airport pick-ups, drops, and day-wise sightseeing transfers via an elite, air-', 4),
            _inc_excluded('conditioned Innova Crysta with a dedicated, professional driver-guide.', 5),
            _inc_excluded('Exclusive Experiences: Private entry tickets to the Mandovi River Luxury Sunset Cruise with VIP reserved seating.', 6),
            _inc_excluded('Heritage Tour: Fully guided, slow-paced exploration of Old Goa’s iconic historical churches and the Fontainhas', 7),
            _inc_excluded('Latin Quarter.', 8),
            _inc_excluded('Complimentary Welcome Amenities: Customized refreshing welcome kit upon arrival, including fresh fruits,', 9),
            _inc_excluded('premium local Goan sweets, and healthy hydration options.', 10),
            _inc_excluded('24/7 TRAGUIN Assistance: Dedicated, round-the-clock remote concierge support from a specialized senior-citizen', 11),
            _inc_excluded('care representative at TRAGUIN.', 12),
            _inc_excluded('Taxes: All applicable luxury resort service charges, toll fees, driver allowances, and government taxes included.', 13),
            _inc_excluded('Airfare: Round-trip domestic or international flights to and from Goa.', 14),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, premium alcoholic beverages, mini-bar consumption, and spa', 15),
            _inc_excluded('treatments.', 16),
            _inc_excluded('Optional Activities: Camera fees at monuments, personal guide fees inside churches, and any adventure activities', 17),
            _inc_excluded('not explicitly mentioned.', 18),
            _inc_excluded('TRAGUIN Premium Luxury Holidays', 19),
        ],
    )
    return package, itinerary

def build_ga_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-006'
    tour_code = 'TRG-GOA-006'
    title = 'TRAGUIN Premium Goa Tour Package — North & South Goa Highlights'
    duration = '03 Nights / 04 Days'
    slug = 'ga-006-north-south-goa-highlights'
    itin_slug = 'ga-006-north-south-goa-highlights-itinerary'
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
            _ph('Serial code GA-006 | TRAGUIN tour code TRG-GOA-006', 1),
            _ph('State / Country: Goa / India | Category: Premium Family', 2),
            _ph('Destinations: North Goa (Calangute, Baga,', 3),
            _ph('Ideal for: Family Vacations, Luxury Explorers & Multi- Generational Getaways', 4),
            _ph('Best season: October to April', 5),
            _ph('Starting price: On Request (Bespoke Family Rates)', 6),
            _ph('Vehicle / Meals: Private Luxury AC', 7),
            _ph('TRAGUIN Signature Experience: Private walking tour through the Portuguese houses of Fontainhas with', 8),
            _ph('Curated by TRAGUIN Experts: Seamless routing avoiding crowded peak hours to maximize family', 9),
            _ph('Premium Handpicked Hotels: Elite properties selected specifically for high safety ratings, private', 10),
            _ph('Luxury Transportation: Professional, uniform-clad, background-verified chauffeurs with absolute route', 11),
            _ph('Local Markets & Souvenirs: Explore the vibrant Anjuna Flea Market or Panaji markets to buy authentic Goan cashews, local Feni, hand-painted Azulejos ceramic tiles, and premium cotton resort wear. Cafes & Food: Indulge in traditional Bebinca desserts, fresh prawn balchão, and elite wood-fired artisan pizzas across legendary seaside cafes in Candolim and Assagao.', 12),
            _ph('Hotel Policies: Standard check-in is at 14:00 hrs and check-out is at 11:00 hrs. Valid original photo IDs', 13)
        ],
        moods=['Family', 'Beach', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Bespoke Family Rates)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='North & South Goa Highlights',
        overview="LUXURY Welcome to a glorious tropical escape beautifully customized by TRAGUIN. Experience the absolute Best Goa Tour Package designed to combine coastal leisure with cultural discovery. As your trusted luxury travel consultants, TRAGUIN ensures your family receives a truly premium Goa experience. From the golden sands and thrilling waters of North Goa to the colonial heritage and pristine serenity of South Goa, our handpicked hotels and exclusive experiences promise to fill your holiday with sweet, unforgettable memories.\n\nTOUR OVERVIEW\nThis premium travel itinerary is skillfully framed for families looking to balance relaxation with immersive exploration. Travelling in a dedicated, high-end private AC vehicle with professional assistance, you will avoid all local transit hassles. With an elite meal plan comprising lavish breakfasts and curated dinners, the route offers a comprehensive showcase of Goa's iconic attractions. Your journey includes an exceptional TRAGUIN curated experience note—bringing you private cruise bookings, verified safe beach excursions, and uncompromised comfort from arrival to departure.\n\nWHY CHOOSE THE BEST GOA TOUR PACKAGE?\nWhen exploring options for a Luxury Goa Holiday, families seek an seamless merger of pristine beachfronts, local history, and high-quality dining. Goa stands as India's ultimate leisure getaway, making a Goa Family Tour or a dedicated Goa Honeymoon Package the perfect recipe for a blissful vacation. From exploring the historic ramparts of Fort Aguada to walking through the massive Portuguese-era cathedrals of Old Goa, Goa sightseeing offers something deeply magical for every generation. For families and lifestyle enthusiasts, the state reveals highly popular Instagram locations like Fontainhas (the Latin Quarter of Panaji), the vibrant beach shacks of Baga, and stunning sunset viewpoints across Dona Paula. Whether your family is looking to indulge in authentic Goan seafood curry, experience water adventures, or browse local night flea markets, our signature TRAGUIN Goa Packages provide curated exclusive experiences and premium stays during the best time to visit Goa.",
        seo_title='GA-006 | Goa | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Goa package (GA-006 / TRG-GOA-006): North Goa (Calangute, Baga,.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA - NORTH GOA LEISURE', 1),
            _ih('Day 02: NORTH GOA SIGHTSEEING', 2),
            _ih('Day 03: SOUTH GOA HERITAGE & MANDOVI RIVER CRUISE', 3),
            _ih('Day 04: DEPARTURE FROM GOA', 4)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA - NORTH GOA LEISURE',
                (
                    "WELCOME TO INDIA'S COASTAL PARADISE – SUNSET & SERENITY Your luxury Goa holiday begins as your flight lands at MOPA / Dabolim Airport or your train arrives at Madgaon station. A private luxury transport vehicle arranged by TRAGUIN will receive you with premium welcome amenities. Drive through winding lanes flanked by coconut palms to check into your handpicked premium resort. Spend a relaxed afternoon by the pool before heading out to Calangute or Baga beach in the evening to witness a glorious tropical sunset, accompanied by lively music and ambient beachside dining suggestions."
                ),
                [
                    'Sightseeing Included: Baga Beachfront, Calangute Promenade leisure walk.',
                    'Evening Experience: Complimentary beach shack dinner orientation and luxury resort downtime.',
                    'Overnight Stay: North Goa (Premium / Luxury Beachfront Resort)',
                    'Meals Included: Welcome Drink & Luxury Buffet Dinner',
                ],
            ),            _day(
                2,
                'NORTH GOA SIGHTSEEING',
                (
                    'HISTORIC FORTS, SENSATIONAL BEACHES & WATER ADVENTURES Awake to the soothing sound of ocean waves and enjoy a lavish breakfast. Today, delve into an extensive North Goa sightseeing tour. Visit the iconic 17th-century Fort Aguada, where the historic lighthouse offers sweeping views of the Arabian Sea—a highly rated photography point. Proceed to Sinquerim Beach for optional premium water sports, and later explore Anjuna Beach and Vagator Beach, framed by dramatic red cliffs. End the evening exploring high-end beachside cafes or enjoying local boutique shopping.'
                ),
                [
                    'Sightseeing Included: Fort Aguada, Sinquerim Beach, Anjuna Beach, Vagator Beach, Chapora Fort viewpoint.',
                    'Optional Activities: Premium speed-boating, parasailing, or private jet-skiing with certified instructors.',
                    'Overnight Stay: North Goa (Premium / Luxury Beachfront Resort)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),            _day(
                3,
                'SOUTH GOA HERITAGE & MANDOVI RIVER CRUISE',
                (
                    'COLONIAL SPLENDOUR, OLD GOA CATHEDRALS & LATIN QUARTERS Following a rich buffet breakfast, travel southward to experience the cultural heart of the state. Explore Old Goa, visiting the UNESCO World Heritage site Basilica of Bom Jesus, which houses the sacred remains of St. Francis Xavier, and the grand Se Cathedral. Next, visit the beautiful, colorful Latin Quarter of Fontainhas in Panaji—a spectacular popular Instagram location. In the evening, step aboard an exclusive Mandovi River sunset cruise featuring traditional Goan folk dances and music.'
                ),
                [
                    'Sightseeing Included: Basilica of Bom Jesus, Se Cathedral, Fontainhas Latin Walk, Miramar Beach, Dona Paula.',
                    'Evening Experience: Reserved seating on the Mandovi River Scenic Cruise with sunset photography assistance.',
                    'Overnight Stay: North/South Goa Luxury Resort',
                    'Meals Included: Premium Breakfast & Farewell Special Dinner',
                ],
            ),            _day(
                4,
                'DEPARTURE FROM GOA',
                (
                    "CHERISHING THE TRAGUIN TROPICAL MEMORIES Indulge in your final morning breakfast at the resort's open-air restaurant. Take a final stroll along the sandy shores to collect sea shells with the family. As per your travel schedule, your private luxury transport vehicle will transfer you comfortably to MOPA/Dabolim Airport or Madgaon station for your return journey. Depart with a sun-kissed tan, re-energized spirits, and unforgettable memories carefully designed by TRAGUIN."
                ),
                [
                    'Transfers Included: Private luxury door-to-door departure drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Goa Candolim / Fairfield by Marriott / similar',
                'North Goa (3 Nights)',
                '03 Nights',
                'Deluxe',
                'Superior Garden View Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Novotel Goa Candolim / Fairfield by Marriott / similar (North Goa (3 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'DoubleTree by Hilton Panaji / Hyatt Centric Candolim',
                'North Goa (3 Nights)',
                '03 Nights',
                'Premium',
                'Premium Pool View Balcony Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: DoubleTree by Hilton Panaji / Hyatt Centric Candolim (North Goa (3 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Taj Fort Aguada Resort & Spa / W Goa (Vagator)',
                'North Goa (3 Nights)',
                '03 Nights',
                'Luxury',
                'Luxury Sea View Room',
                'Bespoke MAPAI Plan',
                5,
                3,
                description='OPTION 03 – LUXURY: Taj Fort Aguada Resort & Spa / W Goa (Vagator) (North Goa (3 Nights)) | Bespoke MAPAI Plan',
            ),
            _hotel(
                'The Leela Goa / Taj Exotica Resort & Spa (Benaulim)',
                'North Goa (3 Nights)',
                '03 Nights',
                'Ultra Luxury',
                'Private Luxury Plunge Pool Villa Suite',
                'VVIP Custom Dining Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Leela Goa / Taj Exotica Resort & Spa (Benaulim) (North Goa (3 Nights)) | VVIP Custom Dining Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Airfare, flight bookings, or mainline train tickets', 1),
            _inc_excluded('to Goa.', 2),
            _inc_excluded('Water sports equipment rentals or activity hiring', 3),
            _inc_excluded('charges.', 4),
            _inc_excluded('Personal expenses such as laundry, phone', 5),
            _inc_excluded('calls, drinks, or tips.', 6),
            _inc_excluded('Any monument entry fees, local guide charges, or', 7),
            _inc_excluded('camera permits.', 8),
        ],
    )
    return package, itinerary

def build_ga_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-007'
    tour_code = 'TRG-GOA-007'
    title = 'TRAGUIN Premium Goa Tour Package — Complete Goa Explorer'
    duration = '04 Nights / 05 Days'
    slug = 'ga-007-complete-goa-explorer'
    itin_slug = 'ga-007-complete-goa-explorer-itinerary'
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
            _ph('Serial code GA-007 | TRAGUIN tour code TRG-GOA-007', 1),
            _ph('State / Country: Goa / India | Category: Complete Goa', 2),
            _ph('Destinations: North Goa', 3),
            _ph('Ideal for: Premium Family Vacations, Luxury Seekers & Cultural Explorers', 4),
            _ph('Best season: October to April (Pleasant) / June to September (Lush Monsoon)', 5),
            _ph('Starting price: On Request (Premium Family Customised)', 6),
            _ph('Vehicle / Meals: Private Luxury AC', 7),
            _ph('TRAGUIN Signature Experience: Private walking tour through Fontainhas with an architectural historian.', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked restaurant recommendations and reserved premium beach', 9),
            _ph('Premium Handpicked Hotels: Properties selected strictly based on direct beach access, high safety', 10),
            _ph('Luxury Transportation: Expert drivers well-versed in navigating coastal and jungle routes safely.', 11),
            _ph('Local Markets & Souvenirs: Visit the famous Anjuna Flea Market or Panaji markets to purchase premium Goan cashews, authentic Portuguese azulejos tile magnets, local fruit feni, and handcrafted resort wear. Cafes & Food: Indulge in traditional Bebinca cake, classic Goan fish curry rice, and fresh wood-fired artisanal sourdough pizzas across high-end beach bistros.', 12),
            _ph('Hotel Policies: Standard check-in is 14:00 hrs; check-out is 11:00 hrs. Swimming costume is mandatory', 13)
        ],
        moods=['Family', 'Beach', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Family Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Complete Goa Explorer',
        overview='SUNKISSED SPIRITS Welcome to a glorious tropical escape curated exclusively by TRAGUIN. Embark on the definitive Goa Family Tour designed to balance coastal tranquility, rich Portuguese heritage, and vibrant modern luxury. As your elite travel consultants, TRAGUIN transforms your beach vacation into a seamless luxury holiday filled with premium stays, deep cultural exploration, and handpicked hotels. From the golden sands of North Goa to the historic churches of South Goa and the emerald canopy of the Western Ghats, every moment is engineered to craft unforgettable memories for your family.\n\nTOUR OVERVIEW\nThis meticulously planned luxury holiday package delivers the ultimate balance of relaxation, heritage discovery, and family entertainment. Traveling in a fully private, chauffeured premium vehicle, you will experience Goa without standard tourist constraints. Enjoy an optimized meal plan featuring spectacular international breakfasts and personalized gourmet dinners at your resort. Complete with custom TRAGUIN curated experiences—including a private yacht option and exclusive plantation walks—this package defines the gold standard of a premium Goa experience.\n\nWHY CHOOSE THE BEST GOA TOUR PACKAGE?\nWhen exploring a Luxury Goa Holiday, sophisticated travelers want to look beyond the crowded paths to rediscover the hidden charm of India’s sunshine state. Goa offers a phenomenal variety of iconic attractions. From the historical marvel of Aguada Fort to the roaring majesty of Dudhsagar Waterfalls, Goa sightseeing provides layers of deep discovery. For couples and modern families picking a custom Goa Honeymoon Package or Goa Family Tour, the region boasts stunning popular Instagram locations like the Latin Quarter of Fontainhas, pristine private beaches, and upscale clifftop lounges. Indulge in local spice plantation lunches, shop at high-end night markets, or take a sunset river cruise. Our signature TRAGUIN Goa Packages blend immersive experiences with elite comfort, making any time the best time to visit Goa.',
        seo_title='GA-007 | Goa | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Goa package (GA-007 / TRG-GOA-007): North Goa.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA & NORTH COAST DRIVE', 1),
            _ih('Day 02: NORTH GOA BEACHES & FORTS TOUR', 2),
            _ih('Day 03: HERITAGE TOUR OF SOUTH GOA', 3),
            _ih('Day 04: SPICE PLANTATION & DUDHSAGAR WATERFALLS', 4),
            _ih('Day 05: LEISURE & DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA & NORTH COAST DRIVE',
                (
                    'WELCOME TO PARADISE – UNWIND IN THE LUXURY LANDSCAPE Your premium Goa experience kicks off as you land at Goa Airport (Mopa / Dabolim). A professional chauffeur in a private luxury transport vehicle will greet you warmly and smoothly escort you to your premium beachfront resort. Take the afternoon to settle into your spacious sea-view suite. In the late afternoon, enjoy a peaceful stroll down the private sands of Candolim or Sinquerim, catching a spectacular Arabian Sea sunset.'
                ),
                [
                    'Sightseeing Included: Sinquerim Beach walk, coastal orientation drive.',
                    'Evening Experience: Welcome note and a refreshing mocktail service with seaside views.',
                    'Overnight Stay: North Goa (Premium / Luxury Resort)',
                    'Meals Included: Welcome Amenities & Luxury Dinner',
                ],
            ),            _day(
                2,
                'NORTH GOA BEACHES & FORTS TOUR',
                (
                    'MONUMENTS, SUN-KISSED SHORES & EXQUISITE CUISINE Relish a lavish buffet breakfast before setting out for an exciting North Goa sightseeing tour. Explore the imposing 17th-century Fort Aguada, marveling at its stone lighthouse and sweeping ocean panoramas. Next, head down to the vibrant sands of Calangute, Baga, and Anjuna Beach. Conclude your afternoon at the dramatic clifftops of Vagator Beach, overlooking Chapora Fort, famously known as a popular Instagram location for sunset views.'
                ),
                [
                    'Sightseeing Included: Fort Aguada, Calangute Beach, Baga Beach, Vagator Beach clifftops.',
                    'Optional Activities: Premium watersports (parasailing, jet-skiing) with top safety parameters.',
                    'Overnight Stay: North Goa (Premium / Luxury Resort)',
                    'Meals Included: Premium Breakfast & Resort Dinner',
                ],
            ),            _day(
                3,
                'HERITAGE TOUR OF SOUTH GOA',
                (
                    "PORTUGUESE SPLENDOR, SACRED CATHEDRALS & LATIN FLAVORS Today, cross into South Goa to uncover the state's historical and spiritual heart. Tour Old Goa to witness iconic attractions like the Basilica of Bom Jesus, which houses the sacred remains of St. Francis Xavier, and the grand Se Cathedral. Afterwards, enjoy an immersive experience walking through Fontainhas, the stunning Latin Quarter of Panaji, lined with brightly colored heritage Portuguese houses. End your day with a relaxing sunset cruise along the Mandovi River. River."
                ),
                [
                    'Sightseeing Included: Basilica of Bom Jesus, Se Cathedral, Fontainhas Latin Quarter, Miramar Beach, Mandovi',
                    'Evening Experience: Bespoke luxury cruise on the Mandovi River with live Goan folk music.',
                    'Overnight Stay: North / South Goa Luxury Resort',
                    'Meals Included: Breakfast & Traditional Indo-Portuguese Gourmet Dinner',
                ],
            ),            _day(
                4,
                'SPICE PLANTATION & DUDHSAGAR WATERFALLS',
                (
                    'THE EMERALD WILDERNESS & CULINARY ESCAPE Head inland toward the lush foothills of the Western Ghats. Take a thrilling open-jeep safari through the jungle terrain to witness the spectacular Dudhsagar Waterfalls, a top tourist place in Goa for nature enthusiasts. Following this refreshing excursion, visit an authentic spice plantation for a guided tour. Learn about exotic spices, enjoy a traditional Goan buffet lunch served on banana leaves, and experience a refreshing elephant shower demonstration.'
                ),
                [
                    'Sightseeing Included: Dudhsagar Waterfall Jeep Safari, Sahakari Spice Farm walking tour.',
                    'Optional Activities: Artisanal feni-tasting session and organic spice purchasing.',
                    'Overnight Stay: Goa Beachfront Resort',
                    'Meals Included: Breakfast, Traditional Plantation Lunch & Farewell Dinner',
                ],
            ),            _day(
                5,
                'LEISURE & DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS Savor a peaceful breakfast as the ocean breeze drifts through your resort restaurant. Spend your final morning capturing family photos on the beach or picking up last-minute souvenirs. Your private luxury transport will arrive to smoothly transfer you to the airport or train station for your journey home, leaving you with unforgettable memories designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door airport or station drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Lemon Tree Amarante / Novotel Candolim | Heritage Village Resort / similar',
                'North Goa (2 Nights) / South Goa (2 Nights)',
                '04 Nights',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Lemon Tree Amarante / Novotel Candolim (North Goa (2 Nights)) | Heritage Village Resort / similar (South Goa (2 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Hard Rock Hotel / DoubleTree by Hilton | Kenilworth Resort & Spa / Caravela Beach',
                'North Goa (2 Nights) / South Goa (2 Nights)',
                '04 Nights',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Hard Rock Hotel / DoubleTree by Hilton (North Goa (2 Nights)) | Kenilworth Resort & Spa / Caravela Beach (South Goa (2 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Taj Holiday Village / W Goa | Taj Exotica Resort & Spa / Alila Diwa',
                'North Goa (2 Nights) / South Goa (2 Nights)',
                '04 Nights',
                'Luxury',
                'Luxury Suite',
                'MAPAI + Premium Amenities',
                5,
                3,
                description='OPTION 03 – LUXURY: Taj Holiday Village / W Goa (North Goa (2 Nights)) | Taj Exotica Resort & Spa / Alila Diwa (South Goa (2 Nights)) | MAPAI + Premium Amenities',
            ),
            _hotel(
                'The St. Regis Goa Resort (Sea View Suite) | The Leela Goa (The Club Pool Suite)',
                'North Goa (2 Nights) / South Goa (2 Nights)',
                '04 Nights',
                'Ultra Luxury',
                'VVIP Suite',
                'Bespoke Signature VIP Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The St. Regis Goa Resort (Sea View Suite) (North Goa (2 Nights)) | The Leela Goa (The Club Pool Suite) (South Goa (2 Nights)) | Bespoke Signature VIP Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Airfare, flight tickets, or interstate train travel.', 1),
            _inc_excluded('Water sports fees, scuba diving, or optional', 2),
            _inc_excluded('adventure activities.', 3),
            _inc_excluded('Monument entry tickets, professional guide fees,', 4),
            _inc_excluded('camera permits.', 5),
            _inc_excluded('Personal expenses such as laundry, mini-bar', 6),
            _inc_excluded('usage, or tips.', 7),
        ],
    )
    return package, itinerary

def build_ga_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-008'
    tour_code = 'TRG-GOA-008'
    title = 'TRAGUIN Premium Goa Tour Package — Sunny Goa Vacation'
    duration = '05 Nights / 06 Days'
    slug = 'ga-008-sunny-goa-vacation'
    itin_slug = 'ga-008-sunny-goa-vacation-itinerary'
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
            _ph('Serial code GA-008 | TRAGUIN tour code TRG-GOA-008', 1),
            _ph('State / Country: Goa / India | Category: Premium Family', 2),
            _ph('Destinations: North Goa Beaches • South Goa', 3),
            _ph('Ideal for: Family Vacations, Luxury Explorers & Beach Lovers', 4),
            _ph('Best season: November to April', 5),
            _ph('Starting price: On Request (Premium Family Customised)', 6),
            _ph('Vehicle / Meals: Private Luxury AC', 7),
            _ph('TRAGUIN Signature Experience: Private, pre-arranged family table at an exclusive beach shack for a', 8),
            _ph('Curated by TRAGUIN Experts: Seamlessly split routing options that optimize driving times between North', 9),
            _ph('Premium Handpicked Hotels: Properties verified first-hand for premium family luxury, kid-friendly play', 10),
            _ph('Exclusive Recommendations: Access to a curated guide detailing Goa’s hidden beaches and elite', 11),
            _ph("Local Markets & Souvenirs: Explore the vibrant Wednesday Anjuna Flea Market or the Saturday Night Bazaar for chic clothing, leather goods, and handmade jewelry. Don't leave without premium Goan cashews, local Feni, and authentic Mario Miranda artwork. Cafes & Food: Indulge in traditional Bebinca and Dodol desserts. Visit atmospheric beachfront cafes in Vagator and Assagao for signature wood-fired continental dishes and refreshing tropical beverages accompanied by coastal jazz music.", 12),
            _ph('Hotel Policies: Resort check-in begins at 14:00 hrs; check-out is at 11:00 hrs. Government-issued photo', 13)
        ],
        moods=['Family', 'Beach', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Family Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Sunny Goa Vacation',
        overview="Welcome to a sensational beachside holiday escape curated exclusively by TRAGUIN. Embark on the finest Goa Family Tour designed to reveal the breathtaking landscapes, colonial history, and lively sun- soaked shores of this tropical paradise. As your trusted luxury travel consultants, TRAGUIN transforms your getaway into a seamless luxury holiday complete with premium stays, immersive experiences, and magical coastal sunsets. From the high-energy sands of North Goa to the serene, historic cathedrals of South Goa, every element is designed to generate unforgettable memories for your family.\n\nTOUR OVERVIEW\nThis meticulously planned luxury holiday itinerary provides an exquisite balance between golden beaches, cascading waterfalls, aromatic spice farms, and ancient Portuguese heritage. Travelling in a completely private premium AC vehicle accompanied by a professional chauffeur-guide, your family will discover Goa in absolute safety and style. With a carefully structured meal plan showcasing magnificent breakfast spreads and thematic dinners, this itinerary represents the definitive premium Goa experience. Every single day features the signature touch of TRAGUIN curated experiences, assuring smooth VIP arrangements, handpicked hotels, and 24/7 dedicated support.\n\nWHY CHOOSE THE BEST GOA TOUR PACKAGE?\nWhen considering a Luxury Goa Holiday, travelers expect a flawless fusion of seaside luxury, historical depth, and natural marvels. Goa easily excels as India's ultimate beach destination. From the legendary North Goa shores like Calangute, Baga, and Anjuna—famous for water sports and vibrant markets—to the peaceful sanctuaries of South Goa, Goa sightseeing offers something magical for every generation. For families and couples looking to book a signature Goa Honeymoon Package or an expansive Goa Family Tour, the region offers world-class, popular Instagram locations such as the multicoloured streets of Fontainhas, the historic ramparts of Aguada Fort, and the dramatic Dudhsagar Waterfalls. Whether your interest lies in shopping for local boutique items, exploring massive spice plantations, or experiencing the scenic beauty of a private luxury yacht cruise, our specialized TRAGUIN Goa Packages ensure that you enjoy the best time to visit Goa in utmost grandeur.",
        seo_title='GA-008 | Goa | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Goa package (GA-008 / TRG-GOA-008): North Goa Beaches • South Goa.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA', 1),
            _ih('Day 02: NORTH GOA BEACHES & FORTS', 2),
            _ih('Day 03: SOUTH GOA HERITAGE & SPIRITUALITY', 3),
            _ih('Day 04: DUDHSAGAR WATERFALL & SPICE PLANTATION', 4),
            _ih('Day 05: EXCLUSIVE SOUTH GOA BEACHES', 5),
            _ih('Day 06: GOA DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA',
                (
                    "WELCOME TO PARADISE – COASTAL ESCAPE BEGINS Your premium Goa experience starts the moment you land at Goa Airport (Mopa/Dabolim). A professional corporate chauffeur welcomes your family in a private luxury transport vehicle to transition you to your premium beachfront resort. Enjoy a custom welcome drink, check into your spacious suite, and unwind. Spend the late afternoon walking along the resort's private beach stretch, capturing beautiful family photographs as the sun dips below the Arabian Sea."
                ),
                [
                    'Sightseeing Included: Resort beachfront relaxation, beautiful sunset viewing.',
                    'Evening Experience: Exquisite beachside welcome dinner arranged specially by TRAGUIN experts.',
                    'Overnight Stay: North/South Goa Beach Resort (Luxury Category)',
                    'Meals Included: Welcome Drink & Luxury Buffet Dinner',
                ],
            ),            _day(
                2,
                'NORTH GOA BEACHES & FORTS',
                (
                    'VIBRANT SHORES, COLONIAL HISTORY & WATER SPORTS Indulge in a lavish breakfast before heading out for a comprehensive North Goa sightseeing tour. Explore the iconic 17th-century Aguada Fort, a historic Portuguese fortress overlooking the vast ocean. Continue your journey to the golden sands of Sinquerim, Calangute, and Baga beaches. For adventure seekers, thrilling premium water sports such as parasailing and jet-skiing are available. End your afternoon exploring the trendy coastal cafes and craft markets.'
                ),
                [
                    'Sightseeing Included: Fort Aguada, Lighthouse, Calangute Beach, Baga Beach, Anjuna Beach viewpoints.',
                    'Optional Activities: Premium banana boat rides, parasailing, and private speed boat charters.',
                    'Overnight Stay: Goa Premium Luxury Resort',
                    'Meals Included: Premium Breakfast & World-Cuisine Dinner',
                ],
            ),            _day(
                3,
                'SOUTH GOA HERITAGE & SPIRITUALITY',
                (
                    'OLD GOA CATHEDRALS & FONTAINHAS LATIN QUARTER Immerse yourself in history today as you travel to Old Goa. Tour the magnificent Basilica of Bom Jesus, a UNESCO World Heritage site holding the sacred relics of St. Francis Xavier. Marvel at the stunning architecture of the Se Cathedral. Afterwards, step into Fontainhas—the historic Latin Quarter of Panaji— boasting colorful Portuguese houses that serve as popular Instagram locations. Conclude the day with a relaxing sunset luxury cruise on the Mandovi River. Cruise. performances.'
                ),
                [
                    'Sightseeing Included: Basilica of Bom Jesus, Se Cathedral, Fontainhas Walk, Miramar Beach, Mandovi River',
                    'Evening Experience: Reserved deck seating on a luxury river boat cruise with traditional Goan folk',
                    'Overnight Stay: Goa Premium Luxury Resort',
                    'Meals Included: Premium Breakfast & Authentic Indo-Portuguese Dinner',
                ],
            ),            _day(
                4,
                'DUDHSAGAR WATERFALL & SPICE PLANTATION',
                (
                    'CASCADING WATERFALLS & AROMATIC CULINARY TRAILS Embark on a memorable eco-adventure into the lush Western Ghats. Board an open-top private 4x4 jungle jeep safari to reach the base of the spectacular Dudhsagar Waterfalls, where mountain waters crash down from a height of 300 meters, painting a picture of scenic beauty. After relaxing by the natural pools, visit a premium tropical Spice Plantation. Enjoy an immersive, guided walking tour through exotic spices followed by a traditional buffet lunch served on banana leaves.'
                ),
                [
                    'Sightseeing Included: Dudhsagar Jeep Safari, Bhagwan Mahavir Wildlife Sanctuary, Spice Farm Tour.',
                    'Complimentary Experience: Authentic Goan organic buffet lunch and traditional warm welcome at the spice farm.',
                    'Overnight Stay: Goa Premium Luxury Resort',
                    'Meals Included: Breakfast, Spice Plantation Lunch & Resort Dinner',
                ],
            ),            _day(
                5,
                'EXCLUSIVE SOUTH GOA BEACHES',
                (
                    'SERENE WHITE SANDS & BESPOKE SUNSET SAILING Dedicate this day to pure indulgence along the unspoiled white sand beaches of South Goa. Visit Colva, Benaulim, and the crescent-shaped Palolem Beach, framed by dramatic coconut palms. Relax on luxury sun loungers, explore small seaside boutiques, and let the breathtaking landscapes soothe your mind. This is an ideal highlight for any premium Goa experience.'
                ),
                [
                    'Sightseeing Included: Palolem Beach, Colva Beach, romantic coastal driving loops.',
                    'Optional Activities: Private luxury catamaran or yacht hire for an unforgettable ocean sunset.',
                    'Overnight Stay: Goa Premium Luxury Resort',
                    'Meals Included: Premium Breakfast & Farewell Gala Dinner',
                ],
            ),            _day(
                6,
                'GOA DEPARTURE',
                (
                    'CHERISHING GOLDEN FAMILY MEMORIES Savor a peaceful breakfast spread at your resort as the ocean breeze sweeps through the dining terrace. Spend your final morning purchasing unique souvenirs or taking last family photos by the pool. Your private luxury transport will arrive to ensure a comfortable transfer to Goa Airport or Railway Station. Return home carrying unforgettable memories designed beautifully by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury chauffeured airport drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Goa Resort & Spa / Lemon Tree Amarante',
                'Goa (5 Nights)',
                '05 Nights',
                'Deluxe',
                'Superior Garden View Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Novotel Goa Resort & Spa / Lemon Tree Amarante (Goa (5 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Grand Hyatt Goa / Caravela Beach Resort',
                'Goa (5 Nights)',
                '05 Nights',
                'Premium',
                'Premium Balcony Sea View',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Grand Hyatt Goa / Caravela Beach Resort (Goa (5 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Taj Exotica Resort & Spa / The Leela Goa',
                'Goa (5 Nights)',
                '05 Nights',
                'Luxury',
                'Luxury Pavilion Room',
                'MAPAI + Welcome Premium Kit',
                5,
                3,
                description='OPTION 03 – LUXURY: Taj Exotica Resort & Spa / The Leela Goa (Goa (5 Nights)) | MAPAI + Welcome Premium Kit',
            ),
            _hotel(
                'ITC Grand Goa Resort / W Goa (Villas)',
                'Goa (5 Nights)',
                '05 Nights',
                'Ultra Luxury',
                'Private Plunge Pool VVIP Villa',
                'Bespoke Gourmet Custom Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: ITC Grand Goa Resort / W Goa (Villas) (Goa (5 Nights)) | Bespoke Gourmet Custom Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Airfare, domestic flight bookings, or railway tickets.', 1),
            _inc_excluded('Water sports equipment rentals, scuba diving,', 2),
            _inc_excluded('and guide fees.', 3),
            _inc_excluded('Personal items such as laundry, phone charges,', 4),
            _inc_excluded('alcoholic beverages, and tips.', 5),
            _inc_excluded('Monument entrance tickets, camera permits,', 6),
            _inc_excluded('and any unlisted tours.', 7),
        ],
    )
    return package, itinerary

def build_ga_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-009'
    tour_code = 'TRG-GOA-009'
    title = 'TRAGUIN Premium Goa Tour Package — Beaches and Heritage Special'
    duration = '07 Nights / 08 Days'
    slug = 'ga-009-beaches-and-heritage-special'
    itin_slug = 'ga-009-beaches-and-heritage-special-itinerary'
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
            _ph('Serial code GA-009 | TRAGUIN tour code TRG-GOA-009', 1),
            _ph('State / Country: Goa / India | Category: Beaches and', 2),
            _ph('Destinations: North Goa (Candolim/ Calangute) •', 3),
            _ph('Ideal for: Luxury Family Vacations, Heritage Connoisseurs & Multi-Generational Retreats', 4),
            _ph('Best season: October to April (Pleasant Festive Season) / June to September (Lush Monsoon)', 5),
            _ph('Starting price: On Request (Premium Bespoke Pricing)', 6),
            _ph('Vehicle / Meals: Private Premium', 7),
            _ph('TRAGUIN Signature Experience: Private family historical storytelling briefing and custom tea service at', 8),
            _ph('Curated by TRAGUIN Experts: Balanced routes designed to combine coastal relaxation with enriching', 9),
            _ph('Premium Handpicked Hotels: Accommodations selected for their outstanding child-friendly amenities,', 10),
            _ph('Luxury Transportation: Professional, uniform-clad local drivers who know the best scenic roads and', 11),
            _ph("Local Markets & Souvenirs: Browse local markets for premium Goan cashews, authentic Feni, hand-painted Azulejos ceramic tiles, and beautiful sea-shell crafts. Don't miss out on exploring spice sets from the organic plantation. Cafes & Food: Enjoy fresh seafood vindaloo, authentic bebinca dessert, wood-fired pizzas, and artisan coffees at the charming, historic cafes scattered across Panaji and Old Manali-style quarters.", 12),
            _ph('Hotel Policies: Check-in is at 14:00 hrs, check-out at 11:00 hrs. Valid government-issued photo ID cards', 13)
        ],
        moods=['Family', 'Beach', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Bespoke Pricing)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Beaches and Heritage Special',
        overview="FAMILIES Welcome to a timeless tropical escape curated exclusively by TRAGUIN. Embark on the definitive Goa Family Tour, perfectly crafted to balance the sun-kissed tranquility of golden shores with the deep, captivating narrative of Old Goa’s heritage. As your elite travel consultants, TRAGUIN transforms your vacation into a premium luxury holiday complete with handpicked hotels, immersive experiences, and impeccable service. From the swaying palms of pristine private beaches to the majestic cobblestone architecture of a bygone Portuguese era, every single day is engineered to build beautiful family bonds and unforgettable memories.\n\nTOUR OVERVIEW\nThis bespoke 7-Night / 8-Day itinerary offers a sophisticated, comprehensive exploration of India's most beloved coastal paradise. Traveling in an elite, chauffeur-driven luxury vehicle, your family will experience seamless, stress-free transfers and personalized excursions. Featuring an exceptional meal plan with gourmet daily breakfasts and curated multi-cuisine dinners, this route highlights the absolute finest hospitality the coastal state has to offer. Every detail incorporates a signature TRAGUIN curated experience note, from VIP heritage estate passes to private island explorations and dedicated premium support around the clock.\n\nWHY CHOOSE THE BEST GOA TOUR PACKAGE?\nWhen searching for the ultimate Luxury Goa Holiday, discerning family groups require a perfect combination of coastal leisure, child-friendly activity, and deep cultural substance. Goa stands as an iconic destination that offers a magnificent spectrum of travel options. From world-renowned historic structures to pristine sand stretches, Goa sightseeing holds an irresistible allure for every age group. For couples planning a romantic getaway, a Goa Honeymoon Package unveils hidden infinity pools, secret sunset viewpoints, and highly popular Instagram locations like the colorful Latin Quarter of Fontainhas or the dramatic cliff views of Cabo de Rama. Families booking our specialized Goa Family Tour will enjoy exclusive experiences like organic spice plantation culinary walks, dolphin spotting safaris, and high-end shopping at boutique night markets. Our signature TRAGUIN Goa Packages combine top tourist places in Goa with premium stays, making any time the best time to visit Goa when traveling in uncompromising luxury.",
        seo_title='GA-009 | Goa | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Goa package (GA-009 / TRG-GOA-009): North Goa (Candolim/ Calangute) •.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA – WELCOME TO THE SUN-KISSED COAST', 1),
            _ih('Day 02: NORTH GOA BEACHES & COASTAL FORTS', 2),
            _ih('Day 03: PORTUGUESE HERITAGE & THE CHRONICLES OF OLD GOA', 3),
            _ih('Day 04: THE LATIN QUARTER & CHARMING DIVAR ISLAND', 4),
            _ih('Day 05: MAJESTIC DUDHSAGAR WATERFALLS & SPICE PLANTATION', 5),
            _ih('Day 06: SOUTH GOA – TRANQUILITY & WHITE SAND PARADISE', 6),
            _ih('Day 07: SIGHTSEEING IN SOUTH GOA – FORTS & MUSEUMS', 7),
            _ih('Day 08: DEPARTURE FROM GOA', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA – WELCOME TO THE SUN-KISSED COAST',
                (
                    'ELITE RECEPTION & SEAMLESS LUXURY RESORT CHECK-IN Your premium Goa experience begins with a personalized greeting at MOPA / Dabolim Airport by your private TRAGUIN-assigned luxury transport chauffeur. Enjoy a refreshing drive to your handpicked premium luxury resort in North Goa. Upon arrival, receive a signature tropical welcome drink and check in to your exquisite pool-view family suite. The afternoon is yours to unwind by the pool or enjoy a family walk along the golden sand banks of Candolim Beach to capture your first photography points.'
                ),
                [
                    'Sightseeing Included: Candolim Beach leisure walk, Sunset beach photography.',
                    "Evening Experience: Bespoke welcome dinner at the resort's beachfront deck with live acoustic music.",
                    'Overnight Stay: North Goa (Premium / Ultra-Luxury Beachfront Resort)',
                    'Meals Included: Welcome Drink & Luxury Multi-Cuisine Dinner',
                ],
            ),            _day(
                2,
                'NORTH GOA BEACHES & COASTAL FORTS',
                (
                    'PANORAMIC VIEWS, ARCHITECTURE & HISTORIC BEACONS Savor a lavish buffet breakfast before heading out to explore iconic attractions in North Goa. Visit the historic 17th-century Sinquerim Fort and Aguada Fort, which overlook the vast Arabian Sea. Walk along the historic ramparts and admire the ancient Portuguese lighthouse. In the afternoon, explore the lively shores of Calangute and Baga beach, followed by an upscale family shopping excursion at an elegant designer boutique market.'
                ),
                [
                    'Sightseeing Included: Aguada Fort, Sinquerim Beach, Calangute Promenade, Baga Beach.',
                    'Optional Activities: Premium family parasailing or speed-boat rides under certified expert safety guidance.',
                    'Overnight Stay: North Goa (Premium / Ultra-Luxury Beachfront Resort)',
                    'Meals Included: Premium Breakfast & Gourmet Fusion Dinner',
                ],
            ),            _day(
                3,
                'PORTUGUESE HERITAGE & THE CHRONICLES OF OLD GOA',
                (
                    "SACRED ARCHITECTURE & THE REPLICA OF ROME Dedicate your day to an emotionally enriching exploration of Goa's fascinating heritage. Journey to Old Goa to view the majestic Basilica of Bom Jesus, a UNESCO World Heritage Site housing the sacred remains of St. Francis Xavier. Directly opposite stands the grand Se Cathedral, renowned for its golden bell. Stroll through these magnificent structures with a specialist guide who will bring centuries of history to life through engaging storytelling. refreshments."
                ),
                [
                    'Sightseeing Included: Basilica of Bom Jesus, Se Cathedral, Church of St. Cajetan, Arch of Viceroys.',
                    'Evening Experience: An exclusive sunset yacht cruise across the Mandovi River, complete with family',
                    'Overnight Stay: North Goa (Premium / Ultra-Luxury Beachfront Resort)',
                    'Meals Included: Premium Breakfast & Traditional Indo-Portuguese Dinner',
                ],
            ),            _day(
                4,
                'THE LATIN QUARTER & CHARMING DIVAR ISLAND',
                (
                    'FONTAINHAS VIBRANCY & UNTOUCHED ISLAND SERENITY Explore the beautifully preserved Latin Quarter of Fontainhas in Panaji. This highly popular Instagram location features bright pastel-colored houses, ornate iron balconies, and charming narrow winding streets. Afterward, board a private vehicle ferry to Divar Island, an enchanting destination frozen in time. Drive past vast emerald paddy fields and historic baroque churches, immersing your family in authentic local culture.'
                ),
                [
                    'Sightseeing Included: Fontainhas Walk, Maruti Temple, Divar Island old villa drive.',
                    'Food Suggestions: Enjoy artisan Portuguese pastries and authentic Goan poi at a heritage cafe.',
                    'Overnight Stay: North Goa / Panaji Luxury Heritage Boutique Hotel',
                    "Meals Included: Premium Breakfast & Selected Chef's Dinner",
                ],
            ),            _day(
                5,
                'MAJESTIC DUDHSAGAR WATERFALLS & SPICE PLANTATION',
                (
                    'BREATHTAKING LANDSCAPES & EXOTIC FLAVOR TRAILS Set off on an early morning excursion to the awe-inspiring Dudhsagar Waterfalls, a magnificent four-tiered cascade tucked deep within the Bhagwan Mahavir Wildlife Sanctuary. Board an exciting private 4x4 jungle jeep safari to reach the base of the falls. Afterward, enjoy a refreshing walk through an organic spice plantation. Savor an authentic Goan feast served on traditional banana leaves while learning about organic farming practices.'
                ),
                [
                    'Sightseeing Included: Dudhsagar Jeep Safari, Spice Plantation spice trail tour.',
                    'Local Experiences: Traditional Goan musical welcome and herbal oil skin-refreshing demo.',
                    'Overnight Stay: South Goa (Premium / Ultra-Luxury Private Beach Resort)',
                    'Meals Included: Breakfast, Traditional Buffet Lunch & Dinner',
                ],
            ),            _day(
                6,
                'SOUTH GOA – TRANQUILITY & WHITE SAND PARADISE',
                (
                    "SUSEGAD BLISS AT UNTOUCHED SOUTHERN SHORES Transition to the peaceful, upscale ambiance of South Goa. After breakfast, visit the pristine white sands of Colva Beach and Benaulim Beach. These serene coastlines offer breathtaking landscapes and a much quieter, exclusive atmosphere ideal for family relaxation. Spend the afternoon enjoying world-class amenities at your premium beach resort or relaxing with a premium couples' spa therapy session."
                ),
                [
                    'Sightseeing Included: Colva Beach shoreline, Mobor Beach scenic peninsula viewpoint.',
                    'Optional Activities: An early morning private boat safari for dolphin-spotting in the Arabian Sea.',
                    'Overnight Stay: South Goa (Premium / Ultra-Luxury Private Beach Resort)',
                    'Meals Included: Premium Breakfast & Luxury Seafood / Vegetarian Dinner',
                ],
            ),            _day(
                7,
                'SIGHTSEEING IN SOUTH GOA – FORTS & MUSEUMS',
                (
                    'EXPLORING PALACES & DRAMATIC COASTAL CLIFFS Embark on a scenic drive to the dramatic Cabo de Rama Fort, situated on a high cliff edge that offers panoramic views of the sea. Explore the ancient ruins and visit the charming white chapel inside. In the afternoon, discover the beautifully restored 18th-century Palacio do Deao, an elegant heritage mansion surrounded by magnificent historical gardens. This final sightseeing day offers the perfect conclusion to your journey, leaving you with beautiful photographs and memories.'
                ),
                [
                    'Sightseeing Included: Cabo de Rama Fort, Palacio do Deao Mansion, Margao Local Heritage Market.',
                    'Evening Experience: A grand farewell family dinner arranged at an exclusive fine-dining venue.',
                    'Overnight Stay: South Goa (Premium / Ultra-Luxury Private Beach Resort)',
                    'Meals Included: Premium Breakfast & Luxury Farewell Dinner',
                ],
            ),            _day(
                8,
                'DEPARTURE FROM GOA',
                (
                    'FOND FAREWELLS & CHERISHED TRAVEL MEMORIES Indulge in a final morning buffet breakfast at your beach resort. Enjoy a last swim or take a stroll along the shore before packing your bags. Your chauffeur will pick you up in your private luxury vehicle for a smooth transfer to the airport or train station for your onward journey. Return home carrying unforgettable memories of an exquisite coastal holiday designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door departure drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Goa Candolim / similar | Panjim Inn Heritage / similar | Kenilworth Resort & Spa / similar',
                'North Goa (3 Nights) / Panaji Heritage (1 Night) / South Goa (3 Nights)',
                '07 Nights',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Novotel Goa Candolim / similar (North Goa (3 Nights)) | Panjim Inn Heritage / similar (Panaji Heritage (1 Night)) | Kenilworth Resort & Spa / similar (South Goa (3 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Taj Holiday Village / Vivanta Candolim | WelcomHeritage Panjim Pousada | The Leela Goa (Lagoon Suite)',
                'North Goa (3 Nights) / Panaji Heritage (1 Night) / South Goa (3 Nights)',
                '07 Nights',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Taj Holiday Village / Vivanta Candolim (North Goa (3 Nights)) | WelcomHeritage Panjim Pousada (Panaji Heritage (1 Night)) | The Leela Goa (Lagoon Suite) (South Goa (3 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'W Goa (Wonderful Room) / Taj Fort Aguada | Boutique Heritage Villa Mansion | Taj Exotica Resort & Spa (Villa)',
                'North Goa (3 Nights) / Panaji Heritage (1 Night) / South Goa (3 Nights)',
                '07 Nights',
                'Luxury',
                'Luxury Villa / Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: W Goa (Wonderful Room) / Taj Fort Aguada (North Goa (3 Nights)) | Boutique Heritage Villa Mansion (Panaji Heritage (1 Night)) | Taj Exotica Resort & Spa (Villa) (South Goa (3 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'St. Regis Goa Resort (Presidential) | Private Exclusive VVIP Heritage Estate | The Leela Goa (Royal Villa Suite)',
                'North Goa (3 Nights) / Panaji Heritage (1 Night) / South Goa (3 Nights)',
                '07 Nights',
                'Ultra Luxury',
                'VVIP Villa Suite',
                'Elite Custom Luxury Dining Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: St. Regis Goa Resort (Presidential) (North Goa (3 Nights)) | Private Exclusive VVIP Heritage Estate (Panaji Heritage (1 Night)) | The Leela Goa (Royal Villa Suite) (South Goa (3 Nights)) | Elite Custom Luxury Dining Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Airfare, flight taxes, or cross-state interstate train', 1),
            _inc_excluded('tickets.', 2),
            _inc_excluded('Optional extreme water sports, scuba diving, or', 3),
            _inc_excluded('parasailing fees.', 4),
            _inc_excluded('Monument entrance tickets, professional camera', 5),
            _inc_excluded('permissions, local guide fees.', 6),
            _inc_excluded('Personal expenses such as laundry services,', 7),
            _inc_excluded('premium alcohol, or driver tips.', 8),
        ],
    )
    return package, itinerary

def build_ga_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-010'
    tour_code = 'TRG-GOA-010'
    title = 'TRAGUIN Premium Goa Tour Package — Grand Goan Experience'
    duration = '09 Nights / 10 Days'
    slug = 'ga-010-grand-goan-experience'
    itin_slug = 'ga-010-grand-goan-experience-itinerary'
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
            _ph('Serial code GA-010 | TRAGUIN tour code TRG-GOA-010', 1),
            _ph('State / Country: Goa / India | Category: Premium Family Tour', 2),
            _ph('Destinations: North Goa • South Goa', 3),
            _ph('Ideal for: Families, Leisure Travelers & Multi- generational Groups', 4),
            _ph('Best season: October to April', 5),
            _ph('Starting price: On Request (Luxury Tailor- made Portfolio)', 6),
            _ph('Vehicle / Meals: Private Luxury AC', 7),
            _ph('TRAGUIN Signature Experience: Private family heritage tour through Fontainhas, led by a local', 8),
            _ph('Curated by TRAGUIN Experts: Seamless transfers between North and South Goa resorts, timed', 9),
            _ph('Premium Handpicked Hotels: Properties chosen specifically for their excellent safety records, premium', 10),
            _ph('Personalized Assistance: Dedicated on-ground coordinators to ensure VIP restaurant seating and fast-', 11),
            _ph('Local Markets & Souvenirs: Explore the vibrant Saturday Night Market or Anjuna Flea Market to find authentic hand-made jewelry, local terracotta artifacts, premium quality Goan cashews, and traditional Feni souvenirs. Cafes & Food: Old Goa and Panaji feature cozy, atmospheric heritage cafes serving classic bebinca desserts, freshly brewed local pour-over coffees, and delicious authentic prawn balchão recipes.', 12),
            _ph('Hotel Policies: Standard check-in begins at 14:00 hrs, and check-out is strictly at 11:00 hrs. Valid', 13)
        ],
        moods=['Family', 'Beach', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Luxury Tailor- made Portfolio)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Grand Goan Experience',
        overview="Welcome to a glorious sun-kissed escapade crafted to perfection by TRAGUIN. Presenting our signature Grand Goan Experience, curated specifically for travelers who refuse to compromise on class. This is the definitive Best Goa Tour Package, meticulously designed to uncover the soul of India's coastal paradise. Blending the breathtaking landscapes of pristine sandy fringes with the deep architectural legacy of Portuguese history, this itinerary guarantees premium stays and immersive experiences. Treat your loved ones to a magnificent mix of private cruises, handpicked hotels, and cultural milestones, leaving you with nothing but unforgettable memories.\n\nTOUR OVERVIEW\nYour upcoming escape is designed as a fully flexible, private FIT/Family voyage spanning 10 glorious days. Traveling across the scenic routes of both North and South Goa, your group will be chauffeured in a designated premium, air-conditioned vehicle with highly experienced assistance. The selected meal plan balances sophisticated hotel culinary spreads with access to local beachside dining recommendations. Every moment is enhanced by a signature TRAGUIN curated experience note—bringing you exclusive access, curated hidden trails, and around-the-clock VIP operational execution.\n\nWHY CHOOSE THE PREMIUM GOA EXPERIENCE?\nGoa is far more than a tropical beach retreat; it is an incredible tapestry of culture, heritage, and lush natural wonder. When choosing a Luxury Goa Holiday, travelers experience the dramatic contrast between the high- energy lifestyle of the northern beach stretch and the slow, peaceful rhythm of the south. From the historic bastions of Aguada and Chapora to the majestic cascading white waters of Dudhsagar Falls, Goa sightseeing caters beautifully to all age groups. For couples and families organizing a memorable Goa Honeymoon Package or an expansive Goa Family Tour, the region offers iconic attractions alongside popular Instagram locations. Take a stroll through the brightly painted Latin Quarter of Fontainhas, experience adrenaline-pumping luxury water sports, or sample world-class fusion cuisine at upscale seaside bistros. This meticulously planned route features the most searched experiences, handpicked luxury hotels, and hidden cultural treasures, ensuring you travel during the absolute best time to visit Goa with complete luxury and peace of mind.",
        seo_title='GA-010 | Goa | TRAGUIN',
        seo_description='Premium 09 Nights / 10 Days Goa package (GA-010 / TRG-GOA-010): North Goa • South Goa.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA – WELCOME TO PARADISE', 1),
            _ih('Day 02: NORTH GOA FORTRESSES & COASTAL VIEWS', 2),
            _ih('Day 03: HERITAGE TRAIL & OLD GOA CATHEDRALS', 3),
            _ih('Day 04: SPICE PLANTATION TOUR & REFRESHING CULINARY TRAIL', 4),
            _ih('Day 05: FONTAINHAS LATIN QUARTER & PRIVATE SUNSET CRUISE', 5),
            _ih('Day 06: NORTH GOA TO TRANQUIL SOUTH GOA', 6),
            _ih('Day 07: CASCADING DUDHSAGAR WATERFALLS', 7),
            _ih('Day 08: SOUTH GOA HIDDEN BEACH COVES', 8),
            _ih('Day 09: LEISURE DAY AT THE ULTRA-LUXURY RESORT', 9),
            _ih('Day 10: DEPARTURE FROM GOA', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA – WELCOME TO PARADISE',
                (
                    'EXCLUSIVE AIRPORT WELCOME & LUXURY RESORT CHECK-IN Your grand coastal holiday begins with an upscale arrival experience. As you land at Mopa (GGIA) or Dabolim Airport, a private luxury chauffeur extends a warm welcome and transfers you to your premium beachfront resort in North Goa. Enjoy a seamless, private check-in process followed by refreshing welcome amenities. Spend your afternoon unwinding by the azure pool or taking a private evening walk along the soft sandy shores of Candolim, capturing your first sunset photography points.'
                ),
                [
                    'Sightseeing Included: Private luxury airport transfer, Candolim beach sunset walk.',
                    'Evening Experience: Exclusive beachside dinner at the resort, custom-tailored by TRAGUIN.',
                    'Overnight Stay: North Goa Beach Resort (Premium / Luxury Category)',
                    'Meals Included: Welcome Drink & Luxury Welcome Dinner',
                ],
            ),            _day(
                2,
                'NORTH GOA FORTRESSES & COASTAL VIEWS',
                (
                    'EXPLORING ICONIC ATTRACTIONS & HISTORIC BASTIONS Indulge in a lavish buffet breakfast before heading out to discover the historic crown jewels of North Goa sightseeing. Visit the majestic 17th-century Fort Aguada, marveling at its perfectly preserved lighthouse and sweeping panoramic views of the Arabian Sea. Later, wind along beautiful coastal routes toward Chapora Fort, a popular Instagram location made famous by contemporary cinema. Spend your late afternoon experiencing the bohemian charm and dramatic red cliffs of Vagator Beach.'
                ),
                [
                    'Sightseeing Included: Fort Aguada, Sinquerim Beach, Chapora Fort, Vagator Beach Cliffs.',
                    'Optional Activities: Bespoke high-end paragliding or jet-skiing sessions with premium operators.',
                    'Overnight Stay: North Goa Beach Resort',
                    'Meals Included: Premium Breakfast & Gourmet Dinner',
                ],
            ),            _day(
                3,
                'HERITAGE TRAIL & OLD GOA CATHEDRALS',
                (
                    'A JOURNEY INTO SPIRITUALITY & PORTUGUESE ARCHITECTURE Dedicate your day to an enriching cultural journey into the heart of Old Goa, a UNESCO World Heritage site. Wander through the monumental Basilica of Bom Jesus, which holds the sacred relics of St. Francis Xavier, and admire the striking Manueline-style architecture of Se Cathedral. The route then takes you to the beautiful Mangueshi Temple, an architectural gem hidden among lush tropical hills. In the evening, explore local Goan lifestyle hubs and art spaces.'
                ),
                [
                    'Sightseeing Included: Basilica of Bom Jesus, Se Cathedral, Church of St. Cajetan, Mangueshi Temple.',
                    'Food Suggestions: Lunch at an upscale estate serving authentic Indo-Portuguese fusion recipes.',
                    'Overnight Stay: North Goa Beach Resort',
                    'Meals Included: Premium Breakfast & Curated Dinner',
                ],
            ),            _day(
                4,
                'SPICE PLANTATION TOUR & REFRESHING CULINARY TRAIL',
                (
                    'IMMERSIVE EXPERIENCES IN THE LAP OF NATURE Travel inland toward the historic town of Ponda for a truly immersive experience at a premium spice plantation. Walk hand-in-hand through dense fields of cardamom, vanilla, and exotic peppers while learning about traditional farming from an expert guide. Enjoy a traditional buffet lunch served on fresh banana leaves. Cap off your afternoon with a refreshing dip under a natural jungle canopy before heading back to the coast. Complimentary Experience: Traditional herbal welcome drink and organic spice tasting kit provided by TRAGUIN.'
                ),
                [
                    'Sightseeing Included: Guided Exotic Spice Plantation Tour, Ponda heritage countryside routes.',
                    'Overnight Stay: North Goa Beach Resort',
                    'Meals Included: Breakfast, Traditional Plantation Lunch & Dinner',
                ],
            ),            _day(
                5,
                'FONTAINHAS LATIN QUARTER & PRIVATE SUNSET CRUISE',
                (
                    "VIBRANT INSTAGRAM LOCATIONS & MANDOCI RIVER LUXURY Explore Panaji's magical Latin Quarter, Fontainhas. This popular Instagram location charms visitors with its narrow winding lanes, overhanging wooden balconies, and brightly colored pastel Portuguese homes. After a morning of heritage walks and souvenir shopping, transfer to a private luxury yacht on the Mandovi River. Glide gracefully along the water as the sun dips below the horizon, accompanied by live music and fine refreshments."
                ),
                [
                    'Sightseeing Included: Fontainhas Heritage Quarter, Panaji Church, Mandovi River Promenade.',
                    'Evening Experience: Private sunset yacht cruise with premium appetizers and select beverages.',
                    'Overnight Stay: North Goa Beach Resort',
                    'Meals Included: Premium Breakfast & Seafood Specialty Dinner',
                ],
            ),            _day(
                6,
                'NORTH GOA TO TRANQUIL SOUTH GOA',
                (
                    "TRANSITION TO UNTOUCHED COVES & SERENE TROPICAL LUXURY Say goodbye to the lively north as your private luxury vehicle takes you south toward an entirely different rhythm of Goan life. Check into your ultra-luxury resort nestled along South Goa's pristine shoreline. The afternoon is dedicated to absolute leisure—unwind on empty, expansive beaches, enjoy an award-winning spa therapy session, or read a book under a canopy of swaying palms."
                ),
                [
                    'Sightseeing Included: Scenic cross-country transition drive, Miramar Beach stopover.',
                    'Optional Activities: Premium Ayurvedic couple wellness therapy or high-tea at the resort lounge.',
                    'Overnight Stay: South Goa Luxury Resort (Ultra Luxury Category)',
                    'Meals Included: Premium Breakfast & Elegant Resort Buffet Dinner',
                ],
            ),            _day(
                7,
                'CASCADING DUDHSAGAR WATERFALLS',
                (
                    'THE MAJESTIC "SEA OF MILK" JUNGLE EXPEDITION Embark on a thrilling morning safari to Dudhsagar Falls, one of India\'s tallest and most spectacular waterfalls. Board a private 4x4 open jeep that winds through the lush core of the Bhagwan Mahavir Wildlife Sanctuary. Arrive at the base of the falls to witness the river crashing down from over 300 meters, creating a breathtaking "sea of milk." Enjoy swimming in the safe, natural pool under the supervision of expert handlers.'
                ),
                [
                    'Sightseeing Included: Dudhsagar Waterfalls base pool, Mollem National Park 4x4 Jeep Safari tracks.',
                    'Photography Points: The iconic railway bridge over the cascading falls, exotic jungle fauna.',
                    'Overnight Stay: South Goa Luxury Resort',
                    'Meals Included: Early Premium Breakfast & Curated Dinner',
                ],
            ),            _day(
                8,
                'SOUTH GOA HIDDEN BEACH COVES',
                (
                    'THE UNTOUCHED BEAUTY OF PALOLEM & AGONDA CORNERS Discover the crescent-shaped bays of Palolem and Agonda beaches, famed for their breathtaking landscapes and crystal-clear waters. Board a private local boat to spot dolphins playing in their natural habitat. Explore Honeymoon Beach and Butterfly Island—two secluded gems perfect for quiet relaxation and beautiful family photography. In the afternoon, enjoy a fresh meal at an upscale cliffside bistro overlooking the ocean.'
                ),
                [
                    'Sightseeing Included: Palolem Beach, Agonda Beach, Butterfly Island boat ride, Cabo de Rama Fort.',
                    'Evening Experience: Sunset viewing from the ancient clifftop ramparts of Cabo de Rama.',
                    'Overnight Stay: South Goa Luxury Resort',
                    'Meals Included: Premium Breakfast & Continental Dinner',
                ],
            ),            _day(
                9,
                'LEISURE DAY AT THE ULTRA-LUXURY RESORT',
                (
                    'RELAXATION & REFLECTION ON THE SOUTHERN SHORES Enjoy a completely relaxed day at your premium resort. Sleep in late, enjoy a breakfast in bed, or wander along the private beachfront. This day is designed to let you absorb the serene tropical beauty of your surroundings at your own pace, creating lasting family bonds and unforgettable memories.'
                ),
                [
                    'Sightseeing Included: At absolute individual leisure. Full access to resort facilities.',
                    'Optional Activities: A private cooking class with the resort’s executive chef, learning classic Goan curries.',
                    'Overnight Stay: South Goa Luxury Resort',
                    'Meals Included: Premium Breakfast & Custom Grand Farewell Dinner',
                ],
            ),            _day(
                10,
                'DEPARTURE FROM GOA',
                (
                    'CHERISHING THE MEMORIES OF A PERFECT TROPICAL GETAWAY Savor a final breakfast by the ocean before packing your bags. Your private luxury transport will pick you up from the resort lobby and transfer you safely to Mopa or Dabolim Airport for your flight home. Return with a sun-kissed glow and a collection of beautiful memories curated flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury point-to-point airport drop-off.',
                    'Meals Included: Lavish Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Resort & Spa / Lemon Tree Amarante | Kenilworth Resort / Heritage Village',
                'North Goa (5 Nights) / South Goa (4 Nights)',
                '09 Nights',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Novotel Resort & Spa / Lemon Tree Amarante (North Goa (5 Nights)) | Kenilworth Resort / Heritage Village (South Goa (4 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Hard Rock Hotel / Vivanta Goa Candolim | Caravela Beach Resort / Radisson Blu',
                'North Goa (5 Nights) / South Goa (4 Nights)',
                '09 Nights',
                'Premium',
                'Premium Room',
                'MAPAI Plan Portfolio',
                4,
                2,
                description='OPTION 02 – PREMIUM: Hard Rock Hotel / Vivanta Goa Candolim (North Goa (5 Nights)) | Caravela Beach Resort / Radisson Blu (South Goa (4 Nights)) | MAPAI Plan Portfolio',
            ),
            _hotel(
                'The O Hotel / W Goa (Wonderful Room) | Taj Exotica Resort & Spa (Luxury Room)',
                'North Goa (5 Nights) / South Goa (4 Nights)',
                '09 Nights',
                'Luxury',
                'Luxury Room',
                'Bespoke MAPAI Plan Spread',
                5,
                3,
                description='OPTION 03 – LUXURY: The O Hotel / W Goa (Wonderful Room) (North Goa (5 Nights)) | Taj Exotica Resort & Spa (Luxury Room) (South Goa (4 Nights)) | Bespoke MAPAI Plan Spread',
            ),
            _hotel(
                'The Leela Goa (Lagoon Suite) | The St. Regis Goa Resort (VVIP Ocean Villa)',
                'North Goa (5 Nights) / South Goa (4 Nights)',
                '09 Nights',
                'Ultra Luxury',
                'VVIP Ocean Villa',
                'Elite Custom Luxury Dining Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Leela Goa (Lagoon Suite) (North Goa (5 Nights)) | The St. Regis Goa Resort (VVIP Ocean Villa) (South Goa (4 Nights)) | Elite Custom Luxury Dining Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Domestic or international airfares, flight tickets, or', 1),
            _inc_excluded('railway berths.', 2),
            _inc_excluded('Any water sports fees, scuba diving entry, or', 3),
            _inc_excluded('adventure gear rental fees.', 4),
            _inc_excluded('Personal expenses such as laundry, room service,', 5),
            _inc_excluded('bar tabs, phone calls, and tips.', 6),
            _inc_excluded('Monument entry tickets, local camera permits, or', 7),
            _inc_excluded('discretionary guide tips.', 8),
        ],
    )
    return package, itinerary

def build_ga_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-012'
    tour_code = 'TRG-GOA-012'
    title = 'TRAGUIN Premium Goa Tour Package — Exotic Goa Honeymoon'
    duration = '04 Nights / 05 Days'
    slug = 'ga-012-exotic-goa-honeymoon'
    itin_slug = 'ga-012-exotic-goa-honeymoon-itinerary'
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
            _ph('Serial code GA-012 | TRAGUIN tour code TRG-GOA-012', 1),
            _ph('State / Country: Goa / India | Category: Luxury Honeymoon', 2),
            _ph('Destinations: North Goa (Candolim, Vagator) • South', 3),
            _ph('Ideal for: Newlyweds, Romantic Couples & Luxury Seekers', 4),
            _ph('Best season: October to April', 5),
            _ph('Starting price: On Request (Premium Customised)', 6),
            _ph('Vehicle / Meals: Private Premium', 7),
            _ph('TRAGUIN Signature Experience: Private beachside candle-lit dining with a customized 4-course menu.', 8),
            _ph('Curated by TRAGUIN Experts: Well-paced itinerary that avoids heavy tourist traffic, giving you plenty of', 9),
            _ph("Premium Handpicked Hotels: Accommodations selected for their high safety standards, couples' privacy,", 10),
            _ph('Luxury Transportation: Expert drivers who know the best hidden photography spots away from the', 11),
            _ph('Local Markets & Souvenirs: Explore the famous Anjuna Wednesday flea market or Panaji markets to find authentic Goan spices, premium cashews, hand-painted Azulejos tiles, and vibrant resort wear. Cafes & Food: Indulge in authentic Goan fish curry rice, Bebinca desserts, and artisanal wood-fired pizzas at boutique cliffside cafes overlooking the ocean in Vagator.', 12),
            _ph('Hotel Policies: Standard check-in time is 14:00 hrs and check-out is 11:00 hrs. Valid couple identification', 13)
        ],
        moods=['Romantic', 'Beach', 'Luxury'],
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
        tagline='Exotic Goa Honeymoon',
        overview="Welcome to an exquisite romantic escape crafted passionately by TRAGUIN. Embark on the ultimate Goa Honeymoon Package, meticulously planned to present the breathtaking landscapes, gold-sand coastlines, and colonial elegance of India's beach paradise. As your premium travel consultants, TRAGUIN transforms your romantic getaway into a high-end luxury holiday filled with premium stays, candle-lit milestones, and immersive experiences. Let the scenic beauty of the Arabian Sea and palm-fringed coastlines spark timeless magic, weaving unforgettable memories for you and your beloved.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers a masterfully curated balance between North Goa's vibrant, cosmopolitan coastal pulse and South Goa's serene, untouched tropical privacy. Travelling in an exclusive premium private AC vehicle driven by a highly professional chauffeur, your honeymoon is treated with total confidentiality and comfort. Complemented by handpicked hotels and a flexible meal plan, every detail contains the iconic TRAGUIN curated experience note, encompassing VIP sunset cruise access, beachside dining privileges, and specialized travel support.\n\nWHY CHOOSE THE BEST GOA TOUR PACKAGE?\nWhen shortlisting a Luxury Goa Holiday, newlyweds demand an ideal harmony of sun-soaked relaxation, heritage aesthetics, and culinary brilliance. Goa stands as an undisputed champion, rendering a Goa Honeymoon Package the ultimate romantic investment. From navigating legendary architectural monuments to capturing the panoramic scenic beauty from ocean-facing cliff tops, Goa sightseeing offers infinite wonders. For couples searching for a memorable Goa Family Tour or romantic retreat, the territory unveils highly sought-after, popular Instagram locations such as Fontainhas Latin Quarter, Cabo de Rama, and Vagator cliff edges. Indulge in premier boutique shopping at night markets, experience private yacht charters, or capture dramatic frames at iconic attractions like Aguada Fort. Our signature TRAGUIN Goa Packages fuse exclusive experiences with handpicked luxury stays, promising the absolute best time to visit Goa with effortless luxury.",
        seo_title='GA-012 | Goa | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Goa package (GA-012 / TRG-GOA-012): North Goa (Candolim, Vagator) • South.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA', 1),
            _ih('Day 02: NORTH GOA EXPLORATION', 2),
            _ih('Day 03: SOUTH GOA HERITAGE & ROMANTIC LUXURY CRUISE', 3),
            _ih('Day 04: UNTOUCHED SOUTH GOA ROMANCE', 4),
            _ih('Day 05: DEPARTURE FROM GOA', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA',
                (
                    'WELCOME TO COASTAL PARADISE – ROMANTIC SUNSET EXPERIENCE Your premium Goa experience begins as you step out of Manohar International Airport (MOPA) or Dabolim Airport, where a private luxury transport vehicle waits to receive you. Enjoy a refreshing drive to your handpicked premium coastal resort. Take the afternoon to settle into your luxury room. In the evening, step out for an exclusive experiences walk down Candolim beach to capture your first photography points against a blazing tropical sunset.'
                ),
                [
                    'Sightseeing Included: Candolim Coastal Beach Walk, Luxury Resort Ambiance.',
                    'Evening Experience: Romantic honeymoon cake cutting with complimentary wine in your room.',
                    'Overnight Stay: North Goa (Premium / Luxury Beachfront Resort)',
                    'Meals Included: Welcome Mocktail & Gourmet Welcome Dinner',
                ],
            ),            _day(
                2,
                'NORTH GOA EXPLORATION',
                (
                    'FORTRESS VISTAS, VIBRANT BEACHES & POPULAR INSTAGRAM LOCATIONS Awake to a lavish breakfast buffet before heading out for a comprehensive North Goa sightseeing tour. Explore the historic 17th-century Sinquerim Fort and the iconic Aguada Fort, offering spectacular panoramic vistas of the Arabian Sea. In the afternoon, head north towards the dramatic red cliffs of Vagator Beach and the bohemian shores of Anjuna. Spend your evening exploring high-end beach boutiques and enjoying seaside sundowners.'
                ),
                [
                    'Sightseeing Included: Aguada Fort, Sinquerim Beach, Vagator Cliff View, Anjuna Beach Promenade.',
                    'Optional Activities: Thrilling premium water sports (Jet skiing, parasailing) at Calangute beach.',
                    'Overnight Stay: North Goa (Premium / Luxury Beachfront Resort)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),            _day(
                3,
                'SOUTH GOA HERITAGE & ROMANTIC LUXURY CRUISE',
                (
                    'PORTUGUESE ARCHITECTURE & LUXURY PRIVATE YACHT EXPERIENCE Today, travel south to uncover the rich cultural roots of old colonial Goa. Walk hand-in-hand through the breathtaking Basilica of Bom Jesus and Se Cathedral, showcasing centuries-old Baroque architecture. Afterwards, explore Fontainhas, the famous Latin Quarter of Panaji, where pastel-colored Portuguese houses offer a stunning backdrop for photography. In the late afternoon, step aboard a luxury private boat cruise along the Mandovi River. experts.'
                ),
                [
                    'Sightseeing Included: Old Goa Churches, Fontainhas Latin Quarter, Miramar Beach, Mandovi Riverfront.',
                    'Evening Experience: Private sunset river cruise with live music and gourmet appetizers curated by TRAGUIN',
                    'Overnight Stay: South Goa (Premium / Ultra Luxury Serene Resort)',
                    'Meals Included: Breakfast & Heritage Thali Dinner',
                ],
            ),            _day(
                4,
                'UNTOUCHED SOUTH GOA ROMANCE',
                (
                    'PRISTINE BAY VISTAS & PRIVATE BEACHSIDE CANDLE-LIT DINNER Dedicate this day to pure relaxation and romance along the pristine shores of South Goa. Visit Palolem Beach, a crescent-shaped bay famed for its tranquil waters and scenic beauty. Relax under private beach shacks or take a small traditional boat out to spot dolphins. As twilight approaches, return to your resort where an exclusive, intimate surprise awaits you on the shores.'
                ),
                [
                    'Sightseeing Included: Palolem Beach, Colva Beach, Cabo de Rama Fort viewpoints.',
                    'Evening Experience: Bespoke candle-lit dinner right on the beach with private butler service.',
                    'Overnight Stay: South Goa (Premium / Ultra Luxury Serene Resort)',
                    'Meals Included: Premium Breakfast & Romantic Candle-lit Beach Dinner',
                ],
            ),            _day(
                5,
                'DEPARTURE FROM GOA',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES OF YESTERDAY Indulge in a final, lavish breakfast at your premium resort, looking out over the swaying coconut palms. Your private luxury transport will safely drive you to Goa Airport or Madgaon Railway Station for your journey home. Return with your hearts full of romance and unforgettable memories designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door airport or station drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Lemon Tree Amarante / similar | Heritage Village Resort / similar',
                'North Goa (2 Nights) / South Goa (2 Nights)',
                '04 Nights',
                'Deluxe',
                'Deluxe Room',
                'CP (Breakfast Only)',
                4,
                1,
                description='OPTION 01 – DELUXE: Lemon Tree Amarante / similar (North Goa (2 Nights)) | Heritage Village Resort / similar (South Goa (2 Nights)) | CP (Breakfast Only)',
            ),
            _hotel(
                'Novotel Goa Resort & Spa / similar | Caravela Beach Resort / similar',
                'North Goa (2 Nights) / South Goa (2 Nights)',
                '04 Nights',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Novotel Goa Resort & Spa / similar (North Goa (2 Nights)) | Caravela Beach Resort / similar (South Goa (2 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Taj Holiday Village / W Goa | The Leela Goa / Taj Exotica',
                'North Goa (2 Nights) / South Goa (2 Nights)',
                '04 Nights',
                'Luxury',
                'Luxury Suite',
                'MAPAI + Honeymoon Kit',
                5,
                3,
                description='OPTION 03 – LUXURY: Taj Holiday Village / W Goa (North Goa (2 Nights)) | The Leela Goa / Taj Exotica (South Goa (2 Nights)) | MAPAI + Honeymoon Kit',
            ),
            _hotel(
                'Taj Fort Aguada (Hermitage Villa) | The Leela Goa (Royal Villa Suite)',
                'North Goa (2 Nights) / South Goa (2 Nights)',
                '04 Nights',
                'Ultra Luxury',
                'Royal Villa Suite',
                'VVIP Custom Meal Curator Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Taj Fort Aguada (Hermitage Villa) (North Goa (2 Nights)) | The Leela Goa (Royal Villa Suite) (South Goa (2 Nights)) | VVIP Custom Meal Curator Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Airfare, flight tickets, or long-distance interstate train', 1),
            _inc_excluded('fares.', 2),
            _inc_excluded('Water sports, scuba diving, or club entry', 3),
            _inc_excluded('passes.', 4),
            _inc_excluded('Monument entry tickets, professional guide fees,', 5),
            _inc_excluded('camera permits.', 6),
            _inc_excluded('Personal expenses such as laundry, phone', 7),
            _inc_excluded('calls, or tips.', 8),
        ],
    )
    return package, itinerary

def build_ga_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-013'
    tour_code = 'TRG-GOA-013'
    title = 'TRAGUIN Premium Goa Tour Package — Luxury Sunset Romance Honeymoon Escape'
    duration = '05 Nights / 06 Days'
    slug = 'ga-013-luxury-sunset-romance-honeymoon'
    itin_slug = 'ga-013-luxury-sunset-romance-honeymoon-itinerary'
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
            _ph('Serial code GA-013 | TRAGUIN tour code TRG-GOA-013', 1),
            _ph('State / Country: Goa / India | Category: Luxury Honeymoon', 2),
            _ph('Destinations: Candolim •', 3),
            _ph('Ideal for: Newlyweds, Romance Seekers & Discerning Travelers', 4),
            _ph('Best season: November to April', 5),
            _ph('Starting price: On Request (Premium Customized Proposal)', 6),
            _ph('Vehicle / Meals: Private Luxury', 7),
            _ph('TRAGUIN Signature Experience: Private oceanfront candlelit dinner table setup with dedicated butler', 8),
            _ph('Curated by TRAGUIN Experts: A relaxed itinerary that blends exploring with plenty of private couple time.', 9),
            _ph('Premium Handpicked Hotels: Resorts selected for excellent service, prime beachfront locations, and', 10),
            _ph('Luxury Transportation: Uniformed local drivers who know the best routes and secret lookouts.', 11),
            _ph('Local Markets & Souvenirs: Explore the Wednesday Anjuna Flea Market or the Saturday Night Market in Arpora. Pick up fine Goan hand-painted ceramic tiles (Azulejos), organic cashews, rich bebinca dessert cakes, and boutique beachwear. Cafes & Food: Old Goa and Fontainhas feature charming cafes serving authentic Goan fish curry, prawn balchão, wood-fired pizzas, and fresh local fruit juices with live acoustic background music.', 12),
            _ph('Hotel Policies: Check-in time is generally 14:00 hrs and check-out is 11:00 hrs. A valid government photo', 13)
        ],
        moods=['Romantic', 'Beach', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customized Proposal)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Luxury Sunset Romance Honeymoon Escape',
        overview="HONEYMOON ESCAPE Welcome to a heavenly oceanfront paradise curated exclusively by TRAGUIN. Embark on the absolute ultimate Goa Honeymoon Package, meticulously crafted to immerse you and your loved one in breathtaking landscapes, sun-kissed golden sands, and legendary colonial charm. As your premier luxury travel consultants, TRAGUIN transforms your getaway into a romantic haven, combining premium stays, intimate candlelit beachside dinners, and handpicked hotels. Let the rhythm of the waves, historic fortresses, and sunset cruises frame your shared joy, creating unforgettable memories to treasure forever.\n\nTOUR OVERVIEW\nThis bespoke luxury holiday itinerary balances sun-drenched coastal relaxation with deeply rich cultural discovery. Travelling exclusively in a dedicated private premium air-conditioned vehicle with background- verified chauffeur assistance, your comfort is guaranteed from touchdown to departure. Featuring a tailored meal plan with lavish daily breakfasts and specialized intimate dining experiences, this route encompasses the absolute highest tier of a premium Goa experience. Every moment of your journey includes signature TRAGUIN curated experiences, including VIP beach lounge access, private luxury boat charting, and continuous expert travel assistance.\n\nWHY CHOOSE THE BEST GOA TOUR PACKAGE?\nWhen planning a Luxury Goa Holiday, couples look for pristine beach privacy, world-class culinary art, and high-end coastal luxury. Goa stands out as India's ultimate beach escape, making a Goa Honeymoon Package the premier choice for newlyweds. From the historic fortifications of Aguada and Chapora to the quiet, untouched sands of South Goa, Goa sightseeing offers something magical for every romantic couple. Our highly tailored Goa Family Tour and romantic escapes connect you directly to popular Instagram locations like the Latin Quarter of Fontainhas, the grand white-washed colonial cathedrals of Old Goa, and secluded coves perfect for sunset photography points. Discover elite boutique shopping, local spice plantations, and beachfront shacks serving freshly caught, masterfully spiced seafood. With our signature TRAGUIN Goa Packages, expect premium comfort, handpicked hotels, and exclusive experiences during the absolute best time to visit Goa.",
        seo_title='GA-013 | Goa | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Goa package (GA-013 / TRG-GOA-013): Candolim •.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA & SUNSET REVERIE', 1),
            _ih('Day 02: NORTH GOA ICONIC SIGHTSEEING', 2),
            _ih('Day 03: HERITAGE WALK IN FONTAINHAS & OLD GOA', 3),
            _ih('Day 04: TRANSFER TO SOUTH GOA & PRIVATE YACHT EXPERIENCE', 4),
            _ih('Day 05: SOUTH GOA BEACH SERENITY & COUPLES SPA', 5),
            _ih('Day 06: FINAL OCEAN VIEW & DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA & SUNSET REVERIE',
                (
                    'WELCOME TO THE SUNSHINE STATE – COASTAL LUXURY & PRIVATE CHECK-IN Your premium Goa experience begins as your private luxury transport vehicle meets you at Goa Airport (Mopa/Dabolim). Enjoy cold towels and complimentary refreshments on your smooth drive to a handpicked premium luxury resort in North Goa. After checking into your private plunge pool suite, spend a relaxed afternoon unpacking and enjoying resort amenities. As twilight approaches, a reserved beachfront canopy awaits you to witness a glorious golden sunset over the Arabian Sea. custom wedding cake.'
                ),
                [
                    'Sightseeing Included: Private beach access, sunset viewing canopy at Sinquerim Beach.',
                    'Evening Experience: Honeymoon Special: Chilled sparkling wine, a premium flower-bed arrangement, and a',
                    'Overnight Stay: North Goa (Premium Beachfront Resort & Spa)',
                    'Meals Included: Welcome Drink & Luxury Welcome Dinner',
                ],
            ),            _day(
                2,
                'NORTH GOA ICONIC SIGHTSEEING',
                (
                    'HISTORIC FORTRESSES & EXCLUSIVELY CURATED BEACH CABANAS Savor a lavish buffet breakfast before heading out on a tailored North Goa sightseeing tour. Visit the majestic 17th-century Aguada Fort, where the historic lighthouse overlooks the vast ocean. Next, journey to the dramatic cliffs of Chapora Fort, a highly popular Instagram location with expansive panoramic views. In the afternoon, explore the bohemian boutiques of Anjuna and Vagator before relaxing in a private beach cabana with VIP entry. TRAGUIN experts.'
                ),
                [
                    'Sightseeing Included: Aguada Fort, Chapora Fort, Vagator Beach overlook, premium coastal lookouts.',
                    'Evening Experience: An intimate beachside candlelit dinner with a personalized seafood menu curated by',
                    'Overnight Stay: North Goa (Premium Beachfront Resort & Spa)',
                    'Meals Included: Premium Breakfast & Candlelit Oceanfront Dinner',
                ],
            ),            _day(
                3,
                'HERITAGE WALK IN FONTAINHAS & OLD GOA',
                (
                    "LATIN QUARTER ROMANCE & MAJESTIC COLONIAL ARCHITECTURE Immerse yourselves in history today with an exclusive walking tour through Fontainhas, Panaji's historic Latin Quarter. Stroll hand-in-hand along bright yellow and terracotta Portuguese-style heritage homes, tile-roofed cottages, and lovely art galleries. Afterwards, your chauffeur will drive you to the UNESCO World Heritage sites of Old Goa. Tour the Basilica of Bom Jesus and the majestic Se Cathedral, capturing incredible photos of their timeless architecture. Cajetan. Panaji."
                ),
                [
                    'Sightseeing Included: Fontainhas Latin Quarter walk, Basilica of Bom Jesus, Se Cathedral, Church of St.',
                    'Optional Activities: A guided tasting tour of local heritage feni or an artisanal coffee pairing experience in',
                    'Overnight Stay: North Goa (Premium Beachfront Resort & Spa)',
                    'Meals Included: Premium Breakfast & Traditional Indo-Portuguese Gourmet Dinner',
                ],
            ),            _day(
                4,
                'TRANSFER TO SOUTH GOA & PRIVATE YACHT EXPERIENCE',
                (
                    'UNTOUCHED PARADISE & SUNSET CRUISE PRIVILEGE Check out of North Goa after breakfast and take a scenic drive south to an ultra-luxury resort nestled among peaceful, pristine sands. South Goa is known for its breathtaking landscapes and calm beaches. In the late afternoon, step aboard an exclusive private luxury yacht charter arranged by TRAGUIN. Cruise along the coast while enjoying premium drinks and light bites, taking in a stunning, uninterrupted ocean sunset.'
                ),
                [
                    'Sightseeing Included: Scenic countryside drive, private catamaran/yacht coastal routing.',
                    'Evening Experience: Sunset yacht cruise with live acoustic music and a private butler on board.',
                    'Overnight Stay: South Goa (Ultra-Luxury Resort & Spa)',
                    'Meals Included: Premium Breakfast & Deck Dinner',
                ],
            ),            _day(
                5,
                'SOUTH GOA BEACH SERENITY & COUPLES SPA',
                (
                    "PURE LEISURE, BLISSFUL COVES & REJUVENATION Dedicate your day to pure relaxation and luxury. Visit the crescent-shaped Palolem Beach, celebrated for its scenic beauty and calm waters. Take a private rowboat to Butterfly Beach, a hidden cove perfect for spotting dolphins and enjoying a secluded beachside walk. Return to your resort for a 90-minute signature couples' Ayurvedic massage and spa treatment."
                ),
                [
                    'Sightseeing Included: Palolem Beach walk, secret dolphin cove boat spotting.',
                    'Optional Activities: A fine-dining beach picnic with premium wine and charcuterie boards.',
                    'Overnight Stay: South Goa (Ultra-Luxury Resort & Spa)',
                    'Meals Included: Premium Breakfast & Farewell Dinner',
                ],
            ),            _day(
                6,
                'FINAL OCEAN VIEW & DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES UNTIL WE MEET AGAIN Enjoy a final leisurely breakfast while looking out over the clear blue waters of the Arabian Sea. Take one last walk along the soft sands before your private luxury transport arrives to drive you to Goa Airport for your return flight. Head home carrying a heart full of romance and unforgettable memories designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury chauffeured airport terminal drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Goa Resort & Spa / similar | Caravela Beach Resort / similar',
                'North Goa (3 Nights) / South Goa (2 Nights)',
                '05 Nights',
                'Deluxe',
                'Superior Garden View Room',
                'CP (Breakfast)',
                4,
                1,
                description='OPTION 01 – DELUXE: Novotel Goa Resort & Spa / similar (North Goa (3 Nights)) | Caravela Beach Resort / similar (South Goa (2 Nights)) | CP (Breakfast)',
            ),
            _hotel(
                'Taj Holiday Village Resort & Spa | Taj Exotica Resort & Spa Goa',
                'North Goa (3 Nights) / South Goa (2 Nights)',
                '05 Nights',
                'Premium',
                'Premium Private Balcony Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Taj Holiday Village Resort & Spa (North Goa (3 Nights)) | Taj Exotica Resort & Spa Goa (South Goa (2 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'W Goa / Alila Diwa Goa | The Leela Goa (Riverside)',
                'North Goa (3 Nights) / South Goa (2 Nights)',
                '05 Nights',
                'Luxury',
                'Luxury Ocean Sea-Facing Suite',
                'MAPAI + Honeymoon Kit',
                5,
                3,
                description='OPTION 03 – LUXURY: W Goa / Alila Diwa Goa (North Goa (3 Nights)) | The Leela Goa (Riverside) (South Goa (2 Nights)) | MAPAI + Honeymoon Kit',
            ),
            _hotel(
                'The Cape Goa / Taj Fort Aguada (Villa) | The St. Regis Goa Resort',
                'North Goa (3 Nights) / South Goa (2 Nights)',
                '05 Nights',
                'Ultra Luxury',
                'VVIP Private Plunge Pool Sea Villa',
                'VVIP Custom Meal Curator Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Cape Goa / Taj Fort Aguada (Villa) (North Goa (3 Nights)) | The St. Regis Goa Resort (South Goa (2 Nights)) | VVIP Custom Meal Curator Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Domestic or International flight tickets to/from', 1),
            _inc_excluded('Water sports, scuba diving, and adventure activity', 2),
            _inc_excluded('Monument, fort, and museum entry ticket', 3),
            _inc_excluded('costs.', 4),
            _inc_excluded('Personal items, laundry, phone calls, tips, and', 5),
            _inc_excluded('drinks.', 6),
        ],
    )
    return package, itinerary

def build_ga_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-014'
    tour_code = 'TRG-GOA-014'
    title = 'TRAGUIN Premium Goa Tour Package — Girls Trip to Goa'
    duration = '04 Nights / 05 Days'
    slug = 'ga-014-girls-trip-to-goa'
    itin_slug = 'ga-014-girls-trip-to-goa-itinerary'
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
            _ph('Serial code GA-014 | TRAGUIN tour code TRG-GOA-014', 1),
            _ph('State / Country: Goa / India | Category: Female Only / Girls', 2),
            _ph('Destinations: North Goa Beaches •', 3),
            _ph('Ideal for: Girls Getaways, Solo Female Groups & Luxury Seekers', 4),
            _ph('Best season: November to April', 5),
            _ph('Starting price: On Request (Premium Bespoke Curation)', 6),
            _ph('Vehicle / Meals: Private Chauffeur-', 7),
            _ph('TRAGUIN Signature Experience: Private sunset yacht charter down the Mandovi River with wine and', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked stylish café itineraries and pre-vetted female-safe nightlife', 9),
            _ph('Premium Handpicked Hotels: Elite properties selected for their exceptional hospitality, prime locations,', 10),
            _ph('Luxury Transportation: Courteous, well-experienced chauffeurs offering seamless, round-the-clock point-', 11),
            _ph("Local Markets & Souvenirs: Explore the vibrant Saturday Night Bazaar or Anjuna flea markets for beautiful resort wear, handmade silver jewelry, and unique boho accessories. Don't forget to pick up premium Goan cashews and artisanal feni. Cafes & Food: Indulge in fresh wood-fired pizzas, authentic Portuguese-Goan fusion curries, and specialty iced coffees at the aesthetic cafes hidden throughout Assagao and Old Manali's sister beach strips.", 12),
            _ph('Hotel Policies: Check-in time is typically 14:00 hrs and check-out is 11:00 hrs. Valid photo IDs are', 13)
        ],
        moods=['Beach', 'Luxury', 'Romantic'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Bespoke Curation)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Girls Trip to Goa',
        overview="SISTERHOOD Welcome to an ultra-chic, empowering, and absolute luxury escape curated exclusively by TRAGUIN. Embark on the ultimate Goa Family Tour alternative—the ultimate Girls Trip to Goa designed specifically to reveal the breathtaking landscapes, sun-kissed beaches, and eclectic vintage soul of India's coastal crown jewel. As your premium travel consultants, TRAGUIN transforms your getaway into a seamless luxury holiday filled with handpicked hotels, vibrant nightlife access, and deep cultural touchpoints. Gather your inner circle and let the scenic beauty of emerald waters and retro Latin quarters frame your unforgettable memories.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers the perfect balance of glamorous relaxation, high-end beach-club hopping, historical walks, and absolute private safety. Moving about in a dedicated private premium vehicle driven by a highly professional, background-verified chauffeur, your group will experience unparalleled comfort. Featuring an exquisite meal plan with delicious continental breakfasts and curated oceanfront dinners, this route represents the definitive premium Goa experience. Every step of your journey includes the signature touch of TRAGUIN curated experiences, ensuring VIP lounge entry, special girls' sundowner highlights, and 24/7 localized support.\n\nWHY CHOOSE THE BEST GOA TOUR PACKAGE?\nWhen planning a Luxury Goa Holiday with your close girlfriends, you seek an itinerary that blends high-end comfort with spectacular bohemian aesthetics. Goa stands out as the ultimate destination for female-focused luxury travels, easily shifting between the historic colonial charm of South Goa and the high-octane lifestyle venues of North Goa. From exploring the top tourist places in Goa like the 17th-century luxury fortresses to relaxing under swaying palms, Goa sightseeing never fails to captivate. For women designing a customized Goa Honeymoon Package style bachelorette or an exclusive Goa Family Tour, the state offers beautiful, popular Instagram locations like the pastel-hued streets of Fontainhas, the dramatic cliffside cafes of Vagator, and premium private yachts sailing down the Mandovi River. Whether you are looking for designer boutique shopping, indulging in local seafood and feni mixology, or finding zen at a premium yoga wellness retreat, our TRAGUIN Goa Packages ensure immersive experiences and premium stays, making any time the best time to visit Goa.",
        seo_title='GA-014 | Goa | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Goa package (GA-014 / TRG-GOA-014): North Goa Beaches •.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA – CHIC NORTH GOA WELCOME', 1),
            _ih('Day 02: FONTAINHAS LATIN QUARTER & PRIVATE YACHT', 2),
            _ih('Day 03: NORTH GOA ICONIC BEACHES & CAFE HOPPING', 3),
            _ih('Day 04: HERITAGE SOUTH GOA CHILL OUT', 4),
            _ih('Day 05: DEPARTURE WITH FOREVER MEMORIES', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA – CHIC NORTH GOA WELCOME',
                (
                    'GLAMOROUS SUNSET CHILL & SUNDOWNER REVELRY Your premium Goa experience kicks off with a grand airport reception as your private luxury transport vehicle whisks you away to an ultra-exclusive beach resort in North Goa. Upon check-in, enjoy complimentary welcome cocktails and custom-curated goodie bags. In the afternoon, dress up for your first spectacular and watch the golden sun dip below the horizon.'
                ),
                [
                    'evening experience: a private sunset cabana reservation at a top-tier beach club. Enjoy premium mixology',
                    'Sightseeing Included: Scenic coastal drive, premium beachfront property ambiance.',
                    'Evening Experience: VIP cabana seating and sundowner experience curated by TRAGUIN experts.',
                    'Overnight Stay: North Goa (Premium / Luxury Beachfront Resort)',
                    'Meals Included: Welcome Mocktails & Luxury Oceanside Dinner',
                ],
            ),            _day(
                2,
                'FONTAINHAS LATIN QUARTER & PRIVATE YACHT',
                (
                    'PASTEL STREET PHOTOGRAPHY & HIGH-SEAS LUXURY Indulge in a delicious breakfast before heading to Panaji for a guided walk through Fontainhas, the oldest Latin Quarter in Asia. This is a highly popular Instagram location filled with bright yellow, blue, and terracotta Portuguese-era villas. Capture beautiful portraits along the cobblestone pathways. Late in the afternoon, board an exclusive private luxury yacht charter for your group. Cruise down the peaceful waters with custom music, fine wine, and delicious appetizers.'
                ),
                [
                    'Sightseeing Included: Fontainhas Latin Quarter, Panaji Church, Mandovi River waterfront.',
                    'Optional Activities: A professional drone photography session during the private yacht cruise.',
                    'Overnight Stay: North Goa (Premium / Luxury Beachfront Resort)',
                    'Meals Included: Premium Breakfast & Sunset Yacht Canapés',
                ],
            ),            _day(
                3,
                'NORTH GOA ICONIC BEACHES & CAFE HOPPING',
                (
                    'BOHO-CHIC BAZAARS & CLIFFSIDE SUNSETS Spend a beautiful day exploring the famous attractions of North Goa. Visit the historic Aguada Fort overlook for sweeping ocean vistas, then head to the bohemian sands of Ashvem and Mandrem beaches. These pristine stretches offer breathtaking landscapes and a quiet escape from the crowds. Enjoy a late lunch at an organic beachfront cafe before exploring high-end designer boutiques for local resort wear and chic souvenirs.'
                ),
                [
                    'Sightseeing Included: Fort Aguada, Vagator Cliffside views, Ashvem beach walk.',
                    'Evening Experience: Reserved fine dining at a cliffside Greek or Mediterranean restaurant.',
                    'Overnight Stay: North Goa (Premium / Luxury Beachfront Resort)',
                    'Meals Included: Premium Breakfast & Fine Dining Dinner',
                ],
            ),            _day(
                4,
                'HERITAGE SOUTH GOA CHILL OUT',
                (
                    'COLONIAL MANSIONS & WHITE SAND SERENITY Switch to the peaceful, scenic beauty of South Goa today. Explore the historic Basilica of Bom Jesus and experience the imperial scale of a beautifully restored Portuguese mansion, complete with private high tea. Afterward, spend your afternoon relaxing on the soft white sands of Utorda or Palolem beach, enjoying an exclusive, quiet escape.'
                ),
                [
                    'Sightseeing Included: Old Goa Churches, Ancestral Heritage Mansion, South Goa White-Sand Beaches.',
                    'Optional Activities: Bespoke spice plantation tour with an artisanal Goan buffet lunch.',
                    'Overnight Stay: South Goa or North Goa Luxury base',
                    'Meals Included: Breakfast & Farewell Fusion Dinner',
                ],
            ),            _day(
                5,
                'DEPARTURE WITH FOREVER MEMORIES',
                (
                    'SAYING GOODBYE TO THE COAST – MEMORIES BEYOND DESTINATIONS Indulge in a final morning breakfast and perhaps a relaxing dip in the infinity pool. Your private chauffeur will take care of your transfers back to Goa International Airport (Mopa/Dabolim). Return home with endless laughs, strengthened bonds, and unforgettable memories designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door airport drop-off service.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Goa Resort & Spa / similar | Kenilworth Resort / similar',
                'North Goa (3 Nights) / South Goa (1 Night)',
                '04 Nights',
                'Deluxe',
                'Superior Garden View Room',
                'CP (Breakfast)',
                4,
                1,
                description='OPTION 01 – DELUXE: Novotel Goa Resort & Spa / similar (North Goa (3 Nights)) | Kenilworth Resort / similar (South Goa (1 Night)) | CP (Breakfast)',
            ),
            _hotel(
                'The O Resort & Spa / Hilton Goa | Caravela Beach Resort / similar',
                'North Goa (3 Nights) / South Goa (1 Night)',
                '04 Nights',
                'Premium',
                'Premium Pool Access / Balcony Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The O Resort & Spa / Hilton Goa (North Goa (3 Nights)) | Caravela Beach Resort / similar (South Goa (1 Night)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'W Goa (Vagator) / Taj Holiday Village | Taj Exotica Resort & Spa Goa',
                'North Goa (3 Nights) / South Goa (1 Night)',
                '04 Nights',
                'Luxury',
                'Luxury Ocean Sea View Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: W Goa (Vagator) / Taj Holiday Village (North Goa (3 Nights)) | Taj Exotica Resort & Spa Goa (South Goa (1 Night)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Leela Goa (The Club Suites) | Ahilya by the Sea (Private Villa)',
                'North Goa (3 Nights) / South Goa (1 Night)',
                '04 Nights',
                'Ultra Luxury',
                'VVIP Custom Private Luxury Pool Villa',
                'VVIP Custom Dining Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Leela Goa (The Club Suites) (North Goa (3 Nights)) | Ahilya by the Sea (Private Villa) (South Goa (1 Night)) | VVIP Custom Dining Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Airfare, flight tickets, or long-distance train', 1),
            _inc_excluded('bookings.', 2),
            _inc_excluded('Water sports, scuba diving, club entry passes, or', 3),
            _inc_excluded('table covers.', 4),
            _inc_excluded('Monument or museum tickets, camera entry', 5),
            _inc_excluded('fees, local guides.', 6),
            _inc_excluded('Personal expenses such as laundry, alcohol, tips,', 7),
            _inc_excluded('and spa treatments.', 8),
        ],
    )
    return package, itinerary

def build_ga_015(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-015'
    tour_code = 'TRG-GOA-015'
    title = 'TRAGUIN Premium Goa Tour Package — Relaxed Old Goa & Temples'
    duration = '04 Nights / 05 Days'
    slug = 'ga-015-relaxed-old-goa-temples'
    itin_slug = 'ga-015-relaxed-old-goa-temples-itinerary'
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
            _ph('Serial code GA-015 | TRAGUIN tour code TRG-GOA-015', 1),
            _ph('State / Country: Goa / India | Category: Premium Senior', 2),
            _ph('Destinations: Panaji • Old Goa • Ponda Temples • Miramar •', 3),
            _ph('Ideal for: Senior Citizens, Family Groups & Heritage Connoisseurs', 4),
            _ph('Best season: October to April', 5),
            _ph('Starting price: On Request (Bespoke Senior Luxury Customised)', 6),
            _ph('Vehicle / Meals: Private Luxury AC', 7),
            _ph('TRAGUIN Signature Experience: VIP pre-arranged darshan entries at Ponda temples to minimize waiting', 8),
            _ph('Curated by TRAGUIN Experts: Pacing designed with generous afternoon rest blocks, ideal for senior', 9),
            _ph('Premium Handpicked Hotels: Properties meticulously chosen for their step-free layouts, manicured', 10),
            _ph('Luxury Transportation: Chauffeurs skilled in defensive, smooth highway and city driving for maximum', 11),
            _ph('Local Souvenirs: Shop for world-renowned premium Goa whole cashews, authentic local feni, handcrafted Portuguese-style azulejos ceramic tiles, and lovely clay artifacts at the Government handicraft emporium. Mouthwatering Delicacies: Sample mild Bebinca and Dodol (traditional Goan sweets), fresh coconut-based vegetarian curries, and locally made artisan fruit preserves at the spice orchard.', 12),
            _ph('Hotel Policies: Check-in is at 14:00 hrs; check-out is at 11:00 hrs. Early check-in can be requested in', 13)
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
        price_note='On Request (Bespoke Senior Luxury Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Relaxed Old Goa & Temples',
        overview='SERENITY Welcome to a beautifully paced, soul-stirring coastal escape curated exclusively by TRAGUIN. Designed thoughtfully as a relaxed Goa Senior Citizen Holiday, this unique itinerary invites you to discover the spiritual majesty, architectural brilliance, and peaceful rhythms of legendary Old Goa. As your dedicated luxury travel consultants, TRAGUIN ensures a perfectly balanced journey featuring premium stays, smooth low-stride transport, and immersive experiences that cater explicitly to your comfort. Witness breathtaking landscapes, historic shrines, and gentle river tides while creating unforgettable memories with absolute peace of mind.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package focuses deeply on comfort, accessibility, and leisurely enrichment. Travelling in a dedicated private premium AC vehicle managed by a courteous, background- verified chauffeur, our esteemed guests will encounter no hurried schedules. Our route traces a gentle, low- walking path through the beautiful Latin Quarters, grand colonial basilicas, and highly sacred spiritual sanctuaries of Ponda. With a carefully selected premium meal plan serving mild, highly refined culinary options, every detail carries the distinct TRAGUIN curated experience note, guaranteeing priority seating, wheel-chair accessibility options where needed, and continuous care.\n\nWHY CHOOSE THE BEST GOA TOUR PACKAGE FOR SENIORS?\nWhen seeking a Luxury Goa Holiday, travelers often look past the bustling nightlife to discover a realm of quiet grandeur, ancient spirituality, and timeless charm. Goa reveals its most profound cultural treasures within its majestic heritage zone, making a specialized Goa Family Tour or senior escape highly sought after. From exploring world-heritage iconic attractions like the Basilica of Bom Jesus to paying homage at the tranquil Mangueshi Temple, Goa sightseeing offers deep spiritual fulfilment. For families and seniors booking a custom Goa Honeymoon Package or an elegant heritage retreat, the destination boasts highly popular Instagram locations like the pastel-hued streets of Fontainhas and the serene spice plantations of Ponda. Indulge in authentic local handicraft shopping, relax by the calm waters of Miramar Beach, or partake in a gentle sunset cruise along the Mandovi River. Our signature TRAGUIN Goa Packages blend these exclusive experiences seamlessly with handpicked hotels, providing you the absolute best time to visit Goa with complete luxury and comfort.',
        seo_title='GA-015 | Goa | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Goa package (GA-015 / TRG-GOA-015): Panaji • Old Goa • Ponda Temples • Miramar •.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN PANAJI (GOA)', 1),
            _ih('Day 02: RELEXED OLD GOA EXPLORATION', 2),
            _ih('Day 03: PONDA SPIRITUAL TEMPLE TOUR & SPICE ORCHARD', 3),
            _ih('Day 04: RELEXED PANAJI SIGHTSEEING & SUNSET RIVERSIDE CRUISE', 4),
            _ih('Day 05: DEPARTURE FROM GOA', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN PANAJI (GOA)',
                (
                    'WARM WELCOME & LATIN QUARTER AMBIANCE Your premium Goa experience begins as you step out of Mopa or Dabolim Airport, where your private luxury vehicle and an attentive chaperone await. Enjoy a smooth, scenic drive to your handpicked premium resort nestled away from the crowds. Receive a warm welcome note and refreshing amenities upon check-in. In the late afternoon, enjoy a very gentle, slow-paced drive through Fontainhas, the celebrated Latin Quarter of Panaji, filled with vibrant Portuguese-era heritage architecture and excellent photography points.'
                ),
                [
                    'Sightseeing Included: Fontainhas Latin Quarter heritage drive, Altinho hill view layout.',
                    'Evening Experience: Relaxed welcome high-tea and orientation session arranged by our destination manager.',
                    'Overnight Stay: Panaji / Central Goa (Premium Luxury Heritage Resort)',
                    'Meals Included: Welcome Drink, High Tea & Luxury Buffet Dinner',
                ],
            ),            _day(
                2,
                'RELEXED OLD GOA EXPLORATION',
                (
                    'GRAND COLONIAL ARCHITECTURE & HISTORIC BASILICAS Indulge in a wholesome breakfast before heading out to Old Goa, the former historical capital of Portuguese India. Explore the monumental Basilica of Bom Jesus, which holds the sacred remains of St. Francis Xavier, and the grand Se Cathedral across the plaza. Both sites feature flat, paved entry paths for ease of access. Enjoy immersive experiences as our expert guide narrates the deep histories behind these massive structures without any rushed timelines.'
                ),
                [
                    'Sightseeing Included: Basilica of Bom Jesus, Se Cathedral, Church of St. Cajetan.',
                    'Optional Activities: A quiet sitting session inside the historic, beautifully cooled prayer halls.',
                    'Overnight Stay: Panaji / Central Goa (Premium Luxury Heritage Resort)',
                    'Meals Included: Premium Breakfast & Gourmet Dinner',
                ],
            ),            _day(
                3,
                'PONDA SPIRITUAL TEMPLE TOUR & SPICE ORCHARD',
                (
                    'SACRED HERITAGE, SHANTI & TRADITIONAL FLAVORS Dedicate today to the sacred, peaceful temples of Ponda. Visit the highly revered 450-year-old Shri Mangueshi Temple, dedicated to Lord Shiva, known for its elegant multi-story lamp tower (Deepastambha). Next, visit the beautiful Shri Shanta Durga Temple, nestled inside a tranquil valley. Following your temple darshan, enjoy a private curated experience at a premium spice plantation, where you will receive a traditional marigold garland welcome, a slow guided level walk under lush canopies, and a mild, authentic Goan Saraswat lunch.'
                ),
                [
                    'Sightseeing Included: Mangueshi Temple, Shanta Durga Temple, Sahakari Spice Farm Plantation.',
                    'Evening Experience: Relaxed stroll through the spice gardens with an aromatic herbal tea tasting.',
                    'Overnight Stay: Panaji / Central Goa (Premium Luxury Heritage Resort)',
                    'Meals Included: Breakfast, Traditional Buffet Lunch & Dinner',
                ],
            ),            _day(
                4,
                'RELEXED PANAJI SIGHTSEEING & SUNSET RIVERSIDE CRUISE',
                (
                    'SCENIC PROMENADES & EXCLUSIVE WATERWAYS Savor a lazy morning at your resort, taking advantage of the premium luxury amenities. In the afternoon, take a comfortable drive down the scenic Miramar Beach promenade to enjoy the refreshing coastal views. Later, head towards the Mandovi River jetty to board a private luxury catamaran or premium sunset cruise liner. Watch the golden sun dip below the Arabian Sea while listening to soft local music—an exquisite way to collect unforgettable memories.'
                ),
                [
                    'Sightseeing Included: Miramar Beach view drive, Panaji Church square, Mandovi River waterfront.',
                    'Evening Experience: Premium Sunset Cruise on the Mandovi River with reserved lower-deck lounge seating.',
                    'Overnight Stay: Panaji / Central Goa (Premium Luxury Heritage Resort)',
                    'Meals Included: Breakfast & Farewell Premium Dinner',
                ],
            ),            _day(
                5,
                'DEPARTURE FROM GOA',
                (
                    "CHERISHING THE TRANQUIL MOMENTS Enjoy a leisurely final breakfast at the resort's open-air veranda. Your private luxury transportation vehicle will be ready at your preferred time to ensure a stress-free transfer back to Goa Airport or Railway Station. Return home feeling fully refreshed, carrying beautiful memories meticulously designed for you by TRAGUIN."
                ),
                [
                    'Transfers Included: Private luxury door-to-door departure drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Fortune Miramar / Vivanta Panaji / similar',
                'Heritage & Central Goa (4 Nights)',
                '04 Nights',
                'Deluxe',
                'Superior Pool View Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Fortune Miramar / Vivanta Panaji / similar (Heritage & Central Goa (4 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Cidade de Goa - IHCL SeleQtions / similar',
                'Heritage & Central Goa (4 Nights)',
                '04 Nights',
                'Premium',
                'Premium Sea View Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Cidade de Goa - IHCL SeleQtions / similar (Heritage & Central Goa (4 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Taj Resort & Convention Centre Goa / similar',
                'Heritage & Central Goa (4 Nights)',
                '04 Nights',
                'Luxury',
                'Luxury Heritage Balcony Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Taj Resort & Convention Centre Goa / similar (Heritage & Central Goa (4 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Leela Goa / Taj Exotica Resort & Spa',
                'Heritage & Central Goa (4 Nights)',
                '04 Nights',
                'Ultra Luxury',
                'VVIP Private Royal Lagoon Villa',
                'Bespoke Personalized Dining Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Leela Goa / Taj Exotica Resort & Spa (Heritage & Central Goa (4 Nights)) | Bespoke Personalized Dining Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Airfare, flight tickets, or main rail transportation', 1),
            _inc_excluded('to Goa.', 2),
            _inc_excluded('Personal expenses such as laundry, phone calls,', 3),
            _inc_excluded('or tips.', 4),
            _inc_excluded('Specialized temple ritual pooja ticketing fees.', 5),
            _inc_excluded('Any water sports, beach activities, or nightlife', 6),
            _inc_excluded('excursions.', 7),
        ],
    )
    return package, itinerary

def build_ga_016(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-016'
    tour_code = 'TRG-GOA-016'
    title = 'TRAGUIN Premium Goa Tour Package — Water Sports & Scuba Adventure'
    duration = '08 Nights / 09 Days'
    slug = 'ga-016-water-sports-scuba-adventure'
    itin_slug = 'ga-016-water-sports-scuba-adventure-itinerary'
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
            _ph('Serial code GA-016 | TRAGUIN tour code TRG-GOA-016', 1),
            _ph('State / Country: Goa / India | Category: Adventure, Water', 2),
            _ph('Destinations: North Goa (Calangute, Baga) •', 3),
            _ph('Ideal for: Adventure Enthusiasts, High- end FITs, Couples & Active Families', 4),
            _ph('Best season: October to April (Perfect for Water Sports & Scuba Diving)', 5),
            _ph('Starting price: On Request (Premium Customized Tour)', 6),
            _ph('Vehicle / Meals: Private Luxury', 7),
            _ph('TRAGUIN Signature Experience: Private, beachside barbecue lunch prepared by a personal chef at', 8),
            _ph('Curated by TRAGUIN Experts: Custom-tailored activity tracking that balances high-octane water sports', 9),
            _ph("Premium Handpicked Hotels: Accommodations chosen strictly for their safety standards, couples'", 10),
            _ph('Luxury Transportation: Expert drivers ensuring premium comfort across both North and South Goa', 11),
            _ph('Local Markets & Souvenirs: Explore the Anjuna Wednesday Flea Market or the Arpora Saturday Night Market to discover unique hand-made beachwear, premium local cashews, feni liquor bottles, and exquisite terracotta artifacts. Cafes & Food: Old Goa and Panaji boast charming Latin Quarter cafes offering authentic Goan-Portuguese fusion dishes, traditional Bebinca desserts, and artisanal coffees.', 12),
            _ph('Scuba Diving Rules: All diving is subject to weather conditions and visibility. A basic medical declaration', 13)
        ],
        moods=['Family', 'Beach', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customized Tour)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Water Sports & Scuba Adventure',
        overview='LUXURY THRILL Welcome to an extraordinary high-adrenaline escape designed and managed exclusively by TRAGUIN. Embark on the most thrilling Goa Adventure Itinerary, curated perfectly to combine the high-octane excitement of professional deep-sea scuba diving with the sheer elegance of premium stays. As your elite travel consultants, TRAGUIN presents a unique blueprint that reveals the breathtaking landscapes of sun- kissed coastlines, roaring jungle waterfalls, and vibrant marine life. Indulge in handpicked hotels, dynamic private charters, and immersive experiences that transform your tropical getaway into a series of unforgettable memories.\n\nTOUR OVERVIEW\nThis bespoke luxury holiday package is engineered precisely for action-driven travelers who refuse to compromise on top-tier opulence. Travelling in a completely private premium AC luxury vehicle with an expert, highly trained local driver, your route explores both the lively beaches of the North and the untouched, serene lagoons of South Goa. Enjoy an exceptional meal plan featuring magnificent daily breakfasts, beachside barbecues, and private chef-curated dinners. Every aspect of this trip bears the hallmark of a TRAGUIN curated experience note, providing seamless private boat charters, professional PADI dive-master guidance, and 24/7 dedicated support.\n\nWHY CHOOSE THE BEST GOA TOUR PACKAGE?\nWhen organizing a Luxury Goa Holiday, modern travelers look for a masterfully balanced itinerary that fuses action with premium relaxation. Goa stands out as India’s ultimate coastal paradise, making a premium Goa Honeymoon Package or an action-packed Goa Family Tour the top recommendation for an exceptional winter holiday. From the iconic attractions of historic Portuguese cathedrals to the thrill of scuba diving near exotic shipwrecks, Goa sightseeing offers infinite visual rewards. Our comprehensive TRAGUIN Goa Packages position you directly at popular Instagram locations like the majestic Dudhsagar Waterfalls, the vibrant beach clubs of Vagator, and the hidden sandbars of Palolem. Dive into local spice plantation markets, sample legendary Konkani fusion seafood, or enjoy a sunset cruise along the Mandovi River. Rely on our tailored solutions to experience the absolute best time to visit Goa with personalized attention and unmatched premium comfort.',
        seo_title='GA-016 | Goa | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days Goa package (GA-016 / TRG-GOA-016): North Goa (Calangute, Baga) •.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA – CHIC NORTH GOA CHECK-IN', 1),
            _ih('Day 02: NORTH GOA WATER SPORTS EXTRAVAGANZA', 2),
            _ih('Day 03: EXCLUSIVE GRAND ISLAND SCUBA DIVING EXCURSION', 3),
            _ih('Day 04: THE EPIC DUDHSAGAR WATERFALLS SAFARI', 4),
            _ih('Day 05: CULTURAL HERITAGE & PRIVATE LUXURY RIVER YACHT', 5),
            _ih('Day 06: TRANSFER TO UNTOUCHED SOUTH GOA (PALOLEM)', 6),
            _ih('Day 07: COLOURED CANYONS & NETRAVALI BUBBLING LAKE TOUR', 7),
            _ih('Day 08: SEA KAYAKING & PRIVATE ISLAND PICNIC', 8),
            _ih('Day 09: LEISURELY CHECKOUT & DEPARTURE', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA – CHIC NORTH GOA CHECK-IN',
                (
                    "WELCOME TO INDIA’S COASTAL PARADISE – LUXURY & LEISURE Your premium Goa experience begins as you touch down at Mopa (GGIA) or Dabolim Airport. A private luxury SUV awaits to transport you smoothly to your handpicked premium luxury resort in North Goa. Receive an elite welcome amenity kit upon check-in. Spend your afternoon unwinding inside your private villa or exploring the resort's premium amenities. In the evening, take a leisurely stroll down Calangute beach, taking in a spectacular Arabian Sea sunset. TRAGUIN experts."
                ),
                [
                    'Sightseeing Included: Calangute coastline walk, resort private beach access.',
                    'Evening Experience: An intimate beachside welcome dinner featuring local artisan cocktails curated by',
                    'Overnight Stay: North Goa (Premium / Luxury Beachfront Resort)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),            _day(
                2,
                'NORTH GOA WATER SPORTS EXTRAVAGANZA',
                (
                    'HIGH-SPEED WATER ADVENTURES ON THE ARABIAN SEA Awake early for a lavish breakfast before heading to Baga Beach for a thrilling, high-octane water sports session. Enjoy private, priority access to high-speed jet skiing, parasailing with panoramic coastal views, bumper boat rides, and exhilarating banana boat tours. All activities are guided by certified instructors using top-tier safety gear. Spend your afternoon dining at a premium cliffside café overlooking Anjuna.'
                ),
                [
                    'Sightseeing Included: Baga Beach, Anjuna Cliff viewpoints, Chapora Fort photography spots.',
                    'Optional Activities: Private luxury speed-boat rental for a custom 2-hour dolphin spotting cruise.',
                    'Overnight Stay: North Goa (Premium / Luxury Beachfront Resort)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),            _day(
                3,
                'EXCLUSIVE GRAND ISLAND SCUBA DIVING EXCURSION',
                (
                    'DEEP-SEA EXPLORATION & VIBRANT MARINE REEF LIFE Today delivers an iconic highlight of your adventure. Board a private speed boat charter from Sinquerim jetty heading toward Grand Island. Accompanied by PADI-certified dive masters, enjoy an exclusive underwater scuba diving session. Swim alongside brilliant coral reefs, schools of tropical fish, and fascinating marine topography. Afterwards, enjoy a live seafood barbecue lunch served right on a secluded beach. center.'
                ),
                [
                    'Sightseeing Included: Grand Island marine zone, Monkey Beach, Aguada lighthouse coast.',
                    "Evening Experience: A relaxing post-dive therapeutic couples spa session at the resort's premium wellness",
                    'Overnight Stay: North Goa (Premium / Luxury Beachfront Resort)',
                    'Meals Included: Breakfast, Island Barbecue Lunch & Premium Resort Dinner',
                ],
            ),            _day(
                4,
                'THE EPIC DUDHSAGAR WATERFALLS SAFARI',
                (
                    'ROARING JUNGLE CASCADES & UNTOUCHED FOREST JEEP TRAILS Journey deep into the lush Western Ghats for a private 4x4 open-jeep jungle safari through the Bhagwan Mahavir Wildlife Sanctuary. Arrive at the base of the spectacular Dudhsagar Waterfalls, a towering four-tiered cascade that creates a breathtaking landscape. Swim in the refreshing, natural mountain pools under the watchful eyes of certified lifeguards. Conclude your afternoon with an educational heritage tour and traditional buffet at a premium spice plantation.'
                ),
                [
                    'Sightseeing Included: Dudhsagar Waterfalls, Tropical Spice Plantation, Wildlife Sanctuary Jeep Track.',
                    'Evening Experience: A candlelit dinner featuring organic, farm-to-table culinary creations.',
                    'Overnight Stay: North Goa Heritage Mansion Resort',
                    'Meals Included: Breakfast, Traditional Plantation Lunch & Dinner',
                ],
            ),            _day(
                5,
                'CULTURAL HERITAGE & PRIVATE LUXURY RIVER YACHT',
                (
                    "PORTUGUESE SPLENDOUR, OLD GOA & SUNSET SAILING Spend a magnificent morning exploring the timeless architectural wonder of Old Goa. Take a private, guided walking tour through the majestic Basilica of Bom Jesus and the grand Se Cathedral. In the late afternoon, step aboard an exclusive, private luxury yacht on the Mandovi River. Sip premium champagne and enjoy custom hors d'oeuvres while watching the sun drop below the ocean horizon."
                ),
                [
                    'Sightseeing Included: Basilica of Bom Jesus, Fontainhas Latin Quarter, Mandovi River waterways.',
                    "Optional Activities: High-stakes fine dining experience at Goa's premium luxury offshore casino clubs.",
                    'Overnight Stay: Panaji / Central Goa Luxury Hotel',
                    'Meals Included: Breakfast & Yacht Champagne Dinner',
                ],
            ),            _day(
                6,
                'TRANSFER TO UNTOUCHED SOUTH GOA (PALOLEM)',
                (
                    'TRANSITION TO TRANQUILITY – COCONUT GROVES & HIDDEN LAGOONS Bid farewell to the bustling center as your luxury SUV drives you south towards the pristine, postcard-perfect beaches of Palolem and Agonda. Check into an ultra-luxury eco-resort nestled directly into private coconut groves. Spend your afternoon kayaking through secret mangrove forests or relaxing on the fine, powdery golden sand. The atmosphere here is ideal for romantic photography points.'
                ),
                [
                    'Sightseeing Included: Palolem Beach, Agonda turtle nesting coastline, Cabo de Rama Fort sunset.',
                    'Evening Experience: A private bonfire experience on the beach under a canopy of stars.',
                    'Overnight Stay: South Goa (Palolem Luxury Beachfront Villa)',
                    'Meals Included: Breakfast & Fresh Catch Seafood Dinner',
                ],
            ),            _day(
                7,
                'COLOURED CANYONS & NETRAVALI BUBBLING LAKE TOUR',
                (
                    "HIDDEN NATURAL WONDERS & SECRET OFF-ROAD EXPLORATIONS Discover South Goa's best-kept secrets with an off-road jeep excursion to the mysterious Netravali region. Visit the ancient Gopinath Bubbling Lake, a mystical heritage pond where continuous underwater bubbles respond to rhythmic hand claps. Hike along hidden jungle paths to find pristine freshwater pools, perfect for a private midday swim far away from tourist crowds."
                ),
                [
                    'Sightseeing Included: Netravali Bubbling Lake, Savari Waterfall trail, spice orchards.',
                    'Optional Activities: Guided bird watching and botanical photography session with a resident naturalist.',
                    'Overnight Stay: South Goa (Palolem Luxury Beachfront Villa)',
                    'Meals Included: Breakfast & Traditional Goan Portuguese Dinner',
                ],
            ),            _day(
                8,
                'SEA KAYAKING & PRIVATE ISLAND PICNIC',
                (
                    "IMMERSIVE EXPERIENCES ON LONELY SANDBARS Embark on a guided sea-kayaking expedition toward Butterfly Island, a pristine, hidden cove accessible only by water. Enjoy a curated gourmet picnic lunch prepared entirely by your resort's private culinary team, served right on the beach. Spend your final afternoon swimming in crystal clear turquoise waters and capturing beautiful coastal images."
                ),
                [
                    'Sightseeing Included: Butterfly Beach, Honeymoon Lagoon sandbars, Palolem bay.',
                    'Evening Experience: A grand farewell barbecue dinner paired with premium wines directly on the beach.',
                    'Overnight Stay: South Goa (Palolem Luxury Beachfront Villa)',
                    'Meals Included: Breakfast, Gourmet Picnic Lunch & Grand Farewell Dinner',
                ],
            ),            _day(
                9,
                'LEISURELY CHECKOUT & DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Indulge in a final morning breakfast surrounded by swaying palms and ocean breezes. Pack your gear and board your private luxury SUV as your chauffeur guides you back to Mopa or Dabolim Airport for your return flight. Head home carrying a heart filled with high-adrenaline thrills and unforgettable memories designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door airport transfer drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Goa Resort & Spa | Welcomheritage Panjim Inn | The Lalit Golf & Beach Resort',
                'North Goa (4 Nights) / Panaji Heritage (1 Night) / South Goa (3 Nights)',
                '08 Nights',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Novotel Goa Resort & Spa (North Goa (4 Nights)) | Welcomheritage Panjim Inn (Panaji Heritage (1 Night)) | The Lalit Golf & Beach Resort (South Goa (3 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'W Goa (Wonderful Room) | Cidade de Goa IHCL SeleQtions | Alila Diwa Goa (Heritage Room)',
                'North Goa (4 Nights) / Panaji Heritage (1 Night) / South Goa (3 Nights)',
                '08 Nights',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: W Goa (Wonderful Room) (North Goa (4 Nights)) | Cidade de Goa IHCL SeleQtions (Panaji Heritage (1 Night)) | Alila Diwa Goa (Heritage Room) (South Goa (3 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Taj Holiday Village / Taj Fort Aguada | The Postcard Hideaway Netravali | The Leela Goa (Lagoon Suite)',
                'North Goa (4 Nights) / Panaji Heritage (1 Night) / South Goa (3 Nights)',
                '08 Nights',
                'Luxury',
                'Luxury Suite',
                'MAPAI + Premium Amenities',
                5,
                3,
                description='OPTION 03 – LUXURY: Taj Holiday Village / Taj Fort Aguada (North Goa (4 Nights)) | The Postcard Hideaway Netravali (Panaji Heritage (1 Night)) | The Leela Goa (Lagoon Suite) (South Goa (3 Nights)) | MAPAI + Premium Amenities',
            ),
            _hotel(
                'Taj Exotica Resort (Plunge Pool Villa) | The Postcard Moira (Royal Suite) | The Leela Goa (Royal Villa)',
                'North Goa (4 Nights) / Panaji Heritage (1 Night) / South Goa (3 Nights)',
                '08 Nights',
                'Ultra Luxury',
                'Royal Villa',
                'Bespoke Gourmet Custom Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Taj Exotica Resort (Plunge Pool Villa) (North Goa (4 Nights)) | The Postcard Moira (Royal Suite) (Panaji Heritage (1 Night)) | The Leela Goa (Royal Villa) (South Goa (3 Nights)) | Bespoke Gourmet Custom Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Mainline domestic or international flight tickets.', 1),
            _inc_excluded('Personal expenses such as laundry, phone calls,', 2),
            _inc_excluded('tips, and mini-bar charges.', 3),
            _inc_excluded('Monument entry tickets, camera fees, or', 4),
            _inc_excluded('additional unlisted local guides.', 5),
            _inc_excluded('Optional specialized PADI open-water certification', 6),
            _inc_excluded('courses.', 7),
        ],
    )
    return package, itinerary

def build_ga_017(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-017'
    tour_code = 'TRG-GOA-017'
    title = 'TRAGUIN Premium Goa Tour Package — Dudhsagar Trek & Backwater Safari'
    duration = '07 Nights / 08 Days'
    slug = 'ga-017-dudhsagar-trek-backwater-safari'
    itin_slug = 'ga-017-dudhsagar-trek-backwater-safari-itinerary'
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
            _ph('Serial code GA-017 | TRAGUIN tour code TRG-GOA-017', 1),
            _ph('State / Country: Goa / India | Category: Bespoke Adventure & Eco-Luxury', 2),
            _ph('Destinations: North Goa Beaches • Mollem National', 3),
            _ph('Ideal for: Adventure Enthusiasts, Nature Lovers & Luxury Explorers', 4),
            _ph('Best season: October to May (Trekking & Safaris) / June to September (Monsoon Magic)', 5),
            _ph('Starting price: On Request (Premium Customised Expedition)', 6),
            _ph('Vehicle / Meals: Private Luxury', 7),
            _ph('TRAGUIN Signature Experience: Private riverbanks picnic setup with premium organic mocktails during', 8),
            _ph('Curated by TRAGUIN Experts: Expertly routed transfers that bypass traffic to maximize your relaxation', 9),
            _ph('Premium Handpicked Hotels: Accommodations selected for their high safety records, impeccable', 10),
            _ph('Luxury Transportation: Expert drivers with extensive knowledge of local terrains and the best scenic', 11),
            _ph('Local Markets & Souvenirs: Visit the famous Anjuna Wednesday Market or the Saturday Night Market to browse authentic terracotta pottery, hand-crafted coconut shell artifacts, and famous local cashew nuts. Cafes & Food: Old Panaji features cozy, atmospheric cafes offering authentic Indo-Portuguese snacks, fresh local poi bread, and world-class wood-fired seafood delicacies accompanied by live music.', 12),
            _ph('Weather Notes: Summer months require light cotton clothing, while monsoon treks require sturdy, high-', 13)
        ],
        moods=['Family', 'Beach', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customised Expedition)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Dudhsagar Trek & Backwater Safari',
        overview='ADVENTURE ESCAPE Welcome to a thrilling and sophisticated eco-expedition curated exclusively by TRAGUIN. Embark on the ultimate Goa Adventure Package, meticulously engineered to uncover the untamed wilderness, roaring waterfalls, and serene emerald waterways beyond the coast. As your premier travel consultants, TRAGUIN transforms the traditional beach holiday into a seamless luxury holiday filled with premium stays, high- octane explorations, and deep nature immersions. From the majestic heights of the Dudhsagar Trek to the hidden secrets of a Backwater Safari, let us create unforgettable memories for your soul.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers an exquisite balance between legendary coastal relaxation and deep inland exploration. Travelling in a dedicated private premium SUV with professional chauffeur assistance, you will explore Goa in absolute comfort and luxury. Featuring a carefully curated meal plan with expansive breakfasts and specialized culinary dinners, this route represents the definitive premium Goa experience. Every detail of this itinerary includes the signature touch of TRAGUIN curated experiences, ensuring private naturalists, VIP safety permits, and around-the-clock tailored support.\n\nWHY CHOOSE THE BEST GOA TOUR PACKAGE?\nWhen considering a Luxury Goa Holiday, discerning travellers seek experiences that break away from standard itineraries. Goa holds deep, untouched natural secrets. The legendary Dudhsagar Waterfalls and the tranquil Mandovi River backwaters stand out as some of the most searched experiences and iconic attractions in Western India, making a customized Goa Honeymoon Package or Goa Family Tour incredibly unique. For travelers seeking thrill and scenery, the region boasts highly popular Instagram locations like the historic Cabo de Rama cape, the spice plantations of Ponda, and the dense bird sanctuaries of Chorao Island. Whether you are looking for local market shopping, indulging in authentic Indo-Portuguese fusion cuisine, or seeking thrills on a backwater safari, our signature TRAGUIN Goa Packages ensure handpicked hotels, elite comfort, and curated exclusive experiences during the best time to visit Goa.',
        seo_title='GA-017 | Goa | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Goa package (GA-017 / TRG-GOA-017): North Goa Beaches • Mollem National.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA – NORTH COAST', 1),
            _ih('Day 02: HINTERLAND EXPEDITION & CHORAO ISLAND KAYAKING', 2),
            _ih('Day 03: THE EPIC DUDHSAGAR TREK', 3),
            _ih('Day 04: SPICE PLANTATION CANOPY WALK & HERITAGE VILLAGES', 4),
            _ih('Day 05: SOUTH GOA WILDLIFE & BACKWATER SAFARI', 5),
            _ih('Day 06: CLIFFTREK TO CABO DE RAMA FORT', 6),
            _ih('Day 07: ECO-LUXURY RESORT LEISURE & SPA RESORT DAY', 7),
            _ih('Day 08: DEPARTURE FROM GOA', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA – NORTH COAST',
                (
                    'WELCOME TO THE SUN-KISSED COASTLINE & PREMIUM LUXURY Your premium Goa experience begins as you step off your flight or train. A private luxury SUV waits to escort you to your handpicked premium resort in North Goa. Enjoy a refreshing welcome drink while checking in. Spend a relaxed afternoon adjusting to the tropical rhythm before heading down to a secluded beach enclave for your first sunset view over the Arabian Sea—a prime photography point to start your trip.'
                ),
                [
                    'Sightseeing Included: Coastal drive, Secluded North Goa beach walk.',
                    'Evening Experience: Beachside gourmet welcome dinner curated by TRAGUIN experts.',
                    'Overnight Stay: North Goa (Premium Beachfront Resort)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),            _day(
                2,
                'HINTERLAND EXPEDITION & CHORAO ISLAND KAYAKING',
                (
                    'MANDOVI BACKWATER SAFARI & ECO-SYSTEM IMMERSION Awake early for a spectacular morning drive toward the river banks. Board a private boat for an exclusive backwater safari along the Mandovi River. Navigate through dense mangrove forests to Chorao Island, a sanctuary teeming with rare migratory birds. Swap your boat for a premium guided kayaking experience to glide quietly through the narrow, serene mudflats and natural channels.'
                ),
                [
                    'Sightseeing Included: Mandovi River backwaters, Salim Ali Bird Sanctuary borders, Chorao Island.',
                    'Optional Activities: Premium drone photography session during the kayak trail.',
                    'Overnight Stay: North Goa (Premium Beachfront Resort)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),            _day(
                3,
                'THE EPIC DUDHSAGAR TREK',
                (
                    'ROARING WATERFALLS, DEEP JUNGLES & TREK EXPEDITION Today marks the apex of your adventure tour. Travel inland to Mollem National Park, where you will switch to an open-top 4x4 jungle jeep. Venture deep through rugged streams and dense teak forests before initiating the guided trek to the base of Dudhsagar Waterfalls. Witness the awe-inspiring sight of white water cascading down four tiers from a height of over 300 meters. Cool off with a refreshing dip in the natural pool at the base of the falls.'
                ),
                [
                    'Sightseeing Included: Mollem National Park, Dudhsagar Waterfall Trek, Bhagwan Mahavir Wildlife Sanctuary.',
                    'Evening Experience: Private bonfire and dynamic tribal storytelling at a boutique jungle lodge.',
                    'Overnight Stay: Mollem / Ponda (Boutique Eco-Luxury Jungle Resort)',
                    'Meals Included: Breakfast & Traditional Goan Spice Plantation Lunch & Dinner',
                ],
            ),            _day(
                4,
                'SPICE PLANTATION CANOPY WALK & HERITAGE VILLAGES',
                (
                    'ORGANIC TRAILS, ZIP-LINING & PORTUGUESE ARCHITECTURE Enjoy a freshly brewed organic breakfast before embarking on an exclusive tour of a heritage spice plantation. Walk beneath a lush canopy of pepper vines, vanilla orchids, and nutmeg trees. Thrill seekers can opt for a high-altitude zip-lining experience across the forest valley. Later in the afternoon, drive through Fontainhas, the historic Latin Quarter of Panaji, a highly popular Instagram location known for its brightly colored houses.'
                ),
                [
                    'Sightseeing Included: Ponda Spice Farm, Fontainhas Latin Quarter, Panaji Church.',
                    'Evening Experience: Premium sunset cruise along the Arabian Sea coast with live music.',
                    'Overnight Stay: South Goa (Ultra-Luxury Beach Resort)',
                    'Meals Included: Breakfast & Authentic Buffet Dinner',
                ],
            ),            _day(
                5,
                'SOUTH GOA WILDLIFE & BACKWATER SAFARI',
                (
                    'CUMBARJUA CANAL CROCODILE SAFARI & SECLUDED RIVERS Savor a beautiful beachside breakfast and head out for a thrilling backwater safari along the Cumbarjua Canal. This brackish waterway is famous for spotting Mugger crocodiles in their natural mangrove habitat. Accompanied by an expert naturalist, enjoy excellent wildlife photography opportunities as you cruise safely down the canal.'
                ),
                [
                    'Sightseeing Included: Cumbarjua Canal Mangroves, Crocodile Spotting, Mangrove Boardwalk.',
                    'Optional Activities: Traditional line fishing experience aboard the luxury pontoon boat.',
                    'Overnight Stay: South Goa (Ultra-Luxury Beach Resort)',
                    'Meals Included: Breakfast & Exquisite Seafood Specialty Dinner',
                ],
            ),            _day(
                6,
                'CLIFFTREK TO CABO DE RAMA FORT',
                (
                    'OCEAN VISIONS, CANYON VIEWS & ROMANTIC RUINS Embark on a magnificent cliffside trek toward the ancient ruins of Cabo de Rama Fort in South Goa. The trek leads you along pristine clifftops overlooking panoramic ocean vistas and breathtaking landscapes. Explore the historic stone battlements where legendary myths meet colonial history. Conclude your trek at a hidden beach cove accessible only by foot.'
                ),
                [
                    'Sightseeing Included: Cabo de Rama Fort ruins, Hidden Beach Cove, South Goa coastal trails.',
                    'Evening Experience: Sunset champagne toast on the clifftops overlooking the open sea.',
                    'Overnight Stay: South Goa (Ultra-Luxury Beach Resort)',
                    'Meals Included: Breakfast & Coastal Barbecue Dinner',
                ],
            ),            _day(
                7,
                'ECO-LUXURY RESORT LEISURE & SPA RESORT DAY',
                (
                    "RELAXATION, REJUVENATION & REFLECTION Dedicate this day entirely to premium relaxation. Enjoy the extensive amenities of your ultra-luxury South Goa resort. Indulge in an exclusive Ayurvedic or Balinese couple's massage, lounge by the infinity pool, or take a sunset walk along the pristine sands of Varca or Palolem beach. Reflect on your incredible adventure tour in pure bliss."
                ),
                [
                    'Sightseeing Included: Varca/Cavelossim beach access, Resort private gardens.',
                    'Optional Activities: Private luxury yacht rental for a deep-sea dolphin cruise.',
                    'Overnight Stay: South Goa (Ultra-Luxury Beach Resort)',
                    'Meals Included: Breakfast & Farewell Premium Gala Dinner',
                ],
            ),            _day(
                8,
                'DEPARTURE FROM GOA',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Enjoy a final lavish breakfast overlooking the ocean waves. Your private luxury transport will safely drive you to Mopa Airport, Dabolim Airport, or Madgaon Railway Station. Return home carrying a heart filled with spirit, deep bonds, and unforgettable memories designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door airport/station drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Resort & Spa / similar | Dudhsagar Spa Resort / similar | Caravela Beach Resort / similar',
                'North Goa (2 Nights) / Mollem-Ponda (1 Night) / South Goa (4 Nights)',
                '07 Nights',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Novotel Resort & Spa / similar (North Goa (2 Nights)) | Dudhsagar Spa Resort / similar (Mollem-Ponda (1 Night)) | Caravela Beach Resort / similar (South Goa (4 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                "Hard Rock Hotel / Vivanta Vagator | Nature's Nest Eco Lodge | Radisson Blu Resort South Goa",
                'North Goa (2 Nights) / Mollem-Ponda (1 Night) / South Goa (4 Nights)',
                '07 Nights',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description="OPTION 02 – PREMIUM: Hard Rock Hotel / Vivanta Vagator (North Goa (2 Nights)) | Nature's Nest Eco Lodge (Mollem-Ponda (1 Night)) | Radisson Blu Resort South Goa (South Goa (4 Nights)) | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                'W Goa / Taj Holiday Village | Stone Water Eco Resort Stay | The Leela Goa / Taj Exotica Goa',
                'North Goa (2 Nights) / Mollem-Ponda (1 Night) / South Goa (4 Nights)',
                '07 Nights',
                'Luxury',
                'Luxury Suite',
                'MAPAI + Premium Amenities',
                5,
                3,
                description='OPTION 03 – LUXURY: W Goa / Taj Holiday Village (North Goa (2 Nights)) | Stone Water Eco Resort Stay (Mollem-Ponda (1 Night)) | The Leela Goa / Taj Exotica Goa (South Goa (4 Nights)) | MAPAI + Premium Amenities',
            ),
            _hotel(
                'The St. Regis Goa Resort (Suite) | Bespoke Wild Eco Luxury Villa | The St. Regis Goa Resort (Pool Villa)',
                'North Goa (2 Nights) / Mollem-Ponda (1 Night) / South Goa (4 Nights)',
                '07 Nights',
                'Ultra Luxury',
                'Pool Villa',
                'Bespoke Signature VIP Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The St. Regis Goa Resort (Suite) (North Goa (2 Nights)) | Bespoke Wild Eco Luxury Villa (Mollem-Ponda (1 Night)) | The St. Regis Goa Resort (Pool Villa) (South Goa (4 Nights)) | Bespoke Signature VIP Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Airfare, flight tickets, or train tickets to Goa.', 1),
            _inc_excluded('Optional activities (Zip-lining, premium drone', 2),
            _inc_excluded('rentals).', 3),
            _inc_excluded('Personal expenses such as laundry, phone', 4),
            _inc_excluded('calls, or tips.', 5),
            _inc_excluded('Any monument camera permits or alcoholic', 6),
            _inc_excluded('beverage charges.', 7),
        ],
    )
    return package, itinerary

def build_ga_018(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-018'
    tour_code = 'TRG-GOA-018'
    title = 'TRAGUIN Premium Goa Tour Package — Taj & Heritage Luxury Retreat'
    duration = '06 Nights / 07 Days'
    slug = 'ga-018-taj-heritage-luxury-retreat'
    itin_slug = 'ga-018-taj-heritage-luxury-retreat-itinerary'
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
            _ph('Serial code GA-018 | TRAGUIN tour code TRG-GOA-018', 1),
            _ph('State / Country: Goa / India | Category: Luxury', 2),
            _ph('Destinations: Sinquerim •', 3),
            _ph('Ideal for: Discerning Travelers, Luxury Jetsetters & Connoisseurs', 4),
            _ph('Best season: October to April (Vibrant Resort Season)', 5),
            _ph('Starting price: On Request (Ultra Customized Luxury Tier)', 6),
            _ph('Vehicle / Meals: Private Chauffeur', 7),
            _ph('TRAGUIN Signature Experience: Private sunset charter yacht cruise with customized appetizers and', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked heritage trail itinerary to ensure seamless, comfortable travel', 9),
            _ph('Premium Handpicked Hotels: Accommodations selected for their high safety standards, beautiful ocean', 10),
            _ph("Exclusive Recommendations: Access and preferred table seating at some of Goa's top beach lounges", 11),
            _ph("Local Markets & Souvenirs: Find exquisite, handcrafted blue azulejos ceramic tiles, authentic local feni infusions, organic cashews, and high-end resort wear at luxury boutiques in Panjim and Assagao. Cafes & Food: Indulge your palate in rich traditional Bebinca desserts, fiery prawn balchão, and artisan coffees across Fontainhas' charming courtyard cafes.", 12),
            _ph('Booking Policy: We advise booking your package 45–60 days ahead during peak season (October to', 13)
        ],
        moods=['Luxury', 'Romantic', 'Family', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Ultra Customized Luxury Tier)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Taj & Heritage Luxury Retreat',
        overview='REDEFINED Welcome to an unforgettable journey curated exclusively by TRAGUIN. Embark on the finest Goa Honeymoon Package and high-end Goa Family Tour ever crafted to highlight the classic architectural soul, golden coasts, and hidden vintage splendor of this tropical paradise. As your dedicated premium travel consultants, TRAGUIN elevates your beach holiday into a seamless luxury holiday filled with premium stays at iconic Taj grand properties, handpicked hotels, and immersive experiences that linger beautifully. From the majestic historic battlements of Fort Aguada to the pastel-washed Latin corridors of Fontainhas, every element is designed to curate unforgettable memories.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers an exquisite balance between legendary Indian Ocean hospitality and deep Indo-Portuguese architectural exploration. Travelling in a dedicated private premium vehicle with professional, background-verified chauffeur assistance, your family or partner will enjoy unparalleled comfort and absolute privacy. With a carefully structured plan including lavish breakfasts at world-renowned culinary kitchens and customized private tours, this route represents the definitive premium Goa experience. Every moment includes the signature touch of TRAGUIN curated experiences, ensuring private yacht permissions, exclusive heritage estate entries, and around-the-clock personal assistance.\n\nWHY CHOOSE THE BEST GOA TOUR PACKAGE?\nWhen seeking a true Luxury Goa Holiday, sophisticated travelers require more than generic coastlines; they seek private spaces, historic depth, and top-tier hospitality. Goa stands out as an iconic fusion of cultures. From the classic beaches to the peaceful backwaters of the Mandovi River, Goa sightseeing reveals a world of elite discovery. Key icons like the UNESCO World Heritage Basilica of Bom Jesus, the dramatic layout of Reis Magos Fort, and the hidden lanes of Divar Island form the best tourist places in Goa. For discerning couples or family groups reserving a bespoke Goa Honeymoon Package or a Goa Family Tour, the coastal state unveils incredible, highly popular Instagram locations such as the bright yellow-and- blue avenues of Fontainhas, private sand stretches, and ancient spice plantations. Whether you desire local high-fashion designer shopping, private yacht experiences, or heritage luxury, our customized TRAGUIN Goa Packages promise premium stays and exclusive experiences that capture the absolute best time to visit Goa.',
        seo_title='GA-018 | Goa | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Goa package (GA-018 / TRG-GOA-018): Sinquerim •.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA – WELCOME TO THE TAJ OPULENCE', 1),
            _ih('Day 02: NORTH GOA COASTAL RECONNAISSANCE', 2),
            _ih('Day 03: VINTAGE PANJIM & THE LATIN QUARTER LATITUDE', 3),
            _ih('Day 04: UNVEILING OLD GOA & PRIVATE YACHT LUXURY', 4),
            _ih('Day 05: SOUTHERN HERITAGE MANORS & UNTOUCHED SHORES', 5),
            _ih('Day 06: DIVAR ISLAND STEP-BACK IN TIME', 6),
            _ih('Day 07: DEPARTURE FROM PARADISE', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA – WELCOME TO THE TAJ OPULENCE',
                (
                    'ARRIVAL EXPERIENCE • PRIVATE LUXURY ESCORT • SUNSET BY THE FORT Your premium Goa experience begins at Manohar International Airport (MOPA) or Dabolim Airport, where a private luxury transport vehicle waits to receive you with customized dynamic hospitality. Drive smoothly to your ultra-luxury handpicked hotel, the legendary Taj Holiday Village Resort & Spa or Taj Fort Aguada. After a refreshing check-in, relax inside your private Portuguese-style villa. As the afternoon shadows stretch, walk down to the pristine beachfront overlooking the 16th-century Aguada fortress.'
                ),
                [
                    'Sightseeing Included: Fort Aguada outer ramparts, private beachfront exploration.',
                    'Evening Experience: Bespoke seaside sunset cocktail or mocktail sequence curated by TRAGUIN experts.',
                    'Overnight Stay: North Goa Beachfront (Taj Luxury Property)',
                    'Meals Included: Welcome Amenities & Luxury Welcome Dinner Array',
                ],
            ),            _day(
                2,
                'NORTH GOA COASTAL RECONNAISSANCE',
                (
                    "ICONIC ATTRACTIONS • SCENIC BEAUTY • PREMIUM BEACH CLUBS Savor a lavish gourmet breakfast at the resort's open-air deck. Today, experience the dramatic scenic beauty of North Goa. Your private luxury vehicle will escort you to the historic Reis Magos Fort, showcasing spectacular panoramic photography points across the mouth of the Mandovi River. Later, proceed to the quieter, premium stretches of Ashwem and Morjim beaches. Enjoy an immersive afternoon at a luxury beach lounge with curated dining spaces."
                ),
                [
                    'Sightseeing Included: Reis Magos Fort, Vagator Cliffs, Premium Ashwem Beachfront.',
                    'Optional Activities: Private speed-boat excursion along the northern dolphin-spotting paths.',
                    'Overnight Stay: North Goa Beachfront (Taj Luxury Property)',
                    'Meals Included: Premium Breakfast Array',
                ],
            ),            _day(
                3,
                'VINTAGE PANJIM & THE LATIN QUARTER LATITUDE',
                (
                    'FONTAINHAS VINTAGE TOUR • POPULAR INSTAGRAM LOCATIONS • INDO- PORTUGUESE SOUL Delve deep into the cultural core of Goa with a dedicated heritage excursion. Journey to Fontainhas, the oldest surviving Latin Quarter in Asia. Wander on a private walking tour with an expert historian through narrow streets lined with 18th-century pastel-hued mansions. This is a highly popular Instagram location perfect for romantic or family photography. Visit the iconic Panjim Church (Our Lady of the Immaculate Conception) before exploring luxury lifestyle boutiques and designer galleries. restaurant.'
                ),
                [
                    "Sightseeing Included: Fontainhas Latin Quarter, Altinho Hill, Panjim Church, Bishop's Palace plaza.",
                    'Evening Experience: Exclusive high-end Goan-Portuguese fusion dining at an artisanal heritage home',
                    'Overnight Stay: Panjim / North Goa Heritage Resort Hub',
                    'Meals Included: Premium Breakfast & Handpicked Fine-Dining Dinner',
                ],
            ),            _day(
                4,
                'UNVEILING OLD GOA & PRIVATE YACHT LUXURY',
                (
                    'UNESCO MAJESTY • RIVERSIDE RETREAT • SUNSET CATAMARAN EXCLUSIVITY Explore the timeless monuments of Old Goa, the former capital of the Portuguese Eastern Empire. Visit the stunning Basilica of Bom Jesus, which houses the sacred remains of St. Francis Xavier, and the grand Se Cathedral. In the afternoon, transfer to a private marina where TRAGUIN has chartered an exclusive luxury catamaran yacht for your family or partner. Cruise down the peaceful Mandovi River backwaters while enjoying fine beverages as the sun sets over the Arabian Sea.'
                ),
                [
                    'Sightseeing Included: Basilica of Bom Jesus, Se Cathedral, Church of St. Cajetan.',
                    "Evening Experience: 2-Hour Private Yacht Cruise with butler service and customized hors d'oeuvres.",
                    'Overnight Stay: North Goa Beachfront / Heritage Resort',
                    'Meals Included: Premium Breakfast & Sunset Yacht Canapés',
                ],
            ),            _day(
                5,
                'SOUTHERN HERITAGE MANORS & UNTOUCHED SHORES',
                (
                    "SOUTH GOA ELEGANCE • PRIVATE PALACE TOUR • TRANQUIL COVE After a morning of leisure, travel south into the serene, emerald heart of South Goa. Visit the majestic Palacio do Deao in Quepem, a 213-year-old historic mansion situated on the banks of the Kushavati River. Enjoy a private tour of the palace's lush gardens, followed by a customized culinary experience. Spend your late afternoon listening to the quiet surf at Utorda or Arossim Beach, known for its pristine white sands and absolute peace."
                ),
                [
                    'Sightseeing Included: Palacio do Deao Heritage Manor, Arossim Beachfront.',
                    'Optional Activities: An indulgent luxury Ayurvedic spa treatment at your resort.',
                    'Overnight Stay: South Goa Ultra Luxury Resort (Taj Exotica or similar)',
                    'Meals Included: Premium Breakfast & Traditional Indo-Portuguese Manor Lunch',
                ],
            ),            _day(
                6,
                'DIVAR ISLAND STEP-BACK IN TIME',
                (
                    'ISLAND ISOLATION • ECO-LUXURY EXPERIENCES • FAREWELL GALA DINNER Board an exclusive river ferry with your private vehicle to land on the peaceful shores of Divar Island. This untouched paradise feels a world away from modern life, featuring winding lanes, historic hilltop churches, and traditional Portuguese villas. Return to your ultra-luxury resort for an afternoon of relaxation. In the evening, enjoy a grand farewell gala dinner arranged directly on the sand under a starry sky.'
                ),
                [
                    'Sightseeing Included: Divar Island Village Exploration, Piedade Church, South Goa Coastline.',
                    'Evening Experience: Private beachside multi-course dinner with live violin music.',
                    'Overnight Stay: South Goa Ultra Luxury Resort (Taj Exotica or similar)',
                    'Meals Included: Premium Breakfast & Exclusive Farewell Gala Beach Dinner',
                ],
            ),            _day(
                7,
                'DEPARTURE FROM PARADISE',
                (
                    "FINAL LAGOON REFRESHER • CHERISHING UNFORGETTABLE MEMORIES Indulge in a final morning breakfast buffet featuring authentic coastal specialties. Enjoy a last swim in your resort's lagoon-style pool or take a quiet stroll along the shoreline. Your private luxury transport vehicle will pick you up for a smooth transfer back to the airport, ensuring you depart with wonderful, unforgettable memories designed flawlessly by TRAGUIN."
                ),
                [
                    'Transfers Included: Private luxury door-to-door departure terminal transfer.',
                    'Meals Included: Sumptuous Buffet Breakfast array',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Taj Fort Aguada Beach Resort | Kenilworth Resort & Spa / similar',
                'North Goa (3 Nights) / South Goa (3 Nights)',
                '06 Nights',
                'Deluxe',
                'Deluxe Room',
                'CP (Breakfast)',
                4,
                1,
                description='OPTION 01 – DELUXE: Taj Fort Aguada Beach Resort (North Goa (3 Nights)) | Kenilworth Resort & Spa / similar (South Goa (3 Nights)) | CP (Breakfast)',
            ),
            _hotel(
                'Taj Holiday Village Resort & Spa | The Leela Goa (Lagoon Suite)',
                'North Goa (3 Nights) / South Goa (3 Nights)',
                '06 Nights',
                'Premium',
                'Premium Room',
                'CP (Breakfast)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Taj Holiday Village Resort & Spa (North Goa (3 Nights)) | The Leela Goa (Lagoon Suite) (South Goa (3 Nights)) | CP (Breakfast)',
            ),
            _hotel(
                'Taj Cidade de Goa Heritage / Resort | Taj Exotica Resort & Spa (Luxury Villa)',
                'North Goa (3 Nights) / South Goa (3 Nights)',
                '06 Nights',
                'Luxury',
                'Luxury Villa',
                'CP + Honeymoon Amenities',
                5,
                3,
                description='OPTION 03 – LUXURY: Taj Cidade de Goa Heritage / Resort (North Goa (3 Nights)) | Taj Exotica Resort & Spa (Luxury Villa) (South Goa (3 Nights)) | CP + Honeymoon Amenities',
            ),
            _hotel(
                'The St. Regis Goa Resort / Villa Tier | Taj Exotica (Plunge Pool Private Villa)',
                'North Goa (3 Nights) / South Goa (3 Nights)',
                '06 Nights',
                'Ultra Luxury',
                'Plunge Pool Private Villa',
                'VVIP Concierge & Butler Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The St. Regis Goa Resort / Villa Tier (North Goa (3 Nights)) | Taj Exotica (Plunge Pool Private Villa) (South Goa (3 Nights)) | VVIP Concierge & Butler Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Airfare, domestic flight connections, or', 1),
            _inc_excluded('interstate train tickets.', 2),
            _inc_excluded('Any water sports, scuba diving fees, or club', 3),
            _inc_excluded('entrance charges.', 4),
            _inc_excluded('Monument entry tickets, local camera fees, or', 5),
            _inc_excluded('historical guide gratuities.', 6),
            _inc_excluded('Personal expenses such as laundry, premium', 7),
            _inc_excluded('vintage liquors, or room service.', 8),
        ],
    )
    return package, itinerary

def build_ga_019(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-019'
    tour_code = 'TRG-GOA-019'
    title = 'TRAGUIN Premium Goa Tour Package — Premium Villa & Private Yacht Experience'
    duration = '05 Nights / 06 Days'
    slug = 'ga-019-premium-villa-private-yacht'
    itin_slug = 'ga-019-premium-villa-private-yacht-itinerary'
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
            _ph('Serial code GA-019 | TRAGUIN tour code TRG-GOA-019', 1),
            _ph('State / Country: Goa / India | Category: Luxury Holiday', 2),
            _ph('Destinations: North Goa •', 3),
            _ph('Ideal for: Families, Couples, and HNWIs seeking Premium Customization', 4),
            _ph('Best season: October to April (Pleasant Coastal Skies)', 5),
            _ph('Starting price: On Request (Ultra- Luxury Villa Portfolio Pricing)', 6),
            _ph('Vehicle / Meals: Chauffeur-Driven', 7),
            _ph('TRAGUIN Signature Experience: Private 3-hour luxury yacht charter along the sunset coast, complete', 8),
            _ph('Curated by TRAGUIN Experts: Custom-tailored dining arrangements at top, hard-to-book heritage', 9),
            _ph('Personalized Assistance: A dedicated local guest manager on call 24/7 to adjust plans to your', 10),
            _ph('Premium Handpicked Hotels: Elite properties chosen for their absolute safety, high-end hospitality, and', 11),
            _ph('Local Markets & Souvenirs: Explore the high-end artisan boutiques of Assagao and the lively Saturday Night Bazaar. Bring home beautiful, hand-painted Azulejos ceramic tiles, premium local feni, organic Goan spices, and handcrafted resort wear. Cafes & Food Recommendations: Indulge in fresh, line-caught seafood cooked with authentic Goan recheado masala. Visit charming beachside shacks for cold drinks, or enjoy innovative, modern fusion cuisine in restored colonial-era villas.', 12),
            _ph('& BOOKING GUIDELINES', 13)
        ],
        moods=['Luxury', 'Romantic', 'Family', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Ultra- Luxury Villa Portfolio Pricing)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Premium Villa & Private Yacht Experience',
        overview="DAYS Welcome to a realm of sun-kissed opulence and golden horizon coastlines, meticulously curated by TRAGUIN. Embark on the absolute Best Goa Tour Package designed for the ultra-wealthy voyager. This\n\nTOUR OVERVIEW\nTravel Dates: Flexible / Customizable Upon Request Group / FIT: Customized Private FIT Tour Vehicle: Chauffeur-Driven Premium Luxury SUV available round-the-clock Meal Plan: Modified American Plan Plus (Lavish Daily Breakfasts & Curated Gourmet Dinners at Top-Rated Fine Dining Restaurants) Route: North Goa Private Villa Estate ➔ Mandovi River Yachting ➔ South Goa Heritage Enclaves TRAGUIN Curated Experience Note: This elite package includes a private 3-hour luxury yacht charter, exclusive entry privileges into Goa's high-end colonial estates, and a dedicated, 24/7 personal guest experience manager. DESTINATION LIFESTYLE & HERITAGE Choosing a Luxury Goa Holiday means immersing your senses into a beautiful blend of Indo-Portuguese history, pristine coastlines, and a thriving elite lifestyle. Goa offers highly sought-after, famous attractions that cater perfectly to both relaxation and high-octane celebration. From the sun-bleached ramparts of Aguada Fort to the legendary white sands of South Goa, the state remains India’s premier coastal paradise. For travelers booking our signature TRAGUIN Goa Packages, the region unveils its most searched experiences: private beach dining, sunset yachting, and exploring popular Instagram locations like the colorful, historic Latin Quarter of Fontainhas and the dramatic, cliffside infinity pools of Vagator. Delve into high-end boutique shopping, discover ancient spice plantations, and experience vibrant nightlife at exclusive beach clubs. This carefully planned itinerary maximizes your time during the best time to visit Goa, ensuring top tourist places in Goa are discovered through a lens of pure privilege. THE DAY-WISE ITINERARY",
        seo_title='GA-019 | Goa | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Goa package (GA-019 / TRG-GOA-019): North Goa •.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA', 1),
            _ih('Day 02: PRIVATE YACHT EXPERIENCE', 2),
            _ih('Day 03: NORTH GOA EXPLORATION', 3),
            _ih('Day 04: OLD GOA & FONTAINHAS LATIN QUARTER', 4),
            _ih('Day 05: SOUTH GOA PRISTINE RETREAT', 5),
            _ih('Day 06: DEPARTURE FROM GOA', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA',
                (
                    'WELCOME TO THE TROPICAL RIVIERA – LUXURY VILLA ARRIVAL Your premium Goa sightseeing getaway begins the moment you touch down. Upon your arrival experience at Manohar International Airport (MOPA) or Dabolim Airport, you will be greeted warmly by your private luxury transportation vehicle. Enjoy a scenic route winding past swaying coconut grooves to your exclusive private villa estate in North Goa. Enjoy a seamless in-villa check-in process, complete with gourmet signature welcome drinks. The afternoon is yours to relax by your private pool or stroll along a tranquil nearby beach.'
                ),
                [
                    'Sightseeing Included: Private villa estate check-in, exclusive coastal drive orientation.',
                    'Evening Experience: An elegant, private welcome dinner prepared by a personal chef inside your villa.',
                    'Overnight Stay: North Goa Handpicked Ultra-Luxury Private Villa',
                    'Meals Included: Welcome Drink & Gourmet Dinner',
                ],
            ),            _day(
                2,
                'PRIVATE YACHT EXPERIENCE',
                (
                    "SAILING THE MANDOVI IN ABSOLUTE OPULENCE Indulge in a beautiful morning breakfast inside your villa's sunlit gazebo. In the afternoon, your chauffeur will escort you to the private jetty to board a magnificent, fully crewed private luxury yacht chartered exclusively for your family by TRAGUIN. Cruise along the calm waters of the Mandovi River out towards the Arabian Sea. Sip premium champagne and enjoy gourmet finger foods as you take in the breathtaking landscapes and a spectacular coastal sunset from the open deck. This is a top-tier romantic highlight for any Goa honeymoon package."
                ),
                [
                    'Sightseeing Included: Panaji coastal skyline, historic Reis Magos Fort from the water, sunset ocean views.',
                    'Optional Activities: Deep-sea fishing or a professional drone photography session on the yacht deck.',
                    'Overnight Stay: North Goa Handpicked Ultra-Luxury Private Villa',
                    'Meals Included: Lavish Breakfast & On-Board High Tea Refreshments',
                ],
            ),            _day(
                3,
                'NORTH GOA EXPLORATION',
                (
                    'FORTRESSES, HERITAGE, AND CHIC CAFE CULTURE Set out today to discover the legendary iconic attractions of North Goa. Tour the historic Aguada Fort, taking in its expansive sea views and historic lighthouse structure. Next, head inland to the trendy village of Assagao, affectionately called the "Cannes of Goa," known for its beautiful architecture and popular Instagram locations. Stroll past carefully preserved heritage mansions and explore high-end fashion boutiques before enjoying lunch at an award-winning garden restaurant.'
                ),
                [
                    'Sightseeing Included: Aguada Fort, Sinquerim Beach, Assagao Heritage Lanes, Vagator Cliffside viewpoint.',
                    'Evening Experience: Reserved premium lounge access at an exclusive beachfront club for sunset drinks.',
                    'Overnight Stay: North Goa Handpicked Ultra-Luxury Private Villa',
                    'Meals Included: Premium Breakfast & Curated Beach-Club Dinner',
                ],
            ),            _day(
                4,
                'OLD GOA & FONTAINHAS LATIN QUARTER',
                (
                    'INDO-PORTUGUESE SPLENDOR & COLONIAL VIBRANCY Immerse yourself today in the deep history and culture of Goa. Travel back in time with a visit to Old Goa, featuring the magnificent Basilica of Bom Jesus, a UNESCO World Heritage site. Afterward, enjoy a private walking tour through Fontainhas, the historic Latin Quarter of Panaji. Walk hand-in-hand past vibrant, brightly colored Portuguese houses with ornate iron balconies, taking in the old-world charm that makes this area a favorite photography point.'
                ),
                [
                    'Sightseeing Included: Basilica of Bom Jesus, Se Cathedral, Fontainhas Latin Quarter, Maruti Temple.',
                    'Optional Activities: Private fado music performance access paired with vintage port wine tasting.',
                    'Overnight Stay: North Goa Handpicked Ultra-Luxury Private Villa',
                    'Meals Included: Premium Breakfast & Fine Dining Portuguese-Goan Dinner',
                ],
            ),            _day(
                5,
                'SOUTH GOA PRISTINE RETREAT',
                (
                    'WHITE SANDS AND PRIVATE RIVERSIDE ELEGANCE Today, head south to experience the peaceful tranquility and natural, scenic beauty of South Goa. Relax on the uncrowded, pristine shores of Utorda or Arossim Beach, known for their fine white sands and peaceful ambiance. In the afternoon, enjoy a private tour of a historic 18th-century colonial mansion, where you can learn about the fascinating lifestyle of Goan nobility.'
                ),
                [
                    'Sightseeing Included: Pristine South Goan Beaches, Palacio do Deao heritage house and gardens.',
                    'Evening Experience: A beautiful farewell seafood dinner served under the stars on a private beach stretch.',
                    'Overnight Stay: North Goa Handpicked Ultra-Luxury Private Villa',
                    'Meals Included: Premium Breakfast & Farewell Beachfront Dinner',
                ],
            ),            _day(
                6,
                'DEPARTURE FROM GOA',
                (
                    'CHERISHING THE MEMORIES OF A TROPICAL PARADISE Enjoy a last relaxing morning swimming in your private pool, followed by a delicious breakfast spread. Pack your bags and say a fond farewell to your villa team. Your private luxury transport will arrive to convey you smoothly to MOPA or Dabolim Airport for your return flight. Head home carrying unforgettable memories and beautiful shared moments, all meticulously arranged by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door airport transfer.',
                    'Meals Included: Sumptuous In-Villa Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Taj Resort & Convention Centre / Cidade de Goa',
                'Goa (5 Nights)',
                '05 Nights',
                'Deluxe',
                'Premium Sea View Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Taj Resort & Convention Centre / Cidade de Goa (Goa (5 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'W Goa (Vagator) / Heritage Village Resort',
                'Goa (5 Nights)',
                '05 Nights',
                'Premium',
                'Wonderful Room / Private Chalet',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: W Goa (Vagator) / Heritage Village Resort (Goa (5 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Leela Goa / Taj Exotica Resort & Spa',
                'Goa (5 Nights)',
                '05 Nights',
                'Luxury',
                'Luxury Conservatory Premier Suite',
                'Bespoke Gourmet MAPAI Plan',
                5,
                3,
                description='OPTION 03 – LUXURY: The Leela Goa / Taj Exotica Resort & Spa (Goa (5 Nights)) | Bespoke Gourmet MAPAI Plan',
            ),
            _hotel(
                'TRAGUIN Private Elite Villa Collection (Assagao/Candolim)',
                'Goa (5 Nights)',
                '05 Nights',
                'Ultra Luxury',
                'Exclusive 4/5 BHK Private Pool Villa Estate',
                'VVIP Private Chef & Dining Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Private Elite Villa Collection (Assagao/Candolim) (Goa (5 Nights)) | VVIP Private Chef & Dining Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Flights: Domestic or international airfare tickets to', 1),
            _inc_excluded('and from Goa.', 2),
            _inc_excluded('Entry Tickets: Individual monument entry fees or', 3),
            _inc_excluded('museum entry permissions.', 4),
            _inc_excluded('Personal Expenses: Laundry service, premium', 5),
            _inc_excluded('alcoholic drinks, and gratuities.', 6),
            _inc_excluded('Activities: Water sports, club entry covers, and', 7),
            _inc_excluded('optional tours not listed.', 8),
        ],
    )
    return package, itinerary

def build_ga_020(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-020'
    tour_code = 'TRG-GOA-MICE-020'
    title = 'TRAGUIN Premium Goa Tour Package — Corporate Beach Meet MICE'
    duration = '03 Nights / 04 Days'
    slug = 'ga-020-corporate-beach-meet-mice'
    itin_slug = 'ga-020-corporate-beach-meet-mice-itinerary'
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
            _ph('Serial code GA-020 | TRAGUIN tour code TRG-GOA-MICE-020', 1),
            _ph('State / Country: Goa / India | Category: Corporate MICE &', 2),
            _ph('Destinations: North Goa • South Goa', 3),
            _ph('Ideal for: Corporate Retreats, Team Building & Leadership Conferences', 4),
            _ph('Best season: October to May', 5),
            _ph('Starting price: On Request (Bespoke MICE Tariff)', 6),
            _ph('Vehicle / Meals: Premium AC', 7),
            _ph('TRAGUIN Signature Experience: Private oceanfront team-building orchestration handled by certified', 8),
            _ph('Curated by TRAGUIN Experts: Seamless coordination between the conference schedule and evening', 9),
            _ph('Premium Handpicked Hotels: Accommodations chosen strictly based on world-class MICE amenities,', 10),
            _ph('Luxury Transportation: Courteous, background-checked coach captains ensuring safe and uniform', 11),
            _ph("Local Souvenirs: Take home classic Goan memorabilia including premium feni spirits, organic locally-grown cashews, handcrafted terracotta pottery, and classic Mario Miranda artwork items from Panaji's luxury gift boutiques. Food & Cafes: Treat your delegates to rich multi-culinary flavors, traditional Goan fish curry rice, and authentic bebinca desserts at high-end seaside shacks or modern historic bistros.", 12),
            _ph('Hotel Policies: Group check-in usually takes place around 15:00 hrs. Early access depends strictly on', 13)
        ],
        moods=['Luxury', 'Beach', 'Family'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Bespoke MICE Tariff)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Corporate Beach Meet MICE',
        overview='Welcome to an elite corporate arena where productivity seamlessly intersects with seaside opulence, exclusively curated by TRAGUIN. Embark on a definitive Goa Corporate MICE experience engineered to motivate, reward, and unite your leadership team. As your professional travel consultants, TRAGUIN transforms standard corporate agendas into a high-end luxury holiday filled with premium stays, immersive experiences, and top-tier hospitality. From high-tech conference spaces overlooking the Arabian Sea to sand-side networking events, your organization will return with aligned visions and unforgettable memories.\n\nTOUR OVERVIEW\nThis private custom-tailored MICE itinerary provides an impeccable balance between rigorous business conferences, state-of-the-art team-building exercises, and elite coastal leisure. Transported in a fleet of premium air-conditioned luxury coaches under the constant watch of dedicated TRAGUIN onsite managers, your delegates are treated to an unmatched professional environment. With an ultra-premium dining plan featuring lavish oceanfront lunches and private gala dinners, this route represents the finest premium Goa experience. Every moment integrates a TRAGUIN curated experience note, from VIP express hotel check-ins to bespoke audio-visual execution.',
        seo_title='GA-020 | Goa | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Goa package (GA-020 / TRG-GOA-MICE-020): North Goa • South Goa.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA & BEACHFRONT NETWORKING', 1),
            _ih('Day 02: STRATEGIC CONFERENCE & GALA EXTRAVAGANZA', 2),
            _ih('Day 03: HERITAGE TOUR & PRIVATE CHARTER CRUISE', 3),
            _ih('Day 04: LEISURE & DEPARTURE', 4)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA & BEACHFRONT NETWORKING',
                (
                    'ELITE WELCOME, PRIVATE CHECK-IN & SUNSET NETWORKING Your premium Goa experience officially begins as your delegates arrive at Manohar International Airport (MOPA) or Dabolim Airport. A dedicated private luxury coach armada under the coordination of TRAGUIN experts greets the team. Enjoy an express, hassle-free private group check-in at a five-star luxury beachfront resort with a refreshing coastal welcome drink. Spend the afternoon prepping for the meet. In the evening, gather on a reserved segment of the beach for a high-end sunset networking reception with premium appetizers and ambient music.'
                ),
                [
                    'Sightseeing Included: Beachfront sunset landscape viewing, Resort orientation.',
                    'Evening Experience: Ocean-facing corporate networking cocktail meet with premium sound curation.',
                    'Overnight Stay: Goa (Handpicked 5-Star Luxury Beach Resort)',
                    'Meals Included: Welcome Drink & Elite Oceanfront Welcome Dinner',
                ],
            ),            _day(
                2,
                'STRATEGIC CONFERENCE & GALA EXTRAVAGANZA',
                (
                    'HIGH-TECH CONFERENCES & THEMED AWARDS GALA Commence the day with a sprawling international breakfast spread. Gather in the grand ballroom for your official corporate session. The venue features high-end audio-visual alignment, dedicated business support, and gourmet mid-session coffee breaks. After a highly productive corporate meet and an oceanfront lunch buffet, transition into the outdoors for tailored beach-side team-building exercises. In the evening, the energy builds as delegates attend a themed corporate Gala Dinner featuring a live band, awards recognition, and premium beverage options.'
                ),
                [
                    'Sightseeing Included: Resort beachfront view spaces, High-end audio-visual presentation hall setup.',
                    'Optional Activities: Executive mental wellness and beach yoga sessions prior to the conference.',
                    'Overnight Stay: Goa (Handpicked 5-Star Luxury Beach Resort)',
                    'Meals Included: Premium Breakfast, Conference Lunch & Grand Gala Dinner',
                ],
            ),            _day(
                3,
                'HERITAGE TOUR & PRIVATE CHARTER CRUISE',
                (
                    'CULTURE, SIGHTSEEING & PRIVATE LUXURY YACHT CELEBRATION Embark on an insightful cultural sightseeing journey after breakfast. Explore the breathtaking landscapes of Old Goa, visiting iconic attractions like the Basilica of Bom Jesus and Se Cathedral. Meander through the colorful Fontainhas Latin Quarter—a highly sought-after Instagram location for group photography. Late in the afternoon, transfer to the jetty for an absolute highlight of your corporate meet: an exclusive private luxury charter cruise along the Mandovi River, complete with sundowner mocktails, an onboard DJ, and panoramic sea views.'
                ),
                [
                    'Sightseeing Included: Old Goa Churches, Fontainhas Latin Quarter, Mandovi River Cruise.',
                    'Evening Experience: Private luxury yacht sundowner cruise with live music and coastal snacks.',
                    'Overnight Stay: Goa (Handpicked 5-Star Luxury Beach Resort)',
                    'Meals Included: Premium Breakfast, Authentic Goan Lunch & Yacht Dinner',
                ],
            ),            _day(
                4,
                'LEISURE & DEPARTURE',
                (
                    'RETURNING WITH ALIGNED VISIONS & UNFORGETTABLE MEMORIES Indulge in a final morning breakfast overlooking the azure sea waves. Take some time for souvenir shopping at the resort boutique or enjoy a final swim in the infinity pool. Your fleet of private luxury coaches will gather your group for a smooth, coordinated transfer back to the airport. Your corporate team departs carrying renewed enthusiasm and unforgettable memories sculpted perfectly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Coordinated private group airport departure transfers.',
                    'Meals Included: Lavish Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Goa Resort & Spa / Fairfield by Marriott',
                'Goa (3 Nights)',
                '03 Nights',
                'Deluxe',
                'Superior Garden View Room',
                'Ultra Luxury All-Inclusive Plan',
                4,
                1,
                description='OPTION 01 – DELUXE: Novotel Goa Resort & Spa / Fairfield by Marriott (Goa (3 Nights)) | Ultra Luxury All-Inclusive Plan',
            ),
            _hotel(
                'Grand Hyatt Goa / W Goa / similar',
                'Goa (3 Nights)',
                '03 Nights',
                'Premium',
                'Premium Pool View Room',
                'Ultra Luxury All-Inclusive Plan',
                4,
                2,
                description='OPTION 02 – PREMIUM: Grand Hyatt Goa / W Goa / similar (Goa (3 Nights)) | Ultra Luxury All-Inclusive Plan',
            ),
            _hotel(
                'Taj Exotica Resort & Spa / The Leela Goa',
                'Goa (3 Nights)',
                '03 Nights',
                'Luxury',
                'Luxury Ocean View Room',
                'Ultra Luxury All-Inclusive Plan',
                5,
                3,
                description='OPTION 03 – LUXURY: Taj Exotica Resort & Spa / The Leela Goa (Goa (3 Nights)) | Ultra Luxury All-Inclusive Plan',
            ),
            _hotel(
                'ITC Grand Goa Resort & Spa (Private Beachfront)',
                'Goa (3 Nights)',
                '03 Nights',
                'Ultra Luxury',
                'VVIP Sea Facing Luxury Suite',
                'Ultra Luxury All-Inclusive Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: ITC Grand Goa Resort & Spa (Private Beachfront) (Goa (3 Nights)) | Ultra Luxury All-Inclusive Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Domestic or International air tickets to/from', 1),
            _inc_excluded('Any personal laundry, room mini-bar', 2),
            _inc_excluded('consumption, or long-distance phone charges.', 3),
            _inc_excluded('Individual adventure watersports, specialized', 4),
            _inc_excluded('spa sessions, or entry tickets.', 5),
            _inc_excluded('Extended tours or vehicle runs beyond the', 6),
            _inc_excluded('predefined corporate itinerary.', 7),
        ],
    )
    return package, itinerary

def build_ga_021(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-021'
    tour_code = 'TRG-GOA-021'
    title = 'TRAGUIN Premium Goa Tour Package — Educational History & Science Tour'
    duration = '04 Nights / 05 Days'
    slug = 'ga-021-educational-history-science-tour'
    itin_slug = 'ga-021-educational-history-science-tour-itinerary'
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
            _ph('Serial code GA-021 | TRAGUIN tour code TRG-GOA-021', 1),
            _ph('State / Country: Goa / India | Category: School Educational', 2),
            _ph('Destinations: Panaji • Old Goa •', 3),
            _ph('Ideal for: Students, Academic Batches & Educational Institutions', 4),
            _ph('Best season: October to May (Excellent for field studies)', 5),
            _ph('Starting price: On Request (Premium Group Customised Rate)', 6),
            _ph('Vehicle / Meals: Premium Luxury Multi-Axle', 7),
            _ph('TRAGUIN Signature Experience: Private expert-led history briefing and architectural mapping before', 8),
            _ph('Curated by TRAGUIN Experts: Well-paced routing planned away from congested tourist crowds to', 9),
            _ph('Premium Handpicked Hotels: Properties selected strictly based on stringent safety records, perimeter', 10),
            _ph('Luxury Transportation: Fleet of audited luxury touring coaches driven by verified, professional drivers.', 11),
            _ph('Local Markets & Souvenirs: Take a curated shopping trip to find authentic Goan premium cashews, local feni-infused handmade chocolates, traditional clay crafts, and unique hand-painted Azulejos tiles as souvenirs. Cafes & Food: Enjoy refreshing tropical fruit juices, regional Bebinca layer dessert delicacies, and organic farm-to-table treats at the plantation cafes.', 12),
            _ph('Hotel Policies: Uniform check-in is at 14:00 hrs and check-out at 11:00 hrs. Student lists with institute IDs', 13)
        ],
        moods=['Family', 'Beach', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Group Customised Rate)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Educational History & Science Tour',
        overview='BEACHES Welcome to a beautifully designed academic expedition curated by TRAGUIN. This exclusive Goa Family Tour and School Group Package redefines traditional excursions by combining absolute premium comfort with profound, experiential learning. Often celebrated merely for its coastline, Goa holds an extraordinary wealth of scientific, ecological, and historical value. As your professional travel consultants, TRAGUIN has orchestrated an immersive itinerary that weaves the breathtaking landscapes of the Western Ghats together with monumental architectural relics and innovative science exhibits, transforming this journey into an array of unforgettable memories.\n\nTOUR OVERVIEW\nThis elite academic itinerary is crafted to satisfy the intellectual curiosity of students while providing the flawless safety and organization expected of a luxury holiday. Traveling across the state in a dedicated fleet of premium high-deck coaches equipped with advanced safety mechanics and overseen by a professional TRAGUIN tour manager, the group will cover historical Portuguese settlements, advanced oceanographic research centers, and tropical botanical ecosystems. With a comprehensive full-board meal plan featuring hygienic, custom-curated food options at handpicked hotels, this premium Goa experience perfectly combines safety, prestige, and immersive learning.',
        seo_title='GA-021 | Goa | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Goa package (GA-021 / TRG-GOA-021): Panaji • Old Goa •.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA & MANDUVI RIVER CRUISE', 1),
            _ih('Day 02: HISTORICAL EXPLORATION OF OLD GOA & LATIN QUARTER', 2),
            _ih('Day 03: SCIENCE CENTRE & INTERACTIVE OCEANOGRAPHY EXPERIENCES', 3),
            _ih('Day 04: ECO-BOTANY & AGRICULTURAL SCIENCE IN PONDA', 4),
            _ih('Day 05: NAVAL AVIATION MUSEUM & DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA & MANDUVI RIVER CRUISE',
                (
                    "WELCOME TO THE GATEWAY OF ENLIGHTENMENT – URBAN HISTORY & HERITAGE Your premium Goa experience begins as your flight or train arrives. You will be warmly greeted by your private luxury transport team. Transfer smoothly to your handpicked premium accommodation, where a dedicated student check-in lounge and refreshment drinks await. After an afternoon orientation session, step out to explore the scenic beauty of Panaji. In the evening, enjoy a curated educational cruise on the Mandovi River, highlighting the historical maritime importance of Goa's ancient trade routes. TRAGUIN experts."
                ),
                [
                    'Sightseeing Included: Panaji City Walk, Miramar Beach Shoreline, Mandovi River Cruise.',
                    'Evening Experience: Cultural folk dance observation and historical talk onboard the cruise, curated by',
                    'Overnight Stay: Panaji / North Goa (Premium Selected Group Hotel)',
                    'Meals Included: Welcome Amenities, Lunch & Luxury Dinner',
                ],
            ),            _day(
                2,
                'HISTORICAL EXPLORATION OF OLD GOA & LATIN QUARTER',
                (
                    'COLONIAL ARCHITECTURE & THE CRADLE OF INDO-PORTUGUESE CULTURE Awake early for a healthy breakfast before traveling back in time to explore the iconic attractions of Old Goa, the former capital under Portuguese rule. Walk through the breathtakingly massive Basilica of Bom Jesus and the majestic Se Cathedral, studying the structural engineering of late 16th-century Renaissance architecture. In the afternoon, explore Fontainhas—the Latin Quarter of Panaji—a popular Instagram location famous for its bright Mediterranean-style architecture, rich tilework, and heritage art galleries. Quarter.'
                ),
                [
                    'Sightseeing Included: Basilica of Bom Jesus, Se Cathedral, Archaeological Museum of Goa, Fontainhas Latin',
                    'Optional Activities: Interactive architectural sketch workbook session led by local preservation experts.',
                    'Overnight Stay: Panaji / North Goa (Premium Selected Group Hotel)',
                    'Meals Included: Breakfast, Mid-Day Field Lunch & Managed Dinner',
                ],
            ),            _day(
                3,
                'SCIENCE CENTRE & INTERACTIVE OCEANOGRAPHY EXPERIENCES',
                (
                    'MARINE INTERACTIVE RESEARCH & THE WONDERS OF SCIENTIFIC PHYSICS Dedicate today to scientific innovation and hands-on experiments. Visit the renowned Goa Science Centre & Planetarium, taking part in immersive experiences through the 3D starry sky theater, mirror mazes, and outdoor physics parks. Following lunch, head to Dona Paula to understand ocean currents and marine preservation. Students will complete guided research sheets on the unique coastal geography and ecosystems of Goa.'
                ),
                [
                    'Sightseeing Included: Goa Science Centre & Planetarium, Dona Paula Jetty, Caranzalem Bay.',
                    'Evening Experience: Science quiz competition and planetarium celestial viewing session with premium prizes.',
                    'Overnight Stay: Panaji / North Goa (Premium Selected Group Hotel)',
                    'Meals Included: Breakfast, Lunch & Gourmet Institutional Dinner',
                ],
            ),            _day(
                4,
                'ECO-BOTANY & AGRICULTURAL SCIENCE IN PONDA',
                (
                    'BIODIVERSITY BASICS & HORTICULTURAL FIELD WORK Journey into the green heart of Ponda to discover the rich flora and fauna of the Western Ghats. Tour a premium tropical spice plantation, walking along paths filled with aromatic plants, black pepper vines, and rare medicinal herbs. Learn about advanced sustainable farming, natural vermicomposting, and rainwater harvesting techniques. Conclude your afternoon by visiting the majestic Fort Aguada to study coastal defensive design and historical lighthouse engineering.'
                ),
                [
                    'Sightseeing Included: Ponda Tropical Spice Plantation, Sinquerim Coastal Fort, Aguada Fortress & Lighthouse.',
                    'Optional Activities: Traditional Goan plantation lunch served over fresh eco-friendly banana leaves.',
                    'Overnight Stay: Panaji / North Goa (Premium Selected Group Hotel)',
                    'Meals Included: Breakfast, Traditional Organic Spice Farm Buffet Lunch & Farewell Gala Dinner',
                ],
            ),            _day(
                5,
                'NAVAL AVIATION MUSEUM & DEPARTURE',
                (
                    'AERONAUTICAL MARVELS – SHAPING UNFORGETTABLE MEMORIES On the final morning of your luxury holiday, check out and drive towards Bogmalo to tour the unique Naval Aviation Museum. This iconic attraction stands as one of the few naval aviation museums in Asia. It offers an incredible view of decommissioned aircraft, jet fighters, and deep-sea rescue gear, inspiring young minds with aeronautical engineering principles. Your private luxury transport will then guide you comfortably to Goa Airport or Madgaon Station for your journey home, carrying unforgettable memories designed beautifully by TRAGUIN.'
                ),
                [
                    'Transfers Included: Naval Aviation Museum, Final Airport/Station drop-off coordination.',
                    'Meals Included: Sumptuous Buffet Breakfast & Packed Departure Lunch',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Country Inn & Suites by Radisson / similar',
                'Panaji / North Goa (4 Nights)',
                '04 Nights',
                'Deluxe',
                'Standard Triple Shared Wing',
                'Full Board (All Meals)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Country Inn & Suites by Radisson / similar (Panaji / North Goa (4 Nights)) | Full Board (All Meals)',
            ),
            _hotel(
                'Fortune Miramar by ITC Hotel Group / similar',
                'Panaji / North Goa (4 Nights)',
                '04 Nights',
                'Premium',
                'Premium Twin Shared Room Wing',
                'Full Board (All Meals)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Fortune Miramar by ITC Hotel Group / similar (Panaji / North Goa (4 Nights)) | Full Board (All Meals)',
            ),
            _hotel(
                'The O Hotel / Vivanta Goa Panaji',
                'Panaji / North Goa (4 Nights)',
                '04 Nights',
                'Luxury',
                'Luxury Executive Double Room Wing',
                'Full Board + High Tea Service',
                5,
                3,
                description='OPTION 03 – LUXURY: The O Hotel / Vivanta Goa Panaji (Panaji / North Goa (4 Nights)) | Full Board + High Tea Service',
            ),
            _hotel(
                'Taj Cidade de Goa Horizon / Grand Hyatt Goa',
                'Panaji / North Goa (4 Nights)',
                '04 Nights',
                'Ultra Luxury',
                'VVIP Deluxe Oceanfront Institutional Suite',
                'Elite Custom Luxury Dining Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Taj Cidade de Goa Horizon / Grand Hyatt Goa (Panaji / North Goa (4 Nights)) | Elite Custom Luxury Dining Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Interstate flights, airfare, or long-distance', 1),
            _inc_excluded('train tickers.', 2),
            _inc_excluded('Personal expenses like telephone bills, laundry, or', 3),
            _inc_excluded('room service.', 4),
            _inc_excluded('Optional recreational watersports or beach', 5),
            _inc_excluded('rides.', 6),
            _inc_excluded('Any insurance policies or unforeseen medical', 7),
            _inc_excluded('hospitalization fees.', 8),
        ],
    )
    return package, itinerary

def build_ga_022(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-022'
    tour_code = 'TRG-GA-022'
    title = 'TRAGUIN Premium Goa Tour Package — South Goa Portuguese Heritage'
    duration = '04 Nights / 05 Days'
    slug = 'ga-022-south-goa-portuguese-heritage'
    itin_slug = 'ga-022-south-goa-portuguese-heritage-itinerary'
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
            _ph('Serial code GA-022 | TRAGUIN tour code TRG-GA-022', 1),
            _ph('State / Country: Goa / India | Category: South Goa', 2),
            _ph('Destinations: Panaji •', 3),
            _ph('Ideal for: Family Vacations, Heritage Lovers & Connoisseurs of Luxury', 4),
            _ph('Best season: November to April', 5),
            _ph('Starting price: On Request (Premium Bespoke Package)', 6),
            _ph('Vehicle / Meals: Private Luxury', 7),
            _ph('TRAGUIN Signature Experience: Private curator-led walk inside the family archives of the Braganza', 8),
            _ph('Curated by TRAGUIN Experts: Seamless routing planned to optimize travel time, avoiding busy paths for', 9),
            _ph('Premium Handpicked Hotels: Elite properties selected for their rich architectural heritage and child-', 10),
            _ph('Personalized Assistance: Direct access to local coordinators who know the best local hidden gems and', 11),
            _ph('Local Markets & Souvenirs: Take home authentic hand-painted Azulejos (Portuguese ceramic tiles), premium local cashew nuts, Goan chorizo sausage mixes, and high-end organic feni infusions. Cafes & Instagram Spots: Visit the vibrant cafes of Panaji and Margao for fresh pastéis de nata (egg tarts) paired with artisanal coffees, surrounded by beautiful tropical courtyards.', 12),
            _ph('& TRAVEL GUIDELINES', 13)
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
        price_note='On Request (Premium Bespoke Package)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='South Goa Portuguese Heritage',
        overview='Welcome to an extraordinary immersion into history, culture, and coastal luxury designed by TRAGUIN. Discover the timeless charm of our exclusive Goa Family Tour, meticulously tailored to unlock the architectural secrets, Latin quarters, and majestic heritage estates of South Goa. As your high-end travel partner, TRAGUIN transforms your vacation into a Luxury Goa Holiday filled with handpicked hotels, breathtaking landscapes, and elite privileges. Let the scenic beauty of colonial mansions, historic cathedrals, and sun-kissed sands serve as the setting for unforgettable memories with your loved ones.\n\nTOUR OVERVIEW\nThis bespoke luxury itinerary offers families a sophisticated escape far beyond standard beach resort travel. Journeying across Goa in a spacious private premium AC SUV accompanied by an experienced local expert chauffeur, your family will enjoy uncompromising privacy. Enjoy a curated meal plan featuring indulgent daily buffet breakfasts and fine regional dinners. Your route represents the ultimate premium Goa experience, integrating private curator-guided architecture walks, authentic culinary tastings, and the legendary TRAGUIN curated experience note ensuring priority entry and exclusive local experiences at every checkpoint.\n\nWHY CHOOSE THE BEST GOA TOUR PACKAGE?\nWhen planning a Luxury Goa Holiday, travelers looking for authenticity seek the rich cultural identity of South Goa. Our signature Goa Family Tour presents a side of the coastal state steeped in Indo-Portuguese heritage, featuring iconic attractions that tell a story of bygone eras. From the legendary Latin Quarter of Fontainhas—a highly popular Instagram location with candy-colored houses—to the UNESCO World Heritage sites of Old Goa, Goa sightseeing offers deep cultural value. Whether you are looking for a romantic Goa Honeymoon Package or an elegant family getaway, this route brings you to top tourist places in Goa, including grand mansions like the Braganza House in Chandor and the tranquil golden shores of Varca and Cavelossim. Indulge in unique boutique shopping, savor fine fusion dining, and explore lush spice plantations. Booking our specialized TRAGUIN Goa Packages ensures your family experiences the best time to visit Goa in absolute comfort with premium stays and flawless coordination.',
        seo_title='GA-022 | Goa | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Goa package (GA-022 / TRG-GA-022): Panaji •.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA – CHONGM OR PANAJI ARRIVAL', 1),
            _ih('Day 02: REVEALING OLD GOA’S COLONIAL SPLENDOR', 2),
            _ih('Day 03: SOUTH GOA PORTUGUESE MANSIONS EXCURSION', 3),
            _ih('Day 04: COASTAL LEISURE & PRIVATE SUNSET SAILING', 4),
            _ih('Day 05: DEPARTURE FROM GOA', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA – CHONGM OR PANAJI ARRIVAL',
                (
                    'WELCOME TO THE LATIN QUARTERS – PRIVATE HERITAGE EMBARKATION Your premium Goa experience starts the moment you land at Mopa or Dabolim Airport. A dedicated private luxury transport SUV waits to drive you smoothly to your handpicked premium hotel in Panaji or South Goa. After settling into your spacious room, head out for an afternoon walking tour of Fontainhas, the stunning Latin Quarter of Goa. Capture the scenic beauty of the pastel-hued Portuguese villas, ornate wrought-iron balconies, and narrow winding alleys. Conception. TRAGUIN experts.'
                ),
                [
                    'Sightseeing Included: Fontainhas Latin Quarter walking tour, Panaji Church of Our Lady of the Immaculate',
                    'Evening Experience: An intimate family dinner at a restored heritage Portuguese restaurant curated by',
                    'Overnight Stay: Panaji Heritage Boutique Luxury Hotel / South Goa Resort',
                    'Meals Included: Welcome Drink & Fine-Dining Dinner',
                ],
            ),            _day(
                2,
                'REVEALING OLD GOA’S COLONIAL SPLENDOR',
                (
                    'THE ARCHITECTURAL MARVELS OF A BYGONE EMPIRE Indulge in a premium breakfast before heading to Old Goa, the former capital under Portuguese rule and home to some of the most iconic attractions in India. Explore the awe-inspiring Basilica of Bom Jesus, which holds the sacred relics of St. Francis Xavier, and the grand Se Cathedral. Your private guide will share stories of historical events that shaped the region. In the afternoon, escape the heat with a private tour of a tropical spice plantation, featuring a traditional Goan family buffet lunch.'
                ),
                [
                    'Sightseeing Included: Basilica of Bom Jesus, Se Cathedral, Church of St. Cajetan, Ponda Spice Plantation.',
                    'Optional Activities: Feni tasting session and organic spice shopping directly from the plantation estate.',
                    'Overnight Stay: South Goa Luxury Beach Resort',
                    'Meals Included: Premium Breakfast, Plantation Lunch & Luxury Dinner',
                ],
            ),            _day(
                3,
                'SOUTH GOA PORTUGUESE MANSIONS EXCURSION',
                (
                    'THE GRANDEUR OF CHANDOR & MARGAO HERITAGE Dedicate today to exploring the luxurious country life of the pre-liberation Goan elite. Drive deep into the historic village of Chandor to explore the majestic Braganza House, a grand 350-year-old estate filled with priceless antiques, rare porcelain, and family relics. Next, visit the structural wonders of Palacio do Deao in Quepem, an architectural marvel nestled by the Kushavati River. Enjoy a personalized lunch on its beautiful veranda. square.'
                ),
                [
                    'Sightseeing Included: Menezes Braganza House (Chandor), Palacio do Deao (Quepem), Holy Spirit Church',
                    'Evening Experience: Relaxed stroll on the white sands of Colva Beach at sunset for a scenic family photo.',
                    'Overnight Stay: South Goa Luxury Beach Resort',
                    'Meals Included: Premium Breakfast, Indo-Portuguese Veranda Lunch & Dinner',
                ],
            ),            _day(
                4,
                'COASTAL LEISURE & PRIVATE SUNSET SAILING',
                (
                    'GOLDEN SANDS & EXCLUSIVE MARINE ROMANCE Spend a slow morning enjoying the elite amenities of your premium beach resort. Walk along the uncrowded beaches of South Goa, go for a swim, or book a therapeutic spa treatment. Late in the afternoon, arrive at the jetty for a private luxury yacht charter or premium catamaran catamaran sail. Take in breathtaking views as the sun dips below the Arabian Sea horizon—a truly unforgettable memory for the entire family.'
                ),
                [
                    'Sightseeing Included: Varca / Cavelossim pristine beach coastline, Luxury marine cruise lines.',
                    'Optional Activities: Beachside watersports or high-end seafood dining at iconic beach shacks.',
                    'Evening Experience: A special farewell family dinner alongside a beach bonfire, arranged by TRAGUIN support.',
                    'Overnight Stay: South Goa Luxury Beach Resort',
                    'Meals Included: Premium Breakfast & Beachfront Farewell Dinner',
                ],
            ),            _day(
                5,
                'DEPARTURE FROM GOA',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS Savor a final lavish buffet breakfast at your resort. Enjoy a few last moments by the pool before checking out. Your private premium vehicle will pick you up for a smooth transfer back to the airport or railway station. Return home with your hearts full of warm sunshine, deep cultural insights, and unforgettable memories carefully designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private door-to-door luxury airport drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Panjim Inn Heritage / Fairfield by Marriott Benaulim',
                'Panaji / South Goa (4 Nights)',
                '04 Nights',
                'Deluxe',
                'Premium Heritage / Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Panjim Inn Heritage / Fairfield by Marriott Benaulim (Panaji / South Goa (4 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Cidade de Goa (IHCL SeleQtions) / Heritage Village Resort',
                'Panaji / South Goa (4 Nights)',
                '04 Nights',
                'Premium',
                'Premium Sea Facing Room',
                'MAPAI Plan',
                4,
                2,
                description='OPTION 02 – PREMIUM: Cidade de Goa (IHCL SeleQtions) / Heritage Village Resort (Panaji / South Goa (4 Nights)) | MAPAI Plan',
            ),
            _hotel(
                'The Leela Goa / Taj Exotica Resort & Spa',
                'Panaji / South Goa (4 Nights)',
                '04 Nights',
                'Luxury',
                'Luxury Lagoon Suite / Garden Villa',
                'Bespoke MAPAI Package',
                5,
                3,
                description='OPTION 03 – LUXURY: The Leela Goa / Taj Exotica Resort & Spa (Panaji / South Goa (4 Nights)) | Bespoke MAPAI Package',
            ),
            _hotel(
                'ITC Grand Goa Resort & Spa / Alila Diwa (The Club)',
                'Panaji / South Goa (4 Nights)',
                '04 Nights',
                'Ultra Luxury',
                'VVIP Private Pool Villa Stay',
                'Elite Custom Culinary Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: ITC Grand Goa Resort & Spa / Alila Diwa (The Club) (Panaji / South Goa (4 Nights)) | Elite Custom Culinary Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Airfare, domestic flight costs, or interstate rail', 1),
            _inc_excluded('ticketing.', 2),
            _inc_excluded('Entry tickets to individual historical estates or', 3),
            _inc_excluded('camera passes.', 4),
            _inc_excluded('Personal expenses such as boutique bar use,', 5),
            _inc_excluded('laundry, and guide tips.', 6),
            _inc_excluded('Optional luxury yacht charter pricing or dynamic', 7),
            _inc_excluded('watersport packages.', 8),
        ],
    )
    return package, itinerary

def build_ga_023(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-023'
    tour_code = 'TRG-GOA-023'
    title = 'TRAGUIN Premium Goa Tour Package — Fun & Sun Coastal Delight'
    duration = '05 Nights / 06 Days'
    slug = 'ga-023-fun-sun-coastal-delight'
    itin_slug = 'ga-023-fun-sun-coastal-delight-itinerary'
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
            _ph('Serial code GA-023 | TRAGUIN tour code TRG-GOA-023', 1),
            _ph('State / Country: Goa / India | Category: Premium Family', 2),
            _ph('Destinations: North Goa • South Goa', 3),
            _ph('Ideal for: Family Tours, Multi- generational Leisure & Coastal Explorers', 4),
            _ph('Best season: October to May (Pleasant Beach Weather)', 5),
            _ph('Starting price: On Request (Bespoke Luxury Family Tier)', 6),
            _ph('Vehicle / Meals: Private Luxury', 7),
            _ph('TRAGUIN Signature Experience: Private walking exploration of Fontainhas Latin Quarter with an', 8),
            _ph('Curated by TRAGUIN Experts: Custom routing designed to avoid heavy traffic times, maximizing your', 9),
            _ph('Premium Handpicked Hotels: Resort properties chosen for their top-tier family safety ratings, premium', 10),
            _ph('Luxury Transportation: Relax in premium vehicles driven by courteous, background-verified professional', 11),
            _ph('Local Markets & Souvenirs: Explore the vibrant local markets to find authentic hand-painted Azulejos ceramic tiles, premium whole Goan cashews, locally distilled feni blends, and intricate sea-shell home decorations. Cafes & Food: Old Panaji and beach alcoves feature historic bakeries serving fresh poee bread, Portuguese egg tarts, traditional fish recheado, and artisanal coconut-infused desserts accompanied by live music.', 12),
            _ph('Hotel Policies: Standard resort check-in begins at 14:00 hours; check-out is at 11:00 hours. Valid', 13)
        ],
        moods=['Family', 'Beach', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Bespoke Luxury Family Tier)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Fun & Sun Coastal Delight',
        overview="PARADISE Welcome to a spectacular coastal retreat designed to perfection by TRAGUIN. Surrender to the magic of the sun-kissed sands and azure waters with our beautifully orchestrated Goa Family Tour. As your professional luxury travel consultants, TRAGUIN has curated a seamless journey that captures the true essence of India's favorite beach paradise. This itinerary transitions effortlessly from the lively energy of legendary northern beaches to the historical elegance of old southern churches, into hidden lush jungle waterfalls. Relax across premium stays, delight your senses with fresh local seafood, and let the magnificent scenic beauty wrap your family in pure warmth, promising unforgettable memories.\n\nTOUR OVERVIEW\nThis bespoke luxury holiday experience provides your family with a flawless blend of dynamic water excursions, golden sun-drenched beaches, classic architectural history, and interactive wildlife discoveries. Travelling in a completely private, air-conditioned premium vehicle accompanied by an experienced, courteous local chauffeur, comfort is guaranteed throughout the trip. Featuring a masterfully coordinated meal plan with deluxe breakfast buffets and signature multi-cuisine dinners, this itinerary exemplifies the finest premium Goa experience. Every moment contains the signature touch of TRAGUIN curated experiences, assuring personalized assistance and VIP hospitality at every milestone. WHY BOOK THE BEST GOA TOUR PACKAGE? When considering a Luxury Goa Holiday, travelers expect an impeccable combination of sensory immersion, luxury accommodations, and local experiences. Goa continues to stand as an premier global retreat. Offering iconic attractions ranging from the magnificent, cascades of Dudhsagar Waterfalls to the imposing ramparts of Fort Aguada, Goa sightseeing remains unmatched in variety and appeal. For couples and modern families finalizing a high-end Goa Honeymoon Package or Goa Family Tour, the coastal state unveils an array of popular Instagram locations. Take a stroll under the vibrant, multi-colored lanes of Fontainhas Latin Quarter, map the expansive viewpoints over the Arabian Sea, or snap unforgettable frames along Candolim's clean golden sands. From pulse-racing watersports at Calangute to sensory tours within spice farms and premium shopping in Panaji boutiques, our custom TRAGUIN Goa Packages provide curated exclusive experiences during the best time to visit Goa.",
        seo_title='GA-023 | Goa | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Goa package (GA-023 / TRG-GOA-023): North Goa • South Goa.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA – WELCOME TO THE COASTAL PARADISE', 1),
            _ih('Day 02: NORTH GOA EXPLORATION', 2),
            _ih('Day 03: SOUTH GOA HERITAGE & FONTAINHAS LATIN QUARTER', 3),
            _ih('Day 04: DUDHSAGAR WATERFALLS & SPICE PLANTATION EXCURSION', 4),
            _ih('Day 05: LEISURE & RECREATION IN SOUTH GOA', 5),
            _ih('Day 06: GOA DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA – WELCOME TO THE COASTAL PARADISE',
                (
                    'SUN-KISSED AIRS & PREMIUM RIVERSIDE CHECKS Your exceptional premium Goa experience begins as you step out of Manohar International Airport (MOPA) or Dabolim Airport. A dedicated private luxury vehicle waits to transport you in total comfort. Travel through scenic palm-lined roads to check into your handpicked luxury resort property. Unwind with premium welcome amenities tailored for your family. As the sun begins to set, stroll along the powdery sands of the nearest beach, or enjoy an optional luxury sunset catamaran cruise arranged by our experts to capture your first'
                ),
                [
                    'photography points: against the horizon.',
                    'Sightseeing Included: Scenic orientation drive, beachside sunset stroll.',
                    'Optional Activities: Private luxury yacht hire or sunset catamaran experience with champagne.',
                    'Evening Experience: Exquisite beachfront welcome dinner curated by TRAGUIN experts.',
                    'Overnight Stay: North Goa Beach Resort (Premium / Luxury Category)',
                    'Meals Included: Welcome Drink & Gourmet Buffet Dinner',
                ],
            ),            _day(
                2,
                'NORTH GOA EXPLORATION',
                (
                    'ICONIC ATTRACTIONS, VIBRANT BAZAARS & SUNSET FORTS Savor a lavish morning breakfast before heading out to uncover the historic marvels and breathtaking landscapes of North Goa. Tour the 17th-century Fort Aguada, where the historic lighthouse stands as a landmark overlooking the boundless sea. Explore the famous crescent shores of Sinquerim, Candolim, and Calangute. Spend the late afternoon enjoying traditional Goan fish curry, followed by local shopping for handmade clay pottery, beachwear, and beautiful shell souvenirs at a bustling beachside market.'
                ),
                [
                    'Sightseeing Included: Fort Aguada, Sinquerim Beach, Calangute Coast, Anjuna Viewpoint.',
                    'Optional Activities: Thrilling parasailing and jet skiing at Calangute beach with certified operators.',
                    'Evening Experience: Live acoustic music lounge dinner overlooking the crashing waves.',
                    'Overnight Stay: North Goa Beach Resort (Premium / Luxury Category)',
                    'Meals Included: Premium Breakfast & Luxury Dinner',
                ],
            ),            _day(
                3,
                'SOUTH GOA HERITAGE & FONTAINHAS LATIN QUARTER',
                (
                    "PORTUGUESE SPLENDOR, SACRED CATHEDRALS & VIBRANT STREETS Today, delve deep into the rich cultural tapestry and heritage of South Goa. Explore the UNESCO World Heritage-listed Basilica of Bom Jesus, which houses the sacred remains of St. Francis Xavier, and marvel at the Se Cathedral's magnificent architecture. Next, travel to Fontainhas, the old Latin Quarter of Panaji. This highly popular Instagram location features bright pastel-yellow and blue heritage houses with ornate wooden balconies, offering fantastic family photo backdrops."
                ),
                [
                    'Sightseeing Included: Basilica of Bom Jesus, Se Cathedral, Fontainhas Heritage Walk, Panaji Promenade.',
                    'Food Suggestions: Lunch at a heritage Indo-Portuguese mansion serving authentic Bebinca and vindaloo.',
                    'Overnight Stay: South Goa / Central Premium Luxury Resort',
                    'Meals Included: Premium Breakfast & Elite Dinner',
                ],
            ),            _day(
                4,
                'DUDHSAGAR WATERFALLS & SPICE PLANTATION EXCURSION',
                (
                    "JUNGLE JEEPS, MAJESTIC WATERFALLS & AROMATIC SPICE TOURS Embark on a thrilling morning family adventure to the spectacular Dudhsagar Waterfalls, one of India's tallest and most iconic attractions. Ride in an open-top 4x4 jungle jeep through the lush canopies of Bhagwan Mahavir Wildlife Sanctuary. Witness the breathtaking sight of milk-white waters cascading down the sheer mountain cliffside. Afterward, enjoy a traditional welcome at a nearby tropical spice plantation. Savor an authentic Goan buffet lunch served on banana leaves, followed by an educational walk among exotic spices."
                ),
                [
                    'Sightseeing Included: Dudhsagar Jeep Safari, Natural pool swimming, Tropical Spice Plantation walk.',
                    'Optional Activities: Elephant bathing and interactive feeding experience at the plantation.',
                    'Overnight Stay: South Goa / Beachfront Luxury Resort',
                    'Meals Included: Breakfast, Traditional Plantation Lunch & Dinner',
                ],
            ),            _day(
                5,
                'LEISURE & RECREATION IN SOUTH GOA',
                (
                    "SERENE SOUTHERN SHORES & GOLDEN MEMORIES Enjoy a completely relaxed day at your own pace to appreciate the tranquil beauty of South Goa. Sleep in late or take part in an early morning yoga session on the beach. Spend the afternoon swimming in the resort's infinity pool or relaxing on the quiet sands of Palolem or Mobor beach. In the evening, gather on the beach for a special family sunset celebration to toast to a truly unforgettable vacation."
                ),
                [
                    'Sightseeing Included: Palolem or Colva Beach frontages, Resort recreational zones.',
                    'Evening Experience: Grand farewell seafood buffet dinner with premium seaside seating.',
                    'Overnight Stay: South Goa Beachfront Luxury Resort',
                    'Meals Included: Premium Breakfast & Farewell Dinner',
                ],
            ),            _day(
                6,
                'GOA DEPARTURE',
                (
                    'TRANSFERS OUT WITH CHERISHED MOMENTS Indulge in a final lavish breakfast at your premium resort hotel. Pack your belongings as your private luxury vehicle prepares for a comfortable door-to-door highway transfer back to MOPA or Dabolim Airport for your flight home. Return home carrying a heart filled with coastal sun, shared smiles, and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury airport transfer drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'DoubleTree by Hilton / Novotel Candolim | Kenilworth Resort / Heritage Village Resort',
                'North Goa (2 Nights) / South Goa (3 Nights)',
                '05 Nights',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: DoubleTree by Hilton / Novotel Candolim (North Goa (2 Nights)) | Kenilworth Resort / Heritage Village Resort (South Goa (3 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Hard Rock Hotel / Vivanta Goa Candolim | Caravela Beach Resort / Radisson Blu',
                'North Goa (2 Nights) / South Goa (3 Nights)',
                '05 Nights',
                'Premium',
                'Premium Room',
                'MAPAI Premium Tiers',
                4,
                2,
                description='OPTION 02 – PREMIUM: Hard Rock Hotel / Vivanta Goa Candolim (North Goa (2 Nights)) | Caravela Beach Resort / Radisson Blu (South Goa (3 Nights)) | MAPAI Premium Tiers',
            ),
            _hotel(
                'The Leela Goa (Villas) / W Goa (Vagator) | Taj Exotica Resort & Spa / ITC Grand Goa',
                'North Goa (2 Nights) / South Goa (3 Nights)',
                '05 Nights',
                'Luxury',
                'Luxury Villa / Suite',
                'MAPAI Custom Club Class',
                5,
                3,
                description='OPTION 03 – LUXURY: The Leela Goa (Villas) / W Goa (Vagator) (North Goa (2 Nights)) | Taj Exotica Resort & Spa / ITC Grand Goa (South Goa (3 Nights)) | MAPAI Custom Club Class',
            ),
            _hotel(
                'Taj Fort Aguada Resort (Pres. Suite) | The Leela Goa (The Club Suites)',
                'North Goa (2 Nights) / South Goa (3 Nights)',
                '05 Nights',
                'Ultra Luxury',
                'Presidential / Club Suite',
                'Bespoke Gourmet Curated Meal Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Taj Fort Aguada Resort (Pres. Suite) (North Goa (2 Nights)) | The Leela Goa (The Club Suites) (South Goa (3 Nights)) | Bespoke Gourmet Curated Meal Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Domestic or International airfares and train', 1),
            _inc_excluded('booking fees.', 2),
            _inc_excluded('Optional watersports, scuba diving, and deep-', 3),
            _inc_excluded('sea angling expenses.', 4),
            _inc_excluded('Personal incidentals such as room service,', 5),
            _inc_excluded('laundry, premium alcohol, and tips.', 6),
            _inc_excluded('Individual monument entry tickets, specialized', 7),
            _inc_excluded('camera permits, and localized guides.', 8),
        ],
    )
    return package, itinerary

def build_ga_024(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-024'
    tour_code = 'TRG-GOA-024'
    title = 'TRAGUIN Premium Goa Tour Package — Dudhsagar Waterfalls & Spice Plantation Family Escape'
    duration = '06 Nights / 07 Days'
    slug = 'ga-024-dudhsagar-spice-plantation-family'
    itin_slug = 'ga-024-dudhsagar-spice-plantation-family-itinerary'
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
            _ph('Serial code GA-024 | TRAGUIN tour code TRG-GOA-024', 1),
            _ph('State / Country: Goa / India | Category: Premium Family', 2),
            _ph('Destinations: North Goa • South Goa', 3),
            _ph('Ideal for: Families, Leisure Seekers & Nature Lovers', 4),
            _ph('Best season: October to April (Pleasant) / June to September (Lush Monsoon)', 5),
            _ph('Starting price: On Request (Premium Customized)', 6),
            _ph('Vehicle / Meals: Private Luxury AC', 7),
            _ph('TRAGUIN Signature Experience: A private family table reservation at an authentic heritage Portuguese', 8),
            _ph('Curated by TRAGUIN Experts: An optimized itinerary designed to avoid crowded hours at Dudhsagar', 9),
            _ph('Premium Handpicked Hotels: Properties chosen specifically for their excellent family safety standards,', 10),
            _ph('Personalized Assistance: Professional, well-trained drivers who know the best local dining spots and', 11),
            _ph('Local Markets & Souvenirs: Visit the vibrant Anjuna Flea Market or the Panjim arcade shops to look for premium Goan cashews, authentic local spices, hand-painted Azulejos ceramic tiles, and beautiful handmade shell jewelry. Cafes & Food: Enjoy refreshing local drinks, try authentic Goan fish curry rice, or treat the family to Bebinca —the rich, traditional multi-layered Goan dessert—at our handpicked beachside cafes.', 12),
            _ph('Hotel Policies: Standard check-in begins at 14:00 hrs, and check-out is at 11:00 hrs. Valid Government-', 13)
        ],
        moods=['Family', 'Beach', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Customized)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Dudhsagar Waterfalls & Spice Plantation Family Escape',
        overview="ESCAPE Welcome Note: Welcome to a beautifully planned tropical retreat managed with the highest attention to detail by TRAGUIN. This exclusive Goa Family Tour is expertly designed to combine the legendary golden coastlines of India's beach capital with its hidden, majestic inland treasures. As your professional travel consultants, we invite you to look past the usual tourist hotspots and step into a world of curated experiences, where the milky cascades of Dudhsagar and the sweet-scented paths of traditional spice orchards await. Let us elevate your vacation into a true luxury holiday filled with premium stays, handpicked hotels, and exclusive experiences designed to leave your family with unforgettable memories.\n\nTOUR OVERVIEW\nOur customized 06 Nights / 07 Days itinerary offers an exceptional mix of relaxation and immersive exploration. Travelling across Goa in a spacious, chauffeured premium private vehicle, your family will enjoy effortless transitions between tranquil coastal beaches, historic Latin Quarters, and deep tropical forests. Featuring a high-end MAPAI meal plan (lavish breakfasts and fine-course dinners), this holiday route is curated to satisfy both the casual beachgoer and the heritage enthusiast. Every detail of this itinerary is backed by the signature TRAGUIN curated experience note, offering your family priority entry privileges, selected local interactions, and expert, around-the-clock ground assistance.\n\nWHY CHOOSE THE BEST GOA TOUR PACKAGE?\nWhen travelers search for a Luxury Goa Holiday, they look for an itinerary that balances upscale beachfront living with authentic cultural insights. Goa is far more than just its famous shores; it is a rich mix of UNESCO World Heritage Portuguese architecture, lively local markets, and incredible ecosystems. From the dramatic water cascades of Dudhsagar Waterfalls—a top tourist place in Goa for nature enthusiasts—to the aromatic organic farms of Ponda, the state offers beautiful diversity for a rich family vacation. For families and couples booking a specialized Goa Honeymoon Package or an multi-generation Goa Family Tour, the region offers incredibly photogenic, popular Instagram locations such as the colorful Fontainhas streets, the historic Cabo de Rama cliffs, and the peaceful sunset cruises along the Mandovi River. Whether you are looking for local handicraft shopping, thrilling water sports, or a quiet walk through old spice plantations, our signature TRAGUIN Goa Packages ensure premium stays, handpicked hotels, and immersive experiences that make any season the best time to visit Goa.",
        seo_title='GA-024 | Goa | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Goa package (GA-024 / TRG-GOA-024): North Goa • South Goa.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA - WELCOME TO THE EMERALD LAND', 1),
            _ih('Day 02: NORTH GOA BEACHES & SUN-KISSED RECREATION', 2),
            _ih('Day 03: SOUTH GOA HERITAGE & MONUMENTAL HISTORY', 3),
            _ih('Day 04: THE MAJESTIC DUDHSAGAR WATERFALL EXCURSION', 4),
            _ih('Day 05: EXOTIC SPICE PLANTATION TOUR & ELEPHANT INTERACTION', 5),
            _ih('Day 06: TRANQUIL SOUTH GOA BEACH RESORT LEISURE', 6),
            _ih('Day 07: DEPARTURE FROM GOA - CHERISHING MAGICAL MOMMENTS', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA - WELCOME TO THE EMERALD LAND',
                (
                    'EXCLUSIVE ARRIVAL & TROPICAL BEACH BREEZE Your premium Goa experience starts the moment you step out of Manohar International Airport (MOPA) or Dabolim Airport. Your private chauffeured luxury transport will be waiting to drive you to your high-end beachfront resort. After a smooth check-in, unpack and relax in your premium room. In the late afternoon, take a leisurely family stroll along the soft sands, capturing beautiful sunset photos over the Arabian Sea.'
                ),
                [
                    'Sightseeing Included: Resort beachfront access, evening coastal sunset walk.',
                    'Evening Experience: A private welcome dinner at a beachfront restaurant with live acoustic music.',
                    'Overnight Stay: North Goa (Premium / Luxury Beachfront Resort)',
                    'Meals Included: Welcome Refreshment & Luxury Buffet Dinner',
                ],
            ),            _day(
                2,
                'NORTH GOA BEACHES & SUN-KISSED RECREATION',
                (
                    'FORTRESSES, GOLDEN SHORES & COASTAL LIFE Enjoy a rich breakfast before heading out to discover the historic charms of North Goa sightseeing. Explore the 17th-century rock bastions of Fort Aguada, where you can take beautiful photos of the old lighthouse and the wide sea below. Spend your afternoon visiting the popular beaches of Candolim, Calangute, and Baga. For families seeking a bit of adventure, exciting optional watersports can be arranged directly on-site.'
                ),
                [
                    'Sightseeing Included: Fort Aguada, Candolim Beach, Calangute Beach, Baga Beach viewpoint.',
                    'Optional Activities: Parasailing, jet-skiing, and banana boat rides with certified safety operators.',
                    'Overnight Stay: North Goa (Premium / Luxury Beachfront Resort)',
                    'Meals Included: Premium Breakfast & Fine-Course Dinner',
                ],
            ),            _day(
                3,
                'SOUTH GOA HERITAGE & MONUMENTAL HISTORY',
                (
                    'UNESCO CHURCHES, LATIN QUARTERS & MANDOVI SUNSET CRUISE Today, travel south to uncover the rich history of Old Goa. Tour the magnificent Basilica of Bom Jesus, a UNESCO World Heritage site that holds the sacred remains of St. Francis Xavier. Walk through the stunning Se Cathedral before heading to Fontainhas—the historic Latin Quarter of Panaji. Its brightly colored houses and elegant Portuguese balconies make it one of the most popular Instagram locations in India. Finish your afternoon with a relaxing, private sunset boat cruise along the scenic Mandovi River. dances.'
                ),
                [
                    'Sightseeing Included: Basilica of Bom Jesus, Se Cathedral, Fontainhas Latin Quarter walk, Mandovi River cruise.',
                    'Evening Experience: Reserved lower-deck or upper-deck seating on a premium river cruise with local folk',
                    'Overnight Stay: North / South Goa Luxury Resort',
                    'Meals Included: Premium Breakfast & Authentic Indo-Portuguese Dinner',
                ],
            ),            _day(
                4,
                'THE MAJESTIC DUDHSAGAR WATERFALL EXCURSION',
                (
                    'THE MILKY CASCADE, JUNGLE JEEP SAFARI & NATURAL WONDERS Wake up early for the highlight of your tour: the great Dudhsagar Waterfalls excursion. Head to the edge of the Bhagwan Mahavir Wildlife Sanctuary, where you will hop into an authorized open-top 4x4 jungle jeep. Travel through lush mountain streams and dense tropical forests until the spectacular four-tiered, white-water falls come into view. It is a truly breathtaking landscape. Enjoy a refreshing swim in the safe, natural pool at the base of the falls under the watchful eye of local guides.'
                ),
                [
                    'Sightseeing Included: Bhagwan Mahavir Sanctuary forest trek, Dudhsagar Waterfall base pool access.',
                    'Optional Activities: Professional landscape photography session amidst the forest cascades.',
                    'Overnight Stay: South Goa Selected Luxury Eco-Resort / Beach Resort',
                    'Meals Included: Premium Breakfast & Hearty Buffet Dinner',
                ],
            ),            _day(
                5,
                'EXOTIC SPICE PLANTATION TOUR & ELEPHANT INTERACTION',
                (
                    'AROMATIC PATHS, TRADITIONAL BUFFET & CULTURAL IMMERSION Spend a wonderful day exploring an organic spice plantation in Ponda. Receive a warm traditional welcome with a fresh flower garland and a refreshing herbal tea. A knowledgeable local guide will lead you on a walk through the plantation, pointing out how black pepper, cardamom, cinnamon, and vanilla are grown naturally. Afterward, enjoy a delicious traditional Goan buffet lunch served on authentic banana leaves. In the afternoon, your family can participate in an optional, memorable elephant feeding and washing experience.'
                ),
                [
                    'Sightseeing Included: Guided spice farm walking tour, traditional organic buffet pavilion.',
                    'Evening Experience: Feni distillation demonstration and a sampling of fresh local cashew spirits.',
                    'Overnight Stay: South Goa Premium Luxury Resort',
                    'Meals Included: Breakfast, Traditional Plantation Lunch & Luxury Resort Dinner',
                ],
            ),            _day(
                6,
                'TRANQUIL SOUTH GOA BEACH RESORT LEISURE',
                (
                    "WHITE SANDS, CHILL CAFES & FAMILY BONDING TIME Dedicate this day entirely to relaxation and sweet family moments. South Goa's beaches, like Palolem and Varca, are famous for their clean white sands, scenic beauty, and peaceful atmosphere. Relax by the resort's luxury pool, read a book under a shady palm tree, or visit a nearby beachside café to sample delicious local snacks."
                ),
                [
                    'Sightseeing Included: Varca or Palolem beach leisure walks, premium resort amenities.',
                    'Optional Activities: An upscale Ayurvedic full-body spa treatment at the resort wellness center.',
                    'Overnight Stay: South Goa Premium Luxury Resort',
                    "Meals Included: Premium Breakfast & Farewell Chef's Special Dinner",
                ],
            ),            _day(
                7,
                'DEPARTURE FROM GOA - CHERISHING MAGICAL MOMMENTS',
                (
                    'SAYING FAREWELL TO THE SUNNY COASTLINE Enjoy one last delicious breakfast at the resort while taking in views of the pool and ocean. Pack your bags and meet your private chauffeur, who will provide a comfortable ride back to the airport or train station for your journey home. You will return with a heart full of joy and unforgettable memories designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door departure drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Dona Sylvia / Lemon Tree Amarante | Heritage Village Resort & Spa / similar',
                'North Goa (3 Nights) / South Goa (3 Nights)',
                '06 Nights',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Novotel Dona Sylvia / Lemon Tree Amarante (North Goa (3 Nights)) | Heritage Village Resort & Spa / similar (South Goa (3 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Hard Rock Hotel / DoubleTree by Hilton | Caravela Beach Resort / Kenilworth Resort',
                'North Goa (3 Nights) / South Goa (3 Nights)',
                '06 Nights',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Hard Rock Hotel / DoubleTree by Hilton (North Goa (3 Nights)) | Caravela Beach Resort / Kenilworth Resort (South Goa (3 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Taj Holiday Village / W Goa (Wonderful Room) | The Leela Goa (Lagoon Terrace) / Taj Exotica',
                'North Goa (3 Nights) / South Goa (3 Nights)',
                '06 Nights',
                'Luxury',
                'Luxury Suite',
                'MAPAI + Premium Amenities',
                5,
                3,
                description='OPTION 03 – LUXURY: Taj Holiday Village / W Goa (Wonderful Room) (North Goa (3 Nights)) | The Leela Goa (Lagoon Terrace) / Taj Exotica (South Goa (3 Nights)) | MAPAI + Premium Amenities',
            ),
            _hotel(
                'Taj Fort Aguada (Premium Sea View Suite) | The St. Regis Goa Resort (Luxury Private Villa)',
                'North Goa (3 Nights) / South Goa (3 Nights)',
                '06 Nights',
                'Ultra Luxury',
                'Luxury Private Villa',
                'Bespoke Gourmet Custom Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Taj Fort Aguada (Premium Sea View Suite) (North Goa (3 Nights)) | The St. Regis Goa Resort (Luxury Private Villa) (South Goa (3 Nights)) | Bespoke Gourmet Custom Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Airfare, domestic flight charges, or long-distance', 1),
            _inc_excluded('train tickets.', 2),
            _inc_excluded('On-beach water sports fees, scuba diving, or', 3),
            _inc_excluded('para-sailing charges.', 4),
            _inc_excluded('Personal items such as laundry, phone calls,', 5),
            _inc_excluded('premium beverages, and tips.', 6),
            _inc_excluded('Optional activities like elephant rides or', 7),
            _inc_excluded('entry tickets to night clubs.', 8),
        ],
    )
    return package, itinerary

def build_ga_025(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'GA-025'
    tour_code = 'TRG-GOA-025'
    title = 'TRAGUIN Ultimate Goa Panorama — Best Goa Tour Package'
    duration = '07 Nights / 08 Days'
    slug = 'ga-025-ultimate-goa-panorama'
    itin_slug = 'ga-025-ultimate-goa-panorama-itinerary'
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
            _ph('Serial code GA-025 | TRAGUIN tour code TRG-GOA-025', 1),
            _ph('State / Country: Goa / India | Category: Ultimate Goa', 2),
            _ph('Destinations: North Goa • South Goa', 3),
            _ph('Ideal for: Premium Family', 4),
            _ph('Best season: October to May (Pleasant Beach Weather & Sunsets)', 5),
            _ph('Starting price: On Request (Premium Bespoke Package)', 6),
            _ph('Vehicle / Meals: Private Luxury AC Vehicle / CP or MAPAI', 7),
            _ph('TRAGUIN Signature Experience: Private guided heritage walking exploration through Fontainhas with an', 8),
            _ph('Curated by TRAGUIN Experts: Perfect smooth transition routing from vibrant North Goa to tranquil South Goa', 9),
            _ph('Personalized Assistance: Dedicated chauffeur who knows the absolute finest, secluded sunset photography', 10),
            _ph('Premium Handpicked Hotels: Resorts selected strictly based on high safety parameters, excellent family', 11),
            _ph("Local Markets & Souvenirs: Explore the vibrant Anjuna Flea Market or the lively Saturday Night Market in Arpora. Don't forget to pick up authentic Goan cashews, hand-painted Portuguese Azulejos tiles, traditional terracotta pottery, feni bottles, and organic local spices. Cafes & Food: Indulge your family with authentic Goan delicacies like Fish Curry Rice, Chicken Xacuti, and the multi-layered traditional dessert, Bebinca. Visit cozy beach shacks or modern heritage bistros in Panjim for a fantastic culinary experience.", 12),
            _ph('Hotel Policies: Standard resort check-in is at 14:00 hrs and check-out is at 11:00 hrs. Valid government-issued', 13)
        ],
        moods=['Family', 'Beach', 'Luxury', 'Romantic'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Bespoke Package)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Best Goa Tour Package',
        overview='Welcome to the sun-soaked paradise of India, captured beautifully in a bespoke luxury itinerary designed exclusively by TRAGUIN. This exclusive "Ultimate Goa Panorama" represents the absolute pinnacle of a Luxury Goa Holiday, seamlessly weaving together the sparkling coastline of North Goa and the tranquil colonial romance of South Goa. As your professional travel consultants, TRAGUIN transforms a simple vacation into an unforgettable escape filled with premium stays, breathtaking landscapes, and elite privileges. Whether you are traveling as a joyous multi-generational group for a Goa Family Tour or celebrating a glamorous Goa Honeymoon Package, let us guide you into a world of curated experiences, golden sands, and soulful Portuguese heritage.\n\nTOUR OVERVIEW\nYour upcoming luxury holiday is meticulously planned to showcase Goa beyond its famous shores, featuring an optimal mix of relaxation, heritage exploration, and light coastal adventure. Travelling in a dedicated premium air- conditioned vehicle with a professional chauffeur, your family will experience absolute privacy and comfort. With a highly balanced meal plan featuring daily gourmet breakfasts and specialized multi-cuisine dinners at premium handpicked hotels, every detail is engineered to ensure absolute perfection. This signature route incorporates the definitive TRAGUIN curated experience note, providing seamless private yacht transfers, VIP entries to major heritage architectural complexes, and 24/7 dedicated local expert support. WHY VISIT GOA? DISCOVER TOP TOURIST PLACES IN GOA Goa is much more than a destination; it is a lifestyle that seamlessly fuses relaxed susegad living with high-octane luxury. A Luxury Goa Holiday is highly sought after by discerning travelers worldwide because of the destination’s unique cultural tapestry, combining vibrant Portuguese history with world-class beach resorts. For those planning a definitive Goa Family Tour or a romantic Goa Honeymoon Package, the state unfolds into a paradise of scenic beauty, lush spice plantations, and grand architecture. When you choose our premium TRAGUIN Goa Packages, you gain immediate, curated access to the most famous attractions and highly popular Instagram locations. From the historic fortifications of Aguada and Chapora to the majestic cascading white waters of Dudhsagar Waterfalls—one of the absolute top tourist places in Goa—your camera will capture endless beauty. Dive into the most searched experiences, such as private sunset Mandovi River cruises, exploring the pastel-colored alleys of the Fontainhas Latin Quarter, experiencing thrilling water sports, and enjoying beachside candle-lit dining. The best time to visit Goa spans from autumn to spring, when the coastal breeze is delightful and the sea is calm, making it the perfect setting for a Premium Goa Experience filled with exclusive experiences.',
        seo_title='GA-025 | TRAGUIN Ultimate Goa Panorama | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Goa package (GA-025 / TRG-GOA-025): North Goa • South Goa.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GOA – WELCOME TO THE SUN-KISSSED PARADISE', 1),
            _ih('Day 02: NORTH GOA SIGHTSEEING & FORTRESS LEGACIES', 2),
            _ih('Day 03: SOUTH GOA HERITAGE & SPIRITUAL GRANDEUR', 3),
            _ih('Day 04: FONTAINHAS LATIN QUARTER & PANJIM LIFESTYLE', 4),
            _ih('Day 05: EXCURSION TO DUDHSAGAR WATERFALLS & SPICE PLANTATION', 5),
            _ih('Day 06: SOUTHERN BEACH BLISS & PALOLEM ESCAPE', 6),
            _ih('Day 07: LEISURE DAY, SPA INDULGENCE & SUNSET CASINO', 7),
            _ih('Day 08: DEPARTURE FROM GOA', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GOA – WELCOME TO THE SUN-KISSSED PARADISE',
                (
                    'TOUCHDOWN, LUXURY RIVERSIDE/BEACH RESORT CHECK-IN & EVENING AT LEISURE Your ultimate premium Goa experience begins the moment you step off your flight or train. Your private luxury transport and professional chauffeur will greet you with a warm welcome and transfer you smoothly to your premium beachside resort. Soak in the breathtaking landscapes of swaying coconut palms along the scenic routes. Spend your afternoon unpacking and unwinding in your luxury suite. In the evening, take a romantic walk along the beach to watch a brilliant crimson sunset over the Arabian Sea.'
                ),
                [
                    'Sightseeing Included: Private luxury arrival transfer, Beach walk, Resort orientation.',
                    'Evening Experience: Welcome drink and beachfront family dinner with a menu curated by TRAGUIN experts.',
                    'Overnight Stay: North Goa / South Goa (Premium Luxury Resort Stay)',
                    'Meals Included: Welcome Amenities & Luxury Dinner',
                ],
            ),            _day(
                2,
                'NORTH GOA SIGHTSEEING & FORTRESS LEGACIES',
                (
                    'EXPLORING HISTORIC AGUADA FORT, ICONIC LANDMARKS & GOLDEN SHORES Indulge in a lavish buffet breakfast before heading out for a comprehensive North Goa sightseeing tour. Your first stop is the magnificent 17th-century Fort Aguada, where the historic Portuguese lighthouse offers a panoramic view of the vast ocean—a perfect photography point. Continue along the scenic coastal road to explore the legendary Chapora Fort, famously known from Bollywood cinema. In the afternoon, explore the lively, golden sands of Calangute and Baga beaches, where your family can choose from a variety of exciting water sports.'
                ),
                [
                    'Sightseeing Included: Fort Aguada, Chapora Fort, Baga Beach, Calangute Beach, Sinquerim Viewpoint.',
                    'Optional Activities: Premium jet-skiing, parasailing, and speed-boat rides with certified instructors.',
                    'Overnight Stay: Premium Handpicked Beach Resort in Goa',
                    'Meals Included: Premium Breakfast & Specialized Dinner',
                ],
            ),            _day(
                3,
                'SOUTH GOA HERITAGE & SPIRITUAL GRANDEUR',
                (
                    'CATHEDRALS OF OLD GOA & THE PRIVATE SUNSET MANDOVI RIVER CRUISE Today, delve deep into the rich cultural history of South Goa. After a premium breakfast, visit Old Goa to see the stunning Basilica of Bom Jesus, a UNESCO World Heritage site that holds the sacred mortal remains of St. Francis Xavier. Marvel at the grand interior of Se Cathedral, the largest church in Asia. Later, visit the beautiful Mangueshi Temple, nestled amidst serene hills. As the sun begins to set, head to the jetty for an exclusive luxury cruise along the Mandovi River, complete with traditional Goan folk music and dancing.'
                ),
                [
                    'Sightseeing Included: Basilica of Bom Jesus, Se Cathedral, Mangueshi Temple, Mandovi Riverfront.',
                    'Evening Experience: Premium sunset river cruise with live Goan music and panoramic city light views.',
                    'Overnight Stay: Premium Handpicked Beach Resort in Goa',
                    'Meals Included: Premium Breakfast & Multi-Cuisine Dinner',
                ],
            ),            _day(
                4,
                'FONTAINHAS LATIN QUARTER & PANJIM LIFESTYLE',
                (
                    'A JOURNEY THROUGH PORTUGUESE ALLEYS & INSATGRAM SPOTS Following breakfast, explore Fontainhas, the famous Latin Quarter of Panjim. This highly popular Instagram location is famous for its narrow, winding streets lined with brightly colored 18th-century Portuguese villas featuring elegant wrought-iron balconies. Enjoy a guided historical walking tour filled with fascinating emotional storytelling. Afterward, visit the iconic, pristine white Church of Our Lady of the Immaculate Conception before spending your afternoon shopping for beautiful boutique tiles and high-end local souvenirs.'
                ),
                [
                    'Sightseeing Included: Fontainhas Latin Quarter, Panjim Church, Azad Maidan, local arts craft emporium.',
                    'Food Suggestions: Stop by an old Portuguese bakery for traditional pasteis de nata and fresh Goan poee.',
                    'Overnight Stay: Premium Handpicked Beach Resort in Goa',
                    'Meals Included: Premium Breakfast & Gourmet Dinner',
                ],
            ),            _day(
                5,
                'EXCURSION TO DUDHSAGAR WATERFALLS & SPICE PLANTATION',
                (
                    'CASCADING WHITE WATERS & AN AUTHENTIC JUNGLE BUFFET Set off early for an unforgettable adventure to the spectacular Dudhsagar Waterfalls. Board an open-top 4x4 jungle jeep that splashes through forest streams to reach the base of the massive four-tiered waterfall. Feel the refreshing, cool mist on your face and capture stunning photographs of this natural wonder. Afterward, visit a lush, aromatic spice plantation. Enjoy a traditional welcome, take a guided walk to learn about exotic spices, and sit down for a delicious traditional Goan lunch served on banana leaves.'
                ),
                [
                    'Sightseeing Included: Dudhsagar Waterfall Jeep Safari, Spice Plantation Tour, Bhagwan Mahavir Sanctuary.',
                    'Optional Activities: A refreshing swim in the natural pool at the base of the waterfall (life jackets provided).',
                    'Overnight Stay: Premium Handpicked Beach Resort in Goa',
                    'Meals Included: Breakfast, Traditional Spice Plantation Buffet Lunch & Resort Dinner',
                ],
            ),            _day(
                6,
                'SOUTHERN BEACH BLISS & PALOLEM ESCAPE',
                (
                    'UNTOUCHED WHITE SANDS & PRIVATE DOLPHIN SPOTTING Today is dedicated to the pristine, white-sand beauty of South Goa’s finest beaches. Journey down south to Palolem Beach and Agonda Beach, known for their calm, crescent-shaped bays and peaceful atmosphere. Board a traditional private boat for an early afternoon cruise to spot wild dolphins playing in the ocean. Spend the rest of your day relaxing on sun loungers, listening to the gentle waves, and enjoying the serene beauty of the coast.'
                ),
                [
                    'Sightseeing Included: Palolem Beach, Agonda Beach, Butterfly Beach island overlook.',
                    'Evening Experience: A relaxed family evening at an upscale beachside shack with live acoustic music.',
                    'Overnight Stay: Premium Handpicked Beach Resort in Goa',
                    'Meals Included: Premium Breakfast & Seafood / Vegetarian Specialty Dinner',
                ],
            ),            _day(
                7,
                'LEISURE DAY, SPA INDULGENCE & SUNSET CASINO',
                (
                    "REJUVENATION & GLAMOROUS NIGHTLIFE EXPERIENCE Enjoy a completely relaxed morning at your luxury resort. Sleep in late, take a dip in the sparkling swimming pool, or treat yourself to a soothing Ayurvedic full-body massage at the resort's premium spa. In the late afternoon, your private chauffeur will take you to Panjim, where you will board a premium offshore live casino vessel on the Mandovi River. Enjoy an exciting evening of games, international buffet dining, and live entertainment."
                ),
                [
                    'Sightseeing Included: Resort luxury facilities, Premium Panjim gaming dock area.',
                    'Optional Activities: Luxury Ayurvedic or Swedish couple spa therapies at the resort wellness center.',
                    'Overnight Stay: Premium Handpicked Beach Resort in Goa',
                    'Meals Included: Premium Breakfast & Farewell Dinner Cruise/Casino Buffet',
                ],
            ),            _day(
                8,
                'DEPARTURE FROM GOA',
                (
                    'FOND FAREWELL TO THE EMERALD COAST – SWEET UNFORGETTABLE MEMORIES Enjoy a final, delicious breakfast overlooking the ocean. Pack your bags and board your private luxury vehicle. Your chauffeur will drive you safely to Goa International Airport (Dabolim or Mopa) or Madgaon Railway Station for your journey home. Return home carrying a heart full of joy, family bonds, and sweet unforgettable memories designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door departure airport/station drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Goa Resort & Spa / Lemon Tree Amarante | Heritage Village Resort / Kenilworth Resort',
                'North Goa (4 Nights) / South Goa (3 Nights)',
                '07 Nights',
                'Deluxe',
                'Superior Garden View Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Novotel Goa Resort & Spa / Lemon Tree Amarante (North Goa (4 Nights)) | Heritage Village Resort / Kenilworth Resort (South Goa (3 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The O Hotel / Hard Rock Hotel Goa / similar | Caravela Beach Resort / Azaya Beach Resort',
                'North Goa (4 Nights) / South Goa (3 Nights)',
                '07 Nights',
                'Premium',
                'Premium Balcony / Pool View Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The O Hotel / Hard Rock Hotel Goa / similar (North Goa (4 Nights)) | Caravela Beach Resort / Azaya Beach Resort (South Goa (3 Nights)) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Taj Holiday Village / Taj Fort Aguada Resort | The Leela Goa / Taj Exotica Resort & Spa',
                'North Goa (4 Nights) / South Goa (3 Nights)',
                '07 Nights',
                'Luxury',
                'Luxury Sea-Facing Cottage / Suite',
                'MAPAI + Premium Amenities',
                5,
                3,
                description='OPTION 03 – LUXURY: Taj Holiday Village / Taj Fort Aguada Resort (North Goa (4 Nights)) | The Leela Goa / Taj Exotica Resort & Spa (South Goa (3 Nights)) | MAPAI + Premium Amenities',
            ),
            _hotel(
                'W Goa (Marvelous Chalet) / JW Marriott Vagator | The St. Regis Goa Resort (Private Pool Villa)',
                'North Goa (4 Nights) / South Goa (3 Nights)',
                '07 Nights',
                'Ultra Luxury',
                'VVIP Custom Sea Front Presidential Villa',
                'Bespoke Signature VIP Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: W Goa (Marvelous Chalet) / JW Marriott Vagator (North Goa (4 Nights)) | The St. Regis Goa Resort (Private Pool Villa) (South Goa (3 Nights)) | Bespoke Signature VIP Plan',
            )
        ],
        inclusions=[
            _inc_excluded('Domestic or International Airfare / Train tickets', 1),
            _inc_excluded('to and from Goa.', 2),
            _inc_excluded('Water sports activity charges, scuba diving, and', 3),
            _inc_excluded('parasailing equipment rentals.', 4),
            _inc_excluded('Monument entry tickets, camera fees, historical', 5),
            _inc_excluded('church guide charges.', 6),
            _inc_excluded('Personal expenses such as laundry, phone calls,', 7),
            _inc_excluded('premium liquor, and tips.', 8),
        ],
    )
    return package, itinerary

GOA_DOMESTIC_BUILDERS = [
    build_ga_001,
    build_ga_002,
    build_ga_003,
    build_ga_004,
    build_ga_005,
    build_ga_006,
    build_ga_007,
    build_ga_008,
    build_ga_009,
    build_ga_010,
    build_ga_012,
    build_ga_013,
    build_ga_014,
    build_ga_015,
    build_ga_016,
    build_ga_017,
    build_ga_018,
    build_ga_019,
    build_ga_020,
    build_ga_021,
    build_ga_022,
    build_ga_023,
    build_ga_024,
    build_ga_025,
]
