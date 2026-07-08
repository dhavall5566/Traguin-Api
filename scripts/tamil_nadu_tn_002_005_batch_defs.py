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


def build_tn_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TN-002'
    tour_code = 'TRG-TN-002'
    title = 'TEMPLE TRAIL TAMIL NADU • ARCHITECTURAL GRANDEUR & DIVINE DEVOTION'
    duration = '05 Nights / 06 Days'
    slug = 'tn-002-temple-trail-tamil-nadu-architectural-grandeur-divine-devotion'
    itin_slug = 'tn-002-temple-trail-tamil-nadu-architectural-grandeur-divine-devotion-itinerary'
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
            _ph('Serial code TN-002 | TRAGUIN tour code TRG-TN-002', 1),
            _ph('State / Country: Tamil Nadu / India | Category: Premium Pilgrimage / Divine Spiritual Escape', 2),
            _ph('Destinations: Madurai • Rameshwaram • Thanjavur • Kumbakonam • Trichy', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Luxury AC Innova Crysta / MAPAI (Breakfast & Gourmet Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private orientation session with a renowned cultural historian prior to', 8),
            _ph('Curated by TRAGUIN Experts: Optimized driving schedules that balance divine darshans with premium', 9),
            _ph('Personalized Assistance: Dedicated destination handlers to seamlessly manage shoes and secure fast-', 10),
            _ph('Exclusive Recommendations: Handpicked local dining stops serving genuine, hygienic traditional filter', 11)
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
        tagline='TEMPLE TRAIL TAMIL NADU',
        overview='PACKAGE TEMPLE TRAIL TAMIL NADU • ARCHITECTURAL GRANDEUR & DIVINE DEVOTION Welcome to an extraordinary spiritual quest elegantly crafted by TRAGUIN. Embark on the definitive Temple Trail Tamil Nadu, an immersive experience tailored for families and discerning travellers seeking a profound connection with ancient Vedic heritage. As your elite luxury travel consultants, TRAGUIN transforms this sacred pilgrimage into a sophisticated, premium stays holiday. Marvel at the breathtaking landscapes of the southern plains and the towering, jewel-encrusted gopurams of historic spiritual capitals. Every step of this journey yields unforgettable memories of architectural wonder and deep, emotional storytelling.\n\nTOUR OVERVIEW\nThis custom luxury holiday proposal covers the core cultural heartland of Southern India. Travelling in a dedicated private premium AC vehicle under the careful guidance of a courteous local expert chauffeur, your family will enjoy unrivaled comfort, safety, and personalized assistance. Featuring a meticulous meal plan packed with grand traditional breakfasts and curated specialized dinners, this itinerary represents the absolute peak of a premium Tamil Nadu experience. Every phase includes a signature TRAGUIN curated experience note, ensuring exclusive VIP temple entries, direct priest interactions, and round-the-clock logistical excellence.\n\nWHY CHOOSE THE BEST TAMIL NADU TOUR PACKAGE?\nWhen arranging a Luxury Tamil Nadu Holiday, travelers expect a profound journey through time, heritage, and artistic perfection. Our meticulously planned Tamil Nadu Family Tour features iconic attractions including UNESCO World Heritage sites, majestic stone-carved complexes, and divine island shrines. From the legendary Meenakshi Amman Temple to the engineering majesty of Thanjavur’s Brihadeeswarar Temple, Tamil Nadu sightseeing offers unmatched cultural scale. For families celebrating milestones or couples booking a meaningful Tamil Nadu Honeymoon Package, this trail maps out highly popular Instagram locations like the architectural corridors of Rameshwaram, scenic coastal bridges, and the traditional artistic quarters of Kumbakonam. Indulge in exquisite silk shopping, relish aromatic local cuisines, and absorb profound cultural highlights. Our boutique TRAGUIN Tamil Nadu Packages blend high-end handpicked hotels with exclusive experiences, making this the best time to visit Tamil Nadu with flawless peace of mind. TRAGUIN Premium Luxury Itinerary — TN-002 2',
        seo_title='TN-002 | TEMPLE TRAIL TAMIL NADU | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Tamil Nadu package (TN-002 / TRG-TN-002): Madurai • Rameshwaram • Thanjavur • Kumbakonam • Trichy with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN MADURAI', 1),
            _ih('Day 02: MADURAI TO RAMESHWARAM', 2),
            _ih('Day 03: DHANUSHKODI EXCURSION & TRAVEL TO THANJAVUR', 3),
            _ih('Day 04: THANJAVUR TO KUMBAKONAM', 4),
            _ih('Day 05: KUMBAKONAM TO TRICHY', 5),
            _ih('Day 06: TRICHY TO DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private orientation session with a renowned cultural historian prior to', 7),
            _ih('Curated by TRAGUIN Experts: Optimized driving schedules that balance divine darshans with premium', 8),
            _ih('Personalized Assistance: Dedicated destination handlers to seamlessly manage shoes and secure fast-', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN MADURAI',
                (
                    'WELCOME TO THE ATHENS OF THE EAST – DIVINE NIGHT CEREMONY Your premium Tamil Nadu experience takes flight as you arrive at Madurai Airport, where a private luxury transport vehicle waits to escort you. Check into your choice of premium stays and take time to refresh. In the afternoon, explore the magnificent Thirumalai Nayakkar Palace, showcasing an opulent blend of Dravidian and Islamic design. As twilight descends, prepare for an emotionally charged evening at the world-famous Meenakshi Amman Temple, watching the iconic night procession ceremony where Lord Shiva is carried to Goddess Meenakshi’s shrine amidst chanting and bells. TRAGUIN experts.'
                ),
                [
                    'Sightseeing Included: Thirumalai Nayakkar Palace, Meenakshi Amman Temple Complex, Local Bazaar Walks.',
                    'Evening Experience: VIP entry for the divine Palliyarai (Night Procession) ceremony, exclusively curated by',
                    'Overnight Stay: Madurai (Premium / Luxury Heritage Hotel)',
                    'Meals Included: Welcome Drink & Luxury Welcome Dinner',
                ],
            ),
            _day(
                2,
                'MADURAI TO RAMESHWARAM',
                (
                    'CROSSING THE PAMBAN BRIDGE – SACRED SEAS & PILGRIM PURIFICATION Relish a lavish breakfast before setting off on a highly scenic drive toward the sacred island city of Rameshwaram. Cross the iconic Pamban Bridge, capturing breathtaking landscapes of the turquoise ocean surrounding the railway corridor—a popular Instagram location. Upon arrival, check into your handpicked premium stay. In the afternoon, visit the Ramanathaswamy Temple, renowned for the longest temple corridor in the world, framed by intricately sculpted stone pillars. Participate in the traditional ritual of bathing across the 22 holy teerthams (wells) inside the temple precinct.'
                ),
                [
                    'Sightseeing Included: Pamban Bridge Viewpoint, Ramanathaswamy Temple Corridors, Agnitheertham Coastline.',
                    'Optional Activities: Private guided holy teertham purification route with a dedicated scholar priest.',
                    'Overnight Stay: Rameshwaram (Premium / Handpicked Beachside Luxury Resort)',
                    'Meals Included: Premium Breakfast & Coastal Buffet Dinner',
                ],
            ),
            _day(
                3,
                'DHANUSHKODI EXCURSION & TRAVEL TO THANJAVUR',
                (
                    "THE GHOST TOWN AT THE BORDER & THE GRANARY OF SOUTH INDIA Experience a breathtaking sunrise excursion to Dhanushkodi, the atmospheric ghost town sitting at the edge of India’s land border. Witness the emotional storytelling behind this lost town and gaze out at Ram Setu's historic waters. Return to the hotel for breakfast, then drive through lush agricultural fields to Thanjavur (Tanjore). Arrive in the evening and check into a premium eco-heritage resort. Unwind with an intimate traditional classical Carnatic music performance arranged in the courtyard."
                ),
                [
                    'Sightseeing Included: Dhanushkodi Ruins, Kodandaramaswamy Temple, Thanjavur Royal Palace & Museum.',
                    'Evening Experience: Private heritage art briefing and traditional musical evening at the resort.',
                    'Overnight Stay: Thanjavur (Premium Luxury Eco-Resort)',
                    'Meals Included: Premium Breakfast & Regional Tanjore Delicacy Dinner',
                ],
            ),
            _day(
                4,
                'THANJAVUR TO KUMBAKONAM',
                (
                    'CHOLA ARCHITECTURAL MASTERPIECES & SACRED CHRONICLES Following a rich morning buffet, visit the legendary UNESCO World Heritage Site—the Brihadeeswarar Temple (Big Temple). This architectural marvel features a massive monolithic Vimana capstone weighing 80 tons, placed flawlessly by Chola kings. After discovering its historic mysteries, drive to the holy town of Kumbakonam. Along the way, explore the Airavatesvara Temple at Darasuram, a treasure trove of miniature stone carvings depicting music, dance, and epics. Check into your luxury resort nestled within manicured coconut groves.'
                ),
                [
                    'Sightseeing Included: Brihadeeswarar Temple, Darasuram Airavatesvara Temple, Adi Kumbeswarar Complex.',
                    'Evening Experience: Private live demonstration of ancient lost-wax bronze casting by heritage artisans.',
                    'Overnight Stay: Kumbakonam (Premium Handpicked Heritage Villa Stay)',
                    'Meals Included: Premium Breakfast & Authentic South Indian Thali Dinner',
                ],
            ),
            _day(
                5,
                'KUMBAKONAM TO TRICHY',
                (
                    'THE FORTRESS ON THE HILL & THE LARGEST FUNCTIONING TEMPLE Enjoy an early breakfast before driving to Trichy (Tiruchirappalli). Your first destination is Srirangam, home to the Sri Ranganathaswamy Temple—the largest functioning temple complex in the world. Walk through its colossal enclosures and ascend to the terrace to view the golden domes. In the afternoon, climb the historic'
                ),
                [
                    'Sightseeing Included: Srirangam Temple Complex, Rockfort Ucchi Pillayar Temple, Jambukeswarar Water',
                    'Optional Activities: Shopping for authentic Trichy brassware and traditional structural keepsakes.',
                    'Overnight Stay: Trichy (Premium Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Farewell Executive Dinner',
                ],
            ),
            _day(
                6,
                'TRICHY TO DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES OF THE SACRED SOUTH Indulge in a final gourmet breakfast at your premium hotel. Your private luxury transport vehicle will handle your transfer to Trichy International Airport or Railway Station for your return flight home. Depart carrying a soul filled with profound serenity, divine blessings, and unforgettable memories carefully orchestrated by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury airport or railway terminal drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Heritage Madurai | Daiwik Hotel | Hotel Sangam | Paradise Resort SRM Hotel',
                'Tamil Nadu',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Heritage Madurai | Daiwik Hotel | Hotel Sangam | Paradise Resort SRM Hotel',
            ),
            _hotel(
                'Courtyard by Marriott | JKR Resort | Svatma Tanjore | Mantra Kulam Courtyard by Marriott',
                'Tamil Nadu',
                '5N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Courtyard by Marriott | JKR Resort | Svatma Tanjore | Mantra Kulam Courtyard by Marriott',
            ),
            _hotel(
                'The Gateway Hotel Pasumalai (Taj) Svatma',
                'Tamil Nadu',
                '5N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Gateway Hotel Pasumalai (Taj) Svatma',
            ),
            _hotel(
                'Taj Pasumalai (Presidential',
                'Tamil Nadu',
                '5N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Taj Pasumalai (Presidential',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Handpicked luxury hotel rooms as per chosen tier.', 1),
            _inc_included('Luxury Transportation: Chauffeur-driven AC Innova Crysta for all route mapping.', 2),
            _inc_included('Curated Meal Plan: Daily elaborate breakfasts and gourmet dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest relations manager and line monitoring.', 4),
            _inc_included('Welcome Amenities: Personalized pilgrimage kits, sacred prasad, and fresh wipes.', 5),
            _inc_included('Complimentary Experiences: Reserved VIP entry cards for select temple ceremonies.', 6),
            _inc_excluded('Airfare, flight taxes, or long-haul interstate rail ticketing.', 7),
            _inc_excluded('Personal expenses such as laundry, telephone calls, tips, and porterage.', 8),
            _inc_excluded('Special ritual dakshina fees, individual pooja costs, or camera permits.', 9),
            _inc_excluded('Optional sightseeing loops, museum entries, or insurance coverage.', 10),
        ],
    )
    return package, itinerary

