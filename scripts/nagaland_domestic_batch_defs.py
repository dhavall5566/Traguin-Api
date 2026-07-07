"""Builder functions for NL-001 through NL-010 Nagaland domestic packages."""

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

NAGALAND_SLUG = "nagaland"


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


def build_nl_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'NL-001'
    tour_code = 'TRAGUIN-NL-001'
    title = 'Nagaland Discovery: A Premium Custom Travel Experience'
    duration = '05 Nights / 06 Days'
    slug = 'nl-001-nagaland-discovery-a-premium-custom-travel-experience'
    itin_slug = 'nl-001-nagaland-discovery-a-premium-custom-travel-experience-itinerary'
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
            _ph('Serial code NL-001 | TRAGUIN tour code TRAGUIN-NL-001', 1),
            _ph('State / Country: Nagaland / India | Category: Premium Luxury Family Vacation', 2),
            _ph('Destinations: Dimapur • Kohima • Khonoma • Mokokchung', 3),
            _ph('Ideal for: Families, Culture Seekers, Luxury Travelers', 4),
            _ph('Best season: October to May (Special Hornbill Festival in Dec)', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle / Meals: Private Premium SUV (Innova Crysta) / Modified American Plan (Breakfast & Dinner)', 7),
            _ph('Route: Dimapur → Kohima → Khonoma Green Village → Mokokchung → Dimapur', 8),
            _ph('TRAGUIN Signature Experience: Private audience with local village elders in Khonoma to listen to orally', 9),
            _ph('Curated by TRAGUIN Experts: Hand-crafted travel paces optimized fully for families, balancing active', 10),
            _ph('Personalized Assistance: Seamless coordination with zero waiting times at protected tribal boundary', 11),
            _ph('Premium Handpicked Hotels: Continuous monitoring of luxury properties to ensure the highest', 12)
        ],
        moods=['Family', 'Culture', 'Luxury'],
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
        tagline='Dimapur • Kohima • Khonoma • Mokokchung',
        overview='Nagaland Discovery: A Premium Custom Travel Experience “Unveiling the Mystique of the Land of the Nagas in Absolute Luxury” Embark on an extraordinary journey through dense mist-laden hills, ancestral tribal legacies, and untouched ecosystems. Designed perfectly as a high-end Nagaland Family Tour or an exclusive Luxury Nagaland Holiday, this bespoke itinerary weaves deep cultural immersion with curated premium comforts, brought to life exclusively by TRAGUIN.\n\nTOUR OVERVIEW\nWelcome to a meticulously planned North-East experience curated by TRAGUIN Experts. This luxury getaway is tailored for discerning families who wish to explore the rich warrior history, intricate handlooms, and scenic visual poetry of Nagaland without compromising on comfort. VEHICLE: Private Premium SUV (Innova Crysta) throughout the journey MEAL PLAN: Modified American Plan (Breakfast & Dinner Included) ROUTE MAP: Dimapur → Kohima → Khonoma Green Village → Mokokchung → Dimapur GUEST TYPE: Premium Family / FIT TRAGUIN Curated Experience Note: Every aspect of this Nagaland Sightseeing tour has been personally vetted. From private cultural audiences with Angami village elders to smooth, high-clearance premium transport along winding mountain ridges, we ensure your family experiences the warmth of Naga hospitality seamlessly.\n\nWHY CHOOSE A PREMIUM NAGALAND EXPERIENCE?\nNagaland remains one of Asia’s last pristine cultural frontiers, making it the ultimate destination for an unforgettable luxury family getaway. The region is highly celebrated for its spectacular landscapes, emerald valleys, and its legendary 16 indigenous tribes, each safeguarding distinct customs, attire, and dialects. Whether you are searching for the Best Nagaland Tour Package for immersive heritage or a highly bespoke Nagaland Honeymoon Package set against misty mountains, the land offers unmatched beauty. Key highlights include exploring the Top Tourist Places in Nagaland such as the historic Kohima War Cemetery, the architectural wonders of Khonoma Green Village, and the traditional tribal bastions of Mokokchung. The Best Time to Visit Nagaland spans from October to May, when the weather is perfectly crisp, skies are clear cerulean blue, and the state bursts into colorful community celebrations, most notably the iconic Hornbill Festival in December. Let TRAGUIN Nagaland Packages guide you through a realm of living history, rare organic gastronomy, and premium high-altitude serenity.',
        seo_title='NL-001 | Nagaland Discovery: A Premium Custom Travel Experience | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Nagaland package (NL-001 / TRAGUIN-NL-001): Dimapur • Kohima • Khonoma • Mokokchung with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DIMAPUR & SCENIC TRANSFER TO KOHIMA', 1),
            _ih('Day 02: KOHIMA SIGHTSEEING — EMBARKING ON HISTORIC & CULTURAL LEGEND', 2),
            _ih("Day 03: EXCURSION TO KHONOMA — ASIA'S FIRST ECO-GREEN VILLAGE", 3),
            _ih('Day 04: KOHIMA TO MOKOKCHUNG — INTO THE CULTURAL HEARTLAND OF THE AO', 4),
            _ih('Day 05: MOKOKCHUNG — UNVEILING THE LIVING HERITAGE OF UNTOUCHED', 5),
            _ih('Day 06: MOKOKCHUNG TO DIMAPUR — DEPARTURE WITH TIMELESS MEMORIES', 6),
            _ih('TRAGUIN Signature Experience: Private audience with local village elders in Khonoma to listen to orally', 7),
            _ih('Curated by TRAGUIN Experts: Hand-crafted travel paces optimized fully for families, balancing active', 8),
            _ih('Personalized Assistance: Seamless coordination with zero waiting times at protected tribal boundary', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DIMAPUR & SCENIC TRANSFER TO KOHIMA',
                (
                    'Your extraordinary journey begins as you step off your flight at Dimapur Airport. A dedicated TRAGUIN tour ambassador will warmly welcome your family and escort you to your awaiting private luxury SUV. Leaving the bustling plains of Dimapur behind, you will embark on a highly scenic drive ascending into the crisp, refreshing air of the Naga hills toward Kohima, the historic capital city. Along the way, stop for a gourmet refreshment break while overlooking breathtaking landscapes of deep-green gorges and cascading roadside waterfalls. As you enter Kohima, check into your handpicked premium accommodation. The evening is yours to relax and adjust to the serene mountain pace. authentic mild Naga culinary delicacies.'
                ),
                [
                    'Sightseeing Included: Scenic mountain drive, entry lookouts, roadside panoramic photography points.',
                    'Evening Experience: A private welcome dinner at the hotel featuring a curated blend of continental and',
                    'Overnight Stay: Handpicked Premium Luxury Hotel / Luxury Eco-Lodge in Kohima.',
                    'Meals Included: Dinner.',
                ],
            ),
            _day(
                2,
                'KOHIMA SIGHTSEEING — EMBARKING ON HISTORIC & CULTURAL LEGEND',
                (
                    "Awake to a majestic sunrise over the mist-clad peaks. Today is dedicated to an immersive Kohima Sightseeing experience. First, visit the beautifully manicured Kohima War Cemetery, a poignant World War II memorial dedicated to the brave soldiers who stopped the advancing forces in the famous Battle of Kohima. Next, drive to the Kisama Heritage Village, the legendary permanent venue of the world-famous Hornbill Festival. Walk through meticulously crafted traditional Naga morungs (tribal bachelors' dormitories) representing all 16 tribes. Conclude your afternoon with a visit to the Kohima State Museum, showcasing priceless royal tribal artifacts, ancestral jewelry, and warrior costumes. Handloom Emporium. organic artisanal coffee."
                ),
                [
                    'Sightseeing Included: WWII War Cemetery, Kisama Heritage Village, Kohima State Museum, Local Naga',
                    'Optional Activities: Specialized guided photography walk through the local fresh produce and spice markets.',
                    'Evening Experience: Relaxed evening stroll at a premium boutique cafe in Kohima sampling locally grown',
                    'Overnight Stay: Handpicked Premium Luxury Hotel / Luxury Eco-Lodge in Kohima.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                3,
                "EXCURSION TO KHONOMA — ASIA'S FIRST ECO-GREEN VILLAGE",
                (
                    'Today, travel back in time as you visit the legendary Khonoma Green Village, located about 20 km from Kohima. Khonoma is an ancient 700-year-old settlement famed for its brave warrior history and its revolutionary global model of eco-conservation. A local village expert will guide your family through traditional stone gateways, explaining the genius of their ancient terrace farming methods. Witness an exclusive, private demonstration of traditional basket weaving and organic shawl weaving. The sheer scenic beauty of the step cultivation fields carved into steep mountain slopes provides an exceptional backdrop for incredible family photographs. Enjoy a premium, organically sourced farm-to-table lunch prepared specially for TRAGUIN guests within the village. morungs.'
                ),
                [
                    'Sightseeing Included: Khonoma Fort, Eco-conservation reserve, ancient step-farming overlooks, traditional',
                    'Optional Activities: A light, scenic nature trek through the surrounding alder tree forests for birdwatching.',
                    'Evening Experience: Return to Kohima for an interactive traditional cooking demonstration at the lodge.',
                    'Overnight Stay: Handpicked Premium Luxury Hotel / Luxury Eco-Lodge in Kohima.',
                    'Meals Included: Breakfast, Curated Lunch & Dinner.',
                ],
            ),
            _day(
                4,
                'KOHIMA TO MOKOKCHUNG — INTO THE CULTURAL HEARTLAND OF THE AO',
                (
                    'NAGA Following an early breakfast, your premium SUV departs northwards toward Mokokchung, the vibrant cultural capital of the Ao Naga tribe. This journey is a breathtaking showcase of rural Nagaland, passing through beautiful terraced rice paddies, tea gardens, and misty valleys. Arrive in Mokokchung by afternoon and check into your premium valley-view resort. Mokokchung is universally celebrated for its pristine hospitality and beautifully kept villages. Spend your late afternoon visiting the structural marvels of the town and interacting with warm, welcoming locals who love sharing stories of their grand cultural lineage. Mokokchung town center. painted attire. staple of Naga culture.'
                ),
                [
                    'Sightseeing Included: Longkhum Village (famed for its panoramic ridge views and rhododendron paths),',
                    'Optional Activities: Interaction with local Ao artisans specializing in traditional wood carving and hand-',
                    'Evening Experience: Sunset viewing from the resort deck accompanied by live acoustic music, a beloved',
                    'Overnight Stay: Premium Heritage Resort / Luxury Eco-Resort in Mokokchung.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                5,
                'MOKOKCHUNG — UNVEILING THE LIVING HERITAGE OF UNTOUCHED',
                (
                    'VILLAGES Dedicate your morning to exploring Mopungchuket Village, widely regarded as one of the best-preserved cultural villages in the entire North-East. Walk along pristine pathways to see the awe-inspiring time- weathered log-drums, towering totem poles, and the romantic cultural monument of Jina and Etiben (the Romeo and Juliet of the Ao tribe). Next, visit Ungma Village, the oldest and largest village of the Ao tribe, offering a profound look into ancestral governing systems. The day is rich with unforgettable memories, deep historical insights, and immersive experiences that connect your family directly to the true spirit of India’s tribal frontier. village museums. photoshoot. cuisine.'
                ),
                [
                    'Sightseeing Included: Mopungchuket cultural site, Ungma heritage village, sacred log-drums, traditional',
                    'Optional Activities: Trying on ornate, traditional Ao warrior attire for an exclusive, professional family',
                    'Evening Experience: A grand, private farewell dinner organized by TRAGUIN featuring premium fusion',
                    'Overnight Stay: Premium Heritage Resort / Luxury Eco-Resort in Mokokchung.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                6,
                'MOKOKCHUNG TO DIMAPUR — DEPARTURE WITH TIMELESS MEMORIES',
                (
                    'After a delightful breakfast overlooking the sweeping valley, pack your bags filled with beautiful memories, authentic souvenirs, and stories to last a lifetime. Your private premium SUV will comfortably transfer your family back down to Dimapur Airport. Your dedicated TRAGUIN travel consultant will ensure a seamless drop- off at the terminal for your homeward flight, concluding your ultra-premium, luxury holiday to magical Nagaland.'
                ),
                [
                    'Sightseeing Included: Return scenic valley transit, final viewpoint stops.',
                    'Meals Included: Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Vivor / Equivalent | Hotel Whispering Winds / Equivalent',
                'Kohima | Mokokchung',
                '3N Kohima|2N Mokokchung',
                'Deluxe',
                'Deluxe Room',
                'Breakfast & Dinner (MAP)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Vivor / Equivalent | Hotel Whispering Winds / Equivalent | Breakfast & Dinner (MAP)',
            ),
            _hotel(
                'The Heritage Kohima / Equivalent | Woodland Resort / Equivalent',
                'Kohima | Mokokchung',
                '3N Kohima|2N Mokokchung',
                'Premium',
                'Deluxe Room',
                'Breakfast & Dinner (MAP)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Heritage Kohima / Equivalent | Woodland Resort / Equivalent | Breakfast & Dinner (MAP)',
            ),
            _hotel(
                'Razhu Pru Heritage Mansion / Equivalent | Mopungchuket Luxury Eco-Lodge',
                'Kohima | Mokokchung',
                '3N Kohima|2N Mokokchung',
                'Luxury',
                'Heritage Mansion | Luxury Eco-Lodge',
                'Breakfast & Dinner (MAP)',
                5,
                3,
                description='OPTION 03 – LUXURY: Razhu Pru Heritage Mansion / Equivalent | Mopungchuket Luxury Eco-Lodge | Breakfast & Dinner (MAP)',
            ),
            _hotel(
                'Dzukou Valley Luxury Glamping / Tents | TRAGUIN Signature Handpicked Estate',
                'Kohima | Mokokchung',
                '3N Kohima|2N Mokokchung',
                'Ultra Luxury',
                'Luxury Glamping | Signature Estate',
                'All Meals Custom Curated',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Dzukou Valley Luxury Glamping / Tents | TRAGUIN Signature Handpicked Estate | All Meals Custom Curated',
            )
        ],
        inclusions=[
            _inc_included('05 Nights luxurious accommodation in handpicked top-rated properties.', 1),
            _inc_included('Modified American Plan (Daily Premium Breakfast and Chef-Curated Dinners).', 2),
            _inc_included('Private exclusive airport transfers and all sightseeing via premium SUV (Innova Crysta).', 3),
            _inc_included('Professional, English-speaking certified local cultural guides for deep storytelling.', 4),
            _inc_included('All inner line permits (ILP) and state entry documentation handled seamlessly.', 5),
            _inc_included('Exclusive farm-to-table lunch experience at Khonoma Green Village.', 6),
            _inc_included('Complimentary welcome amenities and custom travel comfort kits in the vehicle.', 7),
            _inc_included('24/7 dedicated remote concierge support from TRAGUIN operational headquarters.', 8),
            _inc_excluded('Domestic or International Airfare / Train tickets to Dimapur.', 9),
            _inc_excluded('Personal expenses (laundry, telephone calls, premium alcoholic beverages).', 10),
            _inc_excluded('Camera fees, video recording charges at monument checkpoints.', 11),
            _inc_excluded('Optional adventure activities or treks not explicitly outlined.', 12),
            _inc_excluded('Travel insurance policies (highly recommended).', 13),
            _inc_excluded('Tips and gratuities for drivers, local guides, and hotel staff.', 14),
        ],
    )
    return package, itinerary

def build_nl_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'NL-002'
    tour_code = 'TRAGUIN-NL-002'
    title = 'Immersive Cultural Odyssey & The Legendary Hornbill Festival Experience'
    duration = '04 Nights / 05 Days'
    slug = 'nl-002-immersive-cultural-odyssey-and-the-legendary-hornbill-festival-experience'
    itin_slug = 'nl-002-immersive-cultural-odyssey-and-the-legendary-hornbill-festival-experience-itinerary'
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
            _ph('Serial code NL-002 | TRAGUIN tour code TRAGUIN-NL-002', 1),
            _ph('State / Country: Nagaland / India | Category: Culture & Heritage', 2),
            _ph('Destinations: Dimapur • Kohima • Kisama Heritage Village • Khonoma Green Village', 3),
            _ph('Ideal for: Culture Enthusiasts, Photographers, Luxury Explorers, Families & Honeymooners', 4),
            _ph('Best season: December (Hornbill Festival)', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle / Meals: Private Premium Luxury SUV (Toyota Innova Crysta) / MAPAI', 7),
            _ph('Route: Dimapur to Kohima to Kisama Heritage Village to Khonoma to Dimapur', 8),
            _ph('TRAGUIN Signature Experience: Private interactive meet-and-greet sessions with respected tribal', 9),
            _ph('Curated by TRAGUIN Experts: Every day-wise timeline is balanced perfectly to avoid the massive', 10),
            _ph('Premium Handpicked Hotels: Properties are chosen based on rigorous standards of hygiene, local', 11),
            _ph('Exclusive Recommendations: Access to a handpicked selection of top tribal coffee houses and', 12),
            _ph('& BOOKING GUIDELINES', 13),
            _ph('Inner Line Permit (ILP): All Indian domestic tourists require an Inner Line Permit to enter Nagaland.', 14)
        ],
        moods=['Culture', 'Heritage', 'Festival'],
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
        tagline='Dimapur • Kohima • Kisama Heritage Village • Khonoma Green Village',
        overview="Immersive Cultural Odyssey & The Legendary Hornbill Festival Experience 04 NIGHTS / 05 DAYS Step into a realm untouched by time, where the misty emerald hills echo with the rhythmic beats of ancient log drums and the soulful chants of warrior tribes. Nagaland, famously known as the 'Land of Festivals,' opens its heart to discerning travelers through this ultimate Luxury Nagaland Holiday. Carefully crafted by our travel artisans, this immersive itinerary centers around the world-renowned TRAGUIN • Premium Travel & Luxury Holidays Hornbill Festival Tour, presenting an unparalleled opportunity to witness the striking traditions, vivid attires, indigenous culinary practices, and spectacular folk dances of sixteen distinct Naga tribes. Let TRAGUIN guide you into the deep heritage of Northeast India with seamless execution, premium comforts, and highly localized, private insights.\n\nTOUR OVERVIEW\nRoute: Dimapur to Kohima to Kisama Heritage Village to Khonoma to Dimapur Travel Mode / Vehicle: Private Premium Luxury SUV (Toyota Innova Crysta) throughout the journey. Meal Plan: Modified American Plan (MAPAI) – Daily Premium Buffet Breakfast & Gourmet Dinners at Host Properties. Guest Type: FIT / Premium Corporate / Luxury Family Tour / Cultural Explorers. TRAGUIN Curated Experience Note: This itinerary features priority entry passes to the premium seating arenas at the Hornbill Festival main grounds in Kisama, private traditional lunch sessions hosted inside an authentic Angami tribal Morung, and an expert local cultural historian guiding you through the profound symbolism of tribal tattoos, headgears, and historical monoliths.\n\nWHY BOOK THE PREMIUM NAGALAND HORNBILL FESTIVAL\nEXPERIENCE? Choosing the Best Nagaland Tour Package means plunging into an explosive celebration of indigenous folklore and heritage. The landmark Hornbill Festival, celebrated annually from December 1st to 10th at the Kisama Heritage Village, serves as a grand collaborative canvas where all the tribes of Nagaland converge. This highly sought-after Nagaland Family Tour and Nagaland Honeymoon Package combines the thrill of raw ethnic discovery with the comfort of high-end logistics. From exploring the historical remnants of the World War II Cemetery to capturing the popular Instagram locations within the mist-covered valleys of Khonoma—Asia’s first documented green village—every moment is an immersion into living history. Travelers can shop for unique handwoven Naga shawls, delicate bamboo handicrafts, and organic structural jewelry while savoring unique local gastronomy. With TRAGUIN Nagaland Packages, you bypass the challenges of local logistics in remote terrains, ensuring a sophisticated, safe, and profoundly touching experience of Nagaland Sightseeing during the peak festival season. TRAGUIN • Premium Travel & Luxury Holidays",
        seo_title='NL-002 | Immersive Cultural Odyssey & The Legendary Hornbill Festival Experience | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Nagaland package (NL-002 / TRAGUIN-NL-002): Dimapur • Kohima • Kisama Heritage Village • Khonoma Green Village with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DIMAPUR & SCENIC PRIVATE TRANSFER TO THE HILL CAPITAL, KOHIMA YOUR EXTRAORDINARY CULTURAL VOYAGE BEGINS TH...', 1),
            _ih('Day 02: THE GRAND INCEPTION: IMMERSIVE DAY AT HORNBILL FESTIVAL, KISAMA HERITAGE VILLAGE AWAKE TO A PRISTINE MOUNTAIN SUNRISE...', 2),
            _ih('Day 03: ECO-CONSERVATION & TRIBAL HERITAGE: EXCURSION TO KHONOMA GREEN VILLAGE AFTER A PREMIUM BREAKFAST, EMBARK ON A DEEPLY ...', 3),
            _ih('Day 04: KOHIMA DEEP DIVE: WWII HISTORY, CATHEDRALS & TRIBAL CRAFT EMPORIUMS DEVOTE YOUR MORNING TO A DEEPER EXPLORATION OF KO...', 4),
            _ih('Day 05: BID FAREWELL TO THE LAND OF WARRIORS: DRIVE TO DIMAPUR &', 5),
            _ih('TRAGUIN Signature Experience: Private interactive meet-and-greet sessions with respected tribal', 6),
            _ih('Curated by TRAGUIN Experts: Every day-wise timeline is balanced perfectly to avoid the massive', 7),
            _ih('Premium Handpicked Hotels: Properties are chosen based on rigorous standards of hygiene, local', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DIMAPUR & SCENIC PRIVATE TRANSFER TO THE HILL CAPITAL, KOHIMA YOUR EXTRAORDINARY CULTURAL VOYAGE BEGINS TH...',
                (
                    'receive a traditional, warm welcome by a senior representative from TRAGUIN and your dedicated professional driver. Board your luxury SUV and commence a captivating, scenic drive ascending toward Kohima, located at an elevation of H = 1444 meters. As the road snakes upward through verdant sub- tropical forests, watch the plains fade away into breathtaking landscapes of the pristine Naga hills. En route, pause at selected panoramic photography points to capture the gorgeous valley views and enjoy artisanal local tea. Upon arriving in the mist-veiled capital of Kohima, check into your handpicked premium hotel or luxury festival camp. The evening is yours to relax and adapt to the refreshing mountain air, followed by a detailed briefing from your local cultural guide regarding the upcoming festivities. Scenic valley viewpoints, historical entry gates, local countryside photography stops. A casual walk through the local Naga Bazaar to view rare traditional organic produce. Gourmet welcome dinner featuring a fusion of continental classics and subtle local herbs. Handpicked Luxury Resort / Premium Festival Camp, Kohima. Curated Gourmet Dinner.'
                ),
                [
                    'Sightseeing Included',
                    'Optional Activities',
                    'Evening Experience',
                    'Overnight Stay',
                    'Meals Included',
                ],
            ),
            _day(
                2,
                'THE GRAND INCEPTION: IMMERSIVE DAY AT HORNBILL FESTIVAL, KISAMA HERITAGE VILLAGE AWAKE TO A PRISTINE MOUNTAIN SUNRISE...',
                (
                    "attraction of your TRAGUIN Nagaland Packages: the legendary Hornbill Festival held at the Kisama Heritage Village. Located about 12 kilometers from Kohima, this living museum replicates the traditional architectural layouts of the various Naga tribes. With your premium VIP entry passes, take your designated seats to witness the spectacular cultural performances. Be amazed by the thunderous war cries, rhythmic traditional dances, and vibrant attire adorned with hornbill feathers and brass ornaments. Walk alongside your personal expert guide as you explore the 'Morungs'—traditional youth dormitories of each tribe. Engage with tribal elders, observe exquisite woodcarvings, and participate in local games like the famous chili-eating competition. Main Arena Performances, 16 Tribal Morungs, World War II Museum within Kisama, Traditional Craft Complex. Try local rice beer served in traditional bamboo mugs paired with wood-fired local snacks. Attend the spectacular Hornbill National Rock Concert and explore the lively Kohima Night Bazaar. Handpicked Luxury Resort / Premium Festival Camp, Kohima. Premium Breakfast & Curated Gourmet Dinner."
                ),
                [
                    'Sightseeing Included',
                    'Optional Activities',
                    'Evening Experience',
                    'Overnight Stay',
                    'Meals Included',
                ],
            ),
            _day(
                3,
                'ECO-CONSERVATION & TRIBAL HERITAGE: EXCURSION TO KHONOMA GREEN VILLAGE AFTER A PREMIUM BREAKFAST, EMBARK ON A DEEPLY ...',
                (
                    "settlement of the Angami tribe renowned globally as Asia's first official green village. This destination is a prime highlight of the Premium Nagaland Experience. The village is highly praised for its self-sustained community forest conservation models and ancient terraced agricultural fields dating back centuries. Walk along the pristine stone-paved paths of the village to discover historical fortresses (Khels), ceremonial gates, and traditional morungs. Meet local artisans who excel in weaving intricate baskets and blankets from cane and bamboo. Hear heroic stories of how the villagers protected their ancestral lands during the British era, and enjoy a curated, organic traditional lunch inside an authentic village home. Khonoma Ceremonial Gates, Historical Khel Fortifications, Terrace Farming Viewpoints, Traditional Handloom units. A soft guided trek into the surrounding alder wood forests for panoramic bird- watching. Relaxing fireside storytelling session back at your resort, accompanied by acoustic local melodies. Handpicked Luxury Resort / Premium Festival Camp, Kohima. Premium Breakfast, Traditional Local Lunch & Gourmet Dinner."
                ),
                [
                    'Sightseeing Included',
                    'Optional Activities',
                    'Evening Experience',
                    'Overnight Stay',
                    'Meals Included',
                ],
            ),
            _day(
                4,
                'KOHIMA DEEP DIVE: WWII HISTORY, CATHEDRALS & TRIBAL CRAFT EMPORIUMS DEVOTE YOUR MORNING TO A DEEPER EXPLORATION OF KO...',
                (
                    'maintained Kohima World War II Cemetery, located on the historic slopes of Garrison Hill. This quiet memorial stands as a testament to one of the fiercest battles of the second World War, featuring the iconic epitaph: "When you go home, tell them of us and say, for your tomorrow, we gave our today." Next, proceed to the magnificent Cathedral of Kohima, famous for its striking architecture that blends traditional Naga structure with contemporary design, housing one of Asia\'s largest wooden crosses. Spend your afternoon exploring the State Museum, which showcases rare ethnographic collections, tribal ornaments, weapons, and musical instruments. Conclude your day with a curated shopping visit to the Central Handloom & Handicrafts Emporium. WWII Memorial Cemetery, Cathedral of Kohima, Nagaland State Museum, Central Craft Emporium. Fine-dining coffee tasting session featuring premium organically grown local Arabica beans. Premium farewell dinner hosted by TRAGUIN featuring local delicacies and international favorites. Handpicked Luxury Resort / Premium Festival Camp, Kohima. Premium Breakfast & Farewell Gourmet Dinner.'
                ),
                [
                    'Sightseeing Included',
                    'Optional Activities',
                    'Evening Experience',
                    'Overnight Stay',
                    'Meals Included',
                ],
            ),
            _day(
                5,
                'BID FAREWELL TO THE LAND OF WARRIORS: DRIVE TO DIMAPUR &',
                (
                    'Savor your final morning breakfast looking out over the misty hills of Kohima. Check out from your premium stay and board your luxury vehicle for a relaxed drive down back toward Dimapur. As you travel down the hills, pass by rural markets selling fresh bamboo shoots, seasonal local wild fruits, and handcrafted artifacts. Depending on your flight schedule, stop briefly to view the historic 10th-century Kachari Ruins, famous for their mysterious monolithic mushroom-shaped pillars. Your driver will drop you at Dimapur Airport in good time for your onward flight. Your legendary Hornbill Festival Tour concludes here, leaving you with unforgettable memories, deep cultural insights, and a newfound love for Northeast India, all delivered with the signature touch of TRAGUIN. Kachari Monolithic Ruins (time permitting), local highway organic markets. Premium Breakfast.'
                ),
                [
                    'DEPARTURE',
                    'Sightseeing Included',
                    'Meals Included',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Vivor / The Heritage Kohima',
                'Kohima',
                '4N Kohima',
                'Deluxe',
                'Executive Room',
                'MAPAI',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Vivor / The Heritage Kohima | MAPAI',
            ),
            _hotel(
                'Zone Niathu Dimapur By The Park / Hotel Japfü',
                'Kohima',
                '4N Kohima',
                'Premium',
                'Premium Suite',
                'MAPAI',
                4,
                2,
                description='OPTION 02 – PREMIUM: Zone Niathu Dimapur By The Park / Hotel Japfü | MAPAI',
            ),
            _hotel(
                'The Ultimate Travelling Camp (TUTC) Kohima',
                'Kohima',
                '4N Kohima',
                'Luxury',
                'Luxury Safari Tent',
                'MAPAI',
                5,
                3,
                description='OPTION 03 – LUXURY: The Ultimate Travelling Camp (TUTC) Kohima | MAPAI',
            ),
            _hotel(
                'Exclusive Private Tribal Villa Estate / Royal TUTC Suite',
                'Kohima',
                '4N Kohima',
                'Ultra Luxury',
                'Ultra Luxury Presidential Tent',
                'MAPAI',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Exclusive Private Tribal Villa Estate / Royal TUTC Suite | MAPAI',
            )
        ],
        inclusions=[
            _inc_included('Premium Accommodation: 04 Nights stay in handpicked, top-rated luxury accommodations on twin sharing basis.', 1),
            _inc_included("Gourmet Meal Plan: Daily elaborate multi-cuisine breakfasts and customized table d'hôte dinners at the properties.", 2),
            _inc_included('Luxury Transportation: All transfers, inter-city movements, and Nagaland Sightseeing routes in an exclusive, private Toyota Innova Crysta SUV.', 3),
            _inc_included('VIP Access Passes: Pre-arranged priority entry passes to the main arena seats at the Hornbill Festival grounds.', 4),
            _inc_included('Curated Tribal Luncheon: An authentic, private ethnic lunch experience in Khonoma Green Village.', 5),
            _inc_included('Expert Accompaniment: Highly knowledgeable, English-speaking tribal cultural guides certified by local heritage groups.', 6),
            _inc_included('Welcome Amenities: Personalized luxury travel kit including organic sanitizers, premium local teas, and a customized festival guide block.', 7),
            _inc_included('Dedicated Support: 24/7 real-time remote concierge support directly from the TRAGUIN guest relations desk.', 8),
            _inc_included('All Systemic Taxes: Inclusive of all state permits, Inner Line Permits (ILP) documentation charges, fuel surcharges, parking costs, and toll taxes.', 9),
            _inc_excluded('Domestic or international airfares to and from Dimapur Airport.', 10),
            _inc_excluded('Personal expenses such as laundry, premium alcoholic beverages, mineral water, and telephone calls.', 11),
            _inc_excluded('Camera fees, video recording permissions, or specialized drone photography licensing at the sightseeing venues.', 12),
            _inc_excluded('Any optional adventure activities, tips for drivers/guides, or expenses incurred due to flight delays or natural disruptions.', 13),
            _inc_excluded('Any services or entry costs not explicitly listed under the official TRAGUIN inclusions section.', 14),
        ],
    )
    return package, itinerary

