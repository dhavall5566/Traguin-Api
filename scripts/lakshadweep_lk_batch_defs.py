"""Builder functions for LK-001 through LK-010 Lakshadweep premium packages."""

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

LAKSHADWEEP_SLUG = "lakshadweep"
LAKSHADWEEP_DESTINATION_ID = "c5aabbf4-29bd-4acc-ab75-cafb0ee94264"


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


def build_lk_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "LK-001"
    tour_code = "TG-LK-HON-001"
    title = "Premium Lakshadweep Romance Escape"
    duration = "04 Nights / 05 Days"
    slug = "lk-001-premium-lakshadweep-romance-escape"
    itin_slug = "lk-001-premium-lakshadweep-romance-escape-itinerary"
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
            _ph("State / Country: Lakshadweep, India | Category: Honeymoon / Romantic Escape", 2),
            _ph("Destinations Covered: Agatti Island • Bangaram Island • Thinnakara Island", 3),
            _ph("Ideal for: Honeymooners, Newlyweds, Luxury Couples", 4),
            _ph("Best season: October to mid-May", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Vehicle / Transfer: Private Speedboat Charters & Premium Island Airport AC Transfers", 7),
            _ph("Meal Plan: All Meals Included (Daily Gourmet Beach Breakfasts, Island Lunches & Romantic Dinners)", 8),
            _ph("Route Plan: Agatti Airport Arrival → Private Speedboat to Bangaram Island → Thinnakara Day Cruise → Agatti Departure", 9),
            _ph("Curated Note: Complete entry permit processing, VIP airport assistance, private beach arrangements, and dedicated on-ground concierge services managed by TRAGUIN Experts", 10),
            _ph("Bangaram Island: A teardrop-shaped uninhabited island surrounded by a shallow cream-colored lagoon — the absolute top romantic spot in the region", 11),
            _ph("Thinnakara Island: A tiny jewel facing Bangaram across a massive coral lagoon, perfect for exceptional couples' photography and private picnics", 12),
            _ph("Important Notes: Lakshadweep entry permits require clear passport-size scans shared with TRAGUIN 30 days before departure; BSNL and Airtel are the only active mobile networks; alcohol is prohibited except on Bangaram resort island", 13),
        ],
        moods=["Honeymoon", "Romance", "Luxury"],
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
        tagline="TRAGUIN Premium Lakshadweep Romance Escape • Agatti Island • Bangaram Coral Reefs • Thinnakara Lagoons • 04 Nights / 05 Days",
        overview=(
            "Escape to a secluded tropical paradise where turquoise waters meet endless white sands. The ultimate Lakshadweep Honeymoon Package, meticulously designed by TRAGUIN, invites you to start your new journey amid breathtaking landscapes and pristine isolation. Indulge in premium stays, handpicked beach villas, and exclusive experiences tailored to generate unforgettable memories. From romantic sunset cruises to underwater exploration, let the unparalleled scenic beauty of the islands define your romance.\n\n"
            "Vehicle / Transfer: Private Speedboat Charters & Premium Island Airport AC Transfers. Meal Plan: All Meals Included (Daily Gourmet Beach Breakfasts, Island Lunches & Romantic Dinners). Route Plan: Agatti Airport Arrival → Private Speedboat to Bangaram Island → Thinnakara Day Cruise → Agatti Departure. This premium luxury holiday includes complete entry permit processing, VIP airport assistance, private beach arrangements, and dedicated on-ground concierge services managed by TRAGUIN Experts.\n\n"
            "Lakshadweep is widely celebrated as India's most pristine and exclusive destination for a Luxury Lakshadweep Holiday or an idyllic Lakshadweep Honeymoon Package. Offering unmatched privacy, coral gardens, and crystal-clear lagoons, it stands out as the ultimate romantic retreat. Bangaram Island is a teardrop-shaped uninhabited island surrounded by a shallow cream-colored lagoon. Thinnakara Island is a tiny jewel facing Bangaram across a massive coral lagoon. Top Tourist Places in Lakshadweep include celebrated marine sanctuaries, Agatti coral ledges, and deep-sea shipwreck dive spots. The Best Time to Visit Lakshadweep is the sunny tropical window from October to May."
        ),
        seo_title="LK-001 | Premium Lakshadweep Romance Escape | TRAGUIN",
        seo_description="Premium 04 Nights / 05 Days Lakshadweep honeymoon package (LK-001 / TG-LK-HON-001): Agatti, Bangaram, Thinnakara, private candlelight dinner, and 2-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("TRAGUIN Signature Experience: Private beach island excursion with a dedicated crew to manage refreshments, shade, and safety completely", 1),
            _ih("Curated by TRAGUIN Experts: Direct partnerships with top marine guides to guarantee safe, spectacular, and exclusive snorkeling tracks", 2),
            _ih("Private 4-course beachfront candlelight dinner under the stars with soft instrumental acoustic music", 3),
            _ih("Bioluminescent plankton shimmering on the wet sand after sunset on Bangaram Island", 4),
            _ih("Exclusive private boat excursion to Thinnakara Island with curated beachside picnic under coconut palms", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Agatti – Private Speedboat to Bangaram Luxury",
                (
                    "Your extraordinary journey begins with a mesmerizing flight landing at Agatti Island Airport, surrounded entirely by turquoise waters. Upon arrival, a dedicated TRAGUIN island host will provide VIP assistance and guide you to your private speedboat charter. Skim smoothly across the transparent ocean to the premium sands of Bangaram Island Resort. After a warm welcome check-in to your beachfront cottage, enjoy a relaxed afternoon walking hand-in-hand along the endless sandbar."
                ),
                [
                    "Sightseeing Included: Agatti Lagoon View, Bangaram Beach Exploration",
                    "Welcome Amenities: Fresh coconut water blend, tropical fruit platter, and curated complimentary beachwear gift set.",
                    "Overnight Stay: Bangaram Island (Premium Beachfront Villa)",
                    "Meals Included: Lunch & Dinner",
                ],
            ),
            _day(
                2,
                "Coral Reef Revelation – Immersive Snorkeling & Marine Wonders",
                (
                    "Wake up to a premium morning breakfast served right by the breaking waves. Today, experience your TRAGUIN Signature Experience with a guided, private boat trip out to the outer coral reefs. Peer down at sea turtles, vibrant manta rays, and infinite schools of colorful fish. After a delicious fresh catch lunch on the shore, the afternoon is yours for premium leisure. As night falls, experience the magic of bioluminescent plankton shimmering on the wet sand."
                ),
                [
                    "Sightseeing Included: Bangaram Outer Coral Reef, Shipwreck Snorkeling Point",
                    "Evening Experience: A private beachside setup with premium seating to observe the starry night sky over the ocean.",
                    "Overnight Stay: Bangaram Island",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                3,
                "Excursion to Thinnakara Island – Private Lagoon Escape",
                (
                    "Relish a tropical breakfast before boarding an exclusive private boat to the neighboring island of Thinnakara. This uninhabited paradise offers complete seclusion. Swim through shallow, crystal-clear water where the deep blue ocean fades into pale jade. Enjoy a curated beachside afternoon picnic under coconut palms, specially organized by our crew. Capture timeless, iconic memories at the long, shifting sandspit tip."
                ),
                [
                    "Sightseeing Included: Thinnakara Island, Sandspit Lagoon Exploration",
                    "Photography Points: Shifting white sandspit edges framing perfect contrast against the vivid gradient water.",
                    "Overnight Stay: Bangaram Island (Premium Beachfront Villa)",
                    "Meals Included: Breakfast, Curated Picnic Lunch & Dinner",
                ],
            ),
            _day(
                4,
                "Agatti Island Highlights & Romantic Candlelight Beach Dinner",
                (
                    "Following breakfast, transfer back to Agatti Island via private speedboat to discover its unique local culture. Enjoy an immersive Lakshadweep Sightseeing tour in an open-air vehicle, visiting the Eastern side beach cliffs, the local museum, and small coir processing hamlets. In the evening, celebrate your love with a magnificent, private candlelight dinner directly on the beach, featuring customized seafood or gourmet vegetarian specialties."
                ),
                [
                    "Sightseeing Included: Agatti Culture Tour, Sea Turtle Nesting Beaches",
                    "Exclusive Experience: Private 4-Course Beachfront Candlelight Dinner under the stars with soft instrumental acoustic music.",
                    "Overnight Stay: Agatti Island (Premium Lagoon-View Suite)",
                    "Meals Included: Breakfast, Lunch & Special Candlelight Dinner",
                ],
            ),
            _day(
                5,
                "Departure from Paradise with Unforgettable Memories",
                (
                    "Savor a peaceful final breakfast overlooking the lagoon as your tropical adventure concludes. Your private chauffeur will drive you comfortably to Agatti Airport for your departure flight. Your extraordinary TRAGUIN Lakshadweep Packages honeymoon ends here, leaving you with eternal blessings and memories of a pristine island escape."
                ),
                [
                    "Meals Included: Breakfast",
                    "Assistance: Priority airport entry and baggage check-in handling by our local representative.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Bangaram Island Beachfront Resort",
                "Lakshadweep Stay (4 Nights)",
                "03 Nights",
                "Ultra Luxury",
                "Premium Air-Conditioned Ocean Suite",
                "All Meals Included",
                5,
                1,
                description="OPTION 01 – ULTRA LUXURY: Bangaram Island Beachfront Resort (Premium Air-Conditioned Ocean Suite)",
            ),
            _hotel(
                "Agatti Island Beach Resort / White Pearl Beach Stay",
                "Lakshadweep Stay (4 Nights)",
                "01 Night",
                "Luxury",
                "Lagoon-View AC Premium Cottage",
                "All Meals Included",
                5,
                2,
                description="OPTION 02 – LUXURY: Agatti Island Beach Resort / White Pearl Beach Stay (Lagoon-View AC Premium Cottage)",
            ),
        ],
        inclusions=[
            _inc_included("Handpicked hotel and beach villa accommodations as detailed.", 1),
            _inc_included("All island meals (Daily Breakfast, Lunch, and Curated Dinners).", 2),
            _inc_included("One premium 4-course private beachfront Candlelight Dinner.", 3),
            _inc_included("Full Lakshadweep Entry Permit and documentation processing.", 4),
            _inc_included("Private speedboat transfers between Agatti, Bangaram, and Thinnakara.", 5),
            _inc_included("Guided snorkeling session including high-grade equipment rental.", 6),
            _inc_included("Dedicated 24/7 on-call TRAGUIN Support and host assistance.", 7),
            _inc_excluded("Mainland commercial flights (Kochi to Agatti and return).", 8),
            _inc_excluded("Optional deep-sea Scuba Diving or structural catamaran rentals.", 9),
            _inc_excluded("Personal expenses such as laundry, telephone calls, or souvenir purchases.", 10),
            _inc_excluded("National travel insurance or medical evacuation costs.", 11),
        ],
    )
    return package, itinerary


