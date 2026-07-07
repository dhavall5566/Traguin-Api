"""Builder functions for AP-001 through AP-010 Andhra Pradesh domestic packages."""

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

ANDHRA_PRADESH_SLUG = "andhra-pradesh"


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

def build_ap_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AP-001'
    tour_code = 'TG-AP-TIR-001'
    title = 'TRAGUIN Premium Tirupati Darshan Tour Package'
    duration = '02 Nights / 03 Days'
    slug = 'ap-001-premium-tirupati-darshan-tour'
    itin_slug = 'ap-001-premium-tirupati-darshan-tour-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Andhra Pradesh / India | Category: Pilgrimage / Spiritual Family Tour', 2),
            _ph('Destinations: Tirupati • Tirumala • Tiruchanur', 3),
            _ph('Ideal for: Families, Devotees & Elders', 4),
            _ph('Best season: September to March (Pleasant weather)', 5),
            _ph('Starting price: On Request (Premium Luxury Tier)', 6),
            _ph('Vehicle: Private AC Toyota Innova Crysta / Luxury SUV | Meal Plan: Premium CP / MAPAI (Pure Vegetarian Gourmet Meals)', 7),
            _ph('Route Plan: Renigunta / Chennai Arrival → Tirupati (2 Nights) → Tirumala Hills → Departure', 8),
            _ph('TRAGUIN Curated Experience Note: Seamless VIP assistance during hair-tonsuring (Kalyana Katta) rituals, pre-secured traditional Laddu prasadam delivered directly to your vehicle, and dedicated senior assistance for elderly family members.', 9),
            _ph('TRAGUIN Signature Experience: Private pre-darshan orientation with an elite local scholar, explaining the deep history and spiritual mysteries of Tirumala.', 10),
            _ph('Curated by TRAGUIN Experts: Every transit route, private driver, and premium property is rigorously vetted to ensure absolute safety, absolute hygiene, and elder-friendly access.', 11),
            _ph('Personalized Assistance: A dedicated, compassionate pilgrim assistant to guide elders smoothly through temple queue paths.', 12),
            _ph('Premium Handpicked Hotels: Stay in iconic luxury properties like Taj Tirupati, offering magnificent views of the sacred hills and relaxing spa facilities.', 13),
            _ph('Exclusive Recommendations: Handselected choice of verified, ultra-hygienic traditional dining stops serving authentic South Indian delicacies.', 14),
            _ph('Shopping & Local Experiences: Srikalahasti Kalamkari Art, Tirupati Brassware & Idols at Lepakshi Handicrafts Emporium, Traditional Silk Weaves (Mangalagiri and Dharmavaram), Culinary Stops for Tirupati Ghee Roast Dosa and authentic filter coffee.', 15),
            _ph('Important Notes: Traditional Dress Code Guidelines for Tirumala entry. Identity Verification Rules: carry exact original government photo ID used during booking. Electronic Restrictions: mobile phones, cameras prohibited inside main Tirumala temple complex. Advance Booking Suggestions: complete bookings 60–90 days in advance for Special Entry Darshan and premium rooms.', 16),
        ],
        moods=['Pilgrimage', 'Spiritual', 'Family', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Premium Tirupati Darshan Tour • Tirupati • Tirumala • Tiruchanur • 02 Nights / 03 Days',
        overview=(
            'Welcome to the sacred abode of Kaliyuga Vaikuntha. The absolute Best Tirupati Tour Package, meticulously curated by the expert team at TRAGUIN, invites you and your beloved family to experience divine grace without the stress of ordinary planning. Nestled within the breathtaking landscapes of the majestic Seshachalam Hills, this premium Andhra Pradesh Sightseeing experience balances profound spiritual devotion with uncompromised material comfort.\n\nTOUR OVERVIEW\nThis premium Tirupati Honeymoon Package or Tirupati Family Tour is designed to bypass the exhausting challenges of spiritual travel. From your arrival at the airport or station, you will be immersed in an environment of quiet luxury. Benefit from our personalized, high-touch coordination, featuring pre-arranged Special Entry Darshan tickets, an expert spiritual guide, and dedicated luxury ground transport throughout your pilgrimage trail.\n\nWHY CHOOSE THE PREMIUM TIRUPATI FAMILY TOUR?\nA spiritual journey to the world\'s most visited temple city deserves an elite touch. Explore the Top Tourist Places in Tirupati with specialized guides offering an educational, deeply moving, and smooth getaway for your entire family.'
        ),
        seo_title='AP-001 | Premium Tirupati Darshan Tour | TRAGUIN',
        seo_description='Premium 02 Nights / 03 Days Tirupati pilgrimage package (AP-001 / TG-AP-TIR-001): Tirumala VIP darshan, Padmavathi Temple, Srikalahasti, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Sri Padmavathi Ammavari Temple (Tiruchanur) and Sri Govindaraja Swamy Temple on arrival day', 1),
            _ih('Sri Venkateswara Swamy Temple VIP Special Entry Darshan on Tirumala Hills', 2),
            _ih('Silathoranam Rock Gate, Akasa Ganga, and Swami Pushkarini', 3),
            _ih('Srikalahasti Sri Kalahasteeswara Temple excursion (Vayu Lingam)', 4),
            _ih('TRAGUIN Signature Experience: Private pre-darshan orientation with elite local scholar', 5),
        ],
        days=[
            _day(1, 'ARRIVAL, SPIRITUAL AWAKENING & BLESSINGS OF THE GODDESS', ('Your divine pilgrimage path opens as you arrive at Renigunta Tirupati Airport or Railway Station. Your dedicated TRAGUIN private chauffeur welcomes your family with traditional silk stoles and signature welcome amenities, escorting you in an air-conditioned luxury SUV to your premium hotel. Complete your smooth check-in and indulge in a traditional, purely vegetarian gourmet lunch. In the afternoon, embark on your first spiritual exploration to Tiruchanur to seek the grace of the Goddess at the Sri Padmavathi Ammavari Temple. Traditional beliefs dictate seeking the blessings of the Divine Consort before visiting the Lord. Our local spiritual advisor will guide you seamlessly through the special queue lines. Next, experience the historic Sri Govindaraja Swamy Temple in the heart of Tirupati, marveling at its towering seven-tiered outer gateway. Conclude your day with a traditional South Indian fine dining meal at your resort, wrapping up your evening in peace.'), [
                'Sightseeing Included: Private arrival transfer, Sri Padmavathi Ammavari Temple (Tiruchanur), Sri Govindaraja Swamy Temple.',
                'Evening Experience: Traditional welcome dinner and detailed darshan briefing by our tour manager.',
                'Meals Included: Welcome Signature Refreshments & Traditional Pure Vegetarian Fine Dining Dinner.',
                'Overnight Stay: Handpicked Premium Luxury Hotel, Tirupati.',
            ]),
            _day(2, 'TIRUMALA HILLS — THE ULTIMATE DIVINE VIP DARSHAN EXPERIENCE', ('Wake up at dawn to the peaceful sounds of temple bells. Today marks the magnificent center of your TRAGUIN Tirupati Packages journey. Following an early morning traditional breakfast, your private luxury vehicle glides up the winding, scenic Ghat roads of the Tirumala Hills, offering breathtaking landscapes of the surrounding dense valley. For guests wishing to participate in traditional rituals, our helper will provide smooth coordination at the premium Kalyana Katta facilities. Proceed immediately to the temple entrance gate where your pre-secured Special Entry Darshan passes ensure priority entry. Walk through the historic stone mandapams and approach the inner sanctum. Stand in profound awe before the majestic, jewel-encrusted 7-foot tall self-manifested idol of Lord Sri Venkateswara Swamy. Absorb the deep spiritual energy as your guide coordinates the collection of your legendary, traditional Tirupati Laddus. Later, explore the unique natural geological marvel of Silathoranam and the sacred Akasa Ganga waterfalls before returning down to your hotel for a relaxed evening.'), [
                'Sightseeing Included: Scenic Tirumala Ghat road drive, Sri Venkateswara Swamy Temple VIP Darshan, Swami Pushkarini, Silathoranam Rock Gate, Akasa Ganga.',
                'Evening Experience: Private distribution of blessed Laddu Prasadam and a premium relaxed dinner at the property.',
                'Meals Included: Satvik Breakfast & Curated Pure Veg Multi-cuisine Dinner.',
                'Overnight Stay: Handpicked Premium Luxury Hotel, Tirupati.',
            ]),
            _day(3, 'SRIKALAHASTI EXCURSION — FINAL BLESSINGS & JOURNEY HOME', ('Savor a luxurious breakfast at your hotel before embarking on a brief, highly enriching excursion to the ancient town of Srikalahasti, located just 40 minutes away. Here, you will explore the awe-inspiring Sri Kalahasteeswara Temple, a grand 5th-century Chola architectural marvel dedicated to Lord Shiva as the element of Wind (Vayu Lingam). The temple is globally searched for its powerful Rahu-Ketu cosmic balancing prayers. Walk through the towering pillared halls carved elegantly out of solid stone hillsides. Return to Tirupati for some light local shopping or premium dining. In the afternoon, your private chauffeur will provide a seamless transfer to Tirupati Airport or Renigunta Railway Station for your return trip home. Your premium spiritual path draws to a gentle close, leaving your family fully rejuvenated with divine peace, happiness, and unforgettable memories crafted flawlessly by TRAGUIN.'), [
                'Sightseeing Included: Srikalahasti Shiva Temple tour, local handicraft boutique stop, departure airport/station transfer.',
                'Meals Included: Premium Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Fortune Select Grand Ridge / Minerva Grand', 'Tirupati', '02 Nights', 'Deluxe', 'Deluxe Executive Room', 'CP (Includes Daily Breakfast)', 4, 1, description='OPTION 01 – DELUXE: Fortune Select Grand Ridge / Minerva Grand (Tirupati, 02 Nights)'),
            _hotel('Marasa Sarovar Premiere (Tirupati\'s elite themed hotel)', 'Tirupati', '02 Nights', 'Premium', 'Premium Hill View Room', 'MAPAI (Breakfast & Dinner)', 4, 2, description='OPTION 02 – PREMIUM: Marasa Sarovar Premiere (Tirupati, 02 Nights)'),
            _hotel('Taj Tirupati', 'Tirupati', '02 Nights', 'Luxury', 'Superior Garden View Room', 'MAPAI (Gourmet Pure Vegetarian)', 5, 3, description='OPTION 03 – LUXURY: Taj Tirupati (Tirupati, 02 Nights)'),
            _hotel('Taj Tirupati', 'Tirupati', '02 Nights', 'Ultra Luxury', 'Executive Luxury Suite', 'MAPAI & Private VIP Airport Transfers', 5, 4, description='OPTION 04 – ULTRA LUXURY: Taj Tirupati Executive Luxury Suite (Tirupati, 02 Nights)'),
        ],
        inclusions=[
            _inc_included('Premium Stays: 02 Nights luxury accommodation at handpicked properties in Tirupati.', 1),
            _inc_included('Gourmet Dining: Daily premium breakfasts and chef-curated Satvik vegetarian dinners at the hotel.', 2),
            _inc_included('Luxury Transportation: Private air-conditioned vehicle (Toyota Innova Crysta or luxury SUV) dedicated for your entire sightseeing, transfers, and Tirumala hill ascent routes.', 3),
            _inc_included('Elite Assistance: Dedicated TRAGUIN spiritual advisor and helper to handle queue lines, traditional hair-tonsuring rituals, and elder care.', 4),
            _inc_included('Darshan Assistance: Priority facilitation for Special Entry Darshan tickets, along with pre-secured traditional Laddu Prasadam allocations.', 5),
            _inc_included('Welcome Amenities: Traditional silk stole greeting, customized family travel kit, and premium mineral water bottles provided daily.', 6),
            _inc_included('Taxes & Support: 24/7 dedicated virtual support from our concierge team, along with covered fuel, tolls, parking, and driver allowances.', 7),
            _inc_excluded('Travel Tickets: Commercial flights or interstate rail tickets to/from Renigunta or Chennai.', 8),
            _inc_excluded('Ritual Tickets: Personal costs for special individual arjitha sevas or private ritual offerings inside the temples.', 9),
            _inc_excluded('Personal Expenses: Laundry services, telephone charges, traditional temple donation receipts, and tips.', 10),
            _inc_excluded('Optional Extras: Extra luggage handling services, travel insurance policies, or deviations from the pre-planned route.', 11),
        ],
    )
    return package, itinerary

