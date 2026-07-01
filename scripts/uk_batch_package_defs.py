"""Builder functions for UK-001 through UK-010 Uttarakhand packages (no images)."""

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


def build_uk_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug='uk-001-nainital-escape-mystical-lakes',
        destination_id=destination_id,
        title='Nainital Escape • Mystical Lakes & Mountain Grandeur',
        duration_label='03 Nights / 04 Days',
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=20,
        is_published=True,
        highlights=[
            PackageHighlightNested(text='Nainital (3N) → Bhimtal • Sattal • Naukuchiatal lake district', sort_order=1),
    PackageHighlightNested(text='Private luxury AC vehicle with dedicated chauffeur', sort_order=2),
    PackageHighlightNested(text='MAP plan — breakfast and gourmet dinners', sort_order=3),
    PackageHighlightNested(text='Complimentary private boat ride on Naini Lake', sort_order=4),
    PackageHighlightNested(text='TRAGUIN 24/7 personalized concierge support', sort_order=5),
    PackageHighlightNested(text='Tour code TRG-UK-001 | Serial UK-001', sort_order=6),
        ],
        moods=['Family', 'Luxury', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug='uk-001-nainital-escape-itinerary',
        destination_id=destination_id,
        title='Nainital Escape • Mystical Lakes & Mountain Grandeur',
        duration_label='03 Nights / 04 Days',
        duration_days=4,
        starting_price=0,
        price_note='On Request (Bespoke Luxury Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Nainital • Bhimtal • Sattal • Naukuchiatal',
        overview='This custom-tailored premium tour itinerary has been intricately structured by TRAGUIN for discerning travelers who value elegance and flawless execution. Travelling from Delhi in a dedicated, high-end private vehicle accompanied by an experienced local chauffeur, you will explore the serene lake district of Kumaon. With a premium meal plan covering lavish daily breakfasts and multi-cuisine dinners, this journey guarantees comfort at every turn. Every detail features the signature touch of TRAGUIN curated experiences, assuring personalized VIP assistance and premium curated memories for your family.',
        seo_title='UK-001 | Nainital Escape Mystical Lakes Tour | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Nainital family tour (UK-001): Naini Lake, Bhimtal, Sattal, Naukuchiatal with private boat ride, MAP plan, and luxury lakeside resorts.',
        is_featured=True,
        featured_sort_order=20,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text='Naina Devi Temple', sort_order=1),
    ItineraryHighlightNested(text='Eco Cave Gardens', sort_order=2),
    ItineraryHighlightNested(text='Snow View Point via Aerial Ropeway', sort_order=3),
    ItineraryHighlightNested(text='Bhimtal Lake & Island', sort_order=4),
    ItineraryHighlightNested(text='Naukuchiatal Nine-Cornered Lake', sort_order=5),
        ],
        days=[
            _day(
        1,
        'Arrival in Nainital | Welcome to the City of Lakes',
        'Your premium Uttarakhand experience begins as our executive chauffeur welcomes you at Delhi Airport/Railway Station or Kathgodam. Relax in your private premium vehicle as you climb the scenic mountain routes winding past fragrant pine forests. Arrive at your handpicked luxury resort overlooking the valley. After checking in, spend a relaxed evening strolling down Mall Road, indulging in local shopping, and capturing sunset photography points along Naini Lake.',
        [
            'Sightseeing Included: Scenic Kumaon hillside drive, Naini Lake promenade walk, Mall Road exploring',
            'Evening Experience: Welcome note greeting accompanied by a curated fine-dining dinner at the resort restaurant',
            'Overnight Stay: Nainital (Premium / Luxury Lake View Resort)',
            'Meals Included: Welcome Drink & Luxury Dinner',
        ],
    ),
    _day(
        2,
        'Nainital Local Sightseeing | Mystical Lakes, Panoramic Peaks & Heritage Views',
        'Awake to a crisp mountain sunrise and a lavish buffet breakfast. Today, indulge in an intensive Nainital sightseeing tour. Visit the revered Naina Devi Temple on the northern banks of the lake. Explore the fascinating Eco Cave Gardens, a massive favorite for family groups. Later, take an exhilarating aerial ropeway ride to Snow View Point to capture breathtaking landscapes of the snow-clad Himalayan range. Conclude your afternoon with an immersive experience—a private boat cruise on the emerald waters of Naini Lake.',
        [
            'Sightseeing Included: Naina Devi Temple, Eco Cave Gardens, Snow View Point via Aerial Ropeway, Tiffin Top (optional)',
            'Optional Activities: Private guided heritage walk exploring colonial-era structures and old churches of Nainital',
            'Overnight Stay: Nainital (Premium / Luxury Lake View Resort)',
            'Meals Included: Premium Breakfast & Gourmet Dinner',
        ],
    ),
    _day(
        3,
        'Excursion to the Famous Lake District (Bhimtal, Sattal, Naukuchiatal)',
        'After breakfast, set out on a scenic tour of the magnificent lake cluster surrounding Nainital. Drive to Bhimtal, significantly larger than Naini Lake, featuring an island restaurant accessible via boat. Proceed to Sattal, a unique interconnected group of seven freshwater lakes nestled amidst thick oak forests. Finally, visit Naukuchiatal, the lake of nine corners, surrounded by legendary myths and lush terraced fields. Enjoy a serene lakeside lunch experience at a premium boutique cafe.',
        [
            'Sightseeing Included: Bhimtal Lake & Island, Sattal Forest Trails, Naukuchiatal Nine-Cornered Lake view',
            'Evening Experience: Sunset tea session at a scenic photography point overlooking Naukuchiatal valley',
            'Overnight Stay: Nainital (Premium / Luxury Lake View Resort)',
            'Meals Included: Premium Breakfast & Special Themed Farewell Dinner',
        ],
    ),
    _day(
        4,
        'Nainital to Delhi / Departure | Cherishing Unforgettable Mountain Memories',
        'Savor a final sumptuous breakfast while gazing over the morning mist rising off the lake. Check out from your resort as your private luxury transport drives you back down the scenic foothills. Make a brief stop at the beautiful Kainchi Dham Ashram—made famous globally by corporate icons—before continuing your return drive to Delhi Airport or Railway Station. Return home carrying unforgettable memories crafted beautifully by TRAGUIN.',
        [
            'Transfers Included: Private highway drop-off to Delhi or Kathgodam station',
            'Meals Included: Lavish Buffet Breakfast',
        ],
    ),
        ],
        hotels=[
            ItineraryHotelNested(name='The Pavilion Nainital / Balrampur House / similar', location='Nainital', nights_label='03 Nights', category_label='Deluxe', room_type='Deluxe Valley View Room', meal_plan='MAP Plan (Breakfast & Dinner)', stars=4, sort_order=1),
    ItineraryHotelNested(name='The Manu Maharani / Shervani Hilltop / similar', location='Nainital', nights_label='03 Nights', category_label='Premium', room_type='Premium Balcony Room', meal_plan='MAP Plan (Breakfast & Dinner)', stars=4, sort_order=2),
    ItineraryHotelNested(name='The Naini Retreat / WelcomeHeritage Ashdale', location='Nainital', nights_label='03 Nights', category_label='Luxury', room_type='Luxury Lake View Suite', meal_plan='MAP Plan + TRAGUIN Welcome Amenities', stars=5, sort_order=3),
    ItineraryHotelNested(name='The Fern Hillside Resort / Private Luxury Boutique Estate', location='Nainital', nights_label='03 Nights', category_label='Ultra Luxury', room_type='VVIP Panoramic Presidential Suite', meal_plan='Bespoke Signature Menu Plan', stars=5, sort_order=4),
        ],
        inclusions=_uk001_inclusions(),
    )
    return package, itinerary

def _uk001_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text='Premium Stays: 3 Nights in premium handpicked hotels & lakeside resorts', sort_order=1),
        ItineraryInclusionNested(kind="included", text='Luxury Transportation: Private dedicated AC vehicle for all transfers & sightseeing routes', sort_order=2),
        ItineraryInclusionNested(kind="included", text='Curated Meal Plan: Daily premium breakfast and gourmet dinners at hotels', sort_order=3),
        ItineraryInclusionNested(kind="included", text='TRAGUIN Support: 24/7 dedicated guest relationship support on-call', sort_order=4),
        ItineraryInclusionNested(kind="included", text='Welcome Amenities: Personalized custom travel welcome kit upon arrival', sort_order=5),
        ItineraryInclusionNested(kind="included", text='Complimentary Experience: Private family boat ride on the main Naini Lake', sort_order=6),
        ItineraryInclusionNested(kind="excluded", text='Flights or train tickets to and from Delhi / Kathgodam', sort_order=7),
        ItineraryInclusionNested(kind="excluded", text='Entry tickets to ropeways, cave gardens, or local museums', sort_order=8),
        ItineraryInclusionNested(kind="excluded", text='Personal expenses such as laundry, phone calls, drinks, or gratuities', sort_order=9),
        ItineraryInclusionNested(kind="excluded", text='Optional activities, adventure water sports, or independent local guides', sort_order=10),
    ]

def build_uk_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug='uk-002-nainital-mussoorie-majestic-escape',
        destination_id=destination_id,
        title='Nainital • Mussoorie Majestic Escape',
        duration_label='05 Nights / 06 Days',
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=21,
        is_published=True,
        highlights=[
            PackageHighlightNested(text='Nainital (2N) → Mussoorie (3N) with Dhanaulti alpine excursion', sort_order=1),
    PackageHighlightNested(text='Luxury Toyota Innova Crysta with dedicated chauffeur', sort_order=2),
    PackageHighlightNested(text='MAPAI — opulent breakfasts and gourmet dinners', sort_order=3),
    PackageHighlightNested(text='Reserved private boating ticket at Naini Lake', sort_order=4),
    PackageHighlightNested(text='TRAGUIN 24/7 dedicated travel manager on call', sort_order=5),
    PackageHighlightNested(text='Tour code TRG-UK-002 | Serial UK-002', sort_order=6),
        ],
        moods=['Family', 'Luxury', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug='uk-002-nainital-mussoorie-itinerary',
        destination_id=destination_id,
        title='Nainital • Mussoorie Majestic Escape',
        duration_label='05 Nights / 06 Days',
        duration_days=6,
        starting_price=0,
        price_note='On Request (Premium Customized)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Nainital • Bhimtal • Mussoorie • Dhanaulti',
        overview='This custom luxury holiday itinerary offers an exceptional fusion of pristine lake districts and commanding mountain crests. Traveling in the absolute comfort of a private premium AC vehicle managed by an experienced local chauffeur, your family will enjoy unparalleled relaxation. Enhanced with a carefully selected meal plan featuring opulent breakfasts and specialized table dinners, this route highlights the pinnacle of a premium Uttarakhand experience. Your holiday incorporates the exclusive touch of TRAGUIN curated experiences, including VIP sightseeing coordination, expert guide-led stories, and 24/7 dedicated guest support.',
        seo_title='UK-002 | Nainital Mussoorie Majestic Escape | TRAGUIN',
        seo_description='Luxury 05 Nights / 06 Days Uttarakhand family package (UK-002): Nainital lakes, Mussoorie, Kempty Falls, and Dhanaulti Eco Park with Innova Crysta and MAPAI plan.',
        is_featured=True,
        featured_sort_order=21,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text='Bhimtal, Sattal & Naukuchiatal Lakes', sort_order=1),
    ItineraryHighlightNested(text='Kempty Falls', sort_order=2),
    ItineraryHighlightNested(text='Sir George Everest Estate', sort_order=3),
    ItineraryHighlightNested(text='Dhanaulti Eco Park', sort_order=4),
    ItineraryHighlightNested(text='Snow View Point via Ropeway', sort_order=5),
        ],
        days=[
            _day(
        1,
        'Delhi to Nainital Arrival | Journey into the Lake District',
        'Your premium Uttarakhand experience begins with a customized pickup from Delhi Airport or Railway Station in your dedicated private luxury vehicle. Leave the plains behind as your scenic route twists upward into the Kumaon hills, presenting breathtaking landscapes of dense pine forests. Arrive in Nainital, the timeless lake town, and check into your handpicked premium hotel. Spend your evening taking a romantic walk along the vibrant Mall Road, admiring the lights shimmering over the water.',
        [
            'Sightseeing Included: Scenic Kumaon foothills drive, Evening Mall Road walk, Naini Lake view',
            'Evening Experience: Private family stroll along the lakeshore with customized local high-tea',
            'Overnight Stay: Nainital (Premium Premium Lakeside Lake-View Resort)',
            'Meals Included: Welcome Drink & Luxury Dinner',
        ],
    ),
    _day(
        2,
        'Nainital Lake District Tour | Emerald Lakes & Panoramic Himalayan Peaks',
        'Awake to the crisp mountain breeze and enjoy a grand breakfast. Today is dedicated to deep Nainital sightseeing and lake exploration. Visit the sacred Naina Devi Temple on the northern shore of the lake. Next, take a private boat excursion to explore the beautiful surrounding lakes of Bhimtal, Sattal, and Naukuchiatal, each boasting scenic beauty and unique historical legends. In the afternoon, ride the aerial ropeway up to Snow View Point to capture panoramic photographs of the majestic Nanda Devi peak.',
        [
            'Sightseeing Included: Bhimtal, Sattal, Naukuchiatal, Naina Devi Temple, Eco Cave Gardens, Snow View Point',
            'Optional Activities: Kayaking at Sattal or a traditional yacht ride at the elite boat club',
            'Overnight Stay: Nainital (Premium Premium Lakeside Lake-View Resort)',
            'Meals Included: Premium Breakfast & Gourmet Family Dinner',
        ],
    ),
    _day(
        3,
        'Nainital to Mussoorie | Trans-Hill Drive to the Queen of Hill Stations',
        'After a hearty breakfast, check out and embark on a grand trans-hill drive connecting the Kumaon and Garhwal regions. Your journey treats you to iconic attractions along the rolling valleys. Pass through charming villages and forest ridges, capturing the pure spirit of the wilderness. Arrive at Mussoorie, the Queen of Hill Stations, in the late afternoon. Check into your ultra-luxury resort and relax as the sun sets over the Doon Valley, creating a famous winter line phenomenon in the sky.',
        [
            'Sightseeing Included: Scenic inter-hill mountain pass highway drive, Doon Valley sunset views',
            "Evening Experience: Leisurely exploration of Mussoorie's historic Mall Road and colonial libraries",
            'Overnight Stay: Mussoorie (Premium Luxury Mountain Ridge Resort)',
            'Meals Included: Premium Breakfast & Exquisite Buffet Dinner',
        ],
    ),
    _day(
        4,
        'Mussoorie Sightseeing Highlights | Cascading Waterfalls & Colonial Grandeur',
        'Savor an early breakfast before heading out to explore iconic attractions across Mussoorie. First, visit the spectacular Kempty Falls, where mountain water cascades down giant rocks, offering great family photography points. Later, take a peaceful drive to Company Garden and the historic George Everest House—a popular Instagram location that offers breathtaking 360-degree views of snow-capped mountains and green valleys.',
        [
            'Sightseeing Included: Kempty Falls, Sir George Everest Estate, Company Garden, Gun Hill Point via cable car',
            "Optional Activities: A guided heritage walk focused on Mussoorie's colonial-era architecture",
            'Overnight Stay: Mussoorie (Premium Luxury Mountain Ridge Resort)',
            'Meals Included: Premium Breakfast & Curated Royal Dinner',
        ],
    ),
    _day(
        5,
        'Dhanaulti Alpine Excursion | Deodar Forest Sanctuary & Alpine Peace',
        'Today, take a short, refreshing drive to Dhanaulti, a peaceful alpine village located amidst deep deodar, oak, and rhododendron forests. Experience pure serenity inside the Eco Park, where your family can walk along quiet nature trails. Visit the ancient Surkanda Devi Temple for panoramic vistas of the snow-clad central Himalayan peaks. Return to Mussoorie for your final evening, relaxing beside a cozy bonfire at your resort.',
        [
            'Sightseeing Included: Dhanaulti Eco Park, Sukhanda Devi viewpoints, Potato Farm fields',
            'Evening Experience: A special farewell family dinner around a bonfire at your premium resort',
            'Overnight Stay: Mussoorie (Premium Luxury Mountain Ridge Resort)',
            'Meals Included: Premium Breakfast & Farewell Celebration Dinner',
        ],
    ),
    _day(
        6,
        'Mussoorie to Delhi / Departure | Cherishing Unforgettable Family Bonding Moments',
        'Indulge in a final lavish breakfast looking out over the mountain mist. Pack your bags as your private luxury vehicle takes you smoothly down the hills and along the national highway back to New Delhi Airport or Railway Station. Return home carrying a heart filled with shared smiles and unforgettable memories meticulously designed by TRAGUIN.',
        [
            'Transfers Included: Private door-to-door luxury highway drop-off to Delhi',
            'Meals Included: Sumptuous Buffet Breakfast',
        ],
    ),
        ],
        hotels=[
            ItineraryHotelNested(name='The Pavilion / Lake Alpin / similar', location='Nainital', nights_label='02 Nights', category_label='Deluxe', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=1),
    ItineraryHotelNested(name='Hotel Green Castle / similar', location='Mussoorie', nights_label='03 Nights', category_label='Deluxe', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=2),
    ItineraryHotelNested(name='The Manu Maharani / Balrampur House', location='Nainital', nights_label='02 Nights', category_label='Premium', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=3),
    ItineraryHotelNested(name='Sterling Mussoorie / Jaypee Residency', location='Mussoorie', nights_label='03 Nights', category_label='Premium', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=4),
    ItineraryHotelNested(name='The Naini Retreat (Luxury Suite)', location='Nainital', nights_label='02 Nights', category_label='Luxury', meal_plan='Bespoke Custom MAPAI Kit', stars=5, sort_order=5),
    ItineraryHotelNested(name='JW Marriott Walnut Grove Resort', location='Mussoorie', nights_label='03 Nights', category_label='Luxury', meal_plan='Bespoke Custom MAPAI Kit', stars=5, sort_order=6),
    ItineraryHotelNested(name='The Grand Hotel (VVIP Imperial Suite)', location='Nainital', nights_label='02 Nights', category_label='Ultra Luxury', meal_plan='Elite Premium Chef-Curated MAPAI', stars=5, sort_order=7),
    ItineraryHotelNested(name='The Savoy - IHCL SeleQtions', location='Mussoorie', nights_label='03 Nights', category_label='Ultra Luxury', meal_plan='Elite Premium Chef-Curated MAPAI', stars=5, sort_order=8),
        ],
        inclusions=_uk002_inclusions(),
    )
    return package, itinerary