def build_tn_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TN-003'
    tour_code = 'TRG-TN-003'
    title = 'NILGIRI ROMANCE • A LUXURY HILL STATION RETREAT'
    duration = '04 Nights / 05 Days'
    slug = 'tn-003-nilgiri-romance-a-luxury-hill-station-retreat'
    itin_slug = 'tn-003-nilgiri-romance-a-luxury-hill-station-retreat-itinerary'
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
            _ph('Serial code TN-003 | TRAGUIN tour code TRG-TN-003', 1),
            _ph('State / Country: Tamil Nadu / India | Category: Luxury Honeymoon Escape', 2),
            _ph('Destinations: Ooty • Coonoor •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Sedan / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private estate walking tour inside an active 100-year-old tea plantation.', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked romantic routes balancing scenic mountain drives with', 9),
            _ph('Premium Handpicked Hotels: Accommodations selected strictly based on premium safety standards,', 10),
            _ph('Luxury Transportation: Expert hill-station drivers ensuring elite comfort and safety across winding', 11)
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
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='NILGIRI ROMANCE',
        overview='NILGIRI ROMANCE • A LUXURY HILL STATION RETREAT Welcome to an unforgettable romantic sanctuary meticulously curated by TRAGUIN. Bask in the ultimate Tamil Nadu Honeymoon Package, artfully designed to guide you through the breathtaking landscapes, sprawling emerald tea estates, and mist-kissed ridges of the Blue Mountains. As your elite travel consultants, TRAGUIN transforms your romantic getaway into a flawless luxury holiday filled with premium TRAGUIN Premium Luxury Itinerary — TN-003 1 stays, handpicked hotels, and intimate local experiences. Let the scenic beauty of the pristine Nilgiri lakes and aromatic pine woodlands frame your journey, weaving a tapestry of sweet, unforgettable memories for you and your beloved.\n\nTOUR OVERVIEW\nThis custom-tailored romantic voyage offers a perfect blend of high-altitude tranquility, colonial charm, and modern boutique indulgence. Travelling across the stunning hill passes of Tamil Nadu in a private luxury chauffeur-driven sedan, you will experience complete comfort and privacy. With an exquisite meal plan offering gourmet daily breakfasts and curated evening dinners, this route represents the definitive premium Tamil Nadu experience. Every moment features the signature TRAGUIN curated experience note, providing exclusive privileges, private sightseeing itineraries, and round-the-clock specialized concierge support.\n\nWHY CHOOSE THE BEST TAMIL NADU TOUR PACKAGE?\nWhen considering a Luxury Tamil Nadu Holiday, discerning couples seek a harmonious balance of deep natural beauty and private comfort. The Nilgiri hills stand as a legendary haven for romance, making an Ooty Honeymoon Package the ultimate dream choice for couples. From exploring iconic attractions like the Government Botanical Garden and Rose Garden to seeking misty panoramic vistas at Doddabetta Peak, Tamil Nadu sightseeing reveals endless charm. For couples booking a bespoke Tamil Nadu Honeymoon Package or a relaxing Tamil Nadu Family Tour, the region offers incredibly popular Instagram locations such as the Pykara Waterfalls, the historic Nilgiri Mountain Railway, and the tea slopes of Coonoor. Whether you are searching for authentic aromatic oils, organic tea shopping at the local markets, or enjoying cozy lakeside cafes, our custom TRAGUIN Tamil Nadu Packages ensure immersive experiences and premium handpicked hotels during the best time to visit Tamil Nadu.',
        seo_title='TN-003 | NILGIRI ROMANCE | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Tamil Nadu package (TN-003 / TRG-TN-003): Ooty • Coonoor • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN OOTY (VIA COIMBATORE)', 1),
            _ih('Day 02: OOTY ROMANTIC SIGHTSEEING', 2),
            _ih('Day 03: COONOOR EXCURSION & TOY TRAIN EXPERIENCE', 3),
            _ih('Day 04: PYKARA LAKE & PINE FORESTS', 4),
            _ih('Day 05: OOTY TO COIMBATORE / DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private estate walking tour inside an active 100-year-old tea plantation.', 6),
            _ih('Curated by TRAGUIN Experts: Handpicked romantic routes balancing scenic mountain drives with', 7),
            _ih('Premium Handpicked Hotels: Accommodations selected strictly based on premium safety standards,', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN OOTY (VIA COIMBATORE)',
                (
                    'WELCOME TO THE QUEEN OF HILL STATIONS – ROMANTIC RIVERSIDE CHECK-IN Your premium Tamil Nadu experience begins the moment you touch down at Coimbatore Airport or Railway Station. Your private luxury transport vehicle with a professional uniform-clad chauffeur welcomes you. Embark on a spectacular scenic drive twisting through lush mountain ghats, hair-pin curves, and expansive forest preserves. Arrive in the romantic hill station of Ooty and check into your premium luxury resort. Enjoy a special welcome amenity kit. Relax as the evening breeze sweeps over your private balcony.'
                ),
                [
                    'Sightseeing Included: Mettupalayam mountain view route, Ooty lake promenade stroll.',
                    'Evening Experience: Honeymoon Special: Complimentary welcome cake and a beautifully stylized floral room',
                    'Overnight Stay: Ooty (Premium Colonial Heritage Resort or Luxury Suite)',
                    'Meals Included: Welcome Drink & Luxury Sit-down Dinner',
                ],
            ),
            _day(
                2,
                'OOTY ROMANTIC SIGHTSEEING',
                (
                    'BOTANICAL SPLENDOUR & HISTORIC MOUNTAIN VIEWS Awake to the soothing sounds of birds over the valley. After a lavish buffet breakfast, depart for a curated Ooty sightseeing tour. Walk hand-in-hand through the meticulously manicured lawns of the Government Botanical Garden, boasting rare trees and fossils. Ascend to Doddabetta Peak, the highest point in South India, offering breathtaking landscapes of the surrounding mist-covered valleys. In the afternoon, enjoy a private boat cruise across Ooty Lake, capturing the perfect sunset together.'
                ),
                [
                    'Sightseeing Included: Botanical Garden, Rose Garden, Doddabetta Peak, Ooty Lake, Thread Garden.',
                    'Evening Experience: Bespoke candle-lit dinner with a premium menu designed by TRAGUIN experts.',
                    'Overnight Stay: Ooty (Premium Luxury Resort)',
                    'Meals Included: Premium Breakfast & Romantic Candle-lit Dinner',
                ],
            ),
            _day(
                3,
                'COONOOR EXCURSION & TOY TRAIN EXPERIENCE',
                (
                    'EMERALD TEA GARDENS & VINTAGE CHARM Today features a truly iconic experience. Board the historic Nilgiri Mountain Railway Toy Train (subject to availability/booking), a UNESCO World Heritage site, for a vintage rail journey from Ooty to Coonoor. Marvel at the dramatic valleys, old-world bridges, and tunnels along the path. Your luxury vehicle joins you in Coonoor to explore the famous Sim’s Park and the stunning Lamb’s Rock. Stand together at Dolphin’s Nose viewpoint, soaking in the endless views of Catherine Falls cascading in the distance.'
                ),
                [
                    'Sightseeing Included: Toy Train Ride, Sim’s Park, Lamb’s Rock, Dolphin’s Nose, Highfield Tea Factory.',
                    'Optional Activities: Private tea-tasting experience to sample exquisite, rare Nilgiri orthodox varieties.',
                    'Overnight Stay: Ooty / Coonoor Luxury Tea Estate Bungalow',
                    'Meals Included: Premium Breakfast & Fine Dining Dinner',
                ],
            ),
            _day(
                4,
                'PYKARA LAKE & PINE FORESTS',
                (
                    'SERENE LAKES, WATERFALLS & INSTAGRAM SPOTLIGHTS Journey towards the tranquil, untouched landscapes of Pykara. Drive through the dense Shooting Point pine forests, a highly sought-after Instagram location and photography spot. Arrive at the spectacular Pykara Waterfalls, surrounded by pristine native woodlands. Later, enjoy a quiet, exclusive experience with a private speed-boat ride across the deep-blue waters of Pykara Lake, reflecting the gorgeous cloudscapes above.'
                ),
                [
                    'Sightseeing Included: Pykara Falls, Pykara Lake, Pine Forest Trails, Kamaraj Sagar Dam.',
                    'Evening Experience: Sunset bonfire experience with premium snacks at your luxury mountain property.',
                    'Overnight Stay: Ooty (Premium Luxury Resort)',
                    'Meals Included: Premium Breakfast & Special Farwell Dinner',
                ],
            ),
            _day(
                5,
                'OOTY TO COIMBATORE / DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Enjoy your final lavish breakfast overlooking the misty tea fields of the Blue Mountains. Pack your bags as your private luxury transport vehicle readies for your return journey. Descend smoothly along the forested mountain highways back to Coimbatore Airport or Railway Station for your onward journey home. Return with your heart filled with romance and unforgettable memories designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door station or airport drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Sinclairs Retreat Ooty',
                'Tamil Nadu',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Sinclairs Retreat Ooty',
            ),
            _hotel(
                'Sterling Ooty Elk Hill | Fern Hill | Premium Balcony',
                'Tamil Nadu',
                '4N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Sterling Ooty Elk Hill | Fern Hill | Premium Balcony',
            ),
            _hotel(
                'Savoy - IHCL SeleQtions | Gateway Coonoor',
                'Tamil Nadu',
                '4N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Savoy - IHCL SeleQtions | Gateway Coonoor',
            ),
            _hotel(
                'The Savoy | Private Luxury Estate',
                'Tamil Nadu',
                '4N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Savoy | Private Luxury Estate',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 04 Nights in handpicked romantic luxury properties.', 1),
            _inc_included('Luxury Transportation: Private dedicated sedan for all transfers & sightseeing.', 2),
            _inc_included('Curated Meal Plan: Daily premium buffet breakfast and gourmet dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 personalized concierge and guest manager support.', 4),
            _inc_included('Honeymoon Kit: Intimate candle-lit dining, floral bedding art, and custom cake.', 5),
            _inc_included('Exclusive Experiences: Private sunset boating tickets at Ooty Lake.', 6),
            _inc_excluded('Airfare, flight tickets, or long-distance interstate rail fares.', 7),
            _inc_excluded('Toy Train tickets (subject to direct railway allocation and availability).', 8),
            _inc_excluded('Monument entry fees, camera permits, and local guide expenses.', 9),
            _inc_excluded('Personal expenses such as laundry, phone calls, or tips.', 10),
        ],
    )
    return package, itinerary