def build_ap_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AP-002'
    tour_code = 'TG-AP-TSK-002'
    title = 'TRAGUIN Premium Andhra Pradesh Tour Package'
    duration = '03 Nights / 04 Days'
    slug = 'ap-002-divine-sovereign-soul-trail-tirupati-srikalahasti'
    itin_slug = 'ap-002-divine-sovereign-soul-trail-tirupati-srikalahasti-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Andhra Pradesh / India | Category: Premium Pilgrimage / Family Divine FIT', 2),
            _ph('Destinations: Tirupati • Tirumala • Srikalahasti', 3),
            _ph('Ideal for: Families, Devotees & Spiritual Seekers', 4),
            _ph('Best season: September to March', 5),
            _ph('Starting price: On Request (Premium Luxury Tier)', 6),
            _ph('Vehicle: Private AC Luxury Sedan / SUV (Innova Crysta) | Meal Plan: Premium MAPAI (Daily Breakfast & Satvik Dinners)', 7),
            _ph('Route Plan: Renigunta / Chennai Arrival → Tirupati (3 Nights) → Srikalahasti Excursion → Departure', 8),
            _ph('TRAGUIN Curated Experience Note: Pre-booked Special Entry Darshan slots, dedicated local coordinator to handle ritual protocols, handpicked hotels serving exquisite culinary options, and personalized traditional welcome kits for your family.', 9),
            _ph('TRAGUIN Signature Experience: Private traditional family briefing with an analysis of architectural history before exploring the main temples.', 10),
            _ph('Curated by TRAGUIN Experts: Every transport vehicle, hotel room, and transit schedule is rigorously inspected to ensure top comfort for elderly family members and children.', 11),
            _ph('Personalized Assistance: Elite, dedicated holiday specialist monitoring your flight schedules and gate clearances around the clock.', 12),
            _ph('Premium Handpicked Hotels: Stay inside luxury properties like the Taj Tirupati, offering magnificent views of the sacred Seshachalam mountain peaks.', 13),
            _ph('Exclusive Recommendations: Curated selection of verified shopping options for purchasing authentic gold-plated Tanjore paintings and organic sandalwood items.', 14),
            _ph('Shopping & Local Experiences: Kalamkari Fabric Art at Srikalahasti, Tanjore Paintings & Brass in Tirupati markets, traditional Andhra Bhojanom, Tirupati Laddu variants and Pootharekulu sweets.', 15),
            _ph('Important Notes: Mandatory Dress Code Rules for Tirumala and Srikalahasti temples. Identity Verification with original government photo ID. Electronic Equipment Ban inside main temple premises. Advance Darshan Bookings recommended 60 to 90 days in advance.', 16),
        ],
        moods=['Pilgrimage', 'Spiritual', 'Family', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='The Divine Sovereign Soul Trail — Tirupati & Srikalahasti • 03 Nights / 04 Days',
        overview=(
            'Welcome to a journey of profound divinity and sublime peace. The Best Andhra Pradesh Tour Package, exclusively curated by TRAGUIN, invites your family to seek blessings at India\'s most revered spiritual citadels. This ultra-curated pilgrimage blends seamless VIP access with premium comfort, offering an unmatched Premium Andhra Pradesh Experience.\n\nTOUR OVERVIEW\nThis masterfully planned Andhra Pradesh Family Tour covers the grand spiritual sanctuaries of Chittoor district. Beginning in the historic temple town of Tirupati, ascending into the celestial domain of Tirumala, and extending to the ancient Shiva node at Srikalahasti, every segment is tailored for absolute comfort.\n\nWHY CHOOSE THE PREMIUM TIRUPATI & SRIKALAHASTI CIRCUIT?\nFamous Attractions include Tirumala Venkateswara Temple, Srikalahasteeswara Temple, Padmavathi Ammavari Temple, and Kapila Theertham. Best Time to Visit: September to March offers comfortable temperatures for outdoor temple explorations.'
        ),
        seo_title='AP-002 | Divine Sovereign Soul Trail Tirupati Srikalahasti | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Andhra Pradesh pilgrimage package (AP-002 / TG-AP-TSK-002): Tirumala VIP darshan, Srikalahasti Rahu-Ketu node, Kapila Theertham, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Tiruchanur Padmavathi Temple, Kapila Theertham Temple & Waterfall on arrival day', 1),
            _ih('Tirumala Venkateswara Temple Special Entry Darshan and Swami Pushkarini', 2),
            _ih('Srikalahasteeswara Temple Rahu-Ketu rituals and Govindaraja Swamy Temple', 3),
            _ih('Srinivasa Mangapuram temple and seamless departure transfer', 4),
            _ih('TRAGUIN Signature Experience: Private traditional family briefing on temple architectural history', 5),
        ],
        days=[
            _day(1, 'ARRIVAL & INTRODUCTION TO THE DIVINE GATEWAY', ('Your holy journey begins as you land at Tirupati (Renigunta) Airport or arrive at the railway station. Receive a warm traditional welcome from your dedicated TRAGUIN executive chauffeur, who will transfer you in a private luxury SUV to your premium hotel. Enjoy a seamless check-in experience accompanied by traditional welcome drinks. After an exquisite south Indian vegetarian lunch and a short rest, embark on your first Andhra Pradesh Sightseeing excursion. Visit the beautiful Sri Padmavathi Ammavari Temple at Tiruchanur, dedicated to the divine consort of Lord Venkateswara, where custom demands a devotee must pay respect before ascending the hills. Next, drive to the ancient Kapila Theertham, a historic Shiva temple located right at the foothills of Tirumala, featuring a sacred waterfall plunging into a clean temple tank. Return to your hotel for an exclusive Satvik dinner prepared by master chefs.'), [
                'Sightseeing Included: Tiruchanur Padmavathi Temple, Kapila Theertham Temple & Waterfall, local temple lanes.',
                'Evening Experience: Traditional lighting of lamps at the hotel temple corner and a relaxed evening briefing with our local destination representative.',
                'Meals Included: Welcome Refreshments & Gourmet Vegetarian Dinner.',
                'Overnight Stay: Premium Handpicked Hotel, Tirupati.',
            ]),
            _day(2, 'TIRUMALA HILLS — STANDING BEFORE THE LORD OF THE SEVEN HILLS', ('Wake up early to the peaceful chants of Suprabhatam. Today marks the absolute centerpiece of your Luxury Andhra Pradesh Holiday. After breakfast, your private vehicle winds up the beautifully managed ghat road of the Seshachalam hills, featuring scenic beauty and lush mountain ranges. Reach Tirumala, the high celestial domain of Lord Venkateswara. Using the fast-track Special Entry Darshan tokens pre-arranged by TRAGUIN experts, enter the historic temple complex. Stand in deep emotional awe before the self-manifested, jewel-encrusted majestic idol of Lord Venkateswara under the golden Ananda Nilayam dome. Absorb the high spiritual vibration as priests chant Vedic hymns. After a fulfilling darshan, receive the legendary, GI-tagged Tirupati Laddu Prasadam. Spend time exploring the scenic temple structures and the holy Swami Pushkarini tank before descending back to Tirupati in the evening.'), [
                'Sightseeing Included: Tirumala Venkateswara Temple, Swami Pushkarini, Seshachalam mountain view spots.',
                'Evening Experience: Distribution of prasadam and a relaxed multi-course family dinner at your hotel.',
                'Meals Included: Buffet Breakfast & Special Celebratory Satvik Dinner.',
                'Overnight Stay: Premium Handpicked Hotel, Tirupati.',
            ]),
            _day(3, 'SRIKALAHASTI — THE COSMIC RAHU-KETU VAYU NODE', ('Following a relaxed breakfast, depart on an enriching excursion toward the historic town of Srikalahasti, situated neatly between two hills on the banks of the Swarnamukhi River. This iconic attraction represents the element of Air (Vayu) among the sacred Pancha Bhoota Stalams of Lord Shiva. Enter the ancient stone hallways of the Srikalahasteeswara Temple. For families interested in traditional astrological balances, our local coordinator will smoothly facilitate the highly regarded Rahu-Ketu transition or planetary balance rituals inside the temple complex. Observe the flickering lamp in the inner sanctum that moves constantly despite no air movement, symbolizing the Vayu element. In the late afternoon, drive past scenic agricultural fields back to Tirupati, stopping by the historic Govindaraja Swamy Temple featuring an impressive 11-tiered gopuram tower.'), [
                'Sightseeing Included: Srikalahasti Temple, Swarnamukhi River view, Govindaraja Swamy Temple.',
                'Optional Activities: Execution of special Rahu-Ketu planet pacification rituals with pre-assigned temple scholars.',
                'Evening Experience: Final evening shopping walk for authentic traditional textile art pieces.',
                'Meals Included: Breakfast & Multi-cuisine Vegetarian Fine Dining.',
                'Overnight Stay: Premium Handpicked Hotel, Tirupati.',
            ]),
            _day(4, 'FINAL BLESSINGS & SEAMLESS ONWARD JOURNEY', ('Indulge in a final morning breakfast at your hotel. If time permits based on your departure flight or train schedule, visit the peaceful Sri Srinivasa Mangapuram temple, a highly historic site where Lord Venkateswara is believed to have stayed after his celestial marriage. Take a moment to capture final family photographs in front of the elegant temple gardens. Your private chauffeur will provide a seamless transfer to the Tirupati Airport or Renigunta Railway station for your journey home. Your premium pilgrimage trail concludes here, leaving your soul completely rejuvenated, filled with positive spiritual energy and unforgettable memories crafted beautifully by TRAGUIN.'), [
                'Sightseeing Included: Srinivasa Mangapuram temple check-in, Airport Private Transfer.',
                'Meals Included: Premium Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Fortune Select Grand Ridge / Similar', 'Tirupati', '03 Nights', 'Deluxe', 'Deluxe Vegetarian Room', 'Breakfast & Satvik Dinner', 4, 1, description='OPTION 01 – DELUXE: Fortune Select Grand Ridge / Similar (Tirupati, 03 Nights)'),
            _hotel('Marasa Sarovar Premiere Tirupati', 'Tirupati', '03 Nights', 'Premium', 'Premium Hill View Room', 'Breakfast & Satvik Dinner', 4, 2, description='OPTION 02 – PREMIUM: Marasa Sarovar Premiere Tirupati (Tirupati, 03 Nights)'),
            _hotel('Taj Tirupati', 'Tirupati', '03 Nights', 'Luxury', 'Superior Executive Room', 'Breakfast & Gourmet Dinner', 5, 3, description='OPTION 03 – LUXURY: Taj Tirupati (Tirupati, 03 Nights)'),
            _hotel('Taj Tirupati', 'Tirupati', '03 Nights', 'Ultra Luxury', 'Luxury Seshachalam Suite Tier', 'Breakfast, Custom Chef Dinners', 5, 4, description='OPTION 04 – ULTRA LUXURY: Taj Tirupati Luxury Seshachalam Suite (Tirupati, 03 Nights)'),
        ],
        inclusions=[
            _inc_included('Premium Stays: 03 Nights premium luxury accommodation at top-rated handpicked hotels in Tirupati.', 1),
            _inc_included('Gourmet Dining: Daily breakfast and multi-course vegetarian dinners included at the hotel dining rooms.', 2),
            _inc_included('Luxury Transportation: Private air-conditioned luxury vehicle (Toyota Innova Crysta) for all transfers, intercity ghat travel, and excursions as per the itinerary.', 3),
            _inc_included('Spiritual Coordination: Dedicated local representative support to manage timing grids and guide you through ritual lines.', 4),
            _inc_included('Welcome Kit: Traditional welcome stole, religious booklet guide, and premium bottled mineral water supplied inside the car daily.', 5),
            _inc_included('TRAGUIN Assistance: 24/7 priority concierge support from TRAGUIN operational control, covering toll taxes, fuel prices, parking fees, and driver allowances.', 6),
            _inc_excluded('Transit Tickets: Main airline flights or train bookings to Tirupati / Chennai.', 7),
            _inc_excluded('Darshan Tickets: Direct temple ticket fees or specialized ritual costs (Rahu-Ketu transit tickets) unless explicitly bundled in final customized quote options.', 8),
            _inc_excluded('Personal Items: Laundry charges, telephone bills, additional temple donation tokens, and tips for priests or drivers.', 9),
            _inc_excluded('Insurance: Medical or travel insurance policies.', 10),
        ],
    )
    return package, itinerary

