"""Builder functions for AS-004 through AS-013 Assam domestic packages."""

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

ASSAM_SLUG = "assam"


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


def build_as_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AS-004'
    tour_code = 'TG-ASSAM-SHILLONG-AS004'
    title = 'TRAGUIN Premium Assam & Meghalaya Tour Package — Family Luxury Combo: Guwahati • Shillong • Cherrapunjee'
    duration = '05 Nights / 06 Days'
    slug = 'as-004-assam-meghalaya-family-luxury-guwahati-shillong-cherrapunjee'
    itin_slug = 'as-004-assam-meghalaya-family-luxury-guwahati-shillong-cherrapunjee-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Assam & Meghalaya, India | Category: Premium Family Luxury Combo', 2),
            _ph('Destinations Covered: Guwahati • Shillong • Cherrapunjee', 3),
            _ph('Ideal for: Luxury Family Tour & Nature Enthusiasts', 4),
            _ph('Best season: October to May', 5),
            _ph('Starting price: On Request (Premium Quotation)', 6),
            _ph('Vehicle: Private Premium Luxury AC SUV (Toyota Innova Crysta) | Meal Plan: MAPAI — Premium Buffet Breakfasts & Gourmet Dinners', 7),
            _ph('Route Plan: Guwahati Arrival ➔ Shillong (3N) ➔ Cherrapunjee Day Excursion ➔ Guwahati (2N) ➔ Departure', 8),
            _ph('TRAGUIN Signature Experience: Private family cruise along the Brahmaputra River with live folk musical performances.', 9),
            _ph('Curated by TRAGUIN Experts: Handpicked boutique accommodations verified directly for family safety and high-end comfort.', 10),
            _ph('Personalized Assistance: Dedicated on-ground coordinators to manage ticketing and scheduling fluidly.', 11),
            _ph('Shopping & Local Gastronomy: Police Bazar Shillong, Fancy Bazar Guwahati — Muga Silk, bamboo furniture, Khasi spices, Assamese Thali.', 12),
            _ph('Important Notes: Shillong/Cherrapunjee sudden temperature drops; boating subject to weather; book Ri Kynjai 45-60 days ahead.', 13),
        ],
        moods=['Family', 'Luxury', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Quotation)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Assam & Meghalaya Family Luxury • Guwahati • Shillong • Cherrapunjee • 05 Nights / 06 Days',
        overview=(
            'Experience an extraordinary luxury journey through Northeast India with the signature TRAGUIN Assam & Meghalaya Packages. Meticulously mapped for families seeking high-end convenience alongside raw wilderness, this travel itinerary seamlessly combines the cultural heritage of a Guwahati Family Tour with the majestic, mist-veiled cloudscapes of a Luxury Meghalaya Holiday.\n\n'
            'TOUR OVERVIEW\nWelcome to a personalized luxury holiday expertly designed by TRAGUIN. Crafted to serve multi-generational travelers, this premium Guwahati Shillong Combo combines elite private logistics, handpicked hotels, and unique regional discoveries. Proposed Route: Guwahati Arrival ➔ Panoramic Drive to Shillong (3 Nights) ➔ Day Exploration to Cherrapunjee ➔ Return to Guwahati Valley (2 Nights) ➔ Departure Hub. Vehicle Class: Private Premium Luxury Air-Conditioned SUV (Toyota Innova Crysta). Meal Plan: Modified American Plan (MAPAI).\n\n'
            'DESTINATION CONTENT & SEO HIGHLIGHTS\nA Guwahati Shillong Family Tour opens the doors to an emerald paradise. Iconic Attractions: Kamakhya Temple, Umananda river island, Nohkalikai Falls, living root structures, Umngot River Dawki, Umiam Lake. Best Time to Visit Assam & Meghalaya: Post-monsoon autumn months introduce crystalline skies and active waterfalls.'
        ),
        seo_title='AS-004 | Assam Meghalaya Family Luxury Guwahati Shillong | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Assam & Meghalaya family package (AS-004 / TG-ASSAM-SHILLONG-AS004): Guwahati, Shillong, Cherrapunjee, Brahmaputra cruise, Kamakhya VIP, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Guwahati arrival and scenic ascent to Shillong via Umiam Lake on Day 01', 1),
            _ih('Shillong Peak, Elephant Falls, Don Bosco Museum, and Ward\'s Lake on Day 02', 2),
            _ih('Cherrapunjee excursion: Nohkalikai Falls, Mawsmai Cave, Seven Sisters Falls, Eco Park', 3),
            _ih('Return to Guwahati with private Brahmaputra sunset cruise on Day 04', 4),
            _ih('VIP Kamakhya Temple, Umananda Island, Srimanta Sankardev Kalakshetra on Day 05', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN GUWAHATI | SCENIC ASCENT TO THE HILL CAPITAL SHILLONG', ('Your family vacation unfolds as you touch down at Lokpriya Gopinath Bordoloi International Airport in Guwahati. A designated TRAGUIN concierge will welcome you warmly at the arrival lounge, presenting traditional silk stoles and chilled refreshments. Step into your premium air-conditioned SUV and begin the smooth, winding drive up toward Shillong. En route, stop by the majestic Umiam Lake, a vast expanse of calm blue water surrounded by hills of pine trees. Take a quiet break at a panoramic view point for specialty teas and family photos. Later, arrive at your premium handpicked hotel in Shillong to settle in for a relaxing evening.'), [
                'Sightseeing Included: Umiam Lake Panoramic Viewpoint, Pine Valley Drive.',
                'Optional Activities: Speedboat ride at Umiam Lake (weather permitting).',
                'Overnight Stay: Handpicked Luxury Resort in Shillong.',
                'Meals Included: Welcome Buffet Dinner.',
            ]),
            _day(2, 'SHILLONG SIGHTSEEING | HIGHLAND LAKES, ARCHITECTURE & WATERFALLS', ('Wake up to a crisp mountain breeze and a fresh, lavish breakfast spread. Start your day with a drive to Shillong Peak, the highest point in the state, which provides sweeping views of the entire valley below. Next, visit the distinct Elephant Falls, where mountain streams cascade over three tiers of dark rock formations. During the afternoon, explore the renowned Don Bosco Museum to discover the vibrant tribal heritage of Northeast India. Conclude your day with a family walk through the manicured pathways of Ward\'s Lake, a tranquil oasis in the heart of the town.'), [
                'Sightseeing Included: Shillong Peak, Elephant Falls, Don Bosco Museum, Ward\'s Lake.',
                'Evening Experience: Café hopping and exploring local live music spots.',
                'Overnight Stay: Handpicked Luxury Resort in Shillong.',
                'Meals Included: Breakfast & Premium Dinner.',
            ]),
            _day(3, 'EXCURSION TO CHERRAPUNJEE | LAND OF MEGALITHS & THUNDERING PLUNGE FALLS', ('Embark on a day excursion to Cherrapunjee (Sohra), traveling along a scenic highway flanked by deep canyons and mist-shrouded valleys. Witness the remarkable Nohkalikai Falls, India\'s tallest single-tier plunge waterfall, and capture the deep emerald pool formed at its base. Explore the unique limestone paths inside the well-lit Mawsmai Caves, mapping out a subterranean adventure suitable for all ages. Stand at the edge of Eco Park for views extending out to the floodplains of Bangladesh, before returning to Shillong for the night.'), [
                'Sightseeing Included: Nohkalikai Falls, Mawsmai Cave, Seven Sisters Falls, Eco Park.',
                'Photography Points: Duwan Sing Syiem bridge gorge viewpoint.',
                'Overnight Stay: Handpicked Luxury Resort in Shillong.',
                'Meals Included: Breakfast & Gourmet Dinner.',
            ]),
            _day(4, 'SHILLONG TO GUWAHATI | PRIVATE SUNSET RETREAT ON THE BRAHMAPUTRA', ('Savor breakfast overlooking the pine forests before beginning your comfortable return drive to the plains of Assam. Upon arrival in Guwahati, check into your high-end urban resort and take some time to unwind. In the late afternoon, enjoy an exclusive experience managed by TRAGUIN: a private sunset cruise along the Brahmaputra River. Relax on the deck as the sun dips below the horizon, while listening to traditional folk instruments and sampling local Assamese delicacies.'), [
                'Sightseeing Included: Downhill mountain highway drive, Brahmaputra River Cruise.',
                'Evening Experience: Dinner and live cultural performances onboard.',
                'Overnight Stay: Premium Luxury Hotel in Guwahati.',
                'Meals Included: Breakfast & Cruise Dinner.',
            ]),
            _day(5, 'GUWAHATI CITADEL | SPIRITUAL BLISS & EXQUISITE GOLDEN SILK', ('Begin your morning with a premium spiritual experience. TRAGUIN experts will guide your family through a fast-tracked, hassle-free VIP visit to the revered Kamakhya Temple atop Nilachal Hills. Take in the rich heritage and architectural layout of this ancient destination. Later, step aboard a speed ferry to visit the Umananda Temple, located on the smallest inhabited river island in the world. Spend your afternoon visiting regional craft markets to learn about Assam\'s prized Muga and Assam Orthodox tea varieties.'), [
                'Sightseeing Included: Kamakhya Temple (VIP Access), Umananda Island, Srimanta Sankardev Kalakshetra.',
                'Local Experience: High tea featuring curated local Assam orthodox leaf blends.',
                'Overnight Stay: Premium Luxury Hotel in Guwahati.',
                'Meals Included: Breakfast & Grand Farewell Dinner.',
            ]),
            _day(6, 'DEPARTURE FROM GUWAHATI | CHERISHED FAMILY MEMORIES', ('Enjoy your final breakfast at the hotel restaurant. Take a few moments for any last-minute souvenir shopping or to pack your regional keepsakes. At the scheduled hour, your private chauffeur will drive you comfortably to Guwahati International Airport for your flight home, concluding an exceptional holiday managed end-to-end by TRAGUIN.'), [
                'Sightseeing Included: Airport Transit Route.',
                'Meals Included: International Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Hotel Polo Towers / Landmark Hills | Kiranshree Grand / Grand Majesty', 'Shillong (3 Nights) / Guwahati (2 Nights)', '05 Nights', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner (MAP)', 4, 1, description='OPTION 01 – DELUXE: Hotel Polo Towers / Landmark Hills (Shillong, 3 Nights) | Kiranshree Grand / Grand Majesty (Guwahati, 2 Nights) | Breakfast & Dinner (MAP)'),
            _hotel('Moolchand Resorts / Pinewood Hotel | Novotel Guwahati GS Road', 'Shillong (3 Nights) / Guwahati (2 Nights)', '05 Nights', 'Premium', 'Premium Room', 'Breakfast & Dinner (MAP)', 4, 2, description='OPTION 02 – PREMIUM: Moolchand Resorts / Pinewood Hotel (Shillong, 3 Nights) | Novotel Guwahati GS Road (Guwahati, 2 Nights) | Breakfast & Dinner (MAP)'),
            _hotel('Ri Kynjai - Serenity By The Lake | Radisson Blu Hotel Guwahati', 'Shillong (3 Nights) / Guwahati (2 Nights)', '05 Nights', 'Luxury', 'Luxury Room', 'Gourmet MAP Plan', 5, 3, description='OPTION 03 – LUXURY: Ri Kynjai - Serenity By The Lake (Shillong, 3 Nights) | Radisson Blu Hotel Guwahati (Guwahati, 2 Nights) | Gourmet MAP Plan'),
            _hotel('Ri Kynjai (Luxury Cottages) | Vivanta Guwahati (Taj Group)', 'Shillong (3 Nights) / Guwahati (2 Nights)', '05 Nights', 'Ultra Luxury', 'Luxury Cottage / Suite', 'Bespoke Dining Plan', 5, 4, description='OPTION 04 – ULTRA LUXURY: Ri Kynjai Luxury Cottages (Shillong, 3 Nights) | Vivanta Guwahati Taj Group (Guwahati, 2 Nights) | Bespoke Dining Plan'),
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Curated twin/triple sharing options across verified luxury hotels.', 1),
            _inc_included('Luxury Fleet Transport: Entire itinerary managed via a private, air-conditioned Toyota Innova Crysta.', 2),
            _inc_included('Meal Package: 5 premium breakfasts and 5 chef-curated specialty dinners.', 3),
            _inc_included('Welcome Amenities: Personalized welcome setup including local silk stoles and signature refreshments.', 4),
            _inc_included('Complimentary Experiences: Private sunset cruise along the Brahmaputra River and fast-tracked VIP temple access.', 5),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest support and localized coordination throughout your stay.', 6),
            _inc_excluded('Flights / Rail: Airfare or train tickets to and from Guwahati Hub.', 7),
            _inc_excluded('Entry Tickets: Camera permits or personal local guide allocations at monuments.', 8),
            _inc_excluded('Personal Expenses: Laundry service, room service orders, or specialty beverages.', 9),
            _inc_excluded('Activities: Water sports at Umiam Lake or zip-lining excursions in Cherrapunjee.', 10),
            _inc_excluded('Insurance: Travel or health insurance coverage.', 11),
        ],
    )
    return package, itinerary

