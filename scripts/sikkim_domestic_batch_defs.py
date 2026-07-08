"""Builder functions for SK-001 through SK-015 Sikkim domestic packages."""

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

SIKKIM_SLUG = "sikkim"


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


def build_sk_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SK-001'
    tour_code = 'TRG-SIK-001'
    title = 'GANGTOK DELIGHT • HIMALAYAN BLISS & ALPINE SPLENDOUR'
    duration = '03 Nights / 04 Days'
    slug = 'sk-001-gangtok-delight-himalayan-bliss-alpine-splendour'
    itin_slug = 'sk-001-gangtok-delight-himalayan-bliss-alpine-splendour-itinerary'
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
            _ph('Serial code SK-001 | TRAGUIN tour code TRG-SIK-001', 1),
            _ph('State / Country: Sikkim / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Gangtok • Sikkim', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury SUV (Innova/Xylo) / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: A private, premium family tea-tasting tour at an upscale mountain', 8),
            _ph('Curated by TRAGUIN Experts: Expertly managed travel planning designed to give your family plenty of', 9),
            _ph('Premium Handpicked Hotels: Accommodations selected for their high safety standards, stunning', 10),
            _ph('Luxury Transportation: Specially trained mountain drivers ensuring elite safety and comfort across the', 11)
        ],
        moods=['Luxury', 'Nature'],
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
        tagline='GANGTOK DELIGHT',
        overview='SPLENDOUR Welcome to an unforgettable Himalayan escape curated exclusively by TRAGUIN. Embark on the finest Sikkim Family Tour, intricately planned to show you the breathtaking landscapes, mist-shrouded valleys, and sacred traditions of this pristine mountain state. As your dedicated luxury travel consultants, TRAGUIN TRAGUIN Premium Luxury Itinerary — SK-001 1 transforms your vacation into a seamless luxury holiday with premium stays, exquisite local transport, and immersive experiences. From the bustling mountain culture of Gangtok to the mystical alpine waters of Tsomgo Lake, every detail is crafted to capture unforgettable memories.\n\nTOUR OVERVIEW\nThis custom-tailored holiday package offers a sophisticated balance between majestic alpine landscapes, cultural monasteries, and premium comfort. Travelling in a dedicated private luxury SUV driven by an expert mountain chauffeur, your family will experience absolute safety and relaxation. Featuring a curated meal plan with rich breakfasts and gourmet dinners, this route represents the definitive premium Sikkim experience. Every moment of your journey includes the signature touch of TRAGUIN curated experiences, ensuring fast- tracked permit coordination, personalized local insight, and continuous bespoke support.\n\nWHY CHOOSE THE BEST SIKKIM TOUR PACKAGE?\nWhen planning a Luxury Sikkim Holiday, discerning travellers seek a deep connection with untouched alpine beauty, dramatic mountain ridges, and serene spiritual sanctuaries. Sikkim offers an extraordinary array of iconic attractions. From the sacred high-altitude Tsomgo Lake—a top tourist place in Sikkim for alpine photography—to the stunning vistas of the Teesta River, the region provides unparalleled depth. For families and couples looking to book a signature Sikkim Honeymoon Package or Sikkim Family Tour, Gangtok unfolds highly popular Instagram locations like the MG Marg promenade, the scenic Ganesh Tok view decks, and historic Buddhist monasteries. Whether you are interested in souvenir shopping for authentic Tibetan carpets, tasting traditional Himalayan food, or enjoying high-altitude adventure, our TRAGUIN Sikkim Packages guarantee premium comfort, handpicked hotels, and curated exclusive experiences during the absolute best time to visit Sikkim.',
        seo_title='SK-001 | GANGTOK DELIGHT | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Sikkim package (SK-001 / TRG-SIK-001): Gangtok • Sikkim with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL AT IXB/NJP TO GANGTOK', 1),
            _ih('Day 02: EXCURSION TO TSOMGO LAKE & BABA MANDIR', 2),
            _ih('Day 03: GANGTOK LOCAL SIGHTSEEING', 3),
            _ih('Day 04: GANGTOK TO IXB/NJP / DEPARTURE', 4),
            _ih('TRAGUIN Signature Experience: A private, premium family tea-tasting tour at an upscale mountain', 5),
            _ih('Curated by TRAGUIN Experts: Expertly managed travel planning designed to give your family plenty of', 6),
            _ih('Premium Handpicked Hotels: Accommodations selected for their high safety standards, stunning', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL AT IXB/NJP TO GANGTOK',
                (
                    'WELCOME TO THE HIMALAYAN KINGDOM – GATEWAY TO CLOUD REED COMFORT Your premium Sikkim experience starts the moment you land at Bagdogra Airport (IXB) or arrive at New Jalpaiguri Railway Station (NJP). Your private luxury SUV and personal chauffeur await to escort you on a stunning drive along the winding emerald waters of the Teesta River. Pass through lush green tea valleys and mountain footpaths before reaching Gangtok, the hill-station capital perched on a high mountain ridge. Check into your premium handpicked hotel, accept your welcome amenities, and spend the evening enjoying a relaxing stroll down MG Marg, a neat, pedestrian-only boulevard famous for local cafes and upscale mountain fashion.'
                ),
                [
                    'Sightseeing Included: Teesta River viewpoint drive, MG Marg lifestyle promenade walking tour.',
                    'Evening Experience: Premium lounge dinner at MG Marg with artisan Himalayan beverages curated by',
                    'Overnight Stay: Gangtok (Premium Luxury Mountain Resort)',
                    'Meals Included: Welcome Drink & Luxury Welcome Dinner',
                ],
            ),
            _day(
                2,
                'EXCURSION TO TSOMGO LAKE & BABA MANDIR',
                (
                    "MYSTICAL ALPINE LAKES & SNOW-CAPPED PEAKS Savor an early, premium breakfast before setting out on an alpine adventure to Tsomgo Lake (Changu Lake), located at a breathtaking altitude of 12,400 feet. This sacred glacial water body mirrors the majestic peaks surrounding it, creating a premier photography point. Enjoy a fun, colorful Yak ride along the lake's edge or experience a gondola ropeway ride for stunning bird's-eye views. Continue your high-altitude drive to the legendary Baba Harbhajan Singh Memorial Mandir, a sacred shrine deeply woven into local army folklore. costs)."
                ),
                [
                    'Sightseeing Included: Tsomgo Glacial Lake, Baba Harbhajan Singh Mandir, Snow Viewpoints.',
                    'Optional Activities: Nathula Pass excursion to the Indo-China Border (subject to government permits & extra',
                    'Overnight Stay: Gangtok (Premium Luxury Mountain Resort)',
                    'Meals Included: Premium Breakfast & Authentic Mountain Dinner',
                ],
            ),
            _day(
                3,
                'GANGTOK LOCAL SIGHTSEEING',
                (
                    'BUDDHIST HERITAGE, PANORAMIC TOKS & CULTURAL SPLENDOUR Enjoy a beautiful mountain sunrise and a lavish breakfast before heading out on a premium Gangtok sightseeing tour. Discover the spiritual calmness of the ancient Rumtek Monastery, a global center of Kagyu Buddhism. Visit the flower showcase to admire rare Himalayan orchids, and observe ancient sacred art at the Namgyal Institute of Tibetology. Capture stunning family photographs at Ganesh Tok and Tashi Viewpoint, where the majestic Mt. Kanchenjunga massif can be seen clearly on a bright day. Viewpoint. delicacies.'
                ),
                [
                    'Sightseeing Included: Rumtek Monastery, Do Drul Chorten, Directorate of Handicrafts, Ganesh Tok, Tashi',
                    'Evening Experience: Private dinner at a traditional restaurant showcasing authentic Sikkimese Sekuwa and',
                    'Overnight Stay: Gangtok (Premium Luxury Mountain Resort)',
                    'Meals Included: Premium Breakfast & Sikkimese Theme Dinner',
                ],
            ),
            _day(
                4,
                'GANGTOK TO IXB/NJP / DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES OF THE EASTERN HIMALAYAS Indulge in a final morning breakfast while taking in the beautiful panoramic views from your resort deck. Pack your bags as your luxury vehicle arrives to escort you down the foothills back to Bagdogra Airport (IXB) or New Jalpaiguri Railway Station (NJP). Head home with a heart full of joy, family bonding, and unforgettable memories designed beautifully by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door mountain highway drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Summit Golden Crescent / Hotel',
                'Gangtok',
                '3N',
                'Deluxe',
                'Sonam Delek / similar',
                'Deluxe Valley View RoomMAPAI (Breakfast &',
                4,
                1,
                description='OPTION 01 – DELUXE: Summit Golden Crescent / Hotel | Sonam Delek / similar | Deluxe Valley View RoomMAPAI (Breakfast &',
            ),
            _hotel(
                'The Lemon Tree Hotel / Lemon',
                'Gangtok',
                '3N',
                'Premium',
                'Tree Premier Gangtok',
                'Executive Balcony RoomMAPAI (Breakfast &',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Lemon Tree Hotel / Lemon | Tree Premier Gangtok | Executive Balcony RoomMAPAI (Breakfast &',
            ),
            _hotel(
                'Mayfair Spa Resort & Casino /',
                'Gangtok',
                '3N',
                'Luxury',
                'Elgin Nor-Khill',
                'Luxury Heritage Grand',
                4,
                3,
                description='OPTION 03 – LUXURY: Mayfair Spa Resort & Casino / | Elgin Nor-Khill | Luxury Heritage Grand',
            ),
            _hotel(
                'Vivanta Sikkim, Pakyong /',
                'Gangtok',
                '3N',
                'Ultra Luxury',
                'Mayfair Executive Luxury Villa',
                'VVIP Royal Panoramic',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Vivanta Sikkim, Pakyong / | Mayfair Executive Luxury Villa | VVIP Royal Panoramic',
            )
        ],
        inclusions=[
            _inc_included('Premium stays: Handpicked properties as per your chosen luxury tier.', 1),
            _inc_included('Luxury Transportation: Private dedicated SUV for all point-to-point sightseeing.', 2),
            _inc_included('Curated Meal Plan: Daily luxury buffet breakfasts and theme dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated local operations manager on call.', 4),
            _inc_included('Permit Coordination: Seamless upfront handling of Inner Line Permits (ILP).', 5),
            _inc_included('Welcome Amenities: Customized luxury tea sampler and traditional Sikkimese welcome.', 6),
            _inc_excluded('Airfare, flight tickets, or main train line connection travel.', 7),
            _inc_excluded('Nathula Pass entry permit fee and local guide costs.', 8),
            _inc_excluded('Monument entry tickets, cable car passes, camera or video fees.', 9),
            _inc_excluded('Personal expenses such as laundry, phone calls, or tips.', 10),
        ],
    )
    return package, itinerary

def build_sk_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SK-002'
    tour_code = 'TRG-SK-002'
    title = 'GANGTOK & PELLING FAMILY EXPLORER • HIMALAYAN SPLENDOURS'
    duration = '05 Nights / 06 Days'
    slug = 'sk-002-gangtok-pelling-family-explorer-himalayan-splendours'
    itin_slug = 'sk-002-gangtok-pelling-family-explorer-himalayan-splendours-itinerary'
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
            _ph('Serial code SK-002 | TRAGUIN tour code TRG-SK-002', 1),
            _ph('State / Country: Sikkim / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Gangtok • Tsomgo', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury SUV (Innova/Xylo) / MAPAI Plan', 7),
            _ph('TRAGUIN Signature Experience: Private family tea-tasting experience featuring premium, organic leaves', 8),
            _ph('Curated by TRAGUIN Experts: Smooth pre-arranged permit processing for high-altitude zones,', 9),
            _ph('Premium Handpicked Hotels: Elite properties selected based on supreme safety, warm hospitality, and', 10),
            _ph('Luxury Transportation: Specially trained, background-verified mountain chauffeurs ensuring top-tier', 11)
        ],
        moods=['Family', 'Luxury'],
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
        tagline='GANGTOK & PELLING FAMILY EXPLORER',
        overview="SPLENDOURS Welcome to an unforgettable Himalayan escapade crafted with ultimate love and precision by TRAGUIN. Embark on the finest Sikkim Family Tour designed to weave together the legendary vertical peaks, mystical glacial lakes, and profound Buddhist heritage of this mountain kingdom. As your premier luxury travel consultants, TRAGUIN ensures a flawless vacation enriched with handpicked hotels, breathtaking TRAGUIN Premium Luxury Itinerary — SK-002 1 landscapes, and personalized service. Let the crisp mountain air, pristine cascades, and magnificent views of Mt. Kanchenjunga shape your family bond, crafting unforgettable memories that you will treasure forever.\n\nTOUR OVERVIEW\nThis elite luxury holiday package offers a seamless and comprehensive exploration of East and West Sikkim. Traveling in a fully private, luxury four-wheel drive or premium high-ground clearance SUV, your family will traverse mountain roads in absolute comfort and safety. With a curated meal plan offering extensive culinary choices from sumptuous breakfasts to traditional regional dinners, every day is tailored to delight. This specific route incorporates the exclusive TRAGUIN curated experience note, which guarantees smooth permit processing, dedicated expert guidance, and VVIP entry privileges at the state's most sought-after spots.\n\nWHY CHOOSE THE BEST SIKKIM TOUR PACKAGE?\nWhen considering a Luxury Sikkim Holiday, modern families seek a balance of tranquil spirituality, untouched alpine environments, and sophisticated comforts. Sikkim stands as one of the most uniquely pristine regions of the Eastern Himalayas, making our Sikkim Family Tour an extraordinary vacation choice. From the bustling, vibrant mountain streets of Gangtok to the dramatic glass skywalk of Pelling, Sikkim sightseeing reveals endless marvels. For couples and families looking for a specialized Sikkim Honeymoon Package or an immersive cultural escape, the region offers globally famous attractions like the sacred, turquoise Tsomgo Lake and the historic Pemayangtse Monastery. Capture striking family portraits at popular Instagram locations such as the Chenrezig Skywalk or Mahatma Gandhi Marg. Indulge in exquisite traditional handicraft shopping, enjoy local organic delicacies, or discover the raw scenic beauty of mountain waterfalls. Our signature TRAGUIN Sikkim Packages represent the premium Sikkim experience, perfectly scheduled for the best time to visit Sikkim.",
        seo_title='SK-002 | GANGTOK & PELLING FAMILY EXPLORER | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Sikkim package (SK-002 / TRG-SK-002): Gangtok • Tsomgo with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL AT IXB AIRPORT / NJP STATION TO GANGTOK', 1),
            _ih('Day 02: TSOMGO LAKE & BABA MANDIR EXCURSION', 2),
            _ih('Day 03: GANGTOK URBAN EXPEDITION TO PELLING', 3),
            _ih('Day 04: PELLING FULL DAY EXCURSION', 4),
            _ih('Day 05: PELLING TO GANGTOK (VIA RAVANGLA BUDDHA PARK)', 5),
            _ih('Day 06: GANGTOK TO BAGDOGRA / NJP DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private family tea-tasting experience featuring premium, organic leaves', 7),
            _ih('Curated by TRAGUIN Experts: Smooth pre-arranged permit processing for high-altitude zones,', 8),
            _ih('Premium Handpicked Hotels: Elite properties selected based on supreme safety, warm hospitality, and', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL AT IXB AIRPORT / NJP STATION TO GANGTOK',
                (
                    'GATEWAY TO THE CLOUD KINGDOM – SCENIC RIVERSIDE DRIVE Your premium Sikkim experience starts the moment you land at Bagdogra (IXB) Airport or arrive at New Jalpaiguri (NJP) Station. Your dedicated luxury transport vehicle and professional mountain chauffeur will be waiting to receive you. Embark on a highly scenic drive winding alongside the gorgeous, emerald-green Teesta River. Cross the border into Sikkim and climb into Gangtok, the mesmerizing capital city perched elegantly on a ridge. Check into your handpicked premium luxury hotel and enjoy your personalized welcome amenities. Spend your evening strolling leisurely down the clean, pedestrian-only MG Marg, taking in the vibrant local mountain culture.'
                ),
                [
                    'Sightseeing Included: Teesta River viewpoints, MG Marg pedestrian promenade walk.',
                    'Evening Experience: Explore boutique local cafes or shop for authentic prayer wheels and woolens.',
                    'Overnight Stay: Gangtok (Premium Luxury Mountain View Property)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'TSOMGO LAKE & BABA MANDIR EXCURSION',
                (
                    'SACRED ALPINE WATERS & LEGENDARY BORDER FRONTIERS Awake early to a crisp mountain morning and indulge in a lavish breakfast before setting off on a thrilling high- altitude excursion to Tsomgo Lake, situated at 12,400 feet. This sacred glacial lake is a top tourist place in Sikkim, surrounded by raw alpine terrain and reflecting breathtaking landscapes on its glassy surface. Enjoy an iconic yak ride along the snowline or capture family portraits at this pristine photography point. Continue your journey to the historic Baba Harbhajan Singh Memorial Mandir, deeply tied to local military lore. (Optional: Nathu La Pass border visit can be seamlessly incorporated on an extra permit basis).'
                ),
                [
                    'Sightseeing Included: Tsomgo Lake, Baba Harbhajan Singh Mandir, high-altitude alpine passes.',
                    'Optional Activities: Nathu La Pass border post excursion, high-altitude passenger ropeway ride.',
                    'Overnight Stay: Gangtok (Premium Luxury Mountain View Property)',
                    'Meals Included: Premium Breakfast & Gourmet Family Dinner',
                ],
            ),
            _day(
                3,
                'GANGTOK URBAN EXPEDITION TO PELLING',
                (
                    'CULTURE, SPIRITUALITY & THE JOURNEY WESTWARD Following a beautiful breakfast buffet, enjoy a curated half-day Gangtok sightseeing tour. Visit the famous Do Drul Chorten Stupa, the Namgyal Institute of Tibetology to view rare ancient manuscripts, and the beautiful Flower Exhibition Center. After lunch, sit back and enjoy exclusive experiences during your drive across rolling green valleys and terraced plantations to the charming hill town of Pelling in West Sikkim. Pelling is globally renowned for offering the absolute closest, most majestic views of Mt. Kanchenjunga. Check into your premium resort and relax with a breathtaking mountain panorama from your private balcony.'
                ),
                [
                    'Sightseeing Included: Do Drul Chorten, Tibetology Institute, Flower Show, Scenic West Sikkim Highway.',
                    'Evening Experience: Private family bonfire and local tea tasting session at your luxury resort.',
                    'Overnight Stay: Pelling (Premium Luxury Ridge Resort)',
                    'Meals Included: Premium Breakfast & Authentic Local Cuisine Dinner',
                ],
            ),
            _day(
                4,
                'PELLING FULL DAY EXCURSION',
                (
                    "WALKING AMONG THE CLOUDS – MONASTERIES & GLASS SKYWALKS Dedicate your day to exploring the legendary heritage and scenic beauty of Pelling. Begin at the breathtaking Rimbi Waterfalls and the sacred Khecheopalri Lake, fondly known as the wish-fulfilling lake, where birds are said to keep the water clear of leaves. Next, climb to the towering 137-foot Chenrezig Statue and experience the thrilling Pelling Skywalk—India's first glass skywalk and a highly popular Instagram location. Walk out onto transparent glass over deep gorges, looking directly across at giant mountain ranges. Conclude your tour with a tranquil walk through the historic ruins of Rabdentse, the ancient 17th-century second capital of Sikkim. Ruins."
                ),
                [
                    'Sightseeing Included: Chenrezig Statue, Glass Skywalk, Khecheopalri Lake, Rimbi Falls, Rabdentse Palace',
                    'Optional Activities: Traditional Sikkimese family dress photography session inside the historical ruins.',
                    'Overnight Stay: Pelling (Premium Luxury Ridge Resort)',
                    'Meals Included: Premium Breakfast & Royal Buffet Dinner',
                ],
            ),
            _day(
                5,
                'PELLING TO GANGTOK (VIA RAVANGLA BUDDHA PARK)',
                (
                    'THE PATH OF ENLIGHTENMENT – COLLOSSAL ECO-LANDSCAPES Bid a fond farewell to Pelling and start your return loop toward Gangtok, traveling via the spectacular town of Ravangla. Stop at the world-famous Tathagata Tsal, also known as the Buddha Park of Ravangla, featuring a magnificent, 130-foot-tall copper statue of Lord Buddha set against a backdrop of sweeping mountain cliffs. Spend time walking through manicured eco-gardens and taking in the spiritual chanting. Arrive in Gangtok by late afternoon, check back into your luxury hotel, and enjoy a final evening of personal shopping or fine dining.'
                ),
                [
                    'Sightseeing Included: Buddha Park of Ravangla, Temi Tea Garden views (en-route).',
                    'Evening Experience: Grand farewell family dinner curated by TRAGUIN experts at a top-tier mountain bistro.',
                    'Overnight Stay: Gangtok (Premium Luxury Mountain View Property)',
                    'Meals Included: Premium Breakfast & Farewell Celebration Dinner',
                ],
            ),
            _day(
                6,
                'GANGTOK TO BAGDOGRA / NJP DEPARTURE',
                (
                    'CARRYING HOME MEMORIES BEYOND DESTINATIONS Indulge in a final lavish breakfast at your premium hotel while the morning sun highlights the surrounding ridges. Your private luxury transport vehicle will wait to guide you smoothly back down the mountain highway to Bagdogra Airport or New Jalpaiguri Railway Station. As you board your flight or train back home, you will carry a heart full of deep family bonds, beautiful photos, and unforgettable memories designed exclusively by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door downhill transit drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Summit Golden Crescent /',
                'Gangtok',
                '5N',
                'Deluxe',
                'Hotel Sonam Delek',
                'The Elgin Mount Pandim /',
                4,
                1,
                description='OPTION 01 – DELUXE: Summit Golden Crescent / | Hotel Sonam Delek | The Elgin Mount Pandim /',
            ),
            _hotel(
                'Lemon Tree Premier /',
                'Gangtok',
                '5N',
                'Premium',
                'Ramada by Wyndham',
                'Magpie The Chestnut',
                4,
                2,
                description='OPTION 02 – PREMIUM: Lemon Tree Premier / | Ramada by Wyndham | Magpie The Chestnut',
            ),
            _hotel(
                'The Elgin Nor-Khill / Mayfair',
                'Gangtok',
                '5N',
                'Luxury',
                'Spa Resort',
                'Chumbi Mountain Retreat &',
                4,
                3,
                description='OPTION 03 – LUXURY: The Elgin Nor-Khill / Mayfair | Spa Resort | Chumbi Mountain Retreat &',
            ),
            _hotel(
                'Mayfair Spa Resort (Grand',
                'Gangtok',
                '5N',
                'Ultra Luxury',
                'Executive Suite)',
                'The Chumbi Mountain',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Mayfair Spa Resort (Grand | Executive Suite) | The Chumbi Mountain',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury accommodations as selected across Gangtok & Pelling.', 1),
            _inc_included('Luxury Transportation: Private SUV (Innova/ Crysta) for the entire route.', 2),
            _inc_included('Curated Meals: Lavish daily breakfasts and multi-course dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest experience manager on duty.', 4),
            _inc_included('Welcome Kit: Personalized mountain family arrival kit and permits assistance.', 5),
            _inc_included('Complimentary Experience: Private entry access passes to Pelling Glass Skywalk.', 6),
            _inc_excluded('Airfare, flight bookings, or long-distance train tickets to IXB/NJP.', 7),
            _inc_excluded('Nathu La Pass permits and extra vehicle costs (can be added on request).', 8),
            _inc_excluded('Personal items such as laundry, phone calls, premium drinks, or tips.', 9),
            _inc_excluded('Optional activities like yak rides, helicopter rides, or adventure sports.', 10),
        ],
    )
    return package, itinerary