def build_ap_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AP-003'
    tour_code = 'TG-AP-VZG-003'
    title = 'TRAGUIN Premium Vizag Tour Package'
    duration = '03 Nights / 04 Days'
    slug = 'ap-003-bespoke-vizag-escape-coastal-splendour'
    itin_slug = 'ap-003-bespoke-vizag-escape-coastal-splendour-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Andhra Pradesh / India | Category: Premium Family Tour Package', 2),
            _ph('Destinations: Visakhapatnam (Vizag) • Araku Valley', 3),
            _ph('Ideal for: Families, Couples & Nature Enthusiasts', 4),
            _ph('Best season: October to March (Pleasant coastal breezes)', 5),
            _ph('Starting price: On Request (Premium Luxury Tier)', 6),
            _ph('Vehicle: Private AC Luxury Sedan / SUV | Meal Plan: Premium MAPAI (Daily Breakfast & Elegant Dinners)', 7),
            _ph('Route Plan: Vizag Arrival → Vizag Sightseeing (2N) → Araku Valley Excursion (1N) → Departure', 8),
            _ph('TRAGUIN Curated Experience Note: Private sunset high tea at a premium ocean-view cliff spot, pre-arranged VIP passes to historic submarine museums, and a curated culinary trail highlighting authentic coastal Andhra delicacies.', 9),
            _ph('TRAGUIN Signature Experience: Private family sunset high tea set up elegantly at a quiet panoramic viewpoint overlooking the Bay of Bengal.', 10),
            _ph('Curated by TRAGUIN Experts: Every resort hotel, private chauffeur, and activity is rigorously vetted to guarantee complete safety and premium luxury for your family.', 11),
            _ph('Personalized Assistance: Elite, dedicated travel coordinator available 24/7 to manage any adjustments or special requests across your entire stay.', 12),
            _ph('Premium Handpicked Hotels: Stay in iconic properties, from five-star oceanfront resorts to tranquil eco-luxury villas nestled in coffee domains.', 13),
            _ph('Bespoke Recommendations: Handselected collection of hidden coastal view spots, authentic local dining gems, and high-quality textile boutiques.', 14),
            _ph('Shopping & Local Experiences: Ponduru Khadi Fabrics, Etikoppaka lacquered wooden toys, Authentic Coastal Flavors (Royyala Vepudu, Chepala Pulusu), Araku Organic Coffee, honey and pepper from estate outlets.', 15),
            _ph('Important Notes: Hotel Check-in/out standard 14:00 / 11:00 hrs. Beach Safety Rules at Rushikonda Blue Flag Beach. Araku Weather Notes: carry light cardigans for cool evenings. Advance Booking Suggestions: 45–60 days ahead for peak winter weekends.', 16),
        ],
        moods=['Family', 'Coastal', 'Nature', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Bespoke Vizag Escape • Coastal Splendour & Mist-Kissed Valleys • 03 Nights / 04 Days',
        overview=(
            'Welcome to the jewel of the Eastern Coast. The definitive Best Vizag Tour Package, exclusively curated by TRAGUIN, invites your family to discover an extraordinary destination where majestic hills melt directly into the sapphire waters of the Bay of Bengal. This customized Premium Vizag Experience seamlessly brings together serene coastal drives, deep maritime history, and the lush, coffee-scented heights of Araku Valley.\n\nTOUR OVERVIEW\nOur Vizag Escape itinerary offers an ideal blend of sun-drenched beaches and tranquil hill stations. Over 4 days, you will discover the modern coastal charms of Visakhapatnam before climbing into the misty Eastern Ghats to experience the coffee estates and ancient caves of Araku.\n\nWHY CHOOSE A PREMIUM VIZAG & ARAKU FAMILY TOUR?\nIconic Attractions include RK Beach, Rushikonda Beach, INS Kursura Submarine Museum, Kailasagiri Hill, and Borra Caves in Araku. Best Time to Visit Vizag: October to March offers refreshing sea breezes and pleasant sunny days.'
        ),
        seo_title='AP-003 | Premium Vizag Tour Package | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Vizag package (AP-003 / TG-AP-VZG-003): RK Beach, Kailasagiri, Borra Caves, Araku Valley, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('RK Beach, INS Kursura Submarine Museum, and TU-142 Aircraft Museum on arrival day', 1),
            _ih('Kailasagiri Hill Ropeway, Rushikonda Blue Flag Beach, and Thotlakonda Buddhist Complex', 2),
            _ih('Borra Caves, Araku Tribal Museum, and Dimsa folk dance performance', 3),
            _ih('Chaprai Waterfalls and local handloom textile bazaar before departure', 4),
            _ih('TRAGUIN Signature Experience: Private family sunset high tea overlooking the Bay of Bengal', 5),
        ],
        days=[
            _day(1, 'VISAKHAPATNAM — COASTAL ARRIVAL & THE IMPERIAL CITY OF DESTINY', ('Your coastal holiday begins as you touch down at Visakhapatnam Airport or arrive at the central railway station. Your dedicated TRAGUIN private chauffeur welcomes you with refreshing amenities, escorting your family in a luxury vehicle to your handpicked premium beachfront hotel. After a seamless check-in and an exquisite lunch, start your afternoon Vizag Sightseeing track. Head first to the famous Ramakrishna Beach (RK Beach), where long walkways border the azure waters of the Bay of Bengal. Step inside history at the iconic INS Kursura Submarine Museum—a real, decommissioned Soviet-built submarine established right on the sandy shore. Next, explore the adjacent TU-142 Aircraft Museum to see impressive anti-submarine warplanes up close. Return to your premium hotel for an elegant dinner overlooking the ocean, creating your very first unforgettable memories on this escape.'), [
                'Sightseeing Included: RK Beach, INS Kursura Submarine Museum, TU-142 Aircraft Museum, Kali Temple.',
                'Evening Experience: Relaxed evening walk on the beach followed by a curated beachside seafood dinner suggestion.',
                'Meals Included: Welcome Signature Refreshments & Gourmet Multi-course Dinner.',
                'Overnight Stay: Premium Ocean-view Beach Resort, Visakhapatnam.',
            ]),
            _day(2, 'VIZAG — PANORAMIC VIEWPOINTS & PRISTINE GOLDEN BEACHES', ('Awake to the refreshing sound of rolling sea waves and a bright morning sun. After a sumptuous breakfast, drive along the gorgeous beach road to Kailasagiri Hill. Climb to the top via an exciting ropeway ride that gives your family panoramic views of the entire crescent bay. At the summit, stroll through beautifully manicured gardens and see the towering stone statues of Lord Shiva and Goddess Parvati. In the afternoon, discover the golden sands of Rushikonda Beach, widely celebrated as one of India\'s cleanest Blue Flag certified beaches. Next, proceed to Thotlakonda, an ancient hilltop Buddhist monastic complex dating back over 2,000 years. Conclude your afternoon with a TRAGUIN Signature Experience: a premium sunset high tea set up at a quiet, cliffside spot overlooking the ocean before heading back to your luxury stay.'), [
                'Sightseeing Included: Kailasagiri Hill Ropeway, Rushikonda Blue Flag Beach, Thotlakonda Buddhist Complex.',
                'Evening Experience: Exclusive TRAGUIN Sunset High Tea on a cliff overlook, followed by a relaxed family evening.',
                'Meals Included: Buffet Breakfast, Cliffside High Tea, & Gourmet Dinner.',
                'Overnight Stay: Premium Ocean-view Beach Resort, Visakhapatnam.',
            ]),
            _day(3, 'VIZAG TO ARAKU VALLEY — CLIMBING INTO MIST-KISSED COFFEE DOMAINS', ('Following an early breakfast, bid farewell to the coast as your private luxury vehicle winds inland, ascending into the stunning, mist-draped Eastern Ghats toward the beautiful Araku Valley. Your first major highlight is the remarkable Borra Caves, deep million-year-old limestone formations filled with fascinating stalactites and stalagmites under beautiful colorful lighting. Continue your drive into the core of Araku Valley, passing wide green steps of organic coffee estates. Check into your romantic, handpicked eco-luxury resort. In the afternoon, visit the insightful Araku Tribal Museum, which showcases the fascinating culture, attire, and traditions of local indigenous clans. Walk through the fragrant paths of the Ananthagiri Coffee Plantations and watch a vibrant local Dimsa folk dance performance arranged at your resort in the evening.'), [
                'Sightseeing Included: Borra Caves exploration, Araku Valley coffee trail, Araku Tribal Museum, Galikonda View Point.',
                'Evening Experience: Private Dimsa tribal dance performance and traditional Bamboo Chicken culinary tasting.',
                'Meals Included: Buffet Breakfast & Authentic Andhra Tribal Theme Dinner.',
                'Overnight Stay: Premium Eco-Luxury Resort, Araku Valley.',
            ]),
            _day(4, 'ARAKU TO VIZAG — MOUNTAIN WATERFALLS & HOMEWARD DEPARTURE', ('Savor a fresh cup of organic Araku coffee on the veranda of your resort while taking in views of the mist rising from the hills. After breakfast, start your descent back toward the plains, making a scenic stop at the beautiful Chaprai Waterfalls (Dumbriguda Waterfalls). Your private luxury vehicle carries you smoothly back down to Visakhapatnam. Depending on your flight or train departure schedule, your chauffeur can make a final shopping stop in the city for local handloom fabrics before transferring you seamlessly to Visakhapatnam Airport or Railway Station for your journey home.'), [
                'Sightseeing Included: Chaprai Waterfalls, local handloom textile bazaar stop, private departure transfer.',
                'Meals Included: Premium Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('The Gateway Hotel (Ocean Drive) / Novotel RK Beach', 'Visakhapatnam', '02 Nights', 'Deluxe', 'Deluxe Room', 'MAPAI (Breakfast & Dinner)', 4, 1, description='OPTION 01 – DELUXE: The Gateway Hotel (Ocean Drive) / Novotel RK Beach (Visakhapatnam, 02 Nights)'),
            _hotel('MPT Haritha Hill Resort', 'Araku Valley', '01 Night', 'Deluxe', 'Standard Room', 'MAPAI (Breakfast & Dinner)', 4, 2, description='OPTION 01 – DELUXE: MPT Haritha Hill Resort (Araku Valley, 01 Night)'),
            _hotel('Novotel Visakhapatnam Varun Beach (Superior)', 'Visakhapatnam', '02 Nights', 'Premium', 'Superior Room', 'MAPAI (Breakfast & Dinner)', 4, 3, description='OPTION 02 – PREMIUM: Novotel Visakhapatnam Varun Beach (Visakhapatnam, 02 Nights)'),
            _hotel('MPT Haritha Valley Resort (Luxury Suites)', 'Araku Valley', '01 Night', 'Premium', 'Luxury Suite', 'MAPAI (Breakfast & Dinner)', 4, 4, description='OPTION 02 – PREMIUM: MPT Haritha Valley Resort (Araku Valley, 01 Night)'),
            _hotel('Radisson Blu Resort Vishakhapatnam (Ocean View)', 'Visakhapatnam', '02 Nights', 'Luxury', 'Ocean View Room', 'MAPAI (Breakfast & Dinner)', 5, 5, description='OPTION 03 – LUXURY: Radisson Blu Resort Vishakhapatnam (Visakhapatnam, 02 Nights)'),
            _hotel('Araku Eco-Luxury Glamping Tents', 'Araku Valley', '01 Night', 'Luxury', 'Glamping Tent', 'MAPAI (Breakfast & Dinner)', 5, 6, description='OPTION 03 – LUXURY: Araku Eco-Luxury Glamping Tents (Araku Valley, 01 Night)'),
            _hotel('The Park Visakhapatnam (Private Luxury Beach Studio)', 'Visakhapatnam', '02 Nights', 'Ultra Luxury', 'Private Luxury Beach Studio', 'VIP Chef\'s Curated MAPAI', 5, 7, description='OPTION 04 – ULTRA LUXURY: The Park Visakhapatnam (Visakhapatnam, 02 Nights)'),
            _hotel('The Araku Valley Wilderness Heritage Manor', 'Araku Valley', '01 Night', 'Ultra Luxury', 'Heritage Manor Suite', 'VIP Chef\'s Curated MAPAI', 5, 8, description='OPTION 04 – ULTRA LUXURY: The Araku Valley Wilderness Heritage Manor (Araku Valley, 01 Night)'),
        ],
        inclusions=[
            _inc_included('Premium Stays: 03 Nights elite accommodation across handpicked beach resorts and eco-luxury hill properties.', 1),
            _inc_included('Gourmet Dining: Daily buffet breakfast and chef-curated multi-course dinners at all properties.', 2),
            _inc_included('Luxury Transportation: Private air-conditioned luxury vehicle for all airport/station transfers, sightseeing routes, and intercity travel as per itinerary.', 3),
            _inc_included('TRAGUIN Signatures: Exclusive cliffside sunset high tea arrangement in Vizag and custom destination welcome kits.', 4),
            _inc_included('Welcome Amenities: Royal traditional welcomes, fresh floral treats, and premium mineral water bottles provided daily inside the vehicle.', 5),
            _inc_included('Assistance & Taxes: 24/7 dedicated support from TRAGUIN holiday specialists, covered tolls, fuel costs, state taxes, and driver allowances.', 6),
            _inc_excluded('Air / Train Fares: Main intercity transport tickets to and from Visakhapatnam.', 7),
            _inc_excluded('Monument Entry Fees: Entry tickets to submarines, ropeway passes, caves, and individual camera permits.', 8),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, alcoholic beverages, spa therapies, and personal tips.', 9),
            _inc_excluded('Optional Extras: Speedboat rides at Rushikonda Beach or any items not specifically listed in final inclusions.', 10),
        ],
    )
    return package, itinerary

def build_ap_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AP-004'
    tour_code = 'TG-AP-AVF-004'
    title = 'TRAGUIN Premium Araku Valley Tour Package'
    duration = '04 Nights / 05 Days'
    slug = 'ap-004-coastal-hills-symphony-vizag-araku'
    itin_slug = 'ap-004-coastal-hills-symphony-vizag-araku-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Andhra Pradesh / India | Category: Premium Family Tour Package', 2),
            _ph('Destinations: Visakhapatnam (Vizag) • Araku Valley', 3),
            _ph('Ideal for: Families, Nature Lovers & Leisure Seekers', 4),
            _ph('Best season: October to March (Pleasant and misty)', 5),
            _ph('Starting price: On Request (Premium Luxury Tier)', 6),
            _ph('Vehicle: Private AC Luxury SUV (Innova Crysta / Equivalent) | Meal Plan: Premium Breakfast & Dinner (MAPAI)', 7),
            _ph('Route Plan: Visakhapatnam (2N) → Araku Valley (2N) → Visakhapatnam Departure', 8),
            _ph('TRAGUIN Curated Experience Note: Private panoramic Vistadome train ride ascending through tunnels and valleys, aromatic coffee tasting tour within organic estates, and private Dhimsa tribal dance demonstration designed exclusively for your family circle.', 9),
            _ph('TRAGUIN Signature Experience: Private family Vistadome train experience across the majestic Eastern Ghats mountains.', 10),
            _ph('Curated by TRAGUIN Experts: Every resort cottage, transport route, and driver is rigorously vetted to guarantee premium safety and luxury for families.', 11),
            _ph('Personalized Assistance: Dedicated 24/7 holiday consultant assigned specifically to your family from booking until your return flight.', 12),
            _ph('Premium Handpicked Hotels: Stay at incredible properties, ranging from sea-facing Novotel rooms to tranquil green valley resorts.', 13),
            _ph('Exclusive Recommendations: Handselected list of culinary recommendations, local markets, and sunset viewpoints carefully curated by destination experts.', 14),
            _ph('Shopping & Local Experiences: Araku Coffee & Chocolates, Famous Bamboo Chicken, Etikoppaka Toys, Vizag Silk Bazaars (Pochampally, Dharmavaram, Gadwal sarees).', 15),
            _ph('Important Notes: Hotel Check-in/out 14:00 / 11:00 hrs. Vistadome Bookings open 60 days in advance. Borra Caves: wear comfortable walking shoes. Advance Booking Suggestions: 45–60 days ahead for peak winter holidays.', 16),
        ],
        moods=['Family', 'Nature', 'Coastal', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='The Coastal & Hills Symphony: Visakhapatnam • Araku Valley • 04 Nights / 05 Days',
        overview=(
            'Welcome to a breathtaking world where the azure waters of the Bay of Bengal embrace the misty coffee-scented heights of the Eastern Ghats. The Best Andhra Pradesh Tour Package, conceptualized exclusively by TRAGUIN, invites your family to unwind amidst scenic beauty and cultural rich landmarks.\n\nTOUR OVERVIEW\nThis premium Araku Valley Family Tour delivers a magnificent experience of two diverse landscapes: the energetic, clean coastal vibes of Visakhapatnam (Vizag) and the pristine, soothing hill stations of Araku Valley.\n\nWHY CHOOSE THE PREMIUM ARAKU VALLEY EXPERIENCE?\nIconic Attractions include RK Beach, Rushikonda, INS Kursura Submarine Museum, Borra Caves, and Padmapuram Gardens. Best Time to Visit Araku Valley: October to March offers refreshing hill breezes and misty mornings.'
        ),
        seo_title='AP-004 | Premium Araku Valley Tour Package | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Vizag-Araku package (AP-004 / TG-AP-AVF-004): Vistadome train, Borra Caves, Rushikonda speedboating, Dhimsa dance, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('RK Beach, INS Kursura Submarine Museum, TU 142 Aircraft Museum, and Kailasagiri Ropeway', 1),
            _ih('Rushikonda Beach private speedboating, Thotlakonda, and Yarada Secluded Beach', 2),
            _ih('Vistadome Train Route, Araku Tribal Museum, and private Dhimsa Tribal Dance performance', 3),
            _ih('Borra Caves, Coffee Estates, Padmapuram Gardens, Chaprai Waterfalls, and Galikonda View Point', 4),
            _ih('TRAGUIN Signature Experience: Private family Vistadome train across the Eastern Ghats', 5),
        ],
        days=[
            _day(1, 'VISAKHAPATNAM — ARRIVAL & EXPLORING THE COASTAL QUEEN', ('Your premium family getaway begins as you arrive at Visakhapatnam Airport or Railway Station. You are warmly received by your dedicated TRAGUIN chauffeur and tour manager with premium welcoming kits. Transfer comfortably to your handpicked luxury beachfront hotel. After a seamless check-in and an absolute fresh lunch, begin your Visakhapatnam Sightseeing exploration. Visit the iconic INS Kursura Submarine Museum, a real decommissioned Soviet-built submarine standing proudly on the sands of Ramakrishna Beach. Next, explore the adjacent TU 142 Aircraft Museum. In the evening, take a leisurely stroll down the beautifully illuminated RK Beach road or experience a breathtaking panoramic view of the harbor city from the summit of Kailasagiri Hill, accessed via an exciting ropeway ride. Return to the resort for an exquisite sea-facing gourmet dinner.'), [
                'Sightseeing Included: RK Beach, INS Kursura Submarine Museum, TU 142 Aircraft Museum, Kailasagiri Ropeway.',
                'Evening Experience: Breathtaking sunset from Kailasagiri Hill overlooking the coastal expanse.',
                'Meals Included: Welcome Signature Drink & Gourmet Multi-cuisine Dinner.',
                'Overnight Stay: Premium Beachfront Resort, Visakhapatnam.',
            ]),
            _day(2, 'VISAKHAPATNAM — COASTAL MARVELS & GOLDEN BEACH EXPERIENCES', ('Wake up early to witness a glorious, unforgettable sunrise directly over the Bay of Bengal. After a sumptuous breakfast, continue your premium Andhra Pradesh Sightseeing trail. Drive along the spectacular marine road to the pristine Rushikonda Beach, renowned for its clean sand and gentle surf. Enjoy a TRAGUIN Signature Experience: a private speed-boating excursion across the blue waters under professional guidance. In the afternoon, discover the ancient historical heritage at Thotlakonda, a serene Buddhist monastic complex perched high on a hill overlooking the sea, dating back over 2,000 years. Later, find tranquility inside the Yarada Beach, a secluded pristine beach bordered by high green cliffs on three sides. Capture beautiful family photographs before returning to your hotel for a relaxed evening.'), [
                'Sightseeing Included: Rushikonda Beach, Thotlakonda Buddhist Complex, Yarada Secluded Beach, Dolphin\'s Nose Lighthouse.',
                'Optional Activities: Adventurous jet-skiing or surfing lessons at Rushikonda Beach.',
                'Evening Experience: Relaxed high-tea experience at a cliffside cafe overlooking the ocean.',
                'Meals Included: Buffet Breakfast & Specially Prepared Seafood Theme Dinner.',
                'Overnight Stay: Premium Beachfront Resort, Visakhapatnam.',
            ]),
            _day(3, 'VISAKHAPATNAM TO ARAKU VALLEY — THE ENCHANTING VISTADOME RAIL JOURNEY', ('An extraordinary morning awaits your family. After a light early breakfast, your chauffeur transfers you to the Visakhapatnam Railway Station to board the prestigious Vistadome Train to Araku. Recline inside an ultra-modern coach featuring massive glass ceilings and 360-degree rotating seats. Journey across the breathtaking landscapes of the Eastern Ghats, passing through more than 80 tunnels, soaring bridges, and deep green valleys. Your private luxury vehicle will meet you seamlessly as you step out at Araku Station. Check into your premium valley-view eco-resort. In the afternoon, explore the Araku Tribal Museum, showcasing the colorful heritage, lifestyle, and traditional arts of the local indigenous tribes. Conclude your day with an exclusive experience: a private performance of the traditional Dhimsa Dance organized by TRAGUIN within your resort lawns.'), [
                'Sightseeing Included: Vistadome Train Route, Araku Tribal Museum, Local Artisans Market.',
                'Evening Experience: Private Dhimsa Tribal Dance performance with campfire setup.',
                'Meals Included: Breakfast, Light Train Snacks, & Curated Authentic Mountain Dinner.',
                'Overnight Stay: Luxury Valley Eco-Resort, Araku Valley.',
            ]),
            _day(4, 'ARAKU VALLEY — SUBTERRANEAN CAVES & COFFEE PLANTATIONS', ('Relish a fresh breakfast enveloped by mountain mist. Your day is filled with incredible Araku Valley Sightseeing wonders. Head first toward the remarkable Borra Caves, millions-of-years-old limestone formations buried deep inside the Ananthagiri Hills. Next, take a private stroll through the aromatic Araku Coffee Plantations and enjoy an exclusive coffee-tasting session. In the afternoon, wander among the wooden treehouses and rare botanical species inside Padmapuram Gardens, followed by a refreshing stop at the cascading Chaprai Waterfalls. Return to your resort for a special family farewell dinner.'), [
                'Sightseeing Included: Borra Caves, Coffee Estates, Padmapuram Gardens, Chaprai Waterfalls, Galikonda View Point.',
                'Optional Activities: A light trekking trail along the Ananthagiri forest hills.',
                'Evening Experience: Spectacular mountain sunset views from the high Galikonda View Point.',
                'Meals Included: Gourmet Breakfast, Local Culinary Lunch, & Grand Farewell Dinner.',
                'Overnight Stay: Luxury Valley Eco-Resort, Araku Valley.',
            ]),
            _day(5, 'ARAKU VALLEY TO VISAKHAPATNAM — DEPARTURE WITH PRECIOUS MEMORIES', ('Indulge in a final hearty breakfast on your resort balcony as the morning clouds roll across the valley. Complete your check-out and board your luxury private vehicle for a scenic drive descending down the winding ghat roads back toward the coast. On the way, stop at the beautiful Tatipudi Reservoir, a peaceful oasis of blue water bordered by hills, ideal for a quiet break. Depending on your schedule, your private chauffeur will drop you comfortably at the Visakhapatnam Airport or Railway Station for your return home.'), [
                'Sightseeing Included: Winding Ghat Road Drive, Tatipudi Reservoir stop, Private Departure Transfer.',
                'Meals Included: Premium Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('The Gateway Hotel RK Beach (Standard)', 'Visakhapatnam', '02 Nights', 'Deluxe', 'Standard Room', 'Breakfast & Dinner', 4, 1, description='OPTION 01 – DELUXE: The Gateway Hotel RK Beach (Visakhapatnam, 02 Nights)'),
            _hotel('MPT Haritha Hill Resort', 'Araku Valley', '02 Nights', 'Deluxe', 'Standard Room', 'Breakfast & Dinner', 4, 2, description='OPTION 01 – DELUXE: MPT Haritha Hill Resort (Araku Valley, 02 Nights)'),
            _hotel('Novotel Visakhapatnam Varun Beach (Superior)', 'Visakhapatnam', '02 Nights', 'Premium', 'Superior Room', 'Breakfast & Dinner', 4, 3, description='OPTION 02 – PREMIUM: Novotel Visakhapatnam Varun Beach (Visakhapatnam, 02 Nights)'),
            _hotel('MPT Haritha Valley Resort (Luxury AC)', 'Araku Valley', '02 Nights', 'Premium', 'Luxury AC Room', 'Breakfast & Dinner', 4, 4, description='OPTION 02 – PREMIUM: MPT Haritha Valley Resort (Araku Valley, 02 Nights)'),
            _hotel('Novotel Varun Beach (Ocean View Executive)', 'Visakhapatnam', '02 Nights', 'Luxury', 'Ocean View Executive', 'Breakfast & Dinner', 5, 5, description='OPTION 03 – LUXURY: Novotel Varun Beach Ocean View Executive (Visakhapatnam, 02 Nights)'),
            _hotel('Araku Valley Eco Lodges / Private Cottages', 'Araku Valley', '02 Nights', 'Luxury', 'Private Cottage', 'Breakfast & Dinner', 5, 6, description='OPTION 03 – LUXURY: Araku Valley Eco Lodges / Private Cottages (Araku Valley, 02 Nights)'),
            _hotel('The Park Visakhapatnam (Luxury Ocean Suite)', 'Visakhapatnam', '02 Nights', 'Ultra Luxury', 'Luxury Ocean Suite', 'Breakfast & Dinner', 5, 7, description='OPTION 04 – ULTRA LUXURY: The Park Visakhapatnam (Visakhapatnam, 02 Nights)'),
            _hotel('Exclusive Luxury Wilderness Villa Retreat', 'Araku Valley', '02 Nights', 'Ultra Luxury', 'Wilderness Villa', 'Breakfast & Dinner', 5, 8, description='OPTION 04 – ULTRA LUXURY: Exclusive Luxury Wilderness Villa Retreat (Araku Valley, 02 Nights)'),
        ],
        inclusions=[
            _inc_included('Premium Stays: 04 Nights luxury accommodation at our handpicked premium hotels and eco-resorts.', 1),
            _inc_included('Gourmet Dining: Daily buffet breakfasts and curated multi-cuisine dinners at all hotels.', 2),
            _inc_included('Luxury Transportation: Private air-conditioned luxury vehicle (Toyota Innova Crysta) for all transfers, drives, and sightseeing.', 3),
            _inc_included('Exclusive Train Access: Pre-booked Vistadome Premium Train tickets from Visakhapatnam to Araku Valley.', 4),
            _inc_included('Welcome Amenities: Royal traditional welcomes at resorts, fresh fruit baskets, and premium mineral water provided daily inside your car.', 5),
            _inc_included('Complimentary Experiences: Private Speedboating at Rushikonda Beach and an exclusive Dhimsa Tribal Dance performance.', 6),
            _inc_included('TRAGUIN Support: 24/7 dedicated concierge assistance from our expert team, with all toll taxes, fuel, parking, and driver allowances fully covered.', 7),
            _inc_excluded('Main Airfare / Rail: Intercity flight or train tickets to and from Visakhapatnam.', 8),
            _inc_excluded('Monument Entry Tickets: Individual entrance fees at museums, gardens, and caves unless stated otherwise.', 9),
            _inc_excluded('Personal Expenses: Laundry services, telephone calls, alcoholic drinks, spa sessions, and optional tipping.', 10),
            _inc_excluded('Optional Activities: Water sports at beaches or extra items not specified inside inclusions.', 11),
        ],
    )
    return package, itinerary

def build_ap_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AP-005'
    tour_code = 'TG-AP-ARH-005'
    title = 'TRAGUIN Premium Araku Valley Honeymoon Package'
    duration = '04 Nights / 05 Days'
    slug = 'ap-005-romantic-coastal-hills-araku-honeymoon'
    itin_slug = 'ap-005-romantic-coastal-hills-araku-honeymoon-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Andhra Pradesh / India | Category: Romantic Honeymoon FIT', 2),
            _ph('Destinations: Visakhapatnam (Vizag) • Araku Valley', 3),
            _ph('Ideal for: Newlyweds & Couples', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium Luxury Tier)', 6),
            _ph('Vehicle: Private AC Luxury SUV | Meal Plan: Premium MAPAI (Breakfast & Romantic Dinners)', 7),
            _ph('Route Plan: Visakhapatnam Arrival → Araku Valley (2N) → Visakhapatnam (2N) → Departure', 8),
            _ph('TRAGUIN Curated Experience Note: Private scenic Vistadome train ride, intimate couples-only coffee tasting, and special celebratory room decorations with premium welcoming amenities.', 9),
            _ph('TRAGUIN Signature Experience: Private Vistadome train ride across the majestic Eastern Ghats mountains.', 10),
            _ph('Curated by TRAGUIN Experts: Every resort, transport route, and driver rigorously vetted for safety, privacy, and comfort.', 11),
            _ph('Personalized Assistance: Elite, dedicated travel coordinator available around the clock.', 12),
            _ph('Premium Handpicked Hotels: Beautifully managed properties showcasing vast views and unmatched romance.', 13),
            _ph('Exclusive Recommendations: Hidden viewpoints, quiet cafes, and sunset spots away from the crowds.', 14),
            _ph('Shopping & Local Experiences: Araku Coffee, Bamboo Chicken, Etikoppaka wooden toys, photography hotspots.', 15),
            _ph('Important Notes: Hotel check-in 14:00 / check-out 11:00 hrs. Vistadome tickets secured 60 days in advance. Book 45–60 days ahead for peak holidays.', 16),
        ],
        moods=['Honeymoon', 'Romance', 'Coastal', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='The Romantic Coastal & Hills Escape • Visakhapatnam • Araku Valley • 04 Nights / 05 Days',
        overview=(
            'Welcome to your forever beginning. The Best Araku Valley Honeymoon Package, meticulously handcrafted by TRAGUIN, invites you and your beloved to celebrate your love amidst the azure coastal beauty of Vizag and the mist-kissed, coffee-scented heights of Araku Valley.\n\nTOUR OVERVIEW\nThis customized Araku Valley Honeymoon Package offers an intimate sanctuary from the outside world with seamless personalized handling, private luxury transport, romantic handpicked premium hotels, and chef-curated candlelit dining plans.\n\nWHY CHOOSE THE PREMIUM ARAKU VALLEY HONEYMOON TRAIL?\nIconic Attractions include Chaprai Waterfalls, Borra Caves, Galikonda View Point, and serene coffee plantations. Best Time to Visit: October to March.'
        ),
        seo_title='AP-005 | Premium Araku Valley Honeymoon Package | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Araku honeymoon package (AP-005 / TG-AP-ARH-005): Vistadome train, Borra Caves, Yarada Beach picnic, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Vistadome Train Journey and romantic candlelit dinner at Araku eco-resort', 1),
            _ih('Borra Caves, Coffee Estates, Galikonda View Point, and Padmapuram Gardens', 2),
            _ih('Chaprai Waterfalls, Araku Tribal Museum, and quiet RK Beach evening stroll', 3),
            _ih('INS Kursura Submarine Museum, Kailasagiri Hill, and Yarada Beach picnic hamper', 4),
            _ih('TRAGUIN Signature Experience: Private Vistadome train ride across the Eastern Ghats', 5),
        ],
        days=[
            _day(1, 'ARRIVAL & TRANSITION TO THE ENCHANTING HILLS', ('Your romantic adventure begins as you arrive at Visakhapatnam. Your dedicated TRAGUIN private chauffeur welcomes you with traditional hospitality. Board the prestigious Vistadome Train to Araku—a scenic masterpiece. Upon arriving in the serene Araku Valley, check into your romantic handpicked luxury eco-resort. Enjoy a smooth check-in, a special welcome cake, and floral room decorations. Return to your resort for a curated candlelit dinner under the stars.'), [
                'Sightseeing Included: Vistadome Train Journey, Scenic mountain drive.',
                'Evening Experience: Private Lakeside Stroll and a Romantic Candlelit Dinner at the resort.',
                'Meals Included: Welcome Drinks, Honeymoon Cake, & Gourmet Dinner.',
                'Overnight Stay: Handpicked Premium Luxury Eco-Resort, Araku.',
            ]),
            _day(2, 'MYSTICAL CAVES & AROMATIC COFFEE ESTATES', ('Savor a luxurious breakfast before an immersive day of Araku Valley Sightseeing. Begin at the ancient Borra Caves, perfect for your first couple\'s photo session. Next, enjoy a private couples-only coffee tasting in organic Araku Coffee Plantations. Visit Galikonda View Point for a quiet sunset moment over infinite ridges.'), [
                'Sightseeing Included: Borra Caves, Coffee Estates, Galikonda View Point, Padmapuram Gardens.',
                'Evening Experience: Private sunset viewing followed by a cozy evening at the resort.',
                'Meals Included: Buffet Breakfast & Specially Curated Traditional Dinner.',
                'Overnight Stay: Handpicked Premium Luxury Eco-Resort, Araku.',
            ]),
            _day(3, 'ARAKU TO VISAKHAPATNAM — CASCADING FALLS & COASTAL BLISS', ('After breakfast, visit Chaprai Waterfalls and the Araku Tribal Museum. Your luxury vehicle whisks you back toward Visakhapatnam. Check into your premium beachfront hotel. In the evening, take a quiet walk on RK Beach before an exquisite sea-facing gourmet dinner.'), [
                'Sightseeing Included: Chaprai Waterfalls, Araku Tribal Museum, Scenic Ghat Drive.',
                'Optional Activities: A soothing, couples-only wellness massage at a luxury spa.',
                'Evening Experience: Quiet evening beach stroll along the Visakhapatnam coastline.',
                'Meals Included: Premium Breakfast & Multi-cuisine Fine Dining Dinner.',
                'Overnight Stay: Premium Luxury Beachfront Hotel, Visakhapatnam.',
            ]),
            _day(4, 'VISAKHAPATNAM — COASTAL MARVELS & SUNSET ROMANCE', ('Explore the INS Kursura Submarine Museum and Kailasagiri Hill. Enjoy a TRAGUIN Signature Experience: a premium picnic hamper lunch near secluded Yarada Beach. Conclude with a grand farewell dinner arranged by the hotel\'s master chefs.'), [
                'Sightseeing Included: Submarine Museum, Kailasagiri Hill, Yarada Beach, Thotlakonda Buddhist site.',
                'Evening Experience: Special TRAGUIN Farewell Theme Dinner with a complimentary customized souvenir.',
                'Meals Included: Gourmet Breakfast, Signature Picnic Hamper Lunch, & Grand Farewell Dinner.',
                'Overnight Stay: Premium Luxury Beachfront Hotel, Visakhapatnam.',
            ]),
            _day(5, 'DEPARTURE WITH UNFORGETTABLE MEMORIES', ('Share a final morning breakfast overlooking the sea. Your private chauffeur transfers you to the Airport or Railway Station. Your unforgettable Luxury Araku Valley Holiday concludes, curated flawlessly by TRAGUIN.'), [
                'Sightseeing Included: Departure transfer via your private luxury vehicle.',
                'Meals Included: Premium Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Gateway Hotel / Haritha Hill Resort', 'Araku Valley', '02 Nights', 'Deluxe', 'Premium Room', 'MAPAI', 4, 1, description='OPTION 01 – DELUXE: Gateway Hotel / Haritha Hill Resort (Araku Valley, 02 Nights)'),
            _hotel('Gateway Hotel / Haritha Hill Resort', 'Visakhapatnam', '02 Nights', 'Deluxe', 'Premium Room', 'MAPAI', 4, 2, description='OPTION 01 – DELUXE: Gateway Hotel / Haritha Hill Resort (Visakhapatnam, 02 Nights)'),
            _hotel('Novotel Varun Beach / Haritha Valley', 'Araku Valley', '02 Nights', 'Premium', 'Sea View Room', 'MAPAI', 4, 3, description='OPTION 02 – PREMIUM: Novotel Varun Beach / Haritha Valley (Araku Valley, 02 Nights)'),
            _hotel('Novotel Varun Beach / Haritha Valley', 'Visakhapatnam', '02 Nights', 'Premium', 'Sea View Room', 'MAPAI', 4, 4, description='OPTION 02 – PREMIUM: Novotel Varun Beach / Haritha Valley (Visakhapatnam, 02 Nights)'),
            _hotel('Novotel Varun Beach / Araku Eco Lodges', 'Araku Valley', '02 Nights', 'Luxury', 'Luxury Suite', 'MAPAI & Honeymoon Perks', 5, 5, description='OPTION 03 – LUXURY: Novotel Varun Beach / Araku Eco Lodges (Araku Valley, 02 Nights)'),
            _hotel('Novotel Varun Beach / Araku Eco Lodges', 'Visakhapatnam', '02 Nights', 'Luxury', 'Luxury Suite', 'MAPAI & Honeymoon Perks', 5, 6, description='OPTION 03 – LUXURY: Novotel Varun Beach / Araku Eco Lodges (Visakhapatnam, 02 Nights)'),
            _hotel('The Park Vizag / Luxury Villa', 'Araku Valley', '02 Nights', 'Ultra Luxury', 'Royal Ocean Suite', 'MAPAI & VIP Signatures', 5, 7, description='OPTION 04 – ULTRA LUXURY: The Park Vizag / Luxury Villa (Araku Valley, 02 Nights)'),
            _hotel('The Park Vizag / Luxury Villa', 'Visakhapatnam', '02 Nights', 'Ultra Luxury', 'Royal Ocean Suite', 'MAPAI & VIP Signatures', 5, 8, description='OPTION 04 – ULTRA LUXURY: The Park Vizag / Luxury Villa (Visakhapatnam, 02 Nights)'),
        ],
        inclusions=[
            _inc_included('Premium Stays: 04 Nights luxury accommodation at handpicked premium resorts.', 1),
            _inc_included('Gourmet Dining: Daily buffet breakfast and custom-designed romantic dinners at your resort.', 2),
            _inc_included('Luxury Transportation: Private air-conditioned luxury SUV for all airport/station transfers and sightseeing.', 3),
            _inc_included('Exclusive Train Tickets: Pre-booked premium Vistadome tickets for your mountain ascent.', 4),
            _inc_included('Welcome Amenities: Royal traditional welcome, complimentary honeymoon cake, artisanal chocolates, and daily premium mineral water.', 5),
            _inc_included('TRAGUIN Support: 24/7 dedicated virtual concierge assistance, with all fuel, tolls, and driver allowances covered.', 6),
            _inc_excluded('Travel Tickets: Commercial flights or railway tickets to/from Visakhapatnam.', 7),
            _inc_excluded('Entry Tickets: Mandatory forest department permits, guide fees, and individual monument entry tickets.', 8),
            _inc_excluded('Personal Expenses: Laundry, premium room service, telephone calls, alcoholic beverages, and tips.', 9),
            _inc_excluded('Optional Tours: Spa therapies, adventure sports, or any activities not explicitly included.', 10),
            _inc_excluded('Insurance: Travel or medical insurance coverage plans.', 11),
        ],
    )
    return package, itinerary

