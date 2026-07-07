"""Builder functions for ML-001 through ML-010 Meghalaya domestic packages."""

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

MEGHALAYA_SLUG = "meghalaya"


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


def build_ml_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ML-001'
    tour_code = 'TRG-MEG-001'
    title = 'Shillong Escape — Journey Into the Abode of Clouds'
    duration = '03 Nights / 04 Days'
    slug = 'ml-001-shillong-escape-journey-into-the-abode-of-clouds'
    itin_slug = 'ml-001-shillong-escape-journey-into-the-abode-of-clouds-itinerary'
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
            _ph('Serial code ML-001 | TRAGUIN tour code TRG-MEG-001', 1),
            _ph('State / Country: Meghalaya / India | Category: Premium Family', 2),
            _ph('Destinations: Shillong • Cherrapunji • Elephant Falls • Umiam Lake', 3),
            _ph('Ideal for: Family Getaways, Nature Seekers & Luxury Explorers', 4),
            _ph('Best season: October to May (Pleasant & Clear Sky)', 5),
            _ph('Starting price: On Request (Premium Customized)', 6),
            _ph('Vehicle / Meals: Luxury SUV (Innova Crysta) / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private viewpoints for taking family portraits overlooking Cherrapunji', 8),
            _ph('Curated by TRAGUIN Experts: Smooth routing designed to allow ample relaxation time for children and', 9),
            _ph('Premium Handpicked Hotels: Accommodations chosen strictly based on panoramic hill views, top safety,', 10),
            _ph('Luxury Transportation: Expert drivers well-versed with mountain roads ensuring absolute group comfort.', 11),
            _ph('Weather Notes: Meghalaya can experience unexpected rain showers even during dry seasons. We', 12)
        ],
        moods=['Family', 'Nature', 'Luxury'],
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
        tagline='Shillong Escape — Journey Into the Abode of Clouds',
        overview="SHILLONG ESCAPE • JOURNEY INTO THE ABODE OF CLOUDS Welcome to a magical getaway curated exclusively by TRAGUIN. Embark on the finest Meghalaya Family Tour, meticulously designed to unveil the breathtaking landscapes, dramatic waterfalls, and mist-laden pine hills of Northeast India. As your dedicated travel consultants, TRAGUIN transforms your vacation into a seamless luxury holiday packed with premium stays, immersive experiences, and heartwarming stories. Let the scenic beauty of Umiam Lake and the architectural wonders of Cherrapunji welcome your family, creating sweet, unforgettable memories.\n\nTOUR OVERVIEW\nThis custom-tailored premium luxury holiday itinerary provides an exquisite balance between natural wonders, majestic viewpoints, and relaxing elite comfort. Travelling in a completely private premium AC vehicle with a highly knowledgeable local chauffeur, your family will experience pure privacy. Featuring a premium meal plan with grand daily breakfasts and specialized local/continental dinners, this route represents the definitive premium Meghalaya experience. Every detail comes with the distinct TRAGUIN curated experience note, ensuring prioritized entrance privileges and around-the-clock elite customer care.\n\nWHY CHOOSE THE BEST MEGHALAYA TOUR PACKAGE?\nWhen searching for a Luxury Meghalaya Holiday, families and couples look for untouched landscapes, emerald waters, and pristine hill station life. Shillong, often called the 'Scotland of the East', is the perfect anchor for a Meghalaya Family Tour or a romantic Meghalaya Honeymoon Package. From exploring legendary iconic attractions like the Mawsmai Caves and Elephant Falls to viewing majestic mountain canyon edges, Meghalaya sightseeing offers absolute wonder. This itinerary ensures your family explores popular Instagram locations including the tranquil Umiam Lake and the stunning Seven Sisters Falls in Cherrapunji. Dive deep into local Khasi culture, enjoy authentic pine-side cafes, or look for local artifacts while shopping at Police Bazar. Our signature TRAGUIN Meghalaya Packages combine exclusive experiences with premium handpicked hotels, presenting you the absolute best time to visit Meghalaya with complete ease.",
        seo_title='ML-001 | Shillong Escape — Journey Into the Abode of Clouds | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Meghalaya package (ML-001 / TRG-MEG-001): Shillong • Cherrapunji • Elephant Falls • Umiam Lake with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GUWAHATI TO SHILLONG', 1),
            _ih('Day 02: SHILLONG TO CHERRAPUNJI EXCURSION', 2),
            _ih('Day 03: SHILLONG LOCAL SIGHTSEEING', 3),
            _ih('Day 04: SHILLONG TO GUWAHATI / DEPARTURE', 4),
            _ih('TRAGUIN Signature Experience: Private viewpoints for taking family portraits overlooking Cherrapunji', 5),
            _ih('Curated by TRAGUIN Experts: Smooth routing designed to allow ample relaxation time for children and', 6),
            _ih('Premium Handpicked Hotels: Accommodations chosen strictly based on panoramic hill views, top safety,', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GUWAHATI TO SHILLONG',
                (
                    'WELCOME TO THE SCOTLAND OF THE EAST – SCENIC UMIAM LAKE OVERLOOK Your premium Meghalaya experience begins upon arrival at Guwahati Airport, where your private luxury transport vehicle waits to escort you. Enjoy a smooth uphill drive as the warm plains turn into cool pine forests. Pause for a breathtaking look at Umiam Lake, a massive crystal-blue reservoir surrounded by coniferous hills. This highly popular Instagram location is an exceptional photography point for your first family picture. Arrive in Shillong and check into your handpicked premium luxury stay.'
                ),
                [
                    'Sightseeing Included: Umiam Lake panoramic viewpoint, Pine Forest drive.',
                    'Evening Experience: A relaxed stroll along the lake bank followed by a warm welcoming tea session.',
                    'Overnight Stay: Shillong (Premium Boutique Hotel or Luxury Resort)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'SHILLONG TO CHERRAPUNJI EXCURSION',
                (
                    "THE WETTEST PLACE ON EARTH – THUNDERING WATERFALLS & MYSTICAL CAVES Awake early for a spectacular morning drive down to Cherrapunji (Sohra), famed for its deep gorges and record rainfall. En route, witness the roaring beauty of Elephant Falls, where water cascades down three levels of dark fern-covered rocks. Arrive in Cherrapunji to view the spectacular Nohkalikai Falls, India's tallest plunge waterfall. Explore the ancient limestone passages of Mawsmai Cave, featuring naturally formed stalactites and stalagmites that create an immersive experience for the entire family."
                ),
                [
                    'Sightseeing Included: Elephant Falls, Nohkalikai Falls, Mawsmai Cave, Seven Sisters Falls, Eco Park.',
                    'Optional Activities: A light guided family trek to local canyon views or pristine limestone bridges.',
                    'Overnight Stay: Shillong / Cherrapunji Luxury Resort',
                    'Meals Included: Premium Breakfast & Gourmet Dinner',
                ],
            ),
            _day(
                3,
                'SHILLONG LOCAL SIGHTSEEING',
                (
                    'CULTURE, PANORAMIC PEAKS & VIBRANT MARKETS Dedicate your day to exploring the unique heritage and cultural nuances of Shillong. Drive up to Laitlum Canyons to see the breathtaking, endless green ridges that slope deep into hidden valley amphitheaters. Next, visit the Don Bosco Museum to discover the fascinating tribal lifestyles and history of the Northeast states. Spend your evening at the local markets of Police Bazar, picking up fine woolen clothing and authentic bamboo souvenirs. Lake, Police Bazar. music.'
                ),
                [
                    "Sightseeing Included: Laitlum Canyons, Don Bosco Museum, Shillong Peak (Subject to permissions), Ward's",
                    'Evening Experience: Private dinner at a fine-dining restaurant curated by TRAGUIN experts with live acoustic',
                    'Overnight Stay: Shillong (Premium Boutique Hotel)',
                    'Meals Included: Premium Breakfast & Farewell Dinner',
                ],
            ),
            _day(
                4,
                'SHILLONG TO GUWAHATI / DEPARTURE',
                (
                    'CHERISHING MEMORIES OF THE MISTY HILLS Enjoy your final lavish breakfast looking out over the misty hills of Shillong. Pack your bags as your private luxury transport takes you back along the smooth highway to Guwahati. If time permits, stop at the holy Kamakhya Temple before arriving at Guwahati Airport for your onward flight. Return home carrying a heart full of joy and unforgettable memories crafted seamlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury airport transfer drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Polo Towers / similar | Sohra Plaza / similar',
                'Shillong | Cherrapunji',
                '2N Shillong|1N Cherrapunji',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Polo Towers / similar | Sohra Plaza / similar | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'M crown Hotel / MBL Luxury Stay | Cherrapunji Holiday Resort / similar',
                'Shillong | Cherrapunji',
                '2N Shillong|1N Cherrapunji',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: M crown Hotel / MBL Luxury Stay | Cherrapunji Holiday Resort / similar | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Ri Kynjai Resort / Vivanta Shillong | Polo Orchid Resort (Jasmine Suite)',
                'Shillong | Cherrapunji',
                '2N Shillong|1N Cherrapunji',
                'Luxury',
                'Luxury Lake View | Orchid Suite',
                'MAPAI Plan + Welcome Kit',
                5,
                3,
                description='OPTION 03 – LUXURY: Ri Kynjai Resort / Vivanta Shillong | Polo Orchid Resort (Jasmine Suite) | MAPAI Plan + Welcome Kit',
            ),
            _hotel(
                'Ri Kynjai (Premium Lake View Cottage) | Jiva Resort Cherrapunji (Luxury Suite)',
                'Shillong | Cherrapunji',
                '2N Shillong|1N Cherrapunji',
                'Ultra Luxury',
                'Premium Lake View Cottage | Luxury Suite',
                'Bespoke Signature MAPAI Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Ri Kynjai (Premium Lake View Cottage) | Jiva Resort Cherrapunji (Luxury Suite) | Bespoke Signature MAPAI Plan',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 03 Nights in handpicked properties as per chosen category.', 1),
            _inc_included('Luxury Transportation: Private dedicated Innova Crysta for all transfers and sightseeing.', 2),
            _inc_included('Curated Meal Plan: Daily lavish breakfast and gourmet buffet dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest experience manager on call.', 4),
            _inc_included('Welcome Amenities: Customized family travel kit and fresh local fruit basket.', 5),
            _inc_included('Complimentary Experience: Private family tea and local snack sampling platter.', 6),
            _inc_excluded('Airfare, domestic flight bookings, or train tickets.', 7),
            _inc_excluded('Monument entry tickets, cave entry passes, or camera permits.', 8),
            _inc_excluded('Personal expenses such as laundry, phone calls, drinks, tips.', 9),
            _inc_excluded('Any optional excursions or water sports at Umiam Lake.', 10),
        ],
    )
    return package, itinerary

def build_ml_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ML-002'
    tour_code = 'TRG-MEG-002'
    title = 'Shillong • Cherrapunji • Mawlynnong • Dawki'
    duration = '05 Nights / 06 Days'
    slug = 'ml-002-shillong-cherrapunji-mawlynnong-dawki'
    itin_slug = 'ml-002-shillong-cherrapunji-mawlynnong-dawki-itinerary'
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
            _ph('Serial code ML-002 | TRAGUIN tour code TRG-MEG-002', 1),
            _ph('State / Country: Meghalaya / India | Category: Premium Family Tour', 2),
            _ph('Destinations: Shillong • Cherrapunji • Mawlynnong • Dawki • Jowai', 3),
            _ph('Ideal for: Family Getaways, Nature Lovers, Premium Explorers', 4),
            _ph('Best season: October to May', 5),
            _ph('Starting price: On Request (Bespoke Luxury Pricing)', 6),
            _ph('Vehicle / Meals: Luxury Private SUV / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private family briefing on local Khasi custom rules and heritage prior to', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked travel routes to keep mountain travel smooth, ensuring extra', 9),
            _ph('Premium Handpicked Hotels: Accommodations selected strictly based on premium safety guidelines, superb', 10),
            _ph('Luxury Transportation: Highly experienced mountain drivers with uniform presentation and verified safety', 11),
            _ph("Local Markets & Souvenirs: Explore the vibrant local stalls of Police Bazar to purchase authentic Khasi hand- woven wild silk shawls, bamboo basketry, organic cinnamon sticks, and premium Meghalaya local tea variants. Cafes & Food: Shillong's cozy cafes offer a vibrant live rock-music ambiance. Make sure to try smoked pork dishes, local Jadoh rice delicacies, and gourmet hot chocolate bowls at Old Shillong cafes.", 12)
        ],
        moods=['Family', 'Nature', 'Luxury'],
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
        tagline='Shillong',
        overview="05 NIGHTS / 06 DAYS Welcome to the mesmerizing Abode of Clouds, a majestic realm designed exclusively for your family by TRAGUIN. This hand-tailored Meghalaya Family Tour introduces you to breathtaking landscapes, hidden limestone grottos, and roaring mist-veiled cascades. As your elite destination planners, TRAGUIN transforms your vacation into a Luxury Meghalaya Holiday seamlessly matching elite style with natural awe. From the Scottish vibe of Shillong to the deep, precipitation-rich canyons of Cherrapunji, expect premium stays, handpicked hotels, and immersive experiences that weave together to form unforgettable memories.\n\nTOUR OVERVIEW\nTravel Dates: Flexible / Custom FIT | Group Type: Customized Private Family FIT | Vehicle: Dedicated Luxury Chauffeur-Driven SUV (Innova Crysta) | Meal Plan: Modified American Plan (MAPAI - Lavish Breakfast & Dinner at Premium Stays). Route Outline: Guwahati • Shillong (2N) • Cherrapunji (2N) • Dawki • Mawlynnong • Shillong (1N) • Guwahati Departure. Every mileage of this route is supported by a specialized TRAGUIN curated experience note, promising seamless prioritized routing, handpicked local dining advice, and dedicated professional field assistance to look after your family's dynamic requirements. DISCOVER THE PREMIUM MEGHALAYA EXPERIENCE When shortlisting the absolute Best Meghalaya Tour Package, affluent families look for a fine balance of untouched biological spectacles and high-end hospitality. Meghalaya boasts highly searched, iconic attractions globally celebrated for their natural engineering. From the deep root networks of the living root bridges to the hyper- clear crystal currents of the Umngot River in Dawki, the region provides unique wonders that remain unmatched. For couples and modern households reserving a Meghalaya Honeymoon Package or an expansive family getaway, the land delivers exceptional, popular Instagram locations. Capture jaw-dropping pictures at the edge of Laitlum Canyons, marvel at the drop of Nohkalikai Falls, and walk inside the cleanest eco-village in Asia at Mawlynnong. Whether your goals include hunting for tribal souvenirs, exploring local Khasi culinary secrets, or seeking high-end cave walks, our TRAGUIN Meghalaya Packages guarantee premium handpicked hotels and exclusive experiences during the absolute best time to visit Meghalaya.",
        seo_title='ML-002 | Shillong | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Meghalaya package (ML-002 / TRG-MEG-002): Shillong • Cherrapunji • Mawlynnong • Dawki • Jowai with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL GUWAHATI TO SHILLONG', 1),
            _ih('Day 02: SHILLONG SIGHTSEEING & LAITLUM CANYONS', 2),
            _ih('Day 03: SHILLONG TO CHERRAPUNJI', 3),
            _ih('Day 04: CHERRAPUNJI EXCURSION', 4),
            _ih('Day 05: CHERRAPUNJI TO MAWLYNNONG, DAWKI & BACK TO SHILLONG', 5),
            _ih('Day 06: SHILLONG TO GUWAHATI / DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private family briefing on local Khasi custom rules and heritage prior to', 7),
            _ih('Curated by TRAGUIN Experts: Handpicked travel routes to keep mountain travel smooth, ensuring extra', 8),
            _ih('Premium Handpicked Hotels: Accommodations selected strictly based on premium safety guidelines, superb', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL GUWAHATI TO SHILLONG',
                (
                    'GATEWAY TO THE SCOTLAND OF THE EAST – SCENIC HIGHLAND ARRIVAL Your premium Meghalaya experience takes off as you land at Guwahati Airport, where a clean, air-conditioned private luxury SUV and professional chauffeur stand ready for your family. Leave the plains behind as you climb into winding pine-carpeted hills. Stop along the scenic route to marvel at Umiam Lake, a spectacular blue-water expanse. Arrive in Shillong and check into your handpicked premium stay. Spend your evening taking a relaxed stroll down the colonial lanes of Police Bazar for initial handicraft shopping.'
                ),
                [
                    'Sightseeing Included: Umiam Lake Panoramic Viewpoint, Water Sports Plaza (Optional), Shillong local drive.',
                    'Evening Experience: Bespoke welcome dinner at a curated premium hilltop restaurant showcasing fine fusion dining.',
                    'Overnight Stay: Shillong (Premium Luxury Heritage Property)',
                    'Meals Included: Welcome Drink & Gourmet Curated Dinner',
                ],
            ),
            _day(
                2,
                'SHILLONG SIGHTSEEING & LAITLUM CANYONS',
                (
                    'DRAMATIC CANYON HORIZONS & URBAN CULTURE HILLS Treat your family to a beautiful alpine morning. Today, your destination-specific route leads to the stunning Laitlum Canyons, one of the top tourist places in Meghalaya and a widely popular Instagram location featured for its deep gorges and endless mist curtains. Walk along the edge of the world before heading back to the city to visit the magnificent Don Bosco Museum to uncover rich tribal culture. End your day visiting the delicate Elephant Falls.'
                ),
                [
                    "Sightseeing Included: Laitlum Canyons, Don Bosco Museum of Indigenous Cultures, Elephant Falls, Ward's Lake.",
                    'Photography Points: Ridge of Laitlum Canyons, wooden footbridges of Ward’s Lake.',
                    'Overnight Stay: Shillong (Premium Luxury Boutique Hotel)',
                    'Meals Included: Premium Breakfast & Luxury Buffet Dinner',
                ],
            ),
            _day(
                3,
                'SHILLONG TO CHERRAPUNJI',
                (
                    "THE ROAR OF LUSH VALLEYS & GEOLOGICAL WONDERS Bid adieu to Shillong after a lavish breakfast and venture toward Sohra (Cherrapunji). The highway presents breathtaking landscapes around every bend. Stand in awe before the Mawkdok Dympep Valley Viewpoint. Venture deep into Mawsmai Cave to experience natural limestone passages. Later, witness the sheer majesty of Nohkalikai Falls, India's tallest plunge waterfall, wrapped in rich tribal folklore. Check into an eco-luxury resort built into the cliff-face."
                ),
                [
                    'Sightseeing Included: Mawkdok Dympep Valley, Mawsmai Cave, Nohkalikai Falls, Seven Sisters Falls.',
                    'Optional Activities: Ziplining across the massive canyon depths of Mawkdok Valley for adventure enthusiasts.',
                    'Overnight Stay: Cherrapunji (Bespoke Eco-Luxury Cliffside Resort)',
                    'Meals Included: Premium Breakfast & Luxury Resort Dinner',
                ],
            ),
            _day(
                4,
                'CHERRAPUNJI EXCURSION',
                (
                    'LIVING ROOT BRIDGES & IMMERSIVE RAINFOREST COMFORT Devote your day to exploring Cherrapunji sightseeing at its finest. Take a guided family walk down to an ancient Living Root Bridge, a marvelous structure grown by the Khasi tribe over centuries. For avid trekkers, a custom early morning excursion to the famous Double Decker Root Bridge in Nongriat can be arranged. If you prefer a relaxed pace, enjoy the manicured pathways of Eco Park and sample delicious orange flower honey at local stalls.'
                ),
                [
                    'Sightseeing Included: Single Living Root Bridge access points, Eco Park, Arwah Cave fossil trails.',
                    'Evening Experience: Private family bonfire at your luxury resort accompanied by hot local spiced beverages.',
                    'Overnight Stay: Cherrapunji (Bespoke Eco-Luxury Cliffside Resort)',
                    'Meals Included: Premium Breakfast & Fine Dining Dinner',
                ],
            ),
            _day(
                5,
                'CHERRAPUNJI TO MAWLYNNONG, DAWKI & BACK TO SHILLONG',
                (
                    "THE CRYSTAL WATERS OF DAWKI & CLEANEST PARADISE VILLAGE Set off early for an extraordinary day trip. Arrive at Mawlynnong, celebrated globally as Asia's Cleanest Village. Walk on immaculate, flower-bordered paths and climb the Sky Walk for distant views of Bangladesh. Next, travel to Dawki to witness the jaw-dropping clarity of the Umngot River. Board a private wooden boat where you seem to float in mid-air over a transparent riverbed. Return to Shillong late in the evening following an action-packed day of incredible sightseeing. Complimentary Experience: Private, exclusive family boating tour on the crystal waters of Dawki arranged by TRAGUIN."
                ),
                [
                    'Sightseeing Included: Mawlynnong Village, Dawki Umngot River, Indo-Bangladesh Border Post, Balancing Rock.',
                    'Overnight Stay: Shillong (Premium Luxury Stay)',
                    'Meals Included: Premium Breakfast & Farewell Gala Dinner',
                ],
            ),
            _day(
                6,
                'SHILLONG TO GUWAHATI / DEPARTURE',
                (
                    'COLLECTING PRECIOUS HIGHLAND MEMORIES Relish your final luxury breakfast while taking in the beautiful mountain morning. Your private luxury transport vehicle will drive your family smoothly down the highway back toward Guwahati. If time permits, stop at the sacred Kamakhya Temple for blessings. Head to Guwahati Airport to board your flight home, bringing along a heart filled with beautiful family bonds and unforgettable memories shaped perfectly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door highway drop-off to airport/station.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Polo Towers / M-設計 Boutique | Sohra Plaza Heritage / similar',
                'Shillong | Cherrapunji',
                '3N Shillong|2N Cherrapunji',
                'Deluxe',
                'Executive Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Polo Towers / M-設計 Boutique | Sohra Plaza Heritage / similar | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Heritage Club - Tripura Castle | Cherrapunjee Holiday Resort',
                'Shillong | Cherrapunji',
                '3N Shillong|2N Cherrapunji',
                'Premium',
                'Premium Balcony Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Heritage Club - Tripura Castle | Cherrapunjee Holiday Resort | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Ri Kynjai Serene Lake Resort | Polo Orchid Resort Cherrapunji',
                'Shillong | Cherrapunji',
                '3N Shillong|2N Cherrapunji',
                'Luxury',
                'Luxury Lake View Cottage / Orchid Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Ri Kynjai Serene Lake Resort | Polo Orchid Resort Cherrapunji | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Ri Kynjai (Premium Presidential Suite) | Jiva Resort Cherrapunji (Luxury Villa)',
                'Shillong | Cherrapunji',
                '3N Shillong|2N Cherrapunji',
                'Ultra Luxury',
                'Presidential Suite | Luxury Villa',
                'VVIP Custom Handpicked Private Retreat',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Ri Kynjai (Premium Presidential Suite) | Jiva Resort Cherrapunji (Luxury Villa) | VVIP Custom Handpicked Private Retreat',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury accommodations across chosen properties.', 1),
            _inc_included('Luxury Transportation: Private dedicated SUV for transfers & sightseeing.', 2),
            _inc_included('Curated Meal Plan: Daily luxury breakfast and custom premium dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest relations manager on active standby.', 4),
            _inc_included('Welcome Amenities: Personalized family travel kit and fresh fruit basket.', 5),
            _inc_included('Complimentary Experience: Exclusive private family boat cruise ticket at Dawki.', 6),
            _inc_excluded('Mainline Airfare, domestic flight connections, or train tickets.', 7),
            _inc_excluded('All monument entries, caving camera fees, or local site guide tips.', 8),
            _inc_excluded('Personal expenses such as laundry, phone calls, drinks, or room service.', 9),
            _inc_excluded('Adventure sport supplements (Ziplining, canyon scuba diving, trekking guides).', 10),
        ],
    )
    return package, itinerary