def build_as_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AS-005'
    tour_code = 'TG-KAZI-WILD-005'
    title = 'TRAGUIN Premium Kaziranga Wildlife Tour Package — Luxury Safari: Guwahati • Kaziranga National Park'
    duration = '04 Nights / 05 Days'
    slug = 'as-005-kaziranga-wildlife-safari-guwahati-kaziranga'
    itin_slug = 'as-005-kaziranga-wildlife-safari-guwahati-kaziranga-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code AS-005 | TRAGUIN tour code TG-KAZI-WILD-005', 1),
            _ph('State / Country: Assam, India | Category: Premium Wildlife Luxury Safari', 2),
            _ph('Destinations Covered: Guwahati • Kaziranga National Park', 3),
            _ph('Ideal for: Wildlife Enthusiasts, Premium Families, Luxury Connoisseurs', 4),
            _ph('Best season: November to April (Dry winter park openings)', 5),
            _ph('Starting price: INR 56,000/- Per Guest (On Request)', 6),
            _ph('Vehicle: Private Premium Luxury AC SUV (Toyota Innova Crysta) + open-top 4x4 Gypsy for safaris | Meal Plan: Jungle APAI in Kaziranga', 7),
            _ph('Route Plan: Guwahati Arrival ➔ Kaziranga National Park (3N) ➔ Immersive Wilderness Safaris ➔ Guwahati (1N) ➔ Departure', 8),
            _ph('TRAGUIN Signature Experience: Private dining options directly overlooking the beautiful Diphlu River on demand.', 9),
            _ph('Curated by TRAGUIN Experts: All open-top safari vehicles driven by vetted, destination-trained drivers.', 10),
            _ph('Personalized Assistance: Smooth coordination ensuring zero waiting times for park passes.', 11),
            _ph('Shopping & Local Experiences: Organic Assam Orthodox teas, hand-carved rhino figurines, Hathaway Tea Estates.', 12),
            _ph('Important Notes: Park open November–April; wear muted safari colors; book Diphlu River Lodge 60 days ahead.', 13),
        ],
        moods=['Family', 'Luxury', 'Nature', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='INR 56,000/- Per Guest (On Request)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Kaziranga Wildlife Safari • Guwahati • Kaziranga • 04 Nights / 05 Days',
        overview=(
            'Venture into the heart of wild Assam with a signature itinerary intricately conceptualized for true nature lovers. This customized journey blends emotional storytelling, thrilling deep-forest exploration, and stays at the finest eco-luxury lodges.\n\nTOUR OVERVIEW\\nWelcome to an elite wilderness escape meticulously planned by TRAGUIN. Route Plan: Guwahati Arrival ➔ Lush Scenic Drive to Kaziranga National Park (3 Nights) ➔ Immersive Wilderness Safaris ➔ Return to Guwahati (1 Night) ➔ Departure. Vehicle Class: Private Premium Luxury Air-Conditioned SUV paired with open-top specialized 4x4 Gypsy vehicles.\n\nWHY VISIT KAZIRANGA?\\nKaziranga National Park is a jewel in the crown of global biodiversity. Famous as the last stronghold of the Great Indian One-Horned Rhinoceros, sheltering the Big Five: Rhino, Royal Bengal Tiger, Asian Elephant, Wild Water Buffalo, and Swamp Deer.'
        ),
        seo_title='AS-005 | Kaziranga Wildlife Safari Guwahati | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Kaziranga wildlife package (AS-005 / TG-KAZI-WILD-005): elephant and jeep safaris, Orchid Park, Kamakhya VIP, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Scenic transit through tea fields from Guwahati to Kaziranga on Day 01', 1),
            _ih('Dawn elephant safari and afternoon 4x4 jeep safari in Central Range on Day 02', 2),
            _ih('Western Range jeep safari and Kaziranga Orchid & Cultural Park on Day 03', 3),
            _ih('Eastern Range birding paradise and return to Guwahati on Day 04', 4),
            _ih('Spiritual farewell at Kamakhya Temple VIP entry on Day 05', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN GUWAHATI | SCENIC TRANSIT THROUGH TEA FIELDS TO KAZIRANGA', ('Your ultimate wildlife holiday begins at Guwahati International Airport or Railway Station, where a designated TRAGUIN travel coordinator welcomes you warmly. Board your private luxury SUV and leave the city behind for a smooth journey to the historic plains of Kaziranga. The drive transitions beautifully from urban highways to sweeping rural vistas lined with emerald-green paddy fields and manicured tea plantations. Arrive at your luxury wilderness resort by afternoon, where a cooling signature indigenous fruit mocktail awaits you.'), [
                'Sightseeing Included: Scenic countryside drive, Tea Garden vistas.',
                'Evening Experience: Nature walk inside the resort followed by a traditional orientation briefing.',
                'Overnight Stay: Handpicked Luxury Resort in Kaziranga.',
                'Meals Included: Gourmet Welcome Dinner.',
            ]),
            _day(2, 'DAWN ELEPHANT SAFARI & AFTERNOON 4X4 JEEP SAFARI INTO THE CENTRAL RANGE', ('Wake up to the sounds of nature. Before dawn, step into the Central (Kohora) Range for a majestic morning Elephant Safari. As the golden fog rises from the wetlands, ride safely into the tall elephant grass to view the prehistoric One-Horned Rhinoceros grazing just feet away. Return to the lodge for a hearty multi-cuisine breakfast. In the afternoon, board your private open-top 4x4 vehicle for a thrilling Jeep Safari across the Central Range accompanied by a veteran naturalist.'), [
                'Sightseeing Included: Kohora Range Elephant Safari, Central Range Exclusive Jeep Safari.',
                'Photography Points: Wetlands of Mihimukh for spectacular wildlife shots against the horizon.',
                'Overnight Stay: Handpicked Luxury Resort in Kaziranga.',
                'Meals Included: Breakfast, Lunch, and Specialty Jungle Dinner.',
            ]),
            _day(3, 'DEEP JUNGLE JEEP SAFARI IN WESTERN RANGE & ETHNIC ORCHID PARK CULTURAL TOUR', ('Enjoy an early breakfast before heading out to explore the Western (Bagori) Range, famous for its high density of large mammals and massive families of Asian Elephants. In the afternoon, discover the rich heritage of Assam at the Kaziranga National Orchid and Cultural Park with live Bihu and Jhumur performances.'), [
                'Sightseeing Included: Bagori Range Jeep Safari, National Orchid & Cultural Park.',
                'Evening Experience: Live traditional Bihu dance show performed by local artists.',
                'Overnight Stay: Handpicked Luxury Resort in Kaziranga.',
                'Meals Included: Breakfast, Lunch, and Traditional Assamese Dinner.',
            ]),
            _day(4, 'EASTERN RANGE BIRDING PARADISE & SCENIC TRANSIT BACK TO GUWAHATI', ('Your final safari takes you into the Eastern (Agaratoli) Range, a serene paradise renowned among international birding enthusiasts. Bid farewell to Kaziranga as your premium SUV brings you smoothly back to Guwahati for a relaxing final evening.'), [
                'Sightseeing Included: Agaratoli Range Exploration, Intercity Scenic Drive back.',
                'Optional Activities: High-end dinner at a signature heritage restaurant in Guwahati.',
                'Overnight Stay: Luxury Hotel in Guwahati.',
                'Meals Included: Breakfast & Farewell Dinner.',
            ]),
            _day(5, 'SPIRITUAL FAREWELL AT KAMAKHYA TEMPLE & DEPARTURE', ('Conclude your premium vacation with VIP fast-track entry at the highly revered Kamakhya Temple atop Nilachal Hills. After collecting souvenirs, your professional driver will transfer you to the airport or railway station.'), [
                'Sightseeing Included: Kamakhya Temple (VIP Entry), Craft Emporium.',
                'Meals Included: Lavish Breakfast.',
            ])
        ],
        hotels=[
            _hotel('Infinity Oakwood Resort / Kaziranga Resort | Kiranshree Grand / Grand Majesty', 'Kaziranga (3 Nights) / Guwahati (1 Night)', '04 Nights', 'Deluxe', 'Deluxe Room', 'Kaziranga (AP) | Guwahati (CP)', 4, 1, description='OPTION 01 – DELUXE: Infinity Oakwood Resort / Kaziranga Resort (Kaziranga, 3 Nights) | Kiranshree Grand / Grand Majesty (Guwahati, 1 Night) | Kaziranga (AP) | Guwahati (CP)'),
            _hotel('Borgos Resort (Executive Room) | Novotel Guwahati GS Road', 'Kaziranga (3 Nights) / Guwahati (1 Night)', '04 Nights', 'Premium', 'Executive Room', 'Kaziranga (AP) | Guwahati (MAP)', 4, 2, description='OPTION 02 – PREMIUM: Borgos Resort Executive Room (Kaziranga, 3 Nights) | Novotel Guwahati GS Road (Guwahati, 1 Night) | Kaziranga (AP) | Guwahati (MAP)'),
            _hotel('IORA - The Retreat (Luxury Suite) | Radisson Blu Hotel Guwahati', 'Kaziranga (3 Nights) / Guwahati (1 Night)', '04 Nights', 'Luxury', 'Luxury Suite', 'All Gourmet Meals Plan', 5, 3, description='OPTION 03 – LUXURY: IORA - The Retreat Luxury Suite (Kaziranga, 3 Nights) | Radisson Blu Hotel Guwahati (Guwahati, 1 Night) | All Gourmet Meals Plan'),
            _hotel('Diphlu River Lodge (Luxury Eco Cottages) | Vivanta Guwahati (Taj Group)', 'Kaziranga (3 Nights) / Guwahati (1 Night)', '04 Nights', 'Ultra Luxury', 'Luxury Eco Cottage', 'Ultra Premium Dining Plan', 5, 4, description='OPTION 04 – ULTRA LUXURY: Diphlu River Lodge Luxury Eco Cottages (Kaziranga, 3 Nights) | Vivanta Guwahati Taj Group (Guwahati, 1 Night) | Ultra Premium Dining Plan')
        ],
        inclusions=[
            _inc_included('Luxury Stays: Selected sharing rooms across premium handpicked hotels and high-end jungle eco-resorts.', 1),
            _inc_included('Private Premium Logistics: Intercity transport via an air-conditioned Toyota Innova Crysta, including toll taxes and driver allowances.', 2),
            _inc_included('Jungle Safaris: 01 Exclusive Morning Elephant Safari and 02 Private 4x4 Deep Forest Jeep Safaris.', 3),
            _inc_included('Meal Framework: All meals (Breakfast, Lunch, Dinner) included while in Kaziranga, and breakfast in Guwahati.', 4),
            _inc_included('TRAGUIN Support: Fast-tracked VIP temple entry permits and 24/7 dedicated local coordinator backup.', 5),
            _inc_included('Welcome Amenities: Traditional Assamese welcome scarves and complimentary daily mineral water.', 6),
            _inc_excluded('Flights/Rail: Major domestic or international travel tickets to and from Guwahati.', 7),
            _inc_excluded('Camera Charges: Special high-end camera lens fees required inside the forest limits.', 8),
            _inc_excluded('Personal Extras: Laundry services, tips, premium room drinks, or alcoholic beverages.', 9),
            _inc_excluded('Insurance: Travel or health insurance policies.', 10)
        ],
    )
    return package, itinerary


