"""Builder functions for CG-001 through CG-010 Chhattisgarh domestic packages."""

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

CHHATTISGARH_SLUG = "chhattisgarh"


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


def build_cg_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "CG-001"
    tour_code = "TG-CG-DISCOVERY"
    title = (
        "TRAGUIN Premium Chhattisgarh Tour Package — Family Adventure Discovery • "
        "Raipur • Sirpur • Chitrakote • Bastar"
    )
    duration = "05 Nights / 06 Days"
    slug = "cg-001-family-adventure-discovery-raipur-sirpur-chitrakote-bastar"
    itin_slug = "cg-001-family-adventure-discovery-raipur-sirpur-chitrakote-bastar-itinerary"
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
            _ph("State / Country: Chhattisgarh / India | Category: Family Adventure", 2),
            _ph("Destinations: Raipur • Sirpur • Chitrakote • Bastar", 3),
            _ph("Ideal for: Families & Culture Explorers", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Luxury Customized)", 6),
            _ph("Vehicle / Meals: Private Luxury AC SUV / MAPAI (Breakfast & Dinner)", 7),
            _ph(
                "Route Plan: Raipur (2N) ➔ Sirpur (1N) ➔ Chitrakote (1N) ➔ Bastar (1N) ➔ Raipur Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private scholar-guided heritage walks through Sirpur's "
                "Gupta-period archaeological marvels.",
                9,
            ),
            _ph(
                "Curated by TRAGUIN Experts: Handpicked routing and premium hotels emphasizing family comfort, "
                "safety, and cultural immersion.",
                10,
            ),
            _ph(
                "Exclusive Recommendations: Riverside viewpoints at Chitrakote Falls and authentic Bastar tribal "
                "market experiences.",
                11,
            ),
            _ph(
                "Shopping & Local Experiences: Bastar arts, Dhokra metal craft, exotic tribal jewelry, and "
                "regional delicacies.",
                12,
            ),
            _ph(
                "Important Notes: Conservative attire at temples; light woolens Nov–Feb; advance booking "
                "recommended during peak winter season.",
                13,
            ),
        ],
        moods=["Family", "Adventure", "Culture", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Luxury Customized)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Family Adventure Discovery • Raipur • Sirpur • Chitrakote • Bastar • 05 Nights / 06 Days",
        overview=(
            "Embark on an ethereal journey through Chhattisgarh, the hidden gem of India. Curated by TRAGUIN, "
            "this Luxury Chhattisgarh Holiday reveals breathtaking landscapes, from the 'Niagara of India' "
            "(Chitrakote Falls) to ancient architectural marvels. Experience a Premium Chhattisgarh Experience "
            "that promises unforgettable memories for your entire family.\n\n"
            "TOUR OVERVIEW\n"
            "Discover Chhattisgarh's raw, scenic beauty. TRAGUIN ensures your family enjoys seamless private "
            "transfers and handpicked hotels throughout this Best Chhattisgarh Tour Package. From Raipur's vibrant "
            "capital culture to Sirpur's archaeological wonders, the thundering horseshoe of Chitrakote, and the "
            "tribal heartland of Bastar, every day unfolds with curated experiences, expert local guidance, and "
            "premium comfort.\n\n"
            "WHY CHOOSE THE BEST CHHATTISGARH DISCOVERY TOUR?\n"
            "When planning a Luxury Chhattisgarh Holiday, discerning travellers seek more than standard sightseeing; "
            "they seek transformative connections to heritage, nature, and tribal culture. Chhattisgarh features "
            "iconic attractions including the internationally acclaimed Chitrakote Falls, the Gupta-period Laxman "
            "Temple at Sirpur, and vibrant Bastar artisan markets. Whether shopping for authentic Dhokra metal "
            "craft, indulging in local delicacies, or witnessing dramatic waterfall landscapes, our TRAGUIN "
            "Chhattisgarh Packages guarantee premium comfort, handpicked luxury stays, and curated exclusive "
            "experiences during the best time to visit Chhattisgarh."
        ),
        seo_title="CG-001 | Family Adventure Raipur Sirpur Chitrakote Bastar | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days Chhattisgarh family adventure (CG-001 / TG-CG-DISCOVERY): Raipur, "
            "Sirpur, Chitrakote Falls, Bastar tribal markets, and 4-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Raipur arrival and city cultural orientation on Day 01", 1),
            _ih("Sirpur Laxman Temple and Gupta-period heritage walks on Day 02", 2),
            _ih("Chitrakote Falls horseshoe waterfall and riverside stay on Day 03", 3),
            _ih("Bastar tribal markets and ancient arts immersion on Day 04", 4),
            _ih("Return to Raipur with local shopping on Day 05", 5),
            _ih("Raipur departure on Day 06", 6),
        ],
        days=[
            _day(
                1,
                "RAIPUR — ARRIVAL | WELCOME TO THE EMERALD HEART OF CENTRAL INDIA",
                (
                    "Your premium Chhattisgarh family adventure begins as you arrive at Raipur Airport or Railway "
                    "Station, where your dedicated TRAGUIN private chauffeur and tour assistant greet you with "
                    "refreshing welcome amenities. Transfer in absolute comfort to your handpicked luxury hotel. "
                    "After a smooth check-in, explore the city's vibrant culture with a gentle panoramic drive "
                    "across Naya Raipur and an evening visit to Swami Vivekanand Sarovar (Budha Talab). Return "
                    "for a curated welcome dinner introducing regional flavours."
                ),
                [
                    "Sightseeing Included: Naya Raipur panoramic drive, Swami Vivekanand Sarovar lake park.",
                    "Evening Experience: Welcome dinner with regional culinary introductions.",
                    "Overnight Stay: Raipur (Premium Luxury Hotel).",
                    "Meals Included: Welcome Refreshments & Gourmet Dinner.",
                ],
            ),
            _day(
                2,
                "RAIPUR TO SIRPUR | ARCHAEOLOGICAL WONDERS & GUPTA-PERIOD MASTERPIECES",
                (
                    "After a lavish breakfast, drive to Sirpur, an internationally renowned archaeological wonder "
                    "on the banks of the Mahanadi River. Visit the magnificent Laxman Temple, a classic example "
                    "of Gupta-period architecture with intricate brick carvings. TRAGUIN curated experiences include "
                    "private guided heritage walks through the excavated Buddhist monasteries and Anand Prabhu Kudi "
                    "Vihar. Check into your heritage property in Sirpur for an evening of cultural storytelling."
                ),
                [
                    "Sightseeing Included: Laxman Temple, Sirpur Archaeological Complex, Buddhist monastic ruins.",
                    "TRAGUIN Signature: Private scholar-guided heritage walk through Sirpur excavations.",
                    "Overnight Stay: Sirpur (Heritage Boutique Property).",
                    "Meals Included: Premium Breakfast & Traditional Dinner.",
                ],
            ),
            _day(
                3,
                "SIRPUR TO CHITRAKOTE | THE NIAGARA OF INDIA",
                (
                    "Travel south toward the stunning Chitrakote Falls, where the mighty Indravati River cascades "
                    "in a breathtaking horseshoe shape spanning nearly 300 meters. Witness the scenic beauty and "
                    "tranquility of India's widest waterfall from curated cliff-edge viewpoints. Enjoy an immersive "
                    "experience with optional private boat perspectives at the base. Check into your premium riverside "
                    "resort curated by TRAGUIN experts overlooking the thundering white waters."
                ),
                [
                    "Sightseeing Included: Chitrakote Horseshoe Falls, Indravati River viewpoints.",
                    "Evening Experience: Illuminated waterfall viewing from resort decks.",
                    "Overnight Stay: Chitrakote (Premium Riverside Eco-Resort).",
                    "Meals Included: Breakfast & Riverside Dinner.",
                ],
            ),
            _day(
                4,
                "CHITRAKOTE & BASTAR | TRIBAL HEARTLAND & ANCIENT ARTS",
                (
                    "Explore the cultural heart of Bastar. Visit local tribal markets and iconic attractions "
                    "showcasing ancient Dhokra metal art, terracotta crafts, and forest honey trading traditions. "
                    "Immersive experiences await in the heart of tribal India as your guide introduces Gond, Maria, "
                    "and Bhatra community customs. Visit artisan workshops in Kondagaon and experience a vibrant "
                    "local haat before settling into your Bastar heritage stay."
                ),
                [
                    "Sightseeing Included: Bastar tribal markets, Dhokra artisan workshops, Kondagaon craft village.",
                    "Evening Experience: Tribal folk storytelling and craft demonstration.",
                    "Overnight Stay: Bastar / Jagdalpur (Premium Heritage Hotel).",
                    "Meals Included: Breakfast & Authentic Bastar Dinner.",
                ],
            ),
            _day(
                5,
                "BASTAR TO RAIPUR | RELAXATION & LOCAL SHOPPING",
                (
                    "Return to Raipur along scenic forest highways. Enjoy premium stays and relax at your "
                    "handpicked luxury hotel. TRAGUIN offers exclusive recommendations for local shopping — "
                    "authentic Bastar bell-metal, Tussar silk, and tribal jewelry. Spend your evening at leisure "
                    "with optional spa treatments or a farewell dinner celebrating your family's discoveries."
                ),
                [
                    "Sightseeing Included: Scenic return drive, Raipur handicraft shopping districts.",
                    "Evening Experience: Farewell dinner and souvenir shopping guidance.",
                    "Overnight Stay: Raipur (Premium Luxury Hotel).",
                    "Meals Included: Breakfast & Farewell Special Dinner.",
                ],
            ),
            _day(
                6,
                "RAIPUR — DEPARTURE | CHERISHING UNFORGETTABLE MEMORIES",
                (
                    "Indulge in a final lavish breakfast at your premium hotel. Your private luxury transport will "
                    "safely escort you to Raipur Airport or Railway Station for your onward journey, carrying home "
                    "unforgettable memories of your Luxury Chhattisgarh Holiday meticulously designed by TRAGUIN."
                ),
                [
                    "Transfers Included: Private luxury door-to-door departure transfer.",
                    "Meals Included: Sumptuous Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Hotel Babylon Inn / Hyatt Raipur | Mahanadi Heritage Lodge Sirpur | MPT Chitrakote Log Huts | MPT Naman Bastar Resort",
                "Raipur (2 Nights) / Sirpur (1 Night) / Chitrakote (1 Night) / Bastar (1 Night)",
                "05 Nights",
                "Deluxe",
                "Deluxe Room",
                "MAPAI (Breakfast & Dinner)",
                4,
                1,
                description="OPTION 01 – DELUXE: Hotel Babylon Inn / Hyatt Raipur (Raipur, 2 Nights) | Mahanadi Heritage Lodge Sirpur (Sirpur, 1 Night) | MPT Chitrakote Log Huts (Chitrakote, 1 Night) | MPT Naman Bastar Resort (Bastar, 1 Night) | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "Courtyard by Marriott Raipur | Sirpur Archaeological Retreat | Chitrakote River View Huts | Asansol Heritage Resort",
                "Raipur (2 Nights) / Sirpur (1 Night) / Chitrakote (1 Night) / Bastar (1 Night)",
                "05 Nights",
                "Premium",
                "Premium Room",
                "MAPAI (Breakfast & Dinner)",
                4,
                2,
                description="OPTION 02 – PREMIUM: Courtyard by Marriott Raipur (Raipur, 2 Nights) | Sirpur Archaeological Retreat (Sirpur, 1 Night) | Chitrakote River View Huts (Chitrakote, 1 Night) | Asansol Heritage Resort (Bastar, 1 Night) | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "Sayaji Hotel Raipur | Sirpur Boutique Heritage Lodge | Dandami Luxury Bison Resort | Grand Bastar Heritage Estate",
                "Raipur (2 Nights) / Sirpur (1 Night) / Chitrakote (1 Night) / Bastar (1 Night)",
                "05 Nights",
                "Luxury",
                "Luxury Room",
                "MAPAI (Breakfast & Dinner)",
                5,
                3,
                description="OPTION 03 – LUXURY: Sayaji Hotel Raipur (Raipur, 2 Nights) | Sirpur Boutique Heritage Lodge (Sirpur, 1 Night) | Dandami Luxury Bison Resort (Chitrakote, 1 Night) | Grand Bastar Heritage Estate (Bastar, 1 Night) | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "Mayfair Lake Resort Raipur | Sirpur Royal Residency | Dandami Premium Presidential Villa | Bastar Palace Royal Suite",
                "Raipur (2 Nights) / Sirpur (1 Night) / Chitrakote (1 Night) / Bastar (1 Night)",
                "05 Nights",
                "Ultra Luxury",
                "Luxury Suite / Villa",
                "Elite Chef Curated Meals",
                5,
                4,
                description="OPTION 04 – ULTRA LUXURY: Mayfair Lake Resort Raipur (Raipur, 2 Nights) | Sirpur Royal Residency (Sirpur, 1 Night) | Dandami Premium Presidential Villa (Chitrakote, 1 Night) | Bastar Palace Royal Suite (Bastar, 1 Night) | Elite Chef Curated Meals",
            ),
        ],
        inclusions=[
            _inc_included("Premium Accommodation: Handpicked hotels as per chosen category.", 1),
            _inc_included("Luxury Transportation: Private AC Innova Crysta for all transfers & sightseeing.", 2),
            _inc_included("Curated Meal Plan: Daily luxury breakfast and gourmet dinners (MAPAI).", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated guest experience manager on call.", 4),
            _inc_included("Welcome Amenities: Customized family travel kit and refreshments upon arrival.", 5),
            _inc_included("Complimentary Experience: Private guided heritage walk at Sirpur archaeological site.", 6),
            _inc_excluded("Airfare / Train tickets to and from Raipur terminals.", 7),
            _inc_excluded("Monument entry tickets, camera fees, or optional boat ride charges.", 8),
            _inc_excluded("Personal expenses such as laundry, telephone calls, and tips.", 9),
            _inc_excluded("Any optional activities or extended tours not explicitly listed.", 10),
        ],
    )
    return package, itinerary


def build_cg_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "CG-002"
    tour_code = "TG-CG-CHITRA-002"
    title = (
        "TRAGUIN Premium Chitrakote Adventure Package — Luxury Adventure • "
        "The Niagara of India • Jagdalpur Expedition"
    )
    duration = "04 Nights / 05 Days"
    slug = "cg-002-luxury-adventure-chitrakote-jagdalpur"
    itin_slug = "cg-002-luxury-adventure-chitrakote-jagdalpur-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Chhattisgarh / India | Category: Luxury Adventure", 2),
            _ph("Destinations: Jagdalpur • Chitrakote Falls", 3),
            _ph("Ideal for: Adventure & Nature Lovers", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Customised Packages)", 6),
            _ph("Vehicle / Meals: Luxury 4x4 Transfers / MAPAI (Breakfast & Dinner)", 7),
            _ph("Route Plan: Jagdalpur Arrival (4N) ➔ Chitrakote ➔ Kutumsar Caves ➔ Tirathgarh ➔ Departure", 8),
            _ph("TRAGUIN Signature Experience: Private boat ride at the base of Chitrakote Falls.", 9),
            _ph("Curated by TRAGUIN Experts: Handpicked Jagdalpur luxury resorts with nature excursion access.", 10),
            _ph("Exclusive Recommendations: Dokra metal art artisan sessions and Tirathgarh picnic viewpoints.", 11),
            _ph("Shopping & Local Experiences: Bastar Dokra metal art, tribal jewelry, and forest honey.", 12),
            _ph("Important Notes: Non-slip footwear for cave and waterfall trails; book 30–45 days ahead in peak season.", 13),
        ],
        moods=["Adventure", "Nature", "Luxury", "Family"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note="On Request (Premium Customised Packages)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Chitrakote Adventure • Jagdalpur • Chitrakote Falls • 04 Nights / 05 Days",
        overview=(
            "Discover the raw, untamed majesty of Chhattisgarh with TRAGUIN. Our Best Chitrakote Adventure "
            "Package invites you to explore the stunning Chitrakote Falls, where the mighty Indravati River "
            "thunders down in a breathtaking landscape. This curated Luxury Chhattisgarh Holiday combines "
            "thrilling adventure with premium stays, ensuring your family enjoys the scenic beauty and iconic "
            "attractions of Jagdalpur in absolute comfort.\n\n"
            "TOUR OVERVIEW\n"
            "This 4N/5D adventure is a perfectly balanced Chhattisgarh Family Tour, designed for thrill-seekers "
            "and luxury travelers. From exploring ancient Kutumsar Caves to witnessing the 'Niagara of India,' "
            "TRAGUIN ensures a seamless private journey. Your itinerary includes luxury 4x4 transfers, handpicked "
            "hotels, and exclusive nature excursions with TRAGUIN curated experiences throughout.\n\n"
            "WHY CHOOSE THE CHITRAKOTE ADVENTURE PACKAGE?\n"
            "For discerning travelers seeking raw natural beauty alongside premium comfort, this Luxury "
            "Chhattisgarh Holiday presents spectacular waterfall landscapes, subterranean cave wonders, and "
            "vibrant tribal artisan culture. Popular experiences include private boat rides at Chitrakote, "
            "Kutumsar Cave exploration, and Dokra metal art workshops — all delivered with TRAGUIN's signature "
            "personalized luxury support."
        ),
        seo_title="CG-002 | Chitrakote Adventure Jagdalpur | TRAGUIN",
        seo_description="Premium 04 Nights / 05 Days Chitrakote adventure (CG-002 / TG-CG-CHITRA-002): Chitrakote Falls, Kutumsar Caves, Tirathgarh, Dokra art, and 4-tier Jagdalpur hotels.",
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Jagdalpur arrival and Bastar orientation briefing on Day 01", 1),
            _ih("Chitrakote Falls horseshoe waterfall and private boat ride on Day 02", 2),
            _ih("Kutumsar Caves and Tirathgarh Falls adventure on Day 03", 3),
            _ih("Bastar culture, Dokra artisan session, and local markets on Day 04", 4),
            _ih("Jagdalpur departure on Day 05", 5),
        ],
        days=[
            _day(1, "JAGDALPUR — ARRIVAL IN THE HEART OF BASTAR", (
                "Arrive in Jagdalpur, the cultural capital of Bastar. Receive a warm welcome from your TRAGUIN guide "
                "with refreshing adventure kits and mineral water. Transfer to your luxury resort nestled amid sal "
                "forest canopies. Relax before an evening briefing about the breathtaking landscapes of Bastar, "
                "including waterfall volumes, cave access protocols, and artisan village schedules curated by your "
                "dedicated tour manager."
            ), [
                "Sightseeing Included: Jagdalpur town orientation, Bastar Palace grounds preview.",
                "Evening Experience: Pre-expedition briefing and specialty regional dinner.",
                "Overnight Stay: Luxury Resort, Jagdalpur.",
                "Meals Included: Welcome Refreshments & Gourmet Dinner.",
            ]),
            _day(2, "CHITRAKOTE — THE NIAGARA OF INDIA", (
                "Visit the spectacular Chitrakote Falls. Witness the scenic beauty of the Indravati River as it "
                "cascades in a horseshoe shape spanning nearly 300 meters — proudly called the 'Niagara of India'. "
                "Enjoy an immersive experience with a TRAGUIN Signature private boat ride at the base of these "
                "iconic attractions. Capture golden-hour photography from cliff-edge viewpoints before returning "
                "to your Jagdalpur luxury resort for an evening campfire dinner."
            ), [
                "Sightseeing Included: Chitrakote Horseshoe Falls, Indravati River viewpoints.",
                "TRAGUIN Signature: Private boat ride at the base of Chitrakote Falls.",
                "Overnight Stay: Luxury Resort, Jagdalpur.",
                "Meals Included: Premium Breakfast & Riverside Dinner.",
            ]),
            _day(3, "KUTUMSAR CAVES — ADVENTURE & DISCOVERY", (
                "Embark on an adventure to the Kutumsar Caves, famous for their unique blind fish and spectacular "
                "limestone formations carved over millions of years. Descend with certified cave escorts and "
                "headlamps through narrow archways into massive underground chambers. Later, visit Tirathgarh "
                "Falls for a breathtaking multi-tiered waterfall picnic set up by your resort team amid lush "
                "Kanger Valley greenery."
            ), [
                "Sightseeing Included: Kutumsar Caves, Tirathgarh Waterfalls, Kanger Valley corridor.",
                "Evening Experience: Forest picnic lunch and relaxed resort evening.",
                "Overnight Stay: Luxury Resort, Jagdalpur.",
                "Meals Included: Breakfast, Curated Picnic Lunch & Gourmet Dinner.",
            ]),
            _day(4, "BASTAR CULTURE & LOCAL ART", (
                "Explore the local markets of Bastar, famous for Dokra metal art and terracotta crafts. Enjoy an "
                "exclusive session with local tribal artisans — a TRAGUIN curated experience where master craftsmen "
                "demonstrate the ancient lost-wax bell-metal casting technique unchanged since the Indus Valley "
                "Civilization. Visit the Anthropological Museum and browse vibrant weekly haats before a farewell "
                "celebration dinner."
            ), [
                "Sightseeing Included: Dokra artisan village, Bastar Anthropological Museum, tribal haat.",
                "TRAGUIN Signature: Exclusive artisan interaction and hands-on craft demonstration.",
                "Overnight Stay: Luxury Resort, Jagdalpur.",
                "Meals Included: Premium Breakfast & Farewell Special Dinner.",
            ]),
            _day(5, "DEPARTURE | MEMORIES OF A PREMIUM CHHATTISGARH EXPERIENCE", (
                "Savor a final hearty breakfast at your luxury resort. Your private chauffeur-driven vehicle will "
                "transfer you to Jagdalpur Airport or onward connection point for your departure, carrying "
                "unforgettable memories of waterfalls, caves, and tribal artistry curated by TRAGUIN."
            ), [
                "Transfers Included: Private luxury departure transfer.",
                "Meals Included: Sumptuous Buffet Breakfast.",
            ]),
        ],
        hotels=[
            _hotel("Hotel Bastar Palace / MPT Naman Bastar Resort", "Jagdalpur (4 Nights)", "04 Nights", "Deluxe", "Deluxe Room", "MAPAI (Breakfast & Dinner)", 4, 1, description="OPTION 01 – DELUXE: Hotel Bastar Palace / MPT Naman Bastar Resort (Jagdalpur, 4 Nights) | MAPAI (Breakfast & Dinner)"),
            _hotel("Asansol Heritage Resort Jagdalpur", "Jagdalpur (4 Nights)", "04 Nights", "Premium", "Premium Room", "MAPAI (Breakfast & Dinner)", 4, 2, description="OPTION 02 – PREMIUM: Asansol Heritage Resort Jagdalpur (Jagdalpur, 4 Nights) | MAPAI (Breakfast & Dinner)"),
            _hotel("Grand Bastar Heritage Estate", "Jagdalpur (4 Nights)", "04 Nights", "Luxury", "Luxury Room", "MAPAI (Breakfast & Dinner)", 5, 3, description="OPTION 03 – LUXURY: Grand Bastar Heritage Estate (Jagdalpur, 4 Nights) | MAPAI (Breakfast & Dinner)"),
            _hotel("Bastar Palace Royal Suite Residence", "Jagdalpur (4 Nights)", "04 Nights", "Ultra Luxury", "Royal Suite", "Elite Chef Curated Meals", 5, 4, description="OPTION 04 – ULTRA LUXURY: Bastar Palace Royal Suite Residence (Jagdalpur, 4 Nights) | Elite Chef Curated Meals"),
        ],
        inclusions=[
            _inc_included("Accommodation in handpicked hotels as per chosen category.", 1),
            _inc_included("Daily meals & luxury transportation for all sightseeing.", 2),
            _inc_included("Sightseeing with TRAGUIN support and expert local guides.", 3),
            _inc_included("Complimentary Experience: Private boat ride at Chitrakote Falls base.", 4),
            _inc_included("Welcome Amenities: Adventure kit, refreshments, and mineral water in vehicle.", 5),
            _inc_excluded("Flights & personal expenses.", 6),
            _inc_excluded("Entry tickets, cave permits, camera fees & insurance.", 7),
            _inc_excluded("Optional activities not explicitly listed in inclusions.", 8),
        ],
    )
    return package, itinerary


