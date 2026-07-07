"""Builder functions for AR-001 through AR-010 Arunachal Pradesh domestic packages."""

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

ARUNACHAL_PRADESH_SLUG = "arunachal-pradesh"


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


def build_ar_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AR-001'
    tour_code = 'TG-AR-TE-001'
    title = 'TRAGUIN Premium Arunachal Pradesh Tour Package — Tawang Escape: Bhalukpong • Dirang • Tawang'
    duration = '05 Nights / 06 Days'
    slug = 'ar-001-tawang-escape-bhalukpong-dirang-tawang'
    itin_slug = 'ar-001-tawang-escape-bhalukpong-dirang-tawang-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Arunachal Pradesh / India | Category: Luxury Family Holiday Package', 2),
            _ph('Destinations: Guwahati • Bhalukpong • Dirang • Tawang', 3),
            _ph('Ideal for: Families, Nature Enthusiasts, Photography Lovers', 4),
            _ph('Best season: March to June & October to December', 5),
            _ph('Starting price: On Request (Premium Luxury Tier)', 6),
            _ph('Vehicle: Private AC SUV (Toyota Innova Crysta / Scorpio Cross) | Meal Plan: Premium Breakfast & Dinner (MAPAI)', 7),
            _ph('Route Plan: Guwahati ➔ Bhalukpong (1N) ➔ Dirang (1N) ➔ Tawang (3N) ➔ Guwahati Departure', 8),
            _ph('TRAGUIN Curated Experience Note: Private high-altitude sunrise picnic near pristine glacial lakes, aromatic traditional butter-tea tasting inside an authentic Monpa tribal home, and a private blessing ceremony at Tawang Monastery.', 9),
            _ph('TRAGUIN Signature Experience: Private morning family blessing ceremony led by senior lamas inside the sacred Tawang Monastery.', 10),
            _ph('Curated by TRAGUIN Experts: Every resort room, heating system, and professional mountain driver is rigorously vetted to guarantee premium safety and luxury for families.', 11),
            _ph('Personalized Assistance: Dedicated 24/7 holiday consultant assigned specifically to your family from booking until your return flight.', 12),
            _ph('Premium Handpicked Hotels: Stay at incredible properties, ranging from beautiful valley resorts in Dirang to luxury rooms at Vivanta Tawang.', 13),
            _ph('Shopping & Local Experiences: Monpa Carpets & Paper, piping-hot local momos, authentic butter tea, Tibetan curios at Tawang market.', 14),
            _ph('Important Notes: Inner Line Permits mandatory; Tawang at 10,000 ft and Sela Pass at 13,700 ft; book 60–90 days ahead for peak seasons.', 15),
        ],
        moods=['Family', 'Luxury', 'Nature', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Tawang Escape • Bhalukpong • Dirang • Tawang • 05 Nights / 06 Days',
        overview=(
            'Welcome to the Land of the Dawn-Lit Mountains. The Best Arunachal Pradesh Tour Package, envisioned and designed exclusively by TRAGUIN, invites your family to step into a paradise of pure alpine beauty, mist-laden valleys, and ancient spiritual landmarks. This pristine and highly customized Arunachal Pradesh Family Tour connects the lush lowland foothills with the soaring, snowy ridges of the Eastern Himalayas.\n\n'
            'TOUR OVERVIEW\nThis premium Arunachal Pradesh Family Tour delivers a magnificent experience of pristine high-altitude geography. Families enjoy seamless private ground transportation inside a heavy-duty, high-clearance luxury 4x4 or spacious premium vehicle suited to high mountain routes, handpicked hotels matching highest regional comfort tiers, expert storytelling local guides, and seamless coordination of required Inner Line Permits (ILP).\n\n'
            'WHY CHOOSE THE PREMIUM ARUNACHAL PRADESH EXPERIENCE?\nA journey through Northeast India is incomplete without experiencing the pristine mountain roads of Tawang. Celebrated for hosting the most diverse Top Tourist Places in Arunachal Pradesh, this tour provides an unforgettable blend of relaxation, adventure, and history.'
        ),
        seo_title='AR-001 | Tawang Escape Bhalukpong Dirang Tawang | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Arunachal family package (AR-001 / TG-AR-TE-001): Bhalukpong, Dirang, Sela Pass, Tawang Monastery, Madhuri Lake, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Scenic Kameng River drive and Bhalukpong entry gateway on Day 01', 1),
            _ih('Tipi Orchid Sanctuary, Dirang Dzong, and apple orchards on Day 02', 2),
            _ih('Sela Pass (13,700 ft), Sela Lake, and Jaswant Garh War Memorial on Day 03', 3),
            _ih('Tawang Monastery private blessing ceremony and War Memorial Light & Sound Show', 4),
            _ih('Madhuri Lake, PTSO Lake, and Nuranang Falls excursion on Day 05', 5),
        ],
        days=[
            _day(1, 'GUWAHATI TO BHALUKPONG — ENTRY INTO THE PRISTINE FOOTHILLS', ('Your premium family mountain escape begins as you arrive at Guwahati Airport or Railway Station. You are warmly received by your dedicated TRAGUIN professional chauffeur with custom welcoming kits. Settle inside your high-clearance private vehicle and leave the plains behind as you embark on a highly scenic driving route heading toward Bhalukpong, the scenic entry gateway to Arunachal Pradesh located on the banks of the rushing Kameng River. Watch the landscape transform from wide river valleys into dense subtropical evergreen forests. Upon arrival, check into your handpicked premium riverside lodge. After a seamless check-in, spend a relaxed evening walking along the river banks or relaxing amidst the peaceful lawns. Enjoy a fresh gourmet dinner featuring local organic mountain herbs.'), [
                'Sightseeing Included: Scenic Kameng River drive, Bhalukpong entry gates, Jia Bharali view.',
                'Evening Experience: Relaxed riverside walk at sunset.',
                'Meals Included: Welcome Signature Drink & Gourmet Multi-cuisine Dinner.',
                'Overnight Stay: Premium Riverside Lodge, Bhalukpong.',
            ]),
            _day(2, 'BHALUKPONG TO DIRANG — WINDING VALLEYS & APPLE ORCHARDS', ('Awake to the refreshing mountain mist. After a hearty breakfast, continue your premium Arunachal Pradesh Sightseeing trail, ascending higher into the hills toward the beautiful Dirang Valley. Enjoy an immersive driving experience as the road weaves through deep mountain gorges and orchid sanctuaries. Stop at the spectacular Tipi Orchid Research Centre to view hundreds of rare, colorful exotic orchid species. Arrive in Dirang, a picturesque valley located at 4,900 feet. Check into your boutique mountain resort. In the afternoon, explore the Dirang Dzong, an ancient 17th-century Monpa tribal fort village with fascinating stone architecture. Walk hand-in-hand through premium organic apple orchards and kiwi plantations before returning to your resort for a cozy dinner.'), [
                'Sightseeing Included: Tipi Orchid Sanctuary, Dirang Dzong historical village, Apple orchards.',
                'Evening Experience: Relaxing by a warm outdoor fireplace overlooking the valley.',
                'Meals Included: Buffet Breakfast & Specially Prepared Himalayan Dinner.',
                'Overnight Stay: Handpicked Premium Mountain Resort, Dirang.',
            ]),
            _day(3, 'DIRANG TO TAWANG — OVER SELA PASS TO THE LAND OF MYSTIC MONASTERIES', ('A phenomenal and unforgettable day awaits your family. After an early breakfast, begin your ascent toward the magical high-altitude town of Tawang. Your luxury vehicle winds up the dramatic mountain roads, reaching the world-famous Sela Pass at an astonishing 13,700 feet. Gaze in absolute awe at the breathtaking landscapes of snowy peaks and the frozen, sacred Sela Lake. Thousands of colorful Tibetan prayer flags dance in the crisp mountain wind—a supreme spot for family photography. Descend into the valley, stopping at the historic Jaswant Garh War Memorial to pay an emotional tribute to the legendary bravery of Indian soldiers. Continue your drive, passing past cascading waterfalls, until the yellow roofs of Tawang appear on the horizon. Check into your ultra-luxury room and enjoy a customized warm welcome dinner.'), [
                'Sightseeing Included: Sela Pass (13,700 Ft), Sela Lake, Jaswant Garh War Memorial.',
                'Evening Experience: Traditional Monpa welcome cake and local warm tea at the resort.',
                'Meals Included: Breakfast, Hot Mountain Snacks, & Gourmet Dinner.',
                'Overnight Stay: Premium Luxury Hotel, Tawang.',
            ]),
            _day(4, 'TAWANG — THE MAJESTIC MONASTERY & SPIRITUAL GEMS', ('Savor a luxurious breakfast enveloped by crisp mountain air. Today is dedicated to experiencing the timeless spiritual wonders of your Tawang Escape. Visit the legendary Tawang Monastery, the second-largest Buddhist monastery in the world, founded in the 17th century. Marvel at the colossal 26-foot golden Buddha statue inside the main prayer hall. Enjoy a TRAGUIN Curated Experience: a private morning blessing ceremony arranged with the senior lamas for your family\'s well-being. Next, explore the peaceful Urgelling Monastery, the birthplace of the 6th Dalai Lama. In the afternoon, stroll through the local crafts emporium to witness traditional hand-made paper making and exquisite Monpa carpet weaving. In the evening, attend the moving Light & Sound Show at the Tawang War Memorial, celebrating local history and valor.'), [
                'Sightseeing Included: Tawang Monastery, Urgelling Monastery, Craft Centre, Ani Gompa.',
                'Evening Experience: VIP tickets to the Tawang War Memorial Light & Sound Show.',
                'Meals Included: Gourmet Breakfast & Multi-cuisine Chef\'s Table Dinner.',
                'Overnight Stay: Premium Luxury Hotel, Tawang.',
            ]),
            _day(5, 'TAWANG — HIGH-ALTITUDE GLACIAL LAKES & HOLLYWOOD ECHOES', ('Wake up early for an extraordinary excursion toward the high-altitude border plateau. Travel past alpine meadows to visit the breathtaking Madhuri Lake (Shonga-tser Lake), surrounded by rocky mountains and dead tree trunks emerging from the water—a cinematic wonder. Enjoy a TRAGUIN Signature Experience: a premium packed picnic breakfast served on the shores of the lake. On your drive back, pass the beautiful PTSO Lake and stop at the thunderous Nuranang Falls (Jang Falls), where a massive white torrent drops 100 meters down a sheer mountain cliff. Capture incredible photographs before returning to Tawang for a grand family farewell dinner.'), [
                'Sightseeing Included: Madhuri Lake, PTSO Lake, Nuranang Waterfalls (Jang Falls).',
                'Evening Experience: Grand farewell bonfire with an authentic local Monpa dinner menu.',
                'Meals Included: Lakeside Picnic Breakfast & Grand Farewell Dinner.',
                'Overnight Stay: Premium Luxury Hotel, Tawang.',
            ]),
            _day(6, 'TAWANG TO GUWAHATI — DEPARTURE WITH SACRED MEMORIES', ('Indulge in a final hearty breakfast as the morning sun illuminates the snow-capped Himalayan peaks. Complete your check-out and board your luxury private vehicle for a smooth descent back toward Guwahati. Enjoy the sweeping views of valleys and rivers as you journey down from the high altitudes. Depending on your schedule, your private chauffeur will drop you comfortably at the Guwahati Airport or Railway Station for your onward journey home. Your elite family holiday concludes beautifully, leaving you with sacred bonds and unforgettable memories built flawlessly by TRAGUIN.'), [
                'Sightseeing Included: Mountain Descent Drive, Private Departure Transfer.',
                'Meals Included: Premium Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('MPT Prashaanti Lodge | Hotel Pemaling | Hotel Gakyi Khang Zhang', 'Bhalukpong (1 Night) / Dirang (1 Night) / Tawang (3 Nights)', '05 Nights', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner', 4, 1, description='OPTION 01 – DELUXE: MPT Prashaanti Lodge (Bhalukpong, 1 Night) | Hotel Pemaling (Dirang, 1 Night) | Hotel Gakyi Khang Zhang (Tawang, 3 Nights) | Breakfast & Dinner'),
            _hotel('Prashaanti Cottages | Dirang Boutique Cottages | Tawang Heritage Hotel', 'Bhalukpong (1 Night) / Dirang (1 Night) / Tawang (3 Nights)', '05 Nights', 'Premium', 'Premium Room', 'Breakfast & Dinner', 4, 2, description='OPTION 02 – PREMIUM: Prashaanti Cottages (Bhalukpong, 1 Night) | Dirang Boutique Cottages (Dirang, 1 Night) | Tawang Heritage Hotel (Tawang, 3 Nights) | Breakfast & Dinner'),
            _hotel('Luxury Riverside Eco Camp | Avonka Resort Dirang | Vivanta Tawang (Superior)', 'Bhalukpong (1 Night) / Dirang (1 Night) / Tawang (3 Nights)', '05 Nights', 'Luxury', 'Superior / Luxury Room', 'Breakfast & Dinner', 5, 3, description='OPTION 03 – LUXURY: Luxury Riverside Eco Camp (Bhalukpong, 1 Night) | Avonka Resort Dirang (Dirang, 1 Night) | Vivanta Tawang Superior (Tawang, 3 Nights) | Breakfast & Dinner'),
            _hotel('Premium Wilderness Lodge | The Norphel Hotel Dirang | Vivanta Tawang (Luxury Suite)', 'Bhalukpong (1 Night) / Dirang (1 Night) / Tawang (3 Nights)', '05 Nights', 'Ultra Luxury', 'Luxury Suite', 'Breakfast & Dinner', 5, 4, description='OPTION 04 – ULTRA LUXURY: Premium Wilderness Lodge (Bhalukpong, 1 Night) | The Norphel Hotel Dirang (Dirang, 1 Night) | Vivanta Tawang Luxury Suite (Tawang, 3 Nights) | Breakfast & Dinner'),
        ],
        inclusions=[
            _inc_included('Premium Stays: 05 Nights luxury accommodation at our handpicked premium hotels and mountain resorts.', 1),
            _inc_included('Gourmet Dining: Daily buffet breakfasts and curated multi-cuisine dinners at all hotels.', 2),
            _inc_included('Luxury Transportation: Private air-conditioned luxury high-clearance SUV for all transfers, mountain drives, and sightseeing.', 3),
            _inc_included('Permit Coordination: Inner Line Permits (ILP) and required border documentation handled seamlessly by our team.', 4),
            _inc_included('Welcome Amenities: Traditional welcomes at resorts, fresh fruit baskets, and premium mineral water provided daily inside your car.', 5),
            _inc_included('Complimentary Experiences: Private high-altitude lakeside picnic breakfast and an exclusive Tawang Monastery blessing.', 6),
            _inc_included('TRAGUIN Support: 24/7 dedicated concierge assistance from our expert team, with all toll taxes, fuel, parking, and driver allowances fully covered.', 7),
            _inc_excluded('Main Airfare / Rail: Intercity flight or train tickets to and from Guwahati.', 8),
            _inc_excluded('Monument Entry Tickets: Individual entrance fees at museums, light shows, and parks unless stated otherwise.', 9),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, alcoholic drinks, spa sessions, and optional tipping.', 10),
            _inc_excluded('Optional Activities: Extra local excursions or items not specified inside inclusions.', 11),
        ],
    )
    return package, itinerary

