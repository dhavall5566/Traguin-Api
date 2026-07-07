"""Builder functions for WB-006 through WB-020 West Bengal domestic packages."""

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

WEST_BENGAL_SLUG = "west-bengal"


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

def build_wb_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-006'
    tour_code = 'TRAGUIN-WB-006'
    title = 'Darjeeling • Kalimpong Misty Hills'
    duration = '04 Nights / 05 Days'
    slug = 'wb-006-darjeeling-kalimpong-misty-hills'
    itin_slug = 'wb-006-darjeeling-kalimpong-misty-hills-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: West Bengal, India | Category: Family Vacation / Luxury Hills', 2),
            _ph('Destinations: Darjeeling • Kalimpong', 3),
            _ph('Ideal for: Families, Couples & Leisure Seekers', 4),
            _ph('Best season: March to May & October to December', 5),
            _ph('Vehicle Allocated: Private Air-Conditioned Luxury Innova Crysta / Luxury SUV', 6),
            _ph('Meal Plan: Modified American Plan (Gourmet Breakfasts & Lavish Dinners Included)', 7),
            _ph('Route Map: Bagdogra (IXB) / NJP Arrival → Kalimpong Misty Hills → Darjeeling Alpine Ridge → Bagdogra / NJP Departure', 8),
            _ph('TRAGUIN Signature Experience: Curated carefully by TRAGUIN experts — stress-free mountain driving, premium fast-track check-ins, and top-tier hospitality designed for families.', 9),
            _ph('Shopping & Local Experiences: Darjeeling Mall Road & Chowk Bazaar — authentic Flush-01 Darjeeling Tea, woolen shawls, brass prayer wheels. Glenary\'s Bakery, Keventer\'s. Instagram Spots: Batasia Loop and Durpin Dara Monastery prayer flags.', 10),
            _ph('Important Notes: Hotel check-in 14:00 hrs, check-out 11:00 hrs. Hill weather unpredictable — pack light jackets and heavy woolens for Tiger Hill. Advance booking 45-60 days recommended.', 11),
        ],
        moods=['Family', 'Luxury', 'Hills', 'Honeymoon'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Darjeeling • Kalimpong Misty Hills • 04 Nights / 05 Days',
        overview=('Welcome to a land of floating clouds, colonial charm, and world-famous emerald tea estates. Lovingly curated by TRAGUIN, this exclusive West Bengal Honeymoon Package and West Bengal Family Tour brings you the very best of North Bengal\'s alpine splendor. Wake up to panoramic views of Mt. Kanchenjunga, walk along misty ridges, and let our signature hospitality turn a simple getaway into a series of deeply emotional, premium stays.\n\nTOUR OVERVIEW\nVehicle Allocated: Private Air-Conditioned Luxury Innova Crysta / Luxury SUV (Spacious and optimized for mountain terrain). Meal Plan: Modified American Plan (Gourmet Breakfasts & Lavish Dinners Included). Route Map: Bagdogra (IXB) / NJP Arrival → Kalimpong Misty Hills → Darjeeling Alpine Ridge → Bagdogra / NJP Departure.\n\nTRAGUIN Curated Experience Note: Immerse your family in handpicked hotels, an iconic early morning Tiger Hill sunrise cruise, a vintage Toy Train joy ride, and specialized, slow-paced exploration tailored beautifully for uncompromised elite relaxation.\n\nWHY VISIT WEST BENGAL? A PREMIUM MISTY HILLS EXPERIENCE\nThe majestic highlands of West Bengal offer an escape into some of the most breathtaking landscapes in South Asia. Known globally for its aromatic tea leaves and deep-rooted British heritage, a Luxury West Bengal Holiday seamlessly blends vintage colonial culture with pristine scenic beauty. When exploring the Top Tourist Places in West Bengal, the twin gems of Darjeeling and Kalimpong stand out as absolute favorites for premium travelers.\n\nFrom exploring the traditional Buddhist monasteries and orchids of Kalimpong to riding the UNESCO World Heritage Himalayan Railway, our exclusive TRAGUIN West Bengal Packages focus heavily on deep cultural highlights and immersive experiences. This package ensures you catch the Best Time to Visit West Bengal with access to hidden viewpoints, famous Instagram spots, and the signature comfort of handpicked boutique properties.'),
        seo_title='WB-006 | Darjeeling Kalimpong Misty Hills | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days West Bengal package (WB-006 / TRAGUIN-WB-006): Kalimpong monasteries, Darjeeling Tiger Hill sunrise, Toy Train, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Kalimpong Durpin Monastery, Pine View Cactus Nursery, and Deolo Viewpoint', 1),
            _ih('Tiger Hill sunrise over Mt. Kanchenjunga, Ghoom Monastery, and Batasia Loop', 2),
            _ih('UNESCO Darjeeling Himalayan Railway Toy Train joy ride and tea estate walk', 3),
            _ih('Himalayan Mountaineering Institute, Darjeeling Zoo, Peace Pagoda, and Tibetan Refugee Center', 4),
            _ih('4-tier handpicked accommodation: Kalimpong (01 Night) + Darjeeling (03 Nights)', 5),
        ],
        days=[
            _day(1, 'ARRIVAL BAGDOGRA / NJP TO KALIMPONG', ('Your premium mountain escape begins as you arrive at Bagdogra International Airport or New Jalpaiguri Station. A professional TRAGUIN tour manager welcomes your family warmly and introduces you to your private luxury mountain vehicle. Leave the plains behind as you climb alongside the emerald Teesta River. Arrive in the quiet, flower-decked hills of Kalimpong and check into your handpicked premium resort. Spend a relaxed evening listening to the mountain breeze or walking through pristine lawns.'), [
                'Sightseeing Included: Teesta River Viewpoints, Scenic Alpine Drive.',
                'Evening Experience: Curated welcoming briefing over high-tea arranged exclusively by TRAGUIN experts.',
                'Overnight Stay: Handpicked Luxury Resort, Kalimpong.',
                'Meals Included: Welcome Drink & Gourmet Dinner.',
            ]),
            _day(2, 'KALIMPONG SIGHTSEEING TO DARJEELING', ('After a luxurious breakfast, explore the tranquil charms of Kalimpong. Visit the historic Durpin Monastery for serene chants and sweeping views of the valley below. Discover the famous Pine View Nursery, housing a world-class collection of exotic cacti and vibrant orchids. Post lunch, enjoy a scenic drive to Darjeeling—the legendary Queen of Hills. Arrive at your luxury ridge hotel for a smooth, prioritized check-in experience.'), [
                'West Bengal Sightseeing: Durpin Dara Hill, Pine View Cactus Nursery, Deolo Viewpoint.',
                'Photography Points: Panoramic frames of mountain ranges from Deolo Hill.',
                'Overnight Stay: Premium Luxury Heritage Hotel, Darjeeling.',
                'Meals Included: Full Buffet Breakfast & Lavish Dinner.',
            ]),
            _day(3, 'DARJEELING SUNRISE & ICONIC ATTRACTIONS', ('Wake up early at 04:00 AM for an unforgettable, deeply emotional memory. Drive up to Tiger Hill to watch the morning sun paint the snow-peaks of Mt. Kanchenjunga in hues of liquid gold. On your return, visit the serene Ghoom Monastery and the historic Batasia Loop. After a relaxed late breakfast at your hotel, experience an iconic vintage Toy Train Joy Ride across the mountain ridges. Spend the afternoon exploring the lush green slopes of a local tea estate.'), [
                'Sightseeing Included: Tiger Hill Sunrise, Ghoom Monastery, Batasia Loop, Toy Train Ride, Tea Garden Walk.',
                'Local Experiences: Walk among manicured tea shrubs and learn the art of tea plucking from local experts.',
                'Overnight Stay: Premium Luxury Heritage Hotel, Darjeeling.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(4, 'DARJEELING CULTURAL EXPLORATION', ('Dedicate today to discovering Darjeeling\'s deeply rich mountaineering history and unique alpine ecology. Visit the renowned Himalayan Mountaineering Institute (HMI) and the Padmaja Naidu Himalayan Zoological Park, home to rare and beautiful snow leopards and red pandas. Later, find absolute tranquility at the stunning white marble Peace Pagoda, listening to gentle spiritual echoes.'), [
                'Sightseeing Included: HMI, Darjeeling Zoo, Tibetan Refugee Self-Help Center, Japanese Peace Pagoda.',
                'Optional Activities: Spend a cozy evening at a heritage cafe on the famous Mall Road.',
                'Overnight Stay: Premium Luxury Heritage Hotel, Darjeeling.',
                'Meals Included: Breakfast & Festive Farewell Dinner.',
            ]),
            _day(5, 'DARJEELING TO BAGDOGRA / NJP DEPARTURE', ('Savor a final, peaceful breakfast while looking out over the misty valleys. Pack your memories as your luxury private vehicle arrives to transfer you comfortably back down the hills to Bagdogra Airport or NJP Station. Your premium TRAGUIN West Bengal Experience concludes flawlessly, leaving you and your family with unforgettable memories of a lifetime.'), [
                'Transfers Included: Private Luxury Airport / Station Drop-off.',
                'Meals Included: Full Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('The Sian Excellence Summit', 'Kalimpong', '01 Night', 'Deluxe', 'Deluxe Room', 'MAP (Breakfast + Dinner)', 4, 1, description='OPTION 01 – DELUXE: The Sian Excellence Summit (Kalimpong, 01 Night)'),
            _hotel('Hermon Resort & Spa', 'Darjeeling', '03 Nights', 'Deluxe', 'Deluxe Room', 'MAP (Breakfast + Dinner)', 4, 2, description='OPTION 01 – DELUXE: Hermon Resort & Spa (Darjeeling, 03 Nights)'),
            _hotel('Sinclairs Retreat Kalimpong', 'Kalimpong', '01 Night', 'Premium', 'Premium Room', 'MAP (Breakfast + Dinner)', 4, 3, description='OPTION 02 – PREMIUM: Sinclairs Retreat Kalimpong (Kalimpong, 01 Night)'),
            _hotel('Sinclairs Darjeeling', 'Darjeeling', '03 Nights', 'Premium', 'Premium Room', 'MAP (Breakfast + Dinner)', 4, 4, description='OPTION 02 – PREMIUM: Sinclairs Darjeeling (Darjeeling, 03 Nights)'),
            _hotel('The Elgin Silver Oaks', 'Kalimpong', '01 Night', 'Luxury', 'Luxury Heritage Room', 'MAP (Breakfast + Dinner)', 5, 5, description='OPTION 03 – LUXURY: The Elgin Silver Oaks (Kalimpong, 01 Night)'),
            _hotel('The Elgin, Darjeeling', 'Darjeeling', '03 Nights', 'Luxury', 'Luxury Heritage Room', 'MAP (Breakfast + Dinner)', 5, 6, description='OPTION 03 – LUXURY: The Elgin, Darjeeling (Darjeeling, 03 Nights)'),
            _hotel('Mayfair Himalayan Spa Resort', 'Kalimpong', '01 Night', 'Ultra Luxury', 'Executive Suite', 'MAP + High Tea Included', 5, 7, description='OPTION 04 – ULTRA LUXURY: Mayfair Himalayan Spa Resort (Kalimpong, 01 Night)'),
            _hotel('Mayfair Darjeeling', 'Darjeeling', '03 Nights', 'Ultra Luxury', 'Executive Suite', 'MAP + High Tea Included', 5, 8, description='OPTION 04 – ULTRA LUXURY: Mayfair Darjeeling (Darjeeling, 03 Nights)'),
        ],
        inclusions=[
            _inc_included('Accommodation: Premium stays across handpicked hotels with luxury mountain-view rooms.', 1),
            _inc_included('Meals: 04 Lavish Buffet Breakfasts and 04 curated multi-cuisine dinners at the resorts.', 2),
            _inc_included('Transfers & Sightseeing: All commutes via dedicated luxury AC Innova Crysta with a highly skilled mountain driver.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated telephone concierge assistance from our local helpdesks.', 4),
            _inc_included('Complimentary Experiences: A private estate tea-tasting tour and entry passes for the Tiger Hill premium gallery.', 5),
            _inc_included('Welcome Amenities: Fully personalized travel kit featuring premium hill-country mints and fresh local orchids on arrival.', 6),
            _inc_excluded('Airfare or main railway line ticketing costs.', 7),
            _inc_excluded('Toy Train ride ticket costs (Can be added on request based on availability).', 8),
            _inc_excluded('Personal items such as laundry, specialized liquor, telephone tabs, and driver tips.', 9),
            _inc_excluded('Additional vehicle detours or entry costs for cameras/drones.', 10),
            _inc_excluded('Mandatory premium medical or travel protection insurance.', 11),
        ],
    )
    return package, itinerary

def build_wb_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-007'
    tour_code = 'TRAGUIN-WB-007'
    title = 'Darjeeling • Mirik Quick Getaway'
    duration = '03 Nights / 04 Days'
    slug = 'wb-007-darjeeling-mirik-quick-getaway'
    itin_slug = 'wb-007-darjeeling-mirik-quick-getaway-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code WB-007 | TRAGUIN tour code TRAGUIN-WB-007', 1),
            _ph('State / Country: West Bengal, India | Category: Family Getaway / Luxury', 2),
            _ph('Destinations: Darjeeling • Mirik • Kurseong', 3),
            _ph('Ideal for: Families, Couples & Leisure Travelers', 4),
            _ph('Best season: March to May & October to December', 5),
            _ph('Vehicle Allocated: Private Air-Conditioned Luxury Innova Crysta / XUV', 6),
            _ph('Meal Plan: Modified American Plan (Daily Buffet Breakfast & Choice Gourmet Dinners)', 7),
            _ph('Route Map: Bagdogra (IXB) / NJP Arrival → Kurseong Valley → Darjeeling Hills → Mirik Lake → Bagdogra Departure', 8),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts — personalized assistance, seamless room allocations, and priority timing strategies for Tiger Hill.', 9),
            _ph('Shopping & Local Experiences: Chowrasta Mall Road woolen shawls and Tibetan jewelry. NathuMulls / Golden Tips first-flush tea. Glenary\'s Bakery chocolate eclairs.', 10),
            _ph('Important Notes: Check-in 14:00 hrs, check-out 11:00 hrs. Mountain weather changes quickly — carry woolens. Tiger Hill permits require advance booking.', 11),
        ],
        moods=['Family', 'Luxury', 'Hills'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Darjeeling • Mirik Quick Getaway • 03 Nights / 04 Days',
        overview='Welcome to the Queen of the Hills. This premium luxury travel itinerary, meticulously curated by TRAGUIN, offers a flawless mountain escape designed for discerning families. Witness the iconic sunbeams illuminating the snow-clad peak of Mt. Kanchenjunga, breathe in the fragrance of world-renowned tea fields, and cruise along the pristine banks of Sumendu Lake in Mirik.\n\nTOUR OVERVIEW\nVehicle Allocated: Private Air-Conditioned Luxury Innova Crysta / XUV. Meal Plan: Modified American Plan (Daily Buffet Breakfast & Choice Gourmet Dinners). Route Map: Bagdogra (IXB) / NJP Arrival → Kurseong Valley → Darjeeling Hills → Mirik Lake → Bagdogra Departure.\n\nTRAGUIN Curated Experience Note: This Darjeeling Family Tour seamlessly eliminates long transit fatigue by incorporating comfortable private luxury transportation, early morning fast-track access passes to Tiger Hill, and a private heritage Toy Train ride.\n\nPREMIUM DARJEELING EXPERIENCE: WHY VISIT WITH FAMILY?\nDarjeeling remains an iconic attraction for global travelers seeking breathtaking landscapes and rich colonial heritage. Celebrated widely as the ultimate destination for a Darjeeling Honeymoon Package or an enriching Darjeeling Family Tour, the region seamlessly blends mist-covered mountains with vibrant cultural experiences.',
        seo_title='WB-007 | Darjeeling Mirik Quick Getaway | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days West Bengal package (WB-007 / TRAGUIN-WB-007): Tiger Hill sunrise, Mirik Sumendu Lake, Toy Train, and 4-tier Darjeeling accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Tiger Hill sunrise with TRAGUIN priority passes, Batasia Loop, and Ghoom Monastery', 1),
            _ih('Himalayan Mountaineering Institute, Zoo, Peace Pagoda, and ropeway ride', 2),
            _ih('Mirik Sumendu Lake, Simana Viewpoint, and Pashupati Nagar Indo-Nepal border market', 3),
            _ih('Private guided tea garden walk with traditional attire photography spots', 4),
            _ih('4-tier handpicked Darjeeling accommodation (03 Nights)', 5),
        ],
        days=[
            _day(1, 'BAGDOGRA / NJP TO DARJEELING', ('Arrive at Bagdogra International Airport or New Jalpaiguri Railway Station where your elite TRAGUIN chauffeur welcomes you. Board your private luxury vehicle and embark on a mesmerizing drive toward Darjeeling. Pass through the rolling tea estates of Kurseong and watch the mist playfully drift over the pines. Upon arriving at your handpicked hotel, enjoy a swift, contactless check-in. Sip on a hot cup of authentic Muscatel Darjeeling tea while looking over the mountain ridges.'), [
                'Sightseeing Included: Panoramic Kurseong Viewpoints, Rohini Scenic Route.',
                'Evening Experience: Explore Mall Road (The Chowrasta) for vintage local handicrafts and heritage cafes.',
                'Overnight Stay: Premium Luxury Resort / Hotel, Darjeeling.',
                'Meals Included: Welcome Drink & Chef\'s Special Dinner.',
            ]),
            _day(2, 'DARJEELING SIGHTSEEING', ('Wake up at 3:45 AM for an exclusive, highly sought-after experience. Drive to Tiger Hill using TRAGUIN priority passes. Witness the sun slowly rise, painting the snows of Mt. Kanchenjunga in hues of gold and amber. On your way back, stop at the historical Batasia Loop to admire the engineering marvel of the Himalayan Toy Train track, and pay homage at the War Memorial. Return to your hotel for a lavish breakfast, then head out to explore the Padmaja Naidu Himalayan Zoological Park, the Himalayan Mountaineering Institute, and the serene Japanese Peace Pagoda.'), [
                'Sightseeing Included: Tiger Hill Sunrise, Batasia Loop, Ghoom Monastery, Himalayan Mountaineering Institute, Zoo, Ropeway ride.',
                'Immersive Experiences: A private, guided walk through a manicured tea garden with traditional attire photography spots.',
                'Overnight Stay: Premium Luxury Resort / Hotel, Darjeeling.',
                'Meals Included: Full Buffet Breakfast & Dinner.',
            ]),
            _day(3, 'DARJEELING TO MIRIK EXCURSION', ('Following a delicious breakfast, enjoy a picturesque drive along the Indo-Nepal border toward the peaceful town of Mirik. The drive winds through the dense, tall trees of the Simana view-point forest. Arrive at the scenic Sumendu Lake, famous for its iconic footbridge and peaceful, reflective waters. Rent a private shikara-style boat or enjoy a calm horse ride around the lakeside tracks. On the return trip, stop for duty-free international shopping at the bustling Pashupati Nagar Market on the border.'), [
                'Sightseeing Included: Sumendu Lake, Simana Viewpoint, Pashupati Nagar (Indo-Nepal Border Market), Orange Orchards route.',
                'Optional Activities: Boating on Sumendu Lake, buying authentic local cardamom and spices.',
                'Overnight Stay: Premium Luxury Resort / Hotel, Darjeeling.',
                'Meals Included: Breakfast & Farewell Dinner.',
            ]),
            _day(4, 'DEPARTURE FROM DARJEELING', ('Indulge in a final, relaxed breakfast while watching the clouds roll across the valley. Pack your bags and load your souvenirs into your luxury vehicle. Your chauffeur will provide a smooth ride back to Bagdogra Airport or NJP Station. Your premium TRAGUIN Darjeeling Package concludes seamlessly, leaving you with beautiful memories to cherish forever.'), [
                'Transfers Included: Private Luxury Airport / Station Drop-off.',
                'Best Time to Visit: October to May provides the clearest skies for Kanchenjunga views.',
                'Meals Included: Full Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Summit Hermon Resort & Spa', 'Darjeeling', '03 Nights', 'Deluxe', 'Deluxe Room', 'MAP (Breakfast + Dinner)', 4, 1, description='OPTION 01 – DELUXE: Summit Hermon Resort & Spa (Darjeeling, 03 Nights)'),
            _hotel('The Elgin, Darjeeling', 'Darjeeling', '03 Nights', 'Premium', 'Deluxe Suite Room', 'MAP (Breakfast + Dinner)', 4, 2, description='OPTION 02 – PREMIUM: The Elgin, Darjeeling (Darjeeling, 03 Nights)'),
            _hotel('Mayfair Darjeeling', 'Darjeeling', '03 Nights', 'Luxury', 'Executive Heritage Room', 'MAP (Breakfast + Dinner)', 5, 3, description='OPTION 03 – LUXURY: Mayfair Darjeeling (Darjeeling, 03 Nights)'),
            _hotel('Windamere Hotel', 'Darjeeling', '03 Nights', 'Ultra Luxury', 'Lord Kitchener Suite', 'All Meals + English High Tea', 5, 4, description='OPTION 04 – ULTRA LUXURY: Windamere Hotel (Darjeeling, 03 Nights)'),
        ],
        inclusions=[
            _inc_included('Accommodation: 03 Nights stay at premium luxury handpicked hotels tailored for families.', 1),
            _inc_included('Meals: 03 Lavish Buffet Breakfasts and 03 specially designed gourmet Dinners at the properties.', 2),
            _inc_included('Transfers & Sightseeing: Dedicated Chauffeur-driven luxury vehicle for all point-to-point sightseeing tours.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated on-call concierge and expert local route guidance.', 4),
            _inc_included('Taxes & Permits: Fuel costs, state highway taxes, parking charges, and driver allowances.', 5),
            _inc_included('Welcome Amenities: Refreshing welcome kits with traditional mountain stoles, premium hand sanitizers, and mineral water.', 6),
            _inc_excluded('Airfare or train tickets to/from Bagdogra or New Jalpaiguri.', 7),
            _inc_excluded('Entry tickets to museums, parks, or boat rentals unless explicitly stated.', 8),
            _inc_excluded('Personal expenses such as telephone calls, laundry, hard drinks, or tipping.', 9),
            _inc_excluded('Optional excursions, adventure rides, or extended vehicle usage.', 10),
        ],
    )
    return package, itinerary

