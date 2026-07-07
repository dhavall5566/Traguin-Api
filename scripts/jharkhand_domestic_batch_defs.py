"""Builder functions for JH-001 through JH-010 Jharkhand domestic packages."""

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

JHARKHAND_SLUG = "jharkhand"


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


def build_jh_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JH-001'
    tour_code = 'TRAGUIN-RANCHI-001'
    title = 'Ranchi Discovery & Luxury Jharkhand Holiday'
    duration = '04 Nights / 05 Days'
    slug = 'jh-001-ranchi-discovery-luxury-jharkhand-holiday'
    itin_slug = 'jh-001-ranchi-discovery-luxury-jharkhand-holiday-itinerary'
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
            _ph('Serial code JH-001 | TRAGUIN tour code TRAGUIN-RANCHI-001', 1),
            _ph('State / Country: Jharkhand / India | Category: Premium Family Tour', 2),
            _ph('Destinations: Ranchi • Netarhat • Patratu Valley', 3),
            _ph('Ideal for: Family Vacations & Nature Seekers', 4),
            _ph('Best season: October to March TRAGUIN CODE: TRAGUIN-RANCHI-001', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / MAPAI', 7),
            _ph('Hotel Policies: Standard check-in time is 14:00 hrs and check-out is 11:00 hrs. Early check-ins depend on room availability.', 8),
            _ph('Weather Notes: Netarhat can become considerably cool during winter evenings; carrying light woolens is highly', 9)
        ],
        moods=['Nature', 'Family', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Ranchi Discovery & Luxury Jharkhand Holiday',
        overview='WHY CHOOSE A LUXURY JHARKHAND HOLIDAY? Jharkhand is fast becoming India’s ultimate hidden gem for offbeat luxury. Travelers search extensively for the Best Time to Visit Jharkhand to catch its majestic waterfalls at peak flow and experience its famous misty hills. This region features top Instagram locations, such as the dramatic curves of Patratu Valley and the glowing sunset frames of Netarhat. Whether your family seeks the thrill of trekking around rugged hills or the cultural fulfillment of exploring tribal arts and crafts, our TRAGUIN Jharkhand Packages blend safety, comfort, and deep exploration seamlessly.\n\nTOUR OVERVIEW\nThis premium travel itinerary explores the absolute Top Tourist Places in Jharkhand. Your custom itinerary takes you from the energetic, waterfall-rich capital of Ranchi to the serene, cloud-kissed heights of Netarhat, concluding along the legendary hairpin curves of Patratu Valley. Traveling in an exclusive premium vehicle with custom-tailored meal plans, your family will enjoy unparalleled comfort, VIP sightseeing access, and authentic local cultural interactions curated exclusively by TRAGUIN. SERIAL CODE: JH-001 STATE / COUNTRY: Jharkhand / India CATEGORY: Premium Family Tour DURATION: 04 Nights / 05 Days DESTINATIONS: Ranchi • Netarhat • Patratu Valley IDEAL FOR: Family Vacations & Nature Seekers BEST SEASON: October to March TRAGUIN CODE: TRAGUIN-RANCHI-001 TRAGUIN Premium Jharkhand Tour • JH-001 WELCOME TO THE CITY OF WATERFALLS\n\nWHY CHOOSE A LUXURY JHARKHAND HOLIDAY?\nJharkhand is fast becoming India’s ultimate hidden gem for offbeat luxury. Travelers search extensively for the Best Time to Visit Jharkhand to catch its majestic waterfalls at peak flow and experience its famous misty hills. This region features top Instagram locations, such as the dramatic curves of Patratu Valley and the glowing sunset frames of Netarhat. Whether your family seeks the thrill of trekking around rugged hills or the cultural fulfillment of exploring tribal arts and crafts, our TRAGUIN Jharkhand Packages blend safety, comfort, and deep exploration seamlessly.',
        seo_title='JH-001 | Ranchi Discovery & Luxury Jharkhand Holiday | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Jharkhand package (JH-001 / TRAGUIN-RANCHI-001): Ranchi • Netarhat • Patratu Valley with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: RANCHI ARRIVAL', 1),
            _ih('Day 02: RANCHI WATERFALL SAFARI', 2),
            _ih('Day 03: RANCHI TO NETARHAT', 3),
            _ih('Day 04: NETARHAT TO RANCHI VIA PATRATU', 4),
            _ih('Day 05: DEPARTURE FROM RANCHI', 5)
        ],
        days=[
            _day(
                1,
                'RANCHI ARRIVAL',
                (
                    'Ranchi Sightseeing & Premium Arrival Experience Arrive at Ranchi Airport or Railway Station, where a dedicated TRAGUIN tour representative will extend a traditional, warm welcome. Board your premium, air-conditioned vehicle and transfer smoothly to your handpicked luxury hotel. After refreshing, start your Ranchi Sightseeing tour. Visit the serene Kanke Dam and the adjacent Rock Garden, perfectly carved out of the Gonda Hill rocks, offering beautiful sunset backdrops—an ideal spot for family photography. Conclude your evening with an optional fine dining experience featuring authentic regional tribal delicacies or premium North Indian cuisine. Stay & Meals: TRAGUIN Premium Jharkhand Tour • JH-001 THE CASCADING WONDERS OF CHOTA NAGPUR'
                ),
                [
                    'Sightseeing Included: Kanke Dam, Rock Garden, Gonda Hill Sunset Viewpoint.',
                    'Evening Experience: Leisured stroll around Kanke Dam followed by a boutique welcome dinner.',
                    'Overnight Stay: in Ranchi. Meals Included: Dinner.',
                ],
            ),
            _day(
                2,
                'RANCHI WATERFALL SAFARI',
                (
                    'Iconic Attractions & Immersive Nature Experiences Fuel up with a sumptuous breakfast at your premium stay before embarking on an exhilarating nature safari. Today you explore the crown jewels of Jharkhand’s water cascades. Drive along scenic routes bounded by dense sal forests to reach the majestic Dassam Falls, where the Kanchi River drops dramatically from a height of over 144 feet. Next, head to the iconic Jonha Falls (also known as Gautamdhara), reachable via a beautifully curated flight of steps down into a tranquil valley. TRAGUIN arranges a special packed gourmet picnic lunch by the riverside for an unforgettable family bonding experience. Return to Ranchi in the evening for premium relaxation or luxury shopping. Stay & Meals: TRAGUIN Premium Jharkhand Tour • JH-001 JOURNEY TO THE QUEEN OF CHOTA NAGPUR SUNRISE MAJESTY AND THE SERPENTINE VALLEY'
                ),
                [
                    'Sightseeing Included: Dassam Falls, Jonha Falls, Hundru Falls (optional based on time), and lush countryside scenic drives.',
                    'Evening Experience: Relaxation at hotel lounge or exploration of local handicraft boutiques for Sohrai paintings.',
                    'Overnight Stay: in Ranchi. Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                3,
                'RANCHI TO NETARHAT',
                (
                    'Breathtaking Landscapes & Hill Station Retreat After a delicious morning breakfast, checkout and begin a beautiful journey toward Netarhat, affectionately crowned the Queen of Chota Nagpur. This scenic drive curves through dense pine forests, bamboo groves, and agricultural valleys. Upon ascending the plateau, check into your curated nature resort. In the late afternoon, your TRAGUIN chauffeur takes you to the famous Magnolia Sunset Point. Listen to the poignant local folklore of Magnolia while watching the sun dip below the expansive horizon, painting the sky in deep shades of terracotta and violet. This is widely considered the most popular Instagram location in Jharkhand. Stay & Meals:'
                ),
                [
                    'Sightseeing Included: Netarhat Pine Forest, Pear Orchards, Magnolia Sunset Point.',
                    'Evening Experience: Stargazing and bonfire night under the clear skies of the Netarhat plateau.',
                    'Overnight Stay: in Netarhat. Meals Included: Breakfast, Lunch & Dinner.',
                ],
            ),
            _day(
                4,
                'NETARHAT TO RANCHI VIA PATRATU',
                (
                    'Exclusive Experiences & Majestic Hairpin Drives Wake up early for a magical sunrise at Koel Viewpoint, watching the morning mist lift gently off the Koel River flowing far below. Return to your resort for a hearty breakfast before starting your descent back to Ranchi. Your journey includes an unforgettable detour through the breathtaking Patratu Valley. Famous for its sweeping, serpentine S-curves and dramatic engineering marvels, this road overlooks the deep blue waters of the Patratu Dam reservoir. Enjoy a premium, exclusive speed boating experience on the dam, arranged completely by TRAGUIN, before checking into your luxury hotel in Ranchi for your final evening. Stay & Meals: TRAGUIN Premium Jharkhand Tour • JH-001 CHERISHING UNFORGETTABLE MEMORIES'
                ),
                [
                    'Sightseeing Included: Koel Viewpoint, Ghaghri Falls, Patratu Valley Roads, Patratu Dam Lake.',
                    'Evening Experience: Farewell family dinner celebrating your spectacular Jharkhand Honeymoon/Family Package success.',
                    'Overnight Stay: in Ranchi. Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                5,
                'DEPARTURE FROM RANCHI',
                (
                    'End of a Luxury Journey Savor your final luxury breakfast at the hotel. Spend the morning at your leisure, perhaps engaging in some last- minute souvenir shopping at Jharcraft, where you can source genuine Tussar silk, organic honey, and hand- carved bamboo artifacts. At the designated hour, transfer comfortably to the Ranchi Airport or Railway Station for your onward journey home. Your premium tour concludes with beautifully curated experiences and unforgettable memories of the wild, majestic beauty of Jharkhand, proudly delivered by TRAGUIN.'
                ),
                [
                    'Meals Included: Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Radisson / Chanakya BNR | Netarhat Nature Resort (Deluxe)',
                'Ranchi | Netarhat',
                '3N Ranchi|1N Netarhat',
                'Deluxe',
                'Executive Room | Deluxe Cottage',
                'CP (Breakfast Only)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Radisson / Chanakya BNR | Netarhat Nature Resort (Deluxe) | CP (Breakfast Only)',
            ),
            _hotel(
                'The Radisson Blu (Executive Suite) | Netarhat Heritage Cottage',
                'Ranchi | Netarhat',
                '3N Ranchi|1N Netarhat',
                'Premium',
                'Executive Suite | Premium Cottage',
                'MAPAI (Breakfast + Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Radisson Blu (Executive Suite) | Netarhat Heritage Cottage | MAPAI (Breakfast + Dinner)',
            ),
            _hotel(
                'Le Lac Luxury Resort / Radisson Blu | TRAGUIN Premium Eco Luxury Tents',
                'Ranchi | Netarhat',
                '3N Ranchi|1N Netarhat',
                'Luxury',
                'Luxury Suite | Eco Luxury Tent',
                'MAPAI (Breakfast + Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Le Lac Luxury Resort / Radisson Blu | TRAGUIN Premium Eco Luxury Tents | MAPAI (Breakfast + Dinner)',
            ),
            _hotel(
                'The Grand Radisson Luxury Suite | Exclusive Private Nature Villa',
                'Ranchi | Netarhat',
                '3N Ranchi|1N Netarhat',
                'Ultra Luxury',
                'Luxury Suite | Private Villa',
                'APAI (All Meals Included)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Grand Radisson Luxury Suite | Exclusive Private Nature Villa | APAI (All Meals Included)',
            )
        ],
        inclusions=[
            _inc_included('Luxury accommodation in handpicked premium hotels.', 1),
            _inc_included('Daily gourmet breakfast and tailored dinners.', 2),
            _inc_included('Private premium SUV for all transfers and sightseeing.', 3),
            _inc_included('Dedicated, highly experienced professional driver.', 4),
            _inc_included('All fuel, toll taxes, parking fees, and driver allowances.', 5),
            _inc_included('Exclusive TRAGUIN support throughout the tour.', 6),
            _inc_included('Complimentary VIP speed boating at Patratu Dam.', 7),
            _inc_included('Traditional welcome amenities on arrival.', 8),
            _inc_excluded('Airfare / train tickets to and from Ranchi.', 9),
            _inc_excluded('Monument and national park entrance fees.', 10),
            _inc_excluded('Personal expenses (laundry, telephone, tips).', 11),
            _inc_excluded('Optional adventure sports or activities.', 12),
            _inc_excluded('Any items or services not explicitly detailed.', 13),
            _inc_excluded('GST or regulatory government taxes.', 14),
            _inc_excluded('Travel insurance cover.', 15),
        ],
    )
    return package, itinerary

def build_jh_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JH-002'
    tour_code = 'TRAGUIN-JH-NATURE-002'
    title = 'Waterfalls of Jharkhand'
    duration = '04 Nights / 05 Days'
    slug = 'jh-002-waterfalls-of-jharkhand'
    itin_slug = 'jh-002-waterfalls-of-jharkhand-itinerary'
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
            _ph('Serial code JH-002 | TRAGUIN tour code TRAGUIN-JH-NATURE-002', 1),
            _ph('State / Country: Jharkhand / India | Category: NATURE / LUXURY', 2),
            _ph('Destinations: Ranchi • Netarhat • Betla National Park', 3),
            _ph('Ideal for: Nature Enthusiasts, Photographers, Families, Honeymooners', 4),
            _ph('Best season: October to March (Post- Monsoon for lush green waterfalls) TRAGUIN CODE: TRAGUIN-JH-', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Premium Private Luxury SUV (Innova Crysta / Equivalent) Meal Plan: MAPAI (Daily Premium Breakfast & Gourmet Dinner Included) Curated Note: Includes personalized TRAGUIN local guides, VIP entry access, and private sunset high teas. WHY BOOK THE BEST JHARKHAND TOUR PACKAGE? Jharkhand is an emerging jewel for luxury eco-tourism. Travelers searching for a Jharkhand Honeymoon Package or an immersive Jharkhand Family Tour will discover magnificent terrains away from commercial crowds. Boasting iconic attractions like the Hundru and Jonha falls, pristine sunset points in Netarhat, and', 7),
            _ph('Route: Ranchi (Arrival) → Netarhat → Betla National Park → Ranchi (Departure)', 8),
            _ph('TRAGUIN Support: 24/7 dedicated guest', 9),
            _ph('TRAGUIN Signature Experience: Private bonfire dinner under the stars at Netarhat.', 10),
            _ph('Curated by TRAGUIN Experts: Direct routes bypassing tourist bottlenecks to give uninterrupted waterfall views.', 11),
            _ph('Luxury Transportation: Chauffeurs extensively trained in highland protocols and professional guest etiquette.', 12),
            _ph("Local Markets: Firayalal Market and Jharcraft Emporium in Ranchi offer excellent organic items and traditional fabrics. Don't miss buying the legendary Sohrai & Khovar tribal arts directly supporting local women collectives. Food Recommendations: Savor authentic local delicacies like Dhooska with chana aloo curry, and fresh bamboo shoot pickles during your stay in Netarhat.", 13),
            _ph('Hotel Policies: Standard check-in time is 14:00 hrs and check-out is 11:00 hrs. Early check-in is subject to availability.', 14)
        ],
        moods=['Nature', 'Luxury', 'Family'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Waterfalls of Jharkhand',
        overview='pectacular scenic drive to the famous Patratu Valley. The sweeping hairpin turns and panoramic green vistas offer incredible photography points and a glimpse of breathtaking landscapes. Bask in a curated evening experience overlooking the Patratu Dam before returning to the city. Sightseeing Included: Patratu Valley S-Curves, Patratu Dam Overlook, Ranchi Lake Promenade. Evening Experience: Private high tea at Patratu Valley sunset point. Overnight Stay: Ranchi (Radisson Blu / Chanakya BNR Premium Luxury Stay) Meals Included: Gourmet Dinner TRAGUIN • Premium Travel & Luxury Holidays\n\nTOUR OVERVIEW\nWelcome to an extraordinary escape crafted meticulously by TRAGUIN. This exclusive premium itinerary introduces you to the raw, untouched magic of Jharkhand, famously known as the "Land of Forests". Curated by our seasoned holiday experts, this journey balances sensory luxury with wild, dramatic landscapes. Prepare to traverse winding hill roads, witness cascading monumental waterfalls, and dive deep into untamed wildlife reserves. Route: Ranchi (Arrival) → Netarhat → Betla National Park → Ranchi (Departure) Vehicle: Premium Private Luxury SUV (Innova Crysta / Equivalent) Meal Plan: MAPAI (Daily Premium Breakfast & Gourmet Dinner Included) Curated Note: Includes personalized TRAGUIN local guides, VIP entry access, and private sunset high teas.\n\nWHY BOOK THE BEST JHARKHAND TOUR PACKAGE?\nJharkhand is an emerging jewel for luxury eco-tourism. Travelers searching for a Jharkhand Honeymoon Package or an immersive Jharkhand Family Tour will discover magnificent terrains away from commercial crowds. Boasting iconic attractions like the Hundru and Jonha falls, pristine sunset points in Netarhat, and TRAGUIN • Premium Travel & Luxury Holidays rich tribal heritage, a Luxury Jharkhand Holiday guarantees a sensory rejuvenation. This specialized TRAGUIN Jharkhand Package brings you face-to-face with the top tourist places in Jharkhand while assuring exceptional comfort, handpicked premium stays, and safety throughout the expedition. Popular Instagram Locations: Patratu Valley S-Curves, Lodh Falls (Highest in the State), Netarhat Sunrise Point, and the canopy drives of Betla National Park.',
        seo_title='JH-002 | Waterfalls of Jharkhand | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Jharkhand package (JH-002 / TRAGUIN-JH-NATURE-002): Ranchi • Netarhat • Betla National Park with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: RANCHI ARRIVAL', 1),
            _ih('Day 02: RANCHI SIGHTSEEING', 2),
            _ih('Day 03: RANCHI TO NETARHAT', 3),
            _ih('Day 04: NETARHAT TO BETLA NATIONAL PARK', 4),
            _ih('Day 05: BETLA TO RANCHI', 5),
            _ih('TRAGUIN Support: 24/7 dedicated guest', 6),
            _ih('TRAGUIN Signature Experience: Private bonfire dinner under the stars at Netarhat.', 7),
            _ih('Curated by TRAGUIN Experts: Direct routes bypassing tourist bottlenecks to give uninterrupted waterfall views.', 8)
        ],
        days=[
            _day(
                1,
                'RANCHI ARRIVAL | GATEWAY TO THE LAND OF WATERFALLS & PATRATU',
                (
                    'VALLEY DRIVES Arrive at Birsa Munda Airport or Ranchi Railway Station, where your designated premium chauffeur handles your luxury vehicle transfers. Check into your premium handpicked luxury hotel in Ranchi. Post lunch, embark on a spectacular scenic drive to the famous Patratu Valley. The sweeping hairpin turns and panoramic green vistas offer incredible photography points and a glimpse of breathtaking landscapes. Bask in a curated evening experience overlooking the Patratu Dam before returning to the city. TRAGUIN • Premium Travel & Luxury Holidays'
                ),
                [
                    'Sightseeing Included: Patratu Valley S-Curves, Patratu Dam Overlook, Ranchi Lake Promenade.',
                    'Evening Experience: Private high tea at Patratu Valley sunset point.',
                    'Overnight Stay: Ranchi (Radisson Blu / Chanakya BNR Premium Luxury Stay)',
                    'Meals Included: Gourmet Dinner',
                ],
            ),
            _day(
                2,
                'RANCHI SIGHTSEEING | THE MAJESTIC HUNDRU & JONHA WATERFALLS',
                (
                    'CASCADE Indulge in a rich breakfast before plunging into the heart of Jharkhand Sightseeing. Today you visit the iconic Hundru Falls, where the Subarnarekha River plummets from a height of 320 feet, creating an awe- inspiring mist and roaring acoustic masterpiece. Continue your immersive experience to the serene Jonha Falls, also known as the Gautam Dhara, surrounded by dense tranquil forests. Climb down the curated steps to feel the refreshing mountain water spray on your skin, crafting unforgettable memories.'
                ),
                [
                    'Sightseeing Included: Hundru Waterfalls, Jonha Waterfalls, and Sita Falls (time permitting).',
                    'Optional Activities: Local tribal art demonstration (Sohrai painting) at a village center.',
                    'Overnight Stay: Ranchi (Premium Luxury Suite Stay)',
                    'Meals Included: Premium Breakfast & Luxury Dinner',
                ],
            ),
            _day(
                3,
                'RANCHI TO NETARHAT | JOURNEY TO THE QUEEN OF CHOTANAGPUR',
                (
                    'After breakfast, check out and drive towards Netarhat, a scenic hill station nestled amidst dense pine forests and pear orchards. As your premium vehicle climbs the plateau, enjoy the cool breeze and beautiful pristine woodlands. Arrive and check into your nature retreat. In the late afternoon, head to the world-famous Magnolia Sunset Point. Feel the emotional storytelling come alive as the sun dips below the verdant horizons, painting the sky in deep shades of crimson and gold. TRAGUIN • Premium Travel & Luxury Holidays'
                ),
                [
                    'Sightseeing Included: Netarhat Pine Forest, Lower Ghaghri Falls, Magnolia Point Sunset.',
                    'Evening Experience: Stargazing session in the crisp mountain air of Netarhat.',
                    'Overnight Stay: Netarhat (Premium Eco-Resort / Luxury Cottage Stay)',
                    'Meals Included: Premium Breakfast & Authentic Local Dinner',
                ],
            ),
            _day(
                4,
                'NETARHAT TO BETLA NATIONAL PARK | EXCLUSIVE WILDLIFE SAFARI &',
                (
                    'LODH FALLS Wake up early for a spectacular sunrise at the Netarhat Sunrise Point. Following breakfast, check out and drive to the magnificent Lodh Falls—the highest waterfall in Jharkhand, where water crashes down fiercely from a staggering 468 feet amidst deep jungle canopies. After this powerful experience, proceed to Betla National Park, one of India’s earliest declared tiger reserves. Check into your luxury jungle resort and embark on an exclusive evening wilderness safari to spot wild elephants, gaurs, and exotic avian species.'
                ),
                [
                    'Sightseeing Included: Lodh Waterfalls, Betla Forest Reserves, Historical Betla Fort Ruins.',
                    'Optional Activities: Private naturalist-led walk around the old 16th-century Chero Kings Fort ruins.',
                    'Overnight Stay: Betla (Luxury Jungle Lodge / Premium Safari Resort)',
                    'Meals Included: Premium Breakfast & Jungle-side Buffet Dinner',
                ],
            ),
            _day(
                5,
                'BETLA TO RANCHI | DEPARTURE WITH FOREVER MEMORIES',
                (
                    "Relish a peaceful breakfast enveloped by nature's sounds. Check out from your premium wilderness lodge and begin your return drive to Ranchi. Take a brief stopover for last-minute shopping at local artisan boutiques, purchasing authentic souvenirs such as Paitkar paintings or wooden tribal handicrafts. Transfer seamlessly to Ranchi Airport or Railway Station for your onward destination, concluding your elite Premium Jharkhand Experience organized flawlessly by TRAGUIN."
                ),
                [
                    'Sightseeing Included: En-route panoramic stops and Ranchi souvenir marketplace.',
                    'Meals Included: Premium Breakfast Only',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Green Horizon / Executive Room | Hotel Prabhat Vihar / Deluxe Room | Van Vihar Resort / Standard Deluxe',
                'Ranchi | Netarhat | Betla',
                '2N Ranchi|1N Netarhat|1N Betla',
                'Deluxe',
                'Executive Room | Deluxe Room | Standard Deluxe',
                'MAPAI',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Green Horizon / Executive Room | Hotel Prabhat Vihar / Deluxe Room | Van Vihar Resort / Standard Deluxe | MAPAI',
            ),
            _hotel(
                'Chanakya BNR Hotel / Luxury Executive | Netarhat Nature Resort / Premium Cottage | Betla Jungle Retreat / Executive Room',
                'Ranchi | Netarhat | Betla',
                '2N Ranchi|1N Netarhat|1N Betla',
                'Premium',
                'Luxury Executive | Premium Cottage | Executive Room',
                'MAPAI',
                4,
                2,
                description='OPTION 02 – PREMIUM: Chanakya BNR Hotel / Luxury Executive | Netarhat Nature Resort / Premium Cottage | Betla Jungle Retreat / Executive Room | MAPAI',
            ),
            _hotel(
                'Radisson Blu Ranchi / Deluxe Suite | TRAGUIN Handpicked Luxury Camps | The Tree House Resort / Luxury Cabin',
                'Ranchi | Netarhat | Betla',
                '2N Ranchi|1N Netarhat|1N Betla',
                'Luxury',
                'Deluxe Suite | Luxury Camp | Luxury Cabin',
                'MAPAI',
                5,
                3,
                description='OPTION 03 – LUXURY: Radisson Blu Ranchi / Deluxe Suite | TRAGUIN Handpicked Luxury Camps | The Tree House Resort / Luxury Cabin | MAPAI',
            ),
            _hotel(
                'Radisson Blu Ranchi / Executive Club Suite | VIP Elite Bungalow Netarhat | The Wilderness Safari Lodge / Presidential Suite',
                'Ranchi | Netarhat | Betla',
                '2N Ranchi|1N Netarhat|1N Betla',
                'Ultra Luxury',
                'Executive Club Suite | VIP Bungalow | Presidential Suite',
                'MAPAI',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Radisson Blu Ranchi / Executive Club Suite | VIP Elite Bungalow Netarhat | The Wilderness Safari Lodge / Presidential Suite | MAPAI',
            )
        ],
        inclusions=[
            _inc_included('properties across all locations.', 1),
            _inc_included('Gourmet Dining: Daily breakfast & lavish buffet dinners.', 2),
            _inc_included('Luxury Transfers: AC Luxury SUV for all scenic sightseeing routes.', 3),
            _inc_included('Curated Experiences: Specialized VIP Entry and sunset high teas.', 4),
            _inc_included('Welcome Amenities: Non-alcoholic signature refreshing arrival drinks.', 5),
            _inc_included('Taxes: All applicable luxury hospitality taxes and toll charges.', 6),
            _inc_included('Flights / Rail: International or domestic tickets to Ranchi.', 7),
            _inc_included('Curated by TRAGUIN Experts: Direct routes bypassing tourist bottlenecks to give uninterrupted waterfall views.', 8),
            _inc_included('Luxury Transportation: Chauffeurs extensively trained in highland protocols and professional guest etiquette.', 9),
            _inc_included('Personalized Touches: Complimentary local fruit baskets and artisanal snacks refilled daily in your vehicle.', 10),
            _inc_excluded('Monuments Tickets: Camera fees or local monument entries.', 11),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, premium alcoholic drinks.', 12),
            _inc_excluded('Optional Safari: Extra jungle safaris or independent treks.', 13),
            _inc_excluded('Insurance: Personal travel and medical insurance coverage.', 14),
            _inc_excluded('Driver Gratuities: Tips for local guides or premium chauffeurs.', 15),
        ],
    )
    return package, itinerary

def build_jh_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JH-003'
    tour_code = 'TRAGUIN-JH-BAIDYANATH-04D'
    title = 'Baidyanath Dham Spiritual Exploration'
    duration = '03 Nights / 04 Days'
    slug = 'jh-003-baidyanath-dham-spiritual-exploration'
    itin_slug = 'jh-003-baidyanath-dham-spiritual-exploration-itinerary'
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
            _ph('Serial code JH-003 | TRAGUIN tour code TRAGUIN-JH-BAIDYANATH-04D', 1),
            _ph('State / Country: Jharkhand / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Jharkhand', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Premium Air-Conditioned Chauffeur-Driven Luxury Sedan / SUV assigned exclusively for your party. Meal Plan: Daily premium vegetarian breakfast and specially curated satvik multi-course dinners.', 7),
            _ph('& TRAVEL POLICIES', 8),
            _ph('Hotel Policies: Standard check-in time is 14:00 hours, and check-out is 11:00 hours. Early check-ins are', 9)
        ],
        moods=['Spiritual', 'Family', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Baidyanath Dham Spiritual Exploration',
        overview="Baidyanath Dham • Basukinath Dham • Deoghar Spiritual Exploration SERIAL CODE JH-003 STATE / COUNTRY Jharkhand / India CATEGORY Premium Pilgrimage & Luxury Spiritual Tour DURATION 03 Nights / 04 Days DESTINATIONS COVERED Deoghar • Baidyanath Dham • Basukinath Dham IDEAL FOR Families, Devotees, Senior Citizens, Spiritual Seekers BEST SEASON October to March (Plus Shravan Month for Holy Yatras) STARTING PRICE On Request (Premium Curated Pricing) TRAGUIN TOUR CODE TRAGUIN-JH- BAIDYANATH-04D MEAL PLAN MAPAI (Premium Breakfast & Dinner) Embark on a sacred journey of transformation and spiritual awakening with the Best Jharkhand Tour Package custom-crafted for discerning travelers. Experience the divine aura of Baba Baidyanath Dham, one of the revered twelve Jyotirlingas, where timeless rituals, immersive experiences, and heartfelt hospitality converge seamlessly. Let TRAGUIN elevate your pilgrimage into an unforgettable, stress-free luxury experience. TRAGUIN Premium Holidays • Baidyanath Dham\n\nTOUR OVERVIEW\nOur meticulously designed Jharkhand Family Tour is optimized to offer complete physical comfort alongside profound spiritual enrichment. From the moment you arrive, every logistical detail is expertly coordinated to bypass the traditional hassles of spiritual travel sites. Route Covered: Ranchi / Deoghar Airport Arrival → Baba Baidyanath Temple → Naulakha Mandir → Tapovan Caves → Basukinath Dham → Departure Vehicle: Premium Air-Conditioned Chauffeur-Driven Luxury Sedan / SUV assigned exclusively for your party. Meal Plan: Daily premium vegetarian breakfast and specially curated satvik multi-course dinners. TRAGUIN Curated Experience: VIP assisted temple entries, expert local pandit guidance for holy rituals, and 24/7 dedicated remote concierge support to manage on-ground adjustments instantly.\n\nWHY CHOOSE THE PREMIUM JHARKHAND EXPERIENCE?\nJharkhand, famously known as the 'Land of Forests,' holds deep spiritual importance on the global tourism map, primarily centered around the timeless holy township of Deoghar. The Baidyanath Dham Tour represents an ultimate spiritual quest for millions of devotees globally, blending deep mythological heritage with breathtaking landscapes and ancient architectures. Choosing a Luxury Jharkhand Holiday ensures that your family experiences the profound, mystical energy of the holy shrines without the exhausting crowds. Deoghar features heavily on lists of popular Instagram locations for its scenic sunrise over the Trikut Hills and the geometric brilliance of the ancient temple multi- spires. Whether you seek the adventure of exploring prehistoric rock formations at Tapovan Caves, shopping for pristine local silk and hand-made Peda sweets, or fully absorbing the rich Santhal cultural highlights, this TRAGUIN Jharkhand Package strikes the perfect equilibrium of luxury, convenience, and absolute divinity.",
        seo_title='JH-003 | Baidyanath Dham Spiritual Exploration | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Jharkhand package (JH-003 / TRAGUIN-JH-BAIDYANATH-04D): Jharkhand with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DEOGHAR & INTRODUCTION TO THE HOLY LAND', 1),
            _ih('Day 02: SACRED DARSHAN AT BABA BAIDYANATH DHAM JYOTIRLINGA', 2),
            _ih('Day 03: PILGRIMAGE TO BASUKINATH DHAM – THE COURT OF SHIVA', 3),
            _ih('Day 04: SPIRITUAL SOUVENIRS & DESTINATION DEPARTURE', 4)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DEOGHAR & INTRODUCTION TO THE HOLY LAND',
                (
                    'Welcome to Deoghar, the true spiritual heart of Eastern India. Upon your arrival at Deoghar Airport or Jasidih Railway Station, you will be warmly greeted by our professional chauffeur and an executive representative carrying your personalized TRAGUIN welcome kit. Enjoy a smooth and comfortable transfer in your private luxury vehicle to your handpicked premium hotel. TRAGUIN Premium Holidays • Baidyanath Dham After a seamless check-in and quick refreshments, begin your exploration with the famous Top Tourist Places in Deoghar. Visit the exquisite Naulakha Mandir, a stunning 146-feet-high temple architectural marvel dedicated to Radha-Krishna, built through a royal donation of nine lakh rupees. Later, journey to the serene Tapovan Caves, a scenic group of rock structures where Sage Valmiki historically performed penance. Capture memorable photography points against the setting sun before returning to your premium resort.'
                ),
                [
                    'Sightseeing Included: Naulakha Mandir, Tapovan Caves, and Local Heritage Walk.',
                    'Evening Experience: Relaxing traditional tea tasting and spiritual orientation session.',
                    'Overnight Stay: Deoghar (Premium Handpicked Luxury Hotel)',
                    'Meals Included: Welcome Drink & Gourmet Dinner',
                ],
            ),
            _day(
                2,
                'SACRED DARSHAN AT BABA BAIDYANATH DHAM JYOTIRLINGA',
                (
                    'The hallmark day of your Baidyanath Dham Tour begins early with a purifying morning. Enjoy an exclusive VIP assisted entry into the main sanctum sanctorum of the Baba Baidyanath Temple, one of the unique twelve Jyotirlingas where the heart of Shiva rests. Guided by our expert certified local priest, participate in the holy Abhishek or special Shodashopachara Puja rituals, absorbing the intense spiritual vibration and creating unforgettable memories of deep faith. Marvel at the sacred red threads connecting the domes of Shiva and Shakti temples, symbolizing the cosmic union. After a peaceful spiritual immersion, return to your premium hotel for a grand traditional breakfast. In the afternoon, explore the local markets for authenticated souvenirs and traditional copper vessels. As twilight descends, enjoy the mystical evening Shringar Aarti, watching the temple glow with thousands of traditional oil lamps—a highlight of your Premium Deoghar Experience.'
                ),
                [
                    'Sightseeing Included: Baba Baidyanath Main Temple Complex, Shivganga Holy Tank, and Mansarovar.',
                    'Optional Activities: Dedicated personal Sankalp Puja arrangement for family wellness.',
                    'Evening Experience: Witnessing the historic grand Shringar Aarti from an exclusive vantage point.',
                    'Overnight Stay: Deoghar (Premium Handpicked Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Specially Curated Satvik Dinner',
                ],
            ),
            _day(
                3,
                'PILGRIMAGE TO BASUKINATH DHAM – THE COURT OF SHIVA',
                (
                    'Following a hearty breakfast, embark on a picturesque road journey towards Basukinath Dham, located approximately 45 kilometers from Deoghar. Known natively as the majestic "Court of Baba Bhole Nath," it is widely believed that a pilgrimage to Baidyanath Dham is fulfilled only after paying respect at Basukinath. Enjoy the breathtaking landscapes and scenic rural life of Jharkhand along the smooth highway. At Basukinath, experience an immersive and peaceful Darshan. The energy here is uniquely joyful, with traditional singers rendering holy chants. After receiving blessings, return to Deoghar in the late afternoon. TRAGUIN Premium Holidays • Baidyanath Dham Stop at popular scenic spots for panoramic photography, and visit the Rama Krishna Mission Vidyapith campus to experience its serene environment and local educational culture. Conclude your day with a signature dining experience arranged especially for you.'
                ),
                [
                    'Sightseeing Included: Basukinath Dham Temple Complex, Ramakrishna Mission Campus.',
                    'Optional Activities: Interaction with local Vedic scholars regarding regional history.',
                    'Evening Experience: Festive multi-course farewell dinner at the resort.',
                    'Overnight Stay: Deoghar (Premium Handpicked Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Multi-cuisine Gourmet Dinner',
                ],
            ),
            _day(
                4,
                'SPIRITUAL SOUVENIRS & DESTINATION DEPARTURE',
                (
                    "Awake to a peaceful morning and savor a final premium breakfast at your luxury resort. Use the morning hours for last-minute visits to iconic attractions or a casual stroll through local traditional markets to purchase Deoghar's legendary fresh Peda sweets, beautiful handwoven Tusser silk sarees, and local terracotta handicrafts to take back home. Pack your belongings along with an abundance of divine energy and unforgettable blessings. Your private luxury vehicle will transfer you seamlessly back to Deoghar Airport or Jasidih Railway Station for your onward journey. Your majestic Jharkhand Pilgrimage Tour concludes, leaving you with renewed inner peace, expertly managed by TRAGUIN. TRAGUIN Premium Holidays • Baidyanath Dham"
                ),
                [
                    'Sightseeing Included: Local Artisan Markets & Souvenir Emporiums.',
                    'Meals Included: Premium Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Stoneberry / Imperial Heights',
                'Deoghar',
                '03 Nights',
                'Deluxe',
                'Executive Room',
                'MAPAI Plan',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Stoneberry / Imperial Heights (Executive Room) | MAPAI Plan | 03 Nights Stay',
            ),
            _hotel(
                'Hotel Baidyanath / Amrapali Executive',
                'Deoghar',
                '03 Nights',
                'Premium',
                'Club Premium Room',
                'MAPAI Plan',
                4,
                2,
                description='OPTION 02 – PREMIUM: Hotel Baidyanath / Amrapali Executive (Club Premium Room) | MAPAI Plan | 03 Nights Stay',
            ),
            _hotel(
                'The Baidyanath Eco Resort / Luxury Suites',
                'Deoghar',
                '03 Nights',
                'Luxury',
                'Royal Suite',
                'MAPAI Plan',
                5,
                3,
                description='OPTION 03 – LUXURY: The Baidyanath Eco Resort / Luxury Suites (Royal Suite) | MAPAI Plan | 03 Nights Stay',
            ),
            _hotel(
                'TRAGUIN Private Villa Collection / Elite Boutique Resort',
                'Deoghar',
                '03 Nights',
                'Ultra Luxury',
                'Presidential Villa',
                'MAPAI Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Private Villa Collection / Elite Boutique Resort (Presidential Villa) | MAPAI Plan | 03 Nights Stay',
            )
        ],
        inclusions=[
            _inc_included('Meals: Daily premium buffet breakfasts and multi-course dinners as outlined in the itinerary text.', 1),
            _inc_included('Transfers & Sightseeing: All point-to-point travel using a private, air-conditioned luxury vehicle.', 2),
            _inc_included('Assistance: Personalized VIP greeting on arrival and departure at stations/airports.', 3),
            _inc_included('Taxes: All current applicable Goods and Services Tax (GST), toll taxes, driver allowances, and fuel surcharges.', 4),
            _inc_included('Welcome Amenities: Personalized welcome kit, refreshing welcome non-alcoholic drinks, and traditional stoles.', 5),
            _inc_included('Complimentary Experiences: Specially assigned, verified local Pandit guidance at Baidyanath Temple for streamlined darshans.', 6),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest relations manager available via call and WhatsApp during the tour.', 7),
            _inc_included('Flights / Rail: Any domestic or international airfare, train tickets, or inter-state transit permits.', 8),
            _inc_excluded('Accommodation: 03 Nights premium stay at the handpicked luxury hotel option of your choice.', 9),
            _inc_excluded('Entry Tickets: Individual camera fees, special entry counter tickets, or optional inner-sanctum offering items.', 10),
            _inc_excluded('Personal Expenses: Laundry service, telephone charges, extra minibar usage, and gratuities for staff.', 11),
        ],
    )
    return package, itinerary