def build_nl_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'NL-003'
    tour_code = 'TRAGUIN-NL-003'
    title = 'Nagaland Explorer: The Ultimate Horizon'
    duration = '06 Nights / 07 Days'
    slug = 'nl-003-nagaland-explorer-the-ultimate-horizon'
    itin_slug = 'nl-003-nagaland-explorer-the-ultimate-horizon-itinerary'
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
            _ph('Serial code NL-003 | TRAGUIN tour code TRAGUIN-NL-003', 1),
            _ph('State / Country: Nagaland / India | Category: Premium Adventure & Cultural Immersion', 2),
            _ph('Destinations: Dimapur • Kohima • Khonoma • Pfutsero • Mokokchung', 3),
            _ph('Ideal for: Luxury Explorers, Culture Enthusiasts, Photographers', 4),
            _ph('Best season: October to May (Includes Hornbill Festival Season)', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle / Meals: Premium 4x4 Luxury SUV (Toyota Innova Crysta) / MAPAI', 7),
            _ph('Route: Dimapur → Kohima → Khonoma → Pfutsero → Mokokchung → Dimapur', 8),
            _ph('TRAGUIN Signature Experience: Private, arranged audiences with village elders in Khonoma, preserving', 9),
            _ph('Curated by TRAGUIN Experts: Handcrafted itineraries designed to highlight authentic tribal lifestyle without', 10),
            _ph('Personalized Assistance: Dedicated destination managers monitoring road conditions, check-ins, and comfort', 11),
            _ph('Premium Handpicked Hotels: Every property is vetted for cleanliness, local charm, safety, and excellent food', 12),
            _ph('for beautifully patterned tribal shawls, beaded jewelry, bamboo utility baskets, and hand-carved wood accents. For a taste of the local flavors, look for organic forest honey, fermented bamboo shoots, and the famous Naga king chili. Popular spots like the Kohima artisan market and the local cafes in Mokokchung offer great places to relax, chat with residents, and experience the warm hospitality of the region.', 13)
        ],
        moods=['Adventure', 'Culture', 'Luxury'],
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
        tagline='Dimapur • Kohima • Khonoma • Pfutsero • Mokokchung',
        overview="NAGALAND EXPLORER: THE ULTIMATE HORIZON Welcome to an uncharted paradise where ancient tribal traditions blend seamlessly with breathtaking landscapes and mist-shrouded peaks. Designed meticulously for discerning travelers, our exclusive Nagaland Family Tour and bespoke Nagaland Honeymoon Package configurations unlock the enigmatic soul of India’s far east. Journey through deep emerald valleys, historic warrior strongholds, and vibrant tribal hearts with the signature comfort of a TRAGUIN Premium Holidays • Nagaland Explorer Luxury Nagaland Holiday. This curated journey captures the raw, unfiltered essence of the Naga hills while promising elite comforts, immersive local hospitality, and memories designed to stand the test of time.\n\nTOUR OVERVIEW\nThis premium signature itinerary is a handcrafted, experiential voyage through the legendary lands of the Angami, Ao, and Chakhesang tribes. Journeying across a route meticulously mapped from Dimapur to the high-altitude vistas of Pfutsero and the cultural capital of Mokokchung, you will witness the legendary legacy of a proud warrior culture. Operating as a completely private, flexible, and customized Free Independent Traveler (FIT) expedition, this program ensures personalized comfort. Every transfer is managed via an elite, high-clearance premium SUV perfectly suited to the rolling hill topography. Your experience is paired with curated breakfast and dinner plans across Nagaland's finest eco-lodges and luxury boutique homestays. With the dedicated 24/7 concierge support that defines a Premium Nagaland Experience by TRAGUIN, your safety, luxury, and enrichment remain absolutely uncompromised. THE ENIGMATIC ALLURE OF NAGALAND: PREMIUM CULTURAL & ADVENTURE INSIGHTS Choosing a Nagaland Tour Package means stepping beyond conventional tourism into an immersive theater of living culture. Renowned globally for its iconic Hornbill Festival, mystical rolling hills, and resilient tribal legacy, Nagaland stands as one of Asia's most compelling cultural bastions. The Best Time to Visit Nagaland spans from the crisp autumn mornings of October through the blooming spring of May, offering clear blue skies ideal for exploring the Top Tourist Places in Nagaland. For couples seeking an offbeat, deeply romantic escape, a Nagaland Honeymoon Package provides an unparalleled backdrop—from the misty, cobblestone alleyways of Asia’s first green village, Khonoma, to the ethereal sunrise vistas over the high-altitude terrace cultivation fields of Pfutsero. Photography enthusiasts and families will find endless inspiration across popular Instagram locations, including the historic Kisama Heritage Village, the solemn Kohima War Cemetery, and the beautifully preserved traditional log-drum houses of Mokokchung. Whether your travel desires gravitate toward tasting the fiery ghost chili (Raja Mircha), hiking pristine mountain crests, shopping for exquisitely woven tribal shawls, or engaging in profound storytelling sessions with village elders, these exclusive TRAGUIN Nagaland Packages seamlessly weave luxury with raw authenticity. TRAGUIN Premium Holidays • Nagaland Explorer",
        seo_title='NL-003 | Nagaland Explorer: The Ultimate Horizon | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Nagaland package (NL-003 / TRAGUIN-NL-003): Dimapur • Kohima • Khonoma • Pfutsero • Mokokchung with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: DIMAPUR TO KOHIMA: ASCENT TO THE HIGHLANDS OF THE ANGAMI', 1),
            _ih('Day 02: KOHIMA & KISAMA: VALOR, HERITAGE, AND ICONIC LANDMARKS', 2),
            _ih('Day 03: EXCURSION TO KHONOMA: ASIA’S FIRST LEGENDARY GREEN VILLAGE', 3),
            _ih('Day 04: KOHIMA TO PFUTSERO: THE MISTY REALM OF THE CHAKHESANG', 4),
            _ih('Day 05: PFUTSERO TO MOKOKCHUNG: JOURNEY TO THE LAND OF THE AO NAGA', 5),
            _ih('Day 06: UNVEILING MUNGYACHONG & UNGMA: THE CULTURAL ANCHORS', 6),
            _ih('Day 07: MOKOKCHUNG TO DIMAPUR: FAREWELL TO THE LAND OF THE WARRIORS', 7),
            _ih('TRAGUIN Signature Experience: Private, arranged audiences with village elders in Khonoma, preserving', 8),
            _ih('Curated by TRAGUIN Experts: Handcrafted itineraries designed to highlight authentic tribal lifestyle without', 9),
            _ih('Personalized Assistance: Dedicated destination managers monitoring road conditions, check-ins, and comfort', 10)
        ],
        days=[
            _day(
                1,
                'DIMAPUR TO KOHIMA: ASCENT TO THE HIGHLANDS OF THE ANGAMI',
                (
                    'Your extraordinary Nagaland Sightseeing voyage begins with a warm traditional welcome at Dimapur Airport by your dedicated TRAGUIN tour ambassador. Board your premium luxury SUV and begin a highly scenic drive ascending into the mist-draped Naga Hills toward the capital city of Kohima. As the bustling plains give way to crisp, pine-scented mountain air, your chauffeur will pause at handpicked panoramic viewpoints for stunning photography opportunities overlooking the deep, terraced valleys. Upon arrival in Kohima, check into your ultra-premium luxury accommodation. Spend your evening relaxing or enjoying an optional stroll through the vibrant local night market to experience the unique culinary scene and welcoming hospitality of the local community.'
                ),
                [
                    'SIGHTSEEING INCLUDED: Scenic Hill Drive, Patkai Range Viewpoints, Kohima Heritage Orientation.',
                    'EVENING EXPERIENCE: Leisurely exploration of local cafe culture and artisan crafts.',
                    'OVERNIGHT STAY: Kohima (Premium Luxury Boutique Lodge)',
                    'MEALS INCLUDED: Dinner',
                ],
            ),
            _day(
                2,
                'KOHIMA & KISAMA: VALOR, HERITAGE, AND ICONIC LANDMARKS',
                (
                    'Immerse yourself deeply in history today with a comprehensive tour of the most iconic Top Tourist Places in Nagaland. Begin at the beautifully curated Kohima War Cemetery, a poignant World War II memorial situated on the slopes of Garrison Hill, dedicated to the brave Allied soldiers who halted the advancing forces. Afterward, dive into the cultural heart of the state at Kisama Heritage Village, the renowned venue of the annual worldwide Hornbill Festival. Walk through architectural models of traditional tribal houses (Morungs), admire towering ceremonial gateways, and marvel at intricate wood carvings. In the afternoon, enjoy a premium culinary lunch experience featuring authentic, softly spiced organic local dishes prepared by a trained master chef.'
                ),
                [
                    'SIGHTSEEING INCLUDED: Kohima War Cemetery, Kisama Tribal Heritage Village, State Museum.',
                    'OPTIONAL ACTIVITIES: Specialized cultural photography session with traditional attire elements.',
                    'EVENING EXPERIENCE: Interactive session with a local historian over gourmet organic tea.',
                    'OVERNIGHT STAY: Kohima (Premium Luxury Boutique Lodge)',
                    'MEALS INCLUDED: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'EXCURSION TO KHONOMA: ASIA’S FIRST LEGENDARY GREEN VILLAGE',
                (
                    "Embark on an unforgettable excursion to Khonoma Village, a historic 700-year-old settlement celebrated globally as Asia's first official green village. This bastion of the Angami tribe is famous for its pioneering community-led wildlife conservation projects and historic resistance against British colonial forces. Stroll along ancient stone pathways through defensive village gates, traditional granaries, and towering morungs. Engage in a rare, deeply personal conversation with village elders to hear legendary tales of ancestral valor. Take in the breathtaking views of the step-cultivation farms below, which form one of the most stunning Instagram locations in Northeast India, showcasing sustainable indigenous farming at its finest."
                ),
                [
                    'SIGHTSEEING INCLUDED: Khonoma Green Village, Fort Gates, Ancient Terraced Agriculture Viewpoints.',
                    'OPTIONAL ACTIVITIES: Short guided nature trail through the surrounding community conservation forest.',
                    'EVENING EXPERIENCE: Traditional folk singing performance arranged exclusively for you.',
                    'OVERNIGHT STAY: Kohima (Premium Luxury Boutique Lodge)',
                    'MEALS INCLUDED: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'KOHIMA TO PFUTSERO: THE MISTY REALM OF THE CHAKHESANG',
                (
                    'Today, your Luxury Nagaland Holiday takes you to Pfutsero, the highest inhabited town in Nagaland, situated at an altitude of over 2,100 meters above sea level. This hidden gem in Phek district offers crisp alpine temperatures and panoramic views of the Eastern Himalayas. Journey past cascading mountain streams and dense pine forests to explore this cultural capital of the Chakhesang tribe. Visit Glory Peak for an unparalleled view of Mount Saramati on a clear day. Walk through sacred cherry blossom avenues and organic fruit orchards while learning about the sophisticated indigenous water-harvesting systems that have sustained these high-altitude communities for centuries.'
                ),
                [
                    'SIGHTSEEING INCLUDED: Glory Peak Viewpoint, Pfutsero Town Walk, High-Altitude Organic Orchards.',
                    'OPTIONAL ACTIVITIES: Early morning sunrise trek to the peak for spectacular landscape photography.',
                    'EVENING EXPERIENCE: Warm bonfire gathering featuring slow-roasted local delicacies and storytelling.',
                    'OVERNIGHT STAY: Pfutsero (Premium Luxury Eco-Retreat)',
                    'MEALS INCLUDED: Breakfast & Dinner',
                ],
            ),
            _day(
                5,
                'PFUTSERO TO MOKOKCHUNG: JOURNEY TO THE LAND OF THE AO NAGA',
                (
                    'Following a serene mountain breakfast, depart northward toward Mokokchung, the vibrant cultural and intellectual heartland of the proud Ao Naga tribe. This scenic route takes you through changing landscapes, passing emerald tea estates and quiet hillside settlements. Mokokchung is celebrated for its preservation of community traditions, beautiful architecture, and pristine natural beauty. Upon arrival, check into your handpicked, premium resort. Spend your evening relaxing in the tranquil gardens, enjoying the gentle mountain breeze, and looking out over the rolling hills of the surrounding districts.'
                ),
                [
                    'SIGHTSEEING INCLUDED: Inter-district Scenic Drive, Mokokchung Town Center, Panoramic Valley Overlooks.',
                    'OPTIONAL ACTIVITIES: Visit local textile weavers to see the intricate process of creating tribal motifs.',
                    'EVENING EXPERIENCE: Fine dining experience featuring fusion Ao tribal cuisine.',
                    'OVERNIGHT STAY: Mokokchung (Handpicked Premium Resort)',
                    'MEALS INCLUDED: Breakfast & Dinner',
                ],
            ),
            _day(
                6,
                'UNVEILING MUNGYACHONG & UNGMA: THE CULTURAL ANCHORS',
                (
                    'Spend a fascinating day exploring Mungyachong and Ungma, the largest and oldest traditional villages of the Ao tribe. Walk through heritage pathways to see the massive ceremonial log-drums, which were historically beaten to signal alarms or celebrate major village victories. Meet local craftspeople specializing in bamboo architecture and basket weaving. Later, visit the beautiful Mokokchung Park for a peaceful walk among seasonal blooms, offering panoramic views across the town. This comprehensive day of exploration is a highlight of your Best Nagaland Tour Package experience, offering a deep connection to the living culture of the region.'
                ),
                [
                    'SIGHTSEEING INCLUDED: Ungma Heritage Village, Traditional Log-Drums, Mokokchung Town Park.',
                    'OPTIONAL ACTIVITIES: Private bead-making workshop with a master artisan.',
                    'EVENING EXPERIENCE: Farewell dinner celebrating your journey with traditional music elements.',
                    'OVERNIGHT STAY: Mokokchung (Handpicked Premium Resort)',
                    'MEALS INCLUDED: Breakfast & Dinner',
                ],
            ),
            _day(
                7,
                'MOKOKCHUNG TO DIMAPUR: FAREWELL TO THE LAND OF THE WARRIORS',
                (
                    'After a leisurely breakfast, bid farewell to the majestic hills as you begin your comfortable descent back toward Dimapur. Enjoy the changing scenery as you return to the plains, carrying fond memories of spectacular landscapes, rich tribal heritage, and warm hospitality. Your driver will transfer you directly to Dimapur Airport in time for your onward flight, concluding your premium Nagaland Family Tour experience with TRAGUIN.'
                ),
                [
                    'SIGHTSEEING INCLUDED: Scenic Foothill Drive, Dimapur Historical Relics (Time Permitting).',
                    'MEALS INCLUDED: Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Sakhrie House / Similar | Pfutsero Tourist Lodge | Hotel Whispering Winds',
                'Kohima | Pfutsero | Mokokchung',
                '3N Kohima|1N Pfutsero|2N Mokokchung',
                'Deluxe',
                'Executive Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: The Sakhrie House / Similar | Pfutsero Tourist Lodge | Hotel Whispering Winds | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Razhu Pru Heritage Home | Glory Peak Eco-Lodge | Mokokchung Resort',
                'Kohima | Pfutsero | Mokokchung',
                '3N Kohima|1N Pfutsero|2N Mokokchung',
                'Premium',
                'Luxury Suite',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Razhu Pru Heritage Home | Glory Peak Eco-Lodge | Mokokchung Resort | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Kohima Camp / Tanhir Estate | Pfutsero High-Altitude Retreat | The Whispering Ridge Luxury',
                'Kohima | Pfutsero | Mokokchung',
                '3N Kohima|1N Pfutsero|2N Mokokchung',
                'Luxury',
                'Premium Villa',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Kohima Camp / Tanhir Estate | Pfutsero High-Altitude Retreat | The Whispering Ridge Luxury | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Ultimate Hornbill Luxury Pavilion | Private Luxury Chalet Pfutsero | Elite Ao Heritage Mansion',
                'Kohima | Pfutsero | Mokokchung',
                '3N Kohima|1N Pfutsero|2N Mokokchung',
                'Ultra Luxury',
                'Signature Suite',
                'Royal MAPAI Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Ultimate Hornbill Luxury Pavilion | Private Luxury Chalet Pfutsero | Elite Ao Heritage Mansion | Royal MAPAI Plan',
            )
        ],
        inclusions=[
            _inc_included("Premium Accommodations: 06 Nights' stay in handpicked, top-rated luxury properties, boutique heritage homes, and luxury eco-retreats.", 1),
            _inc_included('Gourmet Meal Plan: Daily premium breakfasts and curated multi-course traditional/continental dinners across all destinations.', 2),
            _inc_included('Luxury Private Transportation: Exclusive use of a premium 4x4 high-clearance SUV (Toyota Innova Crysta) for all transfers, excursions, and inter-district travel.', 3),
            _inc_included('Expert Guided Expeditions: Services of a highly knowledgeable, English-speaking local cultural ambassador and expert tribal guides.', 4),
            _inc_included('Exclusive Experiences: Private audiences with village elders, traditional folk music sessions, and artisan craft demonstrations.', 5),
            _inc_included('Welcome Amenities: Premium organic welcome kits, mineral water platters daily, and signature local tea tasting baskets.', 6),
            _inc_included('Hassle-Free Formalities: Complete assistance with securing Inner Line Permits (ILP) and all required local community entry permissions.', 7),
            _inc_included('TRAGUIN Support: Dedicated 24/7 remote concierge support and emergency assistance throughout your journey.', 8),
            _inc_excluded('Airfare & Railfare: Domestic or international flights to and from Dimapur Airport.', 9),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, premium alcoholic beverages, and optional tipping for drivers or guides.', 10),
            _inc_excluded('Entry Tickets & Camera Fees: Monument entry charges, national park fees, and professional camera/drone permits.', 11),
            _inc_excluded('Optional Activities: Unspecified trail excursions, specialized workshops, or personal shopping items.', 12),
            _inc_excluded('Insurance: Comprehensive travel, medical, or baggage loss insurance policies.', 13),
            _inc_excluded('Unforeseen Expenses: Costs resulting from flight delays, weather-related roadblocks, or political strikes.', 14),
        ],
    )
    return package, itinerary

def build_nl_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'NL-004'
    tour_code = 'TRG-NAGA-NL004-2026'
    title = 'Kohima Experience • Mystical Tribal Heritage • Pristine Hills'
    duration = '04 Nights / 05 Days'
    slug = 'nl-004-kohima-experience-mystical-tribal-heritage-pristine-hills'
    itin_slug = 'nl-004-kohima-experience-mystical-tribal-heritage-pristine-hills-itinerary'
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
            _ph('Serial code NL-004 | TRAGUIN tour code TRG-NAGA-NL004-2026', 1),
            _ph('State / Country: Nagaland / India | Category: Premium Family Tour', 2),
            _ph('Destinations: Dimapur • Kohima • Khonoma • Kisama', 3),
            _ph('Ideal for: Family / Culture Enthusiasts', 4),
            _ph('Best season: October to May', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle / Meals: Premium Toyota Innova Crysta / MAPAI (Breakfast & Dinner)', 7),
            _ph('Route: Dimapur ➔ Kohima ➔ Kisama Heritage Village ➔ Khonoma Green Village ➔ Dimapur', 8)
        ],
        moods=['Family', 'Culture', 'Heritage'],
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
        tagline='Dimapur • Kohima • Khonoma • Kisama',
        overview="Kohima Experience • Mystical Tribal Heritage • Pristine Hills 04 Nights / 05 Days Immersive Luxury Family Holiday Embark on an extraordinary cultural journey with the Best Nagaland Tour Package meticulously curated for high-end families. This bespoke Nagaland Family Tour takes you deep into the heart of the ancient Naga hills, combining unmatched hospitality, pristine misty landscapes, and deep indigenous tribal heritage. Witness the timeless allure of the legendary Angami tribes, taste exotic local TRAGUIN Premium Holidays • NL-004 delicacies, and walk through historical milestones with the signature elegance that defines a Luxury Nagaland Holiday. With TRAGUIN Packages, your family doesn't just sightsee—you immerse yourself in curated experiences that blend private luxury transportation, elite local guiding, and unparalleled accesses. Let us introduce your family to the last frontier of pristine Indian tourism.\n\nTOUR OVERVIEW\nTravel Dates: Flexible / Customisable Group / FIT: Private Family FIT Vehicle: Premium Toyota Innova Crysta Meal Plan: MAPAI (Breakfast & Dinner) Route: Dimapur ➔ Kohima ➔ Kisama Heritage Village ➔ Khonoma Green Village ➔ Dimapur TRAGUIN Curated Experience Note: Every element of this Nagaland Sightseeing journey has been handpicked by our regional destination specialists. From private culinary interactions with local Angami hosts to choosing panoramic viewing decks for photography, your premium family luxury vacation is handled with absolute attention to detail. WHY EXPERIENCE NAGALAND WITH TRAGUIN? Nagaland is a mesmerizing tapestry of misty mountain peaks, intense warrior heritage, and incredible emerald valleys. Selecting the perfect Nagaland Honeymoon Package or Nagaland Family Tour demands an intimate understanding of local schedules and luxury stays. TRAGUIN Nagaland Packages provide exclusive security, unparalleled luxury vehicle comfort on mountain passes, and seasoned local guides who transform standard sightseeing into unforgettable stories. The Top Tourist Places in Nagaland span across the soulful Kohima War Cemetery, the architectural marvels of Kisama Heritage Village, and the globally awarded green fields of Khonoma Village. The Best Time to Visit Nagaland is generally between October and May when the skies open up to clear panoramic views of the Dzüko Valley foothills. From capturing striking portraits of authentic Naga attire to tasting organic organic teas at artisanal mountain cafes, this Premium Nagaland Experience guarantees a profound impact on every discerning traveler.",
        seo_title='NL-004 | Kohima Experience | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Nagaland package (NL-004 / TRG-NAGA-NL004-2026): Dimapur • Kohima • Khonoma • Kisama with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: TRAGUIN PREMIUM HOLIDAYS • NL-004 ARRIVAL IN DIMAPUR & SCENIC DRIVE TO HISTORIC KOHIMA', 1),
            _ih('Day 02: KOHIMA SIGHTSEEING - WAR MEMORIAL, MUSEUMS & LOCAL BRAIDED MARKETS SAVOR AN EXQUISITE LOCALLY SOURCED ORGANIC BREAKFA...', 2),
            _ih('Day 03: THE CULTURAL CRADLE OF KISAMA HERITAGE VILLAGE TODAY PROMISES AN IMMERSIVE HISTORICAL FAIRYTALE AS WE TRANSFER YOU TO...', 3),
            _ih('Day 04: KHONOMA VILLAGE - THE FIRST GREEN VILLAGE OF ASIA PREPARE FOR AN AWE-INSPIRING DAY AS WE HEAD TO THE GLOBALLY CELEBRA...', 4),
            _ih('Day 05: DAY 05', 5)
        ],
        days=[
            _day(
                1,
                'TRAGUIN PREMIUM HOLIDAYS • NL-004 ARRIVAL IN DIMAPUR & SCENIC DRIVE TO HISTORIC KOHIMA',
                (
                    'Welcome to the land of the festivals! Your ultra-luxury family holiday begins as you land at Dimapur Airport. Upon arrival, you will receive a traditional, warm welcome by our senior representative representing the signature hospitality of TRAGUIN. Step into your private, plush executive vehicle and begin a deeply scenic 74 km uphill journey to the historic capital city, Kohima. As your vehicle winds up through lush subtropical pine forests, witness breathtaking landscapes and cascading waterfalls cutting through deep mountain ravines. Feel the fresh mountain air replace the plains as you transition into a truly magical altitude. Stop at handpicked viewpoints for fresh organic local pineapples and stellar photography opportunities with your family. Upon arriving in Kohima, complete a smooth, seamless check-in at your premium heritage hotel. Produce Markets. briefing by your accompanying TRAGUIN tour specialist over hot mountain tea.'
                ),
                [
                    'Sightseeing Included: Scenic Mountain Ghat Drive, Chumukedima Viewpoint stops, and Local Organic',
                    'Evening Experience: Leisurely family walk around the local neighborhood followed by a cozy orientation',
                    'Overnight Stay: Premium Luxury Stay in Kohima.',
                    'Meals Included: Welcome Drink & Gourmet Dinner.',
                ],
            ),
            _day(
                2,
                'KOHIMA SIGHTSEEING - WAR MEMORIAL, MUSEUMS & LOCAL BRAIDED MARKETS SAVOR AN EXQUISITE LOCALLY SOURCED ORGANIC BREAKFA...',
                (
                    'town. Your day begins with a highly emotional, curated walk through the globally recognized Kohima War Cemetery, a beautifully manicured memorial dedicated to the brave soldiers who halted the Japanese advance in World War II. Walk past the famous historic tennis court grounds and read the moving epitaphs that encapsulate global history. Next, dive deep into the indigenous roots of the hills with an exclusive tour of the State Museum, housing rare tribal dynamic relics, authentic traditional weapons, and majestic structural models of different Naga tribes. Conclude your daytime sightseeing at the bustling local markets where the indigenous community trades local bamboo products, fresh organic herbs, handwoven fabrics, and intricate tribal jewelry. church structure in Asia), and the vibrant Local Bazaar. family.'
                ),
                [
                    'Sightseeing Included: WWII Kohima War Cemetery, Nagaland State Museum, Kohima Cathedral (largest',
                    'Optional Activities: A private traditional loin-loom weaving demonstration arranged exclusively for your',
                ],
            ),
            _day(
                3,
                'THE CULTURAL CRADLE OF KISAMA HERITAGE VILLAGE TODAY PROMISES AN IMMERSIVE HISTORICAL FAIRYTALE AS WE TRANSFER YOU TO...',
                (
                    "showcases grand, architecturally stunning 'Morungs' (traditional communal youth dormitories) belonging to all 17 distinct major tribes of Nagaland. Your family can marvel at the magnificent woodcarvings, massive log-drums, and traditional tribal architecture up close without the bustling festival rush, allowing for a deep, tranquil, educational family experience. Your expert guide will narrate the intense folklore behind the warrior tattoos, ceremonial hornbill feathers, and majestic spears. This is the top popular Instagram location in the region, perfect for memorable family portraits in traditional backdrops. slopes of Kigwema traditional village. family photoshoot."
                ),
                [
                    'Sightseeing Included: Full exploration of Kisama Morungs, World War II Museum complex, and the scenic',
                    'Optional Activities: Renting authentic tribal ceremonial shawls and headgears for an exclusive professional',
                    'Evening Experience: A private bonfire and storytelling session at the village outskirts.',
                    'Overnight Stay: Kohima.',
                    'Meals Included: Breakfast & Authentic Naga-Style Dinner.',
                ],
            ),
            _day(
                4,
                'KHONOMA VILLAGE - THE FIRST GREEN VILLAGE OF ASIA PREPARE FOR AN AWE-INSPIRING DAY AS WE HEAD TO THE GLOBALLY CELEBRA...',
                (
                    'and breathtaking stepped terraced agriculture. Nestled amidst pristine, mist-shrouded green mountains, Khonoma tells a tale of incredible defiance against British colonial forces and a subsequent transition to absolute global conservation.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary for Day 4.',
                ],
            ),
            _day(
                5,
                'DAY 05',
                (
                    'Bid farewell to the mystical hills of Northeast India. After a leisurely final morning breakfast looking out at the majestic valleys, complete your checkout. Pack your premium souvenirs, intricate wooden artifacts, and beautiful handwoven stoles before boarding your private vehicle. Enjoy a highly comfortable downhill drive back to Dimapur Airport. Your dedicated TRAGUIN logistics expert will assist you right up to the airport terminal gate, ensuring your departure is stress-free. Return home with revitalized family bonds and a treasure trove of unforgettable memories from your premium Himalayan holiday. timings).'
                ),
                [
                    'DEPARTURE: VIA DIMAPUR - COLLECTING FOREVER MEMORIES',
                    'Sightseeing Included: En-route brief stop at the ancient Kachari ruins in Dimapur (subject to departure flight',
                    'Meals Included: Full Buffet Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Vivor / Hotel Razhuprat',
                'Kohima',
                '4N Kohima',
                'Deluxe',
                'Executive Deluxe Room',
                'MAPAI Plan',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Vivor / Hotel Razhuprat | MAPAI Plan',
            ),
            _hotel(
                'The Heritage Kohima / Niraamaya Retreats',
                'Kohima',
                '4N Kohima',
                'Premium',
                'Premium Valley View Room',
                'MAPAI Plan',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Heritage Kohima / Niraamaya Retreats | MAPAI Plan',
            ),
            _hotel(
                'Lazeo Hill Crest Resort / Dzüko Valley Luxury Eco Lodge',
                'Kohima',
                '4N Kohima',
                'Luxury',
                'Luxury Suite / Royal Villa',
                'MAPAI Plan',
                5,
                3,
                description='OPTION 03 – LUXURY: Lazeo Hill Crest Resort / Dzüko Valley Luxury Eco Lodge | MAPAI Plan',
            ),
            _hotel(
                'Ultimate Tented Suite Concept (Bespoke Curated Private Setup)',
                'Kohima',
                '4N Kohima',
                'Ultra Luxury',
                'Signature Imperial Royal Tent',
                'All Inclusive Premium',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Ultimate Tented Suite Concept (Bespoke Curated Private Setup) | All Inclusive Premium',
            )
        ],
        inclusions=[
            _inc_included('04 Nights premium handpicked hotel stay in Kohima.', 1),
            _inc_included('Daily premium multi-cuisine breakfasts and gourmet dinners.', 2),
            _inc_included('Exclusive TRAGUIN Signature Angami Home Lunch in Khonoma.', 3),
            _inc_included('Chauffeur-driven private Toyota Innova Crysta for all transfers.', 4),
            _inc_included('Dedicated English-speaking certified local cultural specialist guide.', 5),
            _inc_included('Inner Line Permits (ILP) documentation for Indian domestic tourists.', 6),
            _inc_included('Premium welcome amenities, fresh organic fruit baskets on arrival.', 7),
            _inc_included('All parking fees, luxury toll taxes, driver allowances, and state entry taxes.', 8),
            _inc_included('24/7 dedicated backend guest assistance via senior TRAGUIN advisors.', 9),
            _inc_excluded('Airfares, train bookings, or helicopter transfer costs to Dimapur.', 10),
            _inc_excluded('Monument entry fees, camera passes, or local museum tickets.', 11),
            _inc_excluded('Optional adventure hikes or custom professional photo shoots.', 12),
            _inc_excluded('Laundry, alcoholic beverages, minibar usages, and telephone bills.', 13),
            _inc_excluded('Mandatory travel insurance or medical evacuation cover costs.', 14),
            _inc_excluded('Tips or gratitude gestures for accompanying drivers and local guides.', 15),
            _inc_excluded('Any expenses incurred due to unexpected roadblocks or flight delays.', 16),
        ],
    )
    return package, itinerary

