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


def build_up_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UP-002'
    tour_code = 'TRG-UP-002'
    title = 'AYODHYA SPIRITUAL JOURNEY • ETERNAL DIVINE BLESSINGS'
    duration = '03 Nights / 04 Days'
    slug = 'up-002-ayodhya-spiritual-journey-eternal-divine-blessings'
    itin_slug = 'up-002-ayodhya-spiritual-journey-eternal-divine-blessings-itinerary'
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
            _ph('Serial code UP-002 | TRAGUIN tour code TRG-UP-002', 1),
            _ph('State / Country: Uttar Pradesh / India | Category: Premium Pilgrimage / Spiritual Journey', 2),
            _ph('Destinations: Ayodhya • Saryu', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Chauffeur-Driven Luxury MUV / MAPAI (Premium Vegetarian meals)', 7),
            _ph('TRAGUIN Signature Experience: Private riverside floral offering arrangement during your Saryu Aarti', 8),
            _ph('Curated by TRAGUIN Experts: Expertly planned timing to avoid heavy afternoon temple crowd lines for', 9),
            _ph('Premium Handpicked Hotels: Accommodations selected strictly based on premium safety standards,', 10),
            _ph('Luxury Transportation: Professional drivers ensuring smooth, safe highway transits.', 11)
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
        tagline='AYODHYA SPIRITUAL JOURNEY',
        overview='AYODHYA SPIRITUAL JOURNEY • ETERNAL DIVINE BLESSINGS Welcome to an extraordinary sacred odyssey curated exclusively by TRAGUIN. Embark on the most majestic Ayodhya Spiritual Journey, meticulously designed to unveil the breathtaking landscapes of deep- rooted Indian heritage, sacred continuous traditions, and royal architecture. As your elite travel consultants, TRAGUIN transforms this soul-stirring destination into an ultra-comfortable luxury proposal. Stay at premium stays, immerse your mind in soulful chanting, and witness iconic attractions with absolute seamlessness. Let the mystical charm of the Saryu River leave you with sweet, unforgettable memories.\n\nTOUR OVERVIEW\nThis custom-tailored divine holiday package offers an unmatched balance between sacred rituals and absolute comfort. Traveling in a premium, fully customized AC vehicle driven by a professional tourist chauffeur, your family will experience top-tier luxury and privacy at every stop. Enjoy a carefully handpicked meal plan featuring fine vegetarian delicacies from classic regional cuisines. Every aspect of this trip features a specialized TRAGUIN curated experience note, providing VIP entry access to sacred temple altars, premium seating during grand evening ceremonies, and 24/7 dedicated travel support.\n\nWHY VISIT AYODHYA? EXPERIENCE THE BEST AYODHYA TOUR\nPACKAGE When considering a Luxury Uttar Pradesh Holiday, spiritual seekers want a flawless mix of deep faith, royal comfort, and expert-guided storytelling. Ayodhya stands as the absolute pinnacle of Indian heritage, making an Ayodhya Honeymoon Package or an Ayodhya Family Tour a deeply meaningful choice for loved ones. From paying your respects at the newly unveiled, majestic Shri Ram Janmabhoomi Temple to exploring the historic Hanuman Garhi, Ayodhya sightseeing offers an enriching experience. This curated itinerary guides you to the most popular Instagram locations along Ram Ki Paidi, the golden palace rooms of Kanak Bhawan, and the vibrant local markets filled with classical brass souvenirs. Indulge in local street food suggestions like hot malpua and authentic rabri, or sit by the riverbank to take in the sheer scenic beauty during sunset. Our premium TRAGUIN Ayodhya Packages combine exclusive experiences with luxury handpicked hotels, ensuring you visit during the best time to visit Ayodhya with complete peace of mind.',
        seo_title='UP-002 | AYODHYA SPIRITUAL JOURNEY | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Uttar Pradesh package (UP-002 / TRG-UP-002): Ayodhya • Saryu with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN LUCKNOW / AYODHYA TRAVEL', 1),
            _ih('Day 02: DEEP DEVOTIONAL AYODHYA DARSHAN', 2),
            _ih('Day 03: HERITAGE TRAILS & MYSTICAL MONUMENTS', 3),
            _ih('Day 04: AYODHYA TO LUCKNOW / DEPARTURE', 4),
            _ih('TRAGUIN Signature Experience: Private riverside floral offering arrangement during your Saryu Aarti', 5),
            _ih('Curated by TRAGUIN Experts: Expertly planned timing to avoid heavy afternoon temple crowd lines for', 6),
            _ih('Premium Handpicked Hotels: Accommodations selected strictly based on premium safety standards,', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN LUCKNOW / AYODHYA TRAVEL',
                (
                    'Your premium Ayodhya experience begins as you arrive at Lucknow Airport or Ayodhya Cantt Station. A dedicated private luxury transport vehicle will greet you warmly and drive you down the smooth national highway. Upon arrival in Ayodhya, check into your handpicked luxury premium stay. After some refreshing downtime, enjoy your first local experience with a private sunset boat cruise along the holy Saryu River. Witness the spectacular grand evening Aarti ceremony from your reserved, exclusive seating.'
                ),
                [
                    'WELCOME NOTE: TO THE HOLY LAND – SACRED SARYU EVENING AARTI',
                    'Sightseeing Included: Saryu River Ghats, Ram Ki Paidi illuminated steps, Local traditional reception.',
                    'Evening Experience: Grand Saryu Aarti with a special floral offering ceremony curated by TRAGUIN experts.',
                    'Overnight Stay: Ayodhya (Premium Boutique Luxury Hotel)',
                    'Meals Included: Welcome Drink & Fine Vegetarian Dinner',
                ],
            ),
            _day(
                2,
                'DEEP DEVOTIONAL AYODHYA DARSHAN',
                (
                    'THE GRAND RAM JANMABHOOMI TEMPLE & THE GOLDEN PALACE Awake early to peaceful temple chimes and enjoy a healthy breakfast. Today features a profound spiritual highlight: a guided VIP tour of the magnificent Shri Ram Janmabhoomi Temple, a masterpiece of modern- classical stone architecture. Next, visit Hanuman Garhi, an ancient fort-style temple standing guard over the holy city. Continue on to Kanak Bhawan, a grand palace temple famous for its golden crowns and beautifully sculpted inner idols. Dashrath Mahal.'
                ),
                [
                    'Sightseeing Included: Ram Janmabhoomi Complex, Hanuman Garhi Fort Temple, Kanak Bhawan Palace,',
                    'Optional Activities: An intimate meeting and blessing ceremony with a senior respected local Vedic scholar.',
                    'Overnight Stay: Ayodhya (Premium Boutique Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Traditional Sattvik Dinner',
                ],
            ),
            _day(
                3,
                'HERITAGE TRAILS & MYSTICAL MONUMENTS',
                (
                    'MANI PARVAT VISTAS, SURYAKUND & IMMERSIVE FOLK LEGENDS Following a leisurely breakfast, explore the historic landscape of Mani Parvat to take in panoramic views of the city. Drive onward to the beautifully restored Surya Kund, an ancient reservoir surrounded by scenic carved stone arches. Spend your afternoon exploring local heritage markets to browse spiritual souvenirs, hand- carved wooden idols, and authentic classical embroidery. In the evening, unwind at an elegant cultural performance venue.'
                ),
                [
                    'Sightseeing Included: Mani Parvat, Surya Kund water body, Tulsi Smarak Bhawan museum.',
                    'Evening Experience: A private traditional bhajan and classic musical performance over high-tea.',
                    'Overnight Stay: Ayodhya (Premium Boutique Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Royal Awadhi Vegetarian Feast',
                ],
            ),
            _day(
                4,
                'AYODHYA TO LUCKNOW / DEPARTURE',
                (
                    'CHERISHING ETERNAL DIVINE MEMORIES BEYOND DESTINATIONS Enjoy a final morning breakfast at your premium hotel before packing your bags. Your private luxury vehicle will escort you safely along the smooth expressway back to Lucknow Airport or Ayodhya Cantt Station for your onward journey. Return home filled with divine peace, renewed spirit, and sweet, unforgettable memories designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door transit drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Ramayana / Park Inn by | Radisson / similar | Dinner)',
                'Multi-city Uttar Pradesh',
                '3N',
                'Deluxe',
                'Deluxe Executive Room',
                'MAPAI (Breakfast &',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Ramayana / Park Inn by | Radisson / similar | Dinner)',
            ),
            _hotel(
                'The Cygnus Palace / Hotel | Ramprastha / similar | Dinner)',
                'Multi-city Uttar Pradesh',
                '3N',
                'Premium',
                'Premium Balcony Room',
                'MAPAI (Breakfast &',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Cygnus Palace / Hotel | Ramprastha / similar | Dinner)',
            ),
            _hotel(
                'Haveli Resort',
                'Uttar Pradesh',
                '3N',
                'Luxury',
                'Luxury Heritage Suite',
                'MAPAI Kit',
                4,
                3,
                description='OPTION 03 – LUXURY: Haveli Resort',
            ),
            _hotel(
                'Ultra-luxury Private Devotional | VVIP Royal Panoramic',
                'Multi-city Uttar Pradesh',
                '3N',
                'Ultra Luxury',
                'Presidential Suite',
                'Signature Dining',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Ultra-luxury Private Devotional | VVIP Royal Panoramic',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 03 Nights in handpicked sacred luxury properties.', 1),
            _inc_included('Luxury Transportation: Private dedicated MUV vehicle for all transfers.', 2),
            _inc_included('Curated Meal Plan: Daily premium buffet breakfast and pure vegetarian dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 personalized guest assistance line.', 4),
            _inc_included('Welcome Amenities: Customized devotional travel kit and traditional stole.', 5),
            _inc_included('Complimentary Experience: Private sunset boat ride ticket at Saryu River.', 6),
            _inc_excluded('Airfare, flight tickets, or long-distance train travel.', 7),
            _inc_excluded('Special ritual dakshina, personal offerings, or pandit fees.', 8),
            _inc_excluded('Camera permits, monument entry tickets, professional guide fees.', 9),
            _inc_excluded('Personal expenses such as laundry, phone calls, or tips.', 10),
        ],
    )
    return package, itinerary

