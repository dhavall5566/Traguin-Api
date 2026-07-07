"""Builder functions for HP-001 through HP-020 Himachal Pradesh packages."""

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

HIMACHAL_SLUG = "himachal"


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


def build_hp_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-001'
    tour_code = 'TRAGUIN-HP-SHIMLA-001'
    title = 'Shimla Delight Family Getaway'
    duration = '03 Nights / 04 Days'
    slug = 'hp-001-shimla-delight-family-getaway'
    itin_slug = 'hp-001-shimla-delight-family-getaway-itinerary'
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
            _ph('Serial code HP-001 | TRAGUIN tour code TRAGUIN-HP-SHIMLA-001', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Family Vacation / Luxury', 2),
            _ph('Destinations: Shimla • Kufri • Mashobra', 3),
            _ph('Ideal for: Family, Honeymoon & Leisure Seekers', 4),
            _ph('Best season: March to June & October to February', 5),
            _ph("Starting price: On Request (Premium Luxury Tier) TOUR CODE: TRAGUIN-HP-SHIMLA-001 Welcome to an enchanting escape into the majestic Himalayas with the premier TRAGUIN Himachal Pradesh Tour Package. Specially curated for discerning travelers, this bespoke itinerary invites your family to rediscover the timeless charm of Shimla, the legendary 'Queen of Hills'. Immerse yourselves in breathtaking landscapes, mist-laden valleys, and a premium travel lifestyle meticulously engineered by the holiday architects at TRAGUIN. Every detail is crafted to evoke emotional bliss and forge unforgettable memories amidst pristine alpine nature.", 6),
            _ph('Vehicle / Meals: Private Luxury SUV / MAPAI', 7),
            _ph('Route: Chandigarh → Shimla → Kufri → Chail → Chandigarh', 8),
            _ph('TRAGUIN Signature Experience: Private bonfire night under the stars with customized regional live', 9),
            _ph('Curated by Experts: Perfectly timed routes designed to bypass crowded tourist choke points.', 10),
            _ph('Premium Handpicked Hotels: Every property is thoroughly checked for hygiene, security, and world-', 11),
            _ph('Luxury Transportation: Elite fleet of perfectly maintained vehicles driven by certified professional', 12),
            _ph('HOTSPOTS Take home the distinct spirit of the hills by purchasing gorgeous hand-woven Himachali shawls, beautiful wooden toys from Lakkar Bazar, and local pure saffron. For food enthusiasts, we highly recommend trying the traditional slow-cooked feast called Siddu served with rich clarified butter, or stopping at the historic Café Sol on Mall Road for authentic global flavors paired with breathtaking valley views.', 13)
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
        price_note="On Request (Premium Luxury Tier) TOUR CODE: TRAGUIN-HP-SHIMLA-001 Welcome to an enchanting escape into the majestic Himalayas with the premier TRAGUIN Himachal Pradesh Tour Package. Specially curated for discerning travelers, this bespoke itinerary invites your family to rediscover the timeless charm of Shimla, the legendary 'Queen of Hills'. Immerse yourselves in breathtaking landscapes, mist-laden valleys, and a premium travel lifestyle meticulously engineered by the holiday architects at TRAGUIN. Every detail is crafted to evoke emotional bliss and forge unforgettable memories amidst pristine alpine nature.",
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Shimla Delight Family Getaway',
        overview="TOUR OVERVIEW\nTravel Mode: Free Independent Traveler (FIT) / Private Family Tour Vehicle Assigned: Premium Luxury Sedan / SUV (Innova Crysta) Meal Plan: Modified American Plan (MAPAI - Breakfast & Dinner) Route Plan: Chandigarh → Shimla → Kufri → Chail → Chandigarh TRAGUIN Curated Experience Note: This premium tour includes handpicked boutique luxury resorts, exclusive personalized local assistance, a professional uniform-wearing chauffeur experienced in mountain terrains, and surprise value-added family amenities seamlessly coordinated by your dedicated TRAGUIN concierge support specialist.\n\nWHY CHOOSE A LUXURY SHIMLA FAMILY TOUR?\nShimla remains India's ultimate holiday sanctuary, widely searched as the Best Himachal Pradesh Tour Package for generations. It boasts a beautiful synthesis of colonial architecture, spiritual heritage, and untouched ecological wonders. Famous attractions like the Ridge, Mall Road, Jakhoo Temple, and the serene slopes of Kufri represent the most searched experiences in the region. Whether you are looking for the quintessential Himachal Pradesh Honeymoon Package or a wholesome Himachal Family Tour, this region delivers unmatched scenic beauty, vibrant shopping at local bazaars, and countless popular Instagram locations perfect for capturing timeless family moments.",
        seo_title='HP-001 | Shimla Delight Family Getaway | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Himachal Pradesh package (HP-001 / TRAGUIN-HP-SHIMLA-001): Shimla • Kufri • Mashobra with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL & SCENIC FOOTHILL DRIVE', 1),
            _ih('Day 02: ALPINE ADVENTURES & WILDLIFE WONDERS', 2),
            _ih('Day 03: COLONIAL ROMANCE & HERITAGE TRAILS', 3),
            _ih('Day 04: FAREWELL TO THE MOUNTAINS', 4),
            _ih('TRAGUIN Signature Experience: Private bonfire night under the stars with customized regional live', 5),
            _ih('Curated by Experts: Perfectly timed routes designed to bypass crowded tourist choke points.', 6),
            _ih('Premium Handpicked Hotels: Every property is thoroughly checked for hygiene, security, and world-', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL & SCENIC FOOTHILL DRIVE',
                (
                    'CHANDIGARH TO SHIMLA – GATEWAY TO THE QUEEN OF HILLS Your extraordinary mountain vacation begins with a warm royal welcome upon your arrival at Chandigarh Airport or Railway Station. Meet your dedicated luxury chauffeur who will escort your family to a plush, temperature-controlled private vehicle. Embark on a spectacular, highly photogenic uphill drive toward Shimla. As the plains transition into rolling lush green hills, notice the crisp pine-scented air revitalizing your senses. Along the way, we pause for an immersive experience at the Timber Trail Parwanoo, where a thrilling optional cable car ride treats your family to majestic panoramic views of deep valleys. Capture beautiful photographs against a backdrop of mist-shrouded orchards. Arrive in Shimla by late afternoon and check into your handpicked premium luxury resort, where a refreshing welcome drink awaits you. Spend a relaxing evening adapting to the pleasant mountain climate. peaks.'
                ),
                [
                    'Sightseeing Included: Scenic drive via Pinjore & Parwanoo valleys, Timber Trail viewpoints, Sunset',
                    'photography points: .',
                    'Optional Activities: Cable car ride at Parwanoo, traditional Himachali tea tasting session en-route.',
                    'Evening Experience: Leisurely exploration of premium resort amenities, high tea overlooking snow-capped',
                    'Overnight Stay: Premium Luxury Resort / Hotel in Shimla',
                    'Meals Included: Gourmet Buffet Dinner',
                ],
            ),            _day(
                2,
                'ALPINE ADVENTURES & WILDLIFE WONDERS',
                (
                    'EXCURSION TO KUFRI & MASHOBRA – BREATHLESS LANDSCAPES & PEAKS Wake up to a gorgeous sunrise framing the snow-laden Himalayan ranges. After a sumptuous multi-cuisine breakfast, proceed for a highly engaging excursion to Kufri, globally celebrated as one of the Top Tourist Places in Himachal Pradesh. Travel through beautiful, winding trails enveloped by dense cedar forests. Arrive at the Kufri Fun World and Adventure Park, where your family can indulge in safe, thrilling alpine sports. Embark on a traditional horse-back ride up to the Mahasu Peak, navigating scenic forest paths to witness an uninterrupted view of the mighty Himalayan ranges. Next, visit the Himalayan Nature Park to spot rare species like the elusive Snow Leopard, Musk Deer, and Monal pheasants—a phenomenal highlight for children. On your return, explore the serene valley of Mashobra, a premium Instagram location renowned for its untouched pine wilderness and pristine quietude, offering unparalleled opportunities for family portraits. glades. photography. baskets.'
                ),
                [
                    'Sightseeing Included: Kufri Valley Viewpoint, Mahasu Peak, Himalayan Nature Park, Mashobra green',
                    'Optional Activities: Yak riding, dynamic zip-lining, ski-simulator rides, and professional mountain',
                    'Evening Experience: Relaxing evening walk through evergreen cedar groves with customized luxury picnic',
                    'Overnight Stay: Premium Luxury Resort / Hotel in Shimla',
                    'Meals Included: International Breakfast & Gourmet Buffet Dinner',
                ],
            ),            _day(
                3,
                'COLONIAL ROMANCE & HERITAGE TRAILS',
                (
                    "SHIMLA SIGHTSEEING – HISTORIC MALL ROAD, THE RIDGE & JAKHOO HILL Dedicate this day to exploring the legendary soul of the capital town. Following an exquisite breakfast, your Shimla Sightseeing journey starts at the grand Viceregal Lodge (Rashtrapati Niwas), an architectural masterwork of British heritage featuring sprawling manicured English gardens. Next, enjoy a short, scenic trek or a premium ropeway cabin ride up to the iconic Jakhoo Temple, perched atop Shimla's highest peak at 8,050 feet. Be greeted by the majestic 108-foot Hanuman statue guarding the valley. In the afternoon, descend to the pedestrian-only paradise of The Ridge and Mall Road. Stroll past landmark structures including the neo-Gothic Christ Church, Gaiety Theatre, and the bustling Scandal Point. Enjoy premium family shopping for authentic wooden crafts, warm Pashmina shawls, and locally produced Himachali fruit preserves. Conclude your day with a memorable family dinner at a classic heritage café overlooking the glittering lights of the hill town. Point. sessions."
                ),
                [
                    'Sightseeing Included: Viceregal Lodge, Jakhoo Temple, Christ Church, The Ridge, Mall Road, Scandal',
                    'Optional Activities: Private guided heritage walk, old-town street food tasting, colonial attire photo',
                    'Evening Experience: Sunset strolling at the Ridge followed by luxury café hopping along the Mall Road.',
                    'Overnight Stay: Premium Luxury Resort / Hotel in Shimla',
                    'Meals Included: International Breakfast & Gourmet Buffet Dinner',
                ],
            ),            _day(
                4,
                'FAREWELL TO THE MOUNTAINS',
                (
                    'SHIMLA TO CHANDIGARH – DEPARTURE WITH FOREVER MEMORIES Savor your final gourmet breakfast overlooking the peaceful valleys of Shimla. Relish the peaceful mountain atmosphere one last time before completing your smooth resort checkout. Your private luxury chauffeur will safely drive your family back down the picturesque foothills to Chandigarh. If time permits, enjoy a brief stopover at the beautifully sculpted Rock Garden or take a calming boat ride at Sukhna Lake in Chandigarh. Conclude your premium holiday as you are chauffeured to Chandigarh Airport or Railway Station for your journey home. Your signature TRAGUIN curated experience draws to a close, leaving your family with beautifully enriched hearts, renewed bonds, and unforgettable memories of a magical Himalayan retreat. Lake if time permits).'
                ),
                [
                    'Sightseeing Included: Scenic downhill mountain drive, Chandigarh city highlights (Rock Garden/Sukhna',
                    'Optional Activities: Souvenir shopping at local cooperative emporiums during transit.',
                    'Meals Included: International Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Willow Banks / Similar',
                'Himachal Pradesh',
                '03 Nights',
                'Deluxe',
                'Deluxe Valley View Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Willow Banks / Similar | Deluxe Valley View Room | MAPAI',
            ),
            _hotel(
                'Radisson Hotel Shimla / Similar',
                'Himachal Pradesh',
                '03 Nights',
                'Premium',
                'Premium Balcony Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Hotel Shimla / Similar | Premium Balcony Room | MAPAI',
            ),
            _hotel(
                'The Oberoi Cecil / Similar',
                'Himachal Pradesh',
                '03 Nights',
                'Luxury',
                'Luxury Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Oberoi Cecil / Similar | Luxury Suite | MAPAI',
            ),
            _hotel(
                'Wildflower Hall, An Oberoi Resort',
                'Himachal Pradesh',
                '03 Nights',
                'Ultra Luxury',
                'Premier Mountain View Suite',
                'Bespoke Signature MAPAI',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Wildflower Hall, An Oberoi Resort | Premier Mountain View Suite | Bespoke MAPAI',
            )
        ],
        inclusions=[
            _inc_included('Airfare / Train Tickets: Main commercial flights or interstate train connections to/from Chandigarh. Page 6 of 8', 1),
            _inc_included('Entry Tickets & Monuments: Entry fees to historical sites, Jakhoo ropeway, and local amusement parks.', 2),
            _inc_included('Personal Expenses: Laundry services, telephone calls, alcoholic beverages, and traditional porter tips.', 3),
            _inc_included('Adventure Activities: Horse riding, skiing gear rentals, and optional professional tour guides.', 4),
            _inc_excluded('Luxury Accommodation: 03 Nights stay at premium handpicked hotels based on your selected tier selection.', 5),
            _inc_excluded('Premium Meal Plan: Daily lavish breakfasts and chef-crafted buffet dinners at the resorts.', 6),
            _inc_excluded('Private Chauffeur: AC Innova Crysta / Luxury Sedan for all transfers, excursions, and intercity travel.', 7),
            _inc_excluded('Welcome Amenities: Personalized mocktails and signature Himachali fruit basket upon arrival.', 8),
            _inc_excluded('TRAGUIN Support: 24/7 dedicated digital concierge support and professional roadside assistance.', 9),
            _inc_excluded('Insurance & Taxes: Comprehensive travel health insurance policies and incremental personal items.', 10),
        ],
    )
    return package, itinerary

def build_hp_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-002'
    tour_code = 'TRG-HIM-002'
    title = 'Shimla Extended • Alpine Luxury & Timeless Ridges'
    duration = '04 Nights / 05 Days'
    slug = 'hp-002-shimla-extended-alpine-luxury-timeless-ridges'
    itin_slug = 'hp-002-shimla-extended-alpine-luxury-timeless-ridges-itinerary'
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
            _ph('Serial code HP-002 | TRAGUIN tour code TRG-HIM-002', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Premium Family', 2),
            _ph('Destinations: Shimla • Kufri • Mashobra • Naldehra • Chail', 3),
            _ph('Ideal for: Family Vacations, Luxury Mountain Seekers & Honeymooners', 4),
            _ph('Best season: March to June (Summer Resort) & November to February (Snowfall)', 5),
            _ph('Starting price: On Request (Exclusive Custom Tier)', 6),
            _ph('Vehicle / Meals: Luxury Dedicated SUV / MAPAI (Lavish Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private colonial heritage trail walk with an expert local storyteller.', 8),
            _ph('Curated by TRAGUIN Experts: Seamless coordination avoiding weekend bottleneck mountain traffic for', 9),
            _ph('Personalized Assistance: Background-verified hill-certified chauffeurs trained to navigate safely and find', 10),
            _ph('Exclusive Recommendations: Handpicked list of hidden boutique bakeries and secret sunset spots away', 11),
            _ph('Advance Booking: We strongly advise final confirmation at least 30–45 days ahead of travel during', 12),
            _ph('summer months and snow seasons.', 13)
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
        price_note='On Request (Exclusive Custom Tier)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Shimla Extended',
        overview="SHIMLA EXTENDED • ALPINE LUXURY & TIMELESS RIDGES Welcome to an alpine paradise crafted with immaculate precision by TRAGUIN. Embark on the definitive Best Shimla Tour Package, flawlessly designed to immerse your family in the breathtaking landscapes, imperial colonial architecture, and majestic snow-capped peaks of Himachal. As your trusted luxury travel consultants, TRAGUIN transforms your mountain holiday into an elite, stress-free escape complete with premium stays, handpicked hotels, and deeply moving local storytelling. From the iconic walkways of the Ridge to the untouched cedar woodlands of Mashobra and the historic royal grounds of Chail, every experience is tailored to form unforgettable memories.\n\nTOUR OVERVIEW\nThis custom-tailored Shimla Extended Family Tour provides an exquisite escape from urban rush into the refreshing, cool breeze of the Himalayas. Travelling in a completely private, high-end SUV with an experienced mountain chauffeur, your family will experience flawless connectivity across the valley's premier lookout spots. Featuring a premium culinary framework, this journey features luxurious morning spreads and personalized evening fine-dining setups. Your itinerary boasts exclusive TRAGUIN curated experiences—including chauffeured lane clearances, premier viewpoint seats, and around-the-clock bespoke assistance.\n\nWHY BOOK A PREMIUM SHIMLA EXTENDED HOLIDAY?\nWhen considering a Luxury Himachal Holiday, luxury travelers demand a curated balance of colonial nostalgic charm, vibrant local markets, and raw natural serenity. Shimla, historically recognized as the summer capital of British India, remains unmatched in its collection of iconic attractions. From the magnificent, neo-Gothic Christ Church and the sprawling Viceregal Lodge to the deep evergreen glades of Kufri and Naldehra, this region provides vast cultural and visual depth. For families and newly married couples seeking a flawless Shimla Honeymoon Package or Shimla Family Tour, the area hosts several highly popular Instagram locations, such as the misty pine trails of Mashobra, the historical Chail Palace grounds, and the legendary Naldehra Golf Course. Whether you wish to indulge in local boutique shopping on the Mall Road, sample artisan bakery goods, or engage in thrilling mountain horse rides, our dedicated TRAGUIN Himachal Packages guarantee absolute luxury and immersive experiences, providing the absolute best time to visit Himachal.",
        seo_title='HP-002 | Shimla Extended | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Himachal Pradesh package (HP-002 / TRG-HIM-002): Shimla • Kufri • Mashobra • Naldehra • Chail with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SHIMLA', 1),
            _ih('Day 02: KUFRI & JAKHOO HILL ADVENTURE', 2),
            _ih('Day 03: EXCURSION TO MASHOBRA & NALDEHRA', 3),
            _ih('Day 04: DAY TRIP TO CHAIL PALACE', 4),
            _ih('Day 05: SHIMLA TO DELHI/CHANDIGARH DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private colonial heritage trail walk with an expert local storyteller.', 6),
            _ih('Curated by TRAGUIN Experts: Seamless coordination avoiding weekend bottleneck mountain traffic for', 7),
            _ih('Personalized Assistance: Background-verified hill-certified chauffeurs trained to navigate safely and find', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SHIMLA',
                (
                    'GATEWAY TO THE QUEEN OF HILL STATIONS – THE ROYAL RESORT Your premium Himachal experience begins with a grand pick-up at Chandigarh or Delhi airport/station by your private luxury transport vehicle. Ascend the smoothly winding Himalayan express highways, drinking in the scenic beauty of changing vegetation and crisp mountain air. Arrive at Shimla, check into your handpicked premium resort, and refresh. In the late afternoon, step out for an iconic evening experience along the vehicle- free Mall Road and The Ridge. Capture panoramic photography points as the sun sets behind the massive Western Himalayan ranges.'
                ),
                [
                    'Sightseeing Included: The Mall Road, The Ridge, Christ Church, Scandal Point, Gaiety Theatre.',
                    'Evening Experience: Bespoke heritage walk and an elite dinner at a historical colonial-era bistro.',
                    'Overnight Stay: Shimla (Premium Luxury Mountain Resort)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),            _day(
                2,
                'KUFRI & JAKHOO HILL ADVENTURE',
                (
                    "SNOW PEAKS, PANORAMIC RIDGES & HIGHEST PEAKS Indulge in a premium breakfast overlooking the mist-filled valley before driving to Kufri, a celebrated epicentre for panoramic mountain vistas and sub-alpine adventure. Experience breathtaking landscapes from the Mahasu Peak trail, surrounded by thick deodar forests. Children and adults alike will enjoy the Himalayan Nature Park, home to rare high-altitude wildlife. In the afternoon, return to Shimla via a private ropeway cabin ride up to the sacred Jakhoo Temple, perched on Shimla's highest peak with a magnificent giant Hanuman statue. Ropeway. lining."
                ),
                [
                    'Sightseeing Included: Kufri Adventure Valley, Mahasu Peak Point, Himalayan Nature Park, Jakhoo Temple',
                    'Optional Activities: Yak riding, professional snow-suit family photography sessions, or adventure park zip-',
                    'Overnight Stay: Shimla (Premium Luxury Mountain Resort)',
                    'Meals Included: Premium Breakfast & Gourmet Dinner',
                ],
            ),            _day(
                3,
                'EXCURSION TO MASHOBRA & NALDEHRA',
                (
                    'UNTOUCHED CONIFER FORESTS & THE ROYAL GOLF LINKS Escape the primary tourist tracks as you drive towards Mashobra, a serene sanctuary known for its immersive experiences within dense oak woodlands. Walk along the tranquil Craignano nature trails before journeying onwards to Naldehra. Here lies one of the oldest, most scenic 9-hole golf courses in India, surrounded by soaring cedar trees. Enjoy a premium horseback excursion across the rolling greens, discovering incredible high-altitude vistas that serve as highly popular Instagram locations. Reserve.'
                ),
                [
                    'Sightseeing Included: Mashobra Cedar Trails, Naldehra High-Altitude Golf Course, Craignano Nature',
                    'Evening Experience: Private family high-tea set up at an overlook clearing curated by TRAGUIN experts.',
                    'Overnight Stay: Shimla Valley (Premium View Resort)',
                    'Meals Included: Premium Breakfast & Mountain-View Dinner',
                ],
            ),            _day(
                4,
                'DAY TRIP TO CHAIL PALACE',
                (
                    "THE MAHARAJA'S RETREAT & WORLD'S HIGHEST CRICKET PITCH Embark on a scenic southern route to Chail, the historic summer retreat of the Maharaja of Patiala. Wander through the magnificent stone-built Chail Palace, discovering its manicured lawns and royal antique galleries. Later, ascend to the famous Chail Cricket Ground—the highest cricket pitch in the world, sitting at an elevation of 2,444 meters. End your afternoon with a peaceful visit to the Kali Ka Tibba temple, which offers unrivaled, unhindered 360-degree views of the Shivalik and Choordni peaks."
                ),
                [
                    'Sightseeing Included: Chail Palace Museum, Chail Cricket Ground, Kali Ka Tibba Hilltop Temple.',
                    'Evening Experience: Sunset viewing over the entire valley followed by premium multi-cuisine dining.',
                    'Overnight Stay: Shimla (Premium Luxury Mountain Resort)',
                    'Meals Included: Premium Breakfast & Farewell Celebration Dinner',
                ],
            ),            _day(
                5,
                'SHIMLA TO DELHI/CHANDIGARH DEPARTURE',
                (
                    'FAREWELL TO THE MOUNTAINS – CHERISHING LIFE-LONG MEMORIES Wake up to a crisp mountain sunrise and enjoy a final lavish breakfast at your premium resort. Pack your bags with handpicked souvenirs and check out. Your dedicated luxury transport vehicle will safely drive you back down the scenic foothills to Chandigarh or New Delhi Airport/Railway Station. Bid adieu to the snow-flecked horizons, bringing home a heart filled with deep family joy and unforgettable memories exclusively designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door highway drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Willow Banks /',
                'Himachal Pradesh',
                '04 Nights',
                'Deluxe',
                'Clarkes Hotel',
                'Mashobra Resort & Spa',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Willow Banks / | Clarkes Hotel | Mashobra Resort & Spa',
            ),
            _hotel(
                'Radisson Jass Shimla /',
                'Himachal Pradesh',
                '04 Nights',
                'Premium',
                'Welcomhotel',
                'Naldehra Grand Chalet /',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Jass Shimla / | Welcomhotel | Naldehra Grand Chalet /',
            ),
            _hotel(
                'The Oberoi Cecil / Taj',
                'Himachal Pradesh',
                '04 Nights',
                'Luxury',
                'Theog Resort',
                'Chail Palace Luxury',
                4,
                3,
                description='OPTION 03 – LUXURY: The Oberoi Cecil / Taj | Theog Resort | Chail Palace Luxury',
            ),
            _hotel(
                'Wildflower Hall, An',
                'Himachal Pradesh',
                '04 Nights',
                'Ultra Luxury',
                'Oberoi Resort',
                'The Oberoi Sukhvilas',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Wildflower Hall, An | Oberoi Resort | The Oberoi Sukhvilas',
            )
        ],
        inclusions=[
            _inc_included('Premium Accommodation: 04 Nights stay in top-rated handpicked hotels.', 1),
            _inc_included('Luxury Transportation: Private dedicated SUV for all point transfers & hill runs.', 2),
            _inc_included('Curated Meal Plan: Lavish daily breakfast spreads and curated multi-cuisine dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest experience manager on speed-dial.', 4),
            _inc_included('Welcome Amenities: Himalayan apple box & refreshing organic infusions upon arrival.', 5),
            _inc_included('Complimentary Experiences: Private premium ropeway tickets for the Jakhoo Hill climb. TRAGUIN Premium Luxury Itinerary — HP-002 5', 6),
            _inc_excluded('Airfare, interstate rail tickets, or airport taxes.', 7),
            _inc_excluded('Monument entrance fees, camera permissions, or horse-hire charges.', 8),
            _inc_excluded('Personal expenses such as laundry, phone calls, liquor, or tips.', 9),
            _inc_excluded('Any supplementary medical, travel insurance, or emergency evacuation fees.', 10),
        ],
    )
    return package, itinerary

def build_hp_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-003'
    tour_code = 'TRG-HP-003'
    title = 'Shimla Manali Classic • Alpine Luxury & Escapes'
    duration = '05 Nights / 06 Days'
    slug = 'hp-003-shimla-manali-classic-alpine-luxury'
    itin_slug = 'hp-003-shimla-manali-classic-alpine-luxury-itinerary'
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
            _ph('Serial code HP-003 | TRAGUIN tour code TRG-HP-003', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Premium Family', 2),
            _ph('Destinations: Shimla • Kufri • Kullu Valley • Manali • Solang Valley', 3),
            _ph('Ideal for: Family Getaways, Honeymooners & Luxury Retreat Seekers', 4),
            _ph('Best season: March to June (Summer) & October to February (Snow Experience)', 5),
            _ph('Starting price: On Request (Premium Curated)', 6),
            _ph('Vehicle / Meals: Premium AC Innova Crysta / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Hand-crafted mountain routes with pre-arranged pit stops at scenic', 8),
            _ph('Curated by TRAGUIN Experts: Direct coordination with premium hoteliers for room upgrades and flexible', 9),
            _ph('Personalized Assistance: Uniformed, mountain-trained expert chauffeurs with comprehensive navigation', 10),
            _ph('Exclusive Recommendations: Handpicked', 11),
            _ph("Local Markets & Souvenirs: Explore Shimla's Lakkar Bazaar for exquisite handcrafted wooden toys, walking sticks, and home decor items. In Manali, don't miss buying original Kullu shawls, warm rugs, and fresh organic mountain honey or apples directly from orchards. Cafes & Food: Old Manali boasts an incredible array of mountain cafes. Indulge in authentic wood-fired pizzas, fresh trout delicacies, mountain teas, and traditional Himachali Siddu dipped in hot ghee.", 12),
            _ph('Weather & Clothing: Heavy woolens are recommended for winter months (Nov to Feb). Light jackets or', 13)
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
        price_note='On Request (Premium Curated)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Shimla Manali Classic',
        overview='SHIMLA MANALI CLASSIC • ALPINE LUXURY & ESCAPES Welcome to an ethereal journey meticulously crafted by TRAGUIN. Discover the ultimate Himachal Family Tour, a premium retreat designed to unveil the majestic peaks, lush valleys, and charming colonial heritages of Northern India. As your dedicated high-end travel consultants, TRAGUIN delivers a luxury holiday enriched with premium stays, immersive experiences, and breathtaking landscapes. From the historic ridges of Shimla to the adventurous, snow-draped horizons of Manali, every aspect is thoughtfully polished to create unforgettable memories for you and your loved ones.\n\nTOUR OVERVIEW\nThis bespoke luxury itinerary connects the two most iconic hill stations of Himachal Pradesh. Traveling inside a private, high-end vehicle managed by an experienced alpine chauffeur, your family will traverse winding mountain passes, pristine river banks, and pine-clad hillsides with unrivaled ease. Featuring handpicked hotels that overlook cloud-kissed ridges and inclusive gourmet dining, this journey captures the finest premium Himachal experience. Every day features an exclusive TRAGUIN curated experience note, from private high- tea viewpoints to fast-track adventure passes.\n\nWHY CHOOSE THE BEST HIMACHAL TOUR PACKAGE?\nA true Luxury Himachal Holiday demands a beautiful balance of heritage exploration, peaceful nature, and world-class hospitality. Himachal Pradesh remains home to some of the most iconic attractions in the Indian subcontinent. Whether it is walking down the historic Mall Road in Shimla, exploring the panoramic ridges of Kufri, or capturing the majestic snowcapped peaks of Solang Valley and Atal Tunnel near Manali, this destination provides unparalleled visual wonders. For discerning families and couples looking for a magical Himachal Honeymoon Package or Himachal Family Tour, the region offers top tourist places in Himachal packed with popular Instagram locations—such as the Beas River rapids, Hadimba Temple, and the colonial architectural masterpieces of the Viceregal Lodge. With specialized local handicraft shopping for pashmina shawls, immersive paragliding adventures, and intimate cafes, our customized TRAGUIN Himachal Packages stand out as the premium option, perfectly tailored to ensure you travel during the best time to visit Himachal with absolute peace of mind.',
        seo_title='HP-003 | Shimla Manali Classic | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Himachal Pradesh package (HP-003 / TRG-HP-003): Shimla • Kufri • Kullu Valley • Manali • Solang Valley with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DELHI / CHANDIGARH TO SHIMLA', 1),
            _ih('Day 02: SHIMLA & KUFRI EXCURSION', 2),
            _ih('Day 03: SHIMLA TO MANALI VIA KULLU VALLEY', 3),
            _ih('Day 04: MANALI SOLANG VALLEY EXCURSION', 4),
            _ih('Day 05: MANALI LOCAL SIGHTSEEING', 5),
            _ih('Day 06: MANALI TO DELHI / CHANDIGARH DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Hand-crafted mountain routes with pre-arranged pit stops at scenic', 7),
            _ih('Curated by TRAGUIN Experts: Direct coordination with premium hoteliers for room upgrades and flexible', 8),
            _ih('Personalized Assistance: Uniformed, mountain-trained expert chauffeurs with comprehensive navigation', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DELHI / CHANDIGARH TO SHIMLA',
                (
                    'ASCENDING TO THE QUEEN OF HILL STATIONS Your premium Himachal experience kicks off with a warm welcome by your private TRAGUIN chauffeur at the airport/railway station. Board your luxury vehicle and begin a beautiful, scenic uphill drive towards Shimla. Watch the changing terrain as plains give way to terraced orchards and pine forests. Arrive at your handpicked luxury resort in Shimla, check into your room featuring sweeping views of the valley, and spend a relaxing evening enjoying the crisp mountain air.'
                ),
                [
                    'Sightseeing Included: Scenic Himalayan Expressway drive, Pinjore timber trail vistas.',
                    'Evening Experience: Private veranda high-tea with valley views, arranged by TRAGUIN.',
                    'Overnight Stay: Shimla (Premium / Luxury Mountain Resort)',
                    'Meals Included: Welcome Refreshment & Gourmet Buffet Dinner',
                ],
            ),            _day(
                2,
                'SHIMLA & KUFRI EXCURSION',
                (
                    'COLONIAL MAJESTY & PANORAMIC ALPINE PEAKS After a premium breakfast, proceed for a morning excursion to Kufri, an iconic attraction famed for its breathtaking landscapes and panoramic Himalayan snow-range views. Enjoy light adventure activities, yak rides, and photography points amidst dense cedar forests. In the afternoon, return to Shimla to explore its colonial past. Walk along the historic Mall Road, visit the beautiful Ridge, the neo-gothic Christ Church, and the grand Viceregal Lodge—once the summer seat of British viceroys.'
                ),
                [
                    'Sightseeing Included: Kufri Fun World, Viceregal Lodge, The Ridge, Mall Road, Christ Church, Scandal Point.',
                    'Optional Activities: Pony trekking in Kufri trails or heritage indoor tour of the Viceregal ballroom.',
                    'Overnight Stay: Shimla (Premium / Luxury Mountain Resort)',
                    'Meals Included: Premium Breakfast & Luxury Dinner',
                ],
            ),            _day(
                3,
                'SHIMLA TO MANALI VIA KULLU VALLEY',
                (
                    'SCENIC DRIVE ALONG THE RUSHING WATERS OF THE BEAS Bid adieu to Shimla and drive towards Manali through the spellbinding Kullu Valley. This scenic route traces the roaring Beas River, framed by towering granite cliffs and emerald pine woodlands. Stop en route at the beautiful Pandoh Dam and visit the traditional handloom factories in Kullu for exclusive shopping of authentic pashmina and woolens. Arrive in Manali by evening—a top tourist place in Himachal—and settle into an exquisite luxury riverside hotel.'
                ),
                [
                    'Sightseeing Included: Kullu Valley drive, Pandoh Dam, Hanogi Mata Temple overlooks, Beas River vistas.',
                    'Evening Experience: Riverside bonfire with live traditional music recommendations by TRAGUIN experts.',
                    'Overnight Stay: Manali (Premium Customised Riverside Resort)',
                    'Meals Included: Breakfast & Lavish Buffet Dinner',
                ],
            ),            _day(
                4,
                'MANALI SOLANG VALLEY EXCURSION',
                (
                    'SNOW FIELDS, GLACIERS & HIGHLAND ADVENTURE Today is dedicated to the thrilling alpine playground of Solang Valley, globally renowned for its immersive experiences and outdoor sports. Witness breathtaking landscapes of glaciers and snowcapped mountains. Participate in thrilling optional activities like paragliding, zorbing, and a scenic cable-car ropeway ride. (Depending on weather and permissions, an optional excursion to the engineering marvel of Atal Tunnel or Rohtang Pass can be seamlessly added by your consultant).'
                ),
                [
                    'Sightseeing Included: Solang Valley Meadow, Snow Point Viewpoints, Adventure Activity Arenas.',
                    'Optional Activities: Tandem paragliding, quad biking over snow, or Atal Tunnel north-portal crossing.',
                    'Overnight Stay: Manali (Premium Customised Riverside Resort)',
                    "Meals Included: Premium Breakfast & Chef's Special Dinner",
                ],
            ),            _day(
                5,
                'MANALI LOCAL SIGHTSEEING',
                (
                    'CULTURAL HERITAGE, FOREST SANCTUARIES & OLD MANALI CAFES Explore the unique cultural tapestry of Manali today. Visit the 16th-century wooden Hadimba Temple, set inside the deep shade of towering Dhungri Deodar forests. Explore the sacred Vashisht Hot Water Springs, followed by the serene Tibetan Monastery. Spend your afternoon wandering through the popular Instagram locations of Old Manali, enjoying its vibrant bohemian cafes, local bakeries, and unique lifestyle boutiques.'
                ),
                [
                    'Sightseeing Included: Hadimba Devi Temple, Vashisht Village & Springs, Tibetan Monastery, Old Manali lanes.',
                    'Evening Experience: Leisurely shopping walk on Manali Mall Road with custom local food suggestions.',
                    'Overnight Stay: Manali (Premium Customised Riverside Resort)',
                    'Meals Included: Breakfast & Farewell Grand Dinner',
                ],
            ),            _day(
                6,
                'MANALI TO DELHI / CHANDIGARH DEPARTURE',
                (
                    'RETURNING WITH MEMORIES BEYOND DESTINATIONS Enjoy your final luxury breakfast facing the mist-draped Beas valley. Pack your bags and check out from your premium resort. Your private vehicle will carefully drive you down the smooth highway paths back to Chandigarh or New Delhi airport/railway station. Head homeward carrying a treasure trove of laughter, familial bonds, and unforgettable memories exclusively designed for you by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private door-to-door highway departure drop-off.',
                    'Meals Included: Lavish Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Willow Banks / East',
                'Himachal Pradesh',
                '05 Nights',
                'Deluxe',
                'Bourne Resort',
                'The Grand Welcome / Solang',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Willow Banks / East | Bourne Resort | The Grand Welcome / Solang',
            ),
            _hotel(
                'Radisson Hotel Shimla /',
                'Himachal Pradesh',
                '05 Nights',
                'Premium',
                'Sterling Kufri',
                'ManuAllaya Resort / Tiaraa',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Hotel Shimla / | Sterling Kufri | ManuAllaya Resort / Tiaraa',
            ),
            _hotel(
                'The Taj The Trees, Shimla /',
                'Himachal Pradesh',
                '05 Nights',
                'Luxury',
                'Welcomhotel',
                'The Himalayan Castle / Span',
                4,
                3,
                description='OPTION 03 – LUXURY: The Taj The Trees, Shimla / | Welcomhotel | The Himalayan Castle / Span',
            ),
            _hotel(
                'Wildflower Hall, An Oberoi',
                'Himachal Pradesh',
                '05 Nights',
                'Ultra Luxury',
                'Resort (Luxury Suite)',
                'The Oberoi Sukhvilas /',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Wildflower Hall, An Oberoi | Resort (Luxury Suite) | The Oberoi Sukhvilas /',
            )
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Curated stay options across handpicked hotels.', 1),
            _inc_included('Luxury Transportation: Private Chauffeur-driven AC Innova Crysta throughout.', 2),
            _inc_included('Curated Meal Plan: Daily elaborate breakfasts and multi-cuisine dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated travel concierge assistant on call.', 4),
            _inc_included('Welcome Amenities: Himalayan customized travel kits, organic juices & fruits.', 5),
            _inc_included('Exclusive Experiences: Private bonfire session & family portrait photography pointers.', 6),
            _inc_excluded('Airfare, flight extensions, or train tickets to Delhi/ Chandigarh.', 7),
            _inc_excluded('Rohtang Pass NGT permissions & local shuttle vehicle charges.', 8),
            _inc_excluded('Adventure sport fees (paragliding, zorbing, river rafting tickets).', 9),
            _inc_excluded('Personal incidentals, room service, laundry, tips, and insurance. TRAGUIN Premium Luxury Itinerary — HP-003 5', 10),
        ],
    )
    return package, itinerary