def build_lk_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "LK-002"
    tour_code = "TG-LK-FAM-002"
    title = "Premium Lakshadweep Family Tour Package"
    duration = "05 Nights / 06 Days"
    slug = "lk-002-premium-lakshadweep-family-tour-package"
    itin_slug = "lk-002-premium-lakshadweep-family-tour-package-itinerary"
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
            _ph("State / Country: Lakshadweep, India | Category: Lakshadweep Discovery Family Tour", 2),
            _ph("Destinations Covered: Agatti Island • Bangaram Island • Thinnakara Island", 3),
            _ph("Ideal for: Families, Beach Lovers, Luxury Seekers", 4),
            _ph("Best season: October to mid-May", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Vehicle/Transit Type: Private AC Island Transfers & Exclusive Speedboat/Boat Charters", 7),
            _ph("Meal Plan: All Meals Included (Breakfast, Lunch, Evening Snacks & Dinner)", 8),
            _ph("Route Plan: Agatti Airport → Bangaram Island Day Cruise → Thinnakara Coral Lagoons → Agatti Departure", 9),
            _ph("Curated Note: Seamless entry permits, pre-arranged water sports access, private boat charters, and dedicated on-ground TRAGUIN Support", 10),
            _ph("Agatti Island: The breathtaking gateway to the islands, featuring a world-famous runway surrounded completely by sparkling blue ocean water", 11),
            _ph("Bangaram Island: An uninhabited teardrop-shaped luxury destination with stunning coral lagoons, popular as a top Instagram location globally", 12),
            _ph("Important Notes: Lakshadweep entry permits require 15-20 working days for processing; mobile connectivity limited to BSNL and Airtel; alcohol prohibited except on Bangaram", 13),
        ],
        moods=["Family", "Luxury", "Beach"],
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
        tagline="TRAGUIN Premium Lakshadweep Family Tour Package • Agatti Island • Bangaram Beach Island Escape • Thinnakara Lagoons • 05 Nights / 06 Days",
        overview=(
            "Welcome to paradise on earth. Our carefully customized Lakshadweep Family Tour created by TRAGUIN is expertly crafted to immerse you and your loved ones into a world of turquoise blue waters, powdery white sand beaches, and vibrant coral reefs. Discover breathtaking landscapes, dramatic sunset horizons, and unforgettable memories at a beautifully relaxing pace. Enjoy premium stays and handpicked hotels that offer unprecedented comfort alongside warm hospitality.\n\n"
            "Vehicle/Transit Type: Private AC Island Transfers & Exclusive Speedboat/Boat Charters. Meal Plan: All Meals Included (Breakfast, Lunch, Evening Snacks & Dinner). Route Plan: Agatti Airport → Bangaram Island Day Cruise → Thinnakara Coral Lagoons → Agatti Departure. This premium luxury escape features seamless entry permits, pre-arranged water sports access, private boat charters, and dedicated on-ground TRAGUIN Support.\n\n"
            "Lakshadweep stands as India's ultimate pristine archipelago, offering an unmatched option for a Luxury Lakshadweep Holiday or a romantic Lakshadweep Honeymoon Package. Known for its endless marine life and peaceful shores, it is ideal for a premium Lakshadweep Family Tour. Agatti Island is the breathtaking gateway to the islands. Bangaram Island is an uninhabited teardrop-shaped luxury destination with stunning coral lagoons. Top Tourist Places in Lakshadweep include pristine Kalpitti Island, Thinnakara coral zones, and the endless sandbanks of Bangaram. The Best Time to Visit Lakshadweep is the tropical, sun-kissed season from October to May."
        ),
        seo_title="LK-002 | Premium Lakshadweep Family Tour Package | TRAGUIN",
        seo_description="Premium 05 Nights / 06 Days Lakshadweep family package (LK-002 / TG-LK-FAM-002): Agatti, Bangaram, Thinnakara, Kalpitti sunset, and 2-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("TRAGUIN Signature Experience: Private family beach picnic with a personal chef on an uninhabited island sandspit", 1),
            _ih("Curated by TRAGUIN Experts: Highly personalized island itineraries ensuring optimal safety for children and elders during boat transits", 2),
            _ih("Premium Handpicked Hotels: Elite beachfront properties offering direct lagoon access from your private balcony patio", 3),
            _ih("Exclusive private boat to Kalpitti Island for a completely private family sunset experience", 4),
            _ih("Complimentary family snorkeling session and glass-bottom boat tour included", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Agatti Island – First Glimpse of Turquoise Paradise",
                (
                    "Arrive at Agatti Airport, experiencing one of the most stunning aerial landings in the world. A warm greeting awaits you from your local TRAGUIN island host, followed by a brief, private check-in process at your premium beachside hotel. After lunch, enjoy a relaxed stroll along the pristine white sands of Agatti. As the sun dips below the horizon, enjoy your first sunset view of this breathtaking tropical wonderland."
                ),
                [
                    "Sightseeing Included: Agatti Private Beach Walk, Island Village Exploration",
                    "Evening Experience: Traditional welcome refreshments and fresh coconut water at the beachside lounge.",
                    "Overnight Stay: Agatti Island (Premium Beach Resort)",
                    "Meals Included: Lunch, Evening Snacks & Dinner",
                ],
            ),
            _day(
                2,
                "Private Speedboat Escape to Uninhabited Bangaram Island",
                (
                    "After a premium morning breakfast, board your private chartered speedboat for a thrilling ride across the turquoise lagoon to the world-famous Bangaram Island. This completely uninhabited island is surrounded by a vast coral reef lagoon. Spend your day swimming in the crystalline waters, lounging under coconut palms, or enjoying an immersive reef walk with our certified island guide."
                ),
                [
                    "Sightseeing Included: Bangaram Island Lagoon, Coral Reef Walks",
                    "Photography Points: The endless sandspit of Bangaram, where the turquoise water splits into multiple shades of blue.",
                    "Overnight Stay: Agatti / Bangaram Premium Island Tents or Cottages",
                    "Meals Included: Breakfast, Buffet Lunch, Dinner",
                ],
            ),
            _day(
                3,
                "Thinnakara Island Cruise & Lagoon Snorkeling Adventure",
                (
                    "Savor a fresh tropical breakfast by the beach. Today, take a boat cruise to the nearby jewel of Thinnakara Island. Known for its spectacular marine ecosystem, your family can participate in custom, safely guided snorkeling sessions to see colorful corals, vibrant sea turtles, and exotic fish species. Enjoy a private family picnic lunch right on the beach, experiencing true barefoot luxury."
                ),
                [
                    "Sightseeing Included: Thinnakara Lagoon, Sea Turtle Nesting Points",
                    "Optional Activities: Glass-bottom boat rides for children and elders to view corals without getting wet.",
                    "Overnight Stay: Agatti Island Premium Resort",
                    "Meals Included: Breakfast, Beach Picnic Lunch, Dinner",
                ],
            ),
            _day(
                4,
                "Agatti Island Sightseeing & Scenic Southern Excursion",
                (
                    "Dedicate your day to an extensive Lakshadweep Sightseeing tour across Agatti Island. Travel in a comfortable private vehicle to see the local culture, visiting the traditional coir weaving centers, the island museum, and the bustling eastern jetty. In the late afternoon, take an exclusive private boat to the nearby uninhabited Kalpitti Island for a glorious, completely private family sunset experience."
                ),
                [
                    "Sightseeing Included: Agatti Island Tour, Coir Museum, Kalpitti Island Sunset Trip",
                    "Evening Experience: A premium beachside live seafood barbecue dinner arranged exclusively for your family.",
                    "Overnight Stay: Agatti Island",
                    "Meals Included: Breakfast, Lunch, Special BBQ Dinner",
                ],
            ),
            _day(
                5,
                "Leisure at the Lagoons – Water Sports & Kawaratti Channels",
                (
                    "Enjoy a relaxed morning breakfast. This day is reserved for total leisure and personalized water sports experiences. Your family can choose to participate in thrilling activities like kayaking, stand-up paddleboarding, or a discover scuba diving session under the guidance of TRAGUIN Experts. Alternatively, simply relax on the sun lounger with a book, taking in the unparalleled scenic beauty."
                ),
                [
                    "Optional Activities: Kayaking, Jet-skiing, or Deep Sea Fishing tours.",
                    "Evening Experience: A special family farewell dinner accompanied by traditional island music.",
                    "Overnight Stay: Agatti Island (Premium Stay)",
                    "Meals Included: Breakfast, Lunch, Farewell Dinner",
                ],
            ),
            _day(
                6,
                "Farewell Lakshadweep – Departure with Forever Memories",
                (
                    "Savor your final breakfast overlooking the shimmering lagoon. Pack your bags filled with beautiful souvenirs, handmade sea-shell crafts, and incredible photographs. Your private island transport will drive you comfortably to Agatti Airport for your return flight. Your memorable TRAGUIN Lakshadweep Packages experience concludes here, leaving you with unforgettable memories of a true island paradise."
                ),
                [
                    "Meals Included: Breakfast",
                    "Assistance: Direct airport gate drop-off and entry permit clearance verification support.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Bangaram Island Beach Resort",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Luxury",
                "Air-Conditioned Premium Beach Cottages",
                "All Meals Included",
                5,
                1,
                description="OPTION 01 – LUXURY: Bangaram Island Beach Resort (Air-Conditioned Premium Beach Cottages)",
            ),
            _hotel(
                "Agatti Island Beach Resort / Kasims Beach Villa",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Premium",
                "Premium Beachfront Executive Suites",
                "All Meals Included",
                5,
                2,
                description="OPTION 02 – PREMIUM: Agatti Island Beach Resort / Kasims Beach Villa (Premium Beachfront Executive Suites)",
            ),
        ],
        inclusions=[
            _inc_included("Premium handpicked accommodations on a beach-facing property.", 1),
            _inc_included("All daily meals (Breakfast, Lunch, Dinner, Snacks) with local/mainland variations.", 2),
            _inc_included("Private chartered speedboats for Bangaram and Thinnakara excursions.", 3),
            _inc_included("Mandatory Lakshadweep Entry Permits and documentation clearances.", 4),
            _inc_included("Complimentary family snorkeling session and glass-bottom boat tour.", 5),
            _inc_included("Dedicated 24/7 on-ground TRAGUIN Support.", 6),
            _inc_excluded("Flights from Kochi to Agatti and return airfare.", 7),
            _inc_excluded("Scuba diving or personalized jet-ski hire charges.", 8),
            _inc_excluded("Personal expenses such as laundry, phone calls, or tips.", 9),
            _inc_excluded("Mandatory travel and medical insurance policies.", 10),
        ],
    )
    return package, itinerary