def build_sk_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SK-003'
    tour_code = 'TRG-SIK-003'
    title = 'NORTH SIKKIM EXPLORER • ULTIMATE HIGH-ALTITUDE EXPEDITION'
    duration = '05 Nights / 06 Days'
    slug = 'sk-003-north-sikkim-explorer-ultimate-high-altitude-expedition'
    itin_slug = 'sk-003-north-sikkim-explorer-ultimate-high-altitude-expedition-itinerary'
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
            _ph('Serial code SK-003 | TRAGUIN tour code TRG-SIK-003', 1),
            _ph('State / Country: Sikkim / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Gangtok • Sikkim', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury 4WD (Innova / Scorpio) / Full Board (APAI) in Hills', 7),
            _ph('TRAGUIN Signature Experience: Hand-packed luxury snack-box and thermal beverages provided for', 8),
            _ph('Curated by TRAGUIN Experts: Perfect vehicle staging and permit clearance arranged ahead of time to', 9),
            _ph('Premium Handpicked Hotels: Accommodations chosen strictly based on heated amenities, structural', 10),
            _ph('Luxury Transportation: Background-verified, highly experienced mountain drivers who are well-versed in', 11)
        ],
        moods=['Luxury', 'Adventure'],
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
        tagline='NORTH SIKKIM EXPLORER',
        overview='NORTH SIKKIM EXPLORER • ULTIMATE HIGH-ALTITUDE EXPEDITION Welcome to a breathtaking high-altitude alpine expedition conceptualized and executed by TRAGUIN. Embark on the definitive North Sikkim Explorer itinerary, meticulously engineered for bold souls who crave untamed paths, roaring waterfalls, and majestic snow-capped peaks. As your premier luxury travel consultants, TRAGUIN transforms this challenging mountain safari into a highly secure, comfortable, and deeply immersive adventure holiday. From the vibrant culture of Gangtok to the sacred shores of Gurudongmar Lake and the stunning rhododendron fields of Yumthang Valley, every detail guarantees an elite, unforgettable memory.\n\nTOUR OVERVIEW\nThis custom-crafted adventure package offers a seamless balance between rugged exploration and premium comfort. Navigating the mountain terrain requires expertise; hence, you will travel in a dedicated, rugged private 4WD vehicle driven by a highly skilled alpine chauffeur. Featuring custom hospitality, a carefully organized meal plan, and essential high-altitude inner-line permits handled smoothly by our specialists, this route represents the gold standard of a premium Sikkim experience. Every milestone of your journey features the signature touch of TRAGUIN curated experiences, ensuring handpicked mountain stays, prioritized safety protocol, and uncompromised luxury amidst remote landscapes.\n\nWHY CHOOSE THE BEST SIKKIM TOUR PACKAGE?\nWhen considering a Luxury Sikkim Holiday, true adventurers demand a flawless blend of remote discovery and operational perfection. The rugged terrain of North Sikkim holds some of the most iconic attractions in Asia. From the sacred, emerald waters of Gurudongmar Lake—standing proudly at an altitude of 17,800 feet as a top tourist place in Sikkim—to the mist-laden gorges of Lachen and Lachung, the visual grandeur is incomparable. For couples seeking an offbeat adventure, our curated Sikkim Honeymoon Package provides deep isolation amidst breathtaking landscapes, while our Sikkim Family Tour setups offer a secure window into the vibrant local Buddhist culture. Capture popular Instagram locations like the Amitabh Bachchan Falls, Singhik Viewpoint, and the snow fields of Zero Point (Yumesamdong). Whether you seek adrenaline-pumping mountain drives, shopping for rare Tibetan artifacts, or tasting organic Himalayan food, our TRAGUIN Sikkim Packages guarantee premium stays and exclusive experiences during the best time to visit Sikkim. TRAGUIN Premium Luxury Itinerary — SK-003 2',
        seo_title='SK-003 | NORTH SIKKIM EXPLORER | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Sikkim package (SK-003 / TRG-SIK-003): Gangtok • Sikkim with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GANGTOK', 1),
            _ih('Day 02: GANGTOK TO LACHEN', 2),
            _ih('Day 03: LACHEN TO GURUDONGMAR LAKE TO LACHUNG', 3),
            _ih('Day 04: LACHUNG TO YUMTHANG VALLEY TO GANGTOK', 4),
            _ih('Day 05: EXCURSION TO TSOMGO LAKE & BABA MANDIR', 5),
            _ih('Day 06: GANGTOK TO DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Hand-packed luxury snack-box and thermal beverages provided for', 7),
            _ih('Curated by TRAGUIN Experts: Perfect vehicle staging and permit clearance arranged ahead of time to', 8),
            _ih('Premium Handpicked Hotels: Accommodations chosen strictly based on heated amenities, structural', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GANGTOK',
                (
                    "GATEWAY TO THE EASTERN HIMALAYAS – URBAN COMFORT & CULTURE Your premium Sikkim experience starts the moment you arrive at Bagdogra Airport (IXB) or New Jalpaiguri Railway Station (NJP). Your private luxury transport chauffeur welcomes you warmly and navigates the scenic route along the emerald Teesta River. Arrive in Gangtok, the hill state's sophisticated capital, and check into your handpicked luxury property. Spend the evening strolling down the pedestrian-only MG Marg for local lifestyle photography, premium souvenir shopping, or relaxing at an elite café."
                ),
                [
                    'Sightseeing Included: Teesta River viewpoint drive, MG Marg lifestyle promenade.',
                    'Evening Experience: Private welcome briefing by our tour manager over specialized local tea.',
                    'Overnight Stay: Gangtok (Premium Luxury Hotel)',
                    'Meals Included: Welcome Drink & Gourmet Dinner',
                ],
            ),
            _day(
                2,
                'GANGTOK TO LACHEN',
                (
                    'JOURNEY INTO THE UNTAMED NORTH – RUGGED GORGES & WATERFALLS After a hearty early breakfast, your high-altitude alpine drive to North Sikkim begins. As your 4WD ascends, witness the landscapes transform into steep gorges, dense pine forests, and roaring waterfalls. Stop along the route to capture breathtaking photographs at the historic Singhik Viewpoint, which offers a dramatic view of Mt. Khangchendzonga, and admire the majestic Seven Sisters Waterfall. Arrive by evening at the quiet, alpine hamlet of Lachen (8,838 ft) and check into your handpicked mountain retreat.'
                ),
                [
                    'Sightseeing Included: Singhik Viewpoint, Seven Sisters Waterfall, Naga Waterfall, Chunthang Confluence.',
                    'Optional Activities: A short evening walk through the serene, traditional Lachen monastery village.',
                    'Overnight Stay: Lachen (Premium Mountain Lodge / Best Available Stay)',
                    'Meals Included: Breakfast, Hot Mid-route Lunch & Local Mountain Dinner',
                ],
            ),
            _day(
                3,
                'LACHEN TO GURUDONGMAR LAKE TO LACHUNG',
                (
                    'SACRED SNOWFIELDS AT 17,800 FEET – THE PINNACLE OF ADVENTURE An unforgettable day unfolds with a pre-dawn departure (approx. 04:00 AM) toward the trans-Himalayan desert of Chopta Valley. Ascend further to arrive at the legendary Gurudongmar Lake, one of the highest and most sacred lakes in the world. Encircled by frozen peaks, its crystal-clear sapphire water remains unfrozen in one specific spot, believed to be blessed. Soak in the profound silence and capture once-in-a-lifetime photographs. Return to Lachen for lunch, pack up, and drive across to the charming valley village of Lachung.'
                ),
                [
                    'Sightseeing Included: Gurudongmar Lake, Chopta Valley high-altitude desert, Thangu Valley outpost.',
                    'Evening Experience: A warm, cozy bonfire evening at your Lachung resort to recover from the high altitude.',
                    'Overnight Stay: Lachung (Premium Luxury Mountain Resort)',
                    'Meals Included: Early Breakfast, Lunch & Evening Special Dinner',
                ],
            ),
            _day(
                4,
                'LACHUNG TO YUMTHANG VALLEY TO GANGTOK',
                (
                    "THE VALLEY OF FLOWERS & THE MAJESTIC ZERO POINT Awake to beautiful snowy views and travel to the famous Yumthang Valley, popularly known as the 'Valley of Flowers'. During spring, the entire valley turns into a vibrant, colorful blanket of wild rhododendrons and primulas. For true thrill-seekers, extend your drive to Yumesamdong, famously called Zero Point—the last outpost of civilization where the road ends amidst heavy, eternal snow. Return to Lachung for a warm lunch before heading back to Gangtok down the mountain roads."
                ),
                [
                    'Sightseeing Included: Yumthang Valley, Hot Sulphur Springs, Zero Point (Yumesamdong).',
                    'Optional Activities: Sampling piping hot local mountain noodles in the snow at Zero Point.',
                    'Overnight Stay: Gangtok (Premium Luxury Hotel)',
                    'Meals Included: Breakfast, Lunch & Farewell Gangtok Dinner',
                ],
            ),
            _day(
                5,
                'EXCURSION TO TSOMGO LAKE & BABA MANDIR',
                (
                    "GLACIAL SPLENDOUR & HISTORIC SILK ROUTE BORDERS Dedicate your day to an iconic alpine excursion on the historic Silk Route trade border. Drive up steep winding roads to visit the glacial Tsomgo Lake (Changu Lake), resting at 12,400 feet. The lake's deep water reflects the shifting colors of the sky and the surrounding snow-capped peaks perfectly. Continue onward to the revered Baba Harbhajan Singh Memorial Shrine, rich with moving military lore. Return to Gangtok by late afternoon for your last evening of shopping and relaxation. permit)."
                ),
                [
                    'Sightseeing Included: Glacial Tsomgo Lake, Baba Harbhajan Singh Shrine, Nathula Pass viewpoint (subject to',
                    'Evening Experience: Reserved table at a premium lounge bar in Gangtok, curated by TRAGUIN experts.',
                    'Overnight Stay: Gangtok (Premium Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Elegant Dinner',
                ],
            ),
            _day(
                6,
                'GANGTOK TO DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES OF THE HIMALAYAS Enjoy your final luxury breakfast at your premium hotel while taking in the morning mountain views. Board your private vehicle for a comfortable drive back to Bagdogra Airport (IXB) or NJP Station. Head home carrying a heart filled with thrilling stories and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury airport / rail station drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Summit Golden Crescent /',
                'Gangtok',
                '5N',
                'Deluxe',
                'similar',
                'Hotel Summit Lachen /',
                4,
                1,
                description='OPTION 01 – DELUXE: Summit Golden Crescent / | similar | Hotel Summit Lachen /',
            ),
            _hotel(
                'Lemon Tree Premier /',
                'Gangtok',
                '5N',
                'Premium',
                'Ramada Gangtok',
                'Lachen View Heritage /',
                4,
                2,
                description='OPTION 02 – PREMIUM: Lemon Tree Premier / | Ramada Gangtok | Lachen View Heritage /',
            ),
            _hotel(
                'The Elgin Nor-Khill /',
                'Gangtok',
                '5N',
                'Luxury',
                'Mayfair Resort',
                'The Delight Lachen',
                4,
                3,
                description='OPTION 03 – LUXURY: The Elgin Nor-Khill / | Mayfair Resort | The Delight Lachen',
            ),
            _hotel(
                'Mayfair Spa Resort &',
                'Gangtok',
                '5N',
                'Ultra Luxury',
                'Casino (Villas)',
                'VVIP Custom Private',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Mayfair Spa Resort & | Casino (Villas) | VVIP Custom Private',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Selected handpicked hotels as per the chosen luxury tier.', 1),
            _inc_included('Luxury Transportation: Private 4WD vehicle for all North Sikkim travel.', 2),
            _inc_included('All Permits Handled: Inner Line Permits for restricted border zones included.', 3),
            _inc_included('TRAGUIN Support: 24/7 specialized ground manager for remote tracking.', 4),
            _inc_included('Welcome Amenities: Personalized warm fleece kit and high-altitude health kit.', 5),
            _inc_included('Complimentary Experience: Evening warm bonfire setup at the Lachung resort.', 6),
            _inc_excluded('Airfare, flight connections, or mainline train tickets.✘ Zero Point or Nathula Pass extra driver allowances (paid on-site).', 7),
            _inc_excluded('Personal expenses such as laundry, phone calls, premium beverages, tips.', 8),
            _inc_excluded('Insurance, medical evacuation costs, or unforeseen roadblock costs.', 9),
        ],
    )
    return package, itinerary

def build_sk_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SK-004'
    tour_code = 'TRG-SIK-004'
    title = 'ROMANTIC SIKKIM • LOVE AMIDST MYSTIC MOUNTAINS'
    duration = '05 Nights / 06 Days'
    slug = 'sk-004-romantic-sikkim-love-amidst-mystic-mountains'
    itin_slug = 'sk-004-romantic-sikkim-love-amidst-mystic-mountains-itinerary'
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
            _ph('Serial code SK-004 | TRAGUIN tour code TRG-SIK-004', 1),
            _ph('State / Country: Sikkim / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Gangtok • Tsomgo', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Innova Crysta / MAPAI (Breakfast & Dinner)', 7),
            _ph("TRAGUIN Signature Experience: Private couple's hot mountain cocoa service overlooking the ravines of", 8),
            _ph('Curated by TRAGUIN Experts: Seamless processing of restricted area mountain permits prior to your', 9),
            _ph('Premium Handpicked Hotels: Accommodations selected for their exceptional room views, hospitality', 10),
            _ph('Luxury Transportation: Elite hill-certified chauffeurs ensure a smooth and safe journey across mountain', 11)
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
        tagline='ROMANTIC SIKKIM',
        overview="Welcome to a timeless mountain romance crafted exclusively by TRAGUIN. Embark on the ultimate Sikkim Honeymoon Package, meticulously curated to reveal the breathtaking landscapes, emerald-green valleys, and snow-kissed alpine lakes of India's most pristine mystical state. As your elite travel consultants, TRAGUIN transforms your romantic getaway into a premium luxury holiday filled with premium stays, TRAGUIN Premium Luxury Itinerary — SK-004 1 intimate candle-lit evenings, and highly customized immersive experiences. Let the scenic beauty of the mighty Mt. Khangchendzonga and the spiritual resonance of ancient monasteries pave the way for unforgettable memories with your partner.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package is engineered exclusively for newlyweds looking for the perfect blend of high-altitude adventure, deep natural serenity, and sophisticated hospitality. Travelling across the dramatic mountain terrains in a dedicated private premium luxury vehicle with an expert local chauffeur, you will enjoy absolute safety and comfort. Featuring a rich meal plan with daily premium breakfasts and custom multi-course dinners, your route captures the definitive premium Sikkim experience. Every detail from priority entry to private lookouts includes the signature TRAGUIN curated experience note to ensure your journey is flawless.\n\nWHY CHOOSE THE BEST SIKKIM TOUR PACKAGE?\nWhen exploring options for a Luxury Sikkim Holiday, romantic couples seek a sanctuary that blends serene valley retreats with majestic mountain adventures. Sikkim is home to some of the most iconic attractions in Northeast India. From the high-altitude alpine allure of Tsomgo Lake—a top tourist place in Sikkim—to the historic and dramatic Skywalk in Pelling, the region offers breathtaking panoramic views. For couples searching for a memorable Sikkim Honeymoon Package or an elegant Sikkim Family Tour, the region reveals incredibly scenic and popular Instagram locations like the Buddha Park of Ravangla, the mist-veiled tea gardens, and the vibrant cafes of Gangtok’s MG Marg. Whether you want to enjoy handicraft shopping at local curio markets, indulge in authentic Himalayan cuisine, or witness pristine waterfalls, our customized TRAGUIN Sikkim Packages guarantee handpicked hotels, premium comfort, and curated exclusive experiences that make any season the best time to visit Sikkim.",
        seo_title='SK-004 | ROMANTIC SIKKIM | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Sikkim package (SK-004 / TRG-SIK-004): Gangtok • Tsomgo with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL AT IXB AIRPORT & TRANSFER TO GANGTOK', 1),
            _ih('Day 02: EXCURSION TO TSOMGO LAKE & BABA MANDIR', 2),
            _ih('Day 03: GANGTOK URBAN EXPLORATION TO PELLING VIA RAVANGLA', 3),
            _ih('Day 04: PELLING FULL DAY SIGHTSEEING', 4),
            _ih('Day 05: PELLING TO GANGTOK (OR OPTIONAL RETREAT STAY)', 5),
            _ih('Day 06: DEPARTURE FROM GANGTOK TO IXB / NJP', 6),
            _ih("TRAGUIN Signature Experience: Private couple's hot mountain cocoa service overlooking the ravines of", 7),
            _ih('Curated by TRAGUIN Experts: Seamless processing of restricted area mountain permits prior to your', 8),
            _ih('Premium Handpicked Hotels: Accommodations selected for their exceptional room views, hospitality', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL AT IXB AIRPORT & TRANSFER TO GANGTOK',
                (
                    'WELCOME TO THE HIMALAYAN REALM – PRIVATE ESCORT TO CAPITAL HILLS Your premium Sikkim experience starts the moment you land at Bagdogra International Airport (IXB) or arrive at NJP Railway Station. Your private luxury transport and professional chauffeur will welcome you with customized refreshments. Enjoy a scenic route along the emerald-green Teesta River as you climb through mountain passes toward Gangtok, the beautiful capital of Sikkim. Check into your handpicked premium luxury hotel, where a special honeymoon cake and welcome amenities await you.'
                ),
                [
                    'Sightseeing Included: Teesta River viewpoint drive, Gangtok pine valley scenery.',
                    'Evening Experience: Leisurely walk through MG Marg; dinner curated by TRAGUIN experts.',
                    'Overnight Stay: Gangtok (Premium / Luxury Mountain Resort)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'EXCURSION TO TSOMGO LAKE & BABA MANDIR',
                (
                    'BREATHTAKING LANDSCAPES & HIGH-ALTITUDE SACRED WATERS Awake early for a spectacular morning drive to the legendary Tsomgo Lake, situated at an altitude of 12,400 feet. This oval-shaped alpine lake is surrounded by rugged, snow-capped peaks and offers truly breathtaking landscapes. Enjoy a romantic lakeside stroll and a unique yak ride before continuing on to the historic Baba Harbhajan Singh Mandir. Capture stunning photographs at these top tourist places in Sikkim.'
                ),
                [
                    'Sightseeing Included: Tsomgo Sacred Lake, Baba Harbhajan Singh Memorial Shrine.',
                    'Optional Activities: Nathu La Pass excursion (subject to permit availability and weather conditions).',
                    'Overnight Stay: Gangtok (Premium / Luxury Mountain Resort)',
                    'Meals Included: Premium Breakfast & Romantic Custom Dinner',
                ],
            ),
            _day(
                3,
                'GANGTOK URBAN EXPLORATION TO PELLING VIA RAVANGLA',
                (
                    "MISTIC SPIRITUALITY & THE MAJESTIC BUDDHA PARK After a delicious breakfast, enjoy a brief tour of Gangtok's top attractions, including the Do Drul Chorten Stupa and the Namgyal Institute of Tibetology. Then, set off on a scenic mountain drive to Pelling. En route, experience the serene beauty of Ravangla and stop at the Buddha Park, home to a majestic 130-foot miniature-mountainside statue of Lord Buddha. This popular Instagram location is surrounded by well- manicured eco-gardens."
                ),
                [
                    'Sightseeing Included: Buddha Park Ravangla, Do Drul Chorten, Ropeway view points.',
                    'Evening Experience: Private luxury check-in at Pelling with views of the Khangchendzonga range.',
                    'Overnight Stay: Pelling (Ultra-Luxury Suite / Premium Villa)',
                    'Meals Included: Premium Breakfast & Traditional Sikkimese Gourmet Dinner',
                ],
            ),
            _day(
                4,
                'PELLING FULL DAY SIGHTSEEING',
                (
                    "WALKING ACROSS THE CLOUDS – ICONIC ATTRACTIONS & SKYWALK Experience a breathtaking sunrise over the mountains right from your balcony. Today, enjoy a premium Pelling sightseeing tour that includes a walk across India's first glass skywalk, which looks out over the giant statue of"
                ),
                [
                    'Sightseeing Included: Pelling Glass Skywalk, Chenrezig Statue, Rabdentse Ruins, Khecheopalri Wish Lake,',
                    'Evening Experience: Honeymoon Special: A private, intimate candle-lit dinner with a premium menu.',
                    'Overnight Stay: Pelling (Ultra-Luxury Suite / Premium Villa)',
                    'Meals Included: Premium Breakfast & Special Candle-lit Celebration Dinner',
                ],
            ),
            _day(
                5,
                'PELLING TO GANGTOK (OR OPTIONAL RETREAT STAY)',
                (
                    'UNWINDING IN THE VALLEY OF MIST & ALPINE SERENITY Enjoy a relaxed morning at your luxury property before a scenic drive back to Gangtok via a different route, passing rustic tea gardens and terraced mountains. Take the afternoon to unwind at a premium wellness spa or enjoy shopping for local souvenirs. Spend your final evening enjoying artisan coffees and live music at a high-end cafe in the hills.'
                ),
                [
                    'Sightseeing Included: Pemayangtse Monastery, optional Temi Tea Garden valley drive.',
                    "Optional Activities: A couple's hot stone spa massage or an authentic local tea-tasting experience.",
                    'Overnight Stay: Gangtok (Premium Luxury Spa Hotel)',
                    'Meals Included: Premium Breakfast & Farewell Dinner',
                ],
            ),
            _day(
                6,
                'DEPARTURE FROM GANGTOK TO IXB / NJP',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Savor a final lavish breakfast as the morning sun illuminates the mountain peaks. Pack your bags as your private luxury vehicle prepares for the smooth downward drive toward Bagdogra International Airport (IXB) or NJP Station. Return home carrying a heart full of romance and unforgettable memories designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door station or airport drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Summit Golden',
                'Gangtok',
                '5N',
                'Deluxe',
                'Crescent / similar',
                'Summit Newroz Resort /',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Summit Golden | Crescent / similar | Summit Newroz Resort /',
            ),
            _hotel(
                'The Lemon Tree Hotel /',
                'Gangtok',
                '5N',
                'Premium',
                'Norbu Ghang',
                'The Elgin Mount Pandim /',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Lemon Tree Hotel / | Norbu Ghang | The Elgin Mount Pandim /',
            ),
            _hotel(
                'Mayfair Spa Resort &',
                'Gangtok',
                '5N',
                'Luxury',
                'Casino / Elgin',
                'Chumbi Mountain Retreat',
                4,
                3,
                description='OPTION 03 – LUXURY: Mayfair Spa Resort & | Casino / Elgin | Chumbi Mountain Retreat',
            ),
            _hotel(
                'Mayfair Imperial Villas',
                'Gangtok',
                '5N',
                'Ultra Luxury',
                '(Grand Suite)',
                'The Chumbi Retreat',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Mayfair Imperial Villas | (Grand Suite) | The Chumbi Retreat',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury valley-view rooms as per chosen category options.', 1),
            _inc_included('Luxury Transportation: Private dedicated Innova Crysta for all mountain routes.', 2),
            _inc_included('Curated Meal Plan: Daily premium breakfast and custom multicourse dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest experience manager and permit support.', 4),
            _inc_included('Honeymoon Privileges: Private candle-lit dinner setup, custom cake, and bed decoration.', 5),
            _inc_included('Complimentary Experience: Pair of priority access tickets for the Pelling Glass Skywalk.', 6),
            _inc_excluded('Airfare, flight tickets, or long-distance rail expenses to IXB/NJP.', 7),
            _inc_excluded('Nathu La Pass permit fees and additional vehicle border surcharges.', 8),
            _inc_excluded('Personal expenses such as laundry, premium telephone calls, or tips.', 9),
            _inc_excluded('Optional adventure sports, yak rides, ropeway tickets, or travel insurance.', 10),
        ],
    )
    return package, itinerary