def build_hp_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-004'
    tour_code = 'TRG-HIM-004'
    title = 'Shimla • Manali • Dharamshala Explorer'
    duration = '07 Nights / 08 Days'
    slug = 'hp-004-shimla-manali-dharamshala-explorer'
    itin_slug = 'hp-004-shimla-manali-dharamshala-explorer-itinerary'
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
            _ph('Serial code HP-004 | TRAGUIN tour code TRG-HIM-004', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Premium Family', 2),
            _ph('Destinations: Shimla • Manali • Solang Valley • Dharamshala • Mcleodganj', 3),
            _ph('Ideal for: Family Vacations, Honeymooners, Luxury Explorers', 4),
            _ph('Best season: March to June (Summer Comfort) & October to February (Snow Experience)', 5),
            _ph('Starting price: On Request (Bespoke Luxury Customized)', 6),
            _ph('Vehicle / Meals: Private Premium SUV (Innova Crysta) / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private family orchard stroll and riverside tea-tasting arrangements', 8),
            _ph('Curated by TRAGUIN Experts: Smart pass planning across the Atal Tunnel to eliminate long lines and', 9),
            _ph('Exclusive Recommendations: Handpicked list of mountain cafes, Tibetan artisan workshops, and secret', 10),
            _ph('Booking Policy: We highly advise advance bookings at least 45 days prior to travel, especially during', 11),
            _ph('peak seasons like summer and winter snow months.', 12)
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
        price_note='On Request (Bespoke Luxury Customized)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Shimla',
        overview='SHIMLA • MANALI • DHARAMSHALA EXPLORER 07 NIGHTS / 08 DAYS Welcome to an otherworldly alpine escape crafted to perfection by TRAGUIN. Embark on the ultimate Himachal Family Tour designed to reveal the breathtaking landscapes, snow-capped peaks, and rich cultural tapestry of the Himalayas. As your elite travel consultants, TRAGUIN transforms your mountain holiday into a flawless luxury retreat filled with handpicked hotels, premium stays, and immersive experiences. From the colonial heritage elegance of Shimla to the high-altitude adventure playgrounds of Manali and the spiritual serenity of Dharamshala, every single day is masterfully balanced to leave you with unforgettable memories.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers an unparalleled exploration through the finest hill stations of Northern India. Travelling in a dedicated private premium AC vehicle with professional mountain-trained chauffeur assistance, your family will enjoy absolute comfort and flexibility. With a carefully curated meal plan featuring lavish buffet breakfasts and specialized dinners, this route represents the definitive premium Himachal experience. Every step of your journey includes the signature touch of TRAGUIN curated experiences, ensuring VIP entry privileges, local heritage insights, and around-the-clock bespoke guest support.\n\nWHY CHOOSE THE BEST HIMACHAL TOUR PACKAGE?\nWhen planning a Luxury Himachal Holiday, sophisticated travelers look past standard itineraries to find truly exclusive experiences. Himachal Pradesh boasts some of the most iconic attractions in the world. From Shimla’s historical Mall Road and the snow-blessed altitudes of Solang Valley in Manali—the ultimate tourist places in Himachal for adventure—to the serene Tibetan monasteries of Dharamshala, this circuit offers unmatched environmental and cultural variety. For couples seeking a romantic Himachal Honeymoon Package or families booking an immersive Himachal Family Tour, the region unveils highly popular Instagram locations like the architectural Ridge of Shimla, the scenic beauty of Rohtang Pass paths, and the deep green cedar forests of McLeodganj. Whether you are looking for local handicraft shopping, indulging in traditional Himachali Dham cuisine, or seeking spiritual peace under the shadow of the Dhauladhar range, our TRAGUIN Himachal Packages guarantee premium comfort, handpicked luxury stays, and curated exclusive experiences that outline the best time to visit Himachal.',
        seo_title='HP-004 | Shimla | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Himachal Pradesh package (HP-004 / TRG-HIM-004): Shimla • Manali • Solang Valley • Dharamshala • Mcleodganj with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DELHI TO SHIMLA', 1),
            _ih('Day 02: SHIMLA & KUFRI SIGHTSEEING', 2),
            _ih('Day 03: SHIMLA TO MANALI VIA KULLU VALLEY', 3),
            _ih('Day 04: MANALI LOCAL SIGHTSEEING', 4),
            _ih('Day 05: SOLANG VALLEY & ATAL TUNNEL EXCURSION', 5),
            _ih('Day 06: MANALI TO DHARAMSHALA', 6),
            _ih('Day 07: DHARAMSHALA & MCLEODGANJ EXPLORATION', 7),
            _ih('Day 08: DHARAMSHALA TO DELHI / DEPARTURE', 8),
            _ih('TRAGUIN Signature Experience: Private family orchard stroll and riverside tea-tasting arrangements', 9),
            _ih('Curated by TRAGUIN Experts: Smart pass planning across the Atal Tunnel to eliminate long lines and', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DELHI TO SHIMLA',
                (
                    'GATEWAY TO THE SUMMER CAPITAL – SCENIC HILL DRIVE Your premium Himachal experience starts with a warm welcome at New Delhi Airport/Railway Station by your private chauffeured luxury vehicle. Leave the plains behind as you climb into the majestic Shivalik hills toward Shimla. As you wind through gorgeous mountain passes, experience the changing air and the breathtaking landscapes. Upon arrival in Shimla, check into your handpicked premium hotel and spend a relaxing evening admiring the mist-laden valleys. Welcome Refreshments & Luxury Dinner'
                ),
                [
                    'Sightseeing Included: Scenic Himalayan express highway drive, Pinjore Gardens stopover (optional).',
                    'Evening Experience: Private candlelight family welcome dinner at your luxury mountain resort.',
                    'Overnight Stay: Shimla (Premium / Luxury Mountain Resort)',
                    'Meals: Included:',
                ],
            ),            _day(
                2,
                'SHIMLA & KUFRI SIGHTSEEING',
                (
                    'COLONIAL CHARM, ALPINE PANORAMAS & THE MALL ROAD After a grand breakfast, enjoy a short drive to Kufri, a top tourist place in Shimla celebrated for its dense pine forests and snow-capped mountain views. Experience a fun yak ride or try soft adventure activities amidst the breathtaking landscapes. In the afternoon, return to Shimla for an iconic walking tour across The Ridge, the neo-Gothic Christ Church, and the historic Mall Road. Capture amazing family photos at these popular Instagram locations while enjoying the pleasant weather. Point.'
                ),
                [
                    'Sightseeing Included: Kufri Adventure Park, Green Valley view, The Ridge, Christ Church, Mall Road, Scandal',
                    'Optional Activities: Heritage walk to the Viceregal Lodge, the historic seat of British power.',
                    'Overnight Stay: Shimla (Premium / Luxury Mountain Resort)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),            _day(
                3,
                'SHIMLA TO MANALI VIA KULLU VALLEY',
                (
                    'JOURNEY ALONG THE BEAS RIVER – VALLEY OF THE GODS Bid farewell to Shimla and head toward Manali on a highly scenic drive through the heart of Himachal. Wind along the sparkling Beas River and cross the breathtaking Kullu Valley. Stop en route to experience the traditional handloom factories of Kullu, famous for premium pashmina shawls. Take in the dramatic canyon views and beautiful waterfalls along the way. Arrive in Manali by evening and check into a premium riverside luxury resort curated by TRAGUIN experts.'
                ),
                [
                    'Sightseeing Included: Sundernagar Lake, Pandoh Dam, Kullu Valley, Beas River drive views.',
                    'Evening Experience: Stroll along the riverbanks of the resort followed by a warm bonfire night.',
                    'Overnight Stay: Manali (Premium Riverside Luxury Property)',
                    'Meals Included: Breakfast & Lavish Riverside Dinner',
                ],
            ),            _day(
                4,
                'MANALI LOCAL SIGHTSEEING',
                (
                    'WOODLAND TEMPLES & HIGHLAND CULTURE Immerse yourself in the local heritage and scenic beauty of Manali. Begin with the ancient Hadimba Devi Temple, tucked away inside a dense, beautiful forest of giant deodar cedars. Explore the old stone structures of Vashisht Village, famous for its therapeutic natural hot sulphur springs. Spend your evening exploring the lively, colorful streets of Manali Mall Road, perfect for premium shopping, cozy cafe hopping, and picking up unique local souvenirs. Road.'
                ),
                [
                    'Sightseeing Included: Hadimba Temple, Club House, Vashisht Hot Springs, Tibetan Monastery, Manali Mall',
                    'Evening Experience: Bespoke cafe hopping and trout dining recommendations in Old Manali.',
                    'Overnight Stay: Manali (Premium Riverside Luxury Property)',
                    'Meals Included: Breakfast & Premium Buffet Dinner',
                ],
            ),            _day(
                5,
                'SOLANG VALLEY & ATAL TUNNEL EXCURSION',
                (
                    'SNOW ADVENTURE, GLACIERS & THRILLING VISTAS An exhilarating day awaits as you head to Solang Valley, the premier adventure hub of Manali. Take in the breathtaking landscapes and enjoy thrilling activities like paragliding, quad biking, and an open gondola cable car ride. Next, drive through the engineering marvel of the Atal Tunnel to enter the spectacular Lahaul Valley. The snow-covered mountain views here make this a truly unforgettable experience for the whole family.'
                ),
                [
                    'Sightseeing Included: Solang Valley, Atal Tunnel, Sissu Village (Lahaul Valley snow viewpoints).',
                    'Optional Activities: Rohtang Pass excursion (subject to local permissions and extra cost parameters).',
                    'Overnight Stay: Manali (Premium Riverside Luxury Property)',
                    "Meals Included: Breakfast & Multi-cuisine Chef's Special Dinner",
                ],
            ),            _day(
                6,
                'MANALI TO DHARAMSHALA',
                (
                    'TRANSITION TO THE DHAULADHAR RANGE – HIGHWAY SPLENDOUR Enjoy a delicious breakfast before heading to Dharamshala, a spectacular spiritual hill station. Drive past rolling tea gardens, beautiful terraced farms, and historic towns like Palampur. As you approach Dharamshala, the massive, snow-covered peaks of the Dhauladhar range create a stunning backdrop. Check into your luxury resort and spend a peaceful evening relaxing surrounded by deep pine forests.'
                ),
                [
                    'Sightseeing Included: Palampur Tea Gardens view, Baijnath Shiva Temple (historic stone marvel).',
                    'Evening Experience: Leisurely relaxation walk inside a private pine estate with mountain sunset photography.',
                    'Overnight Stay: Dharamshala / McLeodganj (Luxury Valley Resort)',
                    'Meals Included: Breakfast & Authentic Mountain Dinner',
                ],
            ),            _day(
                7,
                'DHARAMSHALA & MCLEODGANJ EXPLORATION',
                (
                    'LITTLE LHASA – MONASTERIES, CULTURE & WATERFALLS Discover the rich culture and stunning landscapes of McLeodganj, the home of His Holiness the Dalai Lama. Visit the serene Tsuglagkhang Complex to experience peaceful Tibetan chanting and spin the sacred prayer wheels. Take a scenic walk down to the beautiful Bhagsunag Waterfall and see the historic St. John in the Wilderness Church. In the evening, explore the local markets for premium singing bowls, fine thangka paintings, and delicious authentic momos. Stadium view.'
                ),
                [
                    'Sightseeing Included: Dalai Lama Temple, Bhagsunag Temple & Waterfall, Dal Lake, St. John Church, Cricket',
                    'Evening Experience: Farewell family dinner gathering with live mountain music at your luxury resort.',
                    'Overnight Stay: Dharamshala / McLeodganj (Luxury Valley Resort)',
                    'Meals Included: Breakfast & Premium Farewell Dinner',
                ],
            ),            _day(
                8,
                'DHARAMSHALA TO DELHI / DEPARTURE',
                (
                    'RETURN WITH UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Enjoy your last mountain breakfast before your luxury vehicle drives you back to Delhi. As you travel down the scenic highways, look back on an incredible journey filled with sweet family bonds and unforgettable memories curated exclusively by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door highway drop-off to Delhi Airport / Railway Station.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Willow Banks /',
                'Himachal Pradesh',
                '07 Nights',
                'Deluxe',
                'similar',
                'Solang Valley Resort /',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Willow Banks / | similar | Solang Valley Resort /',
            ),
            _hotel(
                'Radisson Hotel',
                'Himachal Pradesh',
                '07 Nights',
                'Premium',
                'Shimla / similar',
                'ManuAllaya Resort & Spa /',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Hotel | Shimla / similar | ManuAllaya Resort & Spa /',
            ),
            _hotel(
                'The Cecil - Oberoi /',
                'Himachal Pradesh',
                '07 Nights',
                'Luxury',
                'Similar',
                'The Himalayan (Castle',
                4,
                3,
                description='OPTION 03 – LUXURY: The Cecil - Oberoi / | Similar | The Himalayan (Castle',
            ),
            _hotel(
                'Wildflower Hall',
                'Himachal Pradesh',
                '07 Nights',
                'Ultra Luxury',
                '(Oberoi Resort)',
                'Span Resort & Spa (Elite',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Wildflower Hall | (Oberoi Resort) | Span Resort & Spa (Elite',
            )
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Handpicked hotels as per chosen luxury tier.', 1),
            _inc_included('Luxury Transportation: Private AC Innova Crysta for all transfers, valleys & sightseeing.', 2),
            _inc_included('Curated Meal Plan: Daily lavish breakfasts and multi-cuisine dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated elite guest relationship manager assistance.', 4),
            _inc_included('Welcome Amenities: Personalized welcome kit, mineral water, and dry fruits box.', 5),
            _inc_included('Complimentary Experience: Private bonfire session and Kullu handloom tour entry.', 6),
            _inc_excluded('Airfare / Train tickets to and from New Delhi.', 7),
            _inc_excluded('Monument entry tickets, adventure gear hire, and local ski/paragliding fees.', 8),
            _inc_excluded('Personal expenses such as laundry, phone calls, room heaters, and tipping.', 9),
            _inc_excluded('Rohtang Pass green tax permissions or local taxi union vehicles if enforced. TRAGUIN Luxury Proposal — HP-004 6', 10),
        ],
    )
    return package, itinerary

def build_hp_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-005'
    tour_code = 'TRG-HP-005'
    title = 'Complete Himachal • Grand Alpine Escape'
    duration = '09 Nights / 10 Days'
    slug = 'hp-005-complete-himachal-grand-alpine-escape'
    itin_slug = 'hp-005-complete-himachal-grand-alpine-escape-itinerary'
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
            _ph('Serial code HP-005 | TRAGUIN tour code TRG-HP-005', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Complete', 2),
            _ph('Destinations: Shimla • Manali • Solang Valley • Dharamshala • Dalhousie • Khajjiar', 3),
            _ph('Ideal for: Premium Family Vacations, Honeymooners & Nature Admirers', 4),
            _ph('Best season: March to June (Summer) & October to February (Snow Season)', 5),
            _ph('Starting price: On Request (Premium Bespoke Luxury)', 6),
            _ph('Vehicle / Meals: Private Luxury Innova Crysta / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private family dinner customization featuring authentic Himachali', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked mountain driving routes scheduled to avoid traffic and', 9),
            _ph('Premium Handpicked Hotels: Dedicated rooms selected for their unobstructed panoramic mountain and', 10),
            _ph('Luxury Transportation: Highly trusted, background-verified mountain-expert chauffeurs fluent in local', 11),
            _ph('Advance Bookings: We highly recommend confirming bookings 30-45 days in advance, especially during', 12),
            _ph('the summer and winter snow seasons.', 13)
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
        price_note='On Request (Premium Bespoke Luxury)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Complete Himachal',
        overview="COMPLETE HIMACHAL • GRAND ALPINE ESCAPE Welcome to an extraordinary grand alpine escape designed by TRAGUIN. Embark on the definitive Complete Himachal Family Tour, thoughtfully tailored to let you explore the most iconic destinations in comfort. This premium luxury vacation transports your family through breathtaking landscapes, snow- capped peaks, pine-scented valleys, and fascinating cultural legacies. As your premier travel experts, TRAGUIN transforms this classic circuit into an elite journey filled with premium stays, handpicked hotels, and immersive experiences that promise to create unforgettable memories.\n\nTOUR OVERVIEW\nThis meticulously planned luxury holiday itinerary provides a comprehensive journey across the jewel destinations of Himachal Pradesh. Traveling in a dedicated premium AC luxury transport vehicle with a courteous, experienced mountain chauffeur, your family will enjoy absolute comfort. Featuring premium handpicked hotels and a meal plan complete with lavish daily breakfasts and exquisite dinners, every detail has been refined. From the colonial elegance of Shimla and the dramatic valleys of Manali to the peaceful spiritual atmosphere of Dharamshala and Switzerland-inspired meadows of Khajjiar near Dalhousie, this is the ultimate premium Himachal experience backed by signature TRAGUIN curated experiences and round-the- clock personalized assistance.\n\nWHY BOOK THE BEST HIMACHAL TOUR PACKAGE?\nA true Luxury Himachal Holiday is an elegant collection of crisp mountain air, panoramic viewpoints, and unmatched comfort. Himachal Pradesh remains one of India's top searched destinations, offering incredible diversity for all types of travelers. Whether you are looking for a romantic, picture-perfect Himachal Honeymoon Package or an engaging Himachal Family Tour, this region delivers beautiful settings and unforgettable experiences. The state features renowned top tourist places in Himachal, including Shimla’s iconic Ridge, the bustling Mall Roads, and the adventure-filled heights of Solang Valley and Atal Tunnel in Manali. For travelers seeking deep cultural insights, the peaceful monasteries of Dharamshala and Mcleodganj present a beautiful spiritual escape. Meanwhile, the scenic beauty of Dalhousie and the popular Instagram locations of Khajjiar meadow provide excellent backdrops for family photography. Our customized TRAGUIN Himachal Packages combine scenic luxury with local handicraft shopping, regional culinary highlights, and exclusive experiences, ensuring you enjoy the best time to visit Himachal with absolute peace of mind.",
        seo_title='HP-005 | Complete Himachal | TRAGUIN',
        seo_description='Premium 09 Nights / 10 Days Himachal Pradesh package (HP-005 / TRG-HP-005): Shimla • Manali • Solang Valley • Dharamshala • Dalhousie • Khajjiar with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DELHI TO SHIMLA', 1),
            _ih('Day 02: SHIMLA & KUFRI SIGHTSEEING', 2),
            _ih('Day 03: SHIMLA TO MANALI VIA KULLU VALLEY', 3),
            _ih('Day 04: MANALI LOCAL SIGHTSEEING', 4),
            _ih('Day 05: SOLANG VALLEY & ATAL TUNNEL EXCURSION', 5),
            _ih('Day 06: MANALI TO DHARAMSHALA', 6),
            _ih('Day 07: DHARAMSHALA & MCLEODGANJ SIGHTSEEING', 7),
            _ih('Day 08: DHARAMSHALA TO DALHOUSIE', 8),
            _ih('TRAGUIN Signature Experience: Private family dinner customization featuring authentic Himachali', 9),
            _ih('Curated by TRAGUIN Experts: Handpicked mountain driving routes scheduled to avoid traffic and', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DELHI TO SHIMLA',
                (
                    'ASCENDING THE HILLS TO THE SUMMER CAPITAL Your premium Himachal experience begins with a warm welcome by a private chauffeur at Delhi Airport or Railway Station. Step into your luxury transport vehicle and enjoy a scenic drive towards Shimla, the legendary former summer capital of British India. As you ascend into the Himalayas, watch the changing views transition into lush pine forests. Arrive in Shimla, check into your handpicked premium hotel, and spend a relaxing evening enjoying the clean mountain breeze.'
                ),
                [
                    'Sightseeing Included: Scenic Himalayan foothills drive, Pinjore Gardens en-route (optional time-permitting).',
                    'Evening Experience: Leisurely dinner at your premium resort terrace curated by TRAGUIN experts.',
                    'Overnight Stay: Shimla (Premium / Luxury Resort)',
                    'Meals Included: Welcome Refreshment & Luxury Dinner',
                ],
            ),            _day(
                2,
                'SHIMLA & KUFRI SIGHTSEEING',
                (
                    'COLONIAL CHARM, PANORAMAS & ALPINE MEADOWS After a delicious breakfast, head out for a morning excursion to Kufri, a high-altitude destination renowned for its breathtaking landscapes and panoramic Himalayan views. Enjoy fun pony rides through cedar woods and capture beautiful photos at the Himalayan Nature Park. In the afternoon, return to Shimla for a heritage walk along the iconic Mall Road, the historic Ridge, Christ Church, and the Gaiety Theatre, followed by a visit to the Jakhoo Temple hill.'
                ),
                [
                    'Sightseeing Included: Kufri Alpine Viewpoint, The Ridge, Mall Road, Christ Church, Jakhoo Temple.',
                    'Optional Activities: Traditional local costume photography and premium wood-craft souvenir shopping.',
                    'Overnight Stay: Shimla (Premium / Luxury Resort)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),            _day(
                3,
                'SHIMLA TO MANALI VIA KULLU VALLEY',
                (
                    'DRIVING ALONG THE ROARING BEAS RIVER Depart Shimla on a visually stunning drive to Manali, a true jewel of any complete Himachal sightseeing trip. Follow the winding roads alongside the beautiful Beas River. En route, pass through Mandi and enter the green Kullu Valley. Stop at a premier Kullu shawl weaving factory to observe local artisans and experience the dramatic Pandoh Dam. Arrive in Manali by evening and check into a premium riverside or mountain-view luxury resort.'
                ),
                [
                    'Sightseeing Included: Kullu Valley Drive, Pandoh Dam, Sundernagar Lake, Kullu Shawl Emporiums.',
                    'Evening Experience: Private riverside relaxation and evening bonfire at your handpicked hotel.',
                    'Overnight Stay: Manali (Premium Mountain View Resort)',
                    'Meals Included: Premium Breakfast & Hot Gourmet Dinner',
                ],
            ),            _day(
                4,
                'MANALI LOCAL SIGHTSEEING',
                (
                    'ANCIENT LEGENDS & REFRESHING MOUNTAIN CULTURE Discover the local heritage of Manali today. Visit the 450-year-old Hadimba Devi Temple, beautifully crafted from wood and nestled within dense Dhungri Van Vihar cedar forests. Explore the traditional Vashisht Village, known for its therapeutic natural hot sulphur springs, and visit the serene Tibetan Monastery. Spend your evening exploring Old Manali’s vibrant cafes or shopping for authentic mountain handicrafts along the bustling Mall Road.'
                ),
                [
                    'Sightseeing Included: Hadimba Temple, Vashisht Hot Springs, Club House, Tibetan Monastery, Mall Road.',
                    'Food Suggestions: Try fresh trout fish or artisan wood-fired pizzas in the cafes of Old Manali.',
                    'Overnight Stay: Manali (Premium Mountain View Resort)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),            _day(
                5,
                'SOLANG VALLEY & ATAL TUNNEL EXCURSION',
                (
                    "SNOW FIELDS, ADVENTURE & ENGINEERING MARVELS Today promises an exciting excursion to Solang Valley, a playground for adventure enthusiasts. Enjoy breathtaking landscapes and participate in thrilling optional activities like paragliding, zorbing, and quad biking. Next, pass through the historic Atal Tunnel—the world's longest highway tunnel above 10,000 feet—to experience the stunning, snow-covered mountain vistas of the Lahaul Valley."
                ),
                [
                    'Sightseeing Included: Solang Valley, Atal Tunnel engineering landmark, Sissu Village / Lahaul viewpoints.',
                    'Optional Activities: Cable car rides, snow skiing, paragliding, and high-altitude photography.',
                    'Overnight Stay: Manali (Premium Mountain View Resort)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),            _day(
                6,
                'MANALI TO DHARAMSHALA',
                (
                    'JOURNEY TO THE SPIRITUAL HOME OF THE DALAI LAMA Bid adieu to Manali and drive past lush tea gardens to the peaceful hill station of Dharamshala and Mcleodganj. This beautiful drive reveals the stunning contrast of the rugged Dhauladhar mountain range. Upon arrival, check into your premium luxury stay and immerse yourself in the peaceful ambiance of this spiritual Buddhist community.'
                ),
                [
                    'Sightseeing Included: Palampur Tea Gardens en-route, Baijnath Shiva Temple architectural site.',
                    'Evening Experience: A peaceful stroll around the Dalai Lama Temple complex during evening chants.',
                    'Overnight Stay: Dharamshala / Mcleodganj (Premium Stay)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),            _day(
                7,
                'DHARAMSHALA & MCLEODGANJ SIGHTSEEING',
                (
                    "TIBETAN HERITAGE, CRICKET STADIUMS & WATERFALLS Explore the top tourist places in Dharamshala today. Visit the serene Tsuglagkhang Complex (the official residence of His Holiness the Dalai Lama), Bhagsu Nag Temple, and its refreshing mountain waterfall. Later, capture memorable family photographs at the world's highest international cricket stadium, featuring a spectacular mountain backdrop, and visit the serene St. John in the Wilderness Church."
                ),
                [
                    'Sightseeing Included: Dalai Lama Temple, Bhagsu Waterfall, HPCA Cricket Stadium, Dal Lake, Local Bazaars.',
                    'Shopping: Tibetan singing bowls, prayer flags, rugs, and authentic local tea.',
                    'Overnight Stay: Dharamshala / Mcleodganj (Premium Stay)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),            _day(
                8,
                'DHARAMSHALA TO DALHOUSIE',
                (
                    'TRAVEL TO THE COLONIAL HILL RETREAT Embark on a scenic mountain drive to Dalhousie, a charming hill station established during the British era across five forested hills. The route winds through peaceful valleys and offers majestic views of the Ravi River. Check into your luxury hotel and enjoy an afternoon walking through Subhash Chowk and Gandhi Chowk, admiring the well-preserved colonial architecture.'
                ),
                [
                    "Sightseeing Included: Subhash Chowk, Gandhi Chowk, St. John's & St. Patrick's Historical Churches.",
                    'Evening Experience: Watch a beautiful mountain sunset from the colonial church promenade.',
                    'Overnight Stay: Dalhousie (Premium Luxury Resort)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),            _day(
                9,
                'EXCURSION TO KHAJJIAR',
                (
                    'THE MINI SWITZERLAND OF INDIA Today features a short drive through thick deodar forests to the beautiful meadow of Khajjiar, famously known as the "Mini Switzerland of India." This iconic glade features a serene central lake surrounded by dense pine forests and a striking mountain backdrop, making it a highly popular Instagram location. Enjoy family horseback riding, crisp mountain walks, and memorable photography before returning to Dalhousie for your farewell dinner.'
                ),
                [
                    'Sightseeing Included: Khajjiar Meadow, Khajji Nag Temple, Dainkund Peak panoramic vistas (optional trail).',
                    'Optional Activities: Zorbing on the grass hills, professional paragliding, and pony trails.',
                    'Overnight Stay: Dalhousie (Premium Luxury Resort)',
                    'Meals Included: Premium Breakfast & Custom Celebration Dinner',
                ],
            ),            _day(
                10,
                'DALHOUSIE TO DELHI / DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES Enjoy your last breakfast overlooking the misty valleys. Your private luxury vehicle will safely drive you back to Delhi Airport or Railway Station (or alternative nearby rail hubs like Pathankot on request) for your return journey. Head home carrying sweet family stories and unforgettable memories designed exclusively by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door highway drop-off.',
                    'Meals Included: Lavish Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Willow',
                'Himachal Pradesh',
                '09 Nights',
                'Deluxe',
                'Banks',
                'Lemon Tree',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Willow | Banks | Lemon Tree',
            ),
            _hotel(
                'Radisson Hotel',
                'Himachal Pradesh',
                '09 Nights',
                'Premium',
                'Shimla',
                'ManuAllaya',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Hotel | Shimla | ManuAllaya',
            ),
            _hotel(
                'The Cecil - Oberoi',
                'Himachal Pradesh',
                '09 Nights',
                'Luxury',
                'The Himalayan',
                'Resort',
                4,
                3,
                description='OPTION 03 – LUXURY: The Cecil - Oberoi | The Himalayan | Resort',
            ),
            _hotel(
                'Wildflower Hall',
                'Himachal Pradesh',
                '09 Nights',
                'Ultra Luxury',
                '(Oberoi)',
                'Span Resort &',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Wildflower Hall | (Oberoi) | Span Resort &',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Selected luxury room categories across handpicked hotels.', 1),
            _inc_included('Luxury Transportation: Private AC Innova Crysta for all transfers and sightseeing.', 2),
            _inc_included('Curated Meal Plan: Daily premium buffet breakfasts and dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 personalized assistance from a dedicated tour manager.', 4),
            _inc_included('Welcome Amenities: Customized family travel gift kit and mountain snacks upon arrival.', 5),
            _inc_included('Exclusive Experiences: Private evening bonfire session arranged at your Manali resort.', 6),
            _inc_excluded('Airfare, flight tickets, or interstate rail fares to New Delhi.', 7),
            _inc_excluded('Monument entrance tickets, activity/adventure sports fees, and local guides.', 8),
            _inc_excluded('Personal items such as laundry, phone calls, beverages, and tips.', 9),
            _inc_excluded('Rohtang Pass permit fees (subject to availability and local government rules).', 10),
        ],
    )
    return package, itinerary

def build_hp_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-006'
    tour_code = 'TRG-HIM-006'
    title = 'Romantic Himachal • Love Amidst the Snow-Capped Peaks'
    duration = '05 Nights / 06 Days'
    slug = 'hp-006-romantic-himachal-honeymoon'
    itin_slug = 'hp-006-romantic-himachal-honeymoon-itinerary'
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
            _ph('Serial code HP-006 | TRAGUIN tour code TRG-HIM-006', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Luxury', 2),
            _ph('Destinations: Shimla • Kufri • Manali • Solang Valley', 3),
            _ph('Ideal for: Newlyweds, Couples & Romantic Explorers', 4),
            _ph('Best season: March to June (Pleasant) / November to February (Snowfall)', 5),
            _ph('Starting price: On Request (Premium Honeymoon Luxury)', 6),
            _ph('Vehicle / Meals: Private Luxury Sedan / MAPAI (Breakfast, Dinner & Honeymoon Inclusions)', 7),
            _ph('Route: Scenic Himalayan expressways, Timber Trail viewpoints. Welcome Note: Personalised greeting note and fresh floral arrangement in suite from TRAGUIN. Overnight Stay: Shimla (Premium Luxury Resort) Meals Included: Gourmet Buffet Dinner', 8),
            _ph('TRAGUIN Signature Experience: Private, romantic evening parameters with panoramic photography', 9),
            _ph('Curated by TRAGUIN Experts: Custom routing designed to provide relaxing morning wake-up times and', 10),
            _ph('Premium Handpicked Hotels: Properties specifically verified for maximum honeymoon privacy, premium', 11),
            _ph('Exclusive Recommendations: Access to a curated map of hidden mountain viewpoints and premium', 12),
            _ph('Local Markets & Souvenirs: Stroll along Shimla’s Lakkar Bazaar for handcrafted wooden artifacts, custom interior decor, and fine walnut-wood items. While exploring Manali, shop for authentic hand-woven Pashmina and Kullu shawls, warm tweed winter coats, and colorful local Himachali caps. Cafes & Gastronomy: Relax inside the iconic, cozy wooden mountain cafes of Old Manali to sample authentic apple crumbles, artisanal wood-fired pizzas, and locally brewed mountain herbal infusions.', 13),
            _ph('Advance Booking Suggestions: We strongly advise completing reservations 45 days in advance during', 14)
        ],
        moods=['Romantic', 'Luxury', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Honeymoon Luxury)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Romantic Himachal',
        overview="ROMANTIC HIMACHAL • LOVE AMIDST THE SNOW-CAPPED PEAKS Welcome to a timeless fairy-tale retreat curated exclusively by TRAGUIN. Embark on the ultimate Himachal Honeymoon Package crafted meticulously to blend romantic seclusion with unparalleled alpine grandeur. As your elite travel consultants, TRAGUIN elevates your journey into a luxury holiday marked by handpicked hotels, immersive experiences, and heartwarming moments. From walking hand-in-hand along the mist-covered Ridge of Shimla to witnessing the sheer, pristine white magic of Solang Valley in Manali, every itinerary milestone is hand-tailored to foster unforgettable memories for a lifetime.\n\nTOUR OVERVIEW\nThis bespoke romantic getaway delivers a premium Himachal experience, taking couples through the majestic evergreen pine trails of Shimla and the dramatic, snow-kissed alpine borders of Manali. Travel across spectacular mountain passes in a dedicated luxury vehicle guided by a polished, professional private chauffeur. Enjoy handpicked premium stays boasting private valley views, alongside curated dining options that feature candlelit setups and traditional delicacies. The entire itinerary is layered with the signature touch of TRAGUIN curated experiences—ensuring a perfectly seamless, romantic luxury getaway from day one.\n\nWHY CHOOSE THE BEST HIMACHAL HONEYMOON PACKAGE?\nWhen organizing an authentic Luxury Himachal Holiday, couples demand the perfect mixture of scenic beauty, privacy, and premium comfort. Himachal Pradesh stands as one of the most romantic destinations across the globe, housing iconic attractions that capture the heart. From the architectural legacy of Shimla's Viceregal Lodge to the deep, swirling waters of the Beas River in Manali, this destination remains a top tourist place in Himachal for lovers. Our meticulously custom-crafted Himachal Honeymoon Package and Himachal Family Tour architectures reveal highly popular Instagram locations, including the snowy ridges of Kufri, the traditional wooden structures of Old Manali, and the breathtaking vistas of Solang Valley. Indulge in local market shopping, cherish local culinary traditions, or capture stunning photography against dramatic valleys. Choosing our signature TRAGUIN Himachal Packages ensures high-end custom amenities, elite room selections, and exclusive experiences designed around the absolute best time to visit Himachal.",
        seo_title='HP-006 | Romantic Himachal | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Himachal Pradesh package (HP-006 / TRG-HIM-006): Shimla • Kufri • Manali • Solang Valley with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DELHI TO SHIMLA', 1),
            _ih('Day 02: SHIMLA & KUFRI EXCURSION', 2),
            _ih('Day 03: SHIMLA TO MANALI VIA KULLU VALLEY', 3),
            _ih('Day 04: MANALI SOLANG VALLEY EXCURSION', 4),
            _ih('Day 05: LOCAL MANALI CULTURAL SIGHTSEEING', 5),
            _ih('Day 06: MANALI TO DELHI / DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private, romantic evening parameters with panoramic photography', 7),
            _ih('Curated by TRAGUIN Experts: Custom routing designed to provide relaxing morning wake-up times and', 8),
            _ih('Premium Handpicked Hotels: Properties specifically verified for maximum honeymoon privacy, premium', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DELHI TO SHIMLA',
                (
                    'ASCENDING TO THE QUEEN OF HILL STATIONS Your premium Himachal experience initiates with a VIP reception at New Delhi Airport/Railway Station by your private executive chauffeur. Board your luxury sedan and begin a highly scenic drive ascending into the lower Shivalik ranges. Witness magnificent winding mountain views and misty landscapes as you approach Shimla. Check into your custom handpicked premium resort featuring individual valley views. Relax with a complimentary welcome drink and enjoy a lavish dinner.'
                ),
                [
                    'Sightseeing En-route: Scenic Himalayan expressways, Timber Trail viewpoints.',
                    'Welcome Note: Personalised greeting note and fresh floral arrangement in suite from TRAGUIN.',
                    'Overnight Stay: Shimla (Premium Luxury Resort)',
                    'Meals Included: Gourmet Buffet Dinner',
                ],
            ),            _day(
                2,
                'SHIMLA & KUFRI EXCURSION',
                (
                    'ROMANCE AMIDST THE PINE FORESTS & MISTY TRAILS Savor a delightful breakfast before heading to Kufri, an exceptional destination celebrated for its breathtaking landscapes and serene pine trails. Walk together through nature paths, capture panoramic views of the eternal snow-capped peaks, and opt for a classic mountain pony ride. In the afternoon, return to Shimla to explore its iconic attractions, including the historic Mall Road, Christ Church, and The Ridge. Conclude your evening with an intimate, private candlelit dinner carefully arranged by TRAGUIN experts. Shimla Sightseeing: Kufri Nature Park, Mall Road, Scandal Point, Christ Church, Jakhoo Temple path.'
                ),
                [
                    'Evening Experience: Exclusive Candlelit Dinner with a complimentary celebratory honeymoon cake.',
                    'Overnight Stay: Shimla (Premium Luxury Resort)',
                    'Meals Included: Breakfast & Special Honeymoon Dinner',
                ],
            ),            _day(
                3,
                'SHIMLA TO MANALI VIA KULLU VALLEY',
                (
                    'SCENIC RIVER VISTAS & DRIVE THROUGH THE MAJESTIC CANYON Depart Shimla after breakfast for an immersive overland drive to Manali, the crown jewel of your Romantic Himachal journey. Wind along the stunning Beas River valley, passing the famous Kullu town. En-route, pause at breathtaking photography points overlooking cascading river rapids and mist-layered apple orchards. Arrive at your ultra-premium luxury resort in Manali by evening, checking into a master suite facing the river.'
                ),
                [
                    'Sightseeing En-route: Pandoh Dam, Hanogi Mata Temple vista, Kullu Valley shawl weaving ateliers.',
                    'Local Experience: Guided stopover at a traditional Kullu heritage artisan workshop.',
                    'Overnight Stay: Manali (Luxury Valley-Facing Resort)',
                    'Meals Included: Premium Breakfast & Luxury Buffet Dinner',
                ],
            ),            _day(
                4,
                'MANALI SOLANG VALLEY EXCURSION',
                (
                    'SNOW FIELDS, ADVENTURE & ALPINE SPLENDOUR Wake up to magnificent morning mountain views before embarking on an excursion to Solang Valley, a highly popular Instagram location famed for adventure and jaw-dropping snow peaks. For couples seeking a touch of thrill, partake in optional paragliding over the valleys, zorbing, or a cable car ride offering an immersive view of the glaciers. Walk through pristine high-altitude meadows together, capturing unforgettable memories against the alpine skyline. permission).'
                ),
                [
                    'Sightseeing Included: Solang Valley meadows, Snow-view viewpoints, Atal Tunnel entrance portal (subject to',
                    'Optional Activities: Tandem paragliding, Quad biking, Snow snowboarding (winter months).',
                    'Overnight Stay: Manali (Luxury Valley-Facing Resort)',
                    'Meals Included: Premium Breakfast & Authentic Himachali-infused Dinner',
                ],
            ),            _day(
                5,
                'LOCAL MANALI CULTURAL SIGHTSEEING',
                (
                    'WOODEN HERITAGE, CAFE CULTURE & SUNSET PROMENADES Dedicate your day to exploring the iconic local attractions of Manali. Visit the ancient, wooden-crafted Hadimba Devi Temple, tucked deep inside the towering Dhungri Van Vihar pine sanctuary. Stroll through the quaint lanes of Old Manali, exploring eclectic cafes and artisanal shopping alleys. Spend a relaxing afternoon walking around Vashisht Village to experience its therapeutic hot sulfur springs before enjoying a romantic evening by the riverside.'
                ),
                [
                    'Sightseeing Included: Hadimba Temple, Club House, Vashisht Hot Springs, Tibetan Monastery, Old Manali lanes.',
                    'Evening Experience: Private almond-milk and bedside floral presentation setup for newlyweds.',
                    'Overnight Stay: Manali (Luxury Valley-Facing Resort)',
                    'Meals Included: Breakfast & Premium Farewell Dinner',
                ],
            ),            _day(
                6,
                'MANALI TO DELHI / DEPARTURE',
                (
                    'RETURNING HOME WITH CHERISHED MOMENTS Conclude your dream vacation with a lavish breakfast overlooking the valley mist. Your premium vehicle will smoothly navigate the descent back to New Delhi Airport or Railway Station for your flight home. Bid farewell to the spectacular hills, carrying beautifully knitted bonds and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door highway drop-off to Delhi.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Willow Banks / similar',
                'Himachal Pradesh',
                '05 Nights',
                'Deluxe',
                'Solang Valley Resort (Deluxe) /',
                'similar',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Willow Banks / similar | Solang Valley Resort (Deluxe) / | similar',
            ),
            _hotel(
                'The Orchid Hotel / Wildflower Hall',
                'Himachal Pradesh',
                '05 Nights',
                'Luxury',
                '(Classic)',
                'Span Resort & Spa / The Himalayan',
                4,
                3,
                description='OPTION 03 – LUXURY: The Orchid Hotel / Wildflower Hall | (Classic) | Span Resort & Spa / The Himalayan',
            ),
            _hotel(
                'Wildflower Hall, An Oberoi Resort',
                'Himachal Pradesh',
                '05 Nights',
                'Ultra Luxury',
                '(Executive Suite)',
                'The Oberoi Sukhvilas / VVIP River',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Wildflower Hall, An Oberoi Resort | (Executive Suite) | The Oberoi Sukhvilas / VVIP River',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Handpicked romantic resort accommodation.', 1),
            _inc_included('Luxury Transportation: Private Chauffeur- driven executive sedan for the entire tour.', 2),
            _inc_included('Curated Meal Plan: Daily elaborate breakfasts and gourmet dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 priority concierge and guest relationship assistance.', 4),
            _inc_included('Honeymoon Delights: 1x Candlelit dinner, 1x Premium cake, and floral bed setup.', 5),
            _inc_included('Welcome Amenities: Personalized arrival refreshment kit and traditional welcome.', 6),
            _inc_excluded('Domestic/International Airfare or train tickets.', 7),
            _inc_excluded('Rohtang Pass permit fees or shuttle costs (if applicable).', 8),
            _inc_excluded('Personal expenses such as laundry, phone bills, premium drinks, and tips.', 9),
            _inc_excluded('Adventure sport entry tickets, camera passes, and local tour guides.', 10),
        ],
    )
    return package, itinerary

def build_hp_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-007'
    tour_code = 'TRG-HP-HON-007'
    title = 'Snow Romance Manali Honeymoon Special'
    duration = '04 Nights / 05 Days'
    slug = 'hp-007-snow-romance-manali-honeymoon'
    itin_slug = 'hp-007-snow-romance-manali-honeymoon-itinerary'
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
            _ph('Serial code HP-007 | TRAGUIN tour code TRG-HP-HON-007', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Premium', 2),
            _ph('Destinations: Manali • Solang Valley • Rohtang Pass • Kullu', 3),
            _ph('Ideal for: Newlyweds, Couples & Luxury Romantics', 4),
            _ph('Best season: October to June (Snow Season: Dec to Feb)', 5),
            _ph('Starting price: On Request (Bespoke Luxury Customization)', 6),
            _ph('Vehicle / Meals: Private Luxury Sedan / SUV • Breakfast & Dinner', 7),
            _ph('TRAGUIN Signature Experience: Private riverside sunset tea service arranged away from typical crowds.', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked mountain itineraries structured with optimal pacing to ensure', 9),
            _ph('Premium Handpicked Hotels: Properties thoroughly verified for elite security, premium thermal insulation,', 10),
            _ph('Exclusive Recommendations: Access list to the most exclusive hidden dining spots and charming cafes', 11),
            _ph('Local Alpine Markets: Discover the Mall Road and Manu Market to pick up gorgeous authentic hand-woven Kullu shawls, soft pashmina stoles, handcrafted wooden jewelry boxes, and pure organic mountain honey. Food & Cafe Guide: Sip freshly brewed apple cider drinks, taste fresh wood-fired mountain trout fish delicacies, and try artisanal chocolate fondues at the romantic river-facing decks of Old Manali.', 12),
            _ph('Rohtang Guidelines: Trips to Rohtang Pass strictly depend on government weather permissions and daily', 13)
        ],
        moods=['Romantic', 'Luxury', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Bespoke Luxury Customization)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Snow Romance Manali Honeymoon Special',
        overview="SNOW ROMANCE MANALI HONEYMOON SPECIAL Welcome to an extraordinary romantic odyssey beautifully tailored by TRAGUIN. This bespoke Himachal Honeymoon Package is masterfully curated to guide couples into the heart of breathtaking landscapes, majestic snow-clad summits, and cozy valleys. Designed specifically as a premium destination experience, your journey blends exquisite intimacy with the timeless mountain charm of Manali. From wake-up calls overlooking pristine panoramic peaks to romantic twilight strolls along mist-kissed forests, let TRAGUIN frame your new beginnings into a gallery of unforgettable memories.\n\nTOUR OVERVIEW\nYour Snow Romance Manali itinerary represents the ultimate standard for a Luxury Himachal Holiday. Travel in absolute style and exclusivity with your private luxury vehicle, handled by a professional chauffeur-driven guide attentive to your absolute privacy. Rest every night in handpicked hotels known for exceptional mountain views, specialized honeymoon amenities, and warm Himachali hospitality. This exclusive package features an optimized route connecting the majestic heights of Solang Valley and Rohtang Pass down to the serene banks of the Beas River in Kullu. Complete with a TRAGUIN curated experience note, your trip includes beautifully styled candlelight dinners, floral bedroom styling, and delightful culinary surprises along the way.\n\nWHY BOOK THE BEST HIMACHAL HONEYMOON PACKAGE?\nHimachal Pradesh remains the undisputed crown jewel of India's mountain destinations, making a Luxury Himachal Holiday the top choice for couples globally. The high alpine charm of Manali offers an unmatchable setting for a Himachal Honeymoon Package, offering a stunning mix of pristine evergreen forests, gushing rivers, and sub-zero winter wonderlands. It is widely considered one of the top tourist places in Himachal to discover true solace, world-class adventure sports, and sophisticated alpine luxury. Couples booking our signature Himachal Family Tour and couple itineraries gain seamless access to the most popular Instagram locations—including the suspension bridges over the Beas River, the snow slopes of Solang, and the traditional architecture of Old Manali. Whether you are hunting for local woodcraft shopping, relaxing inside intimate cafes, or embarking on an adventurous snow scooter ride, the TRAGUIN Himachal Packages guarantee premium stays, expert travel consultants at your side, and curated exclusive experiences during the absolute best time to visit Himachal.",
        seo_title='HP-007 | Snow Romance Manali Honeymoon Special | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Himachal Pradesh package (HP-007 / TRG-HP-HON-007): Manali • Solang Valley • Rohtang Pass • Kullu with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN MANALI', 1),
            _ih('Day 02: MANALI LOCAL SIGHTSEEING', 2),
            _ih('Day 03: SOLANG VALLEY & ROHTANG PASS EXCURSION', 3),
            _ih('Day 04: MANALI TO KULLU VALLEY EXCURSION', 4),
            _ih('Day 05: MANALI TO DEPARTURE GATEWAY', 5),
            _ih('TRAGUIN Signature Experience: Private riverside sunset tea service arranged away from typical crowds.', 6),
            _ih('Curated by TRAGUIN Experts: Handpicked mountain itineraries structured with optimal pacing to ensure', 7),
            _ih('Premium Handpicked Hotels: Properties thoroughly verified for elite security, premium thermal insulation,', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN MANALI',
                (
                    'GATEWAY TO THE ALPS – LUXURY CHECK-IN & RIVER RESORT PRIVACY Your premium Himachal experience blooms the moment you land at Bhuntar Airport or reach the Chandigarh gateway. Your dedicated private luxury transport escorts you along the scenic highway wrapped by the Beas River. Arrive in Manali, check into your ultra-luxury handpicked resort, and discover a beautifully styled bedroom welcoming you. Spend your afternoon relaxing or taking an intimate walk through the cedar-scented trails of Van Vihar. experts.'
                ),
                [
                    'Sightseeing Included: Van Vihar Forest Trail, Private riverside boardwalk stroll.',
                    'Evening Experience: A private, intimate candlelight dinner with a custom celebratory cake curated by TRAGUIN',
                    'Overnight Stay: Manali (Premium Luxury River View Resort)',
                    'Meals Included: Welcome Libation & Curated Honeymoon Dinner',
                ],
            ),            _day(
                2,
                'MANALI LOCAL SIGHTSEEING',
                (
                    "CULTURE, CAFES & ARCHITECTURAL HERITAGE IN OLD MANALI Savor a lazy, late breakfast before exploring the finest Manali Sightseeing landmarks. Pay a visit to the historic 450-year-old wooden Hadimba Devi Temple, beautifully enclosed within soaring deodar forests. Afterward, head to the Vashisht Hot Springs to experience their natural therapeutic warmth. Spend your afternoon wandering the cobblestone streets of Old Manali, popping into bohemian cafes, shopping for artistic rugs, and capturing timeless couples' portraits at popular Instagram locations."
                ),
                [
                    'Sightseeing Included: Hadimba Temple, Vashisht Springs, Club House, Old Manali Cafes.',
                    'Optional Activities: Artisanal cafe hopper trail with local live acoustic Himachali music performances.',
                    'Overnight Stay: Manali Premium Luxury Resort',
                    'Meals Included: Premium Breakfast & Multi-cuisine Dinner',
                ],
            ),            _day(
                3,
                'SOLANG VALLEY & ROHTANG PASS EXCURSION',
                (
                    'THE GLACIAL WONDERLAND – SNOW ROMANCE & HIGH ADVENTURE Prepare for an exhilarating day witnessing the absolute scenic beauty of Solang Valley and the mighty Rohtang Pass (subject to weather & permit parameters). Marvel at the majestic, unending blanket of snow. This alpine wonderland offers thrilling premium experiences like tandem paragliding, snow-scooter safaris, and skiing down soft snowy slopes. Hold hands and take in the spectacular, panoramic vistas of the Pir Panjal mountain range.'
                ),
                [
                    'Sightseeing Included: Solang Valley Snowy Slopes, Atal Tunnel approach, Rohtang High Altitude viewpoints.',
                    'Evening Experience: Cozy evening lounge session at the resort with a warming private bonfire setting.',
                    'Overnight Stay: Manali Premium Luxury Resort',
                    'Meals Included: Glacial Buffet Breakfast & Evening Dinner',
                ],
            ),            _day(
                4,
                'MANALI TO KULLU VALLEY EXCURSION',
                (
                    'PINE-SHERBET VALLEYS, SOUVENIRS & SHIVALIK VISTAS Embark on a beautiful day trip down the valley to Kullu, a region renowned for its wide river meadows and rich handicraft heritage. Tour the authentic local handloom cooperatives where iconic Kullu shawls are masterfully woven. Adventure-loving couples can choose to enjoy a thrilling river rafting experience over the clear waters of the Beas River before enjoying a peaceful riverside picnic lunch.'
                ),
                [
                    'Sightseeing Included: Kullu Valley Meadows, Angora Shawl Weaving Industry, Kasol/Manikaran overlook option.',
                    'Optional Activities: White Water Rafting (Grade II/III rapids) with professional safety crews.',
                    'Overnight Stay: Manali Premium Luxury Resort',
                    'Meals Included: Breakfast & Festive Fare Farewell Dinner',
                ],
            ),            _day(
                5,
                'MANALI TO DEPARTURE GATEWAY',
                (
                    'ETERNAL MEMORIES BEYOND DESTINATIONS Relish your final lavish breakfast overlooking the morning mist rising off the valley pine trees. Complete your check-out process as your private luxury transport prepares to drive you safely back to your departure airport or railway terminus. Return home with a heart full of joy, newfound promises, and unforgettable memories custom crafted by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury highway transit drop-off to station / airport.',
                    'Meals Included: Gourmet Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Solang Valley Resort / Hotel',
                'Himachal Pradesh',
                '04 Nights',
                'Deluxe',
                'River Crescent',
                'Deluxe Valley View',
                4,
                1,
                description='OPTION 01 – DELUXE: Solang Valley Resort / Hotel | River Crescent | Deluxe Valley View',
            ),
            _hotel(
                'Manuallaya Resort & Spa /',
                'Himachal Pradesh',
                '04 Nights',
                'Premium',
                'Golden Tulip',
                'Premium Balcony',
                4,
                2,
                description='OPTION 02 – PREMIUM: Manuallaya Resort & Spa / | Golden Tulip | Premium Balcony',
            ),
            _hotel(
                'The Himalayan (Castle Resort)',
                'Himachal Pradesh',
                '04 Nights',
                'Luxury',
                '/ Bookmark Resort',
                'Grand Royal',
                4,
                3,
                description='OPTION 03 – LUXURY: The Himalayan (Castle Resort) | / Bookmark Resort | Grand Royal',
            ),
            _hotel(
                'The Oberoi Cecil Shimla combo',
                'Himachal Pradesh',
                '04 Nights',
                'Ultra Luxury',
                '/ Span Resort & Spa',
                'Elite Riverside',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Oberoi Cecil Shimla combo | / Span Resort & Spa | Elite Riverside',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 04 Nights accommodation in handpicked romantic luxury properties.', 1),
            _inc_included('Luxury Transportation: Chauffeur-driven, private elite sedan/SUV for seamless sightseeing.', 2),
            _inc_included('Curated Meal Plan: Lavish daily breakfast arrays and customized five-course dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated travel consultant VIP assistance on-call.', 4),
            _inc_included('Honeymoon Privileges: Premium almond milk nightly, customized room floral layout, and a celebratory cake.', 5),
            _inc_included('Taxes & Logistics: Comprehensive toll fees, parking permits, and driver allowances included.', 6),
            _inc_excluded('Air tickets or train ticket fees to the state gateway destinations.', 7),
            _inc_excluded('Rohtang Pass special NGT green permit costs or local shuttle transit fees.', 8),
            _inc_excluded('Personal expenses such as laundry services, phone bills, premium alcohol, and gratuities.', 9),
            _inc_excluded('Optional high-adventure sport booking charges (Paragliding, River Rafting, Zorbing). TRAGUIN Premium Luxury Proposal • HP-007 5', 10),
        ],
    )
    return package, itinerary

def build_hp_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-008'
    tour_code = 'TRG-HIM-008'
    title = 'Luxury Manali Escape • Romance Amidst the Clouds'
    duration = '05 Nights / 06 Days'
    slug = 'hp-008-luxury-manali-escape-romance-amidst-the-clouds'
    itin_slug = 'hp-008-luxury-manali-escape-romance-amidst-the-clouds-itinerary'
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
            _ph('Serial code HP-008 | TRAGUIN tour code TRG-HIM-008', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Luxury Honeymoon', 2),
            _ph('Destinations: Manali • Solang Valley • Atal Tunnel • Sissu (Lahaul Value) • Kasol (Optional)', 3),
            _ph('Ideal for: Newlyweds, Romance Seekers & Luxury Explorers', 4),
            _ph('Best season: March to June (Pleasant) / November to February (Snowfall)', 5),
            _ph('Starting price: On Request (Premium Honeymoon Customised)', 6),
            _ph('Vehicle / Meals: Private Luxury Sedan / MAPAI with Honeymoon Inclusions', 7),
            _ph('TRAGUIN Signature Experience: Private roadside picnic setup with hot mountain tea during your Lahaul', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked romantic routes that balance scenic drives with intimate,', 9),
            _ph('Premium Handpicked Hotels: Accommodations selected strictly based on premium safety standards,', 10),
            _ph('Luxury Transportation: Expert hill drivers ensuring elite comfort and safety across mountain passes.', 11),
            _ph('Local Markets & Souvenirs: Explore the Mall Road to find authentic, hand-woven Kullu shawls, warm pashminas, pure wooden artifacts, and traditional Himachali caps as beautiful keepsakes of your trip. Cafes & Food: Old Manali features cozy, atmospheric wooden cafes offering authentic Italian wood-fired pizzas, trout fish delicacies, and freshly brewed mountain coffees with live acoustic music.', 12),
            _ph('Weather Notes: Heavy winter months (Dec-Feb) bring thick snow; please carry heavy woolens. Summer', 13)
        ],
        moods=['Romantic', 'Luxury', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Honeymoon Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Luxury Manali Escape',
        overview='LUXURY MANALI ESCAPE • ROMANCE AMIDST THE CLOUDS Welcome to an ethereal romantic getaway curated exclusively by TRAGUIN. Embark on the ultimate Himachal Honeymoon Package, meticulously crafted to showcase the breathtaking landscapes, snow- capped peaks, and mist-laden pine forests of Manali. As your dedicated luxury travel consultants, TRAGUIN delivers a highly customized experience filled with handpicked hotels, intimate candlelight moments, and premium comfort. Let the scenic beauty of the Beas River and the dramatic mountain vistas form the backdrop of your romantic journey, creating sweet unforgettable memories that last a lifetime.\n\nTOUR OVERVIEW\nThis bespoke luxury holiday package is engineered specifically for couples who seek a romantic and immersive experience in the heart of the Himalayas. Travelling in a completely private premium AC vehicle with a highly professional, well-versed local chauffeur, your itinerary balances leisure with exploration. Enjoy a tailored meal plan featuring decadent daily breakfasts and personalized dinners, along with special honeymoon add-ons like flower bed decorations, a custom wedding cake, and candle-lit dining. Every aspect features the distinct TRAGUIN curated experience note, guaranteeing high-end hospitality and round-the- clock peace of mind.\n\nWHY CHOOSE THE BEST HIMACHAL TOUR PACKAGE?\nWhen planning a Luxury Himachal Holiday, couples look for a blend of high-altitude thrill, untouched nature, and quiet privacy. Manali stands out as the crown jewel of Northern India, making a Manali Honeymoon Package the absolute dream choice for newlyweds. From exploring iconic attractions like the historic Hadimba Temple and Vashisht Hot Springs to seeking high-octane adventure at Solang Valley, Manali sightseeing offers an unmatched experience. Our tailored Himachal Family Tour and romantic packages bring you closer to popular Instagram locations like the engineering marvel of the Atal Tunnel and the surreal snowscapes of Sissu in Lahaul Valley. Indulge in local handicraft shopping at the Mall Road, relish authentic Himachali delicacies, or experience the pure bliss of a riverside café in Old Manali. Our signature TRAGUIN Himachal Packages combine exclusive experiences with premium stays, offering you the absolute best time to visit Himachal with zero hassle.',
        seo_title='HP-008 | Luxury Manali Escape | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Himachal Pradesh package (HP-008 / TRG-HIM-008): Manali • Solang Valley • Atal Tunnel • Sissu (Lahaul Value) • Kasol (Optional) with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN MANALI', 1),
            _ih('Day 02: LOCAL MANALI SIGHTSEEING', 2),
            _ih('Day 03: SOLANG VALLEY ADVENTURE EXCURSION', 3),
            _ih('Day 04: ATAL TUNNEL & SISSU EXCURSION', 4),
            _ih('Day 05: EXCURSION TO NAGGAR CASTLE', 5),
            _ih('Day 06: MANALI TO DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private roadside picnic setup with hot mountain tea during your Lahaul', 7),
            _ih('Curated by TRAGUIN Experts: Handpicked romantic routes that balance scenic drives with intimate,', 8),
            _ih('Premium Handpicked Hotels: Accommodations selected strictly based on premium safety standards,', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN MANALI',
                (
                    'WELCOME TO THE VALLEY OF GODS – ROMANTIC RIVERSIDE CHECK-IN Your premium Himachal experience begins with a warm greeting at Bhuntar Airport or Chandigarh station by your private luxury transport chauffeur. Embark on a breathtakingly scenic drive winding alongside the gushing Beas River. Upon arriving in Manali, check into your handpicked premium luxury resort. Enjoy a special welcome amenity kit. The evening is yours to relax or stroll hand-in-hand through the local pathways, enjoying the crisp mountain air.'
                ),
                [
                    'Sightseeing Included: Scenic Beas River valley drive, Riverside resort relaxation.',
                    'Evening Experience: Honeymoon Special: Custom welcome cake and a beautifully decorated room.',
                    'Overnight Stay: Manali (Premium Mountain View Luxury Resort)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),            _day(
                2,
                'LOCAL MANALI SIGHTSEEING',
                (
                    'CULTURE, HERITAGE & OLD WORLD ROMANCE After a leisurely lavish breakfast, step out for an enchanting local Manali sightseeing tour. Visit the iconic 16th- century Hadimba Temple, tucked away amidst giant deodar forests. Explore the mystical Vashisht Village, famous for its natural therapeutic sulfur hot springs. Later in the afternoon, wander through the quaint cafes and popular Instagram locations of Old Manali before concluding your evening with an upscale shopping experience at the Mall Road.'
                ),
                [
                    'Sightseeing Included: Hadimba Temple, Ghatotkach Tree Temple, Vashisht Hot Springs, Club House, Mall Road.',
                    'Evening Experience: Bespoke intimate candle-lit dinner with a premium menu curated by TRAGUIN experts.',
                    'Overnight Stay: Manali (Premium Mountain View Luxury Resort)',
                    'Meals Included: Premium Breakfast & Romantic Candle-lit Dinner',
                ],
            ),            _day(
                3,
                'SOLANG VALLEY ADVENTURE EXCURSION',
                (
                    'THRILLING LANDSCAPES & HIGH-ALTITUDE ROMANCE Wake up to a pristine mountain sunrise and head towards Solang Valley, famed for its breathtaking landscapes and adrenaline-pumping activities. Take a romantic ropeway ride up to Mount Phatru to enjoy panoramic vistas of snow-covered peaks. Couples can opt for immersive experiences like paragliding together over the valley, quad biking, or zorbing down lush green slopes.'
                ),
                [
                    'Sightseeing Included: Solang Valley viewpoints, Anjani Mahadev track path (seasonal).',
                    'Optional Activities: Tandem paragliding, snow skiing, open-air mountain photography session.',
                    'Overnight Stay: Manali (Premium Mountain View Luxury Resort)',
                    'Meals Included: Premium Breakfast & Multi-cuisine Dinner',
                ],
            ),            _day(
                4,
                'ATAL TUNNEL & SISSU EXCURSION',
                (
                    'CROSSING THE GREATER HIMALAYAS INTO LAHAUL VALLEY Today brings a true highlight of your luxury Himachal holiday. Drive through the world-famous Atal Tunnel, an engineering marvel spanning over 9 kilometers beneath the Rohtang Pass. As you exit into Lahaul Valley, marvel at the sudden transformation into a dramatic, rugged mountain wilderness. Arrive at Sissu village, featuring the majestic Sissu Waterfall and incredible snow-globe vistas. It is the perfect photography point for creating lifelong memories.'
                ),
                [
                    'Sightseeing Included: Atal Tunnel, Sissu Village, Sissu Waterfall, Chandra River banks.',
                    'Evening Experience: Warm traditional Himachali hot beverage service overlooking the glaciers.',
                    'Overnight Stay: Manali (Premium Mountain View Luxury Resort)',
                    'Meals Included: Premium Breakfast & Gourmet Dinner',
                ],
            ),            _day(
                5,
                'EXCURSION TO NAGGAR CASTLE',
                (
                    'ROYAL HERITAGE & ARTISTIC SERENITY Embark on a quiet morning drive to the historic town of Naggar, the ancient capital of Kullu. Tour the beautiful Naggar Castle, a magnificent timber-and-stone palace showcasing traditional Kathkuni architecture. Walk through the Roerich Art Gallery to admire masterfully preserved Himalayan landscapes on canvas. Spend a relaxed afternoon inside an aesthetic wood-fired pizzeria overlooking terraced step orchards.'
                ),
                [
                    'Sightseeing Included: Naggar Castle heritage walk, Nicholas Roerich Art Gallery, Tripura Sundari Temple.',
                    'Optional Activities: Traditional attire couple dress-up photography session inside the castle.',
                    'Overnight Stay: Manali (Premium Mountain View Luxury Resort)',
                    'Meals Included: Breakfast & Farewell Gala Dinner',
                ],
            ),            _day(
                6,
                'MANALI TO DEPARTURE',
                (
                    'FAREWELL TO THE HILLS – MEMORIES BEYOND DESTINATIONS Savor your last lavish breakfast overlooking the morning mist rising from the deodar forests. Pack your bags and board your private luxury vehicle as your chauffeur guides you smoothly back down the valley towards Bhuntar Airport or Chandigarh station for your return journey. Head home carrying a heart full of romance and unforgettable memories designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury station or airport drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Solang Valley Resort / Golden',
                'Himachal Pradesh',
                '05 Nights',
                'Deluxe',
                'Tulip / similar',
                'Deluxe Valley View Room',
                4,
                1,
                description='OPTION 01 – DELUXE: Solang Valley Resort / Golden | Tulip / similar | Deluxe Valley View Room',
            ),
            _hotel(
                'The Grand Welcome / Manu',
                'Himachal Pradesh',
                '05 Nights',
                'Premium',
                'Allaya / similar',
                'Premium Balcony Room',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Grand Welcome / Manu | Allaya / similar | Premium Balcony Room',
            ),
            _hotel(
                'Span Resort & Spa / Baragarh',
                'Himachal Pradesh',
                '05 Nights',
                'Luxury',
                'Resort & Spa',
                'Luxury River Facing Suite',
                4,
                3,
                description='OPTION 03 – LUXURY: Span Resort & Spa / Baragarh | Resort & Spa | Luxury River Facing Suite',
            ),
            _hotel(
                'The Khyber / Wildflower Hall',
                'Himachal Pradesh',
                '05 Nights',
                'Ultra Luxury',
                'style luxury private chalet',
                'VVIP Royal Panoramic',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Khyber / Wildflower Hall | style luxury private chalet | VVIP Royal Panoramic',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 05 Nights in handpicked romantic luxury properties.', 1),
            _inc_included('Luxury Transportation: Private dedicated sedan for all point-to-point sightseeing.', 2),
            _inc_included('Curated Meal Plan: Daily premium buffet breakfast and gourmet dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 personalized concierge and emergency travel assistance.', 4),
            _inc_included('Honeymoon Privileges: Candle-lit dining setup, floral bedding art, and custom cake.', 5),
            _inc_included('Exclusive Experiences: High-altitude tunnel access and guided village walks.', 6),
            _inc_excluded('Airfare, flight tickets, or long-distance train travel.', 7),
            _inc_excluded('Adventure sport fees (Paragliding, skiing, zorbing charges).', 8),
            _inc_excluded('Monument entry tickets, professional guide fees, camera permits.', 9),
            _inc_excluded('Personal expenses such as laundry, phone calls, or tips. TRAGUIN Premium Luxury Itinerary — HP-008 5', 10),
        ],
    )
    return package, itinerary

def build_hp_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-009'
    tour_code = 'TRG-HIM-009'
    title = 'Girls Trip Manali • Wanderlust, Luxury & Sisterhood'
    duration = '04 Nights / 05 Days'
    slug = 'hp-009-girls-trip-manali'
    itin_slug = 'hp-009-girls-trip-manali-itinerary'
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
            _ph('Serial code HP-009 | TRAGUIN tour code TRG-HIM-009', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Female Only /', 2),
            _ph('Destinations: Manali • Solang Valley • Atal Tunnel • Old Manali • Jogini Waterfalls', 3),
            _ph('Ideal for: Girlfriends, Solo Female Groups & Women Travelers', 4),
            _ph('Best season: March to June & October to February', 5),
            _ph('Starting price: On Request (Premium Girls Special Customised)', 6),
            _ph('Vehicle / Meals: Private Premium SUV / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private group photography session in Old Manali to capture your', 8),
            _ph('Curated by TRAGUIN Experts: Safety-first routes featuring strictly female-recommended resorts and elite', 9),
            _ph('Personalized Assistance: Dedicated destination managers ensuring immediate entry check-ins and easy', 10),
            _ph('Exclusive Recommendations: Curated guide to the absolute best rooftop cafes and', 11),
            _ph('Local Souvenirs: Check out the local wood-panel shops on Mall Road for real Kullu shawls, woolen stoles, pashminas, organic mountain honey, and hand-painted Tibetan mandalas. Cafes & Food: Old Manali features lovely wooden mountain cafes serving great Italian wood-fired pizzas, Himalayan river trout, hot sweet apple pies, and organic coffees.', 12),
            _ph('Hotel Policies: Standard check-in is 14:00 hrs and check-out is 11:00 hrs. Please present valid photo IDs', 13)
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
        price_note='On Request (Premium Girls Special Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Girls Trip Manali',
        overview="GIRLS TRIP MANALI • WANDERLUST, LUXURY & SISTERHOOD Get ready for the ultimate mountain getaway curated exclusively by TRAGUIN. Presenting a specially designed Himachal Tour Package made for a chic, high-spirited, female-only escape. This Luxury Himachal Holiday balances adrenaline-pumping high-altitude adventures with absolute comfort, top-tier safety, and aesthetic leisure. Revel in the breathtaking landscapes of Himachal, bond over late-night bonfire chats in premium stays, and dine at the most happening riverside cafes. As your trusted luxury travel experts, TRAGUIN turns this girls' getaway into a collection of beautiful, unforgettable memories.\n\nTOUR OVERVIEW\nThis custom-curated Himachal Family Tour variant is optimized specifically for all-female travel groups looking for comfort, style, and total security. Moving in a premium luxury SUV with a highly vetted, professional, and courteous tourist chauffeur, you will explore the best tourist places in Himachal without a single worry. The route includes everything a perfect group escape needs: handpicked hotels with spectacular panoramic balconies, an expansive daily breakfast and dinner plan (MAPAI), safety-first assistance, and a special TRAGUIN curated experience note including a professional photoshoot and high-tea sessions.",
        seo_title='HP-009 | Girls Trip Manali | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Himachal Pradesh package (HP-009 / TRG-HIM-009): Manali • Solang Valley • Atal Tunnel • Old Manali • Jogini Waterfalls with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN MANALI & CAFE HOPPING', 1),
            _ih('Day 02: LOCAL HERITAGE & JOGINI WATERFALL TREK', 2),
            _ih('Day 03: ATAL TUNNEL & SISSU VALLEY EXCURSION', 3),
            _ih('Day 04: SOLANG VALLEY ADVENTURE DAY', 4),
            _ih('Day 05: MANALI TO DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private group photography session in Old Manali to capture your', 6),
            _ih('Curated by TRAGUIN Experts: Safety-first routes featuring strictly female-recommended resorts and elite', 7),
            _ih('Personalized Assistance: Dedicated destination managers ensuring immediate entry check-ins and easy', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN MANALI & CAFE HOPPING',
                (
                    "WELCOME TO THE HIMALAYAS – CHIC VIBES & RIVERSIDE RETREAT Your premium Himachal trip kicks off with a warm reception at Chandigarh Station or Bhuntar Airport by your dedicated private luxury vehicle. Enjoy a scenic drive alongside the winding Beas River, stopping for premium wood-fired snacks along the highway. Arrive in Manali and check into your handpicked premium stay. In the afternoon, head out to explore Old Manali's bohemian cafes, featuring artisan coffees, live acoustic music, and fantastic photography points."
                ),
                [
                    'Sightseeing Included: Old Manali cafe district, Riverside nature walks, Mall Road exploration.',
                    'Evening Experience: Welcome high-tea session with premium snacks curated by TRAGUIN experts.',
                    'Overnight Stay: Manali (Premium Valley View Luxury Resort)',
                    'Meals Included: Welcome Mocktails & Luxury Buffet Dinner',
                ],
            ),            _day(
                2,
                'LOCAL HERITAGE & JOGINI WATERFALL TREK',
                (
                    'MYSTICAL FORESTS, WATERFALLS & HIGH-STREET SHOPPING Start your morning with a healthy breakfast before heading into the pine forests of the Hadimba Temple. Next, drive to Vashisht Village to begin a light, incredibly scenic short trek to Jogini Waterfalls. This route offers breathtaking landscapes and magnificent valleys, making it an excellent spot for group photos. Spend your late afternoon back on Mall Road for authentic local souvenir shopping, fine woolens, and traditional accessories.'
                ),
                [
                    'Sightseeing Included: Hadimba Temple, Jogini Waterfall Trek, Vashisht Village, Tibetan Monasteries.',
                    'Evening Experience: Private cozy bonfire night at the resort with snacks, music, and storytelling.',
                    'Overnight Stay: Manali (Premium Valley View Luxury Resort)',
                    'Meals Included: Premium Breakfast & Barbecue Dinner',
                ],
            ),            _day(
                3,
                'ATAL TUNNEL & SISSU VALLEY EXCURSION',
                (
                    'CROSSING THE GREATER HIMALAYAS – EPIC SNOWSCAPES & WATERFALLS Prepare for an unforgettable journey today as you pass through the Atal Tunnel, a global engineering marvel over 9 km long. Cross underneath the mountains to reveal the wide, dramatic landscapes of Sissu in Lahaul Valley. Pose by the frozen streams, enjoy viewings of the grand Sissu Waterfall, and take in the magnificent scenery. This is a top tourist place in Himachal for viral reels and stunning winter photography.'
                ),
                [
                    'Sightseeing Included: Atal Tunnel North Portal, Sissu Village, Chandra River Basin, Sissu Waterfall viewpoint.',
                    'Optional Activities: Snow scooter riding or a professional group photoshoot in traditional Himachali attire.',
                    'Overnight Stay: Manali (Premium Valley View Luxury Resort)',
                    'Meals Included: Premium Breakfast & Gourmet Dinner',
                ],
            ),            _day(
                4,
                'SOLANG VALLEY ADVENTURE DAY',
                (
                    'THRILLING LANDSCAPES & GLIDING THROUGH THE CLOUDS After a delicious buffet breakfast, drive out to Solang Valley, the adventure sports capital of Manali. Take a modern cable car ride up to Mount Phatru for a striking 360-degree view of the glacier ranges. The group can join in on immersive experiences like tandem paragliding, zorbing, or quad biking down the mountain paths. In the evening, return to your resort to relax and unwind after an action-packed day.'
                ),
                [
                    'Sightseeing Included: Solang Valley meadows, Snow line views, Palchan Village vistas.',
                    'Evening Experience: A premium custom dinner party at a curated fine dining restaurant in town.',
                    'Overnight Stay: Manali (Premium Valley View Luxury Resort)',
                    'Meals Included: Premium Breakfast & Farewell Special Dinner',
                ],
            ),            _day(
                5,
                'MANALI TO DEPARTURE',
                (
                    'CHERISHING THE MEMORIES OF SISTERHOOD BEYOND DESTINATIONS Enjoy a final morning breakfast together on the resort terrace as the sun lights up the snow peaks. Pack your bags and hop into your private premium vehicle for a comfortable ride back to Chandigarh or Delhi. Head home with tons of content for your feed and unforgettable memories designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door station or airport drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Solang Valley Resort /',
                'Himachal Pradesh',
                '04 Nights',
                'Deluxe',
                'Golden Tulip / similar',
                'Deluxe Balcony Room',
                4,
                1,
                description='OPTION 01 – DELUXE: Solang Valley Resort / | Golden Tulip / similar | Deluxe Balcony Room',
            ),
            _hotel(
                'Manu Allaya Resort / The',
                'Himachal Pradesh',
                '04 Nights',
                'Premium',
                'Grand Welcome',
                'Premium Panoramic',
                4,
                2,
                description='OPTION 02 – PREMIUM: Manu Allaya Resort / The | Grand Welcome | Premium Panoramic',
            ),
            _hotel(
                'Span Resort & Spa /',
                'Himachal Pradesh',
                '04 Nights',
                'Luxury',
                'Baragarh Resort',
                'Luxury River View',
                4,
                3,
                description='OPTION 03 – LUXURY: Span Resort & Spa / | Baragarh Resort | Luxury River View',
            ),
            _hotel(
                'The Oberoi Sukhvilas /',
                'Himachal Pradesh',
                '04 Nights',
                'Ultra Luxury',
                'Sukhvilas Luxury Villas',
                'VVIP Royal',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Oberoi Sukhvilas / | Sukhvilas Luxury Villas | VVIP Royal',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 04 Nights in high-end female- recommended hotels.', 1),
            _inc_included('Luxury Transportation: Private premium SUV with a verified, professional chauffeur.', 2),
            _inc_included('Curated Meal Plan: Daily luxury breakfasts and custom dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 active concierge support and emergency assistance.', 4),
            _inc_included('Complimentary Experience: Reserved private bonfire evening with music and snacks.', 5),
            _inc_included('Welcome Kit: Customized travel accessories, dry fruits, and mocktails.', 6),
            _inc_excluded('Airfare, flight tickets, or interstate train travel.', 7),
            _inc_excluded('Adventure sport tickets (Paragliding, quad biking, zipline fees).', 8),
            _inc_excluded('Monument entrance passes, camera permits, local step guide fees.', 9),
            _inc_excluded('Personal items such as laundry, phone calls, or tips.', 10),
        ],
    )
    return package, itinerary

def build_hp_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-010'
    tour_code = 'TRG-HIM-010'
    title = 'Relaxed Shimla Escape • Elegance & Leisure at a Gentle Pace'
    duration = '04 Nights / 05 Days'
    slug = 'hp-010-relaxed-shimla-escape'
    itin_slug = 'hp-010-relaxed-shimla-escape-itinerary'
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
            _ph('Serial code HP-010 | TRAGUIN tour code TRG-HIM-010', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Senior Citizen', 2),
            _ph('Destinations: Shimla • Kufri • Mashobra • Chail', 3),
            _ph('Ideal for: Senior Citizens, Family Groups & Leisure Travelers', 4),
            _ph('Best season: March to June (Mild Weather) / September to November (Crisp Autumn)', 5),
            _ph('Starting price: On Request (Premium Customized Custom Plan)', 6),
            _ph('Vehicle / Meals: Private Luxury Innova Crysta / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: High-comfort roadside pacing with pre-mapped clean, modern', 8),
            _ph('Curated by TRAGUIN Experts: Sightseeing schedules explicitly arranged between 10:00 AM and 4:00', 9),
            _ph('Personalized Assistance: Chauffeur stays dedicated right at vehicle exit gates to guarantee seamless', 10),
            _ph('Premium Handpicked Hotels: Accommodations thoroughly vetted for walk-in showers, operational', 11),
            _ph('Local Markets & Souvenirs: Take a leisurely stroll near Lakkar Bazaar to pick up beautiful hand-carved wooden walking sticks, custom walnut-wood boxes, authentic Himachali woolen shawls, and pure local apple jams. Cafes & Food: Sit back and enjoy the colonial architecture from the glass windows of historic bakeries on Mall Road while trying warm cinnamon buns, fruit crumbles, and light aromatic herbal teas.', 12),
            _ph('Hotel Policies: Standard check-in is at 14:00 hrs; early check-in requests are subject to room availability', 13)
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
        price_note='On Request (Premium Customized Custom Plan)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Relaxed Shimla Escape',
        overview='RELAXED SHIMLA ESCAPE • ELEGANCE & LEISURE AT A GENTLE PACE Welcome to a beautifully paced, thoughtful retreat created exclusively by TRAGUIN. Embark on the finest "Himachal Senior Citizen Holiday" specially customized to reveal the sweeping, breathtaking landscapes and classic colonial heritage of Shimla without any rush or strenuous travel. As your elite travel consultants, TRAGUIN prioritizes your safety, comfort, and emotional well-being, presenting an itinerary featuring premium stays, easily accessible iconic attractions, and handpicked hotels that boast stunning mountain vistas. Let the timeless scenic beauty and crisp, rejuvenating mountain breeze of Shimla envelope you, shaping unforgettable memories with absolute peace of mind.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package is curated with zero-strain, slow-paced travel parameters perfect for senior citizens. Traveling in a dedicated private luxury vehicle with low-step ingress, smooth suspension, and an extremely courteous, background-verified chauffeur, your daily comfort is completely assured. Your stay includes an explicit meal plan featuring nutritious, freshly cooked breakfasts and custom-ordered mild dinners at premium handpicked hotels. Every minor detail is overseen by our operations center to provide the standard TRAGUIN curated experience note, meaning easy vehicle drop-offs close to sight venues, zero long walking intervals, and thoughtful personal assistance at every milestone.\n\nWHY CHOOSE THE BEST SHIMLA TOUR PACKAGE?\nWhen exploring choices for a Luxury Shimla Holiday or a dedicated Shimla Family Tour, elderly travelers require specialized pacing combined with flawless hospitality. Shimla, the historic summer capital of British India, offers the best blend of architectural legacy and scenic quietude. From strolling along the flat, pedestrian-only stretches of the famous Mall Road to viewing the top tourist places in Shimla like the Christ Church and the historic Viceregal Lodge, Shimla sightseeing remains completely timeless. For couples seeking a quiet nostalgic anniversary or parents traveling on a premium Shimla Honeymoon Package structure adapted for absolute relaxation, the evergreen pine slopes of Mashobra and the peaceful apple orchards of Kufri offer perfect serene escapes. These locations feature excellent wheelchair-accessible pathways, charming colonial architecture, and highly popular Instagram locations for grand family portraits. With the signature touch of our TRAGUIN Shimla Packages, you are guaranteed curated exclusive experiences, premium handpicked hotels, and a stress-free journey during the absolute best time to visit Shimla.',
        seo_title='HP-010 | Relaxed Shimla Escape | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Himachal Pradesh package (HP-010 / TRG-HIM-010): Shimla • Kufri • Mashobra • Chail with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SHIMLA', 1),
            _ih('Day 02: SHIMLA COLONIAL HERITAGE SIGHTSEEING', 2),
            _ih('Day 03: EXCURSION TO MASHOBRA & CRAIGNANO GREENERY', 3),
            _ih('Day 04: LEISURELY DAY AT KUFRI VALLEYS', 4),
            _ih('Day 05: SHIMLA TO CHANDIGARH / DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: High-comfort roadside pacing with pre-mapped clean, modern', 6),
            _ih('Curated by TRAGUIN Experts: Sightseeing schedules explicitly arranged between 10:00 AM and 4:00', 7),
            _ih('Personalized Assistance: Chauffeur stays dedicated right at vehicle exit gates to guarantee seamless', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SHIMLA',
                (
                    'ROYAL RECEPTION & TRANSIT THROUGH SCENIC PINE VALLEYS Your premium Shimla experience begins with a warm, personalized greeting by our courteous chauffeur at Chandigarh Airport or Kalka Railway Station. Board your comfortable luxury transport vehicle and embark on a smooth, scenic drive up the Himalayan foothills. The route features wide, beautifully paved highways with spectacular valley viewpoints and curated rest stops for tea and refreshments. Upon arriving in the Queen of Hills, check into your premium luxury hotel with priority hassle-free registration. Spend a relaxing evening admiring the mountain sunset from your private balcony.'
                ),
                [
                    'Sightseeing Included: Scenic Himalayan foothills drive, Timber Trail panoramic valley views en-route.',
                    'Evening Experience: Hot herbal tea presentation and a personalized trip orientation by TRAGUIN experts.',
                    'Overnight Stay: Shimla (Premium Luxury Heritage Resort with easy-access elevators)',
                    'Meals Included: Welcome Drink & Nourishing Gourmet Dinner',
                ],
            ),            _day(
                2,
                'SHIMLA COLONIAL HERITAGE SIGHTSEEING',
                (
                    'TIMELESS COLONIAL SPLENDOUR & EASY MALL ROAD STROLL Indulge in a relaxed, delicious breakfast before setting out for an elegant day of colonial exploration. Visit the majestic Viceregal Lodge (Rashtrapati Niwas), an architectural marvel surrounded by manicured lawns and flat, paved walkways that are highly accessible. In the afternoon, take the dedicated government elevator directly up to the pedestrian-only Ridge and Mall Road. Stroll at your own gentle pace along the flat, vehicle- free boulevard, taking in the historical facade of Christ Church and Gaiety Theatre. mountains.'
                ),
                [
                    'Sightseeing Included: Viceregal Lodge gardens, The Ridge, Christ Church, Scandal Point, Mall Road.',
                    'Optional Activities: An elegant sit-down high tea session at a legendary heritage cafe overlooking the',
                    'Overnight Stay: Shimla (Premium Luxury Heritage Resort)',
                    'Meals Included: Premium Breakfast & Custom Mild Dinner',
                ],
            ),            _day(
                3,
                'EXCURSION TO MASHOBRA & CRAIGNANO GREENERY',
                (
                    'SERENE APPLE ORCHARDS & TRANGUIL MOUNTAIN MEDITATIONS Awake to the soothing sounds of birds and a crisp mountain breeze. Today we head to Mashobra, a peaceful, untouched haven of oak and pine forests away from all tourist bustle. Enjoy a quiet, gentle drive to Craignano Nature Park, featuring beautiful flat garden paths, historic wooden villas, and breathtaking landscapes that showcase the deep snow peaks. There are plenty of sitting benches and shade zones, allowing our senior guests to experience the healing power of pure nature comfortably. points.'
                ),
                [
                    'Sightseeing Included: Mashobra apple orchard vistas, Craignano Italian-style villa lawns, beautiful photography',
                    'Evening Experience: Private cozy bonfire evening with soothing classic instrumental music back at the resort.',
                    'Overnight Stay: Shimla (Premium Luxury Heritage Resort)',
                    'Meals Included: Premium Breakfast & Traditional Himachali-Inspired Dinner',
                ],
            ),            _day(
                4,
                'LEISURELY DAY AT KUFRI VALLEYS',
                (
                    "MAJESTIC CEDAR FOREST PANORAMAS & MILD NATURE VIEWS Enjoy another premium breakfast before embarking on a short, comfortable morning drive to the high hills of Kufri. We bypass the steep, muddy horse trails to focus on the serene, easily reachable viewpoints of the Kufri valley. Visit the Himalayan Nature Park, where well-leveled paths allow you to see beautiful flora and rare fauna like the snow leopard and musk deer up close. The rest of the afternoon is kept free for complete relaxation, reading, or taking advantage of the resort's premium spa facilities. points."
                ),
                [
                    'Sightseeing Included: Kufri pine valley vistas, Himalayan Nature Park, Green Valley panoramic photography',
                    'Optional Activities: A beautiful professional family portraiture session in traditional attire.',
                    'Overnight Stay: Shimla (Premium Luxury Heritage Resort)',
                    'Meals Included: Premium Breakfast & Luxury Farewell Dinner',
                ],
            ),            _day(
                5,
                'SHIMLA TO CHANDIGARH / DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES & A COMFORTABLE RETURN Relish a long, lazy breakfast at your premium hotel while capturing your last mountain valley photos. Your private luxury transport vehicle will be brought right to the main lobby portico for easy, comfortable boarding. Travel smoothly back down the national highway toward Chandigarh Airport or Kalka Station for your return home. Depart with a rested body, a joyful spirit, and unforgettable memories designed meticulously by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door highway drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Willow Banks / Clarkes',
                'Himachal Pradesh',
                '04 Nights',
                'Deluxe',
                'Hotel / similar',
                'Premium Premium',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Willow Banks / Clarkes | Hotel / similar | Premium Premium',
            ),
            _hotel(
                'Radisson Hotel Shimla /',
                'Himachal Pradesh',
                '04 Nights',
                'Premium',
                'Welcomhotel Tavisha',
                'Superior Valley',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Hotel Shimla / | Welcomhotel Tavisha | Superior Valley',
            ),
            _hotel(
                'The Oberoi Cecil, Shimla /',
                'Himachal Pradesh',
                '04 Nights',
                'Luxury',
                'similar',
                'Luxury Heritage',
                4,
                3,
                description='OPTION 03 – LUXURY: The Oberoi Cecil, Shimla / | similar | Luxury Heritage',
            ),
            _hotel(
                'Wildflower Hall, An Oberoi',
                'Himachal Pradesh',
                '04 Nights',
                'Ultra Luxury',
                'Resort / similar',
                'Premier Mountain',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Wildflower Hall, An Oberoi | Resort / similar | Premier Mountain',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 04 Nights in senior-friendly properties with easy accessibility.', 1),
            _inc_included('Luxury Transportation: Chauffeur-driven Innova Crysta with low steps and spacious seating.', 2),
            _inc_included('Curated Meal Plan: Custom, nutritious breakfast and tailored dinner sets (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 proactive assistance and senior concierge on call.', 4),
            _inc_included('Welcome Amenities: Personalized travel blanket, medical comfort kit, and mineral water.', 5),
            _inc_included('Complimentary Experience: Dedicated elevator tickets for easy Mall Road transit.', 6),
            _inc_excluded('Airfare, flight tickets, or long-distance rail fares.', 7),
            _inc_excluded('Monument entry tickets, professional guide fees, or inner camera fees.', 8),
            _inc_excluded('Personal items such as laundry, phone bills, alcoholic beverages, and tips.', 9),
            _inc_excluded('Any horse rides, adventure sports, or external porterage services. TRAGUIN Premium Luxury Itinerary — HP-010 5', 10),
        ],
    )
    return package, itinerary

def build_hp_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-011'
    tour_code = 'TRG-SPI-011'
    title = 'Spiti Explorer • Journey to the Middle Land'
    duration = '08 Nights / 09 Days'
    slug = 'hp-011-spiti-valley-explorer'
    itin_slug = 'hp-011-spiti-valley-explorer-itinerary'
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
            _ph('Serial code HP-011 | TRAGUIN tour code TRG-SPI-011', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Premium Adventure /', 2),
            _ph('Destinations: Shimla • Kalpa • Kaza • Key Monastery • Langza • Hikkim • Komic • Chandratal Lake • Manali', 3),
            _ph('Ideal for: Adventure Explorers, Luxury Seekers & Photography Connoisseurs', 4),
            _ph('Best season: June to September (Spiti Summer Expedition)', 5),
            _ph('Starting price: On Request (Bespoke Luxury Wilderness Pricing)', 6),
            _ph('Vehicle / Meals: Private Luxury 4x4 SUV / MAPAI (Breakfast & Gourmet Dinners)', 7),
            _ph('TRAGUIN Signature Experience: Private hot tea and gourmet snacks set up trailside along the scenic Kunzum', 8),
            _ph('Curated by TRAGUIN Experts: Gradual acclimatization routes designed to ensure high-altitude health and', 9),
            _ph('Premium Handpicked Hotels: Accommodations selected for their heating amenities, reliable power backups,', 10),
            _ph('Luxury Transportation: Experienced, background-verified mountain drivers who know the best hidden', 11),
            _ph('Hotel Policies: High-altitude properties feature traditional solar or wood heating. Continuous running hot water', 12),
            _ph('may be available during designated morning and evening hours.', 13)
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
        price_note='On Request (Bespoke Luxury Wilderness Pricing)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Spiti Explorer',
        overview='Welcome to a transcendental world of rugged raw grandeur, ancient Buddhist monasteries, and pristine high- altitude frontiers, meticulously curated by TRAGUIN. This premier Spiti Explorer itinerary represents the absolute pinnacle of a Luxury Himachal Holiday. Carefully engineered to balance true wild adventure with exceptional premium stays, this custom-designed passage offers immersive experiences across remote marvels. From the deepest trans-Himalayan valleys to the highest post offices on the globe, TRAGUIN invites you to witness breathtaking landscapes and forge unforgettable memories.\n\nTOUR OVERVIEW\nThis elite 08 Nights / 09 Days expedition represents the definitive Premium Himachal Experience. Travelling via a rugged, heavy-duty private 4x4 SUV chauffeured by an elite mountain specialist driver, your path traverses from the lush apple orchards of Kinnaur to the cold desert plateaus of Spiti Valley. Your customizable route features handpicked hotels and exclusive glamping sites nestled right beside deep river gorges. Complete with a signature meal plan blending sophisticated hot breakfast buffets and rich local delicacies, this entire journey is enhanced by a personalized TRAGUIN curated experience note, guaranteeing safety, priority local access, and VIP assistance.\n\nWHY CHOOSE THE BEST HIMACHAL TOUR PACKAGE TO SPITI VALLEY?\nFor discerning global adventurers, a journey into the trans-Himalayan frontier requires precise curation. This Best Himachal Tour Package serves as the ultimate benchmark, redefining remote exploration by combining unmatched wilderness with premium comfort. Himachal Pradesh holds some of the most dramatic, iconic attractions in the world. Spiti Valley—the enchanting "Middle Land"—unveils a realm of high-altitude deserts, centuries-old cliffside monasteries, and sapphire lakes that make it a dream choice for a luxury Himachal Honeymoon Package or an off-beat Himachal Family Tour. Our comprehensive Himachal Sightseeing strategy connects you directly to the top tourist places in Himachal, including the world-famous Key Monastery, the fossil village of Langza, and the high-altitude wonders of Hikkim and Komic. Capture timeless portraits at popular Instagram locations like the serene waters of Chandratal Lake or the stunning snow-capped backdrop of the Kinnaur Kailash range. Whether you are shopping for exotic woolen shawls at the local markets, indulging in Tibetan butter teas, or chasing rugged geographic thrills, our signature TRAGUIN Himachal Packages ensure that you explore during the best time to visit Himachal with supreme luxury.',
        seo_title='HP-011 | Spiti Explorer | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days Himachal Pradesh package (HP-011 / TRG-SPI-011): Shimla • Kalpa • Kaza • Key Monastery • Langza • Hikkim • Komic • Chandratal Lake • Manali with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SHIMLA', 1),
            _ih('Day 02: SHIMLA TO KALPA VIA NARKANDA', 2),
            _ih('Day 03: KALPA TO KAZA VIA NAKO & TABO', 3),
            _ih('Day 04: KAZA LOCAL EXCURSION (KEY MONASTERY & KIBBER)', 4),
            _ih('Day 05: HIGHEST VILLAGES EXCURSION (LANGZA, HIKKIM & KOMIC)', 5),
            _ih('Day 06: KAZA TO CHANDRATAL LAKE VIA KUNZUM PASS', 6),
            _ih('Day 07: CHANDRATAL LAKE TO MANALI VIA ATAL TUNNEL', 7),
            _ih('Day 08: MANALI TO CHANDIGARH', 8),
            _ih('TRAGUIN Signature Experience: Private hot tea and gourmet snacks set up trailside along the scenic Kunzum', 9),
            _ih('Curated by TRAGUIN Experts: Gradual acclimatization routes designed to ensure high-altitude health and', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SHIMLA',
                (
                    'GATEWAY TO THE HILLS & COLONIAL LUXURY RESPLENDENCE Your luxury Himachal holiday begins as you land at Chandigarh or New Delhi, where your private premium 4x4 SUV awaits your family. Ascend into the rolling green foothills to arrive at the historic summer capital of Shimla. Check into your chosen premium hotel or colonial estate. In the evening, take a leisurely stroll down the Mall Road and the Ridge, appreciating the heritage British architecture, boutique handicraft shopping, and gorgeous'
                ),
                [
                    'photography points: at sunset.',
                    'Sightseeing Included: The Ridge, Mall Road, Gaiety Theatre, Christ Church.',
                    'Evening Experience: Exquisite heritage welcome dinner hosted at a refined colonial restaurant.',
                    'Overnight Stay: Shimla (Premium Luxury Heritage Property)',
                    'Meals Included: Welcome Drink & Fine-dining Dinner',
                ],
            ),            _day(
                2,
                'SHIMLA TO KALPA VIA NARKANDA',
                (
                    "THE MAJESTIC KINNAUR ROADWAYS & SNOW-CAPPED PEAKS Depart early after a gourmet breakfast, journeying along the legendary Hindustan-Tibet highway. Drive past the scenic beauty of Narkanda's pine woods and navigate the thrilling, rock-carved cliffs of the Kinnaur gate. Arrive at the scenic hamlet of Kalpa by late afternoon. Watch the incredible sunset illuminate the legendary Kinnaur Kailash peak in shades of crimson and gold from your room's private wooden balcony."
                ),
                [
                    'Sightseeing Included: Tranda Dhank cliff-carved roads, Kalpa Suicide Point, ancient Roghi Village.',
                    'Optional Activities: A short evening stroll through the ancient, aromatic pine orchards of Kalpa.',
                    'Overnight Stay: Kalpa (Premium Mountain-view Luxury Lodge)',
                    'Meals Included: Premium Breakfast & Authentic Kinnauri Dinner',
                ],
            ),            _day(
                3,
                'KALPA TO KAZA VIA NAKO & TABO',
                (
                    'CROSSING THE TRANS-HIMALAYAN REBELS TO THE MIDDLE LAND An extraordinary driving day unfolds as the lush green valleys of Kinnaur dissolve completely into the raw, wind- carved stone canyons of Spiti Valley. Stop by the pristine Nako Lake, tucked away at high altitude, before reaching Tabo. Explore the legendary Tabo Monastery, a UNESCO World Heritage site founded in 996 AD, often called the "Ajanta of the Himalayas" for its exceptionally preserved ancient frescoes and clay statues. Arrive in Kaza, the commercial heart of Spiti, for a luxury stay.'
                ),
                [
                    'Sightseeing Included: Nako Helipad view, Tabo Monastery Caves, Khab Confluence of Spiti & Sutlej rivers.',
                    'Evening Experience: Stargazing walk beneath the brilliantly clear, unpolluted Milky Way galaxy skies.',
                    'Overnight Stay: Kaza (Premium Handpicked Luxury Boutique Hotel)',
                    'Meals Included: Lavish Breakfast & Multi-course Hot Dinner',
                ],
            ),            _day(
                4,
                'KAZA LOCAL EXCURSION (KEY MONASTERY & KIBBER)',
                (
                    "CLIFFSIDE MONASTIC SPLENDOUR & HIGHEST SUSPENSION BRIDGES Dedicate your day to exploring the iconic landmarks of Spiti. Visit the world-famous Key Monastery, a breathtaking fort-like structure that cascades down a monolithic cliffside. Receive a private audience and blessing from senior resident lamas arranged by TRAGUIN experts. Later, ascend to the scenic alpine village of Kibber and walk over the Chicham Bridge, officially celebrated as Asia's highest gorge suspension bridge, offering thrilling, deep canyon views."
                ),
                [
                    'Sightseeing Included: Key Monastery Complex, Kibber Wildlife Sanctuary perimeters, Chicham Bridge.',
                    'Optional Activities: Authentic Tibetan lunch experience inside a traditional mud-crafted homestay.',
                    'Overnight Stay: Kaza (Premium Handpicked Luxury Boutique Hotel)',
                    'Meals Included: Premium Breakfast & Specialized Indo-Tibetan Dinner',
                ],
            ),            _day(
                5,
                'HIGHEST VILLAGES EXCURSION (LANGZA, HIKKIM & KOMIC)',
                (
                    'POSTCARDS FROM THE ROOF OF THE WORLD Journey up to the highest permanently inhabited settlements on earth. Arrive first at Langza, characterized by a massive, colorful golden Buddha statue looking out over snow-capped valleys. Next, drive to Hikkim, home to the highest post office on the planet. Here, you can mail a hand-written postcard to your loved ones from 14,400 feet up. Conclude your high-altitude tour at Komic, the highest village connected by a motorable road, and tour its ancient monastery.'
                ),
                [
                    "Sightseeing Included: Langza Buddha Monument, World's Highest Post Office, Komic Monastery.",
                    'Photography Points: Prehistoric marine fossils walk across Langza plains with a local guide.',
                    'Overnight Stay: Kaza (Premium Handpicked Luxury Boutique Hotel)',
                    'Meals Included: Premium Breakfast & Premium Buffet Dinner',
                ],
            ),            _day(
                6,
                'KAZA TO CHANDRATAL LAKE VIA KUNZUM PASS',
                (
                    'THE SACRED MOON LAKE & PRESTIGE ALPINE GLAMPING Depart Kaza and ascend over the spectacular Kunzum Pass, situated at a breathtaking 14,930 feet, marked by waving colorful Buddhist prayer flags. Take a scenic detour to Chandratal Lake, a deep blue crescent-shaped body of water surrounded by alpine peaks. Walk along the lakeside paths, soaking in the serene atmosphere and beautiful reflections. Later, head to a premium luxury glamping site nearby, complete with cozy, insulated deluxe tents and ensuite amenities.'
                ),
                [
                    'Sightseeing Included: Kunzum Devi Temple, Chandratal Lake (The Moon Lake) Trek & Walk.',
                    'Evening Experience: Private cozy bonfire evening with hot appetizers beneath a star-filled sky.',
                    'Overnight Stay: Chandratal Eco-Luxury Glamping Site (Ensuite Elite Tents)',
                    'Meals Included: Gourmet Breakfast & Freshly Prepared Hot Campfire Dinner',
                ],
            ),            _day(
                7,
                'CHANDRATAL LAKE TO MANALI VIA ATAL TUNNEL',
                (
                    'NAVIGATING THE ROHTANG VALLEY TO LUSH GREEN PARADISE Embark on a ruggedly beautiful drive along the Chandra River beds, navigating the famous boulders of Chhatru and Gramphu. Re-enter modern comfort through the engineering marvel of the Atal Tunnel, transitioning from the dry high-altitude plateau of Lahaul into the lush pine-forested slopes of Manali. Check into your ultra-luxury resort and indulge in a rejuvenating premium spa session to unwind after your trans-Himalayan journey.'
                ),
                [
                    'Sightseeing Included: Atal Tunnel highway, Solang Valley landscape vistas, Old Manali lanes.',
                    'Food Suggestions: Wood-fired pizza or authentic fresh trout at a premium riverside café in Old Manali.',
                    'Overnight Stay: Manali (Premium 5-Star Riverside Luxury Resort)',
                    'Meals Included: Breakfast & Extravagant Buffet Dinner',
                ],
            ),            _day(
                8,
                'MANALI TO CHANDIGARH',
                (
                    'DESCENDING THROUGH THE BEAS VALLEY PROMENADE Enjoy a final morning taking in the mountain views of Manali over a delicious breakfast buffet. Board your luxury SUV for a smooth highway descent down the Beas River valley. Pass through Mandi and Bilaspur, arriving in the meticulously planned city of Chandigarh by evening. Check into an elegant 5-star hotel and enjoy a relaxed evening, reflecting on the incredible journey you have just shared.'
                ),
                [
                    'Sightseeing Included: Kullu valley driving panoramas, Sukhna Lake front promenade walk.',
                    'Evening Experience: A celebratory farewell toast and fine-dining dinner curated by our specialists.',
                    'Overnight Stay: Chandigarh (Elite 5-Star Business Luxury Hotel)',
                    'Meals Included: Breakfast & Farewell Gala Dinner',
                ],
            ),            _day(
                9,
                'CHANDIGARH TO DELHI / DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Savor your final morning breakfast at your premium hotel. Your private luxury transport will escort you along the national highway to New Delhi Airport or Chandigarh Railway Station for your journey home. Return with an enriched spirit, a camera full of stunning photos, and unforgettable memories shaped beautifully by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private door-to-door highway airport drop-off assistance.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Willow Banks / Grand',
                'Himachal Pradesh',
                '08 Nights',
                'Deluxe',
                'View Kalpa',
                'Hotel Spiti Heritage /',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Willow Banks / Grand | View Kalpa | Hotel Spiti Heritage /',
            ),
            _hotel(
                'Radisson Jass Shimla /',
                'Himachal Pradesh',
                '08 Nights',
                'Premium',
                'The Kinner Kailash',
                'Hotel Deyzor / Spiti Valley',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Jass Shimla / | The Kinner Kailash | Hotel Deyzor / Spiti Valley',
            ),
            _hotel(
                'The Grand Welcome /',
                'Himachal Pradesh',
                '08 Nights',
                'Luxury',
                'Kalpa Luxury Chalets',
                'The Spiti Village Resort',
                4,
                3,
                description='OPTION 03 – LUXURY: The Grand Welcome / | Kalpa Luxury Chalets | The Spiti Village Resort',
            ),
            _hotel(
                'Wildflower Hall Oberoi /',
                'Himachal Pradesh',
                '08 Nights',
                'Ultra Luxury',
                'VVIP Private Villa',
                'Custom VVIP Penthouse',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Wildflower Hall Oberoi / | VVIP Private Villa | Custom VVIP Penthouse',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 08 Nights in top-rated high-altitude boutique resorts & luxury camps.', 1),
            _inc_included('Luxury Transportation: Private 4x4 SUV (Innova / Fortuner) driven by an expert.', 2),
            _inc_included('Curated Meal Plan: Daily premium breakfast and hot dinners (MAPAI plan).', 3),
            _inc_included('TRAGUIN Support: 24/7 personalized travel advisor and ground network logistics.', 4),
            _inc_included('Welcome Amenities: Complete medical oxygen supply backup kit and custom dry fruit platters.', 5),
            _inc_included('Complimentary Experience: Private blessing arrangement with senior resident Lamas.', 6),
            _inc_excluded('Flights, airline taxes, or interstate railway travel cards.', 7),
            _inc_excluded('Personal expenses such as laundry, liquor orders, phone calls, tips.', 8),
            _inc_excluded('Monument entry fees, local monastery donations, porter services.', 9),
            _inc_excluded('Any optional adventure activities or emergency evacuation expenses.', 10),
        ],
    )
    return package, itinerary

