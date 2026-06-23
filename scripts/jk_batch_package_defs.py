"""Builder functions for JK-001, JK-002, JK-003, JK-004, JK-006, JK-007, and JK-010 Kashmir packages."""

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
    JK_001_PEXELS_IMAGES,
    JK_002_PEXELS_IMAGES,
    JK_003_PEXELS_IMAGES,
    JK_004_PEXELS_IMAGES,
    JK_006_PEXELS_IMAGES,
    JK_007_PEXELS_IMAGES,
    JK_010_PEXELS_IMAGES,
)


def _standard_inclusions(extra_included: list[str] | None = None) -> list[ItineraryInclusionNested]:
    included_texts = [
        "Premium accommodation at handpicked Kashmir resorts, heritage houseboats, and valley properties",
        "Daily lavish breakfasts and authentic Kashmiri multi-cuisine dinners (MAPAI plan)",
        "Private chauffeur-driven AC Innova Crysta for all transfers, valleys, and sightseeing",
        "TRAGUIN 24/7 dedicated elite guest relationship manager assistance",
        "Personalized welcome kit with kahwa, dry fruits, mineral water, and shikara transfers where applicable",
        "Driver allowances, tolls, parking, fuel, and applicable taxes",
    ]
    if extra_included:
        included_texts.extend(extra_included)
    excluded_texts = [
        "Airfare or train tickets to and from Srinagar or Delhi gateway",
        "Gondola ride tickets, pony rides, and adventure activity fees beyond included tier",
        "Monument entry tickets, camera fees, and optional guide gratuities",
        "Personal expenses such as laundry, phone calls, room heaters, and tipping",
    ]
    items: list[ItineraryInclusionNested] = []
    sort_order = 1
    for text in included_texts:
        items.append(ItineraryInclusionNested(kind="included", text=text, sort_order=sort_order))
        sort_order += 1
    for text in excluded_texts:
        items.append(ItineraryInclusionNested(kind="excluded", text=text, sort_order=sort_order))
        sort_order += 1
    return items


def _trek_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(
            kind="included",
            text="08 nights accommodation — Srinagar hotel, Sonamarg base camp lodge, and alpine camping on trek nights",
            sort_order=1,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="All meals on trek days — nutritious breakfast, packed lunch, and hot dinner at camps",
            sort_order=2,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Certified high-altitude trek leader, local guide, and support crew throughout the expedition",
            sort_order=3,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Premium trekking tents, sleeping bags, mattresses, and communal dining tent on trail",
            sort_order=4,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Porter and mule support for camping equipment and group supplies on trek route",
            sort_order=5,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Private transfers Srinagar ↔ Sonamarg/Naranag and TRAGUIN 24/7 expedition concierge",
            sort_order=6,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Forest permits, trek registration, medical kit, and oxygen support at high camps",
            sort_order=7,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Airfare or train tickets to Srinagar",
            sort_order=8,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Personal trekking gear — boots, jackets, poles (rental available on request)",
            sort_order=9,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Pony hire for personal baggage, tips to crew, and personal insurance",
            sort_order=10,
        ),
    ]