def build_wb_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-008'
    tour_code = 'TRAGUIN-WB-008'
    title = 'Shantiniketan Art & Rabindranath Culture Premium Holiday'
    duration = '02 Nights / 03 Days'
    slug = 'wb-008-shantiniketan-art-culture'
    itin_slug = 'wb-008-shantiniketan-art-culture-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code WB-008 | TRAGUIN tour code TRAGUIN-WB-008', 1),
            _ph('State / Country: West Bengal, India | Category: Family / Art & Culture', 2),
            _ph('Destinations: Kolkata • Shantiniketan • Bolpur', 3),
            _ph('Ideal for: Families, Art Enthusiasts & Intellectuals', 4),
            _ph('Best season: October to March', 5),
            _ph('Travel Style: Private Premium FIT Family Journey', 6),
            _ph('Vehicle Allocated: Luxury Private Air-Conditioned Sedan / SUV', 7),
            _ph('Meal Plan: Continental Breakfast & Authentic Bengali Royal Dinners', 8),
            _ph('TRAGUIN Curated Experience Note: Private guided heritage walk inside Visva-Bharati, live Baul musical evening, and handpicked premium stays.', 9),
            _ph('Shopping & Local Art: Kantha stitch silk sarees, Dokra metal figurines, terracotta home decor. Instagram Spots: Sonajhuri red-soil woodlands and Visva-Bharati prayer halls.', 10),
            _ph('Important Notes: Check-in 14:00 hrs, check-out 11:00 hrs. Visva-Bharati entry limits subject to academic holidays. E-rickshaws arranged in heritage zones.', 11),
        ],
        moods=['Family', 'Art', 'Culture'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Shantiniketan Art & Rabindranath Culture Premium Holiday • 02 Nights / 03 Days',
        overview='Step into the soul-stirring world of literature, classical music, and fine arts. This exclusive, high-end West Bengal Honeymoon Package and West Bengal Family Tour layout designed by TRAGUIN takes you into the heart of Shantiniketan. Walk the pathway of Nobel Laureate Rabindranath Tagore, surrounded by majestic red soil, Baul music, and breathtaking landscapes of rural tranquility.\n\nTOUR OVERVIEW\nTravel Style: Private Premium FIT Family Journey. Vehicle Allocated: Luxury Private Air-Conditioned Sedan / SUV. Meal Plan: Continental Breakfast & Authentic Bengali Royal Dinners.\n\nTRAGUIN Curated Experience Note: Includes a private guided heritage walk inside the Visva-Bharati university campus, a soulful live private Baul musical evening, and accommodations at handpicked premium stays.\n\nPREMIUM WEST BENGAL EXPERIENCE: WHY VISIT SHANTINIKETAN?\nIf you are seeking a Luxury West Bengal Holiday, the cultural retreat of Shantiniketan stands as one of the Top Tourist Places in West Bengal. Known globally as the seat of Rabindranath Tagore\'s Visva-Bharati University, it offers immersive experiences that seamlessly blend heritage with nature.',
        seo_title='WB-008 | Shantiniketan Art & Culture | TRAGUIN',
        seo_description='Premium 02 Nights / 03 Days West Bengal package (WB-008 / TRAGUIN-WB-008): Visva-Bharati, Sonajhuri Haat, Kopai River, and 4-tier heritage accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Visva-Bharati Campus including Uttarayan Complex, Kala Bhavan, and Sangeet Bhavan', 1),
            _ih('Sonajhuri Haat weekly heritage marketplace with Santhali tribal dancers', 2),
            _ih('Kopai River banks and Amar Kutir artisan centre for leather crafts and Kantha sarees', 3),
            _ih('Private live Baul music concert under a banyan tree', 4),
            _ih('4-tier handpicked Shantiniketan accommodation (02 Nights)', 5),
        ],
        days=[
            _day(1, 'KOLKATA TO SHANTINIKETAN', ('Your premium cultural experience begins with a warm welcome by your dedicated Chauffeur at Kolkata. Board your private luxury vehicle for a smooth and scenic drive towards Bolpur, Shantiniketan. Marvel at the shifting breathtaking landscapes as city skylines turn into green expanses of rural West Bengal. Upon arrival, check in seamlessly to your premium heritage resort.'), [
                'Arrival Experience: Chauffeured pickup, refreshing welcome drink, and quick check-in.',
                'Evening Experience: A curated heritage talk regarding the historical significance of Bolpur over high-tea by TRAGUIN experts.',
                'Overnight Stay: Handpicked Luxury Resort, Shantiniketan.',
                'Meals Included: Welcome Amenities & Fine Traditional Dinner.',
            ]),
            _day(2, 'SHANTINIKETAN HERITAGE SIGHTSEEING', ('Enjoy a delicious gourmet breakfast before heading out for a comprehensive day of West Bengal Sightseeing. Accompanied by a certified university guide, visit the grand Visva-Bharati Campus, including the Uttarayan Complex, Rabindra Bhavan Museum, and Upasana Griha. Witness magnificent open-air classrooms under ancient trees. In the afternoon, explore the serene pathways near the Kopai River, followed by a visit to the vibrant Sonajhuri Haat.'), [
                'Sightseeing Included: Uttarayan, Kala Bhavan, Sangeet Bhavan, Sonajhuri Forest, Kopai River banks.',
                'Exclusive Experiences: Private seatings at a live Baul music concert under the shade of a banyan tree.',
                'Overnight Stay: Handpicked Luxury Resort, Shantiniketan.',
                'Meals Included: Buffet Breakfast & Special Festive Dinner.',
            ]),
            _day(3, 'LOCAL HANDICRAFTS & RETURN TO KOLKATA', ('Savor a final slow breakfast at your premium stay. Before heading back, visit Amar Kutir, a cooperative society showcasing the finest local leather crafts, Kantha-stitched silk sarees, and terracotta work of West Bengal. Conclude your tour with a relaxed drive back to Kolkata, leaving you with unforgettable memories of a deeply enriching holiday crafted perfectly by TRAGUIN.'), [
                'Sightseeing Included: Amar Kutir Artisan Centre, Local Shopping Outlets.',
                'Transfers Included: Private Drop-off at Kolkata Airport / Railway Station.',
                'Meals Included: Full Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Mark & Meadows, Shantiniketan', 'Shantiniketan', '02 Nights', 'Deluxe', 'Deluxe AC Room', 'CP (Breakfast Only)', 4, 1, description='OPTION 01 – DELUXE: Mark & Meadows, Shantiniketan (02 Nights)'),
            _hotel('Royal Bengal Resort, Shantiniketan', 'Shantiniketan', '02 Nights', 'Premium', 'Premium Luxury Cottage', 'MAP (Breakfast + Dinner)', 4, 2, description='OPTION 02 – PREMIUM: Royal Bengal Resort, Shantiniketan (02 Nights)'),
            _hotel('The ChasiKoti Heritage Retreat', 'Shantiniketan', '02 Nights', 'Luxury', 'Luxury Suite with Village View', 'MAP (Breakfast + Dinner)', 5, 3, description='OPTION 03 – LUXURY: The ChasiKoti Heritage Retreat (02 Nights)'),
            _hotel('Prokriti Kantho Luxury Eco Resort', 'Shantiniketan', '02 Nights', 'Ultra Luxury', 'Executive Presidential Villa', 'MAP + High Tea Included', 5, 4, description='OPTION 04 – ULTRA LUXURY: Prokriti Kantho Luxury Eco Resort (02 Nights)'),
        ],
        inclusions=[
            _inc_included('Accommodation: 02 Nights stay at premium handpicked hotels or boutique heritage resorts.', 1),
            _inc_included('Meals: Daily gourmet breakfasts and traditional multi-course Bengali dinners as specified.', 2),
            _inc_included('Transfers & Sightseeing: All point-to-point journeys by an executive air-conditioned private vehicle.', 3),
            _inc_included('Assistance: Personalized 24/7 TRAGUIN backend support and a dedicated chauffeur.', 4),
            _inc_included('Complimentary Experiences: Private local university authorized companion guide and a live folk music performance entry.', 5),
            _inc_included('Taxes: All current applicable hotel luxury taxes and toll fees included.', 6),
            _inc_excluded('Airfare or Inter-state train tickets to Kolkata.', 7),
            _inc_excluded('Individual entry tickets to monuments, museums, or cameras inside Uttarayan Complex.', 8),
            _inc_excluded('Personal items such as laundry, boutique cafe bills, tips, and additional room service orders.', 9),
            _inc_excluded('Any medical emergencies or travel insurance charges.', 10),
        ],
    )
    return package, itinerary