def build_ml_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ML-003'
    tour_code = 'TRG-MEG-003'
    title = 'Romantic Meghalaya Escape • Romance in the Abode of Clouds'
    duration = '05 Nights / 06 Days'
    slug = 'ml-003-romantic-meghalaya-escape-romance-in-the-abode-of-clouds'
    itin_slug = 'ml-003-romantic-meghalaya-escape-romance-in-the-abode-of-clouds-itinerary'
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
            _ph('Serial code ML-003 | TRAGUIN tour code TRG-MEG-003', 1),
            _ph('State / Country: Meghalaya / India | Category: Honeymoon /', 2),
            _ph('Destinations: Shillong • Cherrapunjee • Dawki • Shnongpdeng • Mawlynnong', 3),
            _ph('Ideal for: Newlyweds, Nature Lovers & Luxury Seekers', 4),
            _ph('Best season: October to May (Crystal Clear Waters & Spring Blooms)', 5),
            _ph('Starting price: On Request (Premium Customized)', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / MAPAI (Breakfast & Gourmet Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private riverside evening tea setup with traditional local snacks at', 8),
            _ph('Curated by TRAGUIN Experts: Custom routing developed to minimize travel fatigue, allowing maximum', 9),
            _ph('Premium Handpicked Hotels: Properties selected solely based on high safety parameters, excellent', 10),
            _ph("Exclusive Recommendations: VIP seating coordination at Shillong's best live jazz cafes and fine dining", 11),
            _ph("Local Markets & Souvenirs: Take home rare, handmade Khasi bamboo baskets, natural wild organic honey, local orange flower marmalades, and exquisite hand-woven winter stoles from Shillong's elite boutiques. Cafes & Food: Shillong is India's rock-music capital; enjoy live acoustics alongside local smoked-pork platters, hot steamed Kasi momos, and fine single-origin artisanal Meghalayan tea.", 12)
        ],
        moods=['Honeymoon', 'Romance', 'Luxury'],
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
        tagline='Romantic Meghalaya Escape',
        overview="ROMANTIC MEGHALAYA ESCAPE • ROMANCE IN THE ABODE OF CLOUDS Welcome to an ethereal romantic paradise custom-designed for you by TRAGUIN. Embark on a spectacular Meghalaya Honeymoon Package engineered to celebrate your new beginning amidst the most breathtaking landscapes in India. As your dedicated premium travel consultants, TRAGUIN converts this magical journey into a seamless luxury holiday filled with premium stays, emerald-green plunge pools, and intimate experiences. Allow the scenic beauty of cascading waterfalls, mist-kissed hills, and ancient Living Root Bridges to weave an emotional story for your shared future, crafting unforgettable memories along the way.\n\nTOUR OVERVIEW\nThis meticulously planned luxury vacation presents a rare blend of mist-shrouded peaks, crystalline jungle rivers, and high-end privacy. Travelling in an exclusive, chauffeur-driven premium AC vehicle, newlyweds are assured absolute comfort across every highland pass. Featuring an expertly selected meal plan including lavish breakfasts and intimate dinners, this signature path highlights the finest premium Meghalaya experience. To guarantee an exceptional journey, every milestone includes specialized TRAGUIN curated experiences—from candlelit setups to private riverside tracking—ensuring your honeymoon is nothing short of flawless.\n\nWHY CHOOSE THE BEST MEGHALAYA TOUR PACKAGE?\nWhen considering a Luxury Meghalaya Holiday, discerning couples seek an intimate union with nature without sacrificing sophisticated comfort. Meghalaya stands as one of the most iconic attractions in Northeast India. From Cherrapunjee's towering plunges—a top tourist place in Meghalaya for cloud-gazing—to the mesmerizing transparent waters of Dawki, the geographic beauty is simply unparalleled. For newlyweds booking a bespoke Meghalaya Honeymoon Package or Meghalaya Family Tour, the land unveils highly popular Instagram locations like the double-decker root bridges, Mawlynnong (the cleanest village in Asia), and the Krang Shuri waterfall. Whether you choose adrenaline-filled river canyoning, premium local shopping for bamboo art, or capturing professional couple photography against mist-covered gorges, our specialized TRAGUIN Meghalaya Packages ensure premium handpicked hotels and exclusive experiences during the absolute best time to visit Meghalaya.",
        seo_title='ML-003 | Romantic Meghalaya Escape | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Meghalaya package (ML-003 / TRG-MEG-003): Shillong • Cherrapunjee • Dawki • Shnongpdeng • Mawlynnong with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: GUWAHATI TO SHILLONG', 1),
            _ih('Day 02: SHILLONG TO CHERRAPUNJEE', 2),
            _ih('Day 03: CHERRAPUNJEE LIVING ROOT BRIDGES', 3),
            _ih('Day 04: CHERRAPUNJEE TO DAWKI & SHNONGPDENG', 4),
            _ih('Day 05: SHNONGPDENG TO MAWLYNNONG TO SHILLONG', 5),
            _ih('Day 06: SHILLONG TO GUWAHATI / DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private riverside evening tea setup with traditional local snacks at', 7),
            _ih('Curated by TRAGUIN Experts: Custom routing developed to minimize travel fatigue, allowing maximum', 8),
            _ih('Premium Handpicked Hotels: Properties selected solely based on high safety parameters, excellent', 9)
        ],
        days=[
            _day(
                1,
                'GUWAHATI TO SHILLONG',
                (
                    'WELCOME TO THE SCOTLAND OF THE EAST – A SCENIC SCOUT Your premium Meghalaya experience takes flight upon arrival at Guwahati Airport, where your personal luxury transport and professional chauffeur await your presence. Begin your scenic ascent into the Khasi hills, pausing to admire the breathtaking landscapes surrounding the vast Umiam Lake. Take a romantic break by the lakeside for pictures. Arrive in Shillong, the elegant state capital, and check into your handpicked premium resort. Spend your evening exploring the charming local cafes and bustling streets of Police Bazar.'
                ),
                [
                    'Sightseeing Included: Umiam Lake Panoramic Viewpoint, Police Bazar, Shillong Peak ambiance.',
                    'Evening Experience: Honeymoon Special: Complimentary welcome cake and customized room setup.',
                    'Overnight Stay: Shillong (Premium / Luxury Boutique Resort)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'SHILLONG TO CHERRAPUNJEE',
                (
                    'MIST-SHROUDED GORGES & MAJESTIC CASCADES Indulge in a magnificent breakfast before transferring to Cherrapunjee (Sohra), the historical domain of rain and mist. Your route winds past verdant, deep-cut valleys and dramatic limestone escarpments. Stop at Elephant Falls to stroll through its mist-sprayed forest paths. Stand hand-in-hand at the Mawkdok Dympep Valley viewpoint before checking into an ultra-luxury cliffside resort in Cherrapunjee. Watch the evening clouds roll into your private balcony space.'
                ),
                [
                    'Sightseeing Included: Elephant Falls, Mawkdok Valley Overlook, Nohkalikai Falls, Seven Sisters Falls.',
                    'Evening Experience: Bespoke candlelit dining overlooking the illuminated valley, curated by TRAGUIN experts.',
                    'Overnight Stay: Cherrapunjee (Luxury Cliffside Eco-Resort)',
                    'Meals Included: Premium Breakfast & Romantic Candlelit Dinner',
                ],
            ),
            _day(
                3,
                'CHERRAPUNJEE LIVING ROOT BRIDGES',
                (
                    'AN INTENSE JOURNEY TO THE LIVING ARCHITECTURE Awake early to experience a pristine, mountain-ringed dawn. Today is dedicated to an absolute bucket-list marvel: exploring the ancient Living Root Bridges. Trek deep into the emerald forests where the local Khasi tribes have trained living tree roots to span wild rivers. For active couples, descend down to the famous Double Decker Living Root Bridge of Nongriat village, discovering hidden turquoise natural pools perfect for a refreshing dip and timeless couple photography.'
                ),
                [
                    'Sightseeing Included: Tyrna Village Trailhead, Living Root Bridges, Secret Turquoise Rock Pools.',
                    'Optional Activities: Private local tribal guide for deep forest tracking and cultural storytelling.',
                    'Overnight Stay: Cherrapunjee (Luxury Cliffside Eco-Resort)',
                    'Meals Included: Premium Breakfast & Hearty Mountain Dinner',
                ],
            ),
            _day(
                4,
                'CHERRAPUNJEE TO DAWKI & SHNONGPDENG',
                (
                    'CRYSTAL CLEAR WATERS & RIVERSIDE GLAMPING LUXURY Following a rich breakfast, drive towards the international border town of Dawki. Here lies the Umngot River, celebrated worldwide for its unbelievable glass-like clarity. Board a private wooden country boat for an immersive experience, feeling as though you are floating directly in mid-air. Later, transfer to the hidden riverside hamlet of Shnongpdeng. Check into your premium glamping luxury tents set right along the pebble shores, surrounded by pristine nature. point.'
                ),
                [
                    'Sightseeing Included: Umngot River Boat Cruise, Shnongpdeng Suspension Bridge, Indo-Bangladesh Border',
                    'Evening Experience: Private riverside bonfire under a star-lit sky with acoustic mountain music.',
                    'Overnight Stay: Shnongpdeng (Premium Luxury Glamping Tents)',
                    'Meals Included: Breakfast & Riverside Barbecue Dinner',
                ],
            ),
            _day(
                5,
                'SHNONGPDENG TO MAWLYNNONG TO SHILLONG',
                (
                    "ASIA'S CLEANEST GARDEN VILLAGE & FAIRY TALE WATERFALLS Bid adieu to the river shores and head towards Mawlynnong, awarded the prestigious title of Asia's Cleanest Village. Walk along incredibly clean, flower-lined stone pathways that mimic a manicured botanical garden. Climb the Sky Walk for panoramic views extending across the vast plains of Bangladesh. On your loop back toward Shillong, visit the spectacular Krang Shuri Waterfall, a popular Instagram location known for its deep blue pool tucked inside a dramatic limestone cavern."
                ),
                [
                    'Sightseeing Included: Mawlynnong Eco-Village, Riwai Single Root Bridge, Krang Shuri Blue Lagoon.',
                    'Optional Activities: Swimming in the safe, clear cordoned zones of Krang Shuri with life vests.',
                    'Overnight Stay: Shillong (Premium Luxury Stay)',
                    'Meals Included: Breakfast & Farewell Premium Dinner',
                ],
            ),
            _day(
                6,
                'SHILLONG TO GUWAHATI / DEPARTURE',
                (
                    'CHERISHING ROMANTIC MEMORIES BEYOND DESTINATIONS Savor your last morning breakfast in the quiet, cool hills of Shillong. Your private luxury transport will conduct a smooth highway transfer back down to Guwahati. If time permits, visit the sacred Kamakhya Temple atop Nilachal Hill to seek blessings for your new life journey. Transfer directly to the airport or railway station for your homeward flight, carrying beautiful, unforgettable memories designed exclusively by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door airport/station drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Centre Point / M crown | Sohra Plaza Resort / similar | Standard Riverside Tents',
                'Shillong | Cherrapunjee | Shnongpdeng',
                '2N Shillong|2N Cherrapunjee|1N Shnongpdeng',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Centre Point / M crown | Sohra Plaza Resort / similar | Standard Riverside Tents | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Polo Towers / Landmark Victoria | Cherrapunjee Holiday Resort | Premium Riverside Glamping',
                'Shillong | Cherrapunjee | Shnongpdeng',
                '2N Shillong|2N Cherrapunjee|1N Shnongpdeng',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Polo Towers / Landmark Victoria | Cherrapunjee Holiday Resort | Premium Riverside Glamping | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Ri Kynjai Resort / Orchid Lake | Polo Orchid Resort (Jungle Suite) | Luxury Wooden Eco Cottage',
                'Shillong | Cherrapunjee | Shnongpdeng',
                '2N Shillong|2N Cherrapunjee|1N Shnongpdeng',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Ri Kynjai Resort / Orchid Lake | Polo Orchid Resort (Jungle Suite) | Luxury Wooden Eco Cottage | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Ri Kynjai (Cottage Suite Suite) | Jiva Resort (VVIP Luxury Suite) | Bespoke Private Luxury Swiss Camp',
                'Shillong | Cherrapunjee | Shnongpdeng',
                '2N Shillong|2N Cherrapunjee|1N Shnongpdeng',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Ri Kynjai (Cottage Suite Suite) | Jiva Resort (VVIP Luxury Suite) | Bespoke Private Luxury Swiss Camp | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury accommodations and exotic riverside glamping.', 1),
            _inc_included('Luxury Transportation: Private luxury SUV for all transfers and mountain routes.', 2),
            _inc_included('Curated Meals: Daily elaborate breakfasts and customized gourmet dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated local guest experience manager.', 4),
            _inc_included('Welcome Amenities: Customized honeymoon kit, floral bedding, and refreshments.', 5),
            _inc_included('Complimentary Experience: Private country boat cruise on the Umngot River, Dawki.', 6),
            _inc_excluded('Airfare, domestic flight costs, or long train tickets.', 7),
            _inc_excluded('Trekking guide tips, camera licensing, entry monuments.', 8),
            _inc_excluded('Personal expenses such as laundry, liquor, calls, tips.', 9),
            _inc_excluded('Any extreme adventure sports or optional tours not outlined.', 10),
        ],
    )
    return package, itinerary

def build_ml_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ML-004'
    tour_code = 'TRG-MEG-004'
    title = 'Living Route Bridges & Wilderness Luxury Escape'
    duration = '05 Nights / 06 Days'
    slug = 'ml-004-living-route-bridges-wilderness-luxury-escape'
    itin_slug = 'ml-004-living-route-bridges-wilderness-luxury-escape-itinerary'
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
            _ph('Serial code ML-004 | TRAGUIN tour code TRG-MEG-004', 1),
            _ph('State / Country: Meghalaya / India | Category: Premium', 2),
            _ph('Destinations: Shillong • Cherrapunjee • Nongriat • Dawki • Mawlynnong', 3),
            _ph('Ideal for: Adventure Enthusiasts, Nature Lovers & Luxury Trekkers', 4),
            _ph('Best season: October to May (Best for Caving & Trekking)', 5),
            _ph('Starting price: On Request (Premium Customized Expedition)', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / MAPAI', 7),
            _ph('TRAGUIN Signature Experience: Private local Khasi host coordination for the deep-canyon Nongriat root', 8),
            _ph('Curated by TRAGUIN Experts: Perfect travel spacing that matches strenuous forest trekking with luxury', 9),
            _ph('Premium Handpicked Hotels: Elite clifftop properties selected specifically for high safety, comfort, and', 10),
            _ph('Luxury Transportation: Expert local mountain drivers providing impeccable, safe highway tracking.', 11),
            _ph("Local Markets & Souvenirs: Explore Shillong's local markets to discover premium orange blossom honey, high-quality Meghalaya cinnamon, wild black pepper, and exquisitely woven bamboo storage baskets or local Khasi shawls. Cafes & Food: Old Shillong and Cherrapunjee feature warm, timber-clad mountain cafes serving rich smoked meats, Jadoh rice dishes, ginger teas, and excellent local artisan bakery treats with live acoustic background music.", 12)
        ],
        moods=['Adventure', 'Nature', 'Luxury'],
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
        tagline='Living Route Bridges & Wilderness Luxury Escape',
        overview="LIVING ROUTE BRIDGES & WILDERNESS LUXURY ESCAPE Welcome to an unforgettable voyage into the Adobe of Clouds, masterfully crafted by TRAGUIN. Embark on the finest Meghalaya Family Tour and adventure escape, designed to take you deep into breathtaking landscapes, emerald plunge pools, and ancient bio-engineered wonders. As your expert luxury travel consultants, TRAGUIN transforms this rugged raw landscape into a highly seamless luxury holiday, matching immersive experiences with handpicked hotels and boutique premium stays. From the misty vertical drops of Cherrapunjee to the majestic, world-famous double-decker living root bridges of Nongriat, prepare for exclusive experiences that spark deep emotions and build lasting, unforgettable memories.\n\nTOUR OVERVIEW\nThis curated itinerary offers an incredible blend of high-octane adventure and boutique eco-luxury across the Khasi and Jaintia Hills. Traveling in a premium private SUV with a specialized local driver-guide, your party will navigate dramatic valleys, deep limestone caves, and crystal-clear river borders in absolute safety and high comfort. With an elevated meal plan presenting daily hot breakfasts and gourmet multi-cuisine dinners, this route represents the definitive premium Meghalaya experience. Every detail carries the signature touch of TRAGUIN curated experiences, including specialized local trekking marshals, pre-arranged village permissions, and a seamless 24/7 client concierge support network.\n\nWHY CHOOSE THE BEST MEGHALAYA TOUR PACKAGE?\nWhen arranging a Luxury Meghalaya Holiday, modern travelers look past basic sightseeing itineraries to find real, raw, yet comfortable nature encounters. Meghalaya holds some of the most iconic attractions in Northeast India. From Cherrapunjee's record-breaking rainfall cliffs and dramatic cascading waterfalls to the absolute fairytale appearance of Mawlynnong, recognized widely as Asia’s cleanest village, it stands out as an unparalleled getaway. For couples seeking a distinct Meghalaya Honeymoon Package or families booking a highly active Meghalaya Family Tour, the area unveils iconic, popular Instagram locations such as the transparent waters of Dawki's Umngot River, Nohkalikai Falls, and the ancient stone mazes of Mawsmai Cave. Whether you want to trek deep into mystical river canyons, sample rich local Khasi culinary delicacies, or photograph mist rolling over emerald valleys, our TRAGUIN Meghalaya Packages combine handpicked hotels and exclusive experiences to ensure you travel during the absolute best time to visit Meghalaya with total peace of mind.",
        seo_title='ML-004 | Living Route Bridges & Wilderness Luxury Escape | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Meghalaya package (ML-004 / TRG-MEG-004): Shillong • Cherrapunjee • Nongriat • Dawki • Mawlynnong with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: GUWAHATI ARRIVAL TO SHILLONG', 1),
            _ih('Day 02: SHILLONG TO CHERRAPUNJEE', 2),
            _ih('Day 03: NONGRIAT DOUBLE-DECKER LIVING ROOT BRIDGE TREK', 3),
            _ih('Day 04: CHERRAPUNJEE TO MAWLYNNONG & DAWKI', 4),
            _ih('Day 05: DAWKI TO SHILLONG VIA JOVAI', 5),
            _ih('Day 06: SHILLONG TO GUWAHATI DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private local Khasi host coordination for the deep-canyon Nongriat root', 7),
            _ih('Curated by TRAGUIN Experts: Perfect travel spacing that matches strenuous forest trekking with luxury', 8),
            _ih('Premium Handpicked Hotels: Elite clifftop properties selected specifically for high safety, comfort, and', 9)
        ],
        days=[
            _day(
                1,
                'GUWAHATI ARRIVAL TO SHILLONG',
                (
                    'GATEWAY TO THE SCOTLAND OF THE EAST – SCENIC PINE RUNS Your premium Meghalaya experience begins upon arrival at Guwahati Airport. You will be warmly greeted by your private luxury transport chauffeur before starting the scenic climb toward Shillong. Wind past lush rolling hills and take a relaxed break at the beautiful Umiam Lake, a massive azure water body enclosed by thick pine forests. Capture your first stunning landscape photographs here. Check into your boutique premium stay in Shillong and enjoy an evening walking around the historic, vibrant Police Bazar for a true taste of local lifestyle.'
                ),
                [
                    'Sightseeing Included: Umiam Lake panoramic viewpoint, Police Bazar heritage walk.',
                    'Evening Experience: Private dinner reservation highlighting authentic fusion Khasi cuisines.',
                    'Overnight Stay: Shillong (Boutique Premium / Luxury Resort)',
                    'Meals Included: Welcome Refreshment & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'SHILLONG TO CHERRAPUNJEE',
                (
                    "MISTY CANYONS, CASCADING WATERS & DEEP CAVING After a hearty breakfast, check out and drive along spectacular ridge lines to Cherrapunjee (Sohra), the land of clouds and giant waterfalls. Stop at the breathtaking Laitlum Canyons, an incredible popular Instagram location offering sweeping, vertical views of deep green gorges. Explore the mysterious limestone formations of Mawsmai Cave and stand before the awe-inspiring Nohkalikai Falls—India's tallest plunge waterfall. Check into your luxury cliff-side resort in the evening."
                ),
                [
                    'Sightseeing Included: Laitlum Canyons, Mawsmai Cave, Nohkalikai Falls, Seven Sisters Falls.',
                    'Optional Activities: Guided adventure zip-lining across the misty valleys of Sohra.',
                    'Overnight Stay: Cherrapunjee (Premium Cliff-side Resort Stay)',
                    'Meals Included: Premium Breakfast & Gourmet Dinner',
                ],
            ),
            _day(
                3,
                'NONGRIAT DOUBLE-DECKER LIVING ROOT BRIDGE TREK',
                (
                    'THE BIO-ENGINEERED ICONIC ATTRACTIONS OF MEGHALAYA Prepare for an incredible, emotionally moving encounter with pure nature. Accompanied by a private TRAGUIN trekking marshal, descend down the stone steps into the deep river canyon of Nongriat Village. Hike across suspension bridges and deep jungle trails to reach the iconic Double-Decker Living Root Bridge— a true marvel built by ancient Khasi tribes training the roots of Ficus trees. Continue a short distance to the spectacular Rainbow Falls, where sunlight creates vivid color bands over an emerald plunge pool. Enjoy a cooling dip before climbing back to your resort for a well-deserved premium spa massage.'
                ),
                [
                    'Sightseeing Included: Nongriat Double-Decker Root Bridge, Rainbow Falls, Natural turquoise pools.',
                    'Optional Activities: Deep rock pool swimming and outdoor jungle picnic snack service.',
                    'Overnight Stay: Cherrapunjee (Premium Cliff-side Resort Stay)',
                    'Meals Included: Breakfast & Special Relaxing Resort Dinner',
                ],
            ),
            _day(
                4,
                'CHERRAPUNJEE TO MAWLYNNONG & DAWKI',
                (
                    "CRYSTAL WATERS OF UMNGOT RIVER & ASIA'S CLEANEST VILLAGE Drive down toward the international border to witness the unreal, crystal-clear water of Dawki. Enjoy a private boat cruise on the Umngot River, where the water is so translucent that boats seem to float mid-air over the riverbed. Capture iconic photography shots here. Afterward, travel to Mawlynnong Village. Stroll along beautifully manicured flower paths, explore a nearby single living root bridge, and climb the Sky Walk for beautiful panoramic views across the plains of Bangladesh."
                ),
                [
                    'Sightseeing Included: Umngot River boat ride, Mawlynnong Village, Riwai Single Root Bridge.',
                    'Evening Experience: Stargazing bonfire setup along the quiet border valleys.',
                    'Overnight Stay: Dawki Luxury Riverside Glamping / Cherrapunjee Resort',
                    'Meals Included: Premium Breakfast & Riverside Campfire Dinner',
                ],
            ),
            _day(
                5,
                'DAWKI TO SHILLONG VIA JOVAI',
                (
                    'THE SPECTACULAR KRANG SURI WATERFALL EXPERIENCE Travel through the rolling green meadows of the Jaintia Hills to Jovai to witness the spectacular Krang Suri Waterfall. Known as one of the most beautiful tourist places in Meghalaya, Krang Suri is famous for its stunning turquoise pool nestled inside a deep forest clearing. Walk down the flagstone paths to enjoy exclusive swimming and a quiet, relaxed afternoon by the falls. Drive back to Shillong in the evening for your final signature night stay.'
                ),
                [
                    'Sightseeing Included: Krang Suri Waterfalls, Jowai deep forest paths, Laitkor Peak (optional).',
                    "Optional Activities: Cafe hopping in Shillong to enjoy the city's famous live independent music scene.",
                    'Overnight Stay: Shillong (Premium / Luxury Resort Stay)',
                    'Meals Included: Breakfast & Farewell Premium Dinner',
                ],
            ),
            _day(
                6,
                'SHILLONG TO GUWAHATI DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES OF THE CLOUD LAND Indulge in a final premium breakfast at your resort while taking in the morning mountain air. Pack your bags as your private SUV transports you smoothly down the highway back to Guwahati Airport. Bid farewell to the hills, carrying beautiful photographs and unforgettable memories meticulously arranged by the destination experts at TRAGUIN.'
                ),
                [
                    'Transfers Included: Private door-to-door highway drop-off to Guwahati Airport.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Polo Towers / M-Crown | Cherrapunjee Holiday Resort | Dawki Riverside Luxury Tents',
                'Shillong | Cherrapunjee | Dawki',
                '2N Shillong|2N Cherrapunjee|1N Dawki',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Polo Towers / M-Crown | Cherrapunjee Holiday Resort | Dawki Riverside Luxury Tents | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Courtyard by Marriott Shillong | Polo Orchid Resort / similar | Betelnut Resort Shnongpdeng',
                'Shillong | Cherrapunjee | Dawki',
                '2N Shillong|2N Cherrapunjee|1N Dawki',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Courtyard by Marriott Shillong | Polo Orchid Resort / similar | Betelnut Resort Shnongpdeng | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Ri Kynjai Serene Lake Resort | Jiva Resort Cherrapunjee | Bespoke Private Riverside Glamp',
                'Shillong | Cherrapunjee | Dawki',
                '2N Shillong|2N Cherrapunjee|1N Dawki',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Ri Kynjai Serene Lake Resort | Jiva Resort Cherrapunjee | Bespoke Private Riverside Glamp | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Ri Kynjai (Cottage Suite) | Jiva Resort (Luxury Villa) | TRAGUIN VVIP Customized Elite Setup',
                'Shillong | Cherrapunjee | Dawki',
                '2N Shillong|2N Cherrapunjee|1N Dawki',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Ri Kynjai (Cottage Suite) | Jiva Resort (Luxury Villa) | TRAGUIN VVIP Customized Elite Setup | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury accommodation as selected with great views.', 1),
            _inc_included('Luxury Transportation: Private dedicated SUV for all point-to-point tours.', 2),
            _inc_included('Curated Meal Plan: Lavish hot buffet breakfast and gourmet dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest manager assistance on speed dial.', 4),
            _inc_included('Welcome Amenities: Personalized traveler kit, local fruit basket, and maps.', 5),
            _inc_included('Complimentary Experience: Private country boat cruise ride on the Umngot River.', 6),
            _inc_excluded('Airfare, domestic flights, or train ticket costs to Guwahati.', 7),
            _inc_excluded('Adventure activities such as zip-lining, scuba, or cliff jumping.', 8),
            _inc_excluded('Local parking taxes, monument entries, and camera fees.', 9),
            _inc_excluded('Personal items, laundry, alcoholic drinks, or driver tips.', 10),
        ],
    )
    return package, itinerary

def build_ml_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ML-005'
    tour_code = 'TRG-MEG-005'
    title = 'Meghalaya Discovery • Journey Into the Abode of Clouds'
    duration = '06 Nights / 07 Days'
    slug = 'ml-005-meghalaya-discovery-journey-into-the-abode-of-clouds'
    itin_slug = 'ml-005-meghalaya-discovery-journey-into-the-abode-of-clouds-itinerary'
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
            _ph('Serial code ML-005 | TRAGUIN tour code TRG-MEG-005', 1),
            _ph('State / Country: Meghalaya / India | Category: Premium Family', 2),
            _ph('Destinations: Shillong • Cherrapunji • Dawki • Mawlynnong • Jowai', 3),
            _ph('Ideal for: Family Holidays, Eco- Luxury Explorers & Nature Lovers', 4),
            _ph('Best season: October to May (Crisp & Crystal Clear Streams)', 5),
            _ph('Starting price: On Request (Premium Handpicked Customised)', 6),
            _ph('Vehicle / Meals: Private Luxury SUV (Innova Crysta) / MAPAI Plan', 7),
            _ph('TRAGUIN Signature Experience: Private family riverside picnic lunch served along the secret pristine', 8),
            _ph('Curated by TRAGUIN Experts: Seamless routing designed to bypass heavy valley traffic, maximizing', 9),
            _ph('Premium Handpicked Hotels: Elite properties selected for high safety ratings, breathtaking views, and', 10),
            _ph('Luxury Transportation: Professional hill-certified chauffeurs ensuring absolute safety and smooth', 11),
            _ph('Hotel Policies: Check-in time is 14:00 hrs and check-out is 11:00 hrs. Valid government-issued photo IDs', 12)
        ],
        moods=['Family', 'Nature', 'Luxury'],
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
        tagline='Meghalaya Discovery',
        overview='MEGHALAYA DISCOVERY • JOURNEY INTO THE ABODE OF CLOUDS Welcome to an extraordinary luxury holiday curated exclusively by TRAGUIN. Embark on the finest Meghalaya Family Tour, meticulously designed to uncover the breathtaking landscapes, ancient living root architectures, and pristine emerald waters of Northeast India. As your elite travel consultants, TRAGUIN transforms your exploration into a seamless premium holiday filled with handpicked hotels, elite dining, and highly immersive experiences. Let the scenic beauty of pine-covered hills, misty valleys, and majestic cascades frame your family getaway, creating unforgettable memories to cherish forever.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers an exquisite balance between natural wonders, cultural richness, and modern premium hospitality. Travelling in a completely private, luxury SUV with a dedicated professional chauffeur, your family will enjoy absolute comfort along the winding, scenic routes. Featuring a carefully curated meal plan with expansive breakfasts and elite dinners, this itinerary represents the definitive premium Meghalaya experience. Every detail bears the signature touch of TRAGUIN curated experiences, ensuring VIP coordination, local storytelling, and 24/7 bespoke ground assistance.\n\nWHY CHOOSE THE BEST MEGHALAYA TOUR PACKAGE?\nWhen planning a Luxury Meghalaya Holiday, discerning travellers seek a deep dive into pristine ecology and cloud-kissed heights. Meghalaya is home to some of the most iconic attractions in the world. From the globally celebrated Double Decker Living Root Bridges of Cherrapunji to the glass-like transparency of the Umngot River in Dawki, the region offers immense depth for photographers and families alike. For couples and families looking for a unique Meghalaya Honeymoon Package or Meghalaya Family Tour, the state offers popular Instagram locations such as the dramatic Laitlum Canyons, Krang Suri Waterfall, and the immaculately clean village of Mawlynnong. Whether you are indulging in local Khasi culinary delights, shopping for intricate bamboo handicrafts at Police Bazar, or discovering hidden limestone formations, our signature TRAGUIN Meghalaya Packages combine handpicked luxury stays and exclusive experiences to ensure your journey is perfectly timed for the best time to visit Meghalaya.',
        seo_title='ML-005 | Meghalaya Discovery | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Meghalaya package (ML-005 / TRG-MEG-005): Shillong • Cherrapunji • Dawki • Mawlynnong • Jowai with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GUWAHATI TO SHILLONG', 1),
            _ih('Day 02: SHILLONG TO CHERRAPUNJI VIA LAITLUM CANYONS', 2),
            _ih('Day 03: CHERRAPUNJI EXPLORATION', 3),
            _ih('Day 04: CHERRAPUNJI TO MAWLYNNONG & DAWKI', 4),
            _ih('Day 05: EXCURSION TO JOWAI & KRANG SURI FALLS', 5),
            _ih('Day 06: SHILLONG HIGHLIGHTS & LOCAL CULTURE', 6),
            _ih('Day 07: SHILLONG TO GUWAHATI / DEPARTURE', 7),
            _ih('TRAGUIN Signature Experience: Private family riverside picnic lunch served along the secret pristine', 8),
            _ih('Curated by TRAGUIN Experts: Seamless routing designed to bypass heavy valley traffic, maximizing', 9),
            _ih('Premium Handpicked Hotels: Elite properties selected for high safety ratings, breathtaking views, and', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GUWAHATI TO SHILLONG',
                (
                    'Your premium Meghalaya experience starts with a warm welcome at Guwahati Airport by your private luxury transport chauffeur. Begin your scenic drive ascending into the cool, refreshing Khasi hills. Stop en route at the breathtaking Umiam Lake, a massive azure water reservoir enveloped by dense pine forests. Enjoy a private lakeside refreshment service before checking into your handpicked premium stay in Shillong.'
                ),
                [
                    'WELCOME NOTE: JOURNEY TO SCOTLAND OF THE EAST VIA UMIAM LAKE',
                    'Sightseeing Included: Umiam Lake panoramic viewpoint, Shillong pine groves drive.',
                    'Evening Experience: Leisurely walk through the European-style lanes of Shillong; traditional high tea.',
                    'Overnight Stay: Shillong (Premium / Luxury Resort)',
                    'Meals Included: Welcome Drink & Gourmet Dinner',
                ],
            ),
            _day(
                2,
                'SHILLONG TO CHERRAPUNJI VIA LAITLUM CANYONS',
                (
                    'DRAMATIC CANYON HORIZONS & SPECTACULAR WATERFALLS Awake early for a lavish breakfast and check out toward Cherrapunji. Your first destination is Laitlum Canyons, an incredible ridge offering breathtaking landscapes of deep valleys and amphitheater-like mist formations. This highly popular Instagram location feels like stepping onto the edge of the world. Continue your journey to Cherrapunji, stopping at the roaring Elephant Falls and Mawkdok Dympep Valley Viewpoint. Arrive at your luxury cliffside resort in the evening.'
                ),
                [
                    'Sightseeing Included: Laitlum Canyons, Elephant Falls, Mawkdok Valley Overlook, Wakaba Falls.',
                    'Optional Activities: An exhilarating zip-lining experience across the misty gorges of Mawkdok.',
                    'Overnight Stay: Cherrapunji (Premium Cliff-view Luxury Resort)',
                    'Meals Included: Premium Breakfast & Fine-dining Dinner',
                ],
            ),
            _day(
                3,
                'CHERRAPUNJI EXPLORATION',
                (
                    'LIVING ROOT ARCHITECTURE & MYSTICAL SUBTERRANEAN CAVES Dedicate your day to exploring the legendary wettest place on earth. Discover the astounding living root bridges, a marvel of bio-engineering where ancient Khasi tribes trained rubber tree roots to form natural footbridges. For adventurous families, a guided excursion down to the iconic Double Decker Living Root Bridge is available. Later, explore Mawsmai Cave, a beautifully illuminated limestone cavern filled with stalactites, followed by a visit to Seven Sisters Falls and Nohkalikai Falls—the tallest plunge waterfall in India.'
                ),
                [
                    'Sightseeing Included: Single/Double Root Bridges, Mawsmai Cave, Nohkalikai Falls, Eco Park.',
                    'Photography Points: The mist-enshrouded drop of Nohkalikai Falls from the private viewing deck.',
                    'Overnight Stay: Cherrapunji (Premium Cliff-view Luxury Resort)',
                    'Meals Included: Premium Breakfast & Resort Buffet Dinner',
                ],
            ),
            _day(
                4,
                'CHERRAPUNJI TO MAWLYNNONG & DAWKI',
                (
                    'CLEANEST VILLAGE IN ASIA & CRYSTAL EMERALD RIVERS Embark on a scenic drive toward Mawlynnong, awarded the cleanest village in Asia. Stroll through manicured, flower-lined pathways and climb the Sky Walk for a sweeping view into the plains of Bangladesh. Next, journey to Dawki, where the magical Umngot River awaits. Experience an exclusive boat cruise on water so clear that your boat appears suspended in mid-air. Capture stunning photographs at this legendary location before heading to your luxury tented camp or driving back to Shillong. Border.'
                ),
                [
                    'Sightseeing Included: Mawlynnong Clean Village, Living Root Bridge of Riwai, Umngot River (Dawki), Indo-Bangla',
                    'Evening Experience: Private sunset boat cruise along the crystal-clear waters of Dawki arranged by TRAGUIN.',
                    'Overnight Stay: Shillong or Premium Dawki Riverside Riverside Luxury Glamping',
                    'Meals Included: Premium Breakfast & Traditional Khasi-Style Dinner',
                ],
            ),
            _day(
                5,
                'EXCURSION TO JOWAI & KRANG SURI FALLS',
                (
                    'THE INDIGO MAGIC OF JAINTIA HILLS Drive eastward into the hidden paradise of Jaintia Hills to visit Jowai. Discover the spectacular Krang Suri Waterfall, widely considered the most beautiful water pool in Northeast India. The striking turquoise waters, framed by deep limestone cut-outs, offer an incredible setting for relaxation and photography. Wander through the massive stone monoliths of Nartiang, packed with rich tribal histories, before returning to Shillong for your final evening.'
                ),
                [
                    'Sightseeing Included: Krang Suri Waterfall, Nartiang Monoliths, Thadlaskein Lake.',
                    'Optional Activities: Swimming with safety gear in the natural pool at Krang Suri.',
                    'Overnight Stay: Shillong (Premium / Luxury Stay)',
                    'Meals Included: Premium Breakfast & Farewell Dinner Celebration',
                ],
            ),
            _day(
                6,
                'SHILLONG HIGHLIGHTS & LOCAL CULTURE',
                (
                    'THE SOPHISTICATED HERITAGE & CAFE VIBES OF SHILLONG Spend a beautiful, relaxed day soaking in the sophisticated urban culture of Shillong. Visit the Don Bosco Museum, a world-class architectural showcase of Northeast India’s diverse tribal heritage. Walk along the tranquil fairways of the Shillong Golf Course, one of the oldest and highest natural 18-hole courses in Asia. Spend your afternoon sampling artisan coffees and listening to live acoustic music at upscale cafes in the Laitumkhrah neighborhood. Bespoke shopping at Police Bazar for authentic hand-woven tribal shawls and bamboo crafts.'
                ),
                [
                    "Sightseeing Included: Don Bosco Museum, Shillong Peak (viewpoint), Ward's Lake, Shillong Golf Links.",
                    'Shopping: Point:',
                    'Overnight Stay: Shillong (Premium Luxury Stay)',
                    "Meals Included: Premium Breakfast & Chef's Special Dinner",
                ],
            ),
            _day(
                7,
                'SHILLONG TO GUWAHATI / DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Enjoy a final lavish breakfast at your premium hotel while admiring the mountain mist. Pack your bags as your private luxury SUV takes you smoothly back along the highway toward Guwahati Airport. Bid farewell to the stunning hills of Meghalaya, carrying home a heart full of family bonding and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door highway drop-off to Guwahati.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Polo Towers / M-Pratibha / similar | Cherrapunji Holiday Resort / similar',
                'Shillong | Cherrapunji',
                '4N Shillong|2N Cherrapunji',
                'Deluxe',
                'Deluxe Room',
                'MAPAI Plan (Daily Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Polo Towers / M-Pratibha / similar | Cherrapunji Holiday Resort / similar | MAPAI Plan (Daily Breakfast & Dinner)',
            ),
            _hotel(
                'Rigal Heritage / Courtyard by Marriott | Saimika Resort / Jiva Resort (Executive)',
                'Shillong | Cherrapunji',
                '4N Shillong|2N Cherrapunji',
                'Premium',
                'Deluxe Room',
                'MAPAI + Premium Room Upgrades',
                4,
                2,
                description='OPTION 02 – PREMIUM: Rigal Heritage / Courtyard by Marriott | Saimika Resort / Jiva Resort (Executive) | MAPAI + Premium Room Upgrades',
            ),
            _hotel(
                'Ri Kynjai Serenity By The Lake / similar | Polo Orchid Resort (Orchid Rooms)',
                'Shillong | Cherrapunji',
                '4N Shillong|2N Cherrapunji',
                'Luxury',
                'Private Balcony View Suites',
                'MAPAI + Private Balcony View Suites',
                5,
                3,
                description='OPTION 03 – LUXURY: Ri Kynjai Serenity By The Lake / similar | Polo Orchid Resort (Orchid Rooms) | MAPAI + Private Balcony View Suites',
            ),
            _hotel(
                'Ri Kynjai (Luxury Heritage Cottage) | Polo Orchid Resort (Log Cabin With Private Plunge Pool)',
                'Shillong | Cherrapunji',
                '4N Shillong|2N Cherrapunji',
                'Ultra Luxury',
                'Deluxe Room',
                'VVIP Custom Chef Curated Dining',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Ri Kynjai (Luxury Heritage Cottage) | Polo Orchid Resort (Log Cabin With Private Plunge Pool) | VVIP Custom Chef Curated Dining',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury hotels as per chosen category.', 1),
            _inc_included('Luxury Transportation: Private AC Innova Crysta for all transfers & sightseeing.', 2),
            _inc_included('Curated Meal Plan: Daily luxury breakfast and gourmet dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest experience manager on call.', 4),
            _inc_included('Welcome Amenities: Personalized family travel kit, local fruit basket, and refreshments.', 5),
            _inc_included('Complimentary Experience: Private country boat cruise on the clear waters of Umngot River, Dawki.', 6),
            _inc_excluded('Airfare / Train tickets to and from Guwahati.', 7),
            _inc_excluded('Monument entry tickets, local adventure trekking guide fees, and camera costs.', 8),
            _inc_excluded('Personal expenses such as laundry, liquor, telephone calls, and tips.', 9),
            _inc_excluded('Any optional water sports, zip-lining activities, or extension tours.', 10),
        ],
    )
    return package, itinerary