def build_ar_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AR-002'
    tour_code = 'TG-AP-BMT-002'
    title = 'TRAGUIN Premium Arunachal Pradesh Tour Package — Mystical Tawang & Bomdila Family Exploration'
    duration = '06 Nights / 07 Days'
    slug = 'ar-002-mystical-tawang-bomdila-family-exploration'
    itin_slug = 'ar-002-mystical-tawang-bomdila-family-exploration-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Arunachal Pradesh / India | Category: Premium Family Tour Package', 2),
            _ph('Destinations: Guwahati • Bomdila • Tawang • Dirang', 3),
            _ph('Ideal for: Families & Nature Lovers', 4),
            _ph('Best season: March - June & October - November', 5),
            _ph('Starting price: On Request (Luxury Tier)', 6),
            _ph('Vehicle: Private AC Luxury SUV (Toyota Innova Crysta) | Meal Plan: Premium Breakfast & Dinner', 7),
            _ph('Route Plan: Guwahati ➔ Bhalukpong Foothills (1N) ➔ Bomdila (1N) ➔ Tawang (3N) ➔ Dirang (1N) ➔ Guwahati Departure', 8),
            _ph('TRAGUIN Curated Experience Note: Private family high-tea experience set up elegantly along the bubbling Dirang River bank.', 9),
            _ph('TRAGUIN Signature Experience: Private family high-tea experience set up elegantly along the bubbling Dirang River bank.', 10),
            _ph('Curated by TRAGUIN Experts: Every transport route, driver profile, and mountain cottage is thoroughly vetted to guarantee absolute safety and comfort.', 11),
            _ph('Personalized Assistance: Elite, dedicated travel specialist assigned to your family from booking until your return flight home.', 12),
            _ph('Premium Handpicked Hotels: Stay at incredible properties, ranging from snow-view valley resorts to boutique heritage estates.', 13),
            _ph('Shopping & Local Experiences: Monpa Traditional Crafts, fresh organic kiwis and apples, warm mountain delicacies, traditional Monpa attire photo spots.', 14),
            _ph('Important Notes: Inner Line Permits require documents 15 days prior; high altitude acclimatization on Day 3; book 45–60 days ahead for peak travel.', 15),
        ],
        moods=['Family', 'Nature', 'Luxury', 'Culture'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Mystical Tawang & Bomdila • 06 Nights / 07 Days',
        overview=(
            'Welcome to the Land of the Dawn-Lit Mountains. The Best Arunachal Pradesh Tour Package, curated by the travel experts at TRAGUIN, invites your family to explore a world tucked high in the Eastern Himalayas. This exclusive Luxury Arunachal Pradesh Holiday seamlessly guides you across deep misty valleys, cascading glacial rivers, roaring mountain passes, and ancient monastic fortresses.\n\n'
            'WHY CHOOSE THE PREMIUM TAWANG & BOMDILA ROUTE?\nA journey through Arunachal Pradesh is a life-changing encounter with pristine high-altitude ecosystems. Recognized globally for containing the most breathtaking Top Tourist Places in Arunachal Pradesh, this mountain route provides families with an exceptional mix of historical depth, raw alpine beauty, and unique local traditions.'
        ),
        seo_title='AR-002 | Mystical Tawang & Bomdila | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Arunachal package (AR-002 / TG-AP-BMT-002): Bomdila, Sela Pass, Tawang Monastery, Bum La Pass, Madhuri Lake, Dirang Valley, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Bomdila Monastery and Bomdila View Point on Day 02', 1),
            _ih('Sela Pass, Sela Lake, Jaswant Garh War Memorial, and Nuranang Falls on Day 03', 2),
            _ih('Tawang Monastery, Ani Gompa ropeway, and War Memorial Light & Sound Show', 3),
            _ih('Bum La Pass and Madhuri Lake high-altitude excursion on Day 05', 4),
            _ih('TRAGUIN Signature Experience: Private riverside high-tea along the Dirang River', 5),
        ],
        days=[
            _day(1, 'GUWAHATI TO BHALUKPONG / BOMDILA FOOTHILLS — GATE TO THE WILDERNESS', ('Your alpine family getaway begins as you land at Guwahati Airport or arrive at the railway station. You are warmly received by your dedicated TRAGUIN chauffeur with premium welcoming amenities. Board your luxury private vehicle and start a scenic transition toward the pristine foothills of Arunachal Pradesh. Watch the urban landscapes of the Brahmaputra valley dissolve into dense semi-evergreen forests and sprawling tea gardens as you climb toward Bhalukpong, the edge of the Kameng river system. Cross the inner line check post with pre-arranged permits and check into your handpicked premium resort. Spend a relaxed evening listening to the rushing mountain river.'), [
                'Sightseeing Included: Scenic Brahmaputra Valley drive, Bhalukpong riverfront views.',
                'Evening Experience: Relaxed riverside stroll and traditional welcome dinner at the resort.',
                'Meals Included: Gourmet Dinner.',
                'Overnight Stay: Handpicked Premium Resort, Bhalukpong Foothills.',
            ]),
            _day(2, 'BHALUKPONG TO BOMDILA — WINDING HEIGHTS & MONASTIC VISTAS', ('Enjoy a rich breakfast with valley views before starting your mountain ascent along the dramatic ghat roads to Bomdila, standing at a majestic 7,200 feet. Your driver will maintain a gentle, senior and child-friendly speed, handling the winding roads with extreme care. Drive past deep gorges, rising mist, and beautiful Monpa tribal villages. Upon arrival in Bomdila, check into your premium valley-view property. In the afternoon, start your Bomdila Sightseeing exploration. Visit the beautiful Bomdila Monastery (GRL Monastery), home to Buddhist monks, where you can observe peaceful evening prayers. Visit the panoramic Bomdila View Point to view the massive cloud-covered peaks of the Kameng valley.'), [
                'Sightseeing Included: Bomdila Monastery, Bomdila View Point, Local Craft Centre.',
                'Evening Experience: Leisure stroll through the brightly lit local mountain bazaar.',
                'Meals Included: Breakfast, Dinner.',
                'Overnight Stay: Handpicked Premium Hotel, Bomdila.',
            ]),
            _day(3, 'BOMDILA TO TAWANG VIA SELA PASS — CROSSING THE FROZEN SKY PASS', ('Savor an early hearty breakfast as today promises an absolute highlight of your Arunachal Pradesh Family Tour. Depart for the historic fortress town of Tawang, traversing through some of the most breathtaking landscapes in the world. Ascend to the monumental Sela Pass, standing high at a spectacular 13,700 feet. Feel the crisp cold air and marvel at the frozen, mystical Sela Lake, surrounded by snow-draped mountains and hundreds of colorful prayer flags. Your TRAGUIN team ensures a comfortable stop here for hot beverages and group photography. Descend into the valley to pay your respects at the historic Jaswant Garh War Memorial. Before reaching Tawang, stop to view the roaring Nuranang (Jung) Falls, a magnificent 100-foot glacial waterfall crashing down emerald green cliffs. Arrive in Tawang by late evening and settle into your premium luxury resort with pre-heated rooms.'), [
                'Sightseeing Included: High-altitude Sela Pass, Sela Lake, Jaswant Garh War Memorial, Nuranang (Jung) Falls.',
                'Evening Experience: Cozy fireside family dinner at your luxury Tawang resort.',
                'Meals Included: Breakfast, Dinner.',
                'Overnight Stay: Handpicked Premium Luxury Resort, Tawang.',
            ]),
            _day(4, 'TAWANG — MONASTIC HERITAGE & EPIC STORYTELLING WALKS', ('Today is dedicated to discovering the cultural and spiritual core of your Tawang Sightseeing itinerary. Following a sumptuous breakfast, explore the world-famous Tawang Monastery. Founded in the 17th century, this is the largest Buddhist monastery in India and the second largest in the world, standing like a grand medieval palace on a high hill cliff. Accompanied by an expert local storyteller, tour the massive assembly hall, view the colossal 26-foot-tall gilded Buddha statue, and browse ancient manuscripts inside the historic library. Next, visit the peaceful Ani Gompa (Nuns\' Monastery) via a panoramic ropeway ride. In the afternoon, visit the beautifully manicured grounds of the Tawang War Memorial for an emotional evening Light & Sound Show detailing the rich local history. Return to the resort for an exquisite multi-cuisine dinner.'), [
                'Sightseeing Included: Tawang Monastery, Ani Gompa, Tawang War Memorial & Light Show, Urgelling Monastery (Birthplace of the 6th Dalai Lama).',
                'Evening Experience: VIP seats at the Tawang War Memorial Sound and Light Presentation.',
                'Meals Included: Breakfast, Dinner.',
                'Overnight Stay: Handpicked Premium Luxury Resort, Tawang.',
            ]),
            _day(5, 'TAWANG — EXCURSION TO THE MYSTICAL GLACIAL LAKES (BUM LA PASS)', ('Wake up early for a spectacular high-altitude excursion towards the Indo-China border at Bum La Pass, standing at an incredible 15,200 feet above sea level. Transfer into a local, specialized mountain-terrain 4x4 vehicle pre-arranged with military permits by your TRAGUIN concierge. Journey past clear glacial plains to view the serene Madhuri Lake (Shonga-tser Lake), formed by an earthquake and famed for dead tree trunks standing upright in the middle of its clear waters. Walk hand-in-hand with your family along the wooden broadwalks and look out over the snow-covered mountains. Return to Tawang by afternoon and spend a relaxed evening exploring local traditional woodcraft workshops and picking up authentic souvenirs.'), [
                'Sightseeing Included: Bum La Pass, Madhuri Lake, PT Tso (Pankang Teng Tso) Lake.',
                'Optional Activities: Interaction with local artisans at the traditional Tawang craft emporium.',
                'Meals Included: Gourmet Breakfast & Selected Regional Hot Dinner.',
                'Overnight Stay: Handpicked Premium Luxury Resort, Tawang.',
            ]),
            _day(6, 'TAWANG TO DIRANG VALLEY — THE SOOTHING KIWI ORCHARDS & RIVERS', ('Bid farewell to Tawang and start a relaxing return journey down the mountains toward the beautiful, warm plains of the Dirang Valley (4,900 feet). Arrive by afternoon and check into an exclusive riverside boutique resort. Dirang is celebrated for its wonderful pleasant climate and scenic beauty. Explore the historic Dirang Dzong, a 17th-century Monpa tribal fortress town built completely out of stone. Walk through the sprawling green kiwi and apple orchards, and visit the serene National Research Centre on Yak to see the unique high-altitude animals up close. Spend your final evening enjoying a premium TRAGUIN Signature Experience: a private family riverside high-tea set up elegantly along the clear bubbling water of the Dirang River.'), [
                'Sightseeing Included: Dirang Valley Drive, Dirang Dzong, Kiwi & Apple Orchards, Yak Research Centre.',
                'Evening Experience: Exclusive TRAGUIN Riverside High Tea and a final family farewell celebration.',
                'Meals Included: Breakfast, Dinner.',
                'Overnight Stay: Premium Riverside Boutique Resort, Dirang.',
            ]),
            _day(7, 'DIRANG TO GUWAHATI — DEPARTURE WITH LIFELONG MEMORIES', ('Indulge in a final, early morning breakfast on your resort veranda as the mountain mist rolls gently across the river valley. Settle into your premium luxury vehicle for your smooth return drive descending back toward the Brahmaputra plains of Guwahati. Your chauffeur handles the road with care, planning comfortable rest stops on the way. Arrive at Guwahati Airport or Railway Station by late afternoon for your flight home. Your elite family expedition concludes beautifully, leaving you with absolute rejuvenation, deep cultural enrichment, and unforgettable memories built flawlessly by TRAGUIN.'), [
                'Sightseeing Included: Winding mountain descent, private departure airport transfer.',
                'Meals Included: Premium Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Hotel Siphiyang Khang | Hotel Gakyi Khang Zhang | Hotel Pemaling Dirang', 'Bomdila (1 Night) / Tawang (3 Nights) / Dirang Valley (1 Night)', '06 Nights', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner', 4, 1, description='OPTION 01 – DELUXE: Hotel Siphiyang Khang (Bomdila, 1 Night) | Hotel Gakyi Khang Zhang (Tawang, 3 Nights) | Hotel Pemaling Dirang (Dirang Valley, 1 Night) | Breakfast & Dinner'),
            _hotel('Hotel Tashi Denlek | Tawang Horizon / Willow House | MPT Haritha Dirang Valley', 'Bomdila (1 Night) / Tawang (3 Nights) / Dirang Valley (1 Night)', '06 Nights', 'Premium', 'Premium Room', 'Breakfast & Dinner', 4, 2, description='OPTION 02 – PREMIUM: Hotel Tashi Denlek (Bomdila, 1 Night) | Tawang Horizon / Willow House (Tawang, 3 Nights) | MPT Haritha Dirang Valley (Dirang Valley, 1 Night) | Breakfast & Dinner'),
            _hotel('Bomdila Heritage Residency | Dondrub Homestay Luxury Wing | Dirang Boutique Cottages', 'Bomdila (1 Night) / Tawang (3 Nights) / Dirang Valley (1 Night)', '06 Nights', 'Luxury', 'Luxury Room', 'Breakfast & Dinner', 5, 3, description='OPTION 03 – LUXURY: Bomdila Heritage Residency (Bomdila, 1 Night) | Dondrub Homestay Luxury Wing (Tawang, 3 Nights) | Dirang Boutique Cottages (Dirang Valley, 1 Night) | Breakfast & Dinner'),
            _hotel('The Monastery View Pavilion | Tawang Palace Resort & Spa | The Norphel Boutique Resort', 'Bomdila (1 Night) / Tawang (3 Nights) / Dirang Valley (1 Night)', '06 Nights', 'Ultra Luxury', 'Luxury Suite', 'Breakfast & Dinner', 5, 4, description='OPTION 04 – ULTRA LUXURY: The Monastery View Pavilion (Bomdila, 1 Night) | Tawang Palace Resort & Spa (Tawang, 3 Nights) | The Norphel Boutique Resort (Dirang Valley, 1 Night) | Breakfast & Dinner'),
        ],
        inclusions=[
            _inc_included('Premium Stays: 06 Nights accommodation across handpicked luxury and premium mountain resorts.', 1),
            _inc_included('Gourmet Dining: Daily buffet breakfast and custom multi-course dinners across all properties.', 2),
            _inc_included('Luxury Transportation: Private air-conditioned luxury SUV (Toyota Innova Crysta) for all transfers, drives, and sightseeing.', 3),
            _inc_included('Bum La 4x4 SUV: Specialized local mountain-terrain 4x4 vehicle for the high-altitude Bum La Pass day excursion.', 4),
            _inc_included('Permit Handling: Full handling and pre-arrangement of Arunachal Pradesh Inner Line Permits (ILP) and PAP.', 5),
            _inc_included('Welcome Amenities: Royal traditional welcomes, complimentary mountain travel kits, and daily premium mineral water bottles.', 6),
            _inc_included('TRAGUIN Support: 24/7 dedicated virtual concierge support with fully covered fuel, tolls, and driver allowances.', 7),
            _inc_excluded('Main Flights / Rail: Intercity transport tickets to and from Guwahati.', 8),
            _inc_excluded('Monument Entry: Individual entry tickets at museums, light shows, and ropeways unless specified.', 9),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, room heating additions, and tips.', 10),
            _inc_excluded('Optional Tours: Travel or medical insurance coverage plans.', 11),
        ],
    )
    return package, itinerary

def build_ar_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AR-003'
    tour_code = 'TG-AR-EXP-003'
    title = 'TRAGUIN Premium Arunachal Pradesh Tour Package — Arunachal Explorer: The Land of Dawn-Lit Mountains'
    duration = '07 Nights / 08 Days'
    slug = 'ar-003-arunachal-explorer-dawn-lit-mountains'
    itin_slug = 'ar-003-arunachal-explorer-dawn-lit-mountains-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Arunachal Pradesh / India | Category: Premium Adventure Tour', 2),
            _ph('Destinations: Guwahati • Bhalukpong • Dirang • Tawang • Bomdila', 3),
            _ph('Ideal for: Adventure Seekers, Families & Nature Enthusiasts', 4),
            _ph('Best season: March to June & October to December', 5),
            _ph('Starting price: On Request (Premium Luxury Tier)', 6),
            _ph('Vehicle: Private AC Luxury 4x4 (Toyota Innova Crysta / Scorpio N) | Meal Plan: Premium Breakfast & Dinner (MAPAI)', 7),
            _ph('Route Plan: Guwahati ➔ Bhalukpong (1N) ➔ Dirang (1N) ➔ Tawang (3N) ➔ Bomdila (1N) ➔ Guwahati (1N)', 8),
            _ph('TRAGUIN Curated Experience Note: Private high-tea along the Kameng River, intimate Monpa tribal elder interaction, exclusive sunrise photo shoot at Sela Pass, and customized hot-stone wellness experience.', 9),
            _ph('TRAGUIN Signature Experience: Private family sunset cruise across the vast Brahmaputra River with traditional live music.', 10),
            _ph('Curated by TRAGUIN Experts: Every mountain pass route, heavy-duty 4x4 vehicle, and boutique lodge is rigorously vetted for absolute safety and luxury.', 11),
            _ph('Personalized Assistance: Dedicated high-altitude travel consultant available around the clock for permit updates or weather checks.', 12),
            _ph('Premium Handpicked Hotels: Beautifully designed mountain resorts featuring heated room options and gorgeous view balconies.', 13),
            _ph('Shopping & Local Experiences: Monpa wooden artifacts, Himalayan teas & fruits, Tibetan woolen carpets, warm Monpa Thukpa and momos.', 14),
            _ph('Important Notes: High-altitude guidelines for Tawang; ILP documents 15 days prior; book 60–90 days ahead for peak spring and autumn.', 15),
        ],
        moods=['Adventure', 'Family', 'Luxury', 'Culture'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Arunachal Explorer • Bhalukpong • Dirang • Tawang • Bomdila • 07 Nights / 08 Days',
        overview=(
            'Welcome to the mystical frontiers of Northeast India. The Best Arunachal Pradesh Tour Package, designed exclusively by TRAGUIN, invites you on an elite voyage into the land of dawn-lit peaks. This masterfully calibrated Arunachal Pradesh Family Tour and raw wilderness trail leads you through alpine valleys, pristine glacial lakes, and ancient spiritual monasteries.\n\n'
            'TOUR OVERVIEW\nThe Arunachal Explorer expedition is a private, customized journey traversing the western circuit of Arunachal Pradesh. Ascending through sub-tropical forests to the high-alpine heights of the Eastern Himalayas, this comprehensive adventure bridges majestic scenery with complete comfort.'
        ),
        seo_title='AR-003 | Arunachal Explorer | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Arunachal Explorer package (AR-003 / TG-AR-EXP-003): Bhalukpong, Dirang, Sela Pass, Tawang, Bum La Pass, Bomdila, Brahmaputra cruise, and 4-tier accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Bhalukpong foothills entry and Kameng River exploration on Day 01', 1),
            _ih('Tipi Orchid Sanctuary, Dirang Dzong, and natural hot springs on Day 02', 2),
            _ih('Sela Pass ascent, Nuranang Waterfalls, and Tawang arrival on Day 03', 3),
            _ih('Tawang Monastery, Giant Buddha Statue, and War Memorial Light & Sound Show', 4),
            _ih('Bum La Pass, Madhuri Lake, and Brahmaputra sunset cruise finale', 5),
        ],
        days=[
            _day(1, 'GUWAHATI TO BHALUKPONG — ENTRY INTO THE FOOTHILLS', ('Your ultimate adventure begins as you arrive at Guwahati Airport or Railway Station. You are warmly greeted by your dedicated TRAGUIN chauffeur and tour manager with custom mountain kits. Leave the plains of Assam behind as your private luxury 4x4 SUV drives north towards the Arunachal frontier. Cross the boundary into Bhalukpong, nestled comfortably along the banks of the rushing Kameng River. Check into your premium nature resort and enjoy a seamless check-in. Spend your afternoon unwinding amidst the dense sub-tropical greenery or taking a peaceful walk along the pebble-strewn riverbanks. In the evening, gather for a fresh gourmet dinner at the resort.'), [
                'Sightseeing Included: Scenic cross-border highway drive, Kameng River front exploration.',
                'Evening Experience: Briefing with your mountain guide followed by a riverside campfire dinner.',
                'Meals Included: Welcome Refreshments & Gourmet Buffet Dinner.',
                'Overnight Stay: Premium Eco-Resort, Bhalukpong.',
            ]),
            _day(2, 'BHALUKPONG TO DIRANG — THROUGH KIWI ORCHARDS & MONPA VALLEYS', ('Savor a luxurious, warm breakfast before continuing your Arunachal Pradesh Sightseeing ascent. Wind through the dramatic road curves of the Bomdila-Dirang highway, witnessing endless valleys and cascading mountain streams. Stop at the Tipi Orchid Research Centre to view hundreds of rare, colorful orchid species. Drive further into the beautiful Dirang Valley, located at an altitude of 4,900 feet. Check into your handpicked valley lodge. In the afternoon, explore the historic Dirang Dzong—a 17th-century Monpa citadel built entirely of stone, offering a deep look into medieval Himalayan history. Walk through adjacent kiwi and apple orchards, and relax your muscles by dipping your feet in the natural hot water springs of Dirang River before dinner.'), [
                'Sightseeing Included: Tipi Orchid Sanctuary, Dirang Dzong Stone Fortress, Natural Hot Springs.',
                'Evening Experience: Warm traditional Monpa welcome and customized local culinary demonstration.',
                'Meals Included: Buffet Breakfast & Selected Farm-to-Table Dinner.',
                'Overnight Stay: Handpicked Boutique Valley Resort, Dirang.',
            ]),
            _day(3, 'DIRANG TO TAWANG — CROSSING THE MIGHTY SELA PASS', ('Today marks an epic milestone in your Premium Arunachal Pradesh Experience. Following an early breakfast, board your luxury 4x4 SUV to ascend to the towering altitude of Sela Pass, standing high at 13,700 feet. Drive through a frozen paradise bordered by snow-capped peaks and stop by the crystalline Sela Lake, which remains semi-frozen for a large part of the year. Capture spectacular family landscape photographs here. Descend into the valley, stopping to witness the immense force of Nuranang Waterfalls (Jang Falls), which cascades down more than 100 meters against jagged cliffs. Pay your respects to the brave soldiers at Jaswant Garh War Memorial. Arrive in the mystical mountain town of Tawang (10,000 feet) by late afternoon and check into your premium luxury stay curated by TRAGUIN specialists.'), [
                'Sightseeing Included: Sela Pass Ascent, Sela Lake, Jaswant Garh Memorial, Nuranang Waterfalls.',
                'Evening Experience: Welcome hot butter tea session followed by room temperature adjustment and relaxation.',
                'Meals Included: Warm Breakfast & Gourmet Multi-cuisine Dinner.',
                'Overnight Stay: Premium Luxury Mountain Hotel, Tawang.',
            ]),
            _day(4, 'TAWANG — THE MAJESTIC MONASTERY & CULTURAL SOUL', ('Awake to pristine mountain sunbeams hitting your veranda. Today is dedicated to deep Tawang Sightseeing. Accompanied by an expert scholar guide, visit the massive Tawang Monastery, a 400-year-old citadel that stands as the second-largest Buddhist monastery in the world. Walk through its grand library housing priceless ancient manuscripts and stand before the colossal 18-foot-tall gilded statue of Lord Buddha. In the afternoon, ascend the adjacent hill to view the immense Giant Buddha Statue, offering panoramic bird\'s-eye views across the entire Tawang Valley. Later, take a peaceful walk through the local Monpa craft bazaars, observing traditional handmade paper factories and intricate woolen weaving studios. In the evening, attend the moving Light and Sound Show held inside the Tawang War Memorial complex.'), [
                'Sightseeing Included: Tawang Monastery, Giant Buddha Statue, Handmade Paper Factory, Ani Gompa.',
                'Evening Experience: VIP seating at the Tawang War Memorial Sound & Light Show.',
                'Meals Included: Premium Breakfast & Multi-course Fine Dining Dinner.',
                'Overnight Stay: Premium Luxury Mountain Hotel, Tawang.',
            ]),
            _day(5, 'TAWANG — THE HIGH-ALTITUDE GLACIAL LAKES EXCURSION', ('Prepare your lenses for an unforgettable high-altitude adventure. Board your specialized local 4x4 vehicle and drive towards the remote, pristine landscapes bordering the international frontier. Ascend to Madhuri Lake (Sangetsar Lake), a spectacular glacial water body formed by an earthquake, famous for its submerged dead tree trunks standing dramatically out of the clear blue waters. Take a quiet family walk along the wooden walkway encircling the lake. Next, continue to the breathtaking Bum La Pass (15,200 feet), subject to weather conditions and military clearances. Stand right on the international border line and interact with the army personnel. Return to your luxury hotel by late afternoon to unwind and share your stories over a grand farewell theme dinner curated by the hotel chefs.'), [
                'Sightseeing Included: Bum La Pass Border, Madhuri Lake, PT Tso Lake (Pankang Teng Tso).',
                'Exclusive Experience: Custom TRAGUIN mountain picnic box snack served right by the high lakes.',
                'Meals Included: Breakfast, Mountain Picnic Lunch, & Grand Farewell Dinner.',
                'Overnight Stay: Premium Luxury Mountain Hotel, Tawang.',
            ]),
            _day(6, 'TAWANG TO BOMDILA — DECELERATING THROUGH MOUNTAIN MISTS', ('After a hearty breakfast, begin your return journey across the Sela mountain pass, descending gracefully toward the historic town of Bomdila, sitting at an altitude of 7,200 feet. The changing landscape from snow-capped ridges to dense green forests provides an incredible panoramic backdrop for photography. Arrive in Bomdila by afternoon and check into your handpicked premium stay. Visit the gorgeous Bomdila Monastery (GRL Monastery), which stands as a key spiritual hub for the Mahayana Buddhist sect. Take a peaceful stroll across the local market area to shop for traditional Tibetan carpets and local artifacts while enjoying the misty evening weather.'), [
                'Sightseeing Included: Return Sela Pass drive, Bomdila GRL Monastery, Bomdila Viewpoint.',
                'Evening Experience: Relaxed evening walk inside the mountain handicraft cooperative markets.',
                'Meals Included: Buffet Breakfast & Regional Specialty Dinner.',
                'Overnight Stay: Premium Heritage Hotel, Bomdila.',
            ]),
            _day(7, 'BOMDILA TO GUWAHATI — DESCENDING TO THE BRAHMAPUTRA', ('Savor your final breakfast in the mountains before starting your long, comfortable descent down the lush foothills back toward the Brahmaputra plains of Assam. Enjoy your last look at the stunning mountain horizons as the air turns warmer. Your luxury vehicle will maintain a smooth speed, stopping for a gourmet lunch along the highway. Arrive in Guwahati by late evening and check into your ultra-luxury city hotel. To celebrate the final evening of your Arunachal Explorer expedition, embark on a private Brahmaputra River Sunset Cruise, enjoying local Assamese snacks and live traditional music as the sun goes down over the wide river. Return to your hotel for a grand dinner.'), [
                'Sightseeing Included: Foothill scenic drive, Brahmaputra Riverfront.',
                'Evening Experience: Private Luxury Sunset Cruise across the Brahmaputra River.',
                'Meals Included: Breakfast, Highway Lunch, & Cruise Farewell Dinner.',
                'Overnight Stay: Ultra-Luxury Five-Star Hotel, Guwahati.',
            ]),
            _day(8, 'GUWAHATI — DEPARTURE WITH LIFELONG MEMORIES', ('Indulge in a magnificent buffet breakfast at your luxury city hotel. Depending on your flight or train schedule, enjoy a relaxed morning taking advantage of the hotel\'s premium amenities. Your private luxury vehicle will provide a seamless transfer to the Guwahati Airport or Kamakhya Railway Station for your onward journey home. Your comprehensive Arunachal Explorer adventure concludes beautifully, leaving your family with beautiful photographs, enriched minds, and unforgettable memories built flawlessly by TRAGUIN.'), [
                'Sightseeing Included: Airport / Station Private Departure Transfer.',
                'Meals Included: Premium Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('MPT Druk Resort / Dirang Eco Resort | Hotel Tawang View / Pemaling | Hotel Elysium Bomdila | Radisson Blu Guwahati', 'Bhalukpong / Dirang (1N+1N) / Tawang (3 Nights) / Bomdila (1 Night) / Guwahati (1 Night)', '07 Nights', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner', 4, 1, description='OPTION 01 – DELUXE: MPT Druk Resort / Dirang Eco Resort (Bhalukpong/Dirang, 1N+1N) | Hotel Tawang View / Pemaling (Tawang, 3 Nights) | Hotel Elysium Bomdila (Bomdila, 1 Night) | Radisson Blu Guwahati (Guwahati, 1 Night)'),
            _hotel('Prashaanty Resort / J n R Eco Lodge | Hotel Tawang Regency / Gakyi Khang Zhang | Pine Ridge Resort Bomdila | Vivanta by Taj Guwahati', 'Bhalukpong / Dirang (1N+1N) / Tawang (3 Nights) / Bomdila (1 Night) / Guwahati (1 Night)', '07 Nights', 'Premium', 'Premium Room', 'Breakfast & Dinner', 4, 2, description='OPTION 02 – PREMIUM: Prashaanty Resort / J n R Eco Lodge (Bhalukpong/Dirang, 1N+1N) | Hotel Tawang Regency / Gakyi Khang Zhang (Tawang, 3 Nights) | Pine Ridge Resort Bomdila (Bomdila, 1 Night) | Vivanta by Taj Guwahati (Guwahati, 1 Night)'),
            _hotel('Kameng River Eco Lodge / Nameri Camp | Dondrub Homestay Luxury Wing | WelcomHeritage Mon-Pas Residence | Novotel Varun Guwahati', 'Bhalukpong / Dirang (1N+1N) / Tawang (3 Nights) / Bomdila (1 Night) / Guwahati (1 Night)', '07 Nights', 'Luxury', 'Luxury Room', 'Breakfast & Dinner', 5, 3, description='OPTION 03 – LUXURY: Kameng River Eco Lodge / Nameri Camp (Bhalukpong/Dirang, 1N+1N) | Dondrub Homestay Luxury Wing (Tawang, 3 Nights) | WelcomHeritage Mon-Pas Residence (Bomdila, 1 Night) | Novotel Varun Guwahati (Guwahati, 1 Night)'),
            _hotel('Premium Wilderness Eco Retreat (Villas) | The Tawang Heritage Resort (Suite Tier) | Lhakhang Premium Heritage Suite | Taj Landmark Hotel Guwahati', 'Bhalukpong / Dirang (1N+1N) / Tawang (3 Nights) / Bomdila (1 Night) / Guwahati (1 Night)', '07 Nights', 'Ultra Luxury', 'Luxury Suite', 'Breakfast & Dinner', 5, 4, description='OPTION 04 – ULTRA LUXURY: Premium Wilderness Eco Retreat (Bhalukpong/Dirang, 1N+1N) | The Tawang Heritage Resort Suite Tier (Tawang, 3 Nights) | Lhakhang Premium Heritage Suite (Bomdila, 1 Night) | Taj Landmark Hotel Guwahati (Guwahati, 1 Night)'),
        ],
        inclusions=[
            _inc_included('Premium Stays: 07 Nights elite accommodation at our handpicked premium mountain resorts and luxury hotels.', 1),
            _inc_included('Gourmet Dining: Daily buffet breakfast and custom chef-curated hot dinners across all properties.', 2),
            _inc_included('Luxury Transportation: Private air-conditioned luxury 4x4 heavy SUV (Innova Crysta / Scorpio N) for all transfers, drives, and sightseeing.', 3),
            _inc_included('Permits & Clearances: Inner Line Permits (ILP) and complete processing of Bum La Pass border paperwork guidelines.', 4),
            _inc_included('TRAGUIN Signatures: Private high-tea experience along Kameng River and an exclusive Brahmaputra Sunset Cruise.', 5),
            _inc_included('Welcome Amenities: Royal traditional welcomes, fresh fruits, and daily premium mineral water bottles inside your vehicle.', 6),
            _inc_included('Assistance & Taxes: 24/7 dedicated support from TRAGUIN expert managers, covered tolls, fuel, parking, and driver allowances.', 7),
            _inc_excluded('Main Transport Fares: Flight or main rail tickets to and from Guwahati.', 8),
            _inc_excluded('Monument Entry Tickets: Individual entrance fees at monasteries, museums, or local light shows.', 9),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, premium room service, alcoholic drinks, and tipping fees.', 10),
            _inc_excluded('Optional Extras: Emergency vehicle modifications, porter costs during walks, or travel medical insurance plans.', 11),
        ],
    )
    return package, itinerary

