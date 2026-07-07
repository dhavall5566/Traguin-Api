"""Builder functions for UK-011 through UK-018 Uttarakhand domestic packages."""

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

UTTARAKHAND_SLUG = "uttarakhand"


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

def build_uk_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UK-011'
    tour_code = 'TR-UK-011-FAM'
    title = 'Nainital • Corbett Gateway Luxury Escape'
    duration = '04 Nights / 05 Days'
    slug = 'uk-011-nainital-corbett-gateway-luxury-escape'
    itin_slug = 'uk-011-nainital-corbett-gateway-luxury-escape-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Uttarakhand, India | Category: Family / Luxury Wilderness & Lakes', 2),
            _ph('Destinations: Nainital • Bhimtal • Jim Corbett National Park', 3),
            _ph('Ideal for: Premium Families, Nature Enthusiasts, Wildlife Lovers', 4),
            _ph('Best season: Round the Year (September to June Ideal)', 5),
            _ph('Starting price: On Request (Premium Luxury Tier)', 6),
            _ph('Vehicle & Meals: Private Luxury Innova Crysta / Premium | MAPAI Plan', 7),
            _ph('Route: Delhi → Nainital (2N) → Jim Corbett National Park (2N) → Delhi Departure', 8),
            _ph('TRAGUIN Signature Experience: Private, smooth open-top 4x4 jungle safari with expert wildlife naturalists.', 9),
            _ph('Curated by TRAGUIN Experts: A perfectly balanced itinerary blending relaxing mountain stays with exciting wilderness.', 10),
            _ph('Premium Handpicked Hotels: Properties selected for excellent safety, scenic views, and high-quality customer service.', 11),
            _ph('Exclusive Recommendations: Access to beautiful, quiet lakeside observation spots for your family.', 12),
            _ph('Shopping & Local Experiences: Mall Road Boutiques — handcrafted aromatic candles, wooden artifacts, and warm Kumaoni woolens. Local Delicacies: Authentic local sweets like Bal Mithai and Singauri prepared by gourmet chefs.', 13),
            _ph('Important Notes: Hotel Policies: Standard check-in time is 14:00 hrs; early check-in is subject to room availability. Safari Booking: Jim Corbett safari zones are allocated by forest authorities and require booking well in advance. Weather Advisory: Pack comfortable layers for Nainital\'s cool evenings and light clothes for Corbett safaris. Transport Rules: Vehicles are designated for the specific route outlined in the itinerary; extra detours may incur charges.', 14),
        ],
        moods=['Family', 'Luxury', 'Wildlife', 'Lakes'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Nainital • Corbett Gateway Luxury Escape • 04 Nights / 05 Days',
        overview=('Discover the perfect combination of pristine lakes and thrilling wilderness. Our Best Uttarakhand Tour Package is carefully designed to offer an immersive, high-end experience for your family. This Luxury Uttarakhand Holiday takes you from the beautiful, mist-covered lakes of Nainital to the legendary tiger territory of Jim Corbett National Park, ensuring unforgettable memories across breathtaking landscapes.\n\nTOUR OVERVIEW\nThis premium holiday itinerary delivers an exceptional Uttarakhand Family Tour. Traveling in private luxury vehicles with dedicated assistance, guests will experience the magnificent scenic beauty and iconic attractions of the Kumaon region. Every detail aligns with the premier standards of a signature TRAGUIN Uttarakhand Package, featuring handpicked hotels that guarantee high-end comfort and relaxation.\n\nWhy Visit Uttarakhand? Known as the Land of the Gods, Uttarakhand offers a majestic escape into nature. It stands out as an excellent destination for family vacations and honeymoons, blending cool mountain air with rich flora and fauna.\n\nFamous Attractions & Iconic Highlights: The beautiful Naini Lake, the stunning viewpoints of Nainital, the peaceful waters of Bhimtal, and the historic wildlife zones of Jim Corbett National Park are prime tourist places in Uttarakhand that attract global travelers.\n\nMost Searched Experiences: Enjoying a private boat ride on Naini Lake, riding the scenic aerial ropeway, and embarking on an open-top 4x4 morning jeep safari in Corbett are among the top luxury travel highlights requested by premium holiday seekers.\n\nBest Time to Visit Uttarakhand: March to June offers excellent weather for sightseeing, while the post-monsoon months from September to November provide crisp, clear mountain views.'),
        seo_title='UK-011 | Nainital Corbett Gateway Luxury Escape | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Uttarakhand package (UK-011 / TR-UK-011-FAM): Nainital lakes, Bhimtal, Jim Corbett jungle safari, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Naini Lake boating, Naina Devi Temple, Snow View Point ropeway, and Bhimtal lakes', 1),
            _ih('Jim Corbett National Park open-top 4x4 morning jeep safari with expert naturalist', 2),
            _ih('Corbett Museum, Garjiya Devi Temple, and riverside wilderness resort stay', 3),
            _ih('TRAGUIN Signature Experience: Private open-top 4x4 jungle safari with expert wildlife naturalists', 4),
            _ih('4-tier handpicked accommodation: Nainital (02 Nights) + Jim Corbett (02 Nights)', 5),
        ],
        days=[
            _day(1, 'ARRIVAL DELHI TO NAINITAL', ('Arrive in Delhi, where a dedicated driver from TRAGUIN will greet you warmly with personalized assistance. Board your private luxury vehicle and enjoy a smooth, scenic drive up into the foothills of the Himalayas heading toward Nainital. As you climb higher, the plains open up into breathtaking landscapes and fresh mountain air. Arrive in Nainital by afternoon and check into your premium handpicked hotel. Spend a relaxed evening walking along the famous Mall Road, enjoying the cool mountain breeze and beautiful views of the lake. This curated introduction sets a peaceful, majestic tone for your luxury stay.'), [
                'Sightseeing Included: Mall Road walk and evening lake views.',
                'Evening Experience: Leisurely stroll along the brightly lit lakefront.',
                'Overnight Stay: Premium Luxury Hotel in Nainital.',
                'Meals Included: Welcome Dinner at the hotel restaurant.',
            ]),
            _day(2, 'NAINITAL SIGHTSEEING & LAKE TOUR', ('Begin your day with a delicious breakfast before diving into a comprehensive Nainital Sightseeing tour. Your first highlight is a private boat cruise across the emerald waters of Naini Lake, followed by a visit to the historic Naina Devi Temple located on the northern shore. Next, take an exciting aerial ropeway ride up to Snow View Point, which offers incredible, sweeping views of the snow-capped Himalayan peaks. In the afternoon, take a relaxed drive out to explore the nearby lakes of Bhimtal and Sattal, enjoying their quiet charm and beautiful forests away from the main town crowds.'), [
                'Sightseeing Included: Naini Lake boating, Naina Devi Temple, Snow View Point, Bhimtal.',
                'Photography Points: Panoramic mountain peaks from Snow View Point and the reflections on Bhimtal.',
                'Overnight Stay: Premium Luxury Hotel in Nainital.',
                'Meals Included: Breakfast & Multi-cuisine Dinner.',
            ]),
            _day(3, 'NAINITAL TO JIM CORBETT NATIONAL PARK', ('After a relaxed breakfast, leave the mountains behind as you drive down toward the foothills to reach Jim Corbett National Park, India\'s legendary wildlife sanctuary. The route winds through dense sal forests and charming local villages. Arrive at your premium wilderness river resort and check into your luxury cottage. Spend the afternoon relaxing by the pool or listening to the gentle sounds of the Kosi River. In the evening, enjoy an informative nature presentation hosted by the resort\'s resident naturalist, preparing you for the jungle safari tomorrow.'), [
                'Sightseeing Included: Scenic drive and Corbett orientation presentation.',
                'Evening Experience: Riverside high-tea and wildlife documentary screening.',
                'Overnight Stay: Premium Wilderness Resort in Jim Corbett.',
                'Meals Included: Breakfast & Evening Gourmet Dinner.',
            ]),
            _day(4, 'JUNGLE SAFARI EXCURSION', ('Wake up early for the highlight of your Premium Uttarakhand Experience. Board an open-top 4x4 safari jeep for an exciting morning drive into the core wildlife zone of Jim Corbett National Park. With help from an expert naturalist, track the majestic Bengal Tiger, wild elephants, leopards, and various deer species. Return to the resort for a hearty breakfast and well-deserved rest. In the afternoon, visit the historic Corbett Museum—the former home of Jim Corbett—and the sacred Garjiya Devi Temple, which sits on a massive rock in the middle of the Kosi River.'), [
                'Sightseeing Included: 4x4 Morning Jungle Safari, Corbett Museum, Garjiya Temple.',
                'Optional Activities: Relaxing luxury spa treatment at the resort wellness center.',
                'Overnight Stay: Premium Wilderness Resort in Jim Corbett.',
                'Meals Included: Breakfast, Lunch & Special Farewell Dinner.',
            ]),
            _day(5, 'JIM CORBETT TO DELHI DEPARTURE', ('Savor a luxurious breakfast at your resort before completing your check-out. Board your private luxury vehicle for the smooth return drive back to Delhi. Your premium Uttarakhand Honeymoon Package or family getaway concludes seamlessly as your driver drops you off at the Delhi Airport or railway station for your flight home. You return with beautiful photographs, enriched perspectives, and unforgettable memories of a remarkable journey designed and managed by the expert travel team at TRAGUIN.'), [
                'Transfers Included: Private airport drop-off via luxury vehicle.',
                'Meals Included: Lavish Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('The Pavilion / Similar', 'Nainital', '02 Nights', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner (MAPAI)', 4, 1, description='OPTION 01 – DELUXE: The Pavilion / Similar (Nainital, 02 Nights)'),
            _hotel('Corbett Machaan Resort / Similar', 'Jim Corbett', '02 Nights', 'Deluxe', 'Deluxe Cottage', 'Breakfast & Dinner (MAPAI)', 4, 2, description='OPTION 01 – DELUXE: Corbett Machaan Resort / Similar (Jim Corbett, 02 Nights)'),
            _hotel('The Manu Maharani / Similar', 'Nainital', '02 Nights', 'Premium', 'Premium Room', 'Breakfast & Dinner (MAPAI)', 4, 3, description='OPTION 02 – PREMIUM: The Manu Maharani / Similar (Nainital, 02 Nights)'),
            _hotel('Corbett River Creek Resort', 'Jim Corbett', '02 Nights', 'Premium', 'Premium Cottage', 'Breakfast & Dinner (MAPAI)', 4, 4, description='OPTION 02 – PREMIUM: Corbett River Creek Resort (Jim Corbett, 02 Nights)'),
            _hotel('The Naini Retreat / Similar', 'Nainital', '02 Nights', 'Luxury', 'Luxury Suite', 'Luxury Gourmet MAPAI Plan', 5, 5, description='OPTION 03 – LUXURY: The Naini Retreat / Similar (Nainital, 02 Nights)'),
            _hotel('Namah Resort / Wood Castle', 'Jim Corbett', '02 Nights', 'Luxury', 'Luxury Cottage', 'Luxury Gourmet MAPAI Plan', 5, 6, description='OPTION 03 – LUXURY: Namah Resort / Wood Castle (Jim Corbett, 02 Nights)'),
            _hotel('The Grand Hotel Luxury Lakefront Suite', 'Nainital', '02 Nights', 'Ultra Luxury', 'Luxury Lakefront Suite', 'All-Inclusive Bespoke Dining', 5, 7, description='OPTION 04 – ULTRA LUXURY: The Grand Hotel Luxury Lakefront Suite (Nainital, 02 Nights)'),
            _hotel('The Taj Corbett Resort & Spa', 'Jim Corbett', '02 Nights', 'Ultra Luxury', 'Luxury Villa', 'All-Inclusive Bespoke Dining', 5, 8, description='OPTION 04 – ULTRA LUXURY: The Taj Corbett Resort & Spa (Jim Corbett, 02 Nights)'),
        ],
        inclusions=[
            _inc_included('Accommodation: 04 Nights stay in handpicked, premium luxury hotel rooms and jungle cottages.', 1),
            _inc_included('Meals: Daily breakfasts and dinners tailored to your family\'s preferences.', 2),
            _inc_included('Transfers: All transfers and daily sightseeing via a private, air-conditioned Luxury vehicle.', 3),
            _inc_included('Sightseeing: All entry tickets, Naini Lake boat ride, and a private open-top 4x4 Corbett Jeep Safari.', 4),
            _inc_included('Assistance: 24/7 dedicated support and local concierge assistance from TRAGUIN.', 5),
            _inc_included('Welcome Amenities: Refreshing arrival drinks and complimentary mineral water.', 6),
            _inc_included('Taxes: All applicable luxury hotel taxes, parking fees, toll costs, and driver allowances.', 7),
            _inc_excluded('Airfare or train tickets to and from Delhi.', 8),
            _inc_excluded('Personal expenses such as laundry, phone calls, premium drinks, or minibar usage.', 9),
            _inc_excluded('Travel health insurance and emergency medical expenses.', 10),
            _inc_excluded('Tips, porter fees at airport/hotels, and optional camera charges at monuments.', 11),
        ],
    )
    return package, itinerary