def build_as_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AS-006'
    tour_code = 'TG-AS-HM-006'
    title = 'TRAGUIN Premium Assam Honeymoon Package — Romantic Wilderness: Guwahati • Kaziranga National Park'
    duration = '04 Nights / 05 Days'
    slug = 'as-006-assam-honeymoon-kaziranga-guwahati'
    itin_slug = 'as-006-assam-honeymoon-kaziranga-guwahati-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code AS-006 | TRAGUIN tour code TG-AS-HM-006', 1),
            _ph('State / Country: Assam, India | Category: Honeymoon & Romantic Escapes', 2),
            _ph('Destinations Covered: Guwahati • Kaziranga National Park', 3),
            _ph('Ideal for: Newlyweds, Couples Seeking Serenity', 4),
            _ph('Best season: November to April', 5),
            _ph('Starting price: INR 39,500/- Per Person', 6),
            _ph('Vehicle: Premium Luxury AC Sedan / Executive Cruiser | Meal Plan: Royal CP/MAP with private dinners', 7),
            _ph('Route Plan: Guwahati ➔ Romantic Cruise ➔ Kaziranga (3N) ➔ Guwahati (1N) ➔ Departure', 8),
            _ph('TRAGUIN Signature Experience: Private twilight boat excursions and candlelight dinners in isolated nature locations.', 9),
            _ph('Curated by TRAGUIN Experts: Every resort selected for privacy and exceptional hospitality.', 10),
            _ph('Personalized Assistance: Dedicated 24/7 coordinator for dinner reservations and safari adjustments.', 11),
            _ph('Shopping: Muga and Eri silks, single-estate orthodox teas, Diphlu River couple photography spots.', 12),
            _ph('Important Notes: Safari subject to weather; book lodges 45-60 days ahead; respectful dress at Kamakhya.', 13),
        ],
        moods=['Romantic', 'Luxury', 'Nature', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='INR 39,500/- Per Person',
        rating=Decimal("4.9"), review_count=0,
        tagline='Assam Honeymoon • Guwahati • Kaziranga • 04 Nights / 05 Days',
        overview=(
            'Surrender to misty morning horizons, gold-tinted tea estates, and the gentle whisper of the Brahmaputra in this signature romantic escape.\n\nTOUR OVERVIEW\\nCouples-only retreat curated by TRAGUIN: Guwahati ➔ Romantic Cruise ➔ Kaziranga (3 Nights) ➔ Guwahati (1 Night) ➔ Departure with sparkling wine welcome.\n\nTHE ALLURE OF ASSAM\\nKaziranga UNESCO backdrop, Kamakhya spiritual bond, tea estate couple photos, and private candlelight dinners in colonial bungalows.'
        ),
        seo_title='AS-006 | Assam Honeymoon Kaziranga Guwahati | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Assam honeymoon (AS-006 / TG-AS-HM-006): Brahmaputra cruise, Kaziranga safaris, Kamakhya VIP, 4-tier luxury lodges.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Brahmaputra sunset cruise on romantic arrival Day 01', 1),
            _ih('Scenic drive to Kaziranga with tea garden trails Day 02', 2),
            _ih('Dawn and afternoon safaris plus Orchid Conservatory Day 03', 3),
            _ih('Kamakhya VIP and Umananda Island on Day 04', 4),
            _ih('Departure with everlasting romantic memories Day 05', 5),
        ],
        days=[
            _day(1, 'GUWAHATI ARRIVAL | ROMANTIC CRUISE ON THE MIGHTY BRAHMAPUTRA', ('Premium red-carpet welcome at Guwahati airport. Late afternoon exclusive sunset cruise with fine wine and live traditional music as the sun paints the sky gold and magenta.'), [
                'Sightseeing Included: Brahmaputra Sunset Cruise, Riverside Promenade.',
                'Evening Experience: Candlelit dinner reservation over the water.',
                'Overnight Stay: Luxury Hotel in Guwahati.',
                'Meals Included: Welcome Drinks & Gourmet Dinner.',
            ]),
            _day(2, 'GUWAHATI TO KAZIRANGA | JOURNEY INTO THE WILD EMERALD HEARTLAND', ('Scenic drive through paddy fields and tea gardens to premium wilderness resort. Afternoon tea plantation walk and evening private bonfire beneath the stars.'), [
                'Sightseeing Included: Scenic Highway Vista, Tea Garden Trails.',
                'Local Experiences: Private tea leaves plucking experience & local estate walk.',
                'Overnight Stay: Premium Wilderness Resort, Kaziranga.',
                'Meals Included: Breakfast & Traditional Assamese Dinner.',
            ]),
            _day(3, 'KAZIRANGA NATIONAL PARK | DAWN SAFARI & INTIMATE ORCHID CONSERVATORY VISIT', ('Early morning Central Range safari spotting One-Horned Rhinoceros. Orchid and Cultural Park visit and Western Range sunset jeep safari.'), [
                'Sightseeing Included: Morning & Afternoon Safaris, Orchid Conservatory.',
                'Photography Points: Kohora Range panoramic sunset deck.',
                'Overnight Stay: Premium Wilderness Resort, Kaziranga.',
                'Meals Included: Full Board (Breakfast, Lunch & Dinner).',
            ]),
            _day(4, 'KAZIRANGA TO GUWAHATI | SACRED BLESSINGS & SIGHTSEEING', ('Return to Guwahati for VIP Kamakhya Temple, Umananda river island boat ride, and silk souvenir browsing with farewell romantic dinner.'), [
                'Sightseeing Included: Kamakhya Temple, Umananda River Island, Fancy Bazar.',
                'Evening Experience: Farewell romantic culinary dinner setup.',
                'Overnight Stay: Luxury Hotel in Guwahati.',
                'Meals Included: Breakfast & Multi-course Dinner.',
            ]),
            _day(5, 'DEPARTURE | EVERLASTING MEMORIES OF ROMANTIC ASSAM', ('Peaceful breakfast in bed and executive airport transfer concluding your TRAGUIN romantic escape.'), [
                'Sightseeing Included: Airport Transit Route.',
                'Optional Activities: Packing premium tea samplers at local boutiques.',
                'Meals Included: Sumptuous Buffet Breakfast.',
            ])
        ],
        hotels=[
            _hotel('Hotel Grand Majesty / Kiranshree | Kaziranga Resort / Infinity Resort', 'Guwahati (1 Night) / Kaziranga (2 Nights) / Guwahati (1 Night)', '04 Nights', 'Deluxe', 'Deluxe Executive Room', 'Breakfast & Dinner (MAP)', 4, 1, description='OPTION 01 – DELUXE: Hotel Grand Majesty / Kiranshree (Guwahati, 1N+1N) | Kaziranga Resort / Infinity Resort (Kaziranga, 2N) | Breakfast & Dinner'),
            _hotel('Novotel Guwahati GS Road | Borgos Resort / Landmark Woods', 'Guwahati (1 Night) / Kaziranga (2 Nights) / Guwahati (1 Night)', '04 Nights', 'Premium', 'Premium Luxury View Room', 'Breakfast & Dinner (MAP)', 4, 2, description='OPTION 02 – PREMIUM: Novotel Guwahati GS Road (Guwahati, 1N+1N) | Borgos Resort / Landmark Woods (Kaziranga, 2N) | Breakfast & Dinner'),
            _hotel('Radisson Blu Hotel Guwahati | Diphlu River Lodge (Luxury Cabins)', 'Guwahati (1 Night) / Kaziranga (2 Nights) / Guwahati (1 Night)', '04 Nights', 'Luxury', 'River-Facing Luxury Suite', 'Breakfast & Dinner (MAP)', 5, 3, description='OPTION 03 – LUXURY: Radisson Blu Hotel Guwahati (Guwahati, 1N+1N) | Diphlu River Lodge Luxury Cabins (Kaziranga, 2N) | Breakfast & Dinner'),
            _hotel('Vivanta Guwahati (Taj Group) | The Iora - The Retreat / Private Villas', 'Guwahati (1 Night) / Kaziranga (2 Nights) / Guwahati (1 Night)', '04 Nights', 'Ultra Luxury', 'Presidential Luxury Villa Pool', 'Breakfast & Dinner (MAP)', 5, 4, description='OPTION 04 – ULTRA LUXURY: Vivanta Guwahati Taj Group (Guwahati, 1N+1N) | The Iora Private Villas (Kaziranga, 2N) | Breakfast & Dinner')
        ],
        inclusions=[
            _inc_included('Premium Accommodations: 04 Nights at elite handpicked hotels and luxury wilderness lodges.', 1),
            _inc_included('Luxury Transfers: Private air-conditioned premium vehicle throughout, including toll fees and driver allowances.', 2),
            _inc_included('Gourmet Meal Plan: Daily elaborate breakfasts and dynamic multi-course dinners.', 3),
            _inc_included('Exclusive Experiences: Private romantic sunset cruise on the Brahmaputra River and fast-track VIP entry at Kamakhya Temple.', 4),
            _inc_included('Jungle Adventures: Authorized open-jeep safari permits and park entry passes for Kaziranga National Park.', 5),
            _inc_included('Welcome Amenities: Complementary honeymoon cake, traditional welcoming stoles, and daily premium mineral water.', 6),
            _inc_included('TRAGUIN Support & Assistance: Continuous on-ground support and specialized local coordinators.', 7),
            _inc_excluded('Air / Rail Fare: Domestic or international flight tickets to and from Guwahati.', 8),
            _inc_excluded('Personal Expenses: Laundry services, direct dial telephone calls, or premium alcoholic beverages.', 9),
            _inc_excluded('Camera & Guide Fees: Professional video camera permits or individual local monument guide fees.', 10),
            _inc_excluded('Optional Tours: Any extra leisure excursions or activities not specified in the day-by-day itinerary.', 11),
            _inc_excluded('Insurance Cover: Medical or comprehensive travel insurance plans.', 12)
        ],
    )
    return package, itinerary


def build_as_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AS-007'
    tour_code = 'TG-AS-KAM-007'
    title = 'TRAGUIN Premium Kamakhya Spiritual Tour Package — Divine Pilgrimage: Guwahati • Nilachal Hills • Hajo'
    duration = '03 Nights / 04 Days'
    slug = 'as-007-kamakhya-spiritual-pilgrimage-guwahati-hajo'
    itin_slug = 'as-007-kamakhya-spiritual-pilgrimage-guwahati-hajo-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code AS-007 | TRAGUIN tour code TG-AS-KAM-007', 1),
            _ph('State / Country: Assam, India | Category: Pilgrimage & Spiritual', 2),
            _ph('Destinations Covered: Guwahati • Nilachal Hills • Hajo', 3),
            _ph('Ideal for: Devotees, Families, Spiritual Seekers', 4),
            _ph('Best season: October to April (Ambubachi period for special darshan)', 5),
            _ph('Starting price: On Request (Premium Tailored Rates)', 6),
            _ph('Vehicle: Private Premium Luxury AC SUV (Toyota Innova Crysta) | Meal Plan: MAPAI — elaborate breakfasts and gourmet dinners', 7),
            _ph('Route Plan: Guwahati ➔ Nilachal Hills Inner Sanctum ➔ Hajo ➔ Brahmaputra Confluence ➔ Departure', 8),
            _ph('TRAGUIN Signature Experience: Skip crowded queues with meticulously mapped morning entry schedules.', 9),
            _ph('Curated by TRAGUIN Experts: Hand-vetted transport partners for safe, reliable city driving.', 10),
            _ph('Exclusive Recommendations: Verified index of spiritual souvenir shops and authentic handloom centers.', 11),
            _ph('Shopping: Fancy Bazar & Pan Bazar bell-metal artifacts, Muga and Pat silk sarees from state emporiums.', 12),
            _ph('Important Notes: Conservative dress at Kamakhya; vehicle restricted past 10 PM; book festivals 30-45 days ahead.', 13),
        ],
        moods=['Cultural', 'Family', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Tailored Rates)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Kamakhya Spiritual Pilgrimage • Guwahati • Hajo • 03 Nights / 04 Days',
        overview=(
            'Embark on a sacred odyssey into the spiritual epicenter of the Northeast with VIP connectivity and luxurious boutique comfort.\n\nTOUR OVERVIEW\\nKamakhya Spiritual Tour by TRAGUIN bridges historical antiquity with premium stays. Route: Guwahati ➔ Nilachal Hills ➔ Hajo ➔ Brahmaputra Confluence ➔ Departure.\n\nTHE ESSENCE OF ASSAM SIGHTSEEING\\nKamakhya Temple Shakti worship, Umananda Peacock Island, Hajo interfaith confluence, and luxury private river decks at sunset.'
        ),
        seo_title='AS-007 | Kamakhya Spiritual Pilgrimage Guwahati | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Kamakhya spiritual package (AS-007 / TG-AS-KAM-007): VIP darshan, Hajo pilgrimage, Umananda cruise, 4-tier Guwahati hotels.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Guwahati arrival with Vashistha Ashram and Brahmaputra Riverfront Day 01', 1),
            _ih('Priority Kamakhya Temple darshan and Sukreswar Temple Arati Day 02', 2),
            _ih('Hajo pilgrimage and private Brahmaputra cruise to Umananda Day 03', 3),
            _ih('Sacred souvenirs and departure Day 04', 4),
        ],
        days=[
            _day(1, 'ARRIVAL IN GUWAHATI | WELCOME TO THE SACRED VALLEY', ('Sacred journey begins at Guwahati airport with traditional Assamese gamosas. Late afternoon visit serene Vashistha Ashram and sunset stroll along the Brahmaputra Riverfront.'), [
                'Sightseeing Included: Vashistha Ashram, Brahmaputra Riverfront.',
                'Evening Experience: Relaxing evening briefing over premium local tea.',
                'Overnight Stay: Handpicked Luxury Hotel in Guwahati.',
                'Meals Included: Welcome Dinner.',
            ]),
            _day(2, 'DIVINE DARSHAN | INNER SANCTUM OF MAA KAMAKHYA TEMPLE', ('Priority entry sequence for Maa Kamakhya Temple inner sanctum with Dasa Mahavidyas shrines. Evening Sukreswar Temple traditional Arati on the river banks.'), [
                'Sightseeing Included: Kamakhya Temple (Main Darshan), Sukreswar Temple Arati.',
                'Optional Activities: Personal consultation with temple pandits for family rituals.',
                'Overnight Stay: Handpicked Luxury Hotel in Guwahati.',
                'Meals Included: Breakfast & Gourmet Dinner.',
            ]),
            _day(3, 'HAJO PILGRIMAGE & PRIVATE SUNSET RIVER CRUISE', ('Visit historic Hajo and Hayagriva Madhava Temple. Private premium charter cruise to Umananda Temple on Peacock Island at golden hour.'), [
                'Sightseeing Included: Hajo Temples, Umananda Island Temple, Private River Cruise.',
                'Photography Points: Mid-river shots of the Guwahati skyline at golden hour.',
                'Overnight Stay: Handpicked Luxury Hotel in Guwahati.',
                'Meals Included: Breakfast & Farewell Gala Dinner.',
            ]),
            _day(4, 'SACRED SOUVENIRS & DEPARTURE', ('Relaxed breakfast and spiritual keepsakes shopping before graceful airport transfer concluding your TRAGUIN spiritual getaway.'), [
                'Sightseeing Included: Local shopping markets route.',
                'Meals Included: Lavish Breakfast.',
            ])
        ],
        hotels=[
            _hotel('Hotel Grand Majesty / Kiranshree Portico', 'Guwahati (3 Nights)', '03 Nights', 'Deluxe', 'Executive Room', 'Breakfast & Dinner (MAP)', 4, 1, description='OPTION 01 – DELUXE: Hotel Grand Majesty / Kiranshree Portico (Guwahati, 3 Nights) | Breakfast & Dinner (MAP)'),
            _hotel('Novotel Guwahati GS Road', 'Guwahati (3 Nights)', '03 Nights', 'Premium', 'Superior Room', 'Breakfast & Dinner (MAP)', 4, 2, description='OPTION 02 – PREMIUM: Novotel Guwahati GS Road (Guwahati, 3 Nights) | Breakfast & Dinner (MAP)'),
            _hotel('Radisson Blu Hotel Guwahati', 'Guwahati (3 Nights)', '03 Nights', 'Luxury', 'Deluxe Lake View', 'Gourmet MAP Plan', 5, 3, description='OPTION 03 – LUXURY: Radisson Blu Hotel Guwahati Deluxe Lake View (Guwahati, 3 Nights) | Gourmet MAP Plan'),
            _hotel('Vivanta Guwahati (Taj Group)', 'Guwahati (3 Nights)', '03 Nights', 'Ultra Luxury', 'Premium Suite', 'Bespoke Dining Privileges', 5, 4, description='OPTION 04 – ULTRA LUXURY: Vivanta Guwahati Taj Group Premium Suite (Guwahati, 3 Nights) | Bespoke Dining Privileges')
        ],
        inclusions=[
            _inc_included('Premium Stays: 3 Nights accommodation at the finest handpicked hotels based on your preferred tier.', 1),
            _inc_included('Luxury Transportation: All transfers and local sightseeing via a private air-conditioned Toyota Innova Crysta.', 2),
            _inc_included('Meals: Daily multi-cuisine buffet breakfasts and premium dinners at your hotel.', 3),
            _inc_included('Assistance: Personalized airport arrival handling and dedicated TRAGUIN support.', 4),
            _inc_included('Taxes: All current fuel costs, toll prices, parking fees, and government service taxes.', 5),
            _inc_included('Welcome Amenities: Assamese traditional welcome scarves, fresh fruit platters, and premium bottled water.', 6),
            _inc_included('Complimentary Experiences: A scenic private boat cruise to the Umananda river island.', 7),
            _inc_excluded('Flights: Main airline or train transport ticketing to and from Guwahati.', 8),
            _inc_excluded('Entry Tickets: Camera fees, special quick darshan ticket costs, and internal temple donation offerings.', 9),
            _inc_excluded('Personal Expenses: Laundry service, telephone usage bills, and individual hotel room minibar consumptions.', 10),
            _inc_excluded('Activities: Any additional unlisted local boat hires or individual tour options.', 11),
            _inc_excluded('Insurance: Travel medical or cancellation insurance policies.', 12)
        ],
    )
    return package, itinerary