def build_cg_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "CG-003"
    tour_code = "TG-CG-KANGER-003"
    title = (
        "TRAGUIN Premium Kanger Valley Wildlife Tour — Wildlife & Nature Exploration • "
        "Kanger Valley National Park • Jagdalpur"
    )
    duration = "04 Nights / 05 Days"
    slug = "cg-003-kanger-valley-wildlife-jagdalpur"
    itin_slug = "cg-003-kanger-valley-wildlife-jagdalpur-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Chhattisgarh / India | Category: Wildlife & Nature Exploration", 2),
            _ph("Destinations: Kanger Valley National Park • Jagdalpur", 3),
            _ph("Ideal for: Nature Lovers & Wildlife Enthusiasts", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Wildlife Customised)", 6),
            _ph("Vehicle / Meals: Private Luxury Transport / Meal plan per hotel tier", 7),
            _ph("Route Plan: Jagdalpur Arrival (4N) ➔ Kanger Valley ➔ Kutumsar Caves ➔ Tribal Heritage ➔ Departure", 8),
            _ph("TRAGUIN Signature Experience: Subterranean Kutumsar Cave exploration with certified escorts.", 9),
            _ph("Curated by TRAGUIN Experts: Three-tier handpicked Jagdalpur wildlife lodges and heritage stays.", 10),
            _ph("Exclusive Recommendations: Tirathgarh multi-tiered falls and Bastar Anthropological Museum.", 11),
            _ph("Shopping & Local Experiences: Dhokra art, forest honey, and tribal handicrafts.", 12),
            _ph("Important Notes: Valid photo ID required for national park entry; comfortable trekking shoes mandatory.", 13),
        ],
        moods=["Wildlife", "Nature", "Adventure", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note="On Request (Premium Wildlife Customised)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Kanger Valley Wildlife • Jagdalpur • Kutumsar Caves • 04 Nights / 05 Days",
        overview=(
            "Discover the hidden jewel of Central India with TRAGUIN. Our Best Kanger Valley Tour Package offers "
            "an immersion into a landscape of breathtaking landscapes and rich biodiversity. From the subterranean "
            "wonders of Kutumsar Caves to the roaring Tirathgarh Falls, this Luxury Chhattisgarh Holiday is designed "
            "for those who seek curated experiences in the lap of nature.\n\n"
            "TOUR OVERVIEW\n"
            "This 4N/5D itinerary covers the wild heart of Chhattisgarh, featuring private luxury transport and "
            "handpicked hotels. Enjoy seamless TRAGUIN support throughout your journey into the wild — from "
            "Bastar Palace heritage to Kanger Valley National Park corridors, underground limestone galleries, and "
            "authentic tribal craft markets.\n\n"
            "WHY CHOOSE THE KANGER VALLEY WILDLIFE TOUR?\n"
            "For nature lovers and wildlife enthusiasts, Kanger Valley presents unparalleled ecological marvels. "
            "Iconic attractions include Tirathgarh's multi-tiered cascades, Kutumsar's blind-fish caves, and "
            "Bastar's rich tribal heritage. TRAGUIN guarantees premium lodge stays, expert naturalist guidance, and "
            "immersive forest experiences across India's greenest eco-corridor."
        ),
        seo_title="CG-003 | Kanger Valley Wildlife Jagdalpur | TRAGUIN",
        seo_description="Premium 04 Nights / 05 Days Kanger Valley wildlife tour (CG-003): Kutumsar Caves, Tirathgarh Falls, tribal heritage, and 3-tier Jagdalpur accommodation.",
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Jagdalpur arrival, Bastar Palace and Anthropological Museum on Day 01", 1),
            _ih("Kanger Valley National Park and Tirathgarh Falls on Day 02", 2),
            _ih("Kutumsar Caves subterranean exploration on Day 03", 3),
            _ih("Tribal culture, craft heritage, and local markets on Day 04", 4),
            _ih("Jagdalpur departure on Day 05", 5),
        ],
        days=[
            _day(1, "ARRIVAL IN JAGDALPUR & LOCAL HERITAGE", (
                "Arrive in Jagdalpur, the gateway to the wild. Your TRAGUIN representative welcomes you and "
                "transfers you to your handpicked resort. Explore the Bastar Palace and its historic grounds, "
                "then visit the Anthropological Museum showcasing rare tribal clothing, weaponry, and cultural "
                "artifacts. Enjoy an evening orientation on Kanger Valley ecology and wildlife spotting protocols."
            ), [
                "Sightseeing Included: Bastar Palace, Anthropological Museum.",
                "Overnight Stay: Jagdalpur (Handpicked Wildlife Resort).",
                "Meals Included: Welcome Refreshments & Dinner.",
            ]),
            _day(2, "KANGER VALLEY EXPLORATION", (
                "Enter Kanger Valley National Park with your certified naturalist guide. Witness the surreal "
                "Tirathgarh Falls, a multi-tiered marvel of scenic beauty where the Mugabahar River cascades "
                "through limestone steps amid dense sal canopies. Trek along maintained forest paths, observe "
                "local birdlife including the hill myna, and capture panoramic photography of the verdant valley "
                "corridors before returning to your resort."
            ), [
                "Sightseeing Included: Kanger Valley National Park, Tirathgarh Waterfalls.",
                "Overnight Stay: Jagdalpur (Handpicked Wildlife Resort).",
                "Meals Included: Breakfast & Dinner.",
            ]),
            _day(3, "SUBTERRANEAN WONDERS OF KUTUMSAR", (
                "Venture deep into Kutumsar Caves with certified cave tracking escorts and headlamps. These "
                "limestone formations offer exclusive experiences that define Kanger Valley Sightseeing — "
                "colossal stalactites, underground pools, and rare blind cave-fish species inhabiting isolated "
                "subterranean ecosystems. Return for a relaxed evening at your lodge with a wildlife documentary "
                "briefing curated by TRAGUIN."
            ), [
                "Sightseeing Included: Kutumsar Caves, Dandak Caves edge viewpoints.",
                "TRAGUIN Signature: Expert-led subterranean cave navigation.",
                "Overnight Stay: Jagdalpur (Handpicked Wildlife Resort).",
                "Meals Included: Breakfast & Dinner.",
            ]),
            _day(4, "TRIBAL CULTURE & CRAFT HERITAGE", (
                "Immerse in the rich tribal heritage of Bastar. Visit local markets for authentic Dhokra art, "
                "terracotta pottery, and organic forest honey. Enjoy an interactive session with tribal artisans "
                "demonstrating lost-wax metal casting. Visit a vibrant weekly haat to witness barter traditions "
                "and colorful indigenous attire before a farewell dinner celebrating your wilderness journey."
            ), [
                "Sightseeing Included: Tribal haat, Dhokra artisan workshops, craft cooperatives.",
                "Overnight Stay: Jagdalpur (Handpicked Wildlife Resort).",
                "Meals Included: Breakfast & Farewell Dinner.",
            ]),
            _day(5, "DEPARTURE", (
                "Enjoy a final breakfast before your transfer to Jagdalpur Airport or onward connection, taking "
                "with you unforgettable memories curated by TRAGUIN of caves, waterfalls, and tribal wilderness."
            ), [
                "Transfers Included: Private departure transfer.",
                "Meals Included: Buffet Breakfast.",
            ]),
        ],
        hotels=[
            _hotel("Forest Resort Jagdalpur", "Jagdalpur (4 Nights)", "04 Nights", "Deluxe", "Deluxe Room", "Breakfast & Dinner", 4, 1, description="OPTION 01 – DELUXE: Forest Resort Jagdalpur (Jagdalpur, 4 Nights) | Breakfast & Dinner"),
            _hotel("Bastariya Heritage Stay", "Jagdalpur (4 Nights)", "04 Nights", "Premium", "Premium Room", "Breakfast & Dinner", 4, 2, description="OPTION 02 – PREMIUM: Bastariya Heritage Stay (Jagdalpur, 4 Nights) | Breakfast & Dinner"),
            _hotel("Tented Luxury Eco-Lodge", "Jagdalpur (4 Nights)", "04 Nights", "Luxury", "Luxury Tent", "Full Board", 5, 3, description="OPTION 03 – LUXURY: Tented Luxury Eco-Lodge (Jagdalpur, 4 Nights) | Full Board"),
        ],
        inclusions=[
            _inc_included("Accommodation in handpicked hotels as per chosen tier.", 1),
            _inc_included("Daily meals as per hotel meal plan.", 2),
            _inc_included("Luxury transportation for all transfers and sightseeing.", 3),
            _inc_included("TRAGUIN support with certified naturalist and cave escorts.", 4),
            _inc_included("Complimentary Experience: Guided Kutumsar Cave exploration.", 5),
            _inc_excluded("Flights & personal expenses.", 6),
            _inc_excluded("National park entry fees, cave permits, and camera charges.", 7),
            _inc_excluded("Travel insurance and optional activities.", 8),
        ],
    )
    return package, itinerary