def build_sk_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SK-005'
    tour_code = 'TRG-SKM-005'
    title = 'COMPLETE SIKKIM EXPLORER • ALPINE GRANDEUR & MYSTIC CULTURE'
    duration = '07 Nights / 08 Days'
    slug = 'sk-005-complete-sikkim-explorer-alpine-grandeur-mystic-culture'
    itin_slug = 'sk-005-complete-sikkim-explorer-alpine-grandeur-mystic-culture-itinerary'
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
            _ph('Serial code SK-005 | TRAGUIN tour code TRG-SKM-005', 1),
            _ph('State / Country: Sikkim / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Gangtok • Tsomgo Lake', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury 4WD (Innova/Xylo) / MAPAI & APAI', 7),
            _ph('TRAGUIN Signature Experience: Streamlined inner-line permit processing, saving your family hours of', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked mountain routes that balance scenic drives with family-friendly', 9),
            _ph('Premium Handpicked Hotels: Properties selected strictly for their reliable heating, exceptional hospitality, and', 10),
            _ph('Luxury Transportation: Specially certified, highly experienced mountain drivers ensuring elite comfort and', 11)
        ],
        moods=['Luxury', 'Nature', 'Culture'],
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
        tagline='COMPLETE SIKKIM EXPLORER',
        overview="CULTURE Welcome to a majestic Himalayan journey curated exclusively by TRAGUIN. Embark on the definitive Sikkim Family Tour, intricately crafted to reveal the breathtaking landscapes, sacred high-altitude glacial waters, and vibrant Buddhist traditions of this pristine mountain realm. As your premier travel consultants, TRAGUIN elevates your holiday into an opulent luxury escape, combining premium stays, expert coordination, and immersive TRAGUIN Premium Luxury Itinerary — SK-005 1 experiences. From the misty mountain paths of Gangtok to the ethereal, untouched expanses of North Sikkim, every single detail is orchestrated to generate unforgettable memories for your family.\n\nTOUR OVERVIEW\nThis elite itinerary offers an extensive exploration of the best Sikkim sightseeing gems. Traveling in a dedicated, heavy-duty luxury 4WD vehicle with a highly skilled local chauffeur, your family will experience seamless comfort across dramatic mountain terrains. Featuring a balanced meal plan—complete with premium breakfasts, fine-dining dinners, and freshly made high-altitude lunches—this route embodies the ultimate premium Sikkim experience. Every moment of your vacation includes the signature TRAGUIN curated experience note, ensuring private permits, VIP route coordination, and dedicated round-the-clock guest support.\n\nWHY CHOOSE THE BEST SIKKIM TOUR PACKAGE?\nWhen considering a Luxury Sikkim Holiday, travelers expect a profound sensory awakening amidst the snow- capped peak of Mount Kanchenjunga. Choosing a premium Sikkim Honeymoon Package or Sikkim Family Tour unlocks access to iconic attractions that are celebrated worldwide. From the legendary, holy waters of Tsomgo Lake to the dramatic floral blooms of Yumthang Valley—widely regarded as the top tourist places in Sikkim—this region offers an unrivaled spiritual and visual feast. For families documenting their travels, Sikkim reveals extraordinarily popular Instagram locations such as the colorful prayer-flag-draped paths of Gangtok's MG Marg, the majestic Buddha Park, and the reflective mirror waters of Gurudongmar Lake. Whether you are indulging in local hand-woven carpet shopping, tasting traditional steamed momos, or capturing the raw alpine scenic beauty of North Sikkim, our signature TRAGUIN Sikkim Packages guarantee handpicked hotels, safety-focused luxury transportation, and curated exclusive experiences that make it the best time to visit Sikkim.",
        seo_title='SK-005 | COMPLETE SIKKIM EXPLORER | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Sikkim package (SK-005 / TRG-SKM-005): Gangtok • Tsomgo Lake with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL AT IXB AIRPORT / NJP STATION TO GANGTOK', 1),
            _ih('Day 02: EXCURSION TO TSOMGO LAKE & BABA MANDIR', 2),
            _ih('Day 03: GANGTOK TO LACHEN (NORTH SIKKIM)', 3),
            _ih('Day 04: LACHEN TO GURUDONGMAR LAKE TO LACHUNG', 4),
            _ih('Day 05: LACHUNG TO YUMTHANG VALLEY TO GANGTOK', 5),
            _ih('Day 06: FULL DAY GANGTOK CITY SIGHTSEEING', 6),
            _ih('Day 07: EXCURSION TO PEMYANGTSE & RABI DENTSE RUINS', 7),
            _ih('Day 08: GANGTOK TO BAGDOGRA / NJP DEPARTURE', 8),
            _ih('TRAGUIN Signature Experience: Streamlined inner-line permit processing, saving your family hours of', 9),
            _ih('Curated by TRAGUIN Experts: Handpicked mountain routes that balance scenic drives with family-friendly', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL AT IXB AIRPORT / NJP STATION TO GANGTOK',
                (
                    'GATEWAY TO THE HIMALAYAS – ASCENT INTO CLOUD CITY Your premium Sikkim experience starts the moment you step out at Bagdogra Airport (IXB) or New Delhi / NJP Railway Station. A dedicated, private luxury vehicle from TRAGUIN awaits to usher you onto a scenic route winding past emerald tea gardens and along the rushing, sapphire waters of the Teesta River. Arrive at Gangtok, the vibrant hill capital, and check into your premium handpicked hotel. Spend your evening taking a relaxed stroll down the pedestrian-only MG Marg, taking in the clean mountain breeze and local café culture.'
                ),
                [
                    'Sightseeing Included: Teesta River viewpoint drive, Promenade walk at MG Marg.',
                    'Evening Experience: Exclusive high-tea briefing at a premium lounge hosted by TRAGUIN travel specialists.',
                    'Overnight Stay: Gangtok (Premium Luxury Hotel)',
                    'Meals Included: Welcome Drink & Gourmet Buffet Dinner',
                ],
            ),
            _day(
                2,
                'EXCURSION TO TSOMGO LAKE & BABA MANDIR',
                (
                    'SACRED GLACIAL WATERS & HIGH-ALTITUDE LEGENDS Enjoy an early morning breakfast before driving up the steep, thrilling hairpins to Tsomgo Lake, situated at an altitude of 12,400 feet. This deeply revered alpine lake offers breathtaking landscapes, changing its colors with the seasons and reflecting the grand peaks. Capture stunning photography points on a decorated yak ride. Continue further along the old Silk Route border to visit the legendary Baba Harbhajan Singh Mandir, a sacred shrine deeply embedded in local military lore.'
                ),
                [
                    'Sightseeing Included: Tsomgo Lake, Baba Harbhajan Singh Memorial Shrine.',
                    'Optional Activities: Nathu La Pass Indo-China Border excursion (subject to permit availability).',
                    'Overnight Stay: Gangtok (Premium Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'GANGTOK TO LACHEN (NORTH SIKKIM)',
                (
                    'JOURNEY TO THE WILD NORTH – THUNDERING WATERFALLS Depart today on an epic drive to North Sikkim, stoping to capture the sheer scenic beauty of the Seven Sisters Waterfalls and the misty Singhik Viewpoint. As you ascend toward Lachen (8,800 feet), watch the dense sub- tropical vegetation give way to dramatic, primeval pine and alpine forests. Check into your cozy, handpicked premium mountain lodge and experience authentic, warm mountain hospitality.'
                ),
                [
                    'Sightseeing Included: Seven Sisters Waterfalls, Naga Waterfalls, Singhik Viewpoint.',
                    'Evening Experience: Traditional local hearth gathering with freshly brewed butter tea.',
                    'Overnight Stay: Lachen (Selected Premium Mountain Lodge)',
                    'Meals Included: Breakfast, Hot Lunch en-route, Cozy Mountain Dinner',
                ],
            ),
            _day(
                4,
                'LACHEN TO GURUDONGMAR LAKE TO LACHUNG',
                (
                    'ETHEREAL VISIONS AT 17,800 FEET – THE SACRED MIRROR Before dawn, embark on a profound, sensory journey across the cold, wind-swept Tibetan Plateau to reach Gurudongmar Lake, one of the highest and most awe-inspiring freshwater lakes in the world. Encircled by sacred glaciated ridges, its crystal waters remain partially unfrozen even in sub-zero winter temperatures. After absorbing this life-changing view, return to Lachen for lunch and drive through beautiful valleys to the picture-perfect village of Lachung.'
                ),
                [
                    'Sightseeing Included: Gurudongmar Lake, Thangu Valley, Chopta Valley vistas.',
                    'Photography Points: High-altitude desert flats with grazing yaks against snow peaks.',
                    'Overnight Stay: Lachung (Premium Mountain Luxury Resort)',
                    'Meals Included: Early morning tea, Hot Lunch, Premium Dinner',
                ],
            ),
            _day(
                5,
                'LACHUNG TO YUMTHANG VALLEY TO GANGTOK',
                (
                    'THE VALLEY OF FLOWERS – A BOTANICAL PARADISE Drive through ancient, mist-covered rhododendron reserves to visit the iconic Yumthang Valley, popularly known as the Valley of Flowers. Surrounded by towering granite walls and crossed by a winding alpine river, the valley looks like a scene straight out of a storybook. Soak in the therapeutic hot springs before starting your smooth afternoon descent back to your luxury base in Gangtok.'
                ),
                [
                    'Sightseeing Included: Yumthang Valley, Sulphur Hot Springs, Shingba Rhododendron Sanctuary.',
                    'Optional Activities: Excursion further up to Zero Point (Yumesamdong) for touchable snowfields.',
                    'Overnight Stay: Gangtok (Premium Luxury Hotel)',
                    'Meals Included: Breakfast, Lunch on-the-go, Buffet Dinner',
                ],
            ),
            _day(
                6,
                'FULL DAY GANGTOK CITY SIGHTSEEING',
                (
                    'MONASTIC CHANTS & ARTISAN TRADITIONS Dedicate your day to exploring the elegant cultural heritage and top attractions of Gangtok. Visit the stunning Rumtek Monastery, the premier seat of the Kagyu lineage, to listen to the resonant chanting of young monks. Explore the Namgyal Institute of Tibetology to view priceless ancient manuscripts, and witness delicate traditional thangka painting craftsmanship at the Directorate of Handicrafts.'
                ),
                [
                    'Sightseeing Included: Rumtek Monastery, Do Drul Chorten, Tibetology Institute, Flower Show Complex.',
                    'Evening Experience: Private culinary workshop focusing on gourmet Himalayan momo making.',
                    'Overnight Stay: Gangtok (Premium Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Specialized Pan-Asian Dinner',
                ],
            ),
            _day(
                7,
                'EXCURSION TO PEMYANGTSE & RABI DENTSE RUINS',
                (
                    "THE ROYAL CHRONICLES OF OLD SIKKIM Take an enriching excursion into West Sikkim to uncover the roots of the Chogyal kingdom. Explore the magnificent Pemyangtse Monastery, standing proudly against the mountain backdrop. Then, take an easy walk through dense woods to reach the Rabdentse Ruins, the palace complex of Sikkim's ancient capital, where mossy stone walls frame spectacular views of the valley."
                ),
                [
                    'Sightseeing Included: Pemyangtse Monastery, Rabdentse Palace Ruins, Skywalk viewpoint corridors.',
                    'Evening Experience: Farewell dinner celebrating the completion of your ultimate Sikkim tour.',
                    'Overnight Stay: Gangtok (Premium Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Farewell Dinner',
                ],
            ),
            _day(
                8,
                'GANGTOK TO BAGDOGRA / NJP DEPARTURE',
                (
                    'CARRYING HOME SACRED MEMORIES Savor your final mountain breakfast as the morning sun lights up the peaks. Your private luxury transport will arrive to drive you back down along the scenic river highway to Bagdogra Airport (IXB) or NJP station. Board your flight home carrying a heart filled with sacred family bonds and unforgettable memories curated seamlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private airport/station door-to-door highway drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Summit Golden Crescent',
                'Sikkim',
                '7N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Summit Golden Crescent',
            ),
            _hotel(
                'Lemon Tree Premier / Hotel Royal Oasis Lachen View Heritage',
                'Sikkim',
                '7N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Lemon Tree Premier / Hotel Royal Oasis Lachen View Heritage',
            ),
            _hotel(
                'The Elgin Nor-Khill / Mayfair Resort The Apple Orchard Luxury Suite Yumthang Alpine Premium Chalet',
                'Sikkim',
                '7N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Elgin Nor-Khill / Mayfair Resort The Apple Orchard Luxury Suite Yumthang Alpine Premium Chalet',
            ),
            _hotel(
                'Mayfair Spa Resort & Casino (VVIP Villa) Elite Private Sanctuary Chalet The Grand Lachung Heritage Suite',
                'Sikkim',
                '7N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Mayfair Spa Resort & Casino (VVIP Villa) Elite Private Sanctuary Chalet The Grand Lachung Heritage S',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Selected heritage & luxury resort rooms.', 1),
            _inc_included('Luxury Transport: Private 4WD vehicle for North Sikkim terrain.', 2),
            _inc_included('Curated Meal Plan: Full breakfast and dinner arrays across all hotels.', 3),
            _inc_included('TRAGUIN Support: 24/7 inner-line permit liaison officer on standby.', 4),
            _inc_included('Welcome Amenities: Himalayan blessing scarves and travel kit on arrival.', 5),
            _inc_included('Complimentary Experience: Private family tea service at Yumthang valley.', 6),
            _inc_excluded('Personal expenses such as laundry, liquor, porterage, or tips.', 7),
            _inc_excluded('Insurance coverage parameters or unpredictable landslide block costs.', 8),
        ],
    )
    return package, itinerary

def build_sk_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SK-006'
    tour_code = 'TRG-SKM-006'
    title = 'EAST SIKKIM EXPLORER • PEAKS, PRAYERS & PRISTINE LAKES'
    duration = '04 Nights / 05 Days'
    slug = 'sk-006-east-sikkim-explorer-peaks-prayers-pristine-lakes'
    itin_slug = 'sk-006-east-sikkim-explorer-peaks-prayers-pristine-lakes-itinerary'
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
            _ph('Serial code SK-006 | TRAGUIN tour code TRG-SKM-006', 1),
            _ph('State / Country: Sikkim / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Gangtok • Tsomgo', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Priority inner-line permit processing handling, eliminating long border', 8),
            _ph('Curated by TRAGUIN Experts: Custom pacing tailored for senior citizens and children, minimizing high-', 9),
            _ph('Premium Handpicked Hotels: Accommodations selected strictly for their superior valley views, reliable', 10),
            _ph('Luxury Transportation: Certified hill-climb terrain luxury vehicles driven by background-verified regional', 11)
        ],
        moods=['Luxury', 'Nature'],
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
        tagline='EAST SIKKIM EXPLORER',
        overview="EAST SIKKIM EXPLORER • PEAKS, PRAYERS & PRISTINE LAKES TRAGUIN Premium Luxury Proposal — East Sikkim Explorer (SK-006) 1 Welcome to a magical journey into the clouds curated exclusively by TRAGUIN. Embark on the finest Sikkim Family Tour, designed to unearth the majestic heritage, snow-bound passes, and serene alpine waters of this mystical Himalayan kingdom. As your premier travel consultants, TRAGUIN turns your vacation into a seamless luxury holiday defined by handpicked hotels, breathtaking landscapes, and personalized service. Witness the timeless grandeur of Kanchenjunga and the spiritual charm of local monasteries, creating unforgettable memories for your family.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers a profound exploration of East Sikkim's natural wonders and vibrant cultural life. Travelling in an exclusive premium 4WD SUV with an expert mountain chauffeur, your family will experience absolute security, luxury, and comfort. With a curated meal plan featuring extensive morning breakfast spreads and personalized authentic dinners, this route delivers a true premium Sikkim experience. Every milestone of your vacation features the unique TRAGUIN curated experience note, giving you smooth permit clearances, handpicked premium stays, and complete elite support.\n\nWHY CHOOSE THE BEST SIKKIM TOUR PACKAGE?\nWhen seeking an unforgettable Luxury Sikkim Holiday, travelers look for majestic mountain panoramas, ancient culture, and modern boutique amenities. Sikkim stands out as a pristine ecological haven, making a Sikkim Family Tour or a romantic Sikkim Honeymoon Package the ultimate mountain choice. From the bustling avenues of Gangtok's MG Marg to the sacred alpine high points, Sikkim sightseeing promises unmatched serenity. Our tailored TRAGUIN Sikkim Packages bring you directly to top tourist places in Sikkim, such as the mystical Tsomgo Lake and the soaring heights of Nathula Pass on the Indo-China border. Explore popular Instagram locations like the Ban Jhakri Waterfalls, delve into local handloom shopping, or absorb panoramic mountain vistas from Ganesh Tok. Travel during the best time to visit Sikkim and enjoy curated exclusive experiences and premium handpicked hotels that turn your vacation into a legendary journey.",
        seo_title='SK-006 | EAST SIKKIM EXPLORER | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Sikkim package (SK-006 / TRG-SKM-006): Gangtok • Tsomgo with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL AT IXB / NJP TO GANGTOK', 1),
            _ih('Day 02: SACRED TSOMGO LAKE & BABA MANDIR EXCURSION', 2),
            _ih('Day 03: FULL DAY GANGTOK SIGHTSEEING', 3),
            _ih('Day 04: GANGTOK OUTSKIRTS & LANDSCAPE TOURS', 4),
            _ih('Day 05: GANGTOK TO IXB / NJP DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Priority inner-line permit processing handling, eliminating long border', 6),
            _ih('Curated by TRAGUIN Experts: Custom pacing tailored for senior citizens and children, minimizing high-', 7),
            _ih('Premium Handpicked Hotels: Accommodations selected strictly for their superior valley views, reliable', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL AT IXB / NJP TO GANGTOK',
                (
                    'WELCOME TO SIKKIM – GATEWAY TO THE EASTERN HIMALAYAS Your premium Sikkim experience starts the moment you land at Bagdogra Airport (IXB) or arrive at New Jalpaiguri Station (NJP). A dedicated private luxury SUV waits to escort you on a scenic route tracing the emerald-green Teesta River. As you rise into the higher altitudes, feel the fresh mountain breeze of Sikkim TRAGUIN Premium Luxury Proposal — East Sikkim Explorer (SK-006) 2 welcome your family. Upon arrival in Gangtok, check into your handpicked premium luxury hotel. Spend your evening taking a relaxed walk down the pedestrian-only MG Marg, taking in the alpine town ambiance, vibrant cafes, and local shopping delights. Welcome Drink & Luxury Buffet Dinner'
                ),
                [
                    'Sightseeing Included: Teesta River viewpoint, MG Marg evening promenade, local handicraft storefronts.',
                    'Evening Experience: Welcome evening briefing with fine dining curated by TRAGUIN experts.',
                    'Overnight Stay: Gangtok (Premium / Luxury Mountain Resort)',
                    'Meals: Included:',
                ],
            ),
            _day(
                2,
                'SACRED TSOMGO LAKE & BABA MANDIR EXCURSION',
                (
                    'MYSTICAL ALPINE LAKES & SNOW-CLAD BORDER VISIONS Awake early to crisp mountain air and enjoy a rich breakfast before embarking on a high-altitude excursion to the sacred Tsomgo Lake (Changu Lake), situated at an elevation of 12,400 feet. This glacial wonderland offers breathtaking landscapes, reflecting the surrounding snow peaks on its clear waters—a highly popular Instagram location. Capture unforgettable memories riding decorated yaks. Continue onward to the legendary Baba Harbhajan Singh Memorial Mandir, a sacred shrine steeped in deep military lore.'
                ),
                [
                    'Sightseeing Included: Tsomgo Glacial Lake, Baba Harbhajan Singh Shrine, snow-line viewpoints.',
                    'Optional Activities: Nathula Pass Indo-China Border excursion (subject to permit availability and extra cost).',
                    'Overnight Stay: Gangtok (Premium / Luxury Mountain Resort)',
                    'Meals Included: Premium Breakfast & Specialized Alpine Dinner',
                ],
            ),
            _day(
                3,
                'FULL DAY GANGTOK SIGHTSEEING',
                (
                    'BUDDHIST MONASTERIES, WATERFALLS & ROLETTO VIEWS Devote your day to an immersive experience of Gangtok sightseeing. Begin at the world-renowned Rumtek Monastery, a seat of Tibetan Buddhism showcasing spectacular ornate architecture and sacred relics. Visit Do Drul Chorten, surrounded by 108 prayer wheels, and the Namgyal Institute of Tibetology to explore rare historical manuscripts. Conclude your day capturing photography points at Ganesh Tok, enjoying a birds-eye view of the city layout against the sweeping horizon. TRAGUIN Premium Luxury Proposal — East Sikkim Explorer (SK-006) 3 Centre.'
                ),
                [
                    'Sightseeing Included: Rumtek Monastery, Ban Jhakri Waterfalls, Do Drul Chorten, Ganesh Tok, Flower Exhibition',
                    'Evening Experience: Private family traditional Sikkimese high tea experience overlooking the valleys.',
                    'Overnight Stay: Gangtok (Premium / Luxury Mountain Resort)',
                    'Meals Included: Premium Breakfast & Authentic Himalayan Dinner',
                ],
            ),
            _day(
                4,
                'GANGTOK OUTSKIRTS & LANDSCAPE TOURS',
                (
                    'HIDDEN GORGES, ROPEWAYS & PANORAMIC VALLEY ESCAPES Enjoy another day uncovering hidden Sikkim sightseeing gems. Ride the exciting Gangtok Ropeway to enjoy a sweeping panoramic view of the entire valley from above. Visit Tashi Viewpoint early to catch the gold-tinged colors of the morning sun hitting Mt. Kanchenjunga. Spend your afternoon visiting the Enchey Monastery and checking out local handloom factories where traditional hand-knotted carpets and Sikkimese wooden furniture are meticulously made.'
                ),
                [
                    'Sightseeing Included: Tashi Viewpoint, Gangtok Ropeway Ride, Directorate of Handicrafts, Enchey Monastery.',
                    'Optional Activities: Private organic local food-tasting walk trying artisanal momos and local thukpa.',
                    'Overnight Stay: Gangtok (Premium / Luxury Mountain Resort)',
                    'Meals Included: Premium Breakfast & Farewell Special Dinner',
                ],
            ),
            _day(
                5,
                'GANGTOK TO IXB / NJP DEPARTURE',
                (
                    'CHERISHING FAREWELL MOMENTS IN THE CLOUDS Savor a final lavish breakfast at your premium resort while looking out over the morning valley mist. Your private luxury SUV will pick you up for your comfortable journey back down to Bagdogra Airport (IXB) or New Jalpaiguri Station (NJP). Return home carrying a heart full of deep family bonds, scenic beauty, and unforgettable memories designed meticulously by TRAGUIN. TRAGUIN Premium Luxury Proposal — East Sikkim Explorer (SK-006) 4'
                ),
                [
                    'Transfers Included: Private luxury door-to-door airport or railway station drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Summit Golden Crescent / Hotel',
                'Gangtok',
                '4N',
                'Deluxe',
                'Sonam Delek / similar',
                'Deluxe Valley View',
                4,
                1,
                description='OPTION 01 – DELUXE: Summit Golden Crescent / Hotel | Sonam Delek / similar | Deluxe Valley View',
            ),
            _hotel(
                'Lemon Tree Hotel Gangtok / The Elgin',
                'Gangtok',
                '4N',
                'Premium',
                'Nor-Khill / similar',
                'Executive Balcony',
                4,
                2,
                description='OPTION 02 – PREMIUM: Lemon Tree Hotel Gangtok / The Elgin | Nor-Khill / similar | Executive Balcony',
            ),
            _hotel(
                'Mayfair Spa Resort & Casino /',
                'Gangtok',
                '4N',
                'Luxury',
                'Welcomheritage Denzong Regency',
                'Luxury Club Room /',
                4,
                3,
                description='OPTION 03 – LUXURY: Mayfair Spa Resort & Casino / | Welcomheritage Denzong Regency | Luxury Club Room /',
            ),
            _hotel(
                'The Elgin Heritage Suite / Mayfair',
                'Gangtok',
                '4N',
                'Ultra Luxury',
                'Grand Presidential Villa',
                'VVIP Custom Luxury',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Elgin Heritage Suite / Mayfair | Grand Presidential Villa | VVIP Custom Luxury',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 04 Nights accommodation in handpicked top-tier hotels.', 1),
            _inc_included('Luxury Transportation: Dedicated private luxury SUV for all transfers and sightseeing.', 2),
            _inc_included('Curated Meal Plan: Daily lavish morning breakfast spreads and gourmet family dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest relations manager and specialized ground assistance.', 4),
            _inc_included('Welcome Amenities: Customized traditional greeting scarfs, mineral water, and family travel kit.', 5),
            _inc_included('Complimentary Experience: Special high- altitude permit management and inner-line permits documentation.', 6),
            _inc_excluded('Airfare, flight tickets, or long-distance train tickets to Bagdogra/NJP.', 7),
            _inc_excluded('Nathula Pass dynamic permit fees and border vehicle upgrade costs.', 8),
            _inc_excluded('Personal expenses such as laundry, phone calls, premium liquor, and tips.', 9),
            _inc_excluded('Monument entry fees, monastery museum tickets, ropeway ride passes.', 10),
        ],
    )
    return package, itinerary