def build_wb_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-009'
    tour_code = 'TRAGUIN-WB-009'
    title = 'Grand West Bengal Hills & Sunderbans Mega Experience'
    duration = '08 Nights / 09 Days'
    slug = 'wb-009-grand-west-bengal-hills-sunderbans-mega'
    itin_slug = 'wb-009-grand-west-bengal-hills-sunderbans-mega-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code WB-009 | TRAGUIN tour code TRAGUIN-WB-009', 1),
            _ph('State / Country: West Bengal, India | Category: Family Mega Tour', 2),
            _ph('Destinations: Kolkata • Sunderbans • Darjeeling • Kalimpong', 3),
            _ph('Ideal for: Families & Elite Travelers', 4),
            _ph('Best season: October to May', 5),
            _ph('Travel Pattern: Tailor-Made Family FIT Travel', 6),
            _ph('Vehicle Allocated: Private Air-Conditioned Luxury Innova Crysta & Private Motorized Cruise Boat', 7),
            _ph('Meal Plan: Daily Deluxe Buffet Breakfasts (All meals included during Sunderbans Cruise)', 8),
            _ph('TRAGUIN Signature Experience: Optimal blend of comfort and discovery with priority lane check-ins and unique access across national landmarks.', 9),
            _ph('Shopping: Darjeeling first-flush tea, Kolkata Baluchari and Tant cotton sarees, clay handicrafts.', 10),
            _ph('Important Notes: Check-in 14:00 hrs, check-out 11:00 hrs. Mountain regions need warm layers. Toy train and jungle cruise permits require advance booking.', 11),
        ],
        moods=['Family', 'Luxury', 'Wildlife', 'Hills'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Grand West Bengal Hills & Sunderbans Mega Experience • 08 Nights / 09 Days',
        overview='Welcome to an extraordinary journey mapping the cultural soul, royal history, and majestic ecological wonders of Eastern India. Carefully assembled by the lifestyle travel architects at TRAGUIN, this signature itinerary links the architectural grandness of colonial Kolkata, the mysterious deep tidal mangrove networks of the Sunderbans, and the cloud-kissed premium stays of Darjeeling.\n\nTOUR OVERVIEW\nTravel Pattern: Tailor-Made Family FIT Travel. Vehicle Allocated: Private Air-Conditioned Luxury Innova Crysta & Private Motorized Cruise Boat. Meal Plan: Daily Deluxe Buffet Breakfasts (All meals included during Sunderbans Cruise).\n\nTRAGUIN Curated Experience Note: Enjoy seamless, non-hurried private luxury logistics, expert local companion guides, priority check-ins at handpicked heritage luxury resorts, and high-end immersive safaris across top-tier destinations.\n\nWHY CHOOSE OUR PREMIUM WEST BENGAL EXPERIENCE?\nWest Bengal stands out globally as a region defined by profound contrasts—from the iconic attractions of the Himalaya mountain ranges to the deltaic wilderness of the Royal Bengal Tiger. Elite voyagers searching for a Luxury West Bengal Holiday or a well-paced West Bengal Family Tour will discover unmatched cultural complexity, local gastronomy, and unforgettable memories.',
        seo_title='WB-009 | Grand West Bengal Hills & Sunderbans Mega | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days West Bengal package (WB-009 / TRAGUIN-WB-009): Kolkata, Sunderbans safari, Kalimpong, Darjeeling, Mirik, and 4-tier accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Kolkata Hooghly riverside drive, Howrah Bridge, and heritage luxury stay', 1),
            _ih('Sunderbans National Park water safari, Sajnekhali, Sudhanyakhali, and Dobanki Canopy Walk', 2),
            _ih('Kalimpong Durpin Monastery, Deolo Hill, Pine View Nursery, and Toy Train to Ghoom', 3),
            _ih('Darjeeling Tiger Hill sunrise, HMI, Zoo, tea estate, and Mirik Sumendu Lake excursion', 4),
            _ih('4-tier handpicked accommodation across Kolkata/Sunderbans and Darjeeling/Kalimpong', 5),
        ],
        days=[
            _day(1, 'KOLKATA ARRIVAL', ('Arrive at Netaji Subhash Chandra Bose International Airport, Kolkata. A designated premium chauffeur from TRAGUIN will welcome you warmly and escort your family to a handpicked luxury hotel. After a seamless, smooth private check-in, unwind inside your sophisticated suite. In the late afternoon, enjoy an introduction to Kolkata\'s iconic attractions with a leisurely vehicle cruise past the brilliantly lit Howrah Bridge and Babu Ghat along the Hooghly River bank.'), [
                'Sightseeing Included: Private Airport Pick-up, Hooghly Riverside Panoramic Drive.',
                'Evening Experience: A welcome high-tea briefing with local sweet treats curated by our travel consultants.',
                'Overnight Stay: Ultra-Luxury Heritage Hotel, Kolkata.',
                'Meals Included: Welcome Drink & Gourmet Dinner.',
            ]),
            _day(2, 'KOLKATA TO SUNDERBANS', ('Depart early in your comfortable private vehicle towards Godkhali Jetty, the gateway to the world\'s largest mangrove forest ecosystem. Board an exclusive, customized TRAGUIN private motorized luxury cruise vessel. Travel smoothly down the Hogol, Gomor, and Durgaduani rivers. Arrive at a premium eco-luxury jungle resort nestled deep within the Delta. In the afternoon, enjoy an immersive village walking experience.'), [
                'Sightseeing Included: River Delta Navigation, Local Island Village Walk.',
                'Evening Experience: Traditional local tribal dance performance and fresh local seafood culinary dinner inside the resort gardens.',
                'Overnight Stay: Premium Eco-Luxury Resort, Sunderbans.',
                'Meals Included: Breakfast, Lunch, High Tea & Festive Dinner.',
            ]),
            _day(3, 'SUNDERBANS NATIONAL PARK SAFARI', ('Embark on a thrilling, day-long water-bound safari through the narrow water creeks of the Sunderbans National Park. From your secure private vessel, look out for the legendary Royal Bengal Tiger swimming across channels or resting on mudflats. Visit the Sajnekhali Watchtower, Sudhanyakhali Watchtower, and the famous Dobanki Canopy Walkway.'), [
                'Sightseeing Included: Sajnekhali, Sudhanyakhali, Dobanki Canopy Walk, Mangrove Interpretative Center.',
                'Photography Points: Scenic panoramic lookouts from the watchtowers over pristine wild channels.',
                'Overnight Stay: Premium Eco-Luxury Resort, Sunderbans.',
                'Meals Included: Deluxe onboard Breakfast, Hot Regional Lunch, and Lakeside Dinner.',
            ]),
            _day(4, 'SUNDERBANS TO KOLKATA & FLY TO BAGDOGRA', ('Enjoy a beautiful breakfast at the resort as the morning mist lifts over the water channels. Cruise back to Godkhali Jetty and transfer in your private vehicle directly to Kolkata Airport for your domestic flight to Bagdogra. Upon landing at Bagdogra, your hill-station luxury vehicle will comfortably drive your family up the scenic mountain roads to Kalimpong.'), [
                'Sightseeing Included: Scenic Teesta River Valley Mountain Drive.',
                'Evening Experience: Relax on the veranda of a handpicked colonial bungalow overlooking misty alpine peaks.',
                'Overnight Stay: Premium Colonial Heritage Resort, Kalimpong.',
                'Meals Included: Breakfast & Alpine Valley Dinner.',
            ]),
            _day(5, 'KALIMPONG SIGHTSEEING', ('Explore Kalimpong\'s tranquil charm. Visit the Durpin Monastery (Zang Dhok Palri Phodang), located on Durpin Hill, which preserves sacred Tibetan Buddhist scriptures. Stroll through renowned international flower nurseries famous for exotic orchids, and witness historical relic archives at Morgan House. Enjoy panoramic mountain photography from the Deolo Hill view platform.'), [
                'Sightseeing Included: Durpin Monastery, Deolo Hill, Pine View Nursery, Morgan House.',
                'Optional Activities: Short family picnic at the scenic Deolo parkland gardens.',
                'Overnight Stay: Premium Colonial Heritage Resort, Kalimpong.',
                'Meals Included: Full Buffet Breakfast & Multi-cuisine Dinner.',
            ]),
            _day(6, 'KALIMPONG TO DARJEELING', ('Take a scenic, picturesque mountain drive to Darjeeling, weaving past emerald-green tea gardens clinging to steep slopes. Check into your ultra-luxury room in Darjeeling. In the afternoon, embark on an iconic train journey on the UNESCO World Heritage Darjeeling Himalayan Railway (Toy Train) steam engine joyride from Darjeeling to Ghoom Monastery, looping beautifully around the Batasia Loop war memorial.'), [
                'Sightseeing Included: Himalayan Railway Toy Train Steam Ride, Batasia Loop, Ghoom Monastery.',
                'Local Experiences: Private evening walk around the vibrant, heritage Chowrasta Mall square.',
                'Overnight Stay: Luxury Boutique Resort, Darjeeling.',
                'Meals Included: Breakfast & Fine-dining Dinner.',
            ]),
            _day(7, 'DARJEELING EARLY SUNRISE & CITY SIGHTSEEING', ('Wake up early at 4:00 AM and ride in your private 4x4 vehicle up to Tiger Hill to witness an emotional, unforgettable sunrise. Watch the sun light up the snow-capped peak of Mount Kanchenjunga in shades of gold and pink. On your drive down, visit the Himalayan Mountaineering Institute (HMI), Padmaja Naidu Himalayan Zoological Park, and watch local tea pluckers at work inside a premium estate.'), [
                'Sightseeing Included: Tiger Hill Sunrise, Zoo & HMI, Tibetan Refugee Self Help Center, Tea Estate.',
                'Food Suggestions: Enjoy authentic hot tea and baked goods at the iconic Glenary\'s Bakery.',
                'Overnight Stay: Luxury Boutique Resort, Darjeeling.',
                'Meals Included: Morning Tea, Buffet Breakfast & Luxury Dinner.',
            ]),
            _day(8, 'DARJEELING EXCURSION TO MIRIK LAKE', ('Take a relaxing day trip to the peaceful lakeside town of Mirik. The drive travels through high-altitude pine forests and borders the international boundary with Nepal. Enjoy a private, relaxing boat ride across Sumendu Lake (Mirik Lake), surrounded by a canopy of tall dhupi trees and connected by an elegant footbridge. Stop for shopping at the Pashupati Nagar border market before returning to Darjeeling.'), [
                'Sightseeing Included: Mirik Sumendu Lake, Simana Viewpoint, Pashupati Nagar Market area.',
                'Photography Points: Pine forests at Simana view marker overlooking beautiful rolling valley slopes.',
                'Overnight Stay: Luxury Boutique Resort, Darjeeling.',
                'Meals Included: Breakfast & Farewell Theme Dinner.',
            ]),
            _day(9, 'DEPARTURE FROM BAGDOGRA', ('Savor a final breakfast on your resort balcony, taking in the clean mountain air. Your private vehicle will arrive to transport your family down to Bagdogra International Airport for your return flight home. Your elite West Bengal Honeymoon / Family Tour concludes seamlessly, leaving you with incredible stories and premium memories.'), [
                'Transfers Included: Private Mountain Airport Drop-off.',
                'Meals Included: Full Gourmet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('The Peerless Inn', 'Kolkata / Sunderbans', '03 Nights', 'Deluxe', 'Superior Room', 'Breakfast & All Meals (Sunderbans)', 4, 1, description='OPTION 01 – DELUXE: The Peerless Inn / Sunderban Tiger Camp (Kolkata / Sunderbans, 03 Nights)'),
            _hotel('Summit Hermon Resort / Pine Tree Spa', 'Darjeeling / Kalimpong', '05 Nights', 'Deluxe', 'Deluxe Room', 'MAP (Breakfast + Dinner)', 4, 2, description='OPTION 01 – DELUXE: Summit Hermon Resort / Pine Tree Spa (Darjeeling / Kalimpong, 05 Nights)'),
            _hotel('ITC Sonar Luxury Collection / Sunderban Riverside Resort', 'Kolkata / Sunderbans', '03 Nights', 'Premium', 'Premium Room', 'Breakfast & All Meals (Sunderbans)', 5, 3, description='OPTION 02 – PREMIUM: ITC Sonar Luxury Collection / Sunderban Riverside Resort (Kolkata / Sunderbans, 03 Nights)'),
            _hotel('The Elgin Darjeeling / Elgin Silver Oaks Kalimpong', 'Darjeeling / Kalimpong', '05 Nights', 'Premium', 'Premium Heritage Room', 'MAP (Breakfast + Dinner)', 5, 4, description='OPTION 02 – PREMIUM: The Elgin Darjeeling / Elgin Silver Oaks Kalimpong (Darjeeling / Kalimpong, 05 Nights)'),
            _hotel('Taj Bengal Kolkata / Sunderban Luxury Eco Oasis', 'Kolkata / Sunderbans', '03 Nights', 'Luxury', 'Luxury Room', 'Breakfast & All Meals (Sunderbans)', 5, 5, description='OPTION 03 – LUXURY: Taj Bengal Kolkata / Sunderban Luxury Eco Oasis (Kolkata / Sunderbans, 03 Nights)'),
            _hotel('Mayfair Darjeeling / Mayfair Himalayan Resort', 'Darjeeling / Kalimpong', '05 Nights', 'Luxury', 'Luxury Suite', 'MAP (Breakfast + Dinner)', 5, 6, description='OPTION 03 – LUXURY: Mayfair Darjeeling / Mayfair Himalayan Resort (Darjeeling / Kalimpong, 05 Nights)'),
            _hotel('The Oberoi Grand Kolkata / Private Exclusive Jungle Villa', 'Kolkata / Sunderbans', '03 Nights', 'Ultra Luxury', 'Luxury Suite / Private Villa', 'All Inclusive', 5, 7, description='OPTION 04 – ULTRA LUXURY: The Oberoi Grand Kolkata / Private Exclusive Jungle Villa (Kolkata / Sunderbans, 03 Nights)'),
            _hotel('Windamere Hotel / Luxury Chalets', 'Darjeeling / Kalimpong', '05 Nights', 'Ultra Luxury', 'Heritage Suite / Luxury Chalet', 'All Inclusive', 5, 8, description='OPTION 04 – ULTRA LUXURY: Windamere Hotel (Heritage Suite) / Luxury Chalets (Darjeeling / Kalimpong, 05 Nights)'),
        ],
        inclusions=[
            _inc_included('Accommodation: 08 Nights luxury stay in handpicked hotels and high-end mountain chalets.', 1),
            _inc_included('Meals: Daily multi-cuisine breakfast spreads, along with all meals included during the Sunderbans segment.', 2),
            _inc_included('Transfers & Sightseeing: All city excursions and mountain transfers in a private, air-conditioned Luxury Innova Crysta.', 3),
            _inc_included('TRAGUIN Assistance: 24/7 dedicated concierge help-line, along with certified professional local companion guides.', 4),
            _inc_included('Complimentary Experiences: Private boat charter inside Sunderbans water channels and pre-booked tickets for the Darjeeling Toy Train joyride.', 5),
            _inc_included('Welcome Amenities: Luxury arrival kit containing fresh seasonal fruits, traditional handloom stoles, and premium mineral water.', 6),
            _inc_excluded('Airfare tickets from your hometown to Kolkata / Bagdogra.', 7),
            _inc_excluded('Entry tickets to historical monuments, camera permits, or park fees not explicitly mentioned.', 8),
            _inc_excluded('Personal incidentals like laundry, premium alcoholic beverages, and tips.', 9),
            _inc_excluded('Optional activities or detours outside the scheduled itinerary layout.', 10),
        ],
    )
    return package, itinerary

def build_wb_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-010'
    tour_code = 'TRAGUIN-WB-010'
    title = 'Sundarbans Mangrove Cruise Safari'
    duration = '02 Nights / 03 Days'
    slug = 'wb-010-sundarbans-mangrove-cruise-safari'
    itin_slug = 'wb-010-sundarbans-mangrove-cruise-safari-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code WB-010 | TRAGUIN tour code TRAGUIN-WB-010', 1),
            _ph('State / Country: West Bengal, India | Category: Nature / Wildlife Safari', 2),
            _ph('Destinations: Sundarbans Mangrove Forest • Gadkhali • Sajnekhali • Sudhanyakhali', 3),
            _ph('Ideal for: Nature Lovers & Families', 4),
            _ph('Best season: September to March', 5),
            _ph('Vehicle & Cruise: Luxury AC Sedan to Gadkhali Jetty + Exclusive Private Motorized Cruise Boat', 6),
            _ph('Meal Plan: All Meals Included (Gourmet Bengali & Traditional Delta Cuisines)', 7),
            _ph('Route Map: Kolkata Arrival → Gadkhali → Sajnekhali Creek Cruise → Sudhanyakhali → Dobanki → Kolkata Departure', 8),
            _ph('TRAGUIN Signature Experience: Elite eco-safari with priority forest permits and upscale cruise boat with spacious dining decks.', 9),
            _ph('Important Notes: Deep forest permits require advance booking with ID copies. Plastic items strictly prohibited inside tiger reserve.', 10),
        ],
        moods=['Wildlife', 'Nature', 'Family'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Sundarbans Mangrove Cruise Safari • 02 Nights / 03 Days',
        overview='Welcome to the untamed wilderness of the world\'s largest mangrove forest. This ultra-premium Sundarbans Family Tour, curated by TRAGUIN, offers an emotional dive into the land of the Royal Bengal Tiger. Sail seamlessly through narrow creeks, marvel at raw, breathtaking landscapes, and retreat into handpicked hotels offering eco-luxury amenities for unforgettable memories.\n\nTOUR OVERVIEW\nVehicle & Cruise: Luxury Air-Conditioned Chauffeur Sedan to Gadkhali Jetty followed by an Exclusive Private Motorized Cruise Boat. Meal Plan: All Meals Included (Gourmet Bengali & Traditional Delta Cuisines Served Onboard). Route Map: Kolkata Arrival → Gadkhali → Sajnekhali Creek Cruise → Sudhanyakhali Watchtower → Dobanki → Kolkata Departure.\n\nTRAGUIN Curated Experience Note: This is a true Premium West Bengal Experience featuring customized deep-forest entry permissions, dedicated naturalist guides, and private village interactions away from regular crowds.',
        seo_title='WB-010 | Sundarbans Mangrove Cruise Safari | TRAGUIN',
        seo_description='Premium 02 Nights / 03 Days West Bengal package (WB-010 / TRAGUIN-WB-010): Royal Bengal Tiger safari, Sajnekhali, Sudhanyakhali, Dobanki Canopy Walk, and 2-tier eco-luxury resorts.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Delta cruise on Hogol, Gomor, and Durgaduani rivers to Sajnekhali Watchtower', 1),
            _ih('Deep forest cruise through Pirkhali and Gazikhali with Sudhanyakhali tiger spotting', 2),
            _ih('Dobanki 20-foot-high fenced Canopy Walk and Panchamukhani Five River Confluence', 3),
            _ih('Exclusive guided village walk with honey-gathering traditions and Baul folk music', 4),
            _ih('2-tier handpicked eco-luxury Sundarbans accommodation (02 Nights)', 5),
        ],
        days=[
            _day(1, 'KOLKATA TO SUNDARBANS', ('Your premium journey begins with an early morning pickup from Kolkata by a professional luxury vehicle. Drive comfortably through scenic rural landscapes to Gadkhali Jetty. Here, step onto your exclusive private TRAGUIN-vetted cruise boat. Enjoy a refreshing welcome drink as you glide down the Hogol, Gomor, and Durgaduani rivers. Arrive at your eco-luxury resort, check-in seamlessly, and savor a hot traditional lunch. In the afternoon, cruise to the Sajnekhali Watchtower for your initial wildlife sightings and explore the Mangrove Interpretation Center.'), [
                'Sightseeing Included: Delta Cruise, Sajnekhali Watchtower, Crocodile Pond.',
                'Evening Experience: Witness a traditional multi-generational Baul folk music performance at the resort.',
                'Overnight Stay: Handpicked Luxury Eco-Resort, Sundarbans.',
                'Meals Included: Buffet Lunch, Afternoon Tea & Gourmet Dinner.',
            ]),
            _day(2, 'DEEP FOREST CRUISE & WATCHTOWERS', ('Awake to the peaceful calls of exotic birds. Today features an immersive full-day safari cruise through dense waterways. Sail through the narrow canopy creeks of Pirkhali and Gazikhali. Visit the famous Sudhanyakhali Watchtower, where tigers are frequently spotted near the sweet-water pond. Later, proceed to the Dobanki Watchtower to experience the unique 20-foot-high fenced Canopy Walk, putting you right inside the mangrove jungle while ensuring complete safety.'), [
                'Sightseeing Included: Deep Forest Cruise, Sudhanyakhali, Dobanki Canopy Walk, Panchamukhani (Five River Confluence).',
                'Photography Points: Golden hour over the vast mangrove river bends and basking crocodiles.',
                'Overnight Stay: Premium Eco-Resort, Sundarbans.',
                'Meals Included: Onboard Forest Breakfast, Lunch & Elegant Resort Dinner.',
            ]),
            _day(3, 'VILLAGE WALK & RETURN TO KOLKATA', ('After a relaxed breakfast, engage in an exclusive guided village walk to experience the local lifestyle, traditional clay homes, and honey-gathering stories. Board your private boat for a final cruise back to Gadkhali Jetty. Your luxury private vehicle awaits to drive you back to Kolkata, concluding your high-end safari with beautiful memories.'), [
                'Transfers Included: Private Jetty to Kolkata Airport / Hotel Drop-off.',
                'Meals Included: Breakfast & Farewell Lunch.',
            ]),
        ],
        hotels=[
            _hotel('Sundorban Tiger Camp', 'Sundarbans', '02 Nights', 'Luxury', 'Executive AC Cottage', 'All Meals Included', 4, 1, description='OPTION 01 – LUXURY: Sundorban Tiger Camp (Sundarbans, 02 Nights)'),
            _hotel('Sunderban Mangrove Retreat', 'Sundarbans', '02 Nights', 'Ultra Luxury', 'Premium Royal Suite', 'All Meals + Private Naturalist', 5, 2, description='OPTION 02 – ULTRA LUXURY: Sunderban Mangrove Retreat (Sundarbans, 02 Nights)'),
        ],
        inclusions=[
            _inc_included('Accommodation: 02 Nights stay at handpicked premium luxury eco-resorts.', 1),
            _inc_included('Meals: All breakfasts, lunches, and dinners prepared with organic, fresh ingredients.', 2),
            _inc_included('Transfers & Cruise: Private AC vehicle from Kolkata & fully private dedicated safari cruise boat.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated local concierge and professional forest companion guide.', 4),
            _inc_excluded('Flights or train connections to Kolkata.', 5),
            _inc_excluded('Forest entry fees, video camera permits, and personal tips.', 6),
        ],
    )
    return package, itinerary