def build_up_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UP-003'
    tour_code = 'TRG-UP-003'
    title = 'PRAYAGRAJ SANGAM TOUR • SPIRITUAL AWAKENING & SACRED LEGACIES'
    duration = '03 Nights / 04 Days'
    slug = 'up-003-prayagraj-sangam-tour-spiritual-awakening-sacred-legacies'
    itin_slug = 'up-003-prayagraj-sangam-tour-spiritual-awakening-sacred-legacies-itinerary'
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
            _ph('Serial code UP-003 | TRAGUIN tour code TRG-UP-003', 1),
            _ph('State / Country: Uttar Pradesh / India | Category: Premium Pilgrimage', 2),
            _ph('Destinations: Prayagraj', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Elite, pre-arranged Vedic puja with private senior pandit support directly', 8),
            _ph('Curated by TRAGUIN Experts: Smart pacing designed to minimize temple waiting lines and maximize', 9),
            _ph('Premium Handpicked Hotels: Properties selected meticulously for exceptional family safety, cleanliness,', 10),
            _ph('Luxury Transportation: Expertly trained, deeply polite local chauffeurs who excel in route optimization', 11)
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
        tagline='PRAYAGRAJ SANGAM TOUR',
        overview='PRAYAGRAJ SANGAM TOUR • SPIRITUAL AWAKENING & SACRED LEGACIES Welcome to a timeless spiritual journey thoughtfully crafted by TRAGUIN. Embark on the finest Uttar Pradesh Pilgrimage, curated to plunge you into the profound energy, sacred waters, and epic histories of North India. As your elite travel consultants, TRAGUIN translates ancient traditions into a flawless luxury holiday featuring premium stays, VIP access keys, and deeply moving local lore. Experience the majestic confluence at the Triveni Sangam and step along the hallowed paths of ancient kings and deities, making unforgettable memories of serenity and soul-stirring inner peace.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package presents an unmatched fusion of spiritual devotion, historical grandeur, and contemporary opulence. Travelling across the sacred landscapes of Uttar Pradesh in a private chauffeur-driven luxury vehicle, your family will discover complete relaxation and elite privacy. Featuring an expansive meal plan with multi-cuisine morning spreads and fine-dining gourmet dinners, every mile represents the pinnacle of a premium Uttar Pradesh experience. This curated itinerary integrates exclusive experiences—including private chartered boat rides, expert pandit services, and fast-track VIP temple entry lines—ensuring the hallmark of TRAGUIN curated experiences remains true throughout your pilgrimage.\n\nWHY BOOK THE BEST UTTAR PRADESH TOUR PACKAGE?\nWhen seeking an authentic yet ultra-comfortable journey, spiritual travelers choose a Luxury Uttar Pradesh Holiday that transcends standard arrangements. The historic city of Prayagraj hosts the most iconic attractions in spiritual India. From the legendary Triveni Sangam—the mystical meeting point of the holy Ganga, Yamuna, and invisible Saraswati rivers—to the majestic stone ramparts of the Prayagraj Fort, the sightseeing depth is extraordinary. For families planning a definitive Uttar Pradesh Family Tour or couples seeking a soul-cleansing Uttar Pradesh Honeymoon Package, this region unveils top tourist places in Uttar Pradesh such as the Anand Bhavan (ancestral home of the Nehru family), the massive Hanuman Temple where the deity is in a unique reclining posture, and the grand ashrams of legendary sages. Whether capturing stunning landscape frames at sunset or indulging in premium handpicked hotels, our TRAGUIN Uttar Pradesh Packages balance cultural depth with luxurious pampering, mapping perfectly to the best time to visit Uttar Pradesh.',
        seo_title='UP-003 | PRAYAGRAJ SANGAM TOUR | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Uttar Pradesh package (UP-003 / TRG-UP-003): Prayagraj with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN PRAYAGRAJ (ALLAHABAD)', 1),
            _ih('Day 02: TRIVENI SANGAM IMMERSIVE EXPERIENCE', 2),
            _ih('Day 03: EXCURSION TO AYODHYA (THE RAM JANMABHOOMI)', 3),
            _ih('Day 04: PRAYAGRAJ FAREWELL & DEPARTURE', 4),
            _ih('TRAGUIN Signature Experience: Elite, pre-arranged Vedic puja with private senior pandit support directly', 5),
            _ih('Curated by TRAGUIN Experts: Smart pacing designed to minimize temple waiting lines and maximize', 6),
            _ih('Premium Handpicked Hotels: Properties selected meticulously for exceptional family safety, cleanliness,', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN PRAYAGRAJ (ALLAHABAD)',
                (
                    "WELCOME TO THE CITY OF FAITH – SOULFUL ARRIVAL & SIGHTSEEING Your premium Uttar Pradesh experience commences as you step off your flight or train. Your private luxury transport chauffeur will welcome you and escort you to your handpicked premium hotel. After settling into your spacious luxury suite, step out to explore the architectural landmarks of Prayagraj. Visit the majestic Anand Bhavan, a beautifully preserved monument to India's freedom struggle, and the beautifully serene All Saints Cathedral. In the evening, explore local heritage streets before enjoying an elegant dinner. Park."
                ),
                [
                    'Sightseeing Included: Anand Bhavan Museum, Swaraj Bhavan, All Saints Cathedral, Chandra Shekhar Azad',
                    'Evening Experience: Exclusive orientation walk and a fine-dining experience arranged by TRAGUIN experts.',
                    'Overnight Stay: Prayagraj (Premium / Luxury Selected Hotel)',
                    'Meals Included: Welcome Refreshment & Luxury Buffet Dinner',
                ],
            ),
            _day(
                2,
                'TRIVENI SANGAM IMMERSIVE EXPERIENCE',
                (
                    'HOLY DIP, PRIVATE CHARTERED BOAT & SACRED TEMPLES Awake to a mystical dawn and embark towards the breathtaking landscapes of the Triveni Sangam, the crown jewel of Prayagraj sightseeing. Board an exclusive private chartered boat booked specifically for your family to cruise to the precise mid-river point where the distinct colors of the Ganges and Yamuna merge. Experience an emotionally moving, privately conducted Vedic puja ceremony by a senior priest. After a holy dip, return to the banks to visit the historic reclining Let Hanuman Temple and walk through the sprawling, ancient underground Patalpuri Temple inside the historic Prayagraj Fort walls. Temple, Akshaya Vat tree.'
                ),
                [
                    'Sightseeing Included: Triveni Sangam Confluence, Reclining Hanuman Temple, Prayagraj Fort exterior, Patalpuri',
                    'Optional Activities: A professional sunset photography session along the expansive river banks and ghats.',
                    'Overnight Stay: Prayagraj (Premium / Luxury Selected Hotel)',
                    'Meals Included: Premium Breakfast & Specialized Traditional Dinner',
                ],
            ),
            _day(
                3,
                'EXCURSION TO AYODHYA (THE RAM JANMABHOOMI)',
                (
                    'EPIC HERITAGE & SPIRITUAL SPLENDOR SPLENDOR Following a hearty morning breakfast, set off on a premium day excursion to the ancient town of Ayodhya via a smooth, scenic route. Witness the unparalleled grandeur of the newly built Shri Ram Janmabhoomi Temple. Benefit from fast-track arrangements to marvel at the pristine idols. Next, explore the grand, fortress-like Hanuman Garhi Temple and walk along the beautiful riverfront steps of Sarayu Ghat, a highly popular Instagram location. Soak in the emotional chanting before driving back to your luxury base in Prayagraj.'
                ),
                [
                    'Sightseeing Included: Shri Ram Janmabhoomi Temple, Hanuman Garhi, Kanak Bhawan, Sarayu River Ghats.',
                    'Evening Experience: Sarayu River Aarti viewing with private designated seating parameters.',
                    'Overnight Stay: Prayagraj (Premium / Luxury Selected Hotel)',
                    'Meals Included: Lavish Breakfast & Festive Grand Dinner',
                ],
            ),
            _day(
                4,
                'PRAYAGRAJ FAREWELL & DEPARTURE',
                (
                    'CARRYING SACRED BLESSINGS & UNFORGETTABLE MEMORIES Indulge in a final gourmet breakfast at your premium property. Take a relaxed morning stroll to collect authentic local souvenirs and temple prasad. At the designated hour, your chauffeur will transfer your family seamlessly back to Prayagraj Airport or Railway Station. Your journey concludes, leaving you with divine blessings and unforgettable memories crafted meticulously by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door departure drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Milan Palace / Cennet The | Grand / similar | Dinner)',
                'Multi-city Uttar Pradesh',
                '3N',
                'Deluxe',
                'Room',
                'MAPAI (Breakfast &',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Milan Palace / Cennet The | Grand / similar | Dinner)',
            ),
            _hotel(
                'The Legend Hotel / Hotel Kanha | Shyam / similar | Dinner)',
                'Multi-city Uttar Pradesh',
                '3N',
                'Premium',
                'Premium Club Room',
                'MAPAI (Breakfast &',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Legend Hotel / Hotel Kanha | Shyam / similar | Dinner)',
            ),
            _hotel(
                'WelcomHeritage Traditional | Welcome Amenity',
                'Multi-city Uttar Pradesh',
                '3N',
                'Luxury',
                'Heritage Luxury Suite',
                'MAPAI + Premium',
                4,
                3,
                description='OPTION 03 – LUXURY: WelcomHeritage Traditional | Welcome Amenity',
            ),
            _hotel(
                'Elite Private VVIP Glamping Tents | (Mela Season Only) | Ultra-Luxury Royal | Dining Plan',
                'Multi-city Uttar Pradesh',
                '3N',
                'Ultra Luxury',
                'Maharaja Suite Tent',
                'Bespoke Personalized',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Elite Private VVIP Glamping Tents | (Mela Season Only) | Ultra-Luxury Royal | Dining Plan',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 3 Nights accommodation in highly rated, handpicked hotels.', 1),
            _inc_included('Luxury Transportation: Private air- conditioned luxury SUV for entire route.', 2),
            _inc_included('Curated Meals: Daily elaborate breakfast spreads and gourmet dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest relations assistance and care.', 4),
            _inc_included('Exclusive Experiences: Private chartered boat ride to the middle of Triveni Sangam.', 5),
            _inc_included('Welcome Amenities: Specialized spiritual travel kit, holy thread, and sweets.', 6),
            _inc_excluded('Airfare, flight tickets, or cross-state interstate train tickets.', 7),
            _inc_excluded('Personal temple donations, special dakshina for rituals.', 8),
            _inc_excluded('Camera permits, local guide service tips, or laundry costs.', 9),
            _inc_excluded('Any insurance coverages or optional localized activities.', 10),
        ],
    )
    return package, itinerary