def build_lk_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "LK-003"
    tour_code = "TG-LK-LUX-003"
    title = "Luxury Island Escape"
    duration = "05 Nights / 06 Days"
    slug = "lk-003-luxury-island-escape"
    itin_slug = "lk-003-luxury-island-escape-itinerary"
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
            _ph("State / Country: Lakshadweep, India | Category: Luxury Island Escape", 2),
            _ph("Destinations Covered: Agatti Island • Bangaram Island • Thinnakara Island", 3),
            _ph("Ideal for: Honeymooners, Couples, Luxury Seekers, Families", 4),
            _ph("Best season: October to mid-May", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Premium Speedboat & Luxury Yacht Charters between Islands", 7),
            _ph("Meal Plan: All-Inclusive Gourmet Dining (Breakfast, Lunch, High Tea, and Beachfront Dinners)", 8),
            _ph("Route Map: Agatti Airport Arrival → Bangaram Island Resort → Thinnakara Day Cruise → Agatti Departure", 9),
            _ph("TRAGUIN Signature Experience: Private sandbank picnic setup completely isolated from other tourists with a personalized butler service", 10),
            _ph("Shopping & Local Experiences: Agatti Local Markets — organic virgin coconut oil, hand-crafted seashell jewelry, spiced dried tuna sticks (Maas Min); Instagram Spots — sweeping palm-tree curve at Agatti's southern beach and the sandspit between Bangaram and Thinnakara at sunrise", 11),
            _ph("Important Notes: Flights and permits must be booked 60–90 days in advance; plucking coral or carrying shells is strictly prohibited; network connectivity is minimal (BSNL/Airtel function best)", 12),
        ],
        moods=["Honeymoon", "Luxury", "Romance"],
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
        tagline="TRAGUIN Premium Lakshadweep Luxury Island Escape • Agatti Island • Bangaram Island • Thinnakara Island Paradise • 05 Nights / 06 Days",
        overview=(
            "Welcome to an untouched marine paradise of pristine turquoise lagoons and white coral sands. This ultra-exclusive Luxury Lakshadweep Holiday curated passionately by TRAGUIN is expertly designed for discerning travelers looking for absolute seclusion, premium stays, and immersive experiences. Bask in the breathtaking landscapes of isolated atolls, delight in custom private yacht excursions, and harvest unforgettable memories within world-class handpicked hotels offering personalized elite hospitality.\n\n"
            "Travel Mode: Private Premium Speedboat & Luxury Yacht Charters between Islands. Meal Plan: All-Inclusive Gourmet Dining (Breakfast, Lunch, High Tea, and Beachfront Dinners). Route Plan: Agatti Airport Arrival → Bangaram Island Resort → Thinnakara Day Cruise → Agatti Departure. This premium TRAGUIN Lakshadweep Package includes pre-cleared e-permits, mandatory entry documentation, priority airport check-in, and private marine guide services throughout the expedition.\n\n"
            "Lakshadweep stands proudly as India's ultimate tropical archipelago, making it a globally searched choice for a Best Lakshadweep Tour Package or a romantic Lakshadweep Honeymoon Package. Bangaram Island is an uninhabited piece of paradise surrounded by an endless blue lagoon. Thinnakara Island is a scenic beauty hotspot with endless white sandbanks extending into the ocean. Top Tourist Places in Lakshadweep include Agatti's vibrant coconut groves, Bangaram's coral reefs, and the shipwreck diving zones. The Best Time to Visit Lakshadweep is the breezy dry period between October and May."
        ),
        seo_title="LK-003 | Luxury Island Escape | TRAGUIN",
        seo_description="Premium 05 Nights / 06 Days Lakshadweep luxury package (LK-003 / TG-LK-LUX-003): Agatti, Bangaram, Thinnakara, bioluminescent night safari, and 2-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Private speedboat charter from Agatti to Bangaram Island Resort with welcome sundowner mocktails", 1),
            _ih("Exclusive private snorkel safari with certified marine biologist at Bangaram Outer Reef", 2),
            _ih("Luxury yacht cruise to Thinnakara Island with overnight sandbank retreat and seafood beach BBQ", 3),
            _ih("Bioluminescent night safari and deep lagoon glass-bottom kayaking adventure", 4),
            _ih("Agatti island culture tour with coconut groves, village museum, and specialty far-eastern island dinner", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Agatti – Private Boat to Bangaram Luxury Paradise",
                (
                    "Your spectacular journey begins with a sensational flight view over coral rings as you touch down at Agatti Airport. Your specialized TRAGUIN island concierge welcomes you warmly and escorts you to the jetty. Step aboard an exclusive private speedboat charter cutting through the glowing azure waters to Bangaram Island Resort. Settle into your premium beachfront cottage, step straight onto the powder-soft sand, and view your first unforgettable sunset over the horizon."
                ),
                [
                    "Sightseeing Included: Agatti Turquoise Lagoon Cruise, Bangaram Beach Exploration",
                    "Evening Experience: Welcome sundowner mocktails under a private coconut canopy with live acoustic island music.",
                    "Overnight Stay: Bangaram Island (Premium Beachfront Villa)",
                    "Meals Included: Lunch & Gourmet Dinner",
                ],
            ),
            _day(
                2,
                "Immersive Coral Reef Recreation & Private Snorkel Safari",
                (
                    "Wake up to the calming sounds of lapping waves and enjoy a freshly prepared premium breakfast. Today, TRAGUIN Experts have arranged an exclusive private boat safari out to the finest coral points surrounding Bangaram. Accompanied by a certified marine biologist, enjoy an immersive experience snorkeling alongside sea turtles, vibrant parrotfish, and majestic manta rays in crystal-clear waters. Spend a lazy afternoon reading or relaxing under shaded pergolas."
                ),
                [
                    "Sightseeing Included: Bangaram Outer Reef, Shipwreck Viewpoint",
                    "Optional Activities: Scuba diving lessons for beginners or advanced drift diving with private instructors.",
                    "Overnight Stay: Bangaram Island",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                3,
                "Excursion to Thinnakara Island & Overnight Sandbank Retreat",
                (
                    "Savor a magnificent tropical breakfast before embarking on a short luxury yacht cruise to the companion island of Thinnakara. Uninhabited and incredibly raw, Thinnakara features jaw-dropping panoramic views of pure marine wilderness. Spend the afternoon exploring the teardrop-shaped island on foot, capturing breathtaking landscapes at every corner. As night approaches, view an unblemished sky completely free of city light pollution."
                ),
                [
                    "Sightseeing Included: Thinnakara Lagoon, Sandbank Walk",
                    "Photography Points: The striking sandbar at the tip of Thinnakara during low tide.",
                    "Overnight Stay: Bangaram Luxury Island Base / Premium Thinnakara Cottage",
                    "Meals Included: Breakfast, Picnic Lunch & Seafood Beach BBQ",
                ],
            ),
            _day(
                4,
                "Bioluminescent Night Safari & Deep Sea Kayaking Adventure",
                (
                    "After a refreshing morning breakfast, try an array of curated water sports. Glide seamlessly over the glass-like waters using premium transparent glass-bottom kayaks, allowing you to watch the marine life below without getting wet. In the evening, after dusk falls, experience a spellbinding phenomenon as your guides take you to special lagoon pockets to witness magical bioluminescent plankton glowing like stardust in the dark waters."
                ),
                [
                    "Sightseeing Included: Deep Lagoon Kayaking, Glowing Night Sea Sightseeing",
                    "Exclusive Experiences: Private photography session with a professional island photographer.",
                    "Overnight Stay: Bangaram Island Resort",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                5,
                "Agatti Island Tour – Culture, Coconut Groves & Local Cuisine",
                (
                    "Board your private speedboat charter back to Agatti Island for a beautiful change of pace. Experience an authentic local culture tour traveling in an open-air luxury cart. Visit traditional coir-weaving centers, see the charming island villages, and explore the dense, towering coconut plantations. In the evening, enjoy an exclusive beachfront dinner serving fresh local catch cooked with delicious Lakshadweep spices."
                ),
                [
                    "Sightseeing Included: Agatti Village Museum, Eastern Jetty, Coconut Plantation Trails",
                    "Food Suggestion: Traditional island fish curry infused with fresh-pressed coconut cream.",
                    "Overnight Stay: Agatti Island (Luxury Beachfront Resort Suite)",
                    "Meals Included: Breakfast, Lunch & Specialty Far-Eastern Island Dinner",
                ],
            ),
            _day(
                6,
                "Farewell Lakshadweep – Return Flight with Extraordinary Memories",
                (
                    "Indulge in a relaxing breakfast as the warm sun illuminates your resort patio. Pack your beachwear and hand-picked shell souvenirs as your private chauffeur drops you comfortably to the steps of Agatti International Airport terminal. Your unforgettable Lakshadweep Family Tour and premium island vacation concludes here, leaving you with eternal stories and blissful memories crafted exclusively by TRAGUIN."
                ),
                [
                    "Meals Included: Breakfast",
                    "Assistance: Priority boarding support and inner-permit verification clearance by our airport executive.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Bangaram Island Resort",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Ultra Luxury",
                "Premium Air-Conditioned Beach Villa",
                "All-Inclusive Gourmet Dining",
                5,
                1,
                description="OPTION 01 – ULTRA LUXURY: Bangaram Island Resort (Premium Air-Conditioned Beach Villa)",
            ),
            _hotel(
                "Agatti Island Beach Resort / Thinnakara Premium Tented Villas",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Luxury",
                "Suites",
                "All-Inclusive Gourmet Dining",
                5,
                2,
                description="OPTION 02 – LUXURY: Agatti Island Beach Resort / Thinnakara Premium Tented Villas (Suites)",
            ),
        ],
        inclusions=[
            _inc_included("Luxury island villa stays directly on pristine sandy beaches.", 1),
            _inc_included("All-inclusive elite meal plans (Breakfast, Lunch, High-tea, Dinner).", 2),
            _inc_included("Complimentary pre-arranged Lakshadweep Entry Permits and Heritage fees.", 3),
            _inc_included("Private speed-boat and yacht charters for inter-island transfers.", 4),
            _inc_included("Complimentary guided snorkeling safari including premium gear rental.", 5),
            _inc_included("Dedicated 24/7 localized emergency and hospitality TRAGUIN Support.", 6),
            _inc_excluded("Commercial flight tickets to/from Agatti Airport.", 7),
            _inc_excluded("Optional heavy scuba diving courses or deep-sea fishing charters.", 8),
            _inc_excluded("Personal laundry expenditures, souvenir shopping, or tips.", 9),
            _inc_excluded("Any personal travel insurance or medical coverage plans.", 10),
        ],
    )
    return package, itinerary


def build_lk_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "LK-004"
    tour_code = "TG-LK-FAM-004"
    title = "Premium Family Island Vacation"
    duration = "05 Nights / 06 Days"
    slug = "lk-004-premium-family-island-vacation"
    itin_slug = "lk-004-premium-family-island-vacation-itinerary"
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
            _ph("State / Country: Lakshadweep, India | Category: Premium Family Island Vacation", 2),
            _ph("Destinations Covered: Agatti Island • Bangaram Island Atoll", 3),
            _ph("Ideal for: Families, Multi-generational Groups, Couples", 4),
            _ph("Best season: October to Mid-May", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Premium Chauffeur AC Vehicles on land & High-Speed Safety Speedboats over sea", 7),
            _ph("Meal Plan: All-Inclusive Family Buffet Plan (Daily Breakfast, Lunch, High Tea, and Culinary Dinners)", 8),
            _ph("Route Map: Agatti Airport Arrival → Private Speedboat to Bangaram Island → Agatti Local Sightseeing → Departure", 9),
            _ph("TRAGUIN Signature Experience: A private beach canopy setup on an uninhabited sandbank with a dedicated family butler service", 10),
            _ph("Shopping & Local Experiences: Agatti Cooperative Shops — cold-pressed virgin coconut oil, hand-woven palm souvenirs, island dried spiced tuna packets; Instagram Spots — wooden docks at Agatti's southern edge and sweeping sandbanks between Bangaram and Thinnakara at sunset", 11),
            _ph("Important Notes: Flights and mandatory entry permits must be locked in 60 to 90 days before travel; removing corals or disturbing sea turtles is strictly illegal; cellular network coverage is minimal (BSNL and Airtel work best)", 12),
        ],
        moods=["Family", "Island Discovery", "Luxury"],
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
        tagline="TRAGUIN Premium Lakshadweep Family Tour Package • Agatti Island • Bangaram Island Coconut Lagoons Escape • 05 Nights / 06 Days",
        overview=(
            "Embark on the ultimate tropical adventure with your loved ones. This exclusively styled Lakshadweep Family Tour meticulously crafted by TRAGUIN unrolls a paradise of pristine turquoise waters and white sandy shorelines perfect for creating unforgettable memories. Indulge in premium stays, curated experiences, and absolute comfort as you discover breathtaking landscapes. Our handpicked hotels offer top-tier safety and multi-generational conveniences, ensuring a spectacular, stress-free Luxury Lakshadweep Holiday for adults and children alike.\n\n"
            "Vehicle / Transfer: Private Premium Chauffeur AC Vehicles on land & High-Speed Safety Speedboats over sea. Meal Plan: All-Inclusive Family Buffet Plan (Daily Breakfast, Lunch, High Tea, and Culinary Dinners). Route Plan: Agatti Airport Arrival → Private Speedboat to Bangaram Island → Agatti Local Sightseeing → Departure. This exclusive TRAGUIN Lakshadweep Package covers all required entry documentation and e-permit validation processing, complete with priority island tracking and family-friendly logistics assistance.\n\n"
            "The pristine Lakshadweep archipelago stands out as India's finest tropical destination. Agatti Island is the breathtaking gateway lagoon featuring endless rows of coconut palms. Bangaram Island is a stunning, uninhabited coral island ringed by a colossal blue lagoon. Top Tourist Places in Lakshadweep are celebrated for flourishing shallow coral reefs, sandspits, and multi-colored marine biodiversity. The Best Time to Visit Lakshadweep is the beautiful warm weather window between October and May."
        ),
        seo_title="LK-004 | Premium Family Island Vacation | TRAGUIN",
        seo_description="Premium 05 Nights / 06 Days Lakshadweep family package (LK-004 / TG-LK-FAM-004): Agatti, Bangaram, Thinnakara sandbank, bioluminescent evening, and 2-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Private high-speed boat charter from Agatti to Bangaram with family sunset gathering", 1),
            _ih("Family reef snorkel safari at Bangaram Marine Sanctuary with certified life-guards and PADI instructors", 2),
            _ih("Thinnakara Island escape with private island beach canopy and sandbank walkways", 3),
            _ih("Lagoon kayaking adventure and bioluminescent evening magic on Bangaram", 4),
            _ih("Agatti island tour with museum, coconut plantation trails, and special farewell family dinner", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Agatti – Speedboat Expedition to Bangaram Coral Island",
                (
                    "Fly into Agatti Airport, taking in the spectacular aerial views of emerald coral rings scattered over the deep blue ocean. Upon arrival, your dedicated TRAGUIN family tour concierge will welcome you and lead your transfer to the passenger jetty. Board your private high-speed boat charter across the shimmering coral waters straight to Bangaram Island Resort. Check into your premium beachfront interconnected villas, let the kids step right onto the soft powdery sand, and witness a magnificent sunset together."
                ),
                [
                    "Sightseeing Included: Agatti-Bangaram Scenic Lagoon Cruise",
                    "Evening Experience: A family sunset gathering on the beach with complimentary tropical welcome juices and fresh coconut treats.",
                    "Overnight Stay: Bangaram Island (Premium Beachfront Family Villas)",
                    "Meals Included: Lunch & Dinner Buffet",
                ],
            ),
            _day(
                2,
                "Family Reef Encounters – Private Reef Snorkel Safari",
                (
                    "Wake up to clear blue horizons and indulge in a premium breakfast buffet. Today, embark on an immersive family boat cruise to the calmest outer coral reef points of Bangaram. Under the close watch of our certified life-guards and PADI instructors, the whole family can safely snorkel over shallow waters to see sea turtles, colorful clownfish, and magnificent coral shapes. Enjoy a relaxed afternoon playing beach volleyball or collecting shells on the shore."
                ),
                [
                    "Sightseeing Included: Bangaram Marine Sanctuary Coral Reef Points",
                    "Optional Activities: Glass-bottom boat rides for senior family members or children who wish to see the reef dry.",
                    "Overnight Stay: Bangaram Island",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                3,
                "Thinnakara Island Escape & Isolated Sandbank Retreat",
                (
                    "Savor a magnificent tropical breakfast before joining an exclusive day cruise to the nearby uninhabited island of Thinnakara. The island boasts spectacular scenic beauty and feels like a private world. Walk hand-in-hand along the endless white sand bars extending into the crystal-clear ocean. TRAGUIN Experts will set up a beautiful private island beach canopy for your family to relax under while enjoying refreshing tropical drinks."
                ),
                [
                    "Sightseeing Included: Thinnakara Island Lagoon, Sandbank Walkways",
                    "Photography Points: Capture incredible drone-style shots on the thin white sandbars stretching into the turquoise water.",
                    "Overnight Stay: Bangaram Island Resort",
                    "Meals Included: Breakfast, Picnic Lunch & Beach BBQ Dinner",
                ],
            ),
            _day(
                4,
                "Lagoon Kayaking Adventure & Bioluminescent Evening Magic",
                (
                    "Enjoy a leisurely morning. Today is all about immersive water sports in the safe, shallow lagoons. Paddle together in premium tandem kayaks or try Stand-Up Paddleboarding over the transparent water. After dark, our island experts will lead a special night excursion to a unique beach cove to see bioluminescent plankton glowing like stars in the water—a truly magical experience for children and adults alike."
                ),
                [
                    "Sightseeing Included: Bangaram Lagoon Kayaking, Glowing Night Sea Safaris",
                    "Optional Activities: Scuba diving discovery programs for beginners or night beach treasure hunts for kids.",
                    "Overnight Stay: Bangaram Island",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                5,
                "Agatti Island Tour – Exclusive Village Insights & Handicrafts",
                (
                    "Board your private speedboat charter back to Agatti Island for a wonderful change of scenery. Take a family tour of the island in an open-air luxury cart. Discover traditional coir-weaving villages, visit the island museum, and wander through lush coconut groves. In the evening, enjoy a special farewell beachside dinner featuring authentic local delicacies and fresh catch prepared with traditional island spices."
                ),
                [
                    "Sightseeing Included: Agatti Museum, Coconut Plantation Trails, South Beach Point",
                    "Food Suggestion: Traditional grilled fish flavored with fresh coconut water and local lime spices.",
                    "Overnight Stay: Agatti Island (Luxury Beachfront Resort Suite)",
                    "Meals Included: Breakfast, Lunch & Special Farewell Family Dinner",
                ],
            ),
            _day(
                6,
                "Farewell Isles – Departure with Forever Memories",
                (
                    "Indulge in a final tropical breakfast at your resort while watching the turquoise waves lap the shore. Pack your bags and collect your hand-picked coral souvenirs before your private chauffeur transfers you comfortably to the Agatti Airport terminal gates. Your spectacular Lakshadweep Family Tour and premium island holiday concludes here, leaving you with beautiful stories and unforgettable memories."
                ),
                [
                    "Meals Included: Breakfast",
                    "Assistance: Airport checking clearance and permit clearance support managed entirely by our local crew.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Bangaram Island Resort",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Luxury",
                "Air-Conditioned Premium Beach Cottage Suite",
                "All-Inclusive Family Buffet Plan",
                5,
                1,
                description="OPTION 01 – LUXURY (Highly Recommended): Bangaram Island Resort (Air-Conditioned Premium Beach Cottage Suite)",
            ),
            _hotel(
                "Agatti Island Beach Resort / Tented Premium Eco-Villas",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Premium",
                "Deluxe Beachfront Family Accommodation",
                "All-Inclusive Family Buffet Plan",
                5,
                2,
                description="OPTION 02 – PREMIUM: Agatti Island Beach Resort / Tented Premium Eco-Villas (Deluxe Beachfront Family Accommodation)",
            ),
        ],
        inclusions=[
            _inc_included("Premium beachfront cottage accommodations with family layouts.", 1),
            _inc_included("All-inclusive gourmet buffet meal plans (Breakfast, Lunch, Dinner).", 2),
            _inc_included("Complimentary Lakshadweep e-permits, document handling, and entry fees.", 3),
            _inc_included("Private speed-boat charter for inter-island transits.", 4),
            _inc_included("Complimentary guided family snorkeling expedition with premium gear.", 5),
            _inc_included("Full time 24/7 dedicated local operational and emergency TRAGUIN Support.", 6),
            _inc_excluded("Airfare or flight ticket bookings to/from Agatti Airport.", 7),
            _inc_excluded("Advanced professional scuba diving certifications or deep-sea trolling.", 8),
            _inc_excluded("Personal laundry costs, shopping bills, or guide gratuities.", 9),
            _inc_excluded("Any comprehensive travel insurance or health coverage cards.", 10),
        ],
    )
    return package, itinerary


def build_lk_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "LK-005"
    tour_code = "TG-LK-ADV-005"
    title = "Scuba Ultra Adventure Package"
    duration = "04 Nights / 05 Days"
    slug = "lk-005-scuba-ultra-adventure-package"
    itin_slug = "lk-005-scuba-ultra-adventure-package-itinerary"
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
            _ph("State / Country: Lakshadweep, India | Category: Premium Adventure & Deep Sea Scuba", 2),
            _ph("Destinations Covered: Agatti Island • Bangaram Coral Reefs • Pitti Bird Sanctuary", 3),
            _ph("Ideal for: Adventure Seekers, Divers, Couples, Photographers", 4),
            _ph("Best season: October to mid-May", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Dedicated High-Powered Speedboat & Premium Scuba Dive Boats", 7),
            _ph("Meal Plan: All-Inclusive Energizing Meal Layouts (High Protein & Fresh Local Catch)", 8),
            _ph("Route Map: Agatti Airport Arrival → Bangaram Reef Wall → Pitti Island Waters → Agatti Departure", 9),
            _ph("TRAGUIN Signature Experience: Elite underwater photography and 4K video logs included complimentary with every deep marine wall dive", 10),
            _ph("Shopping & Local Experiences: Agatti Local Coir Stalls — premium sea-salt cures, virgin coconut items, handcrafted marine woodwork ornaments; Instagram Spots — hanging off the dive platform at Bangaram Wall and standing alone on the extreme tip of the Pitti sandspit during noon", 11),
            _ph("Important Notes: Strict 24-hour surface interval integrated into Day 04; PADI medical declaration required; TRAGUIN adheres to a 'no touch, no take' marine protection policy", 12),
        ],
        moods=["Adventure", "Scuba", "Luxury"],
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
        tagline="TRAGUIN Scuba Lakshadweep Ultra Adventure Package • Agatti Island Exploration • Bangaram Marine Wall • PADI Diving Experience • 04 Nights / 05 Days",
        overview=(
            "Plunge into an untamed water wilderness featuring dramatic ocean drop-offs, vibrant coral pinnacles, and crystal-clear visibility. This ultimate Luxury Lakshadweep Holiday organized explicitly by TRAGUIN targets true thrill-seekers and luxury enthusiasts. Discover the breathtaking landscapes of isolated marine atolls, undergo exclusive world-class scuba expeditions, and log unforgettable memories within handpicked hotels that serve elite oceanfront comforts and high-adrenaline memories.\n\n"
            "Travel Logistics: Private Dedicated High-Powered Speedboat & Premium Scuba Dive Boats. Meal Plan: All-Inclusive Energizing Meal Layouts (High Protein & Fresh Local Catch). Route Plan: Agatti Airport Arrival → Bangaram Reef Wall → Pitti Island Waters → Agatti Departure. This action-packed TRAGUIN Lakshadweep Package includes pre-cleared island e-permits, comprehensive PADI dive-master support, premium high-end equipment rental, and full insurance clearance.\n\n"
            "Lakshadweep stands unchallenged as India's premier marine exploration zone. Bangaram Marine Wall is a staggering underwater vertical drop-off covered with soft gorgonian corals and home to cruising reef sharks. Pitti Bird Sanctuary Waters is an isolated rocky outcrop surrounded by heavy schools of pelagic fish. Top Tourist Places in Lakshadweep include the coral pathways of Agatti, Bangaram's shipwreck zone, and the lagoon reef centers. The Best Time to Visit Lakshadweep is the clear, sunny months from October to mid-May."
        ),
        seo_title="LK-005 | Scuba Ultra Adventure Package | TRAGUIN",
        seo_description="Premium 04 Nights / 05 Days Lakshadweep scuba package (LK-005 / TG-LK-ADV-005): Bangaram Marine Wall, Princess Royal Shipwreck, Pitti pelagic drift, and 2-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Premium speedboat transit to Bangaram with PADI lagoon acclimatization check-dive", 1),
            _ih("Deep marine wall exploration and Princess Royal Shipwreck encounter with two tank dives", 2),
            _ih("Pitti Island pelagic drift cruise and uninhabited sandspit trek with island picnic lunch", 3),
            _ih("Deep sea kayak safari and Agatti high-speed watersports on barrier reef edges", 4),
            _ih("Logbook certification sign-off with custom TRAGUIN exploration stamps before departure", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Agatti – Deep Blue Transit & Reef Check Dive",
                (
                    "Your ultimate adventure launches with an iconic low-altitude flight across the spectacular blue lagoons into Agatti Airport. Your specialized TRAGUIN dive concierge greets you and coordinates immediate transfer to the pier. Board a custom premium speedboat to cross the sapphire waters to Bangaram Island. Check into your luxury beachfront villa and meet your PADI dive-master for equipment sizing followed by an afternoon shallow lagoon acclimatization check-dive."
                ),
                [
                    "Sightseeing Included: Agatti Lagoon Route, Bangaram Lagoon Coral Patches",
                    "Evening Experience: Sundowner technical briefing over fresh tropical juices detailing underwater signals and marine paths.",
                    "Overnight Stay: Bangaram Island (Premium Beachfront Villa)",
                    "Meals Included: Lunch & Dinner",
                ],
            ),
            _day(
                2,
                "Deep Marine Wall Exploration & Shipwreck Encounter",
                (
                    "Fuel up with an early premium high-energy breakfast. Board the private dive boat for an immersive experience at the legendary Bangaram Marine Wall. Drop down to 20 meters along a vertical canyon to spot sea turtles, moray eels, and sleeping white-tip reef sharks. Following an oceanfront surface interval, execute your second dive exploring a forgotten coastal shipwreck, now transformed into a busy artificial reef complex teeming with thousands of colorful damselfish."
                ),
                [
                    "Sightseeing Included: Bangaram Drop-off Wall, Princess Royal Shipwreck Site",
                    "Optional Activities: Night scuba diving session using specialty underwater torch tracking bioluminescent organisms.",
                    "Overnight Stay: Bangaram Island",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                3,
                "Pitti Island Pelagic Drift Cruise & Uninhabited Sandspit Trek",
                (
                    "Enjoy an early breakfast before crossing deep ocean channels on a fast-paced expedition toward the protected waters of Pitti Island. Witness thousands of pelagic terns circling overhead this isolated wildlife outpost. Experience an open-ocean boat drift dive to watch large pelagics, including eagle rays and tuna schools. Spend your afternoon relaxing on a fully deserted sandbank, dining on a specialized grilled picnic layout prepared exclusively for you."
                ),
                [
                    "Sightseeing Included: Pitti Bird Sanctuary Waters, Deserted Sandbank Trails",
                    "Photography Points: Striking aerial drone-style perspectives over the pristine, thin sandbars during low tide.",
                    "Overnight Stay: Bangaram Island Resort Base",
                    "Meals Included: Breakfast, Island Picnic Lunch & Beachside BBQ",
                ],
            ),
            _day(
                4,
                "Deep Sea Kayak Safari & Agatti High-Speed Watersports",
                (
                    "Following breakfast, board your private speed charter back to Agatti Island. Today is dedicated to surface high-adventure water sports. Power across the lagoon on high-speed jet skis, try deep-sea windsurfing, or lead a long-distance sea kayak safari along the outer barrier reef edges. In the evening, unwind at a premium seaside dining setup, listening to the roar of waves crashing onto the outer coral reef walls."
                ),
                [
                    "Sightseeing Included: Agatti Barrier Reef, Lagoon Water Sports Zone",
                    "Exclusive Experiences: High-definition action camera footage of your dives compiled and presented by our underwater media team.",
                    "Overnight Stay: Agatti Island (Luxury Beachfront Resort Suite)",
                    "Meals Included: Breakfast, Lunch & Specialty Island Dinner",
                ],
            ),
            _day(
                5,
                "Logbook Certification & Return Flight with Extraordinary Memories",
                (
                    "Savor a final tropical breakfast on your open deck. Review your ocean milestones with your instructor as you sign off your official dive logbooks with custom TRAGUIN exploration stamps. Your private chauffeur will transport you comfortably to the Agatti Airport gates. Your epic Lakshadweep Family Tour and ultimate scuba holiday concludes here, leaving you with eternal stories and fearless memories."
                ),
                [
                    "Meals Included: Breakfast",
                    "Assistance: Airport executive escort for smooth customs, baggage check, and permit closure updates.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Bangaram Island Resort",
                "Lakshadweep Stay (4 Nights)",
                "04 Nights",
                "Luxury Adventure",
                "Premium AC Beach Villa - Direct Ocean Access",
                "All-Inclusive Energizing Meal Layouts",
                5,
                1,
                description="OPTION 01 – LUXURY ADVENTURE: Bangaram Island Resort (Premium AC Beach Villa - Direct Ocean Access)",
            ),
            _hotel(
                "Agatti Island Beach Resort",
                "Lakshadweep Stay (4 Nights)",
                "04 Nights",
                "Premium",
                "Executive Lagoon View Suite",
                "All-Inclusive Energizing Meal Layouts",
                5,
                2,
                description="OPTION 02 – PREMIUM ESCAPE: Agatti Island Beach Resort (Executive Lagoon View Suite)",
            ),
        ],
        inclusions=[
            _inc_included("Premium beachfront accommodation steps away from active dive boats.", 1),
            _inc_included("All daily meals customized for intense physical ocean excursions.", 2),
            _inc_included("3 Fully guided boat scuba dives including PADI divemasters.", 3),
            _inc_included("All-inclusive entry permits, local heritage fees, and clearance papers.", 4),
            _inc_included("Private speedboat and high-powered vessel charters.", 5),
            _inc_included("Full technical equipment rental including dive computers and tanks.", 6),
            _inc_included("Dedicated 24/7 on-call localized operational TRAGUIN Support.", 7),
            _inc_excluded("Commercial flight ticketing to/from Agatti Airport terminal.", 8),
            _inc_excluded("Advanced specialized PADI certification course upgrades.", 9),
            _inc_excluded("Personal laundry, shopping, or tips for the boat crew.", 10),
            _inc_excluded("Any decompression chamber medical treatments or evacuation insurance.", 11),
        ],
    )
    return package, itinerary