def _uk002_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text='Premium Stays: Luxury accommodations as per selected room options', sort_order=1),
        ItineraryInclusionNested(kind="included", text='Luxury Transportation: Private Innova Crysta for all highway runs & sightseeing', sort_order=2),
        ItineraryInclusionNested(kind="included", text='Curated Meals: Lavish daily breakfasts and fine gourmet dinners (MAPAI)', sort_order=3),
        ItineraryInclusionNested(kind="included", text='TRAGUIN Support: 24/7 dedicated travel manager on call for your family', sort_order=4),
        ItineraryInclusionNested(kind="included", text='Welcome Amenities: Personalized family travel kit, fresh mountain juice, and fruits', sort_order=5),
        ItineraryInclusionNested(kind="included", text='Complimentary Experience: Reserved private boating ticket at Naini Lake', sort_order=6),
        ItineraryInclusionNested(kind="excluded", text='Airfare, train, or interstate flight tickets to New Delhi', sort_order=7),
        ItineraryInclusionNested(kind="excluded", text='Monument entry tickets, boating tokens, camera permissions, or local guides', sort_order=8),
        ItineraryInclusionNested(kind="excluded", text='Personal items such as laundry services, phone charges, or tips', sort_order=9),
        ItineraryInclusionNested(kind="excluded", text='Any insurance, optional activities, or extended detour charges', sort_order=10),
    ]

def build_uk_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug='uk-003-auli-adventure-family-escape',
        destination_id=destination_id,
        title='Auli Adventure Family Escape • Peaks, Meadows & Rivers',
        duration_label='05 Nights / 06 Days',
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=22,
        is_published=True,
        highlights=[
            PackageHighlightNested(text='Rishikesh (1N) → Joshimath/Auli (3N) → Haridwar (1N)', sort_order=1),
    PackageHighlightNested(text='Private luxury Innova Crysta with mountain-certified chauffeur', sort_order=2),
    PackageHighlightNested(text='MAPAI — daily breakfast and gourmet dinners', sort_order=3),
    PackageHighlightNested(text='Complimentary Joshimath-Auli ropeway return tickets', sort_order=4),
    PackageHighlightNested(text='TRAGUIN 24/7 real-time operations coordination', sort_order=5),
    PackageHighlightNested(text='Tour code TRG-UK-003 | Serial UK-003', sort_order=6),
        ],
        moods=['Family', 'Adventure', 'Nature', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug='uk-003-auli-adventure-itinerary',
        destination_id=destination_id,
        title='Auli Adventure Family Escape • Peaks, Meadows & Rivers',
        duration_label='05 Nights / 06 Days',
        duration_days=6,
        starting_price=0,
        price_note='On Request (Bespoke Luxury Customized)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Dehradun • Rishikesh • Joshimath • Auli • Haridwar',
        overview='This custom-designed holiday itinerary caters perfectly to families seeking crisp alpine air, luxury accommodation, and private, unhurried transit across the mountains. Navigating the majestic Alaknanda and Ganga valleys in your private luxury SUV with an experienced mountain chauffeur, your journey ensures total tranquility. Featuring a premium meal plan with daily rich breakfast spreads and curated fine dinners at top local eateries, this route delivers a Premium Uttarakhand Experience. Every moment is accompanied by the signature touch of TRAGUIN curated experiences, including reserved VIP sightseeing, cable-car tickets, and dedicated ground support.',
        seo_title='UK-003 | Auli Adventure Family Escape | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Auli family adventure (UK-003): Rishikesh, Joshimath, Auli ropeway, Gorson Bugyal, and Haridwar with luxury stays and MAPAI plan.',
        is_featured=True,
        featured_sort_order=22,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text='Ganga Aarti at Triveni Ghat', sort_order=1),
    ItineraryHighlightNested(text='Devprayag & Rudraprayag Confluences', sort_order=2),
    ItineraryHighlightNested(text='Auli Gondola Ropeway Ride', sort_order=3),
    ItineraryHighlightNested(text='Gorson Bugyal Alpine Meadows', sort_order=4),
    ItineraryHighlightNested(text='Har Ki Pauri Evening Aarti', sort_order=5),
        ],
        days=[
            _day(
        1,
        'Arrival in Dehradun & Drive to Rishikesh | Welcome to the Land of the Holy Ganges',
        'Your luxury itinerary begins as your private transport chauffeur greets you at Dehradun Airport or Haridwar Station. Relax inside your premium vehicle as you drive into Rishikesh, the global capital of yoga and spiritual adventure. Check into your premium luxury river resort nestled inside the lush foothills. In the evening, witness the emotionally moving Ganga Aarti at Triveni Ghat with reserved family seating, capturing spectacular sunset views over the rushing holy waters.',
        [
            'Sightseeing Included: Ram Jhula, Laxman Jhula pedestrian walk, Triveni Ghat spiritual ceremony',
            'Evening Experience: Traditional riverbank dinner with organic, locally sourced delicacies under the stars',
            'Overnight Stay: Rishikesh (Premium Riverside Luxury Resort)',
            'Meals Included: Welcome Mountain Drink & Luxury Dinner',
        ],
    ),
    _day(
        2,
        'Rishikesh to Joshimath via Scenic Prayags | Journey Along the Sacred Confluences',
        'Awake to the sound of flowing water and enjoy a nutritious breakfast. Begin your ascent towards Joshimath. This scenic route features breathtaking landscapes as you follow the twisting mountain roads parallel to the emerald Alaknanda River. Pause your journey to photograph the iconic river confluences at Devprayag and Rudraprayag, where different rivers merge into a singular, powerful current. Arrive at Joshimath in the evening and relax at your luxury alpine hotel.',
        [
            'Sightseeing Included: Devprayag (Sangam point of Alaknanda & Bhagirathi), Rudraprayag, Narsingh Temple in Joshimath',
            'Optional Activities: Short guided walk through the old local village bazaars of Joshimath',
            'Overnight Stay: Joshimath (Premium High-Altitude Resort)',
            'Meals Included: Premium Breakfast & Mountain Buffet Dinner',
        ],
    ),
    _day(
        3,
        'Joshimath to Auli | Ascending to the Alpine Paradise',
        "Take an unforgettable Asia's longest bi-cable ropeway from Joshimath directly into Auli. As your cabin glides gracefully above magnificent oak forests, witness majestic views of the Nanda Devi peak. Arrive at the high-altitude ski resort and check into your premium luxury chalet. Spend the afternoon strolling along the glistening perimeter of the Auli Artificial Lake—a highly popular Instagram location that mirrors the snowy mountain peaks perfectly.",
        [
            'Sightseeing Included: Auli Gondola Ropeway Ride, Auli Artificial Lake, Snow-capped Panoramic Viewpoints',
            'Evening Experience: Private cozy bonfire evening with hot beverages arranged by TRAGUIN experts',
            'Overnight Stay: Auli (Premium Luxury Ski Resort / Wooden Chalet)',
            'Meals Included: Breakfast & Special Barbecue Dinner',
        ],
    ),
    _day(
        4,
        'Gorson Bugyal Trek & Winter Adventure | Trekking Across the Alpine Meadows',
        'Indulge in a beautiful breakfast with panoramic views. Today, your family can participate in an easy, scenic trek to Gorson Bugyal, a vast expanse of lush alpine meadows surrounded by majestic peaks. During winter, these slopes are blanketed in pure, thick snow, providing fine opportunities for amateur skiing and snowboarding. Capture unforgettable memories and professional family photos with the mighty Himalayas framing your background.',
        [
            'Sightseeing Included: Gorson Bugyal trails, Chattrakund sweet-water lake, Skiing training area',
            'Optional Activities: Professional ski lesson with a certified instructor or premium snow-mobile ride',
            'Overnight Stay: Auli (Premium Luxury Ski Resort / Wooden Chalet)',
            'Meals Included: Premium Breakfast & Authentic Garhwali Buffet Dinner',
        ],
    ),
    _day(
        5,
        'Auli to Haridwar Vista Drive | Returning from the Clouds',
        'Descend from the high ski slopes via ropeway or private drive and settle back into your premium Innova Crysta. Travel smoothly back down the scenic valleys towards Haridwar. Watch the mountain ranges turn back into beautiful plains. Check into your ultra-luxury heritage haveli along the riverbank. Spend your evening witnessing the glowing lamps floating down the sacred waters at Har Ki Pauri during the grand evening Aarti.',
        [
            'Sightseeing Included: Har Ki Pauri Ghat, Local old market street walk, Heritage riverbank temples',
            'Evening Experience: Bespoke VIP seating at Har Ki Pauri for a hassle-free evening ceremony',
            'Overnight Stay: Haridwar / Rishikesh (Premium Luxury Heritage Haveli)',
            'Meals Included: Breakfast & Farewell Premium Dinner',
        ],
    ),
    _day(
        6,
        'Departure from Dehradun / Delhi | Cherishing Memories Beyond Destinations',
        'Enjoy your last breakfast at the luxury heritage hotel. Your private chauffeur will drive you safely back to Dehradun Airport or Haridwar station to board your journey home. Say goodbye to the grand peaks of Uttarakhand, carrying home a heart full of joy, family closeness, and unforgettable memories designed expertly by TRAGUIN.',
        [
            'Transfers Included: Private luxury door-to-door station or airport drop-off',
            'Meals Included: Sumptuous Buffet Breakfast',
        ],
    ),
        ],
        hotels=[
            ItineraryHotelNested(name='Aloha On The Ganges / similar', location='Rishikesh', nights_label='01 Night', category_label='Deluxe', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=1),
    ItineraryHotelNested(name='The Tattva Joshimath / similar', location='Joshimath / Auli', nights_label='03 Nights', category_label='Deluxe', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=2),
    ItineraryHotelNested(name='Regenta Central Haridwar', location='Haridwar', nights_label='01 Night', category_label='Deluxe', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=3),
    ItineraryHotelNested(name='Divine Resort / Lemon Tree', location='Rishikesh', nights_label='01 Night', category_label='Premium', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=4),
    ItineraryHotelNested(name='Clifftop Club Auli / similar', location='Joshimath / Auli', nights_label='03 Nights', category_label='Premium', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=5),
    ItineraryHotelNested(name='Haveli Hari Ganga / similar', location='Haridwar', nights_label='01 Night', category_label='Premium', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=6),
    ItineraryHotelNested(name='Taj Rishikesh Resort & Spa', location='Rishikesh', nights_label='01 Night', category_label='Luxury', meal_plan='MAPAI (Breakfast & Dinner)', stars=5, sort_order=7),
    ItineraryHotelNested(name='The Himalayan High Auli', location='Joshimath / Auli', nights_label='03 Nights', category_label='Luxury', meal_plan='MAPAI (Breakfast & Dinner)', stars=5, sort_order=8),
    ItineraryHotelNested(name='Pilibhit House - IHCL SeleQtions', location='Haridwar', nights_label='01 Night', category_label='Luxury', meal_plan='MAPAI (Breakfast & Dinner)', stars=5, sort_order=9),
    ItineraryHotelNested(name='Ananda In The Himalayas', location='Rishikesh', nights_label='01 Night', category_label='Ultra Luxury', meal_plan='MAPAI (Breakfast & Dinner)', stars=5, sort_order=10),
    ItineraryHotelNested(name='VVIP Custom Luxury Private Ski Chalet', location='Joshimath / Auli', nights_label='03 Nights', category_label='Ultra Luxury', meal_plan='MAPAI (Breakfast & Dinner)', stars=5, sort_order=11),
    ItineraryHotelNested(name='Pilibhit House Luxury Royal Suite', location='Haridwar', nights_label='01 Night', category_label='Ultra Luxury', meal_plan='MAPAI (Breakfast & Dinner)', stars=5, sort_order=12),
        ],
        inclusions=_uk003_inclusions(),
    )
    return package, itinerary