def build_uk_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UK-012'
    tour_code = 'TR-UK-012'
    title = 'Mussoorie Rishikesh Escape'
    duration = '05 Nights / 06 Days'
    slug = 'uk-012-mussoorie-rishikesh-escape'
    itin_slug = 'uk-012-mussoorie-rishikesh-escape-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Uttarakhand, India | Category: Family Premium Escape', 2),
            _ph('Destinations: Mussoorie • Rishikesh • Dehradun', 3),
            _ph('Ideal for: Families, Leisure Travelers', 4),
            _ph('Best season: April to June & Sep to Dec', 5),
            _ph('Vehicle & Meals: Private high-end luxury vehicle | MAPAI (Breakfast & Dinner)', 6),
            _ph('Route: Dehradun Arrival → Mussoorie (3N) → Rishikesh (2N) → Dehradun Departure', 7),
            _ph('TRAGUIN Signature Experience: Private family bonfire and storytelling evening nestled in the crisp hills of Mussoorie.', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked boutique locations offering the ultimate mountain views and absolute privacy.', 9),
            _ph('Personalized Assistance: Dedicated destination manager monitoring every transition smoothly via WhatsApp for real-time comfort.', 10),
            _ph('Premium Handpicked Hotels: Elite properties recognized for their outstanding multi-generational family comfort and premium wellness amenities.', 11),
            _ph('Luxury Transportation: Top-tier vehicles cleaned daily, driven by well-mannered, experienced mountain chauffeurs.', 12),
            _ph('Shopping & Local Culinary Encounters: Mussoorie Mall Road and Sister\'s Bazaar for hand-knitted woolen shawls, oakwood artifacts, and handmade preserves. Landour cafes for cinnamon rolls and artisanal cheeses. Rishikesh markets for rudraksha beads, organic oils, Himalayan crystal salts, and brass prayer items.', 13),
            _ph('Important Notes: Hotel Policies: Standard check-in time is 14:00 hrs and check-out is 11:00 hrs. Early check-in is subject to room availability. Weather Considerations: Mussoorie can get crisp in the evenings; families are advised to carry light to medium woolens even during the summer months. Transport Regulations: Heavy commercial transport vehicles are occasionally restricted on Mussoorie Mall Road during peak evening hours. Advance Booking Suggestions: Due to the exclusive nature of handpicked luxury properties, early confirmations are highly recommended to secure the most premium rooms.', 14),
        ],
        moods=['Family', 'Luxury', 'Spiritual', 'Hills'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Class)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Premium Uttarakhand Tour Package • Mussoorie Rishikesh Escape • 05 Nights / 06 Days',
        overview=('Welcome to the land of sublime serenity and majestic peaks. The Best Uttarakhand Tour Package by TRAGUIN invites your family to immerse themselves in a world where the misty hills of Mussoorie blend seamlessly with the sacred, soul-stirring currents of Rishikesh. This meticulously planned Uttarakhand Family Tour promises an exquisite tapestry of shared laughter, breathtaking landscapes, handpicked premium stays, and deeply immersive local experiences.\n\nTOUR OVERVIEW\nThis elite TRAGUIN Uttarakhand Package is curated exclusively for families seeking an optimal balance of leisure, cultural immersion, and scenic beauty. Leaving behind ordinary sightseeing routes, our itinerary takes you along the most beautiful corridors of Garhwal. Traveling in an exclusive, high-end luxury vehicle with professional assistance at every milestone, your family will enjoy custom meal plans featuring both gourmet international cuisine and authentic regional delicacies. From the tumbling cascades of Kempty Falls to the iconic evening Ganga Aarti, every aspect represents a signature, handpicked Premium Uttarakhand Experience designed by the destination experts at TRAGUIN.\n\nWhy Visit Uttarakhand? Uttarakhand, fondly called Devbhoomi or the Land of the Gods, stands as one of India\'s most highly searched tourism keywords for travelers looking for pure nature and pristine peace. Families can enjoy the famous attractions of Mussoorie, known affectionately as the Queen of the Hills, where the iconic Mall Road and cloud-kissed peaks provide top popular Instagram locations.\n\nTransitioning to Rishikesh delivers a contrasting spiritual and adventure-rich highlight. Known globally as the Yoga Capital of the world, Rishikesh features highly searched tourism experiences like walking across the iconic Lakshman Jhula and Ram Jhula, visiting the tranquil Beatles Ashram, and capturing the scenic beauty of the holy river Ganges reflecting the setting sun.'),
        seo_title='UK-012 | Mussoorie Rishikesh Escape | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Uttarakhand package (UK-012 / TR-UK-012): Mussoorie hills, Landour, Dhanaulti, Rishikesh Ganga Aarti, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Kempty Falls, Company Garden, Camel\'s Back Road, and Landour cantonment excursion', 1),
            _ih('Dhanaulti Eco Park, Surkanda Devi viewpoint, and family bonfire evening in Mussoorie', 2),
            _ih('Evening Ganga Aarti, Ram Jhula, Lakshman Jhula, Beatles Ashram, and Trayambakeshwar Temple', 3),
            _ih('TRAGUIN Signature Experience: Private family bonfire and storytelling evening in Mussoorie hills', 4),
            _ih('4-tier handpicked accommodation: Mussoorie (03 Nights) + Rishikesh (02 Nights)', 5),
        ],
        days=[
            _day(1, 'ARRIVALS IN DEHRADUN TO THE MAJESTIC HILLS OF MUSSOORIE', ('Your extraordinary luxury vacation commences the moment you arrive at Dehradun Airport or Railway Station. A courteous TRAGUIN representative will receive your family with traditional welcome amenities and guide you to your private luxury vehicle. Begin a spellbinding, scenic drive ascending through the winding mountain roads towards Mussoorie, absorbing the breathtaking landscapes and cool Himalayan air. Upon arrival, check into your exquisitely appointed handpicked luxury resort. Spend your afternoon relaxing or taking a leisurely stroll along the historic Mall Road, discovering quaint shops, beautiful colonial architecture, and capturing spectacular photography points over the Doon Valley.'), [
                'Sightseeing Included: Doon Valley scenic drive, Mall Road walking tour, Gun Hill viewpoint via cable car (optional).',
                'Evening Experience: Sunset photography over the ridge followed by a premium multi-cuisine dinner at the resort.',
                'Overnight Stay: Mussoorie Premium Resort.',
                'Meals Included: Dinner Included.',
            ]),
            _day(2, 'MUSSOORIE SIGHTSEEING & IMMERSIVE NATURE TRAILS', ('Awake to a gorgeous mountain sunrise and enjoy a sumptuous breakfast spread. Today is dedicated to exploring the top tourist places in Mussoorie. Proceed first to the magnificent Kempty Falls, where water cascades dramatically down multiple tiers into a refreshing pool below—a perfect spot for unforgettable family photographs. Next, travel to the tranquil Company Garden, a beautifully landscaped park boasting vibrant floral displays and a small amusement lake. In the afternoon, explore the lush, peaceful walking paths of Camel\'s Back Road, a scenic route named after a natural rock formation that mimics a camel\'s silhouette, offering absolute peace away from the bustling crowds.'), [
                'Sightseeing Included: Kempty Falls, Company Garden, Camel\'s Back Road nature walk, Mussoorie Christ Church.',
                'Optional Activities: Local Garhwali textile shopping at Landour Bazaar, hot chocolate tasting at Landour Bakehouse.',
                'Overnight Stay: Mussoorie Premium Resort.',
                'Meals Included: Breakfast & Dinner Included.',
            ]),
            _day(3, 'EXCURSION TO THE HIDDEN GEMS OF LANDOUR & DHANAULTI', ('Following breakfast, embark on an exclusive journey to the serene, colonial-era cantonment town of Landour, a highly recommended TRAGUIN Signature Experience. Walk along peaceful pine-fringed roads, listening to the whispering wind and gazing at distant snow-capped Himalayan peaks. Later, extend your excursion to Dhanaulti, a tranquil retreat famous for its expansive, lush Eco Parks filled with towering Deodar trees. Your family can walk along pristine eco-trails, indulge in light adventure activities, or simply find a quiet corner to breathe in the pure mountain atmosphere. Return to Mussoorie in the evening for a relaxed dinner.'), [
                'Sightseeing Included: Landour Cantonment, Sister\'s Bazaar, Dhanaulti Eco Park, Surkanda Devi viewpoint route.',
                'Evening Experience: Family bonfire night organized at the resort with curated acoustic background music.',
                'Overnight Stay: Mussoorie Premium Resort.',
                'Meals Included: Breakfast & Dinner Included.',
            ]),
            _day(4, 'MUSSOORIE TO THE SPIRITUAL SANCTUARY OF RISHIKESH', ('Bid a fond farewell to the hills of Mussoorie as your family transitions from the heights to the holy river banks. Board your luxury transport for a comfortable drive downwards to Rishikesh, stopping briefly to admire the lush Sahastradhara springs or the historic temples of Dehradun. Arrive in Rishikesh, the spiritual soul of your Rishikesh Escape, and check into your premium luxury wellness resort overlooking the Ganges. In the late afternoon, your private guide will lead you to the riverbanks to witness the spectacular, world-famous Evening Ganga Aarti at Triveni Ghat or Parmarth Niketan. The rhythmic chanting, flaming brass lamps, and hymns create a deeply moving, emotional storytelling ambiance that will stay with your family forever.'), [
                'Sightseeing Included: Dehradun en-route stops, Rishikesh riverside walk, iconic Evening Ganga Aarti.',
                'Evening Experience: Partaking in floating traditional clay lamps (diyas) down the sacred Ganges river.',
                'Overnight Stay: Rishikesh Luxury Wellness Resort.',
                'Meals Included: Breakfast & Dinner Included.',
            ]),
            _day(5, 'EXPLORING THE ICONIC CULTURAL CORRIDORS OF RISHIKESH', ('Dedicate your morning to wellness with a brief, complimentary family yoga session at the resort, followed by a wholesome breakfast. Today, delve into the legendary Rishikesh Sightseeing experiences. Walk across the architectural wonders of Ram Jhula and Lakshman Jhula, feeling the refreshing spray of the river below. Visit the historic Geeta Bhawan, the multi-tiered Trayambakeshwar Temple, and journey into the mesmerizing ruins of the Beatles Ashram, where the legendary band practiced transcendental meditation in 1968. This site serves as an amazing Instagram location with its beautifully graffitied dome walls wrapped in natural overgrowth. Spend your evening exploring vibrant cafes or relaxing by the sandy river shores.'), [
                'Sightseeing Included: Ram Jhula, Lakshman Jhula suspension bridges, Beatles Ashram, Trayambakeshwar Temple.',
                'Optional Activities: Mild family white-water rafting (grade 1) or an exclusive Ayurvedic spa massage at the resort.',
                'Overnight Stay: Rishikesh Luxury Wellness Resort.',
                'Meals Included: Breakfast & Dinner Included.',
            ]),
            _day(6, 'DEPARTURE VIA DEHRADUN - MEMORIES FOREVER', ('Savor a leisurely breakfast on your final morning looking out at the mist rising from the Ganges. Spend a few quiet moments documenting your journey or purchasing last-minute organic souvenirs from the local markets. At the designated hour, pack your bags and board your private luxury vehicle. Your professional chauffeur will smoothly transfer your family back to Dehradun Airport or Railway Station for your onward journey home. Your magical TRAGUIN Uttarakhand Package concludes here, leaving your family with refreshed minds, closer bonds, and unforgettable memories that will last a lifetime.'), [
                'Sightseeing Included: Leisurely morning resort checkout and departure airport transfer.',
                'Meals Included: Gourmet Buffet Breakfast at the resort.',
            ]),
        ],
        hotels=[
            _hotel('The Fern Hillside Resort / Similar', 'Mussoorie', '03 Nights', 'Deluxe', 'Deluxe Room', 'MAPAI (BF + Dinner)', 4, 1, description='OPTION 01 – DELUXE: The Fern Hillside Resort / Similar (Mussoorie, 03 Nights)'),
            _hotel('Lemon Tree Premier / Similar', 'Rishikesh', '02 Nights', 'Deluxe', 'Deluxe Room', 'MAPAI (BF + Dinner)', 4, 2, description='OPTION 01 – DELUXE: Lemon Tree Premier / Similar (Rishikesh, 02 Nights)'),
            _hotel('Welcomhotel by ITC, The Savoy', 'Mussoorie', '03 Nights', 'Premium', 'Premium Room', 'MAPAI (BF + Dinner)', 4, 3, description='OPTION 02 – PREMIUM: Welcomhotel by ITC, The Savoy (Mussoorie, 03 Nights)'),
            _hotel('Aloha On The Ganges / Similar', 'Rishikesh', '02 Nights', 'Premium', 'Premium Room', 'MAPAI (BF + Dinner)', 4, 4, description='OPTION 02 – PREMIUM: Aloha On The Ganges / Similar (Rishikesh, 02 Nights)'),
            _hotel('JW Marriott Mussoorie Walnut Grove', 'Mussoorie', '03 Nights', 'Luxury', 'Luxury Room', 'MAPAI (BF + Dinner)', 5, 5, description='OPTION 03 – LUXURY: JW Marriott Mussoorie Walnut Grove (Mussoorie, 03 Nights)'),
            _hotel('Taj Rishikesh Resort & Spa', 'Rishikesh', '02 Nights', 'Luxury', 'Luxury Room', 'MAPAI (BF + Dinner)', 5, 6, description='OPTION 03 – LUXURY: Taj Rishikesh Resort & Spa (Rishikesh, 02 Nights)'),
            _hotel('The Ritz-Carlton Reserve / Elite Estate', 'Mussoorie', '03 Nights', 'Ultra Luxury', 'Luxury Suite', 'Gourmet Full Board', 5, 7, description='OPTION 04 – ULTRA LUXURY: The Ritz-Carlton Reserve / Elite Estate (Mussoorie, 03 Nights)'),
            _hotel('Ananda In The Himalayas', 'Rishikesh', '02 Nights', 'Ultra Luxury', 'Luxury Suite', 'Gourmet Full Board', 5, 8, description='OPTION 04 – ULTRA LUXURY: Ananda In The Himalayas (Rishikesh, 02 Nights)'),
        ],
        inclusions=[
            _inc_included('Premium Accommodations: Handpicked luxury stays across Mussoorie and Rishikesh.', 1),
            _inc_included('Curated Meal Plans: Daily buffet breakfast and dinners at the resorts.', 2),
            _inc_included('Luxury Private Vehicle: Dedicated air-conditioned SUV for all transfers and custom sightseeing routes.', 3),
            _inc_included('Welcome Amenities: Personalized welcome drinks and traditional family platter upon arrival.', 4),
            _inc_included('Complimentary Experiences: Guided nature trails in Landour and VIP seating slots for Ganga Aarti.', 5),
            _inc_included('Exclusive Assistance: 24/7 dedicated TRAGUIN Support and professional local expertise.', 6),
            _inc_included('Taxes: All applicable state luxury taxes, toll fees, fuel charges, and driver allowances.', 7),
            _inc_excluded('Airfare / Rail Tickets: Domestic or international flights to/from Dehradun.', 8),
            _inc_excluded('Monuments & Entry Fees: Tickets for historical monuments, Beatles Ashram entry, or cable car tickets.', 9),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, alcoholic beverages, and mini-bar consumption.', 10),
            _inc_excluded('Optional Adventure Activities: Professional river rafting, zip-lining, or specialized trekking guides.', 11),
            _inc_excluded('Travel Insurance: Comprehensive health or trip cancellation insurance policies.', 12),
        ],
    )
    return package, itinerary