def build_jh_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JH-004'
    tour_code = 'TRG-JH-2026-004'
    title = 'Netarhat Escape & Chotanagpur Wonders'
    duration = '04 Nights / 05 Days'
    slug = 'jh-004-netarhat-escape-chotanagpur-wonders'
    itin_slug = 'jh-004-netarhat-escape-chotanagpur-wonders-itinerary'
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
            _ph('Serial code JH-004 | TRAGUIN tour code TRG-JH-2026-004', 1),
            _ph('State / Country: Jharkhand / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Jharkhand', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / MAPAI', 7),
            _ph('TRAGUIN Signature Experience: Private colonial-themed tea service organized beautifully at Magnolia', 8),
            _ph('Curated by TRAGUIN Experts: Perfect route management avoiding rugged paths, keeping your elderly', 9),
            _ph('Personalized Assistance: Dedicated concierge desk tracking your journey live every 50 kilometers for', 10),
            _ph('Premium Handpicked Hotels: Strict inspection protocols ensuring clean linens, immaculate washrooms,', 11)
        ],
        moods=['Nature', 'Family', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Netarhat Escape & Chotanagpur Wonders',
        overview="Jharkhand, literally translating to the 'Land of Forests', is rapidly gaining elite status among the most searched tourism keywords for its pristine, crowd-free environments and incredible eco-tourism potential. A Premium Jharkhand Experience delivers more than standard sightseeing; it promises an emotional rendezvous with pure nature. Famous Attractions & Hidden Gems: Explore the legendary Netarhat Pine Forest, the cascading Hundru and Jonha falls, Lodh Falls (the highest waterfall in the state), and the spellbinding hairpin curves of Patratu Valley. Most Searched Experiences: Revel in the spectacular sunset from Magnolia Point, walk through dense pear orchards, and capture magnificent mist-covered horizons. Best Honeymoon & Family Points: Perfect for bonding over peaceful nature trails, historical exploration, and enjoying cozy evenings around a private luxury bonfire. Popular Instagram Locations: The panoramic serpentine roads of Patratu Valley, the hauntingly beautiful symmetrical canopies of the Pine Forests, and the dramatic vertical drop of Dasham Falls. Culture & Gastronomy Highlights: Immerse your senses in local Sohrai painting demonstrations and savor authentic, hygienically prepared local delicacies alongside contemporary multi-cuisine dining. TRAGUIN Premium Travel & Luxury Holidays\n\nTOUR OVERVIEW\nYour highly exclusive Luxury Jharkhand Holiday begins in the capital city of Ranchi, ascending gradually through the breathtaking curves of the Patratu Valley up to the pine-scented highlands of Netarhat. This customized, client- facing FIT itinerary guarantees seamless logistics, handpicked accommodations, a dedicated premium SUV, and an elegant modified American meal plan (MAPAI) ensuring a tension-free family retreat. TRAGUIN Curated Experience Note: Every element of this itinerary has been vetted by our destination connoisseurs. From securing the best vantage points for the legendary Netarhat sunrise to arranging local Tribal-infused premium dinners, your family’s safety, absolute comfort, and immersive enlightenment are perfectly engineered by TRAGUIN. TRAGUIN Premium Travel & Luxury Holidays WHY EXPERIENCE JHARKHAND WITH TRAGUIN Jharkhand, literally translating to the 'Land of Forests', is rapidly gaining elite status among the most searched tourism keywords for its pristine, crowd-free environments and incredible eco-tourism potential. A Premium Jharkhand Experience delivers more than standard sightseeing; it promises an emotional rendezvous with pure nature. Famous Attractions & Hidden Gems: Explore the legendary Netarhat Pine Forest, the cascading Hundru and Jonha falls, Lodh Falls (the highest waterfall in the state), and the spellbinding hairpin curves of Patratu Valley. Most Searched Experiences: Revel in the spectacular sunset from Magnolia Point, walk through dense pear orchards, and capture magnificent mist-covered horizons. Best Honeymoon & Family Points: Perfect for bonding over peaceful nature trails, historical exploration, and enjoying cozy evenings around a private luxury bonfire. Popular Instagram Locations: The panoramic serpentine roads of Patratu Valley, the hauntingly beautiful symmetrical canopies of the Pine Forests, and the dramatic vertical drop of Dasham Falls. Culture & Gastronomy Highlights: Immerse your senses in local Sohrai painting demonstrations and savor authentic, hygienically prepared local delicacies alongside contemporary multi-cuisine dining. TRAGUIN Premium Travel & Luxury Holidays",
        seo_title='JH-004 | Netarhat Escape & Chotanagpur Wonders | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Jharkhand package (JH-004 / TRG-JH-2026-004): Jharkhand with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: RANCHI ARRIVAL & PATRATU VALLEY EXCURSION', 1),
            _ih('Day 02: RANCHI TO NETARHAT (THE QUEEN OF CHOTANAGPUR)', 2),
            _ih('Day 03: NETARHAT DEEP EXPLORATION & WATERFALLS', 3),
            _ih('Day 04: NETARHAT TO RANCHI & CAPITAL SIGHTSEEING', 4),
            _ih('Day 05: RANCHI CITY TOUR & DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private colonial-themed tea service organized beautifully at Magnolia', 6),
            _ih('Curated by TRAGUIN Experts: Perfect route management avoiding rugged paths, keeping your elderly', 7),
            _ih('Personalized Assistance: Dedicated concierge desk tracking your journey live every 50 kilometers for', 8)
        ],
        days=[
            _day(
                1,
                'RANCHI ARRIVAL & PATRATU VALLEY EXCURSION',
                (
                    'WELCOME TO THE LAND OF WATERFALLS AND VERDANT VALLEYS Upon your arrival at Birsa Munda Airport or Ranchi Railway Station, you will be warmly received by our professional chauffeur with a personalized TRAGUIN welcome placard. Transfer smoothly in your premium private SUV to your handpicked luxury hotel in Ranchi. After checking in and enjoying a brief refreshment, begin your premium Jharkhand Sightseeing. In the afternoon, embark on an unforgettable drive to the iconic Patratu Valley. As your luxury vehicle negotiates the flawlessly engineered serpentine hairpin bends, treat your eyes to breathtaking landscapes of lush green hills meeting the expansive blue waters of the Patratu Dam. This is universally recognized as one of the top tourist places in Jharkhand and a sensational photography hotspot. Enjoy an exclusive, peaceful boat ride on the dam as the golden hour sets in, painting the sky in deep shades of amber. Sightseeing Included Patratu Valley, Patratu Dam & Lake Waterfront, Ranchi Lake. TRAGUIN Premium Travel & Luxury Holidays'
                ),
                [
                    'Optional Activities: Speed boating at Patratu Dam; local handloom shopping in Ranchi.',
                    'Evening Experience: A curated high-tea experience overlooking the valleys or lakes.',
                    'Overnight Stay: Ranchi (Handpicked Premium / Luxury Hotel)',
                    'Meals Included: Dinner (Premium Multi-Cuisine Layout)',
                ],
            ),
            _day(
                2,
                'RANCHI TO NETARHAT (THE QUEEN OF CHOTANAGPUR)',
                (
                    "JOURNEY INTO THE MYSTICAL HIGHLANDS AND PINE FORESTS Savor a sumptuous breakfast at your hotel before embarking on a beautiful road journey toward Netarhat, affectionately crowned the 'Queen of Chotanagpur'. This scenic route takes you past sleepy tribal hamlets, cascading streams, and vast fields of agricultural beauty, climbing steadily to an elevation of nearly 3,600 feet above sea level. The air grows noticeably crisper and scent-heavy with pine needles as you approach this hill station. Upon arrival, check into your boutique resort carefully selected to guarantee ultimate tranquility for your family. In the afternoon, take a serene, hand-in-hand walk through the majestic, towering Netarhat Pine Forest—an immersive experience that feels straight out of a classic fairy tale. As evening approaches, drive to the world- renowned Magnolia Sunset Point. Here, indulge in emotional storytelling as you watch the sun melt elegantly into the endless abyss of the valley below, a legendary view that has captured the hearts of global travelers for generations. Sightseeing Included Netarhat Pine Forest, Magnolia Point Sunset, Netarhat Public School Campus (External view). TRAGUIN Premium Travel & Luxury Holidays"
                ),
                [
                    'Optional Activities: Interaction with local artisans; short nature trail trekking.',
                    'Evening Experience: Sunset colonial-style tea service at Magnolia Point.',
                    'Overnight Stay: Netarhat (Best Available Premium Eco-Resort)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'NETARHAT DEEP EXPLORATION & WATERFALLS',
                (
                    "WITNESSING NATURE'S MAJESTY AT LODH AND SADNI FALLS Wake up early to catch a breathtaking phenomenon—the spectacular Sunrise over the hills from the Netarhat Sunrise Point, right as the morning mist gracefully uncovers the deep valleys. Return to your resort for a hearty, traditional breakfast before setting off on a full-day excursion deep into the natural core of Jharkhand's wilderness. Today, your premium vehicle takes you to the thunderous Lodh Falls, the highest waterfall in Jharkhand, where the Burha River plunges dramatically down a 469-foot cliff surrounded by ancient forest canopies. The sight and echoing sound of this natural marvel offer an unforgettable memory. Later, visit the unique, snake- like layout of Sadni Falls and enjoy a private, elegantly packed gourmet picnic lunch arranged amidst pristine settings. Return to Netarhat in the late afternoon to explore the fragrant local Pear Orchards and the peaceful local markets. Sightseeing Included Netarhat Sunrise Point, Lodh Falls, Sadni Falls, Local Pear Orchards. TRAGUIN Premium Travel & Luxury Holidays"
                ),
                [
                    'Optional Activities: Photography walk guided by your professional chauffeur.',
                    'Evening Experience: A private, cozy family bonfire at the resort under a star-lit sky.',
                    'Overnight Stay: Netarhat (Best Available Premium Eco-Resort)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'NETARHAT TO RANCHI & CAPITAL SIGHTSEEING',
                (
                    'CASCADING MAJESTY AND PANORAMIC URBAN VISTAS Enjoy a leisurely morning breakfast amidst the chirping of exotic birds before checking out of your Netarhat paradise. Board your comfortable SUV for a smooth descent back to Ranchi. En route, the itinerary shifts to exploring the grand water-sculpted geography of Ranchi’s periphery. Visit the spectacular Hundru Falls, where the Subarnarekha River tumbles down 322 feet over spectacular rock formations, creating a fine mist that creates brilliant rainbows on sunny days. Following this, explore Jonha Falls, also known as the Gautamdhara, where you can descend the structural steps to witness the gentle stream up close. Arrive back in Ranchi by late afternoon and check into your luxury hotel. Spend your final evening visiting the beautiful Rock Garden or enjoying premium shopping for authentic Jharkhand handicrafts. Sightseeing Included Hundru Falls, Jonha Falls / Gautamdhara, Ranchi Rock Garden. TRAGUIN Premium Travel & Luxury Holidays'
                ),
                [
                    'Optional Activities: Experiencing authentic tribal food concepts at a luxury venue.',
                    'Evening Experience: Souvenir and luxury handloom shopping at Jharcraft outlets.',
                    'Overnight Stay: Ranchi (Handpicked Premium / Luxury Hotel)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'RANCHI CITY TOUR & DEPARTURE',
                (
                    "CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Begin your final day with an exquisite breakfast spread. Depending on your flight or train schedule, set out for a brief cultural orientation tour of Ranchi city. Visit the revered Pahari Mandir, perched on a hill offering a phenomenal 360-degree panoramic view of the entire capital city, or pay respects at the serene Jagannath Temple, built in 1691 with architecture reminiscent of Puri's iconic shrine. Conclude your luxury holiday with a collection of unforgettable memories and freshly rejuvenated spirits. Your chauffeured vehicle will escort you perfectly to Birsa Munda Airport or Ranchi Railway Station for your journey home. Your premium, magical journey with TRAGUIN concludes here, leaving you with stories to pass down through generations. Sightseeing Included Pahari Mandir, Jagannath Temple, local artisanal craft hubs."
                ),
                [
                    'Optional Activities: Last-minute purchase of local organic products (honey, wood crafts).',
                    'Evening Experience: N/A - Departure departure transfer.',
                    'Overnight Stay: Departure',
                    'Meals Included: Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Green Horizon / Equivalent | Hotel Prabhat Vihar (Standard)',
                'Ranchi | Netarhat',
                '2N Ranchi|2N Netarhat',
                'Deluxe',
                'Standard Room | Standard Cottage',
                'Breakfast & Dinner (MAPAI)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Green Horizon / Equivalent | Hotel Prabhat Vihar (Standard) | Breakfast & Dinner (MAPAI)',
            ),
            _hotel(
                'Hotel BNR Chanakya / Capitol Hill | Nature Eco Resort Netarhat (Premium)',
                'Ranchi | Netarhat',
                '2N Ranchi|2N Netarhat',
                'Premium',
                'Premium Room | Premium Cottage',
                'Breakfast & Dinner (MAPAI)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Hotel BNR Chanakya / Capitol Hill | Nature Eco Resort Netarhat (Premium) | Breakfast & Dinner (MAPAI)',
            ),
            _hotel(
                'Radisson Blu Ranchi / Le Lac Luxury | Luxury Heritage Cottage Netarhat',
                'Ranchi | Netarhat',
                '2N Ranchi|2N Netarhat',
                'Luxury',
                'Luxury Suite | Heritage Cottage',
                'Gourmet Breakfast & Dinner',
                5,
                3,
                description='OPTION 03 – LUXURY: Radisson Blu Ranchi / Le Lac Luxury | Luxury Heritage Cottage Netarhat | Gourmet Breakfast & Dinner',
            ),
            _hotel(
                'The Chanakya BNR Heritage Suite / Radisson Executive | TRAGUIN Private Luxury Camp / Signature Villa',
                'Ranchi | Netarhat',
                '2N Ranchi|2N Netarhat',
                'Ultra Luxury',
                'Heritage Suite | Signature Villa',
                'Custom Elite Chef-Curated Meals',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Chanakya BNR Heritage Suite / Radisson Executive | TRAGUIN Private Luxury Camp / Signature Villa | Custom Elite Chef-Curated Meals',
            )
        ],
        inclusions=[
            _inc_included('Premium accommodation: 04 nights stay in handpicked, highly rated luxury hotels and properties.', 1),
            _inc_included('Curated meals: daily breakfast and dinners as structured in the itinerary hotel panel.', 2),
            _inc_included('Luxury transfers: dedicated air-conditioned SUV (Innova Crysta) for all transit and sightseeing.', 3),
            _inc_included('TRAGUIN support: 24/7 dedicated remote guest assistance and emergency support line.', 4),
            _inc_included('Welcome amenities: personalized arrival kit, organic immunity boosters, and refreshing wet wipes.', 5),
            _inc_included('Chauffeur excellence: highly professional, verified local driver fully knowledgeable of hilly terrains.', 6),
            _inc_included('All tolls & taxes: fuel, driver allowance, parking fees, and interstate government taxes.', 7),
            _inc_excluded('Airfare / train tickets: any incoming or outgoing flights or rail expenses to Ranchi.', 8),
            _inc_excluded('Entry tickets: camera fees, monument entry tickets, and local guide charges.', 9),
            _inc_excluded('Personal expenses: laundry, telephone calls, mini-bar items, and tips or gratuities.', 10),
            _inc_excluded('Optional activities: speedboat rides, adventure sports, or extra sightseeing deviations.', 11),
            _inc_excluded('Insurance: travel insurance premium protection plans.', 12),
            _inc_excluded('Unforeseen expenses: costs arising due to natural disasters, landslides, or political blockades.', 13),
        ],
    )
    return package, itinerary

def build_jh_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JH-005'
    tour_code = 'TRG-JH-2026-005'
    title = 'Ranchi • Netarhat • Betla National Park — Senior Leisure Tour'
    duration = '05 Nights / 06 Days'
    slug = 'jh-005-ranchi-netarhat-betla-senior-leisure'
    itin_slug = 'jh-005-ranchi-netarhat-betla-senior-leisure-itinerary'
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
            _ph('Serial code JH-005 | TRAGUIN tour code TRG-JH-2026-005', 1),
            _ph('State / Country: Jharkhand / India | Category: Senior Citizen / Leisure Tour', 2),
            _ph('Destinations: Ranchi, Netarhat, Betla', 3),
            _ph('Ideal for: Senior Citizens & Families', 4),
            _ph('Best season: October to March (Pleasant)', 5),
            _ph('Starting price: On Request (Premium Scale)', 6),
            _ph('Vehicle / Meals: Premium Toyota Innova Crysta', 7),
            _ph('Route: Ranchi → Netarhat → Betla → Ranchi', 8),
            _ph('TRAGUIN Signature Experience: Private storytelling narration detailing historical lore, making', 9),
            _ph('Curated by TRAGUIN Experts: Route mapping strictly structured to keep single-stretch driving', 10),
            _ph('Personalized Assistance: Hands-on assistance across check-ins, porterage coordination, and', 11),
            _ph('Premium Handpicked Hotels: Every single property has been physically inspected to meet strict', 12),
            _ph('Jharkhand possesses an extraordinary repository of beautiful tribal handicrafts. During your leisurely transit days, our expert chauffeur will guide you safely to government-authorized retail centers to purchase genuine Souvenirs like magnificent Paitkar Paintings, handmade bamboo baskets, and organic forest honey. Enjoy fresh herbal tea blends at the peaceful cafes overlooking Patratu Dam, capturing the perfect Instagram spots without compromising on absolute peace and luxury.', 13),
            _ph('Hotel Policies: Standard check-in time starts at 12:00 PM and check-out is fixed at 11:00 AM. Early', 14)
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
        price_note='On Request (Premium Scale)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Ranchi',
        overview='ight, effortless afternoon tour of the iconic Ranchi Lake and the beautifully sculpted Swami Vivekananda Statue standing proudly amidst the TRAGUIN • Premium Travel & Luxury Holidays water. Designed keeping senior mobility in mind, you can appreciate the stunning city views with comfortable seating layouts. Spend your evening soaking in the spiritual tranquility of the Jagannath Temple, a 17th-century architectural marvel. Witness the soothing evening Aarti that fills the atmosphere with divine energy and unparalleled peace. Sightseeing Included: Ranchi Lake, Swami Vivekananda Island, Historic Jagannath Temple. Evening Experience: Divine Soulful Evening Aarti at Jagannath Temple with priority senior seating. Optional Activities: Mild shopping for organic tribal Tussar Silk shawls. Overnight Stay: Ranchi (Premium / Luxury Category Hotel) Meals Included: Lunch & Dinner (Curated Low-Spice Dietary Meal)\n\nTOUR OVERVIEW\nThis Luxury Jharkhand Holiday offers a perfectly balanced blend of spiritual rejuvenation, colonial-era nostalgia, and pristine natural beauty. Crafted with an easy-going pace, short driving distances, and premium accessible transport, it ensures zero strain for elderly travelers. Our journey begins in the "City of Waterfalls" Ranchi, escalates to the tranquil mist-laden queen of hills Netarhat, and explores the royal woodland heritage of Betla National Park. Every single detail is overseen by our dedicated TRAGUIN local concierge team to assure safety, exquisite dining options, and premium comfort. TRAVEL PACE: Relaxed & Leisurely MEAL PLAN: APA (Breakfast, Lunch & Dinner) TRAGUIN • Premium Travel & Luxury Holidays VEHICLE: Premium Toyota Innova Crysta ROUTE: Ranchi → Netarhat → Betla → Ranchi TRAGUIN CURATED NOTE: Includes specialized senior-friendly ground assistance, certified soft-spoken chauffeurs, and handpicked accessible properties. DISCOVER THE MAGIC OF JHARKHAND\n\nWhy Visit Jharkhand? Often referred to as "The Land of Forests," Jharkhand is an unexplored paradise\nfeaturing dense sal reserves, majestic cascading waterfalls, historical Jain/Buddhist pilgrimage sites, and serene hill stations. This makes a Jharkhand Honeymoon Package or an elegant multigenerational family holiday highly rewarding for those seeking offbeat luxury and untamed natural symmetry. Famous Attractions & Most Searched Experiences: Travelers across the country frequently look for the Top Tourist Places in Jharkhand such as the sacred Hundru and Jonha Waterfalls, the historical Patratu Valley, the sunset points of Netarhat, and the royal wildlife corridors of Betla. Our comprehensive Jharkhand Sightseeing itinerary brings you face-to-face with these marvelous landmarks without requiring arduous treks or physically demanding climbs. Culture, Cuisine & Photography Highlights: Capture the breathtaking, sweeping green hairpin loops of Patratu Valley, perfectly optimized for senior photography enthusiasts with zero walking requirements. Savor the authentic, mild, and highly nutritious local flavors like Dhuska and refreshing herbal infusions under the pristine supervision of TRAGUIN dining partners. 💡 High Ranking Search Insights & Best Time to Visit Jharkhand The Best Time to Visit Jharkhand spans from October to March when the climate transitions into a crisp, cool breeze, rendering outdoor exploration immensely pleasant for elderly guests. Utilizing our specialized TRAGUIN Jharkhand Packages ensures curated stays, private luxury transport, and a deeply emotional storytelling approach to travel.',
        seo_title='JH-005 | Ranchi | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Jharkhand package (JH-005 / TRG-JH-2026-005): Ranchi, Netarhat, Betla with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: RANCHI ARRIVAL', 1),
            _ih('Day 02: RANCHI SIGHTSEEING', 2),
            _ih('Day 03: RANCHI TO NETARHAT', 3),
            _ih('Day 04: NETARHAT TO BETLA NATIONAL PARK', 4),
            _ih('Day 05: BETLA SAFARI & HISTORIC CHEROKEE FORTS', 5),
            _ih('Day 06: BETLA TO RANCHI DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private storytelling narration detailing historical lore, making', 7),
            _ih('Curated by TRAGUIN Experts: Route mapping strictly structured to keep single-stretch driving', 8),
            _ih('Personalized Assistance: Hands-on assistance across check-ins, porterage coordination, and', 9)
        ],
        days=[
            _day(
                1,
                'RANCHI ARRIVAL',
                (
                    'WELCOME TO THE CITY OF WATERFALLS & THE HEALING LAND OF AIR Upon your graceful arrival at Birsa Munda Airport or Ranchi Railway Station, you will be received with a traditional warm greeting by our professional TRAGUIN tour representative. Enjoy a seamless baggage- handled transfer in a private, air-conditioned Premium Toyota Innova Crysta to your handpicked luxury hotel. After a relaxing check-in and an exquisite lunch, embark on a light, effortless afternoon tour of the iconic Ranchi Lake and the beautifully sculpted Swami Vivekananda Statue standing proudly amidst the TRAGUIN • Premium Travel & Luxury Holidays water. Designed keeping senior mobility in mind, you can appreciate the stunning city views with comfortable seating layouts. Spend your evening soaking in the spiritual tranquility of the Jagannath Temple, a 17th-century architectural marvel. Witness the soothing evening Aarti that fills the atmosphere with divine energy and unparalleled peace.'
                ),
                [
                    'Sightseeing Included: Ranchi Lake, Swami Vivekananda Island, Historic Jagannath Temple.',
                    'Evening Experience: Divine Soulful Evening Aarti at Jagannath Temple with priority senior seating.',
                    'Optional Activities: Mild shopping for organic tribal Tussar Silk shawls.',
                    'Overnight Stay: Ranchi (Premium / Luxury Category Hotel)',
                    'Meals Included: Lunch & Dinner (Curated Low-Spice Dietary Meal)',
                ],
            ),
            _day(
                2,
                'RANCHI SIGHTSEEING',
                (
                    'PATRATU VALLEY MAJESTY & SOPHISTICATED URBAN SERENITY Savor a delightful, healthy breakfast before proceeding towards the pride of Ranchi Sightseeing—the spectacular Patratu Valley. The smooth drive itself is an immersive experience, traversing breathtaking landscapes and magnificent hairpin bends that rival the finest mountain pathways of India. Stop at designated safe viewpoints where our chauffeur will assist you to capture amazing photographs without any steep climbs. In the afternoon, enjoy a serene, calm motorized boat ride at the pristine Patratu Dam, absorbing the soothing cool breeze. Return to the city for a comfortable stroll across the beautifully landscaped Rock Garden, an elite park with sitting benches placed conveniently alongside gentle water features. End your rewarding day with an intimate dinner organized by TRAGUIN experts.'
                ),
                [
                    'Sightseeing Included: Patratu Valley Viewpoints, Patratu Dam, Ranchi Rock Garden.',
                    'Evening Experience: Relaxed lakeside sunset view with hot herbal tea.',
                    'Optional Activities: Photography session against the backdrop of Patratu’s sweeping curves.',
                    'Overnight Stay: Ranchi (Premium / Luxury Category Hotel)',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                3,
                'RANCHI TO NETARHAT',
                (
                    'JOURNEY TO THE QUEEN OF CHOTANAGPUR & MISTY HIGHLANDS TRAGUIN • Premium Travel & Luxury Holidays Following an early breakfast, check out and embark on a scenic drive towards Netarhat, affectionately crowned the "Queen of Chotanagpur". This segment of your Premium Jharkhand Experience features a winding climb through thick clusters of pine, bamboo, and majestic sal forests. The clean, unpolluted mountain air is remarkably rejuvenating. Arrive at your handpicked hill resort by afternoon for a relaxed lunch. As the sun begins its downward arc, you will be driven directly to the famous Magnolia Sunset Point. This spot holds deep emotional storytelling value, named after a colonial-era lore. Watch the sun dip below the expansive horizon, painting the sky in fiery shades of orange and soft violet. The viewing deck is fully flat and senior-citizen friendly, allowing you to imbibe the scenic beauty effortlessly.'
                ),
                [
                    'Sightseeing Included: Chotanagpur Pine Forests, Magnolia Sunset Point, Netarhat Lake.',
                    'Evening Experience: Witnessing the breathtaking sunset from the Magnolia viewing lounge.',
                    'Optional Activities: A slow walk along the calm shores of Netarhat Lake.',
                    'Overnight Stay: Netarhat (Best Available Premium Nature Resort)',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                4,
                'NETARHAT TO BETLA NATIONAL PARK',
                (
                    'SOUL-STIRRING SUNRISES AND CHRONICLES OF ROYAL WOODLANDS An optional early morning drive brings you to the Netarhat Sunrise Point located near the historic Netarhat Residential School. Witness the golden sun emerging beautifully out of the dense morning mist. After a hearty breakfast back at the resort, check out and head towards the glorious wilderness of Betla National Park. En route, we stop at the spectacular Lodh Falls or Lower Ghaghri Falls (accessible via safe, flat paved walkways suited for elderly guests) to admire the majestic water flow. Upon reaching Betla, check in to your premium safari lodge. Spend a tranquil evening listening to the soothing calls of nature, safely nestled in a luxury woodland environment carefully vetted by TRAGUIN. TRAGUIN • Premium Travel & Luxury Holidays'
                ),
                [
                    'Sightseeing Included: Netarhat Sunrise Point, Lower Ghaghri Falls, Betla Eco-zone.',
                    'Evening Experience: Tribal folklore acoustic music performance around a cozy evening bonfire.',
                    'Optional Activities: Birdwatching from the private balcony of your premium lodge.',
                    'Overnight Stay: Betla National Park (Premium Wilderness Lodge)',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                5,
                'BETLA SAFARI & HISTORIC CHEROKEE FORTS',
                (
                    'WILDLIFE ENCOUNTERS & LEGENDARY ROYAL HERITAGE Wake up to a fresh morning and embark on an exclusive, private open-top Betla National Park Safari. Accompanied by a registered forest naturalist, cruise safely through the dense forests to spot majestic herds of spotted deer (Chital), Indian Bison (Gaur), elephants, and exotic birds. The safari trails are chosen carefully to avoid excessive bumps, ensuring total comfort for senior citizens. In the afternoon, explore the magnificent ruins of the Betla/Palamu Forts, historical strongholds built by the Chero dynasty kings deep inside the jungle. The majestic architecture tells silent tales of a regal past. Return to your resort for a relaxed evening and packing, concluding the final night of your premium leisure holiday.'
                ),
                [
                    'Sightseeing Included: Betla Core Forest Wildlife Safari, Ancient Palamu Fort Ruins.',
                    'Evening Experience: An elegant, personalized farewell dinner hosted by our tour manager.',
                    'Optional Activities: Interaction with local guides to understand tribal heritage.',
                    'Overnight Stay: Betla National Park (Premium Wilderness Lodge)',
                    'Meals Included: Breakfast, Lunch & Dinner',
                ],
            ),
            _day(
                6,
                'BETLA TO RANCHI DEPARTURE',
                (
                    'BIDDING FAREWELL TO UNFORGETTABLE MEMORIES Indulge in a relaxed breakfast surrounded by nature. Check out from your premium lodge and begin your return drive back to Ranchi via the incredibly beautiful and smooth highways. Our careful routing ensures timely rest stops and access to clean, hygienic washrooms along the way. Upon reaching Ranchi, if time permits, your vehicle will make a final stop at a premium handicraft emporium to purchase beautiful souvenirs. Afterwards, you will be driven directly to Birsa Munda Airport or Ranchi Railway Station for your onward journey home. Your memorable Jharkhand Family Tour concludes with premium memories to cherish forever, courtesy of TRAGUIN. TRAGUIN • Premium Travel & Luxury Holidays'
                ),
                [
                    'Sightseeing Included: En-route scenic highway viewpoints, Souvenir shopping.',
                    'Evening Experience: Assisted airport / station check-in with dedicated luggage handling.',
                    'Optional Activities: Buying famous local sweets (Peda) from certified outlets.',
                    'Overnight Stay: None (Departure)',
                    'Meals Included: Breakfast & Premium En-route Lunch',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Radisson / Chanakya BNR | Hotel Prabhat Vihar (Premium Annex) | Van Vihar Wilderness Lodge',
                'Ranchi | Netarhat | Betla',
                '2N Ranchi|1N Netarhat|2N Betla',
                'Deluxe',
                'Deluxe Room | Premium Annex | Wilderness Lodge',
                'Breakfast & Dinner',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Radisson / Chanakya BNR | Hotel Prabhat Vihar (Premium Annex) | Van Vihar Wilderness Lodge | Breakfast & Dinner',
            ),
            _hotel(
                'Le Lac Luxury Resort | Netarhat Nature Retreat | Betla Tiger Resort (Executive)',
                'Ranchi | Netarhat | Betla',
                '2N Ranchi|1N Netarhat|2N Betla',
                'Premium',
                'Premium Room | Nature Retreat | Executive Room',
                'All Meals Included',
                4,
                2,
                description='OPTION 02 – PREMIUM: Le Lac Luxury Resort | Netarhat Nature Retreat | Betla Tiger Resort (Executive) | All Meals Included',
            ),
            _hotel(
                'Radisson Blu (Executive Suite) | TRAGUIN Elite Luxury Camps | The Forest Landmark Luxury Resort',
                'Ranchi | Netarhat | Betla',
                '2N Ranchi|1N Netarhat|2N Betla',
                'Luxury',
                'Executive Suite | Luxury Camp | Luxury Resort',
                'All Meals (APA)',
                5,
                3,
                description='OPTION 03 – LUXURY: Radisson Blu (Executive Suite) | TRAGUIN Elite Luxury Camps | The Forest Landmark Luxury Resort | All Meals (APA)',
            ),
            _hotel(
                'The Chanakya Royal Suite | Netarhat Luxury Wooden Cottages | Tree House Luxury Villa (Betla)',
                'Ranchi | Netarhat | Betla',
                '2N Ranchi|1N Netarhat|2N Betla',
                'Ultra Luxury',
                'Royal Suite | Wooden Cottage | Tree House Villa',
                'Premium Specially Curated',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Chanakya Royal Suite | Netarhat Luxury Wooden Cottages | Tree House Luxury Villa (Betla) | Premium Specially Curated',
            )
        ],
        inclusions=[
            _inc_included('Accommodation: Dual-sharing premium handpicked properties featuring senior-friendly bathrooms and elevators.', 1),
            _inc_included('Meals: Complete APA plan (Daily Healthy Breakfast, Lunch, and Dinner) tailored for low-oil, low-spice options.', 2),
            _inc_included('Transfers & Sightseeing: Entire journey via private, deeply sanitized Toyota Innova Crysta driven by a certified professional chauffeur.', 3),
            _inc_included('Assistance: 24/7 dedicated TRAGUIN telephone support line alongside priority on-ground emergency medical coordination.', 4),
            _inc_included('Welcome Amenities: Refreshing non-alcoholic welcome health drinks and custom senior wellness travel kits upon arrival.', 5),
            _inc_included('Complimentary Experiences: One exclusive motorized boat cruise at Patratu Dam and private access to the cultural evening bonfire at Betla.', 6),
            _inc_included('Taxes: All current fuel charges, state highway permits, toll taxes, parking fees, and luxury service surcharges.', 7),
            _inc_included('TRAGUIN • Premium Travel & Luxury Holidays Page 6 of 8', 8),
            _inc_excluded('Flights / Trains: Airfare or railway tickets from your hometown to Ranchi and vice versa.', 9),
            _inc_excluded('Entry Tickets: Camera fees, specialized entry monument passes, and voluntary donations at religious shrines.', 10),
            _inc_excluded('Personal Expenses: Laundry service, room telephone usage, premium alcoholic drinks, and extra mineral water bottles.', 11),
            _inc_excluded('Optional Tours: Any extra sightseeing detours not outlined explicitly inside the official itinerary document.', 12),
            _inc_excluded('Insurance: Individual comprehensive medical and travel insurance coverage (highly advised for senior citizens).', 13),
        ],
    )
    return package, itinerary

def build_jh_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JH-006'
    tour_code = 'TRG-JHR-LUX-006'
    title = 'Ranchi • Netarhat • Betla National Park • Deoghar Luxury Tour'
    duration = '05 Nights / 06 Days'
    slug = 'jh-006-ranchi-netarhat-betla-deoghar-luxury'
    itin_slug = 'jh-006-ranchi-netarhat-betla-deoghar-luxury-itinerary'
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
            _ph('Serial code JH-006 | TRAGUIN tour code TRG-JHR-LUX-006', 1),
            _ph('State / Country: Jharkhand / India | Category: Luxury Holiday', 2),
            _ph('Destinations: Ranchi • Netarhat • Betla National Park • Deoghar', 3),
            _ph('Ideal for: Connoisseurs of Culture, Luxury Seekers, Families & Honeymooners', 4),
            _ph('Best season: October to March (Pleasant & Vibrant)', 5),
            _ph('Starting price: On Request (Bespoke Quotation)', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / MAPAI', 7),
            _ph('TRAGUIN SIGNATURE EXPERIENCE', 8),
            _ph('& BOOKING GUIDELINES', 9),
            _ph('Advance Booking: Betla safari permits and luxury Netarhat cottages are highly restricted; early reservations are', 10)
        ],
        moods=['Luxury', 'Nature', 'Spiritual'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Bespoke Quotation)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Ranchi',
        overview='Ranchi • Netarhat • Betla National Park • Deoghar 05 Nights / 06 Days Immersive Luxury Experience Welcome to an untold realm of sublime wilderness, sacred echoes, and majestic cascading waters. The Best Jharkhand Tour Package by TRAGUIN unlocks the hidden heart of India, presenting an elite blueprint of travel where ancient heritage blends with untouched natural opulence. Embark on a highly tailored Jharkhand Family Tour or an ultra-private Jharkhand Honeymoon Package designed specifically for discerning souls who crave curated experiences, breathtaking landscapes, and premium stays. Let TRAGUIN guide you through dense sal forests, misty hillsides, and regal spiritual structures to forge unforgettable memories.\n\nTOUR OVERVIEW\nThis bespoke itinerary traces a deliberate luxury loop through Jharkhand\'s finest gems. Beginning in the vibrant "City of Waterfalls," Ranchi, your journey moves upwards into the serene clouds of Netarhat ("The Queen of Chotanagpur"), dives deep into the ancient wilderness of Betla National Park, and culminates with a TRAGUIN Luxury Holidays • Premium Jharkhand Itinerary soul-stirring VIP pilgrimage into spiritual Deoghar. Every single detail is overseen by elite travel coordinators to guarantee an unparalleled, stress-free escape. Travel Options: Fully customizable dates (FIT / Private Elite Group) Vehicle assigned: Premium Luxury Chauffeur- Driven SUV (Innova Crysta / Audi / BMW on request) Meal Plan: Continental Breakfast & Curated Gourmet Dinners (MAPAI) TRAGUIN Edge: Handpicked 5-Star & Heritage Stays, Private Local Guides, 24/7 Concierge\n\nWHY CHOOSE A LUXURY JHARKHAND HOLIDAY?\nJharkhand, famously known as the land of forests, is rapidly ascending as India\'s ultimate destination for offbeat luxury. Travelers searching for Luxury Jharkhand Holiday or comprehensive Jharkhand Sightseeing are greeted by unprecedented natural geography away from crowded mass tourism. From the majestic, multi-tiered waterfalls of Ranchi to the mist-laden sunrises of Netarhat, the topography offers the perfect canvas for your next viral Popular Instagram locations. Wildlife aficionados find solace in Betla National Park, home to rare tigers, wild elephants, and a centuries-old tribal history. Culturally, the sacred site of Baidyanath Jyotirlinga in Deoghar delivers deeply transformative spiritual fulfillment, ranking as one of the most searched experiences in Eastern India. Whether you seek thrilling outdoor adventure, authentic tribal textile shopping, or an elegant retreat amidst scenic beauty, this package combines them all into an immersive experience. THE MASTER ITINERARY',
        seo_title='JH-006 | Ranchi | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Jharkhand package (JH-006 / TRG-JHR-LUX-006): Ranchi • Netarhat • Betla National Park • Deoghar with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: RANCHI', 1),
            _ih('Day 02: RANCHI TO NETARHAT', 2),
            _ih('Day 03: NETARHAT TO BETLA NATIONAL PARK', 3),
            _ih('Day 04: BETLA NATIONAL PARK TO RANCHI', 4),
            _ih('Day 05: RANCHI TO DEOGHAR', 5),
            _ih('Day 06: DEOGHAR TO RANCHI / DEPARTURE', 6),
            _ih('TRAGUIN SIGNATURE EXPERIENCE', 7)
        ],
        days=[
            _day(
                1,
                'RANCHI',
                (
                    "ARRIVAL IN THE CITY OF WATERFALLS & ELITE URBAN GRANDEUR Your ultimate Premium Jharkhand Experience begins with a warm, personalized reception at Birsa Munda Airport or Ranchi Railway Station. A designated TRAGUIN luxury travel concierge will escort you via a private luxury vehicle to your handpicked premium hotel. After a smooth VIP check-in and refreshing gourmet welcome drinks, step out to explore the fascinating landmarks of Ranchi. We begin with a scenic drive to the famous Ranchi Lake, followed by an elegant cable car ride up to the historic Tagore Hill, where Rabindranath Tagore's family found deep poetic inspiration. Capture stunning, expansive panoramic photos of the city skyline during golden hour. In the evening, immerse yourself in local culture with an exclusive walk through the vibrant local handicraft markets, ideal for purchasing rare tribal Sohrai paintings and elegant Tussar silk. TRAGUIN Luxury Holidays • Premium Jharkhand Itinerary"
                ),
                [
                    'Sightseeing Included: Tagore Hill, Ranchi Lake, Nakshatra Van, local boutique emporiums.',
                ],
            ),
            _day(
                2,
                'RANCHI TO NETARHAT',
                (
                    'ASCENDING TO THE QUEEN OF CHOTANAGPUR & MYSTICAL SUNSETS Indulge in a rich, multi-cuisine breakfast before departing on a breathtakingly scenic road journey toward Netarhat. As your luxury SUV maneuvers through winding ghats and dense, emerald pine forests, you will feel the air transform into a crisp, invigorating chill. This represents the ultimate luxury mountain escape within our TRAGUIN Jharkhand Packages. Arrive at your premium nature resort in Netarhat by early afternoon. After checking into your luxurious cottage, prepare for an iconic visual feast. Travel to the famous Magnolia Sunset Point, an ethereal location steeped in local romantic lore, where the sun dips below undulating blue hills in a brilliant display of crimson and gold. This remains one of the top-rated Popular Instagram locations in Eastern India.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'NETARHAT TO BETLA NATIONAL PARK',
                (
                    'BREATHTAKING SUNRISES, CASCADING WATERFALLS & UNTAMED WILDERNESS Awaken at dawn to witness an incredible sunrise at Netarhat Sunrise Point, where a sea of white mist rolls majestically through the deep valleys below. Return to your resort for a hearty artisanal breakfast before driving towards the famous Betla National Park. En route, we pause at the magnificent Lodh Falls, the highest waterfall in Jharkhand, where pristine water crashes dramatically down 143 meters into a rugged rocky gorge. Continue your premium drive toward Betla, passing through lush bamboo thickets and old-growth sal forests. Check directly into your exclusive jungle safari lodge. In the late afternoon, step back in time at the historic delicacies. TRAGUIN Luxury Holidays • Premium Jharkhand Itinerary 16th-century Palamu Forts, hidden deep within the forest reserve, offering phenomenal photography opportunities.'
                ),
                [
                    'Optional Activities: Private guided interactive session with a master Sohrai tribal painter.',
                    'Evening Experience: A premium fine-dining experience celebrating authentic, upscale Jharkhandi culinary',
                    'Overnight Stay: Radisson Blu Hotel Ranchi / Chanakya BNR Hotel (Luxury Heritage Suite).',
                    'Meals Included: Curated Dinner.',
                    'Sightseeing Included: Pine Forest drives, Netarhat Dam, Magnolia Point Sunset.',
                    'Optional Activities: Stargazing experience in the clear, pollution-free mountain skies of Netarhat.',
                    "Evening Experience: A private bonfire setup beneath the stars with customized premium hors d'oeuvres.",
                    'Overnight Stay: Premium Eco-Luxury Resort, Netarhat.',
                    'Meals Included: Gourmet Breakfast & Dinner.',
                ],
            ),
            _day(
                4,
                'BETLA NATIONAL PARK TO RANCHI',
                (
                    'DEEP JUNGLE SAFARIS & SPECTACULAR CASCADES Embrace the morning with an exhilarating open-top 4x4 Jeep Safari deep into the core of Betla National Park. Accompanied by a senior forest tracker, keep your camera ready to photograph majestic wild elephants, gaurs, sloth bears, multi-hued deer, and if fortune favors you, the royal Bengal tiger. The vibrant birdlife adds a magical soundtrack to your premium morning safari. Return to the lodge for lunch before checking out to begin your return drive to Ranchi. Along the way, visit the incredible Hundru Falls or Dassam Falls, where the Subarnarekha River plunges over sheer rock cliffs, creating a spectacular mist spray. Re-enter Ranchi in the evening to relax in total 5-star comfort.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'RANCHI TO DEOGHAR',
                (
                    'THE SPIRITUAL PINNACLE & VIP BLESSINGS Following an early breakfast, your premium vehicle will drive you northeast toward the sacred capital of Jharkhand: Deoghar. Known across India as an invaluable bastion of peace and spirituality, Deoghar houses the world-renowned Baidyanath Jyotirlinga Temple. Upon your arrival, TRAGUIN organizes an exclusive, seamless VIP entry and private priest consultation for the holy Baba Baidyanath darshan, completely bypassing standard crowds. Feel the deep spiritual energy of this historic temple complex. Later in the afternoon, board the scenic ropeway to ascend the sacred Trikut TRAGUIN Luxury Holidays • Premium Jharkhand Itinerary Hills, believed to be tied directly to legendary tales from the Ramayana, offering gorgeous aerial views of the landscape.'
                ),
                [
                    'Sightseeing Included: Netarhat Sunrise, Lodh Falls, Koel River viewpoint, Historic Palamu Forts.',
                    'Optional Activities: Guided nature walk with an expert tribal naturalist along the river banks.',
                    'Evening Experience: Open-air tribal folk performance around a cozy campfire at your resort.',
                    'Overnight Stay: The Tree House Resort / Luxury Wildlife Lodge, Betla.',
                    'Meals Included: Gourmet Breakfast & Jungle Dinner.',
                    'Sightseeing Included: Core Zone Jeep Safari, Hundru / Dassam Waterfalls, Jonha Falls (time permitting).',
                    'Optional Activities: Organic farm visit and fresh local tea tasting.',
                    'Evening Experience: High-end therapeutic spa session at your luxury hotel to unwind after your jungle safari.',
                    'Overnight Stay: Radisson Blu Hotel Ranchi.',
                    'Meals Included: Gourmet Breakfast & Dinner.',
                ],
            ),
            _day(
                6,
                'DEOGHAR TO RANCHI / DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES & FAREWELL Savor your final morning breakfast at the hotel, soaking in the serene spiritual atmosphere of Deoghar. If time permits, visit the beautifully designed Naulakha Mandir, famous for its grand architecture reminiscent of Ramakrishna Math structures. Conclude your premium journey as your luxury chauffeur drives you smoothly back to Ranchi Airport or Deoghar Airport/Station for your departure flight home. Board your onward flight with a relaxed spirit and a heart full of unforgettable memories, all meticulously designed and perfectly executed by TRAGUIN.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Chanakya BNR (Executive Room) | Hotel Prabhat Vihar | Van Vihar Forest Resort | Hotel Baidyanath (Executive)',
                'Ranchi | Netarhat | Betla | Deoghar',
                '2N Ranchi|1N Netarhat|1N Betla|1N Deoghar',
                'Deluxe',
                'Executive Room | Deluxe Cottage | Forest Resort | Executive Room',
                'Continental Breakfast & Curated Gourmet Dinners (MAPAI)',
                4,
                1,
                description='OPTION 01 – DELUXE: Chanakya BNR (Executive Room) | Hotel Prabhat Vihar | Van Vihar Forest Resort | Hotel Baidyanath (Executive) | Continental Breakfast & Curated Gourmet Dinners (MAPAI)',
            ),
            _hotel(
                'Hotel Capitol Hill / Landmark | Nature Premium Cottages | Betla Wildlife Retreat | Stoneberry Heritage Resort',
                'Ranchi | Netarhat | Betla | Deoghar',
                '2N Ranchi|1N Netarhat|1N Betla|1N Deoghar',
                'Premium',
                'Premium Room | Premium Cottage | Wildlife Retreat | Heritage Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Hotel Capitol Hill / Landmark | Nature Premium Cottages | Betla Wildlife Retreat | Stoneberry Heritage Resort | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Radisson Blu Ranchi (Superior Room) | Netarhat Luxury Glamping Tents | The Tree House Resort (Luxury Cabin) | Hotel Sai Regency ',
                'Ranchi | Netarhat | Betla | Deoghar',
                '2N Ranchi|1N Netarhat|1N Betla|1N Deoghar',
                'Luxury',
                'Superior Room | Glamping Tent | Luxury Cabin | Premium Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Radisson Blu Ranchi (Superior Room) | Netarhat Luxury Glamping Tents | The Tree House Resort (Luxury Cabin) | Hotel Sai Regency (Premium Suite) | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Radisson Blu (Executive Suite) | Royal Forest Eco-Lodge (VIP Wing) | Luxury Safari Lodge (Private Villa) | Imperial Suite Collec',
                'Ranchi | Netarhat | Betla | Deoghar',
                '2N Ranchi|1N Netarhat|1N Betla|1N Deoghar',
                'Ultra Luxury',
                'Executive Suite | VIP Wing | Private Villa | Imperial Suite',
                'Premium bespoke breakfast and gourmet dinners daily',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Radisson Blu (Executive Suite) | Royal Forest Eco-Lodge (VIP Wing) | Luxury Safari Lodge (Private Villa) | Imperial Suite Collection | Premium bespoke breakfast and gourmet dinners daily',
            )
        ],
        inclusions=[
            _inc_included('Gourmet Meal Plan: Daily breakfast and dinners curated by executive head chefs.', 1),
            _inc_included('Luxury Transfers: Dedicated private luxury SUV for all transits and sightseeing.', 2),
            _inc_included('VIP Assistance: Personalized welcome amenities and express check-ins.', 3),
            _inc_included('Exclusive Darshan: Pre-arranged VIP priority pass at Baidyanath Temple.', 4),
            _inc_included('Elite Safari: Private 4x4 open-top Jeep Safari inside Betla National Park.', 5),
            _inc_included('Professional Guide: Certified English/Hindi speaking destination specialists.', 6),
            _inc_included('TRAGUIN Support: 24/7 real-time remote concierge assistance.', 7),
            _inc_included('All Taxes Included: Drivers allowances, toll taxes, parking fees, and GST.', 8),
            _inc_included('TRAGUIN Luxury Holidays • Premium Jharkhand Itinerary Page 6 of 8', 9),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, alcoholic beverages, and mini-bar.', 10),
            _inc_excluded('Optional Excursions: Any activity specified as optional in the daily itinerary.', 11),
            _inc_excluded('Travel Insurance: Comprehensive health and trip cancellation coverage.', 12),
            _inc_excluded('Tipping: Gratuities for drivers, safari trackers, and hotel staff.', 13),
            _inc_excluded('Sohrai & Khovar Paintings: Stunning traditional canvas folk arts perfect for modern home decor. • Tussar Silk Sarees: World-renowned fine silks hand-woven directly by local master weavers. • Paitkar Art: Classic scroll paintings from ancient tribal settlements. • Local Culinary Treats: Try hot, fresh Dhuska with Ghugni at our exclusively vetted premium organic food stops. • TRAGUIN Luxury Holidays • Premium Jharkhand Itinerary Page 7 of 8', 14),
        ],
    )
    return package, itinerary

def build_jh_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JH-007'
    tour_code = 'TRAGUIN-JH-007'
    title = 'Ranchi • Netarhat • Betla National Park • Deoghar Family Luxury Tour'
    duration = '06 Nights / 07 Days'
    slug = 'jh-007-ranchi-netarhat-betla-deoghar-family-luxury'
    itin_slug = 'jh-007-ranchi-netarhat-betla-deoghar-family-luxury-itinerary'
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
            _ph('Serial code JH-007 | TRAGUIN tour code TRAGUIN-JH-007', 1),
            _ph('State / Country: Jharkhand / India | Category: Luxury Family Tour', 2),
            _ph('Destinations: Ranchi (2N) • Netarhat (2N) • Betla (1N) • Deoghar (1N)', 3),
            _ph('Ideal for: Families, Nature Enthusiasts, Cultural Travelers', 4),
            _ph('Best season: October to March (Pleasant Weather)', 5),
            _ph('Starting price: On Request (Premium Custom Luxury)', 6),
            _ph('Vehicle / Meals: Premium Toyota Innova Crysta / Luxury SUV Meal Plan: Modified American Plan (Breakfast & Dinner Included)', 7),
            _ph("Route: Ranchi → Netarhat → Betla National Park → Ranchi → Deoghar → Ranchi Departure DESTINATION SEO CONTENT Why opt for the Best Jharkhand Tour Package? Jharkhand stands out as one of India's best-kept secrets, offering unmatched potential for a Jharkhand Family Tour or an exclusive Luxury Jharkhand Holiday. As a premier destination, it boasts the Top Tourist Places in Jharkhand, ranging from the architectural wonder of the Sun Temple to the rich bio- diversity of Betla. For families and couples looking for a unique setting, a Jharkhand Honeymoon Package provides mist-covered hills in Netarhat—popularly dubbed the 'Queen of Chotanagpur'—and breathtaking panoramic photography points perfect for your Instagram grid. The Best Time to Visit Jharkhand aligns with the crisp autumn and winter months when the waterfalls are in full, roaring glory and wildlife safaris offer optimal tiger and elephant sightings. From exploring traditional tribal arts and shopping for genuine Paitkar paintings and Tussar silk sarees, to enjoying high-end lakeside cafes in Ranchi, TRAGUIN Jharkhand Packages ensure a deeply immersive, highly sought-after Premium Jharkhand Experience that beautifully connects luxury with authentic local culture. DAY WISE ITINERARY", 8),
            _ph('TRAGUIN Signature Experience: Private English/Hindi speaking destination naturalists for Betla National Park.', 9),
            _ph('Curated by TRAGUIN Experts: Premium vantage points reserved for Magnolia Sunset photography away from', 10),
            _ph('Personalized Assistance: Dedicated destination managers managing seamless check-ins and check-outs at', 11),
            _ph('Premium Handpicked Hotels: Properties vetted strictly for luxury metrics, family-friendly hygiene, and top-tier', 12),
            _ph('Hotel Policies: Standard check-in is at 14:00 hrs; check-out is at 11:00 hrs. Early check-in is subject to availability.', 13),
            _ph('Weather Alert: Netarhat can get quite chilly during winter evenings; packing light woolens is highly recommended.', 14)
        ],
        moods=['Family', 'Nature', 'Spiritual'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Custom Luxury)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Ranchi',
        overview="ntroductory afternoon tour of Ranchi. Visit the iconic Kanke Dam and take a serene private boat cruise across the pristine Ranchi Lake as the sun dips below the horizon. Conclude your evening with a gourmet dinner at a top-tier rooftop restaurant. Sightseeing Included Ranchi Lake Cruise, Kanke Dam, Rock Garden, Tagore Hill Sunset Point. Evening Experience Premium fine-dining experience introducing native tribal flavors refined for luxury palates. Overnight Stay Radisson Blu Hotel Ranchi / Chanakya BNR Hotel (Luxury Option) Meals Included Welcome Drink & Luxury Buffet Dinner TRAGUIN • Premium Travel & Luxury Holidays\n\nTOUR OVERVIEW\nThis bespoke TRAGUIN Jharkhand Package is meticulously crafted for discerning families seeking an exquisite blend of leisure, adventure, and spiritual rejuvenation. Traveling in a premium air-conditioned luxury SUV with dedicated expert drivers, your family will traverse the heart of Eastern India seamlessly. Enjoy handpicked luxury heritage properties and premium resorts, complete with an all-inclusive daily breakfast and dinner plan, tailored perfectly to your tastes. Travel Dates: Group / FIT: TRAGUIN • Premium Travel & Luxury Holidays As per Customization / Flexible Private Luxury FIT Family Tour Vehicle: Premium Toyota Innova Crysta / Luxury SUV Meal Plan: Modified American Plan (Breakfast & Dinner Included) Route Map: Ranchi → Netarhat → Betla National Park → Ranchi → Deoghar → Ranchi Departure\n\nDESTINATION SEO CONTENT\nWhy opt for the Best Jharkhand Tour Package? Jharkhand stands out as one of India's best-kept secrets, offering unmatched potential for a Jharkhand Family Tour or an exclusive Luxury Jharkhand Holiday. As a premier destination, it boasts the Top Tourist Places in Jharkhand, ranging from the architectural wonder of the Sun Temple to the rich bio- diversity of Betla. For families and couples looking for a unique setting, a Jharkhand Honeymoon Package provides mist-covered hills in Netarhat—popularly dubbed the 'Queen of Chotanagpur'—and breathtaking panoramic photography points perfect for your Instagram grid. The Best Time to Visit Jharkhand aligns with the crisp autumn and winter months when the waterfalls are in full, roaring glory and wildlife safaris offer optimal tiger and elephant sightings. From exploring traditional tribal arts and shopping for genuine Paitkar paintings and Tussar silk sarees, to enjoying high-end lakeside cafes in Ranchi, TRAGUIN Jharkhand Packages ensure a deeply immersive, highly sought-after Premium Jharkhand Experience that beautifully connects luxury with authentic local culture.",
        seo_title='JH-007 | Ranchi | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Jharkhand package (JH-007 / TRAGUIN-JH-007): Ranchi (2N) • Netarhat (2N) • Betla (1N) • Deoghar (1N) with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: RANCHI • ARRIVAL IN THE CITY OF WATERFALLS & LUXURY WELCOME', 1),
            _ih('Day 02: RANCHI • MAJESTIC WATERFALLS & CULTURAL EXPLORATION', 2),
            _ih('Day 03: RANCHI TO NETARHAT • JOURNEY TO THE QUEEN OF CHOTANAGPUR', 3),
            _ih('Day 04: NETARHAT • SUNRISE OVER VALLEYS & HIDDEN LAKES', 4),
            _ih('Day 05: NETARHAT TO BETLA NATIONAL PARK • WILDLIFE WILDERNESS SAFARI', 5),
            _ih('Day 06: BETLA TO DEOGHAR VIA RANCHI • SPIRITUAL SOJOURN TO BABA BAIDYANATH', 6),
            _ih('Day 07: DEOGHAR TO RANCHI • TRIKUT HILLS & DEPARTURE WITH FOND MEMORIES', 7),
            _ih('TRAGUIN Signature Experience: Private English/Hindi speaking destination naturalists for Betla National Park.', 8),
            _ih('Curated by TRAGUIN Experts: Premium vantage points reserved for Magnolia Sunset photography away from', 9),
            _ih('Personalized Assistance: Dedicated destination managers managing seamless check-ins and check-outs at', 10)
        ],
        days=[
            _day(
                1,
                'RANCHI • ARRIVAL IN THE CITY OF WATERFALLS & LUXURY WELCOME',
                (
                    'Your extraordinary holiday begins as you touch down at Birsa Munda Airport or arrive at Ranchi Railway Station. A designated TRAGUIN luxury travel consultant will warmly greet your family with fresh flower garlands and traditional refreshments before escorting you to your handpicked premium luxury hotel in a private SUV. After check-in and a relaxing afternoon, embark on an introductory afternoon tour of Ranchi. Visit the iconic Kanke Dam and take a serene private boat cruise across the pristine Ranchi Lake as the sun dips below the horizon. Conclude your evening with a gourmet dinner at a top-tier rooftop restaurant. palates. TRAGUIN • Premium Travel & Luxury Holidays'
                ),
                [
                    'Sightseeing Included: Ranchi Lake Cruise, Kanke Dam, Rock Garden, Tagore Hill Sunset Point.',
                    'Evening Experience: Premium fine-dining experience introducing native tribal flavors refined for luxury',
                    'Overnight Stay: Radisson Blu Hotel Ranchi / Chanakya BNR Hotel (Luxury Option)',
                    'Meals Included: Welcome Drink & Luxury Buffet Dinner',
                ],
            ),
            _day(
                2,
                'RANCHI • MAJESTIC WATERFALLS & CULTURAL EXPLORATION',
                (
                    "Awaken to a lavish breakfast spread before setting off for a day dedicated to Ranchi's iconic, roaring waterfalls. Driven through scenic winding country roads, your first stop is the breathtaking Dassam Falls, where the Subarnarekha River plunges gracefully from a height of 144 feet. Take stunning family portraits at exclusive TRAGUIN curated photography decks. In the afternoon, head to Jonha Falls and Hundru Falls, admiring the lush, mist-kissed forests enveloping the valleys. On the return journey, visit the uniquely constructed Sun Temple, marveling at its elegant chariot wheel architecture."
                ),
                [
                    'Sightseeing Included: Hundru Falls, Jonha Falls, Dassam Falls, and the majestic Sun Temple.',
                    'Optional Activities: Private traditional tribal dance performance and artisan interaction at a local village.',
                    'Overnight Stay: Radisson Blu Hotel Ranchi / Chanakya BNR Hotel (Luxury Option)',
                    'Meals Included: Gourmet Breakfast & Extravagant Dinner',
                ],
            ),
            _day(
                3,
                'RANCHI TO NETARHAT • JOURNEY TO THE QUEEN OF CHOTANAGPUR',
                (
                    'Check out after an early breakfast as your premium vehicle climbs toward Netarhat, the spellbinding hill station celebrated for its unparalleled scenic beauty. The route takes you through dense pine forests, bamboo groves, and rustic tribal hamlets. Arrive by afternoon and check into your premium cottage. As evening nears, drive to the world-famous Magnolia Sunset Point. Here, listen to the timeless, romantic local folklore as the sky turns into a brilliant canvas of deep terracotta and violet tones.'
                ),
                [
                    'Sightseeing Included: Magnolia Sunset Point, Pine Forest Trails, Netarhat Lake.',
                    'Evening Experience: Private starlit bonfire accompanied by roasted local delicacies and premium high tea.',
                    'Overnight Stay: Netarhat Luxury Resort / Prabhat Vihar Premium Cottages',
                    'Meals Included: Breakfast & Traditional Platted Dinner',
                ],
            ),
            _day(
                4,
                'NETARHAT • SUNRISE OVER VALLEYS & HIDDEN LAKES',
                (
                    "Begin your day before dawn as TRAGUIN arranges a private excursion to sunrise point. Witness the sun majestically emerging over the profound, mist-filled hills of the Chotanagpur plateau. Return to your resort for a hearty, warm breakfast. TRAGUIN • Premium Travel & Luxury Holidays Spend the rest of the day exploring Netarhat's hidden gems. Visit the pristine, secluded Sadni Falls and the stunning Lower Ghaghri and Upper Ghaghri waterfalls nestled deep inside dense sal canopies. Visit the historic Netarhat Residential School, a prestigious heritage institution. Grounds."
                ),
                [
                    'Sightseeing Included: Sunrise Point, Lower & Upper Ghaghri Waterfalls, Sadni Falls, Netarhat School',
                    'Photography Points: Panoramic valley overlooks and deep pine forest clearing shots.',
                    'Overnight Stay: Netarhat Luxury Resort / Prabhat Vihar Premium Cottages',
                    "Meals Included: Breakfast & Specialty Chef's Dinner",
                ],
            ),
            _day(
                5,
                'NETARHAT TO BETLA NATIONAL PARK • WILDLIFE WILDERNESS SAFARI',
                (
                    "After breakfast, descend the winding hills towards Betla National Park, one of India’s earliest designated sanctuaries under Project Tiger. Upon reaching, check into your luxury jungle safari lodge. In the afternoon, step into an open-top 4x4 private gypsy for a thrilling jungle safari through Betla's deep wilderness. Keep your eyes trained for majestic Bengal tigers, wild elephants, gaurs, and sloth bears. Inside the heart of the forest, step out to explore the fascinating, historic ruins of the 16th-century Chero Dynasty Forts."
                ),
                [
                    'Sightseeing Included: Betla Jungle Safari, Historic Chero Fort Ruins, Koel River Watchtower.',
                    'Optional Activities: An early morning elephant-back safari (subject to availability and forestry guidelines).',
                    'Overnight Stay: The Tree House Resort Betla / Premium Forest Lodge',
                    'Meals Included: Breakfast & Wilderness Campfire Dinner',
                ],
            ),
            _day(
                6,
                'BETLA TO DEOGHAR VIA RANCHI • SPIRITUAL SOJOURN TO BABA BAIDYANATH',
                (
                    'DHAM Enjoy an early breakfast before embarking on a highly anticipated drive to Deoghar, the sacred spiritual capital of Jharkhand. Travel comfortably across smooth highways as your vehicle transitions seamlessly from wildlife country to the holy land of Lord Shiva. Arrive in Deoghar by late afternoon. Your TRAGUIN private VIP escort will seamlessly guide your family past the long queues for an intimate VIP Darshan at the historic Baba Baidyanath Dham Temple, home to one of the revered twelve sacred Jyotirlingas. Feel the deeply moving spiritual energy as your family takes part in traditional rituals. TRAGUIN • Premium Travel & Luxury Holidays Deoghar Peda).'
                ),
                [
                    'Sightseeing Included: Baidyanath Jyotirlinga Temple, Naulakha Mandir, Satsang Ashram.',
                    'Evening Experience: Enchanting evening Maha Aarti experience followed by local sweet tastings (Famous',
                    'Overnight Stay: Stoneberry By_The_Sukhdeo / Hotel Sanyasi Luxury Stay Deoghar',
                    'Meals Included: Breakfast & Satvik Fine Luxury Dinner',
                ],
            ),
            _day(
                7,
                'DEOGHAR TO RANCHI • TRIKUT HILLS & DEPARTURE WITH FOND MEMORIES',
                (
                    "On your concluding morning, enjoy a relaxed breakfast before checking out. Visit the breathtaking Trikut Hills and enjoy an exhilarating ropeway ride offering sweeping views of the landscapes. Take a quiet, reflective walk around the architectural marvel of Naulakha Temple. Afterwards, enjoy a smooth chauffeured drive back to Ranchi's Birsa Munda Airport or Deoghar Airport for your flight back home. Your luxurious TRAGUIN tour concludes, leaving your family with beautiful bonds, breathtaking photographs, and unforgettable memories. cuisine. TRAGUIN • Premium Travel & Luxury Holidays"
                ),
                [
                    'Sightseeing Included: Trikut Hills Ropeway Ride, Tapovan Caves, Departure Transfer.',
                    'Food Suggestions: A rich luxury lunch at a traditional highway estate serving fresh organic farm-to-table',
                    'Meals Included: Lavish Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel BNR Chanakya (Executive) | Prabhat Vihar Cottages | Van Vihar Forest Resort | Hotel Sanyasi International',
                'Ranchi | Netarhat | Betla | Deoghar',
                '2N Ranchi|2N Netarhat|1N Betla|1N Deoghar',
                'Deluxe',
                'Executive Room | Cottage | Forest Resort | International Room',
                'Modified American Plan (Breakfast & Dinner Included)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel BNR Chanakya (Executive) | Prabhat Vihar Cottages | Van Vihar Forest Resort | Hotel Sanyasi International | Modified American Plan (Breakfast & Dinner Included)',
            ),
            _hotel(
                'Radisson Blu Ranchi (Superior) | Netarhat Luxury Resort | Betla Wildlife Lodge | Hotel Imperial Deoghar',
                'Ranchi | Netarhat | Betla | Deoghar',
                '2N Ranchi|2N Netarhat|1N Betla|1N Deoghar',
                'Premium',
                'Superior Room | Luxury Resort | Wildlife Lodge | Imperial Room',
                'Modified American Plan (Breakfast & Dinner Included)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Blu Ranchi (Superior) | Netarhat Luxury Resort | Betla Wildlife Lodge | Hotel Imperial Deoghar | Modified American Plan (Breakfast & Dinner Included)',
            ),
            _hotel(
                'Radisson Blu Ranchi (Business Class) | TRAGUIN Signature Camp | The Tree House Resort Betla | Stoneberry By_The_Sukhdeo',
                'Ranchi | Netarhat | Betla | Deoghar',
                '2N Ranchi|2N Netarhat|1N Betla|1N Deoghar',
                'Luxury',
                'Business Class | Signature Camp | Tree House | Luxury Suite',
                'Modified American Plan (Breakfast & Dinner Included)',
                5,
                3,
                description='OPTION 03 – LUXURY: Radisson Blu Ranchi (Business Class) | TRAGUIN Signature Camp | The Tree House Resort Betla | Stoneberry By_The_Sukhdeo | Modified American Plan (Breakfast & Dinner Included)',
            ),
            _hotel(
                'Radisson Blu (Executive Suite) | VIP Heritage Bungalow | Luxury Safari Glamping Tents | Stoneberry Luxury Suite',
                'Ranchi | Netarhat | Betla | Deoghar',
                '2N Ranchi|2N Netarhat|1N Betla|1N Deoghar',
                'Ultra Luxury',
                'Executive Suite | Heritage Bungalow | Glamping Tent | Luxury Suite',
                'Modified American Plan (Breakfast & Dinner Included)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Radisson Blu (Executive Suite) | VIP Heritage Bungalow | Luxury Safari Glamping Tents | Stoneberry Luxury Suite | Modified American Plan (Breakfast & Dinner Included)',
            )
        ],
        inclusions=[
            _inc_included('EXCLUSIONS', 1),
            _inc_included('Accommodation: 06 Nights in premium handpicked hotels.', 2),
            _inc_included('Meals: Daily gourmet buffet breakfast and lavish dinners.', 3),
            _inc_included('Transfers: Chauffeur-driven Luxury SUV (Innova Crysta).', 4),
            _inc_included('VIP Assistance: Priority VIP Darshan at Deoghar Jyotirlinga.', 5),
            _inc_included('Sightseeing: All entry tickets, parking, and toll fees included.', 6),
            _inc_included('Welcome Amenities: Personalized luxury travel kit and refreshments.', 7),
            _inc_included('TRAGUIN Support: 24/7 dedicated concierge on call.', 8),
            _inc_excluded('INCLUSIONS (TRAGUIN PREMIUM COMFORT)', 9),
            _inc_excluded('Airfare or train tickets to/from Ranchi.', 10),
            _inc_excluded('Personal expenses (laundry, telephone calls, drinks).', 11),
            _inc_excluded('Camera or video recording fees at national parks.', 12),
            _inc_excluded('Optional adventure sports or helicopter rides.', 13),
            _inc_excluded('Anything not specifically detailed in the inclusions.', 14),
        ],
    )
    return package, itinerary