def build_up_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UP-004'
    tour_code = 'TRG-UP-004VEHICLE'
    title = 'AGRA • MATHURA • VRINDAVAN'
    duration = '04 Nights / 05 Days'
    slug = 'up-004-agra-mathura-vrindavan'
    itin_slug = 'up-004-agra-mathura-vrindavan-itinerary'
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
            _ph('Serial code UP-004 | TRAGUIN tour code TRG-UP-004VEHICLE', 1),
            _ph('State / Country: Uttar Pradesh / India | Category: Premium Family Tour', 2),
            _ph('Destinations: Agra •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / MAPAI (Breakfast & Dinner Included)', 7),
            _ph('TRAGUIN Signature Experience: Private family historical briefing before visiting the Taj Mahal.', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked travel routes that avoid peak highway traffic, keeping your', 9),
            _ph('Personalized Assistance: Dedicated destination managers monitoring your entry slots and temple queue', 10),
            _ph('Premium Handpicked Hotels: Elite properties selected for their exceptional comfort, safety, and excellent', 11)
        ],
        moods=['Family', 'Luxury'],
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
        tagline='AGRA',
        overview="AGRA • MATHURA • VRINDAVAN | 04 NIGHTS / 05 DAYS Welcome Note: Experience a breathtaking synthesis of timeless romance, Mughal opulence, and divine spiritual awakening with the Best Uttar Pradesh Tour Package curated specifically for your family. TRAGUIN invites you on an immersive luxury holiday designed to forge unforgettable memories across India's heartland. From the pristine white marble contours of the Taj Mahal in Agra to the sacred, rhythmic temple bells echoing across the holy lands of Mathura and Vrindavan, every detail is engineered to perfection. Trust TRAGUIN to provide an unrivaled premium Uttar Pradesh experience where history blends seamlessly with comfort.\n\nTOUR OVERVIEW\nThis elite itinerary serves as a customized private family getaway (FIT) meticulously crafted by our expert travel consultants. Travelling in a dedicated luxury air-conditioned vehicle with a professional chauffeur, your family will enjoy absolute safety and seamless connectivity. Your curated travel route covers the majestic architectural legacy of Agra before heading deep into the spiritual capital of Braj Bhoomi. With a premium meal plan combining daily lavish breakfasts and specialized multi-cuisine dinners, this journey is further elevated by exclusive privileges. Every single element reflects a signature TRAGUIN curated experience note, offering handpicked hotels and personalized attention from departure to arrival. DISCOVER THE MAGIC OF BRAJ BHOOMI & MUGHAL MAJESTY Choosing a Luxury Uttar Pradesh Holiday means immersing your family in some of the most culturally rich and historical landscapes on Earth. The state features iconic attractions known worldwide, including the magnificent Taj Mahal and the royal red stone citadel of Agra Fort—unmatched jewels of Agra Sightseeing. This comprehensive itinerary acts as the ultimate Uttar Pradesh Family Tour, connecting architectural marvels with deep, soul-stirring heritage. For travelers seeking a meaningful journey, the sacred twins of Mathura Sightseeing and Vrindavan spiritual circuits offer most searched experiences. Discover highly popular Instagram locations like the beautifully lit Prem Mandir, the historic Banke Bihari Temple, and the serene banks of the Yamuna River during a traditional evening cruise. Whether you are seeking a romantic escape covered in an architectural Uttar Pradesh Honeymoon Package or an enriching multigenerational vacation, our elite TRAGUIN Uttar Pradesh Packages guarantee premium stays, expert storytelling, and the absolute best time to visit Uttar Pradesh.",
        seo_title='UP-004 | AGRA | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Uttar Pradesh package (UP-004 / TRG-UP-004VEHICLE): Agra • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN AGRA', 1),
            _ih('Day 02: THE TAJ MAHAL & FATEHPUR SIKRI', 2),
            _ih('Day 03: AGRA TO MATHURA', 3),
            _ih('Day 04: VRINDAVAN SPIRITUAL EXCURSION', 4),
            _ih('Day 05: MATHURA TO DELHI / DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private family historical briefing before visiting the Taj Mahal.', 6),
            _ih('Curated by TRAGUIN Experts: Handpicked travel routes that avoid peak highway traffic, keeping your', 7),
            _ih('Personalized Assistance: Dedicated destination managers monitoring your entry slots and temple queue', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN AGRA',
                (
                    'WELCOME TO THE LAND OF INFINITE ROMANCE & MUGHAL SPLENDOR Your luxury itinerary begins as our professional chauffeur meets your family at New Delhi Airport or Railway Station. Step into your private luxury transportation vehicle and embark on a smooth, scenic route via the Yamuna Expressway to the historic city of Agra. Upon arrival, check into your premium handpicked hotel and refresh. In the afternoon, your expert guide leads you to the majestic Agra Fort, an iconic red sandstone fortress containing exquisite palaces and royal apartments. As evening approaches, catch a spectacular view of the Taj Mahal across the river from the lush lawns of Mehtab Bagh, a perfect photography point to capture unforgettable memories. dinner.'
                ),
                [
                    'Sightseeing Included: Agra Fort, Mehtab Bagh Gardens, Local Marble Inlay Artisan Studios.',
                    'Evening Experience: A stunning sunset viewing of the Taj Mahal silhouette across the river, followed by gourmet',
                    'Overnight Stay: Agra (Premium / Luxury Selected Hotel)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'THE TAJ MAHAL & FATEHPUR SIKRI',
                (
                    "DAWN SPECTACULAR AT THE WORLD'S GREATEST WONDER Awake early for a breathtaking, emotionally moving experience: viewing the Taj Mahal at sunrise. Watch the white marble softly shift colors as the first light hits this monument to eternal love. Return to your hotel for a lavish buffet breakfast. In the afternoon, enjoy an excursion to the UNESCO World Heritage site of Fatehpur Sikri. Explore the magnificent Buland Darwaza, the grand Jama Masjid, and the elegant white marble tomb of Salim Chishti. Spend your evening exploring Agra's bustling markets for artisan keepsakes."
                ),
                [
                    'Sightseeing Included: Taj Mahal (Sunrise Tour), Fatehpur Sikri complex, Panch Mahal.',
                    'Optional Activities: Attend the live theater mega-show "Mohabbat-the-Taj" mapping the historical love story.',
                    'Overnight Stay: Agra (Premium / Luxury Selected Hotel)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'AGRA TO MATHURA',
                (
                    'JOURNEY TO THE BIRTHPLACE OF LORD KRISHNA Following a deluxe breakfast, take a short, comfortable drive to the ancient, sacred city of Mathura—the birthplace of Lord Krishna. Check into your premium stay and begin an immersive cultural tour of the Shri Krishna Janmabhoomi Temple Complex. Walk through ancient corridors filled with spiritual energy and historical depth. Later, visit the holy Vishram Ghat on the banks of the Yamuna River. In the evening, witness a spectacular evening Aarti as hundreds of clay lamps illuminate the water.'
                ),
                [
                    'Sightseeing Included: Krishna Janmabhoomi Temple, Dwarkadhish Temple, Vishram Ghat.',
                    'Evening Experience: A private traditional boat ride during the floating lamp Aarti ceremony at Vishram Ghat.',
                    'Overnight Stay: Mathura (Handpicked Premium Boutique Hotel)',
                    'Meals Included: Breakfast & Authentic Satvik Dinner',
                ],
            ),
            _day(
                4,
                'VRINDAVAN SPIRITUAL EXCURSION',
                (
                    'MYSTICAL TEMPLES & REVERED BRAJ DEVOTION Dedicate your entire day to exploring Vrindavan, a holy town alive with divine love and folklore. Visit the historic Banke Bihari Temple to experience its unique, joyful devotional chants. Explore the grand ISKCON Temple before discovering the architectural brilliance of Prem Mandir. In the evening, the temple walls come alive with an incredible synchronized musical fountain and light show, making it a highly popular Instagram location for capturing beautiful family moments.'
                ),
                [
                    'Sightseeing Included: Banke Bihari Temple, Prem Mandir, ISKCON Temple, Radha Raman Temple.',
                    'Optional Activities: A guided tour through the sacred tulsi groves of Nidhivan.',
                    'Overnight Stay: Mathura / Vrindavan Premium Resort',
                    'Meals Included: Breakfast & Special Farewell Feast Dinner',
                ],
            ),
            _day(
                5,
                'MATHURA TO DELHI / DEPARTURE',
                (
                    'CHERISHING FAITH, LEGEND & UNFORGETTABLE ENCOUNTERS Enjoy a final luxury breakfast at your resort before packing your bags. Your dedicated luxury transportation chauffeur will drive you comfortably back to New Delhi, stopping along the way to pick up famous sweet delicacies from the region. Arrive at New Delhi Airport or Railway Station for your onward journey. Return home carrying deep spiritual peace, beautiful family bonds, and unforgettable memories designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private door-to-door highway drop-off to Delhi airport/station.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Howard Plaza The Fern / Crystal Sarovar | Hotel Best Western / Wingston Resort',
                'Multi-city Uttar Pradesh',
                '4N',
                'Deluxe',
                'Superior Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Howard Plaza The Fern / Crystal Sarovar | Hotel Best Western / Wingston Resort',
            ),
            _hotel(
                'Radisson Hotel Agra / Courtyard by Marriott | Nidhivan Sarovar Portico / similar',
                'Multi-city Uttar Pradesh',
                '4N',
                'Premium',
                'Room Category',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Hotel Agra / Courtyard by Marriott | Nidhivan Sarovar Portico / similar',
            ),
            _hotel(
                'Taj Hotel & Convention | Centre / Trident Agra | The Barkana Boutique Hotel | / Luxury Resort',
                'Multi-city Uttar Pradesh',
                '4N',
                'Luxury',
                'Suite',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: Taj Hotel & Convention | Centre / Trident Agra | The Barkana Boutique Hotel | / Luxury Resort',
            ),
            _hotel(
                'The Oberoi Amarvilas (Taj | Estate villa | Royal Heritage',
                'Multi-city Uttar Pradesh',
                '4N',
                'Ultra Luxury',
                'Presidential Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Oberoi Amarvilas (Taj | Estate villa | Royal Heritage',
            )
        ],
        inclusions=[
            _inc_included("Accommodation: 04 Nights' stay in handpicked, top-rated hotels.", 1),
            _inc_included('Sightseeing: Complete guided tours as per detailed day-wise itinerary.', 2),
            _inc_included('Meals: 4 Premium breakfasts and 4 gourmet dinners included.', 3),
            _inc_included('Assistance: Personalized airport/station pick- up and drop-off.', 4),
            _inc_included('Transfers: Private luxury air-conditioned SUV at your disposal.', 5),
            _inc_included('Taxes & Support: All state toll taxes, parking fees, and 24/7 TRAGUIN support.', 6),
            _inc_included('Welcome Amenities: Custom luxury family welcome kit and fresh packaged water.', 7),
            _inc_included('Complimentary Experiences: Private sunset boat ride ticket at Yamuna River.', 8),
            _inc_excluded('Domestic or International Flights / Train tickets to New Delhi.', 9),
            _inc_excluded('Personal expenses such as laundry, phone calls, premium spirits, and tips.', 10),
            _inc_excluded('Monument entry tickets, professional local guide charges, and camera fees.', 11),
            _inc_excluded('Optional tours, theatre show tickets, or any meals not explicitly mentioned.', 12),
        ],
    )
    return package, itinerary

def build_up_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UP-005'
    tour_code = 'TRG-UP-005'
    title = 'GOLDEN TRIANGLE CLASSIC • HERITAGE, ROYALTY & DIVINE ROMANCE'
    duration = '05 Nights / 06 Days'
    slug = 'up-005-golden-triangle-classic-heritage-royalty-divine-romance'
    itin_slug = 'up-005-golden-triangle-classic-heritage-royalty-divine-romance-itinerary'
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
            _ph('Serial code UP-005 | TRAGUIN tour code TRG-UP-005', 1),
            _ph('State / Country: Uttar Pradesh / India | Category: Premium Family Tour', 2),
            _ph('Destinations: Agra • Fatehpur', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Innova Crysta / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private family interaction and historical storytelling briefing before', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked routing to avoid highway traffic, maximizing your leisure and', 9),
            _ph('Exclusive Recommendations: VIP access parameters to select evening ceremonies and fine-dining', 10)
        ],
        moods=['Family', 'Luxury', 'Culture'],
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
        tagline='GOLDEN TRIANGLE CLASSIC',
        overview='GOLDEN TRIANGLE CLASSIC • HERITAGE, ROYALTY & DIVINE ROMANCE Welcome to a timeless royal expedition curated exclusively by TRAGUIN. Embark on the definitive Uttar Pradesh Family Tour designed to reveal the magnificent monuments, sacred narratives, and iconic attractions of legendary empires. As your trusted premium travel consultants, TRAGUIN transforms your vacation into an unforgettable luxury holiday featuring handpicked hotels, private premium stays, and deeply emotional cultural encounters. From the peerless white marble marvel of the Taj Mahal in Agra to the spiritual sanctuaries of Mathura and Vrindavan, every detail is seamlessly aligned to create beautiful, unforgettable memories.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers an exquisite balance between legendary Mughal grandeur and deeply spiritual Braj heritage. Travelling in a dedicated private premium AC vehicle with professional chauffeur-driven assistance, your family will experience absolute relaxation, privacy, and convenience. Featuring a premium curated meal plan with lavish daily breakfasts and specialized multi-course dinners, this route represents the definitive premium Uttar Pradesh experience. Every section of this journey contains the signature TRAGUIN curated experience note, ensuring skip-the-line VIP entries, private local guides, and around-the-clock bespoke support.\n\nWHY CHOOSE THE BEST UTTAR PRADESH TOUR PACKAGE?\nWhen searching for a Luxury Uttar Pradesh Holiday, premium travelers look for deep cultural storytelling blended with elite modern comfort. Uttar Pradesh contains some of the most highly celebrated tourist locations globally. From the internationally acclaimed Taj Mahal and grand Agra Fort—top tourist places in Uttar Pradesh for architectural majesty—to the timeless river banks of Yamuna in Mathura, this itinerary offers unmatched depth. For families and couples booking a private Uttar Pradesh Family Tour or a romantic Uttar Pradesh Honeymoon Package, this region reveals iconic, popular Instagram locations such as the reflection pools of Mehtab Bagh, the ghost city of Fatehpur Sikri, and the intricately carved Prem Mandir. Whether you are seeking rich local leather and textile shopping, sampling iconic Awadhi or sweet Petha delicacies, or standing in awe where emperors stood, our specialized TRAGUIN Uttar Pradesh Packages guarantee premium',
        seo_title='UP-005 | GOLDEN TRIANGLE CLASSIC | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Uttar Pradesh package (UP-005 / TRG-UP-005): Agra • Fatehpur with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN AGRA', 1),
            _ih('Day 02: AGRA IMPERIAL SIGHTSEEING', 2),
            _ih('Day 03: EXCURSION TO FATEHPUR SIKRI', 3),
            _ih('Day 04: AGRA TO MATHURA', 4),
            _ih('Day 05: VRINDAVAN SPIRITUAL SIGHTSEEING', 5),
            _ih('Day 06: MATHURA / VRINDAVAN TO NEW DELHI / DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private family interaction and historical storytelling briefing before', 7),
            _ih('Curated by TRAGUIN Experts: Handpicked routing to avoid highway traffic, maximizing your leisure and', 8),
            _ih('Exclusive Recommendations: VIP access parameters to select evening ceremonies and fine-dining', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN AGRA',
                (
                    'WELCOME TO THE MUGHAL CAPITAL – EMBARK ON THE LEGACY OF ROMANCE Your premium Uttar Pradesh experience begins as you arrive at New Delhi Airport/Railway Station, where your dedicated private luxury vehicle stands ready to welcome you. Enjoy a smooth drive via the Yamuna Expressway to Agra, the legendary center of the Mughal Empire. Check into your handpicked luxury resort, where custom welcome amenities await you. In the evening, visit Mehtab Bagh for an exclusive sunset view of the Taj Mahal from across the river, providing breathtaking landscapes and magnificent photography points. experts.'
                ),
                [
                    'Sightseeing Included: Yamuna Expressway scenic drive, Mehtab Bagh Taj Sunset View.',
                    'Evening Experience: Bespoke luxury dining experience featuring authentic Mughlai cuisine curated by TRAGUIN',
                    'Overnight Stay: Agra (Premium / Luxury Resort overlooking the Taj vista)',
                    'Meals Included: Welcome Drink & Gourmet Dinner',
                ],
            ),
            _day(
                2,
                'AGRA IMPERIAL SIGHTSEEING',
                (
                    "THE EPITOME OF ETERNAL LOVE & ARCHITECTURAL MAJESTY Awake before dawn for a truly immersive experience: the sunrise tour of the world-famous Taj Mahal. Witness the pure white marble change colors from soft pink to brilliant gold as the sun climbs, creating unforgettable memories for your family. Return to your premium hotel for a lavish buffet breakfast. In the afternoon, discover the formidable Agra Fort, a massive red-sandstone citadel containing exquisite palaces like the Khas Mahal and Jahangir Palace, followed by an evening exploring Agra's vibrant artisan markets."
                ),
                [
                    'Sightseeing Included: Taj Mahal (Sunrise Tour), Agra Fort, Tomb of Itmad-ud-Daulah (Baby Taj).',
                    'Optional Activities: A private marble inlay handicraft workshop with master descendants of original artisans.',
                    'Overnight Stay: Agra (Premium Luxury Resort)',
                    'Meals Included: Premium Breakfast & Fine-Dining Dinner',
                ],
            ),
            _day(
                3,
                'EXCURSION TO FATEHPUR SIKRI',
                (
                    "THE GHOST CITY – ARCHITECTURAL MARVELS OF AKBAR THE GREAT Following a rich morning breakfast, embark on a short scenic drive to Fatehpur Sikri, the perfectly preserved, UNESCO-listed ghost capital built by Emperor Akbar. Walk through the imposing Buland Darwaza, the highest gateway in the world, and listen to emotional storytelling about the mystical saint Salim Chishti. Admire the stunning blend of Hindu and Islamic artistic architecture within Panch Mahal and Jodha Bai's Palace before returning to Agra for a relaxed evening."
                ),
                [
                    'Sightseeing Included: Buland Darwaza, Jama Masjid, Salim Chishti Dargah, Panch Mahal, Diwan-i-Khas.',
                    'Evening Experience: Exclusive high-tea experience at a luxury terrace cafe offering beautiful views.',
                    'Overnight Stay: Agra (Premium Luxury Resort)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                4,
                'AGRA TO MATHURA',
                (
                    'JOURNEY TO THE BRAJ BHOOMI – UNVEILING THE SACRED CRADLE Bid farewell to imperial Agra and drive to Mathura, the sacred birthplace of Lord Krishna. This region forms the core of our premium Uttar Pradesh experience for families seeking cultural heritage. Explore the historic Krishna Janmabhoomi Temple Complex, feeling the deep spiritual energy that fills the air. Later, walk through the ancient ghats of the Yamuna River, experiencing the peaceful rhythms of local culture and ritual temple music.'
                ),
                [
                    'Sightseeing Included: Shri Krishna Janmabhoomi Temple, Dwarkadhish Temple, Vishram Ghat.',
                    'Evening Experience: Private Yamuna River boat ride during the magical evening Maha Aarti ceremony.',
                    'Overnight Stay: Mathura / Vrindavan (Handpicked Premium Boutique Hotel)',
                    'Meals Included: Premium Breakfast & Traditional Sattvik Vegetarian Dinner',
                ],
            ),
            _day(
                5,
                'VRINDAVAN SPIRITUAL SIGHTSEEING',
                (
                    'DIVINE MYSTICISM & ILLUMINATED MARBLE SANCTUARIES Spend a magnificent day exploring Vrindavan, a sacred town filled with thousands of historic and modern temples. Visit the historic Banke Bihari Temple to experience traditional devotion, followed by the serene paths of Nidhivan. In the evening, visit the magnificent Prem Mandir, a highly popular Instagram location sculpted entirely from fine white marble. Watch its stunning multimedia light show illuminate the intricate carvings of divine legends.'
                ),
                [
                    'Sightseeing Included: Banke Bihari Temple, Prem Mandir, ISKCON Temple, Nidhivan Forest.',
                    'Optional Activities: A guided heritage walk through the ancient, narrow streets of old Vrindavan.',
                    'Overnight Stay: Mathura / Vrindavan (Handpicked Premium Boutique Hotel)',
                    'Meals Included: Premium Breakfast & Farewell Elite Dinner',
                ],
            ),
            _day(
                6,
                'MATHURA / VRINDAVAN TO NEW DELHI / DEPARTURE',
                (
                    'CHERISHING ROYAL MEMORIES BEYOND DESTINATIONS Enjoy your final luxury breakfast at your premium stay. Your chauffeured private transport will guide you back via the highway to New Delhi Airport or Railway Station for your onward journey. Return home carrying a heart filled with spiritual harmony and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door highway drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Howard Plaza The Fern / similar | The Avenue Heritage / similar | Dinner)',
                'Multi-city Uttar Pradesh',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast &',
                4,
                1,
                description='OPTION 01 – DELUXE: Howard Plaza The Fern / similar | The Avenue Heritage / similar | Dinner)',
            ),
            _hotel(
                'Courtyard by Marriott / Taj | Hotel Agra | Nidhivan Sarovar Portico / similar | Dinner)',
                'Multi-city Uttar Pradesh',
                '5N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast &',
                4,
                2,
                description='OPTION 02 – PREMIUM: Courtyard by Marriott / Taj | Hotel Agra | Nidhivan Sarovar Portico / similar | Dinner)',
            ),
            _hotel(
                'The Trident Agra / ITC',
                'Uttar Pradesh',
                '5N',
                'Luxury',
                'Deluxe Room',
                'MAPAI + Elevated VIP',
                4,
                3,
                description='OPTION 03 – LUXURY: The Trident Agra / ITC',
            ),
            _hotel(
                'The Oberoi Amarvilas | (Premier Taj View)',
                'Multi-city Uttar Pradesh',
                '5N',
                'Ultra Luxury',
                'Facing Villa',
                'Culinary Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Oberoi Amarvilas | (Premier Taj View)',
            )
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Handpicked hotels as per chosen elite category.', 1),
            _inc_included('Luxury Transportation: Private AC Innova Crysta for all transfers & sightseeing.', 2),
            _inc_included('Curated Meal Plan: Daily luxury breakfast and gourmet dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest experience manager on call.', 4),
            _inc_included('Welcome Amenities: Custom family travel kit and traditional sweets box on arrival.', 5),
            _inc_included('Complimentary Experience: Private evening boat ride ticket on the Yamuna River.', 6),
            _inc_excluded('Airfare or long-distance interstate train tickets.', 7),
            _inc_excluded('Monument entry tickets, professional guide fees, camera permits.', 8),
            _inc_excluded('Personal expenses such as laundry, phone calls, or tips.', 9),
            _inc_excluded('Optional activities, extended detours, or evening theater programs.', 10),
        ],
    )
    return package, itinerary