def build_sk_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SK-007'
    tour_code = 'TRG-SIK-007'
    title = 'GANGTOK • LACHUNG • YUMTHANG VALLEY ESCAPE 05 NIGHTS / 06 DAYS'
    duration = '05 Nights / 06 Days'
    slug = 'sk-007-gangtok-lachung-yumthang-valley-escape-05-nights-06-days'
    itin_slug = 'sk-007-gangtok-lachung-yumthang-valley-escape-05-nights-06-days-itinerary'
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
            _ph('Serial code SK-007 | TRAGUIN tour code TRG-SIK-007', 1),
            _ph('State / Country: Sikkim / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Gangtok • Sikkim', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury SUV (Innova/Xylo) / MAPAI (API in Lachung)', 7),
            _ph('TRAGUIN Signature Experience: Private family tea and refreshment break overlooking the gorgeous', 8),
            _ph('Curated by TRAGUIN Experts: Complete handling of high-altitude Inner Line Permits for North Sikkim with', 9),
            _ph('Luxury Transportation: Elite 4WD SUVs driven by experienced local mountain drivers for smooth travel over', 10)
        ],
        moods=['Luxury', 'Nature'],
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
        tagline='GANGTOK',
        overview='05 NIGHTS / 06 DAYS TRAGUIN Premium Luxury Itinerary — SK-007 1 Welcome note from your premier travel consultants: Welcome to a world of majestic high-altitude alpine wonders, pristine sacred waters, and vibrant Buddhist culture proudly crafted by TRAGUIN. Embark on the ultimate Sikkim Family Tour, intricately customized to showcase the breathtaking landscapes and profound spiritual legacy of North-East India. As your dedicated luxury experts, TRAGUIN elevates your journey into a seamless luxury holiday filled with premium stays, immersive experiences, and handpicked hotels. From the terraced hillsides of Gangtok to the dramatic, snow-dusted meadows of Lachung, every single milestone of this customized package is meticulously styled to leave your family with sweet, unforgettable memories.\n\nTOUR OVERVIEW\nThis elite, custom-tailored package features an exquisite alpine route spanning the vibrant capital of Gangtok and the dramatic high-altitude wilderness of North Sikkim. Traveling in an executive, private luxury 4WD SUV with a background-verified mountain chauffeur, your family will experience absolute security and cloud-like transit comfort. With an enriched meal plan encompassing wholesome breakfast buffets and signature local-infused gourmet dinners, this journey stands out as the definitive premium Sikkim experience. Every part of your passage contains the trademark TRAGUIN curated experience note, guaranteeing seamless inner line permits, premium high-altitude amenities, and around-the-clock remote concierge support.\n\nWHY VISIT SIKKIM? DISCOVER THE BEST SIKKIM TOUR PACKAGE\nWhen shortlisting options for a **Luxury Sikkim Holiday**, elite travelers prioritize breathtaking natural vistas, ancient heritage monasteries, and high-end hospitality. Sikkim offers some of the most iconic attractions in the entire Himalayan belt. From the mystical waters of Tsomgo Lake—a top tourist place in Sikkim—to the majestic alpine fields of Yumthang Valley, often referred to as the Valley of Flowers, the state is a living paradise. For couples planning an idyllic **Sikkim Honeymoon Package** or households seeking a secure, well-paced **Sikkim Family Tour**, this region reveals stunning Instagram locations like the zero-point glaciers, cascading waterfalls, and the colorful curio markets of Gangtok’s MG Marg. Whether you want to witness panoramic views of Mount Kanchenjunga, partake in deep Buddhist cultural immersion, or savor hot steamed momos at premium mountain cafes, booking our specialized **TRAGUIN Sikkim Packages** guarantees personalized premium stays and handpicked hotels. Plan during the best time to visit Sikkim to witness nature in its absolute, uninterrupted prime. TRAGUIN Premium Luxury Itinerary — SK-007 2',
        seo_title='SK-007 | GANGTOK | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Sikkim package (SK-007 / TRG-SIK-007): Gangtok • Sikkim with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: NJP STATION / BAGDOGRA TO GANGTOK', 1),
            _ih('Day 02: GANGTOK (EXCURSION TO TSOMGO LAKE & BABA MANDIR)', 2),
            _ih('Day 03: GANGTOK TO LACHUNG (NORTH SIKKIM)', 3),
            _ih('Day 04: LACHUNG TO YUMTHANG VALLEY TO GANGTOK', 4),
            _ih('Day 05: GANGTOK URBAN REVELRY & MONASTERY SPIRIT', 5),
            _ih('Day 06: GANGTOK TO BAGDOGRA / DEPARTURE', 6),
            _ih('TRAGUIN  Signature  Experience: Private  family  tea  and  refreshment  break  overlooking  the  gorgeous', 7),
            _ih('Curated by TRAGUIN Experts: Complete handling of high-altitude Inner Line Permits for North Sikkim with', 8),
            _ih('Luxury Transportation: Elite 4WD SUVs driven by experienced local mountain drivers for smooth travel over', 9)
        ],
        days=[
            _day(
                1,
                'NJP STATION / BAGDOGRA TO GANGTOK',
                (
                    'GATEWAY TO THE CLOUD KINGDOM – SCENIC TEESTA VALLEY RIDE Your premium Sikkim sightseeing journey begins upon arrival at Bagdogra Airport (IXB) or New Jalpaiguri Railway Station (NJP). Your dedicated luxury transport SUV waits to greet your family with premium welcome amenities. Ascend smoothly into the hills alongside the emerald-green Teesta River. Witness the changing foliage and pristine mountain valleys as you make your way toward Gangtok. Upon arrival, check into your premium handpicked hotel, unzip, and spend your evening exploring the pedestrian paradise of MG Marg for high-end boutique shopping, local cafes, and photography points. dinner.'
                ),
                [
                    'Sightseeing Included: Teesta River Viewpoints, Sevoke Coronation Bridge overview, MG Marg evening promenade.',
                    'Evening Experience: Bespoke evening walk guided by recommendations from TRAGUIN experts, followed by a fine',
                    'Overnight Stay: Gangtok (Premium / Luxury Mountain View Resort)',
                    'Meals Included: Welcome Drink & Luxury Buffet Dinner',
                ],
            ),
            _day(
                2,
                'GANGTOK (EXCURSION TO TSOMGO LAKE & BABA MANDIR)',
                (
                    'SACRED ALPINES & BREATHTAKING GLACIAL WATERWAYS Awake early for a spectacular high-altitude mountain drive to the sacred Tsomgo Lake, situated at an altitude of 12,400 feet. This glacial waterbody is renowned for its breathtaking landscapes and shifting surface colors across seasons. Enjoy a premium family photography session on brightly decorated Himalayan Yaks. Continue your drive to the legendary Baba Harbhajan Singh Mandir, filled with fascinating local military lore. boundary.'
                ),
                [
                    'Sightseeing Included: Tsomgo Oval Glacial Lake, Baba Harbhajan Singh Shrine, Kyongnosla Alpine Sanctuary',
                    'Optional Activities: Nathu La Pass Indo-China Border excursion (subject to permit availability and additional cost).',
                    'Overnight Stay: Gangtok (Premium / Luxury Mountain View Resort)',
                    'Meals Included: Premium Breakfast & Authentic Gourmet Dinner',
                ],
            ),
            _day(
                3,
                'GANGTOK TO LACHUNG (NORTH SIKKIM)',
                (
                    'JOURNEY TO THE RUGGED NORTH – WATERFALLS & MISTY CANYONS After a hearty breakfast, check out and drive north toward the alpine village of Lachung, nestled at 8,800 feet. This route is a dream for photography lovers, showcasing majestic mountains and dense coniferous forests. Stop'
                ),
                [
                    'Sightseeing Included: Singhik Viewpoint (Kanchenjunga overview), Naga Waterfalls, Chunthang Confluence, Bhim',
                    'Evening Experience: Cozy fireside family chat accompanied by hot local tea inside your premium resort.',
                    'Overnight Stay: Lachung (Premium Alpine Eco-Luxury Resort)',
                    'Meals Included: Breakfast, En-route Hot Lunch & Freshly Prepared Warm Dinner',
                ],
            ),
            _day(
                4,
                'LACHUNG TO YUMTHANG VALLEY TO GANGTOK',
                (
                    'THE VALLEY OF FLOWERS & UNTOUCHED SNOWFIELDS Embrace an unforgettable morning drive to the world-famous Yumthang Valley, famously called the Valley of Flowers. Surrounded by majestic snow-capped peaks and winding silver streams, the valley is a signature highlight of our premium Sikkim experience. Walk through the vast rhododendron sanctuaries and pine forests. After soaking in these breathtaking landscapes, bid farewell to the north and embark on a smooth return journey back to your luxury resort in Gangtok. fields.'
                ),
                [
                    'Sightseeing Included: Yumthang Valley Meadow, Hot Sulphur Springs, Singba Rhododendron Sanctuary.',
                    'Optional Activities: Excursion further up to Zero Point (Yumesamdong) at 15,000 feet for pristine touchable snow',
                    'Overnight Stay: Gangtok (Premium / Luxury Resort)',
                    'Meals Included: Breakfast & Post-Travel Relaxing Dinner',
                ],
            ),
            _day(
                5,
                'GANGTOK URBAN REVELRY & MONASTERY SPIRIT',
                (
                    "SACRED MANTRAS & PANORAMIC VALLEY VIEWS Dedicate your day to exploring the rich cultural heritage and iconic attractions of Gangtok. Visit the stunning Rumtek Monastery, a global seat of Tibetan Buddhism. Discover the unique collection of historical artifacts at the Namgyal Institute of Tibetology. Conclude your afternoon with an exciting aerial ropeway ride that gives your family a bird's-eye view of the city's terraced valleys."
                ),
                [
                    'Sightseeing Included: Rumtek Monastery, Do Drul Chorten Stupa, Tibetology Institute, Flower Show, Gangtok',
                    'Evening Experience: Farewell family dining experience featuring curated Sikkimese fusion delicacies.',
                    'Overnight Stay: Gangtok (Premium / Luxury Resort)',
                    'Meals Included: Premium Breakfast & Special Farewell Dinner',
                ],
            ),
            _day(
                6,
                'GANGTOK TO BAGDOGRA / DEPARTURE',
                (
                    'CHERISHING THE MEMORIES OF THE HIMALAYAS Indulge in a final lavish breakfast looking out over the misty mountain valleys. Your private luxury transport SUV will pick you up from the hotel and drive you back to Bagdogra Airport (IXB) or NJP Station. Return to your home destination carrying a heart full of joy, family bonding, and unforgettable memories custom-designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private door-to-door transit drop-off to station/airport.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Summit Golden Crescent',
                'Sikkim',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Summit Golden Crescent',
            ),
            _hotel(
                'Lemon Tree Hotel / Mayfair Spa Resort Lachung Continental',
                'Sikkim',
                '5N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Lemon Tree Hotel / Mayfair Spa Resort Lachung Continental',
            ),
            _hotel(
                'The Elgin Nor-Khill / Mayfair Elite Suite Yarlam Resort (Luxury Suite) Executive Luxury Suite',
                'Sikkim',
                '5N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Elgin Nor-Khill / Mayfair Elite Suite Yarlam Resort (Luxury Suite) Executive Luxury Suite',
            ),
            _hotel(
                'Vivanta Sikkim Pakyong / Mayfair Imperial The Retreat Lachung (VVIP Chalet) Royal Mountain View Villa',
                'Sikkim',
                '5N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Vivanta Sikkim Pakyong / Mayfair Imperial The Retreat Lachung (VVIP Chalet) Royal Mountain View Vill',
            )
        ],
        inclusions=[
            _inc_included('Luxury Transportation: Private dedicated SUV for all point-to-point travel and sightseeing.', 1),
            _inc_included('Curated Meal Plan: Daily premium breakfast and custom buffet dinners (MAPAI).', 2),
            _inc_included('TRAGUIN Support: 24/7 dedicated travel manager for real-time trip coordination.', 3),
            _inc_included('Welcome Amenities: Personalized family travel kit, warm refreshments, and fruit basket.', 4),
            _inc_included('Complimentary Experience: Reserved tickets for the scenic Gangtok Cable Car ride.', 5),
            _inc_excluded('Airfare, flight bookings, or mainline train tickets to West Bengal.', 6),
            _inc_excluded('Zero Point or Nathu La entry/permit extra supplement vehicle charges.', 7),
            _inc_excluded('Personal items such as laundry, alcoholic drinks, extra mineral water, or tips.', 8),
            _inc_excluded('Any insurance fees or unexpected costs caused by weather-related road blockages.', 9),
        ],
    )
    return package, itinerary

def build_sk_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SK-008'
    tour_code = 'TRG-SIK-008'
    title = 'SNOW ROMANCE SIKKIM • A HIMALAYAN LOVE AFFAIR'
    duration = '05 Nights / 06 Days'
    slug = 'sk-008-snow-romance-sikkim-a-himalayan-love-affair'
    itin_slug = 'sk-008-snow-romance-sikkim-a-himalayan-love-affair-itinerary'
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
            _ph('Serial code SK-008 | TRAGUIN tour code TRG-SIK-008', 1),
            _ph('State / Country: Sikkim / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Gangtok • Tsomgo', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury 4WD (Innova/ Xylo) / MAPAI & AP DROP', 7),
            _ph('TRAGUIN Signature Experience: Private roadside hot tea and cocoa station overlooking the freezing', 8),
            _ph('Curated by TRAGUIN Experts: Flawless management of protected area permits (PAP) in advance for a', 9),
            _ph('Premium Handpicked Hotels: Luxury properties selected strictly for outstanding valley views, top-tier', 10),
            _ph('Luxury Transportation: Expert mountain driving professionals well-trained in traversing challenging', 11)
        ],
        moods=['Luxury', 'Honeymoon'],
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
        tagline='SNOW ROMANCE SIKKIM',
        overview="Welcome to an ethereal romantic getaway curated exclusively by TRAGUIN. Embark on the ultimate Sikkim Honeymoon Package, meticulously crafted to showcase the breathtaking landscapes, alpine lakes, and dramatic snowy vistas of North Sikkim. As your dedicated luxury travel consultants, TRAGUIN delivers a highly customized experience filled with handpicked hotels, intimate candlelight moments, and premium TRAGUIN Premium Luxury Itinerary — SK-008 1 mountain comfort. Let the scenic beauty of the majestic Kanchenjunga range and mist-laden pine forests form the backdrop of your romantic journey, creating sweet unforgettable memories that last a lifetime.\n\nTOUR OVERVIEW\nThis bespoke luxury holiday package is engineered specifically for couples who seek a romantic and immersive experience in the heart of the Eastern Himalayas. Travelling in a completely private premium SUV vehicle with a highly professional, well-versed local chauffeur, your itinerary balances high-altitude leisure with deep mountain exploration. Enjoy a tailored meal plan featuring decadent daily breakfasts and personalized dinners, along with special honeymoon add-ons like flower bed decorations, a custom wedding cake, and candle-lit dining in Gangtok. Every aspect features the distinct TRAGUIN curated experience note, guaranteeing high-end hospitality and round-the-clock peace of mind.\n\nWHY CHOOSE THE BEST SIKKIM TOUR PACKAGE?\nWhen planning a Luxury Sikkim Holiday, couples look for a blend of alpine thrill, untouched nature, and quiet privacy. Sikkim stands out as a mystical crown jewel of North-East India, making a Sikkim Honeymoon Package the absolute dream choice for newlyweds. From exploring iconic attractions like the sacred, high- altitude Tsomgo Lake and Baba Mandir to seeking pristine floral tranquility in Yumthang Valley, Sikkim sightseeing offers an unmatched experience. Our tailored Sikkim Family Tour and romantic packages bring you closer to popular Instagram locations like the snow-blanketed valleys of Lachung, Zero Point, and the winding mountain passes of the Eastern Himalayas. Indulge in local handicraft shopping at Gangtok's MG Marg, relish authentic Tibetan and Sikkimese delicacies, or experience the pure bliss of a mountain-facing viewpoint. Our signature TRAGUIN Sikkim Packages combine exclusive experiences with premium stays, offering you the absolute best time to visit Sikkim with zero hassle.",
        seo_title='SK-008 | SNOW ROMANCE SIKKIM | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Sikkim package (SK-008 / TRG-SIK-008): Gangtok • Tsomgo with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GANGTOK', 1),
            _ih('Day 02: EXCURSION TO TSOMGO LAKE & BABA MANDIR', 2),
            _ih('Day 03: GANGTOK TO LACHUNG', 3),
            _ih('Day 04: YUMTHANG VALLEY EXCURSION & RETURN TO GANGTOK', 4),
            _ih('Day 05: GANGTOK LOCAL MONASTERY & VIEWPOINTS TOUR', 5),
            _ih('Day 06: GANGTOK TO BAGDOGRA / DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private roadside hot tea and cocoa station overlooking the freezing', 7),
            _ih('Curated by TRAGUIN Experts: Flawless management of protected area permits (PAP) in advance for a', 8),
            _ih('Premium Handpicked Hotels: Luxury properties selected strictly for outstanding valley views, top-tier', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GANGTOK',
                (
                    'WELCOME TO THE HIMALAYAN REALM – HIGHLAND LUXURY CHECK-IN Your premium Sikkim experience begins with a warm greeting at Bagdogra Airport (IXB) or New Jalpaiguri Railway Station (NJP) by your private luxury transport chauffeur. Embark on a breathtakingly scenic drive winding alongside the turquoise Teesta River, bordered by emerald green hills. Upon arriving in Gangtok, check into your handpicked premium luxury resort. Enjoy a special welcome amenity kit. The evening is yours to relax or stroll hand-in-hand through the pedestrian-only MG Marg, enjoying the crisp mountain air and vibrant local vibe.'
                ),
                [
                    'Sightseeing Included: Scenic Teesta River valley drive, MG Marg evening promenade walk.',
                    'Evening Experience: Honeymoon Special: Custom welcome cake and a beautifully decorated romantic room',
                    'Overnight Stay: Gangtok (Premium Valley View Luxury Resort)',
                    'Meals Included: Welcome Drink & Luxury Buffet Dinner',
                ],
            ),
            _day(
                2,
                'EXCURSION TO TSOMGO LAKE & BABA MANDIR',
                (
                    "GLACIAL MAJESTY & ALPINE SNOW ROMANCE After a sumptuous breakfast, journey towards the high-altitude wonders of East Sikkim at 12,400 feet. Reach the sacred Tsomgo Lake (Changu Lake), a breathtaking glacial wonder that remains completely frozen during winters, offering a classic snow romance backdrop. Take a romantic yak ride along the snowline or capture stunning couples' portraits at this popular Instagram location. Continue the drive to the historic Baba Harbhajan Singh Mandir, learning about its fascinating local legends while surrounded by panoramic alpine valleys."
                ),
                [
                    'Sightseeing Included: Tsomgo Glacial Lake, Baba Harbhajan Singh Shrine, Kyongnosla Alpine Sanctuary view.',
                    'Optional Activities: Nathu La Pass excursion to the Indo-China border (subject to permit availability).',
                    'Overnight Stay: Gangtok (Premium Valley View Luxury Resort)',
                    'Meals Included: Premium Breakfast & Intimate Candle-lit Dinner arranged by TRAGUIN experts',
                ],
            ),
            _day(
                3,
                'GANGTOK TO LACHUNG',
                (
                    'JOURNEY TO THE UNTOUCHED NORTH – WATERFALLS & DEODAR VALLEYS Check out after breakfast and drive northwards to the serene alpine hamlet of Lachung at 8,800 feet. This scenic route passes through dramatic mountain terrains, showcasing cascading waterfalls such as the Seven Sisters Waterfalls and the majestic Naga Waterfall. Stop over at the historic Singhik Viewpoint to catch breathtaking landscapes of Mount Kanchenjunga. Arrive in Lachung by evening, checking into a cozy, premium handpicked hotel offering magnificent snow-capped mountain views.'
                ),
                [
                    'Sightseeing Included: Singhik Viewpoint, Seven Sisters Waterfalls, Naga Falls, Chungthang Confluence.',
                    'Evening Experience: Traditional warm Himalayan tea service in the resort courtyard under the starry sky.',
                    'Overnight Stay: Lachung (Premium Mountain Luxury Lodge)',
                    'Meals Included: Breakfast, En-route Lunch & Freshly Prepared Local Dinner',
                ],
            ),
            _day(
                4,
                'YUMTHANG VALLEY EXCURSION & RETURN TO GANGTOK',
                (
                    'THE VALLEY OF FLOWERS & UNREAL ALPINE MEADOWS Awake early to explore the magnificent Yumthang Valley, famously called the "Valley of Flowers". Situated at 11,800 feet, this valley presents an immersive experience with its sprawling hot springs, rolling yak pastures, and a dense cover of vibrant rhododendrons during spring. During winter, it transforms into an absolute snow paradise. For an ultimate thrill, drive further up to Zero Point (Yumesamdong), where the motorable road ends amidst pristine, perpetual snow sheets. Return to Lachung for lunch before driving back to Gangtok.'
                ),
                [
                    'Sightseeing Included: Yumthang Valley Meadow, Natural Hot Springs, Rhododendron Sanctuary.',
                    'Optional Activities: Excursion to Zero Point (Yumesamdong) for touchable snow fields at 15,000 feet.',
                    'Overnight Stay: Gangtok (Premium Valley View Luxury Resort)',
                    'Meals Included: Breakfast, Lachung Lunch & Premium Dinner in Gangtok',
                ],
            ),
            _day(
                5,
                'GANGTOK LOCAL MONASTERY & VIEWPOINTS TOUR',
                (
                    'SPIRITUAL CALM, ORCHIDS & RIDGE-TOP SPLENDOUR Spend a wonderful, relaxed day exploring the cultural richness and scenic beauty of Gangtok. Visit the world- renowned Rumtek Monastery, a seat of Tibetan Buddhist heritage. Explore the Do Drul Chorten Stupa, the Namgyal Institute of Tibetology, and the colorful Flower Exhibition Centre showcasing rare Himalayan orchids. Conclude your day with a breathtaking aerial view of the city via the Gangtok Ropeway ride. a boutique diner.'
                ),
                [
                    'Sightseeing Included: Rumtek Monastery, Directorate of Handicrafts, Flower Show, Tashi Viewpoint, Cable Car.',
                    'Evening Experience: Exclusive recommendations for cafe hopping and sampling authentic thukpa or momos at',
                    'Overnight Stay: Gangtok (Premium Valley View Luxury Resort)',
                    'Meals Included: Breakfast & Farewell Premium Dinner',
                ],
            ),
            _day(
                6,
                'GANGTOK TO BAGDOGRA / DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Indulge in a final lavish breakfast at your premium resort while taking in the morning mountain views. Your private luxury transport will safely drive you back along the smooth highway drop-off to Bagdogra Airport or NJP Railway Station for your onward journey. Return home carrying a heart full of sweet bonds and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private SUV airport/station drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Summit Golden',
                'Gangtok',
                '5N',
                'Deluxe',
                'Crescent / similar',
                'Summit Alpine Resort /',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Summit Golden | Crescent / similar | Summit Alpine Resort /',
            ),
            _hotel(
                'Lemon Tree Hotel / Muscatel',
                'Gangtok',
                '5N',
                'Premium',
                'Grand / similar',
                'Lachung Continental /',
                4,
                2,
                description='OPTION 02 – PREMIUM: Lemon Tree Hotel / Muscatel | Grand / similar | Lachung Continental /',
            ),
            _hotel(
                'Mayfair Spa Resort &',
                'Gangtok',
                '5N',
                'Luxury',
                'Casino / Elgin Nor-Khill',
                'Yarlam Resort / Modern',
                4,
                3,
                description='OPTION 03 – LUXURY: Mayfair Spa Resort & | Casino / Elgin Nor-Khill | Yarlam Resort / Modern',
            ),
            _hotel(
                'Mayfair Orchid Suite /',
                'Gangtok',
                '5N',
                'Ultra Luxury',
                'Vivanta Sikkim Pakyong',
                'Yarlam Executive Premium',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Mayfair Orchid Suite / | Vivanta Sikkim Pakyong | Yarlam Executive Premium',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 05 Nights in handpicked romantic luxury properties.', 1),
            _inc_included('Luxury Transportation: Private dedicated SUV (Innova/Luxury 4WD) for all hill travel.', 2),
            _inc_included('Curated Meal Plan: Daily premium breakfast & dinners; full meals in North Sikkim.', 3),
            _inc_included('TRAGUIN Support: 24/7 personalized concierge and inner-line permit coordination.', 4),
            _inc_included('Honeymoon Privileges: Candle-lit dining setup, floral bedding art, and custom cake.', 5),
            _inc_included('Exclusive Experiences: Private excursion to Yumthang Valley and high-altitude lakes.', 6),
            _inc_excluded('Airfare, flight tickets, or long-distance train travel to Bagdogra/NJP.', 7),
            _inc_excluded('Zero Point and Nathu La Pass additional transport supplement fees.', 8),
            _inc_excluded('Monument entry tickets, professional guide fees, camera permits.', 9),
            _inc_excluded('Personal expenses such as laundry, phone calls, or tips.', 10),
        ],
    )
    return package, itinerary