def build_ap_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AP-006'
    tour_code = 'TG-AP-VIZ-006'
    title = 'TRAGUIN Premium Vizag-Araku Family Tour'
    duration = '05 Nights / 06 Days'
    slug = 'ap-006-vizag-araku-family-tour'
    itin_slug = 'ap-006-vizag-araku-family-tour-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Andhra Pradesh / India | Category: Premium Family Tour', 2),
            _ph('Destinations: Visakhapatnam (Vizag) • Araku Valley', 3),
            _ph('The Coastal & Hills Symphony: Visakhapatnam • Araku Valley', 4),
            _ph('TOUR OVERVIEW: Discover the perfect blend of coastal charm and hill station tranquility with curated experiences from Vistadome train journeys to beachfront relaxation.', 5),
            _ph('WHY VISIT: Visakhapatnam offers urban beaches and naval history; Araku Valley provides coffee plantations and limestone wonders.', 6),
        ],
        moods=['Family', 'Coastal', 'Nature', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request',
        rating=Decimal("4.9"), review_count=0,
        tagline='The Coastal & Hills Symphony: Visakhapatnam • Araku Valley • 05 Nights / 06 Days',
        overview=(
            'Discover the perfect blend of coastal charm and hill station tranquility with this Best Andhra Pradesh Tour Package. Curated by TRAGUIN, this 5-night family odyssey ensures unforgettable memories, offering curated experiences that range from Vistadome train journeys to beachfront relaxation.\n\nWHY VISIT VISAKHAPATNAM & ARAKU VALLEY?\nAs one of the most sought-after Top Tourist Places in Andhra Pradesh, Visakhapatnam offers a unique mix of urban beaches and naval history, while Araku Valley provides breathtaking landscapes of coffee plantations and limestone wonders. This is the Best Time to Visit Araku Valley for families seeking a Premium Araku Valley Experience.'
        ),
        seo_title='AP-006 | Premium Vizag-Araku Family Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Vizag-Araku family package (AP-006 / TG-AP-VIZ-006): RK Beach, Vistadome train, Borra Caves, Chaprai Waterfalls, and TRAGUIN curated experiences.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('RK Beach and Submarine Museum on arrival evening in Vizag', 1),
            _ih('Rushikonda Beach, Thotlakonda, and Kailasagiri Hill scenic beauty', 2),
            _ih('Iconic Vistadome train with breathtaking Eastern Ghats landscapes', 3),
            _ih('Borra Caves, coffee estates, Chaprai Waterfalls, and local tribal culture', 4),
            _ih('TRAGUIN curated Vistadome train experience and smooth departure support', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN VIZAG', ('Arrive in Visakhapatnam. Transfer to a handpicked hotel by TRAGUIN. Evening visit to RK Beach and the Submarine Museum.'), [
                'Sightseeing Included: RK Beach, Submarine Museum.',
                'Overnight Stay: Vizag.',
            ]),
            _day(2, 'VIZAG COASTAL BEAUTY', ('Visit Rushikonda Beach, Thotlakonda, and the Kailasagiri Hill for scenic beauty.'), [
                'Sightseeing Included: Rushikonda Beach, Thotlakonda, Kailasagiri Hill.',
                'Overnight Stay: Vizag.',
            ]),
            _day(3, 'VISTADOME TRAIN TO ARAKU', ('Board the iconic Vistadome train. Enjoy breathtaking landscapes. Check into an Araku Valley luxury hotel.'), [
                'Sightseeing Included: Vistadome train journey, scenic ghat landscapes.',
                'Overnight Stay: Araku.',
            ]),
            _day(4, 'ARAKU VALLEY EXPLORATION', ('Visit Borra Caves, coffee estates, and Chaprai Waterfalls. Enjoy immersive experiences with local tribal culture.'), [
                'Sightseeing Included: Borra Caves, coffee estates, Chaprai Waterfalls, local tribal culture.',
                'Overnight Stay: Araku.',
            ]),
            _day(5, 'RETURN TO VIZAG', ('Drive back to Vizag via scenic mountain roads. Enjoy an exclusive experience at a beachside cafe.'), [
                'Sightseeing Included: Scenic mountain road drive, beachside cafe experience.',
                'Overnight Stay: Vizag.',
            ]),
            _day(6, 'DEPARTURE', ('Final breakfast before departure. TRAGUIN support ensures a smooth exit.'), [
                'Meals Included: Breakfast.',
            ]),
        ],
        hotels=[],
        inclusions=[
            _inc_included('Premium stays for 05 nights.', 1),
            _inc_included('Daily meals, transfers, and sightseeing.', 2),
            _inc_included('TRAGUIN curated Vistadome train experience.', 3),
        ],
    )
    return package, itinerary