def build_nl_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'NL-005'
    tour_code = 'TRAGUIN-NAGA-LUX-005'
    title = 'Premium Nagaland Experience'
    duration = '05 Nights / 06 Days'
    slug = 'nl-005-premium-nagaland-experience'
    itin_slug = 'nl-005-premium-nagaland-experience-itinerary'
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
            _ph('Serial code NL-005 | TRAGUIN tour code TRAGUIN-NAGA-LUX-005', 1),
            _ph('State / Country: Nagaland / India | Category: Luxury Travel / Tribal Heritage', 2),
            _ph('Destinations: Dimapur • Kohima • Khonoma • Kigwema • Touphema', 3),
            _ph('Ideal for: Connoisseurs of Culture, Luxury Seekers, Honeymooners & Families', 4),
            _ph('Best season: October to May (Featuring the Iconic Hornbill Festival in December)', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle / Meals: Premium Toyota Innova Crysta / Full Board (Premium Breakfast, Curated Lunches & Epicurean Dinners)', 7),
            _ph('Route: Dimapur Arrival • Kohima • Khonoma • Kigwema • Touphema • Dimapur Departure', 8)
        ],
        moods=['Culture', 'Luxury', 'Heritage'],
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
        tagline='Dimapur • Kohima • Khonoma • Kigwema • Touphema',
        overview="Tour Vehicle Allocation: Premium Toyota Innova Crysta (All Transfers & Sightseeing) Meal Strategy: Full Board (Premium Breakfast, Curated Lunches & Epicurean Dinners) Base Route: Dimapur Arrival • Kohima • Khonoma • Kigwema • Touphema • Dimapur Departure TRAGUIN Curated Experience Note: Every moment of this itinerary is backed by 24/7 dedicated local concierge assistance, handpicked premium accommodations, private tribal audience privileges, and elite experiential narrative guiding. DESTINATION SHOWCASE & LUXURY INSIGHTS Nagaland, long celebrated as one of the ultimate cultural frontiers on earth, is a mosaic of sixteen unique indigenous tribes, each safeguarding centuries-old customs, vibrant attires, and fascinating folklore. Choosing our high-end Nagaland Family Tour or a dedicated, romance-infused Nagaland Honeymoon Package grants access to a realm where pristine organic gastronomy, vibrant festivals, and emerald green valleys gracefully collide. During this premium expedition, you will immerse yourself deeply into the Top Tourist Places in Nagaland. From the historic, poignant capital of Kohima to Asia’s first premier green village, Khonoma, every stop is selected to offer profound cultural substance. Photograph the magnificent traditional Angami village gates, savor authentic organic delicacies, and trace the historic paths of the Second World War. Whether you are traveling during the world- famous Hornbill Festival or seeking a serene, mist-veiled sanctuary during the Best Time to Visit Nagaland, this destination offers rich visual and emotional rewards. Capture timeless moments at popular Instagram locations, engage with tribal elders, and submerge your senses completely into an unforgettable cultural masterpiece. THE CURATED DAILY ITINERARY ARRIVAL IN DIMAPUR & SCENIC PRIVATE TRANSFER TO KOHIMA\n\nTOUR OVERVIEW\nThis premium, tailor-made FIT itinerary provides a flawless blend of comfort, privacy, and profound experiential exploration across Nagaland's most legendary heritage sites. TRA GUIN TRAGUIN Premium Holidays • NL-005 Travel Profile: Customizable Private Luxury FIT Tour Vehicle Allocation: Premium Toyota Innova Crysta (All Transfers & Sightseeing) Meal Strategy: Full Board (Premium Breakfast, Curated Lunches & Epicurean Dinners) Base Route: Dimapur Arrival • Kohima • Khonoma • Kigwema • Touphema • Dimapur Departure TRAGUIN Curated Experience Note: Every moment of this itinerary is backed by 24/7 dedicated local concierge assistance, handpicked premium accommodations, private tribal audience privileges, and elite experiential narrative guiding. DESTINATION SHOWCASE & LUXURY INSIGHTS Nagaland, long celebrated as one of the ultimate cultural frontiers on earth, is a mosaic of sixteen unique indigenous tribes, each safeguarding centuries-old customs, vibrant attires, and fascinating folklore. Choosing our high-end Nagaland Family Tour or a dedicated, romance-infused Nagaland Honeymoon Package grants access to a realm where pristine organic gastronomy, vibrant festivals, and emerald green valleys gracefully collide. During this premium expedition, you will immerse yourself deeply into the Top Tourist Places in Nagaland. From the historic, poignant capital of Kohima to Asia’s first premier green village, Khonoma, every stop is selected to offer profound cultural substance. Photograph the magnificent traditional Angami village gates, savor authentic organic delicacies, and trace the historic paths of the Second World War. Whether you are traveling during the world- famous Hornbill Festival or seeking a serene, mist-veiled sanctuary during the Best Time to Visit Nagaland, this destination offers rich visual and emotional rewards. Capture timeless moments at popular Instagram locations, engage with tribal elders, and submerge your senses completely into an unforgettable cultural masterpiece. THE CURATED DAILY ITINERARY ARRIVAL IN DIMAPUR & SCENIC PRIVATE TRANSFER TO KOHIMA",
        seo_title='NL-005 | Premium Nagaland Experience | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Nagaland package (NL-005 / TRAGUIN-NAGA-LUX-005): Dimapur • Kohima • Khonoma • Kigwema • Touphema with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DIMAPUR & SCENIC PRIVATE TRANSFER TO KOHIMA', 1),
            _ih('Day 02: KOHIMA SIGHTSEEING: WORLD WAR II HERITAGE & TRIBAL IDENTITY', 2),
            _ih('Day 03: THE CRADLE OF CONSERVATION: KHONOMA GREEN VILLAGE EXPEDITION', 3),
            _ih('Day 04: LIVING TRADITIONS OF KIGWEMA & KISAMA HERITAGE COMPLEX', 4),
            _ih('Day 05: JOURNEY TO NORTHERN CULTURAL LANDMARKS & TOUPHEMA HERITAGE VILLAGE', 5),
            _ih('Day 06: SCENIC RETURN JOURNEY TO DIMAPUR & HOMEWARD DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DIMAPUR & SCENIC PRIVATE TRANSFER TO KOHIMA',
                (
                    'Your extraordinary journey begins the moment you touch down at Dimapur Airport. A dedicated private luxury transport coordinator awaits you at the arrival terminal to provide a warm traditional welcome. As you settle into your plush private vehicle, you will transition from the bustling plains of Dimapur into a scenic, climbing journey toward the historic capital city, Kohima, situated 1,444 meters above sea level. This breathtaking route passes along winding mountain roads, mist-shrouded gorges, and colorful local markets filled with organic mountain produce. Take advantage of exclusive photography stops arranged along the route to capture the emerald slopes. Upon reaching your handpicked premium accommodation in Kohima, complete a private check-in process and enjoy a specially prepared welcome high-tea featuring regional infusions. Scenic valley driving, stopover at the vibrant Chumoukedima eco-market, and initial orientation drive of historic Kohima. Bespoke in-room therapeutic massage or a private evening briefing with a local cultural historian.'
                ),
                [
                    'Sightseeing Included',
                    'Optional Activities',
                ],
            ),
            _day(
                2,
                'KOHIMA SIGHTSEEING: WORLD WAR II HERITAGE & TRIBAL IDENTITY',
                (
                    'Dedated entirely to exploring the Top Tourist Places in Kohima, today offers a deep look into the historic forces that shaped the region. Following a premium gourmet breakfast, your private guide will escort you to the beautifully terraced Kohima World War II Cemetery. Located on the historic slopes of Garrison Hill, this sacred site honors the brave soldiers who halted the advancing forces during the pivotal Battle of Kohima in 1944. Stand quietly before the legendary bronze memorial inscription: "When you go home, tell them of us and say, for your tomorrow, we gave our today." Afterwards, enjoy an exclusive private tour of the Nagaland State Museum, which houses an unparalleled collection of ancient tribal weaponry, ceremonial attire, and rare archaeological relics. In the afternoon, explore the bustling Kohima Local Market, a sensory-rich market where local traders showcase organic forest produce, traditional ingredients, and unique indigenous delicacies. Kohima World War II Cemetery, Nagaland State Museum, Garrison Hill, and the main Kohima Local Market. A private culinary demonstration focusing on the delicate art of wood-fire smoking and local organic bamboo-shoot infusions. Premium Luxury Heritage Stay / Luxury Eco Resort, Kohima. Breakfast, Lunch & Dinner. THE CRADLE OF CONSERVATION: KHONOMA GREEN VILLAGE EXPEDITION'
                ),
                [
                    'Sightseeing Included',
                    'Evening Experience',
                    'Overnight Stay',
                    'Meals Included',
                ],
            ),
            _day(
                3,
                'THE CRADLE OF CONSERVATION: KHONOMA GREEN VILLAGE EXPEDITION',
                (
                    "Today features an immersive journey to the historic village of Khonoma, situated 20 kilometers from Kohima. Renowned globally as Asia's premier green village, Khonoma is home to the Angami tribe, who made history by banning all logging and hunting to preserve their rich biodiversity. Enter through the intricately carved traditional wooden gates, where village elders will share stories of ancestral resistance against British colonial forces. Walk along clean stone pathways, observe ancient fortress walls, and view precision alder wood cultivation systems designed to sustain soil fertility naturally. Your private guide will lead you to beautiful vantage points overlooking ancient agricultural terraces carved painstakingly into the steep mountainsides. Enjoy a specially prepared, organic farm-to-table lunch served inside a traditional Angami homestead, showcasing fresh wild herbs and locally harvested grain."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary for Day 3.',
                ],
            ),
            _day(
                4,
                'LIVING TRADITIONS OF KIGWEMA & KISAMA HERITAGE COMPLEX',
                (
                    "Begin your morning with a scenic drive to Kigwema, an ancient Angami village that preserves classic tribal architecture. Walk among historic houses adorned with impressive wooden hornbill carvings, which symbolize prestige, prosperity, and valor. Engage with local basket weavers and see firsthand how traditional textiles are woven with deep precision. Next, visit the nearby Kisama Heritage Village, the expansive, permanent venue for the legendary annual Hornbill Festival. Explore the beautifully built 'Morungs'—traditional tribal bachelor dormitories representing each of Nagaland's sixteen major tribes. Your guide will explain the unique architectural styles, decorative motifs, and cultural traditions of each tribe, providing a comprehensive overview of the region's rich diversity. Kigwema Village walk, Kisama Heritage Complex, traditional tribal Morungs, and the World War II Museum at Kisama. A private folk music showcase featuring traditional stringed instruments and storytelling by tribal youth. Premium Luxury Heritage Stay / Luxury Eco Resort, Kohima. Breakfast, Lunch & Dinner. JOURNEY TO NORTHERN CULTURAL LANDMARKS & TOUPHEMA HERITAGE VILLAGE"
                ),
                [
                    'Sightseeing Included',
                    'Evening Experience',
                    'Overnight Stay',
                    'Meals Included',
                ],
            ),
            _day(
                5,
                'JOURNEY TO NORTHERN CULTURAL LANDMARKS & TOUPHEMA HERITAGE VILLAGE',
                (
                    "Embark on a fascinating northern drive toward Touphema Heritage Village, a beautifully curated destination showcasing traditional Northern Angami lifestyle and architecture. Set against a dramatic mountain backdrop, Touphema features authentic, reconstructed tribal cottages designed to immerse guests in classic village life while ensuring modern comforts. Walk through the scenic village lanes, visit the local museum housing prized clan relics, and enjoy sweeping views of the surrounding valleys. In the afternoon, participate in a traditional community reception where you can sample authentic local brews like 'Zutho' (refined rice wine) and engage with community elders, who share captivating folklore and oral histories passed down through generations."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary for Day 5.',
                ],
            ),
            _day(
                6,
                'SCENIC RETURN JOURNEY TO DIMAPUR & HOMEWARD DEPARTURE',
                (
                    'Savor your final morning breakfast surrounded by the peaceful mountain air of Nagaland. Take a quiet walk to capture your final photographs of the misty valleys before your driver secures your luggage in your private luxury vehicle. Embark on a smooth, scenic return drive down to the Dimapur plains. If scheduling permits, enjoy a brief stop to browse for handcrafted souvenirs and fine woven textiles. Your driver will ensure a timely arrival at Dimapur Airport to assist with your check-in for your onward flight, concluding an extraordinary and luxurious cultural journey. En-route landscape photography stops and a brief visit to the Dimapur organic handloom center. Premium Breakfast. Dimapur Airport (DMU).'
                ),
                [
                    'Sightseeing Included',
                    'Meals Included',
                    'Departure: Point:',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Vivor / Razhu Pru (Heritage Suite) | Touphema Heritage Cottage (Standard)',
                'Kohima | Touphema',
                '4N Kohima|1N Touphema',
                'Deluxe',
                'Deluxe Room',
                'Breakfast & Dinner Included',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Vivor / Razhu Pru (Heritage Suite) | Touphema Heritage Cottage (Standard) | Breakfast & Dinner Included',
            ),
            _hotel(
                'The Heritage Dimapur / Grand Pavilion | Touphema Premium Executive Cottage',
                'Kohima | Touphema',
                '4N Kohima|1N Touphema',
                'Premium',
                'Deluxe Room',
                'Full Board (All Meals)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Heritage Dimapur / Grand Pavilion | Touphema Premium Executive Cottage | Full Board (All Meals)',
            ),
            _hotel(
                'Kohima Luxury Eco-Resort (Luxury Villa) | Touphema Royal Heritage Suite',
                'Kohima | Touphema',
                '4N Kohima|1N Touphema',
                'Luxury',
                'Deluxe Room',
                'Full Board (Curated Menus)',
                5,
                3,
                description='OPTION 03 – LUXURY: Kohima Luxury Eco-Resort (Luxury Villa) | Touphema Royal Heritage Suite | Full Board (Curated Menus)',
            ),
            _hotel(
                'Elite Tented Camp Concept / Premium Custom Resort | Elite Presidential Tribal Cottage',
                'Kohima | Touphema',
                '4N Kohima|1N Touphema',
                'Ultra Luxury',
                'Deluxe Room',
                'Bespoke Culinary & Private Chef Service',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Elite Tented Camp Concept / Premium Custom Resort | Elite Presidential Tribal Cottage | Bespoke Culinary & Private Chef Service',
            )
        ],
        inclusions=[
            _inc_included('5 Nights premium accommodation in handpicked, top-tier luxury hotels and heritage resorts.', 1),
            _inc_included('Comprehensive meal plan featuring custom breakfasts, curated lunches, and elegant evening dinners.', 2),
            _inc_included('Private transfers and dedicated sightseeing in an exclusive Toyota Innova Crysta.', 3),
            _inc_included('Accompaniment by an elite, professional local cultural guide throughout the tour.', 4),
            _inc_included('All inner line permits (ILP), regional entry documentation, and state processing fees.', 5),
            _inc_included('Bottled mineral water, premium local fruit baskets, and welcome amenities upon arrival.', 6),
            _inc_included('Exclusive private audience with tribal elders and master artisans.', 7),
            _inc_included('Complete, 24/7 remote concierge support from our executive travel desk.', 8),
            _inc_excluded('Domestic or International airfares to and from Dimapur.', 9),
            _inc_excluded('Personal expenses such as laundry, premium beverages, and telephone charges.', 10),
            _inc_excluded('Camera, video recording, or professional drone photography licensing fees.', 11),
            _inc_excluded('Optional individual activities, personal monument entry tickets, and independent excursions.', 12),
            _inc_excluded('Travel insurance policies, medical expenses, and emergency evacuation costs.', 13),
            _inc_excluded('Gratuities, tips for drivers, local guides, or hotel hospitality personnel.', 14),
            _inc_excluded('Any costs arising from flight delays, weather disruptions, or unexpected roadblocks.', 15),
        ],
    )
    return package, itinerary

