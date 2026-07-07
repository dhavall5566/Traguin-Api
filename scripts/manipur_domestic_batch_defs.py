"""Builder functions for MN-001 through MN-010 Manipur domestic packages."""

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

MANIPUR_SLUG = "manipur"


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


def build_mn_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MN-001'
    tour_code = 'TRG-MAN-FAM-001'
    title = 'Imphal Discovery & Floating Lake Luxury Family Vacation'
    duration = '04 Nights / 05 Days'
    slug = 'mn-001-imphal-discovery-floating-lake-luxury-family-vacation'
    itin_slug = 'mn-001-imphal-discovery-floating-lake-luxury-family-vacation-itinerary'
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
            _ph('Serial code MN-001 | TRAGUIN tour code TRG-MAN-FAM-001', 1),
            _ph('State / Country: Manipur / India | Category: Premium Family Tour', 2),
            _ph('Destinations: Imphal • Loktak Lake • Moirang • Andro • Sendra Island', 3),
            _ph('Ideal for: Families, Heritage Explorers, Nature Seekers', 4),
            _ph('Best season: October to April', 5),
            _ph('Starting price: On Request (Premium Bespoke)', 6),
            _ph('Vehicle / Meals: Private, Chauffeur-Driven Luxury SUV (Innova Crysta / Premium Equivalent)', 7),
            _ph('Route: Imphal Arrival • Kangla Fort Heritage Walk • Loktak Floating Lake Expedition • Andro Cultural Experience • Imphal Departure This elite holiday features a highly specialized...', 8),
            _ph('TRAGUIN Signature Experience: A completely private classical Raas Leela dance recital held at a', 9),
            _ph('Curated by TRAGUIN Experts: Hand-vetted culinary stops selecting restaurants with high', 10),
            _ph('Personalized Assistance: Dedicated destination managers monitoring your routes for smooth,', 11),
            _ph('Premium Handpicked Hotels: Elite properties offering state-of-the-art amenities and beautiful', 12)
        ],
        moods=['Family', 'Heritage', 'Nature'],
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
        tagline='Imphal Discovery & Floating Lake Luxury Family Vacation',
        overview="04 Nights / 05 Days Signature Itinerary Welcome to the jewel of Northeast India with the exclusive Best Manipur Tour Package meticulously curated by TRAGUIN. Immerse your loved ones in a tapestry of emerald valleys, ancient royal history, and breathtaking landscapes that define this mystical border state. Crafted seamlessly as a top-tier Manipur Family Tour and romantic Manipur Honeymoon Package, this itinerary elegantly marries smooth, premium comfort with rich heritage TRAGUIN Premium Family Expeditions exploration. From the floating islands of Loktak Lake to the storied pathways of Kangla Fort, discover a world of unforgettable memories on this high-end Luxury Manipur Holiday.\n\nTOUR OVERVIEW\nTravel Dates: Flexible / Custom FIT Group / FIT: Bespoke Family FIT (Fully Hosted) Vehicle: Private, Chauffeur-Driven Luxury SUV (Innova Crysta / Premium Equivalent) Meal Plan: Royal Modified American Plan (Breakfast & Curated Dinners at Elite Venues) Route: Imphal Arrival • Kangla Fort Heritage Walk • Loktak Floating Lake Expedition • Andro Cultural Experience • Imphal Departure This elite holiday features a highly specialized TRAGUIN curated experience note: every entry, boat ride, and cultural interaction is privately reserved. Your family will enjoy seamless execution, handpicked premium stays, and personal guidance from senior heritage naturalists, balancing refined relaxation with enriching discovery. DESTINATION SPOTLIGHT & PREMIUM EXPERIENCES\n\nWhy Visit Manipur? Known historically as the 'Switzerland of the East', Manipur boasts unparalleled\nscenic beauty, a rich classical dance heritage, and multi-layered tribal traditions. A tailored Premium Manipur Experience opens doors to unique geographical wonders found nowhere else on earth, making it the perfect peaceful oasis for upscale family vacations. Famous Attractions & Most Searched Experiences: This journey showcases the pinnacle of Manipur Sightseeing. Explore Loktak Lake, the largest freshwater lake in Northeast India, famous for its unique circular floating swamps called 'Phumdis'. Witness the world's only floating wildlife sanctuary—Keibul Lamjao National Park, home to the endangered Sangai (brow-antlered deer). Walk down history at the majestic Kangla Fort, the spiritual seat of the ancient Meitei rulers, and admire the classical architecture of the Shree Govindajee Temple. Best Honeymoon, Family, & Luxury Points: For families, staying at a premium lakeside villa on Sendra Island offers absolute tranquility. Couples can indulge in private sunset boat cruises across calm waters, while children are enchanted by the unique floating eco-systems and artisan interactive craft workshops. Popular Instagram Locations: Capture striking imagery amidst the circular Phumdis of Loktak Lake, the historic white bridges and moats of Kangla Fort, the vibrant Ima Keithel (Mother's Market), and the pristine terraced artisan pottery fields of Andro. Adventure, Shopping, & Culture Highlights: Enjoy localized wooden boating, step inside the world's oldest functional polo ground, buy fine authentic Moirang Phee fabrics hand-woven by local matriarchs, and witness a privately hosted classical Manipuri Raas Leela performance. TRAGUIN Premium Family Expeditions",
        seo_title='MN-001 | Imphal Discovery & Floating Lake Luxury Family Vacation | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Manipur package (MN-001 / TRG-MAN-FAM-001): Imphal • Loktak Lake • Moirang • Andro • Sendra Island with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN IMPHAL', 1),
            _ih('Day 02: IMPHAL HERITAGE TOUR', 2),
            _ih('Day 03: IMPHAL TO LOKTAK LAKE & SENDRA ISLAND', 3),
            _ih('Day 04: LOKTAK LAKE TO ANDRO HERITAGE VILLAGE • IMPHAL', 4),
            _ih('Day 05: IMPHAL DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: A completely private classical Raas Leela dance recital held at a', 6),
            _ih('Curated by TRAGUIN Experts: Hand-vetted culinary stops selecting restaurants with high', 7),
            _ih('Personalized Assistance: Dedicated destination managers monitoring your routes for smooth,', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN IMPHAL',
                (
                    'ROYAL WELCOMES & THE SACRED HEART OF MANIPUR Your luxury vacation starts gracefully as your flight descends over the lush green valleys of Imphal. A dedicated TRAGUIN corporate concierge will greet your family at the arrival terminal with traditional stole presentations and cool wellness drinks. Step into your private luxury SUV and transition effortlessly to your handpicked premium hotel. After a refreshing afternoon check-in, begin your exploration of the Top Tourist Places in Manipur with a visit to the magnificent Shree Govindajee Temple. Admire its twin golden domes reflecting the afternoon sun as the rhythmic sound of traditional temple drums fills the air. Follow this with a relaxing stroll through the immaculately landscaped Imphal War Cemetery, honoring the heroes of the fierce Battle of Imphal during WWII.'
                ),
                [
                    'Sightseeing Included: Shree Govindajee Temple, Imphal War Cemetery, Kangla Outer Moat.',
                    'Optional Activities: Photography session in traditional luxury royal Meitei costumes.',
                    'Evening Experience: Private multi-course dinner briefing by your local heritage director.',
                    'Overnight Stay: Classic Luxury Comforts, Imphal.',
                    'Meals Included: Curated Welcome Dinner.',
                ],
            ),
            _day(
                2,
                'IMPHAL HERITAGE TOUR',
                (
                    "THE CITADELS OF KINGS & THE MATRIARCHS OF IMA KEITHEL Savor a delightful gourmet breakfast featuring local and continental delicacies. Today is dedicated to unearthing the profound royal ancestry of Imphal. Your luxury vehicle brings you to the sacred Kangla Fort, the grand epicentre of Manipuri civilization. Explore this massive brick-and-stone fortress on a premium private golf cart, viewing the ancient coronation halls, deep protective moats, and the iconic white sacred shrines of Lord Pakhangba. In the afternoon, step into the legendary Ima Keithel (Mother's Market)—a spectacular 500-year- old commercial hub managed completely by over 5,000 married women. It stands proud as a globally unique monument to female empowerment. Walk down the vibrant lanes as your TRAGUIN host guides you to the finest stalls for luxury handicrafts, local organic spices, and delicate traditional gold-plated ornaments."
                ),
                [
                    'Sightseeing Included: Kangla Fort complex, Ima Keithel, Mapal Kangjeibhung (Historic Polo Ground).',
                    'Optional Activities: Live interaction and textile masterclass with a national award-winning master weaver.',
                    'Evening Experience: A private classical Manipuri Jagoi dance presentation at an elite cultural auditorium.',
                    'Overnight Stay: Classic Luxury Comforts, Imphal.',
                    'Meals Included: Premium Breakfast & Fine Traditional Dinner.',
                ],
            ),
            _day(
                3,
                'IMPHAL TO LOKTAK LAKE & SENDRA ISLAND',
                (
                    "CRUISING THE CELESTIAL FLOATING ISLANDS & DANCING DEER ECHOES Wake up early to a beautiful crisp morning and check out after breakfast. Your smooth TRAGUIN Manipur Packages journey moves south toward the phenomenal Loktak Lake. As you approach Moirang, watch the landscape morph into vast expanses of sparkling water dotted with floating green rings. Arrive at Sendra Island, a premium elevated peninsula offering an exceptional panoramic view of the entire lake. Check into your luxury lakeside cottage. Board an exclusive, privately chartered speed-boat to cruise past the famous floating Phumdis. Visit the Keibul Lamjao National Park—the world's only floating wildlife sanctuary. Walk softly over the spongy, floating organic biomass with senior forest rangers to witness the rare, elegant Sangai Deer jumping gracefully across their pristine wetland habitat."
                ),
                [
                    'Sightseeing Included: Loktak Lake Cruise, Sendra Hills Viewpoint, Keibul Lamjao Floating Park.',
                    'Optional Activities: Traditional dugout canoe steering experience with local fishermen.',
                    'Evening Experience: Private sunset high-tea on a premium floating deck with spectacular lake views.',
                    'Overnight Stay: Elite Lakeside Resort Villas, Sendra Island / Loktak.',
                    'Meals Included: Breakfast, Fresh Lake-View Lunch, and Curated Dinner.',
                ],
            ),
            _day(
                4,
                'LOKTAK LAKE TO ANDRO HERITAGE VILLAGE • IMPHAL',
                (
                    "ANCIENT TERRACOTTA ARTS & THE LIVING FIRE OF FOLKLORE After a peaceful lakeside breakfast with beautiful water views, return comfortably to Imphal via a scenic route leading to Andro Heritage Village. Nestled at the foothills of the Nongmaiching range, Andro is an ancient settlement that carefully preserves the old-world tribal lifestyle and indigenous religious beliefs of the region. Visit the open-air Andro Cultural Museum to see traditional thatch houses representing various clans. Witness the fascinating craft of coil pottery, executed exclusively by married women without using a potter's wheel. Pay respects at the sacred temple where a ritual fire has been kept burning continuously since the 4th century. Return to Imphal in the evening to settle into your luxury hotel."
                ),
                [
                    'Sightseeing Included: Andro Cultural Village, Ancient Pottery Center, Sacred Fire Shrine.',
                    'Optional Activities: Interactive pottery-making session for the family.',
                    'Evening Experience: Festive farewell family dinner showcasing gourmet global cuisines.',
                    'Overnight Stay: Classic Luxury Comforts, Imphal.',
                    'Meals Included: Breakfast, Traditional Lunch, Grand Farewell Dinner.',
                ],
            ),
            _day(
                5,
                'IMPHAL DEPARTURE',
                (
                    'CHERISHING THE JEWELS OF THE EAST & BON VOYAGE Enjoy a relaxed final breakfast at your hotel. Take some time to pack your lovely souvenirs, handwoven textiles, and premium black pottery items. Your dedicated TRAGUIN chauffeur will comfortably handle your luggage and drive you safely back to Imphal Airport. As you check in for your flight home, carry with you the peaceful whispers of Loktak Lake, the grand history of ancient kings, and the unforgettable luxury family memories made in this beautiful corner of Northeast India.'
                ),
                [
                    'Sightseeing Included: En-route city landscapes and handicraft emporiums.',
                    'Overnight Stay: Departure / Onward Journey.',
                    'Meals Included: Rich Continental Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Classic / Similar (Deluxe Room) | Sendra Park Resort (Standard Cottage)',
                'Imphal | Loktak',
                '3N Imphal|1N Loktak/Sendra',
                'Deluxe',
                'Deluxe Room',
                'CP (Breakfast Only)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Classic / Similar (Deluxe Room) | Sendra Park Resort (Standard Cottage) | CP (Breakfast Only)',
            ),
            _hotel(
                'The Classic Grande / Equivalent (Executive) | Sendra Park by Classic (Premium Villa)',
                'Imphal | Loktak',
                '3N Imphal|1N Loktak/Sendra',
                'Premium',
                'Deluxe Room',
                'MAP (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Classic Grande / Equivalent (Executive) | Sendra Park by Classic (Premium Villa) | MAP (Breakfast & Dinner)',
            ),
            _hotel(
                'The Classic Grande (Suite Category) | Sendra Resort Villas (Lake View Front)',
                'Imphal | Loktak',
                '3N Imphal|1N Loktak/Sendra',
                'Luxury',
                'Suite Category | Lake View Front',
                'All Inclusive Managed',
                4,
                3,
                description='OPTION 03 – LUXURY: The Classic Grande (Suite Category) | Sendra Resort Villas (Lake View Front) | All Inclusive Managed',
            ),
            _hotel(
                'Signature Royal Palace Suite Collections | VIP Custom Overwater Luxury Eco Domes',
                'Imphal | Loktak',
                '3N Imphal|1N Loktak/Sendra',
                'Ultra Luxury',
                'Royal Palace Suite | Overwater Eco Dome',
                'Bespoke Private Culinary Host',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Signature Royal Palace Suite Collections | VIP Custom Overwater Luxury Eco Domes | Bespoke Private Culinary Host',
            )
        ],
        inclusions=[
            _inc_included('Accommodation: Luxury double stays at our handpicked hotels.', 1),
            _inc_included('Meals: Daily premium breakfast and custom gourmet dinners.', 2),
            _inc_included('Transfers: Sanitized private luxury SUV at your disposal.', 3),
            _inc_included('Sightseeing: All private boat charters, entry fees, and permits.', 4),
            _inc_included('Assistance: 24/7 dedicated TRAGUIN support helpline.', 5),
            _inc_included('Welcome Amenities: Royal standard arrival gift box and organic fruit baskets.', 6),
            _inc_included('Complimentary Experiences: Private golf-cart ride at Kangla Fort.', 7),
            _inc_excluded('Flights: Flight tickets to and from Imphal Airport.', 8),
            _inc_excluded('Personal Expenses: Laundry, room service, telephone calls.', 9),
            _inc_excluded('Activities: Any additional water sports or optional rides.', 10),
            _inc_excluded('Insurance: Travel, medical, or baggage loss insurance cover.', 11),
        ],
    )
    return package, itinerary

