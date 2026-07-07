"""Builder functions for JK-011 through JK-017 Kashmir domestic packages."""

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

KASHMIR_SLUG = "kashmir"
KASHMIR_DESTINATION_ID = "1e5cb202-978f-48c9-92ca-13b341a4a9b5"


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


def build_jk_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "JK-011"
    tour_code = "TRG-JK-011"
    title = "Grand Kashmir Panorama"
    duration = "06 Nights / 07 Days"
    slug = "jk-011-grand-kashmir-panorama"
    itin_slug = "jk-011-grand-kashmir-panorama-itinerary"
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
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Kashmir / India | Category: Luxury Holidays", 2),
            _ph("Destinations Covered: Srinagar • Gulmarg • Pahalgam • Sonamarg", 3),
            _ph("Ideal for: Couples, Connoisseurs & Luxury Seekers", 4),
            _ph("Best season: March to November (Year-round luxury)", 5),
            _ph("Travel Month: Tailored Premium Flexible Departures", 6),
            _ph("Group / FIT: Bespoke Private Luxury FIT Tour", 7),
            _ph("Vehicle: Dedicated Luxury Chauffeur MUV (Innova Crysta) at full-time disposal", 8),
            _ph("Meal Plan: Modified American Plan (Artisan Buffet Breakfasts & Gourmet Dinners Included)", 9),
            _ph(
                "Route Portfolio: Srinagar Arrival → Sonamarg Excursion → Pahalgam Retreat → "
                "Gulmarg Alpines → Srinagar Return",
                10,
            ),
            _ph(
                "TRAGUIN Curated Experience Note: Exclusive private shikara rides over hidden canals, "
                "pre-booked premium phase-II Gondola tickets to prevent crowds, handpicked boutique luxury "
                "resorts, and dedicated local travel assistant care throughout.",
                11,
            ),
            _ph(
                "Shopping & Local Experiences: Lal Chowk, Polo View High Street, and floating artisan markets. "
                "Famous Items: Pure Pashmina shawls, hand-knotted silk carpets, organic saffron, and carved "
                "walnut wood souvenirs.",
                12,
            ),
            _ph(
                "Important Notes: Gondola cable car operations are heavily dependent on local wind and weather "
                "safety conditions. Please pack appropriate warm winter jackets and thermal layers, as high peaks "
                "like Apharwat remain cold year-round. Hotel confirmations are subject to availability at the "
                "exact time of token reservation payments.",
                13,
            ),
        ],
        moods=["Luxury", "Honeymoon", "Family"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Class)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Grand Kashmir Panorama — A Premium Luxury Holiday Escape",
        overview=(
            "Step into paradise on Earth. TRAGUIN invites you to live an opulent fairytale across the breathtaking "
            "landscapes of Kashmir. Surrender to a world of mist-covered alpine meadows, crystal rivers, and premium "
            "stays meticulously arranged for our discerning guests. From waking up to snowy peaks to relaxing in heritage "
            "properties, this Luxury Kashmir Holiday presents scenic beauty and curated experiences that blossom into "
            "unforgettable memories.\n\n"
            "Securing an authentic Best Kashmir Tour Package or booking a magical Kashmir Honeymoon Package requires "
            "balancing rich cultural storytelling with unmatched comfort. Known historically for its breathtaking alpine "
            "geography, Kashmir is home to legendary architectural and natural highlights. This Kashmir Family Tour "
            "exposes you seamlessly to the Top Tourist Places in Kashmir, from the geometric terraces of the Shalimar "
            "Mughal Gardens to the snowy ridges of Apharwat Peak.\n\n"
            "The Best Time to Visit Kashmir spans from spring's vibrant tulip blossoms in April to autumn's golden "
            "chinars in October. By selecting our premium TRAGUIN Kashmir Packages, you unlock a highly sophisticated "
            "Premium Kashmir Experience featuring private mountain guides, secure luxury transportation, and curated "
            "entry to stunning Kashmir Sightseeing spots."
        ),
        seo_title="JK-011 | Grand Kashmir Panorama Premium Tour | TRAGUIN",
        seo_description=(
            "Premium 06 Nights / 07 Days Kashmir package (JK-011 / TRG-JK-011): Srinagar, Sonamarg, Pahalgam, "
            "Gulmarg Gondola, Dal Lake Shikara, Mughal Gardens, and 3-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Dal Lake Shikara cruise, Sonamarg & Thajiwas Glacier excursion", 1),
            _ih("Mughal Gardens, Pahalgam alpine valleys (Betaab, Aru, Chandanwari)", 2),
            _ih("Gulmarg Gondola Phase I & II to Apharwat Peak", 3),
            _ih("TRAGUIN Signature Experience: Private traditional live music and premium Kehwa tasting session", 4),
            _ih("Curated by Experts: Fully pre-booked gondola and park entries to completely avoid standing in long public lines", 5),
            _ih("Personalized Assistance: Professional drivers with deep experience navigating mountain routes safely", 6),
            _ih(
                "Instagram Spots: The wooden balconies of old houseboats, Betaab Valley pine clearings, and snow paths at Apharwat Peak",
                7,
            ),
        ],
        days=[
            _day(
                1,
                "Arrival in Srinagar & Elegant Lake Shikara Cruise",
                (
                    "Your premium holiday starts as you land at Srinagar International Airport. A dedicated TRAGUIN "
                    "representative will extend a warm welcome and transfer you in a luxury vehicle to your iconic "
                    "premium houseboat or luxury lake resort. After a smooth check-in and an afternoon of relaxation, "
                    "step onto a hand-carved wooden Shikara to glide gracefully across Dal Lake as the setting sun colors "
                    "the snow-capped mountain tops."
                ),
                [
                    "Sightseeing Included: Dal Lake classic cruise, floating vegetable markets, and historical island corners.",
                    "Evening Experience: A traditional welcome Kashmiri Kehwa tea-serving ceremony hosted on the deck of your premium accommodation.",
                    "Overnight Stay: Handpicked Premium Luxury Houseboat / Lakefront Resort",
                    "Meals Included: Welcome Refreshments & Gourmet Dinner",
                ],
            ),
            _day(
                2,
                "Sonamarg Excursion — The Meadow of Gold",
                (
                    "Indulge in a beautiful morning drive along the roaring Sindh River toward Sonamarg, famously called "
                    "the 'Meadow of Gold'. Marvel at the dramatic, breathtaking landscapes shifting into deep pine forests "
                    "and snowy crags. Walk effortlessly along the mountain tracks or charter a local pony ride to approach "
                    "the ancient, shimmering blue Thajiwas Glacier."
                ),
                [
                    "Sightseeing Included: Sonamarg Meadows, Sindh River Valley view loops, and Thajiwas Glacier trail vantage points.",
                    "Optional Activities: A comfortable luxury vehicle extension up toward the high-altitude Zojila Pass viewpoint.",
                    "Overnight Stay: Luxury Hotel / Resort in Srinagar",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                3,
                "Srinagar Mughal Heritage to the Valley of Pahalgam",
                (
                    "Begin the day with an artistic tour through the grand Mughal architecture. Stroll down the royal, "
                    "fountain-filled paths of Nishat Bagh and Shalimar Bagh. In the afternoon, take a picturesque drive "
                    "past saffron fields toward Pahalgam, the famous 'Valley of Shepherds'. Check into your luxury riverside "
                    "forest villa and fall asleep to the gentle, rhythmic sound of the flowing Lidder River."
                ),
                [
                    "Sightseeing Included: Shalimar Bagh, Nishat Garden, Avantipur Temple remnants, and Pampore Saffron Fields.",
                    "Evening Experience: A relaxing stroll across the manicured riverside estate pathways of your luxury hotel property.",
                    "Overnight Stay: Handpicked Luxury Resort in Pahalgam",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                4,
                "Pahalgam — Alpine Valleys Excursion",
                (
                    "Enjoy a beautiful mountain morning in Pahalgam. Board a private local vehicle to explore the magnificent "
                    "alpine valleys. Witness the incredible scenic beauty of Betaab Valley, named after legendary Hindi cinema, "
                    "and the pine-shrouded green clearings of Aru Valley. Spend the afternoon taking photos by the crystal waters "
                    "of Chandanwari."
                ),
                [
                    "Sightseeing Included: Betaab Valley, Aru Valley meadows, and Chandanwari snowy streams.",
                    "Evening Experience: A warm, private wood-fired candle-lit dinner featuring multi-course regional delicacies.",
                    "Overnight Stay: Handpicked Luxury Resort in Pahalgam",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                5,
                "Translocation to the Alpine Fields of Gulmarg",
                (
                    "Drive out today through beautiful countryside lines toward Gulmarg, the iconic 'Meadow of Flowers'. "
                    "Arriving at this spectacular high-altitude plain, check into your ultra-luxury resort featuring heated rooms "
                    "and expansive mountain windows. Spend your afternoon wandering the high meadows or practicing on the world's "
                    "highest green golf course layout."
                ),
                [
                    "Sightseeing Included: Gulmarg Meadows, St. Mary's Church, and the historic Maharaja Palace trail.",
                    "Evening Experience: High mountain tea paired with gourmet local bakery selections overlooking the outer loop trail.",
                    "Overnight Stay: Ultra-Luxury Mountain Resort in Gulmarg",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                6,
                "The High Gondola Ascent & Return to Srinagar",
                (
                    "Today brings a thrilling peak experience. Board the iconic Gulmarg Gondola cable car with pre-booked premium "
                    "passes arranged by TRAGUIN. Float above high pine trees up to Phase 1 (Kongdoori), then rise to the majestic "
                    "heights of Phase 2 (Apharwat Peak) at 14,000 feet. Walk on fields of pristine snow and capture the magnificent "
                    "mountain ranges bordering neighboring lands. In the afternoon, drive back to Srinagar for your final evening."
                ),
                [
                    "Sightseeing Included: Gondola Cable Car Ride (Phase I & II), Apharwat Peak viewpoints, and Nigeen Lake artisan drives.",
                    "Evening Experience: A special premium farewell dinner with live instrumental santoor music performance arranged privately.",
                    "Overnight Stay: Luxury City Resort in Srinagar",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                7,
                "Farewell Paradise",
                (
                    "Savor an early morning breakfast while gazing at the misty mountain ranges. Take a final stroll to pick up "
                    "fine woolens or walnuts before your dedicated chauffeur transfers you seamlessly to Srinagar International "
                    "Airport. Your luxury holiday concludes smoothly, leaving you with beautiful, lifelong memories."
                ),
                [
                    "Meals Included: Sumptuous Buffet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "The Khyber Himalayan Resort & Spa, Gulmarg | The Grand Mumtaz / Radisson Resort, Pahalgam | The Lalit Grand Palace, Srinagar",
                "Gulmarg / Pahalgam / Srinagar",
                "06 Nights",
                "Ultra Luxury",
                "Handpicked Ultra Luxury Rooms",
                "MAP (Breakfast + Dinner)",
                5,
                1,
                description="OPTION 01 – ULTRA LUXURY: The Khyber Himalayan Resort & Spa, Gulmarg | The Grand Mumtaz / Radisson Resort, Pahalgam | The Lalit Grand Palace, Srinagar (6 Nights)",
            ),
            _hotel(
                "Kolahoi Green Resort, Gulmarg | Welcomhotel by ITC Hotels, Pahalgam | Fortune Resort Heevan, Srinagar",
                "Gulmarg / Pahalgam / Srinagar",
                "06 Nights",
                "Luxury",
                "Handpicked Luxury Rooms",
                "MAP (Breakfast + Dinner)",
                5,
                2,
                description="OPTION 02 – LUXURY: Kolahoi Green Resort, Gulmarg | Welcomhotel by ITC Hotels, Pahalgam | Fortune Resort Heevan, Srinagar (6 Nights)",
            ),
            _hotel(
                "Hotel Vintage, Gulmarg | Hotel Pine Spring, Pahalgam | Grand Minaret, Srinagar",
                "Gulmarg / Pahalgam / Srinagar",
                "06 Nights",
                "Premium",
                "Handpicked Premium Rooms",
                "MAP (Breakfast + Dinner)",
                4,
                3,
                description="OPTION 03 – PREMIUM: Hotel Vintage, Gulmarg | Hotel Pine Spring, Pahalgam | Grand Minaret, Srinagar (6 Nights)",
            ),
        ],
        inclusions=[
            _inc_included("06 Nights accommodation in handpicked, top-tier luxury hotels, mountain resorts & houseboats.", 1),
            _inc_included("Daily artisan breakfasts and multi-cuisine gourmet dinners at all resort locations.", 2),
            _inc_included(
                "Complete private airport transfers and long-distance sightseeing in an air-conditioned luxury MUV (Innova Crysta).",
                3,
            ),
            _inc_included("Pre-arranged premium tickets for the Gulmarg Gondola cable car ride (Both Phase I & Phase II).", 4),
            _inc_included("Complimentary 01-Hour private luxury Shikara boat cruise on Dal Lake with welcome amenities.", 5),
            _inc_included(
                "Private internal valley vehicles for localized sightseeing loops within Pahalgam (Aru, Betaab, Chandanwari).",
                6,
            ),
            _inc_included("Continuous 24/7 dedicated TRAGUIN on-ground destination management support.", 7),
            _inc_excluded("Domestic or international flight ticketing costs to Srinagar.", 8),
            _inc_excluded("Local horse/pony rentals and camera equipment permissions.", 9),
            _inc_excluded("Personal costs such as laundry, phone calls, premium spa sessions, or alcoholic beverages.", 10),
        ],
    )
    return package, itinerary


def build_jk_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "JK-012"
    tour_code = "TRG-JK-012"
    title = "Royal Gulmarg Snow Luxury & Srinagar Serenade"
    duration = "04 Nights / 05 Days"
    slug = "jk-012-royal-gulmarg-snow-luxury-srinagar-serenade"
    itin_slug = "jk-012-royal-gulmarg-snow-luxury-srinagar-serenade-itinerary"
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
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Jammu & Kashmir / India | Category: Luxury Wilderness & Snow", 2),
            _ph("Destinations Covered: Srinagar • Gulmarg Snow Kingdom", 3),
            _ph("Ideal for: Luxury Honeymooners, Families & Connoisseurs", 4),
            _ph("Best season: December to March (For Snow Luxury)", 5),
            _ph("Travel Month: Winter Snow Season Special", 6),
            _ph("Group / FIT: Ultra-Luxury Customized Private FIT Tour", 7),
            _ph("Vehicle: Private Premium Heated Luxury SUV (Innova Crysta / Defender) at disposal", 8),
            _ph("Meal Plan: Modified American Plan (Gourmet Breakfasts & Traditional Dinners Included)", 9),
            _ph("Route: Srinagar Airport Arrival → Royal Dal Lake → Gulmarg Snow Kingdom → Srinagar Departure", 10),
            _ph(
                "TRAGUIN Curated Experience Note: Pre-booked Phase 1 & Phase 2 Gondola tickets avoiding all public queues, "
                "private luxury houseboat experience, traditional hand-warmer Kangri presentation, and 24/7 dedicated local VIP concierge support.",
                11,
            ),
            _ph(
                "Shopping & Local Experiences: Hand-knotted silk carpets, genuine Pashmina wool shawls, pure Kashmiri saffron, "
                "walnuts, and papier-mâché art boxes at the heritage Lal Chowk markets.",
                12,
            ),
            _ph(
                "Important Notes: Gulmarg Gondola tickets are highly restricted and booked well in advance; immediate confirmation is requested. "
                "Please carry appropriate heavy winter inner thermals, gloves, woolen caps, and moisture-resistant winter gear. "
                "Prepaid mobile network connections do not operate inside Jammu & Kashmir; please ensure you carry a postpaid roaming connection.",
                13,
            ),
        ],
        moods=["Luxury", "Snow", "Honeymoon"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Class)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Royal Gulmarg Snow Luxury & Srinagar Serenade — 04 Nights / 05 Days of Curated Grandeur",
        overview=(
            "Welcome to paradise on earth. TRAGUIN invites you to step into a winter wonderland of absolute indulgence. "
            "Behold the breathtaking landscapes of Kashmir, where snow-laden Chinar trees frame majestic frozen lakes "
            "and alpine peaks meet timeless royal hospitality. This bespoke Luxury Kashmir Holiday brings you exclusive "
            "curated experiences, seamless private transfers, and stays in the region's finest premium establishments, "
            "creating unforgettable memories to cherish forever.\n\n"
            "When searching for the Best Kashmir Tour Package or planning an elite Kashmir Honeymoon Package, "
            "discerning couples and families look for a seamless blend of natural grandeur and flawless operational comfort. "
            "This dedicated Kashmir Family Tour showcases the absolute finest Top Tourist Places in Kashmir, including the "
            "iconic Shankaracharya temple overlooking the valley, the Mughal-era pleasure gardens, and the pristine "
            "snowfields of Gulmarg.\n\n"
            "The winter alpine season stands as the undisputed Best Time to Visit Kashmir for snow enthusiasts. Our "
            "TRAGUIN Kashmir Packages ensure a highly distinguished Premium Kashmir Experience, seamlessly pairing "
            "deep-comfort heated luxury transportation with exclusive handpicked hotels. From morning shikara rides "
            "amidst the floating markets to soaring heights on the Gulmarg cable car, every moment is crafted into a "
            "spectacular masterpiece of Kashmir Sightseeing."
        ),
        seo_title="JK-012 | Royal Gulmarg Snow Luxury & Srinagar Serenade | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Kashmir winter package (JK-012 / TRG-JK-012): Dal Lake houseboat, "
            "Mughal Gardens, Gulmarg Gondola Phase I & II, Shankaracharya Temple, and 3-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Sunset Shikara cruise on Dal Lake and ultra-luxury houseboat stay", 1),
            _ih("Mughal Gardens, Pari Mahal, Shankaracharya Temple heritage trail", 2),
            _ih("Gulmarg Snow Kingdom with Phase 1 & Phase 2 Gondola excursion", 3),
            _ih("TRAGUIN Signature Experience: Private, exclusive local artisan carpet-weaving preview with heritage storytelling", 4),
            _ih("Curated by Experts: Fully pre-secured Gondola slots ensuring you avoid long cold public wait times entirely", 5),
            _ih("Personalized Assistance: Dedicated baggage escorts at all boat boarding docks for flawless transit transitions", 6),
            _ih(
                "Instagram Spots: Floating flower markets on Dal Lake at dawn, glass conservatory views at The Khyber, "
                "and standing at Apharwat Peak with a snow mountain backdrop",
                7,
            ),
        ],
        days=[
            _day(
                1,
                "Arrival in Kashmir & Memoirs of the Royal Houseboat",
                (
                    "Your premium holiday begins as you land at Srinagar Airport. A personal TRAGUIN luxury travel "
                    "representative welcomes you warmly and escorts you to your private heated luxury vehicle. Drive past "
                    "rows of weeping willows to the edge of the legendary Dal Lake. Step aboard a beautifully carved, "
                    "ultra-luxury wooden houseboat. In the evening, unwind on a private, plushly cushioned Shikara boat "
                    "ride as the setting sun paints the misty Zabarwan Range in hues of gold and violet."
                ),
                [
                    "Sightseeing Included: Sunset Shikara cruise on Dal Lake, visiting Char Chinar and the floating gardens.",
                    "Evening Experience: A traditional welcome Kashmiri Kahwa tea service served with saffron and roasted almonds on the houseboat deck.",
                    "Overnight Stay: Handpicked Ultra-Luxury Houseboat (Dal Lake / Nigeen Lake)",
                    "Meals Included: Welcome Amenities & Gourmet Dinner",
                ],
            ),
            _day(
                2,
                "Mughal Grandeur & Imperial Srinagar Heritage",
                (
                    "Awake to the soothing lapping of water against the houseboat wood. Today, enjoy a beautifully paced "
                    "journey through Srinagar's royal historical core. Explore the manicured terraced expanses of Nishat and "
                    "Shalimar Bagh, constructed by Mughal emperors as symbols of ultimate love and luxury. Walk past cascading "
                    "fountains and ancient stone pavilions while learning the deep history from our local expert storyteller."
                ),
                [
                    "Sightseeing Included: Shalimar Bagh, Nishat Bagh, Pari Mahal (The Palace of Fairies), and the historical Shankaracharya Temple.",
                    "Evening Experience: A private visit to an elite local Pashmina weaving estate to observe master artisans at work.",
                    "Overnight Stay: Premium Luxury Boutique Hotel in Srinagar",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                3,
                "Ascent to the Snow Kingdom of Gulmarg",
                (
                    "After a rich breakfast, take a smooth, scenic drive to Gulmarg, the Meadow of Gold, now fully transformed "
                    "into a dramatic winter kingdom. Watch the scenery shift dramatically into vast, powdery snowfields stretching "
                    "as far as the eye can see. Check into your ultra-luxury heated alpine resort. Spend the afternoon taking a "
                    "gentle sledge ride or simply relaxing by a roaring stone fireplace with panoramic views of the Apharwat peak."
                ),
                [
                    "Sightseeing Included: Scenic pine-forest driving route, high-altitude Gulmarg valley meadows, and the historic St. Mary's Church.",
                    "Evening Experience: Private candle-lit gourmet dining experience looking out over illuminated snow drifts.",
                    "Overnight Stay: Handpicked Luxury Alpine Resort (The Khyber Himalayan Resort & Spa or similar)",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                4,
                "The High-Altitude Gondola Soiree & Snow Comfort",
                (
                    "Prepare for one of the most iconic attractions in Asia. Skip the crowded lines with pre-arranged VIP passes "
                    "from TRAGUIN and board the famous Gulmarg Gondola. Soar gracefully above the snow-capped pine canopies to "
                    "Phase 1 (Kongdoori) and onward to Phase 2 (Apharwat Peak) at an altitude of 14,000 feet. Stand amidst "
                    "pristine Himalayan peaks, enjoying unparalleled panoramic views that create unforgettable memories."
                ),
                [
                    "Sightseeing Included: Phase 1 & Phase 2 Gondola Cable Car Excursion, Apharwat Snow Point exploration.",
                    "Optional Activities: Private guided snow-skiing lesson or a thrilling snowmobile ride across the high-altitude plateau.",
                    "Overnight Stay: Handpicked Luxury Alpine Resort in Gulmarg",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                5,
                "Farewell Kashmir Valleys",
                (
                    "Relish a decadent final breakfast overlooking the frozen alpine valley. Soak in the incredible mountain "
                    "scenery one last time before joining your private chauffeur for a comfortable, well-timed return drive back "
                    "to Srinagar Airport, concluding your ultra-luxury TRAGUIN winter escape with absolute ease."
                ),
                [
                    "Meals Included: Rich Buffet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Sukoon Luxury Houseboat | The Khyber Himalayan Resort & Spa, Gulmarg | Taj Vivanta Dal View, Srinagar",
                "Srinagar / Gulmarg",
                "04 Nights",
                "Ultra Luxury",
                "Handpicked Ultra Luxury Rooms",
                "MAP (Breakfast + Dinner)",
                5,
                1,
                description="OPTION 01 – ULTRA LUXURY (Primary Recommendation): Houseboat: Sukoon Luxury Houseboat | Gulmarg: The Khyber Himalayan Resort & Spa | Srinagar: Taj Vivanta Dal View (4 Nights)",
            ),
            _hotel(
                "Mascot Luxury Houseboat | The Vintage Gulmarg | The Lalit Grand Palace, Srinagar",
                "Srinagar / Gulmarg",
                "04 Nights",
                "Luxury",
                "Handpicked Luxury Rooms",
                "MAP (Breakfast + Dinner)",
                5,
                2,
                description="OPTION 02 – LUXURY: Houseboat: Mascot Luxury Houseboat | Gulmarg: The Vintage Gulmarg | Srinagar: The Lalit Grand Palace (4 Nights)",
            ),
            _hotel(
                "Wangnoo Sheraton Houseboats | Grand Mumtaz, Gulmarg | Fortune Resort Heevan, Srinagar",
                "Srinagar / Gulmarg",
                "04 Nights",
                "Premium",
                "Handpicked Premium Rooms",
                "MAP (Breakfast + Dinner)",
                4,
                3,
                description="OPTION 03 – PREMIUM: Houseboat: Wangnoo Sheraton Houseboats | Gulmarg: Grand Mumtaz | Srinagar: Fortune Resort Heevan (4 Nights)",
            ),
        ],
        inclusions=[
            _inc_included("01 Night stay in an ultra-luxury wooden houseboat and 03 Nights in elite handpicked hotels.", 1),
            _inc_included("Daily artisan breakfasts and multi-cuisine gourmet dinners tailored to your taste.", 2),
            _inc_included("Private airport transfers and complete local sightseeing in a dedicated heated luxury SUV.", 3),
            _inc_included("Pre-booked VIP passes for both Phase 1 and Phase 2 Gulmarg Gondola cable car rides.", 4),
            _inc_included("Complimentary private sunset Shikara boat cruise on Dal Lake with hot Kahwa service.", 5),
            _inc_included("Continuous 24/7 dedicated local VIP concierge support provided by TRAGUIN.", 6),
            _inc_included("All applicable resort fuel surcharges, driver hill allowances, parking fees, and state taxes.", 7),
            _inc_excluded("Domestic or international airfares to and from Srinagar.", 8),
            _inc_excluded("High-altitude special clothing rentals (heavy jackets, snow boots) available locally.", 9),
            _inc_excluded("Personal expenditures such as laundry, phone calls, premium spa visits, and gratitude tips.", 10),
        ],
    )
    return package, itinerary


def build_jk_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "JK-013"
    tour_code = "TRG-JK-013"
    title = "Sonmarg & Gurez Valley Offbeat Trail"
    duration = "07 Nights / 08 Days"
    slug = "jk-013-sonmarg-gurez-valley-offbeat-trail"
    itin_slug = "jk-013-sonmarg-gurez-valley-offbeat-trail-itinerary"
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
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Jammu & Kashmir / India | Category: Leisure & Offbeat Trail", 2),
            _ph("Destinations Covered: Srinagar • Sonmarg • Gurez Valley • Dawar", 3),
            _ph("Ideal for: Families, Couples & Offbeat Explorers", 4),
            _ph("Best season: May to September", 5),
            _ph("Travel Month: Tailored Premium Dates Available", 6),
            _ph("Group / FIT: Private Luxury Customized FIT Exploration", 7),
            _ph("Vehicle: Dedicated Luxury Chauffeur Sedan / SUV (Innova Crysta) throughout the journey", 8),
            _ph("Meal Plan: Modified American Plan (Gourmet Breakfasts & Dinners Included Daily)", 9),
            _ph("Route: Srinagar → Sonmarg Scenic Alpine Zone → Razdan Pass → Gurez Valley (Dawar) → Srinagar Return", 10),
            _ph(
                "TRAGUIN Curated Experience Note: Seamless inner-line border permits, curated high-tea by the "
                "Kishanganga river, handpicked premium properties, and an authentic local cultural interactions package.",
                11,
            ),
        ],
        moods=["Offbeat", "Nature", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Class)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Premium Kashmir Experience — Sonmarg & Gurez Valley Offbeat Trail",
        overview=(
            "Welcome to paradise on earth. TRAGUIN invites you to discover the untouched secrets of Kashmir through "
            "our custom-tailored, ultra-luxury holiday. Traverse past the iconic shikaras of Srinagar into the golden alpine "
            "meadows of Sonmarg, before breaking away into the hidden, dramatic frontiers of Gurez Valley. This Luxury "
            "Kashmir Holiday blends majestic wilderness paths with premium stays, immersive experiences, and impeccable "
            "personal comfort, promising unforgettable memories.\n\n"
            "When considering the perfect Best Kashmir Tour Package or an extraordinary Kashmir Honeymoon Package, "
            "modern travelers look beyond traditional circuits. This signature Kashmir Family Tour brings you face-to-face "
            "with the rarest hidden gems alongside the Top Tourist Places in Kashmir. From the shimmering waters of Dal Lake "
            "to the snow-capped thundering heights of Sonmarg and the untouched wooden villages of Gurez, every vista is spectacular.\n\n"
            "The Best Time to Visit Kashmir for this offbeat trail spans from late spring through autumn, when the high "
            "mountain passes are completely clear. Our TRAGUIN Kashmir Packages are carefully calibrated to ensure a "
            "Premium Kashmir Experience, providing luxury transportation across high altitudes, top-tier hospitality, and "
            "private local access to make your Kashmir Sightseeing truly matchless."
        ),
        seo_title="JK-013 | Sonmarg & Gurez Valley Offbeat Trail | TRAGUIN",
        seo_description=(
            "Premium 07 Nights / 08 Days Kashmir offbeat package (JK-013 / TRG-JK-013): Srinagar, Sonmarg, "
            "Gurez Valley, Dawar, Razdan Pass, Mughal Gardens, and 3-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Dal Lake Shikara, Sonmarg Thajiwas Glacier & Razdan Pass crossing", 1),
            _ih("Gurez Valley Dawar exploration, Habba Khatoon peak & Kishanganga riverside high-tea", 2),
            _ih("Wular Lake transit, Mughal Gardens & Royal Wazwan farewell dinner", 3),
            _ih("Exclusive TRAGUIN riverside sundowner high-tea experience setup in Gurez", 4),
        ],
        days=[
            _day(
                1,
                "Arrival in Imperial Srinagar & Private Shikara Experience",
                (
                    "Your extraordinary trip begins with a private luxury pickup at Srinagar Airport. Your dedicated premium "
                    "chauffeur transfers you to your handpicked premium stay. In the afternoon, experience an emotional "
                    "storytelling hour during a private, extended Shikara ride across Dal Lake. Glide smoothly past floating "
                    "gardens and vibrant local wooden markets while watching the sunset paint the sky in deep shades of gold."
                ),
                [
                    "Sightseeing Included: Dal Lake classic circuit, Char Chinar photography points, and floating markets.",
                    "Evening Experience: A warm traditional welcome drink of Kashmiri Kahwa with roasted almonds served at your property.",
                    "Overnight Stay: Handpicked Luxury Houseboat / Premium Hotel in Srinagar",
                    "Meals Included: Welcome Amenities & Gourmet Dinner",
                ],
            ),
            _day(
                2,
                "Srinagar to Sonmarg — Meadow of Gold Trail",
                (
                    "After a delightful morning artisan breakfast, drive along the sparkling Sindh River towards Sonmarg, the "
                    "famed 'Meadow of Gold'. Marvel at the shifting breathtaking landscapes as the valley narrows into sheer pine "
                    "forests and massive jagged rock cliffs. Check into your premium resort tucked quietly away along the river "
                    "paths, and spend your afternoon relaxing amidst pure alpine air."
                ),
                [
                    "Sightseeing Included: En-route Sindh valley scenic photography overlooks and Gagangir eco-park rest stop.",
                    "Evening Experience: A refreshing custom walk along the property's alpine paths at the base of the mountains.",
                    "Overnight Stay: Premium Luxury Resort in Sonmarg",
                    "Meals Included: Rich Breakfast & Fine Dining Dinner",
                ],
            ),
            _day(
                3,
                "Sonmarg — Exploring the Thajiwas Glacier and Frozen Visions",
                (
                    "Immerse yourself entirely in the high mountain thrill of Sonmarg. Today, head towards the spectacular "
                    "Thajiwas Glacier on local ponies or request your vehicle to traverse the dramatic twists of the Zojila Pass "
                    "towards Zero Point. Marvel at the sheer walls of ice and vast frozen fields that remain magnificent deep into "
                    "the summer months."
                ),
                [
                    "Sightseeing Included: Thajiwas Glacier viewpoint or Zero Point high-altitude pass overlook.",
                    "Optional Activities: Sledge riding on the high snowfields or a guided trout-fishing walk near the river.",
                    "Overnight Stay: Premium Luxury Resort in Sonmarg",
                    "Meals Included: Artisan Breakfast & Multi-Cuisine Buffet Dinner",
                ],
            ),
            _day(
                4,
                "Sonmarg to Gurez Valley — Crossing the High Razdan Pass",
                (
                    "Depart early for your crown jewel destination: Gurez Valley. This legendary, heavily searched offbeat trail "
                    "crosses the high Razdan Pass (11,672 feet), revealing breathtaking panoramic views of the distant snow-covered "
                    "peaks of Harmukh. Descend gently into an otherworldly landscape of terraced wooden villages, pristine pine "
                    "wilderness, and ancient Dardic culture. Arrive at Dawar, the central beating heart of Gurez."
                ),
                [
                    "Sightseeing Included: Razdan Pass mountain top crossing, Koragbal valley viewpoints, and initial Kishanganga river views.",
                    "Overnight Stay: Handpicked Best Available Premium Boutique Property / Luxury Tents in Dawar",
                    "Meals Included: Hearty Breakfast & Hot Curated Dinner",
                ],
            ),
            _day(
                5,
                "Gurez Valley — Dawar & the Pyramid of Habba Khatoon",
                (
                    "Spend a soulful day exploring the historic secrets of Dawar. Learn the poignant love stories and local poetry "
                    "surrounding the legendary Habba Khatoon peak, a massive pyramid-shaped mountain that completely dominates the "
                    "valley skyline. Wander through traditional log-hut villages, interacting warmly with the beautiful, soft-spoken "
                    "Dard-Shin people whose culture has remained beautifully preserved for centuries."
                ),
                [
                    "Sightseeing Included: Habba Khatoon spring, Dawar local wooden market, and ancient heritage log villages.",
                    "Evening Experience: A signature TRAGUIN riverside sundowner high-tea set up directly by the roaring Kishanganga river.",
                    "Overnight Stay: Premium Boutique Property / Luxury Tents in Dawar",
                    "Meals Included: Local Infused Breakfast & Special Traditional Dinner",
                ],
            ),
            _day(
                6,
                "Gurez Valley to Srinagar — The Freshwater Lakes Transit",
                (
                    "Bid farewell to the serene valleys of Gurez and begin your highly scenic return drive back over the Razdan Pass "
                    "to Srinagar. Re-entering the main valley opens up expansive, beautiful views of Wular Lake, one of Asia's largest "
                    "freshwater basins. Check into your luxury city hotel and enjoy a peaceful, relaxing evening at your absolute leisure."
                ),
                [
                    "Sightseeing Included: Wular Lake shoreline panoramic route and local apple orchard rest stops.",
                    "Overnight Stay: Handpicked Premium Luxury Hotel in Srinagar",
                    "Meals Included: Full Breakfast & International Buffet Dinner",
                ],
            ),
            _day(
                7,
                "Srinagar — Mughal Imperial Gardens & Historic Empire Trail",
                (
                    "Dedicate your final full day to the grand imperial monuments of Srinagar. Walk through the beautifully manicured "
                    "terraces of the Mughal Gardens—Shalimar Bagh and Nishat Bagh—built by ancient emperors against backgrounds of "
                    "steep craggy mountains. In the afternoon, step inside old heritage craft workshops to see master artisans creating "
                    "legendary works of art."
                ),
                [
                    "Sightseeing Included: Nishat Bagh, Shalimar Bagh, Pari Mahal historic ruins, and Shankaracharya Temple hilltop overlook.",
                    "Evening Experience: A special, private multi-course traditional Kashmiri Wazwan farewell dinner experience arranged by TRAGUIN.",
                    "Overnight Stay: Handpicked Premium Luxury Hotel in Srinagar",
                    "Meals Included: Artisan Breakfast & Royal Wazwan Farewell Dinner",
                ],
            ),
            _day(
                8,
                "Srinagar Homeward — Catching Valleys in Retrospect",
                (
                    "Savor your final breakfast looking out over the misty mountain lines of Srinagar. Take a last walk through the "
                    "local lanes or simply relax in the manicured resort gardens. Your private chauffeur will drive you comfortably back "
                    "to Srinagar Airport for your outbound flight, concluding your ultra-premium holiday with unforgettable memories."
                ),
                [
                    "Meals Included: Rich Buffet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "The Grand Mamta / Radisson Collection Srinagar | Radisson Hotel Sonmarg | TRAGUIN Selected Premium Boutique Retreat Gurez",
                "Srinagar / Sonmarg / Gurez",
                "07 Nights",
                "Ultra Luxury",
                "Handpicked Ultra Luxury Rooms",
                "MAP (Breakfast + Dinner)",
                5,
                1,
                description="OPTION 01 – ULTRA LUXURY: The Grand Mamta / Radisson Collection Srinagar (3N) • Radisson Hotel Sonmarg (2N) • TRAGUIN Selected Premium Boutique Retreat Gurez (2N)",
            ),
            _hotel(
                "Fortune Resort Heevan Srinagar | Hotel Rah Villas Sonmarg | Kahrwaa Resort Gurez",
                "Srinagar / Sonmarg / Gurez",
                "07 Nights",
                "Luxury",
                "Handpicked Luxury Rooms",
                "MAP (Breakfast + Dinner)",
                5,
                2,
                description="OPTION 02 – LUXURY: Hotel Rah Villas Sonmarg (2N) • Kahrwaa Resort Gurez (2N) • Fortune Resort Heevan Srinagar (3N)",
            ),
            _hotel(
                "Hotel Lemon Tree Srinagar | Village Walk Sonmarg | Gurez Wood Cottage",
                "Srinagar / Sonmarg / Gurez",
                "07 Nights",
                "Premium",
                "Handpicked Premium Rooms",
                "MAP (Breakfast + Dinner)",
                4,
                3,
                description="OPTION 03 – PREMIUM: Village Walk Sonmarg (2N) • Gurez Wood Cottage (2N) • Hotel Lemon Tree Srinagar (3N)",
            ),
        ],
        inclusions=[
            _inc_included(
                "07 Nights premium luxury accommodation across selected high-end hotels, houseboats, and offbeat boutique resorts.",
                1,
            ),
            _inc_included("Modified American Plan: Handcrafted daily breakfasts and multi-course gourmet dinners.", 2),
            _inc_included("Entire private tour circuit transfers in a dedicated luxury air-conditioned Innova Crysta vehicle.", 3),
            _inc_included(
                "All inner-line border permits, military checkpoints documentation clearance, and pass permissions for Gurez Valley.",
                4,
            ),
            _inc_included("01 Complimentary extended private Shikara ride on Dal Lake with special inclusions.", 5),
            _inc_included("Dedicated professional English/Hindi speaking driver-cum-guide.", 6),
            _inc_included("Exclusive TRAGUIN riverside sundowner high-tea experience setup in Gurez.", 7),
            _inc_included("All current resort luxury taxes, fuel surcharges, state tolls, and driver allowances.", 8),
            _inc_excluded("Flight airfares or train transport to and from Srinagar.", 9),
            _inc_excluded("Local pony ride charges in Sonmarg / Thajiwas or optional local internal Union cabs for Zero Point.", 10),
            _inc_excluded(
                "Personal costs such as laundry, top-shelf beverages, professional camera fees, and premium spa treatments.",
                11,
            ),
        ],
    )
    return package, itinerary


def build_jk_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "JK-014"
    tour_code = "TRG-JK-014"
    title = "Beautiful Pahalgam Valley Stay"
    duration = "03 Nights / 04 Days"
    slug = "jk-014-beautiful-pahalgam-valley-stay"
    itin_slug = "jk-014-beautiful-pahalgam-valley-stay-itinerary"
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
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Jammu & Kashmir / India | Category: Leisure Escape", 2),
            _ph("Destinations Covered: Srinagar • Pahalgam (Lidder Valley) • Betaab Valley", 3),
            _ph("Ideal for: Couples, Families & Luxury Leisure Seekers", 4),
            _ph("Best season: April to September (Plus Magical Winter Snows)", 5),
            _ph("Travel Month: Customized Premium Dates Available", 6),
            _ph("Group / FIT: Private Luxury Customized FIT Getaway", 7),
            _ph("Vehicle: Private Dedicated Premium Sedan / SUV (Innova Crysta) throughout", 8),
            _ph("Meal Plan: Modified American Plan (Artisan Breakfasts & Gourmet Dinners Included)", 9),
            _ph(
                "Route: Srinagar Airport → Pampore Saffron Fields → Pahalgam Valley Stay → Srinagar Return",
                10,
            ),
            _ph(
                "TRAGUIN Curated Experience Note: Premium river-facing valley cottages, a private riverside "
                "champagne-style picnic tea, a dedicated local valley expert chauffeur, and fast-track union cab coordination.",
                11,
            ),
            _ph(
                "Shopping & Local Experiences: Pure Kashmiri saffron strands, hand-knotted silk carpets, "
                "walnut wood carving items, and sweet local Kashmiri apples.",
                12,
            ),
            _ph(
                "Important Notes: Pahalgam local sightseeing requires specialized local union cabs which are fully "
                "pre-arranged and paid within your inclusions package. Advance booking suggestions are highly "
                "recommended to ensure premium river-facing room inventory during peak months.",
                13,
            ),
        ],
        moods=["Leisure", "Honeymoon", "Family"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Class)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Premium Kashmir Experience — Beautiful Pahalgam Valley Stay",
        overview=(
            "Surrender to the breathtaking landscapes of the crown jewel of India. TRAGUIN invites you on an exclusive, "
            "immersive luxury journey focused on a deep, relaxing stay inside the majestic Pahalgam Valley. Nestled "
            "against the roaring Lidder River and dense pine slopes, our handpicked hotels and exclusive experiences "
            "ensure a flawless blend of scenic beauty and true royal comfort, creating unforgettable memories to cherish "
            "forever.\n\n"
            "When charting the ultimate escape to the mountains, picking the Best Kashmir Tour Package or a tailored "
            "Kashmir Honeymoon Package leads refined travelers to seek a deeper, immersive experience over rushed travel "
            "tracks. This specialized Kashmir Family Tour emphasizes an extended stay in Pahalgam, the valley of shepherds, "
            "which stands tall among the Top Tourist Places in Kashmir.\n\n"
            "The Best Time to Visit Kashmir runs from April to September for lush alpine meadows, and December to February "
            "for a spectacular winter snowscape. Our tailored TRAGUIN Kashmir Packages unlock a magnificent Premium "
            "Kashmir Experience, providing luxury transportation, elite valley resorts, and incredible Kashmir Sightseeing "
            "tracks to manifest an unforgettable Luxury Kashmir Holiday."
        ),
        seo_title="JK-014 | Beautiful Pahalgam Valley Stay | TRAGUIN",
        seo_description=(
            "Premium 03 Nights / 04 Days Kashmir package (JK-014 / TRG-JK-014): Pahalgam valley stay, "
            "Betaab Valley, Aru, Chandanwari, Baisaran, Dal Lake Shikara, and 3-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Extended Pahalgam valley stay with Betaab, Aru & Chandanwari circuit", 1),
            _ih("Baisaran Mini-Switzerland pony trail and riverside barbeque dining", 2),
            _ih("Dal Lake Shikara cruise and traditional Kashmiri Wazwan farewell dinner", 3),
            _ih("TRAGUIN Signature Experience: Private riverside fireside high-tea along the Lidder River", 4),
            _ih("Curated by TRAGUIN Experts: Seamless local transport connections avoiding common transit bottlenecks", 5),
            _ih("Personalized Assistance: Dedicated 24/7 remote support concierge tracking your mountain routes continually", 6),
            _ih(
                "Instagram Spots: The roaring Lidder river streams, the towering mountain pines of Betaab Valley, "
                "and a traditional shikara pose at Dal Lake",
                7,
            ),
        ],
        days=[
            _day(
                1,
                "Arrival in Srinagar & Scenic Ride to Pahalgam Valley",
                (
                    "Your premium holiday starts at Srinagar Airport where your courteous private chauffeur receives you "
                    "with true warmth. Drive outward along the national highway, crossing through the fragrant Pampore "
                    "saffron fields and ancient walnut groves. As you climb higher, the breathtaking landscapes of the "
                    "majestic Lidder Valley unfold around you. Arrive at your ultra-luxury riverside resort in Pahalgam, "
                    "checking into your private pine cottage effortlessly."
                ),
                [
                    "Sightseeing Included: En-route photography stops at the saffron plains and the ancient Avantipur temple ruins.",
                    "Evening Experience: A private, warm welcome fireside high-tea session overlooking the rushing crystal waters of the Lidder River.",
                    "Overnight Stay: Handpicked Luxury Resort in Pahalgam",
                    "Meals Included: Welcome Drink & Gourmet Buffet Dinner",
                ],
            ),
            _day(
                2,
                "Pahalgam Valley Immersion — Betaab, Aru & Chandanwari",
                (
                    "Wake up to the pristine song of the mountain streams and a cool alpine breeze. Today, embark on a "
                    "full-day discovery of Pahalgam's most iconic attractions using a pre-arranged, private premium local "
                    "vehicle. Stroll across the cinematic meadows of Betaab Valley, gaze at the high mountain peaks framing "
                    "Aru Valley, and touch the pristine snowfields of Chandanwari."
                ),
                [
                    "Sightseeing Included: Complete circuit of Betaab Valley, Aru Eco-Sanctuary, and Chandanwari glacier base.",
                    "Evening Experience: A curated open-air riverside barbeque dining evening arranged privately by the resort culinary team.",
                    "Overnight Stay: Handpicked Luxury Resort in Pahalgam",
                    "Meals Included: Artisan Breakfast & Themed Barbecue Dinner",
                ],
            ),
            _day(
                3,
                "Pahalgam Mini-Switzerland Cozy Trail & Return to Srinagar",
                (
                    "After a rich breakfast, enjoy an immersive experience tracking the old pine forests on horseback towards "
                    "Baisaran Valley, affectionately known as 'Mini-Switzerland'. Breathe in the pure, crisp mountain air "
                    "amidst endless rolling green meadows. In the afternoon, return to your luxury vehicle for a smooth, "
                    "scenic drive back down to Srinagar, checking into a premium city hotel."
                ),
                [
                    "Sightseeing Included: Baisaran Valley Pony Trail, local Pahalgam pine woods, and a gentle evening Shikara cruise on Dal Lake.",
                    "Evening Experience: A traditional multi-course Kashmiri Wazwan farewell dinner arranged exclusively by TRAGUIN.",
                    "Overnight Stay: Handpicked Premium Luxury Hotel in Srinagar",
                    "Meals Included: Full Breakfast & Royal Wazwan Farewell Dinner",
                ],
            ),
            _day(
                4,
                "Departure from Srinagar with Timeless Memories",
                (
                    "Relish a final morning breakfast looking out over the magnificent mountain peaks. If flight timings permit, "
                    "take a swift, elegant walk through the symmetric fountains of Nishat Mughal Garden. Your private chauffeur "
                    "will then ensure a seamless, fully managed transfer to Srinagar Airport for your journey home, concluding "
                    "an extraordinary travel escape."
                ),
                [
                    "Meals Included: Full Buffet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Welcomhotel by ITC Pine n Peak, Pahalgam | The Grand Mamta Srinagar",
                "Pahalgam / Srinagar",
                "03 Nights",
                "Ultra Luxury",
                "Executive River-View Suite",
                "MAP (Breakfast + Dinner)",
                5,
                1,
                description=(
                    "OPTION 01 – ULTRA LUXURY: The Khyber Himalayan Resort (Extension) / Welcomhotel by ITC Pine n Peak, "
                    "Pahalgam | Executive River-View Suite (2 Nights) • The Grand Mamta Srinagar (1 Night)"
                ),
            ),
            _hotel(
                "Grand Mumtaz Resorts Pahalgam | Fortune Resort Heevan Srinagar",
                "Pahalgam / Srinagar",
                "03 Nights",
                "Luxury",
                "Deluxe Pine Cabin",
                "MAP (Breakfast + Dinner)",
                5,
                2,
                description=(
                    "OPTION 02 – LUXURY: Grand Mumtaz Resorts Pahalgam | Deluxe Pine Cabin (2 Nights) • "
                    "Fortune Resort Heevan Srinagar (1 Night)"
                ),
            ),
            _hotel(
                "Hotel Heevan Pahalgam | Hotel Lemon Tree Srinagar",
                "Pahalgam / Srinagar",
                "03 Nights",
                "Premium",
                "Superior Valley Room",
                "MAP (Breakfast + Dinner)",
                4,
                3,
                description=(
                    "OPTION 03 – PREMIUM: Hotel Heevan Pahalgam | Superior Valley Room (2 Nights) • "
                    "Hotel Lemon Tree Srinagar (1 Night)"
                ),
            ),
        ],
        inclusions=[
            _inc_included("02 Nights luxury stay in Pahalgam and 01 Night in Srinagar at premium handpicked hotels.", 1),
            _inc_included("Daily artisan breakfasts and multi-course gourmet dinners.", 2),
            _inc_included("Private airport transfers and inter-city routes in a dedicated luxury AC vehicle.", 3),
            _inc_included(
                "Pre-booked private local union transportation for the absolute finest Aru & Betaab valley sightseeing.",
                4,
            ),
            _inc_included("Complimentary traditional extended Shikara cruise on Dal Lake.", 5),
            _inc_included("24/7 dedicated TRAGUIN on-ground guest assistance support.", 6),
            _inc_included("All regional road tolls, luxury resort taxes, state entry taxes, and chauffeur allowances.", 7),
            _inc_excluded("Flight or railway train tickets to and from Srinagar.", 8),
            _inc_excluded("Local horse/pony riding fees at Baisaran Valley pathways.", 9),
            _inc_excluded("Expenses of a personal nature (laundry, room service, telephone calls).", 10),
        ],
    )
    return package, itinerary


def build_jk_015(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "JK-015"
    tour_code = "TRG-JK-015"
    title = "Sacred Amarnath Yatra via Baltal"
    duration = "04 Nights / 05 Days"
    slug = "jk-015-sacred-amarnath-yatra-via-baltal"
    itin_slug = "jk-015-sacred-amarnath-yatra-via-baltal-itinerary"
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
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Jammu & Kashmir / India | Category: Pilgrimage / Luxury Yatra", 2),
            _ph("Destinations Covered: Srinagar • Sonmarg • Baltal • Amarnath Holy Cave", 3),
            _ph("Ideal for: Devotees, Families & Spiritual Explorers", 4),
            _ph("Best season: July to August (Yatra Shravan Month)", 5),
            _ph("Travel Month: July – August (Official Shrine Board Dates)", 6),
            _ph("Group / FIT: Private Luxury FIT Pilgrimage Customized Escape", 7),
            _ph("Vehicle: Dedicated AC Luxury MUV (Innova Crysta) throughout the entire valley track", 8),
            _ph("Meal Plan: Modified American Plan (Nutritious Breakfasts & Dinners Included Daily)", 9),
            _ph(
                "Route: Srinagar Arrival → Sonmarg Alpine Valley → Baltal Base → Amarnath Holy Cave Darshan → Srinagar Return",
                10,
            ),
            _ph(
                "TRAGUIN Curated Experience Note: Complete administrative permit facilitation support, priority "
                "helicopter ticket coordination (subject to shrine guidelines), pre-arranged premium base camp or hotel "
                "stays, and continuous 24/7 dedicated local field assistance.",
                11,
            ),
            _ph(
                "Shopping & Local Experiences: Pure Pampore saffron filaments, authentic walnut-wood prayer beads, "
                "and pure local organic honey.",
                12,
            ),
            _ph(
                "Important Notes: All Amarnath Yatris must secure a Compulsory Health Certificate (CHC) from authorized "
                "state doctors prior to registration. Please pack adequate thermal clothing, raincoats, waterproof trekking "
                "boots, and essential personal medicines. Helicopter travel parameters remain highly dependent on local "
                "weather conditions for absolute security.",
                13,
            ),
        ],
        moods=["Pilgrimage", "Spiritual", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Class)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Premium Kashmir Experience — Sacred Amarnath Yatra via Baltal",
        overview=(
            "Embark on the ultimate spiritual pilgrimage to the abode of Lord Shiva. TRAGUIN presents a highly secure, "
            "seamless, and meticulously structured premium Amarnath Yatra itinerary via the Baltal route. Witness "
            "breathtaking landscapes, soaring Himalayan peaks, and serene high-altitude tracks under the utmost care. "
            "This Luxury Kashmir Holiday combines your divine aspiration with premium stays, handpicked hotels, and "
            "exclusive experiences, leaving you with unforgettable memories.\n\n"
            "Planning the highly revered Amarnath Yatra via Baltal requires precision planning, seamless logistics, and "
            "comfortable stays. When selecting the Best Kashmir Tour Package with a spiritual core, or aligning it as a "
            "Kashmir Family Tour, devotees look for short pathways and minimal physical strain. The Baltal trail offers "
            "the fastest route to the holy ice lingam, framed by stunningly steep valleys and cascading glacial rivers.\n\n"
            "The Best Time to Visit Kashmir for this pilgrimage is strictly during the summer months of July and August. "
            "Our comprehensive TRAGUIN Kashmir Packages ensure a highly stable and Premium Kashmir Experience despite "
            "the rugged mountain conditions. From organizing transfers to your premium accommodation to facilitating your "
            "Kashmir Sightseeing after the darshan, we manage every moving part with complete professional care."
        ),
        seo_title="JK-015 | Sacred Amarnath Yatra via Baltal | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Amarnath Yatra package (JK-015 / TRG-JK-015): Sonmarg, Baltal, "
            "Amarnath Holy Cave darshan, Dal Lake Shikara, Mughal Gardens, and 3-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Amarnath Holy Cave darshan via Baltal helicopter and Panjtarni track", 1),
            _ih("Sonmarg alpine acclimatization and Dal Lake Shikara romance", 2),
            _ih("Srinagar Mughal Heritage trail — Nishat, Shalimar & Shankaracharya Temple", 3),
            _ih("TRAGUIN Signature Experience: Private dedicated high-altitude helper support available on request", 4),
            _ih("Curated by Experts: Carefully managed mountain travel pacing ensuring excellent acclimatization intervals", 5),
            _ih("Personalized Assistance: Fast-track physical luggage handling assistance across transit base stations", 6),
            _ih(
                "Instagram Spots: Sunset reflections over Dal Lake, the raw glacial valley cuts of Baltal, "
                "and the towering mountain walls of Panjtarni",
                7,
            ),
        ],
        days=[
            _day(
                1,
                "Arrival in Srinagar & Transit to Sonmarg",
                (
                    "Your sacred spiritual passage commences as you touch down at Srinagar Airport. A personal TRAGUIN "
                    "executive welcomes you warmly and introduces you to your premium chauffeur. Board your luxury vehicle "
                    "and begin a smooth, highly scenic drive towards Sonmarg, the 'Meadow of Gold'. Trace the winding paths "
                    "of the sparkling Sindh River, watching the dramatic valley transform into alpine conifer forests. Check "
                    "into your premium hotel seamlessly and spend the evening resting to prepare for the sacred journey ahead."
                ),
                [
                    "Sightseeing Included: En-route photography halts over the expansive Sindh valley views.",
                    "Evening Experience: A vital acclimatization briefing session with high-tea presented by our operational lead tracker.",
                    "Overnight Stay: Handpicked Premium Luxury Resort in Sonmarg",
                    "Meals Included: Welcome High-Tea & Custom Nourishing Dinner",
                ],
            ),
            _day(
                2,
                "Sonmarg to Baltal Base — Sacred Ascent to Holy Cave",
                (
                    "Wake up before dawn to a crisp mountain breeze. Proceed to the Baltal Helipad base camp. Board your "
                    "pre-arranged private chartered helicopter ride flying past breathtaking landscapes and sharp glaciated "
                    "valleys directly towards Panjtarni. Upon landing at Panjtarni, embark on a scenic track towards the "
                    "Amarnath Holy Cave via foot, pony, or palki. Stand in deep spiritual awe inside the massive cave shrine "
                    "before the natural Ice Lingam of Lord Shiva. Soak in the powerful spiritual energy and return safely to "
                    "Panjtarni or Baltal base camp."
                ),
                [
                    "Sightseeing Included: Holy Amarnath Cave Shrine Darshan, high-altitude glacier views, and the sacred Sangam confluence.",
                    "Evening Experience: A cozy relaxation session at the resort following your successful sacred darshan.",
                    "Overnight Stay: Sonmarg Premium Resort (or premium executive alpine Swiss tents at Baltal Base)",
                    "Meals Included: Energetic Breakfast & Piping Hot Restorative Dinner",
                ],
            ),
            _day(
                3,
                "Re-entering Srinagar & Shikara Romance",
                (
                    "Enjoy a relaxed morning breakfast overlooking the mist-laden peaks of Sonmarg. Board your luxury vehicle "
                    "for a smooth drive returning to Srinagar. Check into your premium property or an authentic boutique luxury "
                    "houseboat. In the afternoon, unwind completely during an emotional storytelling experience aboard a private "
                    "Shikara ride across the calm, shimmering waters of Dal Lake, passing old wooden architectures and vibrant "
                    "floating markets."
                ),
                [
                    "Sightseeing Included: Extended Dal Lake cruising, floating lotus fields, and Char Chinar island photography spots.",
                    "Evening Experience: A traditional warm Kashmiri Kahwa tea serving with crisp local treats at sunset.",
                    "Overnight Stay: Premium Luxury Houseboat / Handpicked Luxury Hotel in Srinagar",
                    "Meals Included: Full Breakfast & Multi-Cuisine Gourmet Dinner",
                ],
            ),
            _day(
                4,
                "Srinagar — Imperial Mughal Heritage Trail",
                (
                    "Dedicate a glorious day to uncovering the finest historical landmarks of Srinagar. Explore the terraced "
                    "royal lawns of the Mughal Gardens, built by ancient emperors against backgrounds of steep craggy mountains. "
                    "Stroll along the water channels of Shalimar Bagh and Nishat Bagh, and ascend to higher viewpoints to look "
                    "over the expansive valley plains."
                ),
                [
                    "Sightseeing Included: Nishat Bagh (Garden of Pleasure), Shalimar Bagh (Abode of Love), and the historical Shankaracharya Temple hilltop shrine.",
                    "Evening Experience: A special curated premium farewell dinner celebrating authentic local Kashmiri delicacies.",
                    "Overnight Stay: Handpicked Luxury Hotel in Srinagar",
                    "Meals Included: Artisan Breakfast & Farewell Festive Dinner",
                ],
            ),
            _day(
                5,
                "Farewell Paradise — Departure Journey",
                (
                    "Savor your final morning breakfast looking out over the majestic mountain lines of Kashmir. Take a slow walk "
                    "through the local emporiums to pick up fine souvenirs before your private premium vehicle transfers you "
                    "seamlessly back to Srinagar Airport for your outbound flight, concluding your divine pilgrimage trip with "
                    "absolute convenience."
                ),
                [
                    "Meals Included: Rich Buffet Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Radisson Hotel Sonmarg | Radisson Collection Srinagar / The Grand Mamta",
                "Sonmarg / Srinagar",
                "04 Nights",
                "Ultra Luxury",
                "Handpicked Ultra Luxury Rooms",
                "MAP (Breakfast + Dinner)",
                5,
                1,
                description="OPTION 01 – ULTRA LUXURY: Radisson Hotel Sonmarg (2N) • Radisson Collection Srinagar / The Grand Mamta (2N)",
            ),
            _hotel(
                "Hotel Rah Villas Sonmarg | Fortune Resort Heevan Srinagar",
                "Sonmarg / Srinagar",
                "04 Nights",
                "Luxury",
                "Handpicked Luxury Rooms",
                "MAP (Breakfast + Dinner)",
                5,
                2,
                description="OPTION 02 – LUXURY: Hotel Rah Villas Sonmarg (2N) • Fortune Resort Heevan Srinagar (2N)",
            ),
            _hotel(
                "Village Walk Sonmarg | Hotel Lemon Tree Srinagar",
                "Sonmarg / Srinagar",
                "04 Nights",
                "Premium",
                "Handpicked Premium Rooms",
                "MAP (Breakfast + Dinner)",
                4,
                3,
                description="OPTION 03 – PREMIUM: Village Walk Sonmarg (2N) • Hotel Lemon Tree Srinagar (2N)",
            ),
        ],
        inclusions=[
            _inc_included("04 Nights premium accommodation in handpicked top-tier hotels and luxury houseboats.", 1),
            _inc_included("Modified American Plan: Daily high-nutrition breakfasts and custom dinners included.", 2),
            _inc_included("Complete private valley transfers and sightseeing loops in a dedicated luxury AC Innova Crysta.", 3),
            _inc_included("Administrative permit processing assistance and mandatory shrine board registration clearances.", 4),
            _inc_included("01 Complimentary extended private Shikara cruise setup on Dal Lake.", 5),
            _inc_included("Dedicated professional English/Hindi speaking driver-cum-guide for the entire route.", 6),
            _inc_included("24/7 Continuous TRAGUIN on-ground back-end remote support and safety monitoring.", 7),
            _inc_excluded("Main flight sector or railway ticketing costs to Srinagar.", 8),
            _inc_excluded("Actual helicopter ticketing fares (coordinated transparently based on Shrine Board direct windows).", 9),
            _inc_excluded("Local mountain pony, palki, or porter charges on the mountain tracks.", 10),
            _inc_excluded("Compulsory medical health certificate processing fees.", 11),
        ],
    )
    return package, itinerary