def build_jh_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JH-008'
    tour_code = 'TRAGUIN-EDU-JH-008'
    title = 'Educational Tour — Ranchi • Netarhat • Betla National Park'
    duration = '04 Nights / 05 Days'
    slug = 'jh-008-educational-ranchi-netarhat-betla'
    itin_slug = 'jh-008-educational-ranchi-netarhat-betla-itinerary'
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
            _ph('Serial code JH-008 | TRAGUIN tour code TRAGUIN-EDU-JH-008', 1),
            _ph('State / Country: Jharkhand / India | Category: School /', 2),
            _ph('Destinations: Ranchi • Netarhat • Betla National Park', 3),
            _ph('Ideal for: Students, Educators, Academic Researchers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Group Customization)', 6),
            _ph('Vehicle / Meals: Premium Luxury AC Coaches equipped with modern safety amenities', 7),
            _ph('Route: Ranchi Arrival ➔ Netarhat ➔ Betla National Park ➔ Ranchi Departure', 8),
            _ph('CULTURAL EXPERIENCES Paitkar & Sohrai Paintings: Students can purchase direct-from-artisan traditional scrolls from rural community craft circles. Jharkhand Silk House (Jharcraft): Premium location to explore Tussar silk weaving methods and authentic tribal organic textiles. TRAGUIN Premium Educational Itinerary • JH-008 Culinary Discoveries: Safe sampling of local items like Dhuska, Malpua, and traditional rice-flour snacks during curated high-tea sessions.', 9),
            _ph('& BOOKING GUIDELINES', 10)
        ],
        moods=['Family', 'Nature', 'Spiritual'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Group Customization)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Educational Tour — Ranchi',
        overview="RANCHI • NETARHAT • BETLA NATIONAL PARK • 04 NIGHTS / 05 DAYS Welcome to an extraordinary academic journey through the land of forests. The Best Jharkhand Tour Package by TRAGUIN is expertly crafted to turn the vast landscapes of eastern India into a living classroom. This immersive Jharkhand Family Tour and student excursion uncovers the rich tribal heritage, dynamic geographical formations, complex industrial milestones, and diverse ecosystems of the region. From the majestic cascades of Ranchi to the dense sal forests of Netarhat and the pristine biodiversity of Betla, our meticulously curated experiences offer students premium stays, breathtaking landscapes, and unforgettable memories that bridge textbook knowledge with real-world discoveries.\n\nTOUR OVERVIEW\nTravel Dates: Flexible / Custom Group Bookings Group / FIT: School Educational Group (Students & Accompanying Faculty) Vehicle: Premium Luxury AC Coaches equipped with modern safety amenities TRAGUIN Premium Educational Itinerary • JH-008 Meal Plan: All Meals Included (Breakfast, Lunch, Hi-Tea, and Dinner) – Nutritious & Student-Friendly Route: Ranchi Arrival ➔ Netarhat ➔ Betla National Park ➔ Ranchi Departure TRAGUIN Curated Experience Note: At TRAGUIN, we believe educational travel should seamlessly blend stringent safety protocols, comfortable handpicked premium hotels, and enriching interactive learning sessions. This tailored itinerary includes expert-guided field trips, interactive cultural exchanges with tribal communities, and environmental science modules designed to maximize student engagement and Google ranking SEO-rich tourism values.\n\nWHY CHOOSE TRAGUIN PREMIUM JHARKHAND EXPERIENCE?\nJharkhand, famously known as the 'Land of Forests,' serves as an unmatched ecological, historical, and geological hub for academic development. Opting for a Luxury Jharkhand Holiday or a dedicated Jharkhand Educational Itinerary opens exceptional pathways to explore ancient archaeological sites, mineral-rich topographies, and wildlife preservation preserves. Our itinerary highlights the Top Tourist Places in Jharkhand, such as the marvelous Hundru and Jonha falls, the historical Netarhat Residential School, and the historical Chero Dynasty Forts deep within Betla. Famous attractions include the panoramic views at Magnolia Sunset Point and the vibrant local tribal craft hubs. It provides the ideal setting for geography fieldwork, botanical observation, history workshops, and outbound leadership programs. This Premium Jharkhand Experience ensures absolute safety, logistical perfection, and immersive storytelling led by professional regional specialists.",
        seo_title='JH-008 | Educational Tour — Ranchi | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Jharkhand package (JH-008 / TRAGUIN-EDU-JH-008): Ranchi • Netarhat • Betla National Park with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN RANCHI', 1),
            _ih('Day 02: RANCHI TO NETARHAT', 2),
            _ih('Day 03: NETARHAT TO BETLA NATIONAL PARK', 3),
            _ih('Day 04: BETLA NATIONAL PARK TO RANCHI', 4),
            _ih('Day 05: RANCHI DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN RANCHI',
                (
                    'WELCOME TO THE CITY OF WATERFALLS – GEOLOGICAL & HISTORICAL INITIATION Upon arrival at Birsa Munda Airport or Ranchi Railway Station, the student cohort will be received with warm hospitality by our dedicated TRAGUIN tour directors. Students will board our premium luxury coach and transfer seamlessly to their handpicked hotel. After check-in and an introductory brief on safety and travel guidelines, the academic exploration begins with a guided tour of the Top Tourist Places in Ranchi. We proceed first to the majestic Hundru Falls, where the Subarnarekha River plunges from a height of 320 feet, creating a magnificent display of classic river rejuvenation and knickpoint geomorphology. An on-site geography expert will explain rock weathering and structural joints. Later, we visit the Ranchi Science Centre to engage in interactive exhibits covering physical sciences and resource mapping. The evening includes a refreshing visit to Ranchi Lake, a historic waterbody excavated in 1842 by British Agent Colonel Onsly, providing an ideal setting for photography points and environmental tracking. TRAGUIN Premium Educational Itinerary • JH-008'
                ),
                [
                    'Sightseeing Included: Hundru Falls, Ranchi Science Centre, Ranchi Lake, and Tagor Hill.',
                    "Optional Activities: Group interactive quiz on Jharkhand's water resource management.",
                    'Evening Experience: Ice-breaking dinner session at the hotel with an educational briefing.',
                    'Overnight Stay: Handpicked Premium Hotel in Ranchi.',
                    'Meals Included: Lunch & Dinner.',
                ],
            ),
            _day(
                2,
                'RANCHI TO NETARHAT',
                (
                    "JOURNEY TO THE QUEEN OF CHOTANAGPUR – BOTANICAL & METEOROLOGICAL STUDY Following a nutritious breakfast, the group will embark on a scenic drive toward Netarhat, affectionately crowned the 'Queen of Chotanagpur'. This winding route showcases breathtaking landscapes, passing through dense clusters of bamboo, sal, and pine trees. Netarhat sits on a massive laterite plate (Pat region) at an altitude of approximately 3,622 feet, making it a stellar case study for mountain ecosystems and high-altitude microclimates. Upon arrival, we visit the legendary Netarhat Residential School, established in 1954, to interact with local educators and understand its prestigious Gurukul-style academic heritage. As the afternoon transitions to twilight, the students will assemble at the iconic Magnolia Sunset Point. Here, through emotional storytelling, local guides narrate historical folklore while students document the spectacular solar dispersion, capturing magnificent views for their geography projects and social media logs."
                ),
                [
                    'Sightseeing Included: Netarhat Pine Forests, Netarhat School Campus, and Magnolia Sunset Point.',
                    'Optional Activities: Nature trail walk focusing on indigenous flora collection and identification.',
                    'Evening Experience: Traditional tribal bonfire dance and musical interaction at the resort.',
                    'Overnight Stay: Curated Premium Eco-Resort / Hotel in Netarhat.',
                    'Meals Included: Breakfast, Lunch, Hi-Tea & Dinner.',
                ],
            ),
            _day(
                3,
                'NETARHAT TO BETLA NATIONAL PARK',
                (
                    "EXPLORING PALAMAU'S BIODIVERSITY CORE & CHERO DYNASTY FORTRESSES Rise early to witness a breathtaking sunrise at the Koel River Viewpoint before enjoying breakfast. Today, the TRAGUIN Jharkhand Packages take the students down to the pristine wilderness of Betla National Park, a historical cornerstone of wildlife conservation and one of India’s earliest sanctuaries integrated under Project Tiger in 1974. En route, the tour halts at the massive Lodh Falls (Burha Falls), the highest waterfall in Jharkhand, cascading down 469 feet. Here, students observe hydraulic action and forest stream ecosystems. Arriving in Betla, we pivot to history and anthropology by exploring the ancient Palamau Forts. Hidden deep inside the dense sal forest, these structures built by the Chero Dynasty rulers in the 16th and 17th centuries feature unique Islamic architectural accents combined with indigenous defense designs, offering deep insights into tribal kingships and medieval defense strategies."
                ),
                [
                    'Sightseeing Included: Lodh Falls, Koel River Viewpoint, and the Historic Palamau Forts.',
                    'Optional Activities: Historical sketching and architectural analysis worksheet distribution.',
                    'Evening Experience: Screening of an educational documentary on wildlife conservation in India.',
                    'Overnight Stay: Handpicked Forest Lodge / Premium Wildlife Resort in Betla.',
                    'Meals Included: Breakfast, Lunch & Dinner.',
                ],
            ),
            _day(
                4,
                'BETLA NATIONAL PARK TO RANCHI',
                (
                    'PREMIUM WILDLIFE SAFARI & RETURN TO CAPITAL FOR EXTENSIVE DEBRIEFING The morning starts with an exhilarating open-hood jungle safari inside Betla National Park. Accompanied by certified forest naturalists, students will spot diverse wildlife species, including Asian elephants, sloth bears, wild boars, sambar deer, and various endemic birds. The naturalists will explain food chains, habitat preservation, and the critical balance required to counter human-wildlife conflict. After a late breakfast, the luxury coach departs back TRAGUIN Premium Educational Itinerary • JH-008 toward Ranchi. Along the way, we pause to observe local rural communities, focusing on sustainable agricultural models and indigenous terracotta handicrafts. Arriving in Ranchi by evening, the students will participate in a structured reflection session curated by TRAGUIN Experts to compile their field notes and review project learnings over a celebratory gala dinner.'
                ),
                [
                    'Sightseeing Included: Betla National Park Morning Safari, Rural Craft Hubs, and Johna Falls (time permitting).',
                    'Optional Activities: Photography contest with awards for the best wildlife and landscape captures.',
                    'Evening Experience: Student presentation and certification ceremony organized by TRAGUIN.',
                    'Overnight Stay: Premium Luxury Hotel in Ranchi.',
                    'Meals Included: Breakfast, Lunch & Dinner.',
                ],
            ),
            _day(
                5,
                'RANCHI DEPARTURE',
                (
                    'TRIBAL HERITAGE IMMERSION & DEPARTURE WITH UNFORGETTABLE MEMORIES On the final day of this exceptional Best Jharkhand Tour Package, students will visit the Dr. Ram Dayal Munda Tribal Research Institute Museum after breakfast. This final academic stop showcases an extensive collection of tribal weapons, lifestyle artifacts, musical instruments, and life-size dioramas representing the Santhal, Munda, Oraon, and Ho tribes. This provides a comprehensive overview of the sociological evolution of central Indian communities. Following the museum tour, students can pick up authentic souvenirs like Sohrai paintings, Dokra metal crafts, and bamboo artifacts. Finally, with enhanced knowledge, broader perspectives, and unforgettable memories, the group will transfer to Ranchi Airport or Railway Station for their onward journey, concluding a highly successful educational tour managed with precision by TRAGUIN.'
                ),
                [
                    'Sightseeing Included: Tribal Research Institute Museum and Local Handloom Craft Centers.',
                    'Optional Activities: Interactive feedback collection and distribution of study certificates.',
                    'Meals Included: Breakfast & Packed Executive Lunch.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Radisson / Capitol Hill | Netarhat Tourist Resort (JTDC) | Van Vihar Resort Betla',
                'Ranchi | Netarhat | Betla',
                '2N Ranchi|1N Netarhat|1N Betla',
                'Deluxe',
                'Deluxe Room | Tourist Resort | Standard Deluxe',
                'All Meals (Buffet)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Radisson / Capitol Hill | Netarhat Tourist Resort (JTDC) | Van Vihar Resort Betla | All Meals (Buffet)',
            ),
            _hotel(
                'Chanakya BNR Hotel | Hotel Prabhat Vihar | Betla Forest Lodge Premium',
                'Ranchi | Netarhat | Betla',
                '2N Ranchi|1N Netarhat|1N Betla',
                'Premium',
                'Premium Room | Premium Cottage | Forest Lodge',
                'All Meals (Buffet)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Chanakya BNR Hotel | Hotel Prabhat Vihar | Betla Forest Lodge Premium | All Meals (Buffet)',
            ),
            _hotel(
                'The Chanakya Premium Wing | Royal Eco Palms Resort | Tree House Wilderness Resort',
                'Ranchi | Netarhat | Betla',
                '2N Ranchi|1N Netarhat|1N Betla',
                'Luxury',
                'Premium Wing | Eco Resort | Tree House',
                'All Meals (Premium)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Chanakya Premium Wing | Royal Eco Palms Resort | Tree House Wilderness Resort | All Meals (Premium)',
            ),
            _hotel(
                'Radisson Blu Executive Suites | Netarhat Luxury Alpine Camps | The Palamau Safari Retreat',
                'Ranchi | Netarhat | Betla',
                '2N Ranchi|1N Netarhat|1N Betla',
                'Ultra Luxury',
                'Executive Suite | Alpine Camp | Safari Retreat',
                'Curated Gourmet Menu',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Radisson Blu Executive Suites | Netarhat Luxury Alpine Camps | The Palamau Safari Retreat | Curated Gourmet Menu',
            )
        ],
        inclusions=[
            _inc_included('Accommodation: Premium triple/quad sharing rooms for students and twin sharing for faculty.', 1),
            _inc_included('Meals: Freshly prepared breakfasts, hot lunches, evening snacks, and multi-cuisine dinners.', 2),
            _inc_included('Transfers: Air-conditioned premium high-deck coaches for all transfers and inter-city drives.', 3),
            _inc_included('Sightseeing: Guided entry and tours across all listed national parks, waterfalls, and museums.', 4),
            _inc_included('Assistance: 24/7 on-ground assistance by certified emergency-trained TRAGUIN tour managers.', 5),
            _inc_included('Taxes: All current applicable Goods & Services Taxes (GST) and state highway tolls.', 6),
            _inc_included('Welcome Amenities: Customized student learning journals, identity badges, and safety kits upon arrival.', 7),
            _inc_included('Complimentary Experiences: Open-hood forest safari tickets, entry fees, and cultural tribal dance workshops.', 8),
            _inc_included('TRAGUIN Support: Dedicated back-end tracking, medical first-aid standby, and doctor-on-call facility.', 9),
            _inc_excluded('Flights: Inbound and outbound train or airfare tickets to and from Ranchi.', 10),
        ],
    )
    return package, itinerary