def build_sk_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SK-009'
    tour_code = 'TRG-SIK-009'
    title = 'GURUDONGMAR ADVENTURE • HIGH-ALTITUDE THRILLS & SACRED WATERS'
    duration = '06 Nights / 07 Days'
    slug = 'sk-009-gurudongmar-adventure-high-altitude-thrills-sacred-waters'
    itin_slug = 'sk-009-gurudongmar-adventure-high-altitude-thrills-sacred-waters-itinerary'
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
            _ph('Serial code SK-009 | TRAGUIN tour code TRG-SIK-009', 1),
            _ph('State / Country: Sikkim / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Gangtok • Lachen •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury 4x4 SUV / MAPAI & APAI (All Meals in North Sikkim)', 7),
            _ph('TRAGUIN Signature Experience: Private roadside picnic with warm treats and coffee during your high-', 8),
            _ph('Curated by TRAGUIN Experts: Smart pacing that incorporates gradual acclimatization stops to ensure', 9),
            _ph('Premium Handpicked Hotels: Properties chosen specifically for premium hospitality, ambient warming', 10),
            _ph('Luxury Transportation: Specially trained mountain drivers ensuring smooth mountain navigation.', 11)
        ],
        moods=['Luxury', 'Adventure'],
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
        tagline='GURUDONGMAR ADVENTURE',
        overview='SACRED WATERS Welcome to an extraordinary high-altitude expedition curated exclusively by TRAGUIN. Embark on the finest Sikkim Adventure Tour, meticulously crafted to guide you through the breathtaking landscapes, dramatic mountain passes, and sacred glacial waters of North Sikkim. As your elite travel consultants, TRAGUIN Premium Luxury Itinerary — SK-009 1 TRAGUIN transforms an ambitious mountain exploration into a high-end luxury holiday, complete with premium stays, specialized high-clearance 4x4 vehicles, and immersive experiences. Stand in awe before one of the highest lakes in the world, creating unforgettable memories under the guidance of seasoned alpine experts.\n\nTOUR OVERVIEW\nThis custom-tailored adventure itinerary balances heart-pounding alpine exploration with the absolute finest hospitality available in the remote Himalayan highlands. Traveling in a dedicated premium 4x4 SUV with an expert mountain chauffeur, you will conquer remote frontiers from the vibrant capital of Gangtok to the rugged outposts of Lachen and Lachung. Our comprehensive meal plan ensures you are fully energized with gourmet breakfasts and comforting regional dinners throughout your journey. Every step includes the signature touch of TRAGUIN curated experiences, including pre-arranged Inner Line Permits (ILP), specialized oxygen monitoring assistance, and bespoke premium touchpoints.\n\nWHY CHOOSE THE BEST SIKKIM TOUR PACKAGE?\nWhen planning a Luxury Sikkim Holiday, discerning thrill-seekers and nature enthusiasts demand an absolute balance of rugged exploration and flawless execution. Sikkim offers some of the most iconic attractions in the Eastern Himalayas. From the breathtaking landscapes of Yumthang Valley—often called the Valley of Flowers—to the legendary and sacred Gurudongmar Lake, this destination provides unparalleled spiritual and visual depth. For couples seeking a dramatic backdrop, our specialized Sikkim Honeymoon Package pairs perfectly with the serene beauty of mountain waterfalls and misty pine trails. Families and small groups choosing a Sikkim Family Tour will discover popular Instagram locations like the zero point snowfields, traditional wooden monasteries, and vibrant local markets. Choosing the best time to visit Sikkim allows you to enjoy maximum visibility, pristine photo opportunities, and authentic local culture. Our TRAGUIN Sikkim Packages guarantee premium handpicked hotels, seamless permit coordination, and exclusive experiences across all top tourist places in Sikkim.',
        seo_title='SK-009 | GURUDONGMAR ADVENTURE | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Sikkim package (SK-009 / TRG-SIK-009): Gangtok • Lachen • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GANGTOK', 1),
            _ih('Day 02: GANGTOK TO LACHEN', 2),
            _ih('Day 03: LACHEN TO GURUDONGMAR LAKE TO LACHUNG', 3),
            _ih('Day 04: LACHUNG TO YUMTHANG VALLEY & ZERO POINT EXCURSION', 4),
            _ih('Day 05: EXCURSION TO TSHONGMO LAKE & BABA MANDIR', 5),
            _ih('Day 06: MONASTERIES & LOCAL SIGHTSEEING IN GANGTOK', 6),
            _ih('Day 07: DEPARTURE FROM GANGTOK', 7),
            _ih('TRAGUIN Signature Experience: Private roadside picnic with warm treats and coffee during your high-', 8),
            _ih('Curated by TRAGUIN Experts: Smart pacing that incorporates gradual acclimatization stops to ensure', 9),
            _ih('Premium Handpicked Hotels: Properties chosen specifically for premium hospitality, ambient warming', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GANGTOK',
                (
                    'WELCOME TO THE GATEWAY OF SIKKIM – LUXURY AMBIANCE IN THE HILLS Your premium Sikkim sightseeing journey begins as you land at Pakyong or Bagdogra Airport. Your dedicated private luxury 4x4 SUV and professional tour representative will receive you with silk welcome scarves. Enjoy a scenic route winding past cascading rivers and lush terraced tea gardens to Gangtok. Check into your'
                ),
                [
                    'Sightseeing Included: Scenic Teesta River route, MG Marg walking promenade, Local Gangtok Viewpoint.',
                    'Evening Experience: Gourmet multi-cuisine dinner arranged at a top-tier restaurant curated by TRAGUIN',
                    'Overnight Stay: Gangtok (Premium / Luxury Resort)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'GANGTOK TO LACHEN',
                (
                    'JOURNEY TO THE WILD FRONTIER – RUSHING WATERFALLS & HIGH VALLEYS Depart early after a hearty breakfast towards the remote northern highlands of Lachen. This dramatic drive showcases the breathtaking landscapes of Sikkim, crossing deep gorges and roaring mountain torrents. Stop at the majestic Naga Waterfall and the stunning Bhim Nala Waterfall for iconic photography points. Pass through Chungthang confluence before ascending into the misty alpine village of Lachen, a peaceful valley surrounded by massive pine forests. Confluence.'
                ),
                [
                    'Sightseeing Included: Tshangu viewpoint (en route), Naga Waterfall, Bhim Nala Waterfall, Chungthang',
                    'Optional Activities: Brief evening acclimatization walk to a traditional local Lachenpa stone cottage.',
                    'Overnight Stay: Lachen (Handpicked Premium Alpine Hotel)',
                    'Meals Included: Premium Breakfast, Hot Lunch en-route, & Cozy Alpine Dinner',
                ],
            ),
            _day(
                3,
                'LACHEN TO GURUDONGMAR LAKE TO LACHUNG',
                (
                    'THE ULTIMATE HIGHLAND PINNACLE – GURUDONGMAR SACRED GLACIAL MAJESTY At the break of dawn, your premium 4x4 vehicle begins the ultimate high-altitude adventure toward Gurudongmar Lake, located at a staggering 17,800 feet. Drive across the cold, sun-drenched Tibetan Plateau landscape of Chopta Valley. Arrive at the holy lake, a mesmerizing expanse of pristine turquoise glacial water framed by massive snow-covered peaks. This emotionally moving landscape remains partly unfrozen even in deep winter. After capturing stunning photos, drive down to the peaceful mountain village of Lachung.'
                ),
                [
                    'Sightseeing Included: Gurudongmar Lake, Chopta Valley, Thangu Alpine Village, Sacred Cold Desert Plateau.',
                    'Evening Experience: Comforting, piping hot herbal teas and a premium local organic dinner to unwind.',
                    'Overnight Stay: Lachung (Handpicked Premium Mountain Resort)',
                    'Meals Included: Early morning hot beverages, Breakfast, Packed Lunch, & Dinner',
                ],
            ),
            _day(
                4,
                'LACHUNG TO YUMTHANG VALLEY & ZERO POINT EXCURSION',
                (
                    'THE ALPINE PARADISE – RHODODENDRONS & PERPETUAL SNOWS Drive today to the iconic Yumthang Valley, popularly known as the Valley of Flowers in Sikkim. Surrounded by towering snow peaks, this valley features breathtaking landscapes blanketed with vibrant rhododendrons and alpine flowers during spring. Continue your drive to Zero Point (Yumesamdong), where the civilian road ends and field snowscapes dominate. Enjoy high-altitude snow playing and take incredible pictures before returning to Gangtok in the evening.'
                ),
                [
                    'Sightseeing Included: Yumthang Valley, Yumthang Hot Springs, Zero Point (Yumesamdong).',
                    'Optional Activities: Taste authentic mountain noodle soup at the rustic wooden shacks at Zero Point.',
                    'Overnight Stay: Gangtok (Premium / Luxury Resort)',
                    'Meals Included: Premium Breakfast, Lunch, & Elite Buffet Dinner',
                ],
            ),
            _day(
                5,
                'EXCURSION TO TSHONGMO LAKE & BABA MANDIR',
                (
                    "SACRED HIGH-ALTITUDE WATERS & LEGENDARY FRONTIER OUTPOSTS Today, take an iconic day-trip to the sacred, oval-shaped Tshongmo Lake (Changu Lake). This deep glacial lake is highly revered by locals and reflects changing color tones with the seasons. Continue your drive higher up to visit the legendary Baba Harbhajan Singh Mandir, a unique shrine deeply respected by frontier soldiers. Take a fun yak ride along the lake's edge and enjoy the stunning view. Sanctuary view."
                ),
                [
                    'Sightseeing Included: Tshongmo Glacial Lake, Baba Harbhajan Singh Memorial Shrine, Kyongnosla Alpine',
                    'Optional Activities: Nathu La Pass border post visit (subject to permit availability on extra charge).',
                    'Overnight Stay: Gangtok (Premium / Luxury Resort)',
                    'Meals Included: Premium Breakfast & Farewell Dinner',
                ],
            ),
            _day(
                6,
                'MONASTERIES & LOCAL SIGHTSEEING IN GANGTOK',
                (
                    'CULTURE, HERITAGE & SPIRITUAL REJUVENATION Spend a beautiful, relaxed day exploring the deep spiritual heritage and rich arts of Gangtok. Visit the world- famous Rumtek Monastery, a global seat of Tibetan Buddhism. Explore the Namgyal Institute of Tibetology to view rare collections of ancient thangka paintings and sacred artifacts. Wrap up your afternoon at the Enchey Monastery and catch a panoramic sunset view over the Kanchenjunga range from Tashi Viewpoint.'
                ),
                [
                    'Sightseeing Included: Rumtek Monastery, Do Drul Chorten, Institute of Tibetology, Tashi Viewpoint, Ganesh Tok.',
                    'Evening Experience: Private dinner with live acoustic mountain music arranged exclusively for your group.',
                    'Overnight Stay: Gangtok (Premium / Luxury Resort)',
                    'Meals Included: Premium Breakfast & Luxury Dinner',
                ],
            ),
            _day(
                7,
                'DEPARTURE FROM GANGTOK',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Indulge in a final morning breakfast overlooking the mist-filled valley. Your private luxury SUV will safely drive you back along the scenic national highway to Pakyong or Bagdogra Airport for your onward flight. Return home carrying a heart filled with high-altitude triumphs and unforgettable memories designed meticulously by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury airport drop-off assistance.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Summit Golden',
                'Gangtok',
                '6N',
                'Deluxe',
                'Crescent / similar',
                'Hotel Summit Orchard',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Summit Golden | Crescent / similar | Hotel Summit Orchard',
            ),
            _hotel(
                'Lemon Tree Premier / The',
                'Gangtok',
                '6N',
                'Premium',
                'Royal Plaza',
                'Lachen View Heritage /',
                4,
                2,
                description='OPTION 02 – PREMIUM: Lemon Tree Premier / The | Royal Plaza | Lachen View Heritage /',
            ),
            _hotel(
                'Mayfair Spa Resort & Casino',
                'Gangtok',
                '6N',
                'Luxury',
                '/ Elgin Nor-Khill',
                'The Apple Orchard Resort',
                4,
                3,
                description='OPTION 03 – LUXURY: Mayfair Spa Resort & Casino | / Elgin Nor-Khill | The Apple Orchard Resort',
            ),
            _hotel(
                'Mayfair Resort (Executive',
                'Gangtok',
                '6N',
                'Ultra Luxury',
                'Pool Villa)',
                'VVIP Custom Luxury',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Mayfair Resort (Executive | Pool Villa) | VVIP Custom Luxury',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Handpicked accommodations as per chosen tier.', 1),
            _inc_included('Luxury Transportation: Private 4x4 SUV (Innova/Scorpio/XUV) for rough terrains.', 2),
            _inc_included('Curated Meal Plan: Daily breakfast & dinner in Gangtok; all meals in North Sikkim.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated local operations manager and guide assistance.', 4),
            _inc_included('Permit Coordination: Inner Line Permits (ILP) documentation for protected areas.', 5),
            _inc_included('Complimentary Experience: Private sunset tea service at Yumthang Valley.', 6),
            _inc_excluded('Airfare, domestic flights, or main train tickets.', 7),
            _inc_excluded('Nathu La Pass permits and ticketing costs.', 8),
            _inc_excluded('Personal items, laundry, phone bills, tipping.', 9),
            _inc_excluded('Any medical expenses or emergency high-altitude evacuation.', 10),
        ],
    )
    return package, itinerary

def build_sk_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SK-010'
    tour_code = 'TRG-SIK-010'
    title = 'LADIES SIKKIM ESCAPE • EMPOWERMENT, LUXURY & ALPINE MAJESTY'
    duration = '05 Nights / 06 Days'
    slug = 'sk-010-ladies-sikkim-escape-empowerment-luxury-alpine-majesty'
    itin_slug = 'sk-010-ladies-sikkim-escape-empowerment-luxury-alpine-majesty-itinerary'
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
            _ph('Serial code SK-010 | TRAGUIN tour code TRG-SIK-010', 1),
            _ph('State / Country: Sikkim / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Gangtok •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Luxury Innova Crysta / MAPAI (Premium Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private momo-making workshop and traditional dress-up group photo', 8),
            _ph('Curated by TRAGUIN Experts: Carefully planned itineraries focused on maximum safety, comfort, and', 9),
            _ph('Premium Handpicked Hotels: Accommodations selected for security, hospitality, and spectacular views.', 10),
            _ph('Exclusive Recommendations: Access to the best local artisan markets and boutique cafes.', 11)
        ],
        moods=['Luxury', 'Nature'],
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
        tagline='LADIES SIKKIM ESCAPE',
        overview="MAJESTY Welcome to an empowering alpine experience thoughtfully curated by TRAGUIN. Designed exclusively for women, our Ladies Sikkim Escape balances security, sisterhood, and high-end luxury in the majestic TRAGUIN Premium Luxury Itinerary — SK-010 1 Eastern Himalayas. This unique Sikkim Family Tour alternative or exclusive girlfriends' sanctuary celebrates breathtaking landscapes, mystical monasteries, and premium stays. As your luxury travel advisors, TRAGUIN transforms this Himalayan wonderland into an unforgettable chapter of laughter, wellness, and immersive experiences, creating beautiful memories to last a lifetime.\n\nTOUR OVERVIEW\nThis elite, premium luxury travel itinerary is custom-crafted for discerning female travelers who expect absolute comfort, safety, and sophistication. Travelling in a dedicated, private luxury transport vehicle with an experienced local guide, your group will seamlessly glide through the mist-shrouded valleys of Sikkim. Our meticulous plan balances therapeutic leisure with scenic discovery, featuring handpicked hotels known for their hospitality and beautiful views. From an premium greeting cocktail to artisanal dining, your journey is safe with the signature TRAGUIN curated experience note, guaranteeing high-end hospitality at every altitude.\n\nWHY CHOOSE THE BEST SIKKIM TOUR PACKAGE?\nWhen exploring options for a Luxury Sikkim Holiday, travelers look for spectacular alpine views, rich cultural encounters, and luxurious wellness sanctuaries. Sikkim is a timeless mountain retreat, making a Sikkim Honeymoon Package or an exclusive all-female expedition the perfect choice for an inspiring escape. From the bustling, flower-lined walkways of Gangtok's MG Marg to iconic attractions like the sacred Tsomgo Lake, Sikkim sightseeing provides an unmatched sense of wonder. This tailored Sikkim Family Tour alternative takes you to popular Instagram locations like the towering Buddha Park in Ravangla and the pristine multi-tiered waterfalls hidden in the hills. Indulge in premium handicraft shopping at local directorates, enjoy specialized organic teas at charming cafes, or soak in the serene monastic ambiance of Rumtek. Our signature TRAGUIN Sikkim Packages seamlessly blend exclusive experiences with exceptional stays, giving you the absolute best time to visit Sikkim with complete peace of mind.",
        seo_title='SK-010 | LADIES SIKKIM ESCAPE | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Sikkim package (SK-010 / TRG-SIK-010): Gangtok • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GANGTOK', 1),
            _ih('Day 02: SACRED TSOMGO LAKE & BABA MANDIR EXCURSION', 2),
            _ih('Day 03: GANGTOK URBAN REVELATIONS', 3),
            _ih('Day 04: GANGTOK TO NAMCHI & RAVANGLA', 4),
            _ih('Day 05: TEA GARDENS & WELLNESS SANCTUARY', 5),
            _ih('Day 06: DEPARTURE VIA TEESTA VALLEY', 6),
            _ih('TRAGUIN Signature Experience: Private momo-making workshop and traditional dress-up group photo', 7),
            _ih('Curated by TRAGUIN Experts: Carefully planned itineraries focused on maximum safety, comfort, and', 8),
            _ih('Premium Handpicked Hotels: Accommodations selected for security, hospitality, and spectacular views.', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GANGTOK',
                (
                    'WELCOME TO THE CLOUD CAPITAL – ALPINE LUXURY & HIGH SISTERHOOD Your premium Sikkim experience begins as your private chauffeur welcomes you at Bagdogra Airport (IXB) or New Jalpaiguri Station (NJP). Enjoy a scenic drive tracing the beautiful emerald-green Teesta River up into the hills. Arrive in Gangtok and check into your handpicked premium hotel. Unwind with a signature organic herbal tea welcome ceremony before stepping out for a relaxed orientation walk along MG Marg, an exceptionally safe, clean, and pedestrian-friendly high street.'
                ),
                [
                    'Sightseeing Included: Teesta River viewpoint trail, MG Marg evening promenade walk.',
                    'Evening Experience: Ladies Welcome Evening: Curated local wine tasting and orientation dinner.',
                    'Overnight Stay: Gangtok (Premium / Luxury Boutique Resort)',
                    'Meals Included: Welcome Drink & Gourmet Dinner',
                ],
            ),
            _day(
                2,
                'SACRED TSOMGO LAKE & BABA MANDIR EXCURSION',
                (
                    'GLACIAL SPLENDOUR & SECURE ALPINE MAJESTY Indulge in a premium breakfast before your private luxury transport ascends to 12,400 feet to visit the sacred Tsomgo Lake. This glacial wonder offers breathtaking landscapes reflecting the surrounding peaks, making it a top tourist place in Sikkim. Enjoy an optional yak ride decorated in vibrant traditional colors—a highly popular Instagram location. Continue to the historic Baba Harbhajan Singh Mandir to hear fascinating local legends. view.'
                ),
                [
                    'Sightseeing Included: Tsomgo Glacial Lake, Baba Harbhajan Singh Memorial, Kyongnosla Alpine Sanctuary',
                    'Optional Activities: Private cable car ride over Tsomgo Lake for stunning panoramic photos.',
                    'Overnight Stay: Gangtok (Premium / Luxury Boutique Resort)',
                    'Meals Included: Premium Breakfast & Authentic Dinner',
                ],
            ),
            _day(
                3,
                'GANGTOK URBAN REVELATIONS',
                (
                    'MONASTIC CALM, HANDICRAFTS & ORGANIC GASTRONOMY Spend a beautiful day exploring the rich heritage and culture of Gangtok. Start at the magnificent Rumtek Monastery, a world-renowned center of Tibetan Buddhism. Visit the Namgyal Institute of Tibetology and the Directorate of Handicrafts to see local female artisans practicing traditional weaving and thangka painting. Spend a relaxed late afternoon at an upscale café sampling artisan coffees and local organic delicacies.'
                ),
                [
                    'Sightseeing Included: Rumtek Monastery, Do Drul Chorten, Institute of Tibetology, Flower Exhibition Centre.',
                    'Evening Experience: Interactive Himalayan momo-making masterclass led by an expert local female chef.',
                    'Overnight Stay: Gangtok (Premium / Luxury Boutique Resort)',
                    'Meals Included: Premium Breakfast & Fine Dining Dinner',
                ],
            ),
            _day(
                4,
                'GANGTOK TO NAMCHI & RAVANGLA',
                (
                    'HERITAGE PILGRIMAGE & DRAMATIC VALLEY VIEWS Bid farewell to Gangtok as your premium tour heads to South Sikkim. Drive through lush pine valleys to Ravangla and discover the breathtaking Buddha Park, which features a magnificent 130-foot-tall gilded Buddha statue set against Mt. Narsing. Next, visit Namchi to explore the impressive Siddheshwar Dham (Chardham) replica architecture. Check into your luxury resort nestled within a beautiful tea estate or misty valley.'
                ),
                [
                    'Sightseeing Included: Buddha Park Ravangla, Siddheshwar Dham Namchi, Samdruptse Statue.',
                    'Evening Experience: Private bonfire social under the stars with premium appetizers and music.',
                    'Overnight Stay: Namchi / Ravangla Premium Luxury Resort',
                    'Meals Included: Premium Breakfast & Farm-to-Table Dinner',
                ],
            ),
            _day(
                5,
                'TEA GARDENS & WELLNESS SANCTUARY',
                (
                    'TEA PLUCKING EXPERIENCE & MEDITATIVE WELLNESS Awake to a peaceful mountain sunrise over the Kanchenjunga range. Spend your morning at the beautiful Temi Tea Garden, the only tea estate in Sikkim. Participate in a private tea-plucking experience wearing traditional attire—a fantastic photography point. Spend the afternoon enjoying a custom spa session or a guided mountain meditation circle designed to leave you feeling completely refreshed.'
                ),
                [
                    'Sightseeing Included: Temi Tea Estate walks, Tea Processing Unit insider tour.',
                    'Optional Activities: Premium multi-variety tea tasting and buying session.',
                    'Overnight Stay: Namchi / Ravangla Premium Luxury Resort',
                    'Meals Included: Premium Breakfast & Farewell Gala Dinner',
                ],
            ),
            _day(
                6,
                'DEPARTURE VIA TEESTA VALLEY',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS Savor a final breakfast while taking in the beautiful mountain views. Your private luxury transport will guide you safely down the hills back to Bagdogra Airport or NJP Station for your onward flight. Return home feeling inspired, carrying special connections and unforgettable memories designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury airport drop-off assistance.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Summit Golden Crescent',
                'Sikkim',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Summit Golden Crescent',
            ),
            _hotel(
                'The Elgin Nor-Khill / Lemon Tree Hotel Ravangla Star',
                'Sikkim',
                '5N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Elgin Nor-Khill / Lemon Tree Hotel Ravangla Star',
            ),
            _hotel(
                'Mayfair Spa Resort & Casino Gangtok The Temi Bungalow (Eco-Luxury) VIP Lounge + Spa Discounts',
                'Sikkim',
                '5N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Mayfair Spa Resort & Casino Gangtok The Temi Bungalow (Eco-Luxury) VIP Lounge + Spa Discounts',
            ),
            _hotel(
                'Mayfair Grand Executive Suite Exclusive Tea Estate Private Villa Bespoke Signature Concierge',
                'Sikkim',
                '5N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Mayfair Grand Executive Suite Exclusive Tea Estate Private Villa Bespoke Signature Concierge',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 05 Nights in properties selected for safety and views.', 1),
            _inc_included('Luxury Transportation: Private Innova Crysta with verified local drivers.', 2),
            _inc_included('Curated Meal Plan: Daily premium breakfast and gourmet dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated female guest assistance manager.', 4),
            _inc_included('Welcome Amenities: Himalayan herbal tea kit and personalized travel amenities.', 5),
            _inc_included('Complimentary Experience: Culinary masterclass and tea estate tour fees.', 6),
            _inc_excluded('Airfare, domestic flight tickets, or train travel costs.', 7),
            _inc_excluded('Personal laundry, tipping, alcoholic beverages, and extra phone orders.', 8),
            _inc_excluded('Nathula Pass permit extensions (can be requested additionally).', 9),
            _inc_excluded('Any insurance fees or unexpected emergency cost overruns.', 10),
        ],
    )
    return package, itinerary