def _uk003_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text='Premium Stays: Luxury accommodations across chosen handpicked hotels', sort_order=1),
        ItineraryInclusionNested(kind="included", text='Luxury Transportation: Chauffeur-driven AC Innova Crysta for all mountain segments', sort_order=2),
        ItineraryInclusionNested(kind="included", text='Curated Meal Plan: Daily hot breakfast and gourmet custom dinners (MAPAI)', sort_order=3),
        ItineraryInclusionNested(kind="included", text='TRAGUIN Support: 24/7 real-time operations coordination and ground desk', sort_order=4),
        ItineraryInclusionNested(kind="included", text='Welcome Amenities: Cold-climate care kit, traditional stoles, and water bottles', sort_order=5),
        ItineraryInclusionNested(kind="included", text='Complimentary Experience: Return cable-car ticket for the Joshimath-Auli ropeway', sort_order=6),
        ItineraryInclusionNested(kind="excluded", text='Airfare, domestic flights, or railway tickets to Uttarakhand', sort_order=7),
        ItineraryInclusionNested(kind="excluded", text='Ski equipment rentals or hiring charges for personal trainers', sort_order=8),
        ItineraryInclusionNested(kind="excluded", text='Personal expenses such as laundry, phone calls, or tips', sort_order=9),
        ItineraryInclusionNested(kind="excluded", text='Any medical, accidental insurance, or unexpected landslide costs', sort_order=10),
    ]

def build_uk_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug='uk-004-kedarnath-special-divine-journey',
        destination_id=destination_id,
        title='Kedarnath Special • A Divine Journey of Devotion & Luxury',
        duration_label='04 Nights / 05 Days',
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=23,
        is_published=True,
        highlights=[
            PackageHighlightNested(text='Guptkashi (2N) → Kedarnath Dham (1N) → Rishikesh (1N)', sort_order=1),
    PackageHighlightNested(text='Private luxury SUV with experienced mountain chauffeur', sort_order=2),
    PackageHighlightNested(text='MAPAI pure vegetarian meals — breakfast and dinner', sort_order=3),
    PackageHighlightNested(text='Priority helicopter coordination and VIP Ganga Aarti seating', sort_order=4),
    PackageHighlightNested(text='TRAGUIN 24/7 priority logistical backup', sort_order=5),
    PackageHighlightNested(text='Tour code TRG-UK-004 | Serial UK-004', sort_order=6),
        ],
        moods=['Spiritual', 'Family', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug='uk-004-kedarnath-itinerary',
        destination_id=destination_id,
        title='Kedarnath Special • A Divine Journey of Devotion & Luxury',
        duration_label='04 Nights / 05 Days',
        duration_days=5,
        starting_price=0,
        price_note='On Request (Premium Customised Pilgrimage)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Dehradun • Guptkashi • Kedarnath Dham • Rishikesh',
        overview='This custom-tailored spiritual package provides a flawless balance of religious devotion, comfort, and elite travel logistics. Travelling in a completely private premium AC vehicle managed by an experienced mountain chauffeur, your family will experience unmatched safety across winding scenic routes. With a carefully structured meal plan highlighting freshly prepared, nourishing vegetarian delicacies, this itinerary delivers a true premium Uttarakhand experience. Every component features the signature touch of TRAGUIN curated experiences, seamlessly handling priority helicopter charter bookings, executive local assistance, and around-the-clock ground support.',
        seo_title='UK-004 | Kedarnath Special Divine Journey | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Kedarnath pilgrimage (UK-004): Guptkashi, Kedarnath Dham, Rishikesh with pure vegetarian MAPAI plan and VIP Ganga Aarti seating.',
        is_featured=True,
        featured_sort_order=23,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text='Devprayag River Confluence', sort_order=1),
    ItineraryHighlightNested(text='Kedarnath Temple Complex', sort_order=2),
    ItineraryHighlightNested(text='Bhairav Nath Temple', sort_order=3),
    ItineraryHighlightNested(text='Ram Jhula & Lakshman Jhula', sort_order=4),
    ItineraryHighlightNested(text='Parmarth Niketan Ganga Aarti', sort_order=5),
        ],
        days=[
            _day(
        1,
        'Arrival in Dehradun & Drive to Guptkashi | Gateway to the Holy Shuttles',
        'Your premium Uttarakhand experience begins as your private chauffeur welcomes you at Dehradun Airport or Haridwar Station. Board your luxury transport vehicle and embark on a spectacularly scenic route along the Ganga and Alaknanda rivers. Pass through historic confluences like Devprayag, where the Bhagirathi and Alaknanda rivers meet to form the holy Ganges. Arrive in the scenic mountain town of Guptkashi, beautifully framed by distant snow-capped peaks. Check into your handpicked premium stay and unwind.',
        [
            'Sightseeing Included: Devprayag river confluence view, Mandakini Valley scenic route',
            'Evening Experience: Private evening visit to the ancient Kashi Vishwanath Temple in Guptkashi',
            'Overnight Stay: Guptkashi / Phata (Premium Luxury Resort / Swiss Cottages)',
            'Meals Included: Welcome Drink & Gourmet Vegetarian Dinner',
        ],
    ),
    _day(
        2,
        'Guptkashi to Kedarnath Dham | Ascending to the Abode of Lord Shiva',
        'An emotionally moving day awaits. After an early breakfast, proceed to the helipad (Phata/Sersi/Guptkashi) for an exclusive helicopter experience curated by TRAGUIN experts (or opt for a private pony/trek from Gaurikund). Soar over breathtaking landscapes and deep alpine gorges before landing at the high-altitude Kedarnath helipad. Walk to the majestic, thousands-of-years-old Kedarnath Temple, surrounded by towering glaciers. Feel the powerful cosmic energy as you join thousands of devotees chanting praises to Lord Shiva.',
        [
            'Sightseeing Included: Kedarnath Temple Complex, Shankracharya Samadhi, Panoramic Himalayan Glaciers',
            'Evening Experience: Witness the intensely spiritual and emotional Evening Aarti at Kedarnath Dham',
            'Overnight Stay: Kedarnath (Premium Premium Guest House / Luxury Tented Camp near Temple)',
            'Meals Included: Breakfast & Warm Simple Vegetarian Dinner',
        ],
    ),
    _day(
        3,
        'Kedarnath Dham to Guptkashi / Rudraprayag | Morning Darshan & Spiritual Grace',
        "Awake before dawn to witness the stunning sight of the sun's first golden rays hitting the snow-capped peaks behind the temple. Attend the morning Abhishek Puja inside the inner sanctum. After receiving holy blessings, make your way back down via helicopter or trek to the base valley. Your private luxury vehicle will receive you and escort you to a premium riverside hotel in Rudraprayag or Guptkashi, allowing your family to rest and recover in absolute comfort.",
        [
            'Sightseeing Included: Morning Temple Darshan, Bhairav Nath Temple walk, Rudraprayag confluence',
            'Optional Activities: Professional landscape and portrait photography against the glacial valleys',
            'Overnight Stay: Rudraprayag / Guptkashi (Premium Handpicked Resort)',
            'Meals Included: Premium Breakfast & Traditional Dinner',
        ],
    ),
    _day(
        4,
        'Guptkashi to Rishikesh | The World Capital of Yoga',
        'Drive down the mountain roads to the peaceful city of Rishikesh, the global capital of Yoga and spirituality. Check into your luxury wellness resort along the riverbank. In the afternoon, explore iconic attractions like Lakshman Jhula and Ram Jhula. As the sun begins to set, proceed to the Parmarth Niketan Ashram for an incredible, immersive experience of the world-famous Ganga Aarti, where rows of oil lamps illuminate the sacred river.',
        [
            'Sightseeing Included: Ram Jhula, Lakshman Jhula area, Beatles Ashram, Parmarth Niketan Ghat',
            'Evening Experience: Reserved seating at the iconic Ganga Aarti ceremony along the riverbanks',
            'Overnight Stay: Rishikesh (Premium Riverside Luxury Resort)',
            'Meals Included: Breakfast & Exquisite Organic Dinner',
        ],
    ),
    _day(
        5,
        'Rishikesh to Dehradun / Departure | Cherishing Faith & Unforgettable Memories',
        'Savor a final peaceful breakfast overlooking the emerald waters of the Ganges. If time permits, enjoy a brief morning yoga or meditation session at your resort. Your private luxury transport will then drive you comfortably to Dehradun Airport or Haridwar Railway Station for your return trip home. Depart carrying a profound sense of inner peace, divine blessings, and unforgettable memories carefully designed by TRAGUIN.',
        [
            'Transfers Included: Private luxury highway drop-off to Airport / Station',
            'Meals Included: Sumptuous Buffet Breakfast',
        ],
    ),
        ],
        hotels=[
            ItineraryHotelNested(name='Monal Resort / Mandakini Resort', location='Guptkashi / Rudraprayag', nights_label='02 Nights', category_label='Deluxe', meal_plan='MAPAI (Pure Vegetarian)', stars=4, sort_order=1),
    ItineraryHotelNested(name='GMVN Premium Camps / Cottages', location='Kedarnath Dham', nights_label='01 Night', category_label='Deluxe', meal_plan='MAPAI (Pure Vegetarian)', stars=4, sort_order=2),
    ItineraryHotelNested(name='EllBee Ganga View / similar', location='Rishikesh', nights_label='01 Night', category_label='Deluxe', meal_plan='MAPAI (Pure Vegetarian)', stars=4, sort_order=3),
    ItineraryHotelNested(name='Villa Rishikesh style / Camp Nirvana', location='Guptkashi / Rudraprayag', nights_label='02 Nights', category_label='Premium', meal_plan='MAPAI (Pure Vegetarian)', stars=4, sort_order=4),
    ItineraryHotelNested(name='Premium Private Annex Executive Rooms', location='Kedarnath Dham', nights_label='01 Night', category_label='Premium', meal_plan='MAPAI (Pure Vegetarian)', stars=4, sort_order=5),
    ItineraryHotelNested(name='Aloha On The Ganges / similar', location='Rishikesh', nights_label='01 Night', category_label='Premium', meal_plan='MAPAI (Pure Vegetarian)', stars=4, sort_order=6),
    ItineraryHotelNested(name='Kedar River Retreat Premium Suites', location='Guptkashi / Rudraprayag', nights_label='02 Nights', category_label='Luxury', meal_plan='MAPAI (Pure Vegetarian)', stars=5, sort_order=7),
    ItineraryHotelNested(name='VVIP Custom Luxury Swiss Tents', location='Kedarnath Dham', nights_label='01 Night', category_label='Luxury', meal_plan='MAPAI (Pure Vegetarian)', stars=5, sort_order=8),
    ItineraryHotelNested(name='Taj Rishikesh / Ananda In The Himalayas', location='Rishikesh', nights_label='01 Night', category_label='Luxury', meal_plan='MAPAI (Pure Vegetarian)', stars=5, sort_order=9),
    ItineraryHotelNested(name='Private Luxury Himalayan Chalet', location='Guptkashi / Rudraprayag', nights_label='02 Nights', category_label='Ultra Luxury', meal_plan='MAPAI (Pure Vegetarian)', stars=5, sort_order=10),
    ItineraryHotelNested(name='Exclusive VVIP Private Cottage Facility', location='Kedarnath Dham', nights_label='01 Night', category_label='Ultra Luxury', meal_plan='MAPAI (Pure Vegetarian)', stars=5, sort_order=11),
    ItineraryHotelNested(name='The Roseate Ganges (Luxury Villa)', location='Rishikesh', nights_label='01 Night', category_label='Ultra Luxury', meal_plan='MAPAI (Pure Vegetarian)', stars=5, sort_order=12),
        ],
        inclusions=_uk004_inclusions(),
    )
    return package, itinerary

def _uk004_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text='Premium Stays: Luxury accommodations as per chosen hotel matrix options', sort_order=1),
        ItineraryInclusionNested(kind="included", text='Luxury Transportation: Private dedicated SUV for all point-to-point travel', sort_order=2),
        ItineraryInclusionNested(kind="included", text='Curated Meal Plan: Daily nutritious vegetarian breakfasts and multi-course dinners', sort_order=3),
        ItineraryInclusionNested(kind="included", text='TRAGUIN Support: 24/7 priority logistical backup and dedicated manager access', sort_order=4),
        ItineraryInclusionNested(kind="included", text='Welcome Amenities: Personalized spiritual kit, holy stoles, and route refreshments', sort_order=5),
        ItineraryInclusionNested(kind="included", text='Complimentary Experience: Reserved VIP seating for the Ganga Aarti in Rishikesh', sort_order=6),
        ItineraryInclusionNested(kind="excluded", text='Flights, train tickets, or helicopter shuttle fares (can be booked extra)', sort_order=7),
        ItineraryInclusionNested(kind="excluded", text='Pony, dolie, or personal porter costs for the mountain trail', sort_order=8),
        ItineraryInclusionNested(kind="excluded", text='Personal ritual offerings, specialized temple puja ticketing, tips', sort_order=9),
        ItineraryInclusionNested(kind="excluded", text='Any travel insurance or medical evacuation costs', sort_order=10),
    ]