def build_lk_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "LK-006"
    tour_code = "TG-LK-SNR-006"
    title = "Senior Citizen Leisure Tour"
    duration = "05 Nights / 06 Days"
    slug = "lk-006-senior-citizen-leisure-tour"
    itin_slug = "lk-006-senior-citizen-leisure-tour-itinerary"
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
            _ph("State / Country: Lakshadweep, India | Category: Senior Citizen Leisure Islands Escape", 2),
            _ph("Destinations Covered: Agatti Island • Bangaram Lagoon Atoll • Thinnakara Day Trip", 3),
            _ph("Ideal for: Senior Citizens, Retirees, Families seeking Slow Travel", 4),
            _ph("Best season: October to mid-May (Smooth seas & gentle climate)", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Senior-Accessible Speedboats & Stable Passenger Catamarans", 7),
            _ph("Meal Plan: All-Inclusive Wholesome Plan (Breakfast, Lunch, Soft High-Tea, and Gentle Dinners)", 8),
            _ph("Route Map: Agatti Airport Arrival → Stable Vessel Transfer → Bangaram Lagoon Base → Thinnakara Scenic Cruise → Agatti Departure", 9),
            _ph("TRAGUIN Signature Experience: A slow-paced, zero-rush daily schedule custom-built for older travelers to maximize comfort and physical ease", 10),
            _ph("Shopping & Local Experiences: Agatti Local Coir Cooperatives — fine organic coconut massage oils, hand-made shell keepsakes, sweet jaggery-infused coconut sweets; Instagram Spots — white sand spit at the tip of Bangaram Island and palm-bordered pathways of Agatti during golden hour", 11),
            _ph("Important Notes: Supply copies of government IDs 45 days prior to travel; walking on or touching live corals is strictly prohibited; basic health centers available on Agatti and Bangaram with emergency evacuation to Kochi", 12),
        ],
        moods=["Senior", "Leisure", "Slow Travel"],
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
        tagline="TRAGUIN Lakshadweep Senior Citizen Leisure Tour • Agatti Island • Bangaram Calm Lagoon • Relaxed Island Excursion • 05 Nights / 06 Days",
        overview=(
            "Welcome to India's most serene and mesmerizing tropical haven. Our tailored Lakshadweep Family Tour thoughtfully crafted by TRAGUIN is expertly refined for senior citizens, emphasizing a leisurely pace, absolute security, and zero physical strain. Witness breathtaking landscapes of turquoise water, unwind along shallow calm beaches, and capture unforgettable memories. Rest in premium stays and handpicked hotels that guarantee easy access, modern comforts, and warm island hospitality.\n\n"
            "Travel Logistics: Private Senior-Accessible Speedboats & Stable Passenger Catamarans. Meal Plan: All-Inclusive Wholesome Plan (Breakfast, Lunch, Soft High-Tea, and Gentle Dinners). Route Plan: Agatti Airport Arrival → Stable Vessel Transfer → Bangaram Lagoon Base → Thinnakara Scenic Cruise → Agatti Departure. This premium holiday features comprehensive ground assistance, pre-arranged administrative e-permits, mandatory entry document clearances, and gentle passenger assistance boarding lines managed completely by TRAGUIN Experts.\n\n"
            "Lakshadweep is a spectacular destination for mature travelers seeking a peaceful Luxury Lakshadweep Holiday. Bangaram Island Atoll is a tranquil island retreat completely enclosed by a calm lagoon with zero heavy waves. Thinnakara Island Views feature unmatched scenic beauty with shallow sandspits. Top Tourist Places in Lakshadweep include the historic coconut lanes of Agatti, the pristine turtle reefs of Bangaram, and the peaceful coral observation docks. The Best Time to Visit Lakshadweep is the highly favorable dry winter months from October to May."
        ),
        seo_title="LK-006 | Senior Citizen Leisure Tour | TRAGUIN",
        seo_description="Premium 05 Nights / 06 Days Lakshadweep senior leisure package (LK-006 / TG-LK-SNR-006): glass-bottom boat safari, Thinnakara sandspit, island wellness, and 2-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Effortless private transfer from Agatti to Bangaram with welcome tea party on soft sands", 1),
            _ih("Exclusive glass-bottom boat safari at Bangaram Inner Coral Reefs and Turtle Lagoon Shallows", 2),
            _ih("Thinnakara Island scenic boat excursion with sandspit visuals and lounge chairs under beach umbrellas", 3),
            _ih("Leisure resort day with island wellness, coconut plantation walkways, and sunset photography session", 4),
            _ih("Agatti heritage exploration with craft emporium, coconut groves, and wheelchair boarding assistance", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Agatti – Effortless Private Transfer to Bangaram",
                (
                    "Touch down at the exceptionally scenic Agatti Airport strip, looking out over a pristine azure sea. Your dedicated on-ground TRAGUIN coordinator welcomes you warmly at the exit gates and handles all heavy baggage. Relax in an open-air shuttle cart during a brief ride to the jetty, then step aboard a stable, luxury private speedboat charter. Glide smoothly over calm waters directly to your premium beachfront villa at Bangaram Island Resort."
                ),
                [
                    "Sightseeing Included: Agatti Palm Coastline View, Bangaram Beach Walkway",
                    "Evening Experience: A relaxed welcome tea party on the soft sands under shaded canopies as the tropical sun dips below the horizon.",
                    "Overnight Stay: Bangaram Island (Premium Beachfront Suite with Ground-Floor Entry)",
                    "Meals Included: Lunch & Wholesome Dinner",
                ],
            ),
            _day(
                2,
                "Calm Reef Cruise & Exclusive Glass-Bottom Boat Safari",
                (
                    "Indulge in a fresh tropical morning breakfast. Today, enjoy a highly curated, non-strenuous Premium Lakshadweep Experience. Board a specialized, stable glass-bottom boat designed to view marine life with absolute safety. Look straight through the transparent floor panels to observe vibrant living corals, giant sea turtles, and colorful schools of fish swimming right beneath your feet without having to swim or submerge."
                ),
                [
                    "Sightseeing Included: Bangaram Inner Coral Reefs, Turtle Lagoon Shallows",
                    "Optional Activities: A gentle, guided shallow-water wade assisted by our experienced island life-savers.",
                    "Overnight Stay: Bangaram Island",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                3,
                "Thinnakara Island Scenic Boat Excursion & Sandbank Visuals",
                (
                    "Savor a premium morning breakfast looking out at the turquoise sea. Enjoy a highly smooth, brief boat cruise across the calm lagoon to neighboring Thinnakara Island. Take a comfortable, slow-paced stroll along the pristine white sandbanks that merge gently into the transparent sea, capturing magnificent landscape photos. Relax on customized lounge chairs under large beach umbrellas with cool fresh coconut water."
                ),
                [
                    "Sightseeing Included: Thinnakara Sandspit, Isolated Lagoon Vistas",
                    "Photography Points: The vast, contrasting blue lines of the lagoon from the shaded Thinnakara shore.",
                    "Overnight Stay: Bangaram Island Resort",
                    "Meals Included: Breakfast, Light Picnic Lunch & Dinner",
                ],
            ),
            _day(
                4,
                "Leisure Resort Day – Island Wellness & Sunset Stories",
                (
                    "Enjoy a completely relaxed morning at your own pace. Today is dedicated to total rejuvenation and rest. Take a gentle walk through the resort's interior pathways, shaded beautifully by tall coconut palms. In the afternoon, enjoy an optional, soothing wellness massage at the resort's therapeutic center. Later in the evening, sit by the shore to listen to traditional folk storytelling and soft music performed by local islanders."
                ),
                [
                    "Sightseeing Included: Bangaram Interior Coconut Plantation Walkways",
                    "Exclusive Experiences: A dedicated, private sunset photography session on the beach for your family group.",
                    "Overnight Stay: Bangaram Island Resort",
                    "Meals Included: Breakfast, Lunch & Special Coastal Dinner",
                ],
            ),
            _day(
                5,
                "Agatti Island Heritage Exploration & Local Crafts",
                (
                    "Board your private speedboat charter back to Agatti Island for a beautiful change of scenery. Enjoy a perfectly relaxed island heritage tour using an open-air luxury cart with soft cushions. Visit a traditional coir-handicraft collective to meet local weavers and learn about traditional island life. Spend a peaceful evening sitting out on the resort terrace, savoring mild dishes infused with fresh local coconut flavors."
                ),
                [
                    "Sightseeing Included: Agatti Craft Emporium, Local Coconut Groves, Golden Beach Shallows",
                    "Food Suggestion: Freshly baked traditional rice-cakes and mild local vegetable broth.",
                    "Overnight Stay: Agatti Island (Luxury Beachfront Resort Suite)",
                    "Meals Included: Breakfast, Lunch & Farewell Special Dinner",
                ],
            ),
            _day(
                6,
                "Farewell Lakshadweep – Departure with Forever Memories",
                (
                    "Wake up to a quiet island morning and enjoy a delicious breakfast at the resort. Pack your handpicked seashell gifts and souvenirs as your private premium transport drives you smoothly to the Agatti Airport terminal gates. Your comforting, highly memorable Best Lakshadweep Tour Package vacation concludes here, leaving you with absolute peace of mind and unforgettable memories managed perfectly by TRAGUIN."
                ),
                [
                    "Meals Included: Breakfast",
                    "Assistance: Wheelchair or boarding lane queue-assistance completely pre-arranged by our airport escort.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Bangaram Island Resort",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Luxury",
                "Premium AC Beach Villa, Ground-Level Entry",
                "All-Inclusive Wholesome Plan",
                5,
                1,
                description="OPTION 01 – LUXURY (Highly Recommended): Bangaram Island Resort (Premium AC Beach Villa, Ground-Level Entry)",
            ),
            _hotel(
                "Agatti Island Beach Resort",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Premium",
                "Executive Lagoon View Suite, Easy Access Layout",
                "All-Inclusive Wholesome Plan",
                5,
                2,
                description="OPTION 02 – PREMIUM: Agatti Island Beach Resort (Executive Lagoon View Suite, Easy Access Layout)",
            ),
        ],
        inclusions=[
            _inc_included("Handpicked hotel villas with senior-accessible layout configurations.", 1),
            _inc_included("All-inclusive meal plans (Freshly cooked daily breakfasts, lunches, and dinners).", 2),
            _inc_included("Complimentary pre-processed Lakshadweep Entry Permits & Eco-clearances.", 3),
            _inc_included("Private speedboats and stable catamarans for inter-island transfers.", 4),
            _inc_included("Complimentary private glass-bottom boat safari for safe coral viewing.", 5),
            _inc_included("Consistent on-ground luggage and boarding TRAGUIN Support.", 6),
            _inc_excluded("Commercial airline or train tickets to/from Agatti.", 7),
            _inc_excluded("Optional heavy scuba diving expeditions or deep-sea trolling.", 8),
            _inc_excluded("Personal laundry items, optional spa bills, or staff gratuities.", 9),
            _inc_excluded("Any personal travel or medical insurance policies.", 10),
        ],
    )
    return package, itinerary