def build_ap_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AP-007'
    tour_code = 'TG-AP-SL-007'
    title = 'TRAGUIN Premium Andhra Leisure Tour'
    duration = '04 Nights / 05 Days'
    slug = 'ap-007-graceful-heritage-trail-vijayawada-vizag'
    itin_slug = 'ap-007-graceful-heritage-trail-vijayawada-vizag-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Andhra Pradesh / India | Category: Senior Leisure Comfort', 2),
            _ph('Destinations: Vijayawada • Amaravati • Vizag', 3),
            _ph('Ideal for: Senior Citizens & Relaxed Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Comfort & Luxury)', 6),
            _ph('Vehicle: Private AC Luxury SUV (Extra Comfort & Accessibility) | Meal Plan: Premium MAPAI (Easy-to-digest Breakfast & Comfort Dinners)', 7),
            _ph('Route Plan: Vijayawada Arrival → Amaravati → Visakhapatnam (Vizag) Departure', 8),
            _ph('TRAGUIN Curated Experience Note: Prioritized sightseeing slots to avoid crowds, easily accessible monument visits, comfortable hotel lounges, and dedicated 24/7 travel consultant.', 9),
            _ph('TRAGUIN Comfort Commitment: Manageable pacing, easy access, and professional care for every senior guest.', 10),
            _ph('Curated by TRAGUIN Experts: Every resort, transport route, and driver rigorously vetted to guarantee safety and comfort.', 11),
            _ph('Personalized Assistance: Elite travel coordinator available around the clock to manage every detail.', 12),
            _ph('Premium Handpicked Hotels: Properties known for excellence in service and accessibility.', 13),
            _ph('Local Immersive Experiences: Heritage Textiles (Pochampally and Dharmavaram silks), Spiritual Souvenirs, Coastal Crafts in Vizag beachfront markets.', 14),
            _ph('Important Notes: Itinerary paced to avoid long consecutive transit hours. Advance bookings recommended 45–60 days in advance.', 15),
        ],
        moods=['Leisure', 'Heritage', 'Senior', 'Coastal'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Comfort & Luxury)',
        rating=Decimal("4.9"), review_count=0,
        tagline='The Graceful Heritage Trail: Vijayawada • Amaravati • Vizag • 04 Nights / 05 Days',
        overview=(
            'Welcome to a journey of grace, history, and tranquil beauty. The Best Andhra Pradesh Leisure Package, meticulously curated by TRAGUIN, invites our distinguished senior guests to explore the spiritual heart and coastal serenity of Andhra Pradesh.\n\nTOUR OVERVIEW\nThis customized Senior Citizen Leisure Tour offers a calm, enriching sanctuary away from the hustle of standard tourist circuits. Experience personalized handling, private luxury transport, and handpicked premium properties known for their comfort and accessibility.\n\nWHY CHOOSE THE PREMIUM ANDHRA LEISURE TRAIL?\nIconic Attractions include Amaravati Stupa, Prakasam Barrage, Vijayawada temples, and Vizag coastlines. Best Time to Visit: October to March provides the most pleasant weather.'
        ),
        seo_title='AP-007 | Premium Andhra Leisure Tour | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Andhra leisure package (AP-007 / TG-AP-SL-007): Vijayawada, Amaravati Stupa, Vizag coastline, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Kanaka Durga Temple and Bhavani Island boat ride in Vijayawada', 1),
            _ih('Amaravati Stupa, Archaeological Site Museum, and Prakasam Barrage viewpoint', 2),
            _ih('Scenic coastal drive and lounge time overlooking the Bay of Bengal in Vizag', 3),
            _ih('INS Kursura Submarine Museum, TU 142 Aircraft Museum, and Kailasagiri Hill ropeway', 4),
            _ih('TRAGUIN Comfort Commitment: Manageable pacing and professional care for senior guests', 5),
        ],
        days=[
            _day(1, 'VIJAYAWADA — ARRIVAL & SPIRITUAL SERENITY', ('Your graceful journey begins as you arrive in Vijayawada. Your dedicated TRAGUIN private chauffeur welcomes you with traditional hospitality and signature care. Transfer comfortably to your premium, handpicked hotel. After a smooth check-in and a relaxed lunch, visit the peaceful Kanaka Durga Temple, perched on the Indrakeeladri hill. In the late afternoon, enjoy a quiet, scenic boat ride to Bhavani Island, where lush greenery and the gentle flow of the Krishna River provide a soothing, meditative atmosphere.'), [
                'Sightseeing Included: Kanaka Durga Temple, Bhavani Island boat ride.',
                'Evening Experience: Peaceful riverside evening spent in comfortable ambient surroundings.',
                'Meals Included: Welcome Drink, Refreshments, & Comfort Dinner.',
                'Overnight Stay: Premium Comfort Hotel, Vijayawada.',
            ]),
            _day(2, 'AMARAVATI — ANCIENT HERITAGE AT A GENTLE PACE', ('Savor a relaxed breakfast before a smooth, comfortable drive toward the historic Buddhist seat of Amaravati. Explore the magnificent Amaravati Stupa, a UNESCO-worthy architectural marvel featuring intricate stone relief carvings. Spend time in the site museum to admire the rich history of the Buddhist tradition in Andhra. Return to Vijayawada by late afternoon, allowing time to unwind in your hotel lounge.'), [
                'Sightseeing Included: Amaravati Stupa, Archaeological Site Museum, Prakasam Barrage viewpoint.',
                'Evening Experience: Leisurely time in the hotel lounge followed by a healthy, comforting dinner.',
                'Meals Included: Breakfast & Comfort Dinner.',
                'Overnight Stay: Premium Comfort Hotel, Vijayawada.',
            ]),
            _day(3, 'VIJAYAWADA TO VISAKHAPATNAM — COASTAL TRANSITIONS', ('After a leisurely morning breakfast, enjoy a comfortable, scenic drive toward the coastal city of Visakhapatnam with full assistance for baggage and comfort needs. Upon arrival in Vizag, settle into your premium beachfront hotel. In the late afternoon, take a relaxed drive along the coastal road and spend a quiet hour in a premium lounge overlooking the Bay of Bengal.'), [
                'Sightseeing Included: Scenic coastal drive, brief overview of the Vizag coastline.',
                'Evening Experience: Relaxed lounge time overlooking the Bay of Bengal.',
                'Meals Included: Breakfast & Comfort Dinner.',
                'Overnight Stay: Premium Beachfront Hotel, Visakhapatnam.',
            ]),
            _day(4, 'VISAKHAPATNAM — COASTAL SERENITY & CULTURAL IMMERSION', ('Today\'s Vizag Sightseeing is curated for comfort. Visit the INS Kursura Submarine Museum and the nearby TU 142 Aircraft Museum. The afternoon is kept free for your leisure. In the late afternoon, take a slow drive up to Kailasagiri Hill via the accessible ropeway, offering expansive, gentle views of the sea and city. Conclude your day with a special farewell dinner at your hotel.'), [
                'Sightseeing Included: Submarine Museum, Kailasagiri Hill, coastal view points.',
                'Evening Experience: Farewell dinner in a comfortable setting at your hotel.',
                'Meals Included: Breakfast, Light Afternoon Refreshments, & Farewell Dinner.',
                'Overnight Stay: Premium Beachfront Hotel, Visakhapatnam.',
            ]),
            _day(5, 'DEPARTURE — A GRACEFUL FAREWELL', ('Share a beautiful final morning breakfast by the sea. Take a gentle morning walk on the beach or sit by the resort garden, savoring the peaceful final hours of your holiday. Complete your check-out with our assistance and meet your private chauffeur for your smooth transfer back to the Airport or Railway Station.'), [
                'Sightseeing Included: Departure transfer via your private luxury vehicle.',
                'Meals Included: Premium Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Gateway Hotel (Standard)', 'Vijayawada / Visakhapatnam', '04 Nights', 'Deluxe', 'Comfort Room', 'MAPAI', 4, 1, description='OPTION 01 – DELUXE: Gateway Hotel (Standard) (Comfort Room)'),
            _hotel('Novotel Varun Beach (Superior)', 'Visakhapatnam', '04 Nights', 'Premium', 'Sea View Room', 'MAPAI', 4, 2, description='OPTION 02 – PREMIUM: Novotel Varun Beach (Superior) (Sea View Room)'),
            _hotel('Novotel Varun Beach (Executive)', 'Visakhapatnam', '04 Nights', 'Luxury', 'Luxury Ocean Suite', 'MAPAI', 5, 3, description='OPTION 03 – LUXURY: Novotel Varun Beach (Executive) (Luxury Ocean Suite)'),
            _hotel('The Park Visakhapatnam', 'Visakhapatnam', '04 Nights', 'Ultra Luxury', 'Royal Ocean Suite', 'MAPAI', 5, 4, description='OPTION 04 – ULTRA LUXURY: The Park Visakhapatnam (Royal Ocean Suite)'),
        ],
        inclusions=[
            _inc_included('Premium Stays: 04 Nights luxury accommodation at handpicked premium hotels.', 1),
            _inc_included('Gourmet Dining: Daily breakfast and chef-curated comfort dinners.', 2),
            _inc_included('Luxury Transportation: Private air-conditioned luxury SUV (Innova Crysta or equivalent) dedicated to your party throughout the tour.', 3),
            _inc_included('Concierge Assistance: Dedicated support from our holiday specialists to ensure comfort and ease at every site.', 4),
            _inc_included('TRAGUIN Support: 24/7 travel consultant access for all small needs, and all tolls, parking, and fuel costs included.', 5),
            _inc_excluded('Main Transport: Any commercial flight or railway tickets to/from Andhra Pradesh.', 6),
            _inc_excluded('Monument Fees: Individual entry tickets and camera fees.', 7),
            _inc_excluded('Personal Expenses: Laundry, medical costs, premium alcoholic drinks, and tips for local staff.', 8),
            _inc_excluded('Optional Extras: Any tours not explicitly listed in the inclusions.', 9),
        ],
    )
    return package, itinerary