def build_uk_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UK-013'
    tour_code = 'TR-UK-FAM13'
    title = 'Ranikhet • Almora • Kausani Peaceful Escape'
    duration = '05 Nights / 06 Days'
    slug = 'uk-013-ranikhet-almora-kausani-peaceful-escape'
    itin_slug = 'uk-013-ranikhet-almora-kausani-peaceful-escape-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Uttarakhand, India | Category: Family Peaceful Escape', 2),
            _ph('Destinations: Ranikhet, Almora, Kausani', 3),
            _ph('Ideal for: Families, Leisure Seekers, Nature Lovers', 4),
            _ph('Best season: October to June', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle & Meals: Private Luxury SUV (Innova Crysta) | Modified American Plan (Breakfast & Dinner)', 7),
            _ph('Route: Kathgodam – Ranikhet – Kausani – Almora – Kathgodam', 8),
            _ph('TRAGUIN Curated Experience Note: Enjoy smooth hill transfers with experienced terrain drivers, premium boutique resort stays offering panoramic mountain views, specialized slow-travel pacing for family relaxation, and dedicated local support.', 9),
            _ph('TRAGUIN Signature Experience: A private family sunset high-tea arranged overlooking the Himalayan valleys.', 10),
            _ph('Curated by TRAGUIN Experts: Slow-travel paths avoiding sharp stress points, optimized for family comfort.', 11),
            _ph('Personalized Assistance: Transparent digital trip management with real-time route coordinators.', 12),
            _ph('Premium Handpicked Hotels: Elite properties offering excellent family suites, exceptional safety, and scenic views.', 13),
            _ph('Luxury Transportation: Highly verified mountain drivers ensuring smooth and comfortable road transits.', 14),
            _ph('Shopping & Local Experiences: Famous Shopping Items: Buy genuine Kausani handwoven woolen shawls and organic high-altitude green teas. Local Souvenirs: Traditional Kumaoni Bal Mithai and rhododendron juice. Instagram & Family Spots: Wide panoramic terraces at Kausani and the monumental ancient deodar shadow temples at Jageshwar.', 15),
            _ph('Important Notes: Hotel Policies: Resort check-in begins at 13:00 hrs; check-out is at 11:00 hrs. Room configuration changes depend strictly on seasonal availability. Weather Notes: Summer offers cool breezy days (15°C to 25°C); winters bring crisp cold weather perfect for heavy snow viewpoints. Transport Rules: Our premium vehicles strictly follow safety regulations; mountain driving is limited to daylight hours for safety. Advance Booking Suggestions: Best Time to Visit Uttarakhand mountain ranges sees heavy demand; advance bookings guarantee peak-facing luxury suites.', 16),
        ],
        moods=['Family', 'Nature', 'Peaceful', 'Hills'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request',
        rating=Decimal("4.9"), review_count=0,
        tagline='Ranikhet • Almora • Kausani Peaceful Escape • 05 Nights / 06 Days',
        overview=('Escape into the serene, untouched green valleys of Kumaon with our specially curated Luxury Uttarakhand Holiday. Tailored perfectly for family bonding, this journey avoids commercial rush, leading you straight into majestic pine forests, historical heritage temples, and quiet meadows. From the deep mist-covered forests of Ranikhet and the cultural treasures of Almora to the panoramic snow-clad Himalayan ranges of Kausani, this Premium Uttarakhand Experience by TRAGUIN promises breathtaking landscapes, premium stays, and unforgettable memories for your entire family.\n\nTOUR OVERVIEW\nTravel Dates: Bespoke / Customizable FIT\nMeal Plan: Modified American Plan (Breakfast & Dinner)\nVehicle: Private Luxury SUV (Innova Crysta)\nRoute: Kathgodam – Ranikhet – Kausani – Almora – Kathgodam\n\nTRAGUIN Curated Experience Note: Enjoy smooth hill transfers with experienced terrain drivers, premium boutique resort stays offering panoramic mountain views, specialized slow-travel pacing for family relaxation, and dedicated local support.\n\nWhy Visit Uttarakhand\'s Kumaon Hills? Far away from overly commercialized hill stations, the peaceful triangle of Ranikhet, Almora, and Kausani offers a breath of clean mountain air, pristine oak-pine woodlands, and panoramic sights of high Himalayan ranges including Nanda Devi and Trishul peaks.\n\nFamous Attractions & Most Searched Experiences: The highlights include the rolling green meadows of Ranikhet Golf Course, the grand historical Katarmal Sun Temple, the Anasakti Ashram in Kausani (where Mahatma Gandhi stayed), and the ancient spiritual complex of Jageshwar Dham near Almora.'),
        seo_title='UK-013 | Ranikhet Almora Kausani Peaceful Escape | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Uttarakhand package (UK-013 / TR-UK-FAM13): Ranikhet, Kausani, Almora, Jageshwar Dham, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Upat Golf Course, Chaubatia Orchards, Jhula Devi Temple, and Ranikhet pine forests', 1),
            _ih('Katarmal Sun Temple, Kausani viewpoints, Anasakti Ashram, and tea garden walks', 2),
            _ih('Jageshwar Dham temple complex, Deodar Forest Sanctuary, and Almora heritage market', 3),
            _ih('TRAGUIN Signature Experience: Private family sunset high-tea overlooking Himalayan valleys', 4),
            _ih('4-tier handpicked accommodation across Ranikhet and Kausani with Almora boutique stay', 5),
        ],
        days=[
            _day(1, 'KATHGODAM TO RANIKHET – HILLS OF THE QUEEN', ('Your family\'s mountain getaway begins with a refreshing morning arrival at Kathgodam railway station or corporate pick-up point. Meet your expert terrain chauffeur and step inside your premium private vehicle for a scenic, smooth upward drive to Ranikhet—popularly known as the Queen\'s Meadow. The winding route introduces your family to breathtaking landscapes and majestic pine forests. Upon check-in at your handpicked boutique luxury resort, take the afternoon to unwind and breathe in the crisp mountain air. In the evening, take a gentle family walk down Mall Road or relax inside the manicured lawns of your premium stay.'), [
                'Sightseeing Included: Scenic hillside drive, scenic photography viewpoints.',
                'Evening Experience: Welcome high-tea with sunset view over valleys.',
                'Overnight Stay: Ranikhet (Premium Handpicked Resort).',
                'Meals Included: Welcome Dinner.',
            ]),
            _day(2, 'RANIKHET SIGHTSEEING – ORCHARDS, MEADOWS & HERITAGE', ('Savor a hearty breakfast looking out at the mist-kissed hills. Today, discover the top attractions of this military hill station. Visit the expansive Upat Army Golf Course, one of the highest 9-hole golf courses in Asia, offering rolling green turfs perfect for a beautiful family photograph. Move forward to the serene Chaubatia Orchards, famous for apple, peach, and plum plantations, framed by views of the Himalayan peaks. Later, explore the spiritual tranquility of Jhula Devi Temple, known for thousands of copper bells tied by wishes over centuries. Spend your evening gathering together to enjoy local Kumaoni cuisine and stories.'), [
                'Sightseeing Included: Upat Golf Course, Chaubatia Orchards, Jhula Devi Temple.',
                'Local Experiences: Interaction with local fruit growers and walking in pine forests.',
                'Overnight Stay: Ranikhet.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(3, 'RANIKHET TO KAUSANI – DRIVING TO THE SWITZERLAND OF INDIA', ('After a refreshing breakfast, journey deeper into the tranquil heart of the hills towards Kausani. En route, stop at the mesmerizing Katarmal Sun Temple near Almora, an architectural heritage site from the 9th century boasting exquisite stone carvings. Continue your drive to Kausani, a peaceful village famously called the Switzerland of India by Mahatma Gandhi due to its stunning natural beauty. Check-in at your luxury mountain-view resort, uniquely positioned to offer an uninterrupted look at the snow peaks. Witness a dramatic, deep-orange sunset striking across Nanda Devi, Trishul, and Panchachuli ranges right from your balcony.'), [
                'Sightseeing Included: Katarmal Sun Temple, Kausani viewpoints.',
                'Evening Experience: Private family bonfire with acoustic music or stargazing.',
                'Overnight Stay: Kausani (Luxury Valley-Facing Resort).',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(4, 'KAUSANI SIGHTSEEING – TEA GARDENS & PHILOSOPHICAL RETREATS', ('Wake up early to catch a breathtaking mountain sunrise that paints the entire snow range in pink and gold. After breakfast, visit the peaceful Anasakti Ashram, where Mahatma Gandhi spent time writing his commentaries on Gita, filled with rare historical photographs and deep silence. Next, take a leisurely, immersive walk through the rolling green terraces of the Kausani Tea Estate, sampling fresh orthodox hill teas. Later, visit the traditional Shawl Weaving Center to see local artisans keeping Kumaon\'s heritage alive, making it an educational and culturally enriching experience for children and adults alike.'), [
                'Sightseeing Included: Anasakti Ashram, Kausani Tea Garden, Local Weaving Center.',
                'Optional Activities: Tea tasting session and picking organic estate leaves.',
                'Overnight Stay: Kausani.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(5, 'KAUSANI TO ALMORA VIA JAGESHWAR DHAM – ANCIENT SPIRITUALITY', ('Depart Kausani after breakfast and drive down through scenic, slow paths towards the cultural capital of Kumaon—Almora. Today features an exclusive excursion to Jageshwar Dham, a sacred cluster of over 125 ancient stone temples tucked deeply inside a dense forest of giant Deodar trees. The sheer quietness and ancient stone symmetry create an unforgettable atmosphere. Later, check into your boutique resort in Almora. Spend the evening enjoying the peaceful mountain property, reflecting on the wonderful memories shared during this Best Uttarakhand Family Tour.'), [
                'Sightseeing Included: Jageshwar Dham Temple Complex, Deodar Forest Sanctuary.',
                'Evening Experience: Traditional Kumaoni farewell dinner hosted by the resort.',
                'Overnight Stay: Almora (Boutique Heritage Resort).',
                'Meals Included: Breakfast & Farewell Dinner.',
            ]),
            _day(6, 'ALMORA TO KATHGODAM – DEPARTURE WITH CHERISHED MEMORIES', ('Savor your last morning breakfast facing the mist-filled valley. Pack your bags at a very relaxed pace. Before heading down the hills, make a brief stop at the traditional Almora bazaar to purchase local sweets and handicrafts. Your private luxury vehicle will then smoothly transfer your family back to Kathgodam railway station or airport for your journey onward. Your Luxury Uttarakhand Holiday concludes, leaving your family with refreshed minds and bondings forged amidst nature.'), [
                'Sightseeing Included: Almora local heritage market walk, assisted departure transfer.',
                'Meals Included: Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Woodsvilla Resort', 'Ranikhet', '02 Nights', 'Deluxe', 'Pine View Deluxe Room', 'MAP (Breakfast & Dinner)', 4, 1, description='OPTION 01 – DELUXE: Woodsvilla Resort, Ranikhet (02 Nights)'),
            _hotel('Krishna Mountview Resort', 'Kausani', '02 Nights', 'Deluxe', 'Executive Room', 'MAP (Breakfast & Dinner)', 4, 2, description='OPTION 01 – DELUXE: Krishna Mountview Resort, Kausani (02 Nights)'),
            _hotel('Chevron Rosemount', 'Ranikhet', '02 Nights', 'Premium', 'Premium Heritage Room', 'MAP (Breakfast & Dinner)', 4, 3, description='OPTION 02 – PREMIUM: Chevron Rosemount, Ranikhet (02 Nights)'),
            _hotel('Sun n Snow Inn', 'Kausani', '02 Nights', 'Premium', 'Himalayan View Room', 'MAP (Breakfast & Dinner)', 4, 4, description='OPTION 02 – PREMIUM: Sun n Snow Inn, Kausani (02 Nights)'),
            _hotel("WelcomHeritage Ashoka's Tiger Trail", 'Ranikhet', '02 Nights', 'Luxury', 'Luxury Club Room', 'MAP (Breakfast & Dinner)', 5, 5, description="OPTION 03 – LUXURY: WelcomHeritage Ashoka's Tiger Trail, Ranikhet (02 Nights)"),
            _hotel('The Heritage Resort', 'Kausani', '02 Nights', 'Luxury', 'Super Deluxe Himalayan Facing', 'MAP (Breakfast & Dinner)', 5, 6, description='OPTION 03 – LUXURY: The Heritage Resort, Kausani (02 Nights)'),
            _hotel('10 Nautical Miles', 'Ranikhet', '02 Nights', 'Ultra Luxury', 'Mountain Cottage', 'MAP (Breakfast & Dinner)', 5, 7, description='OPTION 04 – ULTRA LUXURY: 10 Nautical Miles, Ranikhet (02 Nights)'),
            _hotel('The Buransh Luxury Wellness Resort', 'Kausani', '02 Nights', 'Ultra Luxury', 'Luxury Panorama Suite', 'MAP (Breakfast & Dinner)', 5, 8, description='OPTION 04 – ULTRA LUXURY: The Buransh Luxury Wellness Resort, Kausani (02 Nights)'),
        ],
        inclusions=[
            _inc_included('Accommodation: 05 Nights luxury stay in handpicked, family-centric premium resorts.', 1),
            _inc_included('Meals: Daily multi-cuisine buffet breakfasts and multi-course curated dinners at all resorts.', 2),
            _inc_included('Transfers: All transfers, sightseeing tours, and inter-city hill travels via private, luxury Innova Crysta.', 3),
            _inc_included('Sightseeing: Complete curated sightseeing tours as detailed in the daily family itinerary.', 4),
            _inc_included('Assistance: Personalized 24/7 dedicated remote support from TRAGUIN experts.', 5),
            _inc_included('Welcome Amenities: Refreshing non-alcoholic welcome drinks, fresh mineral water, and mountain travel essential kit.', 6),
            _inc_included('Complimentary Experiences: Private family evening bonfire session and custom tea-estate entry clearance.', 7),
            _inc_included('Support: Toll taxes, parking charges, fuel fees, and driver allowances fully handled under TRAGUIN support.', 8),
            _inc_excluded('Flight or train ticket reservations to and from Kathgodam.', 9),
            _inc_excluded('Monument entry tickets, camera permissions, or historic site guide fees.', 10),
            _inc_excluded('Personal expenses like laundry, room service, telephone calls, and traditional tips.', 11),
            _inc_excluded('Any adventure activity or sports fees not detailed in the itinerary.', 12),
            _inc_excluded('Insurance coverage policies and extra lunch arrangements.', 13),
        ],
    )
    return package, itinerary

def build_uk_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UK-014'
    tour_code = 'TR-UK-BR04-V2'
    title = 'Binsar Wildlife Sanctuary • Kasar Devi Retreat'
    duration = '04 Nights / 05 Days'
    slug = 'uk-014-binsar-wildlife-kasar-devi-retreat'
    itin_slug = 'uk-014-binsar-wildlife-kasar-devi-retreat-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Uttarakhand, India | Category: Luxury Family Wilderness Retreat', 2),
            _ph('Destinations: Kathgodam, Binsar Wildlife Sanctuary, Almora Vistas', 3),
            _ph('Ideal for: Families, Nature Enthusiasts, Peace Seekers', 4),
            _ph('Best season: October to June', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle & Meals: Private Luxury Dedicated SUV (Innova Crysta) | Modified American Plan (Breakfast & Dinner)', 7),
            _ph('Route: Kathgodam – Binsar Wildlife Sanctuary – Almora Surroundings – Kathgodam', 8),
            _ph('TRAGUIN Curated Experience Note: This exclusive wilderness package is precision-curated by TRAGUIN specialists to ensure total family relaxation. Features low-fatigue mountain tracks, deep private forest treks accompanied by naturalists, and exceptional peak-viewing cottage selections.', 9),
            _ph('TRAGUIN Signature Experience: Private, naturalist-led mountain trek tailored perfectly for family comfort levels.', 10),
            _ph('Curated by TRAGUIN Experts: Balanced mountain road mapping with ample relaxation periods.', 11),
            _ph('Personalized Assistance: Immediate driver availability and coordinated luggage handling throughout transit gates.', 12),
            _ph('Premium Handpicked Hotels: Properties specifically chosen to maximize high-altitude snow views and peace.', 13),
            _ph('Luxury Transportation: Reliable, top-tier vehicles driven by hill-certified, courteous professional chauffeurs.', 14),
            _ph('Shopping & Local Experiences: Almora Heritage Bazaars for Bal Mithai and hand-beaten copperware. Panchachuli Weavers Center for handspun wool stoles, premium pashminas, and organic Kumaon teas. Instagram Spots: Towering deodar background at Jageshwar and majestic morning peak lines from the resort terrace.', 15),
            _ph('Important Notes: Hotel Policies: Standard check-in window opens at 14:00 hrs and check-out completes by 11:00 hrs. Room types are based on availability. Weather Notes: The Best Time to Visit Uttarakhand hills is October to June, but forest nights turn chilly; bring light woolens. Transport Rules: Private vehicles are permitted up to dedicated sanctuary borders; inner forest transits follow wildlife department protocols. Advance Booking Suggestions: Elite wilderness eco-lodges hold very limited counts; booking early is strongly advised for peak dates.', 16),
        ],
        moods=['Family', 'Wildlife', 'Nature', 'Retreat'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request',
        rating=Decimal("4.9"), review_count=0,
        tagline='Binsar Wildlife Sanctuary • Kasar Devi Retreat • 04 Nights / 05 Days',
        overview=('Escape into the serene alpine wilderness of the Kumaon Himalayas. Our Luxury Uttarakhand Holiday introduces your family to the untouched beauty of Binsar. Uniquely customized as the ultimate Uttarakhand Family Tour, this exclusive retreat provides breathtaking landscapes, sweeping mountain views, and absolute isolation from city chaos. With TRAGUIN Uttarakhand Packages, experience custom handpicked hotels, refined luxury transportation, and curated experiences that build unforgettable memories for generations.\n\nTOUR OVERVIEW\nTravel Dates: Flexible / Custom FIT\nMeal Plan: Modified American Plan (Breakfast & Dinner)\nVehicle: Private Luxury Dedicated SUV (Innova Crysta)\nRoute: Kathgodam – Binsar Wildlife Sanctuary – Almora Surroundings – Kathgodam\n\nTRAGUIN Curated Experience Note: This exclusive wilderness package is precision-curated by TRAGUIN specialists to ensure total family relaxation. Features low-fatigue mountain tracks, deep private forest treks accompanied by naturalists, and exceptional peak-viewing cottage selections.\n\nWhy Visit Binsar Wilderness? Rising amidst towering oak and rhododendron woodlands, the sanctuary zone stands out as a sanctuary of absolute tranquility. Choosing a Premium Uttarakhand Experience ensures your family gets to realign with untouched forest ecologies and spectacular, unobstructed Himalayan horizons.\n\nFamous Attractions & Most Searched Experiences: The signature crown is the legendary Zero Point, presenting an unmatched 360-degree panorama of majestic peaks like Nanda Devi, Trishul, and Shivling. Families actively search for bird-watching expeditions, old stone temple journeys, and calm forest glades.'),
        seo_title='UK-014 | Binsar Wildlife Sanctuary Kasar Devi Retreat | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Uttarakhand package (UK-014 / TR-UK-BR04-V2): Binsar Zero Point trek, Jageshwar Dham, Kasar Devi, and 4-tier wilderness accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Guided Zero Point Nature Trail with 360-degree Himalayan panorama in Binsar Wildlife Sanctuary', 1),
            _ih('Jageshwar Dham ancient temple complex and sacred cedar forest walk', 2),
            _ih('Kasar Devi geomagnetic ridge, Crank\'s Ridge, and Almora cultural experiences', 3),
            _ih('TRAGUIN Signature Experience: Private naturalist-led mountain trek for family comfort levels', 4),
            _ih('4-tier handpicked wilderness accommodation in Binsar (04 Nights)', 5),
        ],
        days=[
            _day(1, 'KATHGODAM TO BINSAR WILDERNESS – ASCENT INTO PARADISE', ('Your exceptional mountain retreat begins with a personalized pickup by your private luxury vehicle at Kathgodam railway station. Ascend gently into the pristine Kumaon hills along winding, beautiful mountain routes flanked by whispering pine woods. Pause along your scenic path to capture stunning family portraits with deep green valleys in the background. Arrive at your handpicked resort bordering the sanctuary, where a traditional mountain welcome waits. Relax in your premium room and enjoy a peaceful evening watching the sun slide behind the vast ridge lines.'), [
                'Sightseeing Included: Scenic mountain valley drive, panoramic valley photo points.',
                'Evening Experience: Cozy family bonfire circle with a dedicated briefing on Binsar\'s flora and fauna.',
                'Overnight Stay: Binsar (Handpicked Premium Wilderness Resort).',
                'Meals Included: Welcome Dinner.',
            ]),
            _day(2, 'ZERO POINT TREK – THE GRAND HIMALAYAN AMBIENCE', ('Wake up to the crisp mountain breeze and a glorious golden sunrise illuminating the great snow wall. Following a relaxed breakfast, start your family-friendly forest trek towards Zero Point within the heart of Binsar Wildlife Sanctuary. Guided by a professional local naturalist, walk effortlessly under beautiful canopies while observing colorful alpine birds. Upon reaching the summit, look out over an incredible 360-degree sweep of Nanda Devi and Trishul peaks. In the afternoon, visit the sanctuary heritage center before a premium outdoor picnic lunch arranged amidst nature.'), [
                'Sightseeing Included: Guided Zero Point Nature Trail, Wildlife Sanctuary Exhibit.',
                'Optional Activities: Specialized high-resolution binocular bird-spotting session.',
                'Evening Experience: Premium high-tea service accompanied by traditional Kumaoni flute melodies.',
                'Overnight Stay: Binsar.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(3, 'HERITAGE TOUR TO JAGESHWAR DHAM – ANCIENT CEDAR SOULS', ('Today features a beautiful driving excursion to Jageshwar Dham, a spectacular cluster of over 100 ancient stone temples tucked away inside deep, towering deodar forests. Walk down flat, accessible stone pathways while marveling at the 7th-century rock architecture and peaceful spiritual energy. Your private driver will guide you along a quiet rural route back, stopping at authentic Kumaoni hamlets where your family can comfortably observe old-world mountain customs and local organic farming.'), [
                'Sightseeing Included: Jageshwar Temple Complex, sacred cedar forest walk.',
                'Local Experiences: Traditional organic lunch served at an authentic local mountain home.',
                'Overnight Stay: Binsar.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(4, 'KASAR DEVI GEOMAGNETIC RIDGE & ALMORA CULTURAL EXPERIENCES', ('After breakfast, enjoy a brief drive to the unique ridge-town of Almora. Discover the world-famous Kasar Devi Temple, universally renowned for its extraordinary geomagnetic energy fields and meditative calm that has drawn world scholars for generations. Walk down the accessible pathways of Crank\'s Ridge, soaking in beautiful mountain views. In the afternoon, return to your resort property for a relaxed family time, allowing children and elders to fully enjoy the boutique indoor facilities or take a peaceful stroll within the private estate woods.'), [
                'Sightseeing Included: Kasar Devi Sanctuary Shrine, panoramic ridge lookouts.',
                'Evening Experience: Exclusive signature family farewell dinner showcasing local mountain delicacies.',
                'Overnight Stay: Binsar.',
                'Meals Included: Breakfast & Farewell Dinner.',
            ]),
            _day(5, 'BINSAR TO KATHGODAM – FAREWELL TO THE HIMALAYAS', ('Savor your final morning breakfast looking out at the majestic mountain expanses. Capture a few last family snapshots with the snowy peaks as a backdrop. At the designated hour, enjoy a comfortable packing pace before boarding your private luxury SUV for the smooth down-hill transfer back to Kathgodam. Your dedicated driver ensures you reach the railway station or transit point seamlessly, wrapping up a perfectly managed Luxury Uttarakhand Holiday with TRAGUIN care.'), [
                'Sightseeing Included: Assisted return valley transfer, local spice market stops.',
                'Meals Included: Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Club Mahindra Binsar Valley', 'Binsar', '04 Nights', 'Deluxe', 'Family Studio Room', 'MAP (Breakfast & Dinner)', 4, 1, description='OPTION 01 – DELUXE: Club Mahindra Binsar Valley | Family Studio Room (04 Nights)'),
            _hotel('The Kumaon, Binsar Road', 'Binsar', '04 Nights', 'Premium', 'Vista Luxury Chalet', 'MAP (Breakfast & Dinner)', 4, 2, description='OPTION 02 – PREMIUM: The Kumaon, Binsar Road | Vista Luxury Chalet (04 Nights)'),
            _hotel('Grand Oak Manor, Binsar Heritage', 'Binsar', '04 Nights', 'Luxury', 'Preferred Premium Suite', 'MAP (Breakfast & Dinner)', 5, 3, description='OPTION 03 – LUXURY: Grand Oak Manor, Binsar Heritage | Preferred Premium Suite (04 Nights)'),
            _hotel('Mary Budden Estate, Binsar Sanctuary', 'Binsar', '04 Nights', 'Ultra Luxury', 'Exclusive Private Luxury Cottage', 'MAP (Breakfast & Dinner)', 5, 4, description='OPTION 04 – ULTRA LUXURY: Mary Budden Estate, Binsar Sanctuary | Exclusive Private Luxury Cottage (04 Nights)'),
        ],
        inclusions=[
            _inc_included('Accommodation: 04 Nights stay in premium, handpicked wilderness properties optimized for families.', 1),
            _inc_included('Meals: Daily gourmet breakfasts and grand buffet dinners inside resort premises.', 2),
            _inc_included('Transfers: Dedicated private luxury SUV (Innova Crysta) for all transits and sightseeing.', 3),
            _inc_included('Sightseeing: Complete curated itinerary excursions as described day-by-day.', 4),
            _inc_included('Assistance: 24/7 remote operational oversight from dedicated destination specialists.', 5),
            _inc_included('Welcome Amenities: Himalayan mineral water bottles, fresh fruit baskets, and organic dry fruits in-car.', 6),
            _inc_included('Complimentary Experiences: Private naturalist-guided trek to Zero Point and an exclusive evening family bonfire circle.', 7),
            _inc_included('TRAGUIN Support: Priority care desk response throughout your vacation.', 8),
            _inc_excluded('Flight or railway train bookings reaching Kathgodam / Pantnagar.', 9),
            _inc_excluded('Binsar Sanctuary direct wildlife entry taxes, vehicle toll tokens, or camera charges.', 10),
            _inc_excluded('Personal expenditures like premium laundry, phone call tariffs, room service, or tips.', 11),
            _inc_excluded('Optional mountain adventure options or custom sports.', 12),
        ],
    )
    return package, itinerary