def build_uk_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug='uk-005-sacred-do-dham-yatra',
        destination_id=destination_id,
        title='Sacred Do Dham Yatra • Kedarnath & Badrinath Divine Sojourn',
        duration_label='06 Nights / 07 Days',
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=24,
        is_published=True,
        highlights=[
            PackageHighlightNested(text='Rishikesh (2N) → Guptkashi (2N) → Kedarnath/Badrinath (2N)', sort_order=1),
    PackageHighlightNested(text='Private luxury executive vehicle with hilly-terrain chauffeur', sort_order=2),
    PackageHighlightNested(text='MAPAI pure-vegetarian breakfasts and dinners', sort_order=3),
    PackageHighlightNested(text='Priority biometric registration and evening Aarti tokens', sort_order=4),
    PackageHighlightNested(text='TRAGUIN 24/7 specialized pilgrimage concierge desk', sort_order=5),
    PackageHighlightNested(text='Tour code TRG-UK-005 | Serial UK-005', sort_order=6),
        ],
        moods=['Spiritual', 'Family', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug='uk-005-do-dham-itinerary',
        destination_id=destination_id,
        title='Sacred Do Dham Yatra • Kedarnath & Badrinath Divine Sojourn',
        duration_label='06 Nights / 07 Days',
        duration_days=7,
        starting_price=0,
        price_note='On Request (Premium Customised Packages)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Haridwar • Rishikesh • Guptkashi • Kedarnath • Badrinath • Govindghat',
        overview='This custom-tailored sacred route offers an immaculate blend of spiritual elevation, absolute mountain safety, and premium physical comfort. Moving in a dedicated private luxury transport layout driven by experienced hilly-terrain chauffeurs, your family or group will bypass typical pilgrimage stressors. Featuring an optimized premium meal plan that guarantees clean, nutritious vegetarian cuisine (Breakfast & Dinner), this specialized itinerary traces the holiest path of Northern India. Every single operational step carries the unmistakable hallmark of TRAGUIN curated experiences—including prioritized biometric registration support, luxury helipad transfers (optional), and trusted local guide insights.',
        seo_title='UK-005 | Sacred Do Dham Yatra Kedarnath Badrinath | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Do Dham yatra (UK-005): Kedarnath and Badrinath with Guptkashi, Joshimath, Mana Village, and Rishikesh with MAPAI vegetarian plan.',
        is_featured=True,
        featured_sort_order=24,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text='Har Ki Pauri Ganga Aarti', sort_order=1),
    ItineraryHighlightNested(text='Devprayag Sacred Confluence', sort_order=2),
    ItineraryHighlightNested(text='Kedarnath Temple Darshan', sort_order=3),
    ItineraryHighlightNested(text='Badrinath Temple & Tapt Kund', sort_order=4),
    ItineraryHighlightNested(text='Mana Village — Last Indian Village', sort_order=5),
        ],
        days=[
            _day(
        1,
        'Arrival in Haridwar / Rishikesh | Gateway to the Gods',
        'Your premium Uttarakhand experience starts with a warm reception at Dehradun Airport or Haridwar Railway Station by a dedicated private luxury transport coordinator. Transfer directly to your handpicked premium hotel. In the evening, witness the world-famous Ganga Aarti at Har Ki Pauri or Parmarth Niketan. Watch thousands of small floating earthen lamps light up the holy river banks while resonant Vedic chants echo into the evening air—a truly emotional storytelling moment.',
        [
            'Sightseeing Included: Har Ki Pauri, Mansa Devi Temple (via ropeway), Rishikesh Ram Jhula walk',
            'Evening Experience: Reserved seating for the grand evening Ganga Aarti, meticulously managed by TRAGUIN',
            'Overnight Stay: Haridwar / Rishikesh (Premium Luxury Wellness Resort)',
            'Meals Included: Welcome Drink & Satvik Fine-Dining Dinner',
        ],
    ),
    _day(
        2,
        'Haridwar / Rishikesh to Guptkashi | Scenic Mountain Ride Along Holy Confluences',
        'Awake early for a refreshing breakfast and begin your ascent into the scenic beauty of the high mountains. Your private executive car takes you on a winding mountain road alongside the Alaknanda and Mandakini rivers. Pause at Devprayag to capture stunning photographs of the exact spot where Bhagirathi and Alaknanda rivers merge to form the holy Ganga. Arrive in Guptkashi by evening, check into a premium luxury cottage stay, and complete your medical checkups for the upcoming trek.',
        [
            'Sightseeing Included: Devprayag Confluence, Rudraprayag view point, Ardhnarishwar Temple in Guptkashi',
            'Photography Points: Dramatic valley views and massive river bends along the national highway',
            'Overnight Stay: Guptkashi / Phata (Handpicked Luxury Alpine Cottages)',
            'Meals Included: Premium Breakfast & Wholesome Dinner',
        ],
    ),
    _day(
        3,
        'Guptkashi to Kedarnath Dham | The Divine Trek Amidst Snow-Capped Peaks',
        'Drive early to Sonprayag/Gaurikund to begin your journey to Kedarnath Dham. Alternatively, take an exclusive helicopter flight from Phata/Sersi helipads. As you climb higher, experience the raw power of the mountain scenery, surrounded by waterfalls and giant peaks. Upon reaching the holy shrine, feel the intense spiritual vibration of the temple courtyard. Stand in awe before the majestic stone temple backed by the snow-covered Kedarnath peak.',
        [
            'Sightseeing Included: Kedarnath Temple, Bhairav Baba Temple, Adi Shankaracharya Samadhi monument',
            'Optional Activities: Pre-booked VIP darshan slot or a private helicopter transfer (subject to availability)',
            'Overnight Stay: Kedarnath (Premium Selected Guest House / Swiss Camp close to the temple)',
            'Meals Included: Hot local Breakfast & Simple Nourishing Dinner',
        ],
    ),
    _day(
        4,
        'Kedarnath to Guptkashi / Joshimath | Descending the Valley',
        'Wake up to a crisp mountain dawn and participate in the early morning Abhishekam darshan. Afterward, trek down to Gaurikund or board your return helicopter flight back to base. Your premium vehicle awaits to drive you through the lush green forests of Chopta, often called the Mini Switzerland of India. Reach your high-end hotel by late evening and unwind with a relaxing herbal tea service.',
        [
            'Sightseeing Included: Chopta Valley road vistas, Ukhimath winter seat view (en-route)',
            'Evening Experience: Relaxed reflexology foot massage recommendation at your premium stay',
            'Overnight Stay: Joshimath / Pipalkoti (Premium Luxury Swiss Camp or Hotel)',
            'Meals Included: Breakfast & Multi-cuisine Buffet Dinner',
        ],
    ),
    _day(
        5,
        'Joshimath to Badrinath Dham | The Abode of Lord Vishnu',
        'Drive towards Badrinath Dham along the spectacular Joshimath-Badrinath ghat road. Take a refreshing, sacred dip in the natural hot springs of Tapt Kund before entering the brightly painted Badrinath Temple for an afternoon darshan. Later, explore Mana Village—the last Indian village on the Indo-Tibetan border—to see the Vyas Gufa cave, Ganesh Gufa, and the dramatic origins of the Saraswati River.',
        [
            'Sightseeing Included: Badrinath Temple, Tapt Kund, Mana Village, Bhim Pul natural stone bridge',
            'Local Experiences: Sipping hot herbal tea at the legendary Last Indian Tea Shop in Mana',
            'Overnight Stay: Badrinath / Govindghat (Premium Selected Luxury Swiss Tents)',
            'Meals Included: Breakfast & Special Traditional Indian Dinner',
        ],
    ),
    _day(
        6,
        'Badrinath to Rudraprayag / Rishikesh | Return Ride Along Highway Villages',
        'Begin your journey down the mountains after breakfast, traveling along smooth national highways. Stop at Joshimath to visit the ancient Narsingh Temple, the winter seat of Lord Badrinath. Continue your drive past picturesque step-farms and cascading mountain streams. Arrive at your luxury riverside resort in Rishikesh by evening and relax alongside a cozy open-air campfire.',
        [
            'Sightseeing Included: Narsingh Temple, Karnaprayag & Nandprayag river views',
            'Optional Activities: A private yoga and meditation session by the banks of the river Ganga',
            'Overnight Stay: Rishikesh (Premium Luxury River-facing Resort)',
            'Meals Included: Breakfast & Farewell Gala Dinner',
        ],
    ),
    _day(
        7,
        'Departure via Dehradun / Delhi | Cherishing Unforgettable Spiritual Bondings',
        'Enjoy a final morning breakfast looking out over the misty mountain valleys. Your private transport vehicle will drive you comfortably to Dehradun Airport or Haridwar/Delhi Station for your journey home. Return home with your heart filled with divine energy and unforgettable memories meticulously arranged by TRAGUIN.',
        [
            'Transfers Included: Private luxury door-to-door highway drop-off',
            'Meals Included: Sumptuous Buffet Breakfast',
        ],
    ),
        ],
        hotels=[
            ItineraryHotelNested(name='Aloha On The Ganges / similar', location='Rishikesh', nights_label='02 Nights', category_label='Deluxe', meal_plan='MAPAI (Pure Vegetarian)', stars=4, sort_order=1),
    ItineraryHotelNested(name='Camp Nirvana / Hotel Mandakini', location='Guptkashi', nights_label='02 Nights', category_label='Deluxe', meal_plan='MAPAI (Pure Vegetarian)', stars=4, sort_order=2),
    ItineraryHotelNested(name='Premium Government Swiss Camps', location='Kedarnath / Badrinath', nights_label='02 Nights', category_label='Deluxe', meal_plan='MAPAI (Pure Vegetarian)', stars=4, sort_order=3),
    ItineraryHotelNested(name='Divine Resort / Lemon Tree Premier', location='Rishikesh', nights_label='02 Nights', category_label='Premium', meal_plan='MAPAI (Pure Vegetarian)', stars=4, sort_order=4),
    ItineraryHotelNested(name='Villa Kedarya / Kedar River Retreat', location='Guptkashi', nights_label='02 Nights', category_label='Premium', meal_plan='MAPAI (Pure Vegetarian)', stars=4, sort_order=5),
    ItineraryHotelNested(name='Sarovar Portico Badrinath / similar', location='Kedarnath / Badrinath', nights_label='02 Nights', category_label='Premium', meal_plan='MAPAI (Pure Vegetarian)', stars=4, sort_order=6),
    ItineraryHotelNested(name='Taj Rishikesh Resort / The Roseate Ganges', location='Rishikesh', nights_label='02 Nights', category_label='Luxury', meal_plan='MAPAI (Pure Vegetarian)', stars=5, sort_order=7),
    ItineraryHotelNested(name='Luxury Shivalik Alpine Cottages', location='Guptkashi', nights_label='02 Nights', category_label='Luxury', meal_plan='MAPAI (Pure Vegetarian)', stars=5, sort_order=8),
    ItineraryHotelNested(name='Elite Private VVIP Cottages', location='Kedarnath / Badrinath', nights_label='02 Nights', category_label='Luxury', meal_plan='MAPAI (Pure Vegetarian)', stars=5, sort_order=9),
    ItineraryHotelNested(name='Ananda In The Himalayas (Luxury Suite)', location='Rishikesh', nights_label='02 Nights', category_label='Ultra Luxury', meal_plan='MAPAI (Pure Vegetarian)', stars=5, sort_order=10),
    ItineraryHotelNested(name='Bespoke Custom Helipad Resort Private Suite', location='Guptkashi', nights_label='02 Nights', category_label='Ultra Luxury', meal_plan='MAPAI (Pure Vegetarian)', stars=5, sort_order=11),
    ItineraryHotelNested(name='Premium Private Glamping Retreats', location='Kedarnath / Badrinath', nights_label='02 Nights', category_label='Ultra Luxury', meal_plan='MAPAI (Pure Vegetarian)', stars=5, sort_order=12),
        ],
        inclusions=_uk005_inclusions(),
    )
    return package, itinerary

def _uk005_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text='Premium Stays: Luxury accommodations as per chosen tier', sort_order=1),
        ItineraryInclusionNested(kind="included", text='Luxury Transportation: Chauffeur-driven AC executive car for mountain sectors', sort_order=2),
        ItineraryInclusionNested(kind="included", text='Curated Meal Plan: Daily pure-vegetarian buffet breakfast and dinner (MAPAI)', sort_order=3),
        ItineraryInclusionNested(kind="included", text='TRAGUIN Support: 24/7 specialized pilgrimage concierge desk line', sort_order=4),
        ItineraryInclusionNested(kind="included", text='Welcome Amenities: Specialized custom travel kit with holy dry-fruits on arrival', sort_order=5),
        ItineraryInclusionNested(kind="included", text='Complimentary Experience: Priority biometric registration pass and evening Aarti tokens', sort_order=6),
        ItineraryInclusionNested(kind="excluded", text='Flights or long-distance train tickets to Dehradun / Delhi', sort_order=7),
        ItineraryInclusionNested(kind="excluded", text='Helicopter tickets, pony rides, or dolis for the trek segment', sort_order=8),
        ItineraryInclusionNested(kind="excluded", text='Personal expenses such as laundry, phone calls, or tips', sort_order=9),
        ItineraryInclusionNested(kind="excluded", text='Any monument entry tickets or custom temple donation receipts', sort_order=10),
    ]