def build_mn_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MN-002'
    tour_code = 'TRG-MAN-FAM-002'
    title = 'Loktak Lake Special & Cultural Heritage Family Tour'
    duration = '04 Nights / 05 Days'
    slug = 'mn-002-loktak-lake-special-cultural-heritage-family-tour'
    itin_slug = 'mn-002-loktak-lake-special-cultural-heritage-family-tour-itinerary'
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
            _ph('Serial code MN-002 | TRAGUIN tour code TRG-MAN-FAM-002', 1),
            _ph('State / Country: Manipur / India | Category: Family Luxury Vacation', 2),
            _ph('Destinations: Imphal • Loktak Lake • Moirang • Sendra Island • Keibul Lamjao', 3),
            _ph('Ideal for: Families, Couples, Nature & Cultural Explorers', 4),
            _ph('Best season: October to April (Pleasant Mountain Weather)', 5),
            _ph('Starting price: On Request (Premium Fully Escorted Tour)', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / MAPAI', 7),
            _ph('TRAGUIN Signature Experience: Private family boat ride with an elite forest ranger inside Keibul', 8),
            _ph('Curated by TRAGUIN Experts: Smooth travel paces designed for seniors and young children,', 9),
            _ph('Personalized Assistance: Dedicated destination guest relations managers assisting at hotels and', 10),
            _ph('Premium Handpicked Hotels: Regular quality checks ensure top-tier safety, luxury linens, and', 11),
            _ph('& TRAVEL POLICIES', 12),
            _ph('Hotel Policies: Standard check-in times are at 14:00 hours; early check-ins are subject to room', 13)
        ],
        moods=['Family', 'Nature', 'Culture'],
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
        tagline='Loktak Lake Special & Cultural Heritage Family Tour',
        overview="04 Nights / 05 Days Premium Handcrafted Proposal Welcome to the jewel of Northeast India with the signature Best Manipur Tour Package meticulously curated by TRAGUIN. Immerse your loved ones in a sanctuary of breathtaking landscapes, floating islands, and timeless heritage. This exclusive Manipur Family Tour and Manipur Honeymoon Package invites you to rediscover the emotional bonds of family against the backdrop of the ethereal Loktak Lake—the only floating lake on earth. Experience a harmonious blend of pristine scenic beauty, rare wildlife, and deeply moving historical TRAGUIN Premium Luxury Expeditions storytelling wrapped in a Premium Manipur Experience. Let our travel experts host you on an incomparable Luxury Manipur Holiday designed for memories that linger far beyond the destination itself.\n\nTOUR OVERVIEW\nThis elite itinerary takes your family on an unforgettable, private route through Manipur's most iconic attractions. Spanning 4 nights and 5 days, your trip operates as a fully customized, private FIT tour. Your transportation is a dedicated, top-tier luxury SUV handled by a professional chauffeur- guide. Enjoy a comprehensive premium meal plan featuring both exquisite global multi-cuisine options and clean, curated traditional local delicacies. Every step of this voyage features a TRAGUIN curated experience note, promising handpicked premium stays, VIP access to cultural locations, unique private boating excursions, and flawless personalized assistance from our local concierges. DESTINATION SPOTLIGHT & IMMERSIVE EXPERIENCES\n\nWhy Visit Manipur? Known historically as the 'Jewel of India', Manipur remains a pristine jewel for\ndiscerning families seeking rich heritage, peaceful landscapes, and unique ecological wonders away from commercial crowds. Engaging in Manipur Sightseeing unlocks a peaceful sanctuary of rolling green mountains, historic royal temples, and warm tribal hospitality. Famous Attractions & Most Searched Experiences: This comprehensive travel plan centers around world-famous landmarks, including the magnificent Loktak Lake, the floating Keibul Lamjao National Park (home to the endangered Sangai Dancing Deer), the moving INA Memorial Complex at Moirang, and the legendary Ima Keithel—the world's largest and only market entirely run and managed by women. Best Family & Luxury Points: For multi-generational families, this package features curated experiences like traditional dance presentations, slow-paced private motorboat rides through floating phumdis (heterogeneous masses of vegetation), and staying at premium lakefront cottages that capture dramatic sunrises right outside your glass window. Popular Instagram Locations: Capture striking visual memories at the high-angle Sendra Island viewpoint overlooking the maze-like circular fishing rings of Loktak Lake, the golden Kangla Fort moats, and the colorful, bustling aisles of the ancient Mother's Market. Adventure, Shopping, & Culture Highlights: Walk over floating swamp grass islands, shop for world-class Moirang Phee handloom sarees and premium black pottery, and delve deep into ancient martial arts demonstrations and graceful classical Manipuri Ras Leela storytelling. TRAGUIN Premium Luxury Expeditions",
        seo_title='MN-002 | Loktak Lake Special & Cultural Heritage Family Tour | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Manipur package (MN-002 / TRG-MAN-FAM-002): Imphal • Loktak Lake • Moirang • Sendra Island • Keibul Lamjao with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN IMPHAL & KANGLA PALACE CHRONICLES', 1),
            _ih('Day 02: IMPHAL TO LOKTAK LAKE & SENDRA ISLAND', 2),
            _ih('Day 03: KEIBUL LAMJAO NATIONAL PARK & HISTORIC MOIRANG', 3),
            _ih("Day 04: LOKTAK TO IMPHAL & THE MATRIARCHS' MARKET", 4),
            _ih('Day 05: WAR MEMORIAL VISIT & IMPHAL DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private family boat ride with an elite forest ranger inside Keibul', 6),
            _ih('Curated by TRAGUIN Experts: Smooth travel paces designed for seniors and young children,', 7),
            _ih('Personalized Assistance: Dedicated destination guest relations managers assisting at hotels and', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN IMPHAL & KANGLA PALACE CHRONICLES',
                (
                    'ROYAL WELCOMES, ANCIENT FORTRESSES & SERENE SUNSETS Your luxury vacation starts as you land at Imphal International Airport. A senior TRAGUIN private travel consultant will receive you with a warm traditional Meitei silk stole welcome and refreshing chilled local fruit infusions. Step into your private luxury SUV and smoothly transfer to your premium hotel for an effortless check-in. In the afternoon, discover the ancient heart of the kingdom at the vast Kangla Fort complex, situated right on the banks of the Imphal River. Walk amongst ancient brick citadels, sacred coronation sites, and the majestic twin white Kangla Sha statues. Your private historian will share gripping stories of royal dynasties and colonial bravery. End the day with a serene evening walk around the peaceful, lotus-filled palace moats as the sun sets over the distant valley walls.'
                ),
                [
                    'Sightseeing Included: Kangla Fort Complex, Kangla Museum, Govindajee Temple.',
                    'Optional Activities: Traditional polo grounds visit (Manipur is the birthplace of modern polo).',
                    'Evening Experience: Private Aarti viewing at the pristine, golden-domed Shri Govindajee Temple.',
                    'Overnight Stay: Handpicked Premium Luxury Luxury Stay in Central Imphal.',
                    'Meals Included: Curated Welcome Lunch & Elegant Hotel Fine Dining.',
                ],
            ),
            _day(
                2,
                'IMPHAL TO LOKTAK LAKE & SENDRA ISLAND',
                (
                    "JOURNEY TO THE FLOATING MIRROR OF MANIPUR & HILLTOP VISTAS Savor a delightful, relaxed breakfast at your hotel before taking a scenic drive through emerald paddy fields toward Loktak Lake, an iconic highlight of our TRAGUIN Manipur Packages. As you approach Moirang, the vast, shimmering freshwater lake unfolds like a giant mirror reflecting the cloud-kissed skies. Arrive at the exclusive Sendra Island Resort, perched elegantly on a hilltop peninsula directly extending into the lake. Check into your premium lakeview cottage. In the afternoon, board an exclusive private traditional wooden longboat. Meander silently through the fascinating circular 'Phumdis'—the floating matrix of organic soil and vegetation unique to this ecosystem. Meet local lake fishermen and experience their unique lifestyle on these floating islands, an emotional storytelling moment that will fascinate children and elders alike."
                ),
                [
                    'Sightseeing Included: Loktak Lake Cruise, Sendra Island Viewpoint, Floating Fishing Villages.',
                    'Optional Activities: Private photography session at sunset in a traditional Manipuri dugout canoe.',
                    'Evening Experience: Gourmet high-tea served on a private panoramic terrace overlooking the vast lake expanse.',
                    'Overnight Stay: Premium Hilltop Lakeview Cottage, Sendra.',
                    'Meals Included: Breakfast, Fresh Lakefront Lunch, Organic Traditional Dinner.',
                ],
            ),
            _day(
                3,
                'KEIBUL LAMJAO NATIONAL PARK & HISTORIC MOIRANG',
                (
                    "THE DANCING DEER OF THE WORLD'S ONLY FLOATING NATIONAL PARK Wake up to a crisp morning over the lake. Today features an early morning excursion to the nearby Keibul Lamjao National Park—the world’s only floating wildlife sanctuary. Accompanied by a senior forest naturalist, embark on a quiet safari to spot the elusive, critically endangered Sangai Deer (the dancing brow-antlered deer), which balances beautifully on the spongy, floating phumdi grass. This is an educational and thrilling highlight for a Manipur Family Tour. Later, drive into the historic town of Moirang. Visit the Indian National Army (INA) Memorial Complex. Stand proudly where Netaji Subhas Chandra Bose’s INA hoisted the first Indian National Tri-color flag on mainland soil in 1944. Explore the museum filled with rare historical photographs, wartime letters, and battlefield relics."
                ),
                [
                    'Sightseeing Included: Keibul Lamjao Floating Safari, INA Memorial & War Museum, Moirang Bazaar.',
                    'Optional Activities: Short gentle trek to a nearby forest watchtower for a wide landscape view.',
                    'Evening Experience: Private family bonfire with acoustic music at the lakeside under clear starry skies.',
                    'Overnight Stay: Premium Hilltop Lakeview Cottage, Sendra.',
                    'Meals Included: Early Morning Coffee & Breakfast, Regional Manipuri Lunch, Continental Barbecue Dinner.',
                ],
            ),
            _day(
                4,
                "LOKTAK TO IMPHAL & THE MATRIARCHS' MARKET",
                (
                    "IMMERSIVE CULTURAL MASTERCLASSES & WORLD'S UNIQUE BAZAAR Enjoy a relaxed morning breakfast overlooking the water before your luxury SUV takes you back to Imphal. Your afternoon is dedicated to exploring the unmatched cultural fabric of the valley. Visit the world-famous Ima Keithel (Mother's Market), a 500-year-old commercial institution run exclusively by over 5,000 married women. Walk down vibrant aisles filled with colorful handwoven textiles, therapeutic brass items, and aromatic spices. Next, enjoy an private visit to the active craft enclave of Andro Heritage Village. See ancient pottery techniques preserved without a wheel, and view an expansive collection of traditional tribal dolls. This evening, celebrate your family's final night with an exclusive private"
                ),
                [
                    "Sightseeing Included: Ima Keithel (Mother's Market), Andro Cultural Village, Kangla Orchard.",
                    'Optional Activities: Silk weaving loom workshop tour with an award-winning master artisan.',
                    'Evening Experience: VIP seating at a private classical Ras Leela or Maibi ritual dance recital.',
                    'Overnight Stay: Elite Luxury Boutique Hotel, Imphal.',
                    'Meals Included: Breakfast, Authentic Farm-to-Table Lunch, Festive Farewell Dinner.',
                ],
            ),
            _day(
                5,
                'WAR MEMORIAL VISIT & IMPHAL DEPARTURE',
                (
                    'CHERISHING BEAUTIFUL FAMILY MOMENTS & SMOOTH DEPARTURES After a late, indulgent breakfast at the hotel, take a peaceful morning drive to the beautifully maintained Imphal WWII War Cemetery. Pay a respectful visit to the quiet, grass-covered grounds that honor Commonwealth soldiers who fought in the historic Battle of Imphal. It is a deeply reflective and educational stop for children. Return to the hotel to gather your belongings. Your premium TRAGUIN vehicle will provide a smooth transfer to Imphal International Airport for your flight home. As you board your flight, look back at the beautiful memories, magnificent landscapes, and unique floating wonders your family shared on this perfect, elite holiday.'
                ),
                [
                    'Sightseeing Included: Imphal War Cemetery, En-route souvenir craft centers.',
                    'Overnight Stay: Departure / Homeward Flight.',
                    'Meals Included: Rich Multi-cuisine Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Classic Hotel / Hotel Imphal (Deluxe) | Sendra Park & Resort (Standard Room)',
                'Imphal | Loktak',
                '2N Imphal|2N Loktak Lake',
                'Deluxe',
                'Deluxe Room',
                'MAP Plan (Breakfast + Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Classic Hotel / Hotel Imphal (Deluxe) | Sendra Park & Resort (Standard Room) | MAP Plan (Breakfast + Dinner)',
            ),
            _hotel(
                'The Classic Grande (Executive Room) | Classic Resort Sendra (Lakeview Room)',
                'Imphal | Loktak',
                '2N Imphal|2N Loktak Lake',
                'Premium',
                'Deluxe Room',
                'AP Plan (All Meals Included)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Classic Grande (Executive Room) | Classic Resort Sendra (Lakeview Room) | AP Plan (All Meals Included)',
            ),
            _hotel(
                'The Classic Grande (Suite Haven) | Sendra Hills Luxury Lakeview Cottage',
                'Imphal | Loktak',
                '2N Imphal|2N Loktak Lake',
                'Luxury',
                'Suite Haven | Lakeview Cottage',
                'Full Board Culinary Hosting',
                5,
                3,
                description='OPTION 03 – LUXURY: The Classic Grande (Suite Haven) | Sendra Hills Luxury Lakeview Cottage | Full Board Culinary Hosting',
            ),
            _hotel(
                'Imphal Heritage Palace / Elite VIP Villa | Sendra Presidential Waterfront Cottage',
                'Imphal | Loktak',
                '2N Imphal|2N Loktak Lake',
                'Ultra Luxury',
                'Elite VIP Villa | Presidential Waterfront',
                'Bespoke Royal Meitei Culinary Experiences',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Imphal Heritage Palace / Elite VIP Villa | Sendra Presidential Waterfront Cottage | Bespoke Royal Meitei Culinary Experiences',
            )
        ],
        inclusions=[
            _inc_included('Accommodation: Premium handpicked hotels and lakefront cottages.', 1),
            _inc_included('Meals: Daily premium breakfast, lunches, and themed dinners.', 2),
            _inc_included('Transfers: Dedicated Luxury SUV (Innova Crysta) throughout the tour.', 3),
            _inc_included('Sightseeing: All entry tickets, museum permits, and park fees.', 4),
            _inc_included('Assistance: 24/7 continuous TRAGUIN concierge support.', 5),
            _inc_included('Welcome Amenities: Specialized local Meitei silk welcome hampers.', 6),
            _inc_included('Complimentary Experiences: Private chartered boat cruise on Loktak Lake and exclusive private classical dance performance.', 7),
            _inc_excluded('Flights: Main airfares to and from Imphal Airport.', 8),
            _inc_excluded('Personal Expenses: Laundry, premium beverages, phone bills.', 9),
            _inc_excluded('Insurance: Travel, medical, or baggage loss insurance cover.', 10),
            _inc_excluded('Optional Tours: Extra activities not listed in the itinerary text.', 11),
            _inc_excluded('Camera Fees: Commercial video cameras or personal drone permits.', 12),
            _inc_excluded('Taxes: Any extra government luxury surcharges if applicable.', 13),
        ],
    )
    return package, itinerary