def build_jk_001(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 21
    package = PackageCreate(
        slug="jk-001-kashmir-paradise-family",
        destination_id=destination_id,
        title="Kashmir Paradise Family — Houseboat, Gulmarg & Pahalgam",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="Heritage cedarwood houseboat nights on Dal Lake with private shikara transfers",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Gulmarg Gondola ascent to Apharwat Peak — snow meadows and alpine panoramas",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Pahalgam valley drive — Betaab Valley, Lidder River, and pine-forested meadows",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Mughal garden circuit — Shalimar Bagh, Nishat Bagh, and Chashme Shahi fountains",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Pampore saffron fields and floating vegetable market on Dal Lake",
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
        slug="jk-001-kashmir-paradise-family-itinerary",
        destination_id=destination_id,
        title="Kashmir Paradise Family — Houseboat, Gulmarg & Pahalgam",
        duration_label="05 Nights / 06 Days",
        duration_days=6,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Paradise Found — A Family Journey Through Kashmir",
        overview=(
            "Discover Kashmir's legendary beauty on TRAGUIN's definitive family escape — from sunrise shikara "
            "glides across mirror-still Dal Lake and nights aboard hand-carved cedar houseboats to Gulmarg's "
            "iconic Gondola and the emerald valleys of Pahalgam. This premium curated journey weaves together "
            "Mughal garden heritage, saffron meadows at Pampore, authentic Wazwan feasts, and handpicked "
            "resorts with a dedicated private chauffeur for seamless family comfort."
        ),
        seo_title="JK-001 | Kashmir Paradise Family | TRAGUIN Premium Kashmir Tour",
        seo_description=(
            "Luxury 05 Nights / 06 Days Kashmir family package (JK-001) covering Dal Lake houseboat, Gulmarg "
            "Gondola, Pahalgam Betaab Valley, and Mughal gardens with premium stays and private transfers. "
            "Ideal for families and nature lovers."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Dal Lake Houseboat & Shikara", sort_order=1),
            ItineraryHighlightNested(text="Gulmarg Gondola & Snow Meadows", sort_order=2),
            ItineraryHighlightNested(text="Pahalgam Betaab & Lidder Valley", sort_order=3),
            ItineraryHighlightNested(text="Mughal Gardens Heritage Circuit", sort_order=4),
            ItineraryHighlightNested(text="Pampore Saffron & Floating Market", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival in Srinagar — Dal Lake Houseboat",
                description=(
                    "Your Kashmir family adventure begins with a warm TRAGUIN welcome at Srinagar Airport. "
                    "Board your private luxury vehicle and glide by shikara to your hand-carved heritage houseboat "
                    "moored on Dal Lake. Spend a magical evening sipping kahwa on the cedar deck as the Zabarwan "
                    "mountains turn gold at sunset."
                ),
                activities=[
                    "Sightseeing Included: Scenic airport transfer, Dal Lake first glimpse, Char Chinar island cruise (optional)",
                    "Evening Experience: Traditional Wazwan tasting dinner aboard your private houseboat",
                    "Overnight Stay: Srinagar (Heritage Deluxe / Premium Houseboat on Dal Lake)",
                    "Meals Included: Welcome kahwa & authentic Kashmiri dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Srinagar Mughal Gardens & Old City",
                description=(
                    "After a leisurely breakfast, explore Kashmir's living heritage — the terraced fountains of "
                    "Shalimar Bagh built by Emperor Jahangir, Nishat Bagh's twelve terraces cascading toward Dal "
                    "Lake, and the royal spring pavilions of Chashme Shahi. Ascend Shankaracharya Temple hill for "
                    "a sweeping valley panorama before browsing Pashmina ateliers in the old city."
                ),
                activities=[
                    "Sightseeing Included: Shalimar Bagh, Nishat Bagh, Chashme Shahi, Shankaracharya Temple, Hazratbal Shrine view",
                    "Optional Activities: Heritage walk through Khanqah-e-Moula and old Srinagar spice lanes",
                    "Overnight Stay: Srinagar (Heritage Houseboat / Premium Lake-View Hotel)",
                    "Meals Included: Premium breakfast & multi-cuisine dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Srinagar to Gulmarg — Gondola & Alpine Meadows",
                description=(
                    "Drive through apple orchards and pine forests to Gulmarg — the Meadow of Flowers at 8,694 ft. "
                    "Ride Asia's highest cable car in two phases to Kongdoori and Apharwat Peak for breathtaking "
                    "views of the Pir Panjal and Karakoram ranges. Families can enjoy snow activities in winter or "
                    "wildflower meadows in summer."
                ),
                activities=[
                    "Sightseeing Included: Gulmarg Golf Course view, Gondola Phase I & II, Apharwat Peak snow ridge panoramas",
                    "Optional Activities: Skiing lessons, snow scooter rides, or pony rides across alpine meadows",
                    "Overnight Stay: Gulmarg (Premium / Luxury Mountain Resort)",
                    "Meals Included: Breakfast & hearty mountain dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Gulmarg to Pahalgam — Betaab Valley",
                description=(
                    "Descend through the Kashmir Valley toward Pahalgam, the Valley of Shepherds. En route, "
                    "marvel at the crystal Lidder River cutting through pine forests. Explore the cinematic Betaab "
                    "Valley meadows and optional Aru Valley with its alpine village charm and trout streams."
                ),
                activities=[
                    "Sightseeing Included: Awantipora temple ruins en route, Betaab Valley meadows, Lidder River viewpoints, Aru Valley (optional)",
                    "Evening Experience: Riverside family bonfire with Kashmiri folk music at your resort",
                    "Overnight Stay: Pahalgam (Premium Riverside Valley Resort)",
                    "Meals Included: Breakfast & riverside barbecue dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="Pahalgam to Srinagar — Saffron Fields & Shikara",
                description=(
                    "Return to Srinagar via the saffron capital Pampore, where purple crocus fields bloom in "
                    "autumn. Check back into your houseboat or lake-view hotel for a final sunset shikara cruise "
                    "past floating gardens and the vibrant early-morning vegetable market."
                ),
                activities=[
                    "Sightseeing Included: Pampore saffron fields, floating vegetable market shikara ride, Pari Mahal terrace gardens",
                    "Evening Experience: Farewell family dinner with live santoor performance on Dal Lake",
                    "Overnight Stay: Srinagar (Heritage Houseboat / Luxury Lake-View Hotel)",
                    "Meals Included: Breakfast & premium farewell Wazwan dinner",
                ],
                sort_order=5,
            ),
            ItineraryDayNested(
                day_number=6,
                title="Srinagar Departure",
                description=(
                    "Savor a final lakeside breakfast as mist rises off Dal Lake. Your private vehicle transfers "
                    "you to Srinagar Airport with cherished family memories of Kashmir's paradise curated by TRAGUIN."
                ),
                activities=[
                    "Transfers Included: Private luxury door-to-door airport drop-off",
                    "Meals Included: Sumptuous buffet breakfast",
                ],
                sort_order=6,
            ),
        ],
        hotels=[
            ItineraryHotelNested(
                name="New Alexandra / Similar Heritage Houseboat",
                location="Srinagar Dal Lake (2N)",
                nights_label="02 Nights",
                description="Deluxe cedarwood houseboat with lake views.",
                stars=4,
                category_label="Deluxe",
                room_type="Deluxe Houseboat Suite",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=1,
            ),
            ItineraryHotelNested(
                name="Peacock Houseboats / Similar",
                location="Srinagar Dal Lake (2N)",
                nights_label="02 Nights",
                description="Premium hand-carved houseboat with shikara transfers.",
                stars=4,
                category_label="Premium",
                room_type="Premium Houseboat Suite",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=2,
            ),
            ItineraryHotelNested(
                name="The Lalit Grand Palace / Similar",
                location="Srinagar (2N)",
                nights_label="02 Nights",
                description="Luxury heritage palace hotel overlooking Dal Lake.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Palace Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=3,
            ),
            ItineraryHotelNested(
                name="Vivanta Dal View / Similar",
                location="Srinagar (2N)",
                nights_label="02 Nights",
                description="Ultra-luxury lake-view suite with butler service.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Luxury Lake View Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=4,
            ),
            ItineraryHotelNested(
                name="Hotel Hilltop / Similar",
                location="Gulmarg (1N)",
                nights_label="01 Night",
                description="Deluxe mountain resort in Gulmarg.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=5,
            ),
            ItineraryHotelNested(
                name="Hotel Pine Spring / Similar",
                location="Gulmarg (1N)",
                nights_label="01 Night",
                description="Premium resort with meadow and peak views.",
                stars=4,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=6,
            ),
            ItineraryHotelNested(
                name="The Khyber Himalayan Resort & Spa / Similar",
                location="Gulmarg (1N)",
                nights_label="01 Night",
                description="Luxury alpine resort at the foot of Apharwat.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=7,
            ),
            ItineraryHotelNested(
                name="Khyber Premium Cottage / Similar",
                location="Gulmarg (1N)",
                nights_label="01 Night",
                description="Ultra-luxury cottage with spa and peak panoramas.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Premium Alpine Cottage",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=8,
            ),
            ItineraryHotelNested(
                name="Hotel Heevan / Similar",
                location="Pahalgam (1N)",
                nights_label="01 Night",
                description="Deluxe riverside resort on the Lidder.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=9,
            ),
            ItineraryHotelNested(
                name="Pine N Peak / Similar",
                location="Pahalgam (1N)",
                nights_label="01 Night",
                description="Premium valley resort with pine forest views.",
                stars=4,
                category_label="Premium",
                room_type="Premium Valley View Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=10,
            ),
            ItineraryHotelNested(
                name="Welcomhotel Pine N Peak / Similar",
                location="Pahalgam (1N)",
                nights_label="01 Night",
                description="Luxury riverside resort with spa facilities.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=11,
            ),
            ItineraryHotelNested(
                name="Pahalgam Hotel / Similar",
                location="Pahalgam (1N)",
                nights_label="01 Night",
                description="Ultra-luxury suite with private riverside access.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Luxury Riverside Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=12,
            ),
        ],
        inclusions=_standard_inclusions(
            extra_included=[
                "05 nights premium accommodation across Srinagar houseboat, Gulmarg, and Pahalgam",
                "One complimentary sunset shikara ride on Dal Lake for the family",
            ]
        ),
    )
    return package, itinerary, JK_001_PEXELS_IMAGES


def build_jk_002(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 22
    package = PackageCreate(
        slug="jk-002-srinagar-gulmarg-premium-family",
        destination_id=destination_id,
        title="Srinagar Gulmarg Premium Family Escape",
        duration_label="04 Nights / 05 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="Premium Dal Lake houseboat nights with floating market and Char Chinar shikara cruise",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Nishat Bagh terraced gardens and Shankaracharya Temple panoramic valley views",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Gulmarg meadow of flowers — Gondola ride and family snow adventure",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Authentic Kashmiri Wazwan feast served in traditional copper dishes",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Handpicked Srinagar and Gulmarg resorts across Deluxe to Ultra Luxury tiers",
                sort_order=5,
            ),
            PackageHighlightNested(
                text="Private Innova Crysta with TRAGUIN 24/7 family concierge support",
                sort_order=6,
            ),
        ],
        moods=["Family", "Luxury", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="jk-002-srinagar-gulmarg-premium-family-itinerary",
        destination_id=destination_id,
        title="Srinagar Gulmarg Premium Family Escape",
        duration_label="04 Nights / 05 Days",
        duration_days=5,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Premium Family Bliss — Srinagar & Gulmarg",
        overview=(
            "A perfectly paced premium family retreat combining Srinagar's timeless lake culture with Gulmarg's "
            "alpine grandeur. TRAGUIN curates this 04-night escape with heritage houseboat evenings on Dal Lake, "
            "Mughal garden explorations, floating vegetable market shikara rides, and two full days in Gulmarg "
            "featuring the iconic Gondola and meadow adventures — all with private chauffeur transfers and "
            "handpicked family-friendly resorts."
        ),
        seo_title="JK-002 | Srinagar Gulmarg Premium Family | TRAGUIN Premium Kashmir Tour",
        seo_description=(
            "Luxury 04 Nights / 05 Days Kashmir family package (JK-002) covering Dal Lake houseboat, Nishat Bagh, "
            "Shankaracharya Temple, and Gulmarg Gondola with premium stays and private transfers. "
            "Ideal for families seeking a shorter Kashmir escape."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Dal Lake Houseboat & Floating Market", sort_order=1),
            ItineraryHighlightNested(text="Nishat Bagh & Shankaracharya Views", sort_order=2),
            ItineraryHighlightNested(text="Gulmarg Gondola & Alpine Meadows", sort_order=3),
            ItineraryHighlightNested(text="Kashmiri Wazwan Family Feast", sort_order=4),
            ItineraryHighlightNested(text="Premium Resort Stays Both Destinations", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival in Srinagar — Houseboat Welcome",
                description=(
                    "Arrive at Srinagar Airport for a warm TRAGUIN family welcome. Transfer by private vehicle "
                    "and shikara to your premium heritage houseboat on Dal Lake. Unwind on the cedar deck with "
                    "kahwa and watch shikaras glide past floating gardens as the Zabarwan range glows at dusk."
                ),
                activities=[
                    "Sightseeing Included: Airport transfer, Dal Lake shikara welcome cruise, Char Chinar island visit",
                    "Evening Experience: Traditional Wazwan family dinner aboard your houseboat",
                    "Overnight Stay: Srinagar (Premium Heritage Houseboat on Dal Lake)",
                    "Meals Included: Welcome kahwa & authentic Kashmiri dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Srinagar Gardens, Temple & Old City",
                description=(
                    "Explore Srinagar's finest landmarks — Nishat Bagh's terraced lawns overlooking Dal Lake, "
                    "the panoramic vista from Shankaracharya Temple, and the floating vegetable market where "
                    "farmers sell produce from shikaras. Browse Pashmina and walnut woodcraft in the old city bazaars."
                ),
                activities=[
                    "Sightseeing Included: Nishat Bagh, Shankaracharya Temple, floating vegetable market, Hazratbal Shrine exterior",
                    "Optional Activities: Pari Mahal terraced gardens and old city heritage walk",
                    "Overnight Stay: Srinagar (Premium Houseboat / Lake-View Hotel)",
                    "Meals Included: Premium breakfast & multi-cuisine dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Srinagar to Gulmarg — Meadow of Flowers",
                description=(
                    "Drive through fragrant apple orchards to Gulmarg, the crown jewel of Kashmir's alpine tourism. "
                    "Check into your premium mountain resort and spend the afternoon exploring the famous golf "
                    "course meadows — carpeted with wildflowers in summer and pristine snow in winter."
                ),
                activities=[
                    "Sightseeing Included: Tangmarg scenic drive, Gulmarg Golf Course, St. Mary's Church, meadow photography",
                    "Evening Experience: Family bonfire with hot chocolate and Kashmiri kehwa at the resort",
                    "Overnight Stay: Gulmarg (Premium / Luxury Mountain Resort)",
                    "Meals Included: Breakfast & hearty mountain dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Gulmarg Gondola & Alpine Adventure",
                description=(
                    "A full day of alpine wonder aboard the Gulmarg Gondola — ascending in two phases to Kongdoori "
                    "and Apharwat Peak at 13,780 ft. Marvel at 360-degree views of the Pir Panjal range. Families "
                    "enjoy snow sledging, skiing, or meadow picnics depending on the season."
                ),
                activities=[
                    "Sightseeing Included: Gondola Phase I & II, Apharwat Peak ridge views, Kongdoori station panoramas",
                    "Optional Activities: Skiing, snow scooter, pony rides, or alpine nature walk for children",
                    "Overnight Stay: Gulmarg (Premium / Luxury Mountain Resort)",
                    "Meals Included: Breakfast & festive farewell mountain dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="Gulmarg to Srinagar — Departure",
                description=(
                    "Enjoy a final mountain breakfast before descending to Srinagar Airport. Reflect on a premium "
                    "family journey through Kashmir's lake culture and alpine meadows curated exclusively by TRAGUIN."
                ),
                activities=[
                    "Transfers Included: Private luxury transfer Gulmarg to Srinagar Airport",
                    "Meals Included: Sumptuous buffet breakfast",
                ],
                sort_order=5,
            ),
        ],
        hotels=[
            ItineraryHotelNested(
                name="New Alexandra / Similar Heritage Houseboat",
                location="Srinagar Dal Lake (2N)",
                nights_label="02 Nights",
                description="Deluxe cedarwood houseboat on Dal Lake.",
                stars=4,
                category_label="Deluxe",
                room_type="Deluxe Houseboat Suite",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=1,
            ),
            ItineraryHotelNested(
                name="Peacock Houseboats / Similar",
                location="Srinagar Dal Lake (2N)",
                nights_label="02 Nights",
                description="Premium hand-carved houseboat with shikara.",
                stars=4,
                category_label="Premium",
                room_type="Premium Houseboat Suite",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=2,
            ),
            ItineraryHotelNested(
                name="The Lalit Grand Palace / Similar",
                location="Srinagar (2N)",
                nights_label="02 Nights",
                description="Luxury heritage palace on Dal Lake.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Palace Room",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=3,
            ),
            ItineraryHotelNested(
                name="Vivanta Dal View / Similar",
                location="Srinagar (2N)",
                nights_label="02 Nights",
                description="Ultra-luxury lake-view suite with butler.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Luxury Lake View Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=4,
            ),
            ItineraryHotelNested(
                name="Hotel Hilltop / Similar",
                location="Gulmarg (2N)",
                nights_label="02 Nights",
                description="Deluxe mountain resort in Gulmarg.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=5,
            ),
            ItineraryHotelNested(
                name="Hotel Pine Spring / Similar",
                location="Gulmarg (2N)",
                nights_label="02 Nights",
                description="Premium resort with meadow views.",
                stars=4,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=6,
            ),
            ItineraryHotelNested(
                name="The Khyber Himalayan Resort & Spa / Similar",
                location="Gulmarg (2N)",
                nights_label="02 Nights",
                description="Luxury alpine resort at Apharwat foothills.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=7,
            ),
            ItineraryHotelNested(
                name="Khyber Premium Cottage / Similar",
                location="Gulmarg (2N)",
                nights_label="02 Nights",
                description="Ultra-luxury cottage with spa and peak views.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Premium Alpine Cottage",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=8,
            ),
        ],
        inclusions=_standard_inclusions(
            extra_included=[
                "04 nights premium accommodation across Srinagar houseboat and Gulmarg resort",
                "One complimentary floating market shikara experience for the family",
            ]
        ),
    )
    return package, itinerary, JK_002_PEXELS_IMAGES


def build_jk_003(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 23
    package = PackageCreate(
        slug="jk-003-srinagar-pahalgam-gulmarg-dal-lake",
        destination_id=destination_id,
        title="Srinagar • Pahalgam • Gulmarg • Dal Lake Discovery",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="Betaab Valley crystal streams and Aru Valley alpine meadow panoramas in Pahalgam",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Golden sunset shikara cruise on Dal Lake with Zabarwan mountain backdrop",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Gulmarg Gondola to Apharwat Peak — snow ridges and Karakoram views",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Chandanwari snow bridge vistas on the legendary Amarnath pilgrimage route",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Pari Mahal terraced gardens with sweeping Srinagar valley panoramas",
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
        slug="jk-003-srinagar-pahalgam-gulmarg-dal-lake-itinerary",
        destination_id=destination_id,
        title="Srinagar • Pahalgam • Gulmarg • Dal Lake Discovery",
        duration_label="05 Nights / 06 Days",
        duration_days=6,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="The Complete Kashmir Valley Circuit",
        overview=(
            "Experience Kashmir's four iconic landscapes in one seamless TRAGUIN journey — the cinematic valleys "
            "of Pahalgam with Betaab and Aru, Gulmarg's alpine Gondola heights, and Srinagar's Dal Lake shikara "
            "culture with Pari Mahal gardens. This premium 05-night circuit balances adventure, heritage, and "
            "leisure with handpicked resorts, private chauffeur transfers, and curated experiences at every stop."
        ),
        seo_title="JK-003 | Srinagar Pahalgam Gulmarg Dal Lake | TRAGUIN Premium Kashmir Tour",
        seo_description=(
            "Luxury 05 Nights / 06 Days Kashmir package (JK-003) covering Pahalgam Betaab Valley, Gulmarg Gondola, "
            "Dal Lake shikara, and Pari Mahal with premium stays and private transfers. "
            "Ideal for families and discovery travelers."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Pahalgam Betaab & Aru Valleys", sort_order=1),
            ItineraryHighlightNested(text="Dal Lake Sunset Shikara", sort_order=2),
            ItineraryHighlightNested(text="Gulmarg Apharwat Gondola", sort_order=3),
            ItineraryHighlightNested(text="Chandanwari Snow Bridge", sort_order=4),
            ItineraryHighlightNested(text="Pari Mahal Terrace Gardens", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival in Srinagar — Dal Lake Shikara",
                description=(
                    "Begin your Kashmir discovery with a TRAGUIN welcome at Srinagar Airport. Check into your "
                    "premium lake-view hotel or heritage houseboat and embark on a golden sunset shikara cruise "
                    "across Dal Lake, gliding past floating gardens and the Zabarwan range."
                ),
                activities=[
                    "Sightseeing Included: Airport transfer, Dal Lake sunset shikara cruise, floating garden views",
                    "Evening Experience: Welcome kahwa ceremony and Kashmiri dinner with valley views",
                    "Overnight Stay: Srinagar (Premium Houseboat / Lake-View Hotel)",
                    "Meals Included: Welcome refreshment & gourmet dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Srinagar to Pahalgam — Betaab & Aru Valleys",
                description=(
                    "Drive south through the Kashmir Valley to Pahalgam, the shepherd's paradise. Explore the "
                    "cinematic Betaab Valley where crystal streams cut through emerald meadows, then continue to "
                    "Aru Valley for alpine village charm and snow-capped peak panoramas."
                ),
                activities=[
                    "Sightseeing Included: Betaab Valley meadows, Lidder River viewpoints, Aru Valley alpine vistas",
                    "Optional Activities: Chandanwari snow bridge excursion (seasonal) or pony trek for children",
                    "Overnight Stay: Pahalgam (Premium Riverside Valley Resort)",
                    "Meals Included: Breakfast & riverside dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Pahalgam Leisure & Chandanwari Excursion",
                description=(
                    "A full day in Pahalgam's pine-scented valleys. Visit Chandanwari, the gateway to the Amarnath "
                    "Yatra, for dramatic snow bridge vistas. Enjoy a riverside picnic on the Lidder or optional "
                    "white-water rafting for adventure-loving families."
                ),
                activities=[
                    "Sightseeing Included: Chandanwari snow bridge, Lidder River banks, Pahalgam market stroll",
                    "Optional Activities: White-water rafting on the Lidder or guided trout fishing experience",
                    "Overnight Stay: Pahalgam (Premium Riverside Valley Resort)",
                    "Meals Included: Breakfast & barbecue dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Pahalgam to Gulmarg — Gondola & Apharwat",
                description=(
                    "Ascend to Gulmarg through apple orchards and pine forests. Ride the iconic two-phase Gondola "
                    "to Apharwat Peak for sweeping views of the Pir Panjal and Karakoram ranges. Spend the "
                    "afternoon on snow activities or wildflower meadow walks."
                ),
                activities=[
                    "Sightseeing Included: Gulmarg Golf Course, Gondola Phase I & II, Apharwat Peak ridge panoramas",
                    "Evening Experience: Mountain sunset photography and hot kehwa at your alpine resort",
                    "Overnight Stay: Gulmarg (Premium / Luxury Mountain Resort)",
                    "Meals Included: Breakfast & mountain feast dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="Gulmarg to Srinagar — Pari Mahal & Gardens",
                description=(
                    "Return to Srinagar and explore the terraced Pari Mahal gardens — the Abode of Fairies — with "
                    "panoramic views over the entire city and Dal Lake. Visit Shalimar Bagh or Nishat Bagh for a "
                    "final Mughal garden experience before a farewell lakeside dinner."
                ),
                activities=[
                    "Sightseeing Included: Pari Mahal terraces, Shalimar Bagh or Nishat Bagh, old city spice bazaar",
                    "Evening Experience: Farewell dinner with live santoor performance overlooking Dal Lake",
                    "Overnight Stay: Srinagar (Heritage Houseboat / Luxury Lake-View Hotel)",
                    "Meals Included: Breakfast & premium farewell Wazwan dinner",
                ],
                sort_order=5,
            ),
            ItineraryDayNested(
                day_number=6,
                title="Srinagar Departure",
                description=(
                    "Enjoy a final morning shikara ride or lakeside breakfast before your private transfer to "
                    "Srinagar Airport. Depart with the complete Kashmir valley etched in memory by TRAGUIN."
                ),
                activities=[
                    "Transfers Included: Private luxury airport drop-off",
                    "Meals Included: Sumptuous buffet breakfast",
                ],
                sort_order=6,
            ),
        ],
        hotels=[
            ItineraryHotelNested(
                name="New Alexandra / Similar Heritage Houseboat",
                location="Srinagar (2N)",
                nights_label="02 Nights",
                description="Deluxe cedarwood houseboat on Dal Lake.",
                stars=4,
                category_label="Deluxe",
                room_type="Deluxe Houseboat Suite",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=1,
            ),
            ItineraryHotelNested(
                name="Peacock Houseboats / Similar",
                location="Srinagar (2N)",
                nights_label="02 Nights",
                description="Premium hand-carved houseboat with shikara.",
                stars=4,
                category_label="Premium",
                room_type="Premium Houseboat Suite",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=2,
            ),
            ItineraryHotelNested(
                name="The Lalit Grand Palace / Similar",
                location="Srinagar (2N)",
                nights_label="02 Nights",
                description="Luxury heritage palace overlooking Dal Lake.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Palace Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=3,
            ),
            ItineraryHotelNested(
                name="Vivanta Dal View / Similar",
                location="Srinagar (2N)",
                nights_label="02 Nights",
                description="Ultra-luxury lake-view suite with butler.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Luxury Lake View Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=4,
            ),
            ItineraryHotelNested(
                name="Hotel Heevan / Similar",
                location="Pahalgam (2N)",
                nights_label="02 Nights",
                description="Deluxe riverside resort on the Lidder.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=5,
            ),
            ItineraryHotelNested(
                name="Pine N Peak / Similar",
                location="Pahalgam (2N)",
                nights_label="02 Nights",
                description="Premium valley resort with pine forest views.",
                stars=4,
                category_label="Premium",
                room_type="Premium Valley View Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=6,
            ),
            ItineraryHotelNested(
                name="Welcomhotel Pine N Peak / Similar",
                location="Pahalgam (2N)",
                nights_label="02 Nights",
                description="Luxury riverside resort with spa.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=7,
            ),
            ItineraryHotelNested(
                name="Pahalgam Hotel / Similar",
                location="Pahalgam (2N)",
                nights_label="02 Nights",
                description="Ultra-luxury suite with riverside access.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Luxury Riverside Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=8,
            ),
            ItineraryHotelNested(
                name="Hotel Hilltop / Similar",
                location="Gulmarg (1N)",
                nights_label="01 Night",
                description="Deluxe mountain resort in Gulmarg.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=9,
            ),
            ItineraryHotelNested(
                name="Hotel Pine Spring / Similar",
                location="Gulmarg (1N)",
                nights_label="01 Night",
                description="Premium resort with meadow views.",
                stars=4,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=10,
            ),
            ItineraryHotelNested(
                name="The Khyber Himalayan Resort & Spa / Similar",
                location="Gulmarg (1N)",
                nights_label="01 Night",
                description="Luxury alpine resort at Apharwat foothills.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=11,
            ),
            ItineraryHotelNested(
                name="Khyber Premium Cottage / Similar",
                location="Gulmarg (1N)",
                nights_label="01 Night",
                description="Ultra-luxury cottage with spa and peak views.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Premium Alpine Cottage",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=12,
            ),
        ],
        inclusions=_standard_inclusions(
            extra_included=[
                "05 nights premium accommodation across Srinagar, Pahalgam, and Gulmarg",
                "One complimentary sunset shikara ride on Dal Lake",
            ]
        ),
    )
    return package, itinerary, JK_003_PEXELS_IMAGES


def build_jk_004(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 24
    package = PackageCreate(
        slug="jk-004-romantic-kashmir-honeymoon",
        destination_id=destination_id,
        title="Romantic Kashmir Honeymoon — Love on Dal Lake",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="Private romantic shikara at sunset with floral décor and Kashmiri kahwa service",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Luxury cedarwood houseboat suite with hand-carved interiors and lake views",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Gulmarg snow meadow romance — couple walks beneath Pir Panjal peaks",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Pahalgam riverside bonfire evenings and intimate candlelight terrace dinners",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Pashmina atelier visit with expert guide for premium shawl selection",
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
        slug="jk-004-romantic-kashmir-honeymoon-itinerary",
        destination_id=destination_id,
        title="Romantic Kashmir Honeymoon — Love on Dal Lake",
        duration_label="05 Nights / 06 Days",
        duration_days=6,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Love Blooms in the Valley of Paradise",
        overview=(
            "Embark on the ultimate Kashmir honeymoon crafted to blend romantic seclusion with unparalleled "
            "natural grandeur. TRAGUIN's bespoke journey takes couples from private sunset shikara glides "
            "across Dal Lake to snow-draped Gulmarg meadows and Pahalgam's riverside serenity — featuring "
            "handpicked luxury houseboats, candlelit terrace dinners, floral bed styling, and a dedicated "
            "private chauffeur throughout."
        ),
        seo_title="JK-004 | Romantic Kashmir Honeymoon | TRAGUIN Premium Kashmir Tour",
        seo_description=(
            "Luxury 05 Nights / 06 Days Kashmir honeymoon package (JK-004) covering Dal Lake houseboat, "
            "Gulmarg snow meadows, Pahalgam riverside, and candlelight dinners with floral bed setup. "
            "Ideal for newlyweds and couples."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Private Sunset Shikara Romance", sort_order=1),
            ItineraryHighlightNested(text="Luxury Cedarwood Houseboat Suite", sort_order=2),
            ItineraryHighlightNested(text="Gulmarg Snow Meadow Walks", sort_order=3),
            ItineraryHighlightNested(text="Pahalgam Riverside Bonfire", sort_order=4),
            ItineraryHighlightNested(text="Candlelight Dinners & Floral Setup", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival in Srinagar — Luxury Houseboat Welcome",
                description=(
                    "Your romantic Kashmir escape begins with a VIP TRAGUIN reception at Srinagar Airport. "
                    "Glide by private shikara to your hand-carved luxury houseboat where a floral welcome and "
                    "chilled kahwa await. Spend the evening on the cedar deck as Dal Lake shimmers under starlight."
                ),
                activities=[
                    "Sightseeing Included: VIP airport transfer, private shikara arrival, Dal Lake twilight cruise",
                    "Evening Experience: Intimate candlelight dinner with celebratory honeymoon cake aboard your houseboat",
                    "Overnight Stay: Srinagar (Luxury Heritage Houseboat on Dal Lake)",
                    "Meals Included: Welcome libation & curated honeymoon dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Srinagar — Romantic Shikara & Mughal Gardens",
                description=(
                    "Wake to mist rising off Dal Lake and enjoy a private sunrise shikara ride with floral décor. "
                    "Explore the terraced beauty of Shalimar Bagh and Nishat Bagh hand-in-hand before an "
                    "exclusive candlelit dinner arranged by TRAGUIN on a lakeside terrace."
                ),
                activities=[
                    "Sightseeing Included: Private sunrise shikara, Shalimar Bagh, Nishat Bagh, Pari Mahal sunset viewpoint",
                    "Evening Experience: Exclusive candlelit terrace dinner with live santoor music",
                    "Overnight Stay: Srinagar (Luxury Heritage Houseboat)",
                    "Meals Included: Breakfast & special honeymoon dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Srinagar to Gulmarg — Snow Meadow Romance",
                description=(
                    "Drive to Gulmarg through fragrant orchards and ascend via the iconic Gondola to snow "
                    "meadows where couples walk hand-in-hand beneath the Pir Panjal range. Capture timeless "
                    "photographs against alpine peaks and return for a cozy evening at your luxury mountain resort."
                ),
                activities=[
                    "Sightseeing Included: Gulmarg Gondola Phase I & II, Apharwat snow ridge, meadow photography",
                    "Optional Activities: Tandem skiing or pony ride through wildflower meadows (seasonal)",
                    "Overnight Stay: Gulmarg (Luxury Alpine Resort)",
                    "Meals Included: Premium breakfast & authentic Kashmiri-infused dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Gulmarg to Pahalgam — Riverside Serenity",
                description=(
                    "Descend to Pahalgam's Lidder Valley for a day of riverside romance. Stroll along crystal "
                    "trout streams, explore Betaab Valley's emerald meadows, and end the evening with a private "
                    "bonfire beneath the stars at your luxury riverside resort."
                ),
                activities=[
                    "Sightseeing Included: Betaab Valley meadows, Lidder River walk, Aru Valley overlook (optional)",
                    "Evening Experience: Private riverside bonfire with Kashmiri kehwa and stargazing",
                    "Overnight Stay: Pahalgam (Luxury Riverside Resort)",
                    "Meals Included: Breakfast & romantic barbecue dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="Pahalgam to Srinagar — Pashmina & Farewell",
                description=(
                    "Return to Srinagar via Pampore saffron fields. Visit a premium Pashmina atelier where "
                    "master weavers demonstrate centuries-old handloom techniques. Enjoy a farewell Wazwan feast "
                    "with private almond-milk and bedside floral presentation at your houseboat."
                ),
                activities=[
                    "Sightseeing Included: Pampore saffron fields, Pashmina weaving atelier, old city heritage bazaar",
                    "Evening Experience: Private almond-milk and bedside floral presentation for newlyweds",
                    "Overnight Stay: Srinagar (Luxury Heritage Houseboat)",
                    "Meals Included: Breakfast & premium farewell Wazwan dinner",
                ],
                sort_order=5,
            ),
            ItineraryDayNested(
                day_number=6,
                title="Srinagar Departure",
                description=(
                    "Conclude your dream honeymoon with a lavish lakeside breakfast. Your private luxury vehicle "
                    "transfers you to Srinagar Airport carrying beautifully woven bonds and unforgettable "
                    "memories custom crafted by TRAGUIN."
                ),
                activities=[
                    "Transfers Included: Private luxury airport drop-off",
                    "Meals Included: Gourmet buffet breakfast",
                ],
                sort_order=6,
            ),
        ],
        hotels=[
            ItineraryHotelNested(
                name="Peacock Houseboats / Similar",
                location="Srinagar Dal Lake (3N)",
                nights_label="03 Nights",
                description="Premium hand-carved houseboat for honeymooners.",
                stars=4,
                category_label="Deluxe",
                room_type="Deluxe Houseboat Suite",
                meal_plan="MAPAI (Breakfast & Dinner) — Welcome Cake & Floral Bed Styling",
                sort_order=1,
            ),
            ItineraryHotelNested(
                name="Royal Group of Houseboats / Similar",
                location="Srinagar Dal Lake (3N)",
                nights_label="03 Nights",
                description="Premium cedarwood houseboat with lake views.",
                stars=4,
                category_label="Premium",
                room_type="Premium Houseboat Suite",
                meal_plan="MAPAI (Premium Buffet Menu) — Candlelight Dinner + Fruit Basket",
                sort_order=2,
            ),
            ItineraryHotelNested(
                name="The Lalit Grand Palace / Similar",
                location="Srinagar (3N)",
                nights_label="03 Nights",
                description="Luxury heritage palace with royal chambers.",
                stars=5,
                category_label="Luxury",
                room_type="Grand Royal Chamber",
                meal_plan="MAPAI (Elite Chef Dynamic Menu) — Private Jacuzzi Access + Wine/Mocktails",
                sort_order=3,
            ),
            ItineraryHotelNested(
                name="Vivanta Dal View / Similar",
                location="Srinagar (3N)",
                nights_label="03 Nights",
                description="Ultra-luxury lake suite with butler service.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Elite Lake Luxury Suite",
                meal_plan="MAPAI (Bespoke Fine Dining) — Personalized Butler + Couple Spa Therapy",
                sort_order=4,
            ),
            ItineraryHotelNested(
                name="Hotel Pine Spring / Similar",
                location="Gulmarg (1N)",
                nights_label="01 Night",
                description="Premium alpine resort with meadow views.",
                stars=4,
                category_label="Premium",
                room_type="Premium Balcony Suite",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=5,
            ),
            ItineraryHotelNested(
                name="The Khyber Himalayan Resort & Spa / Similar",
                location="Gulmarg (1N)",
                nights_label="01 Night",
                description="Luxury spa resort overlooking Apharwat peaks.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=6,
            ),
            ItineraryHotelNested(
                name="Khyber Premium Cottage / Similar",
                location="Gulmarg (1N)",
                nights_label="01 Night",
                description="Ultra-luxury cottage with couple spa access.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Premium Alpine Cottage",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=7,
            ),
            ItineraryHotelNested(
                name="Pine N Peak / Similar",
                location="Pahalgam (1N)",
                nights_label="01 Night",
                description="Premium riverside resort for couples.",
                stars=4,
                category_label="Premium",
                room_type="Premium Valley View Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=8,
            ),
            ItineraryHotelNested(
                name="Welcomhotel Pine N Peak / Similar",
                location="Pahalgam (1N)",
                nights_label="01 Night",
                description="Luxury riverside suite with spa.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Riverside Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=9,
            ),
        ],
        inclusions=_standard_inclusions(
            extra_included=[
                "05 nights handpicked romantic accommodation in Srinagar houseboat, Gulmarg, and Pahalgam",
                "Honeymoon delights — 2x candlelit dinners, 1x premium cake, and floral bed setup",
                "One private sunset shikara ride with floral décor for the couple",
            ]
        ),
    )
    return package, itinerary, JK_004_PEXELS_IMAGES


def build_jk_006(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 25
    package = PackageCreate(
        slug="jk-006-luxury-kashmir-escape",
        destination_id=destination_id,
        title="Luxury Kashmir Escape — Sonamarg, Gulmarg & Palace Stays",
        duration_label="06 Nights / 07 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="Thajiwas Glacier snowfields and Sindh River valley drive at Sonamarg — Meadow of Gold",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Royal cedarwood houseboat nights and The Lalit Grand Palace heritage stay on Dal Lake",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Shalimar Bagh ancient chinar avenue and Mughal fountain terraces",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="The Khyber Himalayan Resort & Spa — Gulmarg's finest luxury mountain address",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Pahalgam Lidder Valley and Betaab meadow excursions",
                sort_order=5,
            ),
            PackageHighlightNested(
                text="Private Innova Crysta with TRAGUIN 24/7 VVIP concierge throughout",
                sort_order=6,
            ),
        ],
        moods=["Luxury", "Family", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="jk-006-luxury-kashmir-escape-itinerary",
        destination_id=destination_id,
        title="Luxury Kashmir Escape — Sonamarg, Gulmarg & Palace Stays",
        duration_label="06 Nights / 07 Days",
        duration_days=7,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="The Definitive Luxury Kashmir Experience",
        overview=(
            "TRAGUIN's most opulent Kashmir journey — a 06-night ultra-premium escape weaving together Srinagar's "
            "royal houseboat heritage, Sonamarg's Thajiwas Glacier snowfields, Gulmarg's Khyber resort elegance, "
            "and Pahalgam's riverside valleys. Stay at The Lalit Grand Palace, ride private shikaras at dawn, "
            "walk Shalimar's chinar avenues, and experience white-glove concierge service at every touchpoint."
        ),
        seo_title="JK-006 | Luxury Kashmir Escape | TRAGUIN Premium Kashmir Tour",
        seo_description=(
            "Luxury 06 Nights / 07 Days Kashmir package (JK-006) covering Sonamarg Thajiwas Glacier, Dal Lake "
            "royal houseboat, Shalimar Bagh, Gulmarg Khyber Resort, and Pahalgam with palace stays and "
            "private transfers. Ideal for luxury travelers and discerning families."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Sonamarg Thajiwas Glacier", sort_order=1),
            ItineraryHighlightNested(text="Royal Houseboat & Lalit Palace", sort_order=2),
            ItineraryHighlightNested(text="Shalimar Chinar Avenue", sort_order=3),
            ItineraryHighlightNested(text="Khyber Gulmarg Luxury Resort", sort_order=4),
            ItineraryHighlightNested(text="Pahalgam Lidder Valley", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival in Srinagar — Royal Houseboat",
                description=(
                    "Your luxury Kashmir escape begins with a VVIP TRAGUIN welcome at Srinagar Airport. "
                    "Transfer by private shikara to your royal cedarwood houseboat on Dal Lake — hand-carved "
                    "interiors, walnut furniture, and panoramic Zabarwan views. Toast with premium kahwa as "
                    "the sun sets over the floating gardens."
                ),
                activities=[
                    "Sightseeing Included: VIP airport transfer, royal shikara arrival, Dal Lake twilight cruise",
                    "Evening Experience: Private Wazwan feast with sommelier-curated mocktail pairings aboard houseboat",
                    "Overnight Stay: Srinagar (Royal Heritage Houseboat on Dal Lake)",
                    "Meals Included: Welcome champagne mocktail & gourmet Wazwan dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Srinagar — Mughal Gardens & Lalit Grand Palace",
                description=(
                    "Explore Shalimar Bagh's ancient chinar tree avenue and cascading fountain terraces built "
                    "for Mughal emperors. Visit Nishat Bagh and Chashme Shahi before checking into The Lalit "
                    "Grand Palace — a former maharaja's residence with Mughal gardens and lake-view suites."
                ),
                activities=[
                    "Sightseeing Included: Shalimar Bagh chinar avenue, Nishat Bagh, Chashme Shahi, Shankaracharya Temple",
                    "Evening Experience: Palace lawn high-tea with live classical Kashmiri music",
                    "Overnight Stay: Srinagar (The Lalit Grand Palace / Luxury Palace Hotel)",
                    "Meals Included: Premium breakfast & palace chef's tasting menu dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Srinagar to Sonamarg — Thajiwas Glacier",
                description=(
                    "Drive along the spectacular Sindh River valley to Sonamarg — the Meadow of Gold at 9,200 ft. "
                    "Trek or pony ride to Thajiwas Glacier's pristine snowfields surrounded by pine forests and "
                    "cascading waterfalls. Return to Srinagar for an evening of palace leisure."
                ),
                activities=[
                    "Sightseeing Included: Sindh River valley drive, Sonamarg golden meadow, Thajiwas Glacier snowfields",
                    "Optional Activities: River rafting on the Sindh or sledging on Thajiwas snow slopes (seasonal)",
                    "Overnight Stay: Srinagar (Luxury Palace Hotel / Royal Houseboat)",
                    "Meals Included: Breakfast & multi-cuisine palace dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Srinagar to Gulmarg — Khyber Resort",
                description=(
                    "Ascend to Gulmarg and check into The Khyber Himalayan Resort & Spa — Kashmir's premier "
                    "luxury mountain address. Spend the afternoon on the meadow golf course or indulge in the "
                    "resort's award-winning spa with Himalayan salt therapies."
                ),
                activities=[
                    "Sightseeing Included: Tangmarg scenic drive, Gulmarg Golf Course, St. Mary's Church, meadow walk",
                    "Evening Experience: Private spa session and sunset kehwa on the Khyber terrace",
                    "Overnight Stay: Gulmarg (The Khyber Himalayan Resort & Spa)",
                    "Meals Included: Breakfast & Khyber chef's signature dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="Gulmarg Gondola & Alpine Heights",
                description=(
                    "Ride the two-phase Gulmarg Gondola to Apharwat Peak for commanding views of the Karakoram "
                    "range. Enjoy snow adventures or alpine meadow picnics before a lavish multi-course dinner "
                    "at your luxury resort beneath star-filled mountain skies."
                ),
                activities=[
                    "Sightseeing Included: Gondola Phase I & II, Apharwat Peak ridge, Kongdoori station panoramas",
                    "Optional Activities: Heli-skiing experience or private photography session on snow meadows",
                    "Overnight Stay: Gulmarg (The Khyber Himalayan Resort & Spa / Luxury Alpine Cottage)",
                    "Meals Included: Glacial breakfast & Khyber tasting menu dinner",
                ],
                sort_order=5,
            ),
            ItineraryDayNested(
                day_number=6,
                title="Gulmarg to Pahalgam — Lidder Valley",
                description=(
                    "Descend through the Kashmir Valley to Pahalgam's Lidder River paradise. Explore Betaab "
                    "Valley's emerald meadows and enjoy a riverside gourmet picnic. Farewell evening with a "
                    "private bonfire and Kashmiri folk performance at your luxury resort."
                ),
                activities=[
                    "Sightseeing Included: Betaab Valley meadows, Lidder River banks, Awantipora ruins en route",
                    "Evening Experience: Farewell bonfire dinner with live Kashmiri folk music and dance",
                    "Overnight Stay: Pahalgam (Luxury Riverside Resort)",
                    "Meals Included: Breakfast & premium farewell riverside dinner",
                ],
                sort_order=6,
            ),
            ItineraryDayNested(
                day_number=7,
                title="Pahalgam to Srinagar — Departure",
                description=(
                    "Enjoy a final valley breakfast before your private luxury transfer to Srinagar Airport. "
                    "Depart Kashmir with the memory of an ultra-premium escape curated exclusively by TRAGUIN."
                ),
                activities=[
                    "Transfers Included: Private luxury transfer Pahalgam to Srinagar Airport",
                    "Meals Included: Sumptuous buffet breakfast",
                ],
                sort_order=7,
            ),
        ],
        hotels=[
            ItineraryHotelNested(
                name="Royal Group of Houseboats / Similar",
                location="Srinagar Dal Lake (2N)",
                nights_label="02 Nights",
                description="Premium royal cedarwood houseboat.",
                stars=4,
                category_label="Deluxe",
                room_type="Royal Houseboat Suite",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=1,
            ),
            ItineraryHotelNested(
                name="Peacock Houseboats / Similar",
                location="Srinagar Dal Lake (2N)",
                nights_label="02 Nights",
                description="Premium hand-carved houseboat with shikara.",
                stars=4,
                category_label="Premium",
                room_type="Premium Houseboat Suite",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=2,
            ),
            ItineraryHotelNested(
                name="The Lalit Grand Palace / Similar",
                location="Srinagar (3N)",
                nights_label="03 Nights",
                description="Luxury heritage palace hotel on Dal Lake.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Palace Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=3,
            ),
            ItineraryHotelNested(
                name="Vivanta Dal View / Similar",
                location="Srinagar (3N)",
                nights_label="03 Nights",
                description="Ultra-luxury lake-view suite with butler.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Luxury Lake View Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=4,
            ),
            ItineraryHotelNested(
                name="Hotel Pine Spring / Similar",
                location="Gulmarg (2N)",
                nights_label="02 Nights",
                description="Premium mountain resort in Gulmarg.",
                stars=4,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=5,
            ),
            ItineraryHotelNested(
                name="The Khyber Himalayan Resort & Spa / Similar",
                location="Gulmarg (2N)",
                nights_label="02 Nights",
                description="Luxury alpine resort at Apharwat foothills.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=6,
            ),
            ItineraryHotelNested(
                name="Khyber Premium Cottage / Similar",
                location="Gulmarg (2N)",
                nights_label="02 Nights",
                description="Ultra-luxury cottage with spa and peak views.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Premium Alpine Cottage",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=7,
            ),
            ItineraryHotelNested(
                name="Pine N Peak / Similar",
                location="Pahalgam (1N)",
                nights_label="01 Night",
                description="Premium riverside resort on the Lidder.",
                stars=4,
                category_label="Premium",
                room_type="Premium Valley View Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=8,
            ),
            ItineraryHotelNested(
                name="Welcomhotel Pine N Peak / Similar",
                location="Pahalgam (1N)",
                nights_label="01 Night",
                description="Luxury riverside resort with spa.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Riverside Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=9,
            ),
            ItineraryHotelNested(
                name="Pahalgam Hotel / Similar",
                location="Pahalgam (1N)",
                nights_label="01 Night",
                description="Ultra-luxury suite with private riverside access.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Luxury Riverside Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=10,
            ),
        ],
        inclusions=_standard_inclusions(
            extra_included=[
                "06 nights ultra-premium accommodation across Srinagar palace, houseboat, Gulmarg Khyber, and Pahalgam",
                "One complimentary palace high-tea and one private sunset shikara experience",
            ]
        ),
    )
    return package, itinerary, JK_006_PEXELS_IMAGES


def build_jk_007(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 26
    package = PackageCreate(
        slug="jk-007-kashmir-great-lakes-trek",
        destination_id=destination_id,
        title="Kashmir Great Lakes Trek — Alpine Expedition",
        duration_label="08 Nights / 09 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="Turquoise Vishansar glacial lake beneath the Kolahoi massif — trek day highlight",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Gadsar Pass summit crossing at 13,800 ft with snow peak panoramas",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Gangabal Lake reflecting sacred Mount Haramukh — the trek's crown jewel",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Nichnai silver birch forests and Satsar interconnected alpine lakes",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="8th-century Naranag temple ruins — archaeological finale at trek end",
                sort_order=5,
            ),
            PackageHighlightNested(
                text="Certified trek leader, camping gear, porters & TRAGUIN expedition concierge",
                sort_order=6,
            ),
        ],
        moods=["Adventure", "Nature", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug="jk-007-kashmir-great-lakes-trek-itinerary",
        destination_id=destination_id,
        title="Kashmir Great Lakes Trek — Alpine Expedition",
        duration_label="08 Nights / 09 Days",
        duration_days=9,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Seven Sacred Lakes — One Legendary Trek",
        overview=(
            "Embark on TRAGUIN's premium Kashmir Great Lakes expedition — one of India's most celebrated "
            "high-altitude treks through seven glacial lakes, birch forests, and alpine meadows between "
            "Sonamarg and Naranag. This 08-night adventure combines Srinagar acclimatization, Sonamarg "
            "base camp, six days of guided trekking through Vishansar, Krishansar, Gadsar Pass, Satsar, "
            "and Gangabal Lake, with premium camping equipment, certified guides, and expedition concierge."
        ),
        seo_title="JK-007 | Kashmir Great Lakes Trek | TRAGUIN Premium Kashmir Adventure",
        seo_description=(
            "Premium 08 Nights / 09 Days Kashmir Great Lakes trek (JK-007) covering Vishansar, Gadsar Pass, "
            "Satsar lakes, Gangabal Lake, and Naranag with certified guides, camping gear, and expedition "
            "support. Ideal for adventure seekers and experienced trekkers."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Vishansar Glacial Lake", sort_order=1),
            ItineraryHighlightNested(text="Gadsar Pass Summit Crossing", sort_order=2),
            ItineraryHighlightNested(text="Gangabal & Mount Haramukh", sort_order=3),
            ItineraryHighlightNested(text="Nichnai Birch Forests", sort_order=4),
            ItineraryHighlightNested(text="Naranag Temple Ruins Finale", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival in Srinagar — Acclimatization",
                description=(
                    "Arrive at Srinagar Airport for your TRAGUIN expedition briefing. Check into a premium "
                    "hotel for altitude acclimatization and equipment check. Meet your certified trek leader "
                    "for route orientation, safety protocols, and a welcome dinner."
                ),
                activities=[
                    "Sightseeing Included: Airport transfer, Dal Lake evening walk (optional)",
                    "Evening Experience: Expedition briefing with trek leader and gear inspection",
                    "Overnight Stay: Srinagar (Premium Hotel — Acclimatization)",
                    "Meals Included: Welcome dinner & trek orientation meal",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Srinagar to Sonamarg — Trek Base Camp",
                description=(
                    "Drive along the Sindh River valley to Sonamarg — the Meadow of Gold and traditional "
                    "starting point for the Great Lakes trek. Check into a premium base camp lodge, final "
                    "gear check, and an early night before the ascent begins."
                ),
                activities=[
                    "Sightseeing Included: Sindh River valley drive, Sonamarg meadow views, base camp setup",
                    "Evening Experience: Pre-trek team dinner and early rest briefing",
                    "Overnight Stay: Sonamarg (Premium Base Camp Lodge)",
                    "Meals Included: Breakfast, lunch & base camp dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Sonamarg to Nichnai — Birch Forest Ascent",
                description=(
                    "Trek begins from Sonamarg through silver birch forests and rolling meadows toward "
                    "Nichnai Pass. Cross the Nichnai stream and camp beside alpine meadows with views of "
                    "snow-capped peaks. First night under canvas in the Kashmir wilderness."
                ),
                activities=[
                    "Sightseeing Included: Nichnai birch forest trail, alpine meadow camps, stream crossings",
                    "Trek Details: Approx. 13 km trek, moderate ascent, camp at Nichnai meadows",
                    "Overnight Stay: Nichnai (Alpine Camping — Premium Tents)",
                    "Meals Included: Hot breakfast, packed trail lunch & camp dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Nichnai to Vishansar Lake via Nichnai Pass",
                description=(
                    "Cross Nichnai Pass at 13,500 ft with sweeping valley views before descending to the "
                    "turquoise Vishansar Lake — the first of the Great Lakes. Camp beside this glacial "
                    "jewel beneath the Kolahoi massif for an unforgettable alpine sunset."
                ),
                activities=[
                    "Sightseeing Included: Nichnai Pass summit, Vishansar Lake turquoise waters, Kolahoi peak views",
                    "Trek Details: Approx. 12 km trek, pass crossing, camp at Vishansar Lake shore",
                    "Overnight Stay: Vishansar Lake (Alpine Camping — Premium Tents)",
                    "Meals Included: Hot breakfast, packed trail lunch & lakeside camp dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="Vishansar to Gadsar via Krishansar & Gadsar Pass",
                description=(
                    "The trek's most dramatic day — visit twin lakes Vishansar and Krishansar, then ascend "
                    "Gadsar Pass at 13,800 ft with panoramic snow peak views. Descend through wildflower "
                    "meadows to camp near Gadsar Lake in the heart of the Great Lakes circuit."
                ),
                activities=[
                    "Sightseeing Included: Krishansar twin lake, Gadsar Pass summit panoramas, Gadsar Lake camp",
                    "Trek Details: Approx. 14 km trek, highest pass crossing, camp near Gadsar Lake",
                    "Overnight Stay: Gadsar Lake (Alpine Camping — Premium Tents)",
                    "Meals Included: Hot breakfast, packed trail lunch & camp dinner",
                ],
                sort_order=5,
            ),
            ItineraryDayNested(
                day_number=6,
                title="Gadsar to Satsar Lakes",
                description=(
                    "Trek through rocky meadows and past shepherd settlements to the interconnected Satsar "
                    "alpine lakes — seven small glacial pools nestled in a high-altitude basin. Camp beside "
                    "the lakes with Mount Harmukh visible on the horizon."
                ),
                activities=[
                    "Sightseeing Included: Satsar interconnected lakes, rocky alpine meadows, shepherd hut encounters",
                    "Trek Details: Approx. 12 km trek, moderate terrain, camp at Satsar lakes basin",
                    "Overnight Stay: Satsar Lakes (Alpine Camping — Premium Tents)",
                    "Meals Included: Hot breakfast, packed trail lunch & camp dinner",
                ],
                sort_order=6,
            ),
            ItineraryDayNested(
                day_number=7,
                title="Satsar to Gangabal Lake — Mount Haramukh",
                description=(
                    "The crown jewel of the trek — ascend to Gangabal Lake at the foot of sacred Mount "
                    "Haramukh (16,870 ft). The lake's mirror-still waters reflect the peak in perfect symmetry. "
                    "Camp at Nundkol Lake nearby for the trek's most spiritual evening."
                ),
                activities=[
                    "Sightseeing Included: Gangabal Lake Haramukh reflection, Nundkol twin lake, high-altitude photography",
                    "Trek Details: Approx. 11 km trek, Gangabal Lake highlight, camp at Nundkol",
                    "Overnight Stay: Gangabal / Nundkol (Alpine Camping — Premium Tents)",
                    "Meals Included: Hot breakfast, packed trail lunch & celebratory camp dinner",
                ],
                sort_order=7,
            ),
            ItineraryDayNested(
                day_number=8,
                title="Gangabal to Naranag — Trek Finale",
                description=(
                    "Descend through pine forests to Naranag village and its 8th-century Shiva temple ruins "
                    "— a fitting archaeological finale. Board your private vehicle for the drive back to "
                    "Srinagar and a well-earned celebration dinner at your premium hotel."
                ),
                activities=[
                    "Sightseeing Included: Naranag ancient temple ruins, pine forest descent, Srinagar valley return",
                    "Trek Details: Approx. 13 km descent, trek ends at Naranag, transfer to Srinagar",
                    "Overnight Stay: Srinagar (Premium Hotel — Recovery & Celebration)",
                    "Meals Included: Hot breakfast, trail lunch & celebration dinner in Srinagar",
                ],
                sort_order=8,
            ),
            ItineraryDayNested(
                day_number=9,
                title="Srinagar Departure",
                description=(
                    "Enjoy a leisurely breakfast and optional Dal Lake shikara ride before your private "
                    "transfer to Srinagar Airport. Depart with the Great Lakes etched forever in memory "
                    "by TRAGUIN's expedition team."
                ),
                activities=[
                    "Transfers Included: Private luxury airport drop-off",
                    "Meals Included: Sumptuous buffet breakfast",
                ],
                sort_order=9,
            ),
        ],
        hotels=[
            ItineraryHotelNested(
                name="Hotel Grand Plaza / Similar",
                location="Srinagar (2N)",
                nights_label="02 Nights",
                description="Deluxe hotel for acclimatization and recovery.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAP (Breakfast & Dinner)",
                sort_order=1,
            ),
            ItineraryHotelNested(
                name="Hotel Pine Spring Srinagar / Similar",
                location="Srinagar (2N)",
                nights_label="02 Nights",
                description="Premium hotel with expedition support desk.",
                stars=4,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAP (Premium Menu)",
                sort_order=2,
            ),
            ItineraryHotelNested(
                name="The Lalit Grand Palace / Similar",
                location="Srinagar (2N)",
                nights_label="02 Nights",
                description="Luxury palace hotel post-trek recovery.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAP (Elite Chef Menu)",
                sort_order=3,
            ),
            ItineraryHotelNested(
                name="Vivanta Dal View / Similar",
                location="Srinagar (2N)",
                nights_label="02 Nights",
                description="Ultra-luxury recovery suite with spa access.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Luxury Suite",
                meal_plan="MAP (Bespoke Fine Dining)",
                sort_order=4,
            ),
            ItineraryHotelNested(
                name="Sonamarg Glacier Heights / Similar",
                location="Sonamarg (1N)",
                nights_label="01 Night",
                description="Deluxe base camp lodge before trek.",
                stars=4,
                category_label="Deluxe",
                room_type="Standard Room",
                meal_plan="Full Board (Pre-Trek Meals)",
                sort_order=5,
            ),
            ItineraryHotelNested(
                name="Hotel Snowland Sonamarg / Similar",
                location="Sonamarg (1N)",
                nights_label="01 Night",
                description="Premium lodge with gear storage and briefing room.",
                stars=4,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="Full Board (Pre-Trek Meals)",
                sort_order=6,
            ),
            ItineraryHotelNested(
                name="TRAGUIN Premium Alpine Camp / Similar",
                location="Trek Route (5N)",
                nights_label="05 Nights",
                description="Luxury trekking tents with dining tent and sleeping systems.",
                stars=4,
                category_label="Luxury",
                room_type="Premium Alpine Tent (Twin Share)",
                meal_plan="Full Board (Trail Meals & Hot Camp Dinners)",
                sort_order=7,
            ),
            ItineraryHotelNested(
                name="TRAGUIN Expedition Camp / Similar",
                location="Trek Route (5N)",
                nights_label="05 Nights",
                description="Ultra-premium expedition tents with heated dining and porter support.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Expedition Suite Tent (Private)",
                meal_plan="Full Board (Gourmet Trail & Camp Cuisine)",
                sort_order=8,
            ),
        ],
        inclusions=_trek_inclusions(),
    )
    return package, itinerary, JK_007_PEXELS_IMAGES


def build_jk_010(destination_id: str) -> tuple[PackageCreate, ItineraryCreate, list]:
    featured_sort_order = 27
    package = PackageCreate(
        slug="jk-010-kashmir-complete",
        destination_id=destination_id,
        title="Kashmir Complete — The Ultimate Valley Discovery",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            PackageHighlightNested(
                text="Panoramic Dal Lake aerial views — Zabarwan range, floating gardens, and shikara culture",
                sort_order=1,
            ),
            PackageHighlightNested(
                text="Hazratbal Shrine white marble elegance on the shores of Dal Lake",
                sort_order=2,
            ),
            PackageHighlightNested(
                text="Sonamarg golden meadows beside the Sindh River — Thajiwas Glacier excursion",
                sort_order=3,
            ),
            PackageHighlightNested(
                text="Gulmarg Gondola Kongdoori phase with Karakoram range snow peak views",
                sort_order=4,
            ),
            PackageHighlightNested(
                text="Pampore saffron harvest fields and Awantipora ancient temple ruins",
                sort_order=5,
            ),
            PackageHighlightNested(
                text="Private Innova Crysta with TRAGUIN 24/7 elite concierge across all valleys",
                sort_order=6,
            ),
        ],
        moods=["Family", "Luxury", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="jk-010-kashmir-complete-itinerary",
        destination_id=destination_id,
        title="Kashmir Complete — The Ultimate Valley Discovery",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="On Request (Premium Curated)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Every Icon of Kashmir — One Definitive Journey",
        overview=(
            "TRAGUIN's most comprehensive Kashmir itinerary — an 07-night grand discovery covering every "
            "iconic landscape from Dal Lake houseboats and Hazratbal Shrine to Sonamarg's golden meadows, "
            "Gulmarg's Gondola heights, Pahalgam's Lidder Valley, Pampore saffron fields, and Awantipora's "
            "ancient ruins. Handpicked resorts, private chauffeur transfers, and curated experiences at "
            "each destination make this the definitive Kashmir vacation."
        ),
        seo_title="JK-010 | Kashmir Complete | TRAGUIN Premium Kashmir Tour",
        seo_description=(
            "Luxury 07 Nights / 08 Days complete Kashmir package (JK-010) covering Dal Lake, Hazratbal, "
            "Sonamarg, Gulmarg Gondola, Pahalgam, Pampore saffron, and Awantipora with premium stays and "
            "private transfers. Ideal for families and first-time Kashmir visitors."
        ),
        is_featured=True,
        featured_sort_order=featured_sort_order,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Dal Lake Panorama & Houseboat", sort_order=1),
            ItineraryHighlightNested(text="Hazratbal Shrine & Mughal Gardens", sort_order=2),
            ItineraryHighlightNested(text="Sonamarg Golden Meadows", sort_order=3),
            ItineraryHighlightNested(text="Gulmarg Gondola Kongdoori", sort_order=4),
            ItineraryHighlightNested(text="Pahalgam & Saffron Fields", sort_order=5),
        ],
        days=[
            ItineraryDayNested(
                day_number=1,
                title="Arrival in Srinagar — Dal Lake Houseboat",
                description=(
                    "Your complete Kashmir journey begins with a TRAGUIN welcome at Srinagar Airport. Transfer "
                    "by shikara to your heritage houseboat on Dal Lake for a panoramic introduction to the "
                    "valley — floating gardens, Zabarwan peaks, and the timeless rhythm of lake life."
                ),
                activities=[
                    "Sightseeing Included: Airport transfer, Dal Lake shikara welcome cruise, floating garden views",
                    "Evening Experience: Traditional Wazwan dinner aboard your houseboat with lake views",
                    "Overnight Stay: Srinagar (Heritage Houseboat on Dal Lake)",
                    "Meals Included: Welcome kahwa & authentic Kashmiri dinner",
                ],
                sort_order=1,
            ),
            ItineraryDayNested(
                day_number=2,
                title="Srinagar — Hazratbal, Gardens & Old City",
                description=(
                    "Explore Srinagar's spiritual and horticultural heritage — the white marble Hazratbal "
                    "Shrine on Dal Lake's shore, terraced Mughal gardens of Shalimar and Nishat Bagh, and "
                    "the aromatic spice lanes of the old city with Pashmina and walnut woodcraft ateliers."
                ),
                activities=[
                    "Sightseeing Included: Hazratbal Shrine, Shalimar Bagh, Nishat Bagh, Shankaracharya Temple, old city bazaar",
                    "Optional Activities: Pari Mahal terraced gardens and floating vegetable market shikara (early morning)",
                    "Overnight Stay: Srinagar (Heritage Houseboat / Premium Lake-View Hotel)",
                    "Meals Included: Premium breakfast & multi-cuisine dinner",
                ],
                sort_order=2,
            ),
            ItineraryDayNested(
                day_number=3,
                title="Srinagar to Sonamarg — Golden Meadows",
                description=(
                    "Drive the spectacular Sindh River valley to Sonamarg — the Meadow of Gold. Trek or pony "
                    "ride to Thajiwas Glacier's snowfields, walk beside golden wildflower meadows, and "
                    "capture the dramatic Sindh River cutting through pine forests."
                ),
                activities=[
                    "Sightseeing Included: Sindh River valley drive, Sonamarg golden meadow, Thajiwas Glacier snowfields",
                    "Optional Activities: River rafting on the Sindh or sledging on Thajiwas snow slopes (seasonal)",
                    "Overnight Stay: Sonamarg (Premium Valley Lodge) or Srinagar (Premium Hotel)",
                    "Meals Included: Breakfast & mountain dinner",
                ],
                sort_order=3,
            ),
            ItineraryDayNested(
                day_number=4,
                title="Sonamarg / Srinagar to Gulmarg — Gondola Heights",
                description=(
                    "Ascend to Gulmarg and ride the iconic two-phase Gondola to Kongdoori and Apharwat Peak "
                    "for commanding Karakoram range views. Spend the afternoon on snow activities or alpine "
                    "meadow walks before checking into your premium mountain resort."
                ),
                activities=[
                    "Sightseeing Included: Gulmarg Golf Course, Gondola Phase I & II, Kongdoori station, Apharwat ridge",
                    "Evening Experience: Mountain sunset kehwa and bonfire at your alpine resort",
                    "Overnight Stay: Gulmarg (Premium / Luxury Mountain Resort)",
                    "Meals Included: Breakfast & hearty mountain dinner",
                ],
                sort_order=4,
            ),
            ItineraryDayNested(
                day_number=5,
                title="Gulmarg Leisure & Meadow Exploration",
                description=(
                    "A full day to savor Gulmarg at your own pace — golf course walks, St. Mary's Church "
                    "heritage visit, optional skiing or snowboarding, or a relaxed spa day at The Khyber. "
                    "Families enjoy pony rides across wildflower meadows in summer months."
                ),
                activities=[
                    "Sightseeing Included: Gulmarg meadow, St. Mary's Church, Tangmarg apple orchards en route views",
                    "Optional Activities: Skiing, snow scooter, golf course walk, or Khyber spa session",
                    "Overnight Stay: Gulmarg (Premium / Luxury Mountain Resort)",
                    "Meals Included: Breakfast & multi-cuisine dinner",
                ],
                sort_order=5,
            ),
            ItineraryDayNested(
                day_number=6,
                title="Gulmarg to Pahalgam — Lidder Valley",
                description=(
                    "Descend through the Kashmir Valley to Pahalgam via Awantipora's 9th-century temple ruins. "
                    "Explore Betaab Valley's emerald meadows and the crystal Lidder River before a riverside "
                    "evening at your premium valley resort."
                ),
                activities=[
                    "Sightseeing Included: Awantipora ancient temple ruins, Betaab Valley meadows, Lidder River viewpoints",
                    "Evening Experience: Riverside bonfire with Kashmiri folk music at your resort",
                    "Overnight Stay: Pahalgam (Premium Riverside Valley Resort)",
                    "Meals Included: Breakfast & riverside barbecue dinner",
                ],
                sort_order=6,
            ),
            ItineraryDayNested(
                day_number=7,
                title="Pahalgam to Srinagar — Saffron Fields & Farewell",
                description=(
                    "Return to Srinagar via Pampore's legendary saffron fields — a purple-gold spectacle in "
                    "autumn harvest season. Final sunset shikara cruise on Dal Lake and a farewell Wazwan "
                    "feast with live santoor performance."
                ),
                activities=[
                    "Sightseeing Included: Pampore saffron fields, floating vegetable market, final Dal Lake shikara cruise",
                    "Evening Experience: Farewell Wazwan dinner with live santoor performance on Dal Lake",
                    "Overnight Stay: Srinagar (Heritage Houseboat / Luxury Lake-View Hotel)",
                    "Meals Included: Breakfast & premium farewell Wazwan dinner",
                ],
                sort_order=7,
            ),
            ItineraryDayNested(
                day_number=8,
                title="Srinagar Departure",
                description=(
                    "Enjoy a final lakeside breakfast as mist rises off Dal Lake. Your private vehicle "
                    "transfers you to Srinagar Airport with the complete Kashmir valley forever in memory "
                    "— curated exclusively by TRAGUIN."
                ),
                activities=[
                    "Transfers Included: Private luxury airport drop-off",
                    "Meals Included: Sumptuous buffet breakfast",
                ],
                sort_order=8,
            ),
        ],
        hotels=[
            ItineraryHotelNested(
                name="New Alexandra / Similar Heritage Houseboat",
                location="Srinagar Dal Lake (3N)",
                nights_label="03 Nights",
                description="Deluxe cedarwood houseboat on Dal Lake.",
                stars=4,
                category_label="Deluxe",
                room_type="Deluxe Houseboat Suite",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=1,
            ),
            ItineraryHotelNested(
                name="Peacock Houseboats / Similar",
                location="Srinagar Dal Lake (3N)",
                nights_label="03 Nights",
                description="Premium hand-carved houseboat with shikara.",
                stars=4,
                category_label="Premium",
                room_type="Premium Houseboat Suite",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=2,
            ),
            ItineraryHotelNested(
                name="The Lalit Grand Palace / Similar",
                location="Srinagar (3N)",
                nights_label="03 Nights",
                description="Luxury heritage palace overlooking Dal Lake.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Palace Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=3,
            ),
            ItineraryHotelNested(
                name="Vivanta Dal View / Similar",
                location="Srinagar (3N)",
                nights_label="03 Nights",
                description="Ultra-luxury lake-view suite with butler.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Luxury Lake View Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=4,
            ),
            ItineraryHotelNested(
                name="Hotel Hilltop / Similar",
                location="Gulmarg (2N)",
                nights_label="02 Nights",
                description="Deluxe mountain resort in Gulmarg.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=5,
            ),
            ItineraryHotelNested(
                name="Hotel Pine Spring / Similar",
                location="Gulmarg (2N)",
                nights_label="02 Nights",
                description="Premium resort with meadow and peak views.",
                stars=4,
                category_label="Premium",
                room_type="Premium Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=6,
            ),
            ItineraryHotelNested(
                name="The Khyber Himalayan Resort & Spa / Similar",
                location="Gulmarg (2N)",
                nights_label="02 Nights",
                description="Luxury alpine resort at Apharwat foothills.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=7,
            ),
            ItineraryHotelNested(
                name="Khyber Premium Cottage / Similar",
                location="Gulmarg (2N)",
                nights_label="02 Nights",
                description="Ultra-luxury cottage with spa and peak views.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Premium Alpine Cottage",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=8,
            ),
            ItineraryHotelNested(
                name="Hotel Heevan / Similar",
                location="Pahalgam (1N)",
                nights_label="01 Night",
                description="Deluxe riverside resort on the Lidder.",
                stars=4,
                category_label="Deluxe",
                room_type="Executive Room",
                meal_plan="MAPAI (Breakfast & Dinner)",
                sort_order=9,
            ),
            ItineraryHotelNested(
                name="Pine N Peak / Similar",
                location="Pahalgam (1N)",
                nights_label="01 Night",
                description="Premium valley resort with pine forest views.",
                stars=4,
                category_label="Premium",
                room_type="Premium Valley View Room",
                meal_plan="MAPAI (Premium Buffet Menu)",
                sort_order=10,
            ),
            ItineraryHotelNested(
                name="Welcomhotel Pine N Peak / Similar",
                location="Pahalgam (1N)",
                nights_label="01 Night",
                description="Luxury riverside resort with spa.",
                stars=5,
                category_label="Luxury",
                room_type="Luxury Room / Suite",
                meal_plan="MAPAI (Elite Chef Dynamic Menu)",
                sort_order=11,
            ),
            ItineraryHotelNested(
                name="Pahalgam Hotel / Similar",
                location="Pahalgam (1N)",
                nights_label="01 Night",
                description="Ultra-luxury suite with private riverside access.",
                stars=5,
                category_label="Ultra Luxury",
                room_type="Luxury Riverside Suite",
                meal_plan="MAPAI (Bespoke Fine Dining)",
                sort_order=12,
            ),
        ],
        inclusions=_standard_inclusions(
            extra_included=[
                "07 nights premium accommodation across Srinagar houseboat, Gulmarg, and Pahalgam",
                "One complimentary Dal Lake shikara cruise and one Sonamarg meadow excursion",
            ]
        ),
    )
    return package, itinerary, JK_010_PEXELS_IMAGES