def build_ar_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AR-004'
    tour_code = 'TG-AP-RTW-004'
    title = 'TRAGUIN Premium Arunachal Pradesh Tour Package — Romantic Tawang & The Land of the Dawn-Lit Mountains'
    duration = '05 Nights / 06 Days'
    slug = 'ar-004-romantic-tawang-honeymoon'
    itin_slug = 'ar-004-romantic-tawang-honeymoon-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Arunachal Pradesh / India | Category: Romantic Honeymoon Private FIT', 2),
            _ph('Destinations: Guwahati • Bhalukpong • Dirang • Tawang', 3),
            _ph('Ideal for: Newlyweds & Romantic Couples', 4),
            _ph('Best season: March to June & October to December', 5),
            _ph('Starting price: On Request (Premium Luxury Tier)', 6),
            _ph('Vehicle: Private AC Luxury 4x4 SUV (Innova / Scorpio) | Meal Plan: Premium MAPAI (Daily Breakfast & Intimate Dinners)', 7),
            _ph('Route Plan: Guwahati ➔ Bhalukpong (1N) ➔ Dirang (1N) ➔ Tawang (3N) ➔ Departure', 8),
            _ph('TRAGUIN Curated Experience Note: Private twilight lakeside toast at Madhuri Lake, romantic Monpa tribal welcome experiences, and custom inner line permit processing handled completely by TRAGUIN specialists.', 9),
            _ph('TRAGUIN Signature Experience: Private high-altitude lakeside picnic set up elegantly on the banks of Madhuri Lake.', 10),
            _ph('Curated by TRAGUIN Experts: Every high-altitude route, luxury 4x4 driver, and resort cottage is rigorously vetted for absolute safety, privacy, and exceptional comfort.', 11),
            _ph('Personalized Assistance: Elite, dedicated travel coordinator available around the clock to manage any adjustments or special requests.', 12),
            _ph('Premium Handpicked Hotels: Beautifully managed properties showcasing vast mountain views, traditional Monpa craftwork, and old-world romance.', 13),
            _ph('Shopping & Local Experiences: Tawang handicraft bazaars, local momos and thukpa, Dirang kiwi wine, traditional Monpa textiles.', 14),
            _ph('Important Notes: High altitude preparation for Tawang; ILP documents 15 days prior; book 60–90 days ahead for Vivanta Tawang peak seasons.', 15),
        ],
        moods=['Honeymoon', 'Romantic', 'Luxury', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Romantic Tawang Honeymoon • Bhalukpong • Dirang • Tawang • 05 Nights / 06 Days',
        overview=(
            'Welcome to your magnificent mountain love story. The Best Arunachal Pradesh Tour Package, thoughtfully curated by TRAGUIN, invites you and your significant other to celebrate the ultimate bond of marriage amidst the spectacular frozen lakes, cascading alpine waterfalls, and majestic snow-capped ridges of the Eastern Himalayas.\n\n'
            'TOUR OVERVIEW\nThis bespoke Luxury Arunachal Pradesh Holiday carries couples deep into the hidden heart of the sub-Himalayan wilderness. Beginning with your seamless arrival in Guwahati, you will journey upward through the lush river valleys of Bhalukpong, the kiwi orchards of Dirang, and scale the majestic height of Sela Pass to reach the historical fortress town of Tawang.'
        ),
        seo_title='AR-004 | Romantic Tawang Honeymoon | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Arunachal honeymoon package (AR-004 / TG-AP-RTW-004): Bhalukpong, Dirang, Sela Pass, Tawang Monastery, Madhuri Lake picnic, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Riverside eco-lodge candlelight dinner and honeymoon cake welcome in Bhalukpong', 1),
            _ih('Tipi Orchid Sanctuary, Dirang Dzong, kiwi orchards, and therapeutic hot springs', 2),
            _ih('Sela Pass (13,700 ft), Sela Alpine Lake, and Nuranang Falls on the Tawang ascent', 3),
            _ih('Tawang Monastery, Ani Gompa, and VIP War Memorial Light & Sound Show', 4),
            _ih('TRAGUIN Signature Experience: Private lakeside picnic and farewell candlelit dinner at Madhuri Lake', 5),
        ],
        days=[
            _day(1, 'GUWAHATI TO BHALUKPONG — ASCENT TO THE FOOTHILLS OF PARADISE', ('Your romantic adventure begins as you land at Guwahati Airport. You are warmly received by your dedicated TRAGUIN private chauffeur with premium welcoming amenities and smooth Inner Line Permits (ILP). Settle inside your luxury 4x4 SUV and begin a highly scenic drive cutting through the lush Assam plains before ascending toward the foothills of Arunachal Pradesh. Cross the border into Bhalukpong, a pristine mountain enclave nestled on the banks of the roaring Kameng River. Check into your handpicked riverside eco-lodge. After a smooth check-in, relax with a special honeymoon cake and floral room highlights. In the late afternoon, take a relaxed hand-in-hand stroll along the smooth river stones, watching the mist drift down from the high green canopies. Return to your lodge for an exquisite candlelight dinner under the starry sky, marking the perfect beginning to your mountain love story.'), [
                'Sightseeing Included: Scenic plains-to-hills drive, Kameng Riverbank walking trails, Bhalukpong nature preserve.',
                'Evening Experience: Private riverside evening stroll followed by an intimate dinner arrangement.',
                'Meals Included: Welcome Signature Refreshment, Honeymoon Cake, & Gourmet Dinner.',
                'Overnight Stay: Premium Riverside Eco-Lodge, Bhalukpong.',
            ]),
            _day(2, 'BHALUKPONG TO DIRANG — WINDING RIVER VALLEYS & EXOTIC ORCHARDS', ('Wake to the soothing symphony of the river and crisp mountain air. Following a hearty breakfast, begin your journey upward into the Eastern Himalayas toward the spectacular Dirang Valley. This driving segment is an immersive visual masterpiece, featuring winding mountain passes, pristine sub-tropical flora, and cascading streams. En route, stop at the Tipi Orchid Research Centre to view hundreds of exotic, rare orchid species blooming in vibrant colors. Arrive in the emerald valley of Dirang and check into your boutique resort overlooking terraced farm fields. In the afternoon, enjoy an immersive experience walking hand-in-hand through the local kiwi and apple orchards. Visit the historic Dirang Dzong, a 17th-century Monpa fortress village built entirely of stone, showcasing remarkable tribal architecture. Conclude your day with a comforting dip in the therapeutic local Hot Water Springs before enjoying a multi-course dinner at your resort.'), [
                'Sightseeing Included: Tipi Orchid Sanctuary, Dirang Valley drive, Dirang Dzong stone village, Hot Springs.',
                'Evening Experience: Private walking tour of kiwi plantations and a peaceful resort dinner.',
                'Meals Included: Premium Buffet Breakfast & Gourmet Continental/Local Dinner.',
                'Overnight Stay: Handpicked Boutique Mountain Resort, Dirang.',
            ]),
            _day(3, 'DIRANG TO TAWANG — SCALING SELA PASS TO THE LAND OF MISTS', ('Today marks a truly unforgettable high-altitude highlight of your Arunachal Pradesh Honeymoon Package. Savor an early breakfast before departing for the legendary alpine fortress of Tawang. Your luxury 4x4 vehicle scales the winding mountain roads up to the jaw-dropping height of Sela Pass at 13,700 feet. Walk together through the iconic colorful Tibetan-style gateway archway and view the spectacular, semi-frozen Sela Lake, where low-floating clouds drift directly over the dark water. Descend into the valley and visit the majestic Nuranang Falls (Jang Falls), where a massive volume of white water plunges over 100 feet down a sheer mountain cliff. Stand at the base to feel the crisp mountain spray before completing your drive to Tawang. Check into your ultra-luxury room featuring panoramic views of the valley peaks, and enjoy a curated hot-pot dinner designed to keep you cozy in the cold mountain night.'), [
                'Sightseeing Included: Sela Pass (13,700 Ft), Sela Alpine Lake, Jaswant Garh War Memorial, Nuranang (Jang) Falls.',
                'Evening Experience: Scenic room orientation with premium mountain tea and traditional Monpa hand-woven wraps.',
                'Meals Included: Hot Buffet Breakfast & Luxury Mountain-View Dinner.',
                'Overnight Stay: Premium Luxury Resort, Tawang.',
            ]),
            _day(4, 'TAWANG — MONASTERIES OF GOLD & SOVEREIGN WAR LEGACIES', ('Awake to the enchanting sound of distant Buddhist morning horns echoing through the valley. Today features a deep exploration of Tawang Sightseeing landmarks. Following breakfast, visit the world-renowned Tawang Monastery (Gaden Namgyal Lhatse). Founded in the 17th century, this immense golden fortress is Asia\'s largest functioning monastery. Walk through the sprawling courtyards with an expert guide, explore the grand prayer halls, and admire the majestic 26-foot-high gilded statue of Lord Buddha. In the afternoon, visit the elegant Ani Gompa (Nunnery) perched high on a secluded hill ridge. Later, proceed to the Tawang War Memorial, a beautiful stupa structure honoring the brave soldiers of the 1962 war. Walk through the beautifully manicured memorial gardens and view the historical artifacts. In the evening, enjoy VIP seating at the emotional light and sound show depicting local heroic histories before enjoying dinner at your resort.'), [
                'Sightseeing Included: Tawang Monastery, Monastery Museum, Ani Gompa, Tawang War Memorial, Craft Centre.',
                'Evening Experience: VIP seating at the Tawang War Memorial Light & Sound Show.',
                'Meals Included: Multi-cuisine Breakfast & Chef\'s Table Traditional Dinner.',
                'Overnight Stay: Premium Luxury Resort, Tawang.',
            ]),
            _day(5, 'TAWANG — HIGH-ALTITUDE MADHURI LAKE & FROZEN VALLEYS', ('Prepare for an extraordinary journey into raw Himalayan beauty. Board your private luxury 4x4 vehicle and ascend through winding mountain trails toward the high-altitude border plateau. Pass by the scenic PTSO Lake (Pankang Teng Tso), surrounded by sweeping snow ridges and mountain mosses. Arrive at the iconic Madhuri Lake (Sangetsar Lake), formed by a dramatic earthquake in 1950, where dead tree trunks still stand up through the clear water mirror. Enjoy a TRAGUIN Signature Experience: a premium customized picnic hamper lunch set up elegantly along the quiet banks of Madhuri Lake. Capture stunning couple portraits against the majestic mountain reflections. Return to Tawang in the late afternoon, where the evening is yours to browse local handicraft markets for authentic woolen souvenirs or cozy up inside your resort\'s luxury library before a grand farewell candlelit dinner.'), [
                'Sightseeing Included: PTSO Lake drive, Madhuri (Sangetsar) Lake valley, Y-Junction vistas.',
                'Evening Experience: Private Lakeside High-Tea picnic followed by a Grand Farewell Couple\'s Dinner.',
                'Meals Included: Gourmet Breakfast, Signature Picnic Lunch, & Premium Candlelit Dinner.',
                'Overnight Stay: Premium Luxury Resort, Tawang.',
            ]),
            _day(6, 'TAWANG TO GUWAHATI — DEPARTURE WITH UNFORGETTABLE MEMORIES', ('Indulge in your final premium mountain breakfast while watching the morning sun illuminate the yellow roofs of Tawang Monastery. Take some final couple photographs against the backdrop of the sub-Himalayan valleys. Complete your check-out and board your luxury private vehicle for a smooth, scenic descent back down toward Guwahati Airport or railway station for your journey home. Your elite mountain romantic escape concludes here, leaving you with a deeply strengthened bond, beautiful photographs, and unforgettable memories crafted flawlessly by TRAGUIN.'), [
                'Sightseeing Included: Winding mountain descent, private airport departure transfer.',
                'Meals Included: Premium Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('MPT Druk Resort | Hotel Pemaling | Hotel Gakyi Khang Zhang', 'Bhalukpong (1 Night) / Dirang (1 Night) / Tawang (3 Nights)', '05 Nights', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner', 4, 1, description='OPTION 01 – DELUXE: MPT Druk Resort (Bhalukpong, 1 Night) | Hotel Pemaling (Dirang, 1 Night) | Hotel Gakyi Khang Zhang (Tawang, 3 Nights) | Breakfast & Dinner'),
            _hotel('Prashanti Eco Tourism Lodge | WelcomHeritage Monpa Heritage | Hotel Tawang Heights (Deluxe)', 'Bhalukpong (1 Night) / Dirang (1 Night) / Tawang (3 Nights)', '05 Nights', 'Premium', 'Premium Room', 'Breakfast & Dinner', 4, 2, description='OPTION 02 – PREMIUM: Prashanti Eco Tourism Lodge (Bhalukpong, 1 Night) | WelcomHeritage Monpa Heritage (Dirang, 1 Night) | Hotel Tawang Heights Deluxe (Tawang, 3 Nights) | Breakfast & Dinner'),
            _hotel('Kameng River Eco-Lodge | Dirang Boutique Cottages | Dondrub Homestay (Luxury Suite)', 'Bhalukpong (1 Night) / Dirang (1 Night) / Tawang (3 Nights)', '05 Nights', 'Luxury', 'Luxury Suite', 'Breakfast & Dinner', 5, 3, description='OPTION 03 – LUXURY: Kameng River Eco-Lodge (Bhalukpong, 1 Night) | Dirang Boutique Cottages (Dirang, 1 Night) | Dondrub Homestay Luxury Suite (Tawang, 3 Nights) | Breakfast & Dinner'),
            _hotel('Luxury Riverside Wood-Cabins | The Norphel Hotel Dirang | Vivanta Tawang / Premium Luxury Villa', 'Bhalukpong (1 Night) / Dirang (1 Night) / Tawang (3 Nights)', '05 Nights', 'Ultra Luxury', 'Luxury Villa / Suite', 'Breakfast & Dinner', 5, 4, description='OPTION 04 – ULTRA LUXURY: Luxury Riverside Wood-Cabins (Bhalukpong, 1 Night) | The Norphel Hotel Dirang (Dirang, 1 Night) | Vivanta Tawang / Premium Luxury Villa (Tawang, 3 Nights) | Breakfast & Dinner'),
        ],
        inclusions=[
            _inc_included('Premium Stays: 05 Nights premium accommodation across handpicked luxury mountain resorts and eco-lodges.', 1),
            _inc_included('Gourmet Dining: Daily buffet breakfast and custom multi-course dinners across all hotels.', 2),
            _inc_included('Luxury Transportation: Private air-conditioned luxury 4x4 SUV dedicated for all sightseeing, long-distance mountain transitions, and transfers.', 3),
            _inc_included('Inner Line Permits: Official processing and facilitation of Arunachal Pradesh Inner Line Permits (ILP) for both guests.', 4),
            _inc_included('Welcome Amenities: Royal traditional welcomes at hotels, premium honeymoon cake, local Monpa fabrics, and fresh mineral water provided inside your car daily.', 5),
            _inc_included('TRAGUIN Support: 24/7 dedicated concierge assistance from TRAGUIN honeymoon consultants, with all fuel, tolls, parking, and driver allowances fully covered.', 6),
            _inc_excluded('Main Tickets: Commercial flights or railway tickets to and from Guwahati.', 7),
            _inc_excluded('Monument Entry Tickets: Entry tickets to local museums, war memorials, and camera permits.', 8),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, alcoholic drinks, spa sessions, and optional tipping.', 9),
            _inc_excluded('High-Altitude Vehicle Upgrades: Local shuttle vehicles required for specific restricted border areas (if mandated by local unions).', 10),
        ],
    )
    return package, itinerary