def build_ml_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ML-006'
    tour_code = 'TRG-MEG-ML-006'
    title = 'Meghalaya Ladies Escape • Abode of Clouds & Sisterhood'
    duration = '05 Nights / 06 Days'
    slug = 'ml-006-meghalaya-ladies-escape-abode-of-clouds-sisterhood'
    itin_slug = 'ml-006-meghalaya-ladies-escape-abode-of-clouds-sisterhood-itinerary'
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
            _ph('Serial code ML-006 | TRAGUIN tour code TRG-MEG-ML-006', 1),
            _ph('State / Country: Meghalaya / India | Category: Female Only (Ladies Escape)', 2),
            _ph('Destinations: Shillong • Cherrapunjee • Dawki • Shnongpdeng • Mawlynnong', 3),
            _ph('Ideal for: Solo Female Groups, Girlfriends Getaway & Luxury Women Explorers', 4),
            _ph('Best season: October to May (Pleasant & Clear Water)', 5),
            _ph('Starting price: On Request (Premium Customized Group)', 6),
            _ph('Vehicle / Meals: Luxury Traveler / Innova Crysta • MAPAI Plan', 7),
            _ph('TRAGUIN Signature Experience: Private, chiseled rock-pool picnic at Krang Suri Waterfall with local', 8),
            _ph('Curated by TRAGUIN Experts: Custom-vetted routes optimized for safety, leisure time, and scenic', 9),
            _ph('TRAGUIN Premium Luxury Proposal • ML-006', 10),
            _ph('Personalized Assistance: A specialized female-friendly itinerary managed with strict professional', 11),
            _ph('Local Markets & Souvenirs: Explore the vibrant alleys of Police Bazar and Laitumkhrah to purchase authentic Khasi handwoven silk wrap-around skirts (Jainsem), intricate bamboo basketry, organic local wild honey, and freshly plucked Meghalaya cinnamon and black pepper spices. Cafes & Food: Shillong possesses a phenomenal live music and jazz café culture. Stop by iconic venues to enjoy artisan brewed coffees, cloud-fluffy pancakes, and authentic smoked bamboo-shoot pork platters.', 12)
        ],
        moods=['Wellness', 'Adventure', 'Luxury'],
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
        tagline='Meghalaya Ladies Escape',
        overview='MEGHALAYA LADIES ESCAPE • ABODE OF CLOUDS & SISTERHOOD TRAGUIN Premium Luxury Proposal • ML-006 1 Welcome to a magical, secure, and infinitely rejuvenating journey meticulously curated by TRAGUIN. Presenting the ultimate Meghalaya Honeymoon Package & Ladies Escape, uniquely designed for women who wish to explore breathtaking landscapes, emerald waters, and deep living root bridges in absolute comfort and luxury. As your premier travel consultants, TRAGUIN transforms this vacation into a beautifully immersive experience. From the mist-kissed hills of Shillong to the dramatic cascading waterfalls of Cherrapunjee and the crystal-clear transparency of Dawki river, every single moment is tailored to offer safe, soulful, and unforgettable memories for our guests.\n\nTOUR OVERVIEW\nThis elite Meghalaya Family Tour and Ladies Escape itinerary offers the perfect equilibrium between safety, sisterhood bonding, adventure, and high-end relaxation. Travelling in a dedicated premium air-conditioned vehicle with an expert, reliable chauffeur and a dedicated TRAGUIN tour coordinator, our guests enjoy premium stays at top-tier handpicked hotels and boutique luxury resorts. With a delicious meal plan combining traditional Khasi flavors and contemporary global cuisines, this route encapsulates the finest premium Meghalaya experience. Every detail includes exclusive experiences designed by TRAGUIN, complete with priority access, custom curated menus, and around-the-clock ground assistance.\n\nWHY CHOOSE THE BEST MEGHALAYA TOUR PACKAGE?\nWhen shortlisting a Luxury Meghalaya Holiday, women travellers and families prioritize seamless execution, exceptional hospitality, and deep local engagement. Meghalaya stands out as one of the most mesmerizing destinations in India, offering legendary iconic attractions. From the cascading multi-tiered Elephant Falls and the dramatic Nohkalikai Falls to the living root bridges engineered by the Khasi tribe, Meghalaya sightseeing is filled with wonder. For women seeking the ultimate getaway or couples looking for a romantic Meghalaya Honeymoon Package, the state offers popular Instagram locations such as the glassy waters of Umngot River in Dawki and the fairy-tale settings of Mawlynnong, famously awarded the cleanest village in Asia. Whether your group is looking for local marketplace handloom shopping, trekking through ancient sacred groves, or indulging in cozy local café cultures, our specialized TRAGUIN Meghalaya Packages ensure custom-vetted security, premium stays, and curated experiences that make it the best time to visit Meghalaya. TRAGUIN Premium Luxury Proposal • ML-006 2',
        seo_title='ML-006 | Meghalaya Ladies Escape | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Meghalaya package (ML-006 / TRG-MEG-ML-006): Shillong • Cherrapunjee • Dawki • Shnongpdeng • Mawlynnong with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GUWAHATI TO SHILLONG', 1),
            _ih('Day 02: SHILLONG TO CHERRAPUNJEE VIA LAITLUM CANYONS', 2),
            _ih('Day 03: CHERRAPUNJEE WATERFALLS & LIVING ROOT BRIDGES', 3),
            _ih('Day 04: CHERRAPUNJEE TO DAWKI, SHNONGPDENG & MAWLYNNONG', 4),
            _ih('Day 05: MAWLYNNONG TO JOWAI (JAINTIA HILLS) TO SHILLONG', 5),
            _ih('Day 06: SHILLONG TO GUWAHATI & DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private, chiseled rock-pool picnic at Krang Suri Waterfall with local', 7),
            _ih('Curated by TRAGUIN Experts: Custom-vetted routes optimized for safety, leisure time, and scenic', 8),
            _ih('TRAGUIN Premium Luxury Proposal • ML-006', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GUWAHATI TO SHILLONG',
                (
                    'WELCOME TO THE SCOTLAND OF THE EAST – HILL STATION GRACE Your premium Meghalaya experience begins upon arrival at Guwahati Airport, where your private luxury vehicle and dedicated TRAGUIN representative await. Embark on a highly scenic mountain drive towards Shillong. En route, stop by the breathtaking landscapes of Umiam Lake (Barapani), a massive azure water reservoir enveloped by dense coniferous pine trees. Take a pause at premium lakeside viewpoints for group photography. Arrive in Shillong and check into your handpicked premium stay. Spend your evening exploring the lively, musically charged ambiance of Police Bazar.'
                ),
                [
                    "Sightseeing Included: Umiam Lake Panoramic Viewpoint, Police Bazar evening walk, Ward's Lake.",
                    'Evening Experience: Exclusive high-tea and orientation circle hosted by your TRAGUIN tour lead.',
                    'Overnight Stay: Shillong (Premium Boutique Luxury Hotel)',
                    'Meals Included: Welcome High-Tea & Gourmet Dinner',
                ],
            ),
            _day(
                2,
                'SHILLONG TO CHERRAPUNJEE VIA LAITLUM CANYONS',
                (
                    'DRAMATIC CANYONS & THE RIDGE OF THE ABODE OF CLOUDS Savor a lavish breakfast before driving to the awe-inspiring Laitlum Canyons, meaning "End of Hills." This is a highly popular Instagram location featuring vast, plunging green gorges and mystical mist swirling through the valleys. Afterward, proceed toward Cherrapunjee, making a special stop at Elephant Falls, a spectacular three-tiered crystalline waterfall cascade. As you drive higher into the clouds, admire the breathtaking landscapes that make a luxury Meghalaya holiday so universally revered. Check into your ultra-luxury cliffside resort in Cherrapunjee.'
                ),
                [
                    'Sightseeing Included: Laitlum Canyons, Elephant Falls, Mawkdok Dympep Valley Viewpoint.',
                    'Optional Activities: Zip-lining across the deep Mawkdok valley gorge for an adrenaline rush.',
                    'Overnight Stay: Cherrapunjee (Ultra-Luxury Cliffside Eco-Resort)',
                    'Meals Included: Premium Breakfast & Luxury Buffer Dinner',
                ],
            ),
            _day(
                3,
                'CHERRAPUNJEE WATERFALLS & LIVING ROOT BRIDGES',
                (
                    "TREKKING THE LIVING WONDERS OF ECO-ENGINEERING Awake early to a spectacular valley sunrise. Today is dedicated to immersive experiences in nature. Explore the famous Living Root Bridges, hand-woven over centuries by indigenous Khasi tribes using the roots of ancient rubber trees. For the adventurous ladies, an optional trek to the iconic double-decker root bridge can be organized. Later, visit the spectacular Nohkalikai Falls—India's tallest plunge waterfall—and delve into the mysterious illuminated chambers of Mawsmai Cave or Arwah Cave, rich in prehistoric fossils."
                ),
                [
                    'Sightseeing Included: Nohkalikai Falls, Living Root Bridge, Mawsmai Cave, Eco Park, Seven Sisters Falls.',
                    'Evening Experience: Private bonfire storytelling evening at the resort with curated acoustic folk music.',
                    'Overnight Stay: Cherrapunjee (Ultra-Luxury Cliffside Eco-Resort)',
                    'Meals Included: Premium Breakfast & Lakeside-Style Dinner',
                ],
            ),
            _day(
                4,
                'CHERRAPUNJEE TO DAWKI, SHNONGPDENG & MAWLYNNONG',
                (
                    'CRYSTAL EMBRACE – THE FLOATING BOATS OF UMNGOT RIVER After breakfast, embark on a spectacular scenic route toward Dawki, situated on the international border. Here lies the Umngot River, world-famous for its glass-like water transparency. Enjoy an exclusive experience on a private, hand-paddled country boat ride where your boat appears to float mid-air over the riverbed. Continue to Shnongpdeng village for quiet riverfront relaxation. In the afternoon, drive to Mawlynnong, famously known as the cleanest village in Asia. Take a romantic walk through the manicured flower paths and climb the Sky View bamboo tower looking into the plains of Bangladesh. Root Bridge. Complimentary Experience: TRAGUIN complimentary private boat cruise on the clear waters of Umngot River.'
                ),
                [
                    'Sightseeing Included: Umngot River at Dawki, Shnongpdeng suspension bridge, Mawlynnong Village, Single',
                    'Overnight Stay: Shillong / Mawlynnong Premium Eco-Lodges',
                    'Meals Included: Breakfast & Traditional Organic Buffet Dinner',
                ],
            ),
            _day(
                5,
                'MAWLYNNONG TO JOWAI (JAINTIA HILLS) TO SHILLONG',
                (
                    'HIDDEN GEM DISCOVERY – TO THE FAIRYLAND OF KRANG SURI Today, travel to the Jaintia Hills region to witness Krang Suri Falls, arguably the most breathtakingly beautiful, under-explored turquoise waterfall in India. Walk through a forested pathway cut out of chiseled stone to arrive at a brilliant blue pool nestled under giant cliffs. It is an unmatched photography point and an ideal location for a relaxed group dip. Return to Shillong in the evening for a special premium farewell dinner celebration inside an elite heritage café.'
                ),
                [
                    'Sightseeing Included: Krang Suri Turquoise Waterfall, Thadlaskein Lake (en route), Laitkor Peak.',
                    'Evening Experience: Farewell gala event with gourmet fine-dining curated by TRAGUIN experts.',
                    'Overnight Stay: Shillong (Premium Boutique Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Gala Farewell Dinner',
                ],
            ),
            _day(
                6,
                'SHILLONG TO GUWAHATI & DEPARTURE',
                (
                    'CHERISHING THE MEMORIES OF SISTERHOOD BEYOND DESTINATIONS Indulge in a final morning breakfast surrounded by the peaceful whispers of the pine trees. Pack your bags and board your private luxury vehicle for a smooth highway transfer back to Guwahati Airport. As your incredible journey concludes, bid farewell to the Northeast, carrying home an array of unforgettable memories, deep new friendships, and rejuvenated spirits, all crafted flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door airport drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Polo Towers / M-Pratishtha | Cherrapunjee Holiday Resort',
                'Shillong | Cherrapunjee',
                '3N Shillong|2N Cherrapunjee',
                'Deluxe',
                'Deluxe Balcony Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Polo Towers / M-Pratishtha | Cherrapunjee Holiday Resort | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Heritage Club - Tripura Castle | Jiva Resort / Polo Orchid Resort',
                'Shillong | Cherrapunjee',
                '3N Shillong|2N Cherrapunjee',
                'Premium',
                'Premium Executive Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Heritage Club - Tripura Castle | Jiva Resort / Polo Orchid Resort | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Ri Kynjai - Serenity By The Lake | Saimika Resort Luxury Chalet',
                'Shillong | Cherrapunjee',
                '3N Shillong|2N Cherrapunjee',
                'Luxury',
                'Luxury Lakeview / Cliff Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Ri Kynjai - Serenity By The Lake | Saimika Resort Luxury Chalet | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Ri Kynjai (Cottage Suite) | Jiva Resort (Royal Presidential Suite)',
                'Shillong | Cherrapunjee',
                '3N Shillong|2N Cherrapunjee',
                'Ultra Luxury',
                'VVIP Private Villa Signature Club',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Ri Kynjai (Cottage Suite) | Jiva Resort (Royal Presidential Suite) | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Handpicked properties verified for female-only safety standards.', 1),
            _inc_included('Luxury Transportation: Chauffeur-driven AC Innova Crysta / Traveler for all sightseeing.', 2),
            _inc_included('Curated Meal Plan: Lavish daily breakfasts and specialized themed dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest manager & on-ground safety assistance.', 4),
            _inc_included('Welcome Amenities: Personalized eco- friendly custom travel kit & arrival snacks.', 5),
            _inc_included('Complimentary Experience: Private country boat cruise ride along the crystal clear Dawki River.', 6),
            _inc_excluded('Airfare, flight bookings, or long-distance train tickets to Guwahati.', 7),
            _inc_excluded('Optional activities like zip-lining, river cliff jumping, or deep canyon scuba.', 8),
            _inc_excluded('Monument entry tickets, local camera permits, or specialized local guide tips.', 9),
            _inc_excluded('Personal expenses such as laundry, phone calls, or mini-bar usage.', 10),
        ],
    )
    return package, itinerary