def build_hp_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-012'
    tour_code = 'TRG-KAZA-012'
    title = 'Premium Kaza Expedition'
    duration = '07 Nights / 08 Days'
    slug = 'hp-012-premium-kaza-expedition'
    itin_slug = 'hp-012-premium-kaza-expedition-itinerary'
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
            _ph('Serial code HP-012 | TRAGUIN tour code TRG-KAZA-012', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Adventure & Expedition', 2),
            _ph('Destinations: Himachal Pradesh', 3),
            _ph('Ideal for: Adventure Enthusiasts, High-Altitude Explorers, Luxury Seekers', 4),
            _ph('Best season: June to September', 5),
            _ph('Starting price: On Request (Premium Luxury Customised)', 6),
            _ph('Vehicle / Meals: Luxury 4x4 SUV / MAPAI (Breakfast & Dinner) BEST HIMACHAL TOUR PACKAGE', 7),
            _ph('TRAGUIN Signature Experience: Private family post-box collection service directly at the Hikkim highest post', 8),
            _ph('Curated by TRAGUIN Experts: Gradual acclimatization routes designed scientifically to eliminate altitude', 9),
            _ph('Personalized Assistance: Professional, highly experienced local mountain drivers trained in extreme terrain', 10),
            _ph('Exclusive Recommendations: Handpicked off-beat riverside picnic lunch coordinates along the pristine Spiti', 11),
            _ph('Hotel Policies: Given the remote mountain infrastructure, electricity and running hot water might be scheduled', 12),
            _ph('during fixed morning and evening hours.', 13)
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
        price_note='On Request (Premium Luxury Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Premium Kaza Expedition',
        overview="Welcome Note: Welcome to a ruggedly magnificent realm of cold deserts, towering peaks, and ancient soul- stirring monasteries, exclusively brought to life through this Premium Himachal Experience. Curated by the destination experts at TRAGUIN, this ultimate luxury Himachal holiday breaks away from the ordinary to immerse your senses in the breathtaking landscapes of Spiti Valley and Kaza. Handcrafted for seasoned adventure lovers and luxury explorers alike, this journey promises premium stays, unmatched luxury transportation, and unforgettable memories etched forever against the high-altitude skies.\n\nTOUR OVERVIEW\nThe TRAGUIN Premium Kaza Expedition is a meticulously engineered luxury holiday across the Trans-Himalayan high-altitude circuits. This curated experience transitions from the colonial lanes of Shimla into the Kinnaur orchards of Kalpa, before penetrating deep into the iconic attractions of Spiti Valley, Kaza, and the mystical Chandratal Lake. Travelling with a private luxury 4x4 SUV vehicle on a MAPAI meal plan (Lavish Breakfasts & Dinners), you are guaranteed unparalleled comfort over challenging mountain passes. Every stop is supported by our handpicked hotels, expert mechanics, satellite communication linkages, and personalized assistance, encapsulating a truly flawless TRAGUIN curated experience note.\n\nDESTINATION SEO CONTENT\nWhy visit Himachal Pradesh and the cold deserts of Spiti? A Luxury Himachal Holiday combined with the raw wildness of a Kaza Honeymoon Package or high-intensity Himachal Family Tour represents one of the most searched experiences in global tourism today. Exploring Kaza Sightseeing offers a glimpse into a time-capsule culture, housing the world's most famous attractions like the Key Monastery, Dhankar Castle, and the ancient Tabo Monastery. For adventure, shopping, and cultural photography enthusiasts, the circuit presents top tourist places in Himachal, including Hikkim—the highest post office in the world—and Langza, famous for its giant Buddha statue facing the majestic snow peaks. These are recognized as popular Instagram locations where the scenic beauty of towering ridges meets deep blue river valleys. Whether you seek the peaceful thrill of a riverside luxury camp or an immersive experience with local communities, booking your TRAGUIN Himachal Packages ensures you travel during the best time to visit Himachal with absolute safety, luxury transportation, and premium customized amenities.",
        seo_title='HP-012 | Premium Kaza Expedition | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Himachal Pradesh package (HP-012 / TRG-KAZA-012): Himachal Pradesh with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SHIMLA', 1),
            _ih('Day 02: SHIMLA TO KALPA', 2),
            _ih('Day 03: KALPA TO KAZA VIA TABO MONASTERY', 3),
            _ih('Day 04: KAZA SIGHTSEEING (KEY MONASTERY & KIBBER)', 4),
            _ih('Day 05: HIGHEST VILLAGES EXCURSION (LANGZA, HIKKIM & KOMIC)', 5),
            _ih('Day 06: KAZA TO CHANDRATAL LAKE VIA KUNZUM PASS', 6),
            _ih('Day 07: CHANDRATAL TO MANALI VIA ATAL TUNNEL', 7),
            _ih('Day 08: DEPARTURE FROM MANALI TO CHANDIGARH', 8),
            _ih('TRAGUIN Signature Experience: Private family post-box collection service directly at the Hikkim highest post', 9),
            _ih('Curated by TRAGUIN Experts: Gradual acclimatization routes designed scientifically to eliminate altitude', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SHIMLA',
                (
                    'GATEWAY TO THE HILLS & COLONIAL LUXURY RESPLENDENCE Your ultimate Kaza Expedition begins with a VIP arrival experience at Chandigarh or Delhi, where your private luxury 4x4 SUV vehicle awaits. Wind upward through majestic pine-fringed roads toward the timeless summer capital of Shimla. Check into your premium resort and relax. In the evening, take a guided walking tour along the historic Mall Road, stopping by iconic attractions like Christ Church and the Ridge for stunning photography points. Savour handcrafted local food suggestions at an upscale boutique café before your tour briefing.'
                ),
                [
                    'Sightseeing Included: The Ridge, Mall Road, Christ Church, Scandal Point.',
                    'Optional Activities: High-tea experience at a restored British colonial heritage estate.',
                    'Evening Experience: Private sunset viewing over the Shivalik range, followed by a welcome dinner.',
                    'Overnight Stay: Shimla (Luxury Premium Stay)',
                    'Meals Included: Welcome Drink & Gourmet Dinner',
                ],
            ),            _day(
                2,
                'SHIMLA TO KALPA',
                (
                    'ALONG THE SUTLEJ CANYONS TO THE KINNER KAILASH VISTAS Awake early for a spectacular scenic route along the Hindustan-Tibet Highway, charting the dramatic curves of the Sutlej River canyon. Pass through the mountain arches of Rampur and Narkanda before climbing steeply through sweet-scented apple orchards into Kalpa in Kinnaur. As you arrive, witness the breathtaking landscapes of the Kinner Kailash massif standing tall at 6,050 meters, catching the golden evening sunbeams—a pure heaven for landscape photography.'
                ),
                [
                    'Sightseeing Included: Kinnaur Gateway, Taranda Dhank cliff-hanger path, Kalpa Monastery.',
                    'Optional Activities: Short exploratory stroll to the dizzying heights of the Roghi Suicide Point.',
                    'Evening Experience: Traditional Kinnauri apple-wine or herbal tea tasting overlooking glaciers.',
                    'Overnight Stay: Kalpa (Premium Boutique Luxury Hotel)',
                    'Meals Included: Breakfast & Traditional Dinner',
                ],
            ),            _day(
                3,
                'KALPA TO KAZA VIA TABO MONASTERY',
                (
                    "ENTERING THE COLD DESERT & STEPPING BACK ONE THOUSAND YEARS Today, watch the green pine forests fade into the majestic, raw, wind-sculpted rock walls of the Spiti River basin. Drive past Khab, the spectacular confluence of the Sutlej and Spiti Rivers. Stop for a deeply emotional storytelling experience at Tabo Monastery, a UNESCO World Heritage site founded in 996 AD, often called the 'Ajanta of the Himalayas' for its pristine stucco statues. Conclude your day's journey by arriving in Kaza, the cultural capital of Spiti Valley."
                ),
                [
                    'Sightseeing Included: Khab Confluence, Nako Lake (brief stop), Tabo Monastery Caves.',
                    'Optional Activities: Meditation session inside the ancient, dark mud chambers of Tabo.',
                    'Evening Experience: Warm towel arrival at Kaza with a customized hot soup dining menu.',
                    'Overnight Stay: Kaza (Premium Handpicked Luxury Hotel)',
                    'Meals Included: Breakfast & Gourmet Dinner',
                ],
            ),            _day(
                4,
                'KAZA SIGHTSEEING (KEY MONASTERY & KIBBER)',
                (
                    'FORTRESSES OF FAITH & THE HIGHEST SUSPENSION BRIDGE IN ASIA Dedicate your morning to the definitive highlights of Kaza Sightseeing. Stand before the iconic Key Monastery, an architectural masterpiece perched dramatically on a conical hill like a fairy-tale castle. Explore the ancient prayer rooms filled with antique thangkas. Afterwards, cross the deep gorge over the Chicham Bridge—the highest suspension bridge in Asia—for exhilarating photography opportunities. Later, explore Kibber, a high wildlife sanctuary refuge home to the elusive snow leopard.'
                ),
                [
                    'Sightseeing Included: Key Monastery, Kibber Village, Chicham Bridge, Gette Viewpoint.',
                    'Optional Activities: Interactive tea session with the senior Buddhist lamas at Key Monastery.',
                    'Evening Experience: Relaxed leisure walk through Kaza’s local markets to shop for sea-buckthorn teas.',
                    'Overnight Stay: Kaza (Premium Handpicked Luxury Hotel)',
                    'Meals Included: Breakfast & Multi-cuisine Dinner',
                ],
            ),            _day(
                5,
                'HIGHEST VILLAGES EXCURSION (LANGZA, HIKKIM & KOMIC)',
                (
                    "FOSSILS, THE HIGHEST POST OFFICE & CALLS FROM THE ROOF OF THE WORLD Embark on an unforgettable day tour across the highest inhabited villages in the world. First, stop at Langza, a stunning village watched over by an iconic, giant golden Buddha statue facing the Cho Cho Kang Nilda peak. Hunt for prehistoric marine fossils in the surrounding soil. Next, drive to Hikkim to post a handwritten postcard from the world's highest post office. Finish your high-altitude circuit at Komic, the highest village connected by a motorable road, visiting the historic Tangyud Monastery."
                ),
                [
                    'Sightseeing Included: Langza Buddha Statue, Hikkim Post Office, Komic Monastery.',
                    'Optional Activities: Buying authentic fossil replicas and local woolens from local village children.',
                    'Evening Experience: Star-gazing experience under the pristine, unpolluted, zero-dust Spiti night skies.',
                    'Overnight Stay: Kaza (Premium Handpicked Luxury Hotel)',
                    'Meals Included: Breakfast & Specialized Local Thali Dinner',
                ],
            ),            _day(
                6,
                'KAZA TO CHANDRATAL LAKE VIA KUNZUM PASS',
                (
                    "ACROSS THE ROOF OF KUNZUM TO THE GLACIAL MOON LAKE Leave Kaza to ascend the mighty Kunzum Pass (4,590 meters), where colorful Buddhist prayer flags flutter wildly against the cold winds. Seek blessings at the Kunzum Devi temple before off-roading down towards Chandratal Lake—the legendary 'Moon Lake'. Walk the final stretch to witness the calm, crystal-clear glacial waters perfectly mirroring the surrounding snow peaks. Check into your premium, double-layered luxury glamping tents nearby, featuring thick mattresses and heavy duvets."
                ),
                [
                    'Sightseeing Included: Kunzum Pass, Chandratal Glacial Lake, Losar Village.',
                    'Optional Activities: Quiet parikrama (circumambulation) trek along the shores of the lake.',
                    'Evening Experience: Cozy bonfire circle and hot buffet dining under the spectacular Milky Way.',
                    'Overnight Stay: Chandratal (Bespoke Luxury Glamping Camps)',
                    'Meals Included: Breakfast & Hot Campfire Dinner',
                ],
            ),            _day(
                7,
                'CHANDRATAL TO MANALI VIA ATAL TUNNEL',
                (
                    'THE ROHTANG RIDGE DESCENT BACK TO GREEN MANALI LUXURY Drive along the unpaved, adventurous tracks of Batal and Chhatru alongside the roaring Chandra River. Cross the newly opened engineering marvel, the Atal Tunnel, passing smoothly beneath the Rohtang Pass to arrive back into the lush, emerald forests of Manali. Check into an ultra-luxury valley resort and treat your muscles to a deeply relaxing premium spa treatment. Celebrate your successful high-altitude loop with fine wines and a grand farewell dinner.'
                ),
                [
                    'Sightseeing Included: Lahaul Mountain Valley, Atal Tunnel, Solang Valley viewpoints.',
                    "Optional Activities: Shopping for authentic wooden artwork or woolens at Manali's Mall Road.",
                    'Evening Experience: Private dinner celebration with live local acoustic music at the resort.',
                    'Overnight Stay: Manali (Ultra Luxury Spa Resort Stay)',
                    'Meals Included: Breakfast & Grand Farewell Dinner',
                ],
            ),            _day(
                8,
                'DEPARTURE FROM MANALI TO CHANDIGARH',
                (
                    'CARRYING HOME MEMORIES BEYOND DESTINATIONS Enjoy a final lavish breakfast overlooking the morning mist lifting off the towering deodars. Your private luxury 4x4 SUV vehicle will drive you smoothly down the scenic highways towards Chandigarh airport or station for your flight home. Depart with a soul fully recharged by nature, carrying unforgettable memories designed flawlessly by your premium travel consultants at TRAGUIN.'
                ),
                [
                    'Transfers Included: Premium private highway drop-off.',
                    'Meals Included: Lavish Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Willow Banks /',
                'Himachal Pradesh',
                '07 Nights',
                'Deluxe',
                'Grand View Kalpa',
                'Hotel Deyzor Kaza /',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Willow Banks / | Grand View Kalpa | Hotel Deyzor Kaza /',
            ),
            _hotel(
                'Radisson Jass Shimla /',
                'Himachal Pradesh',
                '07 Nights',
                'Premium',
                'Kinner Villa',
                'The Spiti House / Mystic',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Jass Shimla / | Kinner Villa | The Spiti House / Mystic',
            ),
            _hotel(
                'The Oberoi Cecil / Echor',
                'Himachal Pradesh',
                '07 Nights',
                'Luxury',
                'Khwabeeda',
                'Spiti Heritage Hotel /',
                4,
                3,
                description='OPTION 03 – LUXURY: The Oberoi Cecil / Echor | Khwabeeda | Spiti Heritage Hotel /',
            ),
            _hotel(
                'Wildflower Hall Shimla',
                'Himachal Pradesh',
                '07 Nights',
                'Ultra Luxury',
                '(Oberoi)',
                'VVIP Private Luxury Villa',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Wildflower Hall Shimla | (Oberoi) | VVIP Private Luxury Villa',
            )
        ],
        inclusions=[
            _inc_included('Accommodation: Premium stays at handpicked hotels and luxury glamping sites.', 1),
            _inc_included('Meals: Daily breakfasts & dinners (MAPAI) with special high-altitude nutritious items.', 2),
            _inc_included('Transfers: Dedicated private luxury 4x4 SUV (Innova Crysta or Fortuner) for all rough-terrain routes.', 3),
            _inc_included('Sightseeing: Complete Kaza Sightseeing, inner-line permit documentation, and toll clearances.', 4),
            _inc_included('TRAGUIN Support: 24/7 personalized remote concierge with satellite communication backing.', 5),
            _inc_included('Welcome Amenities: Eco-friendly travel oxygen bottles, customized welcome kit, and warm local stoles.', 6),
            _inc_excluded('Airfare, internal domestic flights, or long-distance railway connections.', 7),
            _inc_excluded('Entry tickets to monasteries, camera permissions, or local monastery donation tokens.', 8),
            _inc_excluded('Personal expenses like laundry, fine alcoholic beverages, room heaters, or tips.', 9),
            _inc_excluded('Adventure activity costs (paragliding, fossil tour guides, mountain bike rentals).', 10),
        ],
    )
    return package, itinerary