def build_ar_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AR-005'
    tour_code = 'TG-AR-ADF-005'
    title = 'TRAGUIN Premium Arunachal Pradesh Tour Package — Arunachal Discovery: Sela Pass, Monasteries & Glacial Lakes'
    duration = '07 Nights / 08 Days'
    slug = 'ar-005-arunachal-discovery-sela-pass-monasteries'
    itin_slug = 'ar-005-arunachal-discovery-sela-pass-monasteries-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Arunachal Pradesh / India | Category: Premium Family Tour Layout', 2),
            _ph('Destinations: Bhalukpong • Dirang • Tawang • Bomdila • Tezpur', 3),
            _ph('Ideal for: Families, Culture Lovers & Alpine Explorers', 4),
            _ph('Best season: October to April (Crisp air & snowy peaks)', 5),
            _ph('Starting price: On Request (Premium Luxury Tier)', 6),
            _ph('Vehicle: Private AC Luxury SUV (Innova Crysta / Fortuner) | Meal Plan: Premium MAPAI (Daily Breakfast & Warm Comfort Dinners)', 7),
            _ph('Route Plan: Guwahati ➔ Bhalukpong (1N) ➔ Dirang (1N) ➔ Tawang (3N) ➔ Bomdila (1N) ➔ Tezpur (1N) ➔ Guwahati Departure', 8),
            _ph('TRAGUIN Curated Experience Note: Pre-arranged ILPs, curated mountain high-tea on Sela Pass Lake, private Monpa tribal village interaction, and hot picnic lunch near Madhuri Lake.', 9),
            _ph('TRAGUIN Signature Experience: Private, gourmet high-tea served at 13,700 feet right on the snow-dusted shores of Sela Alpine Lake.', 10),
            _ph('Curated by TRAGUIN Experts: Every 4x4 mountain driver, luxury log villa, and permit route is vetted for complete security and premium comfort.', 11),
            _ph('Personalized Assistance: Dedicated holiday coordinator assigned around the clock for weather-related route adjustments.', 12),
            _ph('Premium Handpicked Hotels: Stay at incredible properties, ranging from riverfront lodges to heated luxury alpine suites.', 13),
            _ph('Shopping & Local Experiences: Monpa carpets, local momo delicacies, organic kiwi wines and mountain apples from Dirang cooperatives.', 14),
            _ph('Important Notes: Acclimatization tips for Tawang; government photo IDs 15 days prior for permits; book Vivanta Tawang 60–90 days ahead.', 15),
        ],
        moods=['Family', 'Culture', 'Luxury', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Arunachal Discovery • Bhalukpong • Dirang • Tawang • Bomdila • Tezpur • 07 Nights / 08 Days',
        overview=(
            'Welcome to the land of dawn-lit mountains. The definitive Best Arunachal Pradesh Tour Package, designed exclusively by TRAGUIN, invites your loved ones to witness a pristine paradise where snow-clad Himalayan ridges embrace ancient spiritual sanctuaries.\n\n'
            'TOUR OVERVIEW\nThe Arunachal Discovery signature route stands out as the ultimate Arunachal Pradesh Family Tour. Over 8 days, it captures the dramatic transition from Assam\'s plains into the soaring heights of the Kameng sector, including the cultural City of Eternal Romance at Tezpur.'
        ),
        seo_title='AR-005 | Arunachal Discovery | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Arunachal Discovery package (AR-005 / TG-AR-ADF-005): Bhalukpong, Dirang, Sela Pass, Tawang, Madhuri Lake, Bomdila, Tezpur Brahmaputra cruise, and 4-tier accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Bhalukpong Orchid Sanctuary and Kameng River gateway on Day 01', 1),
            _ih('Dirang Dzong, kiwi orchards, and therapeutic hot springs on Day 02', 2),
            _ih('Sela Pass high-tea, Jaswant Garh Memorial, and heated Tawang suite on Day 03', 3),
            _ih('Tawang Monastery, Tawang Ropeway, and VIP War Memorial Sound & Light Show', 4),
            _ih('Sangetsar (Madhuri) Lake, Bum La Pass, Nuranang Falls, and Tezpur Brahmaputra cruise', 5),
        ],
        days=[
            _day(1, 'GUWAHATI TO BHALUKPONG — ASCENT TO THE FOOTHILL GATEWAY', ('Your grand mountain expedition begins as you touch down at Guwahati Airport. Your dedicated TRAGUIN private chauffeur and tour manager welcome your family with refreshing amenities and your pre-arranged Inner Line Permits. Board your private luxury SUV and begin a scenic drive cutting away from the Brahmaputra plains toward the soaring hills of Arunachal. Arrive at Bhalukpong, the scenic gateway running parallel to the gushing, crystal-clear Kameng River. Check into your handpicked premium resort nestled within the green forest canopy. In the afternoon, take a relaxed family walk through the local Orchid Research Centre, viewing hundreds of rare, exotic tropical orchid blooms under professional guidance. Conclude your evening with a warm, multi-cuisine dinner at the resort property.'), [
                'Sightseeing Included: Foothill scenic drive, Kameng River views, Bhalukpong Orchid Sanctuary.',
                'Evening Experience: Relaxed resort walking trails followed by a detailed mountain briefing with your guide.',
                'Meals Included: Welcome Refreshments & Gourmet Resort Dinner.',
                'Overnight Stay: Premium Riverside Resort, Bhalukpong.',
            ]),
            _day(2, 'BHALUKPONG TO DIRANG — JOURNEY THROUGH AROMATIC KIWI VALLEYS', ('Savor a luxurious breakfast by the river before continuing your scenic ascent up the winding mountain ghat roads toward the pristine Dirang Valley. Watch the vegetation slowly change into towering alpine pine woods and deep terraced valleys. Stop mid-way at the spectacular Tipi Orchid Glasshouse to view unique endangered species. Upon entering Dirang, check into your boutique valley-view eco-lodge. In the afternoon, discover the Dirang Dzong, a 17th-century historic stone fortress displaying timeless Monpa tribal architecture. Walk together through sweeping organic kiwi and apple farms, enjoying a private fresh fruit-tasting session with local growers. Spend your late evening relaxing near the natural therapeutic sulfur Hot Water Springs of Dirang.'), [
                'Sightseeing Included: Tipi Orchid Centre, Dirang Dzong Stone Village, Kiwi & Apple Orchards, Hot Springs.',
                'Evening Experience: A relaxing thermal dip in the Hot Water Springs followed by a traditional dinner.',
                'Meals Included: Buffet Breakfast & Regional Monpa-inspired Dinner.',
                'Overnight Stay: Handpicked Luxury Valley Lodge, Dirang.',
            ]),
            _day(3, 'DIRANG TO TAWANG — OVER THE SNOWY SELA PASS TO THE SPIRITUAL PEAK', ('Awake to the beautiful mountain mist and a fresh breakfast. Today marks a truly legendary segment of your Arunachal Pradesh Family Tour. Settle into your luxury SUV as the vehicle ascends higher into sub-zero domains. Arrive at the towering Sela Pass, standing majestically at 13,700 feet. Marvel at the breathtaking landscapes of snow-blanketed peaks and the pristine, partially frozen Sela Lake reflecting the passing clouds. Enjoy a TRAGUIN Signature Experience: a warm gourmet high-tea served right on the snowy banks of the pass. Continue your descent toward Tawang, stopping to visit the solemn Jaswant Garh War Memorial to hear tales of historic bravery. Arrive in the spiritual capital of Tawang and check into your ultra-luxury heated mountain suite.'), [
                'Sightseeing Included: Sela High Mountain Pass, Sela Glacial Lake, Jaswant Garh War Memorial.',
                'Evening Experience: Signature Mountain High-Tea and sunset photography over the frozen lake limits.',
                'Meals Included: Gourmet Breakfast, Sela Pass High-Tea, & Warm Luxury Dinner.',
                'Overnight Stay: Centrally Heated Luxury Mountain Resort, Tawang.',
            ]),
            _day(4, 'TAWANG — THE GRAND MONASTERY & ALPINE ROPEWAY GLIDES', ('Indulge in a hearty breakfast surrounded by views of soaring peaks. Your morning is dedicated to experiencing the cultural soul of your Premium Arunachal Pradesh Experience. Visit the world-famous Tawang Monastery (Galden Namgyal Lhatse), a massive 400-year-old fortress-monastery perched on a cliff at 10,000 feet. Accompanied by an expert scholar guide, wander through the grand assembly hall, admire the colossal 26-foot gilded Buddha statue, and view timeless sacred manuscripts. Later, experience a thrilling ride on the Tawang Ropeway, gliding gently across pine-forested valleys. In the late afternoon, visit the serene Ani Gompa (Nunneries) and the moving Tawang War Memorial. In the evening, attend a private, interactive cultural discussion inside the monastery complex arranged specially by TRAGUIN specialists.'), [
                'Sightseeing Included: Tawang Monastery, Tawang Ropeway, Ani Gompa Nunnery, Tawang War Memorial.',
                'Evening Experience: VIP seating at the historical Sound & Light Show at the War Memorial complex.',
                'Meals Included: Premium Breakfast & Multi-cuisine Chef\'s Table Dinner.',
                'Overnight Stay: Centrally Heated Luxury Mountain Resort, Tawang.',
            ]),
            _day(5, 'TAWANG — EXCURSION TO THE EERIE STANDING TREES OF MADHURI LAKE', ('Enjoy a late breakfast before boarding your specialized private 4x4 vehicle for an adventurous day excursion toward the high Tibetan border plateaus. Wind past dozens of unnamed high-altitude glacial pools to arrive at the iconic Sangetsar Lake, popularly celebrated as Madhuri Lake. Formed by a massive earthquake, this unique water body features stark, dead tree trunks rising dramatically out of the calm water against a backdrop of snow-covered peaks. Enjoy a warm, catered lakeside hot lunch organized by your tour team. If military permissions permit, take a panoramic drive near the high Bum La Pass at 15,200 feet, marking the official line of control. Return to Tawang by afternoon, spending your evening exploring the local woolen handicraft bazaars.'), [
                'Sightseeing Included: Sangetsar (Madhuri) Lake, P.T. Tso Lake, Bum La Pass road (subject to permit availability).',
                'Evening Experience: Cozy family evening gathered around the resort\'s luxury central fireplace with hot cocoa.',
                'Meals Included: Breakfast, Lakeside Hot Picnic Lunch, & Grand Farewell Dinner.',
                'Overnight Stay: Centrally Heated Luxury Mountain Resort, Tawang.',
            ]),
            _day(6, 'TAWANG TO BOMDILA — THE THUNDERING MIST OF NURANANG FALLS', ('Say goodbye to the high peaks after breakfast and begin your comfortable descent back toward the historic town of Bomdila. Stop midway to experience the jaw-dropping Nuranang Falls (Jung Falls), a spectacular 100-meter vertical white water sheet cascading through lush green cliffs. Feel the cool mountain spray as you walk down flat paths for family photographs. Continue your scenic drive to Bomdila. Check into your premium hotel and spend your afternoon visiting the Bomdila Monastery (GRL Gompa), absorbing panoramic views of the twin peaks of Gorichen and Kangto rising into the clouds. Browse the local arts and crafts center for exquisite hand-woven carpets.'), [
                'Sightseeing Included: Nuranang Waterfalls, Bomdila GRL Gompa, Local Craft Emporium.',
                'Evening Experience: Spectacular sunset viewing from the Bomdila ridge overlooking the Eastern Himalayan ranges.',
                'Meals Included: Breakfast & Authentic Monpa Tribal Style Dinner.',
                'Overnight Stay: Handpicked Premium Hotel, Bomdila.',
            ]),
            _day(7, 'BOMDILA TO TEZPUR — DESCENDING INTO THE CITY OF ETERNAL ROMANCE', ('Savor a final mountain breakfast before your luxury SUV drives you smoothly down the final ghat roads out of Arunachal Pradesh, crossing back into the historic plains of Assam to arrive at Tezpur, the cultural City of Eternal Romance. Check into your premium luxury riverfront property. In the afternoon, enjoy a relaxed Tezpur Sightseeing circuit. Explore the beautiful ancient stone-carvings at Agnigarh Hill, a mythical fortress hill overlooking the expansive Brahmaputra River. Recline on manicured lawns as your guide narrates old tales of royal lovers. Conclude your last evening with a private sunset cruise along the Brahmaputra River organized by your TRAGUIN specialists.'), [
                'Sightseeing Included: Scenic valley descent, Agnigarh Hill ruins, Cole Park lakeside lawns.',
                'Evening Experience: Private sunset cruise along the Brahmaputra River with traditional folk music performances.',
                'Meals Included: Buffet Breakfast & Grand Farewell Celebration Dinner.',
                'Overnight Stay: Premium Luxury Riverfront Hotel, Tezpur.',
            ]),
            _day(8, 'TEZPUR TO GUWAHATI — DEPARTURE WITH UNFORGETTABLE MEMORIES', ('Indulge in a final sumptuous breakfast overlooking the river. Settle into your luxury vehicle for a comfortable highway drive back to Guwahati Airport or Railway Station. Your elite Himalayan family exploration concludes beautifully, leaving you with deep cultural discoveries, timeless family photographs, and unforgettable memories crafted flawlessly by TRAGUIN.'), [
                'Sightseeing Included: Highway transit drive, private airport/station departure transfer.',
                'Meals Included: Premium Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Prashaanti Cottage / Hotel Pemaling | Hotel Gayki Khang Zhang | Siphiyang Sela / Kanyapur Hotel', 'Bhalukpong / Dirang / Tawang (3 Nights) / Bomdila / Tezpur', '07 Nights', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner', 4, 1, description='OPTION 01 – DELUXE: Prashaanti Cottage / Hotel Pemaling (Bhalukpong/Dirang) | Hotel Gayki Khang Zhang (Tawang, 3 Nights) | Siphiyang Sela / Kanyapur Hotel (Bomdila/Tezpur) | Breakfast & Dinner'),
            _hotel('Druk Hotel / Dirang Boutique Resort | Tawang Vista Resort | Central Tavern / Heritage Tezpur', 'Bhalukpong / Dirang / Tawang (3 Nights) / Bomdila / Tezpur', '07 Nights', 'Premium', 'Premium Room', 'Breakfast & Dinner', 4, 2, description='OPTION 02 – PREMIUM: Druk Hotel / Dirang Boutique Resort (Bhalukpong/Dirang) | Tawang Vista Resort (Tawang, 3 Nights) | Central Tavern / Heritage Tezpur (Bomdila/Tezpur) | Breakfast & Dinner'),
            _hotel('WelcomHeritage Marand Lodge | Dondrub Luxury Homestay | Royal Heritage / Landmark Riverfront', 'Bhalukpong / Dirang / Tawang (3 Nights) / Bomdila / Tezpur', '07 Nights', 'Luxury', 'Luxury Room', 'Breakfast & Dinner', 5, 3, description='OPTION 03 – LUXURY: WelcomHeritage Marand Lodge (Bhalukpong/Dirang) | Dondrub Luxury Homestay (Tawang, 3 Nights) | Royal Heritage / Landmark Riverfront (Bomdila/Tezpur) | Breakfast & Dinner'),
            _hotel('Premium Wilderness Eco-Lodges | Vivanta Tawang (Heated Executive Suites) | Boutique Monpa Residences', 'Bhalukpong / Dirang / Tawang (3 Nights) / Bomdila / Tezpur', '07 Nights', 'Ultra Luxury', 'Executive Suite', 'Breakfast & Dinner', 5, 4, description='OPTION 04 – ULTRA LUXURY: Premium Wilderness Eco-Lodges (Bhalukpong/Dirang) | Vivanta Tawang Heated Executive Suites (Tawang, 3 Nights) | Boutique Monpa Residences (Bomdila/Tezpur) | Breakfast & Dinner'),
        ],
        inclusions=[
            _inc_included('Premium Stays: 07 Nights elite accommodation across handpicked properties with customized luxury room heating systems.', 1),
            _inc_included('Gourmet Dining: Daily buffet breakfast and warm multi-course dinners across all destination properties.', 2),
            _inc_included('Luxury Transportation: Private air-conditioned luxury 4x4 SUV dedicated for all transfers, intercity ghat drives, and mountain sightseeing routes.', 3),
            _inc_included('Border Access Support: Pre-cleared processing of mandatory Inner Line Permits (ILPs) and Bum La Pass military check-post document coordination.', 4),
            _inc_included('TRAGUIN Signatures: Private Sela Pass Summit High-Tea, private Brahmaputra sunset cruise, and custom family travel tokens.', 5),
            _inc_included('Welcome Amenities: Traditional royal welcomes, fresh fruit platters, and premium mineral water bottles provided inside your vehicle daily.', 6),
            _inc_included('Assistance & Taxes: 24/7 dedicated support from TRAGUIN holiday specialists, covered tolls, fuel costs, and driver allowances.', 7),
            _inc_excluded('Main Tickets: Commercial flights or main railway tickets to and from Guwahati.', 8),
            _inc_excluded('Monument Entry Fees: Individual entrance tickets or camera permits at specific museums or monasteries.', 9),
            _inc_excluded('Personal Expenses: Personal room service, laundry, telephone bills, and personal tipping allowances.', 10),
            _inc_excluded('Optional Activities: High-altitude adventure sports or travel insurance plans.', 11),
        ],
    )
    return package, itinerary

def build_ar_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AR-006'
    tour_code = 'TRG-ARU-LDS-2026'
    title = 'TRAGUIN Premium Arunachal Pradesh Ladies Tour — Dirang • Tawang Monastery • Sela Pass • Bum La Pass • Sangetsar Lake'
    duration = '06 Nights / 07 Days'
    slug = 'ar-006-arunachal-ladies-tour-dirang-tawang'
    itin_slug = 'ar-006-arunachal-ladies-tour-dirang-tawang-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Arunachal Pradesh / India | Category: Best Arunachal Ladies Tour Package', 2),
            _ph('Destinations: Dirang (2N) • Tawang (4N)', 3),
            _ph('Ideal for: Women-only groups seeking safety, comfort, and sisterhood bonding', 4),
            _ph('Best season: March to June & October to December', 5),
            _ph('Starting price: On Request (Premium Luxury Tier)', 6),
            _ph('Vehicle: Private premium traveler vehicle with trusted escorts | Meal Plan: Premium Breakfast & Dinner', 7),
            _ph('Route Plan: Guwahati Arrival ➔ Dirang (2N) ➔ Tawang (4N) ➔ Guwahati Departure', 8),
            _ph('TRAGUIN Curated Experience Note: Female-only itinerary blending pristine mountain pulse with rich cultural grandeur, premium transport logistics, and handpicked boutique properties.', 9),
            _ph('Premium Handpicked Hotels: Luxury tier only — Norphel House Boutique Hotel Dirang and Dondrub Homestay Luxury Wing / Hotel Mountain View Tawang.', 10),
            _ph('Exclusive Experiences: Sela Pass crossing, Tawang Monastery heritage, Bum La Pass adventure, Sangetsar Lake, Nuranang Waterfalls, and local handicraft shopping.', 11),
            _ph('Important Notes: Inner Line Permits mandatory; specialized 4x4 for Bum La Pass; designed for group photography and cultural storytelling.', 12),
        ],
        moods=['Ladies Tour', 'Luxury', 'Culture', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Arunachal Ladies Tour • Dirang 2N • Tawang 4N • 06 Nights / 07 Days',
        overview=(
            'Embark on an unforgettable Arunachal Pradesh journey with our TRAGUIN curated female-only itinerary. Blending the pristine mountain pulse of the Eastern Himalayas with the rich cultural grandeur of indigenous tribes, this Arunachal ladies tour offers a seamless mix of comfort, safety, and sisterhood bonding, ensuring unforgettable memories.\n\n'
            'THE IMMERSIVE ARUNACHAL LADIES TOUR EXPERIENCE\nArunachal Pradesh is a premier destination for women seeking refreshing clean mountain air, breathtaking landscapes, and immersive cultural heritage. From the misty high-altitude vistas at Sela Pass to the spiritual peace of Tawang Monastery, this specialized female-only holiday delivers elite exclusive experiences.'
        ),
        seo_title='AR-006 | Arunachal Ladies Tour Dirang Tawang | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Arunachal ladies tour (AR-006 / TRG-ARU-LDS-2026): Dirang 2N, Tawang 4N, Sela Pass, Bum La Pass, Sangetsar Lake, luxury hotels only.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Dirang Valley exploration: Dirang Dzong, Monpa villages, and natural hot water springs', 1),
            _ih('Scenic drive to Tawang via majestic Sela Pass at 13,700 feet', 2),
            _ih('Tawang Monastery, Giant Buddha Statue, Ani Gompa, and War Memorial light show', 3),
            _ih('High-altitude adventure to Bum La Pass and Sangetsar (Madhuri) Lake', 4),
            _ih('Nuranang Waterfalls and local handicraft market shopping for Monpa woolen carpets', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN GUWAHATI – DRIVE TO DIRANG VALLEY', ('Your TRAGUIN curated ladies tour begins with a warm welcome by our professional tour manager at Guwahati Airport. Board your private premium traveler vehicle and begin a beautiful journey towards Dirang. Check in at your premium stay nestled amidst spectacular kiwi orchards and enjoy a relaxing evening under the stars.'), [
                'Sightseeing Included: Scenic drive from Guwahati to Dirang Valley.',
                'Evening Experience: Relaxed group welcome dinner under the stars.',
                'Meals Included: Dinner.',
                'Overnight Stay: Norphel House Boutique Hotel / Similar, Dirang Valley.',
            ]),
            _day(2, 'DIRANG VALLEY EXPLORATION & LOCAL CULTURE', ('Explore the best of Dirang with your group. Visit the historic Dirang Dzong, walk through peaceful Monpa tribal villages, and soothe your senses at the natural hot water springs. This curated experience offers deep cultural storytelling and abundant opportunities for dynamic group photography points.'), [
                'Sightseeing Included: Dirang Dzong, Monpa tribal villages, natural hot water springs.',
                'Evening Experience: Group cultural storytelling and photography session.',
                'Meals Included: Breakfast, Dinner.',
                'Overnight Stay: Norphel House Boutique Hotel / Similar, Dirang Valley.',
            ]),
            _day(3, 'SCENIC DRIVE TO TAWANG VIA MAJESTIC SELA PASS', ('Cross the high-altitude threshold as you drive toward Tawang today. Experience the breathtaking landscapes and frozen scenic beauty of the iconic Sela Pass at 13,700 feet. Stop for a hot cup of tea by Paradise Lake before arriving in Tawang. Check into your comfortable premium valley-view stay arranged flawlessly by TRAGUIN.'), [
                'Sightseeing Included: Sela Pass (13,700 ft), Paradise Lake (Sela Lake), scenic mountain drive.',
                'Evening Experience: Warm welcome tea and group acclimatization briefing.',
                'Meals Included: Breakfast, Dinner.',
                'Overnight Stay: Dondrub Homestay Luxury Wing / Hotel Mountain View, Tawang.',
            ]),
            _day(4, 'TAWANG MONASTERY & SPIRITUAL HERITAGE SIGHTSEEING', ('Immerse your group in profound heritage by visiting the legendary Tawang Monastery, the second largest Buddhist monastery in the world. Later, explore the giant Buddha Statue, the Ani Gompa nunneries, and witness a moving evening sound and light show at the Tawang War Memorial, leaving you with unforgettable memories.'), [
                'Sightseeing Included: Tawang Monastery, Giant Buddha Statue, Ani Gompa, Tawang War Memorial.',
                'Evening Experience: Sound and light show at Tawang War Memorial.',
                'Meals Included: Breakfast, Dinner.',
                'Overnight Stay: Dondrub Homestay Luxury Wing / Hotel Mountain View, Tawang.',
            ]),
            _day(5, 'HIGH-ALTITUDE ADVENTURE TO BUM LA PASS & MADHURI LAKE', ('An adrenaline-filled day of exploration as you take local premium 4x4 vehicles up to the Indo-China border at Bum La Pass. On your return route, admire the breathtaking landscapes surrounding the famous Sangetsar Lake (Madhuri Lake). Spend a beautiful afternoon enjoying local piping-hot momos amidst high mountain ridges.'), [
                'Sightseeing Included: Bum La Pass, Sangetsar (Madhuri) Lake, high-altitude mountain ridges.',
                'Evening Experience: Group momo tasting at a local mountain café.',
                'Meals Included: Breakfast, Dinner.',
                'Overnight Stay: Dondrub Homestay Luxury Wing / Hotel Mountain View, Tawang.',
            ]),
            _day(6, 'HIDDEN WATERFALLS & LOCAL SHOPPING LEISURE', ('Discover the spectacular scenic beauty of Nuranang Waterfalls (Jang Falls), where white water cascading down mountain cliffs offers incredible photography backdrops. In the afternoon, explore local handicraft markets to secure unique handwoven Monpa woolen carpets, traditional masks, and authentic souvenirs.'), [
                'Sightseeing Included: Nuranang Waterfalls (Jang Falls), local handicraft markets.',
                'Evening Experience: Leisure shopping and group farewell dinner.',
                'Meals Included: Breakfast, Dinner.',
                'Overnight Stay: Dondrub Homestay Luxury Wing / Hotel Mountain View, Tawang.',
            ]),
            _day(7, 'TAWANG DEPARTURE VIA GUWAHATI', ('Savor a final mountain breakfast with your wonderful group. Take a comfortable private transfer back to the airport for your onward journey. Your classic Arunachal ladies tour concludes with lifelong friendships, empowering stories, and lasting memories designed perfectly by TRAGUIN.'), [
                'Sightseeing Included: Private transfer Tawang to Guwahati Airport.',
                'Meals Included: Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Norphel House Boutique Hotel / Similar | Dondrub Homestay Luxury Wing / Hotel Mountain View', 'Dirang Valley (2 Nights) / Tawang (4 Nights)', '06 Nights', 'Luxury', 'Luxury Room', 'Breakfast & Dinner', 5, 1, description='OPTION 03 – LUXURY: Norphel House Boutique Hotel / Similar (Dirang Valley, 2 Nights) | Dondrub Homestay Luxury Wing / Hotel Mountain View (Tawang, 4 Nights) | Breakfast & Dinner'),
        ],
        inclusions=[
            _inc_included('Premium Stays: 06 Nights luxury accommodation at handpicked ladies-group-friendly properties (Luxury tier only).', 1),
            _inc_included('Gourmet Dining: Daily buffet breakfast and curated dinners across all properties.', 2),
            _inc_included('Luxury Transportation: Private premium traveler vehicle with trusted escorts for all transfers and sightseeing.', 3),
            _inc_included('Bum La 4x4: Specialized local mountain-terrain 4x4 vehicle for the high-altitude Bum La Pass day excursion.', 4),
            _inc_included('Permit Handling: Full handling and pre-arrangement of Arunachal Pradesh Inner Line Permits (ILP).', 5),
            _inc_included('TRAGUIN Support: 24/7 dedicated tour manager and concierge assistance throughout the journey.', 6),
            _inc_excluded('Main Flights / Rail: Intercity transport tickets to and from Guwahati.', 7),
            _inc_excluded('Monument Entry: Individual entry tickets at museums, light shows, and monasteries.', 8),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, spa sessions, and tips.', 9),
            _inc_excluded('Optional Tours: Travel or medical insurance coverage plans.', 10),
        ],
    )
    return package, itinerary