def build_as_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AS-008'
    tour_code = 'TG-AS-TEAGARDEN-008'
    title = 'TRAGUIN Premium Assam Tea Gardens Tour Package — Heritage Family: Dibrugarh • Jorhat • Kaziranga • Guwahati'
    duration = '05 Nights / 06 Days'
    slug = 'as-008-tea-gardens-dibrugarh-jorhat-kaziranga-guwahati'
    itin_slug = 'as-008-tea-gardens-dibrugarh-jorhat-kaziranga-guwahati-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code AS-008 | TRAGUIN tour code TG-AS-TEAGARDEN-008', 1),
            _ph('State / Country: Assam, India | Category: Premium Heritage & Tea Garden Family Tour', 2),
            _ph('Destinations Covered: Dibrugarh • Jorhat • Kaziranga • Guwahati', 3),
            _ph('Ideal for: Multi-generational Families & Culture Aficionados', 4),
            _ph('Best season: October to May', 5),
            _ph('Starting price: INR 56,800/- Per Guest (On Request)', 6),
            _ph('Vehicle: Private Executive AC SUV (Toyota Innova Crysta) with English/Hindi driver-guide | Meal Plan: MAPAI', 7),
            _ph('Route Plan: Dibrugarh ➔ Jorhat (2N) ➔ Kaziranga (2N) ➔ Guwahati (1N) ➔ Departure', 8),
            _ph('TRAGUIN Curated Advantage: Private tea planter interactions, tea leaf picking, vintage high teas, VIP wildlife access.', 9),
            _ph('Curated by TRAGUIN Experts: Heritage bungalows combining historical authenticity with modern luxury.', 10),
            _ph('Personalized Assistance: Dedicated trip manager tracking daily journey for family comfort.', 11),
            _ph('Shopping: Estate teas, Muga and Eri silks in Jorhat, bamboo crafts near Kaziranga.', 12),
            _ph('Important Notes: Kaziranga safaris Nov–Apr; book bungalows 60-90 days ahead; earthy colors for safaris.', 13),
        ],
        moods=['Family', 'Luxury', 'Cultural', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='INR 56,800/- Per Guest (On Request)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Tea Gardens Heritage • Dibrugarh • Jorhat • Kaziranga • 05 Nights / 06 Days',
        overview=(
            'Journey deep into the colonial elegance of the world\'s most illustrious tea country with British-era bungalows and UNESCO Kaziranga wetlands.\n\nTOUR OVERVIEW\\nDibrugarh Arrival ➔ Colonial Bungalow ➔ Jorhat Tea Capital (2 Nights) ➔ Kaziranga (2 Nights) ➔ Guwahati (1 Night) ➔ Departure with private tea tasting and jeep safaris.\n\nPREMIUM ASSAM EXPERIENCE\\nHeritage chang bungalows, tea cupping masterclasses, Majuli or Tocklai options, and Kaziranga rhino safaris across top tourist places in Assam.'
        ),
        seo_title='AS-008 | Tea Gardens Dibrugarh Jorhat Kaziranga | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days tea garden package (AS-008 / TG-AS-TEAGARDEN-008): colonial bungalows, tea tasting, Majuli option, Kaziranga safaris, 4-tier stays.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Dibrugarh arrival and colonial Chang Bungalow heritage Day 01', 1),
            _ih('Tea plucking ritual and sommelier tasting masterclass Jorhat Day 02', 2),
            _ih('Majuli Island or Tocklai Tea Research excursion Day 03', 3),
            _ih('Jorhat to Kaziranga with Orchid Park and cultural dances Day 04', 4),
            _ih('Dual jeep safaris in Kaziranga National Park Day 05', 5),
            _ih('Kaziranga to Guwahati departure along the Brahmaputra Day 06', 6),
        ],
        days=[
            _day(1, 'ARRIVAL DIBRUGARH | STEPPING INTO COLONIAL HERITAGE & CHANG BUNGALOW LUXURY', ('Heritage exploration begins at Dibrugarh Airport. TRAGUIN escorts you to an exquisite restored colonial Chang Bungalow with afternoon tea estate walk and colonial high tea on the verandah.'), [
                'Sightseeing Included: Mancotta / Purvi Tea Estate Walk, Heritage Property Tour.',
                'Evening Experience: Colonial-style high tea with local savory pastries.',
                'Overnight Stay: Handpicked Heritage Bungalow, Dibrugarh.',
                'Meals Included: Traditional Welcoming Dinner.',
            ]),
            _day(2, 'DIBRUGARH TO JORHAT | THE TEA PLUCKING RITUAL & TEA TASTING MASTERCLASS', ('Hands-on tea plucking experience then scenic drive to Jorhat tea capital. Afternoon exclusive tea cupping and tasting session with a master sommelier.'), [
                'Sightseeing Included: Interactive Tea Plucking, Jorhat Gymkhana Club (Historic Site).',
                'Evening Experience: Sommelier-led Tea Tasting Masterclass.',
                'Overnight Stay: Handpicked Boutique Tea Resort, Jorhat.',
                'Meals Included: Breakfast & Gourmet Dinner.',
            ]),
            _day(3, 'JORHAT EXCURSION | MAJULI ISLAND ENCOUNTER OR TOCKLAI EXPERIMENT CENTRE', ('Choice of Tocklai Tea Research Institute visit or private ferry to Majuli Island for Neo-Vaishnavite monasteries, mask-making, and monastic dances.'), [
                'Sightseeing Included: Tocklai Research Centre OR Majuli Island Monasteries (Satras).',
                'Optional Activities: Private pottery-making workshop with Majuli artisans.',
                'Overnight Stay: Handpicked Boutique Tea Resort, Jorhat.',
                'Meals Included: Breakfast & Multi-course Dinner.',
            ]),
            _day(4, 'JORHAT TO KAZIRANGA | FROM MANICURED ESTATES TO WILD UNTAMED JUNGLE', ('Travel to UNESCO Kaziranga National Park and ultra-luxury jungle lodge. Afternoon Orchid and Cultural Park with vibrant Assamese folk dances.'), [
                'Sightseeing Included: Kaziranga Orchid Park, Cultural Dance Amphitheater.',
                'Evening Experience: Open-air bonfire with storytelling by local naturalists.',
                'Overnight Stay: Premium Luxury Jungle Lodge, Kaziranga.',
                'Meals Included: Breakfast & Forest-Inspired Dinner.',
            ]),
            _day(5, 'KAZIRANGA NATIONAL PARK | THE WILDLIFE SAFARI EXPLORATION', ('Morning and afternoon private open-top 4x4 jeep safaris through Central/Western and Eastern (Agaratoli) ranges for rhinos, tigers, and migratory birds.'), [
                'Sightseeing Included: Morning & Afternoon Private 4x4 Jeep Safaris.',
                'Photography Points: Wildlife observation towers overlooking natural water bodies (Beels).',
                'Overnight Stay: Premium Luxury Jungle Lodge, Kaziranga.',
                'Meals Included: Breakfast, Lunch & Festive Farewell Dinner.',
            ]),
            _day(6, 'KAZIRANGA TO GUWAHATI | FINAL JOURNEY ALONG THE BRAHMAPUTRA', ('Final breakfast at jungle lodge then scenic trans-Assam highway to Guwahati Airport with optional Kamakhya viewpoint or silk boutique stop.'), [
                'Sightseeing Included: Trans-Assam Highway Scenic Drive, Airport Transfer route.',
                'Meals Included: Lavish Breakfast.',
            ])
        ],
        hotels=[
            _hotel('Mancotta Heritage Chang Bungalow | Infinity Oaks Resort / Kaziranga Resort', 'Dibrugarh / Jorhat (3 Nights) / Kaziranga (2 Nights)', '05 Nights', 'Deluxe', 'Heritage / Deluxe Room', 'Buffet Breakfast & Dinner (MAP)', 4, 1, description='OPTION 01 – DELUXE: Mancotta Heritage Chang Bungalow (Dibrugarh/Jorhat, 3N) | Infinity Oaks / Kaziranga Resort (Kaziranga, 2N) | Breakfast & Dinner (MAP)'),
            _hotel('Purvi Heritage Bungalows (Dibrugarh) | Borgos Resort / Kaziranga Wilderness', 'Dibrugarh / Jorhat (3 Nights) / Kaziranga (2 Nights)', '05 Nights', 'Premium', 'Premium Room', 'Buffet Breakfast & Dinner (MAP)', 4, 2, description='OPTION 02 – PREMIUM: Purvi Heritage Bungalows (Dibrugarh/Jorhat, 3N) | Borgos / Kaziranga Wilderness (Kaziranga, 2N) | Breakfast & Dinner (MAP)'),
            _hotel('Thengal Manor Heritage Hotel (Jorhat) | Diphlu River Lodge (Luxury Cabins)', 'Dibrugarh / Jorhat (3 Nights) / Kaziranga (2 Nights)', '05 Nights', 'Luxury', 'Heritage / Luxury Cabin', 'Premium Dining Package', 5, 3, description='OPTION 03 – LUXURY: Thengal Manor Heritage Hotel (Jorhat, 3N) | Diphlu River Lodge Luxury Cabins (Kaziranga, 2N) | Premium Dining Package'),
            _hotel('Kaziranga Golf Resort (Private Bungalows) | The Ultimate Travelling Camp (TUTC)', 'Dibrugarh / Jorhat (3 Nights) / Kaziranga (2 Nights)', '05 Nights', 'Ultra Luxury', 'Private Bungalow / Luxury Tent', 'Bespoke Personal Chef Menu', 5, 4, description='OPTION 04 – ULTRA LUXURY: Kaziranga Golf Resort Private Bungalows (Jorhat, 3N) | TUTC (Kaziranga, 2N) | Bespoke Personal Chef Menu')
        ],
        inclusions=[
            _inc_included('Bespoke Stays: 05 Nights accommodation in selected premium tea bungalows and luxury safari lodges.', 1),
            _inc_included('Luxury Ground Fleet: Entire journey via Air-Conditioned Toyota Innova Crysta with permits, toll taxes, and driver fees.', 2),
            _inc_included('Meal Package: 05 Elegant Buffet Breakfasts and 05 Chef-curated Dinners at the properties.', 3),
            _inc_included('Exclusive Experiences: Private Tea Tasting Session with estate sommelier & entry tickets to the Orchid Park.', 4),
            _inc_included('Wildlife Exploration: 02 Private 4x4 open Jeep Safaris in Kaziranga National Park with professional trackers.', 5),
            _inc_included('TRAGUIN Services: Personalized welcome gifts, daily premium bottled water, and dedicated 24/7 on-ground support.', 6),
            _inc_excluded('Air/Rail Tickets: Commercial flights or train connections to Dibrugarh and out of Guwahati.', 7),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, alcoholic beverages, and tips for estate staff or drivers.', 8),
            _inc_excluded('Camera Charges: Specific video camera or high-end DSLR fees at national park checkpoints.', 9),
            _inc_excluded('Optional Excursions: Majuli Island ferry costs and local guide hires outside the primary plan.', 10),
            _inc_excluded('Unforeseen Overheads: Additional costs from flight cancellations, natural weather delays, or unexpected events.', 11)
        ],
    )
    return package, itinerary