def build_nl_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'NL-006'
    tour_code = 'TRAGUIN-NL-006-PREM'
    title = 'Kohima • Khonoma Green Village • Mokokchung • Dimapur — Elegant Leisure Exploration'
    duration = '05 Nights / 06 Days'
    slug = 'nl-006-kohima-khonoma-mokokchung-elegant-leisure-exploration'
    itin_slug = 'nl-006-kohima-khonoma-mokokchung-elegant-leisure-exploration-itinerary'
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
            _ph('Serial code NL-006 | TRAGUIN tour code TRAGUIN-NL-006-PREM', 1),
            _ph('State / Country: Nagaland / India | Category: Senior Citizen Leisure', 2),
            _ph('Destinations: Dimapur • Kohima • Khonoma • Mokokchung', 3),
            _ph('Ideal for: Seniors, Families & Couples', 4),
            _ph('Best season: October to May', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle / Meals: Premium Toyota Innova Crysta / CP / MAP (Premium Buffets)', 7),
            _ph('Route: Dimapur → Kohima → Khonoma → Mokokchung', 8),
            _ph('TRAGUIN Signature Experience: Private, highly restricted cultural access to local council chambers and old', 9),
            _ph('Curated by TRAGUIN Experts: Pacing engineered perfectly for older adults, avoiding any sudden high-altitude', 10),
            _ph('Personalized Assistance: Uniformed professional greeting representatives at entry and departure nodes.', 11),
            _ph('Premium Handpicked Hotels: Properties verified strictly for room level access, running hot water, heater settings,', 12),
            _ph('During your relaxed evening trail, discover beautiful traditional Naga markets. We recommend acquiring authentic, warm Angami tribal hand-woven shawls, highly detailed decorative bamboo storage baskets, and exquisite local organic organic honey. For culinary lovers, a visit to peaceful garden cafes in Kohima to enjoy freshly brewed organic hill-coffee alongside mild traditional steamed rice cakes provides a wonderful highlight.', 13),
            _ph('Inner Line Permit (ILP): Required for all domestic travelers entering Nagaland. This is seamlessly handled in', 14)
        ],
        moods=['Family', 'Leisure', 'Culture'],
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
        tagline='Dimapur • Kohima • Khonoma • Mokokchung',
        overview='Premium Toyota Innova Crysta Route Traversed: Dimapur → Kohima → Khonoma → Mokokchung A Welcome Note from TRAGUIN: "At TRAGUIN, we understand that luxury isn\'t merely about opulent rooms; it\'s about the depth of experience, the smoothness of transit, and the emotional resonance of a place. Nagaland, with its misty blue peaks and deeply rooted clan wisdom, offers a rare, soulful connection. We welcome you to look closely at our meticulously planned itinerary where every single day unfolds as an unforgettable tapestry of comfort and discovery." DESTINATION PROFILE & SEO INSIGHTS Why plan a Premium Nagaland Experience? Known as the \'Land of Festivals\', Nagaland is one of India\'s most fascinating, culturally rich states, making it a highly sought-after paradise for discerning globetrotters. The Top Tourist Places in Nagaland blend profound historic heritage with awe-inspiring nature. From the deeply moving WWII Memorial in Kohima to Asia’s first official green village at Khonoma, every corner provides beautiful stories. Our comprehensive Nagaland Sightseeing framework targets highly searched experiences: capturing iconic Instagram- worthy vistas of terraced valleys, sampling uniquely subtle regional culinary delights adapted to gentle palates, learning the delicate weaves of Angami and Ao tribal artisans, and admiring ancestral architecture. The Best Time to Visit Nagaland spans from October to May, when the weather remains delightfully pleasant and cool, with crisp air ideal for senior wellness, cultural photography, and scenic relaxation. These exclusive TRAGUIN Nagaland Packages ensure that you participate in authentic regional traditions without straining your comfort.\n\nTOUR OVERVIEW\nWelcome to an extraordinary journey into the heart of Northeast India, beautifully orchestrated via this bespoke Luxury Nagaland Holiday. Specially designed for distinguished senior travelers seeking a relaxed pace, immersive cultural understanding, and effortless luxury, this Best Nagaland Tour Package reveals a landscape of emerald hills, rich tribal heritage, and pristine ecological wonders. Your Nagaland Family Tour is meticulously crafted with highly accessible routes, premium chauffeured luxury transportation, gentler pacing, and handpicked accommodations that perfectly celebrate traditional Naga warmth alongside modern elegant amenities. Throughout this journey, the meticulous signature touch of a dedicated TRAGUIN curated experience note ensures seamless comfort, continuous personalized assistance, and elite lifestyle management. Travel Pace: Leisurely & Senior- Friendly Meal Plan: CP / MAP (Premium Buffets) TRAGUIN Premium Luxury Holidays • NL-006 Vehicle Assigned: Premium Toyota Innova Crysta Route Traversed: Dimapur → Kohima → Khonoma → Mokokchung A Welcome Note from TRAGUIN: "At TRAGUIN, we understand that luxury isn\'t merely about opulent rooms; it\'s about the depth of experience, the smoothness of transit, and the emotional resonance of a place. Nagaland, with its misty blue peaks and deeply rooted clan wisdom, offers a rare, soulful connection. We welcome you to look closely at our meticulously planned itinerary where every single day unfolds as an unforgettable tapestry of comfort and discovery." DESTINATION PROFILE & SEO INSIGHTS Why plan a Premium Nagaland Experience? Known as the \'Land of Festivals\', Nagaland is one of India\'s most fascinating, culturally rich states, making it a highly sought-after paradise for discerning globetrotters. The Top Tourist Places in Nagaland blend profound historic heritage with awe-inspiring nature. From the deeply moving WWII Memorial in Kohima to Asia’s first official green village at Khonoma, every corner provides beautiful stories. Our comprehensive Nagaland Sightseeing framework targets highly searched experiences: capturing iconic Instagram- worthy vistas of terraced valleys, sampling uniquely subtle regional culinary delights adapted to gentle palates, learning the delicate weaves of Angami and Ao tribal artisans, and admiring ancestral architecture. The Best Time to Visit Nagaland spans from October to May, when the weather remains delightfully pleasant and cool, with crisp air ideal for senior wellness, cultural photography, and scenic relaxation. These exclusive TRAGUIN Nagaland Packages ensure that you participate in authentic regional traditions without straining your comfort.',
        seo_title='NL-006 | Kohima | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Nagaland package (NL-006 / TRAGUIN-NL-006-PREM): Dimapur • Kohima • Khonoma • Mokokchung with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: DIMAPUR TO KOHIMA', 1),
            _ih('Day 02: KOHIMA SIGHTSEEING', 2),
            _ih('Day 03: KOHIMA TO KHONOMA GREEN VILLAGE', 3),
            _ih('Day 04: KOHIMA TO MOKOKCHUNG', 4),
            _ih('Day 05: MOKOKCHUNG EXPLORATION', 5),
            _ih('Day 06: MOKOKCHUNG TO DIMAPUR DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private, highly restricted cultural access to local council chambers and old', 7),
            _ih('Curated by TRAGUIN Experts: Pacing engineered perfectly for older adults, avoiding any sudden high-altitude', 8),
            _ih('Personalized Assistance: Uniformed professional greeting representatives at entry and departure nodes.', 9)
        ],
        days=[
            _day(
                1,
                'DIMAPUR TO KOHIMA',
                (
                    'THE ROYAL WELCOME & ACCENT INTO THE MISTY HORIZONS Upon your smooth arrival at Dimapur Airport, you will be warmly received by your dedicated professional chauffeur and tour concierge representing your elite TRAGUIN Nagaland Packages. Step inside your temperature-controlled, ultra-comfortable premium vehicle to commence a highly scenic, relaxed drive uphill towards Kohima, the breathtaking capital city located at an elevation of 1,444 meters. The journey winds past lush tropical forests and cascading wayside waterfalls. We slow down at scenic vantage points for pristine photography opportunities. Upon arrival in Kohima, complete a smooth check-in at your handpicked premium resort. Sip on a warm cup of traditional organic tea while soaking in the commanding panoramic mountain views. reception. the resort.'
                ),
                [
                    'Sightseeing Included: Leisurely drive along the foothills, scenic halt at the Chümoukedima viewpoints, local welcome',
                    'Evening Experience: Private orientation briefing with your cultural expert followed by an exquisite welcome dinner at',
                    'Overnight Stay: Kohima (Premium Luxury Resort)',
                    'Meals Included: Welcome Dinner',
                ],
            ),
            _day(
                2,
                'KOHIMA SIGHTSEEING',
                (
                    "ECHOES OF VALOUR & REGAL HERITAGE CHRONICLES Savour a sumptuous breakfast before embarking on a highly enriching, leisurely paced day dedicated to iconic Kohima Sightseeing. Begin with a comfortable visit to the globally revered Kohima War Cemetery—a beautifully landscaped, highly accessible historical memorial built on the historic battlegrounds of Garrison Hill. The pristine paths allow for an effortless walk while taking in deeply moving epitaphs from World War II. Next, take a premium drive to the famous Naga Heritage Village in Kisama, the proud venue of the world-renowned Hornbill Festival. Explore meticulously preserved traditional 'Morungs' (tribal communal houses) representing 17 major tribes, offering deep insights into ancestral architecture without heavy trekking. tribal royal regalia). head chef."
                ),
                [
                    'Sightseeing Included: Kohima War Cemetery, Kisama Heritage Village, State Museum (highly accessible collection of',
                    'Optional Activities: A relaxed stroll through local handloom cooperatives to witness artisanal shawl weaving.',
                    'Evening Experience: Gourmet dining experience featuring mildly seasoned local organic delicacies curated by the',
                    'Overnight Stay: Kohima (Premium Luxury Resort)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'KOHIMA TO KHONOMA GREEN VILLAGE',
                (
                    "ASIA'S ECO PIONEER & BREATHTAKING TERRACED LANDSCAPES Today, delve deep into a genuinely Premium Nagaland Experience as we journey to Khonoma Green Village, located just 20 km from Kohima. Celebrated globally as Asia's very first official eco-village, Khonoma is the proud home of the legendary Angami tribe, known for their fierce history and modern conservation principles. Our senior-friendly route involves direct luxury vehicle access to the village square. Enjoy an inspiring, flat- surface leisurely walking tour accompanied by a respected village elder. Witness the spectacular, centuries-old terraced agricultural fields carved beautifully into the mountainsides—a premier landmark among Top Tourist Places in Nagaland. Listen to captivating emotional storytelling about ancient tribal conservation practices that protect the endangered Blyth’s Tragopan. overlooks."
                ),
                [
                    'Sightseeing Included: Khonoma Eco-Village, traditional village forts, historical stone monoliths, terraced cultivation',
                    'Evening Experience: A beautiful sunset viewing overlooking the mist-filled valleys with fresh local snacks.',
                    'Overnight Stay: Kohima (Premium Luxury Resort)',
                    'Meals Included: Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'KOHIMA TO MOKOKCHUNG',
                (
                    'JOURNEY INTO THE HEART OF AO TRIBAL CULTURE Following an early, wholesome breakfast, we check out and embark on a picturesque journey north towards Mokokchung, the vibrant cultural nerve-center of the illustrious Ao Naga tribe. To ensure complete senior citizen comfort, the driving route is split with frequent rest stops at tranquil tea estates and scenic riversides. Watch the incredible changing topographies unfold through your panoramic windows. Mokokchung is universally acclaimed for its rich folklore, deep artistic music traditions, and pristine cleanliness. Arrive by afternoon and check into your charming premier accommodation. The evening is reserved for pure relaxation to acclimatize completely to the peaceful, unhurried pace of the beautiful northern hills. square lounge. resort gardens.'
                ),
                [
                    'Sightseeing Included: Rural landscape photography halts, Tseminyu Rengma tribal border vistas, Mokokchung town',
                    'Evening Experience: An exclusive private vocal performance of traditional Ao folk lullabies and songs inside the',
                    'Overnight Stay: Mokokchung (Handpicked Luxury Boutique Stay)',
                    'Meals Included: Breakfast, Light Lunch & Dinner',
                ],
            ),
            _day(
                5,
                'MOKOKCHUNG EXPLORATION',
                (
                    "THE LIVING HISTORY OF MOPUNGCHUKET & UNGMA VILLAGES Dedicate this day of your Luxury Nagaland Holiday to experiencing some of the oldest continually inhabited villages in the region. Visit Mopungchuket Village, widely celebrated as one of the best-kept cultural secrets in the state. Walk effortlessly down paved, clean walkways bordered by perfectly manicured gardens to view the striking wooden 'Log-Drums' and cultural monuments. Later, explore Ungma Village, the largest and oldest Ao village, where old clan wisdom continues to guide modern day-to-day life. Meet with local artisans specializing in intricate bamboo craftsmanship and purchase authentic, lightweight souvenirs. This day provides the definitive emotional highlight of your immersive travel experience. studios. assortments."
                ),
                [
                    'Sightseeing Included: Mopungchuket cultural park, historical time pillars, Ungma ancient village court, local craft',
                    'Optional Activities: Interaction session with regional tribal historians over fresh organic ginger tea.',
                    'Evening Experience: A celebratory final night gala dinner with custom curated continental and authentic Naga culinary',
                    'Overnight Stay: Mokokchung (Handpicked Luxury Boutique Stay)',
                    'Meals Included: Breakfast & Gala Dinner',
                ],
            ),
            _day(
                6,
                'MOKOKCHUNG TO DIMAPUR DEPARTURE',
                (
                    'FOND FAREWELLS & UNFORGETTABLE MEMORIES Savour a relaxed breakfast surrounded by the calming morning call of the hills. Your professional chauffeur will carefully handle all luggage transfers into your premium vehicle. Enjoy a comfortable, smooth descent back down towards Dimapur. As you proceed directly to Dimapur Airport for your homeward flight, reflect upon the remarkable hospitality, breathtaking landscapes, and elite care that defined your journey. Your spectacular Nagaland Honeymoon Package or premium senior family retreat concludes beautifully, leaving you with countless unforgettable memories and stories to share for a lifetime. permitting).'
                ),
                [
                    'Sightseeing Included: Final departure scenic drive, Dimapur regional handloom market brief stopover (time-',
                    'Meals Included: Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Vivor / Equivalent | Hotel Whispering Winds',
                'Kohima | Mokokchung',
                '3N Kohima|2N Mokokchung',
                'Deluxe',
                'Executive Room',
                'MAP Plan',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Vivor / Equivalent | Hotel Whispering Winds | MAP Plan',
            ),
            _hotel(
                'The Heritage Kohima | Signature Boutique Retreat',
                'Kohima | Mokokchung',
                '3N Kohima|2N Mokokchung',
                'Premium',
                'Premium Valley View',
                'MAP Plan',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Heritage Kohima | Signature Boutique Retreat | MAP Plan',
            ),
            _hotel(
                'Dzüku Valley Resort Luxury Wing | Woodland Luxury Suite Resort',
                'Kohima | Mokokchung',
                '3N Kohima|2N Mokokchung',
                'Luxury',
                'Luxury Heritage Suite',
                'All Meals',
                5,
                3,
                description='OPTION 03 – LUXURY: Dzüku Valley Resort Luxury Wing | Woodland Luxury Suite Resort | All Meals',
            ),
            _hotel(
                'TRAGUIN Elite Partner Estate | Mokokchung Heritage Villa',
                'Kohima | Mokokchung',
                '3N Kohima|2N Mokokchung',
                'Ultra Luxury',
                'Presidential Tribal Villa',
                'Ultra Luxury VIP',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Elite Partner Estate | Mokokchung Heritage Villa | Ultra Luxury VIP',
            )
        ],
        inclusions=[
            _inc_included('Accommodation: 05 Nights in handpicked premium hotels matching senior safety rules.', 1),
            _inc_included('Meals: Nutritious daily breakfasts and curated dinners suited to requested preferences.', 2),
            _inc_included('Transfers: Dedicated private Toyota Innova Crysta for all smooth transit routes.', 3),
            _inc_included('Sightseeing: All entries to historic sites, heritage villages, and eco-parks.', 4),
            _inc_included('Assistance: Full-time 24/7 dedicated TRAGUIN support helpline.', 5),
            _inc_included('Welcome Amenities: Refreshing traditional welcome drinks and premium organic dry fruit hampers.', 6),
            _inc_included('Complimentary Experiences: Private interaction with tribal historians and village elders.', 7),
            _inc_included('Taxes: All standard luxury hospitality service taxes and inner line permit processing fees.', 8),
            _inc_excluded('Flights: Domestic or international air tickets to and from Dimapur Airport.', 9),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, premium alcoholic beverages, and tips.', 10),
            _inc_excluded('Activities: Individual optional tribal shawl weaving purchases or heavy adventure sports.', 11),
            _inc_excluded('Insurance: Comprehensive personal medical and travel cancellation insurance covers.', 12),
            _inc_excluded('Camera Charges: Special video camera or commercial photography permissions at monuments.', 13),
            _inc_excluded('Unspecified Meals: Mid-day snacks or lunches not listed explicitly in the chosen hotel plan.', 14),
        ],
    )
    return package, itinerary

def build_nl_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'NL-007'
    tour_code = 'TRAGUIN-NAGA-EDU-007'
    title = 'An Immersive Educational Expedition: Dimapur • Kohima • Khonoma Green Village'
    duration = '04 Nights / 05 Days'
    slug = 'nl-007-immersive-educational-expedition-dimapur-kohima-khonoma'
    itin_slug = 'nl-007-immersive-educational-expedition-dimapur-kohima-khonoma-itinerary'
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
            _ph('Serial code NL-007 | TRAGUIN tour code TRAGUIN-NAGA-EDU-007', 1),
            _ph('State / Country: Nagaland / India | Category: Educational Tour', 2),
            _ph('Destinations: Dimapur • Kohima • Khonoma', 3),
            _ph('Ideal for: Students & Educators', 4),
            _ph('Best season: October to May', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle / Meals: Premium Dedicated Luxury Coaches / Comprehensive Full Board', 7),
            _ph('Route: Dimapur Arrival ➔ Kohima Heritage Precincts ➔ Khonoma Eco-Sphere ➔ Dimapur Departure', 8)
        ],
        moods=['Education', 'Culture', 'Heritage'],
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
        tagline='Dimapur • Kohima • Khonoma',
        overview="AN IMMERSIVE EDUCATIONAL EXPEDITION: DIMAPUR • KOHIMA • KHONOMA GREEN VILLAGE 04 Nights / 05 Days of Curated Experiences & Academic Exploration Welcome to an extraordinary chapter of learning and exploration curated exclusively by TRAGUIN. Nagaland, a land of breathtaking landscapes, vibrant cultural heritage, and deep historical resonance, offers an unmatched educational canvas. Far beyond traditional classrooms, this premium Nagaland Family Tour and student journey uncovers the structural geography of Northeast India, the strategic geopolitical impact of WWII battles, and revolutionary socio-ecological preservation models. Let your students embark on a transformative Luxury Nagaland Holiday filled with unforgettable memories and profound cultural integration. TRAGUIN • Premium Travel & Luxury Holidays\n\nTOUR OVERVIEW\nThis bespoke educational itinerary is engineered for premier institutional groups seeking an academic yet highly engaging cultural immersion. Every asset of this itinerary, from safety logistics to field guides, represents the signature quality of TRAGUIN curated experiences. Travel Months: Custom Date Options (Ideal during the pleasant winter-to-spring semesters) Group Type: Institutional Student Cohort / School & College Educational Delegation Vehicle Fleet: Premium Dedicated Luxury Coaches (Ensuring strict transit safety regulations) Meal Plan: Comprehensive Full Board (Healthy, hygienic breakfast, lunch, and dinner tailored to student groups) Route Plan: Dimapur Arrival ➔ Kohima Heritage Precincts ➔ Khonoma Eco-Sphere ➔ Dimapur Departure TRAGUIN Safety Assurance: 24/7 Ground Assistance, First-Aid certified tour managers, and vetted premium stays.\n\nWHY CHOOSE A NAGALAND EDUCATIONAL EXPEDITION?\nNagaland serves as a living laboratory for multiple academic disciplines. Choosing the Best Nagaland Tour Package for students provides direct field insights into Anthropological studies, Botany, Environmental Conservation, and Modern World History. Top Tourist Places in Nagaland such as the Kohima War Cemetery offer profound historical analysis regarding the turning points of World War II in Asia. Meanwhile, exploring the Khonoma Green Village introduces students to South Asia's first official community-led ecological sanctuary, setting an exemplary benchmark for sustainable development studies. For photography, cultural fieldwork, and indigenous crafts, the region provides unmatched, highly educational, and deeply emotional storytelling avenues that form the core of our Premium Nagaland Experience.",
        seo_title='NL-007 | An Immersive Educational Expedition: Dimapur | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Nagaland package (NL-007 / TRAGUIN-NAGA-EDU-007): Dimapur • Kohima • Khonoma with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: GATEWAY TO THE NAGA HILLS: ARRIVAL & ARCHAEOLOGICAL INSIGHTS', 1),
            _ih('Day 02: WORLD WAR II CHRONICLES & INTELLECTUAL HERITAGE AT KISAMA', 2),
            _ih('Day 03: KHONOMA GREEN VILLAGE: THE LIVING LAB OF ECOLOGICAL CONSERVATION', 3),
            _ih('Day 04: ETHNO-BOTANY EXPEDITION & INDIGENOUS ARTISANAL CRAFTS', 4),
            _ih('Day 05: TRANSIT TO DIMAPUR: KNOWLEDGE RETROSPECTIVE & DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'GATEWAY TO THE NAGA HILLS: ARRIVAL & ARCHAEOLOGICAL INSIGHTS',
                (
                    'Your experiential academic odyssey begins upon arrival at Dimapur Airport/Railway Station, where a designated senior representative from TRAGUIN warmly welcomes the student cohort. Dimapur, the ancient historic capital of the Kachari kingdom, serves as the perfect geographical prefix to the region. The first educational milestone is a curated field visit to the Kachari Ruins (10th-century monolithic pillars). Here, students analyze medieval archaeological patterns, architectural techniques, and structural history under the guidance of a specialist local historian. After an enlightening session, the group proceeds on a scenic drive tracing the winding mountain roads up toward the misty heights of Kohima, the capital city situated at 1,444 meters above sea level. Check into your handpicked, secure premium accommodation. 16 primary Naga tribes.'
                ),
                [
                    'Nagaland Sightseeing Included: Monolithic Kachari Heritage Ruins, Dimapur Tribal Market corridor.',
                    'Evening Experience: Interactive ice-breaking briefing by the tour director highlighting the cultural landscape of the',
                    'Overnight Stay: Vetted Premium Student-Friendly Hotel/Resort in Kohima.',
                    'Meals Included: Lunch & Dinner (Served fresh, keeping nutritional requirements in check).',
                ],
            ),
            _day(
                2,
                'WORLD WAR II CHRONICLES & INTELLECTUAL HERITAGE AT KISAMA',
                (
                    'Following an early breakfast, students embark on an emotionally moving historical journey at the globally renowned Kohima War Cemetery. Maintained by the Commonwealth War Graves Commission, this site marks the definitive battlefield of the Battle of Kohima (1944). Students will engage in an interactive historiography assignment, deciphering the tactical significance of the famous "Tennis Court" engagement and analyzing the human cost of war while standing before the iconic epitaph: "When you go home, tell them of us and say, for your tomorrow, we gave our today." In the afternoon, the expedition moves to the Kisama Heritage Village, the permanent venue for the legendary annual Hornbill Festival. Students explore meticulously preserved traditional Naga Morungs (bachelor dormitories), learning about the distinct societal architecture, administrative governance systems, and rich ethnographic oral traditions of different indigenous clans. preservation.'
                ),
                [
                    'Nagaland Sightseeing Included: Kohima WWII Cemetery, State Museum, Kisama Tribal Heritage Village.',
                    'Photography Points: The panoramic terraced view from Kisama amphitheater, Garrison Hill historical coordinates.',
                    'Evening Experience: Panel discussion with a local community elder discussing tribal folklore and oral',
                    'Overnight Stay: Kohima.',
                    'Meals Included: Breakfast, Lunch, and Dinner.',
                ],
            ),
            _day(
                3,
                'KHONOMA GREEN VILLAGE: THE LIVING LAB OF ECOLOGICAL CONSERVATION',
                (
                    "Today marks the core ecological pillar of the TRAGUIN Nagaland Packages. We depart for Khonoma Green Village, an ancient Angami settlement celebrated as South Asia's premier eco-village. This day serves as a practical, highly immersive case study for environmental science, biodiversity management, and agrarian sustainability. Students meet local conservationists to learn how the village banned commercial logging and hunting, creating the 25 sq. km Khonoma Nature Conservation and Tragopan Sanctuary. A soft trek through the village allows students to witness brilliant engineering feats, including centuries-old alder-tree agricultural practices and sophisticated step-terrace water management networks. The emotional storytelling of how a fierce hunting tribe transitioned into dedicated guardians of nature will leave a lifelong impact on young minds. Conservation Sanctuary."
                ),
                [
                    "Nagaland Sightseeing Included: Khonoma Fort, Step-cultivation fields, Traditional Weaver's Hub, Nature",
                    'Optional Activities: Group field-mapping or botanical listing exercise inside the community reserve.',
                    'Overnight Stay: Eco-Lodge / Vetted Premium Homestays in Khonoma/Kohima for true cultural integration.',
                    'Meals Included: Breakfast, Organic Traditional Lunch at Khonoma, and Dinner.',
                ],
            ),
            _day(
                4,
                'ETHNO-BOTANY EXPEDITION & INDIGENOUS ARTISANAL CRAFTS',
                (
                    'Dedicate the morning to a guided academic nature trail exploring the unique sub-tropical flora surrounding the Kohima district, highlighting regional ethno-botany and medicinal plant variants used traditionally by indigenous tribes. In the afternoon, the focus shifts to vocational skills and cultural economies. Students visit a localized handloom cooperative to learn about the intricate symbolic geometry behind Naga shawl patterns, where every stripe denotes a specific social status or merit. They will participate in a hands-on workshop demonstrating traditional bamboo and cane basketry, understanding how local forest products are sustainably converted into exquisite household utility items. presentations.'
                ),
                [
                    'Nagaland Sightseeing Included: Local Handloom Weaving Clusters, Naga Bamboo Craft Exhibition Center.',
                    'Evening Experience: Cultural bonfire night featuring traditional folk tunes, group games, and student reflection',
                    'Overnight Stay: Kohima.',
                    'Meals Included: Breakfast, Lunch, and Festive Closing Dinner.',
                ],
            ),
            _day(
                5,
                'TRANSIT TO DIMAPUR: KNOWLEDGE RETROSPECTIVE & DEPARTURE',
                (
                    "After enjoying a hearty breakfast, the group completes checkout formalities. As we smoothly descend back toward the plains of Dimapur, students participate in a structured retrospective session, consolidating their travel journals and field findings. The luxury coaches arrive timely at Dimapur Airport / Railway Station for the group's onward journey home. The expedition concludes, leaving teachers and students alike with enriched minds, newly forged bonds, a deep respect for sustainable community living, and truly unforgettable memories orchestrated flawlessly by the travel experts at TRAGUIN."
                ),
                [
                    'Meals Included: Breakfast & Packed Travel Lunch.',
                    'Departure: Transit conclusion at Dimapur outbound terminal.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Japfü / Pine Haven Group',
                'Kohima',
                '4N Kohima',
                'Deluxe',
                'Standard Twin Sharing',
                'Full Board (MAPAI / APAI)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Japfü / Pine Haven Group | Full Board (MAPAI / APAI)',
            ),
            _hotel(
                'The Heritage DC Bungalow / Equivalent',
                'Kohima',
                '4N Kohima',
                'Premium',
                'Premium Twin/Triple',
                'Full Board (APAI)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Heritage DC Bungalow / Equivalent | Full Board (APAI)',
            ),
            _hotel(
                'Naga Heritage Resort / Razhu Pris',
                'Kohima',
                '4N Kohima',
                'Luxury',
                'Executive Cohort Rooms',
                'Full Board + Snacks',
                5,
                3,
                description='OPTION 03 – LUXURY: Naga Heritage Resort / Razhu Pris | Full Board + Snacks',
            ),
            _hotel(
                'Touphema Tourist Village / Specialized Eco-Cabins',
                'Kohima',
                '4N Kohima',
                'Ultra Luxury',
                'Heritage Cottage Suites',
                'Curated Tribal Feast Board',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Touphema Tourist Village / Specialized Eco-Cabins | Curated Tribal Feast Board',
            )
        ],
        inclusions=[
            _inc_included('Safe Secure Accommodation: 04 Nights stay in verified, safety-compliant premium properties.', 1),
            _inc_included('All-Tier Meal Plans: 04 Breakfasts, 05 Lunches, and 04 Dinners planned hygienically.', 2),
            _inc_included('Luxury Ground Logistics: Dedicated deluxe coaches with experienced hill drivers for all routes.', 3),
            _inc_included('Curated Academic Sightseeing: Entry permissions to museums, heritage spots, and Khonoma eco-zones.', 4),
            _inc_included('Expert Human Resource: Dedicated TRAGUIN tour director along with certified regional historians.', 5),
            _inc_included('Institutional Privileges: Interactive student workshops, certificates of completion, and community interaction permissions.', 6),
            _inc_included('Taxes & Permissions: All inner line permits (ILP), state entry filings, and government GST overheads.', 7),
            _inc_excluded('Inbound Airfare/Rail Transit: Mainline tickets from the home institution city to Dimapur.', 8),
            _inc_excluded('Personal Student Expenses: Souvenirs, laundry, specialized telephone calls, and individual room service bills.', 9),
            _inc_excluded('Insurance Protocols: Individual travel/medical insurance covers (can be appended on request).', 10),
            _inc_excluded('Unscheduled Logistics: Deviations from the main group itinerary or unauthorized vehicle detours.', 11),
            _inc_excluded('Camera Surcharges: Video/professional DSLR recording fees at specific museum checkpoints.', 12),
        ],
    )
    return package, itinerary

