"""Builder functions for UP-002 through UP-010 Uttar Pradesh domestic packages."""

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

UTTAR_PRADESH_SLUG = "uttar-pradesh"


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


def build_up_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UP-001'
    tour_code = 'TRG-UP-'
    title = 'KASHI VISHWANATH DARSHAN • SACRED LEGACY & DIVINE OPULENCE'
    duration = '03 Nights / 04 Days'
    slug = 'up-001-kashi-vishwanath-darshan-sacred-legacy-divine-opulence'
    itin_slug = 'up-001-kashi-vishwanath-darshan-sacred-legacy-divine-opulence-itinerary'
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
        is_published=True,
        highlights=[
            _ph('Serial code UP-001 | TRAGUIN tour code TRG-UP-', 1),
            _ph('State / Country: Uttar Pradesh / India | Category: Premium Pilgrimage / Luxury Spiritual Tour', 2),
            _ph('Destinations: Varanasi (Kashi)', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Luxury AC Innova Crysta / Premium MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private scholar-guided tour through the architectural corridors of Kashi', 8),
            _ph('Curated by TRAGUIN Experts: Seamless scheduling bypassing heavy public lines during peak Aarti', 9),
            _ph('Personalized Assistance: Dedicated destination support handles elderly family assistance seamlessly at', 10),
            _ph('Premium Handpicked Hotels: Elite properties selected for high safety ratings, fine hygiene, and proximity', 11)
        ],
        moods=['Luxury', 'Spiritual'],
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
        tagline='KASHI VISHWANATH DARSHAN',
        overview='PACKAGE KASHI VISHWANATH DARSHAN • SACRED LEGACY & DIVINE OPULENCE Welcome Note from TRAGUIN: Embark on an incomparable spiritual odyssey into the timeless soul of India, expertly curated by TRAGUIN. This exclusive Uttar Pradesh Pilgrimage presents the definitive Best Uttar Pradesh Tour Package, designed flawlessly to blend profound Vedic spirituality with elite, guest-facing comfort. As your trusted premium travel consultants, we bring you into the eternal city of Varanasi to stand before the divine splendor of Lord Shiva, observe the dramatic, emotional storytelling of the Ganga Aarti, and traverse the holy confluence at Prayagraj. Experience immersive experiences, breathtaking landscapes along the sacred riverbanks, and handpicked hotels that turn this pilgrimage into a series of deeply cherished, unforgettable memories.\n\nTOUR OVERVIEW\nYour upcoming luxury holiday is a meticulously designed fixed independent travel (FIT) itinerary executing the ideal route: Varanasi – Sarnath – Prayagraj – Varanasi. Travelling comfortably within a dedicated private luxury transport vehicle with an experienced, background-verified chauffeur, your family will experience absolute leisure and profound spiritual connection. Featuring a premium meal plan including daily multi- cuisine breakfasts and lavish traditional dinners, this journey incorporates a specialized TRAGUIN curated experience note: including pre-arranged VIP priority darshan passes at the iconic Kashi Vishwanath Temple, private bajra boat seating, and expert cultural guides who decode the profound legacy of Uttar Pradesh sightseeing. DESTINATION HERITAGE & SUPREME SEO CONTENT When seeking the ultimate Luxury Uttar Pradesh Holiday or an enriching Uttar Pradesh Family Tour, the sacred city of Varanasi (Kashi) represents the ultimate epicenter of culture and tradition. As one of the oldest living cities in the world, Varanasi contains the top tourist places in Uttar Pradesh, drawing millions of global seekers to its spiritual ghats and pristine temples. Booking our signature TRAGUIN Uttar Pradesh Packages grants you seamless access to highly searched and most searched experiences—from the grand evening Ganga Aarti at Dashashwamedh Ghat to the quiet, peaceful historic paths of Sarnath where Lord Buddha delivered his first sermon. For families and senior citizens searching for a highly supportive and comfortable Uttar Pradesh Pilgrimage, this itinerary bypasses crowd friction by providing premium stays, private luxury transfers, and curated entry TRAGUIN Premium Luxury Proposal — UP-001 2 systems. Beyond the spiritual essence, explore popular Instagram locations such as the ancient lanes of Varanasi, the dazzling sand dunes of Triveni Sangam in Prayagraj, and the architectural brilliance of the newly transformed Kashi Vishwanath Corridor. Whether your interest lies in exclusive handloom shopping for authentic Banarasi silk, indulging in legendary local street food, or seeking deep ancestral blessings, this proposal ensures you travel during the absolute best time to visit Uttar Pradesh with unmatched distinction.',
        seo_title='UP-001 | KASHI VISHWANATH DARSHAN | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Uttar Pradesh package (UP-001 / TRG-UP-): Varanasi (Kashi) with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=True,
        highlights=[
            _ih('Day 01: VARANASI (KASHI)', 1),
            _ih('Day 02: VARANASI (KASHI)', 2),
            _ih('Day 03: VARANASI – PRAYAGRAJ – VARANASI', 3),
            _ih('Day 04: VARANASI DEPARTURE', 4),
            _ih('TRAGUIN Signature Experience: Private scholar-guided tour through the architectural corridors of Kashi', 5),
            _ih('Curated by TRAGUIN Experts: Seamless scheduling bypassing heavy public lines during peak Aarti', 6),
            _ih('Personalized Assistance: Dedicated destination support handles elderly family assistance seamlessly at', 7)
        ],
        days=[
            _day(
                1,
                'VARANASI (KASHI)',
                (
                    'ARRIVAL EXPERIENCE, SPIRITUAL EMBARKATION & CELESTIAL GANGA AARTI Your premium Uttar Pradesh experience commences with a warm, elite welcome at the Varanasi Airport or Railway Station. Your dedicated luxury transport vehicle awaits to transfer you seamlessly to your premium handpicked hotel. After checking in and enjoying your welcome amenities, relax before an unforgettable evening. As dusk descends, proceed to the ancient Dashashwamedh Ghat. Board a privately chartered luxury Bajra boat arranged exclusively by TRAGUIN. Witness the world-renowned Ganga Aarti from the comfort of your private deck—an emotionally moving spectacle of brass lamps, synchronized Vedic chants, and hundreds of floating earthen lamps reflecting on the sacred river. Harishchandra Ghat vistas.'
                ),
                [
                    'Sightseeing Included: Dashashwamedh Ghat, Private Luxury Boat Cruise, Iconic Manikarnika &',
                    'Evening Experience: Exclusive reserved front-row river boat viewing for the majestic Ganga Aarti ceremony.',
                    'Overnight Stay: Varanasi (Premium / Luxury Selected Hotel)',
                    'Meals Included: Welcome Drink & Gourmet Dinner at Hotel Restaurant',
                ],
            ),
            _day(
                2,
                'VARANASI (KASHI)',
                (
                    'VIP KASHI VISHWANATH DARSHAN & SACRED BUDDHIST HERITAGE AT SARNATH Awake at dawn for an immersive experience. Walk through the beautifully designed, expansive Kashi Vishwanath Corridor for a pre-arranged VIP Priority Sugam Darshan at the sacred golden spire temple of Lord Shiva. Absorb the profound cosmic energy of this ancient shrine. Return for a lavish breakfast at your premium stay. In the afternoon, embark on a short scenic drive to Sarnath, an iconic tourist attraction where Lord Buddha turned the Wheel of Law. Explore the towering Dhamek Stupa, the ancient ruins of the Ashokan Pillar, and the archeological museum housing priceless heritage treasures. TRAGUIN Premium Luxury Proposal — UP-001 3 Archeological Museum.'
                ),
                [
                    'Sightseeing Included: Kashi Vishwanath Temple, Kaal Bhairav Shrine, Dhamek Stupa (Sarnath), Sarnath',
                    'Optional Activities: Early morning subah-e-banaras cultural experience at Assi Ghat with classical ragas.',
                    'Overnight Stay: Varanasi (Premium / Luxury Selected Hotel)',
                    'Meals Included: Premium Buffet Breakfast & Multi-cuisine Dinner',
                ],
            ),
            _day(
                3,
                'VARANASI – PRAYAGRAJ – VARANASI',
                (
                    'TRIVENI SANGAM HOLY CONFLUENCE & MAJESTIC HERITAGE EXCURSION Following an early morning breakfast, your chauffeur-driven luxury vehicle charts a smooth highway route to Prayagraj (Allahabad). Arrive at the legendary Triveni Sangam—the sacred confluence of three holy rivers: Ganga, Yamuna, and the mythical Saraswati. Board a private motorboat to reach the exact center point for holy bathing and family prayers amidst breathtaking landscapes. Later, explore the majestic Prayagraj Fort (built by Emperor Akbar), view the sacred Akshayavat tree, visit Anand Bhavan (the historic Nehru family estate), and pay respects at the unique reclining Hanuman Temple. Drive back to Varanasi by evening. Alopi Devi Temple.'
                ),
                [
                    'Sightseeing Included: Triveni Sangam Private Boat Excursion, Reclining Hanuman Shrine, Anand Bhavan,',
                    'Photography Points: The contrasting turquoise and muddy-brown water merger line at Triveni Sangam.',
                    'Overnight Stay: Varanasi (Premium / Luxury Selected Hotel)',
                    'Meals Included: Premium Breakfast & Special Farewell Dinner',
                ],
            ),
            _day(
                4,
                'VARANASI DEPARTURE',
                (
                    'CHERISHING SACRED BLESSINGS & UNFORGETTABLE MEMORIES Indulge in a relaxed, sumptuous breakfast at your luxury hotel. Spend your morning checking off your final vehicle provides a comfortable door-to-door transfer back to Varanasi Airport or Railway Station for your return flight home. Your elite pilgrimage concludes with divine peace, rejuvenated spirit, and unforgettable memories designed exclusively by TRAGUIN. TRAGUIN Premium Luxury Proposal — UP-001 4'
                ),
                [
                    'shopping: wishes for fine handicrafts or sweet local delicacies. At the designated hour, your premium transport',
                    'Transfers Included: Private luxury hotel check-out and airport/station drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Meraden Grand / Amaya',
                'Varanasi (Kashi)',
                '3N',
                'Deluxe',
                'Hotel / similar',
                'Deluxe Executive',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Meraden Grand / Amaya | Hotel / similar | Deluxe Executive',
            ),
            _hotel(
                'Radisson Hotel Varanasi /',
                'Varanasi (Kashi)',
                '3N',
                'Premium',
                'Ramada Plaza / similar',
                'Premium Club RoomMAPAI (Breakfast &',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Hotel Varanasi / | Ramada Plaza / similar | Premium Club RoomMAPAI (Breakfast &',
            ),
            _hotel(
                'Taj Ganges Varanasi / BrijRama',
                'Varanasi (Kashi)',
                '3N',
                'Luxury',
                'Palace (Heritage)',
                'Luxury Garden View /',
                4,
                3,
                description='OPTION 03 – LUXURY: Taj Ganges Varanasi / BrijRama | Palace (Heritage) | Luxury Garden View /',
            ),
            _hotel(
                'Nadesar Palace Taj (Ultra',
                'Varanasi (Kashi)',
                '3N',
                'Ultra Luxury',
                'Luxury Living)',
                'Historical Royal Palace',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Nadesar Palace Taj (Ultra | Luxury Living) | Historical Royal Palace',
            )
        ],
        inclusions=[
            _inc_included('Premium Accommodation: 03 Nights stay in handpicked hotels of chosen category.', 1),
            _inc_included('Luxury Transportation: All transfers & sightseeing via private AC Innova Crysta.', 2),
            _inc_included('Bespoke Meal Plan: Daily luxury buffet breakfasts and fine dinners included.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated personal tour assistance & manager support.', 4),
            _inc_included('Welcome Amenities: Personalized divine welcome kit with sweets and holy Ganga Jal.', 5),
            _inc_included('Complimentary Experiences: Private chartered Bajra boat ride for Ganga Aarti viewing.', 6),
            _inc_excluded('Flights or long-distance train tickets to and from Varanasi.', 7),
            _inc_excluded('Individual temple entry tickets, local pooja or ritual performance costs.', 8),
            _inc_excluded('Personal expenses such as laundry, phone calls, gratuities, and mini-bar.', 9),
            _inc_excluded('Any insurance, local taxes, or extra excursions not mentioned in the route. TRAGUIN Premium Luxury Proposal — UP-001 5', 10),
        ],
    )
    return package, itinerary

UTTAR_PRADESH_UP_001_BUILDERS = [
    build_up_001,
]