def build_hp_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-013'
    tour_code = 'TRG-HIM-013'
    title = 'Luxury Himachal Retreat • Grand Heritage & High Alpine Escape'
    duration = '06 Nights / 07 Days'
    slug = 'hp-013-luxury-himachal-retreat'
    itin_slug = 'hp-013-luxury-himachal-retreat-itinerary'
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
            _ph('Serial code HP-013 | TRAGUIN tour code TRG-HIM-013', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Luxury Retreat', 2),
            _ph('Destinations: Shimla • Kufri • Manali • Solang Valley • Atal Tunnel', 3),
            _ph('Ideal for: Families, Honeymooners & Discerning Luxury Vacationers', 4),
            _ph('Best season: April to June (Pleasant Summer) & November to February (Snow Experience)', 5),
            _ph('Starting price: On Request (Premium Bespoke Package)', 6),
            _ph('Vehicle / Meals: Luxury Toyota Innova Crysta / Premium MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private family tea and snack setup overlooking the glaciers during the', 8),
            _ph('Curated by TRAGUIN Experts: Well-paced routing that skips heavy highway traffic, maximizing your relaxation', 9),
            _ph('Premium Handpicked Hotels: Accommodations chosen for their top safety records, exceptional views, and', 10),
            _ph('Luxury Transportation: Chauffeurs with expert training in mountain pass safety, ensuring smooth rides.', 11),
            _ph("Local Markets & Souvenirs: Explore Shimla's Lakkar Bazaar for beautiful, handcrafted wooden artifacts and custom toys. Head to Manali's Mall Road to shop for vibrant, authentic Kullu shawls, soft pashminas, and traditional hand-made jewelry. Cafes & Food: Old Manali features cozy wooden bistros serving authentic Italian wood-fired pizzas, fresh river trout, and premium organic mountain coffees accompanied by live music.", 12),
            _ph('Hotel Policies: Standard check-in is at 14:00 hrs and check-out at 11:00 hrs. A valid government photo ID is', 13)
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
        price_note='On Request (Premium Bespoke Package)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Luxury Himachal Retreat',
        overview="ESCAPE Welcome to an unforgettable mountain retreat crafted meticulously by TRAGUIN. Embark on the definitive Best Himachal Tour Package designed to immerse you in the breathtaking landscapes, imperial colonial history, and roaring glacial rivers of Northern India. As your dedicated professional travel consultants, TRAGUIN presents a curated, premium guest-facing itinerary filled with premium stays, exquisite handpicked hotels, and immersive experiences. From the misty ridge lines of Shimla to the soaring snow peaks surrounding Manali, every element of this journey is carefully engineered to deliver exclusive experiences and create timeless, unforgettable memories.\n\nTOUR OVERVIEW\nThis custom Luxury Himachal Holiday itinerary offers a flawless combination of classic heritage exploration, alpine wonders, and peaceful indulgence. Travelling in an elite, chauffeur-driven luxury vehicle, you will navigate through stunning scenic beauty in total comfort. Your meal plan covers decadent breakfasts and custom multi- course dinners across all premium resorts. Featuring the unique TRAGUIN curated experience note, this itinerary includes VIP monument permissions, exclusive local hidden trail suggestions, and uncompromised round-the-clock guest satisfaction management.\n\nWHY BOOK A PREMIUM HIMACHAL EXPERIENCE?\nChoosing the ultimate Himachal Honeymoon Package or Himachal Family Tour unlocks a goldmine of timeless mountain charm and modern luxury. Himachal Pradesh is a majestic realm of majestic pine trees, cold glacial winds, and legendary cultural stories. From the colonial Mall Road architecture in Shimla to the thrill-seeking adventure hubs of Solang Valley and the engineering wonder of the Atal Tunnel, Himachal sightseeing presents an unparalleled journey. For travelers checking out popular Instagram locations like Kufri's snow views or Old Manali's riverside bistros, this trip guarantees magnificent photography points at every turn. Indulge in authentic local shopping, experience vibrant mountain café cultures, and explore the top tourist places in Himachal. When you choose our signature TRAGUIN Himachal Packages, you ensure standard-setting luxury, handpicked boutique hotels, and seamless execution during the absolute best time to visit Himachal.",
        seo_title='HP-013 | Luxury Himachal Retreat | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Himachal Pradesh package (HP-013 / TRG-HIM-013): Shimla • Kufri • Manali • Solang Valley • Atal Tunnel with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SHIMLA', 1),
            _ih('Day 02: SHIMLA & KUFRI EXCURSION', 2),
            _ih('Day 03: SHIMLA TO MANALI (SCENIC TRANSIT)', 3),
            _ih('Day 04: LOCAL MANALI DISCOVERY', 4),
            _ih('Day 05: SOLANG VALLEY EXCURSION', 5),
            _ih('Day 06: ATAL TUNNEL & SISSU ALPINE ADVENTURE', 6),
            _ih('Day 07: MANALI TO DELHI/CHANDIGARH DEPARTURE', 7),
            _ih('TRAGUIN Signature Experience: Private family tea and snack setup overlooking the glaciers during the', 8),
            _ih('Curated by TRAGUIN Experts: Well-paced routing that skips heavy highway traffic, maximizing your relaxation', 9),
            _ih('Premium Handpicked Hotels: Accommodations chosen for their top safety records, exceptional views, and', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SHIMLA',
                (
                    'WELCOME TO THE SUMMER CAPITAL – ROADWAY RIDGE SPLENDOR Your premium Himachal experience starts with a warm airport or station reception by your dedicated private chauffeur. Board your luxury vehicle for a beautiful drive climbing into the Shivalik hills toward Shimla. Take in the crisping mountain air and the terraced hillsides along the way. Arrive at your handpicked luxury resort, settle into your premium valley view suite, and unwind. lights.'
                ),
                [
                    'Sightseeing Included: Scenic mountain highway transit, Timber Trail valley overlooks.',
                    'Evening Experience: Relaxing wellness drink and a custom multi-course dinner overlooking the sparkling town',
                    'Overnight Stay: Shimla (Premium / Luxury Resort Stay)',
                    'Meals Included: Welcome Drink & Gourmet Dinner',
                ],
            ),            _day(
                2,
                'SHIMLA & KUFRI EXCURSION',
                (
                    'PANORAMIC ALPINE PEAKS & HISTORIC MALL RIDGE Enjoy a lavish buffet breakfast before heading to Kufri, an alpine haven famed for its breathtaking landscapes and dense cedar forests. Capture panoramic views of the endless snow ranges, visit the Himalayan Nature Park, and opt for a fun yak ride. In the afternoon, explore historic Shimla sightseeing: walk the colonial Mall Road, visit the neo-gothic Christ Church on the Ridge, and admire the majestic Viceregal Lodge.'
                ),
                [
                    'Sightseeing Included: Kufri Alpine Trails, Viceregal Lodge, Christ Church, The Ridge, Gaiety Theatre, Mall Road.',
                    'Optional Activities: Guided heritage walking tour uncovering the historical British-era scandals of Shimla.',
                    'Overnight Stay: Shimla (Premium / Luxury Resort Stay)',
                    'Meals Included: Premium Breakfast & Luxury Dinner',
                ],
            ),            _day(
                3,
                'SHIMLA TO MANALI (SCENIC TRANSIT)',
                (
                    'ALONG THE RUSHING WATERS OF THE BEAS RIVER Bid farewell to Shimla and hit the road toward Manali, the undisputed crown jewel of valley retreats. This spectacular drive winds past the Pandoh Dam, cuts through the beautiful Aut Tunnel, and skirts the roaring Beas River. Stop at Kullu for a brief riverside break and check out authentic handloom shawls. Reach your luxury resort in Manali by late evening and unwind by an open bonfire.'
                ),
                [
                    'Sightseeing Included: Pandoh Dam lake vista, Kullu Valley road view, Beas River gorges.',
                    'Evening Experience: Private riverside bonfire and musical ambiance at your luxury resort.',
                    'Overnight Stay: Manali (Premium Mountain View Luxury Resort)',
                    'Meals Included: Premium Breakfast & Resort Buffet Dinner',
                ],
            ),            _day(
                4,
                'LOCAL MANALI DISCOVERY',
                (
                    "CULTURE, SACRED DEODAR FORESTS & URBAN CAFES After a hearty breakfast, set out to explore the rich culture of Manali. Discover the legendary Hadimba Temple, set within a quiet forest of towering deodars. Relax at the Vashisht Hot Springs, famous for their natural therapeutic sulfur waters. Later, walk through Old Manali's bohemian lanes to enjoy vibrant cafes, artisanal wooden shopping, and great photography spots."
                ),
                [
                    'Sightseeing Included: Hadimba Temple, Vashisht Springs, Tibetan Monastery, Old Manali lanes, Mall Road.',
                    'Optional Activities: Local trout fish tasting and specialty fruit wine matching at an elite riverside café.',
                    'Overnight Stay: Manali (Premium Mountain View Luxury Resort)',
                    'Meals Included: Premium Breakfast & Gourmet Dinner',
                ],
            ),            _day(
                5,
                'SOLANG VALLEY EXCURSION',
                (
                    'HIGH GLACIAL ADVENTURES & ICONIC PEAK VIEWS Today is all about adventure in Solang Valley, a stunning arena of vast mountain meadows and glaciers. Take an open-air ropeway ride up to Mount Phatru for breathtaking views of the high peaks. For thrill-seekers, dive into immersive experiences like tandem paragliding, zorbing, or high-speed quad biking.'
                ),
                [
                    'Sightseeing Included: Solang Valley meadows, Snow Line vistas, Ropeway viewpoint heights.',
                    'Optional Activities: High-altitude paragliding flight or custom amateur skiing lessons (winter months).',
                    'Overnight Stay: Manali (Premium Mountain View Luxury Resort)',
                    "Meals Included: Premium Breakfast & Chef's Special Dinner",
                ],
            ),            _day(
                6,
                'ATAL TUNNEL & SISSU ALPINE ADVENTURE',
                (
                    'CROSSING THE GREATER HIMALAYAS INTO THE SNOWFIELDS Experience a breathtaking highlight of your luxury Himachal retreat. Drive through the historic Atal Tunnel, a spectacular engineering marvel carved deep under the mountains. Emerge into the majestic Lahaul Valley at Sissu. Marvel at the stunning frozen landscape, the icy Chandra River, and the cascading Sissu Waterfall—a perfect spot for photography. Return to Manali for your final evening celebration.'
                ),
                [
                    'Sightseeing Included: Atal Tunnel Transit, Sissu Village, Chandra River Basin, Sissu Waterfall view.',
                    'Evening Experience: A farewell candlelight dinner celebration with a custom dynamic menu.',
                    'Overnight Stay: Manali (Premium Mountain View Luxury Resort)',
                    'Meals Included: Premium Breakfast & Gala Farewell Dinner',
                ],
            ),            _day(
                7,
                'MANALI TO DELHI/CHANDIGARH DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS Savor a final luxurious breakfast as the morning sun lights up the snow-capped peaks. Board your private vehicle for a smooth drive back down the mountains to Chandigarh or Delhi Airport/Station. Return home with a heart full of joy, family bonds, and unforgettable memories designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury highway transfer to your airport/railway terminal.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'East Bourne Resort /',
                'Himachal Pradesh',
                '06 Nights',
                'Deluxe',
                'similar',
                'Solang Valley Resort /',
                4,
                1,
                description='OPTION 01 – DELUXE: East Bourne Resort / | similar | Solang Valley Resort /',
            ),
            _hotel(
                'Radisson Hotel Shimla /',
                'Himachal Pradesh',
                '06 Nights',
                'Premium',
                'similar',
                'Manu Allaya Resort / similar',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Hotel Shimla / | similar | Manu Allaya Resort / similar',
            ),
            _hotel(
                'The Oberoi Cecil /',
                'Himachal Pradesh',
                '06 Nights',
                'Luxury',
                'Welcomhotel',
                'Span Resort & Spa /',
                4,
                3,
                description='OPTION 03 – LUXURY: The Oberoi Cecil / | Welcomhotel | Span Resort & Spa /',
            ),
            _hotel(
                'Wildflower Hall, An Oberoi',
                'Himachal Pradesh',
                '06 Nights',
                'Ultra Luxury',
                'Resort',
                'The Oberoi Sukhvilas /',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Wildflower Hall, An Oberoi | Resort | The Oberoi Sukhvilas /',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury accommodations at premier mountain properties.', 1),
            _inc_included('Luxury Transportation: Private dedicated Innova Crysta for all transfers & sightseeing.', 2),
            _inc_included('Curated Meals: Daily five-star buffet breakfast and gourmet dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated on-tour concierge manager.', 4),
            _inc_included('Welcome Amenities: Personalized traveler kit, fresh hill juices, and local chocolates.', 5),
            _inc_included('Complimentary Experiences: Private resort evening bonfire and a special candlelight dinner arrangement.', 6),
            _inc_excluded('Flights or inter-state long-distance express rail tickets.', 7),
            _inc_excluded('Adventure sport fees (paragliding, quad biking, zorbing tickets).', 8),
            _inc_excluded('Monument entry passes, local certified guide hiring, camera fees.', 9),
            _inc_excluded('Personal expenses such as laundry, phone calls, premium drinks, or tips.', 10),
        ],
    )
    return package, itinerary