def build_jk_016(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "JK-016"
    tour_code = "TR-JK-016-DIVINE"
    title = "Vaishno Devi Divine Darshan"
    duration = "03 Nights / 04 Days"
    slug = "jk-016-vaishno-devi-divine-darshan"
    itin_slug = "jk-016-vaishno-devi-divine-darshan-itinerary"
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
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Kashmir, India | Category: Pilgrimage / Divine Darshan", 2),
            _ph("Destinations Covered: Katra • Vaishno Devi Bhawan • Jammu", 3),
            _ph("Ideal for: Families & Divine Seekers", 4),
            _ph("Best season: Round the Year", 5),
            _ph("Travel Format: Private Luxury Pilgrimage FIT Tour", 6),
            _ph("Vehicle: Premium AC Luxury Vehicle with dedicated chauffeur", 7),
            _ph("Meal Plan: Pure Vegetarian Breakfast & Dinner Daily", 8),
            _ph("Route: Jammu Arrival → Katra Base Camp → Vaishno Devi Bhawan Darshan → Jammu Sightseeing → Departure", 9),
            _ph(
                "TRAGUIN Curated Experience Note: VIP coordination assistance, Yatra Parchi registration, "
                "handpicked hotels close to Banganga checkpoint, and 24/7 dedicated support helpline.",
                10,
            ),
            _ph(
                "Shopping & Local Experiences: Katra — authentic premium organic walnuts, almonds, and high-grade "
                "Kashmiri saffron. Jammu — exquisite traditional papier-mâché crafts and delicate woolens from local artisans.",
                11,
            ),
        ],
        moods=["Pilgrimage", "Spiritual", "Family"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Class)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="TRAGUIN Vaishno Devi Divine Darshan — Premium Pilgrimage Experience",
        overview=(
            "Embark on a sacred, spiritual journey curated exclusively by TRAGUIN to the holy shrine of Mata Vaishno Devi. "
            "Nestled in the beautiful Trikuta Mountains of Jammu and Kashmir, this Best Kashmir Tour Package is designed to "
            "offer a flawless, comfortable, and deeply emotional pilgrimage experience. Combining premium stays, VIP "
            "coordination assistance, and luxury transport, TRAGUIN ensures your divine darshan leaves you with nothing but "
            "unforgettable memories and peaceful blessings.\n\n"
            "This highly sought-after Kashmir Pilgrimage Tour prioritizes safety, luxury, and spiritual comfort. Avoid the stress "
            "of regular queues with TRAGUIN premium assistance. Transfers are executed via state-of-the-art private vehicles, "
            "and our accommodation options in Katra are handpicked close to the Banganga checkpoint to ensure maximum "
            "convenience for your holy Yatra.\n\n"
            "The pilgrimage to Vaishno Devi is one of the most searched spiritual experiences in the world. Famous attractions "
            "like the sacred Bhairon Nath Temple and the beautiful Ardhkuwari cave are primary destinations for millions of "
            "families. With a Luxury Kashmir Holiday layout, TRAGUIN elevates your journey by offering options for luxury "
            "helicopter ticketing, battery-car passes for senior travelers, and premium handpicked hotels where you can relax "
            "after the long walk, making it the perfect spiritual getaway."
        ),
        seo_title="JK-016 | Vaishno Devi Divine Darshan | TRAGUIN",
        seo_description=(
            "Premium 03 Nights / 04 Days Vaishno Devi pilgrimage package (JK-016 / TR-JK-016-DIVINE): "
            "Katra, Vaishno Devi Bhawan, Bhairon Nath Temple, Jammu sightseeing, and 2-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Holy Mata Vaishno Devi Bhawan darshan with Ardhkuwari and Bhairon Nath Temple", 1),
            _ih("Jammu local sightseeing — Raghunath Temple, Bahu Fort & Bagh-e-Bahu Gardens", 2),
            _ih("TRAGUIN Signature Experience: Priority gate passes and swift checkpoint guidance", 3),
            _ih(
                "Curated by TRAGUIN Experts: Handpicked pure-vegetarian luxury dining options completely free from "
                "onion and garlic if required",
                4,
            ),
            _ih("Personalized Assistance: Dedicated greeting staff right at the vehicle boarding points", 5),
        ],
        days=[
            _day(
                1,
                "Arrival Jammu to Katra Base Camp",
                (
                    "Your divine journey begins with a warm welcome by a specialized TRAGUIN travel consultant at Jammu Airport "
                    "or Jammu Tawi Railway Station. Step into a waiting luxury vehicle for a highly scenic, smooth drive towards "
                    "Katra, the beautiful base camp of Mata Vaishno Devi. Check into your premium handpicked hotel, unwind, and "
                    "prepare your mind and body for the grand spiritual journey ahead. The evening is yours to enjoy a relaxing "
                    "walk around the vibrant Katra local market."
                ),
                [
                    "Sightseeing Included: Scenic transit from Jammu to Katra foothills",
                    "Evening Experience: Pre-Yatra orientation and refreshing local dinner",
                    "Overnight Stay: Premium Luxury Hotel in Katra",
                    "Meals Included: Gourmet Vegetarian Dinner",
                ],
            ),
            _day(
                2,
                "Holy Yatra — Divine Mata Vaishno Devi Darshan",
                (
                    "A magnificent and emotional day! Early morning, TRAGUIN coordinates your comfortable transfer to Banganga or "
                    "the Katra Helipad. Proceed towards the Holy Bhawan nestled beautifully in the Trikuta Hills. Whether you choose "
                    "to walk, take a pony, use the battery car, or fly via a premium helicopter experience, you will reach the sacred "
                    "cave shrine. Experience the blissful darshan of the natural rock formations (Pindis) representing Maha Kali, Maha "
                    "Lakshmi, and Maha Saraswati. Later, visit the essential Bhairon Nath Temple via the premium ropeway before "
                    "returning back down to Katra."
                ),
                [
                    "Sightseeing Included: Holy Cave Bhawan, Ardhkuwari, Bhairon Nath Shrine",
                    "Optional Activities: VIP Darshan Assistance / Helicopter Charter",
                    "Evening Experience: Relaxing premium foot reflexology massage back at hotel",
                    "Overnight Stay: Premium Luxury Hotel in Katra",
                    "Meals Included: Breakfast & Nourishing Dinner",
                ],
            ),
            _day(
                3,
                "Katra to Jammu Local Sightseeing",
                (
                    "After a restorative breakfast, enjoy a peaceful checkout and travel comfortably back to Jammu city. Known as the "
                    "'City of Temples', Jammu offers beautiful spiritual and historical sites. Visit the grand Raghunath Temple complex "
                    "in the center of the city, followed by the historic Bahu Fort and its adjoining beautifully landscaped gardens. "
                    "Spend your evening exploring the best local shopping spots for premium traditional shawls, saffron, and "
                    "high-quality dry fruits."
                ),
                [
                    "Sightseeing Included: Raghunath Temple, Bahu Fort, Bagh-e-Bahu Gardens",
                    "Evening Experience: Luxury sunset views over the Tawi River valley",
                    "Overnight Stay: Luxury Hotel in Jammu",
                    "Meals Included: Breakfast & Dinner",
                ],
            ),
            _day(
                4,
                "Departure from Jammu",
                (
                    "Conclude your spiritual holiday on a grand note. After a luxurious breakfast at your hotel, enjoy a timely "
                    "transfer back to Jammu Airport or Jammu Tawi Railway Station. Your divine trip concludes seamlessly under the "
                    "careful oversight of TRAGUIN, leaving you blessed, peaceful, and filled with unforgettable memories of a "
                    "beautiful pilgrimage."
                ),
                [
                    "Transfers Included: Private luxury transfer to Airport/Station",
                    "Meals Included: Premium Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Welcomhotel by ITC Hotels, Katra | Radisson Blu / Hari Niwas Palace, Jammu",
                "Katra / Jammu",
                "03 Nights",
                "Luxury",
                "Handpicked Luxury Rooms",
                "Pure Veg Breakfast & Dinner",
                5,
                1,
                description=(
                    "OPTION 01 – LUXURY: Welcomhotel by ITC Hotels, Katra (2 Nights) • "
                    "Radisson Blu / Hari Niwas Palace, Jammu (1 Night)"
                ),
            ),
            _hotel(
                "Hotel Fortune Park / Ramada Katra | Zone by The Park, Jammu",
                "Katra / Jammu",
                "03 Nights",
                "Premium",
                "Handpicked Premium Rooms",
                "Premium Breakfast & Dinner",
                4,
                2,
                description=(
                    "OPTION 02 – PREMIUM: Hotel Fortune Park / Ramada Katra (2 Nights) • "
                    "Zone by The Park, Jammu (1 Night)"
                ),
            ),
        ],
        inclusions=[
            _inc_included("03 Nights luxurious stay in award-winning handpicked hotels", 1),
            _inc_included("Delicious pure vegetarian breakfast and dinner menus daily", 2),
            _inc_included("Exclusive private transfers in premium AC luxury vehicles", 3),
            _inc_included("Pre-arranged Yatra Parchi registration and VIP guidance", 4),
            _inc_included("Complimentary traditional welcome immunity drinks & high-quality dry fruit box", 5),
            _inc_included("24/7 Dedicated TRAGUIN support helpline for a hassle-free journey", 6),
            _inc_excluded("Helicopter tickets or ropeway passes (Available as add-on)", 7),
            _inc_excluded("Porter/Palki charges during the mountain climb", 8),
            _inc_excluded("Personal items, medical expenses, or standard travel insurance", 9),
        ],
    )
    return package, itinerary