def build_nl_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'NL-008'
    tour_code = 'TG-NAG-NL008'
    title = 'Dimapur • Kohima • Khonoma • Kigwema • Tuophema — Immersive Tribal Experience'
    duration = '05 Nights / 06 Days'
    slug = 'nl-008-dimapur-kohima-khonoma-kigwema-tuophema-immersive-tribal-experience'
    itin_slug = 'nl-008-dimapur-kohima-khonoma-kigwema-tuophema-immersive-tribal-experience-itinerary'
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
            _ph('Serial code NL-008 | TRAGUIN tour code TG-NAG-NL008', 1),
            _ph('State / Country: Nagaland / India | Category: Family / Tribal Exploration', 2),
            _ph('Destinations: Dimapur, Kohima, Khonoma, Kigwema, Tuophema', 3),
            _ph('Ideal for: Family Vacations, Culture Seekers', 4),
            _ph('Best season: October to May', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle / Meals: Dedicated Premium SUV (Innova Crysta) / MAPAI', 7),
            _ph('Route: Dimapur – Kohima – Khonoma – Tuophema – Dimapur', 8),
            _ph('TRAGUIN Handpicked Luxury Wilderness', 9),
            _ph('TRAGUIN Signature Experience: Private family interaction with the village elders and community leaders of', 10),
            _ph('TRAGUIN Premium Luxury Holidays', 11)
        ],
        moods=['Family', 'Tribal', 'Culture'],
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
        tagline='Dimapur, Kohima, Khonoma, Kigwema, Tuophema',
        overview='05 Nights / 06 Days Immersive Tribal Experience Venture into the mystical land of the warrior tribes with the ultimate Best Nagaland Tour Package, meticulously curated by TRAGUIN. Nestled in the far eastern frontiers of India, Nagaland unfolds as a breathtaking tapestry of emerald green hills, rich heritage, and ancient tribal customs. This exclusive Nagaland Family Tour is crafted to offer an authentic, deep dive into the lives of the Angami Nagas and other indigenous communities. Experience a true Luxury Nagaland Holiday where modern premium comforts blend seamlessly with raw, untouched cultural storytelling, leaving your family with memories that will linger for a lifetime. SERIAL CODE: NL-008 STATE / COUNTRY: Nagaland / India CATEGORY: Family / Tribal Exploration DURATION: 05 Nights / 06 Days DESTINATIONS: Dimapur, Kohima, Khonoma, Kigwema, Tuophema IDEAL FOR: Family Vacations, Culture Seekers BEST SEASON: October to May STARTING PRICE: On Request (Premium FIT) TRAGUIN TOUR CODE: TG-NAG-NL008 BUDGET CATEGORY: Premium Luxury TRAGUIN Premium Luxury Holidays\n\nTOUR OVERVIEW\nYour Handcrafted Experience Summary: Travel Month & Route: Tailored for optimal seasonal comfort spanning Dimapur – Kohima – Khonoma – Tuophema – Dimapur. Group / FIT Status: Exclusive Private Family Tour (Fully Customizable FIT). Luxury Vehicle Assigned: Dedicated Premium SUV (Innova Crysta / Luxury Segment) throughout the journey. Meal Plan: Modified American Plan (MAPAI) – Daily Premium Buffet Breakfast & Elegant Curated Dinners. TRAGUIN Curated Experience Note: This itinerary goes far beyond typical sightseeing. It includes curated interactive audiences with tribal elders, private local folklore storytelling sessions over traditional bonfires, and handpicked local culinary escorts to ensure absolute safety and ultimate comfort for your family.\n\nWHY CHOOSE A PREMIUM NAGALAND EXPERIENCE?\nA premium Nagaland Sightseeing vacation is a magnificent journey into one of India’s most exclusive cultural frontiers. Famous for its pristine eco-villages and historic war memorials, it stands out as a unique destination. The Top Tourist Places in Nagaland include the legendary green village of Khonoma and the cultural hub of Kohima, offering highly sought-after cultural insights. Whether you are seeking a deeply unique Nagaland Honeymoon Package amidst mist-covered valleys or an enriching family retreat, this region boasts incredible Instagram locations such as the panoramic terraces of Kigwema. The Best Time to Visit Nagaland aligns with its grand festivals and crisp winter months, ensuring that your TRAGUIN Nagaland Packages deliver unparalleled access to authentic tribal handlooms, local organic culinary tasting, and the captivating music that echoes through the hills. TRAGUIN Premium Luxury Holidays',
        seo_title='NL-008 | Dimapur | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Nagaland package (NL-008 / TG-NAG-NL008): Dimapur, Kohima, Khonoma, Kigwema, Tuophema with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DIMAPUR & SCENIC GATEWAY DRIVE TO KOHIMA WELCOME TO THE GATEWAY OF NORTHEAST INDIA! UPON YOUR ARRIVAL AT D...', 1),
            _ih('Day 02: WELCOME DRINK & GOURMET DINNER', 2),
            _ih('Day 03: BREAKFAST & CURATED LOCAL DINNER', 3),
            _ih('Day 04: BREAKFAST & SPECIAL TRADITIONAL LUNCH EXPERIENCE', 4),
            _ih('Day 05: BREAKFAST & DINNER', 5),
            _ih('Day 06: BREAKFAST & GRAND LOCAL TRIBAL FEAST DINNER', 6),
            _ih('TRAGUIN Handpicked Luxury Wilderness', 7),
            _ih('TRAGUIN Signature Experience: Private family interaction with the village elders and community leaders of', 8),
            _ih('TRAGUIN Premium Luxury Holidays', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DIMAPUR & SCENIC GATEWAY DRIVE TO KOHIMA WELCOME TO THE GATEWAY OF NORTHEAST INDIA! UPON YOUR ARRIVAL AT D...',
                (
                    'a spectacular, winding uphill drive toward Kohima, the legendary capital city of Nagaland. As the plains give way to breathtaking landscapes and cool mountain air, we will stop at beautiful roadside viewpoints for premium photography points. Arrive in Kohima by late afternoon and check into your handpicked premium hotel. Spend your evening relaxing and acclimatizing to the serene mountain environment. Chumukedima Foothills Viewpoints, Local Organic Fruit Markets. Leisurely stroll around the premium property followed by a cultural orientation. Kohima (Premium Luxury Hotel/Resort) Welcome Drink & Gourmet Dinner'
                ),
                [
                    'Sightseeing Included',
                    'Evening Experience',
                    'Overnight Stay',
                    'Meals Included',
                ],
            ),
            _day(
                2,
                'WELCOME DRINK & GOURMET DINNER',
                (
                    'KOHIMA SIGHTSEEING — CAPTIVATING HISTORY & WAR HEROES HISTORIC TOUR Indulge in a rich breakfast before embarking on an emotionally moving Nagaland Sightseeing tour of Kohima. Today, we visit the iconic Kohima War Cemetery, a beautifully manicured memorial dedicated to the brave soldiers who stopped the advance of the Japanese forces during WWII. Stand before the famous inscription: "When you go home, tell them of us and say, for your tomorrow, we gave our today." Later, explore the comprehensive state museum showcasing rare tribal artifacts, weapons, and traditional attire. Conclude your day exploring local artisan markets where fine Naga handicrafts are displayed. Kohima War Cemetery, Nagaland State Museum, local craft bazaars. Private guided interactions with local historians specializing in WWII history. Cafe-hopping at Kohima\'s popular creative lifestyle cafes. Kohima (Premium Luxury Hotel/Resort) Breakfast & Curated Local Dinner'
                ),
                [
                    'Sightseeing Included',
                    'Optional Activities',
                    'Evening Experience',
                    'Overnight Stay',
                    'Meals Included',
                ],
            ),
            _day(
                3,
                'BREAKFAST & CURATED LOCAL DINNER',
                (
                    'ANCIENT KIGWEMA VILLAGE IMMERSION & KISAMA HERITAGE VILLAGE This morning, your Nagaland Family Tour takes you deeper into native heritage. We drive to Kisama Heritage Village, the renowned venue of the world-famous Hornbill Festival. Marvel at the grand architecture of the Morungs (traditional youth dormitories) representing all major tribes of the state. Next, step back in time with an exclusive immersive experience in Kigwema Village, one of the oldest Angami settlements. Walk past historic houses displaying intricate wooden carvings of buffalo heads, signifying the wealth and prestige of the hosts. Kisama Heritage Complex, Kigwema Village Walk, traditional Angami Morungs. Excellent frames alongside massive wooden ceremonial gates and tribal architecture. Kohima (Premium Luxury Hotel/Resort) Breakfast & Special Traditional Lunch Experience'
                ),
                [
                    'Sightseeing Included',
                    'Photography Points',
                    'Overnight Stay',
                    'Meals Included',
                ],
            ),
            _day(
                4,
                'BREAKFAST & SPECIAL TRADITIONAL LUNCH EXPERIENCE',
                (
                    'KHONOMA GREEN VILLAGE EXCURSION — ECO-TOURISM TRIUMPH Prepare for an inspiring day as we head to Khonoma Green Village, globally acclaimed as India’s first official eco-tourism village. Renowned for its fierce historical resistance against British colonial expansion, it is now an international symbol of wildlife conservation. Explore the stunning terraced agricultural fields carved beautifully into steep mountainsides. Witness the ingenious alder-tree farming techniques and meet local craftspeople weaving remarkable bamboo baskets. This Premium Nagaland Experience provides deep respect for community-led environmental preservation. Khonoma Forts, Terraced Paddy Fields, Craft and Weaving centers. Short nature trail walk in the surrounding Khonoma Nature Conservation sanctuary. Kohima (Premium Luxury Hotel/Resort) Breakfast & Dinner'
                ),
                [
                    'Sightseeing Included',
                    'Optional Activities',
                    'Overnight Stay',
                    'Meals Included',
                ],
            ),
            _day(
                5,
                'BREAKFAST & DINNER',
                (
                    'TUOPHEMA TOURIST VILLAGE — AN AUTHENTIC NAGA HERITAGE NIGHT Check out from Kohima and travel north towards the scenic cultural enclave of Tuophema Tourist Village. Beautifully situated atop a panoramic hillock, Tuophema was established to give travelers an authentic experience of rural Naga life inside premium, comfortable heritage cottages modeled after traditional village homes. Spend your afternoon wandering through the tranquil pathways, meeting local weavers, and capturing stunning Instagram locations looking out over vast valleys. In the evening, gather around a cozy private bonfire organized exclusively for your family. Tuophema Community Village, Local museum housing ancient spears and jewelry. Traditional bonfire evening with local folk songs and storytelling elements. Tuophema Traditional Heritage Village Resort Breakfast & Grand Local Tribal Feast Dinner'
                ),
                [
                    'Sightseeing Included',
                    'Evening Experience',
                    'Overnight Stay',
                    'Meals Included',
                ],
            ),
            _day(
                6,
                'BREAKFAST & GRAND LOCAL TRIBAL FEAST DINNER',
                (
                    'TUOPHEMA TO DIMAPUR AIRPORT — DEPARTURE WITH MEMORIES UNFORGETTABLE Savor your final morning breakfast looking out over the misty mountain horizons of Nagaland. After completing checking-out procedures, enjoy a smooth, relaxed drive back down to Dimapur Airport in your private luxury vehicle. As you head to your boarding gate, carry home the fascinating history, warm hospitality, and the pristine, ancient stories of the Naga hills. Your extraordinary holiday, seamlessly designed by TRAGUIN, concludes with beautiful bonds and unforgettable family memories. En-route craft stops and Dimapur local market updates if time permits. Premium Breakfast'
                ),
                [
                    'Sightseeing Included',
                    'Meals Included',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Japfü Kohima / Similar Standard Premium',
                'Kohima',
                '4N Kohima|1N Tuophema',
                'Deluxe',
                'Executive Room',
                'MAPAI (Breakfast + Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Japfü Kohima / Similar Standard Premium | MAPAI (Breakfast + Dinner)',
            ),
            _hotel(
                'The Ultimate Frontier Resort Kohima / Similar',
                'Kohima',
                '4N Kohima|1N Tuophema',
                'Premium',
                'Luxury Suite',
                'MAPAI (Breakfast + Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Ultimate Frontier Resort Kohima / Similar | MAPAI (Breakfast + Dinner)',
            ),
            _hotel(
                'Razhu Prü Heritage Resort Kohima / Custom Selection',
                'Kohima',
                '4N Kohima|1N Tuophema',
                'Luxury',
                'Heritage Premium Suite',
                'MAPAI (Breakfast + Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Razhu Prü Heritage Resort Kohima / Custom Selection | MAPAI (Breakfast + Dinner)',
            ),
            _hotel(
                'TRAGUIN Handpicked Luxury Wilderness Camp / Premium Villas',
                'Kohima',
                '4N Kohima|1N Tuophema',
                'Ultra Luxury',
                'Signature Premium Villa',
                'MAPAI (Breakfast + Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Luxury Wilderness Camp / Premium Villas | MAPAI (Breakfast + Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 05 Nights accommodation in top-tier handpicked hotels/resorts.', 1),
            _inc_included('Gourmet Meals: Daily breakfast and dinners across properties.', 2),
            _inc_included('Luxury Transfers: Dedicated private SUV (Innova Crysta) for all routes.', 3),
            _inc_included('Curated Experiences: Specialized local tribal guides and village entrance permissions.', 4),
            _inc_included('Welcome Amenities: Personalized arrival gifts and daily packed mineral water.', 5),
            _inc_included('TRAGUIN Support: 24/7 dedicated on-ground expert remote assistance.', 6),
            _inc_excluded('Airfare: Domestic or international flights to/from Dimapur.', 7),
            _inc_excluded('Inner Line Permits (ILP): Nominal documentation charges if processed separately.', 8),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, alcoholic beverages.', 9),
            _inc_excluded('Entry Tickets: Monument entry fees, camera permits, local video charges.', 10),
            _inc_excluded('Insurance: Medical or individual travel insurance coverage.', 11),
            _inc_excluded('Optional Tours: Any activities not explicitly listed in the itinerary.', 12),
        ],
    )
    return package, itinerary

