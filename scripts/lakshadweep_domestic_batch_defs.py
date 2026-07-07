"""Builder functions for LD-011 through LD-015 Lakshadweep domestic packages."""

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


def build_ld_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "LD-011"
    tour_code = "TRAGUIN-LD-011"
    title = "Bangaram Romance Luxury Holiday"
    duration = "05 Nights / 06 Days"
    slug = "ld-011-bangaram-romance-luxury-holiday"
    itin_slug = "ld-011-bangaram-romance-luxury-holiday-itinerary"
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
            _ph("State / Country: Lakshadweep, India | Category: Honeymoon / Premium Luxury", 2),
            _ph("Destinations Covered: Agatti • Bangaram Island • Thinnakara Exploration", 3),
            _ph("Ideal for: Couples, Honeymooners, Luxury Seekers", 4),
            _ph("Best season: October to May", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private FIT Luxury Honeymoon Itinerary", 7),
            _ph("Transfers: Private AC luxury vehicles & premium speedboats", 8),
            _ph("Meal Plan: Curated meals as specified per day itinerary option", 9),
            _ph("Route Map: Agatti Arrival → Bangaram Island → Thinnakara Excursion → Agatti Transition → Departure", 10),
            _ph("TRAGUIN Signature Experience: Handpicked hotels, seamless VIP greeting protocols, customized culinary menus tailored to dietary preferences, and localized support mechanisms ensuring worry-free travel throughout your vacation", 11),
            _ph("Shopping & Local Experiences: Lakshadweep — authentic coconut-shell artifacts, pure hand-pressed virgin coconut oil, and delicious local fish-pickle delicacies directly from native beach artisans", 12),
            _ph("Important Notes: Lakshadweep entry permits require a minimum of 15–20 working days for processing by TRAGUIN experts; island speedboats depend strictly on clear weather guidelines for premium safety standards", 13),
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
        tagline="TRAGUIN Premium Lakshadweep Tour Package • Bangaram Romance Luxury Holiday • 05 Nights / 06 Days",
        overview=(
            "Welcome to an unforgettable romantic escapade curated exclusively by TRAGUIN. Lakshadweep, a pristine archipelago of breathtaking landscapes, silver-white sands, and kaleidoscopic coral reefs, offers the ultimate sanctuary for your dream honeymoon. Escape to the secluded paradise of Bangaram Island, where turquoise waters meet endless skies, delivering immersive experiences and handpicked luxury that linger forever in your memories. Experience the best time to visit Lakshadweep with a meticulously designed premium travel layout.\n\n"
            "This bespoke Luxury Lakshadweep Holiday is tailored as a private FIT itinerary ensuring complete privacy and premium comfort. Your journey includes seamless speed boat transfers, a premium full meal plan, and curated beachside activities managed by TRAGUIN destination experts. Enjoy a handpicked premium beach bungalow stay surrounded by scenic beauty and iconic marine attractions.\n\n"
            "Why Visit Lakshadweep for your Honeymoon? Lakshadweep stands as India's premier exotic island destination. Famous attractions like the Bangaram lagoon and Thinnakara marine life offer the most searched experiences for high-end travelers. It is globally acclaimed as the best honeymoon destination due to its absolute privacy, restricted entry ensuring low tourist crowds, and popular Instagram locations featuring crystal-clear water swings and sandbanks. From adrenaline-pumping water sports like scuba diving and snorkeling to absolute leisure under swaying palms, TRAGUIN Lakshadweep Packages combine the rich local culture with unparalleled premium indulgence."
        ),
        seo_title="LD-011 | Bangaram Romance Luxury Holiday | TRAGUIN",
        seo_description="Premium 05 Nights / 06 Days Lakshadweep honeymoon package (LD-011 / TRAGUIN-LD-011): Agatti, Bangaram Island, Thinnakara exploration, candlelight dinner, and 4-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Scenic speedboat transfer from Agatti to exclusive Bangaram Island Resort", 1),
            _ih("Guided lagoon snorkeling with exotic marine turtles and vibrant coral beds", 2),
            _ih("Private Thinnakara Island excursion with shipwreck sightseeing and stargazing", 3),
            _ih("TRAGUIN Signature Exclusive Candlelight Dinner under the stars with custom menu options", 4),
            _ih("Agatti island sightseeing with local village tour, museum visit, and coconut grove high-tea", 5),
        ],
        days=[
            _day(
                1,
                "Arrival at Agatti & Speedboat to Bangaram Island",
                (
                    "Arrive at the scenic Agatti Airport, where you will experience a warm premium welcome by our TRAGUIN island coordinator. Witness a stunning aerial view of the turquoise coral lagoons. Transfer directly to the jetty for an exhilarating speedboat ride to the exclusive Bangaram Island Resort."
                ),
                [
                    "Sightseeing Included: Scenic speedboat transfer, check-in relaxation at premium beach bungalow.",
                    "Evening Experience: Private sunset stroll along the endless white sandbar with complimentary welcome amenities.",
                    "Overnight Stay: Bangaram Island Beach Resort (Premium Stay)",
                    "Meals Included: Lunch & Dinner",
                ],
            ),
            _day(
                2,
                "Immersive Lagoon Experiences & Water Adventures",
                (
                    "Awake to the soothing sound of gentle waves. Today is dedicated to exploring the top tourist places in Lakshadweep's marine world. Indulge in premium water sports or sit back and absorb the breathtaking scenic beauty of the completely enclosed lagoon environment."
                ),
                [
                    "Sightseeing Included: Guided lagoon snorkeling to view exotic marine turtles and vibrant coral beds.",
                    "Optional Activities: Certified Scuba Diving, Kayaking, and Glass-bottom boat rides.",
                    "Evening Experience: Romantic beachside setup with traditional island refreshments.",
                    "Overnight Stay: Bangaram Island Beach Resort",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                3,
                "Exclusive Thinnakara Island Excursion",
                (
                    "Embark on a private boat excursion to the tiny, uninhabited paradise of Thinnakara Island. Known as one of the most famous Instagram locations, this teardrop-shaped isle offers complete isolation and pristine natural beauty for unforgettable memories."
                ),
                [
                    "Sightseeing Included: Thinnakara Island cruise, shipwreck sightseeing points.",
                    "Evening Experience: Stargazing on the completely dark beach away from all civilization.",
                    "Overnight Stay: Bangaram Island Beach Resort",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                4,
                "Leisure & Private Romantic Candlelight Dinner",
                (
                    "A completely open day curated for personalized comfort. Rejuvenate with standard island wellness treatments or walk hand-in-hand along the continuous coral reef walkways. Tonight features a signature highlight prepared carefully by the TRAGUIN team."
                ),
                [
                    "Sightseeing Included: Self-guided island exploration, photography points.",
                    "Evening Experience: TRAGUIN Signature Exclusive Candlelight Dinner under the stars with custom menu options.",
                    "Overnight Stay: Bangaram Island Beach Resort",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                5,
                "Coral Reef Walk & Agatti Transition",
                (
                    "Bid farewell to the serene shores of Bangaram as you take the morning speedboat back to Agatti Island. Check into your premium villa and discover local island culture, craft markets, and unique traditional lifestyle highlights."
                ),
                [
                    "Sightseeing Included: Agatti island sightseeing, local village tour, museum visit.",
                    "Evening Experience: Coconut grove high-tea experience with local culinary delights.",
                    "Overnight Stay: Premium Agatti Beach Villa",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                6,
                "Departure with Forever Memories",
                (
                    "Enjoy your final breakfast looking out at the vast Indian Ocean. Pack your bags full of lifelong memories of this premium Lakshadweep experience. Transfer directly to Agatti Airport for your return flight home."
                ),
                [
                    "Meals Included: Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Agatti Standard Beach Villa",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Deluxe",
                "Standard Beach Villa",
                "Breakfast & Dinner",
                4,
                1,
                description="OPTION 01 – DELUXE: Agatti Standard Beach Villa | Breakfast & Dinner",
            ),
            _hotel(
                "Agatti Premium Ocean Suite",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Premium",
                "Premium Ocean Suite",
                "Breakfast & Dinner",
                5,
                2,
                description="OPTION 02 – PREMIUM: Agatti Premium Ocean Suite | Breakfast & Dinner",
            ),
            _hotel(
                "Bangaram Island Beach Resort",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Luxury",
                "Beach Resort",
                "Full Meals (All Included)",
                5,
                3,
                description="OPTION 03 – LUXURY: Bangaram Island Beach Resort | Full Meals (All Included)",
            ),
            _hotel(
                "Bangaram Premium Diamond Villa",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Ultra Luxury",
                "Premium Diamond Villa",
                "Curated Premium Dine-around",
                5,
                4,
                description="OPTION 04 – ULTRA LUXURY: Bangaram Premium Diamond Villa | Curated Premium Dine-around",
            ),
        ],
        inclusions=[
            _inc_included("Premium Accommodation: Handpicked senior-friendly & honeymoon-ready luxury stays.", 1),
            _inc_included("Curated Meals: All meals as specified per day itinerary option.", 2),
            _inc_included("Luxury Transfers: Private AC luxury vehicles & premium speedboats.", 3),
            _inc_included("Sightseeing: Guided entries and VIP step-free accesses everywhere.", 4),
            _inc_included("TRAGUIN Support: 24/7 localized on-ground assistance helpline.", 5),
            _inc_included("Welcome Amenities: Personalized honeymoon fruit baskets and refreshments.", 6),
            _inc_excluded("Domestic or International Airfare flight tickets.", 7),
            _inc_excluded("Mandatory travel insurance policies.", 8),
            _inc_excluded("Personal expenses like laundry, mini-bars, telephone calls.", 9),
            _inc_excluded("Optional water sports charges or camera entry fees.", 10),
            _inc_excluded("Anything not specifically mentioned in the inclusions list.", 11),
        ],
    )
    return package, itinerary


def build_ld_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "LD-012"
    tour_code = "TRAGUIN-LD-012"
    title = "Agatti • Bangaram • Thinnakara Island Discovery"
    duration = "05 Nights / 06 Days"
    slug = "ld-012-agatti-bangaram-thinnakara-island-discovery"
    itin_slug = "ld-012-agatti-bangaram-thinnakara-island-discovery-itinerary"
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
            _ph("State / Country: Lakshadweep, India | Category: Family Tour / Island Discovery", 2),
            _ph("Destinations Covered: Agatti Island • Bangaram Island Paradise • Thinnakara Lagoon", 3),
            _ph("Ideal for: Families, Multi-generational Groups, Leisure Travelers", 4),
            _ph("Best season: October to May (Best Time to Visit Lakshadweep)", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private, fully assisted FIT Family Journey", 7),
            _ph("Transfers: High-speed luxury boat transfers across islands", 8),
            _ph("Meal Plan: All-inclusive full meal plan tailored to satisfy all age groups", 9),
            _ph("Route Map: Agatti Arrival → Bangaram Island → Thinnakara Lagoon → Agatti Cultural Tour → Departure", 10),
            _ph("TRAGUIN Signature Experience: Personalized assistance at every junction, handpicked hotels evaluated rigorously for multi-generational safety, customized culinary adaptations for children and seniors, and exclusive recommendations for hidden swimming reefs", 11),
            _ph("Shopping & Local Experiences: Agatti island markets — handcrafted coconut shell items, premium pure virgin coconut oil, locally processed dry fish pickles, and handmade seashell decorative frames crafted by native island women", 12),
            _ph("Important Notes: Entry to Lakshadweep is highly restricted — all traveler documentation must be submitted to TRAGUIN at least 20 days prior to departure; boat transfers depend strictly on local coast guard weather clearances; early reservations recommended due to limited luxury inventory on Bangaram Island", 13),
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
        tagline="Best Lakshadweep Family Tour Package • Agatti • Bangaram • Thinnakara Island Discovery • 05 Nights / 06 Days",
        overview=(
            "Welcome to an unforgettable tropical retreat thoughtfully curated by TRAGUIN for your family. The pristine archipelago of Lakshadweep unfolds a canvas of breathtaking landscapes, unmatched scenic beauty, and vibrant turquoise lagoons that promise perfect bonding moments. This Luxury Lakshadweep Holiday brings together handpicked hotels, safety-first luxury marine transfers, and immersive experiences designed to bridge generations. Let the sun-kissed coral sands and iconic attractions weave unforgettable memories for your loved ones.\n\n"
            "Our elite Lakshadweep Family Tour is meticulously planned as a private, fully assisted FIT journey ensuring complete comfort and unhurried luxury. From seamless airport arrival protocols to premium island-hopping speedboats, this trip incorporates an all-inclusive full meal plan tailored to satisfy all age groups. Discover the true charm of premium stays nestled comfortably inside the absolute jewel of the Indian Ocean, featuring signature touches from our specialized TRAGUIN destination managers.\n\n"
            "Why Visit Lakshadweep for a Family Vacation? Lakshadweep ranks as India's ultimate pristine island sanctuary. Free from commercial overcrowding, it offers an exceptionally safe, serene, and naturally therapeutic environment for parents, kids, and grandparents alike. The archipelago is globally celebrated for its most searched experiences, which include wading through shallow chest-deep crystal waters, spotting sea turtles in coral reefs, and exploring sandbars. The Top Tourist Places in Lakshadweep included in this package span the iconic deep-sea lagoons of Bangaram Island and the untouched scenery of Thinnakara Island. Popular Instagram locations—such as the water swings and traditional coconut groves—provide perfect spots for family portraits. From gentle glass-bottom boat sightseeing to interactive cultural exchanges, TRAGUIN Lakshadweep Packages deliver the premier luxury island getaway."
        ),
        seo_title="LD-012 | Agatti Bangaram Thinnakara Island Discovery | TRAGUIN",
        seo_description="Premium 05 Nights / 06 Days Lakshadweep family package (LD-012 / TRAGUIN-LD-012): Agatti, Bangaram Island, Thinnakara Lagoon, family beachside dinner, and 4-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Assisted Agatti arrival with luxury speedboat transfer to Bangaram Island Resort", 1),
            _ih("Family lagoon exploration with guided coral reef safari and non-swimmer marine interaction zone", 2),
            _ih("Exclusive day cruise to Thinnakara Island with shipwreck viewing and shallow sandbar walk", 3),
            _ih("Exclusive Private Family Beachside Dinner featuring specialized multi-cuisine family menus under the starlight", 4),
            _ih("Agatti native village cultural tour with museum, handloom, and craft demonstrations", 5),
        ],
        days=[
            _day(
                1,
                "Assisted Agatti Arrival & Luxury Speedboat to Bangaram",
                (
                    "Step off your aircraft at the iconic Agatti Airport runway, flanked by turquoise waters on both sides. Your family will enjoy a traditional premium welcome by a dedicated TRAGUIN island coordinate team. We handle your baggage seamlessly as you move to the jetty for an exclusive, highly comfortable speed vessel transfer to the magnificent Bangaram Island Resort."
                ),
                [
                    "Sightseeing Included: Inter-island blue water transfer, check-in hospitality rituals at your premium beach bungalow.",
                    "Evening Experience: A relaxing family walk along the powdery beach ridge to witness a majestic tropical sunset.",
                    "Overnight Stay: Bangaram Island Beach Resort (Premium Beachfront Cottage)",
                    "Meals Included: Lunch & Dinner",
                ],
            ),
            _day(
                2,
                "Family Lagoon Exploration & Snorkeling Safari",
                (
                    "Wake up to panoramic views of endless ocean blue. Today, your family dives deep into the heart of Lakshadweep Sightseeing. Our certified naturalists guide you through safe, shallow-water snorkeling activities directly from the beach, allowing even absolute beginners and children to marvel at colorful marine life and gentle sea turtles."
                ),
                [
                    "Sightseeing Included: Guided coral reef safari, non-swimmer marine interaction zone.",
                    "Optional Activities: Glass-bottom boat rides for elderly family members, introductory family scuba diving.",
                    "Evening Experience: Beach volleyball, sandcastle building sessions for kids, followed by fresh local coconut water refreshments.",
                    "Overnight Stay: Bangaram Island Beach Resort",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                3,
                "Exclusive Day Cruise to Thinnakara Island Paradise",
                (
                    "Board a private boat for an exclusive excursion to neighboring Thinnakara Island, a tiny uninhabited jewel of stunning scenic beauty. This island is surrounded by a massive, perfectly calm lagoon where children can paddle safely while parents relax under high-end shaded loungers curated by our team."
                ),
                [
                    "Sightseeing Included: Thinnakara Island discovery, shipwreck viewing point, shallow sandbar walk.",
                    "Photography Points: Continuous panoramic photo opportunities along the continuous white sand spits.",
                    "Evening Experience: High tea hosted right on the beach lagoon rim with family storytelling sessions.",
                    "Overnight Stay: Bangaram Island Beach Resort",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                4,
                "Leisure Day with Special TRAGUIN Family Dinner",
                (
                    "A completely flexible day designed for maximum relaxation and zero travel fatigue. Stroll through the lush inner pathways of the island, read a book under a canopy of palms, or enjoy personal watercraft sports. Tonight features a signature celebratory dinner event arranged uniquely for your family by TRAGUIN specialists."
                ),
                [
                    "Sightseeing Included: Self-paced nature walks, inner-atoll photography trails.",
                    "Evening Experience: Exclusive Private Family Beachside Dinner featuring specialized multi-cuisine family menus under the starlight.",
                    "Overnight Stay: Bangaram Island Beach Resort",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                5,
                "Return Boat to Agatti & Native Village Cultural Tour",
                (
                    "Bid farewell to the serene oasis of Bangaram as your luxury speedboat journeys back to Agatti Island. Check into your premium oceanside air-conditioned villa. Spend the afternoon taking an easy, informative tour of the local township to learn about the islanders' authentic lifestyle, unique coir-craft industries, and ancient maritime history."
                ),
                [
                    "Sightseeing Included: Agatti local village walk, museum culture tour, traditional handloom and craft demonstration.",
                    "Evening Experience: Farewell island high-tea paired with traditional snacks at an iconic local seaside overlook.",
                    "Overnight Stay: Premium Agatti Lagoon Villa",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                6,
                "Homebound Departure with Forever Memories",
                (
                    "Savor your last breakfast together while looking out at the turquoise waters. Collect your unique island souvenirs and pack a treasure trove of unforgettable memories from this Premium Lakshadweep Experience. Enjoy a seamless, short transfer directly to Agatti Airport for your onward flight home."
                ),
                [
                    "Meals Included: Premium Breakfast Buffet",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Bangaram Standard Beach Hut | Agatti Standard Ocean Stay",
                "Bangaram Island (4 Nights) / Agatti Island (1 Night)",
                "05 Nights",
                "Deluxe",
                "Standard Beach Hut / Standard Ocean Stay",
                "Breakfast & Dinner Plan",
                4,
                1,
                description="OPTION 01 – DELUXE: Bangaram Standard Beach Hut (4 Nights) | Agatti Standard Ocean Stay (1 Night) | Breakfast & Dinner Plan",
            ),
            _hotel(
                "Bangaram Executive Cottage | Agatti Island Premium Villa",
                "Bangaram Island (4 Nights) / Agatti Island (1 Night)",
                "05 Nights",
                "Premium",
                "Executive Cottage / Premium Villa",
                "Breakfast & Dinner Plan",
                5,
                2,
                description="OPTION 02 – PREMIUM: Bangaram Executive Cottage (4 Nights) | Agatti Island Premium Villa (1 Night) | Breakfast & Dinner Plan",
            ),
            _hotel(
                "Bangaram Premium Beach Bungalow | Agatti Premium Lagoon Suite",
                "Bangaram Island (4 Nights) / Agatti Island (1 Night)",
                "05 Nights",
                "Luxury",
                "Premium Beach Bungalow / Premium Lagoon Suite",
                "All-Inclusive Resort Dining",
                5,
                3,
                description="OPTION 03 – LUXURY: Bangaram Premium Beach Bungalow (4 Nights) | Agatti Premium Lagoon Suite (1 Night) | All-Inclusive Resort Dining",
            ),
            _hotel(
                "Bangaram Deluxe Diamond Sea Front Villa | Agatti Presidential Oceanfront Villa",
                "Bangaram Island (4 Nights) / Agatti Island (1 Night)",
                "05 Nights",
                "Ultra Luxury",
                "Deluxe Diamond Sea Front Villa / Presidential Oceanfront Villa",
                "TRAGUIN Private Chef Dining",
                5,
                4,
                description="OPTION 04 – ULTRA LUXURY: Bangaram Deluxe Diamond Sea Front Villa (4 Nights) | Agatti Presidential Oceanfront Villa (1 Night) | TRAGUIN Private Chef Dining",
            ),
        ],
        inclusions=[
            _inc_included("Luxury Accommodation: Handpicked family-friendly premium stays.", 1),
            _inc_included("Island Meals: Comprehensive gourmet breakfast, lunch, and dinner menus.", 2),
            _inc_included("Marine Transfers: High-speed luxury boat transfers across islands.", 3),
            _inc_included("Sightseeing: Guided group excursions to Thinnakara Island lagoons.", 4),
            _inc_included("TRAGUIN Support: Dedicated on-ground travel expert on standby 24/7.", 5),
            _inc_included("Welcome Kit: Traditional welcome mocktails and a premium fruit basket upon arrival.", 6),
            _inc_excluded("Mainland flights to and from Agatti Airport.", 7),
            _inc_excluded("Personal water sports (Scuba diving, Jet ski rental, Kayaking).", 8),
            _inc_excluded("Laundry, mini-bar expenses, and international telephone bills.", 9),
            _inc_excluded("Personal tips, portage services, and entry tickets for optional museums.", 10),
            _inc_excluded("Any item not explicitly detailed in the inclusions column.", 11),
        ],
    )
    return package, itinerary


def build_ld_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "LD-013"
    tour_code = "TRAGUIN-LD-013"
    title = "Bangaram Romance & Deep-Sea Marine Exploration"
    duration = "05 Nights / 06 Days"
    slug = "ld-013-bangaram-romance-deep-sea-marine-exploration"
    itin_slug = "ld-013-bangaram-romance-deep-sea-marine-exploration-itinerary"
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
            _ph("State / Country: Lakshadweep, India | Category: Adventure / Scuba Explorer", 2),
            _ph("Destinations Covered: Agatti • Bangaram Island • Lagoon Scuba Bases", 3),
            _ph("Ideal for: Adventure Enthusiasts, Divers, Luxury Thrill Seekers", 4),
            _ph("Best season: October to May", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Private FIT Scuba Explorer Itinerary", 7),
            _ph("Transfers: High-speed sea craft journeys and airport pick-ups", 8),
            _ph("Meal Plan: Daily dining menus as per chosen option matrix", 9),
            _ph("Route Map: Agatti Arrival → Bangaram Diving Hub → Deep Reef Dives → Thinnakara Shipwreck → Agatti Transition → Departure", 10),
            _ph("TRAGUIN Signature Experience: Exclusive experiences with verified dive masters, premium handpicked hotels, luxury transportation, and exclusive recommendations for the finest underwater photography locations", 11),
            _ph("Shopping & Local Experiences: Agatti fish co-operatives — premium dried tuna snacks, handicraft decorative items carved entirely out of fallen coconut husks, and pristine shell souvenirs from verified sustainable vendors", 12),
            _ph("Important Notes: Pre-clearance health forms are mandatory before diving bookings can be finalized; government island entry permits are organized fully by TRAGUIN operations staff; a minimum 24-hour surface interval is strictly maintained before your departure flight", 13),
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
        tagline="Best Lakshadweep Tour Package - Scuba Adventure • Bangaram Romance & Deep-Sea Marine Exploration • 05 Nights / 06 Days",
        overview=(
            "Welcome to a thrilling marine expedition curated exclusively by TRAGUIN. Lakshadweep, a mesmerizing paradise of breathtaking landscapes, untouched coral reefs, and vast turquoise lagoons, presents the ultimate backdrop for a high-end Scuba Explorer vacation. Immerse yourself in the world-class dive sites surrounding Bangaram Island, enjoying curated experiences, scenic beauty, and handpicked hotels that guarantee unforgettable memories beneath and above the waves. Experience a Premium Lakshadweep Experience tailored perfectly to your thirst for adventure.\n\n"
            "This bespoke Luxury Lakshadweep Holiday is specifically tailored for FIT travelers seeking deep-sea exploration combined with premium comfort. Your journey includes scheduled multi-tank dive excursions, professional dive master guidance, seamless private speed boat island connectivity, a full meal plan, and robust logistical coordination provided by TRAGUIN.\n\n"
            "Why Visit Lakshadweep for Scuba Diving? Renowned for having some of the clearest water visibility in the Indian Ocean, Lakshadweep stands out as the ultimate destination for marine life exploration. Iconic attractions such as the shallow reef slopes of Bangaram Lagoon and the deeper walls around Thinnakara offer highly searched experiences for professional and amateur divers alike. Apart from thrill-seeking aquatic sports, the pristine islands serve as popular Instagram locations with dramatic sandbanks and unique coastal features. Choosing the best time to visit Lakshadweep allows you to fully engage in Lakshadweep Sightseeing while discovering the top tourist places in Lakshadweep through signature TRAGUIN Lakshadweep Packages."
        ),
        seo_title="LD-013 | Bangaram Romance & Deep-Sea Marine Exploration | TRAGUIN",
        seo_description="Premium 05 Nights / 06 Days Lakshadweep scuba package (LD-013 / TRAGUIN-LD-013): lagoon check-dive, deep reef exploration, Thinnakara shipwreck dive, and 4-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Inter-island luxury speed boat transfer to Bangaram Island diving hub", 1),
            _ih("Lagoon scuba check-dive with marine turtle observation in protected calm waters", 2),
            _ih("Two open-water deep tank dive sessions around pristine drop-offs with barracudas, reef sharks, and manta rays", 3),
            _ih("Thinnakara shipwreck dive with drift exploration and glassfish photography points", 4),
            _ih("Watersports carnival with kayaking, windsurfing, and Agatti cultural highlights", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Agatti & Speedboat to Bangaram Island",
                (
                    "Your premium adventure begins as you arrive at the visually stunning Agatti Airport track. Witness a jaw-dropping panoramic view of the reef system. Meet our TRAGUIN island team member for an assisted transfer to the speed boat jetty, bound directly for the legendary diving hub of Bangaram Island."
                ),
                [
                    "Sightseeing Included: Inter-island luxury speed boat transfer, check-in at your beachfront bungalow.",
                    "Evening Experience: Sunset walk to the tip of Bangaram sandspit with standard welcome refreshments.",
                    "Overnight Stay: Bangaram Island Beach Resort (Premium Stay)",
                    "Meals Included: Lunch & Dinner",
                ],
            ),
            _day(
                2,
                "Lagoon Scuba Check-Dive & Coral Reef Survey",
                (
                    "Awake early to crisp ocean views. Head over to the premium dive facility for your gear-fitting session and safety presentation. Execute your initial check-dive in the protected calm waters of Bangaram Lagoon to adjust buoyancy and observe local stingrays."
                ),
                [
                    "Sightseeing Included: 1 Morning Dive session in the lagoon area, marine turtle observation.",
                    "Optional Activities: Evening night snorkeling session along the inner reef rim.",
                    "Evening Experience: Relaxed stargazing lounge setup right next to the dive operations desk.",
                    "Overnight Stay: Bangaram Island Beach Resort",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                3,
                "Deep Reef Exploration & Open-Ocean Wall Dives",
                (
                    "Prepare for advanced open-ocean excursions. Board our specialized dive vessel to reach pristine drop-offs where underwater columns sink deep into the blue. Encounter large schools of barracudas, reef sharks, and magnificent manta rays in their natural habitat."
                ),
                [
                    "Sightseeing Included: 2 Open-water deep tank dive sessions around specific iconic attractions.",
                    "Optional Activities: Deep-sea catch-and-release sport fishing experience.",
                    "Evening Experience: Beach bonfire interaction with local marine biologists and dive pros.",
                    "Overnight Stay: Bangaram Island Beach Resort",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                4,
                "Thinnakara Shipwreck Dive & Drift Exploration",
                (
                    "Embark on a unique boat journey toward Thinnakara Island to explore a historical shallow-water shipwreck site. The site is thriving with glassfish and massive brain coral formations, making it an epic highlight for photography points."
                ),
                [
                    "Sightseeing Included: 1 Shipwreck Dive, Thinnakara island pristine sandbank beach tour.",
                    "Photography Points: Clear-water shipwreck views and isolated sandbar horizons.",
                    "Overnight Stay: Bangaram Island Beach Resort",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                5,
                "Watersports Carnival & Transition Back to Agatti",
                (
                    "Conclude your underwater logbook entry and shift to surface thrills. Enjoy high-speed kayaking or windsurfing across the lagoon before taking the afternoon boat back to Agatti Island to witness native villages and cultural highlights."
                ),
                [
                    "Sightseeing Included: Agatti museum trail, sunset viewpoint tour, village walking paths.",
                    "Evening Experience: Local seafood tasting menu organized by the TRAGUIN operational crew.",
                    "Overnight Stay: Premium Agatti Beach Villa",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                6,
                "Departure with Unforgettable Memories",
                (
                    "Enjoy your final island-style breakfast looking out over the clear blue lagoon. Gather your scuba certifications, media files, and unforgettable memories. Transfer directly to Agatti Airport for your homeward flight path."
                ),
                [
                    "Meals Included: Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Agatti Standard Lagoon Villa",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Deluxe",
                "Standard Lagoon Villa",
                "Breakfast & Dinner Plan",
                4,
                1,
                description="OPTION 01 – DELUXE: Agatti Standard Lagoon Villa | Breakfast & Dinner Plan",
            ),
            _hotel(
                "Agatti Premium Beach Suite",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Premium",
                "Premium Beach Suite",
                "Breakfast & Dinner Plan",
                5,
                2,
                description="OPTION 02 – PREMIUM: Agatti Premium Beach Suite | Breakfast & Dinner Plan",
            ),
            _hotel(
                "Bangaram Island Beach Resort (Standard AC)",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Luxury",
                "Beach Resort (Standard AC)",
                "Full Island Meals Plan (All Included)",
                5,
                3,
                description="OPTION 03 – LUXURY: Bangaram Island Beach Resort (Standard AC) | Full Island Meals Plan (All Included)",
            ),
            _hotel(
                "Bangaram Premium Exec Beachfront Villa",
                "Lakshadweep Stay (5 Nights)",
                "05 Nights",
                "Ultra Luxury",
                "Premium Exec Beachfront Villa",
                "All Inclusive Premium Dining Plan",
                5,
                4,
                description="OPTION 04 – ULTRA LUXURY: Bangaram Premium Exec Beachfront Villa | All Inclusive Premium Dining Plan",
            ),
        ],
        inclusions=[
            _inc_included("Stays: Handpicked hotels and beach resorts across islands.", 1),
            _inc_included("Meals: Daily dining menus as per chosen option matrix.", 2),
            _inc_included("Transfers: High-speed sea craft journeys and airport pick-ups.", 3),
            _inc_included("Scuba Logistics: Pre-booked standard tank sets, weights, and dive boat slots.", 4),
            _inc_included("Support: 24/7 dedicated TRAGUIN on-ground destination help.", 5),
            _inc_included("Amenities: Premium water sports welcome kit and dry-bag kits.", 6),
            _inc_excluded("Flight airline tickets to/from Agatti Airport.", 7),
            _inc_excluded("Personal dive gear rentals (BCD, Regulators, Wetsuits).", 8),
            _inc_excluded("Tips, laundry, telephone charges, and beverages.", 9),
            _inc_excluded("Optional PADI/SSI training upgrade courses.", 10),
        ],
    )
    return package, itinerary


def build_ld_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "LD-014"
    tour_code = "TRAGUIN-LD-014"
    title = "Premium Island Retreat Escape"
    duration = "06 Nights / 07 Days"
    slug = "ld-014-premium-island-retreat-escape"
    itin_slug = "ld-014-premium-island-retreat-escape-itinerary"
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
            _ph("State / Country: Lakshadweep, India | Category: Luxury / Premium Island Retreat", 2),
            _ph("Destinations Covered: Agatti Island • Bangaram Island • Thinnakara • Kalpitti", 3),
            _ph("Ideal for: Couples, Families, Luxury Seekers", 4),
            _ph("Best season: October to May", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Premium private FIT escape", 7),
            _ph("Transfers: Speedboat rides and airport pickups", 8),
            _ph("Meal Plan: Multi-cuisine breakfast, lunch, and dinner options", 9),
            _ph("Route Map: Agatti Arrival → Bangaram Island → Thinnakara Retreat → Kalpitti Sunset Cruise → Agatti Culture → Departure", 10),
            _ph("TRAGUIN Signature Experience: Handpicked hotels, carefully planned marine outings, custom meals, and personalized on-ground assistance provided by our local experts", 11),
            _ph("Shopping & Local Experiences: Village stalls — hand-carved coconut shell ornaments, pure virgin coconut oils, and dried ocean fish delicacies prepared by islanders", 12),
            _ph("Important Notes: Official Lakshadweep entry permits need to be submitted 15–20 days before departure for processing by TRAGUIN coordinators; island boat schedules depend directly on daily ocean conditions; early booking recommended due to strictly limited room availability", 13),
        ],
        moods=["Luxury", "Island Retreat", "Romance"],
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
        tagline="Best Lakshadweep Tour Package • Premium Island Retreat Escape • 06 Nights / 07 Days",
        overview=(
            "Welcome to an extraordinary tropical getaway crafted by TRAGUIN. Lakshadweep invites you to dive into a world of breathtaking landscapes, white coral sands, and shimmering turquoise waters. Our Luxury Lakshadweep Holiday matches the natural scenic beauty of the islands with curated experiences and handpicked hotels. Prepare for unforgettable memories as you embark on this fully immersive premium travel experience designed around iconic attractions.\n\n"
            "This meticulously planned TRAGUIN Lakshadweep Package is arranged as a premium private FIT escape. It covers smooth island transitions via high-speed boats, a fully customized premium meal plan, and curated marine activities managed by dedicated destination specialists. Stay at handpicked luxury beachside bungalows and enjoy exclusive experiences designed to give you both adventure and tranquil isolation.\n\n"
            "Why Choose a Luxury Lakshadweep Holiday? As one of the world's most spectacular untouched marine ecosystems, Lakshadweep offers pristine marine privacy and strict environmental protections. The Best Time to Visit Lakshadweep falls between October and May when the skies are clear and the lagoons turn a bright turquoise. Top tourist places in Lakshadweep like the coral expanses of Bangaram and the calm settings of Thinnakara feature among the most searched experiences for global beach travelers. Whether planning a romantic Lakshadweep Honeymoon Package or a refreshing Lakshadweep Family Tour, guests flock to popular Instagram locations like the water swings of Bangaram and sandbars at Kalpitti. Enjoy world-class Lakshadweep sightseeing, deep-sea exploration, and traditional cultural interactions during this unparalleled Premium Lakshadweep Experience."
        ),
        seo_title="LD-014 | Premium Island Retreat Escape | TRAGUIN",
        seo_description="Premium 06 Nights / 07 Days Lakshadweep package (LD-014 / TRAGUIN-LD-014): Agatti, Bangaram, Thinnakara, Kalpitti sunset cruise, and 4-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Private speedboat from Agatti to remote Bangaram Island paradise", 1),
            _ih("Guided coral reef snorkeling tour with professional safety divers", 2),
            _ih("Exclusive retreat to uninhabited Thinnakara paradise islet with shipwreck viewpoints", 3),
            _ih("Kalpitti Island excursion with sunset cruise through calm outer waters", 4),
            _ih("Agatti cultural museum, fish curing units, handloom weaving centers, and farewell dinner", 5),
        ],
        days=[
            _day(
                1,
                "Welcome to Agatti & Speedboat to Bangaram",
                (
                    "Your premium travel experience starts the moment you land at Agatti Airport. Witness the stunning sight of endless coral rings from above. Enjoy an exclusive airport greeting by your dedicated TRAGUIN island coordinator before boarding a private speedboat heading toward the remote paradise of Bangaram Island."
                ),
                [
                    "Sightseeing Included: Agatti lagoon cruise, check-in assistance at the luxury beach property.",
                    "Evening Experience: A relaxing sunset walk on soft sandbars accompanied by special welcome amenities.",
                    "Overnight Stay: Bangaram Island Beach Resort (Premium Luxury Villa)",
                    "Meals Included: Lunch & Dinner",
                ],
            ),
            _day(
                2,
                "Exploring the Bangaram Lagoon & Reef Snorkeling",
                (
                    "Awaken to panoramic views of a tranquil turquoise ocean. Today features extensive Lakshadweep sightseeing across the expansive inner reef. Dip into warm waters to swim among sea turtles and bright coral fields, experiencing some of the finest marine life the region offers."
                ),
                [
                    "Sightseeing Included: Guided coral reef snorkeling tour with professional safety divers.",
                    "Optional Activities: PADI Scuba Diving lessons, sea-kayaking, and windsurfing sessions.",
                    "Evening Experience: Island-style high tea paired with fresh local culinary creations.",
                    "Overnight Stay: Bangaram Island Beach Resort",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                3,
                "Exclusive Retreat to Thinnakara Paradise Islet",
                (
                    "Board a private vessel for a curated day trip to uninhabited Thinnakara Island. Walk along untouched powdery beaches and discover a teardrop-shaped islet. This location is celebrated as a highly popular Instagram location due to its solitary coconut groves and exceptionally clear shallow lagoons."
                ),
                [
                    "Sightseeing Included: Thinnakara beachfront exploration, historic deep-lagoon shipwreck viewpoints.",
                    "Evening Experience: Relax with a sunset mocktail served on a private beach setup.",
                    "Overnight Stay: Bangaram Island Beach Resort",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                4,
                "Leisure Day with Private Signature Dinner",
                (
                    "A completely open day designed to let you enjoy the island at your own pace. Walk across natural sand bridges at low tide, read beneath a shady palm, or try standard wellness treatments at the resort. The evening concludes with a signature highlight carefully planned by the TRAGUIN team."
                ),
                [
                    "Sightseeing Included: Self-guided beach nature trails, beach photography spots.",
                    "Evening Experience: A curated romantic beachfront dinner featuring fine multi-cuisine dishes under the stars.",
                    "Overnight Stay: Bangaram Island Beach Resort",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                5,
                "Return to Agatti & Kalpitti Sunset Cruise",
                (
                    "Take a morning speedboat transfer back to Agatti Island and check into your beachside accommodation. In the afternoon, head out on an exclusive boat cruise to Kalpitti Island, a location well-known for offering beautiful panoramic sunset views."
                ),
                [
                    "Sightseeing Included: Kalpitti Island excursion, local village heritage walk.",
                    "Evening Experience: Sunset cruise through calm outer waters with great photography opportunities.",
                    "Overnight Stay: Premium Agatti Lagoon Villa",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                6,
                "Local Culture, Coconut Groves & Souvenir Tracking",
                (
                    "Spend a quiet day uncovering local island culture. Visit traditional handicraft centers, see how coir is made, and explore quiet local markets. Collect unique souvenirs while experiencing the authentic lifestyle of the island's residents."
                ),
                [
                    "Sightseeing Included: Agatti Cultural Museum, local fish curing units, handloom weaving centers.",
                    "Evening Experience: A special farewell dinner arranged by your resort hosts to celebrate your journey.",
                    "Overnight Stay: Premium Agatti Lagoon Villa",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                7,
                "Farewell Lakshadweep",
                (
                    "Enjoy your final breakfast while taking in a last look at the wide ocean. Pack your bags carrying unforgettable memories of this premium travel experience. Take a direct luxury transfer to Agatti Airport for your flight back home."
                ),
                [
                    "Meals Included: Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Bangaram Standard Cabin | Agatti Beach Homestay",
                "Bangaram (4 Nights) / Agatti (2 Nights)",
                "06 Nights",
                "Deluxe",
                "Standard Cabin / Beach Homestay",
                "Breakfast & Dinner",
                4,
                1,
                description="OPTION 01 – DELUXE: Bangaram Standard Cabin (4 Nights) | Agatti Beach Homestay (2 Nights) | Breakfast & Dinner",
            ),
            _hotel(
                "Bangaram Deluxe Cottage | Agatti Coral Premium Inn",
                "Bangaram (4 Nights) / Agatti (2 Nights)",
                "06 Nights",
                "Premium",
                "Deluxe Cottage / Coral Premium Inn",
                "Breakfast & Dinner",
                5,
                2,
                description="OPTION 02 – PREMIUM: Bangaram Deluxe Cottage (4 Nights) | Agatti Coral Premium Inn (2 Nights) | Breakfast & Dinner",
            ),
            _hotel(
                "Bangaram Island Beach Resort | Premium Agatti Lagoon Villa",
                "Bangaram (4 Nights) / Agatti (2 Nights)",
                "06 Nights",
                "Luxury",
                "Beach Resort / Premium Lagoon Villa",
                "Full Meals (All Included)",
                5,
                3,
                description="OPTION 03 – LUXURY: Bangaram Island Beach Resort (4 Nights) | Premium Agatti Lagoon Villa (2 Nights) | Full Meals (All Included)",
            ),
            _hotel(
                "Bangaram Executive Suite | Agatti Diamond Ocean Front Villa",
                "Bangaram (4 Nights) / Agatti (2 Nights)",
                "06 Nights",
                "Ultra Luxury",
                "Executive Suite / Diamond Ocean Front Villa",
                "Curated Premium Dine-around",
                5,
                4,
                description="OPTION 04 – ULTRA LUXURY: Bangaram Executive Suite (4 Nights) | Agatti Diamond Ocean Front Villa (2 Nights) | Curated Premium Dine-around",
            ),
        ],
        inclusions=[
            _inc_included("Luxury Lodging: Handpicked accommodations selected for comfort and location.", 1),
            _inc_included("Curated Meals: Multi-cuisine breakfast, lunch, and dinner options.", 2),
            _inc_included("Island Transfers: Speedboat rides and airport pickups.", 3),
            _inc_included("Sightseeing: Guided water excursions and entry clearances.", 4),
            _inc_included("TRAGUIN Support: On-ground assistance throughout your vacation.", 5),
            _inc_included("Welcome Perks: Fresh juices and seasonal fruit baskets on arrival.", 6),
            _inc_excluded("Airfare or flight tickets to and from Agatti.", 7),
            _inc_excluded("Personal expenses like laundry or phone calls.", 8),
            _inc_excluded("Optional scuba diving courses and water sports rentals.", 9),
            _inc_excluded("Compulsory individual travel insurance policies.", 10),
        ],
    )
    return package, itinerary


def build_ld_015(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "LD-015"
    tour_code = "TRAGUIN-LD-015"
    title = "Lakshadweep Grand Tour — Premium Family Experience"
    duration = "07 Nights / 08 Days"
    slug = "ld-015-lakshadweep-grand-tour-premium-family-experience"
    itin_slug = "ld-015-lakshadweep-grand-tour-premium-family-experience-itinerary"
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
            _ph("State / Country: Lakshadweep, India | Category: Luxury Family Vacation", 2),
            _ph("Destinations Covered: Agatti • Bangaram Island • Thinnakara • Kalpetti Island", 3),
            _ph("Ideal for: Families, Multi-Generational Groups, Leisure Travelers", 4),
            _ph("Best season: October to May (Best Time to Visit Lakshadweep)", 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph("Travel Format: Elite 8-day FIT Premium Family Itinerary", 7),
            _ph("Transfers: High-speed boats and air-conditioned island vehicles", 8),
            _ph("Meal Plan: Daily meals matching your selected hotel tier", 9),
            _ph("Route Map: Agatti Arrival → Bangaram Island → Thinnakara → Kalpetti Reefs → Agatti Culture → Farewell Dinner → Departure", 10),
            _ph("TRAGUIN Signature Experience: Smooth transfers with no long wait times at the docks, VIP entry points, handpicked premium hotels, private luxury transportation, and personalized assistance for a seamless world-class holiday", 11),
            _ph("Shopping & Local Experiences: Agatti cooperative markets — hand-carved coconut shell lamps, premium virgin coconut oils, dried fish delicacies, and exquisite seashell jewelry pieces handcrafted by native artisans", 12),
            _ph("Important Notes: Lakshadweep entry permits are strictly limited — submit family identity proofs 25 days before departure; inter-island speedboats permit up to 20kg of baggage per guest; speedboat transfers depend entirely on coastal water conditions", 13),
        ],
        moods=["Family", "Luxury", "Multi-Generational"],
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
        tagline="Best Lakshadweep Family Tour Package • Lakshadweep Grand Tour — Premium Family Experience • 07 Nights / 08 Days",
        overview=(
            "Welcome to an extraordinary tropical journey meticulously customized by TRAGUIN. Lakshadweep invites your family to immerse yourselves in a world of breathtaking landscapes, where white powder sands wrap gently around crystal-clear lagoon waters. This Luxury Lakshadweep Holiday is architected specifically to present curated experiences for every generation. From thrilling marine encounters for the youngsters to tranquil seaside relaxation for elders, your family will forge unforgettable memories amidst unparalleled scenic beauty. Discover the magic of iconic attractions and exclusive handpicked hotels on this magnificent premium island escape.\n\n"
            "This elite 8-day FIT itinerary represents the definitive Premium Lakshadweep Experience. Carefully planned to balance active coral sightseeing with extensive island relaxation, your family will travel seamlessly with private speedboats, stay at top-tier beachfront villas, and enjoy comprehensive gourmet meal plans. Every element is supervised closely by dedicated TRAGUIN island logistical experts to guarantee hassle-free operations from arrival to departure.\n\n"
            "Why Choose Lakshadweep for a Family Vacation? As a premium eco-tourism boundary, Lakshadweep offers pristine marine safety and isolated coral islands that are completely family-friendly. It stands as a top choice for a customized Lakshadweep Family Tour because it avoids dense commercial crowds, ensuring deep natural preservation. The most searched experiences center around the vibrant shallow reefs of the Bangaram lagoon, which boast famous swimming channels and popular Instagram locations like the natural palm-fringed sandbars. Whether your focus is culture, shopping for coral artifacts, or tracking rich marine wildlife, our specialized TRAGUIN Lakshadweep Packages deliver comprehensive access to the Top Tourist Places in Lakshadweep."
        ),
        seo_title="LD-015 | Lakshadweep Grand Tour Premium Family Experience | TRAGUIN",
        seo_description="Premium 07 Nights / 08 Days Lakshadweep family package (LD-015 / TRAGUIN-LD-015): Agatti, Bangaram, Thinnakara, Kalpetti reefs, deep-sea fishing BBQ, and 4-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Private speedboat transition from Agatti to exclusive Bangaram Island paradise", 1),
            _ih("Family lagoon snorkeling with guided private boat safari and turtle point snorkeling", 2),
            _ih("Excursion to uninhabited Thinnakara Island with deep-water shipwreck viewing site", 3),
            _ih("Deep-sea fishing expedition with premium family beachside barbecue and musical performances", 4),
            _ih("Kalpetti coral reef walks, Agatti cultural experience, and exclusive TRAGUIN farewell dinner", 5),
        ],
        days=[
            _day(
                1,
                "Arrival at Agatti & Private Transition to Bangaram Island",
                (
                    "Your family vacation launches beautifully as your flight glides over the deep turquoise lagoons into Agatti Airport. Step off the aircraft into a seamless, elite welcome arranged by your dedicated TRAGUIN vacation representative. We take charge of your luggage while your family is guided comfortably to the boarding jetty for a premium private speedboat transfer over the open ocean to the exclusive paradise of Bangaram Island."
                ),
                [
                    "Sightseeing Included: Inter-island ocean transit, aerial lagoon photography vistas.",
                    "Evening Experience: A warm family beach gathering at sunset with complimentary signature island drinks.",
                    "Overnight Stay: Handpicked Beach Bungalow at Bangaram Island Resort.",
                    "Meals Included: Lunch & Dinner",
                ],
            ),
            _day(
                2,
                "Family Lagoon Snorkeling & Exclusive Underwater Safari",
                (
                    "Awake to a gorgeous morning breakfast looking directly over calm coastal waters. Today, your family enjoys a fully guided private boat safari into the shallow inner barrier reefs. Trained marine naturalists ensure that children and elders alike can securely view spectacular coral formations and swim alongside friendly sea turtles in their natural habitat."
                ),
                [
                    "Sightseeing Included: Inner lagoon coral exploration, turtle point snorkeling.",
                    "Optional Activities: Introduction to Scuba Diving for family members, Glass-bottom boat cruises.",
                    "Evening Experience: Relaxing stroll down the island's pristine western point to witness the luminous sunset.",
                    "Overnight Stay: Bangaram Island Resort.",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                3,
                "Excursion to Uninhabited Thinnakara Island",
                (
                    "Board our premium charter boat for a short journey to the completely uninhabited islet of Thinnakara. This pristine spot is celebrated globally as one of the ultimate popular Instagram locations due to its untouched sand bars. Your family can explore the tiny coast, find beautiful seashells, or rest under custom-pitched luxury shade tents right on the shore."
                ),
                [
                    "Sightseeing Included: Thinnakara island shores, deep-water shipwreck viewing site.",
                    "Photography Points: Continuous panoramic sand banks merging into multi-toned blue ocean waters.",
                    "Overnight Stay: Bangaram Island Resort.",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                4,
                "Deep-Sea Fishing Expedition & Beach Side BBQ Luxury",
                (
                    "Today features an incredible adventure designed for the whole family. Board a professionally equipped deep-sea vessel for a guided catch-and-release family sports fishing session. In the afternoon, return to the shores of Bangaram where our resort chefs will convert the local catch into a spectacular customized culinary experience."
                ),
                [
                    "Sightseeing Included: Open ocean deep-sea coastal navigation safari.",
                    "Evening Experience: A private, premium family beachside barbecue with traditional musical performances.",
                    "Overnight Stay: Bangaram Island Resort.",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                5,
                "Private Exploration of Kalpetti Coral Reefs",
                (
                    "Following a relaxing breakfast, take a premium boat tour to the close-by Kalpetti Island. This unique geological ecosystem is famous for its shallow water walking flats, allowing family members to safely wander through low-tide zones to observe small colorful reef fish, unique crabs, and sea anemones up close without needing to swim."
                ),
                [
                    "Sightseeing Included: Guided low-tide reef walks, marine educational tour for kids.",
                    "Evening Experience: Calm tea session served directly on the soft sand banks.",
                    "Overnight Stay: Bangaram Island Resort.",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                6,
                "Jetty Transit to Agatti & Local Culture Experience",
                (
                    "Bid farewell to the serene environment of Bangaram as your family transfers via a smooth private speedboat back to Agatti Island. Check into your premium beachfront cottage villa. Spend the afternoon taking an unhurried luxury vehicle tour around the island, visiting traditional villages to see local coconut-carving crafts firsthand."
                ),
                [
                    "Sightseeing Included: Agatti Island museum, local village heritage walk.",
                    "Food Suggestions: Authentic local island delicacies and fresh coconut water refreshments.",
                    "Overnight Stay: Premium Agatti Lagoon Villa.",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                7,
                "Leisure at Agatti Beach & Grand Farewell Dinner",
                (
                    "A completely open day designed for premium relaxation and personalized family memories. Rejuvenate at the villa, enjoy complimentary kayaking right in front of your rooms, or stroll into the local craft markets to buy souvenirs. Tonight, we celebrate your journey with a signature experience created especially by our expert team."
                ),
                [
                    "Sightseeing Included: Beachfront photography setups, complimentary non-motorized water sports.",
                    "Evening Experience: Exclusive TRAGUIN Farewell Dinner hosted right on the beach under beautifully lit canopies.",
                    "Overnight Stay: Premium Agatti Lagoon Villa.",
                    "Meals Included: Breakfast, Lunch & Dinner",
                ],
            ),
            _day(
                8,
                "Departure Home with Unforgettable Memories",
                (
                    "Savor your last morning breakfast overlooking the glistening waters of the Arabian Sea. Pack your bags with unforgettable memories of a beautiful island holiday. Enjoy a seamless luxury vehicle transfer to Agatti Airport for your return flight home, fully satisfied with your high-end travel experience."
                ),
                [
                    "Sightseeing Included: Assisted airport drop-off.",
                    "Meals Included: Breakfast",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Standard Beach Cottage | Agatti Island Beach Villa",
                "Bangaram Island (5 Nights) / Agatti Island (2 Nights)",
                "07 Nights",
                "Deluxe",
                "Standard Beach Cottage / Beach Villa",
                "Breakfast & Dinner Included",
                4,
                1,
                description="OPTION 01 – DELUXE: Standard Beach Cottage (5 Nights) | Agatti Island Beach Villa (2 Nights) | Breakfast & Dinner Included",
            ),
            _hotel(
                "Premium Beach Villa | Agatti Deluxe Ocean View Villa",
                "Bangaram Island (5 Nights) / Agatti Island (2 Nights)",
                "07 Nights",
                "Premium",
                "Premium Beach Villa / Deluxe Ocean View Villa",
                "Breakfast & Dinner Included",
                5,
                2,
                description="OPTION 02 – PREMIUM: Premium Beach Villa (5 Nights) | Agatti Deluxe Ocean View Villa (2 Nights) | Breakfast & Dinner Included",
            ),
            _hotel(
                "Executive Beach Bungalow | Agatti Premium Lagoon Villa",
                "Bangaram Island (5 Nights) / Agatti Island (2 Nights)",
                "07 Nights",
                "Luxury",
                "Executive Beach Bungalow / Premium Lagoon Villa",
                "Full Meal Plan (All Meals)",
                5,
                3,
                description="OPTION 03 – LUXURY: Executive Beach Bungalow (5 Nights) | Agatti Premium Lagoon Villa (2 Nights) | Full Meal Plan (All Meals)",
            ),
            _hotel(
                "TRAGUIN Signature Royal Suite | Agatti Ultra Beachfront Diamond Suite",
                "Bangaram Island (5 Nights) / Agatti Island (2 Nights)",
                "07 Nights",
                "Ultra Luxury",
                "Signature Royal Suite / Ultra Beachfront Diamond Suite",
                "Bespoke Dine-Anywhere Meals",
                5,
                4,
                description="OPTION 04 – ULTRA LUXURY: TRAGUIN Signature Royal Suite (5 Nights) | Agatti Ultra Beachfront Diamond Suite (2 Nights) | Bespoke Dine-Anywhere Meals",
            ),
        ],
        inclusions=[
            _inc_included("Luxury Accommodation: Handpicked beach front resort villas.", 1),
            _inc_included("Gourmet Meals: Daily meals matching your selected hotel tier.", 2),
            _inc_included("Private Transfers: High-speed boats and air-conditioned island vehicles.", 3),
            _inc_included("Sightseeing Permits: All required Lakshadweep entry permissions managed completely by TRAGUIN.", 4),
            _inc_included("VIP On-Ground Support: 24/7 dedicated local assistance throughout the tour.", 5),
            _inc_included("Welcome Amenities: Personalized family gift box and refreshments on arrival.", 6),
            _inc_excluded("Air tickets to and from Agatti Airport.", 7),
            _inc_excluded("Scuba diving and other personal water sports activities.", 8),
            _inc_excluded("Laundry, telephone calls, or mini-bar charges.", 9),
            _inc_excluded("Tips, gratuities, and general porter services.", 10),
            _inc_excluded("Comprehensive travel insurance options.", 11),
        ],
    )
    return package, itinerary


LAKSHADWEEP_DOMESTIC_BUILDERS = [
    build_ld_011,
    build_ld_012,
    build_ld_013,
    build_ld_014,
    build_ld_015,
]