def build_ml_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ML-007'
    tour_code = 'TRG-MEG-007'
    title = 'Leisure Meghalaya Escape • The Abode of Clouds'
    duration = '05 Nights / 06 Days'
    slug = 'ml-007-leisure-meghalaya-escape-the-abode-of-clouds'
    itin_slug = 'ml-007-leisure-meghalaya-escape-the-abode-of-clouds-itinerary'
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
            _ph('Serial code ML-007 | TRAGUIN tour code TRG-MEG-007', 1),
            _ph('State / Country: Meghalaya / India | Category: Senior Citizen', 2),
            _ph('Destinations: Shillong • Umiam Lake • Cherrapunji • Mawlynnong • Dawki', 3),
            _ph('Ideal for: Senior Citizens, Families & Leisure Travelers', 4),
            _ph('Best season: October to May (Pleasant & Comfortable)', 5),
            _ph('Starting price: On Request (Bespoke Luxury Customization)', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / MAPAI', 7),
            _ph('Route: Guwahati • Umiam Lake • Shillong (2N) • Cherrapunji (2N) • Mawlynnong & Dawki Excursion • Shillong (1N) • Guwahati Departure This custom-tailored luxury holiday is thoughtfully planned as a Fully Independent Tour (FIT) optimized specifically for senior citizens and luxury leisure travelers. Avoid long walks, steep stairs, or stressful schedules. Rest and travel comfortably inside a private, spacious, air-conditioned premium', 8),
            _ph('TRAGUIN Signature Experience: Private roadside tea and light refreshment setup during long scenic', 9),
            _ph('Curated by TRAGUIN Experts: Highly optimized itineraries keeping senior health and luggage ease in', 10),
            _ph('Premium Handpicked Hotels: Properties chosen specifically for excellent lift facilities, step-free access,', 11),
            _ph('Luxury Transportation: Expert drivers well-trained in smooth hill driving to ensure your comfort.', 12),
            _ph("Local Markets & Souvenirs: Explore Shillong's famous markets to purchase genuine Khasi organic honey, world-renowned spicy soot-dried black pepper, authentic Sohiong fruit jams, and exquisite handmade bamboo baskets or cane furniture pieces. Food & Cafes: Relax inside the beautiful, warm ambient wood cafes of Shillong to enjoy freshly brewed Assam and Meghalaya tea blends, soft bakeries, and high-end local culinary options.", 13)
        ],
        moods=['Leisure', 'Family', 'Luxury'],
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
        tagline='Leisure Meghalaya Escape',
        overview='LEISURE MEGHALAYA ESCAPE • THE ABODE OF CLOUDS Welcome to an ethereal journey into nature’s quiet embrace, carefully designed and presented by TRAGUIN. This exclusive Meghalaya Senior Citizen Leisure itinerary offers the ultimate Best Meghalaya Tour Package experience, combining comfort, safety, and smooth accessibility. Delve into the breathtaking landscapes, emerald hills, and mist-kissed valleys of Northeast India without any physical strain. As your expert travel consultants, TRAGUIN transforms your holiday into a highly personalized luxury vacation filled with handpicked hotels, smooth scenic drives, and immersive experiences that linger beautifully in your mind, weaving unforgettable memories for you and your loved ones.\n\nTOUR OVERVIEW\nTravel Route: Guwahati • Umiam Lake • Shillong (2N) • Cherrapunji (2N) • Mawlynnong & Dawki Excursion • Shillong (1N) • Guwahati Departure This custom-tailored luxury holiday is thoughtfully planned as a Fully Independent Tour (FIT) optimized specifically for senior citizens and luxury leisure travelers. Avoid long walks, steep stairs, or stressful schedules. Rest and travel comfortably inside a private, spacious, air-conditioned premium vehicle under the supervision of a seasoned, courteous chauffeur. Enjoy a curated meal plan featuring delicious, light, and healthy breakfast spreads and traditional multi-cuisine gourmet dinners. Every single detail includes the signature TRAGUIN curated experience note, providing VIP assistance, low-impact sight viewing, and round- the-clock concierge comfort.\n\nWHY CHOOSE THE BEST MEGHALAYA TOUR PACKAGE?\nWhen exploring a Luxury Meghalaya Holiday, senior travelers and families look for absolute tranquility, pristine nature, and top-tier hospitality. Meghalaya boasts some of the most iconic attractions in the world, ranging from magnificent water bodies to dense green canyon systems. A beautifully planned Meghalaya Family Tour or a romantic Meghalaya Honeymoon Package reveals the stunning scenic beauty of Umiam Lake—often called the Jewel of Meghalaya—alongside the legendary mist-shrouded peaks of Cherrapunji. Our itinerary targets highly searched experiences and popular Instagram locations that require very little walking, including the historic Seven Sisters Falls, Mawsmai Cave boardwalk, and the breathtakingly clean heritage pathways of Mawlynnong Village, widely celebrated as the Cleanest Village in Asia. Whether you want to enjoy a relaxed boat cruise on the crystalline waters of Umngot River in Dawki, shop for traditional bamboo crafts, or indulge in fine tea sampling in the Scotland of the East, our curated TRAGUIN Meghalaya Packages guarantee premium stays, expert coordination, and an unhurried travel pace during the absolute best time to visit Meghalaya.',
        seo_title='ML-007 | Leisure Meghalaya Escape | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Meghalaya package (ML-007 / TRG-MEG-007): Shillong • Umiam Lake • Cherrapunji • Mawlynnong • Dawki with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: GUWAHATI TO SHILLONG', 1),
            _ih('Day 02: SHILLONG LOCAL SIGHTSEEING', 2),
            _ih('Day 03: SHILLONG TO CHERRAPUNJI', 3),
            _ih('Day 04: CHERRAPUNJI LEISURE EXPLORATION', 4),
            _ih('Day 05: EXCURSION TO MAWLYNNONG & DAWKI TO SHILLONG', 5),
            _ih('Day 06: SHILLONG TO GUWAHATI / DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private roadside tea and light refreshment setup during long scenic', 7),
            _ih('Curated by TRAGUIN Experts: Highly optimized itineraries keeping senior health and luggage ease in', 8),
            _ih('Premium Handpicked Hotels: Properties chosen specifically for excellent lift facilities, step-free access,', 9)
        ],
        days=[
            _day(
                1,
                'GUWAHATI TO SHILLONG',
                (
                    'WELCOME TO THE SCOTLAND OF THE EAST – EMBARKING ON LEISURE Your premium Meghalaya experience begins with a warm welcome at Guwahati Airport or Railway Station by your dedicated private luxury transport chauffeur. Board your smooth vehicle and begin a highly scenic hill drive. Pause along the highway to experience the majestic scenic beauty of Umiam Lake, a massive azure water reservoir surrounded by soft whispering pine trees. Take magnificent photographs from our pre- selected, easily accessible viewpoint. Proceed to Shillong, check into your premium luxury hotel, and enjoy a warm welcome tea.'
                ),
                [
                    'Sightseeing Included: Umiam Lake Panoramic Viewpoint, Leisurely Shillong Hill Drive.',
                    'Evening Experience: Relaxed welcome lounge reception and high tea curated by TRAGUIN experts.',
                    'Overnight Stay: Shillong (Handpicked Heritage / Premium Resort)',
                    'Meals Included: Welcome Amenities & Luxury Buffet Dinner',
                ],
            ),
            _day(
                2,
                'SHILLONG LOCAL SIGHTSEEING',
                (
                    'CULTURE, BOTANICAL SPLENDOUR & RELAXED CITY HIGHLIGHTS Savor a lavish, light breakfast at your hotel before embarking on a highly comfortable Shillong sightseeing tour. Visit the beautifully maintained Ward’s Lake, featuring flat, easily walkable botanical pathways and an iconic wooden bridge. Explore the Don Bosco Museum to witness the vibrant heritage of the Northeast through premium displays (lifts available for easy access). Conclude your afternoon by exploring the exotic flora at the Lady Hydari Park gardens.'
                ),
                [
                    'Sightseeing Included: Ward’s Lake, Don Bosco Museum, Lady Hydari Park, Shillong Peak (view from vehicle).',
                    'Optional Activities: A curated evening walk through the upscale Police Bazar for local silk shopping.',
                    'Overnight Stay: Shillong (Premium / Luxury Stay)',
                    'Meals Included: Premium Breakfast & Fine Dining Dinner',
                ],
            ),
            _day(
                3,
                'SHILLONG TO CHERRAPUNJI',
                (
                    'JOURNEY INTO THE MISTY CANYONS & ROARING WATERFALLS After breakfast, enjoy a smooth, scenic route winding through deep cloud-filled valleys toward Cherrapunji (Sohra), historically famed as the wettest place on Earth. Marvel at the breathtaking landscapes from the easily accessible Duwan Sing Syiem Bridge viewpoint. Upon reaching Cherrapunji, witness the jaw-dropping majesty of the Seven Sisters Falls and Nohkalikai Falls from perfectly positioned, safe viewing decks that require no walking or climbing. Check into your ultra-luxury nature resort.'
                ),
                [
                    'Sightseeing Included: Duwan Sing Syiem Viewpoint, Seven Sisters Falls, Nohkalikai Cascade Overlook.',
                    'Evening Experience: A warm evening bonfire at the resort accompanied by soft local acoustic music.',
                    'Overnight Stay: Cherrapunji (Premium Luxury Valley-Facing Resort)',
                    'Meals Included: Premium Breakfast & Gourmet Chef’s Special Dinner',
                ],
            ),
            _day(
                4,
                'CHERRAPUNJI LEISURE EXPLORATION',
                (
                    'MYSTICAL CAVERNS & COZY RIVERSIDE RETREATS Spend a magnificent morning exploring the marvels of Cherrapunji at an unhurried, comfortable pace. Visit Mawsmai Cave, where a specialized flat boardwalk allows senior guests to admire stunning stalactite and stalagmite formations safely near the entrance. Spend your afternoon at the Eco Park, which offers serene mountain views and overlooks distant plains. Enjoy a peaceful afternoon reading or relaxing in your premium resort veranda overlooking the canyon.'
                ),
                [
                    'Sightseeing Included: Mawsmai Cave (accessible zone), Eco Park, Ramakrishna Mission Heritage Center.',
                    'Optional Activities: A premium spa treatment and wellness therapy session at your resort.',
                    'Overnight Stay: Cherrapunji (Premium Luxury Valley-Facing Resort)',
                    'Meals Included: Premium Breakfast & Luxury Resort Dinner',
                ],
            ),
            _day(
                5,
                'EXCURSION TO MAWLYNNONG & DAWKI TO SHILLONG',
                (
                    "ASIA'S CLEANEST PARADISE & CRYSTALLINE WATERS Set out on a marvelous full-day excursion. Arrive at Mawlynnong Village, acclaimed across the globe as the cleanest village in Asia. Stroll lazily along beautiful paved stone paths lined with colorful orchids and traditional bamboo houses. Next, drive down to Dawki, where the famous Umngot River flows with complete clarity. Board a private, highly secure luxury country boat for a gentle, peaceful ride across waters so clear that the boat appears suspended in mid-air. Return smoothly to Shillong for your final evening."
                ),
                [
                    'Sightseeing Included: Mawlynnong Living Village, Dawki Umngot River, Indo-Bangladesh Border overlook.',
                    'Evening Experience: Complimentary private boat cruise on the crystal waters of Dawki.',
                    'Overnight Stay: Shillong (Handpicked Premium Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Farewell Celebration Dinner',
                ],
            ),
            _day(
                6,
                'SHILLONG TO GUWAHATI / DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES OF THE CLOUDS Indulge in a final delicious breakfast at your premium hotel. Your private luxury transport will drive you safely down the smooth highway back to Guwahati Airport or Railway Station for your onward destination. Return home carrying a rejuvenated spirit, absolute peace of mind, and sweet unforgettable memories meticulously crafted by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door highway drop-off to Guwahati.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Polo Towers / similar | Polo Orchid Resort (Deluxe)',
                'Shillong | Cherrapunji',
                '3N Shillong|2N Cherrapunji',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Polo Towers / similar | Polo Orchid Resort (Deluxe) | MAPAI (Breakfast & Dinner) | Lift Access & Flat Walkways',
            ),
            _hotel(
                'M crown Hotel / Courtyard by Marriott | Cherrapunjee Holiday Resort',
                'Shillong | Cherrapunji',
                '3N Shillong|2N Cherrapunji',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: M crown Hotel / Courtyard by Marriott | Cherrapunjee Holiday Resort | MAPAI (Breakfast & Dinner) | Wheelchair assistance on request',
            ),
            _hotel(
                'Ri Kynjai Serene Lake Resort | Jiva Resort Cherrapunji (Suite)',
                'Shillong | Cherrapunji',
                '3N Shillong|2N Cherrapunji',
                'Luxury',
                'Premium ground-floor valley view suites',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Ri Kynjai Serene Lake Resort | Jiva Resort Cherrapunji (Suite) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Heritage Club - Tripura Castle (VVIP) | Jiva Resort (Royal Luxury Executive)',
                'Shillong | Cherrapunji',
                '3N Shillong|2N Cherrapunji',
                'Ultra Luxury',
                'VVIP Suite',
                'Bespoke luxury customized priority support',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Heritage Club - Tripura Castle (VVIP) | Jiva Resort (Royal Luxury Executive) | Bespoke luxury customized priority support',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 05 Nights in senior-friendly handpicked hotels.', 1),
            _inc_included('Luxury Transportation: Private AC Toyota Innova Crysta for all transfers.', 2),
            _inc_included('Curated Meal Plan: Daily hot breakfasts and custom dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest manager with senior assistance protocol.', 4),
            _inc_included('Welcome Amenities: Customized family comfort kit, umbrellas, and rehydration aids.', 5),
            _inc_included('Complimentary Experience: Private country boat cruise ride at Dawki Umngot River.', 6),
            _inc_excluded('Airfare or long-distance train tickets to/from Guwahati.', 7),
            _inc_excluded('Monument entry tickets, professional museum guides, and camera fees.', 8),
            _inc_excluded('Personal expenses such as laundry, phone calls, drinks, and tips.', 9),
            _inc_excluded('Any adventure activities, trekking, or optional tours not specified.', 10),
        ],
    )
    return package, itinerary