def build_ar_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AR-007'
    tour_code = 'TRG-ARU-SNR-2026'
    title = 'TRAGUIN Premium Arunachal Pradesh Senior Citizen Leisure Ladies Tour — Bomdila • Dirang Valley • Sangti Valley • Tawang Calm Escapes'
    duration = '06 Nights / 07 Days'
    slug = 'ar-007-senior-citizen-ladies-tour-bomdila-dirang-tawang'
    itin_slug = 'ar-007-senior-citizen-ladies-tour-bomdila-dirang-tawang-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Arunachal Pradesh / India | Category: Premium Arunachal Family Tour & Senior Leisure Package', 2),
            _ph('Destinations: Bomdila (1N) • Dirang (3N) • Tawang (2N)', 3),
            _ph('Ideal for: Senior citizen ladies seeking gentle pacing and zero fatigue', 4),
            _ph('Best season: March to June & October to December', 5),
            _ph('Starting price: On Request (Premium Luxury Tier)', 6),
            _ph('Vehicle: Premium comfortable luxury SUV configured for maximum road comfort | Meal Plan: Premium Breakfast & Dinner', 7),
            _ph('Route Plan: Guwahati Arrival ➔ Bomdila (1N) ➔ Dirang (3N) ➔ Tawang (2N) ➔ Guwahati Departure', 8),
            _ph('TRAGUIN Curated Experience Note: Intentionally paced route with easily accessible paths, premium comfortable SUVs, minimal high-altitude strain, and dedicated on-ground helpers.', 9),
            _ph('Premium Handpicked Hotels: Luxury tier only — Hotel Elysium Bomdila, Norphel House Luxury Wing Dirang, Dondrub Luxury Boutique Stay Tawang.', 10),
            _ph('Exclusive Experiences: Bomdila Monastery, Sangti Valley, Dirang Dzong, therapeutic hot springs, gentle Sela Pass crossing, Tawang spiritual sightseeing.', 11),
            _ph('Important Notes: Frequent leisurely stops planned; accessible lower grounds of Tawang Monastery; designed for peaceful rejuvenation.', 12),
        ],
        moods=['Senior Leisure', 'Ladies Tour', 'Luxury', 'Culture'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Senior Citizen Ladies Tour • Bomdila 1N • Dirang 3N • Tawang 2N • 06 Nights / 07 Days',
        overview=(
            'Embark on an unforgettable Arunachal Pradesh journey with our TRAGUIN curated senior citizen leisure ladies tour. Intentionally paced to ensure zero fatigue, this beautiful route blends majestic high-mountain landscapes with deep spiritual heritage and comfortable ground transfers, delivering unforgettable memories.\n\n'
            'THE IMMERSIVE ARUNACHAL SENIOR LADIES LEISURE EXPERIENCE\nArunachal Pradesh serves as a breathtaking sanctuary for senior travelers seeking natural scenic beauty, crisp Himalayan air, and enriching cultural immersion. Designed with easily accessible paths, premium comfortable SUVs, and minimal high-altitude strain, this exclusive vacation offers a premium Arunachal experience.'
        ),
        seo_title='AR-007 | Senior Citizen Ladies Tour Bomdila Dirang Tawang | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Arunachal senior ladies tour (AR-007 / TRG-ARU-SNR-2026): Bomdila 1N, Dirang 3N, Tawang 2N, Sangti Valley, luxury hotels only.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Gentle foothills drive to Bomdila with serene monastery visit on Day 02', 1),
            _ih('Relaxed Sangti Valley exploration and kiwi orchards walk at easy pace', 2),
            _ih('Dirang Dzong heritage and therapeutic sulphur hot springs wellness treat', 3),
            _ih('Gentle Sela Pass crossing with frequent leisurely photo stops to Tawang', 4),
            _ih('Accessible Tawang Monastery courtyards and handicrafts emporium shopping', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN GUWAHATI – SCENIC FOOTHILLS DRIVE TO BOMDILA', ('Your TRAGUIN specialized senior ladies tour begins with a warm welcome at Guwahati Airport by our dedicated support team. Step into your premium, well-padded luxury vehicle configured for maximum road comfort. Travel through lush tea estates as you gently ascend to Bomdila for a relaxed overnight stay.'), [
                'Sightseeing Included: Scenic drive through Assam tea estates to Bomdila.',
                'Evening Experience: Relaxed check-in and gentle welcome dinner.',
                'Meals Included: Dinner.',
                'Overnight Stay: Hotel Elysium / Similar, Bomdila.',
            ]),
            _day(2, 'BOMDILA MONASTERY VISIT & DRIVE TO GENTLE DIRANG VALLEY', ('Enjoy a beautiful crisp morning exploring the serene Bomdila Monastery with easily flat walking routes. Later, take a smooth short drive to the lower elevation of Dirang Valley. Check in at your luxury orchard resort arranged by TRAGUIN, designed perfectly for peaceful rejuvenation and mountain unwinding.'), [
                'Sightseeing Included: Bomdila Monastery, scenic drive to Dirang Valley.',
                'Evening Experience: Peaceful mountain unwinding at the orchard resort.',
                'Meals Included: Breakfast, Dinner.',
                'Overnight Stay: Norphel House Luxury Wing, Dirang Valley.',
            ]),
            _day(3, 'RELAXED SANGTI VALLEY EXPLORATION & KIWI ORCHARDS WALK', ('Immerse your group in absolute scenic beauty without strenuous walking. Spend a peaceful day driving through Sangti Valley, listening to the gentle gurgling of fresh alpine rivers. Walk at your own easy pace through local black-necked crane sanctuaries and lush organic kiwi orchards, capturing beautiful memory points.'), [
                'Sightseeing Included: Sangti Valley drive, black-necked crane sanctuary, kiwi orchards.',
                'Evening Experience: Leisure photography and relaxed group dinner.',
                'Meals Included: Breakfast, Dinner.',
                'Overnight Stay: Norphel House Luxury Wing, Dirang Valley.',
            ]),
            _day(4, 'DIRANG HERITAGE SITES & THERAPEUTIC HOT SPRINGS', ('Discover the rich local heritage of the Monpa community. Visit the accessible lower grounds of the ancient Dirang Dzong. Later, enjoy a soothing afternoon near the natural sulphur hot springs, known for their therapeutic properties—a perfect wellness treat curated beautifully by our travel specialists.'), [
                'Sightseeing Included: Dirang Dzong, natural sulphur hot springs.',
                'Evening Experience: Therapeutic hot springs wellness session.',
                'Meals Included: Breakfast, Dinner.',
                'Overnight Stay: Norphel House Luxury Wing, Dirang Valley.',
            ]),
            _day(5, 'GENTLE MOUNTAIN CROSSING TO TAWANG HOLY TOWN', ('Travel comfortably as your premium vehicle navigates across the scenic Sela Pass corridor. Frequent leisurely stops are planned for you to capture breathtaking landscapes without sudden physical strain. Arrive smoothly in Tawang and enjoy a hot traditional herbal tea welcome at your luxury handpicked hotel.'), [
                'Sightseeing Included: Sela Pass corridor with leisurely photo stops, Tawang arrival.',
                'Evening Experience: Traditional herbal tea welcome and rest for acclimatization.',
                'Meals Included: Breakfast, Dinner.',
                'Overnight Stay: Dondrub Luxury Boutique Stay, Tawang.',
            ]),
            _day(6, 'TAWANG SPIRITUAL SIGHTSEEING & HANDICRAFTS EMPORIUM', ('Spend a memorable morning exploring the lower, accessible courtyards of the historic Tawang Monastery. Soak in the peaceful prayers and ancient spiritual vibes. In the afternoon, visit the local government handicraft emporium to shop for soft handwoven pashminas, exquisite wooden crafts, and authentic souvenirs.'), [
                'Sightseeing Included: Tawang Monastery accessible courtyards, handicraft emporium.',
                'Evening Experience: Leisure shopping for pashminas and wooden crafts.',
                'Meals Included: Breakfast, Dinner.',
                'Overnight Stay: Dondrub Luxury Boutique Stay, Tawang.',
            ]),
            _day(7, 'TAWANG DEPARTURE VIA GUWAHATI', ('Savor a hearty, nutritious final breakfast looking out at misty mountain peaks. Your professional chauffeur ensures a smooth and secure drive back towards Guwahati airport. Your premium Arunachal ladies tour concludes with warm hearts, relaxed minds, and beautiful memories designed flawlessly by TRAGUIN.'), [
                'Sightseeing Included: Private transfer Tawang to Guwahati Airport.',
                'Meals Included: Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Hotel Elysium / Similar | Norphel House Luxury Wing | Dondrub Luxury Boutique Stay', 'Bomdila (1 Night) / Dirang Valley (3 Nights) / Tawang (2 Nights)', '06 Nights', 'Luxury', 'Luxury Room', 'Breakfast & Dinner', 5, 1, description='OPTION 03 – LUXURY: Hotel Elysium / Similar (Bomdila, 1 Night) | Norphel House Luxury Wing (Dirang Valley, 3 Nights) | Dondrub Luxury Boutique Stay (Tawang, 2 Nights) | Breakfast & Dinner'),
        ],
        inclusions=[
            _inc_included('Premium Stays: 06 Nights luxury accommodation at senior-comfort handpicked properties (Luxury tier only).', 1),
            _inc_included('Gourmet Dining: Daily buffet breakfast and curated dinners across all properties.', 2),
            _inc_included('Luxury Transportation: Premium well-padded luxury SUV configured for maximum road comfort with dedicated on-ground helpers.', 3),
            _inc_included('Permit Handling: Full handling and pre-arrangement of Arunachal Pradesh Inner Line Permits (ILP).', 4),
            _inc_included('Gentle Pacing: Frequent leisurely stops and accessible sightseeing routes designed for zero fatigue.', 5),
            _inc_included('TRAGUIN Support: 24/7 dedicated support team and concierge assistance throughout the journey.', 6),
            _inc_excluded('Main Flights / Rail: Intercity transport tickets to and from Guwahati.', 7),
            _inc_excluded('Monument Entry: Individual entry tickets at museums and monasteries.', 8),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, spa sessions, and tips.', 9),
            _inc_excluded('Optional Tours: Travel or medical insurance coverage plans.', 10),
        ],
    )
    return package, itinerary