def build_hp_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-014'
    tour_code = 'TRG-OB-HP-014'
    title = 'The Oberoi Himachal Experience • Royalty Reimagined'
    duration = '05 Nights / 06 Days'
    slug = 'hp-014-oberoi-himachal-experience'
    itin_slug = 'hp-014-oberoi-himachal-experience-itinerary'
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
            _ph('Serial code HP-014 | TRAGUIN tour code TRG-OB-HP-014', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Ultra-Luxury', 2),
            _ph('Destinations: Shimla • Wildflower Hall • Mashobra • Kufri', 3),
            _ph('Ideal for: Connoisseurs of Luxury, Romantic Escapes & Families', 4),
            _ph('Best season: April to June (Pleasant) / November to February (Snow Experience)', 5),
            _ph('Starting price: On Request (Ultra- Luxury Customised)', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / Premium MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private heritage walkthrough of historic Shimla lanes with an expert', 8),
            _ph('Curated by TRAGUIN Experts: Custom pacing that balances cultural sightseeing with serene,', 9),
            _ph('Premium Handpicked Hotels: Accommodations chosen strictly based on outstanding heritage value,', 10),
            _ph('Luxury Transportation: Chauffeurs thoroughly vetted for elite behavior, safety records, and local route', 11),
            _ph('Local Markets & Souvenirs: Explore the old Lakkar Bazaar to purchase authentic wooden handicrafts, custom-made walking sticks, exquisite Himachali shawls, and organic local fruit jams or honey. Cafes & Food: Old Shimla features classic wood-paneled cafes serving traditional English afternoon teas, delicate fresh pastries, and authentic Himalayan-style comfort food.', 12),
            _ph('Weather Notes: Evenings can be cold throughout the year; we recommend carrying light woolens for the', 13)
        ],
        moods=['Luxury', 'Romantic', 'Family'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Ultra- Luxury Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='The Oberoi Himachal Experience',
        overview='THE OBEROI HIMACHAL EXPERIENCE • ROYALTY REIMAGINED Welcome to an extraordinary luxury holiday created exclusively by TRAGUIN. Embark on the prestigious Oberoi Himachal Experience, a tour meticulously designed to surround you with absolute opulence, majestic cedar forests, and time-honored colonial grandeur. As your elite travel consultants, TRAGUIN transforms your vacation into a premium Himachal experience featuring unparalleled service, handpicked hotels of legendary repute, and deeply curated exclusive experiences. Immerse yourselves in the staggering scenic beauty of the Shivalik range and allow the legendary hospitality of Oberoi properties to curate unforgettable memories for you and your loved ones.\n\nTOUR OVERVIEW\nThis bespoke Luxury Himachal Holiday brings you an unmatched level of privacy, prestige, and comfort. Travel in an ultra-premium, chauffeur-driven luxury SUV customized to negotiate mountain passes seamlessly. This signature route takes you to the historic summer capital of Shimla and into the tranquil forest paradise of Wildflower Hall. Your package includes an exquisite meal plan with breakfasts and custom curations at award- winning restaurants. Every detail contains the signature TRAGUIN curated experience note—offering customized fast-track access, private heritage guides, and around-the-clock dedicated assistance.\n\nWHY VISIT HIMACHAL WITH THE BEST HIMACHAL TOUR PACKAGE?\nWhen exploring options for a Luxury Himachal Holiday, true luxury travellers seek a world apart from the ordinary. This region offers a perfect sanctuary of breathtaking landscapes, colonial timelessness, and majestic heritage. For discerning couples looking at an elite Himachal Honeymoon Package or families choosing an upscale Himachal Family Tour, this destination offers an ideal landscape of wellness, culture, and high-altitude sophistication. From iconic attractions such as the regal Viceregal Lodge and the bustling historic Ridge to popular Instagram locations buried in the pine valleys of Mashobra, the options for exploration are endless. Indulge in premium handicraft shopping, private nature photography sessions, or a forest bath under century-old cedars. Our elite TRAGUIN Himachal Packages guarantee that you visit during the best time to visit Himachal, wrapped in the comfort of premium stays and unparalleled leisure.',
        seo_title='HP-014 | The Oberoi Himachal Experience | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Himachal Pradesh package (HP-014 / TRG-OB-HP-014): Shimla • Wildflower Hall • Mashobra • Kufri with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SHIMLA', 1),
            _ih('Day 02: SHIMLA HERITAGE EXPLORATION', 2),
            _ih('Day 03: SHIMLA TO WILDFLOWER HALL (MASHOBRA)', 3),
            _ih('Day 04: SANCTUARY NATURE TRAIL & PICNIC', 4),
            _ih('Day 05: EXCURSION TO KUFRI & NALDEHRA', 5),
            _ih('Day 06: DEPARTURE TO CHANDIGARH / DELHI', 6),
            _ih('TRAGUIN Signature Experience: Private heritage walkthrough of historic Shimla lanes with an expert', 7),
            _ih('Curated by TRAGUIN Experts: Custom pacing that balances cultural sightseeing with serene,', 8),
            _ih('Premium Handpicked Hotels: Accommodations chosen strictly based on outstanding heritage value,', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SHIMLA',
                (
                    "COLONIAL MAJESTY & THE LEGENDARY OBEROI CECIL EXPERIENCE Your premium Himachal experience begins with a VIP greeting at Chandigarh Airport or Shimla's airport by your private luxury transport chauffeur. Travel along scenic, well-paved mountain roads directly to Shimla. Check into the historic Oberoi Cecil, a grand 100-year-old ballroom palace that instantly evokes colonial majesty. Relax in your meticulously designed premium room and enjoy a customized welcome tea service overlooking the valley."
                ),
                [
                    'Sightseeing Included: Scenic Shivalik foothills drive, historic luxury hotel orientation.',
                    'Evening Experience: Private heritage walkthrough of the colonial ballroom and lounge.',
                    'Overnight Stay: The Oberoi Cecil, Shimla (Luxury Room)',
                    'Meals Included: Welcome Drink & Signature Fine-Dining Dinner',
                ],
            ),            _day(
                2,
                'SHIMLA HERITAGE EXPLORATION',
                (
                    'WALKING AMIDST ARCHITECTURAL LEGENDS & REGENCIES Relish a lavish breakfast before stepping out for a beautifully curated Shimla sightseeing tour. Accompanied by a private historian, visit the spectacular Viceregal Lodge, the seat of British power during the summer months. Take a soft walk along the pedestrian-only Mall Road, stopping at Christchurch, the Gaiety Theatre, and the sprawling Ridge. Capture magnificent panoramic mountain photographs at these iconic attractions.'
                ),
                [
                    'Sightseeing Included: Viceregal Lodge, The Ridge, Mall Road, Gaiety Theatre, Christchurch.',
                    'Optional Activities: High-tea reservation at an upscale heritage café with views of the valley.',
                    'Overnight Stay: The Oberoi Cecil, Shimla (Luxury Room)',
                    'Meals Included: Premium Breakfast & Ala Carte Dinner',
                ],
            ),            _day(
                3,
                'SHIMLA TO WILDFLOWER HALL (MASHOBRA)',
                (
                    'TRANSIT TO AN ANCIENT PINE FORTRESS OF SUPREME WELLNESS Depart The Oberoi Cecil for a short, beautiful mountain drive farther into the mountains towards Mashobra. Check into Wildflower Hall, An Oberoi Resort, perched at 8,250 feet amidst dense cedar forests. This magnificent fairy-tale estate provides breathtaking landscapes and unmatched tranquility. Spend your afternoon enjoying the world-renowned outdoor infinity whirlpool, heated to perfection and looking directly onto the snow-capped Himalayan ranges.'
                ),
                [
                    'Sightseeing Included: Mashobra forest vistas, Wildflower estate grounds exploration.',
                    'Evening Experience: Sunset viewing from the open deck with custom-brewed artisanal teas.',
                    'Overnight Stay: Wildflower Hall, An Oberoi Resort (Premier Valley View Room)',
                    "Meals Included: Premium Breakfast & Curated Chef's Tasting Dinner",
                ],
            ),            _day(
                4,
                'SANCTUARY NATURE TRAIL & PICNIC',
                (
                    "IMMERSIVE EXPERIENCES IN NATURE'S PRIVATE AMPHITHEATRE Wake up early to the soothing sound of the mountain wind. Today, enjoy an immersive experience: a private guided sanctuary nature trail through the protected pine reserves surrounding the estate. TRAGUIN experts have organized an exclusive, private gourmet picnic lunch at a secluded strawberry glade within the forest. Spend the rest of your day unwinding at the luxury spa pavilion or reading in the grand colonial library."
                ),
                [
                    'Sightseeing Included: Private Forest Sanctuary Trails, Cedar Glades, Wildflower paths.',
                    'Complimentary Experience: TRAGUIN Exclusive Private Forest Picnic with a dedicated butler.',
                    'Overnight Stay: Wildflower Hall, An Oberoi Resort (Premier Valley View Room)',
                    'Meals Included: Premium Breakfast, Forest Picnic Lunch, & Fine Dining Dinner',
                ],
            ),            _day(
                5,
                'EXCURSION TO KUFRI & NALDEHRA',
                (
                    'HIGH-ALTITUDE MEADOWS & ICONIC HIGHLAND GOLF TURFS Take a short, pleasant morning excursion to Kufri, a beautiful high-altitude meadow offering spectacular panoramic views of the inner Himalayan ranges. Later, proceed to Naldehra, home to one of India’s oldest and most scenic 9-hole golf courses, designed under the supervision of Lord Curzon. Walk hand-in-hand along the cedar-fringed fairways before returning to your luxury resort for a special farewell evening.'
                ),
                [
                    'Sightseeing Included: Kufri nature paths, Naldehra historical golf glades.',
                    'Evening Experience: Candle-lit farewell dinner organized in a private gazebo or the grand dining room.',
                    'Overnight Stay: Wildflower Hall, An Oberoi Resort (Premier Valley View Room)',
                    'Meals Included: Premium Breakfast & Gala Farewell Dinner',
                ],
            ),            _day(
                6,
                'DEPARTURE TO CHANDIGARH / DELHI',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES OF AN ELITE JOURNEY Savor your final gourmet breakfast as the mountain fog gently rolls across the cedar treetops. Pack your belongings as your private luxury SUV arrives to escort you down the scenic highway. Your chauffeur will drop you safely at Chandigarh or New Delhi Airport for your journey onward. Return home with a refreshed spirit and unforgettable memories designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door highway drop-off.',
                    'Meals Included: Lavish Breakfast Buffet',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Radisson Hotel Shimla /',
                'Himachal Pradesh',
                '05 Nights',
                'Deluxe',
                'similar',
                'Club Mahindra Mashobra /',
                4,
                1,
                description='OPTION 01 – DELUXE: Radisson Hotel Shimla / | similar | Club Mahindra Mashobra /',
            ),
            _hotel(
                'Marina Hotel /',
                'Himachal Pradesh',
                '05 Nights',
                'Premium',
                'Welcomhotel Shimla',
                'Tathagata Tents / Premium',
                4,
                2,
                description='OPTION 02 – PREMIUM: Marina Hotel / | Welcomhotel Shimla | Tathagata Tents / Premium',
            ),
            _hotel(
                'The Oberoi Cecil (Deluxe',
                'Himachal Pradesh',
                '05 Nights',
                'Luxury',
                'Room)',
                'Wildflower Hall (Deluxe',
                4,
                3,
                description='OPTION 03 – LUXURY: The Oberoi Cecil (Deluxe | Room) | Wildflower Hall (Deluxe',
            ),
            _hotel(
                'The Oberoi Cecil',
                'Himachal Pradesh',
                '05 Nights',
                'Ultra Luxury',
                '(Executive Suite)',
                'Wildflower Hall (Premier',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Oberoi Cecil | (Executive Suite) | Wildflower Hall (Premier',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury accommodations at Oberoi properties or similar chosen tiers.', 1),
            _inc_included('Luxury Transportation: Private dedicated Innova Crysta / Fortuner for all routes.', 2),
            _inc_included('Curated Meal Plan: Daily multi-cuisine breakfast and custom tasting dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated local guest relation officer on stand-by.', 4),
            _inc_included('Welcome Amenities: Personalized welcome kit, high-altitude chocolates, and refreshments.', 5),
            _inc_included('Complimentary Experience: Private guided forest sanctuary trail and luxury picnic.', 6),
            _inc_excluded('Domestic or International airfares and train tickets.', 7),
            _inc_excluded('Government monuments, museums, or historical property entry tickets.', 8),
            _inc_excluded('Personal items such as laundry, premium liquor, telephone calls, tips.', 9),
            _inc_excluded('Optional activities, green taxes, golf course rentals, or spa therapies. TRAGUIN Premium Luxury Itinerary — HP-014 5', 10),
        ],
    )
    return package, itinerary