def build_uk_015(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UK-015'
    tour_code = 'TR-UK-LK06'
    title = 'Nainital • Bhimtal • Sattal • Mukteshwar Vistas'
    duration = '06 Nights / 07 Days'
    slug = 'uk-015-nainital-bhimtal-sattal-mukteshwar-vistas'
    itin_slug = 'uk-015-nainital-bhimtal-sattal-mukteshwar-vistas-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Uttarakhand, India | Category: Luxury Leisure Lakes & Hills Tour', 2),
            _ph('Destinations: Nainital, Bhimtal, Sattal, Naukuchiatal, Mukteshwar', 3),
            _ph('Ideal for: Families, Couples, Leisure Travelers', 4),
            _ph('Best season: March to June & October to January', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle & Meals: Dedicated Luxury SUV (Innova Crysta) | Modified American Plan (Breakfast & Dinner)', 7),
            _ph('Route: Kathgodam – Nainital – Bhimtal & Lakes – Mukteshwar – Kathgodam', 8),
            _ph('TRAGUIN Curated Experience Note: This signature leisure itinerary offers an elegant, slow-paced holiday layout with premium lakefront accommodations, private shikara cruises, chauffeured high-ridge driving loops, and total dedicated ground hospitality from arrival to departure.', 9),
            _ph('TRAGUIN Signature Experience: Private, pre-booked lake cruises and customized ridge-view picnics away from standard crowds.', 10),
            _ph('Curated by TRAGUIN Experts: Flawlessly structured hill driving itineraries ensuring minimal travel fatigue.', 11),
            _ph('Personalized Assistance: Courteous luggage management and direct coordinator communication at every destination stop.', 12),
            _ph('Premium Handpicked Hotels: Properties chosen specifically for their superior views, fine hospitality, and premier location.', 13),
            _ph('Luxury Transportation: Reliable premium SUVs driven by safe, professional, and hill-certified drivers.', 14),
            _ph('Shopping & Local Experiences: Bara Bazar (Nainital) for premium home-crafted aromatic candles and pure cane artifacts. Kumaon Specialties: Organic fruit preserves from Ramgarh, fresh apple chutneys, and premium locally harvested organic teas. Instagram Spots: Majestic sunrise over the Trishul peak range from your Mukteshwar balcony.', 15),
            _ph('Important Notes: Hotel Policies: Check-in open from 14:00 hrs and check-out settles by 11:00 hrs. Room upgrades are subject to resort availability. Weather Notes: The Best Time to Visit Uttarakhand lake region is summer for mild air, or late autumn for sharp, completely clear snow peaks. Transport Rules: Private tourist vehicles have designated entry windows along certain Mall Roads; your driver will manage schedules smoothly. Advance Booking Suggestions: Elite lake-facing suites fill up months in advance; early confirmation is highly advised for peak seasons.', 16),
        ],
        moods=['Family', 'Luxury', 'Lakes', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request',
        rating=Decimal("4.9"), review_count=0,
        tagline='Nainital • Bhimtal • Sattal • Mukteshwar Vistas • 06 Nights / 07 Days',
        overview=('Immerse yourself in the poetic charm of the Kumaon lake district. Our Luxury Uttarakhand Holiday delivers a flawlessly curated exploration of glassy alpine lakes and dramatic orchard ridges. As the definitive Best Uttarakhand Tour Package, this itinerary seamlessly weaves breathtaking landscapes, high-altitude serenity, and unmatched personal care. Let TRAGUIN indulge your senses with premium stays, handpicked hotels, and elite private transport that elevate this leisure mountain holiday into a series of truly unforgettable memories.\n\nTOUR OVERVIEW\nTravel Dates: Flexible / Customized FIT\nMeal Plan: Modified American Plan (Breakfast & Dinner)\nVehicle: Dedicated Luxury SUV (Innova Crysta)\nRoute: Kathgodam – Nainital – Bhimtal & Lakes – Mukteshwar – Kathgodam\n\nTRAGUIN Curated Experience Note: This signature leisure itinerary offers an elegant, slow-paced holiday layout with premium lakefront accommodations, private shikara cruises, chauffeured high-ridge driving loops, and total dedicated ground hospitality from arrival to departure.\n\nWhy Visit Kumaon Lakes & Hills? The lake region of Uttarakhand provides a refreshing alternative to traditional mountain touring, balancing quiet water retreats with crisp pine-scented high altitudes. A Premium Uttarakhand Experience here allows you to rest beside pristine water sheets before winding up to orchards presenting unbroken views of India\'s highest peaks.\n\nFamous Attractions & Most Searched Experiences: The essential milestones center on the beautiful crescent-shaped Naini Lake, the emerald waters of Bhimtal, the mystical forest-enclosed Sattal, the seven-cornered Naukuchiatal, and the historic clifftops of Mukteshwar Dham.'),
        seo_title='UK-015 | Nainital Bhimtal Sattal Mukteshwar Vistas | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Uttarakhand package (UK-015 / TR-UK-LK06): Nainital, Bhimtal, Sattal, Mukteshwar lake district tour with 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Naina Devi Temple, aerial ropeway to Snow View Point, and private Shikara cruise on Naini Lake', 1),
            _ih('Sattal forest loop, Naukuchiatal, Bhimtal island aquarium, and lakeside bonfire lounge', 2),
            _ih('Mukteshwar Dham Temple, Chauli Ki Jali cliffs, IVRI campus paths, and organic farm visits', 3),
            _ih('TRAGUIN Signature Experience: Private pre-booked lake cruises and customized ridge-view picnics', 4),
            _ih('4-tier handpicked accommodation: Nainital (02N) + Bhimtal (01N) + Mukteshwar (03N)', 5),
        ],
        days=[
            _day(1, 'KATHGODAM TO NAINITAL – WELCOME TO THE LAKE CITY', ('Your exceptional mountain holiday opens with an elite pickup by your private luxury vehicle at Kathgodam. Ascend effortlessly through green, winding mountain valleys into the refreshing air of the lower Himalayas. Arrive at Nainital, the timeless jewel town positioned around the mystical pear-shaped Naini Lake. Check into your premium handpicked hotel offering spectacular viewpoints. Spend your evening taking a relaxed stroll along the elegant, paved Mall Road, watching the town lights twinkle across the dark lake water.'), [
                'Sightseeing Included: Scenic valley drive, Mall Road walking exploration.',
                'Evening Experience: A relaxing welcome cocktail session looking over the lake mist.',
                'Overnight Stay: Nainital (Premium Lakefront Handpicked Hotel).',
                'Meals Included: Luxury Welcome Dinner.',
            ]),
            _day(2, 'NAINITAL SIGHTSEEING – CULTURAL GEMS & HIGH RIDGE ASCENT', ('After a delightful premium breakfast spread, visit the iconic Naina Devi Temple situated gracefully on the northern edge of the lake water. Following this, experience an effortless aerial ropeway cruise ascending to Snow View Point, providing an incredible panorama of the snow-crowned Himalayan crest. In the afternoon, enjoy a private, traditional Shikara boat cruise across Naini Lake, gliding past historic colonial-era boat clubs. Conclude your day with a relaxed drive to the high-elevation Eco Cave Gardens or choose to rest inside your luxury suite.'), [
                'Sightseeing Included: Naina Devi Temple, Aerial Ropeway ride, Private Shikara Lake Cruise.',
                'Optional Activities: High-altitude horse-trail riding up to the scenic Tiffin Top viewpoint.',
                'Evening Experience: Fine-dining lakeside experience featuring traditional continental cuisines.',
                'Overnight Stay: Nainital.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(3, 'LAKE DISTRICT EXCURSION – SATAL, NAUKUCHIATAL & BHIMTAL', ('Leave Nainital behind for a smooth driving loop across the serene lake network of Kumaon. Your first stop is Sattal, an extraordinary group of seven interconnected freshwater lakes surrounded by deep, green oak and pine forests. Next, proceed to Naukuchiatal, the deep lake of nine corners, where your family can enjoy absolute tranquility away from commercial noise. Arrive by afternoon at the peaceful town of Bhimtal. Check into your luxury resort and enjoy a private boat ride out to the unique aquarium islet located in the center of Bhimtal lake.'), [
                'Sightseeing Included: Sattal Forest Loop, Naukuchiatal, Bhimtal Island & Aquarium.',
                'Evening Experience: Lakeside bonfire lounge accompanied by light classical guitar tunes.',
                'Overnight Stay: Bhimtal (Exclusive Premium Lakefront Resort).',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(4, 'BHIMTAL TO MUKTESHWAR – ASCENDING TO THE FRUIT ORCHARD RIDGES', ('Savor a beautiful breakfast looking over the lake before embarking on a beautiful mountain drive up toward Mukteshwar, a tranquil town positioned high at 7,500 feet. The route winds through the famous fruit-growing belt of Ramgarh, presenting vast terraced orchards and endless views of mountain valleys. Upon arrival in Mukteshwar, check into your boutique ridge resort. Spend a completely peaceful afternoon reading on your private sundeck or wandering through adjacent pine forests as the mountain clouds roll past your feet.'), [
                'Sightseeing Included: Ramgarh orchard drive valleys, high-altitude ridge overview stops.',
                'Evening Experience: Tea session featuring freshly picked local rhododendron juices.',
                'Overnight Stay: Mukteshwar (Handpicked Luxury Boutique Ridge Resort).',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(5, 'MUKTESHWAR EXPLORATION – SACRED TEMPLES & CLIFF CHASMS', ('Dedicate your day to discovering the dramatic natural beauty of Mukteshwar. Visit the 350-year-old stone Mukteshwar Dham Temple, located at the highest point of the ridge, offering profound spiritual calm and sweeping views of Almora valley. Just behind the temple cliffs, witness Chauli Ki Jali – a breathtaking rock formation and vertical chasm that drops dramatically into the plains below, making it an extraordinary photography canvas. In the afternoon, take a relaxed guided walk through the expansive colonial-era campus of the Indian Veterinary Research Institute (IVRI), surrounded by pristine cedar woods.'), [
                'Sightseeing Included: Mukteshwar Dham Temple, Chauli Ki Jali Cliffs, historic IVRI campus paths.',
                'Optional Activities: Gentle rock-rappelling or zip-lining at the cliff edge under expert guidance.',
                'Evening Experience: Gourmet dinner experience hosted inside a wood-accented mountain greenhouse lounge.',
                'Overnight Stay: Mukteshwar.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(6, 'CHHIFI LEISURE HAMLET LOOP – HIDDEN VALLEY HARMONY', ('Enjoy an ease-filled morning before taking a private excursion down to the hidden mountain valley hamlets surrounding Mukteshwar. Drive through quiet, pristine woods down to peaceful mountain streams, observing the slow, beautiful traditional lifestyle of the Kumaon hills. Visit local organic farms producing premium mountain honey, fruit jams, and handmade woolen crafts. Return to your resort by late afternoon to relax and enjoy the final signature evening of your luxury trip.'), [
                'Sightseeing Included: Countryside valley drive, organic farm estate visit.',
                'Evening Experience: A special curated candle-lit farewell dinner celebrating your journey.',
                'Overnight Stay: Mukteshwar.',
                'Meals Included: Breakfast & Farewell Dinner.',
            ]),
            _day(7, 'MUKTESHWAR TO KATHGODAM – FAREWELL HIMALAYAS', ('Wake up early for a spectacular final glimpse of the sun rising over the snow-capped Himalayan peaks. Enjoy a long, relaxed breakfast at the resort before packing your bags comfortably. Board your private luxury SUV for a smooth return drive down to Kathgodam railway station or your next departure terminal. Your dedicated driver ensures a seamless drop, completing your elite Luxury Uttarakhand Holiday managed end-to-end with TRAGUIN professionalism.'), [
                'Sightseeing Included: Guided return transfer, en-route stops for choosing regional souvenirs.',
                'Meals Included: Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('The Manu Maharani (Nainital) / Fern Hillside (Bhimtal)', 'Nainital • Bhimtal • Mukteshwar', '06 Nights', 'Deluxe', 'Premium Luxury Room', 'MAP (Breakfast & Dinner)', 4, 1, description='OPTION 01 – DELUXE: The Manu Maharani (Nainital) / Fern Hillside (Bhimtal) | 02N Nainital • 01N Bhimtal • 03N Mukteshwar'),
            _hotel('Alka The Lake Side Hotel (Nainital) / Aamod Resort (Bhimtal)', 'Nainital • Bhimtal • Mukteshwar', '06 Nights', 'Premium', 'Executive Lake View Room', 'MAP (Breakfast & Dinner)', 4, 2, description='OPTION 02 – PREMIUM: Alka The Lake Side Hotel (Nainital) / Aamod Resort (Bhimtal) | 02N Nainital • 01N Bhimtal • 03N Mukteshwar'),
            _hotel('The Naini Retreat (Nainital) / The Fern Hillside Resort (Bhimtal)', 'Nainital • Bhimtal • Mukteshwar', '06 Nights', 'Luxury', 'Garden Suite / Lake View Luxury Suite', 'MAP (Breakfast & Dinner)', 5, 3, description='OPTION 03 – LUXURY: The Naini Retreat (Nainital) / The Fern Hillside Resort (Bhimtal) | 02N Nainital • 01N Bhimtal • 03N Mukteshwar'),
            _hotel('The Pavilion Heritage (Nainital) / Casa Dream The Resort (Mukteshwar)', 'Nainital • Bhimtal • Mukteshwar', '06 Nights', 'Ultra Luxury', 'Royal Heritage Suite / Presidential Ridge Suite', 'MAP (Breakfast & Dinner)', 5, 4, description='OPTION 04 – ULTRA LUXURY: The Pavilion Heritage (Nainital) / Casa Dream The Resort (Mukteshwar) | 02N Nainital • 01N Bhimtal • 03N Mukteshwar'),
        ],
        inclusions=[
            _inc_included('Accommodation: 06 Nights stay in premium, handpicked lakeside and ridgefront hotels.', 1),
            _inc_included('Meals: Daily multi-cuisine buffet breakfasts and premium curated dinners at the properties.', 2),
            _inc_included('Transfers: Complete ground transportation and sightseeing via an exclusive private luxury Innova Crysta SUV.', 3),
            _inc_included('Sightseeing: Complete guided tours matching the detailed day-wise itinerary.', 4),
            _inc_included('Assistance: 24/7 dedicated remote operational care from TRAGUIN travel experts.', 5),
            _inc_included('Welcome Amenities: Himalayan mineral water bottles, fresh fruit baskets, and premium local sweets on arrival.', 6),
            _inc_included('Complimentary Experiences: Private Shikara cruise on Naini Lake and an exclusive island boat ride in Bhimtal.', 7),
            _inc_included('TRAGUIN Support: Priority care logistics to ensure a completely smooth holiday.', 8),
            _inc_excluded('Domestic or international flights / train bookings to Kathgodam.', 9),
            _inc_excluded('Entry tickets to monuments, ropeway boarding tokens, or site guide fees.', 10),
            _inc_excluded('Personal expenditures like premium drinks, laundry, tipping, and room service.', 11),
            _inc_excluded('Optional adventure activities or specialized sports equipment rentals.', 12),
        ],
    )
    return package, itinerary

def build_uk_016(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UK-016'
    tour_code = 'TRG-UK-016'
    title = 'Premium Lansdowne Weekend Escape'
    duration = '02 Nights / 03 Days'
    slug = 'uk-016-premium-lansdowne-weekend-escape'
    itin_slug = 'uk-016-premium-lansdowne-weekend-escape-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Uttarakhand, India | Category: Leisure Escape', 2),
            _ph('Destinations: Lansdowne Weekend Sanctuary', 3),
            _ph('Ideal for: Couples, Families & Refined Travelers', 4),
            _ph('Best season: Year-Round Retreat', 5),
            _ph('Vehicle & Meals: Private Premium Sedan or Luxury SUV at disposal | Modified American Plan (Breakfast & Dinner Included)', 6),
            _ph('Route: Delhi / Dehradun Departure → Scenic Kotdwar Route → Lansdowne Pine Retreat → Return Journey', 7),
            _ph('TRAGUIN Curated Experience Note: Seamless luxury transport from your home doorstep, handpicked premium pine-view resort stays, private evening fireplace access, and premium personalized touring paths.', 8),
            _ph('Shopping & Local Experiences: Lansdowne colonial heritage markets and local Garhwali artisan crafts.', 9),
            _ph('Important Notes: Best Time to Visit Lansdowne is practically year-round, offering refreshing summers and cozy, misty winters. TRAGUIN Lansdowne Packages present a genuinely Luxury Lansdowne Holiday tailored around exclusive handpicked hotels and flawless mountain transit options.', 10),
        ],
        moods=['Weekend', 'Leisure', 'Family', 'Couples'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Class)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Best Lansdowne Tour Package • Premium Lansdowne Experience Weekend Escape • 02 Nights / 03 Days',
        overview=('Escape the mundane and venture into the peaceful, pristine oak and pine forests of the Garhwal Himalayas. TRAGUIN presents a uniquely refreshing weekend escape crafted meticulously to offer deep relaxation, breathtaking landscapes, and premium stays. Our curated experiences guarantee immersive hill-station exploration, giving you unforgettable memories.\n\nTOUR OVERVIEW\nTravel Month: Weekend Getaways Available Weekly\nGroup / FIT: Private Luxury FIT Getaway\nVehicle: Private Premium Sedan or Luxury SUV at disposal\nMeal Plan: Modified American Plan (Breakfast & Dinner Included)\nRoute: Delhi / Dehradun Departure → Scenic Kotdwar Route → Lansdowne Pine Retreat → Return Journey\n\nTRAGUIN Curated Experience Note: Seamless luxury transport from your home doorstep, handpicked premium pine-view resort stays, private evening fireplace access, and premium personalized touring paths.\n\nIf you are charting a quick mountain vacation, choosing the Best Lansdowne Tour Package or a dedicated Lansdowne Honeymoon Package guarantees a pristine environment devoid of overwhelming commercial crowds. Lansdowne retains a grand colonial layout, deep pine canopies, and beautiful vistas. This Lansdowne Family Tour introduces you directly to the Top Tourist Places in Lansdowne including the mirror-like Bhulla Tal Lake, the historical St. John\'s Church, and the unmatched sunrise viewpoint at Tip-In-Top.'),
        seo_title='UK-016 | Premium Lansdowne Weekend Escape | TRAGUIN',
        seo_description='Premium 02 Nights / 03 Days Uttarakhand package (UK-016 / TRG-UK-016): Lansdowne Bhulla Tal, Tip-In-Top, St. John\'s Church with Ultra Luxury and Premium accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Scenic Kotdwar ascent with Khoh River photography halts and valley overlooks', 1),
            _ih('Bhulla Tal Lake rowboat ride, Tip-In-Top Viewpoint, St. John\'s Church, and Garhwali Military Heritage Museum', 2),
            _ih('Private sunset observation tea session and exclusive cozy bonfire evening with artisan snacks', 3),
            _ih('TRAGUIN Curated Experience: Seamless luxury transport and handpicked premium pine-view resort stays', 4),
            _ih('2-tier handpicked accommodation: Ultra Luxury and Premium options in Lansdowne (02 Nights)', 5),
        ],
        days=[
            _day(1, 'SCENIC ASCENT TO LANSDOWNE SANCTUARY', ('Your premium holiday starts with a comfortable private pickup. Drive out through scenic roads transitioning quickly from bustling highways into the breathtaking landscapes of the Shivalik foothills. Climb the winding mountain paths past old historic outposts, arriving at your premium hill resort overlooking deep mist-filled valleys.'), [
                'Sightseeing Included: En-route photography halts along the Khoh River curves and valley overlooks.',
                'Evening Experience: Private sunset observation tea session organized on your resort\'s expansive wooden deck.',
                'Overnight Stay: Luxury Valley-View Resort in Lansdowne.',
                'Meals Included: Welcome Drink & Gourmet Buffet Dinner.',
            ]),
            _day(2, 'MISTY PINELANDS & COLONIAL HIGHLIGHTS', ('Wake up to the gentle chirping of birds and a panoramic mountain landscape. Today, explore Lansdowne\'s timeless historical attractions. Enjoy a gentle rowboat ride on Bhulla Tal Lake, admire the grand architecture of St. John\'s Church, and walk through pristine forest paths up to the dramatic Tip-In-Top ridge.'), [
                'Sightseeing Included: Bhulla Tal Lake, Tip-In-Top Viewpoint, St. John\'s Church, and the Garhwali Military Heritage Museum.',
                'Evening Experience: An exclusive private cozy bonfire evening paired with artisan snacks arranged by TRAGUIN.',
                'Overnight Stay: Handpicked Luxury Resort in Lansdowne.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(3, 'MOUNTAIN SERENITY & DEPARTURE RETURNING HOME', ('Gaze out over the glorious snow peaks one last time over a fresh breakfast. Enjoy a leisurely walk across the pine-sheltered paths around the resort property before joining your private chauffeur for a smooth, comfortable return drive back to your home station.'), [
                'Optional Activities: Guided morning forest walk and specialized local bird-watching session with an expert tracker.',
                'Meals Included: Artisan Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Vanaja Forest Resort / Blue Pine Resort', 'Lansdowne', '02 Nights', 'Ultra Luxury', 'Luxury Pine Cottage', 'Modified American Plan (Breakfast & Dinner)', 5, 1, description='OPTION 01 – ULTRA LUXURY: Vanaja Forest Resort / Blue Pine Resort | Luxury Pine Cottage (02 Nights)'),
            _hotel('Hotel Lans Castle', 'Lansdowne', '02 Nights', 'Premium', 'Executive Valley View Room', 'Modified American Plan (Breakfast & Dinner)', 4, 2, description='OPTION 02 – PREMIUM: Hotel Lans Castle | Executive Valley View Room (02 Nights)'),
        ],
        inclusions=[
            _inc_included('02 Nights stay in handpicked, high-end luxury resorts with valley views.', 1),
            _inc_included('Daily gourmet buffet breakfasts and elegant themed dinners at the resort restaurant.', 2),
            _inc_included('Complete private luxury transport and mountain sightseeing via dedicated premium sedan/SUV.', 3),
            _inc_included('Pre-arranged entry passes and complimentary rowboat tickets at Bhulla Tal Lake.', 4),
            _inc_included('TRAGUIN 24/7 dedicated remote concierge support during the travel route.', 5),
            _inc_excluded('Flight or railway train fares to the nearest base stations.', 6),
            _inc_excluded('Personal expenses such as laundry, telephone calls, or camera entry tokens.', 7),
        ],
    )
    return package, itinerary

def build_uk_017(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UK-017'
    tour_code = 'TRG-UK-017'
    title = 'Premium Jim Corbett Wild Wilderness Escape'
    duration = '02 Nights / 03 Days'
    slug = 'uk-017-premium-jim-corbett-wild-wilderness-escape'
    itin_slug = 'uk-017-premium-jim-corbett-wild-wilderness-escape-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Uttarakhand, India | Category: Nature & Wildlife', 2),
            _ph('Destinations: Jim Corbett National Park', 3),
            _ph('Ideal for: Wildlife Enthusiasts, Families & Couples', 4),
            _ph('Best season: November to May', 5),
            _ph('Vehicle & Meals: Dedicated Luxury AC Chauffeur Sedan/SUV for transfers & Private 4x4 open Gypsy for Safaris | Modified American Plan (All Artisan Breakfasts & Dinners Included)', 6),
            _ph('Route: Delhi / Dehradun Arrival → Scenic Ramnagar Drive → Corbett Wilderness Zone → Return Departure', 7),
            _ph('TRAGUIN Curated Experience Note: Pre-booked premium safari zones, personalized expert naturalist guidance, private riverside sundowner high-tea, and premium handpicked wilderness resort stays with deep comfort amenities.', 8),
            _ph('TRAGUIN Signature Experience: Private riverside sundowner high-tea experience with a personalized luxury setup.', 9),
            _ph('Curated by Experts: Guaranteed core safari zone allocations pre-registered through our premium network.', 10),
            _ph('Personalized Assistance: 24/7 dedicated remote guest relations desk to adjust scheduling dynamically.', 11),
            _ph('Shopping & Local Experiences: Local Souvenirs: Hand-painted wildlife art plates, organic wild honey, and authentic wooden jungle crafts at the Ramnagar local markets. Instagram Spots: Suspension bridge over the Kosi River, Garjiya Temple rock backdrop, and morning sun hitting the Sal forest canopy.', 12),
            _ph('Important Notes: Core jungle zone safari permits open strictly in advance; immediate booking is highly recommended to guarantee prime zones. Please carry valid government-issued photo identification copies matching safari booking documentation details. Muted or earth-toned clothing (khaki, olive green, brown) is highly recommended for core safari tracks.', 13),
        ],
        moods=['Wildlife', 'Luxury', 'Nature', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Class)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Best Jim Corbett Tour Package • Premium Jim Corbett Experience & Wild Wilderness Escape • 02 Nights / 03 Days',
        overview=('Welcome to the majestic wilderness of Uttarakhand. TRAGUIN invites you to embark on a thrilling, ultra-luxury wildlife expedition to Jim Corbett National Park. Experience immersive wilderness encounters, breathtaking landscapes, and premium stays tucked away in deep riverine forests. This exclusive Luxury Jim Corbett Holiday blends the raw thrill of the jungle with handpicked hotels and sophisticated personal comfort, promising unforgettable memories.\n\nTOUR OVERVIEW\nTravel Month: Customized Flexi-Dates Available\nGroup / FIT: Private Luxury Customized FIT Escape\nVehicle: Dedicated Luxury AC Chauffeur Sedan/SUV for transfers & Private 4x4 open Gypsy for Safaris\nMeal Plan: Modified American Plan (All Artisan Breakfasts & Dinners Included)\nRoute: Delhi / Dehradun Arrival → Scenic Ramnagar Drive → Corbett Wilderness Zone → Return Departure\n\nTRAGUIN Curated Experience Note: Pre-booked premium safari zones, personalized expert naturalist guidance, private riverside sundowner high-tea, and premium handpicked wilderness resort stays with deep comfort amenities.\n\nWhen shortlisting the perfect Best Jim Corbett Tour Package or a memorable Jim Corbett Honeymoon Package, discerning travelers select exclusive options that balance adrenaline-pumping game drives with peaceful relaxation. As a signature Jim Corbett Family Tour, this journey introduces you flawlessly to the Top Tourist Places in Jim Corbett, including the core safari blocks (Bijrani/Dhikala/Jhirna), the iconic Garjiya Devi Temple, and the pristine Kosi River pathways.'),
        seo_title='UK-017 | Premium Jim Corbett Wild Wilderness Escape | TRAGUIN',
        seo_description='Premium 02 Nights / 03 Days Uttarakhand package (UK-017 / TRG-UK-017): Jim Corbett core zone jeep safari, Garjiya Devi Temple, and 3-tier wilderness accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Garjiya Devi Temple on Kosi River boulder and private riverside sundowner high-tea', 1),
            _ih('Core Zone Morning Jeep Safari with expert naturalist tracking Royal Bengal Tiger and wildlife', 2),
            _ih('Corbett Waterfalls evening drive and curated open-air live barbecue dinner under starlit canopy', 3),
            _ih('TRAGUIN Signature Experience: Private riverside sundowner high-tea with personalized luxury setup', 4),
            _ih('3-tier handpicked wilderness accommodation in Jim Corbett (02 Nights)', 5),
        ],
        days=[
            _day(1, 'ARRIVAL & RIVERSIDE RESORT RETREAT', ('Your luxury wilderness journey commences with a personalized private pickup from Delhi or Dehradun Airport/Railway Station. Enjoy a highly comfortable drive as the urban landscape gives way to the breathtaking landscapes of Uttarakhand, bordered by towering Sal trees and old mountain streams. Arrive at your premium handpicked luxury resort near Jim Corbett National Park, checking in seamlessly. After lunch, relax amidst nature\'s pristine quietude.'), [
                'Sightseeing Included: En-route valley photography stops and a late afternoon visit to the scenic Garjiya Devi Temple perched on a massive boulder in the Kosi River.',
                'Evening Experience: A private riverside sundowner high-tea organized exclusively by TRAGUIN with refreshing local herbal blends.',
                'Overnight Stay: Handpicked Luxury Wildlife Resort in Jim Corbett.',
                'Meals Included: Welcome Drink & Gourmet Buffet Dinner.',
            ]),
            _day(2, 'DEEP CORE SAFARI EXPEDITION & WILDLIFE IMMERSION', ('Awake before dawn to the deep call of the wild. Sip freshly brewed coffee before boarding your private, specially chartered 4x4 open-top Jeep Gypsy. Enter the core zone of Jim Corbett National Park as the golden morning mist rises off the grasslands. With an expert TRAGUIN naturalist guiding your sights, track the grand Royal Bengal Tiger, Asian Elephants, Spotted Deer, and an array of rare exotic birds. Return to the resort for a sumptuous late breakfast and midday relaxation by the luxury pool.'), [
                'Sightseeing Included: Core Zone Morning Jeep Safari Drive & evening drive to the beautiful Corbett Waterfalls.',
                'Evening Experience: A curated open-air live barbecue dinner evening accompanied by live traditional acoustic music under a starlit canopy.',
                'Overnight Stay: Handpicked Luxury Wildlife Resort in Jim Corbett.',
                'Meals Included: Artisan Breakfast & Themed Barbecue Dinner.',
            ]),
            _day(3, 'SOULFUL JUNGLE PATHS & HOMEWARD JOURNEY', ('Relish a peaceful breakfast on the resort terrace overlooking the whispering forest canopy. Take a final, gentle walking tour along the resort\'s private nature paths to absorb the calming mountain air. Pack your luxury travel gear and check out smoothly. Your dedicated premium chauffeur will drive you comfortably back to Delhi or Dehradun, completing your exclusive TRAGUIN holiday.'), [
                'Optional Activities: Early morning guided bird-watching walk along the banks of the Kosi River.',
                'Meals Included: Rich Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Taj Corbett Resort & Spa / Aahana The Corbett Wilderness', 'Jim Corbett', '02 Nights', 'Ultra Luxury', 'Luxury Canopy Villa', 'Modified American Plan (Breakfast & Dinner)', 5, 1, description='OPTION 01 – ULTRA LUXURY: Taj Corbett Resort & Spa / Aahana The Corbett Wilderness | Luxury Canopy Villa (02 Nights)'),
            _hotel('The Riverview Retreat / Namah Resort', 'Jim Corbett', '02 Nights', 'Luxury', 'Superior Creek-View Room', 'Modified American Plan (Breakfast & Dinner)', 5, 2, description='OPTION 02 – LUXURY: The Riverview Retreat / Namah Resort | Superior Creek-View Room (02 Nights)'),
            _hotel('Corbett Leela Vilas', 'Jim Corbett', '02 Nights', 'Premium', 'Luxury Cottage Suite', 'Modified American Plan (Breakfast & Dinner)', 4, 3, description='OPTION 03 – PREMIUM: Corbett Leela Vilas | Luxury Cottage Suite (02 Nights)'),
        ],
        inclusions=[
            _inc_included('02 Nights ultra-luxury accommodation in handpicked, premium wilderness properties.', 1),
            _inc_included('Daily artisan breakfasts and multi-cuisine gourmet dinners at the luxury resorts.', 2),
            _inc_included('Complete private city transfers and local journeys in a dedicated luxury air-conditioned vehicle.', 3),
            _inc_included('01 Private Exclusive 4x4 Jeep Safari in the official core Tiger Reserve zone with mandatory permits included.', 4),
            _inc_included('Dedicated professional English/Hindi speaking driver-cum-guide and expert tracker.', 5),
            _inc_included('Complimentary TRAGUIN personalized riverside high-tea setup.', 6),
            _inc_included('All applicable resort luxury taxes, fuel charges, parking fees, and driver toll allocations.', 7),
            _inc_excluded('Flight or interstate railway train bookings to the entry hub.', 8),
            _inc_excluded('Camera equipment fees inside the national reserve boundaries.', 9),
            _inc_excluded('Personal expenditures such as laundry, liquor, and premium spa treatments.', 10),
        ],
    )
    return package, itinerary

