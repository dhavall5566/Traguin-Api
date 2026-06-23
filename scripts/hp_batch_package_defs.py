"""Builder functions for HP-004, HP-006, HP-007, HP-009, and HP-010 Himachal packages."""

from __future__ import annotations

from decimal import Decimal

from schemas.itineraries import (
    ItineraryCreate,
    ItineraryDayNested,
    ItineraryHighlightNested,
    ItineraryHotelNested,
    ItineraryInclusionNested,
)
from schemas.packages import PackageCreate, PackageHighlightNested
from services.package_image_specs import (
    HP_004_PEXELS_IMAGES,
    HP_006_PEXELS_IMAGES,
    HP_007_PEXELS_IMAGES,
    HP_009_PEXELS_IMAGES,
    HP_010_PEXELS_IMAGES,
)


def build_hp_004(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 7
    package = PackageCreate(
        slug="hp-004-shimla-manali-dharamshala-explorer",
        destination_id=destination_id,
        title="Shimla • Manali • Dharamshala Explorer",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="Colonial heritage elegance of Shimla — Mall Road, Ridge & Viceregal Lodge",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Kufri alpine panoramas, pine forests & family adventure park",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Scenic Kullu Valley drive along the Beas River to Manali",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Solang Valley snow fields, Atal Tunnel & Lahaul Valley vistas",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Spiritual serenity of Dharamshala & McLeodganj — Little Lhasa",
                sort_order=5,
            ),
            PackageHighlightNested(
                text="Private Innova Crysta with TRAGUIN 24/7 elite concierge",
                sort_order=6,
            ),
        ],
        moods=["Family", "Luxury", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="hp-004-shimla-manali-dharamshala-itinerary",
        destination_id=destination_id,
        title="Shimla • Manali • Dharamshala Explorer",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Alpine Luxury Across Three Himalayan Jewels",
        overview=(
            "Embark on the ultimate Himachal family tour — a premium retreat unveiling majestic peaks, lush valleys, "
            "and rich cultural tapestry from colonial Shimla to snow-draped Manali and the spiritual serenity of "
            "Dharamshala. This TRAGUIN bespoke journey features private alpine chauffeur transfers, handpicked "
            "mountain and riverside resorts, gourmet MAPAI dining, and curated experiences from Kufri panoramas "
            "to Solang Valley adventures and McLeodganj monasteries."
        ),
        seo_title="HP-004 | Shimla Manali Dharamshala Explorer | TRAGUIN Premium Himachal Tour",
        seo_description=(
            "Luxury 07 Nights / 08 Days Himachal Pradesh package (HP-004) covering Shimla, Kufri, Kullu Valley, "
            "Manali, Solang Valley, Atal Tunnel, Dharamshala, and McLeodganj with premium stays and private "
            "transfers. Ideal for families, luxury explorers, and nature lovers."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Shimla & Kufri Excursion", sort_order=1),
            ItineraryHighlightNested(text="Kullu Valley Scenic Drive", sort_order=2),
            ItineraryHighlightNested(text="Manali Heritage & Solang Adventure", sort_order=3),
            ItineraryHighlightNested(text="Atal Tunnel & Lahaul Valley", sort_order=4),
            ItineraryHighlightNested(text="Dharamshala & McLeodganj Exploration", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival in Delhi to Shimla",
                description=(
                    "Your premium Himachal experience starts with a warm welcome at New Delhi Airport or Railway "
                    "Station by your private chauffeured luxury vehicle. Leave the plains behind as you climb into "
                    "the majestic Shivalik hills toward Shimla. Check into your handpicked premium hotel and spend "
                    "a relaxing evening admiring the mist-laden valleys."
                ),
                activities=[
                    "Sightseeing Included: Scenic Himalayan express highway drive, Pinjore Gardens stopover (optional)",
                    "Evening Experience: Private candlelight family welcome dinner at your luxury mountain resort",
                    "Overnight Stay: Shimla (Premium / Luxury Mountain Resort)",
                    "Meals Included: Welcome refreshment & luxury dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Shimla & Kufri Sightseeing",
                description=(
                    "After a grand breakfast, enjoy a short drive to Kufri, celebrated for dense pine forests and "
                    "snow-capped mountain views. Experience a fun yak ride or soft adventure activities. Return to "
                    "Shimla for an iconic walking tour across The Ridge, neo-Gothic Christ Church, and historic Mall Road."
                ),
                activities=[
                    "Sightseeing Included: Kufri Adventure Park, Green Valley view, The Ridge, Christ Church, Mall Road, Scandal Point",
                    "Optional Activities: Heritage walk to the Viceregal Lodge, the historic seat of British power",
                    "Overnight Stay: Shimla (Premium / Luxury Mountain Resort)",
                    "Meals Included: Premium breakfast & dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Shimla to Manali via Kullu Valley",
                description=(
                    "Bid farewell to Shimla and head toward Manali on a highly scenic drive through the heart of "
                    "Himachal. Wind along the sparkling Beas River and cross the breathtaking Kullu Valley. Stop "
                    "en route at traditional handloom factories famous for premium pashmina shawls before arriving "
                    "at your premium riverside luxury resort in Manali."
                ),
                activities=[
                    "Sightseeing Included: Sundernagar Lake, Pandoh Dam, Kullu Valley, Beas River drive views",
                    "Evening Experience: Stroll along the riverbanks of the resort followed by a warm bonfire night",
                    "Overnight Stay: Manali (Premium Riverside Luxury Property)",
                    "Meals Included: Breakfast & lavish riverside dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Manali Local Sightseeing",
                description=(
                    "Immerse yourself in the local heritage and scenic beauty of Manali. Begin with the ancient "
                    "Hadimba Devi Temple tucked inside a dense deodar forest. Explore Vashisht Village's therapeutic "
                    "hot sulphur springs and spend your evening on Manali Mall Road for premium shopping and cafe hopping."
                ),
                activities=[
                    "Sightseeing Included: Hadimba Temple, Club House, Vashisht Hot Springs, Tibetan Monastery, Manali Mall Road",
                    "Evening Experience: Bespoke cafe hopping and trout dining recommendations in Old Manali",
                    "Overnight Stay: Manali (Premium Riverside Luxury Property)",
                    "Meals Included: Breakfast & premium buffet dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="Solang Valley & Atal Tunnel Excursion",
                description=(
                    "An exhilarating day at Solang Valley — the premier adventure hub of Manali. Enjoy paragliding, "
                    "quad biking, and an open gondola cable car ride. Drive through the engineering marvel of the "
                    "Atal Tunnel to enter the spectacular Lahaul Valley with snow-covered mountain views."
                ),
                activities=[
                    "Sightseeing Included: Solang Valley, Atal Tunnel, Sissu Village (Lahaul Valley snow viewpoints)",
                    "Optional Activities: Rohtang Pass excursion (subject to local permissions and extra cost parameters)",
                    "Overnight Stay: Manali (Premium Riverside Luxury Property)",
                    "Meals Included: Breakfast & multi-cuisine chef's special dinner",
                ],
                sort_order=5,
            ),
            ItineraryDayNested(
                day_number=6,
                title="Manali to Dharamshala",
                description=(
                    "Enjoy a delicious breakfast before heading to Dharamshala, a spectacular spiritual hill station. "
                    "Drive past rolling tea gardens, terraced farms, and historic towns like Palampur. The massive "
                    "Dhauladhar range creates a stunning backdrop as you check into your luxury resort."
                ),
                activities=[
                    "Sightseeing Included: Palampur Tea Gardens view, Baijnath Shiva Temple (historic stone marvel)",
                    "Evening Experience: Leisurely relaxation walk inside a private pine estate with mountain sunset photography",
                    "Overnight Stay: Dharamshala / McLeodganj (Luxury Valley Resort)",
                    "Meals Included: Breakfast & authentic mountain dinner",
                ],
                sort_order=6,
            ),
            ItineraryDayNested(
                day_number=7,
                title="Dharamshala & McLeodganj Exploration",
                description=(
                    "Discover the rich culture of McLeodganj, home of His Holiness the Dalai Lama. Visit the serene "
                    "Tsuglagkhang Complex, walk to Bhagsunag Waterfall, and see St. John in the Wilderness Church. "
                    "Explore local markets for premium singing bowls, thangka paintings, and authentic momos."
                ),
                activities=[
                    "Sightseeing Included: Dalai Lama Temple, Bhagsunag Temple & Waterfall, Dal Lake, St. John Church, Cricket Stadium view",
                    "Evening Experience: Farewell family dinner gathering with live mountain music at your luxury resort",
                    "Overnight Stay: Dharamshala / McLeodganj (Luxury Valley Resort)",
                    "Meals Included: Breakfast & premium farewell dinner",
                ],
                sort_order=7,
            ),
            ItineraryDayNested(
                day_number=8,
                title="Dharamshala to Delhi / Departure",
                description=(
                    "Enjoy your last mountain breakfast before your luxury vehicle drives you back to Delhi. Look "
                    "back on an incredible journey filled with sweet family bonds and unforgettable memories "
                    "curated exclusively by TRAGUIN."
                ),
                activities=[
                    "Transfers Included: Private luxury door-to-door highway drop-off to Delhi Airport / Railway Station",
                    "Meals Included: Sumptuous buffet breakfast",
                ],
                sort_order=8,
            ),
        ],
        hotels=[
            ItineraryHotelNested(
                name="Hotel Willow Banks / Similar",
                location="Shimla (2N)",
                nights_label="02 Nights",
                description="Deluxe mountain resort in Shimla.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=1,
            ),
            ItineraryHotelNested(
                name="Radisson Hotel Shimla / Similar",
                location="Shimla (2N)",
                nights_label="02 Nights",
                description="Premium hill resort with valley views.",
                stars=4,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=2,
            ),
            ItineraryHotelNested(
                name="The Cecil — Oberoi / Similar",
                location="Shimla (2N)",
                nights_label="02 Nights",
                description="Luxury mountain hospitality in Shimla.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=3,
            ),
            ItineraryHotelNested(
                name="Wildflower Hall, An Oberoi Resort / Similar",
                location="Shimla (2N)",
                nights_label="02 Nights",
                description="Ultra-luxury Oberoi suite experience in the Himalayas.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Luxury Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=4,
            ),
            ItineraryHotelNested(
                name="Solang Valley Resort / Similar",
                location="Manali (3N)",
                nights_label="03 Nights",
                description="Deluxe riverside resort in Manali.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=5,
            ),
            ItineraryHotelNested(
                name="ManuAllaya Resort & Spa / Similar",
                location="Manali (3N)",
                nights_label="03 Nights",
                description="Premium riverside resort with alpine views.",
                stars=5,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=6,
            ),
            ItineraryHotelNested(
                name="The Himalayan (Castle Resort) / Similar",
                location="Manali (3N)",
                nights_label="03 Nights",
                description="Luxury castle resort on the Beas riverside.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=7,
            ),
            ItineraryHotelNested(
                name="Span Resort & Spa (Elite Presidential) / Similar",
                location="Manali (3N)",
                nights_label="03 Nights",
                description="Ultra-luxury spa resort on the Beas riverside.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Elite Presidential Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=8,
            ),
            ItineraryHotelNested(
                name="Pride Elite Dharamshala / Similar",
                location="Dharamshala (2N)",
                nights_label="02 Nights",
                description="Deluxe valley resort in Dharamshala.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=9,
            ),
            ItineraryHotelNested(
                name="Fortune Park Moksha / Similar",
                location="Dharamshala (2N)",
                nights_label="02 Nights",
                description="Premium resort with Dhauladhar valley views.",
                stars=4,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=10,
            ),
            ItineraryHotelNested(
                name="The Pavilion by HPCA / Hyatt Regency / Similar",
                location="Dharamshala (2N)",
                nights_label="02 Nights",
                description="Luxury resort overlooking the Kangra Valley.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=11,
            ),
            ItineraryHotelNested(
                name="Radisson Blu Resort Dharamshala / Similar",
                location="Dharamshala (2N)",
                nights_label="02 Nights",
                description="Ultra-luxury resort beneath the Dhauladhar range.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Luxury Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=12,
            ),
        ],
        inclusions=[
            ItineraryInclusionNested(
                kind="included",
                text="07 nights premium accommodation at handpicked Shimla, Manali, and Dharamshala resorts",
                sort_order=1,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Daily lavish breakfasts and multi-cuisine dinners (MAPAI plan)",
                sort_order=2,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Private chauffeur-driven AC Innova Crysta for all transfers, valleys & sightseeing",
                sort_order=3,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="TRAGUIN 24/7 dedicated elite guest relationship manager assistance",
                sort_order=4,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Personalized welcome kit, mineral water, dry fruits box, and private bonfire session",
                sort_order=5,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Driver allowances, tolls, parking, fuel, and applicable taxes",
                sort_order=6,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Airfare or train tickets to and from New Delhi",
                sort_order=7,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Monument entry tickets, adventure gear hire, and local ski/paragliding fees",
                sort_order=8,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Personal expenses such as laundry, phone calls, room heaters, and tipping",
                sort_order=9,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Rohtang Pass green tax permissions or local taxi union vehicles if enforced",
                sort_order=10,
            ),
        ],
    )
    return package, itinerary, HP_004_PEXELS_IMAGES


def build_hp_006(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 8
    package = PackageCreate(
        slug="hp-006-romantic-himachal-honeymoon",
        destination_id=destination_id,
        title="Romantic Himachal — Love Amidst the Snow-Capped Peaks",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="VIP reception & scenic Shivalik ascent to colonial Shimla",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Kufri pine trails, panoramic snow peaks & exclusive candlelit dinner",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Romantic Kullu Valley drive with heritage artisan workshop stopover",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Solang Valley snow fields, paragliding & alpine meadow romance",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Hadimba Temple, Old Manali cafes & Vashisht hot springs",
                sort_order=5,
            ),
            PackageHighlightNested(
                text="Honeymoon delights — floral bed setup, premium cake & private chauffeur",
                sort_order=6,
            ),
        ],
        moods=["Romantic", "Luxury", "Honeymoon"],
    )
    itinerary = ItineraryCreate(
        slug="hp-006-romantic-himachal-itinerary",
        destination_id=destination_id,
        title="Romantic Himachal — Love Amidst the Snow-Capped Peaks",
        duration_label="05 Nights / 06 Days",
        duration_days=6,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Love Amidst the Snow-Capped Peaks",
        overview=(
            "Embark on the ultimate Himachal honeymoon package crafted to blend romantic seclusion with "
            "unparalleled alpine grandeur. This TRAGUIN bespoke journey takes couples from walking hand-in-hand "
            "along the mist-covered Ridge of Shimla to witnessing the pristine white magic of Solang Valley in "
            "Manali — featuring handpicked premium stays, candlelit setups, floral bed styling, and a dedicated "
            "luxury chauffeur throughout."
        ),
        seo_title="HP-006 | Romantic Himachal Honeymoon | TRAGUIN Premium Himachal Tour",
        seo_description=(
            "Luxury 05 Nights / 06 Days Himachal honeymoon package (HP-006) covering Shimla, Kufri, Kullu Valley, "
            "Manali, and Solang Valley with candlelit dinners, floral bed setup, and premium romantic stays. "
            "Ideal for newlyweds and couples."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Shimla & Kufri Romance", sort_order=1),
            ItineraryHighlightNested(text="Kullu Valley Scenic Drive", sort_order=2),
            ItineraryHighlightNested(text="Solang Valley Snow Adventure", sort_order=3),
            ItineraryHighlightNested(text="Manali Heritage & Old Manali", sort_order=4),
            ItineraryHighlightNested(text="Honeymoon Candlelit Dinners & Floral Setup", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival in Delhi to Shimla",
                description=(
                    "Your premium Himachal experience initiates with a VIP reception at New Delhi Airport or "
                    "Railway Station by your private executive chauffeur. Board your luxury sedan and ascend into "
                    "the lower Shivalik ranges toward Shimla. Check into your handpicked premium resort with "
                    "individual valley views and enjoy a lavish dinner."
                ),
                activities=[
                    "Sightseeing En-route: Scenic Himalayan expressways, Timber Trail viewpoints",
                    "Welcome Note: Personalised greeting note and fresh floral arrangement in suite from TRAGUIN",
                    "Overnight Stay: Shimla (Premium Luxury Resort)",
                    "Meals Included: Gourmet buffet dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Shimla & Kufri Excursion",
                description=(
                    "Savor a delightful breakfast before heading to Kufri, celebrated for breathtaking landscapes "
                    "and serene pine trails. Walk together through nature paths and capture panoramic snow-capped "
                    "peaks. Return to Shimla for Mall Road, Christ Church, and The Ridge before an intimate "
                    "private candlelit dinner arranged by TRAGUIN experts."
                ),
                activities=[
                    "Shimla Sightseeing: Kufri Nature Park, Mall Road, Scandal Point, Christ Church, Jakhoo Temple path",
                    "Evening Experience: Exclusive candlelit dinner with a complimentary celebratory honeymoon cake",
                    "Overnight Stay: Shimla (Premium Luxury Resort)",
                    "Meals Included: Breakfast & special honeymoon dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Shimla to Manali via Kullu Valley",
                description=(
                    "Depart Shimla after breakfast for an immersive overland drive to Manali. Wind along the stunning "
                    "Beas River valley, passing Kullu town with breathtaking photography points and mist-layered apple "
                    "orchards. Arrive at your ultra-premium luxury resort checking into a master suite facing the river."
                ),
                activities=[
                    "Sightseeing En-route: Pandoh Dam, Hanogi Mata Temple vista, Kullu Valley shawl weaving ateliers",
                    "Local Experience: Guided stopover at a traditional Kullu heritage artisan workshop",
                    "Overnight Stay: Manali (Luxury Valley-Facing Resort)",
                    "Meals Included: Premium breakfast & luxury buffet dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Manali Solang Valley Excursion",
                description=(
                    "Wake up to magnificent morning mountain views before an excursion to Solang Valley — famed for "
                    "adventure and jaw-dropping snow peaks. Partake in optional paragliding, zorbing, or a cable car "
                    "ride offering immersive glacier views. Walk through pristine high-altitude meadows together."
                ),
                activities=[
                    "Sightseeing Included: Solang Valley meadows, snow-view viewpoints, Atal Tunnel entrance portal (subject to permission)",
                    "Optional Activities: Tandem paragliding, quad biking, snow snowboarding (winter months)",
                    "Overnight Stay: Manali (Luxury Valley-Facing Resort)",
                    "Meals Included: Premium breakfast & authentic Himachali-infused dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="Local Manali Cultural Sightseeing",
                description=(
                    "Dedicate your day to exploring Manali's iconic landmarks — the ancient wooden Hadimba Devi "
                    "Temple in Dhungri Van Vihar, quaint Old Manali cafes, and therapeutic Vashisht hot sulfur springs. "
                    "Enjoy a romantic evening by the riverside with a private almond-milk and bedside floral presentation."
                ),
                activities=[
                    "Sightseeing Included: Hadimba Temple, Club House, Vashisht Hot Springs, Tibetan Monastery, Old Manali lanes",
                    "Evening Experience: Private almond-milk and bedside floral presentation setup for newlyweds",
                    "Overnight Stay: Manali (Luxury Valley-Facing Resort)",
                    "Meals Included: Breakfast & premium farewell dinner",
                ],
                sort_order=5,
            ),
            ItineraryDayNested(
                day_number=6,
                title="Manali to Delhi / Departure",
                description=(
                    "Conclude your dream vacation with a lavish breakfast overlooking the valley mist. Your premium "
                    "vehicle navigates the descent back to New Delhi Airport or Railway Station. Bid farewell to the "
                    "spectacular hills carrying beautifully knitted bonds and unforgettable memories by TRAGUIN."
                ),
                activities=[
                    "Transfers Included: Private luxury door-to-door highway drop-off to Delhi",
                    "Meals Included: Sumptuous buffet breakfast",
                ],
                sort_order=6,
            ),
        ],
        hotels=[
            ItineraryHotelNested(
                name="Hotel Willow Banks / Similar",
                location="Shimla (2N)",
                nights_label="02 Nights",
                description="Deluxe romantic mountain resort in Shimla.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=1,
            ),
            ItineraryHotelNested(
                name="Radisson Hotel Shimla / Similar",
                location="Shimla (2N)",
                nights_label="02 Nights",
                description="Premium hill resort with valley views.",
                stars=4,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=2,
            ),
            ItineraryHotelNested(
                name="The Orchid Hotel / Wildflower Hall (Classic) / Similar",
                location="Shimla (2N)",
                nights_label="02 Nights",
                description="Luxury mountain hospitality for honeymooners.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=3,
            ),
            ItineraryHotelNested(
                name="Wildflower Hall, An Oberoi Resort (Executive Suite) / Similar",
                location="Shimla (2N)",
                nights_label="02 Nights",
                description="Ultra-luxury Oberoi executive suite in the Himalayas.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Executive Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=4,
            ),
            ItineraryHotelNested(
                name="Solang Valley Resort (Deluxe) / Similar",
                location="Manali (3N)",
                nights_label="03 Nights",
                description="Deluxe riverside resort in Manali.",
                stars=4,
                category_label="Deluxe",
                room_type="Deluxe Valley View Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=5,
            ),
            ItineraryHotelNested(
                name="ManuAllaya Resort & Spa / Similar",
                location="Manali (3N)",
                nights_label="03 Nights",
                description="Premium riverside resort with alpine views.",
                stars=5,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=6,
            ),
            ItineraryHotelNested(
                name="Span Resort & Spa / The Himalayan (Castle) / Similar",
                location="Manali (3N)",
                nights_label="03 Nights",
                description="Luxury spa resort on the Beas riverside.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=7,
            ),
            ItineraryHotelNested(
                name="The Oberoi Sukhvilas / VVIP River Estate Villa / Similar",
                location="Manali (3N)",
                nights_label="03 Nights",
                description="Ultra-luxury chalet stay near Manali.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="VVIP River Estate Villa",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=8,
            ),
        ],
        inclusions=[
            ItineraryInclusionNested(
                kind="included",
                text="05 nights handpicked romantic resort accommodation in Shimla and Manali",
                sort_order=1,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Daily elaborate breakfasts and gourmet dinners (MAPAI plan)",
                sort_order=2,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Private chauffeur-driven executive sedan for the entire tour",
                sort_order=3,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="TRAGUIN 24/7 priority concierge and guest relationship assistance",
                sort_order=4,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Honeymoon delights — 1x candlelit dinner, 1x premium cake, and floral bed setup",
                sort_order=5,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Personalized arrival refreshment kit and traditional welcome",
                sort_order=6,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Domestic or international airfare or train tickets",
                sort_order=7,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Rohtang Pass permit fees or shuttle costs (if applicable)",
                sort_order=8,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Personal expenses such as laundry, phone bills, premium drinks, and tips",
                sort_order=9,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Adventure sport entry tickets, camera passes, and local tour guides",
                sort_order=10,
            ),
        ],
    )
    return package, itinerary, HP_006_PEXELS_IMAGES


def build_hp_007(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 9
    package = PackageCreate(
        slug="hp-007-snow-romance-manali-honeymoon",
        destination_id=destination_id,
        title="Snow Romance Manali Honeymoon Special",
        duration_label="04 Nights / 05 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="Ultra-luxury Manali river-view resort with styled honeymoon welcome",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Hadimba Temple, Old Manali cafes & Vashisht therapeutic springs",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Solang Valley & Rohtang Pass glacial wonderland snow romance",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Kullu Valley excursion — shawl weaving, meadows & river rafting",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Private candlelight dinner, celebratory cake & floral bedroom styling",
                sort_order=5,
            ),
            PackageHighlightNested(
                text="Private luxury sedan/SUV with TRAGUIN VIP concierge on-call",
                sort_order=6,
            ),
        ],
        moods=["Romantic", "Luxury", "Honeymoon"],
    )
    itinerary = ItineraryCreate(
        slug="hp-007-snow-romance-manali-itinerary",
        destination_id=destination_id,
        title="Snow Romance Manali Honeymoon Special",
        duration_label="04 Nights / 05 Days",
        duration_days=5,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Snow Romance in the Heart of Manali",
        overview=(
            "This bespoke Himachal honeymoon package guides couples into the heart of breathtaking landscapes, "
            "majestic snow-clad summits, and cozy Manali valleys. Travel in absolute style with a private luxury "
            "vehicle, rest in handpicked romantic resorts, and enjoy candlelight dinners, floral bedroom styling, "
            "and curated experiences from Solang Valley snow slopes to Kullu Valley handicraft heritage."
        ),
        seo_title="HP-007 | Snow Romance Manali Honeymoon | TRAGUIN Premium Himachal Tour",
        seo_description=(
            "Luxury 04 Nights / 05 Days Manali honeymoon package (HP-007) covering Solang Valley, Rohtang Pass, "
            "Kullu Valley, and Old Manali with premium romantic stays, candlelight dinners, and floral bed setup. "
            "Ideal for newlyweds and luxury romantics."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Manali River-View Luxury Arrival", sort_order=1),
            ItineraryHighlightNested(text="Heritage Temples & Old Manali Cafes", sort_order=2),
            ItineraryHighlightNested(text="Solang Valley & Rohtang Snow Adventure", sort_order=3),
            ItineraryHighlightNested(text="Kullu Valley Handloom & Rafting", sort_order=4),
            ItineraryHighlightNested(text="Honeymoon Privileges & Bonfire Evenings", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival in Manali",
                description=(
                    "Your premium Himachal experience blooms the moment you land at Bhuntar Airport or reach the "
                    "Chandigarh gateway. Your dedicated private luxury transport escorts you along the scenic Beas "
                    "River highway. Check into your ultra-luxury handpicked resort with a beautifully styled bedroom "
                    "welcome and spend the afternoon on cedar-scented Van Vihar trails."
                ),
                activities=[
                    "Sightseeing Included: Van Vihar Forest Trail, private riverside boardwalk stroll",
                    "Evening Experience: Private intimate candlelight dinner with a custom celebratory cake curated by TRAGUIN experts",
                    "Overnight Stay: Manali (Premium Luxury River View Resort)",
                    "Meals Included: Welcome libation & curated honeymoon dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Manali Local Sightseeing",
                description=(
                    "Savor a lazy, late breakfast before exploring Manali's finest landmarks — the 450-year-old "
                    "wooden Hadimba Devi Temple in deodar forests, therapeutic Vashisht Hot Springs, and the "
                    "cobblestone streets of Old Manali with bohemian cafes and artisanal shopping alleys."
                ),
                activities=[
                    "Sightseeing Included: Hadimba Temple, Vashisht Springs, Club House, Old Manali Cafes",
                    "Optional Activities: Artisanal cafe hopper trail with local live acoustic Himachali music performances",
                    "Overnight Stay: Manali (Premium Luxury Resort)",
                    "Meals Included: Premium breakfast & multi-cuisine dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Solang Valley & Rohtang Pass Excursion",
                description=(
                    "Prepare for an exhilarating day witnessing the scenic beauty of Solang Valley and mighty "
                    "Rohtang Pass (subject to weather and permit parameters). Marvel at the unending blanket of "
                    "snow with optional tandem paragliding, snow-scooter safaris, and skiing. Hold hands and take "
                    "in panoramic vistas of the Pir Panjal range."
                ),
                activities=[
                    "Sightseeing Included: Solang Valley snowy slopes, Atal Tunnel approach, Rohtang high altitude viewpoints",
                    "Evening Experience: Cozy evening lounge session at the resort with a warming private bonfire setting",
                    "Overnight Stay: Manali (Premium Luxury Resort)",
                    "Meals Included: Glacial buffet breakfast & evening dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Manali to Kullu Valley Excursion",
                description=(
                    "Embark on a beautiful day trip to Kullu, renowned for wide river meadows and rich handicraft "
                    "heritage. Tour authentic handloom cooperatives where iconic Kullu shawls are masterfully woven. "
                    "Adventure-loving couples can enjoy optional white-water rafting on the Beas River."
                ),
                activities=[
                    "Sightseeing Included: Kullu Valley meadows, Angora shawl weaving industry, Kasol/Manikaran overlook option",
                    "Optional Activities: White water rafting (Grade II/III rapids) with professional safety crews",
                    "Overnight Stay: Manali (Premium Luxury Resort)",
                    "Meals Included: Breakfast & festive farewell dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="Manali to Departure Gateway",
                description=(
                    "Relish your final lavish breakfast overlooking morning mist rising off valley pine trees. "
                    "Your private luxury transport drives you safely back to your departure airport or railway "
                    "terminus with joy, newfound promises, and unforgettable memories custom crafted by TRAGUIN."
                ),
                activities=[
                    "Transfers Included: Private luxury highway transit drop-off to station / airport",
                    "Meals Included: Gourmet buffet breakfast",
                ],
                sort_order=5,
            ),
        ],
        hotels=[
            ItineraryHotelNested(
                name="Solang Valley Resort / Hotel River Crescent / Similar",
                location="Manali (4N)",
                nights_label="04 Nights",
                description="Deluxe valley-view romantic resort in Manali.",
                stars=4,
                category_label="Deluxe",
                room_type="Deluxe Valley View",
                meal_plan="MAPAI (Breakfast & Dinner) — Welcome Cake & Floral Bed Styling",
                sort_order=1,
            ),
            ItineraryHotelNested(
                name="ManuAllaya Resort & Spa / Golden Tulip / Similar",
                location="Manali (4N)",
                nights_label="04 Nights",
                description="Premium balcony suite with alpine views.",
                stars=5,
                category_label="Premium",
                room_type="Premium Balcony Suite",
                meal_plan="MAPAI (Premium Buffet Menu) — Candlelight Dinner + Fruit Basket",
                sort_order=2,
            ),
            ItineraryHotelNested(
                name="The Himalayan (Castle Resort) / Bookmark Resort / Similar",
                location="Manali (4N)",
                nights_label="04 Nights",
                description="Luxury castle resort with royal chambers.",
                stars=5,
                category_label="Luxury",
                room_type="Grand Royal Chamber",
                meal_plan="MAPAI (Elite Chef Dynamic Menu) — Private Jacuzzi Access + Wine/Mocktails",
                sort_order=3,
            ),
            ItineraryHotelNested(
                name="Span Resort & Spa / Similar",
                location="Manali (4N)",
                nights_label="04 Nights",
                description="Ultra-luxury riverside suite with butler service.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Elite Riverside Luxury Suite",
                meal_plan="MAPAI (Bespoke Fine Dining) — Personalized Butler + Couple Spa Therapy",
                sort_order=4,
            ),
        ],
        inclusions=[
            ItineraryInclusionNested(
                kind="included",
                text="04 nights accommodation in handpicked romantic luxury properties in Manali",
                sort_order=1,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Lavish daily breakfast arrays and customized five-course dinners (MAPAI)",
                sort_order=2,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Chauffeur-driven private elite sedan/SUV for seamless sightseeing",
                sort_order=3,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="TRAGUIN 24/7 dedicated travel consultant VIP assistance on-call",
                sort_order=4,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Honeymoon privileges — premium almond milk nightly, floral room layout, and celebratory cake",
                sort_order=5,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Comprehensive toll fees, parking permits, and driver allowances",
                sort_order=6,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Air tickets or train ticket fees to the state gateway destinations",
                sort_order=7,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Rohtang Pass special NGT green permit costs or local shuttle transit fees",
                sort_order=8,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Personal expenses such as laundry services, phone bills, premium alcohol, and gratuities",
                sort_order=9,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Optional high-adventure sport booking charges (paragliding, river rafting, zorbing)",
                sort_order=10,
            ),
        ],
    )
    return package, itinerary, HP_007_PEXELS_IMAGES


def build_hp_009(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 10
    package = PackageCreate(
        slug="hp-009-girls-trip-manali",
        destination_id=destination_id,
        title="Girls Trip Manali — Wanderlust, Luxury & Sisterhood",
        duration_label="04 Nights / 05 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="Old Manali cafe hopping — artisan coffees, live acoustic music & photography",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Hadimba Temple forests & scenic Jogini Waterfall group trek",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Atal Tunnel crossing to Sissu Valley — epic snowscapes & waterfalls",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Solang Valley cable car, paragliding, zorbing & quad biking adventures",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Private bonfire nights, welcome high-tea & group photoshoot session",
                sort_order=5,
            ),
            PackageHighlightNested(
                text="Premium SUV with vetted chauffeur & TRAGUIN 24/7 female-friendly concierge",
                sort_order=6,
            ),
        ],
        moods=["Adventure", "Nature", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug="hp-009-girls-trip-manali-itinerary",
        destination_id=destination_id,
        title="Girls Trip Manali — Wanderlust, Luxury & Sisterhood",
        duration_label="04 Nights / 05 Days",
        duration_days=5,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Wanderlust, Luxury & Sisterhood in the Himalayas",
        overview=(
            "Presenting a specially designed Himachal tour package for a chic, high-spirited female-only escape. "
            "This TRAGUIN luxury holiday balances adrenaline-pumping high-altitude adventures with absolute comfort, "
            "top-tier safety, and aesthetic leisure — from Old Manali cafe hopping to Jogini Waterfall treks, "
            "Atal Tunnel snowscapes, and Solang Valley adventure sports with private bonfire evenings."
        ),
        seo_title="HP-009 | Girls Trip Manali | TRAGUIN Premium Himachal Tour",
        seo_description=(
            "Luxury 04 Nights / 05 Days Manali girls trip package (HP-009) covering Old Manali cafes, Jogini "
            "Waterfall trek, Atal Tunnel, Sissu Valley, and Solang Valley adventures with premium female-recommended "
            "stays and private SUV transfers."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Old Manali Cafe Hopping", sort_order=1),
            ItineraryHighlightNested(text="Jogini Waterfall Trek", sort_order=2),
            ItineraryHighlightNested(text="Atal Tunnel & Sissu Valley", sort_order=3),
            ItineraryHighlightNested(text="Solang Valley Adventure Sports", sort_order=4),
            ItineraryHighlightNested(text="Private Bonfire & Group Photoshoot", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival in Manali & Cafe Hopping",
                description=(
                    "Your premium Himachal trip kicks off with a warm reception at Chandigarh Station or Bhuntar "
                    "Airport by your dedicated private luxury vehicle. Enjoy a scenic drive alongside the Beas River "
                    "before checking into your handpicked premium stay. Head out to explore Old Manali's bohemian "
                    "cafes with artisan coffees, live acoustic music, and fantastic photography points."
                ),
                activities=[
                    "Sightseeing Included: Old Manali cafe district, riverside nature walks, Mall Road exploration",
                    "Evening Experience: Welcome high-tea session with premium snacks curated by TRAGUIN experts",
                    "Overnight Stay: Manali (Premium Valley View Luxury Resort)",
                    "Meals Included: Welcome mocktails & luxury buffet dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Local Heritage & Jogini Waterfall Trek",
                description=(
                    "Start your morning with a healthy breakfast before heading into the pine forests of Hadimba "
                    "Temple. Drive to Vashisht Village for a light, incredibly scenic short trek to Jogini Waterfalls "
                    "with magnificent valleys perfect for group photos. Spend your late afternoon on Mall Road for "
                    "authentic local souvenir shopping."
                ),
                activities=[
                    "Sightseeing Included: Hadimba Temple, Jogini Waterfall trek, Vashisht Village, Tibetan Monasteries",
                    "Evening Experience: Private cozy bonfire night at the resort with snacks, music, and storytelling",
                    "Overnight Stay: Manali (Premium Valley View Luxury Resort)",
                    "Meals Included: Premium breakfast & barbecue dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Atal Tunnel & Sissu Valley Excursion",
                description=(
                    "Prepare for an unforgettable journey through the Atal Tunnel — a global engineering marvel "
                    "over 9 km long. Cross underneath the mountains to reveal the dramatic landscapes of Sissu in "
                    "Lahaul Valley. Pose by frozen streams, enjoy Sissu Waterfall viewings, and capture stunning "
                    "winter photography."
                ),
                activities=[
                    "Sightseeing Included: Atal Tunnel North Portal, Sissu Village, Chandra River Basin, Sissu Waterfall viewpoint",
                    "Optional Activities: Snow scooter riding or a professional group photoshoot in traditional Himachali attire",
                    "Overnight Stay: Manali (Premium Valley View Luxury Resort)",
                    "Meals Included: Premium breakfast & gourmet dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Solang Valley Adventure Day",
                description=(
                    "After a delicious buffet breakfast, drive to Solang Valley — the adventure sports capital of "
                    "Manali. Take a modern cable car ride up to Mount Phatru for a striking 360-degree glacier view. "
                    "Join immersive experiences like tandem paragliding, zorbing, or quad biking before a premium "
                    "custom dinner party at a curated fine dining restaurant."
                ),
                activities=[
                    "Sightseeing Included: Solang Valley meadows, snow line views, Palchan Village vistas",
                    "Evening Experience: Premium custom dinner party at a curated fine dining restaurant in town",
                    "Overnight Stay: Manali (Premium Valley View Luxury Resort)",
                    "Meals Included: Premium breakfast & farewell special dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="Manali to Departure",
                description=(
                    "Enjoy a final morning breakfast together on the resort terrace as the sun lights up the snow "
                    "peaks. Pack your bags and hop into your private premium vehicle for a comfortable ride back to "
                    "Chandigarh or Delhi with tons of content and unforgettable memories by TRAGUIN."
                ),
                activities=[
                    "Transfers Included: Private luxury door-to-door station or airport drop-off",
                    "Meals Included: Sumptuous buffet breakfast",
                ],
                sort_order=5,
            ),
        ],
        hotels=[
            ItineraryHotelNested(
                name="Solang Valley Resort / Golden Tulip / Similar",
                location="Manali (4N)",
                nights_label="04 Nights",
                description="Deluxe balcony room with valley views and free Wi-Fi.",
                stars=4,
                category_label="Deluxe",
                room_type="Deluxe Balcony Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=1,
            ),
            ItineraryHotelNested(
                name="Manu Allaya Resort / The Grand Welcome / Similar",
                location="Manali (4N)",
                nights_label="04 Nights",
                description="Premium panoramic room with in-house spa discounts.",
                stars=5,
                category_label="Premium",
                room_type="Premium Panoramic Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=2,
            ),
            ItineraryHotelNested(
                name="Span Resort & Spa / Baragarh Resort / Similar",
                location="Manali (4N)",
                nights_label="04 Nights",
                description="Luxury river view suite with private riverside access.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury River View Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=3,
            ),
            ItineraryHotelNested(
                name="The Oberoi Sukhvilas / Sukhvilas Luxury Villas / Similar",
                location="Manali (4N)",
                nights_label="04 Nights",
                description="Ultra-luxury presidential cottage with 24/7 butler service.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="VVIP Royal Presidential Cottage",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=4,
            ),
        ],
        inclusions=[
            ItineraryInclusionNested(
                kind="included",
                text="04 nights in high-end female-recommended premium hotels in Manali",
                sort_order=1,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Daily luxury breakfasts and custom dinners (MAPAI plan)",
                sort_order=2,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Private premium SUV with a verified, professional chauffeur",
                sort_order=3,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="TRAGUIN 24/7 active concierge support and emergency assistance",
                sort_order=4,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Complimentary private bonfire evening with music and snacks",
                sort_order=5,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Welcome kit with customized travel accessories, dry fruits, and mocktails",
                sort_order=6,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Airfare, flight tickets, or interstate train travel",
                sort_order=7,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Adventure sport tickets (paragliding, quad biking, zipline fees)",
                sort_order=8,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Monument entrance passes, camera permits, and local step guide fees",
                sort_order=9,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Personal items such as laundry, phone calls, or tips",
                sort_order=10,
            ),
        ],
    )
    return package, itinerary, HP_009_PEXELS_IMAGES


def build_hp_010(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 11
    package = PackageCreate(
        slug="hp-010-relaxed-shimla-escape",
        destination_id=destination_id,
        title="Relaxed Shimla Escape — Elegance & Leisure at a Gentle Pace",
        duration_label="04 Nights / 05 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="Gentle-paced senior-friendly itinerary with zero-strain travel parameters",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Viceregal Lodge, Ridge, Christ Church & accessible Mall Road stroll",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Mashobra apple orchards & Craignano Nature Park flat garden paths",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Kufri Himalayan Nature Park with leveled wildlife viewing paths",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Low-step Innova Crysta with background-verified courteous chauffeur",
                sort_order=5,
            ),
            PackageHighlightNested(
                text="Senior-friendly hotels with elevators, grab bars & walk-in showers",
                sort_order=6,
            ),
        ],
        moods=["Family", "Luxury", "Culture"],
    )
    itinerary = ItineraryCreate(
        slug="hp-010-relaxed-shimla-itinerary",
        destination_id=destination_id,
        title="Relaxed Shimla Escape — Elegance & Leisure at a Gentle Pace",
        duration_label="04 Nights / 05 Days",
        duration_days=5,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Elegance & Leisure at a Gentle Pace",
        overview=(
            "Embark on the finest Himachal senior citizen holiday specially customized to reveal the sweeping "
            "landscapes and classic colonial heritage of Shimla without any rush or strenuous travel. This "
            "TRAGUIN bespoke journey prioritizes safety, comfort, and emotional well-being with premium stays, "
            "easily accessible iconic attractions, low-step luxury transport, and thoughtfully paced sightseeing "
            "between 10 AM and 4 PM."
        ),
        seo_title="HP-010 | Relaxed Shimla Escape | TRAGUIN Premium Himachal Tour",
        seo_description=(
            "Luxury 04 Nights / 05 Days senior-friendly Shimla package (HP-010) covering Viceregal Lodge, "
            "Mall Road, Mashobra, Craignano, and Kufri with accessible premium stays and gentle-paced sightseeing. "
            "Ideal for senior citizens, family groups, and leisure travelers."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Colonial Heritage & Mall Road", sort_order=1),
            ItineraryHighlightNested(text="Mashobra & Craignano Greenery", sort_order=2),
            ItineraryHighlightNested(text="Kufri Nature Park Panoramas", sort_order=3),
            ItineraryHighlightNested(text="Senior-Friendly Premium Stays", sort_order=4),
            ItineraryHighlightNested(text="Gentle-Paced TRAGUIN Concierge", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival in Shimla",
                description=(
                    "Your premium Shimla experience begins with a warm, personalized greeting by our courteous "
                    "chauffeur at Chandigarh Airport or Kalka Railway Station. Board your comfortable luxury "
                    "transport for a smooth scenic drive up the Himalayan foothills with curated rest stops. "
                    "Check into your premium luxury hotel and spend a relaxing evening admiring the mountain "
                    "sunset from your private balcony."
                ),
                activities=[
                    "Sightseeing Included: Scenic Himalayan foothills drive, Timber Trail panoramic valley views en-route",
                    "Evening Experience: Hot herbal tea presentation and a personalized trip orientation by TRAGUIN experts",
                    "Overnight Stay: Shimla (Premium Luxury Heritage Resort with easy-access elevators)",
                    "Meals Included: Welcome drink & nourishing gourmet dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Shimla Colonial Heritage Sightseeing",
                description=(
                    "Indulge in a relaxed, delicious breakfast before an elegant day of colonial exploration. Visit "
                    "the majestic Viceregal Lodge (Rashtrapati Niwas) with manicured lawns and flat, paved walkways. "
                    "Take the dedicated government elevator to the pedestrian-only Ridge and Mall Road for Christ "
                    "Church and Gaiety Theatre at your own gentle pace."
                ),
                activities=[
                    "Sightseeing Included: Viceregal Lodge gardens, The Ridge, Christ Church, Scandal Point, Mall Road",
                    "Optional Activities: An elegant sit-down high tea session at a legendary heritage cafe overlooking the mountains",
                    "Overnight Stay: Shimla (Premium Luxury Heritage Resort)",
                    "Meals Included: Premium breakfast & custom mild dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Excursion to Mashobra & Craignano Greenery",
                description=(
                    "Awake to the soothing sounds of birds and a crisp mountain breeze. Head to Mashobra, a peaceful "
                    "haven of oak and pine forests, for a quiet drive to Craignano Nature Park with beautiful flat "
                    "garden paths, historic wooden villas, and breathtaking snow peak landscapes with plenty of "
                    "sitting benches and shade zones."
                ),
                activities=[
                    "Sightseeing Included: Mashobra apple orchard vistas, Craignano Italian-style villa lawns, beautiful photography points",
                    "Evening Experience: Private cozy bonfire evening with soothing classic instrumental music back at the resort",
                    "Overnight Stay: Shimla (Premium Luxury Heritage Resort)",
                    "Meals Included: Premium breakfast & traditional Himachali-inspired dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Leisurely Day at Kufri Valleys",
                description=(
                    "Enjoy another premium breakfast before a short, comfortable morning drive to Kufri. Bypass steep "
                    "horse trails to focus on serene, easily reachable viewpoints and the Himalayan Nature Park with "
                    "well-leveled paths for beautiful flora and rare fauna. The afternoon is kept free for complete "
                    "relaxation or resort spa facilities."
                ),
                activities=[
                    "Sightseeing Included: Kufri pine valley vistas, Himalayan Nature Park, Green Valley panoramic photography points",
                    "Optional Activities: A beautiful professional family portraiture session in traditional attire",
                    "Overnight Stay: Shimla (Premium Luxury Heritage Resort)",
                    "Meals Included: Premium breakfast & luxury farewell dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="Shimla to Chandigarh / Departure",
                description=(
                    "Relish a long, lazy breakfast at your premium hotel while capturing your last mountain valley "
                    "photos. Your private luxury transport will be brought right to the main lobby portico for easy, "
                    "comfortable boarding back to Chandigarh Airport or Kalka Station with a rested body and joyful "
                    "spirit."
                ),
                activities=[
                    "Transfers Included: Private luxury door-to-door highway drop-off",
                    "Meals Included: Sumptuous buffet breakfast",
                ],
                sort_order=5,
            ),
        ],
        hotels=[
            ItineraryHotelNested(
                name="Hotel Willow Banks / Clarkes Hotel / Similar",
                location="Shimla (4N)",
                nights_label="04 Nights",
                description="Deluxe heritage hotel with central Mall location and step-free access.",
                stars=4,
                category_label="Deluxe",
                room_type="Premium Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=1,
            ),
            ItineraryHotelNested(
                name="Radisson Hotel Shimla / Welcomhotel Tavisha / Similar",
                location="Shimla (4N)",
                nights_label="04 Nights",
                description="Premium valley-view room with elevators on all floors.",
                stars=4,
                category_label="Premium",
                room_type="Superior Valley View Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=2,
            ),
            ItineraryHotelNested(
                name="The Oberoi Cecil, Shimla / Similar",
                location="Shimla (4N)",
                nights_label="04 Nights",
                description="Luxury heritage valley room with flawless white-glove service.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Heritage Valley Room",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=3,
            ),
            ItineraryHotelNested(
                name="Wildflower Hall, An Oberoi Resort / Similar",
                location="Shimla (4N)",
                nights_label="04 Nights",
                description="Ultra-luxury premier mountain view suite with heated indoor pools.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Premier Mountain View Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=4,
            ),
        ],
        inclusions=[
            ItineraryInclusionNested(
                kind="included",
                text="04 nights in senior-friendly properties with easy accessibility in Shimla",
                sort_order=1,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Custom nutritious breakfasts and tailored mild dinner sets (MAPAI plan)",
                sort_order=2,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Chauffeur-driven Innova Crysta with low steps and spacious seating",
                sort_order=3,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="TRAGUIN 24/7 proactive assistance and senior concierge on call",
                sort_order=4,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Welcome amenities — personalized travel blanket, medical comfort kit, and mineral water",
                sort_order=5,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Complimentary dedicated elevator tickets for easy Mall Road transit",
                sort_order=6,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Airfare, flight tickets, or long-distance rail fares",
                sort_order=7,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Monument entry tickets, professional guide fees, or inner camera fees",
                sort_order=8,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Personal items such as laundry, phone bills, alcoholic beverages, and tips",
                sort_order=9,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Any horse rides, adventure sports, or external porterage services",
                sort_order=10,
            ),
        ],
    )
    return package, itinerary, HP_010_PEXELS_IMAGES