def build_up_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UP-006'
    tour_code = 'TRG-UP-006'
    title = 'MUGHAL HERITAGE TRAIL • EPITOME OF IMPERIAL SPLENDOUR'
    duration = '04 Nights / 05 Days'
    slug = 'up-006-mughal-heritage-trail-epitome-of-imperial-splendour'
    itin_slug = 'up-006-mughal-heritage-trail-epitome-of-imperial-splendour-itinerary'
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
            _ph('Serial code UP-006 | TRAGUIN tour code TRG-UP-006', 1),
            _ph('State / Country: Uttar Pradesh / India | Category: Heritage / Luxury Vacation', 2),
            _ph('Destinations: Agra • Fatehpur', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Luxury Chauffeur- Driven Sedan / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private family historical overview with a professional architectural', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked scheduling designed to avoid large crowds at major', 9),
            _ph('Premium Handpicked Hotels: Accommodations selected strictly based on luxury comfort standards,', 10),
            _ph('Luxury Transportation: Professional chauffeurs providing seamless highway transitions and regional', 11)
        ],
        moods=['Luxury', 'Culture'],
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
        tagline='MUGHAL HERITAGE TRAIL',
        overview="MUGHAL HERITAGE TRAIL • EPITOME OF IMPERIAL SPLENDOUR Welcome to an unforgettable voyage through time, curated exclusively by TRAGUIN. Embark on a definitive Luxury Uttar Pradesh Holiday crafted to showcase the epic grandeur, intricate architecture, and profound cultural legacy of the legendary Mughal Empire. As your premier travel consultants, TRAGUIN transforms this journey into an elite immersive experience, matching grand historic sagas with handpicked hotels, refined gastronomy, and unparalleled comfort. Let the timeless beauty of the world's most romantic monuments paint a stunning background for your premium stays, promising unforgettable memories for you and your loved ones.\n\nTOUR OVERVIEW\nThis bespoke Mughal Heritage Trail offers a meticulously executed route designed for discerning travelers who want to explore imperial Indian history without sacrificing contemporary luxury. Moving in absolute privacy aboard a premium luxury vehicle guided by a uniform-clad, background-verified chauffeur, your transitions will be smooth and seamless. Your stay features our handpicked hotels that offer grand palace-like hospitality. Accompanied by a specialized gourmet meal plan (Breakfast and Dinner), the route also incorporates unique TRAGUIN curated experiences—including fast-track VIP entries, elite evening culinary tracks, and personalized local guides.\n\nWHY CHOOSE THE BEST UTTAR PRADESH TOUR PACKAGE?\nWhen planning a Luxury Uttar Pradesh Holiday, true explorers search for an ideal harmony between historic architecture and modern-day comfort. Uttar Pradesh houses the absolute crown jewels of India's golden heritage. From the world-famous Taj Mahal—an unmatched masterpiece and top tourist place in Uttar Pradesh—to the red sandstone expanse of Fatehpur Sikri and the grand fortifications of Agra Fort, the region offers incredibly rich history. For couples planning an upscale Uttar Pradesh Honeymoon Package or families choosing an elite Uttar Pradesh Family Tour, our specialized itinerary leads you straight to famous attractions and popular Instagram locations like Mehtab Bagh at sunset, the ornate tomb of Itmad-ud-Daulah, and the mystical temples of Vrindavan. Whether you are indulging in exquisite local Zardozi handicraft shopping, sampling centuries-old Mughal cuisine, or capturing iconic photography points, our TRAGUIN Uttar Pradesh Packages promise handpicked hotels, private premium stays, and exclusive experiences during the best time to visit Uttar Pradesh.",
        seo_title='UP-006 | MUGHAL HERITAGE TRAIL | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Uttar Pradesh package (UP-006 / TRG-UP-006): Agra • Fatehpur with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN AGRA', 1),
            _ih('Day 02: REVEALING THE TAJ MAHAL & AGRA FORT', 2),
            _ih('Day 03: EXCURSION TO FATEHPUR SIKRI', 3),
            _ih('Day 04: EXCURSION TO SIKANDRA & ITMAD-UD-DAULAH', 4),
            _ih('Day 05: MATHURA / VRINDAVAN EXCURSION & DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private family historical overview with a professional architectural', 6),
            _ih('Curated by TRAGUIN Experts: Handpicked scheduling designed to avoid large crowds at major', 7),
            _ih('Premium Handpicked Hotels: Accommodations selected strictly based on luxury comfort standards,', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN AGRA',
                (
                    'WELCOME TO THE IMPERIAL CITY – SUNSET OVER THE TAJ MAHAL Your premium Uttar Pradesh experience begins the moment you arrive in New Delhi or Agra. Your dedicated private luxury vehicle stands ready to transition you effortlessly to your handpicked premium luxury hotel in Agra. After checking in and enjoying a custom welcome refreshment, spend your afternoon relaxing. In the late afternoon, experience a private guided tour of Mehtab Bagh—the spectacular moonlit pleasure gardens across the Yamuna River, offering a breathtaking view of the Taj Mahal at sunset. This iconic photography point provides an ideal canvas to begin your holiday.'
                ),
                [
                    'Sightseeing Included: Yamuna Expressway scenic route, Mehtab Bagh sunset gardens view.',
                    'Evening Experience: Elite Mughal-inspired welcome dinner at a signature fine-dining restaurant.',
                    'Overnight Stay: Agra (Premium / Luxury Taj View Property)',
                    'Meals Included: Welcome Drink & Luxury Welcome Dinner',
                ],
            ),
            _day(
                2,
                'REVEALING THE TAJ MAHAL & AGRA FORT',
                (
                    "A DAWN ROMANCE WITH THE WORLD'S GREATEST WONDER Awake before dawn for a truly unforgettable memory. Travel via private eco-golf cart to witness the Taj Mahal during sunrise, as the shifting morning light casts soft golden tones across the pure white Makrana marble. A private historian will guide you through this monument of love, sharing deep architectural secrets and emotional storytelling. Return to your luxury resort for a lavish breakfast. In the afternoon, explore the massive red sandstone walls of the UNESCO World Heritage-listed Agra Fort, exploring its royal audience halls and marble palaces where emperors once ruled."
                ),
                [
                    "Sightseeing Included: Taj Mahal at Sunrise, Agra Fort, Shah Jahan's Private Marble Quarters.",
                    'Optional Activities: High-end live musical theater performance depicting the epic love story of the Taj Mahal.',
                    'Overnight Stay: Agra (Premium / Luxury Taj View Property)',
                    'Meals Included: Premium Breakfast & Luxury Dinner',
                ],
            ),
            _day(
                3,
                'EXCURSION TO FATEHPUR SIKRI',
                (
                    "THE IMPERIAL GHOST CITY OF EMPEROR AKBAR Indulge in a magnificent buffet breakfast before taking a short, scenic drive to Fatehpur Sikri, the legendary ghost city built by Emperor Akbar in the late 16th century. Walk through the beautifully preserved architectural masterpieces, including the towering Buland Darwaza (the world's highest gateway), the elegant Panch Mahal, and the serene, white marble tomb of Sufi Saint Salim Chishti. Your private guide will bring this beautifully deserted imperial capital to life through captivating historical stories."
                ),
                [
                    'Sightseeing Included: Fatehpur Sikri Complex, Buland Darwaza, Salim Chishti Shrine, Jodha Bai Palace.',
                    'Evening Experience: Exclusive high-tea service overlooking the surrounding rural landscape.',
                    'Overnight Stay: Agra (Premium / Luxury Resort)',
                    'Meals Included: Premium Breakfast & Traditional Mughlai Dinner',
                ],
            ),
            _day(
                4,
                'EXCURSION TO SIKANDRA & ITMAD-UD-DAULAH',
                (
                    'THE JEWEL BOX T0MB & THE EMPEROR\'S FINAL RESTING PLACE Dedicate your day to exploring the hidden architectural gems of the Mughal Heritage Trail. Visit the beautiful Tomb of Itmad-ud-Daulah, affectionately known as the "Baby Taj" due to its intricate marble inlay work, which served as inspiration for the Taj Mahal itself. Afterward, drive to Sikandra to marvel at the grand, multi-tiered red sandstone and white marble mausoleum of Emperor Akbar, set amidst expansive lawns inhabited by graceful blackbucks and peacocks.'
                ),
                [
                    "Sightseeing Included: Akbar's Mausoleum at Sikandra, Tomb of Itmad-ud-Daulah, local handicraft centers.",
                    'Optional Activities: A guided heritage walk through the ancient local bazaars and craft workshops of Agra.',
                    'Overnight Stay: Agra (Premium / Luxury Resort)',
                    'Meals Included: Premium Breakfast & Farewell Dinner Track',
                ],
            ),
            _day(
                5,
                'MATHURA / VRINDAVAN EXCURSION & DEPARTURE',
                (
                    'SPIRITUAL ESSENCE & RETURN CONCLUDING JOURNEY Following a final morning breakfast, check out of your premium hotel. Your private luxury transport will escort you on a spiritual excursion to the historic twin cities of Mathura and Vrindavan—the birthplace of Lord Krishna. Marvel at the breathtaking architecture of the Prem Mandir and Banke Bihari Temple before guiding you smoothly back to New Delhi. Return home carrying a heart filled with sweet familial bonds and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door highway drop-off to Delhi Airport / Railway Station.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Howard Plaza The Fern / Crystal | Sarovar / similar | Dinner)',
                'Multi-city Uttar Pradesh',
                '4N',
                'Deluxe',
                'Room',
                'MAPAI (Breakfast &',
                4,
                1,
                description='OPTION 01 – DELUXE: Howard Plaza The Fern / Crystal | Sarovar / similar | Dinner)',
            ),
            _hotel(
                'Radisson Hotel Agra / Courtyard | by Marriott / similar | Dinner)',
                'Multi-city Uttar Pradesh',
                '4N',
                'Premium',
                'Premium View Room',
                'MAPAI (Breakfast &',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Hotel Agra / Courtyard | by Marriott / similar | Dinner)',
            ),
            _hotel(
                'The Taj Gateway / ITC Mughal | Resort & Spa | Welcome Perks',
                'Multi-city Uttar Pradesh',
                '4N',
                'Luxury',
                'Suite',
                'MAPAI + Heritage',
                4,
                3,
                description='OPTION 03 – LUXURY: The Taj Gateway / ITC Mughal | Resort & Spa | Welcome Perks',
            ),
            _hotel(
                'The Oberoi Amarvilas (Direct Taj | VVIP Royal Taj View',
                'Multi-city Uttar Pradesh',
                '4N',
                'Ultra Luxury',
                'Premier Suite',
                'MAPAI Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Oberoi Amarvilas (Direct Taj | VVIP Royal Taj View',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 04 Nights in handpicked properties with luxury view options.', 1),
            _inc_included('Luxury Transportation: Private dedicated sedan for all point-to-point sightseeing.', 2),
            _inc_included('Curated Meal Plan: Daily premium breakfast and gourmet dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 personalized customer care and concierge assistance.', 4),
            _inc_included('Welcome Amenities: Custom heritage travel kit and cold-pressed juices upon arrival.', 5),
            _inc_included('Complimentary Experience: Private eco-friendly golf cart ride tickets at the Taj Mahal.', 6),
            _inc_excluded('Airfare, domestic flight tickets, or interstate train travel.', 7),
            _inc_excluded('Monument entry tickets, professional guide fees, camera permits.', 8),
            _inc_excluded('Personal expenses such as laundry, phone calls, or tipping staff.', 9),
            _inc_excluded('Any optional excursions, live cultural events, or shopping spend.', 10),
        ],
    )
    return package, itinerary