def build_hp_015(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-015'
    tour_code = 'TRG-HIM-MICE-015'
    title = 'Corporate Himachal • Elevation, Leadership & Synergy'
    duration = '03 Nights / 04 Days'
    slug = 'hp-015-corporate-himachal-mice'
    itin_slug = 'hp-015-corporate-himachal-mice-itinerary'
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
            _ph('Serial code HP-015 | TRAGUIN tour code TRG-HIM-MICE-015', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Corporate MICE & Team Building', 2),
            _ph('Destinations: Shimla • Mashobra • Kufri • Naldera', 3),
            _ph('Ideal for: Corporate Conferences, Executive Retreats & Team Building', 4),
            _ph('Best season: April to July (Pleasant Summer) / October to March (Alpine Winter)', 5),
            _ph('Starting price: On Request (Bespoke Group Tariffs Offered)', 6),
            _ph('Vehicle / Meals: Luxury Multi-axle Coaches / APEX (All Meals & Gala Events)', 7),
            _ph('TRAGUIN Signature Experience: A mountain-top drone photography session with customized company', 8),
            _ph('Curated by TRAGUIN Experts: Seamless luggage check-in systems and prioritized lane passages across', 9),
            _ph('Premium Handpicked Hotels: Accommodations thoroughly vetted for executive safety, corporate', 10),
            _ph('Luxury Transportation: Highly vetted transit partners executing punctual multi-coach logistics with full', 11),
            _ph("Local Corporate Gifting: Reward your high performers with authentic wooden artifacts, high-quality woolen shawls from the local handloom emporiums, or premium artisanal forest honey from Himachal. Cafes & Culture: Experience the historic charm of Shimla's colonial-era bakeries, artisanal coffee venues along the Mall Road, and traditional Himachali food experiences designed to satisfy sophisticated global palates.", 12),
            _ph('Conference Booking: Final presentation layouts, seating choices (Cluster/Theater), and specialized AV', 13)
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
        price_note='On Request (Bespoke Group Tariffs Offered)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Corporate Himachal',
        overview="CORPORATE HIMACHAL • ELEVATION, LEADERSHIP & SYNERGY Welcome to a highly sophisticated corporate escape expertly curated by TRAGUIN. Align your organization's vision amidst the inspiring peaks of the Himalayas with the definitive Corporate Himachal retreat. As your dedicated corporate travel specialists, TRAGUIN transforms an ordinary business meeting into an exceptional luxury holiday, complete with state-of-the-art conference facilities, handpicked hotels, and exhilarating outdoor team-building sessions. Immerse your leadership teams in the scenic beauty of Shimla's alpine landscape, combining strategic focus with immersive experiences that foster unforgettable memories and long-term synergy.\n\nTOUR OVERVIEW\nThis elite corporate incentive and strategy retreat is designed exclusively for high-performing professional groups, key stakeholders, and leadership teams. Traveling in premium multi-axle luxury coaches under the seamless execution of a dedicated TRAGUIN tour director, the route balances analytical sessions with curated experiential rewards. Your customized meal plan includes expansive networking breakfasts, gourmet luncheon breaks, and elite themed Gala dinners. Every element incorporates the trademark TRAGUIN curated experience note, from smooth group check-ins and state-of-the-art AV logistics to premium stays and bespoke executive engagement options.\n\nWHY CHOOSE CORPORATE HIMACHAL FOR YOUR NEXT MICE EVENT?\nWhen planning a Luxury Himachal Holiday for corporate teams, businesses require spaces that seamlessly integrate dynamic professional facilities with untouched, breathtaking landscapes. Shimla serves as an extraordinary choice, making the signature Corporate Himachal Package an invaluable corporate asset. From exploring iconic attractions like the historic Viceregal Lodge and the ridge to undertaking high-altitude group ice-breakers in Kufri, Himachal sightseeing offers deep engagement. For companies looking to combine business milestones with team bonding, the region provides magnificent settings that serve as popular Instagram locations—such as the cedar groves of Mashobra and the manicured expanses of Naldera. Whether you are arranging an executive golf tournament, organizing group shopping excursions along the historic Mall Road, or enjoying traditional Himachali food experiences, our TRAGUIN Himachal Packages offer unparalleled corporate event management. Our commitment to premium stays and",
        seo_title='HP-015 | Corporate Himachal | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Himachal Pradesh package (HP-015 / TRG-HIM-MICE-015): Shimla • Mashobra • Kufri • Naldera with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SHIMLA & EXECUTIVE RETREAT WELCOME', 1),
            _ih('Day 02: STRATEGIC CONFERENCING & TEAM ALIGNMENT', 2),
            _ih('Day 03: OUTDOOR TEAM BUILDING & HIGHLAND SYNERGY', 3),
            _ih('Day 04: RESOLUTIONS & FLIGHT HOME', 4),
            _ih('TRAGUIN Signature Experience: A mountain-top drone photography session with customized company', 5),
            _ih('Curated by TRAGUIN Experts: Seamless luggage check-in systems and prioritized lane passages across', 6),
            _ih('Premium Handpicked Hotels: Accommodations thoroughly vetted for executive safety, corporate', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SHIMLA & EXECUTIVE RETREAT WELCOME',
                (
                    'MOUNTAIN ESCAPE – VIP ARRIVAL & NETWORKING RECEPTION Your premium Himachal corporate experience launches smoothly as your executive delegation lands at Chandigarh or Shimla Airport. A convoy of private luxury transport vehicles awaits to escort your team up through the pristine Shivalik hills. Arrive at your premium handpicked luxury resort, where a traditional Himachali welcome ceremony with custom brand badges has been organized. After checking in, assemble at the scenic overlooking deck for a high-tea reception, followed by an evening ice-breaker and cocktail networking session curated by TRAGUIN experts.'
                ),
                [
                    'Sightseeing Included: Scenic hillside transit routes, Resort panoramic deck viewing.',
                    'Evening Experience: Elite welcome cocktail reception with ice-breaking activities and corporate backdrop setup.',
                    'Overnight Stay: Shimla (Premium / Ultra-Luxury Convention Resort)',
                    'Meals Included: Hi-Tea, Premium Cocktails & Gourmet Welcome Dinner',
                ],
            ),            _day(
                2,
                'STRATEGIC CONFERENCING & TEAM ALIGNMENT',
                (
                    'ELEVATING VISION – STATE-OF-THE-ART SUMMIT & GALA NIGHT Power your morning with a nutritious, lavish buffet breakfast before moving into the state-of-the-art ballroom for your annual summit or strategic reviews. Enjoy top-tier audiovisual infrastructure, customized business stationery, and structured gourmet tea breaks. Following an open-air buffet luncheon, the delegation will step out for an afternoon corporate heritage walk to the historic Viceregal Lodge—an iconic attraction perfect for a team milestone group photograph. and fine dining.'
                ),
                [
                    'Sightseeing Included: Viceregal Lodge, The Ridge, Historic Christ Church, Mall Road.',
                    'Optional Activities: Private customized shopping tour on Mall Road for premium local handicrafts.',
                    'Evening Experience: Corporate Gala Night featuring live acoustic musical performances, award distributions,',
                    'Overnight Stay: Shimla (Premium / Ultra-Luxury Convention Resort)',
                    'Meals Included: Breakfast, Business Lunch, Mid-Session Refreshments & Gala Dinner',
                ],
            ),            _day(
                3,
                'OUTDOOR TEAM BUILDING & HIGHLAND SYNERGY',
                (
                    'COLLABORATIVE HORIZONS – ADVENTURE CHALLENGES IN MASHOBRA & KUFRI Ditch the formal attire for outdoor sports kits today. Head to the dramatic, breathtaking landscapes of Mashobra and Kufri for a custom experiential team-building program. Under the supervision of certified corporate coaches, your teams will engage in strategic wilderness mapping, trust-building obstacle courses, and collaborative archery tournaments. In the afternoon, enjoy an executive lunch breakout at a premium golf glade in Naldera, taking in the magnificent scenic beauty.'
                ),
                [
                    'Sightseeing Included: Kufri snow view points, Naldera cedar woods, Mashobra forest glades.',
                    'Optional Activities: Paragliding challenges, high-rope adventure setups, or a casual golf putting clinic.',
                    'Evening Experience: Alpine campfire celebration with traditional Himachali folk art and live barbeque.',
                    'Overnight Stay: Shimla (Premium / Ultra-Luxury Convention Resort)',
                    'Meals Included: Premium Breakfast, Highland Picnic Lunch & Barbeque Dinner',
                ],
            ),            _day(
                4,
                'RESOLUTIONS & FLIGHT HOME',
                (
                    'FORWARD STRATEGY – DEPARTURE WITH UNFORGETTABLE MEMORIES Enjoy a final morning breakfast session at the resort, finalizing action items and group resolutions. Your luxury transportation fleet will stand by to assist with smooth luggage check-out and boarding. Relax in comfort as you are driven back along the scenic national highway towards Chandigarh Airport/Station for your onward flight home, leaving with renewed corporate focus and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury group coach highway transfer to airport or station.',
                    'Meals Included: Sumptuous Farewell Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Radisson Hotel Shimla /',
                'Himachal Pradesh',
                '03 Nights',
                'Deluxe',
                'similar',
                'Corporate Hall with 150+ Pax',
                4,
                1,
                description='OPTION 01 – DELUXE: Radisson Hotel Shimla / | similar | Corporate Hall with 150+ Pax',
            ),
            _hotel(
                'The Orchid Hotel /',
                'Himachal Pradesh',
                '03 Nights',
                'Premium',
                'Welcomhotel by ITC',
                'Shimla',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Orchid Hotel / | Welcomhotel by ITC | Shimla',
            ),
            _hotel(
                'Taj Theig / Wildflower Hall',
                'Himachal Pradesh',
                '03 Nights',
                'Luxury',
                '(Oberoi Group)',
                'VVIP Executive Boardrooms',
                4,
                3,
                description='OPTION 03 – LUXURY: Taj Theig / Wildflower Hall | (Oberoi Group) | VVIP Executive Boardrooms',
            ),
            _hotel(
                'The Oberoi Cecil Luxury',
                'Himachal Pradesh',
                '03 Nights',
                'Ultra Luxury',
                'Corporate Wings',
                'Exclusive private palace',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Oberoi Cecil Luxury | Corporate Wings | Exclusive private palace',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 03 Nights accommodation at premium selected hotels.', 1),
            _inc_included('MICE Infrastructure: Complimentary main conference hall usage with premium AV gear.', 2),
            _inc_included('Luxury Transportation: Chauffeur-driven multi- axle luxury coach for group transfers & sightseeing.', 3),
            _inc_included('TRAGUIN Support: Two dedicated physical on-site MICE managers for group coordination.', 4),
            _inc_included('Gala Event & Breaks: Multi-tier networking breakfasts, lunches, and themed gala dinners.', 5),
            _inc_included('Corporate Experiences: Customized team- building exercises and forest trail permits.', 6),
            _inc_excluded('Domestic or International flight fares/train travel for delegates.', 7),
            _inc_excluded('Individual expenses such as room service mini- bars, laundry, or private tips.', 8),
            _inc_excluded('Specific specialized external artists or celebrity performers for Gala nights.', 9),
            _inc_excluded('Personalized sports equipment rental or professional golf green fees.', 10),
        ],
    )
    return package, itinerary

