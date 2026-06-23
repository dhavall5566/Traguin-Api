"""Builder functions for HP-011 through HP-020 Himachal packages (excluding HP-016)."""

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
    HP_011_PEXELS_IMAGES,
    HP_012_PEXELS_IMAGES,
    HP_013_PEXELS_IMAGES,
    HP_014_PEXELS_IMAGES,
    HP_015_PEXELS_IMAGES,
    HP_017_PEXELS_IMAGES,
    HP_018_PEXELS_IMAGES,
    HP_019_PEXELS_IMAGES,
    HP_020_PEXELS_IMAGES,
)


def build_hp_011(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 12
    package = PackageCreate(
        slug="hp-011-spiti-valley-explorer",
        destination_id=destination_id,
        title="Spiti Explorer — Journey to the Middle Land",
        duration_label="08 Nights / 09 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="Epic trans-Himalayan odyssey through Kinnaur & Spiti — the Middle Land of ancient Buddhism",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Key Monastery cliffside marvel, Kibber village & Chicham Bridge over a 1,000-ft gorge",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Langza Buddha statue, Hikkim world's highest post office & fossil-rich Komic village",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Chandratal Moon Lake camping beneath star-studded Spiti skies at 14,100 ft",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Kunzum Pass prayer flags, Atal Tunnel engineering marvel & Manali alpine finale",
                sort_order=5,
            ),
            PackageHighlightNested(
                text="Private 4x4 Innova Crysta with TRAGUIN 24/7 high-altitude concierge support",
                sort_order=6,
            ),
        ],
        moods=["Adventure", "Luxury", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="hp-011-spiti-valley-itinerary",
        destination_id=destination_id,
        title="Spiti Explorer — Journey to the Middle Land",
        duration_label="08 Nights / 09 Days",
        duration_days=9,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Journey to the Middle Land",
        overview=(
            "Embark on TRAGUIN's definitive Spiti Valley expedition — a premium trans-Himalayan journey through "
            "Kinnaur's apple orchards, ancient Tabo monastery caves, and the cold desert landscapes of Kaza. "
            "This bespoke adventure weaves together Key Monastery, fossil villages of Langza and Komic, the "
            "world's highest post office at Hikkim, Chandratal Moon Lake, and a dramatic exit via Kunzum Pass "
            "and the Atal Tunnel to Manali with handpicked mountain lodges, glamping, and expert high-altitude "
            "chauffeur guidance throughout."
        ),
        seo_title="HP-011 | Spiti Valley Explorer | TRAGUIN Premium Himachal Adventure",
        seo_description=(
            "Luxury 08 Nights / 09 Days Spiti Valley package (HP-011) covering Shimla, Kalpa, Nako, Tabo, Kaza, "
            "Key Monastery, Kibber, Langza, Hikkim, Komic, Chandratal, Kunzum Pass, Atal Tunnel, and Manali "
            "with premium stays and private 4x4 transfers. Ideal for adventure seekers and nature lovers."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Kalpa & Kinnaur Kailash Panoramas", sort_order=1),
            ItineraryHighlightNested(text="Nako Lake & Ancient Tabo Monastery", sort_order=2),
            ItineraryHighlightNested(text="Key Monastery, Kibber & Chicham Bridge", sort_order=3),
            ItineraryHighlightNested(text="Langza, Hikkim & Komic Fossil Villages", sort_order=4),
            ItineraryHighlightNested(text="Chandratal Moon Lake & Kunzum Pass", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival in Delhi / Chandigarh to Shimla",
                description=(
                    "Your Spiti odyssey begins with a warm TRAGUIN welcome at New Delhi Airport, Chandigarh "
                    "Airport, or Chandigarh Railway Station. Board your private luxury vehicle and ascend through "
                    "the Shivalik foothills toward Shimla for gentle altitude acclimatization before the high "
                    "Himalayan crossing ahead."
                ),
                activities=[
                    "Sightseeing Included: Scenic Himalayan express highway drive, Pinjore Gardens stopover (optional)",
                    "Evening Experience: Private welcome dinner and Spiti expedition briefing with your TRAGUIN concierge",
                    "Overnight Stay: Shimla (Premium / Luxury Mountain Resort)",
                    "Meals Included: Welcome refreshment & luxury dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Shimla to Kalpa via Rampur",
                description=(
                    "After a hearty breakfast, descend toward the Sutlej Valley and follow the ancient Hindustan-Tibet "
                    "Highway through Rampur Bushahr. Wind past terraced valleys and enter Kinnaur as the sacred "
                    "Kinnaur Kailash peak emerges above Kalpa's famed apple orchards."
                ),
                activities=[
                    "Sightseeing Included: Rampur Bushahr heritage town, Sutlej River gorge views, Suicide Point Kalpa, Roghi Village walk",
                    "Evening Experience: Sunset photography of Kinnaur Kailash from Kalpa ridge with premium local apple cider tasting",
                    "Overnight Stay: Kalpa (Premium Kinnaur Valley Resort)",
                    "Meals Included: Premium breakfast & dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Kalpa to Kaza via Nako & Tabo",
                description=(
                    "Cross into the high Himalayas via Nako village and its serene high-altitude lake. Continue "
                    "to the 1,000-year-old Tabo Monastery — the Ajanta of the Himalayas — with ancient mural caves "
                    "before descending into the cold desert capital of Spiti, Kaza."
                ),
                activities=[
                    "Sightseeing Included: Nako Lake, Gue Mummy Village (optional), Tabo Monastery caves & murals, Kaza market stroll",
                    "Evening Experience: Traditional Spitian dinner with local barley brew recommendations",
                    "Overnight Stay: Kaza (Premium Spiti Valley Lodge)",
                    "Meals Included: Breakfast & authentic mountain dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Key Monastery, Kibber & Chicham Bridge",
                description=(
                    "A spectacular day exploring Spiti's iconic Buddhist landmarks. Visit the cliff-perched Key "
                    "Monastery, drive to one of the world's highest motorable villages at Kibber, and cross the "
                    "thrilling Chicham Bridge suspended over a deep gorge."
                ),
                activities=[
                    "Sightseeing Included: Key Monastery, Kibber Wildlife Sanctuary viewpoint, Chicham Bridge, Kee Gete village vistas",
                    "Optional Activities: Guided monastery meditation session or professional landscape photography tour",
                    "Overnight Stay: Kaza (Premium Spiti Valley Lodge)",
                    "Meals Included: Breakfast & multi-cuisine dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="Langza, Hikkim & Komic Fossil Villages",
                description=(
                    "Discover Spiti's highest inhabited villages on a curated fossil-hunting expedition. Marvel at "
                    "Langza's giant golden Buddha statue, mail a postcard from Hikkim's world's highest post office, "
                    "and explore Komic — one of the highest villages in Asia perched above the valley floor."
                ),
                activities=[
                    "Sightseeing Included: Langza Buddha statue, Hikkim Post Office, Komic Monastery, fossil discovery walk with local guide",
                    "Evening Experience: Stargazing session from your lodge terrace under pristine dark-sky conditions",
                    "Overnight Stay: Kaza (Premium Spiti Valley Lodge)",
                    "Meals Included: Breakfast & chef's special dinner",
                ],
                sort_order=5,
            ),
            ItineraryDayNested(
                day_number=6,
                title="Kaza to Chandratal Moon Lake",
                description=(
                    "Depart Kaza and ascend toward the legendary Chandratal — the Moon Lake — via Losar and Kunzum "
                    "Pass adorned with fluttering prayer flags. Arrive at your premium glamping or boutique lodge "
                    "beside the crystal-clear alpine lake for an unforgettable high-altitude evening."
                ),
                activities=[
                    "Sightseeing Included: Losar village, Kunzum Pass prayer flags, Chandratal Lake walk & photography",
                    "Evening Experience: Private bonfire and hot soup service beside the Moon Lake under the Milky Way",
                    "Overnight Stay: Chandratal (Premium Glamping / Boutique Alpine Camp)",
                    "Meals Included: Breakfast, packed lunch & warm mountain dinner",
                ],
                sort_order=6,
            ),
            ItineraryDayNested(
                day_number=7,
                title="Chandratal to Manali via Atal Tunnel",
                description=(
                    "Witness sunrise over Chandratal's mirror-still waters before descending through Batal and "
                    "Gramphu. Cross the engineering marvel of the Atal Tunnel into Lahaul Valley and continue "
                    "to Manali for a well-earned alpine celebration."
                ),
                activities=[
                    "Sightseeing Included: Chandratal sunrise, Batal checkpoint, Atal Tunnel North Portal, Sissu Village vistas",
                    "Evening Experience: Celebratory riverside dinner at your Manali luxury resort",
                    "Overnight Stay: Manali (Premium Riverside Luxury Property)",
                    "Meals Included: Breakfast & lavish riverside dinner",
                ],
                sort_order=7,
            ),
            ItineraryDayNested(
                day_number=8,
                title="Manali to Chandigarh",
                description=(
                    "Enjoy a leisurely breakfast before a scenic descent through the Kullu Valley toward "
                    "Chandigarh. Stop at Pandoh Dam and Sundernagar Lake viewpoints en route before checking "
                    "into your premium city hotel for a comfortable final night."
                ),
                activities=[
                    "Sightseeing Included: Kullu Valley drive, Pandoh Dam, Sundernagar Lake, Beas River panoramas",
                    "Evening Experience: Farewell dinner at a curated Chandigarh fine-dining restaurant",
                    "Overnight Stay: Chandigarh (Premium City Luxury Hotel)",
                    "Meals Included: Breakfast & farewell dinner",
                ],
                sort_order=8,
            ),
            ItineraryDayNested(
                day_number=9,
                title="Chandigarh Departure",
                description=(
                    "Enjoy your final mountain breakfast before your private luxury vehicle transfers you to "
                    "Chandigarh Airport or Railway Station. Depart with unforgettable memories of Spiti's "
                    "Middle Land curated exclusively by TRAGUIN."
                ),
                activities=[
                    "Transfers Included: Private luxury door-to-door airport or railway station drop-off",
                    "Meals Included: Sumptuous buffet breakfast",
                ],
                sort_order=9,
            ),
        ],
        hotels=[
            ItineraryHotelNested(
                name="Hotel Willow Banks / Similar",
                location="Shimla (1N)",
                nights_label="01 Night",
                description="Deluxe mountain resort for altitude acclimatization.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=1,
            ),
            ItineraryHotelNested(
                name="Radisson Hotel Shimla / Similar",
                location="Shimla (1N)",
                nights_label="01 Night",
                description="Premium hill resort with valley views.",
                stars=4,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=2,
            ),
            ItineraryHotelNested(
                name="The Cecil — Oberoi / Similar",
                location="Shimla (1N)",
                nights_label="01 Night",
                description="Luxury mountain hospitality in Shimla.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=3,
            ),
            ItineraryHotelNested(
                name="Wildflower Hall, An Oberoi Resort / Similar",
                location="Shimla (1N)",
                nights_label="01 Night",
                description="Ultra-luxury Oberoi suite experience in the Himalayas.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Luxury Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=4,
            ),
            ItineraryHotelNested(
                name="Hotel Kinner Villa / Similar",
                location="Kalpa (1N)",
                nights_label="01 Night",
                description="Deluxe Kinnaur valley lodge with Kailash views.",
                stars=3,
                category_label="Deluxe",
                room_type="Valley View Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=5,
            ),
            ItineraryHotelNested(
                name="Hotel Rolling Stones / Similar",
                location="Kalpa (1N)",
                nights_label="01 Night",
                description="Premium apple-orchard resort overlooking Kinnaur Kailash.",
                stars=4,
                category_label="Premium",
                room_type="Premium Kailash View Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=6,
            ),
            ItineraryHotelNested(
                name="The Grand Shamba-La / Similar",
                location="Kalpa (1N)",
                nights_label="01 Night",
                description="Luxury boutique property on Kalpa ridge.",
                stars=4,
                category_label="Luxury",
                room_type="Luxury Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=7,
            ),
            ItineraryHotelNested(
                name="Banjara Retreat Kalpa / Similar",
                location="Kalpa (1N)",
                nights_label="01 Night",
                description="Ultra-luxury heritage cottage with panoramic Kinnaur vistas.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Heritage Cottage Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=8,
            ),
            ItineraryHotelNested(
                name="Hotel Deyzor / Similar",
                location="Kaza (3N)",
                nights_label="03 Nights",
                description="Deluxe Spiti valley lodge in Kaza town.",
                stars=3,
                category_label="Deluxe",
                room_type="Standard Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=9,
            ),
            ItineraryHotelNested(
                name="Spiti Valley Hotel / Similar",
                location="Kaza (3N)",
                nights_label="03 Nights",
                description="Premium heated rooms for high-altitude comfort.",
                stars=4,
                category_label="Premium",
                room_type="Premium Heated Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=10,
            ),
            ItineraryHotelNested(
                name="Spiti Serai by TUTC / Similar",
                location="Kaza (3N)",
                nights_label="03 Nights",
                description="Luxury boutique lodge with Spiti valley panoramas.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Valley Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=11,
            ),
            ItineraryHotelNested(
                name="Spiti Valley Glamping / Similar",
                location="Kaza (3N)",
                nights_label="03 Nights",
                description="Ultra-luxury heated glamping tents with ensuite facilities.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Luxury Glamping Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=12,
            ),
            ItineraryHotelNested(
                name="Chandra Taal Swiss Cottages / Similar",
                location="Chandratal (1N)",
                nights_label="01 Night",
                description="Deluxe alpine camp near Chandratal Lake.",
                stars=3,
                category_label="Deluxe",
                room_type="Swiss Cottage",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=13,
            ),
            ItineraryHotelNested(
                name="Paradise Chandratal Camp / Similar",
                location="Chandratal (1N)",
                nights_label="01 Night",
                description="Premium heated camp with lake access.",
                stars=4,
                category_label="Premium",
                room_type="Premium Heated Tent",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=14,
            ),
            ItineraryHotelNested(
                name="Moon Lake Luxury Camp / Similar",
                location="Chandratal (1N)",
                nights_label="01 Night",
                description="Luxury glamping with ensuite facilities at 14,100 ft.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Glamping Tent",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=15,
            ),
            ItineraryHotelNested(
                name="Bespoke Chandratal Private Camp / Similar",
                location="Chandratal (1N)",
                nights_label="01 Night",
                description="Ultra-luxury private camp with personal butler service.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Private Luxury Camp Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=16,
            ),
            ItineraryHotelNested(
                name="Solang Valley Resort / Similar",
                location="Manali (1N)",
                nights_label="01 Night",
                description="Deluxe riverside resort in Manali.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=17,
            ),
            ItineraryHotelNested(
                name="ManuAllaya Resort & Spa / Similar",
                location="Manali (1N)",
                nights_label="01 Night",
                description="Premium riverside resort with alpine views.",
                stars=5,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=18,
            ),
            ItineraryHotelNested(
                name="The Himalayan (Castle Resort) / Similar",
                location="Manali (1N)",
                nights_label="01 Night",
                description="Luxury castle resort on the Beas riverside.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=19,
            ),
            ItineraryHotelNested(
                name="Span Resort & Spa (Elite Presidential) / Similar",
                location="Manali (1N)",
                nights_label="01 Night",
                description="Ultra-luxury spa resort on the Beas riverside.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Elite Presidential Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=20,
            ),
        ],
        inclusions=[
            ItineraryInclusionNested(
                kind="included",
                text="08 nights premium accommodation across Shimla, Kalpa, Kaza, Chandratal, Manali, and Chandigarh",
                sort_order=1,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Daily lavish breakfasts and multi-cuisine dinners (MAPAI plan)",
                sort_order=2,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Private chauffeur-driven 4x4 Innova Crysta for all high-altitude transfers and sightseeing",
                sort_order=3,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="TRAGUIN 24/7 dedicated elite guest relationship manager and high-altitude emergency support",
                sort_order=4,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Inner Line Permit assistance, oxygen kit, and acclimatization briefing for Spiti sector",
                sort_order=5,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Driver allowances, tolls, parking, fuel, and applicable taxes",
                sort_order=6,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Airfare or train tickets to and from Delhi / Chandigarh",
                sort_order=7,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Monument entry tickets, monastery donations, and local guide fees at Tabo / Key",
                sort_order=8,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Personal expenses such as laundry, phone calls, room heaters, and tipping",
                sort_order=9,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Adventure activities, professional photography, and optional Rohtang Pass permits",
                sort_order=10,
            ),
        ],
    )
    return package, itinerary, HP_011_PEXELS_IMAGES


def build_hp_012(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 13
    package = PackageCreate(
        slug="hp-012-premium-kaza-expedition",
        destination_id=destination_id,
        title="Premium Kaza Expedition",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="Focused premium Spiti circuit centered on Kaza — the cold desert capital of the Himalayas",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Nako Lake serenity & Tabo Monastery — UNESCO-nominated Ajanta of the Himalayas",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Key Monastery, Kibber plateau & Chicham Bridge — Spiti's most iconic landmarks",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Hikkim post office, Langza Buddha & Komic — highest fossil villages on Earth",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Chandratal glamping under Milky Way skies & Atal Tunnel descent to Manali",
                sort_order=5,
            ),
            PackageHighlightNested(
                text="Luxury glamping options with heated ensuite tents and TRAGUIN 24/7 concierge",
                sort_order=6,
            ),
        ],
        moods=["Adventure", "Luxury", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="hp-012-premium-kaza-itinerary",
        destination_id=destination_id,
        title="Premium Kaza Expedition",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="The Definitive Premium Spiti Circuit",
        overview=(
            "TRAGUIN's Premium Kaza Expedition is a refined, high-altitude journey through Spiti Valley's most "
            "extraordinary landscapes. Beginning from Chandigarh, traverse Kinnaur's apple country to ancient Tabo, "
            "establish a luxurious base in Kaza for deep exploration of Key Monastery and fossil villages, camp "
            "beside Chandratal Moon Lake, and descend through the Atal Tunnel to Manali — all with premium glamping, "
            "heated mountain lodges, and expert chauffeur guidance."
        ),
        seo_title="HP-012 | Premium Kaza Expedition | TRAGUIN Luxury Spiti Adventure",
        seo_description=(
            "Luxury 07 Nights / 08 Days Spiti package (HP-012) covering Kalpa, Nako, Tabo, Kaza, Key Monastery, "
            "Kibber, Langza, Hikkim, Komic, Chandratal, Kunzum Pass, Atal Tunnel, and Manali with premium glamping "
            "and private 4x4 transfers."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Kalpa Kinnaur Gateway & Nako Lake", sort_order=1),
            ItineraryHighlightNested(text="Tabo Monastery Ancient Caves", sort_order=2),
            ItineraryHighlightNested(text="Kaza Base — Key, Kibber & Chicham", sort_order=3),
            ItineraryHighlightNested(text="Langza, Hikkim & Komic Villages", sort_order=4),
            ItineraryHighlightNested(text="Chandratal Glamping & Atal Tunnel", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Chandigarh to Kalpa",
                description=(
                    "Your premium Spiti expedition begins with a TRAGUIN welcome at Chandigarh Airport or "
                    "Railway Station. Drive along the Sutlej gorge through Rampur Bushahr into Kinnaur, arriving "
                    "at Kalpa for your first high-altitude acclimatization evening beneath Kinnaur Kailash."
                ),
                activities=[
                    "Sightseeing Included: Rampur Bushahr, Sutlej River gorge, Kalpa Suicide Point, Roghi Village",
                    "Evening Experience: Kinnaur Kailash sunset photography and apple orchard walk",
                    "Overnight Stay: Kalpa (Premium Kinnaur Valley Resort)",
                    "Meals Included: Welcome lunch en-route & premium dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Kalpa to Kaza via Nako & Tabo",
                description=(
                    "Cross the high Himalayan watershed via Nako village and its mirror-still lake. Visit the "
                    "1,000-year-old Tabo Monastery with its ancient mural caves before entering Spiti's cold "
                    "desert capital, Kaza, for a three-night premium base."
                ),
                activities=[
                    "Sightseeing Included: Nako Lake, Tabo Monastery caves & murals, Dhankar Monastery viewpoint (optional)",
                    "Evening Experience: Curated Spitian cuisine tasting at your premium Kaza lodge",
                    "Overnight Stay: Kaza (Premium Spiti Valley Lodge)",
                    "Meals Included: Breakfast & authentic mountain dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Key Monastery, Kibber & Chicham Bridge",
                description=(
                    "Explore Spiti's crown jewels — the cliff-perched Key Monastery, the high plateau village "
                    "of Kibber, and the adrenaline-inducing Chicham Bridge spanning a 1,000-foot gorge."
                ),
                activities=[
                    "Sightseeing Included: Key Monastery, Kibber village, Chicham Bridge, Gete village panoramas",
                    "Optional Activities: Guided monastery tour with resident monk interaction",
                    "Overnight Stay: Kaza (Premium Spiti Valley Lodge)",
                    "Meals Included: Breakfast & multi-cuisine dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Langza, Hikkim & Komic",
                description=(
                    "A curated day among Spiti's highest fossil villages. Photograph Langza's golden Buddha, "
                    "send a postcard from Hikkim's world's highest post office, and hunt marine fossils in "
                    "the ancient seabed of Komic village."
                ),
                activities=[
                    "Sightseeing Included: Langza Buddha statue, Hikkim Post Office, Komic Monastery, fossil discovery walk",
                    "Evening Experience: Premium stargazing session from your lodge terrace",
                    "Overnight Stay: Kaza (Premium Spiti Valley Lodge)",
                    "Meals Included: Breakfast & chef's special dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="Kaza to Chandratal Moon Lake",
                description=(
                    "Ascend from Kaza through Losar village and over Kunzum Pass to reach the legendary "
                    "Chandratal Moon Lake. Check into your premium glamping camp for an unforgettable "
                    "high-altitude night beneath the stars."
                ),
                activities=[
                    "Sightseeing Included: Losar village, Kunzum Pass prayer flags, Chandratal Lake circumambulation",
                    "Evening Experience: Private bonfire, hot soup service, and Milky Way photography session",
                    "Overnight Stay: Chandratal (Premium Luxury Glamping Camp)",
                    "Meals Included: Breakfast, packed lunch & warm mountain dinner",
                ],
                sort_order=5,
            ),
            ItineraryDayNested(
                day_number=6,
                title="Chandratal to Manali via Atal Tunnel",
                description=(
                    "Witness Chandratal sunrise before descending through Batal and crossing the Atal Tunnel "
                    "into Lahaul Valley. Continue to Manali for a celebratory alpine evening at your riverside "
                    "luxury resort."
                ),
                activities=[
                    "Sightseeing Included: Chandratal sunrise, Atal Tunnel North Portal, Sissu Waterfall viewpoint",
                    "Evening Experience: Riverside bonfire and gourmet dinner at your Manali resort",
                    "Overnight Stay: Manali (Premium Riverside Luxury Property)",
                    "Meals Included: Breakfast & lavish riverside dinner",
                ],
                sort_order=6,
            ),
            ItineraryDayNested(
                day_number=7,
                title="Manali — Solang Valley & Atal Excursion",
                description=(
                    "A full day of alpine adventure in Manali. Ride the Solang Valley cable car for glacier "
                    "panoramas, explore Old Manali's cafe culture, and revisit the Atal Tunnel for Sissu "
                    "Valley snow photography."
                ),
                activities=[
                    "Sightseeing Included: Solang Valley cable car, Old Manali, Hadimba Temple, Sissu Valley revisit",
                    "Optional Activities: Tandem paragliding, quad biking, or zorbing at Solang Valley",
                    "Overnight Stay: Manali (Premium Riverside Luxury Property)",
                    "Meals Included: Breakfast & multi-cuisine chef's special dinner",
                ],
                sort_order=7,
            ),
            ItineraryDayNested(
                day_number=8,
                title="Manali to Chandigarh / Departure",
                description=(
                    "Enjoy a final mountain breakfast on your resort terrace before your private luxury vehicle "
                    "transfers you to Chandigarh Airport or Railway Station with unforgettable Spiti memories."
                ),
                activities=[
                    "Transfers Included: Private luxury door-to-door station or airport drop-off via Kullu Valley",
                    "Meals Included: Sumptuous buffet breakfast",
                ],
                sort_order=8,
            ),
        ],
        hotels=[
            ItineraryHotelNested(
                name="Hotel Kinner Villa / Similar",
                location="Kalpa (1N)",
                nights_label="01 Night",
                description="Deluxe Kinnaur valley lodge with Kailash views.",
                stars=3,
                category_label="Deluxe",
                room_type="Valley View Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=1,
            ),
            ItineraryHotelNested(
                name="Hotel Rolling Stones / Similar",
                location="Kalpa (1N)",
                nights_label="01 Night",
                description="Premium apple-orchard resort overlooking Kinnaur Kailash.",
                stars=4,
                category_label="Premium",
                room_type="Premium Kailash View Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=2,
            ),
            ItineraryHotelNested(
                name="The Grand Shamba-La / Similar",
                location="Kalpa (1N)",
                nights_label="01 Night",
                description="Luxury boutique property on Kalpa ridge.",
                stars=4,
                category_label="Luxury",
                room_type="Luxury Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=3,
            ),
            ItineraryHotelNested(
                name="Banjara Retreat Kalpa / Similar",
                location="Kalpa (1N)",
                nights_label="01 Night",
                description="Ultra-luxury heritage cottage with panoramic Kinnaur vistas.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Heritage Cottage Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=4,
            ),
            ItineraryHotelNested(
                name="Hotel Deyzor / Similar",
                location="Kaza (3N)",
                nights_label="03 Nights",
                description="Deluxe Spiti valley lodge in Kaza town.",
                stars=3,
                category_label="Deluxe",
                room_type="Standard Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=5,
            ),
            ItineraryHotelNested(
                name="Spiti Valley Hotel / Similar",
                location="Kaza (3N)",
                nights_label="03 Nights",
                description="Premium heated rooms for high-altitude comfort.",
                stars=4,
                category_label="Premium",
                room_type="Premium Heated Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=6,
            ),
            ItineraryHotelNested(
                name="Spiti Serai by TUTC / Similar",
                location="Kaza (3N)",
                nights_label="03 Nights",
                description="Luxury boutique lodge with Spiti valley panoramas.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Valley Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=7,
            ),
            ItineraryHotelNested(
                name="Spiti Valley Glamping / Similar",
                location="Kaza (3N)",
                nights_label="03 Nights",
                description="Ultra-luxury heated glamping tents with ensuite facilities.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Luxury Glamping Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=8,
            ),
            ItineraryHotelNested(
                name="Chandra Taal Swiss Cottages / Similar",
                location="Chandratal (1N)",
                nights_label="01 Night",
                description="Deluxe alpine camp near Chandratal Lake.",
                stars=3,
                category_label="Deluxe",
                room_type="Swiss Cottage",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=9,
            ),
            ItineraryHotelNested(
                name="Paradise Chandratal Camp / Similar",
                location="Chandratal (1N)",
                nights_label="01 Night",
                description="Premium heated camp with lake access.",
                stars=4,
                category_label="Premium",
                room_type="Premium Heated Tent",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=10,
            ),
            ItineraryHotelNested(
                name="Moon Lake Luxury Camp / Similar",
                location="Chandratal (1N)",
                nights_label="01 Night",
                description="Luxury glamping with ensuite facilities at 14,100 ft.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Glamping Tent",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=11,
            ),
            ItineraryHotelNested(
                name="Bespoke Chandratal Private Camp / Similar",
                location="Chandratal (1N)",
                nights_label="01 Night",
                description="Ultra-luxury private camp with personal butler service.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Private Luxury Camp Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=12,
            ),
            ItineraryHotelNested(
                name="Solang Valley Resort / Similar",
                location="Manali (2N)",
                nights_label="02 Nights",
                description="Deluxe riverside resort in Manali.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=13,
            ),
            ItineraryHotelNested(
                name="ManuAllaya Resort & Spa / Similar",
                location="Manali (2N)",
                nights_label="02 Nights",
                description="Premium riverside resort with alpine views.",
                stars=5,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=14,
            ),
            ItineraryHotelNested(
                name="The Himalayan (Castle Resort) / Similar",
                location="Manali (2N)",
                nights_label="02 Nights",
                description="Luxury castle resort on the Beas riverside.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=15,
            ),
            ItineraryHotelNested(
                name="Span Resort & Spa (Elite Presidential) / Similar",
                location="Manali (2N)",
                nights_label="02 Nights",
                description="Ultra-luxury spa resort on the Beas riverside.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Elite Presidential Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=16,
            ),
        ],
        inclusions=[
            ItineraryInclusionNested(
                kind="included",
                text="07 nights premium accommodation across Kalpa, Kaza, Chandratal, and Manali",
                sort_order=1,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Daily lavish breakfasts and multi-cuisine dinners (MAPAI plan)",
                sort_order=2,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Private chauffeur-driven 4x4 Innova Crysta for all high-altitude transfers and sightseeing",
                sort_order=3,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="TRAGUIN 24/7 dedicated elite guest relationship manager and high-altitude emergency support",
                sort_order=4,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Inner Line Permit assistance, oxygen kit, and premium glamping amenities at Chandratal",
                sort_order=5,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Driver allowances, tolls, parking, fuel, and applicable taxes",
                sort_order=6,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Airfare or train tickets to and from Chandigarh",
                sort_order=7,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Monument entry tickets, monastery donations, and local guide fees",
                sort_order=8,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Adventure sport fees at Solang Valley (paragliding, quad biking, zorbing)",
                sort_order=9,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Personal expenses such as laundry, phone calls, room heaters, and tipping",
                sort_order=10,
            ),
        ],
    )
    return package, itinerary, HP_012_PEXELS_IMAGES


def build_hp_013(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 14
    package = PackageCreate(
        slug="hp-013-luxury-himachal-retreat",
        destination_id=destination_id,
        title="Luxury Himachal Retreat — Grand Heritage & High Alpine Escape",
        duration_label="06 Nights / 07 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="Colonial Shimla heritage — Viceregal Lodge, Ridge, Christ Church & Mall Road elegance",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Kufri alpine panoramas, pine forests & family adventure park excursions",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Scenic Kullu Valley descent with artisan pashmina workshop stopover",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Extended 4-night Manali base — Solang Valley, Atal Tunnel & Sissu Waterfall",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Hadimba Temple, Old Manali cafes & Vashisht therapeutic hot springs",
                sort_order=5,
            ),
            PackageHighlightNested(
                text="Private Innova Crysta with TRAGUIN 24/7 elite concierge throughout",
                sort_order=6,
            ),
        ],
        moods=["Family", "Luxury", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="hp-013-luxury-himachal-itinerary",
        destination_id=destination_id,
        title="Luxury Himachal Retreat — Grand Heritage & High Alpine Escape",
        duration_label="06 Nights / 07 Days",
        duration_days=7,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Grand Heritage & High Alpine Escape",
        overview=(
            "TRAGUIN's Luxury Himachal Retreat blends colonial grandeur with high-alpine adventure across "
            "Shimla and Manali. Spend two nights amid Shimla's heritage architecture and Kufri panoramas, "
            "then settle into a four-night Manali riverside base for Solang Valley thrills, the Atal Tunnel "
            "engineering marvel, Sissu Waterfall vistas, and curated Old Manali experiences — all with premium "
            "resorts, gourmet MAPAI dining, and private chauffeur transfers."
        ),
        seo_title="HP-013 | Luxury Himachal Retreat | TRAGUIN Premium Family Tour",
        seo_description=(
            "Luxury 06 Nights / 07 Days Himachal package (HP-013) covering Shimla, Kufri, Kullu Valley, Manali, "
            "Solang Valley, Atal Tunnel, and Sissu with premium stays and private transfers. Ideal for families "
            "and luxury nature lovers."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Shimla Colonial Heritage & Kufri", sort_order=1),
            ItineraryHighlightNested(text="Kullu Valley Scenic Transfer", sort_order=2),
            ItineraryHighlightNested(text="Manali Heritage & Riverside Leisure", sort_order=3),
            ItineraryHighlightNested(text="Solang Valley Adventure Day", sort_order=4),
            ItineraryHighlightNested(text="Atal Tunnel & Sissu Excursion", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival in Chandigarh to Shimla",
                description=(
                    "Your luxury Himachal retreat begins with a warm TRAGUIN welcome at Chandigarh Airport or "
                    "Railway Station. Ascend through the Shivalik foothills to Shimla and check into your "
                    "handpicked premium heritage resort for a relaxing mountain evening."
                ),
                activities=[
                    "Sightseeing Included: Scenic Himalayan foothills drive, Timber Trail valley views en-route",
                    "Evening Experience: Private welcome dinner and heritage walk briefing on Mall Road",
                    "Overnight Stay: Shimla (Premium Luxury Heritage Resort)",
                    "Meals Included: Welcome refreshment & luxury dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Shimla Heritage & Kufri Excursion",
                description=(
                    "Explore Shimla's colonial legacy at the Viceregal Lodge, Christ Church, and The Ridge. "
                    "Drive to Kufri for alpine panoramas, pine forest trails, and the Himalayan Nature Park "
                    "before returning for an evening stroll along historic Mall Road."
                ),
                activities=[
                    "Sightseeing Included: Viceregal Lodge, The Ridge, Christ Church, Mall Road, Kufri Adventure Park, Green Valley",
                    "Evening Experience: Curated cafe hopping and heritage bookstore visit on Mall Road",
                    "Overnight Stay: Shimla (Premium Luxury Heritage Resort)",
                    "Meals Included: Premium breakfast & dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Shimla to Manali via Kullu Valley",
                description=(
                    "Bid farewell to Shimla and descend through the spectacular Kullu Valley along the Beas River. "
                    "Stop at Pandoh Dam and traditional handloom workshops before arriving at your premium "
                    "riverside luxury resort in Manali."
                ),
                activities=[
                    "Sightseeing Included: Sundernagar Lake, Pandoh Dam, Kullu Valley, Beas River drive, pashmina workshop stop",
                    "Evening Experience: Riverside bonfire and gourmet dinner at your Manali resort",
                    "Overnight Stay: Manali (Premium Riverside Luxury Property)",
                    "Meals Included: Breakfast & lavish riverside dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Manali Local Sightseeing",
                description=(
                    "Immerse yourself in Manali's cultural tapestry. Visit the ancient Hadimba Devi Temple "
                    "in a deodar forest, explore Vashisht's therapeutic hot sulphur springs, and spend your "
                    "evening in Old Manali's bohemian cafe culture."
                ),
                activities=[
                    "Sightseeing Included: Hadimba Temple, Club House, Vashisht Hot Springs, Tibetan Monastery, Old Manali",
                    "Evening Experience: Bespoke trout dining and riverside cafe recommendations in Old Manali",
                    "Overnight Stay: Manali (Premium Riverside Luxury Property)",
                    "Meals Included: Breakfast & premium buffet dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="Solang Valley Adventure Day",
                description=(
                    "An exhilarating day at Solang Valley — Manali's premier adventure hub. Ride the open gondola "
                    "cable car to Mount Phatru for glacier panoramas and enjoy paragliding, zorbing, or quad "
                    "biking amid snow-draped meadows."
                ),
                activities=[
                    "Sightseeing Included: Solang Valley meadows, cable car ride, snow line views, Palchan Village",
                    "Optional Activities: Tandem paragliding, zorbing, quad biking, or ski hire (seasonal)",
                    "Overnight Stay: Manali (Premium Riverside Luxury Property)",
                    "Meals Included: Breakfast & multi-cuisine chef's special dinner",
                ],
                sort_order=5,
            ),
            ItineraryDayNested(
                day_number=6,
                title="Atal Tunnel & Sissu Valley Excursion",
                description=(
                    "Drive through the 9-km Atal Tunnel — a global engineering marvel — into Lahaul Valley. "
                    "Explore Sissu village, photograph the dramatic Sissu Waterfall, and capture snow-covered "
                    "Chandra River basin vistas before a farewell dinner in Manali."
                ),
                activities=[
                    "Sightseeing Included: Atal Tunnel North Portal, Sissu Village, Sissu Waterfall, Chandra River Basin",
                    "Evening Experience: Farewell family dinner with live mountain music at your luxury resort",
                    "Overnight Stay: Manali (Premium Riverside Luxury Property)",
                    "Meals Included: Breakfast & premium farewell dinner",
                ],
                sort_order=6,
            ),
            ItineraryDayNested(
                day_number=7,
                title="Manali to Chandigarh / Departure",
                description=(
                    "Enjoy your final mountain breakfast on the resort terrace before your private luxury vehicle "
                    "transfers you to Chandigarh Airport or Railway Station with unforgettable Himalayan memories."
                ),
                activities=[
                    "Transfers Included: Private luxury door-to-door station or airport drop-off via Kullu Valley",
                    "Meals Included: Sumptuous buffet breakfast",
                ],
                sort_order=7,
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
                location="Manali (4N)",
                nights_label="04 Nights",
                description="Deluxe riverside resort in Manali.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=5,
            ),
            ItineraryHotelNested(
                name="ManuAllaya Resort & Spa / Similar",
                location="Manali (4N)",
                nights_label="04 Nights",
                description="Premium riverside resort with alpine views.",
                stars=5,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=6,
            ),
            ItineraryHotelNested(
                name="The Himalayan (Castle Resort) / Similar",
                location="Manali (4N)",
                nights_label="04 Nights",
                description="Luxury castle resort on the Beas riverside.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=7,
            ),
            ItineraryHotelNested(
                name="Span Resort & Spa (Elite Presidential) / Similar",
                location="Manali (4N)",
                nights_label="04 Nights",
                description="Ultra-luxury spa resort on the Beas riverside.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Elite Presidential Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=8,
            ),
        ],
        inclusions=[
            ItineraryInclusionNested(
                kind="included",
                text="06 nights premium accommodation at handpicked Shimla and Manali resorts",
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
                text="Airfare or train tickets to and from Chandigarh",
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
    return package, itinerary, HP_013_PEXELS_IMAGES


def build_hp_014(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 15
    package = PackageCreate(
        slug="hp-014-oberoi-himachal-experience",
        destination_id=destination_id,
        title="The Oberoi Himachal Experience — Royalty Reimagined",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="Two nights at The Oberoi Cecil, Shimla — colonial grandeur on the historic Mall Road",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Three nights at Wildflower Hall, Mashobra — cedar forest sanctuary & infinity pool bliss",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Private Kufri excursion with curated picnic amid Himalayan panoramas",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Naldehra golf course heritage walk & Mashobra forest sanctuary trails",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Oberoi spa rituals, forest picnics & bespoke fine dining experiences",
                sort_order=5,
            ),
            PackageHighlightNested(
                text="Private luxury chauffeur with TRAGUIN 24/7 Oberoi concierge coordination",
                sort_order=6,
            ),
        ],
        moods=["Luxury", "Romantic", "Culture"],
    )
    itinerary = ItineraryCreate(
        slug="hp-014-oberoi-himachal-itinerary",
        destination_id=destination_id,
        title="The Oberoi Himachal Experience — Royalty Reimagined",
        duration_label="05 Nights / 06 Days",
        duration_days=6,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Royalty Reimagined in the Himalayas",
        overview=(
            "Experience Himachal Pradesh through the lens of Oberoi hospitality — where colonial heritage "
            "meets cedar-forest sanctuary luxury. Two nights at The Oberoi Cecil in Shimla reveal Mall Road "
            "elegance, Viceregal Lodge grandeur, and Kufri alpine excursions. Three nights at Wildflower Hall "
            "in Mashobra offer infinity pool serenity, Naldehra golf heritage, forest sanctuary walks, and "
            "bespoke Oberoi spa rituals curated exclusively by TRAGUIN."
        ),
        seo_title="HP-014 | Oberoi Himachal Experience | TRAGUIN Ultra-Luxury Tour",
        seo_description=(
            "Ultra-luxury 05 Nights / 06 Days Himachal package (HP-014) at The Oberoi Cecil Shimla and "
            "Wildflower Hall Mashobra with Kufri, Naldehra, and Mashobra experiences. Ideal for luxury, "
            "romantic, and cultural travelers."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="The Oberoi Cecil Colonial Heritage", sort_order=1),
            ItineraryHighlightNested(text="Kufri Alpine Picnic Excursion", sort_order=2),
            ItineraryHighlightNested(text="Wildflower Hall Cedar Sanctuary", sort_order=3),
            ItineraryHighlightNested(text="Naldehra Golf Heritage Walk", sort_order=4),
            ItineraryHighlightNested(text="Oberoi Spa & Forest Picnic", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival at The Oberoi Cecil, Shimla",
                description=(
                    "Your Oberoi Himachal experience begins with a VIP TRAGUIN welcome at Chandigarh Airport "
                    "or Kalka Railway Station. Ascend to Shimla and check into The Oberoi Cecil — a landmark "
                    "of colonial elegance on the historic Mall Road with panoramic valley views."
                ),
                activities=[
                    "Sightseeing Included: Scenic Shivalik foothills drive, Timber Trail valley views en-route",
                    "Evening Experience: Oberoi welcome champagne and curated heritage orientation on Mall Road",
                    "Overnight Stay: Shimla — The Oberoi Cecil (Luxury Heritage Suite)",
                    "Meals Included: Oberoi welcome refreshment & fine dining dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Shimla Heritage & Kufri Excursion",
                description=(
                    "After an Oberoi grand breakfast, explore Shimla's colonial legacy at the Viceregal Lodge, "
                    "Christ Church, and The Ridge. Drive to Kufri for a private curated picnic amid alpine "
                    "panoramas and pine forest trails."
                ),
                activities=[
                    "Sightseeing Included: Viceregal Lodge, The Ridge, Christ Church, Mall Road, Kufri Green Valley",
                    "Evening Experience: Private gourmet picnic setup at Kufri with Himalayan panorama views",
                    "Overnight Stay: Shimla — The Oberoi Cecil (Luxury Heritage Suite)",
                    "Meals Included: Oberoi breakfast, picnic lunch & fine dining dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Shimla to Wildflower Hall, Mashobra",
                description=(
                    "Transfer to Wildflower Hall, An Oberoi Resort — a cedar-forest sanctuary perched above "
                    "Mashobra with sweeping Himalayan views. Settle into your luxury suite and enjoy an "
                    "afternoon at the infinity pool overlooking snow-capped peaks."
                ),
                activities=[
                    "Sightseeing Included: Mashobra cedar forest drive, Craignano Nature Park (optional)",
                    "Evening Experience: Oberoi infinity pool session and sunset aperitif on the terrace",
                    "Overnight Stay: Mashobra — Wildflower Hall, An Oberoi Resort (Luxury Forest Suite)",
                    "Meals Included: Oberoi breakfast & bespoke fine dining dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Naldehra Golf & Mashobra Forest Sanctuary",
                description=(
                    "Walk the historic Naldehra golf course — one of the oldest in India — lined with towering "
                    "cedar trees. Explore Mashobra forest sanctuary trails on a guided nature walk before an "
                    "Oberoi spa ritual and forest picnic lunch in a secluded cedar glade."
                ),
                activities=[
                    "Sightseeing Included: Naldehra golf course heritage walk, Mashobra forest sanctuary trails",
                    "Evening Experience: Oberoi signature spa ritual and private forest gourmet picnic",
                    "Overnight Stay: Mashobra — Wildflower Hall, An Oberoi Resort (Luxury Forest Suite)",
                    "Meals Included: Oberoi breakfast, forest picnic lunch & fine dining dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="Wildflower Hall Leisure & Wellness Day",
                description=(
                    "A day of unhurried Oberoi luxury. Enjoy a morning yoga session on the terrace, explore "
                    "the resort's private forest trails, indulge in a couples spa treatment, and savor a "
                    "bespoke chef's tasting menu for your farewell evening."
                ),
                activities=[
                    "Sightseeing Included: Private forest trail walk, Mashobra apple orchard visit (seasonal)",
                    "Evening Experience: Oberoi farewell chef's tasting menu with wine pairing on the terrace",
                    "Overnight Stay: Mashobra — Wildflower Hall, An Oberoi Resort (Luxury Forest Suite)",
                    "Meals Included: Oberoi breakfast & farewell tasting menu dinner",
                ],
                sort_order=5,
            ),
            ItineraryDayNested(
                day_number=6,
                title="Wildflower Hall to Chandigarh / Departure",
                description=(
                    "Enjoy a final Oberoi breakfast amid cedar forests before your private luxury vehicle "
                    "transfers you to Chandigarh Airport or Kalka Railway Station with memories of Himalayan "
                    "royalty reimagined."
                ),
                activities=[
                    "Transfers Included: Private luxury door-to-door station or airport drop-off",
                    "Meals Included: Oberoi grand buffet breakfast",
                ],
                sort_order=6,
            ),
        ],
        hotels=[
            ItineraryHotelNested(
                name="Hotel Willow Banks / Similar",
                location="Shimla (2N)",
                nights_label="02 Nights",
                description="Deluxe mountain resort alternative in Shimla.",
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
                name="The Oberoi Cecil, Shimla / Similar",
                location="Shimla (2N)",
                nights_label="02 Nights",
                description="Luxury colonial heritage hotel on Mall Road.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Heritage Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=3,
            ),
            ItineraryHotelNested(
                name="The Oberoi Cecil — Presidential Suite / Similar",
                location="Shimla (2N)",
                nights_label="02 Nights",
                description="Ultra-luxury presidential suite with Mall Road panoramas.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Presidential Heritage Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=4,
            ),
            ItineraryHotelNested(
                name="Marigold Sarovar Portico Mashobra / Similar",
                location="Mashobra (3N)",
                nights_label="03 Nights",
                description="Deluxe cedar-forest resort near Mashobra.",
                stars=4,
                category_label="Deluxe",
                room_type="Forest View Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=5,
            ),
            ItineraryHotelNested(
                name="Royal Tulip Shimla / Similar",
                location="Mashobra (3N)",
                nights_label="03 Nights",
                description="Premium hill resort with cedar forest access.",
                stars=4,
                category_label="Premium",
                room_type="Premium Forest Suite",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=6,
            ),
            ItineraryHotelNested(
                name="Wildflower Hall, An Oberoi Resort / Similar",
                location="Mashobra (3N)",
                nights_label="03 Nights",
                description="Luxury cedar-forest sanctuary with infinity pool.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Forest Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=7,
            ),
            ItineraryHotelNested(
                name="Wildflower Hall — Oberoi Luxury Villa / Similar",
                location="Mashobra (3N)",
                nights_label="03 Nights",
                description="Ultra-luxury private villa with butler service and spa access.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Private Luxury Villa",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=8,
            ),
        ],
        inclusions=[
            ItineraryInclusionNested(
                kind="included",
                text="05 nights at Oberoi-calibre luxury properties in Shimla and Mashobra",
                sort_order=1,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Daily Oberoi breakfasts and bespoke fine dining dinners (MAPAI plan)",
                sort_order=2,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Private chauffeur-driven luxury sedan for all transfers and sightseeing",
                sort_order=3,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="TRAGUIN 24/7 dedicated elite guest relationship manager with Oberoi coordination",
                sort_order=4,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Private Kufri gourmet picnic setup and Mashobra forest picnic experience",
                sort_order=5,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Driver allowances, tolls, parking, fuel, and applicable taxes",
                sort_order=6,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Airfare or train tickets to and from Chandigarh / Kalka",
                sort_order=7,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Oberoi spa treatments, golf green fees, and premium wine pairings",
                sort_order=8,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Monument entry tickets and Viceregal Lodge camera permits",
                sort_order=9,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Personal expenses such as laundry, phone calls, and tipping",
                sort_order=10,
            ),
        ],
    )
    return package, itinerary, HP_014_PEXELS_IMAGES


def build_hp_015(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 16
    package = PackageCreate(
        slug="hp-015-corporate-himachal-mice",
        destination_id=destination_id,
        title="Corporate Himachal — Elevation, Leadership & Synergy",
        duration_label="03 Nights / 04 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="State-of-the-art conference facilities with mountain-view presentation halls in Shimla",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Curated team-building challenges at Kufri meadows & Mashobra forest ropes course",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Executive networking cocktail terrace with sunset Himalayan panoramas",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Gala dinner ballroom with live entertainment and bespoke corporate branding",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Leadership workshop modules amid cedar forests — elevation meets inspiration",
                sort_order=5,
            ),
            PackageHighlightNested(
                text="Dedicated MICE event manager with TRAGUIN 24/7 corporate concierge support",
                sort_order=6,
            ),
        ],
        moods=["Corporate", "Luxury", "Culture"],
    )
    itinerary = ItineraryCreate(
        slug="hp-015-corporate-himachal-itinerary",
        destination_id=destination_id,
        title="Corporate Himachal — Elevation, Leadership & Synergy",
        duration_label="03 Nights / 04 Days",
        duration_days=4,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Elevation, Leadership & Synergy",
        overview=(
            "TRAGUIN's Corporate Himachal MICE retreat transforms Shimla's mountain grandeur into a catalyst "
            "for leadership, team synergy, and strategic alignment. Three nights at a premium convention resort "
            "feature state-of-the-art conference halls, curated team-building at Kufri and Mashobra, executive "
            "networking cocktails, and a gala dinner ballroom — all with dedicated MICE event management and "
            "24/7 corporate concierge support."
        ),
        seo_title="HP-015 | Corporate Himachal MICE Retreat | TRAGUIN Premium Events",
        seo_description=(
            "Premium 03 Nights / 04 Days corporate MICE package (HP-015) in Shimla with conference facilities, "
            "team-building at Kufri and Mashobra, gala dinner, and executive networking. Ideal for corporate "
            "retreats, leadership offsites, and incentive travel."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Mountain-View Conference Hall", sort_order=1),
            ItineraryHighlightNested(text="Kufri Team-Building Challenge", sort_order=2),
            ItineraryHighlightNested(text="Mashobra Leadership Workshop", sort_order=3),
            ItineraryHighlightNested(text="Executive Networking Cocktail", sort_order=4),
            ItineraryHighlightNested(text="Gala Dinner Ballroom Event", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival & Conference Kickoff, Shimla",
                description=(
                    "Your corporate retreat begins with a professional TRAGUIN welcome at Chandigarh Airport "
                    "or Railway Station. Transfer to your premium convention resort in Shimla, check in, and "
                    "commence the opening conference session in a state-of-the-art mountain-view presentation hall."
                ),
                activities=[
                    "Conference Included: Welcome address, opening keynote session, and breakout room allocation",
                    "Evening Experience: Executive networking cocktail on the terrace with Himalayan sunset views",
                    "Overnight Stay: Shimla (Premium Convention Resort)",
                    "Meals Included: Working lunch, coffee breaks & welcome dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Team Building at Kufri & Mashobra",
                description=(
                    "A full day of curated outdoor team-building activities. Morning challenges at Kufri meadows "
                    "include group adventure races and collaborative problem-solving. Afternoon leadership "
                    "workshop modules amid Mashobra's cedar forests with ropes course elements."
                ),
                activities=[
                    "Team Building Included: Kufri group adventure challenge, Mashobra forest ropes course, leadership workshop modules",
                    "Evening Experience: Debrief session and team celebration dinner with live mountain music",
                    "Overnight Stay: Shimla (Premium Convention Resort)",
                    "Meals Included: Breakfast, outdoor BBQ lunch & celebration dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Strategy Sessions & Gala Dinner",
                description=(
                    "Morning strategy and alignment sessions in the conference hall with dedicated AV support "
                    "and breakout rooms. Afternoon free time for Mall Road networking walks. Evening gala dinner "
                    "in the resort ballroom with bespoke corporate branding and live entertainment."
                ),
                activities=[
                    "Conference Included: Strategy alignment sessions, breakout workshops, closing presentations",
                    "Evening Experience: Gala dinner ballroom event with live entertainment and awards ceremony",
                    "Overnight Stay: Shimla (Premium Convention Resort)",
                    "Meals Included: Breakfast, working lunch & gala dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Shimla to Chandigarh / Departure",
                description=(
                    "Enjoy a final breakfast and closing remarks before your private luxury coaches transfer "
                    "the team to Chandigarh Airport or Railway Station with renewed synergy and leadership clarity."
                ),
                activities=[
                    "Transfers Included: Private luxury coach or sedan fleet to Chandigarh Airport / Railway Station",
                    "Meals Included: Sumptuous buffet breakfast",
                ],
                sort_order=4,
            ),
        ],
        hotels=[
            ItineraryHotelNested(
                name="Hotel Combermere / Similar",
                location="Shimla (3N)",
                nights_label="03 Nights",
                description="Deluxe convention hotel with meeting rooms in Shimla.",
                stars=3,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=1,
            ),
            ItineraryHotelNested(
                name="Radisson Hotel Shimla / Similar",
                location="Shimla (3N)",
                nights_label="03 Nights",
                description="Premium hill resort with conference facilities.",
                stars=4,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=2,
            ),
            ItineraryHotelNested(
                name="The Cecil — Oberoi / Similar",
                location="Shimla (3N)",
                nights_label="03 Nights",
                description="Luxury heritage hotel with ballroom event space.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=3,
            ),
            ItineraryHotelNested(
                name="Wildflower Hall, An Oberoi Resort / Similar",
                location="Shimla (3N)",
                nights_label="03 Nights",
                description="Ultra-luxury resort with private conference pavilion.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Luxury Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=4,
            ),
        ],
        inclusions=[
            ItineraryInclusionNested(
                kind="included",
                text="03 nights premium convention resort accommodation in Shimla for all delegates",
                sort_order=1,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Daily breakfasts, working lunches, coffee breaks, and gala dinner (MAPAI plan)",
                sort_order=2,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="State-of-the-art conference hall with AV equipment, breakout rooms, and Wi-Fi",
                sort_order=3,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Dedicated TRAGUIN MICE event manager and 24/7 corporate concierge support",
                sort_order=4,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Curated Kufri team-building and Mashobra leadership workshop with professional facilitators",
                sort_order=5,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Private luxury coach or sedan fleet transfers from Chandigarh and all local sightseeing",
                sort_order=6,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Airfare or train tickets to and from Chandigarh for delegates",
                sort_order=7,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Gala dinner premium branding, custom staging, and live entertainment upgrades",
                sort_order=8,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Alcoholic beverages beyond welcome cocktail reception",
                sort_order=9,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Personal expenses, laundry, and individual tipping",
                sort_order=10,
            ),
        ],
    )
    return package, itinerary, HP_015_PEXELS_IMAGES


def build_hp_017(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 17
    package = PackageCreate(
        slug="hp-017-dharamshala-escape",
        destination_id=destination_id,
        title="Dharamshala Escape — Serenity, Spirituality & Peaks",
        duration_label="04 Nights / 05 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="Four-night Dharamshala base — Dhauladhar peaks, deodar forests & spiritual serenity",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="McLeodganj Little Lhasa — Dalai Lama Temple, Tibetan markets & momo culture",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Naddi View Point sunset panoramas over the Dhauladhar range",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Bhagsunag Waterfall forest trail & St. John in the Wilderness Church",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Palampur tea estate walk with artisanal tea tasting in Kangra Valley",
                sort_order=5,
            ),
            PackageHighlightNested(
                text="Private Innova Crysta with TRAGUIN 24/7 elite concierge throughout",
                sort_order=6,
            ),
        ],
        moods=["Family", "Culture", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="hp-017-dharamshala-itinerary",
        destination_id=destination_id,
        title="Dharamshala Escape — Serenity, Spirituality & Peaks",
        duration_label="04 Nights / 05 Days",
        duration_days=5,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Serenity, Spirituality & Peaks",
        overview=(
            "TRAGUIN's Dharamshala Escape is a four-night immersion in the spiritual heart of the Kangra Valley. "
            "From the Tibetan monasteries and bustling markets of McLeodganj to Naddi's Dhauladhar sunset panoramas, "
            "Bhagsunag's forest waterfall, and Palampur's lush tea terraces — this bespoke journey offers premium "
            "valley resorts, curated cultural experiences, and the tranquil pace of Himalayan village life."
        ),
        seo_title="HP-017 | Dharamshala Escape | TRAGUIN Premium Kangra Valley Tour",
        seo_description=(
            "Luxury 04 Nights / 05 Days Dharamshala package (HP-017) covering McLeodganj, Naddi, Bhagsunag, "
            "Dal Lake, HPCA Stadium, and Palampur tea estates with premium stays and private transfers. "
            "Ideal for families, culture seekers, and nature lovers."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="McLeodganj & Dalai Lama Temple", sort_order=1),
            ItineraryHighlightNested(text="Naddi Dhauladhar Sunset Views", sort_order=2),
            ItineraryHighlightNested(text="Bhagsunag Waterfall Trail", sort_order=3),
            ItineraryHighlightNested(text="Palampur Tea Estate Walk", sort_order=4),
            ItineraryHighlightNested(text="HPCA Cricket Stadium Panorama", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival in Chandigarh to Dharamshala",
                description=(
                    "Your Dharamshala escape begins with a warm TRAGUIN welcome at Chandigarh Airport or "
                    "Railway Station. Drive through Kangra Valley's terraced farms and tea gardens to "
                    "Dharamshala, checking into your premium luxury valley resort beneath the Dhauladhar range."
                ),
                activities=[
                    "Sightseeing Included: Kangra Valley scenic drive, terraced farm vistas, Dharamshala town orientation",
                    "Evening Experience: Welcome dinner with Dhauladhar mountain sunset views from your resort terrace",
                    "Overnight Stay: Dharamshala (Premium Luxury Valley Resort)",
                    "Meals Included: Welcome refreshment & luxury dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="McLeodganj & Tibetan Culture Day",
                description=(
                    "Explore McLeodganj — Little Lhasa — home of His Holiness the Dalai Lama. Visit the serene "
                    "Tsuglagkhang Complex, browse Tibetan markets for thangka paintings and singing bowls, and "
                    "savor authentic momos at a curated local eatery."
                ),
                activities=[
                    "Sightseeing Included: Dalai Lama Temple (Tsuglagkhang), Tibetan market, Bhagsunag Temple, Dal Lake, St. John Church",
                    "Evening Experience: Curated Tibetan momo tasting and thangka painting gallery visit",
                    "Overnight Stay: Dharamshala (Premium Luxury Valley Resort)",
                    "Meals Included: Premium breakfast & authentic mountain dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Naddi View Point & Bhagsunag Waterfall",
                description=(
                    "Drive to Naddi View Point for sweeping Dhauladhar panoramas at sunset. Walk the forest "
                    "trail to Bhagsunag Waterfall and explore Dharamkot village's peaceful wellness cafes "
                    "above McLeodganj."
                ),
                activities=[
                    "Sightseeing Included: Naddi View Point, Bhagsunag Waterfall forest trail, Dharamkot village, HPCA Cricket Stadium view",
                    "Evening Experience: Sunset photography session at Naddi with premium hot beverage service",
                    "Overnight Stay: Dharamshala (Premium Luxury Valley Resort)",
                    "Meals Included: Breakfast & multi-cuisine dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Palampur Tea Estate Excursion",
                description=(
                    "A curated day in Palampur — the tea capital of Kangra Valley. Walk through lush green "
                    "tea terraces, enjoy an artisanal tea tasting session at a heritage estate, and visit "
                    "Baijnath Shiva Temple before a farewell dinner at your resort."
                ),
                activities=[
                    "Sightseeing Included: Palampur tea plantation walk, artisanal tea tasting, Baijnath Shiva Temple, Andretta Artist Village (optional)",
                    "Evening Experience: Farewell dinner with live mountain music at your luxury resort",
                    "Overnight Stay: Dharamshala (Premium Luxury Valley Resort)",
                    "Meals Included: Breakfast, estate lunch & premium farewell dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="Dharamshala to Chandigarh / Departure",
                description=(
                    "Enjoy your final mountain breakfast before your private luxury vehicle transfers you "
                    "to Chandigarh Airport or Railway Station with serene memories of the Kangra Valley."
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
                name="Pride Elite Dharamshala / Similar",
                location="Dharamshala (4N)",
                nights_label="04 Nights",
                description="Deluxe valley resort in Dharamshala.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=1,
            ),
            ItineraryHotelNested(
                name="Fortune Park Moksha / Similar",
                location="Dharamshala (4N)",
                nights_label="04 Nights",
                description="Premium resort with Dhauladhar valley views.",
                stars=4,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=2,
            ),
            ItineraryHotelNested(
                name="The Pavilion by HPCA / Hyatt Regency / Similar",
                location="Dharamshala (4N)",
                nights_label="04 Nights",
                description="Luxury resort overlooking the Kangra Valley.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=3,
            ),
            ItineraryHotelNested(
                name="Radisson Blu Resort Dharamshala / Similar",
                location="Dharamshala (4N)",
                nights_label="04 Nights",
                description="Ultra-luxury resort beneath the Dhauladhar range.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Luxury Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=4,
            ),
        ],
        inclusions=[
            ItineraryInclusionNested(
                kind="included",
                text="04 nights premium accommodation at handpicked Dharamshala valley resorts",
                sort_order=1,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Daily lavish breakfasts and multi-cuisine dinners (MAPAI plan)",
                sort_order=2,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Private chauffeur-driven AC Innova Crysta for all transfers and sightseeing",
                sort_order=3,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="TRAGUIN 24/7 dedicated elite guest relationship manager assistance",
                sort_order=4,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Palampur tea estate walk with artisanal tea tasting session",
                sort_order=5,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Driver allowances, tolls, parking, fuel, and applicable taxes",
                sort_order=6,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Airfare or train tickets to and from Chandigarh",
                sort_order=7,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Monument entry tickets, monastery donations, and local guide fees",
                sort_order=8,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Personal expenses such as laundry, phone calls, and tipping",
                sort_order=9,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Tibetan handicraft purchases and optional wellness spa treatments",
                sort_order=10,
            ),
        ],
    )
    return package, itinerary, HP_017_PEXELS_IMAGES


def build_hp_018(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 18
    package = PackageCreate(
        slug="hp-018-shimla-kasol-delight",
        destination_id=destination_id,
        title="Shimla Kasol Delight — The Royal Ridge to the Mystic Valley",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="Colonial Shimla elegance — Jakhoo Hanuman statue, Ridge & Mall Road heritage walk",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Kasol bohemian paradise — Parvati River, pine forests & Israeli cafe culture",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Manikaran Sahib Gurudwara hot springs beside the sacred Parvati River",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Tosh village alpine trek & Chalal suspension bridge forest trail",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Jibhi waterfall walk through ancient cedar forests (optional extension)",
                sort_order=5,
            ),
            PackageHighlightNested(
                text="Private Innova Crysta with TRAGUIN 24/7 elite concierge throughout",
                sort_order=6,
            ),
        ],
        moods=["Family", "Adventure", "Culture"],
    )
    itinerary = ItineraryCreate(
        slug="hp-018-shimla-kasol-itinerary",
        destination_id=destination_id,
        title="Shimla Kasol Delight — The Royal Ridge to the Mystic Valley",
        duration_label="05 Nights / 06 Days",
        duration_days=6,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="The Royal Ridge to the Mystic Valley",
        overview=(
            "TRAGUIN's Shimla Kasol Delight bridges two worlds — colonial Shimla's royal ridge elegance and "
            "Kasol's mystic Parvati Valley bohemian charm. Two nights amid Shimla's heritage architecture "
            "and Jakhoo panoramas lead to three nights in Kasol exploring Manikaran's sacred hot springs, "
            "Tosh village alpine trails, and Chalal's riverside suspension bridge — with premium stays, "
            "riverside bonfires, and private chauffeur transfers throughout."
        ),
        seo_title="HP-018 | Shimla Kasol Delight | TRAGUIN Premium Parvati Valley Tour",
        seo_description=(
            "Luxury 05 Nights / 06 Days package (HP-018) covering Shimla, Kasol, Manikaran, Tosh, Chalal, "
            "and Jibhi with premium stays and private transfers. Ideal for families, adventure seekers, "
            "and culture enthusiasts."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Shimla Heritage & Jakhoo Panoramas", sort_order=1),
            ItineraryHighlightNested(text="Kasol Parvati River Valley", sort_order=2),
            ItineraryHighlightNested(text="Manikaran Sahib Hot Springs", sort_order=3),
            ItineraryHighlightNested(text="Tosh Village Alpine Trek", sort_order=4),
            ItineraryHighlightNested(text="Chalal Suspension Bridge Trail", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival in Chandigarh to Shimla",
                description=(
                    "Your Royal Ridge to Mystic Valley journey begins with a TRAGUIN welcome at Chandigarh "
                    "Airport or Railway Station. Ascend through the Shivalik foothills to Shimla and check "
                    "into your premium heritage resort for a relaxing mountain evening."
                ),
                activities=[
                    "Sightseeing Included: Scenic Himalayan foothills drive, Timber Trail valley views en-route",
                    "Evening Experience: Private welcome dinner and heritage walk briefing on Mall Road",
                    "Overnight Stay: Shimla (Premium Luxury Heritage Resort)",
                    "Meals Included: Welcome refreshment & luxury dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Shimla Heritage & Jakhoo Excursion",
                description=(
                    "Explore Shimla's colonial legacy at Christ Church, The Ridge, and Mall Road. Ride the "
                    "heritage toy train segment (optional) or drive to Jakhoo Hill for the towering Hanuman "
                    "statue and sweeping town panoramas."
                ),
                activities=[
                    "Sightseeing Included: Christ Church, The Ridge, Mall Road, Jakhoo Hanuman statue, Scandal Point",
                    "Optional Activities: Heritage toy train ride to Tara Devi or Viceregal Lodge visit",
                    "Overnight Stay: Shimla (Premium Luxury Heritage Resort)",
                    "Meals Included: Premium breakfast & dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Shimla to Kasol via Bhuntar",
                description=(
                    "Descend from Shimla through Mandi and Bhuntar into the mystical Parvati Valley. Follow "
                    "the Parvati River to Kasol — India's bohemian hub — and check into your premium riverside "
                    "lodge amid pine forests."
                ),
                activities=[
                    "Sightseeing Included: Mandi town, Bhuntar confluence, Parvati River valley drive, Kasol market stroll",
                    "Evening Experience: Riverside bonfire with live acoustic music at your Kasol lodge",
                    "Overnight Stay: Kasol (Premium Parvati Valley Riverside Lodge)",
                    "Meals Included: Breakfast & riverside dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Manikaran Sahib & Kasol Exploration",
                description=(
                    "Visit the sacred Manikaran Sahib Gurudwara with its natural hot springs beside the Parvati "
                    "River. Return to Kasol for cafe hopping, explore the Chalal village suspension bridge trail, "
                    "and enjoy the bohemian market culture."
                ),
                activities=[
                    "Sightseeing Included: Manikaran Sahib Gurudwara, hot springs, Chalal village bridge trail, Kasol market",
                    "Evening Experience: Curated Israeli cafe dinner and riverside stargazing",
                    "Overnight Stay: Kasol (Premium Parvati Valley Riverside Lodge)",
                    "Meals Included: Breakfast & multi-cuisine dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="Tosh Village & Jibhi Excursion",
                description=(
                    "A day of alpine adventure. Trek or drive to Tosh village perched above the Parvati Valley "
                    "with traditional wooden houses and snow peaks. Optional extension to Jibhi's ancient cedar "
                    "forest waterfall walk before a farewell riverside dinner."
                ),
                activities=[
                    "Sightseeing Included: Tosh village alpine trail, Parvati Valley panoramas, Jibhi waterfall walk (optional)",
                    "Evening Experience: Farewell riverside bonfire dinner with Parvati Valley night sky views",
                    "Overnight Stay: Kasol (Premium Parvati Valley Riverside Lodge)",
                    "Meals Included: Breakfast, packed lunch & premium farewell dinner",
                ],
                sort_order=5,
            ),
            ItineraryDayNested(
                day_number=6,
                title="Kasol to Chandigarh / Departure",
                description=(
                    "Enjoy your final mountain breakfast beside the Parvati River before your private luxury "
                    "vehicle transfers you to Chandigarh Airport or Railway Station."
                ),
                activities=[
                    "Transfers Included: Private luxury door-to-door station or airport drop-off via Bhuntar",
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
                name="Hotel Sandhya Kasol / Similar",
                location="Kasol (3N)",
                nights_label="03 Nights",
                description="Deluxe riverside lodge in Kasol.",
                stars=3,
                category_label="Deluxe",
                room_type="Riverside Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=5,
            ),
            ItineraryHotelNested(
                name="Parvati Kuteer / Similar",
                location="Kasol (3N)",
                nights_label="03 Nights",
                description="Premium cottage resort along the Parvati River.",
                stars=4,
                category_label="Premium",
                room_type="Premium Cottage",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=6,
            ),
            ItineraryHotelNested(
                name="The Himalayan Village Kasol / Similar",
                location="Kasol (3N)",
                nights_label="03 Nights",
                description="Luxury boutique lodge with Parvati Valley views.",
                stars=4,
                category_label="Luxury",
                room_type="Luxury Valley Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=7,
            ),
            ItineraryHotelNested(
                name="Whoopers Hostel & Cottages Premium / Similar",
                location="Kasol (3N)",
                nights_label="03 Nights",
                description="Ultra-luxury private cottage with riverside deck and bonfire pit.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Private Luxury Cottage",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=8,
            ),
        ],
        inclusions=[
            ItineraryInclusionNested(
                kind="included",
                text="05 nights premium accommodation at handpicked Shimla and Kasol properties",
                sort_order=1,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Daily lavish breakfasts and multi-cuisine dinners (MAPAI plan)",
                sort_order=2,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Private chauffeur-driven AC Innova Crysta for all transfers and sightseeing",
                sort_order=3,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="TRAGUIN 24/7 dedicated elite guest relationship manager assistance",
                sort_order=4,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Private riverside bonfire evening with music in Kasol",
                sort_order=5,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Driver allowances, tolls, parking, fuel, and applicable taxes",
                sort_order=6,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Airfare or train tickets to and from Chandigarh",
                sort_order=7,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Heritage toy train tickets, monument entry fees, and local guide charges",
                sort_order=8,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Tosh village trek pony hire and adventure activity fees",
                sort_order=9,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Personal expenses such as laundry, phone calls, and tipping",
                sort_order=10,
            ),
        ],
    )
    return package, itinerary, HP_018_PEXELS_IMAGES


def build_hp_019(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 19
    package = PackageCreate(
        slug="hp-019-manali-dharamshala-family",
        destination_id=destination_id,
        title="Manali & Dharamshala Family Explorer",
        duration_label="06 Nights / 07 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="Three-night Manali riverside base — Hadimba Temple, Solang Valley & Old Manali cafes",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Solang Valley cable car, paragliding & snow meadow family adventures",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Three-night Dharamshala valley retreat — McLeodganj, Naddi & Bhagsunag",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Ancient Kangra Fort heritage walk overlooking the Kangra Valley",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Palampur tea tasting & Tibetan market shopping in McLeodganj",
                sort_order=5,
            ),
            PackageHighlightNested(
                text="Private Innova Crysta with TRAGUIN 24/7 family concierge throughout",
                sort_order=6,
            ),
        ],
        moods=["Family", "Luxury", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="hp-019-manali-dharamshala-itinerary",
        destination_id=destination_id,
        title="Manali & Dharamshala Family Explorer",
        duration_label="06 Nights / 07 Days",
        duration_days=7,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Alpine Adventure Meets Spiritual Serenity",
        overview=(
            "TRAGUIN's Manali & Dharamshala Family Explorer combines alpine adventure with spiritual serenity "
            "across two of Himachal's most beloved destinations. Three nights in Manali offer Solang Valley "
            "thrills, Hadimba Temple heritage, and riverside leisure. Three nights in Dharamshala reveal "
            "McLeodganj's Tibetan culture, Naddi's Dhauladhar panoramas, Kangra Fort's ancient grandeur, "
            "and Palampur tea estates — all with premium family-friendly resorts and private chauffeur transfers."
        ),
        seo_title="HP-019 | Manali Dharamshala Family Explorer | TRAGUIN Premium Family Tour",
        seo_description=(
            "Luxury 06 Nights / 07 Days family package (HP-019) covering Manali, Solang Valley, Dharamshala, "
            "McLeodganj, Kangra Fort, and Palampur with premium stays and private transfers. Ideal for "
            "multi-generational families and luxury nature lovers."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Manali Heritage & Solang Adventure", sort_order=1),
            ItineraryHighlightNested(text="Kullu Valley Scenic Transfer", sort_order=2),
            ItineraryHighlightNested(text="McLeodganj & Dalai Lama Temple", sort_order=3),
            ItineraryHighlightNested(text="Kangra Fort Heritage Walk", sort_order=4),
            ItineraryHighlightNested(text="Palampur Tea Estate Tasting", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival in Chandigarh to Manali",
                description=(
                    "Your family Himalayan adventure begins with a warm TRAGUIN welcome at Chandigarh Airport "
                    "or Railway Station. Drive through the spectacular Kullu Valley along the Beas River to "
                    "Manali and check into your premium riverside luxury resort."
                ),
                activities=[
                    "Sightseeing Included: Kullu Valley drive, Pandoh Dam, Sundernagar Lake, Beas River panoramas",
                    "Evening Experience: Private family welcome dinner and riverside bonfire at your resort",
                    "Overnight Stay: Manali (Premium Riverside Luxury Property)",
                    "Meals Included: Welcome refreshment & luxury dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Manali Local Sightseeing",
                description=(
                    "Immerse the family in Manali's cultural tapestry. Visit the ancient Hadimba Devi Temple "
                    "in a deodar forest, explore Vashisht's therapeutic hot sulphur springs, and spend the "
                    "evening shopping and cafe hopping on Manali Mall Road."
                ),
                activities=[
                    "Sightseeing Included: Hadimba Temple, Club House, Vashisht Hot Springs, Tibetan Monastery, Manali Mall Road",
                    "Evening Experience: Family trout dining and Old Manali cafe recommendations",
                    "Overnight Stay: Manali (Premium Riverside Luxury Property)",
                    "Meals Included: Premium breakfast & buffet dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Solang Valley Family Adventure",
                description=(
                    "An exhilarating family day at Solang Valley. Ride the open gondola cable car to Mount "
                    "Phatru for glacier panoramas and enjoy age-appropriate adventures like zorbing, quad "
                    "biking, or snow play in the meadows."
                ),
                activities=[
                    "Sightseeing Included: Solang Valley meadows, cable car ride, snow line views, Palchan Village",
                    "Optional Activities: Family paragliding, zorbing, quad biking, or ski hire (seasonal)",
                    "Overnight Stay: Manali (Premium Riverside Luxury Property)",
                    "Meals Included: Breakfast & multi-cuisine chef's special dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Manali to Dharamshala via Kangra Fort",
                description=(
                    "After breakfast, drive toward Dharamshala through the Kangra Valley. Stop at the ancient "
                    "Kangra Fort — one of India's oldest hill forts — for a family heritage walk with sweeping "
                    "valley views before checking into your premium Dharamshala resort."
                ),
                activities=[
                    "Sightseeing Included: Kangra Fort heritage walk, Kangra Valley panoramas, Dharamshala town orientation",
                    "Evening Experience: Welcome dinner with Dhauladhar sunset views from your resort terrace",
                    "Overnight Stay: Dharamshala (Premium Luxury Valley Resort)",
                    "Meals Included: Breakfast & luxury dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="McLeodganj & Tibetan Culture Day",
                description=(
                    "Explore McLeodganj — Little Lhasa — with the family. Visit the Dalai Lama Temple complex, "
                    "walk to Bhagsunag Waterfall, see St. John in the Wilderness Church, and browse Tibetan "
                    "markets for singing bowls, thangka paintings, and momos."
                ),
                activities=[
                    "Sightseeing Included: Dalai Lama Temple, Bhagsunag Waterfall, Dal Lake, St. John Church, Tibetan market",
                    "Evening Experience: Family momo tasting and thangka painting gallery visit in McLeodganj",
                    "Overnight Stay: Dharamshala (Premium Luxury Valley Resort)",
                    "Meals Included: Breakfast & authentic mountain dinner",
                ],
                sort_order=5,
            ),
            ItineraryDayNested(
                day_number=6,
                title="Palampur Tea Estate & Naddi Views",
                description=(
                    "A curated family day in Palampur's tea country with an estate walk and artisanal tea "
                    "tasting. Return via Naddi View Point for Dhauladhar sunset panoramas and a farewell "
                    "family dinner at your resort."
                ),
                activities=[
                    "Sightseeing Included: Palampur tea plantation walk, artisanal tea tasting, Naddi View Point, HPCA Cricket Stadium view",
                    "Evening Experience: Farewell family dinner with live mountain music at your luxury resort",
                    "Overnight Stay: Dharamshala (Premium Luxury Valley Resort)",
                    "Meals Included: Breakfast, estate lunch & premium farewell dinner",
                ],
                sort_order=6,
            ),
            ItineraryDayNested(
                day_number=7,
                title="Dharamshala to Chandigarh / Departure",
                description=(
                    "Enjoy your final mountain breakfast before your private luxury vehicle transfers the "
                    "family to Chandigarh Airport or Railway Station with unforgettable Himalayan memories."
                ),
                activities=[
                    "Transfers Included: Private luxury door-to-door station or airport drop-off",
                    "Meals Included: Sumptuous buffet breakfast",
                ],
                sort_order=7,
            ),
        ],
        hotels=[
            ItineraryHotelNested(
                name="Solang Valley Resort / Similar",
                location="Manali (3N)",
                nights_label="03 Nights",
                description="Deluxe riverside resort in Manali.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=1,
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
                sort_order=2,
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
                sort_order=3,
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
                sort_order=4,
            ),
            ItineraryHotelNested(
                name="Pride Elite Dharamshala / Similar",
                location="Dharamshala (3N)",
                nights_label="03 Nights",
                description="Deluxe valley resort in Dharamshala.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=5,
            ),
            ItineraryHotelNested(
                name="Fortune Park Moksha / Similar",
                location="Dharamshala (3N)",
                nights_label="03 Nights",
                description="Premium resort with Dhauladhar valley views.",
                stars=4,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=6,
            ),
            ItineraryHotelNested(
                name="The Pavilion by HPCA / Hyatt Regency / Similar",
                location="Dharamshala (3N)",
                nights_label="03 Nights",
                description="Luxury resort overlooking the Kangra Valley.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=7,
            ),
            ItineraryHotelNested(
                name="Radisson Blu Resort Dharamshala / Similar",
                location="Dharamshala (3N)",
                nights_label="03 Nights",
                description="Ultra-luxury resort beneath the Dhauladhar range.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Luxury Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=8,
            ),
        ],
        inclusions=[
            ItineraryInclusionNested(
                kind="included",
                text="06 nights premium family accommodation at handpicked Manali and Dharamshala resorts",
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
                text="Palampur tea estate walk with family artisanal tea tasting session",
                sort_order=5,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Driver allowances, tolls, parking, fuel, and applicable taxes",
                sort_order=6,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Airfare or train tickets to and from Chandigarh",
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
                text="Kangra Fort guide fees and optional toy train or pony ride charges",
                sort_order=10,
            ),
        ],
    )
    return package, itinerary, HP_019_PEXELS_IMAGES


def build_hp_020(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 20
    package = PackageCreate(
        slug="hp-020-himachal-panorama",
        destination_id=destination_id,
        title="Himachal Panorama — The Ultimate Luxury Alpine Journey",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="Grand four-destination circuit — Shimla, Manali, Dharamshala & Dalhousie in one journey",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Colonial Shimla heritage — Viceregal Lodge, Ridge & Kufri alpine panoramas",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Manali riverside luxury — Solang Valley, Hadimba Temple & Atal Tunnel excursion",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Dharamshala spiritual serenity — McLeodganj monasteries & Dhauladhar peaks",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Dalhousie colonial charm & Khajjiar — India's Mini Switzerland meadow and lake",
                sort_order=5,
            ),
            PackageHighlightNested(
                text="Private Innova Crysta with TRAGUIN 24/7 elite concierge across the full circuit",
                sort_order=6,
            ),
        ],
        moods=["Family", "Luxury", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="hp-020-himachal-panorama-itinerary",
        destination_id=destination_id,
        title="Himachal Panorama — The Ultimate Luxury Alpine Journey",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="The Ultimate Luxury Alpine Journey",
        overview=(
            "TRAGUIN's Himachal Panorama is the definitive luxury circuit spanning four of Himachal Pradesh's "
            "most iconic destinations. From colonial Shimla's heritage elegance through Manali's alpine adventure, "
            "Dharamshala's spiritual serenity, to Dalhousie's colonial lanes and Khajjiar's Mini Switzerland "
            "meadow — this eight-day bespoke journey delivers premium resorts, gourmet MAPAI dining, and private "
            "chauffeur transfers across the complete Himalayan panorama."
        ),
        seo_title="HP-020 | Himachal Panorama | TRAGUIN Ultimate Luxury Circuit Tour",
        seo_description=(
            "Ultra-luxury 07 Nights / 08 Days Himachal package (HP-020) covering Shimla, Manali, Dharamshala, "
            "Dalhousie, and Khajjiar with premium stays and private transfers. The ultimate family luxury "
            "circuit across Himachal Pradesh."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Shimla Colonial Heritage & Kufri", sort_order=1),
            ItineraryHighlightNested(text="Manali Solang & Riverside Leisure", sort_order=2),
            ItineraryHighlightNested(text="Dharamshala & McLeodganj Serenity", sort_order=3),
            ItineraryHighlightNested(text="Dalhousie Colonial Lanes & Deodar Forests", sort_order=4),
            ItineraryHighlightNested(text="Khajjiar Mini Switzerland Meadow", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival in Chandigarh to Shimla",
                description=(
                    "Your ultimate Himachal panorama begins with a warm TRAGUIN welcome at Chandigarh Airport "
                    "or Railway Station. Ascend through the Shivalik foothills to Shimla and check into your "
                    "handpicked premium heritage resort."
                ),
                activities=[
                    "Sightseeing Included: Scenic Himalayan foothills drive, Timber Trail valley views en-route",
                    "Evening Experience: Private welcome dinner and heritage walk briefing on Mall Road",
                    "Overnight Stay: Shimla (Premium Luxury Heritage Resort)",
                    "Meals Included: Welcome refreshment & luxury dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Shimla Heritage & Kufri Excursion",
                description=(
                    "Explore Shimla's colonial legacy at the Viceregal Lodge, Christ Church, and The Ridge. "
                    "Drive to Kufri for alpine panoramas, pine forest trails, and the Himalayan Nature Park "
                    "before returning for an evening stroll along historic Mall Road."
                ),
                activities=[
                    "Sightseeing Included: Viceregal Lodge, The Ridge, Christ Church, Mall Road, Kufri Adventure Park, Green Valley",
                    "Evening Experience: Curated cafe hopping and heritage bookstore visit on Mall Road",
                    "Overnight Stay: Shimla (Premium Luxury Heritage Resort)",
                    "Meals Included: Premium breakfast & dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Shimla to Manali via Kullu Valley",
                description=(
                    "Bid farewell to Shimla and descend through the spectacular Kullu Valley along the Beas River. "
                    "Stop at Pandoh Dam and traditional handloom workshops before arriving at your premium "
                    "riverside luxury resort in Manali."
                ),
                activities=[
                    "Sightseeing Included: Sundernagar Lake, Pandoh Dam, Kullu Valley, Beas River drive views",
                    "Evening Experience: Riverside bonfire and gourmet dinner at your Manali resort",
                    "Overnight Stay: Manali (Premium Riverside Luxury Property)",
                    "Meals Included: Breakfast & lavish riverside dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Manali Local Sightseeing",
                description=(
                    "Immerse yourself in Manali's cultural tapestry. Visit the ancient Hadimba Devi Temple "
                    "in a deodar forest, explore Vashisht's therapeutic hot sulphur springs, and spend your "
                    "evening in Old Manali's bohemian cafe culture."
                ),
                activities=[
                    "Sightseeing Included: Hadimba Temple, Club House, Vashisht Hot Springs, Tibetan Monastery, Old Manali",
                    "Evening Experience: Bespoke trout dining and riverside cafe recommendations in Old Manali",
                    "Overnight Stay: Manali (Premium Riverside Luxury Property)",
                    "Meals Included: Breakfast & premium buffet dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="Solang Valley Adventure Day",
                description=(
                    "An exhilarating day at Solang Valley — Manali's premier adventure hub. Ride the open gondola "
                    "cable car to Mount Phatru for glacier panoramas and enjoy paragliding, zorbing, or quad "
                    "biking amid snow-draped meadows."
                ),
                activities=[
                    "Sightseeing Included: Solang Valley meadows, cable car ride, snow line views, Palchan Village",
                    "Optional Activities: Tandem paragliding, zorbing, quad biking, or ski hire (seasonal)",
                    "Overnight Stay: Manali (Premium Riverside Luxury Property)",
                    "Meals Included: Breakfast & multi-cuisine chef's special dinner",
                ],
                sort_order=5,
            ),
            ItineraryDayNested(
                day_number=6,
                title="Manali to Dharamshala",
                description=(
                    "After breakfast, drive toward Dharamshala through the Kangra Valley's terraced farms and "
                    "tea gardens. Spend the afternoon exploring McLeodganj's Dalai Lama Temple and Bhagsunag "
                    "Waterfall before checking into your premium valley resort."
                ),
                activities=[
                    "Sightseeing Included: Kangra Valley drive, Dalai Lama Temple, Bhagsunag Waterfall, Dal Lake, St. John Church",
                    "Evening Experience: Curated Tibetan momo tasting and Dhauladhar sunset photography from your resort",
                    "Overnight Stay: Dharamshala (Premium Luxury Valley Resort)",
                    "Meals Included: Breakfast & authentic mountain dinner",
                ],
                sort_order=6,
            ),
            ItineraryDayNested(
                day_number=7,
                title="Dharamshala to Dalhousie via Khajjiar",
                description=(
                    "Drive to Dalhousie through the spectacular Khajjiar meadow — India's Mini Switzerland. "
                    "Walk around the emerald lake surrounded by cedar forests and rolling meadows before "
                    "continuing to Dalhousie's colonial-era hill station for a farewell dinner."
                ),
                activities=[
                    "Sightseeing Included: Khajjiar meadow and lake, Khajjiar Nag Temple, Dalhousie Subhash Baoli, St. Francis Church",
                    "Evening Experience: Farewell gala dinner with live mountain music at your colonial hill resort",
                    "Overnight Stay: Dalhousie (Premium Colonial Hill Resort)",
                    "Meals Included: Breakfast & premium farewell dinner",
                ],
                sort_order=7,
            ),
            ItineraryDayNested(
                day_number=8,
                title="Dalhousie to Chandigarh / Departure",
                description=(
                    "Enjoy your final mountain breakfast before your private luxury vehicle transfers you "
                    "to Chandigarh Airport or Railway Station with the complete Himalayan panorama etched "
                    "in memory."
                ),
                activities=[
                    "Transfers Included: Private luxury door-to-door station or airport drop-off via Chamba Valley",
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
                location="Dharamshala (1N)",
                nights_label="01 Night",
                description="Deluxe valley resort in Dharamshala.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=9,
            ),
            ItineraryHotelNested(
                name="Fortune Park Moksha / Similar",
                location="Dharamshala (1N)",
                nights_label="01 Night",
                description="Premium resort with Dhauladhar valley views.",
                stars=4,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=10,
            ),
            ItineraryHotelNested(
                name="The Pavilion by HPCA / Hyatt Regency / Similar",
                location="Dharamshala (1N)",
                nights_label="01 Night",
                description="Luxury resort overlooking the Kangra Valley.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=11,
            ),
            ItineraryHotelNested(
                name="Radisson Blu Resort Dharamshala / Similar",
                location="Dharamshala (1N)",
                nights_label="01 Night",
                description="Ultra-luxury resort beneath the Dhauladhar range.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Luxury Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=12,
            ),
            ItineraryHotelNested(
                name="Hotel Dalhousie Grand / Similar",
                location="Dalhousie (1N)",
                nights_label="01 Night",
                description="Deluxe colonial hill resort in Dalhousie.",
                stars=3,
                category_label="Deluxe",
                room_type="Valley View Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=13,
            ),
            ItineraryHotelNested(
                name="Snow Valley Resorts Dalhousie / Similar",
                location="Dalhousie (1N)",
                nights_label="01 Night",
                description="Premium hill resort with cedar forest views.",
                stars=4,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=14,
            ),
            ItineraryHotelNested(
                name="Aamod Dalhousie / Similar",
                location="Dalhousie (1N)",
                nights_label="01 Night",
                description="Luxury boutique resort amid deodar forests.",
                stars=4,
                category_label="Luxury",
                room_type="Luxury Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=15,
            ),
            ItineraryHotelNested(
                name="JK Clarks Exotica Dalhousie / Similar",
                location="Dalhousie (1N)",
                nights_label="01 Night",
                description="Ultra-luxury colonial heritage suite in Dalhousie.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Heritage Luxury Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=16,
            ),
        ],
        inclusions=[
            ItineraryInclusionNested(
                kind="included",
                text="07 nights premium accommodation across Shimla, Manali, Dharamshala, and Dalhousie",
                sort_order=1,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Daily lavish breakfasts and multi-cuisine dinners (MAPAI plan)",
                sort_order=2,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Private chauffeur-driven AC Innova Crysta for all circuit transfers and sightseeing",
                sort_order=3,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="TRAGUIN 24/7 dedicated elite guest relationship manager assistance",
                sort_order=4,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Khajjiar meadow excursion and personalized welcome kit with dry fruits and mineral water",
                sort_order=5,
            ),
            ItineraryInclusionNested(
                kind="included",
                text="Driver allowances, tolls, parking, fuel, and applicable taxes",
                sort_order=6,
            ),
            ItineraryInclusionNested(
                kind="excluded",
                text="Airfare or train tickets to and from Chandigarh",
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
                text="Khajjiar pony ride, zorbing fees, and optional Rohtang Pass permits",
                sort_order=10,
            ),
        ],
    )
    return package, itinerary, HP_020_PEXELS_IMAGES