def build_up_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UP-007'
    tour_code = 'TRG-UP-007'
    title = 'DIVINE UTTAR PRADESH • A JOURNEY OF FAITH, SERENITY & LUXURY'
    duration = '05 Nights / 06 Days'
    slug = 'up-007-divine-uttar-pradesh-a-journey-of-faith-serenity-luxury'
    itin_slug = 'up-007-divine-uttar-pradesh-a-journey-of-faith-serenity-luxury-itinerary'
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
            _ph('Serial code UP-007 | TRAGUIN tour code TRG-UP-007', 1),
            _ph('State / Country: Uttar Pradesh / India | Category: Senior Citizen Special / Spiritual', 2),
            _ph('Destinations: Varanasi •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury AC Innova Crysta / MAPAI (Veg)', 7),
            _ph('TRAGUIN Signature Experience: Hand-vetted, soft-spoken local guides specializing in care for senior', 8),
            _ph('Curated by TRAGUIN Experts: Pre-arranged e-rickshaws for temple lanes where regular automotive', 9),
            _ph('Premium Handpicked Hotels: Properties selected for elevator infrastructure, walk-in showers, and quiet', 10),
            _ph('Exclusive Recommendations: Hand-vetted dining spots emphasizing freshly prepared, organic regional', 11)
        ],
        moods=['Luxury', 'Spiritual', 'Leisure'],
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
        tagline='DIVINE UTTAR PRADESH',
        overview='DIVINE UTTAR PRADESH • A JOURNEY OF FAITH, SERENITY & LUXURY Welcome to a soul-stirring spiritual odyssey thoughtfully designed by TRAGUIN. Embark on the finest Uttar Pradesh Senior Citizen Special Tour, meticulously organized to blend sacred ancient heritage with absolute physical comfort and relaxed pacing. As your premier travel consultants, TRAGUIN elevates your pilgrimage into a seamless luxury holiday filled with premium stays, wheel-chair accessible routes where needed, hassle-free private darshans, and expert local guidance. From the eternal ghats of Varanasi and the holy Sangam of Prayagraj to the newly resplendent temples of Ayodhya, let the divine atmosphere create unforgettable memories for your loved ones.\n\nTOUR OVERVIEW\nThis custom-crafted spiritual itinerary offers an exceptional balance between sacred rituals, profound historical insights, and premium relaxation. Understanding the specific needs of senior citizens, our route minimizes walking distances and features smooth highway transfers in a premium, chauffeured AC vehicle. With a curated meal plan offering freshly prepared, hygienic, and nutritious vegetarian breakfasts and dinners, your health and peace of mind remain paramount. This journey is the definitive premium Uttar Pradesh experience, incorporating signature TRAGUIN curated experiences like private boat ceremonies, priority temple entries, and 24/7 dedicated assistance.\n\nWHY CHOOSE THE BEST UTTAR PRADESH TOUR PACKAGE?\nWhen planning a Luxury Uttar Pradesh Holiday, discerning families seek a journey that guarantees deep spiritual connection without compromising on physical well-being. The sacred circuits of Northern India host some of the most iconic attractions in the world. From the ancient, pulsating energy of Kashi Vishwanath Temple in Varanasi—recognized globally as a top tourist place in Uttar Pradesh—to the majestic confluence of three holy rivers at Prayagraj, the region offers unparalleled cultural immersion. For multi-generational travelers booking a tailored Uttar Pradesh Family Tour, or elders choosing an Uttar Pradesh Pilgrimage Package, the itinerary captures highly sought-after experiences. Witness the grand evening Ganga Aarti, capture popular Instagram locations like the beautifully sculpted corridors of the newly opened Ram Mandir in Ayodhya, and explore the peaceful Buddhist monuments of Sarnath. Our custom- designed TRAGUIN Uttar Pradesh Packages guarantee premium handpicked hotels, smooth transit layouts, and immersive experiences during the best time to visit Uttar Pradesh.',
        seo_title='UP-007 | DIVINE UTTAR PRADESH | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Uttar Pradesh package (UP-007 / TRG-UP-007): Varanasi • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN VARANASI', 1),
            _ih('Day 02: SACRED VARANASI DARSHAN & SARNATH EXCURSION', 2),
            _ih('Day 03: VARANASI TO PRAYAGRAJ', 3),
            _ih('Day 04: PRAYAGRAJ TO AYODHYA', 4),
            _ih('Day 05: FULL DAY IN AYODHYA', 5),
            _ih('Day 06: AYODHYA TO LUCKNOW / VARANASI DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Hand-vetted, soft-spoken local guides specializing in care for senior', 7),
            _ih('Curated by TRAGUIN Experts: Pre-arranged e-rickshaws for temple lanes where regular automotive', 8),
            _ih('Premium Handpicked Hotels: Properties selected for elevator infrastructure, walk-in showers, and quiet', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN VARANASI',
                (
                    'WELCOME TO THE ETERNAL CITY – SUNSET RIVERSIDE SPIRITUALITY Your premium Uttar Pradesh experience begins upon arrival at Varanasi Airport or Railway Station. A dedicated TRAGUIN representative and a private luxury transport vehicle await to drive you comfortably to your premium handpicked hotel. After a smooth check-in and an afternoon of rest, embark on an emotional storytelling evening. Glide on a private, stable bajra (traditional boat) along the Ganges to view the magnificent Subah-e-Banaras and the legendary Ganga Aarti at Dashashwamedh Ghat from a comfortable, reserved vantage point. explanation.'
                ),
                [
                    'Sightseeing Included: Ganga Ghats, Private Reserved Boat Cruise, Dashashwamedh Aarti.',
                    'Evening Experience: Exclusive illuminated evening boat ride with complimentary traditional Vedic hymns',
                    'Overnight Stay: Varanasi (Premium / Luxury Heritage Hotel)',
                    'Meals Included: Welcome Drink & Gourmet Vegetarian Dinner',
                ],
            ),
            _day(
                2,
                'SACRED VARANASI DARSHAN & SARNATH EXCURSION',
                (
                    'DIVINE BLESSINGS & BREATHTAKING LANDSCAPES OF PEACE Experience a divine morning with priority access for darshan at the holy Kashi Vishwanath Temple corridor, thoughtfully managed by your guide to avoid long queues. Visit the sacred Mata Annapurna Temple and the historic Vishalakshi Temple. Return to your premium stay for a relaxed breakfast. In the afternoon, enjoy a short, smooth drive to Sarnath, where Lord Buddha delivered his first sermon. Explore the tranquil breathtaking landscapes of the Deer Park and view the iconic Dhamek Stupa, offering pristine photography points. Museum.'
                ),
                [
                    'Sightseeing Included: Kashi Vishwanath Corridor, Sarnath Deer Park, Dhamek Stupa, Sarnath Archeological',
                    'Optional Activities: Interactive private session with an expert local scholar on Banaras heritage.',
                    'Overnight Stay: Varanasi (Premium / Luxury Heritage Hotel)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'VARANASI TO PRAYAGRAJ',
                (
                    'THE CONFLUENCE OF HOLY RIVERS – THE TRIVENI SANGAM MILAN After a nourishing breakfast, enjoy a smooth ride along the national highway to Prayagraj. Check into your luxury boutique hotel. In the afternoon, proceed to the Triveni Sangam—the mystical confluence of the Ganga, Yamuna, and Saraswati rivers. Board a specially chartered, high-sided private motorboat equipped with safety cushions and lifejackets to reach the holy bathing point comfortably. Perform a personalized family prayer ceremony led by a vetted priest. (Reclining Idol).'
                ),
                [
                    'Sightseeing Included: Triveni Sangam, Anand Bhavan (Nehru Family Ancestral Home), Hanuman Temple',
                    'Evening Experience: Peaceful sunset stroll along the manicured lawns of the Civil Lines promenade.',
                    'Overnight Stay: Prayagraj (Selected Premium Business / Luxury Property)',
                    'Meals Included: Breakfast & Traditional Satvik Dinner',
                ],
            ),
            _day(
                4,
                'PRAYAGRAJ TO AYODHYA',
                (
                    'JOURNEY TO THE RAM JANMABHOOMI – IMMERSIVE RELIGIOUS SPLENDOUR Depart for the historic and newly resplendent city of Ayodhya. The scenic route runs through rural landscapes and well-maintained state highways. Upon arriving, check into your premium luxury hotel and rest. In the late afternoon, visit the serene Saryu River Ghats. Experience the beautifully synchronized evening Saryu Aarti, capturing the scenic beauty of the illuminated riverbanks from comfortable seating.'
                ),
                [
                    'Sightseeing Included: Saryu River Ghats, Ram Ki Paidi, Nageshwarnath Temple.',
                    'Evening Experience: Illuminated heritage walk around Ram Ki Paidi with traditional sweet tastings.',
                    'Overnight Stay: Ayodhya (Premium Boutique / Luxury Resort)',
                    'Meals Included: Breakfast & Premium Vegetarian Buffet Dinner',
                ],
            ),
            _day(
                5,
                'FULL DAY IN AYODHYA',
                (
                    "DIVINE DARSHAN AT RAM MANDIR & SACRED LANDMARKS This day is a focal highlight of your premium Uttar Pradesh experience. Proceed for an early morning, priority- assisted darshan at the magnificent, newly constructed Shri Ram Janmabhoomi Mandir. Admire the exquisite architecture and peaceful aura of the temple complex. Later, visit the fort-like Hanumangarhi Temple and the historical Kanak Bhawan Palace, renowned for its golden idols and musical bhajans. Spend a relaxed evening at leisure in the city's gardens."
                ),
                [
                    'Sightseeing Included: Shri Ram Janmabhoomi Mandir, Hanumangarhi, Kanak Bhawan, Dashrath Mahal.',
                    'Optional Activities: Shopping for authentic brass icons, religious souvenirs, and special local treats.',
                    'Overnight Stay: Ayodhya (Premium Boutique / Luxury Resort)',
                    'Meals Included: Breakfast & Special Farewell Dinner',
                ],
            ),
            _day(
                6,
                'AYODHYA TO LUCKNOW / VARANASI DEPARTURE',
                (
                    'CHERISHING FAITH & UNFORGETTABLE MEMORIES Enjoy a final lavish breakfast at your premium boutique hotel. Your private luxury transport will safely drive you along the expressway to Lucknow Airport (or back to Varanasi Airport, based on your departure flight preference). Return home filled with divine spiritual rejuvenation and unforgettable memories crafted meticulously by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private door-to-door luxury highway drop-off to the airport or station.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Meraden Grand / similar | Hotel Kanha Shyam / similar | Hotel Ramprastha / similar',
                'Multi-city Uttar Pradesh',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Meraden Grand / similar | Hotel Kanha Shyam / similar | Hotel Ramprastha / similar',
            ),
            _hotel(
                'Radisson Hotel / Ramada Plaza | Cygnett Inn Paras / similar | The Park Inn by Radisson',
                'Multi-city Uttar Pradesh',
                '5N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Hotel / Ramada Plaza | Cygnett Inn Paras / similar | The Park Inn by Radisson',
            ),
            _hotel(
                'BrijRama Palace | (Heritage Luxury) | Welcomheritage Hotel / similar | Amatra Hotels / Royal | Heritage',
                'Multi-city Uttar Pradesh',
                '5N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: BrijRama Palace | (Heritage Luxury) | Welcomheritage Hotel / similar | Amatra Hotels / Royal | Heritage',
            ),
            _hotel(
                'Taj Ganges Varanasi | The Taj Mahal Palace',
                'Multi-city Uttar Pradesh',
                '5N',
                'Ultra Luxury',
                'Suite (VIP)',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Taj Ganges Varanasi | The Taj Mahal Palace',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Selected elderly-friendly accessible hotels as per category.', 1),
            _inc_included('Luxury Transportation: Private AC Innova Crysta for smooth, cushioned highway transfers.', 2),
            _inc_included('Curated Meal Plan: Daily mild, hygienic vegetarian breakfasts and hot dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest experience manager and porterage assistance.', 4),
            _inc_included('Welcome Amenities: Customized spiritual kit containing sacred scarves and wellness items.', 5),
            _inc_included('Complimentary Experience: Specially chartered private boat ride at Varanasi and Prayagraj.', 6),
            _inc_excluded('Airfare or long-distance main train ticketing to Uttar Pradesh.', 7),
            _inc_excluded('Special customized VIP Abhishek or Puja tickets (can be pre-booked on request).', 8),
            _inc_excluded('Personal expenses such as laundry, telephone calls, tips, and insurance.', 9),
            _inc_excluded('Any item or temple offering not explicitly listed in the inclusions.', 10),
        ],
    )
    return package, itinerary