def build_as_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AS-009'
    tour_code = 'TG-LUX-AS009-2026'
    title = 'TRAGUIN Premium Luxury Assam Retreat — Wild Horizon: Guwahati • Kaziranga • Brahmaputra River Cruise'
    duration = '05 Nights / 06 Days'
    slug = 'as-009-luxury-assam-retreat-kaziranga-cruise'
    itin_slug = 'as-009-luxury-assam-retreat-kaziranga-cruise-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code AS-009 | TRAGUIN tour code TG-LUX-AS009-2026', 1),
            _ph('State / Country: Assam, India | Category: Luxury Assam Retreat', 2),
            _ph('Destinations Covered: Guwahati • Kaziranga National Park • Absolute Luxury River Cruise', 3),
            _ph('Ideal for: Discerning Families, High-End Wildlife Enthusiasts, Experiential Travelers', 4),
            _ph('Best season: November to April (Optimal Wildlife Sightings)', 5),
            _ph('Starting price: INR 1,24,500/- Per Guest (On Bespoke Basis)', 6),
            _ph('Vehicle: Ultra-Premium SUV (Mercedes-Benz GLS or Toyota Vellfire) | Meal Plan: Fully Inclusive Royal Assamese Gastronomy', 7),
            _ph('Route Plan: Guwahati ➔ Kaziranga (3N) ➔ Guwahati Riverside (2N) ➔ Departure', 8),
            _ph('TRAGUIN Signature Experience: Private champagne high tea on authentic heritage colonial plantation cottage grounds.', 9),
            _ph('Curated by TRAGUIN Experts: Every detail reviewed for complete privacy, comfort, and exceptional service.', 10),
            _ph('Personalized Assistance: 24/7 on-ground luxury manager for adjustments and special requests.', 11),
            _ph('Shopping: Golden Muga silk, bespoke tea collections, bamboo decor and rhino wood carvings.', 12),
            _ph('Important Notes: Safaris seasonal; book 60-90 days ahead; neutral safari clothing; AC paused during forest drives.', 13),
        ],
        moods=['Family', 'Luxury', 'Nature', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='INR 1,24,500/- Per Guest (On Bespoke Basis)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Luxury Assam Retreat • Kaziranga • Brahmaputra Cruise • 05 Nights / 06 Days',
        overview=(
            'Extraordinary journey blending boutique wildlife lodges, private charters, and the realm of the Great Indian One-Horned Rhinoceros.\n\nTOUR OVERVIEW\\nGuwahati ➔ Kaziranga (3 Luxury Nights) ➔ Guwahati Premium Riverside (2 Nights) with private safaris, executive airport clearance, and heritage tea high-tea.\n\nWHY CHOOSE THE LUXURY ASSAM RETREAT?\\nPrivate safaris, Brahmaputra serenity with Ganges dolphins, colonial tea plantations, and premium handpicked hotels across top Assam sightseeing.'
        ),
        seo_title='AS-009 | Luxury Assam Retreat Kaziranga Cruise | TRAGUIN',
        seo_description='Ultra-premium 05 Nights / 06 Days Assam retreat (AS-009 / TG-LUX-AS009-2026): private safaris, heritage tea estate, Brahmaputra charter, Kamakhya VIP, 4-tier luxury.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Private escort to Kaziranga ultra-luxury lodge Day 01', 1),
            _ih('Central and Western Range private safaris with senior naturalist Day 02', 2),
            _ih('Heritage tea estate immersion with champagne high tea Day 03', 3),
            _ih('Exclusive private Brahmaputra sunset charter Day 04', 4),
            _ih('VIP Kamakhya Shrine and golden Muga silk heritage Day 05', 5),
            _ih('Departure with cherished memories Day 06', 6),
        ],
        days=[
            _day(1, 'GUWAHATI ARRIVAL | PRIVATE ESCORT TO KAZIRANGA WILDLIFE SANCTUARY', ('TRAGUIN luxury concierge at premium arrivals lounge. Magnificent scenic drive through tea estates to ultra-luxury Kaziranga jungle lodge with welcome cocktail and folk musicians.'), [
                'Sightseeing Included: Scenic foothills drive, private tea estate entry.',
                'Evening Experience: Private tribal dance performance and welcome reception.',
                'Overnight Stay: Ultra-Luxury Lodge in Kaziranga.',
                'Meals Included: Curated Welcome Dinner.',
            ]),
            _day(2, 'KAZIRANGA NATIONAL PARK | DAWN SAFARI & EVENING JEEP TRACKING', ('Early morning private Central Range safari with senior naturalist. Afternoon pool relaxation then Western Range golden-hour tracking expedition.'), [
                'Sightseeing Included: Central & Western Range private safaris.',
                'Optional Activities: Therapeutic wellness treatment at the luxury lodge spa.',
                'Overnight Stay: Ultra-Luxury Lodge in Kaziranga.',
                'Meals Included: All Inclusive Gourmet Plan.',
            ]),
            _day(3, 'HERITAGE TEA ESTATE IMMERSION | CHIEFS & CHAMPAGNE HIGH TEA', ('Privately owned colonial plantation with estate manager walk, orthodox tea-tasting masterclass with champagne on heritage bungalow verandah, and bonfire dinner under stars.'), [
                'Sightseeing Included: Colonial Tea Factory & Heritage Bungalow Grounds.',
                'Local Experience: Premium Orthodox tea-tasting masterclass with a master blender.',
                'Overnight Stay: Ultra-Luxury Lodge in Kaziranga.',
                'Meals Included: Breakfast, Estate Lunch & Al-Fresco Dinner.',
            ]),
            _day(4, 'KAZIRANGA TO GUWAHATI | EXCLUSIVE PRIVATE BRAHMAPUTRA SUNSET CHARTER', ('Return to ultra-premium Guwahati hotel then exclusive charter boat with local delicacies, cocktails, and crimson sunset behind Nilachal Hills.'), [
                'Sightseeing Included: Silk-weaving route stop, Private River Charter.',
                'Evening Experience: Live soothing instrumental music on board.',
                'Overnight Stay: Ultra-Luxury Hotel in Guwahati.',
                'Meals Included: Breakfast & On-board Dining Experience.',
            ]),
            _day(5, 'GUWAHATI CULTURE | VIP SHRINE ACCESS & GOLDEN SILK HERITAGE', ('Fast-track VIP Kamakhya Temple access, optional Muga silk artisan workshop, and intimate fine-dining farewell dinner with refined regional cuisine.'), [
                'Sightseeing Included: Kamakhya Temple (VIP Entry), Silk Heritage Center.',
                'Local Experience: Curated shopping tour of luxury textile collections.',
                'Overnight Stay: Ultra-Luxury Hotel in Guwahati.',
                'Meals Included: Breakfast & Premium Farewell Dinner.',
            ]),
            _day(6, 'DEPARTURE | JOURNEY HOME WITH CHERISHED MEMORIES', ('Gourmet breakfast on riverview terraces before seamless luxury SUV transfer to Guwahati International Airport.'), [
                'Sightseeing Included: Private Airport Terminal Transit.',
                'Meals Included: Premium Buffet Breakfast.',
            ])
        ],
        hotels=[
            _hotel('Infinity Resorts / Borgos Resort | Kiranshree Grand Luxury Rooms', 'Kaziranga (3 Nights) / Guwahati (2 Nights)', '05 Nights', 'Deluxe', 'Luxury Room', 'Breakfast & Dinner (MAP)', 4, 1, description='OPTION 01 – DELUXE: Infinity Resorts / Borgos Resort (Kaziranga, 3N) | Kiranshree Grand (Guwahati, 2N) | Breakfast & Dinner (MAP)'),
            _hotel('Diphlu River Lodge (Standard Cottage) | Novotel Guwahati (Executive Suite)', 'Kaziranga (3 Nights) / Guwahati (2 Nights)', '05 Nights', 'Premium', 'Standard Cottage / Executive Suite', 'Breakfast & Dinner (MAP)', 4, 2, description='OPTION 02 – PREMIUM: Diphlu River Lodge Standard Cottage (Kaziranga, 3N) | Novotel Guwahati Executive Suite (Guwahati, 2N) | Breakfast & Dinner (MAP)'),
            _hotel('Diphlu River Lodge (Luxury River Suite) | Radisson Blu (Executive Panorama View)', 'Kaziranga (3 Nights) / Guwahati (2 Nights)', '05 Nights', 'Luxury', 'Luxury River Suite', 'Full Inclusive Board (APAI)', 5, 3, description='OPTION 03 – LUXURY: Diphlu River Lodge Luxury River Suite (Kaziranga, 3N) | Radisson Blu Executive Panorama (Guwahati, 2N) | Full Inclusive Board (APAI)'),
            _hotel('The Ultimate Travelling Camp (TUTC) / Taj Safari | Vivanta Guwahati (Presidential Suite)', 'Kaziranga (3 Nights) / Guwahati (2 Nights)', '05 Nights', 'Ultra Luxury', 'Luxury Tent / Presidential Suite', 'Bespoke Elite Dining Plan', 5, 4, description='OPTION 04 – ULTRA LUXURY: TUTC / Taj Safari (Kaziranga, 3N) | Vivanta Guwahati Presidential Suite (Guwahati, 2N) | Bespoke Elite Dining Plan')
        ],
        inclusions=[
            _inc_included('Premium Accommodations: Five nights at top-tier luxury hotels and safari lodges on a twin/triple-share basis.', 1),
            _inc_included('Luxury Fleet Transport: Full tour transfers using Mercedes-Benz GLS or Toyota Vellfire SUV, covering all tolls, fuel, and driver fees.', 2),
            _inc_included('Bespoke Meal Plan: Daily multi-course breakfasts, custom lunches, and specialty dinners as detailed.', 3),
            _inc_included('TRAGUIN Support & Amenities: Personalized welcome gifts, premium Assamese Orthodox tea sets, and unlimited bottled spring water.', 4),
            _inc_included('Exclusive Experiences: Private sunset charter cruise on the Brahmaputra River and expedited VIP entry at Kamakhya Temple.', 5),
            _inc_included('Expert Logistics: Accompanied by certified expert naturalists during private national park safaris.', 6),
            _inc_excluded('Flights / Rail: Domestic or international airfares to and from Guwahati.', 7),
            _inc_excluded('Personal Incidental Charges: Laundry, premium phone services, or extended minibar purchases.', 8),
            _inc_excluded('Optional Excursions: Additional activities or private purchases not specified in the main itinerary.', 9),
            _inc_excluded('Insurance Coverage: Personal travel, medical, or baggage loss insurance policies.', 10),
            _inc_excluded('Unforeseen Circumstances: Extra costs resulting from flight disruptions, weather delays, or structural road changes.', 11)
        ],
    )
    return package, itinerary