def build_cg_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "CG-004"
    tour_code = "TG-CG-BST-004"
    title = (
        "TRAGUIN Premium Bastar Experience Package — Tribal Soul of India • "
        "Jagdalpur • Bastar • Chitrakoot"
    )
    duration = "05 Nights / 06 Days"
    slug = "cg-004-bastar-experience-jagdalpur-chitrakoot"
    itin_slug = "cg-004-bastar-experience-jagdalpur-chitrakoot-itinerary"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Chhattisgarh / India | Category: Premium Family Cultural Tour", 2),
            _ph("Destinations: Jagdalpur • Bastar • Chitrakoot", 3),
            _ph("Ideal for: Families & Culture Enthusiasts", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Luxury Customized)", 6),
            _ph("Vehicle / Meals: Private Luxury SUV / Premium Breakfast & Dinner", 7),
            _ph("Route Plan: Jagdalpur Arrival (5N) ➔ Bastar ➔ Chitrakoot Falls ➔ Departure", 8),
            _ph("TRAGUIN Signature Experience: Private artisan interactions and sunset high tea at Chitrakoot Falls.", 9),
            _ph("Curated by TRAGUIN Experts: Handpicked local experiences and dedicated photography tours.", 10),
            _ph("Premium Handpicked Hotels: Three-tier Jagdalpur accommodation with chef-curated dining.", 11),
            _ph("Shopping & Local Experiences: Dhokra metal art, tribal haats, and Bastar handicrafts.", 12),
            _ph("Important Notes: Book 30–45 days ahead for peak winter; conservative attire at Danteshwari Temple.", 13),
        ],
        moods=["Family", "Culture", "Heritage", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note="On Request (Premium Luxury Customized)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Bastar Experience • Jagdalpur • Chitrakoot • 05 Nights / 06 Days",
        overview=(
            "Discover the hidden crown jewel of central India. The Best Bastar Tour Package, curated exclusively by "
            "TRAGUIN, invites your family to an extraordinary journey into the heart of tribal culture, raw landscapes, "
            "and ancient traditions. Known as the 'tribal soul of India', Bastar is a sanctuary of breathtaking "
            "landscapes, magnificent waterfalls like the 'Niagara of India' (Chitrakoot), and ancient art forms.\n\n"
            "TOUR OVERVIEW\n"
            "This bespoke Bastar Family Tour offers an intimate window into some of India's most preserved tribal "
            "traditions and scenic wonders. From arrival to departure, experience seamless personalized luxury with "
            "private premium transport, handpicked top-rated hotels, and chef-curated dining highlighting unique "
            "local flavors of Bastar.\n\n"
            "WHY CHOOSE THE PREMIUM BASTAR EXPERIENCE?\n"
            "Iconic Attractions: Chitrakoot Falls, Tirathgarh waterfalls, Danteshwari Temple, and Kanger Valley "
            "National Park. Most Searched Experiences: Tribal haats, Dhokra metal art, underground caves, and "
            "panoramic sunset vistas. Best Time to Visit Bastar: October to March for perfect outdoor sightseeing."
        ),
        seo_title="CG-004 | Bastar Experience Jagdalpur Chitrakoot | TRAGUIN",
        seo_description="Premium 05 Nights / 06 Days Bastar experience (CG-004 / TG-CG-BST-004): Chitrakoot Falls, Tirathgarh, Kutumsar Caves, Dhokra villages, and 3-tier Jagdalpur hotels.",
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Jagdalpur arrival, Bastar Palace, and local orientation on Day 01", 1),
            _ih("Chitrakoot Falls private boat ride and sunset high tea on Day 02", 2),
            _ih("Tirathgarh Falls, Kanger Valley, and Kutumsar Caves on Day 03", 3),
            _ih("Dhokra artisan villages and tribal haat on Day 04", 4),
            _ih("Danteshwari Temple and Bastar museums on Day 05", 5),
            _ih("Jagdalpur departure on Day 06", 6),
        ],
        days=[
            _day(1, "JAGDALPUR — ARRIVAL & GATEWAY TO TRIBAL SOUL", (
                "Your journey begins as you arrive in Jagdalpur. Your dedicated TRAGUIN private chauffeur welcomes you "
                "and transfers you comfortably to your premium handpicked heritage-style hotel. After smooth check-in, "
                "spend your afternoon exploring the local town and visiting the Bastar Palace and its grounds. Conclude "
                "the day with a dinner featuring local specialties tailored by your hotel chefs."
            ), [
                "Sightseeing Included: Jagdalpur town orientation, Bastar Palace grounds.",
                "Meals Included: Welcome Dinner.",
                "Overnight Stay: Premium Hotel, Jagdalpur.",
            ]),
            _day(2, "THE NIAGARA OF INDIA — CHITRAKOOT FALLS", (
                "After breakfast, drive to the breathtaking Chitrakoot Falls, where the Indravati River plunges down "
                "with thunderous force. Enjoy a private boat ride for an up-close perspective. Spend the afternoon taking "
                "photos of this natural wonder. As evening falls, enjoy a TRAGUIN curated sunset high tea near the falls."
            ), [
                "Sightseeing Included: Chitrakoot Falls, private boat excursion.",
                "Meals Included: Breakfast & Dinner.",
                "Overnight Stay: Premium Hotel, Jagdalpur.",
            ]),
            _day(3, "NATURE'S WONDERS — TIRATHGARH & KANGER VALLEY", (
                "Travel to Kanger Valley National Park, a sanctuary of biodiversity. Visit the stunning Tirathgarh "
                "waterfalls, where water cascades in multiple stages through lush greenery. Explore the nearby Kutumsar "
                "Caves with an expert guide to discover hidden subterranean stalactites. This is a day for immersive "
                "nature discovery."
            ), [
                "Sightseeing Included: Tirathgarh Falls, Kanger Valley National Park, Kutumsar Caves.",
                "Meals Included: Breakfast & Dinner.",
                "Overnight Stay: Premium Hotel, Jagdalpur.",
            ]),
            _day(4, "ARTISAN VILLAGES & TRIBAL TRADITIONS", (
                "Today is dedicated to the artistry of Bastar. Visit traditional Dhokra metal-casting villages where "
                "artisans still use ancient lost-wax techniques. Meet the masters, witness the process, and shop for "
                "authentic metal crafts. In the afternoon, visit a local tribal Haat (market) to see colorful traditional life."
            ), [
                "Sightseeing Included: Dhokra artisan village, Local Tribal Haat.",
                "Meals Included: Breakfast & Dinner.",
                "Overnight Stay: Premium Hotel, Jagdalpur.",
            ]),
            _day(5, "HERITAGE & CULTURE — DANTESHWARI TEMPLE", (
                "Visit the historic Danteshwari Temple in Dantewada, one of the most significant spiritual centers in "
                "the region. Spend the afternoon visiting local museums to understand the rich historical timeline of the "
                "Bastar tribal kingdoms. Celebrate your final full day with a grand TRAGUIN signature farewell dinner."
            ), [
                "Sightseeing Included: Danteshwari Temple, Bastar Museums.",
                "Meals Included: Breakfast & Farewell Dinner.",
                "Overnight Stay: Premium Hotel, Jagdalpur.",
            ]),
            _day(6, "DEPARTURE WITH MEMORIES", (
                "Enjoy a final breakfast and some leisure time before your transfer to the airport or station. Your "
                "journey through the heart of India concludes here, leaving you with precious memories curated by TRAGUIN."
            ), [
                "Meals Included: Breakfast.",
            ]),
        ],
        hotels=[
            _hotel("Hotel Bastar Palace", "Jagdalpur (5 Nights)", "05 Nights", "Deluxe", "Deluxe Room", "Breakfast & Dinner", 4, 1, description="OPTION 01 – DELUXE: Hotel Bastar Palace (Jagdalpur, 5 Nights) | Breakfast & Dinner"),
            _hotel("MPT Dandami Luxury Resort", "Jagdalpur (5 Nights)", "05 Nights", "Premium", "Premium Room", "Breakfast & Dinner", 4, 2, description="OPTION 02 – PREMIUM: MPT Dandami Luxury Resort (Jagdalpur, 5 Nights) | Breakfast & Dinner"),
            _hotel("Heritage Boutique Stay", "Jagdalpur (5 Nights)", "05 Nights", "Luxury", "Luxury Room", "Breakfast & Dinner", 5, 3, description="OPTION 03 – LUXURY: Heritage Boutique Stay (Jagdalpur, 5 Nights) | Breakfast & Dinner"),
        ],
        inclusions=[
            _inc_included("Accommodation in premium hotels as per chosen tier.", 1),
            _inc_included("Daily breakfast and dinner.", 2),
            _inc_included("Private luxury vehicle for all transfers and sightseeing.", 3),
            _inc_included("Expert guide services for cultural and heritage tours.", 4),
            _inc_included("TRAGUIN support and assistance.", 5),
            _inc_excluded("Flights/Trains.", 6),
            _inc_excluded("Entry fees and camera charges.", 7),
            _inc_excluded("Personal expenses.", 8),
            _inc_excluded("Optional tours or activities.", 9),
        ],
    )
    return package, itinerary