def build_up_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UP-008'
    tour_code = 'TRG-UP-008'
    title = 'ROYAL UTTAR PRADESH • LEGENDS, OPULENCE & HERITAGE'
    duration = '05 Nights / 06 Days'
    slug = 'up-008-royal-uttar-pradesh-legends-opulence-heritage'
    itin_slug = 'up-008-royal-uttar-pradesh-legends-opulence-heritage-itinerary'
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
            _ph('Serial code UP-008 | TRAGUIN tour code TRG-UP-008', 1),
            _ph('State / Country: Uttar Pradesh / India | Category: Luxury Holiday / Royal Legacy', 2),
            _ph('Destinations: Varanasi •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Chauffeur-Driven Luxury MUV / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private family interaction and historical storytelling briefing before', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked routing to avoid highway traffic, maximizing your leisure and', 9),
            _ph('Premium Handpicked Hotels: Accommodations selected strictly based on premium safety standards,', 10),
            _ph('Luxury Transportation: Professional, uniform-clad, background-verified tourist chauffeurs who know the', 11)
        ],
        moods=['Luxury', 'Culture'],
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
        tagline='ROYAL UTTAR PRADESH',
        overview="ROYAL UTTAR PRADESH • LEGENDS, OPULENCE & HERITAGE Welcome to a timeless journey through the absolute spiritual and royal heartland of India, masterfully curated exclusively by TRAGUIN. Embark on a definitive Luxury Uttar Pradesh Holiday crafted meticulously to capture the legendary monuments, breathtaking landscapes, and exquisite Awadhi grandeur of this monumental state. As your elite travel consultants, TRAGUIN transforms your voyage into an elite experience featuring handpicked hotels, intimate local interactions, and immersive storytelling. From the ancient steps of sacred Varanasi to the poetic palaces of regal Lucknow and the sublime marble romance of Agra, every detail is seamlessly curated to weave unforgettable memories.\n\nTOUR OVERVIEW\nThis elite itinerary offers an unparalleled look into the core cultural capitals of the region, specifically designed as the definitive Best Uttar Pradesh Tour Package. Travelling in an absolute premium, private luxury transport vehicle with a dedicated professional chauffeur, your family or companions will enjoy unrivaled comfort and privacy. With an impeccably tailored meal plan featuring daily multi-cuisine breakfasts and specialized regional gourmet dinners, this route represents the highest standard of a Premium Uttar Pradesh Experience. Every single moment includes the hallmark TRAGUIN curated experience note, providing private VIP access, expert historical narrations, and flawless round-the-clock ground assistance.\n\nWHY CHOOSE THE BEST UTTAR PRADESH TOUR PACKAGE?\nWhen planning a Luxury Uttar Pradesh Holiday, worldly travelers look for a path that beautifully bridges deep antiquity with modern, high-end comfort. Uttar Pradesh houses some of the most iconic attractions on Earth. From the unparalleled spiritual presence of Varanasi's ghats—the ultimate tourist highlights for cultural discovery—to the grand architecture of Nawabi Lucknow and the world-renowned symbol of love in Agra, Uttar Pradesh sightseeing is an absolute feast for the soul. For discerning couples searching for a majestic Uttar Pradesh Honeymoon Package or families booking a Uttar Pradesh Family Tour, the region reveals a magnificent collection of popular Instagram locations. Capture the golden morning light reflecting over the Ganges, the symmetry of the Bara Imambara, or the perfect marble reflections at the Taj Mahal. Indulge in classic Chikan embroidery shopping, savor fine slow- cooked culinary heritage, and explore ancient lanes with the luxury of TRAGUIN Uttar Pradesh Packages, guaranteeing premium stays and exclusive experiences during the best time to visit Uttar Pradesh.",
        seo_title='UP-008 | ROYAL UTTAR PRADESH | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Uttar Pradesh package (UP-008 / TRG-UP-008): Varanasi • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN VARANASI', 1),
            _ih('Day 02: VARANASI SIGHTSEEING TO LUCKNOW', 2),
            _ih('Day 03: LUCKNOW HERITAGE EXPLORATION', 3),
            _ih('Day 04: LUCKNOW TO AGRA VIA EXPRESSWAY', 4),
            _ih('Day 05: ULTIMATE TAJ MAHAL SUNRISE & FATEHPUR SIKRI', 5),
            _ih('Day 06: AGRA TO DELHI / DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private family interaction and historical storytelling briefing before', 7),
            _ih('Curated by TRAGUIN Experts: Handpicked routing to avoid highway traffic, maximizing your leisure and', 8),
            _ih('Premium Handpicked Hotels: Accommodations selected strictly based on premium safety standards,', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN VARANASI',
                (
                    'THE ETERNAL CITY – MYSTICAL GANGES & GOLDEN SHORELINE Your premium Uttar Pradesh experience begins as you land in Varanasi, one of the oldest living cities in the world. A private luxury transport vehicle will greet you for a smooth check-in at your handpicked premium palace hotel. After refreshing, step into the mystical spiritual heart of India. As the evening sets, enjoy a private cruise over the sacred Ganges River to witness the soul-stirring Ganga Aarti at Dashashwamedh Ghat. The rhythmic chanting, flaming brass lamps, and incense smoke create deeply emotional storytelling moments and incredible photography points. Corridor corridor walk.'
                ),
                [
                    'Sightseeing Included: Ganges River Private Boat Cruise, Dashashwamedh Ghat Ganga Aarti, Kashi Vishwanath',
                    'Evening Experience: Reserved luxury seating on a private terrace platform for the grand evening prayers.',
                    'Overnight Stay: Varanasi (Premium Heritage Luxury Hotel / Palace)',
                    'Meals Included: Welcome Drink & Gourmet Local Dinner',
                ],
            ),
            _day(
                2,
                'VARANASI SIGHTSEEING TO LUCKNOW',
                (
                    'DAWN ECO-TOUR & THE ROAD TO NAWABI GRANDEUR Experience a breathtaking morning subah-e-banaras boat ride as the city wakes up to Vedic chants and soft morning light. Return to your premium hotel for breakfast, then explore the historic archeological ruins of Sarnath, where Lord Buddha delivered his first sermon. In the afternoon, embark on a smooth private highway transfer to the city of Nawabs—Lucknow. Arrive and check into your ultra-luxury colonial property to relax for the evening.'
                ),
                [
                    'Sightseeing Included: Sarnath Deer Park & Stupas, Ashoka Pillar Museum, Scenic highway transition.',
                    "Optional Activities: An insider walking tour of Varanasi's ancient hidden silk-weaving lanes.",
                    'Overnight Stay: Lucknow (Premium Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Royal Awadhi Dinner',
                ],
            ),
            _day(
                3,
                'LUCKNOW HERITAGE EXPLORATION',
                (
                    "POETIC ARCHITECTURE, COLONIAL LEGACIES & FINE DINING Spend a magnificent day exploring the unmatched culture and architectural attractions of Lucknow. Marvel at the grand Bara Imambara, famous for its incredible Bhool Bhulaiya labyrinth. Walk through the historic British Residency, a quiet site filled with stories from the 1857 uprising. In the afternoon, enjoy high-end shopping for authentic Chikan textiles in Hazratganj, and savor the city's legendary culinary legacy with soft, melt-in-the- mouth kebabs. experts."
                ),
                [
                    'Sightseeing Included: Bara Imambara, Chhota Imambara, Rumi Darwaza, The British Residency, Hazratganj.',
                    'Evening Experience: An exclusive multi-course Awadhi Dastarkhwan dinner experience curated by TRAGUIN',
                    'Overnight Stay: Lucknow (Premium Luxury Hotel)',
                    'Meals Included: Bespoke Breakfast & Royal Kebab Dinner',
                ],
            ),
            _day(
                4,
                'LUCKNOW TO AGRA VIA EXPRESSWAY',
                (
                    'CRUISING TOWARDS THE EMPIRE OF MARBLE ROMANCE Depart Lucknow after a lavish breakfast and cruise along the smooth, world-class Agra-Lucknow Expressway in your private luxury transport. Arrive in Agra by midday and check into your luxury resort, where rooms offer unhindered views of the horizon. In the afternoon, visit the massive Agra Fort, a UNESCO World Heritage site carved from red sandstone that highlights the sheer power of the Mughal Empire. End the day watching the sunset paint the white marble of the Taj Mahal in soft shades of pink from across the Yamuna River at Mehtab Bagh.'
                ),
                [
                    'Sightseeing Included: Agra Fort, Mehtab Bagh Sunset Point, Itmad-ud-Daulah (Baby Taj).',
                    'Evening Experience: High tea over a private viewing deck with views of the Agra cityscape.',
                    'Overnight Stay: Agra (Ultra Luxury Resort / View Property)',
                    'Meals Included: Premium Breakfast & Mughal Buffet Dinner',
                ],
            ),
            _day(
                5,
                'ULTIMATE TAJ MAHAL SUNRISE & FATEHPUR SIKRI',
                (
                    'ICONIC ATTRACTIONS & THE SUNRISE EPIPHANY Awake before dawn for an unforgettable, immersive experience: the sunrise over the Taj Mahal. Watch the morning light illuminate the pure white marble monument, free from daytime crowds—an essential highlight of any top tour package. Return to your luxury property for a relaxed breakfast. In the afternoon, take an excursion to Fatehpur Sikri, the perfectly preserved ghost city of Emperor Akbar, and marvel at the colossal Buland Darwaza gate. Shrine.'
                ),
                [
                    'Sightseeing Included: Taj Mahal interior tour, Fatehpur Sikri Palace complex, Buland Darwaza, Salim Chishti',
                    'Optional Activities: A private marble inlay handicraft workshop with local master craftsmen.',
                    'Overnight Stay: Agra (Ultra Luxury Resort)',
                    'Meals Included: Gourmet Breakfast & Farewell Celebration Dinner',
                ],
            ),
            _day(
                6,
                'AGRA TO DELHI / DEPARTURE',
                (
                    'CHERISHING THE ROYAL MEMORIES OF UTTAR PRADESH Enjoy your final lavish breakfast at your premium hotel. Your private luxury vehicle will smoothly drive you along the Yamuna Expressway to New Delhi Airport or Railway Station for your onward journey. Return home carrying a heart filled with beautiful bonds, royal stories, and unforgettable memories designed flawlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door expressway drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Radisson Hotel / similarNovotel Gomti Nagar / | similar | Howard Plaza The Fern / similar',
                'Multi-city Uttar Pradesh',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Radisson Hotel / similarNovotel Gomti Nagar / | similar | Howard Plaza The Fern / similar',
            ),
            _hotel(
                'Taj Ganges Varanasi / similar | Hyatt Regency Lucknow / similar | Radisson Hotel Taj East',
                'Multi-city Uttar Pradesh',
                '5N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Taj Ganges Varanasi / similar | Hyatt Regency Lucknow / similar | Radisson Hotel Taj East',
            ),
            _hotel(
                'BrijRama Palace | (Heritage) | Taj Mahal Lucknow / similar | ITC Mughal, A Luxury',
                'Multi-city Uttar Pradesh',
                '5N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: BrijRama Palace | (Heritage) | Taj Mahal Lucknow / similar | ITC Mughal, A Luxury',
            ),
            _hotel(
                'Taj Nadesar Palace | The Oberoi Amarvilas | (Taj View)',
                'Multi-city Uttar Pradesh',
                '5N',
                'Ultra Luxury',
                'The Centrestage Villa',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Taj Nadesar Palace | The Oberoi Amarvilas | (Taj View)',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury accommodations based on your selected hotel tier.', 1),
            _inc_included('Luxury Transportation: Private chauffeur-driven vehicle for all transfers and sightseeing.', 2),
            _inc_included('Curated Meal Plan: Lavish daily breakfast and gourmet dinners (MAPAI standard).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest relations executive on standby.', 4),
            _inc_included('Welcome Amenities: Customized luxury welcome gifts and travel kit on arrival.', 5),
            _inc_included('Complimentary Experience: Reserved private boat ride on the sacred Ganges River.', 6),
            _inc_excluded('Airfare, flight connections, or domestic train tickets.', 7),
            _inc_excluded('Monument entry tickets, professional guide fees, camera permits.', 8),
            _inc_excluded('Personal expenses such as laundry, phone calls, room service, or tips.', 9),
            _inc_excluded('Any optional adventure activities, boutique tours, or unexpected route updates.', 10),
        ],
    )
    return package, itinerary

