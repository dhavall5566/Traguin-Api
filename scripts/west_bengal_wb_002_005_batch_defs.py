"""Builder functions for WB-002 through WB-005 West Bengal domestic packages."""

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


def build_wb_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-002'
    tour_code = 'TRG-EZ-WB002'
    title = 'HIMALAYAN MAJESTY • DARJEELING & GANGTOK FAMILY ESCAPE'
    duration = '05 Nights / 06 Days'
    slug = 'wb-002-himalayan-majesty-darjeeling-gangtok-family-escape'
    itin_slug = 'wb-002-himalayan-majesty-darjeeling-gangtok-family-escape-itinerary'
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
            _ph('Serial code WB-002 | TRAGUIN tour code TRG-EZ-WB002', 1),
            _ph('State / Country: West Bengal / India | Category: Premium Family Tour', 2),
            _ph('Destinations: Darjeeling •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury SUV (Innova/Xylo) / Premium MAPAI', 7),
            _ph('TRAGUIN Signature Experience: Private family briefing and historical tea lineage walk inside a premier', 8),
            _ph('Curated by TRAGUIN Experts: Flawlessly managed inner-line permits for Sikkim border regions without', 9),
            _ph('Premium Handpicked Hotels: Properties chosen specifically for premium valley views and stellar family', 10),
            _ph('Luxury Transportation: Expert hill drivers background-verified for supreme safety across winding curves.', 11)
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
        tagline='HIMALAYAN MAJESTY',
        overview="HIMALAYAN MAJESTY • DARJEELING & GANGTOK FAMILY ESCAPE Welcome to a majestic high-altitude holiday designed exclusively by TRAGUIN. Embark on the finest West Bengal Family Tour combined with the mystical allure of Sikkim, curated perfectly to show you the breathtaking landscapes, sprawling emerald tea gardens, and snow-clad Himalayan peaks. As your elite travel consultants, TRAGUIN elevates your journey into a seamless luxury holiday packed with premium stays, handpicked hotels, and emotionally rich storytelling. From watching the golden sunrise melt over Mt. Kanchenjunga in Darjeeling to exploring the serene monasteries and high lakes of Gangtok, every single moment is destined to craft unforgettable memories for you and your family.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers an exquisite balance between legendary colonial charm and mystical Buddhist heritage. Travelling in a completely private premium AC SUV with a skilled mountain chauffeur, your family will experience flawless transitions through the hills. Featuring a meticulously planned meal layout (MAPAI - breakfast and dinner) at top-tier properties, your route represents the definitive premium West Bengal experience. Every single portion of your journey features the signature touch of TRAGUIN curated experiences, assuring personalized assistance, comfortable high-altitude transitions, and VIP sightseeing parameters.\n\nWHY CHOOSE THE BEST WEST BENGAL TOUR PACKAGE?\nWhen arranging a Luxury West Bengal Holiday, discerning travellers seek a deep immersion into natural beauty and rich cultural heritage. Darjeeling and Gangtok boast some of the most iconic attractions in Eastern India. From the legendary Tiger Hill sunrise and the historic UNESCO World Heritage Darjeeling Himalayan Railway to the high-altitude wonders of Tsomgo Lake, West Bengal sightseeing and Eastern Himalayan trails provide a deeply spiritual, refreshing escape. For couples and families reserving a customized West Bengal Honeymoon Package or West Bengal Family Tour, the region showcases highly popular Instagram locations like the Batasia Loop, Happy Valley Tea Estate, and the colorful streets of Gangtok's MG Marg. Whether you desire local tea tasting, authentic handicraft shopping, or exploring centuries-old monasteries, our TRAGUIN West Bengal Packages promise premium comfort, handpicked hotels, and immersive experiences that align beautifully with the best time to visit West Bengal.",
        seo_title='WB-002 | HIMALAYAN MAJESTY | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days West Bengal package (WB-002 / TRG-EZ-WB002): Darjeeling • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL AT IXB AIRPORT / NJP STATION TO DARJEELING', 1),
            _ih('Day 02: DARJEELING SIGHTSEEING', 2),
            _ih('Day 03: DARJEELING TO GANGTOK', 3),
            _ih('Day 04: TSOMGO LAKE & BABA MANDIR EXCURSION', 4),
            _ih('Day 05: GANGTOK URBAN SIGHTSEEING', 5),
            _ih('Day 06: GANGTOK TO BAGDOGRA / DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private family briefing and historical tea lineage walk inside a premier', 7),
            _ih('Curated by TRAGUIN Experts: Flawlessly managed inner-line permits for Sikkim border regions without', 8),
            _ih('Premium Handpicked Hotels: Properties chosen specifically for premium valley views and stellar family', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL AT IXB AIRPORT / NJP STATION TO DARJEELING',
                (
                    'JOURNEY INTO THE QUEEN OF THE HILLS – TEA GARDEN AMBIANCE Your premium West Bengal experience commences as you land at Bagdogra Airport (IXB) or arrive at New Jalpaiguri Railway Station (NJP). A dedicated private luxury SUV waits to usher you away. Wind upward through scenic routes wrapped in emerald tea fields and mist-covered cedar forests. Arrive in Darjeeling, the historic queen of the hills, and check into your handpicked luxury mountain resort. Spend a relaxed evening exploring the Mall Road or absorbing the old-world colonial charm.'
                ),
                [
                    'Sightseeing Included: Scenic Rohini/Kurseong bypass route, Darjeeling Mall Road stroll.',
                    'Evening Experience: Premium local tea-tasting welcome session arranged by TRAGUIN experts.',
                    'Overnight Stay: Darjeeling (Premium / Luxury Mountain Resort)',
                    'Meals Included: Welcome Mountain Tea & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'DARJEELING SIGHTSEEING',
                (
                    'GOLDEN KANCHENJUNGA SUNRISE & COLONIAL HERITAGE TRAILS Awake at 4:00 AM for a thrilling drive up to Tiger Hill to witness a breathtaking spectacle—the first golden rays of sunrise illuminating the majestic peak of Mt. Kanchenjunga. On your return journey, visit the iconic Batasia Loop and the solemn Ghoom Monastery. Following a lavish breakfast at your resort, explore the Himalayan Mountaineering Institute (HMI), Padmaja Naidu Himalayan Zoological Park, and a popular Instagram location —the sprawling green tea estates for an unforgettable storytelling walk.'
                ),
                [
                    'Sightseeing Included: Tiger Hill Sunrise, Batasia Loop, Ghoom Monastery, HMI, Himalayan Zoo, Tea Gardens.',
                    'Optional Activities: Joyride on the historic Darjeeling Himalayan Toy Train (UNESCO World Heritage).',
                    'Overnight Stay: Darjeeling (Premium / Luxury Mountain Resort)',
                    'Meals Included: Premium Breakfast & Gourmet Dinner',
                ],
            ),
            _day(
                3,
                'DARJEELING TO GANGTOK',
                (
                    "MEANDERING TEESTA RIVER RIDE TO SIKKIM'S ROYAL CAPITAL Depart Darjeeling after a gourmet breakfast and embark on a mesmerizing drive toward Gangtok, the capital of Sikkim. The scenic route runs parallel to the emerald waters of the Teesta River, presenting dramatic mountain gorges and breathtaking landscapes. Cross the Rangpo border with pre-arranged seamless permits and ascend to Gangtok. Check into your ultra-luxury resort and spend your evening walking down the immaculate, pedestrian-only MG Marg, ideal for elite cafe hopping."
                ),
                [
                    'Sightseeing Included: Teesta River Viewpoints, Triveni Confluence point photography, MG Marg Promenade.',
                    'Evening Experience: Reserved outdoor seating at a premium boutique cafe on MG Marg.',
                    'Overnight Stay: Gangtok (Premium Luxury Spa Resort)',
                    'Meals Included: Premium Breakfast & Traditional Sikkimese Dinner',
                ],
            ),
            _day(
                4,
                'TSOMGO LAKE & BABA MANDIR EXCURSION',
                (
                    'HIGH-ALTITUDE SACRED GLACIER LAKE & EPIC BORDER LANDSCAPES Enjoy an early breakfast before venturing on a spectacular high-altitude mountain drive to Tsomgo Lake, situated at a breathtaking 12,400 feet. This sacred glacial lake mirrors the surrounding jagged snow peaks with crystalline clarity. Continue further to the legendary Baba Harbhajan Singh Mandir, an emotionally moving shrine built in honor of a brave soldier. Absorb the dramatic, raw altitude views and snapshot amazing alpine family photographs.'
                ),
                [
                    'Sightseeing Included: Tsomgo Lake, Baba Harbhajan Singh Memorial Shrine.',
                    'Optional Activities: Nathu La Pass Indo-China Border excursion (subject to permit availability).',
                    'Overnight Stay: Gangtok (Premium Luxury Spa Resort)',
                    "Meals Included: Premium Breakfast & Elegant Chef's Dinner",
                ],
            ),
            _day(
                5,
                'GANGTOK URBAN SIGHTSEEING',
                (
                    'BUDDHIST MONASTIC PEACE & TROPICAL FLORA TRAILS Spend a beautiful day diving into the artistic and immersive experiences of Gangtok. Visit the stunning Rumtek Monastery, a global seat of Tibetan Buddhism. Witness rare, exotic orchids at the Flower Exhibition Centre and experience a panoramic birds-eye perspective of the city via the Gangtok Ropeway ride. Conclude your day with a deep visit to the Do Drul Chorten Stupa and Namgyal Institute of Tibetology.'
                ),
                [
                    'Sightseeing Included: Rumtek Monastery, Flower Show, Gangtok Ropeway, Do Drul Chorten, Tashi Viewpoint.',
                    'Evening Experience: Farewell premium dining experience celebrating traditional flavors of the Northeast.',
                    'Overnight Stay: Gangtok (Premium Luxury Spa Resort)',
                    'Meals Included: Premium Breakfast & Gala Dinner',
                ],
            ),
            _day(
                6,
                'GANGTOK TO BAGDOGRA / DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Indulge in a final lavish breakfast looking out over the mountain valley. Step back into your private luxury vehicle as your chauffeur guides you back down along the scenic foothills to Bagdogra Airport (IXB) or NJP Railway Station for your onward journey. Return home with your family carrying a treasure trove of sweet bonds and unforgettable memories planned perfectly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private door-to-door mountain highway drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Summit Hermon Resort / similar | Summit Golden Crescent / similar | Dinner)',
                'Multi-city West Bengal',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast &',
                4,
                1,
                description='OPTION 01 – DELUXE: Summit Hermon Resort / similar | Summit Golden Crescent / similar | Dinner)',
            ),
            _hotel(
                'Ramada by Wyndham / Elgin | Lemon Tree Premier / The | Dinner)',
                'Multi-city West Bengal',
                '5N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast &',
                4,
                2,
                description='OPTION 02 – PREMIUM: Ramada by Wyndham / Elgin | Lemon Tree Premier / The | Dinner)',
            ),
            _hotel(
                'The Elgin Darjeeling / Windamere Hotel | The Elgin Nor-Khill / Mayfair Spa Resort',
                'Multi-city West Bengal',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Luxury MAPAI',
                4,
                3,
                description='OPTION 03 – LUXURY: The Elgin Darjeeling / Windamere Hotel | The Elgin Nor-Khill / Mayfair Spa Resort',
            ),
            _hotel(
                'JW Marriott Gangtok | Resort & Spa',
                'Multi-city West Bengal',
                '5N',
                'Ultra Luxury',
                '(Executive Suite)',
                'MAPAI Layout',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: JW Marriott Gangtok | Resort & Spa',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury accommodations at handpicked hotels.', 1),
            _inc_included('Luxury Transportation: Private dedicated SUV for all hill transfers & sightseeing.', 2),
            _inc_included('Curated Meals: Lavish daily breakfast and specialty gourmet dinner spreads.', 3),
            _inc_included('TRAGUIN Support: 24/7 personalized concierge and inner-line permit assistance.', 4),
            _inc_included('Welcome Amenities: Himalayan customized travel kit and refreshments upon entry.', 5),
            _inc_included('Complimentary Experience: Premium tea tasting session at Darjeeling.', 6),
            _inc_excluded('Airfare, flight routing, or main train ticketing costs.', 7),
            _inc_excluded('Nathu La Pass permit costs and special vehicle entry supplements.', 8),
            _inc_excluded('Monument entry fees, joyride tickets, or local porter tips.', 9),
            _inc_excluded('Personal expenses such as laundry, liquor, and optional activities.', 10),
        ],
    )
    return package, itinerary