def build_mn_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MN-003'
    tour_code = 'TRG-MAN-EXPLORER-003'
    title = 'Manipur Explorer Luxury Expedition'
    duration = '05 Nights / 06 Days'
    slug = 'mn-003-manipur-explorer-luxury-expedition'
    itin_slug = 'mn-003-manipur-explorer-luxury-expedition-itinerary'
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
            _ph('Serial code MN-003 | TRAGUIN tour code TRG-MAN-EXPLORER-003', 1),
            _ph('State / Country: Manipur / India | Category: Luxury Adventure &', 2),
            _ph('Destinations: Imphal • Loktak Lake • Moirang • Khangkhui Caves • Ukhrul', 3),
            _ph('Ideal for: Luxury Explorers, Adventure Seekers, Culture & Nature Enthusiasts', 4),
            _ph('Best season: October to April (Pleasant Mountain Weather)', 5),
            _ph('Starting price: On Request (Premium Bespoke Package)', 6),
            _ph('Vehicle / Meals: Premium 4x4 SUV & Full Board (All Meals)', 7),
            _ph('TRAGUIN Signature Experience: Private classical Jagoi dance and live Thang-Ta martial arts', 8),
            _ph('Curated by TRAGUIN Experts: Custom cave exploration mapping with premium safety', 9),
            _ph('Personalized Assistance: Dedicated destination managers handling all permissions, inner-line', 10),
            _ph('Premium Handpicked Hotels: Stay in ultra-exclusive overwater cottages on Loktak Lake with', 11),
            _ph('Travel Permissions: Internal security validations and local reporting are fully managed in', 12)
        ],
        moods=['Adventure', 'Wildlife', 'Luxury'],
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
        tagline='Manipur Explorer Luxury Expedition',
        overview="MANIPUR EXPLORER LUXURY EXPEDITION 05 Nights / 06 Days Premium Crafted Itinerary Welcome to the jewel of Northeast India with the exclusive Best Manipur Tour Package designed flawlessly by TRAGUIN. Manipur is a spellbinding tapestry of emerald hills, ancient TRAGUIN Premium Luxury Expeditions tribal lore, and floating worlds that defy imagination. This bespoke holiday is crafted meticulously as a premium Manipur Honeymoon Package and an enriching Manipur Family Tour, perfect for elite travelers seeking high-octane thrills and unparalleled comforts. Prepare to surrender your senses to breathtaking landscapes, delve deep into limestone caverns, and stand amazed before the world’s only floating national park. Let the legendary hospitality of the land and the elite curation of a Luxury Manipur Holiday elevate your travel story into an unforgettable memory.\n\nTOUR OVERVIEW\nThis elite, hand-tailored exploration charts the absolute pinnacle of cultural heritage and active adventure in Manipur. Operating as a private, high-end FIT expedition, your journey encompasses smooth valley routes and rugged mountain ascents handled entirely by our professional drivers in premium luxury 4x4 SUVs. Your fully managed meal plan ranges from gourmet fine-dining continental menus to curated traditional Meitei and Tangkhul tribal feasts. Every moment of this itinerary features a signature TRAGUIN curated experience note: you will bypass public crowds with private motorboat access on Loktak Lake, explore deep cavern networks accompanied by expert speleologists, and settle each evening into handpicked luxury hotels and premium eco-lodges offering ultimate privacy and warmth. DESTINATION SPOTLIGHT & HIGH-SEARCH EXPERIENCES\n\nWhy Visit Manipur? Known historically as the 'Jewel of India', Manipur remains one of Asia's most\nenigmatic frontier destinations. It offers an unfiltered look into ancient kingdoms, rare endemic species, and dramatic topography, presenting a pristine playground for a Premium Manipur Experience. Famous Attractions & Most Searched Experiences: This comprehensive journey brings you face-to- face with legendary highlights during your Manipur Sightseeing. Experience the incredible floating islands (Phumdis) of Loktak Lake, the historic Kangla Fort, the inspiring INA Memorial at Moirang, the unique women-led Ima Keithel market, and the dramatic pine-laden heights of Ukhrul. Best Honeymoon, Family, & Luxury Points: For couples, a private sunset cruise inside Loktak Lake while staying in a premium overwater cottage offers unmatched romantic intimacy. For families, the educational experience of seeing the endangered Sangai brow-antlered deer leaping across floating marshes provides incredible bonding moments. Popular Instagram Locations: Capture striking visual content at the panoramic viewpoints over Loktak Lake, inside the dark limestone chambers of Khangkhui Caves, and amidst the lush green slopes of Shirui Kashong Peak. Adventure, Shopping, & Culture Highlights: Trek through steep ridges home to the rare Shirui Lily, explore subterranean prehistoric cave systems, shop for elite handwoven Moirang Phee silks, and TRAGUIN Premium Luxury Expeditions witness exclusive private showcases of classical Manipuri Jagoi dancing and traditional martial arts (Thang-Ta).",
        seo_title='MN-003 | Manipur Explorer Luxury Expedition | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Manipur package (MN-003 / TRG-MAN-EXPLORER-003): Imphal • Loktak Lake • Moirang • Khangkhui Caves • Ukhrul with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN IMPHAL', 1),
            _ih('Day 02: IMPHAL TO LOKTAK LAKE & MOIRANG', 2),
            _ih('Day 03: LOKTAK TO IMPHAL', 3),
            _ih('Day 04: IMPHAL TO UKHRUL', 4),
            _ih('Day 05: UKHRUL (SHIRUI PEAK & KHANGKHUI CAVES)', 5),
            _ih('Day 06: UKHRUL TO IMPHAL DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private classical Jagoi dance and live Thang-Ta martial arts', 7),
            _ih('Curated by TRAGUIN Experts: Custom cave exploration mapping with premium safety', 8),
            _ih('Personalized Assistance: Dedicated destination managers handling all permissions, inner-line', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN IMPHAL',
                (
                    "THE ROYAL GATEWAY & MYTHICAL BEGINNINGS Your extraordinary luxury adventure begins as your flight descends into Imphal Airport. As you step into the arrival terminal, a senior TRAGUIN luxury travel concierge awaits to receive you with a traditional silk stole welcome and chilled native fruit mocktails. Transition seamlessly into your waiting premium private 4x4 SUV and transfer to your luxury hotel. After checking in and enjoying a curated lunch, set out to explore the historic capital city. Your afternoon features exclusive entry into the ancient Kangla Fort, the seat of the medieval Ningthouja dynasty. Walk past historical royal moats and traditional sacred shrines as our expert historian uncovers tales of old empires. Conclude your afternoon at the unique Ima Keithel (Mother’s Market), the world’s largest and oldest commercial market run exclusively by over 5,000 married women, offering a spectacular glimpse into Manipur's vibrant social structure."
                ),
                [
                    'Sightseeing Included: Kangla Fort, Kangla Museum, Ima Keithel, Govindajee Temple.',
                    'Optional Activities: Private consultation with a master silk-weaver.',
                    'Evening Experience: Private orientation by your Expedition Lead paired with an authentic Meitei fine-dining dinner.',
                    'Overnight Stay: Classic Luxury Hotel in Imphal.',
                    'Meals Included: Welcome Lunch & Curated Dinner.',
                ],
            ),
            _day(
                2,
                'IMPHAL TO LOKTAK LAKE & MOIRANG',
                (
                    "THE FLOATING WORLD & THE SACRED SANGAI SANCTUARY Wake up to a crisp morning and enjoy a gourmet breakfast. Today, you embark on one of the most remarkable highlights of your TRAGUIN Manipur Packages—a scenic drive south to the ethereal Loktak Lake, the largest freshwater lake in Northeast India. Arriving at the lakeside, step aboard our private luxury motorboat and cruise through the vast expanse of water dotted with 'Phumdis'—unique circular formations of floating organic matter that look like emerald rings from above. Disembark directly at Keibul Lamjao National Park, the world’s only floating national park. Guided by an indigenous naturalist, look through high-end spotting scopes to witness the majestic Sangai (Brow-antlered Deer), affectionately called the dancing deer, leaping gracefully"
                ),
                [
                    'Sightseeing Included: Loktak Lake Cruise, Keibul Lamjao Floating Park, INA Memorial Museum, Sendra Hill',
                    'Optional Activities: Traditional dugout canoe ride managed by local fishermen.',
                    'Evening Experience: Breathtaking sunset champagne toast at our exclusive overwater lake viewpoint.',
                    'Overnight Stay: Premium Overwater Eco-Resort Cottages at Loktak.',
                    'Meals Included: Breakfast, Fresh Lakefront Lunch, Private Curated Dinner.',
                ],
            ),
            _day(
                3,
                'LOKTAK TO IMPHAL',
                (
                    'SERPENTINE ROADS, CASCADING WATERFALLS & CULTURAL SHOWCASES Savor a glorious overwater breakfast as the morning mist gently lifts from Loktak Lake. Check out and embark on an adventurous detour along the scenic foothill roads towards Khoupum valley extensions. This panoramic drive takes you through dramatic landscape formations, terraced hillsides, and pristine tribal hamlets. Stop at a secluded canyon viewpoint where a private gourmet picnic lunch has been set up exclusively for you by our trail team beside a cascading mountain waterfall. Return to Imphal by late afternoon. After refreshing at your luxury hotel, transfer to a private heritage amphitheater. Here, enjoy an exclusive private performance of the world-famous Manipuri Classical Dance (Jagoi) and the thrilling martial art of Thang-Ta (Spear and Sword play), celebrating the deep emotional spiritualism and physical agility of Manipuri culture.'
                ),
                [
                    'Sightseeing Included: Foothill Panoramic Passages, Local Waterfalls, Private Performance Venue.',
                    'Optional Activities: Interactive basic drumming session with classical exponents.',
                    'Evening Experience: Royal classical performance showcase followed by an elegant multi-course dinner.',
                    'Overnight Stay: Classic Luxury Hotel in Imphal.',
                    'Meals Included: Breakfast, Luxury Waterfall Picnic Lunch, Fine Dining Dinner.',
                ],
            ),
            _day(
                4,
                'Imphal to Ukhrul',
                (
                    'Enjoy an early breakfast before commencing an exhilarating journey into the high-altitude mountain country of Ukhrul, the home of the colorful Tangkhul Naga tribe. As your premium 4x4 SUV negotiates the twisting mountain roads, look out at the deep gorges and dense pine forests that define the region. The air cools rapidly as you ascend to over 1,600 meters, entering a serene landscape wrapped in perpetual mountain mist. Upon reaching Ukhrul, check into your premium luxury eco-lodge. In the afternoon, take a relaxed walking tour through a traditional Tangkhul village. Admire the distinctive architecture of tribal homes adorned with buffalo horns, symbolizing wealth and bravery. Engage with elder artisans who continue to craft traditional black pottery using techniques passed down through generations.'
                ),
                [
                    'Sightseeing Included: Mountain Pass Highways, Longpi Pottery Village, Ukhrul Tribal Market.',
                    'Optional Activities: Black clay pottery molding workshop with a national award artisan.',
                    'Evening Experience: Fireside tribal storytelling session with locally roasted wild coffee and organic snacks.',
                    'Overnight Stay: Premium Luxury Eco-Lodge in Ukhrul.',
                    'Meals Included: Breakfast, Mountain View Lunch, Curated Tribal Barbecue Dinner.',
                ],
            ),
            _day(
                5,
                'UKHRUL (SHIRUI PEAK & KHANGKHUI CAVES)',
                (
                    'SUBTERRANEAN MYSTERIES & THE HIGH PEAK LILY TREK Today brings a thrilling mix of subterranean exploration and mountain trekking. Following a hearty breakfast, your SUV takes you to the prehistoric Khangkhui Mangsor Caves. Equipped with premium safety helmets and high-powered headlamps, enter these ancient limestone caverns with an expert speleologist. Marvel at the grand stalactite and stalagmite formations as you explore deep chambers that served as natural air-raid shelters during World War II. In the afternoon, head to the base of the sacred Shirui Kashong Peak. Embark on a moderately challenging, professionally supported trek through beautiful rhododendron forests to the summit. This pristine mountain is the exclusive global home of the rare Shirui Lily (Lilium mackliniae). Stand atop the windy crest, surrounded by sweeping 360-degree views of the Myanmar border hills, and soak in the raw, majestic beauty of this unique destination. music.'
                ),
                [
                    'Sightseeing Included: Khangkhui Cave System, Shirui Kashong Peak, High-Altitude Viewpoints.',
                    'Optional Activities: High-altitude alpine meditation or professional landscape photography session.',
                    'Evening Experience: A grand celebratory farewell dinner featuring fine fusion cuisine and acoustic mountain',
                    'Overnight Stay: Premium Luxury Eco-Lodge in Ukhrul.',
                    'Meals Included: Breakfast, Trailhead Hot Lunch, Grand Farewell Dinner.',
                ],
            ),
            _day(
                6,
                'Ukhrul to Imphal Departure',
                (
                    'Savor your final mountain-view breakfast as the morning sun casts a golden glow over the pine forests of Ukhrul. Take a quiet moment to absorb the crisp mountain air before checking out. Your professional TRAGUIN chauffeur will carefully secure your luggage for the comfortable downhill drive back to Imphal. Reflect on the incredible floating worlds, deep caverns, mist-laden peaks, and warm smiles encountered on your journey. Arrive at Imphal Airport seamlessly timed with your departure flight, concluding your premium luxury exploration with a rejuvenated spirit and stories to last a lifetime.'
                ),
                [
                    'Sightseeing Included: En-route mountain valley lookouts, Imphal Airport Handover.',
                    'Overnight Stay: Departure / Homeward Journey.',
                    'Meals Included: Rich Continental Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Classic Hotel / Hotel Imphal | Sendra Park Resort (Standard) | Shalom Eco Lodge (Standard)',
                'Imphal | Loktak | Ukhrul',
                '2N Imphal|1N Loktak|2N Ukhrul',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast + Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Classic Hotel / Hotel Imphal | Sendra Park Resort (Standard) | Shalom Eco Lodge (Standard) | MAPAI (Breakfast + Dinner)',
            ),
            _hotel(
                'The Classic Grande (Executive) | Loktak Floating Cottages (Premium) | Shirui Eco Lodge (Premium Cabin)',
                'Imphal | Loktak | Ukhrul',
                '2N Imphal|1N Loktak|2N Ukhrul',
                'Premium',
                'Deluxe Room',
                'APAI (All Meals Included)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Classic Grande (Executive) | Loktak Floating Cottages (Premium) | Shirui Eco Lodge (Premium Cabin) | APAI (All Meals Included)',
            ),
            _hotel(
                'The Classic Grande (Suite Tier) | TRAGUIN Private Luxury Floating Villa | Ukhrul Heritage Retreat (Luxury Villa)',
                'Imphal | Loktak | Ukhrul',
                '2N Imphal|1N Loktak|2N Ukhrul',
                'Luxury',
                'Suite Tier | Luxury Villa',
                'All Inclusive Gourmet',
                5,
                3,
                description='OPTION 03 – LUXURY: The Classic Grande (Suite Tier) | TRAGUIN Private Luxury Floating Villa | Ukhrul Heritage Retreat (Luxury Villa) | All Inclusive Gourmet',
            ),
            _hotel(
                'Radisson Blu Imphal / Elite Signature Suite | TRAGUIN Bespoke VIP Overwater Geodesic Dome | The Cloud Estate (Bespoke Private Ch',
                'Imphal | Loktak | Ukhrul',
                '2N Imphal|1N Loktak|2N Ukhrul',
                'Ultra Luxury',
                'Elite Signature Suite | Private Chalet',
                'Royal Custom Dining',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Radisson Blu Imphal / Elite Signature Suite | TRAGUIN Bespoke VIP Overwater Geodesic Dome | The Cloud Estate (Bespoke Private Chalet) | Royal Custom Dining',
            )
        ],
        inclusions=[
            _inc_included('Accommodation: Premium handpicked luxury hotels and overwater chalets.', 1),
            _inc_included('Meals: All breakfasts, custom trail lunches, and curated gourmet dinners.', 2),
            _inc_included('Transfers: Private Luxury 4x4 SUV (Innova Crysta / Fortuner) throughout.', 3),
            _inc_included('Sightseeing: All park entries, special cave permits, and inner authorizations.', 4),
            _inc_included('Assistance: 24/7 dedicated TRAGUIN concierge support.', 5),
            _inc_included('Welcome Amenities: Premium welcome hampers and local organic amenities kit.', 6),
            _inc_included('Experiences: Private Loktak lake cruise and exclusive classical dance showcase.', 7),
            _inc_excluded('Flights: Domestic or International air tickets to/from Imphal.', 8),
            _inc_excluded('Personal Expenses: Laundry, telephone charges, premium hard beverages.', 9),
            _inc_excluded('Insurance: Comprehensive medical and travel disruption insurance.', 10),
            _inc_excluded('Optional Tours: Extra activities not listed in the core itinerary.', 11),
            _inc_excluded('Camera Fees: Professional cinematic drone or commercial video licenses.', 12),
            _inc_excluded('Tips: Gratuities for drivers, local cave specialists, and hotel bellboys.', 13),
        ],
    )
    return package, itinerary

def build_mn_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MN-004'
    tour_code = 'TRG-MAN-LUX-004'
    title = 'Bespoke Loktak Floating Paradise & Royal Tribal Heritage'
    duration = '05 Nights / 06 Days'
    slug = 'mn-004-bespoke-loktak-floating-paradise-royal-tribal-heritage'
    itin_slug = 'mn-004-bespoke-loktak-floating-paradise-royal-tribal-heritage-itinerary'
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
            _ph('Serial code MN-004 | TRAGUIN tour code TRG-MAN-LUX-004', 1),
            _ph('State / Country: Manipur / India | Category: Luxury Heritage &', 2),
            _ph('Destinations: Imphal • Loktak Lake • Moirang • Andro Cultural Outpost • Moreh Border', 3),
            _ph('Ideal for: Premium Couples, Luxury Honeymooners, Discerning Families', 4),
            _ph('Best season: October to April (Pleasant Mountain Climate)', 5),
            _ph('Starting price: On Request (Bespoke Fully Hosted Portfolio)', 6),
            _ph('Vehicle / Meals: Premium All-Terrain SUV & All Gourmet Meals', 7),
            _ph('TRAGUIN Signature Experience: Private, front-row seating at an intimate, classical Manipuri', 8),
            _ph('Curated by TRAGUIN Experts: Custom-tailored daily routes designed to avoid large tour groups,', 9),
            _ph('Personalized Assistance: Enjoy premium, air-conditioned luxury transportation with dedicated', 10),
            _ph('Premium Handpicked Hotels: Every property is chosen for its excellent service standards, rich', 11),
            _ph('Inner Line Permits: Domestic travelers require an Inner Line Permit (ILP), which will be', 12)
        ],
        moods=['Luxury', 'Heritage', 'Honeymoon'],
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
        tagline='Bespoke Loktak Floating Paradise & Royal Tribal Heritage',
        overview='Welcome to Northeast India\'s hidden jewel with the signature Best Manipur Tour Package curated exclusively by TRAGUIN. Known historically as the "Jeweled Land," Manipur unfolds as a sanctuary of sweeping valley basins, misty blue hill horizons, and an ancient royal heritage that remains utterly untouched by commercialism. This completely tailored Manipur TRAGUIN Premium Luxury Proposals Honeymoon Package and premium Manipur Family Tour has been designed meticulously for sophisticated travelers seeking both raw ecological wonders and seamless, high-end hospitality. From private speedboats exploring mysterious floating lake ecosystems to grand multi-course feasts in royal compounds, every day is balanced to weave unforgettable memories into your soul. Embark on a definitive Luxury Manipur Holiday and find yourself enchanted by the timeless magic of the Orient.\n\nTOUR OVERVIEW\nThis elite, hand-tailored exploration traces an expansive private route through the historic heartlands, ecological wonders, and vibrant borderlands of beautiful Manipur. Your expedition begins upon arrival at Imphal, transitioning seamlessly into the royal strongholds of the ancient Meitei Kings, expanding to custom over-water stays at Loktak Lake, and detailing a private hosted crossing down to the Indo-Myanmar border town of Moreh. Every parameter of this elite itinerary reflects a signature TRAGUIN curated experience note: you will enjoy private premium stays at handpicked hotels, relax inside customized luxury 4x4 SUVs with dedicated local travel concierges, and partake in private culinary and classical dance showcase experiences curated exclusively for our distinguished guests. DESTINATION SPOTLIGHT & PREMIUM EXPERIENCES\n\nWhy Visit Manipur? Tucked quietly away on India\'s easternmost frontier, Manipur offers an escape\ninto a land where rolling grasslands blend with unique floating biotopes and rich royal traditions. Choosing a Premium Manipur Experience allows high-end travelers to discover a deeply preserved culture of martial arts, sophisticated classical dances, and beautiful handicraft arts that cannot be found anywhere else in the world. Famous Attractions & Most Searched Experiences: The absolute peak of Manipur Sightseeing is the world-famous Loktak Lake, the only floating lake on earth, and the Keibul Lamjao National Park, a completely floating wildlife sanctuary that is home to the rare Sangai "Dancing Deer." Other iconic attractions include the historic brick redoubts of Kangla Fort, the ancient pottery center of Andro Cultural Village, and the sprawling international trade hubs of Moreh. Best Honeymoon, Family, & Luxury Points: For couples, watching a gold-tinted sunset from a private over-water cottage balcony over Loktak Lake is incredibly romantic and beautiful. Families will love the interactive history lessons, traditional sports demonstrations, and comfortable, private, chauffeured security that defines this curated travel format. Popular Instagram Locations: Capture striking, high-end photography at the majestic white dragon gateways of Kangla Fort, the bustling paths of the all-women-run Ima Keithel market, and the sweeping circular *phumdi* biomass rings on Loktak Lake. TRAGUIN Premium Luxury Proposals Adventure, Shopping, & Culture Highlights: Explore high-end textile craft shopping for rare Moirang Phee silks, enjoy fully hosted traditional Meitei multi-course meals served on gleaming bell- metal platters, and experience a private, intimate performance of the world-famous Manipuri Raas Leela classical dance.',
        seo_title='MN-004 | Bespoke Loktak Floating Paradise & Royal Tribal Heritage | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Manipur package (MN-004 / TRG-MAN-LUX-004): Imphal • Loktak Lake • Moirang • Andro Cultural Outpost • Moreh Border with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: IMPHAL ARRIVAL', 1),
            _ih('Day 02: IMPHAL TO LOKTAK LAKE & MOIRANG', 2),
            _ih('Day 03: KEIBUL LAMJAO FLOATING SAFARI TO ANDRO VILLAGE', 3),
            _ih('Day 04: EXCURSION TO MOREH (INDO-MYANMAR BORDER)', 4),
            _ih('Day 05: IMPHAL DOWNTOWN & THE IMA KEITHEL HISTORIC EXPERIENCE', 5),
            _ih('Day 06: IMPHAL DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private, front-row seating at an intimate, classical Manipuri', 7),
            _ih('Curated by TRAGUIN Experts: Custom-tailored daily routes designed to avoid large tour groups,', 8),
            _ih('Personalized Assistance: Enjoy premium, air-conditioned luxury transportation with dedicated', 9)
        ],
        days=[
            _day(
                1,
                'IMPHAL ARRIVAL',
                (
                    'THE ROYAL GATEWAY & ANCIENT SHRINES OF THE MEITEI KINGS Your ultimate luxury journey begins the moment you touch down at Bir Tikendrajit International Airport in Imphal. A senior travel coordinator from TRAGUIN will greet you warmly inside the arrival hall with a traditional royal shawl presentation and fresh seasonal mocktails. Step into your private, plush luxury SUV and transfer smoothly through the scenic tree-lined avenues of the capital to check into your handpicked luxury suite. After a relaxing lunch, begin your discovery of the finest Top Tourist Places in Manipur with a private guided walk through the expansive Kangla Fort, the ancient royal seat of power. Admire the reconstructed wood and brick fortresses, step inside the sacred temple of Lord Pakhangba, and view the imposing white stone Kangla Sha statues. Conclude your afternoon at the beautiful Shree Govindajee Temple, marveling at its twin gold-plated domes just as the evening prayer bells begin to chime.'
                ),
                [
                    'Sightseeing Included: Kangla Fort Palace Complex, Royal Moats, Shree Govindajee Temple, Sha Shrines.',
                    'Optional Activities: A private introductory meeting with a Meitei royal family heritage archivist.',
                    'Evening Experience: Private orientation by your travel concierge accompanied by gourmet local snacks.',
                    'Overnight Stay: Premium Luxury Suite, Imphal.',
                    'Meals Included: Welcome Lunch & Curated Fine Dining Dinner.',
                ],
            ),
            _day(
                2,
                'IMPHAL TO LOKTAK LAKE & MOIRANG',
                (
                    "CRUISING THE CELESTIAL FLOATING RINGS & PATRIOTIC FOOTSTEPS Indulge in a beautiful buffet breakfast before checking out for your scenic southern drive toward Moirang town. Today, your destination is the iconic Loktak Lake, a breathtaking landscape that forms the core of all TRAGUIN Manipur Packages. Upon arrival, step directly into a private, high-speed luxury motorboat arranged exclusively for you. Glide across the glass- like water to weave around the massive circular *phumdis*—floating mats of vegetation and soil that drift beautifully across the lake. TRAGUIN Premium Luxury Proposals Step onto a local floating fisherman's island to experience a warm cup of local tea and learn about their unique lifestyle on water. Later, return to the mainland at Moirang to explore the historic Indian National Army (INA) Memorial Complex. Stand inside the historic hall where the tricolor flag of free India was first raised on mainland soil by the forces of Netaji Subhash Chandra Bose. As the sun begins to set, check into your premium lakeside resort to enjoy panoramic water views."
                ),
                [
                    'Sightseeing Included: Private Speedboat Lake Cruise, Phumdi Floating Village, INA Memorial Museum.',
                    'Optional Activities: A traditional wooden canoe rowing experience alongside local lake guides.',
                    'Evening Experience: Private lakeside barbecue under the stars with traditional flute music.',
                    'Overnight Stay: Premium Luxury Over-Water / Lakeside Resort, Loktak.',
                    'Meals Included: Breakfast, Fresh Lakeside Lunch, and Private Grilled Dinner.',
                ],
            ),
            _day(
                3,
                'KEIBUL LAMJAO FLOATING SAFARI TO ANDRO VILLAGE',
                (
                    'THE DANCING DEER OF THE WILD & ANCIENT POTTERY FIRE SHRINES Wake up early to catch a pristine mountain sunrise as the morning mist gently rises off Loktak Lake. Board an early morning boat safari to enter the famous Keibul Lamjao National Park, the world\'s only floating wildlife park. Accompanied by a senior naturalist, use high- magnification spotting scopes to sight the rare and endangered Sangai Deer. Watch these beautiful animals move gracefully over the floating reeds, a sight that has made them famous as the "dancing deer" of the region. Return for a late breakfast, then enjoy a scenic country drive to the ancient heritage enclave of Andro Cultural Village. This beautifully preserved village functions as a living museum of tribal history. Walk through traditional thatched-roof houses and meet local women artisans who create beautiful black pottery using ancient coil techniques instead of a standard potter\'s wheel. Conclude your tour by viewing the ancient community fire shrine, which has been kept continuously burning by the villagers for hundreds of years.'
                ),
                [
                    'Sightseeing Included: Keibul Lamjao National Park, Andro Living Museum, Santhei Natural Park.',
                    'Optional Activities: A hands-on pottery molding masterclass with an award-winning village artisan.',
                    'Evening Experience: Private transfer back to Imphal for a gourmet dinner.',
                    'Overnight Stay: Premium Luxury Suite, Imphal.',
                    'Meals Included: Breakfast, Traditional Tribal Lunch, and Multi-Cuisine Dinner.',
                ],
            ),
            _day(
                4,
                'EXCURSION TO MOREH (INDO-MYANMAR BORDER)',
                (
                    "TRAGUIN Premium Luxury Proposals THE TRANS-ASIAN TRADE HIGHWAY & CROSSROADS OF SOUTHEAST ASIA Start your day early with a premium breakfast basket packed into your vehicle by our culinary team. Today, your private luxury SUV heads south along the Asian Highway down through the misty hills of Chandel to reach Moreh, India's strategic international border town trading directly with Myanmar. This route offers incredible views of steep mountain valleys and beautiful dense green forests. Your dedicated TRAGUIN logistics assistant will effortlessly manage all local border checkpoint formalities for you. Explore the vibrant international markets filled with unique Burmese teakwood carvings, rare gemstones, and beautiful imported silks. For lunch, step into a trusted local dining venue to enjoy an authentic, aromatic Burmese Khow Suey noodle meal. On your return drive, make a brief stop at the historic Khongjong War Memorial, located on the hills where the last Anglo-Manipur war was fought in 1891."
                ),
                [
                    'Sightseeing Included: Moreh International Border Post, Namphalong Asian Bazaar, Khongjong War Memorial Hill.',
                    'Optional Activities: A panoramic hilltop drive for a wide view over the rolling Kabaw Valley of Myanmar.',
                    'Evening Experience: Return to the capital for a relaxing evening and a light dinner at the hotel.',
                    'Overnight Stay: Premium Luxury Suite, Imphal.',
                    'Meals Included: Packed Luxury Breakfast, Burmese Fusion Lunch, and Elegant Suite Dinner.',
                ],
            ),
            _day(
                5,
                'IMPHAL DOWNTOWN & THE IMA KEITHEL HISTORIC EXPERIENCE',
                (
                    "THE SPRAWLING MATRIARCHAL HERITAGE MARKETS & SACRED CLASSICAL ARTS Savor a relaxed gourmet breakfast before spending your day exploring the rich culture of downtown Imphal. Your first highlight is a guided immersion into the world-famous Ima Keithel (The Mothers' Market). This incredible 500-year-old commercial center is entirely owned and managed by over 5,000 married women traders, making it the largest all-women market in Asia. Walk through rows of brightly colored hand-woven shawls, aromatic organic spices, and delicate brass ornaments. In the afternoon, pay a thoughtful visit to the serene Imphal War Cemetery, a beautifully maintained Commonwealth heritage site that honors the brave soldiers who turned the tide of World War II during the intense battles of 1944. As the evening approaches, prepare for your grand farewell event—a private, front-row viewing of the classical Manipuri Raas Leela dance, followed by a magnificent traditional Meitei feast served on elegant bell-metal platters. TRAGUIN Premium Luxury Proposals"
                ),
                [
                    "Sightseeing Included: Ima Keithel Mother's Market, Imphal WWII War Cemetery, State Craft Emporium.",
                    'Optional Activities: Private demonstration of Thang-Ta, the dramatic traditional martial art of Manipur.',
                    'Evening Experience: A spectacular traditional farewell dinner ceremony arranged by our team.',
                    'Overnight Stay: Premium Luxury Suite, Imphal.',
                    'Meals Included: Breakfast, Local Artisan Café Lunch, and Grand Farewell Dinner.',
                ],
            ),
            _day(
                6,
                'IMPHAL DEPARTURE',
                (
                    'CHERISHING THE MAGIC OF THE JEWELED LAND & DEPARTURE Enjoy your final morning breakfast looking out over the misty hills of the Imphal valley. Spend a few quiet moments picking up any last-minute souvenirs or packing your bags with the beautiful gifts gathered during your journey. Your professional chauffeur will ensure your luggage is carefully loaded into your premium vehicle before transferring you smoothly to Bir Tikendrajit International Airport for your departure flight. You board your plane with a deep sense of peace, new friendships, and unforgettable memories from your elite journey with TRAGUIN.'
                ),
                [
                    'Sightseeing Included: En-route scenic valley views and airport departure drop-off.',
                    'Overnight Stay: Departure / Onward Journey Home.',
                    'Meals Included: Full International Buffet Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Classic Hotel, Imphal (Executive Room) | Sendra Park Resort by Classic (Standard Villa)',
                'Imphal | Loktak',
                '4N Imphal|1N Loktak Lake',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: The Classic Hotel, Imphal (Executive Room) | Sendra Park Resort by Classic (Standard Villa) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Classic Grande, Imphal (Club Elite Room) | Sendra Park Heritage Resort (Deluxe Water-View)',
                'Imphal | Loktak',
                '4N Imphal|1N Loktak Lake',
                'Premium',
                'Deluxe Room',
                'APAI (All Daily Meals Included)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Classic Grande, Imphal (Club Elite Room) | Sendra Park Heritage Resort (Deluxe Water-View) | APAI (All Daily Meals Included)',
            ),
            _hotel(
                'Radisson Choice / Classic Grande (Luxury Suite) | Loktak Floating Luxury Over-Water Cottages',
                'Imphal | Loktak',
                '4N Imphal|1N Loktak Lake',
                'Luxury',
                'Luxury Suite | Over-Water Cottage',
                'TRAGUIN Private Culinary Plan',
                5,
                3,
                description='OPTION 03 – LUXURY: Radisson Choice / Classic Grande (Luxury Suite) | Loktak Floating Luxury Over-Water Cottages | TRAGUIN Private Culinary Plan',
            ),
            _hotel(
                'Royal Palace Suite Portfolio / Private Elite | TRAGUIN VIP Custom Floating Geodesic Eco-Dome',
                'Imphal | Loktak',
                '4N Imphal|1N Loktak Lake',
                'Ultra Luxury',
                'Royal Palace Suite | Geodesic Eco-Dome',
                'Bespoke Royal In-Dome Dining',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Royal Palace Suite Portfolio / Private Elite | TRAGUIN VIP Custom Floating Geodesic Eco-Dome | Bespoke Royal In-Dome Dining',
            )
        ],
        inclusions=[
            _inc_included('Accommodation: Premium suites and over- water floating cottages.', 1),
            _inc_included('Meals: Daily breakfasts, hosted artisan lunches, and fine farewell dinners.', 2),
            _inc_included('Transfers: Dedicated luxury 4x4 SUVs with an experienced mountain chauffeur.', 3),
            _inc_included('Sightseeing: All entry tickets, inner fort passes, and border crossing permits.', 4),
            _inc_included('Assistance: 24/7 real-time on-ground TRAGUIN support and local experts.', 5),
            _inc_included('Welcome Amenities: Exclusive arrival gift hampers featuring organic local products.', 6),
            _inc_included('Complimentary Experiences: Private high- speed speedboat rides on Loktak Lake.', 7),
            _inc_excluded('Flights: Commercial domestic or international airfares to/from Imphal.', 8),
            _inc_excluded('Personal Expenses: Laundry, premium hard drinks, and phone charges.', 9),
            _inc_excluded('Insurance: Comprehensive travel, baggage, and medical insurance coverage.', 10),
            _inc_excluded('Optional Tours: Any extra sightseeing detours not listed in the itinerary.', 11),
            _inc_excluded('Camera Fees: Professional drone or special filming gear permits.', 12),
            _inc_excluded('Tips: Voluntary gratuities for local drivers, guides, and hotel staff.', 13),
        ],
    )
    return package, itinerary