def build_ml_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ML-008'
    tour_code = 'TRG-MEG-008'
    title = 'Luxury Meghalaya Escape • The Abode of Clouds'
    duration = '06 Nights / 07 Days'
    slug = 'ml-008-luxury-meghalaya-escape-the-abode-of-clouds'
    itin_slug = 'ml-008-luxury-meghalaya-escape-the-abode-of-clouds-itinerary'
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
            _ph('Serial code ML-008 | TRAGUIN tour code TRG-MEG-008', 1),
            _ph('State / Country: Meghalaya / India | Category: Luxury Travel', 2),
            _ph('Destinations: Shillong • Cherrapunji • Dawki • Mawlynnong • Jowai', 3),
            _ph('Ideal for: Luxury Honeymoon, Family Escape & Nature Discerning Guests', 4),
            _ph('Best season: October to May (Pleasant & Clear Water)', 5),
            _ph('Starting price: On Request (Premium Fully Bespoke)', 6),
            _ph('Vehicle / Meals: Luxury Private SUV / MAPAI (Luxury Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private, reserved riverside evening high-tea party on the pristine banks', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked local English-speaking tribal tracking guides to walk you', 9),
            _ph('Premium Handpicked Hotels: Cliff properties and lakeside villas offering unmatched balcony views of the', 10),
            _ph('Luxury Transportation: Highly skilled hill-certified chauffeurs with comprehensive navigation tools.', 11),
            _ph('Local Markets & Souvenirs: Head over to Police Bazar and Khasi heritage stores to find magnificent hand- woven endi silk shawls, organic wild honey, locally grown Sohiong fruit preserves, and wonderful handmade bamboo furniture items. Cafes & Food: Shillong is celebrated for its incredible live music and indie cafes. Do not miss tasting legendary local smoked pork dishes, traditional Jadoh rice meals, and artisanal fresh fruit desserts while listening to local acoustic artists in Old Shillong.', 12)
        ],
        moods=['Luxury', 'Honeymoon', 'Nature'],
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
        tagline='Luxury Meghalaya Escape',
        overview="LUXURY MEGHALAYA ESCAPE • THE ABODE OF CLOUDS Welcome to a timeless mountain sanctuary curated exclusively by TRAGUIN. Embark on the ultimate Luxury Meghalaya Holiday, meticulously tailored to reveal breathtaking landscapes, roaring waterfalls, living root bridges, and crystal-clear emerald rivers. As your elite travel consultants, TRAGUIN transforms your north-eastern vacation into a seamless luxury getaway complete with premium stays, deep cultural exploration, and private storytelling guides. From the pine-scented colonial charm of Shillong to the dramatic mist-shrouded gorges of Cherrapunji and the unblemished aquatic wonder of Dawki, every moment is crafted to leave you with unforgettable memories.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday itinerary offers an unparalleled balance between misty mountain peaks, untouched bio-diverse valleys, sacred indigenous forests, and elegant retreat stays. Traveling in a dedicated private premium luxury vehicle with a well-trained, local, English-speaking driver, your party will enjoy absolute seclusion and smooth transport. With an exceptional meal plan featuring magnificent spreads of fresh continental breakfasts and customized fine dinners, this custom route represents the definitive premium Meghalaya experience. Every single day of your journey carries the trademark signature touch of a TRAGUIN curated experience, providing private transfers, VIP access privileges, local interaction, and continuous bespoke support.\n\nWHY CHOOSE THE BEST MEGHALAYA TOUR PACKAGE?\nWhen considering a high-end Luxury Meghalaya Holiday, sophisticated travelers want to experience the rare ecosystems and warm tribal cultures without compromising on premium comfort. Meghalaya stands out as one of the most culturally unique and geographically fascinating regions in India. From exploring iconic attractions like the Double Decker Living Root Bridges—an ancient bio-engineering wonder—to visiting the top tourist places in Meghalaya like Nohkalikai Falls and the sacred groves of Mawphlang, Meghalaya sightseeing delivers awe-inspiring beauty at every corner. For couples and discerning families looking for a Meghalaya Honeymoon Package or a comprehensive Meghalaya Family Tour, the land unveils highly famous, popular Instagram locations such as the glassy Umngot River in Dawki, the hidden Laitlum Canyons, and the pristine, clean paths of Mawlynnong (Asia's cleanest village). Whether you seek adventure trekking inside deep limestone caves, shopping for exquisite hand-woven Khasi silk and cane artifacts, or simply enjoying the scenic beauty from your balcony at a boutique resort, our handpicked TRAGUIN Meghalaya Packages guarantee an extraordinary, stress-free escape during the absolute best time to visit Meghalaya.",
        seo_title='ML-008 | Luxury Meghalaya Escape | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Meghalaya package (ML-008 / TRG-MEG-008): Shillong • Cherrapunji • Dawki • Mawlynnong • Jowai with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: GUWAHATI TO SHILLONG', 1),
            _ih('Day 02: SHILLONG TO CHERRAPUNJI EXCURSION', 2),
            _ih('Day 03: CHERRAPUNJI LIVING ROOT BRIDGES', 3),
            _ih('Day 04: CHERRAPUNJI TO MAWLYNNONG & DAWKI', 4),
            _ih('Day 05: DAWKI TO JOWAI (JAINTIA HILLS) TO SHILLONG', 5),
            _ih('Day 06: SHILLONG FULL DAY HIGHLIGHTS', 6),
            _ih('Day 07: SHILLONG TO GUWAHATI / DEPARTURE', 7),
            _ih('TRAGUIN Signature Experience: Private, reserved riverside evening high-tea party on the pristine banks', 8),
            _ih('Curated by TRAGUIN Experts: Handpicked local English-speaking tribal tracking guides to walk you', 9),
            _ih('Premium Handpicked Hotels: Cliff properties and lakeside villas offering unmatched balcony views of the', 10)
        ],
        days=[
            _day(
                1,
                'GUWAHATI TO SHILLONG',
                (
                    'JOURNEY TO SCOTLAND OF THE EAST – SCENIC PINE RUNS Your premium Meghalaya experience begins upon arrival at Guwahati Airport, where your personal luxury private vehicle and chauffeur await you. Ascend seamlessly into the fresh hills of the East Khasi district. En route, experience a curated stop at the majestic Umiam Lake (Barapani), a massive sapphire-blue water body surrounded by dense pine groves. Capture breathtaking landscapes at scenic photography points before arriving in Shillong. Check into your premium stay at a luxury heritage estate or lakeside boutique resort. Spend your evening at leisure exploring the charming café culture of the city.'
                ),
                [
                    'Sightseeing Included: Umiam Lake viewpoint, Shillong local colonial avenues.',
                    'Evening Experience: Bespoke welcome dinner at a premium restaurant curated by TRAGUIN experts.',
                    'Overnight Stay: Shillong (Premium Handpicked Hotel / Luxury Resort)',
                    'Meals Included: Welcome Refreshments & Fine Dining Dinner',
                ],
            ),
            _day(
                2,
                'SHILLONG TO CHERRAPUNJI EXCURSION',
                (
                    "THE MIST-SHROUDED CANYONS & ROARING WATERFALLS Awake to the whispering pines and indulge in a lavish breakfast. Today you will drive to Cherrapunji (Sohra), the legendary land of rain and deep valleys. En route, enjoy an exclusive detour to the spectacular Laitlum Canyons, one of the most popular Instagram locations in the northeast, offering vast, panoramic mountain drop-offs. Continue into Cherrapunji to witness the iconic attractions of Mawsmai Cave, an extraordinary prehistoric limestone cave system, and the majestic Nohkalikai Falls, India's tallest plunge waterfall, cascading dramatically into an emerald pool."
                ),
                [
                    'Sightseeing Included: Laitlum Canyons, Nohkalikai Falls, Seven Sisters Falls, Mawsmai Cave, Eco Park.',
                    'Optional Activities: A private guided geological walk inside the deep recesses of Arwah Cave.',
                    'Overnight Stay: Cherrapunji (Luxury Cliff-front Resort)',
                    'Meals Included: Premium Breakfast & Gourmet Valley-View Dinner',
                ],
            ),
            _day(
                3,
                'CHERRAPUNJI LIVING ROOT BRIDGES',
                (
                    'IMMERSIVE BIO-ENGINEERING EXPERIENCES IN THE JUNGLE Dedicate this day to experiencing the awe-inspiring, living bio-architecture of Meghalaya. Following an energizing breakfast, head down to Tyrna village. Embark on a private guided trek down the valley to witness the world-famous Double Decker Living Root Bridge of Nongriat. Hand-woven from the roots of ancient Ficus trees by tribal Khasi ancestors over centuries, this location offers an emotionally moving tribute to nature and human harmony. Spend time by the crystal-clear natural pools before heading back up to your premium resort for a relaxing hot stone spa ritual. Authentic interaction with native Khasi village elders over traditional wild tea.'
                ),
                [
                    'Sightseeing Included: Nongriat Double Decker Living Root Bridge, Rainbow Falls (optional extended trek).',
                    'Local Experience: s:',
                    'Overnight Stay: Cherrapunji (Luxury Cliff-front Resort)',
                    'Meals Included: Premium Breakfast & Organic Local-Infused Dinner',
                ],
            ),
            _day(
                4,
                'CHERRAPUNJI TO MAWLYNNONG & DAWKI',
                (
                    "THE GLASS RIVER OF INDIA & ASIA'S CLEANEST VILLAGE Check out after an early morning breakfast and travel to Mawlynnong, internationally celebrated as Asia's cleanest village. Walk along the manicured, flower-lined pathways, explore the single-tier living root bridge of Riwai, and climb the sky-view bamboo tower. From there, descend to the India-Bangladesh border at Dawki. Behold the magnificent, jaw-dropping scenic beauty of the Umngot River, where the water is so impeccably clear that floating boats appear suspended in thin air. Enjoy a private, exclusive boating experience on its pristine emerald waters."
                ),
                [
                    'Sightseeing Included: Mawlynnong Village, Riwai Root Bridge, Dawki Umngot River, Indo-Bangla Border.',
                    'Evening Experience: Private sunset boat cruise with exclusive high-tea service right on the river banks.',
                    'Overnight Stay: Dawki Luxury Glamping Resort / Luxury Riverside Stay',
                    'Meals Included: Premium Breakfast & Barbecue Riverside Dinner',
                ],
            ),
            _day(
                5,
                'DAWKI TO JOWAI (JAINTIA HILLS) TO SHILLONG',
                (
                    'EXPLORING THE MAGICAL TURQUOISE CASCADES OF JOWAI Travel north today into the Jaintia Hills region to visit the top tourist places in Jowai. Discover Krang Shuri Waterfall, one of the most ethereal and photographed waterfalls in India, glowing with a deep, magical turquoise color. Walk down via a specially reserved paved path into the canyon to experience this untouched paradise. Afterward, drive through vast hill plateaus back toward Shillong, stopping by the scenic Laitkor Peak to view the city lights under a clear starry night.'
                ),
                [
                    'Sightseeing Included: Krang Shuri Falls, Phe Phe Falls (optional), Jowai scenic valleys, Laitkor Peak.',
                    'Optional Activities: Swimming in the natural blue lagoons of Krang Shuri with life-safety gear.',
                    'Overnight Stay: Shillong (Premium Handpicked Hotel / Luxury Resort)',
                    'Meals Included: Premium Breakfast & Elite Continental Dinner',
                ],
            ),
            _day(
                6,
                'SHILLONG FULL DAY HIGHLIGHTS',
                (
                    'SACRED GROVES, TRIBAL CULTURE & BOUTIQUE SHOPPING Immerse yourself completely in the rich indigenous heritage of the state. Travel to the ancient Mawphlang Sacred Forest, preserved intact for over 800 years by local tribal clans. A private local cultural expert will guide you past rare orchids, giant ferns, and megalithic stone altars while sharing ancient legends. Spend your afternoon touring the world-class Don Bosco Museum for a deep look into North-Eastern tribal history, followed by an elegant afternoon shopping trip around Police Bazar.'
                ),
                [
                    "Sightseeing Included: Mawphlang Sacred Grove, Don Bosco Museum, Ward's Lake, Elephant Falls.",
                    'Evening Experience: Farewell premium dining experience at a boutique colonial estate restaurant.',
                    'Overnight Stay: Shillong (Premium Handpicked Hotel / Luxury Resort)',
                    'Meals Included: Premium Breakfast & Farewell Gala Dinner',
                ],
            ),
            _day(
                7,
                'SHILLONG TO GUWAHATI / DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Indulge in a final lavish, hearty breakfast at your premium stay while enjoying the morning mountain breeze. Your private luxury transport will comfortably escort you back down the national highway to Guwahati Airport or Railway Station for your return flight. Head home carrying a heart filled with deep peace, awe-inspiring stories, and unforgettable memories flawlessly curated by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury airport highway drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Polo Towers / M-Pratiba | Sohra Plaza Resort / similar | Betelnut Resort Dawki / similar',
                'Shillong | Cherrapunji | Dawki',
                '3N Shillong|2N Cherrapunji|1N Dawki',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Polo Towers / M-Pratiba | Sohra Plaza Resort / similar | Betelnut Resort Dawki / similar | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Courtyard by Marriott Shillong | Cherrapunjee Holiday Resort | Dawki Exotic Glamping Tents',
                'Shillong | Cherrapunji | Dawki',
                '3N Shillong|2N Cherrapunji|1N Dawki',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Courtyard by Marriott Shillong | Cherrapunjee Holiday Resort | Dawki Exotic Glamping Tents | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Ri Kynjai Serene Lake Resort | Polo Orchid Resort Cherrapunji | ShantiDawki Luxury Riverfront Cabins',
                'Shillong | Cherrapunji | Dawki',
                '3N Shillong|2N Cherrapunji|1N Dawki',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Ri Kynjai Serene Lake Resort | Polo Orchid Resort Cherrapunji | ShantiDawki Luxury Riverfront Cabins | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Ri Kynjai (Premium Heritage Cottage) | Polo Orchid (Log Cabin with Private Pool) | VVIP Custom Private Luxury Eco-Retreat',
                'Shillong | Cherrapunji | Dawki',
                '3N Shillong|2N Cherrapunji|1N Dawki',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Ri Kynjai (Premium Heritage Cottage) | Polo Orchid (Log Cabin with Private Pool) | VVIP Custom Private Luxury Eco-Retreat | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury accommodations as per chosen hotel tier list.', 1),
            _inc_included('Luxury Transportation: Private dedicated SUV (Innova/In賓a Crysta) for all transit.', 2),
            _inc_included('Curated Meals: Daily high-end breakfast spreads and tailored dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest experience helpline on speed dial.', 4),
            _inc_included('Welcome Kit: Traditional north-eastern welcome scarf, custom travel maps, and treats.', 5),
            _inc_included('Complimentary Experience: Private country boat ride ticket on the crystal Umngot River.', 6),
            _inc_excluded('Airfare, domestic flights, or train tickets to Guwahati.', 7),
            _inc_excluded('Caving gears, local porterage, and personal trekking guide tips.', 8),
            _inc_excluded('Personal items, laundry, phone calls, and alcoholic drinks.', 9),
            _inc_excluded('Any insurance coverage, emergency rescue costs, or optional detours.', 10),
        ],
    )
    return package, itinerary