def build_cg_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "CG-005"
    tour_code = "TG-CG-SCL-005"
    title = (
        "TRAGUIN Premium Chhattisgarh Tour Package — Senior Citizen Leisure • "
        "Raipur • Sirpur • Jagdalpur • Chitrakote"
    )
    duration = "05 Nights / 06 Days"
    slug = "cg-005-senior-citizen-leisure-raipur-jagdalpur-chitrakote"
    itin_slug = "cg-005-senior-citizen-leisure-raipur-jagdalpur-chitrakote-itinerary"
    loc = "Raipur (2 Nights) / Jagdalpur (2 Nights) / Chitrakote (1 Night)"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Chhattisgarh / India | Category: Senior Citizen Leisure Tour", 2),
            _ph("Destinations: Raipur • Sirpur • Jagdalpur (Bastar) • Chitrakote", 3),
            _ph("Ideal for: Senior Citizens & Slow-Paced Families", 4),
            _ph("Best season: October to March (Mild & Pleasant weather)", 5),
            _ph("Starting price: On Request (Premium Luxury Tier)", 6),
            _ph("Vehicle: Private AC Luxury SUV (Innova Crysta with Captain Seats) | Meal Plan: Premium MAPAI", 7),
            _ph("Route Plan: Raipur (2N) ➔ Jagdalpur / Bastar (2N) ➔ Chitrakote Falls (1N) ➔ Raipur Departure", 8),
            _ph("TRAGUIN Signature Experience: Private smooth boat excursion at Chitrakote Falls without steep stairs.", 9),
            _ph("Curated by TRAGUIN Experts: Ground-floor room blockings and senior-friendly walking paths.", 10),
            _ph("Premium Handpicked Hotels: Mayfair Lake Resort to royal heritage bungalows across 4 tiers.", 11),
            _ph("Shopping: Dhonkra bell-metal, Tussar silk, organic forest honey, terracotta crafts.", 12),
            _ph("Important Notes: Notify walking limitations during booking; book 45–60 days ahead for Chitrakote huts.", 13),
        ],
        moods=["Senior", "Leisure", "Culture", "Luxury", "Family"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note="On Request (Premium Luxury Tier)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Senior Citizen Leisure • Raipur • Sirpur • Jagdalpur • Chitrakote • 05 Nights / 06 Days",
        overview=(
            "Welcome to India's best-kept cultural secret. The absolute Best Chhattisgarh Tour Package, thoughtfully "
            "curated by TRAGUIN, invites distinguished senior guests to discover ancient archaeological wonders, deep "
            "tribal legacies, and magnificent waterfalls. This custom Luxury Chhattisgarh Holiday prioritizes absolute "
            "comfort, minimal walking distances, and smooth road transits.\n\n"
            "TOUR OVERVIEW\n"
            "This customized Chhattisgarh Family Tour delivers a wonderfully relaxing exploration tailored as a "
            "senior citizen-friendly journey. Guests travel in a private luxury vehicle with low ingress, empathetic "
            "guides, and highly comfortable premium properties. Route: Raipur (2N) ➔ Jagdalpur / Bastar (2N) ➔ "
            "Chitrakote Falls (1N) ➔ Raipur Departure.\n\n"
            "WHY CHOOSE THE PREMIUM LEISURE CHHATTISGARH TRAIL?\n"
            "Iconic Attractions: Laxman Temple at Sirpur, Chitrakote Waterfalls, Danteshwari Temple, and Kanger Valley. "
            "Senior Comfort Highlights: Premium ground transport, flat walking paths, accessible riverside resorts, and "
            "attentive medical standby support. Best Time: October to March for pleasant Chhattisgarh Sightseeing."
        ),
        seo_title="CG-005 | Senior Citizen Leisure Raipur Jagdalpur Chitrakote | TRAGUIN",
        seo_description="Premium 05 Nights / 06 Days senior-friendly Chhattisgarh tour (CG-005 / TG-CG-SCL-005): Sirpur, Chitrakote boat ride, Dhonkra art, and 4-tier accessible hotels.",
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Raipur arrival, Naya Raipur drive, and Budha Talab sunset on Day 01", 1),
            _ih("Sirpur Laxman Temple and Buddhist monasteries excursion on Day 02", 2),
            _ih("Raipur to Jagdalpur via Kondagaon Dhonkra village on Day 03", 3),
            _ih("Jagdalpur museum, Tirathgarh Falls, and Bastar Palace on Day 04", 4),
            _ih("Chitrakote Falls boat ride and illuminated waterfall dinner on Day 05", 5),
            _ih("Chitrakote to Raipur departure on Day 06", 6),
        ],
        days=[
            _day(1, "RAIPUR — ARRIVAL & STEP INTO PREMIUM RELAXATION", (
                "Your premium slow-paced journey begins at Raipur Airport or Railway Station. Your dedicated TRAGUIN "
                "chauffeur greets you with cold towels and mineral water. Transfer in your luxury SUV to a handpicked "
                "premium hotel with priority check-in and lower-level room assignments. After a relaxed lunch, enjoy a "
                "gentle panoramic drive across Naya Raipur. In the evening, visit Swami Vivekanand Sarovar (Budha Talab) "
                "for a quiet sunset walk along flat paved trails."
            ), ["Sightseeing Included: Naya Raipur panoramic drive, Swami Vivekanand Sarovar.", "Overnight Stay: Premium Luxury Hotel, Raipur.", "Meals Included: Welcome Refreshments & Chef-Curated Soft Dinner."]),
            _day(2, "SIRPUR — EXPLORING ANCIENT SPIRITUAL BRICK MASTERPIECES", (
                "Savor a relaxed breakfast before a comfortable day excursion to historic Sirpur. Visit the world-famous "
                "Laxman Temple with optimized entry paths avoiding strenuous climbs. Take a short electric golf-cart ride "
                "to Anand Prabhu Kudi Vihar, an ancient Buddhist monastery with a colossal serene Buddha statue. Enjoy "
                "a light lunch nearby before returning to Raipur for a leisure evening."
            ), ["Sightseeing Included: Sirpur Archaeological Site, Laxman Brick Temple, Buddhist Monasteries.", "Overnight Stay: Premium Luxury Hotel, Raipur.", "Meals Included: Buffet Breakfast & Selected Dinner."]),
            _day(3, "RAIPUR TO JAGDALPUR — JOURNEY TO THE TRIBAL HEARTLAND", (
                "Following breakfast, begin your scenic drive south toward Jagdalpur through dense sal forests and the "
                "scenic Keshkal Ghats. Stop at Kondagaon for a TRAGUIN Signature Experience: an exclusive interactive "
                "visit to a tribal workshop watching master craftsmen sculpt figures using the ancient lost-wax Dhonkra "
                "Bell-Metal method. Arrive in Jagdalpur by late afternoon and check into your heritage luxury hotel."
            ), ["Sightseeing Included: Keshkal Ghat viewpoint, Kondagaon Dhonkra craft village.", "Overnight Stay: Handpicked Premium Heritage Hotel, Jagdalpur.", "Meals Included: Breakfast, Mid-way Refreshments & Traditional Bastar Dinner."]),
            _day(4, "JAGDALPUR — TRIBAL ARTS, WOODED VALLEYS & ROYAL HISTORY", (
                "After breakfast, visit the Anthropological Museum showcasing Bastar's indigenous tribes. Drive to the "
                "Kanger Valley corridor for a short flat walk to view Tirathgarh Waterfalls. In the afternoon, visit "
                "Bastar Palace learning about the Kakatiya royal lineage. Browse the vibrant local village haat trading "
                "forest honey and handmade artifacts."
            ), ["Sightseeing Included: Bastar Anthropological Museum, Tirathgarh Falls, Bastar Royal Palace.", "Overnight Stay: Handpicked Premium Heritage Hotel, Jagdalpur.", "Meals Included: Premium Breakfast & Multi-cuisine Fine Dining Dinner."]),
            _day(5, "JAGDALPUR TO CHITRAKOTE — THE MAGNIFICENT HORSESHOE WATERFALL", (
                "Drive to majestic Chitrakote Waterfalls, the 300-meter-wide horseshoe called the Niagara Falls of India. "
                "Check into a luxury riverside eco-resort with veranda overlooking thundering waters. Enjoy a TRAGUIN "
                "Signature private boat ride along the calm lower river pool. Watch waterfalls light up under spotlights "
                "from premium viewing decks during a grand farewell dinner."
            ), ["Sightseeing Included: Chitrakote Horseshoe Falls, Indravati Riverfront viewpoints.", "Overnight Stay: Premium Luxury Riverside Eco-Resort, Chitrakote.", "Meals Included: Gourmet Breakfast, Riverside Lunch & Grand Farewell Dinner."]),
            _day(6, "CHITRAKOTE TO RAIPUR — DEPARTURE WITH TIMELESS MEMORIES", (
                "Indulge in a late relaxing breakfast on your veranda as morning rainbow forms over Chitrakote Falls. "
                "Complete check-out and settle into your premium SUV for the return drive to Raipur Airport or Railway "
                "Station, concluding your senior-friendly exploration with deep cultural enrichment."
            ), ["Sightseeing Included: Return scenic drive, private departure transfer.", "Meals Included: Premium Buffet Breakfast & Farewell Highway Lunch."]),
        ],
        hotels=[
            _hotel("Hotel Babylon Inn / Hyatt Raipur | MPT Naman Bastar Resort | MPT Chitrakote Log Huts", loc, "05 Nights", "Deluxe", "Deluxe Room", "Breakfast & Dinner", 4, 1, description=f"OPTION 01 – DELUXE: Hotel Babylon Inn / Hyatt Raipur (Raipur, 2 Nights) | MPT Naman Bastar Resort (Jagdalpur, 2 Nights) | MPT Chitrakote Log Huts (Chitrakote, 1 Night) | Breakfast & Dinner"),
            _hotel("Courtyard by Marriott Raipur | Asansol Heritage Resort Jagdalpur | Chitrakote Luxury River View Huts", loc, "05 Nights", "Premium", "Premium Room", "Breakfast & Dinner", 4, 2, description=f"OPTION 02 – PREMIUM: Courtyard by Marriott Raipur (Raipur, 2 Nights) | Asansol Heritage Resort Jagdalpur (Jagdalpur, 2 Nights) | Chitrakote Luxury River View Huts (Chitrakote, 1 Night) | Breakfast & Dinner"),
            _hotel("Sayaji Hotel Raipur | Grand Bastar Heritage Estate | Dandami Luxury Bison Resort", loc, "05 Nights", "Luxury", "Luxury Room", "Breakfast & Dinner", 5, 3, description=f"OPTION 03 – LUXURY: Sayaji Hotel Raipur (Raipur, 2 Nights) | Grand Bastar Heritage Estate (Jagdalpur, 2 Nights) | Dandami Luxury Bison Resort (Chitrakote, 1 Night) | Breakfast & Dinner"),
            _hotel("Mayfair Lake Resort Raipur | Bastar Palace Royal Suite Residence | Dandami Resort Premium Presidential Suite", loc, "05 Nights", "Ultra Luxury", "Luxury Suite", "Breakfast & Dinner", 5, 4, description=f"OPTION 04 – ULTRA LUXURY: Mayfair Lake Resort Raipur (Raipur, 2 Nights) | Bastar Palace Royal Suite Residence (Jagdalpur, 2 Nights) | Dandami Resort Premium Presidential Suite (Chitrakote, 1 Night) | Breakfast & Dinner"),
        ],
        inclusions=[
            _inc_included("Premium Stays: 05 Nights elite accommodation with ground floor/elevator accessibility.", 1),
            _inc_included("Gourmet Dining: Daily healthy breakfast and customized soft dinners.", 2),
            _inc_included("Luxury Transportation: AC Luxury SUV with dedicated chauffeur, tolls, fuel, parking.", 3),
            _inc_included("Elite Guiding: Government-approved historians at senior-friendly walking pace.", 4),
            _inc_included("TRAGUIN Signatures: Private boat excursion at Chitrakote and Dhonkra art demonstration.", 5),
            _inc_included("TRAGUIN Support: 24/7 dedicated virtual concierge with priority senior assistance.", 6),
            _inc_excluded("Commercial flights or train fares to and from Raipur.", 7),
            _inc_excluded("Monument entry tickets, camera permits, personal expenses.", 8),
            _inc_excluded("Optional adventure water rides not explicitly stated.", 9),
        ],
    )
    return package, itinerary