def build_uk_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug='uk-006-char-dham-yatra',
        destination_id=destination_id,
        title='Char Dham Yatra • Absolute Spiritual Awakening',
        duration_label='10 Nights / 11 Days',
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=25,
        is_published=True,
        highlights=[
            PackageHighlightNested(text='Haridwar/Rishikesh (2N) → Barkot/Uttarkashi (4N) → Guptkashi/Badrinath (4N)', sort_order=1),
    PackageHighlightNested(text='Private high-clearance luxury vehicle with hill-experienced chauffeurs', sort_order=2),
    PackageHighlightNested(text='Premium MAPAI pure vegetarian breakfasts and dinners', sort_order=3),
    PackageHighlightNested(text='Exclusive reserved seating for Haridwar Ganga Aarti', sort_order=4),
    PackageHighlightNested(text='TRAGUIN 24/7 round-the-clock ground assistance marshals', sort_order=5),
    PackageHighlightNested(text='Tour code TRG-UK-006 | Serial UK-006', sort_order=6),
        ],
        moods=['Spiritual', 'Family', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug='uk-006-char-dham-itinerary',
        destination_id=destination_id,
        title='Char Dham Yatra • Absolute Spiritual Awakening',
        duration_label='10 Nights / 11 Days',
        duration_days=11,
        starting_price=0,
        price_note='On Request (Premium Customised Pilgrimage)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Haridwar • Barkot • Yamunotri • Gangotri • Kedarnath • Badrinath • Rishikesh',
        overview='This elite 10 Nights / 11 Days itinerary offers a meticulously balanced journey through the four sacred abodes of Uttarakhand—Yamunotri, Gangotri, Kedarnath, and Badrinath. Traveling in a customized, private luxury transportation vehicle with highly skilled mountain marshals, your safety and absolute relaxation remain our highest priority. Featuring a specialized meal plan consisting of nourishing, freshly prepared pure vegetarian breakfasts and dinners, this journey represents the finest premium Uttarakhand experience available. Every step of your yatra includes signature TRAGUIN curated experiences, offering hassle-free registration, helicopter/palki coordination assistance, and around-the-clock bespoke ground support.',
        seo_title='UK-006 | Char Dham Yatra Uttarakhand | TRAGUIN',
        seo_description='Premium 10 Nights / 11 Days Char Dham yatra (UK-006): Yamunotri, Gangotri, Kedarnath, Badrinath with luxury stays, MAPAI vegetarian plan, and VIP Ganga Aarti seating.',
        is_featured=True,
        featured_sort_order=25,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text='Har Ki Pauri Ganga Aarti', sort_order=1),
    ItineraryHighlightNested(text='Yamunotri Temple & Surya Kund', sort_order=2),
    ItineraryHighlightNested(text='Gangotri Temple & Harsil Valley', sort_order=3),
    ItineraryHighlightNested(text='Kedarnath Jyotirlinga Darshan', sort_order=4),
    ItineraryHighlightNested(text='Badrinath Temple & Mana Village', sort_order=5),
        ],
        days=[
            _day(
        1,
        'Arrival in Haridwar | Gateway to the Gods',
        'Your premium Uttarakhand experience commences as you are received at New Delhi Airport or Dehradun Airport by your private luxury transport chauffeur. Enjoy a smooth drive to Haridwar, the historic gateway to Devbhoomi. Check into your handpicked premium hotel along the Ganges. After relaxing, step out for an exclusive evening experience at Har Ki Pauri to witness the world-renowned evening Ganga Aarti ceremony, where thousands of oil lamps reflect beautifully on the holy river.',
        [
            'Sightseeing Included: Har Ki Pauri, Mansa Devi Temple (via private cable car), evening spiritual walks',
            'Evening Experience: Reserved seating for the grand Aarti ceremony managed by TRAGUIN experts',
            'Overnight Stay: Haridwar (Premium Riverside Luxury Hotel)',
            'Meals Included: Welcome Divine Drink & Luxury Dinner',
        ],
    ),
    _day(
        2,
        'Haridwar to Barkot | Scenic Mountain Ascent to the Shivalik Foothills',
        'Awake to the chime of temple bells and enjoy a lavish breakfast. Board your premium luxury vehicle for a scenic drive toward Barkot via Dehradun and the queen of hills, Mussoorie. En route, pause at the majestic Kempty Falls for photography points and a refreshing break. As you ascend higher, notice the breathtaking landscapes change into dense pine forests and snow-tipped alpine views. Arrive at your cozy, handpicked luxury cottage resort in Barkot.',
        [
            'Sightseeing Included: Kempty Falls, Mussoorie bypass ridge, Yamuna River valley drive',
            'Optional Activities: Short nature walk around the apple orchards surrounding your luxury cottages',
            'Overnight Stay: Barkot / Janki Chatti outskirts (Premium Luxury Cottages)',
            'Meals Included: Premium Breakfast & Organic Satvik Dinner',
        ],
    ),
    _day(
        3,
        'Barkot to Yamunotri Excursion | The First Abode',
        'Depart before sunrise to Janki Chatti, the launchpad for your holy trek to Yamunotri (6 km). TRAGUIN can arrange a premium pony or palki service for an effortless journey. Arrive at the holy shrine of Yamunotri against a dramatic backdrop of rugged cliffs. Cook rice in the boiling waters of Surya Kund as a sacred offering, take a holy dip in Jamunabai Kund, and enjoy VIP Darshan of Goddess Yamuna. Return to Barkot late in the afternoon to rest your muscles.',
        [
            'Sightseeing Included: Yamunotri Temple, Surya Kund thermal spring, Divya Shila rock altar',
            'Evening Experience: Foot reflexology massage service pre-arranged at your luxury cottage resort',
            'Overnight Stay: Barkot / Janki Chatti outskirts (Premium Luxury Cottages)',
            'Meals Included: Nourishing Breakfast & Hearty Himalayan Dinner',
        ],
    ),
    _day(
        4,
        'Barkot to Uttarkashi | Journey Along the Bhagirathi',
        'Enjoy a relaxed breakfast before packing your bags for a gorgeous journey to Uttarkashi, situated on the banks of the pristine Bhagirathi River. The drive features scenic beauty, passing through tunnels and riverside paths. Upon arrival, check into your premium luxury riverfront hotel. In the evening, visit the historic Kashi Vishwanath Temple, famous for its massive, enigmatic copper trident embedded deep into the earth.',
        [
            'Sightseeing Included: Kashi Vishwanath Temple, Shakti Temple, Bhagirathi Riverfront ghats',
            'Photography Points: The suspension bridge over Bhagirathi, stunning mountain reflections at sunset',
            'Overnight Stay: Uttarkashi (Premium Valley View Luxury Resort)',
            'Meals Included: Breakfast & Exquisite Vegetarian Buffet Dinner',
        ],
    ),
    _day(
        5,
        'Uttarkashi to Gangotri Excursion | The Second Abode',
        'Today, travel up the spectacular Bhagirathi Valley to Gangotri. Pass through Harsil, a hidden paradise famous for apple orchards and popular Instagram locations. Arrive at the iconic white granite Gangotri Temple, surrounded by towering deodar and cedar forests. Take part in the holy rituals on the banks of the Bhagirathi, explore the submerged rock lingam where Lord Shiva caught the river in his locks, and head back to Uttarkashi in your luxury transport.',
        [
            'Sightseeing Included: Gangotri Temple, Bhagirathi River stone bank, Harsil Valley apple estates',
            'Optional Activities: Sampling freshly baked local Himachali apple turnover desserts in Harsil village',
            'Overnight Stay: Uttarkashi (Premium Valley View Luxury Resort)',
            'Meals Included: Early Breakfast & Warm Signature Comfort Dinner',
        ],
    ),
    _day(
        6,
        'Uttarkashi to Guptkashi | Crossing the Sacred Valley Ridges',
        'Set off on a long, visually stunning transit day across the heart of the Garhwal hills toward Guptkashi. Your route winds around lush green terraced mountains with vistas of the Mandakini River. Pass through serene mountain towns and glimpse the historic Tehri Dam reservoir. Arrive at your luxury Swiss glamping tents or premium resort in Guptkashi, where a medical status check-up is organized to prepare your family for the upcoming Kedarnath journey.',
        [
            'Sightseeing Included: Tehri Dam overview points, Mandakini Valley convergence panoramas',
            'Evening Experience: Visit the ancient Ardhanarishwar Temple in Guptkashi for private peaceful meditation',
            'Overnight Stay: Guptkashi / Phata (Premium Luxury Resort / Premium Glamping)',
            'Meals Included: Breakfast & Nutritious Multi-course Dinner',
        ],
    ),
    _day(
        7,
        'Guptkashi to Kedarnath | The Third Abode',
        'Today marks the apex of your spiritual immersion. Transfer to Phata or Sirsi helipad for an elite helicopter flight directly to Kedarnath, skipping the arduous 18 km trek. Walk to the majestic 8th-century Kedarnath Temple, standing proud in front of the snow-clad Kedarnath peak. Feel the deep spiritual energy as you enter the temple for an intimate darshan. In the evening, witness the legendary night temple ritual when the mountain air echoes with ancient chants.',
        [
            'Sightseeing Included: Kedarnath Jyotirlinga, Bhairav Nath Temple trek path, Shankaracharya Samadhi',
            'Immersive Experiences: Experiencing the majestic sunset glow casting gold over the snow peaks behind the shrine',
            'Overnight Stay: Kedarnath (Premium Selected Guest House / Swiss Camps near the shrine)',
            'Meals Included: Breakfast & Warm Freshly Prepared local Dinner',
        ],
    ),
    _day(
        8,
        'Kedarnath to Guptkashi / Rudraprayag | Return Flyback & Comfort Resort Relaxation',
        'Wake up early for a rare morning darshan of the deity draped in fresh Himalayan snow-melt waters. Board your scheduled helicopter flight back to the base station. Your private luxury transportation vehicle will be waiting to take you down to a lower altitude resort in Rudraprayag. Unwind and relax after your high-altitude journey, enjoying the luxury amenities and pristine mountain views.',
        [
            'Sightseeing Included: Helicopter return flyback, Rudraprayag Sangam (Confluence of Alaknanda & Mandakini)',
            'Evening Experience: Relaxing beside a private evening bonfire arranged on the resort lawn',
            'Overnight Stay: Rudraprayag / Guptkashi (Premium Luxury Riverside Resort)',
            'Meals Included: Breakfast & Premium Global Buffet Dinner',
        ],
    ),
    _day(
        9,
        'Rudraprayag to Badrinath | The Fourth Abode',
        'Drive through Joshimath along the spectacular Alaknanda River to Badrinath, the final temple of your Char Dham journey. Check into your premium luxury hotel. After a short rest, take a refreshing dip in the hot sulfur waters of Tapt Kund before stepping into the colorfully painted Badrinath Temple for an exclusive VIP entry experience. Later, explore Mana Village, the last Indian village before the Tibetan border, to see the historic Vyas Cave where the Mahabharata was transcribed.',
        [
            'Sightseeing Included: Badrinath Temple, Tapt Kund, Mana Village, Vyas Cave, Saraswati River Origin bridge',
            'Evening Experience: Reserved access to the special evening Kapoor Aarti inside the inner sanctum',
            'Overnight Stay: Badrinath (Premium Selected Luxury Stay / Sarovar Portico style)',
            'Meals Included: Breakfast & Royal Satvik Vegetarian Dinner',
        ],
    ),
    _day(
        10,
        'Badrinath to Rishikesh | Yoga Capital of the World',
        'After breakfast, enjoy a pleasant drive down the hills to Rishikesh, the world capital of Yoga and spiritual rejuvenation. Check into your luxury wellness spa resort along the riverbank. Spend your afternoon visiting the iconic attractions of Lakshman Jhula and Ram Jhula, followed by an elegant farewell walk along the serene white-sand beaches of the upper Ganges.',
        [
            'Sightseeing Included: Ram Jhula, Lakshman Jhula suspension points, Beatles Ashram architecture',
            'Optional Activities: Private evening yoga and sound-healing meditation session at the wellness resort',
            'Overnight Stay: Rishikesh (Premium Luxury Wellness Spa Resort)',
            'Meals Included: Breakfast & Farewell Premium Gourmet Dinner',
        ],
    ),
    _day(
        11,
        'Rishikesh to Delhi / Departure | Return with Holy Blessings',
        'Indulge in a final morning breakfast overlooking the peaceful flowing waters of the Ganges. Your private luxury transportation vehicle will pick you up for a smooth highway drive back to New Delhi Airport or Railway Station. Return home carrying sacred blessings, deep peace, and unforgettable memories from your premium pilgrimage expertly organized by TRAGUIN.',
        [
            'Transfers Included: Private door-to-door luxury highway transfer back to Delhi',
            'Meals Included: Sumptuous Buffet Breakfast',
        ],
    ),
        ],
        hotels=[
            ItineraryHotelNested(name='Regenta Central / Lemon Tree', location='Haridwar / Rishikesh', nights_label='02 Nights', category_label='Deluxe', meal_plan='Premium MAPAI (Pure Vegetarian)', stars=4, sort_order=1),
    ItineraryHotelNested(name='Barkot Luxury Camps / Shivlinga', location='Barkot / Uttarkashi', nights_label='04 Nights', category_label='Deluxe', meal_plan='Premium MAPAI (Pure Vegetarian)', stars=4, sort_order=2),
    ItineraryHotelNested(name='Chhangani Resort / New Snow Crest', location='Guptkashi / Badrinath', nights_label='04 Nights', category_label='Deluxe', meal_plan='Premium MAPAI (Pure Vegetarian)', stars=4, sort_order=3),
    ItineraryHotelNested(name='Pilibhit House / Aloha On Ganges', location='Haridwar / Rishikesh', nights_label='02 Nights', category_label='Premium', meal_plan='Premium MAPAI (Pure Vegetarian)', stars=4, sort_order=4),
    ItineraryHotelNested(name='Camp Nirvana / Himalayan Eco Lodges', location='Barkot / Uttarkashi', nights_label='04 Nights', category_label='Premium', meal_plan='Premium MAPAI (Pure Vegetarian)', stars=4, sort_order=5),
    ItineraryHotelNested(name='Villa Kedarnath / Sarovar Portico', location='Guptkashi / Badrinath', nights_label='04 Nights', category_label='Premium', meal_plan='Premium MAPAI (Pure Vegetarian)', stars=4, sort_order=6),
    ItineraryHotelNested(name='Taj Rishikesh Resort & Spa', location='Haridwar / Rishikesh', nights_label='02 Nights', category_label='Luxury', meal_plan='Premium MAPAI (Pure Vegetarian)', stars=5, sort_order=7),
    ItineraryHotelNested(name='Monal Resort Premium Deluxe Suites', location='Barkot / Uttarkashi', nights_label='04 Nights', category_label='Luxury', meal_plan='Premium MAPAI (Pure Vegetarian)', stars=5, sort_order=8),
    ItineraryHotelNested(name='The Kedar Camp Resort Luxury Cottages', location='Guptkashi / Badrinath', nights_label='04 Nights', category_label='Luxury', meal_plan='Premium MAPAI (Pure Vegetarian)', stars=5, sort_order=9),
    ItineraryHotelNested(name='Ananda In The Himalayas (Palace Suite)', location='Haridwar / Rishikesh', nights_label='02 Nights', category_label='Ultra Luxury', meal_plan='Premium MAPAI (Pure Vegetarian)', stars=5, sort_order=10),
    ItineraryHotelNested(name='VVIP Custom Private Glamping Suites', location='Barkot / Uttarkashi', nights_label='04 Nights', category_label='Ultra Luxury', meal_plan='Premium MAPAI (Pure Vegetarian)', stars=5, sort_order=11),
    ItineraryHotelNested(name='Bespoke Private Heli-Chalet Retainers', location='Guptkashi / Badrinath', nights_label='04 Nights', category_label='Ultra Luxury', meal_plan='Premium MAPAI (Pure Vegetarian)', stars=5, sort_order=12),
        ],
        inclusions=_uk006_inclusions(),
    )
    return package, itinerary