def build_nl_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'NL-009'
    tour_code = 'TRG-NAG-ADV-009'
    title = 'Dzukou Valley & Tribal Heritage Luxury Expedition'
    duration = '05 Nights / 06 Days'
    slug = 'nl-009-dzukou-valley-and-tribal-heritage-luxury-expedition'
    itin_slug = 'nl-009-dzukou-valley-and-tribal-heritage-luxury-expedition-itinerary'
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
            _ph('Serial code NL-009 | TRAGUIN tour code TRG-NAG-ADV-009', 1),
            _ph('State / Country: Nagaland / India | Category: Luxury Adventure & Trekking', 2),
            _ph('Destinations: Dimapur • Kohima • Jakhama • Dzukou Valley • Khonoma', 3),
            _ph('Ideal for: Adventure Enthusiasts, Nature Lovers, Luxury Explorers', 4),
            _ph('Best season: October to May (Treks), June-Sept (Lush Greenery)', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle / Meals: Premium SUV & All Meals Included', 7),
            _ph('Route: Dimapur → Kohima → Jakhama → Dzukou Valley → Khonoma → Dimapur', 8),
            _ph('TRAGUIN Signature Experience: Private tribal wrestling demonstration and interaction with', 9),
            _ph('Curated by TRAGUIN Experts: Custom trail mapping ensuring comfortable gradient ascents', 10),
            _ph('Personalized Assistance: High-altitude oxygen kits, customized cold-weather gear, and', 11),
            _ph('Luxury Transportation: Expertly trained mountain drivers handling top-tier, regularly sanitized', 12),
            _ph('& POLICIES', 13),
            _ph('Inner Line Permits: Domestic travelers require an Inner Line Permit (ILP), which will be fully', 14)
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
        tagline='Dimapur • Kohima • Jakhama • Dzukou Valley • Khonoma',
        overview='DZUKOU VALLEY & TRIBAL HERITAGE LUXURY EXPEDITION 05 Nights / 06 Days Premium Itinerary Welcome to the mystical realm of Northeast India with the signature Best Nagaland Tour Package crafted exclusively by TRAGUIN. This is not just a holiday; it is an emotional journey into the heart of the ancient Naga hills. Prepare to immerse yourself in breathtaking TRAGUIN Premium Luxury Expeditions landscapes, stand in awe before emerald vistas, and discover the raw, untouched magic of the legendary Dzukou Valley. Designed carefully for discerning travelers who seek both thrilling high-altitude treks and premium comfort, this bespoke Nagaland Honeymoon Package and Nagaland Family Tour guarantees unforgettable memories wrapped in signature hospitality. Let the whisper of the pristine winds and the warmth of tribal folklore reawaken your spirit on this ultimate Luxury Nagaland Holiday.\n\nTOUR OVERVIEW\nThis elite, custom-tailored exploration traces a spectacular route through the cultural hubs and pristine wilderness of Nagaland. Your expedition begins upon arrival at Dimapur, transitioning smoothly into the historic high-altitude town of Kohima, leading up to an immersive, professionally assisted trek into the world-famous Dzukou Valley. Every detail of this itinerary is backed by a TRAGUIN curated experience note: you will be accompanied by certified indigenous naturalists, enjoy high-end glamping setups with warm comforts amidst wild valleys, and travel via premium luxury 4x4 SUVs. All gourmet meals showcasing local organic ingredients and refined continental options are fully managed by our private culinary team, ensuring a seamless luxury experience from start to finish. DESTINATION SPOTLIGHT & PREMIUM EXPERIENCES\n\nWhy Visit Nagaland? Nagaland is a land of vibrant warriors, mystical mist-covered valleys, and\ndeeply rooted indigenous traditions. It offers an escape from the mundane into a world where culture and wilderness thrive side by side. A Premium Nagaland Experience allows travelers to witness rare geographical wonders, dramatic topography, and unparalleled biodiversity. Famous Attractions & Most Searched Experiences: The peak highlight of this voyage is Nagaland Sightseeing at its finest—the ethereal Dzukou Valley, famously known as the "Valley of Celestial Charm," where the unique Dzukou Lily blooms. Key highlights include exploring the Kisama Heritage Village (the legendary site of the Hornbill Festival), paying respects at the historic Kohima War Cemetery, and wandering through Khonoma, Africa and Asia’s first official Green Village. Best Honeymoon, Family, & Luxury Points: For couples, watching the sunrise over the rolling green hills of Dzukou from a private luxury tent is arguably the most romantic and elite experience in Northeast India. Families will find rich cultural education and safe, professionally managed soft- adventure activities perfect for creating lifelong bonding experiences. Popular Instagram Locations: Capture spectacular content at the sweeping panoramic ridges of Dzukou Valley, the traditional carved wooden gateways of Khonoma, and the historic WWII tank monument overlooking Kohima town. Adventure, Shopping, & Culture Highlights: Embark on exhilarating treks through steep bamboo trails, purchase world-class handwoven Naga shawls and exquisite bamboo wickerwork at local TRAGUIN Premium Luxury Expeditions artisan markets, and experience authentic tribal hospitality with curated culinary tastings of local organic delicacies.',
        seo_title='NL-009 | Dzukou Valley & Tribal Heritage Luxury Expedition | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Nagaland package (NL-009 / TRG-NAG-ADV-009): Dimapur • Kohima • Jakhama • Dzukou Valley • Khonoma with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: DIMAPUR TO KOHIMA', 1),
            _ih('Day 02: KOHIMA TO JAKHAMA & TREK TO DZUKOU VALLEY', 2),
            _ih('Day 03: EXPLORING THE HEART OF DZUKOU VALLEY', 3),
            _ih('Day 04: DZUKOU VALLEY TO VISWEMA & KISAMA HERITAGE VILLAGE', 4),
            _ih('Day 05: KOHIMA TO KHONOMA GREEN VILLAGE', 5),
            _ih('Day 06: KOHIMA TO DIMAPUR DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private tribal wrestling demonstration and interaction with', 7),
            _ih('Curated by TRAGUIN Experts: Custom trail mapping ensuring comfortable gradient ascents', 8),
            _ih('Personalized Assistance: High-altitude oxygen kits, customized cold-weather gear, and', 9)
        ],
        days=[
            _day(
                1,
                'DIMAPUR TO KOHIMA',
                (
                    'THE GATEWAY TO WARRIOR LAND & ROYAL WELCOME Your ultimate luxury adventure begins as you land at Dimapur Airport. A dedicated TRAGUIN luxury travel concierge will receive you warmly with a traditional Naga welcome garland and fresh seasonal refreshments. Step into your private, plush 4x4 SUV and begin a highly scenic uphill drive towards Kohima, the capital city steeped in history and culture. As you traverse winding roads, observe the changing flora and feel the crisp mountain air revitalize your senses. Upon reaching Kohima, check into your handpicked luxury accommodation. In the afternoon, enjoy an exclusive guided tour of the Top Tourist Places in Nagaland, starting with the beautifully landscaped Kohima War Cemetery, dedicated to the brave hearts of WWII. End your evening with an aromatic cup of local organic Naga coffee at a boutique cafe overlooking the glittering lights of Kohima.'
                ),
                [
                    'Sightseeing Included: Kohima War Cemetery, Local Cathedral, Kohima Local Bazaar.',
                    'Optional Activities: Traditional attire photography session.',
                    'Evening Experience: Private orientation by our Lead Mountain Guide over gourmet appetizers.',
                    'Overnight Stay: Premium Hotel / Luxury Resort in Kohima.',
                    'Meals Included: Welcome Lunch & Curated Dinner.',
                ],
            ),
            _day(
                2,
                'KOHIMA TO JAKHAMA & TREK TO DZUKOU VALLEY',
                (
                    'ASCENDING INTO THE VALLEY OF GODS & CELESTIAL VISTAS Wake up early to a glorious sunrise and enjoy a wholesome, energy-packed breakfast. Today, you embark on the crown jewel experience of your TRAGUIN Nagaland Packages—the trek to the majestic Dzukou Valley. Your private SUV transfers you to the Jakhama trail head. Accompanied by professional porters and indigenous naturalists, you begin your ascent. The initial climb features moss-covered stone steps under a dense canopy of ancient forests, echoing with exotic birdsong. As you reach the ridge crest, the forest opens spectacularly into a breathless landscape of endless rolling green hills, reminiscent of giant velvet waves. This is the stunning Dzukou Valley,'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary for Day 2.',
                ],
            ),
            _day(
                3,
                'EXPLORING THE HEART OF DZUKOU VALLEY',
                (
                    'MEANDERING STREAMS, PRISTINE CAVES & EMOTIONAL SERENITY An unforgettable morning awaits. Witness the famous Dzukou morning mist rise from the valley floor as our camp chef serves hot, freshly brewed tea directly to your tent. Today is dedicated entirely to deep, immersive exploration of this mystical valley. We hike down to the valley floor where the crystal-clear Dzukou and Japfu rivers intersect. Walk over natural stone bridges and explore hidden caves that have guarded tribal secrets for centuries. The topography is magical, featuring unique dwarf bamboo that blankets the earth perfectly. Your guide will lead you to prime blooming zones where the rare endemic flowers paint the valley in delicate pink hues during the Best Time to Visit Nagaland. Enjoy a peaceful luxury picnic lunch served on a clean granite rock beside a sparkling stream, letting the pure emotional peace of nature sink into your soul.'
                ),
                [
                    'Sightseeing Included: Ghost Caves, Valley Floor River Confluence, Lily Blooming Zones.',
                    'Optional Activities: High-altitude meditation session or professional landscape photography masterclass.',
                    'Evening Experience: Stargazing and hot hotpot dinner prepared with locally foraging mountain herbs.',
                    'Overnight Stay: Premium Heated Glamping Tents in Dzukou Valley.',
                    'Meals Included: Breakfast, Luxury River Picnic Lunch, Gourmet Camp Dinner.',
                ],
            ),
            _day(
                4,
                'DZUKOU VALLEY TO VISWEMA & KISAMA HERITAGE VILLAGE',
                (
                    'THE DESCENT OF EXPLORERS & THE CRADLE OF NAGA CULTURE After a leisurely breakfast, bid farewell to the pristine wilderness of the valley as you begin a gentle, panoramic descent via the Viswema route. This path offers sweeping alternative angles of the stunning landscapes, making it an excellent time for group photos and memorable captures. Your private luxury transport awaits at the foothills to whisk you back into comfort.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary for Day 4.',
                ],
            ),
            _day(
                5,
                'KOHIMA TO KHONOMA GREEN VILLAGE',
                (
                    "ASIA'S FIRST GREEN VILLAGE & ECO-LUXURY HERITAGE TOUR Indulge in a premium breakfast before taking a highly scenic drive to Khonoma Green Village, an ancient bastion of the Angami tribe famed for its fierce resistance against British colonial forces and its modern global leadership in eco-conservation. This historical village is surrounded by magnificent terraced rice fields that cascade elegantly down the mountain slopes, engineered with ancient indigenous irrigation technology. Stroll down clean, stone-paved pathways through historical village fortresses (Khels). Interact with local weavers creating intricate masterpieces from wild stinging nettle fibers. Witness a live demonstration of traditional Naga wrestling, an energetic sport deeply rooted in tribal honor. This evening, celebrate the final night of your premium journey with a specially curated grand celebratory dinner."
                ),
                [
                    'Sightseeing Included: Khonoma Fort, Terraced Paddy Fields, Conservation Forest Walk, Artisan Craft Centers.',
                    'Optional Activities: Short organic farming experience or nature birdwatching walk.',
                    'Evening Experience: Grand Farewell Barbecue Dinner with premium tribal fusion pairings.',
                    'Overnight Stay: Premium Luxury Eco-Lodge in Khonoma / Kohima.',
                    'Meals Included: Breakfast, Organic Farm-to-Table Lunch, Luxury Farewell Dinner.',
                ],
            ),
            _day(
                6,
                'KOHIMA TO DIMAPUR DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES & HOMEWARD JOURNEY'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary for Day 6.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Vivor / Razhu Pru (Heritage Room) | TRAGUIN Coordinated Standard Dome Tents',
                'Kohima | Dzukou',
                '3N Kohima/Khonoma|2N Dzukou Valley',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast + Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Vivor / Razhu Pru (Heritage Room) | TRAGUIN Coordinated Standard Dome Tents | MAPAI (Breakfast + Dinner)',
            ),
            _hotel(
                'The Horizon / Niraamaya Heritage (Executive) | TRAGUIN Private Comfort Camps (Thick Bedding)',
                'Kohima | Dzukou',
                '3N Kohima/Khonoma|2N Dzukou Valley',
                'Premium',
                'Deluxe Room',
                'APAI (All Meals Included)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Horizon / Niraamaya Heritage (Executive) | TRAGUIN Private Comfort Camps (Thick Bedding) | APAI (All Meals Included)',
            ),
            _hotel(
                'Dzukou Valley Eco Resort / Luxury Cottages | TRAGUIN Premium Heated Glamping Tents',
                'Kohima | Dzukou',
                '3N Kohima/Khonoma|2N Dzukou Valley',
                'Luxury',
                'Deluxe Room',
                'All Inclusive Gourmet',
                5,
                3,
                description='OPTION 03 – LUXURY: Dzukou Valley Eco Resort / Luxury Cottages | TRAGUIN Premium Heated Glamping Tents | All Inclusive Gourmet',
            ),
            _hotel(
                'The Ultimate Travelling Camp (TUTC) / Signature Elite | TRAGUIN VIP Custom Alpine Luxury Geodesic Domes',
                'Kohima | Dzukou',
                '3N Kohima/Khonoma|2N Dzukou Valley',
                'Ultra Luxury',
                'Deluxe Room',
                'Royal Bespoke Dining',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Ultimate Travelling Camp (TUTC) / Signature Elite | TRAGUIN VIP Custom Alpine Luxury Geodesic Domes | Royal Bespoke Dining',
            )
        ],
        inclusions=[
            _inc_included('Accommodation: Handpicked premium hotels and luxury glamping.', 1),
            _inc_included('Meals: All premium breakfast, curated lunches, and gourmet dinners.', 2),
            _inc_included('Transfers: Dedicated Luxury 4x4 SUV (Innova Crysta / Fortuner) throughout.', 3),
            _inc_included('Sightseeing: All entry fees, Inner Line Permits (ILP), and local taxes.', 4),
            _inc_included('Assistance: 24/7 dedicated TRAGUIN concierge support.', 5),
            _inc_included('Welcome Amenities: Luxury arrival gift hampers and local organic kits.', 6),
            _inc_included('Trek Support: Professional indigenous guides, certified camp kitchen team, and personal porters.', 7),
            _inc_excluded('Flights: Domestic or International airfare to/from Dimapur.', 8),
            _inc_excluded('Personal Expenses: Laundry, premium hard beverages, telephone calls.', 9),
            _inc_excluded('Insurance: International or domestic medical and travel insurance.', 10),
            _inc_excluded('Optional Tours: Any activities not explicitly listed in the itinerary.', 11),
            _inc_excluded('Camera Fees: Professional drone or special video camera permits.', 12),
            _inc_excluded('Tips: Gratuities for local drivers, porters, and camp staff.', 13),
        ],
    )
    return package, itinerary