def build_jh_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JH-009'
    tour_code = 'TG-JHR-ROM-009'
    title = 'Romantic Netarhat & Chotanagpur Hills Luxury Escape'
    duration = '04 Nights / 05 Days'
    slug = 'jh-009-romantic-netarhat-chotanagpur-honeymoon'
    itin_slug = 'jh-009-romantic-netarhat-chotanagpur-honeymoon-itinerary'
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
            _ph('Serial code JH-009 | TRAGUIN tour code TG-JHR-ROM-009', 1),
            _ph('State / Country: Jharkhand / India | Category: Honeymoon / Luxury', 2),
            _ph('Destinations: Jharkhand', 3),
            _ph('Ideal for: Newlyweds, Couples, Luxury Seekers', 4),
            _ph('Best season: October to March (Pleasant Mist & Greenery)', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Luxury Chauffeur-Driven SUV (Innova Crysta / Premium Sedan) Meal Architecture: Daily Elaborate Buffet Breakfast and Custom Gastronomic Dinners Bespoke Route: Ranchi Arrival → Scenic Patratu Valley → Netarhat Highland Retreat → Lodh & Sadni Excursions → Ranchi Departure', 7),
            _ph('Route: Ranchi Arrival → Scenic Patratu Valley → Netarhat Highland Retreat → Lodh & Sadni Excursions → Ranchi Departure', 8),
            _ph('TRAGUIN Signature Experience: Private, romantic evening high-tea setup at Magnolia Point with a', 9),
            _ph('Curated by TRAGUIN Experts: Hand-picked itineraries designed by destination specialists who map', 10),
            _ph('Premium Handpicked Hotels: Every property features exceptional hospitality scores, guaranteed couple-', 11),
            _ph('Luxury Transportation: Professional, fully verified, courteous chauffeurs trained in elite hospitality', 12)
        ],
        moods=['Luxury', 'Nature', 'Spiritual'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Romantic Netarhat & Chotanagpur Hills Luxury Escape',
        overview='Romantic Netarhat & Chotanagpur Hills Luxury Escape Ranchi • Netarhat (Queen of Chotanagpur) • Lodh Waterfalls • Betla • Patratu Valley "Step into a world where mist-covered valleys whisper timeless love stories, and the pristine wilderness of the Chotanagpur Plateau sings in harmony with your hearts. TRAGUIN invites you to experience Jharkhand\'s best-kept secret—a curated romantic honeymoon odyssey through rolling hills, cascading pine forests, and breathtaking panoramic horizons. This is not just a holiday; it is an unforgettable luxury travel experience custom-tailored for souls beginning their shared eternity."\n\nTOUR OVERVIEW\nEmbark on the ultimate Jharkhand Honeymoon Package designed by our elite travel architects. This meticulously planned luxury itinerary weaves together the breathtaking landscapes of the Patratu Valley, the pine-infused mountain breezes of Netarhat—affectionately crowned the "Queen of Chotanagpur"—and the untamed green corridors of Betla. Travel in absolute comfort with a private premium luxury vehicle, TRAGUIN Premium Luxury Holidays handpicked romantic accommodations, and curated experiences that transform moments into milestones. Your bespoke journey features curated candlelit experiences, specialized photography halts, and deep cultural immersions managed seamlessly by TRAGUIN dedicated concierge professionals. Travel Protocol: Private Luxury FIT (Fully Independent Traveler) Execution Premium Vehicle: Luxury Chauffeur-Driven SUV (Innova Crysta / Premium Sedan) Meal Architecture: Daily Elaborate Buffet Breakfast and Custom Gastronomic Dinners Bespoke Route: Ranchi Arrival → Scenic Patratu Valley → Netarhat Highland Retreat → Lodh & Sadni Excursions → Ranchi Departure TRAGUIN Curated Advantage: Dedicated 24/7 VIP assistance, welcome champagne/mocktail amenities, exclusive honeymoon cake cutting, and pre-mapped top Instagram locations for timeless memories.\n\nWHY CHOOSE A LUXURY JHARKHAND HOLIDAY?\nJharkhand is rapidly emerging as India\'s premier choice for eco-luxury tourism and romantic escapades, boasting some of the most spectacular, pristine sights in Eastern India. The Best Jharkhand Tour Package reveals an uncharted paradise far from crowded standard destinations. It is universally sought after for a unique Jharkhand Family Tour or an intimate Jharkhand Honeymoon Package due to its pleasant high- altitude climate, deep mystical woodlands, and expansive views. From the stunning serpentine roads of Patratu Valley, rivaling international alpine routes, to the mesmerizing sunset points of Netarhat, this itinerary captures the essence of Jharkhand Sightseeing. Couples seeking immersive experiences, rich tribal culture, fine local culinary traditions, and rare wildlife photography find their expectations beautifully exceeded with TRAGUIN Jharkhand Packages.',
        seo_title='JH-009 | Romantic Netarhat & Chotanagpur Hills Luxury Escape | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Jharkhand package (JH-009 / TG-JHR-ROM-009): Jharkhand with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: RANCHI ARRIVAL & PATRATU VALLEY EXCURSION', 1),
            _ih('Day 02: RANCHI TO NETARHAT (QUEEN OF CHOTANAGPUR)', 2),
            _ih('Day 03: NETARHAT SUNRISE & LODH FALLS WILDERNESS EXCURSION', 3),
            _ih('Day 04: NETARHAT TO BETLA NATIONAL PARK ECO-ADVENTURE', 4),
            _ih('Day 05: BETLA TO RANCHI & FINAL DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private, romantic evening high-tea setup at Magnolia Point with a', 6),
            _ih('Curated by TRAGUIN Experts: Hand-picked itineraries designed by destination specialists who map', 7),
            _ih('Premium Handpicked Hotels: Every property features exceptional hospitality scores, guaranteed couple-', 8)
        ],
        days=[
            _day(
                1,
                'RANCHI ARRIVAL & PATRATU VALLEY EXCURSION',
                (
                    "WELCOME TO THE LAND OF FORESTS – ASCENT INTO THE SERPENTINE LUXURY OF PATRATU Your premium Jharkhand Tour Package begins with a warm, grand VIP welcome at Ranchi Airport (IXR) or Ranchi Railway Station by our dedicated TRAGUIN tour ambassador. Step into your plush, private air- conditioned vehicle as we escort you into the heart of Jharkhand's capital city. Check into your ultra-luxury room and enjoy an exclusive welcome amenity box curated just for you. By afternoon, your romantic journey heads toward the world-famous Patratu Valley. Prepare to be spellbound as your luxury car glides down the impeccably engineered hairpin turns, surrounded by lush green hills. Stop at our pre-mapped Popular Instagram locations to capture stunning panoramic photographs with the shimmering Patratu Dam backdrop. Enjoy a private, handpicked luxury speedboat ride over the placid waters as the setting sun colors the sky in beautiful hues of gold and amber. TRAGUIN Premium Luxury Holidays Optional Activities: High- speed jet- skiing, local handloom artifact Empora. Overnight Stay: Radisson Blu Hotel Ranchi / Rahi Patratu Luxury Resort (Luxury Option)."
                ),
                [
                    'Sightseeing Included: Patratu Valley S-Curves, Patratu Dam and Lake, VIP Lake Boardwalk.',
                    'shopping: at Ranchi',
                    'Evening Experience: Gourmet high-tea served at a scenic viewpoint overlooking the valley.',
                    'Meals Included: Welcome Drink & Gourmet Dinner.',
                ],
            ),
            _day(
                2,
                'RANCHI TO NETARHAT (QUEEN OF CHOTANAGPUR)',
                (
                    'DRIVE INTO THE MIST-SHROUDED HIGHLANDS & UNMATCHED ROMANTIC SUNSET EXPERIENCE Wake up to a beautiful morning and enjoy a delicious breakfast buffet. Today, we embark on an incredibly scenic drive toward the star highlight of your Jharkhand Honeymoon Package: Netarhat, legendary as the "Queen of Chotanagpur". As the altitude rises, the air cools and becomes crisp, carrying the sweet scent of eucalyptus and pine trees. This high-altitude sanctuary is widely recognized as one of the Top Tourist Places in Jharkhand for travelers seeking pure serenity. Arrive in Netarhat by early afternoon and check into your handpicked, premium cottage sanctuary. After refreshing, stroll hand-in-hand through the majestic, towering Netarhat Pine Forest, an absolute dream for couples and photography lovers. Later, we escort you to the iconic Magnolia Sunset Point. Here, you will witness a breathtaking sunset while hearing the romantic local folklore of Magnolia. It is an emotional, unforgettable moment that defines your premium TRAGUIN Netarhat Experience. TRAGUIN Premium Luxury Holidays Optional Activities: Guided couple\'s nature walk with an expert naturalist through tribal woodland tracks. starry sky. Overnight Stay: Nature Hat Resort / Prabhat Vihar Luxury Premium Cottages, Netarhat.'
                ),
                [
                    'Sightseeing Included: Netarhat Pine Forest, Magnolia Sunset Point, Upper Ghaghri Waterfalls.',
                    'Evening Experience: A warm, private bonfire with an artisanal barbecue session beneath a clear,',
                    'Meals Included: Full Breakfast & Traditional Chotanagpur Royal Dinner.',
                ],
            ),
            _day(
                3,
                'NETARHAT SUNRISE & LODH FALLS WILDERNESS EXCURSION',
                (
                    'A GLORIOUS DAWN AT SUNRISE POINT & MARVELING AT THE MAJESTIC LODH WATERFALLS Begin your day early to witness a spectacular sunrise at Sunrise Point, Netarhat. Watch together in awe as the morning mist rises from the deep valleys, revealing a beautiful canvas of gold, orange, and purple light across the hills. This is widely known as the absolute Best Time to Visit Netarhat for capturing magical, mist-kissed couple photographs. Return to your resort for a hearty, hot breakfast before setting off on an exciting day-trip to the magnificent Lodh Falls, the highest and most awe-inspiring waterfall in Jharkhand. Located within a lush, untamed jungle setting, the sight and sound of water cascading from over 460 feet is truly spectacular. Feel the refreshing, cool mist on your face as you enjoy a private, premium picnic lunch curated by TRAGUIN near the safe viewing zones. On the way back, explore the beautiful, multi-tiered Sadni Falls, nestled gracefully within a tranquil, verdant valley landscape. TRAGUIN Premium Luxury Holidays Optional Activities: Interactive cultural visit to a local tribal village to see traditional Chhotanagpur art. resort. Overnight Stay: Nature Hat Resort / Prabhat Vihar Luxury Premium Cottages, Netarhat.'
                ),
                [
                    'Sightseeing Included: Sunrise Point Netarhat, Lodh Waterfalls, Sadni Falls, Netarhat Dam.',
                    'Evening Experience: A cozy, romantic candlelit dinner featuring fine regional delicacies at your',
                    'Meals Included: Breakfast, Curated Picnic Lunch, and a Special Honeymoon Candlelit Dinner.',
                ],
            ),
            _day(
                4,
                'NETARHAT TO BETLA NATIONAL PARK ECO-ADVENTURE',
                (
                    "JUNGLE SAFARI ROMANCE, ANCIENT FORTS, & IMMERSIVE WILDLIFE ENCOUNTERS After a leisurely, scenic breakfast, check out from the misty heights of Netarhat as we descend toward the lush eco-reserve of Betla National Park, one of India's earliest and most historic wildlife sanctuaries. The drive takes you through beautiful tribal heartlands, dense sal forests, and winding rivers, offering a true taste of wilderness luxury. Arrive and check into your premium wildlife lodge. In the afternoon, embark on an exclusive jungle safari inside Betla National Park. Keep your cameras ready to spot majestic elephants, spotted deer, wild boars, gaurs, and elusive big cats. Deep within the forest, you will explore the historic, atmospheric ruins of the 16th- century Chero Kings' Betla Fort, where nature and history blend beautifully. This unique combination makes it a key highlight of our TRAGUIN Jharkhand Packages. Viewpoint. Optional Activities: Elephant- back safari (subject to availability and forestry TRAGUIN Premium Luxury Holidays department permissions). grounds. Overnight Stay: Hotel Tree House Betla / Van Vihar Premium Eco Resort, Betla."
                ),
                [
                    'Sightseeing Included: Betla Tiger Reserve Sanctuary, Historical Betla Chero Fort, Koel River',
                    'Evening Experience: Tribal dance performance showcase by local artists at the eco-resort',
                    'Meals Included: Breakfast, Lunch, and Jungle-Theme Dinner.',
                ],
            ),
            _day(
                5,
                'BETLA TO RANCHI & FINAL DEPARTURE',
                (
                    "FAREWELL TO THE MAGICAL CHOTANAGPUR HILLS WITH UNFORGETTABLE MEMORIES Enjoy a beautiful, relaxed breakfast while listening to the sweet sounds of the forest. Check out from your eco- lodge as your premium chauffeured vehicle takes you back on a smooth, scenic drive to Ranchi. Along the way, stop at the magnificent Jonha Falls or Hundru Falls (depending on your flight schedule) to marvel at the beautiful river drops that make Ranchi famous as the 'City of Waterfalls'. Indulge in some last-minute shopping at the premium handloom markets to pick up beautiful Souvenirs. Your incredible Luxury Jharkhand Holiday concludes as we transfer you with VIP assistance to Ranchi Airport (IXR) or Ranchi Railway Station for your journey home. You leave with a heart full of joy, deep love, and beautiful memories carefully crafted by TRAGUIN. Optional Activities: Quick lunch stop at a top- rated fine dining restaurant in Ranchi city. Overnight Stay: None (Happy Journey). TRAGUIN Premium Luxury Holidays"
                ),
                [
                    'Sightseeing Included: En-route Waterfall Stop (Jonha/Hundru), Ranchi Local Souvenir Emporium.',
                    'Evening Experience: Direct airport check-in assistance by your dedicated chauffeur.',
                    'Meals Included: Full Buffet Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Chanakya BNR Hotel | Hotel Prabhat Vihar (Govt Class A) | Van Vihar Resort Eco Block',
                'Ranchi | Netarhat | Betla',
                '1N Ranchi|2N Netarhat|1N Betla',
                'Deluxe',
                'Executive Room | Govt Class A | Eco Block',
                'CP Plan (Breakfast & Dinner on select nights)',
                4,
                1,
                description='OPTION 01 – DELUXE: Chanakya BNR Hotel | Hotel Prabhat Vihar (Govt Class A) | Van Vihar Resort Eco Block | CP Plan (Breakfast & Dinner on select nights)',
            ),
            _hotel(
                'Hotel Capitol Hill | Nature Hat Resort (Premium Cottage) | Hotel Tree House Betla',
                'Ranchi | Netarhat | Betla',
                '1N Ranchi|2N Netarhat|1N Betla',
                'Premium',
                'Luxury Suite | Premium Cottage | Valley View',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Hotel Capitol Hill | Nature Hat Resort (Premium Cottage) | Hotel Tree House Betla | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Radisson Blu Ranchi | The Woodside Premium Highlands | Betla Forest Oasis Lodge',
                'Ranchi | Netarhat | Betla',
                '1N Ranchi|2N Netarhat|1N Betla',
                'Luxury',
                'Club Room | VIP Villa | Forest Oasis',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Radisson Blu Ranchi | The Woodside Premium Highlands | Betla Forest Oasis Lodge | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Radisson Blu (Executive Suite) | TRAGUIN Bespoke Heritage Villa Upgrade | Grand Wilderness Safari Suite',
                'Ranchi | Netarhat | Betla',
                '1N Ranchi|2N Netarhat|1N Betla',
                'Ultra Luxury',
                'Executive Suite | Heritage Villa | Plunge Pool Villa',
                'All Meals Included',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Radisson Blu (Executive Suite) | TRAGUIN Bespoke Heritage Villa Upgrade | Grand Wilderness Safari Suite | All Meals Included',
            )
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Double occupancy stays across the selected hotel options.', 1),
            _inc_included('Gourmet Dining: Daily breakfast and dinners as specified in the customized meal plan.', 2),
            _inc_included('Luxury Fleet: Private AC Innova Crysta or premium sedan for all transfers and sightseeing.', 3),
            _inc_included('Welcome Touches: Complimentary honeymoon cake, room decoration, and premium non-alcoholic sparkling drinks upon arrival.', 4),
            _inc_included('Curated Experiences: Private speedboating at Patratu Dam and custom high-tea at Magnolia Point.', 5),
            _inc_included('TRAGUIN Premium Luxury Holidays Page 7 of 9', 6),
            _inc_included('VIP Service: Comprehensive parking fees, toll taxes, driver night allowances, and fuel surcharges included.', 7),
            _inc_included('TRAGUIN Support: 24/7 dedicated remote guest relations manager and local ground assistance.', 8),
            _inc_excluded('Air & Rail Tickets: Domestic/International airfare or train bookings to and from Ranchi.', 9),
            _inc_excluded('Entry & Activity Tickets: Monument entry charges, camera fees, forest safari seat ticketing, and guide charges.', 10),
            _inc_excluded('Personal Expenses: Laundry service, telephone charges, alcoholic beverages, and mini- bar usage.', 11),
            _inc_excluded('Optional Tours: Any sightseeing or extensions not mentioned explicitly in the day-wise itinerary.', 12),
            _inc_excluded('Insurance Protection: Travel, medical, or baggage loss insurance coverages.', 13),
            _inc_excluded('Emergency Costs: Flight delays, land blockage, or expenses arising from unexpected natural events.', 14),
        ],
    )
    return package, itinerary