def build_sk_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SK-011'
    tour_code = 'TRG-SK-011'
    title = 'LEISURE SIKKIM • SERENE HORIZONS & MYSTICAL HIMALAYAN VALLEYS'
    duration = '05 Nights / 06 Days'
    slug = 'sk-011-leisure-sikkim-serene-horizons-mystical-himalayan-valleys'
    itin_slug = 'sk-011-leisure-sikkim-serene-horizons-mystical-himalayan-valleys-itinerary'
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
            _ph('Serial code SK-011 | TRAGUIN tour code TRG-SK-011', 1),
            _ph('State / Country: Sikkim / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Gangtok • Sikkim', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Innova / Premium MAPAI Plan', 7),
            _ph('TRAGUIN Signature Experience: Private, slow-paced sightseeing with reserved premium seating at all', 8),
            _ph('Curated by TRAGUIN Experts: Specialized routing that eliminates long, bumpy paths for a smoother', 9),
            _ph('Personalized Assistance: A dedicated tour coordinator at the hotel to assist with any physical or medical', 10),
            _ph('Premium Handpicked Hotels: Accommodations chosen specifically for flat pathways, premium', 11)
        ],
        moods=['Luxury', 'Nature', 'Leisure'],
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
        tagline='LEISURE SIKKIM',
        overview="HIMALAYAN VALLEYS Welcome to an beautifully relaxed exploration of the Northeast, mindfully crafted by TRAGUIN. Discover our signature Sikkim Senior Citizen Holiday, deliberately designed to balance the region's breathtaking TRAGUIN Premium Luxury Travel Proposal — SK-011 1 landscapes with a perfectly slow, stress-free, and leisurely pace. As your premium travel consultants, TRAGUIN transforms this alpine escape into a deeply reassuring luxury holiday, emphasizing premium stays, handpicked hotels with direct elevator access, smooth transfers, and deeply moving local narratives. Let the spiritual ambiance, majestic snow-covered peaks, and stunning scenic beauty bring peace to your soul, creating unforgettable memories for you and your loved ones.\n\nTOUR OVERVIEW\nTravel Route: Bagdogra (IXB) / Pakyong Airport • Gangtok (3 Nights) • Namchi & Ravangla Excursion • Gangtok (1 Night) • Departure. This custom-tailored, slow-paced Luxury Sikkim Holiday is curated exclusively for senior travelers who prefer premium comfort over rushed schedules. Your private group or FIT experience includes a dedicated luxury vehicle driven by a highly professional, polite mountain chauffeur. Our specialized meal plan features fresh, mild, and highly customized health-conscious culinary options. To elevate your peace of mind, every detail includes a unique TRAGUIN curated experience note, guaranteeing priority medical coordination, zero- staircase entry paths, and seamless wheelchair assistance where required.\n\nWHY CHOOSE THE BEST SIKKIM TOUR PACKAGE?\nWhen exploring options for a Luxury Sikkim Holiday, discerning family members look for specialized itineraries that respect physical stamina while fully introducing the region's iconic attractions. Sikkim represents a majestic kingdom of clouds and spiritual Monasteries, positioning a customized Sikkim Family Tour or a romantic Sikkim Honeymoon Package among India's most highly sought-after mountain vacations. From the misty heights of Gangtok sightseeing to the spiritual complex of Chardham in Namchi, the state offers immense peace and comfort. For elderly travelers, our itineraries target low-altitude, smooth alpine spots and popular Instagram locations such as the serene Buddha Park in Ravangla and the pristine banks of Tsomgo Lake. Experience the calm rhythms of local Buddhist chants, explore delightful orchid gardens, and participate in local handicraft shopping at the vehicle-free MG Marg. With our specialized TRAGUIN Sikkim Packages, we seamlessly merge exclusive experiences with top tourist places in Sikkim, identifying the best time to visit Sikkim for perfect weather, zero crowds, and a premium Sikkim experience. TRAGUIN Premium Luxury Travel Proposal — SK-011 2 DAY WISE ITINERARY",
        seo_title='SK-011 | LEISURE SIKKIM | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Sikkim package (SK-011 / TRG-SK-011): Gangtok • Sikkim with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GANGTOK', 1),
            _ih('Day 02: REFRESHING GANGTOK SIGHTSEEING', 2),
            _ih('Day 03: EXCURSION TO TSOMGO ALPINE LAKE', 3),
            _ih('Day 04: GANGTOK TO NAMCHI & RAVANGLA EXCURSION', 4),
            _ih('Day 05: DAY OF RELAXATION & LOCAL CULTURAL IMMERSION', 5),
            _ih('Day 06: GANGTOK TO DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private, slow-paced sightseeing with reserved premium seating at all', 7),
            _ih('Curated by TRAGUIN Experts: Specialized routing that eliminates long, bumpy paths for a smoother', 8),
            _ih('Personalized Assistance: A dedicated tour coordinator at the hotel to assist with any physical or medical', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GANGTOK',
                (
                    'GATEWAY TO THE CLOUD KINGDOM – SMOOTH ARRIVAL & LEISURELY INDUCTION Your premium Sikkim experience starts the moment you land. Your dedicated luxury transportation vehicle and private assistant greet you warmly at the terminal, handling all luggage with absolute care. Relax in air- conditioned comfort as you begin a beautiful, scenic journey alongside the emerald-green Teesta River. Arrive in Gangtok, the capital city, and check into one of our handpicked hotels. Savor a fresh welcome beverage as our team completes check-in formalities on your behalf. Spend the evening resting or enjoy a light, flat walk along the manicured, cobblestone walking trails of MG Marg.'
                ),
                [
                    'Sightseeing Included: Teesta River viewpoints, evening leisure exploration at Gangtok Mall Road (MG Marg).',
                    'Evening Experience: Relaxed stroll on flat surfaces followed by a mild, freshly prepared gourmet dinner.',
                    'Overnight Stay: Gangtok (Premium Luxury Property with central heating and elevator access)',
                    'Meals Included: Welcome Drink & Specialized Light Dinner',
                ],
            ),
            _day(
                2,
                'REFRESHING GANGTOK SIGHTSEEING',
                (
                    'SPIRITUAL MONASTERIES & MANICURED ALPINE GARDENS Wake up to the breathtaking sight of mist lifting off the green valleys. After a relaxed, tailor-made breakfast, enjoy a peaceful Gangtok sightseeing tour. Visit the serene Enchey Monastery, where your private guide shares stories of ancient Buddhist heritage without requiring long walks. Explore the Flower Exhibition Centre, showcasing a vibrant collection of rare Himalayan orchids. Conclude your afternoon at the Do Drul Chorten Stupa, spinning the holy prayer wheels for peace, health, and family longevity. Tibetology. TRAGUIN Premium Luxury Travel Proposal — SK-011 3'
                ),
                [
                    'Sightseeing Included: Enchey Monastery, Flower Exhibition Centre, Do Drul Chorten, Namgyal Institute of',
                    'Optional Activities: A smooth, accessible cable car ride offering panoramic mountain views over Gangtok.',
                    'Overnight Stay: Gangtok (Premium Luxury Property)',
                    'Meals Included: Premium Breakfast & Fine Dining Dinner',
                ],
            ),
            _day(
                3,
                'EXCURSION TO TSOMGO ALPINE LAKE',
                (
                    'SACRED WATERS & MAJESTIC SNOW-CLAD PANORAMAS Indulge in an early breakfast before heading out on a scenic excursion to the sacred Tsomgo Lake, situated at 12,400 feet. Your premium vehicle is equipped with supplemental oxygen cylinders for your complete comfort. Marvel at the breathtaking landscapes as the lake reflects the surrounding snow-capped peaks. A smooth, accessible lakeside pavilion allows you to enjoy the cool crisp mountain breeze comfortably without strenuous walking. borders. resort.'
                ),
                [
                    'Sightseeing Included: Tsomgo Sacred Lake, Lakeside viewing terrace, Kyongnosla Alpine Sanctuary',
                    'Evening Experience: A warm, freshly brewed organic herbal tea tasting session upon returning to your',
                    'Overnight Stay: Gangtok (Premium Luxury Property)',
                    'Meals Included: Premium Breakfast & Wholesome Warm Dinner',
                ],
            ),
            _day(
                4,
                'GANGTOK TO NAMCHI & RAVANGLA EXCURSION',
                (
                    'THE SPIRITUAL HEARTLAND – MAJESTIC BUDDHA PARK & CHARDHAM Today, take a peaceful drive through beautiful tea gardens to South Sikkim. Your destination is the famous Buddha Park in Ravangla, home to a magnificent 130-foot-tall Buddha statue framed by the Himalayas. The park is senior-friendly, offering paved, flat walking trails and golf-cart assistance. Continue on to the Siddheswar Dham (Chardham) in Namchi, a breathtaking cultural complex designed for comfortable, accessible heritage walks.'
                ),
                [
                    'Sightseeing Included: Buddha Park (Tathagata Tsal), Namchi Chardham Complex, Temi Tea Garden vistas.',
                    'Optional Activities: A gentle, guided stroll through the beautiful, rolling hills of Temi Tea Estate.',
                    'Overnight Stay: Gangtok (Premium Luxury Property)',
                    'Meals Included: Premium Breakfast & Authentic Organic Thali Dinner',
                ],
            ),
            _day(
                5,
                'DAY OF RELAXATION & LOCAL CULTURAL IMMERSION',
                (
                    'LEISURE IN GANGTOK – SOUVENIR SHOPPING & EXPERIENTIAL TEA CAFE Enjoy a wonderfully relaxed day with no early morning wake-up alarms. Following a late gourmet breakfast, take a leisurely drive to the Directorate of Handicrafts and Handlooms to view local artisans creating exquisite TRAGUIN Premium Luxury Travel Proposal — SK-011 4 Sikkimese rugs and wood carvings. The afternoon is reserved for a special high-tea experience at an exclusive cafe overlooking the valley, allowing you to reflect on your journey in comfort.'
                ),
                [
                    'Sightseeing Included: Cottage Industry Center, local Tibetan artisan markets, panoramic valley viewpoints.',
                    'Evening Experience: A special farewell dinner arranged in a private dining hall with traditional soft music.',
                    'Overnight Stay: Gangtok (Premium Luxury Property)',
                    'Meals Included: Premium Breakfast & Farewell Celebration Dinner',
                ],
            ),
            _day(
                6,
                'GANGTOK TO DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS – COMFORTABLE HOMEWARD JOURNEY Enjoy a final breakfast at your hotel before embarking on a comfortable return drive to Bagdogra Airport or New Jalpaiguri Station. Your private luxury transport ensures a smooth ride down the mountains. Depart with a completely refreshed spirit and beautiful, lifelong memories designed with care by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury highway drop-off with comfortable rest stops en route.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Summit Golden',
                'Gangtok',
                '5N',
                'Deluxe',
                'Crescent / similar',
                'Deluxe Room',
                4,
                1,
                description='OPTION 01 – DELUXE: The Summit Golden | Crescent / similar | Deluxe Room',
            ),
            _hotel(
                'Lemon Tree Hotel',
                'Gangtok',
                '5N',
                'Premium',
                'Gangtok / similar',
                'Executive Balcony',
                4,
                2,
                description='OPTION 02 – PREMIUM: Lemon Tree Hotel | Gangtok / similar | Executive Balcony',
            ),
            _hotel(
                'Mayfair Spa Resort &',
                'Gangtok',
                '5N',
                'Luxury',
                'Casino Gangtok',
                'Luxury Cottage',
                4,
                3,
                description='OPTION 03 – LUXURY: Mayfair Spa Resort & | Casino Gangtok | Luxury Cottage',
            ),
            _hotel(
                'The Elgin Nor-Khill',
                'Gangtok',
                '5N',
                'Ultra Luxury',
                'Heritage Resort',
                'VVIP Royal',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Elgin Nor-Khill | Heritage Resort | VVIP Royal',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Handpicked senior-friendly hotels with smooth elevator systems.', 1),
            _inc_included('Luxury Transportation: Private luxury Innova Crysta for all transfers and sightseeing.', 2),
            _inc_included('Curated Meal Plan: Daily mild breakfasts and customizable dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated medical concierge on-call.', 4),
            _inc_included('Welcome Amenities: Personalized herbal travel kit, oxygen canisters, and healthy snacks.', 5),
            _inc_included('Complimentary Experience: Private family tea-tasting experience at Temi Estate.', 6),
            _inc_excluded('Flights or long-distance train tickets to Bagdogra / NJP.', 7),
            _inc_excluded('Monument entry fees, camera permits, and local guide charges.', 8),
            _inc_excluded('Personal expenses such as laundry, phone calls, tips, and insurance.', 9),
            _inc_excluded('Nathu La Pass excursions (available upon request at extra cost).', 10),
        ],
    )
    return package, itinerary