def build_as_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AS-010'
    tour_code = 'TG-AS-010-LEISURE'
    title = 'TRAGUIN Premium Assam Tour Package for Senior Citizens — Leisure Kaziranga: Guwahati • Kaziranga National Park'
    duration = '05 Nights / 06 Days'
    slug = 'as-010-senior-citizen-leisure-kaziranga-guwahati'
    itin_slug = 'as-010-senior-citizen-leisure-kaziranga-guwahati-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code AS-010 | TRAGUIN tour code TG-AS-010-LEISURE', 1),
            _ph('State / Country: Assam, India | Category: Senior Citizen Leisure Tour', 2),
            _ph('Destinations Covered: Guwahati • Kaziranga National Park', 3),
            _ph('Ideal for: Senior Citizens, Families, Nature Lovers', 4),
            _ph('Best season: November to April', 5),
            _ph('Starting price: On Request (Premium Inclusive)', 6),
            _ph('Vehicle: Private luxury AC Toyota Innova Crysta with patient destination-trained chauffeur | Meal Plan: MAPAI', 7),
            _ph('Route Plan: Guwahati ➔ Kaziranga (3N) ➔ Guwahati (2N) ➔ Departure', 8),
            _ph('TRAGUIN Welcome Note: Dedicated ground handler support and VIP fast-track coordination at historic temples.', 9),
            _ph('Curated by TRAGUIN Experts: Hand-vetted transit routes and properties ensuring comfortable mobility.', 10),
            _ph('Personalized Assistance: Dedicated local ground coordinators available around the clock.', 11),
            _ph('Shopping: Muga and Eri silks, organic tea from Upper Assam, cane baskets and bamboo decor.', 12),
            _ph('Important Notes: Share dietary needs 14 days ahead; safari seating for back concerns; light shawls Nov–Feb.', 13),
        ],
        moods=['Family', 'Luxury', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Inclusive)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Senior Citizen Leisure • Guwahati • Kaziranga • 05 Nights / 06 Days',
        overview=(
            'Deeply therapeutic journey through the green heart of Northeast India optimized for senior citizens with leisurely rhythm and premier luxury safety.\n\nTOUR OVERVIEW\\nLeisure Assam Holiday avoiding strenuous journeys with low-step vehicles, elevator-access hotels, and light cultural strolls. Route: Guwahati ➔ Kaziranga (3N) ➔ Guwahati (2N).\n\nWHY CHOOSE THIS PREMIUM ASSAM EXPERIENCE?\\nSpiritual Kamakhya VIP, comfortable jeep safaris for rhino viewing, orchid gardens, tea plantations, and TRAGUIN elimination of long waiting lines.'
        ),
        seo_title='AS-010 | Senior Citizen Leisure Kaziranga | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days senior citizen Assam package (AS-010 / TG-AS-010-LEISURE): gentle Kaziranga safaris, orchid park, Brahmaputra cruise, Kamakhya VIP, 4-tier hotels.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Arrival and smooth highway drive to Kaziranga Day 01', 1),
            _ih('Comfortable Western Range jeep safari Day 02', 2),
            _ih('Orchid garden ambles and cultural weaving tales Day 03', 3),
            _ih('Return to Guwahati with Brahmaputra sunset cruise Day 04', 4),
            _ih('VIP Kamakhya darshan and Kalakshetra cultural museum Day 05', 5),
            _ih('Relaxed departure Day 06', 6),
        ],
        days=[
            _day(1, 'ARRIVAL IN GUWAHATI | DRIVE THROUGH FLOATING MIST TO KAZIRANGA', ('TRAGUIN airport coordinator receives you at arrival gate. Smooth flat highway journey past paddy fields with premium highway tea stop to handpicked Kaziranga luxury resort.'), [
                'Sightseeing Included: Scenic highway drive, welcoming resort orientation.',
                'Evening Experience: Relaxing evening by the resort fireplace with local light music.',
                'Overnight Stay: Handpicked Luxury Resort in Kaziranga.',
                'Meals Included: Premium Dinner.',
            ]),
            _day(2, 'KAZIRANGA JEEP SAFARI | CHRONICLES OF THE ONE-HORNED RHINO', ('Relaxed breakfast then comfortable open-top private Jeep Safari in Western Range with expert naturalist viewing rhinos, buffaloes, and swamp deer without strenuous walking.'), [
                'Sightseeing Included: Kaziranga Western Range Private Safari.',
                'Optional Activities: Short bird-watching session from the resort balcony.',
                'Overnight Stay: Handpicked Luxury Resort in Kaziranga.',
                'Meals Included: Breakfast, Lunch & Dinner.',
            ]),
            _day(3, 'ORCHID GARDEN AMBLES & CULTURAL WEAVING TALES', ('Slow-paced Kaziranga Orchid and Cultural Park with paved pathways, seated Bihu cultural presentation, and gentle neighboring tea estate walk.'), [
                'Sightseeing Included: National Orchid Park, Tea Garden walk.',
                'Evening Experience: Local Assamese traditional cultural dance show.',
                'Overnight Stay: Handpicked Luxury Resort in Kaziranga.',
                'Meals Included: Breakfast & Gourmet Dinner.',
            ]),
            _day(4, 'KAZIRANGA TO GUWAHATI | SUNSET ON THE BRAHMAPUTRA', ('Peaceful breakfast, return to Guwahati ultra-premium hotel, and exclusive private sunset cruise on the majestic Brahmaputra with gentle breezes and light music.'), [
                'Sightseeing Included: Return road trip, Luxury River Cruise.',
                'Evening Experience: Relaxing tea session on the cruise ship deck.',
                'Overnight Stay: Luxury Hotel in Guwahati.',
                'Meals Included: Breakfast & Elegant Dinner.',
            ]),
            _day(5, 'SPIRITUAL SOLACE | VIP KAMAKHYA DARSHAN & HERITAGE MUSEUM', ('Seamless fast-track VIP Kamakhya Temple visit with minimized walking. Afternoon Srimanta Sankaradeva Kalakshetra open-air museum and light silk souvenir shopping.'), [
                'Sightseeing Included: VIP Kamakhya Temple, Kalakshetra Cultural Centre.',
                'Photography Points: Scenic hill views overlooking the Guwahati cityscape.',
                'Overnight Stay: Luxury Hotel in Guwahati.',
                'Meals Included: Breakfast & Farewell Dinner.',
            ]),
            _day(6, 'DEPARTURE | EVERLASTING FAMILY MEMORIES', ('Final luxury breakfast and comfortable private transfer to Guwahati International Airport.'), [
                'Sightseeing Included: Private airport transfer.',
                'Meals Included: Full Buffet Breakfast.',
            ])
        ],
        hotels=[
            _hotel('Infinity Resort / Borgos Resort (Executive) | Kiranshree Grand / Hotel Shoolin Grand', 'Kaziranga (3 Nights) / Guwahati (2 Nights)', '05 Nights', 'Deluxe', 'Executive / Deluxe Room', 'Breakfast & Dinner (MAP)', 4, 1, description='OPTION 01 – DELUXE: Infinity Resort / Borgos Resort Executive (Kaziranga, 3N) | Kiranshree Grand / Shoolin Grand (Guwahati, 2N) | Breakfast & Dinner (MAP)'),
            _hotel('Diphlu River Lodge (Standard Cottage) | Novotel Guwahati GS Road', 'Kaziranga (3 Nights) / Guwahati (2 Nights)', '05 Nights', 'Premium', 'Standard Cottage', 'Breakfast & Dinner (MAP)', 4, 2, description='OPTION 02 – PREMIUM: Diphlu River Lodge Standard Cottage (Kaziranga, 3N) | Novotel Guwahati GS Road (Guwahati, 2N) | Breakfast & Dinner (MAP)'),
            _hotel('Borgos Resort (Luxury Suite Tier) | Radisson Blu Hotel Guwahati', 'Kaziranga (3 Nights) / Guwahati (2 Nights)', '05 Nights', 'Luxury', 'Luxury Suite', 'Gourmet Inclusive MAP', 5, 3, description='OPTION 03 – LUXURY: Borgos Resort Luxury Suite (Kaziranga, 3N) | Radisson Blu Hotel Guwahati (Guwahati, 2N) | Gourmet Inclusive MAP'),
            _hotel('Diphlu River Lodge (Premium River Villa) | Vivanta Guwahati (Taj Group Heritage)', 'Kaziranga (3 Nights) / Guwahati (2 Nights)', '05 Nights', 'Ultra Luxury', 'Premium River Villa', 'Bespoke Chef MAP Plan', 5, 4, description='OPTION 04 – ULTRA LUXURY: Diphlu River Lodge Premium River Villa (Kaziranga, 3N) | Vivanta Guwahati Taj Group (Guwahati, 2N) | Bespoke Chef MAP Plan')
        ],
        inclusions=[
            _inc_included('Premium Stays: 5 Nights accommodation at top-rated hotels featuring elevator access and senior-friendly room designs.', 1),
            _inc_included('Luxury Transportation: Private air-conditioned Toyota Innova Crysta for all transfers and sightseeing.', 2),
            _inc_included('Curated Dining: 5 comprehensive breakfasts and 5 mild, freshly prepared dinners suited to guest preferences.', 3),
            _inc_included('TRAGUIN Welcome Amenities: Assamese Gamosa greeting, daily packaged water bottles, and premium tea sampler kit.', 4),
            _inc_included('Exclusive Experiences: Private Brahmaputra Sunset Cruise and fast-track VIP entry coordination at Kamakhya Temple.', 5),
            _inc_included('Dedicated Assistance: On-ground passenger assistance and luggage handling by TRAGUIN team members.', 6),
            _inc_included('All Applicable Taxes: Comprehensive toll fees, parking, driver allowances, and state taxes included.', 7),
            _inc_excluded('Air / Train Tickets: Airfare or railway tickets to and from Guwahati.', 8),
            _inc_excluded('Personal Expenses: Laundry service, room telephone calls, and premium alcoholic beverages.', 9),
            _inc_excluded('Optional Extras: Camera fees, individual monument entry tickets, and tips for local guides.', 10),
            _inc_excluded('Medical Insurance: Travel and medical insurance coverage.', 11)
        ],
    )
    return package, itinerary


def build_as_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AS-011'
    tour_code = 'TG-ED-AS011-2026'
    title = 'TRAGUIN Premium Assam Educational Tour Package — Student Learning: Guwahati • Pobitora • Kaziranga National Park'
    duration = '04 Nights / 05 Days'
    slug = 'as-011-educational-student-pobitora-kaziranga'
    itin_slug = 'as-011-educational-student-pobitora-kaziranga-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code AS-011 | TRAGUIN tour code TG-ED-AS011-2026', 1),
            _ph('State / Country: Assam, India | Category: School Educational Tour', 2),
            _ph('Destinations Covered: Guwahati • Kaziranga National Park • Pobitora', 3),
            _ph('Ideal for: Student Groups, Academic Institutions, Researchers', 4),
            _ph('Best season: November to April', 5),
            _ph('Starting price: Student Group Concession (On Request)', 6),
            _ph('Vehicle: Dedicated Luxury AC Coaches with certified safety features | Meal Plan: Full Board Academic Plan (APAI)', 7),
            _ph('Route Plan: Guwahati ➔ Pobitora Ecology Briefing ➔ Kaziranga (2N) ➔ Guwahati Historical Survey (2N) ➔ Departure', 8),
            _ph('TRAGUIN Curated Note: Dedicated field guides, interactive worksheets, educational handbooks, and multi-point security coordination.', 9),
            _ph('Curated by Experts: Learning exercises aligned with leading academic curricula.', 10),
            _ph('Personalized Assistance: Support desks for faculty with student headcounts and medical needs.', 11),
            _ph('Shopping: Orchid center organic remedies, bamboo handicraft centers, Guwahati book centers.', 12),
            _ph('Important Notes: Follow safari safety guidelines; monitor plastic usage in Kaziranga; book 60 days ahead for concessions.', 13),
        ],
        moods=['Cultural', 'Family', 'Nature', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='Student Group Concession (On Request)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Educational Student Tour • Pobitora • Kaziranga • 04 Nights / 05 Days',
        overview=(
            'Enlightening academic voyage combining rigorous learning modules with immersive experiences across Assam\'s biodiversity hotspots.\n\nTOUR OVERVIEW\\nEducational Assam Tour for academic excellence: Guwahati ➔ Pobitora ➔ Kaziranga (2N) ➔ Guwahati (2N) with luxury AC coaches and field research modules.\n\nWHY PLAN AN EDUCATIONAL ASSAM TOUR?\\nKaziranga rhino conservation, Brahmaputra hydro-geomorphology, bio-diversity research stations, and sustainable silk cultivation for student field excursions.'
        ),
        seo_title='AS-011 | Educational Student Tour Pobitora Kaziranga | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Assam educational package (AS-011 / TG-ED-AS011-2026): Pobitora ecology, Kaziranga safari, tea estate study, science centre, Brahmaputra cruise.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Pobitora ecology briefing and grassland field session Day 01', 1),
            _ih('Wetland survey and Kaziranga Orchid Park ethnobotanical mapping Day 02', 2),
            _ih('Kaziranga jeep safari and tea plantation manufacturing study Day 03', 3),
            _ih('Regional Science Centre and Brahmaputra hydro-geography cruise Day 04', 4),
            _ih('Kamakhya architectural survey and academic certificate wrap-up Day 05', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN GUWAHATI | FIELD BRIEFING & TRANSFER TO POBITORA ECO-ZONE', ('Student groups welcomed at Guwahati airport by TRAGUIN tour managers. Premium AC coach to Pobitora for interactive conservationist orientation on alluvial grasslands and rhino habitats.'), [
                'Sightseeing Included: Pobitora Buffer Zone, Wetland Observation Deck.',
                'Learning Activity: Grassland Ecology Field Briefing and Q&A session.',
                'Overnight Stay: Handpicked Student Resort / Eco Lodge near Pobitora/Guwahati.',
                'Meals Included: Lunch & Dinner.',
            ]),
            _day(2, 'POBITORA TO KAZIRANGA | WETLAND SURVEY & ORCHID BIODIVERSITY CENTER', ('Early bird-watching and wetland survey then scenic drive to UNESCO Kaziranga. Visit Orchid and Cultural Park for ethnobotanical mapping and folk culture showcase.'), [
                'Sightseeing Included: Kaziranga Orchid Park, Conservation Greenhouses.',
                'Learning Activity: Ethnobotanical mapping and local folk culture showcase.',
                'Overnight Stay: Handpicked Eco-Resort in Kaziranga.',
                'Meals Included: Breakfast, Lunch, Dinner.',
            ]),
            _day(3, 'KAZIRANGA WILDLIFE SAFARI | MEGAMAMMAL CONSERVATION MODULE', ('Early open jeep safari observing rhinos, buffaloes, and birds. Afternoon tea processing estate study of economic geography and fair-trade labor models.'), [
                'Sightseeing Included: Kaziranga National Park Jeep Safari, Tea Plantation Estate.',
                'Learning Activity: Habitat observation logging and agricultural manufacturing study.',
                'Overnight Stay: Handpicked Eco-Resort in Kaziranga.',
                'Meals Included: Breakfast, Lunch, Dinner.',
            ]),
            _day(4, 'KAZIRANGA TO GUWAHATI | REGIONAL SCIENCE MUSEUM & BRAHMAPUTRA HYDROLOGY CRUISE', ('Regional Science Centre interactive galleries then exclusive educational Brahmaputra cruise lecture on river island formation and silt dynamics.'), [
                'Sightseeing Included: Regional Science Centre, Brahmaputra Educational Cruise.',
                'Learning Activity: Hydro-geographic lecture and interactive science experiments.',
                'Overnight Stay: Premium Hotel in Guwahati.',
                'Meals Included: Breakfast, Lunch, Dinner.',
            ]),
            _day(5, 'GUWAHATI HISTORICAL SURVEY | KAMAKHYA STUDIES & DEPARTURE', ('Kamakhya Temple compound architectural study, field notes wrap-up session, academic certificate distribution, and safe group airport transfer.'), [
                'Sightseeing Included: Kamakhya Temple Complex, Archaeological view points.',
                'Learning Activity: Final presentation and distribution of academic certificates.',
                'Meals Included: Breakfast & Packed Box Lunch.',
            ])
        ],
        hotels=[
            _hotel('Pobitora Village Eco Resort | Kaziranga Village Resort / Aranya | Hotel Dynasty / Landmark', 'Pobitora/Guwahati (1 Night) / Kaziranga (2 Nights) / Guwahati (1 Night)', '04 Nights', 'Deluxe', 'Student / Executive Room', 'Full Board (APAI)', 4, 1, description='OPTION 01 – DELUXE: Pobitora Village Eco Resort (Night 1) | Kaziranga Village Resort / Aranya (Nights 2-3) | Hotel Dynasty / Landmark (Night 4)'),
            _hotel('Mayang Village Eco Camp | Infinity Resort / Borgos Resort | Kiranshree Grand / Novotel', 'Pobitora/Guwahati (1 Night) / Kaziranga (2 Nights) / Guwahati (1 Night)', '04 Nights', 'Premium', 'Premium Room', 'Full Board (APAI)', 4, 2, description='OPTION 02 – PREMIUM: Mayang Village Eco Camp (Night 1) | Infinity / Borgos (Nights 2-3) | Kiranshree Grand / Novotel (Night 4)'),
            _hotel('The Brahmaputra River Lodge | Iora - The Retreat / Diphlu River Lodge | Radisson Blu Guwahati', 'Pobitora/Guwahati (1 Night) / Kaziranga (2 Nights) / Guwahati (1 Night)', '04 Nights', 'Luxury', 'Luxury Room', 'Full Board (APAI)', 5, 3, description='OPTION 03 – LUXURY: The Brahmaputra River Lodge (Night 1) | Iora / Diphlu (Nights 2-3) | Radisson Blu (Night 4)'),
            _hotel('Bespoke Premium Private Cruise | Taj Kaziranga Safari Lodge | Vivanta Guwahati (Taj Group)', 'Pobitora/Guwahati (1 Night) / Kaziranga (2 Nights) / Guwahati (1 Night)', '04 Nights', 'Ultra Luxury', 'Luxury Suite', 'Full Board (APAI)', 5, 4, description='OPTION 04 – ULTRA LUXURY: Bespoke Premium Private Cruise (Night 1) | Taj Kaziranga Safari Lodge (Nights 2-3) | Vivanta Guwahati (Night 4)')
        ],
        inclusions=[
            _inc_included('Accommodation: Safe multi-share or twin room configurations across curated handpicked hotels.', 1),
            _inc_included('Luxury Transportation: Entire itinerary via premium AC luxury coaches including fuel, driver allowances, and permits.', 2),
            _inc_included('Hygienic Catering: All student-friendly meals (Breakfast, Lunch, Dinner) included as listed.', 3),
            _inc_included('Field Access: Open Jeep Safari permits for Kaziranga and standard entry tickets to all science centres.', 4),
            _inc_included('Welcome Amenities: Student learning portfolios, custom clipboards, identification tags, and welcome stoles.', 5),
            _inc_included('TRAGUIN Support: On-site student coordinators, first-aid kits, and real-time medical backup.', 6),
            _inc_excluded('Travel Costs: Institutional airfare or train transit tickets to and from Guwahati.', 7),
            _inc_excluded('Personal Media: Camera premium recording passes or drone use permits inside sanctuary zones.', 8),
            _inc_excluded('Incidentals: Laundry, individual cold drinks, snacks, or extra souvenir shopping.', 9),
            _inc_excluded('Unforeseen Overheads: Expenses from flight cancellations, bad weather, or sudden national holidays.', 10)
        ],
    )
    return package, itinerary