def build_ap_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AP-008'
    tour_code = 'TG-AP-VIZ-008'
    title = 'TRAGUIN Premium Luxury Vizag Tour Package'
    duration = '05 Nights / 06 Days'
    slug = 'ap-008-luxury-vizag-coastal-symphony'
    itin_slug = 'ap-008-luxury-vizag-coastal-symphony-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Andhra Pradesh / India | Category: Ultra-Luxury Coastal Retreat', 2),
            _ph('Destinations: Visakhapatnam (Vizag)', 3),
            _ph('Ideal for: Luxury Travelers, Connoisseurs', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium Luxury Tier)', 6),
            _ph('Vehicle: Private AC Luxury SUV (Innova Crysta / Luxury Coach) | Meal Plan: Premium Breakfast & Fine Dining Dinners', 7),
            _ph('Route Plan: Visakhapatnam Arrival → Beachfront Luxury Resort (5 Nights) → Departure', 8),
            _ph('TRAGUIN Curated Experience Note: Private luxury yacht charter at sunset, sunrise breakfast setup on a secluded beach, and priority access to maritime heritage museums.', 9),
            _ph('TRAGUIN Signature Experience: Private luxury yacht charter on the Bay of Bengal at sunset.', 10),
        ],
        moods=['Luxury', 'Coastal', 'Leisure', 'Romance'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Luxury Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='The Coastal Symphony: Iconic Luxury in Visakhapatnam • 05 Nights / 06 Days',
        overview=(
            'Welcome to a realm of unparalleled coastal elegance. The Best Vizag Tour Package, meticulously handcrafted by TRAGUIN, invites you to experience the finest luxury escape along the Bay of Bengal.\n\nTOUR OVERVIEW\nThis customized Luxury Vizag Tour delivers a supreme experience of the coastal capital with private luxury transportation, premium beachfront suites, gourmet culinary experiences, and expert-led cultural tours.'
        ),
        seo_title='AP-008 | Premium Luxury Vizag Tour Package | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days luxury Vizag package (AP-008 / TG-AP-VIZ-008): Private yacht charter, Yarada Beach, Kailasagiri, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Luxury beachfront resort arrival and sunset welcome reception', 1),
            _ih('INS Kursura Submarine Museum, TU 142 Aircraft Museum, and Kailasagiri Ropeway', 2),
            _ih('Yarada Beach, Dolphin\'s Nose cliffs, and private sunset yacht cruise', 3),
            _ih('Thotlakonda Buddhist Complex, Rushikonda Beach drive, and luxury spa immersion', 4),
            _ih('TRAGUIN Signature Experience: Private luxury yacht sunset cruise on the Bay of Bengal', 5),
        ],
        days=[
            _day(1, 'ARRIVAL & COASTAL LUXURY INITIATION', ('Your grand escape begins as you arrive at Visakhapatnam Airport. A dedicated TRAGUIN chauffeur greets you with premium hospitality and escorts you to your luxury beachfront resort. Check into your sea-facing ocean suite. Spend the evening unwinding with a welcome cocktail by the infinity pool.'), [
                'Sightseeing Included: Luxury airport arrival, Beachfront Resort relaxation.',
                'Evening Experience: Sunset welcome reception at the beach resort.',
                'Meals Included: Welcome Signature Refreshments & Gourmet Fine Dining Dinner.',
                'Overnight Stay: Premium Luxury Beachfront Resort, Vizag.',
            ]),
            _day(2, 'VIZAG MARITIME LEGACY & SKYLINE VIEWS', ('Begin your day with a gourmet breakfast overlooking the ocean. Explore the INS Kursura Submarine Museum, followed by a visit to the TU 142 Aircraft Museum. In the afternoon, ascend Kailasagiri Hill via private ropeway for panoramic views of the coastal skyline.'), [
                'Sightseeing Included: Submarine Museum, Aircraft Museum, Kailasagiri Ropeway, RK Beach walk.',
                'Meals Included: Gourmet Breakfast, Lunch, & Fine Dining Dinner.',
                'Overnight Stay: Premium Luxury Beachfront Resort, Vizag.',
            ]),
            _day(3, 'SECLUDED SHORES & PRIVATE YACHTING', ('Head to the secluded Yarada Beach. In the afternoon, enjoy a TRAGUIN Signature Experience: a private luxury yacht charter on the Bay of Bengal with gourmet canapes and premium beverages at sunset.'), [
                'Sightseeing Included: Yarada Beach visit, Dolphin\'s Nose cliffs, Private Yacht Charter.',
                'Evening Experience: Private Sunset Yacht Cruise with music and gourmet snacks.',
                'Meals Included: Breakfast, Picnic Lunch, & Fine Dining Dinner.',
                'Overnight Stay: Premium Luxury Beachfront Resort, Vizag.',
            ]),
            _day(4, 'COASTAL HERITAGE & SPA IMMERSION', ('Explore the historic Buddhist site of Thotlakonda. Return to your resort for a TRAGUIN curated luxury spa treatment with local aromatics.'), [
                'Sightseeing Included: Thotlakonda Buddhist Complex, Rushikonda Beach drive.',
                'Evening Experience: Rejuvenating luxury spa session and leisurely seaside lounge evening.',
                'Meals Included: Gourmet Breakfast, Lunch, & Fine Dining Dinner.',
                'Overnight Stay: Premium Luxury Beachfront Resort, Vizag.',
            ]),
            _day(5, 'LEISURE, SHOPPING & FAREWELL GALA', ('Relax by the beach. Explore Vizag\'s premium markets for heritage textiles and local handicrafts. Join a grand TRAGUIN Farewell Gala Dinner at a boutique restaurant.'), [
                'Sightseeing Included: Leisure beach time, Premium shopping tour.',
                'Evening Experience: Grand Farewell Gala Dinner hosted by TRAGUIN team.',
                'Meals Included: Gourmet Breakfast, Lunch, & Farewell Gala Dinner.',
                'Overnight Stay: Premium Luxury Beachfront Resort, Vizag.',
            ]),
            _day(6, 'DEPARTURE WITH MEMORIES', ('Enjoy one final breakfast with ocean views. Your private chauffeur will transfer you to the airport, concluding your Luxury Vizag Holiday, crafted perfectly by TRAGUIN.'), [
                'Meals Included: Premium Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Gateway Hotel (Standard)', 'Visakhapatnam', '05 Nights', 'Deluxe', 'Standard Room', 'Breakfast & Dinner', 4, 1, description='OPTION 01 – DELUXE: Gateway Hotel (Standard) (Visakhapatnam, 05 Nights)'),
            _hotel('Novotel Varun Beach (Superior)', 'Visakhapatnam', '05 Nights', 'Premium', 'Superior Room', 'Breakfast & Dinner', 4, 2, description='OPTION 02 – PREMIUM: Novotel Varun Beach (Superior) (Visakhapatnam, 05 Nights)'),
            _hotel('Novotel Varun Beach (Executive Suite)', 'Visakhapatnam', '05 Nights', 'Luxury', 'Executive Suite', 'Breakfast & Dinner', 5, 3, description='OPTION 03 – LUXURY: Novotel Varun Beach (Executive Suite) (Visakhapatnam, 05 Nights)'),
            _hotel('The Park Visakhapatnam (Ocean Suite)', 'Visakhapatnam', '05 Nights', 'Ultra Luxury', 'Ocean Suite', 'Breakfast & Dinner', 5, 4, description='OPTION 04 – ULTRA LUXURY: The Park Visakhapatnam (Ocean Suite) (Visakhapatnam, 05 Nights)'),
        ],
        inclusions=[
            _inc_included('Premium Stays: 05 Nights luxury beachfront accommodation.', 1),
            _inc_included('Gourmet Dining: Daily breakfast and fine-dining dinners.', 2),
            _inc_included('Luxury Transport: Private AC Luxury SUV throughout.', 3),
            _inc_included('TRAGUIN Signature Experience: Private luxury yacht sunset cruise.', 4),
            _inc_included('Concierge Support: 24/7 dedicated TRAGUIN specialist support.', 5),
            _inc_excluded('Airfare, entry fees, and personal expenses.', 6),
        ],
    )
    return package, itinerary