def build_tn_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TN-004'
    tour_code = 'TRG-TN-004'
    title = 'CHENNAI PONDICHERRY ESCAPE • HERITAGE, COASTLINE & CULTURE'
    duration = '04 Nights / 05 Days'
    slug = 'tn-004-chennai-pondicherry-escape-heritage-coastline-culture'
    itin_slug = 'tn-004-chennai-pondicherry-escape-heritage-coastline-culture-itinerary'
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
            _ph('Serial code TN-004 | TRAGUIN tour code TRG-TN-004', 1),
            _ph('State / Country: Tamil Nadu / India | Category: Premium Family Tour', 2),
            _ph('Destinations: Chennai •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury AC Innova Crysta / MAPAI Plan', 7),
            _ph('TRAGUIN Signature Experience: Curated artisan filter coffee tasting session in an authentic heritage', 8),
            _ph('Curated by TRAGUIN Experts: Custom-timed departures along the East Coast Road to capture stunning', 9),
            _ph('Premium Handpicked Hotels: Elite properties selected for their exceptional family safety, architectural', 10),
            _ph('Luxury Transportation: Premium modern vehicles with expert, verified tourist chauffeurs fluent in English', 11)
        ],
        moods=['Family', 'Luxury', 'Culture'],
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
        tagline='CHENNAI PONDICHERRY ESCAPE',
        overview="CHENNAI PONDICHERRY ESCAPE • HERITAGE, COASTLINE & CULTURE TRAGUIN Premium Luxury Itinerary — TN-004 1 Welcome to an unforgettable coastal and cultural journey curated exclusively by TRAGUIN. Embark on the finest Tamil Nadu Family Tour designed to reveal the golden shorelines, monolithic rock marvels, and sophisticated French quarters of this historic southern region. As your premier travel consultants, TRAGUIN transforms your vacation into a seamless luxury holiday filled with handpicked hotels, immersive experiences, and deeply moving stories. From the cultural heritage and temple architecture of Chennai to the timeless stone poetry of Mahabalipuram and the colonial European charm of Pondicherry, every detail is engineered to create unforgettable memories.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers an exquisite balance between bustling metropolitan culture, ancient UNESCO World Heritage sites, and serene colonial seaside promenades. Travelling in a dedicated premium AC vehicle with professional chauffeur-driven assistance, your family will enjoy absolute comfort and privacy. With a carefully curated meal plan featuring lavish breakfasts and specialized dinners, this route represents the definitive premium Tamil Nadu experience. Every step of your journey includes the signature touch of TRAGUIN curated experiences, ensuring VIP entry privileges, local storytelling insight, and around- the-clock bespoke support.\n\nWHY CHOOSE THE BEST TAMIL NADU TOUR PACKAGE?\nWhen considering a Luxury Tamil Nadu Holiday, discerning travellers seek more than just standard sightseeing; they seek a deeply immersive dive into living traditions, architectural marvels, and modern relaxation. Tamil Nadu boasts some of the most iconic attractions in Southern India. From Chennai's historic Kapaleeshwarar Temple and the endless stretch of Marina Beach to the monolithic Shore Temple of Mahabalipuram—a top tourist place in Tamil Nadu for architecture and photography—the region offers unparalleled depth. For families and couples booking a bespoke Tamil Nadu Honeymoon Package or Tamil Nadu Family Tour, the state reveals highly popular Instagram locations like the vibrant French Quarter streets of Pondicherry, the giant boulder known as Krishna's Butterball, and the spiritual oasis of Matrimandir in Auroville. Whether you are looking for silk sari and boutique handicraft shopping, indulging in traditional filter coffee and French culinary delights, or seeking historical enlightenment along ancient trade routes, our TRAGUIN Tamil Nadu Packages guarantee premium comfort, handpicked luxury stays, and curated exclusive experiences that mark the best time to visit Tamil Nadu. TRAGUIN Premium Luxury Itinerary — TN-004 2",
        seo_title='TN-004 | CHENNAI PONDICHERRY ESCAPE | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Tamil Nadu package (TN-004 / TRG-TN-004): Chennai • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN CHENNAI', 1),
            _ih('Day 02: CHENNAI TO MAHABALIPURAM VIA ECR', 2),
            _ih('Day 03: MAHABALIPURAM TO PONDICHERRY', 3),
            _ih('Day 04: AUROVILLE EXCURSION & LOCAL CAFE EXPERIENCE', 4),
            _ih('Day 05: PONDICHERRY TO CHENNAI / DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Curated artisan filter coffee tasting session in an authentic heritage', 6),
            _ih('Curated by TRAGUIN Experts: Custom-timed departures along the East Coast Road to capture stunning', 7),
            _ih('Premium Handpicked Hotels: Elite properties selected for their exceptional family safety, architectural', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN CHENNAI',
                (
                    'WELCOME TO THE GATEWAY OF SOUTH INDIA – HERITAGE & METROPOLITAN LUXURY Your premium Tamil Nadu experience begins as you arrive at Chennai International Airport/Railway Station, where a dedicated private luxury transport vehicle waits to escort you. Transfer smoothly to your handpicked premium luxury hotel and check in. After a refreshing afternoon, step out to explore the historic side of Chennai. Visit the grand Kapaleeshwarar Temple in Mylapore, showcasing brilliant Dravidian architecture. Later, take a peaceful evening walk along Marina Beach, the second longest urban beach in the world, capturing beautiful sunset photography points.'
                ),
                [
                    'Sightseeing Included: Kapaleeshwarar Temple, Santhome Cathedral Basilica, Marina Beach Promenade.',
                    'Evening Experience: Gourmet traditional dinner accompanied by authentic South Indian filter coffee tasting.',
                    'Overnight Stay: Chennai (Premium / Luxury Beachfront Hotel)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'CHENNAI TO MAHABALIPURAM VIA ECR',
                (
                    "SCENIC COASTAL DRIVES & ANCIENT ROCK-CUT ARCHITECTURE Indulge in a lavish breakfast before embarking on a beautiful drive along the East Coast Road (ECR), offering scenic beauty and glimpses of the sparkling Bay of Bengal. Arrive at Mahabalipuram (Mamallapuram), an ancient historic port town famous for its 7th-century UNESCO World Heritage rock carvings. Explore the iconic Shore Temple standing proudly on the water's edge, admire the massive monolithic Five Rathas, and pose for a fun family picture at Krishna’s Butterball—a highly popular Instagram location. Check into your luxury beach resort for an evening of coastal bliss."
                ),
                [
                    'Sightseeing Included: Shore Temple, Five Rathas, Arjuna’s Penance rock relief, Krishna’s Butterball.',
                    'Optional Activities: Private guided heritage walk with an expert archaeologist arranged by TRAGUIN.',
                    'Overnight Stay: Mahabalipuram (Premium Luxury Beach Resort)',
                    'Meals Included: Premium Breakfast & Coastal Seafood/Multi-cuisine Dinner',
                ],
            ),
            _day(
                3,
                'MAHABALIPURAM TO PONDICHERRY',
                (
                    'TRANSITION TO THE FRENCH RIVIERA OF THE EAST After a morning breakfast overlooking the ocean waves, continue your private luxury journey southward to Pondicherry (Puducherry). Upon arrival, the atmosphere shifts instantly into a charming European dreamscape. Check into your handpicked heritage boutique hotel nestled inside the famous French Quarter'
                ),
                [
                    'Sightseeing Included: White Town Heritage Walk, Promenade Beach, French War Memorial, Sri Aurobindo',
                    'Evening Experience: Private candlelight dinner at a curated French-Creole courtyard restaurant.',
                    'Overnight Stay: Pondicherry (Premium Heritage Luxury Boutique Stay)',
                    'Meals Included: Breakfast & Exquisite French-Indo Dinner',
                ],
            ),
            _day(
                4,
                'AUROVILLE EXCURSION & LOCAL CAFE EXPERIENCE',
                (
                    'SPIRITUAL ODYSSEY & EXPERIMENTAL TOWNSHIP EXPLORATION Dedicate your morning to an immersive experience inside Auroville, an international experimental township dedicated to human unity. Drive through the serene forested paths to view the magnificent Matrimandir, a giant golden metallic sphere that serves as the spiritual heart of the community. Explore the Auroville Visitors Centre, browse high-end sustainable handicraft boutiques, and relax at an eco-café. Return to Pondicherry for a free afternoon of boutique shopping or an optional boat ride to Paradise Beach.'
                ),
                [
                    'Sightseeing Included: Auroville Township, Matrimandir Outer Viewpoint, Sacred Heart Basilica in Pondicherry.',
                    'Optional Activities: Speedboat excursion to Paradise Beach Sandbar or a private pottery-making workshop.',
                    'Overnight Stay: Pondicherry (Premium Heritage Luxury Boutique Stay)',
                    'Meals Included: Breakfast & Farewell Premium Dinner',
                ],
            ),
            _day(
                5,
                'PONDICHERRY TO CHENNAI / DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Enjoy your last premium breakfast at your hotel before embarking on a smooth return drive back to Chennai. If time permits, stop at Kanchipuram or local craft villages en route for some textile shopping. Your private luxury transport will drop you off safely at Chennai International Airport or Central Railway Station for your journey home. Return with a heart filled with beautiful family bonds and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door highway drop-off at airport/station.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Residential',
                'Tamil Nadu',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: The Residential',
            ),
            _hotel(
                'Radisson Blu City Centre | Welcomhotel by ITC Bay Island | The Promenade | Palais de Mahe',
                'Tamil Nadu',
                '4N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Blu City Centre | Welcomhotel by ITC Bay Island | The Promenade | Palais de Mahe',
            ),
            _hotel(
                'Taj Connemara | The Leela Palace Radisson Blu Resort Temple Bay La | Maison Perumal',
                'Tamil Nadu',
                '4N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Taj Connemara | The Leela Palace Radisson Blu Resort Temple Bay La | Maison Perumal',
            ),
            _hotel(
                'ITC Grand Chola (Executive',
                'Tamil Nadu',
                '4N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: ITC Grand Chola (Executive',
            )
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Handpicked luxury and heritage hotels as per selected tier.', 1),
            _inc_included('Luxury Transportation: Private chauffeur-driven AC Innova Crysta for all sightseeing.', 2),
            _inc_included('Curated Meal Plan: Daily lavish multi-cuisine buffet breakfasts and gourmet dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated travel concierge and elite guest experience manager.', 4),
            _inc_included('Welcome Amenities: Personalized family refreshment kit, cold wipes, and travel essentials.', 5),
            _inc_included("Complimentary Experience: Guided heritage evening walk through Pondicherry's French Quarter.", 6),
            _inc_excluded('Airfare / Train tickets to and from Chennai.', 7),
            _inc_excluded('Monument entry fees, camera permits, and local structural guide charges.', 8),
            _inc_excluded('Personal expenses such as laundry, premium liquor, laundry, and tipping.', 9),
            _inc_excluded('Any optional activities, boat rides, or water sports charges.', 10),
        ],
    )
    return package, itinerary