def build_as_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AS-012'
    tour_code = 'TG-ASM-ADV-012'
    title = 'TRAGUIN Premium Assam Adventure Tour Package — Brahmaputra Rafting: Guwahati • Kaziranga • River Basin'
    duration = '05 Nights / 06 Days'
    slug = 'as-012-adventure-rafting-brahmaputra-kaziranga'
    itin_slug = 'as-012-adventure-rafting-brahmaputra-kaziranga-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code AS-012 | TRAGUIN tour code TG-ASM-ADV-012', 1),
            _ph('State / Country: Assam, India | Category: Luxury Adventure', 2),
            _ph('Destinations Covered: Guwahati • Kaziranga • Brahmaputra River Basin', 3),
            _ph('Ideal for: Thrill-Seekers, Wildlife Lovers & Corporate Retreats', 4),
            _ph('Best season: November to April', 5),
            _ph('Starting price: INR 56,000/- Per Guest', 6),
            _ph('Vehicle: Private Luxury AC 4x4 All-Terrain SUV with expert tracker-chauffeur | Meal Plan: Jungle MAPAI', 7),
            _ph('Route Plan: Guwahati ➔ Kaziranga (3N) ➔ Brahmaputra River Excursions ➔ Guwahati (2N) ➔ Departure', 8),
            _ph('TRAGUIN Signature Experience: Private secluded sand-island picnic on the Brahmaputra with custom menu.', 9),
            _ph('Curated by TRAGUIN Experts: Every safari path, rafting route, and property personally vetted for safety and luxury.', 10),
            _ph('Premium Handpicked Hotels: Boutique accommodations balancing modern luxury with natural surroundings.', 11),
            _ph('Shopping: Fancy Bazar Muga silk sarees, hand-woven stoles, bamboo artifacts, Assamese fish curries.', 12),
            _ph('Important Notes: Safaris weather-dependent; rafting depends on water levels; book properties 45-60 days ahead.', 13),
        ],
        moods=['Adventure', 'Luxury', 'Nature', 'Family'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='INR 56,000/- Per Guest',
        rating=Decimal("4.9"), review_count=0,
        tagline='Assam Adventure • Brahmaputra Rafting • Kaziranga • 05 Nights / 06 Days',
        overview=(
            'Adrenaline-infused high-end expedition through untamed Northeast India with luxury intertwined with raw wilderness.\n\nTOUR OVERVIEW\\nElite Brahmaputra Adventure: Guwahati ➔ Kaziranga (3N) ➔ River Excursions ➔ Guwahati (2N) with private rafting access and elite luxury camping amenities.\n\nWHY UNDERTAKE THE PREMIUM ASSAM ADVENTURE?\\nRhino safaris, Brahmaputra white-water rafting, Gangetic dolphins, misty Kaziranga sunrise frames, and ancient Guwahati spiritual landmarks.'
        ),
        seo_title='AS-012 | Adventure Rafting Brahmaputra Kaziranga | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Assam adventure (AS-012 / TG-ASM-ADV-012): jeep safaris, Brahmaputra rafting, sand-island picnic, sunset cruise, Kamakhya VIP, 4-tier hotels.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Scenic 4x4 drive to Kaziranga with tribal campfire Day 01', 1),
            _ih('Central and Western Range jeep safaris and Orchid Park Day 02', 2),
            _ih('Brahmaputra rafting and Gangetic dolphin spotting Day 03', 3),
            _ih('Return to Guwahati with premium sunset cruise Day 04', 4),
            _ih('Kamakhya VIP, Umananda Island, and Muga silk weaving Day 05', 5),
            _ih('Departure from wild valley Day 06', 6),
        ],
        days=[
            _day(1, 'GUWAHATI ARRIVAL | SCENIC HIGHWAY DRIVE TO KAZIRANGA WILDLIFE RESERVE', ('Traditional Gamosa welcome at Guwahati airport. Premium all-terrain 4x4 drive along Brahmaputra banks past tea estates to luxury wilderness lodge with open-air tribal campfire.'), [
                'Sightseeing Included: Tea Estate Viewpoints, Forest Fringe Trail.',
                'Evening Experience: Traditional Karbi tribal campfire and dinner.',
                'Overnight Stay: Handpicked Luxury Jungle Lodge in Kaziranga.',
                'Meals Included: Welcome Drinks & Luxury Dinner.',
            ]),
            _day(2, 'KAZIRANGA JUNGLE SAFARI | TRACKING THE ONE-HORNED RHINO', ('Dawn private Central Range jeep safari tracking rhinos and buffaloes. Afternoon Western Range safari and Kaziranga Orchid National Biodiversity Park with 500+ orchid species.'), [
                'Sightseeing Included: Kaziranga Jeep Safaris (Central & Western Zones), Orchid Park.',
                'Photography Points: Kohora watchtowers overlooking sprawling water bodies.',
                'Overnight Stay: Handpicked Luxury Jungle Lodge in Kaziranga.',
                'Meals Included: Buffet Breakfast & Themed Dinner.',
            ]),
            _day(3, 'BRAHMAPUTRA RIVER WATER ADVENTURE | RAFTING & DOLPHIN SPOTTING', ('Premium safety gear and certified river masters guide private rafts on Brahmaputra currents with Gangetic dolphin spotting and exclusive gourmet sand-island picnic lunch.'), [
                'Sightseeing Included: Brahmaputra Basin Rafting, Isolated Sand Island Exploration.',
                'Optional Activities: Controlled river swimming, wildlife bird-watching from water channels.',
                'Overnight Stay: Premium Riverside Boutique Property / Lodge.',
                'Meals Included: Breakfast, Island Picnic Lunch, Dinner.',
            ]),
            _day(4, 'KAZIRANGA TO GUWAHATI | SUNSET CRUISE ON THE MIGHTY RIVER', ('Morning tea plantation nature walk then return to Guwahati ultra-luxury hotel. Spectacular sunset cruise with fine local teas, appetizers, and live acoustic regional music.'), [
                'Sightseeing Included: Guwahati Riverside Highway, Premium Brahmaputra Sunset Cruise.',
                'Evening Experience: Live folk music and cultural showcase on-board.',
                'Overnight Stay: Luxury Hotel in Guwahati.',
                'Meals Included: Breakfast & Gourmet Dinner.',
            ]),
            _day(5, 'GUWAHATI EXPLORATION | SACRED SHRINES & GOLDEN SILK EXPEDITIONS', ('Priority VIP Kamakhya Temple visit, private speed-boat to Umananda Temple, and silk emporium hand-weaving of Assam Muga Silk with premium orthodox high tea.'), [
                'Sightseeing Included: Kamakhya Temple (VIP Entry), Umananda River Island, Silk Weaving Centers.',
                'Local Experience: High tea featuring handpicked single-estate Premium Assam Orthodox Tea.',
                'Overnight Stay: Luxury Hotel in Guwahati.',
                'Meals Included: Breakfast & Grand Farewell Dinner.',
            ]),
            _day(6, 'DEPARTURE | MEMORIES OF THE WILD VALLEY', ('Final gourmet terrace breakfast and private chauffeur transfer to Guwahati International Airport with tea blends and fine silks collected along the way.'), [
                'Sightseeing Included: Airport Transit Route.',
                'Meals Included: Luxury Buffet Breakfast.',
            ])
        ],
        hotels=[
            _hotel('Infinity Oak Forest Resort / Borgos | Kiranshree Grand / Grand Majesty', 'Kaziranga (3 Nights) / Guwahati (2 Nights)', '05 Nights', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner (MAP)', 4, 1, description='OPTION 01 – DELUXE: Infinity Oak Forest Resort / Borgos (Kaziranga, 3N) | Kiranshree Grand / Grand Majesty (Guwahati, 2N) | Breakfast & Dinner (MAP)'),
            _hotel('Diphlu River Lodge (Standard) | Novotel Guwahati GS Road', 'Kaziranga (3 Nights) / Guwahati (2 Nights)', '05 Nights', 'Premium', 'Standard Cottage', 'Breakfast & Dinner (MAP)', 4, 2, description='OPTION 02 – PREMIUM: Diphlu River Lodge Standard (Kaziranga, 3N) | Novotel Guwahati GS Road (Guwahati, 2N) | Breakfast & Dinner (MAP)'),
            _hotel('The Iora Retreat / Diphlu River Luxury Cabin | Radisson Blu Hotel Guwahati', 'Kaziranga (3 Nights) / Guwahati (2 Nights)', '05 Nights', 'Luxury', 'Luxury Cabin', 'Gourmet Wilderness MAP', 5, 3, description='OPTION 03 – LUXURY: Iora Retreat / Diphlu River Luxury Cabin (Kaziranga, 3N) | Radisson Blu (Guwahati, 2N) | Gourmet Wilderness MAP'),
            _hotel('Bespoke Luxury Glamping Safari Tents | Vivanta Guwahati (Taj Group)', 'Kaziranga (3 Nights) / Guwahati (2 Nights)', '05 Nights', 'Ultra Luxury', 'Luxury Glamping Tent', 'Signature Full Board Plan', 5, 4, description='OPTION 04 – ULTRA LUXURY: Bespoke Luxury Glamping Safari Tents (Kaziranga, 3N) | Vivanta Guwahati Taj Group (Guwahati, 2N) | Signature Full Board Plan')
        ],
        inclusions=[
            _inc_included('Bespoke Accommodations: Five nights at handpicked elite jungle resorts and luxury city hotels.', 1),
            _inc_included('Luxury Fleet Transport: Complete itinerary via private 4x4 SUV with toll fees, parking, and driver logistics.', 2),
            _inc_included('Wilderness Dinings: 05 multi-cuisine breakfasts and 05 chef-curated premium dinners.', 3),
            _inc_included('TRAGUIN Support & Assistance: On-ground tracking coordinators and 24/7 dedicated telephone support.', 4),
            _inc_included('Curated Adventure Assets: Private river rafting outfit rentals, professional guides, life jackets, and sand-island picnic.', 5),
            _inc_included('Exclusive Privileges: VIP Kamakhya Temple assistance and private boat access to Umananda Island.', 6),
            _inc_included('Welcome Amenities: Welcome drinks on arrival, traditional stoles, and complimentary Assam tea sample packs.', 7),
            _inc_excluded('Air / Train Tickets: Inbound and outbound domestic or international travel tickets to Guwahati.', 8),
            _inc_excluded('Entry Tickets: Camera fees and individual monument tickets not specified in the itinerary.', 9),
            _inc_excluded('Personal Discretionary Expenses: Premium room service, laundry services, and telephone charges.', 10),
            _inc_excluded('Insurance Coverage: Medical insurance or personal travel protection plans.', 11),
            _inc_excluded('Optional Tours: Optional excursions or activities not listed in the day-by-day plan.', 12)
        ],
    )
    return package, itinerary