def build_wb_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-011'
    tour_code = 'TQ-WB-011'
    title = 'Kolkata City of Joy Heritage Tour'
    duration = '03 Nights / 04 Days'
    slug = 'wb-011-kolkata-city-of-joy-heritage-tour'
    itin_slug = 'wb-011-kolkata-city-of-joy-heritage-tour-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code WB-011 | TRAGUIN tour code TQ-WB-011', 1),
            _ph('State / Country: West Bengal, India | Category: Heritage & Cultural Discovery', 2),
            _ph('Destinations: Kolkata (City of Joy Heritage)', 3),
            _ph('Ideal for: Families, Couples & Art Connoisseurs', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: Premium Luxury On Request', 6),
            _ph('Vehicle: Premium Mercedes-Benz / Crysta', 7),
            _ph('Route: Kolkata Historic Center • Hooghly River • North Kolkata Heritage Blocks', 8),
            _ph('TRAGUIN Signature Experience: Private entry access to exclusive classical zamindar heritage estates rarely open to the public.', 9),
            _ph('Shopping: Baluchari and Jamdani silk sarees, legendary sandesh delicacies, handcrafted terracotta pottery.', 10),
            _ph('Important Notes: Advance table reservations at fine legacy restaurants handled by TRAGUIN concierges. Wear suitable clothing for temple visits.', 11),
        ],
        moods=['Heritage', 'Culture', 'Family'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='Premium Luxury On Request',
        rating=Decimal("4.9"), review_count=0,
        tagline='Kolkata City of Joy Heritage Tour • 03 Nights / 04 Days',
        overview='Immerse yourself in the intellectual soul of India\'s cultural capital. This ultimate TRAGUIN vacation experience guides you through magnificent British colonial monuments, exclusive art galleries, vibrant old quarters, and delicious culinary traditions.\n\nTOUR OVERVIEW\nStep into the rich old-world elegance of Kolkata with a meticulously arranged, high-end travel sequence. This exclusive tour treats you to handpicked luxury boutique hotels, exceptional private transportation, and insightful culinary journeys designed by top travel consultants. Route: Kolkata Historic Center • Hooghly River • North Kolkata Heritage Blocks. Meal Plan: Royal Breakfasts & Celebrated Fine Dining Experiences (including authentic legacy lunches).\n\nTRAGUIN Premium Luxury Advantage: Front-row entry access passes, private museum curators, and handpicked artisanal encounters.\n\nDESTINATION HIGHLIGHTS\nTo enjoy the absolute finest experiences, booking the Best West Bengal Tour Package ensures unmatched cultural depth. A Luxury West Bengal Holiday uncovers the magnificent stories of ancient zamindar palaces, classic gothic revival structures, and thriving modern art forms. Kolkata remains the ultimate highlight for any culturally rich West Bengal Family Tour.',
        seo_title='WB-011 | Kolkata City of Joy Heritage Tour | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days West Bengal package (WB-011 / TQ-WB-011): Victoria Memorial, Jorasanko Thakurbari, Kumartuli, Hooghly sunset cruise, and 4-tier Kolkata hotels.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Victoria Memorial, St. Paul\'s Cathedral, and Dalhousie Square heritage vista', 1),
            _ih('Jorasanko Thakurbari, Marble Palace, College Street, and Coffee House', 2),
            _ih('Kumartuli clay studios, Dakshineswar Kali Temple VIP entry, and Hooghly sunset cruise', 3),
            _ih('Epicurean sweet shop tour with mishti treats and handloom saree boutiques', 4),
            _ih('4-tier elite Kolkata accommodation (03 Nights)', 5),
        ],
        days=[
            _day(1, 'COLONIAL MAJESTY & THE GRAND VICTORIA MEMORIAL', ('Arrive in Kolkata, where you will be met by a premium TRAGUIN representative and escorted via luxury vehicle to your iconic heritage hotel. After lunch, take a relaxed private tour of the majestic Victoria Memorial, admiring its extensive collection of oil paintings, historic artifacts, and pristine manicured gardens. Conclude your evening with a pleasant, slow drive past the beautifully illuminated heritage structures of Dalhousie Square.'), [
                'Sightseeing Included: Victoria Memorial, St. Paul\'s Cathedral, Dalhousie Square Heritage Vista.',
                'Evening Experience: Private high-tea experience inside a beautifully restored 19th-century salon.',
                'Overnight Stay: The Oberoi Grand / The Taj Bengal - Kolkata.',
                'Meals Included: Welcome Lunch, Elite Fine Dining Dinner.',
            ]),
            _day(2, 'INTELLECTUAL ROOTS & INTREPID NORTH KOLKATA HERITAGE', ('Dive deep into the artistic soul of North Kolkata. Visit Jorasanko Thakurbari, the ancestral home of Nobel Laureate Rabindranath Tagore. Walk along beautiful corridors filled with classic literary history. Later, discover the incredible architecture of the Marble Palace, an elegant private mansion filled with valuable classical sculptures and European paintings. Spend your afternoon wandering through College Street\'s famous historic book stalls and iconic intellectual cafes.'), [
                'Sightseeing Included: Jorasanko Thakurbari, Marble Palace, College Street, Coffee House.',
                'Photography Points: The grand classical courtyards of the Marble Palace; vintage hand-pulled rickshaw backdrops.',
                'Overnight Stay: The Oberoi Grand / The Taj Bengal - Kolkata.',
                'Meals Included: Breakfast, Authentic Traditional Bengali Zamindari Lunch, Dinner.',
            ]),
            _day(3, 'KUMARTULI ARTISTRY & SUNSET HOOGHLY RIVER CRUISE', ('In the morning, visit Kumartuli, the historic potters\' enclave where master craftsmen skillfully sculpt magnificent clay idols. Observe the intricate techniques used to shape traditional art. In the late afternoon, step aboard an exclusive private luxury boat for a sunset cruise on the Hooghly River. Glide smoothly beneath the iconic Howrah Bridge and Vidyasagar Setu as the city lights begin to sparkle over the calm waters.'), [
                'Sightseeing Included: Kumartuli Clay Studios, Dakshineswar Kali Temple (VIP Entry), River Hooghly Cruise.',
                'Evening Experience: TRAGUIN Sunset Cruise accompanied by classical live music performances on board.',
                'Overnight Stay: The Oberoi Grand / The Taj Bengal - Kolkata.',
                'Meals Included: Breakfast, Contemporary Fusion Lunch, Grand Farewell Dinner.',
            ]),
            _day(4, 'EPICUREAN DELIGHTS & HEARTFELT DEPARTURES', ('Enjoy a relaxed breakfast at your hotel before embarking on a specialized culinary tour of historic sweet shops to sample legendary mishti treats. Visit the famous local artisan boutiques for fine handloom sarees and beautiful terracotta souvenirs. Transfer smoothly via premium luxury vehicle to Netaji Subhash Chandra Bose International Airport for your departure home, concluding your premium TRAGUIN holiday.'), [
                'Meals Included: Breakfast Buffet, Sweet Tasting Tour.',
                'Assistance: Dedicated airport check-in support and luggage assistance.',
            ]),
        ],
        hotels=[
            _hotel('Peerless Inn Kolkata', 'Kolkata', '03 Nights', 'Deluxe', 'Superior City View Room', 'MAPAI (Breakfast & Dinner)', 4, 1, description='OPTION 01 – DELUXE: Peerless Inn Kolkata (Kolkata, 03 Nights)'),
            _hotel('ITC Sonar, Luxury Collection', 'Kolkata', '03 Nights', 'Premium', 'Executive Club Heritage Room', 'MAPAI (Breakfast & Dinner)', 5, 2, description='OPTION 02 – PREMIUM: ITC Sonar, Luxury Collection (Kolkata, 03 Nights)'),
            _hotel('The Taj Bengal, Kolkata', 'Kolkata', '03 Nights', 'Luxury', 'Luxury Club Room', 'CPAI + Gourmet Dinner Lineup', 5, 3, description='OPTION 03 – LUXURY: The Taj Bengal, Kolkata (Kolkata, 03 Nights)'),
            _hotel('The Oberoi Grand, Kolkata', 'Kolkata', '03 Nights', 'Ultra Luxury', 'Luxury Balcony Premier Suite', 'All-Inclusive Royal Boarding', 5, 4, description='OPTION 04 – ULTRA LUXURY: The Oberoi Grand, Kolkata (Kolkata, 03 Nights)'),
        ],
        inclusions=[
            _inc_included('Elite luxury accommodations at premier properties like The Oberoi Grand / Taj.', 1),
            _inc_included('Daily premium breakfast and special curated fine dining lunch/dinner experiences.', 2),
            _inc_included('Premium private AC luxury transportation for all transfers and city sightseeing.', 3),
            _inc_included('Private river boat charter and curated heritage walk specialists.', 4),
            _inc_included('TRAGUIN signature on-ground support with VIP entrance privileges.', 5),
            _inc_included('Welcome amenities, artisan souvenir gift hampers, and travel safety care.', 6),
            _inc_excluded('Airfare tickets to/from Kolkata.', 7),
            _inc_excluded('Camera or specialized media permissions at historic monuments.', 8),
            _inc_excluded('Personal gratuities, laundry, and alcoholic beverages.', 9),
            _inc_excluded('Insurance coverages or personal medical policies.', 10),
        ],
    )
    return package, itinerary

def build_wb_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-012'
    tour_code = 'TR-WB-012-HNYM'
    title = 'Romantic Dooars Wildlife & Tea Gardens'
    duration = '04 Nights / 05 Days'
    slug = 'wb-012-romantic-dooars-wildlife-tea-gardens'
    itin_slug = 'wb-012-romantic-dooars-wildlife-tea-gardens-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code WB-012 | TRAGUIN tour code TR-WB-012-HNYM', 1),
            _ph('State / Country: West Bengal, India | Category: Honeymoon Special', 2),
            _ph('Destinations: Lataguri • Gorumara • Murti • Jhalong • Bindu', 3),
            _ph('Ideal for: Couples & Honeymooners', 4),
            _ph('Best season: October to May', 5),
            _ph('Vehicle: Private Luxury AC Sedan or SUV dedicated for complete privacy', 6),
            _ph('Meal Plan: MAPAI (Sumptuous Breakfast and romantic curated dinners included)', 7),
            _ph('Route: NJP/Bagdogra → Lataguri (Gorumara) → Murti → Jhalong → Bindu → Departure', 8),
            _ph('TRAGUIN Signature Experience: Private walking tour inside a colonial-era functional tea processing facility with expert tasters.', 9),
            _ph('Shopping: Premium orthodox and CTC Darjeeling & Dooars Teas, wooden carvings, organic hill honey.', 10),
            _ph('Important Notes: Check-in 12 Noon, Check-out 11 AM. Parks closed 15 June–15 September. Jungle safari advance registration mandatory.', 11),
        ],
        moods=['Honeymoon', 'Wildlife', 'Romance'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Romantic Dooars Wildlife & Tea Gardens • 04 Nights / 05 Days',
        overview='Escape into the pristine, mist-laden foothills of the Eastern Himalayas with the ultimate luxury West Bengal Honeymoon Package. Handcrafted with passion by TRAGUIN, this romantic journey through the iconic Dooars Wildlife & Tea Gardens invites newlywed couples to lose themselves amidst lush, velvety green estates, breathtaking landscapes, and deep, mysterious forests.\n\nTOUR OVERVIEW\nVehicle: Private Luxury AC Sedan or SUV dedicated for your complete privacy. Meal Plan: MAPAI (Sumptuous Breakfast and romantic curated dinners included). Route: NJP Station/Bagdogra Airport • Lataguri (Gorumara) • Murti • Jhalong • Bindu • Departure.\n\nTRAGUIN Curated Experience Note: Includes a complimentary welcome bottle of sparkling juice, standard honeymoon room decorations, and a private candlelight dinner tucked away in a scenic forest clearing.',
        seo_title='WB-012 | Romantic Dooars Wildlife & Tea Gardens | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days West Bengal honeymoon package (WB-012 / TR-WB-012-HNYM): Gorumara safari, Murti River, Jhalong, Bindu, Samsing, and 3-tier boutique resorts.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Gorumara National Park morning jeep safari and Jatraprasad Watch Tower rhino spotting', 1),
            _ih('Murti Riverbend photography session and private candlelit dinner on hotel lawns', 2),
            _ih('Jhalong Hydro Project, Bindu Border Viewpoint, and cardamom gardens on Bhutan border', 3),
            _ih('Samsing Viewpoint, Suntalekhola hanging footbridge, and couple\'s tea-plucking experience', 4),
            _ih('3-tier romantic boutique forest and tea estate accommodation (04 Nights)', 5),
        ],
        days=[
            _day(1, 'ARRIVAL AT NJP/BAGDOGRA TO LATAGURI (GORUMARA)', ('Arrive at New Jalpaiguri Railway Station (NJP) or Bagdogra Airport (IXB), where your dedicated TRAGUIN luxury private car awaits you. Embark on a breathtaking drive through wide-open highways, cutting through the iconic Mahananda Wildlife Sanctuary. Feel the crisp mountain air as you arrive in Lataguri, the threshold of Gorumara National Park. Check into your romantic handpicked hotel with beautiful garden paths.'), [
                'Sightseeing Included: Scenic driveway through wildlife corridors.',
                'Meals Included: Dinner.',
                'Evening Experience: Romantic tribal folk dance showcase over bonfire.',
                'Overnight Stay: Handpicked Luxury Resort, Lataguri.',
            ]),
            _day(2, 'GORUMARA NATIONAL PARK WILDLIFE JEEP SAFARI', ('Wake up early to the sweet chorus of tropical birds. Board an exclusive private open-hood 4x4 Jeep for a thrilling morning safari inside Gorumara National Park. Accompanied by a professional naturalist, scan the horizon from the famous Jatraprasad Watch Tower to spot the legendary Indian One-Horned Rhinoceros, herds of wild elephants, and barking deer. Return for a lazy breakfast. In the afternoon, visit the breathtaking banks of the Murti River for an exclusive photography session.'), [
                'Sightseeing Included: Gorumara Jungle Safari, Jatraprasad Tower, Murti Riverbend.',
                'Meals Included: Breakfast & Dinner.',
                'Evening Experience: Private Candlelit Dinner arranged on hotel lawns by TRAGUIN.',
                'Overnight Stay: Handpicked Luxury Resort, Lataguri.',
            ]),
            _day(3, 'EXCURSION TO MISTY JALONG, BINDU & SULTANEKHOLA', ('Today, your West Bengal Sightseeing leads you to the hidden gems of the Dooars foothills. Drive through dense tea garden estates towards Jhalong, located beautifully on the banks of the Jaldhaka River. Sip hot cardamom coffee as you gaze across the hills into Bhutan. Continue to Bindu, the last village on the Indian border, famous for cardamom plantations and sweeping views of the river dam.'), [
                'Sightseeing Included: Jhalong Hydro Project, Bindu Border Viewpoint, Cardamom Gardens.',
                'Meals Included: Breakfast & Dinner.',
                'Evening Experience: Stargazing and romantic acoustic music session by the resort pool.',
                'Overnight Stay: Handpicked Luxury Resort, Lataguri.',
            ]),
            _day(4, 'SAMSING, SUNTALEKHOLA & TEA ESTATE ROMANCE', ('After a delicious breakfast, journey to Samsing, a beautiful countryside hamlet draped in dense orange orchards and tea gardens. Take an intimate walk together across the hanging footbridge at Suntalekhola, suspended over a gurgling hill stream. Afterwards, walk through our handpicked premium tea estate where you can participate in a romantic couple\'s tea-plucking experience.'), [
                'Sightseeing Included: Samsing Viewpoint, Suntalekhola Stream, Premium Tea Estates.',
                'Meals Included: Breakfast & Dinner.',
                'Evening Experience: Special couple\'s premium spa and relaxation treatment.',
                'Overnight Stay: Premium Eco-Resort / Tea Bungalow, Dooars.',
            ]),
            _day(5, 'LATAGURI TO NJP / BAGDOGRA DEPARTURE', ('Enjoy your final breakfast overlooking the emerald tea gardens. Capture some final couple portraits in the beautiful morning light. Check out from your premium stay as your private luxury vehicle arrives to drive you smoothly back to New Jalpaiguri Station (NJP) or Bagdogra Airport (IXB) for your onward flight home.'), [
                'Sightseeing Included: Departure airport/station drop transfers.',
                'Meals Included: Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Green Lagoon Resort / Resort Rhino', 'Lataguri / Dooars', '04 Nights', 'Deluxe', 'Deluxe Cottage', 'MAPAI (Breakfast & Dinner)', 4, 1, description='OPTION 01 – DELUXE: Green Lagoon Resort / Resort Rhino (04 Nights)'),
            _hotel('Sinclair\'s Retreat Dooars / Resort Gorumara Nest', 'Lataguri / Dooars', '04 Nights', 'Premium', 'Premium Room', 'MAPAI (Breakfast & Dinner)', 4, 2, description='OPTION 02 – PREMIUM: Sinclair\'s Retreat Dooars / Resort Gorumara Nest (04 Nights)'),
            _hotel('Handpicked Tea Estate Heritage Bungalow', 'Lataguri / Dooars', '04 Nights', 'Luxury', 'Heritage Bungalow Suite', 'MAPAI (Breakfast & Dinner)', 5, 3, description='OPTION 03 – LUXURY: Handpicked Tea Estate Heritage Bungalow by TRAGUIN (04 Nights)'),
        ],
        inclusions=[
            _inc_included('Premium accommodation in romantic boutique forest/tea resorts on a double occupancy basis.', 1),
            _inc_included('Daily freshly cooked breakfast and curated candlelit dinners at the resort.', 2),
            _inc_included('Complete private sightseeing transfers in a dedicated luxury air-conditioned vehicle.', 3),
            _inc_included('Complimentary honeymoon package benefits (bed decoration, cake, and welcome drinks).', 4),
            _inc_included('Continuous backend concierge tracking and support provided by TRAGUIN.', 5),
            _inc_included('All toll charges, state permits, driver food, and overnight allowances.', 6),
            _inc_excluded('Flight or train tickets connecting to Bagdogra/NJP.', 7),
            _inc_excluded('Gorumara National Park forest safari entry tickets and mandatory government guide hiring fees.', 8),
            _inc_excluded('Personal tips, snacks, mineral water bottles, and laundry charges.', 9),
            _inc_excluded('Any insurance coverage charges.', 10),
        ],
    )
    return package, itinerary