def build_cg_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "CG-006"
    tour_code = "TG-CG-THT-006"
    title = (
        "TRAGUIN Premium Chhattisgarh Tour Package — Tribal Heritage Trail • "
        "Sirpur • Jagdalpur • Bastar Heartland"
    )
    duration = "05 Nights / 06 Days"
    slug = "cg-006-tribal-heritage-sirpur-jagdalpur-chitrakote"
    itin_slug = "cg-006-tribal-heritage-sirpur-jagdalpur-chitrakote-itinerary"
    loc = "Raipur (1 Night) / Jagdalpur (3 Nights) / Chitrakote (1 Night)"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Chhattisgarh / India | Category: Premium Tribal Heritage Tour", 2),
            _ph("Destinations: Raipur • Sirpur • Jagdalpur (Bastar) • Chitrakote", 3),
            _ph("Ideal for: Families, Cultural Explorers & Heritage Connoisseurs", 4),
            _ph("Best season: October to March (Pleasant forest canopies)", 5),
            _ph("Starting price: On Request (Premium Luxury Tier)", 6),
            _ph("Vehicle: Private AC Luxury SUV (Innova Crysta) | Meal Plan: Premium MAPAI", 7),
            _ph("Route Plan: Raipur (1N) ➔ Sirpur ➔ Jagdalpur / Bastar (3N) ➔ Chitrakote (1N) ➔ Raipur Departure", 8),
            _ph("TRAGUIN Signature Experience: Scholar-led Sirpur walks and private sunset boat cruise at Chitrakote.", 9),
            _ph("Curated by TRAGUIN Experts: Hands-on lost-wax metal modeling with royal tribal masters.", 10),
            _ph("Premium Handpicked Hotels: 4-tier properties from Babylon Inn to Bastar Palace Royal Suite.", 11),
            _ph("Shopping: Dhonkra art, Tussar silk, organic forest honey, terracotta crafts.", 12),
            _ph("Important Notes: Conservative attire at temples; book 45–60 days ahead for Chitrakote riverside huts.", 13),
        ],
        moods=["Heritage", "Tribal", "Culture", "Family", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note="On Request (Premium Luxury Tier)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Tribal Heritage Trail • Sirpur • Jagdalpur • Chitrakote • 05 Nights / 06 Days",
        overview=(
            "Welcome to the mesmerizing ancient heartland of Tribal India. The definitive Best Chhattisgarh Tour Package, "
            "masterfully orchestrated by TRAGUIN, guides your family across archaeological ruins and living communities "
            "preserving age-old traditions deep within vast sal forests.\n\n"
            "TOUR OVERVIEW\n"
            "This premium Chhattisgarh Family Tour delivers incomparable cultural immersion across the legendary Bastar "
            "region. Guests enjoy private transportation, handpicked heritage hotels, expert cultural guides, and "
            "exclusive village interaction permits. Route: Raipur (1N) ➔ Sirpur Excursion ➔ Jagdalpur / Bastar (3N) ➔ "
            "Chitrakote (1N) ➔ Raipur Departure.\n\n"
            "WHY CHOOSE THE PREMIUM TRIBAL CHHATTISGARH TRAIL?\n"
            "Iconic Attractions: Laxman Temple Sirpur, Bastar Palace, Chitrakote Falls, Kotumsar Caves. Most Searched "
            "Experiences: Weekly tribal haats, lost-wax metal casting, Maria tribal dance. Best Time: October to March."
        ),
        seo_title="CG-006 | Tribal Heritage Sirpur Jagdalpur Chitrakote | TRAGUIN",
        seo_description="Premium 05 Nights / 06 Days tribal heritage tour (CG-006 / TG-CG-THT-006): Sirpur, Bastar haats, Kotumsar Caves, Chitrakote boat ride, and 4-tier hotels.",
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Raipur to Sirpur Laxman Temple and Buddhist monasteries on Day 01", 1),
            _ih("Raipur to Jagdalpur via Kondagaon Dhonkra workshop on Day 02", 2),
            _ih("Weekly tribal haats and Anthropological Museum on Day 03", 3),
            _ih("Kotumsar Caves and Tirathgarh Cascades on Day 04", 4),
            _ih("Chitrakote Falls boat ride and illuminated dinner on Day 05", 5),
            _ih("Chitrakote to Raipur departure on Day 06", 6),
        ],
        days=[
            _day(1, "RAIPUR TO SIRPUR — ARCHAEOLOGICAL MARVELS & ANCIENT MONASTERIES", (
                "Arrive at Raipur and board your luxury SUV toward historical Sirpur on the Mahanadi River. Explore the "
                "magnificent Laxman Temple with your private scholar guide, then Anand Prabhu Kudi Vihar Buddhist ruins. "
                "Drive back to Raipur for a handpicked premium resort stay and gourmet regional dinner."
            ), ["Sightseeing Included: Sirpur Archeological Complex, Laxman Brick Temple, Buddhist Monastic ruins.", "Overnight Stay: Premium Luxury Resort, Raipur.", "Meals Included: Welcome Signature Drink & Gourmet Dinner."]),
            _day(2, "RAIPUR TO JAGDALPUR — JOURNEY INTO THE BASTAR TRIBAL KINGDOM", (
                "Drive south toward Jagdalpur through Keshkal Ghats. Stop at Kondagaon for a TRAGUIN Signature "
                "interactive tour inside a family workshop demonstrating Dhonkra Bell-Metal casting. Check into "
                "authentic heritage hotel properties in Jagdalpur."
            ), ["Sightseeing Included: Keshkal Ghats drive, Kondagaon Dhonkra metal craft village.", "Overnight Stay: Handpicked Premium Heritage Hotel, Jagdalpur.", "Meals Included: Buffet Breakfast & Traditional Bastar Palace-style Dinner."]),
            _day(3, "JAGDALPUR — WEEKLY TRIBAL HAATS & ANTHROPOLOGICAL TREASURES", (
                "Visit the Anthropological Museum, then access a colorful weekly Bastar Haat with your local guide among "
                "Gond, Maria, and Bhatra tribes trading forest honey and handcrafted works. View Bastar Palace "
                "architecture before an evening of relaxation at your premium resort."
            ), ["Sightseeing Included: Bastar Anthropological Museum, Weekly Tribal Market, Jagdalpur Royal Palace.", "Overnight Stay: Handpicked Premium Heritage Hotel, Jagdalpur.", "Meals Included: Premium Breakfast & Multi-cuisine Fine Dining Dinner."]),
            _day(4, "KANGER VALLEY — SUBTERRANEAN CAVES & TIRATHGARH CASCADES", (
                "Drive into Kanger Valley National Park to Kotumsar Caves with specialized headlamps viewing stalactites "
                "and blind cave-fish pools. Visit Tirathgarh Waterfalls splitting into multiple steps over rugged stone. "
                "Enjoy a prepared outdoor family picnic lunch near terracotta artisan clusters."
            ), ["Sightseeing Included: Kotumsar Caves, Tirathgarh Waterfalls, Terracotta artisan village.", "Overnight Stay: Handpicked Premium Heritage Hotel, Jagdalpur.", "Meals Included: Breakfast, Custom Picnic Lunch & Regional Dinner."]),
            _day(5, "JAGDALPUR TO CHITRAKOTE — THE MAGNIFICENT NIAGARA OF INDIA", (
                "Drive to Chitrakote Waterfalls and check into a luxury riverside eco-resort. Enjoy a TRAGUIN Signature "
                "private boat ride along the calm lower river pool. Watch illuminated waterfalls from premium viewing "
                "decks during a grand farewell celebration dinner."
            ), ["Sightseeing Included: Chitrakote Horseshoe Falls, Indravati Riverfront viewpoints.", "Overnight Stay: Premium Luxury Riverside Eco-Resort, Chitrakote.", "Meals Included: Gourmet Breakfast, Riverside Lunch & Grand Farewell Dinner."]),
            _day(6, "CHITRAKOTE TO RAIPUR — DEPARTURE WITH TIMELESS MEMORIES", (
                "Late relaxing breakfast on your veranda overlooking Chitrakote Falls mist. Return drive to Raipur with "
                "elegant highway lunch before airport or railway departure."
            ), ["Sightseeing Included: Return scenic drive, private departure transfer.", "Meals Included: Premium Buffet Breakfast & Farewell Highway Lunch."]),
        ],
        hotels=[
            _hotel("Hotel Babylon Inn / Hyatt Raipur | MPT Naman Bastar Resort | MPT Chitrakote Log Huts", loc, "05 Nights", "Deluxe", "Deluxe Room", "Breakfast & Dinner", 4, 1, description=f"OPTION 01 – DELUXE: Hotel Babylon Inn / Hyatt Raipur (Raipur, 1 Night) | MPT Naman Bastar Resort (Jagdalpur, 3 Nights) | MPT Chitrakote Log Huts (Chitrakote, 1 Night) | Breakfast & Dinner"),
            _hotel("Courtyard by Marriott Raipur | Asansol Heritage Resort Jagdalpur | Chitrakote Luxury River View Huts", loc, "05 Nights", "Premium", "Premium Room", "Breakfast & Dinner", 4, 2, description=f"OPTION 02 – PREMIUM: Courtyard by Marriott Raipur (Raipur, 1 Night) | Asansol Heritage Resort Jagdalpur (Jagdalpur, 3 Nights) | Chitrakote Luxury River View Huts (Chitrakote, 1 Night) | Breakfast & Dinner"),
            _hotel("Sayaji Hotel Raipur | Grand Bastar Heritage Estate | Dandami Luxury Bison Resort", loc, "05 Nights", "Luxury", "Luxury Room", "Breakfast & Dinner", 5, 3, description=f"OPTION 03 – LUXURY: Sayaji Hotel Raipur (Raipur, 1 Night) | Grand Bastar Heritage Estate (Jagdalpur, 3 Nights) | Dandami Luxury Bison Resort (Chitrakote, 1 Night) | Breakfast & Dinner"),
            _hotel("Mayfair Lake Resort Raipur | Bastar Palace Royal Suite Residence | Dandami Resort Premium Presidential Suite", loc, "05 Nights", "Ultra Luxury", "Luxury Suite", "Breakfast & Dinner", 5, 4, description=f"OPTION 04 – ULTRA LUXURY: Mayfair Lake Resort Raipur (Raipur, 1 Night) | Bastar Palace Royal Suite Residence (Jagdalpur, 3 Nights) | Dandami Resort Premium Presidential Suite (Chitrakote, 1 Night) | Breakfast & Dinner"),
        ],
        inclusions=[
            _inc_included("Premium Stays: 05 Nights elite accommodation at handpicked properties.", 1),
            _inc_included("Gourmet Dining: Daily breakfast and customized dinners.", 2),
            _inc_included("Luxury Transportation: Private AC Luxury SUV with dedicated chauffeur.", 3),
            _inc_included("Elite Guiding: Government-approved local historians and cultural guides.", 4),
            _inc_included("TRAGUIN Signatures: Private boat excursion at Chitrakote and Dhonkra demonstration.", 5),
            _inc_included("TRAGUIN Support: 24/7 dedicated virtual concierge support.", 6),
            _inc_excluded("Commercial flights or train fares to and from Raipur.", 7),
            _inc_excluded("Monument fees, camera permits, personal expenses.", 8),
            _inc_excluded("Optional activities not explicitly stated.", 9),
        ],
    )
    return package, itinerary