def build_uk_018(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UK-018'
    tour_code = 'TRG-UK-018'
    title = 'Premium Mussoorie & Dhanaulti Romantic Experience'
    duration = '03 Nights / 04 Days'
    slug = 'uk-018-premium-mussoorie-dhanaulti-romantic-experience'
    itin_slug = 'uk-018-premium-mussoorie-dhanaulti-romantic-experience-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Uttarakhand, India | Category: Honeymoon / Romantic Escape', 2),
            _ph('Destinations: Mussoorie • Dhanaulti', 3),
            _ph('Ideal for: Newlyweds, Couples & Romance Seekers', 4),
            _ph('Best season: March to June & September to December', 5),
            _ph('Vehicle & Meals: Dedicated Luxury Chauffeur Sedan / SUV at disposal | Modified American Plan (Artisan Breakfasts & Romantic Candlelight Dinners Included)', 6),
            _ph('Route: Dehradun Arrival → Scenic Mussoorie Foothills Drive → Eco Dhanaulti Excursion → Return Departure', 7),
            _ph('TRAGUIN Curated Experience Note: Premium honeymoon suite upgrades with personalized floral layout, custom chocolate platters, a private sunset high-tea on open valley ledges, and highly romantic, unhurried sightseeing trails.', 8),
            _ph('TRAGUIN Signature Experience: Private cliff-side sundowner high-tea setup with premium artisanal blends.', 9),
            _ph('Curated by Experts: Fully flexible day itineraries designed to emphasize relaxation, avoiding any rigid or rushed tracking.', 10),
            _ph('Premium Accommodations: Strategic room requests guaranteeing unobstructed valley and sunrise viewpoints.', 11),
            _ph('Shopping & Local Experiences: Local Souvenirs: Hand-knitted Garhwali pashminas, organic plum jams from Landour, and custom wooden artifacts. Instagram Spots: Vintage red post box at Landour, sunset silhouette at Camel\'s Back Road, and high pine paths of Dhanaulti Eco Park. Café Recommendations: Cafe By The Way and Landour Bakehouse for iconic artisan mountain pastries.', 12),
            _ph('Important Notes: Honeymoon inclusion requests must be finalized along with your initial booking token payment. Heavy winter woolens are essential for Dhanaulti from November through February; light jackets are recommended for summers.', 13),
        ],
        moods=['Honeymoon', 'Romantic', 'Luxury', 'Hills'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Class)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Best Mussoorie Honeymoon Package • Premium Mussoorie & Dhanaulti Romantic Wilderness Experience • 03 Nights / 04 Days',
        overview=('Welcome to the Queen of Hills. TRAGUIN invites you and your significant other to celebrate love amidst the misty valleys, whispering deodars, and soaring snow peaks of Uttarakhand. Surrender to a world of curated experiences, breathtaking landscapes, and premium stays meticulously arranged to ignite romance. This Luxury Mussoorie Holiday brings you exclusive access to scenic beauty, iconic attractions, and immersive experiences, weaving memories that will remain close to your heart forever.\n\nTOUR OVERVIEW\nTravel Month: Tailored Around Your Personal Milestones\nGroup / FIT: Bespoke Private Luxury Honeymoon FIT Tour\nVehicle: Dedicated Luxury Chauffeur Sedan / SUV at disposal for smooth transfers\nMeal Plan: Modified American Plan (Artisan Breakfasts & Romantic Candlelight Dinners Included)\nRoute: Dehradun Arrival → Scenic Mussoorie Foothills Drive → Eco Dhanaulti Excursion → Return Departure\n\nTRAGUIN Curated Experience Note: Premium honeymoon suite upgrades with personalized floral layout, custom chocolate platters, a private sunset high-tea on open valley ledges, and highly romantic, unhurried sightseeing trails.\n\nChoosing the ultimate Best Mussoorie Tour Package or a deeply memorable Mussoorie Honeymoon Package demands an itinerary that smoothly blends colonial charm with tranquil mountain escapes. Discover the Top Tourist Places in Mussoorie, featuring the cascading Kempty Falls, the historic Mall Road, the cloud-kissed heights of Lal Tibba, and the pristine quietude of the Eco Parks in Dhanaulti.'),
        seo_title='UK-018 | Premium Mussoorie Dhanaulti Romantic Experience | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Uttarakhand package (UK-018 / TRG-UK-018): Mussoorie honeymoon, Kempty Falls, Dhanaulti Eco Park, and 3-tier romantic accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Decorated honeymoon suite welcome with fruit basket, chocolate platter, and Camel\'s Back Road sunset stroll', 1),
            _ih('Kempty Falls, Gun Hill Ropeway Ride, Lal Tibba Viewpoint, and Mall Road evening walk', 2),
            _ih('Dhanaulti Eco Park, Surkanda Devi Temple ropeway, and premium cliff-side sundowner high-tea', 3),
            _ih('TRAGUIN Signature Experience: Private cliff-side sundowner high-tea with premium artisanal blends', 4),
            _ih('3-tier handpicked romantic accommodation in Mussoorie (03 Nights)', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN THE CLOUDS — THE ROMANTIC WELCOME', ('Your love story in the hills begins with a private, premium greeting at Dehradun Airport or Railway Station by your dedicated TRAGUIN chauffeur. Ascend the winding, beautiful mountain tracks as the air turns refreshingly crisp. Arrive at your luxury handpicked resort in Mussoorie, where a decorated honeymoon suite awaits your arrival. Enjoy a leisurely afternoon toast to your new journey while admiring the rolling mist over the hills.'), [
                'Sightseeing Included: En-route valley photography stops and an evening exploratory stroll along the iconic Camel\'s Back Road.',
                'Evening Experience: A premium welcome fruit basket, custom chocolate platter, and a private balcony sunset orientation session.',
                'Overnight Stay: Luxury Ridge-Facing Resort in Mussoorie.',
                'Meals Included: Welcome Amenities & Curated Romantic Dinner.',
            ]),
            _day(2, 'MUSSOORIE ICONIC SIGHTSEEING & SUNSET SPECTACLE', ('Awake to a gorgeous mountain sunrise right from your premium bed. Today, uncover the old-world colonial beauty of Mussoorie. Take a cable car ride to Gun Hill for breathtaking views of the majestic Himalayan peaks, visit the cascading waters of Kempty Falls, and explore the beautiful gardens of Company Bagh. In the evening, walk hand-in-hand through Mall Road, soaking in the mountain atmosphere.'), [
                'Sightseeing Included: Kempty Falls, Gun Hill Ropeway Ride, Lal Tibba Viewpoint, and the bustling Mall Road.',
                'Evening Experience: A deeply romantic, private candlelit dinner set up exclusively for you by the resort pool or open-view deck.',
                'Overnight Stay: Handpicked Luxury Resort in Mussoorie.',
                'Meals Included: Artisan Breakfast & Candlelit Dinner.',
            ]),
            _day(3, 'ROMANTIC ESCAPE TO DHANAULTI\'S PINE SANCTUARY', ('Embark on a spectacular day excursion through dense pine and oak forests to the peaceful alpine retreat of Dhanaulti. Marvel at the dramatic, snow-capped mountain vistas flanking the road. Stroll gracefully through the beautifully maintained Eco Park, enjoying the absolute quietude and the crisp, clean breeze.'), [
                'Sightseeing Included: Dhanaulti Eco Park (Amber & Dhara), Surkanda Devi Temple (via comfortable modern ropeway), and the misty Jainalal forest trails.',
                'Evening Experience: A premium roadside high-tea session hosted on a cliff overlook, arranged beautifully by TRAGUIN experts.',
                'Overnight Stay: Premium Luxury Resort in Mussoorie.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(4, 'FOND MEMORIES & FAREWELL TO THE MOUNTAINS', ('Savor your final morning breakfast together on the mountain terrace as the sun illuminates the valley below. Take a final, peaceful stroll along the pine-lined lanes to capture last-minute travel photographs. Your premium luxury vehicle and courteous chauffeur will ensure a comfortable return transfer to Dehradun, completing your dream holiday.'), [
                'Meals Included: Sumptuous Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('JW Marriott Mussoorie Walnut Grove Resort & Spa', 'Mussoorie', '03 Nights', 'Ultra Luxury', 'Luxury Valley View Room', 'Modified American Plan (Breakfast & Dinner)', 5, 1, description='OPTION 01 – ULTRA LUXURY: JW Marriott Mussoorie Walnut Grove Resort & Spa | Luxury Valley View Room (03 Nights)'),
            _hotel('Welcomhotel by ITC Hotels, The Savoy / Rokeby Manor', 'Mussoorie', '03 Nights', 'Luxury', 'Premium Suite', 'Modified American Plan (Breakfast & Dinner)', 5, 2, description='OPTION 02 – LUXURY: Welcomhotel by ITC Hotels, The Savoy / Rokeby Manor | Premium Suite (03 Nights)'),
            _hotel('Mosaic Hotel Mussoorie / Jaypee Residency Manor', 'Mussoorie', '03 Nights', 'Premium', 'Executive Room', 'Modified American Plan (Breakfast & Dinner)', 4, 3, description='OPTION 03 – PREMIUM: Mosaic Hotel Mussoorie / Jaypee Residency Manor | Executive Room (03 Nights)'),
        ],
        inclusions=[
            _inc_included('03 Nights ultra-luxury accommodation in handpicked, romance-oriented premium properties.', 1),
            _inc_included('Daily curated buffet breakfasts and custom candlelight dinners at the resorts.', 2),
            _inc_included('Dedicated private luxury sedan/SUV for complete airport/station transfers and localized sightseeing.', 3),
            _inc_included('Complimentary honeymoon layout features (personalized floral decoration, custom cake, and chocolate platter).', 4),
            _inc_included('Pre-arranged premium round-trip cable car ropeway tickets for Gun Hill.', 5),
            _inc_included('Dedicated TRAGUIN 24/7 on-ground guest relations remote assistance.', 6),
            _inc_included('All applicable resort luxury service taxes, state border permits, driver allowance, and toll costs.', 7),
            _inc_excluded('Long-distance airfare or intercity express train tickets to Dehradun.', 8),
            _inc_excluded('Personal expenditures such as laundry, specialty spa sessions, and telephone calls.', 9),
            _inc_excluded('Optional adventure activity charges (ziplining, sky walking in Dhanaulti).', 10),
        ],
    )
    return package, itinerary

UK_011_018_BUILDERS = [
    build_uk_011,
    build_uk_012,
    build_uk_013,
    build_uk_014,
    build_uk_015,
    build_uk_016,
    build_uk_017,
    build_uk_018,
]