def build_wb_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-013'
    tour_code = 'TRAGUIN-WB-013'
    title = 'TRAGUIN Elgin Darjeeling Heritage Luxury Stay Tour Package'
    duration = '03 Nights / 04 Days'
    slug = 'wb-013-elgin-darjeeling-heritage-luxury-stay'
    itin_slug = 'wb-013-elgin-darjeeling-heritage-luxury-stay-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code WB-013 | TRAGUIN tour code TRAGUIN-WB-013', 1),
            _ph('State / Country: West Bengal, India | Category: Luxury Mountain Retreat', 2),
            _ph('Destinations: Darjeeling • Tiger Hill • Ghoom', 3),
            _ph('Ideal for: Luxury Travelers & Honeymooners', 4),
            _ph('Best season: March to May & October to December', 5),
            _ph('Premium Hotel: The Elgin, Darjeeling — legendary King George V era heritage property', 6),
            _ph('TRAGUIN Signature Experience: Private cultural interactions and exclusive heritage entries.', 7),
            _ph('Shopping: Hand-woven textiles, tribal artifacts, premium tea varieties, and heritage crafts.', 8),
            _ph('Important Notes: Check-in 14:00 hrs, check-out 11:00 hrs. Dedicated vehicle per approved TRAGUIN itinerary. Heritage site entries require prior reservations.', 9),
        ],
        moods=['Luxury', 'Honeymoon', 'Heritage'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='TRAGUIN Elgin Darjeeling Heritage Luxury Stay • 03 Nights / 04 Days',
        overview='Welcome to a truly magnificent luxury vacation experience planned specifically for you. Every detail of this itinerary has been curated by TRAGUIN Experts to offer premium comfort, unforgettable memories, and scenic beauty.\n\nDESTINATION STRATEGIC INSIGHTS\nWhy Visit Darjeeling: Offering breathtaking views of the world\'s highest peaks and world-renowned tea estates, Darjeeling is perfect for a Luxury Darjeeling Holiday or a romantic Darjeeling Honeymoon Package. Premium Handpicked Experiences: Staying at the legendary Elgin heritage luxury resort combined with a classic UNESCO Toy Train ride guarantees an elite, unforgettable mountain getaway. Best Time to Visit Darjeeling: March to May and October to December provide the clearest panoramic views of Mount Kanchenjunga.',
        seo_title='WB-013 | Elgin Darjeeling Heritage Luxury Stay | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days West Bengal package (WB-013 / TRAGUIN-WB-013): The Elgin Darjeeling, Tiger Hill sunrise, Toy Train, tea garden tour, and 4 Elgin room tiers.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('The Elgin heritage hotel with colonial history session and Chowrasta Mall walk', 1),
            _ih('Tiger Hill sunrise, Ghoom Monastery, Batasia Loop, and UNESCO Toy Train steam ride', 2),
            _ih('Heritage Darjeeling Tea Estate tour with exclusive tea-tasting masterclass', 3),
            _ih('Himalayan Mountaineering Institute, Zoo with Red Panda and Snow Leopard, Tibetan Refugee Center', 4),
            _ih('4 Elgin room tiers: Deluxe Heritage, Luxury Heritage Suite, Grand Executive, Royal Emperor (03 Nights)', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN DARJEELING – THE ELGIN HERITAGE EXPERIENCE', ('Your luxury Himalayan experience begins with a scenic drive from Bagdogra Airport to the Queen of the Hills. Arrive at The Elgin, Darjeeling—a legendary luxury heritage hotel that reflects King George V era elegance. Sip a welcoming cup of authentic Darjeeling first-flush tea by the fireplace while your TRAGUIN coordinator completes a seamless in-room check-in. Spend a relaxed evening walking around the historic Mall Road (Chowrasta) breathing in the fresh mountain air.'), [
                'Sightseeing Included: Chowrasta Mall, The Elgin Heritage Property Walk.',
                'Evening Experience: Exclusive high tea and colonial history session at The Elgin Lounge.',
                'Overnight Stay: Darjeeling (The Elgin Heritage Luxury Stay).',
                'Meals Included: Welcome Dinner.',
            ]),
            _day(2, 'TIGER HILL SUNRISE & THE DARJEELING TOY TRAIN RIDE', ('Wake up early for a premium highlight: a private luxury vehicle ride to Tiger Hill to watch the sunrise paint Mount Kanchenjunga in golden hues. On your return, visit the tranquil Ghoom Monastery and Batasia Loop. After a delicious breakfast at The Elgin, enjoy an iconic ride on the UNESCO World Heritage Darjeeling Himalayan Railway (Toy Train)—a classic immersive experience through breathtaking landscapes.'), [
                'Sightseeing Included: Tiger Hill Sunrise, Ghoom Monastery, Batasia Loop, Toy Train Steam Ride.',
                'Evening Experience: Fine dining featuring curated Himalayan and Continental cuisines.',
                'Overnight Stay: Darjeeling (The Elgin).',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(3, 'TEA GARDEN IMMERSION & HIMALAYAN ALPINE EXPLORATION', ('Discover the secrets behind the world\'s most premium tea with a curated tour of a heritage Darjeeling Tea Estate. Walk alongside traditional tea pluckers and enjoy an exclusive tea-tasting masterclass. In the afternoon, explore the Himalayan Mountaineering Institute (HMI) and meet rare alpine species at the Padmaja Naidu Himalayan Zoological Park, including the endangered Red Panda and Snow Leopard.'), [
                'Sightseeing Included: Heritage Tea Garden Tour, Himalayan Mountaineering Institute, Zoo, Tibetan Refugee Self-Help Center.',
                'Evening Experience: Local warm Tibetan hot-pot (Gyathuk) dining suggestion.',
                'Overnight Stay: Darjeeling (The Elgin).',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(4, 'DEPARTURE FROM THE QUEEN OF THE HILLS', ('Enjoy a relaxed morning breakfast overlooking the mist-filled valleys from the gardens of The Elgin. Your premium Darjeeling Sightseeing holiday draws to a close. Board your luxury private vehicle for a comfortable return transfer to Bagdogra Airport/NJP Railway Station, taking home unforgettable memories curated exclusively by your premier travel experts at TRAGUIN.'), [
                'Sightseeing Included: Scenic Mirik Lake Route (Optional en-route stop).',
                'Meals Included: Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('The Elgin, Darjeeling', 'Darjeeling', '03 Nights', 'Deluxe', 'Deluxe Heritage Room', 'MAPAI (Breakfast & Dinner)', 5, 1, description='DELUXE: The Elgin, Darjeeling — Deluxe Heritage Room (03 Nights)'),
            _hotel('The Elgin, Darjeeling', 'Darjeeling', '03 Nights', 'Premium', 'Luxury Heritage Suite', 'MAPAI (Breakfast & Dinner)', 5, 2, description='PREMIUM: The Elgin, Darjeeling — Luxury Heritage Suite (03 Nights)'),
            _hotel('The Elgin, Darjeeling', 'Darjeeling', '03 Nights', 'Luxury', 'Grand Executive Suite', 'MAPAI (Breakfast & Dinner)', 5, 3, description='LUXURY: The Elgin, Darjeeling — Grand Executive Suite (03 Nights)'),
            _hotel('The Elgin, Darjeeling', 'Darjeeling', '03 Nights', 'Ultra Luxury', 'Royal Emperor Suite', 'MAPAI (Breakfast & Dinner)', 5, 4, description='ULTRA LUXURY: The Elgin, Darjeeling — Royal Emperor Suite (03 Nights)'),
        ],
        inclusions=[
            _inc_included('Luxury handpicked premium accommodations as per selected plan.', 1),
            _inc_included('Professional English/Hindi speaking tour managers and destination experts.', 2),
            _inc_included('Dedicated luxury air-conditioned private transportation throughout the route.', 3),
            _inc_included('All sightseeing entries, special permissions, and curated experiences.', 4),
            _inc_included('Comprehensive TRAGUIN 24/7 VIP desk support during the entire tour.', 5),
            _inc_included('Refreshments, welcome amenities, and surprise local souvenirs.', 6),
            _inc_excluded('Airfare, flight tickets, or train bookings to and from the starting destination.', 7),
            _inc_excluded('Personal expenses such as laundry, premium telephone calls, bar bills, and tips.', 8),
            _inc_excluded('Optional adventure activities or specialized local guide upgrades not in the itinerary.', 9),
            _inc_excluded('Travel insurance policies and medical evacuation coverages.', 10),
        ],
    )
    return package, itinerary

def build_wb_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-014'
    tour_code = 'TR-WB-014-PREMIUM'
    title = 'Gangasagar Divine Spiritual Tour'
    duration = '02 Nights / 03 Days'
    slug = 'wb-014-gangasagar-divine-spiritual-tour'
    itin_slug = 'wb-014-gangasagar-divine-spiritual-tour-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code WB-014 | TRAGUIN tour code TR-WB-014-PREMIUM', 1),
            _ph('State / Country: West Bengal / India | Category: Pilgrimage & Heritage', 2),
            _ph('Destinations: Kolkata • Gangasagar • Kolkata', 3),
            _ph('Ideal for: Seniors, Families & Spiritual Seekers', 4),
            _ph('Best season: October to March', 5),
            _ph('TRAGUIN Signature Experience: Private, priority entry arrangements for senior citizens at major temples.', 6),
            _ph('Curated by TRAGUIN Experts: Seamless transit transitions perfectly paced for senior comfort.', 7),
            _ph('Premium Handpicked Hotels: Properties chosen specifically for wheelchair access and high-end hospitality.', 8),
            _ph('Important Notes: Check-in 14:00 hrs, check-out 12:00 noon. Gangasagar transit relies on ferry timings and tidal conditions.', 9),
        ],
        moods=['Pilgrimage', 'Heritage', 'Family'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Gangasagar Divine Spiritual Tour • 02 Nights / 03 Days',
        overview='Welcome to an extraordinary spiritual odyssey curated meticulously by TRAGUIN. Embark on the highly revered Best West Bengal Tour Package, designed specifically to blend sacred traditions with an unparalleled level of premium comfort. This exclusive West Bengal Family Tour takes you deep into the heart of India\'s spiritual heritage, guiding you effortlessly to the sacred confluence where the holy River Ganges meets the majestic Bay of Bengal.\n\nTOUR OVERVIEW\nThis meticulously structured Luxury West Bengal Holiday features seamless, end-to-end luxury private transfers via air-conditioned premium vehicles, exceptionally comfortable stays at handpicked hotels, and curated culinary experiences. Our custom route guarantees a relaxed pace ideal for a timeless pilgrimage, complete with a dedicated TRAGUIN companion to ensure flawless assistance throughout your divine journey.',
        seo_title='WB-014 | Gangasagar Divine Spiritual Tour | TRAGUIN',
        seo_description='Premium 02 Nights / 03 Days West Bengal package (WB-014 / TR-WB-014-PREMIUM): Kalighat Temple, Gangasagar holy dip, Victoria Memorial, and 4-tier Kolkata hotels.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Kalighat Temple private evening darshan and Vidyasagar Setu heritage drive', 1),
            _ih('Exclusive speed-boat transit to Gangasagar with holy dip at sacred confluence and Kapil Muni Ashram', 2),
            _ih('Victoria Memorial, Mother House, and iconic Howrah Bridge photo-op', 3),
            _ih('Traditional mishti dahi, rosogollas, and premium Bengali lunch suggestions', 4),
            _ih('4-tier premium Kolkata accommodation (02 Nights)', 5),
        ],
        days=[
            _day(1, 'KOLKATA ARRIVAL — WELCOME TO THE CITY OF JOY & SPIRITUAL AWAKENING', ('Your magnificent journey commences with a warm welcome at Kolkata Airport or Railway Station, where a dedicated TRAGUIN luxury representative awaits you. Step into your premium private vehicle and transfer effortlessly to your luxury handpicked hotel. After a seamless check-in, enjoy a relaxed afternoon soaking in the cultural charm of Kolkata. In the evening, immerse yourself in a soulful visit to the iconic Kalighat Temple for a private, hassle-free evening darshan.'), [
                'Sightseeing Included: Kalighat Temple Darshan, Vidyasagar Setu, Heritage Drive.',
                'Evening Experience: Private Aarti viewing and traditional Bengali welcome dinner.',
                'Overnight Stay: Kolkata (Premium Luxury Property).',
                'Meals Included: Dinner.',
            ]),
            _day(2, 'KOLKATA TO GANGASAGAR EXCURSION — THE SACRED CONFLUENCE', ('Awake early for the ultimate spiritual highlight of your Luxury West Bengal Holiday. Enjoy a nutritious, early breakfast before departing in premium comfort toward Lot No. 8. From here, experience an exclusive speed-boat transit across the Muriganga River to Kachuberia, where a private vehicle takes you directly to the sacred Kapil Muni Ashram. Participate in immersive experiences, take a holy dip at the tranquil confluence, and enjoy a peaceful afternoon absorbed in unforgettable memories of devotion.'), [
                'Sightseeing Included: Holy Confluence, Kapil Muni Ashram, Kachuberia, Sagar Island.',
                'Optional Activities: Personalized Vedic rituals and customized family prayers arranged upon request.',
                'Evening Experience: Relaxing premium transit back with curated onboard refreshments.',
                'Overnight Stay: Kolkata (Premium Luxury Property).',
                'Meals Included: Breakfast, Lunch, Dinner.',
            ]),
            _day(3, 'KOLKATA SIGHTSEEING & DEPARTURE — COLONIAL HERITAGE & FAREWELL', ('Savor a luxurious buffet breakfast at your hotel before embarking on a brief, curated tour of Kolkata\'s most magnificent landmarks. Marvel at the breathtaking landscapes surrounding the iconic Victoria Memorial, and pay your respects at the serene Mother House. Indulge in some fine boutique shopping at local markets for exclusive traditional sarees and handpicked authentic souvenirs. Conclude your tour with exceptional memories as TRAGUIN ensures a smooth, timely transfer to the airport or railway station.'), [
                'Sightseeing Included: Victoria Memorial, Mother House, Iconic Howrah Bridge Photo-op.',
                'Food Suggestions: Traditional mishti dahi, rosogollas, and premium standard Bengali lunch.',
                'Meals Included: Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('The Peerless Inn / Pride Plaza Hotel', 'Kolkata', '02 Nights', 'Deluxe', 'Superior Room', 'CP (Breakfast Only)', 4, 1, description='OPTION 01 – DELUXE: The Peerless Inn / Pride Plaza Hotel (Kolkata, 02 Nights)'),
            _hotel('Novotel Hotel & Residences / ITC Fortune', 'Kolkata', '02 Nights', 'Premium', 'Premium Room', 'MAPAI (Breakfast & Dinner)', 4, 2, description='OPTION 02 – PREMIUM: Novotel Hotel & Residences / ITC Fortune (Kolkata, 02 Nights)'),
            _hotel('The Oberoi Grand / Taj Bengal', 'Kolkata', '02 Nights', 'Luxury', 'Luxury Heritage Room', 'Luxury Meal Plan', 5, 3, description='OPTION 03 – LUXURY: The Oberoi Grand / Taj Bengal (Kolkata, 02 Nights)'),
            _hotel('ITC Sonar / ITC Royal Bengal', 'Kolkata', '02 Nights', 'Ultra Luxury', 'Executive Suite with Butler Service', 'All Inclusive Curated Meals', 5, 4, description='OPTION 04 – ULTRA LUXURY: ITC Sonar / ITC Royal Bengal (Kolkata, 02 Nights)'),
        ],
        inclusions=[
            _inc_included('Premium accommodation at handpicked properties.', 1),
            _inc_included('Daily breakfast and curated specialty dinners.', 2),
            _inc_included('Private luxury AC transportation for all sightseeing.', 3),
            _inc_included('Exclusive private speed boat tickets to Gangasagar.', 4),
            _inc_included('Dedicated 24/7 TRAGUIN local guest assistance.', 5),
            _inc_included('All applicable government taxes and parking fees.', 6),
            _inc_excluded('Airfare or train tickets to/from Kolkata.', 7),
            _inc_excluded('Monument entry tickets and camera fees.', 8),
            _inc_excluded('Personal expenses like laundry, tips, and drinks.', 9),
            _inc_excluded('Optional traditional ritual or pooja charges.', 10),
            _inc_excluded('Any mandatory holiday or festival peak surcharges.', 11),
        ],
    )
    return package, itinerary

def build_wb_015(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-015'
    tour_code = 'TRAGUIN-WB-015'
    title = 'Lepchajagat • Lava • Lolegaon Canopy Walk Serenity'
    duration = '04 Nights / 05 Days'
    slug = 'wb-015-lepchajagat-lava-lolegaon-serenity'
    itin_slug = 'wb-015-lepchajagat-lava-lolegaon-serenity-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code WB-015 | TRAGUIN tour code TRAGUIN-WB-015', 1),
            _ph('State / Country: West Bengal / India | Category: Offbeat Nature & Serenity Tour', 2),
            _ph('Destinations: Lepchajagat • Lava • Lolegaon • Kalimpong', 3),
            _ph('Ideal for: Nature Lovers, Couples, Families, Photographers', 4),
            _ph('Best season: October to June', 5),
            _ph('Vehicle: Premium Private 4WD SUV dedicated throughout mountain trails', 6),
            _ph('Meal Plan: Modified American Plan (Breakfast & Dinner Included)', 7),
            _ph('Route: NJP/Bagdogra Arrival → Lepchajagat → Lava → Lolegaon → NJP/Bagdogra Departure', 8),
            _ph('TRAGUIN Signature Experience: Curated morning tea-tasting tour with an expert local sommelier.', 9),
            _ph('Shopping: Organic cardamom, alpine cheese (Chhurpi), Tibetan woolens, and Darjeeling tea.', 10),
            _ph('Important Notes: Mountain weather unpredictable — carry warm layers. Canopy Walk subject to forest department clearance. Advance booking advisable.', 11),
        ],
        moods=['Offbeat', 'Nature', 'Serenity'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Lepchajagat • Lava • Lolegaon Canopy Walk Serenity • 04 Nights / 05 Days',
        overview='Escape into the misty, untouched pine forests of the Eastern Himalayas. This Premium West Bengal Offbeat Experience transports you far away from commercial tourist tracks into a world of pristine silence, cozy luxury mountain lodges, and spellbinding panoramic views of Mount Kanchenjunga. Curated exclusively by TRAGUIN for discerning travelers who seek peaceful indulgence.\n\nTOUR OVERVIEW\nTravel Dates: Flexible / As per preference. Group / FIT: Bespoke Private Luxury Tour. Vehicle: Premium Private 4WD SUV dedicated throughout the mountain trails. Meal Plan: Modified American Plan (Breakfast & Dinner Included). Route: NJP/Bagdogra Arrival → Lepchajagat → Lava → Lolegaon → NJP/Bagdogra Departure.\n\nTRAGUIN Curated Experience Note: Luxury boutique stays overlooking mountain ridges, private bonfire dinners, early morning sunrise trail assistance, and seamless high-altitude transfers.',
        seo_title='WB-015 | Lepchajagat Lava Lolegaon Serenity | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days West Bengal offbeat package (WB-015 / TRAGUIN-WB-015): Lepchajagat pine forests, Lava Monastery, Lolegaon Canopy Walk, and 4-tier boutique mountain lodges.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Lepchajagat sunrise over Kanchenjunga and whispering pine forest nature walk', 1),
            _ih('Kalimpong Delo Park, Pine View Nursery en route to cloud-kissed Lava hamlet', 2),
            _ih('Lava Monastery (Kagyu Thegchen Ling) and Lolegaon Canopy Walk among century-old pines', 3),
            _ih('Jhandi Dara Sunrise Point and private bonfire dinner with gourmet finger food', 4),
            _ih('4-tier combined boutique mountain lodges: Lepchajagat & Lava (04 Nights)', 5),
        ],
        days=[
            _day(1, 'ARRIVAL NJP / BAGDOGRA TO LEPCHAJAGAT', ('Your premium mountain escape begins the moment you land at Bagdogra Airport or arrive at New Jalpaiguri (NJP) Railway Station. A designated TRAGUIN hospitality concierge will welcome you and escort you to your private high-performance luxury SUV. Enjoy a beautiful, winding scenic drive through emerald tea estates and misty alpine forests up to Lepchajagat. Upon checking into your premium boutique resort, unwind with a steaming cup of authentic Darjeeling tea while watching the sun descend over the tranquil Himalayan valleys.'), [
                'Sightseeing Included: Scenic foothills transit, Mirik Lake (en route optional).',
                'Optional Activities: Evening tea tasting session.',
                'Evening Experience: Mountain sunset viewing from your private balcony.',
                'Overnight Stay: Lepchajagat.',
                'Meals Included: Dinner.',
            ]),
            _day(2, 'LEPCHAJAGAT SERENITY & PINE FOREST WALK', ('Wake up early to witness a breathtaking sunrise painting Mount Kanchenjunga in hues of gold and crimson. After an artisanal breakfast, join our local expert for a gentle, curated nature walk through the whispering pine forests of Lepchajagat. Discover hidden viewpoints, enjoy bird-spotting, and indulge in pristine photography sessions. The afternoon is kept completely at leisure for you to enjoy the premium amenities of your boutique lodge.'), [
                'Sightseeing Included: Sunrise point walk, Lepchajagat Pine Reserve.',
                'Optional Activities: Village heritage walk.',
                'Evening Experience: Private bonfire dinner with local folk music.',
                'Overnight Stay: Lepchajagat.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(3, 'LEPCHAJAGAT TO LAVA VIA KALIMPONG', ('Following breakfast, we check out and drive towards the pristine town of Lava, passing through the beautiful city of Kalimpong. En route, stop to visit the serene Delo Park for majestic views of the Teesta River and the magnificent Pine View Nursery, famed for its massive collection of exotic cacti. Arrive at Lava by afternoon—a quiet hamlet wrapped in everlasting clouds. Check into your premium resort and spend the evening enjoying a cozy fireplace dinner.'), [
                'Sightseeing Included: Delo Park Kalimpong, Pine View Nursery.',
                'Optional Activities: Kalimpong local market stroll.',
                'Evening Experience: Cozy fireside dining and mountain storytelling.',
                'Overnight Stay: Lava.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(4, 'LAVA SIGHTSEEING & LOLEGAON CANOPY WALK', ('Today features one of the most immersive experiences of your holiday. First, visit the beautiful, peaceful Lava Monastery (Kagyu Thegchen Ling Monastery) nestled amidst the clouds. Then, take a short, beautiful drive to Lolegaon to experience the famous Canopy Walk. Walk across secure, swaying footbridges suspended high up in the tree tops of the heritage forest, feeling completely at one with nature. Visit Jhandi Dara Sunrise Point before returning to your premium resort for your final night.'), [
                'Sightseeing Included: Lava Monastery, Lolegaon Canopy Walk, Jhandi Dara Viewpoint.',
                'Optional Activities: Traditional wood-carving viewing.',
                'Evening Experience: Premium farewell multi-cuisine dinner curated by the chef.',
                'Overnight Stay: Lava.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(5, 'DEPARTURE FROM LAVA TO NJP / BAGDOGRA', ('Enjoy a final luxury breakfast overlooking the cloud-kissed pine valleys. Pack your bags along with your unforgettable memories of this pristine offbeat wonderland. Your private luxury SUV will pick you up for a smooth, relaxed drive down to NJP Railway Station or Bagdogra Airport for your journey back home, concluding your premium TRAGUIN experience.'), [
                'Sightseeing Included: Return mountain transfer.',
                'Optional Activities: Last-minute roadside tea estate photography.',
                'Evening Experience: Onward departure assistance.',
                'Overnight Stay: End of Tour.',
                'Meals Included: Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Humro Home Lepchajagat & Lava Pine Resort', 'Lepchajagat / Lava', '04 Nights', 'Deluxe', 'Deluxe Mountain Room', 'MAP Plan', 4, 1, description='OPTION 01 – DELUXE: Humro Home Lepchajagat & Lava Pine Resort | MAP Plan | 4 Nights'),
            _hotel('Saluja Residency Mountain Lodge / WBFDC Forest Cottages', 'Lepchajagat / Lava', '04 Nights', 'Premium', 'Premium Mountain Cottage', 'MAP Plan', 4, 2, description='OPTION 02 – PREMIUM: Saluja Residency Mountain Lodge / WBFDC Forest Cottages | MAP Plan | 4 Nights'),
            _hotel('The Senses Resort Lepchajagat & Orchid Luxury Lodge Lava', 'Lepchajagat / Lava', '04 Nights', 'Luxury', 'Luxury Valley View Suite', 'MAP Plan', 5, 3, description='OPTION 03 – LUXURY: The Senses Resort Lepchajagat & Orchid Luxury Lodge Lava | MAP Plan | 4 Nights'),
            _hotel('Elite Heritage Boutique Chalet', 'Lepchajagat / Lava', '04 Nights', 'Ultra Luxury', 'Private Valley View Chalet', 'MAP Plan', 5, 4, description='OPTION 04 – ULTRA LUXURY: Elite Heritage Boutique Chalet with private valley views | MAP Plan | 4 Nights'),
        ],
        inclusions=[
            _inc_included('Accommodation: 04 Nights stay at selected premium mountain chalets and boutique resorts.', 1),
            _inc_included('Meals: Daily organic breakfast and multi-cuisine dinners.', 2),
            _inc_included('Transfers: Dedicated private premium luxury 4WD SUV for all transits and sightseeing.', 3),
            _inc_included('Sightseeing: Complete guided tours including entry permits to Canopy Walk and viewpoints.', 4),
            _inc_included('Assistance: 24/7 dedicated on-call operational support from mountain travel experts.', 5),
            _inc_included('Taxes: All luxury resort taxes, driver allowances, toll fees, and green mountain permits.', 6),
            _inc_included('Welcome Amenities: Choice of freshly brewed Darjeeling First Flush Tea or hot cocoa upon arrival.', 7),
            _inc_included('Complimentary Experiences: Private evening bonfire with gourmet finger food.', 8),
            _inc_included('TRAGUIN Support: Real-time remote route monitoring for total comfort.', 9),
            _inc_excluded('Airfare or train tickets to Bagdogra / New Jalpaiguri.', 10),
            _inc_excluded('Personal expenses such as laundry, liquor, telephone calls, or tips.', 11),
            _inc_excluded('Extra costs arising due to mountain landslides, roadblocks, or political strikes.', 12),
            _inc_excluded('Travel or medical insurance.', 13),
        ],
    )
    return package, itinerary