def build_up_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UP-009'
    tour_code = 'TRG-UP-009'
    title = 'HISTORICAL UTTAR PRADESH • LEGACY, LEARNING & ARCHITECTURE'
    duration = '04 Nights / 05 Days'
    slug = 'up-009-historical-uttar-pradesh-legacy-learning-architecture'
    itin_slug = 'up-009-historical-uttar-pradesh-legacy-learning-architecture-itinerary'
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
            _ph('Serial code UP-009 | TRAGUIN tour code TRG-UP-009', 1),
            _ph('State / Country: Uttar Pradesh / India | Category: School & Educational Historical Tour', 2),
            _ph('Destinations: Agra • Fatehpur', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Premium Luxury AC Coaches / APBAI (All Meals Included)', 7),
            _ph('TRAGUIN Signature Experience: Private architecture workshop and acoustic testing session inside the', 8),
            _ph('Curated by TRAGUIN Experts: Safe routes and verified, hygiene-audited hotels perfect for educational', 9),
            _ph('Personalized Assistance: Experienced historical storytellers who make learning interactive for students.', 10),
            _ph('TRAGUIN Premium Educational Proposal — UP-009 5', 11)
        ],
        moods=['Luxury', 'Culture', 'Educational'],
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
        tagline='HISTORICAL UTTAR PRADESH',
        overview="PACKAGE HISTORICAL UTTAR PRADESH • LEGACY, LEARNING & ARCHITECTURE Welcome to an educational exploration of grand dimensions curated exclusively by TRAGUIN. Embark on the finest Historical Uttar Pradesh student journey, carefully customized to bring history books to life through breathtaking landscapes, grand royal courts, and architectural marvels. As your trusted premium travel consultants, TRAGUIN ensures a safe, enriching, and luxury holiday standard for educational institutions. From the iconic symmetry of the Taj Mahal to the political wisdom carved inside Fatehpur Sikri and the classic Nawabi heritage of Lucknow, we turn a student tour into an unforgettable repository of memories.\n\nTOUR OVERVIEW\nThis bespoke Uttar Pradesh Family Tour and student educational itinerary is masterfully designed to balance safety, academic value, and premium comfort. Traveling in customized luxury air-conditioned coaches with expert multi-lingual historical guides and round-the-clock medical assistance, every single day is tightly managed. With a comprehensive meal plan covering freshly prepared nutritious buffet meals, this itinerary ensures active students stay energized. Every stage of this path includes the distinct TRAGUIN curated experience note, meaning prioritized monument permissions, expert storytelling interactions, and seamless administrative support.\n\nWHY VISIT HISTORICAL PLACES WITH THE BEST UTTAR PRADESH\nTOUR PACKAGE? When considering a Luxury Uttar Pradesh Holiday for academic bodies, schools expect structural reliability, safe premium stays, and high informational quality. Uttar Pradesh boasts some of the world's most sought- after iconic attractions. From the internationally admired Taj Mahal in Agra—a top tourist place in Uttar Pradesh for global historical analysis—to the intricate maze of Bara Imambara in Lucknow, Uttar Pradesh sightseeing provides a deep and immersive look into world history. For educational bodies securing a custom Uttar Pradesh Honeymoon Package, family escape, or large student cohort group, the state provides famous Instagram locations like the majestic buland darwaza and the beautiful banks of the Gomti River. Whether exploring regional marble inlay art, looking at medieval military architecture, or tasting legendary culinary treats, our customized TRAGUIN Uttar Pradesh Packages guarantee premium handpicked hotels and exclusive experiences during the best time to visit Uttar Pradesh. TRAGUIN Premium Educational Proposal — UP-009 2",
        seo_title='UP-009 | HISTORICAL UTTAR PRADESH | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Uttar Pradesh package (UP-009 / TRG-UP-009): Agra • Fatehpur with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN AGRA', 1),
            _ih('Day 02: THE TAJ MAHAL & FATEHPUR SIKRI EXCURSION', 2),
            _ih('Day 03: AGRA TO LUCKNOW (VIA EXPRESSWAY)', 3),
            _ih('Day 04: LUCKNOW HERITAGE EXPLORATION', 4),
            _ih('Day 05: DEPARTURE FROM LUCKNOW', 5),
            _ih('TRAGUIN Signature Experience: Private architecture workshop and acoustic testing session inside the', 6),
            _ih('Curated by TRAGUIN Experts: Safe routes and verified, hygiene-audited hotels perfect for educational', 7),
            _ih('Personalized Assistance: Experienced historical storytellers who make learning interactive for students.', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN AGRA',
                (
                    'ENTRY TO THE CITY OF THE TAJ – ARCHITECTURAL MARVELS Your premium Uttar Pradesh experience begins upon arrival at Delhi or Agra station, where a private luxury coach waits to welcome the group. Drive along the Yamuna Expressway to the historic capital of the Mughal Empire—Agra. Check into your premium handpicked hotels and enjoy a refreshing welcome note briefing. In the afternoon, visit the magnificent Agra Fort, a massive red sandstone fortress containing grand royal chambers where emperors lived, creating an inspiring learning environment.'
                ),
                [
                    'Sightseeing Included: Agra Fort, Sheesh Mahal, Diwan-i-Aam, Diwan-i-Khas.',
                    'Evening Experience: Interactive historical quiz night and introductory briefing session by TRAGUIN experts.',
                    'Overnight Stay: Agra (Premium Selected Student-Friendly Luxury Hotel)',
                    'Meals Included: Welcome Drink, Mid-day Lunch & Luxury Buffet Dinner',
                ],
            ),
            _day(
                2,
                'THE TAJ MAHAL & FATEHPUR SIKRI EXCURSION',
                (
                    'SYMBOL OF IMMORTAL LOVE & THE GHOST CITY OF STONE Awake early to witness the unparalleled scenic beauty of the Taj Mahal at sunrise, a UNESCO World Heritage site and the absolute centerpiece of Uttar Pradesh sightseeing. Guide-led educational groups will focus on its perfect symmetry and marble engineering. Return to the hotel for breakfast, then drive to Fatehpur Sikri, the perfectly preserved ghost city of Emperor Akbar. Walk through the imposing Buland Darwaza and study ancient water harvesting systems.'
                ),
                [
                    'Sightseeing Included: The Taj Mahal, Fatehpur Sikri Palace Complex, Buland Darwaza, Jama Masjid.',
                    'Optional Activities: Live demonstration of Pietra Dura (marble inlay artwork) by local master craftsmen.',
                    'Overnight Stay: Agra (Premium Selected Student-Friendly Luxury Hotel)',
                    'Meals Included: Full Board Plan (Breakfast, Lunch & Dinner)',
                ],
            ),
            _day(
                3,
                'AGRA TO LUCKNOW (VIA EXPRESSWAY)',
                (
                    'TRANSIT TO THE LAND OF NAWABS – AWADHI HERITAGE Enjoy a wholesome breakfast before setting off on a smooth drive over the Agra-Lucknow Expressway in your premium transport vehicle. Arrive in Lucknow, the historical capital city renowned for its refined manners, poetry, and beautiful architecture. Check into your premium stays and spend the late afternoon visiting the British Residency, a major historical landmark that tells the story of the Uprising of 1857. TRAGUIN Premium Educational Proposal — UP-009 3'
                ),
                [
                    'Sightseeing Included: Agra-Lucknow Expressway corridor scenic route, The British Residency Museum.',
                    'Evening Experience: Cultural evening focusing on Awadhi history, heritage storytelling, and traditional music.',
                    'Overnight Stay: Lucknow (Premium Luxury Business Class Hotel)',
                    'Meals Included: Full Board Plan (Breakfast, Highway Lunch & Gourmet Dinner)',
                ],
            ),
            _day(
                4,
                'LUCKNOW HERITAGE EXPLORATION',
                (
                    'ACOUSTICS, LABYRINTHS & GRAND ARCHES Devote your day to exploring the iconic attractions of Lucknow. Visit the magnificent Bara Imambara, famous for its incredible Bhool Bhulaiya (an acoustic labyrinth where students can experiment with echoes and sound engineering). Walk under the grand Rumi Darwaza, also known as the Turkish Gate, and explore the beautiful Husainabad Clock Tower before a photography stop at the grand Ambedkar Memorial Park. Tower.'
                ),
                [
                    'Sightseeing Included: Bara Imambara, Bhool Bhulaiya Labyrinth, Chhota Imambara, Rumi Darwaza, Clock',
                    'Optional Activities: A guided walk through traditional Chikan embroidery textile manufacturing centers.',
                    'Overnight Stay: Lucknow (Premium Luxury Business Class Hotel)',
                    'Meals Included: Full Board Plan with special local street-food options included.',
                ],
            ),
            _day(
                5,
                'DEPARTURE FROM LUCKNOW',
                (
                    'CHERISHING KNOWLEDGE AND UNFORGETTABLE MEMORIES Indulge in a final hearty breakfast at your premium stays. Gather your educational journals and memories as your private luxury transport transfers your group safely to Lucknow Airport or Charbagh Railway Station for the journey back home. Your educational tour concludes with new knowledge and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private group luxury transfers to the airport or station.',
                    'Meals Included: Nutritious Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Howard Plaza The',
                'Agra',
                '4N',
                'Deluxe',
                'Fern / similar',
                'Hotel Levana / Regnant /',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Howard Plaza The | Fern / similar | Hotel Levana / Regnant /',
            ),
            _hotel(
                'Crystal Sarovar Premiere /',
                'Agra',
                '4N',
                'Premium',
                'similar',
                'Novotel Lucknow Gomti',
                4,
                2,
                description='OPTION 02 – PREMIUM: Crystal Sarovar Premiere / | similar | Novotel Lucknow Gomti',
            ),
            _hotel(
                'The Taj Gateway /',
                'Agra',
                '4N',
                'Luxury',
                'Courtyard by Marriott',
                'Renaissance Lucknow',
                4,
                3,
                description='OPTION 03 – LUXURY: The Taj Gateway / | Courtyard by Marriott | Renaissance Lucknow',
            ),
            _hotel(
                'The Oberoi Amarvilas',
                'Agra',
                '4N',
                'Ultra Luxury',
                '(Luxury View)',
                'The Taj Mahal Lucknow',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Oberoi Amarvilas | (Luxury View) | The Taj Mahal Lucknow',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Multi-night stays at handpicked hotels approved for safety.', 1),
            _inc_included('Luxury Transportation: High-deck luxury AC tourist coaches with seatbelts.', 2),
            _inc_included('All Meals: Buffet breakfast, hot lunches, and balanced dinners.', 3),
            _inc_included('TRAGUIN Support: Dedicated tour managers and 24/7 security control.', 4),
            _inc_included('Welcome Amenities: Customized learning journals, student kits, and bottled water.', 5),
            _inc_included('Complimentary Experience: Prioritized group entry passes at historical locations.', 6),
            _inc_excluded('Interstate flights, airfare, or train tickets to Delhi/ Agra.', 7),
            _inc_excluded('Personal items, laundry, optional drinks, or snacks.', 8),
            _inc_excluded('Monument camera fees, video equipment permits, or insurance.', 9),
            _inc_excluded('Any optional excursions not outlined in the core schedule.', 10),
        ],
    )
    return package, itinerary