def _uk006_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text='Premium Stays: 10 Nights in handpicked properties and premium cottages', sort_order=1),
        ItineraryInclusionNested(kind="included", text='Luxury Transportation: Private dedicated high-clearance vehicle for mountain roads', sort_order=2),
        ItineraryInclusionNested(kind="included", text='Curated Meal Plan: Nourishing, pure vegetarian daily breakfast and dinners', sort_order=3),
        ItineraryInclusionNested(kind="included", text='TRAGUIN Support: 24/7 round-the-clock ground assistance marshals on-site', sort_order=4),
        ItineraryInclusionNested(kind="included", text='Welcome Amenities: Customized family biometric card kit and medical check coordination', sort_order=5),
        ItineraryInclusionNested(kind="included", text='Complimentary Experience: Exclusive reserved seating tickets for Haridwar Ganga Aarti', sort_order=6),
        ItineraryInclusionNested(kind="excluded", text='Flights or long-distance trains to/from New Delhi', sort_order=7),
        ItineraryInclusionNested(kind="excluded", text='Helicopter shuttle tickets or mule/palki rental fees', sort_order=8),
        ItineraryInclusionNested(kind="excluded", text='Personal expenses, laundry, temple puja offerings, tips', sort_order=9),
        ItineraryInclusionNested(kind="excluded", text='Any insurance cover or extra medical hospitalization bills', sort_order=10),
    ]

def build_uk_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug='uk-007-romantic-hills-honeymoon-escape',
        destination_id=destination_id,
        title='Romantic Hills • A Sublime Luxury Honeymoon Escape',
        duration_label='05 Nights / 06 Days',
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=26,
        is_published=True,
        highlights=[
            PackageHighlightNested(text='Mussoorie (3N) → Rishikesh (2N) with Dhanaulti excursion', sort_order=1),
    PackageHighlightNested(text='Private chauffeur-driven luxury sedan for all sightseeing', sort_order=2),
    PackageHighlightNested(text='MAPAI — lavish breakfasts and gourmet thematic dinners', sort_order=3),
    PackageHighlightNested(text='Honeymoon floral layout, chocolates, and fruit basket', sort_order=4),
    PackageHighlightNested(text='TRAGUIN 24/7 dedicated guest relations manager', sort_order=5),
    PackageHighlightNested(text='Tour code TRG-UK-007 | Serial UK-007', sort_order=6),
        ],
        moods=['Romantic', 'Luxury', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug='uk-007-romantic-hills-itinerary',
        destination_id=destination_id,
        title='Romantic Hills • A Sublime Luxury Honeymoon Escape',
        duration_label='05 Nights / 06 Days',
        duration_days=6,
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Mussoorie • Dhanaulti • Rishikesh • Haridwar',
        overview='This custom-tailored luxury proposal offers an exquisite blend of misty mountain ranges, emerald lakes, dense oak forests, and soulful riverside luxury. Traveling in a dedicated premium private vehicle with a professional tourist chauffeur, you will discover the absolute best of the region. Complete with a curated luxury meal plan containing sumptuous breakfasts and intimate candlelit dinners, this route represents the definitive premium Uttarakhand experience. Your journey is elevated by a specialized TRAGUIN curated experience note, ensuring priority access, signature honeymoon amenities, and round-the-clock bespoke support.',
        seo_title='UK-007 | Romantic Hills Honeymoon Escape | TRAGUIN',
        seo_description='Luxury 05 Nights / 06 Days Uttarakhand honeymoon (UK-007): Mussoorie, Dhanaulti, Rishikesh, and Haridwar with candlelit dinners, MAPAI plan, and private Triveni Ghat Aarti seating.',
        is_featured=True,
        featured_sort_order=26,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text='Kempty Falls & Lal Tibba Viewpoint', sort_order=1),
    ItineraryHighlightNested(text='Gun Hill Cable Car', sort_order=2),
    ItineraryHighlightNested(text='Dhanaulti Eco Park', sort_order=3),
    ItineraryHighlightNested(text='Triveni Ghat Ganga Aarti', sort_order=4),
    ItineraryHighlightNested(text='Beatles Ashram', sort_order=5),
        ],
        days=[
            _day(
        1,
        'Arrival in Dehradun to Mussoorie | Welcome to the Queen of Hills',
        'Your premium Uttarakhand experience begins as you touch down at Dehradun Airport or arrive at the railway station. A private luxury transport vehicle waits to receive you with refreshing welcome amenities. Begin your scenic ascent up the winding mountain roads towards Mussoorie. Check into your handpicked premium luxury resort boasting majestic valley views. Spend a beautifully relaxed evening exploring the colonial lanes of Mall Road hand-in-hand, sampling local pastries, and capturing romantic sunset photography points.',
        [
            "Sightseeing Included: Scenic Dehradun-Mussoorie route, Mussoorie Mall Road heritage stroll, Camel's Back Road",
            'Evening Experience: Honeymoon special cake cutting ceremony and welcome drinks at your private resort terrace',
            'Overnight Stay: Mussoorie (Premium / Luxury Resort with Valley View Balcony)',
            'Meals Included: Welcome Drink & Gourmet Dinner',
        ],
    ),
    _day(
        2,
        'Mussoorie Sightseeing Experiences | Misty Waterfalls & Highest Peaks of Romance',
        'Wake up to a pristine mountain sunrise over the Himalayas. Today, enjoy a fully guided Mussoorie sightseeing tour. Head towards the cascading waters of Kempty Falls for a refreshing morning experience. Later, ascend to Lal Tibba, the highest peak in Mussoorie, offering breathtaking landscapes of snow-capped Himalayan peaks through a telescope. Conclude your afternoon at the historic Company Garden and take a romantic cable car ride up to Gun Hill for an unmatched view of the sunset.',
        [
            'Sightseeing Included: Kempty Falls, Lal Tibba Viewpoint, Gun Hill Cable Car, Company Garden, Mussoorie Lake',
            'Optional Activities: Private professional couple photography session amidst the alpine settings',
            'Overnight Stay: Mussoorie (Premium / Luxury Resort)',
            'Meals Included: Premium Breakfast & Romantic Candlelit Dinner',
        ],
    ),
    _day(
        3,
        'Excursion to Dhanaulti Meadows | Pristine Alpine Woods & Tranquil Isolation',
        'Depart after breakfast for an exquisite day excursion to Dhanaulti, a peaceful haven surrounded by dense eco-parks of oak, pine, and deodar trees. Walk down the serene paths of Eco Park, experiencing pure mountain silence and natural scenic beauty. Visit the Surkanda Devi temple for panoramic mountain views before returning to Mussoorie in the evening for an intimate dinner.',
        [
            'Sightseeing Included: Dhanaulti Eco Park, Amber and Twin Eco Forests, Himalayan viewpoints',
            'Evening Experience: Warm mountain tea and local snacks at a rustic hillside café curated by TRAGUIN experts',
            'Overnight Stay: Mussoorie (Premium / Luxury Resort)',
            'Meals Included: Premium Breakfast & Dinner',
        ],
    ),
    _day(
        4,
        'Mussoorie to Rishikesh | Yoga Capital of the World',
        'Drive down the picturesque hills towards Rishikesh, the world-renowned capital of spiritual wellness and riverside charm. Check into your luxury riverside resort. In the afternoon, cross the iconic suspension bridges of Lakshman Jhula and Ram Jhula, visiting historic ashrams and vibrant local markets. As dusk sets, head to Triveni Ghat for an emotionally moving, private-seating Ganga Aarti experience where thousands of oil lamps float beautifully upon the river.',
        [
            'Sightseeing Included: Ram Jhula, Lakshman Jhula, Gita Bhawan, Triveni Ghat Ganga Aarti',
            'Evening Experience: Reserved luxury seating for the grand evening musical prayer ceremony at the Holy Ganges',
            'Overnight Stay: Rishikesh (Luxury Riverside Spa Resort)',
            'Meals Included: Premium Breakfast & Elaborate Organic Dinner Buffet',
        ],
    ),
    _day(
        5,
        'Rishikesh Immersive Experiences | Adventure, Cafe Culture & Emerald Waters',
        "Spend a magnificent day exploring the diverse culture of Rishikesh. Start your morning with a complimentary couple's meditation or yoga session at the resort. For adventure enthusiasts, an optional premium white-water rafting experience or a cliff-jumping session can be organized. In the afternoon, explore the famous Beatles Ashram, a highly popular Instagram location filled with beautiful murals and tranquil ruins.",
        [
            'Sightseeing Included: Beatles Ashram, Local lifestyle cafes, Shivananda Ashram paths',
            'Optional Activities: White-water river rafting under expert safety guidance, Bungee jumping',
            'Overnight Stay: Rishikesh (Luxury Riverside Spa Resort)',
            'Meals Included: Premium Breakfast & Farewell Special Dinner',
        ],
    ),
    _day(
        6,
        'Rishikesh to Dehradun / Departure | Cherishing Unforgettable Memories for a Lifetime',
        'Indulge in a final lavish breakfast at your premium resort. Enjoy a serene morning look at the emerald waters of the Ganges. Your private luxury transport will escort you safely back to Dehradun Airport or Railway Station for your onward journey. Return home carrying a heart filled with deep love and unforgettable memories meticulously designed by TRAGUIN.',
        [
            'Transfers Included: Private luxury door-to-door departure transfer',
            'Meals Included: Sumptuous Buffet Breakfast',
        ],
    ),
        ],
        hotels=[
            ItineraryHotelNested(name='Golden Tulip / Hotel Horizon / similar', location='Mussoorie', nights_label='03 Nights', category_label='Deluxe', room_type='Deluxe Valley View Room', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=1),
    ItineraryHotelNested(name='EllBee Ganga View / similar', location='Rishikesh', nights_label='02 Nights', category_label='Deluxe', room_type='Deluxe Room', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=2),
    ItineraryHotelNested(name='Jaypee Residency Manor / Welcomhotel', location='Mussoorie', nights_label='03 Nights', category_label='Premium', room_type='Premium Balcony Room', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=3),
    ItineraryHotelNested(name='Aloha On The Ganges / similar', location='Rishikesh', nights_label='02 Nights', category_label='Premium', room_type='Premium Room', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=4),
    ItineraryHotelNested(name='The Savoy (IHCL SeleQtions) / JW Marriott', location='Mussoorie', nights_label='03 Nights', category_label='Luxury', room_type='Luxury Executive Valley Suite', meal_plan='MAPAI + Honeymoon Kit', stars=5, sort_order=5),
    ItineraryHotelNested(name='Taj Rishikesh Resort & Spa / similar', location='Rishikesh', nights_label='02 Nights', category_label='Luxury', room_type='Luxury River View Suite', meal_plan='MAPAI + Spa Privilege', stars=5, sort_order=6),
    ItineraryHotelNested(name='The Grand Orchid Luxury Private Villa Suite', location='Mussoorie', nights_label='03 Nights', category_label='Ultra Luxury', room_type='VVIP Royal Presidential Suite', meal_plan='Bespoke Royal MAPAI', stars=5, sort_order=7),
    ItineraryHotelNested(name='Ananda In The Himalayas (Palace Suite)', location='Rishikesh', nights_label='02 Nights', category_label='Ultra Luxury', room_type='Palace Suite', meal_plan='Bespoke Royal Concierge MAPAI', stars=5, sort_order=8),
        ],
        inclusions=_uk007_inclusions(),
    )
    return package, itinerary

def _uk007_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text='Premium Accommodation: Handpicked romantic hotels as per your selected tier', sort_order=1),
        ItineraryInclusionNested(kind="included", text='Luxury Transportation: Private chauffeur-driven sedan for all sightseeing', sort_order=2),
        ItineraryInclusionNested(kind="included", text='Curated Meal Plan: Lavish daily breakfast and gourmet thematic dinners', sort_order=3),
        ItineraryInclusionNested(kind="included", text='TRAGUIN Support: 24/7 dedicated guest relations manager on active call', sort_order=4),
        ItineraryInclusionNested(kind="included", text='Welcome Amenities: Honeymoon floral layout, luxury chocolates, and fruit basket', sort_order=5),
        ItineraryInclusionNested(kind="included", text='Exclusive Experiences: Private entry slot for Triveni Ghat evening prayer', sort_order=6),
        ItineraryInclusionNested(kind="excluded", text='Airfare, domestic flight charges, or train tickets', sort_order=7),
        ItineraryInclusionNested(kind="excluded", text='Monument entry fees, camera passes, and local tour guide fees', sort_order=8),
        ItineraryInclusionNested(kind="excluded", text='Personal items such as laundry, telephone billing, or tips', sort_order=9),
        ItineraryInclusionNested(kind="excluded", text='Adventure sports like rafting, bungee jumping, and ropeways', sort_order=10),
    ]