def build_wb_016(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-016'
    tour_code = 'TRAGUIN-WB-016-LUX'
    title = 'Digha • Mandarmani Coastal Beach Break'
    duration = '03 Nights / 04 Days'
    slug = 'wb-016-digha-mandarmani-coastal-beach-break'
    itin_slug = 'wb-016-digha-mandarmani-coastal-beach-break-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code WB-016 | TRAGUIN tour code TRAGUIN-WB-016-LUX', 1),
            _ph('State / Country: West Bengal / India | Category: Leisure / Coastal Beach Break', 2),
            _ph('Destinations: Digha, Mandarmani', 3),
            _ph('Ideal for: Families, Couples, Solo Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium Tier)', 6),
            _ph('Vehicle Assigned: Premium Air-Conditioned Sedan / SUV', 7),
            _ph('Route Map: Kolkata → Digha (1N) → Mandarmani (2N) → Kolkata Departure', 8),
            _ph('TRAGUIN Signature Experience: Private beachside high-tea set up against the sunset.', 9),
            _ph('Shopping: Sea shell handicrafts, pure cotton handloom sarees, fresh pomfret and prawns.', 10),
            _ph('Important Notes: Check-in 12:00 PM, check-out 11:00 AM. Water sports subject to sea safety clearances. Book 30-45 days ahead during holidays.', 11),
        ],
        moods=['Beach', 'Leisure', 'Family'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Digha • Mandarmani Coastal Beach Break • 03 Nights / 04 Days',
        overview='Welcome to an unforgettable journey along the sun-kissed sands and rolling surf of the Bay of Bengal. The Best West Bengal Tour Package presents an exquisite escape from urban life into a world of pristine marine horizons and soothing coastal breezes. Handcrafted with precision, this luxury West Bengal Family Tour and West Bengal Honeymoon Package weaves together the historic allure of Digha with the tranquil, premium exclusivity of Mandarmani\'s expansive shores.\n\nTOUR OVERVIEW\nTravel Dates: Flexible / Custom. Group Type: FIT / Private Luxury Tour. Vehicle Assigned: Premium Air-Conditioned Sedan / SUV. Meal Plan: CP / MAPAI (Breakfast & Dinner Included). Route Map: Kolkata → Digha (1N) → Mandarmani (2N) → Kolkata Departure. Curated Note: Includes a personalized beachfront high-tea experience and priority access to premium water sports.',
        seo_title='WB-016 | Digha Mandarmani Coastal Beach Break | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days West Bengal package (WB-016 / TRAGUIN-WB-016-LUX): Digha, Mandarmani beach, Chandaneswar Temple, water sports, and 4-tier coastal accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Amrabati Park, New Digha Beach Promenade, Science Centre, and sunset seafood tasting', 1),
            _ih('Chandaneswar Shiva Temple, Udaipur Beach, Talsari Beach, and Mandarmani private coastline', 2),
            _ih('Mandarmani water sports — parasailing, jet skiing, banana boat, and Mohana River Estuary', 3),
            _ih('Private starlit beach bonfire with live-grill dinner and red crab photography viewpoints', 4),
            _ih('4-tier handpicked accommodation: Digha (01 Night) + Mandarmani (02 Nights)', 5),
        ],
        days=[
            _day(1, 'KOLKATA TO DIGHA — ARRIVAL & SUNSET AT NEW DIGHA BEACH', ('Your premium coastal holiday begins with a warm, VIP greeting by our professional chauffeur at your residence or airport/railway station in Kolkata. Step into your private luxury vehicle and embark on a smooth, scenic drive through the verdant landscapes of rural Bengal towards the historic town of Digha. Upon arrival, check into your handpicked premium hotel and experience traditional welcome amenities. In the afternoon, begin your curated Digha Sightseeing tour.'), [
                'Sightseeing Included: Amrabati Park, New Digha Beach Promenade, Science Centre Complex.',
                'Evening Experience: Sensory sunset stroll, seafood tasting tour, and handloom shopping at local markets.',
                'Optional Activities: Speed boating at Amrabati Lake or a private photography session on the beach.',
                'Overnight Stay: Handpicked Premium Luxury Hotel in Digha.',
                'Meals Included: Welcome Drink & Premium Buffet Dinner.',
            ]),
            _day(2, 'DIGHA TO MANDARMANI — SPIRITUAL HERITAGE & LUXURY RESORT', ('Awake to the soothing rhythm of crashing ocean waves. After a gourmet breakfast, check out and drive towards the pristine white sands of Mandarmani. En route, experience an immersive cultural excursion to the ancient Chandaneswar Shiva Temple. Following this, take a scenic drive to Udaipur Beach and Talsari Beach, famous for their unique deltaic formations, pristine casuarina groves, and dynamic red crab colonies. Cross over into Mandarmani—a haven of luxury and calm.'), [
                'Sightseeing Included: Chandaneswar Temple, Udaipur Beach, Talsari Beach, Mandarmani private coastline.',
                'Evening Experience: Private beachside high-tea experience with artisanal snacks while watching the twilight fade.',
                'Optional Activities: Rejuvenating luxury spa session or traditional Ayurvedic therapies within the resort.',
                'Overnight Stay: Ultra-Luxury Beachfront Resort in Mandarmani.',
                'Meals Included: Breakfast & Specially Curated Beachside Dinner.',
            ]),
            _day(3, 'MANDARMANI EXPERIENCES — WATER SPORTS & BEACH BONFIRE', ('A perfect day dedicated entirely to luxury, relaxation, and thrill on the longest motorable beach in India. Start your morning with a spectacular view of the sun emerging from the open sea horizon. For adventure enthusiasts, Mandarmani offers an immersive array of premium water sports. Under professional guidance, enjoy exhilarating parasailing, jet skiing, or high-speed banana boat rides on the gentle waves. In the afternoon, travel to the famous Mohana (River Estuary). Conclude your day with a luxurious, private beach bonfire arranged exclusively for you under a clear, starlit coastal sky.'), [
                'Sightseeing Included: Mandarmani River Estuary (Mohana), Red Crab Viewpoints, Local Fishing Villages.',
                'Evening Experience: Private starlit beach bonfire with personalized multi-cuisine live-grill dinner options.',
                'Optional Activities: ATV Quad Biking on the sand tracks or Parasailing high above the Bay of Bengal.',
                'Overnight Stay: Ultra-Luxury Beachfront Resort in Mandarmani.',
                'Meals Included: Gourmet Breakfast & Exclusive Beach Bonfire Dinner.',
            ]),
            _day(4, 'MANDARMANI TO KOLKATA — FINAL SUNRISE & DEPARTURE', ('Conclude your luxury holiday with a final, serene morning walk along the calm waters of Mandarmani Beach. Enjoy a lavish buffet breakfast spread featuring international and local coastal delicacies. Pack your bags with fond memories as you check out of your resort. Your private luxury vehicle will be waiting to transfer you comfortably back to Kolkata. En route, stop at popular local souvenir hubs to purchase authentic local handicrafts and sweet treats.'), [
                'Sightseeing Included: En-route panoramic landscapes, rural handicraft stops.',
                'Evening Experience: Safe drop-off at your final destination in Kolkata.',
                'Optional Activities: Traditional Bengali lunch stop at a renowned premium highway restaurant.',
                'Overnight Stay: Tour Concludes.',
                'Meals Included: Sumptuous Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Hotel Sgres / Similar', 'Digha', '01 Night', 'Deluxe', 'Executive AC Room', 'CP / MAPAI', 4, 1, description='OPTION 01 – DELUXE: Hotel Sgres / Similar (Digha, 01 Night)'),
            _hotel('Sun City Resort / Similar', 'Mandarmani', '02 Nights', 'Deluxe', 'Executive AC Room', 'CP / MAPAI', 4, 2, description='OPTION 01 – DELUXE: Sun City Resort / Similar (Mandarmani, 02 Nights)'),
            _hotel('Le ROI Digha / Similar', 'Digha', '01 Night', 'Premium', 'Premium Sea Facing Room', 'CP / MAPAI', 4, 3, description='OPTION 02 – PREMIUM: Le ROI Digha / Similar (Digha, 01 Night)'),
            _hotel('Victerra Resort / Similar', 'Mandarmani', '02 Nights', 'Premium', 'Premium Sea Facing Room', 'CP / MAPAI', 4, 4, description='OPTION 02 – PREMIUM: Victerra Resort / Similar (Mandarmani, 02 Nights)'),
            _hotel('Hotel Sea Hawk / Premium Block', 'Digha', '01 Night', 'Luxury', 'Luxury Balcony Ocean Suite', 'CP / MAPAI', 5, 5, description='OPTION 03 – LUXURY: Hotel Sea Hawk / Premium Block (Digha, 01 Night)'),
            _hotel('The Sonar Bangla Mandarmani', 'Mandarmani', '02 Nights', 'Luxury', 'Luxury Balcony Ocean Suite', 'CP / MAPAI', 5, 6, description='OPTION 03 – LUXURY: The Sonar Bangla Mandarmani (Mandarmani, 02 Nights)'),
            _hotel('Sayantan Beach Resort Luxe', 'Digha', '01 Night', 'Ultra Luxury', 'Ultra Luxury Private Beach Cottage', 'CP / MAPAI', 5, 7, description='OPTION 04 – ULTRA LUXURY: Sayantan Beach Resort Luxe (Digha, 01 Night)'),
            _hotel('The Mandarmani Regenta / Sana Beach', 'Mandarmani', '02 Nights', 'Ultra Luxury', 'Ultra Luxury Private Beach Cottage', 'CP / MAPAI', 5, 8, description='OPTION 04 – ULTRA LUXURY: The Mandarmani Regenta / Sana Beach (Mandarmani, 02 Nights)'),
        ],
        inclusions=[
            _inc_included('Accommodation: Handpicked premium stays across choices from Deluxe to Ultra Luxury tiers.', 1),
            _inc_included('Meals: Daily breakfasts and dinners included as per selected gourmet menu frameworks.', 2),
            _inc_included('Transfers: Dedicated private luxury air-conditioned sedan/SUV for all long drives and local tours.', 3),
            _inc_included('Sightseeing: Complete curated sightseeing itineraries including entrance arrangements as detailed.', 4),
            _inc_included('Assistance: 24/7 dedicated telephone support from your personal travel planner.', 5),
            _inc_included('Taxes: All standard government taxes, fuel surcharges, toll fees, and driver allowances covered.', 6),
            _inc_included('Welcome Amenities: Refreshing traditional welcome drink and cold towels upon resort arrivals.', 7),
            _inc_included('Complimentary Experiences: One exclusive private beachside high-tea set up at Mandarmani.', 8),
            _inc_included('TRAGUIN Support: Real-time digital updates and coordination from professional consultants throughout.', 9),
            _inc_excluded('Flights or Train ticket bookings to and from Kolkata.', 10),
            _inc_excluded('Entry tickets to amusement parks, museum exhibitions, or special temple entry passes.', 11),
            _inc_excluded('Personal expenses such as laundry services, premium telephone charges, and bar tabs.', 12),
            _inc_excluded('Optional water sports activities (Parasailing, Jet Skiing, ATV rides, etc.).', 13),
            _inc_excluded('Travel insurance coverage and medical expenses.', 14),
            _inc_excluded('Additional meals or midnight room-service ordering not highlighted in inclusions.', 15),
            _inc_excluded('Optional customized tour deviations or extra vehicle mileage requests.', 16),
        ],
    )
    return package, itinerary