def build_as_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AS-013'
    tour_code = 'TRG-ASM-2026-V1'
    title = 'TRAGUIN Premium Assam Family Tour Package — Guwahati • Kaziranga • Majuli • Jorhat'
    duration = '06 Nights / 07 Days'
    slug = 'as-013-guwahati-kaziranga-majuli-jorhat-family'
    itin_slug = 'as-013-guwahati-kaziranga-majuli-jorhat-family-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph('Serial code AS-013 | TRAGUIN tour code TRG-ASM-2026-V1', 1),
            _ph('State / Country: Assam, India | Category: Premium Family Tour', 2),
            _ph('Destinations: Guwahati • Kaziranga National Park • Majuli Island • Jorhat', 3),
            _ph('Ideal for: Families, Nature Enthusiasts, Wildlife Photographers', 4),
            _ph('Best season: November to April', 5),
            _ph('Starting price: On Request (Premium Customized)', 6),
            _ph('Vehicle: Premium air-conditioned luxury SUV with dedicated chauffeur-guide | Meal Plan: Daily breakfast and dinner', 7),
            _ph('Route Plan: Guwahati (1N) ➔ Kaziranga (2N) ➔ Majuli (2N) ➔ Jorhat (1N) ➔ Guwahati Departure', 8),
            _ph('TRAGUIN Signature Experience: Private hands-on masterclass with national award-winning mask makers at Samaguri Satra.', 9),
            _ph('Curated by TRAGUIN Experts: Every route and hotel personally inspected by regional specialists.', 10),
            _ph('Luxury Transportation: High-end sanitised vehicles with professional well-trained drivers.', 11),
            _ph('Shopping: Muga and Pat silks, Second Flush orthodox tea from Jorhat, Majuli masks and bamboo crafts.', 12),
            _ph('Important Notes: Kaziranga safaris Nov 1–Apr 30; book heritage properties 60-90 days ahead; carry valid photo ID.', 13),
        ],
        moods=['Family', 'Luxury', 'Nature', 'Cultural'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Customized)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Guwahati • Kaziranga • Majuli • Jorhat • 06 Nights / 07 Days',
        overview=(
            'Bespoke luxury Assam family tour through breathtaking landscapes, rare wildlife, and rich cultural heritage from sacred shrines to Kaziranga grasslands.\n\nTOUR OVERVIEW\\nWildlife adventure, spiritual exploration, and cultural immersion with VIP access, expert local insights, and round-the-clock personalized TRAGUIN assistance.\n\nWHY CHOOSE A LUXURY ASSAM FAMILY TOUR?\\nKamakhya Temple, Jorhat tea estates, Majuli river island Satras, Kaziranga UNESCO rhino safaris, and Brahmaputra sunset cruises November to April.'
        ),
        seo_title='AS-013 | Guwahati Kaziranga Majuli Jorhat Family | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Assam family package (AS-013 / TRG-ASM-2026-V1): Brahmaputra cruise, Kaziranga safaris, Majuli Satras, Jorhat tea bungalow, 4-tier hotels.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Guwahati arrival and Alfresco Grand sunset cruise Day 01', 1),
            _ih('VIP Kamakhya darshan and scenic drive to Kaziranga Day 02', 2),
            _ih('Central and Western Range jeep safaris and Orchid Park Day 03', 3),
            _ih('Private ferry to Majuli Island cultural adventure Day 04', 4),
            _ih('Majuli Satras, mask-making, and Mising tribal villages Day 05', 5),
            _ih('Jorhat heritage tea bungalow and tasting session Day 06', 6),
            _ih('Scenic return to Guwahati airport Day 07', 7),
        ],
        days=[
            _day(1, 'ARRIVAL IN GUWAHATI | THE GATEWAY TO THE NORTHEAST & SUNSET RIVER CRUISE', ('Extraordinary family tour begins at Guwahati airport with traditional Assamese welcome. Premium hotel check-in then Alfresco Grand luxury sunset cruise over the Brahmaputra with folk music and local snacks.'), [
                'Sightseeing Included: Brahmaputra Riverfront, Local Heritage Markets.',
                'Evening Experience: Premium Sunset Cruise on Alfresco Grand with cultural performances.',
                'Overnight Stay: Guwahati (Premium Luxury Hotel).',
                'Meals Included: Dinner.',
            ]),
            _day(2, 'GUWAHATI SPIRITUAL SOJOURN | KAMAKHYA TEMPLE TO KAZIRANGA NATIONAL PARK', ('Early VIP Kamakhya Temple darshan atop Nilachal Hills with panoramic Brahmaputra views. Lavish breakfast, checkout, and scenic drive through paddy fields to Kaziranga luxury wildlife resort.'), [
                'Sightseeing Included: Kamakhya Temple VIP Darshan, Scenic Highway Viewpoints.',
                'Optional Activities: Nature walk around resort boundaries, traditional bonfire.',
                'Overnight Stay: Kaziranga National Park (Luxury Wildlife Resort).',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(3, 'KAZIRANGA WILDLIFE ADVENTURE | JEEP SAFARIS & ORCHID PARK EXPLORATION', ('Morning Central Range jeep safari for One-horned Rhinoceros. Orchid and Cultural Park with 500+ orchid species and Bihu dance pavilion. Afternoon Western Range sunset jeep safari.'), [
                'Sightseeing Included: Central Range Jeep Safari, Western Range Jeep Safari, Orchid Park.',
                'Evening Experience: Assamese Bihu and local tribal dance performances at the Orchid Park.',
                'Overnight Stay: Kaziranga National Park (Luxury Wildlife Resort).',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(4, 'KAZIRANGA TO MAJULI ISLAND | CRUISE ON THE MIGHTY BRAHMAPUTRA', ('Drive to Nimati Ghat and private TRAGUIN ferry across the Brahmaputra to Majuli Island. Check in to luxury eco-resort blending rustic tribal architecture with premium amenities.'), [
                'Sightseeing Included: Private River Ferry Cruise, Rural Majuli Landscapes.',
                'Photography Points: Brahmaputra riverbed and traditional Mising tribal houses.',
                'Overnight Stay: Majuli Island (Premium Luxury Eco-Resort).',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(5, 'MAJULI CULTURAL IMMERSION | MONASTIC SATRAS & MASK-MAKING ARTISTRY', ('Visit Auniati Satra artifacts collection and Samaguri Satra mask-making with hands-on master craftsman demonstration. Mising tribal village stilt houses and handloom weaving. Majuli wetland sunset.'), [
                'Sightseeing Included: Auniati Satra, Samaguri Satra (Mask-making), Mising Tribal Village.',
                'Local Experiences: Private interaction with master mask-makers and local tribal weavers.',
                'Overnight Stay: Majuli Island (Premium Luxury Eco-Resort).',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(6, 'MAJULI TO JORHAT | HERITAGE TEA BUNGALOW EXPERIENCE', ('Return ferry to Nimati Ghat and short drive to Jorhat Tea Capital. Check into restored British tea bungalow with exclusive tea-tasting session and estate walk.'), [
                'Sightseeing Included: Jorhat Tea Research Association Outskirts, Historic Tea Gardens.',
                'Exclusive Experiences: Curated tea tasting and educational walk through working tea estate.',
                'Overnight Stay: Jorhat (Luxury Heritage Tea Bungalow).',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(7, 'JORHAT TO GUWAHATI | DEPARTURE WITH UNFORGETTABLE MEMORIES', ('Final breakfast on heritage bungalow veranda with estate views. Scenic highway to Guwahati airport with premium tea packets and handloom textile souvenirs.'), [
                'Sightseeing Included: En-route Highway Souvenir Shopping.',
                'Transfers: Private transfer to Guwahati Airport (GAU).',
                'Meals Included: Breakfast.',
            ])
        ],
        hotels=[
            _hotel('Vivanta Guwahati (Superior Room) | Infinity Resorts (Deluxe Cottage) | La Maison de Ananda (Eco Cottage) | Kaziranga Golf Resort (Executive Room)', 'Guwahati (1 Night) / Kaziranga (2 Nights) / Majuli Island (2 Nights) / Jorhat (1 Night)', '06 Nights', 'Deluxe', 'Superior / Deluxe / Eco Cottage / Executive', 'Breakfast & Dinner', 4, 1, description='OPTION 01 – DELUXE: Vivanta Guwahati Superior (Guwahati, 1N) | Infinity Resorts Deluxe Cottage (Kaziranga, 2N) | La Maison de Ananda Eco Cottage (Majuli, 2N) | Kaziranga Golf Resort Executive (Jorhat, 1N)'),
            _hotel('Radisson Blu Guwahati (Deluxe Room) | Borgos Resort (Executive Room) | Majuli Heritage Lodge (Premium Cabin) | The anya - Luxury Tea Resort', 'Guwahati (1 Night) / Kaziranga (2 Nights) / Majuli Island (2 Nights) / Jorhat (1 Night)', '06 Nights', 'Premium', 'Deluxe / Executive / Premium Cabin', 'Breakfast & Dinner', 4, 2, description='OPTION 02 – PREMIUM: Radisson Blu Deluxe (Guwahati, 1N) | Borgos Executive (Kaziranga, 2N) | Majuli Heritage Lodge Premium Cabin (Majuli, 2N) | The anya Luxury Tea Resort (Jorhat, 1N)'),
            _hotel('Taj Vivanta (Premium Suite) | Diphlu River Lodge (Luxury Cottage) | Prashanti Eco-Tourism Lodge (VVIP Suite) | Burra Sahib Bungalow (Heritage Suite)', 'Guwahati (1 Night) / Kaziranga (2 Nights) / Majuli Island (2 Nights) / Jorhat (1 Night)', '06 Nights', 'Luxury', 'Premium Suite / Luxury Cottage / VVIP Suite / Heritage Suite', 'Breakfast & Dinner', 5, 3, description='OPTION 03 – LUXURY: Taj Vivanta Premium Suite (Guwahati, 1N) | Diphlu River Lodge Luxury Cottage (Kaziranga, 2N) | Prashanti Eco-Tourism VVIP Suite (Majuli, 2N) | Burra Sahib Bungalow Heritage Suite (Jorhat, 1N)'),
            _hotel('The Gateway Hotel VIP Block | Diphlu River Lodge (Presidential Suite) | TRAGUIN Private Luxury Camp Setups | Thengal Manor Heritage (Royal Suite)', 'Guwahati (1 Night) / Kaziranga (2 Nights) / Majuli Island (2 Nights) / Jorhat (1 Night)', '06 Nights', 'Ultra Luxury', 'VIP Block / Presidential Suite / Luxury Camp / Royal Suite', 'Breakfast & Dinner', 5, 4, description='OPTION 04 – ULTRA LUXURY: Gateway Hotel VIP Block (Guwahati, 1N) | Diphlu River Lodge Presidential Suite (Kaziranga, 2N) | TRAGUIN Private Luxury Camp (Majuli, 2N) | Thengal Manor Royal Suite (Jorhat, 1N)')
        ],
        inclusions=[
            _inc_included('Premium Accommodation: 06 Nights stay at selected handpicked luxury hotels and heritage bungalows.', 1),
            _inc_included('Curated Meal Plan: Daily buffet breakfast and chef-crafted dinners at all properties.', 2),
            _inc_included('Private Luxury Transfers: All transfers, inter-city drives, and sightseeing in an executive SUV.', 3),
            _inc_included('Exclusive Sightseeing: Entry permissions for Kamakhya VIP Darshan, Kaziranga Jeep Safaris, and Majuli Satras.', 4),
            _inc_included('Brahmaputra River Experiences: Premium Sunset Cruise in Guwahati and private ferry transfers to Majuli.', 5),
            _inc_included('Welcome Amenities: Traditional Assamese Gamosa welcome and complimentary luxury refreshments basket on arrival.', 6),
            _inc_included('TRAGUIN Support: 24/7 dedicated concierge assistance from a senior operations manager.', 7),
            _inc_included('All Taxes: All standard luxury hospitality taxes, toll charges, parking fees, and driver allowances included.', 8),
            _inc_excluded('Airfare / Train Tickets: Round-trip flights or rail tickets to Guwahati are not included.', 9),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, premium alcoholic beverages, and room service.', 10),
            _inc_excluded('Optional Tours: Extra activities not explicitly detailed in the day-wise itinerary.', 11),
            _inc_excluded('Camera Fees: Professional video camera or DSLR lens fees inside Kaziranga National Park.', 12),
            _inc_excluded('Travel Insurance: Personal comprehensive medical and travel insurance.', 13)
        ],
    )
    return package, itinerary


ASSAM_DOMESTIC_BUILDERS = [
    build_as_004,
    build_as_005,
    build_as_006,
    build_as_007,
    build_as_008,
    build_as_009,
    build_as_010,
    build_as_011,
    build_as_012,
    build_as_013,
]