def build_jh_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JH-010'
    tour_code = 'TG-JH-PANORAMA-010'
    title = 'Jharkhand Panorama Private Luxury Escape'
    duration = '06 Nights / 07 Days'
    slug = 'jh-010-jharkhand-panorama-private-luxury'
    itin_slug = 'jh-010-jharkhand-panorama-private-luxury-itinerary'
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
            _ph('Serial code JH-010 | TRAGUIN tour code TG-JH-PANORAMA-010', 1),
            _ph('State / Country: Jharkhand / India | Category: Luxury Family Tour', 2),
            _ph('Destinations: Ranchi • Netarhat • Betla • Deoghar', 3),
            _ph('Ideal for: Families, Culture Seekers, Nature Lovers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium Customised)', 6),
            _ph('Vehicle / Meals: Private Premium SUV (Toyota Crysta / Luxury Coach) throughout the journey Meal Plan: Modified American Plan (Breakfast & Gourmet Dinner included)', 7),
            _ph('TRAGUIN Signature Experience: Private family interaction session with native Sohrai and Khovar tribal artists,', 8),
            _ph('Curated by TRAGUIN Experts: Hand-tailored routing avoiding bumpy stretches, ensuring utmost travel comfort', 9),
            _ph("Exclusive Recommendations: Savour Jharkhand's royal dessert 'Peda' from local traditional sweet shops in", 10)
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
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Jharkhand Panorama Private Luxury Escape',
        overview='J H A R K H A N D PA N O R A M A P R I VAT E L U X U RY E S C A P E S Embark on a soulful expedition through India’s hidden treasure. TRAGUIN invites your family to immerse in breathtaking landscapes, historic spiritual sanctuaries, pristine tribal cultures, and untouched wildlife reserves with our meticulously crafted Jharkhand Family Tour.\n\nTOUR OVERVIEW\nWelcome to an unforgettable journey curated by TRAGUIN signature travel designers. This bespoke **Jharkhand Panorama** itinerary seamlessly balances premium stays, privately guided exploration, and immersive experiences tailored specifically for discerning families. Your journey spans across magnificent waterfalls, mist-laden plateaus, and highly revered spiritual heritage trail markers. TRAGUIN • Premium Travel & Luxury Holidays Travel Type: Private FIT (Fully Individual Travel) / Private Family Holiday Vehicle: Private Premium SUV (Toyota Crysta / Luxury Coach) throughout the journey Meal Plan: Modified American Plan (Breakfast & Gourmet Dinner included) Route Outline: Ranchi (2N) → Netarhat (1N) → Betla National Park (1N) → Ranchi (1N) → Deoghar (1N) TRAGUIN Curated Highlight: Private tribal art workshop, exclusive sunrise breakfast over the Queen of Chotanagpur, and VIP priority darshan assistance.\n\nWHY CHOOSE A LUXURY JHARKHAND HOLIDAY?\nJharkhand, famously known as the "Land of Forests," is rapidly establishing its mark on the luxury experiential travel map. Far removed from commercialized tourist rushes, a Luxury Jharkhand Holiday offers an intimate rendezvous with nature\'s raw majesty and ancient heritage. From the captivating waterfalls of Ranchi to the surreal, mist-kissed pine forests of Netarhat and the spiritual aura of Deoghar, it is an idyllic destination for an enriching multi-generational family retreat. Top Tourist Places in Jharkhand: Explore iconic architectural wonders like the Baidyanath Jyotirlinga, witness the raw wild flora and fauna at Betla National Park, marvel at the engineering wonder of Maithon and Patratu Valley, and capture Instagram-worthy panoramic vistas from Netarhat Sunset Point. Our comprehensive Jharkhand Sightseeing modules ensure you experience the absolute best time to visit Jharkhand with uncompromised comfort and safety. TRAGUIN • Premium Travel & Luxury Holidays WELCOME TO THE CITY OF WATERFALLS THE CASCADE TRAIL & PATRATU VALLEY VISTAS',
        seo_title='JH-010 | Jharkhand Panorama Private Luxury Escape | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Jharkhand package (JH-010 / TG-JH-PANORAMA-010): Ranchi • Netarhat • Betla • Deoghar with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: RANCHI ARRIVAL', 1),
            _ih('Day 02: RANCHI SIGHTSEEING', 2),
            _ih('Day 03: RANCHI TO NETARHAT', 3),
            _ih('Day 04: NETARHAT TO BETLA NATIONAL PARK', 4),
            _ih('Day 05: BETLA TO RANCHI VIA LODH FALLS', 5),
            _ih('Day 06: RANCHI TO DEOGHAR', 6),
            _ih('Day 07: DEOGHAR DEPARTURE', 7),
            _ih('TRAGUIN Signature Experience: Private family interaction session with native Sohrai and Khovar tribal artists,', 8),
            _ih('Curated by TRAGUIN Experts: Hand-tailored routing avoiding bumpy stretches, ensuring utmost travel comfort', 9),
            _ih("Exclusive Recommendations: Savour Jharkhand's royal dessert 'Peda' from local traditional sweet shops in", 10)
        ],
        days=[
            _day(
                1,
                'RANCHI ARRIVAL',
                (
                    'Arrive at Birsa Munda Airport or Ranchi Railway Station, where your designated TRAGUIN luxury travel concierge warmly greets you to begin your magnificent Premium Jharkhand Experience. Transfer in a premium, high-end SUV to your handpicked luxury hotel. After checking in and enjoying a refreshing welcome drink, take some time to unwind. In the afternoon, enjoy a scenic drive through the breathtaking landscapes of Ranchi to visit the iconic **Rock Garden** and the serene **Kanke Dam**. As evening approaches, experience a mesmerizing private sunset boat cruise on **Ranchi Lake**, set against the majestic backdrop of the historic Tagor Hill. Conclude your day with a curated dining experience introducing your family to sophisticated local culinary treats.'
                ),
                [
                    'Sightseeing Included: Rock Garden, Kanke Dam, Ranchi Lake Private Boat Ride',
                    'Optional Activities: Evening exploration of high-end handicraft emporiums for Sohrai paintings',
                    "Evening Experience: Fine-dining interactive dinner at the hotel's signature restaurant",
                    'Overnight Stay: Ranchi (Premium / Luxury Category)',
                    'Meals Included: Dinner',
                ],
            ),
            _day(
                2,
                'RANCHI SIGHTSEEING',
                (
                    'Relish a sumptuous breakfast before embarking on an exhilarating day of Ranchi Sightseeing. Today you will explore Jharkhand’s legendary cascades. Your private chauffeur will drive you first to the breathtaking **Hundru Falls**, where the Subarnarekha River plunges gracefully from spectacular heights. Next, visit the majestic **Jonha Falls**, also known as the Gautamdhara, tucked beautifully inside lush, sacred groves. Post a luxurious lunch, experience the thrill of negotiating the hairpin bends of the legendary **Patratu Valley S- Curves**—undoubtedly one of the most popular Instagram locations in Eastern India. The engineering marvel of Patratu Dam surrounded by emerald hills offers unforgettable memories. Return to Ranchi for a relaxing evening. TRAGUIN • Premium Travel & Luxury Holidays JOURNEY TO THE QUEEN OF CHOTANAGPUR'
                ),
                [
                    'Sightseeing Included: Hundru Waterfalls, Jonha Falls, Patratu Valley Vistas, Patratu Dam',
                    'Optional Activities: Private cable car ride at Patratu Dam (subject to availability)',
                    'Evening Experience: Leisurely family stroll followed by an authentic tribal-inspired dinner matrix',
                    'Overnight Stay: Ranchi (Premium / Luxury Category)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'RANCHI TO NETARHAT',
                (
                    'Today, our TRAGUIN Jharkhand Packages route ascends towards the heavens. Check out after breakfast and drive through winding, mist-laden roads enveloped by dense Sal and Pine forests to **Netarhat**, fondly called the Queen of Chotanagpur. Upon reaching Netarhat, check in to your premium hillside retreat. In the afternoon, explore the iconic **Netarhat Pear Orchards** and the prestigious Netarhat Residential School campus. As the sun begins its descent, gather at the world- renowned **Netarhat Sunset Point (Magnolia Point)** to witness a deeply emotional storytelling sky ablaze with shades of crimson and gold. TRAGUIN • Premium Travel & Luxury Holidays THE WILD HEARTLAND OF PALAMU ENCOUNTERING THE HIGHEST CASCADE SPIRITUAL AWAKENING AT BABA DHAM'
                ),
                [
                    'Sightseeing Included: Pine Forests, Netarhat School, Magnolia Sunset Point, Lower Ghaghri Falls',
                    'Evening Experience: Stargazing bonfire experience under the clear, crisp skies of Netarhat plateau',
                    'Overnight Stay: Netarhat (Best available boutique heritage/nature resort)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'NETARHAT TO BETLA NATIONAL PARK',
                (
                    "Wake up early to catch a glorious, mist-shrouded sunrise at **Koel View Point**, followed by a specially curated TRAGUIN outdoor bush breakfast. Bid adieu to the hills as we drive down to **Betla National Park**, one of India's earliest established tiger reserves and a core part of the Palamu sanctuary eco-system. Check in to your luxury jungle lodge located on the periphery of the wilderness. In the afternoon, embark on an exclusive private open-jeep wildlife safari through the dense forest tracks. Keep your camera ready to capture sightings of wild elephants, gaurs, sloth bears, sambar deer, and if fortune favors, the elusive big cat. Later, explore the spectacular, historic 16th-century **Palamu Fort ruins** hidden deep inside the park's interior jungles."
                ),
                [
                    'Sightseeing Included: Koel View Point, Betla Jeep Safari, Historical Palamu Fort Ruins',
                    'Optional Activities: Guided nature walk with an expert tribal naturalist',
                    'Evening Experience: Traditional tribal dance presentation around a cozy luxury camp gathering',
                    'Overnight Stay: Betla (Premium Wilderness Lodge)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'BETLA TO RANCHI VIA LODH FALLS',
                (
                    'Enjoy an early breakfast at your jungle lodge before beginning your return leg to Ranchi. En route, embark on an immersive detour to visit the monumental **Lodh Falls (Burha Falls)**—the highest waterfall in Jharkhand, cascading down from an awe-inspiring height of 469 feet amidst deep, green valleys. The drive back is highly scenic, showcasing rural tribal hamlets and vibrant forest life. Arrive back in Ranchi by late afternoon and check in to your luxury urban oasis. Spend the evening relaxing or taking advantage of premium hotel amenities like the spa or rooftop pool.'
                ),
                [
                    'Sightseeing Included: Lodh Falls, Rural Chotanagpur Scenic Drive',
                    "Evening Experience: Gourmet multi-course dinner celebrating your family's travel milestones",
                    'Overnight Stay: Ranchi (Premium / Luxury Category)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                6,
                'RANCHI TO DEOGHAR',
                (
                    "TRAGUIN • Premium Travel & Luxury Holidays CHERISHING UNFORGETTABLE MEMORIES Following an early breakfast, check out and drive towards the highly revered spiritual capital of Eastern India, **Deoghar**. This holy destination forms the focal point of the spiritual aspect of our **Best Jharkhand Tour Package**. Upon arriving in Deoghar, check in to your handpicked premium accommodation. In the afternoon, benefit from TRAGUIN VIP Priority Darshan Assistance at the ancient **Baidyanath Jyotirlinga Temple**, one of the 12 sacred Jyotirlingas in India. Soak in the powerful spiritual energy and view the beautifully interconnected temple spires. Later, enjoy a breathtaking cable car ride up the scenic **Trikut Hills**, renowned as India's only triple-peaked hill."
                ),
                [
                    'Sightseeing Included: Baidyanath Temple, Trikut Hills Ropeway, Naulakha Mandir',
                    'Evening Experience: Divine evening sandhya aarti experience followed by local sweet tastings (Peda)',
                    'Overnight Stay: Deoghar (Premium / Handpicked Best Available)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                7,
                'DEOGHAR DEPARTURE',
                (
                    'Your ultimate Jharkhand Family Tour reaches its beautiful conclusion today. After a leisurely breakfast at your hotel, packing souvenirs and memorable milestones, check out. Enjoy a smooth transfer to the newly commissioned Deoghar Airport (DGH) or Jasidih Railway Station for your homeward journey. Your heart is sure to be filled with deep warmth, pristine photographs, and exceptional, unforgettable stories crafted flawlessly by your premier travel partner, TRAGUIN. TRAGUIN • Premium Travel & Luxury Holidays'
                ),
                [
                    'Transfers Included: Private Airport/Station Drop-off',
                    'Meals Included: Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Chinar / Similar | RSTDC Nature Resort | Hotel Van Vihar (RSTDC) | Hotel Srijan / Similar',
                'Ranchi | Netarhat | Betla | Deoghar',
                '3N Ranchi|1N Netarhat|1N Betla|1N Deoghar',
                'Deluxe',
                'Deluxe Room | Nature Resort | RSTDC Room | Deluxe Room',
                'Modified American Plan (Breakfast & Gourmet Dinner included)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Chinar / Similar | RSTDC Nature Resort | Hotel Van Vihar (RSTDC) | Hotel Srijan / Similar | Modified American Plan (Breakfast & Gourmet Dinner included)',
            ),
            _hotel(
                'Le Lac Luxury Hotel | Netarhat Pine Retreat | Betla Forest Lodge | Stoneberry Heritage',
                'Ranchi | Netarhat | Betla | Deoghar',
                '3N Ranchi|1N Netarhat|1N Betla|1N Deoghar',
                'Premium',
                'Premium Room | Pine Retreat | Forest Lodge | Heritage Room',
                'Modified American Plan (Breakfast & Gourmet Dinner included)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Le Lac Luxury Hotel | Netarhat Pine Retreat | Betla Forest Lodge | Stoneberry Heritage | Modified American Plan (Breakfast & Gourmet Dinner included)',
            ),
            _hotel(
                'Radisson Blu Ranchi | TRAGUIN Premium Eco-Cottage | The Tree House Resort Betla | Imperial Heights Deoghar',
                'Ranchi | Netarhat | Betla | Deoghar',
                '3N Ranchi|1N Netarhat|1N Betla|1N Deoghar',
                'Luxury',
                'Luxury Room | Eco-Cottage | Tree House | Imperial Room',
                'Modified American Plan (Breakfast & Gourmet Dinner included)',
                5,
                3,
                description='OPTION 03 – LUXURY: Radisson Blu Ranchi | TRAGUIN Premium Eco-Cottage | The Tree House Resort Betla | Imperial Heights Deoghar | Modified American Plan (Breakfast & Gourmet Dinner included)',
            ),
            _hotel(
                'Chanakya BNR Heritage Hotel | Signature Swiss Alpine Camps | Palamu Wilderness Luxury Camp | The Grand Deoghar (VIP Suite)',
                'Ranchi | Netarhat | Betla | Deoghar',
                '3N Ranchi|1N Netarhat|1N Betla|1N Deoghar',
                'Ultra Luxury',
                'Heritage Suite | Alpine Camp | Wilderness Camp | VIP Suite',
                'Modified American Plan (Breakfast & Gourmet Dinner included)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Chanakya BNR Heritage Hotel | Signature Swiss Alpine Camps | Palamu Wilderness Luxury Camp | The Grand Deoghar (VIP Suite) | Modified American Plan (Breakfast & Gourmet Dinner included)',
            )
        ],
        inclusions=[
            _inc_included('Daily Gourmet Breakfast & Multi-cuisine Dinners.', 1),
            _inc_included('Entire transit in Private Premium AC SUV (Toyota Crysta).', 2),
            _inc_included('All fuel surcharges, driver allowances, state permits & tolls.', 3),
            _inc_included('TRAGUIN Dedicated 24/7 Remote Concierge support.', 4),
            _inc_included('VIP Priority Darshan passes at Baba Baidyanath Temple.', 5),
            _inc_included('Complimentary mineral water bottles inside your vehicle daily.', 6),
            _inc_included('1 Private Jeep Safari session at Betla National Park.', 7),
            _inc_included('Domestic flights, interstate train bookings or transit tickets.', 8),
            _inc_excluded('Luxury Handpicked Hotel Accommodations as chosen.', 9),
            _inc_excluded('Monument camera fees, guide gratuities or tip pools.', 10),
            _inc_excluded('Personal expanses like laundry, telephone calls, mini- bar usage.', 11),
            _inc_excluded('Any optional adventure activities or lunch meals.', 12),
            _inc_excluded('Goods & Services Tax (GST) as applicable by government norms.', 13),
            _inc_excluded('Travel insurance policies.', 14),
        ],
    )
    return package, itinerary

JHARKHAND_DOMESTIC_BUILDERS = [
    build_jh_001,
    build_jh_002,
    build_jh_003,
    build_jh_004,
    build_jh_005,
    build_jh_006,
    build_jh_007,
    build_jh_008,
    build_jh_009,
    build_jh_010,
]