def build_wb_017(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-017'
    tour_code = 'TRG-WB-017-ADVR'
    title = 'Sandakphu Trek & Vintage Land Rover Premium Experience'
    duration = '06 Nights / 07 Days'
    slug = 'wb-017-sandakphu-vintage-land-rover-adventure'
    itin_slug = 'wb-017-sandakphu-vintage-land-rover-adventure-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code WB-017 | TRAGUIN tour code TRG-WB-017-ADVR', 1),
            _ph('State / Country: West Bengal / India | Category: Adventure & Wildlife', 2),
            _ph('Destinations: Manebhanjan • Tumling • Sandakphu • Phalut', 3),
            _ph('Ideal for: Adventure Seekers & Luxury Explorers', 4),
            _ph('Best season: October to May', 5),
            _ph('Vehicle: Private Luxury SUV + Traditional Heritage Land Rover for the Ridge', 6),
            _ph('Meal Plan: MAPAI (Breakfast, Premium Dinner, and Evening High Tea)', 7),
            _ph('Route: Bagdogra → Manebhanjan → Tumling → Sandakphu → Phalut → Darjeeling', 8),
            _ph('TRAGUIN Signature Experience: Private champagne or gourmet hot chocolate toast upon reaching the Sandakphu summit.', 9),
            _ph('Important Notes: Sandakphu at 11,929 ft — stay hydrated. Carry heavy woolens and windcheaters. Ridge route restricted to certified heritage 4x4 vehicles.', 10),
        ],
        moods=['Adventure', 'Wildlife', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Sandakphu Trek & Vintage Land Rover Premium Experience • 06 Nights / 07 Days',
        overview='Welcome to an extraordinary escape crafted by TRAGUIN. Embark on the ultimate Luxury West Bengal Holiday that takes you along the legendary Singalila Ridge. Witness the majestic Sleeping Buddha mountain formation and enjoy a curated, premium journey through breathtaking landscapes, combining classic Himalayan trekking elements with the iconic vintage 1950s Land Rover experience.\n\nTOUR OVERVIEW\nRoute: Bagdogra • Manebhanjan • Tumling • Sandakphu • Phalut • Darjeeling. Vehicle: Private Luxury SUV for transfers & Traditional Heritage Land Rover for the Ridge. Meal Plan: MAPAI (Breakfast, Premium Dinner, and Evening High Tea). Vibe: Immersive, Luxurious, Scenic, and Emotionally Uplifting.',
        seo_title='WB-017 | Sandakphu Vintage Land Rover Adventure | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days West Bengal package (WB-017 / TRG-WB-017-ADVR): Singalila Ridge, Sandakphu peak, Phalut, vintage Land Rover, Tiger Hill, and 4-tier mountain accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Vintage 1950s Land Rover ascent through Chitrey and Lameydhura to Tumling meadows', 1),
            _ih('Sandakphu Peak (11,929 ft) with 360-degree views of Everest, Kanchenjunga, Lhotse, and Makalu', 2),
            _ih('Phalut day-excursion along the world\'s most scenic ridge trail', 3),
            _ih('Darjeeling Tiger Hill sunrise, Toy Train, HMI, Zoo, and Glenary\'s pastries', 4),
            _ih('4-tier accommodation: Manebhanjan/Tumling/Sandakphu ridge (04 Nights) + Darjeeling (02 Nights)', 5),
        ],
        days=[
            _day(1, 'ARRIVAL AT BAGDOGRA TO MANEBHANJAN', ('Your unforgettable journey begins with a warm welcome by a TRAGUIN representative at Bagdogra Airport. From here, enjoy a scenic drive winding through emerald green tea estates and misty pine forests up to Manebhanjan, the historic starting point of the Sandakphu trail. Breathe in the crisp, pure Himalayan air as you transition into a slower, deeply rejuvenating mountain rhythm.'), [
                'Sightseeing Included: Mirik Lake (en-route), Simana Viewpoint, Pine Forest scenic drives.',
                'Evening Experience: Private orientation session with your TRAGUIN mountain guide over artisan local tea.',
                'Overnight Stay: Premium Handpicked Himalayan Eco-Lodge, Manebhanjan.',
                'Meals Included: Welcome Drink & Gourmet Dinner.',
            ]),
            _day(2, 'MANEBHANJAN TO TUMLING — VINTAGE LAND ROVER ASCENT', ('Today, step into your exclusively reserved, beautifully maintained vintage 1950s Land Rover. Feel the thrill of a bygone era as the classic 4x4 negotiates the steep, rugged terrain through Chitrey and Lameydhura. Arrive at the peaceful village of Tumling. The evening presents a mesmerizing sunset over the Nepalese hills, filling your heart with unforgettable memories.'), [
                'Sightseeing Included: Chitrey Monastery, Singalila National Park Entry Checkpoint, Tumling Meadows.',
                'Photography Points: Spectacular views of the valleys shifting below the clouds.',
                'Overnight Stay: Curated Premium Lodge / Shikhar Luxury Homestay, Tumling.',
                'Meals Included: Organic Breakfast & Hot Traditional Dinner.',
            ]),
            _day(3, 'TUMLING TO SANDAKPHU — THE ROOF OF WEST BENGAL', ('Wake up early to catch a breathtaking sunrise. After breakfast, your Land Rover continues its dramatic ascent along the border ridge, driving through Kalapokhri—famous for its sacred black pond. Then, ascend the challenging hairpin curves to reach Sandakphu, the pinnacle of your Luxury West Bengal Holiday. The 360-degree theater of snow-capped giants will leave you speechless.'), [
                'Sightseeing Included: Kalapokhri Lake, Sandakphu Peak Sightseeing, Sunset over the Sleeping Buddha.',
                'Optional Activities: A short, guided alpine walk to a nearby viewpoint for unmatched solace.',
                'Overnight Stay: Sandakphu Premium Alpine Suite (Best available heated comfort).',
                'Meals Included: Power Breakfast, Local Cuisine Lunch, and Dinner.',
            ]),
            _day(4, 'SANDAKPHU EXCURSION TO PHALUT — PRISTINE WILDERNESS RIDGE', ('A truly immersive experience awaits as we embark on a day-excursion towards Phalut. The road between Sandakphu and Phalut is one of the most scenic trails in the world, running along the ridge with continuous views of Everest and Kanchenjunga. The stark, pristine beauty of Phalut feels like touching the edge of the sky. Return to Sandakphu by evening to witness another dramatic celestial display.'), [
                'Sightseeing Included: Phalut Viewpoint, Singalila Forest deep ridges, high-altitude grassland view.',
                'Evening Experience: Cozy bonfire setup (weather permitting) with hot local rhododendron beverages.',
                'Overnight Stay: Sandakphu Premium Alpine Suite.',
                'Meals Included: Breakfast, Packed Ridge Lunch, and Dinner.',
            ]),
            _day(5, 'SANDAKPHU TO DARJEELING — DESCENT TO THE QUEEN OF HILLS', ('Bid farewell to the high peaks as your Land Rover smoothly brings you down to Manebhanjan. Here, you will switch to your luxury private SUV and travel towards Darjeeling. Check into your premium colonial-style resort. Spend your evening strolling down the iconic Mall Road, enjoying a stark contrast of vibrant café culture after the silent mountains.'), [
                'Sightseeing Included: Lepchajagat viewpoint, Darjeeling Chowrasta, Mahakal Temple.',
                'Food Suggestions: Fresh pastries at Glenary\'s and authentic tea tasting at Nathmulls.',
                'Overnight Stay: Luxury Heritage Resort (Mayfair Darjeeling / Elgin or similar).',
                'Meals Included: Breakfast & Elegant Multi-cuisine Dinner.',
            ]),
            _day(6, 'DARJEELING ICONIC SIGHTSEEING — COLONIAL SPLENDOR', ('Start before dawn with a luxury excursion to Tiger Hill to watch the sun turn Kanchenjunga into pure gold. Return for a lavish breakfast, then visit the Himalayan Mountaineering Institute and take a ride on the UNESCO World Heritage Darjeeling Himalayan Railway (Toy Train). This day beautifully balances historic culture with majestic natural viewpoints.'), [
                'Sightseeing Included: Tiger Hill Sunrise, Ghoom Monastery, Batasia Loop, Padmaja Naidu Himalayan Zoological Park.',
                'Shopping: Handwoven Tibetan carpets, fine Darjeeling tea, local handicrafts.',
                'Overnight Stay: Luxury Heritage Resort, Darjeeling.',
                'Meals Included: Elite Breakfast & Grand Farewell Dinner.',
            ]),
            _day(7, 'DEPARTURE FROM BAGDOGRA', ('After a leisurely breakfast overlooking the tea valleys, enjoy a comfortable luxury transfer back to Bagdogra Airport. Your premium TRAGUIN West Bengal Package concludes here, leaving you with timeless stories, pristine mountain energy, and unforgettable memories to cherish forever.'), [
                'Transfers: Private Chauffeur driven Luxury SUV to airport.',
                'Meals Included: Lavish Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Himalayan Retreat / Shikhar Lodge / Sunrise Alpine Lodge', 'Manebhanjan / Tumling / Sandakphu', '04 Nights', 'Deluxe', 'Alpine Lodge Room', 'MAPAI (Breakfast & Dinner)', 3, 1, description='OPTION 01 – DELUXE: Himalayan Retreat / Shikhar Lodge / Sunrise Alpine Lodge (Ridge, 04 Nights)'),
            _hotel('Dekeling Resort / Cedar Inn', 'Darjeeling', '02 Nights', 'Deluxe', 'Deluxe Room', 'MAPAI (Breakfast & Dinner)', 4, 2, description='OPTION 01 – DELUXE: Dekeling Resort / Cedar Inn (Darjeeling, 02 Nights)'),
            _hotel('Tumling Eco Resort / Sandakphu Chalet (Heated)', 'Manebhanjan / Tumling / Sandakphu', '04 Nights', 'Premium', 'Premium Suite', 'MAPAI (Breakfast & Dinner)', 4, 3, description='OPTION 02 – PREMIUM: Tumling Eco Resort / Sandakphu Chalet (Ridge, 04 Nights)'),
            _hotel('The Elgin Heritage Resort', 'Darjeeling', '02 Nights', 'Premium', 'Heritage Room', 'MAPAI (Breakfast & Dinner)', 5, 4, description='OPTION 02 – PREMIUM: The Elgin Heritage Resort (Darjeeling, 02 Nights)'),
            _hotel('TRAGUIN Elite Mountain Villa / Sandakphu Star Suite', 'Manebhanjan / Tumling / Sandakphu', '04 Nights', 'Luxury', 'Star Suite', 'MAPAI (Breakfast & Dinner)', 5, 5, description='OPTION 03 – LUXURY: TRAGUIN Elite Mountain Villa / Sandakphu Star Suite (Ridge, 04 Nights)'),
            _hotel('Mayfair Hill Resort Exclusive Mountain Cottage', 'Darjeeling', '02 Nights', 'Luxury', 'Mountain Cottage', 'MAPAI (Breakfast & Dinner)', 5, 6, description='OPTION 03 – LUXURY: Mayfair Hill Resort Exclusive Mountain Cottage (Darjeeling, 02 Nights)'),
            _hotel('TRAGUIN Horizon View Presidential', 'Manebhanjan / Tumling / Sandakphu', '04 Nights', 'Ultra Luxury', 'Presidential Suite', 'MAPAI (Breakfast & Dinner)', 5, 7, description='OPTION 04 – ULTRA LUXURY: TRAGUIN Horizon View Presidential (Ridge, 04 Nights)'),
            _hotel('Windamere Colonial Hotel', 'Darjeeling', '02 Nights', 'Ultra Luxury', 'Colonial Heritage Suite', 'MAPAI (Breakfast & Dinner)', 5, 8, description='OPTION 04 – ULTRA LUXURY: Windamere Colonial Hotel (Darjeeling, 02 Nights)'),
        ],
        inclusions=[
            _inc_included('Luxury accommodation in handpicked premium hotels.', 1),
            _inc_included('Daily breakfast, evening high-tea, and multi-cuisine gourmet dinners.', 2),
            _inc_included('Exclusive Heritage Land Rover (4x4) rental for the entire ridge journey.', 3),
            _inc_included('Private luxury SUV (Innova/XUV) for airport transfers and Darjeeling sightseeing.', 4),
            _inc_included('Singalila National Park permits, eco-fees, and entry formalities.', 5),
            _inc_included('Dedicated, professional local mountain guide and TRAGUIN support team.', 6),
            _inc_included('Welcome premium amenities & localized mineral water supplies.', 7),
            _inc_excluded('Airfare or Train tickets to/from Bagdogra.', 8),
            _inc_excluded('Personal expenses like laundry, alcoholic beverages, phone calls.', 9),
            _inc_excluded('Monastery/Museum entry tickets or Toy Train joyride tickets.', 10),
            _inc_excluded('Travel and emergency high-altitude medical insurance.', 11),
            _inc_excluded('Tips for drivers, guides, and hotel staff.', 12),
            _inc_excluded('Optional tours or activities not mentioned in the itinerary.', 13),
        ],
    )
    return package, itinerary

def build_wb_018(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-018'
    tour_code = 'TRAG-WB-018-NAV'
    title = 'Murshidabad Nawabi Tour — Historic Nawabi Trail Experience'
    duration = '03 Nights / 04 Days'
    slug = 'wb-018-murshidabad-nawabi-trail'
    itin_slug = 'wb-018-murshidabad-nawabi-trail-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code WB-018 | TRAGUIN tour code TRAG-WB-018-NAV', 1),
            _ph('State / Country: West Bengal / India | Category: Heritage Tour', 2),
            _ph('Destinations: Murshidabad Historic Nawabi Trail', 3),
            _ph('Ideal for: History Buffs, Royals Lovers, Families', 4),
            _ph('Best season: October to March', 5),
            _ph('TRAGUIN Signature Experience: Private curated access to royal archives and interactive session inside Cossimbazar Palace.', 6),
            _ph('Curated by TRAGUIN Experts: Seamless routing mapped to showcase authentic weavers of royal Baluchari silk sarees live.', 7),
            _ph('Shopping: Handloomed Baluchari sarees and local Chanabora sweets.', 8),
            _ph('Important Notes: Scenic overland drive from Kolkata. Full transit luggage support by accompanying chauffeur.', 9),
        ],
        moods=['Heritage', 'History', 'Culture'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Murshidabad Nawabi Tour — Historic Nawabi Trail • 03 Nights / 04 Days',
        overview='Step directly back into the magnificent golden era of the Nawabs of Bengal. Our highly recommended Best West Bengal Tour Package takes you along the pristine banks of the Bhagirathi River into legendary Murshidabad. Proudly curated by TRAGUIN, this iconic Luxury West Bengal Holiday promises an epic glimpse into massive European-style palaces, ancient structural ruins, and opulent craftsmanship.\n\nWHY EXPERIENCE THE ROYALTY OF MURSHIDABAD?\nMurshidabad is the ultimate crown jewel for historical seekers. Families searching for an elite West Bengal Family Tour marvel at the sheer architectural variance from grand Italianate arches to pristine Islamic domes. The absolute Best Time to Visit West Bengal\'s royal sector is late autumn and winter when gentle river mist blankets the majestic structures. The iconic Hazarduari Palace—boasting 1,000 real and false doors—stands proudly as a centerpiece of our premium West Bengal Sightseeing layout.',
        seo_title='WB-018 | Murshidabad Nawabi Trail | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days West Bengal package (WB-018 / TRAG-WB-018-NAV): Hazarduari Palace, Katra Masjid, Cossimbazar Palace, Bhagirathi river cruise, and 4-tier heritage hotels.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Hazarduari Palace Museum with 1,000 doors, Nizamat Imambara, and Katra Masjid', 1),
            _ih('Jahankosha Cannon and optional vintage horse-drawn carriage (Tanga) ride', 2),
            _ih('Cossimbazar Palace Royal Chambers, Nashipur Rajbari, and Kathgola Gardens', 3),
            _ih('Private Bhagirathi River cruise with royal folk musicians on board', 4),
            _ih('Khushbagh tomb of Nawab Siraj-ud-Daulah and 4-tier heritage Murshidabad accommodation (03 Nights)', 5),
        ],
        days=[
            _day(1, 'KOLKATA TO MURSHIDABAD — ENTRY INTO THE NAWABI KINGDOM', ('Your premium journey starts early from Kolkata city. Board your TRAGUIN private luxury vehicle for a highly scenic, comfortable driven cruise towards Murshidabad. Wind past historic towns and endless lush paddy fields. Upon reaching Murshidabad, check into your premium heritage resort. Spend the evening completely at leisure, listening to the ambient sounds of the nearby river or strolling through beautiful royal orchards.'), [
                'Sightseeing Included: Scenic Overland Private Drive, Heritage Hotel Transfer, Evening Leisure Stroll.',
                'Evening Experience: Gourmet traditional dinner introducing classic aromatic Sheherwali cuisine items.',
                'Overnight Stay: Elite Handpicked Heritage Resort in Murshidabad.',
                'Meals Included: Dinner.',
            ]),
            _day(2, 'THE MAGNIFICENT HAZARDUARI PALACE & ROYAL ARCHITECTURE', ('Dedicate your morning to the legendary Hazarduari Palace, designed by grand British architects for the Nawabs. Wander through spectacular collections of real royal armor, mirrors, and precious art canvases. Afterwards, explore the massive Nizamat Imambara located right opposite. Conclude your daylight hours by capturing photographs outside the Katra Masjid, an imposing mosque built by Nawab Murshid Quli Khan with unique fortification towers.'), [
                'Sightseeing Included: Hazarduari Palace Museum, Nizamat Imambara, Katra Masjid, Jahankosha Cannon.',
                'Optional Activities: A vintage horse-drawn carriage ride (Tanga) around the historic perimeter wall ruins.',
                'Overnight Stay: Premium Heritage Resort in Murshidabad.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(3, 'COOSIMBAZAR PALACES & BHAGIRATHI RIVER SUNSET', ('Today, explore the exceptionally maintained Cossimbazar Palace Royal Chambers. Walk straight past pristine family ballrooms, vintage clocks, and antique furniture. Learn the rich history of silk trading that brought global merchants here. In the late afternoon, step aboard an exclusive private wooden country boat arranged by TRAGUIN on the Bhagirathi River, floating right past historical tombstones as the evening sun descends gracefully.'), [
                'Sightseeing Included: Cossimbazar Palace, Nashipur Rajbari, Kathgola Gardens & Jain Temple Complex.',
                'Evening Experience: Serene private river cruise with royal folk musicians performing on board.',
                'Overnight Stay: Heritage Resort in Murshidabad.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(4, 'DEPARTURE TO KOLKATA — UNFORGETTABLE MEMORIES OF THE NAWABS', ('Savor an early morning breakfast. Visit Khushbagh across the river to pay soft homage at the final resting place of Nawab Siraj-ud-Daulah. Following this, pack your bags with precious handloomed Baluchari sarees and return smoothly in your luxury private car back to Kolkata. Arrive late afternoon at the airport or station with everlasting, unforgettable memories of the Nawabi Trail.'), [
                'Sightseeing Included: Khushbagh Tomb, Return Private Overland Cruise Drive to Kolkata.',
                'Assistance: Full transit luggage support by the accompanying chauffeur.',
                'Meals Included: Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Hotel Sagnik Murshidabad or similar', 'Murshidabad', '03 Nights', 'Deluxe', 'Deluxe Executive AC Room', 'Breakfast & Dinner', 4, 1, description='OPTION 01 – DELUXE: Hotel Sagnik Murshidabad or similar (Murshidabad, 03 Nights)'),
            _hotel('Cossimbazar Palace Heritage Stay (Chhoti Rajbari)', 'Murshidabad', '03 Nights', 'Premium', 'Royal Heritage Classic Room', 'Breakfast & Dinner', 4, 2, description='OPTION 02 – PREMIUM: Cossimbazar Palace Heritage Stay (Murshidabad, 03 Nights)'),
            _hotel('The Bari Kothi Heritage Hotel (Azimganj)', 'Murshidabad', '03 Nights', 'Luxury', 'Heritage Suite (Heritage Experience)', 'Breakfast & Dinner', 5, 3, description='OPTION 03 – LUXURY: The Bari Kothi Heritage Hotel (Murshidabad, 03 Nights)'),
            _hotel('The Bari Kothi Heritage Luxury Palace', 'Murshidabad', '03 Nights', 'Ultra Luxury', 'Maharaja Premium Suite', 'All Inclusive Royal Gastronomy Plan', 5, 4, description='OPTION 04 – ULTRA LUXURY: The Bari Kothi Heritage Luxury Palace (Murshidabad, 03 Nights)'),
        ],
        inclusions=[
            _inc_included('03 Nights stay in premium palaces or elite riverfront properties.', 1),
            _inc_included('Daily breakfast arrays and thematic Nawabi-style dinners.', 2),
            _inc_included('Fully dedicated AC sedan or SUV for all intercity transits.', 3),
            _inc_included('Exclusive private boat ride across the sacred Bhagirathi River.', 4),
            _inc_included('Heritage walk assistance and curated palace entrance handling.', 5),
            _inc_included('Inclusive of fuel charges, tolls, parking, and driver meal allowances.', 6),
            _inc_included('Continuous 24/7 TRAGUIN holiday supervisor tracking.', 7),
            _inc_excluded('Airfare or long-distance railway tickets to Kolkata hub.', 8),
            _inc_excluded('Local monuments ticket costs or guide service fee charges.', 9),
            _inc_excluded('Personal tips, laundry, internal shopping, or beverage items.', 10),
            _inc_excluded('Insurance parameters or unforeseen road blocks expense.', 11),
            _inc_excluded('Any element missing inside the inclusion list column.', 12),
        ],
    )
    return package, itinerary