def build_tn_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TN-005'
    tour_code = 'TRG-TN-005'
    title = 'NAVGRAHA CIRCUIT • THE CELESTIAL NINE PLANETS PILGRIMAGE'
    duration = '04 Nights / 05 Days'
    slug = 'tn-005-navgraha-circuit-the-celestial-nine-planets-pilgrimage'
    itin_slug = 'tn-005-navgraha-circuit-the-celestial-nine-planets-pilgrimage-itinerary'
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
            _ph('Serial code TN-005 | TRAGUIN tour code TRG-TN-005', 1),
            _ph('State / Country: Tamil Nadu / India | Category: Premium Spiritual Pilgrimage', 2),
            _ph('Destinations: Trichy •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Innova Crysta / MAPAI (Satvik Cuisine Options)', 7),
            _ph('TRAGUIN Signature Experience: Pre-arranged local temple guides ensuring structured step-by-step', 8),
            _ph('TRAGUIN Premium Luxury Itinerary — TN-005 5', 9),
            _ph('Curated by TRAGUIN Experts: Smart sequential routing designed around ancient temple opening hours', 10),
            _ph('Premium Handpicked Hotels: Properties specifically chosen for their tranquil environments and hygienic', 11)
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
        tagline='NAVGRAHA CIRCUIT',
        overview="NAVGRAHA CIRCUIT • THE CELESTIAL NINE PLANETS PILGRIMAGE TRAGUIN Premium Luxury Itinerary — TN-005 1 Welcome to an extraordinary spiritual quest curated exclusively by TRAGUIN. Embark on the definitive Tamil Nadu Family Tour, meticulously orchestrated around the ancient Chola kingdom's sacred geography. As your trusted premium travel consultants, TRAGUIN transforms this celestial tour into a seamless luxury holiday. Unveil the architectural marvels, cosmic energies, and deep spiritual heritage of the classic Navgraha circuit. Complete with premium stays, private specialized temple assistance, and absolute comfort, this journey ensures unforgettable memories for you and your family.\n\nTOUR OVERVIEW\nThis custom luxury pilgrimage itinerary offers an unparalleled balance between deep spiritual devotion and premium personal relaxation. Travelling in a dedicated, private luxury transport vehicle with an experienced, verified regional chauffeur, your family will experience absolute ease on the road. Featuring a thoughtful meal plan containing traditional south Indian vegetarian fares alongside elite global breakfasts, this route stands as the ultimate premium Tamil Nadu experience. Every phase of your travel includes the signature TRAGUIN curated experience note, guaranteeing specialized priest access, timed darshans, and round-the-clock ground coordination.\n\nWHY CHOOSE THE BEST TAMIL NADU TOUR PACKAGE?\nWhen seeking a Luxury Tamil Nadu Holiday, discerning pilgrims look far beyond standard tour arrangements. The ancient Kaveri delta region around Kumbakonam contains the world's only intact cluster of shrines dedicated to the nine celestial planetary deities, making a Tamil Nadu Pilgrimage Package a profoundly transformative experience. From the legendary architectural genius of Brihadeeswarar Temple in Thanjavur to the timeless spiritual vibrations of the Navgraha temples, Tamil Nadu sightseeing reveals unprecedented depth. For multi-generational households booking a curated Tamil Nadu Family Tour or couples seeking a uniquely peaceful Tamil Nadu Honeymoon Package, this region provides scenic beauty lined with grand temple tanks, lush paddy fields, and popular Instagram locations like traditional heritage mansions and bronze casting studios. Indulge in authentic silk shopping, sample local degree coffee, and immerse your spirit in old- world tranquility. Our high-end TRAGUIN Tamil Nadu Packages fuse exclusive experiences with premium",
        seo_title='TN-005 | NAVGRAHA CIRCUIT | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Tamil Nadu package (TN-005 / TRG-TN-005): Trichy • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN TRICHY TO KUMBAKONAM', 1),
            _ih('Day 02: NAVGRAHA EASTERN CIRCUIT', 2),
            _ih('Day 03: NAVGRAHA INNER CIRCUIT', 3),
            _ih('Day 04: NAVGRAHA CONCLUSION TO THANJAVUR', 4),
            _ih('Day 05: THANJAVUR TO TRICHY / DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Pre-arranged local temple guides ensuring structured step-by-step', 6),
            _ih('TRAGUIN Premium Luxury Itinerary — TN-005 5', 7),
            _ih('Curated by TRAGUIN Experts: Smart sequential routing designed around ancient temple opening hours', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN TRICHY TO KUMBAKONAM',
                (
                    'WELCOME TO THE TEMPLE CITY – GATEWAY TO CELESTIAL BLESSINGS Your premium Tamil Nadu experience begins upon arrival at Trichy Airport/Railway Station. A dedicated private luxury transport vehicle will greet you for a comfortable scenic drive towards Kumbakonam, the sacred hub of your pilgrimage. Check into your premium handpicked heritage-luxury resort and relax. In the evening, visit the stunning Thingaloor Temple (dedicated to the Moon - Chandra) to inaugurate your cosmic alignment trail.'
                ),
                [
                    'Sightseeing Included: Thingaloor Chandran Temple, serene village landscape drive.',
                    'Evening Experience: Exclusive welcoming traditional filter coffee tasting session and orientation.',
                    'Overnight Stay: Kumbakonam (Premium Heritage Luxury Resort)',
                    'Meals Included: Welcome Drink & Gourmet Dinner',
                ],
            ),
            _day(
                2,
                'NAVGRAHA EASTERN CIRCUIT',
                (
                    'SUN, MARS & MERCURY – ARCHITECTURAL GENIUS & SPIRITUAL ENERGY Awake early for a peaceful morning breakfast. Today, your specialized Tamil Nadu sightseeing trail covers three major temples. Visit Suryanar Kovil (The Sun God temple), followed by the majestic Vaitheeswaran Kovil (Mars - Angarakan), celebrated for its historic healing properties. Conclude your afternoon at Thiruvenkadu (Mercury - Budhan). Appreciate the breathtaking landscapes of rural Tamil Nadu along the route, capturing timeless photography points.'
                ),
                [
                    'Sightseeing Included: Suryanar Kovil, Vaitheeswaran Kovil, Thiruvenkadu Temple complex.',
                    'Optional Activities: Private consultation with traditional Nadi Astrologers at Vaitheeswaran Kovil.',
                    'Overnight Stay: Kumbakonam (Premium Heritage Luxury Resort)',
                    'Meals Included: Premium Breakfast & Satvik Dinner',
                ],
            ),
            _day(
                3,
                'NAVGRAHA INNER CIRCUIT',
                (
                    "JUPITER, VENUS & RAHU – SACRED RITUALS & IMMERSIVE EXPERIENCES Enjoy a lavish breakfast before entering the inner core of the Navgraha circuit. Visit Alangudi (Jupiter - Guru), followed by the beautiful Thirunageswarar temple (Rahu), famous for its milk abhishekam miracle. In the afternoon, explore Kanchanur (Venus - Sukran), surrounded by lush paddy fields. Every step of today's tour is rich with emotional storytelling provided by your local guide companion."
                ),
                [
                    'Sightseeing Included: Alangudi Guru Temple, Thirunageswarar Rahu Temple, Kanchanur Sukran Temple.',
                    'Evening Experience: Special pre-arranged VIP entry for evening rituals at Thirunageswarar.',
                    'Overnight Stay: Kumbakonam (Premium Heritage Luxury Resort)',
                    'Meals Included: Premium Breakfast & Authentic South Indian Dinner',
                ],
            ),
            _day(
                4,
                'NAVGRAHA CONCLUSION TO THANJAVUR',
                (
                    'SATURN & KETU TO THE ROYAL SEAT OF CHOLAS After breakfast, complete the final leg of the Navgraha pilgrimage. Drive to Thirunallar (Saturn - Shani), arguably the most sought-after shrine on this circuit, followed by Keezhaperumpallam (Ketu). With your planetary path completed, proceed to Thanjavur. Visit the legendary Brihadeeswarar Temple (Big Temple), a UNESCO World Heritage site and a highly popular Instagram location due to its massive shadow-dropping vimana architecture.'
                ),
                [
                    'Sightseeing Included: Thirunallar Shani Temple, Keezhaperumpallam, Thanjavur Big Temple, Maratha Palace.',
                    'Evening Experience: Illuminated evening walk around the golden stone corridors of Brihadeeswarar.',
                    'Overnight Stay: Thanjavur (Luxury Palace-Style Property)',
                    'Meals Included: Premium Breakfast & Royal Thanjavur Dinner',
                ],
            ),
            _day(
                5,
                'THANJAVUR TO TRICHY / DEPARTURE',
                (
                    'HERITAGE FINALE – UNFORGETTABLE MEMORIES SECURED Indulge in a final lavish breakfast at your premium hotel. Check out and drive towards Trichy. Time permitting, visit the famous Rockfort Temple or Srirangam Ranganathaswamy Temple, the largest functioning temple complex in the world. Afterwards, your private luxury transport will drop you at Trichy Airport/Railway Station. Your sacred journey concludes, leaving you with divine peace and unforgettable memories designed beautifully by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door transit drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                "Raya's Grand | Indeco Heritage Resort | Premium Comfort",
                'Tamil Nadu',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description="OPTION 01 – DELUXE: Raya's Grand | Indeco Heritage Resort | Premium Comfort",
            ),
            _hotel(
                'Mantra Heritage Eco-Resort | Great Trails River View by GRT | Private Balcony Garden Views',
                'Tamil Nadu',
                '4N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Mantra Heritage Eco-Resort | Great Trails River View by GRT | Private Balcony Garden Views',
            ),
            _hotel(
                'Svatma Kumbakonam (Heritage | Luxury Boutique Spa Access, Curated Cultural Shows',
                'Tamil Nadu',
                '4N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Svatma Kumbakonam (Heritage | Luxury Boutique Spa Access, Curated Cultural Shows',
            ),
            _hotel(
                'Mantra Heritage (Executive Royal',
                'Tamil Nadu',
                '4N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Mantra Heritage (Executive Royal',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Handpicked properties reflecting traditional heritage and modern luxury.', 1),
            _inc_included('Luxury Transportation: Chauffeur-driven AC Innova Crysta for smooth, customized travel.', 2),
            _inc_included('Curated Meals: Daily high-end breakfasts and rich regional dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated travel consultant and priority ground assistance.', 4),
            _inc_included('Welcome Amenities: Specialized divine welcome kit and traditional stole presentation.', 5),
            _inc_included('Complimentary Experience: Filter coffee brewing masterclass and heritage walk.', 6),
            _inc_excluded('Airfare, flight tickets, or train costs to/from Trichy.', 7),
            _inc_excluded('Special puja ticket pricing and personal temple offerings (Archanai kits).', 8),
            _inc_excluded('Personal items such as laundry, phone bills, or premium drinks.', 9),
            _inc_excluded('Tips, portages, and optional custom heritage detours.', 10),
        ],
    )
    return package, itinerary

TAMIL_NADU_TN_002_005_BUILDERS = [
    build_tn_002,
    build_tn_003,
    build_tn_004,
    build_tn_005,
]