def build_mn_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MN-005'
    tour_code = 'TRG-MN-LEI-05'
    title = 'Senior Citizen Leisure — Imphal • Loktak Lake • Moirang • Khongjom'
    duration = '05 Nights / 06 Days'
    slug = 'mn-005-senior-citizen-leisure-imphal-loktak-khongjom'
    itin_slug = 'mn-005-senior-citizen-leisure-imphal-loktak-khongjom-itinerary'
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
            _ph('Serial code MN-005 | TRAGUIN tour code TRG-MN-LEI-05', 1),
            _ph('State / Country: Manipur / India | Category: Senior Citizen Leisure', 2),
            _ph('Destinations: Imphal • Loktak Lake • Moirang • Khongjom', 3),
            _ph('Ideal for: Seniors, Families & Leisure Travelers DESTINATIONS: Imphal, Loktak Lake, Moirang, Khongjom', 4),
            _ph('Best season: October to April HOTEL CATEGORY: Premium / Handpicked Luxury MEAL PLAN: MAPAI (Breakfast & Dinner) Welcome to the jewel of Northeast India. This bespoke luxury Manipur holiday is meticulously curated by TRAGUIN to offer a relaxed, deeply immersive, and thoroughly accessible experience of a land steeped in rich heritage, unmatched scenic beauty, and peaceful landscapes. Tailored specifically to the comfort of senior citizens, this holiday unfolds at a gentle, leisurely pace, blending spiritual calmness, cultural depth, and breathtaking natural vistas.', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / MAPAI', 7),
            _ph('TRAGUIN Signature Experience: Curated slower pace with late-morning starts to ensure proper rest.', 8),
            _ph('Curated by Experts: Itinerary designed by specialized consultants familiar with senior mobility', 9),
            _ph('Personalized Assistance: Pre-arranged wheelchair access at key monuments and airports upon request.', 10),
            _ph('Premium Handpicked Hotels: Strictly verified premium hotel properties featuring lift access and walk-in', 11),
            _ph("🛍️ Ima Keithel (Mother's Market): Buy exquisite hand-woven Moirang Phee sarees, traditional shawls, and stoles. 🛍️ Andro Village Craft Center: Purchase authentic, eco-friendly black terracotta pottery and organic kitchenware. 🛍️ Local Delicacies: Sample Singju (a light, healthy herb salad) or traditional black rice kheer (Chak-Hao Kheer). 📸 Instagram & Photo Spots: Capture the floating phumdis from Sendra hill, and the historical gates of Kangla Fort.", 12)
        ],
        moods=['Leisure', 'Family', 'Heritage'],
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
        tagline='Senior Citizen Leisure',
        overview="cenic, smooth road journey toward Moirang to witness the crown jewel of Northeast India's natural wonders—the legendary Loktak Lake. This full-day excursion is a highlight of your TRAGUIN Manipur Packages, offering breathtaking landscapes of shimmering water dotted with unique floating circular swamps known as Phumdis. Arriving at Sendra Hill Resort overlooking the lake, sit back and enjoy a spectacular, panoramic view of this vast ecosystem without any physical strain. A premium, safely boarded country boat ride will take you gently along the calm waters, allowing you to experience the world's only floating national park, Keibul Lamjao National Park. Keep your binoculars ready to catch a rare glimpse of the majestic Sangai—the brow-antlered dancing deer of Manipur. Later, visit the historic Moirang INA Memorial, where the Indian National Army under Netaji Subhash Chandra Bose first hoisted the tricolor on Indian soil in 1944. Return to Imphal via a beautiful scenic route as the evening shadows fall. Sightseeing Included: Loktak Lake, Sendra Viewpoint, INA Memorial Museum, Keibul Lamjao National Park. Optional Activities: Assisted gentle boat cruise on the calm waters of Loktak. Evening Experience: Panoramic sunset viewing over the floating islands. Overnight Stay: Imphal (Premium Handpicked Hotel). Meals Included: Breakfast & Dinner.\n\nTOUR OVERVIEW\nVehicle Description: Dedicated premium, air-conditioned luxury Innova / Crysta ensuring ultra-comfortable, spacious road Meal Specification: Modified American Plan (MAPAI) providing daily curated breakfasts and exquisite, wholesome transfers with experienced, polite, and senior- friendly chauffeurs. dinners prepared with tailored dietary preferences in handpicked hotels. TRAGUIN Curated Experience Note: Our signature TRAGUIN touch ensures priority boarding, easily accessible sightseeing routes with minimal walking stress, wheelchair assistance where requested, regular comfort stops, and personalized assistance throughout this unforgettable leisure Manipur journey. DESTINATION PROFILE & SEO INSIGHTS When considering the Best Manipur Tour Package, discerning travelers seek a harmonious balance of pristine eco-tourism, untouched historical legacies, and profound cultural immersion. Manipur, long celebrated as the Swiss Alps of the East, boasts some of the most iconic attractions in Northeast India. A premium Manipur Family Tour or a relaxed Luxury Manipur Holiday provides exclusive entry into a world of breathtaking landscapes, dominated by the legendary Loktak Lake—the largest freshwater lake in Northeast India, famous for its unique floating islands or 'phumdis'. Our meticulously planned Manipur Sightseeing tracks the top tourist places in Manipur, ensuring a deeply engaging yet physically effortless vacation. From the spiritual aura of the historic Shree Govindajee Temple to the moving legacy of the Imphal War Cemetery, each location is handpicked for its accessibility and profound historical importance. For those looking for the Best Time to Visit Manipur, the pleasant winter months offer crystal-clear azure skies and cool breezes, perfect for exploring popular Instagram locations, cultural hubs, and traditional markets like the world-renowned Ima Keithel (Mother's Market)—the largest all-women operated market in Asia. This Premium Manipur Experience connects you with authentic Manipuri heritage, peaceful nature, and world-class luxury care.",
        seo_title='MN-005 | Senior Citizen Leisure | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Manipur package (MN-005 / TRG-MN-LEI-05): Imphal • Loktak Lake • Moirang • Khongjom with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: IMPHAL ARRIVAL - WELCOME TO THE JEWEL OF THE EAST', 1),
            _ih('Day 02: IMPHAL CITY TOUR - SPIRITUAL SPLENDOR & HISTORIC LEGACIES', 2),
            _ih('Day 03: LOKTAK LAKE & MOIRANG - FLOATING PARADISES & ETERNAL LOVE', 3),
            _ih('Day 04: KHONGJOM EXCURSION - VALOUR ON THE HILLS & RURAL SERENITY', 4),
            _ih('Day 05: ANDRO CULTURAL VILLAGE - LIVING HERITAGE & ARTISTRY', 5),
            _ih('Day 06: IMPHAL DEPARTURE - CARRYING CHERISHED MEMORIES HOME', 6),
            _ih('TRAGUIN Signature Experience: Curated slower pace with late-morning starts to ensure proper rest.', 7),
            _ih('Curated by Experts: Itinerary designed by specialized consultants familiar with senior mobility', 8),
            _ih('Personalized Assistance: Pre-arranged wheelchair access at key monuments and airports upon request.', 9)
        ],
        days=[
            _day(
                1,
                'IMPHAL ARRIVAL - WELCOME TO THE JEWEL OF THE EAST',
                (
                    "Your ultimate Premium Manipur Experience begins the moment you touch down at Imphal International Airport. A warm, traditional Manipuri welcome awaits you, managed flawlessly by your dedicated TRAGUIN holiday representative. Step into your private luxury vehicle and transfer smoothly to your handpicked premium hotel in the heart of Imphal. After a relaxed check-in and an afternoon dedicated to unpacking and resting, enjoy a gentle evening visit to the magnificent Kangla Fort. Situated on the banks of the Imphal River, this historic citadel serves as the ancestral seat of Manipur's erstwhile rulers. The fort layout is senior-friendly, offering paved walkways surrounded by beautifully manicured lawns and sacred water moats. Capture stunning photographs as the setting sun glints off the ancient royal structures. Conclude your evening with an atmospheric drive past Imphal's prominent civic monuments before returning to your premium sanctuary for a specially prepared dinner."
                ),
                [
                    'Sightseeing Included: Kangla Fort, Royal Moats, and Kangla Museum.',
                    'Optional Activities: Leisure stroll around the inner palace lawns.',
                    'Evening Experience: Sunset photography at the historical fort ramparts.',
                    'Overnight Stay: Imphal (Premium Handpicked Hotel).',
                    'Meals Included: Welcome Dinner.',
                ],
            ),
            _day(
                2,
                'IMPHAL CITY TOUR - SPIRITUAL SPLENDOR & HISTORIC LEGACIES',
                (
                    "Awaken to a serene morning and savor a healthy, premium breakfast. Today's meticulously designed Manipur Sightseeing itinerary dives into the deep cultural and historical soul of the state. Your first stop is the sacred Shree Govindajee Temple, a historic golden-domed structure adjacent to the royal palace. Experience the soul-stirring morning prayers and witness the graceful devotion that characterizes Manipuri Vaishnavism. Next, proceed to the Imphal War Cemetery, a beautifully maintained Commonwealth site that pays poignant tribute to the brave British and Indian soldiers who defended the region during World War II. The flat, accessible layout allows for an easy, contemplative stroll along the floral-bordered commemorative plaques. In the afternoon, enjoy an exclusive visit to the Manipur State Museum, showcasing ancient royal relics, exquisite traditional costumes, and historical armor. End your day at the famous Ima Keithel Market, a vibrant symbol of women empowerment where over 5,000 local mothers run commerce. It is the ultimate spot for premium souvenir hunting and authentic interactions."
                ),
                [
                    'Sightseeing Included: Shree Govindajee Temple, Imphal War Cemetery, State Museum, Ima Keithel.',
                    'Optional Activities: Guided interactives with local weavers.',
                    'Evening Experience: Relaxed tea and traditional snacks tasting session at a premium local café.',
                    'Overnight Stay: Imphal (Premium Handpicked Hotel).',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                3,
                'LOKTAK LAKE & MOIRANG - FLOATING PARADISES & ETERNAL LOVE',
                (
                    "LEGENDS Following a hearty breakfast, embark on a scenic, smooth road journey toward Moirang to witness the crown jewel of Northeast India's natural wonders—the legendary Loktak Lake. This full-day excursion is a highlight of your TRAGUIN Manipur Packages, offering breathtaking landscapes of shimmering water dotted with unique floating circular swamps known as Phumdis. Arriving at Sendra Hill Resort overlooking the lake, sit back and enjoy a spectacular, panoramic view of this vast ecosystem without any physical strain. A premium, safely boarded country boat ride will take you gently along the calm waters, allowing you to experience the world's only floating national park, Keibul Lamjao National Park. Keep your binoculars ready to catch a rare glimpse of the majestic Sangai—the brow-antlered dancing deer of Manipur. Later, visit the historic Moirang INA Memorial, where the Indian National Army under Netaji Subhash Chandra Bose first hoisted the tricolor on Indian soil in 1944. Return to Imphal via a beautiful scenic route as the evening shadows fall."
                ),
                [
                    'Sightseeing Included: Loktak Lake, Sendra Viewpoint, INA Memorial Museum, Keibul Lamjao National Park.',
                    'Optional Activities: Assisted gentle boat cruise on the calm waters of Loktak.',
                    'Evening Experience: Panoramic sunset viewing over the floating islands.',
                    'Overnight Stay: Imphal (Premium Handpicked Hotel).',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                4,
                'KHONGJOM EXCURSION - VALOUR ON THE HILLS & RURAL SERENITY',
                (
                    "Dedicate your morning to an elegant breakfast before setting off on a peaceful south-bound drive to Khongjom, located roughly 36 kilometers from Imphal. This drive highlights the scenic beauty of Manipur's countryside, presenting endless vistas of rolling green hills, traditional villages, and golden paddy fields. Khongjom is a place of deep national pride, home to the Khongjom War Memorial Complex, built to honor the heroic Major General Paona Brajabashi and his soldiers who fought valiantly against the British Army during the Anglo-Manipur War of 1891. The site features a beautiful, easily accessible monumental park situated on the peaceful Kheba hills. Seniors can leisurely enjoy the manicured gardens, large reflecting pools, and striking commemorative pillars. This immersive experience offers deep insights into the region's proud royal history. Return comfortably to Imphal by afternoon for an extended period of personal leisure, relaxation, or optional luxury spa therapies."
                ),
                [
                    'Sightseeing Included: Khongjom War Memorial, Kheba Hill Gardens, Historical Footprint Exhibits.',
                    'Optional Activities: Traditional handloom weaving workshop visits.',
                    'Evening Experience: Relaxing classical Manipuri musical performance arrangement at the hotel.',
                    'Overnight Stay: Imphal (Premium Handpicked Hotel).',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                5,
                'ANDRO CULTURAL VILLAGE - LIVING HERITAGE & ARTISTRY',
                (
                    'Savor your breakfast before departing for a fascinating, leisurely day trip to the ancient village of Andro. Nestled at the foothills of the Nongmaiching range, Andro is an extraordinary living heritage museum meticulously chosen for our Luxury Manipur Holiday travelers. The village is renowned for preserving its centuries-old tribal customs, pottery styles, and traditional architecture. Explore the Mutua Ancient Cultural Museum, which houses a collection of traditional huts representing different ethnic clans of Manipur, alongside rare dolls, stone carvings, and ancient musical instruments. Witness a live demonstration of the unique coil-pottery technique performed exclusively by the village craftswomen without a pottery wheel. The layout of Andro is exceptionally serene, shaded, and flat, offering an intimate yet physically comfortable cultural encounter. Head back to Imphal for your final evening in the state, enjoying a premium farewell dinner curated exclusively by TRAGUIN.'
                ),
                [
                    'Sightseeing Included: Andro Living Museum, Cultural Heritage Huts, Ancient Pottery Center.',
                    'Optional Activities: Buying authentic terracotta souvenirs directly from local artisans.',
                    'Evening Experience: Grand Farewell Dinner celebrating authentic regional cuisines.',
                    'Overnight Stay: Imphal (Premium Handpicked Hotel).',
                    'Meals Included: Breakfast & Grand Farewell Dinner.',
                ],
            ),
            _day(
                6,
                'IMPHAL DEPARTURE - CARRYING CHERISHED MEMORIES HOME',
                (
                    'Greet your final morning in this beautiful destination with a relaxed, slow-paced breakfast at the luxury hotel. Take some time to secure your souvenirs, review your incredible photographs, and enjoy the premium amenities of your luxury accommodation. At the designated hour, complete your smooth checkout process. Your dedicated luxury private vehicle will transfer you comfortably to Imphal International Airport for your onward journey home. As you board your flight, you carry with you unforgettable memories, deep cultural insights, and newfound friendships, all perfectly arranged through the signature care and precision of your trusted travel companion, TRAGUIN.'
                ),
                [
                    'Sightseeing Included: Airport Transfer via scenic routes.',
                    'Meals Included: Complete Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Classic / Similar (Executive Room)',
                'Imphal',
                '5N Imphal',
                'Deluxe',
                'Executive Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Classic / Similar (Executive Room) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Classic Grande / Similar (Superior Room)',
                'Imphal',
                '5N Imphal',
                'Premium',
                'Superior Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Classic Grande / Similar (Superior Room) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Classic Grande - A Member of Radisson Individuals (Deluxe Club Room)',
                'Imphal',
                '5N Imphal',
                'Luxury',
                'Deluxe Club Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Classic Grande - A Member of Radisson Individuals (Deluxe Club Room) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Classic Grande - Premium Suite Experience (Executive Luxury Suite)',
                'Imphal',
                '5N Imphal',
                'Ultra Luxury',
                'Executive Luxury Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Classic Grande - Premium Suite Experience (Executive Luxury Suite) | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('05 Nights luxury accommodation in handpicked, senior-accessible hotels.', 1),
            _inc_included('Curated Meal Plan: 5 Breakfasts & 5 Dinners tailored to dietary requests.', 2),
            _inc_included('Private luxury AC Toyota Innova Crysta for all transfers & sightseeing.', 3),
            _inc_included('Dedicated, courteous, and highly experienced English/Hindi speaking driver.', 4),
            _inc_included('VIP assistance at Imphal Airport on arrival & departure.', 5),
            _inc_included('Safe, private boat cruise on Loktak Lake with dedicated safety vests.', 6),
            _inc_included('Complimentary mineral water bottles provided daily in the vehicle.', 7),
            _inc_included('All applicable state taxes, toll charges, fuel expenses, and driver allowances.', 8),
            _inc_included('24/7 dedicated TRAGUIN emergency guest support line.', 9),
            _inc_excluded('Domestic or International Airfare to/from Imphal.', 10),
            _inc_excluded('Monument entrance fees, camera permissions, or local guide services.', 11),
            _inc_excluded('Personal expenses (laundry, telephone calls, mini-bar, alcoholic drinks).', 12),
            _inc_excluded('Optional adventure activities or specialized porter services.', 13),
            _inc_excluded('Mandatory travel insurance or medical evacuation costs.', 14),
            _inc_excluded('Any expenses caused due to flight delays, bad weather, or political unrest.', 15),
            _inc_excluded('GST & TCS Government taxes (applied at invoice time).', 16),
        ],
    )
    return package, itinerary

def build_mn_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MN-006'
    tour_code = 'TRAGUIN-MAN-006'
    title = 'Imphal • Loktak Lake • Moirang • Andro • Moreh Border Family Holiday'
    duration = '06 Nights / 07 Days'
    slug = 'mn-006-imphal-loktak-moirang-andro-moreh-family-holiday'
    itin_slug = 'mn-006-imphal-loktak-moirang-andro-moreh-family-holiday-itinerary'
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
            _ph('Serial code MN-006 | TRAGUIN tour code TRAGUIN-MAN-006', 1),
            _ph('State / Country: Manipur / India | Category: Family Holiday', 2),
            _ph('Destinations: Imphal • Moirang • Loktak Lake • Andro • Moreh', 3),
            _ph('Ideal for: Families, Culture & Nature Lovers', 4),
            _ph('Best season: October to April', 5),
            _ph('Starting price: On Request (Premium Luxury)', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / MAPAI', 7),
            _ph('Route: Imphal Arrival → Loktak Lake & Moirang → Andro Cultural Village → Border Town of Moreh → Imphal Departure', 8),
            _ph('TRAGUIN Signature Experience: Private access to premium handloom workshops with expert', 9),
            _ph('Curated by TRAGUIN Experts: A relaxed, senior-friendly and child-friendly pace designed for multi-', 10),
            _ph("Personalized Assistance: Dedicated local concierge service ensures your family's preferences are met", 11),
            _ph('Luxury Transportation: Highly safe, well-screened professional drivers who know the local terrain', 12),
            _ph('Booking Policy: We recommend making your bookings well in advance for peak season travel (October –', 13),
            _ph('April) to secure the finest rooms.', 14)
        ],
        moods=['Family', 'Culture', 'Nature'],
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
        tagline='Imphal',
        overview='Imphal • Loktak Lake • Moirang • Andro • Moreh Border Welcome to a realm untouched by time. Manipur, the "Jewel of India," opens its arms to your family for an extraordinary escape into breathtaking landscapes, rich royal history, and deeply immersive experiences. This meticulously customized Manipur Family Tour is designed by TRAGUIN to balance absolute luxury with deep cultural discoveries, ensuring every member of your family from children to seniors shares unforgettable memories. From the floating islands of Loktak to the warm, welcoming traditions of the Meitei people, let TRAGUIN orchestrate a magical holiday that feels deeply personal and perfectly seamless.\n\nTOUR OVERVIEW\nThis exclusive **Luxury Manipur Holiday** provides a comprehensive exploration of the state\'s most iconic attractions. Your family will enjoy private, air-conditioned premium transportation, handpicked premium accommodations, and personalized guided tours that breathe life into local history. Travel Category: Private Family FIT (Fully Independent Tour) Vehicle Status: Premium Luxury Innova / Crysta for ultimate road comfort Meal Plan: Modified American Plan (Breakfast & Choice of Lunch or Dinner) The Route: Imphal Arrival → Loktak Lake & Moirang → Andro Cultural Village → Border Town of Moreh → Imphal Departure TRAGUIN Curated Experience: Private traditional dance presentation, handpicked local culinary tastings, and exclusive access to community weavers. DISCOVER THE MAGIC: PREMIUM MANIPUR EXPERIENCE When planning a family vacation, finding a destination that satisfies everyone can be challenging. A Manipur Family Tour offers the perfect blend of scenic beauty, intriguing historical narratives, and unique geographical marvels. Home to the world\'s only floating national park, Manipur stands out as an exceptional choice for discerning families looking for an authentic, premium travel experience away from overcrowded commercial hubs. The Best Time to Visit Manipur is between October and April when the weather is delightfully pleasant, allowing you to easily explore the Top Tourist Places in Manipur. Families can dive deep into the local culture by visiting the historical Kangla Fort, witnessing the graceful Sangai deer, shopping at the world- famous all-women Ima Keithel market, and admiring the popular Instagram locations across the pristine Loktak Lake. Whether it’s adventure, cross-border excitement at Moreh, or shopping for exquisite handloom silks, our TRAGUIN Manipur Packages guarantee absolute luxury and seamless execution. YOUR BESPOKE DAY-WISE ITINERARY',
        seo_title='MN-006 | Imphal | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Manipur package (MN-006 / TRAGUIN-MAN-006): Imphal • Moirang • Loktak Lake • Andro • Moreh with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: IMPHAL ARRIVAL – WELCOME TO THE JEWELED LAND', 1),
            _ih('Day 02: IMPHAL SIGHTSEEING – HISTORIC ICONS & ALL-WOMEN MARKET', 2),
            _ih('Day 03: LOKTAK LAKE & MOIRANG – THE FLOATING MARVEL', 3),
            _ih('Day 04: ANDRO CULTURAL VILLAGE – POTTERY & HERITAGE TRADITIONS', 4),
            _ih('Day 05: MOREH EXCURSION – CROSS-BORDER INDO-MYANMAR CULTURE', 5),
            _ih('Day 06: EXCLUSIVE LEISURE & HANDLOOM SHOPPING IN IMPHAL', 6),
            _ih('Day 07: DEPARTURE FROM IMPHAL – UNFORGETTABLE MEMORIES', 7),
            _ih('TRAGUIN Signature Experience: Private access to premium handloom workshops with expert', 8),
            _ih('Curated by TRAGUIN Experts: A relaxed, senior-friendly and child-friendly pace designed for multi-', 9),
            _ih("Personalized Assistance: Dedicated local concierge service ensures your family's preferences are met", 10)
        ],
        days=[
            _day(
                1,
                'IMPHAL ARRIVAL – WELCOME TO THE JEWELED LAND',
                (
                    'Step off your flight into the crisp air of Imphal, where your dedicated TRAGUIN professional representative awaits your family. Your premium luxury vehicle will comfortably transfer you to your handpicked premium hotel. After a smooth check-in and some time to unpack and relax, embark on a light introductory afternoon tour of Imphal city. Visit the serene Kangla Fort, the ancient seat of Manipur’s past rulers, located right on the banks of the Imphal River. Walk along its historical moats and sacred shrines as your guide shares tales of royal legacy. Conclude your evening with a relaxing walk around the local areas, capturing your first family photos against the gorgeous sunset over the valley.'
                ),
                [
                    'Sightseeing Included: Kangla Fort, Royal Moat, City Orientation',
                    'Evening Experience: Leisurely family walk & traditional welcome welcome mocktails',
                    'Overnight Stay: Handpicked Luxury Hotel in Imphal',
                    'Meals Included: Welcome Dinner',
                ],
            ),
            _day(
                2,
                'IMPHAL SIGHTSEEING – HISTORIC ICONS & ALL-WOMEN MARKET',
                (
                    "Enjoy a sumptuous breakfast before diving into a comprehensive Manipur Sightseeing experience. Today your family visits the emotional Imphal War Cemetery, a beautifully maintained site dedicated to the brave British and Indian soldiers of WWII. Next, experience the vibrant energy of the world-famous Ima Keithel (Mother's Market), a massive commercial hub managed entirely by thousands of local women—a wonderful display of women empowerment and local culture. In the afternoon, head to the Manipur State Museum to view royal artifacts, costumes, and weapons. Finish your day at the pristine Govindajee Temple, participating in a soothing evening prayer ceremony that offers a deep sense of peace."
                ),
                [
                    'Sightseeing Included: Ima Keithel, WWII War Cemetery, State Museum, Govindajee Temple',
                    'Optional Activities: Interaction with local textile experts arranged by TRAGUIN',
                    'Evening Experience: Attending the evening arti ceremony at Govindajee Temple',
                    'Overnight Stay: Handpicked Luxury Hotel in Imphal',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'LOKTAK LAKE & MOIRANG – THE FLOATING MARVEL',
                (
                    'Today promises an absolute highlight of your Luxury Manipur Holiday. Travel south to Moirang to witness the ethereal beauty of Loktak Lake, the largest freshwater lake in Northeast India. Look out over the phumdis —unique floating circles of organic mass that form a surreal pattern on the water. Board a private wooden boat curated by TRAGUIN for a gentle cruise. Your boat takes you to the Keibul Lamjao National Park, the world’s only floating national park and the last natural home of the endangered, elegant Sangai brow-antlered deer. Later, visit the INA Memorial Complex in Moirang, where the Indian National Army flag was first unfurled on mainland India during WWII.'
                ),
                [
                    'Sightseeing Included: Loktak Lake, Keibul Lamjao Floating Park, INA Memorial Complex',
                    'Optional Activities: Private boat ride with local fishermen to see traditional floating huts',
                    'Evening Experience: Sunset photography over the breathtaking landscapes of Loktak',
                    'Overnight Stay: Premium Lakefront Resort / Imphal Luxury Hotel',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'ANDRO CULTURAL VILLAGE – POTTERY & HERITAGE TRADITIONS',
                (
                    "After a leisurely breakfast, journey to the ancient village of Andro, nestled at the foothills of the region. This carefully designed cultural excursion offers an immersive experience into the ancestral crafts of Manipur. Witness the unique pottery traditions where artisans create beautiful vessels without using a pottery wheel. Explore the Andro Cultural Heritage Complex, which displays traditional model houses of various tribes, wood carvings, and a sacred fire that has been kept burning continuously for centuries. It's a wonderful educational experience for children and an eye-opening cultural journey for adults."
                ),
                [
                    'Sightseeing Included: Andro Tribal Heritage Complex, Ancient Fire Temple, Pottery Workshops',
                    'Optional Activities: Hands-on pottery making experience for the family',
                    'Evening Experience: Private Meitei traditional musical demonstration at the village',
                    'Overnight Stay: Handpicked Luxury Hotel in Imphal',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'MOREH EXCURSION – CROSS-BORDER INDO-MYANMAR CULTURE',
                (
                    'Set off early for a fascinating day trip to Moreh, the bustling international border town between India and Myanmar. The scenic route winds through beautiful hills and dense forests, offering panoramic views of the Indo-Myanmar border. Explore the lively border markets where a diverse mix of Indian and Burmese goods are traded. Subject to prevailing government regulations and permissions, step across the international border to visit Tamu town in Myanmar, exploring its beautiful multi-tiered Buddhist monasteries and experiencing a distinct change in culture, architecture, and language within just a few steps.'
                ),
                [
                    'Sightseeing Included: Moreh Border Market, Indo-Myanmar Friendship Gate, Tamu Town Monasteries',
                    'Optional Activities: Sampling authentic Burmese Khao Suey and local delicacies',
                    'Evening Experience: Relaxing scenic drive back to Imphal city',
                    'Overnight Stay: Handpicked Luxury Hotel in Imphal',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                6,
                'EXCLUSIVE LEISURE & HANDLOOM SHOPPING IN IMPHAL',
                (
                    'Dedicate this day to relaxation and collecting beautiful memories. Enjoy a late breakfast before setting out for an exclusive shopping tour tailored by TRAGUIN. Manipur is famous for its intricate handloom weaving. Visit a premium weaving cooperative to see how local families create stunning Phaneks (traditional skirts), Rani Phees, and elegant silk stoles. This afternoon is perfect for visiting popular Instagram locations around the city for final family photographs. In the evening, TRAGUIN hosts a special farewell family dinner featuring a curated multi-course menu of local and international delicacies to celebrate your wonderful journey together.'
                ),
                [
                    'Sightseeing Included: Handloom Weaving Center, Local Craft Emporiums, Leisure Highlights',
                    'Optional Activities: Pre-booked family portrait session in traditional Manipuri attire',
                    'Evening Experience: Premium Grand Farewell Dinner hosted by TRAGUIN',
                    'Overnight Stay: Handpicked Luxury Hotel in Imphal',
                    'Meals Included: Breakfast & Farewell Dinner',
                ],
            ),
            _day(
                7,
                'DEPARTURE FROM IMPHAL – UNFORGETTABLE MEMORIES',
                (
                    'Wake up to your final morning in this beautiful valley. Share a relaxed breakfast with your family and pack your wonderful souvenirs, handloom silks, and memorable photos. Your luxury private vehicle will pick you up from the hotel lobby and provide a comfortable transfer to Bir Tikendrajit International Airport in Imphal for your flight home. Your premium Best Manipur Tour Package concludes with seamless assistance, leaving your family with beautiful stories and unforgettable memories that will be cherished for a lifetime.'
                ),
                [
                    'Transfers Included: Private Luxury Airport Drop-off',
                    'Meals Included: Premium Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Classic / Similar | Sendra Park Resort (Deluxe Room)',
                'Imphal | Loktak Moirang',
                '5N Imphal|1N Loktak/Moirang',
                'Deluxe',
                'Executive Room',
                'MAPAI',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Classic / Similar | Sendra Park Resort (Deluxe Room) | MAPAI',
            ),
            _hotel(
                'The Classic Grande / Similar | Sendra Park Resort (Cottage)',
                'Imphal | Loktak Moirang',
                '5N Imphal|1N Loktak/Moirang',
                'Premium',
                'Superior Room',
                'MAPAI',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Classic Grande / Similar | Sendra Park Resort (Cottage) | MAPAI',
            ),
            _hotel(
                'Classic Grande - Member of Radisson Individuals | Sendra Luxury Lake Resort (Suite)',
                'Imphal | Loktak Moirang',
                '5N Imphal|1N Loktak/Moirang',
                'Luxury',
                'Deluxe Suite Room',
                'MAPAI',
                5,
                3,
                description='OPTION 03 – LUXURY: Classic Grande - Member of Radisson Individuals | Sendra Luxury Lake Resort (Suite) | MAPAI',
            ),
            _hotel(
                'Elite Premium Royal Suites Selection | Premium Overwater Villa Tier Selection',
                'Imphal | Loktak Moirang',
                '5N Imphal|1N Loktak/Moirang',
                'Ultra Luxury',
                'Ultra Premium Elite Package',
                'Ultra Premium Elite Package',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Elite Premium Royal Suites Selection | Premium Overwater Villa Tier Selection | Ultra Premium Elite Package',
            )
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Handpicked luxury stays chosen carefully for family comfort.', 1),
            _inc_included('Daily Meal Plan: Healthy, delicious breakfasts and grand dinners included every day.', 2),
            _inc_included('Luxury Transfers: Dedicated private AC Innova Crysta for all airport transfers, excursions, and inter-city travel.', 3),
            _inc_included('Immersive Experiences: Private boat charter on Loktak Lake and exclusive craft tours in Andro.', 4),
            _inc_included('Welcome Amenities: Personalized luxury travel welcome kit and refreshing traditional mocktails upon arrival.', 5),
            _inc_included('Expert Assistance: 24/7 dedicated TRAGUIN logistics support and professional English/Hindi speaking guides.', 6),
            _inc_included('All Taxes Included: Tolls, driver allowances, parking fees, and state luxury taxes are fully covered.', 7),
            _inc_excluded('Airfare or train tickets to and from Imphal.', 8),
            _inc_excluded('Personal expenses such as laundry, telephone calls, alcoholic beverages, and mini-bar usage.', 9),
            _inc_excluded('Monastery, museum, and national park entry tickets or camera fees.', 10),
            _inc_excluded('Optional activities or meals not specifically highlighted in the day-wise itinerary.', 11),
        ],
    )
    return package, itinerary

def build_mn_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MN-007'
    tour_code = 'TG-MAN-EDU-007'
    title = 'Manipur Educational Tour — Imphal • Loktak Lake • Moirang • Khongjom'
    duration = '04 Nights / 05 Days'
    slug = 'mn-007-manipur-educational-tour'
    itin_slug = 'mn-007-manipur-educational-tour-itinerary'
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
            _ph('Serial code MN-007 | TRAGUIN tour code TG-MAN-EDU-007', 1),
            _ph('State / Country: Manipur / India | Category: School / Educational', 2),
            _ph('Destinations: Imphal • Moirang • Loktak Lake • Khongjom • Moreh Border', 3),
            _ph('Ideal for: Students, Educators, Institutions', 4),
            _ph('Best season: October to April', 5),
            _ph('Starting price: On Request (Group Pricing)', 6),
            _ph('Vehicle / Meals: Premium Luxury Coaches (Fully Air-Conditioned with professional drivers)', 7),
            _ph('Route: Imphal Arrival • Kangla Fort • Loktak Lake • Moirang • Khongjom Battlefields • Imphal Departure', 8),
            _ph('TRAGUIN Signature Experience: Specialized expert interactions with environmental activists', 9),
            _ph('Curated by TRAGUIN Experts: Safety prioritized parameters with pre-scouted routes, emergency-', 10),
            _ph('Exclusive Recommendations: Experiencing the famous traditional Manipuri Thang-Ta (martial arts)', 11),
            _ph('TRAGUIN Premium Travel Experience', 12),
            _ph('All student lists must be shared along with institutional authorization letters 30 days prior for smooth', 13),
            _ph('security check alignments.', 14)
        ],
        moods=['Educational', 'Culture', 'Nature'],
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
        tagline='Manipur Educational Tour',
        overview="Imphal • Loktak Lake • Moirang • Khongjom • Keibul Lamjao Welcome to an unforgettable journey curated by TRAGUIN to the 'Jeweled Land' of Manipur. Designed specifically for young minds, our Luxury Manipur Holiday and experiential curriculum offer breathtaking TRAGUIN Premium Travel Experience 1 landscapes, immersive cultural exchanges, and deep historical context. This is the ultimate Manipur Educational Tour, combining pristine nature with key educational landmarks.\n\nTOUR OVERVIEW\nThis premium Manipur Family Tour and student group itinerary is perfectly crafted for comprehensive learning. As an industry-leading Premium Manipur Experience, we blend interactive sightseeing with safe, comfortable, and premium group logistics. Travel Dates: Flexible / Customizable as per institution requirements Group / FIT: Student Group Special (Accompanied by tour educators & professional guides) Vehicle: Premium Luxury Coaches (Fully Air-Conditioned with professional drivers) Meal Plan: All Meals Included (Breakfast, Lunch, and Dinner served fresh) Route: Imphal Arrival • Kangla Fort • Loktak Lake • Moirang • Khongjom Battlefields • Imphal Departure TRAGUIN Curated Experience Note: Every single destination features expert storytelling sessions covering WWII histories, unique ecological bio-diversities, and indigenous traditions.\n\nWHY CHOOSE A MANIPUR EDUCATIONAL TOUR?\nManipur is quickly emerging as one of the top searched destinations for experiential learning in Northeast India. Offering the Best Manipur Tour Package for academic groups, it presents a living classroom. Students explore the world's only floating national park, interact with weavers at Asia's largest all-women market, and walk the grounds of monumental World War II battlefields. From the popular Instagram locations like the floating phumdis of Loktak Lake to cultural heritage sites like Kangla Fort, this trip hits all the Top Tourist Places in Manipur. It provides an immersive look into indigenous governance, Commonwealth history, unique geographical phenomena, and ecological conservation strategies, making it the finest Manipur Sightseeing ecosystem for schools. DAY WISE DETAILED ITINERARY",
        seo_title='MN-007 | Manipur Educational Tour | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Manipur package (MN-007 / TG-MAN-EDU-007): Imphal • Moirang • Loktak Lake • Khongjom • Moreh Border with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN IMPHAL — GATEWAY TO THE JEWELED LAND', 1),
            _ih('Day 02: THE LIVING ECOLOGY — LOKTAK LAKE & KEIBUL LAMJAO', 2),
            _ih('Day 03: HERITAGE & PATRIOTISM — MOIRANG & INA MEMORIAL', 3),
            _ih('Day 04: MILITARY HISTORY & EMPOWERMENT — KHONGJOM & IMA KEITHEL', 4),
            _ih('Day 05: DEPARTURE WITH FOREVER MEMORIES — VALEDICTORY', 5),
            _ih('TRAGUIN Signature Experience: Specialized expert interactions with environmental activists', 6),
            _ih('Curated by TRAGUIN Experts: Safety prioritized parameters with pre-scouted routes, emergency-', 7),
            _ih('Exclusive Recommendations: Experiencing the famous traditional Manipuri Thang-Ta (martial arts)', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN IMPHAL — GATEWAY TO THE JEWELED LAND',
                (
                    'Arrive at Bir Tikendrajit International Airport in Imphal, where the premium TRAGUIN team welcomes your institution with traditional stoles. Transfer in luxury coaches to your premium handpicked hotel. After check-in and an orientation briefing, we begin our exploration at Kangla Fort, the ancient seat of power for the Kingdom of Manipur. Students will learn about pre-colonial archaeological ruins and traditional solar-aligned architecture.'
                ),
                [
                    'Sightseeing Included: Kangla Fort, Archaeological Museum, Govindajee Temple.',
                    'Evening Experience: Interactive orientation and ice-breaking session on Manipuri heritage.',
                    'Overnight Stay: Imphal (Premium/Luxury Hotel Select).',
                    'Meals Included: Lunch & Dinner.',
                ],
            ),
            _day(
                2,
                'THE LIVING ECOLOGY — LOKTAK LAKE & KEIBUL LAMJAO',
                (
                    "An early morning drive leads us to the iconic Loktak Lake, the largest freshwater lake in Northeast India, famous for its unique floating islands called phumdis. We check into an immersive experience at the Keibul Lamjao National Park, the world's only floating wildlife sanctuary. Students will conduct field observations to spot the critically endangered Sangai (Brow-antlered deer), analyzing conservation methods and wetland ecosystems. point."
                ),
                [
                    'Sightseeing Included: Loktak Lake boat safari, Keibul Lamjao National Park tracking, Sendra Hills view',
                    'Optional Activities: Interaction with local fishermen regarding sustainable inland fishing technologies.',
                    'Evening Experience: Audio-visual presentation on the unique biodiversity of the Indo-Burma hotspot.',
                    'Overnight Stay: Imphal.',
                    'Meals Included: Breakfast, Lunch & Dinner.',
                ],
            ),
            _day(
                3,
                'HERITAGE & PATRIOTISM — MOIRANG & INA MEMORIAL',
                (
                    "Dive into national modern history by visiting Moirang. Here, the Indian National Army (INA) under Netaji Subhash Chandra Bose unfurled the tricolor flag on Indian soil for the first time in 1944. Students explore the INA Martyr's Complex, analyzing rare letters, uniform remnants, and historical battlefield documentation. This day covers core elements of the Best Time to Visit Manipur syllabus, matching high emotional patriotism with academic curriculum. introduction)."
                ),
                [
                    'Sightseeing Included: INA Memorial Museum, Moirang Bazaar, historical battle mapping markers.',
                    'Evening Experience: Traditional Meitei cultural dance demonstration (Pung Cholom & Ras Leela',
                    'Overnight Stay: Imphal.',
                    'Meals Included: Breakfast, Lunch & Dinner.',
                ],
            ),
            _day(
                4,
                'MILITARY HISTORY & EMPOWERMENT — KHONGJOM & IMA KEITHEL',
                (
                    "Travel down the Indo-Myanmar highway to the Khongjom War Memorial Complex, dedicated to the Anglo- Manipur War of 1891. Students explore historical hillsides where soldiers fought alongside Major Paona Brajabashi. In the afternoon, we return to Imphal to study a unique socio-economic marvel: the Ima Keithel (Mother's Market), a 500-year-old market managed completely by over 5,000 married women, offering an incredible lesson in community finance and female leadership. Market."
                ),
                [
                    'Sightseeing Included: Khongjom Memorial, Imphal WWII Commonwealth War Cemetery, Ima Keithel',
                    'Evening Experience: Debating session and project brief completion. Souvenir collection and photography.',
                    'Overnight Stay: Imphal.',
                    'Meals Included: Breakfast, Lunch & Dinner.',
                ],
            ),
            _day(
                5,
                'DEPARTURE WITH FOREVER MEMORIES — VALEDICTORY',
                (
                    'Enjoy a relaxed breakfast at your premium stay. Complete a final reflection circle overseen by your travel consultants. Students are presented with specialized certificates of participation from TRAGUIN Packages. Board the luxury coach for a smooth airport transfer, taking home unforgettable memories and profound geographical insights.'
                ),
                [
                    'Sightseeing Included: Local handloom visual center (brief visit).',
                    'Overnight Stay: Tour Concluded.',
                    'Meals Included: Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Classic Hotel / Hotel Imphal',
                'Imphal',
                '4N Imphal',
                'Deluxe',
                'Executive Twin Bed / Triple Bed Options',
                'Breakfast & Dinner (MAPAI)',
                4,
                1,
                description='OPTION 01 – DELUXE: Classic Hotel / Hotel Imphal | Breakfast & Dinner (MAPAI)',
            ),
            _hotel(
                'The Classic Grande (A Member of Radisson Individuals)',
                'Imphal',
                '4N Imphal',
                'Premium',
                'Superior Deluxe Twin Rooms',
                'All Meals Curated (APAI)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Classic Grande (A Member of Radisson Individuals) | All Meals Curated (APAI)',
            ),
            _hotel(
                'Premium Heritage Palace / Elite Suites',
                'Imphal',
                '4N Imphal',
                'Luxury',
                'Luxury Club Rooms',
                'All Meals Curated + High Tea',
                5,
                3,
                description='OPTION 03 – LUXURY: Premium Heritage Palace / Elite Suites | All Meals Curated + High Tea',
            ),
            _hotel(
                'Exclusive Boutique Eco-Resorts / Royal Palace Wings',
                'Imphal',
                '4N Imphal',
                'Ultra Luxury',
                'Signature Executive Suites',
                'Gourmet Customized Institutional Catering',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Exclusive Boutique Eco-Resorts / Royal Palace Wings | Gourmet Customized Institutional Catering',
            )
        ],
        inclusions=[
            _inc_included('04 Nights premium accommodation in select twin/triple occupancy.', 1),
            _inc_included('Standard customized institutional meals (Breakfast, Lunch & Dinner).', 2),
            _inc_included('All point-to-point transfers via fully sanitized Luxury AC Coaches.', 3),
            _inc_included('Full academic entries to Kangla Fort, INA Complex, and Khongjom.', 4),
            _inc_included('Special boat safari inside the core eco-zone of Loktak Lake.', 5),
            _inc_included('Comprehensive TRAGUIN Support with a dedicated Tour Manager 24/7.', 6),
            _inc_included('All local state taxes, parking fees, and professional guiding charges.', 7),
            _inc_excluded('Inbound/Outbound Domestic or International airfares.', 8),
            _inc_excluded('Personal expenditures (laundry, optional shopping, telephone calls).', 9),
            _inc_excluded('Extra food ordering outside our pre-fixed curated school menus.', 10),
            _inc_excluded('Comprehensive travel insurance or early medical evacuations.', 11),
            _inc_excluded('Camera fees, video recording special permits inside historic museums.', 12),
        ],
    )
    return package, itinerary

def build_mn_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MN-008'
    tour_code = 'TRAGUIN-MN-008'
    title = 'Imphal Heritage Tour'
    duration = '04 Nights / 05 Days'
    slug = 'mn-008-imphal-heritage-tour'
    itin_slug = 'mn-008-imphal-heritage-tour-itinerary'
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
            _ph('Serial code MN-008 | TRAGUIN tour code TRAGUIN-MN-008', 1),
            _ph('State / Country: Manipur / India | Category: Family Tour', 2),
            _ph('Destinations: Imphal • Moirang • Loktak Lake • Andro', 3),
            _ph('Ideal for: Family & Heritage Travellers', 4),
            _ph('Best season: October to April', 5),
            _ph('Starting price: On Request (Premium FIT)', 6),
            _ph('Vehicle / Meals: Luxury Private Innova / SUV', 7),
            _ph('TRAGUIN Signature Experience: Private guided interactions with local state-award winning artisans at Andro', 8),
            _ph('Curated by TRAGUIN Experts: Smartly timed departures to ensure optimal wildlife sighting possibilities at Keibul', 9),
            _ph('Premium Handpicked Hotels: Accommodations chosen for their excellent prime safety locations and superb multi-', 10),
            _ph('Luxury Transportation: Highly trained, polite, and English/Hindi-fluent local chauffeurs with deep knowledge of', 11)
        ],
        moods=['Family', 'Heritage', 'Culture'],
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
        tagline='Imphal Heritage Tour',
        overview='I M P H A L H E R I TA G E T O U R 04 Nights / 05 Days of Curated Luxury, Immersive Culture, and Unforgettable Family Memories Welcome to the jewel of Northeast India! The Luxury Manipur Holiday customized by TRAGUIN unrolls a beautiful canvas of breathtaking landscapes, royal legacy, and profound historical depth. Specially crafted for families looking for an exclusive and deeply enriching getaway, this premium itinerary offers an elegant fusion of handpicked hotels, seamless luxury private transportation, and expertly curated experiences. From the floating islands of the legendary Loktak Lake to the heroic chronicles of the INA and WWII battlegrounds, your TRAGUIN Premium Luxury Holidays • Manipur Heritage family will discover an exquisite land of raw scenic beauty, vibrant shopping bazaars, and deep cultural insights.\n\nTOUR OVERVIEW\nThis customized Best Manipur Tour Package is curated by TRAGUIN Experts to offer a relaxed yet comprehensive exploration of the central and southern heritage corridors of Manipur. Travelling via a dedicated premium private vehicle with full chauffeured service, your family will enjoy personalized assistance from the moment you step off the plane at Imphal Airport. TRAGUIN Curated Experience Note: Your comfort is our utmost priority. This itinerary has been mindfully organized with optimal travel timings, minimal walking fatigue, premium culinary arrangements, and handpicked boutique properties to make it a perfect, stress-free choice for multi-generational family vacations.\n\nWHY CHOOSE A PREMIUM MANIPUR EXPERIENCE?\nManipur, often praised as the "Switzerland of the East," remains one of India’s most captivating yet pristine travel secrets, offering a wealth of highly sought-after Manipur Sightseeing treasures. Families choosing a Manipur Family Tour are greeted by a breathtaking collage of rolling green hills, iconic heritage sites, and unparalleled cultural warmth. Here, you will visit the world’s only floating national park, explore ancient royal seat coordinates at Kangla, and walk through the historic, globally unique Ima Keithel—an all-women-run market that serves as a powerful symbol of Manipuri heritage and community. For photography enthusiasts and social storytellers, the region boasts exceptional, highly trending Instagram locations—such as the serene viewpoints over the pristine waters of Loktak Lake, the historic Japanese Peace Treaty memorial at Red Hill, and the meticulously sculpted pottery blocks of Andro Heritage Village. Whether you want to deep dive into old Anglo-Manipuri conflict history, sample delicious local organic delicacies, or shop for premium hand-woven visual souvenirs like the classic Moirang Phee fabrics, this journey promises an absolute wealth of immersive experiences and unforgettable memories.',
        seo_title='MN-008 | Imphal Heritage Tour | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Manipur package (MN-008 / TRAGUIN-MN-008): Imphal • Moirang • Loktak Lake • Andro with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN IMPHAL', 1),
            _ih('Day 02: IMPHAL SIGHTSEEING & CULTURE', 2),
            _ih('Day 03: EXCURSION TO LOKTAK LAKE & MOIRANG', 3),
            _ih('Day 04: HERITAGE EXCURSION TO ANDRO VILLAGE', 4),
            _ih('Day 05: SOUVENIR SHOPPING & DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private guided interactions with local state-award winning artisans at Andro', 6),
            _ih('Curated by TRAGUIN Experts: Smartly timed departures to ensure optimal wildlife sighting possibilities at Keibul', 7),
            _ih('Premium Handpicked Hotels: Accommodations chosen for their excellent prime safety locations and superb multi-', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN IMPHAL',
                (
                    'A ROYAL WELCOME TO THE ANCIENT CAPITAL CORRIDOR Your extraordinary Luxury Manipur Holiday begins with your arrival at Bir Tikendrajit International Airport in Imphal. As you step out, a dedicated TRAGUIN corporate greeting representative will warmly receive your family and escort you to your premium private luxury vehicle. Enjoy a seamless transfer to your handpicked luxury hotel, taking in your first glimpses of the bustling city nestled within a scenic, hill-ringed valley basin. TRAGUIN Premium Luxury Holidays • Manipur Heritage After a smooth check-in and an exquisite lunch at the hotel’s premium restaurant, embark on an introductory tour of the ancient Kangla Fort. This vast archaeological complex represents the historic seat of the former Meitei rulers and stands as one of the Top Tourist Places in Manipur. Explore the preserved royal moat structures, the sacred inner polo ground boundaries, and the elegant, reconstructed twin statues of the Kangla Sha (sacred mythical dragons). As dusk settles over the city, enjoy a sophisticated high-tea experience looking over the fort ramparts before returning to your hotel for a relaxing evening. cuisines.'
                ),
                [
                    'Sightseeing Included: Kangla Fort Complex, Kangla Sha Statues, Royal Moats, Heritage Galleries.',
                    'Optional Activities: Private guided slow-paced golf-cart tour within the expansive Kangla Fort complex.',
                    'Evening Experience: Premium curated multi-course dinner highlighting fine signature Indian and continental',
                    'Overnight Stay: Imphal (Premium Luxury Hotel Option)',
                    'Meals Included: Lunch & Dinner',
                ],
            ),
            _day(
                2,
                'IMPHAL SIGHTSEEING & CULTURE',
                (
                    "IMMERSIVE CULTURAL ENCOUNTERS & ICONIC HERITAGE LANDMARKS Wake up to a crisp morning and enjoy a lavish buffet breakfast. Today is dedicated to exploring the core highlights of Imphal Sightseeing. Your premium family tour begins with a visit to the globally celebrated Ima Keithel (Mother’s Market). Dating back over 500 years, this magnificent, bustling market is managed entirely by thousands of local married women. Walking through its vibrant aisles is an incredible cultural immersion, filled with the rich aromas of fresh local spices, beautiful hand-woven textiles, and masterfully crafted bamboo souvenirs. Next, visit the beautifully maintained Imphal WWII War Cemetery, a deeply touching commonwealth memorial that honors British, Indian, and Allied soldiers who fought valiantly during the historic 1944 Battle of Imphal. In the afternoon, explore the Manipur State Museum to admire an impressive collection of royal artifacts, ancient tribal costumes, and a magnificent 54-foot-long royal boat (Hiyang Hiren). Conclude your afternoon at the peaceful Govindaji Temple, watching the elegant afternoon direct prayer rituals and architectural gold-domed reflections. It's a wonderful opportunity for beautiful family photography. Temple. Shawls. experience. TRAGUIN Premium Luxury Holidays • Manipur Heritage"
                ),
                [
                    'Sightseeing Included: Ima Keithel, Imphal War Cemetery, Manipur State Museum, Shree Shree Govindaji',
                    'Optional Activities: Exclusive interactive meeting arranged with a master weaver of traditional Phanek and',
                    'Evening Experience: Leisurely stroll through local premium handicraft galleries followed by a fine-dining',
                    'Overnight Stay: Imphal (Premium Luxury Hotel Option)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'EXCURSION TO LOKTAK LAKE & MOIRANG',
                (
                    "THE WONDERS OF THE FLOATING NATIONAL PARK & VALIANT HISTORY Following an early gourmet breakfast, embark on a scenic private drive southward toward the legendary Loktak Lake, the largest freshwater lake in Northeast India and a centerpiece of any Manipur Honeymoon Package or premium family getaway. This breathtaking natural marvel is world-renowned for its unique Phumdis—heterogeneous masses of vegetation, soil, and organic matter that float elegantly on the water's surface, creating an incredible landscape. Board an exclusive private boat to glide across the serene waters, visiting the remarkable Keibul Lamjao National Park—the world's only floating national park and the final natural sanctuary for the critically endangered, brow-antlered Sangai Deer (the dancing deer of Manipur). Keep your binoculars ready for unforgettable wildlife encounters. Afterward, drive to the historic town of Moirang to visit the INA Martyr’s Memorial Complex. This is the historic site where Netaji Subhas Chandra Bose’s Indian National Army proudly hoisted the Indian Tri-color flag on mainland soil for the very first time in 1944. Explore the museum's fascinating collection of wartime photographs, currency, and battlefield relics before driving past the scenic Sendra Hills on your smooth return journey to Imphal. Views. Phumdis. organic dishes."
                ),
                [
                    'Sightseeing Included: Loktak Lake Cruise, Keibul Lamjao Floating Park, INA Memorial Museum, Sendra Hill',
                    'Optional Activities: A premium traditional canoe ride steered by local fishermen for a closer look at the',
                    'Evening Experience: Relaxing family dinner at the hotel featuring a specially curated tasting menu of local',
                    'Overnight Stay: Imphal (Premium Luxury Hotel Option)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'HERITAGE EXCURSION TO ANDRO VILLAGE',
                (
                    "LIVING CHRONICLES OF ANCIENT CLAY ARTISTRY & ECO-CULTURE After a relaxed breakfast, your luxury private vehicle takes you on an enriching cultural journey east to the ancient Andro Heritage Village. Nestled against the backdrop of rolling green hills, Andro is an extraordinary living eco-cultural museum. The village is highly celebrated for its ancient, ancestral coil-pottery techniques, meticulously preserved exclusively by the married women of the community. Walk through the open-air cultural heritage complex to see traditional thatched tribal huts, ancestral totem poles, and a fascinating collection of regional wood carvings and stone structures. Witness a live demonstration of Charai Taba (coil pottery creation) without using a traditional potter's wheel. You'll also visit the sacred fire temple, home to a ritual flame that has been kept burning continuously since the 4th century. TRAGUIN Premium Luxury Holidays • Manipur Heritage On your way back to Imphal, stop at the lush Kakching Garden, a beautifully landscaped hill-slope garden that offers stunning, expansive panoramic views over the sprawling valley below. Garden. artisan."
                ),
                [
                    'Sightseeing Included: Andro Cultural Museum, Ancient Pottery Workshop, Sacred Fire Temple, Kakching',
                    'Optional Activities: A hands-on pottery shaping session under the warm guidance of an expert village',
                    'Evening Experience: A grand farewell family dinner arranged at a premium specialty restaurant in Imphal.',
                    'Overnight Stay: Imphal (Premium Luxury Hotel Option)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'SOUVENIR SHOPPING & DEPARTURE',
                (
                    'BIDDING FAREWELL TO THE LAND OF JEWELS Enjoy your final lavish breakfast at the hotel before checking out. Depending on your flight schedule, your premium private vehicle will be at your service for any last-minute premium shopping or sightseeing. Visit the state-run Central Handicrafts Emporium to pick up exquisite souvenirs like fine bamboo baskets, local organic black rice, and beautiful, authentic Manipuri dolls. Your unforgettable TRAGUIN Manipur Package comes to a close as you are chauffeured in smooth luxury to Bir Tikendrajit International Airport for your onward flight. Board your plane with beautiful photographs, deeply enriched perspectives, and cherished, unforgettable family memories of this spectacular heritage kingdom.'
                ),
                [
                    'Sightseeing Included: Local Craft Emporiums, Visual Souvenir Shopping Stopovers.',
                    'Optional Activities: A final photography stop at the historic high-pillars of the city gate if time permits.',
                    'Evening Experience: Seamless airport drop-off with complete baggage handling assistance.',
                    'Overnight Stay: Departure / End of Tour Services',
                    'Meals Included: Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Imphal by The Classic (Heritage Wing)',
                'Imphal',
                '4N Imphal',
                'Deluxe',
                'Executive Deluxe Room',
                'CP / MAP AI',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Imphal by The Classic (Heritage Wing) | CP / MAP AI',
            ),
            _hotel(
                'The Classic Grand (Premium Business Address)',
                'Imphal',
                '4N Imphal',
                'Premium',
                'Grand Deluxe Room',
                'MAP Plan',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Classic Grand (Premium Business Address) | MAP Plan',
            ),
            _hotel(
                'Classic Grand / Premium Boutique Suites',
                'Imphal',
                '4N Imphal',
                'Luxury',
                'Executive Suite Comfort',
                'MAP Plan',
                5,
                3,
                description='OPTION 03 – LUXURY: Classic Grand / Premium Boutique Suites | MAP Plan',
            ),
            _hotel(
                'Handpicked Elite Corporate Suites / Classic Luxury',
                'Imphal',
                '4N Imphal',
                'Ultra Luxury',
                'Presidential / Royal Suite',
                'Custom Luxury Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Handpicked Elite Corporate Suites / Classic Luxury | Custom Luxury Plan',
            )
        ],
        inclusions=[
            _inc_included('Premium Accommodation: 04 Nights stay in handpicked, top-rated hotels.', 1),
            _inc_included('Private Transfers: All transfers & sightseeing via a luxury private Innova/SUV.', 2),
            _inc_included('Meal Plan: Daily buffet breakfast and curated multi-course dinners.', 3),
            _inc_included('Exclusive Boat Cruise: Private chartered boat experience on Loktak Lake.', 4),
            _inc_included('Personalized Support: 24/7 dedicated TRAGUIN Support access line.', 5),
            _inc_included('Welcome Amenities: Traditional Manipuri stoles and local organic welcome platter.', 6),
            _inc_included('All Tolls & Taxes: Includes all driver allowances, fuel, state tolls, and GST.', 7),
            _inc_excluded('Airfare / Rail: Domestic or international flight tickets to/from Imphal.', 8),
            _inc_excluded('Entry Fees: Camera charges and monument entry tickets at heritage sites.', 9),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, premium bar tabs, and tips.', 10),
            _inc_excluded('Optional Activities: Any activities marked optional in the itinerary text.', 11),
            _inc_excluded('Travel Insurance: Comprehensive medical or trip cancellation insurance cover.', 12),
            _inc_excluded('Additional Extensions: Any detour costs due to bad weather or flight delays.', 13),
        ],
    )
    return package, itinerary

def build_mn_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MN-009'
    tour_code = 'TRAGUIN-MN-009-ROMANTIC'
    title = 'Romantic Loktak Lake Escapade • Imphal Luxury'
    duration = '04 Nights / 05 Days'
    slug = 'mn-009-romantic-loktak-lake-escapade-imphal-luxury'
    itin_slug = 'mn-009-romantic-loktak-lake-escapade-imphal-luxury-itinerary'
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
            _ph('Serial code MN-009 | TRAGUIN tour code TRAGUIN-MN-009-ROMANTIC', 1),
            _ph('State / Country: Manipur / India | Category: Honeymoon / Romantic', 2),
            _ph('Destinations: Imphal • Loktak Lake • Sendra Hills • Moirang', 3),
            _ph('Ideal for: Newlyweds & Couples', 4),
            _ph('Best season: October to May', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Chauffeur Sedan (Chauffeur-driven Premium Segment)', 7),
            _ph('TRAGUIN Signature Experience: Private', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked', 9),
            _ph('Exclusive Recommendations: Personalized', 10)
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
        tagline='Romantic Loktak Lake Escapade',
        overview="04 Nights / 05 Days Exclusive Romantic Experience SERIAL CODE: MN-009 STATE / COUNTRY: Manipur / India CATEGORY: Honeymoon / Romantic DURATION: 04 Nights / 05 Days DESTINATIONS: Imphal • Loktak Lake • Sendra Hills • Moirang IDEAL FOR: Newlyweds & Couples BEST SEASON: October to May STARTING PRICE: On Request TRAGUIN TOUR CODE: TRAGUIN-MN-009- ROMANTIC INTRODUCTION Celebrate your unique love story amidst the pristine landscapes of Northeast India. The Best Manipur Tour Package by TRAGUIN presents an intimate, magical getaway tailored beautifully for newlyweds. Fall in love all over again alongside the legendary floating islands of Loktak Lake, watch unforgettable golden sunsets from Sendra Hills, and enjoy private candlelight dining under a canopy of stars. This romantic Manipur Honeymoon Package combines curated luxury, beautiful scenery, and handpicked hotels to create an unforgettable couple's escape filled with immersive experiences.\n\nTOUR OVERVIEW\nTravel Framework: Ultra-Private Couple's Escape (FIT) Vehicle: Private Luxury Chauffeur Sedan (Chauffeur-driven Premium Segment) Meal Plan: Modified American Plan (CPAI + Candlelight Specialty Dinner Arrangement) Route Outline: Imphal Arrival → Sendra Floating Lakes → Romantic Loktak Exploration → Imphal Luxury Leisure → Departure 1 TRAGUIN Curated Experience: Welcome floral arrangements, private lake cruise, couple's photography points, and signature lakeside high tea. DESTINATION INSIGHTS & SEO RICH CONTENT When searching for the perfect romantic getaway, the Top Tourist Places in Manipur stand out for their serene charm and stunning scenery. This customized Luxury Manipur Holiday provides a beautiful escape far from crowded tourist tracks. Couples can experience the unique beauty of Loktak Lake, explore the world's only floating national park at Keibul Lamjao, and enjoy peaceful walks through the historic Kangla Fort gardens. Our meticulously arranged TRAGUIN Manipur Packages feature the best Manipur Sightseeing locations, offering incredible Instagram backdrops and quiet moments together. The Best Time to Visit Manipur is between October and May, offering clear blue skies and pleasant weather to explore this premium paradise. 2",
        seo_title='MN-009 | Romantic Loktak Lake Escapade | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Manipur package (MN-009 / TRAGUIN-MN-009-ROMANTIC): Imphal • Loktak Lake • Sendra Hills • Moirang with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN IMPHAL → ROMANTIC SENDRA HILLS', 1),
            _ih('Day 02: EXCLUSIVE LOKTAK LAKE CRUISE & FLOATING PARK', 2),
            _ih('Day 03: MOIRANG HERITAGE TO IMPHAL RETREAT', 3),
            _ih('Day 04: IMPHAL ROMANTIC HIGHLIGHTS & SIGHTSEEING', 4),
            _ih('Day 05: FAREWELL FROM IMPHAL', 5),
            _ih('TRAGUIN Signature Experience: Private', 6),
            _ih('Curated by TRAGUIN Experts: Handpicked', 7),
            _ih('Exclusive Recommendations: Personalized', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN IMPHAL → ROMANTIC SENDRA HILLS',
                (
                    'WELCOME AMENITIES AND GOLDEN SUNSET VIEWS OVER LOKTAK LAKE Arrive at Imphal Airport where a premium private vehicle awaits to take you on a scenic drive to the beautiful Sendra Hills, overlooking the magnificent Loktak Lake. Upon arrival, enjoy a seamless check-in at your luxury lake-view resort. Celebrate the beginning of your honeymoon with a signature TRAGUIN welcome basket featuring local chocolates and premium sparkling juice. As evening falls, relax together on your private balcony to watch a breathtaking sunset over the shimmering floating islands.'
                ),
                [
                    'Sightseeing Included: Sendra Hills Viewpoints, Loktak Panoramic Vistas.',
                    'Evening Experience: Romantic lakeside stroll followed by an intimate dinner.',
                    'Overnight Stay: Sendra Premium Lakefront Resort.',
                    'Meals Included: Welcome Drinks & Romantic Dinner.',
                ],
            ),
            _day(
                2,
                'EXCLUSIVE LOKTAK LAKE CRUISE & FLOATING PARK',
                (
                    "PRIVATE BOAT CRUISE AND UNIQUE WILDLIFE DISCOVERIES Wake up to misty lake views and enjoy a delicious breakfast. Today, experience a private boat cruise across the pristine waters of Loktak Lake, tailored exclusively for couples. Glide past the unique floating phumdis and visit the Keibul Lamjao National Park—the world's only floating wildlife sanctuary. Keep an eye out for the rare and elegant Sangai brow-antlered deer. In the afternoon, enjoy a premium high-tea experience setup on a scenic hillock, offering perfect photography backdrops for couples. 3"
                ),
                [
                    'Sightseeing Included: Keibul Lamjao National Park, Private Loktak Longboat Cruise.',
                    'Evening Experience: Premium lakeside high-tea setup with personalized service.',
                    'Overnight Stay: Sendra Premium Lakefront Resort.',
                    'Meals Included: Breakfast & Afternoon High-Tea.',
                ],
            ),
            _day(
                3,
                'MOIRANG HERITAGE TO IMPHAL RETREAT',
                (
                    "CULTURAL MILESTONES AND PRIVATE CANDLELIGHT DINING After breakfast, take a scenic drive to Moirang to explore the historic INA Memorial Complex and learn about the region's fascinating royal love stories. In the afternoon, return to Imphal and check into your luxury city hotel. Spend a relaxed afternoon enjoying the premium amenities or spoiling yourselves with a therapeutic couple's spa session. The highlight of your evening is an exclusive, private candlelight dinner curated by TRAGUIN experts, set under the stars with a beautifully personalized menu. 4"
                ),
                [
                    'Sightseeing Included: Moirang Cultural Center, INA Monument, Imphal Royal Pathways.',
                    "Optional Activities: Therapeutic couple's traditional spa treatment.",
                    'Evening Experience: Signature candlelight dinner with premium floral table styling.',
                    'Overnight Stay: Imphal Luxury Partner Hotel.',
                    'Meals Included: Breakfast & Specialized Candlelight Dinner.',
                ],
            ),
            _day(
                4,
                'IMPHAL ROMANTIC HIGHLIGHTS & SIGHTSEEING',
                (
                    "HISTORIC PALACES, LOVERS' LANES AND EXCLUSIVE SHOPPING Enjoy a delicious breakfast before exploring the beautiful sights of Imphal. Take a romantic walk through the historic Kangla Fort, wandering along the serene rose gardens and peaceful moats. Visit the nearby craft markets to pick up beautiful handwoven souvenirs. Later, enjoy a quiet afternoon coffee date at a charming local café, known for its artistic atmosphere and delicious regional treats. Spend your final evening at leisure, relaxing and reflecting on your wonderful journey together."
                ),
                [
                    'Sightseeing Included: Kangla Fort Gardens, Royal Palace Temples, Ima Keithel.',
                    'Evening Experience: Private café reservation and quiet evening walk.',
                    'Overnight Stay: Imphal Luxury Partner Hotel.',
                    'Meals Included: Breakfast & High-End Café Voucher.',
                ],
            ),
            _day(
                5,
                'FAREWELL FROM IMPHAL',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES OF YOUR HONEYMOON Savor a relaxed breakfast together on your final morning in Manipur. Take advantage of a late check-out before your private chauffeur transfers you comfortably to Imphal International Airport for your journey home. Leave with beautiful photos, a deeper connection, and unforgettable memories from your premium getaway curated by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private airport transfer in a luxury vehicle.',
                    'Meals Included: Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Sendra Park Resort (Standard) | The Classic Hotel',
                'Lakeside | Imphal',
                '2N Lakeside|2N Imphal',
                'Deluxe',
                'Standard | Classic Hotel',
                'Welcome Drink & Cake',
                4,
                1,
                description='OPTION 01 – DELUXE: Sendra Park Resort (Standard) | The Classic Hotel | Welcome Drink & Cake',
            ),
            _hotel(
                'Sendra Resort (Lake View Cottage) | Classic Grande (Superior)',
                'Lakeside | Imphal',
                '2N Lakeside|2N Imphal',
                'Premium',
                'Lake View Cottage | Superior',
                'Bed Decoration + Fruit Basket',
                4,
                2,
                description='OPTION 02 – PREMIUM: Sendra Resort (Lake View Cottage) | Classic Grande (Superior) | Bed Decoration + Fruit Basket',
            ),
            _hotel(
                'Loktak Floating Luxury Cabins | Radisson Suite Properties',
                'Lakeside | Imphal',
                '2N Lakeside|2N Imphal',
                'Luxury',
                'Floating Luxury Cabin | Radisson Suite',
                'Candlelight Dinner + Floral Decor',
                5,
                3,
                description='OPTION 03 – LUXURY: Loktak Floating Luxury Cabins | Radisson Suite Properties | Candlelight Dinner + Floral Decor',
            ),
            _hotel(
                'The Sangai Premium Floating Villa | The Sangai Luxury City Suites',
                'Lakeside | Imphal',
                '2N Lakeside|2N Imphal',
                'Ultra Luxury',
                'Premium Floating Villa | Luxury City Suite',
                'Spa Voucher + Poolside Dinner',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Sangai Premium Floating Villa | The Sangai Luxury City Suites | Spa Voucher + Poolside Dinner',
            )
        ],
        inclusions=[
            _inc_included('lakeside high-tea setup at sunset, away from crowds. Curated by TRAGUIN Experts: Handpicked romantic viewpoints with flexible, unhurried timings. Exclusive Recommendations: Personalized local café maps and recommendations for unique photo backdrops. Shopping & Local Experiences Local Markets & Souvenirs: Silk phanek garments, elegant bamboo decorative items, and traditional pottery at local markets. Cafes & Food: Try delicious local treats like Singju salad and sweet black rice kheer at recommended romantic spots. Instagram spots: Sendra Hills balcony views, Loktak sunset longboat rides, and Kangla moats. Premium accommodation with beautiful romantic views.', 1),
            _inc_included('Daily breakfast and specialty dinners (CPAI Plus).', 2),
            _inc_included('Private luxury sedan transport with a dedicated chauffeur.', 3),
            _inc_included('A complimentary honeymoon cake and custom floral bed decoration.', 4),
            _inc_included('An exclusive private boat cruise on Loktak Lake for the couple.', 5),
            _inc_included('A signature lakeside high-tea experience setup by our team.', 6),
            _inc_included('All applicable luxury resort taxes and venue entry fees.', 7),
            _inc_included('24/7 dedicated telephone support from TRAGUIN experts.', 8),
            _inc_included('Domestic or international airfares to and from Imphal.', 9),
            _inc_excluded('Camera entry charges or optional videography fees.', 10),
            _inc_excluded('Personal expenses (laundry, phone calls, premium bar orders).', 11),
            _inc_excluded('Optional spa treatments or unlisted sightseeing detours.', 12),
            _inc_excluded('Travel insurance coverage and medical expenses.', 13),
            _inc_excluded('Tips or gratuities for drivers and resort staff.', 14),
        ],
    )
    return package, itinerary

def build_mn_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'MN-010'
    tour_code = 'TRG-MAN-010'
    title = 'Manipur Panorama Family Luxury Tour — Imphal • Loktak • Moreh • Ukhrul'
    duration = '6 Nights / 7 Days'
    slug = 'mn-010-manipur-panorama-family-luxury-tour'
    itin_slug = 'mn-010-manipur-panorama-family-luxury-tour-itinerary'
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
            _ph('Serial code MN-010 | TRAGUIN tour code TRG-MAN-010', 1),
            _ph('State / Country: Manipur / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Imphal • Loktak • Moirang • Moreh • Ukhrul', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Premium Luxury Toyota Innova Crysta', 7),
            _ph('Route: Imphal → Loktak Lake → Moreh Border → Ukhrul Hills → Imphal TRAGUIN Premium Travel Experience • Manipur Panorama 1', 8),
            _ph('TRAGUIN Signature Experience: Private sunset boat cruise on Loktak Lake with authentic traditional', 9),
            _ph('Curated by TRAGUIN Experts: Handpicked local encounters with master artisans of the Tangkhul Naga', 10),
            _ph('Personalized Assistance: Instant messaging support and proactive day-to-day management for', 11)
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
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Manipur Panorama Family Luxury Tour',
        overview="eticulously designed **Luxury Manipur Holiday** with **TRAGUIN**, crafted exclusively for families seeking comfort, cultural enrichment, and breathtaking landscapes. This **Best Manipur Tour Package** unveils a land of vibrant traditions, pristine freshwater lakes, and untouched rolling hills. From the floating islands of Loktak to the international border of Moreh and the misty heights of Ukhrul, experience an unforgettable journey enveloped in true premium luxury. Group / FIT: Private Family FIT Vehicle: Premium Luxury Toyota Innova Crysta Meal Plan: MAPAI (Breakfast & Dinner Included) Route: Imphal → Loktak Lake → Moreh Border → Ukhrul Hills → Imphal TRAGUIN Premium Travel Experience • Manipur Panorama 1 TRAGUIN Curated Experience Note: Handpicked premium hotel stays, professional local English/Hindi- speaking escort guide, private sunset boat cruises, and traditional Manipuri royal culinary highlights.\n\nTOUR OVERVIEW\nWelcome to the jewel of Northeast India. Embark on a meticulously designed **Luxury Manipur Holiday** with **TRAGUIN**, crafted exclusively for families seeking comfort, cultural enrichment, and breathtaking landscapes. This **Best Manipur Tour Package** unveils a land of vibrant traditions, pristine freshwater lakes, and untouched rolling hills. From the floating islands of Loktak to the international border of Moreh and the misty heights of Ukhrul, experience an unforgettable journey enveloped in true premium luxury. Group / FIT: Private Family FIT Vehicle: Premium Luxury Toyota Innova Crysta Meal Plan: MAPAI (Breakfast & Dinner Included) Route: Imphal → Loktak Lake → Moreh Border → Ukhrul Hills → Imphal TRAGUIN Premium Travel Experience • Manipur Panorama 1 TRAGUIN Curated Experience Note: Handpicked premium hotel stays, professional local English/Hindi- speaking escort guide, private sunset boat cruises, and traditional Manipuri royal culinary highlights.\n\nWHY CHOOSE A PREMIUM MANIPUR EXPERIENCE?\nManipur, often referred to as the 'Switzerland of the East', offers an offbeat, highly exclusive travel experience away from conventional tourist crowds. A **Manipur Family Tour** brings you face-to-face with rich heritage, remarkable historic battlefields, and world-renowned ecological marvels. Top Tourist Places in Manipur & Most Searched Experiences: Loktak Lake: The world's only floating national park, highly rated as a top Instagram location. Kangla Fort: The historical and spiritual heart of Imphal, rich with tales of ancient royalty. Ima Keithel (Mother's Market): The largest all-women-run market in Asia, a paradise for culture and shopping highlights. Moreh Border Town: A unique cross-border commercial hub neighboring Tamu in Myanmar. Ukhrul Hills: The land of the exotic Shirui Lily, offering scenic beauty and immersive tribal experiences.",
        seo_title='MN-010 | Manipur Panorama Family Luxury Tour | TRAGUIN',
        seo_description='Premium 6 Nights / 7 Days Manipur package (MN-010 / TRG-MAN-010): Imphal • Loktak • Moirang • Moreh • Ukhrul with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN IMPHAL WELCOME TO THE JEWEL OF NORTHEAST INDIA', 1),
            _ih('Day 02: IMPHAL TO LOKTAK LAKE THE MYSTICAL FLOATING VEGETATION', 2),
            _ih('Day 03: IMPHAL TO MOREH BORDER CROSS-BORDER EXCURSION TO MYANMAR', 3),
            _ih('Day 04: IMPHAL TO UKHRUL HILLS ASCENDING TO THE MISTY MOUNTAINS', 4),
            _ih('Day 05: UKHRUL SIGHTSEEING TO IMPHAL CRAZY ROCK FORMATIONS AND RETURN', 5),
            _ih("Day 06: IMPHAL HERITAGE & CULTURE ASIA'S LARGEST ALL-WOMEN MARKET", 6),
            _ih('Day 07: DEPARTURE FROM IMPHAL CHERISHING UNFORGETTABLE MEMORIES', 7),
            _ih('TRAGUIN Signature Experience: Private sunset boat cruise on Loktak Lake with authentic traditional', 8),
            _ih('Curated by TRAGUIN Experts: Handpicked local encounters with master artisans of the Tangkhul Naga', 9),
            _ih('Personalized Assistance: Instant messaging support and proactive day-to-day management for', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN IMPHAL WELCOME TO THE JEWEL OF NORTHEAST INDIA',
                (
                    'Your highly anticipated **Premium Manipur Experience** begins the moment you touch down at Imphal International Airport. A dedicated **TRAGUIN** luxury travel consultant and chauffeur will warmly welcome your family and transfer you in a premium air-conditioned vehicle to your handpicked luxury hotel. After a seamless check-in and short relaxation, begin your **Manipur Sightseeing** journey with a visit to the sacred **Kangla Fort**, the ancient seat of Manipuri rulers, surrounded by deep moats and regal brick structures. Capture stunning family photographs at the majestic Kangla Sha statues. As the evening sets in, enjoy an intimate welcome dinner arranged by **TRAGUIN** featuring curated regional highlights.'
                ),
                [
                    'Sightseeing Included: Kangla Fort, Govindajee Temple, Imphal War Cemetery.',
                    'Evening Experience: Leisurely walks around the illuminated capital square.',
                    'Overnight Stay: Classic Luxury Hotel, Imphal.',
                    'Meals Included: Welcome Dinner.',
                ],
            ),
            _day(
                2,
                'IMPHAL TO LOKTAK LAKE THE MYSTICAL FLOATING VEGETATION',
                (
                    "Indulge in a rich breakfast before embarking on an excursion to the world-famous **Loktak Lake**, a central highlight of any **Luxury Manipur Holiday**. Marvel at the 'Phumdis'—heterogeneous masses of vegetation, soil, and organic matter forming floating islands. Head into the **Keibul Lamjao National Park**, the world's only floating national park, to catch a glimpse of the rare and endangered Sangai (Brow-antlered) dancing deer. Next, discover the historical town of **Moirang**, where the Indian National Army (INA) flag was hoisted for the first time on Indian soil. Experience an immersive private boat cruise during sunset, tailored exclusively by **TRAGUIN** for an unforgettable memory."
                ),
                [
                    'Sightseeing Included: Loktak Lake, Keibul Lamjao National Park, INA Memorial Museum.',
                    'Optional Activities: Local traditional canoe ride among the floating phumdis.',
                    'Evening Experience: Stunning lakeside sunset photography sessions.',
                    'Overnight Stay: Premium Lakeside Eco-Resort / Imphal Luxury Stay.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                3,
                'IMPHAL TO MOREH BORDER CROSS-BORDER EXCURSION TO MYANMAR',
                (
                    'FRONTIER Today, take a scenic drive through the verdant hills to **Moreh**, the bustling international border town connecting India with Myanmar. This route showcases the breathtaking landscapes of the Chandel district. Upon reaching Moreh, feel the vibrant multi-cultural energy where Indo-Myanmar trade thrives. Cross over to **Tamu** (subject to prevailing border regulations and permissions) to see the striking golden-domed Buddhist Pagodas and experience an entirely different cultural landscape. Explore local markets filled with unique cross-border trade goods, electronics, and rare souvenirs before driving back to Imphal for a restful evening.'
                ),
                [
                    'Sightseeing Included: Moreh Border Town, Indo-Myanmar Friendship Gate, Tamu Town Exploration.',
                    'Shopping: Moreh International Border Market for authentic lifestyle products.',
                    'Evening Experience: Relaxing premium high-tea upon returning to your hotel.',
                    'Overnight Stay: Classic Luxury Hotel, Imphal.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                4,
                'IMPHAL TO UKHRUL HILLS ASCENDING TO THE MISTY MOUNTAINS',
                (
                    'Bid temporary farewell to the valleys as your **TRAGUIN** luxury transport carries you high up into the refreshing, misty domain of **Ukhrul**. Famous for its stunning green valleys, pine forests, and deep tribal history, Ukhrul is the perfect destination for family leisure and serene natural beauty. Check into a handpicked premium property overlooking beautiful panoramic hill ridges. Spend the afternoon exploring the pristine surroundings and interacting with the welcoming local Tangkhul Naga community, discovering their traditional lifestyle, exceptional handloom crafts, and artistic woodworks.'
                ),
                [
                    'Sightseeing Included: Shirui Kashong Hill bases, Ukhrul Viewpoints, Local Tribal Village walks.',
                    'Optional Activities: Mild nature walking trails suitable for all family members.',
                    'Evening Experience: Cozy bonfire evening accompanied by local acoustic musical elements.',
                    'Overnight Stay: Premium Boutique Resort, Ukhrul.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                5,
                'UKHRUL SIGHTSEEING TO IMPHAL CRAZY ROCK FORMATIONS AND RETURN',
                (
                    'VALLEY JOURNEY Savor a fresh mountain breakfast amidst the clouds. Venture to the enigmatic **Khayang Peak** or explore the fascinating **Khangkhui Mangsor Cave**, an ancient natural limestone cave system that has stood for millennia. This geological marvel offers immense family fun and excellent educational stories for children. Witness spectacular valley views before beginning your smooth descent back to the capital. Re-enter Imphal in the late afternoon and enjoy premium leisure time at your luxury accommodation.'
                ),
                [
                    'Sightseeing Included: Khangkhui Cave, Hundung Local Pottery Village.',
                    'Photography Points: Panoramic vistas along the Ukhrul-Imphal highway.',
                    'Evening Experience: Leisurely evening at the luxury hotel lounge.',
                    'Overnight Stay: Classic Luxury Hotel, Imphal.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                6,
                "IMPHAL HERITAGE & CULTURE ASIA'S LARGEST ALL-WOMEN MARKET",
                (
                    'Dedicate this day to exploring the soul of the city with **TRAGUIN [Destination] Packages**. Visit the legendary **Ima Keithel** (Mother’s Market), a world-renowned landmark operated entirely by thousands of local women. It serves as an incredible showcase of woman empowerment and rich culture. Discover traditional handloom phreks, shawls, and beautiful handicraft souvenirs. Continue your journey to the **Manipur State Museum** to learn about tribal archeology, and finish your historical tour at the emotional **Red Hill (Maibam Lokpa Ching)**, a critical WWII battlefield where Allied and Japanese forces clashed.'
                ),
                [
                    'Sightseeing Included: Ima Keithel, Red Hill WWII Memorial, Manipur State Museum.',
                    'Food Suggestions: Sample traditional Manipuri black rice pudding (Chak-hao Kheer).',
                    'Evening Experience: Grand farewell dinner organized by the team.',
                    'Overnight Stay: Classic Luxury Hotel, Imphal.',
                    'Meals Included: Breakfast & Farewell Dinner.',
                ],
            ),
            _day(
                7,
                'DEPARTURE FROM IMPHAL CHERISHING UNFORGETTABLE MEMORIES',
                (
                    'Enjoy a luxurious final breakfast at your hotel. Depending on your flight schedule, indulge in some last-minute will pick you up for a comfortable transfer back to Imphal International Airport. As you board your flight home, your **Manipur Family Tour** concludes, leaving your family with beautiful, deep-seated stories and unforgettable memories curated seamlessly by **TRAGUIN**.'
                ),
                [
                    'shopping: for local organic teas, aromatic black rice, or delicate bamboo artifacts. Your premium private vehicle',
                    'Transfers Included: Private direct airport drop-off via luxury vehicle.',
                    'Meals Included: Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Classic Hotel / Similar | Shalom Lodge / Similar',
                'Imphal | Ukhrul',
                '5N Imphal|1N Ukhrul',
                'Deluxe',
                'Executive Room',
                'MAPAI',
                4,
                1,
                description='OPTION 01 – DELUXE: Classic Hotel / Similar | Shalom Lodge / Similar | MAPAI',
            ),
            _hotel(
                'The Classic Grande / Similar | The Hills Hotel / Similar',
                'Imphal | Ukhrul',
                '5N Imphal|1N Ukhrul',
                'Premium',
                'Deluxe Suite Room',
                'MAPAI',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Classic Grande / Similar | The Hills Hotel / Similar | MAPAI',
            ),
            _hotel(
                'Classic Grande - Premium Wing | Luxury Eco Retreat Ukhrul',
                'Imphal | Ukhrul',
                '5N Imphal|1N Ukhrul',
                'Luxury',
                'Club Luxury Room',
                'MAPAI',
                5,
                3,
                description='OPTION 03 – LUXURY: Classic Grande - Premium Wing | Luxury Eco Retreat Ukhrul | MAPAI',
            ),
            _hotel(
                'Hotel Imphal Radisson / Elite Villa | Bespoke Elite Highland Cabin',
                'Imphal | Ukhrul',
                '5N Imphal|1N Ukhrul',
                'Ultra Luxury',
                'Presidential / Royal Suite',
                'MAPAI',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Hotel Imphal Radisson / Elite Villa | Bespoke Elite Highland Cabin | MAPAI',
            )
        ],
        inclusions=[
            _inc_included('Handpicked luxury accommodations as selected.', 1),
            _inc_included('Daily premium buffet breakfasts and fine dining dinners.', 2),
            _inc_included('Private luxury transfers via Toyota Innova Crysta.', 3),
            _inc_included('Dedicated professional local English/Hindi guide.', 4),
            _inc_included('All state permits, border crossing clearances, and taxes.', 5),
            _inc_included('TRAGUIN 24/7 dedicated on-tour concierge support.', 6),
            _inc_included('Welcome amenities kit with authentic Manipuri organic tea.', 7),
            _inc_excluded('Airfare or train tickets to/from Imphal.', 8),
            _inc_excluded('Monument entry fees, camera fees, and local activity charges.', 9),
            _inc_excluded('Personal expenses (laundry, telephone calls, bar bills).', 10),
            _inc_excluded('Travel insurance and emergency medical expenses.', 11),
            _inc_excluded('Tips to drivers, guides, and hotel staff.', 12),
            _inc_excluded('Optional excursions or extra vehicle usage beyond plan.', 13),
        ],
    )
    return package, itinerary

MANIPUR_DOMESTIC_BUILDERS = [
    build_mn_001,
    build_mn_002,
    build_mn_003,
    build_mn_004,
    build_mn_005,
    build_mn_006,
    build_mn_007,
    build_mn_008,
    build_mn_009,
    build_mn_010,
]