def build_cg_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "CG-007"
    tour_code = "TG-CG-EDU-007"
    title = (
        "TRAGUIN Premium Chhattisgarh Tour Package — Educational Bastar Experience • "
        "Anthropology, Art & Geography"
    )
    duration = "04 Nights / 05 Days"
    slug = "cg-007-educational-bastar-raipur-kondagaon-chitrakote"
    itin_slug = "cg-007-educational-bastar-raipur-kondagaon-chitrakote-itinerary"
    loc = "Raipur (1 Night) / Jagdalpur (2 Nights) / Chitrakote (1 Night)"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Chhattisgarh / India | Category: School / Educational Group Tour", 2),
            _ph("Destinations: Raipur • Kondagaon • Jagdalpur • Chitrakote", 3),
            _ph("Ideal for: Students, Educators & Academic Groups", 4),
            _ph("Best season: October to March (Excellent for field studies)", 5),
            _ph("Starting price: On Request (Premium Group Tier)", 6),
            _ph("Vehicle: Private AC Luxury Coaches (GPS & Attendant) | Meal Plan: Premium Buffet Plan", 7),
            _ph("Route Plan: Raipur Arrival ➔ Kondagaon ➔ Jagdalpur / Bastar (2N) ➔ Chitrakote (1N) ➔ Raipur Departure", 8),
            _ph("TRAGUIN Signature Experience: Hands-on wax-moulding workshop with National Award-winning Dhonkra artisans.", 9),
            _ph("Curated by TRAGUIN Experts: Field study workbooks and campfire tribal folk dance presentation.", 10),
            _ph("Premium Handpicked Hotels: Student floor partitions with rigorous security and hygiene standards.", 11),
            _ph("Shopping: Dhonkra miniatures, terracotta crafts, forest honey, Tussar weaving centers.", 12),
            _ph("Important Notes: Share student rosters 30 days prior; book Chitrakote rooms 60–90 days ahead.", 13),
        ],
        moods=["Educational", "Culture", "Nature", "Group"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note="On Request (Premium Group Tier)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Educational Bastar • Raipur • Kondagaon • Jagdalpur • Chitrakote • 04 Nights / 05 Days",
        overview=(
            "Welcome to a living classroom like no other. The definitive Best Chhattisgarh Tour Package, engineered by "
            "TRAGUIN, invites young minds to discover ancient history, indigenous arts, and magnificent geographical "
            "wonders optimized for learning outcomes and team safety.\n\n"
            "TOUR OVERVIEW\n"
            "The Educational Bastar field expedition covers historical, anthropological, and geographical landmarks of "
            "southern Chhattisgarh over 5 days. Private luxury coach transportation with strict safety protocols, expert "
            "destination handlers, and wholesome dietary meal planning throughout.\n\n"
            "WHY CHOOSE THE PREMIUM EDUCATIONAL BASTAR FIELD STUDY?\n"
            "Iconic Attractions: Chitrakote Waterfalls, Anthropological Museum, Kanger Valley ecosystems. Student "
            "Safety Highlights: Verified premium hotels with separate student wings, multi-vehicle tracking, onboard "
            "first-aid support. Best Time: October to March for field walks and group data logging."
        ),
        seo_title="CG-007 | Educational Bastar Raipur Kondagaon Chitrakote | TRAGUIN",
        seo_description="Premium 04 Nights / 05 Days educational Bastar tour (CG-007 / TG-CG-EDU-007): Dhonkra workshop, anthropological fieldwork, Chitrakote hydro-geography, and 4-tier group hotels.",
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Raipur arrival, Purkhouti Muktangan museum orientation on Day 01", 1),
            _ih("Kondagaon Dhonkra bell-metal hands-on workshop on Day 02", 2),
            _ih("Anthropological Museum and Bastar Palace fieldwork on Day 03", 3),
            _ih("Chitrakote hydro-geography boat study and tribal folk dance on Day 04", 4),
            _ih("Chitrakote to Raipur group departure on Day 05", 5),
        ],
        days=[
            _day(1, "RAIPUR ARRIVAL — ORIENTATION & MODERN CHHATTISGARH STUDY", (
                "Student group arrives at Raipur and is received by TRAGUIN tour coordinators. Transfer to premium group "
                "hotel for safety briefing and orientation on Bastar tribal anthropology. Afternoon panoramic drive "
                "across Naya Raipur and visit Purkhouti Muktangan open-air museum displaying tribal architecture models."
            ), ["Sightseeing Included: Naya Raipur architectural drive, Purkhouti Muktangan Museum.", "Overnight Stay: Premium Luxury Group Hotel, Raipur.", "Meals Included: Welcome Group Drinks, Buffet Lunch & Wholesome Dinner."]),
            _day(2, "RAIPUR TO JAGDALPUR — THE DHONKRA BELL-METAL CRAFT KILNS OF KONDAGAON", (
                "Board luxury coaches heading south through Keshkal Ghat hills. Arrive at Kondagaon for a TRAGUIN "
                "Signature interactive workshop where National Award-winning artisans demonstrate lost-wax Dhonkra "
                "Bell-Metal technique. Students get hands-on experience shaping clay core designs before arriving "
                "in Jagdalpur."
            ), ["Sightseeing Included: Keshkal Ghat geographical pass, Kondagaon Dhonkra workshops.", "Overnight Stay: Handpicked Premium Hotel, Jagdalpur.", "Meals Included: Full Buffet Breakfast, Hot Highway Lunch & Wholesome Dinner."]),
            _day(3, "JAGDALPUR — ANTHROPOLOGICAL FIELDWORK & TRIBAL DYNASTIC RECORDS", (
                "Begin at the Anthropological Museum with custom field study worksheets documenting Maria, Muria, and "
                "Bhatra cultures. Visit Bastar Palace analyzing regional and colonial architectural elements. Participate "
                "in an immersive experience with local youth leaders on forest resource conservation methods."
            ), ["Sightseeing Included: Bastar Anthropological Museum, Bastar Royal Palace historical tour.", "Overnight Stay: Handpicked Premium Hotel, Jagdalpur.", "Meals Included: Premium Breakfast, Group Lunch & Multi-cuisine Dinner."]),
            _day(4, "JAGDALPUR TO CHITRAKOTE — HYDRO-GEOGRAPHY OF THE NIAGARA OF INDIA", (
                "Drive to Chitrakote Waterfalls spanning nearly 300 meters during peak flow. Geography handlers guide "
                "students along safe terraced paths analyzing erosion patterns. Enjoy a safe private boat excursion "
                "across the calm lower pool. Evening campfire with traditional tribal folk dances by native youth groups."
            ), ["Sightseeing Included: Chitrakote Horseshoe Falls canyon, Indravati River basin paths.", "Overnight Stay: Premium Luxury Riverside Eco-Resort, Chitrakote.", "Meals Included: Buffet Breakfast, Resort Lunch & Festive Farewell Dinner."]),
            _day(5, "CHITRAKOTE TO RAIPUR — DATA LOGGING & FINAL DEPARTURE", (
                "Catch morning rainbow over Chitrakote Falls mist. Return journey north to Raipur with farewell group "
                "lunch along the highway. Arrive at Raipur Airport or Railway Station for institutional departures."
            ), ["Sightseeing Included: Return scenic highway transit, private group transfer.", "Meals Included: Full Buffet Breakfast & Farewell Group Highway Lunch."]),
        ],
        hotels=[
            _hotel("Hotel Babylon Inn / Hyatt Raipur | MPT Naman Bastar Resort | MPT Chitrakote Log Huts", loc, "04 Nights", "Deluxe", "Triple Share", "Triple Share Buffet", 4, 1, description=f"OPTION 01 – DELUXE: Hotel Babylon Inn / Hyatt Raipur (Raipur, 1 Night) | MPT Naman Bastar Resort (Jagdalpur, 2 Nights) | MPT Chitrakote Log Huts (Chitrakote, 1 Night) | Triple Share Buffet"),
            _hotel("Courtyard by Marriott Raipur | Asansol Heritage Resort | Chitrakote River View Huts", loc, "04 Nights", "Premium", "Triple Share", "Triple Share Buffet", 4, 2, description=f"OPTION 02 – PREMIUM: Courtyard by Marriott Raipur (Raipur, 1 Night) | Asansol Heritage Resort (Jagdalpur, 2 Nights) | Chitrakote River View Huts (Chitrakote, 1 Night) | Triple Share Buffet"),
            _hotel("Sayaji Hotel Raipur | Grand Bastar Heritage Estate | Dandami Luxury Bison Resort", loc, "04 Nights", "Luxury", "Twin Share Premium", "Twin Share Premium", 5, 3, description=f"OPTION 03 – LUXURY: Sayaji Hotel Raipur (Raipur, 1 Night) | Grand Bastar Heritage Estate (Jagdalpur, 2 Nights) | Dandami Luxury Bison Resort (Chitrakote, 1 Night) | Twin Share Premium"),
            _hotel("Mayfair Lake Resort Raipur | Bastar Palace Royal Residences | Dandami Resort Executive Suites", loc, "04 Nights", "Ultra Luxury", "Twin Share Premium", "Twin Share Premium", 5, 4, description=f"OPTION 04 – ULTRA LUXURY: Mayfair Lake Resort Raipur (Raipur, 1 Night) | Bastar Palace Royal Residences (Jagdalpur, 2 Nights) | Dandami Resort Executive Suites (Chitrakote, 1 Night) | Twin Share Premium"),
        ],
        inclusions=[
            _inc_included("Premium Stays: 04 Nights with dedicated student floor partitions.", 1),
            _inc_included("Wholesome Catering: All buffet breakfasts, lunches, and nutritious dinners.", 2),
            _inc_included("Luxury Group Transit: Private AC coaches with GPS tracking and school-vetted drivers.", 3),
            _inc_included("Academic Handlers: Local historians, tribal guides, and interactive worksheets.", 4),
            _inc_included("TRAGUIN Signatures: Dhonkra moulding masterclass and campfire tribal dance.", 5),
            _inc_included("TRAGUIN Support: 24/7 support with onboard safety manager.", 6),
            _inc_excluded("Train or flight tickets from institutional hubs to Raipur.", 7),
            _inc_excluded("Personal items, optional activities, and travel insurance.", 8),
        ],
    )
    return package, itinerary

def build_cg_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "CG-008"
    tour_code = "TG-CG-CMP-008"
    title = (
        "TRAGUIN Premium Chhattisgarh Tour Package — Complete Expedition • "
        "Temples, Tribes & Waterfalls"
    )
    duration = "06 Nights / 07 Days"
    slug = "cg-008-complete-chhattisgarh-raipur-sirpur-mainpat"
    itin_slug = "cg-008-complete-chhattisgarh-raipur-sirpur-mainpat-itinerary"
    loc = "Raipur (1 Night) / Jagdalpur (2 Nights) / Chitrakote (1 Night) / Mainpat (2 Nights)"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Chhattisgarh / India | Category: Complete Luxury Family Tour", 2),
            _ph("Destinations: Raipur • Sirpur • Jagdalpur • Chitrakote • Mainpat", 3),
            _ph("Ideal for: Families, Culture Seekers & Nature Lovers", 4),
            _ph("Best season: October to March (Delightfully cool)", 5),
            _ph("Starting price: On Request (Premium Luxury Tier)", 6),
            _ph("Vehicle: Private AC Luxury SUV (Innova Crysta) | Meal Plan: Premium MAPAI", 7),
            _ph("Route Plan: Raipur (1N) ➔ Sirpur ➔ Jagdalpur (2N) ➔ Chitrakote (1N) ➔ Mainpat (2N) ➔ Raipur Departure", 8),
            _ph("TRAGUIN Signature Experience: Sunset boat cruise at Chitrakote and Mehta Point family high tea.", 9),
            _ph("Curated by TRAGUIN Experts: Dhonkra artisan interaction and Mainpat Tibetan monastery visit.", 10),
            _ph("Premium Handpicked Hotels: 4-tier properties from Hyatt to Mainpat Highlands Luxury Resort.", 11),
            _ph("Shopping: Dhonkra art, Tussar silk, Tibetan handicrafts, highland organic honey.", 12),
            _ph("Important Notes: Carry light woolens for Mainpat; book Chitrakote and Mainpat 45–60 days ahead.", 13),
        ],
        moods=["Family", "Culture", "Nature", "Luxury", "Complete"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note="On Request (Premium Luxury Tier)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Complete Chhattisgarh • Raipur • Sirpur • Jagdalpur • Chitrakote • Mainpat • 06 Nights / 07 Days",
        overview=(
            "Welcome to the raw, magical, and undiscovered heart of India. The definitive Best Chhattisgarh Tour Package "
            "by TRAGUIN invites your loved ones to dive deep into prehistoric heritage, pristine river valleys, and "
            "spectacular tribal folklore across a complete grand loop.\n\n"
            "TOUR OVERVIEW\n"
            "The Complete Chhattisgarh itinerary encapsulates Sirpur's architectural legacy, Chitrakote's majestic "
            "thunders, Jagdalpur's indigenous art worlds, and Mainpat's mist-laden green plateaus — the Shimla of "
            "Chhattisgarh. Private luxury SUV, elite local chroniclers, and impeccable concierge attention throughout.\n\n"
            "WHY CHOOSE THE PREMIUM COMPLETE CHHATTISGARH FAMILY TOUR?\n"
            "Famous Attractions: Laxman Temple Sirpur, Chitrakote Waterfalls, Danteshwari Temple, Mainpat hills. "
            "Popular Instagram Locations: Sirpur red-brick ruins, Chitrakote horseshoe edge, Tiger Point Mainpat. "
            "Best Time: October to March for extensive Chhattisgarh Sightseeing."
        ),
        seo_title="CG-008 | Complete Chhattisgarh Raipur Sirpur Mainpat | TRAGUIN",
        seo_description="Premium 06 Nights / 07 Days complete Chhattisgarh tour (CG-008 / TG-CG-CMP-008): Sirpur, Chitrakote, Kanger Valley, Mainpat Zaljali, and 4-tier hotels.",
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Raipur arrival, Purkhouti Muktangan, and Budha Talab on Day 01", 1),
            _ih("Sirpur Laxman Temple and drive to Jagdalpur via Kondagaon on Day 02", 2),
            _ih("Kanger Valley, Tirathgarh Falls, and tribal haat on Day 03", 3),
            _ih("Chitrakote Falls private boat ride on Day 04", 4),
            _ih("Mainpat plateau and Dhammapada Tibetan Monastery on Day 05", 5),
            _ih("Zaljali Shaking Earth, Tiger Point, and Mehta Point high tea on Day 06", 6),
            _ih("Mainpat to Raipur departure on Day 07", 7),
        ],
        days=[
            _day(1, "RAIPUR — ARRIVAL & ENTRY INTO THE MODERN CAPITAL GATEWAY", (
                "Land at Raipur and receive welcome kits from your TRAGUIN chauffeur. Transfer to premium hotel. "
                "Explore Naya Raipur, visit Swami Vivekanand Sarovar for sunset walk, and tour Purkhauti Muktangan "
                "open-air museum detailing tribal architecture and art forms. Return for gourmet welcome dinner."
            ), ["Sightseeing Included: Naya Raipur drive, Swami Vivekanand Sarovar, Purkhauti Muktangan.", "Overnight Stay: Premium Luxury Hotel, Raipur.", "Meals Included: Welcome Signature Drinks & Gourmet Dinner."]),
            _day(2, "SIRPUR ARCHAEOLOGICAL SITE TO JAGDALPUR — THE TRIBAL HEARTLAND", (
                "Drive to Sirpur's iconic Laxman Temple and Anand Prabhu Kudi Vihar Buddhist monastery. Continue "
                "south through Keshkal Ghats to Kondagaon for TRAGUIN Signature Dhonkra bell-metal workshop visit. "
                "Arrive Jagdalpur evening and check into premium heritage hotel."
            ), ["Sightseeing Included: Laxman Temple, Buddhist Monasteries, Kondagaon craft village.", "Overnight Stay: Handpicked Premium Heritage Hotel, Jagdalpur.", "Meals Included: Buffet Breakfast & Authentic Bastar Dinner."]),
            _day(3, "JAGDALPUR — DEEP FOREST CANYONS & INDIGENOUS LOCAL MARKETS", (
                "Enter Kanger Valley National Park for Tirathgarh Waterfalls splitting into silver streams. Visit "
                "Anthropological Museum and vibrant local village Haat trading forest honey and handmade crafts."
            ), ["Sightseeing Included: Kanger Valley, Tirathgarh Falls, Anthropological Museum, Tribal Market.", "Overnight Stay: Handpicked Premium Heritage Hotel, Jagdalpur.", "Meals Included: Premium Breakfast & Multi-cuisine Dinner."]),
            _day(4, "JAGDALPUR TO CHITRAKOTE — THE MAJESTIC HORSESHOE FALLS", (
                "Drive to spectacular Chitrakote Waterfalls — the Niagara of India. Check into luxury riverside eco-resort. "
                "Enjoy TRAGUIN Signature private boat ride on calm lower river pool. Watch illuminated waterfalls during "
                "grand festive dinner."
            ), ["Sightseeing Included: Chitrakote Horseshoe Falls, Indravati Riverfront viewpoints.", "Overnight Stay: Premium Luxury Riverside Eco-Resort, Chitrakote.", "Meals Included: Gourmet Breakfast, Riverside Lunch & Grand Theme Dinner."]),
            _day(5, "CHITRAKOTE TO MAINPAT — ASCENDING THE MISTY GREEN PLATEAU", (
                "Morning rainbow over Chitrakote mist before heading north to Mainpat plateau at 3,500 feet. Check into "
                "luxury mountain resort. Visit serene Dhammapada Tibetan Monastery with colorful prayer flags. Enjoy "
                "cozy campfire dinner."
            ), ["Sightseeing Included: Highlands drive, Dhammapada Tibetan Monastery.", "Overnight Stay: Luxury Mountain View Resort, Mainpat.", "Meals Included: Breakfast & Curated Highlands Dinner."]),
            _day(6, "MAINPAT — SHAKING EARTH, TIGER POINTS & SCENIC VALLEYS", (
                "Explore Zaljali bouncing meadow where mossy earth shakes beneath your feet. Visit Tiger Point and Fish "
                "Point waterfalls with hanging bridge views. TRAGUIN Highlight: premium family high tea at Mehta Point "
                "with panoramic hill views and grand farewell dinner."
            ), ["Sightseeing Included: Zaljali Shaking Earth, Tiger Point, Fish Point, Mehta Point.", "Overnight Stay: Luxury Mountain View Resort, Mainpat.", "Meals Included: Gourmet Breakfast, Picnic High Tea & Grand Farewell Dinner."]),
            _day(7, "MAINPAT TO RAIPUR — DEPARTURE WITH LIFELONG FAMILY MEMORIES", (
                "Final breakfast on resort balcony overlooking valley hills. Smooth descent drive to Raipur with highway "
                "lunch before airport or railway departure."
            ), ["Sightseeing Included: Return mountain descent, private transfer.", "Meals Included: Premium Buffet Breakfast & Farewell Highway Lunch."]),
        ],
        hotels=[
            _hotel("Hyatt Raipur | MPT Naman Bastar | MPT Chitrakote Log Huts | MPT Mercury Resort", loc, "06 Nights", "Deluxe", "Deluxe Room", "MAPAI (Breakfast & Dinner)", 4, 1, description=f"OPTION 01 – DELUXE: Hyatt Raipur (Raipur, 1 Night) | MPT Naman Bastar (Jagdalpur, 2 Nights) | MPT Chitrakote Log Huts (Chitrakote, 1 Night) | MPT Mercury Resort (Mainpat, 2 Nights) | MAPAI"),
            _hotel("Courtyard by Marriott | Asansol Heritage Resort | Chitrakote Luxury Huts | Mainpat Eco Resort", loc, "06 Nights", "Premium", "Premium Room", "MAPAI (Breakfast & Dinner)", 4, 2, description=f"OPTION 02 – PREMIUM: Courtyard by Marriott (Raipur, 1 Night) | Asansol Heritage Resort (Jagdalpur, 2 Nights) | Chitrakote Luxury Huts (Chitrakote, 1 Night) | Mainpat Eco Resort (Mainpat, 2 Nights) | MAPAI"),
            _hotel("Sayaji Hotel Raipur | Grand Bastar Heritage | Dandami Luxury Resort | Shailly Valley Resort", loc, "06 Nights", "Luxury", "Luxury Room", "MAPAI (Breakfast & Dinner)", 5, 3, description=f"OPTION 03 – LUXURY: Sayaji Hotel Raipur (Raipur, 1 Night) | Grand Bastar Heritage (Jagdalpur, 2 Nights) | Dandami Luxury Resort (Chitrakote, 1 Night) | Shailly Valley Resort (Mainpat, 2 Nights) | MAPAI"),
            _hotel("Mayfair Lake Resort | Bastar Palace Suite | Dandami Presidential Suite | The Mainpat Highlands Luxury Resort", loc, "06 Nights", "Ultra Luxury", "Luxury Suite", "MAPAI (Breakfast & Dinner)", 5, 4, description=f"OPTION 04 – ULTRA LUXURY: Mayfair Lake Resort (Raipur, 1 Night) | Bastar Palace Suite (Jagdalpur, 2 Nights) | Dandami Presidential Suite (Chitrakote, 1 Night) | The Mainpat Highlands Luxury Resort (Mainpat, 2 Nights) | MAPAI"),
        ],
        inclusions=[
            _inc_included("Premium Stays: 06 Nights at handpicked hotels, eco-resorts, and mountain lodges.", 1),
            _inc_included("Gourmet Dining: Daily breakfast and executive dinners across all properties.", 2),
            _inc_included("Luxury Transportation: Private Innova Crysta for all transfers and sightseeing.", 3),
            _inc_included("Elite Guiding: Government-approved historians at archaeological and tribal sites.", 4),
            _inc_included("TRAGUIN Signatures: Chitrakote boat excursion and Mehta Point family high tea.", 5),
            _inc_included("TRAGUIN Support: 24/7 dedicated holiday specialists with covered tolls and fuel.", 6),
            _inc_excluded("Commercial flights or train fares to and from Raipur.", 7),
            _inc_excluded("Monument entry tickets, camera permits, personal expenses.", 8),
            _inc_excluded("Optional activities not explicitly stated.", 9),
        ],
    )
    return package, itinerary