def build_up_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UP-010'
    tour_code = 'TRG-UP-010'
    title = 'COMPLETE UP HERITAGE • SPIRITUAL REALMS & NAWABI SPLENDOURS'
    duration = '07 Nights / 08 Days'
    slug = 'up-010-complete-up-heritage-spiritual-realms-nawabi-splendours'
    itin_slug = 'up-010-complete-up-heritage-spiritual-realms-nawabi-splendours-itinerary'
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
            _ph('Serial code UP-010 | TRAGUIN tour code TRG-UP-010', 1),
            _ph('State / Country: Uttar Pradesh / India | Category: Premium Family Tour', 2),
            _ph('Destinations: Varanasi •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van or MUV / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private family boat cruise with traditional flower floating arrangements', 8),
            _ph('Curated by TRAGUIN Experts: Seamless routing across expressways to minimize drive times and', 9),
            _ph('Premium Handpicked Hotels: Properties selected for structural luxury, prime location access, and strict', 10),
            _ph('Luxury Transportation: Elite tourist transport with heavily vetted, experienced, uniform-clad highway', 11)
        ],
        moods=['Family', 'Luxury', 'Culture'],
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
        tagline='COMPLETE UP HERITAGE',
        overview="COMPLETE UP HERITAGE • SPIRITUAL REALMS & NAWABI SPLENDOURS Welcome to an unforgettable voyage of cultural discovery carefully designed and curated by TRAGUIN. Embark on the definitive Uttar Pradesh Family Tour engineered to introduce your loved ones to the breathtaking landscapes, ancient civilizations, sacred rivers, and architectural wonders of Northern India. As your dedicated luxury travel consultants, TRAGUIN crafts an intimate immersion featuring premium stays, seamless transfers, and profoundly emotional storytelling. From the soul-stirring morning chants along the ghats of Varanasi to the grand Nawabi lanes of Lucknow and the iconic, timeless romance of Agra's Taj Mahal, let us mold your vacation into timeless, unforgettable memories.\n\nTOUR OVERVIEW\nThis completely custom-tailored luxury holiday itinerary offers an exceptional tapestry linking India’s most holy spiritual hubs with its grandest royal legacies. Traveling in absolute comfort inside a dedicated private premium luxury vehicle with a personal chauffeur-driven guide, your family will traverse the heartland of India. Featuring a meticulous luxury meal plan encompassing grand daily breakfasts and authentic, multi-course regional dinners, this route represents the finest premium Uttar Pradesh experience. Every single day of your trip is refined with a TRAGUIN curated experience note, guaranteeing priority monument entrance, curated local culinary walks, and expert 24/7 client-facing assistance.\n\nWHY CHOOSE THE BEST UTTAR PRADESH TOUR PACKAGE?\nWhen arranging a Luxury Uttar Pradesh Holiday, meticulous travelers look for deep cultural authenticity paired with contemporary opulence. Uttar Pradesh is home to the most famous attractions and iconic attractions in the world. From Varanasi's ancient spiritual paths—a top tourist place in Uttar Pradesh—to the holy waters of Prayagraj's Triveni Sangam and the newly transformed spiritual golden hub of Ayodhya, the region offers unparalleled depth for an immersive family vacation. For families and newlyweds exploring a tailored Uttar Pradesh Honeymoon Package or Uttar Pradesh Family Tour, the state offers diverse, globally recognized experiences. Capture popular Instagram locations along the vibrant colored river ghats, inside the spectacular Bara Imambara of Lucknow, or under the soft morning light reflecting off the white marble of the Taj Mahal. From traditional shopping for exquisite Banarasi silk sarees and Chikankari garments to tasting legendary street food and watching dramatic evening light and sound shows, our TRAGUIN Uttar Pradesh Packages merge handpicked hotels with exclusive experiences to reveal the ultimate best time to visit Uttar Pradesh.",
        seo_title='UP-010 | COMPLETE UP HERITAGE | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Uttar Pradesh package (UP-010 / TRG-UP-010): Varanasi • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN VARANASI', 1),
            _ih('Day 02: VARANASI & SARNATH EXCURSION', 2),
            _ih('Day 03: VARANASI TO PRAYAGRAJ', 3),
            _ih('Day 04: PRAYAGRAJ TO AYODHYA', 4),
            _ih('Day 05: AYODHYA TO LUCKNOW', 5),
            _ih('Day 06: LUCKNOW TO AGRA', 6),
            _ih('Day 07: AGRA IMPERIAL SIGHTSEEING', 7),
            _ih('Day 08: AGRA TO NEW DELHI / DEPARTURE', 8),
            _ih('TRAGUIN Signature Experience: Private family boat cruise with traditional flower floating arrangements', 9),
            _ih('Curated by TRAGUIN Experts: Seamless routing across expressways to minimize drive times and', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN VARANASI',
                (
                    "WELCOME TO THE WORLD'S OLDEST LIVING CITY – SACRED RIVER AARTI Your premium Uttar Pradesh experience begins upon arrival at Lal Bahadur Shastri Airport or Varanasi Station, where your private luxury transportation vehicle awaits. Check into your premium handpicked hotel and unwind. In the late afternoon, your guide leads you through the sensory, historical labyrinth of old lanes to the ancient riverbanks. Experience a private boat cruise on the Ganges to witness the world-famous Ganga Aarti at Dashashwamedh Ghat—an emotionally moving ritual of fire, chants, and brass lamps that creates unforgettable memories."
                ),
                [
                    'Sightseeing Included: Ganges Private Boat Cruise, Dashashwamedh Ghat Aarti, Kashi Vishwanath Corridor walk.',
                    'Evening Experience: VIP reserved terrace sitting for the spectacular evening oil lamp ceremony.',
                    'Overnight Stay: Varanasi (Premium Riverside or Heritage Palace Hotel)',
                    'Meals Included: Welcome Refreshment & Gourmet Dinner',
                ],
            ),
            _day(
                2,
                'VARANASI & SARNATH EXCURSION',
                (
                    "SUBAH-E-BENARAS & THE CRADLE OF BUDDHIST ENLIGHTENMENT Awake before dawn for 'Subah-e-Benaras'—a majestic morning sunrise boat ride witnessing the breathtaking landscapes of pilgrims bathing against grand sunrise rays. Return for a lavish breakfast at your premium stays, then proceed on an excursion to Sarnath, the peaceful deer park sanctuary where Lord Buddha delivered his monumental first sermon. Explore ancient stupas and the iconic Ashoka Lion Capital museum. Hindu University (BHU)."
                ),
                [
                    'Sightseeing Included: Sunrise Boat Ride, Dhamek Stupa (Sarnath), Sarnath Archaeological Museum, Banaras',
                    'Optional Activities: Private evening interaction with a local classical music maestro in Old Varanasi.',
                    'Overnight Stay: Varanasi (Premium / Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Authentic Satvik Dinner',
                ],
            ),
            _day(
                3,
                'VARANASI TO PRAYAGRAJ',
                (
                    'THE CONFLUENCE OF HOLY RIVERS & MAJESTIC FORTS After breakfast, enjoy a smooth scenic drive in your luxury vehicle to Prayagraj (Allahabad). Head directly to the magnificent Triveni Sangam—the mystical, sacred confluence of the Ganges, Yamuna, and mythical Saraswati rivers. Board a traditional private boat out to the confluence point for a quiet, emotionally grounding family prayer experience. Later, explore the historic Akbar Fort and the beautifully carved Anand Bhawan, the ancestral home of the Nehru family. Museum.'
                ),
                [
                    'Sightseeing Included: Triveni Sangam Boat Excursion, Allahabad Fort, Patalpuri Temple, Anand Bhawan',
                    'Evening Experience: Sunset photography over the grand architectural arches of the New Yamuna Bridge.',
                    'Overnight Stay: Prayagraj (Handpicked Premium Boutique Stay)',
                    'Meals Included: Premium Breakfast & Multi-cuisine Buffet Dinner',
                ],
            ),
            _day(
                4,
                'PRAYAGRAJ TO AYODHYA',
                (
                    'JOURNEY TO THE EPIC LAND OF RAMAYANA Depart today for Ayodhya, the historic and newly revitalized golden city on the banks of the sacred Saryu River. Your premium Uttar Pradesh experience centers around the newly built Shri Ram Janmabhoomi Temple, an architectural marvel carved out of pink sandstone. Walk along the vibrant Ram Ki Paidi ghats, where rows of steps form a beautiful reflection on the water, presenting a popular Instagram location for travelers. Paidi.'
                ),
                [
                    'Sightseeing Included: Shri Ram Janmabhoomi Temple, Hanuman Garhi, Kanak Bhawan Palace Temple, Ram Ki',
                    'Evening Experience: Beautiful sunset Saryu River Aarti followed by traditional bhajan music melodies.',
                    'Overnight Stay: Ayodhya (Premium Selected Luxury Heritage Hotel)',
                    'Meals Included: Premium Breakfast & Traditional Avadhi Vegetarian Dinner',
                ],
            ),
            _day(
                5,
                'AYODHYA TO LUCKNOW',
                (
                    "THE CITY OF NAWABS – ARCHITECTURAL GRANDEUR & ETIQUETTE Drive today to Lucknow, the state capital renowned for its courtly manners, culinary arts, and stunning Mughal-Baroque architecture. Check into your ultra-luxury hotel. In the afternoon, explore the magnificent Bara Imambara, home to the surreal 'Bhool Bhulaiya' (an incredible, complex architectural labyrinth). Your expert guide will reveal stories of the Nawabs while you explore the grand Rumi Darwaza gateway."
                ),
                [
                    'Sightseeing Included: Bara Imambara & Labyrinth, Chhota Imambara, Rumi Darwaza, British Residency Ruins.',
                    'Optional Activities: An elite private evening food tour through Aminabad to taste legendary Galouti Kebabs.',
                    'Overnight Stay: Lucknow (Ultra Luxury Hotel / Heritage Palace Estate)',
                    'Meals Included: Premium Breakfast & Royal Awadhi Nawabi Dinner',
                ],
            ),
            _day(
                6,
                'LUCKNOW TO AGRA',
                (
                    'VIA EXTREME EXPRESSWAY COMFORT TO THE CITY OF ROMANCE Enjoy a lavish morning breakfast before cruising along the smooth, ultra-modern Agra-Lucknow Expressway in your premium vehicle. Arrive in Agra, the world-famous imperial Mughal capital. Check into a luxury resort featuring uninterrupted views of the monument of love. Spend your late afternoon visiting the massive Agra Fort, a UNESCO World Heritage site built in red sandstone that holds deep imperial histories.'
                ),
                [
                    'Sightseeing Included: Agra Fort, Itmad-ud-Daulah (Baby Taj), Yamuna River viewpoints.',
                    'Evening Experience: Sunset viewing of the Taj Mahal from Mehtab Bagh gardens across the river.',
                    'Overnight Stay: Agra (Luxury Resort / Premium View Properties)',
                    'Meals Included: Premium Breakfast & Extravagant Mughlai Dinner',
                ],
            ),
            _day(
                7,
                'AGRA IMPERIAL SIGHTSEEING',
                (
                    'THE SOUL OF THE TAJ MAHAL AT SUNRISE Experience a breathtaking, emotionally moving highlight at dawn as you enter the Taj Mahal under the soft morning light. Witness the white Makrana marble turn from soft pink to golden yellow—an iconic attraction that represents the peak of a luxury holiday. Return to your premium stays for a late breakfast, then visit the fascinating ghost city of Fatehpur Sikri, a marvel of imperial Mughal town planning.'
                ),
                [
                    'Sightseeing Included: Taj Mahal at Sunrise, Fatehpur Sikri Complex, Buland Darwaza Palace.',
                    'Optional Activities: Private marble inlay workshop demonstration with traditional master craftsmen.',
                    'Overnight Stay: Agra (Luxury Resort)',
                    'Meals Included: Premium Breakfast & Grand Farewell Dinner',
                ],
            ),
            _day(
                8,
                'AGRA TO NEW DELHI / DEPARTURE',
                (
                    'CHERISHING THE MEMORIES OF AN EPIC VOYAGE Indulge in a final gourmet breakfast at your luxury resort. Your private luxury transport will safely drive you along the Yamuna Expressway back to New Delhi Airport or Railway Station for your onward journey. Return home carrying a heart full of deep cultural experiences, shared family laughter, and unforgettable memories designed meticulously by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury expressway drop-off directly to Delhi NCR airport/station.',
                    'Meals Included: Lavish Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Radisson Varanasi / Rama Heritage Ayodhya | Lemon Tree Lucknow / Cennet Prayagraj | Howard Plaza The Fern | / similar',
                'Multi-city Uttar Pradesh',
                '7N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Radisson Varanasi / Rama Heritage Ayodhya | Lemon Tree Lucknow / Cennet Prayagraj | Howard Plaza The Fern | / similar',
            ),
            _hotel(
                'Taj Ganges Varanasi / Park Inn Ayodhya | Novotel Lucknow / Welcomheritage Prayagraj | Radisson Hotel Agra / similar',
                'Multi-city Uttar Pradesh',
                '7N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Taj Ganges Varanasi / Park Inn Ayodhya | Novotel Lucknow / Welcomheritage Prayagraj | Radisson Hotel Agra / similar',
            ),
            _hotel(
                'BrijRama Palace / Amatra | Taj Mahal Lucknow / Private | Boutique Estate | Taj Hotel & Convention',
                'Multi-city Uttar Pradesh',
                '7N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: BrijRama Palace / Amatra | Taj Mahal Lucknow / Private | Boutique Estate | Taj Hotel & Convention',
            ),
            _hotel(
                'Nadesar Palace Varanasi | The Grand Hyatt Executive | Palace Suite | The Oberoi Amarvilas | (Taj View Rooms)',
                'Multi-city Uttar Pradesh',
                '7N',
                'Ultra Luxury',
                '(Royal Suite)',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Nadesar Palace Varanasi | The Grand Hyatt Executive | Palace Suite | The Oberoi Amarvilas | (Taj View Rooms)',
            )
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Handpicked stays across historic destinations.', 1),
            _inc_included('Luxury Transportation: Private Chauffeur- driven premium vehicle for the full route.', 2),
            _inc_included('Curated Meal Plan: Daily luxury breakfast and multi-course dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest relations manager tracking the tour.', 4),
            _inc_included('Welcome Amenities: Personalized heritage travel welcome kit and mineral water.', 5),
            _inc_included('Complimentary Experiences: Private boat cruises at Varanasi and Prayagraj Triveni.', 6),
            _inc_excluded('Domestic or International Flights / Inter-state Mainline Train tickets.', 7),
            _inc_excluded('Monument entry tickets, professional inner tour guides, camera permits.', 8),
            _inc_excluded('Personal expenses such as laundry, phone calls, premium beverages, and tips.', 9),
            _inc_excluded('Optional culinary walks or extra temple pooja ceremony materials.', 10),
        ],
    )
    return package, itinerary

UTTAR_PRADESH_UP_002_010_BUILDERS = [
    build_up_002,
    build_up_003,
    build_up_004,
    build_up_005,
    build_up_006,
    build_up_007,
    build_up_008,
    build_up_009,
    build_up_010,
]