def build_ap_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AP-009'
    tour_code = 'TG-AP-ADV-009'
    title = 'TRAGUIN Premium Eastern Ghats Adventure Trail'
    duration = '05 Nights / 06 Days'
    slug = 'ap-009-eastern-ghats-adventure-trail'
    itin_slug = 'ap-009-eastern-ghats-adventure-trail-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Andhra Pradesh / India | Category: Premium Adventure Trail', 2),
            _ph('Destinations: Visakhapatnam • Araku Valley • Lambasingi', 3),
            _ph('Ideal for: Adventure Enthusiasts, Active Families', 4),
            _ph('Best season: September to March', 5),
            _ph('Starting price: On Request (Premium Adventure Tier)', 6),
            _ph('Vehicle: High-Clearance 4x4 Luxury SUVs | Meal Plan: Premium MAPAI (Adventure-Fueled Menus)', 7),
            _ph('Route Plan: Vizag (1N) → Lambasingi (1N) → Araku Valley (3N) → Vizag Departure', 8),
            _ph('TRAGUIN Signature Experience: Private sunset canyon trek and expert-led mountain navigation.', 9),
        ],
        moods=['Adventure', 'Nature', 'Family', 'Trekking'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Adventure Tier)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Rugged Mountains • Pristine Canyons • Coastal Heights • 05 Nights / 06 Days',
        overview=(
            'Awaken your inner explorer. The Best Andhra Pradesh Adventure Tour Package, curated by TRAGUIN, invites you to conquer the dramatic Eastern Ghats.\n\nTOUR OVERVIEW\nThis adrenaline-focused Eastern Ghats Adventure Trail spans Visakhapatnam, Lambasingi, and Araku Valley with bespoke luxury transportation in high-ground-clearance vehicles and expert-led trekking routes.'
        ),
        seo_title='AP-009 | Premium Eastern Ghats Adventure Trail | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Eastern Ghats adventure package (AP-009 / TG-AP-ADV-009): Lambasingi, Borra Caves, canyon treks, Katiki Waterfalls, and 4-tier adventure stays.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Dolphin\'s Nose Lighthouse trek and coastal cliff exploration in Vizag', 1),
            _ih('Lambasingi fog-covered mountain woods trek and luxury tented bonfire camp', 2),
            _ih('Borra Caves rigorous descent and mountain eco-resort basecamp', 3),
            _ih('Chaprai Waterfalls canyon gorge trek and Galikonda high-peak summit climb', 4),
            _ih('Katiki Waterfalls multi-level forest trek and farewell bonfire at basecamp', 5),
        ],
        days=[
            _day(1, 'ARRIVAL & COASTAL EXPLORATION', ('Arrive in Visakhapatnam to a warm TRAGUIN welcome. Head out to the rugged coastal cliffs at Dolphin\'s Nose for a high-intensity trek up to the lighthouse point. Spend your evening by the beach preparing for the mountain climb ahead.'), [
                'Sightseeing Included: Dolphin\'s Nose Lighthouse trek, coastal cliff exploration.',
                'Evening Experience: Beachfront strategy briefing for the mountain trail.',
                'Meals Included: Welcome Lunch, Dinner.',
                'Overnight Stay: Premium Coastal Resort, Visakhapatnam.',
            ]),
            _day(2, 'TO THE FOGGY HEIGHTS OF LAMBASINGI', ('Drive into the mountains to Lambasingi, often called the Kashmir of Andhra. Your TRAGUIN guides lead an exploratory trek into the thick mountain woods. Experience a luxury-tented camp with an open bonfire under the clear mountain sky.'), [
                'Sightseeing Included: Mountain ghat drive, forest trekking, valley view exploration.',
                'Evening Experience: Bonfire camping in high-altitude forest surroundings.',
                'Meals Included: Breakfast, Lunch, Dinner.',
                'Overnight Stay: Luxury Tented Camp, Lambasingi.',
            ]),
            _day(3, 'CROSSING TO THE ARAKU VALLEY DEEP-WOODS', ('Trek through local tea and strawberry estates before descending into Araku Valley. Prepare for a rigorous descent into the Borra Caves before settling into your mountain basecamp.'), [
                'Sightseeing Included: Borra Caves exploration, mountain driving trail.',
                'Evening Experience: Relaxing in mountain eco-resort after a full day of trekking.',
                'Meals Included: Breakfast, Packed Adventure Lunch, Dinner.',
                'Overnight Stay: Luxury Mountain Eco-Resort, Araku.',
            ]),
            _day(4, 'THE CANYONS & HIGH PEAKS ADVENTURE', ('Expert-led canyon trek to Chaprai Waterfalls along the river gorge. In the afternoon, conquer the Galikonda View Point trek for breathtaking 360-degree mountain vistas.'), [
                'Sightseeing Included: Canyon gorge trek, Galikonda high-peak summit climb.',
                'Evening Experience: Tribal cultural interaction and adventure storytelling.',
                'Meals Included: Breakfast, Adventure Lunch, Dinner.',
                'Overnight Stay: Luxury Mountain Eco-Resort, Araku.',
            ]),
            _day(5, 'WATERFALL TRAILS & THE DESCENT', ('Focus on the Katiki Waterfalls multi-level climb through forest thickets. Post-hike, enjoy a high-protein tribal meal cooked by local experts. Begin your return journey to the lowlands.'), [
                'Sightseeing Included: Katiki waterfall trekking, forest navigation.',
                'Evening Experience: Farewell bonfire at your basecamp.',
                'Meals Included: Breakfast, Adventure Lunch, Dinner.',
                'Overnight Stay: Luxury Mountain Eco-Resort, Araku.',
            ]),
            _day(6, 'RETURN TO VIZAG & DEPARTURE', ('After a final breakfast overlooking the valley, descend back to the coast for your smooth final drive to the airport or station.'), [
                'Sightseeing Included: Mountain-to-coast descent transfer.',
                'Meals Included: Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Standard Resort / Forest Rest House', 'Visakhapatnam / Lambasingi / Araku Valley', '05 Nights', 'Deluxe', 'Standard Mountain View', 'Premium MAPAI', 4, 1, description='OPTION 01 – DELUXE: Standard Resort / Forest Rest House (Standard Mountain View)'),
            _hotel('Haritha Resorts / Boutique Mountain Stay', 'Visakhapatnam / Lambasingi / Araku Valley', '05 Nights', 'Premium', 'Premium Valley View', 'Premium MAPAI', 4, 2, description='OPTION 02 – PREMIUM: Haritha Resorts / Boutique Mountain Stay (Premium Valley View)'),
            _hotel('Private Mountain Eco-Lodges', 'Visakhapatnam / Lambasingi / Araku Valley', '05 Nights', 'Luxury', 'Luxury Cottage / Tented Suite', 'Premium MAPAI', 5, 3, description='OPTION 03 – LUXURY: Private Mountain Eco-Lodges (Luxury Cottage / Tented Suite)'),
            _hotel('Elite Forest Retreats / Adventure Resorts', 'Visakhapatnam / Lambasingi / Araku Valley', '05 Nights', 'Ultra Luxury', 'Private Adventure Villa', 'Premium MAPAI', 5, 4, description='OPTION 04 – ULTRA LUXURY: Elite Forest Retreats / Adventure Resorts (Private Adventure Villa)'),
        ],
        inclusions=[
            _inc_included('Premium Stays: 05 Nights luxury mountain and coastal accommodations.', 1),
            _inc_included('Adventure Dining: Daily breakfast, high-protein adventure lunches, and gourmet dinners.', 2),
            _inc_included('Luxury Transportation: Private 4x4 high-clearance SUV throughout the journey.', 3),
            _inc_included('Elite Adventure Team: Local expert trackers, mountain guides, and naturalist navigators.', 4),
            _inc_included('TRAGUIN Signature Experience: Private sunset canyon trek and expert-led mountain navigation.', 5),
            _inc_included('TRAGUIN Support: Dedicated concierge assistance, gear support, toll taxes, and driver allowance.', 6),
            _inc_excluded('Travel Tickets: Intercity flight or rail tickets.', 7),
            _inc_excluded('Entry Tickets: Forest permits, cave entry fees, and lighthouse tickets.', 8),
            _inc_excluded('Personal Items: Laundry, premium drinks, spa services, and tips.', 9),
            _inc_excluded('Insurance: Personal travel adventure insurance (Highly Recommended).', 10),
        ],
    )
    return package, itinerary