def build_lk_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "LK-007"
    tour_code = "TG-LK-FEM-007"
    title = "Ladies Island Escape"
    duration = "05 Nights / 06 Days"
    slug = "lk-007-ladies-island-escape"
    itin_slug = "lk-007-ladies-island-escape-itinerary"
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
            _ph("State / Country: Lakshadweep, India | Category: Exclusive Women-Only Luxury Escape", 2),
            _ph("Destinations Covered: Agatti Island • Bangaram Island • Thinnakara Island Atolls", 3),
            _ph("Ideal for: Female Solo Travelers, Girlfriends, Women Groups", 4),
            _ph("Best season: October to mid-May", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Premium Marine Speedboat & Luxury Yacht Charters (All-Female Friendly Crews)", 7),
            _ph("Meal Plan: All-Inclusive Beachfront Gourmet Dining (Detox Drinks, High Tea, Seafood BBQs)", 8),
            _ph("Route Map: Agatti Airport → Private Speedboat to Bangaram Island → Thinnakara Atoll Cruise → Agatti Departure", 9),
            _ph("TRAGUIN Signature Experience: Private beach sandbank lunch canopy set up away from crowds with a personal group hostess", 10),
            _ph("Shopping & Local Experiences: Agatti Local Cooperatives — extra virgin organic coconut oils, hand-woven palm mats, locally sourced spiced dried tuna; Top Instagram Locations — crystal-clear shallow lagoon waters of Bangaram and sweeping sandspits of Thinnakara at dawn", 11),
            _ph("Important Notes: Completely pre-cleared travel permits with priority bag management and local female guest assistance throughout", 12),
        ],
        moods=["Women-Only", "Luxury", "Wellness"],
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
        tagline="TRAGUIN Ladies Lakshadweep Island Escape • Agatti Island • Bangaram Island Private Cruise • Thinnakara Sandbanks • 05 Nights / 06 Days",
        overview=(
            "Welcome to an empowering paradise of absolute safety, turquoise wonders, and ultimate luxury freedom. This ultra-exclusive, female-only Luxury Lakshadweep Holiday curated with precision by TRAGUIN is expertly tailored to offer comfort, sisterhood, and wellness. Witness the breathtaking landscapes of secluded lagoons, discover the vibrant coral ecosystems through guided aquatic safaris, and capture unforgettable memories within our highly secure, handpicked hotels and premium stays across the islands.\n\n"
            "Travel Mode: Private Premium Marine Speedboat & Luxury Yacht Charters (All-Female Friendly Crews). Meal Plan: All-Inclusive Beachfront Gourmet Dining (Detox Drinks, High Tea, Seafood BBQs). Route Plan: Agatti Airport → Private Speedboat to Bangaram Island → Thinnakara Atoll Cruise → Agatti Departure. This premium TRAGUIN Lakshadweep Package features completely pre-cleared travel permits, priority bag management, local female guest assistance, and premium beach-yoga setups.\n\n"
            "Lakshadweep stands as India's safest and most visually spectacular coral archipelago. Bangaram Island Atoll is an uninhabited, serene sanctuary offering premium villas directly on white sands. Thinnakara Sandbanks is a slice of tropical perfection and a world-class Instagram location. Top Tourist Places in Lakshadweep include the coral lagoons of Bangaram, the historical village paths of Agatti, and the turtle nesting reef zones. The Best Time to Visit Lakshadweep is the smooth, blue-sky period from October to May."
        ),
        seo_title="LK-007 | Ladies Island Escape | TRAGUIN",
        seo_description="Premium 05 Nights / 06 Days Lakshadweep women-only package (LK-007 / TG-LK-FEM-007): Bangaram snorkel safari, Thinnakara yacht picnic, bioluminescent safari, and 2-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Private speedboat to Bangaram Haven with sun-lounger mocktail social under coconut trees", 1),
            _ih("Private snorkel safari with certified female dive instructor at Bangaram Inner Lagoon Reefs", 2),
            _ih("Luxury yacht to Thinnakara with sisterhood picnic on white sands and group drone portraits", 3),
            _ih("Glass-bottom kayaking and magical bioluminescent safari with private sunset bonfire", 4),
            _ih("Agatti cultural trail with hand-loom centers, female artisans, and farewell island dinner", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Agatti – Private Speedboat to Bangaram Haven",
                (
                    "Your ultimate tropical island adventure takes flight with an awe-inspiring aerial overview of coral rings before landing at Agatti Airport. Your specialized TRAGUIN female guest coordinator welcomes you warmly at the gate. Step aboard a private high-speed boat charter slicing through mirror-smooth teal waters directly to the pristine Bangaram Island Resort. Check into your premium beachfront villa, feel the powder-white sand under your feet, and unwind with an exclusive beachfront reception."
                ),
                [
                    "Sightseeing Included: Agatti Marine Lagoon Transit, Bangaram Beach Walk",
                    "Evening Experience: Sun-lounger mocktail social with curated appetizers under the coconut trees.",
                    "Overnight Stay: Bangaram Island (Premium Beachfront Cottage)",
                    "Meals Included: Lunch & Evening Gourmet Dinner",
                ],
            ),
            _day(
                2,
                "Private Snorkel Safari – Exploring Sea Turtles & Coral Gardens",
                (
                    "Wake up early to the soothing ocean breeze for a sunrise beach meditation session. Following a nutritious premium breakfast, TRAGUIN Experts lead you out on an exclusive private boat safari tailored for the group. Alongside a certified female dive instructor, enjoy an immersive experience snorkeling into crystal-clear shallows to spot colorful clownfish, graceful sea turtles, and majestic coral reefs. Spend your afternoon relaxing at leisure."
                ),
                [
                    "Sightseeing Included: Bangaram Inner Lagoon Reefs, Turtle Observation Zone",
                    "Optional Activities: Professional introductory Scuba Diving or guided sea-walking experiences.",
                    "Overnight Stay: Bangaram Island",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                3,
                "Luxury Yacht to Thinnakara – Sisterhood Picnic on White Sands",
                (
                    "Indulge in a late morning breakfast buffet. Today, step on board a private luxury yacht cruise heading to the neighboring island of Thinnakara. This uninhabited island is yours to explore. Stroll along the endless white sandbanks extending out into the blue ocean, capturing breathtaking landscapes. Enjoy a specially prepared gourmet picnic lunch on the sandbar arranged exclusively for your group, complete with beach-side canopy seating."
                ),
                [
                    "Sightseeing Included: Thinnakara Island Atoll, Extruded Sandbar Formations",
                    "Photography Points: Coordinated group drone portraits on the isolated Thinnakara sandbar tip.",
                    "Overnight Stay: Bangaram Island Resort Base",
                    "Meals Included: Breakfast, Luxury Picnic Lunch & Seafood Beach BBQ",
                ],
            ),
            _day(
                4,
                "Glass-Bottom Kayaking & Magical Bioluminescent Safari",
                (
                    "Enjoy a relaxed breakfast by the water. The day focuses on fun water sports customized for your comfort. Try your hand at paddleboarding or slide gracefully over the lagoon in premium transparent glass-bottom kayaks. After a spectacular island sunset and a fine dinner, head out after dark with your dedicated naturalists to see the incredible bioluminescent plankton glowing like starlight beneath the dark waves."
                ),
                [
                    "Sightseeing Included: Coral Lagoon Kayaking, Phosphorescent Ocean Sightseeing",
                    "Exclusive Experiences: Private sunset bonfire accompanied by stargazing and local stories.",
                    "Overnight Stay: Bangaram Island Resort",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                5,
                "Agatti Cultural Trail – Local Handicrafts & Seafront Dinner",
                (
                    "Board your private speedboat charter back to Agatti Island for a delightful local experience. Explore the island in an open-air luxury cart, visiting traditional hand-loom centers, meeting local female artisans, and strolling through coconut groves. Spend your afternoon finding authentic shell crafts before gathering for a final evening dinner right on the edge of the water, featuring authentic island recipes."
                ),
                [
                    "Sightseeing Included: Agatti Handicraft Quarter, Southern Palm Groves, Lighthouse Point",
                    "Food Suggestion: Traditional spiced lagoon fish baked delicately in fresh banana leaves.",
                    "Overnight Stay: Agatti Island (Luxury Lagoon-View Resort Suite)",
                    "Meals Included: Breakfast, Lunch & Farewell Island Dinner",
                ],
            ),
            _day(
                6,
                "Farewell Island Escape – Return with Forever Bonded Memories",
                (
                    "Savor your final breakfast as the tropical sun illuminates the lagoon. Pack your resort wear and your collection of authentic local souvenirs as your private chauffeur drives you comfortably to Agatti Airport. Your exceptional Lakshadweep Ladies Island Escape concludes here. You depart with a rejuvenated spirit, new friendships, and priceless memories crafted meticulously by TRAGUIN."
                ),
                [
                    "Meals Included: Breakfast",
                    "Assistance: Luggage handling, trolley support, and permit validation check by our airport executive.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Bangaram Island Resort",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Luxury",
                "Premium Air-Conditioned Beachfront Villa",
                "All-Inclusive Beachfront Gourmet Dining",
                5,
                1,
                description="OPTION 01 – LUXURY: Bangaram Island Resort (Premium Air-Conditioned Beachfront Villa)",
            ),
            _hotel(
                "Agatti Island Lagoon-View Suites / Thinnakara Premium Cottage Base",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Premium",
                "Lagoon-View Suites / Premium Cottage Base",
                "All-Inclusive Beachfront Gourmet Dining",
                5,
                2,
                description="OPTION 02 – PREMIUM: Agatti Island Lagoon-View Suites / Thinnakara Premium Cottage Base",
            ),
        ],
        inclusions=[
            _inc_included("Premium beachside villa stays with high-security privacy layouts.", 1),
            _inc_included("All daily multi-course meals, beach BBQs, and healthy mocktails.", 2),
            _inc_included("Pre-cleared Lakshadweep Administrative Entry Permits & Green fees.", 3),
            _inc_included("Private speedboat and luxury yacht transfers for all islands.", 4),
            _inc_included("Complimentary guided snorkeling safari including top-tier safety vests.", 5),
            _inc_included("Dedicated local female coordinator and 24/7 TRAGUIN Support.", 6),
            _inc_excluded("Commercial flight airfare to and from Agatti Airport.", 7),
            _inc_excluded("Optional heavy advanced scuba certification courses.", 8),
            _inc_excluded("Personal boutique shopping, laundry charges, or individual tips.", 9),
            _inc_excluded("Personal travel insurance coverage.", 10),
        ],
    )
    return package, itinerary


def build_lk_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "LK-008"
    tour_code = "TG-LK-FAM-008"
    title = "Coral Paradise Family Tour"
    duration = "05 Nights / 06 Days"
    slug = "lk-008-coral-paradise-family-tour"
    itin_slug = "lk-008-coral-paradise-family-tour-itinerary"
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
            _ph("State / Country: Lakshadweep, India | Category: Coral Paradise Family Tour", 2),
            _ph("Destinations Covered: Agatti Island • Kadmat Island • Kalpeni Atoll", 3),
            _ph("Ideal for: Families, Multi-generation Groups, Nature Enthusiasts", 4),
            _ph("Best season: October to May", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Premium Speedboat & Luxury Yacht Charters for inter-island transits", 7),
            _ph("Meal Plan: All-Inclusive Meal Structures (Daily Breakfast, Lunch, High-tea, and Dinner)", 8),
            _ph("Route Map: Agatti Arrival → Kadmat Coral Paradise → Kalpeni Atoll Excursion → Agatti Culture → Departure", 9),
            _ph("TRAGUIN Signature Experience: A fully customized sandbank picnic setup tailored around families, featuring specialized children's play kits and elderly comfort seats", 10),
            _ph("Shopping & Local Experiences: Agatti Handloom Markets — organic cold-pressed virgin coconut oil, hand-crafted sea-shell souvenirs, dried fish condiments; Famous Instagram Spots — wooden pier walkway at Kadmat Island and sandspits of Kalpeni Atoll during sunrise", 11),
            _ph("Important Notes: Flights and permits must be confirmed 60-90 days in advance; damaging coral reefs or removing seashells is strictly illegal; mobile connectivity primary to BSNL and Airtel networks", 12),
        ],
        moods=["Family", "Nature", "Coral Paradise"],
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
        tagline="TRAGUIN Premium Lakshadweep Family Tour Package • Agatti Island • Kadmat Island Coral Paradise • Kalpeni Atoll Explorations • 05 Nights / 06 Days",
        overview=(
            "Welcome to an unforgettable family voyage across India's premier coral archipelago. This exclusive Lakshadweep Family Tour meticulously curated by TRAGUIN Experts combines rich maritime adventures, vibrant reef discovery, and pure multi-generational relaxation. Discover the breathtaking landscapes of deep emerald lagoons, delight in shared glass-bottom boat excursions, and harvest unforgettable memories inside handpicked hotels offering elite beachside comfort and specialized personalized assistance for travelers of all ages.\n\n"
            "The stunning coral atolls of Lakshadweep serve as the ultimate safe haven for a mesmerizing Luxury Lakshadweep Holiday or an exciting Lakshadweep Family Tour. Kadmat Island Coral Paradise is celebrated for its long stretches of sandy beaches and shallow coral reefs, perfect for safe family snorkeling. Kalpeni Atoll is distinctive for its massive storm-defying coral debris banks and highly popular family picnic sandbars. Top Tourist Places in Lakshadweep include Agatti's picturesque palm-fringed coastlines, Kadmat's diving lagoons, and the pristine islets of Kalpeni. The Best Time to Visit Lakshadweep is the serene winter and sunny spring months between October and May."
        ),
        seo_title="LK-008 | Coral Paradise Family Tour | TRAGUIN",
        seo_description="Premium 05 Nights / 06 Days Lakshadweep family package (LK-008 / TG-LK-FAM-008): Kadmat coral paradise, Kalpeni sandbank picnic, glass-bottom reef exploration, and 2-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Agatti island welcome with private beachside family party and southern cape sunset view", 1),
            _ih("Private luxury cruise to Kadmat Coral Paradise with inter-island marine cruise", 2),
            _ih("Family snorkel safari and glass-bottom reef exploration at Kadmat Marine Lagoon", 3),
            _ih("Kalpeni Atoll excursion with exclusive sandbank picnic and beachfront family BBQ", 4),
            _ih("Agatti cultural tour with island anthropology museum, craft markets, and farewell gala dinner", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Agatti – Island Welcome & Chauffeur Transfer",
                (
                    "Your family holiday begins with a dramatic bird's-eye view of beautiful coral rings as you descend into Agatti Airport. Your professional TRAGUIN family concierge greets you right at the terminal gates and assists with baggage handling. Relax as a premium eco-cart brings you directly to your handpicked luxury beachfront resort. Spend a leisurely afternoon walking on the white sand, exploring coconut groves, and soaking in your first breathtaking landscapes at sunset."
                ),
                [
                    "Sightseeing Included: Agatti Beach Trail, Southern Cape Sunset View",
                    "Evening Experience: A private beachside family welcome party featuring fresh coconut mocktails and traditional folk songs.",
                    "Overnight Stay: Agatti Island (Premium Beachfront Suite)",
                    "Meals Included: Lunch & Gourmet Dinner",
                ],
            ),
            _day(
                2,
                "Private Luxury Cruise to Kadmat Coral Paradise Island",
                (
                    "Enjoy an early multi-course family breakfast. Today, step on board a high-speed private speedboat charter managed by TRAGUIN to sail northwest toward the legendary Kadmat Island. Marvel at flying fish leaping alongside your boat during the journey. Upon checking into your premium lagoon-facing villas, spend your afternoon discovering the beautiful shallow reef flats, capturing brilliant family photographs against the turquoise horizon."
                ),
                [
                    "Sightseeing Included: Inter-island Marine Cruise, Kadmat North Point Reef",
                    "Photography Points: The scenic wooden jetty at Kadmat stretching far out into the clear ocean waters.",
                    "Overnight Stay: Kadmat Island (Premium Air-Conditioned Beach Villa)",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                3,
                "Family Snorkel Safari & Glass-Bottom Reef Exploration",
                (
                    "An incredible day of shared marine exploration awaits. Board a large, comfortable family-sized glass-bottom boat to watch the vivid coral fields below without getting wet—an exceptional option for elders and young children. Later, the family can join our certified TRAGUIN Experts for a safely guided lagoon snorkeling safari. Swim hand-in-hand over gentle sand flats filled with harmless sea turtles and colorful reef fish."
                ),
                [
                    "Sightseeing Included: Kadmat Marine Lagoon, Giant Turtle Nesting Shoals",
                    "Optional Activities: Beginner family scuba diving tryouts or guided ocean kayaking sessions.",
                    "Overnight Stay: Kadmat Island",
                    "Meals Included: Breakfast, Lunch & Island Dinner",
                ],
            ),
            _day(
                4,
                "Kalpeni Atoll Excursion – Exclusive Sandbank Picnic",
                (
                    "Savor a fresh tropical breakfast before boarding our private luxury yacht charter to the scenic Kalpeni Atoll, famous for its unique geological coral banks. Enjoy an exclusive family picnic on an uninhabited sandbar setup entirely by your private crew. Relax under shaded luxury tents while the kids splash in the safe, knee-deep lagoon waters. Return to the main resort for a magnificent family evening under the stars."
                ),
                [
                    "Sightseeing Included: Kalpeni Coral Debris Bank, Tilakkam Islet Lagoons",
                    "Exclusive Experience: Private, catered beachfront family BBQ with a personal chef cooking fresh catches.",
                    "Overnight Stay: Agatti Premium Lagoon Base",
                    "Meals Included: Breakfast, Luxury Picnic Lunch & Beach BBQ Dinner",
                ],
            ),
            _day(
                5,
                "Agatti Island Tour – Local Culture & Souvenir Tracks",
                (
                    "Dedicate your day to an immersive cultural tour of Agatti Island. Explore local coir-weaving craft houses, visit the small Island Museum containing ancient ship models, and learn about the local way of living. Spend your late afternoon buying beautiful local souvenirs at the craft stalls. Celebrate your final evening of this Premium Lakshadweep Experience with a grand celebratory dinner overlooking the vast, quiet ocean."
                ),
                [
                    "Sightseeing Included: Island Anthropology Museum, Local Craft Markets, Eastern Jetty Point",
                    "Food Suggestion: Traditional local coconut-rice dessert wrapped in sweet banana leaves.",
                    "Overnight Stay: Agatti Island",
                    "Meals Included: Breakfast, Lunch & Farewell Special Gala Dinner",
                ],
            ),
            _day(
                6,
                "Farewell Lakshadweep – Return Home with Unforgettable Memories",
                (
                    "Indulge in your final morning breakfast at your beachfront resort while the warm morning sun gleams over the water. Pack your sea gear and beautifully gathered coral memories as our private chauffeur transfers your family smoothly to the Agatti Airport terminal gates. Your magical Lakshadweep Honeymoon Package and premium family holiday concludes here, leaving you with eternal bonds and memories crafted by TRAGUIN."
                ),
                [
                    "Meals Included: Breakfast",
                    "Assistance: Complete airport permit clearance check and luggage tracking support by our local staff.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Kadmat Island Beach Resort / Agatti Premium Villas",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Luxury",
                "Executive Beachfront Villas",
                "All-Inclusive Meal Structures",
                5,
                1,
                description="OPTION 01 – LUXURY: Kadmat Island Beach Resort / Agatti Premium Villas (Executive Beachfront Villas)",
            ),
            _hotel(
                "Sea Shells Luxury Partner Hub / Coral Paradise Resort",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Premium",
                "Family Lagoon Suites",
                "All-Inclusive Meal Structures",
                5,
                2,
                description="OPTION 02 – PREMIUM: Sea Shells Luxury Partner Hub / Coral Paradise Resort (Family Lagoon Suites)",
            ),
        ],
        inclusions=[
            _inc_included("Handpicked hotel accommodations directly on prime family beaches.", 1),
            _inc_included("All-inclusive meal structures (Daily Breakfast, Lunch, High-tea, and Dinner).", 2),
            _inc_included("Complimentary pre-processed Lakshadweep Entry Permits & Eco-Taxes.", 3),
            _inc_included("Private speedboat and luxury yacht charters for inter-island transits.", 4),
            _inc_included("Complimentary glass-bottom boat reef excursion for the whole family.", 5),
            _inc_included("Consistent 24/7 localized emergency and hospitality TRAGUIN Support.", 6),
            _inc_excluded("Commercial flight tickets to and from Agatti Airport.", 7),
            _inc_excluded("Professional deep-sea scuba certification courses.", 8),
            _inc_excluded("Personal laundry, souvenir expenses, or alcohol billing.", 9),
            _inc_excluded("National travel or medical insurance coverage policies.", 10),
        ],
    )
    return package, itinerary