def build_wb_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-003'
    tour_code = 'TRG-WB-SUNDAR-003'
    title = 'SUNDARBANS ADVENTURE • INTO THE REALM OF THE ROYAL BENGAL TIGER'
    duration = '03 Nights / 04 Days'
    slug = 'wb-003-sundarbans-adventure-into-the-realm-of-the-royal-bengal-tiger'
    itin_slug = 'wb-003-sundarbans-adventure-into-the-realm-of-the-royal-bengal-tiger-itinerary'
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
            _ph('Serial code WB-003 | TRAGUIN tour code TRG-WB-SUNDAR-003', 1),
            _ph('State / Country: West Bengal / India | Category: Wildlife Luxury Adventure', 2),
            _ph('Destinations: Kolkata • Gadkhali • Sajnekhali • Sudhanyakhali • Dobanki • Pirkhali', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Luxury Chauffeur Sedan & Exclusive Private Motorized Cruise Boat', 7),
            _ph('TRAGUIN Signature Experience: Private deck-top tea tasting session featuring premium Darjeeling', 8),
            _ph('Curated by TRAGUIN Experts: Custom navigation paths timed to match low tides for the absolute best', 9),
            _ph('Personalized Assistance: An accompanying government-certified elite wildlife naturalist for private', 10)
        ],
        moods=['Luxury', 'Culture', 'Wildlife'],
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
        tagline='SUNDARBANS ADVENTURE',
        overview="SUNDARBANS ADVENTURE • INTO THE REALM OF THE ROYAL BENGAL TIGER Welcome to a pristine natural wonderland curated meticulously by the destination experts at TRAGUIN. Embark on the definitive West Bengal Tour Package into the world's largest mangrove forest ecosystem. This immersive wild safari is designed to uncover the breathtaking landscapes, hidden waterways, and magnificent wildlife of the legendary Sundarbans. As your dedicated travel consultants, TRAGUIN transforms this ecosystem expedition into a seamless luxury holiday, matching untamed wilderness with premium stays and exclusive experiences. Prepare for unforgettable memories as we trace the footprints of the Royal Bengal Tiger.\n\nTOUR OVERVIEW\nThis elite wildlife holiday itinerary offers a perfect blend of high-end metropolitan comfort and raw, thrilling mangrove exploration. Travelling from Kolkata via private luxury transportation, you will step aboard an exclusive private cruise boat engineered for smooth navigation through twisting saltwater rivers. Featuring a curated meal plan packed with gourmet local delicacies and fresh river catches, this route guarantees the ultimate West Bengal experience. Every segment includes signature TRAGUIN curated experiences, providing private naturalists, VIP forest clearances, and bespoke client service.\n\nWHY CHOOSE THE BEST WEST BENGAL TOUR PACKAGE?\nWhen considering a high-end Luxury West Bengal Holiday, sophisticated adventurers seek a profound connection with nature without sacrificing modern conveniences. The Sundarbans National Park is an internationally celebrated UNESCO World Heritage Site and remains one of the top tourist places in West Bengal for photography, eco-tourism, and birdwatching. Tracing the legendary mangrove labyrinths provides travelers with most searched experiences like spotting the swimming Royal Bengal Tiger, estuarine crocodiles, and rare Irrawaddy dolphins. For couples seeking a distinct, rustic West Bengal Honeymoon Package or families booking an educational West Bengal Family Tour, this region reveals iconic attractions and spectacular Instagram locations, from the mist-covered watchtowers of Dobanki to traditional cultural villages. Whether you are shopping for pure mangrove honey, savoring fresh coastal cuisine, or immersing yourself in local folklore, our exclusive TRAGUIN West Bengal Packages promise handpicked hotels, immersive experiences, and the premium quality required for the best time to visit West Bengal.",
        seo_title='WB-003 | SUNDARBANS ADVENTURE | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days West Bengal package (WB-003 / TRG-WB-SUNDAR-003): Kolkata • Gadkhali • Sajnekhali • Sudhanyakhali • Dobanki • Pirkhali with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: KOLKATA TO GADKHALI JETTY & SUNDARBANS', 1),
            _ih('Day 02: DEEP FOREST CRUISE & ICONIC WATCHTOWERS', 2),
            _ih('Day 03: DOBANKI CANOPY WALK & ADVENTURE SAFARI', 3),
            _ih('Day 04: SUNDARBANS TO KOLKATA / DEPARTURE', 4),
            _ih('TRAGUIN  Signature  Experience: Private  deck-top  tea  tasting  session  featuring  premium  Darjeeling', 5),
            _ih('Curated by TRAGUIN Experts: Custom navigation paths timed to match low tides for the absolute best', 6),
            _ih('Personalized  Assistance: An  accompanying  government-certified  elite  wildlife  naturalist  for  private', 7)
        ],
        days=[
            _day(
                1,
                'KOLKATA TO GADKHALI JETTY & SUNDARBANS',
                (
                    'GATEWAY TO THE MANGROVES – CRUISE INTO SERENITY Your premium West Bengal experience begins with an early morning private luxury pickup from your Kolkata residence or airport. Travel along scenic rural routes through classic Bengal hamlets to reach Gadkhali Jetty. Here, step aboard your private luxury motorized cruise vessel. As you sail into the delta, enjoy a freshly prepared welcome lunch on deck. Drift past breathtaking landscapes where the freshwater streams meet the roaring sea, arriving at your premium handpicked eco-luxury resort in time for a traditional village walk. experts.'
                ),
                [
                    'Sightseeing Included: Gadkhali delta rim, Pakhiralay bird nesting island, local eco-village walk.',
                    'Optional Activities: Guided photography walk along the earthen dikes during golden hour sunset.',
                    "Evening Experience: A traditional 'Bonbibi Yatra' folk theater performance hosted exclusively by TRAGUIN",
                    'Overnight Stay: Sundarbans Delta (Premium Eco-Luxury Resort)',
                    'Meals Included: Welcome Drink, Gourmet Deck Lunch & Traditional Resort Dinner',
                ],
            ),
            _day(
                2,
                'DEEP FOREST CRUISE & ICONIC WATCHTOWERS',
                (
                    'THE REALM OF THE APEX PREDATOR – SAJNEKHALI & SUDHANYAKHALI Awake early to the haunting calls of exotic birds. Today features deep forest Sundarbans sightseeing. Board your luxury boat at dawn for a cruise into the core tiger reserve. Pass through twisting creeks like Pirkhali and Gajikhali, scanning the roots for saltwater crocodiles and spotted deer. Visit the Sajnekhali Watchtower and its nature interpretation center. Continue to the Sudhanyakhali Watchtower, widely recognized as a premier location for spotting the Royal Bengal Tiger drinking from sweet-water ponds. techniques.'
                ),
                [
                    'Sightseeing Included: Sajnekhali Complex, Sudhanyakhali Watchtower, narrow delta mangrove creeks.',
                    'Optional Activities: Private naturalist-guided session focused on pugmark identification and tracking',
                    'Evening Experience: Relaxing starlit deck dining experience featuring local acoustic Baul music.',
                    'Overnight Stay: Sundarbans Delta (Premium Eco-Luxury Resort)',
                    'Meals Included: Jungle Breakfast on Boat, Deck Lunch & Barbecue Dinner',
                ],
            ),
            _day(
                3,
                'DOBANKI CANOPY WALK & ADVENTURE SAFARI',
                (
                    'WALKING ABOVE THE MANGR0VES – HIGHLAND WILDLIFE WATCHING Indulge in breakfast on the water as your private vessel charts a course to the Dobanki Watchtower. This iconic attraction features a half-kilometer-long canopy walk elevated 20 feet above the ground, protected by a secure net canopy. It offers spectacular views of the forest floor, allowing you to observe leopards, axis deer, and wild boars from safety. Spend the afternoon winding through hidden channels, stopping at beautiful Instagram locations before returning to the resort for an evening of luxury leisure.'
                ),
                [
                    'Sightseeing Included: Dobanki Canopy Walkway, Spotted Deer Rehabilitation Center, Panchamukhani junction.',
                    'Optional Activities: Country boat rowing excursion inside shallow, non-motorized silent channels.',
                    'Evening Experience: A romantic candlelit poolside dinner featuring traditional recipes and fresh catches.',
                    'Overnight Stay: Sundarbans Delta (Premium Eco-Luxury Resort)',
                    'Meals Included: Premium Breakfast, Shipboard Lunch & Elegant Farewell Dinner',
                ],
            ),
            _day(
                4,
                'SUNDARBANS TO KOLKATA / DEPARTURE',
                (
                    'RETURN FROM THE WILDERNESS – CHERISHING UNFORGETTABLE MEMORIES Enjoy your final breakfast surrounded by beautiful views at your premium stays. Board your private cruise boat for a final scenic sail back to the Gadkhali Jetty, capturing last-minute photography points along the wide river junctions. Your chauffeured luxury transport vehicle will be waiting to drive you back smoothly to Kolkata Airport or your hotel. Return home carrying unforgettable memories and a deep connection to the wild, crafted with care by TRAGUIN.'
                ),
                [
                    'Transfers Included: Vessel cruise back to Gadkhali Jetty followed by private car transfer to Kolkata.',
                    'Meals Included: Sumptuous Buffet Breakfast & Light On-board Refreshments',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Sunderban Tiger Camp / United 21 Resort / similar',
                'West Bengal',
                '3N',
                'Deluxe',
                'Room Category',
                '(APAI)',
                4,
                1,
                description='OPTION 01 – DELUXE: Sunderban Tiger Camp / United 21 Resort / similar',
            ),
            _hotel(
                'Sundorban Tiger Roar Resort / similar',
                'West Bengal',
                '3N',
                'Premium',
                'Deluxe Room',
                '(APAI)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Sundorban Tiger Roar Resort / similar',
            ),
            _hotel(
                'Jharkhali Eco Resort / WBTDCI',
                'West Bengal',
                '3N',
                'Luxury',
                'Facing Villa',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: Jharkhali Eco Resort / WBTDCI',
            ),
            _hotel(
                'Exclusive Custom Private | Jungle Cruise Houseboat Stay | VVIP Ultra Luxury | Fine Dining Plan',
                'Multi-city West Bengal',
                '3N',
                'Ultra Luxury',
                'Master Stateroom Suite',
                'Bespoke Private Chef',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Exclusive Custom Private | Jungle Cruise Houseboat Stay | VVIP Ultra Luxury | Fine Dining Plan',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 3 Nights accommodation in handpicked eco-resorts.', 1),
            _inc_included('Luxury Transportation: Private AC sedan from Kolkata & dedicated boat cruise.', 2),
            _inc_included('Curated Meal Plan: Full-board elite breakfasts, lunches, and dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated local guest relationship concierge.', 4),
            _inc_included('Welcome Amenities: Native fresh fruit basket, travel kits, and delta map.', 5),
            _inc_included('Complimentary Experience: Exclusive access to private Baul musical evening.', 6),
            _inc_excluded('Flights or rail tickets arriving into/departing from Kolkata.', 7),
            _inc_excluded('Forest entry permits, watchtower tickets, and camera permissions.', 8),
            _inc_excluded('Personal expenses such as laundry, phone calls, premium drinks, or tips.', 9),
            _inc_excluded('Any optional country boat rides or extended city tours.', 10),
        ],
    )
    return package, itinerary