def build_ar_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AR-008'
    tour_code = 'TRAGUIN-TAWANG-LUX-008'
    title = 'TRAGUIN Premium Arunachal Pradesh Tour Package — Bespoke Luxury Tawang & Eastern Himalayas Expedition'
    duration = '06 Nights / 07 Days'
    slug = 'ar-008-bespoke-luxury-tawang-eastern-himalayas'
    itin_slug = 'ar-008-bespoke-luxury-tawang-eastern-himalayas-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Arunachal Pradesh / India | Category: Luxury / Premium Holidays | Budget Category: Ultra Luxury Elite', 2),
            _ph('Destinations: Guwahati • Bhalukpong • Dirang • Tawang • Bomdila', 3),
            _ph('Ideal for: Luxury Seekers, Honeymooners, Families, Culture Connoisseurs', 4),
            _ph('Best season: October to May (Spring & Winter Splendor)', 5),
            _ph('Starting price: On Request (Premium Bespoke Quoting)', 6),
            _ph('Vehicle: Private top-tier Toyota Innova Crysta / Luxury SUV | Meal Plan: Ultimate Premium MAPAI (Daily Sumptuous Breakfast & Elite Curated Dinners)', 7),
            _ph('Route Plan: Guwahati → Bhalukpong → Dirang → Tawang → Bomdila → Guwahati Departure', 8),
            _ph('TRAGUIN Curated Experience: 24/7 dedicated local concierge support, inner line permit coordination, private local monastery guides, and exclusive local culinary tastings.', 9),
            _ph('TRAGUIN Signature Experience: Exclusive private butter-lamp lighting ceremony inside the historic Tawang Monastery.', 10),
            _ph('Curated by TRAGUIN Experts: Every detail of your high-altitude itinerary is meticulously planned for seamless transitions and comfortable pace.', 11),
            _ph('Premium Handpicked Hotels: Region\'s finest luxury properties with heated amenities and spectacular panoramic views.', 12),
            _ph('Shopping & Local Experiences: Hand-woven Monpa wool rugs, wooden masks, traditional jewelry, thukpa, momos, and butter tea.', 13),
            _ph('Important Notes: High-altitude acclimatization above 13,000 ft; ILP and PAP mandatory; book 60–90 days ahead for peak seasons.', 14),
        ],
        moods=['Luxury', 'Honeymoon', 'Family', 'Culture'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Bespoke Quoting)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Bespoke Luxury Tawang • Bhalukpong • Dirang • Tawang • Bomdila • 06 Nights / 07 Days',
        overview=(
            'Embark on an immersive, ultra-private journey curated exclusively for the discerning global traveler. Experience the mystical charm, dramatic valleys, and ancient monasteries of the Land of the Dawn-Lit Mountains with TRAGUIN\'s signature elite hospitality.\n\n'
            'TOUR OVERVIEW\nWelcome to a realm where pristine cloud-kissed heights meet ancient Buddhist lineage. This signature luxury Arunachal Pradesh travel experience is meticulously crafted to blend thrilling Himalayan transitions with handpicked premium accommodations, private chauffeured luxury SUVs, and bespoke cultural interactions.'
        ),
        seo_title='AR-008 | Bespoke Luxury Tawang Expedition | TRAGUIN',
        seo_description='Ultra-luxury 06 Nights / 07 Days Tawang package (AR-008 / TRAGUIN-TAWANG-LUX-008): Bhalukpong, Dirang, Sela Pass, Tawang Monastery, Bum La Pass, Madhuri Lake, Bomdila, and 4-tier elite accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('VIP reception and Kameng River sunset views at Bhalukpong on Day 01', 1),
            _ih('Tipi Orchid Sanctuary, Dirang Dzong fortress, and natural hot springs on Day 02', 2),
            _ih('Sela Pass (13,700 ft), Paradise Lake, Jaswant Garh Memorial, and Nuranang Waterfall', 3),
            _ih('Tawang Monastery private tour, Urgelling Monastery, and VIP Light & Sound Show', 4),
            _ih('Bum La Pass, Madhuri Lake, and Bomdila Monastery sunset viewpoint finale', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN GUWAHATI & PRIVATE SCENIC TRANSFER TO BHALUKPONG', ('Your extraordinary high-altitude expedition begins the moment you touch down at Guwahati International Airport. You will be greeted with a warm, VIP reception by our private chauffeured escort, signifying your entry into the exclusive care of TRAGUIN. Board your luxury SUV and begin a beautiful, scenic journey winding past the lush plains of Assam towards the misty gateway of Arunachal Pradesh—Bhalukpong. Located along the banks of the roaring Kameng River, Bhalukpong provides a tranquil, comforting environment that is perfect for relaxing after your travels. Upon arrival, check into your premium riverfront resort chalet. Spend your afternoon wandering through the beautifully manicured property gardens or capture stunning landscape photographs of the river as the sun sets behind the hills. In the evening, enjoy a specially curated welcome dinner featuring subtle, locally inspired culinary touches.'), [
                'Sightseeing Included: Scenic drive along the Brahmaputra basin, Kameng River sunset views, Bhalukpong nature trails.',
                'Optional Activities: Traditional riverside high-tea experience with a private setup.',
                'Evening Experience: Gourmet welcoming dinner and private briefing with your personal guide.',
                'Meals Included: Curated Dinner (Premium MAPAI).',
                'Overnight Stay: Premium Riverside Eco-Resort / Luxury Lodge, Bhalukpong.',
            ]),
            _day(2, 'BHALUKPONG TO DIRANG VIA THE SPECTACULAR TIPI ORCHID SANCTUARY', ('Enjoy an early morning breakfast surrounded by the soothing sounds of the river before checking out to continue your journey into the pristine sub-tropical valleys of Dirang. Your first stop is the famous Tipi Orchid Sanctuary, a beautifully curated botanical dome that houses over several hundred rare and exotic orchid species. As your private luxury vehicle winds higher into the mountains, the air becomes crisp and the scenery transitions into breathtaking terraced farms and traditional Monpa tribal villages. As you enter the beautiful Dirang Valley, check into your boutique luxury valley resort. Spend your afternoon exploring the historic Dirang Dzong—a centuries-old stone fortress that looks out over the entire valley. Afterward, take a relaxing walk down to the soothing local hot springs, renowned for their rejuvenating and mineral-rich natural waters.'), [
                'Sightseeing Included: Tipi Orchid Research Centre, Dirang Dzong historical fortress, Dirang River Valley viewpoint, Natural Hot Springs.',
                'Optional Activities: A private, guided interaction with Monpa village elders to learn about traditional architecture.',
                'Evening Experience: Leisurely evening stroll through the orchard trails followed by a multi-course dinner.',
                'Meals Included: Sumptuous Breakfast & Curated Dinner.',
                'Overnight Stay: Elite Boutique Valley Resort, Dirang.',
            ]),
            _day(3, 'HIGH-ALTITUDE JOURNEY FROM DIRANG TO TAWANG VIA THE MAJESTIC SELA PASS', ('Today marks one of the most awe-inspiring legs of your journey as you ascend to the mystical city of Tawang. After a fresh breakfast, your luxury SUV begins climbing towards the high-altitude Sela Pass, which stands at an incredible 13,700 feet above sea level. This high mountain pass offers panoramic views of endless, snow-capped peaks. Pause here to witness the tranquil beauty of Paradise Lake (Sela Lake), where crystal-clear waters perfectly mirror the surrounding blue skies and frozen crags. After crossing the pass, your journey continues with a respectful stop at the Jaswant Garh War Memorial, a historic site dedicated to the legendary bravery of Indian soldiers. From there, admire the spectacular view of Nuranang Falls (Bong Bong Falls), as it plunges down a dramatic 100 meters through the lush greenery. Arrive in Tawang by the late afternoon, where you will check into your handpicked premium luxury suite, complete with heated amenities and stunning alpine views.'), [
                'Sightseeing Included: Sela Pass (13,700 ft), Paradise Lake, Jaswant Garh War Memorial, Nuranang Waterfall.',
                'Optional Activities: A scenic hot coffee stop at the high-altitude pass, hosted privately by your chauffeur guide.',
                'Evening Experience: Relaxing in your heated premium room to properly acclimate to the beautiful high-altitude environment.',
                'Meals Included: Sumptuous Breakfast & Curated Dinner.',
                'Overnight Stay: Handpicked Premium Luxury Suite, Tawang.',
            ]),
            _day(4, 'IMMERSIVE EXPLORATION OF TAWANG MONASTERY & LOCAL CULTURAL TREASURES', ('Awake to the peaceful, resonant sounds of monastic horns echoing across the valley. Today is completely dedicated to exploring the rich culture and spiritual legacy of Tawang. Your morning begins with a private, guided tour of the magnificent Tawang Monastery (Galden Namgyal Lhatse). Founded in the 17th century, it is the largest monastery in India and stands proudly as the second largest in the entire world. Explore its grand assembly halls, admire the majestic three-story golden Buddha statue, and view its carefully preserved, ancient illuminated manuscripts. Next, visit the peaceful Urgelling Monastery, the historic birthplace of the 6th Dalai Lama. In the afternoon, explore the moving Tawang War Memorial to pay tribute to local heroes, and visit the Craft Centre to see beautiful hand-woven carpets and traditional Monpa woodcarvings. Conclude your day with an elegant evening experience, watching the spectacular light and sound show that beautifully brings Tawang\'s rich history to life.'), [
                'Sightseeing Included: Tawang Monastery, Urgelling Monastery, Tawang War Memorial, Local Handicraft Emporium, Giant Buddha Statue.',
                'Optional Activities: A private prayer and butter-lamp lighting ceremony inside the main monastery hall.',
                'Evening Experience: VIP seating at the Tawang Light & Sound Show, followed by an authentic dinner.',
                'Meals Included: Sumptuous Breakfast & Curated Dinner.',
                'Overnight Stay: Handpicked Premium Luxury Suite, Tawang.',
            ]),
            _day(5, 'PRIVATE EXPEDITION TO THE BREATHTAKING MADHURI LAKE & BUM LA PASS', ('Prepare for an unforgettable high-altitude adventure as you journey towards the international border to visit the legendary Bum La Pass, standing at an incredible 15,200 feet above sea level. This high mountain pass offers rare, panoramic views of the Tibetan plateau. Your journey continues to the stunning Shonga-tser Lake, famously known as Madhuri Lake. Surrounded by dramatic, snow-capped peaks and featuring unique, submerged tree trunks, this lake offers one of the most iconic and beautiful landscapes in the entire Eastern Himalayas. As you explore the area, walk along the wooden pathways and capture stunning photographs of the serene waters. Enjoy a premium, hot picnic lunch set up nearby, surrounded by the crisp mountain air. Return to your luxury suite in Tawang by late afternoon to unwind, relax, and share stories from an incredible day of high-altitude exploration.'), [
                'Sightseeing Included: Bum La Pass (Indo-China Border), Madhuri Lake (Shonga-tser Lake), PT Tso (Pankang Teng Tso Lake).',
                'Optional Activities: A private, warm gourmet picnic lunch served by the lakeside.',
                'Evening Experience: Leisure time to explore the local Tawang markets for unique, hand-crafted souvenirs.',
                'Meals Included: Sumptuous Breakfast & Curated Dinner.',
                'Overnight Stay: Handpicked Premium Luxury Suite, Tawang.',
            ]),
            _day(6, 'SCENIC MOUNTAIN DESCENT FROM TAWANG TO THE PANORAMIC SLOPES OF BOMDILA', ('Today, begin your scenic descent from Tawang, traveling back through the dramatic mountain passes towards the beautiful town of Bomdila. Perched gracefully along high ridges, Bomdila offers magnificent, sweeping views of the snow-capped Kangto and Gorichen mountain peaks. Upon arrival, check into your premium room and visit the beautiful Bomdila Monastery (Gontse Gaden Rabgyel Lling). This peaceful spiritual center features stunning Tibetan architecture and vibrant, colorful murals. Later, head to the local Bomdila Viewpoint as evening approaches to watch a spectacular sunset, casting a warm, golden glow over the entire mountain landscape.'), [
                'Sightseeing Included: Bomdila Monastery, Local Apple Orchards (seasonal), Bomdila Viewpoint, Local Emporium.',
                'Optional Activities: A private evening interaction with a local artisan to learn about traditional mask-making.',
                'Evening Experience: A special farewell dinner featuring a curated blend of fine local flavors and classic continental cuisine.',
                'Meals Included: Sumptuous Breakfast & Curated Dinner.',
                'Overnight Stay: Premium Luxury Mountain Lodge, Bomdila.',
            ]),
            _day(7, 'BOMDILA TO GUWAHATI & ONWARD JOURNEY DEPARTURE', ('Enjoy your final morning breakfast surrounded by the crisp, fresh mountain air of Bomdila. Afterward, your private luxury SUV will guide you on a smooth, scenic descent back down to the plains of Assam. This relaxing drive offers a perfect opportunity to look back on the incredible landscapes, ancient monasteries, and unforgettable moments you\'ve experienced during your trip. You will be chauffeured directly to Guwahati International Airport or the railway station to connect with your onward flight or journey home. As you prepare for your departure, you carry with you a collection of beautiful, lasting memories of the Land of the Dawn-Lit Mountains—all beautifully crafted and looked after by TRAGUIN.'), [
                'Sightseeing Included: Scenic foothills transition, views of the expansive Assam plains.',
                'Optional Activities: A brief, afternoon stop to purchase authentic, fresh Assam tea before heading to the airport.',
                'Evening Experience: VIP drop-off at the airport terminal for a smooth checkout.',
                'Meals Included: Sumptuous Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Prashanti Cottage Deluxe Room | Hotel Pemaling Standard Valley Room | Hotel Gakyi Khang Zhang Standard Room Tier | Hotel Siphiyang Phong Deluxe Ridge View', 'Bhalukpong (1 Night) / Dirang (1 Night) / Tawang (3 Nights) / Bomdila (1 Night)', '06 Nights', 'Deluxe', 'Deluxe Room', 'MAPAI (Breakfast & Dinner)', 4, 1, description='OPTION 01 – DELUXE: Prashanti Cottage (Bhalukpong, 1 Night) | Hotel Pemaling Standard Valley Room (Dirang, 1 Night) | Hotel Gakyi Khang Zhang (Tawang, 3 Nights) | Hotel Siphiyang Phong (Bomdila, 1 Night) | MAPAI'),
            _hotel('Wild West Resort Premium River Cabin | Dirang Boutique Hearth Premium View Room | Tawang Crest Resort Premium Balcony Room | Ecolodge Bomdila Premium Suite Tier', 'Bhalukpong (1 Night) / Dirang (1 Night) / Tawang (3 Nights) / Bomdila (1 Night)', '06 Nights', 'Premium', 'Premium Room', 'MAPAI (Breakfast & Dinner)', 4, 2, description='OPTION 02 – PREMIUM: Wild West Resort (Bhalukpong, 1 Night) | Dirang Boutique Hearth (Dirang, 1 Night) | Tawang Crest Resort (Tawang, 3 Nights) | Ecolodge Bomdila (Bomdila, 1 Night) | MAPAI'),
            _hotel('Druk Deorali Luxury Retreat Luxury Villa | The Norphel House Resort Luxury Valley Suite | Dondrub Heritage Inn Luxury Heated Suite | Hotel Tsepal Yangjom Luxury Classic Executive', 'Bhalukpong (1 Night) / Dirang (1 Night) / Tawang (3 Nights) / Bomdila (1 Night)', '06 Nights', 'Luxury', 'Luxury Suite', 'MAPAI (Breakfast & Dinner)', 5, 3, description='OPTION 03 – LUXURY: Druk Deorali Luxury Retreat (Bhalukpong, 1 Night) | The Norphel House Resort (Dirang, 1 Night) | Dondrub Heritage Inn (Tawang, 3 Nights) | Hotel Tsepal Yangjom (Bomdila, 1 Night) | MAPAI'),
            _hotel('TRAGUIN Elite Signature Hideaway Presidential Pool Cottage | The Norphel House Luxury Estate Royal Orchid Suite | Vivanta Tawang / Elite Luxury Sanctuary | The High-Ridge Luxury Manor Grand Imperial Suite', 'Bhalukpong (1 Night) / Dirang (1 Night) / Tawang (3 Nights) / Bomdila (1 Night)', '06 Nights', 'Ultra Luxury', 'Presidential / Imperial Suite', 'MAPAI (Breakfast & Dinner)', 5, 4, description='OPTION 04 – ULTRA LUXURY: TRAGUIN Elite Signature Hideaway (Bhalukpong, 1 Night) | The Norphel House Luxury Estate (Dirang, 1 Night) | Vivanta Tawang Elite Sanctuary (Tawang, 3 Nights) | The High-Ridge Luxury Manor (Bomdila, 1 Night) | MAPAI'),
        ],
        inclusions=[
            _inc_included('Luxury Lodging: 06 Nights in premium handpicked properties.', 1),
            _inc_included('Premium Meal Plan: Daily hot breakfasts and multi-course dinners.', 2),
            _inc_included('Private Elite Fleet: Premium SUV (Innova Crysta) dedicated for all transfers.', 3),
            _inc_included('VIP Paperwork: Coordination of Inner Line Permits (ILP) and Protected Area Permits.', 4),
            _inc_included('Local Guide Services: Private expert guides for Tawang Monastery tours.', 5),
            _inc_included('Bespoke Touches: Welcome amenities, local fruit baskets, and mineral water.', 6),
            _inc_included('24/7 Concierge: Unwavering remote assistance from TRAGUIN support teams.', 7),
            _inc_excluded('Airfare & Rail tickets: Flights to/from Guwahati are excluded.', 8),
            _inc_excluded('Bum La Pass Transport: Local Arunachal SUV union vehicle charges.', 9),
            _inc_excluded('Entry & Camera Tickets: Monument entry fees paid directly.', 10),
            _inc_excluded('Personal Discretionary Expenses: Laundry, liquor, and tips.', 11),
            _inc_excluded('Insurance Cover: Emergency medical or travel insurance cover.', 12),
            _inc_excluded('Unforeseen Overheads: Extra costs from roadblocks or landslips.', 13),
        ],
    )
    return package, itinerary