def build_jk_017(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "JK-017"
    tour_code = "TRAGUIN-KASHMIR-WINTER-JK017"
    title = "Winter Luxury Tour Srinagar Gulmarg Pahalgam Sonamarg"
    duration = "05 Nights / 06 Days"
    slug = "jk-017-winter-luxury-tour-srinagar-gulmarg-pahalgam-sonamarg"
    itin_slug = "jk-017-winter-luxury-tour-srinagar-gulmarg-pahalgam-sonamarg-itinerary"
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
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Kashmir / India | Category: Winter Luxury Tour", 2),
            _ph("Destinations Covered: Srinagar • Gulmarg • Pahalgam • Sonamarg", 3),
            _ph("Ideal for: Honeymoon, Families & Luxury Travelers", 4),
            _ph("Best season: December to March (Winter Snow)", 5),
            _ph("Starting price: On Request (Premium Tier)", 6),
            _ph("Travel Dates: Flexible / Customized Choice", 7),
            _ph("Group Type: FIT / Private Luxury Couple or Family Group", 8),
            _ph("Vehicle: Private Luxury SUV (Innova Crysta / Equivalent with heating)", 9),
            _ph("Meal Plan: MAPAI (Premium Breakfast & Premium Dinner Included)", 10),
            _ph(
                "Route Map: Srinagar Airport → Srinagar Houseboat → Sonamarg → Gulmarg → Pahalgam → Srinagar Airport",
                11,
            ),
            _ph(
                "TRAGUIN Curated Experience Note: VIP Gondola line access guidelines, special warm traditional Kehwa welcomes, "
                "and premium handpicked hotels with optimized heating facilities.",
                12,
            ),
            _ph(
                "Shopping & Local Experiences: 100% authentic hand-knotted Cashmere and Pashmina shawls, handwrought "
                "Walnut wood carvings, organic saffron strands from Pampore, and fresh Kashmiri almonds and walnuts.",
                13,
            ),
            _ph(
                "Important Notes: Gulmarg Gondola tickets are subject to availability and must be booked at least 30 days in "
                "advance. Winter temperatures can drop to -10°C — pack heavy thermal wear, gloves, windcheaters, and waterproof "
                "boots. Heavy snow may require switching to local vehicles with snow chains at Tangmarg/Gulmarg. Standard "
                "check-in is 14:00 hrs and check-out is 11:00 hrs.",
                14,
            ),
        ],
        moods=["Winter", "Luxury", "Honeymoon"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Class)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Winter Luxury Tour — Srinagar • Gulmarg • Pahalgam • Sonamarg",
        overview=(
            "Experience paradise on earth wrapped in a blanket of pristine white snow with the Best Kashmir Tour Package by "
            "TRAGUIN. This winter, let us take you on an emotional journey through breathtaking landscapes, frozen alpine lakes, "
            "and dramatic snow-capped peaks. Our Luxury Kashmir Holiday promises an immersive experience into the heart of the "
            "valley, combining traditional Kashmiri warmth with highly curated experiences that stay etched in your memory forever. "
            "Discover why a Kashmir Honeymoon Package or an exclusive Kashmir Family Tour remains the ultimate Indian luxury "
            "getaway.\n\n"
            "Embark on an extraordinary winter odyssey meticulously planned by our expert travel consultants. This Premium "
            "Kashmir Experience guarantees seamless logistics, beautiful stays, and personalized touches.\n\n"
            "Kashmir in winter is a magical realm that rivals the Swiss Alps. Choosing the right TRAGUIN Kashmir Packages ensures "
            "you unlock the best-kept secrets of the valley. From the legendary Mughal Gardens to the snowy ski slopes of Gulmarg, "
            "every destination offers an unparalleled visual feast. Why Visit in Winter: Witness the phenomenon of complete snow "
            "transformation. Top Tourist Places in Kashmir Covered: The iconic Dal Lake, the frozen paradise of Sonamarg, the "
            "thrilling high-altitude meadow of Gulmarg, and the soothing, pine-sheltered valleys of Pahalgam."
        ),
        seo_title="JK-017 | Winter Luxury Tour Srinagar Gulmarg Pahalgam Sonamarg | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days winter Kashmir package (JK-017 / TRAGUIN-KASHMIR-WINTER-JK017): "
            "Srinagar houseboat, Sonamarg, Gulmarg Gondola, Pahalgam valleys, Mughal Gardens, and 4-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Dal Lake luxury houseboat stay with Shikara ride and Sonamarg snow excursion", 1),
            _ih("Gulmarg Gondola Phase I & II to Apharwat Peak and Pahalgam valley sightseeing", 2),
            _ih("Betaab Valley, Aru Valley, Chandanwari Snow Park and Mughal Gardens heritage walk", 3),
            _ih("TRAGUIN Signature Experience: Private, romantic floating musical session on Dal Lake", 4),
            _ih(
                "Curated by TRAGUIN Experts: Itinerary built by regional experts to ensure maximum comfort during peak winter",
                5,
            ),
            _ih(
                "Premium Handpicked Hotels: Properties selected explicitly for superior central heating, top-tier bedding, "
                "and standard of service",
                6,
            ),
            _ih("Personalized Assistance: Direct hotlines to regional managers for instantaneous support and dynamic changes", 7),
        ],
        days=[
            _day(
                1,
                "Arrival in Srinagar — Welcome to the Winter Wonderland & Luxurious Houseboat Experience",
                (
                    "Your exceptional Luxury Kashmir Holiday begins as you touch down at Srinagar International Airport. Our "
                    "dedicated local representative welcomes you into a world of warmth amidst freezing temperatures, transferring "
                    "you in a premium heated luxury vehicle to the banks of the legendary Dal Lake. Step into a meticulously "
                    "handpicked luxury houseboat, an architectural marvel of carved cedarwood. Relax with a steaming cup of "
                    "traditional Kashmiri saffron Kehwa. In the late afternoon, enjoy a 1-hour immersive Shikara ride across the "
                    "mirrored waters of Dal Lake. Watch the vibrant sunset reflect off floating gardens and snow-capped peaks. "
                    "Explore local floating markets for an authentic local interaction."
                ),
                [
                    "Sightseeing Included: Dal Lake, Floating Markets, Boulevard Road.",
                    "Optional Activities: Photography session in traditional Kashmiri attire (Pheran).",
                    "Evening Experience: Private candlelight setup or traditional musical seating in the houseboat lounge.",
                    "Overnight Stay: Handpicked Luxury Floating Houseboat, Dal Lake, Srinagar.",
                    "Meals Included: Premium Dinner.",
                ],
            ),
            _day(
                2,
                "Srinagar to Sonamarg to Srinagar — Excursion to the Meadow of Gold Wrapped in Frozen Silver",
                (
                    "Awake to the crisp winter morning breeze and relish a royal breakfast. Today we proceed for a breathtaking "
                    "day excursion to Sonamarg, famously called the 'Meadow of Gold'. The scenic route takes you alongside the "
                    "roaring Sindh River, bordered by majestic snow-laden pine forests. Sonamarg in winter serves as an ultimate "
                    "backdrop for a Premium Kashmir Experience. Walk across the snowy plains or hire a local pony to explore the "
                    "mesmerizing Thajiwas Glacier viewpoint. The dramatic ice structures and raw mountain vistas provide excellent "
                    "photography points for breathtaking memories."
                ),
                [
                    "Sightseeing Included: Sindh River Valley, Sonamarg Snow Meadows, Thajiwas Point Access.",
                    "Optional Activities: Sledge riding, snow biking across frozen trails.",
                    "Evening Experience: Return to Srinagar; warm casual dining at a famous boutique cafe overlooking the river.",
                    "Overnight Stay: Premium Luxury Hotel, Srinagar.",
                    "Meals Included: Premium Breakfast & Premium Dinner.",
                ],
            ),
            _day(
                3,
                "Srinagar to Gulmarg — Journey to the Skiing Capital of Asia & Gondola Adventure",
                (
                    "After breakfast, check out and drive towards Gulmarg, the crown jewel of Kashmir Sightseeing. The drive "
                    "climbs through winding mountain passes adorned with giant fir trees heavy with fresh winter snow. Upon "
                    "reaching Gulmarg, check into your ultra-luxury alpine resort featuring top-tier central heating. Today, "
                    "enjoy the legendary Gulmarg Gondola Ride (Phase 1 & Phase 2), one of the highest cable cars in the world. "
                    "Ascend above the clouds to Apharwat Peak at over 13,000 feet. Look out over panoramic, uninterrupted views "
                    "of the mighty Himalayas covered in deep white powder—a true highlight of your TRAGUIN Kashmir Packages."
                ),
                [
                    "Sightseeing Included: Tangmarg Scenic Pass, Gulmarg Golf Course, Gondola Cable Car Ride.",
                    "Optional Activities: Professional skiing lessons, snowboarding, high-speed snowmobile rides.",
                    "Evening Experience: Hot chocolate session by the resort's fireplace.",
                    "Overnight Stay: Handpicked Ultra Luxury Heated Resort, Gulmarg.",
                    "Meals Included: Premium Breakfast & Premium Dinner.",
                ],
            ),
            _day(
                4,
                "Gulmarg to Pahalgam — Traversing the Saffron Fields to the Shepherds' Vale",
                (
                    "Relish a lavish breakfast amidst views of snow-draped pine woods before driving to Pahalgam. En route, we "
                    "pass through the historic town of Pampore to admire the sprawling saffron cultivation fields. We then trace "
                    "the path of the beautiful Lidder River to enter Pahalgam, the iconic 'Valley of Shepherds'. Pahalgam is "
                    "globally renowned for its scenic beauty and tranquil environment. Check into your luxury riverside resort. "
                    "Spend the afternoon strolling along the banks of the Lidder River, taking in the dramatic mountain cliffs "
                    "and crisp mountain air."
                ),
                [
                    "Sightseeing Included: Pampore Saffron Fields, Lidder River Trail, Avantipur Ruins.",
                    "Optional Activities: Trout fishing experience (seasonal), traditional local market walk.",
                    "Evening Experience: Multi-course traditional Kashmiri Wazwan dinner experience at the resort.",
                    "Overnight Stay: Luxury Riverside Resort, Pahalgam.",
                    "Meals Included: Premium Breakfast & Premium Dinner.",
                ],
            ),
            _day(
                5,
                "Pahalgam Valley Sightseeing to Srinagar — Exploring Iconic Cinematic Valleys & Return to Srinagar",
                (
                    "Enjoy a wonderful breakfast before setting out to explore the cinematic valleys of Pahalgam via local union "
                    "vehicles. Visit Betaab Valley, named after the Bollywood blockbuster movie, where dense pine forests frame a "
                    "clear river. Proceed to Chandanwari, the historical starting point of the holy Amarnath Yatra, which transforms "
                    "into a snow playground in winter. Finally, explore Aru Valley, an alpine meadow offering breathtaking vistas. "
                    "In the afternoon, enjoy a scenic drive back to Srinagar. Check into your hotel and spend the evening hunting "
                    "for exquisite local souvenirs."
                ),
                [
                    "Sightseeing Included: Betaab Valley, Aru Valley, Chandanwari Snow Park.",
                    "Optional Activities: Riverside horse riding, premium shopping for hand-knotted pashminas.",
                    "Evening Experience: Final night celebration dinner with live traditional santoor music backing.",
                    "Overnight Stay: Premium Luxury Hotel, Srinagar.",
                    "Meals Included: Premium Breakfast & Premium Dinner.",
                ],
            ),
            _day(
                6,
                "Srinagar Heritage Walk & Departure — Farewell to Paradise on Earth",
                (
                    "Savor your final breakfast in the valley. Depending on your flight schedule, embark on a light sightseeing tour "
                    "of the famous historic Mughal Gardens, including Nishat Bagh (The Garden of Pleasure) and Shalimar Bagh "
                    "(The Abode of Love), situated beautifully on the banks of Dal Lake. Bid adieu to the magical valley as our "
                    "chauffeur transfers you back to Srinagar International Airport. Carry home unforgettable memories, beautiful "
                    "photographs, and stories of a lifetime curated exclusively by TRAGUIN."
                ),
                [
                    "Sightseeing Included: Nishat Bagh, Shalimar Bagh, Shankaracharya Temple (optional).",
                    "Meals Included: Premium Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Hotel Lemon Tree Srinagar | Hotel Green Top Gulmarg | Hotel Mountview Pahalgam",
                "Srinagar / Gulmarg / Pahalgam",
                "05 Nights",
                "Deluxe",
                "Deluxe Room",
                "MAPAI (Breakfast + Dinner)",
                4,
                1,
                description=(
                    "OPTION 01 – DELUXE: Hotel Lemon Tree / Equivalent Srinagar (3N) • Hotel Green Top / Equivalent Gulmarg (1N) • "
                    "Hotel Mountview / Equivalent Pahalgam (1N)"
                ),
            ),
            _hotel(
                "Hotel Radisson Blu Srinagar | Grand Mumtaz Resort Gulmarg | Pine N Peak Resort Pahalgam",
                "Srinagar / Gulmarg / Pahalgam",
                "05 Nights",
                "Premium",
                "Premium Room",
                "MAPAI (Breakfast + Dinner)",
                4,
                2,
                description=(
                    "OPTION 02 – PREMIUM: Hotel Radisson Blu / Equivalent Srinagar (3N) • Grand Mumtaz Resort / Equivalent Gulmarg (1N) • "
                    "Pine N Peak Resort / Equivalent Pahalgam (1N)"
                ),
            ),
            _hotel(
                "The Lalit Grand Palace Srinagar | The Vintage Gulmarg | Hotel Heevan Pahalgam",
                "Srinagar / Gulmarg / Pahalgam",
                "05 Nights",
                "Luxury",
                "Luxury Club Room",
                "MAPAI (Breakfast + Dinner)",
                5,
                3,
                description=(
                    "OPTION 03 – LUXURY: The Lalit Grand Palace / Equivalent Srinagar (3N) • The Vintage Gulmarg / Equivalent (1N) • "
                    "Hotel Heevan / Equivalent Pahalgam (1N)"
                ),
            ),
            _hotel(
                "Taj Dal View Resort Srinagar | The Khyber Himalayan Resort Gulmarg | Welcomhotel Pine N Peak Pahalgam",
                "Srinagar / Gulmarg / Pahalgam",
                "05 Nights",
                "Ultra Luxury",
                "Premium Suite",
                "MAPAI (Breakfast + Dinner)",
                5,
                4,
                description=(
                    "OPTION 04 – ULTRA LUXURY: Taj Dal View Resort / Equivalent Srinagar (3N) • The Khyber Himalayan Resort (1N) • "
                    "Welcomhotel Pine N Peak (Suites) Pahalgam (1N)"
                ),
            ),
        ],
        inclusions=[
            _inc_included(
                "Accommodation: 05 Nights stay in handpicked, top-tier premium hotels, resorts, and luxury houseboats.",
                1,
            ),
            _inc_included("Meals: 05 Premium Breakfasts and 05 Multi-cuisine Dinners curated by executive chefs.", 2),
            _inc_included(
                "Transfers & Transport: Entire tour via private, heated Luxury SUV (Innova Crysta) including airport pickups and drop-offs.",
                3,
            ),
            _inc_included(
                "Sightseeing: Complete Kashmir Sightseeing itinerary as detailed including internal union vehicles at Pahalgam.",
                4,
            ),
            _inc_included("Welcome Amenities: Traditional Saffron Kehwa greeting and customized fruit basket on arrival.", 5),
            _inc_included("Complimentary Experiences: 1-Hour traditional Shikara Ride on Dal Lake.", 6),
            _inc_included("TRAGUIN Support: 24/7 dedicated on-ground concierge assistance and local expert guide integration.", 7),
            _inc_included("Taxes: All current fuel charges, toll taxes, parking fees, and driver allowances included.", 8),
            _inc_excluded("Airfare or Train tickets to and from Srinagar.", 9),
            _inc_excluded("Entry tickets to Mughal Gardens, historical monuments, and sanctuaries.", 10),
            _inc_excluded("Gulmarg Gondola Cable Car ride tickets (can be pre-booked via TRAGUIN add-on).", 11),
            _inc_excluded("Personal expenses: Laundry, telephone calls, tips, alcoholic or soft beverages.", 12),
            _inc_excluded("Adventure sports, horse riding, sledge pulling, and snow-bike hire charges.", 13),
            _inc_excluded("Travel Insurance and medical evacuation expenses.", 14),
            _inc_excluded("Any cost arising due to natural calamities, roadblocks, or flight delays.", 15),
        ],
    )
    return package, itinerary


KASHMIR_DOMESTIC_BUILDERS = [
    build_jk_011,
    build_jk_012,
    build_jk_013,
    build_jk_014,
    build_jk_015,
    build_jk_016,
    build_jk_017,
]