def build_wb_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-004'
    tour_code = 'TRG-WB-004'
    title = 'KOLKATA HERITAGE • COLONIAL GRANDEUR & CULTURAL MAJESTY'
    duration = '03 Nights / 04 Days'
    slug = 'wb-004-kolkata-heritage-colonial-grandeur-cultural-majesty'
    itin_slug = 'wb-004-kolkata-heritage-colonial-grandeur-cultural-majesty-itinerary'
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
            _ph('Serial code WB-004 | TRAGUIN tour code TRG-WB-004', 1),
            _ph('State / Country: West Bengal / India | Category: Heritage Luxury Escape', 2),
            _ph('Destinations: Kolkata (The City of Joy)', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Chauffeur Sedan / CP (Lavish Breakfast)', 7),
            _ph('TRAGUIN Signature Experience: Private curated access to the artisans of Kumartuli with local experts', 8),
            _ph('Curated by TRAGUIN Experts: Custom routing designed to bypass traffic blocks, ensuring optimal', 9),
            _ph('Premium Handpicked Hotels: Properties chosen specifically for their cultural luxury story and elite', 10),
            _ph('Personalized Assistance: Dedicated greeting and smooth handling at all arrival and departure junctions.', 11)
        ],
        moods=['Luxury', 'Culture'],
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
        tagline='KOLKATA HERITAGE',
        overview="KOLKATA HERITAGE • COLONIAL GRANDEUR & CULTURAL MAJESTY Welcome to a timeless journey through the imperial corridors of India's cultural capital, flawlessly designed and curated exclusively by TRAGUIN. Embark on the definitive Kolkata Heritage tour package, structured to immerse you in legendary stories, grand architecture, and soul-stirring artistic legacies. As your premier travel consultants, TRAGUIN transforms this destination into an exquisite premium West Bengal experience, complete with handpicked hotels, elite culinary trails, and unmatched luxury transportation. Prepare for unforgettable memories as you traverse colonial streets and experience the artistic heartbeat of the City of Joy.\n\nTOUR OVERVIEW\nThis elite 03 Nights / 04 Days luxury holiday itinerary balances cultural depth with absolute relaxation. Travel in style in a dedicated premium air-conditioned vehicle under the guidance of a highly professional, well- versed local chauffeur who handles every detail seamlessly. Enjoy a flexible and premium meal plan featuring grand breakfasts at elite dining spaces. Our special TRAGUIN curated experience note ensures private exclusive access to historical monuments, vintage tram car explorations, and an evocative sunset cruise along the historic Hooghly River.\n\nWHY CHOOSE THE BEST WEST BENGAL TOUR PACKAGE?\nWhen exploring options for a Luxury West Bengal Holiday, sophisticated travelers prioritize deep historical immersion paired with elite modern comfort. Kolkata stands proudly as the cultural heart of Eastern India, making a Kolkata Honeymoon Package or a Kolkata Family Tour a deeply romantic and intellectual journey. From iconic attractions like the spectacular Victoria Memorial and the majestic Howrah Bridge to the architectural grandeur of Marble Palace, West Bengal sightseeing is rich with legendary storytelling. Discover highly sought-after, popular Instagram locations such as the vibrant Mallick Ghat Flower Market and the artistic terracotta avenues of Kumartuli. Savor the authentic flavours of legendary high teas at colonial clubs, indulge in exquisite shopping for traditional Baluchari and Jamdani silks, and dive deep into centuries of unmatched art. These iconic landmarks make anytime between autumn and winter the absolute best time to visit West Bengal. Our signature TRAGUIN West Bengal Packages merge top tourist places in West Bengal with the finest curated experiences to elevate your journey.",
        seo_title='WB-004 | KOLKATA HERITAGE | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days West Bengal package (WB-004 / TRG-WB-004): Kolkata (The City of Joy) with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN KOLKATA', 1),
            _ih('Day 02: IMPERIAL IMPRESSIONS & RIVERSIDE SUNSET', 2),
            _ih('Day 03: SOUL OF THE NORTH – ART, CLAY & LITERATURE', 3),
            _ih('Day 04: SPIRITUAL ESCAPE & DEPARTURE', 4),
            _ih('TRAGUIN Signature Experience: Private curated access to the artisans of Kumartuli with local experts', 5),
            _ih('Curated by TRAGUIN Experts: Custom routing designed to bypass traffic blocks, ensuring optimal', 6),
            _ih('Premium Handpicked Hotels: Properties chosen specifically for their cultural luxury story and elite', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN KOLKATA',
                (
                    "WELCOME TO THE CITY OF JOY – COLONIAL CHARM & GRAND CHECK-IN Your premium West Bengal experience begins with a grand welcome at Kolkata Airport or Howrah Railway Station. Your private luxury transportation vehicle is ready to chauffeur you smoothly to your handpicked premium luxury heritage hotel. After a refreshing afternoon, step out for an emotional storytelling stroll through the legendary Dalhousie Square (B.B.D. Bagh), admiring majestic structures like the Writers' Building and the General Post Office. Conclude your evening with gourmet artisanal refreshments at a historic colonial café. exteriors."
                ),
                [
                    "Sightseeing Included: Dalhousie Square, St. John’s Church Complex, Writers' Building heritage",
                    'Evening Experience: Traditional high tea and heritage introduction at a legendary club or hotel lounge.',
                    'Overnight Stay: Kolkata (Premium Palace or Luxury Heritage Stay)',
                    'Meals Included: Welcome Mocktail & Gourmet Breakfast (Next Morning)',
                ],
            ),
            _day(
                2,
                'IMPERIAL IMPRESSIONS & RIVERSIDE SUNSET',
                (
                    'VICTORIAN MONUMENTS & THE ROMANTIC HOOGHLY CRUISE Indulge in a lavish buffet breakfast before embarking on a comprehensive West Bengal sightseeing tour. Explore the white marble grandeur of the iconic Victoria Memorial, a breathtaking monument displaying centuries of fascinating history. Photograph the spectacular architecture of St. Paul’s Cathedral. Late in the afternoon, transition to the Princep Ghat for an exclusive experience: a private sunset country-boat cruise on the tranquil Hooghly River, gliding gracefully under the majestic Vidyasagar Setu.'
                ),
                [
                    "Sightseeing Included: Victoria Memorial Hall, St. Paul's Cathedral, Princep Ghat Promenade.",
                    'Optional Activities: A private vintage tram car ride through the leafy lanes of Ballygunge.',
                    'Overnight Stay: Kolkata (Premium Palace or Luxury Heritage Stay)',
                    'Meals Included: Lavish Buffet Breakfast',
                ],
            ),
            _day(
                3,
                'SOUL OF THE NORTH – ART, CLAY & LITERATURE',
                (
                    'KUMARTULI POTTERS, TAGORE HOUSE & THE MAJESTIC HOWRAH BRIDGE Awake early to visit the vibrant, bustling Mallick Ghat Flower Market, a globally famous photography point and a popular Instagram location. Cross the iconic Howrah Bridge to witness the timeless pulse of the city. Later, dive deep into local culture at Kumartuli, where multi-generational clay artisans sculpt breathtaking deities. Pay an emotional visit to Jorasanko Thakurbari, the ancestral home of Nobel Laureate Rabindranath Tagore, before indulging in a premium fine-dining lunch tasting authentic culinary delicacies. Marble Palace. fine classical music.'
                ),
                [
                    'Sightseeing Included: Howrah Bridge, Mallick Ghat, Kumartuli Artisan Enclave, Jorasanko Thakurbari,',
                    'Evening Experience: Farewell dinner at a specialty restaurant curated by TRAGUIN experts, featuring',
                    'Overnight Stay: Kolkata (Premium Palace or Luxury Heritage Stay)',
                    'Meals Included: Lavish Breakfast & Premium Farewell Dinner',
                ],
            ),
            _day(
                4,
                'SPIRITUAL ESCAPE & DEPARTURE',
                (
                    'DAKSHINESWAR, MEMORIES BEYOND DESTINATIONS Savor your final morning breakfast at your premium stay. Before concluding your tour, embark on a spiritual drive to the sacred Dakshineswar Kali Temple along the banks of the river. Wander through the peaceful temple pathways and reflect on your experiences. Afterward, your private luxury transport provides a smooth door-to-door transfer to Kolkata Airport or Railway Station. Return home carrying unforgettable memories designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury terminal drop-off with complete luggage assistance.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Peerless Inn / Kenilworth | Hotel / similar',
                'Multi-city West Bengal',
                '3N',
                'Deluxe',
                'Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: The Peerless Inn / Kenilworth | Hotel / similar',
            ),
            _hotel(
                'The Oberoi Grand (Deluxe Room) | / Itc Sonar',
                'Multi-city West Bengal',
                '3N',
                'Premium',
                'View Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Oberoi Grand (Deluxe Room) | / Itc Sonar',
            ),
            _hotel(
                'The Oberoi Grand (Luxury Room) | / Itc Royal Bengal',
                'Multi-city West Bengal',
                '3N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: The Oberoi Grand (Luxury Room) | / Itc Royal Bengal',
            ),
            _hotel(
                'The Raajkutir An Inseco Heritage | / Taj Bengal Palace',
                'Multi-city West Bengal',
                '3N',
                'Ultra Luxury',
                'Suite',
                'Bespoke Signature',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Raajkutir An Inseco Heritage | / Taj Bengal Palace',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 03 Nights accommodation in handpicked elite hotels.', 1),
            _inc_included('Luxury Transportation: Chauffeur-driven private luxury sedan for all excursions.', 2),
            _inc_included('Meals: Daily lavish multi-cuisine buffet breakfasts at the hotel.', 3),
            _inc_included('TRAGUIN Support: Dedicated 24/7 priority concierge support line.', 4),
            _inc_included('Complimentary Experience: Exclusive private country-boat sunset cruise on the Hooghly.', 5),
            _inc_included('Welcome Amenities: Personalized arrival welcome hamper and sweet box.', 6),
            _inc_excluded('Airfare, domestic flights, or train ticket costs to Kolkata.', 7),
            _inc_excluded('Monument entry fees, camera permits, or local guide tips.', 8),
            _inc_excluded('Personal expenses such as premium liquor, laundry, or phone calls.', 9),
            _inc_excluded('Optional extensions, tram bookings, or activities not listed. s — Kolkata Heritage Escape 5', 10),
        ],
    )
    return package, itinerary