def build_ar_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AR-009'
    tour_code = 'TRAGUIN-AR-009'
    title = 'Best Arunachal Pradesh Tour Package — Monastery & Mountains Premium Luxury Holiday'
    duration = '07 Nights / 08 Days'
    slug = 'ar-009-monastery-mountains-premium-luxury'
    itin_slug = 'ar-009-monastery-mountains-premium-luxury-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Arunachal Pradesh / India | Category: Adventure & Luxury Heritage', 2),
            _ph('Destinations: Guwahati • Bhalukpong • Dirang • Tawang • Bomdila • Guwahati', 3),
            _ph('Ideal for: Honeymooners, Families, Luxury Seekers', 4),
            _ph('Best season: October to May', 5),
            _ph('Starting price: On Request (Premium FIT)', 6),
            _ph('Vehicle: Premium SUV (Innova Crysta / Luxury 4x4) | Meal Plan: Modified American Plan (Breakfast & Dinner)', 7),
            _ph('Route Plan: Guwahati ➔ Bhalukpong ➔ Dirang ➔ Tawang ➔ Bomdila ➔ Guwahati', 8),
            _ph('TRAGUIN Curated Experience Note: Handcrafted leisurely pace, handpicked luxury accommodations, inner-line permit assistance, private local expert guides, and continuous remote monitoring.', 9),
            _ph('TRAGUIN Signature Experience: Private cultural interactions with Monpa community elders to explore ancient Buddhist traditions.', 10),
            _ph('Curated by TRAGUIN Experts: Pacing designed carefully to allow smooth acclimation across the high-altitude Sela Pass loop.', 11),
            _ph('Premium Handpicked Hotels: Elite properties featuring modern central heating, local decor elements, and exceptional mountain views.', 12),
            _ph('Shopping & Local Experiences: Monpa hand-woven woolen carpets, wooden masks, kiwi wine, Thangka scrolls, Yak wool shawls, Dragon Café thukpa and momos.', 13),
            _ph('Important Notes: ILP/PAP permits 15 days prior; heavy woolens essential; acclimatize on Day 2 in Dirang before Sela Pass; early booking strongly recommended.', 14),
        ],
        moods=['Adventure', 'Luxury', 'Heritage', 'Honeymoon'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium FIT)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Monastery & Mountains • Bhalukpong • Dirang • Tawang • Bomdila • 07 Nights / 08 Days',
        overview=(
            'Welcome to the land of the dawn-lit mountains. Embark on an extraordinary journey through towering peaks, mystical valleys, and ancient Buddhist heritage with our signature Arunachal Pradesh Tour Package. Tailored specifically for discerning travelers, this Arunachal Pradesh Family Tour and Arunachal Pradesh Honeymoon Package weaves breathtaking landscapes into curated experiences.\n\n'
            'PREMIUM ARUNACHAL PRADESH EXPERIENCE\nAs one of India\'s most pristine, unexplored eco-tourism frontiers, this region promises dramatic vertical topography paired with unique cultural wealth. TRAGUIN Arunachal Pradesh Packages are meticulously engineered to bring you close to iconic attractions like the spectacular Sela Pass and the legendary Tawang Monastery while ensuring premium stays.'
        ),
        seo_title='AR-009 | Monastery & Mountains Premium Luxury | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Arunachal package (AR-009 / TRAGUIN-AR-009): Bhalukpong, Dirang, Sela Pass, Tawang, Bum La Pass, Madhuri Lake, Bomdila, Brahmaputra cruise, Kamakhya Temple.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Bhalukpong foothill gateway with Kameng riverbank sunset and tribal storytelling bonfire', 1),
            _ih('Tipi Orchidarium, Dirang Dzong, kiwi orchards, and Dirang River hot springs', 2),
            _ih('Sela Pass (13,700 ft), Sela Lake, Jaswant Garh Memorial, and Nuranang Waterfalls', 3),
            _ih('Tawang Monastery, Urgelling Monastery, Bum La Pass, and Madhuri Lake excursion', 4),
            _ih('Brahmaputra sundowner dinner cruise and optional Kamakhya Temple VIP darshan', 5),
        ],
        days=[
            _day(1, 'GUWAHATI TO BHALUKPONG — GATEWAY TO THE EASTERN HIMALAYAS & FOOTHILL SERENADE', ('Upon your arrival at Guwahati Airport, a TRAGUIN luxury private representative welcomes you warmly. Board your premium vehicle and begin a picturesque transit toward Bhalukpong, the scenic threshold of Arunachal Pradesh situated alongside the Kameng River. As the plains give way to dense subtropical forests, feel the refreshing alpine air take over. Check into your boutique eco-lodge and unwind into the calm rhythms of nature.'), [
                'Sightseeing Included: Scenic drive through Assamese tea estates, Kameng riverbank sunset view.',
                'Evening Experience: Private bonfire setup with local tribal storytelling elements.',
                'Meals Included: Dinner.',
                'Overnight Stay: Premium Eco-Resort, Bhalukpong.',
            ]),
            _day(2, 'BHALUKPONG TO DIRANG — WHISPERING VALLEYS OF WEST KAMENG & KIWI ORCHARDS', ('An exquisite morning drive takes you deeper into the mountains toward Dirang, an enchanting valley blessed with unique microclimates. The route winds past cascading mountain waterfalls and steep gorges. Visit the beautiful orchid research center at Tipi, housing hundreds of exotic species. Upon entering Dirang, explore the historic Monpa village and witness the architectural marvel of the centuries-old Dirang Dzong overlooking the river.'), [
                'Sightseeing Included: Tipi Orchidarium, Dirang Dzong (Fort), Local Kiwi & Apple Orchards, Dirang River Hot Springs.',
                'Photography Points: Panoramic views of Dirang Valley from the suspension bridge.',
                'Meals Included: Breakfast & Dinner.',
                'Overnight Stay: Handpicked Luxury Boutique Hotel, Dirang.',
            ]),
            _day(3, 'DIRANG TO TAWANG VIA SELA PASS — ASCENDING THE MYSTIC HIGH-ALTITUDE GATEWAY OF SELA', ('Prepare for an epic, awe-inspiring driving day as your TRAGUIN expert pilot navigates the ascent to the magnificent Sela Pass, standing tall at an altitude of 13,700 feet. Witness the breathtaking frozen or azure Sela Lake, a revered site wrapped in local myth. After pausing for an emotional storytelling encounter at the Jaswant Garh War Memorial, descend into the pristine Tawang Valley, catching glimpses of towering waterfalls along the way.'), [
                'Sightseeing Included: Sela Pass, Sela Lake, Jaswant Garh War Memorial, Nuranang (Jung) Waterfalls.',
                'Optional Activities: High-altitude hot tea tasting at the military outpost café.',
                'Meals Included: Breakfast & Dinner.',
                'Overnight Stay: Premium Luxury Stay, Tawang.',
            ]),
            _day(4, 'TAWANG LOCAL SIGHTSEEING — THE SPIRITUAL SOUL OF MONPA HERITAGE & GREAT MONASTERIES', ('Dedicate your morning to the crown jewel of Arunachal Pradesh Sightseeing—the spectacular Tawang Monastery. Founded in the 17th century, it is the second-largest monastery in the world. Walk through its colorful assembly halls and interact with the resident monks. Later, visit the serene Urgelling Monastery, the birthplace of the 6th Dalai Lama, and complete your emotional cultural immersion at the Tawang War Memorial with its moving evening light show.'), [
                'Sightseeing Included: Tawang Monastery, Urgelling Monastery, Ani Gompa, Tawang War Memorial and museum.',
                'Evening Experience: Interactive Light and Sound Show at the War Memorial.',
                'Meals Included: Breakfast & Dinner.',
                'Overnight Stay: Premium Luxury Stay, Tawang.',
            ]),
            _day(5, 'TAWANG EXCURSION (BUM LA PASS & MADHURI LAKE) — THE HIGH FRONTIER: GLACIAL TARNS & BORDER VISTAS', ('Embark on a thrilling high-altitude excursion via specialized local 4x4 vehicles to Bum La Pass, situated at 15,200 feet on the Indo-China border. Stand at the edge of the frontier and witness standard border meeting points. On your return, visit the stunningly ethereal Shonga-tser Lake, popularly known as Madhuri Lake, surrounded by stark dead trees standing out from its glacial blue waters.'), [
                'Sightseeing Included: Bum La Pass, Madhuri Lake, PTSO Lake, Nagula Lake.',
                'Photography Points: Reflections of snow-clad ridges in the high alpine lakes.',
                'Meals Included: Breakfast & Dinner.',
                'Overnight Stay: Premium Luxury Stay, Tawang.',
            ]),
            _day(6, 'TAWANG TO BOMDILA — TRANQUIL RIDGES AND MONASTIC PANORAMAS OF BOMDILA', ('Bid farewell to Tawang as you retrace your route across the majestic Sela Pass, descending into the beautiful ridge town of Bomdila. The town offers spectacular vantage points overlooking the twin peaks of Kangto and Gorichen. Spend the afternoon exploring the peaceful Bomdila Monastery (Gontse Gaden Rabgyel Lling) and the local ethnographic museum, uncovering more about the unique Monpa, Sherdukpen, and Miji tribes.'), [
                'Sightseeing Included: Bomdila Monastery, Bomdila Viewpoint, Local Craft Center & Emporium.',
                'Evening Experience: Leisurely walk through the old town bazaar sampling local butter tea.',
                'Meals Included: Breakfast & Dinner.',
                'Overnight Stay: Curated Premium Stay, Bomdila.',
            ]),
            _day(7, 'BOMDILA TO GUWAHATI — DESCENT TO THE PLAINS & BRAHMAPUTRA SUNSET CRUISE', ('Conclude your mountain journey with a smooth, comfortable descent back into the vibrant city of Guwahati. Check into your final luxury city hotel. As the sun begins to set, enjoy an exclusive private charter cruise along the mighty Brahmaputra River. Celebrate the final evening of your incredible journey with fine dining and curated live cultural music on board.'), [
                'Sightseeing Included: Scenic downhill highway drive, Brahmaputra River sunset views.',
                'Evening Experience: Premium Sundowner/Dinner Cruise on the Brahmaputra River.',
                'Meals Included: Breakfast & Dinner.',
                'Overnight Stay: 5-Star Luxury Hotel, Guwahati.',
            ]),
            _day(8, 'GUWAHATI DEPARTURE — BLESSINGS OF KAMAKHYA & FOND FAREWELLS', ('On your final morning, visit the historic Kamakhya Temple atop Nilachal Hills to seek blessings before departure. Relish a relaxed breakfast at your luxury hotel. Your dedicated TRAGUIN vehicle transfers you seamlessly back to Guwahati Airport, concluding your premium Himalayan adventure with unforgettable memories.'), [
                'Sightseeing Included: Kamakhya Temple VIP Darshan (Optional).',
                'Meals Included: Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Tipi Eco Lodge | Hotel Pemaling | Hotel Gakyi Khang Zhang | Mon-Palace Bomdila | Novotel / Kiranshree Grand', 'Bhalukpong (1N) / Dirang (1N) / Tawang (3N) / Bomdila (1N) / Guwahati (1N)', '07 Nights', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner', 4, 1, description='OPTION – DELUXE/PREMIUM: Tipi Eco Lodge (Bhalukpong, 1N) | Hotel Pemaling (Dirang, 1N) | Hotel Gakyi Khang Zhang (Tawang, 3N) | Mon-Palace Bomdila (Bomdila, 1N) | Novotel / Kiranshree Grand (Guwahati, 1N)'),
            _hotel('Prashaanti Cottages (Premium) | The Dirang Boutique Resort / Nomad | Dondrub Heritage Inn / Vivanta Tawang | Hotel Tsepal Yangjom (Luxury Suite) | Taj Vivanta / Radisson Blu (Executive)', 'Bhalukpong (1N) / Dirang (1N) / Tawang (3N) / Bomdila (1N) / Guwahati (1N)', '07 Nights', 'Luxury', 'Luxury Room / Suite', 'Breakfast & Dinner', 5, 2, description='OPTION – LUXURY/ULTRA LUXURY: Prashaanti Cottages Premium (Bhalukpong, 1N) | The Dirang Boutique Resort / Nomad (Dirang, 1N) | Dondrub Heritage Inn / Vivanta Tawang (Tawang, 3N) | Hotel Tsepal Yangjom Luxury Suite (Bomdila, 1N) | Taj Vivanta / Radisson Blu Executive (Guwahati, 1N)'),
        ],
        inclusions=[
            _inc_included('07 Nights handpicked premium/luxury hotel accommodation as selected.', 1),
            _inc_included('Modified American Plan (Daily breakfast and lavish multi-cuisine dinners).', 2),
            _inc_included('Private luxury SUV (Innova Crysta) dedicated for all transfers and sightseeing.', 3),
            _inc_included('Inner Line Permits (ILP) and Protected Area Permits paperwork managed entirely by TRAGUIN.', 4),
            _inc_included('Local 4x4 wheel vehicle for Bum La Pass and Madhuri Lake excursions.', 5),
            _inc_included('Exclusive Brahmaputra River luxury sundowner dinner cruise voucher.', 6),
            _inc_included('Welcome amenities, fresh local fruits, and package mineral water bottles in-vehicle.', 7),
            _inc_included('24/7 dedicated premium backend support from TRAGUIN lifestyle managers.', 8),
            _inc_excluded('Airfare or train tickets to and from Guwahati Airport / Station.', 9),
            _inc_excluded('Monument entry fees, monastery camera tokens, and local tour guide fees.', 10),
            _inc_excluded('Personal expenses such as laundry, phone calls, alcoholic beverages, and tips.', 11),
            _inc_excluded('Optional activity upgrades or extra meals not outlined in the itinerary.', 12),
            _inc_excluded('Travel insurance or medical evacuation costs in high altitudes.', 13),
            _inc_excluded('Any cost arising due to natural calamities, landslides, or road blockages.', 14),
        ],
    )
    return package, itinerary

def build_ar_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AR-010'
    tour_code = 'TRAGUIN-AR-010'
    title = 'Premium Arunachal Pradesh Tour Package — Ultimate Luxury Family Vacation'
    duration = '08 Nights / 09 Days'
    slug = 'ar-010-ultimate-luxury-family-arunachal'
    itin_slug = 'ar-010-ultimate-luxury-family-arunachal-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Arunachal Pradesh / India | Category: Family Luxury Holidays', 2),
            _ph('Destinations: Bhalukpong (1N) • Dirang (2N) • Tawang (3N) • Bomdila (1N) • Guwahati (1N)', 3),
            _ph('Ideal for: Families, Honeymooners, Luxury Travelers', 4),
            _ph('Best season: October to May (Spring / Autumn)', 5),
            _ph('Starting price: On Request (Premium Curated)', 6),
            _ph('Vehicle: Luxury Toyota Innova Crysta / SUV | Meal Plan: Daily Gourmet Breakfast & Multi-cuisine Dinner', 7),
            _ph('Route Plan: Guwahati ➔ Bhalukpong (1N) ➔ Dirang (2N) ➔ Tawang (3N) ➔ Bomdila (1N) ➔ Guwahati (1N) ➔ Departure', 8),
            _ph('TRAGUIN Curated Experience Note: Relaxed driving run-times, handpicked premium accommodations, seamless ILP arrangement, traditional high-tea setups, localized expert guides, and 24/7 concierge assistance.', 9),
            _ph('TRAGUIN Signature Experience: Uniquely curated traditional family picnic lunch along the crystal-clear streams of Sangti Valley.', 10),
            _ph('Curated by Experts: Perfectly managed driving times optimized for the comfort of elderly members and young children.', 11),
            _ph('Premium Handpicked Hotels: Continuous quality audits ensure properties offering the best heating, views, and hospitality.', 12),
            _ph('Shopping & Local Experiences: Handmade Tibetan woolen carpets, Monpa wood carvings, traditional masks, momos, thukpa, Sela Pass and Madhuri Lake Instagram spots.', 13),
            _ph('Important Notes: ILP documents 7 days prior; Bum La Pass subject to military permits; pack heavy woolens and thermals; mountain roads may experience delays.', 14),
        ],
        moods=['Family', 'Luxury', 'Adventure', 'Culture'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Curated)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Ultimate Luxury Family • Bhalukpong • Dirang • Tawang • Bomdila • Guwahati • 08 Nights / 09 Days',
        overview=(
            'Embark on an extraordinary journey into the Land of the Dawn-Lit Mountains with the ultimate Best Arunachal Pradesh Tour Package expertly crafted by TRAGUIN. Designed exclusively for discerning families looking for a Luxury Arunachal Pradesh Holiday, this masterfully structured itinerary promises an immersive escape into pristine high-altitude valleys, misty alpine meadows, ancient vibrant monasteries, and rich tribal heritage.\n\n'
            'TOUR OVERVIEW\nThis elite Arunachal Pradesh Family Tour covers the most pristine circuit of Western Arunachal Pradesh. Traveling via private luxury transport with experienced mountain drivers, your family will traverse mountain passes, witness spectacular cascading rivers, and immerse themselves in Monpa cultural hospitality.'
        ),
        seo_title='AR-010 | Ultimate Luxury Family Arunachal | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days Arunachal family package (AR-010 / TRAGUIN-AR-010): Bhalukpong, Dirang, Sangti Valley picnic, Sela Pass, Tawang, Bum La Pass, Bomdila, Brahmaputra cruise, Kamakhya Temple.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Guwahati arrival and Bhalukpong gateway with Kameng River Valley scenic drive', 1),
            _ih('Tipi Orchidarium and Dirang Valley orientation with hot water springs dip', 2),
            _ih('Dirang Dzong, Thupsung Dhargye Monastery, and TRAGUIN Sangti Valley family picnic', 3),
            _ih('Sela Pass, Sela Lake, Jaswant Garh Memorial, Nuranang Waterfalls, and Tawang Monastery', 4),
            _ih('Bum La Pass, Madhuri Lake, Brahmaputra dinner cruise, and Kamakhya Temple blessings', 5),
        ],
        days=[
            _day(1, 'GUWAHATI ARRIVAL TO BHALUKPONG (240 KM / 5-6 HRS) — GATEWAY TO THE DAWN-LIT WILDERNESS', ('Your magnificent Himalayan journey begins as you land at Guwahati Airport. Here, your professional TRAGUIN tour representative warmly welcomes you and introduces you to your private luxury chauffeur-driven SUV. Depart immediately for Bhalukpong, the scenic border town nestled on the banks of the rushing Kameng River, marking the official gateway to Arunachal Pradesh. The scenic route winds past lush, green Assamese tea gardens and rolling foothills. Upon arriving at your handpicked riverside resort in Bhalukpong, complete a seamless check-in. Spend your evening breathing in the crisp mountain air, listening to the soothing melodies of the river rapids, and relaxing amidst untamed nature.'), [
                'Sightseeing Included: Scenic drive along the Kameng River Valley, Border entry crossings.',
                'Evening Experience: Leisurely riverside nature walk, followed by a warm traditional welcome dinner.',
                'Meals Included: Dinner (Buffet / Fixed Menu).',
                'Overnight Stay: Premium Eco-Resort / Hotel, Bhalukpong.',
            ]),
            _day(2, 'BHALUKPONG TO DIRANG VALLEY (140 KM / 5-6 HRS) — ASCENDING INTO THE ORCHARD VALLEY', ('Awake to a stunning sunrise over the misty river. After a sumptuous breakfast, check out and drive towards the idyllic Dirang Valley, situated at an altitude of 4,900 feet. As your luxury vehicle climbs higher, the air turns cool and refreshing, revealing breathtaking landscapes of deep gorges and evergreen pine forests. En route, stop at the celebrated Tipi Orchid Research Centre, which features a magnificent glasshouse displaying hundreds of exotic, rare orchid species. Continue your drive, stopping at scenic viewpoints perfect for family photography. Arrive in Dirang by afternoon and check into your premium valley-facing resort.'), [
                'Sightseeing Included: Tipi Orchidarium, Kameng River Viewpoints, Dirang Valley orientation.',
                'Optional Activities: A short therapeutic dip in the natural local hot water springs rich in minerals.',
                'Meals Included: Breakfast & Dinner.',
                'Overnight Stay: Premium Boutique Property / Luxury Resort, Dirang.',
            ]),
            _day(3, 'DIRANG VALLEY SIGHTSEEING — IMMERSIVE MONPA CULTURE & ALPINE VIEWS', ('Dedicate today to exploring the cultural gems of Dirang with your dedicated guide. Visit the historic Dirang Dzong, a centuries-old Monpa tribal fortress perched strategically on a hilltop, boasting unique stone architecture and panoramic valley views. Next, explore the serene, newly built Thupsung Dhargye Monastery, a major center for Buddhist learning adorned with vibrant murals and intricate wood carvings. In the afternoon, enjoy an exclusive TRAGUIN curated experience: a curated family picnic lunch at the beautiful Sangti Valley, an alpine paradise surrounded by pine forests, pristine rivers, and fields of black-necked cranes (seasonal).'), [
                'Sightseeing Included: Dirang Dzong, Thupsung Dhargye Monastery, Sangti Valley, Kiwi Orchards.',
                'Evening Experience: Stroll through local kiwi and apple plantations; tea tasting at a valley-view café.',
                'Meals Included: Breakfast & Dinner.',
                'Overnight Stay: Premium Boutique Property / Luxury Resort, Dirang.',
            ]),
            _day(4, 'DIRANG TO TAWANG VIA SELA PASS (135 KM / 6 HRS) — CROSSING THE HIGH-ALTITUDE SELA PASS', ('Today promises one of the most thrilling and iconic highlights of your Arunachal Pradesh Sightseeing journey. Your vehicle ascends to the majestic Sela Pass, standing tall at an incredible altitude of 13,700 feet. Witness the breathtaking, snow-rimmed Sela Lake (Paradise Lake), which remains partially frozen during winter, reflecting the majestic surrounding peaks. Stop for hot tea and photographs against this dramatic Himalayan backdrop. Pay your respects at the legendary Jaswant Garh War Memorial, dedicated to the brave Indian soldier Jaswant Singh Rawat, MVC. Descend into Tawang, stopping to admire the thunderous Nuranang Waterfalls. Arrive in Tawang (10,000 feet) and check into your luxury valley resort.'), [
                'Sightseeing Included: Sela Pass, Sela Lake, Jaswant Garh War Memorial, Nuranang Waterfalls (Jung Falls).',
                'Photography Points: Sela Pass gateway signpost, frozen lakeside, majestic waterfalls base.',
                'Meals Included: Breakfast & Dinner.',
                'Overnight Stay: Luxury Valley-View Resort / Premium Stay, Tawang.',
            ]),
            _day(5, 'TAWANG MONASTERY & LOCAL SIGHTSEEING — THE SPIRITUAL SOUL OF TAWANG', ('Discover the spiritual and historical treasures of Tawang. Begin your morning at the grand Tawang Monastery (Galden Namgyal Lhatse), founded in the 17th century. It stands as the largest monastery in India and houses a magnificent 28-foot gilded statue of Lord Buddha. Explore its vast library of ancient scriptures and interact with the resident monks. Next, visit the Urgelling Monastery, the peaceful birthplace of the 6th Dalai Lama. Later, discover the inspiring Tawang War Memorial, which honors the martyrs of the 1962 Sino-Indian War. Spend your evening exploring the vibrant local markets for traditional souvenirs.'), [
                'Sightseeing Included: Tawang Monastery, Urgelling Monastery, Ani Gompa (Nuns), War Memorial.',
                'Evening Experience: Moving Light and Sound Show at the Tawang War Memorial.',
                'Meals Included: Breakfast & Dinner.',
                'Overnight Stay: Luxury Valley-View Resort / Premium Stay, Tawang.',
            ]),
            _day(6, 'EXCURSION TO MADHURI LAKE & BUM LA PASS — THE HIGH-HIMALAYAN FRONTIER EXCURSION', ('Board a specialized local high-clearance 4x4 vehicle for an adrenaline-fueled excursion towards the Indo-China border. Ascend to Bum La Pass at a staggering 15,200 feet, where Indian Army soldiers warmly welcome travelers and share insightful border histories. On your return journey, stop at the mesmerizing Shonga-tser Lake, famously known across India as Madhuri Lake. Formed by a massive earthquake in 1950, it features dramatic dead tree trunks standing right out of its crystal-clear water, surrounded by towering, snow-dusted mountains. Enjoy hot maggi and tea at the army-run lakeside cafeteria before returning to Tawang.'), [
                'Sightseeing Included: Bum La Pass border outpost, Shonga-tser (Madhuri) Lake, PTSO Lake.',
                'Important Note: Bum La Pass visiting is subject to military permits and weather clear-out.',
                'Meals Included: Breakfast & Dinner.',
                'Overnight Stay: Luxury Valley-View Resort / Premium Stay, Tawang.',
            ]),
            _day(7, 'TAWANG TO BOMDILA (180 KM / 6.5 HRS) — SCENIC DRIVE TO THE CLOUD-KISSED RIDGE', ('After breakfast, bidding adieu to Tawang, trace your path back across Sela Pass as you travel towards Bomdila, a beautiful ridge-top town located at 7,900 feet. The journey offers another chance to witness the majestic shifting Himalayan views under different lighting conditions. Bomdila is famed for its expansive apple orchards, misty walking paths, and rich Monpa, Miji, and Sherdukpen tribal cultural heritage. Arrive by late afternoon and check into your premium hotel. Spend the evening relaxing or visiting the central Bomdila Monastery to enjoy panoramic views of the town below as the lights begin to twinkle.'), [
                'Sightseeing Included: Bomdila Monastery (GRL Gompa), Bomdila Viewpoint, central market stroll.',
                'Evening Experience: Sunset watching from the monastery ridge, followed by local tea sampling.',
                'Meals Included: Breakfast & Dinner.',
                'Overnight Stay: Premium Selected Luxury Hotel, Bomdila.',
            ]),
            _day(8, 'BOMDILA TO GUWAHATI (270 KM / 7.5 HRS) — RETURN TO THE BRAHMAPUTRA VALLEY', ('After an early breakfast, begin your final mountain descent as you head back towards Guwahati. Watch the dense pine forests gradually give way to lush bamboo groves and expansive plains. Re-enter the plains of Assam and cross the mighty Brahmaputra River. Upon arrival in Guwahati, check into your luxury five-star hotel. In the evening, celebrate the conclusion of an incredible family vacation with an exclusive TRAGUIN signature experience: an elegant private dinner cruise on the Brahmaputra River, enjoying live folk music and classic Assamese hospitality.'), [
                'Sightseeing Included: Brahmaputra River crossing, Guwahati city orientation.',
                'Evening Experience: Private Luxury Sunset/Dinner Cruise on the Brahmaputra River.',
                'Meals Included: Breakfast & Dinner.',
                'Overnight Stay: Luxury 5-Star Hotel (Vivanta / Radisson Blu), Guwahati.',
            ]),
            _day(9, 'GUWAHATI DEPARTURE — BLESSINGS & FOND FAREWELLS', ('On your final morning, after an exquisite breakfast, visit the sacred Kamakhya Temple, located atop Nilachal Hill, to seek blessings for your family\'s prosperity and well-being. Return briefly to your hotel to check out. Your luxury SUV will transfer you smoothly to Guwahati International Airport for your flight back home. Your unmatched TRAGUIN Arunachal Pradesh Packages journey concludes here, leaving your family with breathtaking landscapes, deep cultural insights, and a treasury of unforgettable memories.'), [
                'Sightseeing Included: Kamakhya Temple VIP Darshan (optional), Airport transfer drop-off.',
                'Meals Included: Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Prashanti Lodge | Hotel Pemaling | Hotel DNA | Hotel Shipmu | Hotel Gateway', 'Bhalukpong (1N) / Dirang (2N) / Tawang (3N) / Bomdila (1N) / Guwahati (1N)', '08 Nights', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner', 4, 1, description='OPTION 01 – DELUXE: Prashanti Lodge (Bhalukpong, 1N) | Hotel Pemaling (Dirang, 2N) | Hotel DNA (Tawang, 3N) | Hotel Shipmu (Bomdila, 1N) | Hotel Gateway (Guwahati, 1N)'),
            _hotel('Hotel Mandal Ghang | Dirang Resort | Tawang Horizon | Tsepal Yangjom | Kiranshree Grand', 'Bhalukpong (1N) / Dirang (2N) / Tawang (3N) / Bomdila (1N) / Guwahati (1N)', '08 Nights', 'Premium', 'Premium Room', 'Breakfast & Dinner', 4, 2, description='OPTION 02 – PREMIUM: Hotel Mandal Ghang (Bhalukpong, 1N) | Dirang Resort (Dirang, 2N) | Tawang Horizon (Tawang, 3N) | Tsepal Yangjom (Bomdila, 1N) | Kiranshree Grand (Guwahati, 1N)'),
            _hotel('Tipi Eco Resort | The itsy bitsy cabin | Dondrub Homestay / Vivanta | Hotel Elysium | Radisson Blu Guwahati', 'Bhalukpong (1N) / Dirang (2N) / Tawang (3N) / Bomdila (1N) / Guwahati (1N)', '08 Nights', 'Luxury', 'Luxury Room', 'Breakfast & Dinner', 5, 3, description='OPTION 03 – LUXURY: Tipi Eco Resort (Bhalukpong, 1N) | The itsy bitsy cabin (Dirang, 2N) | Dondrub Homestay / Vivanta (Tawang, 3N) | Hotel Elysium (Bomdila, 1N) | Radisson Blu Guwahati (Guwahati, 1N)'),
            _hotel('Luxury Riverside Cottages | Premium Valley Glamping Suites | Nuranang Luxury Alpine Resort | High Ridge Heritage Suite | Vivanta Guwahati (Executive)', 'Bhalukpong (1N) / Dirang (2N) / Tawang (3N) / Bomdila (1N) / Guwahati (1N)', '08 Nights', 'Ultra Luxury', 'Executive Suite / Glamping Suite', 'Breakfast & Dinner', 5, 4, description='OPTION 04 – ULTRA LUXURY: Luxury Riverside Cottages (Bhalukpong, 1N) | Premium Valley Glamping Suites (Dirang, 2N) | Nuranang Luxury Alpine Resort (Tawang, 3N) | High Ridge Heritage Suite (Bomdila, 1N) | Vivanta Guwahati Executive (Guwahati, 1N)'),
        ],
        inclusions=[
            _inc_included('Accommodation: 08 Nights premium luxury stay in double/twin sharing configuration at handpicked top-rated hotels.', 1),
            _inc_included('Meals: Daily gourmet breakfasts and multi-cuisine dinners included at all resort properties.', 2),
            _inc_included('Transfers & Transport: All point-to-point transfers and sightseeing in a private, clean, air-conditioned Toyota Innova Crysta / SUV with an experienced mountain-track driver.', 3),
            _inc_included('Special Permits: Seamless processing of all Inner Line Permits (ILP) and regional Arunachal government border registration fees.', 4),
            _inc_included('Exclusive Experiences: Private Brahmaputra River Evening Cruise tickets with dinner, and TRAGUIN signature family picnic lunch at Sangti Valley.', 5),
            _inc_included('Assistance: Warm traditional Assamese welcome amenities upon arrival and local Monpa scarves given in Tawang.', 6),
            _inc_included('TRAGUIN Support: 24/7 dedicated travel consultant backend concierge tracking and support throughout your tour.', 7),
            _inc_included('Taxes: All applicable luxury hotel taxes, toll fares, state permits, and fuel allowances.', 8),
            _inc_excluded('Flights: Domestic or international airfares to and from Guwahati Airport.', 9),
            _inc_excluded('Entry Fees: Monument entry tickets, camera fees, local monastery donations, and tour guide tips.', 10),
            _inc_excluded('Bum La Pass Transport: Charges for local Tawang union 4x4 vehicles required for the Bum La Pass / Madhuri Lake excursion (approx. ₹5,500–₹6,500 per vehicle, payable directly).', 11),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, premium alcoholic beverages, mini-bar consumption, and insurance.', 12),
            _inc_excluded('Optional Activities: Adventure sports, river rafting costs, or any unmentioned dining requests.', 13),
        ],
    )
    return package, itinerary

ARUNACHAL_PRADESH_DOMESTIC_BUILDERS = [
    build_ar_001,
    build_ar_002,
    build_ar_003,
    build_ar_004,
    build_ar_005,
    build_ar_006,
    build_ar_007,
    build_ar_008,
    build_ar_009,
    build_ar_010,
]