def build_cg_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "CG-009"
    tour_code = "TG-CG-WFA-009"
    title = (
        "TRAGUIN Premium Chhattisgarh Tour Package — Great Waterfalls Adventure • "
        "Chitrakote • Tirathgarh • Tamra Gumar"
    )
    duration = "05 Nights / 06 Days"
    slug = "cg-009-waterfalls-adventure-chitrakote-jagdalpur"
    itin_slug = "cg-009-waterfalls-adventure-chitrakote-jagdalpur-itinerary"
    loc = "Raipur (1 Night) / Chitrakote (2 Nights) / Jagdalpur (2 Nights)"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Chhattisgarh / India | Category: Premium Adventure & Nature Tour", 2),
            _ph("Destinations: Raipur • Chitrakote • Tirathgarh • Tamra Gumar", 3),
            _ph("Ideal for: Adventure Seekers, Couples & Nature Enthusiasts", 4),
            _ph("Best season: July to March (Monsoons host spectacular roaring volumes)", 5),
            _ph("Starting price: On Request (Premium Luxury Tier)", 6),
            _ph("Vehicle: Private AC Luxury SUV (Innova Crysta / Fortuner 4x4) | Meal Plan: Premium MAPAI", 7),
            _ph("Route Plan: Raipur Arrival ➔ Chitrakote Falls (2N) ➔ Jagdalpur / Kanger Valley (2N) ➔ Raipur Departure", 8),
            _ph("TRAGUIN Signature Experience: Rapid basin boating into Chitrakote mist and Kutumsar cave navigation.", 9),
            _ph("Curated by TRAGUIN Experts: Private riverside tribal barbecue on Indravati River banks.", 10),
            _ph("Premium Handpicked Hotels: 4-tier riverside eco-lodges and heritage palace wings.", 11),
            _ph("Shopping: Dhonkra metal craft, Kosa silk, organic forest honey, Bastar wood craft.", 12),
            _ph("Important Notes: Non-slip trekking shoes mandatory; valid photo ID for national park entry.", 13),
        ],
        moods=["Adventure", "Waterfalls", "Nature", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note="On Request (Premium Luxury Tier)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Great Waterfalls Adventure • Chitrakote • Tirathgarh • Kanger Valley • 05 Nights / 06 Days",
        overview=(
            "Welcome to the untamed, pulsating wilderness of India's greenest eco-corridor. The definitive Best "
            "Chhattisgarh Tour Package by TRAGUIN invites adrenaline seekers to witness monumental liquid thunder "
            "across pristine river valleys and dense tribal woodlands.\n\n"
            "TOUR OVERVIEW\n"
            "The Waterfalls of Chhattisgarh signature package is the ultimate Chhattisgarh Adventure trail. Track "
            "Chitrakote's colossal horseshoe, Tirathgarh's multi-tiered limestone steps, and hidden jungle gems like "
            "Tamra Gumar and Mendri Gumar. Private luxury SUV, riverside eco-lodges, and expert jungle escorts.\n\n"
            "WHY UNDERTAKE THE GREAT CHHATTISGARH WATERFALL ADVENTURE?\n"
            "Iconic Attractions: 300-meter Chitrakote curtain, Tirathgarh tiers, Tamra Gumar ravines, Kutumsar Caves. "
            "Best Time: July to March when river volumes peak dramatically for spectacular Chhattisgarh Sightseeing."
        ),
        seo_title="CG-009 | Waterfalls Adventure Chitrakote Jagdalpur | TRAGUIN",
        seo_description="Premium 05 Nights / 06 Days waterfalls adventure (CG-009 / TG-CG-WFA-009): Chitrakote rapid boating, Tamra Gumar, Tirathgarh, Kutumsar Caves, and 4-tier hotels.",
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Raipur arrival and expedition briefing at Sengatta Eco-Park on Day 01", 1),
            _ih("Keshkal Ghats drive and Chitrakote illuminated cliff dinner on Day 02", 2),
            _ih("Chitrakote rapid boating and Tamra Gumar gorge picnic on Day 03", 3),
            _ih("Tirathgarh multi-tiered falls and Bastar Palace on Day 04", 4),
            _ih("Kutumsar Caves and Kanger Valley wildlife safari on Day 05", 5),
            _ih("Jagdalpur to Raipur departure on Day 06", 6),
        ],
        days=[
            _day(1, "RAIPUR ARRIVAL — GATEWAY TO THE WILDERNESS", (
                "Land at Raipur with TRAGUIN adventure kits and thermal flasks. Transfer to handpicked resort. Light "
                "tour of Naya Raipur, Sengatta Eco-Park, and Swami Vivekanand Sarovar. Evening expedition briefing "
                "with specialty dinner mapping the Bastar plateau river networks."
            ), ["Sightseeing Included: Naya Raipur drive, Swami Vivekanand Sarovar, Sengatta forest edge.", "Overnight Stay: Premium Luxury Eco-Resort, Raipur.", "Meals Included: Welcome Refreshments & Chef-Curated Dinner."]),
            _day(2, "RAIPUR TO CHITRAKOTE — JOURNEY TO THE NIAGARA OF INDIA", (
                "Drive south through Keshkal Ghats with twelve hairpin bends flanked by sal canopies. Arrive at "
                "Chitrakote Waterfalls and check into cliff-rim riverside eco-lodge. Watch 300-meter horseshoe falls "
                "as Indravati plunges 100 feet. Evening illuminated waterfall viewing with gourmet cliff dinner."
            ), ["Sightseeing Included: Keshkal Ghats pass, Chitrakote cliff edge trail.", "Overnight Stay: Premium Luxury Riverside Eco-Lodge, Chitrakote.", "Meals Included: Buffet Breakfast & Riverside Cliff Dinner."]),
            _day(3, "CHITRAKOTE BASIN — RAPID BOATING & THE HIDDEN GUMAR VALLEYS", (
                "Golden sunrise over Chitrakote mist. TRAGUIN Signature trek to lower basin for private country boat "
                "into thunderous spray. Afternoon off-road to Tamra Gumar and Mendri Gumar hidden twin ravines. Premium "
                "picnic lunch on valley rim and private riverside barbecue dinner under stars."
            ), ["Sightseeing Included: Chitrakote lower basin, Tamra Gumar gorge, Mendri Gumar falls.", "Overnight Stay: Premium Luxury Riverside Eco-Lodge, Chitrakote.", "Meals Included: Breakfast, Picnic Lunch & Grand Barbecue Dinner."]),
            _day(4, "CHITRAKOTE TO JAGDALPUR — THE MULTI-TIERED TIRATHGARH CASCADE", (
                "Depart Chitrakote for Jagdalpur heritage property. Enter Kanger Valley National Park for Tirathgarh "
                "Waterfalls — 300-foot multi-tiered white water sheets. Trek forest path to lower plunge pools. "
                "Afternoon visit to Bastar Palace and tribal craft bazaar high-tea walk."
            ), ["Sightseeing Included: Kanger Valley drive, Tirathgarh falls, Bastar Royal Palace.", "Overnight Stay: Handpicked Premium Luxury Hotel, Jagdalpur.", "Meals Included: Premium Breakfast & Multi-cuisine Dinner."]),
            _day(5, "KANGER VALLEY — SUBTERRANEAN CAVE EXPLORATION & JUNGLE SAFARIS", (
                "Certified escorts lead Kutumsar Caves exploration through stalactite chambers and blind cave-fish "
                "pools. Afternoon open-top 4x4 safari scanning sal canopies for leopards, wild boars, and hill myna. "
                "Grand farewell theme dinner celebrating your wilderness expedition."
            ), ["Sightseeing Included: Kutumsar Caves, Kanger Valley Wildlife Safari, Dandak Caves edge.", "Overnight Stay: Handpicked Premium Luxury Hotel, Jagdalpur.", "Meals Included: Gourmet Breakfast, Safari Packed Lunch & Grand Farewell Dinner."]),
            _day(6, "JAGDALPUR TO RAIPUR — DEPARTURE WITH LIFELONG MEMORIES", (
                "Final hearty breakfast with morning forest views. Smooth return drive to Raipur with highway lunch "
                "before airport departure."
            ), ["Sightseeing Included: Return highway transit, private airport transfer.", "Meals Included: Premium Buffet Breakfast & Farewell Highway Lunch."]),
        ],
        hotels=[
            _hotel("Babylon Inn / Hyatt Raipur | MPT Chitrakote Log Huts | MPT Naman Bastar Resort", loc, "05 Nights", "Deluxe", "Deluxe Room", "Breakfast & Dinner", 4, 1, description=f"OPTION 01 – DELUXE: Babylon Inn / Hyatt Raipur (Raipur, 1 Night) | MPT Chitrakote Log Huts (Chitrakote, 2 Nights) | MPT Naman Bastar Resort (Jagdalpur, 2 Nights) | Breakfast & Dinner"),
            _hotel("Courtyard by Marriott Raipur | Chitrakote Luxury River Huts | Asansol Heritage Resort", loc, "05 Nights", "Premium", "Premium Room", "Breakfast & Dinner", 4, 2, description=f"OPTION 02 – PREMIUM: Courtyard by Marriott Raipur (Raipur, 1 Night) | Chitrakote Luxury River Huts (Chitrakote, 2 Nights) | Asansol Heritage Resort (Jagdalpur, 2 Nights) | Breakfast & Dinner"),
            _hotel("Sayaji Hotel Raipur | Dandami Luxury Bison Resort | Grand Bastar Heritage Estate", loc, "05 Nights", "Luxury", "Luxury Room", "Breakfast & Dinner", 5, 3, description=f"OPTION 03 – LUXURY: Sayaji Hotel Raipur (Raipur, 1 Night) | Dandami Luxury Bison Resort (Chitrakote, 2 Nights) | Grand Bastar Heritage Estate (Jagdalpur, 2 Nights) | Breakfast & Dinner"),
            _hotel("Mayfair Lake Resort Raipur | Dandami Premium Presidential Villa | Bastar Palace Royal Suite", loc, "05 Nights", "Ultra Luxury", "Luxury Villa / Suite", "Breakfast & Dinner", 5, 4, description=f"OPTION 04 – ULTRA LUXURY: Mayfair Lake Resort Raipur (Raipur, 1 Night) | Dandami Premium Presidential Villa (Chitrakote, 2 Nights) | Bastar Palace Royal Suite (Jagdalpur, 2 Nights) | Breakfast & Dinner"),
        ],
        inclusions=[
            _inc_included("Premium Stays: 05 Nights at handpicked luxury hotels and riverside eco-resorts.", 1),
            _inc_included("Gourmet Dining: Daily buffet breakfast and adventurous resort dinners.", 2),
            _inc_included("Luxury Transportation: Private SUV/Fortuner 4x4 for all transfers and sightseeing.", 3),
            _inc_included("Elite Guiding: Certified naturalists, cave escorts, and wilderness guides.", 4),
            _inc_included("Complimentary Experiences: Rapid basin boat ride and Tamra Gumar picnic lunch.", 5),
            _inc_included("TRAGUIN Support: 24/7 concierge with covered tolls, fuel, and driver allowances.", 6),
            _inc_excluded("Commercial flights or train fares to and from Raipur.", 7),
            _inc_excluded("Park entry fees, cave permits, camera charges, personal expenses.", 8),
            _inc_excluded("Water sports or optional items not specified.", 9),
        ],
    )
    return package, itinerary