def build_ap_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'AP-010'
    tour_code = 'TG-AP-EXP-010'
    title = 'TRAGUIN Premium Andhra Explorer Package'
    duration = '06 Nights / 07 Days'
    slug = 'ap-010-andhra-explorer-vizag-araku-rajahmundry'
    itin_slug = 'ap-010-andhra-explorer-vizag-araku-rajahmundry-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Andhra Pradesh / India | Category: Premium Family Tour', 2),
            _ph('Destinations: Vizag • Araku • Rajahmundry', 3),
            _ph('From Coastal Wonders to Spiritual Rivers', 4),
            _ph('TOUR OVERVIEW: 06 Nights / 07 Days Andhra Pradesh Family Tour mixing adventure, culture, and coastal serenity.', 5),
            _ph('TRAGUIN Signature Experience: Private river cruise in Rajahmundry.', 6),
            _ph('Personalized Assistance: 24/7 dedicated travel support.', 7),
            _ph('Premium Handpicked Hotels: Stay in the best beach and hill properties.', 8),
        ],
        moods=['Family', 'Heritage', 'Coastal', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request',
        rating=Decimal("4.9"), review_count=0,
        tagline='From Coastal Wonders to Spiritual Rivers • Vizag • Araku • Rajahmundry • 06 Nights / 07 Days',
        overview=(
            'Discover the rich heritage and breathtaking landscapes of Andhra Pradesh with TRAGUIN. This 06 Nights / 07 Days Andhra Pradesh Family Tour is meticulously crafted for those seeking a mix of adventure, culture, and coastal serenity.\n\nWHY VISIT ANDHRA PRADESH?\nFrom the pristine beaches of Visakhapatnam to the lush coffee estates of Araku Valley and the serene backwaters of the Godavari river in Rajahmundry, this journey is a perfect luxury Andhra Pradesh holiday.'
        ),
        seo_title='AP-010 | Premium Andhra Explorer Package | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Andhra explorer package (AP-010 / TG-AP-EXP-010): Vizag, Araku Valley, Rajahmundry Godavari backwaters, and TRAGUIN curated experiences.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Vizag arrival with RK Beach evening walk and coastal bliss', 1),
            _ih('INS Kursura Submarine Museum, Kailasagiri Hill, and Bay of Bengal sunset', 2),
            _ih('Vistadome train through tunnels and ghats to Araku Tribal Museum and coffee plantations', 3),
            _ih('Borra Caves and Chaprai Waterfalls surrounded by nature', 4),
            _ih('TRAGUIN Signature Experience: Private river cruise on the Godavari with Papikondalu range views', 5),
        ],
        days=[
            _day(1, 'VISAKHAPATNAM - ARRIVAL & COASTAL BLISS', ('Arrive in Vizag, the City of Destiny. Experience a warm welcome by TRAGUIN and check into your beachfront resort. Evening walk at RK Beach.'), [
                'Overnight Stay: Vizag Luxury Beachfront Resort.',
                'Meals Included: Dinner.',
            ]),
            _day(2, 'VISAKHAPATNAM - HERITAGE & HARBOR', ('Visit the INS Kursura Submarine Museum and the serene Kailasagiri Hill. Enjoy a breathtaking sunset view over the Bay of Bengal.'), [
                'Sightseeing Included: INS Kursura Submarine Museum, Kailasagiri Hill.',
                'Overnight Stay: Vizag.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(3, 'VIZAG TO ARAKU - THE MOUNTAIN ESCAPE', ('Board the Vistadome train through tunnels and ghats. Explore the Araku Tribal Museum and enjoy exclusive experiences in the coffee plantations.'), [
                'Sightseeing Included: Vistadome train, Araku Tribal Museum, coffee plantations.',
                'Overnight Stay: Araku Luxury Eco-Resort.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(4, 'ARAKU VALLEY - CAVES & WATERFALLS', ('Marvel at the Borra Caves and the scenic Chaprai Waterfalls. Enjoy premium stays surrounded by nature.'), [
                'Sightseeing Included: Borra Caves, Chaprai Waterfalls.',
                'Overnight Stay: Araku.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(5, 'ARAKU TO RAJAHMUNDRY - RIVER SERENITY', ('Drive to Rajahmundry. Experience the spiritual vibe of the Godavari river. This is a must-visit Andhra Pradesh sightseeing spot.'), [
                'Sightseeing Included: Godavari river, Rajahmundry spiritual landmarks.',
                'Overnight Stay: Rajahmundry Riverside Resort.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(6, 'RAJAHMUNDRY - GODAVARI BACKWATERS', ('Enjoy a private boat ride on the Godavari river. Experience the scenic beauty of the Papikondalu range.'), [
                'Sightseeing Included: Private Godavari river boat ride, Papikondalu range views.',
                'Overnight Stay: Rajahmundry.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(7, 'DEPARTURE - UNFORGETTABLE MEMORIES', ('Transfer to the airport/station. Depart with unforgettable memories curated by TRAGUIN.'), [
                'Meals Included: Breakfast.',
            ]),
        ],
        hotels=[],
        inclusions=[
            _inc_included('TRAGUIN Signature Experience: Private river cruise in Rajahmundry.', 1),
            _inc_included('Personalized Assistance: 24/7 dedicated travel support.', 2),
            _inc_included('Premium Handpicked Hotels: Stay in the best beach and hill properties.', 3),
        ],
    )
    return package, itinerary

ANDHRA_PRADESH_DOMESTIC_BUILDERS = [
    build_ap_001,
    build_ap_002,
    build_ap_003,
    build_ap_004,
    build_ap_005,
    build_ap_006,
    build_ap_007,
    build_ap_008,
    build_ap_009,
    build_ap_010,
]