def build_wb_019(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-019'
    tour_code = 'TG-WB-019'
    title = 'Jaldapara • Buxa Tiger Reserve • Jayanti • Chilapata Wildlife Tour'
    duration = '04 Nights / 05 Days'
    slug = 'wb-019-jaldapara-buxa-jayanti-chilapata-wildlife'
    itin_slug = 'wb-019-jaldapara-buxa-jayanti-chilapata-wildlife-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code WB-019 | TRAGUIN tour code TG-WB-019', 1),
            _ph('State / Country: West Bengal / India | Category: Nature, Wildlife Adventure', 2),
            _ph('Destinations: Jaldapara • Buxa Tiger Reserve • Jayanti • Chilapata', 3),
            _ph('Ideal for: Wildlife Enthusiasts, Families', 4),
            _ph('Best season: November to May', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle: Luxury Air-Conditioned SUV for all intercity transfers', 7),
            _ph('Meal Plan: All Meals Included (Jungle Gourmet Breakfast, Lunch & Dinner)', 8),
            _ph('Route: NJP/Bagdogra → Jaldapara → Buxa Tiger Reserve → Chilapata → Departure', 9),
            _ph('Important Notes: Parks closed 15 June–15 September. Government ID mandatory for safari passes.', 10),
        ],
        moods=['Wildlife', 'Nature', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request',
        rating=Decimal("4.9"), review_count=0,
        tagline='Jaldapara • Buxa Tiger Reserve • Jayanti • Chilapata • 04 Nights / 05 Days',
        overview='Immerse yourself in the raw, untouched wilderness of Dooars with TRAGUIN. This luxury holiday package invites you to witness the pristine habitats of the rare One-Horned Rhinoceros and the elusive Bengal Tiger. Experience breathtaking landscapes, premium forest stays, and handpicked resort experiences designed to connect you deeply with nature.\n\nTOUR OVERVIEW\nVehicle: Luxury Air-Conditioned SUV for all intercity transfers. Meal Plan: All Meals Included (Jungle Gourmet Breakfast, Lunch & Dinner). Route: NJP/Bagdogra Arrival → Jaldapara National Park → Buxa Tiger Reserve → Chilapata Forest → Departure.\n\nTRAGUIN Curated Experience Note: Pre-booked premium safari slots, exclusive open-hood gypsies, and dinner setups under the starlit sky.',
        seo_title='WB-019 | Jaldapara Buxa Jayanti Chilapata Wildlife | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days West Bengal wildlife package (WB-019 / TG-WB-019): Jaldapara rhino safari, Chilapata forest, Buxa Fort, Jayanti riverbed, and 2-tier forest lodges.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Jaldapara morning open-jeep or elephant safari for One-Horned Rhinoceros', 1),
            _ih('Chilapata Forest drive and Nalrajan Garh (Fort of King Nala) ruins', 2),
            _ih('Jayanti riverside village safari with Bhutan hills backdrop and Mahakal Cave path', 3),
            _ih('Buxa Fort trek or Rajabhatkhawa Nature Interpretation Center with bonfire barbecue', 4),
            _ih('2-tier forest lodges: Jaldapara (02 Nights) + Buxa/Rajabhatkhawa (02 Nights)', 5),
        ],
        days=[
            _day(1, 'NJP / BAGDOGRA TO JALDAPARA — GATEWAY TO THE DOOARS WILDERNESS', ('Arrive at NJP or Bagdogra Airport where your dedicated TRAGUIN driver will meet you. Journey through mesmerizing tea gardens and breathtaking landscapes towards Jaldapara National Park. Check into your handpicked premium luxury resort bordering the forest lines. Spend a peaceful evening listening to the ambient sounds of the jungle as your naturalist presents an introductory briefing over high tea.'), [
                'Arrival Experience: Private luxury transfer with premium refreshments onboard.',
                'Evening Experience: Local tribal dance performance followed by a lavish buffet dinner.',
                'Overnight Stay: Luxury Resort in Jaldapara.',
                'Meals Included: Evening Snacks & Dinner.',
            ]),
            _day(2, 'JALDAPARA RHINO SAFARI & CHILAPATA FOREST', ('Wake up early for an exhilarating open-jeep or elephant safari inside Jaldapara National Park, famous for holding the largest population of Indian One-Horned Rhinoceros after Kaziranga. Keep your camera ready at the photography points to capture bison, deer, and diverse bird species. Return for a sumptuous breakfast. In the afternoon, explore the deep, mysterious corridors of Chilapata Forest, discovering the historical ruins of Nalrajan Garh (Fort of King Nala).'), [
                'Sightseeing Included: Jaldapara Morning Safari, Chilapata Jungle Drive, Nalrajan Garh Ruins.',
                'Immersive Experiences: Deep-forest wildlife tracking with certified naturalists.',
                'Overnight Stay: Jaldapara Premium Luxury Resort.',
                'Meals Included: Breakfast, Lunch & Dinner.',
            ]),
            _day(3, 'JALDAPARA TO BUXA TIGER RESERVE & JAYANTI', ('After breakfast, transfer to the spectacular Buxa Tiger Reserve. Check into your premium eco-luxury lodge nestled near the forest borders. In the afternoon, embark on an exclusive safari towards Jayanti, a picturesque riverside village bordering Bhutan. The breathtaking landscapes of the dry Jayanti riverbed against the majestic Bhutan hills create an unforgettable memory and premium Instagram locations.'), [
                'Sightseeing Included: Jayanti Riverbed, Mahakal Cave path, Buxa forest trails.',
                'Photography Points: Stunning landscape shots of the Eastern Himalayas crossing into Bhutan.',
                'Overnight Stay: Luxury Eco-Lodge in Buxa/Rajabhatkhawa.',
                'Meals Included: Breakfast, Lunch & Dinner.',
            ]),
            _day(4, 'BUXA FORT TREK & RAJABHATKHAWA INTERPRETATION CENTER', ('Enjoy an optional, gentle trek to the historic Buxa Fort, a heritage site holding deep links to India\'s freedom struggle. For senior citizens or relaxed travelers, a smooth alternative vehicle option takes you to the Rajabhatkhawa Nature Interpretation Center, showcasing deep wildlife insights. Spend your afternoon enjoying a private birdwatching trail organized exclusively by TRAGUIN experts.'), [
                'Sightseeing Included: Buxa Fort (or alternative nature center), Pokhari Lake path.',
                'Evening Experience: A premium bonfire experience with fine barbecue delicacies cooked by private chefs.',
                'Overnight Stay: Buxa / Rajabhatkhawa.',
                'Meals Included: Breakfast, Lunch & Dinner.',
            ]),
            _day(5, 'DEPARTURE TO NJP / BAGDOGRA', ('Savor your final breakfast surrounded by wilderness. Pack your bags along with memorable souvenirs, premium local tea leaves, and thousands of wildlife photographs. Enjoy a comfortable private transfer back to NJP or Bagdogra Airport for your journey onward, carrying the luxurious mark of a TRAGUIN crafted holiday.'), [
                'Sightseeing Included: En-route view of pristine South Khayerbari leopard rescue center (time permitting).',
                'Meals Included: Gourmet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('The Hollong Lodge / Jaldapara Tourist Lodge Premium', 'Jaldapara', '02 Nights', 'Luxury', 'Premium Forest Cottage', 'All Meals (APAI)', 4, 1, description='OPTION 01 – LUXURY: The Hollong Lodge / Jaldapara Tourist Lodge Premium (Jaldapara, 02 Nights)'),
            _hotel('The Buxa Tiger Roar Resort / Similar Luxury Eco-Lodge', 'Buxa / Rajabhatkhawa', '02 Nights', 'Luxury', 'Luxury Eco-Lodge Room', 'All Meals (APAI)', 4, 2, description='OPTION 01 – LUXURY: The Buxa Tiger Roar Resort / Similar (Buxa, 02 Nights)'),
            _hotel('Resort Mystic Dooars / Similar', 'Jaldapara', '02 Nights', 'Premium', 'Premium Forest Room', 'All Meals (APAI)', 4, 3, description='OPTION 02 – PREMIUM: Resort Mystic Dooars / Similar (Jaldapara, 02 Nights)'),
            _hotel('Chilapata Green Resort / Similar', 'Buxa / Rajabhatkhawa', '02 Nights', 'Premium', 'Premium Eco Room', 'All Meals (APAI)', 4, 4, description='OPTION 02 – PREMIUM: Chilapata Green Resort / Similar (Buxa, 02 Nights)'),
        ],
        inclusions=[
            _inc_included('Handpicked premium forest resorts and luxury eco-lodges.', 1),
            _inc_included('All jungle gourmet meals (Breakfast, Lunch, Dinner).', 2),
            _inc_included('All private luxury ground transfers via dedicated SUV.', 3),
            _inc_included('Pre-arranged Jaldapara and Buxa jungle safari passes.', 4),
            _inc_included('Services of experienced naturalists and destination managers.', 5),
            _inc_included('TRAGUIN round-the-clock backend guest assistance.', 6),
            _inc_excluded('Airfare / Train tickets to destination gateway.', 7),
            _inc_excluded('Camera or video recording fees inside national parks.', 8),
            _inc_excluded('Alcoholic beverages and personal laundry expenses.', 9),
            _inc_excluded('Tips for drivers, forest guards, and hotel bellboys.', 10),
        ],
    )
    return package, itinerary

def build_wb_020(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-020'
    tour_code = 'TRAGUIN-WB-020'
    title = 'Kolkata Luxury Executive MICE Meet'
    duration = '02 Nights / 03 Days'
    slug = 'wb-020-kolkata-luxury-executive-mice-meet'
    itin_slug = 'wb-020-kolkata-luxury-executive-mice-meet-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code WB-020 | TRAGUIN tour code TRAGUIN-WB-020', 1),
            _ph('State / Country: West Bengal, India | Category: Corporate MICE & Elite Meet', 2),
            _ph('Destinations: Kolkata (City of Joy Corporate Hub) • Hooghly Luxury Cruise', 3),
            _ph('Ideal for: Corporate Executives, Board Members & MICE', 4),
            _ph('Best season: Year-Round (Best Oct to Mar)', 5),
            _ph('Starting price: Corporate Rates on Request', 6),
            _ph('TRAGUIN MICE Setup: Conference hall, corporate Wi-Fi, executive dining, luxury group coach, Hooghly cruise, multi-lingual coordinators', 7),
            _ph('TRAGUIN Signature Corporate Touch: Seamless custom branding, dedicated check-in desks, and premium welcome packages.', 8),
            _ph('Important Notes: Conference dates require 4-6 weeks confirmation. Share AV requirements 10 days before event.', 9),
        ],
        moods=['Corporate', 'MICE', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='Corporate Rates on Request',
        rating=Decimal("4.9"), review_count=0,
        tagline='Kolkata Luxury Executive MICE Meet • 02 Nights / 03 Days',
        overview='Accelerate your corporate growth and inspire your core leadership with this ultra-exclusive Luxury Kolkata Holiday tailored for selective enterprise meets. Masterfully crafted by TRAGUIN, this high-end MICE itinerary delivers top-tier corporate presentation environments alongside rich, relaxed team networking. Experience high-end business infrastructure paired with the historical charm of the City of Joy.\n\nCORPORATE OVERVIEW\nEvery logistics detail—from private luxury airport transfers to premium audio-visual conference layouts—is meticulously managed with dedicated 24/7 TRAGUIN support. TRAGUIN MICE Setup Inclusions: Full-day premium conference hall access, high-speed corporate Wi-Fi, tailored executive gourmet dining, dedicated luxury group coach, private networking cruise on the Hooghly River, and local multi-lingual coordinators.',
        seo_title='WB-020 | Kolkata Luxury Executive MICE Meet | TRAGUIN',
        seo_description='Premium 02 Nights / 03 Days West Bengal corporate package (WB-020 / TRAGUIN-WB-020): Executive summit, Hooghly chartered cruise, Victoria Memorial, and 4-tier 5-star business hotels.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('VIP airport welcome and private chartered Hooghly networking cruise beneath Howrah Bridge', 1),
            _ih('Annual strategy summit in grand ballroom with Victoria Memorial sightseeing', 2),
            _ih('Themed corporate gala dinner with authentic Bengali gourmet and global cuisines', 3),
            _ih('Park Street heritage drive, Quest Mall boutique shopping, and Eden Gardens drive-past', 4),
            _ih('4-tier elite 5-star Kolkata business hotels (02 Nights)', 5),
        ],
        days=[
            _day(1, 'ARRIVAL & ELITE RECEPTION — HOOGHLY CHARTERED NETWORKING CRUISE', ('Your executives arrive at Kolkata International Airport, greeted by private TRAGUIN corporate hosts. Board our premium luxury coaches for a comfortable transfer to your 5-star luxury hotel. Following a priority express check-in, host an ice-breaking corporate presentation or mid-afternoon briefing in the reserved boardroom. As dusk falls, head to the jetty to board a private, fully chartered luxury river cruise on the historical Hooghly River. Network seamlessly beneath the illuminated masterpiece of the Howrah Bridge while enjoying fine drinks, premium live music, and exquisite global appetizers.'), [
                'Event: VIP Welcome, Private Hooghly Chartered Cruise.',
                'Meals: Welcome High-Tea & Elite Gala Dinner.',
                'Networking Point: Under the spectacular illuminated Howrah Bridge.',
                'Stay: Kolkata Elite 5-Star Hotel.',
            ]),
            _day(2, 'EXECUTIVES SUMMIT & GLOBAL GALA — STRATEGIC BOARD MEET', ('Savor an early morning breakfast before commencing your corporate summit inside the grand ballroom. Enjoy impeccable 5-star catering during mid-session high-tea breaks and a lavish executive networking lunch buffet. After wrapping up your strategic sessions by mid-afternoon, embark on an immersive, curated tour of the Top Tourist Places in Kolkata. Tour the stunning Victoria Memorial and the iconic structures of colonial Dalhousie Square. End this highly successful day with a grand themed corporate gala dinner featuring authentic, premium Bengali gourmet delicacies and global cuisines.'), [
                'Event: Annual Strategy Summit, Victoria Memorial Sightseeing.',
                'Meals: Breakfast, Business Lunch & Premium Gala Dinner.',
                'Premium Add-on: Tailored audio-visual technical setups & corporate branding accents.',
                'Stay: Kolkata Elite 5-Star Hotel.',
            ]),
            _day(3, 'HERITAGE INSPIRED NETWORKING & DEPARTURE', ('The final morning is structured for seamless team bonding and local cultural discovery. Take an easy, premium drive past the sprawling Eden Gardens stadium and visit the historic Mother House for a truly peaceful, reflective morning. Afterward, enjoy exclusive entry to high-end boutique stores at Quest Mall or Park Street to pick up premium local souvenirs. Following an early executive lunch, your private premium coach arranged by TRAGUIN will provide effortless airport drops, bringing a successful, highly productive executive corporate event to a magnificent close.'), [
                'Sightseeing: Park Street Heritage Drive, High-End Boutique Shopping.',
                'Meals: Breakfast & Premium Farewell Lunch.',
                'Transfers: Airport drops managed via private premium group coaches.',
            ]),
        ],
        hotels=[
            _hotel('Hyatt Regency Kolkata / Novotel Business Tower', 'Kolkata', '02 Nights', 'Deluxe', 'Luxury King Room', 'All Inclusive Corporate Plan', 5, 1, description='DELUXE: Hyatt Regency Kolkata / Novotel Business Tower (Kolkata, 02 Nights)'),
            _hotel('JW Marriott Hotel Kolkata', 'Kolkata', '02 Nights', 'Premium', 'Executive Club Room', 'All Inclusive Corporate Plan', 5, 2, description='PREMIUM: JW Marriott Hotel Kolkata (Kolkata, 02 Nights)'),
            _hotel('The Oberoi Grand, Kolkata', 'Kolkata', '02 Nights', 'Luxury', 'Premier Heritage Balcony Room', 'Elite Handpicked Gourmet Plan', 5, 3, description='LUXURY: The Oberoi Grand, Kolkata (Kolkata, 02 Nights)'),
            _hotel('The Taj Bengal Kolkata (Presidential Access)', 'Kolkata', '02 Nights', 'Ultra Luxury', 'Luxury Premium Suite Tier', 'Bespoke Customized Menu Plan', 5, 4, description='ULTRA LUXURY: The Taj Bengal Kolkata (Kolkata, 02 Nights)'),
        ],
        inclusions=[
            _inc_included('02 Nights elite 5-star accommodation in prime business hubs.', 1),
            _inc_included('Full-day conference space with premium audio-visual equipment.', 2),
            _inc_included('All premium meals, gala dinners, and continuous high-tea breaks.', 3),
            _inc_included('Private chartered luxury boat cruise on the Hooghly River.', 4),
            _inc_included('Luxury AC group coaches for smooth transfers & local tours.', 5),
            _inc_included('Dedicated TRAGUIN on-site corporate desk coordination.', 6),
            _inc_excluded('Domestic or International flight tickets to Kolkata.', 7),
            _inc_excluded('Personal hotel charges such as mini-bar, laundry, and spa.', 8),
            _inc_excluded('Extra alcoholic beverage packages not predefined for gala.', 9),
            _inc_excluded('Individual billing extensions or early/late check-out penalties.', 10),
        ],
    )
    return package, itinerary

WEST_BENGAL_DOMESTIC_BUILDERS = [
    build_wb_006,
    build_wb_007,
    build_wb_008,
    build_wb_009,
    build_wb_010,
    build_wb_011,
    build_wb_012,
    build_wb_013,
    build_wb_014,
    build_wb_015,
    build_wb_016,
    build_wb_017,
    build_wb_018,
    build_wb_019,
    build_wb_020,
]