def build_cg_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "CG-010"
    tour_code = "TG-CG-NAT-010"
    title = (
        "TRAGUIN Premium Chhattisgarh Tour Package — Pristine Nature Trail • "
        "Wildlife, Waterfalls & Ancient Canyons"
    )
    duration = "05 Nights / 06 Days"
    slug = "cg-010-nature-trail-barnawapara-chitrakote-kanger"
    itin_slug = "cg-010-nature-trail-barnawapara-chitrakote-kanger-itinerary"
    loc = "Raipur (1 Night) / Barnawapara (1 Night) / Chitrakote (2 Nights) / Jagdalpur (1 Night)"
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph("State / Country: Chhattisgarh / India | Category: Premium Family Nature Tour", 2),
            _ph("Destinations: Raipur • Barnawapara • Chitrakote • Kanger Valley", 3),
            _ph("Ideal for: Families, Eco-Tourists & Wildlife Lovers", 4),
            _ph("Best season: October to March (Lush and vibrant post-monsoon)", 5),
            _ph("Starting price: On Request (Premium Luxury Tier)", 6),
            _ph("Vehicle: Private AC Luxury SUV (Innova Crysta) | Meal Plan: Premium MAPAI", 7),
            _ph("Route Plan: Raipur (1N) ➔ Barnawapara (1N) ➔ Chitrakote (2N) ➔ Jagdalpur (1N) ➔ Raipur Departure", 8),
            _ph("TRAGUIN Signature Experience: Night-spotting nature walk and Chitrakote sunrise boat excursion.", 9),
            _ph("Curated by TRAGUIN Experts: Certified naturalists for Barnawapara safari and Kotumsar cave tours.", 10),
            _ph("Premium Handpicked Hotels: 4-tier eco-lodges from Hyatt to Bastar Palace Royal Suite.", 11),
            _ph("Shopping: Organic forest honey, Dhonkra art, woodcraft artifacts, Tussar silk.", 12),
            _ph("Important Notes: Good-grip shoes for Kotumsar Caves; secure safari permits 45–60 days ahead.", 13),
        ],
        moods=["Nature", "Wildlife", "Family", "Eco", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note="On Request (Premium Luxury Tier)",
        rating=Decimal("4.9"), review_count=0,
        tagline="Pristine Nature Trail • Barnawapara • Chitrakote • Kanger Valley • 05 Nights / 06 Days",
        overview=(
            "Welcome to India's ultimate eco-tourism frontier. The Best Chhattisgarh Tour Package by TRAGUIN invites "
            "your family to explore untouched sal canopies, thundering waterfalls, and ancient underground cave "
            "formations across the greenest corners of Central India.\n\n"
            "TOUR OVERVIEW\n"
            "This premium Chhattisgarh Family Tour crosses Barnawapara Sanctuary bird forests, Chitrakote's colossal "
            "curtain, and Kanger Valley wooded trails. Private executive SUV, boutique eco-lodges, expert jungle "
            "trackers, and curated meals matching dietary requirements.\n\n"
            "WHY CHOOSE THE PREMIUM CHHATTISGARH NATURE TRAIL?\n"
            "Iconic Attractions: Chitrakote Falls, Kotumsar Caves, Tirathgarh Falls, Barnawapara wildlife. Family "
            "Highlights: Eco-resort river views, low-impact jungle walks, private riverside picnics. Best Time: "
            "October to March for vibrant post-monsoon forests."
        ),
        seo_title="CG-010 | Nature Trail Barnawapara Chitrakote Kanger Valley | TRAGUIN",
        seo_description="Premium 05 Nights / 06 Days nature trail (CG-010 / TG-CG-NAT-010): Barnawapara safari, Chitrakote sunrise boat, Kotumsar Caves, and 4-tier eco-lodges.",
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Raipur arrival and Swami Vivekanand Sarovar sunset on Day 01", 1),
            _ih("Barnawapara safari and night-spotting nature walk on Day 02", 2),
            _ih("Drive to Chitrakote illuminated waterfall dinner on Day 03", 3),
            _ih("Chitrakote sunrise boat cruise and Dhonkra craft village on Day 04", 4),
            _ih("Kotumsar Caves and Tirathgarh Falls on Day 05", 5),
            _ih("Jagdalpur to Raipur departure on Day 06", 6),
        ],
        days=[
            _day(1, "RAIPUR — ARRIVAL & STEP INTO PREMIUM COMFORT", (
                "Arrive at Raipur with TRAGUIN welcome amenities. Transfer to handpicked premium resort. Relaxed "
                "afternoon at property. Late afternoon scenic drive to Swami Vivekanand Sarovar for casual sunset "
                "walk along paved trails followed by elegant welcome dinner."
            ), ["Sightseeing Included: Swami Vivekanand Sarovar, Raipur panoramic drive.", "Overnight Stay: Premium Luxury Lake Resort, Raipur.", "Meals Included: Welcome Refreshments & Gourmet Dinner."]),
            _day(2, "BARNAWAPARA WILDLIFE SANCTUARY — FOREST CANOPIES & WILDLIFE ENCOUNTERS", (
                "Drive east into Barnawapara Wildlife Sanctuary teak and sal forests. Check into premium wilderness "
                "eco-lodge. Afternoon open-top 4x4 safari tracking Indian Gaurs, wild boars, sambar deer, and exotic "
                "birds. TRAGUIN Signature evening guided night-spotting walk with senior naturalist along lodge buffer zone."
            ), ["Sightseeing Included: Barnawapara Core Safari, Teak forest corridors.", "Overnight Stay: Luxury Jungle Lodge, Barnawapara.", "Meals Included: Buffet Breakfast, Jungle Lunch & Campfire Dinner."]),
            _day(3, "BARNAWAPARA TO CHITRAKOTE — APPROACHING THE NIAGARA OF INDIA", (
                "Morning bird chorus before scenic drive south to Chitrakote Waterfalls. Check into luxury riverside "
                "eco-resort with cottage deck overlooking rushing white waters. Evening illuminated waterfall viewing "
                "from premium terrace decks during exquisite dinner."
            ), ["Sightseeing Included: Scenic cross-country drive, Chitrakote Riverfront viewpoints.", "Overnight Stay: Premium Luxury Riverside Eco-Resort, Chitrakote.", "Meals Included: Premium Breakfast & Multi-cuisine Riverside Dinner."]),
            _day(4, "CHITRAKOTE FALLS — SUNRISE WATER CRUISE & TRIBAL CRAFT IMMERSIONS", (
                "Board private boat excursion at sunrise for misty base views and vibrant rainbows across water spray. "
                "Return for fresh breakfast. Afternoon visit Kondagaon craft hamlets watching Dhonkra bell-metal "
                "masters. Evening private family sunset photography along Indravati river cliffs."
            ), ["Sightseeing Included: Sunrise Mist Boat Tour, Dhonkra Craft Village, Bastar Village Walk.", "Overnight Stay: Premium Luxury Riverside Eco-Resort, Chitrakote.", "Meals Included: Buffet Breakfast, Local Organic Lunch & Specialty Dinner."]),
            _day(5, "KANGER VALLEY NATIONAL PARK — SUBTERRANEAN CAVES & TIERED FALLS", (
                "Explore Kanger Valley National Park entering Kotumsar Caves with breathtaking stalactite formations "
                "and rare blind cave-fish. Visit Tirathgarh Waterfalls dropping through multiple rocky steps. Transfer "
                "to Jagdalpur for grand farewell celebration dinner inside historic heritage estate."
            ), ["Sightseeing Included: Kotumsar Caves, Tirathgarh Tiered Waterfalls, Kanger Valley Park road.", "Overnight Stay: Handpicked Premium Heritage Hotel, Jagdalpur.", "Meals Included: Gourmet Breakfast, Forest Picnic Lunch & Grand Farewell Dinner."]),
            _day(6, "JAGDALPUR TO RAIPUR — DEPARTURE WITH LASTING BONDS", (
                "Final relaxing breakfast at heritage hotel. Smooth comfortable drive north to Raipur with elegant "
                "highway lunch before airport or railway departure."
            ), ["Sightseeing Included: Return highway drive, private departure transfer.", "Meals Included: Premium Buffet Breakfast & Farewell Highway Lunch."]),
        ],
        hotels=[
            _hotel("Hyatt Raipur | MPT Hareli Eco Resort | MPT Chitrakote Log Huts | MPT Naman Bastar Resort", loc, "05 Nights", "Deluxe", "Deluxe Room", "MAPAI (Breakfast & Dinner)", 4, 1, description=f"OPTION 01 – DELUXE: Hyatt Raipur (Raipur, 1 Night) | MPT Hareli Eco Resort (Barnawapara, 1 Night) | MPT Chitrakote Log Huts (Chitrakote, 2 Nights) | MPT Naman Bastar Resort (Jagdalpur, 1 Night) | MAPAI"),
            _hotel("Courtyard by Marriott | MPT Muba's Jungle Lodge | Chitrakote River View Huts | Asansol Heritage Resort", loc, "05 Nights", "Premium", "Premium Room", "MAPAI (Breakfast & Dinner)", 4, 2, description=f"OPTION 02 – PREMIUM: Courtyard by Marriott (Raipur, 1 Night) | MPT Muba's Jungle Lodge (Barnawapara, 1 Night) | Chitrakote River View Huts (Chitrakote, 2 Nights) | Asansol Heritage Resort (Jagdalpur, 1 Night) | MAPAI"),
            _hotel("Sayaji Hotel Raipur | Bastar Jungle Wellness Lodge | Dandami Luxury Bison Resort | Grand Bastar Heritage Estate", loc, "05 Nights", "Luxury", "Luxury Room", "MAPAI (Breakfast & Dinner)", 5, 3, description=f"OPTION 03 – LUXURY: Sayaji Hotel Raipur (Raipur, 1 Night) | Bastar Jungle Wellness Lodge (Barnawapara, 1 Night) | Dandami Luxury Bison Resort (Chitrakote, 2 Nights) | Grand Bastar Heritage Estate (Jagdalpur, 1 Night) | MAPAI"),
            _hotel("Mayfair Lake Resort (Suite) | Elite Private Wilderness Villa | Dandami Resort Premium Suite | Bastar Palace Royal Suite", loc, "05 Nights", "Ultra Luxury", "Luxury Suite", "MAPAI (Breakfast & Dinner)", 5, 4, description=f"OPTION 04 – ULTRA LUXURY: Mayfair Lake Resort Suite (Raipur, 1 Night) | Elite Private Wilderness Villa (Barnawapara, 1 Night) | Dandami Resort Premium Suite (Chitrakote, 2 Nights) | Bastar Palace Royal Suite (Jagdalpur, 1 Night) | MAPAI"),
        ],
        inclusions=[
            _inc_included("Premium Stays: 05 Nights across lake resorts, jungle lodges, and riverside eco-cottages.", 1),
            _inc_included("Gourmet Dining: Daily buffet breakfast and chef-curated dinners.", 2),
            _inc_included("Luxury Transportation: Private Innova Crysta for all transfers and sightseeing.", 3),
            _inc_included("Elite Guiding: Certified naturalists and jungle trackers during wildlife excursions.", 4),
            _inc_included("TRAGUIN Signatures: Chitrakote sunrise boat tour and guided night-spotting forest walk.", 5),
            _inc_included("TRAGUIN Support: 24/7 virtual concierge with covered tolls, fuel, and driver allowances.", 6),
            _inc_excluded("Commercial flights or railway tickets to and from Raipur.", 7),
            _inc_excluded("Park entry permits, cave guiding fees, camera tickets, personal expenses.", 8),
            _inc_excluded("Water sports or items not listed in inclusions.", 9),
        ],
    )
    return package, itinerary


CHHATTISGARH_DOMESTIC_BUILDERS = [
    build_cg_001,
    build_cg_002,
    build_cg_003,
    build_cg_004,
    build_cg_005,
    build_cg_006,
    build_cg_007,
    build_cg_008,
    build_cg_009,
    build_cg_010,
]