def build_lk_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "LK-009"
    tour_code = "TG-LK-PREM-009"
    title = "Premium Luxury Holiday"
    duration = "06 Nights / 07 Days"
    slug = "lk-009-premium-luxury-holiday"
    itin_slug = "lk-009-premium-luxury-holiday-itinerary"
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
            _ph("State / Country: Lakshadweep, India | Category: Premium Lakshadweep Luxury Escape", 2),
            _ph("Destinations Covered: Agatti Island • Bangaram Atoll • Thinnakara • Kalpitti Coral Island", 3),
            _ph("Ideal for: Discerning Couples, Honeymooners, Luxury Families", 4),
            _ph("Best season: October to May", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Dedicated Luxury Speedboats & Chartered Island Transits", 7),
            _ph("Meal Plan: All-Inclusive Royal Island Gastronomy (Breakfast, Lunch, High Tea, and Beachfront BBQs)", 8),
            _ph("Route Map: Agatti Airport Arrival → Bangaram Lagoon Resort → Thinnakara Island Excursion → Kalpitti Cruise → Agatti Departure", 9),
            _ph("TRAGUIN Signature Experience: A private, fully catered sandbank lunch setup far away from other travelers, complete with a dedicated server", 10),
            _ph("Shopping & Local Experiences: Agatti Local Markets — cold-pressed virgin coconut oil, handcrafted shell decor items, traditionally dried tuna sticks (Maas Min); Instagram Spots — sweeping palm bent over the water at Agatti's southern coastline and uninhabited sandbanks of Kalpitti at twilight", 11),
            _ph("Important Notes: Flights and permits should be finalized 60–90 days ahead; touching, breaking, or removing coral and shells is strictly prohibited; network connectivity is minimal (BSNL/Airtel function best)", 12),
        ],
        moods=["Luxury", "Honeymoon", "Premium"],
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
        tagline="TRAGUIN Premium Lakshadweep Luxury Holiday • Agatti Island • Bangaram Island • Thinnakara • Private Island Expeditions • 06 Nights / 07 Days",
        overview=(
            "Welcome to an extraordinary paradise on earth, where absolute seclusion meets untamed tropical ocean splendor. This highly refined Premium Lakshadweep Experience meticulously crafted by TRAGUIN is an exclusive gateway to endless sapphire horizons, curated experiences, and absolute comfort. Immerse yourself in the breathtaking landscapes of deep-sea lagoons, indulge in private luxury speedboat charters, and gather unforgettable memories in premium stays across handpicked hotels designed to deliver the pinnacle of island hospitality.\n\n"
            "Travel Mode: Private Dedicated Luxury Speedboats & Chartered Island Transits. Meal Plan: All-Inclusive Royal Island Gastronomy (Breakfast, Lunch, High Tea, and Beachfront BBQs). Route Plan: Agatti Airport Arrival → Bangaram Lagoon Resort → Thinnakara Island Excursion → Kalpitti Cruise → Agatti Departure. This ultra-premium holiday by TRAGUIN features completely pre-vetted entry documentation, priority government e-permits, premium luggage handling, and dedicated private marine naturalists.\n\n"
            "The pristine sands of Lakshadweep host India's most brilliant multi-tonal ocean reefs. Bangaram Island Atoll is a stunning, uninhabited tropical sanctuary enveloped by a sprawling 10-kilometer lagoon area. Thinnakara Sandspits are teardrop sand islands extending directly into shallow marine beds. Top Tourist Places in Lakshadweep include the coral fields of Agatti, Bangaram's marine conservation centers, and Kalpitti's sunset cliffs. The Best Time to Visit Lakshadweep is the sunny and calm months from October until May."
        ),
        seo_title="LK-009 | Premium Luxury Holiday | TRAGUIN",
        seo_description="Premium 06 Nights / 07 Days Lakshadweep luxury package (LK-009 / TG-LK-PREM-009): Bangaram coral safari, Thinnakara lagoon picnic, Kalpitti sunset cliffs, and 2-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Private premium speedboat charter from Agatti to Bangaram Royal Resort with welcome cocktail event", 1),
            _ih("Private coral safari and sunken shipwreck snorkeling with marine naturalist at Bangaram Outer Reef", 2),
            _ih("Luxury speed-yacht excursion to Thinnakara with exclusive lagoon picnic and beachfront BBQ dinner", 3),
            _ih("Deep lagoon glass kayaking and stunning bioluminescent evening with professional photographer session", 4),
            _ih("Kalpitti Island uninhabited sunset cliffs excursion with premium high-tea picnic on sandbanks", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Agatti – Speedboat Chop to Bangaram Royal Resort",
                (
                    "Your luxury escape begins as you fly over surreal rings of sand and turquoise waters before landing at the iconic Agatti Airport runway. Your private TRAGUIN island manager greets you with iced coconut water and manages your baggage transfers seamlessly. Board an exclusive private premium speedboat charter, cutting across deep channels directly to the pristine shores of Bangaram Island Resort. Check into your premium air-conditioned beachfront villa, step onto powder-soft sand, and look out over a spectacular golden sunset."
                ),
                [
                    "Sightseeing Included: Agatti Deep Sea Channel Transit, Bangaram Lagoon Walk",
                    "Evening Experience: A private beachside welcome cocktail event with acoustic island music beneath towering palms.",
                    "Overnight Stay: Bangaram Island (Premium Beachfront Villa)",
                    "Meals Included: Lunch & Gourmet Dinner",
                ],
            ),
            _day(
                2,
                "Private Coral Safari & Sunken Shipwreck Snorkeling",
                (
                    "Wake to the rhythmic sounds of gentle waves and enjoy a gourmet breakfast. Today, a private marine naturalist arranged by TRAGUIN Experts guides you on a custom-chartered reef safari. Venture out to exclusive, undisturbed coral gardens where you will snorkel alongside vibrant sea turtles, harmless reef sharks, and multi-colored schools of parrotfish. Spend your afternoon relaxing under your private beach pergola."
                ),
                [
                    "Sightseeing Included: Bangaram Outer Reef Formations, Black Coral Coral Fields",
                    "Optional Activities: Certified PADI introductory scuba diving sessions over deep wall drop-offs.",
                    "Overnight Stay: Bangaram Island Resort",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                3,
                "Excursion to Thinnakara Island & Exclusive Lagoon Picnic",
                (
                    "Relish a tropical breakfast before boarding a luxury speed-yacht over to the sister island of Thinnakara. This uninhabited paradise offers breathtaking landscapes of raw marine wilderness. Walk hand-in-hand along a private sandspit extending a kilometer out into the open sea. Your crew sets up an exclusive, shaded beach canopy with chilled refreshments, offering an immersive experience of absolute privacy."
                ),
                [
                    "Sightseeing Included: Thinnakara Island Perimeter, Sandbar Tip Walks",
                    "Photography Points: Striking low-tide drone-style vistas from the Thinnakara sandbar.",
                    "Overnight Stay: Bangaram Island Resort / Tented Luxury Base",
                    "Meals Included: Breakfast, Curated Island Picnic Lunch, Beachfront BBQ Dinner",
                ],
            ),
            _day(
                4,
                "Deep Lagoon Glass Kayaking & Stunning Bioluminescent Evening",
                (
                    "Following a refreshing morning meal, indulge in customized watersports. Glide across the glass-like ocean inside premium transparent glass-bottom kayaks, viewing the busy coral life beneath you without getting wet. As darkness blankets the atoll, your private guide leads you to hidden lagoon pockets to witness the incredible bioluminescent plankton glowing like stardust in the water."
                ),
                [
                    "Sightseeing Included: Bangaram Interior Lagoons, Bioluminescent Night Bay Tour",
                    "Exclusive Experiences: Private drone and portrait session with a dedicated professional vacation photographer.",
                    "Overnight Stay: Bangaram Island Resort",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                5,
                "Returning to Agatti – Coconut Groves & Heritage Discovery",
                (
                    "After breakfast, board your private speedboat charter back to Agatti Island for a delightful change of scenery. Check into your luxury beach resort suite and discover the local heritage in an open-air luxury cart. Travel past traditional coir-weaving communities, historical mosques, and thick coconut plantations. In the evening, relax with an exclusive culinary showcase featuring authentic island seafood recipes."
                ),
                [
                    "Sightseeing Included: Agatti Culture Museum, Eastern Marine Jetty, Coconut Grove Trails",
                    "Food Suggestion: Local lobster or fresh fish curry simmered gently with fresh organic coconut milk.",
                    "Overnight Stay: Agatti Island (Luxury Beachfront Resort Suite)",
                    "Meals Included: Breakfast, Lunch & Island Specialty Dinner",
                ],
            ),
            _day(
                6,
                "Excursion to Kalpitti Island – Uninhabited Sunset Cliffs",
                (
                    "Dedicate your morning to absolute relaxation on Agatti's southern beaches. In the afternoon, embark on an exclusive short boat cruise to the tiny, uninhabited coral island of Kalpitti. Renowned for its unique jagged coral rock formations and breathtaking landscapes, Kalpitti is the absolute best sunset viewpoint in the archipelago. Share a premium high-tea basket as the sun sinks below the endless blue horizon."
                ),
                [
                    "Sightseeing Included: Kalpitti Coral Island, Southern Reef Flats",
                    "Evening Experience: A premium high-tea picnic basket prepared and served on the quiet Kalpitti sandbanks.",
                    "Overnight Stay: Agatti Island Luxury Suite",
                    "Meals Included: Breakfast, Lunch & Farewell Grand Buffet Dinner",
                ],
            ),
            _day(
                7,
                "Farewell Lakshadweep – Departure with Timeless Ocean Blessings",
                (
                    "Savor your final morning breakfast as the sun lights up your resort terrace. Pack your beach attire and unique handcrafted shell souvenirs before your driver transfers you comfortably to the Agatti Airport terminal gates. Your unforgettable Lakshadweep Family Tour and premium island journey concludes here. Depart with divine peace and everlasting memories designed exclusively by TRAGUIN."
                ),
                [
                    "Meals Included: Breakfast",
                    "Assistance: Direct airport luggage escort and fast-track permit verification support from our resident staff.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Bangaram Island Resort",
                "Lakshadweep Stay (6 Nights)",
                "06 Nights",
                "Ultra Luxury",
                "Premium Air-Conditioned Deluxe Beach Villa",
                "All-Inclusive Royal Island Gastronomy",
                5,
                1,
                description="OPTION 01 – ULTRA LUXURY: Bangaram Island Resort (Premium Air-Conditioned Deluxe Beach Villa)",
            ),
            _hotel(
                "Agatti Island Beach Resort / Thinnakara Luxury Lagoon Cottages",
                "Lakshadweep Stay (6 Nights)",
                "06 Nights",
                "Luxury",
                "Executive Beach Suites",
                "All-Inclusive Royal Island Gastronomy",
                5,
                2,
                description="OPTION 02 – LUXURY: Agatti Island Beach Resort / Thinnakara Luxury Lagoon Cottages (Executive Beach Suites)",
            ),
        ],
        inclusions=[
            _inc_included("Luxury air-conditioned villa stays situated directly on white sand beaches.", 1),
            _inc_included("All-inclusive gourmet meal plans (Daily Breakfast, Lunch, High-Tea, and Dinner).", 2),
            _inc_included("Pre-arranged government e-permits, heritage fees, and clearance paper management.", 3),
            _inc_included("Private speedboat and speed-yacht charters for all island inter-connections.", 4),
            _inc_included("Complimentary guided snorkeling safari and transparent glass-kayak rentals.", 5),
            _inc_included("Constant 24/7 on-call localized operational and hospitality TRAGUIN Support.", 6),
            _inc_excluded("Commercial airline or flight ticketing to/from Agatti Airport.", 7),
            _inc_excluded("Optional PADI deep-sea scuba certifications or night-diving fees.", 8),
            _inc_excluded("Personal laundry, phone tabs, or specialized shopping items.", 9),
            _inc_excluded("Personal travel insurance coverage or medical evacuation policies.", 10),
        ],
    )
    return package, itinerary


def build_lk_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "LK-010"
    tour_code = "TG-LK-FAM-010"
    title = "Complete Family Tour Package"
    duration = "07 Nights / 08 Days"
    slug = "lk-010-complete-family-tour-package"
    itin_slug = "lk-010-complete-family-tour-package-itinerary"
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
            _ph("State / Country: Lakshadweep, India | Category: Complete Lakshadweep Family Expedition", 2),
            _ph("Destinations Covered: Agatti Island • Bangaram Island • Thinnakara • Kalpeni • Kavaratti", 3),
            _ph("Ideal for: Families, Multi-generational Groups, Ocean Devotees", 4),
            _ph("Best season: October to May", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private Premium Chauffeur/Escort with Luxury Speedboats & Charter Yacht Fleet", 7),
            _ph("Meal Plan: All-Inclusive Royal Island Plan (Buffet Breakfast, Premium Lunches, Sunset High-Tea, Specialized Theme Dinners)", 8),
            _ph("Route Map: Agatti Airport → Bangaram Island Paradise → Thinnakara Day Excursion → Kavaratti Capital Hub → Kalpeni Lagoon Exploration → Agatti Departure", 9),
            _ph("TRAGUIN Signature Experience: Private family sandbank setup with custom seating, refreshments, and a personal butler, completely isolated from other travelers", 10),
            _ph("Shopping & Local Experiences: Agatti Local Co-operatives — authentic virgin coconut oils, handmade shell art souvenirs, spiced dried tuna delicacies; Famous Cafes — cozy seaside shacks serving sweet coconut-water pudding and fresh local fish fry", 11),
            _ph("Important Notes: Flights and permits must be secured 60–90 days in advance; damaging or taking coral or shells is strictly prohibited; minimal network coverage (BSNL/Airtel work best)", 12),
        ],
        moods=["Family", "Multi-Island", "Luxury"],
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
        tagline="TRAGUIN Complete Lakshadweep Family Tour Package • The Ultimate Multi-Island Coral Realm Odyssey • 07 Nights / 08 Days",
        overview=(
            "Welcome to India's most dazzling emerald archipelago. This comprehensive, ultra-luxurious Lakshadweep Family Tour meticulously blueprinted by TRAGUIN unlocks the entire coral kingdom. Specifically optimized for family bonding across generations, this itinerary blends premium stays, breathtaking landscapes, and exclusive experiences. Cherish immersive experiences across multiple vibrant islands, enjoy private yacht passages, and secure unforgettable memories in handpicked hotels curated by our travel masters.\n\n"
            "Travel Setup: Private Premium Chauffeur/Escort with Luxury Speedboats & Charter Yacht Fleet. Meal Plan: All-Inclusive Royal Island Plan (Buffet Breakfast, Premium Lunches, Sunset High-Tea, Specialized Theme Dinners). Route Plan: Agatti Airport → Bangaram Island Paradise → Thinnakara Day Excursion → Kavaratti Capital Hub → Kalpeni Lagoon Exploration → Agatti Departure. This expansive TRAGUIN Lakshadweep Package manages all mandatory local permit clearances, inter-island cruise manifest approvals, and specialized family water-safety captains prior to arrival.\n\n"
            "Planning a comprehensive multi-island cruise makes this the definitive Best Lakshadweep Tour Package or a quintessential Lakshadweep Family Tour. Kavaratti Island is the administrative heart, famous for its magnificent sea-glass mosques, marine aquariums, and calm inner lagoons. Kalpeni Atoll is renowned for its massive storm-tossed coral banks and exceptionally massive shallow lagoon walking floors. Most Searched Experiences include multi-generational family snorkeling, sandspit volleyball, glass-bottom reef viewing, and authentic local folk performances. The Best Time to Visit Lakshadweep is the smooth, sunny months from October to May."
        ),
        seo_title="LK-010 | Complete Family Tour Package | TRAGUIN",
        seo_description="Premium 07 Nights / 08 Days Lakshadweep family package (LK-010 / TG-LK-FAM-010): Bangaram, Thinnakara, Kavaratti, Kalpeni, bioluminescent lagoon, and 2-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Private boat crossing from Agatti to Bangaram Atoll with customized welcome amenities", 1),
            _ih("Family reef snorkel safari and marine turtle tracking at Bangaram Inner Coral Reef Garden", 2),
            _ih("Thinnakara expedition with private lagoon sunset and family beach bonfire under starry sky", 3),
            _ih("Chartered yacht to Kavaratti with marine aquarium, Ujra Mosque, and glass-bottom boat cruise", 4),
            _ih("Kalpeni storm reefs with Parichakali dance, Agatti bioluminescent lagoon, and grand farewell dinner", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Agatti – Private Boat Crossing to Bangaram Atoll",
                (
                    "Fly into Agatti International Airport, capturing birds-eye views of deep blue rings below. Upon clearing documentation, your senior TRAGUIN coordinator escorts your family onto a high-speed private boat charter. Zip through sparkling turquoise waves directly to the paradise shores of Bangaram Island Resort. Check into adjacent oceanfront villas, feel the fine white sand beneath your feet, and unwind with an immersive beachside family sunset."
                ),
                [
                    "Sightseeing Included: Agatti-Bangaram Sea Route Cruise, Bangaram North Beach",
                    "Welcome Amenities: Customized refreshing coconut water mocktails, chilled towels, and a family travel portrait token.",
                    "Overnight Stay: Bangaram Island (Premium Beachside Family Villas)",
                    "Meals Included: Lunch & Welcoming Buffet Dinner",
                ],
            ),
            _day(
                2,
                "Family Reef Snorkel Safari & Marine Turtle Tracking",
                (
                    "Wake up early to glorious breathtaking landscapes. After a premium fresh breakfast, your family boards our custom-equipped private boat for an extensive reef excursion. Guided by specialized water-safety instructors, explore safe, shallow inner reef lines to swim alongside ancient green sea turtles and glowing schools of reef fish. The afternoon is dedicated to family leisure, beach-combing, and relaxation under shaded palms."
                ),
                [
                    "Sightseeing Included: Bangaram Inner Coral Reef Garden, Turtle Shallow Sanctuary",
                    "Optional Activities: Beginner scuba dives or deep-sea family fishing challenges with professional gear.",
                    "Overnight Stay: Bangaram Island Resort",
                    "Meals Included: Breakfast, Island Lunch & Dinner",
                ],
            ),
            _day(
                3,
                "Expedition to Thinnakara Island & Private Lagoon Sunset",
                (
                    "Enjoy a tropical breakfast before sailing on a private luxury yacht charter to the uninhabited sister isle of Thinnakara. The island offers endless white sandbanks extending into the bright ocean—a popular Instagram location. Children can enjoy building sandcastles on the soft shores, while adults relax under private gazebos. In the evening, witness a spectacular sunset over the water before returning to your island base."
                ),
                [
                    "Sightseeing Included: Thinnakara Pristine Island, Sandbar Walkways",
                    "Evening Experience: Private family beach bonfire under a starry sky with specialized local chefs serving grilled treats.",
                    "Overnight Stay: Bangaram Island Base",
                    "Meals Included: Breakfast, Picnic Lunch & Beachfront BBQ Dinner",
                ],
            ),
            _day(
                4,
                "Chartered Yacht to Kavaratti – The Capital Atoll Experience",
                (
                    "Savor an early morning breakfast before check-out. Board your luxury private cruise to Kavaratti Island, the vibrant administrative hub. Transfer directly to your premium stay. Spend your afternoon discovering iconic attractions, including the Kavaratti Marine Aquarium to marvel at indigenous oceanic wonders, followed by a visit to the beautifully carved drift-wood structures of Ujra Mosque."
                ),
                [
                    "Sightseeing Included: Kavaratti Marine Museum, Historic Ujra Mosque, Capital Lagoon Walk",
                    "Photography Points: Vibrant family photos on Kavaratti's sweeping jetty during late afternoon.",
                    "Overnight Stay: Kavaratti Island (Premium Waterfront Accommodations)",
                    "Meals Included: Breakfast, Regional Lunch & Dinner",
                ],
            ),
            _day(
                5,
                "Glass-Bottom Boat Cruise & Premium Water Sports Odyssey",
                (
                    "Enjoy a relaxed morning. Today features an array of curated family activities. Board an exclusive private glass-bottom boat, allowing grandmothers and children alike to peer into deep reef life without getting wet. Afterwards, teens and adults can enjoy guided sea kayaking, stand-up paddleboarding, or jet-skiing across the protected lagoon waters."
                ),
                [
                    "Sightseeing Included: Kavaratti Outer Coral Reef Line via Glass-Bottom Cruiser",
                    "Exclusive Experiences: Private family windsurfing orientation or sea-kayak races arranged by our local guides.",
                    "Overnight Stay: Kavaratti Island",
                    "Meals Included: Breakfast, Lunch & Traditional Coastal Dinner",
                ],
            ),
            _day(
                6,
                "Excursion to Kalpeni – Storm Reefs & Traditional Folk Arts",
                (
                    "Board an early morning speed-yacht charter to the striking island of Kalpeni, famous for its unique geological storm-banks and islet chains like Tilakkam and Pitti. Walk through shallow waters at low tide, then enjoy an exclusive cultural performance of the traditional Parichakali dance, organized privately for your family."
                ),
                [
                    "Sightseeing Included: Kalpeni Lagoon, Storm Coral Banks, Tilakkam Islet",
                    "Food Suggestion: Freshly baked local coconut rice cakes served alongside aromatic herbal teas.",
                    "Overnight Stay: Kavaratti / Agatti Premium Family Suites",
                    "Meals Included: Breakfast, Kalpeni Village Lunch & Dinner",
                ],
            ),
            _day(
                7,
                "Agatti Land Trails, Bioluminescent Evening Reflections",
                (
                    "Return comfortably to Agatti Island for your final full day of island exploration. Tour the island in open-air golf carts, visiting traditional coir industries and walking through towering coconut plantations. After dark, your guides will take you to special lagoon pockets to witness magical bioluminescent plankton glowing like stardust in the dark waters."
                ),
                [
                    "Sightseeing Included: Agatti Culture Trail, Coir Production Center, Bioluminescent Lagoon Safari",
                    "Evening Experience: A celebratory farewell dinner on the beach to toast your incredible family vacation.",
                    "Overnight Stay: Agatti Island (Luxury Lagoon Suite)",
                    "Meals Included: Breakfast, Lunch & Grand Farewell Dinner",
                ],
            ),
            _day(
                8,
                "Farewell Lakshadweep – Departure with Forever Memories",
                (
                    "Savor a final delicious tropical breakfast at the resort. Enjoy a last walk along the sunny shores before your private vehicle brings you comfortably to Agatti Airport terminal gates. Your comprehensive, ultra-luxury Luxury Lakshadweep Holiday concludes here, leaving your family with beautiful blessings and unforgettable memories to cherish for generations, proudly crafted by TRAGUIN."
                ),
                [
                    "Meals Included: Breakfast",
                    "Assistance: Airport checking hand-holding and baggage manifest verification by our standby executive.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Bangaram Island Resort + Kavaratti Sea-View Elite",
                "Multi-Island Stay (7 Nights)",
                "07 Nights",
                "Ultra Luxury",
                "Premium Interconnected Family Suites",
                "All-Inclusive Royal Island Plan",
                5,
                1,
                description="OPTION 01 – ULTRA LUXURY: Bangaram Island Resort + Kavaratti Sea-View Elite (Premium Interconnected Family Suites)",
            ),
            _hotel(
                "Agatti Beach Pearl Resorts / Coral Reef Homestay Elite",
                "Multi-Island Stay (7 Nights)",
                "07 Nights",
                "Luxury",
                "Luxury Tented Family Villas",
                "All-Inclusive Royal Island Plan",
                5,
                2,
                description="OPTION 02 – LUXURY: Agatti Beach Pearl Resorts / Coral Reef Homestay Elite (Luxury Tented Family Villas)",
            ),
        ],
        inclusions=[
            _inc_included("Handpicked family villa stays across premium island bases.", 1),
            _inc_included("All-inclusive elite dining plans (Breakfast, Lunch, High-tea, Dinners).", 2),
            _inc_included("Complimentary pre-arranged Lakshadweep Entry Permits for the entire family.", 3),
            _inc_included("Private speed-boat and yacht charters for inter-island crossings.", 4),
            _inc_included("Complimentary family reef snorkeling safari including premium gear rentals.", 5),
            _inc_included("Private family glass-bottom boat charter.", 6),
            _inc_included("Dedicated 24/7 localized operational and safety TRAGUIN Support.", 7),
            _inc_excluded("Commercial flight tickets to/from Agatti Airport.", 8),
            _inc_excluded("Professional deep-sea scuba certification courses.", 9),
            _inc_excluded("Personal laundry expenditures, heavy shopping, or tips.", 10),
            _inc_excluded("Any personal travel insurance or medical coverage plans.", 11),
        ],
    )
    return package, itinerary


LAKSHADWEEP_LK_BUILDERS = [
    build_lk_001,
    build_lk_002,
    build_lk_003,
    build_lk_004,
    build_lk_005,
    build_lk_006,
    build_lk_007,
    build_lk_008,
    build_lk_009,
    build_lk_010,
]
