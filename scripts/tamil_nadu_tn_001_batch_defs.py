"""Builder functions for TN-002 through TN-005 Tamil Nadu domestic packages."""

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

TAMIL_NADU_SLUG = "tamil-nadu"


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


def build_tn_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TN-001'
    tour_code = 'TRG-TN-001'
    title = 'OOTY • KODAIKANAL LUXURY ESCAPE'
    duration = '05 Nights / 06 Days'
    slug = 'tn-001-ooty-kodaikanal-luxury-escape'
    itin_slug = 'tn-001-ooty-kodaikanal-luxury-escape-itinerary'
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
            _ph('Serial code TN-001 | TRAGUIN tour code TRG-TN-001', 1),
            _ph('State / Country: Tamil Nadu / India | Category: Premium Family Tour', 2),
            _ph('Destinations: Coimbatore •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Luxury Toyota Innova Crysta / Premium MAPAI Plan', 7),
            _ph('TRAGUIN Signature Experience: Private, slow-paced family walk through high-altitude tea trails', 8),
            _ph('Curated by TRAGUIN Experts: Custom pacing designed to allow families complete relaxation, avoiding', 9),
            _ph('Premium Handpicked Hotels: Accommodations chosen strictly for their grand valley viewpoints, safety,', 10),
            _ph("Luxury Transportation: Professional hill drivers trained to prioritize your family's safety and on-road", 11)
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
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='OOTY',
        overview="OOTY • KODAIKANAL LUXURY ESCAPE 05 NIGHTS / 06 DAYS TRAGUIN Premium Luxury Proposal — TN-001 1 Welcome to an unforgettable mountain retreat designed by TRAGUIN. Embark on the finest Tamil Nadu Family Tour that captures the breathtaking landscapes and scenic beauty of the Nilgiris and Palani hills. As your premium travel consultants, TRAGUIN crafts this high-end custom proposal to provide an extraordinary blend of mist-clad mountains, heritage charm, and pristine lakes. Combining the classic colonial allure of Ooty with the tranquil forest paths of Kodaikanal, this journey guarantees premium stays, immersive experiences, and handpicked hotels that create beautiful memories for your entire family.\n\nTOUR OVERVIEW\nThis meticulously planned luxury holiday is structured for an exclusive group or independent family looking for total relaxation and comfort. Your travel route encompasses smooth transfers through the western ghats in a designated private premium AC vehicle managed by an experienced tourist chauffeur. Featuring an extensive map plan including gourmet multi-cuisine breakfasts and lavish dinners, your family will experience pure leisure. Every element features the trademark TRAGUIN curated experience note, ensuring priority check-ins, VIP entry permissions at top sightseeing spots, and bespoke guest-centric coordination.\n\nWHY VISIT TAMIL NADU’S HILL STATIONS?\nWhen exploring the ultimate option for a Luxury Tamil Nadu Holiday, the twin hill stations of Ooty and Kodaikanal remain unmatched in their legacy and pristine natural wonder. Ooty, often referred to as the 'Queen of Hill Stations', offers magnificent iconic attractions like the historic Nilgiri Mountain Railway—a UNESCO world heritage site—and the sprawling Government Botanical Gardens. Kodaikanal, known affectionately as the 'Princess of Hill Stations', charms travelers with its mist-covered pine forests, dramatic cliff edges, and serene star-shaped lake. Whether you choose a romantic Tamil Nadu Honeymoon Package or an enriching Tamil Nadu Family Tour, these hills reveal a treasure trove of popular Instagram locations, from the rolling green meadows of Shooting Point to the dramatic views at Coaker's Walk. Enjoy adventure highlights like high-altitude horse riding, hand-loom garment shopping, or treating your tastebuds to delicious, locally made artisanal chocolates. Our signature TRAGUIN Tamil Nadu Packages provide handpicked hotels and exclusive experiences, confirming that anytime is the best time to visit Tamil Nadu when you travel in absolute luxury.",
        seo_title='TN-001 | OOTY | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Tamil Nadu package (TN-001 / TRG-TN-001): Coimbatore • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=True,
        highlights=[
            _ih('Day 01: ARRIVAL IN COIMBATORE TO OOTY', 1),
            _ih('Day 02: OOTY LOCAL SIGHTSEEING', 2),
            _ih('Day 03: EXCURSION TO COONOOR', 3),
            _ih('Day 04: OOTY TO KODAIKANAL', 4),
            _ih('Day 05: KODAIKANAL LOCAL SIGHTSEEING', 5),
            _ih('Day 06: KODAIKANAL TO COIMBATORE / DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private, slow-paced family walk through high-altitude tea trails', 7),
            _ih('Curated by TRAGUIN Experts: Custom pacing designed to allow families complete relaxation, avoiding', 8),
            _ih('Premium Handpicked Hotels: Accommodations chosen strictly for their grand valley viewpoints, safety,', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN COIMBATORE TO OOTY',
                (
                    'WELCOME TO THE NILGIRIS – JOURNEY TO THE QUEEN OF HILLS Your premium Tamil Nadu experience begins with a personalized reception at Coimbatore Airport or Railway Station. Your private chauffeur-driven luxury transport will guide you along a wonderfully scenic route winding TRAGUIN Premium Luxury Proposal — TN-001 2 past dense forests, vast emerald tea plantations, and sharp mountain curves. As you ascend into the Nilgiris, witness breathtaking landscapes opening up. Arrive at your handpicked luxury resort in Ooty, receive your exclusive welcome amenity kit, and spend a relaxing evening admiring a beautiful mountain sunset from your private balcony.'
                ),
                [
                    'Sightseeing Included: Scenic Nilgiri hairpin drive, panoramic tea estate valley stopovers.',
                    "Evening Experience: Leisurely walk through the resort's private manicured gardens followed by gourmet dining.",
                    'Overnight Stay: Ooty (Premium / Luxury Resort)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'OOTY LOCAL SIGHTSEEING',
                (
                    'COLONIAL LEGACIES, LUSH BOTANY & CALM LAKES Awake to the refreshing mountain air and indulge in a lavish breakfast before beginning a detailed Ooty sightseeing tour. Explore the stunning Government Botanical Gardens, home to a fossil tree trunk estimated to be over 20 million years old. Visit the beautifully terraced Ooty Rose Garden, boasting thousands of unique rose varieties. In the afternoon, head to Ooty Lake for a premium boating session surrounded by tall eucalyptus trees, and enjoy shopping for premium Nilgiri teas and essential oils.'
                ),
                [
                    'Sightseeing Included: Botanical Gardens, Rose Garden, Ooty Lake, Doddabetta Peak (highest point).',
                    'Optional Activities: Bespoke joyride on the historic Nilgiri Mountain Toy Train (subject to ticket availability).',
                    'Overnight Stay: Ooty (Premium / Luxury Resort)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'EXCURSION TO COONOOR',
                (
                    "EMERALD VALLEY VIEWS & VINTAGE TEA ESSENCES Take a short, highly scenic drive to the neighboring paradise of Coonoor. Visit the legendary Dolphin's Nose viewpoint, a magnificent natural rock formation offering an unparalleled view of the Catherine Falls. Explore Sims Park, an exquisite botanical garden showcasing rare species of northern hemisphere plants. Walk hand- in-hand through a premium working tea estate to see how classic tea is processed, and capture gorgeous photos at the popular Instagram locations across the valley. TRAGUIN Premium Luxury Proposal — TN-001 3"
                ),
                [
                    "Sightseeing Included: Sims Park, Dolphin's Nose, Lamb's Rock, Highfield Tea Factory.",
                    'Evening Experience: Private premium tea-tasting masterclass showcasing exotic hill leaf blends.',
                    'Overnight Stay: Ooty (Premium / Luxury Resort)',
                    'Meals Included: Premium Breakfast & Traditional Dinner',
                ],
            ),
            _day(
                4,
                'OOTY TO KODAIKANAL',
                (
                    'CROSSING THE GHATS TO THE PRINCESS OF HILL STATIONS Following a wonderful breakfast, check out and journey towards Kodaikanal. This long, beautiful road trip winds downward through the Nilgiris and ascends the majestic Palani Hills. Arrive late in the afternoon at Kodaikanal, a hill town wrapped completely in soft mist and dense pine woods. Check into your ultra-luxury resort and relax. In the evening, take a quiet stroll around the beautiful Kodaikanal Lake as the stars begin to reflect on its calm waters.'
                ),
                [
                    'Sightseeing Included: Inter-hill valley highway drive, Palani hill viewpoints, Kodaikanal Lake promenade.',
                    'Evening Experience: Intimate lakeside evening walk followed by a warm campfire gathering at the resort.',
                    'Overnight Stay: Kodaikanal (Premium / Luxury Resort)',
                    'Meals Included: Premium Breakfast & Multi-cuisine Buffet Dinner',
                ],
            ),
            _day(
                5,
                'KODAIKANAL LOCAL SIGHTSEEING',
                (
                    "MISTY CLIFFS, PINE FORESTS & EPIC NATURAL WONDERS Dedicate your day to exploring the legendary attractions and scenic beauty of Kodaikanal. Walk along Coaker's Walk, a narrow pedestrian path running along the edge of steep mountain slopes that offers an incredible view of the plains. Explore the mysterious Guna Caves, surrounded by deep, intertwined tree roots, and walk through the historic Pine Forest. Later, enjoy a private sunset boat ride arranged on the star-shaped Kodaikanal Lake."
                ),
                [
                    "Sightseeing Included: Coaker's Walk, Bryant Park, Pillar Rocks, Pine Forest, Guna Caves, Kodaikanal Lake.",
                    'Optional Activities: Bicycle riding around the lake perimeter, local homemade chocolate shopping.',
                    'Overnight Stay: Kodaikanal (Premium / Luxury Resort)',
                    'Meals Included: Premium Breakfast & Special Farewell Dinner',
                ],
            ),
            _day(
                6,
                'KODAIKANAL TO COIMBATORE / DEPARTURE',
                (
                    'RETURN HOME WITH BEAUTIFUL FAMILY MEMORIES Enjoy a final morning breakfast looking out at the foggy valleys. Pack your bags as your private luxury transport picks you up from the resort lobby. Enjoy a comfortable drive down the hills back to Coimbatore Airport or Railway Station for your return home. Your incredible journey concludes with a heart full of joy and unforgettable memories crafted seamlessly by TRAGUIN. TRAGUIN Premium Luxury Proposal — TN-001 4'
                ),
                [
                    'Transfers Included: Private point-to-point departure drop-off service.',
                    'Meals Included: Lavish Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Gem Park | Accord Highland | Hotel Kodai International',
                'Tamil Nadu',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Gem Park | Accord Highland | Hotel Kodai International',
            ),
            _hotel(
                'Sterling Ooty Elk Hill | Fern Hill | The Carlton | Sterling Valley View Buffet Selection)',
                'Tamil Nadu',
                '5N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Sterling Ooty Elk Hill | Fern Hill | The Carlton | Sterling Valley View Buffet Selection)',
            ),
            _hotel(
                'Savoy - IHCL SeleQtions | The Tamara Kodai (Luxury',
                'Tamil Nadu',
                '5N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Savoy - IHCL SeleQtions | The Tamara Kodai (Luxury',
            ),
            _hotel(
                'Private Luxury Colonial Heritage Bungalow | The Tamara Kodai (VVIP Private',
                'Tamil Nadu',
                '5N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Private Luxury Colonial Heritage Bungalow | The Tamara Kodai (VVIP Private',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 05 Nights in premium handpicked hotels and luxury mountain resorts.', 1),
            _inc_included('Luxury Transportation: Private dedicated AC Innova Crysta throughout the tour.', 2),
            _inc_included('Curated Meal Plan: Lavish daily breakfast and dinners included at all resorts.', 3),
            _inc_included('TRAGUIN Support: 24/7 priority concierge line and guest support system.', 4),
            _inc_included('Welcome Amenities: Customized family welcome drink, fresh flowers, and holiday kit.', 5),
            _inc_included('Complimentary Experiences: Reserved private boating tickets at Kodaikanal Lake.', 6),
            _inc_excluded('Domestic or international air tickets / train travel to Coimbatore.', 7),
            _inc_excluded('Monument entry fees, camera passes, and local spot guide expenses.', 8),
            _inc_excluded('Personal expenses including laundry, telephone calls, alcoholic drinks, and tips.', 9),
            _inc_excluded('Optional sightseeing, extreme sports, or any activity outside the plan. TRAGUIN Premium Luxury Proposal — TN-001 5', 10),
        ],
    )
    return package, itinerary

TAMIL_NADU_TN_001_BUILDERS = [
    build_tn_001,
]