def build_ml_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ML-009'
    tour_code = 'TRG-MEG-009'
    title = 'Caving Meghalaya • The Subterranean Chronicles & Mystic Hills'
    duration = '05 Nights / 06 Days'
    slug = 'ml-009-caving-meghalaya-the-subterranean-chronicles-mystic-hills'
    itin_slug = 'ml-009-caving-meghalaya-the-subterranean-chronicles-mystic-hills-itinerary'
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
            _ph('Serial code ML-009 | TRAGUIN tour code TRG-MEG-009', 1),
            _ph('State / Country: Meghalaya / India | Category: Premium Adventure & Caving', 2),
            _ph('Destinations: Shillong • Cherrapunjee • Mawsmai • Mawryngkhang • Shnongpdeng', 3),
            _ph('Ideal for: Adventure Enthusiasts, Caving Explorers & Luxury Thrill Seekers', 4),
            _ph('Best season: October to May (Best for Caving & Clear Waters)', 5),
            _ph('Starting price: On Request (Premium Experiential Rates)', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private caving trails led by certified national speleological instructors.', 8),
            _ph('Curated by TRAGUIN Experts: Custom timing schedules to explore popular locations ahead of general', 9),
            _ph('Premium Handpicked Hotels: Accommodations chosen for their spectacular locations, top safety', 10),
            _ph('Exclusive Recommendations: Access maps and reservations for hidden hillside cafes and authentic', 11),
            _ph('Local Handcrafts: Purchase high-quality Khasi bamboo items, exquisitely woven cane baskets, hand-knitted woolen shawls, and pure organic forest honey from local markets. Food & Cafes: Savour traditional Jadoh (red rice dish), hot smoked pork skewers, local Sohphlang salads, and organic cinnamon-infused mountain teas at boutique cafes in Shillong.', 12)
        ],
        moods=['Adventure', 'Nature', 'Luxury'],
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
        tagline='Caving Meghalaya',
        overview="CAVING MEGHALAYA • THE SUBTERRANEAN CHRONICLES & MYSTIC HILLS Welcome to a spellbinding expedition into the Abode of Clouds, curated precisely by TRAGUIN. Embark on the ultimate Meghalaya Adventure Tour, designed to take you beneath the earth's crust into majestic Cretaceous limestone mazes and across rugged, moss-covered rainforests. As your elite travel consultants, TRAGUIN elevates your thrill-seeking exploration into a seamless luxury holiday complete with premium stays, exceptional technical guiding, and profound wilderness encounters. From the mist-kissed ridges of Cherrapunjee to the deepest cavern corridors of Krem Mawmluh, every segment ensures a premium Meghalaya experience designed to script unforgettable memories.\n\nTOUR OVERVIEW\nThis custom-tailored adventure route offers a fine-tuned balance between high-end adrenaline, cave exploration, pristine river sports, and premium comfort. Travelling in a dedicated private luxury SUV driven by an expert mountain chauffeur-guide, you will navigate breathtaking landscapes with total ease. Your journey features a carefully balanced meal plan consisting of hearty breakfasts and signature evening feasts. Every moment includes a unique TRAGUIN curated experience note, from VIP caving equipment arrangements and specialized speleology guides to handpicked boutique hotels and secluded eco-luxury tented riverside lounges.\n\nWHY BOOK THE BEST MEGHALAYA TOUR PACKAGE?\nMeghalaya is globally renowned for hosting some of the longest and deepest cave systems in the Indian subcontinent. Choosing a specialized Luxury Meghalaya Holiday allows bold explorers to safely discover secret underworld rivers, colossal stalactite galleries, and fossilized rock floors. This is not just standard Meghalaya sightseeing; it is an intimate dive into the untamed heart of the East Khasi and Jaintia Hills. For couples and modern explorers seeking an experiential Meghalaya Honeymoon Package or an action- packed Meghalaya Family Tour, the region offers stunningly raw, popular Instagram locations. Discover the living root bridges of Cherrapunjee, stand on the bamboo skywalks of Mawryngkhang, or drift over the glass- like waters of Dawki. Our custom TRAGUIN Meghalaya Packages combine wild underground thrill with",
        seo_title='ML-009 | Caving Meghalaya | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Meghalaya package (ML-009 / TRG-MEG-009): Shillong • Cherrapunjee • Mawsmai • Mawryngkhang • Shnongpdeng with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: GUWAHATI TO SHILLONG', 1),
            _ih('Day 02: SHILLONG TO CHERRAPUNJEE (SOHRA)', 2),
            _ih('Day 03: CAVING EXPERIENCE IN CHERRAPUNJEE', 3),
            _ih('Day 04: THE MAWRYNGKHANG BAMBOO TREK', 4),
            _ih('Day 05: SHNONGPDENG TO DAWKI & BACK TO SHILLONG', 5),
            _ih('Day 06: SHILLONG TO GUWAHATI / DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private caving trails led by certified national speleological instructors.', 7),
            _ih('Curated by TRAGUIN Experts: Custom timing schedules to explore popular locations ahead of general', 8),
            _ih('Premium Handpicked Hotels: Accommodations chosen for their spectacular locations, top safety', 9)
        ],
        days=[
            _day(
                1,
                'GUWAHATI TO SHILLONG',
                (
                    'THE GATEWAY TO THE CLOUD KINGDOM & HIGHLAND VIBES Your premium Meghalaya experience takes flight upon arrival at Guwahati Airport, where your personal luxury SUV and driver await. Ascend into the rolling green Khasi hills, stopping along the scenic route to appreciate the vast expanse of Umiam Lake (Barapani), a breathtaking landscape perfect for photography points. Arrive in Shillong, the capital, and check into your handpicked premium stay. Spend your evening exploring the lively cafes, local boutiques, and indie music scenes of Police Bazar.'
                ),
                [
                    'Sightseeing Included: Umiam Lake viewpoint, Shillong peak panorama ambiance.',
                    'Evening Experience: Fine dining and live jazz music at an upscale lounge recommended by TRAGUIN experts.',
                    'Overnight Stay: Shillong (Boutique Luxury Hotel / Resort)',
                    'Meals Included: Welcome Drink & Gourmet Dinner',
                ],
            ),
            _day(
                2,
                'SHILLONG TO CHERRAPUNJEE (SOHRA)',
                (
                    'MAWPHLANG SACRED GROVE & CRADLE OF THE RAINFOREST After a lavish morning breakfast, drive towards Mawphlang to explore its centuries-old Sacred Grove. Learn about ancient Khasi tribal folklore during a guided walk under the canopy. Continue along the dramatic gorge- side routes toward Cherrapunjee, stopping to witness the plunging majesty of the Elephant Falls and Mawkdok Dympep Valley Viewpoint. Arrive at your luxury clifftop resort in Cherrapunjee by sunset to view the mist drifting dynamically across the hills.'
                ),
                [
                    'Sightseeing Included: Mawphlang Sacred Grove, Elephant Falls, Mawkdok Dympep Valley.',
                    'Optional Activities: Zip-lining across the deep Mawkdok valley gap (weather permitting).',
                    'Overnight Stay: Cherrapunjee (Premium Cliff-view Luxury Resort)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'CAVING EXPERIENCE IN CHERRAPUNJEE',
                (
                    'SUBTERRANEAN CAVING MEGHALAYA & ICONIC WATERFALLS Gear up for an adrenaline-fueled day of caving in Meghalaya. Don your specialized jumpsuits, helmets, and headlamps as professional speleologists lead you into the fascinating depths of the Mawsmai and Arwah Caves, known for their stunning limestone pillars and ancient crustacean fossils. For those seeking advanced adventure, navigate the underground river streams of Krem Mawmluh. Emerge back into the sunlight to witness the majestic Nohkalikai Falls and Seven Sisters Falls.'
                ),
                [
                    'Sightseeing Included: Mawsmai Cave, Arwah Fossil Cave, Krem Mawmluh (selective zone), Nohkalikai Falls.',
                    'Evening Experience: Private bonfire night with customized local culinary treats organized at your resort.',
                    'Overnight Stay: Cherrapunjee (Premium Cliff-view Luxury Resort)',
                    'Meals Included: Breakfast & Traditional Khasi Style Dinner',
                ],
            ),
            _day(
                4,
                'THE MAWRYNGKHANG BAMBOO TREK',
                (
                    'WALKING THE MOST ADVENTUROUS SKYWALK IN INDIA Embark early on a highly searched adventure to Wahkhen village, the starting point of the legendary Mawryngkhang Bamboo Trek. Walk along a magnificent bamboo pathway engineered by local artisans, pinned securely against sheer vertical cliff faces over roaring river canyons. This trek provides incredible mountain vistas and stands out as a popular Instagram location for elite thrill-seekers. After the trek, enjoy a smooth luxury drive down to the peaceful river border town of Shnongpdeng.'
                ),
                [
                    'Sightseeing Included: Mawryngkhang Rock Skywalk trail, Umngot River entry banks.',
                    'Evening Experience: Riverside camp barbecue lounge under a clear, starlit sky.',
                    'Overnight Stay: Shnongpdeng (Luxury Glamping / Premium Eco-Lodge)',
                    'Meals Included: Breakfast & Hot Tented Buffet Dinner',
                ],
            ),
            _day(
                5,
                'SHNONGPDENG TO DAWKI & BACK TO SHILLONG',
                (
                    'CRYSTAL RIVER WATER SPORTS & IMMERSIVE ECO-ADVENTURE Awake to the peaceful sound of the pristine Umngot River in Shnongpdeng. Experience the unique sensation of floating over glass-like water during an exclusive morning boating session. Adventure lovers can enjoy cliff jumping, river kayaking, or scuba diving in crystal clear pools. In the afternoon, journey past Dawki toward the exceptionally clean village of Mawlynnong, before driving back up to Shillong for your final evening. village.'
                ),
                [
                    'Sightseeing Included: Umngot River suspension bridge, Dawki international border viewpoint, Mawlynnong',
                    'Optional Activities: Snorkeling, deep-pool kayaking, or local treehouse walks.',
                    'Overnight Stay: Shillong (Boutique Luxury Hotel / Resort)',
                    'Meals Included: Breakfast & Farewell Premium Dinner',
                ],
            ),
            _day(
                6,
                'SHILLONG TO GUWAHATI / DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Indulge in a relaxing breakfast at your premium hotel while admiring the beautiful hills. Pack your adventure gear as your private luxury SUV transfers you smoothly back to Guwahati Airport. Bid a fond farewell to the Northeast, carrying home thrilling stories and unforgettable memories crafted seamlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door airport highway drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Centre Point / similar | Sohra Plaza / similar | Standard Eco Comfort Lodge',
                'Shillong | Cherrapunjee | Shnongpdeng',
                '2N Shillong|2N Cherrapunjee|1N Shnongpdeng',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Centre Point / similar | Sohra Plaza / similar | Standard Eco Comfort Lodge | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Mawiandun Boutique / similar | Jiva Resort / similar | Premium Riverside Glamping Tents',
                'Shillong | Cherrapunjee | Shnongpdeng',
                '2N Shillong|2N Cherrapunjee|1N Shnongpdeng',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Mawiandun Boutique / similar | Jiva Resort / similar | Premium Riverside Glamping Tents | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Ri Kynjai Serenity By The Lake | Polo Orchid Resort (Log Cabin) | Bespoke Eco-Luxury Tented Suites',
                'Shillong | Cherrapunjee | Shnongpdeng',
                '2N Shillong|2N Cherrapunjee|1N Shnongpdeng',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Ri Kynjai Serenity By The Lake | Polo Orchid Resort (Log Cabin) | Bespoke Eco-Luxury Tented Suites | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Ri Kynjai (Luxury Heritage Cottage) | Polo Orchid (Presidential Villa with Pool) | VIP Private Custom Riverside Cottage',
                'Shillong | Cherrapunjee | Shnongpdeng',
                '2N Shillong|2N Cherrapunjee|1N Shnongpdeng',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Ri Kynjai (Luxury Heritage Cottage) | Polo Orchid (Presidential Villa with Pool) | VIP Private Custom Riverside Cottage | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 05 Nights in top-rated boutique properties and luxury camps.', 1),
            _inc_included('Luxury Transportation: Private AC SUV for all transfers and sightseeing tours.', 2),
            _inc_included('Curated Meal Plan: Daily luxury breakfasts and custom dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated adventure concierge officer on call.', 4),
            _inc_included('Caving Amenities: Safety helmets, headlamps, and jumpsuits for specified caves.', 5),
            _inc_included('Complimentary Experience: Private country boat cruise on the clear Umngot River.', 6),
            _inc_excluded('Airfare, flight routing, or railway tickets to Guwahati.', 7),
            _inc_excluded('Advanced scuba diving, cliff jumping, or zip-line operational tickets.', 8),
            _inc_excluded('Personal items, laundry expenses, alcoholic drinks, and gratuities.', 9),
            _inc_excluded('Any mandatory travel insurance or medical evacuation costs.', 10),
        ],
    )
    return package, itinerary

def build_ml_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ML-010'
    tour_code = 'TRG-MEG-010'
    title = 'Complete Meghalaya Explorer • Symphony of Clouds & Cascades'
    duration = '07 Nights / 08 Days'
    slug = 'ml-010-complete-meghalaya-explorer-symphony-of-clouds-cascades'
    itin_slug = 'ml-010-complete-meghalaya-explorer-symphony-of-clouds-cascades-itinerary'
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
            _ph('Serial code ML-010 | TRAGUIN tour code TRG-MEG-010', 1),
            _ph('State / Country: Meghalaya / India | Category: Premium Family', 2),
            _ph('Destinations: Shillong • Cherrapunjee • Mawlynnong • Dawki • Jowai', 3),
            _ph('Ideal for: Family Getaways, Nature Admirers & Luxury Travelers', 4),
            _ph('Best season: October to May (Pleasant Cascades & Clear Skies)', 5),
            _ph('Starting price: On Request (Bespoke Curated Family Pricing)', 6),
            _ph('Vehicle / Meals: Private Luxury SUV (Innova Crysta) / MAPAI Plan', 7),
            _ph('TRAGUIN Signature Experience: Private family tea picnic at the edge of the Laitlum Canyons with a', 8),
            _ph('Curated by TRAGUIN Experts: Smartly planned itinerary keeping comfortable travel distances for elders', 9),
            _ph('Premium Handpicked Hotels: Properties chosen specifically for exceptional service, beautiful room', 10),
            _ph('Luxury Transportation: Expert high-altitude chauffeurs specializing in managing unpredictable weather', 11),
            _ph('Local Handloom & Crafts: Head to Shillong’s local shops to find magnificent Khasi bamboo baskets, handmade organic scrubs, pure orange blossom flower honey, and fine hand-woven wild Eri silk stoles. Cafes & Food: Shillong boasts a vibrant musical culture; spend an evening inside a cozy cafe enjoying local smoked pork recipes, traditional Jadoh rice meals, and exceptional live jazz performances.', 12)
        ],
        moods=['Family', 'Nature', 'Luxury'],
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
        tagline='Complete Meghalaya Explorer',
        overview="COMPLETE MEGHALAYA EXPLORER • SYMPHONY OF CLOUDS & CASCADES Welcome to an unforgettable escape into the Abode of Clouds, carefully conceptualized and managed by TRAGUIN. Embark on the absolute Best Meghalaya Tour Package, designed purposefully to show your loved ones the breathtaking landscapes, hidden caves, crystalline rivers, and living root structures of Northeast India. As your dedicated corporate travel consultants, TRAGUIN delivers a flawlessly integrated luxury holiday overflowing with premium stays, deep cultural storytelling, and immersive experiences. Treat your loved ones to the scenic beauty of emerald valleys and majestic mist-shrouded monoliths, forging timeless, beautiful memories together.\n\nTOUR OVERVIEW\nThis exhaustive, highly curated family vacation provides an ideal mix of colonial old-world charm, untouched sub-tropical nature reserves, sacred cultural forests, and mirror-clear river waters. Travelling in an exclusive, high-ground-clearance luxury SUV under the care of a skilled local chauffeur-guide, your family travels in absolute serenity. With a detailed, robust dining plan featuring lavish breakfasts and specialized, warm dinners at each retreat, this route highlights the pinnacle of a premium Meghalaya experience. Each phase of the journey comes backed by our signature TRAGUIN curated experience note, providing seamless private entries, curated gourmet stopovers, and 24/7 localized support.\n\nWHY CHOOSE THE BEST MEGHALAYA TOUR PACKAGE?\nWhen considering a Luxury Meghalaya Holiday, elite travelers demand an itinerary that seamlessly links rugged natural spectacles with polished, warm accommodations. Meghalaya hosts some of the most iconic attractions in Asia. From Cherrapunjee—world-renowned for its thunderous waterfalls and massive limestone cavern complexes—to the famous Umngot River at Dawki, which stands out as a world-class tourist place for boating, Meghalaya sightseeing promises incredible visual rewards. For couples and larger groups requesting a dedicated Meghalaya Honeymoon Package or an expansive Meghalaya Family Tour, the region offers incredibly popular Instagram locations such as the Double Decker Living Root Bridge of Nongriat, the clean pathways of Mawlynnong (Asia's Cleanest Village), and the dramatic canyon edge of Laitlum Canyons. From exploring local bamboo crafts to enjoying authentic Khasi culinary platters, our specialized TRAGUIN Meghalaya Packages ensure custom-selected premium hotels and exclusive experiences that capture the best time to visit Meghalaya.",
        seo_title='ML-010 | Complete Meghalaya Explorer | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Meghalaya package (ML-010 / TRG-MEG-010): Shillong • Cherrapunjee • Mawlynnong • Dawki • Jowai with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GUWAHATI TO SHILLONG', 1),
            _ih('Day 02: SHILLONG LOCAL SIGHTSEEING', 2),
            _ih('Day 03: SHILLONG TO CHERRAPUNJEE (SOHRA)', 3),
            _ih('Day 04: CHERRAPUNJEE – NONGRIAT TREK OR LEISURE DAY', 4),
            _ih('Day 05: CHERRAPUNJEE TO MAWLYNNONG TO DAWKI', 5),
            _ih('Day 06: DAWKI TO JOWAI (JAINTIA HILLS) TO SHILLONG', 6),
            _ih('Day 07: SHILLONG SACRED GROVE EXCURSION (MAWPHLANG)', 7),
            _ih('Day 08: SHILLONG TO GUWAHATI / DEPARTURE', 8),
            _ih('TRAGUIN Signature Experience: Private family tea picnic at the edge of the Laitlum Canyons with a', 9),
            _ih('Curated by TRAGUIN Experts: Smartly planned itinerary keeping comfortable travel distances for elders', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GUWAHATI TO SHILLONG',
                (
                    'JOURNEY TO THE SCOTLAND OF THE EAST – SCENIC RIVERSIDES & UMIAM LAKE Your premium Meghalaya experience starts as you arrive at Guwahati Airport/Station. Meet your dedicated private luxury vehicle chauffeur and begin a gorgeous uphill journey towards Shillong. Pass through verdant pine hills and pause at the majestic Umiam Lake (Barapani), a massive, tranquil body of water offering breathtaking landscapes and awesome photography points. Arrive in Shillong, check into your handpicked premium luxury property, and spend a relaxing evening exploring the dynamic Police Bazar for early souvenir hunting. TRAGUIN experts.'
                ),
                [
                    'Sightseeing Included: Umiam Lake Panoramic Viewpoint, Pine Valley highway drive, Police Bazar walk.',
                    'Evening Experience: Gourmet dinner featuring fusion North-Eastern and continental courses curated by',
                    'Overnight Stay: Shillong (Premium Boutique Hotel Resort)',
                    'Meals Included: Welcome Mocktail & Gourmet Dinner',
                ],
            ),
            _day(
                2,
                'SHILLONG LOCAL SIGHTSEEING',
                (
                    'CULTURE, HERITAGE & THE LAITLUM CANYON AMPHITHEATER Relish a fine breakfast before plunging into a rich Shillong sightseeing tour. Stand at the edge of the Laitlum Canyons, an expansive gorge often draped in dramatic mist, widely ranked among the most breathtaking popular Instagram locations in the state. Return to the town to explore the multi-tiered Elephant Falls, the meticulously curated Don Bosco Museum of Indigenous Cultures, and take a peaceful walk around Ward’s Lake. (Subject to permissions).'
                ),
                [
                    "Sightseeing Included: Laitlum Canyons, Elephant Falls, Don Bosco Museum, Ward's Lake, Shillong Peak",
                    'Optional Activities: Private traditional archery gambling match viewing (Teer) or high-end local cafe hopping.',
                    'Overnight Stay: Shillong (Premium Boutique Hotel Resort)',
                    'Meals Included: Premium Breakfast & Luxury Dinner',
                ],
            ),
            _day(
                3,
                'SHILLONG TO CHERRAPUNJEE (SOHRA)',
                (
                    "MIST-VEILED REBELS & PLUNGING GIANT WATERFALLS Check out after breakfast and take the spectacular mist-laden mountain highway towards Cherrapunjee (Sohra). En route, step onto the Mawkdok Dympep Valley Bridge to witness grand, expansive views. Visit the incredible, roaring Nohkalikai Falls—India's tallest plunge waterfall—steeped in moving local tribal legends. Explore the massive, illuminated limestone chambers of Mawsmai Cave to experience the ancient geological heritage of Meghalaya. Falls."
                ),
                [
                    'Sightseeing Included: Mawkdok Valley Viewpoint, Nohkalikai Falls, Mawsmai Cave, Eco Park, Seven Sisters',
                    'Evening Experience: Private sunset tea service on a luxury resort lawn overlooking the plains of Bangladesh.',
                    'Overnight Stay: Cherrapunjee (Premium Eco-Luxury Valley Resort)',
                    'Meals Included: Premium Breakfast & Luxury Platter Dinner',
                ],
            ),
            _day(
                4,
                'CHERRAPUNJEE – NONGRIAT TREK OR LEISURE DAY',
                (
                    'THE LIVING ROOT SYMPHONY – AN ANCIENT BIOLOGICAL MARVEL An incredible day packed with immersive experiences. True adventure enthusiasts can embark on a guided trek down 3,000 stone steps to see the world-famous Double Decker Living Root Bridge in Nongriat village, an unforgettable feat of bio-engineering by the Khasi elders. For family members seeking a relaxed pace, an alternative itinerary explores the serene Wei Sawdong three-tiered falls and the ancient, deep Arwah Caves, known for hidden prehistoric fossils. guide.'
                ),
                [
                    'Sightseeing Included: Nongriat Double Decker Living Root Bridge OR Wei Sawdong Falls & Arwah Cave.',
                    'Optional Activities: Natural crystal pool swimming at the base of the living roots with a dedicated local trek',
                    'Overnight Stay: Cherrapunjee (Premium Eco-Luxury Valley Resort)',
                    'Meals Included: Premium Breakfast & Hearty Mountain Dinner',
                ],
            ),
            _day(
                5,
                'CHERRAPUNJEE TO MAWLYNNONG TO DAWKI',
                (
                    "ASIA'S CLEANEST VILLAGE & THE MIRROR-CLEAR CRYSTAL RIVER Depart early along the Southern Ridge towards Mawlynnong, celebrated as Asia's Cleanest Village. Take a peaceful family walk across manicured, flower-lined pathways and explore a single-tier living root bridge at Riwai village. In the afternoon, head to Dawki, where the legendary Umngot River flows with water so pristine and transparent that boats seem to float effortlessly in mid-air. Enjoy an exclusive private boating cruise across this international border waterbody. Bangladesh Border point. barbecue."
                ),
                [
                    'Sightseeing Included: Mawlynnong Village, Riwai Living Root Bridge, Sky View Tower, Dawki Umngot River, Indo-',
                    'Evening Experience: Private luxury riverside camping ambiance setup with premium dynamic lighting and a light',
                    'Overnight Stay: Dawki (Premium Luxury Glamping Tents) OR Luxury Day-return to Shillong property.',
                    'Meals Included: Premium Breakfast & Riverside Fusion Dinner',
                ],
            ),
            _day(
                6,
                'DAWKI TO JOWAI (JAINTIA HILLS) TO SHILLONG',
                (
                    'THE ENCHANTED JAINTIA KINGDOM – KRANG SURI SAPPHIRE POOLS Drive north through the Jaintia Hills to discover the magical town of Jowai. Visit the iconic Krang Suri Falls, universally considered the most stunning tourist place in Meghalaya for its turquoise sapphire water pool nestled deep inside a dense jungle grove. Capture breathtaking photographs along the stone bridges of Tyrshi Falls before heading back up to Shillong for your final luxury holiday stay. Suri.'
                ),
                [
                    'Sightseeing Included: Krang Suri Falls, Thadlaskein Lake, Tyrshi Falls viewpoint.',
                    'Optional Activities: Life jacket rentals for an immersive swimming experience in the natural pools of Krang',
                    'Overnight Stay: Shillong (Premium Heritage Resort Stay)',
                    'Meals Included: Premium Breakfast & Traditional Jaintia Dinner Accent',
                ],
            ),
            _day(
                7,
                'SHILLONG SACRED GROVE EXCURSION (MAWPHLANG)',
                (
                    "ANCIENT KHASI MYSTICISM & SACRED FOREST SECRETS Dedicate your final exploration day to the mysterious Mawphlang Sacred Grove. Walk into an ancient, preserved forest patch accompanied by a local tribal elder. Learn about centuries-old nature conservation habits, spiritual offering altars, and deep medicinal plants. It's an emotionally rich, immersive experience for the entire family. Spend your final afternoon picking up exceptional local souvenirs and handicrafts."
                ),
                [
                    'Sightseeing Included: Mawphlang Sacred Grove guided walk, Khasi Heritage Village, Elephant Falls re-visit.',
                    'Evening Experience: Grand Farewell Dinner curated by TRAGUIN experts celebrating your family bond.',
                    'Overnight Stay: Shillong (Premium Heritage Resort Stay)',
                    'Meals Included: Premium Breakfast & Elite Farewell Dinner',
                ],
            ),
            _day(
                8,
                'SHILLONG TO GUWAHATI / DEPARTURE',
                (
                    'CARRYING HOME CHERISHED MEMORIES BEYOND DESTINATIONS Enjoy a final morning buffet breakfast at your heritage resort. Board your comfortable private luxury SUV for a smooth downhill drive back to Guwahati Airport or Railway Station. Return home carrying a heart full of joy, deep cultural discoveries, and unforgettable memories designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private airport terminal door drop-off service.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Polo Towers / M-Crown / similar | Cherrapunjee Holiday Resort / similar',
                'Shillong | Cherrapunjee',
                '5N Shillong|2N Cherrapunjee',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Daily Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Polo Towers / M-Crown / similar | Cherrapunjee Holiday Resort / similar | MAPAI (Daily Breakfast & Dinner)',
            ),
            _hotel(
                'Rigal Heritage / Pinewood Hotel / similar | Sohra Plaza Resort / Jiva Resort (Executive)',
                'Shillong | Cherrapunjee',
                '5N Shillong|2N Cherrapunjee',
                'Premium',
                'Deluxe Room',
                'MAPAI (Premium Selected Dining)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Rigal Heritage / Pinewood Hotel / similar | Sohra Plaza Resort / Jiva Resort (Executive) | MAPAI (Premium Selected Dining)',
            ),
            _hotel(
                'Ri Kynjai Serenity Lake Resort / Similar | Jiva Resort (Luxury Suite) / Polo Orchid Resort',
                'Shillong | Cherrapunjee',
                '5N Shillong|2N Cherrapunjee',
                'Luxury',
                'Deluxe Room',
                'MAPAI + Welcome Premium Amenities',
                5,
                3,
                description='OPTION 03 – LUXURY: Ri Kynjai Serenity Lake Resort / Similar | Jiva Resort (Luxury Suite) / Polo Orchid Resort | MAPAI + Welcome Premium Amenities',
            ),
            _hotel(
                'Ri Kynjai (Luxury Cottage Overlooking Lake) | Polo Orchid (Log Cabin With Plunge Pool)',
                'Shillong | Cherrapunjee',
                '5N Shillong|2N Cherrapunjee',
                'Ultra Luxury',
                'Deluxe Room',
                'Bespoke Custom Signature VVIP Dining',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Ri Kynjai (Luxury Cottage Overlooking Lake) | Polo Orchid (Log Cabin With Plunge Pool) | Bespoke Custom Signature VVIP Dining',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 07 Nights in top-rated, handpicked hotels & eco-resorts.', 1),
            _inc_included('Luxury Transportation: Private dedicated Innova Crysta SUV for entire routing.', 2),
            _inc_included('Curated Meal Plan: Daily lavish buffet breakfasts and premium warm multi-course dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 localized guest experience executive and ground coordination.', 4),
            _inc_included('Welcome Privileges: Personalized fruit baskets, tribal sweets, and family travel kits.', 5),
            _inc_included('Complimentary Experience: Reserved private boating tour on the crystal-clear Dawki river.', 6),
            _inc_excluded('Airfare, domestic flight connections, or broad railway booking tickets.', 7),
            _inc_excluded('Local guide tips, monument entrance charges, and individual cave camera fees.', 8),
            _inc_excluded('Adventure costs such as zip-lining at Cherrapunjee or cliff jumping at Dawki.', 9),
            _inc_excluded('Personal expenses including laundry, telephone calls, liquor, or optional safari detours.', 10),
        ],
    )
    return package, itinerary

MEGHALAYA_DOMESTIC_BUILDERS = [
    build_ml_001,
    build_ml_002,
    build_ml_003,
    build_ml_004,
    build_ml_005,
    build_ml_006,
    build_ml_007,
    build_ml_008,
    build_ml_009,
    build_ml_010,
]
