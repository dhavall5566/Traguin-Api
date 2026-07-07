"""Builder functions for LA-001 through LA-010 Ladakh domestic packages."""

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

LADAKH_SLUG = "ladakh"


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



def build_la_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'LA-001'
    tour_code = 'TRAGUIN-LA-001'
    title = 'Leh Discovery Luxury Family Tour'
    duration = '04 Nights / 05 Days'
    slug = 'la-001-leh-discovery-luxury-family-tour'
    itin_slug = 'la-001-leh-discovery-luxury-family-tour-itinerary'
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
            _ph('State / Country: Ladakh, India | Category: Family Tour / Premium Luxury', 2),
            _ph('Destinations Covered: Leh • Sham Valley • Pangong Tso Lake • Khardung La', 3),
            _ph('Ideal for: Families, Adventure Seekers, Luxury Vacationers', 4),
            _ph('Best season: May to September (Best Time to Visit Ladakh)', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Luxury FIT Family Tour', 7),
            _ph('Vehicle: Private dedicated AC-XUV / Innova Crysta for all mountain segments', 8),
            _ph('Meal Plan: Premium breakfasts and dinners included across all stays', 9),
            _ph('Route Map: Leh Arrival → Sham Valley → Pangong Tso Lake → Khardung La → Leh Departure', 10),
            _ph('TRAGUIN Signature Experience: Carefully paced high-altitude acclimatization schedule, priority check-ins at elite handpicked hotels, executive luxury transportation, and direct access to off-beat local experiences', 11),
            _ph('Shopping & Local Experiences: Leh Main Market — hand-woven Pashmina shawls, traditional Tibetan prayer wheels, fine turquoise jewelry, pure organic apricot oils, and hand-hammered brass kitchenware', 12),
            _ph('Important Notes: Avoid physical exertion on Day 1 for AMS prevention; book 45-60 days in advance; only postpaid connections (BSNL, Airtel, Jio) work reliably across Ladakh', 13),
        ],
        moods=['Family', 'Adventure', 'Luxury'],
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
        tagline='Leh Discovery Luxury Family Tour • 04 Nights / 05 Days',
        overview='Welcome to a land beyond the clouds, beautifully brought to life through a Premium Ladakh Experience curated exclusively by TRAGUIN. Ladakh, a pristine realm of high-altitude deserts, breathtaking landscapes, deep azure skies, and ancient monasteries, offers an incomparable escape for your next Luxury Ladakh Holiday. Journey across towering mountain passes, rest beside the mesmerizing shimmer of Pangong Tso Lake, and build unforgettable memories with your loved ones. Our completely handpicked hotels, seamless premium stays, and exclusive experiences ensure a flawless, majestic retreat crafted just for your family.\n\nThis meticulously planned Ladakh Family Tour is engineered as a highly optimized Private FIT itinerary to assure the utmost physical comfort, deep acclimatization, and premium pacing. Your alpine journey encompasses a premium meal plan, private luxury transportation managed by experienced mountain drivers, and high-tier personalized assistance from our localized expert squad. Every component has been refined to capture the vast scenic beauty and iconic attractions of the trans-Himalayas under the trusted guidance of TRAGUIN.\n\nWhy Visit Ladakh for your next Premium Vacation? Ladakh remains an unmatched bucket-list frontier, capturing the hearts of global travelers with its raw geology and deep spiritual Buddhist heritage. This custom package highlights the absolute finest Ladakh Sightseeing landmarks, ensuring your family avoids common logistical hurdles. Our itinerary takes you directly to the most searched experiences—from witnessing the gravity-defying marvel at Magnetic Hill to photographing the rare blue shades of Pangong Tso. Whether your family seeks cultural immersion inside centuries-old prayer halls or mild Himalayan thrills, our custom TRAGUIN Ladakh Packages fuse absolute safety with uncompromising luxury.',
        seo_title='LA-001 | Leh Discovery Luxury Family Tour | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Ladakh package (LA-001 / TRAGUIN-LA-001): Sham Valley, Pangong Tso Lake, Khardung La, Magnetic Hill, Sangam, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Sham Valley sightseeing: Magnetic Hill, Sangam, Hall of Fame, Gurudwara Pathar Sahib', 1),
            _ih('Pangong Tso Lake via Chang La Pass with ultra-luxury glamping domes', 2),
            _ih('Khardung La Pass crossing — one of the highest motorable roads on Earth', 3),
            _ih('TRAGUIN Signature Experience: Curated by TRAGUIN Experts with 24/7 emergency medical support and in-vehicle oxygen backup', 4),
            _ih('Premium Handpicked Hotels: 4-tier luxury accommodation options across Leh and Pangong Tso', 5),
        ],
        days=[
            _day(
                1,
                'Arrival in Leh & Rest for Acclimatization',
                (
                    "Your extraordinary mountain vacation begins with a dramatic flight over the snow-capped Zanskar range into Kushok Bakula Rimpochee Airport in Leh. Upon arrival, experience an assisted premium greeting by our localized TRAGUIN travel representative. Transfer smoothly in your private vehicle to your luxury hotel. Today is strictly reserved for absolute rest and gentle hydration to smoothly adapt to Ladakh's high altitude (11,500 feet)."
                ),
                [
                    'Sightseeing Included: Scenic arrival flight view, private airport transfer, and complete hotel leisure.',
                    'Evening Experience: A relaxed in-hotel welcome briefing over specialized local herbal tea blends.',
                    'Overnight Stay: Handpicked Luxury Resort in Leh (Premium Stay)',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                2,
                'Sham Valley Sightseeing & Monastery Journey',
                (
                    'After a refreshing breakfast, set off on a gentle, senior-and-child-friendly road excursion along the pristine Indus River highway. Explore the legendary Sham Valley, packed with fascinating geological formations and historical structures. Witness the unique optical illusion at Magnetic Hill, experience spiritual tranquility at Gurudwara Pathar Sahib, and admire the majestic confluence of the Indus and Zanskar rivers at Sangam.'
                ),
                [
                    'Sightseeing Included: Magnetic Hill, Confluence at Sangam, Hall of Fame Museum, Gurudwara Pathar Sahib.',
                    'Photography Points: Phenomenal multi-colored contrast shots of the river confluence from elevated custom viewpoints.',
                    'Overnight Stay: Luxury Hotel Wing in Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'Leh to High-Altitude Pangong Tso Lake Cruise',
                (
                    'Depart early in the morning via a thrilling mountain route cutting through Chang La Pass (17,590 feet) to arrive at the world-renowned Pangong Tso Lake, stretching across the international border. As you arrive, the incredible expanse of changing turquoise, green, and deep blue hues will unfold before your eyes. Walk along the legendary lakeside banks, enjoy the crisp alpine air, and relax inside highly comfortable, fully heated premium luxury glamping structures right near the shore.'
                ),
                [
                    'Sightseeing Included: Chang La Pass crossing, Pangong Lake shores exploration, iconic movie shooting spots.',
                    'Evening Experience: A premium hot lakeside dinner paired with an exceptional stargazing session under the unpolluted night sky.',
                    'Overnight Stay: Ultra-Luxury Boutique Glamping Domes at Pangong Tso',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                4,
                'Pangong to Leh via the Mighty Khardung La Pass',
                (
                    'Awake to a mesmerizing sunrise over the tranquil waters of Pangong Tso. Drive back to Leh via the world-famous Khardung La Pass—standing at an immense 17,582 feet, long celebrated as one of the highest motorable roads on Earth. Celebrate the achievement with a family photo session at the top. Arrive back in Leh by afternoon and spend your evening exploring the historic town center at your own comfortable pace.'
                ),
                [
                    'Sightseeing Included: Khardung La Pass summit, Leh Palace outer views, and Leh Main Market walks.',
                    'Optional Activities: Curated cafe hoppings or private shopping for precious local stones and shawls.',
                    'Overnight Stay: Handpicked Luxury Resort in Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'Farewell Departure from Leh',
                (
                    'Savor your final premium breakfast while gazing out at the beautiful Stok Kangri mountain peaks. Our luxury vehicle will pick you up for an assisted transfer back to Leh Airport for your return flight home, concluding your magnificent family holiday filled with unforgettable memories.'
                ),
                [
                    'Meals Included: Breakfast',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Singge Palace / Hotel Shangrila | Pangong Inn Luxury Cottage',
                'Leh (3 Nights) / Pangong Tso (1 Night)',
                '04 Nights',
                'Deluxe',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Singge Palace / Hotel Shangrila (Leh, 3 Nights) | Pangong Inn Luxury Cottage (Pangong Tso, 1 Night) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                "The Grand Dragon Ladakh (Premier Room) | Nature's Nest Luxury Camp",
                'Leh (3 Nights) / Pangong Tso (1 Night)',
                '04 Nights',
                'Premium',
                'Premier Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                2,
                description="OPTION 02 – PREMIUM: The Grand Dragon Ladakh (Premier Room) (Leh, 3 Nights) | Nature's Nest Luxury Camp (Pangong Tso, 1 Night) | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                'Stok Palace Heritage Hotel / Zen Resort | Pangong Hermitage Luxury Domes',
                'Leh (3 Nights) / Pangong Tso (1 Night)',
                '04 Nights',
                'Luxury',
                'Heritage / Luxury Room',
                'JAI (All Meals Included)',
                5,
                3,
                description='OPTION 03 – LUXURY: Stok Palace Heritage Hotel / Zen Resort (Leh, 3 Nights) | Pangong Hermitage Luxury Domes (Pangong Tso, 1 Night) | JAI (All Meals Included)',
            ),
            _hotel(
                'TRAGUIN Private Signature Estate Wing | The Ultimate Travelling Camp (TUTC)',
                'Leh (3 Nights) / Pangong Tso (1 Night)',
                '04 Nights',
                'Ultra Luxury',
                'Signature Estate Wing / Luxury Glamping Suite',
                'Chef Curated Bespoke Menu',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Private Signature Estate Wing (Leh, 3 Nights) | The Ultimate Travelling Camp (TUTC) (Pangong Tso, 1 Night) | Chef Curated Bespoke Menu',
            ),
        ],
        inclusions=[
            _inc_included('Luxury Accommodations: Double sharing rooms in handpicked premium hotels.', 1),
            _inc_included('Premium Meals: Nourishing breakfasts and dinners included across all stays.', 2),
            _inc_included('Luxury Transportation: Private dedicated AC-XUV / Innova Crysta for all mountain segments.', 3),
            _inc_included('Sightseeing Permits: Outer Line Permits (ILP) and environmental fees managed by TRAGUIN.', 4),
            _inc_included('Assistance & Oxygen: 24/7 on-call emergency medical support and in-vehicle oxygen backup.', 5),
            _inc_included('Welcome Perks: Traditional Ladakhi welcome stoles and fresh fruit hampers upon check-in.', 6),
            _inc_excluded('Airfare flight tickets to and from Leh.', 7),
            _inc_excluded('Tips, porterage fees, and general driver gratuities.', 8),
            _inc_excluded('Personal expenses like laundry, alcoholic drinks, and phone bills.', 9),
            _inc_excluded('Professional guide service fees unless explicitly requested ahead.', 10),
            _inc_excluded('Any additional costs arising from unexpected landslides or flight cancellations.', 11),
        ],
    )
    return package, itinerary

def build_la_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'LA-002'
    tour_code = 'TRAGUIN-LA-002'
    title = 'Leh Nubra Pangong Highland Luxury Escape'
    duration = '06 Nights / 07 Days'
    slug = 'la-002-leh-nubra-pangong-highland-luxury-escape'
    itin_slug = 'la-002-leh-nubra-pangong-highland-luxury-escape-itinerary'
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
            _ph('State / Country: Ladakh, India | Category: Premium Family Tour Package', 2),
            _ph('Destinations Covered: Leh • Nubra Valley • Pangong Tso • Khardung La', 3),
            _ph('Ideal for: Families, Multi-Generational Groups, Luxury Vacationers', 4),
            _ph('Best season: May to September (Best Time to Visit Ladakh)', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Executive Luxury FIT Family Tour', 7),
            _ph('Vehicle: Private high-clearance executive SUV (Innova Crysta) throughout', 8),
            _ph('Meal Plan: Modified American Plan (Daily Breakfast & Gourmet Dinners)', 9),
            _ph('Route Map: Leh Arrival → Monasteries & Sham Valley → Khardung La → Nubra Valley → Turtuk → Pangong Tso → Chang La → Leh Departure', 10),
            _ph('TRAGUIN Signature Experience: 24/7 dedicated on-ground localized concierge assistance, priority access lines at high check-points, handpicked premium properties boasting centralized insulation/heating systems, and medically certified backup emergency logistics', 11),
            _ph('Shopping & Local Experiences: Leh Main Bazaar — rare cashmere pashmina shawls, authentic Tibetan prayer wheels, turquoise jewelry ornaments, organic sun-dried apricots, and unique local hand-woven rugs; stunning pictures at popular Instagram locations surrounding Shanti Stupa during golden hour', 12),
            _ph('Important Notes: Strict complete physical rest required on Day 01 to prevent AMS; high diurnal temperature variations — layering with proper thermal wear and down jackets advised; advance bookings heavily recommended to guarantee preferred premium suites', 13),
        ],
        moods=['Family', 'Luxury', 'Multi-Generational'],
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
        tagline='Leh Nubra Pangong Highland Luxury Escape • 06 Nights / 07 Days',
        overview="Welcome to the land of high passes, ancient monasteries, and dramatic high-altitude cold deserts, meticulously designed via this Premium Ladakh Experience curated by TRAGUIN. This bespoke Ladakh Family Tour introduces your loved ones to a majestic realm of breathtaking landscapes, serene emerald-blue lakes, and deep cultural immersion. Combining elite luxury with safety-vetted handpicked hotels, executive oxygen-equipped transportation, and slow-paced acclimatization schedules, TRAGUIN ensures your high-altitude holiday transitions into a seamless collection of unforgettable memories. Welcome to an exceptional, sophisticated travel layout designed for the discerning explorer. \n\nThis private executive Luxury Ladakh Holiday is custom-tailored as an exclusive FIT itinerary, accommodating your family with unmatched safety protocols and high-tier hospitality. The complete path traverses iconic mountain passes, deep valley routes, and high lake vistas. Every component—ranging from private local high-clearance oxygenated vehicles to premium stays and a comprehensive meal plan—reflects the strict TRAGUIN curated experience standard. \n\nWhy Visit Ladakh for a Family Vacation? Ladakh boasts some of the most dramatic physical features on Earth, making a Ladakh Family Tour an educational, deeply aesthetic, and unifying journey. Highly searched tourist experiences center around traversing the world's highest motorable passes, witnessing the gravity-defying wonders of Magnetic Hill, and sleeping under a canopy of billion-star skies beside high-altitude saltwater wetlands. Famous attractions include the historical Leh Palace, the high-altitude desert of Nubra Valley, and the vast turquoise expanse of Pangong Tso. TRAGUIN Ladakh Packages seamlessly manage high-altitude dynamics, ensuring elderly members and children enjoy the scenic beauty, local Indo-Tibetan culture, unique double-humped camel safaris, and popular Instagram locations without any environmental stress. ",
        seo_title='LA-002 | Leh Nubra Pangong Highland Luxury Escape | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Ladakh package (LA-002 / TRAGUIN-LA-002): Leh, Nubra Valley, Pangong Tso, Khardung La, Turtuk, and 4-tier handpicked accommodation. ',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Khardung La Pass crossing — one of the world's highest motorable passes at 5,359 meters", 1),
            _ih('Nubra Valley with Diskit Monastery and double-humped Bactrian camel ride at Hunder Sand Dunes', 2),
            _ih('Turtuk village excursion — unique Balti culture on the edge of the line of control', 3),
            _ih('Pangong Tso via Shyok River with private sunset bonfire and lakeside stargazing', 4),
            _ih('Chang La Pass return with Thiksey Monastery and Shey Palace complex', 5),
        ],
        days=[
            _day(
                1,
                'Arrival in Leh & Acclimatization Leisure Day',
                (
                    'Arrive at Kushok Bakula Rimpochee Airport in Leh, located at an elevation of 3,524 meters. Experience a warm traditional welcome by your dedicated TRAGUIN destination officer. Transfer directly via private executive luxury vehicle to your handpicked premium hotel. The remainder of the day is strictly reserved for complete rest to allow healthy atmospheric pressure and oxygen level acclimatization, ensuring a smooth family holiday. '
                ),
                [
                    'Sightseeing Included: Relaxed mountain-view residency check-in.',
                    'Evening Experience: Gentle in-house orientation briefing with warm herbal tea mixtures.',
                    'Overnight Stay: Handpicked Luxury Resort / Hotel in Leh',
                    'Meals Included: Lunch & Dinner',
                ],
            ),
            _day(
                2,
                'Monasteries, Magnetic Hill & Confluence Exploration',
                (
                    'Enjoy a beautiful high-altitude morning breakfast. Today, enjoy comfortable local Ladakh Sightseeing along the scenic Indus Valley highway. Your family will witness the inexplicable visual illusion at Magnetic Hill and visit the sacred Gurudwara Pathar Sahib, followed by the majestic confluence point of the Indus and Zanskar rivers. '
                ),
                [
                    'Sightseeing Included: Hall of Fame Museum, Magnetic Hill, Confluence of Indus & Zanskar (Sangam), Spituk Monastery.',
                    'Photography Points: Incredible panoramic setups at the dual-color river confluence valley.',
                    'Overnight Stay: Handpicked Luxury Resort / Hotel in Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'Leh to Nubra Valley via the Iconic Khardung La',
                (
                    "Prepare for an exhilarating drive across the legendary Khardung La, historically celebrated as one of the world's highest motorable passes at 5,359 meters. Marvel at the breathtaking landscapes of snow-capped peaks. Descend into the spectacular, wide-open Nubra Valley, known for its silver sand dunes and oasis villages. "
                ),
                [
                    'Sightseeing Included: Khardung La Pass crossing, Diskit Monastery with the giant Maitreya Buddha statue.',
                    'Local Experiences: An exclusive double-humped Bactrian camel ride across the Hunder Sand Dunes.',
                    'Overnight Stay: Premium Luxury Desert Camp / Cottage in Nubra Valley',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                4,
                'Turtuk Village Excursion – The Baltistan Border Experience',
                (
                    'Embark on an immersive cultural journey to Turtuk, a unique valley village opened to tourism recently. Driving along the pristine Shyok River, your family will discover a distinct Balti culture, stone architecture, and apricot orchards tucked safely away on the edge of the line of control. '
                ),
                [
                    'Sightseeing Included: Turtuk historic village walk, local Balti heritage house tour.',
                    'Food Suggestions: Sampling authentic organic apricot pancakes and local walnut dishes.',
                    'Overnight Stay: Premium Luxury Desert Camp / Cottage in Nubra Valley',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'Nubra to the Majestic Pangong Tso along Shyok River',
                (
                    'Depart early along the rugged, visually spectacular Shyok river road to reach the jewel of your Premium Ladakh Experience—Pangong Tso. Arrive to witness the deep blue colors of this high-altitude saltwater lake stretching deep into China, bordered by stark, multi-shaded mountains. '
                ),
                [
                    'Sightseeing Included: Pangong Lake shore drive, famous cinematic shooting spots.',
                    'Evening Experience: A private sunset bonfire session organized on the lakeside with warm soup servings.',
                    'Overnight Stay: Premium Semi-Luxury Heated Cottage / Camp at Pangong Tso',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                6,
                'Pangong Tso to Leh via Chang La High Pass',
                (
                    "Awake early to capture the brilliant sunrise reflection over the crystal lake waters—a legendary photography point. Begin your return journey to Leh, traversing the mighty Chang La Pass (5,360 meters). Stop to visit the magnificent, historic Thiksey Monastery, reminiscent of Tibet's Potala Palace. "
                ),
                [
                    'Sightseeing Included: Chang La Pass crossing, Thiksey Monastery, Shey Palace complex.',
                    'Optional Activities: Evening leisurely walk around the vibrant local Leh Main Bazaar for souvenir collection.',
                    'Overnight Stay: Handpicked Luxury Resort / Hotel in Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                7,
                'Departure from Leh with Unforgettable Memories',
                (
                    'Bid farewell to the mystical lands of Ladakh. Enjoy an early morning breakfast before boarding your private transfer vehicle. Your TRAGUIN representative will assist you smoothly through the airport terminals for your homeward flight, carrying home lifelong family memories. '
                ),
                [
                    'Meals Included: Breakfast',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Singge Palace / Similar | Hunder Resort / Similar | Pangong Inn Cottage / Similar',
                'Leh (3 Nights) / Nubra Valley (2 Nights) / Pangong Tso (1 Night)',
                '06 Nights',
                'Deluxe',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Singge Palace / Similar (Leh, 3 Nights) | Hunder Resort / Similar (Nubra Valley, 2 Nights) | Pangong Inn Cottage / Similar (Pangong Tso, 1 Night)',
            ),
            _hotel(
                'The Grand Dragon Ladakh | Nubra Eco Lodge / Luxury Camps | Pangong Woods Cottages',
                'Leh (3 Nights) / Nubra Valley (2 Nights) / Pangong Tso (1 Night)',
                '06 Nights',
                'Premium',
                'Premier Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                2,
                description='OPTION 02 – PREMIUM: The Grand Dragon Ladakh (Leh, 3 Nights) | Nubra Eco Lodge / Luxury Camps (Nubra Valley, 2 Nights) | Pangong Woods Cottages (Pangong Tso, 1 Night)',
            ),
            _hotel(
                'The Zen Ladakh / Luxury Wing | Stone Hedge Luxury Hotel | Nirvana Resort Luxury Cottages',
                'Leh (3 Nights) / Nubra Valley (2 Nights) / Pangong Tso (1 Night)',
                '06 Nights',
                'Luxury',
                'Luxury Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Zen Ladakh / Luxury Wing (Leh, 3 Nights) | Stone Hedge Luxury Hotel (Nubra Valley, 2 Nights) | Nirvana Resort Luxury Cottages (Pangong Tso, 1 Night)',
            ),
            _hotel(
                'Chamba Camp Thiksey (Glamping) | The Kyagar Luxury Valley Resort | Martsemik Camping Glamping Suite',
                'Leh (3 Nights) / Nubra Valley (2 Nights) / Pangong Tso (1 Night)',
                '06 Nights',
                'Ultra Luxury',
                'Glamping Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Chamba Camp Thiksey (Glamping) (Leh, 3 Nights) | The Kyagar Luxury Valley Resort (Nubra Valley, 2 Nights) | Martsemik Camping Glamping Suite (Pangong Tso, 1 Night)',
            ),
        ],
        inclusions=[
            _inc_included('Handpicked Accommodations: Choice of premium hotel, cottage, or luxury glamping suites.', 1),
            _inc_included('Meal Plan: Modified American Plan (Daily Breakfast & Gourmet Dinners).', 2),
            _inc_included('Luxury Transfers: Private, high-clearance executive SUV (Innova Crysta) throughout.', 3),
            _inc_included('Sightseeing & Passes: All Inner Line Permits, Wildlife fees, and environment taxes managed by TRAGUIN support.', 4),
            _inc_included('Special Welcome Amenities: Oxygen canisters equipped inside vehicles, welcome dry fruit platters, and traditional silk scarf welcome.', 5),
            _inc_excluded('Domestic flight airline tickets to and from Leh.', 6),
            _inc_excluded('Personal expenditures like laundry, boutique minibars, phone bills.', 7),
            _inc_excluded('Professional camera equipment entry fees at historical monuments.', 8),
            _inc_excluded('Optional recreational activities (e.g., River Rafting, Camel Safari rides).', 9),
            _inc_excluded('Personal dynamic travel health and emergency evacuation insurance.', 10),
        ],
    )
    return package, itinerary

def build_la_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'LA-003'
    tour_code = 'TRAGUIN-LA-003'
    title = 'Ultimate Ladakh Road Trip Experience'
    duration = '08 Nights / 09 Days'
    slug = 'la-003-ultimate-ladakh-road-trip-experience'
    itin_slug = 'la-003-ultimate-ladakh-road-trip-experience-itinerary'
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
            _ph('State / Country: Ladakh, India | Category: Adventure / Luxury Road Trip', 2),
            _ph('Destinations Covered: Leh • Sham Valley • Nubra Valley • Turtuk • Pangong Lake', 3),
            _ph('Ideal for: Adventure Enthusiasts, Honeymooners, Families', 4),
            _ph('Best season: May to October', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Premium Custom FIT Road Trip', 7),
            _ph('Vehicle: Private 4x4 Scorpio/Innova for all mountain-road transfers', 8),
            _ph('Meal Plan: Nourishing breakfasts and dinners included across all camps', 9),
            _ph('Route Map: Leh Arrival → Sham Valley → Khardung La → Nubra → Turtuk → Pangong → Chang La → Tso Moriri → Leh Departure', 10),
            _ph('TRAGUIN Signature Experience: Private bonfire nights at high-altitude lakeshores, pre-arranged VIP entry passes at restricted borders, and fully certified mechanics checking luxury transportation vehicles continuously daily', 11),
            _ph('Shopping & Local Experiences: Leh markets — authentic Pashmina shawls, handcrafted Tibetan prayer wheels, intricate silver jewelry, organic dried apricots; premium mountain-view cafes for sea-buckthorn juice and fresh yak-cheese pizzas', 12),
            _ph('Important Notes: Minimum 24 to 36 hours total physical rest mandatory upon landing; only postpaid SIM cards (BSNL, Airtel, Jio) operate efficiently; book 45-60 days ahead due to limited high-end property availability', 13),
        ],
        moods=['Adventure', 'Luxury', 'Road Trip'],
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
        tagline='Ultimate Ladakh Road Trip Experience • 08 Nights / 09 Days',
        overview="Welcome to a high-octane luxury adventure across the roof of the world, masterfully curated by TRAGUIN. A Ladakh Road Trip is not just a holiday; it's an emotional pilgrimage through breathtaking landscapes, high-altitude mountain passes, and soul-stirring cultural bastions. Witness the raw scenic beauty of Ladakh as you traverse dramatic valleys, pristine deep-blue lakes, and historical monasteries. This Premium Ladakh Experience blends adrenaline-pumping discovery with premium stays and handpicked hotels, creating unforgettable memories that linger for a lifetime. Choose the best time to visit Ladakh and step into an extraordinary world with TRAGUIN Ladakh Packages. \n\nThis meticulously mapped Luxury Ladakh Holiday is designed as a premium custom FIT (Free Independent Traveler) roadmap. Your elite experience includes luxury transportation using specialized 4x4 vehicles suitable for rugged terrains, a highly supportive premium meal plan, and curated experiences monitored by our on-ground expert mechanics and local travel consultants. TRAGUIN ensures strict acclimatization protocols combined with premium mountain-facing cottages to deliver maximum luxury, flexibility, and absolute peace of mind. \n\nWhy Visit Ladakh? Known as the land of high passes, Ladakh features globally celebrated iconic attractions and top tourist places in Ladakh like the mesmerizing Pangong Lake, Khardung La Pass (one of the highest motorable roads globally), and the sand dunes of Hunder. It represents the ultimate adrenaline territory for a Ladakh Honeymoon Package or an active Ladakh Family Tour. Our itinerary takes you to the most searched experiences such as tracing the optical illusion at Magnetic Hill, discovering the hidden border village of Turtuk, and photographing popular Instagram locations including the reflection zones of high-altitude lakes and dramatic cliffside monasteries. Immerse your senses in local Ladakhi culture, traditional cuisine highlights, and exclusive high-altitude stargazing. ",
        seo_title='LA-003 | Ultimate Ladakh Road Trip Experience | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days Ladakh road trip (LA-003 / TRAGUIN-LA-003): Sham Valley, Nubra Valley, Turtuk, Pangong Lake, Tso Moriri, and 4-tier handpicked accommodation. ',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Sham Valley tour with Magnetic Hill, Sangam, Hall of Fame, and Gurudwara Pathar Sahib', 1),
            _ih('Khardung La Pass crossing and Nubra Valley with Bactrian camel safari at Hunder Sand Dunes', 2),
            _ih('Exclusive Turtuk border village discovery along the Shyok River', 3),
            _ih('Pangong Lake via scenic Shyok route with luxury bonfire under starlit Himalayan sky', 4),
            _ih('Optional Tso Moriri exploration with Chumathang Hot Springs and wildlife spotting', 5),
        ],
        days=[
            _day(
                1,
                'Arrival in Leh & Acclimatization Leisure',
                (
                    'Fly into Kushok Bakula Rimpochee Airport, Leh—one of the most scenic high-altitude airports globally. Experience a grand, personalized premium welcome by our TRAGUIN tour representative. Enjoy a direct luxury transfer to your handpicked premium hotel. The remainder of the day is strictly reserved for absolute resting to seamlessly adjust to the high altitudes (11,500 feet). '
                ),
                [
                    'Sightseeing Included: Relaxed airport transfer, mountain-view room positioning.',
                    'Evening Experience: A gentle walk to the local Leh Market for a warm welcome note session and standard briefing.',
                    'Overnight Stay: Handpicked Premium Luxury Hotel in Leh',
                    'Meals Included: Lunch & Dinner',
                ],
            ),
            _day(
                2,
                'Sham Valley Tour & Iconic Sightseeing',
                (
                    'After a premium breakfast, start your luxury road trip along the pristine Indus River. Today you discover legendary spots that define Ladakh Sightseeing. Witness the mysterious phenomenon at Magnetic Hill and observe the holy serenity of Gurudwara Pathar Sahib before admiring the majestic confluence of two massive rivers. '
                ),
                [
                    'Sightseeing Included: Magnetic Hill, Confluence of Indus and Zanskar Rivers (Sangam), Hall of Fame Museum, Sangam photography points.',
                    'Local Food Suggestions: Traditional hot butter tea and gourmet steam-dumplings at a curated countryside luxury rest-stop.',
                    'Overnight Stay: Handpicked Premium Luxury Hotel in Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'Leh to Nubra Valley via the Iconic Khardung La Pass',
                (
                    'Prepare for a thrill of a lifetime as your premium 4x4 scales the mighty Khardung La Pass, standing proudly at an elevation of 17,582 feet. Descend into the spectacular desert plains of Nubra Valley. Capture breathtaking landscapes and marvel at the giant 106-foot Maitreya Buddha statue at Diskit Monastery. '
                ),
                [
                    'Sightseeing Included: Khardung La Pass crossing, Diskit Monastery, Hunder Sand Dunes.',
                    'Immersive Experiences: A unique safari across cold sand dunes riding the rare double-humped Bactrian Camels.',
                    'Overnight Stay: Premium Luxury Tents / Cottages in Nubra Valley',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                4,
                'Exclusive Turtuk Border Village Discovery',
                (
                    'Drive deeper towards the northernmost border of India to unlock Turtuk, a hidden Baltic village opened to tourism recently. Walk through scenic apricot orchards and stone-carved heritage pathways, contrasting dramatically with the harsh high-mountain passes around it. '
                ),
                [
                    'Sightseeing Included: Turtuk heritage bridge, Baltic museum courtyard, panoramic views of the Karakoram range.',
                    'Optional Activities: Interaction with village elders to understand the fascinating border history.',
                    'Overnight Stay: Premium Luxury Tents / Cottages in Nubra Valley',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'Nubra to Pangong Lake via Scenic Shyok Route',
                (
                    'Set out early on an adventurous mountain route tracing the rugged Shyok River bed. Your destination is the crown jewel of your trip: the majestic Pangong Lake. Watch in absolute awe as this high-altitude saltwater lake changes its shades from deep turquoise to brilliant indigo right before your eyes. '
                ),
                [
                    'Sightseeing Included: Shyok valley route, Pangong Lake shores, popular movie shooting locations.',
                    'Evening Experience: Luxury bonfire setup by the lakeshore under an exceptionally clear, starlit Himalayan sky.',
                    'Overnight Stay: Exclusive Premium Eco-Resort Camps right next to Pangong Lake',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                6,
                'Pangong Lake to Leh via Chang La Pass',
                (
                    'Wake up early to catch a breathtaking sunrise reflection bouncing off the calm waters of Pangong Lake. Begin your return road trip back towards Leh, navigating across the third highest motorable pass in the world—Chang La Pass (17,586 feet). '
                ),
                [
                    'Sightseeing Included: Chang La Pass, Thiksey Monastery (resembling the Potala Palace of Tibet).',
                    'Photography Points: Golden hour mountain panoramic backdrops from the rooftop of Thiksey.',
                    'Overnight Stay: Premium Luxury Hotel in Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                7,
                'Tso Moriri Exploration (Optional / Highlight Road Trip)',
                (
                    'For true adventurers, a smooth journey into the high-altitude wetlands of Tso Moriri Lake is organized. This pristine sanctuary offers total isolation and untouched natural scenery, far away from regular tourist rushes. '
                ),
                [
                    'Sightseeing Included: Chumathang Hot Springs, Tso Moriri lake boundaries, wildlife spotting (Kiangs/Tibetan Wild Ass).',
                    'Overnight Stay: Handpicked Deluxe Lakeview Cottage / Leh Luxury Base',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                8,
                'Souvenir Excursions & Cultural Farewell Dinner',
                (
                    'A relaxing day tailored for personalized leisure and local retail therapy. Take your time visiting fine local craft markets or exploring independent cafes celebrating the colorful lifestyle of modern Leh town. '
                ),
                [
                    'Sightseeing Included: Shanti Stupa evening sunset views, Leh Palace tour.',
                    'Evening Experience: A celebratory TRAGUIN Farewell Dinner highlighting authentic multi-course Himalayan signature dishes.',
                    'Overnight Stay: Premium Luxury Hotel in Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                9,
                'Departure with Unforgettable Memories',
                (
                    'Savor your final luxury breakfast amidst crisp mountain air. Complete your check-out and boarding assistance. Board your private luxury airport vehicle transfer to catch your flight home, concluding your premium adventure. '
                ),
                [
                    'Meals Included: Breakfast',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Singge Palace / Similar | Hunder Resort Camps | Pangong Inn Cottages',
                'Leh (5 Nights) / Nubra Valley (2 Nights) / Pangong Lake (1 Night)',
                '08 Nights',
                'Deluxe',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Singge Palace / Similar (Leh, 5 Nights) | Hunder Resort Camps (Nubra Valley, 2 Nights) | Pangong Inn Cottages (Pangong Lake, 1 Night)',
            ),
            _hotel(
                'The Grand Dragon Ladakh | Nubra Organic Retreat | Pangong Eco Traveler Tents',
                'Leh (5 Nights) / Nubra Valley (2 Nights) / Pangong Lake (1 Night)',
                '08 Nights',
                'Premium',
                'Premier Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                2,
                description='OPTION 02 – PREMIUM: The Grand Dragon Ladakh (Leh, 5 Nights) | Nubra Organic Retreat (Nubra Valley, 2 Nights) | Pangong Eco Traveler Tents (Pangong Lake, 1 Night)',
            ),
            _hotel(
                'The Zen Ladakh Resort | Stone Hedge Luxury Hotel | Martsemik Camping Resort',
                'Leh (5 Nights) / Nubra Valley (2 Nights) / Pangong Lake (1 Night)',
                '08 Nights',
                'Luxury',
                'Luxury Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Zen Ladakh Resort (Leh, 5 Nights) | Stone Hedge Luxury Hotel (Nubra Valley, 2 Nights) | Martsemik Camping Resort (Pangong Lake, 1 Night)',
            ),
            _hotel(
                'Chamba Camp Thiksey | Lumiere Luxury Cottages | Pangong Luxury Wilderness Camp',
                'Leh (5 Nights) / Nubra Valley (2 Nights) / Pangong Lake (1 Night)',
                '08 Nights',
                'Ultra Luxury',
                'Luxury Glamping Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Chamba Camp Thiksey (Leh, 5 Nights) | Lumiere Luxury Cottages (Nubra Valley, 2 Nights) | Pangong Luxury Wilderness Camp (Pangong Lake, 1 Night)',
            ),
        ],
        inclusions=[
            _inc_included('Handpicked Hotels: Premium luxury stays with proper heating & mountain views.', 1),
            _inc_included('Curated Meal Plan: Nourishing breakfasts and dinners included across all camps.', 2),
            _inc_included('Luxury Transportation: Private 4x4 Scorpio/Innova for all mountain-road transfers.', 3),
            _inc_included('Inner Line Permits: Seamlessly managed environment fees and wildlife passes.', 4),
            _inc_included('Oxygen Assistance: Oxygen cylinders equipped inside vehicles for safety protocols.', 5),
            _inc_included('TRAGUIN Support: 24/7 dedicated local on-ground assistance desk.', 6),
            _inc_excluded('Airfare flight tickets to and from Leh.', 7),
            _inc_excluded('Personal expenditures like telephone bills, laundry, or premium bar orders.', 8),
            _inc_excluded('Camel rides, quad biking fees, or extreme river rafting entry tickets.', 9),
            _inc_excluded('Tipping fees, monument camera passes, or guide fees.', 10),
            _inc_excluded('Expenses resulting from roadblocks, landslides, or flight disruptions.', 11),
        ],
    )
    return package, itinerary

def build_la_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'LA-004'
    tour_code = 'TRAGUIN-LA-004'
    title = 'Premium Bike Expedition Ladakh'
    duration = '09 Nights / 10 Days'
    slug = 'la-004-premium-bike-expedition-ladakh'
    itin_slug = 'la-004-premium-bike-expedition-ladakh-itinerary'
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
            _ph('State / Country: Ladakh, India | Category: Adventure / Bike Expedition', 2),
            _ph('Destinations Covered: Leh • Sham Valley • Nubra Valley • Turtuk • Pangong Lake • Hanle • Tso Moriri', 3),
            _ph('Ideal for: Adventure Enthusiasts, Bikers, Photographers', 4),
            _ph('Best season: June to September', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Premium Guided Motorcycle Expedition with 4x4 Backup', 7),
            _ph('Vehicle: Royal Enfield 500cc / Himalayan bikes with 4x4 support vehicle', 8),
            _ph('Meal Plan: Premium meals as per day-by-day itinerary', 9),
            _ph('Route Map: Leh → Sham Valley → Khardung La → Nubra → Turtuk → Pangong → Hanle → Tso Moriri → Leh Departure', 10),
            _ph('TRAGUIN Signature Experience: Professional mechanics trailing the group, oxygen reserves in backup vehicles, and custom curated dine-around setups at remote destinations like Hanle', 11),
            _ph('Shopping & Local Experiences: Leh Main Bazar — genuine pashmina shawls, hand-woven carpets, intricate silver prayer wheels, organic dried apricots; premium cafes for fresh seabuckthorn tea', 12),
            _ph('Important Notes: Resting on Day 1 mandatory under TRAGUIN medical protocols; valid Indian permanent driving license required for gear motorcycles; mountain passes subject to weather alterations', 13),
        ],
        moods=['Adventure', 'Biking', 'Photography'],
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
        tagline='Premium Bike Expedition Ladakh • 09 Nights / 10 Days',
        overview="Welcome to the ultimate thrill of a lifetime, proudly presented by TRAGUIN. Ladakh, a land of majestic barren high-altitude deserts, deep sapphire lakes, and iconic mountain passes, calls out to the explorer inside you. Our Luxury Ladakh Holiday Bike Expedition blends pure raw adrenaline with signature premium comfort. Ride through the legendary breathtaking landscapes on powerful premium machinery, engineering unforgettable memories under vast open horizons. With handpicked hotels, elite mechanical support, and curated experiences, your Premium Ladakh Experience will be nothing short of legendary. \n\nThis meticulously mapped Ladakh Bike Expedition is designed for discerning riders who demand high adventure without sacrificing corporate presentation standards. Your itinerary covers rugged terrain with top-tier technical backup vehicles, an experienced tour leader, localized support networks, and custom selected premium stays. Every rider receives personalized assistance to handle altitude acclimatization perfectly, guaranteeing a seamless blend of grit and absolute comfort. \n\nWhy embark on a Luxury Ladakh Holiday? Ladakh stands out as the ultimate destination for global adventure riders. Key iconic attractions like the Khardung La pass, Chang La pass, and the remote village of Turtuk offer the most searched experiences in Indian sub-continental tourism. The majestic lakes of Pangong Tso and Tso Moriri offer pristine popular Instagram locations, making Ladakh Sightseeing an absolute dream for travel connoisseurs. Whether it's discovering ancient multi-tiered monasteries, navigating extreme water crossings, or experiencing the high-altitude stargazing haven of Hanle, our TRAGUIN Ladakh Packages offer deep cultural encounters alongside premium exploration. ",
        seo_title='LA-004 | Premium Bike Expedition Ladakh | TRAGUIN',
        seo_description='Premium 09 Nights / 10 Days Ladakh bike expedition (LA-004 / TRAGUIN-LA-004): Sham Valley, Nubra, Turtuk, Pangong, Hanle, Tso Moriri, Royal Enfield bikes, and 4-tier accommodation. ',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Sham Valley warm-up ride with Magnetic Hill, Sangam, and Gurudwara Pathar Sahib', 1),
            _ih('Khardung La Pass crossing to Nubra Valley with Bactrian camel ride at Hunder', 2),
            _ih('Turtuk border village with Balti Heritage Museum and Indo-Pak viewpoint spots', 3),
            _ih('Pangong Lake via Shyok River with lakeside campfire under star-studded sky', 4),
            _ih('Hanle stargazing haven and Tso Moriri via Rezang La Memorial', 5),
        ],
        days=[
            _day(
                1,
                'Arrival in Leh - Acclimatization & Welcome Briefing',
                (
                    'Land at Kushok Bakula Rimpochee Airport, Leh. Step into an assisted private transit to your handpicked luxury hotel. Today is explicitly kept for essential altitude acclimatization to guarantee a safe ride ahead. Sip hot herbal tea and relax in premium stays as your body adapts to the beautiful mountain atmosphere. '
                ),
                [
                    'Sightseeing Included: Rest and relaxation inside hotel premises.',
                    'Evening Experience: Introductory briefing and route mapping session conducted by TRAGUIN Experts.',
                    'Overnight Stay: The Grand Dragon / Stone Hedge Hotel, Leh (Premium Luxury Stay)',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                2,
                'Ride to Sham Valley - Bike Allocation & Warm-Up Trails',
                (
                    "Following a robust breakfast, your premium bikes are formally allocated. Today features a relaxed orientation ride through scenic routes into the Sham Valley to let you comfortably test your machine's mechanical layout. "
                ),
                [
                    'Sightseeing Included: Magnetic Hill, confluence of Indus & Zanskar Rivers (Sangam), and the ancient Gurudwara Pathar Sahib.',
                    'Photography Points: Pristine panoramic lookouts across high mountain gorges.',
                    'Overnight Stay: Premium Boutique Resort, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'Conquering Khardung La to Nubra Valley',
                (
                    'Gear up for an iconic milestone as you rev up your engines to climb the world-renowned Khardung La Pass, located at an incredible altitude of 17,582 feet. Descend safely into the sweeping sand dunes of Nubra Valley, capturing breathtaking landscapes along the way. '
                ),
                [
                    'Sightseeing Included: Khardung La Pass crossing, Diskit Monastery giant Buddha statue.',
                    "Local Experiences: Double-humped Bactrian camel ride amidst Hunder's white sand dunes.",
                    'Overnight Stay: Luxury Desert Wilderness Camp, Nubra',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'Exclusive Day Excursion to Turtuk Village',
                (
                    'Ride close to the border to discover the uniquely historical Balti village of Turtuk. Unveiled to tourism recently, Turtuk offers refreshing apricot orchards, rich ethnic culture, and distinct stone-hewn architecture that sets it apart from traditional Ladakh structures. '
                ),
                [
                    'Sightseeing Included: Balti Heritage Museum, local walk pathways, and Indo-Pak viewpoint spots.',
                    'Food Suggestions: Authentic Balti traditional local cuisine and fresh apricot juices at a village cafe.',
                    'Overnight Stay: Luxury Camp / Premium Resort, Nubra',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'Nubra to Pangong Lake via Shyok River Route',
                (
                    'Navigate through the thrilling, rugged trails of the Shyok River route. Arrive at the iconic Pangong Lake, an incredible high-altitude saltwater marvel known worldwide for shifting its shades from bright turquoise to deep indigo as the day passes. '
                ),
                [
                    'Sightseeing Included: Shyok valley water crossings, Pangong Tso shoreline ride.',
                    'Evening Experience: Lakeside photography and cozy campfire conversation beneath a star-studded sky.',
                    'Overnight Stay: Premium Luxury Glamping Domes, Pangong',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                6,
                'Pangong Lake to the Stargazing Haven of Hanle',
                (
                    'Set forth on a remote, off-the-beaten-path ride through the vast Changthang plains heading towards Hanle. Home to the Indian Astronomical Observatory, Hanle boasts some of the clearest night skies found anywhere globally. '
                ),
                [
                    'Sightseeing Included: Hanle Observatory, high-altitude vast plain sanctuaries.',
                    'Immersive Experiences: Deep-sky observation and premium astrophotography setups curated by experts.',
                    'Overnight Stay: Handpicked Luxury Guest House / Camp, Hanle',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                7,
                'Hanle to Tso Moriri Lake via Rezang La Crossing',
                (
                    'Pay your respects at the historic Rezang La War Memorial before steering your motorcycle towards the magnificent Tso Moriri Lake. This pristine wetland sanctuary is famous for its stunning blue waters, ringed closely by dramatic snow-dusted peaks. '
                ),
                [
                    'Sightseeing Included: Rezang La Memorial, Korzok Village, and Tso Moriri lake sanctuary loop.',
                    'Photography Points: Unrivaled wildlife photography including rare migratory birds and wild Tibetan asses (Kiangs).',
                    'Overnight Stay: Premium Nomadic Camp, Tso Moriri',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                8,
                'Tso Moriri Return to Leh via Mahe Bridge',
                (
                    'Embark on your return journey to Leh, riding alongside the roaring Indus River across the Mahe Bridge. Savor smooth tarmac roads as you reflect on the high mountain passes and immense milestones you have successfully crossed. '
                ),
                [
                    'Sightseeing Included: Chomathang Hot Springs, dramatic geographical rock faces.',
                    'Evening Experience: Leisure time to unwind and celebrate your expedition milestones.',
                    'Overnight Stay: The Grand Dragon / Premium Hotel, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                9,
                'Leisure Exploration & TRAGUIN Farewell Gala',
                (
                    'A relaxing buffer day in Leh to wander at your own pace. Discover local cafes, indulge in souvenir shopping at the local markets, or enjoy standard wellness therapies to unwind your muscles after a long, exhilarating journey. '
                ),
                [
                    'Optional Activities: Souvenir gathering, local monastery tours.',
                    'Evening Experience: Signature TRAGUIN Farewell Gala Dinner with authentic Ladakhi cultural presentations.',
                    'Overnight Stay: Premium Luxury Hotel, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                10,
                'Departure with Unforgettable Memories',
                (
                    'Relish your final morning breakfast looking out at the Stoke Kangri mountain range. Complete your check-out and step into your luxury assisted airport transfer for your flight back home, carrying a treasure trove of unforgettable memories. '
                ),
                [
                    'Meals Included: Breakfast',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Singge Palace | Hunder Resort Camp | Pangong Heritage Camps',
                'Leh (5 Nights) / Nubra Valley (2 Nights) / Lakeside Glamping (2 Nights)',
                '09 Nights',
                'Deluxe',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Singge Palace (Leh, 5 Nights) | Hunder Resort Camp (Nubra Valley, 2 Nights) | Pangong Heritage Camps (Lakeside Glamping, 2 Nights)',
            ),
            _hotel(
                'Hotel Zen Ladakh | Nubra Organic Retreat | Pangong Inn Luxury Wing',
                'Leh (5 Nights) / Nubra Valley (2 Nights) / Lakeside Glamping (2 Nights)',
                '09 Nights',
                'Premium',
                'Premier Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                2,
                description='OPTION 02 – PREMIUM: Hotel Zen Ladakh (Leh, 5 Nights) | Nubra Organic Retreat (Nubra Valley, 2 Nights) | Pangong Inn Luxury Wing (Lakeside Glamping, 2 Nights)',
            ),
            _hotel(
                'The Grand Dragon Ladakh | Stone Hedge Luxury Hotel | Nirvana Luxury Domes',
                'Leh (5 Nights) / Nubra Valley (2 Nights) / Lakeside Glamping (2 Nights)',
                '09 Nights',
                'Luxury',
                'Luxury Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Grand Dragon Ladakh (Leh, 5 Nights) | Stone Hedge Luxury Hotel (Nubra Valley, 2 Nights) | Nirvana Luxury Domes (Lakeside Glamping, 2 Nights)',
            ),
            _hotel(
                'TRAGUIN Elite Residency | Lchang Nang Retreat | Pangong Eco Luxury Glamping',
                'Leh (5 Nights) / Nubra Valley (2 Nights) / Lakeside Glamping (2 Nights)',
                '09 Nights',
                'Ultra Luxury',
                'Luxury Glamping Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Elite Residency (Leh, 5 Nights) | Lchang Nang Retreat (Nubra Valley, 2 Nights) | Pangong Eco Luxury Glamping (Lakeside Glamping, 2 Nights)',
            ),
        ],
        inclusions=[
            _inc_included('Premium Bikes: Royal Enfield 500cc / Himalayan bikes including all fuel costs.', 1),
            _inc_included('Handpicked Hotels: Premium accommodation across all destinations.', 2),
            _inc_included('Backup Support: 4x4 Support vehicle with professional mechanic & essential spares.', 3),
            _inc_included('Tour Leader: Expert road captain with satellite communication access.', 4),
            _inc_included('Permits: All inner-line permits and Ladakh environmental fees.', 5),
            _inc_included('TRAGUIN Support: 24/7 dedicated on-ground concierge support line.', 6),
            _inc_excluded('Flight tickets to and from Leh Airport.', 7),
            _inc_excluded('Cost of damage or major parts replacement for motorcycles.', 8),
            _inc_excluded('Personal bike riding gear (Helmets, jackets, gloves, knee-guards).', 9),
            _inc_excluded('Medical insurance or emergency helicopter evacuation expenses.', 10),
            _inc_excluded('Tips, laundry, and beverage charges at properties.', 11),
        ],
    )
    return package, itinerary

def build_la_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'LA-005'
    tour_code = 'TRAGUIN-LA-005'
    title = 'Romantic Ladakh Premium Experience'
    duration = '05 Nights / 06 Days'
    slug = 'la-005-romantic-ladakh-premium-experience'
    itin_slug = 'la-005-romantic-ladakh-premium-experience-itinerary'
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
            _ph('State / Country: Ladakh, India | Category: Honeymoon / Romantic Escapes', 2),
            _ph('Destinations Covered: Leh • Sham Valley • Khardung La • Nubra Valley • Pangong Lake', 3),
            _ph('Ideal for: Couples, Honeymooners, Luxury Seekers', 4),
            _ph('Best season: June to September', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Bespoke Honeymoon FIT Holiday', 7),
            _ph('Vehicle: Dedicated spacious AC luxury vehicle for the entire route', 8),
            _ph('Meal Plan: Generous meal plan as selected in booking categories', 9),
            _ph('Route Map: Leh Arrival → Sham Valley → Khardung La → Nubra → Pangong → Chang La → Leh Departure', 10),
            _ph('TRAGUIN Signature Experience: Handpicked hotels, VIP surprise additions for couples, flexible daily pacing, and localized backup networks', 11),
            _ph('Shopping & Local Experiences: Local family-run weaving circles for authenticated pashmina wool, pure mountain apricot oils, hand-painted thangka scrolls; cozy rooftop cafes for fresh seabuckthorn juices', 12),
            _ph('Important Notes: Strict rest on Day 1 mandatory; high mountain weather shifts quickly — premium thermal layers recommended; inner-line pass generation requires ID submissions 7 days before arrival', 13),
        ],
        moods=['Honeymoon', 'Romantic', 'Luxury'],
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
        tagline='Romantic Ladakh Premium Experience • 05 Nights / 06 Days',
        overview="Welcome to an ethereal romantic journey designed to celebrate love amidst the heavens, proudly crafted by TRAGUIN. Ladakh, characterized by its majestic mountain peaks, endless deep-blue skies, and emerald lagoons, presents an otherworldly backdrop for a dreamy getaway. Our curated Luxury Ladakh Holiday Honeymoon seamlessly infuses deeply emotional, guest-facing storytelling with elite execution. Immerse yourselves in breathtaking landscapes, snuggle in handpicked hotels, and take away unforgettable memories forged in the heart of high-altitude serenity. Enjoy a refined and premium travel setup meticulously designed by TRAGUIN experts. \n\nThis private, bespoke Ladakh Honeymoon Package operates as an exclusive FIT holiday ensuring absolute intimacy for newlyweds. Travel safely inside a premium, spacious AC luxury vehicle accompanied by highly experienced mountain chauffeurs. Your romantic retreat features curated experiences, special couples' amenities, and a flexible daily cadence arranged by TRAGUIN consultants to keep your comfort uncompromised. \n\nWhy Choose a Premium Ladakh Experience for your Honeymoon? The tranquil high-desert valleys offer rare intimacy and unmatched natural beauty far away from packed tourist grids. Iconic attractions like the shimmering Pangong Lake and the historic sand dunes of Hunder represent highly sought-after, most-searched experiences for elite couples. These valleys present exceptional popular Instagram locations, making Ladakh Sightseeing a truly poetic endeavor. From cozy evenings by crackling campfires to passing through the grand top tourist places in Ladakh, TRAGUIN Ladakh Packages promise an alpine fairy-tale come to life. ",
        seo_title='LA-005 | Romantic Ladakh Premium Experience | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Ladakh honeymoon (LA-005 / TRAGUIN-LA-005): Sham Valley, Khardung La, Nubra Valley, Pangong Lake, candlelight dinner, and 4-tier accommodation. ',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Romantic landing in Leh with decorated honeymoon suite and private balcony high-tea', 1),
            _ih('Sham Valley with Magnetic Hill, Sangam, and Spituk Monastery', 2),
            _ih('Khardung La Pass to Nubra Valley with private twilight camel caravan ride at Hunder', 3),
            _ih('Pangong Lake with TRAGUIN Signature Exclusive Candlelight Dinner under starry canopy', 4),
            _ih('Chang La descent return with Thiksey Monastery and Leh Main Bazar shopping', 5),
        ],
        days=[
            _day(
                1,
                'Romantic Landing in Leh & Acclimatization Retreat',
                (
                    'Fly into the high-altitude valley of Leh, absorbing beautiful aerial mountain vistas from above. Receive an intimate, assisted premium welcome by our dedicated TRAGUIN resort representative. Check straight into your luxury honeymoon suite, specially decorated with local greeting elements. Spend the day resting smoothly together to ensure natural altitude acclimatization. '
                ),
                [
                    'Sightseeing Included: Complete leisure day for health acclimatization.',
                    'Evening Experience: Quiet high-tea on your private balcony overlooking snow-capped mountain ranges.',
                    'Overnight Stay: The Grand Dragon / Stone Hedge Hotel, Leh (Premium Luxury Stay)',
                    'Meals Included: Lunch & Dinner',
                ],
            ),
            _day(
                2,
                'Sham Valley Paths & Iconic Magnetic Hill',
                (
                    'Savor a gourmet morning breakfast before setting out along scenic routes into the Sham Valley. Experience the beautiful geological secrets of the region together, pausing frequently at curated photography points to create timeless souvenirs of your love story. '
                ),
                [
                    'Sightseeing Included: Confluence of Indus and Zanskar Rivers (Sangam), the mystical Magnetic Hill, and historical Spituk Monastery.',
                    'Food Suggestions: Authentic local barley-based snacks and organic fruit mocktails at a premium riverside café.',
                    'Overnight Stay: Premium Boutique Resort, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'Conquering Khardung La Pass to Nubra Valley Valley',
                (
                    'Ascend hand-in-hand to the legendary Khardung La Pass, one of the highest motorable passes on earth at 17,582 feet. Capture beautiful photographs against a backdrop of colorful fluttering prayer flags before dipping into the warm, dramatic vistas of Nubra Valley. '
                ),
                [
                    'Sightseeing Included: High-altitude mountain pass crossing, Diskit Monastery viewpoint.',
                    'Evening Experience: A romantic, private double-humped camel caravan ride across the silver sands of Hunder at twilight.',
                    'Overnight Stay: Luxury Desert Glamping Domes, Nubra',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'Cross-Valley Ride to the Turquoise Shores of Pangong Lake',
                (
                    'Drive along the breathtaking Shyok River valley trails toward the mesmerizing waters of Pangong Lake. Watch this high-altitude saltwater lake gracefully alter its coloration from bright turquoise to sapphire blue directly from the windows of your premium stay. '
                ),
                [
                    'Sightseeing Included: Pangong Tso shoreline exploration and classic lakeside photography points.',
                    'Evening Experience: TRAGUIN Signature Exclusive Candlelight Dinner served under a crystal-clear starry canopy.',
                    'Overnight Stay: Premium Luxury Lakeside Glamping Cottage, Pangong',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                5,
                'Chang La Descent Return to Leh & Souvenir Gathering',
                (
                    'Bid farewell to the shimmering waters of Pangong and drive back to Leh crossing the majestic Chang La Pass. Spend a relaxed afternoon strolling through local markets to find memorable tokens of your beautiful journey. '
                ),
                [
                    'Sightseeing Included: Chang La pass vistas, Thiksey Monastery exterior photo-stop.',
                    'Shopping & Local Experiences: Sift through exquisite, soft pashminas and elegant silver trinkets at Leh Main Bazar.',
                    'Overnight Stay: Premium Luxury Hotel, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                6,
                'Departure with Forever Memories',
                (
                    'Enjoy a final romantic breakfast overlooking the mountains. Pack your bags with a lifetime of beautiful, unforgettable memories. Your premium luxury vehicle will provide an assisted drop-off directly at Leh Airport for your return flight home. '
                ),
                [
                    'Meals Included: Breakfast',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Singge Palace | Hunder Desert Resort | Pangong Alpine Camps',
                'Leh (3 Nights) / Nubra Glamping (1 Night) / Pangong Luxury Camps (1 Night)',
                '05 Nights',
                'Deluxe',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Singge Palace (Leh, 3 Nights) | Hunder Desert Resort (Nubra Glamping, 1 Night) | Pangong Alpine Camps (Pangong Luxury Camps, 1 Night)',
            ),
            _hotel(
                'Hotel Zen Ladakh | Nubra Organic Retreat | Pangong Inn Luxury Wing',
                'Leh (3 Nights) / Nubra Glamping (1 Night) / Pangong Luxury Camps (1 Night)',
                '05 Nights',
                'Premium',
                'Premier Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                2,
                description='OPTION 02 – PREMIUM: Hotel Zen Ladakh (Leh, 3 Nights) | Nubra Organic Retreat (Nubra Glamping, 1 Night) | Pangong Inn Luxury Wing (Pangong Luxury Camps, 1 Night)',
            ),
            _hotel(
                'The Grand Dragon Ladakh | Stone Hedge Luxury Hotel | Nirvana Luxury Glamping',
                'Leh (3 Nights) / Nubra Glamping (1 Night) / Pangong Luxury Camps (1 Night)',
                '05 Nights',
                'Luxury',
                'Luxury Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Grand Dragon Ladakh (Leh, 3 Nights) | Stone Hedge Luxury Hotel (Nubra Glamping, 1 Night) | Nirvana Luxury Glamping (Pangong Luxury Camps, 1 Night)',
            ),
            _hotel(
                'TRAGUIN Signature Elite Villa | Lchang Nang Retreat | Pangong Eco Luxury Geodesic Domes',
                'Leh (3 Nights) / Nubra Glamping (1 Night) / Pangong Luxury Camps (1 Night)',
                '05 Nights',
                'Ultra Luxury',
                'Signature Elite Villa / Geodesic Dome',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Signature Elite Villa (Leh, 3 Nights) | Lchang Nang Retreat (Nubra Glamping, 1 Night) | Pangong Eco Luxury Geodesic Domes (Pangong Luxury Camps, 1 Night)',
            ),
        ],
        inclusions=[
            _inc_included('Premium Stays: Curated honeymoon-decorated rooms across all locations.', 1),
            _inc_included('Private Luxury Transit: Dedicated spacious AC luxury vehicle for the entire route.', 2),
            _inc_included('Meals: Generous meal plan as selected in your booking categories.', 3),
            _inc_included('Honeymoon Add-ons: One signature candlelight setup and a custom welcome cake.', 4),
            _inc_included('Permits: All inner-line permits and wildlife conservation taxes managed by TRAGUIN.', 5),
            _inc_included('TRAGUIN Support: 24/7 dedicated on-call virtual holiday concierge.', 6),
            _inc_excluded('Airfare flight tickets to and from Leh Airport.', 7),
            _inc_excluded('Entry tickets for monuments, museums, or ride fees.', 8),
            _inc_excluded('Optional adventure water sports or professional quad biking expenses.', 9),
            _inc_excluded('Mandatory comprehensive personal travel insurance policies.', 10),
            _inc_excluded('Personal expenditures such as laundry, phone calls, or room service.', 11),
        ],
    )
    return package, itinerary

def build_la_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'LA-006'
    tour_code = 'TRAGUIN-LA-006'
    title = 'Premium Ladakh Imperial Vacation'
    duration = '06 Nights / 07 Days'
    slug = 'la-006-premium-ladakh-imperial-vacation'
    itin_slug = 'la-006-premium-ladakh-imperial-vacation-itinerary'
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
            _ph('State / Country: Ladakh, India | Category: Luxury / Premium Holidays', 2),
            _ph('Destinations Covered: Leh • Sham Valley • Khardung La • Nubra Valley • Pangong Lake • Chang La', 3),
            _ph('Ideal for: Discerning Couples, Corporate VIPs, Luxury Families', 4),
            _ph('Best season: June to September', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Ultra-Premium Imperial FIT Holiday', 7),
            _ph('Vehicle: Private Toyota Innova Crysta / Luxury SUV for all routes', 8),
            _ph('Meal Plan: Curated dining as itemized in the day-by-day plan', 9),
            _ph('Route Map: Leh Arrival → Sham Valley → Khardung La → Nubra → Pangong → Chang La → Leh Heritage Walk → Departure', 10),
            _ph('TRAGUIN Signature Experience: Customized luxury vehicles driven by handpicked mountain experts, continuous oxygen setups, priority VIP seating at monastic festivals, and curated fine-dining at high altitudes', 11),
            _ph('Shopping & Local Experiences: Leh Old Bazaar — luxury grade Pashmina garments, intricate handmade silver jewelry, authentic prayer wheels, organic seabuckthorn preserves; artisan coffee roasters in historical alleyways', 12),
            _ph('Important Notes: Peaceful schedule on Day 1 mandatory; valid government ID copies required 10 days before arrival; high mountain passes subject to temporary weather-related shifts', 13),
        ],
        moods=['Luxury', 'Premium', 'Imperial'],
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
        tagline='Premium Ladakh Imperial Vacation • 06 Nights / 07 Days',
        overview='Welcome to an ethereal paradise of high-altitude grandeur, exclusively designed and flawlessly executed by TRAGUIN. Immerse your senses in a terrain sculpted with breathtaking landscapes, emerald-tinted high altitude rivers, and deep cobalt-blue alpine lakes that transcend conventional beauty. This Premium Ladakh Experience is curated to offer an impeccable balance of exploration and deep relaxation. Journey past iconic attractions, sleep soundly inside elite handpicked hotels, and cherish unforgettable memories within the Himalayan crown. Every single detail is personalized for you to enjoy the best time to visit Ladakh in supreme imperial style. \n\nThis flagship Best Ladakh Tour Package caters specifically to travelers who seek raw geographical marvels coupled with meticulous hospitality arrangements. Travel in ultra-premium private luxury vehicles, enjoy flexibility across daily excursions, and indulge in full custom meal configurations. From oxygen-equipped premium stays to customized high-altitude safety parameters, our expert travel consultants handle every detail to ensure flawless implementation. \n\nWhy Choose a Premium Ladakh Experience? Ladakh remains an aspirational jewel in luxury experiential tourism. Landmark locations such as the iconic Thiksey Monastery, the sand dunes of Hunder, and the timeless serenity of Pangong Tso serve as highly searched experiences globally. It provides an exceptional backdrop as a luxury honeymoon package or an elite family tour due to its absolute privacy, majestic popular Instagram locations, and deeply spiritual culture. From exploring ancient monastic relics to standing atop the highest motorable alpine highways, our TRAGUIN Ladakh Packages encapsulate unparalleled luxury travel standards alongside breathtaking scenic beauty. ',
        seo_title='LA-006 | Premium Ladakh Imperial Vacation | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Ladakh imperial vacation (LA-006 / TRAGUIN-LA-006): Sham Valley, Khardung La, Nubra, Pangong, Chang La, and 4-tier ultra-premium accommodation. ',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Imperial welcome to Leh with ultra-luxury suite and custom menu consultation', 1),
            _ih('Sham Valley cultural monuments with Magnetic Hill, Gurudwara Pathar Sahib, and Sangam', 2),
            _ih('Khardung La summit to Nubra Valley with private Bactrian Camel safari at Hunder', 3),
            _ih('Pangong Lake via Shyok gorges with private lakeside high-tea setup', 4),
            _ih('Royal Leh heritage walk with TRAGUIN Farewell Gala Banquet', 5),
        ],
        days=[
            _day(
                1,
                'Imperial Welcome to Leh & Oxygen-Acclimatization Leisure',
                (
                    'Arrive at Leh Airport, where your private chauffeur welcomes you with customized amenities. Benefit from an assisted check-in into your ultra-luxury hotel suite. The first day is strictly dedicated to restful acclimatization to the alpine environment, allowing your body to seamlessly transition to high altitudes while enjoying elite property luxuries. '
                ),
                [
                    'Sightseeing Included: Complete leisure inside premium stays, acclimatization rest.',
                    'Evening Experience: Private orientation and custom menu consultation by our resident TRAGUIN experts.',
                    "Overnight Stay: The Grand Dragon / The Ultimate Traveller's Luxury Camp, Leh",
                    'Meals Included: Lunch & Dinner',
                ],
            ),
            _day(
                2,
                'Cultural Monuments of Sham Valley & Confluence Cruise',
                (
                    "Embark on a relaxed excursion through scenic routes bordering the Indus River. Witness unique natural anomalies and iconic spiritual structures that capture the rich cultural history of Ladakh's indigenous legacy. "
                ),
                [
                    'Sightseeing Included: The mystical Magnetic Hill, the sacred Gurudwara Pathar Sahib, and the breathtaking Sangam confluence (Indus & Zanskar rivers).',
                    'Photography Points: Hall of Fame panoramic vistas and high-altitude river overlook decks.',
                    'Overnight Stay: Luxury Boutique Resort, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'Khardung La Summit Pass to the Coconut Sands of Nubra Valley',
                (
                    'Board your premium luxury vehicle to climb the world-famous Khardung La Pass, ascending to a legendary 17,582 feet. Capture spectacular vistas of snow-capped mountains before heading down into the desert landscape of Nubra Valley. '
                ),
                [
                    'Sightseeing Included: Khardung La top, historic Diskit Monastery with its majestic colossal Buddha statue.',
                    'Evening Experience: A premium, private double-humped Bactrian Camel safari across the stark white sand dunes of Hunder.',
                    'Overnight Stay: Lchang Nang Retreat / Stone Hedge Luxury Villa, Nubra',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                4,
                'Nubra Valley to Turquoise Pangong Lake via the Shyok Gorges',
                (
                    'Drive along the dramatic, winding canyons of the Shyok River route. Emerge onto the shores of the world-famous Pangong Lake, an endorheic lake celebrated for changing its colors from crystalline turquoise to royal sapphire under the high-altitude sun. '
                ),
                [
                    'Sightseeing Included: Shyok valley route sightseeing, western banks of Pangong Lake.',
                    'Evening Experience: Private lakeside high-tea setup featuring luxury gourmet pastries and bespoke snacks.',
                    'Overnight Stay: Luxury Premium Glamping Domes / Luxury Cottages, Pangong',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                5,
                'Sunrise at Pangong Lake to Leh via Chang La Pass',
                (
                    'Awake early to admire a brilliant sunrise shifting over the sparkling lake waters. After an open-air breakfast, travel back towards Leh, crossing the high-altitude Chang La pass while enjoying the raw natural beauty of the surrounding wilderness. '
                ),
                [
                    "Sightseeing Included: Chang La summit, Thiksey Monastery (reminiscent of Tibet's Potala Palace).",
                    'Local Experiences: Direct interaction with local monks during afternoon prayers.',
                    'Overnight Stay: Ultra-Luxury Hotel Suite, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                6,
                'Curated Royal Leh Heritage Walk & Farewell Banquet',
                (
                    'Spend a relaxing day exploring the rich historical layers of Leh. Browse exclusive heritage boutiques for authentic high-end collectibles or indulge in relaxing spa experiences designed to soothe your senses after your mountain journey. '
                ),
                [
                    'Sightseeing Included: Leh Palace, Shanti Stupa sunset viewpoint, and the old historic craft quarters.',
                    'Evening Experience: Exclusive TRAGUIN Farewell Gala Banquet featuring traditional music and a premium multi-course menu.',
                    'Overnight Stay: Ultra-Luxury Hotel Suite, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                7,
                'Departure with Unforgettable Memories',
                (
                    'Enjoy a final morning meal while gazing at the pristine Stok mountain peaks. Your chauffeur will provide a comfortable private transfer back to Leh Airport for your return flight home, concluding your premium journey filled with unforgettable memories. '
                ),
                [
                    'Meals Included: Breakfast',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Singge Palace | Hunder Resort Oasis | Pangong Retreat Camps',
                'Leh (4 Nights) / Nubra Valley Luxury (1 Night) / Pangong Glamping Domes (1 Night)',
                '06 Nights',
                'Deluxe',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Singge Palace (Leh, 4 Nights) | Hunder Resort Oasis (Nubra Valley, 1 Night) | Pangong Retreat Camps (Pangong, 1 Night)',
            ),
            _hotel(
                'The Zen Ladakh (Premium Room) | Nubra Organic Luxury Tents | Pangong Inn Premium Wing',
                'Leh (4 Nights) / Nubra Valley Luxury (1 Night) / Pangong Glamping Domes (1 Night)',
                '06 Nights',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                2,
                description='OPTION 02 – PREMIUM: The Zen Ladakh (Premium Room) (Leh, 4 Nights) | Nubra Organic Luxury Tents (Nubra Valley, 1 Night) | Pangong Inn Premium Wing (Pangong, 1 Night)',
            ),
            _hotel(
                'The Grand Dragon Ladakh | Stone Hedge Luxury Hotel | Nirvana Premium Domes',
                'Leh (4 Nights) / Nubra Valley Luxury (1 Night) / Pangong Glamping Domes (1 Night)',
                '06 Nights',
                'Luxury',
                'Luxury Room',
                'JAI (All Meals Included)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Grand Dragon Ladakh (Leh, 4 Nights) | Stone Hedge Luxury Hotel (Nubra Valley, 1 Night) | Nirvana Premium Domes (Pangong, 1 Night)',
            ),
            _hotel(
                'TRAGUIN Imperial Residency Suite | Lchang Nang Retreat (Luxury Villa) | Pangong Eco Luxury Glamping Domes',
                'Leh (4 Nights) / Nubra Valley Luxury (1 Night) / Pangong Glamping Domes (1 Night)',
                '06 Nights',
                'Ultra Luxury',
                'Imperial Residency Suite / Luxury Villa',
                'Curated Wellness Dine-Around',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Imperial Residency Suite (Leh, 4 Nights) | Lchang Nang Retreat (Luxury Villa) (Nubra Valley, 1 Night) | Pangong Eco Luxury Glamping Domes (Pangong, 1 Night)',
            ),
        ],
        inclusions=[
            _inc_included('Handpicked Hotels: Ultra-premium accommodations with complete oxygen support.', 1),
            _inc_included('Luxury Transfers: Private Toyota Innova Crysta / Luxury SUV for all routes.', 2),
            _inc_included('Curated Dining: Meal setups as itemized in the day-by-day plan.', 3),
            _inc_included('Inner Line Permits: Seamless processing of all environmental and wildlife fees.', 4),
            _inc_included('TRAGUIN Support: 24/7 localized on-ground concierge assistance.', 5),
            _inc_included('Exclusive Amenities: Welcome baskets, specialized oxygen test kits, and premium travel tokens.', 6),
            _inc_excluded('Domestic or international air tickets to and from Leh.', 7),
            _inc_excluded('Expenses arising from unplanned itinerary modifications due to weather changes.', 8),
            _inc_excluded('Premium beverages, laundry services, or mini-bar charges.', 9),
            _inc_excluded('Voluntary tips for local porters, drivers, or tour guides.', 10),
            _inc_excluded('Any service not explicitly highlighted in the official inclusions layout.', 11),
        ],
    )
    return package, itinerary

def build_la_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'LA-007'
    tour_code = 'TRAGUIN-LA-007'
    title = 'Senior Citizen Leisure Leh Vacation'
    duration = '05 Nights / 06 Days'
    slug = 'la-007-senior-citizen-leisure-leh-vacation'
    itin_slug = 'la-007-senior-citizen-leisure-leh-vacation-itinerary'
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
            _ph('State / Country: Ladakh, India | Category: Senior Citizen Leisure Tour', 2),
            _ph('Destinations Covered: Leh • Sham Valley • Indus Valley • Nimmu Confluence', 3),
            _ph('Ideal for: Senior Citizens, Mature Travelers, Relaxed Families', 4),
            _ph('Best season: May to September', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Senior-Friendly Leisure FIT Tour (Leh Base)', 7),
            _ph('Vehicle: Private luxury AC Innova/Crysta with customized soft suspension', 8),
            _ph('Meal Plan: Light, nutritious, non-spicy multi-cuisine dishes daily', 9),
            _ph('Route Map: Leh Arrival → Hall of Fame & Spituk → Sham Valley & Sangam → Indus Valley Heritage → Leh Departure', 10),
            _ph('TRAGUIN Signature Experience: Daily health monitoring check-ins, medical oxygen backups, slower transit speeds, and verified ground-floor room assignments', 11),
            _ph('Shopping & Local Experiences: Leh Main Bazar — cloud-soft pashmina shawls, sweet organic dried apricots, traditional wooden prayer wheels, healing local herbal tea leaves', 12),
            _ph("Important Notes: Complete rest on Day 1 mandatory; drink plenty of warm water throughout; daily timings completely flexible to senior guests' rest preferences", 13),
        ],
        moods=['Senior Citizens', 'Leisure', 'Family'],
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
        tagline='Senior Citizen Leisure Leh Vacation • 05 Nights / 06 Days',
        overview='Welcome to a peaceful, soul-stirring Himalayan retreat meticulously structured by TRAGUIN. Ladakh, renowned for its breathtaking landscapes, pristine fresh air, and deep spiritual heritage, is an extraordinary destination when explored at an unhurried, graceful pace. Designed specifically as a senior citizen family tour, this luxury Ladakh holiday replaces frantic travel loops with pure relaxation, curated experiences, and top-tier comfort. Stay in premium handpicked hotels, explore iconic attractions with step-free assistance, and cultivate unforgettable memories across the spectacular scenic beauty of Leh. \n\nThis custom Premium Ladakh Experience prioritizes absolute guest safety, steady acclimatization, and zero-stress pacing. Your journey features a dedicated luxury vehicle with smooth suspension, expert local guides versed in elder assistance, a healthy personalized meal plan, and round-the-clock oxygen monitoring. Every detail is curated by TRAGUIN experts to provide flat walking pathways and seamless transitions, ensuring an enchanting vacation for senior travelers. \n\nWhy choose a Leisure Ladakh Family Tour? Leh and its surrounding valleys offer incredible cultural immersion without the high-altitude strain of rugged cross-country passes. Top tourist places in Ladakh, including the peaceful Spituk Monastery, Hall of Fame, and the gentle scenic banks of the Indus River, are perfectly accessible. These historical sanctuaries provide popular Instagram locations and deep spiritual tranquility, making the best time to visit Ladakh a fulfilling cultural journey for seasoned travelers who cherish heritage, photography points, and localized culinary delights. ',
        seo_title='LA-007 | Senior Citizen Leisure Leh Vacation | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days senior citizen Ladakh tour (LA-007 / TRAGUIN-LA-007): Sham Valley, Indus Valley, Nimmu Confluence, step-free sightseeing, and 4-tier Leh-only accommodation. ',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Assisted arrival with in-room medical wellness check and gentle orientation', 1),
            _ih('Leisure sightseeing to Hall of Fame Museum and Spituk Monastery lower grounds', 2),
            _ih('Sham Valley exploration with Magnetic Hill and Nimmu River Confluence (Sangam)', 3),
            _ih('Indus Valley heritage tour with Thiksey Monastery lower court and Shey Palace', 4),
            _ih('Souvenir gathering at Leh Main Bazar with TRAGUIN Farewell Dinner and folk sitar performance', 5),
        ],
        days=[
            _day(
                1,
                'Assisted Arrival in Leh - Complete Acclimatization & Rest',
                (
                    'Step off your flight at Kushok Bakula Rimpochee Airport, Leh, where a dedicated TRAGUIN local coordinator will welcome you with a gentle silk scarf greet. Transfer via private luxury vehicle to your handpicked premium resort. Today is strictly reserved for complete rest and oxygen-level synchronization to guarantee total physical comfort. '
                ),
                [
                    'Sightseeing Included: Complete physical rest within your luxury room premises.',
                    'Evening Experience: In-room medical wellness check and a gentle orientation talk by our travel consultant.',
                    'Overnight Stay: The Grand Dragon / Stone Hedge Luxury Hotel, Leh (Premium Stay)',
                    'Meals Included: Lunch & Dinner',
                ],
            ),
            _day(
                2,
                'Leisure Sightseeing - Hall of Fame & Spituk Monastery',
                (
                    'Awake to spectacular mountain views and enjoy a warm, wholesome breakfast. Today features a very gentle sightseeing route through the smooth, flat-terraced tourist places in Ladakh, minimizing steps or steep inclines. '
                ),
                [
                    'Sightseeing Included: The historic Hall of Fame Museum (fully assisted) and the scenic lower grounds of Spituk Monastery.',
                    'Photography Points: Beautiful flat lookouts across the snow-capped Stok Kangri range.',
                    'Overnight Stay: Premium Luxury Hotel, Leh',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                3,
                'Sham Valley Exploration - Confluence & Magnetic Hill',
                (
                    'Embark on a beautiful drive along the smooth, wide tarmac of the Srinagar-Leh highway. Relax as your luxury vehicle glides past breathtaking landscapes toward Nimmu, where the Indus and Zanskar rivers elegantly meet. '
                ),
                [
                    'Sightseeing Included: The mysterious Magnetic Hill phenomenon and the Nimmu River Confluence (Sangam).',
                    'Local Experiences: A quiet, peaceful hot lunch at a curated garden resort along the highway.',
                    'Overnight Stay: Premium Luxury Hotel, Leh',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                4,
                'Indus Valley Heritage - Thiksey Monastery Lower Court & Shey Palace',
                (
                    'Discover the spiritual heart of Ladakh with a relaxed excursion along the Indus Valley. Visit the lower, step-free court spaces of Thiksey Monastery, marveling at its architectural grandeur resembling the Potala Palace of Tibet. '
                ),
                [
                    'Sightseeing Included: Shey Palace photography grounds, Thiksey Monastery lower complex, and Sindhu Ghat.',
                    'Optional Activities: A mild, flat stroll around the peaceful lotus ponds near Shey.',
                    'Overnight Stay: Premium Luxury Hotel, Leh',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                5,
                'Souvenir Gathering, Royal Palace Cafe & Farewell Gala',
                (
                    'Spend a delightful day entirely at your own leisure. Take an effortless, slow-paced stroll through the clean, vehicle-free lanes of Leh Main Bazar, interacting with warm local artisans and gathering traditional tokens of your journey. '
                ),
                [
                    'Shopping & Cafes: High-tea at a premium local cafe serving fresh local sea-buckthorn fruit juices.',
                    'Evening Experience: A celebratory TRAGUIN Farewell Dinner accompanied by a gentle Ladakhi folk sitar performance.',
                    'Overnight Stay: Premium Luxury Hotel, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                6,
                'Departure from Leh',
                (
                    'Enjoy your final breakfast surrounded by clear blue Himalayan skies. Your dedicated luxury vehicle provides a smooth transfer back to Leh Airport for your comfortable journey home, leaving you with unforgettable memories. '
                ),
                [
                    'Meals Included: Breakfast',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Singge Palace',
                'Leh (5 Nights)',
                '05 Nights',
                'Deluxe',
                'Deluxe Premium Room (Elevator Access)',
                'Breakfast & Dinner',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Singge Palace (Leh, 5 Nights) | Deluxe Premium Room (Elevator Access) | Breakfast & Dinner',
            ),
            _hotel(
                'Hotel Zen Ladakh',
                'Leh (5 Nights)',
                '05 Nights',
                'Premium',
                'Luxury Ground Floor Suite',
                'Breakfast & Dinner',
                5,
                2,
                description='OPTION 02 – PREMIUM: Hotel Zen Ladakh (Leh, 5 Nights) | Luxury Ground Floor Suite | Breakfast & Dinner',
            ),
            _hotel(
                'The Grand Dragon Ladakh',
                'Leh (5 Nights)',
                '05 Nights',
                'Luxury',
                'Executive Mountain View Suite',
                'Full Meals (All Included)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Grand Dragon Ladakh (Leh, 5 Nights) | Executive Mountain View Suite | Full Meals (All Included)',
            ),
            _hotel(
                'TRAGUIN Elite Mountain Residency',
                'Leh (5 Nights)',
                '05 Nights',
                'Ultra Luxury',
                'Signature Imperial Royal Wing',
                'Curated Wellness Dine-Around',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Elite Mountain Residency (Leh, 5 Nights) | Signature Imperial Royal Wing | Curated Wellness Dine-Around',
            ),
        ],
        inclusions=[
            _inc_included('Handpicked Hotels: Senior-friendly luxury stays with continuous heating & elevators.', 1),
            _inc_included('Curated Meals: Light, nutritious, non-spicy multi-cuisine dishes daily.', 2),
            _inc_included('Premium Transfers: Private luxury AC Innova/Crysta with customized soft suspension.', 3),
            _inc_included('Medical Kit: On-board oxygen cylinder systems inside the vehicle at all times.', 4),
            _inc_included('VIP Sightseeing: Seamless, step-free access permits for all iconic attractions.', 5),
            _inc_included('TRAGUIN Support: 24/7 dedicated local concierge assistance line.', 6),
            _inc_excluded('Airfare flight tickets to and from Leh Airport.', 7),
            _inc_excluded('Personal tips, porterage, and laundry services.', 8),
            _inc_excluded('Entry fees for cameras or specialized historical museums.', 9),
            _inc_excluded('Medical insurance or emergency air evacuation protocols.', 10),
            _inc_excluded('Anything not explicitly outlined in the active inclusions catalog.', 11),
        ],
    )
    return package, itinerary

def build_la_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'LA-008'
    tour_code = 'TRAGUIN-LA-008'
    title = 'Women Riders Ladakh Expedition'
    duration = '08 Nights / 09 Days'
    slug = 'la-008-women-riders-ladakh-expedition'
    itin_slug = 'la-008-women-riders-ladakh-expedition-itinerary'
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
            _ph('State / Country: Ladakh, India | Category: Female Only / Women Riders', 2),
            _ph('Destinations Covered: Leh • Sham Valley • Nubra Valley • Hunder • Pangong Lake • Chang La', 3),
            _ph('Ideal for: Solo Female Travelers, Women Biking Groups, Adventurers', 4),
            _ph('Best season: June to September', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Premium All-Women Guided Motorcycle Expedition', 7),
            _ph('Vehicle: Royal Enfield Himalayan / Scram models with 4x4 support utility vehicle', 8),
            _ph('Meal Plan: Premium meals with curated organic menu alternatives across all stays', 9),
            _ph('Route Map: Leh → Sham Valley → Khardung La → Nubra → Turtuk → Pangong → Chang La → Leh Departure', 10),
            _ph('TRAGUIN Signature Experience: Comprehensive satellite tracking links for family members, curated organic menu alternatives, and exclusive access to certified female wellness doctors stationed on-ground in Leh', 11),
            _ph("Shopping & Local Experiences: Leh Tibetan Market — hand-carved silver jewelry, pure turquoise stones, authentic Pashmina stoles, aromatic organic dried apricots; local women's weaving collectives for handmade woolen socks and beanies", 12),
            _ph('Important Notes: Strict rest on Day 1 mandatory — no riding until medical clearance; valid permanent Indian two-wheeler driving license with gear endorsement required; final route access at sole discretion of road captain', 13),
        ],
        moods=['Women Riders', 'Adventure', 'Biking'],
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
        tagline='Women Riders Ladakh Expedition • 08 Nights / 09 Days',
        overview='Welcome to an empowering journey across the roof of the world, proudly curated by TRAGUIN. Ladakh, with its dramatic mountain passes, pristine azure lakes, and deep spiritual legacy, forms the canvas for your ultimate sisterhood adventure. Designed exclusively for fearless women riders, this Luxury Ladakh Holiday blends pure high-altitude thrill with the absolute safety, luxury, and warmth of our premium stays. Reclaim the open highways, capture unforgettable memories, and let the sheer scenic beauty of Ladakh ignite your spirit. Backed by handpicked hotels and comprehensive expert escorts, this is the Premium Ladakh Experience you have been waiting for. \n\nThis elite Ladakh Honeymoon & Women Expedition is structured specifically to provide a perfect harmony of adventurous grit and premium hospitality. Navigating through rugged high passes demands absolute security; hence, our package features specialized all-women mechanical and logistical backups, premium medical kits, and an expert female tour leader. Unwind inside handpicked hotels, experience curated wellness evenings, and travel with absolute peace of mind. \n\nWhy choose a Luxury Ladakh Holiday for Women Riders? Ladakh represents the global standard for high-altitude achievement. Conquering iconic attractions like Khardung La and tracking the hypnotic shifts of Pangong Tso Lake rank among the most searched experiences in contemporary exploration. The endless sand vistas of Hunder and the dramatic high gorges provide popular Instagram locations that are perfect for capturing your milestone achievements. From exploring quiet prayer halls in ancient cliffside monasteries to immersive shopping for local silver crafts, our custom TRAGUIN Ladakh Packages deliver deep cultural connection paired with absolute premium execution. ',
        seo_title='LA-008 | Women Riders Ladakh Expedition | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days women riders Ladakh expedition (LA-008 / TRAGUIN-LA-008): Sham Valley, Nubra, Hunder, Pangong, Chang La, Royal Enfield bikes, female road captain. ',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Welcome circle, bike fitment check, and comprehensive safety mapping with TRAGUIN Experts', 1),
            _ih('Sham Valley cruise with Magnetic Hill, Sangam, and Gurudwara Pathar Sahib', 2),
            _ih('Khardung La conquest to Nubra Valley with golden sunset camel ride at Hunder', 3),
            _ih('Turtuk Balti sisterhood village walk with local handloom setups', 4),
            _ih('Off-road Shyok route to Pangong with private bonfire, music, and hot chocolate', 5),
        ],
        days=[
            _day(
                1,
                'Arrival in Leh - Stepping into the Highlands & Acclimatization',
                (
                    'Land at Kushok Bakula Rimpochee Airport, Leh. Receive a warm premium welcome by the specialized TRAGUIN liaison team and transfer via private luxury coach to your handpicked premium stay. The entire day is dedicated to vital oxygen acclimatization to ensure a flawless and safe expedition ahead. '
                ),
                [
                    'Sightseeing Included: Rest and leisure within hotel premises.',
                    'Evening Experience: Welcome circle, bike fitment check, and comprehensive safety mapping with TRAGUIN Experts.',
                    'Overnight Stay: The Grand Dragon / Zen Ladakh, Leh (Premium Luxury Stay)',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                2,
                'Sham Valley Cruise - Trail Testing & Spiritual Landmarks',
                (
                    "Rev up your allotted premium motorcycles for an exhilarating acclimatization cruise down the smooth tarmac of the Srinagar-Leh highway. Test your riding gears, feel the bike's weight distribution, and explore the mystical Sham Valley landscape. "
                ),
                [
                    'Sightseeing Included: Magnetic Hill, Sangam (Indus & Zanskar River confluence), and Gurudwara Pathar Sahib.',
                    'Photography Points: Incredible contrast views of mountain rivers meeting sandstone canyons.',
                    'Overnight Stay: Premium Luxury Hotel, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'Climbing the Mighty Khardung La to Nubra Valley',
                (
                    'A milestone day! Ride up the steep, winding mountain switchbacks to conquer the legendary Khardung La Pass at 17,582 feet. Celebrate your success at the top before descending into the warm, dramatic desert basin of the Nubra Valley. '
                ),
                [
                    'Sightseeing Included: Khardung La peak stop, Diskit Monastery and its majestic open-air Maitreya Buddha statue.',
                    'Evening Experience: Double-humped camel desert ride across Hunder sand dunes during a magnificent golden sunset.',
                    'Overnight Stay: Luxury Organic Glamping Retreat, Nubra',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'Historic Turtuk Village - Exploring the Balti Sisterhood',
                (
                    'Ride deep along the flowing Shyok River to explore Turtuk, a picturesque village nestled right near the Line of Control. Walk through lush apricot orchards, interact with the local Balti women, and understand their rich cultural history. '
                ),
                [
                    'Sightseeing Included: Turtuk Balti Museum, traditional stone villages, and local handloom setups.',
                    'Food Suggestions: Freshly harvested local apricot desserts and herbal mountain tea at a village cafe.',
                    'Overnight Stay: Luxury Glamping Retreat, Nubra',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'Off-Road Adventure: Nubra to Turquoise Pangong Lake',
                (
                    'Conquer challenging riverbeds and off-road tracks along the rugged Shyok route. Arrive at the breathtaking Pangong Tso Lake, an expansive saltwater jewel that reflects vivid shades of sapphire blue right against the backdrop of massive Tibetan peaks. '
                ),
                [
                    'Sightseeing Included: Shyok valley landscapes, Pangong Lake panoramic shore trail.',
                    'Evening Experience: Private bonfire setup right by the lakeside with music, hot chocolate, and endless starlit skies.',
                    'Overnight Stay: Ultra Luxury Geodesic Domes, Pangong Lake',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                6,
                'Pangong Lake to Leh via the Majestic Chang La Pass',
                (
                    'Wake up early to capture the beautiful sunrise reflecting off the glassy lake surface. Mount your bikes to scale Chang La Pass, the third-highest motorable highway pass in the world, before descending smoothly back into Leh. '
                ),
                [
                    "Sightseeing Included: Chang La Pass crossing, Thiksey Monastery (resembling Tibet's Potala Palace).",
                    'Shopping: Stop at a local Cooperative Society for authentic high-quality winter fabrics.',
                    'Overnight Stay: Premium Luxury Hotel, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                7,
                'Discovering the Spirit of Leh & Souvenir Tracks',
                (
                    'Give your bikes a rest today. This day is specially curated for slow exploration. Stroll through old town streets, photograph historic architecture, and reward yourself after the long ride with relaxing premium wellness therapies. '
                ),
                [
                    'Sightseeing Included: Leh Palace, Shanti Stupa sunset viewpoint, and local organic gardens.',
                    'Evening Experience: Traditional Ladakhi dress styling and group portrait photography session.',
                    'Overnight Stay: Premium Luxury Hotel, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                8,
                'Leisure Day & The TRAGUIN Farewell Gala',
                (
                    'A completely flexible day to unwind, journal, or visit cozy mountain cafes. In the evening, gather for a grand celebration dinner to mark the successful completion of your high-altitude motorcycle expedition. '
                ),
                [
                    'Evening Experience: Signature TRAGUIN Farewell Gala Dinner with certificates of achievement and local live acoustic folk music.',
                    'Overnight Stay: Premium Luxury Hotel, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                9,
                'Bidding Farewell to the Land of High Passes',
                (
                    'Savor your final breakfast with stunning views of the snow-capped Stok range. Pack your bags full of empowering memories and lifelong bonds. Enjoy an assisted luxury transfer to Leh Airport for your return flight home. '
                ),
                [
                    'Meals Included: Breakfast',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Singge Palace | Hunder Desert Camp | Pangong Wooden Cottages',
                'Leh (5 Nights) / Nubra Valley Glamping (2 Nights) / Pangong Luxury Domes (1 Night)',
                '08 Nights',
                'Deluxe',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Singge Palace (Leh, 5 Nights) | Hunder Desert Camp (Nubra Valley, 2 Nights) | Pangong Wooden Cottages (Pangong, 1 Night)',
            ),
            _hotel(
                'The Zen Ladakh Resort | Nubra Organic Retreat vills | Pangong Inn Premium Wing',
                'Leh (5 Nights) / Nubra Valley Glamping (2 Nights) / Pangong Luxury Domes (1 Night)',
                '08 Nights',
                'Premium',
                'Premier Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                2,
                description='OPTION 02 – PREMIUM: The Zen Ladakh Resort (Leh, 5 Nights) | Nubra Organic Retreat vills (Nubra Valley, 2 Nights) | Pangong Inn Premium Wing (Pangong, 1 Night)',
            ),
            _hotel(
                'The Grand Dragon Ladakh | Stone Hedge Luxury Hotel | Martsemik Luxury Domes',
                'Leh (5 Nights) / Nubra Valley Glamping (2 Nights) / Pangong Luxury Domes (1 Night)',
                '08 Nights',
                'Luxury',
                'Luxury Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Grand Dragon Ladakh (Leh, 5 Nights) | Stone Hedge Luxury Hotel (Nubra Valley, 2 Nights) | Martsemik Luxury Domes (Pangong, 1 Night)',
            ),
            _hotel(
                'TRAGUIN Exclusive Residency | Lchang Nang Eco Retreat | Pangong Eco Luxury Glamping Domes',
                'Leh (5 Nights) / Nubra Valley Glamping (2 Nights) / Pangong Luxury Domes (1 Night)',
                '08 Nights',
                'Ultra Luxury',
                'Exclusive Residency / Glamping Dome',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Exclusive Residency (Leh, 5 Nights) | Lchang Nang Eco Retreat (Nubra Valley, 2 Nights) | Pangong Eco Luxury Glamping Domes (Pangong, 1 Night)',
            ),
        ],
        inclusions=[
            _inc_included('Premium Bikes: Royal Enfield Himalayan / Scram models with fuel included.', 1),
            _inc_included('Handpicked Hotels: Elite, highly rated safety-certified properties.', 2),
            _inc_included('Technical Escort: 4x4 Support utility vehicle with mechanic, spares, and tools.', 3),
            _inc_included('Expert Captain: Professional female road captain leading the trail.', 4),
            _inc_included('Medical Safety: Oxygen cylinders, oximeters, and trauma kits on board.', 5),
            _inc_included('TRAGUIN Support: 24/7 localized on-ground concierge assistance.', 6),
            _inc_excluded('Personal domestic or international airline tickets.', 7),
            _inc_excluded('Personal riding gear (helmets with Bluetooth, armored jackets, knee guards).', 8),
            _inc_excluded('Motorcycle security deposits or damage costs for major parts.', 9),
            _inc_excluded('Medical emergencies or remote helicopter evacuation charges.', 10),
            _inc_excluded('Standard laundry, phone bills, or premium mini-bar utilization.', 11),
        ],
    )
    return package, itinerary

def build_la_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'LA-009'
    tour_code = 'TRAGUIN-LA-009'
    title = 'Premium Ladakh Family Tour & Monastery Trail'
    duration = '05 Nights / 06 Days'
    slug = 'la-009-premium-ladakh-family-tour-monastery-trail'
    itin_slug = 'la-009-premium-ladakh-family-tour-monastery-trail-itinerary'
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
            _ph('State / Country: Ladakh, India | Category: Family Tour / Monastery Trail', 2),
            _ph('Destinations Covered: Leh • Sham Valley • Thiksey • Hemis • Pangong Lake', 3),
            _ph('Ideal for: Families, Cultural Explorers, Leisure Travelers', 4),
            _ph('Best season: May to October', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Premium Family FIT Monastery Trail', 7),
            _ph('Vehicle: Dedicated private luxury AC vehicles (Innova / Tempo Traveler)', 8),
            _ph('Meal Plan: Generous gourmet meal frameworks across all destinations', 9),
            _ph('Route Map: Leh Arrival → Sham Valley → Thiksey & Hemis → Pangong via Chang La → Leh Departure', 10),
            _ph('TRAGUIN Signature Experience: Medical-grade oxygen canisters in private transport fleet, customized menus crafted around regional preferences, and completely step-free accessibility mappings', 11),
            _ph('Shopping & Local Experiences: Leh Main Bazar — premium pashmina stoles, beautiful local prayer wheels, handmade Tibetan carpets, sweet organic dried apricots; premium local cafes serving fresh seabuckthorn tea', 12),
            _ph('Important Notes: Summer months May through October offer most stable conditions; inner line permits handled by TRAGUIN in advance; complete resting protocols on Day 01 mandatory', 13),
        ],
        moods=['Family', 'Cultural', 'Monastery'],
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
        tagline='Premium Ladakh Family Tour & Monastery Trail • 05 Nights / 06 Days',
        overview='Welcome to an ethereal family pilgrimage across the roof of the world, meticulously crafted by TRAGUIN. Ladakh, a land of sacred chants, multi-tiered historic sanctuaries, and breathtaking landscapes, offers an exceptional destination for your next luxury family holiday. Our custom-designed itinerary blends spiritual heritage with complete leisure, unfolding majestic scenic beauty and immersive experiences for every family member. Stay in handpicked hotels, absorb pristine iconic attractions, and create unforgettable memories through curated experiences planned beautifully by your premium travel consultants. \n\nThis premium Ladakh Family Tour is optimized as an FIT private route focusing on absolute travel comfort, slow unhurried pacing, and premium family-sized luxury vehicles. From spectacular high-altitude lakes to sacred ancestral shrines, your travel dates will showcase professional destination management, a highly nutritious meal plan, and smooth, curated interaction guidelines managed entirely by TRAGUIN on-ground representatives. \n\nWhy Choose a Premium Ladakh Experience for Families? Ladakh provides a deeply peaceful atmosphere safe for multi-generational families. Top tourist places in Ladakh feature centuries-old architectural wonders like Thiksey and Hemis monasteries, alongside highly sought-after natural marvels like the magnetic hills. Pangong Lake serves as a beautiful backdrop for popular Instagram locations, making Ladakh Sightseeing highly searched for luxury vacations. From local souvenir markets to absolute spiritual peace, our TRAGUIN Ladakh Packages seamlessly stitch adventure with total premium relaxation. ',
        seo_title='LA-009 | Premium Ladakh Family Tour & Monastery Trail | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Ladakh family monastery tour (LA-009 / TRAGUIN-LA-009): Sham Valley, Thiksey, Hemis, Pangong Lake, and 4-tier handpicked accommodation. ',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Assisted arrival with family introductory discussion and acclimatization day', 1),
            _ih('Sham Valley trail with Hall of Fame, Magnetic Hill, Sangam, and Gurudwara Pathar Sahib', 2),
            _ih('Sacred trails to Thiksey Monastery and Hemis Treasury Museum with Shey Palace', 3),
            _ih('Pangong Lake via Chang La Pass with private lakeside tea and family stargazing', 4),
            _ih('TRAGUIN Farewell Family Dinner with local musical storytelling presentations', 5),
        ],
        days=[
            _day(
                1,
                'Assisted Arrival in Leh - Mandatory Acclimatization Deluxe',
                (
                    'Arrive at Leh Airport, where you will experience a warm premium greeting by our dedicated TRAGUIN coordinator. Transfer in comfort to your luxurious handpicked hotel. Today is explicitly dedicated to essential rest and low activity for flawless altitude acclimatization, ensuring the health and safety of your entire family. '
                ),
                [
                    'Sightseeing Included: Relaxed indoor environment acclimatization.',
                    'Evening Experience: Leisure family introductory discussion with our local travel consultant team.',
                    'Overnight Stay: Grand Dragon / The Zen Ladakh (Premium Luxury Stay)',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                2,
                'Sham Valley Trail - Iconic Monuments & Confluences',
                (
                    'Enjoy a relaxed morning breakfast. Your family will set off on a smooth, scenic route along the Srinagar-Leh highway, revealing pristine, barren canyons and beautiful mountain geography perfectly suitable for family photography points. '
                ),
                [
                    'Sightseeing Included: Hall of Fame Museum, Magnetic Hill marvel, and the breathtaking Indus & Zanskar River Confluence (Sangam).',
                    'Local Experiences: Private prayers at the historic Gurudwara Pathar Sahib.',
                    'Overnight Stay: Handpicked Luxury Hotel, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'Sacred Trails - Thiksey & Hemis Monastery Majesty',
                (
                    "Today is dedicated to discovering the core spiritual heritage of Ladakh. Visit the majestic twelve-story Thiksey Monastery, reminiscent of Tibet's Potala Palace, and explore the hidden wealth of Hemis, the wealthiest monastic institution in the region. "
                ),
                [
                    'Sightseeing Included: Thiksey Monastery prayer halls, Hemis Treasury Museum, and Shey Palace complex.',
                    'Food Suggestions: Private gourmet lunch served at a premium garden restaurant near the Indus bank.',
                    'Overnight Stay: Handpicked Luxury Hotel, Leh',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                4,
                'Leh to Exotic Pangong Lake via Chang La Pass',
                (
                    'Drive through the high mountain walls across the Chang La Pass to reach the world-famous Pangong Tso Lake. Witness its magical shifting shades of blue, creating unforgettable memories for your loved ones at this iconic attraction. '
                ),
                [
                    'Sightseeing Included: High-altitude alpine passes, Pangong Lake nature trails.',
                    'Evening Experience: Private lakeside tea service and starlight family stargazing sessions.',
                    'Overnight Stay: Premium Luxury Glamping Domes, Pangong Shoreline',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                5,
                'Pangong Lake Sunrise & Return Transit to Leh',
                (
                    "Awake early to catch a breathtaking sunrise painting the lake's glass-like surface. After an indoor breakfast, your premium vehicle will bring you safely back to Leh for a relaxed evening of local exploration. "
                ),
                [
                    'Sightseeing Included: Changthang wildlife corridor views, local Leh market strolls.',
                    'Evening Experience: Signature TRAGUIN Farewell Family Dinner with local musical storytelling presentations.',
                    'Overnight Stay: Premium Luxury Hotel, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                6,
                'Departure from Leh Airport',
                (
                    'Indulge in your final morning breakfast looking out over the majestic mountain horizons. Avail your premium assisted check-out and private luxury transfer back to Leh Airport for your homeward flight. '
                ),
                [
                    'Meals Included: Breakfast',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Singge Palace | Pangong Heritage Camp',
                'Leh (4 Nights) / Pangong Glamping (1 Night)',
                '05 Nights',
                'Deluxe',
                'Premium Room',
                'Breakfast & Dinner',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Singge Palace (Leh, 4 Nights) | Pangong Heritage Camp (Pangong Glamping, 1 Night) | Breakfast & Dinner',
            ),
            _hotel(
                'Hotel Zen Ladakh | Pangong Inn Luxury Cottages',
                'Leh (4 Nights) / Pangong Glamping (1 Night)',
                '05 Nights',
                'Premium',
                'Premier Room',
                'Breakfast & Dinner',
                5,
                2,
                description='OPTION 02 – PREMIUM: Hotel Zen Ladakh (Leh, 4 Nights) | Pangong Inn Luxury Cottages (Pangong Glamping, 1 Night) | Breakfast & Dinner',
            ),
            _hotel(
                'The Grand Dragon Ladakh | Nirvana Luxury Glamping Domes',
                'Leh (4 Nights) / Pangong Glamping (1 Night)',
                '05 Nights',
                'Luxury',
                'Luxury Room',
                'Full Meal Options',
                5,
                3,
                description='OPTION 03 – LUXURY: The Grand Dragon Ladakh (Leh, 4 Nights) | Nirvana Luxury Glamping Domes (Pangong Glamping, 1 Night) | Full Meal Options',
            ),
            _hotel(
                'TRAGUIN Selected Elite Retreat | Pangong Eco Luxury Domes',
                'Leh (4 Nights) / Pangong Glamping (1 Night)',
                '05 Nights',
                'Ultra Luxury',
                'Elite Retreat Suite',
                'Custom Premium Menu Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Selected Elite Retreat (Leh, 4 Nights) | Pangong Eco Luxury Domes (Pangong Glamping, 1 Night) | Custom Premium Menu Plan',
            ),
        ],
        inclusions=[
            _inc_included('Luxury Accommodations: Handpicked family-centric premium stays.', 1),
            _inc_included('Meals: Generous gourmet meal frameworks across all destinations.', 2),
            _inc_included('Transfers: Dedicated private luxury AC vehicles (Innova / Tempo Traveler).', 3),
            _inc_included('Sightseeing: VIP step-free permissions across major scenic monuments.', 4),
            _inc_included('Welcome Amenities: Customized welcome fruit baskets and high-altitude health kits.', 5),
            _inc_included('TRAGUIN Support: Continuous 24/7 localized operational concierge line.', 6),
            _inc_excluded('Airfare flight tickets to and from Leh destination.', 7),
            _inc_excluded('Medical expenditures, oxygen cylinder extensions outside emergencies.', 8),
            _inc_excluded('Personal laundry, phone bills, micro-bar refreshments inside properties.', 9),
            _inc_excluded('Tips to drivers, guides, or hotel luggage handling staff.', 10),
            _inc_excluded('Anything omitted from the explicit inclusions checklist.', 11),
        ],
    )
    return package, itinerary

def build_la_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'LA-010'
    tour_code = 'TRAGUIN-LA-010'
    title = 'Complete Premium Ladakh Family Tour'
    duration = '09 Nights / 10 Days'
    slug = 'la-010-complete-premium-ladakh-family-tour'
    itin_slug = 'la-010-complete-premium-ladakh-family-tour-itinerary'
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
            _ph('State / Country: Ladakh, India | Category: Family / Complete Premium Luxury', 2),
            _ph('Destinations Covered: Leh • Sham Valley • Nubra Valley • Turtuk Village • Pangong Lake • Chang La • Indus Valley', 3),
            _ph('Ideal for: Families, Multi-generational Groups, Comfort Seekers', 4),
            _ph('Best season: June to September', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Complete Premium Luxury Family FIT Tour', 7),
            _ph('Vehicle: Private AC Innova Crysta / Tempo Traveller throughout', 8),
            _ph('Meal Plan: Premium meals with custom dietary adjustments for children and seniors', 9),
            _ph('Route Map: Leh → Sham Valley → Khardung La → Nubra → Turtuk → Pangong → Chang La → Indus Valley → Stok → Leh Departure', 10),
            _ph('TRAGUIN Signature Experience: Slower climbing speeds across high passes, handpick properties with level walkways and step-free restaurant access, and direct kitchen coordination for specialized child or senior dietary preferences', 11),
            _ph('Shopping & Local Experiences: Leh markets — authentic Pashmina shawls, gorgeous handmade carpets, turquoise jewelry, refreshing organic seabuckthorn juices; artisan cafes for Ladakhi butter teas and fresh hand-pulled momos', 12),
            _ph('Important Notes: Rest on Day 1 mandatory under TRAGUIN medical guidelines; Government ID proofs required 10 days prior for inner-line permits; high pass operations depend on local weather regulations', 13),
        ],
        moods=['Family', 'Luxury', 'Multi-Generational'],
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
        tagline='Complete Premium Ladakh Family Tour • 09 Nights / 10 Days',
        overview='Welcome to an extraordinary multi-generational wonderland, seamlessly organized by TRAGUIN. Ladakh, a crown jewel of majestic snow-capped peaks, ancient spiritual monasteries, and tranquil high-altitude waters, invites your family to connect deeply amidst breathtaking landscapes. Our Luxury Ladakh Holiday Family Tour is custom-crafted to blend exciting Himalayan exploration with gentle premium stays, fostering unforgettable memories. Traverse pristine mountain passes in supreme comfort inside premium luxury SUVs, enjoying handpicked hotels and exclusive experiences curated thoughtfully for every member of your family. \n\nThis elite Ladakh Family Tour is meticulously managed as a private luxury FIT getaway, prioritizing absolute relaxation, unhurried routing, and top-tier hospitality. Your family will travel in spacious, dedicated luxury vehicles with highly experienced local captains. From oxygen-equipped hospitality kits to custom dietary adjustments at all properties, TRAGUIN destination experts handle every single touchpoint to ensure a perfect, stress-free Himalayan vacation. \n\nWhy select a Premium Ladakh Experience for your family? Ladakh delivers a perfect blend of peaceful scenery and rich cultural heritage. Renowned iconic attractions like the spectacular sand dunes of Hunder, the mesmerizing reflection of Pangong Lake, and the historic multi-tiered monasteries of Thiksey form the ultimate checklist for seasoned global travelers. These pristine geographic valleys provide unmatched popular Instagram locations and highly sought-after cultural deep-dives. With the best time to visit Ladakh spanning across the beautiful summer months, our TRAGUIN Ladakh Packages elevate traditional Ladakh Sightseeing into an immersive journey filled with luxury handloom discoveries, authentic culinary classes, and supreme natural beauty. ',
        seo_title='LA-010 | Complete Premium Ladakh Family Tour | TRAGUIN',
        seo_description='Premium 09 Nights / 10 Days complete Ladakh family tour (LA-010 / TRAGUIN-LA-010): Sham Valley, Nubra, Turtuk, Pangong, Indus Valley, Stok Village, and 4-tier accommodation. ',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Cozy welcome and acclimatization day with personalized family briefing', 1),
            _ih('Sham Valley exploration with Magnetic Hill, Gurudwara Pathar Sahib, and Sangam', 2),
            _ih('Khardung La crossing to Nubra Valley with family Bactrian camel ride at Hunder', 3),
            _ih('Heritage excursion to Turtuk border village with Balti Heritage Museum', 4),
            _ih('Complete Indus Valley monastery tour and Stok Village heritage excursion', 5),
        ],
        days=[
            _day(
                1,
                'Arrival in Leh – Cozy Welcome & Acclimatization Day',
                (
                    'Your family will receive a premium assisted welcome at Kushok Bakula Rimpochee Airport by our dedicated TRAGUIN local coordinator. Board your spacious luxury vehicle and transfer smoothly to your handpicked premium hotel. Spend the day resting completely to ensure flawless acclimatization to the high altitude. '
                ),
                [
                    'Sightseeing Included: Complete leisure and rest inside your premium room.',
                    'Evening Experience: Personalized orientation meeting and gentle family briefing over a hot welcome brew.',
                    'Overnight Stay: The Grand Dragon / Stone Hedge Hotel, Leh (Premium Stay)',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                2,
                'Sham Valley Exploration – Natural Wonders & Famous Shrines',
                (
                    'Enjoy a beautiful family breakfast before moving out on a relaxed, scenic drive along the smooth Srinagar-Leh highway. Today introduces your family to some of the most unique geographic attractions and top tourist places in Ladakh. '
                ),
                [
                    'Sightseeing Included: The mystical Magnetic Hill, the ancient holy Gurudwara Pathar Sahib, and the spectacular Sangam (confluence of Indus & Zanskar rivers).',
                    'Photography Points: Striking viewpoints capturing the contrasting multi-colored river waters.',
                    'Overnight Stay: Premium Luxury Hotel, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'Journey Through the Clouds – Over Khardung La to Nubra Valley',
                (
                    'Embark on an exhilarating mountain crossing as your premium SUV effortlessly scales the legendary Khardung La Pass (17,582 ft). Descend beautifully into the wide, peaceful expanses of Nubra Valley, a spectacular destination famed for its unique desert-like mountain settings. '
                ),
                [
                    'Sightseeing Included: Khardung La Pass crossing, Diskit Monastery with its majestic 106-foot tall Maitreya Buddha statue.',
                    'Evening Experience: A joyful family double-humped Bactrian Camel ride across the glowing white sand dunes of Hunder.',
                    'Overnight Stay: Luxury Wilderness Resort / Premium Boutique Glamping, Nubra',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'Heritage Family Excursion to Turtuk Village',
                (
                    'Take an exclusive day trip to the historic and incredibly beautiful border village of Turtuk. Walking with your family through this serene settlement offers a glimpse into Balti cultural roots, beautiful green apricot orchards, and stone pathways. '
                ),
                [
                    'Sightseeing Included: Balti Heritage Museum interaction, local village walkthroughs, and panoramic frontier vistas.',
                    'Food Suggestions: Enjoy refreshing fresh apricot juices and traditional Balti platters at a curated garden café.',
                    'Overnight Stay: Luxury Wilderness Resort, Nubra',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'Scenic Shyok River Drive to Pangong Lake',
                (
                    'Travel along the breathtaking trails tracing the banks of the Shyok River as you make your way towards the globally renowned Pangong Tso. Watch in amazement as your family catches their first glimpse of this immense, shimmering lake. '
                ),
                [
                    'Sightseeing Included: Shyok valley scenery, pristine shoreline walks along the crystal-clear waters of Pangong Tso.',
                    'Photography Points: Endless popular Instagram locations by the bright blue shores.',
                    'Overnight Stay: Premium Luxury Eco-Glamping Domes, Pangong Lake',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                6,
                'Pangong Sunrise & Crossing Chang La Back to Leh',
                (
                    'Wake up early to witness a magical Himalayan sunrise paint the lake surface in spectacular shades of gold and deep violet. After breakfast, return to Leh by crossing the magnificent Chang La Pass, stopping for comfortable breaks along the way. '
                ),
                [
                    'Sightseeing Included: Chang La Pass crossing, peaceful valley stops for refreshments.',
                    'Evening Experience: Relaxed evening to unwind or wander through the charming boutique streets of Leh.',
                    'Overnight Stay: Premium Luxury Hotel, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                7,
                'Monastery Heritage Tour & Indus Valley Cultural Immersion',
                (
                    'Dedicate your day to exploring the spiritual soul of Ladakh. Visit the iconic architectural landmarks of the Indus Valley, designed with gentle paths and accessible steps perfect for family sightseeing. '
                ),
                [
                    "Sightseeing Included: Thiksey Monastery (resembling Tibet's Potala Palace), the historic Shey Palace, and Hemis Monastery.",
                    'Immersive Experiences: Attend a private prayer wheels explanation session conducted by a senior resident monk.',
                    'Overnight Stay: Premium Luxury Hotel, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                8,
                'Indulgent Family Leisure & Souvenir Gathering',
                (
                    'A beautifully unhurried day reserved entirely for family bonding and shopping. Walk through local handloom emporiums at a relaxed pace, sampling mountain delicacies and gathering beautiful keepsakes to carry home. '
                ),
                [
                    'Shopping & Leisure: Leh Main Bazar exploration, traditional pashmina validation clinics.',
                    'Evening Experience: Exclusive TRAGUIN Family Farewell Gala Dinner with a custom multi-course layout.',
                    'Overnight Stay: Premium Luxury Hotel, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                9,
                'Secrets of Stok Village Excursion',
                (
                    'Take a short, highly scenic drive to the beautiful heritage settlement of Stok Village. Explore the royal residential histories and experience local organic farm living alongside your loved ones. '
                ),
                [
                    'Sightseeing Included: Stok Palace Museum, local heritage crop walks.',
                    'Overnight Stay: Premium Luxury Hotel, Leh',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                10,
                'Departure from Leh with Unforgettable Memories',
                (
                    'Savor a final group breakfast facing the breathtaking landscapes of the Stok mountain range. Complete your smooth check-out and board your luxury private vehicle for your assisted transfer to the airport, leaving with unforgettable memories. '
                ),
                [
                    'Meals Included: Breakfast',
                ],
            ),
        ],
        hotels=[
            _hotel(
                'Hotel Singge Palace | Hunder Desert Resort | Pangong Heritage Camps',
                'Leh (7 Nights) / Nubra Valley Luxury (2 Nights) / Pangong Luxury Domes (1 Night)',
                '09 Nights',
                'Deluxe',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Singge Palace (Leh, 7 Nights) | Hunder Desert Resort (Nubra Valley, 2 Nights) | Pangong Heritage Camps (Pangong, 1 Night)',
            ),
            _hotel(
                'Hotel Zen Ladakh | Nubra Organic Retreat | Pangong Inn Luxury Wing',
                'Leh (7 Nights) / Nubra Valley Luxury (2 Nights) / Pangong Luxury Domes (1 Night)',
                '09 Nights',
                'Premium',
                'Premier Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                2,
                description='OPTION 02 – PREMIUM: Hotel Zen Ladakh (Leh, 7 Nights) | Nubra Organic Retreat (Nubra Valley, 2 Nights) | Pangong Inn Luxury Wing (Pangong, 1 Night)',
            ),
            _hotel(
                'The Grand Dragon Ladakh | Stone Hedge Luxury Hotel | Nirvana Luxury Glamping Domes',
                'Leh (7 Nights) / Nubra Valley Luxury (2 Nights) / Pangong Luxury Domes (1 Night)',
                '09 Nights',
                'Luxury',
                'Luxury Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Grand Dragon Ladakh (Leh, 7 Nights) | Stone Hedge Luxury Hotel (Nubra Valley, 2 Nights) | Nirvana Luxury Glamping Domes (Pangong, 1 Night)',
            ),
            _hotel(
                'TRAGUIN Signature Residency | Lchang Nang Retreat | Pangong Eco Luxury Glamping',
                'Leh (7 Nights) / Nubra Valley Luxury (2 Nights) / Pangong Luxury Domes (1 Night)',
                '09 Nights',
                'Ultra Luxury',
                'Signature Residency Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Signature Residency (Leh, 7 Nights) | Lchang Nang Retreat (Nubra Valley, 2 Nights) | Pangong Eco Luxury Glamping (Pangong, 1 Night)',
            ),
        ],
        inclusions=[
            _inc_included('Premium Accommodations: Choice of elite handpicked hotels and luxury glamping.', 1),
            _inc_included('Luxury Transportation: Private AC Innova Crysta / Tempo Traveller throughout.', 2),
            _inc_included('Hospitality Care: Dedicated local captain and continuous oxygen supply cylinder inside vehicles.', 3),
            _inc_included('Sightseeing & Activities: Guided entries, Camel rides, and inner-line wildlife permits included.', 4),
            _inc_included('Welcome Amenities: Custom family fruit baskets and traditional dry fruit boxes upon arrival.', 5),
            _inc_included('TRAGUIN Support: 24/7 dedicated on-ground expert remote monitoring.', 6),
            _inc_excluded('Airfare flight tickets to and from Leh Airport.', 7),
            _inc_excluded('Personal expenditures like laundry, phone calls, or boutique mini-bars.', 8),
            _inc_excluded('Optional extreme adventure sports (ATV rides, river rafting fees).', 9),
            _inc_excluded('Medical or standard trip cancellation insurance policies.', 10),
            _inc_excluded('Anything not explicitly highlighted under the inclusions section.', 11),
        ],
    )
    return package, itinerary

LADAKH_DOMESTIC_BUILDERS = [
    build_la_001,
    build_la_002,
    build_la_003,
    build_la_004,
    build_la_005,
    build_la_006,
    build_la_007,
    build_la_008,
    build_la_009,
    build_la_010,
]