def build_hp_016(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-016'
    tour_code = 'TRG-HIM-ED016'
    title = 'Educational Himachal Tour'
    duration = '04 Nights / 05 Days'
    slug = 'hp-016-educational-himachal-tour'
    itin_slug = 'hp-016-educational-himachal-tour-itinerary'
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
            _ph('Serial code HP-016 | TRAGUIN tour code TRG-HIM-ED016', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Educational', 2),
            _ph('Destinations: Shimla • Kufri • Mashobra • Chail', 3),
            _ph('Ideal for: Students, Educators & Academic Institutions', 4),
            _ph('Best season: March to June & September to November', 5),
            _ph('Starting price: On Request (Institutional Student Rates)', 6),
            _ph('Vehicle / Meals: Premium Luxury Coaches / All Meals Included (APAI)', 7),
            _ph('TRAGUIN Signature Experience: Private group field interactive lecture at the Viceregal Lodge gardens', 8),
            _ph('Curated by TRAGUIN Experts: Safety-verified travel corridors avoiding narrow mountain roads during', 9),
            _ph('Personalized Assistance: Complimentary FOC (Free of Cost) teacher slots provided based on institution', 10),
            _ph('Exclusive Recommendations: Premium access to institutional lecture theatres and scientific research', 11),
            _ph('Local Markets & Collectibles: Students can securely browse Lakkar Bazaar under faculty supervision for authentic wooden handicrafts, geometric puzzle games, high-altitude honey, and beautiful traditional souvenirs. Cafes & Delicacies: Enjoy historical bakeries on the Mall Road featuring British-style crumpets, local apple crumbles, and traditional warm sweet pies.', 12),
            _ph('Hotel Policies: Room configurations and student-to-bed ratios are locked during booking initialization.', 13)
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
        price_note='On Request (Institutional Student Rates)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Educational Himachal Tour',
        overview='EDUCATIONAL HIMACHAL TOUR • LEARNING BEYOND CLASSROOMS Dear Educators and Students, Welcome to an enriching pedagogical expedition meticulously curated by TRAGUIN. We are proud to present our premier Educational Himachal Tour, engineered specifically to combine the pristine natural sciences, history, geography, and rich heritage of Himachal Pradesh into an elite outdoor classroom. As your professional travel consultants, TRAGUIN transforms standard excursions into a flawless luxury holiday framework where student safety, experiential learning, and premium stays converge. Witnessing the breathtaking landscapes and scenic beauty of the Himalayas provides a perfect backdrop for life-long inspiration and unforgettable memories.\n\nTOUR OVERVIEW\nThis institutional travel itinerary provides a balanced learning ecosystem across the historic summer capital of Shimla and surrounding eco-zones. Traveling in dedicated, luxury transportation coaches with seasoned mountain operators and certified medical assistance, your student group will experience absolute security and continuous engagement. Our curated experience note guarantees exclusive visits to historical architectural structures, environmental parks, meteorological stations, and indigenous craft centers. Accompanied by full- board healthy meal plans and carefully screened, premium student-friendly handpicked hotels, this is the definitive Premium Himachal Experience.\n\nWHY CHOOSE THE BEST HIMACHAL TOUR PACKAGE FOR SCHOOLS?\nAn extraordinary Educational Himachal Tour bridges the gap between theoretical textbooks and practical world observations. Himachal stands as a rich repository of geographical, meteorological, and cultural wonders. Choosing a specialized Himachal Family Tour or a structured institutional program allows students to research Himalayan tectonic geology, British-era colonial history, and unique mountain ecological patterns. Featuring iconic attractions like the Indian Institute of Advanced Study, the legendary Kufri Himalayan Nature Park, and the world-heritage Kalka-Shimla Toy Train track, Himachal sightseeing delivers incredible intellectual stimulation. For young explorers, the state offers popular Instagram locations that also double as environmental case study points, such as the Mashobra water catchment forest. Booking our signature TRAGUIN Himachal Packages ensures that your educational group receives immersive experiences, highly secure handpicked hotels, and structured interactive workshops during the absolute best time to visit Himachal.',
        seo_title='HP-016 | Educational Himachal Tour | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Himachal Pradesh package (HP-016 / TRG-HIM-ED016): Shimla • Kufri • Mashobra • Chail with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SHIMLA', 1),
            _ih('Day 02: HISTORIC SHIMLA HERITAGE EXPLORATION', 2),
            _ih('Day 03: KUFRI HIMALAYAN BIODIVERSITY STUDY', 3),
            _ih('Day 04: MASHOBRA NATURE RESERVES & CHAIL MILITARY HISTORY', 4),
            _ih('Day 05: HERITAGE TOY TRAIN RIDE & DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private group field interactive lecture at the Viceregal Lodge gardens', 6),
            _ih('Curated by TRAGUIN Experts: Safety-verified travel corridors avoiding narrow mountain roads during', 7),
            _ih('Personalized Assistance: Complimentary FOC (Free of Cost) teacher slots provided based on institution', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SHIMLA',
                (
                    'GATEWAY TO THE QUEEN OF HILLS – GEOGRAPHICAL TRANSITION Your premium educational journey commences upon arrival at Chandigarh or Delhi, where your high-end luxury transportation coaches await your institute. The scenic route up the winding Himalayan foothills serves as a living lesson in physical geography and altitudinal vegetation zones. Upon reaching Shimla, check into your handpicked hotels selected specifically for maximum student group safety and premium amenities. Gather for a formal orientation session in the evening conducted by your TRAGUIN tour manager detailing the days ahead.'
                ),
                [
                    'Sightseeing Included: Shivalik foothill pass, Pinjore-Parwanoo tectonic zone view.',
                    'Evening Experience: Interactive group icebreaker session and documentary screening on Himalayan geology.',
                    'Overnight Stay: Shimla (Premium Student-Friendly Resort / Hotel)',
                    'Meals Included: Welcome Evening Drinks & Freshly Prepared Buffet Dinner',
                ],
            ),            _day(
                2,
                'HISTORIC SHIMLA HERITAGE EXPLORATION',
                (
                    "COLONIAL ARCHITECTURE & POLITICAL HISTORY OF BRITISH INDIA Relish a nutritious breakfast before heading out for a profound historical immersion. Visit the magnificent Indian Institute of Advanced Study (Viceregal Lodge), an architectural marvel in the Scottish Baronial style where critical historic decisions regarding India's partition were signed. Walk through the sprawling gardens to understand the mountain eco-construction methods of the 19th century. Later, visit the heritage State Museum and take an educational walk down the Ridge, visiting Christ Church and Gaiety Theatre."
                ),
                [
                    'Sightseeing Included: Viceregal Lodge, Himachal State Museum, The Ridge, Mall Road, Gaiety Theatre.',
                    'Optional Activities: Interactive Q&A session with a local historian regarding colonial mountain urbanism.',
                    'Overnight Stay: Shimla (Premium Student-Friendly Resort / Hotel)',
                    'Meals Included: Healthy Breakfast, Warm Lunch & Elaborate Buffet Dinner',
                ],
            ),            _day(
                3,
                'KUFRI HIMALAYAN BIODIVERSITY STUDY',
                (
                    'BOTANICAL RICHNESS, FAUNA RECONNAISSANCE & ECO-BALANCE Depart early for Kufri, situated at an altitude of 2,630 meters, showcasing breathtaking landscapes and severe pine alpine forests. Visit the Himalayan Nature Park, home to rare high-altitude wildlife like the Snow Leopard, Tibetan Wolf, and Himalayan Monal. Students will participate in a structured biodiversity mapping worksheet exercise. After lunch, visit the local apple orchard belts to study mountain agricultural techniques and terrace farming economics.'
                ),
                [
                    'Sightseeing Included: Kufri Himalayan Nature Park, Mahasu Peak flora paths, local agricultural steps.',
                    'Evening Experience: Group campfire night with educational astronomy and stargazing over the clear skies.',
                    'Overnight Stay: Shimla / Kufri Group Resort',
                    'Meals Included: Full Board Plan (Breakfast, Lunch & Dinner)',
                ],
            ),            _day(
                4,
                'MASHOBRA NATURE RESERVES & CHAIL MILITARY HISTORY',
                (
                    "HYDROLOGY WONDERS & HIGHEST CRICKET GROUND VISIT Dedicate your morning to exploring Mashobra, a dense oak and pine forest reserve that serves as one of Asia's largest natural water catchment zones. This field excursion focuses on water harvesting systems and sustainable mountain lifestyle models. In the afternoon, journey to Chail to explore the majestic Chail Palace and stand on the world's highest cricket ground at 2,444 meters, learning about its unique sports history and strategic military alignment."
                ),
                [
                    'Sightseeing Included: Mashobra Water Reserve, Chail Palace, Chail Military School Cricket Ground.',
                    'Optional Activities: Light team-building adventure ropes course under trained instructors.',
                    'Overnight Stay: Shimla (Premium Student-Friendly Resort)',
                    'Meals Included: Breakfast, Packed Field Lunch & Institutional Gala Dinner',
                ],
            ),            _day(
                5,
                'HERITAGE TOY TRAIN RIDE & DEPARTURE',
                (
                    'UNESCO ENGINEERING MARVEL – CHERISHING UNFORGETTABLE MEMORIES The pinnacle of your educational journey arrives with a custom group ride on the UNESCO World Heritage Kalka-Shimla Toy Train. This historical rail track highlights 103 spectacular tunnels and multi-arched gallery bridges built over a century ago. Understand the brilliant mechanical physics behind mountain rail engineering. Disembark and board your luxury transportation coaches for your departure journey home. Your academic trip concludes with deep bonds and unforgettable memories meticulously structured by TRAGUIN.'
                ),
                [
                    'Transfers Included: Toy train experience tickets followed by private luxury coach drop-off.',
                    'Meals Included: Sumptuous Breakfast & On-Route Midday Meal',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Asia The Dawn / East',
                'Himachal Pradesh',
                '04 Nights',
                'Deluxe',
                'Bourne Resort / similar',
                'Triple / Quad Shared Elite',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Asia The Dawn / East | Bourne Resort / similar | Triple / Quad Shared Elite',
            ),
            _hotel(
                'Hotel Willow Banks / Sterling',
                'Himachal Pradesh',
                '04 Nights',
                'Premium',
                'Shimla / similar',
                'Triple Shared Premium',
                4,
                2,
                description='OPTION 02 – PREMIUM: Hotel Willow Banks / Sterling | Shimla / similar | Triple Shared Premium',
            ),
            _hotel(
                'Radisson Hotel Shimla /',
                'Himachal Pradesh',
                '04 Nights',
                'Luxury',
                'Welcomhotel Shimla',
                'Double Shared Twin Luxury',
                4,
                3,
                description='OPTION 03 – LUXURY: Radisson Hotel Shimla / | Welcomhotel Shimla | Double Shared Twin Luxury',
            ),
            _hotel(
                'Wildflower Hall / The Oberoi',
                'Himachal Pradesh',
                '04 Nights',
                'Ultra Luxury',
                'Cecil (Faculty Premium)',
                'Exclusive Premium Club',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Wildflower Hall / The Oberoi | Cecil (Faculty Premium) | Exclusive Premium Club',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 04 Nights in student-safe, heavily screened handpicked hotels.', 1),
            _inc_included('Luxury Transportation: High-end air- conditioned private touring coaches.', 2),
            _inc_included('Institutional Meal Plan: Full-board multi-cuisine healthy menus (Breakfast, Lunch & Dinner).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated tour escort managers and first-aid safety personnel.', 4),
            _inc_included('Complimentary Experience: Reserved tickets for the UNESCO World Heritage Toy Train ride.', 5),
            _inc_included('Academic Features: Custom student learning worksheets, field maps, and pens.', 6),
            _inc_excluded('Major commercial airfares or long-distance interstate express train tickets.', 7),
            _inc_excluded('Individual', 8),
        ],
    )
    return package, itinerary

def build_hp_017(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-017'
    tour_code = 'TRG-HP-017'
    title = 'Dharamshala Escape • Serenity, Spirituality & Peaks'
    duration = '04 Nights / 05 Days'
    slug = 'hp-017-dharamshala-escape'
    itin_slug = 'hp-017-dharamshala-escape-itinerary'
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
            _ph('Serial code HP-017 | TRAGUIN tour code TRG-HP-017', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Premium Family', 2),
            _ph('Destinations: Dharamshala • Mcleodganj • Dharamkot • Naddi • Palampur', 3),
            _ph('Ideal for: Family Vacations, Cultural Explorers & Nature Lovers', 4),
            _ph('Best season: March to June & September to December', 5),
            _ph('Starting price: On Request (Premium Customised)', 6),
            _ph('Vehicle / Meals: Luxury Innova Crysta / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private guided heritage walk through the Norbulingka Institute to', 8),
            _ph('Curated by TRAGUIN Experts: Carefully planned daily drives that ensure plenty of relaxed family time.', 9),
            _ph('Premium Handpicked Hotels: Accommodations selected for their high safety standards, stunning views,', 10),
            _ph('Luxury Transportation: Expert, uniform-clad mountain drivers who know the best spots for photography.', 11),
            _ph('Hotel Policies: Check-in time is 14:00 hrs and check-out is 11:00 hrs. Please bring a valid government-', 12),
            _ph('issued photo ID card.', 13)
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
        tagline='Dharamshala Escape',
        overview='DHARAMSHALA ESCAPE • SERENITY, SPIRITUALITY & PEAKS Welcome to a breathtaking family adventure proudly curated by TRAGUIN. Embark on the finest Dharamshala Family Tour designed to uncover the mystical charms, spiritual depths, and stunning pine- clad peaks of the Dhauladhar range. As your luxury travel consultant, TRAGUIN transforms your retreat into a seamless luxury holiday packed with handpicked hotels, refreshing scenic beauty, and heartwarming local stories. From the sacred, peaceful chanting at the Dalai Lama Temple to the rich colonial heritage of Palampur, every element is designed to craft unforgettable memories for you and your family.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers an exquisite blend of Tibetan spirituality, pristine pine forests, high-altitude sports, and rolling green tea estates. Travelling in a completely private premium AC vehicle with a highly knowledgeable local chauffeur-guide, your family is assured absolute comfort, safety, and leisure. Featuring a refined meal plan comprising lavish daily breakfasts and specialized dinners, this route represents the definitive premium Dharamshala experience. Every single phase of your vacation includes the hallmark TRAGUIN curated experiences, assuring personalized assistance, exclusive recommendations, and seamless entry privileges everywhere.\n\nWHY CHOOSE THE BEST DHARAMSHALA TOUR PACKAGE?\nWhen considering a Luxury Himachal Holiday, discerning travellers seek a profound mix of untouched nature, rich culture, and top-tier comfort. Dharamshala is a world-class hill station offering some of the most iconic attractions in Northern India. From the internationally admired Tsuglagkhang Complex (Dalai Lama Temple)—a top tourist place in Dharamshala for cultural deep dives—to the high-altitude bliss of Naddi View Point, the valley overflows with beauty. For couples and families reserving a specialized Dharamshala Honeymoon Package or Dharamshala Family Tour, this region unveils stellar popular Instagram locations such as the HPCA Cricket Stadium, the historic St. John in the Wilderness Church, and the misty paths of Bhagsunag Waterfall. Whether you are looking for authentic Tibetan handicraft shopping, exploring lush tea gardens, or seeking inner peace under the shade of giant deodars, our customized TRAGUIN Himachal Packages guarantee premium stays, immersive experiences, and handpicked luxury hotels that reveal the absolute best time to visit Himachal.',
        seo_title='HP-017 | Dharamshala Escape | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Himachal Pradesh package (HP-017 / TRG-HP-017): Dharamshala • Mcleodganj • Dharamkot • Naddi • Palampur with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DHARAMSHALA', 1),
            _ih('Day 02: MCLEODGANJ SPIRITUAL & HERITAGE TOUR', 2),
            _ih('Day 03: EXCURSION TO NADDI VIEW POINT & DHARAMKOT', 3),
            _ih('Day 04: PALAMPUR TEA GARDENS DAY TRIP', 4),
            _ih('Day 05: DHARAMSHALA TO DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private guided heritage walk through the Norbulingka Institute to', 6),
            _ih('Curated by TRAGUIN Experts: Carefully planned daily drives that ensure plenty of relaxed family time.', 7),
            _ih('Premium Handpicked Hotels: Accommodations selected for their high safety standards, stunning views,', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DHARAMSHALA',
                (
                    'WELCOME TO THE DHARAMSHALA RETREAT – SPIRITUAL BEGINNINGS Your premium Himachal experience starts as you arrive at Pathankot Railway Station or Gaggal Airport, where your private luxury transportation vehicle awaits to greet you. Drive through winding, pine-scented mountain roads with vistas of cascading streams until you reach Dharamshala. Check into your premium handpicked luxury hotel and settle down. In the afternoon, take a relaxed family walk to explore the local markets or enjoy a warm cup of Tibetan tea at a cozy café overlooking the valley.'
                ),
                [
                    'Sightseeing Included: Scenic valley drive, local market stroll, orientation walk.',
                    'Evening Experience: Traditional welcome drinks and a curated multi-course dinner at the resort.',
                    'Overnight Stay: Dharamshala (Premium Luxury Resort View Room)',
                    'Meals Included: Welcome Drink & Luxury Welcome Dinner',
                ],
            ),            _day(
                2,
                'MCLEODGANJ SPIRITUAL & HERITAGE TOUR',
                (
                    'LITTLE LHASA – TIBETAN CULTURE & THE MAJESTIC DHAULADHARS Awake to a peaceful mountain sunrise and a lavish breakfast. Today, immerse yourself in Mcleodganj sightseeing, the vibrant home of His Holiness the Dalai Lama. Visit the tranquil Tsuglagkhang Temple complex, where you can watch monks debating in the courtyard and turn the sacred prayer wheels. Afterward, explore the neo-Gothic St. John in the Wilderness Church, built in 1852 amidst dense deodar woods. Conclude your afternoon by trekking a short, scenic route to the beautiful Bhagsunag Waterfall. Road.'
                ),
                [
                    'Sightseeing Included: Dalai Lama Temple, St. John Church, Bhagsunag Temple & Waterfall, Mcleodganj Mall',
                    'Optional Activities: Private guided meditation session or an interactive Tibetan cooking class.',
                    'Overnight Stay: Dharamshala (Premium Luxury Resort View Room)',
                    'Meals Included: Premium Breakfast & Gourmet Dinner',
                ],
            ),            _day(
                3,
                'EXCURSION TO NADDI VIEW POINT & DHARAMKOT',
                (
                    "PANORAMIC PEAKS, SUNSET GLORY & HIPPIE SERENITY Following a delicious breakfast, your luxury transportation takes you higher up the mountainside to Naddi Village. This spot offers stunning landscapes and panoramic close-up views of the snow-clad Dhauladhar peaks, making it a highly popular Instagram location. Next, journey to the peaceful village of Dharamkot, often called the 'Hippie Village' of Himachal, known for its tranquil vibe and wellness cafes. Spend your late afternoon visiting the Dal Lake of Dharamshala, a sacred pond enclosed by ancient deodar trees. area."
                ),
                [
                    "Sightseeing Included: Naddi Sunset Point, Dharamkot Eco Village, Sacred Dal Lake, Tibetan Children's Village",
                    'Evening Experience: A private sunset tea session at Naddi with reserved premium terrace seating.',
                    'Overnight Stay: Dharamshala (Premium Luxury Resort View Room)',
                    'Meals Included: Premium Breakfast & Traditional Himachali Dinner',
                ],
            ),            _day(
                4,
                'PALAMPUR TEA GARDENS DAY TRIP',
                (
                    'THE GREEN VALLEY – TEA CARPETS & COLONIAL SPLENDOUR Embark on a scenic day excursion to Palampur, the tea capital of Northwest India. The drive itself is filled with scenic beauty, taking you past pine forests and over gushing mountain streams. Walk through lush green tea estates, breathe in the fresh aroma of tea leaves, and take beautiful family photographs. Later, visit the historic Baijnath Temple, a 13th-century architectural masterpiece dedicated to Lord Shiva, before driving past the iconic HPCA Stadium in Dharamshala on your return.'
                ),
                [
                    'Sightseeing Included: Palampur Tea Estates, Baijnath Temple, Norbulingka Institute, HPCA Cricket Stadium.',
                    'Evening Experience: A guided tour of the tea factory followed by an exclusive tea-tasting session.',
                    'Overnight Stay: Dharamshala (Premium Luxury Resort View Room)',
                    'Meals Included: Premium Breakfast & Farewell Gala Dinner',
                ],
            ),            _day(
                5,
                'DHARAMSHALA TO DEPARTURE',
                (
                    'CHERISHING FAREWELL MOMENTS – MEMORIES FOR A LIFETIME Enjoy a final luxury breakfast at your resort while taking in the morning mountain views. Pack your bags as your dedicated private luxury vehicle arrives to escort you back to Pathankot or Gaggal Airport for your journey home. Leave the hills behind with your heart full of peace, joy, and unforgettable memories designed beautifully by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door station or airport drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Pride Surya Mountain Resort / Hotel',
                'Himachal Pradesh',
                '04 Nights',
                'Deluxe',
                'Imperial / similar',
                'Deluxe Valley View',
                4,
                1,
                description='OPTION 01 – DELUXE: Pride Surya Mountain Resort / Hotel | Imperial / similar | Deluxe Valley View',
            ),
            _hotel(
                'Regenta Resort Camellia / Fortune',
                'Himachal Pradesh',
                '04 Nights',
                'Premium',
                'Park Moksha',
                'Premium Balcony',
                4,
                2,
                description='OPTION 02 – PREMIUM: Regenta Resort Camellia / Fortune | Park Moksha | Premium Balcony',
            ),
            _hotel(
                'Hyatt Regency Dharamshala Resort /',
                'Himachal Pradesh',
                '04 Nights',
                'Luxury',
                'Radisson Blu',
                'Luxury Club Resort',
                4,
                3,
                description='OPTION 03 – LUXURY: Hyatt Regency Dharamshala Resort / | Radisson Blu | Luxury Club Resort',
            ),
            _hotel(
                'The Pavilion by HPCA / Luxurious',
                'Himachal Pradesh',
                '04 Nights',
                'Ultra Luxury',
                'Private Mountain Villa',
                'VVIP Royal',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Pavilion by HPCA / Luxurious | Private Mountain Villa | VVIP Royal',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 04 Nights in handpicked luxury mountain hotels.', 1),
            _inc_included('Luxury Transportation: Private AC Innova Crysta for all transfers and sightseeing.', 2),
            _inc_included('Curated Meal Plan: Lavish daily buffet breakfasts and premium dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated local guest experience manager assistance.', 4),
            _inc_included('Welcome Kit: Warm traditional shawl welcome and customized family amenities.', 5),
            _inc_included('Complimentary Experience: Curated family tea tasting tour in Palampur.', 6),
            _inc_excluded('Airfare, flight tickets, or main train travel.', 7),
            _inc_excluded('Monument entry tickets, paragliding, or ropeway ride charges.', 8),
            _inc_excluded('Personal expenses like laundry, phone calls, or tips.', 9),
            _inc_excluded('Any optional adventure activities or extended tours.', 10),
        ],
    )
    return package, itinerary