def build_sk_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SK-012'
    tour_code = 'TRG-SIK-012'
    title = 'PREMIUM SIKKIM • MYSTICAL HEIGHTS & ALPINE GRANDEUR'
    duration = '06 Nights / 07 Days'
    slug = 'sk-012-premium-sikkim-mystical-heights-alpine-grandeur'
    itin_slug = 'sk-012-premium-sikkim-mystical-heights-alpine-grandeur-itinerary'
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
            _ph('Serial code SK-012 | TRAGUIN tour code TRG-SIK-012', 1),
            _ph('State / Country: Sikkim / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Gangtok •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury SUV (Innova/Crysta) / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private curated riverside picnic stops with hot regional finger snacks', 8),
            _ph('Curated by TRAGUIN Experts: Seamless processing of restricted area defense permits handled by', 9),
            _ph('Premium Handpicked Hotels: Accommodations chosen strictly based on pristine scenery, safety, luxury', 10),
            _ph('Luxury Transportation: Uniformed mountain-expert drivers ensuring maximum vehicle safety and', 11)
        ],
        moods=['Luxury', 'Nature'],
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
        tagline='PREMIUM SIKKIM',
        overview='Welcome to an extraordinary high-altitude sanctuary curated exclusively by TRAGUIN. Embark on the finest Premium Sikkim Experience designed to reveal the breathtaking landscapes, ancient monasteries, and majestic snow-capped peaks of the Eastern Himalayas. As your elite travel consultants, TRAGUIN TRAGUIN Premium Luxury Itinerary — SK-012 1 transforms your mountain getaway into a seamless luxury holiday filled with premium stays, intimate cultural milestones, and flawless execution. From the vibrant ridges of Gangtok to the dramatic rhododendron meadows of Yumthang Valley, every detail is meticulously tailored to produce sweet, unforgettable memories for you and your loved ones.\n\nTOUR OVERVIEW\nThis custom-crafted luxury itinerary presents a perfect harmony of alpine adventure, untouched ecological beauty, sacred spiritual architecture, and refined hospitality. Traveling in a dedicated private premium luxury vehicle perfectly suited for mountain terrains, you will navigate the scenic beauty of the Teesta River valley in ultimate comfort. Featuring a rich, handpicked meal plan with gourmet breakfasts and tailored regional dinners, this route represents the gold standard of travel. Every milestone is heightened by the signature TRAGUIN curated experience note, providing VIP permit clearances, local expert insight, and unmatched personal attention.\n\nWHY CHOOSE THE BEST SIKKIM TOUR PACKAGE?\nWhen planning a Luxury Sikkim Holiday, discerning globetrotters seek far more than standard itineraries; they seek deep immersive experiences and complete peace of mind. Sikkim hosts some of the most iconic attractions in the Indian subcontinent. From the sacred glacial heights of Tsomgo Lake—a top tourist place in Sikkim—to the mist-covered therapeutic hot springs of North Sikkim, the destination stands unmatched. For couples seeking a dream Sikkim Honeymoon Package or families booking a comprehensive Sikkim Family Tour, the region offers incredibly famous Instagram locations like the Lachung monastery paths, Mahatma Gandhi Marg promenade, and the pristine, flower-filled carpets of Yumthang Valley. Whether you choose to indulge in authentic local Tibetan culinary specialties, seek blessings at spiritual monasteries, or go shopping for traditional hand-woven prayer rugs, our signature TRAGUIN Sikkim Packages guarantee opulent comfort, handpicked hotels, and curated exclusive experiences during the absolute best time to visit Sikkim.',
        seo_title='SK-012 | PREMIUM SIKKIM | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Sikkim package (SK-012 / TRG-SIK-012): Gangtok • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GANGTOK', 1),
            _ih('Day 02: EXCURSION TO TSOMGO LAKE & BABA MANDIR', 2),
            _ih('Day 03: GANGTOK TO LACHUNG', 3),
            _ih('Day 04: LACHUNG TO YUMTHANG VALLEY TO GANGTOK', 4),
            _ih('Day 05: GANGTOK URBAN & CULTURAL SIGHTSEEING', 5),
            _ih('Day 06: GANGTOK TO DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private curated riverside picnic stops with hot regional finger snacks', 7),
            _ih('Curated by TRAGUIN Experts: Seamless processing of restricted area defense permits handled by', 8),
            _ih('Premium Handpicked Hotels: Accommodations chosen strictly based on pristine scenery, safety, luxury', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GANGTOK',
                (
                    'WELCOME TO THE HIMALAYAN REALM – PRIVATE RIVERSIDE ASCENT Your premium Sikkim itinerary begins as you touch down at Bagdogra Airport or Pakyong Airport, where a dedicated private luxury transport vehicle stands ready to receive you. Wind through mountain passes running alongside the emerald-green Teesta River, a legendary scenic route. Arrive at the capital city of Gangtok, and step into your handpicked luxury resort. Spend your evening taking a relaxed stroll through the spotless, pedestrian-only MG Marg, discovering local cafes and elite handicraft shopping stalls.'
                ),
                [
                    'Sightseeing Included: Teesta River scenic drive, MG Marg promenade stroll.',
                    'Evening Experience: Traditional welcome tea service and premium dinner curated by TRAGUIN experts.',
                    'Overnight Stay: Gangtok (Premium / Luxury Mountain Resort)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'EXCURSION TO TSOMGO LAKE & BABA MANDIR',
                (
                    'SACRED GLACIAL MAJESTY & HIGH-ALTITUDE WONDERS Awake early for a spectacular drive to Tsomgo Lake, situated at an alpine altitude of 12,400 feet. This deeply revered glacial lake reflects the changing colors of the sky, presenting a truly breathtaking landscape. Capture stunning photography points around the snow-covered lake banks. Continue your high-altitude drive to the legendary Baba Harbhajan Singh Mandir, filled with incredible local folklore. Return to Gangtok for a peaceful evening of luxury spa therapies.'
                ),
                [
                    'Sightseeing Included: Tsomgo Glacial Lake, Baba Harbhajan Singh Memorial Shrine.',
                    'Optional Activities: Permit extension to Nathula Pass on the Indo-China border (subject to availability).',
                    'Overnight Stay: Gangtok (Premium / Luxury Mountain Resort)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'GANGTOK TO LACHUNG',
                (
                    'JOURNEY TO NORTH SIKKIM – WATERFALLS & ALPINE VALLEYS Following a delicious breakfast, check out and drive north toward the ethereal alpine village of Lachung. This scenic route is arguably one of the most magnificent drives in Asia, punctuated by gushing waterfalls, deep gorges, and dense pine forests. Stop to view the dramatic Seven Sisters Waterfalls and the breathtaking Singhik viewpoint, which offers views of Mount Khangchendzonga on a clear day. Arrive at your handpicked boutique lodge in Lachung, surrounded by snow-draped cliffs.'
                ),
                [
                    'Sightseeing Included: Seven Sisters Waterfalls, Naga Waterfalls, Singhik Viewpoint, Chungthang Confluence.',
                    'Evening Experience: Cozy fireplace gathering with traditional Himalayan herbal teas.',
                    'Overnight Stay: Lachung (Premium Handpicked Luxury Alpine Cottage)',
                    'Meals Included: Breakfast, Hot Lunch en-route & Authentic Local Dinner',
                ],
            ),
            _day(
                4,
                'LACHUNG TO YUMTHANG VALLEY TO GANGTOK',
                (
                    'THE VALLEY OF FLOWERS – SHANGRI-LA EXPERIENCED Drive early to the spectacular Yumthang Valley, popularly known as the Valley of Flowers. Situated at 11,800 feet, this valley features a breathtaking landscape where pristine rivers carve through lush meadows covered in dozens of unique rhododendron species. Visit the natural sulfur hot springs before starting your return drive to Gangtok, soaking in the changing evening hues of the mountain ranges.'
                ),
                [
                    'Sightseeing Included: Yumthang Flower Valley, Pine Forest Trails, Natural Hot Springs.',
                    'Optional Activities: Excursion further up to Zero Point (Yumesamdong) to touch everlasting snow.',
                    'Overnight Stay: Gangtok (Premium / Luxury Mountain Resort)',
                    'Meals Included: Premium Breakfast & Luxury Farewell Dinner',
                ],
            ),
            _day(
                5,
                'GANGTOK URBAN & CULTURAL SIGHTSEEING',
                (
                    'BUDDHIST MONASTIC HERITAGE & ARCHITECTURAL GEMS Devote your day to discovering the top tourist places in Gangtok. Tour the majestic Rumtek Monastery, a world-renowned seat of Tibetan Buddhist architecture and spirituality. Visit the Namgyal Institute of Tibetology to explore rare historical manuscripts and religious artwork. Conclude your afternoon at the Ganesh Tok and Hanuman Tok viewpoints for sweeping panoramic vistas of the urban landscape backed by snowy ridges. Show.'
                ),
                [
                    'Sightseeing Included: Rumtek Monastery, Namgyal Institute, Do Drul Chorten, Director of Handicrafts, Flower',
                    'Evening Experience: Exclusive fine-dining tasting menu highlighting gourmet Sikkimese cuisine.',
                    'Overnight Stay: Gangtok (Premium / Luxury Mountain Resort)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                6,
                'GANGTOK TO DEPARTURE',
                (
                    'CHRENGTHENING BONDS – CREATING MEMORIES BEYOND DESTINATIONS Indulge in a final lavish breakfast at your luxury resort while watching the sunrise illuminate the valleys. Your private luxury transport will escort you safely back along the foothill highways toward Bagdogra Airport or Pakyong Airport for your departure flight. Return home carrying a heart filled with alpine serenity and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury chauffeur-driven airport drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Summit Golden Crescent /',
                'Gangtok',
                '6N',
                'Deluxe',
                'similar',
                'Alpine Resort Lachung /',
                4,
                1,
                description='OPTION 01 – DELUXE: Summit Golden Crescent / | similar | Alpine Resort Lachung /',
            ),
            _hotel(
                'Lemon Tree Hotel / Chumbi',
                'Gangtok',
                '6N',
                'Premium',
                'Mountain Resort',
                'Lachung Continental /',
                4,
                2,
                description='OPTION 02 – PREMIUM: Lemon Tree Hotel / Chumbi | Mountain Resort | Lachung Continental /',
            ),
            _hotel(
                'Mayfair Spa Resort & Casino /',
                'Gangtok',
                '6N',
                'Luxury',
                'The Elgin Nor-Khill',
                'Yarlam Resort Lachung',
                4,
                3,
                description='OPTION 03 – LUXURY: Mayfair Spa Resort & Casino / | The Elgin Nor-Khill | Yarlam Resort Lachung',
            ),
            _hotel(
                'Vivanta Gangtok, Pakyong /',
                'Gangtok',
                '6N',
                'Ultra Luxury',
                'Mayfair Executive Suite',
                'The Retreat Lachung (Ultra',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Vivanta Gangtok, Pakyong / | Mayfair Executive Suite | The Retreat Lachung (Ultra',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury accommodations as per chosen hotel profile matrix.', 1),
            _inc_included('Luxury Transportation: Private dedicated SUV (Innova Crysta) for all terrains.', 2),
            _inc_included('Curated Meal Plan: Daily premium breakfast and gourmet multi-cuisine dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 localized guest relationship manager and permit handling.', 4),
            _inc_included('Welcome Amenities: Personalized Himalayan herbal tea kit and altitude health packs.', 5),
            _inc_included('Complimentary Experience: Private family traditional Sikkimese high-tea setup.', 6),
            _inc_excluded('Airfare, domestic flights, or train ticket costs to bagdogra.', 7),
            _inc_excluded('Zero Point or Nathula Pass surcharges imposed by local unions.', 8),
            _inc_excluded('Personal expenses such as laundry, liquor bar tabs, telephone bills, and tips.', 9),
            _inc_excluded('Any insurance premium fees or medical emergency evacuation costs.', 10),
        ],
    )
    return package, itinerary

def build_sk_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SK-013'
    tour_code = 'TRG-SIK-013'
    title = 'SIKKIM HERITAGE TOUR • MYSTICAL MONASTERIES & ALPINE GRANDEUR'
    duration = '06 Nights / 07 Days'
    slug = 'sk-013-sikkim-heritage-tour-mystical-monasteries-alpine-grandeur'
    itin_slug = 'sk-013-sikkim-heritage-tour-mystical-monasteries-alpine-grandeur-itinerary'
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
            _ph('Serial code SK-013 | TRAGUIN tour code TRG-SIK-013', 1),
            _ph('State / Country: Sikkim / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Gangtok • Sikkim', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury SUV (Innova/Xylo) / MAPAI (Premium Meals)', 7),
            _ph('TRAGUIN Signature Experience: Private, hassle-free processing of restricted area permits for Tsomgo', 8),
            _ph('Curated by TRAGUIN Experts: Relaxed driving schedules that minimize mountain sickness while', 9),
            _ph('Premium Handpicked Hotels: Resort properties selected for spectacular balcony views of mountain', 10),
            _ph('Luxury Transportation: Expert local drivers thoroughly trained in mountain safety rules and photography', 11)
        ],
        moods=['Luxury', 'Nature', 'Culture'],
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
        tagline='SIKKIM HERITAGE TOUR',
        overview='GRANDEUR Welcome to an unforgettable journey curated exclusively by TRAGUIN. Embark on the finest Sikkim Family Tour designed to reveal the breathtaking landscapes, age-old Buddhist legacies, and pristine alpine wonders of this magnificent Himalayan kingdom. As your premier travel consultants, TRAGUIN transforms TRAGUIN Premium Luxury Itinerary — SK-013 1 your vacation into a seamless luxury holiday filled with handpicked hotels, immersive experiences, and deeply touching local insights. From the misty heights and prayer flags of Gangtok to the dramatic reflection of the holy Tsomgo Lake and the majestic heritage of Pelling facing Mount Kanchenjunga, every detail is engineered to create unforgettable memories.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers an exquisite balance between sacred royal histories, alpine wildlife lakes, and contemporary mountain leisure. Travelling in a dedicated premium luxury 4-wheel drive vehicle with professional chauffeur-driven assistance, your family will enjoy absolute safety and comfort over mountain passes. With a carefully curated meal plan featuring lavish breakfasts and specialized ethnic dinners, this route represents the definitive premium Sikkim experience. Every step of your journey includes the signature touch of TRAGUIN curated experiences, ensuring VIP permit processing, local storytelling insight, and around-the-clock bespoke support.\n\nWHY CHOOSE THE BEST SIKKIM TOUR PACKAGE?\nWhen considering a Luxury Sikkim Holiday, discerning travellers seek more than just standard high-altitude driving; they seek a deeply immersive dive into timeless spirituality, natural preservation, and superior comfort. Sikkim boasts some of the most iconic attractions in Northeast India. From the holy and frozen alpine waters of Tsomgo Lake—a top tourist place in Sikkim for high-altitude photography—to the ancient, serene chanting halls of Rumtek and Pemayangtse Monasteries, the region offers unparalleled depth. For families and couples booking a bespoke Sikkim Honeymoon Package or Sikkim Family Tour, the state reveals highly popular Instagram locations like the Skywalk in Pelling, the misty paths of MG Marg, and the dramatic backdrop of Nathula Pass. Whether you are looking for local hand-woven carpet shopping, indulging in authentic Himalayan culinary delights, or seeking historical enlightenment along the old Silk Route paths, our TRAGUIN Sikkim Packages guarantee premium comfort, handpicked luxury stays, and curated exclusive experiences that make it the best time to visit Sikkim.',
        seo_title='SK-013 | SIKKIM HERITAGE TOUR | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Sikkim package (SK-013 / TRG-SIK-013): Gangtok • Sikkim with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GANGTOK', 1),
            _ih('Day 02: EXCURSION TO TSOMGO LAKE & BABA MANDIR', 2),
            _ih('Day 03: GANGTOK HIGH-END SIGHTSEEING', 3),
            _ih('Day 04: GANGTOK TO PELLING VIA NAMCHI', 4),
            _ih('Day 05: PELLING SIGHTSEEING & EXPERIENCE', 5),
            _ih('Day 06: PELLING TO GANGTOK (OR SILIGURI/BAGDOGRA EN-ROUTE STAY)', 6),
            _ih('Day 07: DEPARTURE VIA BAGDOGRA / NJP', 7),
            _ih('TRAGUIN Signature Experience: Private, hassle-free processing of restricted area permits for Tsomgo', 8),
            _ih('Curated by TRAGUIN Experts: Relaxed driving schedules that minimize mountain sickness while', 9),
            _ih('Premium Handpicked Hotels: Resort properties selected for spectacular balcony views of mountain', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GANGTOK',
                (
                    'WELCOME TO THE REGINA OF THE HILLS – EN-ROUTE MISTY VALLEY ASCENT Your premium Sikkim experience begins as you arrive at Bagdogra Airport (IXB) or New Jalpaiguri Railway Station (NJP), where a dedicated private luxury transport vehicle waits to escort you. Travel along the winding emerald waters of the Teesta River, mounting through lush green pine valleys up to Gangtok, the charming capital city of Sikkim. Check into your handpicked premium luxury hotel and enjoy a personalized welcome'
                ),
                [
                    'Sightseeing Included: Teesta River viewpoint drive, MG Marg evening promenade walk.',
                    'Evening Experience: Gourmet dinner featuring a fusion of Sikkimese and continental cuisines curated by',
                    'Overnight Stay: Gangtok (Premium / Luxury Mountain Resort)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'EXCURSION TO TSOMGO LAKE & BABA MANDIR',
                (
                    'SACRED ALPINE WATERS & DRAMATIC GLACIAL VIEWS Awake early for a spectacular morning excursion towards the sacred Tsomgo Lake, situated at an altitude of 12,400 feet. This oval-shaped glacial lake is deep in spiritual lore and offers breathtaking landscapes as the surrounding snow-capped peaks reflect on its surface. Enjoy a romantic or family yak ride along the snowbanks. Proceed further to visit the Baba Harbhajan Singh Memorial Mandir, an emotionally moving shrine built in honor of a legendary brave soldier. Weather and permit permitting, catch sight of the historic Indo-China border at Nathula Pass.'
                ),
                [
                    'Sightseeing Included: Tsomgo Holy Lake, Baba Mandir, Alpine Viewpoints.',
                    'Optional Activities: Nathula Pass Indo-China Border Extension (subject to prior permit confirmation).',
                    'Overnight Stay: Gangtok (Premium / Luxury Mountain Resort)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'GANGTOK HIGH-END SIGHTSEEING',
                (
                    'BUDDHIST HERITAGE & IMPERIAL MONASTIC CHANTS Dedicate this day to exploring the deep heritage and cultural landmarks of Gangtok. Visit the world-renowned Rumtek Monastery, a magnificent seat of Tibetan Buddhism showcasing complex architectural paintings and sacred gold stupas. Explore the Namgyal Institute of Tibetology to view ancient manuscripts and thangkas, followed by the peaceful Do Drul Chorten stupa. Conclude your day by observing the exquisite exotic flora at the Flower Exhibition Centre. Viewpoint. venue.'
                ),
                [
                    'Sightseeing Included: Rumtek Monastery, Directorate of Handicrafts, Tibetology Institute, Do Drul Chorten, Tashi',
                    'Evening Experience: Private authentic tea tasting session and local lifestyle presentation at a premium heritage',
                    'Overnight Stay: Gangtok (Premium / Luxury Mountain Resort)',
                    'Meals Included: Breakfast & Curated Pan-Asian Dinner',
                ],
            ),
            _day(
                4,
                'GANGTOK TO PELLING VIA NAMCHI',
                (
                    "THE PATH OF SACRED ICONS & PANORAMIC TERRACES Depart after a hearty breakfast on a beautiful trans-valley road trip towards the pristine hamlet of Pelling. En route, your private luxury transport stops at Namchi to visit the majestic Siddheshwar Dham (Chardham), featuring a breathtaking 108-foot statue of Lord Shiva atop Solophok Hill, surrounded by miniature replicas of India's sacred shrines. Continue through terraced tea estates into Pelling, a peaceful village offering the closest panoramic views of the mighty Mount Kanchenjunga range. local brew."
                ),
                [
                    'Sightseeing Included: Namchi Chardham Complex, Samdruptse Statue, Scenic Mountain Ridge Trails.',
                    'Evening Experience: Relaxed sunset viewing from your resort balcony overlooking the snowy ranges with hot',
                    'Overnight Stay: Pelling (Premium Valley Facing Luxury Stay)',
                    'Meals Included: Breakfast & Traditional Elite Dinner',
                ],
            ),
            _day(
                5,
                'PELLING SIGHTSEEING & EXPERIENCE',
                (
                    "GLASS SKYWALKS, THUNDERING FALLS & ROYAL RUINS Experience a thrilling day of sightseeing around Pelling. Walk onto India's first glass Skywalk, suspended directly opposite the colossal Chenrezig statue, offering an exhilarating perspective of the valley below. Visit the sacred, wish-fulfilling Khecheopalri Lake, beautifully hidden inside thick forests, and admire the cascading Rimbi and Kanchenjunga Waterfalls. Later, walk amidst the romantic stone ruins of the Rabdentse Palace, the ancient second capital of the Sikkimese Kingdom. Khecheopalri Lake, Kanchenjunga Falls."
                ),
                [
                    'Sightseeing Included: Pelling Skywalk & Chenrezig Statue, Pemayangtse Monastery, Rabdentse Ruins,',
                    'Optional Activities: Private heritage photography walk with a local cultural archivist.',
                    'Overnight Stay: Pelling (Premium Valley Facing Luxury Stay)',
                    'Meals Included: Breakfast & Farewell Premium Dinner',
                ],
            ),
            _day(
                6,
                'PELLING TO GANGTOK (OR SILIGURI/BAGDOGRA EN-ROUTE STAY)',
                (
                    'CHERISHING THE MEMORIES OF THE SEVEN SISTERS Enjoy a quiet sunrise over the eternal snow peaks. After a leisurely breakfast, drive back along scenic pathways, stopping at beautiful mountain viewpoints and orange orchards. Arrive back for your final evening in the hills, ideal for catching any missed local experiences, shopping for exquisite curios, or relaxing in a premium spa hotel environment.'
                ),
                [
                    'Sightseeing Included: En-route mountain photography points, Local handicraft shopping stops.',
                    'Evening Experience: Special farewell family cocktail/mocktail hours hosted by the resort.',
                    'Overnight Stay: Gangtok or Siliguri En-route Premium Hotel',
                    'Meals Included: Breakfast & Gala Dinner',
                ],
            ),
            _day(
                7,
                'DEPARTURE VIA BAGDOGRA / NJP',
                (
                    'RETURN WITH UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Indulge in your final lavish breakfast at your premium hotel. Your private luxury transport will safely drive you back down the scenic foothill highways to Bagdogra Airport or New Jalpaiguri Railway Station for your onward journey home. Return with your spirit rejuvenated, carrying a chest full of beautiful family bonds and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury airport or railway door-to-door drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Summit Golden Crescent /',
                'Gangtok',
                '6N',
                'Deluxe',
                'similar',
                'The Premium Heritage /',
                4,
                1,
                description='OPTION 01 – DELUXE: Summit Golden Crescent / | similar | The Premium Heritage /',
            ),
            _hotel(
                'Lemon Tree Hotel / Mayfair Spa',
                'Gangtok',
                '6N',
                'Premium',
                'Resort',
                'The Elgin Mount Pandim',
                4,
                2,
                description='OPTION 02 – PREMIUM: Lemon Tree Hotel / Mayfair Spa | Resort | The Elgin Mount Pandim',
            ),
            _hotel(
                'The Ramada by Wyndham /',
                'Gangtok',
                '6N',
                'Luxury',
                'Welcomheritage',
                'Chumbi Mountain',
                4,
                3,
                description='OPTION 03 – LUXURY: The Ramada by Wyndham / | Welcomheritage | Chumbi Mountain',
            ),
            _hotel(
                'Mayfair Imperial Villa / Taj',
                'Gangtok',
                '6N',
                'Ultra Luxury',
                'Guras Kutir',
                'The Chumbi Mountain',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Mayfair Imperial Villa / Taj | Guras Kutir | The Chumbi Mountain',
            )
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Handpicked luxury stays as per chosen tier.', 1),
            _inc_included('Luxury Transportation: Private dedicated SUV (Innova/Crysta) for all mountain runs.', 2),
            _inc_included('Curated Meal Plan: Daily premium breakfasts and gourmet themed dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest relation manager and permit handler.', 4),
            _inc_included('Welcome Amenities: Customized family travel gift bag, bottled spring water, and high-altitude snacks.', 5),
            _inc_included('Complimentary Experience: Entry tickets to the spectacular Pelling Glass Skywalk.', 6),
            _inc_excluded('Airfare, domestic flights, or main railway lines ticketing.', 7),
            _inc_excluded('Nathula Pass supplementary vehicle charges (payable directly to local syndicate).', 8),
            _inc_excluded('Personal expenses such as premium alcoholic beverages, laundry, and porter tips.', 9),
            _inc_excluded('Optional activities like yak rides, helicopter rides, or travel insurance.', 10),
        ],
    )
    return package, itinerary

def build_sk_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SK-014'
    tour_code = 'TRG-SIK-014'
    title = 'COMPLETE SIKKIM DELUXE • MYSTICAL PEAKS & SACRED VALLEYS'
    duration = '08 Nights / 09 Days'
    slug = 'sk-014-complete-sikkim-deluxe-mystical-peaks-sacred-valleys'
    itin_slug = 'sk-014-complete-sikkim-deluxe-mystical-peaks-sacred-valleys-itinerary'
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
            _ph('Serial code SK-014 | TRAGUIN tour code TRG-SIK-014', 1),
            _ph('State / Country: Sikkim / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Gangtok • Tsomgo', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Innova Crysta / Luxury MAPAI Plan', 7),
            _ph('TRAGUIN Signature Experience: Private family briefing and permit facilitation seamlessly handled', 8),
            _ph('Curated by TRAGUIN Experts: Custom high-altitude pacing designed to ensure comfortable', 9),
            _ph('Premium Handpicked Hotels: Elite properties offering breathtaking mountain views, reliable heating, and', 10),
            _ph('Luxury Transportation: Expertly vetted mountain drivers ensuring absolute safety and smooth travel on', 11)
        ],
        moods=['Luxury', 'Nature'],
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
        tagline='COMPLETE SIKKIM DELUXE',
        overview='VALLEYS TRAGUIN Premium Luxury Itinerary — SK-014 1 Welcome to an extraordinary high-altitude retreat curated exclusively by TRAGUIN. Embark on the definitive Sikkim Family Tour, seamlessly structured to reveal the breathtaking landscapes, emerald-green valleys, and magnificent snow-clad vistas of India’s most mystical state. As your professional luxury travel consultants, TRAGUIN transforms your vacation into an unforgettable escape filled with premium stays, deep cultural discovery, and handpicked hotels. From the cascading waterfalls of Gangtok to the sacred shores of Tsomgo Lake, the pristine high-altitude deserts of Lachen, and the panoramic mountain views of Pelling, every detail has been perfectly tailored to design unforgettable memories.\n\nTOUR OVERVIEW\nThis bespoke luxury holiday itinerary offers an unmatched exploration of North, East, and West Sikkim. Travelling in a completely private premium SUV with an experienced hill chauffeur, your family will experience absolute safety, privacy, and elite luxury. With a detailed meal plan featuring gourmet daily breakfasts and curated multi-cuisine dinners, this route represents the finest premium Sikkim experience available. Every milestone of your journey features the signature touch of TRAGUIN curated experiences, assuring personalized entry permits, VIP handling, and 24/7 dedicated guest assistance.\n\nWHY CHOOSE THE BEST SIKKIM TOUR PACKAGE?\nWhen exploring a Luxury Sikkim Holiday, discerning families and travelers look for a flawless balance of raw nature, timeless spiritual heritage, and premium modern comfort. Sikkim stands out as an unparalleled alpine wonderland, making a Sikkim Family Tour or a romantic Sikkim Honeymoon Package a deeply rewarding lifetime experience. From the dynamic streets of Gangtok to iconic attractions like the Gurudongmar Lake— one of the highest alpine lakes in the world—Sikkim sightseeing leaves travelers inspired. Sikkim hosts incredibly popular Instagram locations, from the iconic prayer-flag-strewn structures of the Pelling Skywalk to the vibrant rhododendron fields inside the stunning Yumthang Valley. Immerse your family in local monastery culture at Pemayangtse, enjoy the pure adrenaline of high-altitude passes, and shop for authentic Tibetan handicrafts. Our tailored TRAGUIN Sikkim Packages guarantee immersive experiences, premium',
        seo_title='SK-014 | COMPLETE SIKKIM DELUXE | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days Sikkim package (SK-014 / TRG-SIK-014): Gangtok • Tsomgo with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL AT IXB AIRPORT / NJP RAILWAY STATION TO GANGTOK', 1),
            _ih('Day 02: EXCURSION TO TSOMGO LAKE & BABA MANDIR', 2),
            _ih('Day 03: GANGTOK TO LACHEN', 3),
            _ih('Day 04: LACHEN TO GURUDONGMAR LAKE TO LACHUNG', 4),
            _ih('Day 05: LACHUNG TO YUMTHANG VALLEY TO GANGTOK', 5),
            _ih('Day 06: GANGTOK FULL DAY SIGHTSEEING', 6),
            _ih('Day 07: GANGTOK TO PELLING (VIA RAVANGLA)', 7),
            _ih('Day 08: PELLING FULL DAY EXCURSION', 8),
            _ih('TRAGUIN Signature Experience: Private family briefing and permit facilitation seamlessly handled', 9),
            _ih('Curated by TRAGUIN Experts: Custom high-altitude pacing designed to ensure comfortable', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL AT IXB AIRPORT / NJP RAILWAY STATION TO GANGTOK',
                (
                    'WELCOME TO THE GATEWAY OF SIKKIM – SCENIC RIVERSIDE ASCENT Your premium Sikkim experience kicks off as you arrive at Bagdogra Airport (IXB) or New Jalpaiguri Railway Station (NJP). Your dedicated private luxury transport vehicle waits to receive you warmly. Embark on a highly scenic drive passing lush green tea gardens before running parallel to the majestic, roaring Teesta River.'
                ),
                [
                    'Sightseeing Included: Teesta River viewpoint, MG Marg evening promenade walk.',
                    'Evening Experience: Bespoke family orientation session over welcome drinks, hosted via TRAGUIN support.',
                    'Overnight Stay: Gangtok (Premium Luxury Hotel)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'EXCURSION TO TSOMGO LAKE & BABA MANDIR',
                (
                    'SACRED HIGH-ALTITUDE LAKES & GLACIAL MAJESTY Relish a rich buffet breakfast before departing on an epic high-altitude mountain excursion towards East Sikkim. Arrive at the mystical, oval-shaped Tsomgo Lake (Changu Lake), located at a breathtaking altitude of 12,400 feet. The sacred waters reflect the surrounding snow peaks gracefully, creating a stunning popular Instagram location. Continue the drive to the historic Baba Harbhajan Singh Memorial Mandir, a site rich in moving local military lore.'
                ),
                [
                    'Sightseeing Included: Sacred Tsomgo Lake, Baba Harbhajan Singh Shrine, Kyongnosla Alpine Sanctuary view.',
                    'Optional Activities: Nathu La Pass border tour (subject to government permit availability and extra cost).',
                    'Overnight Stay: Gangtok (Premium Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Handpicked Dinner',
                ],
            ),
            _day(
                3,
                'GANGTOK TO LACHEN',
                (
                    'JOURNEY TO THE NORTH – WATERFALLS AND MAJESTIC GORGES Check out after an early morning breakfast and begin a dramatic drive into the rugged terrain of North Sikkim. Your private luxury Innova Crysta weaves past iconic attractions like the Seven Sisters Waterfalls and the spectacular Singhik Viewpoint, which offers breathtaking landscapes of Mount Khangchendzonga on a clear day. Stop for a delightful lunch at Chungthang before arriving at the serene alpine village of Lachen, nestled among towering pine cliffs.'
                ),
                [
                    'Sightseeing Included: Seven Sisters Waterfalls, Naga Waterfalls, Singhik Viewpoint, Chungthang Confluence.',
                    'Evening Experience: Cozy, relaxed family evening around a traditional wooden hearth in Lachen.',
                    'Overnight Stay: Lachen (Premium Selected Luxury Mountain Lodge)',
                    'Meals Included: Breakfast, En-route Lunch & Hot Mountain Dinner',
                ],
            ),
            _day(
                4,
                'LACHEN TO GURUDONGMAR LAKE TO LACHUNG',
                (
                    'GURUDONGMAR SACRED WATERS – STANDING AT THE ROOF OF INDIA At the crack of dawn, embark on an unforgettable journey to the legendary Gurudongmar Lake. Situated at an astounding 17,800 feet, this is one of the highest lakes globally, surrounded by sacred glaciers. Part of the lake remains miraculously unfrozen even in deep winter, offering an emotionally moving spiritual ambience and a premier photography point. Return to Lachen for lunch, pack your bags, and drive to the beautiful sister valley of Lachung.'
                ),
                [
                    'Sightseeing Included: Sacred Gurudongmar Lake, Thangu Valley alpine meadows, Cold Desert plateau.',
                    'Optional Activities: A custom breakfast box packing service arranged smoothly by your premium stay hotel.',
                    'Overnight Stay: Lachung (Premium Luxury Cottage Property)',
                    'Meals Included: Early Light Breakfast, Warm Lunch & Premium Alpine Dinner',
                ],
            ),
            _day(
                5,
                'LACHUNG TO YUMTHANG VALLEY TO GANGTOK',
                (
                    'THE VALLEY OF FLOWERS & NATURAL HOT SPRINGS Drive after an early breakfast to the spectacular Yumthang Valley, popularly known as the Valley of Flowers. Surrounded by majestic snow peaks, the valley meadows are covered in vibrant rhododendron blooms in spring, making it a highly searched tourism keyword location. Visit the local natural sulfur hot springs, believed to possess powerful healing properties. After soaking in the scenic beauty, return to Lachung for lunch before driving back to Gangtok to relax. cost).'
                ),
                [
                    'Sightseeing Included: Yumthang Valley, Shingba Rhododendron Sanctuary, Medicinal Hot Springs.',
                    'Optional Activities: Excursion further up to Zero Point (Yumesamdong) to play in the perennial snow (extra',
                    'Overnight Stay: Gangtok (Premium Luxury Hotel)',
                    'Meals Included: Premium Breakfast, Lunch & Elegant Gangtok Dinner',
                ],
            ),
            _day(
                6,
                'GANGTOK FULL DAY SIGHTSEEING',
                (
                    "BUDDHIST MONASTIC HERITAGE & PANORAMIC CABLE RIDES Devote a relaxed, wonderful day to exploring the deep-rooted culture, arts, and iconic attractions of Gangtok. Visit the world-famous Rumtek Monastery, a global seat of Tibetan Buddhist architecture and learning. Explore the Namgyal Institute of Tibetology to view ancient manuscripts, followed by a panoramic aerial ride on the Gangtok Ropeway to capture the city's scenic beauty from high above."
                ),
                [
                    'Sightseeing Included: Rumtek Monastery, Do Drul Chorten, Institute of Tibetology, Flower Exhibition Show,',
                    'Evening Experience: Private culinary tasting of boutique local momos and organic Himalayan teas.',
                    'Overnight Stay: Gangtok (Premium Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Signature Dinner',
                ],
            ),
            _day(
                7,
                'GANGTOK TO PELLING (VIA RAVANGLA)',
                (
                    'THE TATHAGATA STHALA – GLISTENING BUDDHA PARK MAJESTY Depart Gangtok and travel southwest toward Pelling. En-route, visit Ravangla to witness the breathtaking Buddha Park (Tathagata Tsal), featuring a majestic 130-foot-tall bronze statue of Lord Buddha framed perfectly against Mt. Narsing. Arrive in Pelling in the afternoon and check into your ultra-luxury resort. Pelling offers the closest, most intimate panoramic views of the entire Khangchendzonga mountain range.'
                ),
                [
                    'Sightseeing Included: Buddha Park Ravangla, Rabdentse Ruins scenic eco-trail walk.',
                    "Evening Experience: Sunset tea ceremony on your resort's private deck overlooking the snow mountains.",
                    'Overnight Stay: Pelling (Premium Handpicked Luxury Mountain Resort)',
                    'Meals Included: Premium Breakfast & Fine Dining Dinner',
                ],
            ),
            _day(
                8,
                'PELLING FULL DAY EXCURSION',
                (
                    "GLASS SKYWALKS, SACRED LAKES & ANCIENT PALACES Embark on a spectacular final sightseeing tour of West Sikkim. Step out onto India's first glass Skywalk, facing the giant Chenrezig statue, which provides a thrilling walking experience suspended directly over deep green valleys. Visit the sacred, wish-fulfilling Khecheopalri Lake, beautifully hidden inside thick foliage, and experience the stunning Rimbi Waterfalls. Rimbi Falls."
                ),
                [
                    'Sightseeing Included: Pelling Glass Skywalk, Chenrezig Statue, Khecheopalri Lake, Pemayangtse Monastery,',
                    'Optional Activities: Bespoke family group portrait session inside the historical Rabdentse palace estate ruins.',
                    'Overnight Stay: Pelling (Premium Handpicked Luxury Mountain Resort)',
                    'Meals Included: Premium Breakfast & Farewell Family Gala Dinner',
                ],
            ),
            _day(
                9,
                'PELLING TO IXB AIRPORT / NJP STATION DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Indulge in a final lavish breakfast as the golden sun illuminates the peaks of Mount Khangchendzonga. Pack your bags, board your premium luxury transportation vehicle, and descend the beautiful winding foothills back towards Bagdogra Airport (IXB) or NJP station for your return flight home. Your magical journey concludes with deep family bonds and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury highway drop-off to station / airport.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Summit Golden Crescent /',
                'Gangtok',
                '8N',
                'Deluxe',
                'similar',
                'Lachen Horizon /',
                4,
                1,
                description='OPTION 01 – DELUXE: Summit Golden Crescent / | similar | Lachen Horizon /',
            ),
            _hotel(
                'Lemon Tree Hotel / Mayfair',
                'Gangtok',
                '8N',
                'Premium',
                'Spa Resort',
                'The Delight Lachen /',
                4,
                2,
                description='OPTION 02 – PREMIUM: Lemon Tree Hotel / Mayfair | Spa Resort | The Delight Lachen /',
            ),
            _hotel(
                'The Elgin Nor-Khill /',
                'Gangtok',
                '8N',
                'Luxury',
                'Welcomheritage',
                'Luxury Wooden Chalet',
                4,
                3,
                description='OPTION 03 – LUXURY: The Elgin Nor-Khill / | Welcomheritage | Luxury Wooden Chalet',
            ),
            _hotel(
                'Mayfair Spa Resort',
                'Gangtok',
                '8N',
                'Ultra Luxury',
                '(Executive Suite)',
                'VIP Custom Private',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Mayfair Spa Resort | (Executive Suite) | VIP Custom Private',
            )
        ],
        inclusions=[
            _inc_included('Premium stays: 08 Nights in selected deluxe and luxury properties.', 1),
            _inc_included('Luxury Transportation: Private dedicated Innova Crysta for all transfers.', 2),
            _inc_included('Curated Meal Plan: Daily luxury breakfasts and gourmet dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated local guest experience manager.', 4),
            _inc_included('Welcome Amenities: Personalized welcome kit, snacks, and high-altitude health aids.', 5),
            _inc_included('Complimentary Experience: Private sunset deck tea ceremony in Pelling.', 6),
            _inc_excluded('Airfare, domestic flights, or main railway line tickets.', 7),
            _inc_excluded('Nathu La Pass & Zero Point supplementary trip costs.', 8),
            _inc_excluded('Personal items, laundry bills, bar tabs, and porter tips.', 9),
            _inc_excluded('Monument admission tickets, local guide hiring, camera fees.', 10),
        ],
    )
    return package, itinerary

def build_sk_015(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'SK-015'
    tour_code = 'TRG-SIK-015'
    title = 'EDUCATIONAL SIKKIM • GEOGRAPHY, CULTURE & LIVING SCIENCE'
    duration = '05 Nights / 06 Days'
    slug = 'sk-015-educational-sikkim-geography-culture-living-science'
    itin_slug = 'sk-015-educational-sikkim-geography-culture-living-science-itinerary'
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
            _ph('Serial code SK-015 | TRAGUIN tour code TRG-SIK-015', 1),
            _ph('State / Country: Sikkim / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Gangtok • Tsomgo', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Luxury Buses/ Sumos / Full Board (APAI - All Meals)', 7),
            _ph('TRAGUIN Signature Experience: Private academic interaction session with senior conservationists to', 8),
            _ph('Curated by TRAGUIN Experts: Structuring perfect, unhurried high-altitude travel curves to guarantee', 9),
            _ph('Premium Handpicked Hotels: Properties thoroughly audited for student group safety, space, and pristine', 10),
            _ph('Exclusive Recommendations: Secured fast-track access permissions for key heritage museums and', 11)
        ],
        moods=['Luxury', 'Culture', 'Educational'],
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
        tagline='EDUCATIONAL SIKKIM',
        overview="SCIENCE Welcome to a profound learning expedition curated exclusively by TRAGUIN. Embark on the definitive Sikkim Family Tour and Educational Program, engineered to introduce young minds to the breathtaking landscapes, biodiversity hot spots, and profound cultural heritage of the Eastern Himalayas. As your premier luxury travel consultants, TRAGUIN elevates student travel into an elite, highly organized immersive TRAGUIN Premium Luxury Educational Itinerary — SK-015 1 experience. Merging premium stays with handpicked hotels, we turn regional geography, Himalayan geology, and eco-conservation into unforgettable memories.\n\nTOUR OVERVIEW\nThis custom-tailored institutional educational itinerary offers a perfect balance between interactive academic learning and premium travel comfort. Moving across diverse altitudes under the care of dedicated student coordinators and expert local marshals, students explore pristine high-altitude ecosystems and timeless spiritual heritage. Featuring robust safety logistics, premium handpicked hotels, and a comprehensive meal plan with hygienic, nutrient-balanced multi-cuisine dining, this represents the signature premium Sikkim experience. Every group tour integrates a TRAGUIN curated experience note, providing expert naturalists, interactive group activities, and absolute 24/7 priority support.\n\nWHY CHOOSE THE BEST SIKKIM TOUR PACKAGE FOR INSTITUTIONS?\nWhen arranging a Luxury Sikkim Holiday or academic group venture, educational leaders require deep institutional expertise, flawless safety standards, and engaging pedagogical content. Sikkim stands out as an exceptional living laboratory. From the alpine ecosystems of Tsomgo Lake—a top tourist place in Sikkim for studying Himalayan hydrology—to the grand monuments of Namchi, Sikkim sightseeing introduces students to critical concepts in environmental conservation, history, and physical geography. For educational bodies, schools, and even newlywed couples booking a Sikkim Honeymoon Package or Sikkim Family Tour, the region offers breathtaking popular Instagram locations like the Buddha Park of Ravangla and the sweeping views of the Kanchenjunga range. Whether it is studying the unique organic farming policies of the state, visiting centuries-old monasteries, or enjoying handicraft shopping at Gangtok's MG Marg, our specialized TRAGUIN Sikkim Packages guarantee elite comfort, immersive experiences, and structural premium execution at the best time to visit Sikkim.",
        seo_title='SK-015 | EDUCATIONAL SIKKIM | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Sikkim package (SK-015 / TRG-SIK-015): Gangtok • Tsomgo with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL & DRIVE TO GANGTOK', 1),
            _ih('Day 02: EXCURSION TO TSOMGO LAKE & BABA MANDIR', 2),
            _ih('Day 03: GANGTOK SIGHTSEEING & RESEARCH CENTERS', 3),
            _ih('Day 04: GANGTOK TO NAMCHI & RAVANGLA', 4),
            _ih('Day 05: ORGANIC FARMING AND TEA GARDENS EXCURSION', 5),
            _ih('Day 06: DEPARTURE TO NJP / BAGDOGRA', 6),
            _ih('TRAGUIN Signature Experience: Private academic interaction session with senior conservationists to', 7),
            _ih('Curated by TRAGUIN Experts: Structuring perfect, unhurried high-altitude travel curves to guarantee', 8),
            _ih('Premium Handpicked Hotels: Properties thoroughly audited for student group safety, space, and pristine', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL & DRIVE TO GANGTOK',
                (
                    'WELCOME TO THE GATEWAY OF THE EASTERN HIMALAYAS Your premium Sikkim experience starts at Bagdogra Airport (IXB) or New Jalpaiguri Railway Station (NJP). A fleet of premium luxury transport vehicles and dedicated TRAGUIN coordinators will welcome the group. Embark on a highly scenic drive winding alongside the magnificent Teesta River, where students can observe mountain river morphology first-hand. Arrive in Gangtok, the beautiful capital of Sikkim, check into your premium hotels, and attend an evening orientation briefing. TRAGUIN Premium Luxury Educational Itinerary — SK-015 2'
                ),
                [
                    'Sightseeing Included: Teesta River Gorge viewpoint, Mahananda Wildlife sanctuary outskirts drive.',
                    'Evening Experience: Interactive group ice-breaking session and trip safety briefing over hot drinks.',
                    'Overnight Stay: Gangtok (Premium / Handpicked Group Hotel)',
                    'Meals Included: Welcome Evening Drinks & Fresh Buffet Dinner',
                ],
            ),
            _day(
                2,
                'EXCURSION TO TSOMGO LAKE & BABA MANDIR',
                (
                    'HIGH-ALTITUDE HYDROLOGY & GLACIAL GEOGRAPHY Awake early for a spectacular mountain drive to the sacred Tsomgo Lake, situated at an incredible altitude of 12,400 feet. This pristine glacial body offers breathtaking landscapes and serves as a stellar educational site to study glacial topography and high-altitude ecology. Continue the excursion to the historic Baba Harbhajan Singh Mandir to learn about regional border history and the geo-strategic significance of the area. Enjoy magnificent alpine photography points along the route.'
                ),
                [
                    'Sightseeing Included: Tsomgo Glacial Lake, Baba Harbhajan Singh Memorial, Snow Viewpoints.',
                    'Optional Activities: Interactive field-note entry session on high-altitude vegetation adaptation.',
                    'Overnight Stay: Gangtok (Premium / Handpicked Group Hotel)',
                    'Meals Included: Full Board - Hot Breakfast, Packaged Mid-day Lunch & Dinner',
                ],
            ),
            _day(
                3,
                'GANGTOK SIGHTSEEING & RESEARCH CENTERS',
                (
                    "BUDDHIST ARCHITECTURE, BOTANY & MONASTIC HISTORY Dedicate the day to exploring the deep cultural roots and scientific institutions of Gangtok. Visit the world- famous Namgyal Institute of Tibetology to study ancient manuscripts and Tibetan art. Explore the adjacent Orchid Sanctuary to learn about the state's rich floral biodiversity. Later, visit the magnificent Rumtek Monastery, an architectural masterpiece that offers a deep look into living monastic traditions. Centre. TRAGUIN Premium Luxury Educational Itinerary — SK-015 3"
                ),
                [
                    'Sightseeing Included: Rumtek Monastery, Namgyal Institute of Tibetology, Do Drul Chorten, Flower Exhibition',
                    'Evening Experience: Guided walk through MG Marg for urban planning study and local handicraft observations.',
                    'Overnight Stay: Gangtok (Premium / Handpicked Group Hotel)',
                    'Meals Included: Full Board - Breakfast, Traditional Local Lunch & Grand Dinner',
                ],
            ),
            _day(
                4,
                'GANGTOK TO NAMCHI & RAVANGLA',
                (
                    'HERITAGE ARCHITECTURE & SPIRITUAL GEOGRAPHY Travel South through beautiful terraced mountain landscapes towards Namchi, the cultural capital of South Sikkim. Visit the magnificent Samdruptse Hill to admire the monumental 135-foot statue of Guru Padmasambhava. Continue to the breathtaking Buddha Park of Ravangla, an iconic attraction featuring an exquisite 130-foot statue of Lord Buddha, set against the dramatic backdrop of Mount Kanchenjunga—a highly popular Instagram location.'
                ),
                [
                    'Sightseeing Included: Buddha Park (Tathagata Tsal), Samdruptse Hill, Char Dham Complex structural walk.',
                    'Evening Experience: Sunset photography workshop overlooking the mist-filled valley plains.',
                    'Overnight Stay: Ravangla / Namchi (Premium Selected Eco-Resort)',
                    'Meals Included: Full Board - Breakfast, Valley Lunch & Resort Dinner',
                ],
            ),
            _day(
                5,
                'ORGANIC FARMING AND TEA GARDENS EXCURSION',
                (
                    'SUSTAINABLE DEVELOPMENT & AGRO-ECONOMICS Spend a magnificent day studying agricultural economics and eco-sustainability models. Visit the lush, manicured slopes of the Temi Tea Garden—the only tea estate in Sikkim, famous globally for its premium organic tea. Students will engage in an educational tour with estate managers to learn about the processing, cultivation, and export metrics of organic tea production.'
                ),
                [
                    'Sightseeing Included: Temi Tea Estate walks, Organic farm demonstration fields, Local village interactive school.',
                    'Optional Activities: Traditional organic tea tasting workshop and cultural interaction with local communities.',
                    'Overnight Stay: Namchi / Gangtok (Premium Selected Property)',
                    'Meals Included: Full Board - Breakfast, Picnic Estate Lunch & Farewell Dinner',
                ],
            ),
            _day(
                6,
                'DEPARTURE TO NJP / BAGDOGRA',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Conclude your educational journey with a final morning buffet breakfast. Board your dedicated luxury transportation fleet as we drive back along the scenic hills down to Bagdogra Airport or NJP Station. Return to your home institution carrying enhanced knowledge, strengthened student bonds, and unforgettable memories designed meticulously by TRAGUIN. TRAGUIN Premium Luxury Educational Itinerary — SK-015 4'
                ),
                [
                    'Transfers Included: Private managed group transit back to railway/airport.',
                    'Meals Included: Lavish Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Summit Golden',
                'Gangtok',
                '5N',
                'Deluxe',
                'Crescent / similar',
                'Summit Sobralia Resort',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Summit Golden | Crescent / similar | Summit Sobralia Resort',
            ),
            _hotel(
                'Lemon Tree Hotel / Hotel',
                'Gangtok',
                '5N',
                'Premium',
                'Royal Plaza',
                'The Shambhala Resort /',
                4,
                2,
                description='OPTION 02 – PREMIUM: Lemon Tree Hotel / Hotel | Royal Plaza | The Shambhala Resort /',
            ),
            _hotel(
                'The Elgin Nor-Khill /',
                'Gangtok',
                '5N',
                'Luxury',
                'WelcomHeritage',
                'Cherry Resort Temi Tea',
                4,
                3,
                description='OPTION 03 – LUXURY: The Elgin Nor-Khill / | WelcomHeritage | Cherry Resort Temi Tea',
            ),
            _hotel(
                'Mayfair Spa Resort &',
                'Gangtok',
                '5N',
                'Ultra Luxury',
                'Casino (Suites)',
                'The Chumbi Mountain',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Mayfair Spa Resort & | Casino (Suites) | The Chumbi Mountain',
            )
        ],
        inclusions=[
            _inc_included('Premium stays: Group accommodations in handpicked, verified properties.', 1),
            _inc_included('Luxury Transportation: Fleet of dedicated vehicles for seamless field transit.', 2),
            _inc_included('Full Board Meals: Hygienic, nutritious breakfast, lunch, and dinner (APAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated on-tour manager and logistics support team.', 4),
            _inc_included('Welcome Amenities: Custom student learning kits, maps, and field guides.', 5),
            _inc_included('Complimentary Experiences: Guided organic tea factory workshop and study permissions.', 6),
            _inc_excluded('Airfare, commercial flights, or inbound train tickets.✘ Nathula Pass permits and associated local vehicle upgrades.', 7),
            _inc_excluded('Personal expenditures such as laundry, room service, telephone charges.', 8),
            _inc_excluded('Individual medical insurance and personal porterage.', 9),
        ],
    )
    return package, itinerary

SIKKIM_DOMESTIC_BUILDERS = [
    build_sk_001,
    build_sk_002,
    build_sk_003,
    build_sk_004,
    build_sk_005,
    build_sk_006,
    build_sk_007,
    build_sk_008,
    build_sk_009,
    build_sk_010,
    build_sk_011,
    build_sk_012,
    build_sk_013,
    build_sk_014,
    build_sk_015,
]