def build_wb_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'WB-005'
    tour_code = 'TRG-WB-005'
    title = 'TARAPITH CIRCUIT • THE DIVINE PATH OF SHAKTI & PEACE'
    duration = '04 Nights / 05 Days'
    slug = 'wb-005-tarapith-circuit-the-divine-path-of-shakti-peace'
    itin_slug = 'wb-005-tarapith-circuit-the-divine-path-of-shakti-peace-itinerary'
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
            _ph('Serial code WB-005 | TRAGUIN tour code TRG-WB-005', 1),
            _ph('State / Country: West Bengal / India | Category: Premium Pilgrimage & Divine Circuit', 2),
            _ph('Destinations: Kolkata • Tarapith •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury AC Innova / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private temple-side pandit assistance for seamless, stress-free holy', 8),
            _ph('Curated by TRAGUIN Experts: Perfect highway logistical coordination ensuring minimal road fatigue for', 9),
            _ph('Premium Handpicked Hotels: Properties chosen specifically for high hygiene parameters and immediate', 10),
            _ph('Exclusive Recommendations: Detailed map guidelines to genuine local sweets and high-grade', 11)
        ],
        moods=['Luxury', 'Spiritual'],
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
        tagline='TARAPITH CIRCUIT',
        overview='TARAPITH CIRCUIT • THE DIVINE PATH OF SHAKTI & PEACE Welcome to a deeply soul-stirring spiritual journey curated exclusively by TRAGUIN. Embark on the finest West Bengal Pilgrimage tour package, masterfully crafted to take you through the historic, mystic, and sacred soil of Bengal. As your elite travel consultants, TRAGUIN ensures your spiritual quest is transformed into a seamless luxury holiday filled with premium stays, handpicked hotels, and emotionally moving spiritual encounters. From the intense cosmic energies of Tarapith and Bakreshwar Shaktipitha to the intellectual peace of Shantiniketan, every detail is woven to ensure unforgettable memories for you and your family.\n\nTOUR OVERVIEW\nThis custom-tailored divine tour offers an ideal balance between sacred Shakta traditions, rejuvenating geothermal natural elements, and heritage preservation. Travelling in a dedicated, high-end private AC vehicle with an expert chauffeur-driven assistance team, your family will experience absolute security, privacy, and reverence. With a carefully structured meal plan incorporating exquisite vegetarian or traditional multi-cuisine breakfasts and customized dinners, this circuit represents the pinnacle of a premium West Bengal experience. Every aspect features the trademark TRAGUIN curated experience note, ensuring priority VIP darshans, local pandit storytelling, and seamless logistical execution.\n\nWHY VISIT THE SACRED TARAPITH CIRCUIT?\nWhen exploring options for the Best West Bengal Tour Package, spiritual families look for deep sacred roots combined with contemporary comforts. The Tarapith Circuit stands out as one of the most spiritually powerful regions in Eastern India, making a West Bengal Pilgrimage Package highly sought after. Tarapith is world- renowned for its ancient temple dedicated to Goddess Tara and the legendary mystic saint Bama Khepa. It is an essential component of any West Bengal Family Tour focused on spiritual enrichment and cultural legacy. For travelers wishing to couple divinity with scenic beauty and historical culture, this itinerary covers iconic attractions like the healing hot springs of Bakreshwar and the beautiful ashram layouts of Shantiniketan—a highly popular Instagram location for culture lovers. Whether you are performing sacred rituals, indulging in local traditional sweet shopping, or finding immense inner peace along the Kopai river, our TRAGUIN West Bengal Packages promise absolute luxury, local immersive experiences, and handpicked premium hotels during the best time to visit West Bengal.',
        seo_title='WB-005 | TARAPITH CIRCUIT | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days West Bengal package (WB-005 / TRG-WB-005): Kolkata • Tarapith • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN KOLKATA TO TARAPITH', 1),
            _ih('Day 02: SACRED RITUALS IN TARAPITH & BAMAKHEPA ASHRAM', 2),
            _ih('Day 03: EXCURSION TO BAKRESHWAR SHAKTIPITHA', 3),
            _ih('Day 04: TARAPITH TO SHANTINIKETAN', 4),
            _ih('Day 05: SHANTINIKETAN TO KOLKATA / DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private temple-side pandit assistance for seamless, stress-free holy', 6),
            _ih('Curated by TRAGUIN Experts: Perfect highway logistical coordination ensuring minimal road fatigue for', 7),
            _ih('Premium Handpicked Hotels: Properties chosen specifically for high hygiene parameters and immediate', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN KOLKATA TO TARAPITH',
                (
                    'JOURNEY TO THE LAND OF TANTRA & COSMIC ENERGY Your premium West Bengal experience commences with a VIP pickup at Kolkata Airport or Howrah Railway Station by your designated luxury transport team. Leave the city behind as you embark on a highly scenic drive through the verdant, emerald-green landscapes of rural Bengal. Arrive at the holy town of Tarapith, check into your handpicked premium hotel, and settle into a serene ambiance. In the evening, visit the main Tarapith Temple complex for an introductory darshan and witness the deeply emotional sandhya aarti that fills the air with sacred chants and mystic fervor.'
                ),
                [
                    'Sightseeing Included: Scenic countryside highway route, evening Tarapith Temple complex.',
                    'Evening Experience: VIP Darshan entry and attending the cosmic evening sandhya aarti.',
                    'Overnight Stay: Tarapith (Premium Selected Comfort Hotel)',
                    'Meals Included: Welcome Drink & Luxury Sit-down Dinner',
                ],
            ),
            _day(
                2,
                'SACRED RITUALS IN TARAPITH & BAMAKHEPA ASHRAM',
                (
                    "DIVINE IMMERSION, SACRED TANTRIC GROUNDS & LOCAL FAITH Awake before dawn for an exclusive, deeply spiritual early morning darshan of Maa Tara, where you can witness the sacred bathing ritual. Explore the famous Tarapith Maha Smashan (cremation grounds), an internationally highly-searched tourism keyword site recognized for its profound spiritual and tantric history. Visit the serene Bama Khepa Ashram, dedicated to the revered mad saint who achieved enlightenment here. Spend your afternoon exploring local handloom stores, tasting the local traditional 'bhog' meals, and taking beautiful family photography points pictures near the riverfront. (optional)."
                ),
                [
                    'Sightseeing Included: Maa Tara Main Temple, Maha Smashan, Bama Khepa Ashram, Jibanti Kali Temple',
                    'Optional Activities: Special private puja and homam ritual organized through certified local priests.',
                    'Overnight Stay: Tarapith (Premium Selected Comfort Hotel)',
                    'Meals Included: Premium Breakfast & Satvik Dinner',
                ],
            ),
            _day(
                3,
                'EXCURSION TO BAKRESHWAR SHAKTIPITHA',
                (
                    'NATURAL GEOTHERMAL HOT SPRINGS & MYSTICAL REJUVENATION After a delightful breakfast, embark on a scenic day-excursion to Bakreshwar, another iconic attraction in the West Bengal sightseeing grid. Bakreshwar is immensely famous for two reasons: its sacred Shaktipitha temple where the mind of Goddess Sati fell, and its extraordinary, healing natural geothermal hot springs. Tour the hot springs (Kundas) such as Agni Kunda and Surya Kunda, known to possess rich therapeutic minerals. Spend time meditating amidst the cluster of ancient terracotta Shiva temples that dot the landscape. cluster.'
                ),
                [
                    'Sightseeing Included: Bakreshwar Shaktipitha Temple, Geothermal Mineral Hot Springs, Terracotta Shiva Shrine',
                    'Evening Experience: A peaceful walking tour across the serene temple gardens with private refreshments.',
                    'Overnight Stay: Tarapith / Suri Luxury Property',
                    'Meals Included: Premium Breakfast & Traditional Regional Dinner',
                ],
            ),
            _day(
                4,
                'TARAPITH TO SHANTINIKETAN',
                (
                    'TRANSITION TO THE ABODE OF PEACE & LITERARY HERITAGE Bid adieu to the intense energies of the Shaktipithas as your luxury transportation brings you to Shantiniketan, the world-renowned abode of peace established by Nobel Laureate Rabindranath Tagore. This is a highly popular Instagram location and cultural highpoint. Explore the serene Visva Bharati University campus, the beautiful Uttarayan Complex, and Rabindra Bhavan Museum. Walk through the pristine red-soil pathways of Sonajhuri forest and experience the unforgettable live Baul folk music performances.'
                ),
                [
                    "Sightseeing Included: Uttarayan Complex, Kala Bhavan, Tagore's Ashram, Sonajhuri Haat (Saturday optional).",
                    'Evening Experience: Private musical interaction session with local authentic Baul singer-storytellers.',
                    'Overnight Stay: Shantiniketan (Premium Boutique Luxury Resort)',
                    'Meals Included: Breakfast & Exquisite Bengali Heritage Buffet Dinner',
                ],
            ),
            _day(
                5,
                'SHANTINIKETAN TO KOLKATA / DEPARTURE',
                (
                    'CHERISHING FAITH, CULTURE & DIVINE MEMORIES Indulge in a final gourmet breakfast at your premium boutique resort. Spend your morning hours picking up exquisite local hand-crafted boutique textiles and Dokra art pieces. Later, your private luxury transport vehicle will drive you back comfortably along the national highway to Kolkata Airport or Howrah Railway Station for your return home. Depart with a completely rejuvenated soul and unforgettable memories designed with ultimate perfection by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private door-to-door luxury highway drop-off to Kolkata.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Sonar Bangla / similar | Bishnupur Heritage Stay / similar | Dinner)',
                'Multi-city West Bengal',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast &',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Sonar Bangla / similar | Bishnupur Heritage Stay / similar | Dinner)',
            ),
            _hotel(
                'Hotel Swagatam | International / similar | Mark & Meadows Resort / similar | Dinner)',
                'Multi-city West Bengal',
                '4N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast &',
                4,
                2,
                description='OPTION 02 – PREMIUM: Hotel Swagatam | International / similar | Mark & Meadows Resort / similar | Dinner)',
            ),
            _hotel(
                'The Camellia Heritage Resort / Royal Bengal',
                'West Bengal',
                '4N',
                'Luxury',
                'Premium Suite at Sonar',
                'MAPAI + Custom',
                4,
                3,
                description='OPTION 03 – LUXURY: The Camellia Heritage Resort / Royal Bengal',
            ),
            _hotel(
                'Chhutir Boutique Resort / Basundhara Luxury',
                'West Bengal',
                '4N',
                'Ultra Luxury',
                'Custom VVIP Private Suite',
                'MAPAI Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Chhutir Boutique Resort / Basundhara Luxury',
            )
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Stays in handpicked properties as specified.', 1),
            _inc_included('Luxury Transportation: Private AC Innova Crysta for all transfers & holy sites.', 2),
            _inc_included('Curated Meal Plan: Lavish daily breakfast and customized family dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated local guest relation manager on call.', 4),
            _inc_included('Welcome Amenities: Personalized pilgrimage welcome kit and divine prasadam.', 5),
            _inc_included('Complimentary Experience: Exclusive private Baul folk musical sitting.', 6),
            _inc_excluded('Airfare, flight tickets, or cross-state main train travel.', 7),
            _inc_excluded('Direct donation to temples, personal dakshina to purohits.', 8),
            _inc_excluded('Personal expenses such as laundry, phone calls, or tips.', 9),
            _inc_excluded('Any insurance premium cover or medical diagnostic costs.', 10),
        ],
    )
    return package, itinerary

WEST_BENGAL_WB_002_005_BUILDERS = [
    build_wb_002,
    build_wb_003,
    build_wb_004,
    build_wb_005,
]