def build_hp_018(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-018'
    tour_code = 'TRG-HP-018'
    title = 'Shimla Kasol Delight • The Royal Ridge to the Mystic Valley'
    duration = '05 Nights / 06 Days'
    slug = 'hp-018-shimla-kasol-delight'
    itin_slug = 'hp-018-shimla-kasol-delight-itinerary'
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
            _ph('Serial code HP-018 | TRAGUIN tour code TRG-HP-018', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Premium Family', 2),
            _ph('Destinations: Shimla • Kufri • Kasol • Manikaran Sahib • Kullu Valley', 3),
            _ph('Ideal for: Family Getaways, Mountain Explorers & Culture Lovers', 4),
            _ph('Best season: April to June (Summer Resort) / October to March (Snowfall)', 5),
            _ph('Starting price: On Request (Premium Customised Family Package)', 6),
            _ph('Vehicle / Meals: Private Luxury Innova Crysta / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private colonial architecture walking tour on the Shimla Ridge with a', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked mountain driving times to ensure leisurely coffee stops and', 9),
            _ph('Premium Handpicked Hotels: Elite properties selected for their stunning views, strict family safety', 10),
            _ph('Luxury Transportation: Chauffeur-driven executive vehicles equipped with emergency kits and pristine', 11),
            _ph("Local Markets & Souvenirs: Explore Shimla's Lakkar Bazar for beautiful handcrafted wooden toys and artifacts. In Kullu, shop for globally celebrated, authentic hand-loomed Kullu shawls, warm pashminas, and local carpets. Cafes & Food: Kasol's local wooden streets are lined with ambient cafes offering authentic Israeli cuisine, fresh river trout delicacies, wood-fired pizzas, and rich mountain teas accompanied by live music.", 12),
            _ph('Hotel Policies: Standard check-in is 14:00 hrs and check-out is 11:00 hrs. Government IDs are required', 13)
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
        price_note='On Request (Premium Customised Family Package)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Shimla Kasol Delight',
        overview='SHIMLA KASOL DELIGHT • THE ROYAL RIDGE TO THE MYSTIC VALLEY Welcome to an unforgettable mountain retreat designed by TRAGUIN. Embark on the finest Himachal Family Tour engineered to perfectly unite the colonial majesty of Shimla with the serene, pine-scented bohemian tranquility of Kasol. As your trusted premium travel consultants, TRAGUIN elevates your holiday into an inspiring luxury experience complete with handpicked hotels, breathtaking landscapes, and exclusive experiences. From family moments on the snow-dusted heights of Kufri to an immersive spiritual visit at Manikaran Sahib, every detail is woven with emotional storytelling to gift your family unforgettable memories.\n\nTOUR OVERVIEW\nThis custom luxury holiday package offers a phenomenal route traversing the changing layers of Himachal Pradesh. Moving from the well-manicured, historical hillsides of the former summer capital to the rushing, crystal-clear Parvati River waters in Kasol, your family travels in absolute style. Your private premium vehicle provides effortless luxury transportation across every mountain switchback, led by an experienced hill chauffeur. With a premium meal plan including expansive hot buffet breakfasts and curated multi-cuisine dinners, this itinerary brings you the ultimate premium Himachal experience. Every step incorporates a dedicated TRAGUIN curated experience note, guaranteeing priority assistance and unmatched travel refinement.\n\nWHY CHOOSE THE BEST HIMACHAL TOUR PACKAGE?\nWhen search-conscious travelers lock in a Luxury Himachal Holiday, they look for iconic attractions paired with hidden, serene escape points. Shimla remains the absolute king of colonial hill heritage, making a Shimla Family Tour or a romantic Himachal Honeymoon Package deeply popular. From taking family walks along the vehicle-free Ridge to discovering the mist-wrapped conifer valleys, Shimla sightseeing never fails to captivate. Further down the valley, Kasol introduces you to spectacular natural trails and popular Instagram locations along the winding Parvati River. Whether you want to experience the spiritual thermal springs of Manikaran, capture the wooden architectural marvels, shop for hand-woven woolen shawls at Kullu, or sit inside bohemian riverside cafes, our custom TRAGUIN Himachal Packages provide the perfect solution. We guarantee premium stays, handpicked hotels, and curated exclusive experiences that outline the best time to visit Himachal.',
        seo_title='HP-018 | Shimla Kasol Delight | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Himachal Pradesh package (HP-018 / TRG-HP-018): Shimla • Kufri • Kasol • Manikaran Sahib • Kullu Valley with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SHIMLA', 1),
            _ih('Day 02: KUFRI EXCURSION & JAKHOO HILL', 2),
            _ih('Day 03: SHIMLA TO KASOL VIA KULLU VALLEY', 3),
            _ih('Day 04: KASOL & MANIKARAN SAHIB EXCURSION', 4),
            _ih('Day 05: EXCURSION TO TOSH OR JIBHI EDGE', 5),
            _ih('Day 06: KASOL TO DELHI / CHANDIGARH DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private colonial architecture walking tour on the Shimla Ridge with a', 7),
            _ih('Curated by TRAGUIN Experts: Handpicked mountain driving times to ensure leisurely coffee stops and', 8),
            _ih('Premium Handpicked Hotels: Elite properties selected for their stunning views, strict family safety', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SHIMLA',
                (
                    'WELCOME TO THE SUMMER CAPITAL – HIGH-LIFESTYLE RIDGE STROLL Your premium Himachal experience initiates as you touch down at Chandigarh or Delhi, where your professional chauffeur welcomes you with your private luxury transport. Enjoy a highly scenic route winding through the lower Shivalik hills, arriving at your handpicked premium resort in Shimla. After a relaxed check-in, step out to experience the iconic Mall Road, The Ridge, and the historical neo-Gothic Christ Church. The absence of motor vehicle traffic on the Mall ensures a peaceful walking and shopping atmosphere for your family.'
                ),
                [
                    'Sightseeing Included: The Ridge, Mall Road, Christ Church, Scandal Point, Gaiety Theatre.',
                    'Evening Experience: Bespoke colonial-era walking tour followed by dinner curated by TRAGUIN experts.',
                    'Overnight Stay: Shimla (Premium Luxury Heritage Resort)',
                    'Meals Included: Welcome Mountain Drink & Gourmet Buffet Dinner',
                ],
            ),            _day(
                2,
                'KUFRI EXCURSION & JAKHOO HILL',
                (
                    'PANORAMIC SNOW PEAKS & ECO-HIGHLANDS Relish a rich buffet breakfast before driving to Kufri, one of the top tourist places in Himachal for panoramic Himalayan views. Pass through the lush green Hasan Valley, capturing magnificent photography points along the way. In Kufri, enjoy immersive experiences like family horse riding or walking through the Himalayan Nature Park. On your return, head up to Jakhoo Hill—the highest peak in Shimla—to see the monumental 108-foot Hanuman Statue and catch a brilliant sunset view.'
                ),
                [
                    'Sightseeing Included: Kufri Meadows, Hasan Valley Viewpoint, Jakhoo Temple, Indira Tourist Park.',
                    'Optional Activities: Traditional Himachali attire family portrait session amidst pine forests.',
                    'Overnight Stay: Shimla (Premium Luxury Heritage Resort)',
                    'Meals Included: Premium Breakfast & Specialized Family Dinner',
                ],
            ),            _day(
                3,
                'SHIMLA TO KASOL VIA KULLU VALLEY',
                (
                    'SCENIC DRIVE ALONG THE PARVATI RIVER CANYON Bid adieu to Shimla after breakfast and head down the grand mountain highways toward the mystical Parvati Valley. This scenic route takes you right through the heart of the Kullu Valley. Stop along the banks of the roaring Beas River for refreshing photography and optional river rafting. By afternoon, your luxury vehicle enters the emerald pine borders of Kasol. Check into your premium riverside hotel and relax to the therapeutic sound of the flowing water.'
                ),
                [
                    'Sightseeing Included: Kullu Valley views, Pandoh Dam en-route, Parvati River banks.',
                    'Evening Experience: Private riverside family bonfire with hot mountain refreshments.',
                    'Overnight Stay: Kasol (Premium Handpicked Riverside Luxury Resort)',
                    'Meals Included: Breakfast & Riverside Buffet Dinner',
                ],
            ),            _day(
                4,
                'KASOL & MANIKARAN SAHIB EXCURSION',
                (
                    'SPIRITUAL THERMAL SPRINGS & BOHEMIAN NATURE TRAILS Today highlights the natural spiritual duality of the valley. Visit the holy Manikaran Sahib Gurudwara, a revered pilgrimage destination famous for its powerful natural hot sulfur springs that run parallel to the icy river waters. Learn the fascinating history of the shrine and partake in the community Langar kitchen. The afternoon leads you back to Kasol to explore the pine trails of Chalal village and the trendy local wooden markets.'
                ),
                [
                    'Sightseeing Included: Manikaran Gurudwara, Lord Shiva Temple, Chalal Suspension Bridge, Kasol Market.',
                    'Optional Activities: A guided wellness cafe tour to sample artisan wood-fired bakery delights.',
                    'Overnight Stay: Kasol (Premium Handpicked Riverside Luxury Resort)',
                    'Meals Included: Premium Breakfast & Organic Valley Dinner',
                ],
            ),            _day(
                5,
                'EXCURSION TO TOSH OR JIBHI EDGE',
                (
                    'UNTOUCHED ALPINE SPLENDOUR & IMPRECISE VISTAS Embark on a morning excursion further up the valley to see traditional wooden Himalayan villages perched on step-cropped hillsides. Walk past pristine streams, apple orchards, and cascading mountain waterfalls. This region offers a quiet retreat far from busy tourist tracks, presenting breathtaking landscapes and popular Instagram locations perfect for capturing your family trip. Return to your luxury resort for a final celebratory evening.'
                ),
                [
                    'Sightseeing Included: Alpine valley vistas, Local wooden village walk, Cascade waterfalls.',
                    'Evening Experience: Special farewell family dinner setup with personalized menu curation.',
                    'Overnight Stay: Kasol (Premium Handpicked Riverside Luxury Resort)',
                    'Meals Included: Breakfast & Farewell Premium Dinner',
                ],
            ),            _day(
                6,
                'KASOL TO DELHI / CHANDIGARH DEPARTURE',
                (
                    'CHERISHING SWEET FAMILY JOURNEYS FOREVER Enjoy your final luxury breakfast overlooking the misty Parvati valley peaks. Pack your bags as your private luxury vehicle safely drives you down the smooth national highways back to Chandigarh or New Delhi Airport for your return home. Your incredible mountain escape concludes, leaving you with unforgettable memories crafted beautifully by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door highway transfer drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Willow Banks / East',
                'Himachal Pradesh',
                '05 Nights',
                'Deluxe',
                'Bourne / similar',
                'The Parvati Kuteer / Hotel',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Willow Banks / East | Bourne / similar | The Parvati Kuteer / Hotel',
            ),
            _hotel(
                'Radisson Hotel Shimla /',
                'Himachal Pradesh',
                '05 Nights',
                'Premium',
                'Marina / similar',
                'Kasol Camps & Resorts /',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Hotel Shimla / | Marina / similar | Kasol Camps & Resorts /',
            ),
            _hotel(
                'The Orchid Hotel /',
                'Himachal Pradesh',
                '05 Nights',
                'Luxury',
                'Welcomhotel by ITC',
                'Echor Riverside Resort /',
                4,
                3,
                description='OPTION 03 – LUXURY: The Orchid Hotel / | Welcomhotel by ITC | Echor Riverside Resort /',
            ),
            _hotel(
                'Wildflower Hall / The Oberoi',
                'Himachal Pradesh',
                '05 Nights',
                'Ultra Luxury',
                'Cecil (Suites)',
                'VVIP Private Luxury Alpine',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Wildflower Hall / The Oberoi | Cecil (Suites) | VVIP Private Luxury Alpine',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury accommodations as per specified selection tier.', 1),
            _inc_included('Luxury Transportation: Private Innova Crysta for all point-to-point tours.', 2),
            _inc_included('Curated Meals: Premium hot buffet breakfasts and delicious table-service dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated local guest relation manager on assignment.', 4),
            _inc_included('Welcome Kit: Customized family welcome pack with travel treats on arrival.', 5),
            _inc_included('Complimentary Experience: Private family bonfire event in Parvati Valley. TRAGUIN Premium Luxury Itinerary — HP-018 5', 6),
            _inc_excluded('Domestic flights, airfare, or train ticketing to/from arrival points.', 7),
            _inc_excluded('River rafting fees, horse riding tickets, adventure park costs.', 8),
            _inc_excluded('Personal items such as laundry, phone calls, drinks, or gratuities.', 9),
            _inc_excluded('Monument entry fees, camera passes, or local guide hire.', 10),
        ],
    )
    return package, itinerary

def build_hp_019(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-019'
    tour_code = 'TRG-HIM-019'
    title = 'Manali & Dharamshala Family Explorer'
    duration = '06 Nights / 07 Days'
    slug = 'hp-019-manali-dharamshala-family'
    itin_slug = 'hp-019-manali-dharamshala-family-itinerary'
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
            _ph('Serial code HP-019 | TRAGUIN tour code TRG-HIM-019', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Premium Family', 2),
            _ph('Destinations: Manali • Solang Valley • Dharamshala • Mcleodganj', 3),
            _ph('Ideal for: Family Vacations, Heritage Seekers & Luxury Explorers', 4),
            _ph('Best season: March to June & September to December', 5),
            _ph('Starting price: On Request (Premium Customized)', 6),
            _ph('Vehicle / Meals: Private Luxury Innova Crysta / MAPAI Plan', 7),
            _ph('TRAGUIN Signature Experience: Private curated tea-tasting session at an estate in Palampur, featuring', 8),
            _ph('Curated by TRAGUIN Experts: Relaxed, scenic routes designed to minimize travel fatigue for families.', 9),
            _ph('Premium Handpicked Hotels: Accommodations selected strictly based on flawless safety standards and', 10),
            _ph('Luxury Transportation: Expert hill drivers ensuring elite comfort and safety across mountain routes.', 11),
            _ph('Hotel Policies: Standard check-in time is 14:00 hrs and check-out is 11:00 hrs. Valid government-issued', 12),
            _ph('photo IDs are mandatory.', 13)
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
        price_note='On Request (Premium Customized)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Manali & Dharamshala Family Explorer',
        overview='MANALI & DHARAMSHALA FAMILY EXPLORER Welcome to an extraordinary Alpine vacation curated exclusively by TRAGUIN. Embark on the finest Himachal Family Tour, thoughtfully tailored to showcase the breathtaking landscapes, ancient spiritual sanctuaries, and mist-covered pine forests of Manali and Dharamshala. As your dedicated luxury travel consultants, TRAGUIN delivers a completely seamless luxury holiday filled with handpicked hotels, experiential detours, and absolute premium comfort. Let the majestic Dhauladhar ranges and the dramatic river vistas form the backdrop of your journey, ensuring sweet unforgettable memories for your family.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers an exceptional balance between high-altitude Alpine adventure and serene spiritual heritage. Travelling in a completely private premium AC vehicle with a highly skilled local chauffeur, your family will explore the iconic destinations of Himachal in unmatched style. Enjoy a carefully curated meal plan featuring lavish breakfasts and specialized multi-cuisine dinners. Every stage of your holiday reflects the signature TRAGUIN curated experience note, ensuring priority VIP access, expert local guidance, and round-the-clock specialized support.\n\nWHY CHOOSE THE BEST HIMACHAL TOUR PACKAGE?\nWhen considering a Luxury Himachal Holiday, discerning families seek a journey that seamlessly blends dynamic adventure with cultural depth. The combination of Manali and Dharamshala stands out as the ultimate choice, offering a top-rated Himachal Family Tour opportunity. From the pristine, snow-clad slopes of Solang Valley—a globally famous playground for family adventure—to the tranquil, prayer-flag-lined ridges of McLeodganj in Dharamshala, this circuit brings you close to top tourist places in Himachal. For families and newlyweds seeking a romantic Himachal Honeymoon Package, this route highlights beautiful Instagram locations like the Dalai Lama Temple, the high-altitude tea gardens, and the tranquil shores of Dal Lake. Indulge in local artifact shopping at the vibrant Tibetan bazaars, experience the pure bliss of riverside dining along the Beas River, and absorb the deep spiritual heritage of the Tibetan community. Our signature TRAGUIN Himachal Packages pair exclusive experiences with handpicked premium stays to ensure the absolute best time to visit Himachal with your loved ones.',
        seo_title='HP-019 | Manali & Dharamshala Family Explorer | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Himachal Pradesh package (HP-019 / TRG-HIM-019): Manali • Solang Valley • Dharamshala • Mcleodganj with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN MANALI', 1),
            _ih('Day 02: LOCAL MANALI SIGHTSEEING', 2),
            _ih('Day 03: SOLANG VALLEY EXCURSION', 3),
            _ih('Day 04: MANALI TO DHARAMSHALA (TRANSIT)', 4),
            _ih('Day 05: DHARAMSHALA & MCLEODGANJ EXPLORATION', 5),
            _ih('Day 06: KANGRA VALLEY & FORT EXCURSION', 6),
            _ih('Day 07: DEPARTURE FROM DHARAMSHALA', 7),
            _ih('TRAGUIN Signature Experience: Private curated tea-tasting session at an estate in Palampur, featuring', 8),
            _ih('Curated by TRAGUIN Experts: Relaxed, scenic routes designed to minimize travel fatigue for families.', 9),
            _ih('Premium Handpicked Hotels: Accommodations selected strictly based on flawless safety standards and', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN MANALI',
                (
                    'WELCOME TO THE VALLEY OF GODS – ALPINE CHECK-IN Your premium Himachal experience begins with a warm greeting at Chandigarh Airport or Delhi station by your private luxury transport chauffeur. Embark on a highly scenic drive winding alongside the gushing Beas River, transitioning from plains to majestic mountain passes. Upon arriving in Manali, check into your handpicked premium luxury resort and receive a special TRAGUIN welcome amenity kit. Relax in the evening as you watch the sunset cast a golden hue over the pine forests.'
                ),
                [
                    'Sightseeing Included: Scenic Beas River valley drive, mountain pass transitions, resort relaxation.',
                    "Evening Experience: Family orientation and leisure stroll along the resort's private panoramic decks.",
                    'Overnight Stay: Manali (Premium Valley View Luxury Resort)',
                    'Meals Included: Welcome Drink & Luxury Buffet Dinner',
                ],
            ),            _day(
                2,
                'LOCAL MANALI SIGHTSEEING',
                (
                    'CULTURE, HISTORIC WOODEN TEMPLES & OLD TOWN CHARM After a lavish breakfast, set out for an enchanting local Manali sightseeing tour. Visit the iconic 16th-century Hadimba Temple, tucked away inside ancient, towering deodar woods. Explore the mystical Vashisht Village, globally famous for its natural hot springs. Spend a relaxed afternoon wandering through the artistic wooden cafes of Old Manali before enjoying a vibrant shopping excursion along the famous Mall Road in the evening.'
                ),
                [
                    'Sightseeing Included: Hadimba Temple, Vashisht Hot Springs, Tibetan Monastery, Mall Road Shopping.',
                    'Photography Points: Giant cedar canopies of Hadimba forest and panoramic terraces of Old Manali.',
                    'Overnight Stay: Manali (Premium Valley View Luxury Resort)',
                    'Meals Included: Premium Breakfast & Gourmet Dinner',
                ],
            ),            _day(
                3,
                'SOLANG VALLEY EXCURSION',
                (
                    'THRILLING LANDSCAPES & HIGH-ALTITUDE SNOW ADVENTURE Wake up to a pristine mountain sunrise and head towards Solang Valley, famed for its breathtaking landscapes and world-class family adventure sports. Take a romantic, scenic ropeway ride up to Mount Phatru to enjoy panoramic vistas of snow-capped peaks. Your family can choose from a range of immersive experiences, including tandem paragliding, quad biking, and zorbing down the lush slopes.'
                ),
                [
                    'Sightseeing Included: Solang Valley meadows, Snow-point views, high-altitude ridges.',
                    'Optional Activities: Paragliding, open-air amateur skiing lessons, custom family snow-photography.',
                    'Overnight Stay: Manali (Premium Valley View Luxury Resort)',
                    'Meals Included: Premium Breakfast & Special Continental Dinner',
                ],
            ),            _day(
                4,
                'MANALI TO DHARAMSHALA (TRANSIT)',
                (
                    'SCENIC REWIND VIA KULLU VALLEY & PALAMPUR TEA GARDENS Bid farewell to Manali after a hearty breakfast and proceed towards the spiritual hill station of Dharamshala. This stunning transit route winds past the fruit orchards of Kullu and passes through the lush, emerald-green terraced slopes of the Palampur Tea Gardens. Stop for a family stroll among the tea manicured lawns, which serve as a spectacular Instagram location. Arrive in Dharamshala by evening and settle into your premium luxury hotel facing the Dhauladhar range. Artisanal tea-tasting tour in Palampur, curated by TRAGUIN experts.'
                ),
                [
                    'Sightseeing Included: Kullu Valley views, Palampur Tea Estates, Dhauladhar foothills drive.',
                    'Local Experience: s:',
                    'Overnight Stay: Dharamshala / Mcleodganj Premium Luxury Stay',
                    'Meals Included: Premium Breakfast & Regional Himachali Dinner',
                ],
            ),            _day(
                5,
                'DHARAMSHALA & MCLEODGANJ EXPLORATION',
                (
                    'THE LITTLE LHASA – BUDDHIST SPACES & TIBETAN HERITAGE Dedicate your day to exploring the spiritual beauty and rich heritage of Upper Dharamshala (McLeodganj). Visit the revered Dalai Lama Temple Complex (Tsuglagkhang), where you can observe monks chanting in deep harmony. Walk around the historic St. John in the Wilderness Church, built in 1852 in Neo-Gothic style amidst thick deodar forests. Later, visit the serene Bhagsunag Waterfall and the peaceful, pine-rimmed Dal Lake.'
                ),
                [
                    'Sightseeing Included: Dalai Lama Temple, St. John Church, Bhagsunag Waterfall, Dal Lake, Tibetan Market.',
                    'Evening Experience: Private prayer wheel rotation walk and high-tea at an authentic Tibetan café.',
                    'Overnight Stay: Dharamshala / Mcleodganj Premium Luxury Stay',
                    'Meals Included: Premium Breakfast & Oriental Luxury Dinner',
                ],
            ),            _day(
                6,
                'KANGRA VALLEY & FORT EXCURSION',
                (
                    'ANCIENT CIVILIZATIONS & IMPERIAL ARCHITECTURE Embark on a captivating historical journey deep into the Kangra Valley. Tour the ancient Kangra Fort, one of the oldest dated fortresses in India, which has withstood imperial sieges and seismic history. Later, visit the beautiful Brajeshwari Devi Temple, which boasts stunning architecture. Spend your afternoon at leisure exploring the local markets of lower Dharamshala for rich artifacts and local spices.'
                ),
                [
                    'Sightseeing Included: Kangra Fort, Brajeshwari Temple, Kangra Art Museum.',
                    'Optional Activities: Bespoke family pottery workshop at the nearby Andretta Pottery Village.',
                    'Overnight Stay: Dharamshala / Mcleodganj Premium Luxury Stay',
                    'Meals Included: Premium Breakfast & Farewell Dinner',
                ],
            ),            _day(
                7,
                'DEPARTURE FROM DHARAMSHALA',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Enjoy your final breakfast overlooking the misty Dhauladhar peaks. Your private luxury transport vehicle will safely drive you back to Chandigarh Airport or Pathankot Station for your return journey. Head home carrying a heart filled with deep family bonds and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door station or airport drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Solang Valley Resort /',
                'Himachal Pradesh',
                '06 Nights',
                'Deluxe',
                'similar',
                'Hotel Quartz / similar',
                4,
                1,
                description='OPTION 01 – DELUXE: Solang Valley Resort / | similar | Hotel Quartz / similar',
            ),
            _hotel(
                'The Grand Welcome /',
                'Himachal Pradesh',
                '06 Nights',
                'Premium',
                'Manu Allaya',
                'Pride Heritage / Fortune',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Grand Welcome / | Manu Allaya | Pride Heritage / Fortune',
            ),
            _hotel(
                'Span Resort & Spa /',
                'Himachal Pradesh',
                '06 Nights',
                'Luxury',
                'Baragarh Resort',
                'Hyatt Regency',
                4,
                3,
                description='OPTION 03 – LUXURY: Span Resort & Spa / | Baragarh Resort | Hyatt Regency',
            ),
            _hotel(
                'The Oberoi Sukhvilas /',
                'Himachal Pradesh',
                '06 Nights',
                'Ultra Luxury',
                'Private Chalet',
                'The Pavilion by HPCA /',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Oberoi Sukhvilas / | Private Chalet | The Pavilion by HPCA /',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 06 Nights accommodation in handpicked top-rated properties.', 1),
            _inc_included('Luxury Transportation: Private AC Innova Crysta for all point-to-point sightseeing.', 2),
            _inc_included('Curated Meal Plan: Daily premium buffet breakfasts and gourmet multi-cuisine dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest experience manager on call.', 4),
            _inc_included('Welcome Amenities: Customized family travel kit and refreshments upon arrival.', 5),
            _inc_included('Complimentary Experience: Private family tea-tasting experience in Palampur. TRAGUIN Premium Luxury Itinerary — HP-019 5', 6),
            _inc_excluded('Airfare, flight tickets, or long-distance rail travel.', 7),
            _inc_excluded('Adventure sport fees (Paragliding, quad biking, or ski hire).', 8),
            _inc_excluded('Monument entry tickets, local museum keys, and specialized guide charges.', 9),
            _inc_excluded('Personal expenses such as laundry, telephone calls, or tips.', 10),
        ],
    )
    return package, itinerary

def build_hp_020(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HP-020'
    tour_code = 'TRG-HIM-PAN-020'
    title = 'Himachal Panorama • The Ultimate Luxury Alpine Journey'
    duration = '07 Nights / 08 Days'
    slug = 'hp-020-himachal-panorama'
    itin_slug = 'hp-020-himachal-panorama-itinerary'
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
            _ph('Serial code HP-020 | TRAGUIN tour code TRG-HIM-PAN-020', 1),
            _ph('State / Country: Himachal Pradesh / India | Category: Luxury Family', 2),
            _ph('Destinations: Shimla • Kufri • Manali • Solang Valley • Atal Tunnel • Dharamshala • Dalhousie', 3),
            _ph('Ideal for: Premium Family Vacations, Multi- generational Groups & Luxury Seekers', 4),
            _ph('Best season: March to June (Summer Escape) & October to February (Snowfall Experience)', 5),
            _ph('Starting price: On Request (Premium Bespoke Family Pricing)', 6),
            _ph('Vehicle / Meals: Private Luxury Innova Crysta / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private family campfire storytelling circle with local hot beverages', 8),
            _ph('Curated by TRAGUIN Experts: Custom-paced, relaxed driving routes to prevent high-altitude motion', 9),
            _ph('Personalized Assistance: Instant priority messaging channel for live, real-time itinerary modifications and', 10),
            _ph('Premium Handpicked Hotels: Elite properties vetted strictly for luxury bedding, supreme safety', 11),
            _ph('Local Markets & Collectibles: Explore the old markets of Shimla and Manali to pick up handmade wooden toys, traditional Himachali caps, organic local fruit preserves, and beautiful Tibetan singing bowls from McLeod Ganj. Food & Cafes: Indulge in hot local steamed momos, freshly caught river trout, authentic mountain Maggi at pitstops, and artisanal wood-fired bakery delights along the colonial promenades.', 12),
            _ph('Hotel Policies: Standard regional check-in is 14:00 hrs; check-out is 11:00 hrs. Valid national photo IDs', 13)
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
        price_note='On Request (Premium Bespoke Family Pricing)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Himachal Panorama',
        overview="HIMACHAL PANORAMA • THE ULTIMATE LUXURY ALPINE JOURNEY Welcome to an unforgettable mountain odyssey handcrafted exclusively for your family by TRAGUIN. Immerse yourselves in our definitive Himachal Family Tour, thoughtfully conceptualized to unveil the grandest vistas, dramatic valleys, colonial histories, and breathtaking landscapes of India's favorite mountain kingdom. As your elite travel consultants, TRAGUIN transforms this vacation into a high-end luxury holiday. Featuring handpicked hotels, majestic premium stays, and deeply moving cultural storytelling, this curated itinerary guarantees sweet, unforgettable memories for every single family member.\n\nTOUR OVERVIEW\nThis comprehensive, signature itinerary is meticulously engineered for families seeking an opulent, seamless, and deeply immersive exploration across the entire spectrum of Himachal Pradesh. Traveling in an elite private luxury vehicle with an experienced, verified professional mountain chauffeur, your multi-generational group is assured absolute safety, ease, and comfort. With a curated meal plan offering extensive culinary choices at breakfasts and refined dinners, the route stretches from the colonial lanes of Shimla to the high- alpine peaks of Manali, moving gracefully into the spiritual folds of Dharamshala and the pristine pine forests of Dalhousie. Every step incorporates a TRAGUIN curated experience note, providing private local guided walking assistance, exclusive recommendations, and full elite concierge support.\n\nWHY VISIT DESTINATION: THE PREMIUM HIMACHAL EXPERIENCE\nWhen exploring choices for a Luxury Himachal Holiday, luxury travelers demand a perfect balance of heritage, wilderness, and modern sophisticated living. Himachal Pradesh delivers this effortlessly. This vast mountain sanctuary boasts some of the most iconic attractions in Southern Asia. From the legendary ridge walks of Shimla to the pristine snowfields of Solang Valley and the ancient monastic sanctuaries of McLeod Ganj, Himachal sightseeing offers an endlessly rewarding cultural and physical experience. For families and couples mapping out a signature Himachal Honeymoon Package or an expansive Himachal Family Tour, the region reveals highly popular Instagram locations such as the dramatic Atal Tunnel portal, the emerald lawns of Khajjiar (The Mini Switzerland of India), and the picturesque colonial facades of the Viceregal Lodge. Whether you are hunting for traditional woolens on the Mall Road, capturing fine photography points at mountain sunsets, or seeking family-focused adventure sports, booking one of our custom TRAGUIN Himachal Packages ensures you visit during the best time to visit Himachal with ultimate hospitality and premium handpicked hotels.",
        seo_title='HP-020 | Himachal Panorama | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Himachal Pradesh package (HP-020 / TRG-HIM-PAN-020): Shimla • Kufri • Manali • Solang Valley • Atal Tunnel • Dharamshala • Dalhousie with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN SHIMLA', 1),
            _ih('Day 02: KUFRI EXCURSION & SHIMLA HERITAGE WALKS', 2),
            _ih('Day 03: SHIMLA TO MANALI VIA KULLU VALLEY', 3),
            _ih('Day 04: MANALI LOCAL SIGHTSEEING & OLD MANALI', 4),
            _ih('Day 05: SOLANG VALLEY & ATAL TUNNEL EXCURSION', 5),
            _ih('Day 06: MANALI TO DHARAMSHALA', 6),
            _ih('Day 07: DHARAMSHALA TO DALHOUSIE', 7),
            _ih('Day 08: EXCURSION TO KHAJJIAR & DEPARTURE', 8),
            _ih('TRAGUIN Signature Experience: Private family campfire storytelling circle with local hot beverages', 9),
            _ih('Curated by TRAGUIN Experts: Custom-paced, relaxed driving routes to prevent high-altitude motion', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN SHIMLA',
                (
                    'WELCOME TO THE SUMMER CAPITAL – GATEWAY TO THE HILLS Your premium Himachal experience begins with a seamless VIP pick-up from Chandigarh Airport/Station inside a private luxury Innova Crysta. Ascend into the rolling foothills of the Himalayas, catching the dramatic fresh mountain air. Arrive in Shimla, the legendary colonial capital, and check into your premium handpicked hotel. Spend your evening taking a relaxed stroll down the historic Mall Road, enjoying its neo-Gothic architecture and bustling high-end vibe.'
                ),
                [
                    'Sightseeing Included: Scenic Himalayan Expressway drive, Shimla Mall Road, The Ridge, Christ Church.',
                    'Evening Experience: Exclusive high-tea experience overlooking the valleys, organized by TRAGUIN experts.',
                    'Overnight Stay: Shimla (Premium / Luxury Resort)',
                    'Meals Included: Welcome Mocktails & Multi-cuisine Buffet Dinner',
                ],
            ),            _day(
                2,
                'KUFRI EXCURSION & SHIMLA HERITAGE WALKS',
                (
                    'PANORAMIC PEAKS AND COLONIAL SPLENDOR Savor a lavish morning breakfast before driving up to Kufri, a high-altitude paradise offering breathtaking landscapes and majestic Himalayan wildlife parks. Take a horse-ride trail through deodar forests to capture incredible snow-peak photography points. In the afternoon, return to Shimla for a private guided walk through the stately Viceregal Lodge, where Indian history was rewritten inside grand teak rooms.'
                ),
                [
                    'Sightseeing Included: Kufri Peak, Himalayan Nature Park, Viceregal Lodge, Jakhoo Hill Hanuman Temple.',
                    'Optional Activities: Private heritage photography walk with a professional local historian.',
                    'Overnight Stay: Shimla (Premium / Luxury Resort)',
                    'Meals Included: Premium Family Breakfast & Dinner',
                ],
            ),            _day(
                3,
                'SHIMLA TO MANALI VIA KULLU VALLEY',
                (
                    'ALONG THE GUSHING WATERS OF THE BEAS RIVER Embark on a magnificent trans-Himalayan drive towards Manali, the crown jewel of your luxury Himachal holiday. Wind through deep river valleys and traverse the incredible aut tunnel. En route, stop inside the spectacular Kullu Valley. Visit premium local handloom cooperatives to shop for authentic pashminas and woolens. Arrive in Manali by late afternoon, checking into an ultra-luxury riverside property.'
                ),
                [
                    'Sightseeing Included: Kullu Valley scenic route, Pandoh Dam reservoir, Beas River drive banks.',
                    'Evening Experience: Riverside bonfire with artisan appetizers overlooking the illuminated pine forests.',
                    'Overnight Stay: Manali (Luxury Mountain View Suite)',
                    'Meals Included: Breakfast & Traditional Elite Dinner',
                ],
            ),            _day(
                4,
                'MANALI LOCAL SIGHTSEEING & OLD MANALI',
                (
                    'ANCIENT LEGENDS & BOHEMIAN MOUNTAIN CULTURE Dedicate your day to exploring the iconic attractions of central Manali. Pay homage at the ancient Hadimba Temple, marveling at its unique pagoda architecture surrounded by centuries-old deodars. Soak in the therapeutic warm sulfur hot springs of Vashisht Village. Spend your afternoon wandering the vibrant, aesthetic wooden lanes and world-famous cafes of Old Manali, a popular Instagram location for travelers.'
                ),
                [
                    'Sightseeing Included: Hadimba Temple, Vashisht Hot Springs, Van Vihar, Old Manali lanes.',
                    'Optional Activities: Family cafe-hopping and trout fish tasting session in highly rated hillside eateries.',
                    'Overnight Stay: Manali (Luxury Mountain View Suite)',
                    'Meals Included: Premium Breakfast & Gourmet Dinner',
                ],
            ),            _day(
                5,
                'SOLANG VALLEY & ATAL TUNNEL EXCURSION',
                (
                    "HIGH ALPINE SNOWFIELDS & ENGINEERING WONDERS Experience pure high-altitude excitement today. Travel towards Solang Valley, renowned for its breathtaking landscapes and thrilling adventure sports. Take the family on a scenic cable car ropeway to capture spectacular panoramic views. Afterwards, drive through the world's longest highway tunnel over 10,000 feet— the Atal Tunnel—and step out into the dramatic, snowy wonderland of Sissu in Lahaul Valley."
                ),
                [
                    'Sightseeing Included: Solang Valley, Atal Tunnel North Portal, Sissu Waterfall, Snow activity zones.',
                    'Optional Activities: Tandem paragliding, snow quad-biking, private family snow tubing.',
                    'Overnight Stay: Manali (Luxury Mountain View Suite)',
                    'Meals Included: Breakfast & Lavish Continental Buffet Dinner',
                ],
            ),            _day(
                6,
                'MANALI TO DHARAMSHALA',
                (
                    'TRANSITION TO THE LAND OF SPIRITUAL CALM Bid farewell to Manali and drive past rolling tea gardens into the peaceful Kangra Valley towards Dharamshala, the spiritual seat of His Holiness the Dalai Lama. As you climb into McLeod Ganj, feel the cultural atmosphere change with spinning Tibetan prayer wheels and colorful flags. Check into your premium handpicked luxury resort overlooking the Dhauladhar range. experience.'
                ),
                [
                    'Sightseeing Included: Palampur tea gardens, Kangra Valley scenic vistas, McLeod Ganj market.',
                    'Evening Experience: Exclusive evening monk chanting observation and a Tibetan butter-tea sampling',
                    'Overnight Stay: Dharamshala / McLeod Ganj (Premium Resort)',
                    'Meals Included: Breakfast & Traditional Tibetan-Indian Dinner',
                ],
            ),            _day(
                7,
                'DHARAMSHALA TO DALHOUSIE',
                (
                    'THE COLONIAL RETREAT EMBEDDED IN DEODAR FORESTS Morning exploration of the serene Tsuglagkhang Complex (Dalai Lama Temple) and the picturesque Bhagsu Waterfall. Afterwards, drive along scenic mountain ridges towards the quiet, majestic colonial outpost of Dalhousie. Famous for its old-world churches and undisturbed scenic beauty, Dalhousie offers the perfect peaceful conclusion for your family holiday.'
                ),
                [
                    "Sightseeing Included: Dalai Lama Temple, Bhagsu Nag, St. John's Church in the Wilderness, Subhash Baoli.",
                    'Evening Experience: Sunset promenade walk through the historic, vehicle-free lanes of Thandi Sarak.',
                    'Overnight Stay: Dalhousie (Premium Heritage Property)',
                    'Meals Included: Breakfast & Premium Farewell Dinner',
                ],
            ),            _day(
                8,
                'EXCURSION TO KHAJJIAR & DEPARTURE',
                (
                    'MINI SWITZERLAND MOMENTS & CHERISHED GOODBYES Following an early breakfast, enjoy a short drive to Khajjiar, a stunning meadow surrounded by dense cedar forests with a small lake at its center, famously called the "Mini Switzerland of India." After capturing breathtaking family group photographs, descend smoothly towards Pathankot Station or Chandigarh Airport for your return flight home. Your elite journey concludes, leaving you with unforgettable memories designed by TRAGUIN.'
                ),
                [
                    'Sightseeing & Drop: Khajjiar Floating Island Meadow, Private airport/station drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'East Bourne Resort /',
                'Himachal Pradesh',
                '07 Nights',
                'Deluxe',
                'similar',
                'Solang Valley Resort /',
                4,
                1,
                description='OPTION 01 – DELUXE: East Bourne Resort / | similar | Solang Valley Resort /',
            ),
            _hotel(
                'Radisson Hotel',
                'Himachal Pradesh',
                '07 Nights',
                'Premium',
                'Shimla',
                'ManuAllaya Resort /',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Hotel | Shimla | ManuAllaya Resort /',
            ),
            _hotel(
                'The Cecil - Oberoi',
                'Himachal Pradesh',
                '07 Nights',
                'Luxury',
                'Heritage',
                'Span Resort & Spa /',
                4,
                3,
                description='OPTION 03 – LUXURY: The Cecil - Oberoi | Heritage | Span Resort & Spa /',
            ),
            _hotel(
                'Wildflower Hall',
                'Himachal Pradesh',
                '07 Nights',
                'Ultra Luxury',
                '(Oberoi)',
                'The Oberoi Sukhvilas /',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Wildflower Hall | (Oberoi) | The Oberoi Sukhvilas /',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury accommodations across 07 nights with guaranteed views.', 1),
            _inc_included('Luxury Transportation: Private dedicated Innova Crysta for all transfers & sightseeing.', 2),
            _inc_included('Curated Meals: Daily expansive premium breakfasts & gourmet themed dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 priority concierge line and dedicated ground support handlers.', 4),
            _inc_included('Welcome Amenities: Personalized family travel kit, healthy snacks, and arrival drinks.', 5),
            _inc_included('Complimentary Experience: Reserved private family high-tea lounge access in Shimla. TRAGUIN Premium Luxury Family Itinerary — HP-020 6', 6),
            _inc_excluded('Domestic airfare, flight bookings, or long-distance train tickets.', 7),
            _inc_excluded('Adventure activities (Paragliding, horse riding, or rafting bills).', 8),
            _inc_excluded('Monument entrance tickets, guide tokens, camera permission charges.', 9),
            _inc_excluded('Personal items such as laundry, alcohol, tips, or phone calls.', 10),
        ],
    )
    return package, itinerary

HIMACHAL_DOMESTIC_BUILDERS = [
    build_hp_001,
    build_hp_002,
    build_hp_003,
    build_hp_004,
    build_hp_005,
    build_hp_006,
    build_hp_007,
    build_hp_008,
    build_hp_009,
    build_hp_010,
    build_hp_011,
    build_hp_012,
    build_hp_013,
    build_hp_014,
    build_hp_015,
    build_hp_016,
    build_hp_017,
    build_hp_018,
    build_hp_019,
    build_hp_020,
]