def build_uk_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug='uk-008-mussoorie-romance-honeymoon',
        destination_id=destination_id,
        title='Mussoorie Romance • 04 Nights / 05 Days',
        duration_label='04 Nights / 05 Days',
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=27,
        is_published=True,
        highlights=[
            PackageHighlightNested(text='Mussoorie (4N) with Landour and Dhanaulti excursions', sort_order=1),
    PackageHighlightNested(text='Private dedicated AC sedan with professional chauffeur', sort_order=2),
    PackageHighlightNested(text='MAPAI — premium buffet breakfasts and gourmet dinners', sort_order=3),
    PackageHighlightNested(text='Complimentary Gun Hill scenic cable car dual tickets', sort_order=4),
    PackageHighlightNested(text='TRAGUIN 24/7 personalized concierge assistance', sort_order=5),
    PackageHighlightNested(text='Tour code TRG-UK-008 | Serial UK-008', sort_order=6),
        ],
        moods=['Romantic', 'Luxury', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug='uk-008-mussoorie-romance-itinerary',
        destination_id=destination_id,
        title='Mussoorie Romance • 04 Nights / 05 Days',
        duration_label='04 Nights / 05 Days',
        duration_days=5,
        starting_price=0,
        price_note='On Request (Premium Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Dehradun • Mussoorie • Dhanaulti • Landour',
        overview='This custom-tailored romantic itinerary offers a perfect blend of high-altitude tranquility, sweeping Himalayan vistas, and timeless colonial luxury. Travelling comfortably in a dedicated premium private vehicle with an experienced professional chauffeur, your couple retreat ensures absolute privacy and a smooth journey throughout the mountains. With a custom meal plan including decadent breakfasts and specially prepared multi-cuisine dinners, this route represents the definitive premium Uttarakhand experience. Each day includes unique TRAGUIN curated experiences, featuring special room upgrades, prioritized entry to iconic attractions, and unmatched round-the-clock guest support.',
        seo_title='UK-008 | Mussoorie Romance Honeymoon | TRAGUIN',
        seo_description='Luxury 04 Nights / 05 Days Mussoorie honeymoon (UK-008): Kempty Falls, Landour heritage, Dhanaulti Eco Park, and Surkanda Devi with 4N Mussoorie stays and MAPAI plan.',
        is_featured=True,
        featured_sort_order=27,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text='Kempty Falls', sort_order=1),
    ItineraryHighlightNested(text="Landour Cantonment & Sister's Bazaar", sort_order=2),
    ItineraryHighlightNested(text='Lal Tibba Scenic Overlook', sort_order=3),
    ItineraryHighlightNested(text='Dhanaulti Eco Park', sort_order=4),
    ItineraryHighlightNested(text='Surkanda Devi Temple Ropeway', sort_order=5),
        ],
        days=[
            _day(
        1,
        'Arrival in Dehradun to Mussoorie | Gateway to the Hills',
        'Your premium Uttarakhand experience begins as you arrive at Dehradun Airport or Railway Station, where a private luxury transport sedan and dedicated chauffeur await your arrival. Leave the plains behind as your scenic route winds through dense sal forests and sharp mountain bends, offering breathtaking landscapes at every turn. Ascend smoothly into Mussoorie and check into your handpicked luxury honeymoon suite. Spend your evening strolling hand-in-hand along the famous, illuminated Mall Road, enjoying local food, heritage architecture, and gorgeous valley vistas.',
        [
            'Sightseeing Included: Scenic Dehradun-Mussoorie highway drive, Mall Road evening walk, Library Bazaar',
            'Evening Experience: Honeymoon Special: Custom welcome cake, floral room arrangement, and a welcome mocktail',
            'Overnight Stay: Mussoorie (Premium Valley View Luxury Resort)',
            'Meals Included: Welcome Drink & Luxury Welcome Dinner',
        ],
    ),
    _day(
        2,
        'Mussoorie Sightseeing Experiences | Cascading Waterfalls & Spectacular Valley Vistas',
        'Awake to a crisp morning over the valley and enjoy a lavish buffet breakfast. Today, enjoy a comprehensive Mussoorie sightseeing tour. Head towards the famous Kempty Falls, where mountain streams cascade dramatically down towering rocks into a clear pool below. Next, visit the beautifully manicured Company Garden and take a romantic cable car ride up to Gun Hill—the second highest peak in Mussoorie—offering an incredible 360-degree view of the majestic Himalayan range.',
        [
            'Sightseeing Included: Kempty Falls, Company Garden, Gun Hill cable car point, Mussoorie Lake',
            'Optional Activities: Private couple boating session on Mussoorie Lake; professional hill-attire photography',
            'Evening Experience: An exclusive private candlelight dinner overlooking the sparkling lights of Dehradun valley, curated by TRAGUIN experts',
            'Overnight Stay: Mussoorie (Premium Valley View Luxury Resort)',
            'Meals Included: Premium Breakfast & Gourmet Candlelight Dinner',
        ],
    ),
    _day(
        3,
        'Landour Heritage Excursion | Old-World Colonial Charm and Silent Pine Trails',
        "After a leisurely morning breakfast, take a scenic drive to the peaceful, historic cantonment town of Landour. Strikingly quiet and exceptionally pristine, Landour offers an immersive experience into colonial history. Walk along the tranquil Sister's Bazaar trail, shaded by towering deodar and pine trees. Visit Lal Tibba, the highest point in the region, featuring binocular views of snow-capped Tibetan peaks. Spend your afternoon relaxing at legendary bakeries, enjoying handmade cheese, fresh crepes, and artisanal coffees.",
        [
            "Sightseeing Included: Landour Cantonment, Lal Tibba Scenic Overlook, St. Paul's Church, Sister's Bazaar",
            'Photography Points: Char Dukan lane, Kelloggs Church colonial facades, Lal Tibba telescope platform',
            'Overnight Stay: Mussoorie (Premium Valley View Luxury Resort)',
            'Meals Included: Premium Breakfast & Multi-Cuisine Dinner',
        ],
    ),
    _day(
        4,
        'Day Excursion to Dhanaulti | Serene Eco-Forests & Dramatic Alpine Landscapes',
        'Today, explore the dramatic, alpine beauty of Dhanaulti. Drive through quiet mountain paths lined with rhododendron forests until you reach the pristine Dhanaulti Eco Park. This serene conservation zone features deep silence, walking paths, and beautiful landscapes. Afterwards, visit the ancient Surkanda Devi Temple, perched on a mountain peak at 9,995 feet, accessible by a scenic ropeway ride that reveals unforgettable memories of the snow-peaks.',
        [
            'Sightseeing Included: Dhanaulti Eco Park, Amber and Dhara Forests, Surkanda Devi Temple (includes Ropeway)',
            'Optional Activities: Adventure Burma bridge walking or zip-lining at Dhanaulti adventure camps',
            'Overnight Stay: Mussoorie (Premium Valley View Luxury Resort)',
            'Meals Included: Premium Breakfast & Specialized Farewell Dinner',
        ],
    ),
    _day(
        5,
        'Mussoorie to Dehradun / Departure | Cherishing Romantic Memories Beyond Destinations',
        'Indulge in a final morning breakfast while watching the sun illuminate the misty mountain peaks. Your private luxury transport will safely guide you back down the scenic mountains towards Dehradun Airport or Railway Station for your onward journey home. Return with your bonds strengthened and a heart filled with unforgettable memories designed beautifully by TRAGUIN.',
        [
            'Transfers Included: Private luxury station or airport drop-off transfer',
            'Meals Included: Sumptuous Buffet Breakfast',
        ],
    ),
        ],
        hotels=[
            ItineraryHotelNested(name='The Fern Hillside Resort / Fortune Resort Grace / similar', location='Mussoorie', nights_label='04 Nights', category_label='Deluxe', room_type='Deluxe Valley View Room', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=1),
    ItineraryHotelNested(name='Welcomhotel by ITC Hotels, The Savoy / Jaypee Manor', location='Mussoorie', nights_label='04 Nights', category_label='Premium', room_type='Premium Balcony Room', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=2),
    ItineraryHotelNested(name='JW Marriott Mussoorie Walnut Grove Resort & Spa', location='Mussoorie', nights_label='04 Nights', category_label='Luxury', room_type='Luxury Executive Valley Suite', meal_plan='MAPAI + Exclusive Honeymoon Kit', stars=5, sort_order=3),
    ItineraryHotelNested(name='Six Senses Vana / Dedicated Private Luxury Chalet Elite', location='Mussoorie', nights_label='04 Nights', category_label='Ultra Luxury', room_type='VVIP Royal Presidential Suite', meal_plan='Bespoke Signature MAPAI Plan', stars=5, sort_order=4),
        ],
        inclusions=_uk008_inclusions(),
    )
    return package, itinerary

def _uk008_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text='Premium Stays: 04 Nights in handpicked romantic luxury properties as per chosen tier', sort_order=1),
        ItineraryInclusionNested(kind="included", text='Luxury Transportation: Private dedicated AC sedan for all point-to-point sightseeing', sort_order=2),
        ItineraryInclusionNested(kind="included", text='Curated Meal Plan: Daily premium buffet breakfasts and gourmet dinners (MAPAI)', sort_order=3),
        ItineraryInclusionNested(kind="included", text='TRAGUIN Support: 24/7 personalized concierge and emergency travel assistance', sort_order=4),
        ItineraryInclusionNested(kind="included", text='Welcome Amenities: Honeymoon welcome cake, floral bedding art, and premium travel kit', sort_order=5),
        ItineraryInclusionNested(kind="included", text='Complimentary Experience: Private dual-ticket for Gun Hill scenic cable car access', sort_order=6),
        ItineraryInclusionNested(kind="excluded", text='Domestic airfare, flight tickets, or long-distance train travel', sort_order=7),
        ItineraryInclusionNested(kind="excluded", text='Adventure sport fees (Zip-lining, sky-walking, paragliding charges)', sort_order=8),
        ItineraryInclusionNested(kind="excluded", text='Monument entry tickets, professional guide fees, camera permits', sort_order=9),
        ItineraryInclusionNested(kind="excluded", text='Personal expenses such as laundry, phone calls, or tips', sort_order=10),
    ]

def build_uk_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug='uk-009-ladies-retreat-rishikesh',
        destination_id=destination_id,
        title='Ladies Retreat Rishikesh • Renewal, Sisterhood & Sacred Waters',
        duration_label='04 Nights / 05 Days',
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=28,
        is_published=True,
        highlights=[
            PackageHighlightNested(text='Rishikesh (4N) with Shivpuri rafting and Kunjapuri sunrise', sort_order=1),
    PackageHighlightNested(text='Private luxury Traveller/Innova with female concierge support', sort_order=2),
    PackageHighlightNested(text='APAI — all gourmet breakfasts, lunches, and dinners', sort_order=3),
    PackageHighlightNested(text='Private Tibetan Sound Bowl healing workshop', sort_order=4),
    PackageHighlightNested(text='TRAGUIN 24/7 dedicated local female concierge assistance', sort_order=5),
    PackageHighlightNested(text='Tour code TRG-UK-009 | Serial UK-009', sort_order=6),
        ],
        moods=['Adventure', 'Spiritual', 'Solo'],
    )
    itinerary = ItineraryCreate(
        slug='uk-009-ladies-retreat-itinerary',
        destination_id=destination_id,
        title='Ladies Retreat Rishikesh • Renewal, Sisterhood & Sacred Waters',
        duration_label='04 Nights / 05 Days',
        duration_days=5,
        starting_price=0,
        price_note='On Request (Premium All-Women Exclusive Customised)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Rishikesh • Narendranagar • Shivpuri • Haridwar',
        overview='This elite, all-women customized luxury holiday package offers an exquisite balance of adventure, holistic wellness, and royal comfort. Travelling in a high-end, chauffeured private premium vehicle backed by female concierge assistance, your group will enjoy unmatched security and leisure. With a carefully structured healthy gourmet meal plan featuring daily organic spreads, this route represents the definitive premium Uttarakhand experience. Every stage of your retreat features the distinct TRAGUIN curated experience note, including private sound-healing workshops, reserved premium seating at the ghats, and tailored local exploration.',
        seo_title='UK-009 | Ladies Retreat Rishikesh | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days all-women Rishikesh retreat (UK-009): yoga, rafting, Kunjapuri sunrise, sound healing, and APAI full-board plan with 4N Rishikesh luxury stays.',
        is_featured=True,
        featured_sort_order=28,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text='Sunrise Yoga & Meditation', sort_order=1),
    ItineraryHighlightNested(text='Beatles Ashram', sort_order=2),
    ItineraryHighlightNested(text='Shivpuri White-Water Rafting', sort_order=3),
    ItineraryHighlightNested(text='Kunjapuri Devi Temple Sunrise', sort_order=4),
    ItineraryHighlightNested(text='Private Ganga Aarti Ceremony', sort_order=5),
        ],
        days=[
            _day(
        1,
        'Arrival in Rishikesh | Welcome to the Spiritual Capital',
        'Your premium Uttarakhand experience begins as you arrive at Dehradun Airport or Haridwar Station, where a private luxury transport coach with dedicated guest assistance awaits your group. Drive along scenic routes carved through the Shivalik forests to arrive in Rishikesh, checking into a handpicked premium wellness resort overlooking the majestic Ganges. After a refreshing organic welcome juice, indulge in a complimentary evening group foot reflexology session to melt away travel fatigue.',
        [
            'Sightseeing Included: Scenic Shivalik foothills drive, Riverside premium wellness resort check-in',
            'Evening Experience: Group ice-breaking dinner with custom herbal cocktails curated by TRAGUIN experts',
            'Overnight Stay: Rishikesh (Premium Riverside Luxury Spa Resort)',
            'Meals Included: Welcome Drink, Refreshing High Tea & Luxury Dinner',
        ],
    ),
    _day(
        2,
        'Rishikesh Ayurveda & Sacred Sightseeing | Yoga Sanctuary & Private Ganga Aarti',
        'Awake early for a sunrise meditation and yoga session led by a master yogi. After a delicious gourmet breakfast, enjoy a curated tour of the famous Beatles Ashram, where the legendary band practiced transcendental meditation amidst breathtaking landscapes. In the afternoon, walk past the iconic attractions of Ram Jhula and Lakshman Jhula. As dusk falls, enjoy an exclusive experience at a private ghat for an emotional, soul-stirring Ganga Aarti ceremony with premium reserved seating.',
        [
            'Sightseeing Included: Beatles Ashram, Ram Jhula, Parmarth Niketan, Private Aarti Ghat',
            'Optional Activities: Private customized astrological and aura reading session inside the resort',
            'Overnight Stay: Rishikesh (Premium Riverside Luxury Spa Resort)',
            'Meals Included: Organic Breakfast, Spa Lunch & Fine Dining Dinner',
        ],
    ),
    _day(
        3,
        'Shivpuri River Adventure & Beach Picnic | White Water Thrills',
        'Today combines high-octane adventure with scenic beauty. Travel to Shivpuri for a thrilling, professionally-guided white-water rafting experience along the emerald currents of the Ganges. For those seeking relaxation, alternative paths lead to beautiful nature walks. Gather later on a clean, white-sand beach for a private luxury picnic lunch featuring live acoustic music and gourmet local delicacies setup exclusively for your group.',
        [
            'Sightseeing Included: Shivpuri river rapids, white-sand river beaches, secret mountain stream trails',
            'Evening Experience: Resort bonfire night under the starry skies with curated interactive drumming circles',
            'Overnight Stay: Rishikesh (Premium Riverside Luxury Spa Resort)',
            'Meals Included: Gourmet Breakfast, Luxury Beach Picnic Lunch & Live Barbecue Dinner',
        ],
    ),
    _day(
        4,
        'Kunjapuri Sunrise & Luxury Wellness Retreat | Sound Healing Therapy',
        'An unforgettable morning begins before dawn with a luxury drive up to Kunjapuri Devi Temple, perched high on a ridge at 1,645 meters. Witness a spectacular sunrise illuminating the snow-clad peaks of the Himalayas—a highly sought-after photography point. Return to the resort for an afternoon of pure leisure. Participate in an exclusive, deeply restorative Tibetan Sound Bowl healing workshop designed to align your mind and spirit.',
        [
            'Sightseeing Included: Kunjapuri Mountain Summit, Himalayan Range Panorama view points',
            'Optional Activities: Signature full-body Ayurvedic Abhyanga massage at the elite resort wellness wing',
            'Overnight Stay: Rishikesh (Premium Riverside Luxury Spa Resort)',
            'Meals Included: Summit High-Tea Breakfast, Nutritious Lunch & Elegant Farewell Dinner',
        ],
    ),
    _day(
        5,
        'Departure via Haridwar | Returning with Renewed Vigor & Lifelong Sisterhood',
        'Enjoy your final organic breakfast overlooking the misty river currents. Check out from your premium stays property and embark on a smooth return drive via Haridwar. Stop briefly to see the sacred Har Ki Pauri ghat before your private vehicle safely transfers you to Dehradun Airport or Haridwar station for your journey home. Return carrying a deep sense of peace, empowerment, and unforgettable memories designed with passion by TRAGUIN.',
        [
            'Transfers Included: Private luxury group drop-off with complete luggage handling assistance',
            'Meals Included: Sumptuous Buffet Breakfast',
        ],
    ),
        ],
        hotels=[
            ItineraryHotelNested(name='Aloha On The Ganges / Divine Resort / similar', location='Rishikesh', nights_label='04 Nights', category_label='Deluxe', room_type='Garden View Executive Room', meal_plan='APAI (Breakfast, Lunch & Dinner)', stars=4, sort_order=1),
    ItineraryHotelNested(name='The Grand Shiva / Namami Ganges / similar', location='Rishikesh', nights_label='04 Nights', category_label='Premium', room_type='Premium Private Balcony Room', meal_plan='APAI (Breakfast, Lunch & Dinner)', stars=4, sort_order=2),
    ItineraryHotelNested(name='Taj Rishikesh Resort & Spa / The Roseate Ganges', location='Rishikesh', nights_label='04 Nights', category_label='Luxury', room_type='Luxury River View Suite', meal_plan='APAI + Wellness Privilege Kit', stars=5, sort_order=3),
    ItineraryHotelNested(name='Ananda In The Himalayas (Palace Estate)', location='Rishikesh', nights_label='04 Nights', category_label='Ultra Luxury', room_type='VVIP Royal Palace Garden Suite', meal_plan='Bespoke Signature Detox APAI', stars=5, sort_order=4),
        ],
        inclusions=_uk009_inclusions(),
    )
    return package, itinerary