def build_nl_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'NL-010'
    tour_code = 'TRG-NAG-FAM-010'
    title = 'Complete Nagaland Immersive Family Luxury Holiday'
    duration = '07 Nights / 08 Days'
    slug = 'nl-010-complete-nagaland-immersive-family-luxury-holiday'
    itin_slug = 'nl-010-complete-nagaland-immersive-family-luxury-holiday-itinerary'
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
            _ph('Serial code NL-010 | TRAGUIN tour code TRG-NAG-FAM-010', 1),
            _ph('State / Country: Nagaland / India | Category: Family Luxury Vacation', 2),
            _ph('Destinations: Dimapur • Kohima • Kigwema • Khonoma • Mokokchung • Tuophema', 3),
            _ph('Ideal for: Multi-Generational Families, Heritage Seekers, Culture Explorers', 4),
            _ph('Best season: October to May (Pleasant and Festive)', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Vehicle / Meals: Luxury SUV Fleet & All Gourmet Meals', 7),
            _ph('Route: Dimapur → Kohima → Kigwema → Khonoma → Tuophema → Mokokchung → Kohima → Dimapur', 8),
            _ph('TRAGUIN Signature Experience: Private family audience with clan elders and exclusive access to', 9),
            _ph('Curated by TRAGUIN Experts: Smooth travel times and custom multi-generational pacing', 10),
            _ph('Personalized Assistance: Professional traveling medical kit, custom car seat configurations for', 11),
            _ph('Premium Handpicked Hotels: Continuous quality vetting ensures every family suite meets', 12),
            _ph('& POLICIES', 13),
            _ph('Inner Line Permits: Domestic family members must submit identification documents 15 days in', 14)
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
        tagline='Dimapur • Kohima • Kigwema • Khonoma • Mokokchung • Tuophema',
        overview='COMPLETE NAGALAND IMMERSIVE FAMILY LUXURY HOLIDAY 07 Nights / 08 Days Elite Heritage Route Discover the hidden cultural crown of Northeast India with the ultimate Best Nagaland Tour Package meticulously mapped for your family by TRAGUIN. This custom Nagaland Family Tour is an emotional story waiting to unfold—a premium journey through timeless mist- TRAGUIN Complete Nagaland Family Tour Proposal laden hills, ancestral fortresses, and vibrant traditional lifestyles. Crafted for families who demand refined elegance alongside rich, authentic learning, this bespoke itinerary masterfully handles every detail. From the traditional royal welcomes to breathtaking landscapes and elite handpicked hotels, TRAGUIN ensures an effortless immersion into the majestic Naga heritage. Share unforgettable memories with your loved ones on this peerless Luxury Nagaland Holiday.\n\nTOUR OVERVIEW\nThis elite 7 Nights / 8 Days exploration provides an extensive and grand cultural loop through the premier tribal heartlands of Nagaland. Specially engineered for families and multi-generational groups (FIT), your journey eliminates all rugged uncertainties while retaining pure cultural magic. Travel in absolute style across challenging terrains in a dedicated convoy of premium 4x4 SUVs. Your custom meal plan features curated multi-cuisine culinary spreads ranging from continental classics to safe, organic local farm-to-table delicacies. Backed by a signature TRAGUIN curated experience note, you will enjoy private tribal audiences, step into living history museums, stay at premium eco- resorts, and benefit from round-the-clock VIP operational monitoring. DESTINATION SPOTLIGHT & PREMIUM FAMILY EXPERIENCES\n\nWhy Visit Nagaland with Family? Far removed from tourist crowds, Nagaland offers families a deep\ndive into an proud, ancient world characterized by incredible warmth, community values, and artistic grandeur. This Premium Nagaland Experience provides rich multi-generational bonding amidst spectacular natural wonders and deep historical narratives. Famous Attractions & Most Searched Experiences: This extensive route showcases premier Nagaland Sightseeing landmarks including the Kisama Heritage Village, the historic WWII War Cemetery, Asia’s first eco-designated Green Village of Khonoma, the traditional Ao Naga cradle of Mokokchung, and the beautiful cultural amphitheatres of Tuophema. Best Honeymoon & Family Tour Highlights: While couples find unparalleled romance in the peaceful, cloud-kissed tribal eco-lodges, families benefit from highly engaging cultural masterclasses —such as learning indigenous bamboo-crafting, traditional folklore storytelling, and tasting rare culinary profiles. Popular Instagram Locations: Capture striking family portraits against the giant carved wood monoliths of ancient village gates, the emerald terraced fields cascading down Khonoma Valley, and the historic thatched roofs of traditional Ao tribal huts. Adventure, Shopping, & Culture Highlights: Walk through lush community conservation forests, purchase legendary handwoven textiles, exquisite beadwork jewelry, and local organic wild honey at exclusive artisan cooperatives, and witness magnificent tribal dances organized privately for your family. TRAGUIN Complete Nagaland Family Tour Proposal',
        seo_title='NL-010 | Complete Nagaland Immersive Family Luxury Holiday | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Nagaland package (NL-010 / TRG-NAG-FAM-010): Dimapur • Kohima • Kigwema • Khonoma • Mokokchung • Tuophema with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL AT DIMAPUR TO KOHIMA', 1),
            _ih('Day 02: KOHIMA TO KISAMA & KIGWEMA VILLAGE', 2),
            _ih('Day 03: KOHIMA TO KHONOMA GREEN VILLAGE', 3),
            _ih('Day 04: KHONOMA TO TUOPHEMA TOURIST VILLAGE', 4),
            _ih('Day 05: TUOPHEMA TO MOKOKCHUNG', 5),
            _ih('Day 06: MOKOKCHUNG: EXCURSION TO UNGMA & MONGSENYIMTI', 6),
            _ih('Day 07: MOKOKCHUNG BACK TO KOHIMA', 7),
            _ih('Day 08: KOHIMA TO DIMAPUR DEPARTURE', 8),
            _ih('TRAGUIN Signature Experience: Private family audience with clan elders and exclusive access to', 9),
            _ih('Curated by TRAGUIN Experts: Smooth travel times and custom multi-generational pacing', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL AT DIMAPUR TO KOHIMA',
                (
                    'A REGAL ROYAL WELCOME TO THE TRIBAL CAPITAL Your premium family holiday begins seamlessly as your flight touches down at Dimapur Airport. Your dedicated TRAGUIN travel concierge will receive you at the arrival terminal with traditional ceremonial silk sashes and chilled fresh mountain juices. Step into your plush, private SUV fleet and begin a highly scenic uphill drive to Kohima. Watch the urban landscapes dissolve into majestic valleys and mist-crowned forests. Arrive in Kohima and check into your elite, handpicked hotel suite. In the evening, visit the beautifully manicured Kohima War Cemetery—a serene historical sanctuary that offers a poignant look into WWII history. Follow this with an exclusive stroll through the local artisan bazaar, introducing your family to the vibrant everyday colors of Naga life.'
                ),
                [
                    'Sightseeing Included: Kohima War Cemetery, Kohima Cathedral, Local Handicraft Markets.',
                    'Optional Activities: Professional family portrait session wearing premium handwoven tribal jackets.',
                    'Evening Experience: Private orientation by our Cultural Anthropologist Guide over fine continental dinner.',
                    'Overnight Stay: Premium Luxury Hotel in Kohima.',
                    'Meals Included: High Tea & Welcoming Gala Dinner.',
                ],
            ),
            _day(
                2,
                'KOHIMA TO KISAMA & KIGWEMA VILLAGE',
                (
                    "WALKING THROUGH LIVING HISTORY & ANCESTRAL MORUNGS Enjoy an exquisite breakfast before driving to the celebrated Kisama Heritage Village, the architectural masterpiece that plays host to the world-renowned annual Hornbill Festival. Your family will enjoy an exclusive private tour through the 16 traditional 'Morungs' (tribal youth dormitories). Admire the intricate woodwork carvings of hornbills, tigers, and ancestral symbols that represent tribal courage. Later, drive to the neighboring historic village of Kigwema, where your family can interact closely with Angami elders. Walk through ancient alleys and step inside a traditional house that still preserves genuine marks from WWII bullet exchanges. This immersive experience bridges historical education with unparalleled luxury hospitality."
                ),
                [
                    'Sightseeing Included: Kisama Heritage Amphitheater, Tribal Morungs, Kigwema Village Walk.',
                    'Optional Activities: Traditional archery masterclass or local organic rice beer tasting for adults.',
                    'Evening Experience: Gourmet multi-cuisine dinner with a private acoustic performance by a local folk artist.',
                    'Overnight Stay: Premium Luxury Hotel in Kohima.',
                ],
            ),
            _day(
                3,
                'KOHIMA TO KHONOMA GREEN VILLAGE',
                (
                    "ASIA'S FIRST GREEN VILLAGE & ANCIENT CONSERVATION ETHICS Set off on a highly scenic drive to Khonoma Green Village, an ancient stronghold of the Angami tribe famed globally for its transition from traditional hunting to pioneering wildlife conservation. Marvel at the dramatic topography as your vehicle winds past thousands of ancient stone-walled terraced agricultural fields, still flawlessly farmed using indigenous engineering passed down across generations. Walk through the historic village defensive forts (Khels), where your family will hear tales of fierce tribal resistance. Meet multi-generational weavers who turn wild nettle fibers into spectacular, soft fabrics. This afternoon, your family will witness an exclusive live exhibition of traditional Naga wrestling arranged privately by our team."
                ),
                [
                    'Sightseeing Included: Khonoma Fort, Terraced Valleys, Village Craft Cooperatives.',
                    'Optional Activities: A short, guided birdwatching walk into the lush community sanctuary.',
                    'Evening Experience: Private farm-to-table culinary workshop focusing on slow-cooked dishes with bamboo shoot.',
                    'Overnight Stay: Premium Luxury Heritage Eco-Lodge in Khonoma.',
                    'Meals Included: Breakfast, Organic Farm Lunch, Specially Curated Heritage Dinner.',
                ],
            ),
            _day(
                4,
                'KHONOMA TO TUOPHEMA TOURIST VILLAGE',
                (
                    'NORTHERN ANGAMI HERITAGE & PREMIUM ETHNIC HOSPITALITY Bid farewell to the eco-bastion of Khonoma as you head north towards the unique cultural township of Tuophema Tourist Village. This community-managed destination was conceptualized to provide elite travelers with a luxurious window into traditional community design. Check into your custom, premium family cottage constructed beautifully in the signature Angami architectural style. Spend the afternoon walking down pristine pathways lined with traditional wildflowers. Your family will visit the village museum, which houses rare antique tribal ornaments, historical warrior headpieces, and ceremonial spears. This evening is a celebration of community values, allowing your children to engage with local youth over traditional indoor games.'
                ),
                [
                    'Sightseeing Included: Tuophema Cultural Village, Heritage Museum, Community Amphitheater.',
                    'Optional Activities: Traditional bead-making and jewelry design workshop.',
                ],
            ),
            _day(
                5,
                'TUOPHEMA TO MOKOKCHUNG',
                (
                    'JOURNEYING INTO THE LAND OF THE AO NAGA TRIBE Today, enjoy an early morning premium breakfast before embarking on an expansive, breathtakingly scenic road journey deep into the cultural heartland of Mokokchung. This region serves as the ancestral home of the vibrant Ao Naga tribe, renowned for their incredible musicality, highly detailed black-and-blue woven motifs, and profound modern literary traditions. As your luxury vehicle fleet glides past vast rolling tea plantations and mist-covered mountain valleys, stop for panoramic photography at dramatic viewpoints. Upon arriving in Mokokchung town, check into your premium luxury suites and spend a relaxing evening enjoying a fine multi-cuisine dinner.'
                ),
                [
                    'Sightseeing Included: En-route mountain passes, Mokokchung Town Square, Panoramic Viewpoints.',
                    'Optional Activities: Relaxing private family spa session at the resort.',
                    'Evening Experience: Private interactive presentation on Ao tribal textile evolution by an expert curator.',
                    'Overnight Stay: Premium Luxury Resort in Mokokchung.',
                    'Meals Included: Breakfast, High-altitude Picnic Lunch, International Buffet Dinner.',
                ],
            ),
            _day(
                6,
                'MOKOKCHUNG: EXCURSION TO UNGMA & MONGSENYIMTI',
                (
                    'THE CRADLE OF ANCIENT CUSTOMS & GIANT TRIBAL LOG-DRUMS Dedicate today to discovering the premier Top Tourist Places in Nagaland found within Mokokchung. Visit Ungma Village, proudly recognized as the largest and oldest traditional Ao village. According to ancient lore, this village is the cradle from which the Ao tribe expanded. Walk to the village summit to view the magnificent, colossal log-drum carved out of a single giant tree trunk—an ancient instrument used to sound war alerts or celebrate royal festivals. Next, drive to the picturesque ridge-top village of Mongsenyimti, which offers awe-inspiring 360-degree views of the surrounding valleys. Meet local tribal craftsmen and painters who continue to practice ancestral storytelling through fine bamboo brush arts.'
                ),
                [
                    'Sightseeing Included: Ungma Heritage Site, Ancient Log-Drum, Mongsenyimti Viewpoints.',
                ],
            ),
            _day(
                7,
                'MOKOKCHUNG BACK TO KOHIMA',
                (
                    'SAVORING THE DRAMATIC TOPOGRAPHY & RESTFUL LUXURY RETURN After a hearty continental breakfast, your family begins their return journey southwards along the beautiful ridge roads back to Kohima. This day is deliberately structured to be relaxed and comfortable. Your premium SUV fleet is fully stocked with organic treats, luxury refreshments, and entertainment options for children. Stop along the way at the picturesque Tseminyu valley town to view traditional Rengma Naga terraced farms. Upon reaching Kohima by late afternoon, check back into your executive luxury suites. Spend your final evening in the state capital doing light souvenir shopping or relaxing over premium amenities at the resort.'
                ),
                [
                    'Sightseeing Included: Tseminyu Valley Overlooks, Kohima Fine Craft Emporium.',
                    'Optional Activities: Last-minute family shopping trip for luxury handwoven throws and artifacts.',
                    "Evening Experience: Grand Farewell Cocktail Banquet and slide-show presentation of your family's journey.",
                    'Overnight Stay: Premium Luxury Hotel in Kohima.',
                    'Meals Included: Breakfast, Comfort En-route Lunch, Grand Farewell Dinner.',
                ],
            ),
            _day(
                8,
                'KOHIMA TO DIMAPUR DEPARTURE',
                (
                    "CHERISHING LIFELONG FAMILY MEMORIES & SMOOTH HOMEWARD DEPARTURE Savor your final luxury breakfast amidst the peaceful mountain clouds of Kohima. Take a moment to capture final family photographs from your suite's panoramic veranda. Your professional TRAGUIN uniform-clad chauffeur will take care of your luggage and secure all your travel souvenirs safely in your premium vehicles. As you drive comfortably downhill back towards Dimapur Airport, look back on a spectacular week of rich discovery, deep heritage, and luxurious comfort. Your travel concierge will assist you completely through the airport check-in and VIP lounge entry, bringing your unparalleled TRAGUIN Nagaland Packages experience to a flawless conclusion."
                ),
                [
                    'Sightseeing Included: Scenic downhill mountain drive.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Vivor (Deluxe Suite) | Tuophema Village Ethnic Cottages | Hotel Whispering Winds',
                'Kohima | Khonoma Tuophema | Mokokchung',
                '4N Kohima|2N Khonoma/Tuophema|2N Mokokchung',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Vivor (Deluxe Suite) | Tuophema Village Ethnic Cottages | Hotel Whispering Winds | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'The Horizon Kohima (Executive Suite) | Khonoma Heritage Eco-Lodge | Bravo Hotel & Resort',
                'Kohima | Khonoma Tuophema | Mokokchung',
                '4N Kohima|2N Khonoma/Tuophema|2N Mokokchung',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Horizon Kohima (Executive Suite) | Khonoma Heritage Eco-Lodge | Bravo Hotel & Resort | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Niraamaya Retreats Aradura (Luxury Suite) | TRAGUIN Private Luxury Villa Units | Mokokchung Elite Eco Resort',
                'Kohima | Khonoma Tuophema | Mokokchung',
                '4N Kohima|2N Khonoma/Tuophema|2N Mokokchung',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Niraamaya Retreats Aradura (Luxury Suite) | TRAGUIN Private Luxury Villa Units | Mokokchung Elite Eco Resort | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'Signature Elite Estate (VVIP Royal Wing) | TRAGUIN Custom VIP Glamping Domes | The Majestic Ao Ridge Estate',
                'Kohima | Khonoma Tuophema | Mokokchung',
                '4N Kohima|2N Khonoma/Tuophema|2N Mokokchung',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Signature Elite Estate (VVIP Royal Wing) | TRAGUIN Custom VIP Glamping Domes | The Majestic Ao Ridge Estate | MAPAI (Breakfast & Dinner)',
            )
        ],
        inclusions=[
            _inc_included('Accommodation: 7 Nights in handpicked premium hotels and eco-resorts.', 1),
            _inc_included('Meals: All daily breakfasts, custom lunches, and grand festive dinners.', 2),
            _inc_included('Transfers: Dedicated Luxury SUV Fleet (Innova Crysta / Toyota Fortuner) throughout.', 3),
            _inc_included('Sightseeing: All destination entry permits, inner-line family passes, and monument taxes.', 4),
            _inc_included('Assistance: 24/7 dedicated TRAGUIN elite concierge support.', 5),
            _inc_included("Welcome Amenities: Premium arrival luxury gift hampers, organic treats, and kids' activity journals.", 6),
            _inc_included('Complimentary Experiences: Private Naga wrestling display and exclusive artisan weaving masterclasses.', 7),
            _inc_excluded('Flights: Commercial or chartered domestic airfare to/from Dimapur.', 8),
            _inc_excluded('Personal Expenses: Premium vintage spirits, room service laundry, international phone roaming.', 9),
            _inc_excluded('Insurance: Multi-risk comprehensive family travel and medical coverage.', 10),
            _inc_excluded('Optional Tours: Extra activities or off-route excursions not detailed in the itinerary.', 11),
            _inc_excluded('Camera Levies: Special institutional commercial or drone videography fees.', 12),
            _inc_excluded('Tips: Optional tips for your professional drivers, local guides, and estate crew.', 13),
        ],
    )
    return package, itinerary

NAGALAND_DOMESTIC_BUILDERS = [
    build_nl_001,
    build_nl_002,
    build_nl_003,
    build_nl_004,
    build_nl_005,
    build_nl_006,
    build_nl_007,
    build_nl_008,
    build_nl_009,
    build_nl_010,
]