def _uk009_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text='Premium Stays: 04 Nights inside high-end handpicked hotels', sort_order=1),
        ItineraryInclusionNested(kind="included", text='Luxury Transportation: Dedicated private AC vehicle with experienced tourist driver', sort_order=2),
        ItineraryInclusionNested(kind="included", text='Curated Meal Plan: Full-board APAI plans (All gourmet breakfasts, lunches & dinners)', sort_order=3),
        ItineraryInclusionNested(kind="included", text='TRAGUIN Support: 24/7 dedicated local female concierge assistance on call', sort_order=4),
        ItineraryInclusionNested(kind="included", text='Welcome Amenities: Customized organic skincare gift kit and welcome beverages', sort_order=5),
        ItineraryInclusionNested(kind="included", text='Exclusive Experiences: Private Tibetan Sound Bowl healing & reserved Aarti seating', sort_order=6),
        ItineraryInclusionNested(kind="excluded", text='Airfare, domestic flight charges, or long-distance train tickets', sort_order=7),
        ItineraryInclusionNested(kind="excluded", text='Personal expenses such as external laundry, shopping, phone calls', sort_order=8),
        ItineraryInclusionNested(kind="excluded", text='Individual tip distributions, alcohol bills, optional medical insurances', sort_order=9),
        ItineraryInclusionNested(kind="excluded", text='Any extreme adventure sports not explicitly mentioned in the itinerary', sort_order=10),
    ]

def build_uk_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug='uk-010-leisure-senior-citizen-retreat',
        destination_id=destination_id,
        title='Leisure Uttarakhand • A Soulful Senior Citizen Retreat',
        duration_label='05 Nights / 06 Days',
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=29,
        is_published=True,
        highlights=[
            PackageHighlightNested(text='Mussoorie (2N) → Rishikesh (3N) with Haridwar excursion', sort_order=1),
    PackageHighlightNested(text='Private AC Innova Crysta with senior-care chauffeur', sort_order=2),
    PackageHighlightNested(text='MAPAI — mild, low-spice healthy breakfasts and dinners', sort_order=3),
    PackageHighlightNested(text='Reserved comfortable seating for Triveni Ghat Maha Aarti', sort_order=4),
    PackageHighlightNested(text='TRAGUIN 24/7 dedicated telephone line and emergency backing', sort_order=5),
    PackageHighlightNested(text='Tour code TRG-UK-010 | Serial UK-010', sort_order=6),
        ],
        moods=['Family', 'Luxury', 'Spiritual', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug='uk-010-senior-leisure-itinerary',
        destination_id=destination_id,
        title='Leisure Uttarakhand • A Soulful Senior Citizen Retreat',
        duration_label='05 Nights / 06 Days',
        duration_days=6,
        starting_price=0,
        price_note='On Request (Premium Fully Customizable)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Dehradun • Mussoorie • Rishikesh • Haridwar',
        overview='This custom-designed leisure itinerary has been carefully planned by TRAGUIN experts to minimize long, exhausting road travel and avoid high-strain walking paths. Traveling in a dedicated premium luxury vehicle equipped with superior suspension and captain seats, our senior guests will enjoy optimal comfort. Accompanied by a highly empathetic, professional chauffeur, this route delivers a flawless premium Uttarakhand experience. Featuring a nourishing meal plan with mild, healthy culinary options across luxury properties, this package ensures a completely smooth vacation from pickup to departure.',
        seo_title='UK-010 | Senior Citizen Leisure Retreat Uttarakhand | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days senior citizen leisure tour (UK-010): Mussoorie, Rishikesh, and Haridwar with gentle sightseeing, MAPAI plan, and accessible luxury stays.',
        is_featured=True,
        featured_sort_order=29,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text='Company Garden & Gun Hill Cable Car', sort_order=1),
    ItineraryHighlightNested(text='Forest Research Institute Dehradun', sort_order=2),
    ItineraryHighlightNested(text='Parmarth Niketan Ashram', sort_order=3),
    ItineraryHighlightNested(text='Triveni Ghat Ganga Aarti', sort_order=4),
    ItineraryHighlightNested(text='Har Ki Pauri & Mansa Devi Temple', sort_order=5),
        ],
        days=[
            _day(
        1,
        'Arrival in Dehradun & Drive to Mussoorie | Welcome to the Queen of Hills',
        'Your premium Uttarakhand experience begins with a VIP reception at Dehradun Airport or Railway Station. Your professional chauffeur assists you into a luxury private vehicle, pre-stocked with refreshing mineral water and healthy snacks. Enjoy a smooth, scenic drive up the winding hills to Mussoorie. Check into your premium luxury hotel with quick, priority room check-in. The evening is spent entirely at leisure, breathing the pure mountain air from your private valley-view balcony.',
        [
            'Sightseeing Included: Malsi Deer Park en-route (gentle walking path), Mussoorie valley views',
            'Evening Experience: Relaxed welcome high-tea session overlooking the glittering Doon Valley',
            'Overnight Stay: Mussoorie (Premium / Luxury Resort)',
            'Meals Included: Welcome Drink & Gourmet Dinner',
        ],
    ),
    _day(
        2,
        'Mussoorie Sightseeing | Colonial Heritage, Scenic Beauty & Refreshing Gardens',
        'Indulge in a nutritious breakfast before embarking on a relaxed Mussoorie sightseeing tour. Visit Company Garden, a beautifully manicured park featuring smooth paved walking tracks, vibrant flower beds, and flat resting benches perfect for seniors. Take an optional, short cable car ride up to Gun Hill to soak in the breathtaking landscapes of the majestic Himalayan peaks. Conclude your afternoon with a gentle drive through the historic, vehicle-restricted Mall Road using authorized local golf carts.',
        [
            'Sightseeing Included: Company Garden, Camels Back Road (scenic drive), Gun Hill Cable Car (optional)',
            'Photography Points: Camels Rock formation, snow-capped Himalayan viewpoint spots',
            'Overnight Stay: Mussoorie (Premium / Luxury Resort)',
            'Meals Included: Premium Breakfast & Luxury Dinner',
        ],
    ),
    _day(
        3,
        'Mussoorie to Rishikesh via Dehradun | Transition to Serenity',
        'After a serene morning breakfast, check out and drive down towards Rishikesh. En-route, enjoy a flat, leisurely stop at the beautiful Forest Research Institute (FRI) in Dehradun, a world-famous architectural wonder and a popular Instagram location. Arrive in Rishikesh by afternoon and check into your handpicked luxury riverside wellness resort. Spend your evening resting or sitting by the holy Ganges riverbank inside the private resort gardens.',
        [
            'Sightseeing Included: FRI Dehradun campus drive, Lakshman Jhula suspension bridge views from café',
            'Evening Experience: Private customized light meditation or gentle chair yoga session at the resort',
            'Overnight Stay: Rishikesh (Luxury Riverside Wellness Resort)',
            'Meals Included: Premium Breakfast & Satvik Dinner',
        ],
    ),
    _day(
        4,
        'Rishikesh Spiritual Experience | Divine Ashrams & Immersive Sightseeing',
        'Embrace the day with a calming view of the emerald-green river. Your exclusive experiences today include a smooth visit to the iconic Parmarth Niketan Ashram. Explore the beautifully manicured spiritual courtyards without any steep climbing. In the late afternoon, TRAGUIN experts arrange VIP reserved seating for you at Triveni Ghat to witness the world-famous, emotionally moving Ganga Aarti. Listen to soul-stirring hymns as hundreds of brass lamps illuminate the river.',
        [
            'Sightseeing Included: Parmarth Niketan, Ram Jhula area via electric battery vehicle, Triveni Ghat Aarti',
            'Optional Activities: Private gemstone shopping or consultation with an ancient Ayurvedic doctor',
            'Overnight Stay: Rishikesh (Luxury Riverside Wellness Resort)',
            'Meals Included: Premium Breakfast & Organic Gourmet Dinner',
        ],
    ),
    _day(
        5,
        'Excursion to Haridwar | Sacred Waterways & Spiritual Legacies',
        'Take a short, comfortable morning drive to Haridwar, one of the oldest living holy cities. Avoid the dense crowds with a custom-scheduled visit to Har Ki Pauri ghat. Take an easy, modern ropeway cable car ride up to Mansa Devi Temple, eliminating any hill climbing. Spend your afternoon exploring local handloom markets or enjoying mild local food recommendations before heading back to your quiet luxury resort in Rishikesh for your final evening.',
        [
            'Sightseeing Included: Har Ki Pauri, Mansa Devi Temple (via Cable Car), Daksh Mahadev Temple',
            'Evening Experience: A soulful private farewell musical bhajan session inside the resort lounge',
            'Overnight Stay: Rishikesh (Luxury Riverside Wellness Resort)',
            'Meals Included: Premium Breakfast & Farewell Dinner',
        ],
    ),
    _day(
        6,
        'Dehradun / Delhi Departure | Cherishing Faith & Unforgettable Memories',
        'Wake up for a final relaxed breakfast by the sound of the flowing river. Pack your bags as your driver handles all heavy luggage transfers seamlessly. Your private luxury vehicle drives you smoothly back to Dehradun Airport (or onwards to New Delhi) for your return journey home. You depart carrying a deeply rejuvenated body, a peaceful soul, and unforgettable memories crafted with pure love and care by TRAGUIN.',
        [
            'Transfers Included: Private luxury door-to-door station or airport drop-off',
            'Meals Included: Lavish Buffet Breakfast',
        ],
    ),
        ],
        hotels=[
            ItineraryHotelNested(name='Fortune Resort Grace / similar', location='Mussoorie', nights_label='02 Nights', category_label='Deluxe', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=1),
    ItineraryHotelNested(name='Aloha On The Ganges / similar', location='Rishikesh', nights_label='03 Nights', category_label='Deluxe', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=2),
    ItineraryHotelNested(name='Welcomhotel by ITC The Savoy', location='Mussoorie', nights_label='02 Nights', category_label='Premium', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=3),
    ItineraryHotelNested(name='Divine Resort / Lemon Tree Premier', location='Rishikesh', nights_label='03 Nights', category_label='Premium', meal_plan='MAPAI (Breakfast & Dinner)', stars=4, sort_order=4),
    ItineraryHotelNested(name='JW Marriott Walnut Grove Resort', location='Mussoorie', nights_label='02 Nights', category_label='Luxury', meal_plan='MAPAI (Breakfast & Dinner)', stars=5, sort_order=5),
    ItineraryHotelNested(name='Taj Rishikesh Resort & Spa / similar', location='Rishikesh', nights_label='03 Nights', category_label='Luxury', meal_plan='MAPAI (Breakfast & Dinner)', stars=5, sort_order=6),
    ItineraryHotelNested(name='The Westin Resort & Spa Himalayas', location='Mussoorie', nights_label='02 Nights', category_label='Ultra Luxury', meal_plan='MAPAI (Breakfast & Dinner)', stars=5, sort_order=7),
    ItineraryHotelNested(name='Ananda In The Himalayas (Palace View)', location='Rishikesh', nights_label='03 Nights', category_label='Ultra Luxury', meal_plan='Bespoke Customized Dietary Wellness Meals', stars=5, sort_order=8),
        ],
        inclusions=_uk010_inclusions(),
    )
    return package, itinerary

def _uk010_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text='Premium Stays: Luxury accommodations with flat layouts and elevator access', sort_order=1),
        ItineraryInclusionNested(kind="included", text='Luxury Transportation: Private AC Innova Crysta driven by an elite senior-care chauffeur', sort_order=2),
        ItineraryInclusionNested(kind="included", text='Curated Meal Plan: Mild, low-spice, healthy breakfasts and dinners daily (MAPAI)', sort_order=3),
        ItineraryInclusionNested(kind="included", text='TRAGUIN Support: 24/7 dedicated telephone line and localized emergency backing', sort_order=4),
        ItineraryInclusionNested(kind="included", text='Welcome Amenities: Personalized senior travel assistance kit, hand sanitizers, and generic health treats', sort_order=5),
        ItineraryInclusionNested(kind="included", text='Complimentary Experience: Reserved comfortable seating and entry tags for Triveni Ghat Maha Aarti', sort_order=6),
        ItineraryInclusionNested(kind="excluded", text='Airfare, domestic flight tickets, or train reservations', sort_order=7),
        ItineraryInclusionNested(kind="excluded", text='Any personal medications, specialized nursing support, or clinical charges', sort_order=8),
        ItineraryInclusionNested(kind="excluded", text='Monument entrance fees, cable car boarding passes, golf cart rentals', sort_order=9),
        ItineraryInclusionNested(kind="excluded", text='Personal expenses such as external laundry, laundry items, and phone calls', sort_order=10),
    ]

UK_BUILDERS = [
    build_uk_001,
    build_uk_002,
    build_uk_003,
    build_uk_004,
    build_uk_005,
    build_uk_006,
    build_uk_007,
    build_uk_008,
    build_uk_009,
    build_uk_010,
]
